import { spawn } from "node:child_process";
import { NextResponse } from "next/server";
import { appendLog, finishJob, pipelineJob, resetJob } from "@/lib/job-state";

export const dynamic = "force-dynamic";

const ROOT = process.cwd();
const REPO = process.env.GITHUB_REPOSITORY || "Meggers1982/trending-content";
const WORKFLOW_ID = process.env.GITHUB_PIPELINE_WORKFLOW || "run-pipeline.yml";

function commandForMode(mode) {
  if (mode === "prefetch") return ["run_pipeline.py", "--prefetch-only"];
  return ["run_pipeline.py", "--no-email"];
}

function shouldUseGithubActions() {
  return Boolean(process.env.VERCEL || process.env.GITHUB_PIPELINE_TOKEN);
}

async function triggerGithubWorkflow(mode) {
  const token = process.env.GITHUB_PIPELINE_TOKEN;
  if (!token) {
    return {
      ok: false,
      status: 500,
      message: "GITHUB_PIPELINE_TOKEN is not configured in Vercel."
    };
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
        inputs: { mode }
      })
    }
  );

  if (!response.ok) {
    const detail = await response.text();
    return {
      ok: false,
      status: response.status,
      message: `GitHub workflow dispatch failed: ${detail}`
    };
  }

  return { ok: true };
}

export async function GET() {
  return NextResponse.json(pipelineJob);
}

export async function POST(request) {
  if (pipelineJob.running) {
    return NextResponse.json(
      { ok: false, message: "A pipeline run is already in progress.", job: pipelineJob },
      { status: 409 }
    );
  }

  const body = await request.json().catch(() => ({}));
  const mode = body.mode === "prefetch" ? "prefetch" : "full";
  resetJob(mode);

  if (shouldUseGithubActions()) {
    appendLog(`Triggering GitHub Actions workflow for ${mode} run...`);
    const trigger = await triggerGithubWorkflow(mode);
    if (!trigger.ok) {
      appendLog(trigger.message);
      finishJob(1, trigger.message);
      return NextResponse.json(
        { ok: false, message: trigger.message, job: pipelineJob },
        { status: trigger.status || 500 }
      );
    }
    appendLog("GitHub Actions workflow queued. Vercel will update after the workflow commits new artifacts.");
    finishJob(0);
    return NextResponse.json({ ok: true, job: pipelineJob });
  }

  const args = commandForMode(mode);
  appendLog(`Starting ${mode === "prefetch" ? "radar refresh" : "full report"}...`);

  const child = spawn("python", args, {
    cwd: ROOT,
    env: process.env,
    stdio: ["ignore", "pipe", "pipe"]
  });

  child.stdout.on("data", (chunk) => appendLog(chunk));
  child.stderr.on("data", (chunk) => appendLog(chunk));
  child.on("error", (error) => {
    appendLog(error.message);
    finishJob(1, error.message);
  });
  child.on("close", (code) => {
    appendLog(code === 0 ? "Run complete." : `Run exited with code ${code}.`);
    finishJob(code);
  });

  return NextResponse.json({ ok: true, job: pipelineJob });
}
