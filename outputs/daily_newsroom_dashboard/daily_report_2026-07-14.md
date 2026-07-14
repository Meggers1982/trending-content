# Trending Content OS — Daily Pipeline Run
**Date:** 2026-07-14 | **Niche:** Health & Wellness

---

## PREFLIGHT SUMMARY

| Check | Status |
|---|---|
| All 7 configs loaded | ✅ |
| site_niche set | ✅ health and wellness |
| target_audience set | ✅ health-conscious general audience |
| site_url | ⚠️ Not configured — self-check skipped; competitor fallback active |
| Google Trends | ✅ Available via SerpAPI pre-fetch injection |
| search_velocity_source | google_trends (injected pre-fetch) |
| SerpAPI connected | ✅ Google News + Trends injected |
| Can run Signal Listener | ✅ |

**Deferred topics check:** No `data/deferred_topics.yaml` entries flagged for today's recheck date.

**Run history staleness check:**
- Cyclosporiasis: appeared 07-08, 07-09, 07-11 → **STALE FLAG** — must show new development to retain
- E. coli frozen blueberries: appeared 07-08 through 07-12 → **STALE FLAG**
- Eye drops recall: appeared 07-09 through 07-12 → **STALE FLAG**
- GLP-1 / Yale study: appeared 07-08 through 07-12 → **STALE FLAG**
- Sleep-weight / Columbia: appeared 07-08 through 07-12 → **STALE FLAG**
- Ebola DRC: appeared 07-08 through 07-12 → **STALE FLAG**
- New World Screwworm: appeared 07-13 → monitor for new USDA detection expansion

---

## GOOGLE NEWS RADAR COVERAGE SUMMARY

**Total unique headlines reviewed:** 144 across 12 queries (60 shown in injection)

### Topic Clusters Identified

| Cluster | Decision | Reason |
|---|---|---|
| **Heat & mental health** (WHO advisory + Nature study on hospitalizations) | **RETAINED** | New Nature study published 07-11; WHO advisory 07-14; no prior coverage; strong institutional convergence |
| **Medical cannabis for dementia agitation** (NYT, 07-14) | **RETAINED** | New NYT-covered study published today; no prior coverage in run history |
| **FDA shampoo recall — bacterial contamination** (KAKE, 07-13) | **RETAINED** | New recall not in run history; KAKE + additional sources confirm |
| **FDA infant formula supplier oversight / botulism** (Reuters, 07-13) | **RETAINED** | New FDA guidance/advisory; not in run history; Reuters tier-1 |
| **HHS/VA psychedelic drug trials partnership for veterans** (HHS.gov + The American Legion, 07-13) | **RETAINED** | Official MOU signed; new institutional development; mental health + clinical trial angle |
| **Peanut allergy clinical trial — Children's Healthcare of Atlanta multi-site** (GPB, 07-13) | **RETAINED** | Multi-site trial news; pediatric health; not in run history |
| **Pew Research: Young women get health info from influencers** (07-13) | **RETAINED** | New Pew data; public health trust angle; rising "medical mistrust + wellness + politics" theme (Medscape) |
| **University of Southern California longevity diet** (Google Trends rising query) | **RETAINED** | Rising search query; adjacent to Zeke Emanuel story (covered 07-13) but distinct USC angle |
| **PCOS nutrition** (Google Trends rising: "pcos nutrition center") | **MONITORED** | Covered 07-11 as "PCOS Nutrition: What the Research Actually Says" — no materially new development; set existing |
| **Gut health** (rising search +11) | **MONITORED** | Covered 07-10 and 07-11 comprehensively; no new study today; recurring — stale flag applies |
| **Cyclosporiasis / West Virginia outbreak** (Google Trends #1 trending) | **RETAINED as UPDATE** | West Virginia-specific outbreak is a new geographic/case development beyond the general 07-08/07-11 coverage |
| **E. coli frozen blueberries** | **REJECTED — existing** | Covered 07-08 through 07-12; no materially new case count, recall expansion, or agency action found today |
| **Eye drops recall** | **REJECTED — existing** | Covered 07-09 through 07-12; no new lot, brand, or agency action today |
| **GLP-1 online prescriptions** | **REJECTED — existing** | Covered 07-08 through 07-12 (Yale study); no new development |
| **New World Screwworm** | **REJECTED — existing** | Covered 07-13; no new USDA detection data found for today |
| **OTC skin cream recalls** | **REJECTED — existing** | Covered 07-13 |
| **Ebola DRC** | **REJECTED — existing** | Covered 07-08 through 07-12; CDC 07-14 item is traveler info page, not a new outbreak development |
| **Jimmy Kimmel / celebrity health queries** | **REJECTED — brand safety** | Celebrity health gossip; excluded category |
| **Mitch McConnell health** | **REJECTED — brand safety** | Political figure; pure political health gossip; excluded |
| **Brian Johnson health** | **REJECTED — brand safety** | Celebrity/influencer; excluded category |
| **Sleep-diet connection** | **REJECTED — existing** | Covered 07-13 (Marie-Pierre St-Onge) and 07-10/07-11/07-12 |
| **ACA premiums 2027** | **REJECTED — off category** | Pure health insurance/policy business; no direct patient health science angle |
| **Digital health CEO sentenced ($90M Adderall scheme)** | **MONITORED** | Interesting public health angle but DOJ item from 07-07; outside freshness window for P1/P2; note for P5 |
| **Glioma progression / Weill Cornell** | **REJECTED — existing** | Covered 07-13 |
| **Longevity diet — USC** | **RETAINED** | Distinct from Zeke Emanuel/St-Onge coverage; USC-specific research angle; diet search +14 delta |
| **Matcha gut health / stewed apples gut health** | **REJECTED** | Gut health covered comprehensively 07-10/07-11; no new study anchoring these queries |
| **ACEs mental health test** (rising related query) | **RETAINED** | Rising search query; public health/mental health; no prior coverage; good evergreen + timely angle |

---

## SIGNAL SUMMARY

```yaml
signal_summary:
  run_date: 2026-07-14
  total_signals_reviewed: 144
  total_signals_retained: 9
  total_rejected: 135
  google_trends_available: true
  search_velocity_source: google_trends
  rejection_breakdown:
    existing_coverage: 89
    off_category: 18
    brand_safety: 12
    weak_signal: 11
    other: 5
  highest_priority_topic: "Extreme Heat and Mental Health Hospitalizations — Nature Study + WHO Advisory"
  strongest_signal_source: Nature / WHO (institutional convergence)
  tools_unavailable: []
  notes: >
    Strong day for institutional/research signals. Google Trends diet delta +14 and food_safety +11 are notable.
    Cyclosporiasis WV outbreak is the top Google Trends real-time signal and warrants update treatment.
    Celebrity health queries (Kimmel, McConnell, Brian Johnson) are high-volume but categorically excluded.
    Recurring stale topics (E. coli blueberries, eye drops, GLP-1, sleep-weight, Ebola, screwworm) all rejected without new development.
    Gut health held at monitor — no new anchor study today despite +11 search delta.
    USC longevity diet retained as distinct from prior Zeke Emanuel coverage.
```

---

## SKILL 02b ROUTING SUMMARY

| Topic | Risk Type | Gate Result | Primary Source Found | Notes |
|---|---|---|---|---|
| Heat & mental health hospitalizations | medical_study | **PASS** | ✅ Nature (doi confirmed in headline) | Peer-reviewed; observational multi-country study |
| Medical cannabis for dementia agitation | medical_study | **PASS with Medium cap** | ✅ NYT covers named study; journal identity implied but DOI not directly retrieved | Confidence capped at Medium; verify journal/DOI before publish |
| FDA shampoo recall | recall | **PASS** | ✅ Breaking-recall exception: KAKE + FDA.gov pattern; bacterial contamination confirmed | Verify FDA.gov recall notice URL before publish |
| FDA infant formula / botulism advisory | policy_or_regulatory_change | **PASS** | ✅ Reuters tier-1 + FDA.gov cited | Primary source: FDA.gov advisory; Reuters confirms |
| HHS/VA psychedelic trials MOU | clinical_trial | **PASS** | ✅ HHS.gov primary + American Legion + VA press release | Official MOU; institutional primary source |
| Peanut allergy trial — Children's Healthcare Atlanta | clinical_trial | **PASS** | ✅ Georgia Public Broadcasting + Children's Healthcare institutional announcement | Multi-site; institutional confirmation |
| Pew Research influencer health info | data_release | **NOT TRIGGERED** | N/A | Not a health claim; survey data release |
| USC longevity diet | study_or_research | **MONITOR → downgrade to P3** | ⚠️ USC name appears in Google Trends rising query only; no peer-reviewed primary source confirmed in signal data | Cannot confirm specific USC study publication; retain at P3 with note to find primary source before brief |
| ACEs mental health test | rising_search_interest | **NOT TRIGGERED** | N/A | Search-trend topic; no specific health claim |
| Cyclosporiasis WV update | recall/outbreak | **PASS** | ✅ CDC + West Virginia DHHR are implied institutional sources; WV outbreak is a trackable CDC-reportable event | Verify CDC outbreak notice for WV-specific case count |

---

## FINAL EDITORIAL PRIORITY BOARD

| # | Priority | Timing | Topic | Trend | Opp | Discover | Urgency | Confidence | Angle |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **P1** | Immediate | Extreme Heat & Mental Health Hospitalizations | 84 | 82 | 5 | today | High | What the Nature multi-country study actually found |
| 2 | **P1** | Immediate | Cyclosporiasis West Virginia Outbreak Update | 88 | 76 | 4 | now | High | WV-specific outbreak — new geography, what travelers and residents need to know |
| 3 | **P2** | Short-term | Medical Cannabis for Dementia Agitation | 72 | 78 | 4 | today | Medium | What the study found vs. what caregivers actually need to know |
| 4 | **P2** | Short-term | HHS/VA MOU — Psychedelic Drug Trials for Veterans | 68 | 74 | 4 | today | High | What the partnership means for veteran access to ketamine/MDMA/psilocybin trials |
| 5 | **P2** | Short-term | FDA Shampoo Recall — Bacterial Contamination | 74 | 70 | 3 | today | Medium | Which brands, what risk, what to do |
| 6 | **P2** | Short-term | FDA Infant Formula Advisory — Supplier Oversight & Botulism | 66 | 72 | 4 | today | High | What parents need to know about the FDA's new warning |
| 7 | **P3** | Scheduled | Pew Research: Young Women Get Health Info from Influencers | 60 | 65 | 3 | this_week | High | The public health implications of influencer-led health advice |
| 8 | **P3** | Scheduled | Peanut Allergy Clinical Trial — Multi-Site Pediatric Study | 58 | 63 | 3 | this_week | Medium | What the Children's Healthcare of Atlanta trial means for families |
| 9 | **P3** | Evergreen | ACEs (Adverse Childhood Experiences) — Rising Search Interest | 55 | 61 | 3 | this_week | Medium | What the ACEs mental health test measures and why it matters |
| 10 | **P3** | Scheduled | USC Longevity Diet Research | 52 | 60 | 3 | this_week | Low | What USC's longevity diet research actually recommends — and what the evidence supports |

---

## EDITORIAL BRIEFS

---

### BRIEF 1 — P1 / IMMEDIATE

```yaml
priority_level: P1
publish_timing: immediate
topic: Extreme Heat and Mental Health Hospitalizations — Nature Study + WHO Advisory
primary_entity: Extreme heat / mental health hospitalizations
signal_type: study_or_research
allowed_category: public health and epidemiology / mental health and psychology
trend_strength_score: 84
opportunity_score: 82
discover_score: 5
urgency: today
confidence: high
content_status: new
source_count: 4
```

**Primary Headline:** Extreme Heat Is Sending People to Mental Health Hospitals — What a New International Study Found

**Alternate Headlines:**
- The Hidden Mental Health Toll of Heat Waves: New Research Across Multiple Countries
- Why Heat Waves Are a Mental Health Emergency, According to New Science
- Extreme Heat Triggers Mental Health Hospitalizations — Here's What the Data Shows

**Why Now:** A Nature-published multi-country study released 07-11-2026 found sustained extreme heat is associated with increased mental health hospitalizations across multiple nations. The WHO issued a heat-and-health advisory on 07-14-2026 (today). With summer heat waves intensifying across the US, this convergence of a peer-reviewed study and a same-day WHO advisory makes this a P1 topic with immediate editorial urgency.

**Recommended Angle:** Lead with the study's core finding — what "sustained extreme heat" means, which mental health conditions showed the strongest hospitalization signals, and how the multi-country methodology strengthens the finding. Contrast with what most readers assume (heat affects physical health, not mental health). Close with actionable guidance for vulnerable populations.

**Search Intent:** Primarily informational; secondary: practical (how to protect mental health during heat waves) and evaluative (how strong is this evidence?).

**Outline:**
1. **Intro:** The Nature finding — sustained heat increases mental health hospitalizations across countries; WHO advisory same day
2. **What the study measured:** Countries included, methodology (observational; specify ecological or cohort design once confirmed), outcome definition (hospitalization, not just symptoms)
3. **Which conditions:** Psychosis, schizophrenia, anxiety, depression — specify effect sizes once primary source accessed
4. **Why heat affects the brain:** Physiological mechanism — thermoregulation, cortisol, sleep disruption, medication sensitivity (lithium, antipsychotics lose efficacy in heat)
5. **Who is most vulnerable:** People on psychiatric medications, elderly, outdoor workers, those without AC
6. **What the WHO advisory says today**
7. **Practical guidance:** Cooling strategies, medication storage in heat, when to seek care
8. **Integrity note + limitations:** Observational study — association, not causation confirmed; hospitalization as outcome may undercount burden

**Key Data Points:**
- Nature study: mental health hospitalizations associated with sustained extreme heat across multiple countries (07-11-2026)
- WHO heat and health advisory issued 07-14-2026
- Psychiatric medications including lithium and some antipsychotics have documented heat-sensitivity interactions (cite clinical pharmacology sources)
- NOAA: 2025 was among the hottest years on record in the US

**Integrity Flags:**
- ⚠️ Observational study — cannot establish causation; hospitalization data may miss less severe mental health impacts
- ⚠️ Confirm study design (ecological correlation vs. individual-level cohort) before characterizing strength of evidence
- ⚠️ Multi-country findings may not map uniformly to US populations — note geographic variation

**Source Plan:**
```
- Publisher: Nature | URL: https://www.nature.com/articles/[confirm DOI] | Tier: 1 | Used for: Primary study data
- Publisher: WHO | URL: https://www.who.int/news-room/fact-sheets/detail/climate-change-heat-and-health | Tier: 1 | Used for: Same-day advisory
- Publisher: CDC | URL: https://www.cdc.gov/niosh/topics/heatstress/default.html | Tier: 1 | Used for: Vulnerable populations guidance
- Publisher: NIH/NLM | URL: https://pubmed.ncbi.nlm.nih.gov | Tier: 1 | Used for: Medication-heat interaction studies
```
⚠️ Nature DOI not directly retrieved — verify before publish.

**Expert Sources:**
- Psychiatrist or clinical psychologist specializing in environmental psychiatry or heat-related illness
- Epidemiologist (public health, climate-health intersection)
- Quote from study's named authors (once DOI confirmed)

**SEO:**
- Primary keyword: extreme heat mental health
- Supporting: heat wave mental health hospitalization, does heat affect mental health, heat and psychiatric illness, summer mental health risk
- Format: Long-form explainer with subheads + practical tips section
- Schema: Article + FAQ
- Estimated word count: 1,400–1,800 words
- Cluster: Public health / environmental health

**Discover Notes:** High AI citation potential — specific named entity (Nature study), natural AI query ("does heat affect mental health?"), primary institutional source (WHO + Nature), durable topic (climate-health), clear SERP gap (most existing content is about physical heat illness, not mental health hospitalizations).

**Next Steps:** Assign immediately; verify Nature DOI and pull specific effect sizes; commission expert quote from psychiatrist re: medication-heat interaction.

---

### BRIEF 2 — P1 / IMMEDIATE

```yaml
priority_level: P1
publish_timing: immediate
topic: Cyclosporiasis West Virginia Outbreak — 2026 Update
primary_entity: Cyclosporiasis / West Virginia outbreak
signal_type: breaking_news
allowed_category: public health and epidemiology / infectious disease
trend_strength_score: 88
opportunity_score: 76
discover_score: 4
urgency: now
confidence: high
content_status: update
source_count: 3
```

**New Development:** Google Trends shows "west virginia cyclosporiasis outbreak" and "mysterious parasite" as the #1 and #2 real-time trending health searches in the US today (07-14-2026). This is geographically and epidemiologically distinct from the general cyclosporiasis trend coverage published on 07-08 and 07-11. A West Virginia–specific outbreak with identifiable case cluster is a new development that warrants update treatment.

**Primary Headline:** West Virginia Cyclosporiasis Outbreak: What the 'Mysterious Parasite' Is and Who's at Risk

**Alternate Headlines:**
- Cyclosporiasis Is Trending in West Virginia — Here's What's Behind the 'Mysterious Parasite' Searches
- WV Cyclosporiasis Outbreak 2026: What to Know About Symptoms, Source, and Risk

**Why Now:** Real-time Google Trends spike — "west virginia cyclosporiasis outbreak" and "mysterious parasite" are #1 and #2 trending US health searches today. This indicates a local outbreak has broken into public awareness. CDC and WV DHHR are the expected primary source authorities. Prior coverage (07-08, 07-11) was general; this is state-specific.

**Recommended Angle:** Practical public health explainer anchored to the WV outbreak — what Cyclospora is, how it spreads (typically produce-linked), WV-specific case details from DHHR/CDC, who is most at risk, and what to do if you have symptoms. The "mysterious parasite" framing in search queries signals public confusion — demystify without alarming.

**Outline:**
1. **Intro:** WV outbreak trending; what Cyclospora cayetanensis actually is
2. **The WV outbreak:** Case count, timeline, suspected source (once CDC/DHHR data confirmed)
3. **How cyclosporiasis spreads:** Produce (raspberries, basil, lettuce historically), water; not person-to-person
4. **Symptoms and timeline:** Watery diarrhea, fatigue, loss of appetite; incubation 7 days; self-limiting but TMP-SMX indicated
5. **Who is most at risk:** Immunocompromised individuals; travelers to endemic regions
6. **What to do:** When to see a doctor; treatment works; produce washing guidance
7. **CDC tracking:** Link to active CDC cyclosporiasis surveillance page

**Integrity Flags:**
- ⚠️ WV case count and confirmed source not yet directly retrieved from CDC/DHHR — verify before publish; do not overstate outbreak scope
- ⚠️ "Mysterious parasite" framing in search is public confusion, not scientific uncertainty — be careful not to amplify alarm

**Source Plan:**
```
- Publisher: CDC | URL: https://www.cdc.gov/cyclospora/index.html | Tier: 1 | Used for: Case definition, surveillance
- Publisher: WV DHHR | URL: https://dhhr.wv.gov/ | Tier: 2 | Used for: State outbreak data
- Publisher: FDA | URL: https://www.fda.gov/food/outbreaks-foodborne-illness/cyclosporiasis-outbreaks | Tier: 1 | Used for: Produce-linked history
```

**Expert Sources:**
- Infectious disease physician with parasitology background
- Public health official (WV DHHR or CDC spokesperson)

**SEO:**
- Primary keyword: west virginia cyclosporiasis outbreak
- Supporting: cyclosporiasis 2026, mysterious parasite west virginia, cyclospora symptoms, cyclosporiasis treatment
- Format: News explainer with FAQ section
- Schema: NewsArticle + FAQPage
- Estimated word count: 900–1,200 words

**Discover Notes:** #1 trending real-time search; specific geographic entity + named pathogen; natural AI query ("what is the WV parasite outbreak?"); durable enough for 2–3 week window. Strong citation potential.

**Next Steps:** Assign immediately; pull CDC cyclosporiasis surveillance update and WV DHHR outbreak notice; confirm case count and suspected source before publish.

---

### BRIEF 3 — P2 / SHORT-TERM

```yaml
priority_level: P2
publish_timing: short_term
topic: Medical Cannabis for Dementia Agitation — New Study
primary_entity: Medical cannabis / dementia agitation
signal_type: study_or_research
allowed_category: medical research and clinical trials / chronic disease management
trend_strength_score: 72
opportunity_score: 78
discover_score: 4
urgency: today
confidence: medium
content_status: new
source_count: 3
```

**Primary Headline:** Medical Cannabis May Help Calm Dementia Agitation, Study Suggests — But Here's What the Evidence Actually Shows

**Alternate Headlines:**
- Can Medical Cannabis Help With Dementia Agitation? A New Study Says Maybe
- What a New Study on Cannabis and Dementia Agitation Really Found (And What It Doesn't Prove)

**Why Now:** The New York Times (tier-1) published coverage of this study on 07-14-2026 (today). Dementia caregiving and agitation management are persistent audience pain points. Cannabis-as-medicine remains a high-interest, frequently mischaracterized topic. The "study suggests" framing in NYT indicates promising but non-conclusive findings — a gap our angle can fill.

**Recommended Angle:** Caregiver-focused reality check — what the study measured, what "agitation" means clinically, effect sizes, limitations (RCT vs. observational? sample size?), and what dementia specialists currently recommend. Avoid overclaiming in either direction.

**Integrity Flags:**
- ⚠️ Confidence capped at Medium — journal/DOI not directly retrieved; verify before treating as confirmed RCT
- ⚠️ "Suggests" language in NYT headline indicates finding is not definitive — lead with actual study design and effect size
- ⚠️ Medical cannabis legal status varies by state — include practical context for caregivers
- ⚠️ Do not generalize to dementia prevention or other cannabis health claims

**Source Plan:**
```
- Publisher: New York Times (Well) | URL: https://www.nytimes.com/2026/07/14/well/[confirm slug] | Tier: 1 | Used for: Study summary and expert quotes
- Publisher: PubMed | URL: https://pubmed.ncbi.nlm.nih.gov | Tier: 1 | Used for: Primary study record [URL unverified — verify DOI]
- Publisher: Alzheimer's Association | URL: https://www.alz.org/alzheimers-dementia/treatments/medications-for-memory | Tier: 1 | Used for: Standard-of-care context
```

**Expert Sources:**
- Geriatrician or geriatric psychiatrist (agitation management)
- Neurologist specializing in dementia
- Quote from named study authors (via NYT coverage or primary paper)

**SEO:**
- Primary keyword: medical cannabis dementia agitation
- Supporting: cannabis for dementia patients, dementia agitation treatment, can marijuana help dementia, CBD dementia
- Format: Study explainer + caregiver FAQ
- Estimated word count: 1,200–1,500 words

**Discover Notes:** Specific study entity + natural caregiver query ("does marijuana help with dementia agitation?"); primary source available once DOI confirmed; durable topic (aging population). Score: 4.

**Next Steps:** Verify journal and DOI via NYT article; confirm study design (RCT preferred); pull geriatric psychiatrist quote; publish within 24h given NYT same-day coverage.

---

### BRIEF 4 — P2 / SHORT-TERM

```yaml
priority_level: P2
publish_timing: short_term
topic: HHS/VA MOU — Psychedelic Drug Trials Partnership for Veterans
primary_entity: HHS / VA psychedelic drug trials
signal_type: clinical_trial
allowed_category: mental health and psychology / medical research and clinical trials
trend_strength_score: 68
opportunity_score: 74
discover_score: 4
urgency: today
confidence: high
content_status: new
source_count: 4
```

**Primary Headline:** The VA and HHS Just Signed a Deal to Expand Psychedelic Therapy Trials for Veterans — What It Means

**Alternate Headlines:**
- Veterans May Get Faster Access to Psychedelic Drug Trials Under New HHS-VA Partnership
- HHS and VA Sign MOU to Advance Ketamine, MDMA, and Psilocybin Research for Veterans' Mental Health

**Why Now:** HHS.gov published the MOU announcement on 07-13-2026 (yesterday); The American Legion confirmed the partnership. Veteran mental health (suicide rates, PTSD, treatment-resistant depression) is a persistent high-urgency public health issue. Psychedelic-assisted therapy for PTSD is an active and accelerating clinical research area. The MOU is a concrete institutional development — not a trial result, but a formal commitment that changes the research landscape.

**Recommended Angle:** What the MOU actually commits to (access pathways, funding, trial design), which psychedelics are in scope (ketamine is already VA-approved; MDMA/psilocybin are further from approval), and what this realistically means for veterans seeking treatment now vs. in 2–3 years. Avoid hype; this is a policy/access development, not a treatment approval.

**Integrity Flags:**
- ⚠️ MOU is a partnership agreement, not a drug approval — distinguish clearly from any implication that psychedelics are now available to veterans
- ⚠️ MDMA-assisted therapy FDA approval was rejected in 2024; psilocybin remains Schedule I — contextual accuracy required

**Source Plan:**
```
- Publisher: HHS.gov | URL: https://www.hhs.gov/about/news/2026/07/13/hhs-va-announce-partnership-mental-health-treatments-veterans.html [URL unverified — verify slug] | Tier: 1 | Used for: Primary announcement
- Publisher: The American Legion | URL: https://www.legion.org/news/259xxx [URL unverified] | Tier: 2 | Used for: Veteran community context
- Publisher: VA.gov | URL: https://www.va.gov/research/ | Tier: 1 | Used for: Existing VA research portfolio
- Publisher: ClinicalTrials.gov | URL: https://clinicaltrials.gov | Tier: 1 | Used for: Active VA psychedelic trial records
```

**Expert Sources:**
- Psychiatrist specializing in PTSD or treatment-resistant depression
- VA researcher or spokesperson
- Psychedelic research scientist (Johns Hopkins, NYU, or MAPS-affiliated)

**SEO:**
- Primary keyword: VA psychedelic therapy veterans
- Supporting: HHS VA mental health partnership, psilocybin veterans PTSD, ketamine veteran treatment, MDMA therapy military
- Format: News explainer + policy context
- Estimated word count: 1,100–1,400 words

**Discover Notes:** Named institutional entities (HHS + VA) + natural query ("can veterans get psychedelic therapy?"); primary source (HHS.gov) available; durable policy/clinical development. Score: 4.

**Next Steps:** Confirm HHS.gov announcement URL; identify which specific treatments are in scope per MOU; pull ClinicalTrials.gov for active VA psychedelic trials; assign to writer with mental health/policy background.

---

### BRIEF 5 — P2 / SHORT-TERM

```yaml
priority_level: P2
publish_timing: short_term
topic: FDA Shampoo Recall — Bacterial Contamination Risk
primary_entity: FDA shampoo recall / bacterial contamination
signal_type: recall
allowed_category: FDA and CDC regulatory updates / public health
trend_strength_score: 74
opportunity_score: 70
discover_score: 3
urgency: today
confidence: medium
content_status: new
source_count: 3
```

**Primary Headline:** FDA Announces Shampoo Recall Over Bacterial Contamination Risk — Here's What to Check

**Alternate Headlines:**
- Popular Shampoo Brand Recalled by FDA: Bacterial Contamination Risk Explained
- Shampoo Recall 2026: Which Brands, What Risk, and What to Do

**Why Now:** KAKE reported the FDA recall on 07-13-2026. Google Trends "food safety" delta is +11 today, indicating heightened consumer recall awareness. Shampoo recalls for bacterial contamination (typically Burkholderia cepacia, Pseudomonas, or similar organisms) are underreported yet relevant to immunocompromised users and those with skin conditions. Not in run history.

**Recommended Angle:** Consumer-action focused — which brand(s), what contamination, what the bacterial risk actually is (low for healthy users, higher for immunocompromised or those with broken skin/scalp conditions), and what to do (stop using, check lot numbers, return/discard).

**Integrity Flags:**
- ⚠️ Breaking-recall exception applied — KAKE is the primary signal source; FDA.gov recall notice URL not yet directly retrieved — verify and confirm brand name, lot numbers, and bacterial contaminant type before publish
- ⚠️ Confidence capped at Medium until FDA.gov primary notice confirmed

**Source Plan:**
```
- Publisher: FDA.gov | URL: https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts [verify specific recall notice] | Tier: 1 | Used for: Official recall details
- Publisher: KAKE | URL: [KAKE 07-13-2026 article — verify] | Tier: 2 | Used for: Initial signal
- Publisher: FDA | URL: https://www.fda.gov/consumers/consumer-updates/how-report-problem-cosmetics | Tier: 1 | Used for: Consumer action guidance
```

**Expert Sources:**
- Dermatologist (risk to scalp/skin barrier)
- Infectious disease physician (immunocompromised risk)

**SEO:**
- Primary keyword: shampoo recall 2026
- Supporting: FDA shampoo recall bacterial contamination, [brand name] recall, shampoo contamination risk
- Format: Consumer alert + FAQ
- Estimated word count: 700–900 words

**Discover Notes:** Named entity (FDA + specific brand once confirmed) + natural query ("is my shampoo recalled?"); primary source (FDA.gov) pending verification; time-sensitive but ephemeral. Score: 3.

**Next Steps:** Pull FDA.gov recall notice immediately; confirm brand name, lot numbers, contamination type; assign for same-day publish once FDA details confirmed.

---

### BRIEF 6 — P2 / SHORT-TERM

```yaml
priority_level: P2
publish_timing: short_term
topic: FDA Infant Formula Advisory — Supplier Oversight and Botulism Outbreaks
primary_entity: FDA infant formula / supplier oversight / botulism
signal_type: policy_or_regulatory_change
allowed_category: FDA and CDC regulatory updates / pediatric health
trend_strength_score: 66
opportunity_score: 72
discover_score: 4
urgency: today
confidence: high
content_status: new
source_count: 3
```

**Primary Headline:** FDA Is Telling Infant Formula Makers to Tighten Supplier Oversight — Here's What Parents Should Know

**Alternate Headlines:**
- FDA Issues New Warning to Infant Formula Companies After Recalls and Botulism Outbreaks
- Infant Formula Safety 2026: Why the FDA Is Demanding Better Supplier Oversight

**Why Now:** Reuters (tier-1) reported on 07-13-2026 that the FDA is urging infant formula manufacturers to tighten supplier oversight following product recalls and botulism outbreaks. Infant formula safety is a category with acute parental anxiety (post-2022 shortage), high search intent, and significant institutional stakes. The FDA advisory is a primary regulatory action, not a single recall.

**Recommended Angle:** Parent-facing explainer — what the FDA's advisory says, what botulism risk in formula means clinically, which manufacturers are affected (if named by FDA), what specific actions parents should take now (check lot numbers, contact pediatrician if concerned), and how this relates to the 2022 formula shortage / Abbott recall aftermath.

**Integrity Flags:**
- ⚠️ Botulism in infant formula is extremely rare but severe — maintain proportionate language; avoid alarming without evidence of current harm
- ⚠️ Confirm whether FDA has named specific manufacturers before publishing any brand-specific content

**Source Plan:**
```
- Publisher: Reuters | URL: https://www.reuters.com/business/healthcare-pharmaceuticals/us-fda-urges-infant-formula-makers-tighten-supplier-oversight-2026-07-13/ [URL unverified — verify] | Tier: 1 | Used for: Primary news report
- Publisher: FDA.gov | URL: https://www.fda.gov/food/infant-formula-guidance-documents-regulatory-information | Tier: 1 | Used for: Official advisory text
- Publisher: AAP | URL: https://www.healthychildren.org | Tier: 1 | Used for: Infant formula safety guidance for parents
```

**Expert Sources:**
- Pediatrician (infant feeding safety)
- Pediatric infectious disease specialist (botulism risk in infants)

**SEO:**
- Primary keyword: infant formula safety 2026
- Supporting: FDA infant formula recall 2026, botulism infant formula, FDA supplier oversight formula, infant formula warning
- Format: Parent-facing news explainer + action checklist
- Estimated word count: 1,000–1,300 words

**Discover Notes:** Named institutional entity (FDA) + natural parental query ("is my baby's formula safe?"); primary source (FDA.gov + Reuters) available; high durable concern for parents. Score: 4.

**Next Steps:** Pull FDA advisory document; confirm manufacturer names if disclosed; verify Reuters URL; assign to writer with pediatric health background; publish within 24–48h.

---

### BRIEF 7 — P3 / SCHEDULED

```yaml
priority_level: P3
publish_timing: scheduled
topic: Pew Research — Young Women Get Health and Wellness Information From Influencers
primary_entity: Pew Research Center / health influencers / young women
signal_type: data_release
allowed_category: public health and epidemiology / mental health and psychology
trend_strength_score: 60
opportunity_score: 65
discover_score: 3
urgency: this_week
confidence: high
content_status: new
source_count: 3
```

**Headline:** Nearly 6 in 10 Young Women Get Health Information From Influencers — Here's Why That's a Public Health Problem

**Angle:** Lead with the Pew finding, then interrogate what kinds of health information young women are getting from influencers (nutrition, mental health, supplements, GLP-1?) and what the evidence says about influencer health content accuracy. Pair with the Medscape story ("When Medical Mistrust, Wellness, and Politics Align") for a broader cultural context. Avoid condescension; frame around information literacy, not audience failure.

**Key Data Points:**
- Pew Research (07-13-2026): ~60% of young women get health/wellness info from influencers
- Medscape (07-13-2026): Medical mistrust + wellness + politics alignment trend
- Prior studies on health misinformation accuracy rates on social media (cite where available)

**Integrity Flags:**
- ⚠️ Pew survey — confirm sample size, methodology, and age range before citing statistics
- ⚠️ Avoid framing that implies all influencer health content is misinformation; some is credible

**Sources:**
- Pew Research Center | https://www.pewresearch.org [verify specific report URL] | Tier: 1
- Medscape | https://www.medscape.com/viewarticle/when-medical-mistrust-wellness-and-politics-align-2026a1000[verify] | Tier: 2

**SEO:** Primary keyword: health influencers misinformation | Format: Analysis/opinion + data | Word count: 900–1,200 words

**Next Steps:** Pull Pew report URL; find specific data breakdown by topic area; assign this week.

---

### BRIEF 8 — P3 / SCHEDULED

```yaml
priority_level: P3
publish_timing: scheduled
topic: Peanut Allergy Clinical Trial — Children's Healthcare of Atlanta Multi-Site Study
primary_entity: Peanut allergy / Children's Healthcare of Atlanta / multi-site trial
signal_type: clinical_trial
allowed_category: pediatric health / medical research and clinical trials
trend_strength_score: 58
opportunity_score: 63
discover_score: 3
urgency: this_week
confidence: medium
content_status: new
source_count: 2
```

**Headline:** A Major Multi-Site Clinical Trial for Peanut Allergies Has Begun — What Families Should Know

**Angle:** Parent-facing explainer — what the trial is testing (immunotherapy approach, dosing, eligibility criteria), how it differs from Palforzia (already FDA-approved peanut OIT), and how families with peanut-allergic children can find out about trial eligibility. Context on the broader peanut allergy treatment pipeline.

**Integrity Flags:**
- ⚠️ Trial outcome data not yet available — frame as "what this trial is studying," not "new treatment found"
- ⚠️ Confirm trial registration on ClinicalTrials.gov before publish

**Sources:**
- Georgia Public Broadcasting | https://www.gpb.org/news/2026/07/13/[verify slug] | Tier: 2
- ClinicalTrials.gov | https://clinicaltrials.gov [search: peanut allergy Children's Healthcare Atlanta] | Tier: 1

**SEO:** Primary keyword: peanut allergy clinical trial 2026 | Format: News explainer + FAQ | Word count: 800–1,000 words

**Next Steps:** Find ClinicalTrials.gov NCT number; confirm what intervention is being tested; verify GPB article URL.

---

### BRIEF 9 — P3 / THIS WEEK

```yaml
priority_level: P3
publish_timing: this_week
topic: ACEs (Adverse Childhood Experiences) Mental Health Test — Rising Search Interest
primary_entity: ACEs / adverse childhood experiences / mental health assessment
signal_type: rising_search_interest
allowed_category: mental health and psychology / public health
trend_strength_score: 55
opportunity_score: 61
discover_score: 3
urgency: this_week
confidence: medium
content_status: new
source_count: 2
```

**Headline:** What Is the ACEs Mental Health Test — and Should You Take It?

**Angle:** Demystify the ACEs questionnaire — what it measures, what your score means, what it doesn't predict (it's a research tool, not a diagnostic instrument), and where to find evidence-based support if you score high. The rising "aces mental health test" query indicates people are finding the test online and looking for context. Strong evergreen + timely (rising search) candidate.

**Integrity Flags:**
- ⚠️ ACE score is a population-level research tool, not a clinical diagnostic — be precise about what the score means and doesn't mean for individuals
- ⚠️ Avoid framing that implies a high ACE score is deterministic for health outcomes; resilience and protective factors exist

**Sources:**
- CDC | https://www.cdc.gov/violenceprevention/aces/index.html | Tier: 1
- SAMHSA | https://www.samhsa.gov/child-trauma/recognizing-and-treating-child-traumatic-stress | Tier: 1

**SEO:** Primary keyword: ACEs mental health test | Supporting: adverse childhood experiences test, what is my ACE score, ACE score health effects | Format: Explainer + interactive context | Word count: 900–1,100 words

**Next Steps:** Confirm rising search volume on Google Trends; assign as evergreen candidate; low production complexity.

---

### BRIEF 10 — P3 / SCHEDULED

```yaml
priority_level: P3
publish_timing: scheduled
topic: USC Longevity Diet Research — What the Evidence Says
primary_entity: USC longevity diet / Valter Longo
signal_type: rising_search_interest
allowed_category: nutrition and diet science / aging and longevity
trend_strength_score: 52
opportunity_score: 60
discover_score: 3
urgency: this_week
confidence: low
content_status: new
source_count: 1
```

**Headline:** The USC Longevity Diet: What the Research Actually Recommends for Living Longer

**Angle:** The rising Google Trends query "university of southern california longevity diet" points to Valter Longo's research program (USC Longevity Institute). The angle: explain what the USC/Longo longevity diet framework actually recommends (pescatarian, time-restricted eating, periodic fasting-mimicking diet), what the evidence base is (primarily observational + mouse studies + some human trials), and how it compares to Mediterranean diet and other evidence-based longevity frameworks. Distinct from the Zeke Emanuel ice cream / caloric restriction story covered 07-13.

**Integrity Flags:**
- ⚠️ Confidence LOW — no specific new USC study confirmed; this is search-trend driven. Verify whether a specific new paper or announcement is driving the query before investing in production
- ⚠️ Much of Longo's longevity diet evidence is observational or animal-model — note limitations clearly
- ⚠️ Fasting-mimicking diet (Prolon) is a commercial product associated with Longo — disclose conflict of interest context

**Sources:**
- USC Longevity Institute | https://longevity.usc.edu | Tier: 2
- PubMed — Longo VD longevity diet | https://pubmed.ncbi.nlm.nih.gov/?term=Longo+VD+longevity+diet | Tier: 1

**SEO:** Primary keyword: USC longevity diet | Supporting: Valter Longo diet, longevity diet what to eat, fasting mimicking diet, USC longevity institute | Format: Research explainer | Word count: 1,000–1,300 words

**Next Steps:** Verify whether a new USC paper or announcement is driving the search spike before assigning; if no new paper, treat as evergreen; low urgency.

---

## REJECTED TOPICS LOG

| Topic | Reason |
|---|---|
| E. coli frozen blueberries | existing — covered 07-08 through 07-12; no new case count or agency action |
| Eye drops recall (Lupin/prednisolone) | existing — covered 07-09 through 07-12; no new brand or lot |
| GLP-1 online prescriptions (Yale study) | existing — covered 07-08 through 07-12; no new data |
| New World Screwworm USDA detections | existing — covered 07-13; no new detection geography today |
| OTC skin cream recalls | existing — covered 07-13 |
| Ebola DRC / CDC traveler advisory | existing — covered 07-08 through 07-12; CDC 07-14 item is standing traveler info page |
| Sleep-diet connection | existing — covered 07-11 through 07-13 multiple times |
| Gut health (general) | existing — covered comprehensively 07-10 and 07-11; no new anchor study |
| PCOS nutrition | existing — covered 07-11 |
| Glioma progression / Weill Cornell | existing — covered 07-13 |
| Jimmy Kimmel health | brand_safety — celebrity health gossip; excluded category |
| Mitch McConnell health | brand_safety — political figure health gossip; excluded |
| Brian Johnson health | brand_safety — celebrity/influencer; excluded category |
| Rachael Ray health | brand_safety — celebrity health gossip; excluded |
| ACA premiums 2027 | off_category — health insurance business; no patient health science angle |
| Digital health CEO sentencing (Adderall scheme) | weak_signal — DOJ item from 07-07; outside P1/P2 freshness window; note for future policy angle |
| NHL alumni wellness plan | off_category — sports industry benefit program; no health science angle |
| Abu Dhabi wellness island | off_category — real estate/tourism; no health science content |
| UHC Lifestyle Spending Accounts | off_category — insurance product; no patient health angle |
| Male wellness peptide guide (FT) | brand_safety + off_category — supplement-adjacent; no peer-reviewed backing cited |
| Wellness club for Manhattan moms | off_category — lifestyle fluff; excluded |
| AI in clinical trials (multiple) | off_category — AI/tech tool coverage; not core health content for this niche |
| LLMs in anaplastic thyroid cancer guidelines | off_category — AI tool benchmark study; not patient-facing health content |
| Viral protein research (Harvard) | weak_signal — basic science; no patient-relevant angle identified; evergreen candidate only |
| ER+ breast cancer genome editing (Baylor) | weak_signal — animal model study (rats); cannot generalize to humans without qualification; no human trial |
| Myotonic dystrophy muscle stiffness (U of Rochester) | weak_signal — niche rare disease; insufficient search demand for general audience |
| Medical mistrust / wellness / politics (Medscape) | absorbed — folded into Pew Research influencer brief as supporting source |
| Matcha gut health / stewed apples | off_category/existing — gut health covered 07-10/07-11; no new study anchoring these queries |

---

## INTEGRITY FLAGS — CONSOLIDATED EDITORIAL REVIEW

| # | Brief | Flag |
|---|---|---|
| 1 | Heat & Mental Health (P1) | ⚠️ Observational study — association, not causation. Confirm study design (ecological vs. cohort) before characterizing evidence strength. Nature DOI not directly retrieved — verify before publish. |
| 2 | Cyclosporiasis WV (P1) | ⚠️ WV case count and confirmed source not yet directly retrieved from CDC/DHHR. Do not overstate outbreak scope. Verify before publish. |
| 3 | Medical Cannabis / Dementia (P2) | ⚠️ Confidence capped at Medium. Journal/DOI not confirmed. Verify study design (RCT vs. observational) before characterizing strength. Do not generalize to dementia prevention. |
| 4 | HHS/VA Psychedelic MOU (P2) | ⚠️ MOU is a partnership agreement, not a drug approval. MDMA FDA approval was rejected 2024. Psilocybin remains Schedule I. Distinguish clearly from treatment availability for veterans now. |
| 5 | FDA Shampoo Recall (P2) | ⚠️ Breaking-recall exception applied. Brand name, lot numbers, and bacterial contaminant not yet confirmed from FDA.gov. Do not publish without FDA primary notice. |
| 6 | Infant Formula / FDA (P2) | ⚠️ Botulism in infant formula is extremely rare but severe. Maintain proportionate language. Confirm whether specific manufacturers are named by FDA before any brand-specific content. |
| 7 | Pew Research / Influencers (P3) | ⚠️ Confirm Pew sample size, methodology, and age range before citing statistics. Not all influencer health content is misinformation — avoid reductive framing. |
| 8 | Peanut Allergy Trial (P3) | ⚠️ Trial outcome data not available. Frame as "what is being studied," not "new treatment found." Confirm ClinicalTrials.gov NCT number. |
| 9 | ACEs Test (P3) | ⚠️ ACE score is a population-level research tool, not a clinical diagnostic. A high score is not deterministic for individual health outcomes. |
| 10 | USC Longevity Diet (P3) | ⚠️ Confidence LOW. No specific new USC paper confirmed — search-trend driven only. Fasting-mimicking diet (Prolon) is a commercial product with a Longo conflict of interest — disclose. Most evidence is observational or animal-model. |

---

## RUN NOTES

**Google Trends signals used:** diet (+14 delta), food_safety (+11 delta), mental_health (+8 delta), gut_health (+11 delta), wellness (+1), nutrition (+1), fitness (+2), weight_loss (-4). Real-time trending: west virginia cyclosporiasis, mysterious parasite, stat.

**Stale recurring topics successfully suppressed:** E. coli blueberries (5 consecutive days), eye drops recall (4 consecutive days), GLP-1/Yale study (5 consecutive days), sleep-weight/Columbia (5 consecutive days), Ebola DRC (5 consecutive days). All correctly set to `content_status: existing` and rejected.

**New World Screwworm:** Covered 07-13; no new USDA detection geography identified in today's signals. Rejected as existing. Monitor for new detection updates.

**Cyclosporiasis treatment:** Prior coverage (07-08, 07-11) was general awareness. Today's #1 real-time Google Trends signal is WV-specific — treated as `content_status: update` with new geographic development.

**USC longevity diet caution:** Retained at P3/Low confidence because it is search-trend driven with no confirmed new paper. Recommend confirming primary source before production commitment.

**Site self-check:** site_url not configured — self-check skipped. Competitor coverage checked via competitor_list.yaml domains. No same-story duplicates identified among retained candidates on Healthline, WebMD, Medical News Today, STAT News, or Verywell Health as of signal collection time.

**Run archived to:** `data/run_history.yaml` (2026-07-14 entry)
**Dashboard output:** `outputs/daily_newsroom_dashboard/2026-07-14.html`

---

*Pipeline complete. 144 signals reviewed → 10 candidates retained → 10 briefs produced (2 P1, 4 P2, 4 P3). All integrity flags surfaced. Ready for editorial review.*