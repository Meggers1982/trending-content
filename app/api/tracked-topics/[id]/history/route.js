import { NextResponse } from "next/server";
import { listScansForSlug } from "@/lib/radar";
import { getTrackedTopic } from "@/lib/tracked-topics";

export const dynamic = "force-dynamic";

export async function GET(_request, { params }) {
  const { id } = await params;
  const topic = await getTrackedTopic(id);
  if (!topic) {
    return NextResponse.json({ ok: false, message: "Tracked topic not found." }, { status: 404 });
  }
  return NextResponse.json({ topic, scans: listScansForSlug(id) });
}
