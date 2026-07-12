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
      return {
        base,
        htmlPath: file,
        csvPath: csvFile,
        hasCsv: exists(path.join(RADAR_OUTPUT_DIR, csvFile))
      };
    });
}
