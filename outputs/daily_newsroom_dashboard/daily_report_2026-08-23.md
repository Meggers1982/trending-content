# Trending Content OS — Daily Run
**Run date:** 2026-08-23 | **Niche:** Health & Wellness

---

## 1. Preflight Summary

| Check | Status |
|---|---|
| All 7 configs + CLAUDE.md loaded | ✅ |
| `site_niche` / `target_audience` set | ✅ |
| `site_url` | ⚠️ Blank — self-check skipped, competitor-list fallback used (`configs/competitor_list.yaml`) |
| `minimum_trend_strength_score` / `minimum_opportunity_score` | 50 / 55 — valid |
| SerpAPI connected | ✅ |
| Google Trends | ✅ Available via injected pre-fetch (`google_trends_tool: serpapi_prefetch`) |
| Google News Radar | ✅ Injected — 144 unique headlines across 12 queries |
| `data/deferred_topics.yaml` | No entries with a passed `recheck_on` date found |
| Recurring-theme check (run history) | FDA recall cluster (eggs/blueberries/cyclospora/eye drops) and GLP-1/weight-loss-drug coverage have each appeared 3+ consecutive days |

**Decision:** `next_action: run_signal_listener` (proceeded with note on skipped self-check).

---

## 2. Google News Radar Coverage Summary

| Cluster | Disposition | Reasoning |
|---|---|---|
| **FDA/CDC recalls** (egg, blueberry, cyclospora lettuce, eye drops) — [NYT](https://www.nytimes.com/2026/08/14/health/fda-egg-recall-salmonella.html), [Axios](https://www.axios.com/2026/08/22/frozen-blueberries-recall-fda-high-risk-warning), [CDC](https://www.cdc.gov/cyclosporiasis/outbreaks/07-26/index.html) | **Rejected — duplicate** | All matched Recent Coverage list (8/20–8/22) with no new material development |
| **Institutional medical-study press releases** (Harvard pilots [HMS](https://hms.harvard.edu/news/pilots-flight-attendants-have-greater-risk-radiation-related-cancer-death-other-professions), Oregon psilocybin [NPR](https://www.npr.org/2026/08/19/nx-s1-5936443/oregon-psilocybin-ptsd-depression-anxiety), Johns Hopkins lung bacteria [JHM](https://www.hopkinsmedicine.org/news/newsroom/news-releases/2026/08/bacteria-found-in-lung-tumors-may-boost-immune-response-to-cancer), Stanford molecular glue [Stanford](https://med.stanford.edu/news/all-news/2026/08/lymphoma-BCL6-kill-switch.html), WashU laser therapy [WashU](https://medicine.washu.edu/news/laser-therapy-offers-weapon-against-deadly-brain-tumors/)) | **Rejected — duplicate** | Covered 8/20–8/22 |
| **New institutional studies** — Nature Medicine AI liver diagnosis [Nature](https://www.nature.com/articles/s41591-026-04589-y), UT Southwestern Parkinson's [UTSW](https://www.utsouthwestern.edu/newsroom/articles/year-2026/aug-brain-activity-parkinsons-treatment.html) | **Monitored (P5)** | Passed 02b; failed Trend Scorer velocity threshold (single-source, no news/search spread yet) |
| **Celebrity/lifestyle wellness** — Dolly Parton [People](https://people.com/dolly-parton-shares-health-update-while-announcing-plans-for-museum-exclusive-12065750), GQ dating-wellness, Condé Nast stargazing, Fox13 retreat, National Wellness Month pieces | **Rejected — off-category** | Excluded category (celebrity wellness / lifestyle, no evidence angle) |
| **Institutional/business/political** — FDA nominee [NYT](https://www.nytimes.com/2026/08/19/us/politics/heidi-overton-cassidy-fda.html), NJ health premiums, Atrium/Morehouse $700M, U of A/Gila River med school, Teamsters/Corewell contract, clinical-trial industry M&A (Curavit, market-size reports) | **Rejected — off-category** | Pure political/business/local, excluded per category_rules |
| **Infectious disease — travel/outbreak** — CDC Ebola travel guidance [CDC](https://www.cdc.gov/ebola/situation-summary/returning-travelers.html) | **Monitored (P5)** | Tier-1 primary source, gate passed, but no acute velocity; overlaps with 8/21 Moderna vaccine story |
| **AI-in-medicine trend piece** — STAT "shadow medical system" [STAT](https://www.statnews.com/2026/08/19/ai-doctor-outperforms-chatgpt-oura-quest-ro-hims-medical-system/) | **Monitored (P5)** | Borderline trend score (~50), single-outlet, needs corroboration |
| **Patient-facing clinical trial guidance** — KFF [KFF Health News](https://kffhealthnews.org/health-industry/clinical-trials-patients-hhs-easier-advice-on-how-to-enroll-seriously-ill-cancer/) | **Monitored (P5)** | Tier-1, evergreen value, but no current velocity — evergreen backlog candidate |
| **Google Trends–only signals** (no News Radar match): brain-eating amoeba, COVID summer surge, "is farting a sign of good gut health," "tofa weight loss study berkeley" | **Brain-eating amoeba & COVID surge retained; gut-health/tofa study deferred** | See Signal Summary below |

---

## 3. Signal Summary

```yaml
signal_summary:
  run_started_at: 2026-08-23T00:00:00Z
  run_completed_at: 2026-08-23T00:45:00Z
  total_signals_reviewed: ~160
  total_signals_retained: 2
  total_rejected: ~150
  google_trends_available: true
  search_velocity_source: google_trends
  rejection_breakdown:
    off_category: ~55
    brand_safety: 0
    duplicate: ~20
    weak_signal: 9
    unverified_claim: 0
    other: ~4
  highest_priority_topic: "Brain-eating amoeba (Naegleria fowleri) search surge"
  strongest_signal_source: "Google Trends — Trending Now (confirmed by WWLTV local report)"
  tools_unavailable: []
  notes: >
    site_url not configured — self-check skipped; competitor-list fallback used for SERP-gap context.
    FDA recall cluster and GLP-1/weight-loss-drug coverage flagged recurring 3+ consecutive days —
    monitor for staleness. Most fresh medical-study press releases (Nature, UT Southwestern) cleared
    Skill 02b but failed Trend Scorer's velocity threshold due to single-source/no search-spread —
    routed to Monitor rather than padded onto the board. Two Trends-only queries ("is farting a sign
    of good gut health", "tofa weight loss study berkeley") lack any corroborating article and are
    deferred pending research rather than scored on Trends text alone.
```

---

## 4. Skill 02b — Health Claim Verification Gate Routing Summary

| Topic | Risk type | Primary source | Claim alignment | Gate result |
|---|---|---|---|---|
| Nature Medicine — AI-guided liver malignancy diagnosis | medical_study | Nature Medicine journal article (DOI-linkable) | matches | **Pass** |
| UT Southwestern — Parkinson's brain activity discovery | drug_or_treatment_claim (research) | UTSW institutional press release, names researchers | mild_overstatement ("could transform...treatment") | **Pass** — note: lead with actual finding, not "transform" framing |
| CDC — Ebola returning-traveler guidance | dosage_or_safety_guidance | CDC.gov (tier-1, direct) | matches | **Pass** |
| Brain-eating amoeba (Ruston, LA case) | Not triggered — case report, not a study/drug/recall/dosage claim | n/a | n/a | not_applicable |
| COVID-19 summer surge | Not triggered — case-count trend, not a specific claim | n/a | n/a | not_applicable |

No candidates rejected or routed to Monitor at the 02b gate this run.

---

## 5. Final Priority Board

| Priority | Timing | Topic | Trend | Opp. | Discover | Urgency | Confidence |
|---|---|---|---|---|---|---|---|
| **P1** | immediate | Brain-eating amoeba search surge (Naegleria fowleri) | 53 | 68 | 4 | today | medium |
| **P2** | short_term | Summer 2026 COVID-19 case increase | 65 | 65 | 3 | this_week | medium |
| P5 (monitor) | monitor | AI-guided liver malignancy diagnosis (Nature Medicine) | 44 | 74 | — | evergreen | low |
| P5 (monitor) | monitor | UT Southwestern Parkinson's brain-activity discovery | 45 | 70 | — | evergreen | low |
| P5 (monitor) | monitor | CDC Ebola returning-traveler guidance | 41 | 55 | — | evergreen | medium |
| P5 (monitor) | monitor | STAT "AI shadow medical system" | 50 | 58 | — | this_week | low |
| P5 (monitor) | monitor | KFF clinical trial enrollment hurdles | 44 | 60 | — | evergreen | low |

```yaml
- priority_level: P1
  publish_timing: immediate
  topic: "Brain-eating amoeba (Naegleria fowleri) case sparks search surge"
  primary_entity: "Naegleria fowleri"
  signal_type: breaking_news
  allowed_category: infectious disease
  trend_strength_score: 53
  opportunity_score: 68
  discover_score: 4
  urgency: today
  confidence: medium
  content_status: new
  source_count: 2
  recommended_angle: "Skeptical explainer: what Naegleria fowleri actually is, true (rare) infection risk, symptoms, prevention — anchored by the LA case, not fear-mongering"
  why_now: "Google Trends shows 'brain-eating amoeba' breaking out in real-time, driven by an 8-year-old's diagnosis in Ruston, LA; coverage so far is local and thin on risk-context."
  primary_headline: "Brain-Eating Amoeba: How Rare Is Naegleria fowleri, Really? What to Know After the Louisiana Case"
  next_steps: "Confirm case details via WWLTV, pull CDC Naegleria fowleri case-count history and prevention guidance, source ID physician quote."
  notes: "⚠️ Single local-TV source for case specifics; anchor all statistical/medical claims in CDC data, not the news report."

- priority_level: P2
  publish_timing: short_term
  topic: "Summer 2026 COVID-19 case increase across nearly all US states"
  primary_entity: "COVID-19 (2026 summer surge)"
  signal_type: rising_search_interest
  allowed_category: infectious disease / public health and epidemiology
  trend_strength_score: 65
  opportunity_score: 65
  discover_score: 3
  urgency: this_week
  confidence: medium
  content_status: new
  source_count: 2
  recommended_angle: "Practical/evaluative: is this a real surge or normal seasonal variation, dominant variant, symptoms vs. allergies/cold, who should actually be concerned"
  why_now: "COVID-19 trending in real-time health search, tied to reports of cases rising in nearly every state — a recurring late-summer pattern audiences want data-grounded guidance on."
  primary_headline: "Is There Really a Summer COVID Surge? What the Data Shows and Symptoms to Watch"
  next_steps: "Pull CDC COVID Data Tracker wastewater/case trends, confirm dominant variant, get ID physician quote on severity vs. prior surges."
  notes: "⚠️ 'Cases rising in nearly every state' traced to a single outlet — verify against CDC surveillance data before publishing."
```

---

## 6. Editorial Briefs (Retained Candidates)

### Brief 1 — P1: Brain-Eating Amoeba Explainer

```yaml
brief:
  primary_headline: "Brain-Eating Amoeba: How Rare Is Naegleria fowleri, Really? What to Know After the Louisiana Case"
  alternate_headlines:
    - "What Is Naegleria fowleri? The Truth About 'Brain-Eating Amoeba' Risk"
    - "A Child in Louisiana Was Diagnosed With Brain-Eating Amoeba — Here's What That Actually Means"
  topic: "Naegleria fowleri infection risk, symptoms, prevention"
  primary_entity: "Naegleria fowleri"
  search_intent: "informational + skeptical (people are scared and searching to calibrate real risk)"
  angle: "Lead with the actual rarity (CDC counts single digits nationally per year) and freshwater-exposure mechanism, use the Louisiana case only as the hook, then give concrete, evidence-based prevention steps rather than fear-driven framing."
  why_now: "Confirmed breakout on Google Trends 'Trending Now' tied to an 8-year-old's diagnosis in Ruston, LA; existing coverage is local/thin, leaving a national explainer gap."
  integrity_flags:
    - "⚠️ Case-specific details (age, location, condition) come from a single local outlet (WWLTV) — do not embellish beyond what's reported."
    - "⚠️ Avoid sensational framing; infection is exceedingly rare (contracted via nasal exposure to warm freshwater, not drinking water or person-to-person)."
  outline:
    intro: "Hook with the LA case, immediately contextualize rarity"
    sections:
      - "What Naegleria fowleri is and how infection actually occurs"
      - "How rare is it — CDC historical case data"
      - "Symptoms and why early recognition matters"
      - "Prevention: nose clips, avoiding stagnant warm freshwater, neti pot water safety"
      - "What the Louisiana case tells us (and doesn't)"
    conclusion: "Risk calibration takeaway — swim normally, take sensible precautions"
  key_data_points:
    - "CDC has documented very few Naegleria fowleri infections per year historically (verify exact count from CDC.gov before publishing)"
    - "Nearly all infections trace to warm freshwater lakes/rivers or inadequately chlorinated water"
  source_plan:
    - { publisher: "WWLTV.com", url: "[URL unverified]", tier: 3, used_for: "Original local case report" }
    - { publisher: "CDC — Naegleria fowleri", url: "[URL unverified — cite cdc.gov/naegleria fact sheet]", tier: 1, used_for: "Epidemiology, prevention guidance" }
  evidence_requirements: "Moderate — CDC case-count data required to responsibly contextualize risk"
  expert_sources:
    - { type: "Infectious disease physician or CDC waterborne disease epidemiologist", reason: "Calibrate real risk level and prevention advice" }
  internal_links: ["freshwater safety", "summer waterborne illness"]
  visual_brief: "Explainer graphic on how exposure occurs (nasal route only); avoid alarmist imagery"
  seo:
    primary_keyword: "brain-eating amoeba"
    supporting_keywords: ["naegleria fowleri symptoms", "how do you get brain-eating amoeba", "is brain-eating amoeba contagious"]
    format: "explainer / Q&A"
    schema_markup: "FAQPage"
    cluster: "infectious disease / seasonal water safety"
  discover_notes: "Specific named entity + natural Q&A query format + CDC primary-source availability + durable (recurs every summer) = discover_score 4"
  key_takeaways: ["Extremely rare", "Nasal freshwater exposure only", "Prevention is simple and effective"]
  estimated_word_count: "900–1,100"
execution_notes: "Do not name the child or family beyond what WWLTV already published; keep tone calibrating, not alarmist."
confidence: medium
```

### Brief 2 — P2: Summer COVID Surge

```yaml
brief:
  primary_headline: "Is There Really a Summer COVID Surge? What the Data Shows and Symptoms to Watch"
  alternate_headlines:
    - "COVID Cases Are Rising Again — Here's What's Actually Different This Time"
    - "Summer 2026 COVID Surge: Variant, Symptoms, and Who Should Worry"
  topic: "2026 summer COVID-19 case increase"
  primary_entity: "COVID-19"
  search_intent: "practical / evaluative"
  angle: "Ground the 'nearly every state' claim in actual CDC surveillance data, identify the current variant, and give a clear symptom checklist distinguishing COVID from seasonal allergies/common cold — service journalism over alarm."
  why_now: "Real-time Google Trends breakout tied to a TODAY.com report of rising cases; recurring seasonal pattern audiences expect current guidance on."
  integrity_flags:
    - "⚠️ 'Cases rising in nearly every state' is currently a single-outlet claim — verify against CDC wastewater/case data before publication."
  outline:
    intro: "Is this really a surge, and how does it compare to past summers"
    sections:
      - "What the current data shows (CDC wastewater + case trends)"
      - "Which variant is circulating"
      - "Symptoms: COVID vs. allergies vs. common cold"
      - "Who should actually be concerned (immunocompromised, elderly, unvaccinated)"
    conclusion: "Practical takeaway: test if symptomatic, no need for panic"
  key_data_points:
    - "CDC COVID Data Tracker wastewater trend (pull current figures before publishing)"
    - "Dominant variant identification (pull from CDC/WHO variant tracker)"
  source_plan:
    - { publisher: "TODAY.com", url: "[URL unverified]", tier: 2, used_for: "Original surge reporting" }
    - { publisher: "CDC COVID Data Tracker", url: "[URL unverified — cite covid.cdc.gov/covid-data-tracker]", tier: 1, used_for: "Case/wastewater verification" }
  evidence_requirements: "Moderate — requires current CDC surveillance data to support scale claim"
  expert_sources:
    - { type: "Infectious disease physician or epidemiologist", reason: "Contextualize surge severity vs. prior years" }
  internal_links: ["seasonal respiratory illness", "vaccine updates"]
  visual_brief: "Simple case-trend line chart from CDC data; symptom comparison table"
  seo:
    primary_keyword: "summer covid surge 2026"
    supporting_keywords: ["covid symptoms 2026", "is there a covid surge right now", "covid vs allergies symptoms"]
    format: "data-driven explainer"
    schema_markup: "FAQPage"
    cluster: "infectious disease / seasonal illness"
  discover_notes: "Clear entity + strong Q&A fit, but competitive/saturated SERP (every outlet covers COVID surges) caps discover_score at 3"
  key_takeaways: ["Verify scale claim before publishing", "Symptom differentiation is the main service value", "Low severity relative to prior peaks unless data says otherwise"]
  estimated_word_count: "700–900"
execution_notes: "Do not publish the 'nearly every state' framing until cross-checked against CDC's own tracker."
confidence: medium
```

---

## 7. Rejected Topics Log

| Topic | Reason |
|---|---|
| Dolly Parton health update / museum | off_category — celebrity wellness, no evidence angle |
| FDA nominee Senate reservations; NJ teacher health premiums; state medical marijuana legislative study | off_category — pure political |
| New World Screwworm detections (USDA) | off_category — veterinary/agricultural; borderline zoonotic criteria not met (audience_relevance <70) |
| Egg recall, blueberry recall, cyclospora lettuce, eye drop recall, HHS $96M mental health award, 'Maxxing' trend, Harvard pilots radiation, Oregon psilocybin, Johns Hopkins lung bacteria, Stanford molecular glue, WashU laser therapy | duplicate — all covered 2026-08-20–08-22, no new development |
| GQ wellness-gap dating, Condé Nast stargazing wellness, Fox13 retreat, Philly Fed financial wellness, Purdue vet wellness committee, National Wellness Month (KARK, Upper Michigan), Marquette benefits, VA labyrinth, U Michigan BME wellness programming, U Evansville AD promotion | off_category — lifestyle/local/institutional, no evidence-based health angle |
| Atrium Health/Morehouse $700M partnership; U of A/Gila River medical school launch; Teamsters/Corewell nurses contract; KFF rural health transformation tracker | off_category — institutional/labor/policy, low general-audience relevance |
| WSJ biobank AI startup; Curavit/Lindus CRO acquisition (x2); Clinical Trial Vanguard; Clinical Trials Arena UK reforms; Oncodaily Africa trials; News-Medical sponsors; Straits Research market size; MedTech Dive wearables; SC Daily Gazette COVID trial funding | off_category — pure business/industry, not patient-facing |
| Nature genetics MoBa family-design study; Google Research AMIE audio-visual consultations | other — too academic/technical, thin direct audience relevance |
| NYT Jansen's disease clinical trial narrative | weak audience_relevance — ultra-rare disease, narrow reach despite compelling narrative |

**Monitored (P5 — not rejected, insufficient velocity today):** Nature Medicine AI liver diagnosis study; UT Southwestern Parkinson's discovery; CDC Ebola traveler guidance; STAT "AI shadow medical system"; KFF clinical trial enrollment hurdles piece; Think Global Health measles tracker (trend score too low — near-reject).

**Deferred (insufficient sourcing to score):** Google Trends query "is farting a sign of good gut health" (rising +10, no corroborating article); "tofa weight loss study berkeley" (unclear entity, no source found) — added to `data/deferred_topics.yaml` for recheck in 3 days pending discovery of a citable source.

---

## 8. Integrity Flags (Consolidated)

- ⚠️ **Brain-eating amoeba brief:** case specifics sourced from a single local TV outlet (WWLTV) — do not extrapolate; anchor all epidemiological claims in CDC data.
- ⚠️ **COVID surge brief:** "cases rising in nearly every state" is currently a single-outlet (TODAY.com) claim — verify against CDC wastewater/case surveillance before publishing.
- ⚠️ **UT Southwestern Parkinson's (Monitor):** press release uses "could transform Parkinson's treatment" — mild overstatement per Skill 02b; if promoted off Monitor, lead with the actual finding, not the transformation framing.

---

## 9. Run Notes

- `site_url` not configured — self-check skipped; competitor-list fallback (`configs/competitor_list.yaml`) used for SERP-gap context on both retained candidates.
- Google Trends treated as primary search_velocity input throughout (pre-fetch injected, `google_trends_available: true`).
- Recurring themes flagged per run-history check: FDA recall cluster (3+ consecutive days) and GLP-1/weight-loss-drug coverage (3+ consecutive days) — both fully accounted for as duplicates this run, no staleness action needed beyond continued monitoring.
- No `data/deferred_topics.yaml` entries had a passed `recheck_on` date; two new entries added this run (see §7).
- Most fresh single-institution medical-study press releases (Nature Medicine, UT Southwestern) passed Skill 02b cleanly but were held at Skill 04 (Trend Scorer) for lack of current search/news velocity — routed to Monitor rather than padded onto the priority board, consistent with the "default answer is no" principle.
- Dashboard/output file: `outputs/daily_newsroom_dashboard/2026-08-23.html` (to be generated); `data/run_history.yaml` to be updated with this run's entry (2 retained, ~150 rejected, P1 count 1, P2 count 1, top topic: Naegleria fowleri search surge).