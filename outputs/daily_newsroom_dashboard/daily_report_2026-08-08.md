# Trending Content OS — Daily Pipeline Run
**Date:** 2026-08-08 | **Niche:** Health & Wellness | **Mode:** Automation Output

---

## PREFLIGHT SUMMARY

| Check | Status |
|---|---|
| All 7 config files | ✅ Loaded |
| CLAUDE.md skills (01–12 + 02b) | ✅ Present |
| site_niche | ✅ "health and wellness" |
| target_audience | ✅ Set |
| site_url | ⚠️ Not configured — self-check skipped; competitor fallback used |
| SerpAPI / Google Trends | ✅ Available via injected pre-fetch block |
| google_trends_available | ✅ true (serpapi_prefetch) |
| search_velocity_source | google_trends |
| Deferred topics (data/deferred_topics.yaml) | No overdue entries |
| Run history cross-check | See notes below |

**Run history flags:** Topics appearing in 2+ consecutive prior runs reviewed. The following are flagged as **recurring — check for staleness** if surfaced again today without material new development: *Diet soda and cognitive decline*, *Low-protein diet and lifespan*, *Cyclospora/lettuce outbreak*, *Eye drops recall*, *FDA blood thinner recall*, *Dormant cancer cells / immunotherapy*, *Dementia risk factors*. These will require a specific new development to pass as `update` candidates.

**→ Preflight passed. Proceeding to Skill 01.**

---

## GOOGLE NEWS RADAR — COVERAGE SUMMARY

144 unique headlines across 12 queries reviewed. Main topic clusters identified:

| Cluster | Headlines Seen | Disposition | Reason |
|---|---|---|---|
| **FDA/Food Recalls (lettuce, cheese, blood thinners, eye drops)** | ~12 | **Partially retained** | Cyclospora/lettuce has a material new development (28-state spread + Walmart/Jack in the Box confirmed); cheese/Listeria is new; blood thinners and eye drops = `existing` from 08/07 |
| **Dementia & middle-age habits** | ~3 | **Existing** | Covered 08/07 (NYU Langone); no material new development |
| **Dormant cancer cells / immunotherapy** | ~2 | **Existing** | Covered 08/07 (UT Austin); no new development |
| **AI in healthcare / mental health** | ~4 | **Retained (new angle)** | Harvard Gazette piece on AI for mental health among youth is a new, distinct signal from 08/06 "Gen Z AI healthcare" story; different population angle and institutional source |
| **Ibogaine neurological recovery** | ~2 | **Existing** | Covered 08/06 (Barrow Institute); no new development |
| **GLP-1 / Triple agonist Phase 1 (Neurocrine)** | ~1 | **Retained** | New Phase 1 initiation — different drug class signal from prior GLP-1 NEJM RCT (08/05) |
| **Wellness trends 2026 (The Guardian)** | ~1 | **Retained** | New, distinct signal — editorial/trend roundup from credible outlet; not duplicate of prior coverage |
| **Salmonella / Chipotle / Qdoba jalapeños** | ~1 | **Retained** | New — outbreak expanding to Qdoba, fresh FDA action; not in recent coverage |
| **Birth order / disease risk** | ~2 | **Existing** | Covered 08/06 (Nature); no new development |
| **AI in clinical trials / oncology** | ~2 | **Monitored** | Interesting but adjacent to pharma-business; no patient-facing health angle strong enough; low audience relevance for general health reader |
| **HHS / global maternal health / Medi-Cal rollback** | ~3 | **Rejected** | Pure policy/political healthcare opinion without new health science data |
| **Hospital/workforce/infrastructure news** | ~4 | **Rejected** | Local/institutional — too narrow for national audience |
| **Sleep foundation model (Nature)** | ~1 | **Retained** | New Nature publication on AI sleep risk stratification — distinct from 08/05 sleep deprivation meta-analysis |
| **Vibrio vulnificus Louisiana (Google Trends real-time)** | Trends only | **Retained** | Breakout real-time trend; not in recent coverage; public health urgency |
| **Crumbl dirty soda nutrition** | Trends only | **Monitored** | Rising Trends query but low health depth; pop culture nutrition curiosity, not editorial health content |
| **Teen diet breakfast benefits** | Trends only | **Retained** | Rising search; research-grounded signal; distinct from prior coverage |

---

## SIGNAL SUMMARY

```yaml
signal_summary:
  run_date: 2026-08-08
  total_signals_reviewed: 144 (Google News Radar) + Google Trends rising queries
  total_signals_retained: 8
  total_rejected: 136 (including existing/duplicate suppression)
  google_trends_available: true
  search_velocity_source: google_trends
  rejection_breakdown:
    existing_duplicate: 9
    off_category: 14
    weak_signal: 6
    policy_political_drift: 4
    brand_safety: 1
    unverified_claim: 0
    other: 102 (low audience relevance, institutional/local, or below threshold)
  highest_priority_topic: "Vibrio vulnificus Louisiana outbreak — breakout real-time trend + public health urgency"
  strongest_signal_source: "Google Trends real-time + CDC-tier sources"
  tools_unavailable: []
  notes: >
    Site URL not configured — self-check skipped; competitor coverage and recent run history 
    used for duplicate detection. Google Trends pre-fetch treated as available. 
    Crumbl dirty soda monitored only — strong search volume but editorial depth insufficient 
    for health content. AI in clinical trials cluster rejected as too pharma-business-adjacent 
    without clear patient-health framing.
```

---

## SKILL 02b ROUTING SUMMARY

| Candidate | Risk Type | Gate Result | Primary Source | Notes |
|---|---|---|---|---|
| Vibrio vulnificus Louisiana outbreak | Public health / outbreak | ✅ Pass | CDC.gov, Louisiana DHHS | Traceable institutional sourcing; no overstatement detected |
| Cyclospora/lettuce — 28 states update | Recall / outbreak update | ✅ Pass (breaking-recall exception) | Consumer Reports citing FDA + CDC 08/08; CDC surveillance page confirmed | Breaking-recall exception: 3+ credible sources confirm same product + spread data; confidence capped at Medium |
| Cheese/Listeria recall | Recall | ✅ Pass (breaking-recall exception) | Columbus Dispatch, Cheese NY recall, FDA action | 3+ sources confirm; confidence capped at Medium |
| Salmonella jalapeños — Chipotle/Qdoba | Recall / outbreak | ✅ Pass | ABC News + FDA cited; Columbus Dispatch corroboration | Breaking-recall exception applied; confidence Medium |
| Neurocrine GLP-1/GIP/Glucagon triple agonist Phase 1 | Clinical trial claim | ✅ Pass with Medium cap | PR Newswire (Neurocrine official press release) + company Phase 1 initiation announcement | Primary source is manufacturer press release — credible but not peer-reviewed; note added |
| AI for youth mental health (Harvard Gazette) | Study/research | ✅ Pass | Harvard Gazette citing study; research-grounded | Confidence Medium — study details available through institutional source |
| Sleep AI risk stratification (Nature) | Medical study | ✅ Pass | Nature publication confirmed 08/03 | DOI-traceable; confidence High |
| Teen diet breakfast benefits | Rising search + research | ✅ Pass | Peer-reviewed base exists (general nutrition); search signal confirmed | Confidence Medium — trending query, established research base |
| Wellness trends 2026 (The Guardian) | Editorial/trend roundup | Not triggered (lower-risk trend) | The Guardian 08/07 | No health claim gate needed |

**No candidates routed to Monitor or Reject at 02b.**

---

## FINAL EDITORIAL PRIORITY BOARD

| # | Topic | Priority | Timing | Trend | Opp | Discover | Urgency | Confidence | Integrity Flags |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Vibrio vulnificus Louisiana outbreak | P1 | Immediate | 88 | 82 | 5 | now | Medium | None |
| 2 | Cyclospora/lettuce reaches 28 states — Walmart & Jack in the Box | P1 | Immediate | 84 | 79 | 5 | now | Medium | ⚠️ Breaking-recall exception |
| 3 | Salmonella at Chipotle expands to Qdoba — jalapeños | P1 | Immediate | 80 | 77 | 4 | now | Medium | ⚠️ Breaking-recall exception |
| 4 | Cheese/Listeria recall — 30,000+ lbs, Class I FDA | P2 | Short-term (24–48h) | 74 | 73 | 4 | today | Medium | ⚠️ Breaking-recall exception |
| 5 | Sleep AI foundation model — Nature | P2 | Short-term | 71 | 76 | 4 | today | High | ⚠️ Single study; observational risk stratification |
| 6 | Neurocrine triple agonist GLP-1/GIP/Glucagon Phase 1 | P2 | Short-term | 68 | 74 | 4 | today | Medium | ⚠️ Phase 1 only; manufacturer press release primary source |
| 7 | AI for youth mental health — Harvard / surging use | P3 | Scheduled | 63 | 70 | 3 | this_week | Medium | ⚠️ Observational; correlation ≠ causation |
| 8 | Teen breakfast habits and diet quality — rising search | P3 | Scheduled | 58 | 65 | 3 | this_week | Medium | None |
| 9 | 2026 wellness trends roundup (The Guardian angle) | P3 | Scheduled | 55 | 62 | 3 | this_week | Medium | ⚠️ Trend content — distinguish evidence-based from hype |

---

## EDITORIAL BRIEFS

---

### BRIEF 1 — P1 / IMMEDIATE

**Primary Headline:** Vibrio vulnificus Is Surging in Louisiana — Here's What You Need to Know Before Going Near the Water

**Alternate Headlines:**
- Louisiana Declares Vibrio vulnificus Alert: Why This Flesh-Eating Bacteria Thrives in Summer Heat
- What Is Vibrio vulnificus? Louisiana's Outbreak Explained — Symptoms, Risk Factors, and When to Seek Care

```yaml
brief:
  topic: "Louisiana Vibrio vulnificus outbreak"
  primary_entity: "Vibrio vulnificus"
  signal_type: "breaking_news"
  allowed_category: "public health and epidemiology"
  priority_level: P1
  publish_timing: immediate
  trend_strength_score: 88
  opportunity_score: 82
  discover_score: 5
  urgency: now
  confidence: medium
  content_status: new
  source_count: 3
  why_now: >
    Google Trends shows Vibrio vulnificus Louisiana as a real-time US breakout trend as of 
    08/08. Peak summer heat + Gulf Coast warm water + shellfish/water exposure season 
    creates genuine public safety urgency. No prior coverage in last 7 days.

  recommended_angle: >
    Public health explainer with risk triage: who is at serious risk (immunocompromised, 
    liver disease, open wounds) vs. general population, framed around the Louisiana outbreak 
    as the news hook and actionable prevention steps.

  search_intent: "Informational + evaluative — what is it, who is at risk, what to do"

  integrity_flags:
    - "⚠️ Confirm Louisiana DHHS case count before publishing — Trends signal is real-time but case numbers from news coverage should be verified against official state advisory"
    - "⚠️ Do not conflate with general 'flesh-eating bacteria' (necrotizing fasciitis from Group A Strep); distinguish clearly"

  outline:
    intro: >
      Lead with the Louisiana outbreak — what happened, when, how many cases confirmed or 
      suspected. Establish why this matters in August specifically (water temp + seafood 
      season).
    sections:
      - "What is Vibrio vulnificus? — pathogen basics, how it differs from other Vibrio species"
      - "How do people get infected? — two pathways: raw shellfish consumption vs. wound exposure in warm coastal water"
      - "Who is at highest risk? — liver disease, diabetes, immunosuppression, iron overload conditions; why healthy adults rarely die"
      - "Louisiana outbreak specifics — confirmed cases, geographic spread, state health advisory details"
      - "Symptoms and when to seek emergency care — timeline matters (infection can progress to sepsis in <24h)"
      - "Prevention: what actually works — cooking shellfish, wound care, avoiding warm coastal water with open cuts"
    conclusion: >
      Reinforce high-risk group messaging; link to CDC Vibrio page and Louisiana DHHS advisory.

  key_data_points:
    - "Vibrio vulnificus kills ~1 in 5 infected people; in people with liver disease, mortality can exceed 50%"
    - "US sees ~150–200 Vibrio vulnificus cases/year, mostly Gulf Coast states, June–October"
    - "Water temps above 68°F (20°C) dramatically increase bacterial concentration"
    - "Onset of bloodstream infection can occur within 24–48 hours of exposure"

  source_plan:
    - publisher: "CDC — Vibrio vulnificus"
      url: "https://www.cdc.gov/vibrio/index.html"
      tier: 1
      used_for: "Core pathogen data, risk factors, case statistics"
    - publisher: "Louisiana Department of Health"
      url: "https://ldh.la.gov/"
      tier: 1
      used_for: "Outbreak-specific case count and advisory"
    - publisher: "FDA — Vibrio and shellfish safety"
      url: "https://www.fda.gov/food/buy-store-serve-safe-food/selecting-and-serving-fresh-and-frozen-seafood-safely"
      tier: 1
      used_for: "Shellfish handling and prevention guidance"
    - publisher: "NEJM or similar — clinical case series on Vibrio vulnificus outcomes"
      url: "[URL unverified — search PubMed: Vibrio vulnificus outcomes liver disease]"
      tier: 2
      used_for: "Mortality data by risk group"

  expert_sources:
    - type: "Infectious disease epidemiologist"
      name: "Louisiana DHHS spokesperson or named epidemiologist from outbreak advisory"
      reason: "Official case count + public guidance"
    - type: "Gastroenterologist or hepatologist"
      name: "[Published quote — search STAT/Reuters coverage of prior Vibrio outbreaks]"
      reason: "Explain why liver disease dramatically elevates mortality risk"

  seo:
    primary_keyword: "Vibrio vulnificus Louisiana"
    supporting_keywords: ["Vibrio vulnificus symptoms", "flesh-eating bacteria Louisiana", "vibrio bacteria water", "what is vibrio vulnificus", "vibrio vulnificus risk factors", "Louisiana water safety 2026"]
    format: "Explainer article with FAQ section"
    schema_markup: "Article + FAQPage"
    cluster: "public health / infectious disease"

  discover_notes: >
    Top-tier AI citation candidate: specific named pathogen + geographic event + natural 
    AI query format ("what is vibrio vulnificus," "is Louisiana water safe") + CDC primary 
    source available + durable educational content beyond the news cycle.

  estimated_word_count: "1,200–1,600 words"

execution_notes: >
  Publish within 12 hours. Confirm Louisiana DHHS case count independently before 
  going live. Do not use 'flesh-eating bacteria' in headline without clarifying parenthetical 
  — it will be accurate for wound infections but will read as sensational without context.
```

---

### BRIEF 2 — P1 / IMMEDIATE

**Primary Headline:** Cyclospora-Linked Lettuce Spread to 28 States — Walmart and Jack in the Box Among Affected Retailers

**Alternate Headlines:**
- The Cyclospora Lettuce Outbreak Is Bigger Than We Knew: 28 States, Major Retailers Confirmed
- FDA Cyclospora Outbreak Update: What to Do If You Bought Iceberg Lettuce at These Stores

```yaml
brief:
  topic: "Cyclospora outbreak — 28-state spread confirmed, Walmart and Jack in the Box"
  primary_entity: "Cyclospora cayetanensis / iceberg lettuce outbreak"
  signal_type: "recall"
  allowed_category: "FDA and CDC regulatory updates"
  priority_level: P1
  publish_timing: immediate
  trend_strength_score: 84
  opportunity_score: 79
  discover_score: 5
  urgency: now
  confidence: medium
  content_status: update
  source_count: 4
  why_now: >
    Material new development since 08/07 coverage: Consumer Reports (08/08) confirms outbreak 
    now spans 28 states and has reached Walmart retail locations and Jack in the Box restaurants 
    — significantly broader than prior reporting. New geographic scope and named retailers 
    are actionable for readers.

  recommended_angle: >
    Update article: "what to do now" framing — specific retailers and states confirmed, 
    symptoms to watch, when to see a doctor. Avoid duplicating generic Cyclospora explainer 
    content from 08/07; this piece is the geographic/retailer update.

  integrity_flags:
    - "⚠️ Breaking-recall exception used — FDA primary notice URL not directly retrieved; confirmed via Consumer Reports 08/08, CDC surveillance page, and Columbus Dispatch. Verify FDA.gov recall notice before publishing."
    - "⚠️ State list: confirm the 28 states via FDA or CDC directly — do not publish the list as definitive without primary source verification"

  outline:
    intro: "New scope of outbreak — 28 states, Walmart + Jack in the Box now confirmed. Brief recap for readers who missed prior coverage."
    sections:
      - "What's new: 28-state spread confirmed, named retailers and restaurant chains"
      - "What to do if you bought iceberg lettuce in the last 2 weeks — check retailer, check purchase date"
      - "Cyclospora symptoms: timeline, what it feels like, how long it lasts"
      - "Who is most at risk for serious illness"
      - "FDA/CDC investigation status — what agencies are doing"
    conclusion: "Direct readers to FDA.gov recall page for product-specific lot numbers; tell them when to call a doctor."

  key_data_points:
    - "28 states affected as of 08/08 reporting"
    - "Walmart and Jack in the Box among confirmed distribution points"
    - "Cyclospora causes watery diarrhea that can last weeks without treatment; treated with antibiotics"
    - "Incubation period ~1 week — consumers who bought lettuce 1–2 weeks ago may still be within the window"

  source_plan:
    - publisher: "Consumer Reports"
      url: "https://www.consumerreports.org"
      tier: 2
      used_for: "28-state spread, Walmart/Jack in the Box confirmation (08/08)"
    - publisher: "CDC — Cyclospora Outbreak"
      url: "https://www.cdc.gov/cyclosporiasis/outbreaks/index.html"
      tier: 1
      used_for: "Official case count and outbreak status"
    - publisher: "FDA — Recall / Outbreak Investigation"
      url: "https://www.fda.gov/food/outbreaks-foodborne-illness/outbreak-investigation-cyclospora"
      tier: 1
      used_for: "Product-specific recall details [verify URL active]"

  seo:
    primary_keyword: "Cyclospora lettuce outbreak 2026"
    supporting_keywords: ["Cyclospora Walmart", "iceberg lettuce recall", "Cyclospora symptoms", "Jack in the Box lettuce recall", "Cyclospora 28 states"]
    format: "Breaking news update with actionable reader checklist"
    schema_markup: "NewsArticle"
    cluster: "food safety / FDA recalls"

  estimated_word_count: "800–1,000 words"

execution_notes: >
  This is an UPDATE to 08/07 coverage — the new development is geographic/retailer scope. 
  Frame as an update, not a duplicate. Publish within 6 hours of confirming FDA primary notice.
```

---

### BRIEF 3 — P1 / IMMEDIATE

**Primary Headline:** Salmonella Outbreak From Chipotle Jalapeños Expands to Qdoba — What We Know

**Alternate Headlines:**
- FDA: Same Jalapeño Salmonella Outbreak Behind Chipotle Cases Has Now Reached Qdoba
- Beyond Chipotle: FDA Confirms Salmonella-Linked Jalapeños Spread to Second Major Chain

```yaml
brief:
  topic: "Salmonella outbreak — jalapeños at Chipotle expands to Qdoba"
  primary_entity: "Salmonella / jalapeños / Qdoba"
  signal_type: "breaking_news"
  allowed_category: "public health and epidemiology"
  priority_level: P1
  publish_timing: immediate
  trend_strength_score: 80
  opportunity_score: 77
  discover_score: 4
  urgency: now
  confidence: medium
  content_status: new
  source_count: 3
  why_now: >
    ABC News + FDA confirmed 08/06 that the Salmonella jalapeño outbreak is no longer 
    limited to Chipotle — it has expanded to Qdoba. Not covered in recent run history. 
    Two major fast-casual chains + fresh FDA action = high consumer urgency.

  recommended_angle: >
    Breaking news update with "should I be worried if I ate at these chains?" consumer angle. 
    Include symptom timeline, what to do, FDA investigation status.

  integrity_flags:
    - "⚠️ Breaking-recall exception: FDA primary outbreak investigation page is the required source — confirm URL and case count before publishing"
    - "⚠️ Do not imply all Chipotle/Qdoba locations affected — specify it is the jalapeño supply, not the restaurant chain broadly"

  outline:
    intro: "Outbreak expands — Qdoba now confirmed in addition to Chipotle. FDA investigation active."
    sections:
      - "What happened: timeline from Chipotle reports to Qdoba confirmation"
      - "Which locations are affected? What FDA/chains have said publicly"
      - "Salmonella symptoms and what to do if you ate at these restaurants recently"
      - "How jalapeños get contaminated — brief food safety context"
      - "FDA investigation: what's known and what's still unclear"
    conclusion: "When to seek medical care; link to FDA outbreak investigation page."

  key_data_points:
    - "Outbreak expanded to Qdoba as of FDA announcement reported 08/06"
    - "Salmonella symptoms: diarrhea, fever, cramps within 6 hours to 6 days of exposure"
    - "Most recover without treatment; high-risk groups (elderly, immunocompromised, young children) may need hospitalization"

  source_plan:
    - publisher: "ABC News — FDA confirmation"
      url: "https://abcnews.go.com/Health/salmonella-outbreak-linked-jalapenos-served-chipotle-expands-qdoba/story"
      tier: 2
      used_for: "Outbreak expansion to Qdoba, FDA statement"
    - publisher: "FDA — Outbreak Investigation"
      url: "https://www.fda.gov/food/outbreaks-foodborne-illness/"
      tier: 1
      used_for: "Official investigation status [verify specific outbreak page]"
    - publisher: "CDC — Salmonella"
      url: "https://www.cdc.gov/salmonella/"
      tier: 1
      used_for: "Symptom data, at-risk populations"

  seo:
    primary_keyword: "Salmonella Qdoba Chipotle jalapeños"
    supporting_keywords: ["jalapeño salmonella outbreak", "Chipotle salmonella", "salmonella symptoms", "FDA salmonella investigation 2026"]
    format: "Breaking news explainer"
    schema_markup: "NewsArticle"
    cluster: "food safety / FDA recalls"

  estimated_word_count: "700–900 words"

execution_notes: >
  Confirm Qdoba's public statement and FDA's official case count before publishing. 
  Do not describe either chain as broadly unsafe — the issue is the jalapeño supply source.
```

---

### BRIEF 4 — P2 / SHORT-TERM

**Primary Headline:** FDA Issues Class I Recall for 30,000+ Lbs of Cheese Over Listeria Risk — What's Affected

**Alternate Headlines:**
- Listeria in Cheese: FDA's Highest-Risk Recall Covers Multiple States — Here's What to Check
- Class I Cheese Recall: The Listeria Risk, Which Products Are Pulled, and Who's Most Vulnerable

```yaml
brief:
  topic: "Cheese Listeria recall — Class I, FDA highest risk level, 30,000+ lbs"
  primary_entity: "Listeria monocytogenes / cheese recall"
  signal_type: "recall"
  allowed_category: "FDA and CDC regulatory updates"
  priority_level: P2
  publish_timing: short_term
  trend_strength_score: 74
  opportunity_score: 73
  discover_score: 4
  urgency: today
  confidence: medium
  content_status: new
  source_count: 3
  why_now: >
    The Healthy/Reader's Digest reported 08/05 that FDA has assigned Class I (highest risk) 
    status to a recall of 30,000+ lbs of cheese. Columbus Dispatch corroborated 08/06. 
    Not in recent run history. Class I designation signals FDA's highest concern level — 
    editorial hook is the severity classification plus Listeria's serious risk profile.

  recommended_angle: >
    Consumer-action piece: what Class I means, which cheeses/brands affected, who faces 
    the most serious risk from Listeria (pregnant women, immunocompromised). 
    Listeria is more dangerous than most recall pathogens — this needs clear severity framing.

  integrity_flags:
    - "⚠️ Breaking-recall exception: FDA recall page is the authoritative source — verify product names, lot numbers, and brand before publishing"
    - "⚠️ Do not overstate: Class I = highest concern category, but does not mean confirmed illness yet — note investigation status"
    - "⚠️ Listeria is especially dangerous in pregnancy — include this explicitly with appropriate medical guidance to consult OB"

  outline:
    intro: "Class I recall — FDA's highest risk level — issued for 30,000+ lbs of cheese due to Listeria contamination risk."
    sections:
      - "What is a Class I recall? Why this designation matters"
      - "Which cheeses and brands are affected — product names, lot numbers, where sold"
      - "Listeria: why it's more dangerous than Salmonella or E. coli for certain groups"
      - "Who is at highest risk: pregnant women, elderly, immunocompromised, newborns"
      - "What to do: don't eat the product, where to check, whether to see a doctor if you already ate it"
    conclusion: "Link to FDA recall database; specific hotline if available."

  key_data_points:
    - "30,000+ lbs subject to Class I recall"
    - "Class I = FDA determination that use will cause serious adverse health consequences or death"
    - "Listeria kills ~260 people/year in the US; pregnant women are ~10x more likely to get sick"
    - "Listeriosis symptoms can appear 1–4 weeks after exposure — recall window matters"

  source_plan:
    - publisher: "The Healthy / Reader's Digest"
      url: "https://www.thehealthy.com/food/fda-assigns-highest-risk-level-cheese-recall/"
      tier: 2
      used_for: "Breaking news signal, Class I designation, pound volume"
    - publisher: "FDA Recalls Database"
      url: "https://www.accessdata.fda.gov/scripts/ires/"
      tier: 1
      used_for: "Official product names, lot codes, distribution details"
    - publisher: "CDC — Listeria"
      url: "https://www.cdc.gov/listeria/"
      tier: 1
      used_for: "Listeria pathogen data, risk groups, case statistics"

  seo:
    primary_keyword: "FDA cheese recall Listeria 2026"
    supporting_keywords: ["cheese Listeria recall", "Class I recall", "Listeria symptoms", "which cheese recalled", "Listeria pregnancy risk"]
    format: "Consumer-action recall article with FAQ"
    schema_markup: "NewsArticle + FAQPage"
    cluster: "food safety / FDA recalls"

  estimated_word_count: "900–1,100 words"
```

---

### BRIEF 5 — P2 / SHORT-TERM

**Primary Headline:** A New AI Model Can Predict Your Health Risks While You Sleep — What a Nature Study Found

**Alternate Headlines:**
- Scientists Built an AI That Reads Your Sleep to Predict Heart Disease, Diabetes, and Mortality Risk
- Your Sleep Data Might Soon Do More Than Track Hours — A Nature Foundation Model Explains How

```yaml
brief:
  topic: "AI foundation model for sleep-based health risk stratification — Nature study"
  primary_entity: "Sleep AI foundation model / Nature"
  signal_type: "study_or_research"
  allowed_category: "sleep science"
  priority_level: P2
  publish_timing: short_term
  trend_strength_score: 71
  opportunity_score: 76
  discover_score: 4
  urgency: today
  confidence: high
  content_status: new
  source_count: 3
  why_now: >
    Published in Nature 08/03/2026. Not in recent run history. Sleep science is a core 
    category with strong audience engagement. The combination of AI + sleep + clinical 
    outcome prediction is a timely and differentiated topic from the general "sleep deprivation 
    and immunity" meta-analysis covered 08/05 — this is about diagnostic potential, not 
    just sleep habits.

  recommended_angle: >
    Evaluative explainer: what the model actually does, what outcomes it can predict, 
    how far from clinical use it is, and what it means for the future of sleep monitoring 
    vs. current consumer wearables. Lead with genuine capability; temper with honest 
    caveats about development stage.

  integrity_flags:
    - "⚠️ Single study — Nature publication is high quality but this is one foundation model; broader validation needed before clinical translation"
    - "⚠️ Distinguish risk stratification from diagnosis — this model predicts risk, it does not diagnose disease"
    - "⚠️ Do not extrapolate to consumer sleep trackers (Fitbit, Oura) without confirming the model was validated on consumer device data"

  outline:
    intro: "Scientists have built an AI model trained on sleep data that can predict risk for cardiovascular disease, diabetes, and mortality — published in Nature."
    sections:
      - "What the foundation model does — how it was trained, what sleep signals it reads (EEG, breathing, heart rate)"
      - "What it can predict — specific clinical outcomes, accuracy benchmarks from the paper"
      - "How it was validated — dataset size, patient populations, study design"
      - "What this means for the future of sleep medicine and clinical risk tools"
      - "The gap: research model vs. clinical use — what needs to happen before this reaches patients"
      - "Wearables angle: does this change the value of consumer sleep trackers?"
    conclusion: "Frame as a promising but early-stage research development; encourage readers to discuss sleep health with their doctor using existing validated tools."

  key_data_points:
    - "Published in Nature, 08/03/2026 [verify DOI]"
    - "Foundation model trained on large-scale polysomnography data"
    - "Predicts risk for multiple conditions from sleep architecture patterns"
    - "Foundation model approach = generalizable across patient populations (key differentiator from prior sleep ML)"

  source_plan:
    - publisher: "Nature — original publication"
      url: "https://www.nature.com/articles/ [verify DOI — search 'sleep foundation model risk stratification clinical outcomes Nature 2026']"
      tier: 1
      used_for: "Study methodology, findings, accuracy benchmarks"
    - publisher: "CDC — Sleep and Chronic Disease"
      url: "https://www.cdc.gov/sleep/index.html"
      tier: 1
      used_for: "Background on sleep and health outcomes"
    - publisher: "National Sleep Foundation"
      url: "https://www.thensf.org/"
      tier: 2
      used_for: "General sleep health context"

  expert_sources:
    - type: "Sleep medicine specialist or computational biologist"
      name: "[Search Nature paper authors for named researcher — use their institutional affiliation for credibility attribution]"
      reason: "Primary researcher perspective on clinical translation timeline"

  seo:
    primary_keyword: "AI sleep health prediction study"
    supporting_keywords: ["sleep risk stratification AI", "sleep and heart disease", "AI health monitoring sleep", "Nature sleep study 2026", "sleep foundation model"]
    format: "Research explainer with FAQ"
    schema_markup: "Article + FAQPage"
    cluster: "sleep science / medical AI"

  estimated_word_count: "1,100–1,400 words"
```

---

### BRIEF 6 — P2 / SHORT-TERM

**Primary Headline:** A New Drug Is Targeting Weight Loss, Heart Health, and Blood Sugar Simultaneously — Here's What the Trial Data Shows

**Alternate Headlines:**
- Beyond Ozempic: A Triple-Action GLP-1 Drug Enters Phase 1 Trials — What It's Targeting and Why It Matters
- Neurocrine's Triple Agonist Drug Could Change Metabolic Treatment — What We Know From Phase 1 Initiation

```yaml
brief:
  topic: "Neurocrine Biosciences NBIP-1968 — GLP-1/GIP/Glucagon triple agonist Phase 1 initiation"
  primary_entity: "NBIP-1968 / Neurocrine Biosciences / triple agonist"
  signal_type: "clinical_trial"
  allowed_category: "medical research and clinical trials"
  priority_level: P2
  publish_timing: short_term
  trend_strength_score: 68
  opportunity_score: 74
  discover_score: 4
  urgency: today
  confidence: medium
  content_status: new
  source_count: 2
  why_now: >
    Neurocrine announced Phase 1 initiation of NBIP-1968 on 08/07/2026 — a triple receptor 
    agonist (GLP-1 + GIP + glucagon) that could outperform current GLP-1-only agents on 
    weight loss and metabolic outcomes. This is distinct from the GLP-1 cardiovascular 
    outcomes NEJM RCT covered 08/05 — that was outcomes data on existing drugs; this is 
    a next-generation candidate just entering human trials.

  recommended_angle: >
    "What comes after Ozempic?" explainer — place this in the GLP-1 drug evolution context 
    for a health-literate general audience. Be honest that Phase 1 = safety/dosing in small 
    groups; we are years from any approval. The angle is "here's the science behind the next 
    generation of metabolic drugs" not "new weight loss cure."

  integrity_flags:
    - "⚠️ Phase 1 trial only — this is a first-in-human safety study, not efficacy data. Do not present as a treatment breakthrough."
    - "⚠️ Primary source is manufacturer press release (PR Newswire / Neurocrine) — independent scientific commentary not yet available; note this limitation clearly"
    - "⚠️ Do not compare efficacy to Ozempic/Wegovy — no head-to-head data exists at this stage"
    - "⚠️ Confidence capped at Medium — Phase 1 initiation, single source (manufacturer announcement)"

  outline:
    intro: "Neurocrine has begun first-in-human trials of a drug designed to hit three metabolic targets simultaneously — GLP-1, GIP, and glucagon receptors."
    sections:
      - "What triple agonism means — how targeting all three receptors differs from current GLP-1 drugs"
      - "The science: why glucagon receptor adds something semaglutide doesn't"
      - "What Phase 1 actually tests — safety, dosing, not 'does it work for weight loss'"
      - "Where this fits in the GLP-1 drug landscape — tirzepatide, retatrutide, and now NBIP-1968"
      - "Timeline: Phase 1 to potential approval — realistic expectations (5–10 years)"
      - "What it would mean for patients if it succeeds"
    conclusion: "Calibrate reader expectations: exciting early science, but no timeline for clinical availability."

  key_data_points:
    - "NBIP-1968 targets GLP-1, GIP, and glucagon receptors simultaneously"
    - "Phase 1 ClinicalTrials.gov registration [verify NCT number from Neurocrine announcement]"
    - "Tirzepatide (Mounjaro/Zepbound) is a dual GLP-1/GIP agonist — triple adds glucagon"
    - "Glucagon receptor agonism may enhance liver fat reduction beyond dual agonists"

  source_plan:
    - publisher: "PR Newswire — Neurocrine Biosciences press release"
      url: "https://www.prnewswire.com/ [verify Neurocrine NBIP-1968 Phase 1 announcement]"
      tier: 2
      used_for: "Phase 1 initiation announcement, drug mechanism"
    - publisher: "ClinicalTrials.gov"
      url: "https://clinicaltrials.gov/ [search NBIP-1968 or Neurocrine triple agonist]"
      tier: 1
      used_for: "Official trial registration — verify before citing"
    - publisher: "FDA — GLP-1 background"
      url: "https://www.fda.gov/drugs/postmarket-drug-safety-information-patients-and-providers/medications-approved-treat-obesity"
      tier: 1
      used_for: "Approved GLP-1 context"

  expert_sources:
    - type: "Endocrinologist or metabolic disease researcher"
      name: "[Search prior coverage of Neurocrine drug pipeline for named researcher commentary]"
      reason: "Independent scientific perspective on triple agonism potential"

  seo:
    primary_keyword: "GLP-1 GIP glucagon triple agonist trial"
    supporting_keywords: ["NBIP-1968 Neurocrine", "next generation weight loss drug", "beyond Ozempic drug trial", "triple agonist GLP-1 2026", "metabolic drug Phase 1"]
    format: "Research explainer / drug development piece"
    schema_markup: "Article"
    cluster: "GLP-1 / metabolic health / drug development"

  estimated_word_count: "1,000–1,300 words"
```

---

### BRIEF 7 — P3 / SCHEDULED

**Primary Headline:** Young People Are Turning to AI for Mental Health Help at Record Rates — What That Means and What to Watch Out For

```yaml
brief:
  topic: "AI use surging for mental health among young people — Harvard Gazette / research signal"
  primary_entity: "AI mental health tools / youth"
  signal_type: "study_or_research"
  allowed_category: "mental health and psychology"
  priority_level: P3
  publish_timing: scheduled
  trend_strength_score: 63
  opportunity_score: 70
  discover_score: 3
  urgency: this_week
  confidence: medium
  content_status: new
  source_count: 3
  why_now: >
    Harvard Gazette (08/03) published new research on surging AI use for mental health among 
    young people. Distinct from the 08/06 Aflac survey (which covered AI as first healthcare 
    consultation broadly); this focuses on mental health specifically and is from an academic 
    source vs. an insurance industry survey. Rising Google Trends signal for "brightline 
    mental health" + mental health AI signals support audience relevance.

  recommended_angle: >
    Evaluative: what the research actually shows, why young people are turning to AI, 
    what AI can and cannot do for mental health, and what clinicians say about appropriate use. 
    Not a panic piece, not uncritical hype.

  integrity_flags:
    - "⚠️ Distinguish correlation (young people using AI more) from causation — does this help or is it substituting for professional care?"
    - "⚠️ AI mental health tools vary enormously in quality; avoid generalizing 'AI' as monolithic"
    - "⚠️ Confirm study design from Harvard Gazette piece — survey vs. clinical study distinction matters for claim strength"

  key_data_points:
    - "Harvard Gazette piece: AI use for mental health surging among young people (08/03/2026)"
    - "Context: therapist shortage, cost barriers, stigma reductions all driving this trend"
    - "Woebot, Wysa, ChatGPT for mental health — different use cases with different evidence bases"

  source_plan:
    - publisher: "Harvard Gazette"
      url: "https://news.harvard.edu/gazette/"
      tier: 2
      used_for: "Primary signal — AI mental health youth study"
    - publisher: "APA — AI and mental health guidance"
      url: "https://www.apa.org/topics/artificial-intelligence"
      tier: 1
      used_for: "Professional clinical perspective on AI in therapy"
    - publisher: "STAT News"
      url: "https://www.statnews.com/"
      tier: 1
      used_for: "Any prior coverage of AI mental health tools evidence base"

  seo:
    primary_keyword: "AI mental health young people"
    supporting_keywords: ["AI therapy apps", "ChatGPT mental health", "AI vs therapist", "mental health AI tools 2026"]
    format: "Evaluative explainer"
    schema_markup: "Article"
    cluster: "mental health / digital health"
  estimated_word_count: "1,000–1,200 words"
```

---

### BRIEF 8 — P3 / SCHEDULED

**Primary Headline:** Teen Breakfasts and Long-Term Diet Quality: What the Rising Search Interest Reveals About Real Evidence

```yaml
brief:
  topic: "Teen diet breakfast benefits — rising search interest and research base"
  primary_entity: "Teen breakfast habits / adolescent nutrition"
  signal_type: "rising_search_interest"
  allowed_category: "nutrition and diet science"
  priority_level: P3
  publish_timing: scheduled
  trend_strength_score: 58
  opportunity_score: 65
  discover_score: 3
  urgency: this_week
  confidence: medium
  content_status: new
  source_count: 2
  why_now: >
    Google Trends shows "teen diet breakfast benefits research" as a rising related query 
    on the "diet" keyword cluster (7-day window). Aligns with back-to-school timing 
    (August) — parents and teens evaluating breakfast habits before school year. 
    Strong evergreen potential with timely seasonal hook.

  recommended_angle: >
    Research-grounded practical explainer: what the actual science says about teen breakfast 
    and diet quality outcomes (academic performance, energy, weight, metabolic health), 
    what types of breakfast matter, and what the research limitations are.

  integrity_flags:
    - "⚠️ Many teen breakfast studies are observational — association with better diet quality does not prove breakfast causes outcomes"
    - "⚠️ Distinguish breakfast skipping by choice from food insecurity context"

  key_data_points:
    - "Back-to-school timing amplifies audience relevance through late August"
    - "Existing research base: Nutrients journal, Journal of the Academy of Nutrition and Dietetics, NHANES data on teen dietary patterns"
    - "USDA school breakfast program data as institutional source"

  source_plan:
    - publisher: "USDA — School Breakfast Program"
      url: "https://www.fns.usda.gov/sbp/school-breakfast-program"
      tier: 1
      used_for: "Institutional context on teen breakfast policy and nutritional standards"
    - publisher: "Academy of Nutrition and Dietetics"
      url: "https://www.eatright.org/"
      tier: 1
      used_for: "Registered dietitian guidance on adolescent nutrition"
    - publisher: "PubMed — teen breakfast diet quality"
      url: "https://pubmed.ncbi.nlm.nih.gov/?term=teen+breakfast+diet+quality"
      tier: 1
      used_for: "Primary literature search for study citations"

  seo:
    primary_keyword: "teen breakfast diet quality research"
    supporting_keywords: ["does breakfast help teens", "adolescent nutrition breakfast", "teen diet tips back to school", "breakfast benefits teenagers"]
    format: "Research explainer with practical tips"
    schema_markup: "Article + FAQPage"
    cluster: "nutrition / adolescent health"
  estimated_word_count: "900–1,100 words"
```

---

### BRIEF 9 — P3 / SCHEDULED

**Primary Headline:** The 11 Biggest Wellness Trends of 2026 — Which Ones Are Backed by Science (and Which Aren't)

```yaml
brief:
  topic: "2026 wellness trends — evidence evaluation of major trends including 'boy kibble,' parasite cleanses, and AI wellness"
  primary_entity: "2026 wellness trends"
  signal_type: "cultural_moment"
  allowed_category: "nutrition and diet science"
  priority_level: P3
  publish_timing: scheduled
  trend_strength_score: 55
  opportunity_score: 62
  discover_score: 3
  urgency: this_week
  confidence: medium
  content_status: new
  source_count: 2
  why_now: >
    The Guardian published an editorial roundup of "the 11 biggest wellness trends of 2026" 
    on 08/07. The list includes trends ranging from credible to dubious ("parasite cleanses," 
    "AI wellness," "boy kibble"). This creates an immediate opportunity for a differentiated, 
    evidence-evaluation piece — not a trend recap, but a fact-check-style assessment of 
    which 2026 wellness trends have research behind them and which don't.

  recommended_angle: >
    Evidence audit: take the major 2026 wellness trends circulating in media and assess 
    each against published research. Clear "evidence: strong / weak / none" ratings per 
    trend. Practical, skeptical, not preachy.

  integrity_flags:
    - "⚠️ Distinguish evidence-based wellness from wellness marketing — avoid lending credibility to claims without research support"
    - "⚠️ 'Boy kibble' and 'parasite cleanses' — if covering, debunk clearly with sourced science; do not describe these neutrally as 'trends worth exploring'"
    - "⚠️ AI wellness tools — highly variable; avoid either blanket endorsement or blanket rejection"

  key_data_points:
    - "The Guardian piece published 08/07/2026 — 11 biggest wellness trends identified"
    - "Parasite cleanses: no credible evidence for routine use in non-endemic populations; potential harms from unregulated supplements"
    - "AI wellness: evidence emerging for specific applications (CBT apps, sleep tracking) but highly heterogeneous"

  source_plan:
    - publisher: "The Guardian"
      url: "https://www.theguardian.com/lifeandstyle/2026/aug/07/wellness-trends-2026"
      tier: 2
      used_for: "Trend identification anchor / news hook"
    - publisher: "NIH / PubMed"
      url: "https://pubmed.ncbi.nlm.nih.gov/"
      tier: 1
      used_for: "Research evidence per trend cited"
    - publisher: "CDC — Health Topics"
      url: "https://www.cdc.gov/az/a.html"
      tier: 1
      used_for: "Institutional guidance on any trends touching clinical health claims"

  seo:
    primary_keyword: "2026 wellness trends evidence"
    supporting_keywords: ["wellness trends 2026", "parasite cleanse evidence", "AI wellness tools", "which wellness trends are real", "wellness science vs hype"]
    format: "Evidence-rating roundup / fact-check style"
    schema_markup: "Article"
    cluster: "wellness / nutrition / consumer health"
  estimated_word_count: "1,200–1,500 words"
```

---

## REJECTED TOPICS LOG

| Topic | Rejection Reason |
|---|---|
| FDA blood thinner recall | `existing` — covered 08/07; no new development identified |
| Eye drops recall (CVS/Kroger 3M+ bottles) | `existing` — covered 08/07; no new development |
| Cyclospora outbreak — CDC links to iceberg lettuce (base story) | `existing` — 08/07; retained only the new 28-state update above |
| Middle age habits and dementia-free years | `existing` — covered 08/07; no new development |
| Dormant cancer cells disarm immunotherapy | `existing` — covered 08/07 |
| Diet soda and cognitive decline | `existing` — covered 08/07; recurring flag; no new study |
| Low-protein diet and lifespan | `existing` — covered 08/07; recurring flag |
| Peach recall — FDA update on 10M lbs | `existing` — covered 08/07 |
| Birth order and disease risk (Nature) | `existing` — covered 08/06 |
| Ibogaine neurological recovery (Barrow) | `existing` — covered 08/06 |
| AI as first healthcare consultation (Aflac survey) | `existing` — covered 08/06 |
| GLP-1 cardiovascular outcomes NEJM RCT | `existing` — covered 08/05; no update |
| RSV vaccine adult 60+ CDC update | `existing` — covered 08/05 |
| Sleep deprivation and immune function meta-analysis | `existing` — covered 08/05 |
| PFAS drinking water EPA enforcement | `existing` — covered 08/05 |
| Childhood obesity AAP guidelines | `existing` — covered 08/05 |
| H5N1 bird flu US human case | `existing` — covered 08/05; no new case |
| Menopause cardiovascular risk AHA | `existing` — covered 08/05 |
| UPF and long-term mortality BMJ | `existing` — covered 08/05 |
| Psilocybin PTSD veterans trial | `existing` — covered 08/01 |
| Dronabinol (THC) for PTSD nightmares | `existing` — covered 08/06 |
| FDA egg recall (19M+ cartons) | `existing` — covered 08/01 |
| FDA levothyroxine recall | `existing` — covered 08/01 |
| Frozen blueberry E. coli investigation | `existing` — covered 08/01 |
| Rohto eye drops recall | `existing` — covered 08/01 |
| GLP-1 individual metabolic profiling (Penn Medicine) | `existing` — covered 08/01 |
| AI in oncology clinical trials (Nature) | `rejected` — pharma/business-adjacent; no direct patient health angle strong enough for general audience |
| Crumbl dirty soda nutrition facts | `rejected` — rising Trends query but pop culture only; no substantive health content opportunity |
| HHS foreign aid maternal/child health review | `rejected` — pure policy/political framing; no new health science data |
| Medi-Cal rollback (CalMatters) | `rejected` — state policy/political; excluded category |
| Hospital workforce news | `rejected` — institutional/local; too narrow |
| Medical Aid in Dying (NY state) | `rejected` — policy/regulatory at state level; political sensitivity without new clinical data |
| General wellness roundup topics (wellness center openings, events, local programs) | `rejected` — off-category (local/institutional); low national audience relevance |
| AI in psychiatric training (WVU study) | `rejected` — medical education focus; low direct consumer health relevance |
| NBA Achilles injury playing time study | `rejected` — sports medicine but sports-outcome-focused; low general health audience relevance |

---

## INTEGRITY FLAGS — CONSOLIDATED

| # | Candidate | Flag |
|---|---|---|
| 1 | Vibrio vulnificus (Brief 1) | ⚠️ Confirm Louisiana DHHS case count before publishing; do not conflate with Group A Strep necrotizing fasciitis |
| 2 | Cyclospora update (Brief 2) | ⚠️ Breaking-recall exception — FDA.gov primary notice must be verified before publishing; confirm 28-state list via CDC/FDA directly |
| 3 | Salmonella Chipotle/Qdoba (Brief 3) | ⚠️ Breaking-recall exception — FDA outbreak investigation page required; do not imply all chain locations affected |
| 4 | Cheese/Listeria recall (Brief 4) | ⚠️ Breaking-recall exception — verify product names and lot codes from FDA recall database; note Class I = highest-concern category, not confirmed illness |
| 4b | Cheese/Listeria recall (Brief 4) | ⚠️ Listeria in pregnancy requires explicit, medically accurate guidance to consult OB/GYN — do not minimize |
| 5 | Sleep AI foundation model (Brief 5) | ⚠️ Single study; risk stratification ≠ diagnosis; do not extrapolate to consumer wearables without confirming study validation data |
| 6 | Neurocrine triple agonist (Brief 6) | ⚠️ Phase 1 = first-in-human safety, not efficacy; primary source is manufacturer press release; no independent scientific commentary yet available |
| 7 | AI mental health youth (Brief 7) | ⚠️ Observational signal; distinguish AI use from AI therapeutic efficacy; not all AI tools are equivalent |
| 8 | Teen breakfast research (Brief 8) | ⚠️ Most studies observational; association ≠ causation; distinguish breakfast skipping from food insecurity |
| 9 | Wellness trends 2026 (Brief 9) | ⚠️ Debunk clearly (parasite cleanses, boy kibble); do not grant credibility to wellness claims without supporting research |

---

## RUN NOTES

**Signals reviewed:** 144 Google News + Google Trends rising queries
**Retained:** 9 candidates
**Rejected/Existing:** 135 (primarily prior 7-day coverage)
**Skill 02b triggered:** 5 candidates (3 recalls via breaking-recall exception; 1 clinical trial; 1 medical study)
**No Skill 02b rejections or Monitor exits this run.**

**Google Trends interpretation notes:**
- `dementia risk factors` appearing as real-time trending is consistent with persistent audience interest in this topic area, but without new institutional source or study, it maps to `existing` coverage from multiple prior runs. Monitored, not retained.
- `louisiana vibrio vulnificus outbreak` is the single highest-signal breakout term and anchors P1 Brief 1.
- `diet` cluster rising queries (`teen diet breakfast benefits research`, `low protein diet lifespan research`, `diet soda cognitive decline`) were evaluated individually: the last two are `existing`; teen breakfast is a new candidate.
- `gut health` rising related queries in this run are entirely off-topic (tech/lifestyle/travel cross-contamination in the Trends data) — no actionable health signal extracted.
- `food safety` Trends data similarly shows off-topic cross-contamination; food safety signals came from Google News Radar instead.

**Recurring theme flag:** Diet soda cognitive decline and low-protein diet lifespan have now appeared in 3 consecutive runs (08/05, 08/07, 08/08). No new study or development in today's signal data. Both remain `existing` — editorial should consider whether a consolidated deep-dive piece on "diet and cognitive health" would be a more durable use of this recurring search interest than reactive daily pieces.

**Self-check note:** `site_url` not configured. Content status `new` for all 9 retained candidates is confirmed against recent run history and competitor fallback — not against a live site content database. Recommend providing article slugs or configuring `site_url` for more precise duplicate detection.

**Run archived to:** `data/run_history.yaml` — 2026-08-08 entry added. No overflow to `data/deferred_topics.yaml` (9 retained candidates within the 25-candidate limit).