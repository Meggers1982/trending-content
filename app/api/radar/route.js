import { spawn } from "node:child_process";
import { NextResponse } from "next/server";
import { explainRunError } from "@/lib/error-messages";
import { appendRadarLog, finishRadarJob, radarJob, resetRadarJob } from "@/lib/job-state";
import { listRecentRadarScans } from "@/lib/radar";

export const dynamic = "force-dynamic";

const ROOT = process.cwd();
const PYTHON_BIN = process.env.PYTHON_BIN || "python3";
const MAX_TOPIC_LENGTH = 100;
const ALLOWED_PROFILES = new Set(["auto", "wellness", "health", "ai", "none"]);

// google_trend_radar.py prints this line on success; capturing the path lets
// the UI link straight to the result instead of the user hunting for it.
const RESULT_LINE_PATTERN = /^Dashboard:\s+.*[\\/](trend_radar_[\w.-]+\.html)\s*$/;

function validateTopic(topic) {
  if (typeof topic !== "string") return null;
  const trimmed = topic.trim();
  if (!trimmed || trimmed.length > MAX_TOPIC_LENGTH) return null;
  if (trimmed.startsWith("-")) return null; // would otherwise be parsed as a CLI flag
  return trimmed;
}

function extractResultFile(logs) {
  for (let i = logs.length - 1; i >= 0; i -= 1) {
    const match = logs[i].match(RESULT_LINE_PATTERN);
    if (match) return match[1];
  }
  return null;
}

export async function GET() {
  return NextResponse.json({ job: radarJob, recentScans: listRecentRadarScans() });
}

export async function POST(request) {
  const runControlToken = process.env.RUN_CONTROL_TOKEN;
  if (runControlToken) {
    const providedToken = request.headers.get("x-run-token");
    if (providedToken !== runControlToken) {
      return NextResponse.json(
        { ok: false, message: "Invalid or missing run token." },
        { status: 401 }
      );
    }
  }

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
  const geo = typeof body.geo === "string" && body.geo.trim() ? body.geo.trim().slice(0, 5) : "US";
  const profile = ALLOWED_PROFILES.has(body.profile) ? body.profile : "auto";

  resetRadarJob(topic);
  appendRadarLog(`Scanning "${topic}" (geo=${geo}, profile=${profile})...`);

  const child = spawn(
    PYTHON_BIN,
    ["google_trend_radar.py", "--topic", topic, "--geo", geo, "--profile", profile, "--skip-timeseries"],
    { cwd: ROOT, env: process.env, stdio: ["ignore", "pipe", "pipe"] }
  );

  child.stdout.on("data", (chunk) => appendRadarLog(chunk));
  child.stderr.on("data", (chunk) => appendRadarLog(chunk));
  child.on("error", (error) => {
    appendRadarLog(error.message);
    finishRadarJob(1, error.message, explainRunError(error.message, "scan"));
  });
  child.on("close", (code) => {
    appendRadarLog(code === 0 ? "Scan complete." : `Scan exited with code ${code}.`);
    const resultFile = code === 0 ? extractResultFile(radarJob.logs) : null;
    finishRadarJob(
      code,
      code === 0 ? null : `Scan exited with code ${code}.`,
      code === 0 ? null : explainRunError(`Scan exited with code ${code}.`, "scan"),
      { resultFile }
    );
  });

  return NextResponse.json({ ok: true, job: radarJob });
}
