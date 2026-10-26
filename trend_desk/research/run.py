"""Daily Research Desk run, on the Mac: read the dashboard, judge the new studies, write the handoff.

  python3 -m trend_desk.research.run              normal run (started by research/mac.py)
  python3 -m trend_desk.research.run --dry-run    build the prompt, call nothing, write nothing
  python3 -m trend_desk.research.run --force      run again even if today's handoff exists

Writes (committed and pushed to main):
  data/research_ledger.json                 every PMID judged, and every idea, so nothing is judged twice
  trend_desk/research/handoff/<date>.json   today's ideas, which the shared builder turns into work
Local only (~/.local/state/research-desk/):
  notes/<date>.md                           the Judge's day notes (they can name her private pitch topics)
  outbox/<stamp>.json                       plain-language problem messages for the research bot
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

from . import judge, rules, sources

DESK = Path(__file__).resolve().parent
REPO = DESK.parents[1]
LEDGER = REPO / "data" / "research_ledger.json"
HANDOFF_DIR = DESK / "handoff"
HOLDS = DESK / "holds.json"
ROUNDUP_FEED = DESK / "feeds" / "roundup.json"
STATE = Path.home() / ".local/state/research-desk"
OUTBOX = STATE / "outbox"
MIN_SCORE = 7          # the dashboard's top-picks default
LOOKBACK_DAYS = 3      # studies found in the last 3 days are eligible the first time they're seen
MAX_CANDIDATES = 150    # a backstop on prompt size, not a quota; a normal day is 20 to 50
READY_SOURCES = 8      # judge once this many digests have published today ...
READY_ANYWAY_HOUR = 14  # ... or after 2pm Central regardless


def chicago_now() -> datetime:
    return datetime.now(ZoneInfo("America/Chicago"))


def slug(text: str, n: int = 50) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:n].rstrip("-")


def read_json(path: Path, default):
    try:
        return json.loads(path.read_text())
    except (OSError, json.JSONDecodeError):
        return default


def write_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n")
    tmp.replace(path)


def load_ledger() -> dict:
    data = read_json(LEDGER, {})
    for k, v in (("studies", {}), ("ideas", {}), ("runs", [])):
        data.setdefault(k, v)
    return data


def outbox(kind: str, text: str) -> None:
    now = chicago_now()
    write_json(OUTBOX / f"{now:%Y%m%d-%H%M%S}-{kind}.json",
               {"created": now.isoformat(timespec="seconds"), "kind": kind, "text": text, "dedupe_key": kind})


def problem_text(err: Exception) -> tuple[str, str]:
    """Plain-language line plus a dedupe key. Never forwards raw error text."""
    s = str(err).lower()
    if "fetch" in s or "curl" in s:
        return ("Research Desk couldn't read the research dashboard today, so no studies were judged. "
                "It tries again on the next run.", "fetch")
    if "usage" in s or "limit" in s:
        return ("Research Desk hit the Claude usage limit today and skipped judging. It tries again "
                "later; nothing needs doing unless this repeats.", "limit")
    return ("Research Desk's daily judging failed, so no new research ideas were routed. "
            "~/Library/Logs/research-desk/judge.log has the details.", "judge-failed")


def digests_ready(updated: dict, now: datetime) -> bool:
    today_utc = now.astimezone(ZoneInfo("UTC")).date().isoformat()
    fresh = sum(1 for v in updated.values() if str(v).startswith(today_utc))
    return fresh >= READY_SOURCES or now.hour >= READY_ANYWAY_HOUR


def view(s: dict, today: date) -> dict:
    """What the Judge sees for one study."""
    days, verified = rules.age_days(s, today)
    angle = (s.get("pitch_angles") or [{}])[0] if isinstance(s.get("pitch_angles"), list) else {}
    cav = s.get("caveats") or ""
    return {
        "pmid": s["pmid"], "headline": s.get("headline", ""), "journal": s.get("journal", ""),
        "digests": s.get("digests", []), "days_online": days, "date_verified": verified,
        "score": s.get("relevance_score"), "score_reason": (s.get("relevance_score_reason") or "")[:300],
        "groundbreaking": s.get("groundbreaking", ""), "why_it_matters": (s.get("why_it_matters") or "")[:400],
        "summary": (s.get("summary") or "")[:700],
        "caveats": cav if isinstance(cav, str) else "; ".join(map(str, cav)),
        "fact_check_note": (s.get("fact_check_note") or "")[:400],
        "coverage": s.get("media_coverage", ""),
        "digest_pitch_angle": {"headline": angle.get("headline", ""), "hook": angle.get("hook", "")},
        "flags": [k for k, v in rules.flags(s).items() if v],
        "blocked": rules.blocked(s, today), "needs_peg": rules.needs_peg(s, today),
    }


def pick(studies: dict, data: dict, taken: dict, today: date) -> tuple[list[dict], dict]:
    cutoff = (today - timedelta(days=LOOKBACK_DAYS)).isoformat()
    skipped = {"already judged": 0, "taken elsewhere": 0, "below score": 0, "older": 0}
    pool = []
    for pmid, s in studies.items():
        if pmid in data["studies"]:
            skipped["already judged"] += 1
        elif (s.get("run_date") or "") < cutoff:
            skipped["older"] += 1
        elif (s.get("relevance_score") or 0) < MIN_SCORE:
            skipped["below score"] += 1
        elif pmid in taken:
            skipped["taken elsewhere"] += 1
        else:
            pool.append(s)
    pool.sort(key=lambda s: (s.get("relevance_score") or 0, s.get("run_date", "")), reverse=True)
    return [view(s, today) for s in pool[:MAX_CANDIDATES]], skipped


def recent_ideas(data: dict, today: date) -> list[dict]:
    cutoff = (today - timedelta(days=45)).isoformat()
    return [{"id": i, "title": v["title"], "route": v["route"], "created": v["created"],
             "status": v["status"], "pmids": v["pmids"]}
            for i, v in data["ideas"].items() if v["created"] >= cutoff]


def apply(data: dict, result: dict, cands: list[dict], studies: dict, today: date) -> tuple[list, dict]:
    t = today.isoformat()
    by_pmid = {c["pmid"]: c for c in cands}
    paused = read_json(HOLDS, {})
    site_slugs = {s["slug"] for s in judge.trend_judge.sites()}
    used, created, dropped = set(), [], {}

    def drop(pmid, reason, detail=""):
        data["studies"][pmid] = {"judged_on": t, "status": "dropped", "reason": reason,
                                 **({"detail": detail} if detail else {})}
        dropped[reason] = dropped.get(reason, 0) + 1

    for idea in result.get("ideas", []):
        pmids = [p for p in idea.get("pmids", []) if p in by_pmid and p not in used]
        if not pmids:
            continue
        used.update(pmids)
        lead, route = by_pmid[pmids[0]], idea["route"]
        site = idea.get("site", "") if route == "brief" else ""
        why_not = lead["blocked"].get(route, "")
        if not why_not and route == "pitch" and lead["needs_peg"] and not idea.get("other_peg", "").strip():
            why_not = f"online {lead['days_online']} days ago with no other peg"
        if not why_not and route == "brief" and site not in site_slugs:
            why_not = "brief without a known site"
        if why_not:
            for p in pmids:
                drop(p, "rule", f"{route}: {why_not}")
            continue
        iid = f"rd-{t}-{slug(idea['title'])}"
        n = 2
        while iid in data["ideas"]:
            iid = f"rd-{t}-{slug(idea['title'], 46)}-{n}"
            n += 1
        status = "paused" if (route in paused or f"{route}:{site}" in paused) else "routed"
        study_views = []
        for p in pmids:
            s, v = studies[p], by_pmid[p]
            study_views.append({
                "pmid": p, "doi": s.get("doi", ""), "journal": s.get("journal", ""),
                "headline": s.get("headline", ""), "pubdate": s.get("pubdate", ""),
                "days_online": v["days_online"], "date_verified": v["date_verified"],
                "digests": v["digests"], "score": v["score"], "caveats": v["caveats"],
                "fact_check_note": v["fact_check_note"], "coverage": v["coverage"], "flags": v["flags"],
            })
        evidence = []
        for s in study_views:
            evidence.append(f"https://pubmed.ncbi.nlm.nih.gov/{s['pmid']}/")
            if s["doi"]:
                evidence.append(f"https://doi.org/{s['doi']}")
        days = lead["days_online"]
        record = {
            "desk": "research", "title": idea["title"], "created": t, "route": route,
            "speed": f"online {days} days" + ("" if lead["date_verified"] else " (unverified)"),
            "beat": idea.get("beat", ""), "angle": idea.get("angle", ""), "why_now": idea.get("why_now", ""),
            "is_it_real": idea.get("is_it_real", ""), "evidence_strength": idea.get("evidence_strength", ""),
            "other_peg": idea.get("other_peg", ""), "audience": idea.get("audience", ""),
            "confidence": idea.get("confidence", ""), "site": site,
            "seed_keyword": idea.get("seed_keyword", "") if route == "brief" else "",
            "pmids": pmids, "studies": study_views, "evidence": evidence, "term_details": [],
            "status": status,
        }
        data["ideas"][iid] = record
        created.append({"id": iid, **record})
        for p in pmids:
            data["studies"][p] = {"judged_on": t, "status": "kept", "idea": iid}
    reasons = {d["pmid"]: d["reason"] for d in result.get("drops", [])}
    passed = data.setdefault("passed_over", {})
    for p in by_pmid:
        if p in used:
            continue
        if p in reasons:
            drop(p, reasons[p])
        elif passed.get(p):  # left out without a reason twice: record it so it isn't judged forever
            drop(p, "not-selected")
        else:  # the Judge didn't mention it; it gets one more look on the next run
            passed[p] = t
            dropped["unanswered"] = dropped.get("unanswered", 0) + 1
    for p in list(passed):
        if p in data["studies"]:
            passed.pop(p)
    return created, dropped


def write_roundup_feed(data: dict, today: date) -> None:
    """Research items for the Friday roundup prompt (~/.claude/scripts/female-model-roundup-prompt.md),
    which reads this next to Trend Desk's feed and lists the ids it considered, so nothing repeats."""
    decisions = read_json(DESK / "feedback" / "decisions.json", [])
    skipped = {d.get("idea_id") for d in decisions if d.get("action") == "skip"}
    cutoff = (today - timedelta(days=21)).isoformat()
    items = [{"id": i, "title": v["title"], "created": v["created"], "angle": v["angle"], "why_now": v["why_now"],
              "is_it_real": v["is_it_real"], "evidence": v["evidence"],
              "studies": [{k: st.get(k) for k in ("pmid", "journal", "caveats", "days_online")} for st in v["studies"]]}
             for i, v in sorted(data["ideas"].items(), key=lambda kv: kv[1]["created"], reverse=True)
             if v["route"] == "roundup" and v["created"] >= cutoff and i not in skipped]
    write_json(ROUNDUP_FEED, {"updated": today.isoformat(), "items": items})


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
        print(f"Research Desk: today's handoff already exists ({handoff.name}).")
        return 0
    try:
        studies, updated = sources.load_studies()
    except Exception as err:  # noqa: BLE001
        print(f"Research Desk: couldn't load the dashboard: {err}")
        if not args.wait_ready:
            outbox(*problem_text(err)[::-1])
        return 1
    if args.wait_ready and not digests_ready(updated, now):
        print("Research Desk: digests haven't published today yet; waiting.")
        return 0

    data = load_ledger()
    taken = sources.taken_pmids()
    cands, skipped = pick(studies, data, taken, today)
    print(f"Research Desk: {len(studies)} studies on the dashboard, {len(cands)} to judge; skipped {skipped}.")
    run = {"date": today.isoformat(), "studies": len(studies), "candidates": len(cands), "skipped": skipped,
           "model": judge.MODEL}

    if not cands:
        if args.dry_run:
            print("Dry run: nothing to judge, nothing written.")
            return 0
        run.update(ideas=0)
        data["runs"].append(run)
        write_json(LEDGER, data)
        write_json(handoff, {"date": today.isoformat(), "ideas": [], "notes": "No new studies cleared the bar."})
        return 0

    text = judge.prompt(today.isoformat(), cands, recent_ideas(data, today), sources.pitched_topics(),
                        sources.trending_now(today))
    if args.dry_run:
        out = REPO / "outputs" / "trend_desk" / "research_dry_run_prompt.md"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text)
        print(f"Dry run: prompt written to {out.relative_to(REPO)} ({len(text):,} chars). Nothing saved.")
        return 0

    try:
        result = judge.judge(text)
    except Exception as err:  # noqa: BLE001 - every failure becomes one plain-language message
        print(f"Research Desk: judging failed: {err}")
        key, msg = problem_text(err)[1], problem_text(err)[0]
        outbox(key, msg)
        run.update(error=key)
        data["runs"].append(run)
        write_json(LEDGER, data)  # the studies stay unjudged, so tomorrow picks them up
        return 1

    created, dropped = apply(data, result, cands, studies, today)
    routes = {}
    for c in created:
        routes[c["route"]] = routes.get(c["route"], 0) + 1
    # The Judge's notes can name topics from her private pitch ledgers, so they stay on the Mac.
    notes = STATE / "notes" / f"{today.isoformat()}.md"
    notes.parent.mkdir(parents=True, exist_ok=True)
    with open(notes, "a") as f:
        f.write(f"{result.get('notes', '')}\n")
    run.update(ideas=len(created), routes=routes, dropped=dropped)
    data["runs"].append(run)
    data["runs"] = data["runs"][-400:]
    write_json(LEDGER, data)
    if handoff.exists():  # a forced rerun adds to the day's ideas; it never drops earlier ones
        earlier = read_json(handoff, {}).get("ideas", [])
        created = [i for i in earlier if i["id"] not in {c["id"] for c in created}] + created
    write_json(handoff, {"date": today.isoformat(), "ideas": created, "dropped": dropped})
    write_roundup_feed(data, today)
    print(f"Research Desk: {len(created)} ideas {routes}, dropped {dropped}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
