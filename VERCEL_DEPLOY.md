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

## Important v1 Constraint

The existing Python pipeline is a long-running local job that writes dashboard files.
Vercel is hosting the interface in v1; it is not yet the job runner.

For now, run the pipeline locally:

```bash
npm run prefetch
npm run pipeline
```

Then deploy the updated artifacts to Vercel.

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

If/when the pipeline runner moves into Vercel, add these in the Vercel dashboard instead:

- `ANTHROPIC_API_KEY`
- `SERPAPI_API_KEY`
- email variables only if cloud email delivery is needed

## Recommended v2

Move pipeline execution into a job layer:

- Vercel app for interface
- Vercel Cron or GitHub Actions to trigger daily runs
- durable storage for generated artifacts, such as Vercel Blob, Supabase, S3, or GitHub commits
- optional API route to trigger a run manually
