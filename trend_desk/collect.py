"""Read every signal source the repo already produces into the trend ledger.

Sources, all files other jobs commit:
  radar      outputs/google_trend_radar/trend_radar_<profile>_<date>_<HHMM>.json (18 weekly radars,
             tracked topics, ad-hoc scans): one sighting per retained candidate
  newsroom   outputs/daily_newsroom_dashboard/extraction_<date>.json: the daily pipeline's retained
             candidates, already vetted by its own 12-stage process
  rising     outputs/daily_newsroom_dashboard/serp_signals_<date>.md: "Top rising related queries"
  wide       outputs/trend_desk/wide_<date>.json: the all-category Trending Now scan (wide_scan.py)

Everything here is untrusted text from Google and news sites. It is stored and passed to the
Judge as data; nothing in it is ever executed or treated as an instruction.
"""
from __future__ import annotations

import json
import re
from datetime import date, timedelta
from pathlib import Path

from . import ledger

ROOT = ledger.ROOT
RADAR_DIR = ROOT / "outputs" / "google_trend_radar"
NEWSROOM_DIR = ROOT / "outputs" / "daily_newsroom_dashboard"
WIDE_DIR = ROOT / "outputs" / "trend_desk"

RADAR_NAME = re.compile(r"trend_radar_(?P<profile>.+)_(?P<date>\d{4}-\d{2}-\d{2})_\d{4}\.json$")
DATED = re.compile(r"_(\d{4}-\d{2}-\d{2})\.(json|md)$")


def _file_date(path: Path) -> str | None:
    m = RADAR_NAME.search(path.name) or DATED.search(path.name)
    return m.group("date") if m and "date" in m.groupdict() else (m.group(1) if m else None)


def collect_radar(data: dict, since: str) -> int:
    n = 0
    for path in sorted(RADAR_DIR.glob("trend_radar_*.json")):
        m = RADAR_NAME.search(path.name)
        if not m or m.group("date") < since:
            continue
        try:
            scan = json.loads(path.read_text())
        except (OSError, json.JSONDecodeError):
            continue
        profile = scan.get("topic") or m.group("profile")
        when = scan.get("run_date") or m.group("date")
        for c in scan.get("candidates", []):
            if ledger.add_sighting(data, c.get("topic", ""), when, "radar", profile,
                                   c.get("trend_stage", ""), c.get("radar_score"), c.get("opportunity_score")):
                n += 1
    return n


def collect_newsroom(data: dict, since: str) -> tuple[int, dict]:
    """Returns (count, context) where context maps term key -> the pipeline's own angle and
    sources, so the Judge doesn't redo work the daily pipeline already did."""
    n, context = 0, {}
    for path in sorted(NEWSROOM_DIR.glob("extraction_*.json")):
        when = _file_date(path)
        if not when or when < since:
            continue
        try:
            run = json.loads(path.read_text())
        except (OSError, json.JSONDecodeError):
            continue
        for c in run.get("candidates", []):
            key = ledger.add_sighting(data, c.get("topic", ""), when, "newsroom", "daily-pipeline",
                                      "", c.get("trend_strength_score"), c.get("opportunity_score"))
            if key:
                n += 1
                context[key] = {
                    "angle": c.get("recommended_angle"), "why_now": c.get("why_now"),
                    "sources": (c.get("source_urls") or [])[:3],
                    "fact_check": (c.get("fact_check") or {}).get("verdict"),
                    "integrity_flags": (c.get("integrity_flags") or [])[:2],
                }
    return n, context


def collect_rising(data: dict, since: str) -> int:
    n = 0
    for path in sorted(NEWSROOM_DIR.glob("serp_signals_*.md")):
        when = _file_date(path)
        if not when or when < since:
            continue
        lines = path.read_text(errors="replace").splitlines()
        grab = False
        for line in lines:
            if line.startswith("Top rising related queries"):
                grab = True
                continue
            if grab:
                m = re.match(r"\s+-\s+(.+)$", line)
                if not m:
                    if line.strip():
                        grab = False
                    continue
                if ledger.add_sighting(data, m.group(1), when, "rising", "daily-signals", "rising"):
                    n += 1
    return n


def collect_wide(data: dict, since: str) -> tuple[int, dict]:
    n, context = 0, {}
    for path in sorted(WIDE_DIR.glob("wide_*.json")):
        when = _file_date(path)
        if not when or when < since:
            continue
        try:
            scan = json.loads(path.read_text())
        except (OSError, json.JSONDecodeError):
            continue
        for item in scan.get("items", []):
            key = ledger.add_sighting(data, item.get("query", ""), when, "wide", "trending-now",
                                      "breakout" if (item.get("increase_percentage") or 0) >= 1000 else "rising",
                                      item.get("search_volume"))
            if key:
                n += 1
                if item.get("news"):
                    context[key] = {"news": item["news"], "categories": item.get("categories", [])}
    return n, context


def collect_all(data: dict, today: date, backfill: bool = False) -> dict:
    """Pull every source newer than the last Judge run (or everything, on the first run, so the
    ledger starts with real history and `emerging` works from day one)."""
    last = data["runs"][-1]["date"] if data["runs"] else None
    if backfill or not last:
        since = "2000-01-01"
    else:
        since = (date.fromisoformat(last) - timedelta(days=1)).isoformat()
    newsroom_n, newsroom_ctx = collect_newsroom(data, since)
    wide_n, wide_ctx = collect_wide(data, since)
    return {
        "since": since,
        "counts": {"radar": collect_radar(data, since), "newsroom": newsroom_n,
                   "rising": collect_rising(data, since), "wide": wide_n},
        "context": {**wide_ctx, **newsroom_ctx},
    }
