import { spawn } from "node:child_process";
import path from "node:path";
import { NextResponse } from "next/server";
import { appendLog, finishJob, pipelineJob, resetJob } from "@/lib/job-state";

export const dynamic = "force-dynamic";

const ROOT = process.cwd();

function commandForMode(mode) {
  if (mode === "prefetch") return ["run_pipeline.py", "--prefetch-only"];
  return ["run_pipeline.py", "--no-email"];
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
