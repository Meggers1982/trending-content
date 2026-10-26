# News Desk

Trend Desk's idea applied to two news dashboards nobody reads: **AgingWire**
(<https://agingwire-research-intelligence-sigma.vercel.app>, repo
`Meggers1982/agingwire-research-intelligence`) and the **org and press news digest**
(<https://news-digest-ivory.vercel.app>, repo `Meggers1982/org-news-digest`). A daily News Judge
reads their new items, code enforces the rules, and Trend Desk's builder turns what's kept into
finished work.

Approved 2026-10-25 (Linear MEA-1864; build tickets MEA-1866 to MEA-1868, review MEA-1869). Plan
page: <https://claude.ai/artifact/WDTx9KeMmUyUWSJuJ9cy32> (vault `Process Diagrams/Digest Desks Plan.html`).
Its sibling change, marketing and career studies joining Research Desk, is in `research/README.md`.

```
news digest /api/items ─┐
                        ├─> News Judge (Mac, daily) ─> news/handoff/<date>.json ─> shared builder (--desk news)
AgingWire latest.json ──┘   code rules + one headless                               pitch -> ~/Pitches/state/news-handoffs.json
                            Claude call, no API credit                              Meagan approves <── its own bot
```

## How it differs from Research Desk

- **The items are claims, not studies.** Each item has a `kind`: `press_release` and `org_release`
  are claims by an interested party; `agency`, `notice` and `analysis` are primary sources.
- **A release pitches only with a test.** The Judge must name `primary_test` (the registry entry,
  filing, dataset or study that shows whether the claim holds). Meagan's change (2026-10-25): a
  really interesting or potentially groundbreaking release is kept anyway as a **standout**; it
  reaches the pitch agents with `needs_independent_test: true`, and they find the test or drop it.
- **Noise is dropped in code** before the Judge sees it: CMS dataset refreshes, meeting and
  paperwork notices, and (for releases only) earnings, lawsuits, awards, conference appearances and
  product launches. Each is recorded in the ledger with its reason.
- **Freshness by kind:** a release is stale after 14 days, a notice, agency release or analysis
  after 42; between that and twice that, a pitch needs another peg; past twice, no pitch. Roundup
  items must be 21 days old or less, and a company's own claim is never a roundup fact.

## Files

| File | What it does |
|---|---|
| `sources.py` | Reads `news-digest-ivory.vercel.app/api/items?date=&days=3` (added for this desk, MEA-1866) and AgingWire's `outputs/latest.json`. Keys match the ~/Pitches triage ledgers (`aw-<slug>`, `press-<slug>`); org items are `org-<slug>`. Deduped across both sources by link. `taken_keys()` reads the triage ledgers and earlier News Desk handoffs. |
| `rules.py` | `noise()`, `age_days()`, `blocked()`, `needs_peg()`, `pitch_problem()`. Pure functions, tested in `test_rules.py`. |
| `beats.md` | What each kind of item is good for at each destination; her news rules at the bottom. |
| `judge.py` | The prompt and the one structured call (`claude -p --json-schema`, no tools, no API key). |
| `run.py` | One day's run. Eligible: first seen in the last 3 days, never judged, not taken, not noise; at most 120. Applies the verdicts with the rules enforced again, accounts for every key (one left out without a reason gets one more look), writes `data/news_ledger.json`, `handoff/<date>.json` and `feeds/roundup.json`. |
| `mac.py` | The launchd tick: fast-forward, run the Judge after 10am Central once both digests published today (or after 3pm regardless; at most 3 tries a day), commit and push, start the builder, deliver problem messages. |
| `tg.py` | Its own bot's send, with a hold-until-paired queue in `~/.local/state/news-desk/unsent.json`. Token in `~/.config/news-desk-bot/`. |
| `holds.json`, `feedback/decisions.json` | Paused routes and her texted decisions, same shape as the other desks'. |
| `com.meagan.news-desk.plist` | Copy of the launchd job; the live one is in `~/Library/LaunchAgents`. |

Destinations: a pitch goes to `~/Pitches/state/news-handoffs.json`, which the weekday pitch routine
ranks as the "News Desk" lane (`daily/PLAYBOOK.md` step 3) and re-verifies at the primary document;
outlines go to `~/The Female Model/News Desk Outlines/`; roundup items are read by the Friday
roundup prompt's "From News Desk" section; briefs use the brief room with the primary documents
as evidence.

## Privacy

This repo is public. The ledger and handoffs hold only public item metadata and the Judge's neutral
decisions. The Judge's day notes can name her pitch topics, so they stay in
`~/.local/state/news-desk/notes/`.

## Run it by hand

```bash
python3 -m pytest trend_desk/news -q          # rules tests, no network
python3 -m trend_desk.news.run --dry-run      # see the prompt
python3 -m trend_desk.news.run                # judge today
python3 -m trend_desk.mac.builder --desk news --dry-run
```
