import { getLatestRun, getReportText, getRunSummary, getSignalText, listRuns } from "@/lib/runs";
import RunControls from "./components/RunControls";
import RadarScan from "./components/RadarScan";

function scoreBar(value, tone = "red") {
  const width = Math.max(0, Math.min(100, Number(value) || 0));
  return (
    <span className="scorebar">
      <span className={`scorefill ${tone}`} style={{ width: `${width}%` }} />
    </span>
  );
}

function badge(value) {
  const normalized = `${value || ""}`.toLowerCase();
  let className = "badge";
  if (normalized.includes("p1") || normalized.includes("now") || normalized.includes("immediate")) className += " hot";
  if (normalized.includes("p2") || normalized.includes("short")) className += " warm";
  if (normalized.includes("high") || normalized.includes("easy")) className += " good";
  if (normalized.includes("medium")) className += " mid";
  if (normalized.includes("low") || normalized.includes("hard")) className += " risk";
  return <span className={className}>{value || "—"}</span>;
}

function inlineParts(text) {
  const parts = `${text || ""}`.split(/(\*\*[^*]+\*\*|`[^`]+`)/g).filter(Boolean);
  return parts.map((part, index) => {
    if (part.startsWith("**") && part.endsWith("**")) {
      return <strong key={index}>{part.slice(2, -2)}</strong>;
    }
    if (part.startsWith("`") && part.endsWith("`")) {
      return <code key={index}>{part.slice(1, -1)}</code>;
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

function parseSignalRadar(text) {
  const trendRows = [];
  const newsRows = [];

  for (const line of `${text || ""}`.split("\n")) {
    const trend = line.match(/^\s+-\s+\*\*(.+?)\*\*:\s+latest=(\d+),\s+peak=(\d+),\s+7d-delta=([+-]?\d+)/);
    if (trend) {
      trendRows.push({
        keyword: trend[1],
        latest: trend[2],
        peak: trend[3],
        delta: trend[4]
      });
      continue;
    }

    const news = line.match(/^\s+-\s+\((.+?)\)\s+\[(.+?)\]\s+(.+?)\s+—\s+(.+)/);
    if (news) {
      newsRows.push({
        query: news[1],
        source: news[2],
        date: news[3],
        title: news[4]
      });
    }
  }

  return { trendRows: trendRows.slice(0, 9), newsRows: newsRows.slice(0, 18) };
}

function RadarDashboard({ text }) {
  const { trendRows, newsRows } = parseSignalRadar(text);
  return (
    <section className="radarDashboard" id="radar">
      <article className="panel formattedPanel">
        <div className="panelHeader">
          <span>Google Trends</span>
          <strong>{trendRows.length ? "7-day interest" : "Missing"}</strong>
        </div>
        <div className="trendGrid">
          {trendRows.map((trend) => (
            <div className="trendCard" key={trend.keyword}>
              <div>
                <strong>{trend.keyword}</strong>
                <span>Peak {trend.peak}</span>
              </div>
              <b>{trend.latest}</b>
              <em className={Number(trend.delta) >= 0 ? "up" : "down"}>{Number(trend.delta) >= 0 ? "+" : ""}{trend.delta}</em>
            </div>
          ))}
        </div>
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
              <strong>{item.title}</strong>
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

  return (
    <main>
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
          <a href="#runs">Runs</a>
          <a href="#ops">Ops</a>
          <a href="#scan">Scan</a>
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

        <section className="formattedReport">
          <div className="sectionTitle">
            <div>
              <p className="eyebrow">Formatted Report</p>
              <h2>Run decisions and safety routing</h2>
            </div>
          </div>
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
        </section>

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
      </section>
    </main>
  );
}
