import { NextResponse } from "next/server";
import { checkRunToken } from "@/lib/auth";
import {
  TRACKED_TOPICS_UNAVAILABLE_MESSAGE,
  isTrackedTopicsConfigured,
  removeTrackedTopic
} from "@/lib/tracked-topics";

export const dynamic = "force-dynamic";

export async function DELETE(request, { params }) {
  const tokenError = checkRunToken(request);
  if (tokenError) return tokenError;

  if (!isTrackedTopicsConfigured()) {
    return NextResponse.json(
      { ok: false, unavailable: true, message: TRACKED_TOPICS_UNAVAILABLE_MESSAGE },
      { status: 503 }
    );
  }

  const { id } = await params;
  const result = await removeTrackedTopic(id);
  if (!result.ok) {
    return NextResponse.json(result, { status: 404 });
  }
  return NextResponse.json(result);
}
