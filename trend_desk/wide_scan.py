"""Wide-open scan: Google Trends "Trending Now" across every category, not just health.

The 18 topic radars only find what their seed terms lead to. This catches the rest (AI, home,
culture, politics, consumer stories) so the Judge can decide what fits Meagan's beats. Costs one
SerpAPI request plus one per news drill-down (WIDE_NEWS_LIMIT), and no Claude credit.

  python -m trend_desk.wide_scan            writes outputs/trend_desk/wide_<date>.json
"""
from __future__ import annotations

import json
import os
import sys
import time
from datetime import datetime
from zoneinfo import ZoneInfo

from . import ledger

OUT_DIR = ledger.ROOT / "outputs" / "trend_desk"
WIDE_LIMIT = 60
WIDE_NEWS_LIMIT = int(os.getenv("TREND_DESK_WIDE_NEWS_LIMIT", "12"))


def main() -> int:
    sys.path.insert(0, str(ledger.ROOT))
    import run_pipeline  # reuses its SerpAPI client: retries, circuit breaker, time budget

    today = datetime.now(ZoneInfo("America/Chicago")).date().isoformat()
    out = OUT_DIR / f"wide_{today}.json"
    if out.exists():
        print(f"Wide scan: {out.name} already exists, skipping (saves SerpAPI quota).")
        return 0
    data = run_pipeline._serp_get({
        "engine": "google_trends_trending_now", "geo": "US", "hours": "24",
        "only_active": "true", "hl": "en",
    })
    if not data:
        print("Wide scan: SerpAPI returned nothing (key missing, quota, or outage). No file written.")
        return 0
    raw = data.get("trending_searches", [])
    raw.sort(key=lambda i: i.get("search_volume") or 0, reverse=True)
    items = []
    for item in raw[:WIDE_LIMIT]:
        if not item.get("query"):
            continue
        items.append({
            "query": item["query"],
            "search_volume": item.get("search_volume"),
            "increase_percentage": item.get("increase_percentage"),
            "categories": [c.get("name") for c in item.get("categories", []) if c.get("name")],
            "news_page_token": item.get("news_page_token", ""),
        })
    for i, item in enumerate([x for x in items if x["news_page_token"]][:WIDE_NEWS_LIMIT]):
        if i:
            time.sleep(1)
        news = run_pipeline._serp_get({"engine": "google_trends_news", "page_token": item["news_page_token"]})
        articles = (news or {}).get("news", [])[:2]
        item["news"] = [{"title": a.get("title"), "link": a.get("link"), "source": a.get("source")}
                        for a in articles if a.get("link", "").startswith("http")]
    for item in items:
        item.pop("news_page_token", None)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({"run_date": today, "geo": "US", "items": items}, indent=1, ensure_ascii=False) + "\n")
    print(f"Wide scan: {len(items)} trending searches saved to {out.relative_to(ledger.ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
