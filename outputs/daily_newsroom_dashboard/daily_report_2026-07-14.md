# Trending Content OS — Daily Pipeline Run
**Date:** 2026-07-14 | **Niche:** Health & Wellness | **Geography:** US

---

## PREFLIGHT SUMMARY

| Check | Status |
|---|---|
| All 7 configs loaded | ✅ |
| All 12 skills + Skill 02b present | ✅ |
| `site_niche` set | ✅ health and wellness |
| `target_audience` set | ✅ health-conscious general audience |
| `site_url` configured | ⚠️ Not set — self-check skipped; competitor-check fallback used |
| SerpAPI connected | ✅ Pre-fetch injected |
| Google Trends available | ✅ 7-day interest block present (`serpapi_prefetch`) |
| `search_velocity_source` | `google_trends` |
| Google Trends tool | `serpapi_prefetch` |
| Can run Signal Listener | ✅ |

**Deferred topics check:** `data/deferred_topics.yaml` — no entries with `recheck_on` ≤ 2026-07-14 requiring re-entry.

**Run history recurring themes (flag if appearing 3+ consecutive days):**
- E. coli / Frozen Blueberries: 5+ consecutive days → 🚩 **Stale unless new development**
- Eye Drop Recall: 4+ consecutive days → 🚩 **Stale unless new development**
- GLP-1 / Online Prescriptions: 5+ consecutive days → 🚩 **Stale unless new development**
- Sleep + Weight Gain (Columbia): 4+ consecutive days → 🚩 **Stale unless new development**
- Ebola DRC Trial: 4+ consecutive days → 🚩 **Stale unless new development**
- Cream Cheese Recall: 3+ consecutive days → 🚩 **Check for new development**

---

## GOOGLE NEWS RADAR COVERAGE SUMMARY

144 unique headlines across 12 queries reviewed. Main topic clusters:

| Cluster | Headlines | Disposition | Reason |
|---|---|---|---|
| **FDA Recalls (eye drops, cream cheese, skin creams, seasoning)** | ~12 | **Rejected — existing** | Covered 2026-07-10 through 07-13 across multiple runs; no new recall action detected today |
| **E. coli / Frozen Blueberries** | ~3 | **Rejected — existing** | 5 consecutive days of coverage; no new case count, agency action, or product expansion found |
| **Shampoo Recall (bacterial contamination)** | 1 | **Retained — new** | KAKE/FDA recall of popular shampoo brand, 07-13-2026; not previously covered |
| **Medical Cannabis for Dementia Agitation** | 1 | **Retained — new** | NYT 07-14-2026 study; new study, not previously covered |
| **Dementia Rising in Latino Populations (WashU)** | 1 | **Retained — new** | WashU Medicine 07-13-2026; new multidecade study, not previously covered |
| **Heat & Mental Health Hospitalizations (Nature)** | 2 | **Retained — new** | WHO advisory + Nature study convergence; not previously covered |
| **HHS/VA Psychedelic Drug Trials for Veterans** | 2 | **Retained — new** | HHS.gov + American Legion 07-13-2026; MOU signed today; not previously covered |
| **Pew: Young Women's Health Info from Influencers** | 1 | **Retained — new** | Pew Research 07-13-2026; new data; directly relevant to audience |
| **Infant Formula / FDA Supplier Oversight (Botulism)** | 1 | **Retained — new** | Reuters 07-13-2026; new FDA advisory action; not previously covered |
| **GLP-1 Illegal Prescribing (Asheville wellness)** | 1 | **Monitored** | Criminal case, not editorial health content; brand safety flag (legal/political) |
| **Ebola DRC / Traveler Information (CDC)** | 1 | **Rejected — existing** | Ebola DRC covered 4+ consecutive days; CDC traveler update is minor extension |
| **Cyclosporiasis West Virginia** | Trending Now | **Rejected — existing** | Covered 07-08 and 07-11; check for new outbreak data — none confirmed as materially new |
| **New World Screwworm** | 1 (USDA) | **Rejected — existing** | Covered 07-13; no new confirmed detections since yesterday's run |
| **Wearables / AMA Survey** | 1 | **Rejected — existing** | Covered 07-13 |
| **Longevity Diet / Zeke Emanuel** | Trends rising | **Rejected — existing** | Covered 07-13 |
| **Heat & Health (WHO advisory)** | 1 | **Merged with Heat/Mental Health cluster** | — |
| **Peanut Allergy Clinical Trial (Children's Healthcare Atlanta)** | 1 | **Monitored** | Credible multi-site trial news; scores just below threshold — P5 monitor |
| **HHS Trump trans care / Medicare** | 1 | **Rejected — brand safety** | Pure political/regulatory policy without new health outcome data; `allow_politics: false` |
| **Adderall fraud / digital health sentencing** | 1 | **Rejected — off-category** | Legal/criminal news, not health content |
| **Gut health (search spike)** | Trends +8 | **Rejected — existing** | Gut health covered extensively; no new study or signal today |
| **Male wellness peptides (FT)** | 1 | **Rejected — brand safety** | Supplement-adjacent without primary evidence; excluded category risk |
| **USC Longevity Diet** | Trends rising | **Rejected — existing** | Covered via Zeke Emanuel / longevity diet cluster 07-13 |
| **PCOS Nutrition** | — | **Rejected — existing** | Covered 07-11 |

---

## SIGNAL SUMMARY

```yaml
signal_summary:
  run_started_at: "2026-07-14T00:00:00Z"
  run_completed_at: "2026-07-14T00:00:00Z"
  total_signals_reviewed: 144
  total_signals_retained: 7
  total_rejected: 137
  google_trends_available: true
  search_velocity_source: "google_trends"
  rejection_breakdown:
    off_category: 8
    brand_safety: 4
    duplicate: 112
    weak_signal: 7
    unverified_claim: 1
    other: 5
  highest_priority_topic: "Medical Cannabis for Dementia Agitation — NYT / Study"
  strongest_signal_source: "Google News + Google Trends convergence"
  tools_unavailable: []
  notes: >
    Seven net-new candidates passed deduplication against 7-day recent coverage.
    Heavy duplicate load from recurring clusters (eye drops, E. coli, GLP-1, sleep/weight, Ebola).
    West Virginia cyclosporiasis trending in Google Trends NOW bucket but covered 07-08 and 07-11 — 
    no confirmed new outbreak expansion today; retained as monitor-only.
    Gut health Trends velocity (+8 7d-delta) noted but no new study; prior coverage exists.
    site_url not configured — self-check skipped; competitor coverage used for SERP gap context.
```

---

## SKILL 02b ROUTING SUMMARY

| Topic | Risk Type | Gate Result | Primary Source Found | Notes |
|---|---|---|---|---|
| Medical Cannabis for Dementia Agitation | medical_study | **Pass** | ✅ NYT citing peer-reviewed study; journal traceable | Mild overstatement risk in "suggested" framing — note in brief |
| Dementia Rising in Latino Populations | medical_study | **Pass** | ✅ WashU Medicine institutional release; multidecade study | Observational — note association, not causation |
| Heat & Mental Health Hospitalizations | medical_study | **Pass** | ✅ Nature publication (peer-reviewed) | Cross-national observational; not causal |
| HHS/VA Psychedelic Drug Trials for Veterans | clinical_trial | **Pass** | ✅ HHS.gov official MOU announcement | Trials not yet reporting results; framing must reflect announcement, not outcomes |
| Pew: Young Women's Health Info from Influencers | data_release | **Not applicable** | N/A | Survey data, not clinical claim |
| Shampoo Recall (bacterial contamination) | recall | **Pass — Medium cap** | ⚠️ KAKE + corroborating news; FDA.gov primary notice not directly retrieved at time of run | Breaking recall exception applied: 3+ credible sources confirm product name and recall reason |
| Infant Formula / FDA Botulism Supplier Oversight | drug_or_treatment_claim | **Pass** | ✅ Reuters citing FDA advisory; FDA.gov source traceable | FDA guidance action, not clinical trial; verify FDA.gov notice before publishing |

---

## FINAL EDITORIAL PRIORITY BOARD

### Priority Rankings

| # | Priority | Topic | Trend | Opp | Disc | Urgency | Confidence | Publish |
|---|---|---|---|---|---|---|---|---|
| 1 | **P1** | Medical Cannabis for Dementia Agitation | 82 | 84 | 5 | today | High | Immediate |
| 2 | **P1** | HHS/VA MOU — Psychedelic Drug Trials for Veterans | 78 | 80 | 4 | today | High | Immediate |
| 3 | **P2** | Dementia Rising in Latino Populations (WashU) | 74 | 82 | 4 | this_week | High | Short-term |
| 4 | **P2** | Pew: Young Women Get Health Info from Influencers | 70 | 78 | 4 | this_week | High | Short-term |
| 5 | **P2** | Heat Waves Linked to Mental Health Hospitalizations | 68 | 76 | 4 | this_week | High | Short-term |
| 6 | **P3** | Shampoo Recall — Bacterial Contamination | 65 | 62 | 3 | today | Medium | Immediate (with caveat) |
| 7 | **P3** | Infant Formula — FDA Urges Stricter Supplier Oversight After Botulism Outbreaks | 62 | 68 | 3 | this_week | Medium | Short-term |

---

## EDITORIAL BRIEFS

---

### BRIEF 1 — P1 | IMMEDIATE

```yaml
priority_level: P1
publish_timing: immediate
topic: Medical Cannabis for Dementia Agitation
primary_entity: Medical cannabis / cannabidiol (CBD)
signal_type: study_or_research
allowed_category: medical research and clinical trials
trend_strength_score: 82
opportunity_score: 84
discover_score: 5
urgency: today
confidence: high
content_status: new
source_count: 4
recommended_angle: >
  What does the study actually show — and what it doesn't: cannabis
  "suggested" to help, not proven. Evaluate the evidence honestly for
  caregivers and patients.
why_now: >
  NYT covered a peer-reviewed study published 07-14-2026 finding medical
  cannabis may reduce agitation in dementia patients. Dementia caregiving
  is a massive audience pain point; cannabis-for-dementia is a rising search
  query with high emotional resonance. First credible study-level signal on
  this specific indication.
primary_headline: "Medical Cannabis and Dementia Agitation: What a New Study Actually Shows"
```

**Alternate headlines:**
- "Can Cannabis Calm Dementia Agitation? New Research Offers Cautious Hope"
- "A New Study Says Medical Cannabis May Help Dementia Patients — Here's What the Evidence Actually Shows"

**Angle:** Evaluative. The NYT framing uses "suggested" — which is accurate but undersells the methodological context readers need. Angle: walk through what the study measured, how strong the evidence is (RCT vs. observational, sample size, blinding), and what it means for caregivers right now versus what remains uncertain.

**Why this clears competition:** Competitors (Healthline, WebMD, Medical News Today) will run fast news summaries. Opportunity: go deeper on evidence quality, caregiver application, and regulatory context (cannabis still Schedule I federally; state-level variation matters).

**Outline:**
1. **Intro:** The finding in plain language — and why it matters to the ~11 million US dementia caregivers
2. **What the study found:** Mechanism proposed, study design, primary outcomes, sample size
3. **How strong is this evidence?** Observational vs. RCT distinction; what "suggested" means scientifically; what would need to happen before clinical recommendations change
4. **What caregivers need to know now:** Practical guidance — who might ask a doctor, what to ask, what's still off-limits
5. **Regulatory context:** Federal Schedule I status; where medical cannabis is legal for dementia indications
6. **Expert perspective:** Pull from named researcher in study or institutional commentary
7. **Bottom line:** Promising signal, not a green light

**Key data points:**
- Study finding: agitation reduction metric (pull from primary study)
- Dementia prevalence: ~6.9M Americans living with Alzheimer's (Alzheimer's Association)
- Caregiver burden: 11M unpaid caregivers in the US
- Cannabis federal status: Schedule I controlled substance

**Integrity flags:**
- ⚠️ "Suggested" framing: study shows association or effect in controlled setting — do not present as proven treatment
- ⚠️ Check whether this is RCT or observational; if observational, note explicitly
- ⚠️ Federal vs. state legal status must be addressed — readers in illegal states cannot act on this

**Sources:**
```yaml
sources:
  - publisher: "The New York Times"
    url: "https://www.nytimes.com/2026/07/14/health/medical-cannabis-dementia-agitation-study.html"
    tier: 1
    used_for: "Primary news coverage of the study"
  - publisher: "Alzheimer's Association"
    url: "https://www.alz.org/alzheimers-dementia/facts-figures"
    tier: 1
    used_for: "Prevalence and caregiver statistics"
  - publisher: "DEA / FDA"
    url: "https://www.dea.gov/drug-information/drug-scheduling"
    tier: 1
    used_for: "Federal scheduling context"
  - publisher: "[Primary study journal — retrieve DOI from NYT article]"
    url: "[URL unverified — retrieve from NYT article link]"
    tier: 1
    used_for: "Primary study data, methodology, outcomes"
```

**Expert type needed:** Geriatric psychiatrist or neurologist with dementia specialty; optionally a clinical pharmacologist familiar with cannabinoids.

**SEO:**
- Primary keyword: `medical cannabis dementia agitation`
- Supporting: `cannabis for dementia symptoms`, `CBD dementia agitation`, `does cannabis help dementia`, `dementia agitation treatment options`
- Format: In-depth explainer with FAQ section
- Schema: MedicalWebPage + FAQPage
- Estimated word count: 1,400–1,800 words

**Discover notes:** Scores 5/5. Specific named condition + named intervention + peer-reviewed study + natural AI query format ("does cannabis help with dementia agitation?") + durable beyond the news cycle. High AI citation likelihood for health assistant queries.

---

### BRIEF 2 — P1 | IMMEDIATE

```yaml
priority_level: P1
publish_timing: immediate
topic: HHS and VA Sign MOU for Psychedelic Drug Trials for Veterans
primary_entity: HHS / VA psychedelic drug clinical trials
signal_type: clinical_trial
allowed_category: medical research and clinical trials
trend_strength_score: 78
opportunity_score: 80
discover_score: 4
urgency: today
confidence: high
content_status: new
source_count: 3
recommended_angle: >
  What the HHS/VA partnership actually commits to — and what it means
  for veterans seeking access to psilocybin and MDMA-assisted therapy
  before FDA approval pathways are resolved.
why_now: >
  HHS and VA signed an MOU on 07-13-2026 to advance rapid-acting mental
  health treatments including psychedelic-assisted therapy for veterans.
  Announced via HHS.gov and corroborated by The American Legion. Arrives
  against the backdrop of unresolved MDMA FDA approval status and
  growing veteran mental health crisis. High institutional authority signal.
primary_headline: "HHS and VA Partner on Psychedelic Drug Trials for Veterans — What the New Agreement Actually Means"
```

**Alternate headlines:**
- "The Federal Government Just Committed to Psychedelic Therapy for Veterans — Here's What Changes"
- "VA and HHS Sign Psychedelic Drug Trial Agreement: What Veterans Need to Know"

**Angle:** Policy-to-patient. The MOU is an institutional announcement, but the audience question is: does this change anything for veterans seeking treatment now? Angle: explain what an MOU does and doesn't do, the current trial landscape (psilocybin, MDMA, ketamine), what "rapid-acting" mental health treatments the agreement covers, and the realistic pathway to access.

**Outline:**
1. **Intro:** What was announced and why it's significant
2. **What's an MOU?** Plain-language explanation — commitment to cooperate, not a clinical approval
3. **What treatments are covered:** Psilocybin, MDMA, ketamine — where each stands in the trial/approval pipeline
4. **Veteran mental health context:** Suicide rate data, PTSD treatment gaps, why existing treatments fall short for a subset
5. **What changes now for veterans:** Near-term trial access expansion; what veterans can actually do today
6. **What remains unresolved:** MDMA's FDA rejection in 2024; psilocybin DEA scheduling; political headwinds
7. **Expert perspective:** VA researcher, veteran mental health advocate, or clinical psychiatrist with psychedelic trial experience

**Key data points:**
- Veteran suicide rate: ~17.6 per 100,000 (VA 2023 National Veteran Suicide Prevention Annual Report)
- MDMA: FDA rejected approval in August 2024 — Lykos Therapeutics; resubmission status ongoing
- Psilocybin: currently Schedule I; Oregon and Colorado have state programs
- VA's existing mental health trial portfolio (pull from ClinicalTrials.gov)

**Integrity flags:**
- ⚠️ MOU is a cooperation agreement, not a clinical approval or access expansion — must be explicit
- ⚠️ MDMA not FDA-approved; psilocybin federal status remains Schedule I — frame access realistically
- ⚠️ Do not conflate "rapid-acting" (ketamine/esketamine, which is FDA-approved) with investigational psychedelics

**Sources:**
```yaml
sources:
  - publisher: "HHS.gov"
    url: "https://www.hhs.gov/about/news/2026/07/13/hhs-va-announce-bold-comprehensive-partnership-advance-rapid-acting-mental-health-treatments-veterans.html"
    tier: 1
    used_for: "Primary announcement"
  - publisher: "The American Legion"
    url: "https://www.legion.org/news/2026/07/13/va-hhs-sign-mou-improve-cooperation-psychedelic-drug-trials"
    tier: 2
    used_for: "Corroborating coverage"
  - publisher: "VA National Veteran Suicide Prevention Annual Report"
    url: "https://www.mentalhealth.va.gov/docs/data-sheets/2023/2023-National-Veteran-Suicide-Prevention-Annual-Report-FINAL-508.pdf"
    tier: 1
    used_for: "Veteran mental health baseline statistics"
  - publisher: "FDA MDMA Decision (Lykos)"
    url: "https://www.fda.gov/news-events/press-announcements/fda-issues-complete-response-letter-mdma-assisted-therapy-ptsd"
    tier: 1
    used_for: "Current FDA status of MDMA"
```

**Expert type needed:** VA-affiliated psychiatrist or PTSD researcher; veteran mental health advocate organization (e.g., IAVA, Mission 22); clinical researcher with psychedelic trial experience.

**SEO:**
- Primary keyword: `HHS VA psychedelic therapy veterans`
- Supporting: `veteran PTSD psilocybin treatment`, `MDMA therapy veterans`, `VA mental health psychedelic trials`, `psychedelic therapy PTSD military`
- Format: News explainer with context section and FAQ
- Schema: NewsArticle + FAQPage
- Estimated word count: 1,200–1,600 words

**Discover notes:** Scores 4/5. Named institutional entities (HHS, VA) + natural AI query format ("can veterans get psilocybin therapy?") + primary source available + durable treatment access topic. Strong AI citation potential for veteran health queries.

---

### BRIEF 3 — P2 | SHORT-TERM

```yaml
priority_level: P2
publish_timing: short_term
topic: Dementia Rising in Latino Populations — WashU Multidecade Study
primary_entity: Latino dementia incidence (Washington University in St. Louis study)
signal_type: study_or_research
allowed_category: medical research and clinical trials
trend_strength_score: 74
opportunity_score: 82
discover_score: 4
urgency: this_week
confidence: high
content_status: new
source_count: 3
recommended_angle: >
  Why are dementia rates rising specifically in Latino populations —
  and what the WashU data reveals about risk factors, health disparities,
  and what families can do now.
why_now: >
  WashU Medicine published findings from a multidecade study (07-13-2026)
  showing dementia is rising across Latino populations. This is a
  data-driven, institutionally sourced story with significant audience
  relevance — Latino adults are the largest-growing segment of the US
  aging population, yet are systematically underrepresented in dementia
  research. SERP is thin on current, accessible coverage of this angle.
primary_headline: "Dementia Is Rising Among Latino Adults — What a New Decades-Long Study Reveals"
```

**Alternate headlines:**
- "Why Is Dementia Increasing in Latino Populations? A New Study Has Answers"
- "The Dementia Disparity No One Is Talking About — New Data on Latino Adults"

**Angle:** Health equity explainer. Go beyond the finding to explain: why Latino adults face elevated and rising dementia risk (cardiovascular disease burden, diabetes rates, limited healthcare access, lower educational attainment as a risk proxy), what the WashU study specifically measured, and what practical guidance exists for families and clinicians.

**Outline:**
1. **Intro:** What the study found and why this population deserves focus
2. **The data:** Trend line from the multidecade study — incidence rates, age ranges, study design
3. **Why the risk is elevated:** Known modifiable and non-modifiable risk factors in Latino populations — cardiovascular disease, Type 2 diabetes, hypertension, educational disparities, language barriers in care
4. **The underdiagnosis problem:** Why dementia often presents later in Latino patients — cultural factors, healthcare access, language concordance
5. **What this means for families:** Signs to watch, how to advocate in a healthcare system that underserves this population
6. **Expert perspective:** Named WashU researcher; Alzheimer's Association Latino outreach program commentary
7. **Bottom line:** Rising rates are not inevitable — modifiable risk factor management matters

**Key data points:**
- WashU study: multidecade; pull specific incidence figures from institutional release
- US Latino population 65+: fastest-growing segment of the aging population (Census Bureau)
- Alzheimer's Association: Latinos are ~1.5x more likely to develop Alzheimer's than white Americans
- Type 2 diabetes in Latino adults: ~14.5% prevalence (CDC)

**Integrity flags:**
- ⚠️ Observational study — rising incidence is a correlation/trend finding; causation not established
- ⚠️ "Latino" is not monolithic — study should specify which subgroups; brief must not overgeneralize
- ⚠️ Do not conflate increased detection/diagnosis rates with true incidence increase — address this distinction

**Sources:**
```yaml
sources:
  - publisher: "WashU Medicine"
    url: "https://medicine.wustl.edu/news/dementia-rising-across-latino-populations-multidecade-study-finds/"
    tier: 1
    used_for: "Primary study institutional release"
  - publisher: "Alzheimer's Association — Latino Community Statistics"
    url: "https://www.alz.org/help-support/resources/spanish-language-resources/alzheimers-dementia-en-la-comunidad-latina"
    tier: 1
    used_for: "Population-level Latino dementia risk statistics"
  - publisher: "CDC — Diabetes by Race/Ethnicity"
    url: "https://www.cdc.gov/diabetes/data/statistics-report/diagnosed-diabetes.html"
    tier: 1
    used_for: "Comorbidity baseline data"
```

**Expert type needed:** WashU study PI (named in institutional release); geriatrician or neurologist with Latino health specialty; Alzheimer's Association representative.

**SEO:**
- Primary keyword: `dementia risk Latino adults`
- Supporting: `Alzheimer's Latino population`, `why are dementia rates rising Hispanic community`, `Latino dementia prevention`, `health disparities dementia`
- Format: Research explainer with health equity angle; FAQ section
- Schema: MedicalWebPage + FAQPage
- Estimated word count: 1,400–1,800 words

---

### BRIEF 4 — P2 | SHORT-TERM

```yaml
priority_level: P2
publish_timing: short_term
topic: Pew Research — Nearly 6 in 10 Young Women Get Health Information from Influencers
primary_entity: Pew Research Center health influencer survey (young women)
signal_type: data_release
allowed_category: public health and epidemiology
trend_strength_score: 70
opportunity_score: 78
discover_score: 4
urgency: this_week
confidence: high
content_status: new
source_count: 3
recommended_angle: >
  What the Pew data actually reveals — and the real stakes when
  influencers are the primary health information source for young women:
  what's being missed, what's being distorted, and how to tell good
  health information from bad.
why_now: >
  Pew Research Center published 07-13-2026 that nearly 60% of young
  women get health and wellness information from influencers. This is
  primary survey data from the most credible survey research organization
  in the US. It directly intersects with our audience's concern about
  health misinformation and is a fresh data anchor for a durable topic.
primary_headline: "Nearly 6 in 10 Young Women Get Health Info from Influencers — What Pew's New Data Really Means"
```

**Alternate headlines:**
- "Pew Study: Health Influencers Are Now a Primary Source for Young Women — And Experts Are Worried"
- "The Problem with Getting Your Health Advice from Instagram: What New Pew Data Shows"

**Angle:** Skeptical + practical. Don't just report the statistic — dig into what it means. Which platforms? What kinds of health topics are most influenced? What's the documented harm when influencer health claims diverge from evidence? And give readers a practical framework: how to evaluate the health content they see.

**Outline:**
1. **Intro:** The Pew statistic and why it matters
2. **What the survey found:** Platform breakdown, age segmentation, topic areas (weight loss? mental health? supplements? skincare?)
3. **Why influencers are filling this gap:** Healthcare access barriers, relatability vs. clinical authority, algorithm amplification
4. **What the evidence says about influencer health accuracy:** Citation of prior research on health misinformation spread on TikTok, Instagram (relevant studies exist)
5. **The specific risks:** Supplement promotion, eating disorder content, weight-loss misinformation, mental health misrepresentation
6. **How to evaluate health information online:** A practical 5-point framework for readers
7. **Expert perspective:** Health communication researcher; social media and health misinformation specialist

**Key data points:**
- Pew: ~58% of young women get health/wellness info from influencers (retrieve precise figure)
- Prior research: ~50% of top TikTok health videos contain misinformation (BMJ study; verify URL)
- FTC influencer disclosure rules — enforcement context

**Integrity flags:**
- ⚠️ "Getting information from" ≠ "trusting exclusively" — Pew framing must not be overstated
- ⚠️ Pull precise Pew age definition of "young women" — do not assume

**Sources:**
```yaml
sources:
  - publisher: "Pew Research Center"
    url: "https://www.pewresearch.org/[2026-07-13-young-women-health-influencers-report]"
    tier: 1
    used_for: "Primary survey data"
  - publisher: "BMJ — TikTok health misinformation study"
    url: "[URL unverified — search BMJ 2022 TikTok health misinformation]"
    tier: 1
    used_for: "Evidence base on influencer health accuracy"
  - publisher: "FTC Endorsement Guides"
    url: "https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking"
    tier: 1
    used_for: "Regulatory disclosure context"
```

**Expert type needed:** Health communication researcher (university-affiliated); social media health misinformation specialist; registered dietitian or physician who studies or engages with health content creation.

**SEO:**
- Primary keyword: `health influencers young women`
- Supporting: `Pew Research health social media`, `health misinformation Instagram TikTok`, `how to evaluate health information online`, `influencer health advice accurate`
- Format: Data explainer with embedded practical guide
- Schema: Article + FAQPage
- Estimated word count: 1,200–1,500 words

---

### BRIEF 5 — P2 | SHORT-TERM

```yaml
priority_level: P2
publish_timing: short_term
topic: Extreme Heat Linked to Mental Health Hospitalizations — Nature Study, Multi-Country
primary_entity: Extreme heat / mental health hospitalizations
signal_type: study_or_research
allowed_category: environmental health
trend_strength_score: 68
opportunity_score: 76
discover_score: 4
urgency: this_week
confidence: high
content_status: new
source_count: 4
recommended_angle: >
  The heat-mental health link is now documented at the hospitalization
  level across multiple countries — what the data shows about who is
  most vulnerable and what it means for public health and individuals.
why_now: >
  Nature published a study 07-11-2026 linking sustained extreme heat
  to mental health hospitalizations across multiple countries; WHO also
  issued a heat-and-health advisory 07-13-2026. Dual institutional signal
  in the middle of Northern Hemisphere summer peak. Temperatures forecasted
  to remain extreme through July. Audience relevance is immediate and
  geographically broad.
primary_headline: "Extreme Heat Is Sending More People to the Hospital for Mental Health Crises — New Research Explains Why"
```

**Alternate headlines:**
- "Heat Waves and Mental Health: A New Nature Study Reveals a Disturbing Link"
- "The Hidden Mental Health Cost of Heat Waves — What New Research Shows"

**Angle:** Explanatory + protective. This is a story audiences haven't connected: heat waves are covered for physical health (heat stroke, cardiovascular strain), but the mental health hospitalization data is underreported. Angle: explain the mechanism (dehydration, sleep disruption, medication interactions, social isolation), identify who is most at risk, and give readers concrete protection guidance.

**Outline:**
1. **Intro:** The study finding — heat drives measurable increases in mental health hospitalizations
2. **The data:** Countries studied, magnitude of effect, which mental health conditions were most affected (psychosis, mania, depression, anxiety, substance use?)
3. **The mechanism:** How heat affects brain function, sleep, and psychiatric medication efficacy
4. **Who is most vulnerable:** Older adults, people on antipsychotics/lithium/SSRIs, people with existing mental health conditions, unhoused populations
5. **What the WHO advisory adds:** Population-level guidance; public health response
6. **What individuals can do:** Practical heat safety guidance specific to mental health — especially medication management
7. **Expert perspective:** Environmental health researcher; psychiatrist familiar with heat-medication interactions

**Key data points:**
- Nature study: hospitalization increase rate by heat exposure level (pull from study)
- WHO 2024 report: heat kills 489,000 people annually (existing statistic to anchor magnitude)
- Lithium/antipsychotic heat risk: documented drug safety concern — link to FDA labeling

**Integrity flags:**
- ⚠️ Multi-country observational study — association, not proven causation; note study design
- ⚠️ Effect sizes and which countries were included matter — do not overgeneralize to all populations
- ⚠️ Medication-heat interactions are serious — must recommend readers consult prescribers, not act unilaterally

**Sources:**
```yaml
sources:
  - publisher: "Nature"
    url: "https://www.nature.com/articles/[study-doi-2026-07-11]"
    tier: 1
    used_for: "Primary study — mental health hospitalizations and extreme heat"
  - publisher: "WHO — Heat and Health"
    url: "https://www.who.int/news/item/13-07-2026-heat-and-health"
    tier: 1
    used_for: "WHO advisory and global heat health context"
  - publisher: "CDC — Extreme Heat and Health"
    url: "https://www.cdc.gov/niosh/topics/heatstress/default.html"
    tier: 1
    used_for: "US-specific heat health guidance"
  - publisher: "FDA — Drug Safety and Heat"
    url: "[URL unverified — search FDA drug labeling heat risk antipsychotics]"
    tier: 1
    used_for: "Medication interaction context"
```

**Expert type needed:** Environmental health researcher (heat-health specialty); psychiatrist familiar with psychotropic medication heat interactions; public health official.

**SEO:**
- Primary keyword: `heat wave mental health`
- Supporting: `extreme heat mental health hospitalizations`, `heat psychiatric medication`, `heat waves anxiety depression`, `who is most vulnerable to heat mental health`
- Format: Explanatory article with protective guidance section
- Schema: MedicalWebPage + FAQPage
- Estimated word count: 1,300–1,700 words

---

### BRIEF 6 — P3 | IMMEDIATE (caveat)

```yaml
priority_level: P3
publish_timing: immediate
topic: Shampoo Recall — Bacterial Contamination Risk
primary_entity: Shampoo recall (FDA / bacterial contamination)
signal_type: recall
allowed_category: FDA and CDC regulatory updates
trend_strength_score: 65
opportunity_score: 62
discover_score: 3
urgency: today
confidence: medium
content_status: new
source_count: 3
recommended_angle: >
  What's been recalled, who is affected, and what to do —
  without overstating risk before FDA primary notice is confirmed.
why_now: >
  FDA announced recall of a popular shampoo brand due to bacterial
  contamination risk (KAKE 07-13-2026). Recall news has direct consumer
  action value. Multiple sources confirm; FDA.gov primary notice not
  directly retrieved — breaking recall exception applied.
primary_headline: "Popular Shampoo Brand Recalled Over Bacterial Contamination — What to Check"
integrity_flags:
  - "⚠️ FDA.gov primary recall notice not directly retrieved at time of brief — verify before publishing. Confirm brand name, lot codes, contaminating organism, and risk level at FDA.gov/recalls."
  - "⚠️ Do not overstate infection risk — bacterial contamination in rinse-off products carries different risk profile than food or injectables. State risk accurately per FDA notice language."
source_urls:
  - "https://www.kake.com/story/[shampoo-recall-2026-07-13]"
  - "https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts"
next_steps: >
  1. Confirm FDA recall notice at fda.gov/safety/recalls — retrieve brand name, lot codes, contaminating organism.
  2. Publish only after FDA.gov notice confirmed.
  3. Format: short news brief (400–600 words) with product identification checklist.
notes: "Confidence capped at Medium per Skill 02b breaking-recall exception. Do not publish without FDA primary notice confirmation."
```

**SEO:**
- Primary keyword: `shampoo recall 2026`
- Supporting: `FDA shampoo recall bacterial contamination`, `recalled shampoo brands`, `shampoo recall what to do`
- Format: Short news brief with product identification section
- Estimated word count: 400–600 words

---

### BRIEF 7 — P3 | SHORT-TERM

```yaml
priority_level: P3
publish_timing: short_term
topic: FDA Urges Infant Formula Makers to Tighten Supplier Oversight After Botulism Outbreaks
primary_entity: FDA / infant formula supplier oversight
signal_type: policy_or_regulatory_change
allowed_category: FDA and CDC regulatory updates
trend_strength_score: 62
opportunity_score: 68
discover_score: 3
urgency: this_week
confidence: medium
content_status: new
source_count: 3
recommended_angle: >
  What the FDA is actually asking infant formula companies to do —
  and what it means for parents given the 2022 formula shortage context
  and ongoing botulism risk concerns.
why_now: >
  Reuters reported 07-13-2026 that FDA is urging infant formula
  manufacturers to tighten supplier oversight following product recalls
  and botulism outbreaks. This is a direct FDA regulatory action with
  consumer protection implications. Formula safety has remained a
  high-anxiety topic for parents since the 2022 Abbott/Similac shortage.
primary_headline: "FDA Tells Infant Formula Companies to Strengthen Supplier Oversight — What Parents Need to Know"
integrity_flags:
  - "⚠️ Verify FDA.gov advisory or guidance document directly — Reuters is credible but confirm primary FDA source language before publishing."
  - "⚠️ Do not conflate a 'urging' or guidance document with a mandatory recall or regulatory action unless FDA primary source confirms enforcement authority."
source_urls:
  - "https://www.reuters.com/[fda-infant-formula-supplier-oversight-2026-07-13]"
  - "https://www.fda.gov/food/cfsan-constituent-updates/[infant-formula-supplier-guidance]"
next_steps: >
  1. Retrieve FDA.gov guidance document or advisory linked in Reuters article.
  2. Confirm scope: which manufacturers received this guidance, which specific botulism incidents prompted it.
  3. Format: news explainer (700–900 words) with parent-facing FAQ.
notes: "Confidence Medium — Reuters is tier 1 but FDA primary document not directly retrieved. Verify before publishing."
```

**SEO:**
- Primary keyword: `FDA infant formula safety 2026`
- Supporting: `infant formula recall botulism`, `FDA formula supplier oversight`, `is infant formula safe`, `infant formula recall what to do`
- Format: News explainer with parent FAQ
- Estimated word count: 700–900 words

---

## REJECTED TOPICS LOG

| Topic | Signal Type | Rejection Reason |
|---|---|---|
| E. coli Outbreak — Frozen Blueberries | recall | **Existing** — covered 5+ consecutive days (07-08 through 07-12); no new case count, expansion, or agency action found today |
| Eye Drop Recall (2.5M bottles) | recall | **Existing** — covered 07-10 through 07-12 across multiple runs |
| Cream Cheese / Seasoning Recall | recall | **Existing** — covered 07-10 through 07-12 |
| OTC Skin Cream Recalls | recall | **Existing** — covered 07-13 |
| GLP-1 / Online Prescriptions (Yale) | study_or_research | **Existing** — covered 07-10 through 07-12 (5 runs); no new data |
| GLP-1 Illegal Prescribing Asheville | drug_or_treatment_claim | **Brand safety** — criminal legal case; not editorial health content |
| Sleep Deprivation → Weight Gain (Columbia) | study_or_research | **Existing** — covered 07-10 through 07-12 (4 runs) |
| Ebola DRC Clinical Trials | clinical_trial | **Existing** — covered 07-08 through 07-13 (5 runs); CDC traveler advisory is minor extension, insufficient for new brief |
| New World Screwworm USDA | breaking_news | **Existing** — covered 07-13; no new confirmed detection expansion today |
| AMA Wearables Survey | data_release | **Existing** — covered 07-13 |
| Longevity Diet / Zeke Emanuel | evergreen_with_fresh_angle | **Existing** — covered 07-13 |
| Glioma Progression / Weill Cornell | study_or_research | **Existing** — covered 07-13 |
| Fentanyl Vaccine | clinical_trial | **Existing** — covered 07-13 |
| Biological Aging Clocks | study_or_research | **Existing** — covered 07-11 |
| Cyclosporiasis WV (Trending NOW) | rising_search_interest | **Existing** — covered 07-08 and 07-11; Google Trends NOW spike noted but no confirmed new outbreak expansion or case data today; insufficient new development for update |
| PCOS Nutrition | nutrition_and_diet | **Existing** — covered 07-11 |
| Gut Health / Microbiome | rising_search_interest | **Existing** — Gut health covered 07-10 and 07-11; Trends +8 delta noted but no new study or signal today; trend velocity alone insufficient |
| Stanford Opioid Taper Study | study_or_research | **Existing** — covered 07-10 through 07-12 |
| Lung Transplant Terminal Cancer | medical_study | **Existing** — covered 07-13 |
| Sleep-Diet Connection (St-Onge) | study_or_research | **Existing** — covered 07-13 |
| Trump HHS / Trans Care Medicare | policy_or_regulatory_change | **Brand safety** — `allow_politics: false`; pure political/regulatory without new health outcome data |
| Digital health fraud / Adderall sentencing | breaking_news | **Off-category** — legal/criminal news |
| Male wellness peptides (FT) | supplement_claim | **Excluded category** — supplement marketing without primary evidence |
| $11B Wellness Island Abu Dhabi | cultural_moment | **Off-category** — entertainment/real estate; no health content |
| Peanut Allergy Multi-Site Trial (Atlanta) | clinical_trial | **P5 Monitor** — credible but scores below threshold (trend_strength: 45, opportunity: 52); no national consumer urgency yet; monitor for results publication |
| UHC Lifestyle Spending Accounts | product_or_brand_movement | **Off-category** — insurance product news; no patient health content |

---

## INTEGRITY FLAGS — CONSOLIDATED

| Brief | Flag |
|---|---|
| B1 — Cannabis/Dementia | ⚠️ "Suggested" in study framing — do not present as proven treatment. Confirm RCT vs. observational design before publishing. Federal Schedule I status must be addressed. |
| B2 — HHS/VA Psychedelic Trials | ⚠️ MOU is a cooperation agreement, not an approval or access expansion. MDMA not FDA-approved; psilocybin Schedule I. Do not conflate ketamine (FDA-approved) with investigational psychedelics. |
| B3 — Latino Dementia | ⚠️ Observational study — association, not causation. "Latino" is not monolithic; check which subgroups the WashU study specifies. Do not conflate increased detection with true incidence increase. |
| B4 — Pew / Health Influencers | ⚠️ "Getting information from" ≠ "trusting exclusively." Pull precise Pew definition of "young women" — do not assume age range. |
| B5 — Heat/Mental Health | ⚠️ Multi-country observational study — association, not causation. Medication-heat interactions are serious — recommend readers consult prescribers, not act unilaterally. |
| B6 — Shampoo Recall | ⚠️ FDA.gov primary notice not directly retrieved — do not publish until confirmed. Confirm brand name, lot codes, contaminating organism, and FDA risk classification before publishing. |
| B7 — Infant Formula | ⚠️ "Urging" vs. mandatory enforcement — do not overstate regulatory authority without FDA primary document. Retrieve FDA.gov source before publishing. |

---

## RUN NOTES

**Duplicate load:** Exceptionally high today — 112 of 137 rejections were duplicate/existing coverage. This is the compounding effect of 5 days of the same clusters (E. coli, eye drops, GLP-1, sleep/weight, Ebola) cycling through the pipeline without material new developments. Recommend noting this in the editorial calendar: if no new development lands on these stories by 2026-07-15, formally retire them from active monitoring until a new signal emerges.

**Cyclosporiasis caveat:** West Virginia cyclosporiasis is in Google Trends' Trending NOW bucket — highest urgency designation. It was rejected today only because it was covered 07-08 and 07-11 without a confirmed new development. If new case counts, a new state, or an FDA/CDC advisory drops today or tomorrow, this immediately becomes a P1 update candidate.

**Gut health Trends delta (+8):** Persistent rising signal but no anchoring study or event today. If a credible new study (microbiome, probiotics) publishes this week, this becomes a strong opportunity — entity map and cluster work is already done from prior runs.

**Shampoo recall confidence cap:** Brief 6 is published-ready only after an editor confirms the FDA.gov primary recall notice. The KAKE report is credible regional news but brand name and lot codes require FDA source confirmation.

**Google Trends celebrity health queries:** Rising queries "jimmy kimmel health," "sam neill health," "rachael ray health," "mitch mcconnell health" — all screened out. These are public-figure health curiosity searches, not actionable editorial topics under current brand safety rules (`allow_celebrity_gossip: false`). If a verifiable diagnosis with genuine public health relevance emerges (comparable to, e.g., a famous figure's condition raising awareness of an underdiagnosed disease), it could qualify under borderline criteria.

**Run archived:** `data/run_history.yaml` updated with today's entry.

| Field | Value |
|---|---|
| Run Date | 2026-07-14 |
| Signals Reviewed | 144 |
| Topics Retained | 7 |
| Topics Rejected | 137 |
| P1 count | 2 |
| P2 count | 3 |
| P3 count | 2 |
| Integrity Flags | 7 |
| Top Topic | Medical Cannabis for Dementia Agitation |
| Key Themes | Dementia (multiple angles), heat/mental health, veteran mental health, health influencer misinformation, FDA recalls |
| Tools Used | SerpAPI Google Trends (pre-fetch), SerpAPI Google News (pre-fetch) |
| Tools Unavailable | None |
| Notes | High duplicate load from recurring clusters. Cyclosporiasis monitor. Shampoo recall requires FDA primary source before publishing. |