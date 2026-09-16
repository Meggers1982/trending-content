"use client";

import { useEffect, useState } from "react";
import RadarResultsTable from "./RadarResultsTable";
import RunTokenField, { readRunToken } from "./RunTokenField";
import TopicScanForm from "./TopicScanForm";

// Read at call time rather than from state: the token lives in a shared field
// that any panel can edit, so a value captured at mount could be stale.
function authHeaders() {
  const token = readRunToken();
  return {
    "content-type": "application/json",
    ...(token ? { "x-run-token": token } : {})
  };
}

async function readJson(response, fallbackMessage) {
  const data = await response.json().catch(() => ({}));
  if (!response.ok) {
    throw new Error(data.message || fallbackMessage);
  }
  return data;
}

export default function TrackedTopics() {
  const [tracked, setTracked] = useState([]);
  const [loading, setLoading] = useState(true);
  const [trackedError, setTrackedError] = useState("");
  const [message, setMessage] = useState("");
  const [newTopic, setNewTopic] = useState("");
  const [newProfile, setNewProfile] = useState("auto");
  const [newGeo, setNewGeo] = useState("US");
  const [expandedId, setExpandedId] = useState(null);
  const [historyById, setHistoryById] = useState({});
  const [viewedById, setViewedById] = useState({});
  const [statusById, setStatusById] = useState({});
  const [activeScanId, setActiveScanId] = useState(null);

  async function loadTracked() {
    try {
      const response = await fetch("/api/tracked-topics", { cache: "no-store" });
      const data = await readJson(response, "Could not load tracked topics.");
      setTracked(data.tracked || []);
      setTrackedError(data.unavailable ? data.message || "Tracked topics are unavailable." : "");
    } catch (error) {
      setTracked([]);
      setTrackedError(error.message || "Could not load tracked topics.");
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    loadTracked();
  }, []);

  // Local "Scan now" writes to the same shared radarJob the ad-hoc scanner
  // uses (see app/api/radar), so polling that endpoint reports progress for
  // a tracked-topic scan too.
  useEffect(() => {
    if (!activeScanId) return undefined;
    const timer = setInterval(async () => {
      try {
        const response = await fetch("/api/radar", { cache: "no-store" });
        const data = await readJson(response, "Could not read scan progress.");
        const job = data.job;
        if (job?.running) {
          setStatusById((prev) => ({ ...prev, [activeScanId]: `Scanning… (${(job.logs || []).length} log lines)` }));
          return;
        }
        setStatusById((prev) => ({
          ...prev,
          [activeScanId]: job?.exitCode === 0 ? "Scan complete." : (job?.friendlyError || "Scan finished with an error.")
        }));
        await loadHistory(activeScanId);
        await loadTracked();
      } catch (error) {
        setStatusById((prev) => ({ ...prev, [activeScanId]: error.message || "Could not read scan progress." }));
      } finally {
        setActiveScanId(null);
      }
    }, 2000);
    return () => clearInterval(timer);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [activeScanId]);

  async function addTracked(event) {
    event.preventDefault();
    setMessage("");
    try {
      const response = await fetch("/api/tracked-topics", {
        method: "POST",
        headers: authHeaders(),
        body: JSON.stringify({ topic: newTopic, profile: newProfile, geo: newGeo })
      });
      await readJson(response, "Could not track this topic.");
      setNewTopic("");
      await loadTracked();
    } catch (error) {
      setMessage(error.message || "Could not track this topic.");
    }
  }

  async function untrack(id) {
    setMessage("");
    try {
      const response = await fetch(`/api/tracked-topics/${id}`, {
        method: "DELETE",
        headers: authHeaders()
      });
      await readJson(response, "Could not untrack this topic.");
      await loadTracked();
    } catch (error) {
      setMessage(error.message || "Could not untrack this topic.");
    }
  }

  async function loadHistory(id) {
    try {
      const response = await fetch(`/api/tracked-topics/${id}/history`, { cache: "no-store" });
      const data = await readJson(response, "Could not load scan history.");
      setHistoryById((prev) => ({ ...prev, [id]: data.scans || [] }));
    } catch (error) {
      setStatusById((prev) => ({ ...prev, [id]: error.message || "Could not load scan history." }));
      setHistoryById((prev) => ({ ...prev, [id]: [] }));
    }
  }

  async function toggleExpand(id) {
    if (expandedId === id) {
      setExpandedId(null);
      return;
    }
    setExpandedId(id);
    if (!historyById[id]) await loadHistory(id);
  }

  async function viewResult(id, jsonPath, label) {
    try {
      const response = await fetch(`/api/radar-artifact/${jsonPath}`, { cache: "no-store" });
      const data = await readJson(response, "Result file not found.");
      setViewedById((prev) => ({ ...prev, [id]: { data, label } }));
    } catch (error) {
      setStatusById((prev) => ({ ...prev, [id]: error.message || "Result file not found." }));
    }
  }

  async function scanNow(id) {
    setMessage("");
    setStatusById((prev) => ({ ...prev, [id]: "Starting scan…" }));
    try {
      const response = await fetch(`/api/tracked-topics/${id}/scan`, {
        method: "POST",
        headers: authHeaders()
      });
      const data = await readJson(response, "Could not start scan.");
      if (data.dispatched) {
        setStatusById((prev) => ({ ...prev, [id]: data.message || "Scan triggered — check back shortly." }));
        return;
      }
      setActiveScanId(id);
    } catch (error) {
      setStatusById((prev) => ({ ...prev, [id]: error.message || "Could not start scan." }));
    }
  }

  return (
    <div className="radarScan trackedTopics">
      <div className="panelHeader">
        <span>Tracked Topics</span>
        <strong>{tracked.length} tracked</strong>
      </div>
      <p>
        Save specific topic/profile/geo combos to re-scan with one click, or automatically every day
        (see <code>.github/workflows/run-tracked-topics.yml</code>). Manual "Scan now" works locally and,
        when deployed, dispatches the scheduled GitHub Actions workflow for just that topic.
      </p>

      <TopicScanForm
        topic={newTopic}
        onTopic={setNewTopic}
        profile={newProfile}
        onProfile={setNewProfile}
        geo={newGeo}
        onGeo={setNewGeo}
        onSubmit={addTracked}
        submitLabel="Track"
        topicLabel="Topic to track"
        topicPlaceholder="e.g. \u201cGLP-1 news\u201d"
      />

      {message ? <p className="runMessage">{message}</p> : null}
      {trackedError ? <p className="runMessage">{trackedError}</p> : null}

      {loading ? (
        <p>Loading tracked topics…</p>
      ) : trackedError ? (
        <p>Tracked topics will appear here after the database is configured.</p>
      ) : tracked.length ? (
        <div className="trackedTopicsList">
          {tracked.map((item) => (
            <article className="trackedTopicRow" key={item.id}>
              <div className="trackedTopicHeader">
                <div>
                  <strong>{item.topic}</strong>
                  <span>
                    {item.profile} · {item.geo} ·{" "}
                    {item.last_scanned_at ? `last scanned ${new Date(item.last_scanned_at).toLocaleString()}` : "never scanned"}
                  </span>
                </div>
                <div className="trackedTopicActions">
                  <button type="button" className="button" onClick={() => scanNow(item.id)} disabled={Boolean(activeScanId)}>
                    Scan now
                  </button>
                  <button type="button" className="button" onClick={() => toggleExpand(item.id)}>
                    {expandedId === item.id ? "Hide" : "History"}
                  </button>
                  <button type="button" className="button" onClick={() => untrack(item.id)}>
                    Untrack
                  </button>
                </div>
              </div>
              {statusById[item.id] ? <p className="runMessage">{statusById[item.id]}</p> : null}
              {expandedId === item.id ? (
                <div className="trackedTopicHistory">
                  {(historyById[item.id] || []).length ? (
                    <ul>
                      {historyById[item.id].map((scan) => (
                        <li key={scan.base}>
                          <span>{new Date(scan.mtimeMs).toLocaleString()}</span>
                          <a href="#" onClick={(event) => { event.preventDefault(); viewResult(item.id, scan.jsonPath, item.topic); }}>
                            View
                          </a>
                          <a href={`/api/radar-artifact/${scan.htmlPath}`} target="_blank" rel="noreferrer">HTML</a>
                        </li>
                      ))}
                    </ul>
                  ) : (
                    <p>No scans yet for this topic. Click "Scan now" to run the first one.</p>
                  )}
                  {viewedById[item.id] ? (
                    <RadarResultsTable data={viewedById[item.id].data} />
                  ) : null}
                </div>
              ) : null}
            </article>
          ))}
        </div>
      ) : (
        <p>No tracked topics yet. Add one above, or use "Track this topic" after running an ad-hoc scan.</p>
      )}

      <RunTokenField />
    </div>
  );
}
