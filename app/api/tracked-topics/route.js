import { NextResponse } from "next/server";
import { checkRunToken } from "@/lib/auth";
import { explainRunError } from "@/lib/error-messages";
import { MAX_TOPIC_LENGTH, normalizeGeo, normalizeProfile, validateTopic } from "@/lib/radar-profiles";
import { addTrackedTopic, readTrackedTopics } from "@/lib/tracked-topics";

export const dynamic = "force-dynamic";

export async function GET() {
  const tracked = await readTrackedTopics();
  return NextResponse.json({ tracked });
}

export async function POST(request) {
  const tokenError = checkRunToken(request);
  if (tokenError) return tokenError;

  const body = await request.json().catch(() => ({}));
  const topic = validateTopic(body.topic);
  if (!topic) {
    return NextResponse.json(
      { ok: false, message: `Enter a topic (1-${MAX_TOPIC_LENGTH} characters, not starting with "-").` },
      { status: 400 }
    );
  }
  const geo = normalizeGeo(body.geo);
  const profile = normalizeProfile(body.profile);

  const result = await addTrackedTopic({ topic, profile, geo });
  if (!result.ok) {
    // Only re-explain infra/credential failures (always prefixed "GitHub..."
    // by lib/tracked-topics.js) - leave business-logic messages like
    // "already tracked" exactly as they are.
    const message = result.message?.toLowerCase().startsWith("github")
      ? explainRunError(result.message, "track")
      : result.message;
    return NextResponse.json({ ...result, message }, { status: 409 });
  }
  return NextResponse.json(result);
}
