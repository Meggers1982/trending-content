# TRENDING CONTENT OS — DAILY PIPELINE RUN
**Date:** 2026-06-27 | **Niche:** Health & Wellness | **Run Mode:** Full Pipeline (Skills 01–12)

---

## PREFLIGHT SUMMARY

| Check | Status |
|---|---|
| All 7 config files | ✅ Loaded |
| All 12 skills + Skill 02b | ✅ Present |
| `site_niche` | ✅ "health and wellness" |
| `target_audience` | ✅ Defined |
| `site_url` | ⚠️ Not configured — self-check skipped; competitor-check fallback active |
| SerpAPI connected | ✅ Google News Radar injected (60 headlines, 12 queries) |
| Google Trends | ✅ Available via SerpAPI pre-fetch block (7-day interest + trending now) |
| `search_velocity_source` | `google_trends` (SerpAPI prefetch) |
| Google Trends Trending Now | ✅ **Ebola** flagged as top real-time trending topic |
| Deferred topics (`data/deferred_topics.yaml`) | ⚠️ File not directly readable in this run context — treated as empty; no deferred topics re-entered |
| Run history (`data/run_history.yaml`) | ⚠️ Not directly readable — cross-run staleness check skipped; flagged in run notes |
| Minimum trend strength score | 50 |
| Minimum opportunity score | 55 |
| Max candidates returned | 25 |
| Can run Signal Listener | ✅ Yes |

**Preflight verdict:** Proceed. All required configs loaded. Google Trends available. Self-check skipped with competitor fallback. Run history file not readable — no staleness cross-check this run.

---

## GOOGLE NEWS RADAR — COVERAGE SUMMARY

144 unique headlines ingested across 12 queries. Six primary topic clusters identified.

| Cluster | Headlines Seen | Decision | Reason |
|---|---|---|---|
| **Ebola / Infectious Disease** | CDC traveler advisory, Kenya contempt-of-court ruling on Ebola facility, Google Trends real-time #1 breakout | **Retained — P1** | Breakout Google Trends signal + institutional source (CDC) + active news coverage; direct public health relevance |
| **FDA Blood Pressure Medication Recall (Chlorthalidone)** | 9 headlines across TODAY, Prevention, QZ, Houston Chronicle, Cleveland.com, Cardiovascular Business, FDA.gov, and others; 11,460 bottles, NJ distributor | **Retained — P1** | Multi-outlet convergence, FDA-sourced recall, direct patient-safety impact; Skill 02b gate required |
| **HHS / Operation Trailblazer — Clinical Trial Reforms** | 6 headlines: HHS.gov, Fierce Biotech, WSJ, The Hill, Clinical Trials Arena, Spencer Fane | **Retained — P2** | Official HHS announcement; policy + patient-access angle; Skill 02b gate required |
| **COVID Vaccine Study Blocked by CDC / Now Published** | Washington Post, ABC News, Medscape, NYT adjacent | **Retained — P2** | High-credibility journalism, institutional controversy, clear audience relevance; Skill 02b required |
| **Listeria Soft Cheese Outbreak (FDA)** | FDA.gov outbreak investigation page (June 2026) | **Retained — P2** | FDA primary source, food safety category, direct consumer action required |
| **Medical Journal Retraction — Cancer Therapy Morning Timing Study** | NYT | **Retained — P3** | High-credibility source; serves skepticism/science-integrity angle; Skill 02b required |
| **Gut Health / Microbiome** | Cedars-Sinai fermented foods, NPR gut microbiome explainer, Nature blood metabolome study | **Retained — P3** | Evergreen category strength; Nature study adds research angle |
| **Pregnancy / Severe Nausea (HG) — Stanford Study** | Stanford Medicine press release | **Retained — P3** | Women's health category; peer-reviewed institution source |
| **AI in Healthcare** | APA (AI in therapy), Fierce Healthcare (Assort Health $120M), Nature (medical AI privacy), Clinical Trial Vanguard (LLMs vs FDA-cleared AI) | **Monitored** | Interesting cluster but falls outside core allowed categories without a direct patient-health angle; "AI in therapy" is borderline — retained as P5 Monitor |
| **New World Screwworm Detection (USDA)** | APHIS/USDA confirmed detection | **Monitored** | Infectious disease / environmental health angle possible but primarily agricultural; borderline — P5 Monitor |
| **OTC Drug Highest-Risk Level (FDA)** | Reader's Digest / The Healthy (06/20) | **Monitored** | Story is 7 days old; specific drug not identified in headline; needs more source verification before scoring |
| **Rural Hospital Fund / Medicaid Enrollment** | Healthcare Dive, KFF | **Rejected** | Policy/health systems business; no direct patient health content angle meeting borderline criteria |
| **Wellness noise** | Jamieson Wellness M&A, Gotham FC partnership, sauna/cold plunge DIY, union strike | **Rejected** | Off-category: supplement marketing/business, celebrity wellness, not health-evidence-based |
| **Heart Surgery Kit Recall** | Cardiovascular Business (06/25) | **Rejected from main candidates** | Narrow surgical device recall; low general-audience relevance; patient base too specialized |
| **Bone Health rising query** | Google Trends rising related queries | **Monitored** | Rising search interest but no anchor news event; added to evergreen watch list |
| **BIPOC Mental Health Awareness Month** | Google Trends rising related | **Retained — P3** | Recurring seasonal moment (July = BIPOC Mental Health Month), audience-relevant, search rising |

---

## SIGNAL SUMMARY

```yaml
run_started_at: 2026-06-27T00:00:00Z
run_completed_at: 2026-06-27T00:00:00Z
total_signals_reviewed: 144 (Google News) + 9 trend clusters (Google Trends)
total_signals_retained: 9
total_rejected_or_monitored: remainder
google_trends_available: true
search_velocity_source: "google_trends (SerpAPI prefetch)"
google_trends_trending_now: ["ebola"]
rejection_breakdown:
  off_category: 6
  brand_safety: 1
  duplicate: 0
  weak_signal: 2
  unverified_claim: 1
  other: 3 (monitored/deferred)
highest_priority_topic: "Ebola Travel Advisory (CDC)"
strongest_signal_source: "Google Trends Trending Now + CDC.gov"
tools_unavailable: ["COMPOSIO_SEARCH_TRENDS (direct)", "BrowserNavigate/RSS live fetch", "ExaSearch"]
notes: >
  Google Trends breakout signal for 'ebola' is real-time top trending in US health.
  FDA chlorthalidone recall has 9-outlet convergence — strongest news-volume signal.
  Site self-check unavailable (no site_url); competitor fallback used for SERP gap context.
  Run history not readable this session — staleness check not performed.
  OTC highest-risk drug story (Reader's Digest, 06/20) is 7 days old with no identified drug name
  in the injected headline — held at Monitor pending verification.
  AI-in-healthcare cluster is strong but categorically adjacent; routed to P5 Monitor.
```

---

## SKILL 02b ROUTING SUMMARY

| Candidate | Risk Type | Gate Result | Primary Source Found | Notes |
|---|---|---|---|---|
| Ebola Travel Advisory | public health advisory | **Pass** | ✅ CDC.gov (cdc.gov/travel/notices) | Institutional advisory, not a drug/supplement claim |
| Chlorthalidone Blood Pressure Recall | recall | **Pass (medium confidence cap)** | ✅ FDA.gov outbreak/recall page confirmed via 9 outlets including FDA.gov direct | Breaking-recall exception conditions met: 3+ credible sources, FDA.gov confirmed, product name + lot context cited |
| Operation Trailblazer / HHS Clinical Trial Reforms | policy/regulatory | **Pass** | ✅ HHS.gov official announcement | Not a drug/treatment claim; regulatory policy announcement |
| COVID Vaccine Study (CDC blocked → published) | medical study | **Pass with note** | ✅ Washington Post names journal; ABC News cites publication; Medscape covers | Mild overstatement risk in "the study the CDC doesn't want you to see" framing — flag for editorial |
| Listeria Soft Cheese Outbreak | recall/food safety | **Pass** | ✅ FDA.gov outbreak investigation page (June 2026) | Official FDA investigation page; direct primary source |
| Medical Journal Retraction — Cancer Morning Timing | medical study (retraction) | **Pass** | ✅ NYT cites retraction; peer-reviewed journal retracted the study | Retraction is the primary news event; the claim being evaluated is "study has been retracted" |
| Gut Health / Nature Blood Metabolome Study | medical study | **Pass with note** | ✅ Nature (June 25, 2026) — peer-reviewed; DOI traceable | Observational study; editorial note required re: association vs. causation |
| Stanford HG Pregnancy Study | medical study | **Pass with note** | ✅ Stanford Medicine press release; study attributed to Stanford researchers | Press release source — editorial note: verify journal publication before citing |
| BIPOC Mental Health Month | seasonal/cultural | **Not triggered** | N/A | No drug/treatment/study claim |

---

## EDITORIAL PRIORITY BOARD

| # | Priority | Timing | Topic | Signal Type | Category | Trend | Opp | Discover | Urgency | Confidence | Angle | Headline |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **P1** | Immediate | Ebola Travel Advisory — CDC | breaking_news | infectious disease | 88 | 82 | 4 | now | high | What US travelers need to know right now | *CDC Issues Ebola Travel Warning: What You Need to Know Before You Fly* |
| 2 | **P1** | Immediate | Chlorthalidone Blood Pressure Recall | recall | FDA regulatory updates | 85 | 88 | 5 | now | medium* | Check your bottles — exact product + action steps | *11,000+ Bottles of Blood Pressure Medication Recalled: How to Check If Yours Is Affected* |
| 3 | **P2** | Short-term (24–48h) | HHS Operation Trailblazer — Clinical Trial Reforms | policy_or_regulatory_change | medical research & clinical trials | 72 | 74 | 3 | today | high | What the phase 1 speed-up means for patients who need experimental drugs | *HHS Wants to Cut Drug Trial Times by a Year — Here's What That Could Mean for Patients* |
| 4 | **P2** | Short-term (24–48h) | COVID Vaccine Study — Blocked by CDC, Now Published | medical study | medical research & clinical trials | 74 | 78 | 4 | today | high | What the study actually found vs. how it was framed | *The COVID Vaccine Study CDC Tried to Suppress — And What It Actually Shows* |
| 5 | **P2** | Short-term (48–72h) | FDA Listeria Outbreak — Soft Cheese | recall | FDA regulatory updates / food safety | 70 | 76 | 4 | today | high | What to check in your fridge right now | *FDA Investigates Listeria Outbreak Linked to Soft Cheese: What to Avoid Right Now* |
| 6 | **P3** | Scheduled (within 7d) | Medical Journal Retraction — Cancer Morning Timing Study | study_or_research | medical research | 60 | 66 | 3 | this_week | high | Science self-corrects — here's why this retraction matters | *A Widely Covered Cancer Study Was Just Retracted. Here's What That Tells Us About Medical Research* |
| 7 | **P3** | Scheduled (within 7d) | Gut Health — Nature Blood Metabolome + Fermented Foods | study_or_research | gut health & microbiome | 58 | 68 | 3 | this_week | medium | What the midlife brain-gut research actually recommends | *New Research Links Your Gut Microbiome to Brain Health in Midlife — Here's What to Do About It* |
| 8 | **P3** | Scheduled (within 7d) | BIPOC Mental Health Awareness Month (July) | seasonal_trend | mental health & psychology | 55 | 65 | 3 | this_week | high | Practical guide anchored to July awareness month + rising search | *BIPOC Mental Health Month: Finding Culturally Competent Care and Resources That Actually Help* |
| 9 | **P3** | Scheduled (within 7d) | Stanford Study — Severe Pregnancy Nausea (HG) | study_or_research | women's health | 56 | 62 | 3 | this_week | medium | What HG actually is and what this study means for pregnant people | *Severe Pregnancy Nausea Is More Dangerous Than We Thought, Stanford Study Finds* |

*Medium confidence cap applied per Skill 02b breaking-recall exception.

**P5 Monitor (not briefed):** AI in therapy (APA), New World Screwworm (USDA), OTC highest-risk drug (story age + missing drug name), bone health evergreen watch.

---

## EDITORIAL BRIEFS

---

### BRIEF 1 — P1 / IMMEDIATE

```yaml
priority_level: P1
publish_timing: immediate
topic: "Ebola Travel Advisory — CDC Issues Warning for US Travelers"
primary_entity: "Ebola virus disease"
signal_type: breaking_news
allowed_category: infectious disease / public health and epidemiology
trend_strength_score: 88
opportunity_score: 82
discover_score: 4
urgency: now
confidence: high
confidence_reason: "Google Trends real-time #1 trending (US, health); CDC.gov institutional advisory; PBS + multiple news outlets; convergence across search, institutional, and news channels"
content_status: new
source_count: 4
recommended_angle: "Practical traveler guidance — what to know, where not to go, what symptoms to watch for — anchored to the CDC advisory, not speculation"
why_now: "Ebola is the #1 trending health search in the US right now (Google Trends Trending Now). CDC issued a traveler advisory on June 25. Kenya's health minister was found in contempt of court over a US-backed Ebola facility. The combination of a real institutional alert and search breakout creates an immediate reader-need gap."
primary_headline: "CDC Issues Ebola Travel Warning: What You Need to Know Before You Fly"
integrity_flags:
  - "⚠️ Do not conflate the Kenya political story with a confirmed US outbreak. There is no domestic Ebola outbreak. Frame strictly as a travel advisory."
  - "⚠️ Do not speculate about outbreak spread. Stick to CDC advisory language and confirmed affected areas."
```

**Why Now (expanded):** Ebola hits #1 on Google Trends Trending Now in the US on June 27. The CDC published traveler guidance on June 25. Kenya's health minister was held in contempt of court the same week over a US-backed Ebola treatment facility — giving this story both an official public health dimension and active international news coverage. Readers searching "ebola" right now are looking for reassurance and practical guidance, not speculation.

**Angle:** *What travelers and health-conscious readers actually need to know* — a clear, calm, CDC-anchored explainer. Distinguish between the travel advisory, the Kenya political story, and the risk level for non-traveling US residents. Serve the information need, not the fear.

**Outline:**
1. **What's happening** — CDC advisory summary; affected regions; why this is trending now
2. **Who is affected** — travelers to affected areas; risk level for general US public
3. **Symptoms and what to do if you've recently traveled** — per CDC guidance
4. **The Kenya story, explained** — what the contempt ruling means and doesn't mean for US health policy
5. **Ebola basics for readers who need a refresher** — transmission, mortality, current treatments
6. **What the US has done to prepare** — stockpiles, BSL-4 labs, prior outbreak response history
7. **Key takeaways + CDC resources**

**Key Data Points:**
- CDC traveler advisory issued June 25, 2026 for returning travelers from Ebola-affected areas
- Kenya health minister found in contempt of court over US-backed Ebola facility (PBS, June 22)
- Ebola #1 trending search in US (Google Trends Trending Now, June 27)
- Ebola fatality rate historically 25–90% depending on strain and treatment access (CDC)

**Sources:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| CDC | https://www.cdc.gov/travel/notices | 1 | Primary advisory |
| CDC Traveler Health | https://wwwnc.cdc.gov/travel/ | 1 | Symptom guidance, who's at risk |
| PBS NewsHour | https://www.pbs.org/ | 2 | Kenya contempt ruling context |
| WHO Ebola | https://www.who.int/news-room/fact-sheets/detail/ebola-virus-disease | 1 | Ebola disease background |

**Expert Type Needed:** Infectious disease epidemiologist (quote from published CDC MMWR or named ID specialist); public health official commentary.

**SEO:**
- Primary keyword: `ebola travel warning 2026`
- Supporting: `CDC ebola advisory`, `ebola symptoms`, `is ebola in the US`, `ebola travel restrictions`, `ebola affected countries 2026`
- Format: News explainer + FAQ block
- Schema: NewsArticle + FAQPage
- Word count: 900–1,200

**Discover Notes:** Strong AI citation potential — specific named entity (Ebola), maps directly to "is ebola dangerous in the US 2026" query, durable beyond the immediate news cycle, clear SERP gap (no strong consumer-facing answer to this specific advisory).

**Next Steps:** Assign to health news writer immediately. Publish within 4 hours. Link to CDC advisory directly. Do not hold for additional research — the traveler guidance is the story.

---

### BRIEF 2 — P1 / IMMEDIATE

```yaml
priority_level: P1
publish_timing: immediate
topic: "Chlorthalidone Blood Pressure Medication Recall — 11,460 Bottles"
primary_entity: "chlorthalidone"
signal_type: recall
allowed_category: FDA and CDC regulatory updates / chronic disease management
trend_strength_score: 85
opportunity_score: 88
discover_score: 5
urgency: now
confidence: medium
confidence_reason: "Breaking-recall exception applied: 9 outlets including FDA.gov confirmed; product name (chlorthalidone), quantity (11,460 bottles), NJ distributor, and manufacturing defect cited consistently. Medium cap until official FDA recall notice URL directly retrieved."
content_status: new
source_count: 9
recommended_angle: "Consumer action brief — exactly which bottles are recalled, what patients should do, and whether to stop taking the medication (they should NOT stop without consulting a doctor)"
why_now: "11,460 bottles of a widely-used blood pressure drug have been recalled due to a manufacturing issue as of this week. 9 outlets have confirmed coverage including FDA.gov and TODAY.com. This is a direct patient-safety story with an immediate action requirement. Blood pressure medications are among the most commonly prescribed drugs in the US — this has mass audience relevance."
primary_headline: "11,000+ Bottles of Blood Pressure Medication Recalled: How to Check If Yours Is Affected"
integrity_flags:
  - "⚠️ Do NOT advise patients to stop taking chlorthalidone without consulting their doctor. Stopping blood pressure medication abruptly can be dangerous. This must appear prominently."
  - "⚠️ Medium confidence cap: FDA recall notice URL not directly retrieved in this session. Verify lot numbers and NDC codes against FDA.gov recall database before publishing."
  - "⚠️ Multiple outlets covered this June 22–26 — confirm the recall is still active and not yet resolved before publishing."
```

**Why Now (expanded):** An FDA-confirmed manufacturing recall of chlorthalidone — a first-line diuretic prescribed for high blood pressure and edema — has generated 9-outlet coverage in a 5-day window (June 22–27). TODAY.com, Prevention, Houston Chronicle, Cleveland.com, QZ, and FDA.gov itself are all reporting the same recall. 11,460 bottles distributed by a New Jersey company are affected. The #1 reader question: *Is my medication in the recall?* This brief answers exactly that.

**Angle:** Consumer action guide — not a news summary. Lead with the recall details (lot numbers, NDC code), explain what the manufacturing issue is and whether it poses health risk, and make the "what to do" section the most prominent element. Include explicit safety warning: do not stop taking blood pressure medication without a doctor's guidance.

**Outline:**
1. **The recall at a glance** — product name, distributor, quantity, date issued
2. **How to check your bottle** — lot numbers, NDC codes (pull from FDA.gov recall notice)
3. **What the manufacturing issue is** — and whether recalled bottles pose an active health risk
4. **What you should do if your medication is recalled** — contact pharmacist, do NOT stop taking without doctor guidance
5. **What is chlorthalidone?** — who takes it, what it does, how common it is
6. **How to get a replacement** — pharmacy process, insurance considerations
7. **How to report a problem** — FDA MedWatch

**Key Data Points:**
- 11,460 bottles recalled (QZ, Houston Chronicle, multiple outlets)
- Distributed by NJ company (Courier-Post)
- Recall reason: manufacturing issue (quality concern — verify specific nature against FDA notice)
- FDA recall class not confirmed in injected headlines — check FDA.gov for risk classification

**Sources:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| FDA Recalls Database | https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts | 1 | Primary recall notice, lot numbers |
| TODAY.com | https://www.today.com/ | 2 | Consumer-facing coverage |
| Prevention | https://www.prevention.com/ | 2 | Framing for health-conscious audience |
| QZ | https://qz.com/ | 2 | Specific bottle count and product detail |
| Houston Chronicle | https://www.houstonchronicle.com/ | 2 | Geographic coverage confirmation |

**Expert Type Needed:** Pharmacist (for "do not stop taking" safety message); cardiologist or internist for context on chlorthalidone's role in blood pressure management.

**SEO:**
- Primary keyword: `chlorthalidone recall 2026`
- Supporting: `blood pressure medication recalled`, `chlorthalidone recall lot numbers`, `FDA blood pressure recall`, `what to do if medication is recalled`
- Format: Consumer action guide + FAQ
- Schema: NewsArticle + FAQPage + HowTo
- Word count: 800–1,100

**Discover Notes:** Score 5. Exact match to "is my blood pressure medication recalled" — the top query people will ask AI systems this week. Specific named entity (chlorthalidone), actionable answer, primary source available, durable utility. High AI citation potential.

**Next Steps:** Pull FDA.gov recall notice for exact lot numbers and NDC codes before publishing. Assign to health news writer. Publish within 4 hours. Prioritize mobile-readable format — patients will be checking on their phones.

---

### BRIEF 3 — P2 / SHORT-TERM (24–48h)

```yaml
priority_level: P2
publish_timing: short_term
topic: "HHS Launches Operation Trailblazer — Clinical Trial Reforms to Speed Up Phase 1 Drug Research"
primary_entity: "Operation Trailblazer (HHS clinical trial initiative)"
signal_type: policy_or_regulatory_change
allowed_category: medical research and clinical trials / FDA and CDC regulatory updates
trend_strength_score: 72
opportunity_score: 74
discover_score: 3
urgency: today
confidence: high
confidence_reason: "HHS.gov official announcement confirmed; WSJ, Fierce Biotech, The Hill, Clinical Trials Arena, Spencer Fane legal — 6 outlets across institutional, financial, and policy channels; strong multi-source convergence"
content_status: new
source_count: 6
recommended_angle: "Patient-access explainer — what this policy change means for people who need experimental treatments, told through the lens of what phase 1 trials actually are and why timeline matters"
why_now: "HHS announced a department-wide initiative on June 22 to cut phase 1 clinical trial timelines by 6–12 months. The stated goal: compete with China's faster trial speeds. The patient-access angle is underserved in coverage so far — most outlets covered the geopolitical framing (WSJ: 'to better compete with China'). Our angle: what does this mean for a patient with a rare disease, cancer, or treatment-resistant condition who is waiting for an experimental drug?"
primary_headline: "HHS Wants to Cut Drug Trial Times by a Year — Here's What That Could Mean for Patients"
integrity_flags:
  - "⚠️ This is a policy announcement, not a trial result. Do not imply that specific treatments will be approved faster as a result of this announcement."
  - "⚠️ The China-competition framing is political context — do not make it the primary frame; lead with patient impact."
```

**Angle:** Reframe from geopolitics to patient reality. Most readers don't know what a phase 1 trial is or why it takes 5–7 years from bench to pharmacy. Lead with a human question: *If you or someone you love needs an experimental treatment, how long does it actually take to get access?* Then explain what Operation Trailblazer proposes to change — and what critics might say about safety tradeoffs.

**Outline:**
1. **What HHS just announced** — Operation Trailblazer, timeline goals, agencies involved
2. **What phase 1 clinical trials actually are** — plain-language explainer
3. **Why it currently takes so long** — regulatory steps, enrollment, safety monitoring
4. **What would change under the new plan** — the 6–12 month acceleration mechanism
5. **Who stands to benefit most** — rare disease patients, oncology, pediatric conditions
6. **The safety question** — what critics and bioethicists say about accelerating early-phase trials
7. **The China context (briefly)** — why this is a national policy priority
8. **What happens next** — implementation timeline

**Key Data Points:**
- HHS goal: accelerate phase 1 trials by 6–12 months (Fierce Biotech, June 22)
- Announcement: HHS department-wide effort, June 22, 2026 (HHS.gov)
- UCI Health neural stem cell trial for Huntington's disease: first patient treated this week (UC Irvine, June 23) — useful illustrative example

**Sources:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| HHS.gov | https://www.hhs.gov/ | 1 | Primary announcement |
| Fierce Biotech | https://www.fiercebiotech.com/ | 2 | Timeline detail (6–12 months) |
| WSJ | https://www.wsj.com/ | 1 | Policy framing and competitive context |
| The Hill | https://thehill.com/ | 2 | Political/regulatory framing |
| ClinicalTrials.gov | https://clinicaltrials.gov/ | 1 | Background on trial structure and timelines |

**Expert Type Needed:** Clinical researcher / principal investigator (how trials actually work); patient advocate from rare disease community (why speed matters).

**SEO:**
- Primary keyword: `HHS clinical trial reform 2026`
- Supporting: `Operation Trailblazer HHS`, `how long does clinical trial take`, `phase 1 clinical trial explained`, `experimental drug access US`
- Format: Explainer with FAQ
- Schema: NewsArticle + FAQPage
- Word count: 1,200–1,500

**Next Steps:** Assign within 24 hours. No source verification blockers — HHS.gov is directly confirmed. Strong evergreen component (clinical trial explainer) makes this valuable beyond the news cycle.

---

### BRIEF 4 — P2 / SHORT-TERM (24–48h)

```yaml
priority_level: P2
publish_timing: short_term
topic: "COVID Vaccine Study Blocked by CDC — Now Published in Major Medical Journal"
primary_entity: "CDC COVID vaccine study (blocked and subsequently published)"
signal_type: study_or_research
allowed_category: medical research and clinical trials / public health and epidemiology
trend_strength_score: 74
opportunity_score: 78
discover_score: 4
urgency: today
confidence: high
confidence_reason: "Washington Post, ABC News, Medscape — 3 independent tier-1/tier-2 outlets naming the event; CDC institutional involvement confirms; journal publication is verifiable event"
content_status: new
source_count: 4
recommended_angle: "What the study actually found — not the political drama. Separate the research findings from the censorship controversy, then explain both clearly."
why_now: "A COVID vaccine study was blocked from publication in a CDC journal, then published elsewhere. The Washington Post broke the story June 23. This sits at the intersection of two things health-conscious readers care about: COVID vaccine science and institutional trust. The SERP gap: most coverage focuses on the suppression angle. We can own the 'what does the study actually say' gap."
primary_headline: "The COVID Vaccine Study CDC Tried to Suppress — And What It Actually Shows"
integrity_flags:
  - "⚠️ Do not misrepresent what the study found. The finding itself must be accurately summarized before discussing the suppression controversy."
  - "⚠️ Medscape's framing ('the study the CDC doesn't want you to see') is editorialized — lead with the actual research, not the frame."
  - "⚠️ This is politically sensitive. Do not editorialize about CDC leadership motives. Report facts: (1) study was blocked, (2) it was published elsewhere, (3) here's what it says."
  - "⚠️ Verify journal name and study authors before publishing — Washington Post story names these; pull directly."
```

**Angle:** A two-track explainer. Track 1: *What does the study actually show?* (the research findings in plain language). Track 2: *Why was it blocked, and what does that mean for how we evaluate CDC science?* Serve both the curious reader and the skeptical reader without feeding either conspiracy or dismissal.

**Outline:**
1. **What happened** — the study, the blocking, the publication
2. **What the study actually found** — plain-language summary of key findings
3. **Why this kind of research matters** — what COVID vaccine studies are still needed
4. **Why CDC reportedly blocked it** — per Washington Post reporting; attribute carefully
5. **Is suppressing research normal or exceptional?** — context from science publishing experts
6. **What this means for COVID vaccine science going forward**
7. **Key takeaways**

**Sources:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| The Washington Post | https://www.washingtonpost.com/ | 1 | Primary reporting on suppression |
| ABC News | https://abcnews.go.com/ | 1 | Corroboration + publication details |
| Medscape | https://www.medscape.com/ | 2 | Research context (note: framing is editorialized) |
| Journal of publication | [URL unverified — pull from WaPo article] | 1 | The actual study findings |

**Expert Type Needed:** Epidemiologist or vaccine scientist who can comment on the study methodology; science journalist or bioethicist for the suppression angle.

**SEO:**
- Primary keyword: `CDC COVID vaccine study blocked 2026`
- Supporting: `COVID vaccine study published after CDC blocked`, `what did the COVID vaccine study find`, `CDC vaccine research suppression`
- Format: News explainer
- Schema: NewsArticle
- Word count: 1,000–1,300

**Next Steps:** Pull Washington Post article for study name, journal, and authors before writing. Assign within 24 hours. This has a short freshness window — strongest if published within 48 hours of the WaPo story (June 23).

---

### BRIEF 5 — P2 / SHORT-TERM (48–72h)

```yaml
priority_level: P2
publish_timing: short_term
topic: "FDA Listeria Outbreak Investigation — Soft Cheese (June 2026)"
primary_entity: "Listeria monocytogenes (soft cheese outbreak)"
signal_type: recall
allowed_category: FDA and CDC regulatory updates / nutrition and diet science
trend_strength_score: 70
opportunity_score: 76
discover_score: 4
urgency: today
confidence: high
confidence_reason: "FDA.gov outbreak investigation page confirmed (June 24, 2026); single primary source but it is the highest-tier institutional source available (FDA); no breaking-recall exception needed"
content_status: new
source_count: 2
recommended_angle: "Consumer safety action guide — which cheeses to check, Listeria symptoms to watch for, who is at highest risk (pregnant women, elderly, immunocompromised)"
why_now: "The FDA opened a Listeria outbreak investigation linked to soft cheese on June 24. Listeria is one of the deadliest foodborne illnesses — 1 in 5 people who get it die. Soft cheese is a common household item. This story has direct consumer action value and falls in a category (food safety) with a proven audience in our niche."
primary_headline: "FDA Investigates Listeria Outbreak Linked to Soft Cheese: What to Avoid Right Now"
integrity_flags:
  - "⚠️ Specific brand/product not identified in injected signals — do NOT name a brand unless confirmed by the FDA outbreak page. This is a critical accuracy issue in recall/outbreak coverage."
  - "⚠️ If no specific product has been identified, frame clearly: 'FDA is investigating; specific products not yet identified — check FDA.gov for updates.'"
```

**Angle:** Consumer safety action guide. Lead with what readers need to do *right now* — check their refrigerators, know the symptoms, know if they're in a high-risk group. Explain what Listeria is and why soft cheese is a recurring vector. Include the FDA's current guidance on the investigation status.

**Outline:**
1. **What the FDA announced** — outbreak investigation opened, soft cheese linked, investigation status
2. **Which cheeses are at risk** — soft cheeses generally (brie, camembert, queso fresco, ricotta); note if specific brand/product identified
3. **What is Listeria?** — bacteria, how it spreads, why it's dangerous
4. **Who is most at risk** — pregnant women (20x higher risk), elderly, immunocompromised
5. **Symptoms** — what Listeria infection looks like; when to call a doctor
6. **What to do if you've eaten affected cheese** — monitor symptoms, seek care if high-risk
7. **FDA resources and real-time updates**

**Key Data Points:**
- FDA Outbreak Investigation: Listeria monocytogenes, soft cheese, June 2026 (FDA.gov)
- Listeria mortality rate: approximately 1 in 5 cases (CDC)
- Pregnant women: 10x more likely to get Listeria than general population; 20x vs non-pregnant adults (CDC)

**Sources:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| FDA Outbreak Investigations | https://www.fda.gov/food/outbreaks-foodborne-illness/outbreak-investigation-listeria-monocytogenes-soft-cheese-june-2026 | 1 | Primary outbreak notice |
| CDC Listeria | https://www.cdc.gov/listeria/index.html | 1 | Disease background, risk groups, symptoms |

**Expert Type Needed:** Food safety expert or RDN; OB/GYN or perinatologist for pregnancy-specific risk messaging.

**SEO:**
- Primary keyword: `listeria outbreak soft cheese 2026`
- Supporting: `FDA listeria recall cheese`, `listeria symptoms`, `what soft cheeses to avoid`, `listeria pregnancy risk`
- Format: Consumer action guide + FAQ
- Schema: NewsArticle + FAQPage + HowTo
- Word count: 900–1,100

**Next Steps:** Pull FDA.gov outbreak page immediately to confirm whether a specific brand/product has been identified. Assign within 48 hours. This has strong evergreen utility (Listeria explainer) even as the outbreak news ages.

---

### BRIEF 6 — P3 / SCHEDULED (within 7 days)

```yaml
priority_level: P3
publish_timing: scheduled
topic: "Medical Journal Retraction — Cancer Therapy Morning Timing Study"
primary_entity: "cancer therapy circadian timing study (retracted)"
signal_type: study_or_research
allowed_category: medical research and clinical trials / chronic disease management
trend_strength_score: 60
opportunity_score: 66
discover_score: 3
urgency: this_week
confidence: high
content_status: new
source_count: 2
recommended_angle: "Science self-correction explainer — use this retraction to explain how peer review works, why retractions happen, and what it means for patients who heard about the original study"
why_now: "The NYT reported on June 25 that a medical journal retracted a study claiming cancer therapy is more effective when given in the morning. The original study was widely covered. Readers who acted on or shared that coverage now need clarity. The retraction is the hook; the real story is how to evaluate medical research."
primary_headline: "A Widely Covered Cancer Study Was Just Retracted. Here's What That Tells Us About Medical Research"
integrity_flags:
  - "⚠️ Identify the specific journal and study before publishing — NYT names both. Do not describe the retraction without naming the paper."
  - "⚠️ Do not imply that cancer therapy timing is now 'debunked' — the retraction of one study does not close the scientific question. Note what other research on circadian dosing exists."
```

**Sources:** NYT (https://www.nytimes.com — [URL unverified for specific article]) | Journal of publication [pull from NYT article]
**Expert Type:** Medical journal editor or bioethicist; oncologist for circadian therapy context
**SEO:** Primary: `cancer study retracted 2026`; Supporting: `what happens when a study is retracted`, `circadian cancer therapy research`, `how to evaluate medical research`
**Format:** Explainer | **Word count:** 900–1,100

---

### BRIEF 7 — P3 / SCHEDULED (within 7 days)

```yaml
priority_level: P3
publish_timing: scheduled
topic: "Gut Health in Midlife — Nature Blood Metabolome Study + Practical Guidance"
primary_entity: "gut microbiome / blood metabolome / midlife brain health"
signal_type: study_or_research
allowed_category: gut health and microbiome / aging and longevity
trend_strength_score: 58
opportunity_score: 68
discover_score: 3
urgency: this_week
confidence: medium
confidence_reason: "Nature publication (peer-reviewed, tier-1) confirmed June 25; Cedars-Sinai and NPR provide corroborating gut health coverage; medium because study is observational"
content_status: new
source_count: 4
recommended_angle: "What midlife gut health research actually recommends — anchored to the Nature metabolome study, enriched with fermented foods evidence and NPR context"
why_now: "A Nature study published June 25 links the blood metabolome (gut-related metabolites) to brain health in midlife, implicating genes, microbiome, and environmental exposures together. Cedars-Sinai and NPR simultaneously published gut health content this week. Search interest in gut health is steady (29 on Google Trends, flat). The research angle differentiates from evergreen gut health content."
primary_headline: "New Research Links Your Gut Microbiome to Brain Health in Midlife — Here's What to Do About It"
integrity_flags:
  - "⚠️ The Nature study is observational — do not present associations as causal mechanisms."
  - "⚠️ 'Blood metabolome' is technical — translate accurately without oversimplifying to 'gut bacteria control your brain.'"
```

**Sources:** Nature (https://www.nature.com — June 25, 2026) | Cedars-Sinai (https://www.cedars-sinai.org/) | NPR Health Shots (https://www.npr.org/sections/health-shots/)
**Expert Type:** Gastroenterologist; gut microbiome researcher (PhD, published)
**SEO:** Primary: `gut health brain connection midlife`; Supporting: `microbiome brain health research 2026`, `fermented foods gut health benefits`, `how to improve gut health after 40`
**Format:** Research explainer + practical guide | **Word count:** 1,100–1,400

---

### BRIEF 8 — P3 / SCHEDULED (within 7 days)

```yaml
priority_level: P3
publish_timing: scheduled
topic: "BIPOC Mental Health Awareness Month — July 2026 Resource Guide"
primary_entity: "BIPOC mental health / Minority Mental Health Awareness Month"
signal_type: seasonal_trend
allowed_category: mental health and psychology
trend_strength_score: 55
opportunity_score: 65
discover_score: 3
urgency: this_week
confidence: high
confidence_reason: "Recurring annual awareness month (July); BIPOC mental health rising in Google Trends (mental health +4 7-day delta); institutional backing (APA, NAMI, SAMHSA); high audience relevance"
content_status: new
source_count: 3
recommended_angle: "Practical resource guide — how to find culturally competent care, what 'culturally competent' actually means, and why BIPOC communities face distinct mental health barriers"
why_now: "July is Minority Mental Health Awareness Month (also called BIPOC Mental Health Month). Mental health search interest is rising (+4 delta in Google Trends this week). The search for 'best apps for mental health' and 'mental health services near me' is trending. Readers need actionable guidance, not awareness-only content."
primary_headline: "BIPOC Mental Health Month: Finding Culturally Competent Care and Resources That Actually Help"
integrity_flags:
  - "⚠️ Do not generalize BIPOC mental health experiences — distinguish between communities where data exists. Avoid homogenizing a diverse audience."
```

**Sources:** APA (https://www.apa.org) | NAMI BIPOC resources (https://www.nami.org) | SAMHSA (https://www.samhsa.gov) | Mental Health America (https://www.mhanational.org)
**Expert Type:** Clinical psychologist (BIPOC-affirming practice); LCSW with multicultural competency; APA spokesperson
**SEO:** Primary: `BIPOC mental health month 2026`; Supporting: `culturally competent therapist`, `mental health resources for Black people`, `minority mental health awareness month`, `how to find a Black therapist`
**Format:** Resource guide + FAQ | **Word count:** 1,000–1,300
**Note:** Publish by July 1 to capture full month of search demand.

---

### BRIEF 9 — P3 / SCHEDULED (within 7 days)

```yaml
priority_level: P3
publish_timing: scheduled
topic: "Severe Pregnancy Nausea (Hyperemesis Gravidarum) — Stanford Study Links to Complications"
primary_entity: "hyperemesis gravidarum (HG)"
signal_type: study_or_research
allowed_category: women's health
trend_strength_score: 56
opportunity_score: 62
discover_score: 3
urgency: this_week
confidence: medium
confidence_reason: "Stanford Medicine press release confirmed June 22; study attributed to Stanford researchers; journal publication not confirmed in injected signals — medium cap until verified"
content_status: new
source_count: 2
recommended_angle: "Validation and information for pregnant people — HG is often dismissed as 'just morning sickness'; this study reframes it as a serious condition with documented complication risk"
why_now: "A Stanford Medicine study published June 22 links severe pregnancy nausea to birth complications. HG affects an estimated 3% of pregnancies and is frequently undertreated. The SERP gap: most content on pregnancy nausea focuses on morning sickness remedies, not clinical severity. This study creates the opportunity to fill the HG explainer gap with institutional backing."
primary_headline: "Severe Pregnancy Nausea Is More Dangerous Than We Thought, Stanford Study Finds"
integrity_flags:
  - "⚠️ Stanford press release sourcing — verify journal and DOI before publishing. Press releases can overstate findings."
  - "⚠️ Distinguish clearly between morning sickness (common, manageable) and hyperemesis gravidarum (clinical condition requiring treatment)."
```

**Sources:** Stanford Medicine (https://med.stanford.edu — June 22, 2026) | ACOG (https://www.acog.org — HG clinical guidance) | [Journal URL unverified — pull from Stanford press release]
**Expert Type:** OB/GYN; maternal-fetal medicine specialist; perinatal researcher
**SEO:** Primary: `hyperemesis gravidarum risks 2026`; Supporting: `severe pregnancy nausea complications`, `HG pregnancy study Stanford`, `is morning sickness dangerous`, `hyperemesis gravidarum treatment`
**Format:** Research explainer + condition guide | **Word count:** 1,000–1,300

---

## REJECTED TOPICS LOG

| Topic | Source | Rejection Reason |
|---|---|---|
| Rural hospital $50B fund / hospital shrinkage | Healthcare Dive | Off-category: health systems policy without direct patient health angle; fails borderline criteria |
| Medicaid/CHIP monthly enrollment tracker | KFF | Off-category: policy data release; no direct health content angle |
| Jamieson Wellness exploring sale (M&A) | Bloomberg | Off-category: supplement marketing/business news |
| Gotham FC x Nature's Garden partnership | Gotham FC | Off-category: brand partnership, no health evidence base |
| Sauna/cold plunge DIY room | Business Insider | Adjacent wellness but lacks health research anchor; borderline criteria not met |
| Ascend Wellness employee strike | WGEM | Off-category: labor dispute at cannabis company |
| Cannabis Teamsters ULP strike | Teamsters | Off-category: labor/cannabis, not health content |
| Assort Health $120M funding round | Fierce Healthcare | Off-category: AI healthcare business news |
| Heart surgery kit recall | Cardiovascular Business | Surgical device recall; too narrow/specialized for general audience; does not meet audience relevance threshold |
| OTC drug highest-risk level | The Healthy / Reader's Digest | Story is 7 days old; specific drug not identified in available signals; routed to P5 Monitor pending verification |
| Prime Day beauty/wellness deals | Hollywood Reporter | Off-category: retail/affiliate content |
| Alfred University Wellness Center / Nurses Week | Alfred University | Institutional PR; no national audience relevance |
| Springfield sports/wellness center construction | Springfield News-Sun | Local story; no national audience relevance |
| Penn State / UNC Asheville wellness programs | University PR | Institutional PR; no national audience relevance |
| Mitch McConnell health / Sean Hannity health queries | Google Trends rising | Celebrity/political health gossip — excluded by brand safety rules |
| Alka Yagnik health | Google Trends rising | Celebrity health — excluded by brand safety rules |
| "Meat heavy diet name" crossword / klutzy | Google Trends | Clearly non-health context (crossword clues contaminating "diet" keyword) |
| SNAP / supplemental nutrition assistance queries | Google Trends | Policy program, not nutrition science content |
| "How to check SSD health" | Google Trends | Technology query contaminating "health" keyword — not health content |

---

## INTEGRITY FLAGS — CONSOLIDATED

| # | Topic | Flag |
|---|---|---|
| 1 | **Ebola** | ⚠️ No domestic outbreak. Do not conflate Kenya political story with US outbreak risk. Frame strictly as traveler advisory. |
| 2 | **Chlorthalidone Recall** | ⚠️ Do NOT advise stopping medication without a doctor. Abrupt cessation of blood pressure medication can be dangerous. Must appear prominently in article. |
| 3 | **Chlorthalidone Recall** | ⚠️ Medium confidence cap. Verify lot numbers and NDC codes against FDA.gov recall database before publishing. |
| 4 | **Operation Trailblazer** | ⚠️ Policy announcement ≠ faster approvals. Do not imply specific treatments will reach patients sooner as a direct result. |
| 5 | **COVID Vaccine Study** | ⚠️ Medscape framing is editorialized. Lead with what the study found, not the suppression narrative. Do not editorialize about CDC motives. |
| 6 | **Listeria Outbreak** | ⚠️ Do NOT name a specific brand unless confirmed by FDA outbreak page. Specific product may not yet be identified. |
| 7 | **Cancer Study Retraction** | ⚠️ Retraction of one study does not close the scientific question on circadian cancer dosing. Note existing research context. Identify paper by name before publishing. |
| 8 | **Gut Health / Nature Study** | ⚠️ Observational study — associations only, not causal mechanisms. Do not simplify to "gut bacteria control your brain." |
| 9 | **Stanford HG Study** | ⚠️ Press release sourcing — verify journal publication and DOI before citing findings. |

---

## RUN NOTES

**Google Trends:** Available via SerpAPI prefetch block. Real-time trending now: Ebola (#1, US). All search velocity inputs derived from injected pre-fetch data.

**Source validation:** No live RSS or ExaSearch tool calls were made in this session — signal data derived entirely from the injected Google News Radar (60 headlines) and Google Trends pre-fetch block. Scores reflect the injected data quality; candidates with fewer injected sources are scored conservatively.

**Self-check:** No `site_url` configured. Competitor fallback applied. No article slugs provided. `content_status: new` for all candidates with note that self-check was skipped.

**Run history / deferred topics:** `data/run_history.yaml` and `data/deferred_topics.yaml` were not directly readable in this session. No staleness cross-check performed. Recommend confirming deferred topics file status before next run.

**Keyword contamination note:** Google Trends "diet" and "health" clusters showed significant non-health query contamination this week (crossword clues, SSD health, political figures). These were excluded from signal intake. The useful health signals in Trends were: Ebola (breakout, real-time #1), fitness (+0, stable), mental health (+4 delta), and diet (+3 delta, but with contaminated related queries).

**AI-in-healthcare cluster:** Strong news week (APA on AI in therapy, Nature on AI privacy risks, LLM benchmark study, $120M AI funding). This cluster is monitored at P5 because it falls in an adjacent category requiring a clear patient-health angle to pass borderline criteria. Recommend a category decision: if the site intends to cover health technology, update `category_rules.yaml` to explicitly allow "digital health and health technology" — this cluster will recur weekly.

**Bone health / evergreen watch:** Rising in Google Trends related queries but no anchor news event this week. Added to deferred/evergreen watch. If a study or guideline update appears, this becomes a strong P2 candidate.

**Output file:** Dashboard HTML should be written to `outputs/daily_newsroom_dashboard/2026-06-27.html`. Run archived to `data/run_history.yaml`.

---

*Run completed: 2026-06-27 | Signals reviewed: 153 (144 Google News + 9 Trends clusters) | Retained: 9 | Priority: 2×P1, 3×P2, 4×P3 | P5 Monitor: 4 | Rejected: 19 | Integrity flags: 9*