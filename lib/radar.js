import fs from "node:fs";
import path from "node:path";
import { resolveSafePath } from "@/lib/artifact-paths";

const ROOT = process.cwd();
const RADAR_OUTPUT_DIR = path.join(ROOT, "outputs", "google_trend_radar");

function exists(filePath) {
  try {
    return fs.existsSync(filePath);
  } catch {
    return false;
  }
}

export function resolveRadarArtifact(fileName) {
  return resolveSafePath(RADAR_OUTPUT_DIR, fileName);
}

// google_trend_radar.py names output trend_radar_{topic-slug}_{YYYY-MM-DD_HHMM}.{ext}
export function listRecentRadarScans(limit = 6) {
  if (!exists(RADAR_OUTPUT_DIR)) return [];

  const htmlFiles = fs.readdirSync(RADAR_OUTPUT_DIR).filter((f) => f.endsWith(".html"));
  const withStats = htmlFiles.map((file) => {
    let mtimeMs = 0;
    try {
      mtimeMs = fs.statSync(path.join(RADAR_OUTPUT_DIR, file)).mtimeMs;
    } catch {
      mtimeMs = 0;
    }
    return { file, mtimeMs };
  });

  return withStats
    .sort((a, b) => b.mtimeMs - a.mtimeMs)
    .slice(0, limit)
    .map(({ file }) => {
      const base = file.replace(/\.html$/, "");
      const csvFile = `${base}.csv`;
      const jsonFile = `${base}.json`;
      return {
        base,
        htmlPath: file,
        csvPath: csvFile,
        jsonPath: jsonFile,
        hasCsv: exists(path.join(RADAR_OUTPUT_DIR, csvFile)),
        hasJson: exists(path.join(RADAR_OUTPUT_DIR, jsonFile))
      };
    });
}

// Finds prior scans for one tracked topic by its slug (google_trend_radar.py
// names files trend_radar_{slug}_{timestamp}.{ext}, and a tracked topic's id
// is generated with that same slug), newest first.
export function listScansForSlug(slug, limit = 12) {
  if (!exists(RADAR_OUTPUT_DIR)) return [];
  const prefix = `trend_radar_${slug}_`;
  const jsonFiles = fs.readdirSync(RADAR_OUTPUT_DIR).filter((f) => f.startsWith(prefix) && f.endsWith(".json"));

  const withStats = jsonFiles.map((file) => {
    let mtimeMs = 0;
    try {
      mtimeMs = fs.statSync(path.join(RADAR_OUTPUT_DIR, file)).mtimeMs;
    } catch {
      mtimeMs = 0;
    }
    return { file, mtimeMs };
  });

  return withStats
    .sort((a, b) => b.mtimeMs - a.mtimeMs)
    .slice(0, limit)
    .map(({ file, mtimeMs }) => {
      const base = file.replace(/\.json$/, "");
      return { base, jsonPath: file, htmlPath: `${base}.html`, mtimeMs };
    });
}

// Reads the JSON payload of the most recent scan (any topic/profile) so the
// dashboard can show a plain keyword list inline instead of only linking out
// to a separate HTML file per scan.
export function getLatestRadarScanData() {
  if (!exists(RADAR_OUTPUT_DIR)) return null;

  const jsonFiles = fs.readdirSync(RADAR_OUTPUT_DIR).filter((f) => f.endsWith(".json"));
  if (!jsonFiles.length) return null;

  const withStats = jsonFiles.map((file) => {
    let mtimeMs = 0;
    try {
      mtimeMs = fs.statSync(path.join(RADAR_OUTPUT_DIR, file)).mtimeMs;
    } catch {
      mtimeMs = 0;
    }
    return { file, mtimeMs };
  });

  const latest = withStats.sort((a, b) => b.mtimeMs - a.mtimeMs)[0];
  if (!latest) return null;

  try {
    const raw = fs.readFileSync(path.join(RADAR_OUTPUT_DIR, latest.file), "utf-8");
    const data = JSON.parse(raw);
    const base = latest.file.replace(/\.json$/, "");
    return { ...data, htmlPath: `${base}.html` };
  } catch {
    return null;
  }
}
