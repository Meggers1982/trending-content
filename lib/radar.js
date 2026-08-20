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

// google_trend_radar.py names output trend_radar_{topic-slug}_{YYYY-MM-DD_HHMM}.{ext}.
// Sort by that embedded timestamp, not filesystem mtime: a fresh git
// checkout/deploy gives every file a similar mtime, so mtime ordering was
// picking whichever profile's file the checkout happened to write last,
// not the actually most recently generated scan.
function timestampKey(fileName) {
  const match = fileName.match(/_(\d{4}-\d{2}-\d{2}_\d{4})\.[a-z]+$/);
  return match ? match[1] : "";
}

// Turns a "YYYY-MM-DD_HHMM" key into an epoch-ms value for display, since the
// filename's timestamp (not file mtime) is now the source of truth for when
// a scan actually ran.
function timestampKeyToMs(key) {
  const match = key.match(/^(\d{4})-(\d{2})-(\d{2})_(\d{2})(\d{2})$/);
  if (!match) return 0;
  const [, year, month, day, hour, minute] = match;
  return new Date(`${year}-${month}-${day}T${hour}:${minute}:00`).getTime() || 0;
}

export function listRecentRadarScans(limit = 6) {
  if (!exists(RADAR_OUTPUT_DIR)) return [];

  const htmlFiles = fs.readdirSync(RADAR_OUTPUT_DIR).filter((f) => f.endsWith(".html"));

  return htmlFiles
    .map((file) => ({ file, key: timestampKey(file) }))
    .sort((a, b) => b.key.localeCompare(a.key))
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

  return jsonFiles
    .map((file) => ({ file, key: timestampKey(file) }))
    .sort((a, b) => b.key.localeCompare(a.key))
    .slice(0, limit)
    .map(({ file, key }) => {
      const base = file.replace(/\.json$/, "");
      return { base, jsonPath: file, htmlPath: `${base}.html`, mtimeMs: timestampKeyToMs(key) };
    });
}

// Reads the JSON payload of the most recent scan (any topic/profile) so the
// dashboard can show a plain keyword list inline instead of only linking out
// to a separate HTML file per scan.
export function getLatestRadarScanData() {
  if (!exists(RADAR_OUTPUT_DIR)) return null;

  const jsonFiles = fs.readdirSync(RADAR_OUTPUT_DIR).filter((f) => f.endsWith(".json"));
  if (!jsonFiles.length) return null;

  const latest = jsonFiles
    .map((file) => ({ file, key: timestampKey(file) }))
    .sort((a, b) => b.key.localeCompare(a.key))[0];
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
