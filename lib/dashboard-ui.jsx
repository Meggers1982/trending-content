export function scoreBar(value, tone = "red") {
  const width = Math.max(0, Math.min(100, Number(value) || 0));
  return (
    <span className="scorebar">
      <span className={`scorefill ${tone}`} style={{ width: `${width}%` }} />
    </span>
  );
}

export function badge(value) {
  const normalized = `${value || ""}`.toLowerCase();
  let className = "badge";
  if (normalized.includes("p1") || normalized.includes("now") || normalized.includes("immediate")) className += " hot";
  if (normalized.includes("p2") || normalized.includes("short")) className += " warm";
  if (normalized.includes("high") || normalized.includes("easy")) className += " good";
  if (normalized.includes("medium")) className += " mid";
  if (normalized.includes("low") || normalized.includes("hard")) className += " risk";
  return <span className={className}>{value || "—"}</span>;
}

export function stageBadge(stage) {
  const tone = { breakout: "hot", emerging: "warm", rising: "good", watch: "" }[stage] || "";
  return <span className={`badge ${tone}`}>{stage || "watch"}</span>;
}

export function tagChips(tags) {
  const entries = tags && typeof tags === "object" ? Object.entries(tags) : [];
  if (!entries.length) return <span>—</span>;
  return entries.map(([tagType, terms]) => (
    <span className="badge" key={tagType} style={{ marginRight: 4, marginBottom: 4 }}>
      {tagType}: {(terms || []).join(", ")}
    </span>
  ));
}
