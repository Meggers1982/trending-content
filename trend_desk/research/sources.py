"""Read the research dashboard's studies, and every ledger that says a study is already taken.

The dashboard repo (Meggers1982/research-digest-dashboard) is public, so its data/*.json files are
read straight from raw.githubusercontent.com with curl (this Mac's python.org Python has no CA
bundle). A study found by several digests is one study: merged by PMID, keeping the highest-scored
copy and the list of every digest that found it.

Two OpenAlex digests join them (Digest Desks, MEA-1865): marketing-research-digest and
career-psychology-digest. Their studies have no PMID, so they are keyed by OpenAlex work id
("W7221827692"), which can't collide with a numeric PMID and matches the bare ids in the
~/Pitches triage ledgers ("marketing:W…" minus its prefix). openalex_study() reshapes each one into
the research dashboard's field names, so run.py and rules.py treat both kinds alike.
"""
from __future__ import annotations

import glob
import json
import subprocess
from datetime import date, timedelta
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


OPENALEX = {  # repo: dashboard label
    "marketing-research-digest": "Marketing research",
    "career-psychology-digest": "Career psychology",
}
OPENALEX_LOOKBACK = 14   # one topic a day on a 14-day rotation, so a study stays eligible two weeks
CROSSREF_CACHE = Path.home() / ".local/state/research-desk/crossref.json"
MONTH_ABBR = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
COVERAGE = {"widely_reported": "Already covered", "lightly_reported": "Lightly covered",
            "unreported": "No coverage found"}


def fetch_url(url: str):
    p = subprocess.run(["curl", "-sS", "--compressed", "--max-time", "120", "-f", url],
                       capture_output=True, text=True)
    if p.returncode:
        raise RuntimeError(f"couldn't fetch {url.split('/')[4] if url.count('/') > 4 else url} (curl exit {p.returncode})")
    return json.loads(p.stdout)


def pubmed_style(iso: str) -> str:
    """OpenAlex's ISO date in PubMed's "2026 Oct 24" form, so rules.online_date() reads it. A date on
    the 1st is usually an issue date, so it becomes month-only and counts as unverified."""
    try:
        y, m, d = (int(x) for x in iso[:10].split("-"))
    except ValueError:
        return ""
    return f"{y} {MONTH_ABBR[m - 1]}" if d == 1 else f"{y} {MONTH_ABBR[m - 1]} {d}"


def openalex_study(s: dict, run: dict, label: str) -> dict:
    """One OpenAlex digest study in the research dashboard's shape."""
    try:
        score = int(str(s.get("score", "0")).strip() or 0)
    except ValueError:
        score = 0
    verdict = str(s.get("verdict") or "")
    cov = s.get("coverage_state") or ""
    covered = ", ".join(c.get("outlet", c) if isinstance(c, dict) else str(c) for c in s.get("covered_by") or [])
    return {
        "pmid": s["work_id"], "doi": s.get("doi", ""), "headline": s.get("title", ""),
        "paper_title": s.get("paper_title", ""), "journal": s.get("journal", ""),
        "pubdate": pubmed_style(s.get("published", "")), "published": s.get("published", ""),
        "run_date": run.get("run_date", ""), "relevance_score": round(score / 10, 1),
        "relevance_score_reason": f"{s.get('band', '')} band, {s.get('evidence_type', '')}, "
                                  f"journal tier {s.get('journal_tier') or 'unrated'}",
        "summary": s.get("the_study", ""), "why_it_matters": s.get("why_it_matters", ""),
        "caveats": s.get("caveats", ""),
        "fact_check_note": f"{verdict}: {s.get('verdict_notes', '')}".strip(": "),
        "verdict": verdict, "evidence_type": s.get("evidence_type") or "unspecified",
        "sample_size": s.get("sample_size"), "band": s.get("band", ""),
        "media_coverage": (COVERAGE.get(cov, cov or "Not checked") + (f": {covered}" if covered else "")),
        "pitch_angles": [{"headline": s.get("story_angle_primary", ""), "hook": s.get("story_angle_secondary", "")}],
        "openalex": True, "eligible": s.get("band") == "Lead", "lookback_days": OPENALEX_LOOKBACK,
        "source_id": label.lower().replace(" ", "-"), "digest_label": f"{label}: {run.get('topic', '')}",
    }


def load_openalex(merged: dict, updated: dict) -> None:
    """Add the OpenAlex digests' studies to `merged`, in place. A digest that can't be read is
    skipped (logged in `updated` as "error"), so one dark digest never stops the day's judging."""
    for repo, label in OPENALEX.items():
        base = f"https://raw.githubusercontent.com/Meggers1982/{repo}/main/docs/data/"
        try:
            index = fetch_url(base + "index.json")
        except Exception:  # noqa: BLE001
            updated[repo] = "error"
            continue
        runs = sorted(index.get("runs", []), key=lambda r: r.get("run_date", ""), reverse=True)
        updated[repo] = runs[0].get("run_date", "") if runs else ""
        cutoff = (date.today() - timedelta(days=OPENALEX_LOOKBACK + 2)).isoformat()
        for r in runs:
            if r.get("run_date", "") < cutoff:
                break
            try:
                run = fetch_url(base + f"runs/{r['id']}.json")
            except Exception:  # noqa: BLE001
                continue
            for s in run.get("studies", []):
                if not s.get("work_id"):
                    continue
                st = openalex_study(s, run, label)
                have = merged.get(st["pmid"])
                if have is None:
                    merged[st["pmid"]] = {**st, "digests": [st["digest_label"]]}
                else:
                    have["digests"] = sorted(set(have["digests"]) | {st["digest_label"]})
                    have["run_date"] = min(have.get("run_date") or "9999", st["run_date"] or "9999")


def crossref_online(doi: str) -> str:
    """The online publication date Crossref holds for a DOI ("2026 Oct 14"), or "" if it has none.
    Cached, since a date doesn't change. Asked only for studies about to be judged."""
    cache = {}
    try:
        cache = json.loads(CROSSREF_CACHE.read_text())
    except (OSError, json.JSONDecodeError):
        pass
    if doi in cache:
        return cache[doi]
    out = ""
    try:
        msg = fetch_url(f"https://api.crossref.org/works/{doi}")["message"]
        parts = (msg.get("published-online") or {}).get("date-parts", [[]])[0]  # never the print date
        if len(parts) == 3:
            out = f"{parts[0]} {MONTH_ABBR[parts[1] - 1]} {parts[2]}"
    except Exception:  # noqa: BLE001 - no Crossref date leaves the OpenAlex date, marked unverified
        return ""
    cache[doi] = out
    CROSSREF_CACHE.parent.mkdir(parents=True, exist_ok=True)
    CROSSREF_CACHE.write_text(json.dumps(cache, indent=0))
    return out


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
    load_openalex(merged, updated)
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
