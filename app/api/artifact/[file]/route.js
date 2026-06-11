import fs from "node:fs";
import path from "node:path";
import { NextResponse } from "next/server";
import { resolveArtifact } from "@/lib/runs";

export const dynamic = "force-dynamic";

const MIME = {
  ".html": "text/html; charset=utf-8",
  ".md": "text/plain; charset=utf-8",
  ".csv": "text/csv; charset=utf-8",
  ".json": "application/json; charset=utf-8"
};

export async function GET(_request, { params }) {
  const resolvedParams = await params;
  const fileName = resolvedParams.file;
  const artifact = resolveArtifact(fileName);
  if (!artifact) {
    return new NextResponse("Not found", { status: 404 });
  }

  const ext = path.extname(artifact);
  const body = fs.readFileSync(artifact);
  return new NextResponse(body, {
    headers: {
      "content-type": MIME[ext] || "application/octet-stream"
    }
  });
}
