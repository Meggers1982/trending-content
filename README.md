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

The web app also includes local controls for starting a new report and refreshing the radar.

## Vercel

This repo is Vercel-ready as a Next.js app. In v1, the web interface reads generated artifacts from:

```text
outputs/daily_newsroom_dashboard/
```

The Python pipeline is still a local/background job. For production, move generated artifacts into durable storage such as Vercel Blob, Supabase, S3, or committed run artifacts.

See `VERCEL_DEPLOY.md` for deployment notes.
