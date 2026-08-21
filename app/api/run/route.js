import { spawn } from "node:child_process";
import { NextResponse } from "next/server";
import { checkRunToken } from "@/lib/auth";
import { explainRunError } from "@/lib/error-messages";
import { shouldUseGithubActions, triggerGithubWorkflow } from "@/lib/github-dispatch";
import { appendLog, finishJob, pipelineJob, resetJob } from "@/lib/job-state";

export const dynamic = "force-dynamic";

const ROOT = process.cwd();
const WORKFLOW_ID = process.env.GITHUB_PIPELINE_WORKFLOW || "run-pipeline.yml";
const PYTHON_BIN = process.env.PYTHON_BIN || "python3";

function commandForMode(mode) {
  if (mode === "prefetch") return ["run_pipeline.py", "--prefetch-only"];
  return ["run_pipeline.py"];
}

export async function GET() {
  return NextResponse.json(pipelineJob);
}

export async function POST(request) {
  const tokenError = checkRunToken(request);
  if (tokenError) return tokenError;

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
    const trigger = await triggerGithubWorkflow(WORKFLOW_ID, { mode });
    if (!trigger.ok) {
      appendLog(trigger.message);
      const friendly = explainRunError(trigger.message, mode);
      finishJob(1, trigger.message, friendly);
      return NextResponse.json(
        { ok: false, message: friendly, job: pipelineJob },
        { status: trigger.status || 500 }
      );
    }
    appendLog("GitHub Actions workflow queued. Vercel will update after the workflow commits new artifacts.");
    finishJob(0);
    return NextResponse.json({ ok: true, job: pipelineJob });
  }

  const args = commandForMode(mode);
  appendLog(`Starting ${mode === "prefetch" ? "radar refresh" : "full report"}...`);

  const child = spawn(PYTHON_BIN, args, {
    cwd: ROOT,
    env: process.env,
    stdio: ["ignore", "pipe", "pipe"]
  });

  child.stdout.on("data", (chunk) => appendLog(chunk));
  child.stderr.on("data", (chunk) => appendLog(chunk));
  child.on("error", (error) => {
    appendLog(error.message);
    finishJob(1, error.message, explainRunError(error.message, mode));
  });
  child.on("close", (code) => {
    appendLog(code === 0 ? "Run complete." : `Run exited with code ${code}.`);
    finishJob(code, code === 0 ? null : `Run exited with code ${code}.`, code === 0 ? null : explainRunError(`Run exited with code ${code}.`, mode));
  });

  return NextResponse.json({ ok: true, job: pipelineJob });
}
