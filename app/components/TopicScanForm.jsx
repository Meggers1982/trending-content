"use client";

import { PROFILES } from "@/lib/radar-profiles";

// Shared by the ad-hoc scanner and tracked topics, which asked for the same
// three inputs in two separate unlabelled forms. Fields are sized by how much
// you actually type into them: the topic gets the room, geo is a country code.
export default function TopicScanForm({
  topic,
  onTopic,
  profile,
  onProfile,
  geo,
  onGeo,
  onSubmit,
  submitLabel,
  submitting = false,
  topicPlaceholder = "e.g. “gut health” or “AI tools”",
  topicLabel = "Topic"
}) {
  return (
    <form className="topicScanForm" onSubmit={onSubmit}>
      <label className="fieldTopic">
        <span>{topicLabel}</span>
        <input
          type="text"
          value={topic}
          onChange={(event) => onTopic(event.target.value)}
          placeholder={topicPlaceholder}
          maxLength={100}
          required
        />
      </label>
      <label className="fieldProfile">
        <span>Profile</span>
        <select value={profile} onChange={(event) => onProfile(event.target.value)}>
          {PROFILES.map((option) => (
            <option key={option} value={option}>
              {option === "auto" ? "auto (pick by topic)" : option}
            </option>
          ))}
        </select>
      </label>
      <label className="fieldGeo">
        <span>Geo</span>
        <input
          type="text"
          value={geo}
          onChange={(event) => onGeo(event.target.value)}
          placeholder="US"
          maxLength={5}
        />
      </label>
      <button className="button primary" type="submit" disabled={submitting || !topic.trim()}>
        {submitting ? "Working…" : submitLabel}
      </button>
    </form>
  );
}
