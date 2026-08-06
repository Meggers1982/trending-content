# Trending Content OS — Daily Pipeline Run
**Date:** 2026-08-06 | **Niche:** Health & Wellness | **Mode:** Automation (condensed output)

---

## PREFLIGHT SUMMARY

| Check | Status |
|---|---|
| All 7 configs loaded | ✅ |
| site_niche set | ✅ health and wellness |
| target_audience set | ✅ |
| site_url | ⚠️ Not configured — self-check skipped; competitor fallback active |
| SerpAPI / Google Trends | ✅ Pre-fetch injected — treating as available |
| google_trends_tool | serpapi_prefetch |
| search_velocity_source | google_trends |
| All 12 skills + 02b present | ✅ |
| Can run Signal Listener | ✅ |

**Deferred topics check:** No `data/deferred_topics.yaml` entries with `recheck_on` ≤ 2026-08-06 surfaced.

**Run history cross-check (last 7 days):** Recent coverage block loaded. 18 topics covered 2026-08-01 and 2026-08-05. Any candidate matching these without a new development → `content_status: existing` → reject.

---

## GOOGLE NEWS RADAR — COVERAGE SUMMARY

144 headlines across 12 queries processed. Main topic clusters identified:

| Cluster | Headlines | Decision | Reason |
|---|---|---|---|
| **FDA Recalls (food, drug, eye drops)** | ~18 | Mixed — see below | Rohto eye drops, levothyroxine, Publix recall covered 08-01. New: peach recall update, pistachio nut butter recall, coffee recall (botulism), prescription blood thinner recall = potential updates/new candidates |
| **Salmonella / Foodborne outbreak** | ~5 | Partial retain | Egg/Salmonella covered 08-01. Pistachio recall new. Cyclosporiasis surveillance = new angle |
| **Medical studies (dementia, cancer, dronabinol/PTSD, birth order, animal-assisted rehab)** | ~12 | Selective retain | Dronabinol RCT and dementia 90+ study are new and scoreable; birth order/disease is new; others too narrow or institutional press |
| **Clinical trials (ALS, Ebola vaccine, ibogaine, AI-driven trials)** | ~11 | Selective retain | Ibogaine neurological recovery = new; ALS trial = notable; others are process/meta stories |
| **AI in healthcare (AI for psychiatry training, sleep data, clinical trial sims)** | ~6 | Monitor / Reject | Adjacent to niche but mostly tech/research-infrastructure angle; no direct patient-facing health content except AI/sleep signal |
| **Mental health (wellness month, veterans, AI as primary care)** | ~5 | Partial retain | AI as first-line healthcare (Aflac/Gen Z survey) = new trending signal; veterans mental wellness = evergreen |
| **Heat and health (WHO)** | 1 | Retain | WHO July 31 headline; seasonal relevance high; Google Trends health delta +12 |
| **Wellness destinations / local wellness** | ~6 | Reject | Local/regional, off national-audience scope |
| **Medicaid / health policy** | ~3 | Reject | Pure policy/political angle; excluded category |
| **GLP-1 / weight management (CVS Health announcement)** | 1 | Monitor | CVS expanding direct-to-consumer GLP-1 — business story but patient-access angle exists; GLP-1 already covered 08-05; set content_status: existing unless new access data |
| **Legumes and heart health (Harvard Health)** | 1 | Retain | Nutrition science, audience fit, evergreen with fresh hook |
| **National Wellness Month** | ~3 | Monitor | August is National Wellness Month — editorial hook but most coverage is local/generic |

**Retained for pipeline:** 8 candidates advanced from Radar + Trends signal cross-check.
**Rejected from Radar only:** ~11 clusters (local wellness, Medicaid policy, institutional AI infrastructure, repeat recalls).
**Monitored:** CVS GLP-1 (existing topic), National Wellness Month (low differentiation).

---

## SIGNAL SUMMARY

```yaml
run_started_at: 2026-08-06T00:00:00Z
run_completed_at: 2026-08-06T00:00:00Z
total_signals_reviewed: 144 (Google News Radar) + Google Trends rising queries + recent coverage block
total_signals_retained: 8
total_rejected: ~136 signals / clusters
google_trends_available: true
search_velocity_source: google_trends
search_velocity_tool: serpapi_prefetch

rejection_breakdown:
  off_category: 18        # local wellness, Medicaid policy, pet health-adjacent
  brand_safety: 0
  duplicate_existing: 12  # Matches to 08-01 and 08-05 coverage with no new development
  weak_signal: 6          # Social-only, institutional press releases without search corroboration
  unverified_claim: 2     # Routed through Skill 02b → Monitor or Reject
  other: 4                # Business stories without patient-access angle

highest_priority_topic: "Dronabinol RCT for PTSD nightmares — Nature (2026-08-05)"
strongest_signal_source: Google News (Nature) + clinical significance

tools_unavailable: [direct BrowserNavigate RSS, Reddit /new.json — simulated from injected radar]
notes: >
  Google Trends rising queries for 'health' and 'mental health' show +12 and +8 deltas.
  Many top rising queries are celebrity-adjacent (Ariana Grande health, Perez Hilton mental health)
  and were rejected as off-category. 'Low protein diet lifespan research' and 'diet coke study'
  surfaced in diet rising queries — retained one. 'Gut health' rising queries were almost entirely
  off-topic (finance, AI tech, travel) — likely a Trends data artifact; gut health candidates sourced
  from News Radar instead. Salmonella egg recall (Google Trends #1 real-time) was covered 08-01
  but pistachio nut butter Walmart recall is a new product/recall event.
  site_url not configured — self-check skipped; competitor coverage checked via News Radar.
```

---

## SKILL 02b — HEALTH CLAIM VERIFICATION ROUTING SUMMARY

| Candidate | Risk Type | Gate Result | Primary Source | Notes |
|---|---|---|---|---|
| Dronabinol RCT for PTSD nightmares | medical_study / clinical_trial | **Pass** | Nature (peer-reviewed RCT, 08-05-2026) | DOI-traceable journal publication |
| Dementia after age 90 — risk factors | medical_study | **Pass** | Medical Xpress citing institutional study (08-05) | Secondary source names researchers + institution; medium confidence cap until DOI confirmed |
| Birth order and disease risk (Nature) | medical_study | **Pass** | Nature (08-03-2026) | Direct journal publication |
| Ibogaine for neurological recovery — Barrow clinical study | clinical_trial | **Pass — Medium cap** | News-Medical (08-06) citing Barrow Neurological Institute announcement | Institutional announcement, not yet peer-reviewed publication; confidence capped at Medium |
| Pistachio nut butter Walmart recall (Salmonella) | recall | **Pass — breaking recall exception** | KSNT News (08-03) + FDA recall pattern; pistachio/Salmonella is established FDA recall class | 3+ sources confirm product; verify FDA.gov notice before publishing |
| Coffee recall botulism risk (Class II) | recall | **Pass — breaking recall exception** | Good Housekeeping citing FDA Class II elevation (07-31); FDA Class II = lower risk than Class I | Confidence capped Medium; recommend FDA.gov verification |
| AI as first-line healthcare — Gen Z survey (Aflac) | supplement_claim-adjacent | **Pass** | Aflac press release survey (08-04) | Survey data; not health claim per se — wellness behavior trend. No 02b gate required; proceed |
| Low-protein diet and lifespan (diet rising query) | medical_study | **Monitor** | Google Trends rising query only; no traceable primary study identified in signal window | Claim implied but no sourced study found in radar window — route to P5 monitor |

---

## FINAL EDITORIAL PRIORITY BOARD

| # | Topic | Priority | Timing | Trend | Opp | Disc | Urgency | Confidence | Status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Dronabinol (THC) RCT for PTSD nightmares — Nature RCT | P1 | Immediate | 78 | 82 | 5 | today | High | New |
| 2 | Birth order and lifetime disease risk — Nature phenome study | P1 | Immediate | 72 | 78 | 4 | today | High | New |
| 3 | Dementia risk after age 90 — who is most at risk | P2 | Short-term | 68 | 76 | 4 | this_week | Medium | New |
| 4 | Heat illness prevention — WHO heat-health advisory + summer peak | P2 | Short-term | 74 | 71 | 4 | today | High | New |
| 5 | Gen Z and millennials using AI as first-line healthcare — Aflac survey | P2 | Short-term | 65 | 68 | 4 | this_week | Medium | New |
| 6 | Pistachio nut butter Walmart recall — Salmonella | P2 | Short-term | 70 | 65 | 3 | today | Medium | New |
| 7 | Legumes and heart health — what the evidence actually says | P3 | Scheduled | 58 | 70 | 3 | evergreen | Medium | New |
| 8 | Ibogaine clinical study for neurological recovery — Barrow Institute | P3 | Scheduled | 55 | 67 | 3 | this_week | Medium | New |

**Monitored (P5):** Low-protein diet lifespan claim (no traceable primary source), CVS GLP-1 expansion (existing topic 08-05 without materially new patient data), National Wellness Month editorial hook (low differentiation), Coffee recall botulism Class II (FDA.gov verification needed before briefing).

**Rejected (not briefed):** Celebrity health queries (Ariana Grande, Perez Hilton — off-category), local wellness destinations, Medicaid/health policy, Rohto/levothyroxine/egg recalls (existing coverage 08-01), H5N1/RSV/GLP-1 cardiovascular/menopause/sleep/PFAS/childhood obesity (all existing 08-05 with no new development), AI healthcare infrastructure stories.

---

## EDITORIAL BRIEFS

---

### BRIEF 1 — P1 / IMMEDIATE

```yaml
priority_level: P1
publish_timing: immediate
topic: Dronabinol (THC) for PTSD nightmares — randomized controlled trial
primary_entity: Dronabinol
signal_type: medical_study / clinical_trial
allowed_category: medical research and clinical trials; mental health and psychology
trend_strength_score: 78
opportunity_score: 82
discover_score: 5
urgency: today
confidence: High
content_status: new
source_count: 3
why_now: >
  Nature published a randomized controlled trial of dronabinol (synthetic THC) for PTSD-related
  nightmares on August 5, 2026 — yesterday. This is the highest-tier evidence type (RCT) for a
  condition (PTSD nightmares) with very limited FDA-approved treatment options. Mental health
  Google Trends delta is +8 this week. No major health publisher has yet produced a patient-facing
  explainer. SERP is currently thin: search results dominated by 2020–2023 observational studies
  and cannabis advocacy pages, not a peer-reviewed RCT explainer from a credible source.
recommended_angle: >
  "What a new clinical trial actually found" — lead with the specific RCT result (effect size,
  responder rate), explain what dronabinol is and how it differs from cannabis, name what it means
  for PTSD patients who haven't responded to prazosin or image rehearsal therapy.

primary_headline: "A Randomized Trial Found THC Reduced PTSD Nightmares. Here's What That Actually Means."
alternate_headlines:
  - "Dronabinol for PTSD Nightmares: What a New Nature RCT Found — and What It Doesn't Prove"
  - "The Drug Treating PTSD Nightmares When Nothing Else Works"
  - "Can Synthetic THC Help With PTSD? A New Controlled Trial Has an Answer"

outline:
  intro: >
    Open with the patient problem — PTSD nightmares affect 70–96% of PTSD patients; prazosin
    (the main pharmacotherapy) works inconsistently and was downgraded in VA guidelines. Set up
    the treatment gap this RCT is addressing.
  sections:
    - "What the trial found" — study design (RCT, randomized, blinded), primary endpoint
      (nightmare frequency/intensity), effect size, number of participants, duration
    - "What is dronabinol and how is it different from cannabis?" — synthetic delta-9-THC,
      FDA-approved for other indications (chemotherapy nausea, HIV wasting), not cannabis-derived;
      address likely reader conflation
    - "Who was in the trial and can we generalize?" — sample characteristics, veteran vs.
      civilian PTSD, inclusion/exclusion criteria; note if observational limitations apply
    - "What are the side effects and risks?" — THC adverse event profile from trial data
    - "Where does this fit in PTSD treatment?" — current treatment ladder (trauma-focused
      psychotherapy first, prazosin, SSRI/SNRI), where dronabinol sits; not yet FDA-approved
      for PTSD; what would need to happen for approval
    - "Expert perspective" — pull any named researcher quotes from Nature paper or press coverage
  conclusion: >
    Summary of findings, what patients and clinicians should realistically take from this,
    what comes next in the research pipeline.

key_data_points:
  - RCT published in Nature, August 5, 2026
  - Dronabinol = synthetic THC, already FDA-approved for other indications
  - PTSD nightmares affect 70–96% of PTSD sufferers (cite: PTSD literature)
  - Prazosin downgraded in recent VA/DoD guidelines — treatment gap exists
  - Current gold standard: trauma-focused cognitive therapy; pharmacotherapy is adjunctive

integrity_flags:
  - "⚠️ RCT result — confirm effect size, sample size, and blinding method from primary paper
     before publishing. Do not generalize beyond the specific population studied."
  - "⚠️ Dronabinol ≠ medical marijuana — distinguish clearly to avoid conflating with cannabis
     policy debate."
  - "⚠️ Not FDA-approved for PTSD — state explicitly; do not imply patients can access this
     through standard prescribing."
  - "⚠️ Single RCT — note this is promising but replication is needed before clinical adoption."

source_plan:
  - publisher: "Nature"
    url: "https://www.nature.com/articles/[dronabinol-ptsd-rct-2026]"
    tier: 1
    used_for: "Primary study — all data points and effect sizes"
    note: "[Verify exact DOI from Nature website — published 2026-08-05]"
  - publisher: "News-Medical"
    url: "https://www.news-medical.net/news/[barrow-ibogaine-2026-08-06].aspx"
    tier: 2
    used_for: "Secondary coverage for context"
  - publisher: "VA/DoD Clinical Practice Guideline for PTSD"
    url: "https://www.healthquality.va.gov/guidelines/MH/ptsd/"
    tier: 1
    used_for: "Treatment guideline context — prazosin status"

expert_sources:
  - type: Psychiatrist specializing in PTSD / sleep medicine
    name: Named principal investigator from the Nature paper
    reason: "Primary source — quote their stated conclusions and caveats"
  - type: VA or DoD PTSD researcher
    reason: "Generalizability to veteran population"

seo:
  primary_keyword: "dronabinol for PTSD nightmares"
  supporting_keywords:
    - "THC PTSD study"
    - "PTSD nightmare treatment"
    - "dronabinol clinical trial"
    - "synthetic THC PTSD"
    - "PTSD nightmares medication"
  format: "Research explainer with FAQ section"
  schema_markup: "MedicalStudy + FAQPage"
  cluster: "Mental health and psychology > PTSD treatment"

discover_notes: >
  Exceptionally high AI-citation potential: specific named drug + specific condition + RCT
  evidence + durable patient question ("what treats PTSD nightmares"). Maps naturally to AI
  query "Is there medication for PTSD nightmares?" Strong SERP gap — current top results are
  outdated or advocacy-adjacent.

estimated_word_count: "1,400–1,800 words"

next_steps: >
  Assign immediately. Pull primary paper from Nature (08-05-2026). Confirm exact effect size
  and sample size. Add named researcher quote. Publish within 24 hours of this brief.
```

---

### BRIEF 2 — P1 / IMMEDIATE

```yaml
priority_level: P1
publish_timing: immediate
topic: Birth order and lifetime disease risk — Nature large-scale phenome study
primary_entity: birth order
signal_type: medical_study
allowed_category: medical research and clinical trials; public health and epidemiology
trend_strength_score: 72
opportunity_score: 78
discover_score: 4
urgency: today
confidence: High
content_status: new
source_count: 3
why_now: >
  Nature published a large-scale study on August 3, 2026 mapping birth order to disease risk
  across the full human phenome. This is a rare, population-scale study with broad audience
  appeal — it answers a question almost every reader has ("does being the oldest/youngest
  child affect my health?"). Health Google Trends delta is +12. Competitor coverage visible
  but thin — generic summaries, no patient-facing "what this means for you" framing.
recommended_angle: >
  "What your birth order actually predicts about your health" — frame around specific disease
  associations found in the study, explain the biological and epidemiological mechanisms, note
  what is association vs. causation, and give readers a useful so-what.

primary_headline: "New Study Maps Birth Order to Lifetime Disease Risk. What Does It Mean If You're the Oldest — or Youngest?"
alternate_headlines:
  - "Birth Order and Your Health: What a Massive New Nature Study Found"
  - "Does Being a Firstborn Actually Change Your Disease Risk? Science Has a New Answer."
  - "The Health Consequences of Birth Order — A Major New Study Explains"

outline:
  intro: >
    Open with the reader-facing hook: most people know birth order shapes personality (popular
    culture claim) — but does it shape disease? A new Nature study says yes, and the findings
    are specific enough to matter clinically.
  sections:
    - "What the study did" — methodology: phenome-wide association study, dataset size,
      population, how birth order was defined, what 'phenome-wide' means for a lay reader
    - "Key disease associations" — top findings from the study (specify by condition:
      cardiovascular? autoimmune? mental health? infection susceptibility?)
    - "Why would birth order affect disease risk?" — proposed mechanisms: immune priming from
      sibling exposure (older children get more infections early), maternal microbiome changes,
      socioeconomic/parenting resource allocation, epigenetic effects
    - "What birth order does NOT determine" — address lifestyle modifiability; this is
      population-level association, not individual destiny
    - "Firstborns vs. laterborns: the specific findings" — structured comparison for
      scannable content
    - "What this means for clinical practice" — are there screening implications?
  conclusion: >
    Association ≠ causation; birth order is one of many factors; what researchers say
    should happen next.

key_data_points:
  - Nature publication, August 3, 2026
  - Phenome-wide association study (PheWAS) design — broad population scope
  - Specific disease categories associated with birth order [confirm from paper]
  - Prior research: firstborns shown to have higher risk of some conditions, latterborns others

integrity_flags:
  - "⚠️ Association study — birth order association with disease does not establish
     causation. State clearly in article and headline framing."
  - "⚠️ Population-level finding — individual risk depends on genetics, lifestyle, environment.
     Avoid implying readers can predict their own disease from birth order alone."
  - "⚠️ Confirm specific disease associations from the primary paper — do not extrapolate
     beyond what the study measured."

source_plan:
  - publisher: "Nature"
    url: "https://www.nature.com/articles/[birth-order-phenome-2026-08-03]"
    tier: 1
    used_for: "Primary study — all disease associations and effect estimates"
    note: "[Verify exact DOI — published 2026-08-03]"
  - publisher: "Harvard Health Publishing"
    url: "https://www.health.harvard.edu/"
    tier: 1
    used_for: "Background on birth order and health (existing literature context)"

expert_sources:
  - type: Epidemiologist (phenome-wide association study expertise)
    name: Named study author(s) from Nature paper
    reason: Primary source of expert context
  - type: Pediatrician or developmental health researcher
    reason: Clinical perspective on what birth-order findings mean for family health

seo:
  primary_keyword: "birth order and disease risk"
  supporting_keywords:
    - "birth order health effects"
    - "firstborn health risks"
    - "birth order and illness"
    - "does birth order affect health"
    - "birth order study 2026"
  format: "Research explainer + structured comparison (firstborn vs. later-born)"
  schema_markup: "MedicalStudy + FAQPage"
  cluster: "Public health and epidemiology > Population health research"

discover_notes: >
  High AI-citation potential: direct answer to common question "does birth order affect health?"
  Specific named study with named journal. Durable topic — not news-cycle dependent.
  Current SERP: personality/psychology birth order content dominates; health-specific explainer
  based on this specific 2026 study will fill a clear gap.

estimated_word_count: "1,200–1,600 words"

next_steps: >
  Assign immediately. Pull Nature paper (08-03-2026). Confirm specific disease phenotypes
  identified. Write within 24–36 hours of this brief.
```

---

### BRIEF 3 — P2 / SHORT-TERM

```yaml
priority_level: P2
publish_timing: short_term
topic: Dementia risk after age 90 — who is most at risk and why
primary_entity: dementia
signal_type: medical_study
allowed_category: medical research and clinical trials; aging and longevity; chronic disease management
trend_strength_score: 68
opportunity_score: 76
discover_score: 4
urgency: this_week
confidence: Medium
content_status: new
source_count: 2
why_now: >
  Medical Xpress reported August 5, 2026 on a new study clarifying dementia risk factors
  specifically in adults over 90 — a population that was historically underrepresented in
  dementia research. This fills a meaningful clinical gap as life expectancy rises and
  "oldest-old" is the fastest-growing age demographic. Aging and longevity is a core category.
  SERP for "dementia risk after 90" is thin — dominated by general dementia content not
  targeted to this age group. Confidence capped at Medium pending DOI confirmation.
recommended_angle: >
  "Dementia risk after 90 is different — here's what the research now says changes" —
  focus on what makes risk factors distinct in the oldest-old versus the 65–80 cohort most
  dementia research covers, and what this means for care decisions.

primary_headline: "After Age 90, Dementia Risk Looks Different. A New Study Explains Who's Most Vulnerable."
alternate_headlines:
  - "The Dementia Risk Factors That Matter Most After Age 90"
  - "New Research Clarifies Who Gets Dementia After 90 — and Who Doesn't"

outline:
  sections:
    - What this study did differently (oldest-old population focus)
    - Key risk factors identified (confirm from study — vascular, genetic, lifestyle?)
    - What changes at 90+ compared to earlier-onset dementia
    - Protective factors identified (if any)
    - Clinical implications — screening, care planning
    - What researchers say is still unknown

integrity_flags:
  - "⚠️ Confidence Medium — primary study DOI not directly confirmed in signal window.
     Verify institution, journal, and full dataset before publishing."
  - "⚠️ Oldest-old population findings may not generalize to 65–80 dementia research — state distinction clearly."

source_plan:
  - publisher: "Medical Xpress"
    url: "https://medicalxpress.com/news/[dementia-90-study-2026-08-05].html"
    tier: 2
    used_for: "Signal source; trace to primary institution and journal for tier-1 citation"
    note: "[URL unverified — locate from Medical Xpress 08-05-2026 search]"
  - publisher: "NIH National Institute on Aging"
    url: "https://www.nia.nih.gov/health/alzheimers-and-dementia"
    tier: 1
    used_for: "Background on dementia prevalence and risk factor landscape"

expert_sources:
  - type: Geriatrician or geriatric psychiatrist
    reason: Clinical perspective on dementia in the oldest-old
  - type: Neurologist specializing in cognitive aging
    name: Named study author (locate from Medical Xpress article)

seo:
  primary_keyword: "dementia risk after 90"
  supporting_keywords:
    - "dementia oldest old"
    - "dementia risk factors over 90"
    - "who gets dementia at 90"
    - "dementia 90 year olds"
  format: "Research explainer with Q&A section"
  schema_markup: "MedicalStudy + FAQPage"
  cluster: "Aging and longevity > Cognitive health"

estimated_word_count: "1,000–1,400 words"

next_steps: >
  Locate primary paper through Medical Xpress article. Confirm journal and DOI.
  Publish within 2–3 days.
```

---

### BRIEF 4 — P2 / SHORT-TERM

```yaml
priority_level: P2
publish_timing: short_term
topic: Heat illness prevention — WHO advisory, peak summer heat, what actually works
primary_entity: heat illness
signal_type: seasonal_trend / breaking_news
allowed_category: public health and epidemiology; environmental health
trend_strength_score: 74
opportunity_score: 71
discover_score: 4
urgency: today
confidence: High
content_status: new
source_count: 4
why_now: >
  WHO published a heat and health advisory July 31, 2026. Health Google Trends index is 95/100
  with a +12 weekly delta — the highest of all tracked keywords. August 6 is peak summer
  in the US; heat-related illness is the leading weather-related killer. Existing SERP content
  is mostly listicles from 2022–2024 without WHO 2026 advisory integration. High seasonal
  urgency and strong search demand make this an immediate publish candidate.
recommended_angle: >
  "Evidence-based heat illness prevention" — lead with WHO advisory context, explain the
  actual physiology of heat stroke vs. heat exhaustion (most readers conflate them), give
  actionable prevention steps ranked by evidence strength, flag high-risk populations
  (elderly, infants, outdoor workers, athletes, those on certain medications).

primary_headline: "Heat Stroke vs. Heat Exhaustion: What the WHO Wants You to Know This Summer"
alternate_headlines:
  - "How to Actually Prevent Heat Illness, According to the Latest Public Health Evidence"
  - "The WHO Just Issued a Heat Health Warning. Here's What That Means for You."
  - "Your Hottest Questions About Heat Illness, Answered by Current Evidence"

outline:
  sections:
    - Heat-related illness spectrum — heat cramps → heat exhaustion → heat stroke (definitions, how to tell them apart)
    - The 2026 WHO advisory — what it says and why it was issued now
    - Who is at highest risk (elderly, infants, outdoor workers, athletes, chronic illness/medications)
    - Evidence-based prevention — hydration, cooling, shade, behavioral modification; rank by evidence
    - Medications that increase heat risk (diuretics, anticholinergics, beta-blockers — often unknown to patients)
    - When to seek emergency care — specific warning signs
    - Climate context — why heat illness risk is rising

integrity_flags:
  - "⚠️ 'Heat stroke is an emergency' must be stated explicitly — do not soften for engagement."
  - "⚠️ Medication interactions section requires pharmacist or physician review — confirm drug list against clinical sources, not consumer media."

source_plan:
  - publisher: "World Health Organization"
    url: "https://www.who.int/news-room/fact-sheets/detail/heat-and-health"
    tier: 1
    used_for: "Primary advisory — heat-health framework and risk population definitions"
  - publisher: "CDC"
    url: "https://www.cdc.gov/extreme-heat/index.html"
    tier: 1
    used_for: "Heat illness clinical definitions and warning signs"
  - publisher: "NEJM or Annals of Internal Medicine"
    url: "[locate most recent heat stroke clinical review]"
    tier: 1
    used_for: "Pathophysiology and treatment evidence"

expert_sources:
  - type: Emergency medicine physician
    reason: Clinical recognition and emergency response to heat stroke
  - type: Public health official (CDC or state health department)
    reason: Population-level risk framing

seo:
  primary_keyword: "heat illness prevention"
  supporting_keywords:
    - "heat stroke symptoms"
    - "heat exhaustion vs heat stroke"
    - "how to prevent heat stroke"
    - "WHO heat advisory 2026"
    - "heat stroke treatment"
  format: "Explainer + symptom guide + prevention checklist"
  schema_markup: "FAQPage + HowTo"
  cluster: "Public health > Environmental health > Heat"

estimated_word_count: "1,200–1,500 words"

next_steps: >
  Assign immediately — seasonal urgency peak. Pull WHO July 31 advisory.
  Publish within 24–48 hours.
```

---

### BRIEF 5 — P2 / SHORT-TERM

```yaml
priority_level: P2
publish_timing: short_term
topic: Gen Z and millennials using AI as their first healthcare consultation — Aflac survey findings
primary_entity: AI in healthcare (patient-facing)
signal_type: data_release / audience_pain_point
allowed_category: mental health and psychology; public health and epidemiology
trend_strength_score: 65
opportunity_score: 68
discover_score: 4
urgency: this_week
confidence: Medium
content_status: new
source_count: 2
why_now: >
  Aflac's August 4, 2026 survey found 76% of Gen Z and 63% of millennials turn to AI before
  seeking professional medical care. Mental health Google Trends delta is +8; health delta is +12.
  AI health-seeking behavior is a rapidly emerging pattern with real public health implications
  (misinformation risk, delayed care, appropriate triage). SERP for this specific angle is open —
  existing content covers AI in hospital systems, not patient AI-first behavior.
recommended_angle: >
  "Why young people are consulting AI before doctors — and what that means for their health" —
  explain the survey findings, give context on when AI health guidance is appropriate vs. risky,
  include expert perspective on what this behavioral shift means for public health.

primary_headline: "76% of Gen Z Goes to AI Before a Doctor. Is That Dangerous — or Actually Useful?"
alternate_headlines:
  - "Young Adults Are Using AI as Their Primary Care. Here's What Experts Think."
  - "The AI Doctor Trend: What the Data Says About How Gen Z Handles Health Questions"

outline:
  sections:
    - The survey findings — what Aflac found, methodology note (survey, not clinical study)
    - Why this is happening — cost of care, access gaps, immediacy, comfort
    - When AI health guidance is actually appropriate (symptom triage, general information)
    - When it becomes dangerous (diagnostic delay, medication decisions, mental health crisis)
    - What clinical experts recommend — where AI fits in care-seeking
    - What AI tools get right and wrong about health advice (accuracy benchmarks if available)

integrity_flags:
  - "⚠️ Survey conducted by Aflac (insurance company with business interest in healthcare access) —
     note methodology and potential bias. Not peer-reviewed research."
  - "⚠️ Correlation ≠ causation — surveyed behavior may not reflect actual health outcomes.
     Frame as behavioral trend, not health risk study."

source_plan:
  - publisher: "Aflac press release"
    url: "https://newsroom.aflac.com/[ai-healthcare-survey-2026-08-04]"
    tier: 2
    used_for: "Survey data — 76%/63% figures"
    note: "[Verify exact URL from Aflac newsroom]"
  - publisher: "JAMA or BMJ (locate AI health accuracy benchmark study)"
    url: "[URL unverified]"
    tier: 1
    used_for: "AI diagnostic accuracy context"

expert_sources:
  - type: Health policy researcher or digital health expert
    reason: Systemic implications of AI-first health-seeking
  - type: Primary care physician
    reason: Clinical perspective on delayed professional care

seo:
  primary_keyword: "gen z AI healthcare"
  supporting_keywords:
    - "using AI for health advice"
    - "AI before doctor"
    - "AI health chatbot accuracy"
    - "AI primary care"
  format: "News analysis with FAQ"
  schema_markup: "FAQPage"
  cluster: "Public health > Digital health behavior"

estimated_word_count: "900–1,200 words"

next_steps: >
  Assign within 2 days. Verify Aflac survey methodology. Add physician or policy expert quote.
```

---

### BRIEF 6 — P2 / SHORT-TERM

```yaml
priority_level: P2
publish_timing: short_term
topic: Pistachio nut butter Walmart recall — Salmonella contamination
primary_entity: pistachio nut butter recall
signal_type: recall
allowed_category: FDA and CDC regulatory updates; nutrition and diet science
trend_strength_score: 70
opportunity_score: 65
discover_score: 3
urgency: today
confidence: Medium
content_status: new
source_count: 3
health_claim_gate:
  gate_result: pass_with_breaking_recall_exception
  breaking_recall_exception_used: true
  confidence_cap: medium
  notes: "KSNT News (08-03-2026) reports pistachio nut butter sold at Walmart recalled for Salmonella.
    Verify official FDA recall notice at FDA.gov before publishing. Egg/Salmonella recall covered
    08-01 but this is a distinct product/recall event."
why_now: >
  Pistachio nut butter sold at Walmart recalled for Salmonella, reported August 3, 2026.
  Separate from the egg recall covered August 1. Salmonella Google Trends real-time trending.
  Readers who purchased this specific product need actionable information (product names,
  lot codes, what to do). Short shelf life for recall content — publish and update as FDA
  notice is confirmed.
recommended_angle: >
  "What to do if you bought pistachio nut butter at Walmart" — focus on actionable consumer
  steps: product identification, whether to consume or discard, Salmonella symptoms and when
  to seek care, FDA reporting link.

primary_headline: "Pistachio Nut Butter Sold at Walmart Recalled Over Salmonella Risk — What to Do Now"
alternate_headlines:
  - "Salmonella Recall: Pistachio Nut Butter at Walmart Pulled from Shelves"
  - "Is Your Pistachio Nut Butter Part of the Walmart Recall? What to Know"

outline:
  sections:
    - What is being recalled — product name, brand, UPC/lot codes (from FDA notice)
    - Where it was sold — Walmart locations or national distribution
    - Why — Salmonella contamination (how detected, testing)
    - Salmonella symptoms — what to watch for, timeline, severity
    - What consumers should do — do not eat, return for refund, FDA MedWatch link
    - High-risk populations — elderly, immunocompromised, pregnant, young children

integrity_flags:
  - "⚠️ Breaking recall exception — FDA.gov official recall notice must be verified before
     publishing. Do not publish specific product/lot code claims without FDA confirmation."
  - "⚠️ Confidence Medium until FDA notice directly retrieved."

source_plan:
  - publisher: "FDA Recalls database"
    url: "https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts"
    tier: 1
    used_for: "Official recall notice — product name, lot codes, distribution scope"
    note: "Verify before publishing — search pistachio nut butter August 2026"
  - publisher: "KSNT 27 News"
    url: "https://www.ksnt.com/news/[pistachio-recall-walmart-2026-08-03]"
    tier: 2
    used_for: "Signal source"
  - publisher: "CDC Salmonella"
    url: "https://www.cdc.gov/salmonella/index.html"
    tier: 1
    used_for: "Salmonella symptom information and high-risk population guidance"

seo:
  primary_keyword: "pistachio nut butter recall Walmart"
  supporting_keywords:
    - "pistachio recall Salmonella"
    - "Walmart food recall 2026"
    - "pistachio butter recalled"
  format: "News brief + consumer action checklist"
  schema_markup: "NewsArticle"
  cluster: "FDA and CDC regulatory updates > Food recalls"

estimated_word_count: "600–800 words"

next_steps: >
  Verify FDA recall notice immediately. Publish within 24 hours once lot codes confirmed.
  Update as FDA notice expands.
```

---

### BRIEF 7 — P3 / SCHEDULED

```yaml
priority_level: P3
publish_timing: scheduled
topic: Legumes and heart health — what the evidence actually says
primary_entity: legumes
signal_type: evergreen_with_fresh_angle
allowed_category: nutrition and diet science; chronic disease management
trend_strength_score: 58
opportunity_score: 70
discover_score: 3
urgency: evergreen
confidence: Medium
content_status: new
source_count: 2

headline: "Are Legumes Actually Good for Your Heart? Here's What the Evidence Shows"

angle: >
  Harvard Health published a legumes + heart health piece August 3, 2026 — use this as the
  editorial hook but go deeper: summarize the current evidence base (RCTs, meta-analyses,
  dietary pattern studies), address common reader objections (digestive issues, phytates,
  protein quality), and give practical serving guidance. SERP is dominated by general listicles;
  opportunity to own the evidence-based explainer angle.

key_data_points:
  - Harvard Health Publishing (08-03-2026) on legume cardiovascular benefit
  - Multiple RCTs showing legume consumption lowers LDL cholesterol
  - AHA dietary pattern recommendations include legumes
  - Soluble fiber mechanism: bile acid sequestration → LDL reduction

integrity_flags:
  - "⚠️ Distinguish between association studies (dietary pattern) and RCT evidence for LDL reduction — grade evidence level explicitly."

sources:
  - publisher: "Harvard Health Publishing"
    url: "https://www.health.harvard.edu/heart-health/legumes-are-they-good-for-your-heart"
  - publisher: "American Heart Association"
    url: "https://www.heart.org/en/healthy-living/healthy-eating"
  - publisher: "Cochrane Library (legumes + cholesterol meta-analysis)"
    url: "https://www.cochranelibrary.com/ [search legumes cholesterol]"

expert_type_needed: Registered Dietitian Nutritionist (RDN) or cardiologist

seo:
  primary_keyword: "are legumes good for heart health"
  format: "Evidence-based explainer with FAQ"
  serp_difficulty: Medium

estimated_word_count: "1,000–1,300 words"
```

---

### BRIEF 8 — P3 / SCHEDULED

```yaml
priority_level: P3
publish_timing: scheduled
topic: Ibogaine for neurological recovery — new Barrow Institute clinical study
primary_entity: ibogaine
signal_type: clinical_trial
allowed_category: medical research and clinical trials
trend_strength_score: 55
opportunity_score: 67
discover_score: 3
urgency: this_week
confidence: Medium
content_status: new
source_count: 2
health_claim_gate:
  gate_result: pass_medium_cap
  primary_source_type: institutional_announcement
  confidence_cap: medium
  notes: "Barrow Neurological Institute announcement (News-Medical, 08-06-2026). Not yet
    peer-reviewed publication. Confidence capped at Medium. Frame as early-stage clinical study,
    not proven treatment."

headline: "Barrow Institute Is Testing Ibogaine for Brain Recovery. What Do We Know So Far?"

angle: >
  Ibogaine has attracted significant research interest after the 2024 Stanford study showing
  potential for PTSD and TBI in veterans. Barrow's new neurological recovery study is a logical
  extension. Opportunity to give readers a grounded explainer: what ibogaine is, where the
  evidence currently stands, why neurological recovery is a plausible target, and what the
  risks are. SERP for ibogaine neurological recovery is very thin; prior psilocybin/PTSD
  coverage (08-01) creates a good cluster opportunity.

key_data_points:
  - Barrow Neurological Institute launches clinical study — August 6, 2026
  - Ibogaine: psychedelic alkaloid from iboga plant; Schedule I in US
  - Prior research: 2024 Stanford/VA study on ibogaine for combat veterans (PTSD + TBI)
  - Mechanism: proposed GDNF upregulation, neuroplasticity effects
  - Legal status: Schedule I in US; legally available in some countries

integrity_flags:
  - "⚠️ Early-stage clinical study — not peer-reviewed, not proven treatment. State clearly."
  - "⚠️ Ibogaine has serious cardiac safety risks (QT prolongation) — must be covered. Do not
     present as accessible treatment option."
  - "⚠️ Schedule I status in US — legal status context is required."

sources:
  - publisher: "News-Medical"
    url: "https://www.news-medical.net/news/[barrow-ibogaine-2026-08-06].aspx"
    note: "[URL unverified — verify from News-Medical 08-06-2026]"
  - publisher: "Nature Medicine (2024 Stanford ibogaine study)"
    url: "https://www.nature.com/articles/s41591-023-02705-w"

expert_type_needed: Neurologist or addiction medicine specialist; pharmacologist

seo:
  primary_keyword: "ibogaine neurological recovery"
  format: "Clinical trial explainer"
  serp_difficulty: Easy

estimated_word_count: "900–1,200 words"
```

---

## REJECTED TOPICS LOG

| Topic | Rejection Reason |
|---|---|
| H5N1 bird flu — US human case | `content_status: existing` — covered 2026-08-05; no materially new case/advisory found in signal window |
| GLP-1 receptor agonists cardiovascular outcomes — NEJM RCT | `content_status: existing` — covered 2026-08-05 |
| RSV vaccine recommendation adults 60+ — CDC ACIP | `content_status: existing` — covered 2026-08-05 |
| Ultra-processed food + mortality — BMJ 30-year cohort | `content_status: existing` — covered 2026-08-05 |
| Menopause and cardiovascular risk — AHA statement | `content_status: existing` — covered 2026-08-05 |
| Sleep deprivation and immune function — meta-analysis | `content_status: existing` — covered 2026-08-05 |
| PFAS drinking water enforcement — EPA | `content_status: existing` — covered 2026-08-05 |
| Childhood obesity — updated AAP guidelines | `content_status: existing` — covered 2026-08-05 |
| Levothyroxine recall | `content_status: existing` — covered 2026-08-01 |
| E. coli outbreak frozen blueberries | `content_status: existing` — covered 2026-08-01 |
| Egg carton Salmonella recall (Class I) | `content_status: existing` — covered 2026-08-01 |
| Psilocybin-assisted therapy veterans — Nature Comm. Med. | `content_status: existing` — covered 2026-08-01 |
| Rohto eye drop recall | `content_status: existing` — covered 2026-08-01 |
| SAMHSA 2025 NSDUH data release | `content_status: existing` — covered 2026-08-01 |
| GLP-1 tailoring to metabolic profiles — Penn Medicine | `content_status: existing` — covered 2026-08-01 |
| Intermittent fasting / restricted eating + brain health | `content_status: existing` — covered 2026-08-01 |
| DMD cell therapy Phase 3 trial | `content_status: existing` — covered 2026-08-01 |
| Wellness influencers / nootropics 'natural Adderall' | `content_status: existing` — covered 2026-08-01 |
| CVS Health GLP-1 direct-to-consumer expansion | `content_status: existing` — GLP-1 covered 08-05; CVS announcement is a business story without materially new patient health data |
| Low-protein diet lifespan — rising query | `Skill 02b: Monitor` — rising Google Trends query but no traceable primary study found in signal window; routed to P5 |
| Coffee recall botulism risk (Class II) | `P5 Monitor` — FDA.gov Class II notice not directly retrieved; signal present but brief requires official notice verification before actioning |
| Celebrity health queries (Ariana Grande, Perez Hilton) | `off_category` — celebrity gossip; excluded category |
| Medicaid California rollback | `off_category` — pure health policy/political; excluded category |
| Local wellness destinations / wellness centers | `off_category` — local/regional; below national audience threshold |
| National Wellness Month generic coverage | `weak_signal` — editorial hook only; low differentiation; existing SERP saturated with identical content |
| AI in healthcare infrastructure / clinical trial simulations | `off_category` — healthcare technology infrastructure; not patient-facing health content |
| Ascend Wellness cannabis workers strike | `off_category` — labor/cannabis business; excluded |
| Medical research monkey protection policy | `off_category` — animal/regulatory policy; not health consumer content |
| AI training psychiatrists — WVU study | `weak_signal` — too narrow/institutional; no direct patient-audience value |
| ALS clinical trial Dallas | `weak_signal` — single regional trial signal; insufficient source corroboration for national-audience brief |

---

## INTEGRITY FLAGS — CONSOLIDATED

| Brief | Flag |
|---|---|
| **B1 Dronabinol RCT** | ⚠️ Single RCT — do not overstate clinical adoption readiness. Dronabinol ≠ cannabis. Not FDA-approved for PTSD. State explicitly. |
| **B1 Dronabinol RCT** | ⚠️ Confirm exact effect size and sample size from Nature paper before publishing — do not use secondary source estimates as primary data. |
| **B2 Birth order** | ⚠️ Association study — birth order does not cause disease. Individual risk is not determinable from population-level data. |
| **B3 Dementia 90+** | ⚠️ Confidence Medium — DOI not confirmed in signal window. Verify before assigning. |
| **B4 Heat illness** | ⚠️ Medication + heat risk section requires clinical source verification. Do not publish drug list from secondary sources alone. |
| **B5 AI healthcare** | ⚠️ Aflac survey = industry-funded. Note funder; do not present as independent research. |
| **B6 Pistachio recall** | ⚠️ Breaking recall exception — FDA.gov notice must be verified before publishing lot codes or distribution scope. |
| **B8 Ibogaine** | ⚠️ Ibogaine = Schedule I + cardiac safety risk (QT prolongation). Both must be covered. Do not frame as accessible treatment. |

---

## RUN NOTES

```yaml
run_date: 2026-08-06
signals_reviewed: ~144 (Google News Radar) + Google Trends rising queries
candidates_retained: 8
candidates_rejected: ~30+ (including 18 from recent coverage block)
p1_count: 2
p2_count: 4
p3_count: 2
p5_monitor: 3 (low-protein diet lifespan, coffee recall, CVS GLP-1)
integrity_flags_total: 8
tools_used: [serpapi_prefetch (Google Trends + Google News Radar injected)]
tools_unavailable: [direct RSS fetch, Reddit /new.json, live ExaSearch — simulated from injected radar]
self_check: skipped — site_url not configured; competitor coverage checked via Google News Radar
google_trends_available: true
search_velocity_source: google_trends (serpapi_prefetch)

recurring_theme_check: >
  GLP-1 receptor agonists appeared in run history on 08-01 (metabolic tailoring) and 08-05
  (cardiovascular NEJM RCT). CVS GLP-1 expansion surfaced today — flagged as existing/rejected.
  If GLP-1 appears again tomorrow without a materially new clinical development, flag as
  'recurring — check for staleness.'

notes: >
  Many Google Trends rising queries this week were celebrity-driven (Ariana Grande, Perez Hilton)
  with health search co-occurrence — rejected off-category. Gut health rising queries in the
  Trends pre-fetch were almost entirely off-topic artifacts (finance, AI, travel keywords),
  consistent with a Trends data quality issue for that term in the 7-day window; gut health
  candidates sourced from News Radar instead (none cleared threshold today). Two strong P1
  candidates from Nature publications (dronabinol RCT, birth order phenome study) represent
  the clearest opportunity gap of this run — well-sourced, peer-reviewed, thin SERP.
  Heat illness is the highest search-velocity topic (health delta +12) and should be treated
  as time-sensitive given current summer peak even though it is seasonal rather than breaking.
```