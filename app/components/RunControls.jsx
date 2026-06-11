"use client";

import { useEffect, useState } from "react";

function formatStatus(job) {
  if (job?.running) {
    return job.mode === "prefetch" ? "Refreshing radar" : "Generating report";
  }
  if (job?.exitCode === 0) return "Complete";
  if (job?.exitCode) return "Needs attention";
  return "Ready";
}

export default function RunControls() {
  const [job, setJob] = useState(null);
  const [message, setMessage] = useState("");

  async function loadStatus() {
    const response = await fetch("/api/run", { cache: "no-store" });
    const nextJob = await response.json();
    setJob(nextJob);
  }

  async function start(mode) {
    setMessage("");
    const response = await fetch("/api/run", {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({ mode })
    });
    const data = await response.json();
    if (!response.ok) {
      setMessage(data.message || "Could not start the run.");
    }
    setJob(data.job);
  }

  useEffect(() => {
    loadStatus();
  }, []);

  useEffect(() => {
    if (!job?.running) return undefined;
    const timer = setInterval(loadStatus, 2000);
    return () => clearInterval(timer);
  }, [job?.running]);

  const running = Boolean(job?.running);
  const logs = job?.logs || [];

  return (
    <div className="runControls">
      <div className="panelHeader">
        <span>Pipeline Control</span>
        <strong>{formatStatus(job)}</strong>
      </div>
      <div className="runButtons">
        <button className="button primary" type="button" disabled={running} onClick={() => start("full")}>
          Start New Report
        </button>
        <button className="button" type="button" disabled={running} onClick={() => start("prefetch")}>
          Refresh Radar Only
        </button>
      </div>
      <p>
        Full report runs can take a few minutes. When it completes, refresh the page to load
        the new dashboard data.
      </p>
      {message ? <p className="runMessage">{message}</p> : null}
      {logs.length ? (
        <div className="logBox" aria-live="polite">
          {logs.slice(-12).map((line, index) => (
            <div key={`${line}-${index}`}>{line}</div>
          ))}
        </div>
      ) : null}
    </div>
  );
}
