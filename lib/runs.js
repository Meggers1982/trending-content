import fs from "node:fs";
import path from "node:path";
import { resolveSafePath } from "@/lib/artifact-paths";

const ROOT = process.cwd();
const OUTPUT_DIR = path.join(ROOT, "outputs", "daily_newsroom_dashboard");

function exists(filePath) {
  try {
    return fs.existsSync(filePath);
  } catch {
    return false;
  }
}

function readText(filePath) {
  try {
    return fs.readFileSync(filePath, "utf8");
  } catch {
    return "";
  }
}

function parseCsv(text) {
  const rows = [];
  let row = [];
  let value = "";
  let quoted = false;

  for (let i = 0; i < text.length; i += 1) {
    const char = text[i];
    const next = text[i + 1];

    if (quoted) {
      if (char === '"' && next === '"') {
        value += '"';
        i += 1;
      } else if (char === '"') {
        quoted = false;
      } else {
        value += char;
      }
      continue;
    }

    if (char === '"') {
      quoted = true;
    } else if (char === ",") {
      row.push(value);
      value = "";
    } else if (char === "\n") {
      row.push(value);
      rows.push(row);
      row = [];
      value = "";
    } else if (char !== "\r") {
      value += char;
    }
  }

  if (value || row.length) {
    row.push(value);
    rows.push(row);
  }

  const [headers = [], ...records] = rows.filter((r) => r.some(Boolean));
  return records.map((record) =>
    Object.fromEntries(headers.map((header, index) => [header, record[index] || ""]))
  );
}

function getDateFromName(name, prefix, ext) {
  const match = name.match(new RegExp(`^${prefix}_(\\d{4}-\\d{2}-\\d{2})\\.${ext}$`));
  return match?.[1] || null;
}

export function listRuns() {
  if (!exists(OUTPUT_DIR)) return [];

  const files = fs.readdirSync(OUTPUT_DIR);
  const dates = new Set();
  for (const file of files) {
    const csvDate = getDateFromName(file, "dashboard", "csv");
    const htmlDate = getDateFromName(file, "dashboard", "html");
    const reportDate = getDateFromName(file, "daily_report", "md");
    const signalDate = getDateFromName(file, "serp_signals", "md");
    const date = csvDate || htmlDate || reportDate || signalDate;
    if (date && !file.includes(".blank.")) dates.add(date);
  }

  return [...dates]
    .sort()
    .reverse()
    .map((date) => {
      const csvPath = path.join(OUTPUT_DIR, `dashboard_${date}.csv`);
      const htmlPath = path.join(OUTPUT_DIR, `dashboard_${date}.html`);
      const reportPath = path.join(OUTPUT_DIR, `daily_report_${date}.md`);
      const signalPath = path.join(OUTPUT_DIR, `serp_signals_${date}.md`);
      const candidates = exists(csvPath) ? parseCsv(readText(csvPath)) : [];

      return {
        date,
        candidates,
        candidateCount: candidates.length,
        hasDashboard: exists(htmlPath),
        hasReport: exists(reportPath),
        hasSignals: exists(signalPath),
        dashboardPath: `dashboard_${date}.html`,
        reportPath: `daily_report_${date}.md`,
        signalPath: `serp_signals_${date}.md`
      };
    });
}

export function getLatestRun() {
  return listRuns()[0] || null;
}

export function getRunSummary(run) {
  if (!run) {
    return {
      signals: 0,
      retained: 0,
      immediate: 0,
      flags: 0,
      highConfidence: 0
    };
  }

  const retained = run.candidates.length;
  const immediate = run.candidates.filter((c) => c.priority_level === "P1").length;
  const flags = run.candidates.filter((c) =>
    `${c.notes || ""} ${c.confidence || ""}`.toLowerCase().includes("verify") ||
    `${c.notes || ""}`.toLowerCase().includes("flag")
  ).length;
  const highConfidence = run.candidates.filter((c) => c.confidence === "high").length;

  return {
    signals: retained ? Math.max(retained, 0) : 0,
    retained,
    immediate,
    flags,
    highConfidence
  };
}

export function getSignalExcerpt(run, maxLines = 24) {
  if (!run?.hasSignals) return "";
  const text = readText(path.join(OUTPUT_DIR, run.signalPath));
  return text.split("\n").slice(0, maxLines).join("\n");
}

export function getSignalText(run) {
  if (!run?.hasSignals) return "";
  return readText(path.join(OUTPUT_DIR, run.signalPath));
}

export function getReportExcerpt(run, maxLines = 40) {
  if (!run?.hasReport) return "";
  const text = readText(path.join(OUTPUT_DIR, run.reportPath));
  return text.split("\n").slice(0, maxLines).join("\n");
}

export function getReportText(run) {
  if (!run?.hasReport) return "";
  return readText(path.join(OUTPUT_DIR, run.reportPath));
}

export function resolveArtifact(fileName) {
  return resolveSafePath(OUTPUT_DIR, fileName);
}
