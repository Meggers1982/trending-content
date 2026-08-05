// Shared by the ad-hoc scan form (/api/radar) and tracked topics
// (/api/tracked-topics, run_tracked_topics.py's --profile choices mirror this
// list) so topic/profile/geo validation stays in one place.
export const ALLOWED_PROFILES = new Set([
  "auto",
  "wellness",
  "health",
  "ai",
  "beauty",
  "nutrition",
  "fitness",
  "food-safety",
  "diet",
  "weight-loss",
  "mental-health",
  "gut-health",
  "none"
]);

export const PROFILES = Array.from(ALLOWED_PROFILES);

export const MAX_TOPIC_LENGTH = 100;

export function validateTopic(topic) {
  if (typeof topic !== "string") return null;
  const trimmed = topic.trim();
  if (!trimmed || trimmed.length > MAX_TOPIC_LENGTH) return null;
  if (trimmed.startsWith("-")) return null; // would otherwise be parsed as a CLI flag
  return trimmed;
}

export function normalizeGeo(geo) {
  return typeof geo === "string" && geo.trim() ? geo.trim().slice(0, 5) : "US";
}

export function normalizeProfile(profile) {
  return ALLOWED_PROFILES.has(profile) ? profile : "auto";
}

// Mirrors google_trend_radar.py's slug: re.sub(r"[^a-z0-9]+", "-", topic.lower()).strip("-")
export function slugifyTopic(topic) {
  const slug = `${topic || ""}`.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "");
  return slug || "topic";
}
