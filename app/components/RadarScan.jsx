"use client";

import { useEffect, useState } from "react";
import RadarResultsTable from "./RadarResultsTable";
import { PROFILES } from "@/lib/radar-profiles";

const RUN_TOKEN_STORAGE_KEY = "trending-content-os:run-token";

function formatStatus(job) {
  if (job?.running) return `Scanning "${job.mode}"`;
  if (job?.exitCode === 0) return "Complete";
  if (job?.exitCode) return "Needs attention";
  return "Ready";
}

export default function RadarScan() {
  const [job, setJob] = useState(null);
  const [recentScans, setRecentScans] = useState([]);
  const [message, setMessage] = useState("");
  const [topic, setTopic] = useState("");
  const [geo, setGeo] = useState("US");
  const [profile, setProfile] = useState("auto");
  const [runToken, setRunToken] = useState("");
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
    setMessage("");
    setTrackMessage("");
    setViewedScan(null);
    setLastScanParams({ topic, profile, geo });
    const response = await fetch("/api/radar", {
      method: "POST",
      headers: {
        "content-type": "application/json",
        ...(runToken ? { "x-run-token": runToken } : {})
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
    setTrackMessage("");
    const response = await fetch("/api/tracked-topics", {
      method: "POST",
      headers: {
        "content-type": "application/json",
        ...(runToken ? { "x-run-token": runToken } : {})
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
    setRunToken(window.localStorage.getItem(RUN_TOKEN_STORAGE_KEY) || "");
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
        Runs google_trend_radar.py directly against SerpAPI for any topic — no Anthropic
        API cost, not tied to the health/wellness niche. Local/self-hosted only. The
        beauty profile also cross-checks Reddit and tags ingredient/benefit/concern terms.
      </p>
      <form className="radarScanForm" onSubmit={startScan}>
        <input
          type="text"
          value={topic}
          onChange={(event) => setTopic(event.target.value)}
          placeholder="Topic, e.g. &quot;AI tools&quot; or &quot;gut health&quot;"
          maxLength={100}
          required
        />
        <select value={profile} onChange={(event) => setProfile(event.target.value)}>
          {PROFILES.map((option) => (
            <option key={option} value={option}>{option}</option>
          ))}
        </select>
        <input
          type="text"
          value={geo}
          onChange={(event) => setGeo(event.target.value)}
          placeholder="Geo"
          maxLength={5}
          className="radarScanGeo"
        />
        <button className="button primary" type="submit" disabled={running || !topic.trim()}>
          Scan
        </button>
      </form>
      <label className="runTokenField">
        Run token (only needed if deployed with RUN_CONTROL_TOKEN)
        <input
          type="password"
          value={runToken}
          onChange={(event) => {
            setRunToken(event.target.value);
            window.localStorage.setItem(RUN_TOKEN_STORAGE_KEY, event.target.value);
          }}
          autoComplete="off"
          placeholder="optional"
        />
      </label>
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
            {recentScans.map((scan) => (
              <li key={scan.base}>
                <span>{scan.base.replace(/^trend_radar_/, "").replace(/_\d{4}-\d{2}-\d{2}_\d{4}$/, "")}</span>
                {scan.hasJson ? (
                  <a href="#" onClick={(event) => { event.preventDefault(); viewScan(scan.jsonPath, scan.base); }}>
                    View
                  </a>
                ) : null}
                <a href={`/api/radar-artifact/${scan.htmlPath}`} target="_blank" rel="noreferrer">HTML</a>
                {scan.hasCsv ? (
                  <a href={`/api/radar-artifact/${scan.csvPath}`} target="_blank" rel="noreferrer">CSV</a>
                ) : null}
              </li>
            ))}
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
