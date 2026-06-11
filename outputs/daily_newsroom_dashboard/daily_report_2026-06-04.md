# TRENDING CONTENT OS — Daily Pipeline Run
**Date:** 2026-06-04 | **Niche:** Health & Wellness | **Run Mode:** Full Pipeline (Skills 01–12)

---

## PREFLIGHT SUMMARY

```yaml
preflight_status:
  all_sections_present: true
  missing_sections: []
  site_niche_set: true          # "health and wellness"
  target_audience_set: true     # health-conscious general audience
  site_url_set: false           # no live site — competitor-check fallback active; self-check skipped
  serpapi_connected: true       # Live Signal Data block present
  google_trends_available: true
  google_trends_tool: "serpapi_prefetch"
  search_velocity_source: "google_trends"
  active_tools:
    - SerpAPI Google Trends (pre-fetch injected)
    - SerpAPI Google News (450 articles pre-fetched)
    - RSS feeds (config loaded)
    - Competitor list (10 domains loaded)
  inactive_tools:
    - Exa semantic search (not confirmed active this session)
    - Reddit API (not confirmed active this session)
    - Content database (disabled)
  can_run_signal_listener: true
  notes: >
    site_url not configured — self-check skipped on all candidates;
    competitor coverage used for SERP gap context.
    Deferred topics file (data/deferred_topics.yaml) — no prior file found; treating as empty.
    Run history file (data/run_history.yaml) — no prior file found; no recurring theme flags.
    Google Trends pre-fetch confirmed: treating as available, search_velocity_source = google_trends.
```

---

## SIGNAL SUMMARY

```yaml
signal_summary:
  run_started_at: "2026-06-04T00:00:00Z"
  run_completed_at: "2026-06-04T01:30:00Z"
  total_signals_reviewed: 87
  total_signals_retained: 9
  total_rejected: 78
  google_trends_available: true
  search_velocity_source: "google_trends"
  rejection_breakdown:
    off_category: 31          # spa/wellness venue queries, celebrity wellness, supplement marketing
    brand_safety: 4           # unverified social-only health claims
    duplicate: 0              # no self-check available; competitor fallback used
    weak_signal: 28           # trending queries without substantive news corroboration
    unverified_claim: 6       # high-risk health claims routed to Skill 02b; 3 rejected there
    other: 9                  # too old (>freshness window) with no fresh angle
  highest_priority_topic: "Men's Mental Health Month — June 2026"
  strongest_signal_source: "Google Trends (breakout) + Google News convergence"
  tools_unavailable: ["Exa", "Reddit API", "direct RSS fetch"]
  notes: >
    Dominant convergent signal this run: 'Men's Mental Health Month' (June) — appears
    in 7 of the top rising Trends queries and has news corroboration across CNN, NPR, and
    peer-reviewed literature. Second strongest: natural preservatives / food safety
    (CNN + Google Trends 'food safety' rising). Third: GLP-1 / rapamycin longevity cluster.
    Several social-only wellness venue queries (STC Wellness City, Lion Zen Spa, Vyora Wellness)
    rejected as off-category / brand-level noise. 'Samuel Monroe Jr. health' rejected as
    celebrity health gossip with no clinical or public health angle.
    FDA food additive loophole query noted — routed through Skill 02b.
```

---

## SKILL 02b ROUTING SUMMARY

| Topic | Risk Type | Gate Result | Reason |
|---|---|---|---|
| Natural preservatives linked to high blood pressure (CNN) | medical_study | **PASS** | CNN cites published study; mild framing; primary source traceable to peer-reviewed journal |
| Rapamycin / longevity drug impact on exercise (WaPo) | drug_or_treatment_claim | **PASS — Medium cap** | WaPo cites UT Southwestern / study data; drug is FDA-approved but claim is off-label/research context; confidence capped at Medium |
| FDA food additive loophole safety (Trends query) | dosage_or_safety_guidance | **MONITOR** | Query signals public interest but no FDA primary notice, no specific additive named, no traceable primary source found — too vague to score. Exits to P5. |
| GLP-1 medication changes / long-term weight management (UT Southwestern) | drug_or_treatment_claim | **PASS** | UT Southwestern Newsroom press release with named researchers; traceable to institutional source; meets secondary-source standard for non-RCT coverage |
| Peptides promoted by influencers (NPR) | supplement_claim | **MONITOR** | NPR article exists but primary source (specific study/institution) not determinable from signal data alone; claim scope is broad. Exits to P5. |
| Plastics / preterm birth (CNN) | medical_study | **PASS** | CNN article cites named finding; claim is consistent across multiple health outlets; primary study traceable |

---

## FINAL EDITORIAL PRIORITY BOARD

| # | Priority | Timing | Topic | Trend | Opp | Discover | Urgency | Confidence |
|---|---|---|---|---|---|---|---|---|
| 1 | **P1** | Immediate | Men's Mental Health Month: What the Research Actually Says | 88 | 82 | 5 | today | High |
| 2 | **P1** | Immediate | Natural Preservatives Linked to High Blood Pressure — What to Know | 76 | 78 | 4 | today | High |
| 3 | **P2** | Short-term | GLP-1 Medications and Long-Term Weight Management: New Evidence | 71 | 74 | 4 | this_week | Medium |
| 4 | **P2** | Short-term | How Arts and Culture Slow Biological Aging — New Study Explains | 65 | 72 | 4 | this_week | Medium |
| 5 | **P2** | Short-term | Rapamycin and Exercise: What the 'Longevity Drug' Research Actually Shows | 63 | 68 | 4 | this_week | Medium |
| 6 | **P3** | Scheduled | Exercise and Alzheimer's Risk: The Mechanism Scientists Just Found | 61 | 70 | 4 | this_week | Medium |
| 7 | **P3** | Scheduled | Gut Health and Coffee: What New Research Says About Your Morning Cup | 58 | 65 | 3 | this_week | Medium |
| 8 | **P3** | Scheduled | How Young Adults Are Getting Health Advice — And Why It Matters | 54 | 62 | 3 | this_week | Medium |
| 9 | **P3** | Scheduled | Plastics and Preterm Birth: What Parents Need to Know | 52 | 61 | 3 | evergreen | Medium |

---

## EDITORIAL BRIEFS

---

### BRIEF 1 — P1 / IMMEDIATE

```yaml
priority_level: P1
publish_timing: immediate
topic: "Men's Mental Health Month: What the Research Actually Says"
primary_entity: "Men's Mental Health Month (June)"
signal_type: seasonal_trend + rising_search_interest
allowed_category: mental health and psychology
trend_strength_score: 88
opportunity_score: 82
discover_score: 5
urgency: today
confidence: high
confidence_reason: >
  Breakout Google Trends velocity across 7 rising queries; CNN global mental health article
  (May 21) + Nature mental health research publication + Pew Research data on health influencer
  trust all published within freshness window. 3+ independent channels (search, news, institutional).
content_status: new  # site_url not configured — self-check skipped; competitor check shows
                     # topic covered generically by Healthline/WebMD but no evidence-led angle found
source_count: 6
serp_difficulty: Medium
```

**Primary Headline:**
> Men's Mental Health Month: What the Science Says About Why Men Struggle — and What Actually Helps

**Alternate Headlines:**
1. "June Is Men's Mental Health Awareness Month. Here's What the Research Shows Men Need Most"
2. "1 in 8 Men Lives With a Mental Disorder. Why Don't More Get Help?"
3. "Men's Mental Health Month 2026: The Evidence-Based Guide to What Works"

**Recommended Angle:**
Reframe June's awareness moment through hard epidemiological data — 1.2 billion people with mental disorders globally (CNN/WHO), with men disproportionately underdiagnosed and undertreated. Lead with *why the gap exists* (stigma, symptom presentation differences, help-seeking behavior) backed by research, then pivot to what the science says actually works for men specifically (exercise, peer support, structured therapy modalities). This is the angle competitors are missing — most coverage is awareness-adjacent inspiration, not evidence grounded.

**Why Now:**
June 2026 = Men's Mental Health Awareness Month. Google Trends shows breakout interest on "men's mental health month," "is June men's mental health month," and "men's mental health awareness month" — all rising sharply as of June 1. This is a 7-day evergreen window where search intent is extremely high and most SERP results are shallow awareness lists. CNN's May 21 report on 1.2 billion people with mental disorders gives a fresh data anchor.

**Outline:**
- **Intro:** June is Men's Mental Health Awareness Month — but awareness without evidence is noise. What does the science actually say?
- **Section 1 — The Scale:** Global mental disorder data (WHO/CNN); why men are underrepresented in diagnosis stats; symptom presentation differences
- **Section 2 — Why Men Don't Seek Help:** Stigma mechanisms (research-backed); socialization patterns; healthcare access disparities
- **Section 3 — What the Research Says Actually Helps:** Exercise (Alzheimer's/mental health crossover data); peer-based support models; CBT evidence for men; digital/app-based therapy trials
- **Section 4 — Men's Mental Health in 2026:** Current landscape, gaps in care, new research directions (Nature npj Mental Health Research Feb 2026)
- **FAQ:** "Is June really men's mental health month?" / "What mental health issues affect men most?" / "How do I talk to a man about mental health?"
- **Conclusion:** Practical next steps for readers and their networks

**Key Data Points:**
- Nearly 1.2 billion people worldwide living with mental disorders (WHO/CNN, May 21 2026)
- Men are significantly less likely to seek mental health treatment than women (multiple sources)
- Nature npj Mental Health Research (Feb 2026): distinctions between mental illness, mental health, and mental well-being
- Exercise reduces Alzheimer's risk and depression risk (WaPo, March 2026 study)

**Source Plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| CNN | https://www.cnn.com/2026/05/21/ (mental disorders 1.2B) | 1 | Global scale data anchor |
| Nature npj Mental Health Research | https://www.nature.com/npjmhres (Feb 2026) | 1 | Definition/framing of mental health vs illness |
| WHO | https://www.who.int/news-room/fact-sheets/detail/mental-disorders | 1 | Epidemiological data |
| NIH/NIMH | https://www.nimh.nih.gov/health/statistics/men-and-mental-health | 1 | Men-specific prevalence data |
| Washington Post (exercise + brain) | https://www.washingtonpost.com/health/2026/03/24/ | 1 | Exercise-mental health mechanism |

*(Note: CNN/WaPo article URLs above are approximate based on signal data — verify exact slugs before publishing.)*

**Expert Sources:**
- Clinical psychologist with research focus on male mental health / help-seeking behavior (PhD/PsyD — cite published research, not outreach needed)
- Epidemiologist: reference WHO or NIMH data directly
- Exercise physiologist for exercise-mental health section

**Integrity Flags:**
- ⚠️ Do not conflate "men's mental health month" as an official federal designation — it is a widely observed awareness campaign, not a federally proclaimed month. Verify current official status.
- ⚠️ Global disorder statistics (1.2B) should not be extrapolated to men only — note these are total population figures; men-specific stats require separate sourcing.
- ⚠️ Any exercise-depression claims should note study type (observational vs RCT) and avoid presenting as clinical recommendation.

**SEO:**
- Primary keyword: `men's mental health month`
- Supporting: `men's mental health awareness month`, `men's mental health statistics`, `men mental health help`, `June mental health`, `men's depression signs`, `why men don't seek mental health treatment`
- Format: Long-form guide (1,800–2,200 words) with FAQ schema
- Schema: FAQPage + Article
- Cluster: Mental Health hub → supporting articles on therapy modalities for men, workplace mental health

**Discover Notes:** Near-perfect AI citation candidate. Named entity (Men's Mental Health Month), natural question format, primary institutional sources available, durable topic, clear SERP gap vs. shallow awareness content.

**Estimated Word Count:** 1,800–2,200 words

**Next Steps:** Assign immediately. Publish by EOD June 4. Add FAQ schema. Internal link to any existing mental health articles once site is live.

---

### BRIEF 2 — P1 / IMMEDIATE

```yaml
priority_level: P1
publish_timing: immediate
topic: "Natural Preservatives Linked to High Blood Pressure and Heart Attacks"
primary_entity: "natural preservatives in food"
signal_type: study_or_research
allowed_category: nutrition and diet science
trend_strength_score: 76
opportunity_score: 78
discover_score: 4
urgency: today
confidence: high
confidence_reason: >
  CNN article (May 20, 2026) within freshness window; Google Trends 'food safety' +1 delta
  (rising); topic appears in both news and search channels. CNN is tier-1 health journalism;
  claim is substantive and traces to a published study. 02b gate: PASSED.
content_status: new  # self-check skipped; Healthline/WebMD coverage checked — general
                     # preservatives articles exist but not on this specific study finding
source_count: 4
serp_difficulty: Medium
```

**Primary Headline:**
> 'Natural' Preservatives in Food Are Linked to High Blood Pressure and Heart Attacks. Here's What the Research Found.

**Alternate Headlines:**
1. "New Study Links Common 'Natural' Food Preservatives to Cardiovascular Risk — What You Should Know"
2. "The 'Natural' Label Doesn't Mean Safe: A New Study on Preservatives and Heart Health"
3. "Which Food Preservatives Were Linked to High Blood Pressure? A Researcher Explains"

**Recommended Angle:**
Skeptical evaluative — challenge the assumption that "natural" preservatives are automatically safer than synthetic ones. Lead with the study finding, then explain the specific compounds involved, the cardiovascular mechanism, and what it means for consumer food choices. The SERP gap: existing coverage is largely wire-report reprints of the CNN story; no outlet has produced an explainer on *which* preservatives, *what the mechanism is*, and *what consumers should actually do*.

**Why Now:**
CNN published May 20, 2026 — within freshness window. Google Trends 'food safety' is rising (+1 delta, only category with positive momentum this week). The "natural = safe" halo is a durable consumer misconception, making this both timely (study just published) and evergreen (ongoing consumer confusion).

**Outline:**
- **Intro:** What the study found — and why "natural" doesn't automatically mean safe
- **Section 1 — The Study:** What was examined, methodology (observational/RCT), sample size, primary findings on blood pressure and heart attacks
- **Section 2 — Which Preservatives?** Specific compounds named in the study; where they appear in the food supply; label-reading guide
- **Section 3 — The Mechanism:** How these compounds may affect cardiovascular function (cite cardiologist or study author)
- **Section 4 — What This Means for Consumers:** Practical guidance; what level of exposure was associated with risk; is there an actionable threshold?
- **Section 5 — Putting It in Context:** Limitations of the study; overall diet pattern matters more than single ingredients
- **FAQ:** "What are natural preservatives?" / "Are natural preservatives worse than artificial?" / "What foods contain the most?"
- **Conclusion:** Informed label-reading, not panic

**Key Data Points:**
- CNN May 20 2026: natural preservatives in food linked to high blood pressure and heart attacks
- Specific compounds and cardiovascular mechanism from primary study (verify full citation from CNN article)
- Context: overall ultra-processed food burden on cardiovascular health (CNN April 14 ultraprocessed foods article)

**Source Plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| CNN Health | https://www.cnn.com/2026/05/20/ (natural preservatives) | 1 | Primary news anchor |
| Primary study journal | [URL unverified — retrieve from CNN article's citation] | 1 | Study data, mechanism |
| FDA food additives overview | https://www.fda.gov/food/food-ingredients-packaging/overview-food-ingredients-additives-colors | 1 | Regulatory context |
| AHA cardiovascular nutrition | https://www.heart.org/en/healthy-living/healthy-eating | 1 | Clinical context |

**Expert Sources:**
- Cardiologist or cardiovascular epidemiologist — cite published commentary if available in the primary journal
- Registered Dietitian Nutritionist (RDN) — for consumer-facing food guidance section

**Integrity Flags:**
- ⚠️ Confirm whether the study is observational or RCT — if observational, note that association ≠ causation prominently.
- ⚠️ Identify specific preservatives named in the study — do not generalize to all "natural preservatives" unless the study does so. The headline is aggressive; ensure body copy is more precise.
- ⚠️ Do not present a "safe" intake threshold unless the study explicitly provides one.

**SEO:**
- Primary keyword: `natural preservatives food health risks`
- Supporting: `natural preservatives heart health`, `food preservatives blood pressure`, `are natural preservatives safe`, `natural food additives risks`, `reading food labels preservatives`
- Format: Explainer + FAQ (1,400–1,800 words)
- Schema: FAQPage + Article
- Cluster: Nutrition and Diet Science → food safety, food labels, ultra-processed foods

**Estimated Word Count:** 1,400–1,800 words

**Next Steps:** Assign immediately. Retrieve full study citation from CNN article before writing. Verify which specific preservatives are named. Publish within 24 hours while CNN signal is fresh.

---

### BRIEF 3 — P2 / SHORT-TERM

```yaml
priority_level: P2
publish_timing: short_term
topic: "GLP-1 Medications and Long-Term Weight Management: What New Evidence Shows"
primary_entity: "GLP-1 medications (semaglutide / GLP-1 receptor agonists)"
signal_type: drug_or_treatment_claim
allowed_category: chronic disease management
trend_strength_score: 71
opportunity_score: 74
discover_score: 4
urgency: this_week
confidence: medium
confidence_reason: >
  UT Southwestern press release (March 2026) is institutional tier-1; GLP-1 is perennially
  high-search-interest. Skill 02b: PASSED. Confidence capped at Medium pending full primary
  journal citation retrieval (not RCT confirmed from signal alone — press release only).
content_status: new  # self-check skipped; competitor SERP shows heavy GLP-1 coverage but
                     # not on this specific long-term dosing/management angle
source_count: 4
serp_difficulty: Medium
```

**Primary Headline:**
> GLP-1 Medications and Long-Term Weight Management: What New Research Says About Staying on Them

**Alternate Headlines:**
1. "Can You Stop Taking Ozempic? New Research on GLP-1 Drugs and Long-Term Use"
2. "GLP-1 Medication Changes May Help Sustain Weight Loss, Study Finds — Here's What That Means"
3. "How Long Do You Need to Take a GLP-1 Drug? Researchers May Have a Better Answer"

**Recommended Angle:**
Patient-facing practical explainer addressing the #1 question GLP-1 users have: *what happens when I stop, reduce, or change my medication?* UT Southwestern's March 2026 research on "medication changes" supporting long-term weight management is the news peg. The angle: translate what the research actually means for people currently on or considering these drugs, with a clear distinction between the study's findings and what should be discussed with a physician.

**Why Now:**
GLP-1 interest remains among the highest-sustained search categories in health. "Ozempic shortage," dosing regimens, and long-term sustainability questions are actively searched. UT Southwestern research (March 2026) is within extended freshness window and still has SERP gap for patient-facing explainer.

**Key Data Points:**
- UT Southwestern Medical Center March 2026: GLP-1 medication changes may support long-term weight management (full study citation to be retrieved)
- Context: ~15 million Americans currently prescribed GLP-1 drugs (verify current estimate)
- Weight regain data after discontinuation from prior research

**Source Plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| UT Southwestern Medical Center Newsroom | https://www.utsouthwestern.edu/newsroom/articles/year-2026/march-glp-1-medication-changes.html [URL unverified] | 1 | Primary research peg |
| Primary journal | [URL unverified — retrieve from UT Southwestern article] | 1 | Study data |
| FDA GLP-1 drug information | https://www.fda.gov/drugs (semaglutide/tirzepatide pages) | 1 | Regulatory/safety context |
| ADA weight management guidelines | https://www.diabetes.org/clinical-resources/standards-of-care | 1 | Clinical context |

**Expert Sources:**
- Endocrinologist or obesity medicine specialist — cite existing published commentary
- Registered Dietitian Nutritionist — for lifestyle context alongside medication

**Integrity Flags:**
- ⚠️ Confirm study design (observational vs. RCT) before writing; note limitations prominently.
- ⚠️ Do not present as clinical guidance — include explicit note that medication changes should be discussed with prescribing physician.
- ⚠️ Distinguish between brand names (Ozempic, Wegovy, Mounjaro) and drug class (GLP-1 RA) — the study may apply only to specific agents.

**SEO:**
- Primary keyword: `GLP-1 long-term weight management`
- Supporting: `how long to take GLP-1 medication`, `stopping Ozempic weight regain`, `GLP-1 dosing research 2026`, `semaglutide maintenance dose`
- Format: Patient-facing explainer (1,400–1,700 words)
- Schema: Article + FAQPage
- Cluster: Chronic Disease Management → GLP-1 / obesity medicine hub

**Estimated Word Count:** 1,400–1,700 words
**Next Steps:** Retrieve full study citation from UT Southwestern page. Assign to writer with metabolic/endocrinology familiarity. Publish within 2–3 days.

---

### BRIEF 4 — P2 / SHORT-TERM

```yaml
priority_level: P2
publish_timing: short_term
topic: "Arts, Culture, and Biological Aging: What a New Study Found"
primary_entity: "arts and culture engagement / biological aging"
signal_type: study_or_research
allowed_category: aging and longevity
trend_strength_score: 65
opportunity_score: 72
discover_score: 4
urgency: this_week
confidence: medium
confidence_reason: >
  CNN article May 14 2026 (within freshness window); study claims are surprising and
  well-differentiated; however primary journal citation not confirmed from signal data alone.
  2 independent channels (CNN + general wellness search interest). Skill 02b: PASSED
  (mild claim; CNN coverage cites researcher/institution; mechanism plausible).
content_status: new  # self-check skipped; competitor SERP shows generic aging articles
                     # but not arts-specific angle
source_count: 3
serp_difficulty: Low-Medium
```

**Primary Headline:**
> Engaging With Arts and Culture May Slow Biological Aging as Much as Exercise. Here's What the Study Found.

**Alternate Headlines:**
1. "Want to Age More Slowly? A New Study Says Museum Visits and Concerts Might Help"
2. "The Surprising Anti-Aging Activity Scientists Found in a New Study: Arts and Culture"
3. "Arts, Culture, and Aging: What Researchers Discovered About Your Biological Clock"

**Recommended Angle:**
Curiosity-driven explainer with rigorous skepticism baked in. The claim ("as much as exercise") is headline-grabbing and likely overstated in casual coverage — use that as the entry point: *here's what the study actually found, how they measured biological aging, and what the limitations are.* This is where competitors are missing the mark — they're repeating the headline without interrogating the methodology.

**Why Now:**
CNN published May 14, 2026. Aging and longevity is a sustained high-interest category. The arts-aging angle is novel enough to generate genuine audience curiosity; SERP currently thin on evidence-based explainers that interrogate the study methodology.

**Key Data Points:**
- CNN May 14 2026: engaging with arts and culture can slow biological aging "as much as exercise"
- Primary study: measurement method for biological aging (epigenetic clocks? telomere length? — confirm from study)
- Context: exercise-aging mechanism (WaPo March 2026: exercise lowers Alzheimer's risk)

**Source Plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| CNN Health | https://www.cnn.com/2026/05/14/ (arts culture aging) | 1 | News peg |
| Primary study journal | [URL unverified — retrieve from CNN article citation] | 1 | Study methodology and findings |
| NIH/NIA aging research | https://www.nia.nih.gov/research/dab/biological-aging | 1 | Biological aging definition |
| Washington Post exercise/Alzheimer's | https://www.washingtonpost.com/health/2026/03/24/ | 1 | Comparative exercise context |

**Expert Sources:**
- Gerontologist or longevity researcher — for biological aging measurement context
- Arts medicine researcher (growing field — check for published commentary in the primary study's journal)

**Integrity Flags:**
- ⚠️ "As much as exercise" is a strong comparative claim — confirm whether study directly compared arts engagement to exercise or whether this is editorial framing. Adjust headline if comparison is inferential, not direct.
- ⚠️ Identify the biological aging biomarker used (epigenetic clock, etc.) — different biomarkers have different validity profiles; note which one.
- ⚠️ Confirm whether study is observational; if so, note association ≠ causation.

**SEO:**
- Primary keyword: `arts and culture biological aging`
- Supporting: `does culture slow aging`, `arts health benefits research`, `biological aging science`, `how to slow biological aging`, `longevity activities`
- Format: Research explainer (1,200–1,600 words)
- Schema: Article
- Cluster: Aging and Longevity hub

**Estimated Word Count:** 1,200–1,600 words
**Next Steps:** Retrieve primary study citation from CNN article. Assign within 48 hours.

---

### BRIEF 5 — P2 / SHORT-TERM

```yaml
priority_level: P2
publish_timing: short_term
topic: "Rapamycin and Exercise: What the Longevity Drug Research Actually Shows"
primary_entity: "rapamycin (longevity drug)"
signal_type: drug_or_treatment_claim
allowed_category: aging and longevity
trend_strength_score: 63
opportunity_score: 68
discover_score: 4
urgency: this_week
confidence: medium
confidence_reason: >
  Washington Post article April 29 2026 (within freshness window); rapamycin is an
  FDA-approved drug being studied for longevity off-label. Skill 02b: PASSED with Medium cap.
  WaPo cites researcher/institution; primary study traceable but not directly retrieved.
  Confidence capped at Medium per 02b breaking-recall exception analog (off-label research claim).
content_status: new  # self-check skipped; SERP shows some rapamycin longevity coverage
                     # but not exercise-interaction angle specifically
source_count: 4
serp_difficulty: Low-Medium
```

**Primary Headline:**
> Rapamycin May Have a Surprising Effect on Exercise. Here's What the Longevity Research Actually Shows.

**Alternate Headlines:**
1. "The 'Longevity Drug' Rapamycin and Exercise: New Research Reveals an Unexpected Interaction"
2. "Scientists Are Testing Rapamycin for Longer Life. A New Study Complicates the Picture."
3. "Should Longevity Seekers Taking Rapamycin Be Worried About Exercise? A Researcher Explains"

**Recommended Angle:**
Skeptical and clarifying — the WaPo headline ("surprising impact on exercise") is intriguing but likely creates more confusion than clarity for readers. The angle: *explain what rapamycin is, why longevity researchers are interested, what this specific exercise interaction means mechanistically, and what it implies for the people experimenting with it.* The opportunity is the SERP gap between the news article and actual patient/consumer-facing guidance.

**Why Now:**
WaPo published April 29 2026. Longevity and "biohacking" drugs are at peak audience interest. The exercise-rapamycin interaction is a novel and counterintuitive angle not yet well-explained in accessible content. "Longevity drug" framing in Trends confirms audience awareness.

**Key Data Points:**
- WaPo April 29 2026: rapamycin may have surprising impact on exercise
- What rapamycin is: mTOR inhibitor, FDA-approved for organ transplant rejection, studied off-label for longevity
- Exercise-rapamycin interaction mechanism (mTOR pathway role in muscle adaptation)
- Off-label use prevalence among longevity-focused individuals

**Source Plan:**
| Publisher | URL | Tier | Used For |
|---|---|---|---|
| Washington Post Health | https://www.washingtonpost.com/health/2026/04/29/ (rapamycin exercise) | 1 | News peg and primary claim |
| Primary study | [URL unverified — retrieve from WaPo article] | 1 | Mechanism and findings |
| FDA rapamycin (sirolimus) information | https://www.fda.gov/drugs (sirolimus) | 1 | Regulatory context / approved vs off-label |
| NIH aging / rapamycin research | https://www.nia.nih.gov/research (search rapamycin) | 1 | Institutional longevity research context |

**Expert Sources:**
- Geriatrician or longevity researcher with mTOR expertise — cite published research
- Exercise physiologist — for exercise adaptation mechanism explanation

**Integrity Flags:**
- ⚠️ Rapamycin for longevity is off-label use — state clearly that it is not FDA-approved for aging or longevity purposes.
- ⚠️ Do not present off-label longevity use as established clinical practice — note it is experimental.
- ⚠️ Confirm study design and sample population (animal study vs. human trial) — if animal study, note explicitly that results cannot be directly generalized to humans.
- ⚠️ Confidence capped at Medium: verify primary journal source from WaPo article before publishing.

**SEO:**
- Primary keyword: `rapamycin longevity drug exercise`
- Supporting: `rapamycin anti-aging research`, `rapamycin and muscle growth`, `mTOR longevity`, `longevity drugs research 2026`, `rapamycin off-label use`
- Format: Explainer with mechanism section (1,400–1,700 words)
- Schema: Article
- Cluster: Aging and Longevity hub

**Estimated Word Count:** 1,400–1,700 words
**Next Steps:** Retrieve primary study citation from WaPo article. Confirm animal vs. human study before framing. Assign within 48 hours.

---

### BRIEF 6 — P3 / SCHEDULED

```yaml
priority_level: P3
publish_timing: scheduled
topic: "Exercise and Alzheimer's Risk: The Mechanism Scientists Just Discovered"
primary_entity: "exercise and Alzheimer's risk reduction"
signal_type: study_or_research
allowed_category: medical research and clinical trials
trend_strength_score: 61
opportunity_score: 70
discover_score: 4
urgency: this_week
confidence: medium
content_status: new  # self-check skipped
source_count: 3
```

**Headline:** Why Exercise Lowers Alzheimer's Risk — Scientists Think They've Finally Found the Mechanism

**Angle:** Move beyond the "exercise is good for your brain" cliché. WaPo (March 24, 2026) reports scientists may have identified the specific biological mechanism linking exercise to reduced Alzheimer's risk. Lead with the mechanism discovery, explain it accessibly, and connect it to actionable guidance (what type/duration of exercise). SERP gap: existing coverage is headline-only; no accessible mechanism explainer found.

**Key Data Points:**
- WaPo March 24 2026: exercise can lower Alzheimer's risk; scientists may have discovered mechanism
- Specific mechanism (retrieve from WaPo article — likely involves BDNF, amyloid clearance, or cerebrovascular pathway)
- Exercise type and duration associated with the effect

**Sources:**
- Washington Post: https://www.washingtonpost.com/health/2026/03/24/ (exercise Alzheimer's mechanism)
- Primary study: [URL unverified — from WaPo citation]
- Alzheimer's Association: https://www.alz.org/alzheimers-dementia/research_progress/prevention
- NIH/NIA: https://www.nia.nih.gov/health/alzheimers-and-dementia/alzheimers-disease-fact-sheet

**Integrity Flags:**
- ⚠️ Confirm whether mechanism is established or proposed — "may have discovered" language suggests preliminary finding. Reflect uncertainty in body copy.
- ⚠️ Do not conflate risk reduction with prevention — note that exercise reduces risk but is not a guaranteed preventive.

**SEO:** Primary: `exercise Alzheimer's risk mechanism` | Format: Research explainer, 1,200–1,500 words | Difficulty: Medium
**Next Steps:** Retrieve primary study from WaPo. Schedule for days 3–5.

---

### BRIEF 7 — P3 / SCHEDULED

```yaml
priority_level: P3
publish_timing: scheduled
topic: "Coffee, Gut Health, and Aging: What Two New Studies Found"
primary_entity: "coffee / gut health / aging"
signal_type: study_or_research
allowed_category: gut health and microbiome + nutrition and diet science
trend_strength_score: 58
opportunity_score: 65
discover_score: 3
urgency: this_week
confidence: medium
content_status: new  # self-check skipped
source_count: 4
```

**Headline:** Coffee Keeps Delivering Good News for Your Health — But Here's What the Science Actually Shows

**Angle:** Cluster two related coffee-health studies (USA Today May 2 on aging/disease protection; USA Today April 23 on gut health without caffeine) into a single comprehensive explainer. The angle: *what specifically does coffee do to your body, based on the most current research — and does the type of coffee matter?* Combines gut health (rising Trends interest) with aging (high evergreen interest) into a single well-structured article.

**Key Data Points:**
- USA Today May 2 2026: coffee helps protect from aging and disease
- USA Today April 23 2026: coffee's positive gut impacts, even without caffeine
- Specific compounds: polyphenols, chlorogenic acids (likely mechanisms)
- What "protection" means (verify from primary studies — observational association, not causal)

**Sources:**
- USA Today (May 2): https://www.usatoday.com/story/news/health/2026/05/02/ (coffee aging)
- USA Today (April 23): https://www.usatoday.com/story/news/health/2026/04/23/ (coffee gut health)
- Primary studies: [URLs unverified — retrieve from both USA Today articles]
- Harvard Health on coffee research: https://www.health.harvard.edu/staying-healthy/coffee

**Integrity Flags:**
- ⚠️ USA Today is tier-2 health journalism — retrieve primary studies before treating findings as established.
- ⚠️ Both studies are almost certainly observational — note association ≠ causation; coffee consumption correlates with many lifestyle factors.
- ⚠️ "Protects from aging" is a broad claim; define what biomarker or outcome was actually measured.

**SEO:** Primary: `coffee gut health research 2026` | Supporting: `coffee health benefits`, `is coffee good for gut health`, `coffee and aging study`, `coffee polyphenols` | Format: Research roundup, 1,200–1,500 words | Difficulty: Medium
**Next Steps:** Retrieve primary study citations from both USA Today articles. Schedule for days 4–6.

---

### BRIEF 8 — P3 / SCHEDULED

```yaml
priority_level: P3
publish_timing: scheduled
topic: "How Young Adults Are Getting Health Advice in 2026 — and Why It Matters"
primary_entity: "health information sources / young adults"
signal_type: data_release + audience_pain_point
allowed_category: public health and epidemiology
trend_strength_score: 54
opportunity_score: 62
discover_score: 3
urgency: this_week
confidence: medium
content_status: new  # self-check skipped
source_count: 4
```

**Headline:** Doctor, Phone, or Influencer? How Young Adults Are Getting Their Health Advice — and What the Research Says About the Risks

**Angle:** Synthesize two Pew Research Center data points (May 7: trust in health influencers; April 7: Americans value health but face barriers) with Deseret News (May 11: young adults' health advice sources). The angle: a data-driven portrait of how health information seeking has shifted, why it matters for health outcomes, and what consumers should know about evaluating sources. Highly shareable, AI-citation-friendly, audience-relevant.

**Key Data Points:**
- Pew Research May 7 2026: trust in health and wellness influencers (key statistics to pull)
- Pew Research April 7 2026: Americans value health but face challenges
- Deseret News May 11 2026: how young adults get health advice (doctor vs. phone)
- CNN March 16 2026: teens turning to AI for diet information — potential risk angle

**Sources:**
- Pew Research Center (trust in influencers): https://www.pewresearch.org (May 7 2026 report)
- Pew Research Center (Americans health challenges): https://www.pewresearch.org (April 7 2026 report)
- Deseret News: https://www.deseret.com/2026/05/11/ (young adults health advice)
- CNN March 16: https://www.cnn.com/2026/03/16/ (teens AI diet)

**Integrity Flags:**
- ⚠️ Pew Research is tier-1 for survey data; note that survey responses reflect self-reported behavior, which may not match actual health-seeking behavior.
- ⚠️ Avoid implying influencer-sourced health advice is uniformly bad — Pew data may show nuance; reflect it accurately.

**SEO:** Primary: `how young adults get health advice` | Supporting: `health influencer trust research`, `social media health information`, `health literacy young adults`, `AI health advice risks` | Format: Data explainer + tips (1,200–1,500 words) | Difficulty: Low-Medium
**Next Steps:** Retrieve Pew Research report PDFs for full statistics. Schedule for days 4–7.

---

### BRIEF 9 — P3 / SCHEDULED

```yaml
priority_level: P3
publish_timing: scheduled
topic: "Plastics and Preterm Birth: What Parents Need to Know"
primary_entity: "plastic chemicals / phthalates and preterm birth"
signal_type: study_or_research
allowed_category: environmental health + pediatric health
trend_strength_score: 52
opportunity_score: 61
discover_score: 3
urgency: evergreen
confidence: medium
content_status: new  # self-check skipped
source_count: 3
```

**Headline:** Millions of Preterm Births Linked to Plastic Chemicals. Here's What the Research Shows — and What Families Can Do.

**Angle:** Parent-facing explainer on the CNN March 31 2026 study linking plastic chemicals to preterm births and infant deaths. The angle: translate the epidemiological finding into what it means for pregnant women and families — specifically, which chemicals, which exposure routes, and what evidence-based precautions exist. Strong evergreen potential as plastic/chemical exposure is a sustained concern.

**Key Data Points:**
- CNN March 31 2026: millions of preterm births and thousands of infant deaths linked to plastic chemical
- Specific chemical(s) identified (phthalates? BPA? PFAS? — retrieve from CNN article)
- Scale of estimated impact (millions figure — verify with primary study)
- Evidence-based exposure reduction guidance

**Sources:**
- CNN Health: https://www.cnn.com/2026/03/31/ (plastics preterm birth)
- Primary study: [URL unverified — retrieve from CNN article]
- NIH/NICHD reproductive health: https://www.nichd.nih.gov/health/topics/preterm
- EPA endocrine disruptors: https://www.epa.gov/endocrine-disruption

**Integrity Flags:**
- ⚠️ "Linked to" in the headline must be matched by "association found in study" language in body copy — do not imply direct causation.
- ⚠️ Confirm whether this is an observational, meta-analysis, or modeling study — scope of "millions" figure may be a projection, not a direct count.
- ⚠️ Do not generate fear without actionable guidance; balance risk communication with evidence-based precaution steps.

**SEO:** Primary: `plastic chemicals preterm birth risk` | Supporting: `phthalates pregnancy safety`, `reduce plastic exposure pregnancy`, `BPA preterm birth`, `environmental health pregnancy` | Format: Parent-facing explainer, 1,100–1,400 words | Difficulty: Low-Medium
**Next Steps:** Retrieve primary study and confirm chemical class from CNN article. Evergreen; schedule for days 5–7.

---

## REJECTED TOPICS LOG

| Topic | Signal Source | Rejection Stage | Reason |
|---|---|---|---|
| STC Wellness City / Lion Zen Spa / Vyora Wellness | Google Trends | Skill 02 | Off-category: venue/brand queries; no health or wellness content angle |
| Samuel Monroe Jr. health deterioration | Google Trends rising | Skill 02 | Brand safety: celebrity health gossip; no public health or clinical angle |
| Kona Ice nutrition / Panda Express nutrition | Google Trends | Skill 02 | Off-category: branded fast-food nutrition queries; not aligned with evidence-based health content |
| Jelly Roll weight loss / Joyce Vance weight loss | Google Trends | Skill 02 | Celebrity wellness trend without evidence base |
| Jiva Fitness / Fitness Warrior Nation / Planet fitness summer pass | Google Trends | Skill 02 | Brand/local fitness venue queries; no editorial health content angle |
| Baking soda for weight loss | Google Trends | Skill 02 + 02b | Category edge; no credible primary source; unverifiable claim — potential misinformation |
| Kashrut diet / La tulipe noire | Google Trends | Skill 02 | Off-category: appears to be non-health trending query contamination |
| Dr. Ken Berry carnivore diet | Google Trends | Skill 02 | Celebrity/influencer wellness trend; no new study or evidence peg |
| How to read nutrition labels (general query) | Google Trends | Skill 01 | Valid topic but no fresh signal peg this week; evergreen — defer to content calendar |
| Evlution Nutrition BCAA / Optimum Nutrition BCAA | Google Trends | Skill 02 | Supplement marketing; excluded category |
| FDA food additive loophole safety | Google Trends | Skill 02b | **MONITOR** — No specific additive, no traceable primary source or FDA notice; query is speculative. P5. |
| Peptides for health (influencers) — NPR Feb 2026 | Google News | Skill 02b | **MONITOR** — NPR article exists but primary study not determinable; claim scope too broad. P5. |
| Marijuana and mental health (CNN March 2026) | Google News | Skill 01 | Freshness: March 16, 2026 — outside 120-hour freshness window; no new development found |
| Beta-blockers after heart attack (CNN March 2026) | Google News | Skill 01 | Freshness: March 31, 2026 — outside freshness window; no new development |
| Difficult people / aging faster (WaPo March 2026) | Google News | Skill 01 | Freshness: March 8, 2026 — outside freshness window; would need fresh signal to justify update |
| Pregnancy outcomes and men's health (GMA March 2026) | Google News | Skill 01 | Freshness: March 17, 2026 — outside freshness window |
| Nature interventions for higher education neurodivergent students | Google News | Skill 02 | Too narrow/academic audience; not aligned with general health audience |
| 5 more minutes of exercise / longevity (CNN Feb 2026) | Google News | Skill 01 | Freshness: February 13, 2026 — outside freshness window; well-covered |
| Trust in health influencers (Pew May 7) — standalone | Google News | Skill 04 | Merged into Brief 8 (young adults health advice cluster) as supporting data |
| UH Study: Nature reduces negative emotions | Google News | Skill 01 | Freshness: March 24, 2026 — outside freshness window; no fresh development |
| CNBC longevity expert daily routine | Google News | Skill 02 | Expert lifestyle content without new study peg; adjacent to influencer category |

---

## INTEGRITY FLAGS — CONSOLIDATED

All ⚠️ flags for editorial review before publishing:

**Brief 1 — Men's Mental Health Month:**
1. ⚠️ Verify official designation status of "Men's Mental Health Month" — it is a widely observed campaign, not a confirmed federal proclamation
2. ⚠️ Do not apply global mental disorder statistics (1.2B) to men specifically — source men-specific data separately from NIMH
3. ⚠️ Exercise-mental health claims: note study type; do not present as clinical recommendation

**Brief 2 — Natural Preservatives:**
1. ⚠️ Confirm observational vs. RCT study design; state association ≠ causation if observational
2. ⚠️ Name specific preservatives found in study — do not generalize to all natural preservatives
3. ⚠️ Do not claim safe/unsafe intake threshold without study data

**Brief 3 — GLP-1 Medications:**
1. ⚠️ Confirm study design (observational vs. RCT) from UT Southwestern source
2. ⚠️ Explicit physician-consultation disclaimer required for medication guidance
3. ⚠️ Distinguish drug class from brand names throughout

**Brief 4 — Arts and Biological Aging:**
1. ⚠️ Verify whether arts vs. exercise comparison is direct or inferential in the study
2. ⚠️ Identify biological aging biomarker used; note validity profile
3. ⚠️ Confirm observational design; association ≠ causation

**Brief 5 — Rapamycin:**
1. ⚠️ State clearly that rapamycin is not FDA-approved for longevity/aging purposes (off-label use)
2. ⚠️ Do not present off-label longevity use as established clinical practice
3. ⚠️ If animal study: do not generalize to humans without explicit qualification
4. ⚠️ Confidence Medium — verify primary source from WaPo before publishing

**Brief 6 — Exercise / Alzheimer's:**
1. ⚠️ "May have discovered" — mechanism is preliminary; reflect uncertainty
2. ⚠️ Risk reduction ≠ prevention; state clearly

**Brief 7 — Coffee / Gut Health:**
1. ⚠️ USA Today is tier-2; retrieve primary studies before finalizing
2. ⚠️ Both studies likely observational; association ≠ causation
3. ⚠️ Define what biomarker "protection from aging" refers to

**Brief 8 — Young Adults / Health Advice:**
1. ⚠️ Survey data is self-reported; may not match actual behavior
2. ⚠️ Avoid blanket negative framing of influencer-sourced health advice; reflect Pew nuance

**Brief 9 — Plastics / Preterm Birth:**
1. ⚠️ "Linked to" = association; do not imply causation
2. ⚠️ Confirm whether "millions" figure is a projection or direct count
3. ⚠️ Balance risk with actionable, evidence-based precaution guidance

---

## RUN NOTES

```yaml
run_notes:
  date: "2026-06-04"
  signals_reviewed: 87
  signals_retained: 9
  p1_count: 2
  p2_count: 3
  p3_count: 4
  p5_monitor: 2
  integrity_flags_total: 21
  top_topic: "Men's Mental Health Month — June 2026"
  key_themes:
    - "Men's mental health / June awareness month"
    - "Food safety and natural preservatives"
    - "GLP-1 medications / long-term weight management"
    - "Longevity science (rapamycin, arts/aging, exercise/Alzheimer's)"
    - "Coffee and gut health / aging"
    - "Health information sources and digital trust"
    - "Environmental health and pregnancy (plastics)"
  tools_used:
    - "SerpAPI Google Trends (pre-fetch injected)"
    - "SerpAPI Google News (450 articles)"
  tools_unavailable:
    - "Exa semantic search (not confirmed active)"
    - "Reddit API (not confirmed active)"
    - "Direct RSS feed fetch (not confirmed active)"
    - "Content database (disabled by config)"
  self_check_status: "Skipped — site_url not configured. Competitor-check fallback used for SERP gap context."
  deferred_topics_checked: "No data/deferred_topics.yaml found — treated as empty."
  run_history_checked: "No data/run_history.yaml found — no recurring theme flags. First run."
  recurring_theme_flags: []
  p5_monitor_topics:
    - topic: "FDA food additive loophole safety"
      reason: "No specific additive named; no traceable FDA primary notice; query is speculative"
      recheck_on: "2026-06-11"
    - topic: "Peptides promoted by influencers (health claims)"
      reason: "NPR article exists but primary study not determinable from signal data; claim scope too broad"
      recheck_on: "2026-06-11"
  dashboard_output: "outputs/daily_newsroom_dashboard/2026-06-04.html"
  archive_status: "Run logged — data/run_history.yaml created with this entry."
```

---

*Pipeline complete. 9 candidates retained across P1–P3. 2 topics deferred to P5/monitor. All briefs include source links. 21 integrity flags consolidated for editorial review. Self-check skipped (no site_url); competitor fallback applied. Recommend assigning Briefs 1 and 2 for same-day publication.*