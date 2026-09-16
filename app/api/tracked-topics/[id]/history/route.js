import { NextResponse } from "next/server";
import { listScansForSlug } from "@/lib/radar";
import {
  TRACKED_TOPICS_UNAVAILABLE_MESSAGE,
  getTrackedTopic,
  isTrackedTopicsConfigured
} from "@/lib/tracked-topics";

export const dynamic = "force-dynamic";

export async function GET(_request, { params }) {
  if (!isTrackedTopicsConfigured()) {
    return NextResponse.json(
      { ok: false, unavailable: true, message: TRACKED_TOPICS_UNAVAILABLE_MESSAGE },
      { status: 503 }
    );
  }

  const { id } = await params;
  const topic = await getTrackedTopic(id);
  if (!topic) {
    return NextResponse.json({ ok: false, message: "Tracked topic not found." }, { status: 404 });
  }
  return NextResponse.json({ topic, scans: listScansForSlug(id) });
}
