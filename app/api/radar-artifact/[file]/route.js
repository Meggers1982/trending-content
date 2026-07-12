import { NextResponse } from "next/server";
import { resolveRadarArtifact } from "@/lib/radar";
import { readArtifactResponse } from "@/lib/artifact-paths";

export const dynamic = "force-dynamic";

export async function GET(_request, { params }) {
  const resolvedParams = await params;
  const fileName = resolvedParams.file;
  const artifact = resolveRadarArtifact(fileName);
  if (!artifact) {
    return new NextResponse("Not found", { status: 404 });
  }

  const { body, contentType } = readArtifactResponse(artifact);
  return new NextResponse(body, {
    headers: {
      "content-type": contentType
    }
  });
}
