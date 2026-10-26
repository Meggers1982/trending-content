"""Shared helpers for Trend Desk's Mac jobs (bot.py, builder.py, brief_room.py, outcomes.py).

Local state, which never goes in the public repo, lives in ~/.local/state/trend-desk/:
  built.json       every idea the builder handled: what it made, where, when, attempts
  delivered.json   outbox messages already sent to Telegram, and recent dedupe keys
  offset           Telegram update offset;  thread.json  her last texts and the bot's replies
  edits/           private snapshots for learning from her edits to outlines and briefs
"""
from __future__ import annotations

import json
import os
import re
import subprocess
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

REPO = Path(__file__).resolve().parents[2]
DESK = REPO / "trend_desk"
STATE = Path.home() / ".local/state/trend-desk"
LOGDIR = Path.home() / "Library/Logs/trend-desk"
BUILT = STATE / "built.json"
CLAUDE = str(Path.home() / ".local/bin/claude")
PITCHES = Path.home() / "Pitches"
TFM_DIR = Path.home() / "The Female Model" / "Trend Desk Outlines"
BRIEF_ROOT = Path.home() / "termscope-app" / "termscope-briefs" / "trend-desk"
VAULT = Path.home() / "Meagan's Obsidian"
DECISIONS = DESK / "feedback" / "decisions.json"

# Research Desk (trend_desk/research/) shares this builder but keeps its own handoffs, holds,
# decisions, local state and Telegram bot. builder.py --desk research selects these.
RESEARCH = DESK / "research"
RESEARCH_STATE = Path.home() / ".local/state/research-desk"
# News Desk (trend_desk/news/, Digest Desks MEA-1867): AgingWire and the news digest, same pattern.
NEWS = DESK / "news"
NEWS_STATE = Path.home() / ".local/state/news-desk"
DESKS = {
    "trend": {"name": "Trend Desk", "handoff": DESK / "handoff", "holds": DESK / "holds.json",
              "decisions": DECISIONS, "last_list": STATE / "last_list.json"},
    "research": {"name": "Research Desk", "handoff": RESEARCH / "handoff", "holds": RESEARCH / "holds.json",
                 "decisions": RESEARCH / "feedback" / "decisions.json",
                 "last_list": RESEARCH_STATE / "last_list.json"},
    "news": {"name": "News Desk", "handoff": NEWS / "handoff", "holds": NEWS / "holds.json",
             "decisions": NEWS / "feedback" / "decisions.json",
             "last_list": NEWS_STATE / "last_list.json"},
}


def study_ref(pmid) -> str:
    """How a study is named in messages and tickets: "PMID 42895138", or "OpenAlex W7221827692" for
    the marketing and career digests' studies, which have no PMID."""
    pmid = str(pmid)
    return f"OpenAlex {pmid}" if pmid.startswith("W") else f"PMID {pmid}"


def now() -> datetime:
    return datetime.now(ZoneInfo("America/Chicago"))


def log(msg: str) -> None:
    print(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {msg}", flush=True)


def read_json(path: Path, default):
    try:
        return json.loads(path.read_text())
    except (OSError, json.JSONDecodeError):
        return default


def write_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n")
    tmp.replace(path)


def git(*args, cwd: Path = REPO, check: bool = False) -> subprocess.CompletedProcess:
    p = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)
    if check and p.returncode:
        raise RuntimeError(f"git {' '.join(args)}: {p.stderr.strip()[:300]}")
    return p


def on_main(cwd: Path = REPO) -> bool:
    return git("rev-parse", "--abbrev-ref", "HEAD", cwd=cwd).stdout.strip() == "main"


def pull(cwd: Path = REPO) -> bool:
    """Fast-forward to origin/main. Never merges, rebases or discards anything local."""
    if not on_main(cwd):
        return False
    if git("fetch", "-q", "origin", "main", cwd=cwd).returncode:
        return False
    return git("merge", "-q", "--ff-only", "origin/main", cwd=cwd).returncode == 0


def commit_push(paths: list[str], message: str, cwd: Path = REPO) -> bool:
    """Commit only the named paths and push to main, rebasing over the Actions bot's commits."""
    if not on_main(cwd):
        return False
    git("add", "--", *[p for p in paths if (cwd / p).exists()], cwd=cwd)
    if git("diff", "--cached", "--quiet", cwd=cwd).returncode == 0:
        # Nothing new, but an earlier commit whose push lost a race may still be local only.
        git("fetch", "-q", "origin", "main", cwd=cwd)
        if git("rev-list", "--count", "origin/main..HEAD", cwd=cwd).stdout.strip() in ("", "0"):
            return True
    elif git("commit", "-q", "-m", message, "--", *paths, cwd=cwd).returncode:
        return False
    for _ in range(3):
        if git("pull", "-q", "--rebase", "origin", "main", cwd=cwd).returncode == 0 and \
           git("push", "-q", "origin", "HEAD:main", cwd=cwd).returncode == 0:
            return True
        git("rebase", "--abort", cwd=cwd)
    return False


def claude(prompt: str, tools: str, cwd: Path, timeout: int = 1800, model: str = "opus",
           mcp: bool = False, logname: str = "agent") -> str:
    """Run headless Claude Code on her subscription (no API credit). Returns stdout.
    ANTHROPIC_API_KEY is removed so the claude.ai login, and its connectors, load."""
    env = {k: v for k, v in os.environ.items() if k != "ANTHROPIC_API_KEY"}
    env["PATH"] = f"{Path.home()}/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin"
    cmd = [CLAUDE, "-p", "--model", model, "--output-format", "text", "--allowedTools", tools,
           "--disallowedTools", "Agent,Task,NotebookEdit"]
    if not mcp:
        cmd += ["--strict-mcp-config", "--mcp-config", '{"mcpServers":{}}']
    p = subprocess.run(cmd, input=prompt, cwd=cwd, env=env, capture_output=True, text=True, timeout=timeout)
    LOGDIR.mkdir(parents=True, exist_ok=True)
    with open(LOGDIR / f"{logname}.log", "a") as f:
        f.write(f"\n===== {datetime.now():%Y-%m-%d %H:%M:%S}\n{p.stdout}\n{p.stderr}")
    return p.stdout or ""


def last_json(text: str) -> dict:
    """The last line of an agent's output that is a JSON object."""
    for line in reversed(text.strip().splitlines()):
        line = line.strip()
        if line.startswith("{") and line.endswith("}"):
            try:
                return json.loads(line)
            except json.JSONDecodeError:
                continue
    return {}


LINEAR_TOOLS = ",".join(f"mcp__claude_ai_Linear__{t}" for t in
                        ["list_issues", "save_issue", "get_issue", "list_projects"])


def file_linear(project: str, title: str, description: str, due: str = "") -> str:
    """File (or find) a Linear ticket through the claude.ai Linear connector. Returns its ID or ''.
    The connector's known failure modes are handled the documented way: search first so a retry
    never duplicates, create with a title only, then update, then check the update stuck."""
    prompt = f"""File one Linear ticket, following these steps exactly. Team MEA, project "{project}".

1. Search: list_issues with project "{project}" and query set to the exact title below. If an
   issue with exactly this title exists, use it and skip to step 3.
2. Create it with save_issue: team "MEA", project "{project}", title only.
3. Update it with save_issue (id = that issue) and the description below{f', dueDate {due}' if due else ''}.
4. get_issue on it and confirm the description is there. If not, repeat step 3 once.

Do nothing else. Never create a second issue.

TITLE:
{title}

DESCRIPTION (markdown, use as-is):
{description}

Last line of your answer: {{"id": "<identifier like MEA-123, or empty if it failed>"}}"""
    out = claude(prompt, LINEAR_TOOLS, cwd=STATE, timeout=600, model="sonnet", mcp=True, logname="linear")
    ident = last_json(out).get("id", "")
    return ident if re.fullmatch(r"MEA-\d+", ident or "") else ""


def decisions(path: Path = DECISIONS) -> list[dict]:
    return read_json(path, [])


def idea_overrides(path: Path = DECISIONS) -> dict:
    """Her standing decision per idea from decisions.json, folded in order.

    A retry is not a change of mind about where an idea goes, so it never replaces an earlier skip
    or reroute: it only sets "retry_seq", the decision's position in the list, which the builder
    compares with the seq it last honored. (Keeping just the latest entry once let "retry 5" wipe
    out "pitch 5 instead", and the builder rebuilt the old outline every 10 minutes.)"""
    out = {}
    for i, d in enumerate(decisions(path)):
        iid = d.get("idea_id")
        if not iid:
            continue
        o = out.setdefault(iid, {})
        if d.get("action") == "retry":
            o["retry_seq"] = i + 1
        elif d.get("action") in ("skip", "reroute", "go"):
            o.update({"action": d["action"], "to_route": d.get("to_route", ""), "to_site": d.get("to_site", ""),
                      "date": d.get("date", "")})
    return out


def holds(path: Path = DESK / "holds.json") -> dict:
    return read_json(path, {})


def is_paused(route: str, site: str = "", path: Path = DESK / "holds.json") -> bool:
    h = holds(path)
    return route in h or (bool(site) and f"{route}:{site}" in h)
