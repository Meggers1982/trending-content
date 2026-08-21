"use client";

import { useEffect, useState } from "react";

export const RUN_TOKEN_STORAGE_KEY = "trending-content-os:run-token";
const RUN_TOKEN_EVENT = "trending-content-os:run-token-change";

export function readRunToken() {
  if (typeof window === "undefined") return "";
  return window.localStorage.getItem(RUN_TOKEN_STORAGE_KEY) || "";
}

/**
 * One token, one value — but it is needed by three separate panels (pipeline
 * runs, ad-hoc scans, tracked topics). Each panel used to render its own input
 * against the same storage key, so editing one left the others showing stale
 * text until a reload. This keeps every instance in sync, and hides the field
 * behind a disclosure because it is only relevant when the app is deployed with
 * RUN_CONTROL_TOKEN set.
 */
export default function RunTokenField() {
  const [runToken, setRunToken] = useState("");

  useEffect(() => {
    setRunToken(readRunToken());
    const sync = (event) => setRunToken(event.detail ?? readRunToken());
    window.addEventListener(RUN_TOKEN_EVENT, sync);
    // `storage` only fires in *other* tabs, so the custom event covers this one.
    window.addEventListener("storage", sync);
    return () => {
      window.removeEventListener(RUN_TOKEN_EVENT, sync);
      window.removeEventListener("storage", sync);
    };
  }, []);

  function handleChange(event) {
    const value = event.target.value;
    setRunToken(value);
    window.localStorage.setItem(RUN_TOKEN_STORAGE_KEY, value);
    window.dispatchEvent(new CustomEvent(RUN_TOKEN_EVENT, { detail: value }));
  }

  return (
    <details className="runTokenDisclosure">
      <summary>
        Run token
        <span className={`badge ${runToken ? "good" : ""}`}>{runToken ? "saved" : "not set"}</span>
      </summary>
      <label>
        Only needed when this app is deployed with <code>RUN_CONTROL_TOKEN</code> set. Stored in
        this browser and shared across all three panels.
        <input
          type="password"
          value={runToken}
          onChange={handleChange}
          autoComplete="off"
          placeholder="Paste token"
        />
      </label>
    </details>
  );
}
