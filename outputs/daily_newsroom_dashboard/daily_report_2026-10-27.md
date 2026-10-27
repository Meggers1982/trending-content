# Trending Content OS — Daily Run
**Run date:** 2026-10-27 | **Niche:** Health & Wellness

---

## 1. Preflight Summary

| Check | Status |
|---|---|
| All 7 configs + CLAUDE.md sections loaded | ✅ |
| `site_niche` / `target_audience` set | ✅ |
| `site_url` | ⚠️ Not configured — self-check skipped, competitor-list fallback used |
| SerpAPI connected | ✅ |
| Google Trends | ✅ Available via injected pre-fetch (`search_velocity_source: google_trends`) |
| `data/deferred_topics.yaml` | No entries past `recheck_on` today |
| `data/run_history.yaml` recurrence check | ⚠️ GLP-1/weight-loss and cancer-immunotherapy/recall clusters have appeared in 3+ consecutive runs (10/23–10/26) — flagged for staleness awareness below |

**Decision:** `run_signal_listener` — proceed with full pipeline.

---

## 2. Google News Radar Coverage Summary (144 unique headlines, 12 queries)

| Cluster | Disposition | Why |
|---|---|---|
| **Health care costs / insurance affordability** (KFF, [NYT](https://www.nytimes.com/2026/10/22/business/health-insurance-costs-workers-premiums-deductibles.html), [NPR](https://www.npr.org/2026/10/22/nx-s1-6008153/health-insurance-costs-kff-commonwealth), Commonwealth Fund, Peterson-KFF, [Ohio Capital Journal](https://ohiocapitaljournal.com/2026/10/27/medical-debt-hit-1-in-4-americans-and-1-in-5-ohioans-last-year-even-the-insured-study-shows/)) | **Retained** | 5+ independent tier-1/2 sources converging same week on medical debt/cost burden — strongest convergence signal in the radar |
| **Wellness lifestyle/local events** ([CNN "wellness darties"](https://www.cnn.com/2026/10/22/us/video/wellness-darties-college-students-find-new-way-to-party), campus wellness fairs, [Granada Theater sale](https://www.nbcdfw.com/news/local/historic-granada-theater-sells-to-new-york-based-wellness-brand/4095056/)) | **Rejected** | Local/human-interest, no evidence base, fails audience-relevance threshold |
| **Medical study — new findings** (OU bariatric/diabetes, USF colorectal cancer, News-Medical genome study, VCU NIH grant, Yale amino acid, Penn personality genetics) | **Split** | Bariatric (B) and colorectal cancer (C) retained as new; amino acid + personality genetics **rejected as existing** (covered 10/26); genome study and VCU grant **monitored** (single-source/early-stage) |
| **Clinical trial health** (PTSD remission, Ebola vaccine trial, T-cell therapy, HIV newborn dosing, pulmonary artery denervation) | **Mostly existing/monitor** | PTSD, Ebola vaccine trial, T-cell therapy already covered 10/24–10/26 → **existing**; HIV dosing + pulmonary denervation → **monitor** (narrow audience / too early) |
| **FDA recall health** (toothpaste, GLP-1 injections) | **Rejected — existing** | Both covered 10/23, no new development since |
| **Ebola outbreak scale** (Trending Now: "ebola" + Al Jazeera WHO vaccine trial context) | **Retained — update** | New case-count milestone (10,000+) distinct from the 10/25 vaccine-trial story |
| **Political/regulatory adjacent** (Jennifer Shuford CDC resignation, Missouri AG vs. Eli Lilly, HHS HTI-5 rule, Calley Means/RFK wellness-stake story) | **Rejected** | Brand-safety/off-category — political or pure policy/business, no clear health-research angle |

---

## 3. Signal Summary

```yaml
signal_summary:
  run_started_at: "2026-10-27T13:00:00Z"
  run_completed_at: "2026-10-27T13:45:00Z"
  total_signals_reviewed: 144
  total_signals_retained: 4
  total_rejected: 140
  google_trends_available: true
  search_velocity_source: "google_trends"
  rejection_breakdown:
    off_category: 6
    brand_safety: 3
    duplicate: 9
    weak_signal: 118
    unverified_claim: 1
    other: 3
  highest_priority_topic: "DR Congo Ebola outbreak surpasses 10,000 cases"
  strongest_signal_source: "Google Trends Trending Now + NBC News + WHO (via Al Jazeera)"
  tools_unavailable: []
  notes: "GLP-1/weight-loss and recall/cancer-immunotherapy clusters have recurred 3+ consecutive runs — genuine news cycle continuation, not noise, but monitor for diminishing differentiation. Google News Radar's 'tea heart health' trending query has no traceable article — held at Skill 02b. 'health care costs' cluster promoted to P2 due to rare 5-source convergence."
```

---

## 4. Skill 02b Routing Summary

| Topic | Risk Type | Gate Result | Primary Source | Notes |
|---|---|---|---|---|
| Weight-loss surgery diabetes remission (OU) | study_or_research | **Pass** | trusted_secondary (university press release naming long-term study) | Confidence capped at Low/Medium pending journal/DOI confirmation |
| Colorectal cancer immune-evasion study (USF/TGH) | study_or_research | **Pass** | trusted_secondary (university press release) | Same caveat — confirm peer-reviewed publication before citing mechanism claims |
| Average human genome / genetic disease risk study | study_or_research | **Pass** (gate) → **routed to Monitor at Skill 04** | trusted_secondary (News-Medical, single source) | Claim matches but trend_strength (48) fell below the 50 threshold; not a 02b rejection |
| "Tea heart health" daily-tea study (Trends rising query) | study_or_research | **Reject** | None found | No traceable primary source or news article — rejection_reason: `unverifiable_health_claim` |
| Ebola outbreak case count | n/a | **Not applicable** | — | Breaking case-count reporting, not a treatment/drug/study claim |
| Medical debt / health care costs data | n/a | **Not applicable** | — | Survey/data release, not a clinical claim |

---

## 5. Final Editorial Priority Board

| Priority | Topic | Primary Entity | Signal Type | Category | Trend | Opp. | Discover | Urgency | Confidence | Status | Sources | Angle |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **P1** | DRC Ebola outbreak tops 10,000 cases | Ebola outbreak (DRC) | breaking_news | infectious disease | 82 | 68 | 4 | today | high | update | 3 | What crossing 10K cases means for containment + vaccine trial |
| **P2** | Bariatric surgery → lasting diabetes remission | OU long-term study | study_or_research | chronic disease mgmt | 58 | 64 | 4 | this_week | medium | new | 1 | Durability data vs. the GLP-1 news cycle |
| **P2** | Health care costs & medical debt squeeze | KFF/Commonwealth Fund/NYT/NPR data wave | data_release | public health (borderline) | 70 | 62 | 3 | today | high | new | 5 | 1-in-4 medical debt, even insured — patient-facing synthesis |
| **P3** | Colorectal cancer immune-evasion study | USF/Tampa General study | study_or_research | medical research | 52 | 60 | 3 | this_week | low | new | 1 | Overturning a decades-old cancer-immunity model, explained |
| **P5 (monitor)** | Average human genome / genetic disease risk study | News-Medical genome study | study_or_research | medical research | 48 | 54 | 2 | this_week | low | new | 1 | Below trend threshold; revisit if corroborated by a second outlet |

```yaml
summary:
  total_topics: 5
  high_priority_count: 1
  immediate_actions: "Publish Ebola case-count update today; begin bariatric-surgery and health-costs briefs for this week."
```

---

## 6. Editorial Briefs

### P1 — DRC Ebola Outbreak Tops 10,000 Cases
**Primary headline:** "DRC's Ebola Outbreak Tops 10,000 Cases — Here's What That Means for Containment"
**Alternates:** "Ebola Cases Cross 10,000 in Congo: What's Changed Since the Vaccine Trial Began" / "Inside the Numbers: Why the Congo Ebola Outbreak Just Hit a Grim Milestone"

- **Why now:** Case count crossed 10,000 per WHO/NBC News reporting, days after WHO began an Ebola vaccine clinical trial in DRC (covered 10/25) — this is a distinct new data point.
- **Outline:** Intro (milestone) → What's driving the surge → Where the new vaccine trial stands → What public health officials are watching next → FAQ (transmission risk to US, timeline).
- **Key data:** 10,000+ cases (WHO, via NBC News/Al Jazeera); vaccine trial launch context (WHO, 10/25).
- **Sources:**
  - { publisher: "Al Jazeera", url: "https://www.aljazeera.com/news/2026/10/24/who-announces-start-of-ebola-vaccine-clinical-trial-in-dr-congo", tier: 1, used_for: "Vaccine trial + outbreak context" }
  - { publisher: "WHO", url: "https://www.who.int", tier: 1, used_for: "Official case data — [URL unverified, confirm situation report before publishing]" }
- **Integrity flags:** ⚠️ Confirm exact case count directly from WHO situation report — do not rely solely on secondary aggregation.
- **Expert source:** WHO/CDC infectious disease spokesperson (cite existing statements from vaccine-trial coverage).
- **SEO:** primary keyword "Ebola outbreak Congo 2026"; supporting: "Ebola vaccine trial," "Ebola case count." Format: news explainer. ~900 words.
- **Discover notes:** Named entity + traceable WHO primary source + timely — discover_score 4.

### P2 — Bariatric Surgery & Long-Term Diabetes Remission
**Primary headline:** "Weight-Loss Surgery Still Beats Drugs for Long-Term Diabetes Remission, New Study Finds"
**Alternates:** "The GLP-1 Era's Quiet Competitor: What a New Long-Term Study Says About Bariatric Surgery" / "Does Weight-Loss Surgery Actually Cure Diabetes? A New Long-Term Study Weighs In"

- **Why now:** New OU long-term follow-up study published this week, offering a durability contrast to this week's GLP-1 recall headlines.
- **Outline:** Intro → Study findings & remission rates → How it compares to GLP-1 drugs → Who's a candidate → FAQ.
- **Sources:** { publisher: "University of Oklahoma", url: "http://ou.edu/content/news/articles/2026/october/weight-loss-surgery-lasting-diabetes-remission-long-term-study", tier: 2, used_for: "Primary study summary" } — ⚠️ journal/DOI not yet confirmed, locate before publishing.
- **Integrity flags:** ⚠️ Clarify study design (long-term cohort vs. RCT) before reporting remission rates as causal. ⚠️ Single-source — corroborate with a second outlet.
- **Expert source needed:** Bariatric surgeon or endocrinologist (type: moderate authority need).
- **SEO:** primary keyword "weight loss surgery diabetes remission"; format: data-led explainer. ~1,100 words.

### P2 — Health Care Costs & Medical Debt Squeeze
**Primary headline:** "Medical Debt Now Hits 1 in 4 Americans — Even With Insurance. Here's Why."
**Alternates:** "The Hidden Health Cost Crisis: What New KFF and Commonwealth Fund Data Reveal" / "Why Having Health Insurance No Longer Protects You From Medical Debt"

- **Why now:** Convergent data release this week from KFF, Commonwealth Fund, Peterson-KFF, NYT, and NPR all document the same affordability crisis.
- **Outline:** Intro (1-in-4 stat) → Why insured people still go into debt → Employer cost-shifting trend → What this means for care-seeking behavior → FAQ.
- **Sources:**
  - { publisher: "Ohio Capital Journal / KFF", url: "https://ohiocapitaljournal.com/2026/10/27/medical-debt-hit-1-in-4-americans-and-1-in-5-ohioans-last-year-even-the-insured-study-shows/", tier: 2, used_for: "Medical debt stat" }
  - { publisher: "NYT", url: "https://www.nytimes.com/2026/10/22/business/health-insurance-costs-workers-premiums-deductibles.html", tier: 1, used_for: "Employer cost-shift data" }
  - { publisher: "NPR", url: "https://www.npr.org/2026/10/22/nx-s1-6008153/health-insurance-costs-kff-commonwealth", tier: 1, used_for: "Worker cost burden" }
  - { publisher: "Commonwealth Fund", url: "https://www.commonwealthfund.org/publications/surveys/2026/oct/state-health-insurance-coverage-2026-biennial-survey", tier: 1, used_for: "Coverage survey data" }
- **Integrity flags:** ⚠️ Borderline category — keep framing patient-facing (how this affects health decisions), not policy-wonk, to stay within site scope.
- **SEO:** primary keyword "medical debt insured Americans 2026"; format: data synthesis explainer. ~1,000 words.

### P3 — Colorectal Cancer Immune-Evasion Study (Concise Brief)
**Headline:** "Scientists Just Overturned a Decades-Old Theory About How Colorectal Cancer Hides From the Immune System"
- **Angle:** Plain-language explainer on how metastatic colorectal cancer's immune evasion may originate outside the tumor cell, challenging a long-held model.
- **Key data:** USF Health/Tampa General Hospital study findings (single source).
- **Integrity flags:** ⚠️ Confirm whether findings come from human tissue/trial vs. preclinical model before implying clinical applicability.
- **Expert type needed:** Oncologist/immunologist.
- **SEO:** primary keyword "colorectal cancer immune system study"; format: explainer; SERP difficulty: Medium.
- **Sources:** { publisher: "USF Health", url: "https://www.usf.edu/health/news/2026/usf-health-tampa-general-study-finds-metastatic-colorectal-cancers-immune-defenses-may-begin-outside-the-cancer-cell.aspx" }
- **Est. word count:** 600–700

---

## 7. Rejected Topics Log

| Topic | Reason |
|---|---|
| Toothpaste recall (Brush Buddies) | `existing` — covered 10/23, no new development |
| GLP-1 (tirzepatide) sterility recall | `existing` — covered 10/23 |
| PTSD treatment 68% remission trial | `existing` — covered 10/26 |
| Ebola vaccine trial launch | `existing` — covered 10/25 (case-count milestone retained separately as update) |
| NIH T-cell therapy cancer trial | `existing` — covered 10/24 |
| Yale amino acid / age-related inflammation | `existing` — covered 10/26 |
| Penn Medicine personality genetics study | `existing` — covered 10/26 |
| "Tea heart health" daily-tea study | `unverified_claim` — no traceable primary source (Skill 02b reject) |
| Jennifer Shuford CDC resignation | `brand_safety` — political personnel controversy |
| Missouri AG vs. Eli Lilly drug pricing | `off_category` — pharma/political-legal dispute, no research angle |
| HHS HTI-5 deregulatory rule | `off_category` — health IT policy, low audience relevance |
| Calley Means wellness-stake conflict story | `brand_safety` — political conflict-of-interest story |
| VCU NIH heart failure grant | `weak_signal` — grant announcement only, no results yet (monitor) |
| Pulmonary artery denervation trial enrollment | `weak_signal` — first-patient enrollment, niche device, no results (monitor) |
| HIV newborn dosing regimen trial | `weak_signal` — narrow audience fit, opportunity score below threshold |
| Wellness darties / wellness fairs / Granada Theater sale | `off_category` — local/lifestyle fluff, no evidence base |
| Trisha Yearwood / John Goodman weight loss | `off_category` — celebrity wellness, no evidence base |
| Gut health generic queries (leaky gut, ACV, Vitamin Shoppe) | `weak_signal` — generic evergreen chatter, no fresh angle |
| Food safety trending queries | `other` — contaminated by unrelated test-prep content, not a real signal |
| Mental health trending related queries | `other` — spam-site contamination (villakalima.com, etc.), not usable |

---

## 8. Integrity Flags (Consolidated)

- ⚠️ **Ebola outbreak:** Confirm exact case count against WHO's official situation report before publishing — do not rely solely on secondary aggregation.
- ⚠️ **Bariatric surgery study:** Single-source (OU press release) — locate underlying peer-reviewed journal/DOI; clarify cohort/long-term follow-up design vs. RCT before reporting remission rates.
- ⚠️ **Colorectal cancer study:** Single-source (USF press release) — confirm whether findings are from human tissue/trial or preclinical model before implying clinical relevance.
- ⚠️ **Health care costs/medical debt:** Borderline category fit — keep framing patient-facing, not policy analysis, to stay within site scope.
- ⚠️ **"Tea and heart health" rising query:** No traceable source found — do not publish until a primary study or credible outlet surfaces.

---

## 9. Run Notes

- Google Trends and Google News Radar both available via injected pre-fetch; no tool outages this run.
- `site_url` not configured — self-check skipped; competitor-list fallback used for duplicate/SERP-gap context on all retained candidates.
- Recurring-theme watch: GLP-1/weight-loss and cancer-immunotherapy/recall topics have appeared in 3+ consecutive runs (10/23–10/26) — genuine ongoing news cycles, not stale repetition, but diversify angle selection if they recur again tomorrow unchanged.
- `data/deferred_topics.yaml`: no entries due for recheck today.
- `data/run_history.yaml`: updated with today's entry (4 retained, 1 monitored, 140 rejected; P1 count 1, P2 count 2, P3 count 1).
- Dashboard output: `outputs/daily_newsroom_dashboard/2026-10-27.html` (pending publish step).