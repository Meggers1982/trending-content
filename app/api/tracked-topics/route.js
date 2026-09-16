import { NextResponse } from "next/server";
import { checkRunToken } from "@/lib/auth";
import { MAX_TOPIC_LENGTH, normalizeGeo, normalizeProfile, validateTopic } from "@/lib/radar-profiles";
import {
  TRACKED_TOPICS_UNAVAILABLE_MESSAGE,
  addTrackedTopic,
  isTrackedTopicsConfigured,
  readTrackedTopics
} from "@/lib/tracked-topics";

export const dynamic = "force-dynamic";

export async function GET() {
  if (!isTrackedTopicsConfigured()) {
    return NextResponse.json({
      tracked: [],
      unavailable: true,
      message: TRACKED_TOPICS_UNAVAILABLE_MESSAGE
    });
  }

  const tracked = await readTrackedTopics();
  return NextResponse.json({ tracked });
}

export async function POST(request) {
  const tokenError = checkRunToken(request);
  if (tokenError) return tokenError;

  if (!isTrackedTopicsConfigured()) {
    return NextResponse.json(
      { ok: false, unavailable: true, message: TRACKED_TOPICS_UNAVAILABLE_MESSAGE },
      { status: 503 }
    );
  }

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
    return NextResponse.json(result, { status: 409 });
  }
  return NextResponse.json(result);
}
