#!/usr/bin/env python3
"""
Google Trend Radar

Creates a standalone trend-discovery dashboard from Google Trends signals
via SerpAPI. It follows the Trending Content OS pattern: listen, dedupe,
score, route weak signals out, and publish a compact priority board.

Usage:
    python google_trend_radar.py --profile wellness
    python google_trend_radar.py --profile health
    python google_trend_radar.py --topic "AI tools" --profile ai --geo US --date "now 7-d"
    python google_trend_radar.py --profile beauty --geo US --date "now 7-d"

The beauty profile additionally cross-checks Reddit (free, no API key) as a
second signal source and tags candidates with ingredient/benefit/concern
labels from configs/beauty_taxonomy.yaml, plus an opportunity_score
estimating whitespace (high emergence, low saturation) alongside radar_score.

Google Trends "Trending Now" real-time terms are folded in as extra seeds by
default (set SERPAPI_TRENDING_NOW_ENABLED=true; disable with
--skip-trending-now). Google Trends Autocomplete suggestions can optionally
be added as further seeds via --include-autocomplete.
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import os
import re
import smtplib
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from dataclasses import dataclass, field
from datetime import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from statistics import mean

import yaml


PROJECT_ROOT = Path(__file__).resolve().parent
ENV_PATH = PROJECT_ROOT / ".env"
OUTPUT_DIR = PROJECT_ROOT / "outputs" / "google_trend_radar"
TEMPLATE_PATH = PROJECT_ROOT / "google_trend_radar_template.html"
BEAUTY_TAXONOMY_PATH = PROJECT_ROOT / "configs" / "beauty_taxonomy.yaml"
SERPAPI_BASE = "https://serpapi.com/search"
REDDIT_SEARCH_BASE = "https://www.reddit.com/search.json"
REDDIT_SUBREDDIT_SEARCH_BASE = "https://www.reddit.com/r/{subreddit}/search.json"
REDDIT_USER_AGENT = "google-trend-radar/1.0 (personal trend-scanning script)"
REDDIT_BEAUTY_SUBREDDITS = ["SkincareAddiction", "MakeupAddiction", "HaircareScience"]

DEFAULT_SEED_PROFILE = "auto"
DEFAULT_MAX_SEEDS = 24
GOOGLE_TRENDS_QUERY_LIMIT = 100
DEFAULT_REQUEST_TIMEOUT = 12
DEFAULT_REQUEST_RETRIES = 0
REDDIT_REQUEST_DELAY_SECONDS = 1.5
REDDIT_MIN_MENTIONS = 2
VERBOSE_ERRORS = False

# Drilling into "why is this trending" costs one extra SerpAPI request per
# term (see fetch_trending_news()), so only the top few Trending Now terms
# get enriched rather than all 20 fetched.
TRENDING_NOW_NEWS_LIMIT = 5
TRENDING_NEWS_REQUEST_DELAY_SECONDS = 1.0
# Google Trends "Beauty and Fashion" category (see
# https://serpapi.com/google-trends-trending-now-categories). The default
# Trending Now category is Health (7, via SERPAPI_TRENDING_NOW_CATEGORY_ID) -
# beauty runs additionally pull this category so the breakouts aren't just
# health spillover with nothing actually beauty-specific in it.
BEAUTY_TRENDING_NOW_CATEGORY_ID = "2"
# Beauty and Fashion is much lower-volume than Health, so the default 24h
# "active breakouts" window can come back completely empty (confirmed live,
# 2026-08-20: Health returned 3 terms, Beauty and Fashion returned 0). Widen
# to 48h for this category only - still fresh enough to call "trending,"
# just less likely to be empty. SerpAPI only accepts 4/24/48/168 here.
BEAUTY_TRENDING_NOW_HOURS = "168"
REQUEST_FAILURES: Counter[str] = Counter()

SEED_PROFILES = {
    "wellness": [
        "wellness",
        "health",
        "nutrition",
        "fitness",
        "mental health",
        "public health",
        "gut health",
        "fermented foods",
        "sleep",
        "weight loss",
        "healthy recipes",
        "supplements",
        "medicine",
        "skincare",
        "self care",
        "workout",
        "walking",
        "protein",
        "plant based protein",
        "vegan protein",
        "protein powder",
        "food safety",
        "stress",
        "diet",
    ],
    "health": [
        "health",
        "wellness",
        "nutrition",
        "fitness",
        "mental health",
        "public health",
        "weight loss",
        "sleep",
        "gut health",
        "fermented foods",
        "diet",
        "food safety",
        "medicine",
        "supplements",
        "protein",
        "plant based protein",
        "vegan protein",
    ],
    "ai": [
        "AI",
        "artificial intelligence",
        "AI tools",
        "generative AI",
        "ChatGPT",
        "AI video",
        "AI search",
        "AI agents",
        "AI coding",
    ],
    "beauty": [
        "beauty",
        "skincare",
        "makeup",
        "haircare",
        "fragrance",
        "clean beauty",
        "retinol",
        "niacinamide",
        "peptides",
        "hyaluronic acid",
        "skin barrier",
        "skin cycling",
        "glass skin",
        "slugging",
        "scalp care",
        "SPF",
        "sunscreen",
        "K-beauty",
        "hair loss",
        "acne treatment",
    ],
    "nutrition": [
        "nutrition",
        "macronutrients",
        "meal prep",
        "whole foods",
        "fiber intake",
        "added sugar",
        "ultra-processed foods",
        "nutrient deficiency",
        "mindful eating",
        "portion control",
        "plant-based diet",
    ],
    "fitness": [
        "fitness",
        "strength training",
        "cardio",
        "HIIT workout",
        "resistance training",
        "mobility training",
        "workout recovery",
        "home workout",
        "running",
        "weightlifting",
        "VO2 max",
    ],
    "food-safety": [
        "food safety",
        "food recall",
        "foodborne illness",
        "food contamination",
        "listeria outbreak",
        "salmonella outbreak",
        "restaurant inspection",
        "USDA recall",
        "cross contamination",
    ],
    "diet": [
        "diet",
        "keto diet",
        "intermittent fasting",
        "low carb diet",
        "Mediterranean diet",
        "weight management",
        "calorie deficit",
        "macro tracking",
        "elimination diet",
        "anti-inflammatory diet",
    ],
    "weight-loss": [
        "weight loss",
        "weight loss journey",
        "fat loss",
        "sustainable weight loss",
        "weight loss surgery",
        "GLP-1",
        "semaglutide",
        "weight loss plateau",
        "weight loss medication",
    ],
    "mental-health": [
        "mental health",
        "anxiety",
        "depression",
        "therapy",
        "burnout",
        "stress management",
        "mindfulness",
        "cognitive behavioral therapy",
        "mental health awareness",
        "trauma recovery",
    ],
    "gut-health": [
        "gut health",
        "microbiome",
        "probiotics",
        "prebiotics",
        "gut bacteria",
        "digestive health",
        "IBS",
        "bloating",
        "gut brain axis",
        "leaky gut",
    ],
}

INTENT_MODIFIERS = [
    "trends",
    "products",
    "news",
    "for beginners",
    "routine",
    "benefits",
    "ideas",
    "reviews",
]

GENERIC_ANCHOR_WORDS = {
    "best",
    "near",
    "news",
    "new",
    "trends",
    "products",
    "reviews",
    "routine",
    "ideas",
    "benefits",
    "beginners",
    # These showed up as false-positive anchors in production: a seed like
    # "clean beauty" or "scalp care" derives the standalone token "clean" or
    # "care", which then matches any unrelated Google Trends query containing
    # that common word (e.g. "how to clean a waffle maker", "pet care tips").
    "clean",
    "care",
    "loss",
    # Audited the rest of the beauty seed list for the same pattern (a
    # compound term whose generic half can stand alone as an anchor) after
    # "glass" (from "glass skin") produced the same failure mode as "clean":
    # "how to clean shower glass" slipped through a second time.
    "glass",
    "acid",
    "treatment",
    "cycling",
    # Audited proactively when adding the nutrition/fitness/food-safety/diet/
    # weight-loss/mental-health/gut-health profiles, before shipping rather
    # than after: each of these is the generic half of a compound seed
    # ("food safety", "strength training", "workout recovery", "weight
    # management", "weight loss surgery", "weight loss medication", "portion
    # control") that would otherwise leak into an anchor matching unrelated
    # queries ("gun safety", "job training", "data recovery", "project
    # management", "heart surgery", "prescription medication", "pest control").
    "safety",
    "training",
    "recovery",
    "management",
    "surgery",
    "medication",
    "control",
}


@dataclass
class Candidate:
    query: str
    discovery_sources: set[str] = field(default_factory=set)
    seed_terms: set[str] = field(default_factory=set)
    related_type: str = "query"
    rising_value: int | None = None
    rising_label: str = ""
    interest_scores: list[int] = field(default_factory=list)
    first_interest: int = 0
    latest_interest: int = 0
    peak_interest: int = 0
    avg_interest: float = 0.0
    slope: int = 0
    acceleration: int = 0
    emergence_score: int = 0
    velocity_score: int = 0
    confidence_score: int = 0
    radar_score: int = 0
    saturation_score: int = 0
    opportunity_score: int = 0
    top_bucket_hits: int = 0
    rising_bucket_hits: int = 0
    trend_stage: str = "watch"
    urgency: str = "monitor"
    confidence: str = "low"
    why_now: str = ""
    recommended_action: str = ""
    tags: dict[str, list[str]] = field(default_factory=dict)


def load_env(path: Path = ENV_PATH) -> None:
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def serp_get(params: dict, timeout: int = DEFAULT_REQUEST_TIMEOUT, retries: int = DEFAULT_REQUEST_RETRIES) -> dict | None:
    api_key = os.getenv("SERPAPI_API_KEY", "").strip()
    if not api_key:
        return None
    payload = dict(params)
    payload["api_key"] = api_key
    url = SERPAPI_BASE + "?" + urllib.parse.urlencode(payload)
    label = payload.get("data_type", payload.get("engine"))
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(url, timeout=timeout) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")[:400]
            print(f"SerpAPI error ({label}): HTTP {exc.code}: {body}", file=sys.stderr)
            REQUEST_FAILURES[f"{label} HTTP {exc.code}"] += 1
            return None
        except TimeoutError:
            if attempt < retries:
                if VERBOSE_ERRORS:
                    print(f"SerpAPI timeout ({label}); retrying...", file=sys.stderr)
                continue
            REQUEST_FAILURES[f"{label} timeout"] += 1
            if VERBOSE_ERRORS:
                print(f"SerpAPI timeout ({label}); skipped after {timeout}s.", file=sys.stderr)
        except Exception as exc:
            message = str(exc)
            if "timed out" in message.lower() and attempt < retries:
                if VERBOSE_ERRORS:
                    print(f"SerpAPI timeout ({label}); retrying...", file=sys.stderr)
                continue
            if "timed out" in message.lower():
                REQUEST_FAILURES[f"{label} timeout"] += 1
                if VERBOSE_ERRORS:
                    print(f"SerpAPI timeout ({label}); skipped after {timeout}s.", file=sys.stderr)
                return None
            REQUEST_FAILURES[f"{label} error"] += 1
            print(f"SerpAPI error ({label}): {exc}", file=sys.stderr)
            return None
    return None


def fetch_trending_now(geo: str = "US", category_id: str | None = None, hours: str | None = None) -> list[dict]:
    """Fetch Google Trends 'Trending Now' (real-time breakout searches) as extra seeds.

    Mirrors run_pipeline.py's fetch_trending_now(), reusing the same
    SERPAPI_TRENDING_NOW_* env vars so both scripts share one config surface,
    but calls this file's own serp_get() instead of duplicating retry logic.

    `category_id` overrides SERPAPI_TRENDING_NOW_CATEGORY_ID for this call -
    used to pull a second category (e.g. Beauty and Fashion) on top of the
    configured default (e.g. Health) rather than only ever getting one.
    `hours` overrides SERPAPI_TRENDING_NOW_HOURS similarly - a smaller
    category can have zero *active* breakouts in the default 24h window,
    so a narrower/lower-volume category may want a wider lookback (SerpAPI
    accepts 4, 24, 48, or 168).

    Returns a list of dicts (not bare strings): each item also carries the
    news_page_token needed to drill into *why* it's trending - see
    enrich_trending_now_news().
    """
    if os.getenv("SERPAPI_TRENDING_NOW_ENABLED", "").strip().lower() not in {"1", "true", "yes"}:
        return []
    data = serp_get({
        "engine": "google_trends_trending_now",
        "geo": geo,
        "hours": hours or os.getenv("SERPAPI_TRENDING_NOW_HOURS", "24").strip() or "24",
        "category_id": category_id or os.getenv("SERPAPI_TRENDING_NOW_CATEGORY_ID", "7").strip() or "7",
        "only_active": "true",
        "hl": "en",
    })
    if not data:
        return []
    items = []
    for item in data.get("trending_searches", [])[:20]:
        query = item.get("query", "")
        if query:
            items.append({
                "query": query,
                "news_page_token": item.get("news_page_token", ""),
                "search_volume": item.get("search_volume"),
                "increase_percentage": item.get("increase_percentage"),
            })
    return items


def fetch_trending_news(page_token: str, *, timeout: int = DEFAULT_REQUEST_TIMEOUT, retries: int = DEFAULT_REQUEST_RETRIES) -> dict | None:
    """Drill into one Trending Now term via its news_page_token to find the
    actual story behind the spike, instead of just a bare search term with no
    context. Returns the top article ({title, link, source, date}), or None."""
    if not page_token:
        return None
    data = serp_get({"engine": "google_trends_news", "page_token": page_token}, timeout=timeout, retries=retries)
    if not data:
        return None
    articles = data.get("news", [])
    return articles[0] if articles else None


def enrich_trending_now_news(
    items: list[dict],
    *,
    limit: int = TRENDING_NOW_NEWS_LIMIT,
    request_timeout: int = DEFAULT_REQUEST_TIMEOUT,
    request_retries: int = DEFAULT_REQUEST_RETRIES,
) -> None:
    """Attach the driving news headline to the top `limit` Trending Now
    items, in place. Capped because each lookup is a separate SerpAPI
    request - drilling into every term fetched would multiply request
    volume for terms that mostly won't end up mattering to the run anyway."""
    to_enrich = [item for item in items if item.get("news_page_token")][:limit]
    for index, item in enumerate(to_enrich):
        if index > 0:
            time.sleep(TRENDING_NEWS_REQUEST_DELAY_SECONDS)
        article = fetch_trending_news(item["news_page_token"], timeout=request_timeout, retries=request_retries)
        if article:
            item["news_headline"] = article.get("title", "")
            item["news_source"] = article.get("source", "")
            item["news_link"] = article.get("link", "")


def fetch_autocomplete(query: str, hl: str = "en") -> list[str]:
    """Fetch Google Trends Autocomplete suggestions for a seed query.

    A different signal than RELATED_QUERIES: these are literal phrasings
    Google Trends' own search box suggests, which can surface candidate
    wording that related-query discovery misses.
    """
    data = serp_get({
        "engine": "google_trends_autocomplete",
        "q": query,
        "hl": hl,
    })
    if not data:
        return []
    suggestions = []
    for item in data.get("suggestions", [])[:8]:
        title = item.get("title") or item.get("q") or ""
        if title:
            suggestions.append(title)
    return suggestions


def tag_discovery_source(candidates: list[Candidate], terms: list[str], source_label: str) -> None:
    """Mark candidates whose discovery seed came from an extra source (trending_now/autocomplete).

    Candidates already track which seed(s) led to them via seed_terms; this
    just cross-references that against the extra-source term list rather
    than threading a source map through discover_candidates() itself.
    """
    keys = {normalize(term) for term in terms if normalize(term)}
    if not keys:
        return
    for candidate in candidates:
        seed_keys = {normalize(seed) for seed in candidate.seed_terms}
        if seed_keys & keys:
            candidate.discovery_sources.add(source_label)


def print_request_summary() -> None:
    if not REQUEST_FAILURES:
        return
    details = ", ".join(f"{count} {label}" for label, count in sorted(REQUEST_FAILURES.items()))
    print(f"Skipped slow/unavailable SerpAPI calls: {details}", file=sys.stderr)


def normalize(text: str) -> str:
    text = re.sub(r"\s+", " ", text or "").strip().lower()
    return re.sub(r"[^\w\s#+.-]", "", text)


def load_taxonomy(path: Path = BEAUTY_TAXONOMY_PATH) -> dict[str, list[str]]:
    if not path.exists():
        return {}
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as exc:
        print(f"Could not parse taxonomy file {path}: {exc}", file=sys.stderr)
        return {}
    taxonomy: dict[str, list[str]] = {}
    for tag_type in ("ingredients", "benefits", "concerns"):
        terms = data.get(tag_type) or []
        taxonomy[tag_type] = [str(term) for term in terms if term]
    return taxonomy


def load_exclusion_terms(path: Path = BEAUTY_TAXONOMY_PATH) -> list[str]:
    """Terms that mark a candidate off-topic even though it matched a beauty
    anchor (see the "exclusions" comment in beauty_taxonomy.yaml)."""
    if not path.exists():
        return []
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError:
        return []
    return [str(term) for term in (data.get("exclusions") or []) if term]


def tag_candidate(query: str, taxonomy: dict[str, list[str]]) -> dict[str, list[str]]:
    """Keyword-match a candidate's query text against the beauty taxonomy.

    Runs for every profile, not just beauty, since ingredient/benefit/concern
    terms (magnesium, hair loss, etc.) show up across wellness/health scans too.
    """
    normalized_query = normalize(query)
    tags: dict[str, list[str]] = {}
    for tag_type, terms in taxonomy.items():
        matches = [term for term in terms if normalize(term) in normalized_query]
        if matches:
            tags[tag_type] = matches
    return tags


def parse_rising_value(value) -> tuple[int | None, str]:
    if value is None:
        return None, ""
    label = str(value)
    if "breakout" in label.lower():
        return 5000, "Breakout"
    match = re.search(r"([\d,]+)", label)
    if match:
        number = int(match.group(1).replace(",", ""))
        return number, f"+{number}%"
    if isinstance(value, (int, float)):
        return int(value), f"+{int(value)}%"
    return None, label


def related_items(data: dict, section: str) -> list[dict]:
    block = data.get(section, {})
    items = []
    for key in ("rising", "top"):
        group = block.get(key, [])
        if isinstance(group, dict):
            group = group.get("items", [])
        for item in group or []:
            copied = dict(item)
            copied["_bucket"] = key
            items.append(copied)
    return items


def candidate_name(item: dict) -> str:
    return item.get("query") or item.get("title") or item.get("topic", {}).get("title") or ""


def seed_profile_terms(topic: str, profile: str) -> list[str]:
    profile = (profile or "").strip().lower()
    topic_key = normalize(topic)
    if profile in {"none", "off", "custom"}:
        return []
    if profile in {"auto", "broad"}:
        if topic_key in SEED_PROFILES:
            return SEED_PROFILES[topic_key]
        for key, terms in SEED_PROFILES.items():
            if key in topic_key:
                return terms
        return []
    if profile in SEED_PROFILES:
        return SEED_PROFILES[profile]
    return []


def build_seed_terms(topic: str, manual_seeds: str, profile: str, max_seeds: int) -> list[str]:
    seeds = [topic.strip()]
    seeds.extend(seed_profile_terms(topic, profile))
    seeds.extend(seed.strip() for seed in manual_seeds.split(",") if seed.strip())

    if profile not in {"none", "off", "custom"}:
        seeds.extend(f"{topic.strip()} {modifier}" for modifier in INTENT_MODIFIERS)

    unique = []
    seen = set()
    for seed in seeds:
        key = normalize(seed)
        if not key or key in seen:
            continue
        unique.append(seed)
        seen.add(key)
        if len(unique) >= max_seeds:
            break
    return unique


def relevance_anchors(topic: str, seeds: list[str]) -> set[str]:
    anchors = set()
    for seed in [topic, *seeds]:
        normalized = normalize(seed)
        if not normalized:
            continue
        anchors.add(normalized)
        for token in normalized.split():
            if len(token) >= 4 and token not in GENERIC_ANCHOR_WORDS:
                anchors.add(token)
    return anchors


def is_relevant_candidate(candidate: Candidate, anchors: set[str]) -> bool:
    query = normalize(candidate.query)
    if not query:
        return False
    return any(anchor in query for anchor in anchors)


def discover_candidates(
    topic: str,
    seeds: list[str],
    geo: str,
    date: str,
    limit: int,
    *,
    include_related_topics: bool = True,
    request_timeout: int = DEFAULT_REQUEST_TIMEOUT,
    request_retries: int = DEFAULT_REQUEST_RETRIES,
) -> tuple[list[Candidate], list[dict]]:
    candidates: dict[str, Candidate] = {}
    rejected: list[dict] = []
    seen_queries = {normalize(topic)}

    for seed in seeds:
        requests = [("RELATED_QUERIES", "related_queries", "rising query")]
        if include_related_topics:
            requests.append(("RELATED_TOPICS", "related_topics", "rising topic"))
        for data_type, section, source_name in requests:
            data = serp_get({
                "engine": "google_trends",
                "q": seed,
                "data_type": data_type,
                "date": date,
                "geo": geo,
                "hl": "en",
            }, timeout=request_timeout, retries=request_retries)
            if not data:
                rejected.append({"topic": seed, "reason": f"No {data_type.lower()} data returned"})
                continue
            for item in related_items(data, section):
                name = candidate_name(item)
                key = normalize(name)
                if not key:
                    continue
                if key in seen_queries and key != normalize(topic):
                    continue
                seen_queries.add(key)
                candidate = candidates.setdefault(key, Candidate(query=name))
                candidate.seed_terms.add(seed)
                candidate.related_type = "topic" if data_type == "RELATED_TOPICS" else "query"
                bucket = item.get("_bucket", "")
                candidate.discovery_sources.add(source_name if bucket == "rising" else f"top {candidate.related_type}")
                if bucket == "rising":
                    candidate.rising_bucket_hits += 1
                else:
                    candidate.top_bucket_hits += 1
                value, label = parse_rising_value(item.get("value") or item.get("extracted_value"))
                if bucket == "rising":
                    if value is not None:
                        candidate.rising_value = (
                            value if candidate.rising_value is None else max(candidate.rising_value, value)
                        )
                    candidate.rising_label = label or candidate.rising_label

    ranked = list(candidates.values())
    ranked.sort(key=lambda c: (c.rising_value or 0, len(c.discovery_sources)), reverse=True)
    return ranked[:limit], rejected


def batches(items: list[Candidate], size: int = 5):
    for index in range(0, len(items), size):
        yield items[index:index + size]


def attach_timeseries(
    candidates: list[Candidate],
    geo: str,
    date: str,
    *,
    request_timeout: int = DEFAULT_REQUEST_TIMEOUT,
    request_retries: int = DEFAULT_REQUEST_RETRIES,
) -> None:
    valid_candidates = [
        candidate for candidate in candidates
        if len(candidate.query) <= GOOGLE_TRENDS_QUERY_LIMIT
    ]
    for candidate in candidates:
        if len(candidate.query) > GOOGLE_TRENDS_QUERY_LIMIT:
            candidate.discovery_sources.add("too long for timeseries")

    for group in batches(valid_candidates, 5):
        query = ",".join(c.query for c in group)
        data = serp_get({
            "engine": "google_trends",
            "q": query,
            "data_type": "TIMESERIES",
            "date": date,
            "geo": geo,
            "hl": "en",
        }, timeout=request_timeout, retries=request_retries)
        if not data:
            continue
        timeline = data.get("interest_over_time", {}).get("timeline_data", [])
        values_by_index = [[] for _ in group]
        for point in timeline:
            values = point.get("values", [])
            if point.get("partial_data"):
                continue
            for idx, value in enumerate(values[:len(group)]):
                extracted = value.get("extracted_value")
                if isinstance(extracted, (int, float)):
                    values_by_index[idx].append(int(extracted))
        for candidate, scores in zip(group, values_by_index):
            candidate.interest_scores = scores


def reddit_get(url: str, params: dict, timeout: int = DEFAULT_REQUEST_TIMEOUT, retries: int = DEFAULT_REQUEST_RETRIES) -> dict | None:
    """Fetch Reddit's public read-only JSON search API.

    No OAuth/API key is required for anonymous search, only a descriptive
    User-Agent (Reddit blocks the urllib default one). Anonymous requests are
    rate-limited more aggressively than authenticated ones, so callers should
    space requests out and treat failures as skippable, same as serp_get.
    """
    full_url = url + "?" + urllib.parse.urlencode(params)
    request = urllib.request.Request(full_url, headers={"User-Agent": REDDIT_USER_AGENT})
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            REQUEST_FAILURES[f"reddit HTTP {exc.code}"] += 1
            if VERBOSE_ERRORS:
                print(f"Reddit error: HTTP {exc.code}", file=sys.stderr)
            return None
        except Exception as exc:
            message = str(exc)
            if "timed out" in message.lower() and attempt < retries:
                continue
            REQUEST_FAILURES["reddit error"] += 1
            if VERBOSE_ERRORS:
                print(f"Reddit error: {exc}", file=sys.stderr)
            return None
    return None


def discover_reddit_candidates(
    candidates: dict[str, Candidate],
    seeds: list[str],
    taxonomy: dict[str, list[str]],
    profile: str,
    *,
    request_timeout: int = DEFAULT_REQUEST_TIMEOUT,
    request_retries: int = DEFAULT_REQUEST_RETRIES,
    max_seed_queries: int = 6,
) -> None:
    """Cross-validate/expand candidates using Reddit as a second signal source.

    Rather than trying to extract arbitrary phrases from post titles with NLP,
    this reuses the beauty taxonomy (ingredients/benefits/concerns) as the
    phrase dictionary to scan titles against - consistent with the rest of the
    script's keyword-matching approach, and free of any Anthropic API cost.
    Mutates `candidates` in place: existing entries gain "reddit" as a
    discovery source (boosting their multi-source/confidence score), and
    taxonomy terms mentioned only on Reddit are added as new candidates.
    """
    phrase_pool = sorted({term for terms in taxonomy.values() for term in terms})
    if not phrase_pool:
        return

    mention_counts: Counter[str] = Counter()
    queries: list[tuple[str, dict]] = []
    for seed in seeds[:max_seed_queries]:
        queries.append((seed, {"q": seed, "sort": "hot", "t": "week", "limit": 25}))
    if profile == "beauty":
        for subreddit in REDDIT_BEAUTY_SUBREDDITS:
            queries.append((subreddit, {"q": seeds[0] if seeds else "", "restrict_sr": 1, "sort": "hot", "t": "week", "limit": 25}))

    for index, (label, params) in enumerate(queries):
        if index > 0:
            time.sleep(REDDIT_REQUEST_DELAY_SECONDS)
        if label in REDDIT_BEAUTY_SUBREDDITS:
            url = REDDIT_SUBREDDIT_SEARCH_BASE.format(subreddit=label)
        else:
            url = REDDIT_SEARCH_BASE
        data = reddit_get(url, params, timeout=request_timeout, retries=request_retries)
        if not data:
            continue
        posts = data.get("data", {}).get("children", [])
        for post in posts:
            title = normalize(post.get("data", {}).get("title", ""))
            if not title:
                continue
            for term in phrase_pool:
                if normalize(term) in title:
                    mention_counts[term] += 1

    for term, count in mention_counts.items():
        if count < REDDIT_MIN_MENTIONS:
            continue
        key = normalize(term)
        if not key:
            continue
        candidate = candidates.get(key)
        if candidate is None:
            candidate = Candidate(query=term)
            candidates[key] = candidate
        candidate.discovery_sources.add("reddit")
        candidate.rising_bucket_hits += count


def clamp(value: float, minimum: int = 0, maximum: int = 100) -> int:
    return int(max(minimum, min(maximum, round(value))))


def score_candidate(candidate: Candidate) -> None:
    scores = candidate.interest_scores
    if scores:
        candidate.first_interest = scores[0]
        candidate.latest_interest = scores[-1]
        candidate.peak_interest = max(scores)
        candidate.avg_interest = mean(scores)
        candidate.slope = scores[-1] - scores[0]
        midpoint = max(1, len(scores) // 2)
        first_slice = scores[:midpoint]
        second_slice = scores[midpoint:]
        # A single-point (or otherwise lopsided) series can leave one slice
        # empty; mean([]) raises StatisticsError, so fall back to the only
        # value available instead of crashing the whole run.
        first_half = mean(first_slice) if first_slice else scores[0]
        second_half = mean(second_slice) if second_slice else first_half
        candidate.acceleration = round(second_half - first_half)

    rising = candidate.rising_value or 0
    faded_spike = bool(scores and candidate.latest_interest == 0 and candidate.peak_interest < 15)
    rising_score = 100 if rising >= 5000 else clamp(rising / 10)
    headroom_score = clamp(100 - candidate.avg_interest) if scores else 55
    slope_score = clamp(50 + candidate.slope) if scores else 50
    acceleration_score = clamp(50 + candidate.acceleration) if scores else 50
    multi_source_score = clamp(len(candidate.discovery_sources) * 30 + len(candidate.seed_terms) * 10)

    candidate.emergence_score = clamp((rising_score * 0.45) + (headroom_score * 0.25) + (multi_source_score * 0.30))
    candidate.velocity_score = clamp((slope_score * 0.55) + (acceleration_score * 0.25) + (candidate.latest_interest * 0.20))
    if faded_spike:
        candidate.velocity_score = min(candidate.velocity_score, 25)
        candidate.emergence_score = min(candidate.emergence_score, 45)
    candidate.confidence_score = clamp((len(candidate.discovery_sources) * 25) + (35 if scores else 0) + (15 if candidate.rising_value else 0))
    candidate.radar_score = clamp((candidate.emergence_score * 0.45) + (candidate.velocity_score * 0.35) + (candidate.confidence_score * 0.20))

    # Whitespace/opportunity: high emergence + low saturation is the actual
    # "get there before it's crowded" signal, not just "is this trending".
    # Saturation approximates how mainstream/established a term already is by
    # how often it showed up in Google Trends' "top" bucket (established
    # queries) versus only the "rising" bucket (newly emerging).
    total_bucket_hits = candidate.top_bucket_hits + candidate.rising_bucket_hits
    top_ratio = (candidate.top_bucket_hits / total_bucket_hits) if total_bucket_hits else 0.5
    candidate.saturation_score = clamp(top_ratio * 100)
    candidate.opportunity_score = clamp((candidate.emergence_score * 0.6) + ((100 - candidate.saturation_score) * 0.4))

    if not faded_spike and (rising >= 5000 or candidate.radar_score >= 84):
        candidate.trend_stage = "breakout"
        candidate.urgency = "today"
    elif candidate.radar_score >= 70 or rising >= 500:
        candidate.trend_stage = "emerging"
        candidate.urgency = "this_week"
    elif candidate.radar_score >= 55 or candidate.slope > 15:
        candidate.trend_stage = "rising"
        candidate.urgency = "monitor"
    else:
        candidate.trend_stage = "watch"
        candidate.urgency = "monitor"

    if candidate.confidence_score >= 75:
        candidate.confidence = "high"
    elif candidate.confidence_score >= 50:
        candidate.confidence = "medium"
    else:
        candidate.confidence = "low"

    reason_bits = []
    if candidate.rising_label:
        reason_bits.append(f"Google Trends labels it {candidate.rising_label}")
    if scores:
        reason_bits.append(f"interest moved from {candidate.first_interest} to {candidate.latest_interest}")
    else:
        reason_bits.append("time-series validation was skipped or unavailable")
    if faded_spike:
        reason_bits.append("latest interest has faded after a small spike")
    if candidate.discovery_sources:
        reason_bits.append(f"found through {', '.join(sorted(candidate.discovery_sources))}")
    candidate.why_now = "; ".join(reason_bits) or "Candidate appeared in Google Trends related discovery"

    if candidate.trend_stage == "breakout":
        candidate.recommended_action = "Prioritize a same-day brief, then validate sources before publishing."
    elif candidate.trend_stage == "emerging":
        candidate.recommended_action = "Build an angle this week and monitor the next 24-48 hours."
    elif candidate.trend_stage == "rising":
        candidate.recommended_action = "Track as a developing query and compare against existing coverage."
    else:
        candidate.recommended_action = "Keep on watchlist unless another signal channel confirms it."


def candidate_to_dict(candidate: Candidate, rank: int) -> dict:
    return {
        "rank": rank,
        "topic": candidate.query,
        "trend_stage": candidate.trend_stage,
        "urgency": candidate.urgency,
        "radar_score": candidate.radar_score,
        "emergence_score": candidate.emergence_score,
        "velocity_score": candidate.velocity_score,
        "confidence_score": candidate.confidence_score,
        "saturation_score": candidate.saturation_score,
        "opportunity_score": candidate.opportunity_score,
        "confidence": candidate.confidence,
        "rising_label": candidate.rising_label,
        "latest_interest": candidate.latest_interest,
        "peak_interest": candidate.peak_interest,
        "slope": candidate.slope,
        "acceleration": candidate.acceleration,
        "seed_terms": sorted(candidate.seed_terms),
        "discovery_sources": sorted(candidate.discovery_sources),
        "interest_scores": candidate.interest_scores,
        "tags": candidate.tags,
        "why_now": candidate.why_now,
        "recommended_action": candidate.recommended_action,
    }


def build_data(
    topic: str,
    geo: str,
    date: str,
    seeds: list[str],
    candidates: list[Candidate],
    rejected: list[dict],
    extra_anchor_terms: list[str] | None = None,
    trending_now_terms: list[str] | None = None,
    trending_now_context: list[dict] | None = None,
    autocomplete_terms: list[str] | None = None,
    exclusion_terms: list[str] | None = None,
) -> dict:
    exclusions = {normalize(term) for term in (exclusion_terms or []) if normalize(term)}
    anchors = relevance_anchors(topic, seeds)
    if extra_anchor_terms:
        # Reddit/taxonomy-sourced candidates (e.g. "ceramides") often aren't a
        # literal substring of the topic/seed anchors even though they're
        # on-topic, so widen the anchor set with the taxonomy terms used to
        # discover them rather than dropping them as off-topic noise.
        #
        # Deliberately NOT using relevance_anchors() here: it decomposes each
        # term into standalone word tokens (>=4 chars), which is fine for a
        # short, curated seed list but not for a ~60-term taxonomy pulled from
        # a config file - a benefit like "even skin tone" would contribute the
        # bare token "even", which then matches any candidate containing
        # "events" (confirmed in production: "upcoming events" slipped through
        # this way). Full-phrase-only anchors avoid that whole class of bug.
        anchors |= {normalize(term) for term in extra_anchor_terms if normalize(term)}
    relevant = []
    off_topic = []
    for candidate in candidates:
        normalized_query = normalize(candidate.query)
        excluded_term = next((term for term in exclusions if term in normalized_query), None)
        if excluded_term:
            # Anchor-matched but a different sense of the seed word (e.g.
            # "peptides" the skincare ingredient vs. "peptides" the
            # injectable research chemical) - see beauty_taxonomy.yaml.
            off_topic.append(candidate)
            rejected.append({
                "topic": candidate.query,
                "reason": f"Off-topic: matched exclusion term {excluded_term!r}",
                "seed_terms": sorted(candidate.seed_terms),
            })
        elif is_relevant_candidate(candidate, anchors):
            relevant.append(candidate)
        else:
            off_topic.append(candidate)
            # Off-topic candidates cluster by originating seed (e.g. a thin
            # "diet news"/"diet products" combo falling back to Google's
            # generic trending-searches filler) - keeping the seed(s) here
            # lets us trace and prune the offending seed instead of guessing.
            rejected.append({
                "topic": candidate.query,
                "reason": "Off-topic after expanded seed scan",
                "seed_terms": sorted(candidate.seed_terms),
            })

    retained = [c for c in relevant if c.radar_score >= 50]
    weak = [c for c in relevant if c.radar_score < 50]
    for candidate in weak:
        rejected.append({"topic": candidate.query, "reason": f"Weak radar score ({candidate.radar_score})"})
    retained.sort(key=lambda c: c.radar_score, reverse=True)

    stages = {}
    for candidate in retained:
        stages[candidate.trend_stage] = stages.get(candidate.trend_stage, 0) + 1

    return {
        "run_date": datetime.now().strftime("%Y-%m-%d"),
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "topic": topic,
        "geo": geo,
        "date_window": date,
        "seed_terms": seeds,
        "trending_now_terms_used": trending_now_terms or [],
        "trending_now_context": [
            {
                "query": item["query"],
                "headline": item.get("news_headline", ""),
                "source": item.get("news_source", ""),
                "link": item.get("news_link", ""),
            }
            for item in (trending_now_context or [])
            if item.get("news_headline")
        ],
        "autocomplete_terms_used": autocomplete_terms or [],
        "methodology": "Google Trends related-query/topic discovery, time-series validation, emergence scoring, confidence routing",
        "summary": {
            "seed_count": len(seeds),
            "total_reviewed": len(candidates),
            "total_retained": len(retained),
            "total_rejected": len(rejected),
            "breakouts": stages.get("breakout", 0),
            "emerging": stages.get("emerging", 0),
            "rising": stages.get("rising", 0),
            "notes": "Scores are relative Google Trends signals, not absolute search volume. Treat low-confidence trends as watchlist items until another channel confirms them.",
        },
        "candidates": [candidate_to_dict(candidate, index + 1) for index, candidate in enumerate(retained)],
        "rejected": rejected,
    }


def _escape_script_close(match: re.Match) -> str:
    # Preserve the matched case (</script vs </SCRIPT, etc.) while breaking
    # up the sequence so it can't prematurely close the surrounding
    # <script> tag when spliced into the HTML template.
    return "<\\/" + match.group(0)[2:]


def generate_html(data: dict) -> str:
    if not TEMPLATE_PATH.exists():
        raise FileNotFoundError(f"Template not found: {TEMPLATE_PATH}")
    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    payload = json.dumps(data, ensure_ascii=False, indent=2)
    # HTML parsers close a <script> tag on the first literal "</script"
    # substring regardless of quoting, so a keyword/title containing it
    # could break out of the JSON payload and inject markup. Escape it.
    payload = re.sub(r"</script", _escape_script_close, payload, flags=re.IGNORECASE)
    return template.replace("__RADAR_DATA__", payload)


FORMULA_TRIGGER_CHARS = ("=", "+", "-", "@")
# Fields whose values are free-text/external and must be neutralized against
# CSV formula injection before being written out.
CSV_FORMULA_RISK_FIELDS = (
    "topic", "trend_stage", "urgency", "confidence", "rising_label",
    "seed_terms", "discovery_sources", "tags", "why_now", "recommended_action",
)


def csv_safe(value: str) -> str:
    """Prefix values that Excel/Sheets would interpret as a formula.

    csv.writer already quote-escapes special characters; this guards against
    a separate risk where a leading =, +, -, or @ makes the spreadsheet
    application evaluate the cell as a formula.
    """
    text = "" if value is None else str(value)
    if text.lstrip().startswith(FORMULA_TRIGGER_CHARS):
        return "'" + text
    return text


def write_csv(data: dict, path: Path) -> None:
    fieldnames = [
        "rank", "topic", "trend_stage", "urgency", "radar_score",
        "emergence_score", "velocity_score", "confidence_score",
        "saturation_score", "opportunity_score", "confidence",
        "rising_label", "latest_interest", "peak_interest", "slope",
        "seed_terms", "discovery_sources", "tags", "why_now", "recommended_action",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in data.get("candidates", []):
            normalized = dict(row)
            normalized["seed_terms"] = "; ".join(row.get("seed_terms", []))
            normalized["discovery_sources"] = "; ".join(row.get("discovery_sources", []))
            tags = row.get("tags") or {}
            normalized["tags"] = "; ".join(f"{tag_type}: {', '.join(terms)}" for tag_type, terms in tags.items())
            for key in CSV_FORMULA_RISK_FIELDS:
                if key in normalized:
                    normalized[key] = csv_safe(normalized[key])
            writer.writerow({field: normalized.get(field, "") for field in fieldnames})


def build_email_body(data: dict) -> str:
    def esc(value) -> str:
        # Trends/News-derived text (keywords, titles, notes, ...) is
        # untrusted and gets f-string-spliced straight into raw HTML below;
        # escape it so it can't inject markup into the email client.
        return html.escape(str(value)) if value is not None else ""

    candidates = data.get("candidates", [])
    summary = data.get("summary", {})
    top_rows = ""
    for candidate in candidates[:10]:
        top_rows += f"""
        <tr>
          <td style="padding:8px 10px;border-bottom:1px solid #e7e5e0;color:#777;font-family:Menlo,Consolas,monospace;font-size:12px;">{candidate.get('rank','')}</td>
          <td style="padding:8px 10px;border-bottom:1px solid #e7e5e0;">
            <strong>{esc(candidate.get('topic',''))}</strong><br>
            <span style="color:#666;font-size:12px;">{esc(candidate.get('why_now',''))}</span>
          </td>
          <td style="padding:8px 10px;border-bottom:1px solid #e7e5e0;font-family:Menlo,Consolas,monospace;font-size:12px;">{esc(candidate.get('trend_stage',''))}</td>
          <td style="padding:8px 10px;border-bottom:1px solid #e7e5e0;font-family:Menlo,Consolas,monospace;font-size:12px;">{candidate.get('radar_score','')}</td>
          <td style="padding:8px 10px;border-bottom:1px solid #e7e5e0;font-family:Menlo,Consolas,monospace;font-size:12px;">{candidate.get('opportunity_score','')}</td>
        </tr>"""

    return f"""<!doctype html>
<html>
<body style="margin:0;padding:24px;background:#fbfaf8;color:#2b2b2b;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;">
  <div style="max-width:760px;margin:0 auto;">
    <div style="font-size:12px;text-transform:uppercase;letter-spacing:.08em;color:#cf2f32;font-weight:700;">Google Trend Radar</div>
    <h1 style="font-family:Georgia,'Times New Roman',serif;margin:8px 0 6px;color:#171717;">{esc(data.get('topic','Trend'))} Radar</h1>
    <div style="color:#666;font-size:13px;margin-bottom:18px;">{esc(data.get('geo','US'))} · {esc(data.get('date_window',''))} · {esc(data.get('run_date',''))}</div>

    <table width="100%" cellpadding="0" cellspacing="8" style="margin:0 0 18px;">
      <tr>
        <td style="background:#fff;border:1px solid #dedbd4;border-top:3px solid #cf2f32;border-radius:6px;padding:14px;">
          <div style="font-size:28px;font-family:Georgia,'Times New Roman',serif;color:#cf2f32;font-weight:700;">{summary.get('total_reviewed',0)}</div>
          <div style="font-size:12px;color:#666;font-weight:700;">Signals Reviewed</div>
        </td>
        <td style="background:#fff;border:1px solid #dedbd4;border-top:3px solid #1f9d55;border-radius:6px;padding:14px;">
          <div style="font-size:28px;font-family:Georgia,'Times New Roman',serif;color:#1f9d55;font-weight:700;">{summary.get('total_retained',0)}</div>
          <div style="font-size:12px;color:#666;font-weight:700;">Retained Trends</div>
        </td>
        <td style="background:#fff;border:1px solid #dedbd4;border-top:3px solid #d97706;border-radius:6px;padding:14px;">
          <div style="font-size:28px;font-family:Georgia,'Times New Roman',serif;color:#d97706;font-weight:700;">{summary.get('breakouts',0)}</div>
          <div style="font-size:12px;color:#666;font-weight:700;">Breakouts</div>
        </td>
      </tr>
    </table>

    <div style="background:#eff6ff;border:1px solid #b7d4ff;border-left:4px solid #2563eb;border-radius:6px;padding:12px 14px;color:#183052;font-size:13px;margin-bottom:18px;">
      Full interactive dashboard and CSV are attached.
    </div>

    <table width="100%" cellpadding="0" cellspacing="0" style="background:#fff;border:1px solid #dedbd4;border-radius:6px;border-collapse:collapse;">
      <tr style="background:#f1f0ec;">
        <th style="text-align:left;padding:9px 10px;font-size:11px;color:#666;text-transform:uppercase;">#</th>
        <th style="text-align:left;padding:9px 10px;font-size:11px;color:#666;text-transform:uppercase;">Trend</th>
        <th style="text-align:left;padding:9px 10px;font-size:11px;color:#666;text-transform:uppercase;">Stage</th>
        <th style="text-align:left;padding:9px 10px;font-size:11px;color:#666;text-transform:uppercase;">Score</th>
        <th style="text-align:left;padding:9px 10px;font-size:11px;color:#666;text-transform:uppercase;">Opportunity</th>
      </tr>
      {top_rows}
    </table>
  </div>
</body>
</html>"""


def attach_file(message: MIMEMultipart, path: Path, mime_type: str) -> None:
    maintype, subtype = mime_type.split("/", 1)
    with path.open("rb") as handle:
        part = MIMEBase(maintype, subtype)
        part.set_payload(handle.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f'attachment; filename="{path.name}"')
    message.attach(part)


def send_email(data: dict, html_path: Path, csv_path: Path, json_path: Path | None = None) -> None:
    sender = os.getenv("EMAIL_SENDER", "").strip()
    password = os.getenv("EMAIL_PASSWORD", "").strip()
    recipient = os.getenv("EMAIL_RECIPIENT", "").strip()
    smtp_host = os.getenv("EMAIL_SMTP_HOST", "smtp.gmail.com").strip()
    smtp_port = int(os.getenv("EMAIL_SMTP_PORT", "587"))

    if not all([sender, password, recipient]):
        raise RuntimeError("Email settings missing. Set EMAIL_SENDER, EMAIL_PASSWORD, and EMAIL_RECIPIENT in .env.")

    subject = f"Google Trend Radar Test - {data.get('topic','Trend')} - {data.get('run_date','')}"
    message = MIMEMultipart("mixed")
    message["Subject"] = subject
    message["From"] = sender
    message["To"] = recipient
    message.attach(MIMEText(build_email_body(data), "html", "utf-8"))

    attach_file(message, html_path, "text/html")
    attach_file(message, csv_path, "text/csv")
    if json_path and json_path.exists():
        attach_file(message, json_path, "application/json")

    with smtplib.SMTP(smtp_host, smtp_port, timeout=30) as server:
        server.ehlo()
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, recipient, message.as_string())


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a Google Trends radar dashboard for a topic.")
    parser.add_argument("--topic", default="", help="Topic or niche to scan, for example 'AI tools', 'health', or 'wellness'. If omitted, --profile health or --profile wellness becomes the topic.")
    parser.add_argument("--geo", default="US", help="Google Trends geography code. Default: US.")
    parser.add_argument("--date", default="now 7-d", help='Google Trends date window. Default: "now 7-d".')
    parser.add_argument("--seeds", default="", help="Optional comma-separated seed terms to scan in addition to the selected profile.")
    parser.add_argument("--profile", "--seed-profile", dest="seed_profile", default=DEFAULT_SEED_PROFILE, choices=["auto", "wellness", "health", "ai", "beauty", "nutrition", "fitness", "food-safety", "diet", "weight-loss", "mental-health", "gut-health", "none"], help="Seed profile to scan: wellness, health, ai, beauty, nutrition, fitness, food-safety, diet, weight-loss, mental-health, gut-health, none, or auto. Default: auto.")
    parser.add_argument("--max-seeds", type=int, default=DEFAULT_MAX_SEEDS, help="Maximum seed terms to scan. Default: 24.")
    parser.add_argument("--limit", type=int, default=80, help="Maximum discovered candidates to validate. Default: 80.")
    parser.add_argument("--timeout", type=int, default=DEFAULT_REQUEST_TIMEOUT, help="Seconds to wait for each SerpAPI request. Default: 12.")
    parser.add_argument("--retries", type=int, default=DEFAULT_REQUEST_RETRIES, help="Retries per SerpAPI request after timeout/error. Default: 0.")
    parser.add_argument("--include-related-topics", action="store_true", help="Also scan related topics. Slower, but can surface entity-level discoveries.")
    parser.add_argument("--skip-timeseries", action="store_true", help="Skip time-series validation. Faster for discovery runs when SerpAPI is slow.")
    parser.add_argument("--skip-reddit", action="store_true", help="Skip Reddit cross-validation. Reddit search is free/no-auth but rate-limited and can be slow or flaky.")
    parser.add_argument("--skip-trending-now", action="store_true", help="Skip Google Trends 'Trending Now' real-time seed enrichment. On by default when SERPAPI_TRENDING_NOW_ENABLED=true.")
    parser.add_argument("--include-autocomplete", action="store_true", help="Also fetch Google Trends Autocomplete suggestions for the top seeds as extra discovery input. Off by default (adds one SerpAPI call per seed scanned).")
    parser.add_argument("--verbose-errors", action="store_true", help="Print every skipped SerpAPI request instead of only the final summary.")
    parser.add_argument("--email", action="store_true", help="Email the generated dashboard to EMAIL_RECIPIENT with HTML, CSV, and JSON attached.")
    parser.add_argument("--output-dir", default=str(OUTPUT_DIR), help="Directory for dashboard, CSV, and JSON output.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    global VERBOSE_ERRORS
    VERBOSE_ERRORS = args.verbose_errors
    load_env()

    if not os.getenv("SERPAPI_API_KEY", "").strip():
        sys.exit("SERPAPI_API_KEY is not set. Add it to .env or export it before running the radar.")

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    if not args.topic.strip():
        if args.seed_profile in SEED_PROFILES:
            args.topic = args.seed_profile
        else:
            sys.exit("Choose a --profile (wellness, health, ai, beauty, nutrition, fitness, food-safety, diet, weight-loss, mental-health, gut-health), or provide --topic.")

    seeds = build_seed_terms(args.topic, args.seeds, args.seed_profile, args.max_seeds)
    taxonomy = load_taxonomy()

    trending_now_items: list[dict] = []
    trending_now_terms: list[str] = []
    if not args.skip_trending_now:
        trending_now_items = fetch_trending_now(geo=args.geo)
        print(f"Trending Now (Health, category_id=7): {len(trending_now_items)} term(s)")
        if trending_now_items:
            enrich_trending_now_news(trending_now_items, request_timeout=args.timeout, request_retries=args.retries)

        if args.seed_profile == "beauty":
            # The default category (Health) rarely surfaces anything
            # actually beauty-specific, so pull the Beauty and Fashion
            # category too instead of only ever getting health spillover.
            # Enriched separately (not after merging) so beauty terms get
            # their own news-lookup budget rather than losing every slot to
            # whichever health terms happened to come first in the list.
            beauty_trending_items = fetch_trending_now(
                geo=args.geo, category_id=BEAUTY_TRENDING_NOW_CATEGORY_ID, hours=BEAUTY_TRENDING_NOW_HOURS,
            )
            print(
                f"Trending Now (Beauty and Fashion, category_id=2, "
                f"hours={BEAUTY_TRENDING_NOW_HOURS}): {len(beauty_trending_items)} term(s)"
            )
            if beauty_trending_items:
                enrich_trending_now_news(beauty_trending_items, request_timeout=args.timeout, request_retries=args.retries)
            seen_queries = {normalize(item["query"]) for item in trending_now_items}
            added = 0
            for item in beauty_trending_items:
                key = normalize(item["query"])
                if key and key not in seen_queries:
                    seen_queries.add(key)
                    trending_now_items.append(item)
                    added += 1
            print(f"Trending Now: merged {added} beauty term(s) not already present from Health")

        if trending_now_items:
            trending_now_terms = [item["query"] for item in trending_now_items]
            print(f"Trending Now: {len(trending_now_terms)} real-time terms found")
            enriched_count = sum(1 for item in trending_now_items if item.get("news_headline"))
            if enriched_count:
                print(f"Trending Now: found the driving news story for {enriched_count} term(s)")
            seeds = list(dict.fromkeys(seeds + trending_now_terms))

    autocomplete_terms: list[str] = []
    if args.include_autocomplete:
        for seed in seeds[:5]:
            autocomplete_terms.extend(fetch_autocomplete(seed))
        autocomplete_terms = list(dict.fromkeys(autocomplete_terms))
        if autocomplete_terms:
            print(f"Autocomplete: {len(autocomplete_terms)} suggestions found")
            seeds = list(dict.fromkeys(seeds + autocomplete_terms))

    print(f"Scanning Google Trends for '{args.topic}' ({args.geo}, {args.date})...")
    print(f"Seed terms ({len(seeds)}): {', '.join(seeds)}")
    candidates, rejected = discover_candidates(
        args.topic,
        seeds,
        args.geo,
        args.date,
        args.limit,
        include_related_topics=args.include_related_topics,
        request_timeout=args.timeout,
        request_retries=args.retries,
    )
    tag_discovery_source(candidates, trending_now_terms, "trending_now")
    tag_discovery_source(candidates, autocomplete_terms, "autocomplete")

    # Reddit cross-validation is only meaningful for the beauty profile today
    # (the taxonomy phrase pool is beauty-specific), and running it for
    # unrelated profiles would just be wasted requests against Reddit's
    # anonymous rate limit.
    if not args.skip_reddit and args.seed_profile == "beauty":
        print("Cross-checking Reddit for beauty signal...")
        candidates_by_key = {normalize(c.query): c for c in candidates}
        discover_reddit_candidates(
            candidates_by_key,
            seeds,
            taxonomy,
            args.seed_profile,
            request_timeout=args.timeout,
            request_retries=args.retries,
        )
        candidates = list(candidates_by_key.values())

    if not args.skip_timeseries:
        attach_timeseries(candidates, args.geo, args.date, request_timeout=args.timeout, request_retries=args.retries)
    for candidate in candidates:
        try:
            candidate.tags = tag_candidate(candidate.query, taxonomy)
            score_candidate(candidate)
        except Exception as exc:
            # A single candidate with sparse/malformed data must not take
            # down the whole run; log it and move on to the next one.
            print(f"Skipping candidate '{candidate.query}' due to scoring error: {exc}", file=sys.stderr)
            continue

    extra_anchor_terms = sorted({term for terms in taxonomy.values() for term in terms}) if args.seed_profile == "beauty" else None
    exclusion_terms = load_exclusion_terms() if args.seed_profile == "beauty" else None
    data = build_data(
        args.topic, args.geo, args.date, seeds, candidates, rejected,
        extra_anchor_terms=extra_anchor_terms,
        trending_now_terms=trending_now_terms,
        trending_now_context=trending_now_items,
        autocomplete_terms=autocomplete_terms,
        exclusion_terms=exclusion_terms,
    )
    stamp = datetime.now().strftime("%Y-%m-%d_%H%M")
    slug = re.sub(r"[^a-z0-9]+", "-", args.topic.lower()).strip("-") or "topic"
    base = f"trend_radar_{slug}_{stamp}"

    json_path = output_dir / f"{base}.json"
    csv_path = output_dir / f"{base}.csv"
    html_path = output_dir / f"{base}.html"

    json_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    write_csv(data, csv_path)
    html_path.write_text(generate_html(data), encoding="utf-8")

    print_request_summary()
    if args.email:
        send_email(data, html_path, csv_path, json_path)
        print(f"Email sent to {os.getenv('EMAIL_RECIPIENT', '').strip()}")
    print(f"Dashboard: {html_path}")
    print(f"CSV:       {csv_path}")
    print(f"JSON:      {json_path}")


if __name__ == "__main__":
    main()
