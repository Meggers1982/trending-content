import { NextResponse } from "next/server";
import { checkRunToken } from "@/lib/auth";
import { explainRunError } from "@/lib/error-messages";
import { removeTrackedTopic } from "@/lib/tracked-topics";

export const dynamic = "force-dynamic";

export async function DELETE(request, { params }) {
  const tokenError = checkRunToken(request);
  if (tokenError) return tokenError;

  const { id } = await params;
  const result = await removeTrackedTopic(id);
  if (!result.ok) {
    // Only re-explain infra/credential failures (always prefixed "GitHub..."
    // by lib/tracked-topics.js) - leave "not found" exactly as it is.
    const message = result.message?.toLowerCase().startsWith("github")
      ? explainRunError(result.message, "track")
      : result.message;
    return NextResponse.json({ ...result, message }, { status: 404 });
  }
  return NextResponse.json(result);
}
