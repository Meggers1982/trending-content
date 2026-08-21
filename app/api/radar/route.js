import { NextResponse } from "next/server";
import { checkRunToken } from "@/lib/auth";
import { shouldUseGithubActions, triggerGithubWorkflow } from "@/lib/github-dispatch";
import { radarJob } from "@/lib/job-state";
import { listRecentRadarScans } from "@/lib/radar";
import { MAX_TOPIC_LENGTH, normalizeGeo, normalizeProfile, validateTopic } from "@/lib/radar-profiles";
import { spawnRadarScan } from "@/lib/spawn-radar-scan";

export const dynamic = "force-dynamic";

const WORKFLOW_ID = process.env.GITHUB_RADAR_WORKFLOW || "run-radar.yml";

export async function GET() {
  return NextResponse.json({ job: radarJob, recentScans: listRecentRadarScans() });
}

export async function POST(request) {
  const tokenError = checkRunToken(request);
  if (tokenError) return tokenError;

  const body = await request.json().catch(() => ({}));
  const topic = validateTopic(body.topic);
  if (!topic) {
    return NextResponse.json(
      { ok: false, message: `Enter a topic (1-${MAX_TOPIC_LENGTH} characters, not starting with "-").` },
      { status: 400 }
    );
  }
  const geo = normalizeGeo(body.geo);
  const profile = normalizeProfile(body.profile);

  // Deployed, there is no Python process or SerpAPI key here, so the scan runs
  // as a GitHub Actions workflow that commits its results back — the same split
  // /api/run and tracked-topic re-scans already use. This used to 501 instead,
  // which left the dashboard's Scan button dead in production.
  if (shouldUseGithubActions()) {
    const trigger = await triggerGithubWorkflow(WORKFLOW_ID, { topic, profile, geo });
    if (!trigger.ok) {
      return NextResponse.json(
        { ok: false, message: trigger.message },
        { status: trigger.status || 500 }
      );
    }
    return NextResponse.json({
      ok: true,
      dispatched: true,
      message:
        "Scan queued in GitHub Actions. Results appear here once the workflow commits them — usually a few minutes."
    });
  }

  // The local job slot only guards the local path; a dispatched run is queued
  // by the workflow's own concurrency group instead.
  if (radarJob.running) {
    return NextResponse.json(
      { ok: false, message: "A trend scan is already in progress.", job: radarJob },
      { status: 409 }
    );
  }

  const job = spawnRadarScan(topic, profile, geo);
  return NextResponse.json({ ok: true, dispatched: false, job });
}
