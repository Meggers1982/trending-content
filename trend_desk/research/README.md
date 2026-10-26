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
| `run.py` | One day's run. Eligible: score 7+ (the dashboard's top-picks default), found in the last 3 days, never judged, not taken elsewhere; at most 150 (a prompt-size backstop, not a quota), best first. Applies the Judge's verdicts with the rules enforced again in code (a blocked route is dropped with reason `rule`), accounts for every PMID, writes `data/research_ledger.json` and `handoff/<date>.json`. A second run the same day is a no-op unless `--force`; `--dry-run` writes the prompt to `outputs/trend_desk/research_dry_run_prompt.md` and nothing else. |
| `mac.py` | The launchd tick: fast-forward, run the Judge after 9am Central once 8+ digests have published today (or after 2pm regardless; at most 3 tries a day), commit and push the ledger and handoff, start the builder, deliver problem messages. |
| `holds.json` | Paused routes for research ideas. tfm, roundup and brief are paused until MEA-1857 gives them research-specific prompts and a feed; until then those ideas are recorded and wait. |
| `tg.py` | Its own bot's send, with the hold-until-paired queue. |
| `feedback/decisions.json` | Her texted decisions about research ideas (written by the bot in piece 4). |
| `com.meagan.research-desk.plist` | Copy of the launchd job; the live one is in `~/Library/LaunchAgents`. |

The builder (`trend_desk/mac/builder.py --desk research`) uses `common.DESKS["research"]` for its
handoffs, holds, decisions and numbered list; `built.json` is shared, and research idea ids start
with `rd-`. A research pitch goes to `~/Pitches/state/research-handoffs.json`, which the weekday
pitch routine ranks as the "Research Desk" lane (`daily/PLAYBOOK.md` step 3) and re-verifies at
PubMed before writing.

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
