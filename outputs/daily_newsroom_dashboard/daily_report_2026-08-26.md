# Trending Content OS — Daily Run
**Run date:** 2026-08-26 | **Niche:** Health & Wellness

---

## 1. Preflight Summary

```yaml
preflight_status:
  all_sections_present: true
  missing_sections: []
  site_niche_set: true
  target_audience_set: true
  site_url_set: false
  serpapi_connected: true
  google_trends_available: true
  google_trends_tool: "serpapi_prefetch"
  active_tools: [serpapi_news, serpapi_trends, google_news_radar]
  inactive_tools: [reddit_api, social_search(exa), content_database]
  can_run_signal_listener: true
  notes: "site_url not configured — self-check skipped; competitor-list fallback (configs/competitor_list.yaml) used for duplicate/SERP-gap context. No deferred_topics.yaml entries due for recheck today."
next_action: run_signal_listener
```

---

## 2. Google News Radar Coverage Summary

144 unique headlines across 12 queries reviewed. Main clusters:

| Cluster | Disposition | Reasoning |
|---|---|---|
| **Dolly Parton health/death** (top Trends term + [People.com](https://people.com/dolly-parton-spoke-about-health-hard-times-four-days-before-death-exclusive-12065830)) | **Rejected** | Off-category — celebrity health/death, no evidence-based angle; excluded per `celebrity wellness trends` + brand safety |
| **Measles outbreak** ([CDC](https://www.cdc.gov/measles/data-research/index.html), [NYT via Trending Now], [Maryland.gov](https://health.maryland.gov/newsroom/Pages/Maryland%20Department%20of%20Health%20declares%20measles%20outbreak%20in%20three%20Maryland%20counties.aspx)) | **Retained (update)** | New fatality development (PA deaths) escalates the already-covered Maryland outbreak story |
| **Local/institutional wellness openings & PR** ([Pratt Institute](https://www.pratt.edu/news/a-centralized-hub-for-student-wellness-opens-on-pratts-brooklyn-campus/), [UNMC](https://www.unmc.edu/newsroom/2026/08/25/center-for-healthy-living-integrates-fitness-wellness/), [WBAL-TV](https://www.wbaltv.com/article/inner-harbor-free-fitness-program-baltimore/73495869), Raiders/Atrium Health gift) | **Rejected** | Local/institutional PR, not national-audience relevant |
| **Wellness-industry critique** ([Eric Topol/Deborah Cohen](https://erictopol.substack.com/p/deborah-cohen-the-wellness-industrial), [Yahoo Creators "wellness stacking"](https://creators.yahoo.com/lifestyle/story/wellness-stacking-why-psychologists-say-it-beats-willpower-for-building-healthy-habits-015140677.html)) | **Retained (Topol piece)** / Monitored (stacking piece — thin sourcing) | Skepticism angle fills real SERP gap vs. uncritical wellness content |
| **Psychedelic/psilocybin research** ([NPR](https://www.npr.org/2026/08/19/nx-s1-5936443/oregon-psilocybin-ptsd-depression-anxiety), [OHSU](https://news.ohsu.edu/2026/08/19/study-finds-sustained-benefit-for-people-using-oregon-psilocybin-services), UMass) | **Rejected — existing** | Same Oregon psilocybin story already covered 08-20; no new development |
| **Neuroscience/mental health studies** ([UT Southwestern](https://www.utsouthwestern.edu/newsroom/articles/year-2026/aug-brain-activity-parkinsons-treatment.html), [Columbia](https://www.cuimc.columbia.edu/news/depression-stalls-formation-new-brain-cells), [Medical Xpress loneliness/alcohol](https://medicalxpress.com/news/2026-08-loneliness-rewires-brain-alcohol-preclinical.html)) | **Retained (UTSW, Columbia)** / Rejected (Medical Xpress — preclinical/animal, single weak-tier source) | Fresh, institutional primary sourcing on the first two |
| **NFL CTE study** ([Yahoo Sports](https://sports.yahoo.com/articles/terrifying-nfl-discovery-bombshell-medical-152045510.html)) | **Rejected at 02b** | Sensationalized single-source aggregation, no named study/journal/institution traceable |
| **Clinical trial business/partnership news** (Ochsner-Paradigm, Curavit acquisition, Allegheny-START, CRO M&A) | **Rejected** | Pure pharma/business, excluded category |
| **Clinical trial patient-facing content** ([CNN](https://www.cnn.com/2026/08/22/health/clinical-trials-what-to-know)) | **Rejected — existing** | Duplicate of "What to know before joining a clinical trial" covered 08-25 |
| **FDA recalls** (blueberries, eye drops, sprouts, Cyclospora lettuce — all covered 08-20 to 08-25; [Outshine fruit bars/ice pops](https://www.health.com/outshine-fruit-bars-recall-august-2026-12063179), [Vitruvias thyroid recall](Trending Now)) | **Rejected (all)** | Prior recalls = existing; Outshine = stale (7 days old, exceeds recall freshness ceiling); Vitruvias = rejected at 02b (insufficient sourcing) |
| **Pediatric health** ([Univ. Miami REACH study](https://news.med.miami.edu/reach-study-school-performance-childrens-health/)) | **Retained** | Fresh (1 day), institutional, novel framing, no existing coverage |
| **FDA regulatory/industry guidance** ([MedTech Dive wearables](https://www.medtechdive.com/news/how-can-wearables-be-used-in-clinical-trials-fda-outlines-best-practices/828512/), [Flow Space women in research](https://www.theflowspace.com/interpersonal-health/access-equity/women-clinical-trials-statistics-3039955/)) | **Rejected** | B2B/industry audience misfit; low-tier single-source clickbait, respectively |

---

## 3. Signal Summary

```yaml
signal_summary:
  run_started_at: "2026-08-26T09:00:00Z"
  run_completed_at: "2026-08-26T09:45:00Z"
  total_signals_reviewed: 144
  total_signals_retained: 5
  total_rejected: 139
  google_trends_available: true
  search_velocity_source: "google_trends"
  rejection_breakdown:
    off_category: 62
    brand_safety: 4
    duplicate: 41
    weak_signal: 24
    unverified_claim: 2
    other: 6
  highest_priority_topic: "Measles outbreak deaths — Pennsylvania"
  strongest_signal_source: "CDC / NYT (Trending Now confirmed)"
  tools_unavailable: [reddit_api, exa_social_search]
  notes: >
    Heavy duplicate overlap with last 7 days of coverage — FDA/food-recall stories have
    appeared in 6 of the last 7 runs (blueberries, eye drops, sprouts, lettuce, eggs).
    Flagging as recurring theme: consider a "recall roundup" evergreen format instead of
    one-off pieces to reduce reader fatigue, per run-history pattern. Dolly Parton
    health/death is the dominant real-time Trends spike today but is excluded on brand
    safety + category grounds. Vitruvias Therapeutics recall is genuinely trending
    (confirmed real-world news event) but only one source (NBC5 Chicago) was available in
    this run's evidence — recommend adding to deferred_topics.yaml with a 3-day recheck to
    gather corroborating sources before next attempt.
```

---

## 4. Skill 02b — Health Claim Verification Gate Routing Summary

| Topic | Risk Type | Gate Result | Reason |
|---|---|---|---|
| Vitruvias Therapeutics thyroid recall | recall | **Reject** | Single source (NBC5 Chicago) only; breaking-recall exception requires 3+ corroborating sources incl. FDA/USDA/CDC/AP/Reuters — not met |
| Outshine Fruit Bars/Ice Pops recall | recall | **N/A — filtered at Skill 04** | Would pass gate (2 sources both naming FDA as announcer) but freshness check rejects as stale (7 days old, exceeds recall ceiling) |
| Measles deaths (Pennsylvania) | not applicable | **Not triggered** | breaking_news/public health signal, not study/drug/supplement/recall/dosage type |
| UT Southwestern Parkinson's study | medical_study | **Pass** | Primary source = institutional newsroom naming researchers/institution directly reporting own peer-reviewed work |
| Columbia depression/neurogenesis study | medical_study | **Pass, note added** | Institutional primary source; ⚠️ study population (animal vs. human) not confirmed in evidence — flagged for writer to verify before publishing |
| Univ. Miami REACH study | study_or_research (low-risk framing) | **Pass** | Institutional source, describes study protocol/aim rather than clinical claim requiring dosage/safety verification |
| NFL CTE study | medical_study | **Reject** | No traceable primary source (journal/DOI/institution); single sensationalized secondary aggregator (Yahoo Sports) |

---

## 5. Final Priority Board

| Priority | Topic | Publish Timing | Trend | Opp | Discover | Urgency | Confidence |
|---|---|---|---|---|---|---|---|
| P1 | Measles outbreak deaths — Pennsylvania | immediate | 88 | 78 | 5 | now | high |
| P2 | UT Southwestern Parkinson's brain-activity discovery | short_term | 58 | 68 | 4 | this_week | medium |
| P2 | Columbia depression/neurogenesis study | short_term | 55 | 65 | 4 | this_week | medium |
| P3 | Univ. Miami REACH pediatric health study | scheduled | 50 | 60 | 3 | this_week | medium |
| P3 | Eric Topol/Deborah Cohen — wellness-industrial complex | scheduled | 52 | 64 | 3 | this_week | medium |

---

## 6. Editorial Briefs

### P1 — Measles Outbreak Deaths (Pennsylvania)

```yaml
priority_level: P1
publish_timing: immediate
topic: "Two unvaccinated people die from measles in Pennsylvania amid multi-state outbreak"
primary_entity: "Measles outbreak (Pennsylvania/Maryland)"
signal_type: breaking_news
allowed_category: "infectious disease"
trend_strength_score: 88
opportunity_score: 78
discover_score: 5
urgency: now
confidence: high
content_status: update
source_count: 4
recommended_angle: "What the first deaths of this outbreak wave reveal about vaccination gaps and outbreak trajectory"
why_now: "NYT reports two unvaccinated Pennsylvanians died of measles (Aug 25) — the first fatalities in a wave that includes Maryland's newly declared three-county outbreak (covered 08-25) and CDC's active case tracker."
primary_headline: "Two People Have Died From Measles in Pennsylvania as Outbreak Spreads Across States"
next_steps: "Assign to health/public-health writer; confirm current CDC case count at publish time; verify PA state health dept has issued own statement"
notes: "Update to previously covered Maryland outbreak — do not duplicate, cross-link"
```
**Headline options:** (1) "Two People Have Died From Measles in Pennsylvania as Outbreak Spreads Across States" (2) "Measles Deaths Reported in Pennsylvania — What to Know About the Growing 2026 Outbreak" (3) "First Measles Deaths of 2026 Confirmed as Cases Rise in Maryland and Pennsylvania"

**Outline:** Intro (deaths reported) → What happened (case details, vaccination status) → Outbreak context (Maryland three-county outbreak, national case trend via CDC tracker) → Why measles is resurging (vaccination rates) → What parents/adults should do → FAQ (symptoms, MMR schedule, is my area at risk)

**Sources:**
```yaml
sources:
  - publisher: "CDC"
    url: "https://www.cdc.gov/measles/data-research/index.html"
    tier: 1
    used_for: "National case count/data"
  - publisher: "Maryland Dept. of Health"
    url: "https://health.maryland.gov/newsroom/Pages/Maryland%20Department%20of%20Health%20declares%20measles%20outbreak%20in%20three%20Maryland%20counties.aspx"
    tier: 1
    used_for: "Related outbreak context"
  - publisher: "Think Global Health"
    url: "https://www.thinkglobalhealth.org/article/vaccine-preventable-disease-a-global-tracker"
    tier: 2
    used_for: "Global/national vaccine-preventable disease tracking"
  - publisher: "The New York Times"
    url: "[URL unverified — cited via Trending Now snippet, confirm direct article link before publishing]"
    tier: 1
    used_for: "Primary report of Pennsylvania deaths"
```
**Expert sources:** CDC immunization official (cite existing public CDC guidance); infectious disease epidemiologist (cite existing published commentary from a trusted outlet).

**SEO:** primary_keyword: "measles deaths 2026" | supporting: "measles outbreak Pennsylvania," "measles outbreak Maryland," "MMR vaccine rate 2026" | format: news explainer + FAQ | cluster: infectious disease/outbreaks

⚠️ **Integrity note:** Confirm exact death count and vaccination status directly from NYT/state health dept before publishing — do not amplify unconfirmed social claims about case totals.

---

### P2 — UT Southwestern Parkinson's Brain-Activity Discovery

```yaml
priority_level: P2
publish_timing: short_term
topic: "New brain activity signature linked to Parkinson's motor symptoms"
primary_entity: "UT Southwestern Medical Center"
signal_type: study_or_research
allowed_category: "chronic disease management"
trend_strength_score: 58
opportunity_score: 68
discover_score: 4
urgency: this_week
confidence: medium
content_status: new
source_count: 1
recommended_angle: "What this newly discovered brain activity pattern could mean for future Parkinson's treatment — and how far away clinical use really is"
why_now: "UT Southwestern researchers published findings Aug 21 identifying a brain-activity signature tied to Parkinson's motor symptoms; no other outlet has covered it yet."
primary_headline: "New Brain Activity Discovery Could Reshape Parkinson's Treatment, Researchers Say"
next_steps: "Confirm underlying journal/DOI via UTSW newsroom link; seek independent neurologist comment for balance"
notes: "Single-source coverage — treat opportunity score as provisional until second source confirms"
```
**Sources:** [UT Southwestern Newsroom](https://www.utsouthwestern.edu/newsroom/articles/year-2026/aug-brain-activity-parkinsons-treatment.html) (tier 2, primary_source_type: institutional)

⚠️ **Integrity note:** Early-stage/preclinical framing — avoid "breakthrough treatment" language; clarify distance from patient application.

**SEO:** primary_keyword: "Parkinson's brain activity discovery" | format: explainer | schema: MedicalWebPage

---

### P2 — Columbia Depression/Neurogenesis Study

```yaml
priority_level: P2
publish_timing: short_term
topic: "Depression stalls formation of new brain cells, Columbia study finds"
primary_entity: "Columbia University Irving Medical Center"
signal_type: study_or_research
allowed_category: "mental health and psychology"
trend_strength_score: 55
opportunity_score: 65
discover_score: 4
urgency: this_week
confidence: medium
content_status: new
source_count: 1
recommended_angle: "Untangling neurogenesis science from oversimplified 'depression shrinks your brain' headlines"
why_now: "Columbia researchers published new neurogenesis-depression findings Aug 21, offering fresh mechanistic detail amid steady mental-health search interest."
primary_headline: "How Depression Stops the Brain From Growing New Cells, New Research Shows"
next_steps: "Verify study population (human tissue vs. animal model) before drafting — currently unconfirmed"
notes: "Do not generalize if underlying study is animal-model only; confirm before publish"
```
**Sources:** [Columbia University Irving Medical Center](https://www.cuimc.columbia.edu/news/depression-stalls-formation-new-brain-cells) (tier 2, institutional)

⚠️ **Integrity note:** Study population (human vs. animal) unconfirmed in available evidence — mandatory verification before publishing per health sourcing rules.

---

### P3 — Univ. Miami REACH Study (concise brief)

```yaml
priority_level: P3
publish_timing: scheduled
topic: "School performance proposed as a measurable indicator of children's health"
primary_entity: "University of Miami REACH Study"
signal_type: study_or_research
allowed_category: "pediatric health"
trend_strength_score: 50
opportunity_score: 60
discover_score: 3
urgency: this_week
confidence: medium
content_status: new
source_count: 1
recommended_angle: "Why researchers want school success tracked alongside traditional child health metrics"
why_now: "University of Miami launched the REACH study Aug 25 proposing school performance as a childhood health measure — fresh, uncovered elsewhere."
primary_headline: "Should School Performance Count as a Health Metric? New Study Investigates"
next_steps: "Confirm study stage (protocol launch vs. results) before drafting"
notes: "Clarify this is a study launch, not completed findings"
sources:
  - publisher: "University of Miami Health"
    url: "https://news.med.miami.edu/reach-study-school-performance-childrens-health/"
seo:
  primary_keyword: "school performance child health"
  format: "explainer"
  serp_difficulty: "Easy"
```

---

### P3 — Wellness-Industrial Complex (Eric Topol/Deborah Cohen) — concise brief

```yaml
priority_level: P3
publish_timing: scheduled
topic: "Epidemiologist critiques the wellness industry's use of pseudo-science"
primary_entity: "Deborah Cohen (via Eric Topol's Ground Truths)"
signal_type: expert_conversation
allowed_category: "borderline — passes on evidence-based critique angle, audience_relevance 75"
trend_strength_score: 52
opportunity_score: 64
discover_score: 3
urgency: this_week
confidence: medium
content_status: new
source_count: 1
recommended_angle: "An epidemiologist's take on where wellness marketing ends and evidence begins"
why_now: "Cardiologist-researcher Eric Topol published a new interview (Aug 23) with epidemiologist Deborah Cohen on wellness-industry science claims, landing amid ongoing 'maxxing'/wellness-fatigue coverage."
primary_headline: "The Wellness Industry Is Selling You a Story, Not Science, an Epidemiologist Says"
next_steps: "Confirm direct quotes are attributable to Cohen's published work before drafting"
notes: "Borderline category pass — evidence-based skepticism angle, not product promotion"
sources:
  - publisher: "Eric Topol / Ground Truths (Substack)"
    url: "https://erictopol.substack.com/p/deborah-cohen-the-wellness-industrial"
seo:
  primary_keyword: "wellness industry science claims"
  format: "Q&A-style explainer"
  serp_difficulty: "Medium"
```

---

## 7. Rejected Topics Log (selected)

| Topic | Reason |
|---|---|
| Dolly Parton health/death | off_category — celebrity, brand safety |
| Vitruvias Therapeutics thyroid recall | unverified_claim — 02b reject, single source, no primary/FDA confirmation |
| Outshine Fruit Bars/Ice Pops recall | stale — 7 days old, exceeds recall freshness ceiling |
| NFL CTE study (Yahoo Sports) | unverified_claim — 02b reject, no traceable primary source, sensationalized framing |
| Oregon psilocybin program (NPR/OHSU) | duplicate — covered 08-20, no new development |
| CNN "clinical trial hurdles" | duplicate — covered 08-25 |
| All prior FDA recalls (blueberries, eye drops, sprouts, lettuce, eggs) | duplicate — existing coverage |
| Clinical trial business/M&A news (Ochsner-Paradigm, Curavit, Allegheny-START) | off_category — pure business |
| Medical Xpress loneliness/alcohol study | weak_signal — preclinical/animal-only, single low-tier aggregator |
| Flow Space "Women in Medical Research" | weak_signal — single low-tier source, sensationalized headline |
| MedTech Dive FDA wearables guidance | off_category — B2B/industry audience misfit |
| Local wellness center/hospital PR items | off_category — local, not national-audience relevant |

---

## 8. Integrity Flags Callout

- ⚠️ **Measles deaths (PA):** Confirm exact death count/vaccination status directly from primary NYT report before publishing.
- ⚠️ **UT Southwestern Parkinson's:** Early/preclinical stage — avoid "breakthrough treatment" framing.
- ⚠️ **Columbia depression study:** Study population (human vs. animal) unconfirmed — must verify before drafting.
- ⚠️ **Miami REACH study:** Clarify study-launch vs. completed-findings stage.

---

## 9. Run Notes

- Recurring theme flag: FDA/food-recall stories have appeared in 6 of the last 7 runs — recommend a recall-roundup format rather than continued one-offs.
- Vitruvias Therapeutics thyroid recall recommended for `data/deferred_topics.yaml` with `recheck_on: 2026-08-29` to allow additional corroborating sources to surface.
- `site_url` not configured — competitor-list fallback used for all SERP-gap/duplicate checks this run.
- Dashboard written to `outputs/daily_newsroom_dashboard/2026-08-26.html`; run entry appended to `data/run_history.yaml`.