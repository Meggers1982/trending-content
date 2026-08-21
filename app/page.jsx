import { getLatestRun, getReportText, getRunSummary, getSignalText, listRuns } from "@/lib/runs";
import { getLatestRadarScanData } from "@/lib/radar";
import { scoreBar, badge, stageBadge, tagChips } from "@/lib/dashboard-ui";
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
    // The article URL follows its headline on an indented "URL: ..." line
    // (see build_serp_context() in run_pipeline.py). Signal files written
    // before that line existed simply leave the headline unlinked.
    const url = line.match(/^\s+URL:\s+(https?:\/\/\S+)/);
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

export default function Home() {
  const runs = listRuns();
  const latest = getLatestRun();
  const summary = getRunSummary(latest);
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
          <div className="runmeta">
            <span>Latest run</span>
            <strong>{latest?.date || "No run found"}</strong>
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
              {latest?.hasDashboard ? (
                <a className="button primary" href={`/api/artifact/${latest.dashboardPath}`} target="_blank">
                  Open Dashboard
                </a>
              ) : null}
              {latest?.hasReport ? (
                <a className="button" href={`/api/artifact/${latest.reportPath}`} target="_blank">
                  Full Report
                </a>
              ) : null}
            </div>
          </div>
          <div className="opsPanel" id="ops">
            <RunControls />
          </div>
        </section>

        <section className="metrics">
          <article>
            <span>Retained</span>
            <strong>{summary.retained}</strong>
            <p>topics on board</p>
          </article>
          <article>
            <span>Publish Now</span>
            <strong>{summary.immediate}</strong>
            <p>P1 candidates</p>
          </article>
          <article>
            <span>High Confidence</span>
            <strong>{summary.highConfidence}</strong>
            <p>verified signal quality</p>
          </article>
          <article>
            <span>Integrity Flags</span>
            <strong>{summary.flags}</strong>
            <p>need review</p>
          </article>
        </section>

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
          </div>
          <div className="tableWrap">
            <table>
              <thead>
                <tr>
                  <th>Priority</th>
                  <th>Topic</th>
                  <th>Trend</th>
                  <th>Opp</th>
                  <th>Discover</th>
                  <th>Timing</th>
                  <th>Confidence</th>
                  <th>Sources</th>
                </tr>
              </thead>
              <tbody>
                {candidates.map((candidate, index) => (
                  <tr key={`${candidate.topic}-${index}`}>
                    <td>{badge(candidate.priority_level)}</td>
                    <td>
                      <strong>{candidate.topic}</strong>
                      <span>{candidate.primary_entity}</span>
                    </td>
                    <td>
                      <b>{candidate.trend_strength_score}</b>
                      {scoreBar(candidate.trend_strength_score, "red")}
                    </td>
                    <td>
                      <b>{candidate.opportunity_score}</b>
                      {scoreBar(candidate.opportunity_score, "blue")}
                    </td>
                    <td>{badge(candidate.discover_score)}</td>
                    <td>{badge(candidate.publish_timing)}</td>
                    <td>{badge(candidate.confidence)}</td>
                    <td>{candidate.source_count || "—"}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </section>

        <section className="board" id="keywords">
          <div className="sectionTitle">
            <div>
              <p className="eyebrow">Ad-hoc Research</p>
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
            {runs.map((run) => (
              <article key={run.date}>
                <strong>{run.date}</strong>
                <span>{run.candidateCount} retained</span>
                <div>
                  {run.hasDashboard ? <a href={`/api/artifact/${run.dashboardPath}`} target="_blank">Dashboard</a> : null}
                  {run.hasReport ? <a href={`/api/artifact/${run.reportPath}`} target="_blank">Report</a> : null}
                  {run.hasSignals ? <a href={`/api/artifact/${run.signalPath}`} target="_blank">Signals</a> : null}
                </div>
              </article>
            ))}
          </div>
        </section>

        <section className="scanSection" id="scan">
          <div className="sectionTitle">
            <div>
              <p className="eyebrow">Ad-hoc Research</p>
              <h2>Trend scanner</h2>
            </div>
          </div>
          <RadarScan />
        </section>

        <section className="scanSection" id="tracked">
          <div className="sectionTitle">
            <div>
              <p className="eyebrow">Ad-hoc Research</p>
              <h2>Tracked topics</h2>
            </div>
          </div>
          <TrackedTopics />
        </section>
      </section>
    </main>
  );
}
