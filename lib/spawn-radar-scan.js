import { spawn } from "node:child_process";
import { explainRunError } from "@/lib/error-messages";
import { appendRadarLog, finishRadarJob, radarJob, resetRadarJob } from "@/lib/job-state";

const ROOT = process.cwd();
const PYTHON_BIN = process.env.PYTHON_BIN || "python3";

// google_trend_radar.py prints this line on success; capturing the path lets
// the UI link straight to the result instead of the user hunting for it.
const RESULT_LINE_PATTERN = /^Dashboard:\s+.*[\\/](trend_radar_[\w.-]+\.html)\s*$/;

function extractResultFile(logs) {
  for (let i = logs.length - 1; i >= 0; i -= 1) {
    const match = logs[i].match(RESULT_LINE_PATTERN);
    if (match) return match[1];
  }
  return null;
}

// Spawns google_trend_radar.py against the shared radarJob slot. Used by both
// the ad-hoc scan form (/api/radar) and a tracked topic's local "Scan now"
// (/api/tracked-topics/[id]/scan) so there's one execution path, not two.
export function spawnRadarScan(topic, profile, geo, extraArgs = []) {
  resetRadarJob(topic);
  appendRadarLog(`Scanning "${topic}" (geo=${geo}, profile=${profile})...`);

  const child = spawn(
    PYTHON_BIN,
    ["google_trend_radar.py", "--topic", topic, "--geo", geo, "--profile", profile, "--skip-timeseries", ...extraArgs],
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

  return radarJob;
}
