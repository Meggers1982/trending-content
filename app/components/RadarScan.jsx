"use client";

import { useEffect, useState } from "react";

const RUN_TOKEN_STORAGE_KEY = "trending-content-os:run-token";
const PROFILES = ["auto", "wellness", "health", "ai", "none"];

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

  async function loadStatus() {
    const response = await fetch("/api/radar", { cache: "no-store" });
    const data = await response.json();
    setJob(data.job);
    setRecentScans(data.recentScans || []);
  }

  async function startScan(event) {
    event.preventDefault();
    setMessage("");
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

  useEffect(() => {
    setRunToken(window.localStorage.getItem(RUN_TOKEN_STORAGE_KEY) || "");
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
    <div className="radarScan">
      <div className="panelHeader">
        <span>Ad-hoc Trend Scan</span>
        <strong>{formatStatus(job)}</strong>
      </div>
      <p>
        Runs google_trend_radar.py directly against SerpAPI for any topic — no Anthropic
        API cost, not tied to the health/wellness niche. Local/self-hosted only.
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
            View Scan Result
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
                <a href={`/api/radar-artifact/${scan.htmlPath}`} target="_blank" rel="noreferrer">
                  {scan.base.replace(/^trend_radar_/, "").replace(/_\d{4}-\d{2}-\d{2}_\d{4}$/, "")}
                </a>
                {scan.hasCsv ? (
                  <a href={`/api/radar-artifact/${scan.csvPath}`} target="_blank" rel="noreferrer">CSV</a>
                ) : null}
              </li>
            ))}
          </ul>
        </div>
      ) : null}
    </div>
  );
}
