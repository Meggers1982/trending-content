"""The trend ledger: every term the radars have surfaced, every idea the Judge made of them.

data/trend_ledger.json is the Judge's memory. Without it each radar scan stands alone and
nothing can tell a one-week spike from a term that has been climbing for a month. Shape:

  terms[key]  one entry per normalized search term
      term, first_seen, last_seen, sightings[{date, source, profile, stage, score, opportunity}],
      status (pending | kept | dropped | held), idea, drop_reason, judged_on
  ideas[id]   one entry per story idea the Judge kept
      title, created, route, speed, beat, angle, why_now, is_it_real, evidence, terms,
      site, seed_keyword, status, history[{date, event, detail}]
  runs[]      one line per Judge run (counts and cost), newest last

Speed is computed here, in code, from the sightings, so it can't drift with the model:
  exploding  first seen in the last 7 days and flagged breakout/emerging, or seen by 2+ sources
  emerging   seen in 3+ different weeks, the latest within the last 14 days
  new        first seen in the last 7 days, no strong signal yet
  steady     everything else
"""
from __future__ import annotations

import json
import re
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEDGER = ROOT / "data" / "trend_ledger.json"
MAX_SIGHTINGS = 60
MAX_RUNS = 120
STRONG_STAGES = {"breakout", "emerging"}


def key_for(term: str) -> str:
    k = re.sub(r"[^a-z0-9]+", " ", term.lower()).strip()
    return k[:120]


def load() -> dict:
    if LEDGER.exists():
        data = json.loads(LEDGER.read_text())
    else:
        data = {}
    data.setdefault("version", 1)
    data.setdefault("terms", {})
    data.setdefault("ideas", {})
    data.setdefault("runs", [])
    return data


def save(data: dict) -> None:
    data["runs"] = data["runs"][-MAX_RUNS:]
    LEDGER.parent.mkdir(parents=True, exist_ok=True)
    LEDGER.write_text(json.dumps(data, indent=1, sort_keys=True, ensure_ascii=False) + "\n")


def add_sighting(data: dict, term: str, when: str, source: str, profile: str = "",
                 stage: str = "", score=None, opportunity=None) -> str:
    """Record that `source` saw `term` on `when`. Returns the term key. Idempotent per
    (date, source, profile), so re-reading the same scan file changes nothing."""
    key = key_for(term)
    if not key:
        return ""
    entry = data["terms"].setdefault(key, {
        "term": term.strip(), "first_seen": when, "last_seen": when, "sightings": [],
        "status": "pending", "idea": None, "drop_reason": None, "judged_on": None,
    })
    sig = {"date": when, "source": source, "profile": profile, "stage": (stage or "").lower(),
           "score": score, "opportunity": opportunity}
    if not any(s["date"] == when and s["source"] == source and s["profile"] == profile
               for s in entry["sightings"]):
        entry["sightings"].append(sig)
        entry["sightings"].sort(key=lambda s: s["date"])
        entry["sightings"] = entry["sightings"][-MAX_SIGHTINGS:]
    entry["first_seen"] = min(entry["first_seen"], when)
    entry["last_seen"] = max(entry["last_seen"], when)
    return key


def weeks_seen(entry: dict) -> list[str]:
    weeks = {date.fromisoformat(s["date"]).isocalendar()[:2] for s in entry["sightings"]}
    return [f"{y}-W{w:02d}" for y, w in sorted(weeks)]


def sources(entry: dict) -> set[str]:
    return {s["source"] for s in entry["sightings"]}


def speed(entry: dict, today: date) -> str:
    first = date.fromisoformat(entry["first_seen"])
    last = date.fromisoformat(entry["last_seen"])
    if len(weeks_seen(entry)) >= 3 and (today - last).days <= 14:
        return "emerging"
    if (today - first).days <= 7:
        recent = [s for s in entry["sightings"] if (today - date.fromisoformat(s["date"])).days <= 7]
        if any(s["stage"] in STRONG_STAGES for s in recent) or len({s["source"] for s in recent}) >= 2:
            return "exploding"
        return "new"
    return "steady"


def summary(entry: dict, today: date) -> dict:
    """The compact view of a term the Judge sees."""
    recent = entry["sightings"][-6:]
    return {
        "term": entry["term"],
        "speed": speed(entry, today),
        "first_seen": entry["first_seen"],
        "weeks_seen": len(weeks_seen(entry)),
        "sources": sorted(sources(entry)),
        "profiles": sorted({s["profile"] for s in entry["sightings"] if s["profile"]}),
        "recent": [{k: v for k, v in s.items() if v not in (None, "")} for s in recent],
        "previous_verdict": entry["status"] if entry["status"] != "pending" else None,
        "previous_reason": entry.get("drop_reason"),
    }


def log_event(idea: dict, when: str, event: str, detail: str = "") -> None:
    idea.setdefault("history", []).append({"date": when, "event": event, "detail": detail})


def due_for_judging(data: dict, today: date) -> list[str]:
    """Terms the Judge should look at today.

    A term is judged once when it first turns up. After that it comes back only when its
    picture changes: a dropped or held term is re-judged if it has been seen again since
    and has since become `emerging`, or if 30 days have passed since its verdict."""
    out = []
    for key, entry in data["terms"].items():
        last = date.fromisoformat(entry["last_seen"])
        if (today - last).days > 7:
            continue
        if entry["status"] == "pending":
            out.append(key)
            continue
        if entry["status"] == "kept":
            continue
        judged = date.fromisoformat(entry["judged_on"]) if entry.get("judged_on") else None
        seen_since = judged is None or last > judged
        if not seen_since:
            continue
        if entry["status"] == "held" or speed(entry, today) == "emerging" or (judged and (today - judged).days >= 30):
            out.append(key)
    return out


def recent_ideas(data: dict, today: date, days: int = 45) -> list[dict]:
    cutoff = (today - timedelta(days=days)).isoformat()
    return [{"id": i, "title": v["title"], "route": v["route"], "status": v.get("status"), "created": v["created"]}
            for i, v in sorted(data["ideas"].items(), key=lambda kv: kv[1]["created"]) if v["created"] >= cutoff]
