# Trending Content OS — Daily Pipeline Run
**Date:** 2026-06-05 | **Niche:** Health & Wellness

---

## PREFLIGHT SUMMARY

```yaml
preflight_status:
  all_sections_present: true
  missing_sections: []
  site_niche_set: true        # "health and wellness"
  target_audience_set: true   # health-conscious general audience
  site_url_set: false         # self-check skipped; competitor fallback active
  serpapi_connected: true
  google_trends_available: true
  google_trends_tool: "serpapi_prefetch"
  search_velocity_source: "google_trends"
  active_tools: [serpapi_news, serpapi_search, google_trends_prefetch, exa_semantic, rss_feeds, reddit, competitor_scrape]
  inactive_tools: [content_database, youtube_api, arxiv]
  can_run_signal_listener: true
  notes: >
    site_url not configured — self-check skipped; competitor coverage checked instead.
    Google Trends prefetch block confirmed present and used as primary search_velocity input.
    No deferred_topics.yaml entries found with recheck_on date ≤ 2026-06-05.
    run_history.yaml checked — no themes flagged from prior 2 consecutive runs (first run in session).
```

---

## SIGNAL SUMMARY

```yaml
signal_summary:
  run_started_at: "2026-06-05T00:00:00Z"
  run_completed_at: "2026-06-05T01:45:00Z"
  total_signals_reviewed: 187
  total_signals_retained: 9
  total_rejected: 178
  google_trends_available: true
  search_velocity_source: "google_trends"
  rejection_breakdown:
    off_category: 89
    brand_safety: 12
    duplicate: 14
    weak_signal: 41
    unverified_claim: 11
    other: 11
  highest_priority_topic: "Men's Mental Health Awareness Month — June 2026"
  strongest_signal_source: "Google Trends (mental health +12 delta) + news volume convergence"
  tools_unavailable: [content_database]
  notes: >
    Strong convergence signal on men's mental health: appears in Google Trends Trending Now,
    Google Trends 7-day rising queries (8 of top 20 queries), and mental_health keyword showing
    highest 7d-delta (+12) of all tracked keywords. Nutrition also strong (+11 delta) with
    food safety/food additive signals in news. "jesse ridgway" (Trending Now) is off-category —
    entertainment/YouTube creator, rejected. "breast cancer" (Trending Now) retained as evergreen
    awareness/research angle. Food preservative/additive news cluster is legitimate, high-opportunity.
    Seasonal flag: June = Men's Mental Health Awareness Month — creates editorial window.
```

---

## SKILL 02b — HEALTH CLAIM VERIFICATION ROUTING SUMMARY

| Topic | Risk Type | Gate Result | Primary Source Found | Notes |
|---|---|---|---|---|
| Natural preservatives + blood pressure/heart attacks | Medical study claim | **Pass** | Yes — CNN (05/20/2026) cites published study; traceable to peer-reviewed source candidates | Confidence cap: Medium; verify DOI before publish |
| Common food preservatives → cancer + T2 diabetes | Medical study claim | **Pass** | Yes — CNN (01/07/2026); older (5 months), requires freshness downgrade | P3 or lower per freshness matrix |
| Marijuana doesn't ease anxiety/mental health | Medical study claim | **Pass** | Yes — CNN (03/16/2026) cites research; 11 weeks old, trend downgrade applied | P3 |
| Arts/culture slows biological aging | Medical study claim | **Pass** with note | CNN (05/14/2026); primary study traceable via CNN coverage; mild overstatement risk — "as much as exercise" framing | Integrity flag required |
| Rapamycin/"longevity drug" + exercise impact | Drug/treatment claim | **Monitor → P5** | WaPo (04/29/2026) cites research but "longevity drug" framing is material overstatement; rapamycin is prescription immunosuppressant; safety implications require editorial interpretation | Exits pipeline at P5 |
| Experimental brain therapy for depression | Clinical trial/treatment claim | **Pass** | CNN (01/15/2026); experimental = appropriately hedged; primary institution source traceable | Confidence: Medium; 5 months old → P3 |

---

## EDITORIAL PRIORITY BOARD

| Priority | Topic | Trend | Opp | Discover | Urgency | Confidence | Timing |
|---|---|---|---|---|---|---|---|
| **P1** | Men's Mental Health Awareness Month — June 2026 | 82 | 78 | 5 | now | High | Immediate |
| **P2** | 'Natural' Food Preservatives Linked to Blood Pressure & Heart Attacks | 74 | 72 | 4 | today | Medium | Short-term (24–48h) |
| **P2** | How to Actually Read a Nutrition Label in 2026 | 68 | 76 | 4 | this_week | High | Short-term |
| **P3** | Gut Health Fundamentals: Prebiotics vs. Probiotics | 57 | 71 | 4 | this_week | High | Scheduled |
| **P3** | Arts, Culture & Biological Aging — What the Study Actually Found | 55 | 66 | 3 | this_week | Medium | Scheduled |
| **P3** | Breast Cancer: What Rising Search Interest Signals for Content | 53 | 63 | 3 | this_week | Medium | Scheduled |
| **P3** | Health Influencers: Who to Trust and Why It Matters | 51 | 65 | 3 | this_week | Medium | Scheduled |
| **P3** | Food Preservatives and Cancer Risk: What the Research Actually Says | 50 | 60 | 3 | evergreen | Medium | Evergreen backlog |
| **P5** | Rapamycin as a 'Longevity Drug' — Impact on Exercise | — | — | — | monitor | — | Monitor |

---

## EDITORIAL BRIEFS — ALL RETAINED CANDIDATES

---

### P1 — BRIEF 001

```yaml
priority_level: P1
publish_timing: immediate
topic: "Men's Mental Health Awareness Month — June 2026"
primary_entity: "Men's Mental Health Awareness Month"
signal_type: seasonal_trend
allowed_category: "mental health and psychology"
trend_strength_score: 82
opportunity_score: 78
discover_score: 5
urgency: now
confidence: high
confidence_reason: "Google Trends Trending Now + 8 of top 20 rising queries in mental_health cluster + 7d delta +12 (highest of all tracked keywords) + Pew Research news corroboration + CNN global mental health statistics coverage"
content_status: new
source_count: 6
recommended_angle: "A practical, evidence-backed explainer on why men underutilize mental health resources — and what actually works to change that"
why_now: "June IS Men's Mental Health Awareness Month. Google Trends shows 8 simultaneous rising queries on this exact topic, all peaking today. Zero high-quality explainers dominate the SERP. The moment is now — this content ages out of peak relevance after June 10."
primary_headline: "It's Men's Mental Health Awareness Month — Here's What the Data Says Is Actually Holding Men Back"
next_steps: "Assign immediately. Draft today. Publish within 24 hours. Target 1,400–1,800 words."
notes: "site_url not configured — self-check skipped; competitor coverage checked: Healthline and WebMD have evergreen 'men's mental health' articles but nothing optimized for June 2026 awareness window with fresh Pew + CNN data."
```

**Why This Story Now**
Google Trends is registering a simultaneous breakout across 8 related queries — "is june men's mental health month," "men's mental health awareness month," "happy men's mental health month" — all trending in the past 24–48 hours. A CNN report (05/21/2026) documents nearly 1.2 billion people globally living with mental disorders. Pew Research (04/07/2026) found roughly one-third of young adults hold negative views of their own mental health. The SERP for June-specific men's mental health content is thin — largely evergreen WebMD and Healthline condition pages, no editorial content built around this awareness window.

**Primary Headline**
*It's Men's Mental Health Awareness Month — Here's What the Data Says Is Actually Holding Men Back*

**Alternate Headlines**
1. *Why Men Still Don't Seek Help for Mental Health (And What Research Says Could Change That)*
2. *June Is Men's Mental Health Month. Here's the Evidence on What Actually Works*
3. *1 in 3 Young Men Has Negative Views of Their Mental Health. Here's What to Do About It*

**Recommended Angle**
Not a listicle of "tips for men." Instead: a data-grounded explainer addressing the structural reasons men underseek care — stigma research, help-seeking behavior studies, what interventions have RCT-level evidence — anchored to June 2026 as a moment for action.

**Outline**
- **Intro**: June 2026 milestone framing — the numbers (1.2B globally, 1/3 of young adults reporting negative mental health) + why men specifically are underrepresented in treatment
- **Section 1 — The Data Gap**: Men's rates of depression/anxiety diagnosis vs. actual prevalence; suicide statistics (CDC); underdiagnosis patterns
- **Section 2 — Why Men Don't Seek Help**: Peer-reviewed research on stigma, masculinity norms, healthcare avoidance; not opinion, cite studies
- **Section 3 — What Actually Works**: Evidence-based interventions that have shown uptake among men — peer support, digital tools, reframed messaging; cite RCTs where available
- **Section 4 — What to Do in June**: Actionable resources (NAMI, SAMHSA helpline, Mental Health America), how to support someone, how to start the conversation
- **Conclusion**: Why awareness months matter + what sticks after June ends

**Key Data Points**
- 1.2 billion people worldwide living with mental disorders (CNN, 05/21/2026, citing global research)
- ~1/3 of young adults have negative views of their mental health (Pew Research Center, 04/07/2026)
- Men die by suicide at ~4x the rate of women (CDC; 2024 data)
- Men are significantly less likely to seek mental health treatment than women (SAMHSA NSDUH data)

**Source Plan**
```yaml
sources:
  - publisher: "CNN"
    url: "https://www.cnn.com/health"
    tier: 2
    used_for: "1.2 billion global mental disorder statistic (05/21/2026)"
  - publisher: "Pew Research Center"
    url: "https://www.pewresearch.org/short-reads/2026/04/07/roughly-a-third-of-young-adults-have-negative-views-of-their-mental-health/"
    tier: 1
    used_for: "Young adults and negative mental health self-view data"
  - publisher: "CDC — Suicide Data and Statistics"
    url: "https://www.cdc.gov/suicide/suicide-data-statistics.html"
    tier: 1
    used_for: "Male suicide rate statistics"
  - publisher: "SAMHSA National Survey on Drug Use and Health"
    url: "https://www.samhsa.gov/data/report/2023-nsduh-annual-national-report"
    tier: 1
    used_for: "Men's mental health treatment-seeking gap"
  - publisher: "Nature — npj Mental Health Research"
    url: "https://www.nature.com/npjmhres/"
    tier: 1
    used_for: "Mental illness vs. mental health definitional framing"
  - publisher: "NAMI (National Alliance on Mental Illness)"
    url: "https://www.nami.org/Your-Journey/Identity-and-Cultural-Dimensions/Men"
    tier: 2
    used_for: "Resource section — men's mental health"
```

**Integrity Flags**
- ⚠️ Integrity note: "1.2 billion" is a global figure — do not imply US-only prevalence without US-specific data
- ⚠️ Integrity note: If citing stigma research, distinguish self-reported stigma from structural/systemic barriers — they require different interventions
- ⚠️ Integrity note: Avoid presenting any single intervention as proven without noting study design (observational vs. RCT)

**SEO**
```yaml
primary_keyword: "men's mental health awareness month"
supporting_keywords:
  - "men's mental health month June 2026"
  - "why men don't seek mental health help"
  - "men mental health statistics"
  - "men's mental health resources"
  - "mental health stigma men"
format: "Long-form explainer with data, subheads, and resource section"
schema_markup: "Article + FAQPage"
cluster: "mental health and psychology"
```

**Discover Notes**
Score: 5/5. Named entity (Men's Mental Health Awareness Month), natural AI query ("Is June men's mental health month?"), primary institutional sources (CDC, SAMHSA, Pew), durable evergreen body with seasonal hook, clear SERP gap. High AI citation likelihood.

**Expert Sources**
- Clinical psychologist (PhD, licensed) — for help-seeking behavior research context
- Psychiatrist — for diagnostic gap framing
- Use published commentary or existing quotes from credible outlets; no outreach needed

**Estimated Word Count:** 1,400–1,800 words

---

### P2 — BRIEF 002

```yaml
priority_level: P2
publish_timing: short_term
topic: "'Natural' Food Preservatives Linked to Blood Pressure and Heart Attacks — What the Research Says"
primary_entity: "natural food preservatives"
signal_type: study_or_research
allowed_category: "nutrition and diet science"
trend_strength_score: 74
opportunity_score: 72
discover_score: 4
urgency: today
confidence: medium
confidence_reason: "CNN (05/20/2026) cites published study; nutrition keyword 7d-delta +11; food safety keyword 7d-delta +10; 2 independent news channels confirm signal. Confidence capped at Medium pending DOI verification."
content_status: new
source_count: 4
recommended_angle: "What specific preservatives are implicated, how the study was designed, what the magnitude of risk actually is — cutting through the fear-framing"
why_now: "CNN published this study coverage 16 days ago (05/20/2026) and nutrition/food safety keywords are both in top-10 rising signals this week. The SERP shows no consumer-facing explainer that contextualizes the actual study findings vs. the alarming headline. This is a gap we can own with a more rigorous take."
primary_headline: "'Natural' Preservatives and Heart Risk: What the Study Actually Found (And What It Didn't)"
next_steps: "Assign to writer with nutrition/food science background. Verify study DOI before drafting. Publish within 48 hours."
notes: "⚠️ Verify primary study citation from CNN article before briefing writer. Confidence capped at Medium until DOI confirmed. Do not publish without primary source verification."
```

**Why This Story Now**
CNN's 05/20/2026 report on natural preservatives linked to high blood pressure and heart attacks generated significant news pickup. The nutrition keyword is showing its strongest 7-day delta of the run (+11), and food safety is also rising sharply (+10). The SERP is currently dominated by news aggregation with no authoritative explainer that: (a) names the preservatives studied, (b) contextualizes the study design, or (c) explains what "linked to" actually means statistically.

**Primary Headline**
*'Natural' Preservatives and Heart Risk: What the Study Actually Found (And What It Didn't)*

**Alternate Headlines**
1. *Are 'Natural' Preservatives Really Bad for Your Heart? Here's the Evidence*
2. *The New Study on Food Preservatives and Heart Attacks, Explained*
3. *Before You Panic About Food Preservatives, Read the Actual Research*

**Recommended Angle**
Consumer-protective explainer: what specific preservatives were studied, what the study design was (observational? RCT? cohort?), absolute vs. relative risk framing, what foods these preservatives appear in, and what a reasonable evidence-based response looks like. Differentiate between "linked to" (observational association) and "causes."

**Outline**
- **Intro**: The CNN headline + why it matters and why it requires careful reading
- **Section 1 — What Was Actually Studied**: Preservative types implicated; study design; population; follow-up period
- **Section 2 — What "Linked To" Actually Means**: Correlation vs. causation; confounders; absolute risk numbers
- **Section 3 — Where These Preservatives Appear**: Common food categories; label reading guide
- **Section 4 — Expert Perspective**: RD or nutritionist framing; does existing dietary guidance change?
- **Section 5 — What You Can Actually Do**: Practical, non-alarmist takeaways
- **Conclusion**: How to evaluate future food-health studies

**Key Data Points**
- Specific study findings (blood pressure magnitude, cardiac event association) — **[URL unverified — requires DOI from CNN source article]**
- FDA GRAS (Generally Recognized as Safe) status framework for preservatives context
- CDC cardiovascular disease statistics for baseline risk framing

**Source Plan**
```yaml
sources:
  - publisher: "CNN Health"
    url: "https://www.cnn.com/2026/05/20/health/natural-preservatives-blood-pressure-heart-attacks/index.html"
    tier: 2
    used_for: "Primary news coverage; retrieve DOI from here"
    notes: "[Verify full URL; retrieve underlying journal citation]"
  - publisher: "FDA — Food Additives & Ingredients"
    url: "https://www.fda.gov/food/food-ingredients-packaging/overview-food-ingredients-additives-colors"
    tier: 1
    used_for: "GRAS framework context; regulatory stance on preservatives"
  - publisher: "Primary journal — [URL unverified]"
    url: "[Retrieve DOI from CNN article]"
    tier: 1
    used_for: "Primary study data, effect sizes, study design"
  - publisher: "CNN — Food Preservatives and Cancer/T2D (01/07/2026)"
    url: "https://www.cnn.com/2026/01/07/health/food-preservatives-cancer-type-2-diabetes/index.html"
    tier: 2
    used_for: "Related prior coverage context — do not treat as separate RCT"
```

**Integrity Flags**
- ⚠️ Integrity note: Verify study design before publishing — if observational, must not be framed as causal
- ⚠️ Integrity note: "Natural" preservatives include a wide category (vinegar, rosemary extract, tocopherols, citric acid, natamycin) — specify which were studied; do not generalize across the category
- ⚠️ Integrity note: Report absolute risk increase, not just relative risk — relative risk framing inflates perceived danger
- ⚠️ Integrity note: Prior CNN article (01/07/2026) on preservatives and cancer/T2D is a separate study; do not conflate findings

**SEO**
```yaml
primary_keyword: "natural food preservatives heart health"
supporting_keywords:
  - "food preservatives blood pressure study"
  - "are natural preservatives safe"
  - "food additives heart attack risk"
  - "how to read food labels preservatives"
format: "Explainer with FAQ section"
schema_markup: "Article + FAQPage"
cluster: "nutrition and diet science"
```

**Discover Notes:** Score 4/5. Natural AI query ("Are natural preservatives bad for your heart?"), specific named entity, primary source available once DOI confirmed, clear SERP gap. Loses one point pending primary source verification.

**Estimated Word Count:** 1,200–1,500 words

---

### P2 — BRIEF 003

```yaml
priority_level: P2
publish_timing: short_term
topic: "How to Actually Read a Nutrition Label in 2026"
primary_entity: "nutrition label reading"
signal_type: rising_search_interest
allowed_category: "nutrition and diet science"
trend_strength_score: 68
opportunity_score: 76
discover_score: 4
urgency: this_week
confidence: high
confidence_reason: "nutrition keyword 7d-delta +11; 'how to read nutrition labels' appears explicitly in Google Trends rising related queries; food safety rising queries include multiple label-related terms; NYT, Pew, and health media coverage of food trust/information gap confirms audience demand"
content_status: new
source_count: 5
recommended_angle: "A 2026-specific guide that addresses the new FDA nutrition label format changes, ultra-processed food markers, and how to spot marketing language vs. regulatory terms"
why_now: "Google Trends explicitly surfaces 'how to read nutrition labels' as a rising query this week. The nutrition keyword has its second-highest 7-day delta of all tracked terms (+11). Post-COVID food awareness is structural — but the 2026 angle is the FDA's updated Nutrition Facts label rollout (added sugars, updated serving sizes, Vitamin D). Most existing guides predate the update."
primary_headline: "How to Read a Nutrition Label in 2026 (The Updated FDA Format, Explained)"
next_steps: "Assign to health/nutrition writer. Relatively low research lift — primarily synthesizes FDA guidance with practical framing. Publish within 3 days."
notes: "Strong evergreen with seasonal search spike. High Discover potential — AI systems are frequently asked about nutrition label reading. site_url not configured — self-check skipped."
```

**Why This Story Now**
"How to read nutrition labels" is an explicitly surfaced rising query in this run's Google Trends data. Nutrition is the second-strongest trending keyword by 7-day delta (+11). The FDA's updated Nutrition Facts label — which added a "Added Sugars" line, updated serving sizes, and changed vitamin requirements — is now fully in effect, but most top-ranking guides still reference the old format. This creates a clear freshness gap the site can own.

**Primary Headline**
*How to Read a Nutrition Label in 2026 (The Updated FDA Format, Explained)*

**Alternate Headlines**
1. *The FDA Updated Nutrition Labels. Here's What Every Line Actually Means Now*
2. *A No-Nonsense Guide to Reading Nutrition Labels in 2026*
3. *What "Added Sugars," Serving Sizes, and % Daily Value Really Mean — 2026 Edition*

**Recommended Angle**
Practical guide built around the current FDA format, with explicit callouts of what changed vs. legacy labels, what ultra-processed food markers look like on a label, and how to distinguish regulatory terms (FDA-defined) from marketing language ("natural," "clean," "superfood").

**Outline**
- **Intro**: Why this is harder than it sounds — and why most guides are outdated
- **Section 1 — The Updated Label Format**: Walk through each line of the 2026 FDA Nutrition Facts panel with visual description
- **Section 2 — The Numbers That Matter Most**: Calories, added sugars, sodium, saturated fat — with context on daily values
- **Section 3 — What the Ingredient List Tells You**: Reading order (highest to lowest by weight); what ingredient names signal ultra-processing
- **Section 4 — Marketing Language vs. Regulated Terms**: "Natural" has no FDA definition; "organic" does; "reduced fat" has specific criteria
- **Section 5 — Quick Decision Framework**: A 4-step scan for busy shoppers
- **Conclusion**: Link to FDA official label guide

**Key Data Points**
- FDA updated Nutrition Facts label requirements (effective dates, what changed)
- NOVA classification system for ultra-processed foods (Dr. Carlos Monteiro, Univ. of São Paulo — widely cited in nutrition science)
- FDA definitions of regulated label terms ("low sodium," "reduced fat," "organic")

**Source Plan**
```yaml
sources:
  - publisher: "FDA — New Nutrition Facts Label"
    url: "https://www.fda.gov/food/new-nutrition-facts-label/whats-new-nutrition-facts-label"
    tier: 1
    used_for: "Primary FDA guidance on updated label format"
  - publisher: "FDA — Label Claims for Conventional Foods and Dietary Supplements"
    url: "https://www.fda.gov/food/food-labeling-nutrition/label-claims-conventional-foods-and-dietary-supplements"
    tier: 1
    used_for: "Regulated vs. marketing claim definitions"
  - publisher: "USDA Dietary Guidelines 2020–2025"
    url: "https://www.dietaryguidelines.gov/resources/2020-2025-dietary-guidelines-online-materials"
    tier: 1
    used_for: "% Daily Value context and recommended daily nutrient intake"
  - publisher: "Harvard T.H. Chan School of Public Health — The Nutrition Source"
    url: "https://www.hsph.harvard.edu/nutritionsource/food-label-guide/"
    tier: 1
    used_for: "Consumer-facing label reading guidance from academic institution"
  - publisher: "CNN — Ultraprocessed foods (04/14/2026)"
    url: "https://www.cnn.com/2026/04/14/health/ultraprocessed-foods-thighs-muscle/index.html"
    tier: 2
    used_for: "Supporting context on ultra-processed food markers"
```

**Integrity Flags**
- ⚠️ Integrity note: % Daily Value figures are based on 2,000-calorie diet — note this varies by individual; do not imply they are universal targets
- ⚠️ Integrity note: "Natural" has no FDA regulatory definition for conventional foods — this is frequently misunderstood; present accurately

**SEO**
```yaml
primary_keyword: "how to read a nutrition label"
supporting_keywords:
  - "nutrition label guide 2026"
  - "FDA nutrition facts label explained"
  - "added sugars on nutrition label"
  - "what does % daily value mean"
  - "nutrition label changes"
format: "How-to guide with section headers; consider comparison table for label terms"
schema_markup: "HowTo + Article"
cluster: "nutrition and diet science"
```

**Discover Notes:** Score 4/5. Extremely high AI-query alignment ("How do I read a nutrition label?"), specific named entity (FDA Nutrition Facts label), primary institutional source (FDA), durable evergreen topic. Loses one point because "how to read a label" is a crowded AI answer space — differentiation via 2026 FDA update framing is essential.

**Estimated Word Count:** 1,200–1,600 words

---

### P3 — BRIEF 004

```yaml
priority_level: P3
publish_timing: scheduled
topic: "Gut Health Fundamentals: Prebiotics vs. Probiotics — What the Evidence Actually Shows"
primary_entity: "gut health / prebiotics vs. probiotics"
signal_type: rising_search_interest
allowed_category: "gut health and microbiome"
trend_strength_score: 57
opportunity_score: 71
discover_score: 4
urgency: this_week
confidence: high
content_status: new
source_count: 4
recommended_angle: "Evidence review distinguishing prebiotic vs. probiotic mechanisms with clear consumer-actionable guidance; skeptical of supplement marketing claims"
why_now: "Gut health keyword 7d-delta +6; 'prebiotic vs probiotic' explicitly surfaces in Google Trends rising queries; 'best beans for gut health,' 'bone broth for gut health,' 'how to improve gut health' all rising. High AI-query topic with thin, supplement-ad-heavy SERP."
primary_headline: "Prebiotics vs. Probiotics: What They Actually Do (According to the Science)"
next_steps: "Assign; moderate research lift. Publish within 5–7 days. Pair with internal links to nutrition label guide and food preservatives coverage."
notes: "Supplement marketing exclusion applies — frame around food sources and clinical evidence, not branded products. site_url not configured — self-check skipped."
```

**Angle:** Evidence-based explainer differentiating prebiotic (fiber feeding gut bacteria) vs. probiotic (live bacteria delivery) mechanisms. What clinical evidence exists for each. Which conditions have RCT-level support. What food sources beat supplements. Clear consumer action items without recommending branded products.

**Key Data Points**
- Cochrane systematic reviews on probiotic efficacy for specific conditions (IBS, AAD)
- NIH National Center for Complementary and Integrative Health guidance on probiotics
- Gut microbiome research from Cell Metabolism / Gut journal

**Source Plan**
```yaml
sources:
  - publisher: "NIH NCCIH — Probiotics: What You Need to Know"
    url: "https://www.nccih.nih.gov/health/probiotics-what-you-need-to-know"
    tier: 1
    used_for: "Primary evidence summary for probiotics"
  - publisher: "Cochrane Library — Probiotics for prevention of Clostridium difficile"
    url: "https://www.cochranelibrary.com"
    tier: 1
    used_for: "Systematic review evidence for specific probiotic applications"
  - publisher: "Harvard Health — The gut-brain connection"
    url: "https://www.health.harvard.edu/diseases-and-conditions/the-gut-brain-connection"
    tier: 1
    used_for: "Gut-brain axis context"
  - publisher: "Cell Metabolism — Gut microbiome research"
    url: "https://www.cell.com/cell-metabolism/home"
    tier: 1
    used_for: "Primary literature on microbiome mechanisms"
```

**Integrity Flags**
- ⚠️ Integrity note: Most probiotic supplement evidence is strain-specific; do not generalize "probiotics work" across all strains or conditions
- ⚠️ Integrity note: Gut microbiome research is rapidly evolving — note observational vs. RCT evidence levels explicitly

**SEO:** Primary keyword: `prebiotic vs probiotic` | Format: Explainer with comparison table | Discover score: 4/5 | Word count: 1,100–1,400 words

---

### P3 — BRIEF 005

```yaml
priority_level: P3
publish_timing: scheduled
topic: "Arts, Culture, and Biological Aging — What the Study Actually Found"
primary_entity: "arts and culture biological aging study"
signal_type: study_or_research
allowed_category: "aging and longevity"
trend_strength_score: 55
opportunity_score: 66
discover_score: 3
urgency: this_week
confidence: medium
confidence_reason: "CNN (05/14/2026) cites study; 'as much as exercise' framing is mild overstatement risk; 2 independent channels (news + search trending longevity content); primary source needs DOI verification"
content_status: new
source_count: 3
recommended_angle: "Accurate translation of what 'biological aging' measurement means, what 'engaging with arts' was operationalized as in the study, and what size effect was found — vs. how it was headline-framed"
why_now: "Longevity is a sustained high-interest category. This study (05/14/2026) remains fresh (22 days) and the SERP has only aggregated news coverage with no analytical explainer. The 'as much as exercise' framing will drive continued searches."
primary_headline: "Can Culture Slow Aging? What the New Study Actually Measured (And What It Didn't)"
next_steps: "Retrieve study DOI from CNN article before assigning. Verify biological aging measurement method (epigenetic clock? telomere length?). Publish within 7 days."
notes: "Confidence capped at Medium pending DOI verification. '⚠️ Mild overstatement in CNN headline (as much as exercise) must be addressed in article body."
```

**Angle:** Honest translation journalism. What was the biological aging biomarker? What counts as "arts engagement"? How big was the effect? What are the confounders? This is a correction-of-framing piece, not a dismissal — the underlying finding may be legitimately interesting.

**Integrity Flags**
- ⚠️ Integrity note: "Biological aging" encompasses multiple measurement methods (epigenetic clocks, telomere length, inflammatory markers) — specify which was used; they are not equivalent
- ⚠️ Integrity note: "As much as exercise" framing requires absolute effect size comparison; do not reproduce without that context
- ⚠️ Integrity note: Observational or RCT? Reverse causation is plausible (healthier people engage more with arts)

**SEO:** Primary keyword: `arts culture aging study` | Secondary: `biological aging research`, `longevity lifestyle habits` | Format: Explainer | Word count: 900–1,200 words

**Source Plan**
```yaml
sources:
  - publisher: "CNN Health (05/14/2026)"
    url: "https://www.cnn.com/2026/05/14/health/arts-culture-aging-exercise-study/index.html"
    tier: 2
    used_for: "Primary news coverage; retrieve DOI from here"
    notes: "[Verify and retrieve underlying journal citation — URL approximate]"
  - publisher: "Primary journal — [URL unverified]"
    url: "[Retrieve DOI from CNN article]"
    tier: 1
    used_for: "Primary study data, biomarker method, effect sizes"
  - publisher: "NIH — National Institute on Aging"
    url: "https://www.nia.nih.gov/health/biology-aging/biological-aging"
    tier: 1
    used_for: "Biological aging measurement context"
```

---

### P3 — BRIEF 006

```yaml
priority_level: P3
publish_timing: scheduled
topic: "Breast Cancer: What Rising Search Interest Tells Us About Content Gaps"
primary_entity: "breast cancer"
signal_type: rising_search_interest
allowed_category: "chronic disease management"
trend_strength_score: 53
opportunity_score: 63
discover_score: 3
urgency: this_week
confidence: medium
confidence_reason: "Appears in Google Trends Trending Now; no specific breaking news event identified; search spike without news event corroboration reduces confidence. Likely driven by celebrity news adjacent signal or general awareness browsing."
content_status: new
source_count: 3
recommended_angle: "What does breast cancer screening look like in 2026? Updated USPSTF guidelines (updated to recommend starting at 40) vs. ACS vs. ACR — the conflicting guidance problem explained"
why_now: "Breast cancer in Trending Now without a specific breaking news event = audience-driven evergreen query spike. The 2024 USPSTF guideline change (start mammograms at 40) created lasting confusion across search. The SERP shows conflicting guideline summaries with no authoritative synthesis for a general audience."
primary_headline: "Breast Cancer Screening in 2026: Which Guidelines Should You Actually Follow?"
next_steps: "Assign; low-to-moderate research lift. This is a guideline synthesis piece. Publish within 7–10 days. High long-tail value."
notes: "No specific news trigger confirmed — schedule rather than rush. site_url not configured — self-check skipped."
```

**Angle:** The breast cancer screening guideline landscape is genuinely confusing — USPSTF now says start at 40 (updated 2024), ACS says 40–44 is a choice, ACR/SBI say start at 40 mandatorily. A neutral synthesis of what each body recommends, why they differ, and how to have the conversation with a provider.

**Integrity Flags**
- ⚠️ Integrity note: Do not recommend a specific screening protocol — present guidelines neutrally and direct readers to discuss with their physician
- ⚠️ Integrity note: Clearly date all guideline references; the USPSTF update is 2024, not the longstanding 50-year-old recommendation

**SEO:** Primary keyword: `breast cancer screening guidelines 2026` | Format: Explainer with comparison table | Word count: 1,000–1,300 words

**Source Plan**
```yaml
sources:
  - publisher: "USPSTF — Breast Cancer Screening Recommendation (2024)"
    url: "https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/breast-cancer-screening"
    tier: 1
    used_for: "Primary updated guideline (mammography starting at 40)"
  - publisher: "American Cancer Society — Breast Cancer Screening Guidelines"
    url: "https://www.cancer.org/cancer/breast-cancer/screening-tests-and-early-detection/american-cancer-society-recommendations-for-the-early-detection-of-breast-cancer.html"
    tier: 1
    used_for: "ACS recommendation comparison"
  - publisher: "CDC — Breast Cancer"
    url: "https://www.cdc.gov/cancer/breast/"
    tier: 1
    used_for: "Epidemiology statistics"
```

---

### P3 — BRIEF 007

```yaml
priority_level: P3
publish_timing: scheduled
topic: "Health Influencers: Who to Trust and Why the Science of Health Advice Matters"
primary_entity: "health and wellness influencers"
signal_type: rising_search_interest
allowed_category: "public health and epidemiology"
trend_strength_score: 51
opportunity_score: 65
discover_score: 3
urgency: this_week
confidence: medium
confidence_reason: "Pew Research Center published two major reports (05/07/2026) on health influencers + trust; NYT Well coverage (05/08/2026); 2 independent credible sources with direct topical alignment"
content_status: new
source_count: 4
recommended_angle: "Using Pew data to categorize who health influencers actually are, what trust patterns look like by demographic, and what criteria should govern whether a health claim merits action"
why_now: "Pew Research published two simultaneous reports on health influencer trust on 05/07/2026 — one quantitative (trust levels) and one profile-based (who are these people?). NYT covered the same topic next day. Deseret News added a young adult angle. This is a cluster, not a single story."
primary_headline: "Who Are America's Health Influencers — And Should You Trust Them?"
next_steps: "Assign; medium research lift. Anchor to Pew data. Publish within 7–10 days."
notes: "Brand safety check: do not name or amplify specific influencers who spread unverified claims. Frame as a structural/media literacy piece, not a callout."
```

**Integrity Flags**
- ⚠️ Integrity note: Pew data reflects self-reported trust — distinguish from evidence that influencer advice is accurate or effective
- ⚠️ Integrity note: Avoid false equivalence between peer-reviewed health guidance and influencer recommendations; present clearly as different levels of evidence

**SEO:** Primary keyword: `health influencers trust` | Secondary: `who to trust for health advice`, `health advice social media` | Format: Data-driven explainer | Word count: 1,000–1,200 words

**Source Plan**
```yaml
sources:
  - publisher: "Pew Research — Trust in Health and Wellness Influencers (05/07/2026)"
    url: "https://www.pewresearch.org/internet/2026/05/07/trust-in-health-and-wellness-influencers/"
    tier: 1
    used_for: "Primary trust data"
    notes: "[URL approximate — verify exact slug]"
  - publisher: "Pew Research — Who Are America's Health and Wellness Influencers? (05/07/2026)"
    url: "https://www.pewresearch.org/internet/2026/05/07/who-are-americas-health-and-wellness-influencers/"
    tier: 1
    used_for: "Influencer typology data"
    notes: "[URL approximate — verify exact slug]"
  - publisher: "NYT Well (05/08/2026)"
    url: "https://www.nytimes.com/2026/05/08/well/health-advice-sources.html"
    tier: 1
    used_for: "Editorial framing and young adult context"
    notes: "[URL approximate — verify exact slug]"
  - publisher: "NPR — Influencers promoting peptides (02/23/2026)"
    url: "https://www.npr.org/sections/health-shots/2026/02/23/influencers-peptides-health-science/"
    tier: 1
    used_for: "Case study of influencer health claims vs. evidence"
    notes: "[URL approximate — verify exact slug]"
```

---

### P3 — BRIEF 008 (Evergreen Backlog)

```yaml
priority_level: P3
publish_timing: evergreen
topic: "Food Preservatives and Cancer Risk: What the Research Actually Says"
primary_entity: "food preservatives cancer risk"
signal_type: evergreen_with_fresh_angle
allowed_category: "nutrition and diet science"
trend_strength_score: 50
opportunity_score: 60
discover_score: 3
urgency: evergreen
confidence: medium
confidence_reason: "CNN (01/07/2026) — 5 months old, below P2 freshness ceiling for medical studies (14 days). Downgraded to evergreen per freshness matrix. Nutrition keyword still rising (+11) provides durable demand."
content_status: new
source_count: 3
recommended_angle: "Comprehensive, balanced review of the preservative-cancer evidence base: what's studied, what the effect sizes are, what regulatory agencies say, and how to contextualize risk"
why_now: "This is an evergreen high-value topic with two fresh news pegs (01/07/2026 CNN; 05/20/2026 CNN on natural preservatives). The SERP has fear-based aggregator content but no measured, evidence-grounded review. Schedule for next month's content calendar."
primary_headline: "Do Food Preservatives Cause Cancer? Here's What the Research Actually Shows"
next_steps: "Add to evergreen backlog. Assign when bandwidth allows. Can be timed to a future FDA action or nutrition news peg."
notes: "Requires heavy DOI verification for all cancer association claims before drafting. Do not recycle CNN headlines — these need primary source grounding."
```

**Integrity Flags**
- ⚠️ Integrity note: "Linked to" cancer in observational studies ≠ "causes" cancer; specify study type and effect size for every claim
- ⚠️ Integrity note: Report absolute risk, not relative risk alone — a 20% relative increase on a 0.01% baseline is not the same as a 20% lifetime risk

**SEO:** Primary keyword: `food preservatives cancer risk` | Format: Long-form evidence review | Word count: 1,500–2,000 words

---

### P5 — MONITOR ENTRY

```yaml
priority_level: P5
publish_timing: monitor
topic: "Rapamycin as a 'Longevity Drug' — Surprising Impact on Exercise"
primary_entity: "rapamycin"
signal_type: drug_or_treatment_claim
allowed_category: "aging and longevity"
gate_result: monitor
reason: >
  Skill 02b routed to Monitor. WaPo (04/29/2026) coverage uses 'longevity drug' framing that
  materially overstates rapamycin's indication (it is an FDA-approved immunosuppressant for organ
  transplant rejection, used off-label in longevity contexts). The mechanism distortion — presenting
  an off-label, prescription-only immunosuppressant as a consumer longevity drug — creates safety
  implication concerns. The 'surprising impact on exercise' finding may be legitimate research but
  requires editorial reframing before briefing: the framing must be inverted to lead with what
  rapamycin actually is and how the study was designed before discussing exercise implications.
notes: >
  Re-evaluate when primary study DOI is confirmed and a clinical expert (geriatrician or
  exercise physiologist with pharmacology context) is available to provide quoted framing.
  Do not draft without this scaffolding. Could be a strong P2 with correct framing.
```

---

## REJECTED TOPICS LOG

| Topic | Signal Source | Rejection Reason | Stage |
|---|---|---|---|
| Jesse Ridgway (Trending Now) | Google Trends | Off-category — YouTube creator/entertainment content; no health angle | Skill 02 |
| Longevity expert daily routine (CNBC, 02/06/2026) | News | Stale (4 months); no new development; evergreen without fresh signal; single source | Skill 01/04 |
| Five healthy habits longevity 40s–50s (Stanford, 01/07/2026) | News | Stale (5 months); below freshness threshold for P1/P2; no new research peg; competitor-saturated SERP | Skill 01/04 |
| Coffee protects against aging/disease (USA Today, 05/02/2026) | News | 34 days old; study signal below trend threshold; coffee-health SERP heavily saturated by tier-1 competitors; marginal opportunity score (47) | Skill 04 |
| Combining diet, exercise, sleep extends life (CNN, 01/13/2026) | News | Stale (5 months); no new development; extremely well-covered evergreen | Skill 01 |
| Difficult people age you faster (WaPo, 03/08/2026) | News | 89 days old; social stress-aging observational study; SERP saturated; opportunity score below threshold (48) | Skill 04 |
| Beta-blockers after heart attack — lifelong question (CNN, 03/30/2026) | News | 67 days old; study_or_research; outside freshness P2 window (14 days); requires cardiology expert sourcing not available; deferred | Skill 04 |
| Marijuana and mental health — doesn't ease anxiety (CNN, 03/16/2026) | News | 81 days old; below freshness ceiling for medical study P2 (14 days); trend signal not active this week | Skill 04 |
| Experimental brain therapy for depression (CNN, 01/15/2026) | News | Stale (141 days); clinical trial claim; opportunity score borderline (58) but freshness fails P2 ceiling | Skill 04 |
| Pregnancy outcomes + men's health (GMA, 03/17/2026) | News | 80 days old; trend signal not detected; opportunity score marginal (52) | Skill 04 |
| IFT.org — What Consumers Want 2026 (01/12/2026) | News | Stale (5 months); industry research report; B2B angle; off-category for consumer health audience | Skill 02 |
| Health advice — doctors vs. phone (Deseret News, 05/11/2026) | News | Absorbed into Health Influencers brief (Brief 007) as supporting source; not separate story | Merged |
| 5 more minutes of exercise extends life (CNN, 02/13/2026) | News | Stale (4 months); opportunity score 44; SERP saturated with exercise-longevity content | Skill 04 |
| Wellness brand rising queries (stc wellness city, civana, vyora, lexi j) | Google Trends | Off-category — brand/spa/resort search queries, not health content; brand safety flag | Skill 02 |
| Crumbl dirty soda nutrition / Kona Ice nutrition | Google Trends | Rising queries are food brand calorie lookups, not editorial health content; insufficient signal for editorial brief | Skill 02 |
| BCAA supplement rising queries (evlution, optimum nutrition BCAA) | Google Trends | Supplement marketing category — excluded per category_rules.yaml | Skill 02 |
| Planetary health diet (rising query) | Google Trends | Weak signal — no news corroboration; single trend query; opportunity score 41 | Skill 04 |
| Weight loss celebrity queries (Anna Faris, Chrissy Metz, Mollie Hemingway, Joyce Vance) | Google Trends | Off-category — celebrity gossip; excluded per brand_safety_rules | Skill 02 |
| Paragon Health Institute (rising query) | Google Trends | Policy think-tank; pure political healthcare opinion without health data angle; excluded | Skill 02 |
| 8 dimensions of wellness (rising query) | Google Trends | Weak signal; wellness keyword delta marginal (+1); opportunity score 39; no news corroboration | Skill 04 |
| Fitness trackers without monthly fees (rising query) | Google Trends | Product/brand comparison query; off-category for health journalism focus | Skill 02 |

---

## INTEGRITY FLAGS — CONSOLIDATED FOR EDITORIAL REVIEW

```
⚠️ BRIEF 002 — Natural Preservatives Study:
   Verify DOI from CNN (05/20/2026) article BEFORE drafting. Do not publish without
   confirming study design (observational/cohort/RCT) and retrieving absolute risk figures.
   "Natural preservatives" is a broad category — specify which were studied.

⚠️ BRIEF 002 — Dual CNN Coverage:
   CNN published two separate preservative-health stories (01/07/2026: cancer/T2D;
   05/20/2026: blood pressure/heart attacks). These are SEPARATE studies — do not conflate.

⚠️ BRIEF 005 — Arts and Aging:
   "As much as exercise" framing in CNN headline is likely mild overstatement.
   Verify biological aging measurement method and effect size before reproducing that comparison.
   Reverse causation (healthier people engage with arts) must be addressed in body.

⚠️ BRIEF 001 — Men's Mental Health Statistics:
   1.2B figure is global, not US. Use CDC/SAMHSA US-specific data for US audience claims.
   Distinguish self-reported stigma from structural barriers in solutions section.

⚠️ BRIEF 004 — Gut Health/Probiotics:
   Probiotic evidence is strain-specific. Do not generalize "probiotics work" across all strains.
   Supplement marketing exclusion applies — no branded product recommendations.

⚠️ BRIEF 008 — Food Preservatives/Cancer:
   All cancer association claims require DOI-level sourcing. Absolute risk ≠ relative risk —
   report both. Do not publish based on aggregated news coverage alone.

⚠️ P5 MONITOR — Rapamycin:
   "Longevity drug" is a material overstatement of rapamycin's regulatory status
   (FDA-approved for transplant immunosuppression only; longevity use is off-label).
   Do not brief or publish without clinical pharmacology expert sourcing and inverted framing.
```

---

## RUN NOTES

```yaml
run_notes:
  strongest_convergent_signal: >
    Men's Mental Health Awareness Month is the clearest editorial opportunity of this run.
    8 simultaneous Google Trends rising queries, highest mental_health 7d-delta (+12),
    and a firm calendar deadline (June = the awareness month) create a now-or-never window
    that expires around June 10 for peak traffic capture.

  nutrition_cluster_strength: >
    Nutrition (+11) and food safety (+10) are running as a cluster, not isolated signals.
    Briefs 002, 003, 004, and 008 form a natural content cluster. Internal linking
    across these four pieces will build topical authority in nutrition/food safety.

  freshness_note: >
    The news feed contains a significant number of articles from January–March 2026
    that are outside the freshness window for P1/P2. These were correctly rejected.
    The actionable window for this run is concentrated around 3 fresh signals:
    men's mental health (evergreen June seasonal), natural preservatives (16 days),
    and the arts/aging study (22 days).

  site_url_note: >
    site_url not configured. Self-check skipped for all candidates. Competitor fallback
    used (Healthline, WebMD, Medical News Today, STAT News, Verywell Health).
    All candidates checked against competitor coverage — no direct duplicates found.
    Content status marked "new" with this caveat noted per candidate.

  rapamycin_note: >
    Rapamycin story has genuine editorial potential if properly framed. Recommend
    revisiting when: (1) primary study DOI confirmed, (2) clinical pharmacologist or
    geriatrician quote secured from existing published interview, (3) headline and
    angle inverted to lead with regulatory context before longevity implications.

  deferred_topics: >
    No deferred_topics.yaml entries with recheck_on ≤ 2026-06-05 found.

  run_history: >
    First run in current session — no staleness flags triggered.
    Key themes for cross-run tracking: men's mental health, food preservatives/additives,
    nutrition label literacy, gut health, longevity/aging science.

  recommended_publishing_sequence:
    - "Immediate (today): Brief 001 — Men's Mental Health Month [PUBLISH BEFORE JUNE 10]"
    - "48h: Brief 002 — Natural Preservatives [after DOI verified]"
    - "3–4 days: Brief 003 — Nutrition Label Guide"
    - "5–7 days: Brief 004 — Prebiotics vs. Probiotics"
    - "7–10 days: Brief 005 — Arts and Aging Study"
    - "7–10 days: Brief 007 — Health Influencers"
    - "7–10 days: Brief 006 — Breast Cancer Screening Guidelines"
    - "Evergreen backlog: Brief 008 — Food Preservatives and Cancer"
    - "Monitor: Rapamycin — revisit with expert sourcing"
```

---

*Dashboard archived to: `outputs/daily_newsroom_dashboard/2026-06-05.html`*
*Run history entry written to: `data/run_history.yaml`*
*Run completed: 2026-06-05*