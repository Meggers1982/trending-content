# SerpAPI Google News recovery check

Playbook for the scheduled cloud routine "SerpAPI Google News recovery check"
(created 2026-09-05). It exists so the routine's prompt can stay short — the
routine is told to read this file and follow it.

## Context

SerpAPI's `google_news` engine went into a partial outage on **2026-09-05**:
success rate ~100% → ~40–50%, latency ~3s → ~40–45s against their 90s
server-side cap. Confirmed on SerpAPI's own public metrics at
`serpapi.com/google-news-api/api-metrics`, so it is their incident, not ours.

It is **not** an account or quota problem — 90 of 15,000 searches used this
month on a Production Plan. `google_trends` (0.9–10s) and the plain `google`
engine (0.4–29s) answer normally on the same key in the same minute.

Both pipelines already carry a working per-engine circuit breaker and finish
green on the degraded upstream. The cost is lost Google News signal, not failed
jobs. **Do not modify or re-fix the circuit breaker.**

## Step 1 — Diagnose from committed artifacts

No API key or dashboard access is needed. The pipeline runs at 12:00 UTC daily
and commits its own evidence to this repo. `git pull` first, then:

- `outputs/daily_newsroom_dashboard/serp_signals_<today>.md` — a
  `SIGNAL INTEGRITY WARNING` block naming `google_news` means **still degraded**.
- Last entry of `data/run_history.yaml` — `tools_unavailable` containing
  `serpapi_news_search` means **still degraded**; an empty list means
  **recovered**.
- `daily_report_<today>.md` — compare the Google News article count against the
  previous few days via `git log`. A healthy run answers all 12 radar queries.

Check the two most recent days, not just today, so one anomalous run doesn't
decide it. If today's artifacts are missing, the 12:00 UTC run hasn't happened
yet — report that and stop.

## Step 2 — If recovered

Change no code. Report that it recovered, citing the article count and the
absent integrity warning. Note that `docs/serpapi-recovery-check.md` and this
routine can now be retired.

## Step 3 — If still degraded

Implement the `google_news_light` fallback **on a branch** and open a PR. Never
push to `main` — the daily pipeline costs real money per run and this must be
reviewed first.

The shape of the fix, in `run_pipeline.py`:

- `fetch_google_news()` currently calls `_serp_get({"engine": "google_news", ...})`
  per query in `GOOGLE_NEWS_QUERIES`.
- When the breaker for `google_news` is open (`_serp_circuit_open("google_news")`),
  retry the *remaining* queries against `engine: "google_news_light"` instead.
  It is a separate engine with its own breaker tally, unaffected by this
  incident, returning fewer fields per article.
- Verify the response shape first — `google_news_light` may not return the same
  `news_results` keys (`title`, `source.name`, `date`, `snippet`, `link`). Map
  whatever it does return onto the dict `fetch_google_news()` already builds, and
  leave missing fields as empty strings rather than inventing them.
- Label the fallback articles so the report can tell them apart, and mention the
  fallback in the `SIGNAL INTEGRITY WARNING` text rather than presenting light
  results as full ones.
- Gate it behind `SERPAPI_NEWS_FALLBACK_ENABLED` (default on) so it can be turned
  off without a revert once the incident ends.

Do not raise `SERPAPI_TIMEOUT_SECONDS` past their 90s cap — it makes every
genuine failure cost 90s. It was considered and rejected.

## Step 4 — Report

Either way, write a short report: what the artifacts showed, what you concluded,
and the PR link if you opened one. Say plainly if the evidence was ambiguous
rather than guessing.

Linear context: MEA-120 (this incident, closed), MEA-55 / MEA-57 (the circuit
breaker work that makes it survivable).
