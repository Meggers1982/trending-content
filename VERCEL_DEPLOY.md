# Trending Content OS on Vercel

This project now includes a Vercel-ready Next.js interface.

## What Vercel Runs

The web app reads generated pipeline artifacts from:

```text
outputs/daily_newsroom_dashboard/
```

It displays:

- latest run date
- retained topic board
- radar snapshot
- report excerpt
- links to generated dashboard, report, and signal cache
- local pipeline commands

## Running the Pipeline From Vercel

The Vercel app should not run the long Python pipeline directly inside a web request.
Instead, the **Start New Report** button triggers a GitHub Actions workflow:

1. Vercel calls GitHub's workflow dispatch API
2. GitHub Actions runs `python run_pipeline.py` (email is off by default — pass `--email` to opt in for a specific run)
3. Generated artifacts are committed back to the repo
4. Vercel redeploys from the new commit

The **Refresh Radar Only** button triggers the same workflow with `--prefetch-only`.

## Ad-hoc Trend Scanner on Vercel

The "Trend scanner" panel (`POST /api/radar`) spawns `google_trend_radar.py` directly when run
locally. Deployed, there is no Python process or SerpAPI key, so it dispatches
`.github/workflows/run-radar.yml` instead — the same pattern `/api/run` and tracked-topic re-scans
use. The workflow scans the requested topic, commits the results to `outputs/google_trend_radar`,
and the resulting push triggers a fresh deploy, so the scan shows up in the dashboard a few minutes
later. This needs `GITHUB_PIPELINE_TOKEN` set in Vercel (the same token `/api/run` uses) and
`SERPAPI_API_KEY` as a repo secret.

Because the dispatched run has no local job to poll, the panel reports "queued" rather than
streaming logs — results appear in "Recent scans" once the workflow commits them.

## Deploy

From the project root:

```bash
npm install
npm run build
vercel
```

Or connect this folder to a GitHub repo and import it in Vercel.

## Environment Variables

Do not upload `.env`.

Add these in Vercel project settings:

- `GITHUB_PIPELINE_TOKEN`
- `GITHUB_REPOSITORY=Meggers1982/trending-content`
- `GITHUB_PIPELINE_WORKFLOW=run-pipeline.yml`
- `GITHUB_PIPELINE_REF=main`
- `DATABASE_URL` — auto-provisioned by the Neon Marketplace integration (project `neon-coffee-nest`,
  dedicated to this app). Backs `lib/tracked-topics.js`; no manual setup needed unless reconnecting.
- `RUN_CONTROL_TOKEN` (optional, but recommended) — a shared secret you choose. When set, `POST /api/run`
  requires a matching `x-run-token` header, so only someone who knows the token can trigger a run.
  Without it, the run-trigger endpoint is publicly triggerable by anyone who has the deployed URL,
  which can rack up Anthropic API, SerpAPI, and GitHub Actions costs. Enter the same value in the
  dashboard's "Run token" field to use it from the browser.

Add these as GitHub Actions repository secrets:

- `ANTHROPIC_API_KEY`
- `SERPAPI_API_KEY`
- `DATABASE_URL` — same Neon connection string as the Vercel env var above. `run_tracked_topics.py`
  (`.github/workflows/run-tracked-topics.yml`) reads/writes the `tracked_topics` table directly.
- `EMAIL_SENDER` only if email delivery is needed
- `EMAIL_PASSWORD` only if email delivery is needed
- `EMAIL_RECIPIENT` only if email delivery is needed

Add these as GitHub Actions repository variables:

- `SERPAPI_TRENDING_NOW_ENABLED=true`
- `SERPAPI_TRENDING_NOW_HOURS=24`
- `SERPAPI_TRENDING_NOW_CATEGORY_ID=7`
- `SERPAPI_TIMEOUT_SECONDS=45`
- `SERPAPI_MAX_RETRIES=3`
- `EMAIL_SMTP_HOST=smtp.gmail.com`
- `EMAIL_SMTP_PORT=587`

`GITHUB_PIPELINE_TOKEN` should be a fine-grained GitHub token with permission to dispatch workflows for this repository. Store it in Vercel only, not in GitHub.

## Recommended v2

Move generated artifacts into durable storage:

- Vercel Blob, Supabase, or S3 for generated dashboards
- ~~database table for run metadata and job status~~ — done for tracked topics (Neon, 2026-09-02);
  run metadata/job status still lives in `outputs/daily_newsroom_dashboard/*.json` + git
- Vercel Cron for automatic scheduled runs
