"use client";

// Filter + sort controls shared by the Priority Board and the Trend Scanner
// results table. Extracted from RadarResultsTable, which had the only copy.
export default function TableControls({
  filterText,
  onFilterText,
  filterPlaceholder = "Filter…",
  groupValue,
  onGroupValue,
  groupOptions = [],
  groupAllLabel = "All",
  sortKey,
  onSortKey,
  sortOptions = [],
  sortDir,
  onToggleSortDir,
  children
}) {
  return (
    <div className="tableControls">
      <input
        type="text"
        value={filterText}
        onChange={(event) => onFilterText(event.target.value)}
        placeholder={filterPlaceholder}
      />
      {groupOptions.length ? (
        <select value={groupValue} onChange={(event) => onGroupValue(event.target.value)}>
          {groupOptions.map((option) => (
            <option key={option} value={option}>
              {option === "all" ? groupAllLabel : option}
            </option>
          ))}
        </select>
      ) : null}
      <select value={sortKey} onChange={(event) => onSortKey(event.target.value)}>
        {sortOptions.map((option) => (
          <option key={option.key} value={option.key}>Sort: {option.label}</option>
        ))}
      </select>
      <button type="button" className="button" onClick={onToggleSortDir}>
        {sortDir === "asc" ? "↑ Asc" : "↓ Desc"}
      </button>
      {children}
    </div>
  );
}
