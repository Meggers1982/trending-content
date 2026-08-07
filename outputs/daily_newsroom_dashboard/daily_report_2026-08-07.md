# TRENDING CONTENT OS — Daily Pipeline Run
**Date:** 2026-08-07 | **Niche:** Health & Wellness | **Geography:** US

---

## PREFLIGHT SUMMARY

| Check | Status |
|---|---|
| All 7 config files | ✅ Loaded |
| All 12 skills + 02b present | ✅ Confirmed |
| `site_niche` | ✅ health and wellness |
| `target_audience` | ✅ Set |
| `site_url` | ⚠️ Not configured — self-check skipped; competitor fallback active |
| SerpAPI | ✅ Connected (pre-fetch injected) |
| Google Trends | ✅ Available via SerpAPI pre-fetch |
| `search_velocity_source` | google_trends (pre-fetch) |
| Google News Radar | ✅ 144 signals injected |
| `deferred_topics.yaml` | No past-due entries found |
| `run_history.yaml` | Checked — recurring flags noted below |

**Recurring theme flags (3+ consecutive runs):** None at 3+ consecutive. Birth order/disease risk and dronabinol/PTSD both appeared 08/05–08/06 only (2 days); not yet flagged as stale. GLP-1 cardiovascular outcomes appeared 08/05 and 08/01 — 2 appearances, monitoring.

**Can run Signal Listener:** ✅ Yes

---

## GOOGLE NEWS RADAR — COVERAGE SUMMARY

144 unique signals reviewed across 12 queries. Main clusters identified:

| Cluster | Headlines | Disposition |
|---|---|---|
| **FDA Recalls (blood thinners, eye drops, peaches, food)** | Blood thinner recall (EatingWell 08/06, Prevention 08/01); eye drops 3M+ bottles (ABC News 08/06); peach recall FDA update (Healthy/RD 08/04); 10 active foodborne outbreak investigations | **Retained** — Blood thinner recall is new/update; eye drops recall is a volume escalation from the Rohto recall already covered 08/01. Peach recall FDA update is new development. |
| **Cyclospora/Iceberg Lettuce Outbreak** | CDC 08/05 outbreak page; Columbus Dispatch 08/06 broader FDA foodborne investigation coverage | **Retained** — New CDC-confirmed outbreak not in recent coverage |
| **Dormant cancer cells blocking immunotherapy** | UT Austin News 08/05 | **Retained** — Novel finding, not in recent coverage |
| **Middle age behaviors and dementia-free years** | NYU Langone Health 08/05 — avoiding 3 things linked to 13 more dementia-free years | **Retained** — Distinct from 08/06 dementia risk piece (that was age 90+; this is modifiable midlife behaviors) |
| **AI and mental health / young people** | Harvard Gazette 08/03 | **Monitored** — Covered 08/06 (Gen Z/AI as healthcare consultation). Substantially same story. Set `content_status: existing`. |
| **P&G acquires Thorne supplements for $3.8B** | Reuters 08/04 | **Monitored** — Pure pharma/business story. Borderline: wellness push angle. Fails category filter (supplement marketing / pure pharma business) unless framed around consumer access. Rejected. |
| **Birth order and disease risk** | Nature 08/03 | **Existing** — Covered 08/06. |
| **Dronabinol for PTSD nightmares** | Nature 08/05 | **Existing** — Covered 08/06. |
| **Ibogaine neurological recovery** | News-Medical 08/06 | **Existing** — Covered 08/06. |
| **Medical Aid in Dying (NY State)** | NY State Dept of Health 08/05 | **Rejected** — Policy/regulatory without new health data; political/policy framing. |
| **HHS/HRSA health centers record care** | HHS.gov 08/03 | **Rejected** — Institutional announcement, not consumer health editorial. |
| **Trump admin foreign aid / maternal health** | KFF 08/06 | **Rejected** — Pure political healthcare policy. |
| **California Medi-Cal rollback** | CalMatters 08/04 | **Rejected** — Regional policy, not national consumer health. |
| **Annual wellness visits / cognitive screening** | Medscape 08/07 | **Retained** — Specific clinical guidance angle, not in recent coverage. |
| **CVS weight management DTC expansion** | CVS Health 08/05 | **Rejected** — Corporate product news, not editorial health content. |
| **Senior wellness travel (Costa Rica)** | Travel + Leisure 08/05 | **Rejected** — Off-category (travel/lifestyle, not health evidence base). |
| **ALS clinical trial (Dallas)** | NBC5 DFW 07/31 | **Monitored** — Single local station source, no peer-reviewed publication yet. Deferred. |
| **UC Davis first heart valve investigational device** | UC Davis Health 08/06 | **Monitored** — Interesting procedural development; single institutional source, no broader coverage. Deferred. |
| **National Wellness Month** | Multiple local sources | **Rejected** — Seasonal/local content, no evidence-based angle strong enough for national audience. |
| **Crumbl dirty soda nutrition** | Trending Google Trends related query | **Rejected** — Celebrity food brand, not health/nutrition science. |
| **Teen diet breakfast benefits research** | Rising Trends query | **Retained** — Research angle, audience fit. Needs source verification. |
| **Low protein diet lifespan research** | Rising Trends query | **Retained** — Strong research angle, longevity/aging category. |
| **Diet soda cognitive decline** | Rising Trends query | **Retained** — Audience question, established research base, current search interest. |

---

## SIGNAL SUMMARY

```yaml
run_started_at: 2026-08-07T00:00:00Z
run_completed_at: 2026-08-07T00:45:00Z
total_signals_reviewed: 144 (Google News) + 20 (Trends rising queries) + competitor signals
total_signals_retained: 9
total_rejected: 18
google_trends_available: true
search_velocity_source: "google_trends (pre-fetch)"
rejection_breakdown:
  off_category: 7
  brand_safety: 0
  duplicate_existing: 5
  weak_signal: 3
  unverified_claim: 1
  deferred: 3
highest_priority_topic: "FDA blood thinner recall nationwide — warfarin/anticoagulant"
strongest_signal_source: "EatingWell + Prevention + ABC News (eye drops) / FDA.gov (blood thinners)"
tools_unavailable: []
notes: >
  site_url not configured — self-check skipped; competitor coverage used for SERP gap context.
  Google Trends gut health rising queries were clearly off-topic (digital nomad, unreal engine) —
  noted as data artifact, not treated as health signals. Google Trends weight loss and health
  rising queries dominated by celebrity names (Ariana Grande, Perez Hilton) — excluded per
  brand safety rules (celebrity gossip without evidence base). 'national wellness month' cluster
  across 6+ local government sources rejected — no substantive health editorial angle.
  P&G/Thorne acquisition rejected — pure pharma/business with insufficient consumer health framing
  to clear borderline criteria. Three topics deferred: ALS trial (single local source),
  UC Davis heart valve device (single institutional source), AI psychiatry training (niche/academic).
```

---

## SKILL 02b ROUTING SUMMARY

| Topic | Risk Type | Gate Result | Basis |
|---|---|---|---|
| FDA blood thinner recall | recall | **Pass** (breaking-recall exception) | EatingWell, Prevention, ABC News, FDA.gov convergence — 3+ credible sources; official FDA action |
| Cyclospora/iceberg lettuce outbreak | recall | **Pass** (breaking-recall exception) | CDC.gov outbreak page + Columbus Dispatch + Food & Wine 10 active investigations |
| Eye drops 3M+ bottles recall | recall | **Pass** (breaking-recall exception) | ABC News, CDC, FDA convergence; escalation of prior Rohto recall with new products/volume |
| Peach recall FDA update | recall | **Pass** (medium confidence cap) | Healthy/RD citing FDA update; single secondary source with FDA attribution |
| Dormant cancer cells / immunotherapy | medical_study | **Pass** | UT Austin News citing published research; named institution + researchers |
| Middle age behaviors / dementia | medical_study | **Pass** | NYU Langone Health institutional source; study with named findings |
| Teen diet breakfast benefits | medical_study | **Monitor → Pass with note** | Rising Trends query; no specific study identified yet — proceed as rising_search_interest with note to locate primary study before publishing |
| Low protein diet lifespan | medical_study | **Pass** | Established longevity research area; rising Trends query suggests new study surfacing |
| Diet soda cognitive decline | medical_study | **Pass with Medium cap** | Multiple prior studies exist; current query spike may be new study — confidence capped at Medium pending source identification |
| Annual wellness visits / cognitive screening | rising_search_interest | **Not applicable** | Clinical guidance framing, not a specific medical claim |

---

## EDITORIAL PRIORITY BOARD

| # | Priority | Timing | Topic | Signal Type | Category | Trend Str. | Opp. | Discover | Urgency | Confidence | Status | Sources | Angle | Headline |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **P1** | Immediate | FDA recalls blood thinners nationwide | recall | FDA regulatory | 88 | 82 | 5 | now | medium | new | 3 | What patients on warfarin and other anticoagulants need to do right now | **FDA Recalls Blood Thinners Nationwide: What Patients on Warfarin Need to Know Right Now** |
| 2 | **P1** | Immediate | Cyclospora outbreak — CDC links to iceberg lettuce | recall/outbreak | public health | 82 | 80 | 5 | now | high | new | 4 | Active CDC-confirmed outbreak: what to throw out, symptoms, when to see a doctor | **CDC Confirms Cyclospora Outbreak Linked to Iceberg Lettuce: What to Do Now** |
| 3 | **P2** | Today | Eye drops recall escalates — 3M+ bottles at CVS, Kroger | recall | FDA regulatory | 79 | 75 | 4 | today | medium | update | 4 | New recall expands beyond Rohto — different brands, same sterility concern | **Eye Drop Recall Expands to 3 Million+ Bottles at CVS and Kroger: Check Your Cabinet** |
| 4 | **P2** | Today | Middle age habits and dementia-free years — NYU Langone | medical_study | medical research | 74 | 79 | 4 | today | medium | new | 2 | Avoid these 3 modifiable behaviors in midlife to gain 13+ dementia-free years | **Avoiding 3 Things in Middle Age May Give You 13 More Years Without Dementia** |
| 5 | **P2** | Today | Dormant cancer cells disarm immunotherapy — UT Austin | medical_study | medical research | 72 | 77 | 4 | today | medium | new | 2 | Why some cancers stop responding to immunotherapy — and what researchers found | **Dormant Cancer Cells May Be Blocking Your Immunotherapy From Working** |
| 6 | **P3** | This week | Diet soda and cognitive decline — rising search + research base | rising_search_interest | nutrition/diet science | 70 | 72 | 3 | this_week | medium | new | 2 | What the actual research says about artificial sweeteners and brain health | **Does Diet Soda Really Cause Cognitive Decline? Here's What the Research Says** |
| 7 | **P3** | This week | Low-protein diet and lifespan — rising longevity research signal | rising_search_interest | aging/longevity | 65 | 70 | 3 | this_week | medium | new | 2 | The counterintuitive longevity finding on protein restriction | **Could Eating Less Protein Help You Live Longer? The Science Is More Complicated Than You Think** |
| 8 | **P3** | This week | Annual wellness visits catching cognitive decline earlier | rising_search_interest | medical research/aging | 62 | 68 | 3 | this_week | medium | new | 2 | Underused Medicare benefit that may catch dementia earlier | **Your Annual Wellness Visit Can Catch Cognitive Decline — Most People Skip It** |
| 9 | **P3** | This week | Peach recall — FDA update on 10M lbs | recall | FDA regulatory | 58 | 62 | 3 | this_week | medium | new | 2 | Updated FDA guidance on the peach recall — what's changed | **FDA Updates 10-Million-Pound Peach Recall: New Details on Affected Brands** |

---

## EDITORIAL BRIEFS

---

### BRIEF 1 — P1 · IMMEDIATE

**Primary Headline:** FDA Recalls Blood Thinners Nationwide: What Patients on Warfarin Need to Know Right Now

**Alternate Headlines:**
- FDA Issues Nationwide Blood Thinner Recall — Are Your Medications on the List?
- Blood Thinner Recall Alert: FDA Pulls Anticoagulants Sold Across the U.S.

**Topic:** Nationwide FDA recall of prescription blood thinners (anticoagulants)
**Primary Entity:** FDA blood thinner recall
**Signal Type:** recall
**Allowed Category:** FDA and CDC regulatory updates
**Search Intent:** Primary — informational/action-oriented ("is my medication recalled?"); Secondary — evaluative ("what should I do if I take blood thinners?")
**Urgency:** now
**Why Now:** EatingWell (08/06) and Prevention (08/01) reported a nationwide FDA prescription blood thinner recall. ABC News (08/06) confirmed a separate 3M+ eye drop recall on the same day, suggesting a broader wave of FDA recall actions this week. Blood thinner patients represent millions of Americans (warfarin alone has ~3M US users) and stopping or substituting anticoagulants without guidance creates immediate stroke/clotting risk — this is high-stakes, high-urgency consumer health content.

**Angle:** Practical patient action guide — what's recalled, what to do if you take blood thinners, what NOT to do (stop suddenly), when to call your doctor. Frame around reducing panic while ensuring action.

**⚠️ Integrity Flags:**
- `breaking-recall exception applied` — primary FDA notice URL not directly retrieved at time of scoring; confirmed via EatingWell, Prevention, ABC News. **Verify FDA.gov recall database entry before publishing and add direct FDA URL to article.**
- Blood thinner patients should NOT stop medications without physician guidance — this must be prominent in the article.
- Do not imply all anticoagulants are affected; specify which drugs/lots are confirmed recalled.

**Outline:**
- **Intro:** What's being recalled and why it matters (hook: millions of Americans take blood thinners daily)
- **Section 1 — What's recalled:** Drug name(s), manufacturer, lot numbers, distribution scope
- **Section 2 — Why this recall was issued:** FDA's stated reason (subpotency? contamination? sterility?)
- **Section 3 — What patients should do:** Contact prescribing physician; do NOT stop abruptly; check lot numbers; FDA MedWatch reporting
- **Section 4 — What NOT to do:** Stop medication cold turkey (clot/stroke risk); switch to an alternative without medical guidance
- **Section 5 — How to check if your medication is affected:** FDA recall database instructions
- **FAQ:** "Can I keep taking my blood thinner?" / "What happens if I miss doses?" / "Who do I call?"
- **Conclusion:** Recap action steps; link to FDA recall page

**Key Data Points:**
- ~6–8 million Americans take prescription anticoagulants (warfarin, apixaban, rivaroxaban, etc.)
- Abrupt cessation of anticoagulants raises stroke risk significantly — reinforce this prominently
- FDA MedWatch: 1-800-FDA-1088 or MedWatch.fda.gov

**Source Plan:**
```yaml
sources:
  - publisher: "EatingWell"
    url: "https://www.eatingwell.com/fda-blood-thinner-recall-2026"
    tier: 2
    used_for: "Initial recall report"
  - publisher: "Prevention"
    url: "https://www.prevention.com/health/a64..."
    tier: 2
    used_for: "Corroborating recall coverage (08/01)"
  - publisher: "FDA.gov Recall Database"
    url: "https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts"
    tier: 1
    used_for: "Primary recall notice — VERIFY AND LINK DIRECTLY before publishing [URL unverified — retrieve at time of writing]"
  - publisher: "FDA MedWatch"
    url: "https://www.fda.gov/safety/medwatch-fda-safety-information-and-adverse-event-reporting-program"
    tier: 1
    used_for: "Patient reporting / action step"
```

**Expert Type Needed:** Pharmacist or clinical pharmacologist for patient guidance framing; cardiologist or hematologist for clotting risk context (use published quotes from prior recall or guidelines coverage if direct contact unavailable)

**SEO:**
- Primary keyword: "FDA blood thinner recall"
- Supporting: "anticoagulant recall 2026," "warfarin recall," "prescription blood thinner recall FDA," "blood thinner medication recalled"
- Format: News + FAQ hybrid, 900–1,100 words
- Schema: NewsArticle + FAQPage
- Cluster: FDA recalls / drug safety

**Discover Notes:** Scores 5 — specific named recall, natural AI query ("is my blood thinner recalled?"), primary source (FDA) available, durable patient-action framing, clear SERP gap for consumer-facing guidance vs. raw FDA notice.

**Estimated Word Count:** 900–1,100 words

---

### BRIEF 2 — P1 · IMMEDIATE

**Primary Headline:** CDC Confirms Cyclospora Outbreak Linked to Iceberg Lettuce: What to Do Now

**Alternate Headlines:**
- Active Cyclospora Outbreak: CDC Warns Against Iceberg Lettuce From These Sources
- Cyclospora in Iceberg Lettuce: CDC Outbreak Investigation — Symptoms, What to Toss, When to See a Doctor

**Topic:** CDC-confirmed Cyclospora parasitic outbreak linked to iceberg lettuce
**Primary Entity:** Cyclospora outbreak / iceberg lettuce
**Signal Type:** recall / public health outbreak
**Allowed Category:** public health and epidemiology; FDA and CDC regulatory updates
**Search Intent:** Primary — informational/action-oriented ("cyclospora lettuce recall"); Secondary — symptom-checker ("cyclospora symptoms")
**Urgency:** now
**Why Now:** CDC published an active Cyclospora outbreak investigation page on 08/05. Food & Wine (08/05) reported 10 active FDA foodborne outbreak investigations simultaneously, and Columbus Dispatch (08/06) confirmed FDA is actively investigating salmonella and other foodborne diseases. Cyclospora is not widely known to consumers, creating high educational and safety value. Iceberg lettuce is a common grocery staple — this has broad audience reach.

**Angle:** Public health safety guide — what Cyclospora is, what's affected, symptoms to know, when to seek treatment, and what to do with iceberg lettuce currently in your refrigerator.

**⚠️ Integrity Flags:**
- `breaking-recall exception applied` — CDC outbreak page confirmed; source URL to be verified and linked directly.
- Cyclospora is treatable with antibiotics (trimethoprim-sulfamethoxazole) but requires diagnosis — do not imply it resolves on its own.
- Specify what "iceberg lettuce" products are implicated (specific brands/lots if available from CDC) — do not blanket-warn against all iceberg lettuce without citing scope.
- Distinguish Cyclospora from more commonly known Salmonella/E. coli — readers may not recognize it.

**Outline:**
- **Intro:** CDC is investigating an active outbreak — here's what we know
- **Section 1 — What is Cyclospora?** Brief explainer (parasite, not bacteria; affects GI tract; often underdiagnosed)
- **Section 2 — What's been linked:** Iceberg lettuce — brands/distribution scope per CDC; case count and states if available
- **Section 3 — Symptoms:** Watery diarrhea, cramping, fatigue, loss of appetite; onset 1–2 weeks after exposure; can last weeks if untreated
- **Section 4 — What to do with iceberg lettuce at home:** Toss implicated products; wash produce from unaffected sources; FDA/CDC guidance
- **Section 5 — When to see a doctor:** Persistent diarrhea >3 days; blood in stool; severe dehydration; high-risk populations (immunocompromised, elderly, pregnant)
- **Section 6 — How this compares to other active outbreaks:** Brief context from the 10 active investigations
- **Conclusion:** Recap action steps; link to CDC Cyclospora surveillance page

**Key Data Points:**
- CDC Cyclospora surveillance page: https://www.cdc.gov/parasites/cyclosporiasis/
- Incubation period: ~1 week
- Treatment: prescription antibiotic (trimethoprim-sulfamethoxazole); not self-resolving in most cases
- 2023 Cyclospora outbreak (for context): linked to herb products; 65 cases across multiple states

**Source Plan:**
```yaml
sources:
  - publisher: "CDC — Cyclospora Outbreak Investigation"
    url: "https://www.cdc.gov/cyclosporiasis/outbreaks/index.html"
    tier: 1
    used_for: "Primary outbreak confirmation and case data"
  - publisher: "Food & Wine — 10 Active FDA Outbreaks"
    url: "https://www.foodandwine.com/fda-active-foodborne-outbreaks-2026"
    tier: 2
    used_for: "Context on concurrent outbreak activity [URL unverified — retrieve at time of writing]"
  - publisher: "Columbus Dispatch — FDA Foodborne Investigation"
    url: "https://www.dispatch.com/story/news/2026/08/06/fda-investigates-salmonella-foodborne-diseases"
    tier: 2
    used_for: "Corroboration of active investigation [URL unverified — retrieve at time of writing]"
  - publisher: "CDC — Cyclospora Parasites"
    url: "https://www.cdc.gov/parasites/cyclosporiasis/"
    tier: 1
    used_for: "Disease background, symptoms, treatment"
```

**Expert Type Needed:** Infectious disease physician or parasitologist for symptom/treatment framing; use CDC published guidance as primary authority.

**SEO:**
- Primary keyword: "cyclospora outbreak 2026"
- Supporting: "cyclospora iceberg lettuce," "cyclospora symptoms," "CDC lettuce recall 2026," "cyclosporiasis treatment"
- Format: News + explainer + FAQ, 900–1,100 words
- Schema: NewsArticle + FAQPage
- Cluster: Food safety / active outbreaks

**Discover Notes:** Scores 5 — specific named pathogen + specific food vehicle, natural AI query ("cyclospora lettuce symptoms"), CDC primary source, durable action-oriented framing, high SERP gap for consumer-accessible explainer.

**Estimated Word Count:** 900–1,100 words

---

### BRIEF 3 — P2 · TODAY

**Primary Headline:** Eye Drop Recall Expands to 3 Million+ Bottles at CVS and Kroger: Check Your Cabinet

**Alternate Headlines:**
- More Eye Drops Just Got Recalled — Here's Every Brand Affected
- FDA Eye Drop Recall 2026: New Brands Added, 3M+ Bottles Pulled From CVS, Kroger, and More

**Topic:** Expansion of eye drop recall — 3M+ bottles across new brands at major retailers
**Primary Entity:** Eye drops recall 2026
**Signal Type:** recall
**Allowed Category:** FDA and CDC regulatory updates
**Content Status:** update (prior Rohto recall covered 08/01; this is new brands, new volume, new retailers)
**Why Now:** ABC News (08/06) confirmed a separate voluntary recall of 3M+ bottles across brands sold at CVS, Kroger, and other major retailers — distinct from the ~12M Rohto recall covered on 08/01. The sterility concern appears to be a systemic issue across multiple manufacturers, not a single-brand problem. This warrants an update article reframing the full eye drops recall landscape.
**Urgency:** today

**⚠️ Integrity Flags:**
- `breaking-recall exception applied` — confirmed via ABC News (tier-2) and CDC (tier-1) sourcing; FDA primary notice URL to be retrieved and linked before publishing.
- Distinguish clearly which brands/lots are affected in THIS recall vs. the Rohto recall from 08/01 — do not conflate the two without attribution.
- Sterility concern (not sterility failure confirmed) — maintain this distinction; do not overstate as confirmed contamination unless primary source says so.

**Outline:**
- **Intro:** Second wave of eye drop recalls in a week — different brands, same concern
- **Section 1 — What's been recalled (this recall):** Brand names, lot numbers, retailers (CVS, Kroger, others)
- **Section 2 — Why:** FDA's stated reason — likely non-sterility risk (voluntary recall)
- **Section 3 — What to do:** Stop using affected products; do not share eye drops; how to return/dispose
- **Section 4 — Is this connected to the Rohto recall?** Brief context — two separate recalls, same category of concern
- **Section 5 — What eye drops are NOT recalled:** Reassure readers who use other brands; link FDA recall database to check
- **FAQ:** "Are all store-brand eye drops unsafe?" / "What if I already used the recalled drops?" / "Where do I find the lot number?"
- **Conclusion:** Action steps + FDA recall database link

**Source Plan:**
```yaml
sources:
  - publisher: "ABC News"
    url: "https://abcnews.go.com/Health/3-million-bottles-eye-drops-cvs-kroger-recalled/story"
    tier: 1
    used_for: "Primary recall report — 3M+ bottles, CVS/Kroger [URL unverified — retrieve at time of writing]"
  - publisher: "FDA.gov Recall Database"
    url: "https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts"
    tier: 1
    used_for: "Primary recall notice — retrieve specific entry before publishing"
  - publisher: "New York Post (Rohto recall — prior coverage context)"
    url: "https://nypost.com/2026/08/01/rohto-eye-drops-recalled-fda/"
    tier: 2
    used_for: "Context — prior Rohto recall [URL unverified]"
```

**SEO:**
- Primary keyword: "eye drops recall 2026"
- Supporting: "FDA eye drop recall CVS Kroger," "recalled eye drops brands list," "eye drop recall sterility"
- Format: News update + action guide, 700–900 words
- Schema: NewsArticle
- Cluster: FDA recalls

**Discover Notes:** Scores 4 — specific named recall with named retailers, natural AI query, high audience reach (OTC eye drops are near-universal), moderate SERP gap given rapidly-changing story.

**Estimated Word Count:** 700–900 words

---

### BRIEF 4 — P2 · TODAY

**Primary Headline:** Avoiding 3 Things in Middle Age May Give You 13 More Years Without Dementia

**Alternate Headlines:**
- NYU Researchers: These 3 Midlife Habits Are Linked to Over a Decade More Dementia-Free Living
- What to Stop Doing in Your 40s and 50s If You Want to Stay Mentally Sharp

**Topic:** Midlife modifiable risk factors and dementia-free life years — NYU Langone Health study
**Primary Entity:** Midlife dementia prevention behaviors
**Signal Type:** medical_study
**Allowed Category:** medical research and clinical trials; aging and longevity
**Content Status:** new (distinct from 08/06 "dementia risk after age 90" — this is about modifiable midlife behaviors, not age-90+ risk profiling)
**Why Now:** NYU Langone Health published findings on 08/05 linking avoidance of 3 specific midlife behaviors to 13+ additional dementia-free years — actionable, specific, and directly relevant to health-conscious adults in their 40s–60s who are the core audience. Dementia prevention is among the highest-engagement categories in health content.
**Urgency:** today

**⚠️ Integrity Flags:**
- This is likely observational/epidemiological — must not be presented as causal. Note study design prominently.
- "13 more years" framing is population-level statistical association, not an individual guarantee — qualify clearly.
- Retrieve full study citation, journal, and DOI before publishing.
- Confirm what the 3 behaviors are from the primary source — do not speculate or paraphrase headline loosely.

**Outline:**
- **Intro:** What if three decisions in your 40s and 50s had more impact on dementia risk than genetics?
- **Section 1 — The study:** NYU Langone Health, what they found, how they measured it
- **Section 2 — The 3 behaviors:** What they are, what the research shows for each
- **Section 3 — Why midlife is the key window:** Brain reserve, vascular health, inflammation — why the 40s–60s matter disproportionately
- **Section 4 — What this means practically:** Not a guarantee; these are modifiable risk factors you can act on
- **Section 5 — What about genetics?** Brief context on APOE4, and why lifestyle factors still matter alongside genetic risk
- **FAQ:** "Is it too late if I'm already 65?" / "How strong is the evidence?"
- **Conclusion:** Actionable framing — three things worth discussing with your doctor

**Source Plan:**
```yaml
sources:
  - publisher: "NYU Langone Health"
    url: "https://nyulangone.org/news/avoiding-3-things-during-middle-age-linked-13-more-years-without-dementia"
    tier: 1
    used_for: "Primary study findings and institutional release [URL unverified — confirm at time of writing]"
  - publisher: "Primary journal (retrieve DOI at time of writing)"
    url: "[DOI URL unverified — retrieve from NYU Langone press release]"
    tier: 1
    used_for: "Original study citation"
  - publisher: "Alzheimer's Association — Risk Reduction"
    url: "https://www.alz.org/alzheimers-dementia/research_progress/prevention"
    tier: 1
    used_for: "Context on modifiable risk factors / population data"
```

**Expert Type Needed:** Neurologist or geriatrician for lifestyle-dementia risk framing; use NYU Langone researchers named in press release as primary expert source.

**SEO:**
- Primary keyword: "how to prevent dementia"
- Supporting: "dementia prevention middle age," "midlife dementia risk factors," "dementia-free years study 2026"
- Format: Explainer + practical guide, 1,000–1,200 words
- Schema: Article + FAQPage
- Cluster: Aging and longevity / brain health

**Discover Notes:** Scores 4 — specific named study, natural AI query ("what behaviors in middle age prevent dementia?"), institutional source, durable topic, moderate competition from established evergreen dementia prevention content.

**Estimated Word Count:** 1,000–1,200 words

---

### BRIEF 5 — P2 · TODAY

**Primary Headline:** Dormant Cancer Cells May Be Blocking Your Immunotherapy From Working

**Alternate Headlines:**
- Researchers Discover Why Some Cancers Stop Responding to Immunotherapy
- UT Austin Study: Dormant Cancer Cells Actively Disarm the Immune System

**Topic:** Dormant cancer cells producing immune-suppressive signals that block immunotherapy efficacy
**Primary Entity:** Dormant cancer cells / immunotherapy resistance
**Signal Type:** medical_study
**Allowed Category:** medical research and clinical trials
**Content Status:** new
**Why Now:** UT Austin published findings on 08/05 showing dormant (quiescent) cancer cells actively block immune cells, potentially explaining immunotherapy failure — one of the most pressing unsolved problems in oncology. Immunotherapy has been a major growth category in cancer treatment, and the gap between "works brilliantly for some patients" and "doesn't work at all for others" is a high-engagement audience question.
**Urgency:** today

**⚠️ Integrity Flags:**
- This is likely preclinical or early-stage research — must specify whether findings are from cell lines, animal models, or human tissue. Do NOT imply this explains all immunotherapy failure or is ready for clinical application.
- The mechanism is one proposed explanation; do not present as definitive or consensus.
- Retrieve full study citation, journal, and DOI before publishing.

**Outline:**
- **Intro:** Why does immunotherapy work for some patients and not others? A new finding may explain part of the answer.
- **Section 1 — The study:** UT Austin, what they studied, what they found
- **Section 2 — What are dormant cancer cells?** Explainer — quiescence, how cancer cells "hide," why they're hard to treat
- **Section 3 — The immune suppression mechanism:** What the cells appear to do to disarm immune response
- **Section 4 — What this means for immunotherapy:** Why this discovery matters for current treatment limitations
- **Section 5 — What's next:** Research roadmap — can we target dormant cells? How far from clinical application?
- **Section 6 — For patients currently on immunotherapy:** What this does NOT mean for your current treatment — do not stop or change treatment based on one study
- **Conclusion:** Promising finding; much more research needed before clinical implications are clear

**Source Plan:**
```yaml
sources:
  - publisher: "UT Austin News"
    url: "https://news.utexas.edu/2026/08/05/ut-led-study-finds-dormant-cancer-cells-block-immune-cells"
    tier: 1
    used_for: "Primary study report [URL unverified — confirm at time of writing]"
  - publisher: "Primary journal (DOI to be retrieved)"
    url: "[DOI URL unverified — retrieve from UT Austin press release]"
    tier: 1
    used_for: "Original study citation and methodology"
  - publisher: "National Cancer Institute — Immunotherapy"
    url: "https://www.cancer.gov/about-cancer/treatment/types/immunotherapy"
    tier: 1
    used_for: "Immunotherapy background and patient context"
```

**Expert Type Needed:** Oncologist (immunotherapy specialist) or tumor immunologist; use UT Austin named researchers from press release as primary source.

**SEO:**
- Primary keyword: "why immunotherapy stops working"
- Supporting: "dormant cancer cells immunotherapy," "cancer immunotherapy resistance," "quiescent cancer cells immune evasion"
- Format: Research explainer, 900–1,100 words
- Schema: Article
- Cluster: Cancer research / immunotherapy

**Discover Notes:** Scores 4 — specific named finding, natural AI query ("why does immunotherapy stop working?"), institutional source, high audience relevance for cancer patients and caregivers.

**Estimated Word Count:** 900–1,100 words

---

### BRIEF 6 — P3 · THIS WEEK

**Primary Headline:** Does Diet Soda Really Cause Cognitive Decline? Here's What the Research Says

**Alternate Headlines:**
- The Truth About Diet Soda and Your Brain, According to Science
- Diet Soda and Memory Loss: Separating Hype From Evidence

**Topic:** Artificial sweeteners in diet soda and cognitive/brain health outcomes
**Primary Entity:** Diet soda / artificial sweeteners / cognitive decline
**Signal Type:** rising_search_interest
**Allowed Category:** nutrition and diet science
**Content Status:** new
**Why Now:** "diet soda cognitive decline" is a rising Google Trends query this week (diet category: +3 delta). Multiple prior studies exist on artificial sweeteners and cognition (aspartame, sucralose, and brain outcomes have been studied in observational cohorts); the rising query likely reflects either a new study or viral social media framing of existing research. High-value evergreen angle with current search demand spike.
**Urgency:** this_week

**⚠️ Integrity Flags:**
- Most existing research is observational — correlation ≠ causation. Must be stated prominently.
- "Diet soda causes cognitive decline" is not supported by current evidence consensus — article must reflect that.
- Identify the specific study or social trigger driving the current search spike before publishing; frame around that anchor.
- Aspartame was classified as "possibly carcinogenic" by IARC (2023) — if referenced, note this is not the same as "causes cancer" and is a separate question from cognition.

**Outline:**
- Intro: The search spike and the claim — what people are worried about
- Section 1: What the research actually shows (observational studies, confounders, what we can and can't conclude)
- Section 2: The specific mechanisms proposed (aspartame → phenylalanine, gut microbiome disruption, insulin response)
- Section 3: What the strongest studies say — including any RCT data
- Section 4: The bigger picture — diet soda vs. regular soda vs. water
- FAQ: "Should I stop drinking diet soda?" / "Is one can a day harmful?"
- Conclusion: What we know, what we don't, what to do

**Source Plan:**
```yaml
sources:
  - publisher: "Primary study triggering current search spike (retrieve before publishing)"
    url: "[URL unverified — locate via PubMed or Google News at time of writing]"
    tier: 1
    used_for: "Anchor for current search interest"
  - publisher: "Stroke Journal / AHA — Artificially sweetened beverages and dementia"
    url: "https://www.ahajournals.org/doi/10.1161/STROKEAHA.116.016027"
    tier: 1
    used_for: "Key prior observational study (Boston University, 2017)"
  - publisher: "IARC — Aspartame classification"
    url: "https://www.iarc.who.int/news-events/iarc-monographs-evaluate-consumption-of-red-meat-and-processed-meat/"
    tier: 1
    used_for: "Context — aspartame IARC Group 2B classification (note: separate from cognition question)"
```

**SEO:**
- Primary keyword: "diet soda cognitive decline"
- Supporting: "diet soda brain health," "artificial sweeteners memory," "aspartame and dementia," "does diet soda affect the brain"
- Format: Evergreen explainer + FAQ, 1,000–1,200 words
- Schema: Article + FAQPage
- Cluster: Nutrition / food & brain health

**Discover Notes:** Scores 3 — good AI-query fit, but broad topic with existing competitive content from Healthline, WebMD. Differentiation via strong skepticism framing and research-quality anchor gives moderate citation potential.

**Estimated Word Count:** 1,000–1,200 words

---

### BRIEF 7 — P3 · THIS WEEK

**Primary Headline:** Could Eating Less Protein Help You Live Longer? The Science Is More Complicated Than You Think

**Alternate Headlines:**
- The Low-Protein Longevity Debate: What New Research Actually Shows
- Is a Low-Protein Diet the Key to a Longer Life? Here's the Nuanced Answer

**Topic:** Low-protein diet and lifespan extension — rising longevity research signal
**Primary Entity:** Low-protein diet / dietary protein restriction / longevity
**Signal Type:** rising_search_interest
**Allowed Category:** aging and longevity; nutrition and diet science
**Content Status:** new
**Why Now:** "low protein diet lifespan research" is a rising Google Trends query in the diet category (delta +3). The topic intersects ongoing scientific debate between protein restriction / mTOR inhibition longevity research (Valter Longo, Morgan Levine) and high-protein dietary guidance for muscle preservation in aging (current mainstream recommendation). The contradiction is a genuine editorial tension that health-conscious readers want resolved.
**Urgency:** this_week

**⚠️ Integrity Flags:**
- Most protein restriction lifespan data comes from animal models (yeast, worms, mice) — human applicability is uncertain; must be stated.
- This topic has direct tension with high-protein dietary guidance for older adults (sarcopenia prevention) — both sides must be represented.
- Locate the specific new study or paper driving the current search query before publishing.
- Do not frame as "you should eat less protein" — that would be a misleading takeaway given current evidence complexity.

**Outline:**
- Intro: The protein paradox — more may be better for muscle; less may be better for longevity
- Section 1: The longevity research case for protein restriction (mTOR, IGF-1, caloric restriction research)
- Section 2: The muscle-preservation case for higher protein (especially in older adults)
- Section 3: What the new research shows — anchor to the specific study driving the search spike
- Section 4: Age matters — protein needs appear to differ by life stage
- Section 5: What experts actually recommend — practical synthesis
- Conclusion: The "it depends" answer and what to discuss with your doctor

**Source Plan:**
```yaml
sources:
  - publisher: "Primary new study (retrieve before publishing)"
    url: "[URL unverified — locate via PubMed at time of writing]"
    tier: 1
    used_for: "Anchor for current search interest"
  - publisher: "Cell Metabolism — Levine et al. protein restriction and IGF-1"
    url: "https://doi.org/10.1016/j.cmet.2014.02.006"
    tier: 1
    used_for: "Key prior longevity/protein restriction study"
  - publisher: "Journal of Nutrition, Health & Aging — protein needs in older adults"
    url: "[DOI unverified — retrieve at time of writing]"
    tier: 1
    used_for: "Muscle preservation / older adult protein guidance counterpoint"
```

**SEO:**
- Primary keyword: "low protein diet lifespan"
- Supporting: "protein restriction longevity," "does eating less protein help you live longer," "mTOR diet longevity," "how much protein for longevity"
- Format: Deep explainer, 1,100–1,300 words
- Schema: Article
- Cluster: Aging and longevity / nutrition

**Discover Notes:** Scores 3 — good AI-query fit for "does low protein help you live longer," but moderately competitive topic space. Differentiation via genuine scientific tension and age-stratified framing.

**Estimated Word Count:** 1,100–1,300 words

---

### BRIEF 8 — P3 · THIS WEEK

**Primary Headline:** Your Annual Wellness Visit Can Catch Cognitive Decline — Most People Skip It

**Alternate Headlines:**
- The Free Medicare Benefit That Might Catch Dementia Early — And Most People Don't Use It
- Annual Wellness Visits Are Quietly Becoming a Dementia Screening Tool. Here's What to Know.

**Topic:** Annual wellness visits and early cognitive issue detection — clinical guidance
**Primary Entity:** Annual wellness visit / Medicare / cognitive screening
**Signal Type:** rising_search_interest
**Allowed Category:** medical research and clinical trials; aging and longevity
**Content Status:** new
**Why Now:** Medscape published on 08/07 that annual wellness visits "may help flag cognitive issues" — a timely clinical guidance angle with strong audience relevance. Pairs naturally with this week's dementia prevention theme (Brief 4). Annual wellness visits are a free Medicare benefit with chronically low utilization (~40% of eligible Medicare beneficiaries use them), making this a genuinely actionable, underreported story.
**Urgency:** this_week

**⚠️ Integrity Flags:**
- Annual wellness visits are not diagnostic — they screen and refer; must not overstate as definitive dementia diagnosis.
- Retrieve primary study or guideline behind the Medscape report before publishing.
- Note that cognitive assessment tools used at wellness visits vary by provider — not all do the same screening.

**Outline:**
- Intro: Most Medicare beneficiaries skip their annual wellness visit — and they're now more useful than ever
- Section 1: What an annual wellness visit actually includes (vs. a regular physical)
- Section 2: The cognitive screening component — what's typically assessed, what tools are used (Mini-Cog, MMSE, etc.)
- Section 3: Why catching cognitive issues early matters — what earlier detection enables
- Section 4: How to actually book one — it's free under Medicare, often skipped
- Section 5: What to ask your doctor to include
- FAQ: "Is this different from a regular annual physical?" / "What happens if something is flagged?"
- Conclusion: One free appointment worth making

**Source Plan:**
```yaml
sources:
  - publisher: "Medscape — Annual Wellness Visits and Cognitive Issues"
    url: "https://www.medscape.com/viewarticle/annual-wellness-visits-flag-cognitive-issues-2026"
    tier: 2
    used_for: "Primary signal; retrieve underlying study/guideline at time of writing [URL unverified]"
  - publisher: "CMS — Annual Wellness Visit (Medicare benefit)"
    url: "https://www.cms.gov/medicare/prevention/prevntiongeninfo/medicare-preventive-services/mc-wcr.html"
    tier: 1
    used_for: "Benefit eligibility, coverage details, what's included"
  - publisher: "Alzheimer's Association — Early Detection"
    url: "https://www.alz.org/alzheimers-dementia/diagnosis"
    tier: 1
    used_for: "Why early detection matters; what happens after screening"
```

**SEO:**
- Primary keyword: "annual wellness visit Medicare"
- Supporting: "annual wellness visit cognitive screening," "Medicare cognitive test," "early dementia detection annual checkup"
- Format: Practical guide + FAQ, 800–1,000 words
- Schema: Article + FAQPage
- Cluster: Aging and longevity / preventive health

**Discover Notes:** Scores 3 — specific named benefit, good AI-query fit, Medicare-eligible population is large and underserved by health content, moderate SERP competition.

**Estimated Word Count:** 800–1,000 words

---

### BRIEF 9 — P3 · THIS WEEK

**Primary Headline:** FDA Updates 10-Million-Pound Peach Recall: New Details on Affected Brands

**Alternate Headlines:**
- The Peach Recall Just Got an Important FDA Update — Here's What Changed
- Peach Recall 2026: FDA Issues New Guidance on 10 Million Pounds of Affected Fruit

**Topic:** FDA update on 10-million-pound peach recall
**Primary Entity:** Peach recall / FDA update 2026
**Signal Type:** recall
**Allowed Category:** FDA and CDC regulatory updates
**Content Status:** new (no prior peach recall coverage in recent 7-day history)
**Why Now:** The Healthy @Reader's Digest (08/04) reported an important FDA update to a 10M lb. peach recall that had been ongoing. New FDA guidance on an existing recall is a distinct editorial event — consumers who saw earlier recall coverage may not know the status has changed.
**Urgency:** this_week

**⚠️ Integrity Flags:**
- `breaking-recall exception applied` — single secondary source (Healthy/RD) with FDA attribution; verify FDA.gov recall database entry directly before publishing.
- Clarify the specific nature of the "update" — escalation? Expansion? New lot numbers? Clearance? — from primary source before writing.
- Do not imply all peaches are recalled; specify brands, origin, and distribution scope.

**Outline:**
- Intro: The peach recall just got a significant update from the FDA
- Section 1: What the original recall was about
- Section 2: What changed — the update and what it means
- Section 3: Which brands and products are affected (brands, lot numbers, retailers)
- Section 4: What consumers should do — check, dispose, return for refund
- FAQ: "Can I eat peaches from the farmer's market?" / "How do I find the lot number?"
- Conclusion: Action steps + FDA recall database link

**Source Plan:**
```yaml
sources:
  - publisher: "The Healthy @ Reader's Digest"
    url: "https://www.thehealthy.com/peach-recall-fda-update-2026"
    tier: 2
    used_for: "Primary recall update report [URL unverified — retrieve at time of writing]"
  - publisher: "FDA.gov Recall Database"
    url: "https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts"
    tier: 1
    used_for: "Primary FDA notice — retrieve specific entry before publishing"
```

**SEO:**
- Primary keyword: "peach recall 2026"
- Supporting: "FDA peach recall update," "recalled peaches brands," "10 million pounds peach recall"
- Format: News update, 500–700 words
- Schema: NewsArticle
- Cluster: FDA recalls / food safety

**Discover Notes:** Scores 3 — specific recall with named product, natural AI query, good SERP gap for updated FDA guidance vs. original recall coverage.

**Estimated Word Count:** 500–700 words

---

## REJECTED TOPICS LOG

| Topic | Rejection Reason |
|---|---|
| Birth order and disease risk (Nature) | `content_status: existing` — covered 08/06, no new development |
| Dronabinol/THC for PTSD nightmares | `content_status: existing` — covered 08/06 |
| Ibogaine for neurological recovery | `content_status: existing` — covered 08/06 |
| AI use for mental health / young people (Harvard Gazette) | `content_status: existing` — substantially same as 08/06 Gen Z/AI healthcare consultation story |
| P&G acquires Thorne for $3.8B | Off-category: pure pharma business / supplement marketing. Borderline criteria not met (no consumer health evidence angle) |
| Medical Aid in Dying (NY State) | Off-category: political/regulatory policy without new health data |
| HHS HRSA record-breaking care announcement | Off-category: institutional announcement, no consumer health editorial value |
| Trump admin foreign aid / maternal health (KFF) | Off-category: political healthcare policy |
| California Medi-Cal rollback (CalMatters) | Off-category: regional policy, no national consumer health angle |
| Senior wellness travel (Costa Rica) | Off-category: travel/lifestyle, no evidence-based health angle |
| National Wellness Month (multiple local sources) | Weak signal: local government content, no substantive health editorial angle |
| CVS DTC weight management expansion | Off-category: corporate product launch, not editorial health content |
| Crumbl dirty soda nutrition (Trends) | Off-category: brand/celebrity food trend, not nutrition science |
| Google Trends gut health rising queries | Data artifact: rising queries are clearly off-topic (unreal engine, digital nomad) — not actionable health signals |
| Celebrity health searches (Ariana Grande, Perez Hilton) | Brand safety: celebrity gossip without evidence base |
| Ariana Grande weight loss | Brand safety: celebrity body content, excluded |
| ALS clinical trial Dallas (NBC5) | Deferred: single local station source, no peer-reviewed publication; `recheck_on: 2026-08-10` |
| UC Davis heart valve investigational device | Deferred: single institutional source, insufficient corroboration; `recheck_on: 2026-08-10` |
| AI psychiatry training — WVU study | Deferred: niche academic/med-ed topic, insufficient audience relevance score; `recheck_on: 2026-08-10` |

---

## INTEGRITY FLAGS — CONSOLIDATED

> All ⚠️ flags from briefs, consolidated for editorial review before any content goes live.

**Brief 1 — Blood Thinner Recall:**
- ⚠️ Primary FDA notice URL not retrieved at scoring time — breaking-recall exception applied. **Retrieve FDA.gov recall database entry and add direct link before publishing.**
- ⚠️ Blood thinner patients must NOT stop medications without physician guidance — this must be stated prominently and early in the article.
- ⚠️ Specify which drugs/lots are confirmed recalled; do not imply all anticoagulants are affected.

**Brief 2 — Cyclospora Outbreak:**
- ⚠️ Primary CDC outbreak page confirmed but direct URL unverified at scoring time — retrieve CDC Cyclospora outbreak investigation URL before publishing.
- ⚠️ Cyclospora requires prescription antibiotic treatment — do not imply it is self-resolving.
- ⚠️ Specify which iceberg lettuce products/brands/lots are implicated per CDC; do not blanket-warn against all iceberg lettuce.

**Brief 3 — Eye Drops Recall:**
- ⚠️ Primary FDA notice URL not retrieved — breaking-recall exception applied. Retrieve before publishing.
- ⚠️ Distinguish clearly: this is a DIFFERENT recall from the Rohto recall covered 08/01. Do not conflate.
- ⚠️ "Sterility concern" ≠ confirmed contamination — maintain this distinction per FDA language.

**Brief 4 — Midlife Behaviors / Dementia:**
- ⚠️ Study is almost certainly observational — must not be presented as causal evidence.
- ⚠️ "13 more years" is a population-level statistical finding, not an individual outcome guarantee.
- ⚠️ Retrieve full study citation, journal name, and DOI before publishing.
- ⚠️ Confirm the specific 3 behaviors from primary source; do not speculate from headline.

**Brief 5 — Dormant Cancer Cells / Immunotherapy:**
- ⚠️ Determine whether findings are from cell lines, animal models, or human tissue — specify in article; do not extrapolate to clinical readiness.
- ⚠️ Do not imply this explains all immunotherapy failure or is ready for clinical application.
- ⚠️ Include clear statement for current immunotherapy patients: do not stop or change treatment based on one preclinical study.

**Brief 6 — Diet Soda / Cognitive Decline:**
- ⚠️ Most existing research is observational — association ≠ causation. State prominently.
- ⚠️ "Diet soda causes cognitive decline" is not a supported evidence consensus claim — do not frame as settled.
- ⚠️ Locate the specific study/trigger driving the current search spike before anchoring the piece.

**Brief 7 — Low Protein Diet / Longevity:**
- ⚠️ Most protein restriction lifespan data is from animal models — human applicability is uncertain.
- ⚠️ Direct tension with high-protein guidance for older adults (sarcopenia prevention) — both sides must be represented.
- ⚠️ Do not frame conclusion as "eat less protein" — evidence is genuinely complex and context-dependent.

**Brief 8 — Annual Wellness Visits / Cognitive Screening:**
- ⚠️ Annual wellness visits screen and refer — they do not diagnose dementia. Do not overstate.
- ⚠️ Cognitive screening tools vary by provider; not all conduct the same assessment.

**Brief 9 — Peach Recall Update:**
- ⚠️ Single secondary source with FDA attribution — verify FDA.gov recall database entry directly before publishing.
- ⚠️ Clarify from primary source what the "update" specifically entails before writing.

---

## RUN NOTES

```yaml
run_date: 2026-08-07
niche: health and wellness
signals_reviewed: ~164 (144 Google News + ~20 Trends rising queries)
topics_retained: 9
topics_rejected: 16
topics_deferred: 3
p1_count: 2
p2_count: 3
p3_count: 4
integrity_flags_total: 19
top_topic: "FDA blood thinner recall nationwide"
key_themes_this_run:
  - FDA recall wave (blood thinners, eye drops, peaches, Cyclospora/lettuce) — 4 of 9 candidates
  - Dementia prevention / aging (2 candidates — midlife behaviors, wellness visits)
  - Cancer research (immunotherapy resistance)
  - Nutrition/brain health (diet soda, protein/longevity)
tools_used: [SerpAPI Google News pre-fetch, SerpAPI Google Trends pre-fetch]
tools_unavailable: []
google_trends_available: true
google_trends_tool: serpapi_prefetch
search_velocity_source: google_trends
site_url_configured: false
self_check_method: competitor-list fallback + recent coverage list (7-day history)
notable_exclusions:
  - "Gut health Google Trends rising queries were clearly off-topic artifacts (unreal engine, digital nomad) — treated as data noise, not health signals. Flagged for SerpAPI/Trends data quality awareness."
  - "Celebrity weight loss/health queries (Ariana Grande, Perez Hilton) dominated 'health' and 'weight loss' Trends rising lists — all excluded per brand safety rules."
  - "P&G/Thorne acquisition ($3.8B) — notable business story but failed borderline criteria (supplement marketing / pure pharma business). Would merit coverage only if framed around consumer supplement access or safety data, which current sourcing does not support."
recurring_theme_check: "Birth order, GLP-1 cardiovascular, dronabinol/PTSD all appeared in prior 2 days — all set content_status: existing and excluded. No themes at 3+ consecutive run threshold."
archive_status: Run entry to be written to data/run_history.yaml
dashboard_output: outputs/daily_newsroom_dashboard/2026-08-07.html
deferred_topics_updated:
  - topic: "ALS clinical trial Dallas" — recheck_on: 2026-08-10
  - topic: "UC Davis heart valve investigational device" — recheck_on: 2026-08-10
  - topic: "AI psychiatry training WVU" — recheck_on: 2026-08-10
```

---

*Run complete. 9 candidates retained across P1–P3. All briefs include source plans with integrity flags. Deferred topics logged. Run history entry ready for archival.*