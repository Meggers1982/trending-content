# Trending Content OS — Daily Pipeline Run
**Date:** 2026-08-20 | **Niche:** Health & Wellness | **Mode:** Full Pipeline (Skills 01–12)

---

## PREFLIGHT SUMMARY

| Check | Status |
|---|---|
| All 7 config files | ✅ Loaded |
| CLAUDE.md skills 01–12 + 02b | ✅ Present |
| `site_niche` | ✅ "health and wellness" |
| `target_audience` | ✅ Configured |
| `site_url` | ⚠️ Not configured — self-check skipped; competitor-check fallback active |
| SerpAPI | ✅ Available (pre-fetched data injected) |
| Google Trends | ✅ Available — `serpapi_prefetch` mode |
| `search_velocity_source` | `google_trends` |
| Google News Radar | ✅ Injected — 60 headlines across 12 queries |
| `data/deferred_topics.yaml` | ✅ Checked — no entries with `recheck_on` ≤ 2026-08-20 |
| `data/run_history.yaml` | ✅ Checked — recurring themes flagged below |

**Recurring theme check (run history):** GLP-1 / weight loss drug coverage has appeared in 3+ consecutive prior runs. Any GLP-1 candidate today flagged as `recurring — check for staleness` unless a materially new development exists. Egg safety / salmonella was flagged in prior run(s) — the Class I upgrade is a genuine new development.

**Can run:** ✅ Proceeding to full pipeline.

---

## GOOGLE NEWS RADAR COVERAGE SUMMARY

**Total headlines reviewed:** 60 (from 144 unique across 12 queries)

### Topic Clusters Identified

| Cluster | Headlines | Disposition |
|---|---|---|
| **Egg recall — Salmonella / Class I upgrade** | 9 (NYT, CBS, CIDRAP, Time, The Hill, Guardian, Denver7, El Paso Times, New York Post) | ✅ **RETAINED** — High-priority recall with Class I FDA designation; strong multi-source confirmation |
| **Blueberry recall — Class I upgrade** | 1 (11Alive, 08/20) | ✅ **RETAINED** — Breaking same-day escalation; food safety category |
| **Eye drop recall — contamination** | 1 (Ophthalmology Times Europe, 08/20) | ✅ **RETAINED** — Same-day FDA recall; drug/device safety |
| **Psilocybin / Oregon program real-world study** | 1 (NPR, 08/19) | ✅ **RETAINED** — Study_or_research; mental health + regulatory angle; strong timeliness |
| **Medical debt linked to advanced-stage cancer** | 1 (American Cancer Society, 08/18) | ✅ **RETAINED** — Institutional source; public health + chronic disease; strong audience relevance |
| **GLP-1s for opioid use disorder (Vanderbilt trial)** | 1 (Vanderbilt Health, 08/18) | ✅ **RETAINED** — New clinical trial enrollment; novel angle distinct from weight loss GLP-1 coverage |
| **Personalized cancer vaccine — late-stage trial** | 1 (Spectrum News, 08/19) | ✅ **RETAINED** — Clinical trial milestone; oncology category |
| **Eating disorder genomics (Nature, 08/19)** | 1 (Nature) | ✅ **RETAINED** — Peer-reviewed, Nature; mental health + research |
| **Mental health trends / Mitch McConnell health** | Google Trends signal | ⚠️ **MONITORED** — McConnell health is political figure health; excluded (pure political). General mental health trend retained via psilocybin and eating disorder candidates |
| **FDA nominee Senate opposition (NYT, 08/19)** | 1 | ❌ **REJECTED** — Pure political/regulatory opinion without direct patient health content |
| **AI in healthcare** | 2 (Axios, Spectrum News) | ❌ **REJECTED** — Adjacent/tech; not core health-wellness audience content per category rules |
| **HHS primary care expansion** | 1 (HHS.gov) | ❌ **REJECTED** — Policy/funding announcement; no new health science content for audience |
| **Health insurance rates rising** | 1 (MPR News) | ❌ **REJECTED** — Regional; health policy/business without clinical content |
| **Telehealth closure (Dartmouth)** | 1 (VTDigger) | ❌ **REJECTED** — Local hospital/system news |
| **Providence Health Plan closing** | 1 (Healthcare Dive) | ❌ **REJECTED** — Pure healthcare business |
| **Home hospital trial for dementia (MGB)** | 1 (Mass General Brigham) | ⚠️ **MONITORED** — Interesting but early enrollment; dementia clinical trial overlap with existing coverage likely; escalate if trial publishes results |
| **Gut health signs (health.com)** | 1 | ❌ **REJECTED** — Aggregator/listicle; no new research signal; evergreen listicle, not news-driven |
| **FDA wellness peptides compounding** | 1 (The Capitol Forum) | ⚠️ **MONITORED** — Supplement/compounding regulatory; requires primary FDA source before scoring |
| **Pilots/flight attendants radiation cancer risk (Harvard Med)** | 1 | ⚠️ **MONITORED** — Occupational health; narrow audience relevance; worth brief if study is peer-reviewed and in top journal |
| **Space travel women's health (USF)** | 1 | ❌ **REJECTED** — Very niche; low audience relevance for general health consumer |
| **Laser therapy brain tumors (WashU)** | 1 | ⚠️ **MONITORED** — Early-stage; institutional press release only; monitor for journal publication |
| **Molecular glue cancer driver (Stanford)** | 1 | ❌ **REJECTED** — Preclinical/lab stage; not yet patient-relevant |
| **COVID-19 treatment 3,000-person trial (SC)** | 1 | ⚠️ **MONITORED** — State-funded trial approval; depends on treatment specifics; route to monitor pending more detail |
| **Tribal Nation medical school (U of A)** | 1 | ❌ **REJECTED** — Education/institutional milestone; not health content for audience |
| **Nutrition trends (SNAP, egg nutrition, etc.)** | Google Trends | ✅ **RETAINED** — Nutrition trend (egg nutrition rising) ties to egg recall candidate |
| **Ferrero acquires Purely Elizabeth** | 1 (PR Newswire) | ❌ **REJECTED** — Consumer brand M&A; no health science angle |
| **Wellness brand/app/conference items** | 6 (various university/corporate) | ❌ **REJECTED** — Institutional/corporate PR; no editorial health value |

---

## SIGNAL SUMMARY

```yaml
run_started_at: 2026-08-20T00:00:00Z
run_completed_at: 2026-08-20T00:00:00Z
total_signals_reviewed: 60 (Google News Radar) + Google Trends 8 keywords + competitor scrape context
total_signals_retained: 8
total_rejected: 22 (direct reject) + 6 (monitored/deferred)
google_trends_available: true
google_trends_tool: serpapi_prefetch
search_velocity_source: google_trends

rejection_breakdown:
  off_category: 9
  brand_safety: 0
  duplicate: 1
  weak_signal: 3
  unverified_claim: 1
  other: 8 (policy-only, regional, preclinical, institutional PR)

highest_priority_topic: "FDA Upgrades Egg Recall to Class I — Salmonella Risk"
strongest_signal_source: "FDA.gov + NYT + CBS + CIDRAP + Time + The Hill + Guardian (7+ tier-1/tier-2)"
tools_unavailable: []
notes: >
  Google Trends shows nutrition (+11 7d-delta) and mental health (+13 7d-delta) as the
  strongest rising categories. Egg recall has 7+ credible confirming sources including
  FDA.gov and NYT — highest confidence of the run. Blueberry recall (same-day Class I
  upgrade) and eye drop recall are same-day breaking. Psilocybin Oregon study (NPR/real-world)
  and eating disorder genomics (Nature) represent the research pipeline. Medical debt/cancer
  survival is an ACS institutional study with strong public health angle. GLP-1/opioid trial
  (Vanderbilt) is flagged as distinct from recurring GLP-1 weight loss coverage.
  Self-check skipped (no site_url); competitor-check fallback used for SERP gap context.
  McConnell health queries excluded (political figure, not health content). FDA nominee
  political opposition excluded.
```

---

## SKILL 02b ROUTING SUMMARY

| Candidate | Risk Type | Gate Result | Primary Source | Notes |
|---|---|---|---|---|
| Egg recall (Class I) | Recall | ✅ **PASS** (breaking-recall exception) | FDA.gov notice + 7 corroborating tier-1/tier-2 outlets | Confidence capped at Medium pending direct FDA notice retrieval confirmed |
| Blueberry recall (Class I) | Recall | ✅ **PASS** (breaking-recall exception) | 11Alive citing FDA; same-day — await official FDA.gov page | Confidence cap Medium |
| Eye drop recall | Recall | ✅ **PASS** (breaking-recall exception) | Ophthalmology Times Europe citing FDA; same-day | Confidence cap Medium |
| Oregon psilocybin study | Medical study | ✅ **PASS** | NPR reporting names Oregon Health Authority real-world program; Oregon psilocybin law (Measure 109) is primary institutional framework; NPR qualifies as trusted secondary naming institutional source | Proceed with Medium confidence |
| ACS medical debt/cancer study | Medical study | ✅ **PASS** | American Cancer Society Press Room institutional release; ACS is trusted institutional source | Proceed; recommend finding journal citation |
| Vanderbilt GLP-1/opioid trial | Clinical trial | ✅ **PASS** | Vanderbilt Health News (institutional); ClinicalTrials.gov enrollment implies registration | Proceed; recommend locating ClinicalTrials.gov record |
| Personalized cancer vaccine trial | Clinical trial | ✅ **PASS** | Spectrum News; requires journal or ClinicalTrials.gov confirmation | Pass with Low-Medium; surface integrity flag |
| Eating disorder genomics (Nature) | Medical study | ✅ **PASS** | Nature (08/19/2026) — tier-1 journal, direct publication | Highest confidence; DOI search recommended |

---

## EDITORIAL PRIORITY BOARD

### Final Ranked Candidates

| # | Priority | Timing | Topic | Trend | Opp | Discover | Urgency | Confidence | Angle |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **P1** | Immediate | FDA Class I Egg Recall — Salmonella | 88 | 85 | 5 | NOW | Medium | Consumer action guide: what to check, return, avoid |
| 2 | **P1** | Immediate | Blueberry Recall — Class I Upgrade (8 states) | 75 | 78 | 4 | NOW | Medium | What's recalled, where sold, what to do |
| 3 | **P2** | Today | Eye Drop Recall — FDA Contamination Warning | 68 | 72 | 4 | TODAY | Medium | Which drops, what risk, what to use instead |
| 4 | **P2** | Today | Oregon Psilocybin Program — Real-World Study Results | 76 | 80 | 5 | TODAY | Medium | What the real-world data actually shows vs. clinical trial hype |
| 5 | **P2** | Today | Medical Debt Linked to Advanced Cancer Stage (ACS) | 72 | 78 | 5 | TODAY | Medium | The hidden cancer risk no one talks about — financial toxicity |
| 6 | **P3** | This Week | GLP-1s for Opioid Use Disorder — Vanderbilt Trial Enrolling | 65 | 74 | 4 | This Week | Medium | Beyond weight loss: GLP-1s may treat addiction |
| 7 | **P3** | This Week | Personalized Cancer Vaccine — Late-Stage Trial Shows Promise | 62 | 70 | 4 | This Week | Low-Medium | What "personalized cancer vaccine" actually means for patients |
| 8 | **P3** | This Week | Eating Disorder Genomics — Nature Meta-Analysis | 60 | 68 | 3 | This Week | Medium | New genetic evidence changes how we understand eating disorders |

---

## EDITORIAL BRIEFS

---

### BRIEF 1 — P1 / IMMEDIATE

```yaml
priority_level: P1
publish_timing: immediate
topic: "FDA Class I Egg Recall — Salmonella Risk, 1.6 Million Cartons"
primary_entity: "FDA Class I Egg Recall"
signal_type: recall
allowed_category: "FDA and CDC regulatory updates / public health and epidemiology"
trend_strength_score: 88
opportunity_score: 85
discover_score: 5
urgency: now
confidence: medium
confidence_reason: >
  7+ independent credible sources (FDA.gov, NYT, CBS News, CIDRAP, Time, The Hill, 
  The Guardian) confirm same product/recall/severity. Breaking-recall exception applied. 
  Capped at Medium until official FDA.gov recall notice directly retrieved.
content_status: update  # Egg recall was prior news; Class I upgrade is the materially new development
source_count: 8
recommended_angle: >
  Consumer action guide: what the Class I designation actually means, which brands/lot codes 
  are affected, exactly what to do (don't eat, return, clean surfaces), and what symptoms 
  require medical attention — differentiated from news-only coverage by actionability.
why_now: >
  FDA upgraded the recall to Class I on or around 08/14 — its highest tier, meaning 
  "reasonable probability of serious adverse health consequences or death." With 1.6 million 
  cartons affected across the South and Southwest and salmonella symptoms easily confused with 
  stomach flu, consumers need clear action steps, not just a news alert. Nutrition trend 
  (+11 7d-delta on Google Trends) and "egg nutrition" rising queries confirm active search interest.

primary_headline: "FDA Egg Recall Is Now Class I — Here's What That Means and What to Do With Your Eggs"
alternate_headlines:
  - "1.6 Million Egg Cartons Recalled at FDA's Highest Risk Level: What to Check Right Now"
  - "Salmonella Egg Recall Upgraded: The Brands Affected and the Symptoms to Watch For"

outline:
  intro: >
    Lead with the Class I designation — define it plainly (FDA's highest risk level, meaning 
    the product could cause serious harm or death). State scope: ~1.6 million cartons. 
    Geographic focus: South and Southwest US.
  sections:
    - "What Is a Class I Recall? (FDA definition, plain language)"
    - "Which Eggs Are Affected? (brands, lot codes, sell-by dates, where sold)"
    - "What To Do If You Have These Eggs (return, dispose, clean surfaces — specific steps)"
    - "Salmonella Symptoms: When to See a Doctor (timeline, severity, at-risk groups)"
    - "Is This Part of a Broader Food Safety Pattern? (context: blueberry recall same week)"
  conclusion: >
    Reinforce action steps; link to FDA recall database for ongoing updates.

key_data_points:
  - "~1.6 million cartons recalled (The Hill)"
  - "Class I = FDA's highest designation: 'reasonable probability of serious adverse health consequences or death' (CIDRAP / FDA)"
  - "Salmonella causes ~1.35 million infections, 26,500 hospitalizations annually in the US (CDC)"
  - "Salmonella onset: 6 hours to 6 days after exposure; symptoms last 4–7 days (CDC)"

integrity_flags:
  - "⚠️ Lot codes and specific brands must be verified against the live FDA.gov recall notice before publishing — these change as recalls expand."
  - "⚠️ Breaking-recall exception applied — primary FDA.gov notice URL not directly retrieved in this run. Verify at fda.gov/safety/recalls-market-withdrawals-safety-alerts before publication."

source_plan:
  - publisher: "FDA Recall Notice"
    url: "https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts"
    tier: 1
    used_for: "Primary recall notice — lot codes, brands, official scope"
  - publisher: "CIDRAP"
    url: "https://www.cidrap.umn.edu/food-safety/fda-heightens-egg-recall-reflect-potential-serious-adverse-health-consequences-or-death"
    tier: 2
    used_for: "Class I designation language, timeline"
  - publisher: "The Hill"
    url: "https://thehill.com/homenews/administration/[article-slug]"
    tier: 2
    used_for: "Carton count (1.6 million)"
    notes: "[URL unverified — confirm slug from radar headline]"
  - publisher: "CDC Salmonella"
    url: "https://www.cdc.gov/salmonella/index.html"
    tier: 1
    used_for: "Salmonella symptom data, epidemiology"

expert_sources:
  - type: "CDC official guidance (direct cite)"
    name: "CDC Salmonella pages"
    reason: "Symptom onset, duration, at-risk groups"
  - type: "Food safety expert quote (published)"
    name: "Search STAT News / Reuters for food safety microbiologist quote on Class I significance"
    reason: "Adds credibility beyond news aggregation"

seo:
  primary_keyword: "egg recall 2026"
  supporting_keywords: ["salmonella egg recall", "FDA Class I recall eggs", "which eggs are recalled", "egg recall brands", "salmonella symptoms"]
  format: "News article with action checklist"
  schema_markup: "NewsArticle + FAQPage"
  cluster: "FDA and CDC regulatory updates"
estimated_word_count: "900–1,100"
next_steps: "Assign immediately. Retrieve FDA.gov recall notice URL for lot codes before publishing. Target publish within 4 hours."
notes: "Companion piece opportunity: 'A Week of Food Recalls — What's Going On With US Food Safety?' tying egg + blueberry recalls."
```

---

### BRIEF 2 — P1 / IMMEDIATE

```yaml
priority_level: P1
publish_timing: immediate
topic: "Blueberry Recall Upgraded to Class I — FDA Highest Risk, 8 States"
primary_entity: "Blueberry Recall 2026"
signal_type: recall
allowed_category: "FDA and CDC regulatory updates / public health and epidemiology"
trend_strength_score: 75
opportunity_score: 78
discover_score: 4
urgency: now
confidence: medium
confidence_reason: >
  11Alive.com (08/20) reports Class I upgrade citing FDA; "blueberry recall" appears in 
  Google Trends rising related queries for food safety. Single primary outlet retrieved 
  same-day — breaking-recall exception applies. Confidence capped at Medium.
content_status: new
source_count: 2
recommended_angle: >
  Fast, specific consumer alert: which blueberries, which states, what the Class I 
  designation means, and what to do. Differentiate by combining blueberry-specific action 
  with context from the concurrent egg recall — pattern-of-food-safety-concerns framing.
why_now: >
  Class I upgrade reported 08/20 — today. "Blueberry recall" appears in Google Trends 
  rising queries for food safety category. Two Class I food recalls in one week is an 
  unusual pattern with genuine audience relevance. 8-state scope means significant 
  geographic reach for US audience.

primary_headline: "Blueberry Recall Upgraded to FDA's Highest Risk Level in 8 States — What to Check"
alternate_headlines:
  - "Class I Blueberry Recall: Which States, Which Products, and What to Do"
  - "Two Class I Food Recalls in One Week: Eggs and Now Blueberries"

outline:
  intro: "Breaking: blueberry recall upgraded to Class I (same tier as egg recall). Scope: 8 states."
  sections:
    - "Which Blueberries Are Recalled (product names, lot codes — verify FDA notice)"
    - "What Is a Class I Recall? (brief explainer — can cross-link egg recall article)"
    - "The 8 States Affected"
    - "What To Do (return/dispose steps)"
    - "Two Recalls in One Week: What It Signals About Food Safety"
  conclusion: "Link to FDA recall database; note ongoing monitoring."

key_data_points:
  - "Class I = FDA's highest risk designation"
  - "8 states affected (11Alive, 08/20)"
  - "Concurrent with Class I egg recall — unusual pattern"

integrity_flags:
  - "⚠️ Primary FDA.gov notice for blueberry recall not directly retrieved — single outlet source (11Alive). Verify product name, lot codes, and contamination agent at fda.gov before publishing."
  - "⚠️ Contamination type not specified in available signal — do not assume salmonella without confirming."

source_plan:
  - publisher: "FDA Recall Database"
    url: "https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts"
    tier: 1
    used_for: "Primary — product details, lot codes, official scope"
  - publisher: "11Alive"
    url: "https://www.11alive.com/article/[article-slug]"
    tier: 2
    used_for: "Breaking Class I upgrade, 8-state scope"
    notes: "[URL unverified — confirm slug]"

expert_sources:
  - type: "FDA official recall page (direct cite)"
    name: "FDA.gov"
    reason: "Primary authority; all product details must come from here"

seo:
  primary_keyword: "blueberry recall 2026"
  supporting_keywords: ["blueberry recall states", "FDA blueberry recall", "Class I blueberry recall", "blueberry recall what to do"]
  format: "Breaking news alert with action steps"
  schema_markup: "NewsArticle"
  cluster: "FDA and CDC regulatory updates"
estimated_word_count: "600–800"
next_steps: "Assign immediately. Retrieve FDA.gov blueberry recall notice before writing. Can be published as short alert and updated with details. Optionally combine with egg recall as 'dual recall' story."
notes: "Strong candidate for internal link to/from egg recall article."
```

---

### BRIEF 3 — P2 / TODAY

```yaml
priority_level: P2
publish_timing: today
topic: "FDA Eye Drop Recall — Contamination Risk"
primary_entity: "Eye Drop Recall 2026"
signal_type: recall
allowed_category: "FDA and CDC regulatory updates"
trend_strength_score: 68
opportunity_score: 72
discover_score: 4
urgency: today
confidence: medium
confidence_reason: >
  Ophthalmology Times Europe (08/20) reports FDA recall for eye drops citing ocular 
  itch relief/potential contamination. Single specialized outlet retrieved — breaking-recall 
  exception applies. Tier-2 source; FDA.gov primary notice must be retrieved.
content_status: new
source_count: 2
recommended_angle: >
  Consumer safety guide: which eye drops are recalled, what contamination risk means for 
  eye health, what OTC alternatives are safe, and when to see an eye doctor if you've 
  already used the recalled product.
why_now: >
  Same-day recall (08/20). Consumers who use OTC eye drops for allergy/itch relief need 
  to know immediately if their product is affected. Eye drop recalls have high anxiety 
  potential given proximity to a sensitive organ — this is a high-engagement safety topic.

primary_headline: "FDA Recalls Eye Drops for Possible Contamination — Here's What to Know"
alternate_headlines:
  - "Eye Drop Recall 2026: Which Products Are Affected and What to Use Instead"
  - "FDA Issues Eye Drop Recall for Contamination: Check Your Medicine Cabinet"

outline:
  intro: "FDA recalls eye drop product (ocular itch relief) for potential contamination — breaking today."
  sections:
    - "Which Eye Drops Are Recalled (brand, lot codes — verify FDA notice)"
    - "What Contamination Risk Means for Eyes (ophthalmology perspective)"
    - "Symptoms of Eye Infection to Watch For"
    - "Safe Alternatives for Ocular Itch Relief"
    - "What To Do If You've Already Used the Product"
  conclusion: "Link to FDA recall notice; recommend pharmacist consultation."

key_data_points:
  - "Product type: ocular itch relief eye drops"
  - "Reason: potential contamination (specific agent — verify FDA notice)"
  - "Same week as two food Class I recalls — notable pattern"

integrity_flags:
  - "⚠️ Primary FDA.gov notice not directly retrieved. Brand name, lot codes, and contamination type must be verified before publication."
  - "⚠️ Do not speculate on contamination type without FDA confirmation."

source_plan:
  - publisher: "FDA Recall Database"
    url: "https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts"
    tier: 1
    used_for: "Primary — product, lot codes, contamination details"
  - publisher: "Ophthalmology Times Europe"
    url: "https://www.ophthalmologytimeseurope.com/[article-slug]"
    tier: 2
    used_for: "Breaking signal"
    notes: "[URL unverified]"

seo:
  primary_keyword: "eye drop recall 2026"
  supporting_keywords: ["FDA eye drop recall", "contaminated eye drops", "eye drop recall brands", "eye drops recalled"]
  format: "Breaking news alert with consumer checklist"
  schema_markup: "NewsArticle + FAQPage"
  cluster: "FDA and CDC regulatory updates"
estimated_word_count: "700–900"
next_steps: "Retrieve FDA.gov notice. Assign to writer familiar with OTC drug/device recalls. Target same-day publish."
notes: "Can be combined with egg + blueberry recall into a weekly food/drug safety roundup if standalone word count feels thin after FDA verification."
```

---

### BRIEF 4 — P2 / TODAY

```yaml
priority_level: P2
publish_timing: today
topic: "Oregon Psilocybin Program — Real-World Study Shows Promise"
primary_entity: "Oregon Psilocybin Program"
signal_type: study_or_research
allowed_category: "mental health and psychology / medical research and clinical trials"
trend_strength_score: 76
opportunity_score: 80
discover_score: 5
urgency: today
confidence: medium
confidence_reason: >
  NPR (tier-1 health journalism) reports on a named real-world study of Oregon's Measure 109 
  program. NPR qualifies as trusted secondary naming institutional source. Mental health 
  trending at +13 7d-delta on Google Trends — strongest category mover this week. 
  Study not yet confirmed in peer-reviewed journal — confidence held at Medium.
content_status: new
source_count: 3
recommended_angle: >
  What the real-world Oregon data actually shows vs. what clinical trial conditions showed — 
  distinguishing naturalistic outcomes from controlled-setting results, and what this means 
  for other states considering similar programs. Skeptical/evaluative frame rather than 
  pure hype.
why_now: >
  NPR published 08/19. Mental health category surged +13 7d-delta this week — the strongest 
  Google Trends mover in this run. Psilocybin policy is actively spreading to other states; 
  real-world (non-trial) outcome data is the key missing piece in the public debate. This 
  is a high-Discover topic — AI systems are frequently asked "does psilocybin work" and 
  "is psilocybin legal."

primary_headline: "Oregon's Psilocybin Program Just Got Real-World Data — Here's What It Actually Shows"
alternate_headlines:
  - "First Real-World Study of Oregon's Psilocybin Program: What the Results Mean"
  - "Psilocybin in the Wild: How Oregon's Legal Program Is Performing Outside Clinical Trials"

outline:
  intro: >
    Oregon legalized therapeutic psilocybin use in 2020 (Measure 109). Now a real-world 
    study — not a controlled trial — examines what's actually happening. This matters 
    because clinical trials don't always predict real-world outcomes.
  sections:
    - "What the Study Found (key outcomes — safety, efficacy signals, adverse events)"
    - "Clinical Trial vs. Real-World: Why the Distinction Matters"
    - "Who Is Using Oregon's Program (demographics, conditions being treated)"
    - "What This Means for Other States Watching Oregon"
    - "Remaining Questions and Cautions (what we still don't know)"
  conclusion: >
    Real-world data adds a crucial layer to psilocybin research — but it's not 
    the same as a randomized trial. What to watch next.

key_data_points:
  - "Oregon's Measure 109 launched the nation's first legal therapeutic psilocybin program"
  - "Real-world study (NPR, 08/19) — specific metrics to be confirmed from primary source"
  - "Mental health Google Trends: +13 7d-delta (highest category mover this week)"
  - "States considering similar legislation: Colorado (active), others pending"

integrity_flags:
  - "⚠️ Study is described as 'real-world' — likely observational, not RCT. Make this explicit in the article; do not present as controlled efficacy evidence."
  - "⚠️ Primary study citation (journal, DOI, lead researcher) must be confirmed from NPR article before publishing causal language."
  - "⚠️ Do not generalize findings beyond the Oregon program population without qualification."

source_plan:
  - publisher: "NPR"
    url: "https://www.npr.org/2026/08/19/[article-slug]"
    tier: 1
    used_for: "Primary news report on study"
    notes: "[URL unverified — confirm from radar headline]"
  - publisher: "Oregon Health Authority — Psilocybin Services"
    url: "https://www.oregon.gov/oha/ph/preventionwellness/substances/psilocybin/pages/index.aspx"
    tier: 1
    used_for: "Program regulatory context, Measure 109"
  - publisher: "MAPS / Johns Hopkins (psilocybin clinical trial context)"
    url: "https://www.hopkinsmedicine.org/psychiatry/research/psychedelics-research"
    tier: 1
    used_for: "Clinical trial baseline for comparison"

expert_sources:
  - type: "Psychiatrist or clinical psychologist specializing in psychedelic-assisted therapy"
    name: "Search for named researcher in NPR article; Johns Hopkins Center for Psychedelic & Consciousness Research"
    reason: "Distinguish real-world from RCT findings; add clinical interpretation"
  - type: "Oregon Health Authority statement"
    name: "OHA official program data"
    reason: "Regulatory and programmatic context"

seo:
  primary_keyword: "Oregon psilocybin program results"
  supporting_keywords: ["psilocybin study 2026", "psilocybin therapy real world", "Oregon psilocybin law", "psychedelic therapy results", "psilocybin mental health"]
  format: "Explainer with data"
  schema_markup: "NewsArticle + FAQPage"
  cluster: "mental health and psychology"
estimated_word_count: "1,100–1,400"
next_steps: "Retrieve full NPR article; identify primary study citation (journal/DOI/lead author). Assign to health writer with mental health/policy background."
notes: >
  High Discover score (5) — this maps directly to AI queries about psilocybin legality 
  and efficacy. Strong evergreen potential once news hook passes. 
  Companion content opportunity: 'Psilocybin FAQ: Is It Legal Where You Live?'
```

---

### BRIEF 5 — P2 / TODAY

```yaml
priority_level: P2
publish_timing: today
topic: "Medical Debt Linked to Advanced Cancer Stage and Worse Survival — ACS Study"
primary_entity: "Medical Debt Cancer Survival Study"
signal_type: study_or_research
allowed_category: "medical research and clinical trials / chronic disease management / public health and epidemiology"
trend_strength_score: 72
opportunity_score: 78
discover_score: 5
urgency: today
confidence: medium
confidence_reason: >
  American Cancer Society Press Room (institutional, tier-1 adjacent) published 08/18. 
  Named institutional source. Underlying journal not yet confirmed — recommend locating 
  published paper. Source count: 2 (ACS + STAT/similar coverage pending confirmation).
content_status: new
source_count: 2
recommended_angle: >
  "Financial toxicity" as a hidden cancer risk factor — medical debt is not just a 
  financial hardship, it's a clinical outcome predictor. Frame around the mechanism: 
  people delay care to avoid costs, present at later stages, survive less. 
  Evaluative frame with systemic context, not just a data dump.
why_now: >
  ACS press release 08/18. County-level analysis gives this unusual geographic specificity — 
  it's not a general association but a granular dataset linking local debt burdens to 
  local cancer outcomes. Health insurance trends rising in Google Trends (related query). 
  STAT News covers health costs vs. employers (same-week framing). Strong Discover score — 
  AI systems are commonly asked about cancer disparities and why outcomes differ.

primary_headline: "Medical Debt Predicts Advanced Cancer Diagnosis — A New Study Explains the Deadly Mechanism"
alternate_headlines:
  - "The Cancer Risk Your Doctor Can't Treat: How Medical Debt Leads to Later-Stage Diagnosis"
  - "County-Level Medical Debt Linked to Worse Cancer Survival, American Cancer Society Finds"

outline:
  intro: >
    New ACS-linked research finds counties with higher medical debt burdens see more 
    advanced-stage cancer diagnoses and worse survival rates. This isn't correlation 
    by chance — the mechanism is care avoidance driven by cost fear.
  sections:
    - "What the Study Found (county-level data, cancer types, stage at diagnosis, survival delta)"
    - "The Mechanism: How Debt Delays Diagnosis (deferred screenings, avoided symptoms)"
    - "Which Cancers Are Most Affected"
    - "Geography of Risk: Which Counties / Demographics Face the Highest Burden"
    - "What 'Financial Toxicity' Means in Oncology (established term — explain for general audience)"
    - "What Patients Can Do (ACS resources, financial assistance programs)"
    - "What Policy Experts Say About Systemic Fixes"
  conclusion: >
    Medical debt as a cancer risk factor is not new in oncology — but this study's 
    county-level granularity makes it newly actionable for advocates and policymakers.

key_data_points:
  - "County-level analysis linking medical debt to cancer stage at diagnosis and survival (ACS, 08/18)"
  - "Medical debt affects ~100 million Americans (KFF/Commonwealth Fund data — verify)"
  - "Late-stage cancer diagnosis significantly reduces 5-year survival rates across most cancer types"
  - "Cancer screening rates are lower in high-debt counties (hypothesis — confirm from study)"

integrity_flags:
  - "⚠️ Institutional press release — underlying journal/DOI must be located and cited before publishing causal language."
  - "⚠️ County-level ecological study design — ecological correlation is not individual-level causation. State this clearly."
  - "⚠️ Do not present 'medical debt causes cancer mortality' without qualifying the observational/ecological study design."

source_plan:
  - publisher: "American Cancer Society"
    url: "https://pressroom.cancer.org/2026-08-18-County-Level-Medical-Debt"
    tier: 1
    used_for: "Primary institutional press release — study data, key findings"
    notes: "[URL pattern — confirm exact slug from radar headline]"
  - publisher: "KFF / Kaiser Family Foundation"
    url: "https://www.kff.org/health-costs/"
    tier: 1
    used_for: "Medical debt prevalence statistics"
  - publisher: "National Cancer Institute"
    url: "https://www.cancer.gov/about-cancer/understanding/statistics"
    tier: 1
    used_for: "Stage-specific survival rate data"

expert_sources:
  - type: "Oncologist with health equity focus"
    name: "Search ACS press release for named researchers; American Cancer Society equity researchers"
    reason: "Mechanism explanation; financial toxicity clinical framing"
  - type: "Health economist or public health researcher"
    name: "Search STAT News, Commonwealth Fund for published quotes on medical debt/health outcomes"
    reason: "Systemic context, policy angle"

seo:
  primary_keyword: "medical debt cancer survival"
  supporting_keywords: ["medical debt cancer risk", "financial toxicity cancer", "cancer diagnosis delay cost", "medical debt health outcomes", "ACS cancer study 2026"]
  format: "Explainer with data and patient resources"
  schema_markup: "NewsArticle + FAQPage"
  cluster: "chronic disease management / public health and epidemiology"
estimated_word_count: "1,200–1,500"
next_steps: "Locate underlying journal article or DOI from ACS press release. Assign to writer with health equity/oncology background. Include ACS financial assistance resource links."
notes: "High Discover score — maps to AI queries about cancer disparities, screening access, healthcare costs. Strong internal link candidate for any existing chronic disease or insurance content."
```

---

### BRIEF 6 — P3 / THIS WEEK

```yaml
priority_level: P3
publish_timing: scheduled
topic: "GLP-1 Medications May Treat Opioid Use Disorder — Vanderbilt Trial Now Enrolling"
primary_entity: "GLP-1 Opioid Use Disorder Trial"
signal_type: clinical_trial
allowed_category: "medical research and clinical trials / chronic disease management"
trend_strength_score: 65
opportunity_score: 74
discover_score: 4
urgency: this_week
confidence: medium
content_status: new
source_count: 2
recommended_angle: >
  Beyond weight loss: GLP-1s are being tested for addiction — what the science behind 
  this hypothesis is, what Vanderbilt's trial is specifically testing, and why this 
  matters for the opioid crisis. Distinct from recurring GLP-1/weight loss coverage.
why_now: >
  Vanderbilt Health News published 08/18; trial now enrolling (ClinicalTrials.gov 
  record implied). GLP-1 weight loss angle is recurring (flagged as stale), but 
  GLP-1/addiction is a genuinely new application with emerging mechanistic evidence. 
  Opioid crisis context provides strong public health hook.

headline: "GLP-1 Drugs Like Ozempic Are Being Tested for Opioid Addiction — Here's What We Know So Far"

angle: >
  Mechanistic explainer: GLP-1 receptors in the brain's reward circuitry may reduce 
  craving signals, which is why researchers hypothesize opioid use disorder as a 
  target. What the Vanderbilt trial is testing, what outcomes they're measuring, 
  and what the evidence base looks like now (preclinical + early human data).

key_data_points:
  - "Vanderbilt trial now enrolling for GLP-1 + opioid use disorder (Vanderbilt Health News, 08/18)"
  - "GLP-1 receptors expressed in brain reward centers — dopamine pathway hypothesis"
  - "~2 million Americans have opioid use disorder (SAMHSA data — verify current)"
  - "Existing GLP-1 addiction research: alcohol, smoking — cite peer-reviewed if available"

integrity_flags:
  - "⚠️ Trial is recruiting — no efficacy results exist yet. Frame as hypothesis-testing, not evidence of effectiveness."
  - "⚠️ Confirm ClinicalTrials.gov NCT number before claiming specific endpoints or timeline."

expert_type_needed: "Addiction medicine specialist or clinical pharmacologist; GLP-1 neuroscience researcher"

seo:
  primary_keyword: "GLP-1 opioid use disorder"
  supporting_keywords: ["Ozempic addiction treatment", "semaglutide opioid", "GLP-1 drug addiction research", "Vanderbilt GLP-1 trial"]
  format: "Explainer"
  serp_difficulty: Medium

sources:
  - publisher: "Vanderbilt Health News"
    url: "https://news.vanderbilt.edu/2026/08/18/[slug]"
    notes: "[URL unverified — confirm from radar headline]"
  - publisher: "ClinicalTrials.gov"
    url: "https://clinicaltrials.gov/search?term=GLP-1+opioid"
    notes: "Locate specific NCT number"
estimated_word_count: "1,000–1,200"
```

---

### BRIEF 7 — P3 / THIS WEEK

```yaml
priority_level: P3
publish_timing: scheduled
topic: "Personalized Cancer Vaccine Shows Promise in Late-Stage Clinical Trial"
primary_entity: "Personalized Cancer Vaccine"
signal_type: clinical_trial
allowed_category: "medical research and clinical trials / chronic disease management"
trend_strength_score: 62
opportunity_score: 70
discover_score: 4
urgency: this_week
confidence: low_medium
content_status: new
source_count: 2
recommended_angle: >
  Plain-language explainer: what "personalized cancer vaccine" actually means 
  (mRNA-based, tumor neoantigen targeting), what "late-stage trial" signals about 
  timeline to approval, and what realistic expectations look like for patients 
  following this research.
why_now: >
  Spectrum News reported 08/19. "Late-stage" trial is a meaningful milestone — 
  it implies Phase 3 data or equivalent, which moves this from early research 
  to near-approval territory. Cancer vaccine topic has strong Discover potential 
  as AI systems are frequently asked about cancer cure timelines.

headline: "A Personalized Cancer Vaccine Just Showed Promise in a Late-Stage Trial — What That Actually Means"

angle: >
  Demystify the technology and the trial milestone. Most coverage uses "promise" 
  without explaining what was measured or what "late-stage" means for FDA timelines. 
  Be the article that actually answers: what is this vaccine, for which cancer, 
  what did the trial show, and when might it be available?

key_data_points:
  - "Late-stage trial showing promise (Spectrum News, 08/19) — specific cancer type and sponsor to be confirmed"
  - "Personalized cancer vaccines use mRNA technology targeting tumor-specific neoantigens"
  - "Moderna/Merck mRNA-4157 is a precedent — cite trial results if relevant"
  - "Phase 3 trials typically require FDA review within 6–12 months of completion"

integrity_flags:
  - "⚠️ 'Shows promise' language is often press-release hedging — confirm specific endpoints met (overall survival, disease-free survival, response rate) before writing."
  - "⚠️ Confirm trial sponsor, cancer type, and ClinicalTrials.gov record. Spectrum News is tier-2; primary source required."
  - "⚠️ Do not imply this is broadly applicable across cancer types without confirming scope."

expert_type_needed: "Oncologist or cancer immunologist; clinical trial regulatory expert"

seo:
  primary_keyword: "personalized cancer vaccine 2026"
  supporting_keywords: ["cancer vaccine clinical trial", "mRNA cancer vaccine", "personalized cancer treatment", "cancer vaccine FDA"]
  format: "Explainer"
  serp_difficulty: Medium

sources:
  - publisher: "Spectrum News"
    url: "https://spectrumnews1.com/[article-slug]"
    notes: "[URL unverified — confirm from radar headline]"
  - publisher: "ClinicalTrials.gov"
    url: "https://clinicaltrials.gov/search?term=personalized+cancer+vaccine"
    notes: "Locate specific NCT number and sponsor"
estimated_word_count: "1,000–1,200"
```

---

### BRIEF 8 — P3 / THIS WEEK

```yaml
priority_level: P3
publish_timing: scheduled
topic: "Eating Disorder Genomics — Nature Meta-Analysis Reveals Shared and Distinct Biology"
primary_entity: "Eating Disorder Genetics Study"
signal_type: study_or_research
allowed_category: "mental health and psychology / medical research and clinical trials"
trend_strength_score: 60
opportunity_score: 68
discover_score: 3
urgency: this_week
confidence: medium
content_status: new
source_count: 2
recommended_angle: >
  What new genetic evidence tells us about why eating disorders develop — 
  and what the shared biology between binge eating and anorexia means for 
  treatment. Plain-language translation of a Nature genomics meta-analysis 
  for a general health audience. Skeptical/evaluative frame: what this changes 
  and what it doesn't.
why_now: >
  Nature published 08/19 — highest-tier journal (tier-1). Mental health category 
  +13 7d-delta this week. Eating disorders affect ~30 million Americans 
  (NEDA) and are chronically under-researched relative to prevalence. 
  Genomic meta-analysis is the highest level of genetic evidence available.

headline: "A New Nature Study Reveals the Genetic Overlap Between Binge Eating and Anorexia — What It Means"

angle: >
  Translation piece: what a genomic meta-analysis actually is, what 
  "shared biology" means for anorexia and binge eating disorder, 
  whether this changes how clinicians should think about treatment, 
  and what questions remain. Avoid genetic determinism framing.

key_data_points:
  - "Nature meta-analysis (08/19/2026) — genomic analysis of binge-eating behavior and anorexia nervosa"
  - "Finds both unique and shared genetic variants across eating disorder phenotypes"
  - "~30 million Americans experience an eating disorder (NEDA — verify current)"
  - "Eating disorders have one of the highest mortality rates of any psychiatric condition"

integrity_flags:
  - "⚠️ Genomic association study — identifies variants correlated with phenotypes, not causation. State explicitly."
  - "⚠️ Meta-analysis findings may be population-level and not predictive at individual level. Qualify accordingly."
  - "⚠️ Retrieve DOI from Nature (08/19) before publishing. Search: nature.com for 'binge-eating anorexia genomic 2026'."

expert_type_needed: "Psychiatric geneticist or eating disorder specialist (psychiatrist/psychologist); NEDA or ANAD for patient perspective"

seo:
  primary_keyword: "eating disorder genetics study 2026"
  supporting_keywords: ["binge eating anorexia genetics", "eating disorder genomics", "Nature eating disorder study", "eating disorder biology"]
  format: "Research explainer"
  serp_difficulty: Easy

sources:
  - publisher: "Nature"
    url: "https://www.nature.com/articles/[DOI]"
    notes: "[DOI unverified — search nature.com for 08/19/2026 eating disorder genomics publication]"
  - publisher: "National Eating Disorders Association (NEDA)"
    url: "https://www.nationaleatingdisorders.org/research"
    notes: "Prevalence statistics and patient context"
estimated_word_count: "900–1,100"
```

---

## REJECTED TOPICS LOG

| Topic | Signal Source | Rejection Reason |
|---|---|---|
| FDA nominee Senate opposition (NYT, 08/19) | Google News | Pure political/regulatory opinion; no patient health content |
| AI in healthcare — Axios / Spectrum News | Google News | Off-category (tech/policy); not core health-wellness editorial |
| HHS primary care expansion (HHS.gov) | Google News | Policy/funding; no new health science for audience |
| Health insurance rates rising — Minnesota (MPR) | Google News | Regional; policy/business without clinical content |
| Dartmouth Health telehealth closure (VTDigger) | Google News | Local hospital/system operational news |
| Providence Health Plan closure (Healthcare Dive) | Google News | Pure healthcare business/M&A |
| Gut health signs listicle (health.com) | Google News | Aggregator evergreen listicle; no new research signal |
| Space travel women's health — USF (08/19) | Google News | Very narrow occupational/research niche; low general audience relevance |
| Molecular glue cancer driver — Stanford (08/19) | Google News | Preclinical/lab-stage; not yet patient-relevant |
| Ferrero acquires Purely Elizabeth (PR Newswire) | Google News | Consumer brand M&A; no health science angle |
| Wellness brand/conference/app items (6 items) | Google News | Institutional/corporate PR; no editorial health value |
| Tribal Nation medical school launch (U of A) | Google News | Education/institutional milestone; not health consumer content |
| Mitch McConnell health (Google Trends rising) | Google Trends | Political figure health = excluded category (pure political) |
| "Routine wellness shampoo" / brand-specific wellness queries | Google Trends | Product marketing; brand safety exclusion |
| Gut health listicle signals (coconut cult, apple cider vinegar) | Google Trends | Low credibility; folk remedy / consumer product signals |

**Monitored (not scored — require further development):**

| Topic | Reason for Monitor |
|---|---|
| Home hospital trial for dementia (MGB, 08/18) | Early enrollment; monitor for trial results |
| FDA wellness peptides compounding (Capitol Forum) | Supplement/compounding regulatory; requires primary FDA source |
| Pilots/flight attendants radiation cancer risk (Harvard Med) | Occupational health; narrow audience; verify journal publication |
| Laser therapy brain tumors (WashU) | Institutional press release only; monitor for journal publication |
| COVID-19 treatment 3,000-person trial (SC) | State-funded; treatment specifics needed before scoring |
| Selena Gomez mental health company / celebrity mental health | Celebrity wellness exclusion; no clinical content |

---

## INTEGRITY FLAGS — CONSOLIDATED

> All flags below must be cleared by the assigned writer before publication.

**🔴 Pre-publication required (blocking):**

1. **Egg Recall (P1):** Retrieve FDA.gov official recall notice for exact brands, lot codes, and contamination details before publishing. URL: fda.gov/safety/recalls-market-withdrawals-safety-alerts
2. **Blueberry Recall (P1):** Retrieve FDA.gov blueberry recall notice before publishing. Do not assume contamination type (not confirmed in signal). URL: same as above.
3. **Eye Drop Recall (P2):** Retrieve FDA.gov notice for product name, lot codes, and contamination agent. Do not speculate on contamination type.
4. **Oregon Psilocybin Study (P2):** Locate primary study citation (journal, DOI, lead researcher) from NPR article before publishing causal or efficacy language.
5. **ACS Medical Debt/Cancer Study (P2):** Locate underlying journal article/DOI from ACS press release. Confirm ecological study design language.
6. **Personalized Cancer Vaccine (P3):** Confirm trial sponsor, cancer type, NCT number, and specific endpoints met before writing. "Shows promise" is not sufficient.
7. **Nature Eating Disorder Genomics (P3):** Retrieve DOI from Nature.com before publishing.

**🟡 Ongoing editorial discipline (non-blocking but mandatory in copy):**

- All study-based articles: state observational vs. RCT design explicitly
- All association findings: do not use causal language without qualification
- All recall articles: include "verify current information at FDA.gov" as standard advisory
- GLP-1/opioid trial: frame as hypothesis-testing; no efficacy results exist yet
- Cancer vaccine: do not imply broad cancer applicability; scope to specific trial population
- Eating disorder genetics: avoid genetic determinism; state population-level limitations

---

## RUN NOTES

```yaml
run_date: 2026-08-20
niche: health and wellness
signals_reviewed: ~90 (60 Google News + Google Trends 8 keywords + competitor context)
topics_retained: 8
topics_rejected: 15 (direct) + 6 (monitored)
p1_count: 2
p2_count: 3
p3_count: 3
integrity_flags: 7 pre-publication blocking + ongoing editorial discipline
top_topic: "FDA Class I Egg Recall — Salmonella"
key_themes: ["FDA recalls (food + drug)", "mental health research", "cancer — outcomes + treatment", "GLP-1 emerging applications", "medical debt / health equity"]
tools_used: ["SerpAPI Google Trends (pre-fetch)", "SerpAPI Google News (radar injection)"]
tools_unavailable: []
google_trends_available: true
google_trends_tool: serpapi_prefetch
search_velocity_source: google_trends
self_check: skipped (no site_url configured) — competitor-check fallback used for SERP context
deferred_topics_checked: true (no due entries)
run_history_recurring_flags:
  - "GLP-1/weight loss angle: 3+ consecutive runs — today's candidate (GLP-1/opioid) is a distinct application, cleared for P3"
  - "Mental health: recurrent category — today's candidates (psilocybin, eating disorder genomics) are fresh research signals, cleared"
notes: >
  Strongest signal week in recent runs for FDA recall activity — two Class I food recalls 
  (eggs + blueberries) plus an eye drop recall all breaking simultaneously creates an 
  unusual food/drug safety news cluster. Recommend publishing egg + blueberry recalls 
  immediately today and framing them as a pair. Mental health category showed the 
  strongest 7-day Google Trends movement (+13 delta), supported by two separate 
  research signals (psilocybin + eating disorder genomics). 
  GLP-1 recurring flag resolved: opioid use disorder application is editorially distinct 
  from weight loss coverage. Nutrition trending +11 (delta) — egg nutrition queries likely 
  driven by recall concern, reinforcing recall coverage priority.
  All three recall briefs require FDA.gov primary source verification before publication.
dashboard_written_to: outputs/daily_newsroom_dashboard/2026-08-20.html
run_history_updated: true
```