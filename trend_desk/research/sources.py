"""Read the research dashboard's studies, and every ledger that says a study is already taken.

The dashboard repo (Meggers1982/research-digest-dashboard) is public, so its data/*.json files are
read straight from raw.githubusercontent.com with curl (this Mac's python.org Python has no CA
bundle). A study found by several digests is one study: merged by PMID, keeping the highest-scored
copy and the list of every digest that found it.
"""
from __future__ import annotations

import glob
import json
import subprocess
from pathlib import Path

RAW = "https://raw.githubusercontent.com/Meggers1982/research-digest-dashboard/main/"
SKIP_SOURCES = {"pitch-ideas"}
PITCHES = Path.home() / "Pitches"


def fetch_json(path: str):
    p = subprocess.run(["curl", "-sS", "--compressed", "--max-time", "120", "-f", RAW + path],
                       capture_output=True, text=True)
    if p.returncode:
        raise RuntimeError(f"couldn't fetch {path} from the dashboard repo (curl exit {p.returncode})")
    return json.loads(p.stdout)


def load_studies() -> tuple[dict, dict]:
    """({pmid: study}, {source_id: last_updated}). Each study gains `digests` and `source_id`."""
    merged, updated = {}, {}
    for src in fetch_json("data/sources.json"):
        if src["id"] in SKIP_SOURCES:
            continue
        data = fetch_json(src["file"])
        updated[src["id"]] = data.get("last_updated", "")
        for s in data.get("studies", []):
            pmid = str(s.get("pmid") or "").strip()
            if not pmid or s.get("excluded"):
                continue
            s = {**s, "pmid": pmid, "source_id": src["id"], "digest_label": src["label"]}
            have = merged.get(pmid)
            if have is None:
                merged[pmid] = {**s, "digests": [src["label"]]}
                continue
            digests = sorted(set(have["digests"]) | {src["label"]})
            if (s.get("relevance_score") or 0, s.get("run_date", "")) > \
               (have.get("relevance_score") or 0, have.get("run_date", "")):
                have = {**s}
            # A repeat keeps its earliest run_date, so a re-found study never looks newly found.
            have["run_date"] = min(have.get("run_date") or "9999", merged[pmid].get("run_date") or "9999")
            have["digests"] = digests
            merged[pmid] = have
    return merged, updated


def taken_pmids() -> dict:
    """{pmid: where} for studies another pitch path already handled. Read from ~/Pitches."""
    out = {}
    state = PITCHES / "state"
    for f in sorted(state.glob("triage-ledger*.json")):
        try:
            for key in json.loads(f.read_text()).get("pmids", {}):
                out.setdefault(key.split(":", 1)[-1], "digest triage")
        except (OSError, json.JSONDecodeError):
            continue
    for f in glob.glob(str(PITCHES / "candidates" / "*.json")):
        try:
            for item in json.loads(Path(f).read_text()).get("items", []):
                if item.get("pmid"):
                    out.setdefault(str(item["pmid"]), "weekly top 12")
        except (OSError, json.JSONDecodeError, AttributeError):
            continue
    try:
        for item in json.loads((state / "research-handoffs.json").read_text()):
            for s in item.get("studies", []):
                out.setdefault(str(s.get("pmid")), "research desk")
    except (OSError, json.JSONDecodeError):
        pass
    return out


def pitched_topics(limit: int = 120) -> list[str]:
    """What has already been pitched or held, as text, for the Judge to dedupe by meaning."""
    topics = []
    state = PITCHES / "state"
    for name in ("daily-ledger.json", "ns-ledger.json"):
        try:
            for t in json.loads((state / name).read_text()).get("topics", [])[-limit:]:
                topics.append(f"{t.get('topic', '')} ({t.get('status', '')}, {t.get('date', '')})")
        except (OSError, json.JSONDecodeError):
            continue
    try:
        for t in json.loads((state / "trend-handoffs.json").read_text())[-40:]:
            topics.append(f"{t.get('headline', '')} (Trend Desk, {t.get('date', '')})")
    except (OSError, json.JSONDecodeError):
        pass
    return topics


def trending_now(today) -> list[str]:
    """What people are searching this week, from Trend Desk's ledger: its recent ideas and the terms
    it kept or put on watch (not the raw radar terms, which are mostly sports and celebrity noise).
    A fresh study that tests one of these is the strongest "Is it real?" outline there is."""
    from .. import ledger
    try:
        data = ledger.load()
    except Exception:  # noqa: BLE001 - the cross-check is a bonus, never a reason to fail
        return []
    out = [f"{i['title']} (Trend Desk idea, {i['route']})" for i in ledger.recent_ideas(data, today, days=14)]
    for e in data.get("terms", {}).values():
        if e.get("status") in ("kept", "held") and ledger.speed(e, today) in ("exploding", "emerging", "new"):
            out.append(f"{e['term']} ({ledger.speed(e, today)})")
    return out[:80]
