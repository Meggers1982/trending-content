# Trend Desk

Turns the radars' output into finished work, so nobody has to read the dashboard and decide.
Built 2026-10-25 (Linear MEA-1828 to MEA-1832, decisions on MEA-117). The plain-language picture
is the vault page `Process Diagrams/Trend Desk.html`.

```
signals ──> Trend Judge (GitHub Actions, daily) ──> handoff/<date>.json ──> Mac builder ──> Meagan approves
  18 radars, daily pipeline,      ledger + one Claude call         pitch / tfm / roundup / brief      via Telegram
  rising queries, wide scan                ^                                                               │
                                           └──────── feedback/ (decisions, outcomes) <───────────────────┘
```

## Cloud half (this repo, `.github/workflows/run-trend-desk.yml`)

Runs when "Run Trending Content Pipeline" completes, with a fallback cron at 16:41 UTC. A second
run on the same day is a no-op unless dispatched with `force`.

| File | What it does |
|---|---|
| `wide_scan.py` | Google Trends Trending Now across all categories (60 items, news for the top 12). SerpAPI only. Writes `outputs/trend_desk/wide_<date>.json`; skips if today's exists. |
| `collect.py` | Reads radar scans, the pipeline's `extraction_*.json`, `serp_signals_*.md` rising queries and the wide scan into the ledger as sightings. The first run backfills all history. |
| `ledger.py` | `data/trend_ledger.json`. Speed is computed in code: **exploding** (first seen ≤7 days, breakout/emerging stage or 2+ sources), **emerging** (3+ ISO weeks, latest ≤14 days ago), **new**, **steady**. A term is judged once; it comes back only if it's held ("watch"), turns emerging, or 30 days pass. |
| `judge.py` | One `claude-opus-5-5` call, adaptive thinking, effort high, schema-enforced JSON, server-side refusal fallback. System prompt = `beats.md` + `sites.yaml` + `rules.md` + `holds.json` (cached). About $0.50 a run. |
| `run.py` | Applies Meagan's decisions, collects, judges, writes `handoff/<date>.json`, `feeds/roundup.json` and, on failure, a plain-language `outbox/` message. Never overwrites a day's handoff; a forced rerun merges into it. |

Editorial settings anyone can edit: `beats.md` (who it's for, what each destination wants),
`sites.yaml` (sites that can get briefs), `rules.md` (her standing rules, append-only),
`holds.json` (paused destinations: `pitch`, `tfm`, `roundup`, `brief`, `brief:<site>`).

## Mac half (`mac/`, launchd `com.meagan.trend-desk`, every minute)

The plist copy is `mac/com.meagan.trend-desk.plist`; the live one is in `~/Library/LaunchAgents`.

| File | What it does |
|---|---|
| `bot.py` | Each tick answers texts. Every 10 minutes: fast-forwards this repo, delivers `outbox/` messages (each `dedupe_key` at most once per 72h, nothing older than 3 days), starts the builder if any routed idea is unbuilt, and once a day runs `outcomes.py`. Works before the bot is paired. |
| `builder.py` | **pitch** → appends to `~/Pitches/state/trend-handoffs.json` (the weekday pitch routine ranks it in step 3). **tfm** → "Is it real?" outline `.docx` in `~/The Female Model/Trend Desk Outlines/` + Linear ticket in The Female Model with a proposed Wednesday. **roundup** → nothing; the Friday roundup prompt reads `feeds/roundup.json`. **brief** → `brief_room.py`. 3 attempts per idea, then set aside. Sends one Telegram message per pass, numbered for "skip 2". |
| `brief_room.py` | Focus keyword (Ahrefs if `~/.config/trend-desk/settings.json` has `"ahrefs": true`, else the strategist picks from free sources), TermScope evidence (`~/termscope-app/api/engine.py --mode strategy --live`, no Claude call), then strategist → search critic + site editor + evidence checker in parallel → strategist accepts/rejects every note. A second round only if something BLOCKING may be unresolved. Ends with a decision log. Brief `.docx` in `~/termscope-app/termscope-briefs/trend-desk/<site>/`, Linear ticket in the site's project (or Trending Content). TermScope is research, never the final structure. |
| `outcomes.py` | Public `feedback/outcomes.json` (aggregates only; the Judge reads it) and private edit lessons in `~/.local/state/trend-desk/lessons-*.md` from diffs of her edited outlines and briefs. |
| `text_prompt.md` | The file-tools-only agent that handles her texts: `feedback/decisions.json` (skip, reroute, retry, more-like, less-like), `holds.json`, `rules.md`, or an answer. |
| `tg.py`, `setup_bot.sh` | Its own Telegram bot (one bot per process). Token in `~/.config/trend-desk-bot/`. Setup: `zsh trend_desk/mac/setup_bot.sh`, then send `/start <code>` to the bot. Sets the avatar too. |

All Mac agents run as headless Claude Code on her subscription (`ANTHROPIC_API_KEY` is unset for
them), so the Mac half spends no API credit. Logs: `~/Library/Logs/trend-desk/`. Local state:
`~/.local/state/trend-desk/` (built.json is the build record).

## Privacy: this repo is public

Her texts, the bot's replies, her edits and pitch outcomes with names stay on the Mac. What goes
in the repo is limited to: editorial settings, short neutral decision records, and aggregate
outcome counts. Keep it that way when adding fields.

## Gotchas

- Structured outputs reject `minimum`/`maximum` on integers; ranges go in descriptions.
- The first live run's commit step failed because `git add` was given a folder that didn't exist
  yet; the step now adds only existing paths and the folders carry `.gitkeep`.
- A `--dry-run` with nothing due must write nothing (it once overwrote the day's handoff).
- This Mac's python.org Python has no CA bundle: Ahrefs and Telegram calls use curl, and
  TermScope runs in `~/.local/share/trend-desk/venv` with `SSL_CERT_FILE` from certifi.
- The Judge's notes on the first run flagged radar profiles pulling noise (fitness → Xbox and
  Packers trades, adhd-focus → gold prices, food-safety → car recalls). It drops them, but the
  seeds are worth tuning.
- Decisions in `feedback/decisions.json` are folded per idea, not "latest wins" (`common.idea_overrides()`).
  A retry only bumps `retry_seq` (its position in the list) and never replaces an earlier skip or
  reroute; `built.json` keeps the seq it honored in `retried`, carried through every rewrite of the
  record. On 2026-10-25 "retry 5" overwrote "pitch 5 instead" and the success record dropped
  `retried`, so the builder rebuilt the old outline every 10 minutes (six copies) until outlines were
  paused.
- `commit_push()` pushes any local-only commits even when there is nothing new to commit, so a push
  that lost a race with another job's commit doesn't leave the handoff stranded on the Mac.
