"use client";

import { useEffect, useState } from "react";
import RadarResultsTable from "./RadarResultsTable";
import RunTokenField, { readRunToken } from "./RunTokenField";
import TopicScanForm from "./TopicScanForm";

function formatStatus(job) {
  if (job?.running) return `Scanning "${job.mode}"`;
  if (job?.exitCode === 0) return "Complete";
  if (job?.exitCode) return "Needs attention";
  return "Ready";
}

// Scan artifacts are named trend_radar_<slug>_<date>_<HHMM>. The label used to
// strip the timestamp off, which made every repeat scan of the same profile
// render as an identical row with no way to tell them apart.
function describeScan(base) {
  const match = `${base}`.match(/^trend_radar_(.+)_(\d{4}-\d{2}-\d{2})_(\d{2})(\d{2})$/);
  if (!match) return { name: `${base}`.replace(/^trend_radar_/, ""), when: "" };
  const [, slug, date, hh, mm] = match;
  return { name: slug.replace(/-/g, " "), when: `${date} ${hh}:${mm}` };
}

export default function RadarScan() {
  const [job, setJob] = useState(null);
  const [recentScans, setRecentScans] = useState([]);
  const [message, setMessage] = useState("");
  const [topic, setTopic] = useState("");
  const [geo, setGeo] = useState("US");
  const [profile, setProfile] = useState("auto");
  const [viewedScan, setViewedScan] = useState(null);
  const [viewedLabel, setViewedLabel] = useState("");
  const [viewLoading, setViewLoading] = useState(false);
  const [lastScanParams, setLastScanParams] = useState(null);
  const [trackMessage, setTrackMessage] = useState("");

  async function loadStatus() {
    const response = await fetch("/api/radar", { cache: "no-store" });
    const data = await response.json();
    setJob(data.job);
    setRecentScans(data.recentScans || []);
  }

  async function startScan(event) {
    event.preventDefault();
    // Read at request time: the token lives in a shared field that any panel
    // can edit, so a value captured at mount could be stale.
    const token = readRunToken();
    setMessage("");
    setTrackMessage("");
    setViewedScan(null);
    setLastScanParams({ topic, profile, geo });
    const response = await fetch("/api/radar", {
      method: "POST",
      headers: {
        "content-type": "application/json",
        ...(token ? { "x-run-token": token } : {})
      },
      body: JSON.stringify({ topic, geo, profile })
    });
    const data = await response.json();
    if (!response.ok) {
      setMessage(data.message || "Could not start the scan.");
    }
    setJob(data.job);
  }

  async function trackTopic() {
    if (!lastScanParams) return;
    const token = readRunToken();
    setTrackMessage("");
    const response = await fetch("/api/tracked-topics", {
      method: "POST",
      headers: {
        "content-type": "application/json",
        ...(token ? { "x-run-token": token } : {})
      },
      body: JSON.stringify(lastScanParams)
    });
    const data = await response.json();
    setTrackMessage(data.ok ? "Tracked — see it in Tracked Topics below." : (data.message || "Could not track this topic."));
  }

  async function viewScan(jsonPath, label) {
    setViewLoading(true);
    setMessage("");
    try {
      const response = await fetch(`/api/radar-artifact/${jsonPath}`, { cache: "no-store" });
      if (!response.ok) throw new Error("Result file not found.");
      const data = await response.json();
      setViewedScan(data);
      setViewedLabel(label);
    } catch (error) {
      setMessage(error.message || "Could not load scan results.");
    } finally {
      setViewLoading(false);
    }
  }

  useEffect(() => {
    loadStatus();
  }, []);

  useEffect(() => {
    if (!job?.running) return undefined;
    const timer = setInterval(loadStatus, 2000);
    return () => clearInterval(timer);
  }, [job?.running]);

  useEffect(() => {
    if (job?.exitCode === 0 && job.resultFile) {
      const jsonPath = job.resultFile.replace(/\.html$/, ".json");
      viewScan(jsonPath, job.mode || topic);
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [job?.resultFile, job?.exitCode]);

  const running = Boolean(job?.running);
  const logs = job?.logs || [];

  return (
    <div className="radarScan">
      <div className="panelHeader">
        <span>Ad-hoc Trend Scan</span>
        <strong>{formatStatus(job)}</strong>
      </div>
      <p>
        Scan any topic for rising search terms — free of Anthropic API cost, and not limited to
        health and wellness.
      </p>
      <TopicScanForm
        topic={topic}
        onTopic={setTopic}
        profile={profile}
        onProfile={setProfile}
        geo={geo}
        onGeo={setGeo}
        onSubmit={startScan}
        submitLabel="Scan"
        submitting={running}
      />
      <details className="panelNote">
        <summary>How this works</summary>
        <p>
          Runs <code>google_trend_radar.py</code> directly against SerpAPI, scoring trends in code
          rather than with Claude — so it costs nothing beyond the SerpAPI request. The{" "}
          <code>beauty</code> profile additionally cross-checks Reddit and tags
          ingredient/benefit/concern terms. Works locally or self-hosted; on Vercel the scan
          endpoint returns 501 because there is no Python process to run.
        </p>
      </details>
      <RunTokenField />
      {message || job?.friendlyError ? (
        <p className="runMessage">{message || job.friendlyError}</p>
      ) : null}
      {job?.exitCode === 0 && job.resultFile ? (
        <p>
          <a className="button" href={`/api/radar-artifact/${job.resultFile}`} target="_blank" rel="noreferrer">
            Open Raw HTML
          </a>
        </p>
      ) : null}
      {logs.length ? (
        <div className="logBox" aria-live="polite">
          {logs.slice(-12).map((line, index) => (
            <div key={`${line}-${index}`}>{line}</div>
          ))}
        </div>
      ) : null}
      {recentScans.length ? (
        <div className="radarScanHistory">
          <span>Recent scans</span>
          <ul>
            {recentScans.map((scan) => {
              const { name, when } = describeScan(scan.base);
              return (
                <li key={scan.base}>
                  {/* The whole row opens the results; the small links are the
                      escape hatches to the raw files. */}
                  {scan.hasJson ? (
                    <button
                      type="button"
                      className="scanRowOpen"
                      onClick={() => viewScan(scan.jsonPath, name)}
                    >
                      <strong>{name}</strong>
                      <em>{when}</em>
                    </button>
                  ) : (
                    <span className="scanRowOpen">
                      <strong>{name}</strong>
                      <em>{when}</em>
                    </span>
                  )}
                  <a href={`/api/radar-artifact/${scan.htmlPath}`} target="_blank" rel="noreferrer">HTML</a>
                  {scan.hasCsv ? (
                    <a href={`/api/radar-artifact/${scan.csvPath}`} target="_blank" rel="noreferrer">CSV</a>
                  ) : null}
                </li>
              );
            })}
          </ul>
        </div>
      ) : null}
      {viewLoading ? <p className="runMessage">Loading results…</p> : null}
      {viewedScan ? (
        <div className="radarViewedScan">
          <div className="panelHeader">
            <span>Results — {viewedLabel}</span>
            <strong>{viewedScan.summary?.total_retained ?? viewedScan.candidates?.length ?? 0} retained</strong>
          </div>
          {lastScanParams ? (
            <p>
              <button type="button" className="button" onClick={trackTopic}>
                Track this topic
              </button>
              {trackMessage ? <span style={{ marginLeft: 10, fontSize: 12, color: "var(--muted)" }}>{trackMessage}</span> : null}
            </p>
          ) : null}
          <RadarResultsTable data={viewedScan} />
        </div>
      ) : null}
    </div>
  );
}
