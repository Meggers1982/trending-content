# LIVE SIGNAL DATA — SerpAPI Pre-Fetch
The following signals were fetched from SerpAPI Google News and SerpAPI Google Trends immediately before this pipeline run. Treat Google Trends as AVAILABLE when this section contains a Google Trends block. Use it as the primary search_velocity input for Skills 01–05 (Signal Listener through Trend Strength Scorer). Use the Google News Radar as the broad discovery layer for news-led health topics, including topics that do not yet appear in Google Trends. Prioritize topics with convergence across News, Trends, primary/institutional sources, and credible publisher coverage.

# SIGNAL INTEGRITY WARNING

SerpAPI stopped answering for google_news, google_news_light, google_trends partway through this run, so that signal is incomplete below. Other sources ran normally — do not read the gap as an absence of activity.

Treat absence of signal as unknown, not as absence of activity. Say so in signal_summary.notes and lower confidence accordingly.