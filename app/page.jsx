import {
  getRecurrence,
  getRejectionTrends,
  getReportText,
  getRunAgeDays,
  getRunSummary,
  getRunTrend,
  getSignalText,
  listRuns
} from "@/lib/runs";
import { getLatestRadarScanData } from "@/lib/radar";
import { scoreBar, stageBadge, tagChips } from "@/lib/dashboard-ui";
import PriorityBoard from "./components/PriorityBoard";
import RunControls from "./components/RunControls";
import RadarScan from "./components/RadarScan";
import TrackedTopics from "./components/TrackedTopics";

function inlineParts(text) {
  const parts = `${text || ""}`.split(/(\*\*[^*]+\*\*|`[^`]+`|\[[^\]]+\]\([^)]+\))/g).filter(Boolean);
  return parts.map((part, index) => {
    if (part.startsWith("**") && part.endsWith("**")) {
      return <strong key={index}>{part.slice(2, -2)}</strong>;
    }
    if (part.startsWith("`") && part.endsWith("`")) {
      return <code key={index}>{part.slice(1, -1)}</code>;
    }
    const linkMatch = part.match(/^\[([^\]]+)\]\(([^)]+)\)$/);
    if (linkMatch) {
      const [, label, url] = linkMatch;
      // Claude writes this markdown itself (not raw external API data), but
      // validate the scheme anyway rather than trusting it into an href.
      if (/^https?:\/\//i.test(url)) {
        return (
          <a key={index} href={url} target="_blank" rel="noopener noreferrer">
            {label}
          </a>
        );
      }
      return <span key={index}>{label}</span>;
    }
    return <span key={index}>{part}</span>;
  });
}

function parseReportSections(text) {
  const sections = [];
  let current = null;

  for (const line of `${text || ""}`.split("\n")) {
    const match = line.match(/^##\s+(.+)/);
    if (match) {
      current = { title: match[1].trim(), lines: [] };
      sections.push(current);
    } else if (current) {
      current.lines.push(line);
    }
  }

  return sections;
}

function parseTable(lines, start) {
  const tableLines = [];
  let index = start;
  while (index < lines.length && lines[index].trim().startsWith("|")) {
    tableLines.push(lines[index].trim());
    index += 1;
  }

  const rows = tableLines
    .filter((line) => !/^\|\s*:?-{3,}/.test(line))
    .map((line) => line.slice(1, -1).split("|").map((cell) => cell.trim()));

  return { rows, next: index };
}

function parseMetadata(lines) {
  const items = [];
  for (const line of lines) {
    const cleaned = line.trim().replace(/^-\s+/, "");
    const match = cleaned.match(/^([^:]+):\s*(.+)?$/);
    if (match && !cleaned.endsWith(">")) {
      items.push({ key: match[1].trim(), value: match[2]?.trim() || "—" });
    }
  }
  return items;
}

function ReportSection({ section }) {
  const blocks = [];
  let index = 0;

  while (index < section.lines.length) {
    const line = section.lines[index];
    const trimmed = line.trim();

    if (!trimmed || trimmed === "---") {
      index += 1;
      continue;
    }

    if (trimmed.startsWith("|")) {
      const table = parseTable(section.lines, index);
      blocks.push({ type: "table", rows: table.rows });
      index = table.next;
      continue;
    }

    if (trimmed.startsWith("```")) {
      const code = [];
      index += 1;
      while (index < section.lines.length && !section.lines[index].trim().startsWith("```")) {
        code.push(section.lines[index]);
        index += 1;
      }
      blocks.push({ type: "metadata", items: parseMetadata(code) });
      index += 1;
      continue;
    }

    if (trimmed.startsWith("- ")) {
      const items = [];
      while (index < section.lines.length && section.lines[index].trim().startsWith("- ")) {
        items.push(section.lines[index].trim().slice(2));
        index += 1;
      }
      blocks.push({ type: "list", items });
      continue;
    }

    blocks.push({ type: "paragraph", text: trimmed });
    index += 1;
  }

  return (
    <article className="reportSection">
      <h3>{section.title}</h3>
      {blocks.map((block, blockIndex) => {
        if (block.type === "table") {
          const [head = [], ...body] = block.rows;
          return (
            <div className="miniTableWrap" key={blockIndex}>
              <table className="miniTable">
                <thead>
                  <tr>{head.map((cell, cellIndex) => <th key={cellIndex}>{inlineParts(cell)}</th>)}</tr>
                </thead>
                <tbody>
                  {body.map((row, rowIndex) => (
                    <tr key={rowIndex}>
                      {row.map((cell, cellIndex) => <td key={cellIndex}>{inlineParts(cell)}</td>)}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          );
        }

        if (block.type === "metadata") {
          return (
            <dl className="metadataGrid" key={blockIndex}>
              {block.items.map((item) => (
                <div key={`${item.key}-${item.value}`}>
                  <dt>{item.key}</dt>
                  <dd>{inlineParts(item.value)}</dd>
                </div>
              ))}
            </dl>
          );
        }

        if (block.type === "list") {
          return (
            <ul className="cleanList" key={blockIndex}>
              {block.items.map((item) => <li key={item}>{inlineParts(item)}</li>)}
            </ul>
          );
        }

        return <p key={blockIndex}>{inlineParts(block.text)}</p>;
      })}
    </article>
  );
}

// The signal file uses "## Section Title" headers (see build_serp_context()
// in run_pipeline.py); splitting on those first lets us tell apart the fixed
// seed-category depth readings from the actual discovered rising/trending
// terms, which live in different sections but share the same "  - text"
// bullet format.
function splitSignalSections(text) {
  const sections = {};
  let current = null;
  for (const line of `${text || ""}`.split("\n")) {
    const match = line.match(/^##\s+(.+)/);
    if (match) {
      current = match[1].trim();
      sections[current] = [];
    } else if (current) {
      sections[current].push(line);
    }
  }
  return sections;
}

function bulletLines(lines) {
  return lines
    .map((line) => line.match(/^\s+-\s+(.+)/))
    .filter(Boolean)
    .map((match) => match[1].trim());
}

function parseSignalRadar(text) {
  const sections = splitSignalSections(text);
  const sectionKeys = Object.keys(sections);

  const trendingNowKey = sectionKeys.find((k) => k.startsWith("Google Trends — Trending Now"));
  const trendingNow = trendingNowKey ? bulletLines(sections[trendingNowKey]).slice(0, 12) : [];

  const interestKey = sectionKeys.find((k) => k.startsWith("Google Trends — 7-Day Interest"));
  const interestLines = interestKey ? sections[interestKey] : [];

  const risingIndex = interestLines.findIndex((line) => line.includes("Top rising related queries"));
  const risingSearches = risingIndex >= 0 ? bulletLines(interestLines.slice(risingIndex + 1)).slice(0, 20) : [];

  const newsKey = sectionKeys.find((k) => k.startsWith("Google News Radar"));
  const newsLines = newsKey ? sections[newsKey] : [];
  const newsRows = [];
  for (const line of newsLines) {
    const news = line.match(/^\s+-\s+\((.+?)\)\s+\[(.+?)\]\s+(.+?)\s+—\s+(.+)/);
    if (news) {
      newsRows.push({ query: news[1], source: news[2], date: news[3], title: news[4], url: "" });
      continue;
    }
    // The article URL follows its headline on an indented "Link: ..." line
    // (see build_serp_context() in run_pipeline.py). Signal files written
    // before that line existed — and articles SerpAPI returned without a link,
    // which write "Link: not available" — leave the headline unlinked.
    const url = line.match(/^\s+Link:\s+(https?:\/\/\S+)/);
    if (url && newsRows.length) {
      newsRows[newsRows.length - 1].url = url[1];
    }
  }

  return {
    trendingNow,
    risingSearches,
    newsRows: newsRows.slice(0, 18)
  };
}

function RadarDashboard({ text }) {
  const { trendingNow, risingSearches, newsRows } = parseSignalRadar(text);
  const hasRising = trendingNow.length > 0 || risingSearches.length > 0;
  return (
    <section className="radarDashboard" id="radar">
      <article className="panel formattedPanel risingPanel">
        <div className="panelHeader">
          <span>Rising Searches</span>
          <strong>{hasRising ? "discovered today" : "Missing"}</strong>
        </div>
        {hasRising ? (
          <>
            {trendingNow.length ? (
              <>
                <h4>Trending Now (real-time)</h4>
                <div className="chipGroup">
                  {trendingNow.map((term) => <span className="chip" key={term}>{term}</span>)}
                </div>
              </>
            ) : null}
            {risingSearches.length ? (
              <>
                <h4>Rising Related Searches</h4>
                <div className="chipGroup">
                  {risingSearches.map((term) => <span className="chip" key={term}>{term}</span>)}
                </div>
              </>
            ) : null}
          </>
        ) : (
          <p>
            No rising-query data in today's signal file yet. This needs{" "}
            <code>SERPAPI_TRENDING_NOW_ENABLED=true</code> (for real-time terms) and a run with
            SerpAPI configured.
          </p>
        )}
      </article>
      <article className="panel formattedPanel">
        <div className="panelHeader">
          <span>Google News Radar</span>
          <strong>{newsRows.length ? `${newsRows.length} shown` : "Missing"}</strong>
        </div>
        <div className="newsList">
          {newsRows.map((item, index) => (
            <div className="newsItem" key={`${item.title}-${index}`}>
              <span>{item.query}</span>
              <strong>
                {item.url ? (
                  <a href={item.url} target="_blank" rel="noopener noreferrer">{item.title}</a>
                ) : (
                  item.title
                )}
              </strong>
              <p>{item.source} · {item.date}</p>
            </div>
          ))}
        </div>
      </article>
    </section>
  );
}

export default async function Home({ searchParams }) {
  const runs = listRuns();
  // ?run=YYYY-MM-DD browses a past run; everything on the page reflects the
  // selected one, so history is readable in-app instead of as raw artifacts.
  const params = await searchParams;
  const requestedDate = typeof params?.run === "string" ? params.run : "";
  const latest = runs.find((run) => run.date === requestedDate) || runs[0] || null;
  const isViewingPast = Boolean(latest) && latest.date !== runs[0]?.date;
  const ageDays = getRunAgeDays(latest);
  const summary = getRunSummary(latest);
  const recurrence = getRecurrence(runs, latest);
  const trend = getRunTrend(runs);
  const rejectionTrends = getRejectionTrends(runs);
  const signals = getSignalText(latest);
  const report = getReportText(latest);
  const reportSections = parseReportSections(report).filter((section) =>
    ["PREFLIGHT SUMMARY", "GOOGLE NEWS RADAR COVERAGE SUMMARY", "SIGNAL SUMMARY", "SKILL 02b ROUTING SUMMARY"].includes(section.title)
  );
  const candidates = latest?.candidates || [];
  const radarScan = getLatestRadarScanData();
  const radarCandidates = radarScan?.candidates || [];
  const radarBreakouts = radarScan?.trending_now_context || [];
  // Candidates traced back to a Trending Now term with a confirmed news
  // story (i.e. present in trending_now_context) are a stronger signal
  // than a bare Google Trends spike - flag them in the table below.
  const groundedSeeds = new Set(radarBreakouts.map((b) => String(b.query || "").toLowerCase().trim()));
  const isGrounded = (seedTerms) =>
    (Array.isArray(seedTerms) ? seedTerms : []).some((s) => groundedSeeds.has(String(s).toLowerCase().trim()));

  return (
    <main id="top">
      <a href="#top" className="scrollTop" aria-label="Scroll to top">
        &uarr;
      </a>
      <aside className="rail">
        <div className="brandmark">
          <span />
          <span />
          <span />
          <span />
        </div>
        <nav>
          <a href="#radar">Radar</a>
          <a href="#board">Board</a>
          <a href="#keywords">Keywords</a>
          <a href="#runs">Runs</a>
          <a href="#ops">Ops</a>
          <a href="#scan">Scan</a>
          <a href="#tracked">Tracked</a>
        </nav>
      </aside>

      <section className="shell">
        <header className="topline">
          <div>
            <p className="eyebrow">Health & Wellness Editorial Intelligence</p>
            <h1>Trending Content OS</h1>
          </div>
          <div className={`runmeta ${ageDays !== null && ageDays > 1 && !isViewingPast ? "stale" : ""}`}>
            <span>{isViewingPast ? "Viewing past run" : "Latest run"}</span>
            <strong>{latest?.date || "No run found"}</strong>
            {latest ? (
              <em>
                {ageDays === 0 ? "today" : ageDays === 1 ? "yesterday" : `${ageDays} days old`}
                {summary.toolsUnavailable.length
                  ? ` · ${summary.toolsUnavailable.length} tool${summary.toolsUnavailable.length > 1 ? "s" : ""} unavailable`
                  : ""}
                {latest.cost?.total_usd ? ` · $${latest.cost.total_usd.toFixed(2)} to run` : ""}
              </em>
            ) : null}
          </div>
        </header>

        <section className="hero">
          <div className="heroCopy">
            <p className="kicker">Google News + Trends Radar</p>
            <h2>Scan demand, route risk, and pick the next health story from one interface.</h2>
            <p>
              This Vercel-ready app reads the pipeline artifacts already generated by
              Trending Content OS and turns them into an editorial command center.
            </p>
            <div className="actions">
              {isViewingPast ? (
                <a className="button primary" href="/">
                  ← Back to latest run
                </a>
              ) : null}
              {latest?.hasReport ? (
                <a className="button" href={`/api/artifact/${latest.reportPath}`} target="_blank">
                  Full Report
                </a>
              ) : null}
              {latest?.hasDashboard ? (
                <a className="button" href={`/api/artifact/${latest.dashboardPath}`} target="_blank">
                  Download snapshot
                </a>
              ) : null}
            </div>
          </div>
          <div className="opsPanel" id="ops">
            <RunControls />
          </div>
        </section>

        {/* The funnel, stated plainly: what was looked at, what survived, what
            was cut. The reviewed and rejected counts come from the run's
            extraction JSON and were invisible before. */}
        <section className="metrics">
          <article>
            <span>Signals Reviewed</span>
            <strong>{summary.reviewed || "—"}</strong>
            <p>{summary.reviewed ? "before filtering" : "not recorded for this run"}</p>
          </article>
          <article>
            <span>Retained</span>
            <strong>{summary.retained}</strong>
            <p>
              {summary.reviewed
                ? `${Math.round((summary.retained / summary.reviewed) * 100)}% of reviewed`
                : "topics on board"}
            </p>
          </article>
          <article>
            <span>Rejected</span>
            <strong>{summary.rejected || summary.rejectedItemized || "—"}</strong>
            <p>
              {summary.rejectedItemized
                ? `${summary.rejectedItemized} itemized below`
                : "none itemized"}
            </p>
          </article>
          <article>
            <span>Publish Now</span>
            <strong>{summary.immediate}</strong>
            <p>P1 · {summary.highConfidence} high confidence</p>
          </article>
        </section>

        {trend.length > 1 ? (
          <section className="trendStrip" aria-label="Signals reviewed and retained per run">
            {trend.map((point) => {
              const peak = Math.max(...trend.map((p) => p.reviewed), 1);
              return (
                <div className="trendCol" key={point.date} title={`${point.date}: ${point.reviewed} reviewed, ${point.retained} retained`}>
                  <div className="trendBar" style={{ height: `${Math.round((point.reviewed / peak) * 100)}%` }}>
                    <div
                      className="trendKept"
                      style={{ height: `${Math.round((point.retained / Math.max(point.reviewed, 1)) * 100)}%` }}
                    />
                  </div>
                  <span>{point.date.slice(5)}</span>
                </div>
              );
            })}
          </section>
        ) : null}

        {latest?.factCheck ? (
          <section className="factCheckBar">
            <span className="detailLabel">Fact check</span>
            {[
              ["accurate", "verified", "good"],
              ["minor_issues", "minor issues", "warm"],
              ["significant_issues", "check before writing", "risk"],
              ["unverifiable", "unverified", ""]
            ]
              .filter(([key]) => latest.factCheck[key])
              .map(([key, label, tone]) => (
                <span key={key}>
                  <span className={`badge ${tone}`}>{latest.factCheck[key]}</span> {label}
                </span>
              ))}
            <span className="quiet">
              Each retained topic checked against the evidence this run collected.
            </span>
          </section>
        ) : null}

        {summary.notes ? (
          <section className="insightPanel">
            <p className="eyebrow">Run Insight</p>
            <p>{summary.notes}</p>
          </section>
        ) : null}

        <RadarDashboard text={signals} />

        <details className="formattedReport">
          <summary className="sectionTitle">
            <div>
              <p className="eyebrow">Formatted Report</p>
              <h2>Run decisions and safety routing</h2>
            </div>
          </summary>
          <div className="reportGrid">
            {reportSections.length ? (
              reportSections.map((section) => <ReportSection key={section.title} section={section} />)
            ) : (
              <article className="reportSection">
                <h3>No report found</h3>
                <p>Run the pipeline to generate a formatted report.</p>
              </article>
            )}
          </div>
        </details>

        <section className="board" id="board">
          <div className="sectionTitle">
            <div>
              <p className="eyebrow">Priority Board</p>
              <h2>{candidates.length} retained topics</h2>
            </div>
            <p className="quiet">Click a topic to see the angle, the headline, and why it matters now.</p>
          </div>
          <PriorityBoard candidates={candidates} recurrence={recurrence} />

          {latest?.rejected?.length ? (
            <details className="rejectedPanel">
              <summary>
                <strong>{latest.rejected.length} rejected topics</strong>
                <span className="quiet">
                  {summary.rejected > latest.rejected.length
                    ? ` — itemized from ${summary.rejected} filtered out`
                    : " — what the filter cut, and why"}
                </span>
              </summary>
              <div className="rejectedGroups">
                {Object.entries(
                  latest.rejected.reduce((groups, item) => {
                    const reason = `${item.reason || "unspecified"}`.trim() || "unspecified";
                    (groups[reason] ||= []).push(item.topic);
                    return groups;
                  }, {})
                )
                  .sort((a, b) => b[1].length - a[1].length)
                  .map(([reason, topics]) => (
                    <div className="rejectedGroup" key={reason}>
                      <p className="detailLabel">
                        {reason} <span className="quiet">({topics.length})</span>
                      </p>
                      <ul className="cleanList">
                        {topics.map((topic, index) => (
                          <li key={`${topic}-${index}`}>{topic}</li>
                        ))}
                      </ul>
                    </div>
                  ))}
              </div>
            </details>
          ) : null}

          {/* Cross-run, not per-run: the reject log is only useful as feedback
              once you can see which reason dominates and which is growing. */}
          {rejectionTrends ? (
            <details className="rejectedPanel">
              <summary>
                <strong>Why topics get cut</strong>
                <span className="quiet">
                  {" "}— {rejectionTrends.total} rejections across {rejectionTrends.runs} runs
                </span>
              </summary>
              <div className="reasonList">
                {rejectionTrends.reasons.map((item) => {
                  const direction =
                    item.delta > 0.5 ? "rising" : item.delta < -0.5 ? "falling" : "";
                  return (
                    <div className="reasonRow" key={item.reason}>
                      <div className="reasonHead">
                        <strong className={item.isRollup ? "quiet" : ""}>{item.reason}</strong>
                        <span className="reasonCount">
                          {item.count}
                          <em>{item.share}%</em>
                        </span>
                      </div>
                      <span className="scorebar">
                        <span className="scorefill blue" style={{ width: `${item.share}%` }} />
                      </span>
                      <p className="reasonNote">
                        {direction ? (
                          <span className={`badge ${direction === "rising" ? "warm" : "good"}`}>
                            {direction}
                          </span>
                        ) : null}
                        {item.implication}
                      </p>
                    </div>
                  );
                })}
              </div>
              <p className="quiet">
                Trend compares the last {rejectionTrends.recentRuns} runs against the{" "}
                {rejectionTrends.priorRuns} before them, per run.
              </p>
            </details>
          ) : null}
        </section>

        <section className="board" id="keywords">
          <div className="sectionTitle">
            <div>
              <p className="eyebrow">Latest Scan</p>
              <h2>Trending keywords{radarScan?.topic ? ` — ${radarScan.topic}` : ""}</h2>
            </div>
          </div>
          {radarCandidates.length ? (
            <>
              <p style={{ color: "var(--muted)", fontSize: 13, marginBottom: 10 }}>
                From the most recent Trend Scanner run ({radarScan.geo || "US"} · {radarScan.date_window || ""} ·{" "}
                {radarScan.run_date || ""}). Plain trending topics/keywords, not synthesized content ideas — no
                Anthropic API cost.{" "}
                {radarScan.htmlPath ? (
                  <a href={`/api/radar-artifact/${radarScan.htmlPath}`} target="_blank" rel="noreferrer">
                    Open full scan
                  </a>
                ) : null}
              </p>
              {radarBreakouts.length ? (
                <div className="breakouts">
                  <p className="eyebrow" style={{ marginBottom: 6 }}>Real-Time Breakouts — Why Now</p>
                  {radarBreakouts.map((b, index) => {
                    const safeLink = /^https?:\/\//i.test(b.link || "") ? b.link : null;
                    return (
                      <div className="breakoutCard" key={`${b.query}-${index}`}>
                        <span className="term">{b.query}</span>
                        <div className="headline">
                          {safeLink ? (
                            <a href={safeLink} target="_blank" rel="noopener noreferrer">
                              {b.headline}
                            </a>
                          ) : (
                            b.headline
                          )}
                          {b.source ? <span className="source"> — {b.source}</span> : null}
                        </div>
                      </div>
                    );
                  })}
                </div>
              ) : null}
              <div className="tableWrap">
                <table>
                  <thead>
                    <tr>
                      <th>Stage</th>
                      <th>Keyword</th>
                      <th>Radar</th>
                      <th>Opportunity</th>
                      <th>Tags</th>
                    </tr>
                  </thead>
                  <tbody>
                    {radarCandidates.slice(0, 25).map((candidate, index) => (
                      <tr key={`${candidate.topic}-${index}`}>
                        <td>{stageBadge(candidate.trend_stage)}</td>
                        <td>
                          <strong>{candidate.topic}</strong>
                          {isGrounded(candidate.seed_terms) ? (
                            <span
                              className="sourcedBadge"
                              title="Traced to a Trending Now term with a confirmed news story"
                            >
                              Sourced
                            </span>
                          ) : null}
                          <span>{candidate.why_now}</span>
                          {candidate.similar?.length ? (
                            <details className="similarToggle">
                              <summary>
                                +{candidate.similar.length} similar phrasing{candidate.similar.length > 1 ? "s" : ""}
                              </summary>
                              <ul className="similarList">
                                {candidate.similar.map((s, sIndex) => (
                                  <li key={`${s.topic}-${sIndex}`}>
                                    {stageBadge(s.trend_stage)} {s.topic} <b>{s.radar_score}</b>
                                  </li>
                                ))}
                              </ul>
                            </details>
                          ) : null}
                        </td>
                        <td>
                          <b>{candidate.radar_score}</b>
                          {scoreBar(candidate.radar_score, "red")}
                        </td>
                        <td>
                          <b>{candidate.opportunity_score}</b>
                          {scoreBar(candidate.opportunity_score, "blue")}
                        </td>
                        <td>{tagChips(candidate.tags)}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </>
          ) : (
            <p>
              No scan has been run yet. Head to the <a href="#scan">Trend scanner</a> below, pick a topic/profile,
              and click Scan — results will show up here automatically on the next page load.
            </p>
          )}
        </section>

        <section className="runs" id="runs">
          <div className="sectionTitle">
            <div>
              <p className="eyebrow">History</p>
              <h2>Generated runs</h2>
            </div>
          </div>
          <div className="runList">
            {runs.map((run) => {
              const active = run.date === latest?.date;
              return (
                <article key={run.date} className={active ? "activeRun" : ""}>
                  {/* Selecting a run re-renders the whole page against it, so
                      past runs are browsable in-app rather than as raw files. */}
                  <a className="runPick" href={run.date === runs[0]?.date ? "/#board" : `/?run=${run.date}#board`}>
                    <strong>{run.date}</strong>
                    <span>
                      {run.summary?.total_reviewed
                        ? `${run.summary.total_reviewed} reviewed · ${run.candidateCount} retained`
                        : `${run.candidateCount} retained`}
                    </span>
                  </a>
                  <div>
                    {active ? <span className="badge good">viewing</span> : null}
                    {run.hasDashboard ? <a href={`/api/artifact/${run.dashboardPath}`} target="_blank">Snapshot</a> : null}
                    {run.hasReport ? <a href={`/api/artifact/${run.reportPath}`} target="_blank">Report</a> : null}
                    {run.hasSignals ? <a href={`/api/artifact/${run.signalPath}`} target="_blank">Signals</a> : null}
                  </div>
                </article>
              );
            })}
          </div>
        </section>

        <section className="scanSection" id="scan">
          <div className="sectionTitle">
            <div>
              <p className="eyebrow">Run a Scan</p>
              <h2>Trend scanner</h2>
            </div>
          </div>
          <RadarScan />
        </section>

        <section className="scanSection" id="tracked">
          <div className="sectionTitle">
            <div>
              <p className="eyebrow">Saved &amp; Scheduled</p>
              <h2>Tracked topics</h2>
            </div>
          </div>
          <TrackedTopics />
        </section>
      </section>
    </main>
  );
}
