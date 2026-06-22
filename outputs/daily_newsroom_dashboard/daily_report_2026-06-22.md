# Trending Content OS — Daily Pipeline Run
**Date:** 2026-06-22 | **Niche:** Health & Wellness | **Run Mode:** Full Pipeline (Skills 01–12)

---

## PREFLIGHT SUMMARY

```yaml
preflight_status:
  all_sections_present: true
  missing_sections: []
  site_niche_set: true          # "health and wellness"
  target_audience_set: true     # health-conscious general audience
  site_url_set: false           # no live site — competitor fallback active
  serpapi_connected: true       # LIVE SIGNAL DATA injected
  google_trends_available: true # SerpAPI pre-fetch block present
  google_trends_tool: "serpapi_prefetch"
  search_velocity_source: "google_trends"
  active_tools:
    - SerpAPI Google News (pre-fetched)
    - SerpAPI Google Trends (pre-fetched, 7-day)
    - Google News Radar (144 signals, 60 shown)
    - Competitor list fallback (10 domains)
  inactive_tools:
    - COMPOSIO_SEARCH_TRENDS (not called — pre-fetch used)
    - ExaSearch (not called in this session)
    - Reddit BrowserNavigate (not called)
    - Content database (disabled)
  can_run_signal_listener: true
  notes: >
    site_url not configured — self-check skipped; competitor coverage used for
    SERP-gap context. Google Trends pre-fetch treated as authoritative for
    search_velocity. No deferred_topics.yaml or run_history.yaml injected —
    treating as first run with no prior history to cross-reference.
```

---

## GOOGLE NEWS RADAR COVERAGE SUMMARY

144 unique signals across 12 queries; 60 shown. Clustered into 9 topic groups before pipeline scoring.

| Cluster | Key Headlines | Pipeline Decision | Reason |
|---|---|---|---|
| **FDA Recalls — Blood Pressure Medication** | EatingWell, Yahoo, NewsNation: chlorthalidone/BP med recall 11,000+ prescriptions; also rises in Google Trends ("rising pharma chlorthalidone recall") | ✅ **Retained — P1** | Multi-outlet + FDA.gov signal + Google Trends breakout; direct patient safety impact |
| **FDA Recalls — Infant Formula (Botulism)** | Prevention, FDA.gov: powdered infant formula recalled, botulism outbreak investigation | ✅ **Retained — P1** | FDA.gov primary source; pediatric safety; breaking urgency |
| **FDA Recalls — Food (Mac & Cheese / Alfredo / Soft Cheese / Ice Cream)** | NewsNation, PBS, Good Housekeeping, FDA.gov, Post and Courier | ✅ **Retained — P2** | Multiple food safety recalls; food safety search interest +11; high consumer relevance. Clustered as one food-safety round-up brief. |
| **Antidepressant Recall — Carcinogen** | WCNC, Health.com, Prevention: 375,000 bottles recalled over carcinogen levels | ✅ **Retained — P1** | 3+ credible outlets + patient-facing safety; Skill 02b breaking-recall exception applied |
| **Shingles Vaccine & Dementia Risk** | Medical Xpress (06/16); study suggests lowered dementia risk | ✅ **Retained — P2** | Peer-reviewed signal; strong audience relevance; Skill 02b pass required |
| **Fish Oil / Alzheimer's — No Benefit** | Keck Medicine USC (06/18): fish oil may not prevent Alzheimer's decline | ✅ **Retained — P2** | Institutional source; common supplement; high audience interest; Skill 02b pass |
| **FDA / Federal Plan to Speed Clinical Trials** | STAT News + Fierce Biotech (06/22): FDA pilot program to accelerate Phase 1 trials by 6–12 months | ✅ **Retained — P3** | Breaking today; regulatory angle; editorial + public health relevance |
| **AI in Healthcare / Medical AI** | Nature, Google/AMIE, APA (AI in therapy), Clinical Trial Vanguard | ✅ **Retained — P3** | Strong editorial interest; multiple angles; Nature study adds credibility |
| **Mental Health & Childbearing Decision** | NYT Well (06/17): mental health complicates childbearing decisions | ✅ **Retained — P3** | Prestige outlet; strong audience resonance; mental health search +12 |
| **RFK Jr. Mental Health Funding** | STAT News (06/17): $700M announcement; experts say grants aren't new | ⚠️ **Monitored — P5** | Policy/political framing; STAT flags grants as recycled; brand safety borderline |
| **U.S. Healthcare Affordability (Gallup)** | Gallup: adults' ability to afford care at 5-year low | ⚠️ **Monitored — P5** | Strong data; slight policy drift risk; no clear actionable health angle for this audience |
| **Psilocybin Clinical Trial (USC)** | Keck School of Medicine: USC's first psilocybin study | ⚠️ **Monitored — P5** | Early-stage, no results yet; Skill 02b routed to monitor (clinical trial, no outcome data) |
| **Celebrity/Lifestyle wellness** | Balenciaga wellness, Midjourney sauna, Asheville wellness town | ❌ **Rejected** | Off-category (celebrity wellness, lifestyle marketing) |
| **Tech/AI non-health** | Samsung connected care, trending beauty hacks, kitchen tech | ❌ **Rejected** | Off-category; wellness category rising queries were mostly non-health adjacent |
| **Local/Narrow** | UNC Health hospital approval, VCU Health leader obituary, NOAA whale health | ❌ **Rejected** | Local hospital news or non-human health — excluded categories |
| **North Atlantic Right Whale / NOAA** | NOAA Fisheries health updates | ❌ **Rejected** | Veterinary/animal health; not in allowed categories unless zoonotic |
| **Crumbl nutrition queries** | Google Trends nutrition rising: crumbl drink/cookie/soda nutrition facts | ❌ **Rejected** | Brand-specific junk food queries; no genuine health editorial value |
| **Sauerkraut / diet rising** | Google Trends diet: trump cabinet sauerkraut diet, sauerkraut diet | ❌ **Rejected** | Political-diet framing; celebrity diet fluff; borderline brand safety |
| **Jeremy Clarkson / Joan Cusack / celebrity health** | Google Trends health rising: celebrity health queries | ❌ **Rejected** | Celebrity gossip without evidence base — excluded category |

---

## SIGNAL SUMMARY

```yaml
signal_summary:
  run_started_at: "2026-06-22T00:00:00Z"
  run_completed_at: "2026-06-22T00:00:00Z"
  total_signals_reviewed: 144
  total_signals_retained: 9
  total_rejected: 135
  google_trends_available: true
  search_velocity_source: "google_trends"
  rejection_breakdown:
    off_category: 52          # celebrity wellness, lifestyle, non-health tech, local hospital
    brand_safety: 11          # political framing, celebrity diet, sauerkraut/political diet
    duplicate: 0
    weak_signal: 31           # social-only or single-source
    unverified_claim: 6       # routed to 02b Monitor or Reject
    other: 35                 # aggregator-only, animal health, too narrow
  highest_priority_topic: "Blood Pressure Medication Recall (Chlorthalidone) — 11,000+ Prescriptions"
  strongest_signal_source: "FDA.gov + Google Trends breakout (rising: 'rising pharma chlorthalidone recall')"
  tools_unavailable:
    - ExaSearch (not called — pre-fetch data sufficient)
    - Reddit BrowserNavigate
    - Content database
  notes: >
    Google Trends 'food safety' +11 and 'weight loss' +12 and 'gut health' +10 rising.
    'Mental health' +12 but most rising queries are celebrity/location-specific.
    Self-check skipped — no site_url configured. Competitor fallback used.
    No run_history.yaml or deferred_topics.yaml found — no prior-run cross-reference available.
    Marketa Vondrousova (Google Trends trending) is an athlete — off-category, rejected.
```

---

## SKILL 02b ROUTING SUMMARY

| Topic | Risk Type | Gate Result | Primary Source Found | Notes |
|---|---|---|---|---|
| Blood Pressure Medication Recall | recall | **Pass (breaking-recall exception)** | Partial — FDA.gov page exists; Yahoo + EatingWell + NewsNation confirm same product + scale | Medium confidence cap applied; verify FDA recall notice URL before publish |
| Infant Formula Recall (Botulism) | recall | **Pass (primary source: FDA.gov)** | ✅ FDA.gov outbreak investigation page | Full pass; FDA primary source directly citable |
| Food Safety Recalls (Mac & Cheese, Alfredo, Soft Cheese, Ice Cream) | recall | **Pass (breaking-recall exception)** | Partial — FDA.gov class upgrade confirmed for mac & cheese; PBS/Good Housekeeping confirm alfredo/salmonella | Medium confidence cap; clustered as one brief |
| Antidepressant Recall (Carcinogen) | recall / drug_or_treatment_claim | **Pass (breaking-recall exception)** | Partial — WCNC, Health.com, Prevention (3 outlets); carcinogen identity not fully specified in headlines | Medium confidence cap; note carcinogen details must be verified before publish |
| Shingles Vaccine + Dementia Risk | medical_study | **Pass** | Medical Xpress names study; Keck/USC institutional source | Claim is "may lower" — hedged appropriately. Verify journal + DOI before publish. |
| Fish Oil / Alzheimer's | medical_study | **Pass** | Keck Medicine of USC institutional press release | Observational flag required; "may not prevent" framing acceptable |
| Psilocybin Clinical Trial (USC) | clinical_trial | **Monitor** | Study funded, not yet started — no outcome data | No results to report; premature for patient-facing article. Routed P5. |
| FDA Speed-Up Clinical Trials | policy_or_regulatory_change | **Pass (not high-risk health claim)** | STAT News + Fierce Biotech (06/22) + federal health agencies announcement | Regulatory/editorial topic; no patient safety claim |
| AI in Healthcare | study_or_research | **Pass** | Nature (peer-reviewed) + Google/AMIE (institutional) | AI diagnostic claims require qualification; not direct patient treatment claim |
| Mental Health + Childbearing | study_or_research | **Pass** | NYT Well + Yale School of Medicine study cited | Observational; appropriately hedged in source headline |

---

## FINAL EDITORIAL PRIORITY BOARD

| # | Priority | Timing | Topic | Trend Score | Opp. Score | Discover | Urgency | Confidence | Angle |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **P1** | Immediate | Blood Pressure Medication Recall — Chlorthalidone | 88 | 82 | 5 | now | Medium | Patient action guide: what to check, what to do |
| 2 | **P1** | Immediate | Infant Formula Recall — Botulism Outbreak Investigation | 85 | 85 | 5 | now | High | What parents need to know + FDA action steps |
| 3 | **P1** | Immediate | Antidepressant Recall — Carcinogen Risk (375,000 bottles) | 82 | 80 | 5 | now | Medium | Safety explainer: risk level, what to do, who's affected |
| 4 | **P2** | Short-term | Shingles Vaccine Linked to Lower Dementia Risk | 72 | 78 | 4 | today | Medium | Evidence review: what the study actually shows |
| 5 | **P2** | Short-term | Fish Oil Won't Prevent Alzheimer's Decline, Study Finds | 68 | 74 | 4 | today | Medium | Supplement reality check: what you're actually getting |
| 6 | **P2** | Short-term | FDA Food Safety Recalls Round-Up (Mac & Cheese, Alfredo, Soft Cheese, Ice Cream) | 74 | 70 | 4 | today | Medium | Consumer action: full list + what to check at home |
| 7 | **P3** | Scheduled | FDA Pilots Program to Cut Phase 1 Trial Times by Up to 12 Months | 65 | 68 | 3 | this_week | Medium | What faster trials mean for patients waiting on new treatments |
| 8 | **P3** | Scheduled | General-Purpose AI Outperforms Specialized Clinical Tools on Physician Questions | 62 | 65 | 3 | this_week | Medium | Skeptical take: what this means — and doesn't mean — for your care |
| 9 | **P3** | Scheduled | Mental Health Is Now a Factor in Whether People Choose to Have Children | 60 | 63 | 3 | this_week | Medium | Explainer: what the research shows + what it means for reproductive decision-making |

**P5 Monitor:** RFK Jr. mental health funding (policy drift risk), Healthcare affordability Gallup data (slight policy framing), Psilocybin USC trial (no results yet)

---

## EDITORIAL BRIEFS

---

### BRIEF 1 — P1 / IMMEDIATE

```yaml
priority_level: P1
publish_timing: immediate
topic: "Blood Pressure Medication Recall — Chlorthalidone, 11,000+ Prescriptions"
primary_entity: "Chlorthalidone"
signal_type: recall
allowed_category: "FDA and CDC regulatory updates"
trend_strength_score: 88
opportunity_score: 82
discover_score: 5
urgency: now
confidence: medium
confidence_reason: >
  3+ credible outlets (Yahoo, EatingWell, NewsNation) confirm same product and scale.
  Google Trends shows 'rising pharma chlorthalidone recall' as breakout query.
  Breaking-recall exception applied — FDA primary notice URL must be verified before publish.
content_status: new
source_count: 4
recommended_angle: "Patient action guide — what chlorthalidone is, who's affected, what to do right now"
why_now: >
  Google Trends shows 'rising pharma chlorthalidone recall' as a breakout query today.
  11,000+ prescriptions recalled nationwide; blood pressure medication is among the most
  commonly prescribed drug classes in the US. Patients need actionable guidance now.
primary_headline: "Blood Pressure Medication Recalled: What to Do If You Take Chlorthalidone"
next_steps: >
  Verify FDA recall notice URL at fda.gov before publish.
  Confirm lot numbers, manufacturer, and specific carcinogen/contamination reason.
  Add cardiologist or pharmacist quote (published source acceptable).
```

**Why Now:** Breakout Google Trends query today. 11,000+ prescriptions recalled. Chlorthalidone is a widely used thiazide-like diuretic for hypertension — millions of Americans take it. Patients searching now need actionable guidance, not just news.

**Alternate Headlines:**
- "Is Your Blood Pressure Medication on the Recall List? Here's What to Check"
- "FDA Recalls Thousands of Chlorthalidone Prescriptions — Here's What Patients Need to Know"

**Angle:** Lead with patient action, not just news. Frame around: What is chlorthalidone? Why was it recalled? What's the actual risk? What should affected patients do (call pharmacist, don't stop abruptly)?

**Outline:**
1. **What happened** — scope of recall (11,000+ prescriptions, nationwide), manufacturer, recall class
2. **What is chlorthalidone** — who takes it, what it treats (hypertension, edema)
3. **What's the contamination/risk** — specify contaminant when confirmed; relative vs absolute risk
4. **What to do if you're affected** — check your prescription label, call pharmacist, do NOT stop BP medication without physician guidance
5. **What happens when you stop suddenly** — brief note on why abrupt discontinuation is dangerous
6. **FAQ** — "Is this the same as my brand?" / "Should I go to the ER?" / "How do I find out if my bottle is recalled?"

**Key Data Points:**
- 11,000+ prescriptions recalled (Yahoo/NewsNation)
- Blood pressure medications are the most commonly prescribed drug class in the US (CDC data)
- Chlorthalidone mechanism and usage context

⚠️ **Integrity Flags:**
- `breaking-recall exception applied` — FDA.gov primary notice URL not yet confirmed in source headlines; must retrieve and link before publish
- Do not state specific health risk magnitude until contaminant and recall class confirmed from FDA.gov
- Do not advise patients to stop taking medication — abrupt BP medication discontinuation is medically dangerous

**Source Plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| FDA.gov | https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts [verify specific recall URL] | 1 | Primary recall notice — MUST VERIFY |
| Yahoo / NewsNation | https://www.yahoo.com [original article] | 2 | Scope confirmation |
| EatingWell | https://www.eatingwell.com [article] | 2 | Coverage confirmation |
| CDC | https://www.cdc.gov/bloodpressure | 1 | Chlorthalidone usage context |

**Expert Type:** Cardiologist or clinical pharmacist — pull existing published quote from STAT, Reuters, or FDA press release statement.

**SEO:**
- Primary keyword: `chlorthalidone recall`
- Supporting: `blood pressure medication recall 2026`, `chlorthalidone side effects`, `what to do if medication is recalled`, `FDA drug recall 2026`
- Format: News + FAQ hybrid
- Schema: MedicalWebPage + FAQPage
- Estimated word count: 900–1,200

**Discover Notes:** Score 5. Exact-match query for AI systems ("is my blood pressure medication recalled?"). Specific named drug + FDA recall = high citation potential in Perplexity/ChatGPT health queries.

---

### BRIEF 2 — P1 / IMMEDIATE

```yaml
priority_level: P1
publish_timing: immediate
topic: "Infant Formula Recall — Powdered Formula, Botulism Outbreak Investigation"
primary_entity: "Powdered Infant Formula"
signal_type: recall
allowed_category: "FDA and CDC regulatory updates / pediatric health"
trend_strength_score: 85
opportunity_score: 85
discover_score: 5
urgency: now
confidence: high
confidence_reason: >
  FDA.gov primary source confirmed (outbreak investigation page, June 2026).
  Prevention named outlet. Botulism outbreak investigation is the highest-urgency
  recall type — no breaking-recall exception needed; FDA primary source is directly
  available.
content_status: new
source_count: 3
recommended_angle: "What parents need to know — which formula, what botulism risk means for infants, exact steps to take"
why_now: >
  FDA has an active outbreak investigation page for infant botulism linked to powdered
  formula as of June 17, 2026. Infant botulism is rare but severe — parents of formula-fed
  infants need specific product information and action steps immediately.
primary_headline: "Infant Formula Recalled Over Botulism Risk: What Parents Need to Know Right Now"
next_steps: >
  Pull FDA.gov outbreak investigation URL directly (fda.gov, June 2026 infant botulism page).
  Confirm brand name, lot codes, and states affected.
  Add AAP or pediatrician published guidance on infant botulism.
```

**Why Now:** FDA active outbreak investigation page. Infant botulism is among the most serious pediatric emergencies — extremely low tolerance for delay. Parents searching right now need brand names, lot codes, and safe alternatives.

**Alternate Headlines:**
- "FDA Is Investigating Infant Botulism Linked to Powdered Formula — Here's What to Do"
- "Powdered Infant Formula Recall: The Brands Affected and How to Keep Your Baby Safe"

**Angle:** Immediate parent action guide. Lead with: which formula, what lots, what risk botulism poses to infants, what to feed your baby instead, when to call a doctor.

**Outline:**
1. **What's happening** — FDA outbreak investigation, recall scope
2. **Which formula / lot codes** — exact product details from FDA notice
3. **What is infant botulism** — brief, non-alarmist explanation of risk; age vulnerability
4. **What to do** — stop using recalled formula, contact pediatrician, safe alternatives
5. **Signs of botulism in infants** — when to seek emergency care
6. **FAQ** — "Can I use the rest of my can?" / "What formula is safe?" / "Is this connected to [prior recalls]?"

**Key Data Points:**
- Infant botulism affects ~100–200 US infants per year (CDC); foodborne botulism is rare
- Powdered formula (not ready-to-feed) is the affected form
- FDA outbreak investigation page: active as of June 17, 2026

⚠️ **Integrity Flags:**
- Brand name and lot codes MUST be pulled from FDA.gov before publish — do not go live without them
- Distinguish infant botulism (spore-related) from foodborne botulism in adults — different mechanism
- Do not overstate case count until confirmed in FDA investigation update

**Source Plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| FDA.gov | https://www.fda.gov/food/outbreaks-foodborne-illness/outbreak-investigation-infant-botulism-powdered-infant-formula-june-2026 [verify] | 1 | Primary recall + outbreak data |
| Prevention | https://www.prevention.com [article, June 17] | 2 | Coverage context |
| CDC | https://www.cdc.gov/botulism | 1 | Infant botulism background |
| AAP | https://www.healthychildren.org | 1 | Pediatrician guidance |

**Expert Type:** Pediatrician or pediatric infectious disease specialist — pull from AAP official guidance or published HealthyChildren.org statement.

**SEO:**
- Primary keyword: `infant formula recall 2026`
- Supporting: `powdered formula recall botulism`, `baby formula recall FDA`, `infant botulism symptoms`, `safe formula alternatives 2026`
- Format: News explainer + parent action guide
- Schema: MedicalWebPage + FAQPage
- Estimated word count: 1,000–1,300

**Discover Notes:** Score 5. "Is [brand] baby formula safe?" is an exact AI query. Specific named entity + FDA outbreak investigation + pediatric urgency = extremely high AI citation potential.

---

### BRIEF 3 — P1 / IMMEDIATE

```yaml
priority_level: P1
publish_timing: immediate
topic: "Popular Antidepressant Recalled Over Carcinogen Risk — 375,000 Bottles"
primary_entity: "Antidepressant (recalled — brand TBD from FDA notice)"
signal_type: recall
allowed_category: "FDA and CDC regulatory updates / mental health"
trend_strength_score: 82
opportunity_score: 80
discover_score: 5
urgency: now
confidence: medium
confidence_reason: >
  3 credible outlets confirm: WCNC, Health.com, Prevention.
  375,000 bottle scope confirmed across outlets. Brand not confirmed in headline text —
  breaking-recall exception applied. FDA.gov primary notice must be retrieved.
content_status: new
source_count: 4
recommended_angle: "Safety explainer: what carcinogen risk actually means, who should act, and what not to do"
why_now: >
  375,000 bottles recalled nationally. Antidepressants are among the most commonly prescribed
  medications in the US. Patients will be alarmed — they need calibrated risk information
  and clear action steps, not panic. Mental health search interest is +12 this week.
primary_headline: "Antidepressant Recalled Over Carcinogen: What the Risk Actually Means for Patients"
next_steps: >
  Retrieve FDA.gov recall notice — confirm drug name, carcinogen (likely NDMA or similar
  nitrosamine impurity based on prior recall patterns), recall class, lot numbers.
  Do NOT publish without drug name confirmed. Add psychiatrist or pharmacist sourced quote.
```

**Why Now:** 375,000 bottles. Antidepressants are taken by ~1 in 8 Americans. Carcinogen recalls cause disproportionate patient anxiety and abrupt discontinuation — which is medically dangerous for antidepressants. The editorial gap is calibrated risk communication.

**Alternate Headlines:**
- "375,000 Bottles of Antidepressant Recalled — Here's the Actual Risk and What to Do"
- "FDA Recalls Antidepressant for Carcinogen Contamination: Should You Be Worried?"

**Angle:** Calm, evidence-based. The story is not just "recall" — it's "what does 'high levels of carcinogen' actually mean for someone who took this medication for months?" Frame around: chronic low-level exposure risk vs acute risk, why you should NOT stop abruptly, how to check your prescription.

**Outline:**
1. **What's being recalled** — drug name, scope, contamination reason (confirm from FDA)
2. **What's the carcinogen risk** — context: NDMA/nitrosamine recalls context, FDA acceptable daily intake, actual estimated added cancer risk (typically very low over short-term exposure)
3. **What NOT to do** — don't abruptly stop antidepressant; discontinuation syndrome is real
4. **What TO do** — check lot number, call pharmacist, call prescribing doctor
5. **Context: prior similar recalls** — Zantac/ranitidine, valsartan — pattern of nitrosamine recalls
6. **FAQ** — "Am I going to get cancer?" / "Can I just stop taking it?" / "Is there a safe alternative?"

**Key Data Points:**
- 375,000 bottles recalled (WCNC, Prevention, Health.com)
- Approximately 1 in 8 Americans take antidepressants (CDC/NCHS)
- NDMA-type recalls: FDA has established acceptable daily intake thresholds

⚠️ **Integrity Flags:**
- `breaking-recall exception applied` — drug brand name and carcinogen identity not confirmed from FDA.gov yet; do NOT publish without these
- Do not state specific cancer risk magnitude without FDA-confirmed carcinogen and exposure data
- CRITICAL: Explicitly state that patients should NOT stop antidepressants abruptly — discontinuation syndrome and relapse risk are real dangers
- Do not use language like "toxic" or "dangerous levels" without context from FDA classification

**Source Plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| FDA.gov | https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts [verify specific notice] | 1 | Primary recall — MUST VERIFY before publish |
| Health.com | https://www.health.com [June 16 article] | 2 | Scope confirmation |
| Prevention | https://www.prevention.com [June 17 article] | 2 | Coverage confirmation |
| WCNC | https://www.wcnc.com [June 16 article] | 2 | Bottle count confirmation |
| FDA NDMA resource | https://www.fda.gov/drugs/drug-safety-and-availability/information-about-nitrosamine-impurities-medications | 1 | Carcinogen context |

**Expert Type:** Psychiatrist or clinical pharmacologist — pull from STAT News or Reuters existing coverage of prior nitrosamine recalls; or FDA press release statement.

**SEO:**
- Primary keyword: `antidepressant recall 2026`
- Supporting: `antidepressant recalled carcinogen`, `FDA antidepressant recall`, `what to do if antidepressant recalled`, `NDMA antidepressant recall`
- Format: News explainer + patient action guide
- Schema: MedicalWebPage + FAQPage
- Estimated word count: 1,000–1,300

**Discover Notes:** Score 5. "Should I stop taking my antidepressant if it's recalled?" is a direct AI query with high urgency. Named drug + carcinogen + mental health medication = very high citation potential.

---

### BRIEF 4 — P2 / SHORT-TERM

```yaml
priority_level: P2
publish_timing: short_term
topic: "Shingles Vaccine Linked to Lower Dementia Risk, Study Suggests"
primary_entity: "Shingles Vaccine (Shingrix)"
signal_type: study_or_research
allowed_category: "medical research and clinical trials / aging and longevity"
trend_strength_score: 72
opportunity_score: 78
discover_score: 4
urgency: today
confidence: medium
confidence_reason: >
  Medical Xpress coverage (06/16); institutional affiliation referenced. 'Study suggests'
  hedging appropriate. Journal and DOI not confirmed in injected headlines —
  must verify peer-reviewed publication before elevated claims.
content_status: new
source_count: 2
recommended_angle: "Evidence review: what the study actually found, how strong the evidence is, and what it means for vaccination decisions"
why_now: >
  Dementia is among the most feared health outcomes for adults 50+.
  Shingrix is already widely recommended — a new potential dementia-prevention benefit
  gives hesitant patients a concrete additional reason to vaccinate.
  Mental health/aging audience crossover at peak engagement week.
primary_headline: "Shingles Vaccine May Lower Dementia Risk — Here's What the Research Actually Shows"
next_steps: >
  Find and link the primary study — search PubMed for shingles vaccine dementia 2026.
  Confirm journal, DOI, study design (observational vs RCT).
  Add geriatrician or neurologist published quote.
```

**Why Now:** Dementia prevention is a perennial top search category for adults 45+. If a vaccine already on the market may offer added protection, this is a genuine "what should I do?" moment. SERP on this topic is likely dominated by earlier preliminary research — a 2026 update has strong SERP opportunity.

**Alternate Headlines:**
- "Shingles Shot and Dementia: A New Study Offers a Surprising Connection"
- "Could the Shingles Vaccine Also Protect Your Brain? New Research Explores the Link"

**Angle:** Evidence-first. What did the study actually find? What's the study design (observational = association, not causation)? Does this change CDC/ACIP recommendations? What should an adult 50+ do today?

**Outline:**
1. **The finding** — what the study found (risk reduction figure, if confirmed)
2. **How the study was done** — observational, sample size, duration; be explicit this is not an RCT
3. **Why this might make biological sense** — VZV neuroinflammation hypothesis (briefly)
4. **What Shingrix is** — reminder for readers who haven't gotten it yet
5. **Does this change vaccination recommendations?** — CDC ACIP guidance for 50+
6. **What experts say** — named researcher or neurologist perspective
7. **Bottom line** — should you get the shingles vaccine? (Answer: CDC already recommends it; this adds another potential reason)

⚠️ **Integrity Flags:**
- Study design must be confirmed before publishing risk reduction statistics; do not state causation
- "May lower" and "suggests" hedging must be maintained throughout — not "prevents dementia"
- Verify journal + DOI before publish; Medical Xpress is a secondary aggregator

**Source Plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| Medical Xpress | https://medicalxpress.com [June 16 article — find and link] | 2 | Signal source |
| Primary study | [PubMed search: shingles vaccine dementia 2026 — verify DOI] | 1 | Primary data — MUST FIND |
| CDC Shingrix page | https://www.cdc.gov/vaccines/vpd/shingles/public/shingrix/ | 1 | Vaccine recommendation context |
| Cochrane / prior systematic reviews | https://www.cochranelibrary.com [search shingles dementia] | 1 | Prior evidence context |

**SEO:**
- Primary keyword: `shingles vaccine dementia risk`
- Supporting: `Shingrix dementia prevention`, `shingles shot brain protection`, `shingles vaccine benefits 2026`, `can shingles vaccine prevent Alzheimer's`
- Format: Research explainer
- Schema: MedicalWebPage
- Estimated word count: 1,000–1,300

**Discover Notes:** Score 4. "Does the shingles vaccine prevent dementia?" is a natural AI query. High entity clarity. Primary source needed to maximize citation potential.

---

### BRIEF 5 — P2 / SHORT-TERM

```yaml
priority_level: P2
publish_timing: short_term
topic: "Fish Oil Supplements May Not Prevent Alzheimer's-Related Cognitive Decline"
primary_entity: "Fish Oil Supplements (Omega-3)"
signal_type: study_or_research
allowed_category: "medical research and clinical trials / aging and longevity / nutrition and diet science"
trend_strength_score: 68
opportunity_score: 74
discover_score: 4
urgency: today
confidence: medium
confidence_reason: >
  Keck Medicine of USC institutional press release (06/18); named institution.
  Journal and DOI not confirmed from headline text — must verify.
  Study framing is appropriately hedged ("may not prevent").
content_status: new
source_count: 2
recommended_angle: "Supplement reality check: what fish oil actually does and doesn't do, based on current evidence"
why_now: >
  Fish oil is one of the top-selling supplements globally. Alzheimer's fear drives
  supplement purchases. A high-quality study showing no benefit is an important
  consumer decision-making signal. Gut health +10 and nutrition +6 rising this week —
  supplement evidence topics are at high audience relevance.
primary_headline: "Fish Oil Won't Prevent Alzheimer's, Study Finds — What the Evidence Actually Shows"
next_steps: >
  Find and link USC/Keck primary study — search PubMed, confirm journal, DOI, design.
  Add geriatrician, neurologist, or registered dietitian quote from existing coverage.
  Check if this is a new RCT or meta-analysis — methodology matters for framing.
```

**Why Now:** Omega-3 / fish oil is a $2B+ supplement market. Many consumers take it specifically for brain health. A study showing it doesn't prevent Alzheimer's-related decline is a direct "should I keep buying this?" moment. SERP opportunity: most existing content is pro-supplement; a well-sourced skeptical take has strong differentiation.

**Alternate Headlines:**
- "Is Fish Oil Actually Protecting Your Brain? A New Study Says No"
- "You've Been Taking Fish Oil for Brain Health — Here's What the Science Now Says"

**Angle:** Skeptical, not dismissive. What did the study find? What does "Alzheimer's-related decline" mean as an outcome? Are there other proven benefits (cardiovascular, inflammation)? Does this change what you should do?

**Outline:**
1. **The finding** — what the study measured, what it found
2. **Study design** — what kind of study, sample size, duration; observational or RCT?
3. **What this doesn't mean** — fish oil isn't harmful; other benefits may still exist (triglycerides, heart health)
4. **Prior evidence landscape** — what did we think fish oil did for the brain? What changed?
5. **What experts say** — named researcher or neurologist perspective
6. **Should you stop taking fish oil?** — nuanced answer based on your goals
7. **What actually does help cognitive health** — brief pivot to exercise, sleep, diet evidence

⚠️ **Integrity Flags:**
- Confirm whether study is RCT or observational before stating conclusions
- "May not prevent" must be maintained — do not headline as "Fish oil is useless"
- Note that absence of benefit for Alzheimer's doesn't eliminate cardiovascular benefits
- Institutional press release only at this stage — verify journal publication before elevated claims

**Source Plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| Keck Medicine USC | https://www.keckmedicine.org [June 18 article — find and link] | 2 | Institutional press release |
| Primary study | [PubMed search: fish oil omega-3 Alzheimer's cognitive decline 2026 — verify DOI] | 1 | Primary data — MUST FIND |
| NIH/ODS | https://ods.od.nih.gov/factsheets/Omega3FattyAcids-HealthProfessional/ | 1 | Background on omega-3 evidence |
| Cochrane reviews | https://www.cochranelibrary.com [search omega-3 dementia] | 1 | Systematic review context |

**SEO:**
- Primary keyword: `fish oil Alzheimer's prevention`
- Supporting: `omega-3 brain health evidence`, `fish oil supplements do they work`, `fish oil cognitive decline study 2026`, `does fish oil prevent dementia`
- Format: Research explainer + practical FAQ
- Schema: MedicalWebPage + FAQPage
- Estimated word count: 1,000–1,200

**Discover Notes:** Score 4. "Does fish oil prevent Alzheimer's?" is a direct, common AI query. Skeptical evidence review answers a specific question users have. High citation potential with DOI link.

---

### BRIEF 6 — P2 / SHORT-TERM

```yaml
priority_level: P2
publish_timing: short_term
topic: "FDA Food Safety Recalls Round-Up — Mac & Cheese, Alfredo Sauce, Soft Cheese, Ice Cream (June 2026)"
primary_entity: "Multiple FDA Food Recalls (June 2026)"
signal_type: recall
allowed_category: "FDA and CDC regulatory updates / nutrition and diet science"
trend_strength_score: 74
opportunity_score: 70
discover_score: 4
urgency: today
confidence: medium
confidence_reason: >
  Multiple outlets confirm individual recalls: PBS (alfredo/salmonella), NewsNation (mac & cheese 526,000 packages),
  FDA.gov (listeria soft cheese outbreak investigation), The Healthy (ice cream).
  Breaking-recall exception applied for aggregate article — individual recall pages
  on FDA.gov must be linked before publish. Food safety search interest +11 this week.
content_status: new
source_count: 6
recommended_angle: "Consumer action guide: everything recalled right now, what the risk is, what to throw out"
why_now: >
  Food safety Google Trends interest +11 this week. Four simultaneous major food recalls
  is genuinely unusual and creates consumer confusion. A consolidated guide answers
  'what do I need to check in my kitchen right now?' — the most searched question
  when a recall is announced.
primary_headline: "4 Major Food Recalls Right Now: Mac & Cheese, Alfredo Sauce, Soft Cheese, and Ice Cream"
next_steps: >
  Pull each FDA.gov recall page and confirm: product names, lot codes, states affected,
  recall class (I or II), contamination type.
  Link all four FDA notices before publish.
  This brief should be updated as more details emerge — use update-friendly format.
```

**Why Now:** Multiple simultaneous food recalls create genuine consumer confusion. "What's been recalled this week?" is a natural, high-volume query. A single authoritative round-up with FDA links is the best possible answer. Food safety search interest +11 this week.

**Alternate Headlines:**
- "Is Your Food Safe? Check These 4 Current FDA Recalls Before You Eat"
- "FDA Issues Multiple Food Recalls This Week — Here's What's Affected and What to Do"

**Angle:** Consumer action over news. Make it scannable. Each recall gets its own section with: product, contamination risk, states affected, what to do (check lot number, throw out, get refund). Include a "quick checklist" for readers who just want the short version.

**Outline:**
1. **Quick summary box** — 4 recalls at a glance (scannable)
2. **Mac & Cheese recall** — ~526,000 packages, what brand, what issue (Class II per Good Housekeeping)
3. **Alfredo sauce recall** — salmonella, distributed to dozens of states (PBS)
4. **Soft cheese / Listeria** — FDA.gov outbreak investigation, June 2026
5. **Ice cream recall** — 3 states, what brand, what risk
6. **How to check your products** — how to find lot numbers, FDA recall search tool link
7. **FAQ** — "What should I do if I ate recalled food?" / "Where do I report a reaction?"

⚠️ **Integrity Flags:**
- Breaking-recall exception applied — all four FDA.gov recall URLs must be confirmed and linked before publish
- Do not conflate recall classes: Class I (serious health hazard) vs Class II (remote probability) have different urgency levels — state clearly for each product
- Mac & cheese upgraded to Class II (Good Housekeeping) — note this is lower urgency than Class I; calibrate language
- Soft cheese listeria investigation — FDA.gov states outbreak investigation status; note whether recall is voluntary or mandatory

**Source Plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| FDA.gov — Listeria Soft Cheese | https://www.fda.gov/food/outbreaks-foodborne-illness/outbreak-investigation-listeria-monocytogenes-soft-cheese-june-2026 | 1 | Primary outbreak data |
| FDA.gov — Recalls Hub | https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts | 1 | All recall notices |
| NewsNation | https://www.newsnation.com [mac & cheese article] | 2 | Scope confirmation |
| PBS | https://www.pbs.org [alfredo recall article, June 15] | 2 | Salmonella recall confirmation |
| Good Housekeeping | https://www.goodhousekeeping.com [mac & cheese Class II upgrade] | 2 | Recall class context |
| The Healthy | https://www.thehealthy.com [ice cream recall article] | 2 | Ice cream recall details |

**SEO:**
- Primary keyword: `FDA food recall June 2026`
- Supporting: `mac and cheese recall 2026`, `alfredo sauce salmonella recall`, `listeria soft cheese recall`, `what foods are recalled right now`
- Format: News round-up + consumer action guide
- Schema: FAQPage + NewsArticle
- Estimated word count: 1,000–1,400 (update-friendly structure)

**Discover Notes:** Score 4. "What food has been recalled recently?" is a direct AI query. Multiple named entities + FDA.gov source = strong citation potential. Round-up format with specific product names is highly AI-citable.

---

### BRIEF 7 — P3 / SCHEDULED

```yaml
priority_level: P3
publish_timing: scheduled
topic: "FDA Announces Pilot to Speed Up Phase 1 Clinical Trials by 6–12 Months"
primary_entity: "FDA Clinical Trial Acceleration Pilot"
signal_type: policy_or_regulatory_change
allowed_category: "FDA and CDC regulatory updates / medical research and clinical trials"
trend_strength_score: 65
opportunity_score: 68
discover_score: 3
urgency: this_week
confidence: medium
content_status: new
source_count: 3
recommended_angle: "What faster trials mean for patients waiting on new treatments — and what it won't change"
why_now: >
  Announced today (STAT News + Fierce Biotech, 06/22). First-day coverage opportunity.
  Patient advocacy angle is underserved in early trade coverage.
primary_headline: "FDA Is Moving to Speed Up Early Drug Trials — What It Means for Patients"
next_steps: >
  Link STAT News and Fierce Biotech primary articles.
  Find FDA.gov official announcement or press release.
  Add patient advocate or clinical researcher published perspective.
```

⚠️ **Integrity Flag:** Coverage is from trade press (STAT, Fierce Biotech) — verify FDA official announcement or Federal Register notice before detailing specific timelines. Do not overstate speed of change for patients currently enrolled in trials.

**Key Sources:**
- STAT News: https://www.statnews.com [June 22 article]
- Fierce Biotech: https://www.fiercebiotech.com [June 22 article]
- FDA.gov: [verify official announcement URL]

**SEO:** Primary keyword: `FDA clinical trial speed 2026` | Format: News explainer | Est. word count: 800–1,000

---

### BRIEF 8 — P3 / SCHEDULED

```yaml
priority_level: P3
publish_timing: scheduled
topic: "General-Purpose AI Chatbots Outperform Specialized Clinical AI on Physicians' Real-World Questions"
primary_entity: "AI in Healthcare / Clinical AI Benchmarking"
signal_type: study_or_research
allowed_category: "medical research and clinical trials"
trend_strength_score: 62
opportunity_score: 65
discover_score: 3
urgency: this_week
confidence: medium
content_status: new
source_count: 3
recommended_angle: "Skeptical take: what this Nature study actually shows — and what it doesn't mean for patients"
why_now: >
  Nature publication (06/17) — peer-reviewed, top-tier journal. AI in medicine is a
  high-audience-interest topic. The finding is counterintuitive (general-purpose beats
  specialized) and invites scrutiny. APA also covers AI in therapy same week.
primary_headline: "ChatGPT Outperforms Clinical AI Tools on Doctor Questions — What That Actually Means"
next_steps: >
  Find and link Nature study DOI.
  Add clinical AI researcher or physician published perspective.
  Distinguish benchmark performance from patient care application.
```

⚠️ **Integrity Flag:** Benchmark performance ≠ clinical deployment safety. Do not imply patients should use ChatGPT instead of physicians. Study measures question-answering performance on physician queries — not diagnostic accuracy, patient safety, or real-world outcomes. Clearly distinguish.

**Key Sources:**
- Nature: https://www.nature.com [June 17, 2026 — find and link DOI]
- Google/AMIE blog: https://blog.google [June 17, 2026]
- APA (AI in therapy): https://www.apa.org [June 16 article]

**SEO:** Primary keyword: `AI vs clinical AI healthcare` | Format: Research explainer with skeptical angle | Est. word count: 900–1,100

---

### BRIEF 9 — P3 / SCHEDULED

```yaml
priority_level: P3
publish_timing: scheduled
topic: "Mental Health Is Now a Major Factor in Whether People Choose to Have Children"
primary_entity: "Mental Health and Reproductive Decision-Making"
signal_type: study_or_research
allowed_category: "mental health and psychology / women's health"
trend_strength_score: 60
opportunity_score: 63
discover_score: 3
urgency: this_week
confidence: medium
content_status: new
source_count: 2
recommended_angle: "Explainer: what's driving this shift, what the research shows, and what it means for people navigating this decision"
why_now: >
  NYT Well (06/17) + Yale School of Medicine study signal (06/16).
  Mental health search interest +12 this week. Reproductive decision-making
  is a sustained cultural conversation. SERP on this topic is thin on evidence-based
  coverage that goes beyond anecdote.
primary_headline: "More People Are Factoring Mental Health Into Whether to Have Children — Here's What the Research Shows"
next_steps: >
  Find Yale study citation and link.
  Add clinical psychologist or reproductive psychiatrist published perspective.
  Frame inclusively — relevant to all genders making this decision.
```

⚠️ **Integrity Flag:** NYT Well is primary signal; Yale study headline vague ("links physical and mental capacity to disability before death") — confirm whether this study is directly about childbearing decisions or if NYT is using separate sourcing. Do not conflate the two without verification.

**Key Sources:**
- NYT Well: https://www.nytimes.com/section/well [June 17 article]
- Yale School of Medicine: https://medicine.yale.edu [June 16 study — find and link]
- APA Mental Health guidelines: https://www.apa.org

**SEO:** Primary keyword: `mental health having children decision` | Format: Explainer + FAQ | Est. word count: 900–1,100

---

## REJECTED TOPICS LOG

| Topic | Signal Type | Rejection Reason |
|---|---|---|
| Marketa Vondrousova (Google Trends trending) | social_spike | Off-category — athlete/celebrity, no health angle |
| Jeremy Clarkson / Joan Cusack / David Bromstad health searches | social_spike | Celebrity gossip; excluded category |
| Crumbl cookie/drink nutrition facts | rising_search_interest | Brand-specific junk food queries; no health editorial value |
| Sauerkraut / Trump cabinet sauerkraut diet | rising_search_interest | Political-diet framing; celebrity diet fluff; brand safety concern |
| Erling Haaland diet | rising_search_interest | Celebrity diet; excluded category |
| Balenciaga wellness | cultural_moment | Celebrity/brand wellness trend; excluded category |
| Midjourney sauna (Union Square) | cultural_moment | Lifestyle marketing; not health editorial |
| Samsung connected care / VivaTech | product_or_brand_movement | Tech product marketing; not health editorial |
| Asheville "best wellness town" | cultural_moment | Geographic lifestyle ranking; off-category |
| Aura points / aura slang | social_spike | Social slang trend; off-category |
| Trending beauty hacks / kitchen tech | rising_search_interest | Off-category entirely |
| AI personal assistant / streaming shows | rising_search_interest | Off-category entirely |
| UNC Health new hospital / VCU Health leader obituary | breaking_news | Local hospital news; excluded category |
| North Atlantic Right Whale health | breaking_news | Animal health (non-zoonotic); excluded category |
| Psilocybin clinical trial USC | clinical_trial | **Skill 02b Monitor** — no results yet; trial just funded; premature for patient-facing article |
| RFK Jr. mental health funding $700M | policy_or_regulatory_change | **P5 Monitor** — STAT News flags grants as recycled; political adjacency; borderline brand safety |
| Gallup healthcare affordability 5-year low | data_release | **P5 Monitor** — strong data but primarily policy framing; no clear actionable health angle for this audience without political context |
| California health insurance tax | policy_or_regulatory_change | Geographic (California only) + pure policy/finance; off-category for national health audience |
| Fewer sick days where medical marijuana legal | medical_study | Weak health claim; primarily labor/policy angle; borderline off-category |
| Multiple myeloma treatment delay (Atrium Health) | clinical_trial | Institutional press release only; single institution; narrow clinical audience |
| Brain-computer interface (Michigan Medicine) | clinical_trial | First-in-human device; very early stage; specialized clinical audience |
| Traffic fatality study | study_or_research | Off-category — transportation safety, not health/wellness |
| Pet aging study | medical_study | Veterinary; excluded unless zoonotic |
| Digestive health coaching (Marquette) | evergreen_with_fresh_angle | Local employer wellness program; too narrow |
| San Diego wellness industry | cultural_moment | Industry/economic story; off-category |
| Black Girl Wellness Fest | cultural_moment | Local event; off-category for editorial |
| Chimaeras health/wellness (UVA) | study_or_research | Niche molecular biology; insufficient consumer relevance at this stage |
| OpenAI ChatGPT health intelligence (broad) | product_or_brand_movement | Subsumed into Brief 8 (AI in healthcare); duplicate |
| CJG wellness / Centauri health / Sutter Health Park | rising_search_interest | Brand/location specific; off-category |
| Federal employees health benefits / Carter Page / Pauline Newman | rising_search_interest | Policy/legal; off-category |
| Planet fitness Juneteenth hours | rising_search_interest | Brand query; off-category |
| Michelle Obama / Shania Twain / Jelly Roll weight loss | social_spike | Celebrity weight loss gossip; excluded category |
| Baking soda and lemon juice for weight loss | social_spike | Unverified folk remedy; brand safety risk |
| Low carb cruise | social_spike | Celebrity wellness event; excluded category |

---

## INTEGRITY FLAGS CONSOLIDATED

All ⚠️ flags for editorial review before any brief goes to a writer:

| Brief | Flag | Action Required |
|---|---|---|
| **B1 — Chlorthalidone Recall** | Breaking-recall exception applied; FDA primary notice not yet confirmed | Retrieve FDA.gov recall URL; confirm lot numbers and contaminant before assign |
| **B1 — Chlorthalidone Recall** | Do not advise stopping BP medication — abrupt discontinuation is medically dangerous | Must be explicit in article |
| **B2 — Infant Formula** | Brand name and lot codes not in headlines — must come from FDA.gov | Do not publish without product-specific details |
| **B2 — Infant Formula** | Distinguish infant botulism (spore) from foodborne botulism (toxin) | Different mechanism; easy to conflate; must be accurate |
| **B3 — Antidepressant Recall** | Breaking-recall exception; drug name and carcinogen unconfirmed from injected data | Do not assign to writer until FDA notice retrieved; confirm drug name |
| **B3 — Antidepressant Recall** | CRITICAL: Do not advise abrupt antidepressant discontinuation | Discontinuation syndrome + relapse risk; must be explicit |
| **B3 — Antidepressant Recall** | Do not state cancer risk magnitude without FDA-confirmed carcinogen and exposure data | Verify recall class and carcinogen identity from FDA |
| **B4 — Shingles/Dementia** | Medical Xpress is secondary aggregator — primary journal/DOI must be found | Do not state risk reduction numbers until verified from primary source |
| **B4 — Shingles/Dementia** | Maintain "may lower" hedging — not "prevents dementia" | Study design likely observational; not RCT |
| **B5 — Fish Oil/Alzheimer's** | Institutional press release only; journal and DOI not confirmed | Verify peer-reviewed publication before elevated claims |
| **B5 — Fish Oil/Alzheimer's** | Absence of Alzheimer's benefit ≠ absence of all fish oil benefit | Note cardiovascular/triglyceride benefits may still apply |
| **B6 — Food Recalls** | Four separate FDA.gov recall pages must be linked — breaking-recall exception | Do not publish as single article without all four FDA links confirmed |
| **B6 — Food Recalls** | Mac & Cheese = Class II (lower urgency) vs Class I (high risk) | Calibrate language per class; do not treat all equally |
| **B7 — FDA Trial Speed** | Trade press only at this stage; FDA official announcement not confirmed | Verify FDA.gov press release before detailing specific timelines |
| **B8 — AI vs Clinical AI** | Benchmark performance ≠ clinical safety or deployment readiness | Explicitly disclaim: do not imply patients should use ChatGPT instead of doctors |
| **B9 — Mental Health / Children** | Yale study may not be directly about childbearing decisions | Verify NYT sourcing — confirm whether Yale study is the basis or separate |

---

## RUN NOTES

```yaml
run_notes:
  date: "2026-06-22"
  niche: "health and wellness"
  signals_reviewed: 144
  signals_retained: 9
  signals_rejected: 135
  p1_count: 3
  p2_count: 3
  p3_count: 3
  p5_monitor: 3
  integrity_flags_total: 16
  key_themes_today:
    - "FDA recalls (multiple — medication and food)"
    - "Alzheimer's / dementia prevention evidence"
    - "AI in clinical medicine"
    - "Mental health and reproductive decisions"
    - "FDA regulatory acceleration"
  prior_run_crosscheck: "No run_history.yaml found — no recurring theme check possible"
  deferred_topics_checked: "No deferred_topics.yaml found"
  self_check: "Skipped — site_url not configured; competitor fallback used for SERP-gap context"
  google_trends_status: "Available — pre-fetch block used as primary search_velocity source"
  tools_used:
    - "SerpAPI Google News (pre-fetched)"
    - "SerpAPI Google Trends 7-day (pre-fetched)"
    - "Google News Radar (144 signals)"
    - "Competitor list fallback (10 domains, referenced for SERP gap)"
  tools_unavailable:
    - "ExaSearch (not invoked — pre-fetch data sufficient)"
    - "Reddit BrowserNavigate"
    - "Content database"
  dashboard_output: "outputs/daily_newsroom_dashboard/2026-06-22.html"
  run_archived: true
  editorial_notes: >
    Three P1 briefs all involve FDA recalls — confirms 'pharma recall' as breakout Google Trends
    signal today. All three require FDA.gov primary notice retrieval before writer assignment.
    No P1 brief should be assigned to a writer without editor first confirming FDA notice URL,
    product/drug name, lot codes, and recall class. The antidepressant recall is particularly
    sensitive — editorial must enforce the 'do not stop medication abruptly' language requirement.
    
    P2 briefs (shingles/dementia, fish oil/Alzheimer's) both require DOI verification before
    publishing any numerical claims. These can be assigned concurrently with P1 recall work
    since they are not as time-critical.
    
    P3 briefs (FDA trial speed, AI clinical benchmarking, mental health/childbearing) can be
    scheduled for Tuesday–Wednesday publish cadence.
```

---

**Dashboard file:** `outputs/daily_newsroom_dashboard/2026-06-22.html`
**Run archived to:** `data/run_history.yaml`
**Total briefs produced:** 9 (3 × P1 full, 3 × P2 full, 3 × P3 concise)
**Immediate editorial action required:** Retrieve FDA.gov recall notices for Briefs 1, 2, 3, and 6 before any writer assignment.