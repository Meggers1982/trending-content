# Trending Content OS

Trending Content OS is a health and wellness editorial radar that combines Google News, Google Trends, safety routing, and content opportunity scoring into a dashboard/report interface.

## Local Setup

```bash
cd /Users/meaganmorris/trending-content-os
npm install
cp .env.example .env
npm run dev
```

Open:

```text
http://localhost:3000
```

## Pipeline Commands

```bash
npm run prefetch
npm run pipeline
```

The web app includes controls for starting a new report and refreshing the radar.
Locally, those controls run Python directly. In Vercel, they trigger the GitHub Actions workflow in `.github/workflows/run-pipeline.yml`.

If `RUN_CONTROL_TOKEN` is set in the environment, the run-trigger endpoint (`POST /api/run`) requires that
token in the dashboard's "Run token" field. See `VERCEL_DEPLOY.md` for why this matters once deployed.

## Reading a run

The dashboard leads with the funnel — how many signals were reviewed, how many survived, how many
were cut — because the ratio (typically ~144 reviewed to ~9 retained) is the point of the system.
Under it:

- **Trend strip** — reviewed vs. retained for the last 14 runs.
- **Run Insight** — the model's own notes about the run.
- **Priority Board** — click any topic to expand its angle, working headline, why-now, and next
  steps, with a "Copy brief" button. Filter by priority or search across angles and headlines. A
  "day N" chip marks a story that has carried across consecutive runs.
- **Rejected topics** — collapsed by default, grouped by rejection reason.
- **Why topics get cut** — the same rejections aggregated across every run, with each reason's
  share, whether it is rising or falling, and which config it implicates. Currently ~53% of all
  rejections are off-category, which points at `GOOGLE_NEWS_QUERIES` rather than at the filter.
- **Generated runs** — click any past date to load that whole run into the page
  (`/?run=YYYY-MM-DD`); the standalone HTML file is still there as a downloadable snapshot.

Expanded rows also carry the source links, any ⚠️ integrity notes, and a one-line reason behind each
score (hover the score to see it). The run header shows what the run cost to produce.

Each run's numbers come from `outputs/daily_newsroom_dashboard/extraction_<date>.json`, the parsed
run data. `raw_extraction_<date>.txt` beside it is the raw model text kept for debugging — it is
fence-wrapped and was never valid JSON despite previously carrying a `.json` extension.

Headlines in the dashboard's "Google News Radar" panel link out to the original article, using
the `Link:` line the pipeline writes under each headline in
`outputs/daily_newsroom_dashboard/serp_signals_*.md`. Signal files generated before that line
existed have no URLs, so their headlines stay plain text until the next run.

## Ad-hoc Trend Scanner

The dashboard's "Trend scanner" panel (`#scan`) runs `google_trend_radar.py` on demand for any
topic — not just health/wellness, and with no Anthropic API cost (pure SerpAPI + code-side trend
scoring). It's a separate tool from the daily automated pipeline above; see the "Known limitation"
/ Engineering Notes sections in `CLAUDE.md` for how it differs from `run_pipeline.py`.

The `beauty` profile additionally cross-checks Reddit (free, no API key) as a second signal
source, tags candidates with ingredient/benefit/concern labels from `configs/beauty_taxonomy.yaml`,
and computes an `opportunity_score` estimating whitespace (high trend interest, low existing
coverage) alongside the base `radar_score` — see `CLAUDE.md`'s Engineering Notes for details.

There are also focused, single-topic profiles for each of the categories the daily pipeline
tracks depth for: `nutrition`, `fitness`, `food-safety`, `diet`, `weight-loss`,
`mental-health`, `gut-health` (plus the existing `wellness`/`health`/`ai`/`beauty`) — pick one
from the Trend Scanner's profile dropdown, or `--profile nutrition` on the CLI, to scan just
that category instead of the broad `wellness`/`health` blend.

The most recent scan's plain keyword list (topic, stage, radar/opportunity scores, tags) also
shows up inline on the main dashboard under "Trending keywords" (`#keywords`), so you don't have
to open a separate HTML file to see what's trending.

A separate scheduled job, `.github/workflows/run-beauty-radar.yml`, runs the beauty profile
automatically once a week (Monday mornings) and commits the results, so "Trending keywords"
stays current without anyone clicking "Scan" — edit the cron line in that file to change how
often it runs.

Each of the other 7 profiles has its own weekly scheduled workflow too
(`run-nutrition-radar.yml`, `run-fitness-radar.yml`, `run-food-safety-radar.yml`,
`run-diet-radar.yml`, `run-weight-loss-radar.yml`, `run-mental-health-radar.yml`,
`run-gut-health-radar.yml`), staggered across Monday-Wednesday mornings so they don't all run
(and push) at the same time. All of them show up individually in the GitHub Actions tab and
can be triggered manually from there ("Run workflow") in addition to their schedule.

Locally the Scan button runs Python directly. Deployed, it dispatches
`.github/workflows/run-radar.yml` — a generic, on-demand counterpart to the per-profile workflows
that accepts any topic/profile/geo — which commits its results back and triggers a fresh deploy.
Either way you need a `SERPAPI_API_KEY`: locally in `.env`, deployed as a repo secret.

## Vercel

This repo is Vercel-ready as a Next.js app. In v1, the web interface reads generated artifacts from:

```text
outputs/daily_newsroom_dashboard/
```

The production button triggers GitHub Actions, which runs the Python pipeline and commits generated artifacts back to the repository.

See `VERCEL_DEPLOY.md` for deployment notes.
