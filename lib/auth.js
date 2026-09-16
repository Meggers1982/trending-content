import { NextResponse } from "next/server";

function isProductionRuntime() {
  return Boolean(process.env.VERCEL || process.env.NODE_ENV === "production");
}

function isAuthOptional() {
  return process.env.RUN_CONTROL_AUTH_OPTIONAL === "true";
}

// Shared by every mutating route (radar/run/tracked-topics scans): deployed
// production must configure RUN_CONTROL_TOKEN, then callers must echo it back
// in x-run-token. Local development can omit it unless explicitly set.
export function checkRunToken(request) {
  const runControlToken = process.env.RUN_CONTROL_TOKEN;
  if (!runControlToken) {
    if (isProductionRuntime() && !isAuthOptional()) {
      return NextResponse.json(
        { ok: false, message: "RUN_CONTROL_TOKEN is not configured for this deployment." },
        { status: 503 }
      );
    }
    return null;
  }

  const providedToken = request.headers.get("x-run-token");
  if (providedToken !== runControlToken) {
    return NextResponse.json({ ok: false, message: "Invalid or missing run token." }, { status: 401 });
  }
  return null;
}
