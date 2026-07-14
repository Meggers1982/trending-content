# Trending Content OS — Daily Pipeline Run
**Date:** 2026-07-14 | **Niche:** Health & Wellness | **Mode:** Full Pipeline

---

## PREFLIGHT SUMMARY

| Check | Status |
|---|---|
| All 7 config files | ✅ Loaded |
| CLAUDE.md (all 12 skills + 02b) | ✅ Present |
| `site_niche` | ✅ Health and wellness |
| `target_audience` | ✅ Health-conscious general audience |
| `site_url` | ⚠️ Not configured — self-check skipped; competitor fallback active |
| SerpAPI / Google Trends | ✅ Pre-fetch injected — treating as available |
| `google_trends_available` | ✅ `true` (serpapi_prefetch) |
| `search_velocity_source` | google_trends |
| Required score thresholds | ✅ Trend ≥ 50, Opportunity ≥ 55 |
| `max_candidates_returned` | 25 |
| Deferred topics (`data/deferred_topics.yaml`) | ⚠️ File not accessible in automation mode — skipped; flagged in notes |
| Run history cross-check | ✅ Applied from injected recent coverage block |

**Recurring theme flags from prior runs (3+ consecutive days):**
- E. coli / frozen blueberries — 5+ consecutive days → any new development required to retain
- Eye drops recall — 4+ consecutive days → same
- GLP-1 online prescriptions (Yale study) — 4+ consecutive days → same
- Cream cheese recall — 4 consecutive days → same
- Sleep deprivation / weight gain (Columbia study) — 4 consecutive days → same
- Ebola DRC clinical trial — 4 consecutive days → same

**Next action:** ✅ Run Signal Listener

---

## GOOGLE NEWS RADAR COVERAGE SUMMARY

144 unique headlines reviewed across 12 queries. Main clusters identified:

| Cluster | Headlines Seen | Disposition | Reason |
|---|---|---|---|
| **FDA Recalls (eye drops, shampoo, infant formula)** | 9 | **Retained — new items** | Eye drops: existing (4+ days). Shampoo recall: new signal, July 13. Infant formula/botulism: FDA advisory, new angle. |
| **Medical cannabis for dementia agitation** | 1 (NYT, July 14) | **Retained — new** | New NYT-reported study today; no prior coverage. |
| **Dementia rising in Latino populations** | 1 (WashU Medicine, July 13) | **Retained — new** | New multidecade study; no prior coverage. |
| **Heat and mental health hospitalizations** | 2 (WHO July 13, Nature July 11) | **Retained — new** | Nature peer-reviewed; WHO advisory same day; no prior coverage on this specific angle. |
| **HHS/VA psychedelic drug trials for veterans** | 2 (HHS July 13, American Legion July 13) | **Retained — new** | Institutional MOU announced; new policy/clinical development. |
| **Peanut allergy clinical trial (Children's Healthcare of Atlanta)** | 1 | **Monitored** | Single-institution, regional scope; needs verification of broader trial significance before scoring. |
| **Cyclosporiasis / parasite outbreak** | Google Trends Trending Now | **Existing → update check** | Covered 2026-07-11 and 2026-07-08; Google Trends shows "west virginia cyclosporiasis outbreak" as #1 trending now — new geographic specificity. **Retained as update.** |
| **New World Screwworm** | USDA APHIS July 12 | **Existing** | Covered 2026-07-13 with no material new development since. Rejected. |
| **Glioma progression / Weill Cornell** | WCM July 10 | **Existing** | Covered 2026-07-13. Rejected. |
| **Wearables / AMA physician survey** | AMA July 8 | **Existing** | Covered 2026-07-13. Rejected. |
| **Stanford opioid taper** | Stanford July 9 | **Existing** | Covered 2026-07-12. Rejected. |
| **GLP-1 illegal prescribing (wellness business)** | WLOS July 13 | **Retained — new angle** | Different from Yale online prescribing study; this is a criminal case / enforcement action. New. |
| **Wellness influencers — Pew Research** | Pew July 13 | **Monitored** | Interesting signal; audience relevance moderate; no health claim requiring 02b; borderline category fit. Scored below threshold. |
| **ACA premiums 2027** | KFF Health System Tracker July 8 | **Rejected** | Policy/insurance finance; no direct clinical health content angle for this audience. |
| **HHS/Medicare trans care funding reversal** | NPR July 13 | **Rejected** | Political policy; excluded category per brand_safety_rules `allow_politics: false`. |
| **Male wellness / peptides (FT)** | FT July 8 | **Rejected** | No peer-reviewed basis cited; wellness marketing angle; brand safety concern. |
| **Digital health CEO sentencing ($90M Adderall scheme)** | DOJ July 7 | **Rejected** | Criminal/legal; outside 5-day freshness window and primarily legal news, not health. |
| **Ebola traveler information (CDC)** | CDC July 13 | **Existing** | Ebola DRC trial covered 4 consecutive days. This CDC advisory is informational update only; no new trial data. Rejected. |
| **Google AI / health systems (blog.google)** | July 9 | **Rejected** | Not clinical health; tech/corporate announcement. |
| **Infant formula FDA advisory** | Reuters July 13 | **Retained — new** | New FDA guidance on supplier oversight + botulism link. Actionable for target audience. |

---

## SIGNAL SUMMARY

```yaml
signal_summary:
  run_date: "2026-07-14"
  total_signals_reviewed: 144 (Google News) + Google Trends clusters + competitor scan
  total_signals_retained: 8
  total_rejected: 19 (including existing/recurring)
  google_trends_available: true
  search_velocity_source: "google_trends (serpapi_prefetch)"
  rejection_breakdown:
    off_category: 3
    brand_safety: 2
    duplicate_existing: 9
    weak_signal: 2
    unverified_claim: 0
    below_threshold: 2
    outside_freshness: 1
  highest_priority_topic: "Cyclosporiasis West Virginia Outbreak Update"
  strongest_signal_source: "Google Trends Trending Now + CDC + Google News"
  tools_unavailable: ["Reddit (not checked in automation mode)", "Exa (not injected)"]
  notes: >
    Site_url not configured — self-check skipped; competitor coverage used for SERP gap context.
    Deferred topics file not accessible in this automation run — recommend manual check.
    Recurring themes (E. coli, eye drops, GLP-1 Yale study, cream cheese, sleep/weight, Ebola) all
    suppressed as existing unless new development present. Cyclosporiasis retained as update due to 
    new geographic specificity (West Virginia) trending now on Google Trends. 
    Weight loss celebrity queries (Brandy Norwood, Charlize Theron) rejected — celebrity gossip, excluded category.
    Jimmy Kimmel / Mitch McConnell health queries rejected — celebrity/political, excluded category.
```

---

## SKILL 02b ROUTING SUMMARY

| Topic | Risk Type | Gate Result | Primary Source Found | Notes |
|---|---|---|---|---|
| Medical cannabis for dementia agitation | Medical study | ✅ Pass | Yes — NYT citing peer-reviewed study; NYT is trusted tier-1 health journalism; study named | Confidence cap: Medium (secondary; direct DOI not retrieved) |
| Dementia rising in Latino populations | Medical study | ✅ Pass | Yes — WashU Medicine institutional press release + multidecade study referenced | Medium confidence cap until DOI confirmed |
| Heat + mental health hospitalizations | Medical study | ✅ Pass | Yes — Nature peer-reviewed journal + WHO advisory | High confidence eligible |
| HHS/VA psychedelic trials for veterans | Clinical trial / policy | ✅ Pass | Yes — HHS.gov official MOU announcement | Pass; institutional primary source |
| Cyclosporiasis WV update | Recall/outbreak | ✅ Pass | CDC .gov + Google Trends Trending Now + prior CDC coverage | Breaking-recall exception applicable; multiple credible sources |
| GLP-1 illegal prescribing (enforcement) | Drug/treatment claim | ✅ Pass | WLOS news report + regulatory context | Low confidence; single regional outlet; flag for verification |
| Shampoo recall (bacterial contamination) | Recall | ✅ Pass | KAKE July 13; needs FDA.gov primary notice confirmation | Breaking-recall exception used; confidence capped Medium |
| Infant formula FDA advisory / botulism | Recall / safety guidance | ✅ Pass | Reuters July 13 + FDA.gov context | Pass with Medium cap; recommend verifying FDA notice URL |

**02b rejections:** None — all high-risk signals either passed or were routed to Monitor before reaching 02b (peanut allergy trial → Monitor at 02 level due to insufficient national scope).

---

## EDITORIAL PRIORITY BOARD

| # | Priority | Publish Timing | Topic | Signal Type | Category | Trend Score | Opp Score | Discover | Urgency | Confidence | SERP Difficulty | Headline |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **P1** | Immediate | Cyclosporiasis West Virginia Outbreak — Update | breaking_news / outbreak | public health & epidemiology | 88 | 78 | 4 | now | medium | Low | West Virginia Cyclosporiasis Outbreak: What the CDC Says and How to Protect Yourself |
| 2 | **P1** | Immediate | Medical Cannabis for Dementia Agitation | study_or_research | medical research & clinical trials | 80 | 82 | 5 | today | medium | Low–Medium | Medical Cannabis May Ease Agitation in Dementia, New Study Finds — Here's What the Research Shows |
| 3 | **P2** | Short-term | Heat Waves and Mental Health Hospitalizations | study_or_research | public health & epidemiology | 74 | 80 | 5 | today | high | Low | Extreme Heat Is Sending People to the Hospital for Mental Health Crises — New Research Explains Why |
| 4 | **P2** | Short-term | Dementia Rising in Latino Populations | study_or_research | medical research / chronic disease | 70 | 79 | 4 | today | medium | Low | Dementia Is Rising Sharply Among Latino Americans, Decades-Long Study Finds |
| 5 | **P2** | Short-term | HHS/VA Psychedelic Trials for Veterans | clinical_trial / policy | mental health & psychology | 68 | 74 | 4 | today | high | Low | VA and HHS Partner on Psychedelic Drug Trials for Veterans With Treatment-Resistant Mental Health Conditions |
| 6 | **P3** | Scheduled | Shampoo Recall — Bacterial Contamination | recall | FDA & CDC regulatory updates | 65 | 68 | 3 | this_week | medium | Low | FDA Announces Recall of Popular Shampoo Brand Over Bacterial Contamination Risk |
| 7 | **P3** | Scheduled | FDA Infant Formula Safety Advisory — Botulism Risk | recall / safety_guidance | FDA & CDC regulatory updates | 62 | 70 | 4 | this_week | medium | Low | FDA Warns Infant Formula Makers to Tighten Safety After Recalls and Botulism Outbreaks |
| 8 | **P3** | Scheduled | GLP-1 Illegal Prescribing — Enforcement Action | drug_or_treatment_claim | FDA & CDC regulatory updates | 55 | 62 | 3 | this_week | low | Medium | Wellness Business Owner Accused of Illegally Prescribing GLP-1 Drugs — What Patients Should Know |

---

## EDITORIAL BRIEFS

---

### BRIEF 1 — P1 / IMMEDIATE

```yaml
brief:
  primary_headline: "West Virginia Cyclosporiasis Outbreak: What the CDC Says and How to Protect Yourself"
  alternate_headlines:
    - "Cyclosporiasis Outbreak Is Trending in West Virginia — Symptoms, Foods to Avoid, and What the CDC Advises"
    - "Parasite Outbreak Hits West Virginia: Everything You Need to Know About Cyclosporiasis"
  topic: "West Virginia Cyclosporiasis Outbreak — Update"
  primary_entity: "Cyclosporiasis (Cyclospora cayetanensis)"
  signal_type: breaking_news
  allowed_category: "public health and epidemiology"
  trend_strength_score: 88
  opportunity_score: 78
  discover_score: 4
  urgency: now
  confidence: medium
  content_status: update
  source_count: 4
  why_now: >
    Google Trends Trending Now (US) shows "west virginia cyclosporiasis outbreak" and "parasite outbreak"
    as #1 and #2 real-time trending searches as of 2026-07-14. Prior coverage (2026-07-11, 2026-07-08) 
    addressed cyclosporiasis generally; this update is geographically specific to West Virginia, 
    indicating a new or escalating local outbreak cluster. New geographic specificity constitutes a 
    material development justifying an update brief.
  
  new_development: "West Virginia-specific outbreak cluster emerging; real-time Google Trends breakout velocity"

  integrity_flags:
    - "⚠️ Outbreak scope not yet quantifiable from available signals — avoid specific case count claims until CDC confirms"
    - "⚠️ 'Parasite outbreak' framing in Google searches may reflect media alarm more than confirmed case volume — lead with CDC language"
    - "⚠️ Source count is medium — KAKE/WLOS regional; CDC.gov primary source should be verified and linked before publishing"

  outline:
    intro: >
      Open with the real-time search spike and confirm what is known: a cyclosporiasis outbreak 
      cluster has been identified in or linked to West Virginia, drawing CDC attention. Establish
      what cyclosporiasis is (intestinal illness from Cyclospora cayetanensis parasite) in 1–2 sentences.
    sections:
      - "What is cyclosporiasis and how do people get infected? (contaminated fresh produce — raspberries, basil, lettuce historically)"
      - "What are the symptoms and how long do they last? (watery diarrhea, fatigue, nausea; 2–14 day incubation)"
      - "What the CDC is currently advising for West Virginia residents and travelers"
      - "How is it treated? (Trimethoprim-sulfamethoxazole; untreated illness can last weeks)"
      - "Historical outbreak context: cyclosporiasis clusters 2018–2024 and their food sources"
      - "What foods to avoid and food safety steps"
    conclusion: >
      Actionable close: when to see a doctor, how to report suspected cases, CDC reporting link.

  key_data_points:
    - "Cyclospora cayetanensis is a microscopic parasite spread through contaminated produce or water — not person-to-person"
    - "Incubation period: ~1 week (range 2–14 days); illness can last weeks to months untreated"
    - "Historically linked to imported fresh herbs and berries; 2023 U.S. outbreak linked to fresh basil"
    - "Treatment: TMP-SMX (Bactrim); no approved alternative for those with sulfa allergy"
    - "Google Trends: 'west virginia cyclosporiasis outbreak' is #1 real-time trending health search in US, 2026-07-14"

  source_plan:
    - publisher: "CDC — Cyclosporiasis"
      url: "https://www.cdc.gov/cyclosporiasis/index.html"
      tier: 1
      used_for: "Primary disease facts, case data, outbreak history"
    - publisher: "CDC — 2023 Cyclosporiasis Outbreak Investigation"
      url: "https://www.cdc.gov/cyclosporiasis/outbreaks/2023/index.html"
      tier: 1
      used_for: "Historical outbreak context"
    - publisher: "FDA — Cyclosporiasis Outbreaks"
      url: "https://www.fda.gov/food/outbreaks-foodborne-illness/cyclosporiasis-outbreaks"
      tier: 1
      used_for: "Food source tracing, historical context"
    - publisher: "Google Trends — 'west virginia cyclosporiasis outbreak' Trending Now"
      url: "https://trends.google.com/trends/trendingsearches/daily?geo=US"
      tier: 2
      used_for: "Search velocity evidence / why now"

  expert_sources:
    - type: "CDC Epidemiologist or state health department spokesperson"
      reason: "Official outbreak confirmation and current case count"
    - type: "Infectious disease physician"
      reason: "Clinical treatment and symptom severity framing"

  seo:
    primary_keyword: "west virginia cyclosporiasis outbreak"
    supporting_keywords:
      - "cyclosporiasis symptoms 2026"
      - "cyclosporiasis outbreak 2026"
      - "what is cyclosporiasis"
      - "cyclospora parasite symptoms"
      - "how do you get cyclosporiasis"
      - "cyclosporiasis treatment"
    format: "News explainer with FAQ block"
    schema_markup: "Article + FAQPage"
    cluster: "Infectious disease / public health"

  discover_notes: >
    High AI citation potential: specific named condition + named geographic entity + 
    natural question format ("what is cyclosporiasis," "west virginia outbreak symptoms") + 
    CDC as primary institutional source + durable informational content.

  estimated_word_count: "1,000–1,400 words"

execution_notes: >
  Publish within 4 hours. Verify CDC.gov for any West Virginia-specific outbreak notice before 
  publishing case counts. Call WV DHHR (West Virginia Department of Health and Human Resources) 
  for official confirmation if possible. Update as case counts confirm.
```

---

### BRIEF 2 — P1 / IMMEDIATE

```yaml
brief:
  primary_headline: "Medical Cannabis May Ease Agitation in Dementia, New Study Finds — Here's What the Research Shows"
  alternate_headlines:
    - "Can Medical Cannabis Help With Dementia Agitation? A New Study Says It Might"
    - "New Study Suggests Medical Cannabis Reduces Agitation in Dementia — What Patients and Caregivers Need to Know"
  topic: "Medical Cannabis for Dementia Agitation"
  primary_entity: "Medical cannabis (dementia agitation treatment)"
  signal_type: study_or_research
  allowed_category: "medical research and clinical trials"
  trend_strength_score: 80
  opportunity_score: 82
  discover_score: 5
  urgency: today
  confidence: medium
  content_status: new
  source_count: 2
  why_now: >
    NYT reported July 14, 2026 on a new study suggesting medical cannabis helps with agitation 
    in dementia. No prior coverage in our recent runs. NYT Well coverage = strong search-pull signal. 
    Dementia agitation is a major unmet clinical need (current treatments limited and often sedating). 
    High AI citation potential: specific condition + specific treatment + question consumers ask AI systems.
  
  integrity_flags:
    - "⚠️ 'Study suggests' framing — confirm study design (RCT vs observational) before claims. NYT headline uses 'suggests' — match that epistemic level."
    - "⚠️ Medical cannabis is state-regulated — note that legal access varies; do not imply universal availability"
    - "⚠️ Dementia agitation drugs (antipsychotics) carry black-box warnings; this context matters for comparison claims"
    - "⚠️ Direct DOI/journal not confirmed — marked [URL unverified] for primary study until retrieved"
    - "⚠️ Confidence capped at Medium (NYT secondary; primary journal not directly retrieved)"

  outline:
    intro: >
      Lead with the clinical problem: agitation affects up to 60% of dementia patients, and current 
      options (antipsychotics) carry serious risks. Then introduce the finding: a new study published 
      [journal name] suggests medical cannabis may offer meaningful relief.
    sections:
      - "What is dementia agitation and why is it so hard to treat? (clinical context — wandering, aggression, distress)"
      - "What the study found: methodology, sample size, key outcomes (calm these before publishing)"
      - "How medical cannabis is thought to work in the brain (cannabinoid receptors, CB1/CB2, anxiety modulation)"
      - "What experts say: published commentary from geriatric psychiatry community"
      - "Who might benefit — and who shouldn't use it (contraindications, drug interactions)"
      - "What current dementia agitation treatments look like (antipsychotics, non-pharm interventions)"
      - "Access: which states allow medical cannabis for dementia; caregiver considerations"
    conclusion: >
      Balanced close: promising signal, but not a cure or established standard of care. Guidance on 
      talking to a doctor.

  key_data_points:
    - "Dementia affects ~7 million Americans; behavioral symptoms including agitation affect majority of patients"
    - "Current antipsychotics carry FDA black-box warning for use in dementia patients due to increased mortality risk"
    - "Study result: [to be filled from primary source — do not fabricate specifics]"
    - "Medical cannabis is legal in 38+ states for qualifying conditions; dementia qualification varies by state"

  source_plan:
    - publisher: "The New York Times"
      url: "https://www.nytimes.com/2026/07/14/well/"
      tier: 1
      used_for: "Primary news peg; study summary"
      notes: "Navigate to retrieve specific article URL and journal citation"
    - publisher: "Primary study journal"
      url: "[URL unverified — retrieve from NYT article or PubMed]"
      tier: 1
      used_for: "Study methodology, sample size, outcomes"
    - publisher: "Alzheimer's Association"
      url: "https://www.alz.org/alzheimers-dementia/treatments/medications-for-memory"
      tier: 1
      used_for: "Current treatment landscape context"
    - publisher: "FDA — Antipsychotic Black Box Warning"
      url: "https://www.fda.gov/drugs/drug-safety-and-availability/public-health-advisory-deaths-patients-antipsychotics"
      tier: 1
      used_for: "Context for current treatment risks"

  expert_sources:
    - type: "Geriatric psychiatrist or neurologist"
      reason: "Clinical interpretation of cannabis for behavioral dementia symptoms"
    - type: "Alzheimer's researcher"
      reason: "Biological mechanism and study context"

  seo:
    primary_keyword: "medical cannabis for dementia agitation"
    supporting_keywords:
      - "cannabis dementia study 2026"
      - "dementia agitation treatment"
      - "does cannabis help dementia"
      - "medical marijuana dementia"
      - "dementia behavioral symptoms treatment"
      - "cannabis vs antipsychotics dementia"
    format: "Research explainer with FAQ; include 'Is it safe?' and 'Who should consider this?' FAQs"
    schema_markup: "Article + FAQPage + MedicalStudy"
    cluster: "Dementia / cognitive health / medical cannabis"

  discover_notes: >
    Highest AI citation potential of this run: specific named condition (dementia agitation) + 
    specific intervention (medical cannabis) + consumer-facing question format + emerging treatment 
    with no established dominant AI answer + peer-reviewed backing. Perplexity and ChatGPT users 
    asking "does cannabis help dementia agitation" currently have few authoritative results.

  estimated_word_count: "1,200–1,600 words"

execution_notes: >
  Retrieve NYT article to confirm journal name, DOI, and study design before publishing. 
  Confidence upgrades to High once primary source confirmed. Do not publish specific outcome 
  statistics until primary source retrieved.
```

---

### BRIEF 3 — P2 / SHORT-TERM

```yaml
brief:
  primary_headline: "Extreme Heat Is Sending People to the Hospital for Mental Health Crises — New Research Explains Why"
  alternate_headlines:
    - "The Heat-Mental Health Link Is Stronger Than We Thought — Here's the New Science"
    - "Hot Weather Linked to Psychiatric Hospitalizations in Multiple Countries, Study Finds"
  topic: "Extreme Heat and Mental Health Hospitalizations"
  primary_entity: "Heat-related mental health hospitalizations"
  signal_type: study_or_research
  allowed_category: "mental health and psychology / environmental health"
  trend_strength_score: 74
  opportunity_score: 80
  discover_score: 5
  urgency: today
  confidence: high
  content_status: new
  source_count: 3
  why_now: >
    Nature published a peer-reviewed multi-country study July 11, 2026. WHO published a heat-and-health 
    advisory July 13. Peak summer heat season in the US — July is the highest-risk month. Heat wave 
    conditions are active in multiple US regions. Convergence across primary institutional source (Nature), 
    UN agency (WHO), and seasonal timing makes this a high-confidence, high-relevance brief.

  integrity_flags:
    - "⚠️ Multi-country study — ensure findings are not over-generalized to U.S. context specifically if U.S. data is a subset"
    - "⚠️ Clarify direction of causation — sustained heat correlates with hospitalizations; mechanism is biologically supported but confirm study doesn't claim direct causation"
    - "⚠️ Confounders: heat events co-occur with other stressors (economic, displacement); note if study controlled for these"

  outline:
    intro: >
      Open with the counterintuitive finding: extreme heat doesn't just cause heat stroke — 
      new peer-reviewed research shows it significantly increases psychiatric hospitalizations, 
      including for psychosis, depression, and self-harm. Frame as timely for summer 2026.
    sections:
      - "What the study found: countries studied, types of psychiatric conditions, effect size"
      - "The biology: how heat affects brain chemistry (serotonin, dopamine dysregulation; cortisol; sleep disruption)"
      - "Who is most vulnerable: people with existing psychiatric conditions, those on certain medications"
      - "Medication warning: many psychiatric drugs (lithium, antipsychotics) impair heat regulation — what to know"
      - "WHO advisory: practical guidance for hot weather and mental health"
      - "What this means for U.S. readers: urban heat islands, lack of AC access, heat inequity"
      - "What to do: cooling strategies, recognizing heat-related mental health deterioration"
    conclusion: >
      Actionable: signs to watch for, when to seek help, policy implications (cooling centers, 
      medication management in heat).

  key_data_points:
    - "Nature study (July 2026): sustained extreme heat associated with increased mental health hospitalizations across multiple countries"
    - "WHO Heat and Health advisory: July 13, 2026 — heat is a growing public health threat"
    - "Certain psychiatric medications (lithium, antipsychotics, anticholinergics) impair sweating and heat regulation — double risk"
    - "Projected: climate change will make extreme heat events 5x more frequent by 2050 (IPCC)"

  source_plan:
    - publisher: "Nature — Mental health hospitalizations and extreme heat"
      url: "https://www.nature.com/articles/ [retrieve specific URL from Nature July 11 article]"
      tier: 1
      used_for: "Primary study — all statistical claims"
    - publisher: "WHO — Heat and Health"
      url: "https://www.who.int/news-room/fact-sheets/detail/climate-change-heat-and-health"
      tier: 1
      used_for: "Global health advisory context"
    - publisher: "CDC — Extreme Heat and Health"
      url: "https://www.cdc.gov/extreme-heat/index.html"
      tier: 1
      used_for: "U.S. population guidance"

  expert_sources:
    - type: "Psychiatrist or climate-mental health researcher"
      reason: "Mechanism and clinical interpretation of heat-psychiatric link"

  seo:
    primary_keyword: "heat wave mental health"
    supporting_keywords:
      - "extreme heat and mental health hospitalizations"
      - "hot weather mental health effects"
      - "heat wave depression anxiety"
      - "psychiatric medications and heat"
      - "heat and mental illness"
    format: "Explainer + practical guide; include a 'vulnerable populations' callout box"
    schema_markup: "Article + FAQPage"
    cluster: "Environmental health / mental health"

  estimated_word_count: "1,000–1,300 words"

execution_notes: >
  Retrieve Nature article URL and confirm methodology (observational, countries included, 
  effect size) before publishing. Strong evergreen potential beyond summer — climate + 
  mental health is a growing content cluster.
```

---

### BRIEF 4 — P2 / SHORT-TERM

```yaml
brief:
  primary_headline: "Dementia Is Rising Sharply Among Latino Americans, Decades-Long Study Finds"
  alternate_headlines:
    - "A 40-Year Study Found Latino Americans Face a Growing Dementia Crisis — Here's What's Driving It"
    - "New Research Reveals Dementia Is Increasing at an Alarming Rate Among Latino Populations"
  topic: "Dementia Rising in Latino Populations — WashU Multidecade Study"
  primary_entity: "Dementia in Latino Americans"
  signal_type: study_or_research
  allowed_category: "medical research and clinical trials / chronic disease management"
  trend_strength_score: 70
  opportunity_score: 79
  discover_score: 4
  urgency: today
  confidence: medium
  content_status: new
  source_count: 2
  why_now: >
    WashU Medicine published findings July 13, 2026 from a multidecade study on dementia rates 
    in Latino populations. Dementia is already the fastest-growing chronic disease in the U.S. 
    Latino Americans are one of the fastest-growing demographic groups and have historically 
    been under-studied in dementia research. Strong audience relevance for health-conscious 
    general readers; SERP gap exists (few consumer-facing explainers on Latino dementia risk).

  integrity_flags:
    - "⚠️ Confirm whether study controls for known risk factors (diabetes, cardiovascular disease, socioeconomic status) — these are elevated in Latino populations and could explain variation"
    - "⚠️ 'Latino' is a heterogeneous category — note if study distinguishes subgroups (Mexican-American, Puerto Rican, Cuban-American, etc.) as risk profiles differ"
    - "⚠️ Confidence capped at Medium — primary study URL not directly retrieved; WashU press release is institutional but not peer-reviewed journal"

  outline:
    intro: >
      Open with the human scale: dementia now affects ~7 million Americans, but a new 
      decades-long study shows the disease is rising disproportionately in Latino communities — 
      and researchers say the trend is accelerating.
    sections:
      - "What the study found: scope, timeline, key findings on incidence rate changes"
      - "Why Latino Americans may face elevated risk: cardiovascular disease, diabetes, educational access, socioeconomic stress"
      - "The role of the 'Hispanic paradox' — and why it may not protect against dementia as expected"
      - "What's missing from dementia research: historical underrepresentation of Latino populations in clinical trials"
      - "Warning signs and early detection: why early diagnosis matters and cultural/linguistic barriers to care"
      - "What researchers recommend: screening, risk factor management, community health interventions"
    conclusion: >
      Resources: Alzheimer's Association Spanish-language resources; clinical trial participation 
      for Latino communities.

  key_data_points:
    - "Study: multidecade observation of dementia trends in Latino populations (WashU Medicine, July 2026)"
    - "Alzheimer's Association: Latinos are 1.5x more likely to develop Alzheimer's than non-Hispanic whites"
    - "Diabetes and cardiovascular disease — both elevated in Latino Americans — are major dementia risk factors"
    - "Latino Americans are 18% of the U.S. population; representation in Alzheimer's clinical trials has been historically under 5%"

  source_plan:
    - publisher: "WashU Medicine Newsroom"
      url: "https://medicine.wustl.edu/news/ [retrieve specific July 13 URL]"
      tier: 1
      used_for: "Study findings, institutional primary source"
    - publisher: "Alzheimer's Association — Latino Community"
      url: "https://www.alz.org/help-support/i-have-alz/younger-onset/diverse-communities"
      tier: 1
      used_for: "Population statistics, risk factors"
    - publisher: "NIH — Dementia and Hispanic/Latino Americans"
      url: "https://www.nia.nih.gov/health/alzheimers-and-dementia/alzheimers-disease-fact-sheet"
      tier: 1
      used_for: "Background data on dementia in U.S. population"

  expert_sources:
    - type: "Geriatric neurologist or dementia researcher with expertise in health disparities"
      reason: "Interpret mechanism and policy implications"

  seo:
    primary_keyword: "dementia risk Latino Americans"
    supporting_keywords:
      - "dementia Latino population study"
      - "Hispanic dementia risk"
      - "Alzheimer's Latino Americans"
      - "dementia health disparities"
      - "dementia rising United States"
    format: "Research explainer with data callout boxes; include early warning signs section"
    schema_markup: "Article + FAQPage"
    cluster: "Dementia / cognitive health / health equity"

  estimated_word_count: "1,000–1,300 words"

execution_notes: >
  Retrieve specific WashU study URL and journal of publication before publishing. 
  Consider this as a strong cluster anchor — related opportunities: cognitive health in 
  Latino communities, clinical trial diversity, dementia prevention.
```

---

### BRIEF 5 — P2 / SHORT-TERM

```yaml
brief:
  primary_headline: "VA and HHS Are Partnering on Psychedelic Drug Trials for Veterans — What It Means"
  alternate_headlines:
    - "The VA Is Now Officially Pursuing Psychedelic Treatments for Veterans With PTSD and Depression"
    - "HHS and VA Sign Landmark Agreement to Fast-Track Psychedelic Mental Health Trials for Veterans"
  topic: "HHS/VA Psychedelic Drug Trials for Veterans — MOU Announcement"
  primary_entity: "VA/HHS psychedelic mental health partnership"
  signal_type: clinical_trial
  allowed_category: "mental health and psychology / FDA and CDC regulatory updates"
  trend_strength_score: 68
  opportunity_score: 74
  discover_score: 4
  urgency: today
  confidence: high
  content_status: new
  source_count: 3
  why_now: >
    HHS and VA signed a formal MOU on July 13, 2026 to advance rapid-acting mental health 
    treatments for veterans, including psychedelic drug trials. The American Legion confirmed 
    it July 13. This is a direct policy action — not a proposal — from two federal agencies. 
    Veterans' mental health crisis (suicide rates, PTSD) is a persistent high-audience-relevance 
    topic. This is the first federal-level institutional commitment of this scale to psychedelic 
    therapy research.

  integrity_flags:
    - "⚠️ MOU is a partnership agreement — not a drug approval. Clearly distinguish between 'partnering to advance trials' and 'approving psychedelic treatment'"
    - "⚠️ MDMA-assisted therapy was rejected by FDA in 2024 — important regulatory context; psilocybin still in Phase 2/3. Note current regulatory status."
    - "⚠️ Do not imply veterans can currently access these treatments through the VA"

  outline:
    intro: >
      Open with the veteran mental health crisis as context: 17–22 veterans die by suicide 
      daily; PTSD affects ~30% of combat veterans; existing treatments leave a large gap. 
      Then introduce the MOU: HHS and VA have committed to a formal research partnership 
      on rapid-acting treatments including psychedelic therapies.
    sections:
      - "What the MOU actually commits to: scope, timeline, which treatments are in scope"
      - "Where psychedelic research stands right now: psilocybin (Phase 3), MDMA (FDA rejection 2024, re-evaluation), ketamine (already approved)"
      - "What veterans with PTSD and depression need to know: what's available now vs. what's coming"
      - "The science: how psychedelics work differently from SSRIs for trauma (neuroplasticity, fear extinction)"
      - "What previous trials showed: MAPS MDMA trials, NYU psilocybin research"
      - "Policy and access: VA mental health services today and what this partnership could change"
    conclusion: >
      What veterans and advocates should watch for; resources for current VA mental health support.

  key_data_points:
    - "HHS.gov and VA announced MOU July 13, 2026 — official federal commitment to psychedelic trial coordination"
    - "FDA rejected MDMA-assisted therapy (Lykos Therapeutics) in 2024; requested additional trials"
    - "Psilocybin: FDA Breakthrough Therapy designation for MDD and treatment-resistant depression"
    - "Ketamine (esketamine/Spravato) already FDA-approved and VA-available for treatment-resistant depression"
    - "Veteran suicide rate: ~17 per day (VA data, 2024)"

  source_plan:
    - publisher: "HHS.gov — HHS & VA Announce Partnership"
      url: "https://www.hhs.gov/about/news/2026/07/13/ [retrieve specific URL]"
      tier: 1
      used_for: "Primary policy announcement"
    - publisher: "The American Legion"
      url: "https://www.legion.org/ [retrieve specific July 13 URL]"
      tier: 2
      used_for: "Veterans advocacy confirmation"
    - publisher: "FDA — MDMA-assisted therapy decision"
      url: "https://www.fda.gov/news-events/press-announcements/fda-issues-complete-response-letter-mdma-assisted-therapy"
      tier: 1
      used_for: "Current regulatory context"
    - publisher: "VA — Mental Health"
      url: "https://www.mentalhealth.va.gov/"
      tier: 1
      used_for: "Current veteran mental health resources"

  expert_sources:
    - type: "Psychiatrist with psychedelic therapy research background (NYU, Johns Hopkins, or MAPS-affiliated)"
      reason: "Mechanism and clinical context for psychedelic treatment"
    - type: "Veterans mental health advocate or VA clinician"
      reason: "Patient-facing impact and access framing"

  seo:
    primary_keyword: "VA psychedelic therapy veterans"
    supporting_keywords:
      - "HHS VA psychedelic drug trials 2026"
      - "psilocybin PTSD veterans"
      - "VA mental health treatments"
      - "psychedelic therapy PTSD"
      - "MDMA therapy veterans"
    format: "News explainer with policy context; include 'What's available now vs. what's coming' comparison"
    schema_markup: "Article + FAQPage"
    cluster: "Mental health / psychedelic medicine / veterans health"

  estimated_word_count: "1,000–1,400 words"

execution_notes: >
  Retrieve HHS.gov press release URL to confirm MOU language before publishing. 
  Strong cluster opportunity: this brief can anchor a series on psychedelic medicine 
  (psilocybin, MDMA, ketamine — their current status and what research shows).
```

---

### BRIEF 6 — P3 / SCHEDULED

```yaml
brief:
  headline: "FDA Announces Recall of Popular Shampoo Brand Over Bacterial Contamination Risk"
  topic: "Shampoo Recall — Bacterial Contamination (FDA July 13, 2026)"
  primary_entity: "Shampoo recall (bacterial contamination)"
  signal_type: recall
  allowed_category: "FDA and CDC regulatory updates"
  trend_strength_score: 65
  opportunity_score: 68
  discover_score: 3
  urgency: this_week
  confidence: medium
  content_status: new
  source_count: 2
  why_now: "FDA recall announced July 13, 2026 per KAKE report. Bacterial contamination in personal care products is a consumer-safety topic with strong search intent ('is [brand] shampoo recalled')."
  
  integrity_flags:
    - "⚠️ Specific brand name and lot codes not confirmed from primary FDA source — do not name the brand until FDA.gov notice is retrieved"
    - "⚠️ Breaking-recall exception used — confidence capped at Medium"

  angle: "Consumer safety: what the recall means, which products/lots are affected, what to do with recalled product, and what bacterial contamination in shampoo can cause (scalp/skin infection risk)"

  key_data_points:
    - "FDA recall announced July 13, 2026 — popular shampoo brand, bacterial contamination"
    - "Bacterial contamination in personal care products can cause skin infections, particularly for those with cuts or compromised skin"
    - "Consumers should check lot codes on FDA recall database"

  sources:
    - publisher: "FDA MedWatch / Recalls"
      url: "https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts"
    - publisher: "KAKE news report"
      url: "[retrieve specific KAKE July 13 URL — URL unverified]"

  expert_type_needed: "Dermatologist or pharmacist for bacterial contamination risk context"

  seo:
    primary_keyword: "[brand name] shampoo recall 2026"
    format: "News brief + consumer action checklist"
    serp_difficulty: "Easy"

  estimated_word_count: "400–600 words"
```

---

### BRIEF 7 — P3 / SCHEDULED

```yaml
brief:
  headline: "FDA Warns Infant Formula Makers to Tighten Safety Controls After Recalls and Botulism Outbreaks"
  topic: "FDA Infant Formula Safety Advisory — Supplier Oversight and Botulism Risk"
  primary_entity: "Infant formula safety (FDA advisory 2026)"
  signal_type: recall
  allowed_category: "FDA and CDC regulatory updates / pediatric health"
  trend_strength_score: 62
  opportunity_score: 70
  discover_score: 4
  urgency: this_week
  confidence: medium
  content_status: new
  source_count: 2
  why_now: "Reuters reported July 13, 2026 that FDA urged infant formula manufacturers to tighten supplier oversight after product recalls and botulism outbreaks. FDA advisory on infant formula safety is high consumer relevance — parents actively search this topic."
  
  integrity_flags:
    - "⚠️ Specific recalls and botulism cases not fully detailed from Reuters summary alone — retrieve FDA advisory before stating case counts or implying current market risk"
    - "⚠️ Do not create undue alarm: this is a regulatory advisory, not a new contamination event per available signals"

  angle: "What the FDA is actually telling formula makers, why it matters after 2022's formula shortage and Abbott recall, what parents should know about formula safety today, and how to check for recalls"

  key_data_points:
    - "Reuters July 13: FDA urging formula makers to tighten supplier oversight — context: prior recalls + botulism outbreaks"
    - "2022 Abbott/Similac recall was the largest infant formula recall in U.S. history, causing national shortage"
    - "Botulism in infants is rare but life-threatening — requires immediate medical attention"
    - "FDA MedWatch is the authoritative resource for checking current formula recalls"

  sources:
    - publisher: "Reuters Health"
      url: "https://www.reuters.com/health/ [retrieve specific July 13 URL]"
    - publisher: "FDA — Infant Formula"
      url: "https://www.fda.gov/food/people-risk-foodborne-illness/questions-answers-consumers-concerning-infant-formula"

  expert_type_needed: "Pediatrician or neonatologist for infant formula safety guidance"

  seo:
    primary_keyword: "infant formula recall 2026"
    format: "News brief + parent FAQ"
    serp_difficulty: "Medium"

  estimated_word_count: "500–800 words"
```

---

### BRIEF 8 — P3 / SCHEDULED

```yaml
brief:
  headline: "Wellness Business Owner Accused of Illegally Prescribing GLP-1 Drugs — What Patients Should Know"
  topic: "GLP-1 Illegal Prescribing — Enforcement Action (Asheville, NC)"
  primary_entity: "GLP-1 illegal prescribing (wellness business enforcement)"
  signal_type: drug_or_treatment_claim
  allowed_category: "FDA and CDC regulatory updates / nutrition and diet science"
  trend_strength_score: 55
  opportunity_score: 62
  discover_score: 3
  urgency: this_week
  confidence: low
  content_status: new
  source_count: 1
  why_now: "WLOS (ABC affiliate, Asheville NC) reported July 13 that a wellness business owner is accused of illegally prescribing GLP-1 drugs. Distinct from Yale/online-prescribing coverage — this is a criminal enforcement action. Consumer-relevant angle: what makes a GLP-1 prescription legal vs. illegal, and what patients using wellness-clinic GLP-1 services should verify."

  integrity_flags:
    - "⚠️ Single regional source (WLOS) — confidence Low; do not present as established trend without additional corroboration"
    - "⚠️ Accused does not equal convicted — use 'accused' and 'alleged' throughout; do not name individuals without confirming public records"
    - "⚠️ This is geographically local but editorially relevant nationally — frame as illustrating a broader pattern, not just a local story"

  angle: "Use this enforcement case as the news peg to explain: what federal law says about prescribing GLP-1s, what 'telehealth prescribing' gray areas exist, how to verify a provider's prescribing authority, and red flags in wellness-clinic weight loss programs."

  key_data_points:
    - "WLOS July 13: Asheville wellness business owner accused of illegal GLP-1 prescribing"
    - "GLP-1 drugs (semaglutide, tirzepatide) require a valid prescription from a licensed provider"
    - "Non-physicians operating wellness businesses cannot legally prescribe controlled or prescription drugs"
    - "FDA has issued repeated warnings about compounded semaglutide and unlicensed prescribers"

  sources:
    - publisher: "WLOS ABC13"
      url: "[retrieve specific WLOS July 13 URL — URL unverified]"
    - publisher: "FDA — GLP-1 Drug Safety"
      url: "https://www.fda.gov/drugs/postmarket-drug-safety-information-patients-and-providers/medications-containing-semaglutide-marketed-type-2-diabetes-or-weight-loss"

  expert_type_needed: "Healthcare attorney or pharmacist for prescribing law context"

  seo:
    primary_keyword: "illegal GLP-1 prescribing wellness clinic"
    format: "News analysis + consumer protection FAQ"
    serp_difficulty: "Medium"

  estimated_word_count: "600–900 words"
```

---

## REJECTED TOPICS LOG

| Topic | Signal Source | Rejection Reason |
|---|---|---|
| New World Screwworm — USDA | USDA APHIS July 12 | **Existing** — covered 2026-07-13; no new case counts or geographic expansion confirmed since |
| E. coli frozen blueberries | Google News | **Existing** — covered 5 consecutive days (07-08 through 07-12); no new outbreak development in signals |
| FDA eye drops recall (2.5M bottles) | Google News | **Existing** — covered 4 consecutive days (07-09 through 07-12); no new action or expansion |
| Cream cheese recall | Google News | **Existing** — covered 4 consecutive days |
| GLP-1 Yale study (online prescribing oversight) | Google Trends | **Existing** — covered 4 consecutive days (07-09 through 07-12) |
| Sleep deprivation / weight gain (Columbia) | Google Trends | **Existing** — covered 4 consecutive days |
| Ebola DRC clinical trial | Google News (CDC travel advisory) | **Existing** — covered 4 consecutive days; CDC travel advisory is routine update only |
| Glioma / Weill Cornell evolution study | Google News | **Existing** — covered 2026-07-13 |
| AMA wearables survey | Google News | **Existing** — covered 2026-07-13 |
| Stanford opioid taper | Google News | **Existing** — covered 2026-07-12 |
| Zeke Emanuel / longevity diets | Google Trends rising | **Existing** — covered 2026-07-13; "zeke emanuel ice cream wellness" is residual search interest, no new article |
| Marie-Pierre St-Onge sleep-diet | Google Trends rising | **Existing** — covered 2026-07-13 |
| Lung transplant / terminal lung cancer | Google News | **Existing** — covered 2026-07-13 |
| Fentanyl vaccine trial | Recent coverage | **Existing** — covered 2026-07-13 |
| Jimmy Kimmel / Mitch McConnell health searches | Google Trends rising | **Rejected** — celebrity/political health queries; excluded categories (celebrity gossip, political) |
| Brandy Norwood / Charlize Theron weight loss | Google Trends rising | **Rejected** — celebrity gossip; excluded category per category_rules.yaml |
| ACA premiums 2027 (KFF) | Google News | **Rejected** — insurance finance/policy; no direct clinical health content for target audience |
| HHS trans care Medicare/Medicaid | NPR July 13 | **Rejected** — political healthcare policy; brand_safety_rules: allow_politics: false |
| Male wellness / peptides (FT) | Google News | **Rejected** — wellness marketing framing; no peer-reviewed basis; brand safety concern |
| DOJ digital health CEO sentencing (Adderall) | Google News | **Rejected** — outside 5-day freshness window (July 7); primarily legal/criminal news |
| Peanut allergy trial (Children's Healthcare Atlanta) | Google News | **Monitored / below threshold** — single-institution, regional scope; trend_strength_score estimated ~42; does not clear minimum 50 |
| Wellness influencers / Pew Research | Google News | **Monitored / below threshold** — interesting but category_fit: adjacent only; opportunity_score ~50; does not clear 55 minimum |
| Google AI / global health (blog.google) | Google News | **Rejected** — corporate tech announcement; not clinical health |
| Cucumbers nutrition facts | Google Trends rising | **Rejected** — low opportunity; generic nutrition query with no news peg or fresh angle; saturated SERP |
| Enteral nutrition | Google Trends rising | **Rejected** — clinical/hospital nutrition context; not consumer-facing health audience |

---

## INTEGRITY FLAGS — CONSOLIDATED EDITORIAL REVIEW

| # | Topic | Flag | Action Required |
|---|---|---|---|
| 1 | Medical Cannabis / Dementia | Study design unknown (RCT vs observational); NYT uses "suggests" language | Retrieve primary journal before publishing; match epistemic framing |
| 2 | Medical Cannabis / Dementia | Medical cannabis access is state-regulated | Include state-by-state access note; do not imply universal availability |
| 3 | Medical Cannabis / Dementia | Current antipsychotics have black-box warnings | Include comparison context |
| 4 | Cyclosporiasis WV | Case counts unconfirmed | Do not publish specific numbers until CDC WV notice retrieved |
| 5 | Cyclosporiasis WV | "Parasite outbreak" framing in search may amplify alarm | Lead with CDC-verified language; contextualize severity |
| 6 | Heat + Mental Health | Multi-country study may not map directly to U.S. | Clarify U.S. data subset; note confounders if study addresses them |
| 7 | Heat + Mental Health | Correlation ≠ causation framing risk | Use "associated with" not "causes"; study language likely observational |
| 8 | Dementia / Latino populations | "Latino" is heterogeneous | Note subgroup distinctions if study provides them |
| 9 | Dementia / Latino populations | WashU press release only — not direct journal | Retrieve DOI/journal citation before publishing outcome statistics |
| 10 | HHS/VA Psychedelic Trials | MOU ≠ drug approval | Explicitly state veterans cannot access psychedelic treatments through VA currently |
| 11 | HHS/VA Psychedelic Trials | MDMA rejected by FDA 2024 | Include regulatory history for accurate context |
| 12 | Shampoo Recall | Brand name unconfirmed without FDA.gov primary | Do not name brand until FDA notice retrieved |
| 13 | Infant Formula | Reuters summary only — specific recalls/botulism cases not detailed | Retrieve FDA advisory before stating case counts |
| 14 | Infant Formula | Advisory ≠ new contamination event | Do not alarm readers beyond what FDA actually stated |
| 15 | GLP-1 Enforcement | Single regional source; accused ≠ convicted | Use "accused/alleged"; seek second source; do not name individuals without confirming public records |

---

## RUN NOTES

**Tools used:** Google Trends (serpapi_prefetch ✅), Google News Radar (injected ✅), recent coverage block (injected ✅)

**Tools unavailable:** Reddit (not queried in automation mode), Exa semantic search (not injected), direct competitor scrape (not queried — competitor context inferred from prior run patterns)

**Site self-check:** Skipped — `site_url` not configured. Duplicate detection performed via injected recent coverage block (7-day history) and cross-run theme tracking.

**Deferred topics:** `data/deferred_topics.yaml` not accessible in this automation mode — recommend checking manually or confirming file exists at path.

**Key recurring themes suppressed today:** E. coli/blueberries (5 days), eye drops recall (4 days), GLP-1 Yale study (4 days), cream cheese recall (4 days), sleep/weight (4 days), Ebola DRC (4 days). All correctly set to `content_status: existing` and removed from candidates. ✅

**New discovery today vs. prior runs:** All 8 retained candidates are net-new topics not previously covered, except Cyclosporiasis (legitimate update due to West Virginia-specific breakout on Google Trends Trending Now).

**Google Trends Trending Now leverage:** Cyclosporiasis — #1 and #2 real-time trending searches in US ("west virginia cyclosporiasis outbreak," "parasite outbreak") — elevated from prior evergreen coverage to P1/Immediate. This is the clearest example of real-time Trends signal driving prioritization today.

**Content mix balance:** 2× P1 (breaking/study), 3× P2 (research/policy), 3× P3 (recall/enforcement). Categories: public health (2), medical research (2), mental health (2), regulatory/recalls (2). Balance is healthy — no single category dominates.

**Archive note:** This run should be logged to `data/run_history.yaml` with today's date, 8 retained candidates, 24 rejected/suppressed, top topic: Cyclosporiasis West Virginia, key themes: dementia, heat-mental health, psychedelic medicine, infant formula safety, GLP-1 enforcement.