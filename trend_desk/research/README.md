# Research Desk

Trend Desk's idea applied to the research dashboard
(<https://research-digest-dashboard.vercel.app>, repo `Meggers1982/research-digest-dashboard`). The
dashboard holds thousands of digest studies, and almost none were ever read or marked, so the
decisions never got made. Research Desk makes them: a daily Research Judge reads the new studies,
code enforces the evidence rules, and Trend Desk's builder turns what's kept into finished work.

Approved 2026-10-25 (Linear MEA-1854; build tickets MEA-1855 to MEA-1859). Plan page:
<https://claude.ai/artifact/Fgb9qSVXnnoNHBEqxzTPsB> (vault `Process Diagrams/Research Desk Plan.html`).

```
12 digests ─> dashboard data/*.json ─> Research Judge (Mac, daily) ─> research/handoff/<date>.json
                                         code rules + one headless       │
                                         Claude call, no API credit       v
                       Meagan approves <── its own bot <── shared builder (--desk research)
                                                             pitch -> ~/Pitches/state/research-handoffs.json
```

## Marketing and career digests (Digest Desks piece 1, MEA-1865)

Two OpenAlex digests feed the same Judge: `marketing-research-digest` and
`career-psychology-digest` (approved 2026-10-25, MEA-1864; plan page
<https://claude.ai/artifact/WDTx9KeMmUyUWSJuJ9cy32>). `sources.load_openalex()` reads each repo's
`docs/data/index.json` and the run files from the last 16 days, and `openalex_study()` reshapes a
study into the dashboard's fields:

- **Id:** the OpenAlex work id (`W7221827692`) stands where a PMID goes. It can't collide with a
  numeric PMID and matches the `marketing:W…` / `career:W…` keys in the ~/Pitches triage ledgers once
  the prefix is stripped, so the 13 October history triage is skipped automatically.
- **Eligible:** the digest's **Lead** band only (82+ of 100; its scores run high, 452 of 522
  marketing studies are 70+), found in the last 14 days (the digests rotate one topic a day).
- **Date:** OpenAlex's date, in PubMed's form. A date on the 1st is treated as an issue date. For
  studies about to be judged, Crossref's `published-online` date replaces it (cached in
  `~/.local/state/research-desk/crossref.json`); without one, `date_verified` is false and the pitch
  agents confirm it. Then the usual 30/60-day rule applies (Meagan, 2026-10-25).
- **Rules:** a "Significant issues" fact-check verdict blocks every route; qualitative, unspecified
  and one-time survey designs never pitch (a longitudinal or diary survey can). See `rules.weak_design()`.
- Evidence links are `openalex.org/W…` plus the DOI; messages call them "OpenAlex W…".

## How it differs from Trend Desk

- **Input is already reported.** Each study arrives summarized, scored, caveated, fact-checked and
  coverage-checked by its digest. There's no trend ledger or "speed": the questions are whether it's
  fresh (online within 30 days), unpublicized, and strong enough to headline.
- **Runs on the Mac, on her subscription.** `judge.py` calls `claude -p --json-schema` with no tools
  and no MCP servers, and `ANTHROPIC_API_KEY` removed. The dashboard JSON is public, so nothing needs
  the cloud. This keeps it off the API balance that has been killing digest runs (MEA-749).
- **Own process, own bot.** launchd `com.meagan.research-desk` (every 10 minutes) runs `mac.py`. Its
  Telegram bot is piece 4 (MEA-1858); until it is paired, messages wait in
  `~/.local/state/research-desk/unsent.json` and go out once it is.

## Files

| File | What it does |
|---|---|
| `sources.py` | Loads every source in the dashboard's `data/sources.json` from raw.githubusercontent.com (curl), merges studies by PMID (highest score kept, every digest listed, earliest `run_date` kept). Reads `~/Pitches` ledgers for PMIDs already taken (digest triage, weekly top-12 candidates, earlier research handoffs) and for topics already pitched (daily and New Scientist ledgers, Trend Desk handoffs). |
| `rules.py` | Code rules, pure functions, tested in `test_rules.py`. Online date from PubMed's pubdate (Epub date wins; month-only or a full date more than 3 days after the digest found it is an issue date, so the find date stands in, marked unverified). `blocked()` per route: preprints go nowhere; subgroup/post hoc/exploratory, n under 50, already covered, or online over 60 days never pitch; animal or lab studies never pitch or go to the roundup; over 60 days never goes to the roundup. 31 to 60 days needs an `other_peg` to pitch. |
| `beats.md` | What a study is good for at each destination, read after Trend Desk's `beats.md`. Her research rules go at its bottom; shared rules stay in `trend_desk/rules.md`. |
| `judge.py` | Builds the prompt and makes the one structured call. |
| `run.py` | One day's run. Eligible: score 7+ (the dashboard's top-picks default), never judged, not taken elsewhere, and found on or after `FLOOR` (2026-10-22, where the backlog review stopped). There's no rolling window, so a study waits until it's judged. Studies below 7 get the backlog's quick Sonnet screen, and the ones it doesn't promote are recorded as `screened-out`. The Judge reads 150 studies per call, as many calls as the day needs, never a cut; a failed call's studies wait for the next run. Applies the Judge's verdicts with the rules enforced again in code (a blocked route is dropped with reason `rule`) and accounts for every PMID (one the Judge leaves out without a reason gets one more look on the next run, then is recorded as `not-selected`). Writes `data/research_ledger.json` and `handoff/<date>.json`. A second run the same day is a no-op unless `--force`; `--dry-run` writes the first call's prompt to `outputs/trend_desk/research_dry_run_prompt.md` and nothing else. OpenAlex studies keep their own Lead-band bar and 14-day lookback (MEA-1865). |
| `mac.py` | The launchd tick: fast-forward, run the Judge after 9am Central once 8+ digests have published today (or after 2pm regardless; at most 3 tries a day), commit and push the ledger and handoff, start the builder, deliver problem messages. |
| `holds.json` | Paused routes for research ideas (`pitch`, `tfm`, `roundup`, `brief`, `brief:<site>`), same shape as Trend Desk's. Empty since MEA-1857 opened all four on 2026-10-25. |
| `tg.py` | Its own bot's send, with the hold-until-paired queue. |
| `feedback/decisions.json` | Her texted decisions about research ideas (written by the bot in piece 4). |
| `backlog.py` | The one-time backlog review (MEA-1862) and the dashboard archive (MEA-1863). See below. |
| `com.meagan.research-desk.plist` | Copy of the launchd job; the live one is in `~/Library/LaunchAgents`. |

The builder (`trend_desk/mac/builder.py --desk research`) uses `common.DESKS["research"]` for its
handoffs, holds, decisions and numbered list; `built.json` is shared, and research idea ids start
with `rd-`. A research pitch goes to `~/Pitches/state/research-handoffs.json`, which the weekday
pitch routine ranks as the "Research Desk" lane (`daily/PLAYBOOK.md` step 3) and re-verifies at
PubMed before writing.

## The backlog review (one time, October 2026)

Approved 2026-10-25 ([plan](https://claude.ai/artifact/FL8AzNWyqjjveowHEziE3M)). The daily Judge only
reads three days, so `backlog.py` reads everything the dashboard held on the start date, once, then
archives it. `--start` snapshots the pile to `~/.local/state/research-desk/backlog/`, and the tick
(`mac.py`) runs `--step` overnight (10pm to 6am Central) until it's done, pausing an hour when it
hits the usage limit. Each batch is saved as it finishes.

1. **Sort** in code: merge by PMID, drop preprints, studies already judged, and the daily Judge's
   current three-day window.
2. **Screen** studies scored 6 or lower, 200 at a time, on Sonnet: which deserve a real look.
3. **Judge** the 7+ studies, her saved ones and whatever the screen promoted, about 80 at a time
   grouped by digest, with the daily prompt plus a backlog note. Old studies may go to tfm and
   brief at any age. A single-study pitch keeps the 30/60 rule, and the roundup takes 21 days at
   most. A study already triaged for pitches is blocked from pitch only.
4. **Final pass** (Opus) over every batch's ideas and "watch" studies: merge cross-digest duplicates
   and build **pattern pitches**. `kind: "pattern"` is 3+ human studies from 2+ journals, one online
   within 90 days, and a lead that could headline (`rules.pattern_problem`). Only `apply(...,
   backlog=True)` accepts them.
5. **Finish**: `handoff/backlog-<date>.json` (its ideas carry `backlog: true`), the ledger, the vault
   report `Research Desk Backlog Review Report.md`, a Linear read-it ticket, then the archive.

The builder builds every backlog idea, with no pacing ("as many outlines, pitches or briefs as
necessary", Meagan, 2026-10-25). Each brief uses about 8 SerpAPI searches. Outlines are banked in
`Research Desk Outlines/Backlog/` with no Wednesday and no ticket each. Pitches go to the pitch
lane, where pattern pitches have no 30-day clock.

**Archive.** The dashboard has an `archived` status (research-digest-dashboard 5f34749). Archived
studies are hidden unless the status menu asks for them. `--archive` marks every digest's copy of
every study found on or before the cutoff, skipping any study with a saved, pitched, passed or
deleted copy. It records the exact rows in `backlog/archived.json`, and `--unarchive` sets those
rows back to `new`.

```bash
python3 -m trend_desk.research.backlog --status
python3 -m trend_desk.research.backlog --step --now    # run outside the night window
```

## Privacy

This repo is public. The ledger and handoffs hold only study metadata from the public dashboard and
the Judge's neutral decisions. Her pitch topics are read from `~/Pitches` into the prompt but never
written here. The Judge's free-text day notes can name those topics, so they go to
`~/.local/state/research-desk/notes/<date>.md`, never to the ledger or a handoff (the first run's
notes were committed in 3d15b2a and removed in the next commit; they named two pitch topics).

## Run it by hand

```bash
python3 -m trend_desk.research.test_rules        # rules tests, no network
python3 -m trend_desk.research.run --dry-run     # see the prompt
python3 -m trend_desk.research.run               # judge today (about 5 minutes)
python3 -m trend_desk.mac.builder --desk research --dry-run
```
