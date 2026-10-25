"""Daily Trend Desk run: collect signals, judge them, route the ideas, write the handoffs.

  python -m trend_desk.run              normal daily run (GitHub Actions, after the pipeline)
  python -m trend_desk.run --dry-run    collect and build the prompt, but don't call Claude
  python -m trend_desk.run --force      run again even if today's handoff exists

Writes (all committed by .github/workflows/run-trend-desk.yml):
  data/trend_ledger.json                the memory (see ledger.py)
  trend_desk/handoff/<date>.json        today's ideas, which the Mac builder turns into work
  trend_desk/feeds/roundup.json         rolling roundup items for the Friday outline job
  trend_desk/outbox/<stamp>-<kind>.json Telegram messages the Mac bot delivers (problems only;
                                        the Mac sends the "what was built" message itself)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo

from . import collect, judge, ledger

DESK = ledger.ROOT / "trend_desk"
HANDOFF_DIR = DESK / "handoff"
OUTBOX = DESK / "outbox"
ROUNDUP_FEED = DESK / "feeds" / "roundup.json"
FEEDBACK = DESK / "feedback" / "outcomes.json"
MAX_TERMS = 300
SPEED_RANK = {"exploding": 0, "emerging": 1, "new": 2, "steady": 3}


def chicago_now() -> datetime:
    return datetime.now(ZoneInfo("America/Chicago"))


def slug(text: str, n: int = 50) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:n].rstrip("-")


def outbox(kind: str, text: str, dedupe_key: str = "") -> None:
    OUTBOX.mkdir(parents=True, exist_ok=True)
    now = chicago_now()
    msg = {"id": f"{now:%Y%m%d-%H%M%S}-{kind}", "created": now.isoformat(timespec="seconds"),
           "kind": kind, "text": text, "dedupe_key": dedupe_key or kind}
    (OUTBOX / f"{msg['id']}.json").write_text(json.dumps(msg, indent=1) + "\n")


def problem_text(err: Exception) -> tuple[str, str]:
    """Plain-language problem line plus a dedupe key. Never forwards raw error text."""
    s = f"{type(err).__name__} {err}".lower()
    if "credit balance" in s or "billing" in s:
        return ("Trend Desk couldn't judge today's trends: the Claude API account is out of credit. "
                "No new pitches, outlines or briefs will come from trends until it's topped up "
                "(console.anthropic.com, Billing).", "credit")
    if "authentication" in s or "api key" in s or "401" in s:
        return ("Trend Desk couldn't judge today's trends: the Claude API key in GitHub isn't working. "
                "Nothing new will be built from trends until the ANTHROPIC_API_KEY secret is fixed.", "auth")
    if "rate" in s and "limit" in s:
        return ("Trend Desk hit the Claude API rate limit today and skipped judging. It tries again "
                "tomorrow; nothing needs doing unless this repeats.", "rate-limit")
    return ("Trend Desk's daily judging failed today, so no new trend ideas were routed. The GitHub "
            "Actions log for 'Run Trend Desk' has the details.", "judge-failed")


def pick_due(data: dict, today: date) -> dict:
    keys = ledger.due_for_judging(data, today)

    def rank(k):
        e = data["terms"][k]
        best = max((s.get("score") or 0) for s in e["sightings"]) if e["sightings"] else 0
        return (SPEED_RANK[ledger.speed(e, today)], -len(ledger.sources(e)), -best)

    keys.sort(key=rank)
    return {k: ledger.summary(data["terms"][k], today) for k in keys[:MAX_TERMS]}


def feedback_summary() -> dict:
    if not FEEDBACK.exists():
        return {}
    try:
        return json.loads(FEEDBACK.read_text()).get("summary", {})
    except json.JSONDecodeError:
        return {}


def apply_verdicts(data: dict, result: dict, due: dict, today: date) -> list[dict]:
    t = today.isoformat()
    paused = judge.holds()
    site_slugs = {s["slug"] for s in judge.sites()}
    created = []
    used = set()
    for idea in result.get("ideas", []):
        keys = [k for k in idea.get("term_keys", []) if k in due and k not in used]
        if not keys:
            continue
        used.update(keys)
        speeds = [ledger.speed(data["terms"][k], today) for k in keys]
        speed = min(speeds, key=lambda s: SPEED_RANK[s])
        existing = idea.get("existing_idea_id") or ""
        if existing in data["ideas"]:
            target = data["ideas"][existing]
            target["terms"] = sorted(set(target["terms"]) | set(keys))
            ledger.log_event(target, t, "new-signal", ", ".join(data["terms"][k]["term"] for k in keys))
            iid = existing
        else:
            route = idea["route"]
            site = idea.get("site") or ""
            if route == "brief" and site not in site_slugs:
                route, site = "roundup", ""  # a brief needs a real site; keep the idea, demote it
            iid = f"{t}-{slug(idea['title'])}"
            n = 2
            while iid in data["ideas"]:
                iid = f"{t}-{slug(idea['title'], 46)}-{n}"
                n += 1
            hold_key = f"{route}:{site}" if site else route
            status = "paused" if (route in paused or hold_key in paused) else "routed"
            record = {
                "title": idea["title"], "created": t, "route": route, "speed": speed,
                "beat": idea.get("beat", ""), "angle": idea.get("angle", ""), "why_now": idea.get("why_now", ""),
                "is_it_real": idea.get("is_it_real", ""), "confidence": idea.get("confidence", ""),
                "evidence": [u for u in idea.get("evidence", []) if u.startswith("http")][:6],
                "terms": keys, "site": site, "seed_keyword": idea.get("seed_keyword", "") if route == "brief" else "",
                "status": status, "history": [],
            }
            ledger.log_event(record, t, status, route + (f":{site}" if site else ""))
            data["ideas"][iid] = record
            created.append({"id": iid, **record,
                            "term_details": [ledger.summary(data["terms"][k], today) for k in keys]})
        for k in keys:
            e = data["terms"][k]
            e.update(status="kept", idea=iid, drop_reason=None, judged_on=t)
    reasons = {d["key"]: d["reason"] for d in result.get("drops", []) if d.get("key") in due}
    for k in due:
        if k in used:
            continue
        reason = reasons.get(k, "not-selected")
        data["terms"][k].update(status="held" if reason == "watch" else "dropped",
                                drop_reason=reason, judged_on=t, idea=None)
    return created


def write_roundup_feed(data: dict, today: date) -> None:
    cutoff = (today - timedelta(days=21)).isoformat()
    items = [{"id": i, "title": v["title"], "created": v["created"], "angle": v["angle"],
              "why_now": v["why_now"], "is_it_real": v["is_it_real"], "evidence": v["evidence"],
              "terms": [data["terms"][k]["term"] for k in v["terms"] if k in data["terms"]],
              "status": v["status"]}
             for i, v in sorted(data["ideas"].items(), key=lambda kv: kv[1]["created"], reverse=True)
             if v["route"] == "roundup" and v["created"] >= cutoff and v["status"] not in ("skipped", "rerouted")]
    ROUNDUP_FEED.parent.mkdir(parents=True, exist_ok=True)
    ROUNDUP_FEED.write_text(json.dumps({"updated": today.isoformat(), "items": items}, indent=1,
                                       ensure_ascii=False) + "\n")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--backfill", action="store_true", help="re-read every historical scan into the ledger")
    args = ap.parse_args()

    today = chicago_now().date()
    handoff = HANDOFF_DIR / f"{today.isoformat()}.json"
    if handoff.exists() and not args.force and not args.dry_run:
        print(f"Trend Desk: today's handoff already exists ({handoff.name}). Use --force to rerun.")
        return 0

    data = ledger.load()
    got = collect.collect_all(data, today, backfill=args.backfill)
    due = pick_due(data, today)
    print(f"Trend Desk: collected {got['counts']} since {got['since']}; {len(due)} terms due for judging.")

    run = {"date": today.isoformat(), "collected": got["counts"], "due": len(due), "model": judge.MODEL}
    if not due:
        run.update(ideas=0, dropped=0, cost_usd=0)
        data["runs"].append(run)
        ledger.save(data)
        write_roundup_feed(data, today)
        HANDOFF_DIR.mkdir(parents=True, exist_ok=True)
        handoff.write_text(json.dumps({"date": today.isoformat(), "ideas": [], "notes": "No new terms."}, indent=1) + "\n")
        return 0

    system = judge.system_prompt()
    user = judge.user_prompt(today.isoformat(), due, got["context"],
                             ledger.recent_ideas(data, today), feedback_summary())
    if args.dry_run:
        out = ledger.ROOT / "outputs" / "trend_desk" / "dry_run_prompt.md"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(f"# SYSTEM\n\n{system}\n\n# USER\n\n{user}")
        print(f"Dry run: prompt written to {out.relative_to(ledger.ROOT)} ({len(system) + len(user):,} chars). "
              "Ledger not saved.")
        return 0

    try:
        result, usd = judge.judge(system, user)
    except Exception as err:  # noqa: BLE001 - every failure becomes one plain-language alert
        text, key = problem_text(err)
        print(f"Trend Desk: judging failed: {type(err).__name__}")
        outbox("problem", text, key)
        run.update(error=key)
        data["runs"].append(run)
        ledger.save(data)  # keep what was collected; those terms stay pending for tomorrow
        return 1

    created = apply_verdicts(data, result, due, today)
    routes = {}
    for c in created:
        routes[c["route"]] = routes.get(c["route"], 0) + 1
    dropped = sum(1 for k in due if data["terms"][k]["status"] == "dropped")
    run.update(ideas=len(created), routes=routes, dropped=dropped,
               watching=sum(1 for k in due if data["terms"][k]["status"] == "held"),
               cost_usd=usd, notes=result.get("notes", ""))
    data["runs"].append(run)
    ledger.save(data)
    write_roundup_feed(data, today)
    HANDOFF_DIR.mkdir(parents=True, exist_ok=True)
    handoff.write_text(json.dumps({"date": today.isoformat(), "ideas": created, "dropped": dropped,
                                   "watching": run["watching"], "notes": result.get("notes", ""),
                                   "cost_usd": usd}, indent=1, ensure_ascii=False) + "\n")
    print(f"Trend Desk: {len(created)} ideas {routes}, {dropped} dropped, ${usd:.2f}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
