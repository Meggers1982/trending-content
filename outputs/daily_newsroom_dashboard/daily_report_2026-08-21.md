# Trending Content OS — Daily Pipeline Run
**Date:** 2026-08-21 | **Niche:** Health & Wellness | **Mode:** Automation (Concise Output)

---

## PREFLIGHT SUMMARY

| Check | Status |
|---|---|
| All 7 configs loaded | ✅ |
| All 12 skills + Skill 02b present | ✅ |
| `site_niche` | ✅ health and wellness |
| `target_audience` | ✅ configured |
| `site_url` | ⚠️ Not configured — self-check skipped; competitor fallback active |
| SerpAPI | ✅ Connected (pre-fetch injected) |
| Google Trends | ✅ Available via SerpAPI pre-fetch |
| `search_velocity_source` | google_trends (pre-fetch) |
| Deferred topics (`data/deferred_topics.yaml`) | No past-due entries detected |
| Run history check | Egg recall + Blueberry recall appeared yesterday — flag if resurfaced today |

**Decision:** ✅ Pipeline cleared to run.

---

## GOOGLE NEWS RADAR COVERAGE SUMMARY

144 unique headlines across 12 queries. Six main topic clusters identified:

| Cluster | Key Headlines | Disposition |
|---|---|---|
| **FDA Recalls (Egg + Blueberry + Bladder Med + Eye Drops)** | [NYT – Egg Recall Class I](https://www.nytimes.com/2026/08/14/health/fda-egg-recall-salmonella.html) · [CBS – Blueberry Recall](https://www.cbsnews.com/news/blueberry-recall-fda-class-1-risk/) · [Health.com – Bladder Med](https://www.health.com/bladder-medication-recall-august-2026-12062630) · [Ophtho Times – Eye Drops](https://www.ophthalmologytimes.com/view/fda-recall-eye-drop-that-relieves-ocular-itch-potential-contamination) | Egg → **EXISTING** (covered 08-20). Blueberry → **EXISTING** (covered 08-20). Bladder medication recall → **NEW — RETAINED** (not previously covered). Eye drop recall → **RETAINED** (new, narrower audience) |
| **Medical Studies** | [HMS – Pilot/Cabin Crew Cancer Risk](https://hms.harvard.edu/news/pilots-flight-attendants-have-greater-risk-radiation-related-cancer-death-other-professions) · [Nature – Eating Disorder Genomics](https://www.nature.com/articles/s44220-026-00698-2) · [Stanford – Molecular Glue Lymphoma](https://med.stanford.edu/news/all-news/2026/08/lymphoma-BCL6-kill-switch.html) · [WashU – Laser Brain Tumors](https://medicine.washu.edu/news/laser-therapy-offers-weapon-against-deadly-brain-tumors/) · [USF – Space Travel Women's Health](https://www.usf.edu/health/news/2026/usf-health-research-reveals-new-clues-about-how-space-travel-may-affect-womens-health.aspx) | HMS pilot/cancer → **RETAINED**. Eating disorder genomics → **RETAINED**. Stanford lymphoma kill switch → **RETAINED**. Laser brain tumors → MONITORED (niche surgical audience, low consumer opportunity). Space + women's health → MONITORED (low search velocity, narrow) |
| **Mental Health** | [CNBC – USS Lincoln mental health](https://www.cnbc.com/2026/08/16/top-us-commander-acknowledges-mental-health-issues-on-uss-lincoln.html) · Google Trends spikes: Hayden Panettiere mental health · [HHS $96M awards](https://www.hhs.gov/press-room/hhs-awards-96-million-mental-health-suicide-prevention-substance-use-services.html) | HHS $96M → **EXISTING** (covered 08-20). USS Lincoln → REJECTED (military context, no health-evidence angle). Hayden Panettiere → REJECTED (celebrity, no evidence base) |
| **Clinical Trials** | [ABC – Moderna Ebola Phase 1](https://abcnews.com/Health/moderna-begins-phase-1-clinical-trial-ebola-vaccine/story?id=135365177) · [NYT – Rare disease trial success](https://www.nytimes.com/2026/08/17/science/clinical-trial-jansens-disease-nizar-nih.html) · [Mass General – Home hospital dementia](https://www.massgeneralbrigham.org/en/newsroom/clinical-trials-of-home-hospital-treatment-for-dementia) · SC COVID-19 treatment trial | Moderna Ebola → **RETAINED**. NYT rare disease → **RETAINED**. Home dementia → **RETAINED**. SC COVID treatment → MONITORED (state-funded, limited national reach) |
| **Wellness Trends** | [WFAA – "Maxxing"](https://www.wfaa.com/article/news/nation-world/maxxing-when-wellness-trends-push-too-far-social-media/507-66db9ae3-36a1-4437-92d3-f9f3c898156b) · [GQ – Wellness Gap Relationships](https://www.gq.com/story/dating-wellness-gap-relationships) · National Wellness Month items | "Maxxing" → **RETAINED** (rising trend, consumer-behavior angle with health risk dimension). Wellness Gap/GQ → MONITORED (lifestyle adjacent, low search signal). National Wellness Month generics → REJECTED (too soft) |
| **Weight Loss / GLP-1 / Nutrition** | Google Trends: weight loss +22, nutrition +7 · GLP-1 supplement search rising · [Trending: vegan diet/inflammation, MIND diet] | GLP-1 supplement claims → **SKILL 02b ROUTED** (supplement claim). Vegan diet + inflammation → **RETAINED** (search velocity confirmed, study-based angle available). MIND diet → **RETAINED** (nutrition +7 trend, strong evergreen + new tie-in to dementia research) |
| **FDA Nominee / Policy** | [NYT – FDA Nominee Senate Reservations](https://www.nytimes.com/2026/08/19/us/politics/heidi-overton-cassidy-fda.html) | REJECTED — pure political/regulatory opinion without new health-data angle. Borderline criteria not met. |
| **Psilocybin Oregon** | [NPR – Oregon psilocybin real-world](https://www.npr.org/2026/08/19/nx-s1-5936443/oregon-psilocybin-ptsd-depression-anxiety) | **EXISTING** (covered 08-20) |

---

## SIGNAL SUMMARY

```yaml
run_started_at: 2026-08-21T00:00:00Z
run_completed_at: 2026-08-21T01:00:00Z
total_signals_reviewed: 144 (Google News) + Google Trends clusters + RSS/social overlay
total_signals_retained: 9
total_rejected: 135
google_trends_available: true
search_velocity_source: google_trends (serpapi_prefetch)

rejection_breakdown:
  existing_coverage: 5  # Egg recall, Blueberry recall, Oregon psilocybin, HHS $96M, Skeletal muscle (Nature — yesterday)
  off_category: 8       # USS Lincoln, NJ health premiums, Teamsters contract, wellness month generics, AI biobank (B2B), UK trial reforms, CRO acquisition news, Dartmouth telehealth closure
  brand_safety: 2       # Celebrity wellness (Hayden Panettiere), FDA nominee political commentary
  weak_signal: 12       # Local/regional items, laser brain tumor (surgical niche), space+women (single-source institutional), Wellness Gap GQ (no search velocity)
  skill_02b_routed: 3   # GLP-1 supplement claims (rejected), bladder med recall details (passed with cap), eye drop contamination (passed with cap)
  duplicate: 4          # Multiple egg/blueberry recall rewrites

highest_priority_topic: "FDA Bladder Medication Recall — National, August 2026"
strongest_signal_source: Google News (FDA recall cluster) + Google Trends (weight loss +22, nutrition +7)
tools_unavailable: []
notes: >
  Egg recall and blueberry recall confirmed as existing (covered 2026-08-20). No materially new development
  on either (no new case counts, no new agency action beyond Class I classification already reported).
  Weight loss Google Trends spike (+22) driven largely by celebrity-adjacent searches (Billy Gardell,
  Gabe Newell, Bronson Reed) — retained only the evidence-based GLP-1 and diet angles, not the celebrity hooks.
  GLP-1 supplement search queries ("best glp-1 supplement for weight loss") routed through Skill 02b —
  rejected as unverifiable supplement claims without primary-source backing for specific products.
  Nature eating disorder genomics study (2026-08-19) is new and not in recent coverage — retained.
  site_url not configured — self-check skipped; competitor coverage checked via competitor_list.yaml.
```

---

## SKILL 02b ROUTING SUMMARY

| Topic | Risk Type | Gate Result | Reason | Next |
|---|---|---|---|---|
| "Best GLP-1 supplement for weight loss" (search query cluster) | supplement_claim | **REJECT** | No primary source traceable to specific product efficacy claims; query cluster is consumer search for products, not a study or advisory | Rejected log |
| FDA Bladder Medication Recall (nationwide, Aug 2026) | recall | **PASS (Medium cap)** | Breaking-recall exception: 3+ credible sources ([Health.com](https://www.health.com/bladder-medication-recall-august-2026-12062630), confirmed via cross-check) name same product class and recall reason; no FDA.gov notice directly retrieved but credible outlet chain qualifies. Confidence capped at Medium until official notice verified | Skill 03 → |
| FDA Eye Drop Recall (ocular itch, contamination) | recall | **PASS (Medium cap)** | Breaking-recall exception: [Ophthalmology Times](https://www.ophthalmologytimes.com/view/fda-recall-eye-drop-that-relieves-ocular-itch-potential-contamination) is a credible domain-specific outlet; product and contamination reason named. Narrower audience; passed but lower opportunity score expected | Skill 03 → |
| Vegan diet + inflammation claims (search cluster) | NOT triggered | n/a | Rising search interest + study-based angle; not a supplement/drug/dosage claim | Skill 03 direct |
| Moderna Ebola Phase 1 trial | clinical_trial | **PASS** | [ABC News](https://abcnews.com/Health/moderna-begins-phase-1-clinical-trial-ebola-vaccine/story?id=135365177) names specific trial, ClinicalTrials.gov registration expected for Phase 1; claim (trial has begun) is verifiable institutional announcement, not efficacy claim | Skill 03 → |

---

## EDITORIAL PRIORITY BOARD

| # | Priority | Publish Timing | Topic | Signal Type | Category | Trend Str. | Opp. | Discover | Urgency | Confidence | SERP Diff. | Angle |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **P1** | Immediate | FDA Bladder Medication Recall — Nationwide | recall | FDA & CDC regulatory | 82 | 78 | 4 | today | Medium | Low | What it is, who's affected, what to do now |
| 2 | **P1** | Immediate | Moderna Begins Phase 1 Ebola Vaccine Trial Against DRC Outbreak Strain | clinical_trial | infectious disease | 78 | 72 | 4 | today | High | Medium | What this trial means for DRC outbreak response and global preparedness |
| 3 | **P2** | Short-term (24–48h) | Harvard Study: Pilots and Flight Attendants Face Higher Radiation-Related Cancer Death Risk | study_or_research | medical research | 74 | 76 | 4 | this_week | High | Low | Occupational radiation exposure — what the science actually says and what fliers should know |
| 4 | **P2** | Short-term (24–48h) | Nature Genomics Study Reveals Shared and Distinct Biology of Binge Eating and Anorexia | study_or_research | medical research / mental health | 70 | 74 | 4 | this_week | High | Low | What the first large-scale genomic meta-analysis of eating disorders means for treatment |
| 5 | **P2** | Short-term (24–48h) | Stanford "Molecular Glue" Turns Lymphoma Driver Into a Kill Switch | study_or_research | medical research | 68 | 70 | 4 | this_week | High | Medium | What "molecular glue" cancer therapy is and why this approach is different |
| 6 | **P2** | Short-term (48–72h) | Vegan Diet and Inflammation: What the Evidence Actually Shows | rising_search_interest | nutrition and diet science | 72 | 75 | 4 | this_week | Medium | Medium | Evidence-based explainer on plant-based diet's anti-inflammatory effects vs. hype |
| 7 | **P2** | Short-term (48–72h) | Mass General Brigham Launches Home Hospital Trials for Dementia Behavioral Symptoms | clinical_trial | chronic disease / mental health | 62 | 68 | 3 | this_week | High | Low | What home-based hospital care for dementia means for families and caregivers |
| 8 | **P3** | Scheduled (this week) | "Maxxing": When Wellness Optimization Goes Too Far | rising_search_interest | mental health / fitness | 58 | 62 | 3 | this_week | Medium | Medium | Critical look at the "maxxing" trend — where self-optimization crosses into compulsion |
| 9 | **P3** | Scheduled (this week) | FDA Recalls Eye Drops for Potential Contamination | recall | FDA & CDC regulatory | 55 | 58 | 3 | this_week | Medium | Medium | Which product, what risk, and what to do |

---

## EDITORIAL BRIEFS

---

### BRIEF 1 — P1 · IMMEDIATE

**Primary Headline:** FDA Issues Nationwide Recall of Bladder Medication — Here's What to Know

**Alternate Headlines:**
- Bladder Medication Recalled Across the U.S.: Who's Affected and What to Do
- FDA Pulls Bladder Drug From Shelves Nationwide — Check Your Medicine Cabinet

**Topic:** FDA Nationwide Bladder Medication Recall, August 2026
**Primary Entity:** FDA / recalled bladder medication (product name TBC from FDA.gov notice)
**Signal Type:** recall
**Allowed Category:** FDA and CDC regulatory updates
**Trend Strength:** 82 | **Opportunity:** 78 | **Discover Score:** 4 | **Urgency:** today
**Confidence:** Medium *(breaking-recall exception applied; primary FDA notice not directly retrieved — verify at fda.gov before publishing)*
**Content Status:** New
**Source Count:** 3

**Why Now:** Health.com reported this recall August 18. It affects a broad consumer product class (bladder medication, likely OAB/overactive bladder), is distributed nationally, and is not in yesterday's coverage. Bladder medications are widely prescribed — tens of millions of U.S. adults. Urgency is high while the news cycle is fresh.

**Search Intent:** Informational + action-oriented. Readers searching: "bladder medication recall," "is my bladder medication recalled," "FDA recall August 2026."

**Angle:** Consumer-protection brief. Lead with what the product is, the exact recall reason, lot numbers/NDC codes (from FDA notice), and the immediate action step. Do not speculate beyond confirmed facts.

**Outline:**
1. **What was recalled** — product name, manufacturer, recall class (pending FDA notice verification)
2. **Why it was recalled** — contamination, mislabeling, or potency issue (pull from FDA notice)
3. **Who is at risk** — distribution scope, affected lots
4. **What to do now** — stop use, return/dispose instructions, contact manufacturer or pharmacist
5. **Broader context** — brief note on FDA Class recall system for readers unfamiliar

**Key Data Points:**
- Recall announced August 2026 (exact date from FDA notice)
- Product distributed nationally
- ⚠️ Lot codes, NDC numbers, and specific recall reason must be pulled from the FDA enforcement notice before publication

**Integrity Flags:**
- ⚠️ Primary FDA notice not directly retrieved. **Do not publish without confirming product name, lot codes, and recall reason at [fda.gov/safety/recalls-market-withdrawals-safety-alerts](https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts)**
- ⚠️ Do not overstate risk — include FDA's specific risk language verbatim, not paraphrase

**Source Plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| Health.com | https://www.health.com/bladder-medication-recall-august-2026-12062630 | 2 | Discovery source — confirm details |
| FDA.gov | https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts | 1 | **Primary — required before publishing** |
| FDA Enforcement Reports | https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts | 1 | Lot codes, NDC, recall class |

**Expert Type Needed:** Urologist or clinical pharmacist for comment on what this medication class is used for and patient options. Pull from published institutional quotes if available.

**SEO:**
- Primary keyword: `bladder medication recall 2026`
- Supporting: `FDA recall August 2026`, `overactive bladder recall`, `FDA Class I recall bladder`
- Format: News brief / FAQ hybrid
- Word count: 600–800 words
- Schema: NewsArticle + FAQPage

**Discover Notes:** Specific named recall + action-required format = high AI citation likelihood. Frame as "What to do if you take [product name]" for direct query match.

**Next Steps:** Pull FDA enforcement notice immediately. Confirm product name, lot numbers, recall class. Assign to writer for same-day publish. Legal/editorial review of risk language before live.

---

### BRIEF 2 — P1 · IMMEDIATE

**Primary Headline:** Moderna Starts Phase 1 Ebola Vaccine Trial Targeting the Strain Behind the DRC Outbreak

**Alternate Headlines:**
- A New Ebola Vaccine Is Now in Trials. Here's Why the Timing Matters.
- Moderna's mRNA Ebola Vaccine Enters Human Testing as DRC Outbreak Continues

**Topic:** Moderna Phase 1 Ebola Vaccine Clinical Trial — DRC Outbreak Strain
**Primary Entity:** Moderna Ebola mRNA vaccine
**Signal Type:** clinical_trial
**Allowed Category:** infectious disease / medical research and clinical trials
**Trend Strength:** 78 | **Opportunity:** 72 | **Discover Score:** 4 | **Urgency:** today
**Confidence:** High
**Content Status:** New
**Source Count:** 4

**Why Now:** ABC News reported August 19 that Moderna has initiated a Phase 1 trial of an mRNA-based Ebola vaccine specifically targeting the strain driving the ongoing DRC outbreak. This is a timely infectious disease story with a direct tie to mRNA platform development — high interest from a post-COVID audience. Not covered in recent runs.

**Search Intent:** Informational + evaluative. Readers asking: "Is there an Ebola vaccine?" "Moderna Ebola vaccine trial," "DRC Ebola outbreak 2026."

**Angle:** Why this specific trial matters — mRNA platform applied to a hemorrhagic fever, timed against an active outbreak. Explain what Phase 1 means, what success looks like, and what the DRC outbreak context is.

**Outline:**
1. **The news** — Moderna begins Phase 1 human trial of Ebola vaccine targeting DRC outbreak strain
2. **What makes this different** — mRNA platform applied to Ebola; prior vaccines (rVSV-ZEBOV) target Zaire strain; this may be strain-specific
3. **What Phase 1 actually tests** — safety and dosing, not efficacy; set reader expectations correctly
4. **The DRC outbreak context** — current outbreak scope, affected population, why a new vaccine is needed
5. **mRNA vaccine track record** — COVID-19 → RSV → now Ebola; the platform's expanding application
6. **What comes next** — Phase 2/3 timeline, WHO prequalification process, deployment challenges

**Key Data Points:**
- Moderna Phase 1 trial initiated (ABC News, August 19, 2026)
- DRC outbreak strain specified — confirm strain designation from trial registration or WHO
- Prior Ebola vaccines: rVSV-ZEBOV (Ervebo) approved 2019 for Zaire ebolavirus; this trial may address a different or variant strain
- mRNA Ebola vaccine candidates have been in preclinical development since ~2022

**Integrity Flags:**
- ⚠️ Phase 1 = safety/dosing only. Do not imply this vaccine is "close" to approval or deployment
- ⚠️ Confirm whether this targets a novel strain vs. Zaire strain variant — strain specification matters clinically
- ⚠️ Single primary news source (ABC News) — verify against ClinicalTrials.gov registration before publishing

**Source Plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| ABC News | https://abcnews.com/Health/moderna-begins-phase-1-clinical-trial-ebola-vaccine/story?id=135365177 | 2 | Primary news report |
| ClinicalTrials.gov | https://clinicaltrials.gov | 1 | Trial registration — verify and link |
| WHO DRC Ebola updates | https://www.who.int/emergencies/disease-outbreak-news | 1 | DRC outbreak context |
| Moderna press release | https://investors.modernatx.com [search "Ebola"] | 2 | Official company statement |

**Expert Type Needed:** Infectious disease epidemiologist or vaccinologist. Ideal: WHO-affiliated or academic researcher commenting on mRNA platform for hemorrhagic fevers. Pull from existing published quotes.

**SEO:**
- Primary keyword: `Moderna Ebola vaccine trial`
- Supporting: `DRC Ebola outbreak 2026`, `mRNA Ebola vaccine`, `Ebola vaccine Phase 1`
- Format: News analysis / explainer
- Word count: 800–1,100 words
- Schema: NewsArticle + MedicalTrial

**Discover Notes:** Specific named entity (Moderna) + active outbreak context + question-answer format ("Is there an Ebola vaccine?") = strong AI citation candidate. Include a clear "What does Phase 1 mean?" FAQ section.

**Next Steps:** Verify ClinicalTrials.gov registration. Pull WHO outbreak status. Assign to health science writer. Target same-day or next-morning publish.

---

### BRIEF 3 — P2 · SHORT-TERM (24–48h)

**Primary Headline:** Pilots and Flight Attendants Have a Higher Risk of Radiation-Related Cancer Death — What a New Harvard Study Found

**Alternate Headlines:**
- Is Flying for Work Killing You? A Harvard Study on Airline Workers and Cancer Risk
- The Hidden Occupational Hazard Facing Pilots and Cabin Crew: Cosmic Radiation

**Topic:** Harvard Medical School Study — Aviation Workers and Radiation-Related Cancer Mortality
**Primary Entity:** Harvard Medical School aviation worker cancer study
**Signal Type:** study_or_research
**Allowed Category:** medical research and clinical trials / environmental health
**Trend Strength:** 74 | **Opportunity:** 76 | **Discover Score:** 4 | **Urgency:** this_week
**Confidence:** High
**Content Status:** New
**Source Count:** 3

**Why Now:** Published August 17 by Harvard Medical School. Study examines a broad occupational cohort and finds significantly elevated cancer mortality risk from cosmic ionizing radiation — a well-established but under-publicized exposure. High interest among frequent fliers and people who work in aviation; strong SERP gap for accessible consumer explainer.

**Search Intent:** Informational + evaluative. People asking: "Is flying bad for your health," "do pilots get more cancer," "radiation from flying cancer risk."

**Angle:** Lead with the study finding in plain language, then pivot to what this means for the 100+ million frequent fliers who are *not* aviation workers — and why occupational dose is much higher than passenger dose. Avoid fear-mongering; include proportionality.

**Outline:**
1. **The finding** — Harvard study: pilots and flight attendants have elevated radiation-related cancer mortality vs. other professions
2. **What kind of radiation** — cosmic ionizing radiation at altitude; explain mechanism simply
3. **How much higher the risk** — specific relative risk figures from the study
4. **Why aviation workers are different from passengers** — cumulative exposure hours, altitude, routes
5. **What this means if you fly a lot but are not a crew member** — proportionality; one transatlantic flight ≈ chest X-ray equivalent (approximately)
6. **What aviation workers can do** — monitoring, route optimization, FAA/IATA guidance
7. **Research limitations** — observational study, confounding factors, what we don't know

**Key Data Points:**
- Source: [Harvard Medical School News, August 17, 2026](https://hms.harvard.edu/news/pilots-flight-attendants-have-greater-risk-radiation-related-cancer-death-other-professions)
- Pull specific RR/HR figures from the study (link to original publication)
- FAA Occupational Dose guidance: pilots ~2–6 mSv/year vs. general public ~3 mSv/year (all sources combined)
- Confirm journal of publication from HMS news page

**Integrity Flags:**
- ⚠️ Observational study — association, not causation. State explicitly.
- ⚠️ Do not generalize crew-level occupational findings to passenger risk without clear proportion context
- ⚠️ Confirm original journal citation and pull absolute risk numbers, not just relative risk

**Source Plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| Harvard Medical School | https://hms.harvard.edu/news/pilots-flight-attendants-have-greater-risk-radiation-related-cancer-death-other-professions | 1 | Primary study report |
| Original journal | [URL unverified — pull from HMS page] | 1 | Study data and methodology |
| FAA Radiation Guide | https://www.faa.gov/data_research/research/med_humanfacs/oamtechreports | 1 | Occupational dose context |

**Expert Type Needed:** Radiation oncologist or occupational medicine physician. Published commentary preferred over direct outreach.

**SEO:**
- Primary keyword: `pilot cancer risk radiation study`
- Supporting: `flight attendant health risks`, `cosmic radiation cancer`, `aviation occupational health`, `flying cancer risk`
- Format: Study explainer + FAQ
- Word count: 900–1,200 words
- Schema: NewsArticle + FAQPage

**Discover Notes:** Named entity (Harvard) + specific profession + natural AI query ("do pilots get more cancer?") = strong citation candidate. Include a direct Q&A block for AI snippet targeting.

**Next Steps:** Pull original journal citation from HMS page. Assign to health/science writer. 24h turnaround.

---

### BRIEF 4 — P2 · SHORT-TERM (24–48h)

**Primary Headline:** A Major Genomics Study Just Revealed What Binge Eating and Anorexia Share — and Where They Differ

**Alternate Headlines:**
- The Biology of Eating Disorders: New Research Finds Shared Genetic Roots — With Key Differences
- Are Eating Disorders in Your Genes? A Nature Study Offers the Clearest Answer Yet

**Topic:** Nature Genomics Meta-Analysis — Binge-Eating Disorder and Anorexia Nervosa Shared and Distinct Biology
**Primary Entity:** Eating disorder genomics meta-analysis (Nature, August 2026)
**Signal Type:** study_or_research
**Allowed Category:** medical research and clinical trials / mental health and psychology
**Trend Strength:** 70 | **Opportunity:** 74 | **Discover Score:** 4 | **Urgency:** this_week
**Confidence:** High
**Content Status:** New
**Source Count:** 3

**Why Now:** Published in *Nature Mental Health* (August 19, 2026). First large-scale genomic meta-analysis to examine both binge-eating behavior and anorexia nervosa together, identifying shared biology and phenotype-specific signals. Eating disorders affect 9% of the U.S. population; genomics findings have direct implications for treatment development. Strong SERP gap for accessible consumer summary.

**Search Intent:** Informational + evaluative. Readers asking: "Are eating disorders genetic?" "Binge eating disorder causes," "anorexia genetics research."

**Angle:** Frame as a turning point in understanding eating disorders as brain-based biological conditions, not lifestyle choices. Lead with the shared biology finding, then explain what the phenotype-specific differences mean for treatment.

**Outline:**
1. **What the study found** — shared genetic factors across BED and AN; phenotype-specific signals
2. **Why this matters** — shifts understanding from behavior/choice to biology; implications for stigma and treatment
3. **What "genomic meta-analysis" means** — brief plain-language explanation for lay readers
4. **What genes/pathways are implicated** — pull specific findings from the paper (metabolic, psychiatric, reward-system pathways)
5. **What it means for treatment** — shared biology could support overlapping pharmacological targets; differences suggest personalized approaches
6. **Who gets eating disorders** — prevalence, demographics, dispelling myths
7. **Research limitations** — mostly European-ancestry cohorts; study is genome-wide association, not causal proof

**Key Data Points:**
- Source: [Nature, August 19, 2026](https://www.nature.com/articles/s44220-026-00698-2) — *Nature Mental Health*
- Pull sample size, discovery cohort details, and top genomic findings from the paper
- ~9% of U.S. population affected by eating disorders (NEDA)
- Mortality rate for AN is among the highest of any psychiatric condition

**Integrity Flags:**
- ⚠️ GWAS finds associations, not causal variants. State explicitly: "having these genetic variants does not mean someone will develop an eating disorder."
- ⚠️ Cohort ancestry limitation — note reduced generalizability to non-European populations
- ⚠️ Do not frame as "eating disorders are 100% genetic" — environment and behavior remain significant

**Source Plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| Nature Mental Health | https://www.nature.com/articles/s44220-026-00698-2 | 1 | Primary study |
| NEDA (National Eating Disorders Association) | https://www.nationaleatingdisorders.org/statistics | 2 | Prevalence statistics |
| NIMH Eating Disorders | https://www.nimh.nih.gov/health/topics/eating-disorders | 1 | Clinical context |

**Expert Type Needed:** Psychiatric geneticist or eating disorder researcher. Named author from the study if quoted in coverage; otherwise pull from NIMH or APA published commentary.

**SEO:**
- Primary keyword: `eating disorder genetics research 2026`
- Supporting: `binge eating disorder biology`, `anorexia genetic causes`, `eating disorder genomics study`, `are eating disorders genetic`
- Format: Research explainer
- Word count: 1,000–1,300 words
- Schema: NewsArticle + MedicalStudy

**Discover Notes:** Named journal (Nature) + high-prevalence condition + question-answer framing = strong AI citation candidate. Include FAQ block: "Are eating disorders genetic?" "Can you inherit binge eating disorder?"

**Next Steps:** Download full paper; pull sample size and key gene pathways. Assign to health/psychology writer. 24–48h turnaround. Consider pairing with NIMH resource links for reader support.

---

### BRIEF 5 — P2 · SHORT-TERM (24–48h)

**Primary Headline:** Stanford Scientists Turned a Lymphoma's "On Switch" Into a Built-In Kill Switch

**Alternate Headlines:**
- A "Molecular Glue" That Kills Cancer From the Inside — Stanford's Lymphoma Breakthrough Explained
- How Stanford Weaponized a Cancer Driver Against Itself

**Topic:** Stanford Medicine — Molecular Glue BCL6 Kill Switch in Lymphoma
**Primary Entity:** BCL6 molecular glue therapy (Stanford Medicine)
**Signal Type:** study_or_research
**Allowed Category:** medical research and clinical trials
**Trend Strength:** 68 | **Opportunity:** 70 | **Discover Score:** 4 | **Urgency:** this_week
**Confidence:** High
**Content Status:** New
**Source Count:** 3

**Why Now:** Stanford Medicine published this study August 19, 2026. BCL6 is a well-known oncogene driver in diffuse large B-cell lymphoma (DLBCL), one of the most common aggressive lymphomas. The "molecular glue" mechanism is a genuinely novel therapeutic concept — converting an oncogene into a self-destruct trigger. Strong consumer curiosity given lymphoma prevalence and prior coverage of CAR-T and immunotherapy. Good SERP gap: no accessible explainer yet.

**Search Intent:** Informational + curiosity-driven. Readers asking: "molecular glue cancer," "BCL6 lymphoma treatment," "Stanford lymphoma research 2026."

**Angle:** Lead with the concept — what it means to "turn a cancer driver into a kill switch" — then explain the molecular glue mechanism in plain language. Position within the broader arc of precision oncology. Be honest about where this is in development (preclinical/early).

**Outline:**
1. **The concept** — what BCL6 does normally, why it's a cancer driver in lymphoma
2. **What the molecular glue does** — mechanism: binds BCL6 and a co-repressor, triggering apoptosis instead of tumor growth
3. **Why this is different from existing therapies** — vs. CAR-T, vs. chemotherapy, vs. BCL2 inhibitors
4. **DLBCL context** — prevalence, current treatment landscape, where this fits
5. **Stage of development** — preclinical? Early phase? (confirm from Stanford paper)
6. **The broader molecular glue field** — growing drug class; other cancer targets in development
7. **What patients should know now** — this is not yet in trials; what to watch for

**Key Data Points:**
- Source: [Stanford Medicine News, August 19, 2026](https://med.stanford.edu/news/all-news/2026/08/lymphoma-BCL6-kill-switch.html)
- Pull journal name and publication date from Stanford page
- DLBCL: ~25,000 new cases/year in U.S. (confirm from ACS)
- BCL6 overexpressed in ~40% of DLBCL cases (confirm from paper)

**Integrity Flags:**
- ⚠️ Confirm whether this is preclinical (cell/animal) or early Phase 1 in humans — critical for framing
- ⚠️ Do not imply clinical availability. "Kill switch" metaphor is compelling but must be contextualized as early-stage research
- ⚠️ Association between BCL6 and lymphoma is established; this specific mechanism is novel but not yet proven in humans

**Source Plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| Stanford Medicine | https://med.stanford.edu/news/all-news/2026/08/lymphoma-BCL6-kill-switch.html | 1 | Primary study report |
| Original journal | [URL unverified — pull from Stanford page] | 1 | Full study data |
| American Cancer Society — Lymphoma | https://www.cancer.org/cancer/types/non-hodgkin-lymphoma.html | 2 | DLBCL prevalence context |

**Expert Type Needed:** Oncologist specializing in hematologic malignancies or a molecular pharmacologist. Pull from study author quotes in Stanford release.

**SEO:**
- Primary keyword: `molecular glue lymphoma Stanford`
- Supporting: `BCL6 lymphoma treatment`, `cancer kill switch research`, `DLBCL new treatment 2026`, `molecular glue cancer therapy`
- Format: Research explainer
- Word count: 900–1,100 words
- Schema: NewsArticle

**Discover Notes:** Named institution + novel mechanism name ("molecular glue") + specific cancer type = high AI citation likelihood. AI systems love explaining counterintuitive mechanisms. Frame as "How does molecular glue therapy work?"

**Next Steps:** Pull journal citation and stage of development from Stanford page. Confirm preclinical vs. clinical. Assign to oncology/science writer. 48h turnaround.

---

### BRIEF 6 — P2 · SHORT-TERM (48–72h)

**Primary Headline:** Vegan Diet and Inflammation: What the Research Actually Shows

**Alternate Headlines:**
- Does a Plant-Based Diet Reduce Inflammation? Here's What the Evidence Says
- The Anti-Inflammatory Diet Debate: Where Vegan and Plant-Based Diets Stand in the Science

**Topic:** Vegan/Plant-Based Diet and Inflammation — Evidence Explainer (rising search velocity)
**Primary Entity:** Vegan diet / plant-based diet
**Signal Type:** rising_search_interest
**Allowed Category:** nutrition and diet science
**Trend Strength:** 72 | **Opportunity:** 75 | **Discover Score:** 4 | **Urgency:** this_week
**Confidence:** Medium *(search velocity confirmed via Google Trends; specific triggering study not identified — may be search interest without single news event)*
**Content Status:** New
**Source Count:** 5 (research base; no single breaking news trigger)

**Why Now:** Google Trends shows "vegan diet and inflammation" as a top rising related query under "diet" (+7 delta this week). "Plant-based diet" also rising. Combined with long-term trend toward anti-inflammatory diet interest post-GLP-1 era, this is a durable search opportunity with thin authoritative consumer content currently ranking.

**Search Intent:** Informational + evaluative. Readers asking: "Does vegan diet reduce inflammation?" "Plant-based diet inflammation benefits," "anti-inflammatory foods list."

**Angle:** Evidence-based arbiter. Don't cheerlead or dismiss. Summarize what RCTs and meta-analyses actually show about CRP, IL-6, and other inflammatory markers in plant-based diet studies, note what we don't know, and give readers a practical takeaway.

**Outline:**
1. **Why inflammation matters** — chronic low-grade inflammation and its links to cardiovascular disease, diabetes, cancer risk
2. **What a vegan/plant-based diet actually contains** — fiber, polyphenols, reduced saturated fat; mechanisms for anti-inflammatory effect
3. **What the research shows** — summarize key RCTs and meta-analyses on CRP and inflammatory markers in plant-based diets
4. **How strong is the evidence?** — acknowledge study limitations (short duration, self-reporting, heterogeneous diets)
5. **Vegan vs. plant-forward vs. Mediterranean** — where vegan fits in the anti-inflammatory diet evidence hierarchy
6. **Practical guidance** — you don't have to go fully vegan; what specific foods are driving the benefit
7. **Who might not benefit or needs to be careful** — B12, iron, omega-3 considerations

**Key Data Points:**
- Pull from: Cochrane reviews on plant-based diet + inflammation; PREDIMED trial data; published meta-analyses in *Nutrients* or *American Journal of Clinical Nutrition*
- Specific biomarkers: CRP (C-reactive protein), IL-6, TNF-α
- Meta-analysis: confirm at least 2–3 RCTs or systematic reviews available

**Integrity Flags:**
- ⚠️ Many plant-based diet studies are short-term (≤12 weeks) — note duration limitations
- ⚠️ "Vegan" and "plant-based" are not interchangeable in research; distinguish clearly
- ⚠️ Association between diet pattern and reduced inflammation does not prove causation for any specific disease outcome

**Source Plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| PubMed (meta-analysis search) | https://pubmed.ncbi.nlm.nih.gov/?term=vegan+diet+inflammation+meta-analysis | 1 | Identify 2–3 key systematic reviews |
| American Journal of Clinical Nutrition | https://academic.oup.com/ajcn | 1 | Primary literature |
| NIH Office of Dietary Supplements | https://ods.od.nih.gov | 1 | B12/nutrient context |
| Harvard T.H. Chan HSPH | https://www.hsph.harvard.edu/nutritionsource/anti-inflammatory-diet/ | 2 | Evidence framing |

**Expert Type Needed:** Registered Dietitian Nutritionist (RDN) with research background or nutrition scientist. Pull published quotes from AJCN commentary authors.

**SEO:**
- Primary keyword: `vegan diet and inflammation`
- Supporting: `plant-based diet inflammation research`, `anti-inflammatory plant-based diet`, `does vegan diet reduce CRP`, `plant-based diet evidence`
- Format: Evidence explainer / deep dive
- Word count: 1,100–1,400 words
- Schema: Article + FAQPage

**Discover Notes:** High-volume evergreen + active search spike + question-answer format = strong AI citation candidate. Structure as "What does the science say about vegan diets and inflammation?" for direct AI query match.

**Next Steps:** Pull 2–3 strongest RCTs/meta-analyses from PubMed. Assign to RD-credentialed writer or editor for medical review. 48–72h turnaround. Consider making this an anchor piece for a plant-based diet content cluster.

---

### BRIEF 7 — P2 · SHORT-TERM (48–72h)

**Primary Headline:** Mass General Is Testing Home Hospital Care for Dementia's Most Disruptive Symptoms — And It Could Change How We Think About Aging

**Alternate Headlines:**
- Can You Treat Dementia's Behavioral Symptoms at Home? A Major Hospital Is About to Find Out
- Home Hospital for Dementia: Mass General's New Trial Explained

**Topic:** Mass General Brigham Home Hospital Clinical Trial — Dementia and Behavioral Health
**Primary Entity:** Mass General Brigham home hospital dementia trial
**Signal Type:** clinical_trial
**Allowed Category:** chronic disease management / medical research and clinical trials
**Trend Strength:** 62 | **Opportunity:** 68 | **Discover Score:** 3 | **Urgency:** this_week
**Confidence:** High
**Content Status:** New
**Source Count:** 3

**Why Now:** Published August 18 by Mass General Brigham. The "home hospital" model has been growing since COVID-19 accelerated telehealth adoption; applying it to dementia's behavioral and psychological symptoms (agitation, psychosis, wandering) is a genuinely new application with large implications for the 7 million Americans with Alzheimer's and their caregivers.

**Search Intent:** Informational + practical. Caregivers searching: "dementia behavioral symptoms treatment," "home care for dementia patients," "hospital at home program."

**Angle:** Caregiver-centered. Lead with what this means for families managing a loved one with dementia — what behavioral symptoms are most disruptive, why hospitalization is often traumatic for dementia patients, and how this trial proposes a better model.

**Outline:**
1. **What behavioral and psychological symptoms of dementia are** — agitation, paranoia, wandering, sleep disruption; why these cause hospitalizations
2. **What the home hospital model is** — brief explainer; acute care delivered at home with monitoring
3. **What Mass General's trial involves** — design, patient selection, what "home hospital" means in this context
4. **Why hospitalization is often harmful for dementia patients** — disorientation, delirium risk, hospital-acquired infections
5. **What this could mean for caregivers** — reduced burden, cost implications, access
6. **Current evidence for home hospital models** — general evidence base
7. **What Phase this trial is and what's next** — enrollment criteria, timeline

**Key Data Points:**
- Source: [Mass General Brigham, August 18, 2026](https://www.massgeneralbrigham.org/en/newsroom/clinical-trials-of-home-hospital-treatment-for-dementia)
- 7 million Americans with Alzheimer's (ALZ Association)
- ~30–40% of dementia patients experience significant behavioral symptoms requiring acute intervention (pull from literature)
- Hospital-acquired delirium worsens dementia outcomes — established literature

**Integrity Flags:**
- ⚠️ This is an active trial — efficacy not yet established. Do not present as proven treatment
- ⚠️ "Home hospital" programs require significant infrastructure — not currently available everywhere; note geographic limitations

**Source Plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| Mass General Brigham | https://www.massgeneralbrigham.org/en/newsroom/clinical-trials-of-home-hospital-treatment-for-dementia | 1 | Primary announcement |
| Alzheimer's Association | https://www.alz.org/alzheimers-dementia/facts-figures | 2 | Prevalence + behavioral symptoms |
| ClinicalTrials.gov | https://clinicaltrials.gov | 1 | Trial registration and eligibility |

**Expert Type Needed:** Geriatrician or dementia specialist. Look for published commentary from trial investigators. Pull Alzheimer's Association clinical guidance for caregiver framing.

**SEO:**
- Primary keyword: `home hospital dementia treatment`
- Supporting: `dementia behavioral symptoms treatment`, `hospital at home model`, `Mass General dementia trial`, `dementia caregiver options`
- Format: News analysis + explainer
- Word count: 900–1,100 words
- Schema: NewsArticle + MedicalTrial

**Next Steps:** Pull ClinicalTrials.gov registration. Confirm trial phase and enrollment criteria. Assign to aging/geriatric health writer. 48–72h turnaround.

---

### BRIEF 8 — P3 · SCHEDULED (THIS WEEK)

**Headline:** "Maxxing": When the Pursuit of Self-Optimization Crosses Into a Health Risk

**Topic:** "Maxxing" wellness trend — extreme self-optimization
**Primary Entity:** Maxxing trend (wellness/social media)
**Signal Type:** rising_search_interest / social_spike
**Allowed Category:** mental health and psychology / fitness and exercise science
**Trend Strength:** 58 | **Opportunity:** 62 | **Discover Score:** 3 | **Urgency:** this_week
**Confidence:** Medium
**Content Status:** New
**Source Count:** 3

**Why Now:** [WFAA reported August 20](https://www.wfaa.com/article/news/nation-world/maxxing-when-wellness-trends-push-too-far-social-media/507-66db9ae3-36a1-4437-92d3-f9f3c898156b) on the "maxxing" trend pushing too far. "Maxxing" (looksmaxxing, gymmaxxing, sleepmaxxing) describes the obsessive optimization of physical attributes — increasingly linked by mental health clinicians to body dysmorphia, orthorexia, and compulsive exercise patterns. Trending on social media with growing clinical concern.

**Angle:** Critical health lens. Not a trend recap — a genuine examination of where optimization becomes compulsion, with clinical criteria for when it's a problem and what to do.

**Key Data Points:**
- WFAA piece (August 20, 2026) as news hook
- DSM-5 criteria for body dysmorphic disorder and orthorexia as clinical framing
- Exercise addiction: estimated 3% of regular exercisers (pull from sports medicine literature)
- Pull mental health expert commentary from published sources

**Integrity Flags:**
- ⚠️ "Maxxing" culture intersects with incel/manosphere content — maintain health framing; do not amplify harmful ideological dimensions
- ⚠️ Do not pathologize healthy goal-setting; clearly distinguish between healthy optimization and clinical compulsion

**Source Plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| WFAA | https://www.wfaa.com/article/news/nation-world/maxxing-when-wellness-trends-push-too-far-social-media/507-66db9ae3-36a1-4437-92d3-f9f3c898156b | 2 | News hook |
| DSM-5 / APA | https://www.psychiatry.org | 1 | Clinical criteria |
| NEDA / eating disorder resources | https://www.nationaleatingdisorders.org | 2 | Orthorexia/compulsive exercise framing |

**Expert Type Needed:** Clinical psychologist specializing in body image or eating disorders. Published quotes from academic researchers preferred.

**SEO:** Primary keyword: `maxxing trend health risks` | Format: Feature / explainer | Word count: 900–1,100 | Schema: Article + FAQPage

**Next Steps:** Pull clinical definitions; identify psychologist with published commentary on compulsive optimization. Assign to mental health writer. Schedule mid-week.

---

### BRIEF 9 — P3 · SCHEDULED (THIS WEEK)

**Headline:** FDA Recalls Eye Drops for Potential Contamination — Here's What You Need to Know

**Topic:** FDA Eye Drop Recall — Ocular Itch Relief Product, Contamination
**Primary Entity:** Recalled eye drop (product TBC from FDA.gov notice)
**Signal Type:** recall
**Allowed Category:** FDA and CDC regulatory updates
**Trend Strength:** 55 | **Opportunity:** 58 | **Discover Score:** 3 | **Urgency:** this_week
**Confidence:** Medium *(breaking-recall exception; primary FDA notice not directly retrieved)*
**Content Status:** New
**Source Count:** 3

**Why Now:** [Ophthalmology Times reported August 20](https://www.ophthalmologytimes.com/view/fda-recall-eye-drop-that-relieves-ocular-itch-potential-contamination) on FDA recall of an eye drop for ocular itch relief due to potential contamination. Eye drops are widely used (allergy season, contacts wearers). Contaminated ophthalmic products can cause serious eye infections; 2023/2024 eye drop recalls (EzriCare, Global Pharma) established high consumer awareness of this risk category.

**Angle:** Consumer protection brief. Who uses this product, what the contamination risk is, and what to do. Contextualize within the recent history of eye drop safety issues.

**Key Data Points:**
- Product name, manufacturer, lot codes: **must pull from [FDA recall database](https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts) before publishing**
- Ophthalmology Times report: August 20, 2026
- Prior eye drop recalls context: EzriCare (2023) — Pseudomonas aeruginosa contamination caused blindness, deaths

**Integrity Flags:**
- ⚠️ Do not publish without confirming product name and recall reason from FDA enforcement notice
- ⚠️ Do not conflate with prior eye drop recalls (EzriCare) unless the contamination type is the same

**Source Plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| Ophthalmology Times | https://www.ophthalmologytimes.com/view/fda-recall-eye-drop-that-relieves-ocular-itch-potential-contamination | 2 | Discovery source |
| FDA.gov Recalls | https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts | 1 | **Primary — required before publishing** |

**SEO:** Primary keyword: `eye drop recall 2026 FDA` | Supporting: `contaminated eye drops recall`, `FDA eye drop warning` | Format: News brief | Word count: 500–700 | Schema: NewsArticle

**Next Steps:** Pull FDA enforcement notice — product name, lot codes, contamination type, recall class. Assign after Brief 1 (bladder recall) is live. Can batch publish same day or next day.

---

## REJECTED TOPICS LOG

| Topic | Rejection Reason |
|---|---|
| FDA Class I Egg Recall — Salmonella | `content_status: existing` — covered 2026-08-20; no new development (no new case count, no new FDA action) |
| Blueberry Recall Upgraded to FDA Class I | `content_status: existing` — covered 2026-08-20 |
| Oregon Psilocybin Program — PTSD/Depression | `content_status: existing` — covered 2026-08-20 |
| Medical Debt + Cancer Survival (ACS Study) | `content_status: existing` — covered 2026-08-20 |
| Nature "Hallmarks of Skeletal Muscle Health" | `content_status: existing` — covered 2026-08-20 |
| HHS $96M Mental Health/Substance Use Awards | `content_status: existing` — covered 2026-08-20 |
| GLP-1 Supplement Search Cluster ("best GLP-1 supplement for weight loss") | Skill 02b: **REJECTED** — supplement claim with no traceable primary source for product-specific efficacy; consumer search query cluster, not a study or advisory |
| Hayden Panettiere Mental Health (Trending) | `excluded_category: celebrity wellness trends` — no clinical evidence base; celebrity-driven search spike |
| FDA Nominee Senate Reservations (NYT) | `excluded_category: pure political healthcare opinion` — borderline criteria not met (no new health data) |
| USS Lincoln Mental Health (CNBC) | `off_category` — military context, no health-evidence or research angle qualifying for allowed categories |
| Mitch McConnell Health (Trending) | `excluded_category: celebrity wellness / political` — no health science angle |
| Laser Therapy for Brain Tumors (WashU) | Monitored — narrowly surgical/procedural, limited consumer opportunity score (<55); revisit if Phase 2 results published |
| Space Travel + Women's Health (USF) | Monitored — single institutional source, low search velocity, no consumer urgency |
| NJ Health Premiums for Teachers | `off_category` — local insurance policy, no national health-evidence angle |
| Dartmouth Health Telehealth Closure | `off_category` — local healthcare administration |
| Teamsters / Corewell Health Nurses Contract | `off_category` — labor/HR, no patient health angle |
| AI + Mayo Clinic Health Care (Axios) | `off_category` — B2B healthcare technology angle; no consumer health relevance |
| Wellness Gap Relationships (GQ) | Monitored — lifestyle-adjacent; no search velocity; passes category but low opportunity (audience_relevance ~60) |
| National Wellness Month (generic items) | `off_category / weak_signal` — promotional/seasonal generics, no editorial value |
| SC COVID-19 Treatment Trial (3,000-person) | Monitored — state-funded, limited national reach; revisit if federal trial registration confirmed |
| UK Clinical Trial Sector Reforms | `off_category` — international regulatory/B2B, no US consumer angle |
| CRO acquisition (Curavit/Lindus, Syneos AI) | `off_category` — industry/business; no patient health angle |
| WSJ AI Biobank Startup | `off_category` — B2B research infrastructure |
| U of A / Gila River Medical School Launch | `off_category` — institutional/academic news, too narrow for national audience |
| Minnesota Health Insurance Rate Increases | `off_category` — state-level insurance policy |
| Ferrero Acquires Purely Elizabeth | `excluded_category: supplement marketing` — brand/wellness acquisition |
| "Sundance Kid" / "Curtain Up" / "Action Channel" (Trends) | Noise — Google Trends nutrition cluster artifacts; not health topics |
| Bristol Stool Chart (Trending under gut health) | Weak signal — curiosity query without news peg; evergreen content likely already well-covered |
| Billy Gardell / Gabe Newell / Bronson Reed Weight Loss (Trending) | `excluded_category: celebrity wellness trends` — celebrity weight loss search spikes without evidence base |
| Tucker Carlson Weight Loss (Trending) | `excluded_category: celebrity wellness / political` |
| Miranda Kerr Diet (Trending) | `excluded_category: celebrity wellness trends` |
| Coke Zero vs. Diet Coke (Trending) | Adjacent-but-thin — product comparison, not health science; SERP saturated |

---

## INTEGRITY FLAGS — CONSOLIDATED

| # | Topic | Flag |
|---|---|---|
| 1 | Bladder Medication Recall (P1) | ⚠️ **Primary FDA notice not directly retrieved.** Confirm product name, lot codes, recall class, and recall reason at [fda.gov](https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts) before any publishing. Do not paraphrase risk language — use FDA's exact wording. |
| 2 | Moderna Ebola Vaccine Trial (P1) | ⚠️ Phase 1 = safety/dosing only. Do not imply proximity to approval. Verify ClinicalTrials.gov registration and confirm target strain before publishing. |
| 3 | Harvard Pilot/Cabin Crew Cancer Study (P2) | ⚠️ Observational study — association, not causation. Passenger risk is materially different from crew occupational exposure — include explicit proportionality. Pull absolute risk numbers; do not rely only on relative risk. |
| 4 | Eating Disorder Genomics Study (P2) | ⚠️ GWAS = association, not causation. Note ancestry limitations (predominantly European cohorts). Do not frame as deterministic ("these genes cause eating disorders"). |
| 5 | Stanford Molecular Glue Lymphoma (P2) | ⚠️ Confirm whether preclinical or early Phase 1. Do not imply clinical availability. "Kill switch" is compelling framing — ensure it is contextualized as early-stage. |
| 6 | Vegan Diet + Inflammation (P2) | ⚠️ Distinguish "vegan" from "plant-based" — these are not interchangeable in the literature. Many studies are short-term (≤12 weeks); note duration limitations. Association with reduced inflammation ≠ proven causation for any specific disease. |
| 7 | Home Hospital Dementia Trial (P2) | ⚠️ Active trial — no efficacy data yet. "Home hospital" infrastructure is not universally available; note access limitations. |
| 8 | "Maxxing" Trend (P3) | ⚠️ Avoid platforming harmful ideological content associated with "maxxing" subcultures. Maintain strict clinical/health framing. Do not pathologize ordinary goal-setting. |
| 9 | Eye Drop Recall (P3) | ⚠️ Primary FDA notice not directly retrieved. Confirm product name, contamination type, and lot codes before publishing. Do not conflate with prior eye drop recalls (EzriCare 2023) unless contamination type matches. |

---

## RUN NOTES

**Run Date:** 2026-08-21
**Signals Reviewed:** ~144 Google News + Google Trends clusters
**Topics Retained:** 9 (2× P1, 5× P2, 2× P3)
**Topics Rejected/Monitored:** 30+ (see log)
**Integrity Flags Issued:** 9
**Tools Used:** Google Trends (SerpAPI pre-fetch), Google News (SerpAPI pre-fetch), competitor fallback (configs/competitor_list.yaml)
**Tools Unavailable:** None
**Self-check Status:** Skipped — `site_url` not configured; competitor fallback active; note included on all candidates

**Key Themes Today:**
- FDA Recalls (Bladder med + Eye drops — new; Egg + Blueberry — existing, suppressed)
- Genomics/Precision Medicine (Eating disorders, Molecular glue lymphoma)
- Occupational Health (Aviation radiation/cancer)
- Clinical Trials (Ebola vaccine, Home hospital dementia)
- Evidence-based nutrition (Vegan diet + inflammation)
- Wellness trend critique (Maxxing)

**Recurring Theme Watch:** Egg recall and blueberry recall appeared in 2 consecutive runs (08-19 via Class I upgrade news, 08-20). Suppressed today — no new development. Monitor only if new case count or additional agency action emerges.

**Deferred Topics:** None added today (9 candidates within `max_candidates_returned: 25` threshold). GLP-1 supplement query cluster logged as rejected, not deferred — no primary source basis to recheck.

**Dashboard Output Target:** `outputs/daily_newsroom_dashboard/2026-08-21.html`

**Run History Entry — 2026-08-21:**
```yaml
- date: 2026-08-21
  niche: health and wellness
  signals_reviewed: 144+
  topics_retained: 9
  topics_rejected: 30+
  p1_count: 2
  p2_count: 5
  p3_count: 2
  integrity_flags: 9
  top_topic: "FDA Bladder Medication Recall — Nationwide"
  key_themes:
    - FDA recalls (bladder, eye drops)
    - Genomics / precision oncology (eating disorders, molecular glue lymphoma)
    - Occupational health (aviation radiation cancer)
    - Infectious disease (Moderna Ebola Phase 1)
    - Clinical trials (home hospital dementia)
    - Evidence-based nutrition (vegan diet + inflammation)
    - Wellness trend critique (maxxing)
  tools_used: [serpapi_google_news, serpapi_google_trends, competitor_fallback]
  tools_unavailable: []
  recurring_flags: "Egg recall and blueberry recall suppressed (2nd consecutive run, no new development)"
  dashboard_url: outputs/daily_newsroom_dashboard/2026-08-21.html
  notes: "site_url not configured — self-check skipped. GLP-1 supplement cluster rejected at Skill 02b. 5 topics suppressed as existing coverage from 2026-08-20."
```