import { NextResponse } from "next/server";
import { checkRunToken } from "@/lib/auth";
import { shouldUseGithubActions, triggerGithubWorkflow } from "@/lib/github-dispatch";
import { radarJob } from "@/lib/job-state";
import { spawnRadarScan } from "@/lib/spawn-radar-scan";
import { getTrackedTopic } from "@/lib/tracked-topics";

export const dynamic = "force-dynamic";

const WORKFLOW_ID = "run-tracked-topics.yml";

export async function POST(request, { params }) {
  const tokenError = checkRunToken(request);
  if (tokenError) return tokenError;

  const { id } = await params;
  const topic = await getTrackedTopic(id);
  if (!topic) {
    return NextResponse.json({ ok: false, message: "Tracked topic not found." }, { status: 404 });
  }

  if (shouldUseGithubActions()) {
    const trigger = await triggerGithubWorkflow(WORKFLOW_ID, { topic_id: id });
    if (!trigger.ok) {
      return NextResponse.json({ ok: false, message: trigger.message }, { status: trigger.status || 500 });
    }
    return NextResponse.json({
      ok: true,
      dispatched: true,
      message: "Scan triggered via GitHub Actions — check back shortly for updated results."
    });
  }

  if (radarJob.running) {
    return NextResponse.json(
      { ok: false, message: "A trend scan is already in progress.", job: radarJob },
      { status: 409 }
    );
  }

  const job = spawnRadarScan(topic.topic, topic.profile, topic.geo);
  return NextResponse.json({ ok: true, dispatched: false, job });
}
