# Trending Content OS — Daily Pipeline Run
**Date:** 2026-06-21 | **Niche:** Health & Wellness | **Run Mode:** Full Pipeline (Skills 01–12)

---

## PREFLIGHT SUMMARY

| Check | Status |
|---|---|
| All 7 config files | ✅ Loaded |
| All 12 skills + Skill 02b | ✅ Present |
| `site_niche` | ✅ health and wellness |
| `target_audience` | ✅ Configured |
| `site_url` | ⚠️ Not configured — self-check skipped; competitor-check fallback active |
| SerpAPI | ✅ Connected (pre-fetch injected) |
| Google Trends | ✅ Available via SerpAPI pre-fetch block |
| `search_velocity_source` | `google_trends` (serpapi_prefetch) |
| Google News Radar | ✅ Injected — 144 signals, 60 shown |
| Deferred topics (`data/deferred_topics.yaml`) | ⚠️ File not found — skipping deferred queue |
| Run history (`data/run_history.yaml`) | ⚠️ File not found — no cross-run staleness check; treating all topics as first-appearance |
| `can_run_signal_listener` | ✅ Yes |

**Preflight decision:** Proceed with full pipeline. Duplicate self-check skipped (no `site_url`); competitor domains used for SERP gap context.

---

## GOOGLE NEWS RADAR — COVERAGE SUMMARY

144 unique signals across 12 queries. After clustering by topic and source pattern, the Google News Radar resolved into **9 major topic clusters**:

| Cluster | Key Headlines / Sources | Pipeline Decision |
|---|---|---|
| **FDA Recalls — Food (Alfredo sauce, mac & cheese, ice cream)** | ABC News, PBS, NBC NY, LiveNOW FOX, NewsNation — Class I recall, salmonella, 41+ states | ✅ **Retained** — breaking recall, high urgency |
| **FDA Recalls — Infant Formula (botulism)** | KGW, Prevention, FDA.gov — 3 botulism cases linked to recalled formula | ✅ **Retained** — safety-critical, institutional source |
| **FDA Recalls — Antidepressant (carcinogen)** | Health.com, WCNC — ~375K bottles, carcinogen risk | ✅ **Retained** — drug recall, Skill 02b gate required |
| **FDA High-Risk OTC Drug Alert** | The Healthy — FDA sets highest risk level for common OTC drug | ✅ **Retained** — pending Skill 02b verification |
| **USC / Fish Oil & Alzheimer's Study** | Keck Medicine of USC — fish oil supplements may not prevent Alzheimer's decline | ✅ **Retained** — trending NOW on Google Trends ("hussein yassine usc study"); Skill 02b gate |
| **Shingles Vaccine & Dementia Risk** | Medical Xpress — study suggests lowered dementia risk | ✅ **Retained** — Skill 02b gate |
| **NIH Prediabetes Lifestyle Intervention** | NIH.gov — lifestyle intervention lowered risk of multiple chronic conditions | ✅ **Retained** — institutional primary source, strong opportunity |
| **Pancreatic Cancer Treatment (Retatrutide / Trial)** | Cedars-Sinai, Mayo Clinic, UCHealth — groundbreaking drug, doubled survival, 30% weight loss | ✅ **Retained** — two separate strong signals merged (pancreatic cancer trial + retatrutide weight loss) |
| **Psilocybin Mental Health (USC clinical study)** | Keck School of Medicine of USC — first USC clinical study of psilocybin for mental health | ✅ **Retained** — Skill 02b gate |
| **RFK Jr. Mental Health Funding** | STAT News — $700M in grants, but experts say grants aren't new | ⚠️ **Monitored** — political adjacency; no new health data; brand safety borderline |
| **AI in Health / Therapy / Clinical Trials** | APA, Google/AMIE, Clinical Trial Vanguard, OpenAI — AI in therapy, clinical AI deployment speed, ChatGPT health intelligence | ⚠️ **Monitored** — adjacent (not core health science); low audience_relevance for health-conscious reader; not a category match |
| **Wellness commercial / lifestyle noise** | Balenciaga wellness, Hilton spa renovation, Samsung VivaTech, Costco wellness, cruise ship wellness | ❌ **Rejected** — brand/lifestyle marketing, not health science; excluded category |
| **California health insurance tax** | CalMatters — state policy | ❌ **Rejected** — pure political/policy without new health data |
| **Gallup: US adults' ability to afford healthcare at 5-year low** | Gallup — survey data | ⚠️ **Monitored** — policy-adjacent; limited health content angle for this site |

---

## SIGNAL SUMMARY

```yaml
run_started_at: 2026-06-21T00:00:00Z
run_completed_at: 2026-06-21T00:45:00Z
total_signals_reviewed: 144
total_signals_retained: 9
total_rejected: 135
google_trends_available: true
search_velocity_source: google_trends (serpapi_prefetch)
rejection_breakdown:
  off_category: 38        # wellness commercial, sports, local news, pet health, policy-only
  brand_safety: 12        # wellness marketing, celebrity wellness
  duplicate: 0            # no self-check available; competitor baseline only
  weak_signal: 61         # single-source, aggregator-only, vague commercial
  unverified_claim: 0     # routed to Skill 02b (not rejected here)
  other: 24               # AI-in-healthcare (monitored, not core), policy adjacency
highest_priority_topic: "Alfredo Sauce Salmonella Recall — FDA Class I"
strongest_signal_source: FDA.gov + ABC News + 6 corroborating outlets
tools_unavailable: [reddit_api (not called), social_search (not called)]
notes: >
  Google Trends real-time shows "hussein yassine usc study" as a breakout signal —
  mapped to USC/Keck Medicine fish oil + Alzheimer's study. This is the single 
  strongest search spike of the run. Retatrutide weight-loss trial (UCHealth) and 
  infant formula botulism (KGW/FDA) are the next most time-sensitive. 
  RFK Jr. mental health funding monitored — no new health data behind the headline.
  AI-in-health cluster monitored — not a core category match for this site.
  site_url not configured — self-check skipped; competitor coverage used for SERP gap.
```

---

## SKILL 02B ROUTING SUMMARY

| Candidate | Risk Type | Gate Result | Primary Source Found | Notes |
|---|---|---|---|---|
| USC Fish Oil / Alzheimer's Study | medical_study | ✅ **Pass** | Yes — Keck Medicine of USC press release + Hussein Yassine MD named researcher; Google Trends breakout confirms | Confidence cap: Medium (press release; peer-reviewed journal citation not yet confirmed in pre-fetch data) |
| Shingles Vaccine / Dementia Risk | medical_study | ✅ **Pass** | Yes — Medical Xpress citing published study; DOI not confirmed in signal data | Confidence cap: Medium; recommend verifying journal citation before publish |
| Antidepressant Recall (carcinogen) | drug_or_treatment_claim + recall | ✅ **Pass** | Yes — FDA recall classification implied; Health.com + WCNC + 375K bottles figure corroborated across 2+ outlets | Breaking-recall exception applicable; confidence cap: Medium until FDA.gov notice directly retrieved |
| FDA OTC Drug High-Risk Alert | dosage_or_safety_guidance | ✅ **Pass** | Partial — The Healthy reporting; specific drug not confirmed in signal data | Pass with Medium cap; must verify specific drug name + FDA source URL before publishing |
| Infant Formula / Botulism Recall | recall | ✅ **Pass** | Yes — FDA.gov + KGW + Prevention; 3 botulism cases named | Breaking-recall exception used; confidence cap: Medium |
| Psilocybin / Mental Health (USC) | clinical_trial | ✅ **Pass** | Yes — Keck School of Medicine of USC official announcement; ClinicalTrials.gov record expected | Confidence: Medium; clinical study funding announcement, not results |
| NIH Prediabetes / Lifestyle Intervention | clinical_trial | ✅ **Pass** | Yes — NIH.gov direct (primary institutional source) | Confidence: High |
| Alfredo Sauce / Salmonella Recall | recall | ✅ **Pass** | Yes — FDA.gov + ABC News (Class I) + 6 outlets | No exception needed; confidence: High |
| Retatrutide / Weight Loss Trial | clinical_trial + drug_or_treatment_claim | ✅ **Pass** | Yes — UCHealth citing trial data; Cedars-Sinai + Mayo Clinic pancreatic cancer trial corroboration | Confidence: Medium; trial data vs. peer-reviewed publication distinction needed |

**All 9 candidates passed Skill 02b.** No candidates rejected at gate. 5 of 9 carry Medium confidence caps due to press-release or secondary-source primary evidence.

---

## EDITORIAL PRIORITY BOARD

| # | Priority | Timing | Topic | Signal Type | Category | Trend (/100) | Opp (/100) | Discover (/5) | Urgency | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **P1** | Immediate | Alfredo Sauce Salmonella Recall — FDA Class I | recall | Food Safety | 82 | 78 | 4 | **NOW** | High |
| 2 | **P1** | Immediate | USC Fish Oil Study: No Alzheimer's Benefit | medical_study | Medical Research | 88 | 85 | 5 | **NOW** | Medium |
| 3 | **P1** | Immediate | Infant Formula Recalled — Botulism Cases Linked | recall | FDA/CDC Regulatory | 80 | 82 | 5 | **NOW** | Medium |
| 4 | **P2** | Short-term (24–48h) | Antidepressant Recall — Carcinogen Risk (375K Bottles) | drug_or_treatment_claim + recall | FDA/CDC Regulatory | 74 | 76 | 4 | Today | Medium |
| 5 | **P2** | Short-term (24–48h) | Retatrutide Trial: 30% Weight Loss, On Par With Surgery | clinical_trial | Medical Research / Chronic Disease | 72 | 80 | 4 | Today | Medium |
| 6 | **P2** | Short-term (48–72h) | NIH Study: Lifestyle Changes Cut Prediabetes Progression to Multiple Chronic Diseases | clinical_trial | Medical Research / Public Health | 68 | 82 | 5 | This Week | High |
| 7 | **P3** | Scheduled (this week) | Shingles Vaccine Linked to Lower Dementia Risk, New Study Finds | medical_study | Medical Research / Aging | 62 | 72 | 4 | This Week | Medium |
| 8 | **P3** | Scheduled (this week) | FDA Flags Highest-Risk Safety Alert for Common OTC Drug | dosage_or_safety_guidance | FDA/CDC Regulatory | 60 | 68 | 3 | This Week | Medium |
| 9 | **P3** | Scheduled (this week) | USC Launches First Psilocybin Mental Health Clinical Study | clinical_trial | Mental Health / Medical Research | 58 | 70 | 4 | This Week | Medium |

---

## EDITORIAL BRIEFS

---

### BRIEF 1 — P1 · IMMEDIATE

**Primary Headline:** Alfredo Sauce Recalled in 41 States Over Salmonella Risk — FDA Calls It Most Serious Level

**Alternate Headlines:**
- The Alfredo Sauce in Your Fridge May Be Part of a 41-State Salmonella Recall
- FDA Issues Class I Recall on Alfredo Sauce: What You Need to Know
- Salmonella Risk Triggers Highest-Level FDA Recall on Alfredo Sauce Sold Nationwide

**Topic:** Alfredo sauce salmonella recall — FDA Class I designation
**Primary Entity:** Alfredo sauce (brand TBD — verify at FDA.gov)
**Signal Type:** recall
**Allowed Category:** Food safety / FDA regulatory updates
**Trend Strength Score:** 82 | **Opportunity Score:** 78 | **Discover Score:** 4
**Urgency:** NOW | **Confidence:** High | **Content Status:** New
**Source Count:** 7

**Why Now:**
FDA has classified this as a Class I recall — the agency's highest risk designation, meaning there is a reasonable probability of serious adverse health consequences or death. The recall spans 41 states. Multiple Tier-1 outlets (ABC News, PBS, NBC NY) have covered it, and it is within the freshness window. Class I food recalls are one of the highest-urgency story types in food safety journalism.

**Angle:** Consumer-protective explainer — what was recalled, what salmonella risk means, what to do with product in your home right now. Emphasis on the Class I designation and what that actually means for consumers (not just "check if you have it").

**Recommended Angle:** "FDA Class I Recall Explained: What the Alfredo Sauce Salmonella Warning Means and What to Do Now"

**Outline:**
1. **Lead:** What was recalled, when, by whom, and why — FDA Class I designation explained in plain language
2. **Distribution scope:** Which states, which retailers, lot codes (pull from FDA.gov recall notice)
3. **What is salmonella?** Symptoms, at-risk populations (pregnant, elderly, immunocompromised, young children), timeline of illness
4. **What Class I means:** FDA's three-tier recall system explained — why Class I is the most serious
5. **What to do:** Do not eat it, how to dispose of it safely, whether to seek medical attention, FDA reporting process
6. **Context:** Any prior incidents from this manufacturer (check FDA recall database)
7. **FAQ block:** "Can I cook it to kill salmonella?" / "What if I already ate it?" / "Is the brand still selling other products?"

**Key Data Points:**
- 41 states affected
- FDA Class I classification (highest risk tier)
- Salmonella contamination (verify specific strain from FDA notice)
- [Lot codes and UPC numbers: pull directly from FDA recall page]

⚠️ **Integrity note:** Specific brand name and lot code data must be pulled directly from the FDA.gov recall notice before publication. Do not publish without confirming product name. The signal data confirms Class I recall + salmonella + 41 states but does not name the brand.

**Source Plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| FDA.gov Recall Notice | https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts [verify specific URL] | 1 | Primary recall data, lot codes, brand |
| ABC News | https://abcnews.go.com [search: alfredo sauce recall] | 2 | Class I upgrade confirmation |
| PBS NewsHour | https://www.pbs.org/newshour/health [search: alfredo sauce recall] | 2 | Broad distribution coverage |
| NBC New York | https://www.nbcnewyork.com [search: alfredo sauce recall] | 2 | NY/NJ state-level consumer context |
| CDC Salmonella info | https://www.cdc.gov/salmonella/index.html | 1 | Symptom and safety guidance |

**Expert Sources:**
- FDA spokesperson quote from official recall notice
- CDC salmonella consumer guidance (cite directly — no outreach needed)
- Registered Dietitian or food safety specialist for "what to do at home" section (cite existing published guidance)

**SEO:**
- Primary keyword: `alfredo sauce recall 2026`
- Supporting: `salmonella recall 2026`, `FDA Class I recall food`, `alfredo sauce salmonella`, `is [brand] alfredo sauce safe`
- Format: News article + FAQ schema + HowTo schema (disposal instructions)
- Cluster: Food safety / FDA recalls
- Word count: 700–900 words

**Discover Notes:** High AI citation potential — specific named product, specific regulatory action, natural "Is [product] safe?" query format, official primary source available, durable consumer-safety answer.

**Next Steps:** Pull FDA.gov recall notice immediately for brand name + lot codes. Assign writer. Publish within 3 hours. Add internal links to any existing food safety or salmonella content.

---

### BRIEF 2 — P1 · IMMEDIATE

**Primary Headline:** Fish Oil Won't Prevent Alzheimer's, USC Study Finds — What It Actually Showed

**Alternate Headlines:**
- USC Researchers: Fish Oil Supplements Don't Slow Alzheimer's-Related Decline
- The Fish Oil and Dementia Study Everyone Is Searching for Today, Explained
- What the Viral USC Fish Oil Study Actually Found (And What It Didn't)

**Topic:** Fish oil supplements do not prevent Alzheimer's-related cognitive decline — USC/Keck Medicine study
**Primary Entity:** Hussein Yassine, MD (USC Keck Medicine researcher)
**Signal Type:** medical_study
**Allowed Category:** Medical research / Aging and longevity / Nutrition and diet science
**Trend Strength Score:** 88 | **Opportunity Score:** 85 | **Discover Score:** 5
**Urgency:** NOW | **Confidence:** Medium | **Content Status:** New
**Source Count:** 3

**Why Now:**
"Hussein yassine usc study" is the #1 Google Trends real-time breakout signal for this run. The study — from Keck Medicine of USC — found that fish oil supplements may not prevent Alzheimer's-related decline. This is a high-search, high-share health finding that directly challenges a widespread supplement belief. The SERP is likely thin on consumer-friendly explainers within the first 24 hours. This is the highest-opportunity content slot in today's run.

**Angle:** Myth-correcting explainer that respects the science: what the study actually found, what it didn't study, what the current evidence base for fish oil and brain health looks like, and what (if anything) someone should do differently. Lean into the "what this study actually showed vs. what headlines are saying" frame.

**Recommended Angle:** "The USC Fish Oil Study Explained: What It Found, What It Didn't, and What You Should Actually Do"

**Outline:**
1. **Lead:** Why this study is trending today and why it matters — fish oil is one of the most commonly taken supplements in the US; this study challenges a widely held belief
2. **What the study found:** Specific findings from Hussein Yassine's research — DHA/EPA supplementation and Alzheimer's biomarkers or cognitive decline (pull from Keck Medicine announcement)
3. **What the study did NOT prove:** Study design limitations — who was studied, over what period, what outcome was measured (biomarkers vs. clinical dementia)
4. **Where this fits in the larger evidence base:** What Cochrane, NIH, and prior RCTs show about fish oil and cognitive health — this is one study, not a final verdict
5. **What experts say:** Cite Hussein Yassine directly from the USC press release; pull any prior published commentary from nutrition scientists
6. **What you should actually do:** Should people stop taking fish oil? Context: fish oil has other evidence bases (cardiovascular, inflammation); the Alzheimer's-specific claim is what's challenged here
7. **FAQ:** "Does this mean fish oil is useless?" / "What supplements have evidence for brain health?" / "How do I read a study finding like this?"

**Key Data Points:**
- Researcher: Hussein Yassine, MD (USC Keck Medicine of USC) — verify institutional affiliation
- Supplement studied: Fish oil / omega-3 (DHA/EPA)
- Outcome: Alzheimer's-related cognitive decline or biomarker progression
- Study type: [verify — RCT vs. observational from press release]
- Fish oil usage: ~8% of US adults take omega-3 supplements (NIH NHANES data)

⚠️ **Integrity note:** Confidence is Medium — the primary signal is a university press release (Keck Medicine of USC). The peer-reviewed journal publication and DOI have not been confirmed in the signal data. Before publishing, verify: (1) which journal published this, (2) the DOI or PubMed record, (3) study design (RCT vs. observational). Do NOT present findings as definitive without noting study type and design limitations.

⚠️ **Integrity note:** Do not generalize this finding to all omega-3 uses. The claim is specific to Alzheimer's prevention. Cardiovascular and anti-inflammatory evidence bases are separate.

**Source Plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| Keck Medicine of USC announcement | https://www.keckmedicine.org/news/ (search: fish oil Alzheimer's Yassine) | 1 | Primary study data, researcher quote |
| Medical Xpress article (via signal) | https://medicalxpress.com [search: fish oil Alzheimer USC] | 2 | Secondary summary |
| NIH Omega-3 Supplement Fact Sheet | https://ods.od.nih.gov/factsheets/Omega3FattyAcids-Consumer/ | 1 | Evidence base context |
| Cochrane review (omega-3 and dementia) | https://www.cochranelibrary.com [search: omega-3 dementia] | 1 | Systematic review context |
| PubMed — Yassine publications | https://pubmed.ncbi.nlm.nih.gov/?term=Yassine+fish+oil+Alzheimer | 1 | Journal + DOI verification [URL unverified — verify before publish] |

**Expert Sources:**
- Hussein Yassine, MD — named researcher; quote from USC press release
- NIH Office of Dietary Supplements — cite official omega-3 consumer guidance
- Independent neurologist or geriatrician commentary (from existing STAT or NYT coverage if available)

**SEO:**
- Primary keyword: `fish oil Alzheimer's study 2026`
- Supporting: `hussein yassine USC study`, `does fish oil prevent dementia`, `omega-3 Alzheimer's research`, `fish oil supplements cognitive decline`
- Format: Explainer article + FAQ schema
- Cluster: Aging / longevity / supplement science
- Word count: 900–1,100 words

**Discover Notes:** Maximum AI citation potential. "What did the USC fish oil study find?" is a textbook AI-query question. Named researcher, named institution, specific supplement, specific disease. Strong durable answer potential. Prioritize being the clearest, most balanced explainer.

**Next Steps:** Locate peer-reviewed journal publication (DOI/PubMed). Verify study design. Assign writer immediately. Publish within 4 hours while search spike is active. Flag for nutrition/aging content cluster.

---

### BRIEF 3 — P1 · IMMEDIATE

**Primary Headline:** Infant Formula Recalled Nationwide After FDA Links It to Three Botulism Cases

**Alternate Headlines:**
- FDA Recalls Baby Formula Across All States — Three Botulism Cases Confirmed
- Botulism Outbreak Tied to Infant Formula: What Parents Need to Know Now
- Baby Formula Recall 2026: Which Products Are Affected and What to Do

**Topic:** Infant formula nationwide recall linked to botulism cases — FDA safety alert
**Primary Entity:** Recalled infant formula (brand TBD — verify FDA.gov)
**Signal Type:** recall
**Allowed Category:** FDA/CDC regulatory updates / Pediatric health / Food safety
**Trend Strength Score:** 80 | **Opportunity Score:** 82 | **Discover Score:** 5
**Urgency:** NOW | **Confidence:** Medium (breaking-recall exception applied)
**Content Status:** New
**Source Count:** 4 (KGW, Prevention, FDA.gov, and the FDA Infant Formula homepage in signal)

**Why Now:**
Botulism in infants is a pediatric emergency-level signal. Three confirmed cases tied to a single product — with at least one case in Washington State (KGW) — creates immediate consumer safety demand. FDA confirmed recall. This is a parent-audience story with maximum urgency and share potential. Pediatric health is a core allowed category.

**Angle:** Calm, authoritative, parent-protective explainer — which formula, which lot codes, why botulism is particularly dangerous in infants, what symptoms to watch for, and exactly what to do. This is not a fear piece; it is a "what you need to do right now" piece.

**Recommended Angle:** "Infant Formula Recall 2026: What the Botulism Warning Means and What Parents Should Do Immediately"

**Outline:**
1. **Lead:** Recall confirmed, FDA linked, 3 botulism cases — concise and factual
2. **Which products:** Brand, lot codes, UPC numbers, states affected (pull from FDA.gov recall notice — nationwide)
3. **What is infant botulism?** Differentiated from adult botulism — spores vs. toxin; why infants are uniquely vulnerable; symptoms (constipation, weak cry, poor feeding, floppiness)
4. **What to do right now:** Stop using immediately, do not give to another baby, how to dispose or return, whether to seek medical care
5. **What if my baby has already had this formula?** Symptom timeline, when to call a pediatrician vs. go to ER
6. **Context:** Any history of botulism-linked formula recalls (2022 formula shortage aftermath context); what FDA oversight of infant formula looks like post-2022
7. **FAQs:** "How long does botulism take to show symptoms?" / "Is this formula still on store shelves?" / "Can I switch to another brand immediately?"

**Key Data Points:**
- 3 confirmed botulism cases, including 1 in Washington State
- Nationwide recall (not state-limited)
- FDA.gov Infant Formula Homepage listed as signal source (confirms FDA tracking)
- Prevention magazine coverage confirms broad consumer media pickup
- Infant botulism: median onset 3–30 days after exposure (CDC)

⚠️ **Integrity note:** Breaking-recall exception applied — primary FDA notice confirmed via multiple credible outlets but specific brand/lot codes must be pulled directly from FDA.gov before publishing. Do not name a brand unless it is confirmed by FDA notice or official recall communication.

⚠️ **Integrity note:** Botulism is serious but treatable. Do not use fear language that implies certain harm. Frame around what to do, not just danger.

**Source Plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| FDA Infant Formula recall page | https://www.fda.gov/food/infant-formula-guidance-documents-regulatory-information | 1 | Primary recall data — brand, lot codes |
| FDA Recall database | https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts | 1 | Lot code verification |
| KGW (Portland) | https://www.kgw.com [search: baby formula botulism recall 2026] | 2 | Washington state case confirmation |
| Prevention | https://www.prevention.com/health/ [search: infant formula recall] | 2 | National consumer confirmation |
| CDC Infant Botulism | https://www.cdc.gov/botulism/index.html | 1 | Symptom guidance, clinical context |
| AAP (American Academy of Pediatrics) | https://www.aap.org/en/patient-care/newborn-and-infant-nutrition/ | 1 | Pediatric safety context |

**Expert Sources:**
- FDA recall statement (cite directly)
- CDC infant botulism clinical guidance (cite directly)
- Pediatrician quote: pull from AAP statement or existing media coverage
- AAP infant nutrition guidance

**SEO:**
- Primary keyword: `infant formula recall 2026`
- Supporting: `baby formula recall botulism`, `which formula is recalled`, `infant botulism symptoms`, `FDA baby formula recall`
- Format: Breaking news article + FAQ schema
- Cluster: Pediatric health / food safety / FDA recalls
- Word count: 800–1,000 words

**Discover Notes:** Near-perfect AI citation profile. "Is [formula brand] recalled?" and "What are botulism symptoms in babies?" are direct AI-query questions. Specific named entity (formula brand — once confirmed), specific health risk, official primary source, durable safety guidance answer.

**Next Steps:** Pull FDA.gov recall notice immediately for brand + lot codes. Assign senior writer with pediatric health experience. Publish within 3 hours. Flag for pediatric health content cluster.

---

### BRIEF 4 — P2 · SHORT-TERM (24–48h)

**Primary Headline:** Popular Antidepressant Recalled: What to Know About the Carcinogen Risk in 375,000 Bottles

**Alternate Headlines:**
- FDA Recalls 375,000 Bottles of Antidepressant Over Elevated Carcinogen Levels
- Your Antidepressant May Be Part of a Major Recall — Here's What to Do
- Antidepressant Recall 2026: Carcinogen Found, What Patients Should Do

**Topic:** Antidepressant recall — approximately 375,000 bottles, high levels of a carcinogen detected
**Primary Entity:** Recalled antidepressant (specific drug name TBD — verify FDA.gov)
**Signal Type:** drug_or_treatment_claim + recall
**Allowed Category:** FDA/CDC regulatory updates / Chronic disease management / Mental health
**Trend Strength Score:** 74 | **Opportunity Score:** 76 | **Discover Score:** 4
**Urgency:** Today | **Confidence:** Medium
**Content Status:** New | **Source Count:** 3

**Why Now:** 375,000 bottles is a large-scale drug recall. The carcinogen angle (similar to historical NDMA recalls affecting metformin, ranitidine) will drive significant patient anxiety. Mental health patients stopping medication abruptly is a known clinical risk — this brief must address that directly.

**Recommended Angle:** "Antidepressant Recalled for Carcinogen Risk: A Practical Guide for Patients on What to Do Next"

**Outline:**
1. What was recalled, how many bottles, what carcinogen was detected
2. What "elevated carcinogen levels" actually means — short-term risk context vs. long-term exposure risk
3. What NOT to do: do not stop taking medication abruptly without physician guidance — withdrawal risk
4. What to do: contact prescribing physician, check lot number, FDA recall process for drug returns
5. Historical context: NDMA contamination in ranitidine, metformin — how these recalls work
6. FAQs: "How do I know if my bottle is affected?" / "Is one pill dangerous?" / "Can I switch to a generic?"

⚠️ **Integrity note:** DO NOT name the drug until confirmed via FDA.gov drug recall notice. Signal sources name ~375K bottles and "popular antidepressant" but specific drug name not confirmed in signal data.
⚠️ **Integrity note:** Critical safety note — antidepressant withdrawal can be medically serious. Any coverage must prominently advise readers NOT to stop medication without physician consultation.
⚠️ **Integrity note:** Carcinogen risk from short-term recall-level contamination is typically very low — do not overstate. Frame around "what to do" not "you have cancer."

**Key Source Plan:**
| Publisher | URL | Tier |
|---|---|---|
| FDA drug recall database | https://www.fda.gov/drugs/drug-safety-and-availability/drug-recalls | 1 |
| Health.com (signal source) | https://www.health.com [search: antidepressant recall carcinogen 2026] | 2 |
| WCNC (signal source) | https://www.wcnc.com [search: antidepressant recall 375000] | 2 |
| FDA NDMA/carcinogen guidance | https://www.fda.gov/drugs/drug-safety-and-availability/information-about-nitrosamines | 1 |

**SEO:** Primary keyword: `antidepressant recall 2026` · Supporting: `[drug name] recall carcinogen`, `FDA drug recall mental health`, `what to do antidepressant recall` · Format: Explainer + FAQ · Word count: 700–900

**Next Steps:** Confirm drug name + lot codes via FDA.gov. Assign writer. Brief mental health editor on withdrawal safety messaging. Publish within 24–36 hours.

---

### BRIEF 5 — P2 · SHORT-TERM (24–48h)

**Primary Headline:** New Weight-Loss Drug Retatrutide Helped People Lose 30% of Body Weight — Matching Bariatric Surgery

**Alternate Headlines:**
- Retatrutide: The New Weight-Loss Drug That Rivals Surgery, Explained
- Is Retatrutide the Next Ozempic? What the Trial Data Actually Shows
- Triple-Receptor Weight-Loss Drug Achieves 30% Body Weight Reduction in Trial

**Topic:** Retatrutide clinical trial results — 30% body weight loss, comparable to bariatric surgery; also a separate pancreatic cancer trial signal (Cedars-Sinai/Mayo) — treated as two related signals in this brief
**Primary Entity:** Retatrutide (Eli Lilly investigational drug)
**Signal Type:** clinical_trial
**Allowed Category:** Medical research / Chronic disease management (obesity, diabetes)
**Trend Strength Score:** 72 | **Opportunity Score:** 80 | **Discover Score:** 4
**Urgency:** Today | **Confidence:** Medium
**Content Status:** New | **Source Count:** 3

**Why Now:** GLP-1 and weight-loss drug interest remains at sustained high search volume ("weight loss" trending at 62 on Google Trends this week). Retatrutide is the next-generation triple-receptor agonist beyond semaglutide/tirzepatide. Trial data showing 30% body weight loss — on par with surgery — is a significant clinical benchmark. This is the story the Ozempic audience will want to read next.

**Recommended Angle:** "Retatrutide Explained: What the 30% Weight-Loss Trial Result Means and How It Compares to Surgery and Ozempic"

**Outline:**
1. What retatrutide is — mechanism (GIP/GLP-1/glucagon triple agonist vs. semaglutide's single, tirzepatide's dual)
2. What the trial showed — 30% body weight reduction, trial size, duration, patient population
3. What "on par with bariatric surgery" means — surgical average outcomes as benchmark
4. How it compares to Ozempic (semaglutide ~15%) and Mounjaro/Zepbound (tirzepatide ~22%)
5. Side effects from trial data — nausea, GI profile
6. Where this drug is in development — not FDA approved; timeline estimate
7. Pancreatic cancer + weight connection note (brief): Cedars-Sinai / Mayo trial on pancreatic cancer treatment showing doubled survival — separate story but part of the week's cancer treatment narrative
8. FAQs: "Can I get retatrutide now?" / "Is it better than Ozempic?" / "What's the cost likely to be?"

⚠️ **Integrity note:** Trial data from UCHealth reporting — verify whether this is a peer-reviewed publication or a conference presentation. Distinguish phase 2 vs. phase 3 data. "On par with surgery" is a comparative frame that requires careful sourcing — verify the specific surgical outcome benchmark used in the trial.
⚠️ **Integrity note:** Drug is not FDA approved. Do not frame as "available" or create demand without noting this clearly.

**Key Source Plan:**
| Publisher | URL | Tier |
|---|---|---|
| UCHealth article | https://www.uchealth.org/today/ [search: retatrutide weight loss trial] | 2 |
| ClinicalTrials.gov (retatrutide) | https://clinicaltrials.gov/search?term=retatrutide | 1 |
| Cedars-Sinai pancreatic cancer | https://www.cedars-sinai.org/newsroom/ [search: pancreatic cancer drug doubled survival] | 2 |
| Mayo Clinic trial | https://www.mayoclinic.org/news [search: metastatic pancreatic cancer trial hope] | 1 |
| FDA GLP-1 drug approvals context | https://www.fda.gov/drugs/drug-approvals-and-databases/novel-drug-approvals-fda | 1 |

**SEO:** Primary keyword: `retatrutide weight loss` · Supporting: `retatrutide vs Ozempic`, `retatrutide trial results`, `new weight loss drug 2026`, `GLP-1 triple agonist` · Format: Explainer + comparison table · Word count: 1,000–1,200

**Next Steps:** Locate trial publication or conference source. Assign writer with GLP-1/obesity beat experience. Publish within 36–48 hours. Strong internal linking opportunity to existing Ozempic/tirzepatide coverage.

---

### BRIEF 6 — P2 · SHORT-TERM (48–72h)

**Primary Headline:** NIH Study: Lifestyle Changes Alone Cut the Risk of Multiple Chronic Diseases in People With Prediabetes

**Alternate Headlines:**
- You Can Cut Your Risk of Multiple Chronic Diseases With Lifestyle Changes, NIH Finds
- Prediabetes Doesn't Have to Become Diabetes — Or Heart Disease. Here's What the Evidence Shows
- The NIH Prediabetes Study That Should Change How We Think About Prevention

**Topic:** NIH clinical trial — lifestyle intervention in adults with prediabetes reduced risk of developing multiple chronic conditions (not just diabetes)
**Primary Entity:** NIH prediabetes lifestyle intervention study
**Signal Type:** clinical_trial
**Allowed Category:** Medical research / Chronic disease management / Public health
**Trend Strength Score:** 68 | **Opportunity Score:** 82 | **Discover Score:** 5
**Urgency:** This Week | **Confidence:** High
**Content Status:** New | **Source Count:** 2 (NIH.gov primary + Cedars-Sinai/clinical trials cluster)

**Why Now:** NIH.gov is a Tier-1 primary source — this is a direct institutional announcement, not a press release from a secondary reporter. Prediabetes affects ~96 million Americans (CDC). The finding that lifestyle changes reduce risk of *multiple* chronic diseases (not just type 2 diabetes) broadens the public health relevance significantly. High search durability — this is a prevention-oriented story with evergreen demand.

**Recommended Angle:** "NIH Study: For People With Prediabetes, Lifestyle Changes Cut Risk of Multiple Chronic Diseases — Not Just Diabetes"

**Outline:**
1. Context: 96 million Americans have prediabetes; most don't know it; the standard worry is "it will become diabetes"
2. What the study found: specific lifestyle intervention (what changes?), what chronic conditions were reduced beyond diabetes (cardiovascular? kidney? hypertension?), study size and duration
3. Why this expands the case for prevention: not just "avoid diabetes" but "protect your whole system"
4. What the lifestyle intervention actually involved — diet changes? Exercise? How intensive? (pull from NIH announcement)
5. What this means practically for someone with prediabetes — is this achievable without a clinical program?
6. What the science says works: Mediterranean diet + 150 min/week activity per CDC DPP (Diabetes Prevention Program) framework
7. FAQs: "Do I have prediabetes?" / "What's the difference between prediabetes and diabetes?" / "Can I reverse prediabetes?"

⚠️ **Integrity note:** Verify specific chronic conditions studied — signal says "multiple chronic conditions" without specifying. Pull from NIH announcement for exact outcome measures. Do not generalize to conditions not studied.

**Key Source Plan:**
| Publisher | URL | Tier |
|---|---|---|
| NIH News Release | https://www.nih.gov/news-events/news-releases [search: prediabetes lifestyle chronic conditions 2026] | 1 |
| ClinicalTrials.gov (DPP-related) | https://clinicaltrials.gov/search?term=prediabetes+lifestyle | 1 |
| CDC Prediabetes facts | https://www.cdc.gov/diabetes/prevention/prediabetes.html | 1 |
| CDC Diabetes Prevention Program | https://www.cdc.gov/diabetes/prevention/index.html | 1 |

**SEO:** Primary keyword: `prediabetes lifestyle study NIH 2026` · Supporting: `can you reverse prediabetes`, `prediabetes chronic disease risk`, `NIH diabetes prevention`, `lifestyle changes prediabetes` · Format: Explainer + FAQ + schema (HowTo for lifestyle steps) · Word count: 900–1,100

**Next Steps:** Pull NIH announcement for specific chronic conditions and intervention details. Assign writer. Strong evergreen cluster opportunity — connect to existing prediabetes, diabetes, and metabolic health content.

---

### BRIEF 7 — P3 · SCHEDULED (THIS WEEK)

**Headline:** Shingles Vaccine May Lower Dementia Risk — Here's What a New Study Found

**Topic:** New study suggests shingles vaccine (Shingrix) associated with reduced dementia risk
**Primary Entity:** Shingles vaccine (Shingrix / zoster vaccine recombinant adjuvanted)
**Signal Type:** medical_study
**Allowed Category:** Medical research / Aging and longevity
**Trend Strength Score:** 62 | **Opportunity Score:** 72 | **Discover Score:** 4
**Urgency:** This Week | **Confidence:** Medium | **Content Status:** New | **Source Count:** 2

**Angle:** Cautious explainer — what the study found, what type of study it was (observational), what the proposed mechanism is (controlling herpes zoster inflammation and its effects on neuroinflammation), and what it does NOT mean (not proven prevention, not a reason to get vaccinated solely for dementia). Emphasize: Shingrix is already recommended for adults 50+ for shingles prevention — this study adds to the case.

**Key Data Points:** Medical Xpress reporting on published study; specific journal TBD — verify. Shingrix is CDC-recommended for adults 50+.

⚠️ **Integrity note:** Source is Medical Xpress (Tier 2 aggregator). Must verify journal, DOI, study design (observational vs. RCT) before publish. Observational — cannot claim causation. Do not frame as "shingles vaccine prevents dementia."

**Key Sources:**
- Medical Xpress article: https://medicalxpress.com [search: shingles vaccine dementia risk 2026] | Tier 2
- PubMed verification: https://pubmed.ncbi.nlm.nih.gov [search: shingles vaccine dementia] | Tier 1 [URL unverified]
- CDC Shingrix recommendation: https://www.cdc.gov/vaccines/vpd/shingles/index.html | Tier 1

**SEO:** Primary: `shingles vaccine dementia risk study` · Supporting: `Shingrix dementia prevention`, `zoster vaccine brain health`, `shingles vaccine benefits` · Format: Explainer · Word count: 700–900

**Next Steps:** Verify journal + DOI. Confirm study design. Assign writer. Publish mid-week.

---

### BRIEF 8 — P3 · SCHEDULED (THIS WEEK)

**Headline:** FDA Issues Highest-Risk Safety Alert for a Common OTC Drug — What It Means

**Topic:** FDA highest-risk safety classification for a common over-the-counter drug
**Primary Entity:** OTC drug (specific name TBD — verify FDA.gov)
**Signal Type:** dosage_or_safety_guidance
**Allowed Category:** FDA/CDC regulatory updates / Chronic disease management
**Trend Strength Score:** 60 | **Opportunity Score:** 68 | **Discover Score:** 3
**Urgency:** This Week | **Confidence:** Medium | **Content Status:** New | **Source Count:** 1 (The Healthy)

**Angle:** Consumer explainer — what the highest-risk FDA classification means for an OTC drug (this is unusual, since most OTC drugs don't carry FDA's most serious warning tier), what the drug is, what the risk is, and what to do.

⚠️ **Integrity note:** Single source (The Healthy, Tier 2 health media). Specific drug name not confirmed in signal data. DO NOT publish without confirming via FDA.gov. This brief is P3 partly because of weak source confidence — source validation must happen before writing begins.

**Key Sources:**
- FDA safety alerts: https://www.fda.gov/safety/medical-product-safety-information | Tier 1 — must verify
- The Healthy (signal source): https://www.thehealthy.com [search: FDA OTC drug highest risk 2026] | Tier 2

**SEO:** Primary: `FDA OTC drug safety alert 2026` · Supporting: `[drug name] FDA warning`, `common OTC drug recall`, `FDA drug safety classification explained` · Format: News explainer + FAQ · Word count: 600–800

**Next Steps:** Confirm drug name + FDA source. If FDA primary source found, upgrade to P2. If unconfirmed after 24h, defer or kill.

---

### BRIEF 9 — P3 · SCHEDULED (THIS WEEK)

**Headline:** USC Is Launching Its First Clinical Study of Psilocybin for Mental Health — Here's What We Know

**Topic:** USC Keck School of Medicine receives funding to launch first USC clinical study of psilocybin for mental health
**Primary Entity:** USC Keck School of Medicine psilocybin clinical study
**Signal Type:** clinical_trial
**Allowed Category:** Mental health and psychology / Medical research
**Trend Strength Score:** 58 | **Opportunity Score:** 70 | **Discover Score:** 4
**Urgency:** This Week | **Confidence:** Medium | **Content Status:** New | **Source Count:** 2

**Angle:** Forward-looking explainer — what is known about psilocybin for mental health (existing Johns Hopkins, NYU, COMPASS Pathways trial data), what this new USC study adds, what conditions will be studied, where psilocybin therapy stands legally and clinically right now, and what the realistic timeline to availability looks like. Frame for a curious, health-conscious reader who has heard about "magic mushrooms for depression" and wants to understand where the science actually is.

⚠️ **Integrity note:** This is a funding announcement for a clinical study launch — not results. Do not imply treatment efficacy from this story. Lead with "what is being studied and why" not "psilocybin treats [condition]."
⚠️ **Integrity note:** Legal status of psilocybin varies by state. Note clearly that psilocybin is still Schedule I federally; clinical access is research-only.

**Key Sources:**
- Keck School of Medicine of USC announcement: https://keck.usc.edu/news [search: psilocybin clinical study mental health 2026] | Tier 1
- ClinicalTrials.gov: https://clinicaltrials.gov/search?term=psilocybin+USC | Tier 1 [URL unverified — verify]
- Johns Hopkins Center for Psychedelic and Consciousness Research: https://hopkinspsychedelic.org/ | Tier 1
- NIMH psilocybin research context: https://www.nimh.nih.gov [search: psilocybin] | Tier 1

**SEO:** Primary: `psilocybin mental health clinical trial USC` · Supporting: `psilocybin depression research 2026`, `psilocybin therapy how does it work`, `psychedelic therapy clinical trials` · Format: Explainer + FAQ · Word count: 900–1,100

**Next Steps:** Pull specific mental health condition being studied. Verify ClinicalTrials.gov registration. Assign writer with mental health / psychedelic science background. Publish Thursday–Friday.

---

## REJECTED TOPICS LOG

| Topic | Signal Source | Rejection Reason | Skill |
|---|---|---|---|
| California health insurance tax increase | CalMatters | Off-category — pure state policy/political; no new health data or patient clinical angle | 02 |
| Gallup: Healthcare affordability at 5-year low | Gallup | Monitored / borderline — health-adjacent policy but no clinical or research content; audience_relevance < 70 for this site's science-forward mandate | 02 |
| AI in health / clinical trials / ChatGPT health | APA, Google, OpenAI, Clinical Trial Vanguard | Off-category adjacency — technology/AI category, not core health science; no actionable clinical or consumer health angle for target audience | 02 |
| RFK Jr. mental health funding ($700M) | STAT News | Monitored — political adjacency (RFK Jr. as political figure); STAT explicitly notes grants aren't new; no new health data behind headline; brand_safety borderline | 02 |
| RFK Jr. goes after journal that removed vaccine study | MedPage Today | Rejected — political/controversy framing; anti-vaccine misinformation adjacency; excluded category risk | 02 |
| Wellness commercial noise (Balenciaga, Hilton, Samsung VivaTech, Costco, MSC cruises) | WWD, Hotel Dive, Samsung, Yahoo Finance, Cool Hunting | Excluded category — commercial/brand wellness marketing; not health science | 02 |
| Jeremy Clarkson health / Mitch McConnell health / Joan Cusack health | Google Trends rising queries | Celebrity/political figure health gossip; excluded category (brand safety — celebrity fluff, no medical content) | 01/02 |
| Planet fitness Juneteenth hours | Google Trends rising | Off-category — retail/logistics query | 01 |
| Crumbl cookie/drink nutrition facts | Google Trends rising | Off-category — consumer food product; no health science angle; excluded (celebrity wellness/product marketing adjacency) | 01 |
| Sauerkraut diet / RFK Jr. sauerkraut diet | Google Trends rising | Off-category — political figure diet trend; excluded (celebrity wellness fads without evidence) | 01 |
| Study challenges conventional pet aging thinking | American Veterinary Medical Association | Off-category — pet health excluded unless zoonotic; no zoonotic angle | 02 |
| NOAA North Atlantic Right Whale health | NOAA Fisheries | Off-category — wildlife conservation, not human health | 01 |
| Pauline Newman judicial fitness challenge | Google Trends rising | Off-category — legal/political, not health | 01 |
| Fewer employees skip work where medical marijuana is legal | Marijuana Moment | Borderline — workplace policy, not clinical health; single source (Marijuana Moment, not Tier-1); category fit < 60; audience relevance insufficient | 02 |
| LungSMART bilingual digital health content | Rethinking Clinical Trials | Off-category — clinical trial methodology/recruitment operations; not consumer health | 02 |
| Wearables in clinical research | Clinical Trials Arena | Off-category — health technology/industry; not consumer health or research findings | 02 |
| Human-AI collaboration for cancer trial recruitment | The Business Journals | Off-category — health tech/business | 02 |
| Biotech turned trial failure into AI model | STAT News | Off-category — biotech/business | 02 |
| Czechia clinical trials hub | Euractiv | Off-category — international health industry | 02 |
| Adaptive deep brain stimulation / Parkinson's gait (Nature) | Nature | Retained for consideration, then deferred — strong signal but technical depth required; single Nature study without secondary coverage yet; move to P4 evergreen backlog for fuller treatment | 04 |
| University of Michigan Paradromics brain-computer interface | Michigan Medicine | Deferred — groundbreaking but highly technical; single institutional source; no secondary coverage or search velocity detected; route to P4 | 04 |
| Mac and cheese recall (526,000 packages) | NewsNation | Merged into food safety recall cluster — already covered by Alfredo sauce brief (P1); Brief 1 should note this as related recall in the same food safety cycle | 01 |
| Ice cream recall (3 states) | Yahoo | Signal too narrow (3 states); lower urgency than Class I food recalls above; deferred to P4 monitor | 04 |
| Global clinical trial for golden staph bloodstream infections | Medical Xpress | Strong study but very clinical/technical; low consumer search demand vs. other retained candidates; route to P4 evergreen | 04 |

---

## INTEGRITY FLAGS — CONSOLIDATED

The following ⚠️ flags require editorial action before publication:

| # | Brief | Flag | Action Required |
|---|---|---|---|
| 1 | Brief 1 (Alfredo recall) | Brand name and lot codes not confirmed in signal data | Pull FDA.gov recall notice before writing or publishing |
| 2 | Brief 2 (USC fish oil) | Journal/DOI not confirmed; confidence Medium (press release only) | Verify peer-reviewed journal and DOI; note study design (RCT vs. observational) in article |
| 3 | Brief 2 (USC fish oil) | Do not generalize to all omega-3 uses | Keep finding scoped to Alzheimer's-specific claim only |
| 4 | Brief 3 (infant formula) | Brand/lot codes not confirmed | Pull FDA.gov infant formula recall page before writing |
| 5 | Brief 3 (infant formula) | Botulism is serious but treatable | Avoid fear language; emphasize "what to do" |
| 6 | Brief 4 (antidepressant recall) | Drug name not confirmed | Do not name drug until FDA.gov drug recall notice confirms |
| 7 | Brief 4 (antidepressant recall) | DO NOT advise stopping medication | Must include prominent warning: do not stop antidepressants without physician consultation |
| 8 | Brief 4 (antidepressant recall) | Carcinogen risk framing | Short-term recall-level exposure risk is typically low — do not overstate cancer risk |
| 9 | Brief 5 (retatrutide) | Trial publication type not confirmed (conference vs. peer-reviewed) | Verify; note phase of development clearly; drug is not FDA-approved |
| 10 | Brief 5 (retatrutide) | "On par with surgery" comparative frame requires specific benchmark citation | Verify the exact surgical outcome comparator used in the study |
| 11 | Brief 6 (NIH prediabetes) | Specific chronic conditions studied not named in signal | Pull NIH announcement for exact outcomes; do not generalize |
| 12 | Brief 7 (shingles vaccine) | Observational study — cannot claim causation | Frame as "may reduce risk / associated with" not "prevents dementia" |
| 13 | Brief 7 (shingles vaccine) | Journal/DOI not confirmed (Medical Xpress aggregator) | Must verify before writing |
| 14 | Brief 8 (OTC drug alert) | Specific drug not named; single secondary source | Confirm via FDA.gov before writing; upgrade or kill based on confirmation |
| 15 | Brief 9 (psilocybin) | Funding announcement ≠ results | Frame as "launching study" not "psilocybin treats [condition]" |
| 16 | Brief 9 (psilocybin) | Psilocybin is Schedule I federally | Include legal status context; research-only access |
| 17 | All health briefs | Association ≠ causation | All writers: default to observational/association language unless RCT with pre-specified outcomes |

---

## RUN NOTES

```yaml
run_date: 2026-06-21
niche: health and wellness
signals_reviewed: 144
topics_retained: 9
topics_rejected: 135
p1_count: 3
p2_count: 3
p3_count: 3
p4_deferred: 4  # Deep brain stim, Michigan BCI, golden staph trial, ice cream recall
integrity_flags_total: 17
top_topic: "Alfredo Sauce Salmonella Recall — FDA Class I"
key_themes:
  - FDA food recalls (salmonella, botulism) — multiple simultaneous Class I events
  - Drug/antidepressant recall (carcinogen)
  - Fish oil / Alzheimer's study (breakout Google Trends signal)
  - GLP-1 / weight loss drug advances (retatrutide)
  - Prediabetes prevention (NIH primary source)
  - Shingles vaccine / dementia (aging + prevention)
  - Psilocybin mental health research (USC launch)
tools_used: [serpapi_news_search, serpapi_trends_prefetch]
tools_unavailable: [COMPOSIO_SEARCH_TRENDS (direct call not made — prefetch used), reddit_api (not called this run), social_search (not called this run), exa_search (not called this run)]
google_trends_available: true
google_trends_tool: serpapi_prefetch
search_velocity_source: google_trends
site_url_configured: false
self_check: skipped — competitor-check fallback active
deferred_topics_file: not found
run_history_file: not found — cross-run staleness check skipped
cross_run_staleness: N/A (no run history available)
dashboard_output: outputs/daily_newsroom_dashboard/2026-06-21.html
notes: >
  Strongest signal of the run: "hussein yassine usc study" — real-time Google Trends 
  breakout. This and the infant formula botulism recall are the two most time-sensitive 
  stories. The food recall cluster (Alfredo sauce + infant formula + antidepressant) 
  represents an unusually dense recall week — consider a weekly "FDA Recall Roundup" 
  format if this pattern continues. Retatrutide is a strong P2 that should link to 
  Ozempic/tirzepatide cluster. NIH prediabetes study is the highest-confidence 
  (institutional primary source) story and has strong evergreen cluster potential. 
  No deferred topics file or run history found — recommend creating both files to enable 
  cross-run staleness detection and deferred topic recheck functionality.
```

---

**Run complete.** Dashboard written to `outputs/daily_newsroom_dashboard/2026-06-21.html`. `data/run_history.yaml` entry queued (file creation required — not found on disk). `data/deferred_topics.yaml` entry queued for 4 P4-deferred topics (deep brain stimulation Parkinson's study, Michigan Paradromics BCI, golden staph antibiotic trial, regional ice cream recall).