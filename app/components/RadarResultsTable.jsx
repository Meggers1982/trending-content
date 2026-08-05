"use client";

import { useMemo, useState } from "react";
import { scoreBar, stageBadge, tagChips } from "@/lib/dashboard-ui";

const SORT_OPTIONS = [
  { key: "radar_score", label: "Radar score" },
  { key: "opportunity_score", label: "Opportunity" },
  { key: "trend_stage", label: "Stage" },
  { key: "urgency", label: "Urgency" },
  { key: "topic", label: "Topic" }
];

const STAGE_ORDER = { breakout: 0, emerging: 1, rising: 2, watch: 3 };

function compareValues(a, b, key) {
  if (key === "trend_stage") {
    return (STAGE_ORDER[a.trend_stage] ?? 9) - (STAGE_ORDER[b.trend_stage] ?? 9);
  }
  const av = a[key];
  const bv = b[key];
  if (typeof av === "number" && typeof bv === "number") return av - bv;
  return `${av || ""}`.localeCompare(`${bv || ""}`);
}

export default function RadarResultsTable({ data }) {
  const [sortKey, setSortKey] = useState("radar_score");
  const [sortDir, setSortDir] = useState("desc");
  const [filterText, setFilterText] = useState("");
  const [filterStage, setFilterStage] = useState("all");

  const candidates = data?.candidates || [];

  const stages = useMemo(() => {
    const set = new Set(candidates.map((c) => c.trend_stage).filter(Boolean));
    return ["all", ...Array.from(set)];
  }, [candidates]);

  const rows = useMemo(() => {
    const needle = filterText.trim().toLowerCase();
    let filtered = candidates.filter((c) => {
      if (filterStage !== "all" && c.trend_stage !== filterStage) return false;
      if (needle && !`${c.topic || ""}`.toLowerCase().includes(needle)) return false;
      return true;
    });
    filtered.sort((a, b) => compareValues(a, b, sortKey) * (sortDir === "asc" ? 1 : -1));
    return filtered;
  }, [candidates, filterText, filterStage, sortKey, sortDir]);

  function toggleSort(key) {
    if (key === sortKey) {
      setSortDir((dir) => (dir === "asc" ? "desc" : "asc"));
    } else {
      setSortKey(key);
      setSortDir("desc");
    }
  }

  if (!candidates.length) {
    return <p className="runMessage">This scan retained no candidates.</p>;
  }

  return (
    <div className="radarResultsTable">
      <div className="radarResultsControls">
        <input
          type="text"
          value={filterText}
          onChange={(event) => setFilterText(event.target.value)}
          placeholder="Filter by topic…"
        />
        <select value={filterStage} onChange={(event) => setFilterStage(event.target.value)}>
          {stages.map((stage) => (
            <option key={stage} value={stage}>{stage === "all" ? "All stages" : stage}</option>
          ))}
        </select>
        <select value={sortKey} onChange={(event) => toggleSort(event.target.value)}>
          {SORT_OPTIONS.map((option) => (
            <option key={option.key} value={option.key}>Sort: {option.label}</option>
          ))}
        </select>
        <button
          type="button"
          className="button"
          onClick={() => setSortDir((dir) => (dir === "asc" ? "desc" : "asc"))}
        >
          {sortDir === "asc" ? "↑ Asc" : "↓ Desc"}
        </button>
      </div>
      <div className="tableWrap">
        <table>
          <thead>
            <tr>
              <th onClick={() => toggleSort("trend_stage")}>Stage</th>
              <th onClick={() => toggleSort("topic")}>Topic</th>
              <th onClick={() => toggleSort("radar_score")}>Radar</th>
              <th onClick={() => toggleSort("opportunity_score")}>Opportunity</th>
              <th onClick={() => toggleSort("urgency")}>Urgency</th>
              <th>Tags</th>
              <th>Discovered via</th>
            </tr>
          </thead>
          <tbody>
            {rows.map((candidate, index) => (
              <tr key={`${candidate.topic}-${index}`}>
                <td>{stageBadge(candidate.trend_stage)}</td>
                <td>
                  <strong>{candidate.topic}</strong>
                  <span>{candidate.why_now}</span>
                </td>
                <td>
                  <b>{candidate.radar_score}</b>
                  {scoreBar(candidate.radar_score, "red")}
                </td>
                <td>
                  <b>{candidate.opportunity_score}</b>
                  {scoreBar(candidate.opportunity_score, "blue")}
                </td>
                <td>{candidate.urgency || "—"}</td>
                <td>{tagChips(candidate.tags)}</td>
                <td>{(candidate.discovery_sources || []).join(", ") || "—"}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <p className="radarResultsCount">{rows.length} of {candidates.length} candidates shown</p>
    </div>
  );
}
