import fs from "node:fs";
import path from "node:path";
import { slugifyTopic } from "@/lib/radar-profiles";

const ROOT = process.cwd();
const TRACKED_TOPICS_PATH = path.join(ROOT, "data", "tracked_topics.json");
const TRACKED_TOPICS_REPO_PATH = "data/tracked_topics.json";

function readLocal() {
  try {
    if (!fs.existsSync(TRACKED_TOPICS_PATH)) return { tracked_topics: [] };
    const raw = fs.readFileSync(TRACKED_TOPICS_PATH, "utf-8");
    const parsed = JSON.parse(raw);
    return { tracked_topics: Array.isArray(parsed.tracked_topics) ? parsed.tracked_topics : [] };
  } catch {
    return { tracked_topics: [] };
  }
}

function writeLocal(data) {
  fs.mkdirSync(path.dirname(TRACKED_TOPICS_PATH), { recursive: true });
  fs.writeFileSync(TRACKED_TOPICS_PATH, `${JSON.stringify(data, null, 2)}\n`, "utf-8");
}

// Vercel's deployed filesystem is ephemeral/read-only, so writes there can't
// use fs directly (and wouldn't be seen by GitHub Actions anyway) — this
// branch commits through GitHub's Contents API instead, same "Vercel writes
// back through GitHub" pattern app/api/run uses to trigger the pipeline.
function isVercel() {
  return Boolean(process.env.VERCEL);
}

async function readRemote() {
  const repo = process.env.GITHUB_REPOSITORY || "Meggers1982/trending-content";
  const ref = process.env.GITHUB_PIPELINE_REF || "main";
  const token = process.env.GITHUB_PIPELINE_TOKEN;
  const headers = {
    accept: "application/vnd.github.raw+json",
    "x-github-api-version": "2022-11-28",
    ...(token ? { authorization: `Bearer ${token}` } : {})
  };
  const response = await fetch(
    `https://api.github.com/repos/${repo}/contents/${TRACKED_TOPICS_REPO_PATH}?ref=${ref}`,
    { headers, cache: "no-store" }
  );
  if (!response.ok) return { tracked_topics: [] };
  try {
    const parsed = JSON.parse(await response.text());
    return { tracked_topics: Array.isArray(parsed.tracked_topics) ? parsed.tracked_topics : [] };
  } catch {
    return { tracked_topics: [] };
  }
}

async function writeRemote(data) {
  const repo = process.env.GITHUB_REPOSITORY || "Meggers1982/trending-content";
  const ref = process.env.GITHUB_PIPELINE_REF || "main";
  const token = process.env.GITHUB_PIPELINE_TOKEN;
  if (!token) {
    return { ok: false, message: "GITHUB_PIPELINE_TOKEN is not configured in Vercel." };
  }

  const apiBase = `https://api.github.com/repos/${repo}/contents/${TRACKED_TOPICS_REPO_PATH}`;
  const headers = {
    accept: "application/vnd.github+json",
    authorization: `Bearer ${token}`,
    "content-type": "application/json",
    "x-github-api-version": "2022-11-28"
  };

  // The Contents API requires the current file's sha to update it in place.
  const current = await fetch(`${apiBase}?ref=${ref}`, { headers, cache: "no-store" });
  const sha = current.ok ? (await current.json()).sha : undefined;

  const content = Buffer.from(`${JSON.stringify(data, null, 2)}\n`, "utf-8").toString("base64");
  const response = await fetch(apiBase, {
    method: "PUT",
    headers,
    body: JSON.stringify({
      message: "Update tracked topics",
      content,
      branch: ref,
      ...(sha ? { sha } : {})
    })
  });

  if (!response.ok) {
    const detail = await response.text();
    return { ok: false, message: `GitHub commit failed: ${detail}` };
  }
  return { ok: true };
}

async function readAll() {
  return isVercel() ? readRemote() : readLocal();
}

async function writeAll(data) {
  return isVercel() ? writeRemote(data) : (writeLocal(data), { ok: true });
}

export async function readTrackedTopics() {
  const data = await readAll();
  return data.tracked_topics;
}

export async function getTrackedTopic(id) {
  const data = await readAll();
  return data.tracked_topics.find((entry) => entry.id === id) || null;
}

export async function addTrackedTopic({ topic, profile, geo }) {
  const data = await readAll();
  const id = slugifyTopic(topic);
  if (data.tracked_topics.some((entry) => entry.id === id)) {
    return { ok: false, message: "This topic is already tracked." };
  }
  const entry = {
    id,
    topic,
    profile,
    geo,
    created_at: new Date().toISOString(),
    last_scanned_at: null
  };
  data.tracked_topics.push(entry);
  const result = await writeAll(data);
  if (!result.ok) return result;
  return { ok: true, entry };
}

export async function removeTrackedTopic(id) {
  const data = await readAll();
  const next = data.tracked_topics.filter((entry) => entry.id !== id);
  if (next.length === data.tracked_topics.length) {
    return { ok: false, message: "Tracked topic not found." };
  }
  const result = await writeAll({ tracked_topics: next });
  if (!result.ok) return result;
  return { ok: true };
}
