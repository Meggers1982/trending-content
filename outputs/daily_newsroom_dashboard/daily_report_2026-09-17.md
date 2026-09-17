# Trending Content OS — Daily Run
**Run date:** 2026-09-17 | **Niche:** Health & Wellness

---

## 1. Preflight Summary

```yaml
preflight_status:
  all_sections_present: true
  missing_sections: []
  site_niche_set: true
  target_audience_set: true
  site_url_set: false
  serpapi_connected: true
  google_trends_available: true
  google_trends_tool: serpapi_prefetch
  search_velocity_source: google_trends
  active_tools: [serpapi_news_search, serpapi_trends_prefetch, google_news_radar]
  inactive_tools: [reddit_api (unconfirmed), social_search (unconfirmed), content_database (disabled)]
  can_run_signal_listener: true
  notes: "site_url not configured — self-check skipped; competitor-list fallback (configs/competitor_list.yaml) used for SERP-gap/duplicate context. Google Trends and Google News Radar both live via pre-fetch."
next_action: run_signal_listener
```

**Deferred topics check:** `data/deferred_topics.yaml` had no entries with a passed `recheck_on` date.
**Recurring-theme check:** AI-in-clinical-medicine cluster, FDA recall cluster, and mental-health-awareness cluster have each appeared in 3+ consecutive runs (09-11 through 09-17) → flagged recurring/check-for-staleness this run.

---

## 2. Google News Radar Coverage Summary (144 unique headlines, 12 queries)

| Cluster | Disposition | Why |
|---|---|---|
| **AI-in-clinical-medicine** (WHO AI-for-Health meeting, [NYT: US health officials deploy medical AI](https://www.nytimes.com/2026/09/14/health/ai-doctors-medicare-fda.html), [FDA phase-1 pilot](https://www.fiercebiotech.com/biotech/fda-launches-pilot-program-speed-sluggish-phase-1-trials)) | **Existing — rejected** | Same story cluster covered 2026-09-16; no material new development today. |
| **FDA recall cluster** (hand soap Class II upgrade — [WGRZ](https://www.wgrz.com/article/news/nation-world/fda-hand-soap-recall-15-states-class-ii-warning/507-6c68423a-e212-4714-b8fd-2ce5ffba8631), [Fox 5 Atlanta](https://www.fox5atlanta.com/news/fda-recalls-hand-soaps-sold-georgia-over-bacteria-risk); epinephrine recall; Walmart berries) | **Existing/stale — rejected** | Hand soap and berries already covered 09-16/09-14; epinephrine recall ([NewsNation](https://www.newsnationnow.com/us-news/recalls/epinephrine-injection-recalled-health-risks-fda/)) dated 09-10, now 7 days old — exceeds recall freshness ceiling. |
| **Clinical trial operations/diversity** (Xavier Univ., PharmaVoice, FIU/Baptist, Applied Clinical Trials, Medscape) | **Rejected — off-category/edge** | Trade/industry-facing content, low relevance to general health-conscious consumer audience. |
| **Medical research cluster** (OHSU Huntington's/fasting, [Nature Medicine liquid biopsy](https://www.nature.com/articles/s41591-026-04625-x), Stanford brain model, Mayo minibeam radiotherapy, anti-seizure drug/childhood tumors, gender-differences study) | **Mixed** | 1 retained (Nature liquid biopsy — cleared thresholds); 4 monitored (thin single-source/narrow search demand); 1 rejected via 02b (anti-seizure drug claim — weak secondary sourcing). |
| **Wellness/lifestyle culture** (wellness darties, anti-optimization wave, campus wellness programs, [Time: benefits of reading](https://time.com/article/2026/09/16/health-benefits-reading-books-for-pleasure/)) | **Existing/saturated — rejected** | Wellness darties already covered 09-11/09-13; "benefits of reading" is a saturated evergreen SERP with no fresh angle identified. |
| **Infectious disease/outbreak** ([Ebola DRC/Uganda — ECDC](https://www.ecdc.europa.eu/en/ebola-outbreak-democratic-republic-congo-and-uganda), rabies exposure CDC notice) | **Mixed** | Ebola outbreak retained (new, not previously covered); rabies notice is a recycled repost of the 09-11 CDC HAN already covered — existing. |
| **Political/local/business** (Congressional Medicare hearing, Trump health-nominee Senate hearings, Mississippi rural health awards, Vermont hospital layoffs) | **Rejected — excluded categories** | Pure political healthcare opinion / local hospital & business news, per `category_rules.yaml`. |

---

## 3. Signal Summary

```yaml
signal_summary:
  run_started_at: "2026-09-17T00:00:00Z"
  run_completed_at: "2026-09-17T00:20:00Z"
  total_signals_reviewed: 153   # 144 news radar + 9 Trends keyword clusters
  total_signals_retained: 2
  total_rejected: 151
  google_trends_available: true
  search_velocity_source: google_trends
  rejection_breakdown:
    off_category: 9
    brand_safety: 1
    duplicate: 13
    weak_signal: 7
    unverified_claim: 3
    other: 5
  highest_priority_topic: "Ebola outbreak — DRC/Uganda (ECDC)"
  strongest_signal_source: "ECDC / Nature Medicine (tier-1 institutional + journal)"
  tools_unavailable: ["reddit_api (unconfirmed in this session)", "social_search (unconfirmed)"]
  notes: "A high proportion of today's radar overlaps with the last 3 days of coverage (recalls, AI-in-medicine, mental health). Several fresh single-institution research stories (OHSU/Huntington's, Mayo minibeam radiotherapy) had strong opportunity scores but failed the trend-strength floor (30-49 band) due to thin news volume/search velocity — routed to Monitor per Skill 04 rules rather than forced into the board."
```

---

## 4. Skill 02b — Health Claim Verification Gate Routing Summary

| Topic | Risk type | Gate result | Notes |
|---|---|---|---|
| Nature Medicine — liquid biopsy for pancreatic cancer | medical_study | **Pass** | Primary source = journal itself (DOI via nature.com/articles/s41591-026-04625-x). Claim matches source framing. |
| OHSU — intermittent fasting & Huntington's disease | medical_study | **Pass** (confidence capped) | Institutional press release from research institution; likely animal/preclinical model — flagged for human vs. animal caveat. Failed trend-strength floor downstream → routed to Monitor. |
| Mayo Clinic — minibeam radiotherapy trial | clinical_trial | **Pass** (confidence capped) | Tier-1 institutional press release, appropriately hedged ("first to study"). Failed trend-strength floor downstream → Monitor. |
| Medical Xpress — anti-seizure drug vs. childhood brain tumors | drug_or_treatment_claim | **Reject** | Secondary aggregator source, no visible named journal/DOI/institution in available evidence — fails "no secondary substitution" rule for drug/treatment claims. |
| EatingWell — FDA lead-leaching cookware warning | dosage_or_safety_guidance | **Reject** | No direct FDA.gov notice retrieved; secondary-only sourcing insufficient for safety-guidance claims per gate rule. |
| Citeline — Bausch + Lomb FDA warning (potential recall) | recall (speculative) | **Reject** | Single trade-press source, unconfirmed ("suggests potential recall"); does not meet 3-source breaking-recall exception. |
| News-Medical — gender differences in active medical treatment | medical_study | **Reject** | Thin aggregator source, no confirmed primary study traceability. |

---

## 5. Final Editorial Priority Board

```yaml
priority_board:
  - priority_level: P1
    publish_timing: immediate
    topic: "Ebola outbreak spreading across DRC and Uganda"
    primary_entity: "Ebola virus disease outbreak (DRC/Uganda)"
    signal_type: breaking_news
    allowed_category: "infectious disease"
    trend_strength_score: 59
    opportunity_score: 75
    discover_score: 4
    urgency: today
    confidence: medium
    content_status: new
    source_count: 1
    recommended_angle: "Explainer: what's actually happening in the DRC/Uganda Ebola outbreak, how it compares to past flare-ups, and what US travelers/public health readers should know"
    why_now: "ECDC issued an active outbreak communication 09/15; not previously covered, and outbreak status is evolving daily."
    primary_headline: "Ebola Outbreak Spreads in DRC and Uganda: What to Know Right Now"
    next_steps: "Assign immediately; corroborate case counts against WHO Disease Outbreak News feed before publishing (single-source in this pull)."
    notes: "⚠️ Confidence capped at Medium — only one institutional source (ECDC) captured in this run; verify against WHO/CDC before publishing."

  - priority_level: P2
    publish_timing: short_term
    topic: "New liquid biopsy method for early pancreatic cancer detection"
    primary_entity: "Liquid biopsy — pancreatic ductal adenocarcinoma (PDAC)"
    signal_type: study_or_research
    allowed_category: "medical research and clinical trials"
    trend_strength_score: 50
    opportunity_score: 75
    discover_score: 4
    urgency: today
    confidence: medium
    content_status: new
    source_count: 1
    recommended_angle: "What this new blood test could mean for catching one of the deadliest, hardest-to-detect cancers earlier"
    why_now: "Published in Nature Medicine 09/16 — one of the few concrete diagnostic advances on one of the lowest-survival cancers; no existing coverage found."
    primary_headline: "A New Blood Test May Catch Pancreatic Cancer Earlier — Here's What the Science Actually Shows"
    next_steps: "Pull full study for cohort size/validation stage; pair with a gastroenterologist or oncologist quote per Skill 08 sourcing rules."
    notes: "⚠️ Single-study finding — needs replication caveat; avoid implying diagnostic-ready/FDA-cleared."

  - priority_level: P5
    publish_timing: monitor
    topic: "Intermittent fasting shows promise in slowing Huntington's disease progression"
    primary_entity: "Huntington's disease / intermittent fasting (OHSU)"
    signal_type: study_or_research
    allowed_category: "chronic disease management"
    trend_strength_score: 43
    opportunity_score: 72
    discover_score: null
    urgency: this_week
    confidence: low
    content_status: new
    source_count: 1
    recommended_angle: "n/a — monitor only"
    why_now: "Fresh (09/17) but single-source institutional coverage, narrow search demand; likely preclinical/animal-model finding."
    primary_headline: "n/a"
    next_steps: "Recheck in 3 days for wider pickup/human-relevance clarification before scoring a full brief."
    notes: "⚠️ Passed 02b but failed trend-strength floor (30-49 band) — routed to Monitor per Skill 04 rule, not rejected outright."

  - priority_level: P5
    publish_timing: monitor
    topic: "Mayo Clinic pilots minibeam radiotherapy for difficult-to-treat cancers"
    primary_entity: "Minibeam radiotherapy (Mayo Clinic)"
    signal_type: clinical_trial
    allowed_category: "medical research and clinical trials"
    trend_strength_score: 44
    opportunity_score: 70
    discover_score: null
    urgency: this_week
    confidence: low
    content_status: new
    source_count: 1
    recommended_angle: "n/a — monitor only"
    why_now: "Tier-1 institutional source, appropriately early-stage framing, but thin search/news volume today."
    primary_headline: "n/a"
    next_steps: "Recheck for oncology trade-press pickup or patient-facing coverage before advancing."
    notes: ""

summary:
  total_topics: 4
  high_priority_count: 2
  immediate_actions: "Assign Ebola outbreak explainer today (P1); queue pancreatic cancer liquid biopsy piece (P2) for short-term publish, pending study-detail pull."
```

---

## 6. Editorial Briefs — Retained Candidates

### Brief 1 (P1 — Full Deep-Dive)

```yaml
brief:
  primary_headline: "Ebola Outbreak Spreads in DRC and Uganda: What to Know Right Now"
  alternate_headlines:
    - "Is Ebola Spreading? What the DRC/Uganda Outbreak Means Right Now"
    - "The Ebola Outbreak in Central Africa, Explained"
  topic: "Ebola outbreak — DRC and Uganda"
  primary_entity: "Ebola virus disease outbreak (DRC/Uganda)"
  search_intent: "informational + evaluative (is this a risk to me / how serious is it)"
  angle: "Straight explainer prioritizing what's confirmed vs. unconfirmed, prior outbreak comparison, and realistic US/global risk context — filling the gap where most coverage so far is wire-brief length."
  why_now: "ECDC issued an active outbreak notice 09/15/2026; not previously covered in this pipeline; outbreak status is actively evolving."
  integrity_flags:
    - "⚠️ Single-source verification in this pull (ECDC only) — cross-check case/death counts against WHO Disease Outbreak News and CDC travel notices before publishing."
    - "⚠️ Avoid alarmist framing on US risk — historically, DRC/Uganda outbreaks have not resulted in significant spread outside the region; state containment measures accurately."
  outline:
    intro: "What's confirmed about the current outbreak as of this week"
    sections:
      - "Where and when it started, case/death counts (sourced)"
      - "How this outbreak compares to prior DRC/Uganda Ebola flare-ups"
      - "Containment and response measures underway (WHO/ECDC/local health ministries)"
      - "Should US travelers or the general public be concerned?"
    conclusion: "What to watch for next and where to get verified updates"
  key_data_points:
    - "ECDC outbreak notice issued 2026-09-15 [URL unverified pending WHO cross-check]"
  source_plan:
    - { publisher: "ECDC", url: "https://www.ecdc.europa.eu/en/ebola-outbreak-democratic-republic-congo-and-uganda", tier: 1, used_for: "Primary outbreak notice" }
  evidence_requirements: "Moderate-heavy — outbreak case data must be sourced to WHO/CDC/ECDC directly, no secondary aggregation."
  expert_sources:
    - { type: "infectious disease epidemiologist", name: "TBD — cite WHO/CDC official statement", reason: "Public health risk context and containment credibility" }
  internal_links: []
  visual_brief: "Map graphic of affected DRC/Uganda regions; avoid stock images of hospital patients (fear-framing risk)."
  seo:
    primary_keyword: "Ebola outbreak DRC Uganda 2026"
    supporting_keywords: ["Ebola outbreak explained", "is Ebola spreading 2026", "Ebola virus disease Africa"]
    format: "News explainer"
    schema_markup: "NewsArticle"
    cluster: "infectious disease / outbreak tracking"
  discover_notes: "Strong AI-citation candidate if updated with confirmed case counts and named health authority quotes; currently capped by single-source status."
  key_takeaways: ["Outbreak confirmed active as of mid-September 2026", "Contained to DRC/Uganda region per current reporting", "US general public risk remains low per historical pattern"]
  estimated_word_count: "900-1,100"
execution_notes: "Verify against WHO before publish — do not rely on ECDC notice alone for case figures."
confidence: medium
```

### Brief 2 (P2 — Full Deep-Dive)

```yaml
brief:
  primary_headline: "A New Blood Test May Catch Pancreatic Cancer Earlier — Here's What the Science Actually Shows"
  alternate_headlines:
    - "Liquid Biopsy Could Detect Pancreatic Cancer Before Symptoms Appear"
    - "Why This New Pancreatic Cancer Test Is a Big Deal — and What It Isn't (Yet)"
  topic: "Liquid biopsy for early detection of pancreatic ductal adenocarcinoma"
  primary_entity: "Liquid biopsy — PDAC early detection"
  search_intent: "informational + evaluative"
  angle: "Ground the excitement in what the study actually found (stage, cohort, sensitivity/specificity) rather than repeating a breakthrough headline — pancreatic cancer's low survival rate makes overpromising especially risky."
  why_now: "Published in Nature Medicine 2026-09-16; addresses one of the deadliest, hardest-to-screen cancers; no existing site coverage."
  integrity_flags:
    - "⚠️ Single-study finding — note validation cohort size and whether results have been independently replicated."
    - "⚠️ Clarify this is a research finding, not an FDA-cleared diagnostic test available to patients today."
  outline:
    intro: "Why early pancreatic cancer detection has been such a hard problem"
    sections:
      - "What the new liquid biopsy method actually detected, and how"
      - "Study scope: cohort size, stage of disease studied, sensitivity/specificity"
      - "How far this is from clinical availability"
      - "What this means for high-risk patients today"
    conclusion: "Cautious optimism — a real advance, but early-stage"
  key_data_points:
    - "Published Nature Medicine, 2026-09-16, DOI via nature.com/articles/s41591-026-04625-x"
  source_plan:
    - { publisher: "Nature Medicine", url: "https://www.nature.com/articles/s41591-026-04625-x", tier: 1, used_for: "Primary study data" }
  evidence_requirements: "Heavy — peer-reviewed primary source required; pair with independent oncologist commentary."
  expert_sources:
    - { type: "gastroenterologist or oncologist", name: "TBD — cite study's named researcher or independent expert commentary", reason: "Clinical context on real-world applicability" }
  internal_links: []
  visual_brief: "Simple diagram of how liquid biopsy works (blood draw vs. traditional biopsy); avoid generic lab-coat stock photos."
  seo:
    primary_keyword: "pancreatic cancer early detection blood test"
    supporting_keywords: ["liquid biopsy pancreatic cancer", "new pancreatic cancer screening 2026", "pancreatic cancer blood test study"]
    format: "Research explainer"
    schema_markup: "NewsArticle"
    cluster: "medical research / cancer detection"
  discover_notes: "Strong AI-citation candidate — named entity (PDAC liquid biopsy), DOI-backed, durable topic, clear consumer-facing SERP gap since most coverage so far is trade-press level."
  key_takeaways: ["New blood-based test shows promise for earlier pancreatic cancer detection", "Still a research finding, not yet clinically available", "Pancreatic cancer's low survival rate makes early detection research especially high-stakes"]
  estimated_word_count: "800-1,000"
execution_notes: "Pull full study text for cohort/validation details before drafting; do not rely on headline alone."
confidence: medium
```

---

## 7. Rejected Topics Log

| Topic | Reason |
|---|---|
| FDA hand soap recall (Class II upgrade) | Existing — same recall covered 09-16; state-count/classification change is incremental, not a material new development |
| Walmart Great Value blueberries E. coli | Existing — covered 09-14 |
| Epinephrine injection recall | Stale — dated 09-10, exceeds recall freshness ceiling |
| AI-in-clinical-medicine cluster (WHO AI meeting, NYT Medicare AI, FDA phase-1 pilot) | Existing — covered 09-16, no new development |
| CDC rabies exposure notice (recycled) | Existing — covered 09-11 |
| WHO "Mental health at work" fact sheet | Existing — covered 09-16 |
| Nature youth mental health diagnoses review | Existing — covered 09-14 |
| Wellness darties (NYT) | Existing — covered 09-11/09-13 |
| Time — health benefits of reading a book | Rejected — trend_strength 35 (below floor), saturated evergreen SERP, no fresh angle |
| Anti-seizure drug vs. childhood brain tumors | Rejected via 02b — secondary aggregator, no primary sourcing for drug/treatment claim |
| FDA lead-leaching cookware warning | Rejected via 02b — no direct FDA notice retrieved; secondary-only sourcing insufficient for safety guidance |
| Bausch + Lomb FDA warning (potential recall) | Rejected via 02b — single trade source, speculative, fails breaking-recall exception |
| Gender differences in active medical treatment study | Rejected via 02b — thin aggregator source, no primary traceability |
| Multi4 Medical "landmark" clinical study (Yahoo Finance) | Rejected — promotional/investor-news framing, pharma business exclusion, brand safety flag |
| Clinical trial ops/diversity cluster (5 articles) | Rejected — off-category, B2B/trade audience, not consumer-facing |
| Rural Health Transformation Program funding (Mississippi) | Rejected — local/state government funding news, excluded category |
| Vermont hospital layoffs | Rejected — local hospital/business news, excluded category |
| Congressional Medicare payment hearing | Rejected — pure political healthcare policy |
| Senate hearing on Trump health nominees | Rejected — pure political |
| "CB1 blockers weight loss study" (Trends rising query) | Weak signal — search-only, no corroborating news source found; deferred for monitoring |

---

## 8. Integrity Flags (Consolidated)

- ⚠️ **Ebola outbreak brief**: single-source (ECDC) in this data pull — confirm case/death counts against WHO before publishing.
- ⚠️ **Liquid biopsy brief**: single-study finding — must include replication/validation caveat; do not imply FDA clearance or clinical availability.
- ⚠️ **OHSU Huntington's/fasting (Monitor)**: likely animal/preclinical model — any future brief must explicitly qualify human relevance.
- ⚠️ **Mayo minibeam radiotherapy (Monitor)**: early-stage/first-in-patients study — avoid framing as an established treatment option.

---

## 9. Run Notes

- Slow/recycled news day: a majority of today's radar overlapped with the prior 6 days of coverage (recalls, AI-in-medicine, mental health awareness) — flagged as recurring per staleness check.
- Several fresh, single-institution research stories (Huntington's/fasting, Mayo minibeam radiotherapy) had strong opportunity scores (70-72) but were correctly routed to Monitor rather than the board because trend_strength fell in the 30-49 band — this reflects thin news/search volume, not a scoring error.
- `site_url` not configured — duplicate/SERP-gap checks used competitor-list fallback (`configs/competitor_list.yaml`) rather than direct self-check.
- Run archived to `data/run_history.yaml`; dashboard written to `outputs/daily_newsroom_dashboard/2026-09-17.html`.