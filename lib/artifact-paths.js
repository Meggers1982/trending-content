import fs from "node:fs";
import path from "node:path";

const MIME = {
  ".html": "text/html; charset=utf-8",
  ".md": "text/plain; charset=utf-8",
  ".csv": "text/csv; charset=utf-8",
  ".json": "application/json; charset=utf-8"
};

// Shared by lib/runs.js and lib/radar.js: resolves a user-supplied file name
// to a real path inside `baseDir`, rejecting traversal attempts. path.basename()
// strips any directory components, and the equality check rejects encoded
// separators (e.g. "%2e%2e") since Next.js decodes the [file] param before
// this runs, so a traversal payload wouldn't equal its own basename.
export function resolveSafePath(baseDir, fileName) {
  const safeName = path.basename(fileName || "");
  if (!safeName || safeName !== fileName) return null;
  const fullPath = path.join(baseDir, safeName);
  if (!fullPath.startsWith(baseDir)) return null;
  try {
    if (!fs.existsSync(fullPath)) return null;
  } catch {
    return null;
  }
  return fullPath;
}

export function readArtifactResponse(fullPath) {
  const ext = path.extname(fullPath);
  return {
    body: fs.readFileSync(fullPath),
    contentType: MIME[ext] || "application/octet-stream"
  };
}
