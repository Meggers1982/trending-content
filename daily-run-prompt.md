# Daily Run Prompt

Copy and paste the block below into a new Claude Code session opened from the `/Users/meaganmorris/trending-content-os` directory.

---

```
Run the full daily pipeline for Trending Content OS.

Project directory: /Users/meaganmorris/trending-content-os
CLAUDE.md has all skill and workflow instructions — load it first.

Steps:
1. Load all configs from configs/
2. Run the Preflight Check
3. Check data/deferred_topics.yaml for any topics with a recheck_on date that has passed
4. Check data/run_history.yaml — note any key themes that have appeared in 2+ consecutive runs (flag if they appear again today)
5. Run Skill 01 through Skill 12 in order for all retained candidates, including Skill 02b for high-risk health topics before scoring
6. Write the dashboard to outputs/daily_newsroom_dashboard/YYYY-MM-DD.html (today's date)
7. Update data/run_history.yaml with today's run entry

Today's date: [INSERT DATE]

Notes:
- If site_url is not configured, use competitor-list fallback for duplicate/SERP-gap context and note that self-check was skipped
- Use the Google News Radar injected by run_pipeline.py as the broad discovery layer for news-led health topics before narrowing to retained candidates
- Use the SerpAPI Google Trends pre-fetch injected by run_pipeline.py as the primary search_velocity signal when present
- Estimate search_velocity from news volume and source credibility only if no Google Trends block is present in the live signal data
- If output token limit errors occur, set CLAUDE_CODE_MAX_OUTPUT_TOKENS=65000 before running
```

---

## How to use

1. Open Claude Code in `/Users/meaganmorris/trending-content-os`
2. Update `[INSERT DATE]` to today's date (e.g., `May 15, 2026`)
3. Paste and send

## Optional additions

Append any of these to the prompt as needed:

**If you have recent article slugs for duplicate detection:**
```
For duplicate checking, here are our recent article slugs (last 90 days):
[paste slugs]
```

**If you want to focus on specific signals:**
```
Prioritize signals from these areas today: [e.g., "FDA news, cancer research, GLP-1 updates"]
```

**If you want to skip straight to a brief:**
```
Skip the full pipeline. I already have a topic: [topic]. Jump to Skill 09 (Angle Generator) and run through Skill 12.
```

**If you want a lightweight triage instead of a full run:**
```
Run Signal Review (lightweight triage) only — do not run the full pipeline. Here are the signals to triage:
[paste headlines/URLs]
```
