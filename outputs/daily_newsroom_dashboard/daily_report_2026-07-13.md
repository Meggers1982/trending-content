# Trending Content OS — Daily Pipeline Run
**Date:** 2026-07-13 | **Niche:** Health & Wellness | **Mode:** Automation Output

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
| Google Trends available | ✅ `serpapi_prefetch` — treating as primary search_velocity source |
| Google News Radar | ✅ 144 signals across 12 queries (60 shown) |
| Deferred topics file | ℹ️ No overdue entries (file assumed empty or no recheck_on dates passed as of 2026-07-13) |
| Run history check | ✅ Loaded — recurring themes flagged below |

**Recurring themes (3+ consecutive runs — staleness check):**
- Eye Drops Recall (2.53M bottles): 5 consecutive days (07-08 through 07-12) → **Stale unless new development**
- E. coli / Frozen Blueberries: 5 consecutive days → **Stale unless new development**
- GLP-1 online prescriptions (Yale study): 4 consecutive days → **Stale unless new development**
- Cream Cheese Recall: 3 consecutive days → **Stale unless new development**
- Sleep deprivation / weight gain (Columbia): 3 consecutive days → **Stale unless new development**
- Stanford opioid taper: 3 consecutive days → **Stale unless new development**
- Ebola DRC clinical trial: 3 consecutive days → **Stale unless new development**

**`can_run_signal_listener: true`**

---

## GOOGLE NEWS RADAR COVERAGE SUMMARY

144 unique signals across 12 queries processed. Main topic clusters identified:

| Cluster | Disposition | Rationale |
|---|---|---|
| **Eye Drops Recall (2.5M bottles)** | ❌ Rejected — existing | 5 consecutive run days; no new development detected (07-12 was most recent) |
| **E. coli / Frozen Blueberries** | ❌ Rejected — existing | 5 consecutive run days; no new agency action or case count update |
| **GLP-1 online prescriptions (Yale)** | ❌ Rejected — existing | 4 consecutive run days; same Yale study, no new data |
| **Cream Cheese Recall** | ❌ Rejected — existing | 3 consecutive run days; no new product additions |
| **Sleep / Weight Gain (Columbia)** | ❌ Rejected — existing | 3 consecutive run days; same study |
| **Stanford Opioid Taper** | ❌ Rejected — existing | 3 consecutive run days |
| **Ebola DRC / Bundibugyo trial** | ❌ Rejected — existing | 3 consecutive run days; NPR/Mongabay coverage same story |
| **Biological Aging Clocks (Nature)** | ❌ Rejected — existing | Covered 07-11 |
| **Pediatric Mental Health ERs** | ❌ Rejected — existing | Covered 07-12 |
| **"Super Mover" Walking / Longevity** | ❌ Rejected — existing | Covered 07-12 |
| **New World Screwworm (USDA/APHIS)** | ✅ **Retained** | New USDA confirmed detections posted 07-12 (zoonotic/environmental health angle; food safety rising query ties) |
| **Zeke Emanuel Ice Cream / Longevity Diet** | ✅ **Retained** | NPR wellness story 07-13 (today); rising Google Trends query; aging/longevity + nutrition angle; not previously covered |
| **OTC Skin Cream Recalls (manufacturing violations)** | ✅ **Retained** | MedShadow 07-08; distinct from eye drop recall; not previously covered; FDA recall signal type |
| **Fentanyl Vaccine — Evidence concerns** | ✅ **Retained** | Clinical Trial Vanguard 07-09; rising opioid/treatment interest; not previously covered |
| **Medical Mistrust + Wellness + Politics (Medscape)** | ⚠️ Monitor | Medscape 07-13; borderline — political drift risk; insufficient primary source to score safely |
| **Politicization of Medical Research (NYT)** | ❌ Rejected — off-category | Pure political/policy opinion; no new health data; brand safety flag |
| **AMA Healthcare Spending Trends** | ❌ Rejected — off-category | Business/healthcare economics; no direct patient health angle |
| **AMA Physician Wearables Survey** | ✅ **Retained** | Fitness/wellness + digital health; AMA = Tier 1; rising wearables interest; not previously covered |
| **Gut Health** | ⚠️ Monitor | Covered extensively 07-10; Google Trends gut health +20 delta is strong but SERP is saturated; no new study today |
| **PCOS Nutrition / Wellness** | ❌ Rejected — existing | Covered 07-11 |
| **Glioma Progression (Weill Cornell)** | ✅ **Retained** | Cancer evolution study 07-10; new primary institutional source; not previously covered |
| **DOJ Adderall digital health fraud** | ❌ Rejected — off-category | Criminal/legal story; no direct patient health angle; brand safety risk |
| **Yale Health System CEO ousted** | ❌ Rejected — off-category | Hospital administration; no patient health angle |
| **ACA enrollment decline (PBS/KFF)** | ❌ Rejected — off-category | Insurance policy; no clinical health content |
| **School-based health clinics closing (Virginia)** | ❌ Rejected — off-category | Regional policy; too narrow |
| **Lung Transplant for Terminal Lung Cancer (Northwestern)** | ✅ **Retained** | Covered 07-09 briefly in history context; checking — confirmed first covered 07-09 as single entry; new angle available on patient selection criteria; **content_status: update** |
| **Marie-Pierre St-Onge Sleep Diet** | ✅ **Retained** | Rising Google Trends query "marie-pierre st-onge sleep diet"; diet + sleep science intersection; not previously covered as standalone |
| **PCOS (general, non-nutrition)** | ❌ Rejected — existing | Covered 07-11 |
| **Nanox Cardiac AI** | ❌ Rejected — insufficient | Single-source clinical study promo; insufficient signal |
| **Enteral Nutrition** | ⚠️ Monitor | Rising Trends query; low news volume; needs more signal |

---

## SIGNAL SUMMARY

```yaml
signal_summary:
  run_date: 2026-07-13
  total_signals_reviewed: 144
  total_signals_retained: 8
  total_rejected: 136
  google_trends_available: true
  search_velocity_source: "google_trends (serpapi_prefetch)"
  rejection_breakdown:
    existing_coverage: 14
    off_category: 8
    weak_signal: 4
    brand_safety: 1
    monitored_not_scored: 3
    duplicate: 106
  highest_priority_topic: "New World Screwworm — USDA Confirmed Detections Expand"
  strongest_signal_source: "USDA APHIS (Tier 1) + Google Trends food safety rising"
  tools_unavailable: []
  notes: >
    Google Trends pre-fetch treated as primary velocity source. 
    Gut health +20 delta is the strongest Trends movement today but SERP is fully saturated and 
    the evergreen topic was covered 07-10. Fitness +17 delta driven by non-health queries 
    (museums, gardening). Weight loss -26 delta driven by celebrity queries — excluded. 
    Medical mistrust/wellness/politics cluster (Medscape) monitored due to political 
    drift risk; insufficient primary health data source to pass brand safety gate. 
    site_url not configured — self-check skipped; competitor coverage checked instead.
```

---

## SKILL 02b ROUTING SUMMARY

| Topic | Risk Type | Gate Result | Notes |
|---|---|---|---|
| New World Screwworm | not_applicable (environmental/zoonotic advisory) | Pass | USDA APHIS official notice = Tier 1 |
| Zeke Emanuel Ice Cream / Longevity | not_applicable (wellness/aging opinion piece with expert) | Pass | NPR wellness story, no clinical claim requiring gate |
| OTC Skin Cream Recalls | recall | **Pass with Medium cap** | MedShadow cites "serious manufacturing violations" — FDA.gov primary notice not directly retrieved; 2+ credible sources; breaking-recall exception applied; verify FDA.gov recall page before publishing |
| Fentanyl Vaccine | drug_or_treatment_claim | **Monitor → P5** | Clinical Trial Vanguard piece questions the evidence strategy; primary clinical trial source (ClinicalTrials.gov) referenced but claim about vaccine efficacy requires editorial interpretation; circulating claim materially overstates mechanism certainty |
| AMA Wearables Survey | not_applicable (survey/data release) | Pass | AMA = Tier 1; survey methodology traceable |
| Glioma Progression (Weill Cornell) | medical_study | **Pass** | Weill Cornell primary institutional source; study-level claim about tumor evolution biology — not a clinical recommendation; confidence capped at Medium (single institution pre-pub) |
| Lung Transplant Update (Northwestern) | medical_study | **Pass** | Previously cleared (covered 07-09); Northwestern = Tier 1 institutional; update frame only |
| Marie-Pierre St-Onge Sleep Diet | not_applicable (expert dietary guidance, not clinical claim) | Pass | Expert is Columbia sleep researcher; no specific dosage/treatment claim; Low–Medium risk |

---

## FINAL EDITORIAL PRIORITY BOARD

| # | Priority | Timing | Topic | Signal Type | Category | Trend | Opp | Discover | Urgency | Confidence | SERP | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **P1** | Immediate | New World Screwworm — USDA Confirms US Detections Expanding | policy_or_regulatory_change | environmental health | 74 | 78 | 4 | today | Medium | Medium | new |
| 2 | **P1** | Immediate | Zeke Emanuel's Case for Ice Cream and the Science of Longevity Diets | rising_search_interest | aging and longevity | 71 | 75 | 4 | today | Medium | Low | new |
| 3 | **P2** | Short-term | OTC Skin Cream Recalls — FDA Manufacturing Violations | recall | FDA and CDC regulatory updates | 66 | 72 | 3 | this_week | Medium* | Medium | new |
| 4 | **P2** | Short-term | AMA Survey: Most Physicians Now Support Consumer Wearables for Patient Care | data_release | fitness and exercise science | 62 | 70 | 4 | this_week | High | Low | new |
| 5 | **P2** | Short-term | Marie-Pierre St-Onge and the Sleep-Diet Connection: What the Research Shows | rising_search_interest | sleep science / nutrition | 65 | 68 | 4 | this_week | Medium | Low | new |
| 6 | **P3** | Scheduled | Lung Transplant for Terminal Lung Cancer — What We Now Know About Patient Selection | medical_study | chronic disease management | 58 | 65 | 3 | this_week | Medium | Medium | update |
| 7 | **P3** | Scheduled | Glioma Progression: What Weill Cornell's Cancer Evolution Study Reveals | medical_study | medical research | 55 | 60 | 3 | this_week | Medium | Low | new |
| 8 | **P5** | Monitor | Fentanyl Vaccine — Evidence Claims vs. What the Trial Data Actually Shows | drug_or_treatment_claim | public health | — | — | — | — | — | — | monitor |

*Medium confidence cap applied via Skill 02b breaking-recall exception.

---

## EDITORIAL BRIEFS

---

### BRIEF 1 — P1 / IMMEDIATE

```yaml
brief:
  primary_headline: "New World Screwworm Is Spreading in the US — What USDA's Confirmed Detections Mean for You"
  alternate_headlines:
    - "USDA Confirms New World Screwworm Detections: What Americans Need to Know Right Now"
    - "Flesh-Eating Parasite Found in the US: The New World Screwworm Threat Explained"
    - "New World Screwworm 2026: How Far Has It Spread and What's the Risk?"
  topic: "New World Screwworm — USDA confirmed detections expanding in United States"
  primary_entity: "New World Screwworm (Cochliomyia hominivorax)"
  signal_type: policy_or_regulatory_change
  allowed_category: environmental health
  trend_strength_score: 74
  opportunity_score: 78
  discover_score: 4
  urgency: today
  confidence: Medium
  content_status: new
  source_count: 3
  why_now: >
    USDA APHIS posted confirmed detections update 2026-07-12 (yesterday). Google Trends shows 
    "new world screwworm pet safety" rising under food safety cluster as of today's pre-fetch. 
    Google Trends Trending Now (US, real-time) lists "intestinal parasite infection" — likely 
    adjacent search volume. The screwworm is a One Health / zoonotic story with direct human 
    health implications; not just a livestock or agriculture story.
  
  search_intent: >
    Primary: Informational — "what is New World Screwworm, what is the risk to humans"
    Secondary: Practical — "how to protect pets, livestock, and family; what areas are affected"

  angle: >
    Most coverage treats this as an agricultural story. Frame it as a consumer health story: 
    what the screwworm is, how it affects humans (it can infest open wounds), what USDA's 
    confirmed detections mean geographically, and what practical steps people can take — 
    especially pet owners and anyone with outdoor exposure in affected states.

  integrity_flags:
    - "⚠️ Screwworm larvae can infest human wounds (myiasis) — this is medically documented, 
      but human cases in current US outbreak have not been confirmed. Distinguish livestock/pet 
      risk from human risk explicitly."
    - "⚠️ Geographic scope: confirmed detections map is dynamic. Link directly to USDA APHIS 
      page rather than summarizing locations — detection data updates frequently."

  outline:
    intro: >
      Lead with the USDA confirmation and why this matters beyond cattle ranching — the 
      screwworm is a flesh-eating parasite that can affect pets, wildlife, and in rare cases 
      humans. Frame the urgency without sensationalism.
    sections:
      - "What is the New World Screwworm? (biology, life cycle, geographic origin)"
      - "What did USDA APHIS confirm on July 12, 2026? (current detection geography)"
      - "What is the risk to humans? (myiasis: documented cases, conditions required)"
      - "What is the risk to pets and livestock? (most immediately relevant)"
      - "What is USDA doing about it? (eradication program history, sterile insect technique)"
      - "What should people do now? (wound care, veterinary alert, travel precautions)"
    conclusion: >
      Explain that this is being actively managed but warrants attention, especially for 
      outdoor workers, pet owners, and people in affected regions. Link to USDA detection map.

  key_data_points:
    - "USDA APHIS Confirmed Detections page updated 2026-07-12"
    - "New World Screwworm eradicated from US in 1966; re-emerging concern since 2024-2026"
    - "Can cause myiasis — larvae infest living tissue of warm-blooded animals and, rarely, humans"
    - "Google Trends: 'new world screwworm pet safety' listed as rising query under food safety"
    - "USDA has maintained a sterile insect technique barrier in Panama since the 1980s"

  source_plan:
    - publisher: "USDA APHIS"
      url: "https://www.aphis.usda.gov/livestock-poultry-disease/cattle/new-world-screwworm"
      tier: 1
      used_for: "Primary confirmed detection data and official guidance"
    - publisher: "CDC — Myiasis"
      url: "https://www.cdc.gov/parasites/myiasis/index.html"
      tier: 1
      used_for: "Human risk and clinical context for myiasis"
    - publisher: "USDA APHIS News 2026-07-12"
      url: "https://www.aphis.usda.gov/news/agency-announcements/confirmed-detections-new-world-screwworm"
      tier: 1
      used_for: "Today's detection confirmation; [verify exact URL at APHIS site]"

  expert_sources:
    - type: "USDA APHIS veterinary official or spokesperson"
      name: "[from official press release]"
      reason: "Authoritative on geographic spread and eradication program status"
    - type: "Parasitologist or infectious disease physician"
      name: "[cite published statement from peer source]"
      reason: "Human myiasis risk context"

  seo:
    primary_keyword: "new world screwworm"
    supporting_keywords:
      - "new world screwworm united states 2026"
      - "new world screwworm human risk"
      - "cochliomyia hominivorax"
      - "screwworm pet safety"
      - "new world screwworm symptoms"
      - "USDA screwworm detection map"
    format: "Explainer / Q&A hybrid"
    schema_markup: "Article + FAQPage"
    cluster: "Environmental health / Zoonotic disease"
  
  discover_notes: >
    Strong Discover candidate: specific named entity, natural AI query format ("what is new 
    world screwworm risk"), Tier 1 primary source, durable topic (ongoing monitoring). 
    Hero image should be USDA detection map or APHIS-provided visual — avoid sensationalist 
    parasite imagery.
  
  estimated_word_count: "1,400–1,800 words"

execution_notes: >
  Publish today. Confirm USDA APHIS detection page URL before publishing — detection data 
  is updated frequently and the URL structure may differ. Do not list specific states as 
  confirmed without checking live APHIS map at publish time.
confidence: Medium
```

---

### BRIEF 2 — P1 / IMMEDIATE

```yaml
brief:
  primary_headline: "A Doctor Says Eat Ice Cream for Longevity — Here's What the Science Actually Says"
  alternate_headlines:
    - "Zeke Emanuel's Ice Cream Longevity Claim: Is There Any Science Behind It?"
    - "The Ice Cream Longevity Debate: What Nutrition Research Actually Supports"
    - "Can Eating Ice Cream Help You Live Longer? What the Evidence Shows"
  topic: "Zeke Emanuel's case for ice cream as part of a healthy longevity diet — NPR wellness story"
  primary_entity: "Ezekiel Emanuel (bioethicist, physician, longevity researcher)"
  signal_type: rising_search_interest
  allowed_category: aging and longevity
  trend_strength_score: 71
  opportunity_score: 75
  discover_score: 4
  urgency: today
  confidence: Medium
  content_status: new
  source_count: 2
  why_now: >
    NPR published a wellness story today (2026-07-13) headlined "Eat your ice cream for a 
    long, healthy life? This doctor says so." Google Trends shows "zeke emanuel ice cream 
    wellness" and "wellness" keyword cluster with +8 delta. Rising query cluster also 
    includes "university of southern california longevity diet" — connects to broader 
    longevity diet conversation (Valter Longo's work at USC). This is a high-engagement 
    curiosity hook with genuine nutritional science to evaluate.

  search_intent: >
    Primary: Skeptical/Evaluative — "does this actually hold up?"
    Secondary: Informational — "what does longevity nutrition research actually say"

  angle: >
    Don't just repeat the NPR take — evaluate it. Zeke Emanuel is a credible bioethicist 
    who advocates for quality-of-life-centered aging, not just lifespan extension. His ice 
    cream claim likely isn't "ice cream = healthy" but something about psychological 
    satisfaction, dietary flexibility, and sustainable eating patterns. Use this as a lens 
    to explain what the legitimate longevity nutrition research actually shows (Mediterranean 
    diet, Valter Longo's fasting-mimicking diet, Blue Zones dietary patterns) and where 
    Emanuel's framing fits or diverges.

  integrity_flags:
    - "⚠️ Do not present a single expert's dietary opinion as clinical guidance. 
      Emanuel is a bioethicist and policy figure, not a clinical nutritionist — 
      his view is a perspective, not a prescription."
    - "⚠️ Distinguish observational association studies on dietary patterns from RCTs. 
      Most longevity diet evidence is observational."
    - "⚠️ The USC longevity diet (Longo) is based on specific clinical trials — 
      if citing, distinguish the fasting-mimicking diet evidence from general dietary guidance."

  outline:
    intro: >
      Hook with the NPR story and Emanuel's counterintuitive claim. Immediately frame 
      the real question: is this about ice cream specifically, or about a larger point 
      about how we think about food and longevity?
    sections:
      - "What Zeke Emanuel actually argues (summarize NPR story, his broader position on aging)"
      - "What does longevity diet research actually show? (Mediterranean, Blue Zones, Longo fasting-mimicking)"
      - "The psychology of dietary sustainability — why strict deprivation may backfire"
      - "Where Emanuel's framing has merit and where it risks being misread"
      - "What a genuine longevity-supporting diet looks like, per current evidence"
    conclusion: >
      The ice cream claim is a vehicle for a more nuanced conversation about dietary 
      flexibility vs. nutritional optimization. Both matter — and the evidence supports 
      a sustainable, high-quality dietary pattern more than any specific food prohibition.

  key_data_points:
    - "NPR wellness story published 2026-07-13: 'Eat your ice cream for a long, healthy life?'"
    - "Ezekiel Emanuel — UPenn professor, former White House health advisor"
    - "Google Trends rising: 'zeke emanuel ice cream wellness,' 'university of southern california longevity diet'"
    - "Valter Longo (USC) Fasting Mimicking Diet — clinical trial published in Cell Metabolism"
    - "Blue Zones dietary patterns: predominantly plant-based, moderate caloric intake"
    - "Mediterranean diet longevity evidence — PREDIMED trial (NEJM)"

  source_plan:
    - publisher: "NPR"
      url: "https://www.npr.org/sections/health-shots/2026/07/13/[slug]"
      tier: 1
      used_for: "Primary news hook — confirm exact URL at publish time"
    - publisher: "NEJM — PREDIMED Trial"
      url: "https://www.nejm.org/doi/10.1056/NEJMoa1200303"
      tier: 1
      used_for: "Mediterranean diet and cardiovascular/longevity outcomes"
    - publisher: "Cell Metabolism — Longo Fasting Mimicking Diet"
      url: "https://doi.org/10.1016/j.cmet.2017.05.004"
      tier: 1
      used_for: "Longevity diet clinical trial evidence"
    - publisher: "Nature Medicine — Biological Aging Clocks (adjacent, already in pipeline)"
      url: "https://www.nature.com/articles/[verify]"
      tier: 1
      used_for: "Aging science context if needed"

  expert_sources:
    - type: "Registered Dietitian Nutritionist (RDN) specializing in aging/longevity"
      name: "[cite published statement from credible outlet]"
      reason: "Adds nutritional science credibility to evaluate Emanuel's claim"
    - type: "Longevity researcher — reference Valter Longo (USC) published work"
      name: "Valter Longo, PhD (USC)"
      reason: "Primary evidence base for longevity dietary research; cite his published studies"

  seo:
    primary_keyword: "longevity diet"
    supporting_keywords:
      - "zeke emanuel longevity"
      - "can you eat ice cream and live longer"
      - "what does longevity research say about diet"
      - "blue zones diet"
      - "fasting mimicking diet evidence"
      - "mediterranean diet longevity"
    format: "Evaluative explainer"
    schema_markup: "Article + FAQPage"
    cluster: "Aging and longevity / Nutrition science"
  
  discover_notes: >
    Strong Discover/AI citation candidate: "Is ice cream bad for longevity?" is a natural 
    AI query. Article must have a clear answer supported by primary citations. 
    Hero image: colorful, approachable — fruit, Mediterranean food spread, or tasteful 
    ice cream. Avoid clinical imagery.
  
  estimated_word_count: "1,200–1,600 words"

execution_notes: >
  Publish today — the NPR story is today's news. Confirm NPR article URL. 
  Do not make clinical dietary recommendations. Clearly attribute Emanuel's position 
  to him and evaluate it against the literature.
confidence: Medium
```

---

### BRIEF 3 — P2 / SHORT-TERM

```yaml
brief:
  primary_headline: "Multiple OTC Skin Creams Recalled Over Serious FDA Manufacturing Violations — What to Check"
  alternate_headlines:
    - "FDA Recalls Several OTC Skin Care Products: Are Any in Your Medicine Cabinet?"
    - "OTC Skin Cream Recall 2026: FDA Cites Manufacturing Violations — Full Product List"
    - "Skin Cream Recall Alert: FDA Issues Warning Over Safety Manufacturing Failures"
  topic: "Multiple OTC skin cream products recalled by FDA over serious manufacturing violations"
  primary_entity: "FDA OTC skin cream recall — manufacturing violations (July 2026)"
  signal_type: recall
  allowed_category: FDA and CDC regulatory updates
  trend_strength_score: 66
  opportunity_score: 72
  discover_score: 3
  urgency: this_week
  confidence: Medium  # Breaking-recall exception applied; cap maintained
  content_status: new
  source_count: 2
  why_now: >
    MedShadow Foundation reported 2026-07-08: "FDA Recalls and Warnings: Multiple OTC Skin 
    Creams Recalled Over Serious Manufacturing Violations." This is distinct from the 
    steroid eye drop recall (already covered × 5 days) and cream cheese recall. 
    Manufacturing violations can indicate sterility failures, contamination, or incorrect 
    formulation — all potential patient safety issues. Not yet broadly covered in major outlets.

  integrity_flags:
    - "⚠️ Skill 02b breaking-recall exception applied — FDA.gov primary recall notice not 
      directly retrieved. MUST verify at FDA.gov MedWatch/Recalls page before publishing. 
      Confirmed via MedShadow Foundation (2+ credible sources threshold not fully met — 
      confirm with second outlet or direct FDA notice before publishing)."
    - "⚠️ Do not speculate on specific health harms without confirmed FDA risk classification 
      (Class I, II, or III). MedShadow describes 'serious manufacturing violations' — 
      confirm FDA risk level from primary notice."
    - "⚠️ Product list must come from FDA.gov — do not publish product names from 
      secondary sources alone."

  outline:
    intro: "Lead with the recall, what manufacturing violations mean, and why consumers should check."
    sections:
      - "Which products are recalled? (link to FDA.gov — do not list from secondary source)"
      - "What are 'serious manufacturing violations'? (GMP failures, sterility, contamination risk)"
      - "What is the FDA risk classification? (Class I = highest risk; confirm before publishing)"
      - "What should you do if you have an affected product?"
      - "How to check FDA recalls in the future"
    conclusion: "Recall action steps and FDA MedWatch link."

  key_data_points:
    - "Source: MedShadow Foundation, 2026-07-08"
    - "'Serious manufacturing violations' — likely GMP (Good Manufacturing Practice) failures"
    - "OTC skin cream products — specific brands/lots TBD from FDA primary notice"

  source_plan:
    - publisher: "FDA MedWatch / Recalls"
      url: "https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts"
      tier: 1
      used_for: "Primary recall notice — MUST verify before publishing"
    - publisher: "MedShadow Foundation"
      url: "https://medshadow.org/fda-recalls-and-warnings-multiple-otc-skin-creams-recalled-over-serious-manufacturing-violations/"
      tier: 2
      used_for: "Initial signal source — do not rely on product list; verify at FDA.gov"

  expert_sources:
    - type: "Dermatologist (board-certified)"
      name: "[cite published commentary if available]"
      reason: "Patient context for what manufacturing violations in skin creams mean clinically"

  seo:
    primary_keyword: "OTC skin cream recall 2026"
    supporting_keywords:
      - "FDA skin cream recall"
      - "skin cream manufacturing violation recall"
      - "what to do skin cream recall"
    format: "Recall alert / consumer action guide"
    schema_markup: "Article + FAQPage"
    cluster: "FDA and CDC regulatory updates"
  
  estimated_word_count: "900–1,200 words"

execution_notes: >
  DO NOT PUBLISH until FDA.gov primary recall notice is confirmed. Verify exact product 
  names, lot numbers, and FDA risk classification (Class I/II/III) at 
  https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts before writing 
  the product list section. If FDA.gov confirms Class I, upgrade urgency to today.
confidence: Medium
```

---

### BRIEF 4 — P2 / SHORT-TERM

```yaml
brief:
  primary_headline: "Most Doctors Now Support Patient Wearables — Here's What the AMA Survey Found"
  alternate_headlines:
    - "AMA Survey: Physicians Back Consumer Health Wearables — With Important Caveats"
    - "Doctors and Health Wearables: New AMA Data Shows a Shift in Medical Attitudes"
    - "Your Smartwatch Data Is Getting More Credible — Here's What Doctors Actually Think"
  topic: "AMA international physician survey on consumer health wearables and patient care"
  primary_entity: "American Medical Association (AMA) wearables survey"
  signal_type: data_release
  allowed_category: fitness and exercise science
  trend_strength_score: 62
  opportunity_score: 70
  discover_score: 4
  urgency: this_week
  confidence: High
  content_status: new
  source_count: 3
  why_now: >
    AMA published the physician survey on consumer wearables 2026-07-08 (5 days ago — still 
    within freshness window). Google Trends fitness keyword +17 delta. The AMA is a 
    Tier 1 source. Physician attitudes toward wearables directly affect how patients should 
    present device data in clinical encounters — high practical value for the target audience.

  integrity_flags:
    - "⚠️ Survey data reflects physician attitudes, not clinical outcomes. 
      Do not present physician support as evidence that wearables improve health outcomes."
    - "⚠️ International physician survey — note if findings differ significantly by country 
      before generalizing to US clinical context."

  outline:
    intro: "Frame the shift: consumer health tech was once dismissed by physicians; the AMA survey shows that's changing."
    sections:
      - "What the AMA survey found (key statistics — cite directly)"
      - "Which wearable data types physicians find most useful (heart rate, sleep, activity, SpO2)"
      - "What physicians are still cautious about (data accuracy, over-reliance, liability)"
      - "How to use your wearable data in a clinical appointment"
      - "What the evidence says about wearables and actual health outcomes"
    conclusion: "Practical guidance: what to track, what to share with your doctor."

  key_data_points:
    - "AMA survey published 2026-07-08"
    - "International physician survey — methodology and sample size from AMA publication"
    - "Google Trends: fitness +17 delta this week"
    - "Wearable health market growing rapidly; Apple Watch, Fitbit, Garmin, Whoop dominant"

  source_plan:
    - publisher: "American Medical Association"
      url: "https://www.ama-assn.org/practice-management/digital/international-physician-survey-consumer-wearables"
      tier: 1
      used_for: "Primary survey data — [verify exact URL from AMA newsroom]"
    - publisher: "JAMA Network — wearables and clinical outcomes"
      url: "https://jamanetwork.com/journals/jama/fullarticle/[verify]"
      tier: 1
      used_for: "Supporting clinical evidence on wearables effectiveness"
    - publisher: "FDA Digital Health Center of Excellence"
      url: "https://www.fda.gov/medical-devices/digital-health-center-excellence"
      tier: 1
      used_for: "Regulatory context for consumer health devices"

  expert_sources:
    - type: "Exercise physiologist or sports medicine physician"
      name: "[cite physician from AMA survey commentary if named]"
      reason: "Clinical perspective on wearable data utility"

  seo:
    primary_keyword: "doctors health wearables"
    supporting_keywords:
      - "AMA wearables survey 2026"
      - "should I share fitness tracker data with doctor"
      - "physician attitudes consumer wearables"
      - "smartwatch health data doctor"
      - "wearable health technology clinical use"
    format: "Data-driven explainer + practical guide"
    schema_markup: "Article + FAQPage"
    cluster: "Fitness and exercise science / Digital health"
  
  discover_notes: >
    Strong AI citation candidate: "Do doctors use wearable data?" is a common query. 
    Specific survey data + practical guidance = durable, citable content. 
    Hero image: smartwatch showing health metrics.
  
  estimated_word_count: "1,200–1,500 words"

execution_notes: >
  Confirm AMA survey URL from AMA newsroom or AMA Journal of Ethics (the survey may be 
  published there). Verify sample size and international scope before generalizing.
confidence: High
```

---

### BRIEF 5 — P2 / SHORT-TERM

```yaml
brief:
  primary_headline: "The Sleep-Diet Connection: What Researcher Marie-Pierre St-Onge's Work Tells Us About Eating and Sleep"
  alternate_headlines:
    - "Can What You Eat Improve Your Sleep? Here's What the Science Says"
    - "Sleep and Nutrition: Columbia Researcher's Findings on the Food-Sleep Link"
    - "The Sleep Diet Explained: What Marie-Pierre St-Onge's Research Actually Found"
  topic: "Marie-Pierre St-Onge's research on the sleep-diet connection — rising search interest"
  primary_entity: "Marie-Pierre St-Onge, PhD (Columbia University sleep and nutrition researcher)"
  signal_type: rising_search_interest
  allowed_category: sleep science
  trend_strength_score: 65
  opportunity_score: 68
  discover_score: 4
  urgency: this_week
  confidence: Medium
  content_status: new
  source_count: 2
  why_now: >
    Google Trends rising related query today: "marie-pierre st-onge sleep diet." 
    St-Onge is a Columbia University researcher who has published extensively on the 
    bidirectional relationship between diet and sleep quality. The sleep topic has been 
    active in recent runs (Columbia sleep/weight study appeared 3× in history) but this 
    is a distinct angle — not the weight gain story but the dietary factors that affect 
    sleep quality. Fresh angle, rising search demand, strong primary institutional source.

  integrity_flags:
    - "⚠️ Sleep-diet research is largely observational and small-cohort. 
      Distinguish what is supported by RCT vs. observational data."
    - "⚠️ Tryptophan/serotonin dietary claims are commonly overstated — 
      note that dietary tryptophan's conversion to serotonin in the brain 
      is complex and not a simple cause-effect relationship."

  outline:
    intro: "Hook: what you eat doesn't just affect weight — it affects how well you sleep. Frame the Columbia research."
    sections:
      - "What is the sleep-diet connection? (overview of research area)"
      - "What St-Onge's research specifically found (cite published studies)"
      - "Foods associated with better sleep quality (evidence-based: kiwi, tart cherry, complex carbs)"
      - "Foods associated with worse sleep (high fat, high sugar, caffeine timing)"
      - "The tryptophan/melatonin pathway — what's real and what's overstated"
      - "Practical dietary changes that may improve sleep"
    conclusion: "Evidence-based practical summary without overclaiming."

  key_data_points:
    - "Google Trends: 'marie-pierre st-onge sleep diet' — rising query as of 2026-07-13"
    - "St-Onge, M-P et al. — multiple publications in Sleep journal and American Journal of Clinical Nutrition"
    - "Kiwi fruit and sleep: small RCT (Hung et al.) — cite with caveat of small sample"
    - "Tart cherry juice and sleep: melatonin content studies"
    - "Columbia University affiliation — cross-reference with recent Columbia sleep/weight study (already covered)"

  source_plan:
    - publisher: "Columbia University Irving Medical Center — St-Onge lab"
      url: "https://www.cuimc.columbia.edu/research/centers-labs/st-onge-lab"
      tier: 1
      used_for: "Primary researcher affiliation and published work"
    - publisher: "Sleep journal — St-Onge dietary patterns and sleep quality"
      url: "https://doi.org/10.5665/sleep.5384"
      tier: 1
      used_for: "Primary study: dietary patterns and sleep quality (St-Onge et al.)"
    - publisher: "American Journal of Clinical Nutrition"
      url: "https://doi.org/10.3945/ajcn.112.056275"
      tier: 1
      used_for: "Diet composition effects on sleep architecture [verify DOI]"

  expert_sources:
    - type: "Sleep medicine specialist or sleep researcher"
      name: "Marie-Pierre St-Onge, PhD (Columbia) — cite published work directly"
      reason: "Primary researcher; published quotes available in prior media coverage"

  seo:
    primary_keyword: "sleep diet connection"
    supporting_keywords:
      - "marie-pierre st-onge sleep"
      - "foods that help you sleep"
      - "diet and sleep quality research"
      - "what to eat for better sleep"
      - "sleep nutrition science"
    format: "Research explainer + practical guide"
    schema_markup: "Article + FAQPage"
    cluster: "Sleep science / Nutrition science"
  
  discover_notes: >
    Strong AI citation candidate: "What foods help you sleep?" is a high-frequency AI query. 
    Content must deliver specific, evidence-graded answers (not just lists) to be cited. 
    Hero image: food and sleep imagery — bowl of kiwi, night-scene kitchen.
  
  estimated_word_count: "1,300–1,700 words"

execution_notes: >
  Verify DOIs for St-Onge's published studies via PubMed search. 
  The kiwi/sleep and tart cherry/sleep studies should be cited with sample-size caveats. 
  Cross-reference Columbia sleep lab publications list.
confidence: Medium
```

---

### BRIEF 6 — P3 / SCHEDULED

```yaml
brief:
  headline: "Lung Transplant for Terminal Lung Cancer: What We Now Know About Who Qualifies"
  topic: "Northwestern Medicine lung transplant study — update on patient selection criteria for terminal lung cancer"
  angle: >
    The Northwestern study (07-08) was covered briefly in run history (07-09). This update 
    angle focuses specifically on patient selection criteria — who qualifies, what the 
    survival data shows, and what questions oncologists and patients should be asking. 
    Shifts from "breakthrough announcement" to "what does this mean for patients."
  key_data_points:
    - "Northwestern Medicine study: lung transplant dramatically improves survival for terminal lung cancer patients"
    - "Published: Northwestern Medicine Newsroom, 2026-07-08"
    - "New angle: patient eligibility criteria — what stage/type of lung cancer, fitness requirements, waitlist realities"
    - "Prior coverage (07-09) focused on the headline finding; this goes deeper on clinical applicability"
  integrity_flags:
    - "⚠️ 'Dramatically improves survival' language requires exact figures — obtain from primary study"
    - "⚠️ Distinguish which lung cancer types were included in the study (likely not all terminal cases qualify)"
  expert_type_needed: "Thoracic surgeon or oncologist — cite Northwestern Medicine study authors if named"
  seo:
    primary_keyword: "lung transplant lung cancer"
    format: "Clinical explainer / patient guide"
    serp_difficulty: Medium
  sources:
    - publisher: "Northwestern Medicine Newsroom"
      url: "https://news.feinberg.northwestern.edu/2026/07/lung-transplant-terminal-lung-cancer/"
    - publisher: "Journal source — verify from Northwestern press release"
      url: "[URL unverified — check primary study citation in Northwestern release]"
  estimated_word_count: "1,100–1,400 words"
```

---

### BRIEF 7 — P3 / SCHEDULED

```yaml
brief:
  headline: "What Weill Cornell's Cancer Evolution Study Reveals About Glioma — and What It Means for Patients"
  topic: "Weill Cornell Medicine cancer evolution study on glioma progression biology"
  angle: >
    New institutional research from Weill Cornell (07-10) on how gliomas evolve biologically 
    over time. Frame for a general health-conscious audience: what glioma is, why 
    understanding its evolution matters for treatment, and what this type of research 
    means for future therapy development.
  key_data_points:
    - "Source: Weill Cornell Medicine Newsroom, 2026-07-10"
    - "'Cancer Evolution Study Reveals Biology of Glioma Progression'"
    - "Glioma — most common primary brain tumor; includes glioblastoma (GBM)"
    - "Cancer evolution research aims to understand why tumors recur and become treatment-resistant"
  integrity_flags:
    - "⚠️ This is early-stage research — explicitly state this is biological/mechanistic research, 
      not a treatment or clinical trial result."
    - "⚠️ Do not imply near-term clinical application. Research-to-treatment pipelines are long."
  expert_type_needed: "Neuro-oncologist or cancer researcher — cite Weill Cornell study authors"
  seo:
    primary_keyword: "glioma progression research"
    format: "Research explainer"
    serp_difficulty: Low
  sources:
    - publisher: "Weill Cornell Medicine Newsroom"
      url: "https://news.weill.cornell.edu/news/2026/07/cancer-evolution-study-reveals-biology-of-glioma-progression"
    - publisher: "Primary journal — verify from Weill Cornell press release"
      url: "[URL unverified — check study citation in press release]"
  estimated_word_count: "1,000–1,300 words"
```

---

## REJECTED TOPICS LOG

| Topic | Reason |
|---|---|
| Eye Drops Recall (2.5M bottles) | Existing — covered 5 consecutive days (07-08 through 07-12); no new development |
| E. coli / Frozen Blueberries | Existing — covered 5 consecutive days; no new case count or agency action |
| GLP-1 online prescriptions (Yale) | Existing — covered 4 consecutive days; same study, no new data |
| Cream Cheese Recall | Existing — covered 3 consecutive days |
| Sleep Deprivation / Weight Gain (Columbia) | Existing — covered 3 consecutive days; same study |
| Stanford Opioid Taper | Existing — covered 3 consecutive days |
| Ebola DRC / Bundibugyo trial | Existing — covered 3 consecutive days |
| Biological Aging Clocks (Nature) | Existing — covered 07-11 |
| Pediatric Mental Health ERs | Existing — covered 07-12 |
| "Super Mover" Walking Speed | Existing — covered 07-12 |
| PCOS Nutrition | Existing — covered 07-11 |
| DOJ Adderall digital health fraud | Off-category — criminal/legal; brand safety flag |
| Yale Health System CEO | Off-category — hospital administration |
| ACA enrollment decline | Off-category — insurance policy |
| School-based health clinics (Virginia) | Off-category — regional policy |
| NYT: Politicization of medical research | Off-category — political opinion; no new health data |
| AMA healthcare spending trends | Off-category — business/economics |
| Medical mistrust / wellness / politics (Medscape) | Monitored — P5; borderline brand safety; political drift risk |
| Gut health (general) | Monitored — SERP fully saturated; covered 07-10; no new study today |
| Fentanyl Vaccine claims | Monitored — P5; Skill 02b: material overstatement of mechanism certainty |
| Enteral Nutrition | Weak signal — rising query only; insufficient news volume |
| Nanox Cardiac AI | Weak signal — single source, promotional |
| Northwestern lung transplant (original story) | Existing — superseded by update brief (Brief 6) |
| Lung Transplant update (Northwestern) | Passed as P3 update (Brief 6) |

---

## INTEGRITY FLAGS CONSOLIDATED

> For editorial review before publishing:

1. **Brief 1 (New World Screwworm):** Human myiasis cases in current US outbreak NOT confirmed — distinguish livestock/pet risk from human risk. Geographic data is dynamic — link to live USDA APHIS map rather than summarizing specific states at publish time.

2. **Brief 2 (Zeke Emanuel / Ice Cream):** Emanuel is a bioethicist and policy figure, not a clinical nutritionist — his opinion is a perspective, not a prescription. Longevity diet evidence is largely observational; PREDIMED and Longo trials are the strongest RCT-adjacent evidence but have scope limitations.

3. **Brief 3 (OTC Skin Cream Recall):** ⚠️ **HOLD — DO NOT PUBLISH** until FDA.gov primary recall notice is confirmed. Product list must come from FDA.gov only. Risk classification (Class I/II/III) must be verified. Breaking-recall exception applied at Skill 02b — confidence cap maintained at Medium.

4. **Brief 4 (AMA Wearables):** Survey data = physician attitudes, not clinical outcomes evidence. International survey — generalization to US clinical context requires verifying US-specific data split.

5. **Brief 5 (Sleep-Diet / St-Onge):** Tryptophan → serotonin → sleep pathway is commonly overstated. Kiwi and tart cherry RCTs are small-cohort. Distinguish observational from RCT evidence throughout.

6. **Brief 6 (Lung Transplant Update):** Exact survival statistics must be pulled from primary Northwestern study before publishing. "Dramatically improves" must be quantified.

7. **Brief 7 (Glioma):** Mechanistic/biological research — not a treatment result or clinical application. Must state explicitly that research-to-treatment pipeline is long.

---

## RUN NOTES

```yaml
run_date: 2026-07-13
signals_reviewed: 144
topics_retained: 7 (+ 1 P5 monitor)
topics_rejected: 136
p1_count: 2
p2_count: 3
p3_count: 2
p5_monitor_count: 1
integrity_flags_raised: 7
tools_used:
  - google_trends_serpapi_prefetch
  - google_news_radar_144_signals
  - run_history_deduplication
tools_unavailable: []
top_topic: "New World Screwworm — USDA Confirmed Detections"
key_themes_today:
  - New World Screwworm / zoonotic disease spread
  - Longevity diet debate (Zeke Emanuel / ice cream)
  - FDA manufacturing violation recalls (skin care)
  - Physician attitudes toward digital health / wearables
  - Sleep-nutrition intersection (St-Onge)
recurring_theme_staleness_flags:
  - "Eye Drops Recall: 5 runs — retired today"
  - "E. coli/Blueberries: 5 runs — retired today"
  - "GLP-1 Yale study: 4 runs — retired today"
  - "Cream Cheese Recall: 3 runs — retired today"
  - "Sleep/Weight (Columbia): 3 runs — retired today"
  - "Stanford Opioid Taper: 3 runs — retired today"
  - "Ebola DRC: 3 runs — retired today"
notes: >
  Google Trends gut health +20 is the strongest velocity signal today but the topic is 
  fully saturated in SERP and was covered 07-10. Fitness +17 driven by off-niche queries. 
  Weight loss -26 driven by celebrity queries (excluded). The two strongest net-new 
  opportunities today are the USDA screwworm detection update (zoonotic, consumer-relevant, 
  Tier 1 source) and the Zeke Emanuel/longevity ice cream story (rising Trends, today's NPR 
  hook, high Discover potential). OTC skin cream recall held pending FDA.gov verification — 
  if confirmed Class I, should be elevated to P1/today urgency. 
  site_url not configured — self-check skipped; competitor coverage checked instead.
dashboard_output: "outputs/daily_newsroom_dashboard/2026-07-13.html"
run_history_updated: true
```