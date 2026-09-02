#!/usr/bin/env python3
"""
run_tracked_topics.py — re-scan saved topics from the tracked_topics table

Loops the tracked-topics list (added via the dashboard's "Track this topic" /
"Track" form, see app/api/tracked-topics) and re-runs google_trend_radar.py
for each one, always with --include-autocomplete since tracked lists are
small/curated and the extra SerpAPI calls are worth the richer discovery
(regular ad-hoc scans default that flag off to control API volume).

Tracked topics live in Neon Postgres (DATABASE_URL), the same database the
Next.js app's lib/tracked-topics.js reads and writes — this script is the
Python side of that same source of truth, not a separate copy.

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
import os
import subprocess
import sys
from pathlib import Path

import psycopg

PROJECT_ROOT = Path(__file__).resolve().parent


def db_connect() -> psycopg.Connection:
    database_url = os.environ.get("DATABASE_URL")
    if not database_url:
        sys.exit("DATABASE_URL is not set.")
    return psycopg.connect(database_url)


def load_tracked_topics() -> list[dict]:
    with db_connect() as conn, conn.cursor() as cur:
        cur.execute("select id, topic, profile, geo from tracked_topics order by created_at asc")
        rows = cur.fetchall()
    return [{"id": r[0], "topic": r[1], "profile": r[2], "geo": r[3]} for r in rows]


def mark_scanned(ids: set[str]) -> None:
    if not ids:
        return
    with db_connect() as conn, conn.cursor() as cur:
        cur.execute(
            "update tracked_topics set last_scanned_at = now() where id = any(%s)",
            (list(ids),),
        )
        conn.commit()


def scan_topic(entry: dict) -> bool:
    args = [
        sys.executable, "google_trend_radar.py",
        "--topic", entry["topic"],
        "--profile", entry.get("profile") or "auto",
        "--geo", entry.get("geo") or "US",
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
    parser = argparse.ArgumentParser(description="Re-scan tracked topics from Neon.")
    parser.add_argument("--topic-id", default="", help="Only scan the tracked topic with this id, instead of the full list.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    topics = load_tracked_topics()
    if not topics:
        print("No tracked topics found.")
        return

    if args.topic_id:
        topics_to_scan = [t for t in topics if t["id"] == args.topic_id]
        if not topics_to_scan:
            sys.exit(f"No tracked topic with id '{args.topic_id}'.")
    else:
        topics_to_scan = topics

    scanned_ids = set()
    for entry in topics_to_scan:
        if scan_topic(entry):
            scanned_ids.add(entry["id"])

    mark_scanned(scanned_ids)
    print(f"Scanned {len(scanned_ids)}/{len(topics_to_scan)} tracked topic(s).")


if __name__ == "__main__":
    main()
