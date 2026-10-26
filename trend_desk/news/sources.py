"""Read News Desk's two sources, and every ledger that says an item is already taken.

  news digest   news-digest-ivory.vercel.app/api/items (org-news-digest, MEA-1866): press releases
                from Business Wire and PR Newswire, and org-watch items from agency and advocacy feeds
  AgingWire     agingwire-research-intelligence's outputs/latest.json on raw GitHub: Federal Register
                notices, CMS, BLS, Census, CFPB, and KFF, RAND and Justice in Aging analyses

Both read with curl (this Mac's python.org Python has no CA bundle). Every item gets a key that
matches the ~/Pitches triage ledgers (`aw-<slug>`, `press-<slug>`, from bin/sources.py) and is
deduped across both sources by its link, since both read KFF, CMS and the Commonwealth Fund.
"""
from __future__ import annotations

import json
import re
import subprocess
from datetime import date, timedelta
from pathlib import Path
from urllib.parse import urlsplit

NEWS_API = "https://news-digest-ivory.vercel.app/api/items"
AGINGWIRE = "https://raw.githubusercontent.com/Meggers1982/agingwire-research-intelligence/main/outputs/latest.json"
PITCHES = Path.home() / "Pitches"
ANALYSIS_HOSTS = ("kff.org", "rand.org", "commonwealthfund.org", "urban.org", "brookings.edu", "justiceinaging.org",
                  "ebri.org", "aarp.org", "nber.org", "pewresearch.org", "census.gov", "bls.gov")


def fetch(url: str):
    p = subprocess.run(["curl", "-sS", "--compressed", "--max-time", "120", "-f", url],
                       capture_output=True, text=True)
    if p.returncode:
        raise RuntimeError(f"couldn't fetch {urlsplit(url).netloc} (curl exit {p.returncode})")
    return json.loads(p.stdout)


def slug(text: str, n: int = 60) -> str:
    """bin/sources.py's slug, so keys match the triage ledgers."""
    s = re.sub(r"[^a-z0-9]+", "-", (text or "").lower()).strip("-")
    return s[:n].rstrip("-") or "item"


def link_key(url: str) -> str:
    u = urlsplit((url or "").strip())
    return (u.netloc.lower().removeprefix("www.") + u.path.rstrip("/")).lower()


def host(url: str) -> str:
    return urlsplit(url or "").netloc.lower().removeprefix("www.")


def org_kind(url: str) -> str:
    h = host(url)
    if h.endswith(".gov") and not h.endswith(("census.gov", "bls.gov")):
        return "agency"
    if any(h == a or h.endswith("." + a) for a in ANALYSIS_HOSTS):
        return "analysis"
    return "org_release"


def iso(text: str) -> str:
    m = re.search(r"\d{4}-\d{2}-\d{2}", text or "")
    return m.group(0) if m else ""


def load_news(today: date, days: int = 3) -> list[dict]:
    data = fetch(f"{NEWS_API}?date={today.isoformat()}&days={days}")
    out = []
    for run in data.get("runs", []):
        for it in run.get("items", []):
            press = run["digest"] == "press"
            out.append({
                "key": ("press-" + slug(it.get("headline", ""))[:70]) if press else "org-" + slug(it.get("headline", ""), 70),
                "source": "news digest", "digest": "press" if press else "org",
                "kind": "press_release" if press else org_kind(it.get("url", "")),
                "title": it.get("headline", ""), "summary": it.get("summary", ""), "section": it.get("section", ""),
                "publisher": it.get("source", ""), "url": it.get("url", ""),
                # A press item was released on its run date or within the feed's lookback before it.
                "released": iso(it.get("published", "")) or it.get("released_after") or run["run_date"],
                "date_basis": "feed date" if iso(it.get("published", "")) else f"within {run.get('lookback_days', 1)} day(s) of the digest run",
                "found": run["run_date"], "run_id": run.get("id"),
            })
    return out


def load_agingwire() -> tuple[list[dict], str]:
    data = fetch(AGINGWIRE)
    out = []
    for e in data.get("evidence", []):
        meta = e.get("raw_metadata") or {}
        st = e.get("source_type", "")
        out.append({
            "key": "aw-" + slug(e.get("title", ""), 70), "source": "AgingWire", "digest": e.get("source_id", ""),
            "kind": "dataset" if meta.get("record_type") == "dataset" else
                    "notice" if st in ("regulatory_filing", "government_api") else org_kind(e.get("url", "")),
            "title": e.get("title", ""), "summary": (e.get("summary") or "")[:600],
            "key_findings": (e.get("key_findings") or [])[:5], "publisher": e.get("source_id", ""),
            "url": e.get("url", ""), "released": iso(e.get("published_at", "")), "date_basis": "source date",
            "found": iso(meta.get("first_seen", "")), "topics": e.get("topics", []),
            "score": e.get("score"), "evidence_grade": e.get("evidence_grade"),
            "coverage": meta.get("coverage_state", ""), "localizable": e.get("localizable", False),
        })
    return out, data.get("generated_at", "")


def taken_keys() -> dict:
    """{key or link: where} for items another pitch path already handled."""
    out = {}
    state = PITCHES / "state"
    for name in ("triage-ledger.agingwire.json", "triage-ledger.press.json"):
        try:
            for k in json.loads((state / name).read_text()).get("pmids", {}):
                out.setdefault(k.split(":", 1)[-1], "digest triage")
        except (OSError, json.JSONDecodeError):
            continue
    try:
        for item in json.loads((state / "news-handoffs.json").read_text()):
            for it in item.get("items", []):
                out.setdefault(it.get("key", ""), "news desk")
                out.setdefault(link_key(it.get("url", "")), "news desk")
    except (OSError, json.JSONDecodeError):
        pass
    return out
