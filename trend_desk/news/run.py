"""Daily News Desk run, on the Mac: read both digests, judge the new items, write the handoff.

  python3 -m trend_desk.news.run              normal run (started by news/mac.py)
  python3 -m trend_desk.news.run --dry-run    build the prompt, call nothing, write nothing
  python3 -m trend_desk.news.run --force      run again even if today's handoff exists

Writes (committed and pushed to main):
  data/news_ledger.json                 every item judged or dropped as noise, and every idea
  trend_desk/news/handoff/<date>.json   today's ideas, which the shared builder turns into work
  trend_desk/news/feeds/roundup.json    roundup items for the Friday roundup prompt
Local only (~/.local/state/news-desk/):
  notes/<date>.md                       the Judge's day notes (they can name her private pitch topics)
  outbox/<stamp>.json                   plain-language problem messages for the News Desk bot
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

from ..research import run as research_run
from ..research import sources as research_sources
from . import judge, rules, sources

DESK = Path(__file__).resolve().parent
REPO = DESK.parents[1]
LEDGER = REPO / "data" / "news_ledger.json"
HANDOFF_DIR = DESK / "handoff"
HOLDS = DESK / "holds.json"
ROUNDUP_FEED = DESK / "feeds" / "roundup.json"
STATE = Path.home() / ".local/state/news-desk"
OUTBOX = STATE / "outbox"
LOOKBACK_DAYS = 3       # items first seen in the last 3 days are eligible the first time they're seen
MAX_CANDIDATES = 120    # a backstop on prompt size, not a quota; a normal day is 20 to 40
READY_ANYWAY_HOUR = 15  # judge once both digests published today, or after 3pm Central regardless

read_json, write_json, slug, chicago_now = (research_run.read_json, research_run.write_json,
                                            research_run.slug, research_run.chicago_now)


def load_ledger() -> dict:
    data = read_json(LEDGER, {})
    for k, v in (("items", {}), ("ideas", {}), ("runs", [])):
        data.setdefault(k, v)
    return data


def outbox(kind: str, text: str) -> None:
    now = chicago_now()
    write_json(OUTBOX / f"{now:%Y%m%d-%H%M%S}-{kind}.json",
               {"created": now.isoformat(timespec="seconds"), "kind": kind, "text": text, "dedupe_key": kind})


def load_all(today: date) -> tuple[list[dict], dict]:
    """Both sources, deduped by link. A source that can't be read is noted, not fatal, unless both fail."""
    items, status = [], {}
    try:
        news = sources.load_news(today, LOOKBACK_DAYS)
        status["news"] = max((i["found"] for i in news), default="")
        items += news
    except Exception as err:  # noqa: BLE001
        status["news"] = f"error: {err}"
    try:
        aw, generated = sources.load_agingwire()
        status["agingwire"] = generated[:10]
        items += aw
    except Exception as err:  # noqa: BLE001
        status["agingwire"] = f"error: {err}"
    if all(str(v).startswith("error") for v in status.values()):
        raise RuntimeError("couldn't fetch either digest")
    seen, out = set(), []
    for it in items:
        lk = sources.link_key(it["url"]) or it["key"]
        if lk in seen:
            continue
        seen.add(lk)
        out.append(it)
    return out, status


def ready(status: dict, now: datetime) -> bool:
    today = now.date().isoformat()
    utc_today = now.astimezone(ZoneInfo("UTC")).date().isoformat()
    fresh = all(str(v)[:10] in (today, utc_today) for v in status.values())
    return fresh or now.hour >= READY_ANYWAY_HOUR


def view(it: dict, today: date) -> dict:
    return {
        "key": it["key"], "kind": it["kind"], "interested_party": rules.interested_party(it),
        "title": it["title"], "summary": it.get("summary", "")[:600], "publisher": it.get("publisher", ""),
        "source": it["source"], "section": it.get("section", ""), "url": it["url"],
        "released": it.get("released", ""), "date_basis": it.get("date_basis", ""),
        "days_old": rules.age_days(it, today), "topics": it.get("topics", []),
        "key_findings": it.get("key_findings", []), "coverage": it.get("coverage", ""),
        "blocked": rules.blocked(it, today), "needs_peg": rules.needs_peg(it, today),
    }


def pick(items: list[dict], data: dict, taken: dict, today: date) -> tuple[list[dict], dict, dict]:
    cutoff = (today - timedelta(days=LOOKBACK_DAYS)).isoformat()
    skipped = {"already judged": 0, "taken elsewhere": 0, "older": 0, "noise": 0}
    pool, by_key = [], {}
    t = today.isoformat()
    for it in items:
        if it["key"] in data["items"]:
            skipped["already judged"] += 1
        elif (it.get("found") or "") < cutoff:
            skipped["older"] += 1
        elif it["key"] in taken or sources.link_key(it["url"]) in taken:
            skipped["taken elsewhere"] += 1
        elif why := rules.noise(it):
            skipped["noise"] += 1
            data["items"][it["key"]] = {"judged_on": t, "status": "dropped", "reason": "noise", "detail": why}
        else:
            pool.append(it)
    pool.sort(key=lambda i: (i["found"], i.get("score") or 0), reverse=True)
    for it in pool[:MAX_CANDIDATES]:
        by_key[it["key"]] = it
    return [view(i, today) for i in pool[:MAX_CANDIDATES]], skipped, by_key


def recent_ideas(data: dict, today: date) -> list[dict]:
    cutoff = (today - timedelta(days=45)).isoformat()
    return [{"id": i, "title": v["title"], "route": v["route"], "created": v["created"], "status": v["status"]}
            for i, v in data["ideas"].items() if v["created"] >= cutoff]


def apply(data: dict, result: dict, cands: list[dict], items: dict, today: date) -> tuple[list, dict]:
    """Record the Judge's answer, enforcing the code rules again."""
    t = today.isoformat()
    by_key = {c["key"]: c for c in cands}
    paused = read_json(HOLDS, {})
    site_slugs = {s["slug"] for s in judge.trend_judge.sites()}
    used, created, dropped = set(), [], {}

    def drop(key, reason, detail=""):
        data["items"][key] = {"judged_on": t, "status": "dropped", "reason": reason,
                              **({"detail": detail} if detail else {})}
        dropped[reason] = dropped.get(reason, 0) + 1

    for idea in result.get("ideas", []):
        keys = [k for k in idea.get("keys", []) if k in by_key and k not in used]
        if not keys:
            continue
        used.update(keys)
        lead, route = by_key[keys[0]], idea["route"]
        site = idea.get("site", "") if route == "brief" else ""
        why_not = lead["blocked"].get(route, "")
        if not why_not and route == "pitch":
            why_not = rules.pitch_problem(idea, [items[k] for k in keys])
            if not why_not and lead["needs_peg"] and not idea.get("other_peg", "").strip():
                why_not = f"released {lead['days_old']} days ago with no other peg"
        if not why_not and route == "roundup" and lead["interested_party"] and len(keys) == 1:
            why_not = "a release's own claim can't be a roundup fact"
        if not why_not and route == "brief" and site not in site_slugs:
            why_not = "brief without a known site"
        if why_not:
            for k in keys:
                drop(k, "rule", f"{route}: {why_not}")
            continue
        iid = f"nd-{t}-{slug(idea['title'])}"
        n = 2
        while iid in data["ideas"]:
            iid = f"nd-{t}-{slug(idea['title'], 46)}-{n}"
            n += 1
        status = "paused" if (route in paused or f"{route}:{site}" in paused) else "routed"
        item_views = [{k: by_key[x][k] for k in ("key", "kind", "interested_party", "title", "publisher", "url",
                                                  "released", "date_basis", "days_old", "source", "summary")}
                      for x in keys]
        standout = bool(idea.get("standout")) and route == "pitch" and not idea.get("primary_test", "").strip()
        record = {
            "desk": "news", "title": idea["title"], "created": t, "route": route,
            "speed": f"released {lead['days_old']} days ago", "beat": idea.get("beat", ""),
            "angle": idea.get("angle", ""), "why_now": idea.get("why_now", ""), "is_it_real": idea.get("is_it_real", ""),
            "primary_test": idea.get("primary_test", ""), "standout": standout,
            "standout_reason": idea.get("standout_reason", "") if standout else "",
            "needs_independent_test": standout, "other_peg": idea.get("other_peg", ""),
            "audience": idea.get("audience", ""), "evidence_strength": idea.get("evidence_strength", ""),
            "confidence": idea.get("confidence", ""), "site": site,
            "seed_keyword": idea.get("seed_keyword", "") if route == "brief" else "",
            "keys": keys, "items": item_views, "evidence": [v["url"] for v in item_views if v["url"]],
            "term_details": [], "status": status,
        }
        data["ideas"][iid] = record
        created.append({"id": iid, **record})
        for k in keys:
            data["items"][k] = {"judged_on": t, "status": "kept", "idea": iid}
    reasons = {d["key"]: d["reason"] for d in result.get("drops", [])}
    passed = data.setdefault("passed_over", {})
    for k in by_key:
        if k in used:
            continue
        if k in reasons:
            drop(k, reasons[k])
        elif passed.get(k):
            drop(k, "not-selected")
        else:  # the Judge didn't mention it; it gets one more look on the next run
            passed[k] = t
            dropped["unanswered"] = dropped.get("unanswered", 0) + 1
    for k in list(passed):
        if k in data["items"]:
            passed.pop(k)
    return created, dropped


def write_roundup_feed(data: dict, today: date) -> None:
    """News items for the Friday roundup prompt (~/.claude/scripts/female-model-roundup-prompt.md)."""
    decisions = read_json(DESK / "feedback" / "decisions.json", [])
    skipped = {d.get("idea_id") for d in decisions if d.get("action") == "skip"}
    cutoff = (today - timedelta(days=21)).isoformat()
    items = [{"id": i, "title": v["title"], "created": v["created"], "angle": v["angle"], "why_now": v["why_now"],
              "is_it_real": v["is_it_real"], "evidence": v["evidence"],
              "items": [{k: x.get(k) for k in ("kind", "publisher", "released", "url")} for x in v["items"]]}
             for i, v in sorted(data["ideas"].items(), key=lambda kv: kv[1]["created"], reverse=True)
             if v["route"] == "roundup" and v["created"] >= cutoff and i not in skipped]
    write_json(ROUNDUP_FEED, {"updated": today.isoformat(), "items": items})


def problem_text(err: Exception) -> tuple[str, str]:
    s = str(err).lower()
    if "fetch" in s or "curl" in s:
        return ("News Desk couldn't read the news digest or AgingWire today, so nothing was judged. "
                "It tries again on the next run.", "fetch")
    if "usage" in s or "limit" in s:
        return ("News Desk hit the Claude usage limit today and skipped judging. It tries again later; "
                "nothing needs doing unless this repeats.", "limit")
    return ("News Desk's daily judging failed, so no news ideas were routed. "
            "~/Library/Logs/news-desk/judge.log has the details.", "judge-failed")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--wait-ready", action="store_true", help="exit quietly if the digests haven't published yet")
    args = ap.parse_args()

    now = chicago_now()
    today = now.date()
    handoff = HANDOFF_DIR / f"{today.isoformat()}.json"
    if handoff.exists() and not args.force and not args.dry_run:
        print(f"News Desk: today's handoff already exists ({handoff.name}).")
        return 0
    try:
        items, status = load_all(today)
    except Exception as err:  # noqa: BLE001
        print(f"News Desk: couldn't load the digests: {err}")
        if not args.wait_ready:
            outbox(*problem_text(err)[::-1])
        return 1
    if args.wait_ready and not ready(status, now):
        print(f"News Desk: digests haven't both published today yet ({status}); waiting.")
        return 0

    data = load_ledger()
    cands, skipped, by_key = pick(items, data, sources.taken_keys(), today)
    print(f"News Desk: {len(items)} items, {len(cands)} to judge; skipped {skipped}; sources {status}.")
    run = {"date": today.isoformat(), "items": len(items), "candidates": len(cands), "skipped": skipped,
           "sources": {k: (v if not str(v).startswith("error") else "error") for k, v in status.items()},
           "model": judge.MODEL}
    if not cands:
        if args.dry_run:
            print("Dry run: nothing to judge, nothing written.")
            return 0
        run.update(ideas=0)
        data["runs"].append(run)
        write_json(LEDGER, data)
        write_json(handoff, {"date": today.isoformat(), "ideas": [], "notes": "No new items cleared the bar."})
        return 0

    text = judge.prompt(today.isoformat(), cands, recent_ideas(data, today), research_sources.pitched_topics(),
                        research_sources.trending_now(today))
    if args.dry_run:
        out = REPO / "outputs" / "trend_desk" / "news_dry_run_prompt.md"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text)
        print(f"Dry run: prompt written to {out.relative_to(REPO)} ({len(text):,} chars). Nothing saved.")
        return 0

    try:
        result = judge.judge(text)
    except Exception as err:  # noqa: BLE001
        print(f"News Desk: judging failed: {err}")
        msg, key = problem_text(err)
        outbox(key, msg)
        run.update(error=key)
        data["runs"].append(run)
        write_json(LEDGER, data)
        return 1

    created, dropped = apply(data, result, cands, by_key, today)
    routes = {}
    for c in created:
        routes[c["route"]] = routes.get(c["route"], 0) + 1
    notes = STATE / "notes" / f"{today.isoformat()}.md"
    notes.parent.mkdir(parents=True, exist_ok=True)
    with open(notes, "a") as f:
        f.write(f"{result.get('notes', '')}\n")
    run.update(ideas=len(created), routes=routes, dropped=dropped)
    data["runs"].append(run)
    data["runs"] = data["runs"][-400:]
    write_json(LEDGER, data)
    if handoff.exists():
        earlier = read_json(handoff, {}).get("ideas", [])
        created = [i for i in earlier if i["id"] not in {c["id"] for c in created}] + created
    write_json(handoff, {"date": today.isoformat(), "ideas": created, "dropped": dropped})
    write_roundup_feed(data, today)
    print(f"News Desk: {len(created)} ideas {routes}, dropped {dropped}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
