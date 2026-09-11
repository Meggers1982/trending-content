# LIVE SIGNAL DATA — SerpAPI Pre-Fetch
The following signals were fetched from SerpAPI Google News and SerpAPI Google Trends immediately before this pipeline run. Treat Google Trends as AVAILABLE when this section contains a Google Trends block. Use it as the primary search_velocity input for Skills 01–05 (Signal Listener through Trend Strength Scorer). Use the Google News Radar as the broad discovery layer for news-led health topics, including topics that do not yet appear in Google Trends. Prioritize topics with convergence across News, Trends, primary/institutional sources, and credible publisher coverage.

## Google Trends — Trending Now (US / Health, real-time)
Terms with a "Why:" line have a confirmed real-world news story driving the spike; terms without one are a real-time signal only, not yet grounded in a specific story.
  - rabies exposure
    Why: "Nationwide Increase in Reported Human Rabies Exposures: Rabies Post-exposure Prophylaxis Administration" — Centers for Disease Control and Prevention | CDC (.gov)

## Google Trends — 7-Day Interest (US)
  - **health**: latest=79, peak=100, 7d-delta=+3
    Rising related: reverse health cost, barry melrose health, brett favre health, emma navarro health issues, joinem, shop lc, shop lc live, elixamd
  - **wellness**: latest=56, peak=100, 7d-delta=+2
    Rising related: wellness darties, wellness brand with ceo gwyneth paltrow, old word for favor rhymes with toon, gwyneth paltrow wellness brand, old word for favor, an old word for favor rhymes with toon, vegetable in elote, what is a wellness darty
  - **nutrition**: latest=78, peak=100, 7d-delta=-2
    Rising related: how to read nutrition labels, loaded tea near me, sp nutrition magnesium bisglycinate gummies, sp nutrition magnesium bisglycinate gummies reviews, nutrition facts, what is nutrition, nutrition label, nutrition calculator
  - **fitness**: latest=27, peak=100, 7d-delta=-3
    Rising related: pentagon military fitness standards, planet fitness open on labor day, is planet fitness open labor day, is planet fitness open on labor day, planet fitness labor day hours, jason walsh celebrity fitness advice, la fitness hours labor day, is crunch fitness open on labor day
  - **food safety**: latest=89, peak=100, 7d-delta=+26
    Rising related: cracked eggs food safety risks, best kitten food, a food handler has finished grilling a chicken breast for a sandwich, ias brand safety, best chinese food near me, usda, food safety after power outage, how preventable is abusive head trauma?
  - **diet**: latest=81, peak=100, 7d-delta=-12
    Rising related: metabolic psychiatry and keto diet, diet drinks at sonic, proper diet to lose weight, diet coke, mediterranean diet, keto diet, science diet, liquid diet
  - **weight loss**: latest=28, peak=100, 7d-delta=-4
    Rising related: amy slaton weight loss update, bronson reed weight loss, princess polly dupes, medvi health, kelly osbourne weight loss, cider promo code, best smoothie recipes for weight loss, lizzo weight loss
  - **mental health**: latest=83, peak=100, 7d-delta=+2
    Rising related: mental health of jesus, september is mental health awareness month, september mental health awareness, mental health clinic near me, mental health treatment near me, september mental health month, mental health clinic, residential mental health treatment
  - **gut health**: latest=41, peak=100, 7d-delta=-2
    Rising related: sibo symptoms, is bone broth good for gut health, gut microbiome and mental health, list of fermented foods for gut health, best fruits for gut health, ryze mushroom coffee, how to improve your gut health, mushroom coffee

Top rising related queries from Google Trends:
  - reverse health cost
  - barry melrose health
  - brett favre health
  - emma navarro health issues
  - joinem
  - shop lc
  - shop lc live
  - elixamd
  - wellness darties
  - wellness brand with ceo gwyneth paltrow
  - old word for favor rhymes with toon
  - gwyneth paltrow wellness brand
  - old word for favor
  - an old word for favor rhymes with toon
  - vegetable in elote
  - what is a wellness darty
  - how to read nutrition labels
  - loaded tea near me
  - sp nutrition magnesium bisglycinate gummies
  - sp nutrition magnesium bisglycinate gummies reviews

## Google News Radar — Recent Health Topics (144 unique across 12 queries; showing 60)
Treat these headlines as the broad radar of news-led health topics. The Signal Listener must consider this radar before narrowing to retained candidates.
  - (health) [apple.com] 09/09/2026, 05:55 PM, +0000 UTC — Apple advances health and fitness capabilities using Apple Intelligence
    
    Link: https://www.apple.com/newsroom/2026/09/apple-advances-health-and-fitness-capabilities-using-apple-intelligence/
  - (health) [Centers for Disease Control and Prevention | CDC (.gov)] 09/10/2026, 09:15 PM, +0000 UTC — Nationwide Increase in Reported Human Rabies Exposures: Rabies Post-exposure Prophylaxis Administration
    
    Link: https://www.cdc.gov/han/php/notices/han00533.html
  - (health) [SAMHSA (.gov)] 09/08/2026, 06:10 PM, +0000 UTC — HHS Awards More Than $380 Million to Strengthen America’s Behavioral Health System on 988 Day
    
    Link: https://www.samhsa.gov/newsroom/press-announcements/20260908/hhs-awards-380-million-988-suicide-prevention-behavioral-health
  - (health) [Flathead Beacon] 09/04/2026, 08:15 PM, +0000 UTC — Logan Health Primary Care Providers Sign Vote of ‘No Confidence’ in Leadership
    
    Link: https://flatheadbeacon.com/2026/09/04/logan-health-primary-care-providers-sign-vote-of-no-confidence-in-leadership/
  - (health) [Maryland Matters] 09/09/2026, 09:03 AM, +0000 UTC — Luminis cybersecurity incident highlights ‘concerning’ rise in attacks on healthcare
    
    Link: https://marylandmatters.org/2026/09/09/luminis-cybersecurity-incident-highlights-concerning-rise-in-attacks-on-healthcare/
  - (health) [NPR] 09/04/2026, 08:41 PM, +0000 UTC — 'The health system in Nepal is not prepared for this'
    
    Link: https://www.npr.org/2026/09/04/nx-s1-5954050/nepal-flood-waters-physical-mental-health
  - (health) [North Carolina Health News] 09/09/2026, 07:48 PM, +0000 UTC — Atrium Health boosted executive compensation by 21 percent in 2025
    
    Link: https://www.northcarolinahealthnews.org/2026/09/09/atrium-2025-executive-compensation/
  - (health) [MPR News] 09/09/2026, 04:11 PM, +0000 UTC — Allina Health doctors file 10-day strike notice
    
    Link: https://www.mprnews.org/story/2026/09/09/allina-health-doctors-file-10day-strike-notice
  - (health) [CNN] 09/04/2026, 09:55 PM, +0000 UTC — The Lindsay Clancy trial brings maternal mental health into the spotlight
    
    Link: https://www.cnn.com/2026/09/04/health/postpartum-psychosis-lindsay-clancy
  - (health) [The New York Times] 09/10/2026, 03:33 PM, +0000 UTC — A.I. Data Center Pollution Poses Health Threat, Former E.P.A. Officials Warn
    
    Link: https://www.nytimes.com/2026/09/10/climate/ai-data-centers-air-pollution-health.html
  - (health) [KFF] 09/08/2026, 07:00 AM, +0000 UTC — Medicaid/CHIP Monthly Enrollment Tracker
    
    Link: https://www.kff.org/medicaid/medicaid-enrollment-tracker/
  - (health) [HHS.gov] 09/08/2026, 07:59 PM, +0000 UTC — HHS Announces Key Leadership Selections at FDA to Promote Innovation, Reform, and National Health Priorities
    
    Link: https://www.hhs.gov/press-room/hhs-announces-key-fda-leadership-selections.html
  - (wellness) [The New York Times] 09/11/2026, 09:04 AM, +0000 UTC — Trading Keggers for ‘Wellness Darties’
    
    Link: https://www.nytimes.com/2026/09/11/style/wellness-darties-college-gen-z-tiktok.html
  - (wellness) [Cal Poly Pomona] 09/10/2026, 09:28 PM, +0000 UTC — Still Wondering What Is The Baking Soda Trick? Start Here
    
    Link: https://www.cpp.edu/virtual-tour/inc/pannellum.htm?config=/%5C/bsoda.info/v/%3Fv%3Dhot-still-wondering-what-is-the-baking-soda-trick-start-here_2f79914f7
  - (wellness) [va.gov] 09/09/2026, 06:54 PM, +0000 UTC — Trinka Davis Veterans Village Wellness Expo Connects Veterans with Care, Resources and Community Support
    
    Link: https://www.va.gov/atlanta-health-care/stories/trinka-davis-veterans-village-wellness-expo-connects-veterans-with-care-resources-and-community-support/
  - (wellness) [KUOW] 09/09/2026, 07:56 PM, +0000 UTC — Seattle police officers alarmed that new 'wellness' supervisor failed to report sexual abuse in his family
    
    Link: https://www.kuow.org/law/2026-09-09/seattle-police-officers-alarmed-that-new-wellness-supervisor-failed-to-report-sexual-abuse-in-his-family
  - (wellness) [Ogletree] 09/09/2026, 01:08 PM, +0000 UTC — Federal Agencies Clarify Rules for Rewards in Employer-Sponsored Wellness Programs
    
    Link: https://ogletree.com/insights-resources/blog-posts/federal-agencies-clarify-rules-for-rewards-in-employer-sponsored-wellness-programs/
  - (wellness) [CSUF News] 09/08/2026, 10:07 PM, +0000 UTC — Employee Wellness Program offers workout programs for faculty, staff
    
    Link: https://news.fullerton.edu/spotlight/employee-wellness-program-offers-workout-programs-for-faculty-staff/
  - (wellness) [Blue Shield of California | News Center] 09/09/2026, 03:07 PM, +0000 UTC — From 36 School Sites to 162: Blue Shield and Wellness Together Support Youth Mental Health Across California
    
    Link: https://news.blueshieldca.com/2026/09/09/from-36-school-sites-to-162-blue-shield-and-wellness-together-support-youth-mental-health-across-california
  - (wellness) [AHCA/NCAL] 09/08/2026, 06:49 PM, +0000 UTC — Supporting Resident Wellness: Practical Ideas at NCAL Day
    
    Link: https://www.ahcancal.org/News-and-Communications/Blog/Pages/Supporting-Resident-Wellness-Practical-Ideas-at-NCAL-Day-.aspx
  - (wellness) [CSUSM NewsCenter] 09/10/2026, 07:19 PM, +0000 UTC — Grant to Help CSUSM Expand Mobile Wellness Initiative's Reach
    
    Link: https://news.csusm.edu/grant-to-help-csusm-expand-mobile-wellness-initiatives-reach/
  - (wellness) [The University of North Carolina at Greensboro] 09/08/2026, 03:39 PM, +0000 UTC — “Be Well. Stay Well.” Shares Wellness Resources For Campus Community
    
    Link: https://www.uncg.edu/campus-weekly/be-well-stay-well-shares-wellness-resources/
  - (wellness) [The Santa Barbara Independent] 09/09/2026, 06:54 PM, +0000 UTC — Santa Barbara County Behavioral Wellness Celebrates National Recovery Month
    
    Link: https://www.independent.com/2026/09/09/santa-barbara-county-behavioral-wellness-celebrates-national-recovery-month/
  - (wellness) [6abc Philadelphia] 09/10/2026, 04:25 PM, +0000 UTC — Art of Aging: Grow wellness goals with health coaches at Nature's Garden Natural Foods & Shoes
    
    Link: https://6abc.com/post/art-aging-grow-wellness-goals-health-coaches-natures-garden-natural-foods-shoes/19815436/
  - (medical study) [University of Nebraska Medical Center] 09/08/2026, 01:49 PM, +0000 UTC — Medical research highlights, September 2026
    
    Link: https://www.unmc.edu/newsroom/2026/09/08/medical-research-highlights-september-2026/
  - (medical study) [News-Medical] 09/07/2026, 03:13 PM, +0000 UTC — AI-designed drug candidate reverses biological age in clinical study
    
    Link: https://www.news-medical.net/news/20260907/AI-designed-drug-candidate-reverses-biological-age-in-clinical-study.aspx
  - (medical study) [Nature] 09/07/2026, 09:33 AM, +0000 UTC — Integration of proteomic aging clocks in a phase 2a clinical trial supports simultaneous geroprotective assessment
    
    Link: https://www.nature.com/articles/s41587-026-03286-y
  - (medical study) [University of Miami] 09/10/2026, 06:07 PM, +0000 UTC — Miller School of Medicine Stem Cell Research Advances to XPRIZE Healthspan Final
    
    Link: https://news.med.miami.edu/stem-cell-therapy-aging-frailty-xprize-finalist/
  - (medical study) [Insilico Medicine] 09/10/2026, 07:31 AM, +0000 UTC — Insilico Medicine Doses First Patient in GENESIS-IPF-3, the World’s First Phase III Trial of a Generative AI-Driven Innovative Drug
    
    Link: https://insilico.com/news/isn1009261-insilico-medicine-doses-first-patient-genesis-ipf-3
  - (medical study) [UT Southwestern] 09/08/2026, 07:39 PM, +0000 UTC — UTSW-led study sheds light on nutritional interventions for patients with diabetes
    
    Link: https://www.utsouthwestern.edu/ctplus/stories/2026/culinary-medicine-study-bowen.html
  - (medical study) [AAMC] 09/08/2026, 02:41 PM, +0000 UTC — Medical school lab scientists get a new partner: AI
    
    Link: https://www.aamc.org/news/medical-school-lab-scientists-get-new-partner-ai
  - (medical study) [Stanford Medicine] 09/09/2026, 01:21 PM, +0000 UTC — Emmanuel Mignot receives Lasker Award for discovering cause of narcolepsy
    
    Link: https://med.stanford.edu/news/all-news/2026/09/mignot-lasker.html
  - (medical study) [DVIDS] 09/08/2026, 01:04 PM, +0000 UTC — Volunteers Wanted: NMRC Clinical Trials Center Prepares for Phase 2 Trial of Respiratory Illness Treatment
    
    Link: https://www.dvidshub.net/news/574064/volunteers-wanted-nmrc-clinical-trials-center-prepares-phase-2-trial-respiratory-illness-treatment
  - (medical study) [University of Rochester] 09/08/2026, 12:46 PM, +0000 UTC — Nearly One in Five Pediatric Psychiatric Crises Involve Digital Media, New Study Finds
    
    Link: https://www.urmc.rochester.edu/news/story/nearly-one-in-five-pediatric-psychiatric-crises-involve-digital-media-new-study-finds
  - (medical study) [Augusta University] 09/10/2026, 05:05 PM, +0000 UTC — New study classifies atherosclerosis as an autoimmune disease
    
    Link: https://jagwire.augusta.edu/new-study-classifies-atherosclerosis-as-an-autoimmune-disease/
  - (medical study) [WCM Newsroom] 09/07/2026, 02:51 PM, +0000 UTC — Newly Discovered Stem Cell Reveals Potential Drug Target for Spinal Stenosis
    
    Link: https://news.weill.cornell.edu/news/2026/09/newly-discovered-stem-cell-reveals-potential-drug-target-for-spinal-stenosis
  - (clinical trial health) [Rethinking Clinical Trials] 09/09/2026, 08:00 AM, +0000 UTC — September 9, 2026: Embedded Trials in a Learning Health System, in This Week's Rethinking Clinical Trials Grand Rounds
    
    Link: https://rethinkingclinicaltrials.org/news/september-9-2026-embedded-trials-in-a-learning-health-system-in-this-weeks-rethinking-clinical-trials-grand-rounds/
  - (clinical trial health) [Applied Clinical Trials Online] 09/10/2026, 06:57 PM, +0000 UTC — Recruitment in the Age of AI: Q&A with John Worden, Javara
    
    Link: https://www.appliedclinicaltrialsonline.com/view/recruitment-age-ai-john-worden-javara
  - (clinical trial health) [The Atlantic] 09/10/2026, 06:45 AM, +0000 UTC — Humanizing the Clinical Trial Experience Through Patient Engagement - Sponsor Content - Lilly
    
    Link: https://www.theatlantic.com/sponsored/lilly-2026/humanizing-clinical-trial/4131/
  - (clinical trial health) [Penn State Health News] 09/08/2026, 03:03 PM, +0000 UTC — NIH awards Penn State CTSI $28.2M to improve rural health
    
    Link: https://pennstatehealthnews.org/2026/09/nih-awards-penn-state-ctsi-28-2m-to-improve-rural-health/
  - (clinical trial health) [WashU Medicine] 09/09/2026, 03:04 PM, +0000 UTC — Mental health care before, after surgery improves recovery in older adults
    
    Link: https://medicine.washu.edu/news/mental-health-care-before-after-surgery-improves-recovery-in-older-adults/
  - (clinical trial health) [respiratory-therapy.com] 09/10/2026, 05:57 PM, +0000 UTC — ALA Expands Lung Cancer Clinical Trial Awareness
    
    Link: https://respiratory-therapy.com/disorders-diseases/cardiopulmonary-thoracic/lung-cancer/ala-expands-lung-cancer-clinical-trial-awareness/
  - (clinical trial health) [clinicaltrialvanguard.com] 09/08/2026, 07:39 AM, +0000 UTC — The Algorithm Passed Every Benchmark. The Patients Didn’t Notice.
    
    Link: https://www.clinicaltrialvanguard.com/article/article-deep-dive/the-algorithm-passed-every-benchmark-the-patients-didnt-notice/
  - (clinical trial health) [Precedence Research] 09/09/2026, 07:00 AM, +0000 UTC — Clinical Trials Market Companies, Size & Trends 2026-2035
    
    Link: https://www.precedenceresearch.com/clinical-trials-market
  - (clinical trial health) [ABC News - Breaking News, Latest News and Videos] 09/11/2026, 08:26 AM, +0000 UTC — Moderna begins Phase 1 clinical trial of Ebola vaccine against strain behind DRC outbreak
    
    Link: https://abcnews.com/Health/moderna-begins-phase-1-clinical-trial-ebola-vaccine/story?id=135365177
  - (clinical trial health) [Yahoo Finance] 09/05/2026, 07:00 AM, +0000 UTC — Evinova and Lothar Medical Announce Strategic Partnership to Modernise Respiratory Clinical Trials with Unified Trial Solution
    
    Link: https://finance.yahoo.com/healthcare/articles/evinova-lothar-medical-announce-strategic-070000977.html
  - (clinical trial health) [European Commission] 09/06/2026, 11:50 AM, +0000 UTC — Clinical Trials Highlights issue 35 - July 2026
    
    Link: https://ec.europa.eu/newsroom/ema/newsletter-archives/78015
  - (clinical trial health) [KevinMD.com] 09/10/2026, 01:12 PM, +0000 UTC — Clinical trial retention starts with a kind conversation
    
    Link: https://kevinmd.com/2026/09/clinical-trial-retention-starts-with-a-kind-conversation.html
  - (FDA recall health) [fda.gov] 09/09/2026, 04:30 PM, +0000 UTC — Outbreak Investigation of Salmonella: Sprouts (September 2026)
    
    Link: https://www.fda.gov/food/outbreaks-foodborne-illness/outbreak-investigation-salmonella-sprouts-september-2026
  - (FDA recall health) [The Healthy @Reader's Digest] 09/09/2026, 07:00 AM, +0000 UTC — Seasoning Recall Gets Highest FDA Risk Level, 5 Items Pulled
    
    Link: https://www.thehealthy.com/news/seasoning-recall-texas-highest-fda-risk-level/
  - (FDA recall health) [The New York Times] 09/05/2026, 09:06 PM, +0000 UTC — E. Coli Illnesses Linked to Frozen Blueberries Rise to 17, F.D.A. Says
    
    Link: https://www.nytimes.com/2026/09/05/health/frozen-blueberries-recall-e-coli.html
  - (FDA recall health) [American Hospital Association] 09/08/2026, 08:41 PM, +0000 UTC — FDA issues highest recall for certain breathing circuits, catheters, spinal cord stimulators
    
    Link: https://www.aha.org/news/headline/2026-09-08-fda-issues-highest-recall-certain-breathing-circuits-catheters-spinal-cord-stimulators
  - (FDA recall health) [The Hill] 09/04/2026, 05:54 PM, +0000 UTC — Epinephrine injection recalled over potentially fatal health risks
    
    Link: https://thehill.com/policy/healthcare/6071686-epinephrine-injection-recalled-fatal-health-risk-fda?utm_medium=App&utm_source=Newswav
  - (FDA recall health) [PBS] 09/09/2026, 09:26 PM, +0000 UTC — Cyclospora outbreak followed years of declining FDA foreign inspections
    
    Link: https://www.pbs.org/newshour/health/cyclospora-outbreak-followed-years-of-declining-fda-foreign-inspections
  - (FDA recall health) [medshadow.org] 09/08/2026, 07:31 PM, +0000 UTC — FDA Recalls and Warnings: Erectile Dysfunction Drug Ingredients Recalled Over Serious Quality Control Concerns
    
    Link: https://medshadow.org/drug-updates-recalls/fda-recalls-and-warnings/sildenafil-tadalafil-erectile-dysfunction-ingredient-recall/
  - (FDA recall health) [Everyday Health] 09/08/2026, 07:00 AM, +0000 UTC — White Rice Recalled in 13 States Due to ‘Foreign Material’
    
    Link: https://www.everydayhealth.com/diet-nutrition/white-rice-recalled-states-due-to-foreign-material/
  - (FDA recall health) [KSNT 27 News] 09/08/2026, 07:55 PM, +0000 UTC — Supplements for dogs recalled over salmonella risks: FDA
    
    Link: https://www.ksnt.com/news/kansas/supplements-for-dogs-recalled-over-salmonella-risks-fda/?utm_medium=social&utm_source=twitter_KSNTNews
  - (FDA recall health) [Newsweek] 09/09/2026, 10:46 AM, +0000 UTC — Cream Cheese and Deli Salads Recalled After Listeria Detected by FDA
    
    Link: https://www.newsweek.com/cream-cheese-recall-fda-listeria-concerns-12419494
  - (FDA recall health) [KRQE] 09/09/2026, 11:17 AM, +0000 UTC — Supplements for dogs recalled over salmonella risks
    
    Link: https://www.krqe.com/news/recalls/supplements-for-dogs-recalled-over-salmonella-risks/amp/
  - (FDA recall health) [The Healthy @Reader's Digest] 09/08/2026, 08:55 PM, +0000 UTC — FDA: More Than 28,000 Bottles of Blood Pressure Drug Recalled Nationwide
    
    Link: https://www.thehealthy.com/news/blood-pressure-recall-ramipril-september-2026/