Run the full Trending Content OS daily pipeline.

Project directory: /Users/meaganmorris/trending-content-os
CLAUDE.md has all skill and workflow instructions — load it first.

Steps:
1. Load all configs from configs/
2. Run the Preflight Check
3. Check data/deferred_topics.yaml for any topics with a recheck_on date that has passed
4. Check data/run_history.yaml — note any key themes that have appeared in 2+ consecutive runs and flag if they appear again today
5. Run Skill 01 through Skill 12 in order for all retained candidates
6. Write the dashboard to outputs/daily_newsroom_dashboard/YYYY-MM-DD.html using today's date
7. Update data/run_history.yaml with today's run entry

Notes:
- Use the Google News Radar injected by run_pipeline.py as the broad discovery layer for news-led health topics before narrowing to retained candidates
- Use the SerpAPI Google Trends pre-fetch injected by run_pipeline.py as the primary search_velocity signal when present
- Estimate search_velocity from news volume and source credibility only if no Google Trends block is present in the live signal data
- CLAUDE_CODE_MAX_OUTPUT_TOKENS is set to 65000 in ~/.zshrc — restart the session if you hit output limit errors

$ARGUMENTS
