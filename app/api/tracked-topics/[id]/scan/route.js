import { NextResponse } from "next/server";
import { checkRunToken } from "@/lib/auth";
import { radarJob } from "@/lib/job-state";
import { spawnRadarScan } from "@/lib/spawn-radar-scan";
import { getTrackedTopic } from "@/lib/tracked-topics";

export const dynamic = "force-dynamic";

const REPO = process.env.GITHUB_REPOSITORY || "Meggers1982/trending-content";
const WORKFLOW_ID = "run-tracked-topics.yml";

// Same "Vercel dispatches GitHub Actions, local spawns Python directly" split
// app/api/run uses for the daily pipeline — unlike plain ad-hoc scans
// (/api/radar, which hard-501s on Vercel), tracked-topic re-scans need to
// work when the dashboard is deployed, so this route gets the remote path
// that /api/radar deliberately skips.
function shouldUseGithubActions() {
  return Boolean(process.env.VERCEL || process.env.GITHUB_PIPELINE_TOKEN);
}

async function triggerGithubWorkflow(topicId) {
  const token = process.env.GITHUB_PIPELINE_TOKEN;
  if (!token) {
    return { ok: false, status: 500, message: "GITHUB_PIPELINE_TOKEN is not configured in Vercel." };
  }

  const response = await fetch(
    `https://api.github.com/repos/${REPO}/actions/workflows/${WORKFLOW_ID}/dispatches`,
    {
      method: "POST",
      headers: {
        accept: "application/vnd.github+json",
        authorization: `Bearer ${token}`,
        "content-type": "application/json",
        "x-github-api-version": "2022-11-28"
      },
      body: JSON.stringify({
        ref: process.env.GITHUB_PIPELINE_REF || "main",
        inputs: { topic_id: topicId }
      })
    }
  );

  if (!response.ok) {
    const detail = await response.text();
    return { ok: false, status: response.status, message: `GitHub workflow dispatch failed: ${detail}` };
  }
  return { ok: true };
}

export async function POST(request, { params }) {
  const tokenError = checkRunToken(request);
  if (tokenError) return tokenError;

  const { id } = await params;
  const topic = await getTrackedTopic(id);
  if (!topic) {
    return NextResponse.json({ ok: false, message: "Tracked topic not found." }, { status: 404 });
  }

  if (shouldUseGithubActions()) {
    const trigger = await triggerGithubWorkflow(id);
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
