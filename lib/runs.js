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

// The parsed run data written by run_pipeline.py alongside the CSV. It carries
// what the CSV structurally can't: how many signals were reviewed vs. rejected,
// the rejected topics and their reasons, which tools were unavailable, and the
// run notes. Runs generated before this file existed return null and fall back
// to CSV-only rendering.
function readExtraction(date) {
  const filePath = path.join(OUTPUT_DIR, `extraction_${date}.json`);
  if (!exists(filePath)) return null;
  try {
    const parsed = JSON.parse(readText(filePath));
    return parsed && typeof parsed === "object" ? parsed : null;
  } catch {
    return null;
  }
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
      const extraction = readExtraction(date);
      // Prefer the CSV for candidates so a hand-edited CSV still wins, and fall
      // back to the extraction JSON when only that exists.
      const candidates = exists(csvPath)
        ? parseCsv(readText(csvPath))
        : extraction?.candidates || [];

      return {
        date,
        candidates,
        candidateCount: candidates.length,
        summary: extraction?.signal_summary || null,
        rejected: Array.isArray(extraction?.rejected) ? extraction.rejected : [],
        cost: extraction?.run_cost || null,
        factCheck: extraction?.fact_check_summary || null,
        hasExtraction: Boolean(extraction),
        hasDashboard: exists(htmlPath),
        hasReport: exists(reportPath),
        hasSignals: exists(signalPath),
        dashboardPath: `dashboard_${date}.html`,
        reportPath: `daily_report_${date}.md`,
        signalPath: `serp_signals_${date}.md`
      };
    });
}

// Mirrors _integrity_flag_count() in run_pipeline.py. Both are heuristics over
// free text until the extraction schema carries a real integrity_flags array.
function hasIntegrityFlag(candidate) {
  const notes = `${candidate.notes || ""}`.toLowerCase();
  return notes.includes("flag") || `${notes} ${candidate.confidence || ""}`.includes("verify");
}

export function getRunSummary(run) {
  if (!run) {
    return {
      reviewed: 0,
      retained: 0,
      rejected: 0,
      rejectedItemized: 0,
      immediate: 0,
      flags: 0,
      highConfidence: 0,
      toolsUnavailable: [],
      notes: ""
    };
  }

  const retained = run.candidates.length;
  const summary = run.summary || {};

  return {
    // total_reviewed is the whole point of the funnel — how much was looked at
    // to produce the handful that were kept.
    reviewed: Number(summary.total_reviewed) || 0,
    retained,
    // The model reports a total it filtered but only itemizes some of them, so
    // these two numbers legitimately differ and both are shown.
    rejected: Number(summary.total_rejected) || 0,
    rejectedItemized: run.rejected?.length || 0,
    immediate: run.candidates.filter((c) => c.priority_level === "P1").length,
    flags: run.candidates.filter(hasIntegrityFlag).length,
    highConfidence: run.candidates.filter((c) => c.confidence === "high").length,
    toolsUnavailable: Array.isArray(summary.tools_unavailable) ? summary.tools_unavailable : [],
    notes: `${summary.notes || ""}`.trim()
  };
}

// Whole days between a run's date and today, for the staleness warning. Run
// dates are plain YYYY-MM-DD with no timezone, so both sides are compared at
// UTC midnight to avoid an off-by-one when the viewer is behind UTC.
export function getRunAgeDays(run) {
  if (!run?.date) return null;
  const runTime = Date.parse(`${run.date}T00:00:00Z`);
  if (Number.isNaN(runTime)) return null;
  const now = new Date();
  const todayUtc = Date.UTC(now.getUTCFullYear(), now.getUTCMonth(), now.getUTCDate());
  return Math.max(0, Math.round((todayUtc - runTime) / 86400000));
}

// Rejection reasons are free text, so the same decision arrives 398 different
// ways across 28 runs: "off-category", "off_category", and "off-category —
// celebrity gossip; excluded per brand_safety_rules" are one reason. Cut at the
// first detail separator, then normalize separators.
const REASON_ALIASES = {
  "excluded-category": "off-category",
  "celebrity-health": "brand-safety",
  "political-celebrity-health": "brand-safety",
  "content-status": "existing",
  "duplicate": "existing",
};

// What each reason implicates, so the number points at the knob that changes it.
export const REASON_IMPLICATIONS = {
  "off-category": "GOOGLE_NEWS_QUERIES pulling the wrong material, or category_rules.yaml too narrow",
  "existing": "Overlap with recent coverage — dedup is working, but the queries repeat themselves",
  "weak-signal": "minimum_trend_strength_score / source tiers in scoring_weights.yaml",
  "stale": "freshness_window_hours, or queries surfacing archive material",
  "brand-safety": "brand_safety_rules — usually celebrity or political drift",
  "unverified-claim": "Skill 02b gate firing — sourcing quality upstream",
};

export function normalizeRejectionReason(reason) {
  const raw = `${reason || ""}`.trim().toLowerCase();
  if (!raw) return "unspecified";
  const [head] = raw.split(/[—–:/(,;]/);
  const key = head
    .trim()
    .replace(/[\s_]+/g, "-")
    .replace(/^-+|[-.]+$/g, "");
  if (!key) return "unspecified";
  const aliased = REASON_ALIASES[key] || key;
  if (REASON_IMPLICATIONS[aliased]) return aliased;
  // Fold qualified variants onto their family: "off-category-product-marketing"
  // is an off-category rejection with a note welded to it.
  const family = Object.keys(REASON_IMPLICATIONS).find((name) => aliased.startsWith(`${name}-`));
  return family || aliased;
}

// Reasons seen fewer than this many times across the whole history are noise —
// one-off phrasings the model invented once — and roll up rather than crowd out
// the families that matter.
const MIN_REASON_COUNT = 3;

// Aggregate rejections across runs so the reject log becomes config feedback
// rather than exhaust. `window` runs are compared against the `window` before
// them to show which reasons are growing.
export function getRejectionTrends(runs, window = 7) {
  const withRejections = runs.filter((run) => run.rejected?.length);
  if (!withRejections.length) return null;

  const tally = (subset) => {
    const counts = {};
    for (const run of subset) {
      for (const item of run.rejected) {
        const reason = normalizeRejectionReason(item.reason);
        counts[reason] = (counts[reason] || 0) + 1;
      }
    }
    return counts;
  };

  const recentRuns = withRejections.slice(0, window);
  const priorRuns = withRejections.slice(window, window * 2);
  const all = tally(withRejections);
  const recent = tally(recentRuns);
  const prior = tally(priorRuns);
  const total = Object.values(all).reduce((sum, n) => sum + n, 0);

  const rare = Object.entries(all).filter(([, count]) => count < MIN_REASON_COUNT);
  const rareTotal = rare.reduce((sum, [, count]) => sum + count, 0);
  for (const [reason] of rare) delete all[reason];

  const reasons = Object.entries(all)
    .map(([reason, count]) => ({
      reason,
      count,
      share: total ? Math.round((count / total) * 100) : 0,
      recent: recent[reason] || 0,
      prior: prior[reason] || 0,
      // Per-run averages, so an uneven number of runs on each side is fair.
      delta:
        (recentRuns.length ? (recent[reason] || 0) / recentRuns.length : 0) -
        (priorRuns.length ? (prior[reason] || 0) / priorRuns.length : 0),
      implication: REASON_IMPLICATIONS[reason] || "",
    }))
    .sort((a, b) => b.count - a.count);

  if (rareTotal) {
    reasons.push({
      reason: `${rare.length} one-off reasons`,
      count: rareTotal,
      share: total ? Math.round((rareTotal / total) * 100) : 0,
      recent: 0,
      prior: 0,
      delta: 0,
      implication: "",
      isRollup: true,
    });
  }

  return {
    total,
    runs: withRejections.length,
    recentRuns: recentRuns.length,
    priorRuns: priorRuns.length,
    reasons,
  };
}

const STOPWORDS = new Set([
  "the", "a", "an", "and", "or", "of", "for", "to", "in", "on", "with", "new",
  "study", "says", "after", "amid", "as", "at", "by", "from", "is", "are", "its"
]);

function topicTokens(topic) {
  return new Set(
    `${topic || ""}`
      .toLowerCase()
      .replace(/[^a-z0-9\s]/g, " ")
      .split(/\s+/)
      .filter((word) => word.length > 2 && !STOPWORDS.has(word))
  );
}

// Two topics are "the same story" when most of the distinctive words in the
// shorter one also appear in the longer one. Deliberately looser than exact
// matching (the model rewords headlines between runs) and looser than
// filter_recent_duplicates() in run_pipeline.py, which is a suppression
// decision — this one only drives a informational badge, so a false positive
// costs a mislabeled chip rather than a dropped story.
function sameStory(a, b) {
  const left = topicTokens(a);
  const right = topicTokens(b);
  if (!left.size || !right.size) return false;
  let shared = 0;
  for (const word of left) if (right.has(word)) shared += 1;
  return shared / Math.min(left.size, right.size) >= 0.6;
}

// For each topic in `run`, how many consecutive runs (ending at this one) have
// carried the same story. 1 means it is new today. CLAUDE.md's Daily Run step 2
// asks for exactly this staleness check; nothing surfaced it before.
export function getRecurrence(runs, run) {
  const recurrence = {};
  if (!run) return recurrence;

  const index = runs.findIndex((r) => r.date === run.date);
  const earlier = index >= 0 ? runs.slice(index + 1) : [];

  for (const candidate of run.candidates) {
    let streak = 1;
    for (const previous of earlier) {
      if (previous.candidates.some((c) => sameStory(c.topic, candidate.topic))) {
        streak += 1;
      } else {
        break;
      }
    }
    recurrence[candidate.topic] = streak;
  }
  return recurrence;
}

// Oldest-first funnel counts for the trend strip.
export function getRunTrend(runs, limit = 14) {
  return runs
    .slice(0, limit)
    .filter((run) => run.summary)
    .map((run) => ({
      date: run.date,
      reviewed: Number(run.summary.total_reviewed) || 0,
      retained: run.candidates.length
    }))
    .reverse();
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
