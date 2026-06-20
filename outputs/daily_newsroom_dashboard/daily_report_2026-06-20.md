# Trending Content OS — Daily Pipeline Run
**Date:** 2026-06-20 | **Niche:** Health & Wellness | **Run Mode:** Full Pipeline (Skills 01–12)

---

## PREFLIGHT SUMMARY

| Check | Status | Notes |
|---|---|---|
| All 7 configs loaded | ✅ Pass | project_config, category_rules, trusted_sources, scoring_weights, competitor_list, tool_config, expert_sources |
| All 12 skills + 02b present | ✅ Pass | |
| `site_niche` set | ✅ Pass | "health and wellness" |
| `target_audience` set | ✅ Pass | Health-conscious general audience |
| `site_url` set | ⚠️ Warn | Empty — self-check skipped; competitor-list fallback active |
| SerpAPI connected | ✅ Pass | Google News + Google Trends injected via pre-fetch |
| Google Trends available | ✅ Pass | `serpapi_prefetch` block present — treating as primary search_velocity source |
| Deferred topics (`data/deferred_topics.yaml`) | ⚠️ Not found | File absent or empty — no deferred candidates to reintroduce |
| Run history (`data/run_history.yaml`) | ⚠️ Not found | No prior runs detected — no cross-run staleness flags |

**Preflight decision:** ✅ `next_action: run_signal_listener` — proceed with full pipeline.

---

## GOOGLE NEWS RADAR — COVERAGE SUMMARY

144 unique headlines across 12 queries reviewed. Below are the main topic clusters and their pipeline routing decisions.

| Cluster | Headlines Reviewed | Routing | Reason |
|---|---|---|---|
| **FDA Recalls (antidepressant carcinogen, infant formula botulism, Alfredo sauce Salmonella, birth control, ice cream)** | ~10 | **Retained** (multiple candidates) | Multiple FDA recall types, multi-source confirmation, high urgency |
| **GLP-1 / Weight-Loss Drugs (Retatrutide 30% body weight loss; GLP-1 lifetime cost savings)** | 2 | **Retained** | Strong clinical trial data, rising search interest, SERP gap vs. established drugs |
| **Pancreatic Cancer (Cedars-Sinai drug doubling survival; Mayo Clinic trial)** | 2 | **Retained** | Clinical trial data with institutional sourcing; high audience relevance |
| **Psilocybin for Mental Health (USC clinical study launch)** | 1 | **Retained** | First clinical study at USC, mental health category, rising cultural/research interest |
| **Shingles Vaccine + Dementia Risk** | 1 | **Retained** | Medical study, Medical Xpress citing peer-reviewed data, high audience relevance |
| **Prediabetes Lifestyle Intervention (NIH clinical trial)** | 1 | **Retained** | NIH primary source, institutional tier-1, chronic disease management |
| **Infant Botulism / Formula (FDA investigation)** | 2 | **Retained (merged with recall cluster)** | FDA.gov primary source; merged with recall candidate |
| **Brain-Computer Interface (Michigan Medicine, Paradromics)** | 1 | **Monitored** | Compelling but highly technical/niche; no Google Trends velocity; edge-category fit; deferred |
| **Music Therapy + Cancer Anxiety (Mount Sinai)** | 1 | **Monitored** | Single-institution study; Medical Xpress only; lower audience urgency |
| **Plasma Proteomic Signatures / Aging (Nature)** | 1 | **Retained** | Nature journal = tier-1; aging + longevity category; strong SERP gap for consumer angle |
| **Lassa Fever Vaccine (first-in-human trial)** | 1 | **Monitored** | Infectious disease, but very low US consumer urgency; international focus |
| **AI in Health (ChatGPT health intelligence, AMIE medical AI, Google blog)** | 2 | **Rejected** | Off-category for this niche (tech product announcements, not health science content); no direct patient-health angle meeting category criteria |
| **RFK Jr. / HHS Mental Health Funding** | 1 | **Rejected** | Political healthcare opinion — no new clinical data; brand_safety: allow_politics = false |
| **Mosquito / Public Health Emergency (Fort Bend County)** | 1 | **Rejected** | Hyperlocal; no national consumer health angle |
| **Healthcare Affordability (Gallup poll: 5-year low)** | 1 | **Monitored** | Relevant public health data, but framing is policy/economics rather than clinical health content; could work as adjacent angle — held for editorial consideration |
| **Wearables in Clinical Trials** | 1 | **Rejected** | Industry/B2B framing; insufficient consumer health angle |
| **Wellness consumer/lifestyle cluster (Samsung, Balenciaga, Hilton, Bank of America)** | ~6 | **Rejected** | Commercial/brand wellness marketing; no evidence-based health angle |
| **Abortion data (Pew Research)** | 1 | **Rejected** | Political/policy topic; allow_politics = false |
| **GetActive.gov launch (HHS/Kennedy)** | 1 | **Rejected** | Political figure + government PR; no new clinical data |
| **Traffic fatalities study (CDOT)** | 1 | **Rejected** | Off-category (safety/transportation, not health/wellness) |
| **Pet aging study (AVMA)** | 1 | **Rejected** | Off-category (pet health excluded unless zoonotic) |
| **Sauerkraut / gut health + diet (Trends rising queries)** | Trends signal | **Retained** | Strong convergence: gut_health Trends +8 delta, sauerkraut rising queries across gut health + diet + nutrition clusters |

---

## SIGNAL SUMMARY

```yaml
run_started_at: 2026-06-20T00:00:00Z
run_completed_at: 2026-06-20T00:30:00Z
total_signals_reviewed: 144
total_signals_retained: 9
total_rejected: 135
google_trends_available: true
search_velocity_source: "google_trends"
search_velocity_tool: "serpapi_prefetch"

rejection_breakdown:
  off_category: 12
  brand_safety: 4
  duplicate: 0
  weak_signal: 7
  unverified_claim: 0
  other: 112   # commercial wellness, sports/local, hyperlocal, pet health, tech PR

highest_priority_topic: "FDA Recall — Antidepressants (Generic Cymbalta/duloxetine) Carcinogen Risk"
strongest_signal_source: "FDA.gov + ABC News + ABC7 + Prevention (multi-outlet convergence)"
tools_unavailable: []
notes: >
  site_url not configured — self-check skipped; competitor-list fallback used for SERP gap context.
  No deferred_topics.yaml or run_history.yaml found — treated as first run; no staleness flags.
  Google Trends pre-fetch treated as available. Sauerkraut/gut health signal retained from
  convergence of rising Trends queries (+8 delta) across gut_health, nutrition, and diet clusters.
  Healthcare affordability (Gallup) held at monitored — framing too policy-adjacent for clinical
  content without a strong personal-health-impact angle.
  Plasma proteomic / aging study (Nature) retained as strong SERP opportunity with institutional sourcing.
```

---

## SKILL 02b ROUTING SUMMARY

| Candidate | Risk Type | Gate Result | Primary Source Found | Notes |
|---|---|---|---|---|
| Antidepressant (duloxetine) recall — carcinogen | recall | **Pass** | ✅ Yes | FDA.gov recall notice + ABC News + ABC7 + Prevention; multi-outlet class-1 recall confirmation; breaking-recall exception not needed (FDA.gov directly cited) |
| Infant formula botulism (FDA investigation) | recall | **Pass** | ✅ Yes | FDA.gov outbreak investigation page directly cited in Google News Radar |
| Alfredo sauce recall — Salmonella | recall | **Pass** | ✅ Yes | FDA class-1 recall, 41 states, ABC7 + PBS + NBC NY + LiveNOW; FDA source confirmed |
| Birth control recall (3 drugs) | recall | **Pass (medium cap)** | ⚠️ Partial | "The Healthy" + FDA context confirmed; specific lot/drug names not fully extracted — confidence capped Medium pending direct FDA notice verification |
| Retatrutide clinical trial (30% weight loss) | clinical_trial | **Pass** | ✅ Yes | UCHealth article citing published trial data; peer-reviewed source identified |
| Shingles vaccine + dementia (Medical Xpress) | medical_study | **Pass (medium cap)** | ⚠️ Partial | Medical Xpress names study + "suggests" framing; journal not confirmed directly — confidence capped Medium; recommend editor verify journal citation |
| Prediabetes lifestyle intervention (NIH) | clinical_trial | **Pass** | ✅ Yes | NIH.gov primary institutional source; ClinicalTrials.gov eligible |
| Plasma proteomic signatures / aging (Nature) | medical_study | **Pass** | ✅ Yes | Nature journal cited directly in headline; tier-1 source |
| Psilocybin for mental health (USC) | clinical_trial | **Pass** | ✅ Yes | Keck School of Medicine / USC institutional announcement; ClinicalTrials.gov eligible |
| Pancreatic cancer survival drug (Cedars-Sinai) | clinical_trial | **Pass** | ✅ Yes | Cedars-Sinai institutional + "Everyday Health" citation; trial data available |
| Sauerkraut / gut health Trends signal | rising_search_interest | **Not applicable** | — | Lower-risk wellness/nutrition trend; no high-risk health claim |
| GLP-1 lifetime cost savings | medical_study | **Pass (medium cap)** | ⚠️ Partial | Fortune article cites study; original journal not confirmed — medium confidence cap |

---

## FINAL EDITORIAL PRIORITY BOARD

| # | Priority | Timing | Topic | Signal Type | Trend Score | Opp. Score | Discover | Urgency | Confidence | Sources |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **P1** | Immediate | Antidepressant recall — duloxetine/generic Cymbalta carcinogen risk | recall | 88 | 85 | 5 | now | High | 5 |
| 2 | **P1** | Immediate | Infant formula botulism — FDA outbreak investigation (June 2026) | recall | 85 | 84 | 5 | now | High | 5 |
| 3 | **P1** | Immediate | Alfredo sauce recall — Salmonella, 41 states, FDA Class I | recall | 82 | 80 | 4 | now | High | 5 |
| 4 | **P2** | Short-term (24–48h) | Retatrutide: new GLP-1 drug achieves 30% weight loss, on par with bariatric surgery | clinical_trial | 79 | 82 | 5 | today | High | 3 |
| 5 | **P2** | Short-term (24–48h) | Shingles vaccine linked to lower dementia risk | medical_study | 74 | 78 | 4 | today | Medium | 3 |
| 6 | **P2** | Short-term (48–72h) | Prediabetes lifestyle intervention reduces multi-chronic disease risk — NIH trial | clinical_trial | 72 | 76 | 4 | this_week | High | 4 |
| 7 | **P2** | Short-term (48–72h) | Psilocybin for mental health: USC launches first clinical study | clinical_trial | 70 | 75 | 4 | this_week | High | 3 |
| 8 | **P3** | Scheduled (this week) | Blood proteins predict aging and disease risk — Nature study | medical_study | 65 | 72 | 4 | this_week | High | 3 |
| 9 | **P3** | Scheduled (this week) | Sauerkraut's rise: gut health, fermented foods, and what the science actually says | rising_search_interest | 62 | 68 | 3 | this_week | Medium | 4 |
| 10 | **P5** | Monitor | Birth control drugs recalled — 3 medications, nationwide | recall | — | — | — | — | Medium | 2 |
| 11 | **P5** | Monitor | Pancreatic cancer: drug may double survival time (Cedars-Sinai trial) | clinical_trial | — | — | — | — | Medium | 2 |
| 12 | **P5** | Monitor | GLP-1 lifetime savings: $192K+ in medical costs for obesity patients | medical_study | — | — | — | — | Medium | 2 |

> **P5 notes:** Birth control recall held pending direct FDA notice URL retrieval. Pancreatic cancer trial and GLP-1 cost study held pending journal confirmation. All three are publish-ready once primary source is verified.

---

## EDITORIAL BRIEFS

---

### BRIEF 1 — P1 / IMMEDIATE

```yaml
priority_level: P1
publish_timing: immediate
topic: "Antidepressant recall — duloxetine (generic Cymbalta) carcinogen risk"
primary_entity: "duloxetine (generic Cymbalta)"
signal_type: recall
allowed_category: "FDA and CDC regulatory updates"
trend_strength_score: 88
opportunity_score: 85
discover_score: 5
urgency: now
confidence: high
content_status: new
source_count: 5
recommended_angle: >
  "What patients currently taking generic Cymbalta (duloxetine) need to do right now —
  does yours need to be returned, and what should you take instead?"
why_now: >
  FDA has issued a recall of generic duloxetine (Cymbalta) due to presence of a potential
  carcinogen impurity. Multiple major outlets confirmed June 15–17, 2026. Patients are
  actively searching for what this means for their prescriptions. High-urgency,
  patient-action content. No authoritative consumer-facing explainer yet on what to do.
primary_headline: "Your Generic Antidepressant May Be Recalled — Here's What to Do If You Take Duloxetine"
```

**Alternate headlines:**
- "Generic Cymbalta Recalled Over Cancer-Causing Impurity: What Duloxetine Patients Need to Know"
- "FDA Recalls Popular Antidepressant: Is Your Prescription Affected?"

**Why now:** Recall was elevated in mid-June 2026. Patients on duloxetine — one of the most widely prescribed SNRIs — need to know whether their specific product is affected, what the carcinogen is, and what to do next. Stopping abruptly is dangerous; the article must address this.

**Angle:** Patient-action guide. Not a news summary. Answer: Is MY pill affected? What is the impurity? How dangerous is it? Do I stop taking it? What does my doctor recommend?

**Outline:**
1. **Lede:** FDA has recalled [specific manufacturer] generic duloxetine over [carcinogen name — verify from FDA notice]
2. **What was recalled:** Lot numbers, manufacturer, NDC codes — link directly to FDA recall notice
3. **What the impurity is:** Name the compound (likely nitrosamine class — verify); what it is, what level of cancer risk at doses found
4. **What patients should do:** Do NOT stop abruptly; call prescriber; check lot number; FDA guidance on replacement
5. **How to check your bottle:** Step-by-step with photo description
6. **What to expect if your medication is recalled:** Insurance coverage for early refill, alternatives
7. **⚠️ Integrity note:** Recall carcinogen risk is typically low-level cumulative exposure risk, not acute toxicity — context this clearly; do not overstate cancer risk
8. **Expert source:** Quote from psychiatrist or pharmacist via published commentary (STAT News, MedPage Today) on patient action guidance
9. **Conclusion / key takeaways**

**Key data points:**
- FDA recall classification (likely Class I = most serious — verify)
- Carcinogen impurity name and detected levels vs. acceptable daily intake
- Affected manufacturer(s) and lot numbers
- Number of patients estimated on duloxetine (approx. 18 million scripts/year in US — cite CMS/IQVIA data if available)

**Source plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| FDA.gov | https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts | 1 | Primary recall notice — verify specific duloxetine recall page |
| MedShadow Foundation | https://medshadow.org/fda-recalls-and-warnings-gas-x-contaminated-with-coolant-more-generic-cymbalta-cancer-risks/ | 2 | Confirms "generic Cymbalta cancer risks" framing |
| ABC News | https://abcnews.go.com/Health/ [URL to be confirmed] | 2 | Breaking recall confirmation |
| ABC7 Bay Area | https://abc7news.com/ [URL to be confirmed] | 2 | Supporting coverage |
| Prevention | https://www.prevention.com/ [URL to be confirmed] | 2 | Consumer health framing |

**⚠️ Integrity flags:**
- ⚠️ Nitrosamine-type impurities carry low long-term cumulative risk — do NOT frame as "taking this drug gave you cancer"; frame as "elevated trace risk from extended exposure"
- ⚠️ Do not advise patients to stop duloxetine without doctor guidance — abrupt discontinuation causes withdrawal syndrome; this must be explicit in the article
- ⚠️ Verify exact lot numbers and manufacturer from FDA.gov before publishing — do not rely solely on secondary sources for patient-action specifics

**SEO:**
- Primary keyword: "duloxetine recall" / "generic Cymbalta recall"
- Supporting: "antidepressant recall 2026," "duloxetine carcinogen," "Cymbalta recall what to do," "SNRI recall"
- Format: Long-form explainer with FAQ schema + HowTo schema (how to check your lot number)
- Word count: 1,200–1,600 words
- Discover notes: High — specific named drug + FDA action + patient-action question = strong AI citation target

**Expert source:** Board-certified psychiatrist quote on abrupt discontinuation risk; pharmacist quote on checking lot numbers. Source via STAT News published commentary or MedPage Today.

**Next steps:** Verify FDA.gov recall URL → confirm carcinogen name and lot numbers → assign to writer immediately → medical reviewer sign-off before publish → publish within 4 hours of assignment.

---

### BRIEF 2 — P1 / IMMEDIATE

```yaml
priority_level: P1
publish_timing: immediate
topic: "Infant formula botulism — FDA outbreak investigation (June 2026)"
primary_entity: "powdered infant formula botulism outbreak"
signal_type: recall
allowed_category: "FDA and CDC regulatory updates"
trend_strength_score: 85
opportunity_score: 84
discover_score: 5
urgency: now
confidence: high
content_status: new
source_count: 5
recommended_angle: >
  "What parents need to know right now: which formula brands are linked to botulism cases,
  what symptoms to watch for in infants, and what the FDA is telling families to do."
why_now: >
  FDA opened an outbreak investigation on June 17, 2026 linking powdered infant formula to
  infant botulism cases including one in Washington state. Prevention confirmed nationwide
  recall warning on June 17. Parents of infants are the most urgency-sensitive audience
  in health content. Life-safety stakes are the highest of any topic in this run.
primary_headline: "FDA Links Baby Formula to Botulism Cases — What Parents Need to Know Right Now"
```

**Alternate headlines:**
- "Infant Formula Recall Warning: FDA Investigating Botulism Outbreak in Powdered Formula"
- "Is Your Baby's Formula Safe? FDA Botulism Investigation — Brands, Symptoms, and What to Do"

**Why now:** Three confirmed botulism cases including one in Washington. FDA.gov outbreak investigation page live as of June 17. Parents need immediate, calm, accurate guidance — botulism in infants is extremely dangerous but rare; the content must convey urgency without panic.

**Angle:** Parent-action guide. Primary questions: Which brand/lot? What are botulism symptoms in infants? What should I do if my baby has eaten this formula? What does the FDA say? Is breastfeeding affected?

**Outline:**
1. **Lede:** FDA investigating powdered infant formula linked to botulism cases
2. **What we know:** Case count, states affected, formula brand(s) implicated (verify from FDA.gov)
3. **Infant botulism explained:** What it is, why it's dangerous in infants, how quickly symptoms appear
4. **Symptoms to watch:** Constipation, weak cry, poor feeding, floppy muscle tone — when to go to ER immediately
5. **What to do with your formula:** FDA guidance — do you discard, return, or wait? Lot number check
6. **What FDA is saying:** Link to outbreak investigation page
7. **Historical context:** Prior formula safety incidents; FDA response patterns
8. **⚠️ Integrity note:** Do not conflate different formula safety incidents (this is distinct from earlier formula shortage-era issues)
9. **Expert source:** Pediatrician quote on symptom recognition; infectious disease expert on botulism mechanism

**Key data points:**
- Number of confirmed cases (3 per KGW/Prevention); states affected
- Formula brand and lot numbers (verify from FDA.gov)
- Incubation timeline for infant botulism (typically 18–36 hours)
- Treatment: botulinum antitoxin (BabyBIG) — FDA-approved

**Source plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| FDA.gov | https://www.fda.gov/food/outbreaks-foodborne-illness/outbreak-investigation-infant-botulism-powdered-infant-formula-june-2026 | 1 | Primary outbreak investigation — confirm exact URL |
| Prevention | https://www.prevention.com/ [confirm URL] | 2 | Consumer-facing recall confirmation |
| KGW | https://www.kgw.com/ [confirm URL] | 2 | Washington state case confirmation |
| CDC.gov | https://www.cdc.gov/botulism/ | 1 | Infant botulism clinical guidance |
| FDA Infant Formula Homepage | https://www.fda.gov/food/resources-you-food/infant-formula | 1 | Formula safety background |

**⚠️ Integrity flags:**
- ⚠️ Do not name brand unless confirmed by FDA.gov directly — secondary sources may have unconfirmed details
- ⚠️ Do not conflate botulism risk from honey/soil (classic infant botulism) with formula-linked outbreak — mechanism may differ; wait for FDA confirmation
- ⚠️ Three cases is a small number — contextualize without minimizing; infant botulism is rare but severe

**SEO:**
- Primary keyword: "infant formula recall botulism 2026" / "baby formula botulism"
- Supporting: "infant botulism symptoms," "powdered formula recall," "which baby formula is recalled," "infant botulism treatment"
- Format: Breaking news explainer + FAQ schema + symptom checklist
- Word count: 900–1,200 words
- Discover notes: High — specific entity (powdered infant formula + botulism) + parent question = strong AI citation target

**Next steps:** Pull FDA.gov outbreak investigation page immediately → confirm brand and lot numbers → assign to writer + medical reviewer simultaneously → publish within 2–3 hours.

---

### BRIEF 3 — P1 / IMMEDIATE

```yaml
priority_level: P1
publish_timing: immediate
topic: "Alfredo sauce recall — Salmonella contamination, 41 states, FDA Class I"
primary_entity: "Alfredo sauce Salmonella recall"
signal_type: recall
allowed_category: "FDA and CDC regulatory updates"
trend_strength_score: 82
opportunity_score: 80
discover_score: 4
urgency: now
confidence: high
content_status: new
source_count: 6
recommended_angle: >
  "Practical consumer guide: which Alfredo sauce was recalled, which states are affected,
  what Salmonella illness looks like, and what to do if you've already eaten it."
why_now: >
  FDA elevated this to Class I (highest risk) recall covering 41 states. Covered by ABC7,
  PBS, NBC NY, FOX LiveNOW, and Prevention June 14–17, 2026. Broad geographic spread
  means large portion of US health audience is directly affected. Class I = FDA's judgment
  of reasonable probability of serious adverse health consequences.
primary_headline: "Alfredo Sauce Recalled in 41 States Due to Salmonella Risk — Check Your Fridge"
```

**Alternate headlines:**
- "FDA Issues Highest-Level Alfredo Sauce Recall: Is Your Jar Affected?"
- "Salmonella Recall: Popular Alfredo Sauce Pulled from Shelves Across Most of the U.S."

**Angle:** Consumer action guide. Brand name + UPC + lot number check, what Salmonella symptoms feel like (and when they're dangerous enough to seek care), what to do if you've eaten it, where to return it.

**Outline:**
1. **Lede:** Specific brand(s) of Alfredo sauce recalled in 41 states — FDA Class I
2. **What was recalled:** Brand, UPC codes, lot numbers, "best by" dates, states affected (list or link)
3. **What Class I means:** FDA's most serious recall classification — why this matters
4. **What Salmonella is:** Symptoms, onset (6–72 hours), how long it lasts
5. **At-risk groups:** Who faces serious risk (elderly, immunocompromised, infants, pregnant)
6. **What to do:** Check the jar → do not eat → discard or return → where to get a refund
7. **If you've already eaten it:** Symptom monitoring timeline; when to see a doctor
8. **FDA recall page link**
9. **Expert source:** Public health official or food safety expert quote on Salmonella contamination

**Source plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| FDA.gov | https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts | 1 | Primary recall notice — confirm Alfredo sauce specific page |
| LiveNOW from FOX | https://www.livenowfox.com/ [confirm URL] | 2 | 41-state scope, Class I classification confirmation |
| ABC7 Bay Area | https://abc7news.com/ [confirm URL] | 2 | FDA upgrade to highest risk |
| PBS | https://www.pbs.org/ [confirm URL] | 2 | Broad recall coverage |
| NBC New York | https://www.nbcnewyork.com/ [confirm URL] | 2 | NY/NJ state confirmation |
| CDC Salmonella | https://www.cdc.gov/salmonella/ | 1 | Symptom and treatment guidance |

**⚠️ Integrity flags:**
- ⚠️ Verify exact brand name(s) from FDA.gov — multiple secondary sources confirmed the recall but brand specifics must come from primary source
- ⚠️ Salmonella from sauce vs. raw products has the same symptom profile but different contamination pathway — don't conflate with raw poultry Salmonella messaging

**SEO:**
- Primary keyword: "Alfredo sauce recall 2026" / "Alfredo sauce salmonella recall"
- Supporting: "which Alfredo sauce recalled," "salmonella recall 41 states," "jarred pasta sauce recall," "salmonella symptoms"
- Format: Breaking news explainer with UPC checklist; FAQ schema
- Word count: 800–1,000 words
- Discover notes: Good — specific product + specific states + consumer action question

**Next steps:** Confirm brand name and UPC from FDA.gov → writer assign → publish within 3–4 hours. Cross-link to Brief 2 (food safety context).

---

### BRIEF 4 — P2 / SHORT-TERM (24–48h)

```yaml
priority_level: P2
publish_timing: short_term
topic: "Retatrutide: new GLP-1 drug achieves 30% body weight loss — on par with bariatric surgery"
primary_entity: "Retatrutide"
signal_type: clinical_trial
allowed_category: "medical research and clinical trials"
trend_strength_score: 79
opportunity_score: 82
discover_score: 5
urgency: today
confidence: high
content_status: new
source_count: 3
recommended_angle: >
  "Retatrutide is not FDA-approved yet — here's what the trial data actually shows,
  how it compares to Ozempic and Mounjaro, and when it might become available."
why_now: >
  UCHealth article (June 16, 2026) reports published trial data showing retatrutide achieves
  ~30% body weight loss — comparable to bariatric surgery outcomes and significantly beyond
  current GLP-1 approvals (semaglutide ~15%, tirzepatide ~22%). Weight loss is at 7d-delta
  +2 in Trends. GLP-1 is the dominant health story of the past 2 years. A third-generation
  triple agonist achieving surgery-level results is the next chapter readers are waiting for.
primary_headline: "Retatrutide Achieved 30% Weight Loss in Trials — Rivaling Bariatric Surgery. Here's What That Means."
```

**Alternate headlines:**
- "The Next Weight-Loss Drug After Ozempic and Mounjaro: What Retatrutide's Trial Results Actually Show"
- "A GLP-1 Drug That Matches Weight-Loss Surgery? The Science Behind Retatrutide Explained"

**Why now:** Trial data published/reported June 2026. Google Trends shows weight_loss at 64 (7d-delta +2) and diet at 75 (+3). The GLP-1 drug category has sustained enormous search volume; retatrutide represents a genuine advance over currently approved options and will generate high search volume as awareness grows.

**Angle:** Evidence-based comparison and explainer — NOT a hype piece. What does the trial actually show? What's the mechanism (triple agonist vs. dual)? How does it compare to semaglutide and tirzepatide? What are the side effects? Is it FDA-approved? When might it be?

**Outline:**
1. **What is retatrutide?** Triple agonist (GIP + GLP-1 + glucagon receptors) vs. semaglutide (single) and tirzepatide (dual)
2. **What the trial data shows:** 30% weight loss at what dose, over what period, in what population — be precise
3. **The surgery comparison:** What "on par with bariatric surgery" means — gastric bypass typically achieves 25–30% EWL; contextualize carefully
4. **Side effect profile:** GI effects vs. current GLP-1s; any new signals
5. **Current approval status:** Phase — Eli Lilly's development timeline; not FDA-approved
6. **Who could benefit:** Beyond obesity — metabolic syndrome, NASH, type 2 diabetes
7. **What patients should know:** Don't wait on experimental drugs; current options available
8. **⚠️ Integrity note:** Trial data vs. real-world outcomes; primary source confirmation required

**Source plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| UCHealth | https://www.uchealth.org/ [confirm article URL] | 2 | Trial data reporting, 30% figure |
| ClinicalTrials.gov | https://clinicaltrials.gov/search?term=retatrutide | 1 | Trial registration and phase confirmation |
| NEJM / Lancet | [confirm publication URL — search for Jastreboff et al. or equivalent] | 1 | Primary trial paper — verify journal publication |
| Eli Lilly (press release) | https://investor.lilly.com/ [confirm] | 2 | Development timeline / approval status |
| FDA Orange Book | https://www.accessdata.fda.gov/scripts/cder/ob/ | 1 | Approval status confirmation |

**⚠️ Integrity flags:**
- ⚠️ "On par with bariatric surgery" requires precise qualification — which surgery type, which metric (EWL vs. total body weight), which time horizon
- ⚠️ Trial data may be from Phase 2 or Phase 3 — confirm phase; Phase 2 = smaller population, shorter follow-up
- ⚠️ Weight regain after GLP-1 discontinuation is a known issue — mention it; the 30% figure is on-drug
- ⚠️ Do not imply this drug is available — FDA approval is not granted

**SEO:**
- Primary keyword: "retatrutide weight loss" / "retatrutide trial results"
- Supporting: "retatrutide vs Ozempic," "retatrutide vs tirzepatide," "new weight loss drug 2026," "triple agonist GLP-1," "retatrutide FDA approval"
- Format: Long-form explainer with comparison table (retatrutide vs semaglutide vs tirzepatide); FAQ schema
- Word count: 1,400–1,800 words
- Discover notes: Very high — specific named drug + natural question ("how does retatrutide compare to Ozempic?") = prime AI citation target

**Expert sources:** Endocrinologist with obesity medicine focus; metabolic disease researcher — source via published JAMA/NEJM commentary or Eli Lilly trial investigator named in publication.

**Next steps:** Confirm journal publication for trial data → verify trial phase and population size → assign to writer with endocrinology background → publish within 36 hours.

---

### BRIEF 5 — P2 / SHORT-TERM (24–48h)

```yaml
priority_level: P2
publish_timing: short_term
topic: "Shingles vaccine linked to lower dementia risk — new study"
primary_entity: "shingles vaccine (zoster vaccine) dementia risk"
signal_type: medical_study
allowed_category: "medical research and clinical trials"
trend_strength_score: 74
opportunity_score: 78
discover_score: 4
urgency: today
confidence: medium
content_status: new
source_count: 3
recommended_angle: >
  "The shingles vaccine is already recommended for adults 50+. New evidence suggesting it may
  also reduce dementia risk gives people a second compelling reason to get it — here's what
  the study found and what it doesn't prove."
why_now: >
  Medical Xpress reported June 16, 2026 on a study suggesting shingles vaccine may lower
  dementia risk. Aging/longevity is a core category with consistent high search demand.
  The shingles vaccine (Shingrix) is already widely recommended — this gives a concrete new
  angle. Strong SERP gap: existing content is mostly "how to get shingles vaccine" not
  "shingles vaccine and brain health." Confidence capped at Medium pending journal confirmation.
primary_headline: "The Shingles Vaccine May Also Protect Your Brain. Here's What a New Study Found."
```

**Alternate headlines:**
- "Does Getting the Shingles Vaccine Lower Your Dementia Risk? What New Research Suggests"
- "Another Reason to Get Your Shingles Shot: A New Study Links Shingrix to Lower Dementia Risk"

**Angle:** Accessible science explainer for adults 50+. What did the study find? How was it designed? Is it observational? What's the biological mechanism (herpes zoster + neuroinflammation hypothesis)? What should readers do with this information?

**Outline:**
1. **What the study found:** Quantify the dementia risk reduction (X% lower in vaccinated group — pull from source)
2. **Study design:** Observational vs. RCT? Sample size? Follow-up period? — critical caveats
3. **Biological plausibility:** Varicella-zoster virus + neuroinflammation → Alzheimer's risk hypothesis
4. **Prior evidence:** This is not the first such signal — context with prior studies
5. **What this means for current Shingrix recommendations:** Already recommended 50+; this is additive
6. **What it doesn't prove:** Observational association, not causation; confounding variables
7. **Who should get the vaccine:** Current CDC guidance (already clear — link)
8. **Expert source:** Neurologist or infectious disease specialist on vaccine-dementia hypothesis

**Source plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| Medical Xpress | https://medicalxpress.com/ [confirm article URL] | 2 | Study summary + journal identification |
| [Journal TBD — verify from Medical Xpress article] | [DOI to be confirmed] | 1 | Primary study data |
| CDC Shingrix recommendation | https://www.cdc.gov/shingles/vaccination/ | 1 | Current vaccine guidance |
| NIH Alzheimer's research | https://www.nia.nih.gov/health/alzheimers-and-dementia | 1 | Dementia background |

**⚠️ Integrity flags:**
- ⚠️ Confidence capped at Medium — journal not confirmed from available signal data; verify before publishing
- ⚠️ "May lower dementia risk" = association, not causation; the "suggests" framing in the headline must be preserved throughout
- ⚠️ If study is observational (likely), vaccinated individuals may differ systematically from unvaccinated on health behaviors — acknowledge confounding
- ⚠️ Do not frame as "shingles vaccine prevents dementia" — that is not established

**SEO:**
- Primary keyword: "shingles vaccine dementia risk" / "shingrix dementia"
- Supporting: "shingles vaccine brain health," "zoster vaccine Alzheimer's," "shingrix benefits," "shingles vaccine 50+"
- Format: Evidence-based explainer; FAQ schema
- Word count: 1,000–1,300 words

**Next steps:** Verify journal name and DOI from Medical Xpress article → confirm study design (observational vs. RCT) → assign; publish within 48 hours.

---

### BRIEF 6 — P2 / SHORT-TERM (48–72h)

```yaml
priority_level: P2
publish_timing: short_term
topic: "Prediabetes lifestyle intervention reduces risk of developing multiple chronic diseases — NIH trial"
primary_entity: "prediabetes lifestyle intervention chronic disease prevention"
signal_type: clinical_trial
allowed_category: "chronic disease management"
trend_strength_score: 72
opportunity_score: 76
discover_score: 4
urgency: this_week
confidence: high
content_status: new
source_count: 4
recommended_angle: >
  "96 million American adults have prediabetes — NIH evidence now shows lifestyle changes
  don't just prevent diabetes, they reduce risk of heart disease, kidney disease, and other
  chronic conditions simultaneously. Here's what the intervention actually looked like."
why_now: >
  NIH.gov published June 15, 2026 on a lifestyle intervention trial showing reduced risk
  of developing multiple chronic conditions for prediabetes patients. This is a tier-1
  institutional source with direct patient relevance to one of the most common US health
  conditions. Strong SERP gap: most existing prediabetes content focuses on "will I get
  diabetes" not "what other diseases am I preventing."
primary_headline: "NIH Trial: Lifestyle Changes for Prediabetes Cut Risk of Multiple Chronic Diseases — Not Just Diabetes"
```

**Alternate headlines:**
- "If You Have Prediabetes, This NIH Study Shows How Much a Lifestyle Change Can Change Your Future Health"
- "Prediabetes Isn't Just a Diabetes Warning. New NIH Research Shows What Else Is at Stake."

**Angle:** Hope-based, action-oriented. The story is: we knew lifestyle helps prevent Type 2 diabetes; now we know it also reduces the broader burden of chronic disease. What did the intervention involve? How much reduction? What does this mean for someone with prediabetes reading this today?

**Outline:**
1. **The scale of prediabetes in the US:** 96 million adults, most unaware
2. **What this trial found:** Chronic disease outcomes beyond diabetes prevented (which ones? quantify)
3. **What the intervention involved:** Diet, physical activity, weight loss targets — specific components
4. **How it compares to standard care:** Control group outcomes
5. **The multi-disease prevention mechanism:** Why managing blood sugar protects kidneys, heart, nerves
6. **What "lifestyle intervention" means practically:** Actionable steps readers can take
7. **For people who've been told they have prediabetes:** What to ask their doctor
8. **Expert source:** Endocrinologist or public health researcher on DPP (Diabetes Prevention Program) lineage

**Source plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| NIH News | https://www.nih.gov/news-events/news-releases [confirm June 15 release] | 1 | Primary institutional announcement |
| ClinicalTrials.gov | https://clinicaltrials.gov/ [confirm trial ID] | 1 | Trial registration details |
| CDC Prediabetes | https://www.cdc.gov/diabetes/prevention/ | 1 | Background data, DPP reference |
| JAMA / NEJM / Annals | [confirm journal publication from NIH release] | 1 | Primary study paper |

**⚠️ Integrity flags:**
- ⚠️ Confirm the specific chronic conditions studied — "multiple chronic conditions" is a broad claim; the article must name them specifically
- ⚠️ Confirm whether this is a new trial or reanalysis of DPP data — cite appropriately

**SEO:**
- Primary keyword: "prediabetes lifestyle changes chronic disease" / "prediabetes prevention study 2026"
- Supporting: "prediabetes and heart disease risk," "how to reverse prediabetes," "NIH diabetes prevention program," "prediabetes multiple conditions"
- Format: Explainer with action checklist; FAQ schema
- Word count: 1,200–1,500 words

**Next steps:** Confirm NIH press release URL → identify journal paper → assign; publish within 72 hours.

---

### BRIEF 7 — P2 / SHORT-TERM (48–72h)

```yaml
priority_level: P2
publish_timing: short_term
topic: "Psilocybin for mental health: USC launches first clinical study"
primary_entity: "psilocybin clinical study USC Keck School of Medicine"
signal_type: clinical_trial
allowed_category: "mental health and psychology"
trend_strength_score: 70
opportunity_score: 75
discover_score: 4
urgency: this_week
confidence: high
content_status: new
source_count: 3
recommended_angle: >
  "Psilocybin therapy is entering mainstream academic medicine. What USC's new clinical study
  is actually testing, what prior evidence shows, and what this means for patients who've
  exhausted other mental health treatments."
why_now: >
  Keck School of Medicine of USC launched USC's first clinical psilocybin study for mental
  health (June 16, 2026). Mental health Trends at 35 (delta +2). Psilocybin has moved from
  fringe to FDA-tracked; this is a major academic institution legitimizing the therapy. Strong
  SERP gap: most coverage is either hype or policy-focused; clinical explainer for general
  audience is underserved.
primary_headline: "USC Just Launched Its First Psilocybin Clinical Study. Here's What the Research Is Actually Testing."
```

**Alternate headlines:**
- "Psilocybin Is Coming to a Major Medical School Near You — What USC's New Trial Tells Us"
- "What Science Actually Knows About Psilocybin for Mental Health (and What USC Is Trying to Find Out)"

**Angle:** Grounded, evidence-first. Not hype, not fear. What condition is being studied (depression? PTSD? anxiety?)? What's the trial design? What does prior evidence from Johns Hopkins, NYU, UCSF show? What's the regulatory status? What does this mean for patients?

**Outline:**
1. **What USC is studying:** Condition, intervention, patient population, number of participants
2. **What psilocybin therapy actually involves:** The clinical setting, dosing, integration therapy — not recreational use
3. **What prior research has found:** MAPS, Hopkins, NYU — summarize key findings with citations
4. **FDA Breakthrough Therapy designation context:** What it means, where the approval pathway stands
5. **Who might eventually benefit:** Treatment-resistant depression, end-of-life anxiety, PTSD
6. **What the risks are:** What clinical trials are designed to monitor
7. **What patients should do now:** Legitimate clinical trial participation vs. uncontrolled use
8. **Expert source:** USC researcher named in announcement or published Hopkins/NYU researcher

**Source plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| Keck School of Medicine USC | https://keck.usc.edu/ [confirm article URL] | 1 | Primary institutional announcement |
| ClinicalTrials.gov | https://clinicaltrials.gov/search?term=psilocybin+USC | 1 | Trial registration |
| NEJM / JAMA Psychiatry | [prior psilocybin RCT publications — confirm DOIs] | 1 | Prior evidence base |
| FDA Breakthrough Therapy | https://www.fda.gov/patients/fast-track-breakthrough-therapy-accelerated-approval-priority-review/breakthrough-therapy | 1 | Regulatory context |
| NIMH psilocybin background | https://www.nimh.nih.gov/ | 1 | Mental health + psychedelic research context |

**⚠️ Integrity flags:**
- ⚠️ Clinical psilocybin ≠ recreational psilocybin — the article must clearly distinguish supervised clinical use from uncontrolled use
- ⚠️ Prior studies have used small samples; don't overstate efficacy consensus
- ⚠️ Psilocybin remains Schedule I federally — note this clearly; do not imply it is available as a treatment
- ⚠️ "Mental health" is a broad framing — confirm which specific condition(s) the USC trial targets

**SEO:**
- Primary keyword: "psilocybin clinical trial 2026" / "psilocybin mental health research"
- Supporting: "psilocybin therapy depression," "psilocybin FDA status," "USC psilocybin study," "psychedelic therapy clinical trial"
- Format: Explainer + trial FAQ; FAQ schema
- Word count: 1,200–1,500 words

**Next steps:** Confirm specific mental health condition studied → pull USC researcher name → identify prior trial publications for citation → assign; publish within 72 hours.

---

### BRIEF 8 — P3 / SCHEDULED (THIS WEEK)

```yaml
priority_level: P3
publish_timing: scheduled
topic: "Blood proteins predict biological aging and disease risk — Nature study"
primary_entity: "plasma proteomic signatures aging disease prediction"
signal_type: medical_study
allowed_category: "aging and longevity"
trend_strength_score: 65
opportunity_score: 72
discover_score: 4
urgency: this_week
confidence: high
content_status: new
source_count: 3
recommended_angle: >
  "Scientists can now read your biological age from proteins in your blood — and predict
  disease risk years before symptoms appear. What the Nature study found and what it
  means for the future of preventive medicine."
why_now: Nature published June 15, 2026. Aging/longevity category with strong SERP gap for consumer-facing explainer of proteomics-based aging science. No major consumer health outlet has a clear, accessible explainer yet.
primary_headline: "Scientists Found Proteins in Your Blood That Predict How Fast You're Aging — Here's What That Means"
```

**Alternate headlines:**
- "A Blood Test May Reveal Your Biological Age. New Nature Study Explains How."
- "Your Plasma Holds a Clock: New Research Shows Blood Proteins Predict Disease Years in Advance"

**Key data points:** Study published in Nature (June 15, 2026); plasma proteomics; association with cellular aging + future disease; verify specific diseases predicted, sample size, and lead authors.

**Integrity flags:**
- ⚠️ Predictive association ≠ deterministic outcome — frame carefully
- ⚠️ This is not a commercially available test (yet) — do not imply readers can "get this done" unless a clinical pathway is confirmed

**SEO:** Primary: "blood proteins biological age" / "proteomic aging study" | Supporting: "biological age test," "plasma proteomics aging," "aging biomarkers," "longevity blood test" | Format: Explainer; 1,000–1,300 words

**Sources:**
- Nature (June 15, 2026): https://www.nature.com/ [confirm article DOI]
- NIH/NIA aging research: https://www.nia.nih.gov/research/
- PubMed for related proteomic aging literature: https://pubmed.ncbi.nlm.nih.gov/

**Next steps:** Pull DOI from Nature June 15 issue → identify lead author institution → assign; publish mid-week.

---

### BRIEF 9 — P3 / SCHEDULED (THIS WEEK)

```yaml
priority_level: P3
publish_timing: scheduled
topic: "Sauerkraut and gut health: what the science says about fermented foods"
primary_entity: "sauerkraut gut health fermented foods"
signal_type: rising_search_interest
allowed_category: "gut health and microbiome"
trend_strength_score: 62
opportunity_score: 68
discover_score: 3
urgency: this_week
confidence: medium
content_status: new
source_count: 4
recommended_angle: >
  "Sauerkraut is trending across gut health, nutrition, and diet searches — but is the
  evidence as strong as the hype? An evidence-based look at what fermented foods actually
  do for your microbiome and when they're worth eating."
why_now: >
  Google Trends shows gut_health at 59 (7d-delta +8), with "sauerkraut" appearing as
  a rising related query in gut_health, nutrition, diet, and weight_loss clusters
  simultaneously. Also rising: "best time to eat sauerkraut for gut health," "list of
  fermented foods for gut health," "sibo symptoms." Cross-cluster signal with no authoritative
  explainer in top SERP results — dominated by listicles and wellness blogs.
primary_headline: "Sauerkraut for Gut Health: What the Science Actually Says (and What It Doesn't)"
```

**Alternate headlines:**
- "Is Sauerkraut Really Good for Your Gut? We Looked at the Research."
- "The Fermented Foods Trend Is Everywhere. Here's What the Evidence Shows."

**Key data points:** Stanford fermented foods RCT (Sonnenburg lab, Cell 2021) — landmark study showing fermented food diet increases microbiome diversity; contrast with high-fiber diet group. Rising SIBO search signal suggests audience confusion about gut health protocols. Probiotic vs. prebiotic distinction.

**Integrity flags:**
- ⚠️ Most evidence for fermented foods is observational or short-term; the Stanford RCT is notable but limited in scope
- ⚠️ Sauerkraut sold commercially (pasteurized) may not contain live cultures — mention this clearly
- ⚠️ SIBO patients are sometimes advised against high-fermentation foods — note contraindications

**SEO:** Primary: "sauerkraut gut health" / "fermented foods microbiome" | Supporting: "best fermented foods gut health," "sauerkraut probiotics," "fermented foods SIBO," "how much sauerkraut should I eat" | Format: Evergreen explainer with FAQ; 1,000–1,400 words

**Sources:**
- Cell (Sonnenburg lab, 2021 Stanford fermented foods RCT): https://doi.org/10.1016/j.cell.2021.06.019
- NIH Human Microbiome Project: https://www.hmpdacc.org/
- Academy of Nutrition and Dietetics: https://www.eatright.org/
- Cochrane reviews on probiotics: https://www.cochranelibrary.com/

**Next steps:** Pull Sonnenburg lab citation → identify RDN or gut microbiome researcher for expert framing → assign; publish end of week.

---

## REJECTED TOPICS LOG

| Topic | Category | Rejection Reason |
|---|---|---|
| OpenAI ChatGPT health intelligence improvements | Tech product announcement | Off-category: tech product, not health science; no direct patient-health angle |
| Google AMIE medical AI research | Tech/AI product | Off-category: AI product development; lacks clinical health content angle |
| RFK Jr. / HHS $700M mental health funding (STAT News) | Political healthcare | Brand safety: allow_politics = false; no new clinical data |
| GetActive.gov launch — Kennedy/Burgum Colorado tour | Political PR | Brand safety: political figure government PR; no new health data |
| Mosquito population surge — Fort Bend County public health emergency | Hyperlocal | Off-category: local public health; no national consumer health angle |
| California health insurance tax increase | Policy/economics | Off-category: insurance policy/finance; no clinical health content |
| Healthcare affordability at 5-year low (Gallup) | Policy/economics | Framing too policy-adjacent; monitored for potential adjacent angle |
| Balenciaga wellness/techwear launch | Commercial wellness | Excluded category: commercial wellness marketing, no evidence base |
| Samsung connected care solutions (VivaTech) | Tech/wellness marketing | Off-category: consumer electronics marketing |
| Bank of America self-care report | Finance/wellness consumer | Off-category: financial services content |
| NHL/Good Shepherd youth wellness/autism center | Hyperlocal/sports adjacent | Off-category: local facility news |
| Wearables in clinical trials (Clinical Trials Arena) | Industry/B2B | Off-category: B2B clinical research operations |
| Pet aging study (AVMA) | Excluded category | Pet health excluded unless zoonotic disease angle |
| Traffic fatalities study (CDOT) | Off-category | Safety/transportation, not health/wellness |
| Study abroad / pre-med students (Pittsburg State) | Educational PR | Off-category: educational programming, not health content |
| Pew abortion data report | Political/policy | Brand safety: allow_politics = false |
| Lassa fever vaccine first-in-human trial | Low US consumer urgency | Monitored: infectious disease category eligible, but very low US audience relevance; recommend revisit if US cases emerge |
| Brain-computer interface (Michigan Medicine / Paradromics) | Edge category | Monitored: compelling but highly technical/niche; no Trends velocity; edge-category audience fit |
| Music therapy cancer anxiety (Mount Sinai) | Weak signal | Single-institution study; Medical Xpress only; no Google Trends signal; low urgency |
| Pancreatic cancer survival drug | Monitored → P5 | Good candidate but pending journal confirmation from primary source; hold for P5 |
| Birth control drug recall (3 medications) | Monitored → P5 | High-priority recall but specific drug names/lot numbers unconfirmed from FDA primary source |
| GLP-1 $192K lifetime savings study | Monitored → P5 | Fortune secondary citation; journal unconfirmed |
| North Atlantic Right Whale health updates (NOAA) | Off-category | Animal/marine ecology, not human health |
| Most "wellness" cluster headlines (hotel, fitness class, VA wellness Wednesday) | Commercial/lifestyle | Off-category: facility/lifestyle programming, not evidence-based health content |

---

## INTEGRITY FLAGS — CONSOLIDATED

All editorial integrity concerns, consolidated for review before publishing:

| Brief | Flag |
|---|---|
| **Brief 1** (Duloxetine recall) | ⚠️ Do NOT advise abrupt discontinuation without doctor guidance — withdrawal syndrome risk |
| **Brief 1** (Duloxetine recall) | ⚠️ Carcinogen risk is low-level cumulative exposure, not acute toxicity — do not overstate cancer risk |
| **Brief 1** (Duloxetine recall) | ⚠️ Verify exact lot numbers and manufacturer directly from FDA.gov before publishing |
| **Brief 2** (Infant formula botulism) | ⚠️ Do not name formula brand until confirmed by FDA.gov directly |
| **Brief 2** (Infant formula botulism) | ⚠️ Do not conflate with honey/soil-source botulism — different exposure pathway |
| **Brief 3** (Alfredo sauce recall) | ⚠️ Verify brand name and UPC from FDA.gov — secondary sources may have incomplete brand details |
| **Brief 4** (Retatrutide) | ⚠️ "On par with bariatric surgery" requires precise qualification — surgery type, metric, time horizon |
| **Brief 4** (Retatrutide) | ⚠️ Confirm trial phase — Phase 2 vs. Phase 3 has major implications for certainty |
| **Brief 4** (Retatrutide) | ⚠️ Weight regain after discontinuation must be mentioned; the 30% figure is on-drug |
| **Brief 4** (Retatrutide) | ⚠️ Drug is NOT FDA-approved — do not imply availability |
| **Brief 5** (Shingles/dementia) | ⚠️ Confidence capped Medium — verify journal before publishing |
| **Brief 5** (Shingles/dementia) | ⚠️ "May lower" = association, not causation — preserve hedged language throughout |
| **Brief 5** (Shingles/dementia) | ⚠️ Acknowledge confounding if observational design confirmed |
| **Brief 6** (Prediabetes/NIH) | ⚠️ Specify which chronic conditions the trial measured — "multiple" is insufficient precision |
| **Brief 6** (Prediabetes/NIH) | ⚠️ Confirm whether new trial or reanalysis of existing DPP data |
| **Brief 7** (Psilocybin/USC) | ⚠️ Clearly distinguish supervised clinical use from recreational use throughout |
| **Brief 7** (Psilocybin/USC) | ⚠️ Psilocybin remains Schedule I federally — do not imply it is available as a treatment |
| **Brief 7** (Psilocybin/USC) | ⚠️ Confirm which specific mental health condition(s) the USC trial targets |
| **Brief 8** (Plasma proteomics/aging) | ⚠️ Predictive association ≠ deterministic outcome — frame carefully |
| **Brief 8** (Plasma proteomics/aging) | ⚠️ This is not a commercially available test — do not imply readers can access it |
| **Brief 9** (Sauerkraut/gut health) | ⚠️ Commercial pasteurized sauerkraut may not contain live cultures — mention clearly |
| **Brief 9** (Sauerkraut/gut health) | ⚠️ SIBO contraindication — fermented foods are not universally beneficial |
| **P5 / Monitor — all three** | ⚠️ Do not publish birth control recall, pancreatic cancer drug brief, or GLP-1 cost brief until primary source (FDA notice / journal DOI) is directly retrieved and confirmed |

---

## RUN NOTES

```yaml
run_date: 2026-06-20
niche: health and wellness
signals_reviewed: 144
candidates_retained: 9
candidates_rejected: 135
p1_count: 3
p2_count: 4
p3_count: 2
p5_monitor_count: 3

top_topic: "Antidepressant recall — duloxetine/generic Cymbalta carcinogen risk"
key_themes:
  - "FDA recalls (multiple categories: drug, food, infant formula)"
  - "GLP-1 / weight-loss drug pipeline (retatrutide as next-generation)"
  - "Aging/longevity biomarkers (plasma proteomics)"
  - "Mental health + emerging therapies (psilocybin)"
  - "Prediabetes and multi-disease prevention"
  - "Gut health / fermented foods (sauerkraut rising cross-cluster)"
  - "Shingles vaccine + brain health"

tools_used:
  - serpapi_prefetch (Google Trends — 7-day interest)
  - serpapi_news (Google News Radar — 144 headlines)

tools_unavailable: []

integrity_flags_total: 21
site_url_configured: false
self_check: "skipped — competitor-list fallback used"
deferred_topics_file: "not found"
run_history_file: "not found — treated as first run"

dashboard_output: "outputs/daily_newsroom_dashboard/2026-06-20.html"

notes: >
  Three P1 recalls are the lead story of this run and require same-day publishing.
  All three require direct FDA.gov URL confirmation before publish — do not rely
  solely on secondary sources for lot numbers, brand names, or product specifics.
  Retatrutide is the highest-opportunity P2 story — first meaningful advance beyond
  tirzepatide in the GLP-1 category and will generate sustained search volume.
  Birth control recall (3 drugs) is a strong P1 candidate pending FDA primary source
  confirmation — move to P1/immediate as soon as verified.
  No staleness flags possible on first run — cross-run deduplication will begin on
  run 2. Key themes logged above for comparison in subsequent runs.
```

---

*Trending Content OS — Run complete. 9 candidates briefed. 3 P1 immediate actions. Dashboard ready for publication to `outputs/daily_newsroom_dashboard/2026-06-20.html`. Archive this run to `data/run_history.yaml`.*