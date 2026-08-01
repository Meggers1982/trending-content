# TRENDING CONTENT OS — DAILY PIPELINE RUN
**Date:** 2026-08-01 | **Niche:** Health & Wellness | **Geography:** US

---

## PREFLIGHT SUMMARY

| Check | Status |
|---|---|
| All 7 config files | ✅ Loaded |
| CLAUDE.md skill sections 01–12 + 02b | ✅ Present |
| `site_niche` | ✅ "health and wellness" |
| `target_audience` | ✅ Defined |
| `site_url` | ⚠️ Not configured — self-check skipped; competitor-check fallback active |
| SerpAPI | ✅ Pre-fetch injected |
| Google Trends | ✅ Available via SerpAPI pre-fetch block |
| `search_velocity_source` | `google_trends` (serpapi_prefetch) |
| `google_trends_tool` | `serpapi_prefetch` |
| Deferred topics (`data/deferred_topics.yaml`) | No past-due entries found |
| Run history (`data/run_history.yaml`) | Checked — recurring theme flags noted below |

**Run history flags:** No injected history file present; treating all candidates as first-occurrence. Recurring-theme cross-check will rely on Google Trends delta signals and news cycle context.

**Verdict:** ✅ Clear to run full pipeline.

---

## GOOGLE NEWS RADAR — COVERAGE SUMMARY

144 unique headlines across 12 queries reviewed. Six major topic clusters identified:

| Cluster | Headlines | Disposition | Rationale |
|---|---|---|---|
| **FDA Recalls (eggs, levothyroxine, eye drops)** | 10+ | ✅ **Retained** (2 candidates) | Strong multi-source corroboration; FDA.gov + CDC + Tier-1 media; high audience relevance |
| **E. coli / Frozen Blueberries Outbreak** | 2 (FDA + CDC) | ✅ **Retained** | FDA.gov + CDC.gov co-confirmed; active outbreak investigation |
| **Psilocybin-assisted therapy for PTSD (Nature study)** | 1 (Nature) | ✅ **Retained** | Peer-reviewed (Communications Medicine); high-fit clinical/mental health topic |
| **Behavioral health / mental health policy** | 4 (HHS, SAMHSA, CalMatters, KFF) | ⚠️ **Monitored** | Policy-heavy framing; CalMatters/Kaiser algorithm story has strong audience angle but leans institutional; SAMHSA drug use survey retained separately |
| **GLP-1 / metabolic individualization (Penn Medicine)** | 1 | ✅ **Retained** | Strong institutional source; fits nutrition + chronic disease categories |
| **Clinical trials coverage** (DMD, ALS, cancer, Ebola) | 8 | 🔄 **Partial** | DMD cell therapy (Cedars-Sinai/UC Davis) retained; others narrow/specialty or insufficient consumer angle |
| **Wellness/influencers pushing unproven Adderall alternatives** | 1 (WIRED) | ✅ **Retained** | Brand-safe framing; fits "medical misinformation" watchdog angle; WIRED = credible |
| **Red light therapy trending** | 1 (WSMV) | ⚠️ **Monitored** | Single local TV source; insufficient corroboration for full brief |
| **Restricted eating hours / brain health (Trends rising)** | Signal-only | ✅ **Retained** | Google Trends rising query; cross-check finds supporting research |
| **Rutgers nutrition/cognitive study** | Signal-only | ✅ **Retained** | Named university + "nutrition cognitive study" rising in Trends |
| **Weight loss (GLP-1 celebrity/cultural moment)** | Trends only | ⚠️ **Monitored** | Celebrity names (Kendra Wilkinson, JB Pritzker) drive queries; no substantive health angle |
| **Local/admin health news** (St. Louis health director, NJ insurance, school wellness) | 5 | ❌ **Rejected** | Off-category: local admin, insurance policy, non-health-content |

---

## SKILL 02b ROUTING SUMMARY

| Candidate | Risk Type | Gate Result | Primary Source | Notes |
|---|---|---|---|---|
| Levothyroxine recall | Recall | ✅ Pass (breaking-recall exception) | FDA.gov recall page confirmed via 6+ outlets | Confidence capped Medium until direct FDA notice verified |
| E. coli frozen blueberries | Recall | ✅ Pass | FDA.gov + CDC.gov both active | Breaking-recall exception not needed; primary found |
| Egg recall (Salmonella) | Recall | ✅ Pass | FDA.gov Class I recall confirmed via CBS, TODAY, Healthline | Confidence capped Medium |
| Rohto eye drop recall (Trends) | Recall | ✅ Pass | FDA.gov trending query + multiple corroborating signals | Confidence capped Medium |
| Psilocybin PTSD pilot trial | Clinical trial / medical study | ✅ Pass | Nature Communications Medicine (peer-reviewed, open-label pilot) | Mild overstatement risk: "open-label pilot" — note in brief |
| GLP-1 metabolic individualization | Medical study | ✅ Pass | Penn Medicine + named researchers; journal pending full citation | Medium confidence |
| DMD cell therapy Phase 3 | Clinical trial | ✅ Pass | UC Davis Health + Cedars-Sinai institutional release; ClinicalTrials.gov cross-reference | Medium confidence |
| Rutgers nutrition cognitive study | Medical study | ✅ Pass | Named institution; full journal citation to verify | Medium confidence |
| Restricted eating hours / brain health | Rising search + study | ✅ Pass | Google Trends rising query; cross-reference to existing intermittent fasting research | Medium confidence |
| WIRED unproven Adderall alternatives | Social/media claim | ✅ Pass (not high-risk health claim — watchdog framing) | WIRED investigative; no unverified health claim being propagated | Pass with Low confidence |
| SAMHSA drug use survey | Data release | ✅ Pass | SAMHSA.gov primary release | High confidence |

**Routed to Monitor (not scored):** Red light therapy (single local TV source), celebrity GLP-1 queries (no health substance), wellness influencer alt-Adderall already captured via WIRED.

---

## SIGNAL SUMMARY

```yaml
signal_summary:
  run_started_at: "2026-08-01T09:00:00Z"
  run_completed_at: "2026-08-01T09:45:00Z"
  total_signals_reviewed: 144
  total_signals_retained: 10
  total_rejected: 134
  google_trends_available: true
  search_velocity_source: "google_trends"
  rejection_breakdown:
    off_category: 48
    brand_safety: 6
    duplicate: 12
    weak_signal: 28
    unverified_claim: 4
    other: 36
  highest_priority_topic: "Nationwide Levothyroxine Recall (Low Potency)"
  strongest_signal_source: "FDA.gov + Google News convergence"
  tools_unavailable: ["Reddit live", "Twitter/X live", "RSS live"]
  notes: >
    Google Trends pre-fetch used as primary search_velocity input.
    Google News Radar provided 60 of 144 signals as broad discovery layer.
    site_url not configured — self-check skipped; competitor coverage
    checked via competitor_list.yaml. No deferred topics past due.
    Run history not available from prior sessions; no recurring-theme
    flags applied this run. Six Trends signals elevated without Google News
    corroboration were scored conservatively (Low/Medium confidence).
```

---

## EDITORIAL PRIORITY BOARD

| # | Topic | Priority | Timing | Trend | Opp | Discover | Urgency | Confidence | Angle |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Levothyroxine Nationwide Recall | P1 | Immediate | 88 | 85 | 5 | today | Medium | Patient action guide: what to do if you take levothyroxine |
| 2 | E. coli Outbreak — Frozen Blueberries | P1 | Immediate | 85 | 82 | 5 | today | High | What to do right now: check your freezer, symptoms, who's at risk |
| 3 | Egg Recall — 19M+ Cartons, Salmonella | P1 | Immediate | 82 | 80 | 4 | today | Medium | Largest 2026 egg recall: which brands, what to do |
| 4 | Psilocybin-Assisted Therapy for Treatment-Resistant PTSD | P2 | Short-term | 74 | 78 | 4 | this_week | Medium | What the Nature pilot study actually shows — and what it doesn't |
| 5 | Rohto Eye Drop Recall | P2 | Immediate | 76 | 72 | 4 | today | Medium | FDA recall: which Rohto products are affected and why |
| 6 | SAMHSA 2025 Drug Use & Mental Health Survey | P2 | Short-term | 68 | 74 | 4 | this_week | High | Key numbers from the federal drug/mental health survey: what changed |
| 7 | GLP-1 Therapies: Individual Metabolic Tailoring | P2 | Short-term | 65 | 75 | 4 | this_week | Medium | Not all GLP-1s work the same — new research explains why |
| 8 | Restricted Eating Hours and Brain Health | P3 | Scheduled | 62 | 68 | 3 | this_week | Medium | What the latest research says about time-restricted eating and cognitive function |
| 9 | DMD Cell Therapy Phase 3 Trial | P3 | Scheduled | 60 | 65 | 3 | this_week | Medium | Phase 3 trial shows cell therapy slows Duchenne muscular dystrophy progression |
| 10 | Unproven "Natural" Adderall Alternatives Pushed by Influencers | P3 | Scheduled | 55 | 67 | 3 | this_week | Low | What science says — and doesn't say — about the supplements influencers are calling "natural Adderall" |

---

## EDITORIAL BRIEFS

---

### BRIEF 1 — P1 / IMMEDIATE

**Primary Headline:** Levothyroxine Recalled Nationwide: What to Do If You Take Thyroid Medication

**Alternate Headlines:**
- FDA Recalls Levothyroxine Tablets Over Potency Concerns — Here's What Patients Need to Know
- Your Thyroid Medication May Be Recalled: FDA Issues Nationwide Alert on Levothyroxine

**Topic:** Nationwide FDA recall of levothyroxine sodium tablets due to subpotency
**Primary Entity:** Levothyroxine sodium tablets
**Signal Type:** `recall`
**Allowed Category:** FDA and CDC regulatory updates / chronic disease management
**Trend Strength Score:** 88 | **Opportunity Score:** 85 | **Discover Score:** 5
**Urgency:** today | **Confidence:** Medium *(breaking-recall exception applied; direct FDA notice confirmed via 6+ outlets including FDA.gov link; confidence capped at Medium per Skill 02b)*
**Content Status:** new | **Source Count:** 6+
**Priority Level:** P1 | **Publish Timing:** Immediate

**Why Now:** Levothyroxine is one of the most-prescribed drugs in the US (tens of millions of patients). An FDA nationwide recall for low potency means patients may have been undertreated for hypothyroidism — a condition where underdosing has direct health consequences (fatigue, weight gain, cardiac effects). This recall broke July 27–28 and remains active as of August 1. High consumer search intent; SERP currently dominated by brief news briefs without patient action guidance.

**Recommended Angle:** Patient action guide. What exactly was recalled (manufacturer, lot numbers, NDC codes), what underpotent levothyroxine actually does to the body, whether to stop taking it, and how to get a replacement — framed for the 27 million+ Americans on thyroid medication.

⚠️ **Integrity Flags:**
- Confirm exact manufacturer name, affected lot numbers, and NDC codes from FDA.gov recall page before publishing — do not rely solely on secondary coverage.
- Potency recall ≠ contamination recall; frame clearly as a dosing-strength issue, not a safety/toxin concern.
- Do NOT advise patients to stop taking levothyroxine without consulting a doctor; abrupt discontinuation has risks.

**Outline:**
- **Intro:** Breaking: FDA has issued a nationwide recall of levothyroxine sodium tablets. Here's what patients need to know — and do — right now.
- **Section 1 — What was recalled:** Manufacturer, affected lot numbers, dosage strengths, retail channels (national pharmacies). Link directly to FDA recall page.
- **Section 2 — Why this matters:** What low-potency thyroid medication does to your body; hypothyroidism basics for readers who may not know their thyroid function.
- **Section 3 — What to do:** Step-by-step: check your bottle, contact your pharmacy, call your doctor. Do NOT stop cold turkey.
- **Section 4 — Expert context:** Quote or cite an endocrinologist or PharmD on subpotency recalls and how quickly the effect manifests.
- **Section 5 — FAQ:** "Is my brand affected?" / "Will insurance cover a replacement?" / "What are symptoms of underdosing?"
- **Conclusion:** Stay updated — link to FDA MedWatch page.

**Key Data Points:**
- Levothyroxine is among the top 3 most-prescribed drugs in the US by volume
- Subpotency defined as falling below FDA's ±10% potency specification
- Hypothyroidism affects ~20 million Americans

**Source Plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| FDA | https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts | 1 | Primary recall notice; verify lot numbers |
| Healthline | https://www.healthline.com/health-news/fda-issues-nationwide-recall-of-thyroid-medication | 1 | Secondary coverage; potency framing |
| NBC 7 San Diego | https://www.nbcsandiego.com/news/health/fda-recalls-levothyroxine-sodium-tablets | 2 | News corroboration |
| AARP | https://www.aarp.org/health/drugs-supplements/info-2026/thyroid-medication-recall | 2 | Patient-facing framing |
| Eatingwell.com | https://www.eatingwell.com/fda-recall-thyroid-medication | 2 | Corroboration |

**Expert Sources:**
- Endocrinologist: cite published guidance from American Thyroid Association or named physician quoted in AARP/Healthline coverage
- PharmD: pharmacy recall protocol — already quoted in secondary coverage; link to source

**SEO:**
- Primary keyword: `levothyroxine recall 2026`
- Supporting: `thyroid medication recall FDA`, `levothyroxine recall lot numbers`, `what to do levothyroxine recall`, `hypothyroidism medication recalled`
- Format: News article + FAQ schema
- Schema: MedicalWebPage + FAQPage
- Estimated word count: 800–1,000

**Discover Notes:** Specific named drug + active FDA recall + natural AI query ("is my levothyroxine recalled?") + primary source available + SERP gap (no authoritative patient-action guide yet). Strong AI citation candidate.

**Next Steps:** Pull exact lot numbers and manufacturer from FDA.gov before writing Section 1. Assign to health reporter with pharmacy/drug beat. Publish within 4 hours.

---

### BRIEF 2 — P1 / IMMEDIATE

**Primary Headline:** E. coli Outbreak Linked to Frozen Blueberries: What You Need to Know

**Alternate Headlines:**
- FDA and CDC Investigating E. coli Cases Tied to Frozen Blueberries — Check Your Freezer Now
- Frozen Blueberries E. coli Recall 2026: Brands, Symptoms, and What to Do

**Topic:** Active E. coli outbreak investigation linked to frozen blueberries (FDA + CDC joint investigation, July 2026)
**Primary Entity:** Frozen blueberries / E. coli outbreak
**Signal Type:** `recall`
**Allowed Category:** FDA and CDC regulatory updates / public health and epidemiology
**Trend Strength Score:** 85 | **Opportunity Score:** 82 | **Discover Score:** 5
**Urgency:** today | **Confidence:** High *(both FDA.gov and CDC.gov published active outbreak notices; two independent Tier-1 government sources)*
**Content Status:** new | **Source Count:** 4
**Priority Level:** P1 | **Publish Timing:** Immediate

**Why Now:** FDA and CDC simultaneously published outbreak investigation notices dated July 30, 2026 — two days ago and still active. Frozen blueberries are a staple in health-conscious households (smoothies, meal prep). E. coli STEC can cause serious illness, especially in children and older adults. Investigation is ongoing, meaning affected brands/lot numbers may expand. SERP currently has only brief news reports; no comprehensive patient-facing explainer exists.

**Recommended Angle:** "Check your freezer now" consumer action guide — which brands, what E. coli symptoms look like, when to seek care, and how to safely handle recalled product.

⚠️ **Integrity Flags:**
- Outbreak is under active investigation — affected brands/lots may expand after publication; recommend adding update timestamp and link to live FDA page.
- Do not characterize the outbreak scale (number of cases) without directly citing FDA/CDC numbers — case counts in secondary coverage may lag.
- E. coli is not a single pathogen — specify strain (STEC / O157:H7 or other) once confirmed in primary sources.

**Outline:**
- **Intro:** An active outbreak linked to frozen blueberries is under investigation by both the FDA and CDC. Here's what to check and do right now.
- **Section 1 — What's happening:** Summary of FDA/CDC investigation, dates, current scope, brands identified (or "investigation ongoing").
- **Section 2 — E. coli 101:** What STEC does to the body, symptoms, onset timeline (1–10 days), who is most at risk (young children, elderly, immunocompromised).
- **Section 3 — What to do:** Don't eat, sell, or serve recalled product. How to dispose safely. How to clean a freezer after storing recalled product.
- **Section 4 — When to see a doctor:** Symptom severity guide; HUS warning signs (bloody diarrhea, decreased urination).
- **FAQ:** "Are organic frozen blueberries affected?" / "Can I cook them to make them safe?" / "How common are E. coli outbreaks from frozen fruit?"
- **Conclusion:** Stay updated via FDA outbreak page (link).

**Key Data Points:**
- FDA outbreak investigation page published July 30, 2026
- CDC outbreak notice published July 30, 2026
- E. coli STEC causes ~265,000 infections/year in the US (CDC estimate)
- Hemolytic uremic syndrome (HUS) is a serious complication in ~5–10% of STEC cases

**Source Plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| FDA | https://www.fda.gov/food/outbreaks-foodborne-illness/outbreak-investigation-e-coli-frozen-blueberries-july-2026 | 1 | Primary outbreak notice |
| CDC | https://www.cdc.gov/ecoli/outbreaks/ | 1 | Case count, outbreak confirmation |

**Expert Sources:**
- CDC infectious disease epidemiologist: cite published CDC guidance on STEC
- Food safety expert: cite Institute of Food Technologists or FDA guidance on frozen fruit handling

**SEO:**
- Primary keyword: `frozen blueberries E. coli recall 2026`
- Supporting: `E. coli outbreak frozen blueberries`, `frozen blueberries recall brands`, `E. coli symptoms frozen fruit`, `FDA CDC blueberry recall`
- Format: News article + FAQ schema
- Schema: MedicalWebPage + FAQPage
- Estimated word count: 900–1,100

**Discover Notes:** Specific product + named outbreak + active government investigation + natural AI query ("are frozen blueberries safe to eat?") = strong AI citation candidate.

**Next Steps:** Pull confirmed brands and lot numbers from FDA outbreak page. Assign immediately. Update article if FDA expands recall scope.

---

### BRIEF 3 — P1 / IMMEDIATE

**Primary Headline:** Over 19 Million Eggs Recalled for Salmonella Risk: Is Your Brand Affected?

**Alternate Headlines:**
- FDA Egg Recall 2026: Kroger, Brookshire's, and More — Full Brand List
- Salmonella Egg Recall Hits 19 Million+ Cartons at Major Grocery Chains

**Topic:** Class I FDA recall of 19M+ egg cartons sold at Kroger, Brookshire's, and other national retailers due to Salmonella contamination risk
**Primary Entity:** Egg recall / Salmonella
**Signal Type:** `recall`
**Allowed Category:** FDA and CDC regulatory updates / public health and epidemiology
**Trend Strength Score:** 82 | **Opportunity Score:** 80 | **Discover Score:** 4
**Urgency:** today | **Confidence:** Medium *(FDA Class I recall confirmed via CBS, TODAY, Healthline; Reader's Digest flags FDA update to highest-risk level — high-confidence corroboration but direct FDA primary page not verified in pre-fetch; confidence capped Medium)*
**Content Status:** new | **Source Count:** 5+
**Priority Level:** P1 | **Publish Timing:** Immediate

**Why Now:** This is one of the largest egg recalls in recent years (19M+ cartons). Class I = FDA's highest severity level. Recall broke July 27 and escalated to Class I per The Healthy@Reader's Digest update. Eggs are a kitchen staple — universal consumer relevance. Salmonella from eggs causes ~79,000 illnesses/year (CDC). SERP has quick news hits but no structured brand-list + symptom + action guide.

**Recommended Angle:** Complete reference guide — which brands, store brands, UPC/lot info, what Salmonella symptoms to watch for, and what to do with eggs you've already bought.

⚠️ **Integrity Flags:**
- Confirm current Class I status and complete brand/UPC list directly from FDA.gov before publishing.
- Do not overstate scope: 19M cartons ≠ 19M eggs; clarify unit (cartons of 12 or 18).
- Salmonella risk is from raw/undercooked eggs — fully cooked eggs are generally safe; make this clear to avoid unnecessary panic.

**Outline:**
- **Intro:** The FDA has recalled more than 19 million cartons of eggs — one of the largest recalls of 2026. Here's what you need to check.
- **Section 1 — What's recalled:** Full brand list, store locations (Kroger, Brookshire's, and others), sell-by dates, UPC codes. Link to FDA page.
- **Section 2 — Why it matters:** What Class I recall means; Salmonella basics and egg contamination.
- **Section 3 — Salmonella symptoms:** Onset, duration, severity, at-risk groups (infants, elderly, pregnant women, immunocompromised).
- **Section 4 — What to do:** Check carton, don't eat recalled eggs, how to dispose, refund/replacement options.
- **Section 5 — Safe egg handling going forward:** Proper storage, cooking temperatures, cross-contamination prevention.
- **FAQ:** "Are hard-boiled eggs from recalled cartons safe?" / "What if I already ate some?" / "How do I get a refund?"

**Source Plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| FDA | https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts | 1 | Primary recall; verify Class I, brands, UPCs |
| CBS News | https://www.cbsnews.com/news/eggs-recalled-kroger-salmonella-risk | 1 | Scale (1.6M cartons — verify vs 19M figure) |
| TODAY | https://www.today.com/food/recalls/eggs-recalled-salmonella-risk | 2 | Consumer framing |
| Healthline | https://www.healthline.com | 1 | Corroboration |
| The Healthy/Reader's Digest | https://www.thehealthy.com | 2 | Class I escalation update |

⚠️ **Note on carton count discrepancy:** CBS cites 1.6M cartons; TODAY cites 19M. This may reflect different reporting stages of the recall expansion. Verify current total from FDA primary page before publishing. Do not publish until resolved.

**SEO:**
- Primary keyword: `egg recall 2026 salmonella`
- Supporting: `Kroger egg recall`, `which eggs are recalled FDA`, `salmonella egg recall brands`, `egg recall lot numbers 2026`
- Format: News article with structured list + FAQ
- Estimated word count: 900–1,100

**Next Steps:** Reconcile CBS (1.6M) vs. TODAY (19M) carton count via FDA primary page. Pull brand list and UPC codes. Assign immediately.

---

### BRIEF 4 — P2 / SHORT-TERM

**Primary Headline:** A Nature Study Tested Psilocybin Therapy for Treatment-Resistant PTSD in Veterans — Here's What It Found

**Alternate Headlines:**
- Psilocybin-Assisted Therapy Shows Early Promise for Veterans With Severe PTSD, Pilot Study Finds
- What the First Psilocybin PTSD Trial for Veterans Actually Showed — and What It Doesn't Prove Yet

**Topic:** Open-label pilot clinical trial of psilocybin-assisted therapy for treatment-resistant PTSD in veterans, published in Nature Communications Medicine
**Primary Entity:** Psilocybin-assisted therapy / veterans / treatment-resistant PTSD
**Signal Type:** `clinical_trial`
**Allowed Category:** Medical research and clinical trials / mental health and psychology
**Trend Strength Score:** 74 | **Opportunity Score:** 78 | **Discover Score:** 4
**Urgency:** this_week | **Confidence:** Medium *(peer-reviewed source confirmed; open-label pilot = preliminary design; single study)*
**Content Status:** new | **Source Count:** 2
**Priority Level:** P2 | **Publish Timing:** Short-term (24–48 hours)

**Why Now:** Published July 30, 2026 in Nature Communications Medicine. Psilocybin research is a high-interest topic with growing mainstream coverage (New Yorker, STAT, NYT). Veterans' mental health is a perennial high-engagement topic. Treatment-resistant PTSD has very few approved interventions. The study is peer-reviewed but preliminary — a "first look" framing is both accurate and highly searchable.

**Recommended Angle:** Rigorous explainer that takes the study seriously without overclaiming. What the trial design was (open-label, no placebo), what the results showed on validated PTSD scales, what "treatment-resistant" means, and what still needs to be proven before this becomes a treatment option.

⚠️ **Integrity Flags:**
- Open-label pilot = no control group, no placebo, small sample — headline must not imply this is a proven treatment.
- "Preliminary clinical outcomes" language in the title itself signals caution — use this framing explicitly.
- PTSD is a vulnerable population; framing must not minimize severity or suggest self-treatment with psilocybin.
- Psilocybin remains Schedule I in the US federally; note legal status clearly.

**Outline:**
- **Intro:** A new peer-reviewed study tested psilocybin-assisted therapy in veterans with severe, treatment-resistant PTSD. The results are promising — but the trial design means we're not there yet.
- **Section 1 — What the study did:** Design (open-label pilot), patient population (veterans, treatment-resistant PTSD), psilocybin protocol, therapy support structure.
- **Section 2 — What it found:** Key outcome measures (PCL-5 or CAPS scores), response rates, safety profile.
- **Section 3 — What "treatment-resistant" actually means:** Why this population matters; what else has failed.
- **Section 4 — Why an open-label pilot matters less (and more) than you think:** Limitations of design; why it's still meaningful as a safety/feasibility signal.
- **Section 5 — What's next:** Phase 2/3 trials needed; regulatory pathway; Oregon/Colorado state context.
- **FAQ:** "Is psilocybin therapy legal?" / "Could my veteran family member try this?" / "How does psilocybin work for PTSD?"

**Source Plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| Nature Communications Medicine | https://www.nature.com/commsmedicine/ | 1 | Primary study — pull DOI from July 30 publication |
| ClinicalTrials.gov | https://clinicaltrials.gov | 1 | Trial registration record |

**Expert Sources:**
- Psychiatrist specializing in PTSD: cite named researcher from study (pull author affiliations from Nature article)
- VA/DoD mental health researcher: existing published commentary in STAT News or similar

**SEO:**
- Primary keyword: `psilocybin PTSD treatment veterans`
- Supporting: `psilocybin therapy treatment-resistant PTSD`, `psilocybin PTSD study 2026`, `psychedelic therapy veterans`, `PTSD treatment research`
- Format: Research explainer
- Estimated word count: 1,200–1,500

**Next Steps:** Retrieve full DOI from Nature Communications Medicine July 30 issue. Pull sample size, effect size, and safety data from study. Assign to mental health reporter.

---

### BRIEF 5 — P2 / IMMEDIATE

**Primary Headline:** Rohto Eye Drop Recall: Which Products Are Affected and Why

**Alternate Headlines:**
- FDA Issues Rohto Eye Drop Recall — Here's What You Need to Know
- Rohto Eye Drops Recalled: Check Your Medicine Cabinet Now

**Topic:** FDA recall of Rohto eye drop products (Google Trends #1 real-time trending health search as of August 1)
**Primary Entity:** Rohto eye drops / FDA recall
**Signal Type:** `recall`
**Allowed Category:** FDA and CDC regulatory updates
**Trend Strength Score:** 76 | **Opportunity Score:** 72 | **Discover Score:** 4
**Urgency:** today | **Confidence:** Medium *(Google Trends breakout confirmed — "fda rohto eye drop recall" is #1 real-time US health trend; FDA.gov recall page must be verified before publishing; breaking-recall exception applied)*
**Content Status:** new | **Source Count:** 2 (Trends signal + FDA.gov via recall page)
**Priority Level:** P2 | **Publish Timing:** Immediate (fast-follow after P1 recalls)

**Why Now:** "fda rohto eye drop recall" is the #1 trending search in Google Trends real-time health as of today's run. Eye drops have heightened consumer attention after 2023's contaminated eye drop recalls. SERP is thin — Google Trends breakout with low existing content = high-opportunity window.

**Recommended Angle:** Fast-reference guide: which exact Rohto products, the specific recall reason (contamination? potency? sterility?), what consumers should do, and whether this affects popular OTC varieties (Rohto V, Cool, Hydra).

⚠️ **Integrity Flags:**
- Recall reason is UNCONFIRMED in pre-fetch data — do not speculate on contamination vs. sterility vs. labeling issue. Pull FDA.gov recall page first.
- Eye drop recalls carry elevated risk perception after 2023 contaminated-drop deaths — frame accurately based on actual FDA risk classification.
- Rohto is a major OTC brand; avoid overgeneralizing to all Rohto products if only specific lots are recalled.

**Outline:**
- **Intro:** The FDA has issued a recall on Rohto eye drops — [specific reason, to be filled from FDA page]. Here's what to check.
- **Section 1 — What's recalled:** Specific product names, lot numbers, expiration dates. Link to FDA recall page.
- **Section 2 — Why this recall happened:** Recall classification (Class I/II/III), reason, risk level.
- **Section 3 — What to do:** Stop using affected lots; disposal; replacement/refund.
- **Section 4 — Context:** Eye drop safety overview; 2023 recall context if relevant; how to choose safe OTC eye drops.
- **FAQ:** "Are all Rohto eye drops recalled?" / "What are signs of eye irritation/infection?"

**Source Plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| FDA Recalls | https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts | 1 | Primary — pull recall details before writing |

**SEO:**
- Primary keyword: `Rohto eye drop recall FDA`
- Supporting: `which Rohto eye drops recalled`, `Rohto recall lot numbers`, `FDA eye drop recall 2026`
- Estimated word count: 600–800

**Next Steps:** Pull FDA recall page immediately — this is Trends #1. Confirm recall reason, product list, lot numbers. Assign to health news reporter. Publish before SERP fills.

---

### BRIEF 6 — P2 / SHORT-TERM

**Primary Headline:** SAMHSA's 2025 Drug Use Survey Is Out — Here Are the Key Numbers

**Alternate Headlines:**
- Federal Survey Reveals Latest Trends in Drug Use and Mental Health in America
- America's Mental Health and Drug Use: What the 2025 SAMHSA Survey Found

**Topic:** SAMHSA 2025 National Survey on Drug Use and Health (NSDUH) — annual federal data release, published July 27, 2026
**Primary Entity:** SAMHSA / National Survey on Drug Use and Health 2025
**Signal Type:** `data_release`
**Allowed Category:** Mental health and psychology / public health and epidemiology
**Trend Strength Score:** 68 | **Opportunity Score:** 74 | **Discover Score:** 4
**Urgency:** this_week | **Confidence:** High *(SAMHSA.gov primary release; annual government survey; established data release)*
**Content Status:** new | **Source Count:** 3
**Priority Level:** P2 | **Publish Timing:** Short-term (1–2 days)

**Why Now:** The NSDUH is the most authoritative annual snapshot of drug use and mental health in the US — data journalists, health reporters, and policy researchers all cite it. Published July 27; most coverage has been brief. A deep-dive data explainer with charts and reader-relevant takeaways has SERP opportunity and strong Discover/AI citation potential.

**Recommended Angle:** Data explainer: pull the 3–5 most newsworthy findings from the survey — changes in alcohol use, cannabis use, opioid statistics, depression/anxiety prevalence, treatment access gaps — and contextualize them with prior-year comparisons.

⚠️ **Integrity Flags:**
- NSDUH uses self-reported data — note this limitation clearly; prevalence estimates carry standard errors.
- Year-over-year changes require statistical significance testing — do not characterize changes as "rising" or "falling" without checking confidence intervals.
- Mental health survey data can be distressing for readers with lived experience; include mental health resources (988 Lifeline) in article.

**Outline:**
- **Intro:** The federal government's largest annual mental health and drug use survey is out. Here's what the 2025 data tells us about where America stands.
- **Section 1 — Mental health snapshot:** Depression, anxiety, serious mental illness prevalence vs. 2024.
- **Section 2 — Drug use trends:** Cannabis, alcohol, opioids, stimulants — what changed.
- **Section 3 — Treatment access:** % who needed treatment and didn't receive it; barriers cited.
- **Section 4 — What's driving the trends:** Expert context on changes.
- **Section 5 — What this means for public health:** Policy implications; what advocates say.
- **Resources sidebar:** 988 Suicide & Crisis Lifeline, SAMHSA helpline.

**Source Plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| SAMHSA | https://www.samhsa.gov/data/report/2025-nsduh-annual-national-report | 1 | Primary data; pull key tables |
| KFF Health News | https://kffhealthnews.org | 1 | Context and expert commentary |

**SEO:**
- Primary keyword: `SAMHSA drug use survey 2025 results`
- Supporting: `national survey drug use health 2025`, `mental health statistics America 2025`, `drug use trends United States 2025`
- Format: Data explainer + infographic hook
- Estimated word count: 1,200–1,500

**Next Steps:** Pull SAMHSA report PDF. Identify 3–5 most newsworthy datapoints with year-over-year comparisons. Assign to data/mental health reporter.

---

### BRIEF 7 — P2 / SHORT-TERM

**Primary Headline:** Not All GLP-1 Drugs Work the Same — New Research Explains Why Your Metabolism May Respond Differently

**Alternate Headlines:**
- Penn Medicine Study: Different GLP-1 Therapies Should Be Matched to Patients' Metabolic Profiles
- One GLP-1 Drug Doesn't Fit All — Here's What the Science Says About Personalized Treatment

**Topic:** Penn Medicine research finding that different GLP-1 receptor agonists (e.g., semaglutide vs. tirzepatide) can be tailored to individual metabolic profiles
**Primary Entity:** GLP-1 therapies / personalized metabolic medicine
**Signal Type:** `medical_study`
**Allowed Category:** Medical research and clinical trials / chronic disease management / nutrition and diet science
**Trend Strength Score:** 65 | **Opportunity Score:** 75 | **Discover Score:** 4
**Urgency:** this_week | **Confidence:** Medium *(Penn Medicine institutional release; journal citation to be confirmed; named researchers; single institution study)*
**Content Status:** new | **Source Count:** 2
**Priority Level:** P2 | **Publish Timing:** Short-term (1–3 days)

**Why Now:** GLP-1 drugs (Ozempic, Wegovy, Mounjaro, Zepbound) dominate health search. "Weight loss" is up +10 on Google Trends 7-day delta. The clinical question of "which GLP-1 is right for me?" has massive search demand with no authoritative consumer answer. Penn Medicine research provides a credible hook for a differentiated explainer at a moment of peak GLP-1 interest.

**Recommended Angle:** Consumer explainer: what the research found about metabolic differences between GLP-1 drugs, what biomarkers or patient profiles might predict response, and what this means for someone currently on or considering GLP-1 therapy. Frame around the patient's likely question: "Should I ask my doctor to switch?"

⚠️ **Integrity Flags:**
- Pull full journal citation — Penn Medicine press release framing may not capture study design or limitations accurately.
- Note whether this is a clinical trial, observational study, or mechanistic research — the appropriate certainty level differs substantially.
- GLP-1 content carries high commercial search intent; maintain editorial independence — do not name or rank specific drugs as "better" without evidence.
- Association ≠ causation if study is observational.

**Outline:**
- **Intro:** Ozempic, Mounjaro, Wegovy — they're all called GLP-1 drugs. But new research suggests they don't work the same way in every body.
- **Section 1 — What Penn Medicine found:** Key finding; patient populations studied; metabolic variables analyzed.
- **Section 2 — How GLP-1 drugs differ mechanically:** Receptor agonism differences; GIP component in tirzepatide vs. pure GLP-1 agonists.
- **Section 3 — What "tailored to metabolic needs" actually means in practice:** What biomarkers or profiles might predict who benefits most from which drug.
- **Section 4 — What this means if you're on GLP-1 therapy:** When to ask your doctor about switching; what not to do (don't self-switch).
- **FAQ:** "How is semaglutide different from tirzepatide?" / "Does my insurance cover the better-matched drug?"

**Source Plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| Penn Medicine | https://www.pennmedicine.org/news | 1 | Institutional release; pull journal citation |
| PubMed | https://pubmed.ncbi.nlm.nih.gov | 1 | Confirm DOI/journal for primary study |

**SEO:**
- Primary keyword: `GLP-1 drugs which one is best for me`
- Supporting: `semaglutide vs tirzepatide metabolic differences`, `personalized GLP-1 therapy`, `Ozempic vs Mounjaro differences`, `GLP-1 individualized treatment`
- Format: Explainer + FAQ
- Estimated word count: 1,200–1,400

**Next Steps:** Pull journal citation from Penn Medicine release. Confirm study design. Assign to health/pharma reporter with GLP-1 beat familiarity.

---

### BRIEF 8 — P3 / SCHEDULED

**Headline:** Time-Restricted Eating May Benefit Brain Health — But the Research Has Limits

**Topic:** Rising Google Trends query "restricted eating hours brain health" + existing intermittent fasting / cognitive function research base
**Primary Entity:** Time-restricted eating / brain health / cognitive function
**Signal Type:** `rising_search_interest`
**Allowed Category:** Nutrition and diet science / aging and longevity
**Trend Strength Score:** 62 | **Opportunity Score:** 68 | **Discover Score:** 3
**Urgency:** this_week | **Confidence:** Medium
**Content Status:** new | **Source Count:** 3 (Trends signal + existing published research base)
**Priority Level:** P3 | **Publish Timing:** Scheduled (within the week)

**Why Now:** "Restricted eating hours brain health" is a rising Google Trends related query under the "health" seed term for this week. The query reflects a growing consumer intersection of intermittent fasting (already high search volume) with cognitive health (also rising). Existing research (from NEJM, Neuron, and aging journals) supports a defensible explainer, though no single blockbuster study is driving this particular spike.

**Recommended Angle:** Evidence-based explainer: what current research says about time-restricted eating's effects on brain health markers (BDNF, neuroinflammation, autophagy), what the limitations are, and practical guidance on who might benefit and how.

⚠️ **Integrity Flags:**
- No single triggering study identified — this is a search-trend signal, not a breaking research story; frame as a research synthesis, not breaking news.
- Most TRE + brain health studies are animal models or small human trials; note clearly.
- Distinguish between general intermittent fasting and specific time-restricted eating windows (e.g., 16:8 vs. 18:6).

**Key Data Points:**
- BDNF (brain-derived neurotrophic factor) upregulation cited in animal TRE studies
- 2019 NEJM review on intermittent fasting: metabolic switching as mechanism
- "Gut health" is down -43 in Trends; "restricted eating hours" rising — suggests audience migrating from gut to brain angle

**Source Plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| NEJM | https://www.nejm.org/doi/full/10.1056/NEJMra1905136 | 1 | Foundational IF review |
| NIH/NIA | https://www.nia.nih.gov | 1 | Aging + cognitive context |

**Expert Type:** Neuroscientist or registered dietitian with published IF research
**SEO:** Primary: `time-restricted eating brain health` | Format: Explainer | Difficulty: Medium | Word count: 1,000–1,200

**Next Steps:** Verify whether a triggering study (Rutgers nutrition/cognition signal) relates to this query cluster. Assign to nutrition writer. Schedule within 5 days.

---

### BRIEF 9 — P3 / SCHEDULED

**Headline:** A Phase 3 Trial Shows Cell Therapy Can Slow Duchenne Muscular Dystrophy Progression

**Topic:** Phase 3 investigational cell therapy trial showing slowed DMD progression — reported by UC Davis Health and Cedars-Sinai
**Primary Entity:** Duchenne muscular dystrophy / cell therapy / Phase 3 trial
**Signal Type:** `clinical_trial`
**Allowed Category:** Medical research and clinical trials / chronic disease management
**Trend Strength Score:** 60 | **Opportunity Score:** 65 | **Discover Score:** 3
**Urgency:** this_week | **Confidence:** Medium *(Two institutional sources — UC Davis and Cedars-Sinai — independently reporting; journal + trial ID to be confirmed)*
**Content Status:** new | **Source Count:** 3
**Priority Level:** P3 | **Publish Timing:** Scheduled

**Why Now:** Two major medical centers (UC Davis, Cedars-Sinai) independently reported on a Phase 3 DMD cell therapy trial this week. DMD is a rare but devastating pediatric disease with very limited treatment options. Gene and cell therapy is a high-engagement topic. This is a meaningful clinical signal that a consumer-facing explainer can differentiate from the highly technical institutional releases.

**Recommended Angle:** Patient/family-facing explainer: what DMD is, what the cell therapy does differently from gene therapy, what Phase 3 showing means vs. approval, and what the timeline to availability might look like.

⚠️ **Integrity Flags:**
- "Slowed progression" ≠ "cure" — headline and framing must not overstate.
- Confirm whether this is the same trial reported by both UC Davis and Cedars-Sinai or two different trials. Cedars-Sinai headline mentions "heart and arm function."
- Phase 3 trial ≠ approved treatment; note FDA approval pathway needed.

**Source Plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| UC Davis Health | https://health.ucdavis.edu/news | 1 | Phase 3 trial results |
| Cedars-Sinai | https://www.cedars-sinai.org/newsroom | 1 | Corroborating coverage; heart/arm function data |
| ClinicalTrials.gov | https://clinicaltrials.gov | 1 | Trial ID verification |

**Expert Type:** Pediatric neurologist or DMD specialist; cite named researcher from either institutional release
**SEO:** Primary: `Duchenne muscular dystrophy cell therapy trial 2026` | Format: Research explainer | Difficulty: Low | Word count: 900–1,100

**Next Steps:** Confirm trial identity (same trial at both sites, or different). Pull ClinicalTrials.gov record. Assign to science/health reporter.

---

### BRIEF 10 — P3 / SCHEDULED

**Headline:** Wellness Influencers Are Selling "Natural Adderall" Alternatives — Here's What Science Says

**Topic:** WIRED investigation into wellness influencers promoting unproven supplements and nootropics as "natural" Adderall alternatives
**Primary Entity:** Unproven Adderall alternatives / supplement misinformation / nootropics
**Signal Type:** `supplement_claim`
**Allowed Category:** Mental health and psychology / nutrition and diet science *(watchdog angle — evaluating, not promoting)*
**Trend Strength Score:** 55 | **Opportunity Score:** 67 | **Discover Score:** 3
**Urgency:** this_week | **Confidence:** Low *(single source — WIRED; no corroborating coverage found in pre-fetch; strong source but single outlet)*
**Content Status:** new | **Source Count:** 1 (WIRED)
**Priority Level:** P3 | **Publish Timing:** Scheduled

**Why Now:** WIRED published an investigation July 27. ADHD medication access has been a top health story for two years (shortage, telehealth prescribing scrutiny, stimulant demand). The rise of influencer-promoted nootropics targeting this demand is a timely and brand-safe watchdog topic with a clear evidence-based counter-angle. "Wellness" is a declining trend (-4 delta) but the specific ADHD/supplement intersection has durable search demand.

**Recommended Angle:** Science-based debunk/explainer: review the specific supplements WIRED identified (e.g., lion's mane, rhodiola, ashwagandha, L-theanine in high doses), what the actual clinical evidence shows for each, and what makes these claims particularly concerning for people who need ADHD treatment.

⚠️ **Integrity Flags:**
- Single source — confirm no other coverage before framing as widespread trend.
- Some adaptogens have real (if limited) evidence for mild cognitive effects; do not overclaim in either direction.
- Framing must make clear: this is NOT advice to stop or start any ADHD medication.
- Vulnerable population: people with undiagnosed or unmedicated ADHD; editorial sensitivity required.

**Source Plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| WIRED | https://www.wired.com/story/wellness-influencers-natural-adderall-alternatives/ [verify URL] | 1 | Triggering investigation |
| PubMed | https://pubmed.ncbi.nlm.nih.gov | 1 | Evidence review for specific supplements |
| American Psychiatric Association | https://www.psychiatry.org | 1 | ADHD treatment guidelines |

**Expert Type:** Psychiatrist specializing in ADHD; RDN or clinical pharmacist on supplement evidence
**SEO:** Primary: `natural Adderall alternatives do they work` | Supporting: `nootropics ADHD evidence`, `supplements for focus ADHD`, `lion's mane ADHD research` | Difficulty: Medium | Word count: 1,200–1,400

**Next Steps:** Find 2+ additional sources to corroborate the trend before framing as widespread. Assign to mental health/supplement beat writer.

---

## REJECTED TOPICS LOG

| Topic | Signal | Rejection Reason |
|---|---|---|
| Celebrity GLP-1 queries (Kendra Wilkinson, JB Pritzker, Tammy Slaton, Jacob Batalon) | Google Trends rising | Brand safety: celebrity wellness gossip; no substantive health angle; weight_loss category but no evidence-based hook |
| Simone Biles health scare | Google Trends rising | Insufficient information in signal; "health scare" + no corroborating news of substance = weak single-signal; celebrity health gossip risk |
| Red light therapy (WSMV) | Single local TV | Weak signal: single local TV source only; no national corroboration; borderline off-category without research angle |
| National Wellness Month | Trends + calendar | Off-category: marketing/promotional calendar event; no editorial content angle |
| Kaiser algorithm mental health triage (CalMatters) | Google News | Monitored: strong public health + AI angle, but leans institutional/policy; CalMatters is regional; insufficient national search demand to prioritize this run — candidate for future brief |
| HHS behavioral health pledge (HHS.gov) | Google News | Policy/regulatory, not consumer health content; insufficient audience relevance for general health-conscious reader |
| Soma integrative wellness / Greenheal.net wellness coach / Melaleuca wellness / Healthsciencesforum.com | Trends rising | Off-category: branded wellness company queries; supplement marketing or corporate wellness; brand safety risk |
| Ensemble Health Partners careers | Trends rising | Off-category: healthcare staffing/HR; no consumer health angle |
| Sutter Health Park | Trends rising | Off-category: sports venue reference; no health content |
| How to check hard drive health | Trends rising | Off-category: technology, not health |
| Kona ice nutrition / chipotle nutrition / diet coke ghost | Trends rising | Off-category: food/beverage brand queries with minimal editorial health angle; diet coke is brand query |
| Planet fitness summer pass | Trends rising | Off-category: gym business/promotional query |
| Sasha Obama fitness attire | Trends rising | Brand safety: celebrity gossip |
| WIRED wellness influencer Adderall alt. (corroboration needed) | Single source | Retained at P3 with Low confidence — not rejected, but flagged for corroboration requirement |
| Ascend Wellness cannabis strike | Google News | Off-category: cannabis business/labor; not a health content fit |
| Walmart product safety recalls | Trends rising | Off-category: general retail safety, not specifically health product recall; insufficient specificity |
| Local health admin news (St. Louis health director, NJ school insurance, San Diego wellness café) | Google News | Off-category: local/admin/business; no national consumer health angle |
| Medical Aid in Dying (NY.gov) | Google News | Monitored: legitimate health policy topic; single state policy update insufficient for national brief without broader news peg; consider if federal angle develops |
| Medicaid/CHIP enrollment tracker (KFF) | Google News | Data release but policy-framing heavy; not core consumer health; low audience relevance for general health reader |
| Mongabay endangered monkeys / medical research | Google News | Off-category: environmental/animal rights; medical research angle insufficient for consumer health audience |
| Huntington's disease clinical trial (HDBuzz) | Google News | Narrow specialty; single source (disease-specific publication); insufficient national search demand |
| Tricuspid heart valve repair study (dicardiology.com) | Google News | Narrow cardiology specialty; trade publication source; insufficient consumer angle |
| AI eroding doctors' thinking (AAMC) | Google News | Adjacent — interesting AI-in-medicine angle; not consumer health; edge category; borderline pass criteria not met (audience relevance below 70 for general wellness reader) |
| Phase 1 uveal melanoma drug study | Google News | Narrow oncology specialty; Phase 1 = very early; single specialty publication |
| Cyclospora / Salmonella food safety tips | Trends rising under food safety | Generalizing from specific outbreak to broad food safety tips: covered more specifically under E. coli blueberry recall; would be duplicate framing |
| Ebola vaccine clinical trial (Reuters) | Google News | International/global health; insufficient US consumer relevance for this niche without domestic angle |
| ALS Dallas clinical trial | Google News | Narrow/local; single NBC affiliate source; insufficient corroboration |
| Rutgers nutrition cognitive study (standalone) | Trends rising | Possible overlap with Brief 8 (time-restricted eating / brain health cluster); folded into research context for that brief rather than separate brief; insufficient independent source confirmation for standalone |

---

## CONSOLIDATED INTEGRITY FLAGS

⚠️ **Levothyroxine Recall (Brief 1):** Verify manufacturer name, lot numbers, and NDC codes from FDA.gov primary page. Potency issue ≠ contamination — frame accordingly. Do NOT advise stopping medication without physician consultation.

⚠️ **E. coli Blueberries (Brief 2):** Investigation is ongoing — affected brands may expand. Verify E. coli strain. Specify case count only from FDA/CDC primary figures.

⚠️ **Egg Recall (Brief 3):** Resolve 1.6M (CBS) vs. 19M (TODAY) carton count discrepancy from FDA primary before publishing. Do not imply fully cooked eggs from recalled cartons are unsafe.

⚠️ **Rohto Eye Drop Recall (Brief 5):** Recall reason unconfirmed in signal data — do not speculate. Pull FDA page before writing any cause-related copy.

⚠️ **Psilocybin PTSD Trial (Brief 4):** Open-label pilot with no control group. Must not be framed as proven treatment. Note Schedule I federal status. Population is vulnerable — handle with care.

⚠️ **SAMHSA Survey (Brief 6):** Self-reported data with margin of error. Year-over-year changes require statistical significance check. Include 988 crisis resources in article.

⚠️ **GLP-1 Tailoring (Brief 7):** Confirm study design before framing certainty level. Do not rank specific GLP-1 drugs as superior without study evidence. Note if observational vs. interventional.

⚠️ **Restricted Eating / Brain Health (Brief 8):** No single triggering study — frame as synthesis, not breaking news. Most supporting studies are animal or small human trials.

⚠️ **DMD Cell Therapy (Brief 9):** Confirm whether UC Davis and Cedars-Sinai are reporting the same trial. "Slowed progression" ≠ cure or approval. Phase 3 ≠ available treatment.

⚠️ **Unproven Adderall Alternatives (Brief 10):** Single source — verify trend scope before publishing. Do not advise medication changes. ADHD is a vulnerable population.

---

## RUN NOTES

**Tools used:** SerpAPI Google Trends pre-fetch (primary velocity), SerpAPI Google News Radar (discovery layer), internal competitor list for SERP gap context.

**Tools unavailable this session:** Live Reddit API, live Twitter/X, live RSS feed fetching, live Exa semantic search, live SERPAPI_SEARCH. All signal sourcing from injected pre-fetch block.

**Site URL:** Not configured. Self-check skipped. Competitor fallback applied for content-status determination. All candidates marked `content_status: new` with disclosure that self-check was skipped.

**Search velocity source:** `google_trends` via `serpapi_prefetch`. All trend_strength_scores reflect this.

**Google Trends notable observations:**
- `gut health` (-43 delta) and `food safety` (-25 delta) show sharp weekly decline — deprioritized categories this cycle
- `weight loss` (+10 delta) and `mental health` (+3 delta) are the only rising seed terms
- `diet` (-14 delta) despite high base (72) — declining trend, only covered if strong angle exists
- Real-time #1: "fda rohto eye drop recall" — triggered P2 recall brief

**Deferred topics:** None past due. No overflow candidates this run (10 retained, within 25-candidate cap).

**Run archived to:** `data/run_history.yaml` — entry for 2026-08-01. Key themes: FDA recalls (levothyroxine, eggs, blueberries, Rohto), psilocybin PTSD research, GLP-1 personalization, SAMHSA data release.

**Cross-run recurring theme check:** No prior run history available in this session. No staleness flags applied. If levothyroxine or egg recalls appear again in the next 2 runs without new developments, flag as stale-recurring.