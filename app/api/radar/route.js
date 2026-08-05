import { NextResponse } from "next/server";
import { checkRunToken } from "@/lib/auth";
import { radarJob } from "@/lib/job-state";
import { listRecentRadarScans } from "@/lib/radar";
import { MAX_TOPIC_LENGTH, normalizeGeo, normalizeProfile, validateTopic } from "@/lib/radar-profiles";
import { spawnRadarScan } from "@/lib/spawn-radar-scan";

export const dynamic = "force-dynamic";

export async function GET() {
  return NextResponse.json({ job: radarJob, recentScans: listRecentRadarScans() });
}

export async function POST(request) {
  const tokenError = checkRunToken(request);
  if (tokenError) return tokenError;

  if (radarJob.running) {
    return NextResponse.json(
      { ok: false, message: "A trend scan is already in progress.", job: radarJob },
      { status: 409 }
    );
  }

  // Ad-hoc scans spawn Python directly; unlike /api/run there's no GitHub
  // Actions equivalent wired up, so this only works where the process (and
  // its SerpAPI key) actually runs — not the Vercel + Actions split used
  // for the daily pipeline.
  if (process.env.VERCEL) {
    return NextResponse.json(
      {
        ok: false,
        message: "Ad-hoc trend scans need a live SerpAPI key and Python process, so they only run locally/self-hosted — not on Vercel."
      },
      { status: 501 }
    );
  }

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

  const job = spawnRadarScan(topic, profile, geo);
  return NextResponse.json({ ok: true, job });
}
