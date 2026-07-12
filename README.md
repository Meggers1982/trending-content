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

## Ad-hoc Trend Scanner

The dashboard's "Trend scanner" panel (`#scan`) runs `google_trend_radar.py` on demand for any
topic — not just health/wellness, and with no Anthropic API cost (pure SerpAPI + code-side trend
scoring). It's a separate tool from the daily automated pipeline above; see the "Known limitation"
/ Engineering Notes sections in `CLAUDE.md` for how it differs from `run_pipeline.py`.

This only works where the request is actually handled — i.e. locally or on a self-hosted server
with a `SERPAPI_API_KEY` set. It's not available when the app is deployed to Vercel (`POST /api/radar`
returns a 501 there), since there's no GitHub Actions equivalent wired up for ad-hoc scans.

## Vercel

This repo is Vercel-ready as a Next.js app. In v1, the web interface reads generated artifacts from:

```text
outputs/daily_newsroom_dashboard/
```

The production button triggers GitHub Actions, which runs the Python pipeline and commits generated artifacts back to the repository.

See `VERCEL_DEPLOY.md` for deployment notes.
