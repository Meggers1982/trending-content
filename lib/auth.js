import { NextResponse } from "next/server";

// Shared by every mutating route (radar/run/tracked-topics scans): if
// RUN_CONTROL_TOKEN is set, the caller must echo it back in x-run-token.
export function checkRunToken(request) {
  const runControlToken = process.env.RUN_CONTROL_TOKEN;
  if (!runControlToken) return null;
  const providedToken = request.headers.get("x-run-token");
  if (providedToken !== runControlToken) {
    return NextResponse.json({ ok: false, message: "Invalid or missing run token." }, { status: 401 });
  }
  return null;
}
