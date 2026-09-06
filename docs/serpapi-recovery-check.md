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

You may start in a detached HEAD. Run `git checkout main && git pull origin main`
before anything else.

Check the two most recent days, not just today, so one anomalous run doesn't
decide it.

**What counts as usable evidence.** Judge the artifacts by age, not by which run
produced them. A manual `workflow_dispatch` run is exactly as good a witness to
the engine's state as the 12:00 UTC cron — do not discount artifacts for having
been committed at an unexpected hour. Proceed whenever the newest
`serp_signals_*.md` is **less than 24 hours old** (check the commit time with
`git log -1 --format=%ad --date=iso -- <file>`, not the filename date).

Stop and report only if the newest artifacts are older than that, which means no
run has completed recently and you have nothing current to judge from.

If a run *did* fire and produced no artifacts at all for a given date, that
absence is itself evidence — the outage killed it before it could commit. That is
what happened on 2026-09-05.

## Step 2 — If recovered

Change no code. Report that it recovered, citing the article count and the
absent integrity warning.

Then say plainly that this routine has done its job and should be retired, and
that the merged fallback can be switched off with
`SERPAPI_NEWS_FALLBACK_ENABLED=false` — or left on, since it only ever engages
when the `google_news` breaker opens, which a healthy engine never does.

## Step 3 — If still degraded

**The `google_news_light` fallback is already merged** (PR #1, `4b3f268`,
2026-09-06). There is nothing left to build. Check first and confirm:

```
grep -q google_news_light run_pipeline.py && echo "fallback already present"
```

If it is present — which it should be — then **write no code and open no PR**.
Report that the engine is still degraded, that the fallback is carrying the
load, and how well it is doing: the latest `run_history.yaml` entry and the
Google News article count tell you whether the pipeline is getting usable signal
through the fallback. That report is the whole job on a still-degraded day.

Only if the fallback has somehow been reverted out of `main` should you rebuild
it, on branch `fix/serpapi-google-news-light-fallback`, and never open a second
PR if that branch or an open PR already exists.

Otherwise, implement the `google_news_light` fallback **on a branch** and open a
PR. Never push to `main` — the daily pipeline costs real money per run and this
must be reviewed first.

If the push or PR creation is rejected with a 403 (`Resource not accessible by
integration`), the Claude GitHub App lacks write access to this repo. Do not
retry it repeatedly or look for a way around it: report the diagnosis, say the
push was blocked, and stop. Only the repo owner can grant that, at
`https://github.com/apps/claude/installations/select_target`.

The shape of the fix, in `run_pipeline.py`:

- `fetch_google_news()` currently calls `_serp_get({"engine": "google_news", ...})`
  per query in `GOOGLE_NEWS_QUERIES`.
- When the breaker for `google_news` is open (`_serp_circuit_open("google_news")`),
  retry the *remaining* queries against `engine: "google_news_light"` instead.
  It is a separate engine with its own breaker tally, unaffected by this
  incident, returning fewer fields per article.
- The engine's contract is already known, verified live on 2026-09-06:
  `news_results` items carry `date`, `link`, `position`, `snippet`, `source`,
  `thumbnail`, `title`. `source` is a **bare string** ("NPR"), not
  `{"name": ...}` as on `google_news`.
- It does **not** accept `num`, and it does **not** accept `when:7d` — that
  operator returns "Fully empty", because this engine is a `tbm=nws` Google
  search rather than Google News proper. Strip both from fallback queries.

**You cannot call SerpAPI from this sandbox** — egress to `serpapi.com` is
blocked. Do not spend turns trying; the contract above is what you need. If you
ever need something about the engine that is not written here, say so in your
report and ask for it to be checked by hand rather than guessing and shipping.
That exact guess is what nearly shipped a fallback that returned zero articles
on every query while logging that it worked.
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
