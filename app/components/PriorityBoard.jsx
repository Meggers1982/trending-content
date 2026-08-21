"use client";

import { useMemo, useState } from "react";
import { scoreBar, badge } from "@/lib/dashboard-ui";
import TableControls from "./TableControls";

const SORT_OPTIONS = [
  { key: "priority_level", label: "Priority" },
  { key: "trend_strength_score", label: "Trend" },
  { key: "opportunity_score", label: "Opportunity" },
  { key: "discover_score", label: "Discover" },
  { key: "topic", label: "Topic" }
];

const PRIORITY_ORDER = { P1: 0, P2: 1, P3: 2, P4: 3, P5: 4 };

// Labelled fields shown when a row is expanded. This is the whole editorial
// payload the pipeline already produces and the board used to throw away.
const DETAIL_FIELDS = [
  { key: "why_now", label: "Why now" },
  { key: "recommended_angle", label: "Recommended angle" },
  { key: "primary_headline", label: "Working headline" },
  { key: "next_steps", label: "Next steps" },
  { key: "signal_type", label: "Signal type" },
  { key: "allowed_category", label: "Category" },
  { key: "content_status", label: "Content status" },
  { key: "urgency", label: "Urgency" }
];

function compareValues(a, b, key) {
  if (key === "priority_level") {
    return (PRIORITY_ORDER[a.priority_level] ?? 9) - (PRIORITY_ORDER[b.priority_level] ?? 9);
  }
  const av = a[key];
  const bv = b[key];
  const an = Number(av);
  const bn = Number(bv);
  if (!Number.isNaN(an) && !Number.isNaN(bn) && `${av}`.trim() && `${bv}`.trim()) return an - bn;
  return `${av || ""}`.localeCompare(`${bv || ""}`);
}

function briefText(candidate) {
  const lines = [candidate.primary_headline || candidate.topic];
  for (const field of DETAIL_FIELDS) {
    const value = `${candidate[field.key] || ""}`.trim();
    if (value) lines.push(`${field.label}: ${value}`);
  }
  const notes = `${candidate.notes || ""}`.trim();
  if (notes) lines.push(`Notes: ${notes}`);
  return lines.join("\n");
}

function priorityTone(level) {
  return `${level || ""}`.toUpperCase();
}

export default function PriorityBoard({ candidates = [], recurrence = {} }) {
  const [filterText, setFilterText] = useState("");
  const [priority, setPriority] = useState("all");
  const [sortKey, setSortKey] = useState("priority_level");
  const [sortDir, setSortDir] = useState("asc");
  const [expanded, setExpanded] = useState(() => new Set());
  const [copied, setCopied] = useState("");

  const priorities = useMemo(() => {
    const set = new Set(candidates.map((c) => c.priority_level).filter(Boolean));
    return ["all", ...Array.from(set).sort()];
  }, [candidates]);

  const rows = useMemo(() => {
    const needle = filterText.trim().toLowerCase();
    const filtered = candidates.filter((c) => {
      if (priority !== "all" && c.priority_level !== priority) return false;
      if (!needle) return true;
      // Search the editorial fields too, not just the topic — the angle is
      // often what you remember a story by.
      return `${c.topic} ${c.primary_entity} ${c.recommended_angle} ${c.why_now} ${c.primary_headline}`
        .toLowerCase()
        .includes(needle);
    });
    return [...filtered].sort((a, b) => compareValues(a, b, sortKey) * (sortDir === "asc" ? 1 : -1));
  }, [candidates, filterText, priority, sortKey, sortDir]);

  function toggleRow(key) {
    setExpanded((current) => {
      const next = new Set(current);
      if (next.has(key)) next.delete(key);
      else next.add(key);
      return next;
    });
  }

  async function copyBrief(candidate, key) {
    try {
      await navigator.clipboard.writeText(briefText(candidate));
      setCopied(key);
      setTimeout(() => setCopied(""), 2000);
    } catch {
      setCopied("");
    }
  }

  if (!candidates.length) {
    return <p className="emptyState">This run retained no topics.</p>;
  }

  return (
    <>
      <TableControls
        filterText={filterText}
        onFilterText={setFilterText}
        filterPlaceholder="Filter by topic, angle, headline…"
        groupValue={priority}
        onGroupValue={setPriority}
        groupOptions={priorities}
        groupAllLabel="All priorities"
        sortKey={sortKey}
        onSortKey={setSortKey}
        sortOptions={SORT_OPTIONS}
        sortDir={sortDir}
        onToggleSortDir={() => setSortDir((dir) => (dir === "asc" ? "desc" : "asc"))}
      />
      <div className="boardList">
        {rows.map((candidate, index) => {
          const key = `${candidate.topic}-${index}`;
          const isOpen = expanded.has(key);
          const days = recurrence[candidate.topic] || 1;
          const flagged = `${candidate.notes || ""}`.trim();
          return (
            <article
              key={key}
              className={`boardCard ${priorityTone(candidate.priority_level)}`}
            >
              <button
                type="button"
                className="boardCardHead"
                onClick={() => toggleRow(key)}
                aria-expanded={isOpen}
              >
                <span className="boardCardMain">
                  <span className="boardCardTitle">
                    <span className="chevron">{isOpen ? "▾" : "▸"}</span>
                    {candidate.topic}
                  </span>
                  <span className="boardCardMeta">
                    {badge(candidate.priority_level)}
                    {badge(candidate.publish_timing)}
                    {badge(candidate.confidence)}
                    {candidate.primary_entity ? <span className="quiet">{candidate.primary_entity}</span> : null}
                    {days > 1 ? (
                      <span className="badge warm" title="Consecutive runs carrying this story">
                        day {days}
                      </span>
                    ) : null}
                    {flagged ? <span className="badge risk" title={flagged}>⚠ flagged</span> : null}
                  </span>
                </span>
                <span className="boardCardScores">
                  <span title="Trend strength">
                    <b>{candidate.trend_strength_score || "—"}</b>
                    {scoreBar(candidate.trend_strength_score, "red")}
                  </span>
                  <span title="Opportunity">
                    <b>{candidate.opportunity_score || "—"}</b>
                    {scoreBar(candidate.opportunity_score, "blue")}
                  </span>
                  <span className="discover" title="Discover score (1–5)">
                    D{candidate.discover_score || "—"}
                  </span>
                </span>
              </button>
              {isOpen ? (
                <div className="boardCardBody">
                  {DETAIL_FIELDS.map((field) => {
                    const value = `${candidate[field.key] || ""}`.trim();
                    if (!value) return null;
                    return (
                      <div className="detailField" key={field.key}>
                        <span className="detailLabel">{field.label}</span>
                        <p className="detailBody">{value}</p>
                      </div>
                    );
                  })}
                  {flagged ? (
                    <div className="integrityNote">
                      <span className="detailLabel">⚠️ Integrity note</span>
                      <p className="detailBody">{flagged}</p>
                    </div>
                  ) : null}
                  <div className="detailActions">
                    <button
                      type="button"
                      className="button"
                      onClick={() => copyBrief(candidate, key)}
                    >
                      {copied === key ? "Copied!" : "Copy brief"}
                    </button>
                    <span className="quiet">
                      {candidate.source_count ? `${candidate.source_count} sources` : "source count unavailable"}
                    </span>
                  </div>
                </div>
              ) : null}
            </article>
          );
        })}
      </div>
      <p className="resultCount">
        {rows.length} of {candidates.length} topics shown
      </p>
    </>
  );
}
