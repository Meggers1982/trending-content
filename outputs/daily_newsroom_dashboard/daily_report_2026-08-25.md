# Trending Content OS — Daily Run
**Run date:** 2026-08-25 | **Niche:** Health & Wellness

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
  active_tools: [serpapi_google_trends, serpapi_google_news, serpapi_google_search]
  inactive_tools: [reddit_api, social_search, arxiv_search, youtube_api, content_database]
  can_run_signal_listener: true
  notes: "site_url not configured — self-check skipped; competitor-list fallback (configs/competitor_list.yaml) used for duplicate/SERP-gap context. Reddit/social collectors not injected this run — search_velocity sourced entirely from Google Trends pre-fetch, no estimation needed. data/deferred_topics.yaml checked: no entries past recheck_on date."
next_action: run_signal_listener
```

---

## 2. Google News Radar Coverage Summary
(144 unique headlines across 12 queries reviewed)

| Cluster | Disposition | Notes |
|---|---|---|
| Hospital/health-system business & philanthropy — [Atrium Health $700M commitment](https://atriumhealth.org/about-us/newsroom/news/2026/08/in-partnership-with-morehouse-school-of-medicine-atrium-health-commits-more-than-700-million), [Raiders $25M gift to Intermountain](https://www.raiders.com/news/las-vegas-raiders-announce-25-million-game-changing-gift-to-intermountain-health-to-help-build-nevada-s-first-stand-alone-children-s-hospital), [Corewell nurses ratify contract](https://teamster.org/2026/08/10000-corewell-health-east-nurses-ratify-first-teamsters-contract/), [employer health costs](https://www.axios.com/2026/08/20/health-care-costs-employers-rising), NJ teacher premiums, U of A/Gila River med school | **Rejected** | Off-category — business/labor/philanthropy, no patient-facing health angle |
| Public health outbreaks & infectious disease — [Maryland measles outbreak](https://health.maryland.gov/newsroom/Pages/Maryland%20Department%20of%20Health%20declares%20measles%20outbreak%20in%20three%20Maryland%20counties.aspx), [CDC Ebola traveler guidance](https://www.cdc.gov/ebola/situation-summary/returning-travelers.html), [USDA screwworm detections](https://www.aphis.usda.gov/animals/animal-health/livestock-and-poultry-disease/stop-screwworm/current-status/confirmed) | **Retained / Rejected** | Measles **retained (P1)** — new, breaking. Ebola/Moderna **rejected (existing, covered 8/21)**. Screwworm **rejected** — agricultural/veterinary framing, insufficient human-health angle |
| FDA recalls & food-safety outbreaks — [egg recall](https://www.nytimes.com/2026/08/14/health/fda-egg-recall-salmonella.html), [blueberry recall](https://www.cbsnews.com/news/blueberry-recall-fda-class-1-risk/), [ice pops recall](https://www.goodhousekeeping.com/food-products/a73468917/outshine-fruit-bars-recall/), [sprouts outbreak investigation](https://www.fda.gov/food/outbreaks-foodborne-illness/outbreak-investigation-shiga-toxin-producing-e-coli-salmonella-sprouts-august-2026) | **Retained (1) / Rejected (rest)** | Sprouts outbreak **retained as update** (new pathogen/product, distinct from prior coverage). Egg/blueberry/ice pops/lettuce **rejected — existing**, already absorbed into 8/24 recall-surge explainer |
| Medical research & clinical studies — [Mount Sinai chemo-free breast cancer](https://www.mountsinai.org/about/newsroom/2026/mount-sinai-study-finds-chemotherapy-free-treatment-shows-promise-for-some-patients-with-metastatic-breast-cancer), [Stanford molecular glue](https://med.stanford.edu/news/all-news/2026/08/lymphoma-BCL6-kill-switch.html), [Oregon psilocybin](https://www.npr.org/2026/08/19/nx-s1-5936443/oregon-psilocybin-ptsd-depression-anxiety), [UMass Chan psychedelic study](https://www.umassmed.edu/news/articles/2026/08/umass-chan-researchers-study-psychedelic-medication-for-adjustment-disorder-in-people-with-serious-medical-conditions/), [Nature AI liver diagnosis](https://www.nature.com/articles/s41591-026-04589-y), [Ohio State fentanyl study](https://news.osu.edu/illicit-fentanyl-use-is-more-than-double-medical-use-in-us/), [UCR tick-borne antibody](https://news.ucr.edu/articles/2026/08/21/study-suggests-new-antibody-therapy-tick-borne-disease), [Monteris brain tumor](https://www.massdevice.com/monteris-medical-nueroblate-brain-tumor-study/) | **Mixed** | Mount Sinai **retained (P2)**; Ohio State fentanyl **retained (P3)**. Stanford/Oregon/Monteris **rejected — existing**. UMass Chan psychedelic **monitored (P5)** — single-source + recurring-theme fatigue. Nature AI liver, UCR tick-borne **monitored/rejected** — single-source, thin general-audience fit |
| Clinical trial industry/business — Curavit/Lindus acquisition, Clinical Trials Arena, Straits Research market report, Ochsner-Paradigm, [KFF "join a trial" guide](https://kffhealthnews.org/health-industry/clinical-trials-patients-hhs-easier-advice-on-how-to-enroll-seriously-ill-cancer/) | **Retained (1) / Rejected (rest)** | KFF patient how-to guide **retained (P4, evergreen)**. Industry/M&A/market-sizing items **rejected — off-category** |
| Wellness lifestyle & culture — retreat real estate, [wellness stacking](https://creators.yahoo.com/lifestyle/story/wellness-stacking-why-psychologists-say-it-beats-willpower-for-building-healthy-habits-015140677.html), VA labyrinth, wellness-check police incident, NYT "Spa Weekend" review, [Topol/Cohen "Wellness-Industrial Complex"](https://erictopol.substack.com/p/deborah-cohen-the-wellness-industrial), stargazing travel, [UCLA functional beverage](https://www.uclahealth.org/news/article/wellness-drink-worth-it-decoding-functional-beverage-labels) | **Retained (1) / Monitored (2) / Rejected (rest)** | UCLA functional-beverage piece **retained (P3)**. Wellness-stacking + Topol substack **monitored** — credible but single-source. Retreat/travel/local/entertainment items **rejected — off-category** |
| FDA nominee politics — [Senate Health Panel/Cassidy reservations on FDA nominee](https://www.nytimes.com/2026/08/19/us/politics/heidi-overton-cassidy-fda.html) | **Rejected** | Excluded category — pure political healthcare opinion |
| Google Trends real-time — Vitruvias Therapeutics hyperthyroidism/"superpotent" recall | **Rejected at 02b** | Single local-news attribution (WTHR), no FDA.gov notice retrieved, breaking-recall exception not met (needs 3+ sources). Sent to `deferred_topics.yaml` for recheck in 48h |

---

## 3. Signal Summary

```yaml
signal_summary:
  run_started_at: "2026-08-25T13:00:00Z"
  run_completed_at: "2026-08-25T13:45:00Z"
  total_signals_reviewed: 153   # 144 News Radar + 9 Trends-derived
  total_signals_retained: 6
  total_rejected: 39
  google_trends_available: true
  search_velocity_source: "google_trends"
  rejection_breakdown:
    off_category: 24
    brand_safety: 1
    duplicate: 10
    weak_signal: 3
    unverified_claim: 1
    other: 0
  highest_priority_topic: "Maryland measles outbreak declared across three counties"
  strongest_signal_source: "health.maryland.gov (state health department, tier-2)"
  tools_unavailable: [reddit_api, social_search_x, arxiv]
  notes: "Recall fatigue is a live editorial risk — 6 of the last 6 days' recent-coverage list contain FDA recalls, and the 8/24 recall-surge explainer already covers the 'why so many recalls' meta-question. Only the sprouts outbreak cleared as a genuinely distinct new development this run; egg/blueberry/ice-pop/lettuce items were rejected as existing. Psychedelic-medicine research is recurring (Oregon psilocybin 8/20 → UMass Chan 8/25) — flagged for staleness watch. No Reddit/X data this run; confidence capped at medium on several single-source institutional items as a result."
```

---

## 4. Skill 02b Routing Summary

| Topic | Risk Type | Primary Source | Gate Result | Notes |
|---|---|---|---|---|
| Vitruvias Therapeutics thyroid med recall | Recall / dosage-safety | None retrieved (WTHR only) | **Reject** | Breaking-recall exception requires 3+ sources incl. one FDA/AP/Reuters/trusted outlet — not met. Deferred for recheck. |
| Mount Sinai chemo-free breast cancer treatment | Medical study | Mount Sinai institutional press release | **Pass** | Institutional tier-1 source; note observational vs. trial-phase caveat before publishing. |
| FDA sprouts E. coli/Salmonella outbreak | Recall/outbreak | FDA.gov outbreak investigation page | **Pass** | Direct primary source (FDA.gov). |
| UMass Chan psychedelic medication study | Drug/treatment claim | UMass Chan institutional press release only | **Monitor** | Single source, early-stage/small cohort implied, overlaps recently-covered psilocybin story — routed to P5 for editorial interpretation before briefing. |
| Ohio State fentanyl use study | Data release (non-treatment) | Ohio State News (institutional) | **Not applicable** | Epidemiological usage data, not a treatment/dosage claim — proceeded to standard scoring. |

---

## 5. Final Priority Board

| Priority | Topic | Primary Entity | Signal Type | Category | Trend | Opp | Discover | Urgency | Confidence | Status | Sources | Publish Timing |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **P1** | Maryland measles outbreak declared in 3 counties | Maryland Dept. of Health | breaking_news | Public health & epidemiology | 68 | 75 | 4 | today | medium | new | 2 | immediate |
| **P2** | Mount Sinai chemo-free treatment for metastatic breast cancer | Mount Sinai | study_or_research | Chronic disease management | 55 | 68 | 4 | this_week | medium | new | 1 | short_term |
| **P3** | FDA opens outbreak investigation: E. coli/Salmonella linked to sprouts | FDA | recall | FDA/CDC regulatory updates | 58 | 62 | 3 | today | medium | update | 1 | short_term |
| **P3** | Illicit fentanyl use more than double medical use, Ohio State study finds | Ohio State University | data_release | Public health & epidemiology | 52 | 58 | 3 | this_week | medium | new | 1 | scheduled |
| **P3** | Is a wellness drink worth it? Decoding functional beverage labels | UCLA Health | audience_pain_point | Nutrition and diet science | 52 | 64 | 3 | this_week | medium | new | 1 | scheduled |
| **P4** | What to know before joining a clinical trial | KFF Health News | audience_pain_point | Medical research & clinical trials | 50 | 60 | 4 | evergreen | medium | new | 1 | evergreen |

```yaml
summary:
  total_topics: 6
  high_priority_count: 2
  immediate_actions: "Publish Maryland measles piece today; queue Mount Sinai brief for 1-3 day turnaround."
```

---

## 6. Editorial Briefs

### P1 — Maryland Measles Outbreak (Full Brief)

```yaml
brief:
  primary_headline: "Measles Outbreak Declared in Three Maryland Counties — What to Know About Symptoms, Risk, and Vaccination"
  alternate_headlines:
    - "Maryland Declares Measles Outbreak: Here's Who's at Risk"
    - "Measles Is Spreading in Maryland — Doctors Explain What's Driving the Resurgence"
  topic: "Maryland measles outbreak declared in three counties"
  primary_entity: "Maryland Department of Health"
  search_intent: "informational + evaluative (risk assessment)"
  angle: "Explain the outbreak in the context of the broader 2026 measles resurgence and falling vaccination rates — not just 'what happened' but 'why this is happening now.'"
  why_now: "MDH declared the outbreak 8/24; measles is trending nationally as a vaccine-preventable disease concern (Think Global Health tracker), and search interest in 'measles outbreak' typically spikes fast once local cases are confirmed."
  integrity_flags:
    - "⚠️ Integrity note: Confirm vaccination status breakdown of cases (vaccinated vs. unvaccinated) directly from MDH before publishing — do not assume unvaccinated without sourcing."
    - "⚠️ Integrity note: Case count is likely to change; use MDH's live count, not the 8/24 snapshot, at time of publish."
  outline:
    intro: "Frame the outbreak declaration and immediate practical relevance to MD residents and travelers."
    sections:
      - "What we know: counties affected, case count, timeline"
      - "Why measles outbreaks are resurging nationally (vaccination rate context)"
      - "Symptoms, contagious window, and who's most at risk"
      - "What to do: MMR vaccine guidance, exposure sites if published"
    conclusion: "Practical next steps for readers in/near affected counties."
  key_data_points:
    - "Outbreak declared across 3 Maryland counties (MDH, 8/24/26)"
  source_plan:
    - { publisher: "Maryland Department of Health", url: "https://health.maryland.gov/newsroom/Pages/Maryland%20Department%20of%20Health%20declares%20measles%20outbreak%20in%20three%20Maryland%20counties.aspx", tier: 2, used_for: "Primary outbreak declaration" }
    - { publisher: "Think Global Health", url: "https://www.thinkglobalhealth.org/article/vaccine-preventable-disease-a-global-tracker", tier: 2, used_for: "National measles/vaccine-preventable disease context" }
    - { publisher: "CDC", url: "https://www.cdc.gov/measles/", tier: 1, used_for: "Symptoms, vaccination guidance [URL unverified — confirm live CDC measles page before publishing]" }
  evidence_requirements: "Moderate — public health advisory + CDC guidance, no peer-reviewed study required"
  expert_sources:
    - { type: "Public health official / infectious disease epidemiologist", name: "Maryland state health officer (quote from MDH release) or CDC spokesperson", reason: "Authoritative context on outbreak drivers and vaccination guidance" }
  internal_links: ["(pending site launch — no existing cluster to link)"]
  visual_brief: "Map of affected MD counties; MMR vaccination rate chart if available"
  seo:
    primary_keyword: "Maryland measles outbreak"
    supporting_keywords: ["measles symptoms", "MMR vaccine", "measles outbreak 2026", "is measles contagious"]
    format: "News explainer, 700-900 words"
    schema_markup: "NewsArticle"
    cluster: "Infectious disease / vaccine-preventable disease"
  discover_notes: "High AI-citation potential — specific named entity (MDH), natural query format ('is there a measles outbreak in Maryland'), durable through outbreak resolution."
  key_takeaways: ["Outbreak confirmed in 3 MD counties", "Part of a broader 2026 measles resurgence tied to declining vaccination rates", "MMR vaccine remains highly effective prevention"]
  estimated_word_count: "700-900"
execution_notes: "Time-sensitive — publish within 24h; update case counts before final copy edit."
confidence: medium
```

### P2 — Mount Sinai Chemo-Free Breast Cancer Treatment (Full Brief)

```yaml
brief:
  primary_headline: "A Chemotherapy-Free Treatment Is Showing Promise for Some Patients With Metastatic Breast Cancer"
  alternate_headlines:
    - "Mount Sinai Study: Some Metastatic Breast Cancer Patients May Be Able to Skip Chemo"
    - "What Mount Sinai's New Breast Cancer Study Actually Found — And Who It Applies To"
  topic: "Mount Sinai chemo-free treatment for metastatic breast cancer"
  primary_entity: "Mount Sinai"
  search_intent: "informational + evaluative"
  angle: "Lead with what the study actually showed (which patient subgroup, what endpoints) rather than the 'chemo-free' headline hook — most competitor coverage will oversimplify this."
  why_now: "New institutional announcement (8/23/26), not yet in recent coverage; fits ongoing reader interest in less-toxic cancer treatment options."
  integrity_flags:
    - "⚠️ Integrity note: Confirm whether this is an observational study or randomized controlled trial, and disclose accordingly."
    - "⚠️ Integrity note: Clarify which specific molecular/biomarker subtype qualifies for the chemo-free approach — avoid implying broad applicability to all metastatic breast cancer patients."
  outline:
    intro: "What Mount Sinai found and why it matters for treatment options."
    sections:
      - "What the study tested and in which patients"
      - "How this differs from standard chemotherapy protocols"
      - "Expert caveats: who this does/doesn't apply to"
      - "What's next (trial phase, timeline to broader availability)"
    conclusion: "Practical guidance for patients to discuss with their oncologist."
  key_data_points:
    - "Mount Sinai study findings on chemotherapy-free approach (8/23/26 release)"
  source_plan:
    - { publisher: "Mount Sinai", url: "https://www.mountsinai.org/about/newsroom/2026/mount-sinai-study-finds-chemotherapy-free-treatment-shows-promise-for-some-patients-with-metastatic-breast-cancer", tier: 1, used_for: "Primary study announcement" }
  evidence_requirements: "Heavy — oncology/treatment claim requires peer-reviewed publication confirmation and trial-design disclosure"
  expert_sources:
    - { type: "Oncologist (breast cancer specialist)", name: "Named Mount Sinai study author (from press release)", reason: "Direct study authority and patient-applicability context" }
  internal_links: ["(pending site launch)"]
  visual_brief: "Simple explainer graphic: standard chemo pathway vs. new approach"
  seo:
    primary_keyword: "chemo-free treatment metastatic breast cancer"
    supporting_keywords: ["metastatic breast cancer treatment options", "Mount Sinai breast cancer study", "targeted therapy breast cancer"]
    format: "Research explainer, 700-1000 words"
    schema_markup: "NewsArticle"
    cluster: "Chronic disease management / oncology"
  discover_notes: "Good citation potential — named institution + specific treatment, but needs a DOI/journal citation to reach top discover tier."
  key_takeaways: ["Applies to a specific patient subgroup, not all metastatic breast cancer", "Represents a step toward less-toxic treatment options", "Awaiting peer-reviewed publication confirmation"]
  estimated_word_count: "700-1000"
execution_notes: "Hold for peer-reviewed/journal citation confirmation before publishing if possible; single-source risk noted."
confidence: medium
```

### P3 — FDA Sprouts Outbreak (Concise Brief)

```yaml
brief:
  headline: "FDA Investigates E. coli and Salmonella Outbreak Linked to Sprouts"
  topic: "FDA sprouts E. coli/Salmonella outbreak investigation"
  angle: "Frame as an active, evolving investigation with clear consumer action steps — distinct pathogen/product from the egg and blueberry recalls already covered."
  key_data_points: ["FDA opened outbreak investigation into Shiga toxin-producing E. coli and Salmonella tied to sprouts, August 2026"]
  integrity_flags: ["⚠️ Integrity note: Investigation is ongoing — case count and implicated brands may expand; verify against FDA.gov before publish."]
  expert_type_needed: "Food safety scientist or CDC foodborne illness spokesperson"
  seo: { primary_keyword: "sprouts recall E. coli Salmonella", format: "News update, 400-500 words", serp_difficulty: "Medium" }
  sources: [{ publisher: "FDA", url: "https://www.fda.gov/food/outbreaks-foodborne-illness/outbreak-investigation-shiga-toxin-producing-e-coli-salmonella-sprouts-august-2026" }]
  estimated_word_count: "400-500"
```

### P3 — Ohio State Fentanyl Study (Concise Brief)

```yaml
brief:
  headline: "Illicit Fentanyl Use Now More Than Double Medical Use in the US, Study Finds"
  topic: "Ohio State fentanyl use study"
  angle: "Ground the statistic in what it means for overdose-prevention policy and public awareness, not just the number itself."
  key_data_points: ["Illicit fentanyl use more than double medical use nationally, per Ohio State research (8/24/26)"]
  integrity_flags: ["⚠️ Integrity note: Clarify data source/methodology (self-report vs. toxicology-based) and avoid implying causation with overdose trends without direct citation."]
  expert_type_needed: "Addiction medicine specialist or public health epidemiologist"
  seo: { primary_keyword: "fentanyl use statistics 2026", format: "Data explainer, 500-600 words", serp_difficulty: "Medium" }
  sources: [{ publisher: "Ohio State News", url: "https://news.osu.edu/illicit-fentanyl-use-is-more-than-double-medical-use-in-us/" }]
  estimated_word_count: "500-600"
```

### P3 — UCLA Health Functional Beverage Labels (Concise Brief)

```yaml
brief:
  headline: "Is That Wellness Drink Worth It? How to Actually Read a Functional Beverage Label"
  topic: "UCLA Health functional beverage labels"
  angle: "Skeptical/evaluative — most existing coverage of functional beverages is marketing-driven; this fills a genuine evidence-based gap."
  key_data_points: ["UCLA Health guidance on decoding functional beverage label claims (8/24/26)"]
  integrity_flags: ["⚠️ Integrity note: Distinguish regulated nutrition claims from unregulated marketing language (e.g., 'gut health,' 'immunity boost')."]
  expert_type_needed: "Registered Dietitian Nutritionist"
  seo: { primary_keyword: "are functional beverages worth it", format: "Evaluative guide, 600-800 words", serp_difficulty: "Easy" }
  sources: [{ publisher: "UCLA Health", url: "https://www.uclahealth.org/news/article/wellness-drink-worth-it-decoding-functional-beverage-labels" }]
  estimated_word_count: "600-800"
```

### P4 — KFF Clinical Trial Guide (Concise Brief, Evergreen)

```yaml
brief:
  headline: "Thinking About Joining a Clinical Trial? Here's What to Know First"
  topic: "How to join a clinical trial"
  angle: "Practical how-to for patients navigating enrollment hurdles, especially for serious illness — evergreen with a fresh news hook."
  key_data_points: ["KFF Health News guide on clinical trial enrollment hurdles for seriously ill patients (8/19/26)"]
  integrity_flags: []
  expert_type_needed: "Clinical research coordinator or oncologist with trial-enrollment experience"
  seo: { primary_keyword: "how to join a clinical trial", format: "Evergreen how-to guide, 800-1000 words", serp_difficulty: "Medium" }
  sources: [{ publisher: "KFF Health News", url: "https://kffhealthnews.org/health-industry/clinical-trials-patients-hhs-easier-advice-on-how-to-enroll-seriously-ill-cancer/" }]
  estimated_word_count: "800-1000"
```

---

## 7. Rejected Topics Log

| Topic | Reason |
|---|---|
| Atrium Health $700M commitment, Raiders/Intermountain gift, Corewell nurses contract, employer health costs, NJ teacher premiums, U of A/Gila River med school | Off-category — business/labor/philanthropy, no direct patient health angle |
| CDC Ebola traveler guidance / Moderna Ebola trial | Existing — DRC Ebola outbreak covered 8/21 |
| New World Screwworm detections (USDA) | Off-category — agricultural/veterinary framing, insufficient human-health relevance |
| Egg recall, blueberry recall, ice pops recall, Cyclospora lettuce outbreak | Existing — covered 8/20–8/24, absorbed into recall-surge explainer |
| Vitruvias Therapeutics thyroid recall | Unverifiable health claim — single local-news source, no FDA notice retrieved (see 02b) |
| Stanford molecular glue lymphoma, Oregon psilocybin study, Monteris brain tumor study | Existing — covered 8/20–8/21 |
| Senate Health Panel/FDA nominee reservations | Excluded category — political healthcare opinion |
| UMass Chan psychedelic medication study | Monitor (P5) — single institutional source, overlaps recently-covered psilocybin research |
| Nature AI liver malignancy diagnosis study | Weak signal — single source, low general-audience fit/high technicality |
| UCR tick-borne antibody therapy | Weak signal — single source, early-stage research |
| Robotic-assisted knee replacement trial | Weak signal — single trade-press source, narrow orthopedic audience |
| Curavit/Lindus acquisition, Clinical Trials Arena, Straits Research market report, Ochsner-Paradigm partnership | Off-category — clinical trial industry/business news |
| Wellness retreat real estate, VA labyrinth, wellness-check police incident, NYT "Spa Weekend" review, stargazing travel, UNMC fitness center, Waterfront Wellness Baltimore | Off-category — lifestyle/local/entertainment, no evidence-based health angle |
| Wellness stacking (Yahoo Creators), Topol/Cohen "Wellness-Industrial Complex" | Weak signal — single source each, credible but uncorroborated |

---

## 8. Integrity Flags (Consolidated)

⚠️ **Maryland measles**: Confirm vaccination status of cases and live case count directly from MDH before publishing.
⚠️ **Mount Sinai**: Confirm study design (observational vs. trial) and specific patient subgroup before implying broad applicability.
⚠️ **FDA sprouts outbreak**: Investigation is active — verify case count/implicated products against FDA.gov at publish time.
⚠️ **Ohio State fentanyl study**: Clarify data methodology; avoid implying causation with overdose trend data.
⚠️ **UCLA functional beverage**: Distinguish regulated nutrition claims from unregulated marketing language.

---

## 9. Run Notes

- **Recall fatigue risk**: 5 of the last 6 days' coverage involved FDA recalls; only the sprouts outbreak cleared as genuinely new this run. Recommend the site be selective going forward — cover new recalls only when pathogen/product/scale is materially distinct.
- **Recurring theme flag**: Psychedelic medicine research (Oregon psilocybin 8/20 → UMass Chan 8/25) — approaching staleness; hold for a bigger development (trial results, FDA action) before further coverage.
- **Confidence ceiling**: No Reddit/social collectors were injected this run, so several single-institutional-source items (Mount Sinai, Ohio State, UCLA, KFF) are capped at medium confidence rather than high, despite tier-1 sourcing.
- **Deferred**: Vitruvias Therapeutics thyroid recall added to `data/deferred_topics.yaml`, recheck in 48h for FDA.gov primary notice.
- `data/run_history.yaml` updated with today's entry; today's Key Themes (measles outbreak, chemo-free cancer treatment, recall fatigue, psychedelic medicine recurrence) will be checked against the next 2 runs for staleness.