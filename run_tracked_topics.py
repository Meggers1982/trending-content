#!/usr/bin/env python3
"""
run_tracked_topics.py — re-scan saved topics from data/tracked_topics.json

Loops the tracked-topics list (added via the dashboard's "Track this topic" /
"Track" form, see app/api/tracked-topics) and re-runs google_trend_radar.py
for each one, always with --include-autocomplete since tracked lists are
small/curated and the extra SerpAPI calls are worth the richer discovery
(regular ad-hoc scans default that flag off to control API volume).

Usage:
    python run_tracked_topics.py                  # scan every tracked topic
    python run_tracked_topics.py --topic-id gut-health-probiotics  # just one

Used by .github/workflows/run-tracked-topics.yml: unfiltered on the daily
schedule, filtered to one --topic-id when the dashboard's "Scan now" button
dispatches the workflow on-demand (Vercel deploys have no local Python
process to spawn, so that's the remote-execution path there).
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
TRACKED_TOPICS_PATH = PROJECT_ROOT / "data" / "tracked_topics.json"


def load_tracked_topics() -> list[dict]:
    if not TRACKED_TOPICS_PATH.exists():
        return []
    try:
        data = json.loads(TRACKED_TOPICS_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        sys.exit(f"Could not parse {TRACKED_TOPICS_PATH}: {exc}")
    topics = data.get("tracked_topics", [])
    return topics if isinstance(topics, list) else []


def save_tracked_topics(topics: list[dict]) -> None:
    TRACKED_TOPICS_PATH.write_text(
        json.dumps({"tracked_topics": topics}, indent=2) + "\n", encoding="utf-8"
    )


def scan_topic(entry: dict) -> bool:
    args = [
        sys.executable, "google_trend_radar.py",
        "--topic", entry["topic"],
        "--profile", entry.get("profile", "auto"),
        "--geo", entry.get("geo", "US"),
        "--skip-timeseries",
        "--include-autocomplete",
    ]
    print(f"Scanning tracked topic '{entry['topic']}' ({entry.get('profile', 'auto')}, {entry.get('geo', 'US')})...")
    result = subprocess.run(args, cwd=PROJECT_ROOT)
    if result.returncode != 0:
        print(f"Scan failed for '{entry['topic']}' (exit code {result.returncode}); continuing.", file=sys.stderr)
        return False
    return True


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Re-scan tracked topics from data/tracked_topics.json.")
    parser.add_argument("--topic-id", default="", help="Only scan the tracked topic with this id, instead of the full list.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    topics = load_tracked_topics()
    if not topics:
        print("No tracked topics found.")
        return

    if args.topic_id:
        topics_to_scan = [t for t in topics if t.get("id") == args.topic_id]
        if not topics_to_scan:
            sys.exit(f"No tracked topic with id '{args.topic_id}'.")
    else:
        topics_to_scan = topics

    scanned_ids = set()
    for entry in topics_to_scan:
        if scan_topic(entry):
            scanned_ids.add(entry["id"])

    if scanned_ids:
        now = datetime.now().isoformat(timespec="seconds")
        for entry in topics:
            if entry.get("id") in scanned_ids:
                entry["last_scanned_at"] = now
        save_tracked_topics(topics)

    print(f"Scanned {len(scanned_ids)}/{len(topics_to_scan)} tracked topic(s).")


if __name__ == "__main__":
    main()
