#!/usr/bin/env python3
"""
run_pipeline.py — Trending Content OS daily runner

Runs the full 12-skill pipeline via the Anthropic API, then generates:
  outputs/daily_newsroom_dashboard/dashboard_YYYY-MM-DD.html  ← visual dashboard
  outputs/daily_newsroom_dashboard/daily_report_YYYY-MM-DD.md ← full pipeline output
  outputs/daily_newsroom_dashboard/dashboard_YYYY-MM-DD.csv   ← spreadsheet export

And optionally emails the results to EMAIL_RECIPIENT (set in .env).

Usage:
    python run_pipeline.py                          # run once now
    python run_pipeline.py --schedule --time 07:00  # run daily at 7am
    python run_pipeline.py --no-email               # skip email this run

Cron (add with: crontab -e):
    0 7 * * * /usr/bin/python3 /path/to/run_pipeline.py >> /path/to/outputs/pipeline.log 2>&1

Requirements:
    pip install anthropic python-dotenv schedule

.env setup:
    ANTHROPIC_API_KEY=sk-ant-...
    SERPAPI_API_KEY=your-serpapi-key      # https://serpapi.com — enables Google News + Trends
    EMAIL_SENDER=you@gmail.com
    EMAIL_PASSWORD=your-gmail-app-password   # https://myaccount.google.com/apppasswords
    EMAIL_RECIPIENT=meagan@hurrdat.com
    EMAIL_SMTP_HOST=smtp.gmail.com           # optional, default: smtp.gmail.com
    EMAIL_SMTP_PORT=587                      # optional, default: 587
"""

import os
import sys
import csv
import json
import re
import html
import difflib
import argparse
import logging
import time
import urllib.parse
import urllib.request
import urllib.error
import yaml
from datetime import datetime, timedelta
from pathlib import Path

# ── Paths ─────────────────────────────────────────────────────────────────────
PROJECT_ROOT   = Path(__file__).resolve().parent
ENV_PATH       = PROJECT_ROOT / ".env"
CONFIGS_DIR    = PROJECT_ROOT / "configs"
SKILLS_DIR     = PROJECT_ROOT / "skills"
PROMPTS_DIR    = PROJECT_ROOT / "prompts"
DATA_DIR       = PROJECT_ROOT / "data"
RUN_HISTORY_PATH     = DATA_DIR / "run_history.yaml"
DEFERRED_TOPICS_PATH = DATA_DIR / "deferred_topics.yaml"
OUTPUT_DIR     = PROJECT_ROOT / "outputs" / "daily_newsroom_dashboard"
TEMPLATE_PATH  = PROJECT_ROOT / "dashboard_template.html"
LOG_PATH       = PROJECT_ROOT / "outputs" / "pipeline.log"


# ── Logging ───────────────────────────────────────────────────────────────────
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)s  %(message)s",
    handlers=[
        logging.FileHandler(LOG_PATH),
        logging.StreamHandler(sys.stdout),
    ],
)
log = logging.getLogger(__name__)


# ── File helpers ──────────────────────────────────────────────────────────────

def load_file(path: Path) -> str:
    if path.exists():
        return path.read_text(encoding="utf-8")
    log.warning(f"Config/prompt file not found: {path} — using fallback placeholder text.")
    return f"[FILE NOT FOUND: {path.name}]"


def build_system_prompt() -> str:
    """Assemble full system context: CLAUDE.md + configs + optional skill files."""
    sections = []

    sections.append("# SYSTEM: CLAUDE.md — Operating Rules\n\n" + load_file(PROJECT_ROOT / "CLAUDE.md"))

    config_files = [
        "project_config.yaml",
        "category_rules.yaml",
        "trusted_sources.yaml",
        "scoring_weights.yaml",
        "competitor_list.yaml",
        "tool_config.yaml",
        "expert_sources.yaml",
    ]
    config_block = "\n\n".join(
        f"## configs/{name}\n\n```yaml\n{load_file(CONFIGS_DIR / name)}\n```"
        for name in config_files
        if (CONFIGS_DIR / name).exists()
    )
    sections.append("# CONFIGS\n\n" + config_block)

    skill_files = sorted(SKILLS_DIR.glob("*.md"))
    if skill_files:
        skill_block = "\n\n".join(
            f"## {sf.name}\n\n{load_file(sf)}"
            for sf in skill_files
        )
        sections.append("# SKILL FILES\n\n" + skill_block)

    return "\n\n---\n\n".join(sections)


# ── SerpAPI signal pre-fetch ──────────────────────────────────────────────────

SERPAPI_BASE = "https://serpapi.com/search"
SERPAPI_TIMEOUT_SECONDS = int(os.getenv("SERPAPI_TIMEOUT_SECONDS", "45"))
SERPAPI_MAX_RETRIES = int(os.getenv("SERPAPI_MAX_RETRIES", "3"))

# Google News queries to run each day for health & wellness signal gathering.
# Google News supports `when:` inside q. SerpAPI docs note `q` can use
# anything valid in Google News search, including `site:` and `when:`.
GOOGLE_NEWS_QUERIES = [
    "health when:7d",
    "wellness when:7d",
    "medical study when:7d",
    "clinical trial health when:7d",
    "FDA recall health when:7d",
    "food safety recall when:7d",
    "nutrition study when:7d",
    "mental health when:7d",
    "weight loss drug when:7d",
    "sleep health when:7d",
    "public health when:7d",
    "consumer health product recall when:7d",
]

# Seed keywords for Google Trends — broad enough to catch breakouts
GOOGLE_TRENDS_KEYWORDS = [
    "health",
    "wellness",
    "nutrition",
    "fitness",
    "food safety",
    "diet",
    "weight loss",
    "mental health",
    "gut health",
]

MAX_NEWS_RESULTS_PER_QUERY = 12
MAX_NEWS_CONTEXT_ITEMS = 60
PIPELINE_MAX_TOKENS = 20000
EXTRACTION_MAX_TOKENS = 12000

AUTOMATION_OUTPUT_CONSTRAINT = """
Automation output mode:
- Complete all pipeline skills internally, but do not print exhaustive intermediate analysis.
- Do not emit full per-candidate entity maps, SERP notes, or source validation logs unless they affect a final decision.
- The report must reach the final Editorial Priority Board.
- Include these sections only: preflight summary, Google News Radar coverage summary, signal summary, Skill 02b routing summary, final priority board, editorial briefs for retained candidates, rejected topics log, integrity flags, and run notes.
- The Google News Radar coverage summary must name the main topic clusters seen in Google News and explain which were retained, rejected, or monitored.
- For each retained candidate, include the fields needed by the extraction schema: priority_level, publish_timing, topic, primary_entity, signal_type, allowed_category, trend_strength_score, opportunity_score, discover_score, urgency, confidence, content_status, source_count, recommended_angle, why_now, primary_headline, next_steps, notes.
- Keep the report concise enough to finish within the output budget.
"""


def _serp_get(params: dict) -> dict | None:
    """Make a single SerpAPI request. Returns parsed JSON or None on failure."""
    api_key = os.getenv("SERPAPI_API_KEY", "").strip()
    if not api_key:
        return None
    request_params = dict(params)
    request_params["api_key"] = api_key
    engine = request_params.get("engine", "?")
    query = request_params.get("q") or request_params.get("engine", "?")
    for attempt in range(1, SERPAPI_MAX_RETRIES + 1):
        try:
            url = SERPAPI_BASE + "?" + urllib.parse.urlencode(request_params)
            with urllib.request.urlopen(url, timeout=SERPAPI_TIMEOUT_SECONDS) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", errors="replace")[:300]
            if e.code == 429 or e.code >= 500:
                if attempt >= SERPAPI_MAX_RETRIES:
                    log.warning(
                        f"SerpAPI request failed ({engine}, {query}) after "
                        f"{SERPAPI_MAX_RETRIES} attempts: HTTP Error {e.code}: {body}"
                    )
                    return None
                log.warning(
                    f"SerpAPI request failed ({engine}, {query}): "
                    f"HTTP Error {e.code}: {body}; retrying "
                    f"{attempt + 1}/{SERPAPI_MAX_RETRIES}..."
                )
                time.sleep(min(2 ** attempt, 8))
                continue
            log.warning(
                f"SerpAPI request failed ({engine}, {query}): "
                f"HTTP Error {e.code}: {body}"
            )
            return None
        except Exception as e:
            if attempt >= SERPAPI_MAX_RETRIES:
                log.warning(
                    f"SerpAPI request failed ({engine}, {query}) after "
                    f"{SERPAPI_MAX_RETRIES} attempts: {e}"
                )
                return None
            log.warning(
                f"SerpAPI request timed out/failed ({engine}, {query}); "
                f"retrying {attempt + 1}/{SERPAPI_MAX_RETRIES}..."
            )
            time.sleep(min(2 ** attempt, 8))
    return None


def fetch_google_news() -> list[dict]:
    """
    Run GOOGLE_NEWS_QUERIES through SerpAPI Google News.
    Returns a deduplicated list of article dicts with keys:
      title, source, date, snippet, link
    """
    seen   = set()
    result = []
    per_query_counts = {}
    for q in GOOGLE_NEWS_QUERIES:
        data = _serp_get({
            "engine": "google_news",
            "q": q,
            "gl": "us",
            "hl": "en",
            "num": MAX_NEWS_RESULTS_PER_QUERY,
        })
        if not data:
            continue
        kept_for_query = 0
        for article in data.get("news_results", []):
            if kept_for_query >= MAX_NEWS_RESULTS_PER_QUERY:
                break
            title = article.get("title", "")
            if not title or title in seen:
                continue
            seen.add(title)
            kept_for_query += 1
            result.append({
                "query":   q,
                "title":   title,
                "source":  article.get("source", {}).get("name", ""),
                "date":    article.get("date", ""),
                "snippet": article.get("snippet", ""),
                "link":    article.get("link", ""),
            })
        per_query_counts[q] = kept_for_query
    log.info(
        f"Google News: fetched {len(result)} unique articles across "
        f"{len(GOOGLE_NEWS_QUERIES)} radar queries"
    )
    log.info(
        "Google News radar counts: "
        + ", ".join(f"{q.replace(' when:7d','')}={n}" for q, n in per_query_counts.items())
    )
    return result


def _extract_related_queries(data: dict) -> list[str]:
    related = data.get("related_queries", {})
    candidates = []
    for key in ("rising", "top"):
        items = related.get(key, [])
        if isinstance(items, dict):
            items = items.get("items", [])
        for item in items[:8]:
            query = item.get("query") or item.get("title")
            if query and query not in candidates:
                candidates.append(query)
    return candidates[:8]


def fetch_google_trends() -> list[dict]:
    """
    Pull Google Trends interest-over-time + related-query data for GOOGLE_TRENDS_KEYWORDS.
    Returns a list of dicts: { keyword, interest_scores: [{"date": ..., "value": ...}] }
    """
    results = []
    for kw in GOOGLE_TRENDS_KEYWORDS:
        timeseries = _serp_get({
            "engine":      "google_trends",
            "q":           kw,
            "data_type":   "TIMESERIES",
            "date":        "now 7-d",   # last 7 days for velocity signal
            "geo":         "US",
        })
        if not timeseries:
            continue

        timeline = timeseries.get("interest_over_time", {}).get("timeline_data", [])
        scores = [
            {"date": pt.get("date", ""), "value": pt.get("values", [{}])[0].get("extracted_value", 0)}
            for pt in timeline
        ]

        related_queries = _serp_get({
            "engine":      "google_trends",
            "q":           kw,
            "data_type":   "RELATED_QUERIES",
            "date":        "now 7-d",
            "geo":         "US",
        }) or {}

        results.append({
            "keyword":        kw,
            "interest_scores": scores,
            "rising_related":  _extract_related_queries(related_queries),
        })
    log.info(f"Google Trends: fetched timeseries + related-query data for {len(results)} seed keywords")
    return results


def fetch_trending_now() -> list[str]:
    """
    Fetch Google Trends 'Trending Now' for the US to catch today's breakout topics.
    Returns a list of trending search terms.
    """
    if os.getenv("SERPAPI_TRENDING_NOW_ENABLED", "").strip().lower() not in {"1", "true", "yes"}:
        log.info("Trending Now: skipped. Set SERPAPI_TRENDING_NOW_ENABLED=true to enable.")
        return []

    data = _serp_get({
        "engine":      "google_trends_trending_now",
        "geo":         "US",
        "hours":       os.getenv("SERPAPI_TRENDING_NOW_HOURS", "24").strip() or "24",
        "category_id": os.getenv("SERPAPI_TRENDING_NOW_CATEGORY_ID", "7").strip() or "7",
        "only_active": "true",
        "hl":          "en",
    })
    if not data:
        return []
    terms = []
    for item in data.get("trending_searches", [])[:20]:
        query = item.get("query", "")
        if query:
            terms.append(query)
    log.info(f"Trending Now: {len(terms)} real-time health trends found")
    return terms


def build_serp_context() -> str:
    """
    Fetch all SerpAPI signals and format them as structured context
    to inject into the pipeline prompt. Returns an empty string if
    SERPAPI_API_KEY is not configured.
    """
    api_key = os.getenv("SERPAPI_API_KEY", "").strip()
    if not api_key:
        log.warning("SERPAPI_API_KEY not set — skipping Google News + Trends pre-fetch.")
        return ""

    log.info("Pre-fetching SerpAPI signals: Google News + Trends...")

    news_articles  = fetch_google_news()
    trends_data    = fetch_google_trends()
    trending_terms = fetch_trending_now()

    sections = []

    # ── Google Trending Now ───────────────────────────────────────────────────
    if trending_terms:
        terms_str = "\n".join(f"  - {t}" for t in trending_terms)
        sections.append(
            f"## Google Trends — Trending Now (US / Health, real-time)\n{terms_str}"
        )

    # ── Google Trends interest over time ─────────────────────────────────────
    if trends_data:
        trend_lines = []
        rising_terms = []
        for t in trends_data:
            scores = t.get("interest_scores", [])
            if scores:
                vals   = [s["value"] for s in scores if isinstance(s.get("value"), (int, float))]
                latest = vals[-1] if vals else "n/a"
                peak   = max(vals) if vals else "n/a"
                delta  = round(vals[-1] - vals[0], 1) if len(vals) >= 2 else 0
                trend_lines.append(
                    f"  - **{t['keyword']}**: latest={latest}, peak={peak}, "
                    f"7d-delta={'+' if delta >= 0 else ''}{delta}"
                )
            if t.get("rising_related"):
                trend_lines.append(f"    Rising related: {', '.join(t['rising_related'])}")
                rising_terms.extend(t["rising_related"])
        if rising_terms:
            unique_rising = []
            for term in rising_terms:
                if term not in unique_rising:
                    unique_rising.append(term)
            trend_lines.append("")
            trend_lines.append("Top rising related queries from Google Trends:")
            trend_lines.extend(f"  - {term}" for term in unique_rising[:20])
        sections.append(
            "## Google Trends — 7-Day Interest (US)\n" + "\n".join(trend_lines)
        )

    # ── Google News articles ──────────────────────────────────────────────────
    if news_articles:
        article_lines = []
        for a in news_articles[:MAX_NEWS_CONTEXT_ITEMS]:   # cap to control context size
            query_label = a.get("query", "").replace(" when:7d", "")
            article_lines.append(
                f"  - ({query_label}) [{a['source']}] {a['date']} — {a['title']}\n"
                f"    {a['snippet']}"
            )
        sections.append(
            f"## Google News Radar — Recent Health Topics "
            f"({len(news_articles)} unique across {len(GOOGLE_NEWS_QUERIES)} queries; "
            f"showing {min(len(news_articles), MAX_NEWS_CONTEXT_ITEMS)})\n"
            "Treat these headlines as the broad radar of news-led health topics. "
            "The Signal Listener must consider this radar before narrowing to retained candidates.\n"
            + "\n".join(article_lines)
        )

    if not sections:
        return ""

    header = (
        "# LIVE SIGNAL DATA — SerpAPI Pre-Fetch\n"
        "The following signals were fetched from SerpAPI Google News and SerpAPI Google Trends "
        "immediately before this pipeline run. Treat Google Trends as AVAILABLE when this "
        "section contains a Google Trends block. Use it as the primary search_velocity input "
        "for Skills 01–05 (Signal Listener through Trend Strength Scorer). Use the Google News "
        "Radar as the broad discovery layer for news-led health topics, including topics that "
        "do not yet appear in Google Trends. Prioritize topics with convergence across News, "
        "Trends, primary/institutional sources, and credible publisher coverage.\n\n"
    )
    return header + "\n\n".join(sections)


def build_pipeline_prompt(serp_context: str = "", history_context: str = "") -> str:
    today = datetime.now().strftime("%Y-%m-%d")
    prompt_path = PROMPTS_DIR / "daily_run_prompt.md"
    if not prompt_path.exists():
        prompt_path = PROJECT_ROOT / "daily-run-prompt.md"
    base  = load_file(prompt_path)
    prefix = f"Today's date: {today}\n\n{AUTOMATION_OUTPUT_CONSTRAINT}\n\n"
    if history_context:
        prefix += history_context + "\n\n---\n\n"
    if serp_context:
        prefix += serp_context + "\n\n---\n\n"
    return prefix + base


def create_message_with_connection_fallback(client, *, label: str, **kwargs):
    """Run an Anthropic request with one explicit retry after SDK retries."""
    try:
        return client.messages.create(**kwargs)
    except Exception as e:
        if e.__class__.__name__ not in {"APIConnectionError", "APITimeoutError"}:
            raise
        log.warning(f"{label} connection failed after SDK retries: {e}. Retrying once...")
        return client.messages.create(**kwargs)


def extract_response_text(response, *, label: str) -> str:
    """
    Safely pull the text out of a Claude API response.
    A refusal, empty response, or non-text content block would otherwise
    raise IndexError/AttributeError and crash the whole run — log a clear
    error with context and fail fast instead, consistent with how other
    unrecoverable pipeline failures in this file (e.g. JSON repair failure)
    are handled.
    """
    content = getattr(response, "content", None)
    if not content:
        log.error(f"{label}: Claude API returned empty content — cannot continue.")
        raise SystemExit(1)
    block = content[0]
    if getattr(block, "type", None) != "text" or not hasattr(block, "text"):
        log.error(
            f"{label}: Claude API returned a non-text content block "
            f"(type={getattr(block, 'type', 'unknown')}) — cannot continue."
        )
        raise SystemExit(1)
    return block.text


def parse_extraction_json(raw_json: str) -> dict:
    """Parse model JSON output after stripping common markdown wrappers."""
    cleaned = raw_json.strip()
    cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned)
    cleaned = re.sub(r"\s*```$", "", cleaned)
    return json.loads(cleaned)


def build_json_repair_prompt(raw_json: str) -> str:
    return f"""Repair the following malformed JSON into one valid JSON object.

Return ONLY valid JSON. Do not include markdown fences or explanation.
Preserve all fields and values from the original as much as possible.

Malformed JSON:
{raw_json}
"""


# ── Recent-topic dedup ──────────────────────────────────────────────────────
# Belt-and-suspenders lexical safety net that runs regardless of whether the
# model actually used the history context below (e.g. if it mislabels a
# repeat as content_status: new anyway). Compares today's candidates against
# the last few days' already-generated dashboard CSVs on disk and drops
# near-duplicate topics before output.
DEDUP_LOOKBACK_DAYS = 5
DEDUP_SIMILARITY_THRESHOLD = 0.6


def _normalize_for_dedup(*parts: str) -> str:
    text = " ".join(p for p in parts if p).lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def load_recent_dashboard_topics(exclude_date: str, days: int = DEDUP_LOOKBACK_DAYS) -> list[dict]:
    """Read topic/primary_entity from the last `days` days of already-written
    dashboard CSVs (excluding today's own file, if one already exists)."""
    if not OUTPUT_DIR.exists():
        return []

    cutoff = datetime.strptime(exclude_date, "%Y-%m-%d") - timedelta(days=days)
    recent = []
    for csv_path in OUTPUT_DIR.glob("dashboard_*.csv"):
        match = re.match(r"^dashboard_(\d{4}-\d{2}-\d{2})\.csv$", csv_path.name)
        if not match:
            continue
        file_date_str = match.group(1)
        if file_date_str == exclude_date:
            continue
        try:
            file_date = datetime.strptime(file_date_str, "%Y-%m-%d")
        except ValueError:
            continue
        if file_date < cutoff:
            continue
        try:
            with csv_path.open(encoding="utf-8") as fh:
                for row in csv.DictReader(fh):
                    topic = (row.get("topic") or "").strip()
                    if not topic:
                        continue
                    recent.append({
                        "date": file_date_str,
                        "topic": topic,
                        "normalized": _normalize_for_dedup(topic, row.get("primary_entity") or ""),
                    })
        except OSError as e:
            log.warning(f"Dedup: could not read {csv_path}: {e}")
    return recent


def filter_recent_duplicates(data: dict, today_str: str) -> dict:
    """Drop candidates that closely match a topic already covered in a
    recent run, moving them into `rejected` with a note instead of silently
    dropping them. Candidates the model itself already tagged as an
    intentional `update` (a deliberate follow-up on new evidence) are left
    alone rather than re-filtered."""
    candidates = data.get("candidates", [])
    if not candidates:
        return data

    recent = load_recent_dashboard_topics(today_str)
    if not recent:
        return data

    kept, dropped = [], []
    for candidate in candidates:
        if candidate.get("content_status") == "update":
            kept.append(candidate)
            continue

        cand_text = _normalize_for_dedup(candidate.get("topic", ""), candidate.get("primary_entity", ""))
        if not cand_text:
            kept.append(candidate)
            continue

        best_ratio, best_match = 0.0, None
        for item in recent:
            ratio = difflib.SequenceMatcher(None, cand_text, item["normalized"]).ratio()
            if ratio > best_ratio:
                best_ratio, best_match = ratio, item

        if best_match and best_ratio >= DEDUP_SIMILARITY_THRESHOLD:
            candidate["content_status"] = "existing"
            dropped.append({
                "topic": candidate.get("topic", ""),
                "reason": (
                    f"Auto-filtered: {best_ratio:.0%} match to '{best_match['topic']}' "
                    f"already covered {best_match['date']}."
                ),
            })
        else:
            kept.append(candidate)

    if dropped:
        log.info(f"Dedup: filtered {len(dropped)} candidate(s) matching recent runs: "
                  f"{[d['topic'] for d in dropped]}")
        data["rejected"] = data.get("rejected", []) + dropped
    data["candidates"] = kept
    return data


# ── Run history & deferred topics ───────────────────────────────────────────
# Implements CLAUDE.md's Skill 01 Step 2 ("check deferred topics") and Daily
# Run Step 9 ("archive run to history") for real: previously these files
# were never read or written by this script, so the model had no memory of
# prior runs at all. build_history_context() feeds recent coverage + due
# deferred topics into the pipeline prompt; archive_run_to_history() and
# update_deferred_topics() persist this run's results afterward. GitHub
# Actions already commits data/run_history.yaml and data/deferred_topics.yaml
# on every run, so once this script writes real data, it persists across days.
HISTORY_LOOKBACK_DAYS = 7
RUN_HISTORY_MAX_ENTRIES = 120
DEFERRED_RECHECK_DAYS = 3
PRIORITY_LEVELS = ("P1", "P2", "P3", "P4", "P5")


def _parse_date_safe(value):
    if not value:
        return None
    try:
        return datetime.strptime(str(value), "%Y-%m-%d").date()
    except ValueError:
        return None


def load_project_config() -> dict:
    path = CONFIGS_DIR / "project_config.yaml"
    if not path.exists():
        return {}
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as e:
        log.warning(f"Could not parse {path}: {e}")
        return {}


def read_deferred_topics() -> list[dict]:
    if not DEFERRED_TOPICS_PATH.exists():
        return []
    try:
        parsed = yaml.safe_load(DEFERRED_TOPICS_PATH.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as e:
        log.warning(f"Could not parse {DEFERRED_TOPICS_PATH}: {e}")
        return []
    return parsed.get("deferred_topics") or []


def write_deferred_topics(topics: list[dict]) -> None:
    DEFERRED_TOPICS_PATH.parent.mkdir(parents=True, exist_ok=True)
    header = (
        "# Deferred topics — overflow from daily runs\n"
        "# Topics here passed scoring thresholds but exceeded max_candidates_returned.\n"
    )
    DEFERRED_TOPICS_PATH.write_text(
        header + yaml.safe_dump({"deferred_topics": topics}, sort_keys=False, allow_unicode=True, width=100),
        encoding="utf-8",
    )


def build_history_context(today_str: str, days: int = HISTORY_LOOKBACK_DAYS) -> str:
    """Format recent coverage + due deferred topics as a prompt section so
    the model actually has the memory CLAUDE.md's dedup/recheck steps assume
    it has, instead of re-discovering the same stories as content_status:new
    every day."""
    sections = []

    recent = load_recent_dashboard_topics(today_str, days=days)
    if recent:
        recent_sorted = sorted(recent, key=lambda r: r["date"], reverse=True)
        lines = "\n".join(f"- {r['date']}: {r['topic']}" for r in recent_sorted)
        sections.append(
            f"## Recent Coverage (last {days} days) — Check Before Selecting\n\n"
            "The topics below were already covered in recent runs. Before adding a "
            "candidate, check whether it is materially the same story. If so, set "
            "`content_status: existing` and reject it — unless there is a specific new "
            "development since it was last covered (new data, new casualty/case count, "
            "new agency action, new study, etc.), in which case set `content_status: "
            "update` and name the new development in `why_now`.\n\n" + lines
        )

    today = datetime.strptime(today_str, "%Y-%m-%d").date()
    due = [
        t for t in read_deferred_topics()
        if (d := _parse_date_safe(t.get("recheck_on"))) and d <= today
    ]
    if due:
        lines = "\n".join(
            f"- {t.get('topic', '')} (entity: {t.get('primary_entity', '')}, "
            f"prior trend={t.get('trend_strength_score', '?')}/opportunity={t.get('opportunity_score', '?')}, "
            f"notes: {t.get('notes', '')})"
            for t in due
        )
        sections.append(
            "## Deferred Topics Due For Recheck\n\n"
            "These topics scored well in a previous run but were cut for exceeding the "
            "daily candidate limit. Consider whether each is still worth including today "
            "given current signals.\n\n" + lines
        )

    return "\n\n---\n\n".join(sections)


def update_deferred_topics(data: dict, today_str: str, max_candidates: int) -> dict:
    """Cap today's candidates at `max_candidates` (by opportunity_score),
    pushing overflow into deferred_topics.yaml for a later recheck. Clears
    previously-deferred entries whose recheck_on date has passed — they were
    surfaced once via build_history_context(), so they get one recheck
    rather than resurfacing indefinitely regardless of outcome."""
    today = datetime.strptime(today_str, "%Y-%m-%d").date()
    still_pending = [
        t for t in read_deferred_topics()
        if not ((d := _parse_date_safe(t.get("recheck_on"))) and d <= today)
    ]

    candidates = data.get("candidates", [])
    if len(candidates) > max_candidates:
        ranked = sorted(candidates, key=lambda c: c.get("opportunity_score", 0), reverse=True)
        kept, overflow = ranked[:max_candidates], ranked[max_candidates:]
        recheck_date = (today + timedelta(days=DEFERRED_RECHECK_DAYS)).strftime("%Y-%m-%d")
        for c in overflow:
            still_pending.append({
                "topic": c.get("topic", ""),
                "primary_entity": c.get("primary_entity", ""),
                "trend_strength_score": c.get("trend_strength_score", 0),
                "opportunity_score": c.get("opportunity_score", 0),
                "recheck_on": recheck_date,
                "notes": f"Deferred {today_str}: exceeded max_candidates_returned ({max_candidates}).",
            })
        data["candidates"] = kept
        log.info(f"Deferred {len(overflow)} candidate(s) exceeding max_candidates_returned={max_candidates}.")

    write_deferred_topics(still_pending)
    return data


def _integrity_flag_count(candidates: list[dict]) -> int:
    count = 0
    for c in candidates:
        text = f"{c.get('notes', '')} {c.get('confidence', '')}".lower()
        if "verify" in text or "flag" in str(c.get("notes", "")).lower():
            count += 1
    return count


def archive_run_to_history(data: dict, today_str: str, dashboard_file: str) -> None:
    """Append this run's results to data/run_history.yaml so the next run's
    build_history_context() has real memory of it."""
    candidates = data.get("candidates", [])
    rejected = data.get("rejected", [])
    summary = data.get("signal_summary", {})

    priority_counts = {level: 0 for level in PRIORITY_LEVELS}
    for c in candidates:
        level = c.get("priority_level")
        if level in priority_counts:
            priority_counts[level] += 1

    top_topic = next((c.get("topic", "") for c in candidates if c.get("priority_level") == "P1"), None)
    if not top_topic and candidates:
        top_topic = candidates[0].get("topic", "")

    entry = {
        "run_date": today_str,
        "niche": data.get("niche", "health and wellness"),
        "signals_reviewed": summary.get("total_reviewed", 0),
        "topics_retained": len(candidates),
        "topics_rejected": len(rejected),
        "p1_count": priority_counts["P1"],
        "p2_count": priority_counts["P2"],
        "p3_count": priority_counts["P3"],
        "p4_count": priority_counts["P4"],
        "p5_count": priority_counts["P5"],
        "integrity_flags": _integrity_flag_count(candidates),
        "top_topic": top_topic or "",
        "key_themes": [c.get("topic", "") for c in candidates if c.get("topic")],
        "tools_used": summary.get("tools_active", []),
        "tools_unavailable": summary.get("tools_unavailable", []),
        "dashboard_file": dashboard_file,
        "notes": summary.get("notes", ""),
    }

    existing = {}
    if RUN_HISTORY_PATH.exists():
        try:
            existing = yaml.safe_load(RUN_HISTORY_PATH.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError as e:
            log.warning(f"Could not parse {RUN_HISTORY_PATH}, starting a fresh history: {e}")

    runs = existing.get("runs") or []
    runs = [r for r in runs if r.get("run_date") != today_str]  # replace same-day entry on re-run
    runs.insert(0, entry)
    runs = runs[:RUN_HISTORY_MAX_ENTRIES]

    header = (
        "# Run History — Trending Content OS\n"
        "# Appended after each completed pipeline run.\n"
        "# Format mirrors Daily Run workflow Step 9 schema.\n\n"
    )
    RUN_HISTORY_PATH.parent.mkdir(parents=True, exist_ok=True)
    RUN_HISTORY_PATH.write_text(
        header + yaml.safe_dump({"runs": runs}, sort_keys=False, allow_unicode=True, width=100),
        encoding="utf-8",
    )
    log.info(f"Run archived → {RUN_HISTORY_PATH} ({len(runs)} total entries)")


def load_env_or_exit() -> None:
    try:
        from dotenv import load_dotenv
    except ImportError:
        sys.exit("Missing dependency: pip install python-dotenv")
    load_dotenv(ENV_PATH)


def run_prefetch_only() -> None:
    load_env_or_exit()
    today_str = datetime.now().strftime("%Y-%m-%d")
    context = build_serp_context()
    if not context:
        log.error("No SerpAPI context generated. Check SERPAPI_API_KEY and network access.")
        raise SystemExit(1)
    out_path = OUTPUT_DIR / f"serp_signals_{today_str}.md"
    out_path.write_text(context, encoding="utf-8")
    log.info(f"SerpAPI signals cached → {out_path}")
    if "Google Trends — 7-Day Interest" in context:
        log.info("Google Trends implementation check: OK — Trends block generated.")
    else:
        log.warning("Google Trends implementation check: no Trends block generated.")
    log.info(
        "Prefetch-only complete. To update the dashboard, run: "
        "python run_pipeline.py --no-email"
    )


# ── JSON extraction prompt ────────────────────────────────────────────────────

JSON_SCHEMA = """
{
  "run_date": "YYYY-MM-DD",
  "niche": "health and wellness",
  "signal_summary": {
    "total_reviewed": 0,
    "total_retained": 0,
    "total_rejected": 0,
    "tools_active": ["web_search", "google_news", "google_trends", "serpapi"],
    "tools_unavailable": [],
    "notes": "..."
  },
  "candidates": [
    {
      "priority_level": "P1",
      "publish_timing": "immediate",
      "topic": "...",
      "primary_entity": "...",
      "signal_type": "breaking_news",
      "allowed_category": "food trends",
      "trend_strength_score": 75,
      "opportunity_score": 85,
      "discover_score": 4,
      "urgency": "today",
      "confidence": "high",
      "content_status": "new",
      "source_count": 3,
      "recommended_angle": "...",
      "why_now": "...",
      "primary_headline": "...",
      "next_steps": "...",
      "notes": ""
    }
  ],
  "rejected": [
    { "topic": "...", "reason": "stale / off-category / weak-signal / etc." }
  ]
}
"""

def build_extraction_prompt(pipeline_output: str) -> str:
    return f"""You just ran the Trending Content OS pipeline. Below is the full output.

Extract the structured data and return ONLY a valid JSON object matching this schema exactly.
No markdown fences, no explanation — raw JSON only.

Schema:
{JSON_SCHEMA}

Rules:
- urgency values must be exactly: now | today | this_week | evergreen
- priority_level values: P1 | P2 | P3 | P4 | P5
- publish_timing values: immediate | short_term | scheduled | evergreen | monitor
- confidence values: high | medium | low
- discover_score: integer 1–5
- trend_strength_score and opportunity_score: integer 0–100
- source_count: integer (count of source_evidence items, or estimate)
- tools_active and tools_unavailable: short lowercase names (e.g. "web_search", "google_news", "google_trends", "serpapi", "ahrefs"). Always list "google_news" and "google_trends" separately when SerpAPI pre-fetch data was present in the pipeline context.
- Include ALL retained candidates and ALL rejected topics from the output

Pipeline output:
{pipeline_output}
"""


# ── HTML generation ───────────────────────────────────────────────────────────

def generate_html(data: dict, today_str: str) -> str:
    """Inject pipeline data JSON into the HTML template."""
    template_path = TEMPLATE_PATH

    # Fall back to sibling of this script if template not in project root
    if not template_path.exists():
        template_path = Path(__file__).resolve().parent / "dashboard_template.html"

    if not template_path.exists():
        log.error(f"dashboard_template.html not found at {template_path}")
        return ""

    html = template_path.read_text(encoding="utf-8")
    data_json = json.dumps(data, indent=2, ensure_ascii=False)
    # Prevent a news title/field containing a literal "</script" from
    # breaking out of the <script type="application/json"> tag — HTML
    # parsers close the tag on that substring regardless of the type attr.
    data_json = re.sub(r"</script", lambda _m: "<\\/script", data_json, flags=re.IGNORECASE)
    html = html.replace("__PIPELINE_DATA__", data_json)
    return html


# ── CSV generation ────────────────────────────────────────────────────────────

CSV_HEADER = (
    "date_detected,priority_level,publish_timing,topic,primary_entity,"
    "signal_type,allowed_category,trend_strength_score,opportunity_score,"
    "discover_score,urgency,confidence,content_status,source_count,"
    "recommended_angle,why_now,primary_headline,next_steps,notes"
)

def generate_csv(data: dict) -> str:
    def esc(val):
        v = str(val).replace('"', '""')
        # Formula-injection guard: Excel/Sheets treats a leading
        # = + - @ as the start of a formula. Neutralize by prefixing
        # with a single quote, which forces text interpretation.
        if v.lstrip()[:1] in ("=", "+", "-", "@"):
            v = "'" + v
        return f'"{v}"'

    rows = [CSV_HEADER]
    for c in data.get("candidates", []):
        row = ",".join([
            esc(data["run_date"]),
            esc(c.get("priority_level", "")),
            esc(c.get("publish_timing", "")),
            esc(c.get("topic", "")),
            esc(c.get("primary_entity", "")),
            esc(c.get("signal_type", "")),
            esc(c.get("allowed_category", "")),
            esc(c.get("trend_strength_score", "")),
            esc(c.get("opportunity_score", "")),
            esc(c.get("discover_score", "")),
            esc(c.get("urgency", "")),
            esc(c.get("confidence", "")),
            esc(c.get("content_status", "")),
            esc(c.get("source_count", "")),
            esc(c.get("recommended_angle", "")),
            esc(c.get("why_now", "")),
            esc(c.get("primary_headline", "")),
            esc(c.get("next_steps", "")),
            esc(c.get("notes", "")),
        ])
        rows.append(row)
    return "\n".join(rows)


# ── Email ─────────────────────────────────────────────────────────────────────

URGENCY_EMOJI = {
    "now":       "🔴",
    "today":     "🟠",
    "this_week": "🟣",
    "evergreen": "🟢",
}
PRIORITY_COLOR = {
    "P1": "#ef4444",
    "P2": "#f97316",
    "P3": "#eab308",
    "P4": "#22c55e",
    "P5": "#6b7280",
}


def build_email_body(data: dict) -> str:
    """
    Generate an email-client-safe HTML summary (inline styles only, no JS).
    Includes run stats, a candidate table, and a rejected log.
    The full interactive dashboard is attached separately.
    """
    today        = data.get("run_date", "")
    summary      = data.get("signal_summary", {})
    candidates   = data.get("candidates", [])
    rejected     = data.get("rejected", [])
    p1_topics    = [c for c in candidates if c.get("priority_level") == "P1"]
    alert_html   = ""

    if p1_topics:
        p1 = p1_topics[0]
        alert_html = f"""
        <tr><td style="padding:0 0 16px">
          <div style="background:#1f1010;border:1px solid #7f1d1d;border-radius:8px;
                      padding:14px 18px;font-size:13px;color:#fca5a5;">
            <strong style="color:#ef4444;">🔴 P1 — Publish Now:</strong>&nbsp;
            {html.escape(str(p1.get('topic','')))}
          </div>
        </td></tr>
        """

    # Stat row
    p1_count  = sum(1 for c in candidates if c.get("priority_level") == "P1")
    p2_count  = sum(1 for c in candidates if c.get("priority_level") == "P2")
    avg_opp   = (
        round(sum(c.get("opportunity_score", 0) for c in candidates) / len(candidates))
        if candidates else 0
    )
    def stat_cell(label, value, sub=""):
        return f"""
        <td style="background:#181c27;border:1px solid #2a2f45;border-radius:8px;
                   padding:14px 16px;text-align:center;width:25%;">
          <div style="font-size:10px;text-transform:uppercase;letter-spacing:.08em;
                      color:#6b7280;margin-bottom:4px;">{label}</div>
          <div style="font-size:22px;font-weight:700;color:#fff;">{value}</div>
          {f'<div style="font-size:11px;color:#6b7280;margin-top:2px;">{sub}</div>' if sub else ''}
        </td>"""

    stats_html = f"""
    <tr><td style="padding:0 0 20px">
      <table width="100%" cellpadding="0" cellspacing="6" border="0">
        <tr>
          {stat_cell("Candidates", len(candidates), "retained")}
          {stat_cell("P1 — Now", p1_count, "publish immediately")}
          {stat_cell("P2 — High", p2_count, "queue next")}
          {stat_cell("Avg Opp", f"{avg_opp}/100", "opportunity score")}
        </tr>
      </table>
    </td></tr>"""

    # Candidate rows
    def score_bar(pct, color):
        filled = max(0, min(100, int(pct)))
        return (
            f'<div style="background:#2a2f45;border-radius:3px;height:5px;width:80px;display:inline-block;vertical-align:middle;">'
            f'<div style="background:{color};height:5px;width:{filled}%;border-radius:3px;"></div></div>'
            f'&nbsp;<span style="font-size:11px;color:#e2e8f0;">{filled}</span>'
        )

    candidate_rows = ""
    for c in candidates:
        p      = c.get("priority_level", "P5")
        pcolor = PRIORITY_COLOR.get(p, "#6b7280")
        u      = c.get("urgency", "this_week")
        emoji  = URGENCY_EMOJI.get(u, "")
        candidate_rows += f"""
        <tr style="border-bottom:1px solid #1e2235;">
          <td style="padding:12px 10px;vertical-align:top;width:44px;">
            <span style="background:#1e1e20;border:1px solid {pcolor};color:{pcolor};
                         font-size:11px;font-weight:700;padding:3px 8px;border-radius:4px;">
              {p}
            </span>
          </td>
          <td style="padding:12px 10px;vertical-align:top;">
            <div style="font-size:13px;font-weight:600;color:#fff;margin-bottom:3px;">
              {emoji} {html.escape(str(c.get('topic','')))}
            </div>
            {f'<div style="font-size:11px;color:#818cf8;font-style:italic;margin-bottom:5px;">{html.escape(str(c.get("primary_headline","")))}</div>' if c.get("primary_headline") else ''}
            <div style="font-size:11px;color:#9ca3af;">{html.escape(str(c.get("recommended_angle","")))}</div>
          </td>
          <td style="padding:12px 10px;vertical-align:top;white-space:nowrap;">
            <div style="margin-bottom:4px;">{score_bar(c.get("trend_strength_score",0), "#818cf8")}</div>
            <div style="margin-bottom:4px;">{score_bar(c.get("opportunity_score",0), "#4ade80")}</div>
            <div style="font-size:10px;color:#6b7280;margin-top:2px;">
              Discover {c.get("discover_score","—")}/5 &nbsp;·&nbsp; {html.escape(str(c.get("confidence","—")))} confidence
            </div>
          </td>
          <td style="padding:12px 10px;vertical-align:top;font-size:11px;color:#9ca3af;max-width:180px;">
            {html.escape(str(c.get("next_steps","")))}
          </td>
        </tr>"""

    # Rejected rows
    rejected_rows = "".join(
        f'<tr><td style="padding:6px 10px;color:#e2e8f0;font-size:12px;">{html.escape(str(r.get("topic","")))}</td>'
        f'<td style="padding:6px 10px;color:#6b7280;font-size:12px;">{html.escape(str(r.get("reason","")))}</td></tr>'
        for r in rejected
    )
    rejected_table = f"""
    <tr><td style="padding:24px 0 0">
      <div style="font-size:10px;text-transform:uppercase;letter-spacing:.1em;
                  color:#6b7280;border-bottom:1px solid #2a2f45;padding-bottom:8px;margin-bottom:4px;">
        Rejected Topics
      </div>
      <table width="100%" cellpadding="0" cellspacing="0" border="0">
        <tr>
          <th style="text-align:left;padding:6px 10px;font-size:10px;text-transform:uppercase;
                     letter-spacing:.06em;color:#6b7280;border-bottom:1px solid #2a2f45;">Topic</th>
          <th style="text-align:left;padding:6px 10px;font-size:10px;text-transform:uppercase;
                     letter-spacing:.06em;color:#6b7280;border-bottom:1px solid #2a2f45;">Reason</th>
        </tr>
        {rejected_rows}
      </table>
    </td></tr>""" if rejected else ""

    tools_active   = summary.get("tools_active", [])
    tools_inactive = summary.get("tools_unavailable", [])
    tools_html = "".join(
        f'<span style="background:#14291a;border:1px solid #1e4228;color:#4ade80;'
        f'font-size:11px;padding:2px 9px;border-radius:20px;margin-right:5px;">✓ {t}</span>'
        for t in tools_active
    ) + "".join(
        f'<span style="background:#1e1e20;border:1px solid #2a2f45;color:#6b7280;'
        f'font-size:11px;padding:2px 9px;border-radius:20px;margin-right:5px;text-decoration:line-through;">✗ {t}</span>'
        for t in tools_inactive
    )

    return f"""<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head>
<body style="margin:0;padding:0;background:#0f1117;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;">
<table width="100%" cellpadding="0" cellspacing="0" border="0"
       style="background:#0f1117;padding:32px 16px;">
  <tr><td>
    <table width="100%" cellpadding="0" cellspacing="0" border="0"
           style="max-width:680px;margin:0 auto;">

      <!-- Header -->
      <tr><td style="padding:0 0 24px">
        <table width="100%" cellpadding="0" cellspacing="0" border="0">
          <tr>
            <td>
              <div style="font-size:20px;font-weight:700;color:#fff;">📰 Trending Content OS</div>
              <div style="font-size:12px;color:#6b7280;margin-top:2px;">
                Daily brief — health &amp; wellness &nbsp;·&nbsp; {today}
              </div>
            </td>
            <td style="text-align:right;vertical-align:top;">
              <div style="font-size:11px;color:#6b7280;line-height:1.8;">
                <strong style="color:#e2e8f0;">{summary.get('total_reviewed',0)}</strong> signals reviewed<br>
                <strong style="color:#e2e8f0;">{summary.get('total_retained',0)}</strong> retained &nbsp;·&nbsp;
                <strong style="color:#e2e8f0;">{summary.get('total_rejected',0)}</strong> rejected
              </div>
            </td>
          </tr>
        </table>
      </td></tr>

      <!-- Alert -->
      {alert_html}

      <!-- Stats -->
      {stats_html}

      <!-- Tools -->
      <tr><td style="padding:0 0 20px">{tools_html}</td></tr>

      <!-- Candidate table -->
      <tr><td>
        <div style="font-size:10px;text-transform:uppercase;letter-spacing:.1em;
                    color:#6b7280;border-bottom:1px solid #2a2f45;padding-bottom:8px;margin-bottom:4px;">
          Priority Board
        </div>
        <table width="100%" cellpadding="0" cellspacing="0" border="0"
               style="background:#181c27;border:1px solid #2a2f45;border-radius:10px;overflow:hidden;">
          <tr style="background:#1e2235;">
            <th style="padding:9px 10px;text-align:left;font-size:10px;text-transform:uppercase;
                       letter-spacing:.06em;color:#6b7280;font-weight:500;">P</th>
            <th style="padding:9px 10px;text-align:left;font-size:10px;text-transform:uppercase;
                       letter-spacing:.06em;color:#6b7280;font-weight:500;">Topic &amp; Angle</th>
            <th style="padding:9px 10px;text-align:left;font-size:10px;text-transform:uppercase;
                       letter-spacing:.06em;color:#6b7280;font-weight:500;">Scores</th>
            <th style="padding:9px 10px;text-align:left;font-size:10px;text-transform:uppercase;
                       letter-spacing:.06em;color:#6b7280;font-weight:500;">Next Steps</th>
          </tr>
          {candidate_rows}
        </table>
      </td></tr>

      <!-- Rejected -->
      {rejected_table}

      <!-- Notes -->
      {f'<tr><td style="padding:20px 0 0"><div style="background:#181c27;border:1px solid #2a2f45;border-radius:8px;padding:12px 14px;font-size:12px;color:#9ca3af;line-height:1.6;"><strong style="color:#e2e8f0;">Run notes:</strong> {html.escape(str(summary.get("notes","")))}</div></td></tr>' if summary.get("notes") else ''}

      <!-- Footer -->
      <tr><td style="padding:28px 0 0;border-top:1px solid #2a2f45;margin-top:24px;">
        <div style="font-size:11px;color:#6b7280;">
          Trending Content OS &nbsp;·&nbsp; Generated by Claude &nbsp;·&nbsp;
          Interactive dashboard + CSV attached.
        </div>
      </td></tr>

    </table>
  </td></tr>
</table>
</body>
</html>"""


def send_email(
    data: dict,
    html_path: Path,
    csv_path: Path,
    today_str: str,
) -> None:
    """Send the daily brief email with dashboard HTML + CSV attached via Resend."""
    try:
        import resend
    except ImportError:
        log.error("Missing dependency: pip install resend")
        return

    import base64

    api_key   = os.getenv("RESEND_API_KEY", "").strip()
    sender    = os.getenv("EMAIL_SENDER", "").strip()
    recipient = os.getenv("EMAIL_RECIPIENT", "").strip()

    if not all([api_key, sender, recipient]):
        log.warning(
            "Email skipped — set RESEND_API_KEY, EMAIL_SENDER, and "
            "EMAIL_RECIPIENT in .env to enable delivery."
        )
        return

    resend.api_key = api_key

    candidates = data.get("candidates", [])
    p1_count   = sum(1 for c in candidates if c.get("priority_level") == "P1")
    subject    = f"📰 Content OS Daily Brief — {today_str}"
    if p1_count:
        subject += f" ({p1_count} P1{'s' if p1_count > 1 else ''})"

    attachments = []
    for path, filename in [
        (html_path, f"dashboard_{today_str}.html"),
        (csv_path,  f"dashboard_{today_str}.csv"),
    ]:
        if path and path.exists():
            attachments.append({
                "filename": filename,
                "content":  base64.b64encode(path.read_bytes()).decode(),
            })

    try:
        log.info(f"Sending email to {recipient} via Resend...")
        resend.Emails.send({
            "from":        sender,
            "to":          [recipient],
            "subject":     subject,
            "html":        build_email_body(data),
            "attachments": attachments,
        })
        log.info(f"✅ Email sent via Resend → {recipient}")
    except Exception as e:
        log.error(f"Resend email failed: {e}")


# ── Main pipeline runner ──────────────────────────────────────────────────────

def run_pipeline(send_email_flag: bool = True) -> None:
    try:
        import anthropic
    except ImportError:
        sys.exit("Missing dependency: pip install anthropic")

    load_env_or_exit()

    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        log.error("ANTHROPIC_API_KEY not set in .env — cannot run pipeline.")
        sys.exit(1)

    serpapi_key = os.getenv("SERPAPI_API_KEY", "").strip()
    if not serpapi_key:
        log.warning(
            "SERPAPI_API_KEY not set — Google News and Trends signals will be skipped. "
            "Add SERPAPI_API_KEY to .env to enable (https://serpapi.com)."
        )

    today_str = datetime.now().strftime("%Y-%m-%d")
    client    = anthropic.Anthropic(api_key=api_key, timeout=300.0, max_retries=4)

    # ── Step 0: Pre-fetch live signals from SerpAPI ────────────────────────────
    log.info("Step 0/3 — Pre-fetching Google News + Trends signals via SerpAPI...")
    serp_context = build_serp_context()
    if serp_context:
        serp_cache_path = OUTPUT_DIR / f"serp_signals_{today_str}.md"
        serp_cache_path.write_text(serp_context, encoding="utf-8")
        log.info(f"SerpAPI signals cached → {serp_cache_path}")
    else:
        log.info("SerpAPI signals not available — pipeline will use Ahrefs + WebSearch only.")

    # ── Step 1: Run the full pipeline ──────────────────────────────────────────
    log.info("Step 1/4 — Running full pipeline (claude-sonnet-4-6)...")
    history_context = build_history_context(today_str)
    system_prompt = build_system_prompt()
    pipeline_prompt = build_pipeline_prompt(serp_context, history_context)
    log.info(
        f"Prompt sizes — system: {len(system_prompt):,} chars, "
        f"user: {len(pipeline_prompt):,} chars"
    )
    try:
        pipeline_response = create_message_with_connection_fallback(
            client,
            label="Pipeline call",
            model="claude-sonnet-4-6",
            max_tokens=PIPELINE_MAX_TOKENS,
            system=[{"type": "text", "text": system_prompt, "cache_control": {"type": "ephemeral"}}],
            messages=[{"role": "user", "content": pipeline_prompt}],
        )
    except Exception as e:
        if serp_context and e.__class__.__name__ in {"APIConnectionError", "APITimeoutError"}:
            log.warning(
                "Pipeline call still failed with SerpAPI context. "
                "Retrying once with the cached SerpAPI file omitted from the prompt."
            )
            pipeline_response = create_message_with_connection_fallback(
                client,
                label="Pipeline call without SerpAPI context",
                model="claude-sonnet-4-6",
                max_tokens=PIPELINE_MAX_TOKENS,
                system=[{"type": "text", "text": system_prompt, "cache_control": {"type": "ephemeral"}}],
                messages=[{"role": "user", "content": build_pipeline_prompt("", history_context)}],
            )
        else:
            raise
    pipeline_output = extract_response_text(pipeline_response, label="Pipeline call")
    log.info(
        f"Pipeline complete. Tokens in: {pipeline_response.usage.input_tokens}, "
        f"out: {pipeline_response.usage.output_tokens}"
    )

    # Write full markdown report
    report_path = OUTPUT_DIR / f"daily_report_{today_str}.md"
    report_path.write_text(pipeline_output, encoding="utf-8")
    log.info(f"Full report → {report_path}")

    # ── Step 2: Extract structured JSON from the output ───────────────────────
    log.info("Step 2/4 — Extracting structured data (claude-haiku-4-5-20251001)...")
    extraction_response = create_message_with_connection_fallback(
        client,
        label="Extraction call",
        model="claude-haiku-4-5-20251001",   # cheap + fast for extraction
        max_tokens=EXTRACTION_MAX_TOKENS,
        messages=[{
            "role": "user",
            "content": build_extraction_prompt(pipeline_output),
        }],
    )
    raw_json = extract_response_text(extraction_response, label="Extraction call").strip()
    raw_json_path = OUTPUT_DIR / f"raw_extraction_{today_str}.json"
    raw_json_path.write_text(raw_json, encoding="utf-8")
    log.info(f"Raw extraction JSON → {raw_json_path}")

    try:
        data = parse_extraction_json(raw_json)
    except json.JSONDecodeError as e:
        log.warning(f"JSON parse failed: {e}. Asking extraction model to repair raw JSON...")
        repair_response = create_message_with_connection_fallback(
            client,
            label="Extraction JSON repair call",
            model="claude-haiku-4-5-20251001",
            max_tokens=EXTRACTION_MAX_TOKENS,
            messages=[{
                "role": "user",
                "content": build_json_repair_prompt(raw_json),
            }],
        )
        repaired_json = extract_response_text(repair_response, label="Extraction JSON repair call").strip()
        repaired_json_path = OUTPUT_DIR / f"repaired_extraction_{today_str}.json"
        repaired_json_path.write_text(repaired_json, encoding="utf-8")
        log.info(f"Repaired extraction JSON → {repaired_json_path}")
        try:
            data = parse_extraction_json(repaired_json)
        except json.JSONDecodeError as repair_error:
            log.error(
                f"JSON repair failed: {repair_error}. "
                f"Not generating dashboard/CSV to avoid blank placeholder output. "
                f"See {raw_json_path} and {repaired_json_path}."
            )
            raise SystemExit(1)

    # Ensure run_date is set
    data.setdefault("run_date", today_str)

    # Drop candidates that closely match a topic from a recent run — see
    # filter_recent_duplicates() docstring for why this exists.
    data = filter_recent_duplicates(data, today_str)

    # Cap at max_candidates_returned, deferring overflow for a later recheck.
    max_candidates = load_project_config().get("max_candidates_returned", 25)
    data = update_deferred_topics(data, today_str, max_candidates)

    # ── Step 3: Write HTML dashboard + CSV ────────────────────────────────────
    log.info("Step 3/4 — Generating HTML dashboard and CSV...")

    html = generate_html(data, today_str)
    if html:
        html_path = OUTPUT_DIR / f"dashboard_{today_str}.html"
        html_path.write_text(html, encoding="utf-8")
        log.info(f"HTML dashboard → {html_path}")
    else:
        log.warning("HTML generation skipped (template missing).")

    csv_path = OUTPUT_DIR / f"dashboard_{today_str}.csv"
    csv_path.write_text(generate_csv(data), encoding="utf-8")
    log.info(f"CSV export → {csv_path}")

    # Archive this run so tomorrow's build_history_context() has real memory of it.
    archive_run_to_history(data, today_str, dashboard_file=f"outputs/daily_newsroom_dashboard/dashboard_{today_str}.html")

    # ── Step 4: Send email ────────────────────────────────────────────────────
    log.info("Step 4/4 — Sending email...")
    if send_email_flag:
        html_out = OUTPUT_DIR / f"dashboard_{today_str}.html"
        csv_out  = OUTPUT_DIR / f"dashboard_{today_str}.csv"
        send_email(data, html_out, csv_out, today_str)

    log.info("✅ Daily pipeline run complete.")


# ── Scheduler ─────────────────────────────────────────────────────────────────

def start_scheduler(run_time: str) -> None:
    try:
        import schedule
        import time
    except ImportError:
        sys.exit("Missing dependency for scheduler: pip install schedule")

    log.info(f"Scheduler started — pipeline runs daily at {run_time}.")
    schedule.every().day.at(run_time).do(lambda: _run_locked(run_pipeline))

    log.info("Running once now for verification...")
    _run_locked(run_pipeline, send_email_flag=True)

    while True:
        schedule.run_pending()
        time.sleep(30)


# ── Entrypoint ────────────────────────────────────────────────────────────────

# Guards against a manually-triggered run (web UI) overlapping a scheduled
# GitHub Actions run and both writing to the same day's output files.
PIPELINE_LOCK_PATH = PROJECT_ROOT / "outputs" / ".pipeline.lock"
PIPELINE_LOCK_STALE_MINUTES = 30  # roughly matches the GH Actions timeout-minutes budget


def _acquire_pipeline_lock() -> None:
    if PIPELINE_LOCK_PATH.exists():
        try:
            age_minutes = (time.time() - PIPELINE_LOCK_PATH.stat().st_mtime) / 60
        except OSError:
            age_minutes = 0
        if age_minutes < PIPELINE_LOCK_STALE_MINUTES:
            log.error(
                f"Another pipeline run appears to be in progress "
                f"(lock file {PIPELINE_LOCK_PATH} is {age_minutes:.1f} min old, "
                f"staleness threshold is {PIPELINE_LOCK_STALE_MINUTES} min). "
                f"Exiting to avoid a concurrent run corrupting today's output files."
            )
            sys.exit(1)
        log.warning(
            f"Found stale pipeline lock ({age_minutes:.1f} min old) — "
            f"treating prior run as dead and proceeding."
        )
    PIPELINE_LOCK_PATH.parent.mkdir(parents=True, exist_ok=True)
    PIPELINE_LOCK_PATH.write_text(f"pid={os.getpid()} started={datetime.now().isoformat()}", encoding="utf-8")


def _release_pipeline_lock() -> None:
    try:
        PIPELINE_LOCK_PATH.unlink()
    except FileNotFoundError:
        pass
    except OSError as e:
        log.warning(f"Failed to remove pipeline lock file {PIPELINE_LOCK_PATH}: {e}")


def _run_locked(fn, *args, **kwargs):
    """Run a single pipeline execution under the lock, releasing it when that
    execution finishes. Used per-run rather than around --schedule's whole
    (potentially days-long) process lifetime, so the lock's staleness window
    reflects one run, not the scheduler daemon's uptime."""
    _acquire_pipeline_lock()
    try:
        return fn(*args, **kwargs)
    finally:
        _release_pipeline_lock()


def main() -> None:
    parser = argparse.ArgumentParser(description="Trending Content OS — daily runner")
    parser.add_argument("--schedule", action="store_true",
                        help="Keep process alive and run daily at --time")
    parser.add_argument("--time", default="07:00",
                        help="Daily run time in 24h format (default: 07:00)")
    parser.add_argument("--no-email", action="store_true",
                        help="Skip email delivery for this run")
    parser.add_argument("--prefetch-only", action="store_true",
                        help="Fetch SerpAPI Google News/Trends context and exit")
    args = parser.parse_args()

    if args.prefetch_only:
        _run_locked(run_prefetch_only)
    elif args.schedule:
        # start_scheduler manages the lock itself, once per triggered run,
        # since it stays alive indefinitely rather than exiting after one run.
        start_scheduler(args.time)
    else:
        _run_locked(run_pipeline, send_email_flag=not args.no_email)


if __name__ == "__main__":
    main()
