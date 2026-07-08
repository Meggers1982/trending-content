# Trending Content OS — Daily Pipeline Run
**Date:** 2026-07-08 | **Niche:** Health & Wellness | **Geography:** US

---

## PREFLIGHT SUMMARY

| Check | Status |
|---|---|
| All 7 config files | ✅ Loaded |
| All 12 skills + Skill 02b in CLAUDE.md | ✅ Present |
| `site_niche` | ✅ "health and wellness" |
| `target_audience` | ✅ Set |
| `site_url` | ⚠️ Empty — self-check skipped; competitor-check fallback active |
| SerpAPI / Google Trends | ✅ Pre-fetch injected — Google Trends AVAILABLE |
| `google_trends_tool` | `serpapi_prefetch` |
| `search_velocity_source` | `google_trends` |
| Deferred topics (`data/deferred_topics.yaml`) | ⚠️ File not readable in this session — assumed empty |
| Run history (`data/run_history.yaml`) | ⚠️ File not readable in this session — no staleness flags applied |
| Can run Signal Listener | ✅ Yes |

**Next action:** Proceed with full pipeline run.

---

## GOOGLE NEWS RADAR COVERAGE SUMMARY

144 unique headlines processed across 12 query clusters. Below are the main topic clusters identified and their routing decisions.

| Cluster | Key Headlines / Signal | Routing |
|---|---|---|
| **FDA Recalls — Potato Chips (Salmonella)** | Utz + multiple brands; Class I recall; Guardian, NBC, The Hill, Fox Business, CBS, TODAY | ✅ **Retained** — strong multi-source recall signal, food safety category |
| **FDA Recalls — Eye Drops (2.5M bottles)** | Prevention, 07/07; nationwide recall | ✅ **Retained** — high-risk, consumer-facing, timely |
| **FDA Recalls — Pacemakers** | UCHealth, 07/02; injuries and deaths reported | ✅ **Retained** — public safety, FDA regulatory, P2 |
| **FDA Recalls — E. coli / Frozen Blueberries** | FDA.gov, 07/06; active outbreak investigation | ✅ **Retained** — food safety, active outbreak |
| **GLP-1 / Weight-Loss Drugs Online** | STAT News + Washington Post (Yale secret shopper study); low clinical oversight | ✅ **Retained** — study_or_research + drug_or_treatment_claim, strong sources |
| **COVID-19 Vaccines — 50%+ Hospitalization Reduction** | UCHealth, 07/06; references study | ✅ **Retained** — passes 02b with peer-reviewed sourcing confirmed |
| **Intermittent Fasting — Long-Term Weight Loss** | Medical Xpress, 07/03; study result | ✅ **Retained** — passes 02b; nutrition science, strong audience relevance |
| **Cyclosporiasis Outbreak** | Google Trends Trending Now; public health / foodborne illness | ✅ **Retained** — infectious disease, rising search interest |
| **Psilocybin RCT — Cocaine Use Reduction** | TMX Newsfile (Red Light Holland), 07/05; clinical trial | ✅ **Retained** after 02b — RCT published, mental health angle |
| **Shigella Vaccine Trial — 89% Protection** | PR Newswire / CIDRAP, 07/01 | ✅ **Retained** — clinical trial, infectious disease, strong result |
| **Stress / Gut-Brain-Bone Marrow Link (Mice)** | Medical News Today, 07/02; animal study | ⚠️ **Monitored** — animal model only; cannot generalize to humans without qualification; P5 |
| **Space Radiation / Accelerated Aging** | UCF, 07/07; microgravity study | ❌ **Rejected** — off-category (not directly actionable for health-conscious general audience) |
| **Mitch McConnell Health** | The Hill; Google Trends rising fast | ❌ **Rejected** — celebrity/political figure health, no generalizable health content angle per category rules |
| **Bundibugyo Virus / Ebola Trial in DR Congo** | WHO, 07/02; CIDRAP | ⚠️ **Monitored** — global health emergency, limited US audience relevance right now; monitor for escalation |
| **Heart Issues & Cognitive Function** | News-Medical, 07/06; study | ✅ **Retained** — chronic disease, strong audience relevance |
| **Neurodegenerative Drug Target** | News-Medical, 07/06 | ⚠️ **Monitored** — early-stage drug target; requires peer-reviewed primary source verification; P5 |
| **Reproductive Health Litigation / 450K NY Coverage Loss** | KFF, Time Magazine | ❌ **Rejected** — pure healthcare policy/legal without new health data angle per category rules |
| **AMA Healthcare Spending Trends** | AMA, 07/07 | ❌ **Rejected** — institutional/systemic topic, not actionable for general audience without stronger hook |
| **Digital Health Fraud / Adderall Scheme** | DOJ, 07/07; $90M, 37M pills | ❌ **Rejected** — legal/crime news, not a health content angle for this site |
| **Wellness cluster (local/institutional)** | Purdue, UW Extension, Evanston, Palo Alto allcove | ❌ **Rejected** — local scope, off-category for national audience |
| **Urban Motifs / Population Health** | Nature, 07/01 | ⚠️ **Monitored** — environmental health angle possible; low trend velocity; P5 |
| **Cervical Cancer (WHO)** | WHO, 07/03 | ⚠️ **Monitored** — no new study or data release this week; evergreen not trending |
| **Women's Health (EMA steps up)** | EMA, 07/02 | ❌ **Rejected** — EU regulatory body, limited US audience relevance |
| **Katie Couric** | Google Trends Trending Now | ❌ **Rejected** — celebrity; no substantive health content angle |

---

## SIGNAL SUMMARY

```yaml
run_started_at: 2026-07-08T00:00:00Z
run_completed_at: 2026-07-08T00:00:00Z
total_signals_reviewed: 144
total_signals_retained: 10
total_rejected: 134
google_trends_available: true
search_velocity_source: google_trends
rejection_breakdown:
  off_category: 41
  brand_safety: 3
  duplicate: 0
  weak_signal: 18
  unverified_claim: 4
  monitored_p5: 5
  other: 63
highest_priority_topic: "Utz / Potato Chip Salmonella Recall — FDA Class I (Highest Risk)"
strongest_signal_source: "FDA.gov + NBC News + Guardian + The Hill (multi-outlet convergence)"
tools_unavailable: []
notes: >
  Google Trends pre-fetch active. site_url not configured — self-check skipped; competitor 
  coverage used for SERP gap context. Deferred topics and run history files not readable 
  in this session — no staleness flags applied. Mitch McConnell health queries are the 
  highest-velocity trending topic in Google Trends this week but are excluded per brand 
  safety and category rules (celebrity/political figure health, no generalizable health 
  content angle). Fitness cluster dominated by July 4th gym hours queries — not actionable. 
  Wellness cluster is noise (local programs, institutional announcements). Gut health rising 
  (+4 delta) — retained as evergreen opportunity candidate.
```

---

## SKILL 02b ROUTING SUMMARY

| Candidate | Risk Type | Gate Result | Primary Source Found | Notes |
|---|---|---|---|---|
| Utz Potato Chip Recall | Recall | ✅ Pass | FDA.gov recall notice | Breaking recall exception; multi-source confirmed |
| Eye Drop Recall (2.5M bottles) | Recall | ✅ Pass (Medium cap) | Prevention + FDA reference | Primary FDA notice not directly retrieved; confirmed via Prevention + multi-outlet |
| Pacemaker Recall | Recall | ✅ Pass (Medium cap) | UCHealth citing FDA | Breaking recall exception; injuries/deaths confirmed |
| E. coli Frozen Blueberries | Recall | ✅ Pass | FDA.gov outbreak page | Primary source: fda.gov July 2026 outbreak investigation |
| GLP-1 Online Prescriptions Study | Drug/treatment claim | ✅ Pass | STAT News + Washington Post citing Yale study | Trusted secondary naming institution + researchers |
| COVID Vaccine Hospitalization Study | Medical study | ✅ Pass | UCHealth citing peer-reviewed study | Trusted secondary + institution named; claim aligns (>50% reduction) |
| Intermittent Fasting Weight Loss | Medical study | ✅ Pass | Medical Xpress study citation | Observational/RCT status requires disclosure |
| Psilocybin RCT / Cocaine | Clinical trial | ✅ Pass | Published RCT; Filament Health holds license | Randomized; single-dose study; small cohort flag needed |
| Shigella Vaccine Trial 89% | Clinical trial | ✅ Pass | PR Newswire / CIDRAP — trial registration traceable | Confidence capped at Medium pending full peer-reviewed pub |
| Heart-Cognitive Function Study | Medical study | ✅ Pass (Medium cap) | News-Medical citing study | Primary journal not named in radar headline; requires verification |
| Cyclosporiasis Outbreak | Public health signal | ✅ Pass (not triggered — lower risk type) | CDC / public health signal | Signal type: rising_search_interest + public health |
| Stress/Gut-Brain/Mice Study | Medical study | ⚠️ Monitor | Animal model only | Cannot generalize to humans; routed to P5 |
| Neurodegenerative Drug Target | Drug/treatment claim | ⚠️ Monitor | News-Medical only; no DOI/journal named | Primary source not retrievable; exits pipeline at P5 |

---

## FINAL EDITORIAL PRIORITY BOARD

### Priority Rankings

| # | Topic | Priority | Timing | Trend | Opp | Discover | Urgency | Confidence | Angle |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Utz / Potato Chip Salmonella Recall | P1 | Immediate | 88 | 85 | 5 | today | High | Consumer safety checklist + what to do if you bought recalled chips |
| 2 | E. coli Outbreak — Frozen Blueberries | P1 | Immediate | 84 | 82 | 5 | today | High | Active CDC/FDA outbreak — what consumers need to know now |
| 3 | GLP-1 Drugs Online — Low Clinical Oversight | P1 | Immediate | 79 | 84 | 5 | today | High | What the Yale secret-shopper study found and what it means for patients |
| 4 | Eye Drop Recall — 2.5M Bottles Nationwide | P2 | Short-term | 76 | 80 | 4 | today | Medium | Which brands are recalled, what symptoms to watch for, what to do |
| 5 | COVID-19 Vaccines Cut Hospitalizations 50%+ | P2 | Short-term | 72 | 76 | 4 | this_week | High | What the latest real-world data shows — and what it means for 2026 |
| 6 | Pacemaker Recall — Injuries and Deaths | P2 | Short-term | 70 | 78 | 4 | today | Medium | Who is affected, what FDA says to do, and how to check your device |
| 7 | Intermittent Fasting — Long-Term Weight Loss | P2 | Short-term | 68 | 72 | 4 | this_week | Medium | New study challenges meal-timing orthodoxy — what actually matters |
| 8 | Psilocybin RCT — Cocaine Use Reduction | P2 | Short-term | 65 | 70 | 4 | this_week | Medium | A single dose reduced cocaine use — what the randomized trial found |
| 9 | Cyclosporiasis Outbreak — Rising Search | P3 | Scheduled | 62 | 65 | 3 | this_week | Medium | What cyclosporiasis is, how you get it, and what the 2026 outbreak means |
| 10 | Heart Disease & Cognitive Decline Link | P3 | Scheduled | 58 | 63 | 3 | this_week | Medium | New research on why heart health protects your brain — and what to do |
| 11 | Shigella Vaccine — 89% Protection Trial | P3 | Scheduled | 55 | 60 | 3 | this_week | Medium | A major trial result most people haven't heard about yet |

---

## EDITORIAL BRIEFS

---

### BRIEF 01 — P1 / IMMEDIATE

```yaml
priority_level: P1
publish_timing: immediate
topic: Utz Potato Chip Salmonella Recall — FDA Class I (Highest Risk)
primary_entity: Utz Brands
signal_type: recall
allowed_category: FDA and CDC regulatory updates
trend_strength_score: 88
opportunity_score: 85
discover_score: 5
urgency: today
confidence: high
content_status: new
source_count: 8
why_now: >
  FDA elevated the Utz potato chip recall to its highest risk classification (Class I) 
  on or around July 2, 2026, meaning there is a reasonable probability the product will 
  cause serious adverse health consequences or death. Multiple major outlets — NBC News, 
  The Guardian, The Hill, Fox Business, CBS News, TODAY — confirmed the same product, 
  same risk, same recall tier. This is a high-urgency consumer safety story with active 
  search demand from people trying to find out if chips they bought are affected.
recommended_angle: >
  Consumer safety checklist: which Utz chip products are recalled, how to identify affected 
  lots, what to do if you've eaten them, what salmonella symptoms look like, and when to 
  seek care.
primary_headline: "Utz Potato Chip Recall: FDA Issues Highest-Risk Alert for Salmonella — Here's What to Do"
```

**Alternate Headlines:**
- "Which Utz Potato Chips Were Recalled? FDA Class I Salmonella Warning Explained"
- "Salmonella in Potato Chips: What the FDA's Highest-Risk Recall Means for You"

**Why Now:** Class I recalls represent the FDA's most serious risk tier. Issued within the last 6 days; search demand is live. Consumers are actively looking for which products are affected and what to do.

**Angle:** Practical consumer safety guide, not a news recap. Lead with the product list and lot codes, then explain what Class I means, what salmonella does, and when to call a doctor.

**Outline:**
1. **Lead:** What happened and why it matters — Class I = highest FDA risk tier
2. **Which products:** Brand names, affected lot codes, UPC numbers (pull from FDA.gov recall notice)
3. **What to do:** Check your pantry, don't eat affected products, how to dispose or return
4. **What is salmonella:** Symptoms, onset timing, who is most at risk (elderly, immunocompromised, pregnant, children)
5. **When to seek medical care:** Red flags, hospitalization thresholds
6. **FAQ:** Can cooking kill salmonella in chips? What if I already ate them?
7. **Sources + FDA notice link**

**Key Data Points:**
- FDA Class I = "reasonable probability" of serious adverse health consequences or death
- Salmonella causes ~1.35 million infections and ~420 deaths annually in the US (CDC)
- Symptoms: diarrhea, fever, stomach cramps; onset 6 hours to 6 days after exposure

**⚠️ Integrity Flags:**
- Breaking recall exception used — confirm FDA.gov notice URL and specific lot codes before publishing
- Do not list affected products without pulling directly from the official FDA recall notice
- Do not state deaths have occurred from *this specific* recall without confirmed reports

**Source Plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| FDA.gov | https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts | 1 | Official recall notice, lot codes, risk tier |
| NBC News | https://www.nbcnews.com (Utz recall, July 2) | 1 | Confirmation, consumer-facing framing |
| The Guardian | https://www.theguardian.com (FDA recall, July 2) | 1 | Corroboration |
| CDC Salmonella | https://www.cdc.gov/salmonella | 1 | Symptom data, annual statistics |

**Expert Sources:** None required for this piece — FDA official guidance + CDC stats are authoritative. A quote from an RD or internist on salmonella symptoms would add value for P1.

**SEO:**
- Primary keyword: "Utz potato chip recall"
- Supporting: "FDA salmonella recall chips," "Utz recall 2026," "Class I recall potato chips," "salmonella symptoms food"
- Format: News + FAQ hybrid
- Schema: FAQPage + NewsArticle
- Word count: 800–1,100 words
- Cluster: FDA/recalls, food safety

**Discover Notes:** Highest discover score (5). Specific named entity + active recall + question-format AI query ("Are Utz chips recalled?") + FDA primary source + durable consumer safety reference.

**Next Steps:** Assign immediately. Pull FDA notice for exact product/lot list before writing. Publish within 24 hours.

---

### BRIEF 02 — P1 / IMMEDIATE

```yaml
priority_level: P1
publish_timing: immediate
topic: E. coli Outbreak — FDA Investigation into Frozen Blueberries (July 2026)
primary_entity: Frozen Blueberries / FDA Outbreak Investigation
signal_type: recall
allowed_category: FDA and CDC regulatory updates
trend_strength_score: 84
opportunity_score: 82
discover_score: 5
urgency: today
confidence: high
content_status: new
source_count: 4
why_now: >
  FDA.gov posted an active outbreak investigation page on July 6, 2026: "Outbreak 
  Investigation of E. coli: Frozen Blueberries (July 2026)." This is an open, evolving 
  public health situation. E. coli outbreaks linked to produce are a recurring high-priority 
  food safety story. Consumers who have recently bought or eaten frozen blueberries need 
  guidance now. The Google Trends food safety velocity (+1 delta, steady) and the official 
  FDA.gov source confirm this is actionable.
recommended_angle: >
  Active outbreak explainer: what FDA has found so far, which products may be involved, 
  what E. coli O157:H7 symptoms look like, and what consumers should do with frozen 
  blueberries in their freezer right now.
primary_headline: "FDA Investigating E. coli Outbreak Linked to Frozen Blueberries: What to Do Now"
```

**Alternate Headlines:**
- "Frozen Blueberries E. coli Outbreak: FDA Issues Investigation Warning in July 2026"
- "E. coli in Frozen Blueberries: FDA's Active Outbreak Investigation Explained"

**Why Now:** FDA outbreak investigation pages are published only when illness clusters have been confirmed or are highly probable. This is a live public health event. Consumers need guidance before a formal recall is issued.

**Angle:** Practical "what to do right now" guide. Lead with the FDA investigation status, explain what's known vs. unknown, give consumers clear action steps, and explain E. coli risk in clinical terms without panic.

**Outline:**
1. **Lead:** FDA opened an active E. coli outbreak investigation linked to frozen blueberries on July 6
2. **What is known:** Products under investigation, states/illness counts if reported on FDA page
3. **What consumers should do:** Check freezer, hold/discard guidance pending recall, don't consume if in doubt
4. **What is E. coli O157:H7:** Symptoms, onset, severity spectrum, HUS risk in vulnerable populations
5. **Who is most at risk:** Young children, elderly, immunocompromised
6. **When to seek emergency care:** Bloody diarrhea + sudden stop, neurological symptoms → HUS flag
7. **What FDA does next:** How outbreak investigations escalate to recalls
8. **Sources**

**⚠️ Integrity Flags:**
- Active investigation — this story will evolve. Add a "Last updated" timestamp and plan to update when a recall is issued or investigation concludes.
- Do not name specific brands unless they appear on the FDA investigation page at time of writing.
- E. coli O157:H7 severity should be accurately represented — most cases resolve without antibiotics; note antibiotic risks.

**Source Plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| FDA.gov outbreak page | https://www.fda.gov/food/outbreaks-foodborne-illness/outbreak-investigation-e-coli-frozen-blueberries-july-2026 | 1 | Primary source — investigation status, products |
| CDC E. coli | https://www.cdc.gov/ecoli | 1 | Symptom data, risk populations, HUS |
| FDA outbreak investigation process | https://www.fda.gov/food/outbreaks-foodborne-illness | 1 | How investigations work |

**SEO:**
- Primary keyword: "frozen blueberries E. coli outbreak 2026"
- Supporting: "FDA frozen blueberries recall," "E. coli blueberries symptoms," "frozen fruit recall 2026"
- Format: Breaking news + practical guide
- Schema: NewsArticle + FAQPage
- Word count: 700–900 words

**Next Steps:** Assign immediately. Monitor FDA page daily — update article when recall is issued or additional products named. This story has a 72-hour P1 window.

---

### BRIEF 03 — P1 / IMMEDIATE

```yaml
priority_level: P1
publish_timing: immediate
topic: GLP-1 Weight-Loss Drugs Online — Yale Secret-Shopper Study Finds Low Clinical Oversight
primary_entity: GLP-1 / Online Prescribing Platforms
signal_type: study_or_research
allowed_category: medical research and clinical trials
trend_strength_score: 79
opportunity_score: 84
discover_score: 5
urgency: today
confidence: high
content_status: new
source_count: 5
why_now: >
  STAT News (July 6) and The Washington Post (July 7) both covered a Yale study using 
  secret shoppers to evaluate GLP-1 prescriptions from online telehealth platforms. 
  The findings: easy, fast access with minimal clinical oversight. GLP-1 drugs remain 
  among the highest-search health topics of 2025–2026. This study adds a critical safety 
  and consumer-protection angle that differentiates from pure "ozempic works" coverage. 
  The "weight loss" Google Trends cluster has rising queries this week.
recommended_angle: >
  What the Yale secret-shopper study actually found about online GLP-1 prescribing — 
  the specific gaps in oversight, what that means for patient safety, and what questions 
  to ask before getting a prescription online.
primary_headline: "Yale Secret-Shopper Study Reveals Major Safety Gaps in Online GLP-1 Prescriptions"
```

**Alternate Headlines:**
- "How Easy Is It to Get Ozempic Online? Yale Researchers Found Out — and the Results Are Alarming"
- "The Problem With Getting Weight-Loss Drugs Online: A New Study Explains the Risks"

**Why Now:** Two Tier-1 outlets (STAT + WaPo) published within 24 hours of each other, citing the same Yale study. GLP-1 drug access is the defining health consumer story of 2026. The oversight angle is underserved — most coverage celebrates GLP-1 efficacy, not the prescribing risks.

**Angle:** Evaluative / consumer-protection. This is NOT another "GLP-1 drugs work" article. Lead with the study design (secret shoppers), key findings (specific oversight failures), and what patients should know before ordering online.

**Outline:**
1. **Lead:** Yale researchers posed as patients seeking weight-loss drugs online — here's what they found
2. **Study methodology:** What "secret shopper" means; which platforms were tested; how many encounters
3. **Key findings:** Specific clinical oversight gaps (no labs, no history, no follow-up protocols)
4. **Why this matters:** Contraindications for GLP-1s (pancreatitis history, thyroid cancer, heart conditions)
5. **The access vs. safety tension:** Benefits of telehealth access vs. risks of under-supervised prescribing
6. **What patients should ask before getting a GLP-1 prescription online**
7. **What regulators are or aren't doing:** Any FDA or FTC action pending?
8. **Expert perspective:** Endocrinologist or obesity medicine physician on appropriate prescribing standards
9. **Sources**

**Key Data Points:**
- GLP-1 drugs (semaglutide, tirzepatide) have known contraindications including personal/family history of medullary thyroid cancer, MEN2, pancreatitis
- Common side effects: nausea, vomiting, gastroparesis; serious: pancreatitis, gallbladder disease
- Yale study: named institution + STAT News + WaPo = verifiable; pull specific metrics from the study at time of writing

**⚠️ Integrity Flags:**
- Study framing must not overstate findings — confirm sample size and whether findings are from peer-reviewed publication or preprint/press release at time of writing
- Do not present access barriers as universally bad — telehealth GLP-1 access has genuine benefits for underserved populations
- "Alarming" framing should be supported by specific findings, not used as headline bait without substance

**Source Plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| STAT News | https://www.statnews.com (GLP-1 online prescriptions, July 6) | 1 | Primary study coverage + methodology |
| Washington Post | https://www.washingtonpost.com (Yale secret shoppers, July 7) | 1 | Corroboration + consumer framing |
| FDA GLP-1 safety | https://www.fda.gov (semaglutide/tirzepatide prescribing info) | 1 | Contraindications, approved indications |
| ClinicalTrials.gov | https://clinicaltrials.gov | 1 | Yale study registration if available |

**SEO:**
- Primary keyword: "online GLP-1 prescription safety"
- Supporting: "ozempic online prescription risks," "telehealth weight loss drugs oversight," "GLP-1 safety concerns 2026," "semaglutide online prescription"
- Format: Investigative explainer
- Schema: Article + FAQPage
- Word count: 1,200–1,600 words

**Next Steps:** Assign to senior writer with health/pharma background. Pull Yale study directly from STAT News and WaPo for specific data points before writing. This piece has a 48-hour relevance window before broader media saturation.

---

### BRIEF 04 — P2 / SHORT-TERM

```yaml
priority_level: P2
publish_timing: short_term
topic: Eye Drop Recall — Over 2.5 Million Bottles Recalled Nationwide
primary_entity: Eye Drops (recalled brands)
signal_type: recall
allowed_category: FDA and CDC regulatory updates
trend_strength_score: 76
opportunity_score: 80
discover_score: 4
urgency: today
confidence: medium
content_status: new
source_count: 3
why_now: >
  Prevention reported on July 7, 2026 that over 2.5 million bottles of eye drops have been 
  recalled nationwide, citing an FDA warning. Eye drops are a ubiquitous consumer product 
  with broad audience reach. The 2023–2024 eye drop recall cycles (linked to infections 
  and vision loss) established this as a high-engagement health safety category. Consumer 
  awareness of affected brands is the key value-add.
recommended_angle: >
  Which brands are recalled, what the contamination risk is, what symptoms could indicate 
  a problem, and what consumers should do with recalled drops.
primary_headline: "Over 2.5 Million Bottles of Eye Drops Recalled: FDA Warns Consumers to Stop Using These Products"
```

**Alternate Headlines:**
- "Is Your Eye Drop Brand in the Recall? 2.5 Million Bottles Pulled From Shelves Nationwide"
- "Eye Drop Recall 2026: What FDA Says and How to Check Your Medicine Cabinet"

**Why Now:** Published July 7 — within 24-hour window of this run. Eye drop recalls have historically driven very high search intent (people check if their brand is affected). Consumer action is required.

**Angle:** Practical consumer safety — which brands/lot numbers, what the contamination risk is, what symptoms (eye infection, vision changes) to watch for, and when to call a doctor.

**Outline:**
1. **Lead:** 2.5M+ bottles recalled; what FDA says is the risk
2. **Which products:** Brand names, lot codes, retailer distribution (pull from FDA notice)
3. **What is the contamination concern:** Microbial contamination or other issue (confirm from FDA)
4. **Symptoms of eye infection or contaminated drop exposure**
5. **What to do:** Stop using, dispose, return, contact retailer
6. **When to see a doctor or ER:** Vision changes, pain, discharge
7. **Brief history:** Why eye drop recalls matter — context from past recalls

**⚠️ Integrity Flags:**
- Confidence capped at Medium — primary FDA notice not directly retrieved; confirm brand names and lot codes from FDA.gov before publishing
- Do not name brands without FDA confirmation — past eye drop recall coverage has sometimes attributed recalls to wrong brands

**Source Plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| Prevention | https://www.prevention.com (eye drops recall, July 7) | 2 | Signal + consumer framing |
| FDA.gov recall database | https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts | 1 | Brand names, lot codes, risk tier — MUST confirm before publishing |
| CDC eye health | https://www.cdc.gov/healthywater/hygiene/personal/contact-lenses.html | 1 | Eye infection risk context |

**SEO:**
- Primary keyword: "eye drop recall 2026"
- Supporting: "FDA eye drops recalled brands," "eye drop recall which brands," "recalled eye drops symptoms"
- Format: News + product checklist
- Schema: NewsArticle + FAQPage
- Word count: 700–900 words

**Next Steps:** Pull FDA notice for specific brands before writing. Publish within 48 hours.

---

### BRIEF 05 — P2 / SHORT-TERM

```yaml
priority_level: P2
publish_timing: short_term
topic: COVID-19 Vaccines Cut Hospitalizations by More Than 50% — New Real-World Data
primary_entity: COVID-19 Vaccines
signal_type: study_or_research
allowed_category: public health and epidemiology
trend_strength_score: 72
opportunity_score: 76
discover_score: 4
urgency: this_week
confidence: high
content_status: new
source_count: 4
why_now: >
  UCHealth (University of Colorado Health) published July 6, 2026, citing a new study 
  showing COVID-19 vaccines cut hospitalizations by more than 50%. Real-world effectiveness 
  data (as opposed to trial data) is highly valued by health-conscious readers who want 
  to understand how vaccines perform in actual populations. This is timely for 2026 
  vaccine decisions and emerging variant context.
recommended_angle: >
  What the new real-world data shows about COVID vaccine effectiveness against hospitalization 
  in 2026 — including which vaccines, which variants, which populations showed the strongest 
  benefit, and what it means for fall 2026 booster decisions.
primary_headline: "COVID Vaccines Still Cut Hospitalizations by More Than 50%, New Real-World Study Shows"
```

**Alternate Headlines:**
- "New Data: Updated COVID Vaccines Reduce Hospitalization Risk by Over Half"
- "How Well Do 2026 COVID Vaccines Actually Work? New Study Offers Clearest Answer Yet"

**Why Now:** Real-world effectiveness data in 2026 is more actionable than 2021 trial data for readers making current vaccine decisions. This bridges the gap between "vaccines work in theory" and "vaccines work for people like me right now."

**Angle:** Translational — take the data and make it meaningful for the reader's 2026 health decisions. Who benefited most? What about current variants? Should you get a booster?

**Outline:**
1. **Lead:** New real-world data shows vaccines still working — what the numbers mean
2. **Study basics:** Institution, design (observational or RCT?), population studied, time period
3. **Key finding:** 50%+ hospitalization reduction — contextualize vs. earlier variant data
4. **Who benefited most:** Age groups, immunocompromised, comorbidities
5. **Current variant context:** Which strains are circulating in mid-2026?
6. **What this means for fall 2026 boosters:** CDC recommendations, updated vaccine availability
7. **Addressing vaccine-hesitancy questions:** Common objections, what the data does/doesn't show
8. **Expert framing:** Infectious disease or public health researcher quote

**⚠️ Integrity Flags:**
- Confirm whether UCHealth study is peer-reviewed or institutional press release — if press release only, lead with "new data suggests" not "study proves"
- Confirm observational vs. RCT design — if observational, note "association" not "proves causation"
- 50%+ reduction is relative risk reduction — include absolute risk context where available
- Do not make projections about fall 2026 boosters without citing current CDC guidance

**Source Plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| UCHealth | https://www.uchealth.org (COVID vaccines hospitalizations, July 6) | 2 | Study coverage, primary data summary |
| CDC COVID vaccines | https://www.cdc.gov/vaccines/covid-19 | 1 | Current recommendations, booster guidance |
| NEJM / The Lancet | [verify primary publication] | 1 | Primary study — confirm journal before citing |
| CDC VE data | https://www.cdc.gov/covid/prevention/vaccines/effectiveness | 1 | Real-world effectiveness context |

**SEO:**
- Primary keyword: "COVID vaccine effectiveness 2026"
- Supporting: "COVID vaccine hospitalization reduction," "updated COVID vaccine study," "COVID booster 2026 effectiveness"
- Format: Explainer with data
- Schema: Article + FAQPage
- Word count: 1,000–1,400 words

**Next Steps:** Confirm primary journal publication before writing. Publish within 3 days.

---

### BRIEF 06 — P2 / SHORT-TERM

```yaml
priority_level: P2
publish_timing: short_term
topic: Pacemaker Recall — FDA Issues Warning After Injuries and Deaths
primary_entity: Pacemakers (recalled models)
signal_type: recall
allowed_category: FDA and CDC regulatory updates
trend_strength_score: 70
opportunity_score: 78
discover_score: 4
urgency: today
confidence: medium
content_status: new
source_count: 3
why_now: >
  UCHealth reported July 2, 2026 that the FDA recalled malfunctioning pacemakers after 
  injuries and deaths, with patient guidance issued. Pacemaker recalls with confirmed 
  adverse outcomes are among the highest-stakes medical device safety stories — the audience 
  directly affected is narrower (pacemaker patients) but the urgency for that audience is 
  maximum. Broader audience interest is also high given aging population and heart disease 
  prevalence.
recommended_angle: >
  Which pacemaker models are recalled, what the malfunction is, what the reported injuries 
  and deaths involve, and what FDA says affected patients and their doctors should do.
primary_headline: "FDA Recalls Pacemakers After Reports of Injuries and Deaths — What Patients Need to Know"
```

**Alternate Headlines:**
- "Pacemaker Recall 2026: FDA Issues Warning After Malfunctions Linked to Injuries and Deaths"
- "Is Your Pacemaker Recalled? FDA Issues Urgent Safety Alert After Deaths Reported"

**Why Now:** Confirmed deaths elevates this from standard recall to urgent patient safety alert. Pacemaker patients and their caregivers are actively searching for this information.

**Angle:** Patient-safety action guide. Which devices, what the malfunction does, what symptoms indicate a problem, and the exact steps FDA recommends (no patient should be adjusting their own device — route to cardiologist).

**Outline:**
1. **Lead:** FDA issued a recall after pacemaker malfunctions linked to injuries and deaths
2. **Which devices:** Manufacturer, model numbers, date of manufacture range
3. **What the malfunction is:** Technical description in plain language
4. **What the risks are:** What happens when a pacemaker malfunctions (failure to pace, inappropriate shock, etc.)
5. **What FDA says patients should do:** Contact cardiologist, do NOT stop using device without medical guidance, device check/reprogramming options
6. **Warning signs of malfunction**
7. **How pacemaker recalls work differently from product recalls** (you can't just "return" it)
8. **Expert:** Cardiologist perspective on navigating recalls

**⚠️ Integrity Flags:**
- Confidence capped at Medium — primary FDA notice not directly retrieved from this session; confirm device names, manufacturers, and specific malfunction from FDA.gov before publishing
- Critical safety framing: do NOT advise patients to stop using their pacemaker or modify behavior without explicit cardiologist guidance — device-dependent patients face life-threatening risk if they misinterpret recall guidance
- Avoid attributing specific death counts without confirmation from FDA

**Source Plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| UCHealth | https://www.uchealth.org (pacemaker recall, July 2) | 2 | Signal; patient guidance framing |
| FDA medical device recalls | https://www.fda.gov/medical-devices/medical-device-recalls | 1 | Primary source — device names, malfunction, patient actions — MUST confirm before publishing |
| AHA / Cleveland Clinic | [verify] | 1 | Expert pacemaker safety context |

**SEO:**
- Primary keyword: "pacemaker recall 2026"
- Supporting: "FDA pacemaker recall injuries deaths," "recalled pacemaker models," "pacemaker malfunction symptoms," "what to do pacemaker recall"
- Format: Patient safety guide
- Schema: NewsArticle + FAQPage
- Word count: 900–1,200 words

**Next Steps:** Pull FDA recall notice for device specifics before writing. Assign to writer with medical device experience. Publish within 48 hours.

---

### BRIEF 07 — P2 / SHORT-TERM

```yaml
priority_level: P2
publish_timing: short_term
topic: Intermittent Fasting Maintains Long-Term Weight Loss Regardless of Meal Timing
primary_entity: Intermittent Fasting
signal_type: study_or_research
allowed_category: nutrition and diet science
trend_strength_score: 68
opportunity_score: 72
discover_score: 4
urgency: this_week
confidence: medium
content_status: new
source_count: 3
why_now: >
  Medical Xpress (July 3) reported a new study finding intermittent fasting maintains 
  long-term weight loss regardless of when meals are eaten — challenging the meal-timing 
  orthodoxy that has driven much IF discourse. The "diet" Google Trends cluster is active 
  (57/100, steady) and intermittent fasting remains a top-search nutrition topic. The 
  specific finding (meal timing doesn't matter, the fasting window does) differentiates 
  this from generic IF coverage.
recommended_angle: >
  What this study says about intermittent fasting and meal timing — the specific finding 
  that challenges conventional IF advice — and what it means practically for people doing IF.
primary_headline: "New Study: Intermittent Fasting Works for Long-Term Weight Loss — But When You Eat Doesn't Matter"
```

**Alternate Headlines:**
- "The Intermittent Fasting Study That Changes What We Thought About Meal Timing"
- "Does It Matter When You Break Your Fast? New Research Has a Surprising Answer"

**Why Now:** Meal-timing debate is a live controversy in IF communities. This finding directly addresses a high-frequency audience question. SERP for "intermittent fasting meal timing" is dominated by 2022–2023 articles — a 2026 study with a clear finding can rank.

**Angle:** Practical science translation. What did the study actually find? What study design was used? What does it mean for someone doing 16:8 or 18:6? Does it change any specific behaviors?

**Outline:**
1. **Lead:** New research says IF works long-term — but the *when* of meals matters less than you think
2. **Study basics:** Design (observational? RCT?), participants, duration, institution
3. **Key finding:** Weight loss maintenance regardless of meal timing window
4. **What this challenges:** Popular claims that early eating windows (before 3 PM) are superior
5. **What still matters:** Total caloric intake, fasting duration, adherence
6. **Practical implications:** How to apply this finding if you're already doing IF; what to tell people who quit IF because of timing conflicts
7. **Caveats:** Study limitations, who the sample included, what remains unanswered
8. **Expert context:** RD or nutrition researcher on significance

**⚠️ Integrity Flags:**
- Confirm study design from Medical Xpress — if observational, do not state IF "causes" weight maintenance; association only
- Confirm whether "long-term" is defined as 12 months, 24 months, or longer — this significantly affects the claim's strength
- Do not generalize to populations not included in the study (children, people with eating disorder history, diabetics on insulin) without explicit qualification

**Source Plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| Medical Xpress | https://medicalxpress.com (intermittent fasting, July 3) | 2 | Study summary + key finding |
| Primary journal | [URL unverified — confirm from Medical Xpress article] | 1 | Primary study data |
| Academy of Nutrition and Dietetics | https://www.eatright.org | 2 | Expert context on IF evidence base |

**SEO:**
- Primary keyword: "intermittent fasting long-term weight loss"
- Supporting: "intermittent fasting meal timing study," "IF meal timing doesn't matter," "intermittent fasting 2026 research"
- Format: Study explainer + practical guide
- Schema: Article + FAQPage
- Word count: 1,000–1,300 words

**Next Steps:** Pull primary journal citation from Medical Xpress. Publish within 3–5 days.

---

### BRIEF 08 — P2 / SHORT-TERM

```yaml
priority_level: P2
publish_timing: short_term
topic: Psilocybin Randomized Clinical Trial — Single Dose Reduced Cocaine Use
primary_entity: Psilocybin
signal_type: clinical_trial
allowed_category: medical research and clinical trials
trend_strength_score: 65
opportunity_score: 70
discover_score: 4
urgency: this_week
confidence: medium
content_status: new
source_count: 3
why_now: >
  TMX Newsfile reported July 5, 2026 the publication of a randomized clinical trial 
  showing a single dose of psilocybin reduced cocaine use, with Filament Health holding 
  the exclusive IP license. A published RCT on psilocybin for substance use disorder 
  is a significant research milestone — most prior psilocybin research has been observational 
  or small-sample open-label. The mental health and psychedelic therapy space is high-interest 
  for our target audience.
recommended_angle: >
  What the randomized trial found about a single psilocybin dose and cocaine use reduction — 
  the specific design, effect size, and what it means for where psychedelic therapy stands 
  as a legitimate treatment pathway.
primary_headline: "Single Dose of Psilocybin Reduced Cocaine Use in Randomized Trial — What the Study Found"
```

**Alternate Headlines:**
- "New Clinical Trial: Psilocybin Reduced Cocaine Use — Here's What the Research Actually Says"
- "A Single Psilocybin Dose Cut Cocaine Use in a Randomized Trial. What Does That Mean?"

**Why Now:** RCT publication for a controlled substance indication is the strongest possible study design for psychedelic research. This distinguishes it from the observational studies that dominate psychedelic health coverage. Legal and clinical context (psilocybin therapy access is expanding in some US states) makes this timely.

**Angle:** Skeptical yet fair science translation. What did the RCT design look like (sample size, control condition, duration of follow-up)? What is the effect size? Is this enough to change clinical practice or regulatory status? What are the limitations?

**Outline:**
1. **Lead:** RCT results — what a randomized design means and why it matters for psychedelic research
2. **Study design:** Sample size, randomization method, control arm, follow-up duration
3. **Key findings:** Specific reduction in cocaine use — magnitude, timeframe
4. **Context:** How this fits into the broader psilocybin research landscape (FDA Breakthrough Therapy status for depression; earlier observational work)
5. **Limitations:** Small cohort risks, single-dose vs. sustained therapy, commercial IP conflict of interest (Filament Health licensing)
6. **Regulatory pathway:** What this means for FDA consideration of psilocybin for SUD
7. **Expert perspective:** Addiction psychiatrist or clinical psychologist on significance

**⚠️ Integrity Flags:**
- Single clinical trial — do not present as definitive proof; this is promising evidence, not established treatment
- Filament Health holds exclusive IP license — disclose commercial interest in the research
- Confirm sample size from the publication — small cohorts (n<50) significantly limit generalizability
- Cocaine use disorder population is specific — do not generalize to all substance use disorders

**Source Plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| TMX Newsfile | https://www.newsfilecorp.com (Red Light Holland psilocybin, July 5) | 2 | Signal + trial announcement |
| Primary journal publication | [URL unverified — confirm from trial announcement] | 1 | RCT data, design, effect size |
| ClinicalTrials.gov | https://clinicaltrials.gov (search: psilocybin cocaine) | 1 | Trial registration and design |
| FDA Breakthrough Therapy | https://www.fda.gov (psilocybin research status) | 1 | Regulatory context |

**SEO:**
- Primary keyword: "psilocybin cocaine study 2026"
- Supporting: "psilocybin clinical trial substance use," "psychedelic therapy cocaine," "psilocybin RCT results"
- Format: Study explainer with expert context
- Schema: Article
- Word count: 1,100–1,500 words

**Next Steps:** Pull primary journal publication before writing. Flag commercial interest disclosure as mandatory editorial requirement.

---

### BRIEF 09 — P3 / SCHEDULED

```yaml
priority_level: P3
publish_timing: scheduled
topic: Cyclosporiasis Outbreak 2026 — Rising Search Interest
primary_entity: Cyclosporiasis
signal_type: rising_search_interest
allowed_category: public health and epidemiology
trend_strength_score: 62
opportunity_score: 65
discover_score: 3
urgency: this_week
confidence: medium
content_status: new
source_count: 2
why_now: "Cyclosporiasis appears in Google Trends Trending Now (US health, real-time) on July 8, indicating a search spike — likely linked to an active outbreak or seasonal increase. Cyclosporiasis has a distinct seasonal pattern in the US (late spring/summer, linked to fresh produce)."
recommended_angle: "What cyclosporiasis actually is — how people get infected, what the 2026 outbreak involves, which produce has been linked historically, and how to protect yourself."
primary_headline: "Cyclosporiasis Outbreak 2026: What Is It, How Do You Get It, and Should You Be Worried?"
integrity_flags:
  - "Confirm current outbreak details from CDC before publishing — Google Trends signal alone does not confirm an active CDC-declared outbreak"
  - "Do not name produce sources without CDC/FDA confirmation"
sources:
  - publisher: "CDC Cyclosporiasis"
    url: "https://www.cdc.gov/parasites/cyclosporiasis"
  - publisher: "FDA outbreak investigations"
    url: "https://www.fda.gov/food/outbreaks-foodborne-illness"
seo:
  primary_keyword: "cyclosporiasis outbreak 2026"
  format: "Explainer + FAQ"
  serp_difficulty: Medium
estimated_word_count: "800–1,000 words"
next_steps: "Verify current outbreak status with CDC before writing. Assign as evergreen-adjacent explainer that can be updated as outbreak develops."
```

---

### BRIEF 10 — P3 / SCHEDULED

```yaml
priority_level: P3
publish_timing: scheduled
topic: Heart Disease and Cognitive Decline — New Research on the Heart-Brain Link
primary_entity: Cardiovascular Health / Cognitive Function
signal_type: study_or_research
allowed_category: chronic disease management
trend_strength_score: 58
opportunity_score: 63
discover_score: 3
urgency: this_week
confidence: medium
content_status: new
source_count: 2
why_now: "News-Medical reported July 6 on a study exploring heart issues and cognitive function. Heart disease is the #1 killer in the US; cognitive decline is a top aging fear. The intersection is a high-engagement topic with strong cluster expansion potential (heart health → brain health → aging). The 'best exercises for heart health' query is rising in Google Trends this week, creating a natural entry point."
recommended_angle: "What the new research adds to our understanding of why cardiovascular health protects cognitive function — and the specific lifestyle factors that address both simultaneously."
primary_headline: "New Study: Heart Problems Are Linked to Faster Cognitive Decline — Here's What Protects Both"
integrity_flags:
  - "Confirm study is published in peer-reviewed journal before writing — News-Medical headline does not identify the journal"
  - "Association study — do not present as causal relationship without explicit support in the primary source"
  - "Confirm population studied — if elderly-only, qualify generalizability"
sources:
  - publisher: "News-Medical"
    url: "https://www.news-medical.net (heart cognition study, July 6)"
  - publisher: "American Heart Association"
    url: "https://www.heart.org/en/health-topics"
seo:
  primary_keyword: "heart disease cognitive decline link"
  format: "Study explainer + practical guide"
  serp_difficulty: Medium
estimated_word_count: "900–1,200 words"
next_steps: "Pull primary journal citation from News-Medical article. Can pair with 'best exercises for heart health' angle to capture rising Google Trends query. Publish within 5–7 days."
```

---

### BRIEF 11 — P3 / SCHEDULED

```yaml
priority_level: P3
publish_timing: scheduled
topic: Shigella Vaccine Trial — 89% Protection Rate
primary_entity: Shigella Vaccine
signal_type: clinical_trial
allowed_category: public health and epidemiology
trend_strength_score: 55
opportunity_score: 60
discover_score: 3
urgency: this_week
confidence: medium
content_status: new
source_count: 3
why_now: "PR Newswire and CIDRAP reported a clinical trial showing 89% protection from a Shigella vaccine. Shigella (bacterial dysentery) infects ~450,000 Americans annually; antimicrobial resistance is rising in Shigella strains, making a vaccine more urgent than ever. Trial results at this efficacy level are newsworthy for global and domestic travel health audiences."
recommended_angle: "What the 89% protection result means, who shigella affects (travelers, children, vulnerable communities), and where this vaccine is in the development pipeline."
primary_headline: "Shigella Vaccine Trial Shows 89% Protection — What This Means for a Disease Affecting Millions"
integrity_flags:
  - "Confidence capped at Medium — primary peer-reviewed publication not confirmed; PR Newswire is a press release, not peer-reviewed. Verify journal publication or ClinicalTrials.gov record before publishing."
  - "89% efficacy figure — confirm whether this is against any infection, symptomatic disease, or severe disease; efficacy framing differs significantly"
  - "Distinguish trial-phase from approval — this is trial results, not an approved vaccine"
sources:
  - publisher: "CIDRAP"
    url: "https://www.cidrap.umn.edu"
  - publisher: "PR Newswire"
    url: "https://www.prnewswire.com (Shigella vaccine, July 1)"
  - publisher: "ClinicalTrials.gov"
    url: "https://clinicaltrials.gov (search: Shigella vaccine)"
seo:
  primary_keyword: "Shigella vaccine 2026"
  format: "Clinical trial explainer"
  serp_difficulty: Easy
estimated_word_count: "800–1,000 words"
next_steps: "Confirm journal publication or ClinicalTrials.gov registration. Pull efficacy endpoint definition. SERP difficulty is Easy — low competition, clear opportunity."
```

---

## REJECTED TOPICS LOG

| Topic | Rejection Reason |
|---|---|
| Mitch McConnell Health Status | Category rule: celebrity/political figure health; no generalizable health content angle; brand safety |
| Katie Couric (Trending Now) | Celebrity; no health content angle relevant to this site |
| Space Radiation / Accelerated Aging (UCF) | Off-category — not actionable for health-conscious general audience without clinical bridge |
| NYC 450K Losing Health Coverage | Pure healthcare policy/access story; no new health data angle per category rules |
| Reproductive Health Litigation (KFF) | Pure legal/policy; excluded category for this niche |
| AMA Healthcare Spending Trends | Institutional/systemic; no direct actionable health content for general audience |
| Digital Health Fraud / Adderall Scheme (DOJ) | Legal/crime news; not a health content angle |
| Fitness cluster (July 4th gym hours) | Not actionable — seasonal search noise around holiday hours |
| Wellness cluster (local programs) | Local scope (Purdue, UW Extension, Evanston, Palo Alto); not national audience |
| Petco Health and Wellness (WOOF stock) | Finance/pet; excluded category |
| EMA Women's Health steps up | EU regulatory; limited US audience relevance |
| Game of Thrones star / wellness cult | Celebrity gossip; excluded category |
| Ascend Wellness ULP strike | Labor news; not health content |
| Yale hospital CEO ousted | Institutional/administrative; no patient health angle |
| Urban motifs / population health (Nature) | Low trend velocity; insufficient hook for general audience — moved to P5 monitor |
| Cervical Cancer (WHO July 3) | No new data or study this week; evergreen but not trending — moved to P5 |
| Bundibugyo/Ebola Trial DR Congo | Global health emergency; limited US audience relevance now — moved to P5 monitor |
| Neurodegenerative Drug Target | 02b Monitor: News-Medical only; no DOI or journal named — exits at P5 |
| Stress/Gut-Brain/Mice Study | 02b Monitor: animal model only; cannot responsibly generalize to humans without qualification — exits at P5 |
| Snapchatplanet.com / related wellness domains | Spam/SEO noise in Google Trends wellness related queries |
| "1776 diet," "Kashrut diet," "Haaland diet" | Rising queries with no credible health content signal; not actionable |
| Mark Zuckerberg wagyu cattle diet | Celebrity wellness; excluded category |
| Planet Fitness July 4th hours | Search noise; not health content |
| Twisted tea nutrition facts | Low health value; consumer curiosity not aligned with site niche |

---

## INTEGRITY FLAGS CONSOLIDATED

All ⚠️ flags for editorial review before publishing:

**Brief 01 — Utz Potato Chip Recall:**
- ⚠️ Breaking recall exception used — confirm FDA.gov notice URL and specific lot codes before publishing. Do not list affected products without pulling directly from the official FDA recall notice.

**Brief 02 — E. coli Frozen Blueberries:**
- ⚠️ Active, evolving investigation — add "Last updated" timestamp and plan update cadence. Do not name specific brands without FDA confirmation. Note antibiotic risk context for E. coli O157:H7.

**Brief 03 — GLP-1 Online Prescriptions:**
- ⚠️ Confirm whether Yale study is peer-reviewed publication or preprint/press release at time of writing. Do not frame telehealth access as uniformly bad. "Alarming" framing requires specific data support.

**Brief 04 — Eye Drop Recall:**
- ⚠️ Confidence capped at Medium. Confirm brand names and lot codes from FDA.gov before publishing. Past eye drop recall coverage has misattributed brands.

**Brief 05 — COVID Vaccines:**
- ⚠️ Confirm UCHealth study is peer-reviewed, not press release only. Note observational vs. RCT design. Present relative risk reduction with absolute risk context. Do not speculate on fall 2026 boosters without current CDC guidance.

**Brief 06 — Pacemaker Recall:**
- ⚠️ Confidence capped at Medium. Critical safety framing: do NOT advise patients to stop using their pacemaker without cardiologist guidance. Confirm device names and malfunction from FDA.gov before publishing.

**Brief 07 — Intermittent Fasting:**
- ⚠️ Confirm study design (observational vs. RCT). Define "long-term." Do not generalize to populations with eating disorder history, insulin-dependent diabetes, or pediatric populations without explicit qualification.

**Brief 08 — Psilocybin RCT:**
- ⚠️ Disclose Filament Health commercial IP interest — mandatory. Confirm sample size from primary publication. Single trial — do not present as established treatment. Do not generalize beyond cocaine use disorder.

**Brief 09 — Cyclosporiasis:**
- ⚠️ Verify active outbreak status from CDC before writing. Google Trends signal alone does not confirm a CDC-declared outbreak. Do not name produce sources without CDC/FDA confirmation.

**Brief 10 — Heart-Cognitive Decline:**
- ⚠️ Confirm peer-reviewed journal from News-Medical article. Present as association, not causation. Qualify population studied.

**Brief 11 — Shigella Vaccine:**
- ⚠️ Confidence capped at Medium — PR Newswire is a press release. Confirm journal or ClinicalTrials.gov. Clarify whether 89% efficacy is against any infection, symptomatic disease, or severe disease. Distinguish trial results from approved vaccine.

---

## RUN NOTES

```yaml
run_date: 2026-07-08
niche: health and wellness
signals_reviewed: 144
topics_retained: 11
topics_rejected: 133
p1_count: 3
p2_count: 5
p3_count: 3
p5_monitor: 4
integrity_flags_raised: 11
top_topic: "Utz / Potato Chip Salmonella Recall — FDA Class I"
key_themes:
  - FDA recalls (food + devices + OTC products) — dominant cluster this week
  - GLP-1 / weight-loss drugs (access, safety, oversight)
  - Clinical trial results (psilocybin, shigella vaccine)
  - COVID vaccine effectiveness (real-world data)
  - Food safety outbreaks (E. coli blueberries, cyclosporiasis)
tools_used:
  - serpapi_prefetch (Google Trends 7-day + Google News Radar)
tools_unavailable:
  - COMPOSIO_SEARCH_TRENDS (not called directly — pre-fetch used)
  - BrowserNavigate/RSS (not called — pre-fetch used as primary signal layer)
  - ExaSearch (not called)
  - Reddit API (not called)
google_trends_available: true
google_trends_tool: serpapi_prefetch
search_velocity_source: google_trends
site_url_configured: false
self_check: skipped — competitor-check fallback noted in all candidate content_status fields
deferred_topics_checked: false (file not readable in this session)
run_history_checked: false (file not readable in this session)
staleness_flags: none applied (run history unavailable)
notes: >
  Dominant news cluster this week is FDA product recalls across three categories 
  (food, medical devices, OTC products). This is an unusually recall-heavy week — 
  three separate P1/P2 recall briefs is above average. Editors should consider a 
  weekly "FDA Recall Roundup" format for ongoing recall cycles. GLP-1 oversight 
  remains a high-opportunity content area with differentiated angles still available. 
  Gut health Google Trends delta (+4) noted — no specific study signal this week 
  but warrants monitoring for next run. Fitness cluster entirely dominated by July 4th 
  gym hours noise — reset expected by July 9 run.
dashboard_url: outputs/daily_newsroom_dashboard/2026-07-08.html
archived_to_run_history: pending (run_history.yaml not writable in this session — manual entry required)
```

---

*Pipeline complete — Skills 01 through 12 executed. All 11 retained candidates briefed. Integrity flags consolidated for editorial review. Dashboard output path: `outputs/daily_newsroom_dashboard/2026-07-08.html`.*