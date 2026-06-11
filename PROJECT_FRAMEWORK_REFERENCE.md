# Trending Content OS Framework Reference

Use this project as a reusable framework for future trend-intelligence and editorial-prioritization systems.

## Core Product Pattern

Trending Content OS is a daily content intelligence pipeline that turns raw trend signals into a ranked editorial priority board.

Reusable flow:

1. Load niche, audience, source, category, scoring, and competitor configs.
2. Fetch live signal data from search, news, trends, trusted sources, and competitors.
3. Classify whether each signal fits the audience and category rules.
4. Run a pre-scoring safety gate for high-risk topics.
5. Score trend strength, content opportunity, confidence, urgency, and AI citation potential.
6. Filter duplicates or route update candidates.
7. Generate content angles, headlines, briefs, next steps, and source requirements.
8. Output an editorial dashboard, CSV, narrative report, and optional email.

## Reusable Architecture

The project currently stores the operating workflow in `CLAUDE.md`, not separate skill files.

Core stages:

- Skill 01: Signal Listener
- Skill 02: Category Classifier
- Skill 02b: Health Claim Verification Gate
- Skill 03: Entity Expander
- Skill 04: Trend Scorer
- Skill 05: SERP Gap Analyzer
- Skill 06: Source Validator
- Skill 07: Data & Research Decider
- Skill 08: Expert Source Finder
- Skill 09: Angle Generator
- Skill 10: News Brief Builder
- Skill 11: Discover Optimizer
- Skill 12: Editorial Priority Board

## Important Design Decisions

- SerpAPI is a current dependency for Google News and Google Trends.
- Google Trends from `run_pipeline.py` should be treated as available when the live signal block is injected.
- `requests` is not required; SerpAPI calls use Python stdlib HTTP.
- `run_pipeline.py` and `dashboard_template.html` belong in the project root.
- Output goes to `outputs/daily_newsroom_dashboard/`.
- `publish_timing` values are `immediate`, `short_term`, `scheduled`, `evergreen`, and `monitor`.
- CSV output has 19 columns: `date_detected` plus 18 candidate fields.
- Dashboard v1 is read-only: no approve/reject/save/comment state.

## Safety Gate Pattern

Skill 02b is a reusable hard-gate pattern for high-risk domains.

For health content, it triggers on:

- Medical study or clinical trial claim
- Drug or treatment claim, including OTC
- Supplement claim
- Product recall
- Dosage or safety guidance

Outcomes:

- Pass: source exists and claim matches
- Monitor: source exists but public claim materially distorts the evidence
- Reject: no verifiable source or claim does not match source

This gate is not a scoring penalty. Failed topics should not reach scoring.

## Confidence Pattern

Confidence is data-quality confidence, not truth confidence.

It measures whether trend and opportunity scores are based on verifiable inputs rather than inference, thin sourcing, stale signals, or social-only noise.

Use:

- High: `source_count >= 3` and 2+ independent signal channels
- Medium: `source_count == 2` or one strong channel with at least 2 sources
- Low: `source_count <= 1`, social-only signal, or missing keyword/search support

Freeze confidence at scoring time.

## Signal Convergence Channels

Use four independent channels:

- Search: Ahrefs plus Google Trends, counted as one channel
- News: 2+ named outlets not simply repeating one wire story
- Social: Reddit, X, or social spike; weak alone for health topics
- Primary/Institutional: FDA, CDC, NIH, journal, DOI, PubMed, ClinicalTrials.gov, etc.

## Discover Score Pattern

`discover_score` estimates AI citation likelihood, not SEO ranking.

Factors:

- Entity clarity
- Question-answer fit
- Primary source density
- Evergreen potential
- SERP gap

Keep it as a separate 1-5 ordinal score. Do not average it into trend or opportunity.

## Duplicate Fallback Pattern

Use two tiers:

- If `site_url` exists, self-check for existing or update content.
- If `site_url` is absent, use competitor-list fallback and disclose that self-check was skipped.

Schema-safe values:

- `new`
- `existing`
- `update`

When self-check is unavailable, use `new` plus a note.

## Dashboard UX Pattern

The preferred dashboard direction is a light editorial operations surface:

- Black top bar
- Serif editorial title
- Compact run metadata
- Large metric cards
- Google Trends insight callout
- Dense priority table
- Trend/opportunity mini bars
- Velocity, urgency, SERP, source count, and source/status chips
- Expandable table rows for angle, why now, and next steps
- Rejected topics below the fold

Reference files:

- `dashboard_template.html`
- `outputs/daily_newsroom_dashboard/dashboard_preview.html`

## Reuse Notes

For future niches or clients:

- Keep the staged skill architecture.
- Swap configs first, not code.
- Replace the safety gate domain logic if moving outside health.
- Keep confidence, convergence, duplicate fallback, and dashboard patterns.
- Keep extraction strict and fail closed rather than generating blank dashboards.
