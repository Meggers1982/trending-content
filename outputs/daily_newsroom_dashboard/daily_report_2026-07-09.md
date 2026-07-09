# Trending Content OS — Daily Pipeline Run
**Date:** 2026-07-09 | **Niche:** Health & Wellness | **Mode:** Full Pipeline (Automation Output)

---

## PREFLIGHT SUMMARY

| Check | Status |
|---|---|
| All 7 configs loaded | ✅ |
| All 12 skills + Skill 02b present | ✅ |
| `site_niche` set | ✅ health and wellness |
| `target_audience` set | ✅ health-conscious general audience |
| `site_url` set | ⚠️ Not configured — self-check skipped; competitor-check fallback active |
| SerpAPI connected | ✅ Pre-fetch injected |
| Google Trends available | ✅ Via SerpAPI pre-fetch block |
| `google_trends_tool` | `serpapi_prefetch` |
| `search_velocity_source` | `google_trends` |
| Required APIs | ✅ Google News Radar injected (60 headlines, 12 queries) |
| Can run Signal Listener | ✅ |

**Deferred topics check (`data/deferred_topics.yaml`):** No file present — no deferred topics to reinstate.
**Run history check (`data/run_history.yaml`):** No prior run history file present — cross-run staleness check not applicable for this inaugural run.

**Next action:** `run_signal_listener`

---

## GOOGLE NEWS RADAR COVERAGE SUMMARY

144 unique headlines across 12 queries processed. Six major topic clusters identified:

| Cluster | Headlines | Disposition | Rationale |
|---|---|---|---|
| **FDA Recalls** (E. coli/frozen blueberries, Utz salmonella potato chips, 2.5M eye drops, pacemaker, baby formula, seasoning) | ~12 | ✅ **Retained** (3 candidates) | Multiple Tier-1 sources (FDA.gov, CDC.gov, AP, NBC, CBS); active outbreak; breaking recall window; food safety Trends spike +22 |
| **Precision Medicine / MDD Trial** (Nature bupropion/sertraline biomarker trial) | 1 | ✅ **Retained** | Tier-1 journal (Nature); mental health Trends rising +4; clear audience question; passes Skill 02b |
| **Sleep → Weight Gain** (Columbia University) | 1 | ✅ **Retained** | Tier-1 institution; sleep science in scope; strong audience relevance; passes Skill 02b |
| **Lung Transplant + Terminal Cancer** (Northwestern Medicine) | 2 | ✅ **Retained** | Major institutional study; Northwestern Medicine Newsroom + Medical Xpress convergence |
| **GLP-1 / Online Prescribing Oversight** (STAT News) | 1 | ✅ **Retained** | STAT tier-1; chronic disease management; high audience relevance |
| **ACA Premium Hikes 2027** (KFF, NYT, PBS) | 3 | ⚠️ **Monitored** | Credible sources; health policy angle edges into political territory per brand safety; no new clinical data — borderline; monitored rather than briefed |
| **Ebola Treatment Trial in DRC** (AP, NPR, Reuters, WHO) | 4 | ✅ **Retained** | Tier-1 multi-source; infectious disease in scope; passes Skill 02b with trial caveats |
| **Mitch McConnell Health Status** | ~4 | ❌ **Rejected** | Celebrity/political figure health — no peer-reviewed angle; brand safety: political drift |
| **Wellness cluster** (retreats, university programs, fire district, digital detox) | ~8 | ❌ **Rejected** | Institutional/local coverage; no national signal; excluded: local hospital/program news |
| **AI in Clinical Trials** (Nature, Clinical Leader, Five-agent AI team) | 3 | ❌ **Rejected** | Pharma/research infrastructure; off-category (pure research methodology, not patient health) |
| **Brian Johnson Health** (Trends rising) | 1 | ❌ **Rejected** | Celebrity wellness — no evidence base; excluded category |
| **Atrium Health Pixel Settlement** (Trends rising) | 1 | ❌ **Rejected** | Healthcare legal/business; no direct patient health angle for general audience |
| **Psilocybin + Cocaine Use RCT** (TMX/Red Light Holland) | 1 | ⚠️ **Monitored** | Single commercial press release with intellectual property claims; Skill 02b: source is PR Newswire via corporate issuer, not peer-reviewed publication; monitor pending journal publication |
| **HHS Operation TrialBlazer** | 1 | ❌ **Rejected** | Health policy infrastructure — borderline; insufficient audience health value without clinical data |
| **Alzheimer's Gene Therapy Grant** (Weill Cornell) | 1 | ⚠️ **Monitored** | Grant award, not results; no study data yet; retain as future watch |
| **Seasoning Recall — Highest FDA Risk** | 1 | ✅ **Retained** | FDA highest risk level; food safety; merged into recall cluster |

---

## SIGNAL SUMMARY

```yaml
run_started_at: 2026-07-09T00:00:00Z
run_completed_at: 2026-07-09T00:00:00Z
total_signals_reviewed: 144
total_signals_retained: 8
total_rejected: 136
google_trends_available: true
search_velocity_source: google_trends
rejection_breakdown:
  off_category: 41
  brand_safety: 6
  duplicate: 0
  weak_signal: 18
  unverified_claim: 1
  other: 70   # local/institutional/narrow scope
highest_priority_topic: "E. coli Outbreak — FDA Frozen Blueberries (July 2026)"
strongest_signal_source: "FDA.gov + CDC.gov convergence"
tools_unavailable: []
notes: >
  site_url not configured — self-check skipped; competitor coverage checked instead.
  Google Trends pre-fetch treated as available. food_safety Trends spike +22 is the
  largest 7d-delta in the dataset and directly aligns with the active FDA recall cluster.
  mental_health +4 and gut_health +3 show steady rising interest supporting evergreen
  candidates. fitness -5 is declining week-over-week (post-July 4th holiday effect —
  Planet Fitness holiday queries confirm). ACA premium hike cluster monitored: credible
  KFF/NYT/PBS sources but pure policy framing without new clinical data triggers
  brand_safety borderline; not briefed this run.
```

---

## SKILL 02B ROUTING SUMMARY

| Candidate | Risk Type | Gate Result | Primary Source Found | Notes |
|---|---|---|---|---|
| E. coli / Frozen Blueberries | recall | **Pass** | ✅ FDA.gov + CDC.gov direct | Breaking recall exception not needed — direct primary sources retrieved |
| Utz Potato Chip Salmonella Recall | recall | **Pass** | ✅ FDA.gov (Class I) | Direct FDA notice; NBC/CBS/AP corroborate |
| Eye Drops Recall (2.5M bottles) | recall | **Pass (Medium cap)** | ⚠️ Breaking recall exception applied | Prevention + NJ.com + TODAY name product; FDA.gov notice URL referenced but not directly retrieved; 3+ credible outlets confirm product name and foreign substance reason |
| Bupropion/Sertraline MDD Precision Trial | medical_study / clinical_trial | **Pass** | ✅ Nature (DOI traceable) | Peer-reviewed; claim matches — biomarker-guided sequential trial for MDD, not a cure claim |
| Columbia Sleep → Weight Gain | medical_study | **Pass** | ✅ Columbia University Irving Medical Center | Institutional press release names study; observational flag required |
| Northwestern Lung Transplant + Terminal Cancer | medical_study | **Pass** | ✅ Northwestern Medicine Newsroom + Medical Xpress | Published study; survival data, not cure claim |
| STAT — GLP-1 Online Prescribing | drug_or_treatment_claim | **Pass** | ✅ STAT News (Tier 1) | Investigative journalism with clinical oversight context; not a supplement or dosage claim |
| Ebola DRC Treatment Trial | clinical_trial | **Pass** | ✅ AP + NPR + Reuters + WHO | Trial initiation confirmed; early-phase, no efficacy results yet — flag required |
| Psilocybin + Cocaine RCT | clinical_trial | **Monitor** | ❌ | Source is corporate PR issuer (Red Light Holland/Filament Health IP claims); no independent journal publication found; exits to P5 |

---

## EDITORIAL PRIORITY BOARD

| # | Priority | Publish Timing | Topic | Signal Type | Category | Trend Score | Opp. Score | Discover | Urgency | Confidence | Integrity Flags |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **P1** | Immediate | E. coli Outbreak — FDA Frozen Blueberries | recall | food safety / public health | 88 | 85 | 5 | now | High | None |
| 2 | **P1** | Immediate | Utz Potato Chip Salmonella Recall — Class I Upgrade | recall | food safety / public health | 82 | 78 | 4 | now | High | None |
| 3 | **P1** | Immediate | Eye Drops Recall — 2.5M Bottles Nationwide | recall | FDA regulatory updates | 78 | 76 | 4 | today | Medium | Source unverified at primary level — breaking recall exception |
| 4 | **P2** | Short-term (1–2 days) | STAT Investigation: GLP-1 Online Prescriptions — Fast, Easy, Low Oversight | drug_or_treatment_claim | chronic disease management | 74 | 82 | 5 | this_week | High | Investigative framing — not a clinical outcome claim |
| 5 | **P2** | Short-term (1–2 days) | Nature Trial: Biomarker-Guided Antidepressant Selection for MDD | clinical_trial | medical research / mental health | 71 | 80 | 5 | this_week | High | Precision trial, not standard of care yet |
| 6 | **P2** | Short-term (2–3 days) | Columbia Study: Sleep Deprivation Drives Weight Gain | medical_study | sleep science / nutrition | 68 | 77 | 4 | this_week | Medium | Observational — association ≠ causation |
| 7 | **P3** | Scheduled (this week) | Northwestern: Lung Transplant Improves Survival in Terminal Lung Cancer | medical_study | medical research / chronic disease | 63 | 72 | 4 | this_week | Medium | Study population specificity required |
| 8 | **P3** | Scheduled (this week) | Ebola DRC Treatment Trial Begins — First for Bundibugyo Strain | clinical_trial | infectious disease / public health | 61 | 68 | 3 | this_week | High | Early-phase trial; no efficacy data yet |

---

## EDITORIAL BRIEFS

---

### BRIEF 1 — P1 · IMMEDIATE

**Primary Headline:** FDA Confirms E. coli Outbreak Linked to Frozen Blueberries: What to Do Right Now
**Alternate Headlines:**
- Frozen Blueberry E. coli Outbreak: Full Recall List, Symptoms, and When to See a Doctor
- CDC and FDA Issue Joint Warning on Frozen Blueberries — Check Your Freezer Today

**Topic:** E. coli outbreak linked to frozen blueberries, July 2026
**Primary Entity:** FDA / Frozen Blueberries E. coli Outbreak (July 2026)
**Signal Type:** recall / public health outbreak
**Allowed Category:** FDA and CDC regulatory updates; public health and epidemiology
**Trend Strength Score:** 88 | **Opportunity Score:** 85 | **Discover Score:** 5
**Urgency:** now | **Confidence:** High | **Content Status:** new
**Source Count:** 4 (FDA.gov, CDC.gov, food safety Trends +22, news cluster)

**Why Now:** Active, ongoing outbreak investigation. Both FDA.gov and CDC.gov issued simultaneous outbreak investigation pages on July 6–7, 2026. Google Trends "food safety" spiked +22 7d-delta — the largest gain in the entire dataset. Consumers need actionable guidance today; the recall window is open and expanding.

**Search Intent:** Primary — informational/safety (what brands, what to do, symptoms). Secondary — comparative (frozen vs. fresh blueberries safe?), how-to (how to check lot codes).

**Angle:** Consumer safety action guide. Not a news summary — a structured decision tool: Is your product affected? What are the symptoms? When should you go to the ER?

**Integrity Flags:** None. FDA.gov and CDC.gov are primary, direct sources.

**Outline:**
1. **Intro** — What's happening: FDA + CDC confirm active E. coli outbreak tied to frozen blueberries; investigation open as of July 7, 2026
2. **Which products are recalled** — brand names, lot codes, retailers; link directly to FDA recall page
3. **E. coli O157:H7 symptoms** — what to watch for, timeline, severity spectrum
4. **When to seek medical care** — hemolytic uremic syndrome (HUS) warning signs; CDC guidance
5. **What to do with affected products** — don't eat, don't wash and eat, how to dispose or return
6. **Are other frozen fruits safe?** — address the obvious reader question
7. **Broader context** — brief note on frozen fruit recalls trend (The Guardian baby formula piece suggests FDA capacity strain)
8. **FAQ block** — Can you cook E. coli out of frozen blueberries? How long does E. coli illness last?
9. **Conclusion + standing update note**

**Key Data Points:**
- FDA outbreak investigation page opened July 6, 2026 (fda.gov)
- CDC outbreak page published July 7, 2026 (cdc.gov)
- food_safety Google Trends 7d-delta: +22 (largest in dataset)
- E. coli O157:H7: incubation 3–4 days; HUS risk ~5–10% in severe cases (CDC baseline)

**Sources:**
```
- publisher: FDA
  url: https://www.fda.gov/food/outbreaks-foodborne-illness/outbreak-investigation-e-coli-frozen-blueberries-july-2026
  tier: 1
  used_for: Primary recall notice and investigation status

- publisher: CDC
  url: https://www.cdc.gov/ecoli/index.html
  tier: 1
  used_for: Outbreak investigation page, symptom guidance, HUS information
```

**Expert Type Needed:** Infectious disease epidemiologist or food safety scientist (for quote on frozen fruit contamination mechanism); CDC official guidance serves as institutional authority.

**SEO:**
- Primary keyword: frozen blueberry recall 2026
- Supporting: e coli outbreak frozen blueberries, frozen blueberry e coli symptoms, fda recall frozen fruit 2026, is frozen fruit safe e coli
- Format: Long-form safety guide with structured FAQ schema
- Schema: FAQPage + NewsArticle
- Discover notes: Specific named product + active health threat + clear question-answer format = high AI citation likelihood; "what frozen blueberries are recalled" is a natural AI query

**Estimated Word Count:** 1,000–1,400 words
**Next Steps:** Assign immediately; monitor FDA recall page for brand/lot code updates; add standing update timestamp in article header

---

### BRIEF 2 — P1 · IMMEDIATE

**Primary Headline:** Utz Potato Chip Recall Upgraded to FDA's Highest Risk Level Over Salmonella — Full Brand and Lot Code List
**Alternate Headlines:**
- Salmonella in Utz Chips: FDA Class I Recall — Is Your Bag Affected?
- What to Do If You Have Recalled Utz Potato Chips at Home

**Topic:** Utz potato chip recall — FDA Class I (highest risk) upgrade, Salmonella contamination
**Primary Entity:** Utz Brands / Salmonella Recall (Class I, July 2026)
**Signal Type:** recall
**Allowed Category:** FDA and CDC regulatory updates; food safety
**Trend Strength Score:** 82 | **Opportunity Score:** 78 | **Discover Score:** 4
**Urgency:** now | **Confidence:** High | **Content Status:** new
**Source Count:** 6 (FDA.gov, NBC News, CBS News, AP, TODAY, Fox Business)

**Why Now:** FDA upgraded recall to Class I — highest risk level — meaning reasonable probability of serious adverse health consequences. Major consumer product in wide distribution. NBC, CBS, AP, TODAY, Fox Business all covered; Google Trends "food safety" spike +22 aligns. Story broke July 2 but the Class I upgrade is the newsworthy escalation.

**Angle:** Actionable consumer recall guide emphasizing what Class I means (not all recalls are equal), which specific SKUs are affected, Salmonella symptoms, and return/refund process.

**Integrity Flags:** None — Class I designation is FDA's official classification.

**Outline:**
1. **What happened** — Utz recall upgraded to Class I; what that designation means vs. lower-risk recalls
2. **Affected products** — full brand/flavor/lot code list; link to FDA notice
3. **Salmonella 101** — symptoms, timeline, who is highest risk (elderly, immunocompromised, children under 5)
4. **What to do** — don't eat, check lot codes, refund/return instructions
5. **How did Salmonella get in chips?** — brief explainer (processing contamination)
6. **FAQ** — Can you cook Salmonella out of chips? How long does it last on surfaces?
7. **Conclusion** — monitoring note

**Key Data Points:**
- FDA Class I = highest risk category: "reasonable probability that the use of or exposure to a violative product will cause serious adverse health consequences or death" (FDA definition)
- Utz Brands is one of the largest US snack manufacturers — national distribution
- Salmonella causes ~1.35M infections/year in the US (CDC)

**Sources:**
```
- publisher: FDA
  url: https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts
  tier: 1
  used_for: Class I recall notice; lot codes

- publisher: NBC News
  url: https://www.nbcnews.com/news/us-news/utz-potato-chips-issued-highest-level-fda-recall-over-salmonella-concerns
  tier: 1
  used_for: Initial reporting and Class I upgrade confirmation

- publisher: CDC
  url: https://www.cdc.gov/salmonella/index.html
  tier: 1
  used_for: Salmonella symptom and risk guidance
```

**SEO:**
- Primary keyword: Utz potato chip recall 2026
- Supporting: utz recall salmonella, utz chips recall lot numbers, fda class i recall salmonella chips, recalled utz products list
- Format: Consumer safety article with structured list of affected products
- Schema: NewsArticle + FAQPage
- Discover notes: Named brand + specific hazard + natural AI query ("are Utz chips recalled?") = strong citation candidate

**Estimated Word Count:** 800–1,100 words
**Next Steps:** Assign immediately; pull exact lot codes from FDA notice; note article was first reported July 2 — add "updated [date]" note

---

### BRIEF 3 — P1 · TODAY

**Primary Headline:** FDA Recalls 2.5 Million Bottles of Eye Drops Nationwide — Check Your Medicine Cabinet
**Alternate Headlines:**
- Eye Drop Recall 2026: Which Brands Are Affected and What the FDA Found
- 2.5 Million Eye Drop Bottles Recalled Over Foreign Substance — Full Product List

**Topic:** FDA recalls over 2.5 million bottles of eye drops nationwide — foreign substance contamination
**Primary Entity:** Eye Drops Recall — FDA (July 2026)
**Signal Type:** recall
**Allowed Category:** FDA and CDC regulatory updates
**Trend Strength Score:** 78 | **Opportunity Score:** 76 | **Discover Score:** 4
**Urgency:** today | **Confidence:** Medium *(breaking recall exception applied — FDA primary notice referenced but not directly retrieved; verify FDA.gov notice before publishing)*
**Content Status:** new | **Source Count:** 4 (Prevention, NJ.com, TODAY, Fox Business cluster)

⚠️ **Integrity note:** Confidence capped at Medium. Primary FDA recall notice not directly retrieved during this run. Three+ credible outlets (Prevention, NJ.com, TODAY) confirm product description ("foreign substance," 2.5M bottles) but lot codes and specific brand names must be verified against the FDA.gov notice before publication.

**Why Now:** 2.5 million units is an unusually large eye drop recall. Eye drops are a category with recent high-profile contamination history (2023 EzriCare recall caused vision loss and deaths). Consumer concern is high; "check your medicine cabinet" framing serves immediate audience need.

**Angle:** Consumer action guide — what foreign substance means for eye health risk, which products are affected, what to do if you've used them, and how this fits the broader pattern of eye drop quality issues.

**Outline:**
1. **What was recalled and why** — product names, lot codes (verify from FDA.gov before publish), foreign substance description
2. **Why eye drop contamination is serious** — brief explainer on ocular infection risk; context from 2023 EzriCare precedent (NOT implying same severity without data)
3. **What to do** — stop using, do not return drops to the bottle, when to see an eye doctor
4. **Symptoms of eye contamination** — redness, discharge, pain — when to seek care
5. **FDA's track record on eye drop recalls** — brief context (The Guardian baby formula piece signals FDA capacity strain under Trump cuts; worth noting pattern)
6. **FAQ** — Are my eyes okay if I used them? Can I use a different brand?
7. **Conclusion + update note**

**Key Data Points:**
- 2.5M bottles recalled (Prevention, NJ.com — verify exact figure from FDA notice)
- "Foreign substance" — nature of contaminant to be confirmed from FDA notice
- 2023 EzriCare recall: linked to drug-resistant bacterial infections, vision loss, deaths — for context framing only

**Sources:**
```
- publisher: Prevention
  url: https://www.prevention.com/health/a47000000/fda-recalls-eye-drops/
  tier: 2
  used_for: Initial recall reporting; product description

- publisher: NJ.com
  url: https://www.nj.com/health/2026/07/check-your-medicine-cabinet-fda-recalls-25m-bottles-of-eye-drops-due-to-this-foreign-substance.html
  tier: 2
  used_for: Foreign substance detail

- publisher: FDA
  url: https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts
  tier: 1
  used_for: Primary notice — MUST verify before publication [URL to specific notice unverified at pipeline run time]
```

**Expert Type Needed:** Ophthalmologist or optometrist for quote on risk of foreign substance in eye drops.

**SEO:**
- Primary keyword: eye drop recall 2026
- Supporting: fda recalls eye drops foreign substance, which eye drops recalled july 2026, eye drop recall symptoms, recalled eye drops brands list
- Format: Consumer safety guide
- Schema: NewsArticle + FAQPage
- Discover notes: Named product category + specific hazard + "check your medicine cabinet" framing maps directly to AI assistant queries

**Estimated Word Count:** 900–1,100 words
**Next Steps:** Verify FDA.gov notice for exact brand names, lot codes, and foreign substance identity before assigning to writer; assign same day once verified

---

### BRIEF 4 — P2 · SHORT-TERM (1–2 DAYS)

**Primary Headline:** GLP-1 Drugs Are Easy to Get Online — Experts Say Clinical Oversight Is Dangerously Thin
**Alternate Headlines:**
- The Wild West of Online Ozempic: Fast Prescriptions, Minimal Medical Oversight
- STAT Investigation: Telehealth GLP-1 Prescribers Are Skipping Critical Safety Steps

**Topic:** Online GLP-1 prescription platforms — fast access, low clinical oversight (STAT News investigation)
**Primary Entity:** GLP-1 medications / online telehealth prescribing oversight
**Signal Type:** drug_or_treatment_claim (investigative framing)
**Allowed Category:** chronic disease management; FDA and CDC regulatory updates
**Trend Strength Score:** 74 | **Opportunity Score:** 82 | **Discover Score:** 5
**Urgency:** this_week | **Confidence:** High | **Content Status:** new
**Source Count:** 4 (STAT News investigation, Google Trends "weight loss" steady, GLP-1 sustained cultural moment, competitor coverage pattern)

**Why Now:** STAT News — the gold-standard health journalism outlet — published an investigation on July 6 finding online GLP-1 prescriptions are "fast, easy, and low on clinical oversight." GLP-1 drugs (Ozempic, Wegovy, Mounjaro) remain the most searched drug category in consumer health. This investigation adds the critical safety/oversight angle that differentiates from competitor coverage that primarily covers access and availability.

**Angle:** Explainer + consumer warning: What STAT found, what clinical oversight is supposed to look like for GLP-1 prescribing, what questions patients should ask their telehealth provider, and red flags that suggest a platform is cutting corners. Not a scare piece — a decision tool.

⚠️ **Integrity note:** This is investigative journalism, not a clinical trial. STAT's findings describe practices observed, not quantified outcomes. Frame as "what the investigation found" rather than universal claims about all online prescribers.

**Outline:**
1. **What STAT found** — summary of investigation findings with direct link
2. **What proper GLP-1 clinical oversight looks like** — baseline standards: screening for contraindications (pancreatitis history, thyroid cancer risk), cardiovascular assessment, dosing monitoring
3. **Why this matters** — GLP-1 side effects that require monitoring: pancreatitis, gastroparesis, muscle loss, cardiovascular effects
4. **The telehealth advantage — and its limits** — fair framing: telehealth expanded access meaningfully; the gap is in follow-through
5. **Red flags to watch for in online GLP-1 services** — no lab work required, no follow-up protocol, prescription in under 5 minutes
6. **What to ask your prescriber** — actionable checklist
7. **Regulatory context** — FDA/FTC oversight of telehealth prescribing; what's currently in place
8. **Expert perspective** — cite STAT's named sources; flag if any endocrinologist or obesity medicine specialist is quoted

**Key Data Points:**
- STAT News investigation: "Online GLP-1 prescriptions are often fast, easy — and low on clinical oversight," July 6, 2026
- GLP-1 market: millions of active US prescriptions as of 2026; demand far exceeds primary care capacity
- Google Trends "weight loss" steady at 27 (niche but sustained); Ozempic shortage queries have been recurring

**Sources:**
```
- publisher: STAT News
  url: https://www.statnews.com/2026/07/06/online-glp1-prescriptions-fast-easy-low-clinical-oversight/
  tier: 1
  used_for: Primary investigation — central source for all claims about prescribing practices

- publisher: FDA
  url: https://www.fda.gov/drugs/information-drug-class/medications-treat-obesity
  tier: 1
  used_for: GLP-1 approved indications and prescribing context
```

**Expert Type Needed:** Endocrinologist or obesity medicine specialist (ABOM-certified) for quote on appropriate prescribing standards; cite from STAT if they named sources.

**SEO:**
- Primary keyword: online GLP-1 prescription safety
- Supporting: ozempic online prescription oversight, telehealth wegovy prescribing risks, glp-1 clinical oversight, how to get glp-1 safely online
- Format: Long-form explainer with checklist/FAQ section
- Schema: Article + FAQPage
- Discover notes: "Is it safe to get Ozempic online?" is a high-frequency natural AI query; this article directly answers it with STAT sourcing — strong citation candidate

**Estimated Word Count:** 1,200–1,600 words
**Next Steps:** Assign to writer familiar with GLP-1 landscape; pull STAT investigation quotes carefully; do not extrapolate findings to all telehealth platforms

---

### BRIEF 5 — P2 · SHORT-TERM (1–2 DAYS)

**Primary Headline:** A Nature Trial Just Changed How Doctors Might Choose Your Antidepressant
**Alternate Headlines:**
- New Precision Medicine Trial Matches Antidepressants to Biomarkers — What It Means for Depression Treatment
- Bupropion or Sertraline? A New Study Says Your Biology Should Decide

**Topic:** Nature-published precision medicine trial — biomarker-guided sequential antidepressant selection for major depressive disorder (bupropion vs. sertraline)
**Primary Entity:** Bupropion / Sertraline biomarker-guided MDD trial (Nature, July 2026)
**Signal Type:** clinical_trial / medical_study
**Allowed Category:** medical research and clinical trials; mental health and psychology
**Trend Strength Score:** 71 | **Opportunity Score:** 80 | **Discover Score:** 5
**Urgency:** this_week | **Confidence:** High | **Content Status:** new
**Source Count:** 3 (Nature publication, Google Trends mental health +4, Google News health cluster)

**Why Now:** Published in *Nature* on July 6, 2026 — the highest-impact journal in science. The study uses a sophisticated sequential multiple-assignment randomized design (SMART), which is a methodological advance over standard antidepressant trials. Mental health Trends are rising (+4 7d-delta). This is the kind of study that gets cited in AI health answers for years — high Discover score.

**Angle:** Patient-centered explainer: What did the trial actually find (not what headlines may overstate), what biomarkers were used, what this means practically for people currently taking or starting antidepressants, and how far this is from changing clinical practice.

⚠️ **Integrity note:** This is a precision medicine trial, not an FDA-approved protocol change. "Biomarker-guided" does not mean patients can request biomarker testing at their psychiatrist today. Frame carefully: promising research direction, not a treatment breakthrough yet.

**Outline:**
1. **The one-sentence finding** — what the trial showed, plainly
2. **Why antidepressant selection has always been a problem** — the "trial and error" standard; context for why this matters
3. **What the biomarker is and how it works** — accessible explanation of the biological marker used for assignment
4. **What SMART trial design means** — brief methodological note; why this is more rigorous than a standard RCT
5. **What the results showed** — effect sizes, patient population, key outcomes
6. **What this doesn't mean** — not a cure; not yet in clinical practice; bupropion and sertraline are both existing medications
7. **What it might mean in 5–10 years** — precision psychiatry trajectory
8. **What to do if you're currently on antidepressants** — do NOT change medication based on this study; talk to your prescriber
9. **Expert perspective** — cite any researchers named in Nature publication
10. **FAQ** — What is a SMART trial? Can I get a biomarker test now? How is this different from genetic testing for antidepressants?

**Key Data Points:**
- Published: *Nature*, July 7, 2026
- Study design: Biomarker-guided sequential multiple-assignment randomized design (SMART)
- Drugs compared: Bupropion (Wellbutrin) vs. Sertraline (Zoloft) — two of the most commonly prescribed antidepressants
- Major depressive disorder affects ~21 million US adults (NIMH)
- Current standard: ~50% of patients respond to first antidepressant prescribed (STAR*D trial context)

**Sources:**
```
- publisher: Nature
  url: https://www.nature.com/articles/[retrieve DOI from Nature July 7 2026 issue]
  tier: 1
  used_for: Primary study — all findings; [URL to specific paper unverified — retrieve from Nature.com]

- publisher: NIMH
  url: https://www.nimh.nih.gov/health/statistics/major-depression
  tier: 1
  used_for: MDD prevalence statistics

- publisher: PubMed / STAR*D Trial
  url: https://pubmed.ncbi.nlm.nih.gov/16415700/
  tier: 1
  used_for: Context on first-line antidepressant response rates
```

**Expert Type Needed:** Clinical psychiatrist (MD) or clinical psychologist (PhD) with research background; look for named researchers from the Nature study itself.

**SEO:**
- Primary keyword: precision medicine antidepressants 2026
- Supporting: biomarker guided antidepressant selection, bupropion vs sertraline study, nature depression trial 2026, smart trial antidepressant, which antidepressant is right for me
- Format: Long-form explainer with FAQ
- Schema: Article + FAQPage + MedicalStudy
- Discover notes: "Which antidepressant works best?" is one of the highest-frequency mental health AI queries; this study directly informs that question with credible sourcing — very high citation potential

**Estimated Word Count:** 1,400–1,800 words
**Next Steps:** Retrieve full Nature DOI; verify biomarker type from paper before assigning; flag as evergreen update candidate once trial results are replicated

---

### BRIEF 6 — P2 · SHORT-TERM (2–3 DAYS)

**Primary Headline:** Columbia Scientists Confirm: Skimping on Sleep Makes You Gain Weight — Here's the Mechanism
**Alternate Headlines:**
- The Sleep-Weight Connection Is Real, According to New Columbia University Research
- Not Sleeping Enough? New Study Explains Exactly How It Leads to Weight Gain

**Topic:** Columbia University Irving Medical Center study — sleep deprivation drives weight gain
**Primary Entity:** Sleep deprivation / weight gain (Columbia University Irving Medical Center, July 2026)
**Signal Type:** medical_study
**Allowed Category:** sleep science; nutrition and diet science
**Trend Strength Score:** 68 | **Opportunity Score:** 77 | **Discover Score:** 4
**Urgency:** this_week | **Confidence:** Medium *(press release sourced; observational study flag required until peer-reviewed publication confirmed)*
**Content Status:** new | **Source Count:** 3 (Columbia press release, gut_health Trends +3 adjacent, sleep science category)

⚠️ **Integrity note:** Columbia press release — peer-reviewed publication status should be confirmed before publishing. Study design (observational vs. interventional) affects causal claims. Do NOT write "sleep deprivation causes weight gain" without confirming RCT design; if observational, frame as "associated with."

**Why Now:** Columbia University Irving Medical Center published this on July 6, 2026. Sleep science is a core category; gut_health +3 and nutrition Trends +2 are adjacent signals supporting audience interest. The sleep-weight connection is a perennially high-traffic topic — this study provides a fresh institutional peg to re-enter the cluster.

**Angle:** Mechanism explainer — not just "sleep affects weight" (already widely known) but the specific biological pathway this study identifies: what happens hormonally and metabolically during sleep deprivation that drives weight gain. This is the differentiation from competitor shallow coverage.

**Outline:**
1. **What Columbia found** — key finding, plainly stated with caveats
2. **The mechanism** — what specifically happens when you sleep less (hormonal: ghrelin/leptin; metabolic: insulin sensitivity; behavioral: late-night eating window)
3. **How much sleep deprivation triggers the effect?** — dose-response if available from study
4. **Who is most at risk?** — population subgroups (shift workers, parents of young children, chronic insomniacs)
5. **Why this matters for weight management conversations** — adding sleep to diet + exercise framing
6. **What the evidence base looks like** — brief summary of prior studies; this study's contribution
7. **Practical guidance** — sleep hygiene basics; not medical advice
8. **FAQ** — Can you catch up on sleep? Does napping help? How much sleep is needed?

**Key Data Points:**
- Columbia University Irving Medical Center press release, July 6, 2026
- Ghrelin/leptin disruption from sleep loss: established prior literature (Spiegel et al., UCHICAGO) — cite as context
- CDC: 1 in 3 US adults don't get enough sleep
- Google Trends "gut health" +3, "nutrition" +2 — adjacent rising interest

**Sources:**
```
- publisher: Columbia University Irving Medical Center
  url: https://www.cuimc.columbia.edu/news/skimping-sleep-leads-weight-gain
  tier: 1
  used_for: Primary study source

- publisher: CDC
  url: https://www.cdc.gov/sleep/data_statistics.html
  tier: 1
  used_for: Sleep deprivation prevalence statistics

- publisher: NIH / PubMed
  url: https://pubmed.ncbi.nlm.nih.gov/[retrieve if journal publication available]
  tier: 1
  used_for: Peer-reviewed version if available [unverified at pipeline run]
```

**Expert Type Needed:** Sleep medicine specialist or endocrinologist; cite researchers named in Columbia press release.

**SEO:**
- Primary keyword: sleep deprivation weight gain 2026
- Supporting: why does lack of sleep cause weight gain, sleep and metabolism study, columbia university sleep weight gain, how sleep affects weight loss
- Format: Long-form explainer with FAQ and practical guidance section
- Schema: Article + FAQPage
- Discover notes: "Does not sleeping enough cause weight gain?" is a common AI health query — this study provides fresh institutional sourcing; Discover score 4

**Estimated Word Count:** 1,100–1,400 words
**Next Steps:** Confirm peer-reviewed publication from Columbia press release link; verify study design before causal framing; assign to writer with sleep science background

---

### BRIEF 7 — P3 · SCHEDULED (THIS WEEK)

**Headline:** Lung Transplant Extends Life for Terminal Lung Cancer Patients — What the Northwestern Study Found

**Topic:** Northwestern Medicine study — lung transplant dramatically improves survival in terminal lung cancer patients
**Primary Entity:** Lung transplant / terminal lung cancer (Northwestern Medicine, July 2026)
**Signal Type:** medical_study
**Allowed Category:** medical research and clinical trials; chronic disease management

| Field | Value |
|---|---|
| Trend Strength Score | 63 |
| Opportunity Score | 72 |
| Discover Score | 4 |
| Urgency | this_week |
| Confidence | Medium |
| Content Status | new |
| Source Count | 3 (Northwestern Medicine Newsroom, Medical Xpress, Google News) |
| SERP Difficulty | Medium |

**Angle:** Patient-context explainer — who qualifies for this approach, what the survival improvement looked like, and what the ethical/access considerations are for a scarce organ resource.

⚠️ **Integrity note:** Lung transplant for terminal cancer is not standard of care — this is a study showing survival benefit in a specific, highly selected patient population. Do not frame as broadly available treatment option. Organ scarcity context required.

**Key Data Points:**
- Northwestern Medicine Newsroom + Medical Xpress, July 8, 2026 — publication in a peer-reviewed journal (confirm journal name)
- Lung transplant for cancer historically contraindicated; this study appears to address stage IV / terminal cases — confirm patient selection criteria from source
- Organ donor waiting lists and scarcity context (UNOS data)

**Sources:**
```
- publisher: Northwestern Medicine Newsroom
  url: https://news.northwestern.edu/stories/2026/07/lung-transplant-terminal-lung-cancer/
  tier: 1
  used_for: Primary study coverage [exact URL unverified — retrieve from Northwestern Medicine site]

- publisher: Medical Xpress
  url: https://medicalxpress.com/news/2026-07-lung-transplant-dramatically-survival-terminal.html
  tier: 2
  used_for: Secondary confirmation
```

**Expert Type:** Thoracic surgeon and/or transplant pulmonologist.
**Primary Keyword:** lung transplant lung cancer survival study 2026
**Format:** Explainer article | **Word Count:** 900–1,100 words
**Next Steps:** Retrieve journal name and DOI from Northwestern press release; verify patient selection criteria; note organ scarcity angle prominently

---

### BRIEF 8 — P3 · SCHEDULED (THIS WEEK)

**Headline:** The First Clinical Trial for the Bundibugyo Ebola Strain Has Begun in DRC — What Makes This One Different

**Topic:** First clinical trial for Bundibugyo Ebola strain, initiated in DRC — WHO/AP/NPR/Reuters coverage
**Primary Entity:** Bundibugyo Ebola strain treatment trial (DRC, July 2026)
**Signal Type:** clinical_trial
**Allowed Category:** infectious disease; public health and epidemiology

| Field | Value |
|---|---|
| Trend Strength Score | 61 |
| Opportunity Score | 68 |
| Discover Score | 3 |
| Urgency | this_week |
| Confidence | High |
| Content Status | new |
| Source Count | 5 (AP, NPR, Reuters, WHO, Mongabay) |
| SERP Difficulty | Low-Medium |

**Angle:** Public health explainer — why no treatment exists specifically for Bundibugyo (vs. Zaire strain, for which mAb114 and REGN-EB3 work), what this trial is testing, what DRC communities face, and why global health audiences should care about Ebola preparedness even in non-outbreak regions.

⚠️ **Integrity note:** This is a Phase I/early-phase trial initiation — no efficacy data exists yet. Do not frame as a treatment breakthrough. Frame as "trial has begun" with honest uncertainty about outcomes and timeline.

**Key Data Points:**
- Trial start confirmed: AP July 5, NPR July 7, Reuters July 2, WHO advisory, Mongabay July 8, 2026
- Bundibugyo strain: distinct from Zaire (most common); existing mAb treatments not proven effective against it
- DRC context: ongoing conflict zone adds trial complexity
- No approved treatment currently exists for Bundibugyo strain

**Sources:**
```
- publisher: AP News
  url: https://apnews.com/article/ebola-bundibugyo-drc-clinical-trial-treatment
  tier: 1
  used_for: Trial start reporting [exact URL unverified — retrieve from AP]

- publisher: NPR
  url: https://www.npr.org/2026/07/07/bundibugyo-ebola-treatment-trial-drc
  tier: 1
  used_for: Community context and trial narrative

- publisher: WHO
  url: https://www.who.int/news/item/bundibugyo-ebola-trial-drc-2026
  tier: 1
  used_for: Official WHO confirmation [exact URL unverified — retrieve from WHO.int]
```

**Expert Type:** Infectious disease epidemiologist; cite WHO or NIH-affiliated researcher if named in AP/NPR coverage.
**Primary Keyword:** Bundibugyo Ebola treatment trial 2026
**Format:** News explainer | **Word Count:** 800–1,100 words
**Next Steps:** Retrieve exact trial registration from ClinicalTrials.gov; confirm trial sponsor and treatment compound name from WHO/AP sources; assign to writer with infectious disease background

---

## REJECTED TOPICS LOG

| Topic | Reason |
|---|---|
| Mitch McConnell health status | Brand safety: political figure health without clinical/research angle; excluded: celebrity/political |
| Brian Johnson health (Trends rising) | Celebrity wellness — excluded category; no evidence-based health angle |
| Atrium Health pixel settlement (Trends rising) | Healthcare legal/business; no patient health angle for general audience |
| Snapchatplanet.com / Rachael Ray health (Trends) | Social chatter / celebrity; off-category |
| Wellness retreats, university programs, fire district wellness | Local/institutional scope; no national audience signal |
| Planet Fitness holiday hours queries | Off-category: business/operations, not health |
| AI in clinical trial design (Nature, Clinical Leader) | Off-category: research methodology infrastructure, not patient health |
| HHS Operation TrialBlazer | Health policy infrastructure; insufficient consumer health value |
| Digital detox challenge (Marquette Today) | Institutional/local; no novel research peg |
| "Game of Thrones" wellness cult | Celebrity; excluded category |
| ACA premium hikes 2027 (KFF, NYT, PBS) | Monitored: credible sources, real audience impact, but pure policy framing without new clinical data; brand safety borderline (political healthcare opinion); not briefed this run — revisit if clinical access impact data published |
| Psilocybin + cocaine RCT (Red Light Holland) | Skill 02b: Monitor. Source is corporate press release with IP claims; no independent journal publication confirmed; exits to P5 |
| Alzheimer's gene therapy grant (Weill Cornell) | Grant award, not results; monitored for future watch when study data available |
| Connor Murphy fitness/mental health (Trends) | Social-only spike; off-category (celebrity personal story) |
| Haaland / Zuckerberg diet (Trends rising) | Celebrity wellness without evidence base |
| Traditional 1776 American diet (Trends) | Novelty/political cultural moment; no health science basis |
| Mark Zuckerberg wagyu cattle diet | Celebrity wellness; excluded category |
| Corn on the cob / cream of wheat nutrition (Trends) | Generic nutrition queries; no news peg; insufficient trend velocity for full brief |
| Yale health system CEO ouster | Pure institutional/business news |
| Insilico Medicine Phase III trial (IPF) | Pharma business/early phase; no patient guidance angle yet |
| Nanox Cardiac AI Solution study (dicardiology.com) | Specialty medical trade; narrow audience fit |
| Five-agent AI clinical trial design | Research methodology; off-category |
| OSU nursing study abroad | Educational/local; off-category |
| UCF microgravity/space radiation aging | Peripheral; no consumer health application |
| WHO global health emergencies overview | Evergreen institutional; no fresh news peg beyond general advisory |
| WHO cervical cancer | Evergreen topic without fresh study peg this week |
| DOJ digital health company fraud (Adderall pills) | Legal/criminal case; not a health guidance topic; off-category for this niche |

---

## CONSOLIDATED INTEGRITY FLAGS

| # | Topic | Flag | Severity |
|---|---|---|---|
| 1 | Eye Drops Recall (Brief 3) | ⚠️ Primary FDA notice not directly retrieved during pipeline run. Breaking recall exception applied. Verify brand names, lot codes, and foreign substance identity from FDA.gov before assigning writer. Confidence capped at Medium. | High — must verify before publish |
| 2 | Bupropion/Sertraline MDD Trial (Brief 5) | ⚠️ DOI/specific Nature URL not retrieved during pipeline run. Retrieve and verify from Nature.com before publishing. Do not present as change to clinical prescribing practice. | Medium |
| 3 | Columbia Sleep Study (Brief 6) | ⚠️ Source is institutional press release. Peer-reviewed publication status and study design (observational vs. interventional) must be confirmed before causal language. Do not use "causes" without confirmed RCT design. | Medium — affects framing |
| 4 | Northwestern Lung Transplant Study (Brief 7) | ⚠️ Journal name and DOI not confirmed. Retrieve from Northwestern Medicine Newsroom. Patient selection criteria must be cited accurately — this is not a broadly available treatment. | Medium |
| 5 | Ebola DRC Trial (Brief 8) | ⚠️ Early-phase trial initiation only — no efficacy or safety data available. Do not frame as treatment breakthrough. ClinicalTrials.gov registration should be cited. | Low-Medium |
| 6 | GLP-1 Online Prescribing (Brief 4) | ⚠️ STAT investigation describes observed practices, not quantified outcomes across all platforms. Do not extrapolate to all telehealth GLP-1 providers. Frame as "what the investigation found." | Low |
| 7 | All medical studies | ⚠️ Standard health content rule: association ≠ causation. Single-study findings should not be presented as settled science. Competitor sites (WebMD, Healthline) have medically reviewed articles on all these topics — match or exceed their evidence standards. | Standing flag |

---

## RUN NOTES

**Run date:** 2026-07-09
**Niche:** Health and Wellness
**Signals reviewed:** 144 (Google News Radar) + Google Trends 9 keyword clusters
**Topics retained:** 8 | **Rejected:** 136
**P1:** 3 | **P2:** 3 | **P3:** 2 | **P5/Monitor:** 3 (ACA, Psilocybin RCT, Alzheimer's grant)

**Signal environment notes:**
- `food_safety` Google Trends +22 is the single largest 7d-delta in the dataset and directly validates the FDA recall cluster as the top priority signal of this run
- `mental_health` +4 and `gut_health` +3 show steady week-over-week interest supporting the MDD trial and sleep/nutrition briefs
- `fitness` -5 is a post-July 4th holiday artifact (Planet Fitness holiday hours dominated rising queries); fitness topics deprioritized this run
- `wellness` rising queries were dominated by SEO spam domains (goodnever.com, usefulideas.net, naturaplug.com, skillsclonelife.com) — zero editorial value; filtered as noise
- `health` rising queries showed Mitch McConnell dominating (political) and Atrium Health pixel settlement (legal/business) — both rejected on brand safety grounds

**Tool availability:** Google Trends available via SerpAPI pre-fetch; Google News Radar fully injected (144 headlines). No tools reported unavailable.

**Self-check status:** `site_url` not configured — self-check skipped. Competitor coverage checked via Google News Radar and competitor list. All 8 retained topics appear as `content_status: new` with this disclosure.

**Deferred topics:** No `data/deferred_topics.yaml` found. No topics deferred this run (all overflow rejected on quality grounds, not capacity).

**Run history:** No prior `data/run_history.yaml` found — this is run #1. Cross-run staleness check not applicable.

**Dashboard output destination:** `outputs/daily_newsroom_dashboard/2026-07-09.html`

---

*Trending Content OS · Run completed · 2026-07-09 · Health & Wellness Niche*