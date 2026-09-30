# LIVE SIGNAL DATA — SerpAPI Pre-Fetch
The following signals were fetched from SerpAPI Google News and SerpAPI Google Trends immediately before this pipeline run. Treat Google Trends as AVAILABLE when this section contains a Google Trends block. Use it as the primary search_velocity input for Skills 01–05 (Signal Listener through Trend Strength Scorer). Use the Google News Radar as the broad discovery layer for news-led health topics, including topics that do not yet appear in Google Trends. Prioritize topics with convergence across News, Trends, primary/institutional sources, and credible publisher coverage.

## Google Trends — Trending Now (US / Health, real-time)
Terms with a "Why:" line have a confirmed real-world news story driving the spike; terms without one are a real-time signal only, not yet grounded in a specific story.
  - inventia healthcare chlorthalidone tablet recall
    Why: "Widely used blood pressure medication recalled nationwide" — Fox Business

## Google Trends — 7-Day Interest (US)
  - **health**: latest=93, peak=100, 7d-delta=+3
    Rising related: darrell waltrip health, neko health, health insurance agency, health care fraud, sutter health park, essentia health, mental health, health insurance
  - **wellness**: latest=45, peak=100, 7d-delta=-3
    Rising related: tech gadgets 2025, spacecamp wellness, ai personal assistant, streaming shows trending, digital side hustles, kitchen tech upgrades, healthy cooking tools, ai image enhancer
  - **nutrition**: latest=97, peak=100, 7d-delta=-3
    Rising related: nutrition and sleep quality study, supplemental nutrition assistance program, bowmar nutrition, fitness nutrition twspoondietary, nutrition guide fparentips, acorn squash nutrition, butternut squash nutrition, nutrition facts
  - **fitness**: latest=16, peak=100, 7d-delta=-3
    Rising related: online banking review, diy home renovation, meal delivery service, tax software comparison, organic skincare products, baby stroller review, smart home devices, electric bike review
  - **food safety**: latest=67, peak=100, 7d-delta=+7
    Rising related: food safety violations tennessee valley, how many seconds should the entire handwashing process take, 123 premier food safety, which bacteria cause the greatest harm in the food industry, one of the most important reasons for using only reliable water sources is to reduce, according to the video, how was the banking act of 1933 a reaction to the great depression?, how can an operation prevent cross-contamination in self-service areas, premier food safety
  - **diet**: latest=87, peak=100, 7d-delta=-8
    Rising related: sean o'mara, sean o'mara diet, living diet sean o'mara, diet marble cheesecake, sean omara diet, the living diet sean o'mara, dr sean omara diet, dr sean o'mara diet
  - **weight loss**: latest=28, peak=100, 7d-delta=+2
    Rising related: what happened when dylan dreyer questioned craig melvin about weight loss on today, cagrisema and zepbound weight loss results, zion williamson weight loss, kate upton weight loss, alison hammond weight loss, camryn manheim weight loss, new weight loss drug, billy gardell weight loss
  - **mental health**: latest=60, peak=100, 7d-delta=+2
    Rising related: ted kaczynski mental health, mental health in aviation act, pilot mental health bill, john a. hauser mental health in aviation act, john a hauser mental health in aviation act, pink clouding mental health, unabomber mental health, kids mental health foundation
  - **gut health**: latest=47, peak=100, 7d-delta=-13
    Rising related: leaky gut symptoms, signs of bad gut health, list of fermented foods for gut health, best fermented foods for gut health, align probiotics, best mushroom coffee for gut health, fermented foods for gut health, fermented foods

Top rising related queries from Google Trends:
  - darrell waltrip health
  - neko health
  - health insurance agency
  - health care fraud
  - sutter health park
  - essentia health
  - mental health
  - health insurance
  - tech gadgets 2025
  - spacecamp wellness
  - ai personal assistant
  - streaming shows trending
  - digital side hustles
  - kitchen tech upgrades
  - healthy cooking tools
  - ai image enhancer
  - nutrition and sleep quality study
  - supplemental nutrition assistance program
  - bowmar nutrition
  - fitness nutrition twspoondietary

## Google News Radar — Recent Health Topics (144 unique across 12 queries; showing 60)
Treat these headlines as the broad radar of news-led health topics. The Signal Listener must consider this radar before narrowing to retained candidates.
  - (health) [blog.google] 09/24/2026, 05:07 PM, +0000 UTC — Our new health and safety tools are live in the Google Health app.
    
    Link: https://blog.google/products-and-platforms/products/google-health/health-guardian-features-live/
  - (health) [Department of Justice (.gov)] 09/25/2026, 04:15 PM, +0000 UTC — Texas Mental Health Clinic Owner Convicted in $26M Scheme to Defraud Military Health Benefits Program
    
    Link: https://www.justice.gov/opa/pr/texas-mental-health-clinic-owner-convicted-26m-scheme-defraud-military-health-benefits
  - (health) [California State Portal | CA.gov] 09/28/2026, 06:48 PM, +0000 UTC — Governor Newsom signs legislation creating non-UPF label, other health bills advancing California’s nation-leading healthcare strategy
    
    Link: https://www.gov.ca.gov/2026/09/28/governor-newsom-signs-legislation-creating-non-upf-label-other-health-bills-advancing-californias-nation-leading-healthcare-strategy/
  - (health) [pbs.org] 09/25/2026, 10:35 PM, +0000 UTC — Health care costs a major concern for voters ahead of midterms
    
    Link: https://www.pbs.org/newshour/show/health-care-costs-a-major-concern-for-voters-ahead-of-midterms
  - (health) [World Health Organization (WHO)] 09/25/2026, 10:09 PM, +0000 UTC — World leaders renew commitment to protect the world from future pandemics
    
    Link: https://www.who.int/news/item/25-09-2026-world-leaders-renew-commitment-to-protect-the-world-from-future-pandemics
  - (health) [NPR] 09/24/2026, 05:14 AM, +0000 UTC — OpenAI's breach of Australian health department website prompts rebuke
    
    Link: https://www.npr.org/2026/09/24/g-s1-144835/openai-breach-australia
  - (health) [Healthcare Dive] 09/28/2026, 03:44 PM, +0000 UTC — Insurers say AI could add billions in health costs. Billing companies disagree
    
    Link: https://www.healthcaredive.com/news/insurers-say-ai-could-add-billions-in-health-costs-billing-companies-disag/831497/
  - (health) [MPR News] 09/29/2026, 04:11 PM, +0000 UTC — Minnesota health systems HealthPartners, Essentia Health announce plan to merge
    
    Link: https://www.mprnews.org/story/2026/09/29/healthpartners-and-essentia-health-announce-plan-to-merge
  - (health) [Reuters] 09/25/2026, 04:00 PM, +0000 UTC — Americans navigate 'wild West' of health insurance options after dropping Obamacare plans
    
    Link: https://www.reuters.com/legal/litigation/americans-navigate-wild-west-health-insurance-options-after-dropping-obamacare-2026-09-25/
  - (health) [NJ.gov] 09/29/2026, 03:05 PM, +0000 UTC — New Jersey Health Department Issues Executive Directives to Ensure Access to Influenza, COVID-19, RSV, and Routine Childhood Vaccines
    
    Link: https://www.nj.gov/health/news/2026/approved/20260929a.shtml
  - (health) [Georgia Institute of Technology] 09/24/2026, 06:11 PM, +0000 UTC — Engineers Connect Health Wearables and Implants Using the Body as the Network
    
    Link: https://coe.gatech.edu/news/2026/09/engineers-connect-health-wearables-and-implants-using-body-network
  - (health) [newjerseymonitor.com] 09/25/2026, 05:48 PM, +0000 UTC — After state warning, NJ panel approves 34% health premium hike for teachers
    
    Link: https://newjerseymonitor.com/2026/09/25/nj-health-premium-increase-school-workers-approved/
  - (wellness) [cdcr.ca.gov] 09/29/2026, 01:46 PM, +0000 UTC — Valley State Prison hosts wellness fair
    
    Link: https://www.cdcr.ca.gov/insidecdcr/2026/09/29/valley-state-prison-hosts-wellness-fair/
  - (wellness) [UConn Today] 09/25/2026, 12:13 PM, +0000 UTC — 40 Years and Counting for Student Health and Wellness Fairs at UConn
    
    Link: https://today.uconn.edu/2026/09/celebrating-40-years-of-student-health-and-wellness-fairs-at-uconn/
  - (wellness) [The American Legion] 09/28/2026, 11:46 AM, +0000 UTC — Be the One focus of motorcycle ride, community wellness fair
    
    Link: https://www.legion.org/information-center/news/riders/2026/september/be-the-one-focus-of-motorcycle-ride-community-wellness-fair
  - (wellness) [Inter Miami CF] 09/29/2026, 02:06 PM, +0000 UTC — Inter Miami CF and Nu Stadium Host Annual Health and Wellness Fair for Front Office and Sporting Team Members
    
    Link: https://www.intermiamicf.com/news/inter-miami-cf-and-nu-stadium-host-annual-health-and-wellness-fair-for-front-office-and-sporting-team-members
  - (wellness) [UAMS News] 09/28/2026, 03:30 PM, +0000 UTC — UAMS-Sponsored Health & Wellness Expo Offers Free Screenings, Other Resources
    
    Link: https://news.uams.edu/2026/09/28/uams-sponsored-health-wellness-expo-offers-free-screenings-other-resources/
  - (wellness) [University of North Carolina Wilmington] 09/25/2026, 10:55 PM, +0000 UTC — Ncflex Miles For Wellness Challenge # 34
    
    Link: https://www.uncw.edu/news/administrative-units/human-resources/2026/09/ncflex-miles-for-wellness-challenge-34.html
  - (wellness) [State University of New York at Fredonia] 09/28/2026, 05:32 PM, +0000 UTC — Fredonia to hold World Mental Health Day Wellness Fair
    
    Link: https://www.fredonia.edu/news/articles/fredonia-hold-world-mental-health-day-wellness-fair
  - (wellness) [City of Champaign (.gov)] 09/29/2026, 07:31 AM, +0000 UTC — 4th Annual Black Mental Health and Wellness Conference Recap
    
    Link: https://champaignil.gov/2026/09/28/4th-annual-black-mental-health-and-wellness-conference-recap/
  - (wellness) [KCRA] 09/26/2026, 01:38 AM, +0000 UTC — San Joaquin County shelter opens new health and wellness center
    
    Link: https://www.kcra.com/article/san-joaquin-county-shelter-health-and-wellness-center/73896344
  - (wellness) [The Santa Barbara Independent] 09/29/2026, 10:41 PM, +0000 UTC — Santa Barbara High School Welcomes New-and-Improved Student Wellness Center
    
    Link: https://www.independent.com/2026/09/29/santa-barbara-high-school-welcomes-new-and-improved-student-wellness-center/
  - (wellness) [The New York Times] 09/28/2026, 07:00 AM, +0000 UTC — Do Supplement Patches Actually Work?
    
    Link: https://www.nytimes.com/2026/09/21/well/health-wellness-patches-supplements.html
  - (wellness) [Depor] 09/26/2026, 01:00 AM, +0000 UTC — Who Won Wellness Olympia 2026? Final Results and Placings
    
    Link: https://depor.com/en/us-live/who-won-wellness-olympia-2026-final-results-and-placings-nnda-nnrt-noticia/
  - (medical study) [Stanford Medicine] 09/28/2026, 03:36 PM, +0000 UTC — Cutting ultra-processed food from school menus will be tricky, Stanford Medicine study finds
    
    Link: https://med.stanford.edu/news/all-news/2026/09/ultra-processed-school-food.html
  - (medical study) [The University of Maryland, Baltimore] 09/25/2026, 04:59 PM, +0000 UTC — 2026 News
    
    Link: https://www.medschool.umaryland.edu/news/2026/new-umsom-research-shows-promising-results-for-health-care-professionals-using-ketogenic-diet-therapy-to-treat-mental-illness.html
  - (medical study) [UToledo News] 09/30/2026, 08:01 AM, +0000 UTC — UToledo Medical Students Set Sail to Study How Lake Erie Shapes Human Health
    
    Link: https://news.utoledo.edu/index.php/09_30_2026/utoledo-medical-students-set-sail-to-study-how-lake-erie-shapes-human-health
  - (medical study) [Nature] 09/29/2026, 10:42 AM, +0000 UTC — Reproducibility in biomedical research
    
    Link: https://www.nature.com/articles/s41591-026-04667-1
  - (medical study) [Healthcare Dive] 09/28/2026, 03:52 PM, +0000 UTC — Healthcare workers battle persistent long COVID: study
    
    Link: https://www.healthcaredive.com/news/healthcare-workers-battle-persistent-long-covid/831493/
  - (medical study) [News-Medical] 09/28/2026, 08:47 AM, +0000 UTC — Study links insomnia to higher stroke and hospitalization risks
    
    Link: https://www.news-medical.net/news/20260928/Study-links-insomnia-to-higher-stroke-and-hospitalization-risks.aspx
  - (medical study) [NPR] 09/24/2026, 09:00 AM, +0000 UTC — These 6 charts show how NIH research funding has been reshaped under Trump
    
    Link: https://www.npr.org/2026/09/24/nx-s1-5931971/trump-nih-science-funding-disruptions-charts
  - (medical study) [University of Cincinnati] 09/24/2026, 07:25 AM, +0000 UTC — More young adults are having strokes than three decades ago: UC study
    
    Link: https://www.uc.edu/news/articles/2026/09/more-young-adult-strokes-uc-study.html
  - (medical study) [WVIR] 09/25/2026, 09:48 PM, +0000 UTC — Icarus Medical seeks adults with knee pain for new brace study
    
    Link: https://www.29news.com/2026/09/25/icarus-medical-seeks-adults-with-knee-pain-new-brace-study/
  - (medical study) [MedPage Today] 09/24/2026, 05:33 PM, +0000 UTC — Is AI Flooding Medical Journals With 'Meaningless' Research?
    
    Link: https://www.medpagetoday.com/special-reports/features/123133
  - (medical study) [ScienceDaily] 09/24/2026, 03:59 AM, +0000 UTC — More REM sleep linked to lower risk of 83 diseases
    
    Link: https://www.sciencedaily.com/releases/2026/09/260923035930.htm
  - (medical study) [Veeva] 09/24/2026, 11:21 AM, +0000 UTC — New Veeva Study Builder Agent to Configure Clinical Studies in as Little as One Day
    
    Link: https://www.veeva.com/resources/new-veeva-study-builder-agent-to-configure-clinical-studies-in-as-little-as-one-day/
  - (clinical trial health) [Nature] 09/25/2026, 10:49 AM, +0000 UTC — Does expansion of clinical trial capacity improve healthcare access?
    
    Link: https://www.nature.com/articles/s41591-026-04683-1
  - (clinical trial health) [Pfizer] 09/30/2026, 12:26 PM, +0000 UTC — How AI Is Helping Match Patients to Clinical Trials Faster
    
    Link: https://www.pfizer.com/news/articles/how_ai_is_helping_match_patients_to_clinical_trials_faster
  - (clinical trial health) [The New York Times] 09/26/2026, 11:00 AM, +0000 UTC — Opinion | Why Do Clinical Trials for Cancer Drugs Take So Long?
    
    Link: https://www.nytimes.com/2026/09/26/opinion/clinical-trials-cancer-drugs.html
  - (clinical trial health) [Fierce Healthcare] 09/24/2026, 11:00 AM, +0000 UTC — Oracle Health rolls out AI solutions for RCM, oncology as part of broader healthcare, life sciences strategy
    
    Link: https://www.fiercehealthcare.com/health-tech/oracle-health-ai-clinical-financial-research
  - (clinical trial health) [stlamerican.com] 09/29/2026, 12:00 PM, +0000 UTC — Black patients face barriers to clinical trials
    
    Link: https://www.stlamerican.com/your-health-matters/black-patients-face-barriers-to-clinical-trials/
  - (clinical trial health) [Fierce Biotech] 09/29/2026, 07:04 PM, +0000 UTC — Canadian $5M accelerated clinical trial program cuts start-up to 45 days
    
    Link: https://www.fiercebiotech.com/cro/canadian-5m-accelerated-clinical-trial-program-cuts-start-45-days
  - (clinical trial health) [The Clinical Trial Vanguard] 09/26/2026, 07:28 AM, +0000 UTC — Platform Trials Are Rewriting the Rules of Evidence Generation. Regulators Haven’t Caught Up.
    
    Link: https://www.clinicaltrialvanguard.com/opinion/platform-trials-are-rewriting-the-rules-of-evidence-generation-regulators-havent-caught-up/
  - (clinical trial health) [news.va.gov] 09/27/2026, 08:30 PM, +0000 UTC — From health research to healthcare
    
    Link: https://news.va.gov/149786/from-health-research-to-healthcare/
  - (clinical trial health) [Crain's Chicago Business] 09/30/2026, 10:15 AM, +0000 UTC — Sinai Chicago teams with startup to bring clinical trials to safety-net system
    
    Link: https://www.chicagobusiness.com/health-care/ccb-sinai-clinical-trial-partnership-20260930/
  - (clinical trial health) [Rethinking Clinical Trials] 09/29/2026, 03:17 PM, +0000 UTC — September 29, 2026: Registration Opens for Pragmatic Trials Workshop at AcademyHealth–NIH Dissemination & Implementation Conference
    
    Link: https://rethinkingclinicaltrials.org/news/september-29-2026-registration-opens-for-pragmatic-trials-workshop-at-academyhealth-nih-dissemination-implementation-conference/
  - (clinical trial health) [Clinical Leader] 09/30/2026, 04:56 AM, +0000 UTC — Most Patients Learn About A Trial Online, But Is That What They Want?
    
    Link: https://www.clinicalleader.com/doc/most-patients-learn-about-a-trial-online-but-is-that-what-they-want-0001
  - (clinical trial health) [therevelator.org] 09/25/2026, 02:00 PM, +0000 UTC — Climate Policy Has a Sacrifice Problem. My Clinical Trials Kept Solving It by Accident.
    
    Link: https://therevelator.org/climate-policy-diet/
  - (FDA recall health) [NBC 5 Dallas-Fort Worth] 09/29/2026, 10:22 AM, +0000 UTC — FDA recalls more than 13k bottles of blood pressure medication after quality issue
    
    Link: https://www.nbcdfw.com/news/local/recall-alert-local/fda-recalls-more-than-13000-bottles-of-blood-pressure-medication-after-quality-issue/4083976/
  - (FDA recall health) [The Hill] 09/28/2026, 06:54 PM, +0000 UTC — Blood pressure medication recalled nationwide under FDA’s Class II risk level
    
    Link: https://thehill.com/homenews/6115677-blood-pressure-medication-recalled-nationwide-under-fdas-class-ii-risk-level/
  - (FDA recall health) [Dallas News] 09/28/2026, 11:10 PM, +0000 UTC — FDA recalls more than 13,000 bottles of blood pressure medication after quality issue
    
    Link: https://www.dallasnews.com/news/public-health/article/chlorthalidone-blood-pressure-tablets-recalled-fda-22453633.php
  - (FDA recall health) [EatingWell] 09/29/2026, 02:42 PM, +0000 UTC — The FDA Issued a Recall on Sugar Due to Contamination
    
    Link: https://www.eatingwell.com/sugar-recall-sept-2026-12146967
  - (FDA recall health) [health.com] 09/24/2026, 04:34 PM, +0000 UTC — FDA Announces Recall on Blood Pressure Medication—More Than 13,000 Bottles Affected Nationwide
    
    Link: https://www.health.com/blood-pressure-medication-recall-september-2026-12138343
  - (FDA recall health) [Good Housekeeping] 09/27/2026, 05:06 PM, +0000 UTC — FDA Announces New Nationwide Blood Pressure Medication Recall
    
    Link: https://www.goodhousekeeping.com/health/a73839435/fda-new-blood-pressure-medicine-recall/
  - (FDA recall health) [USA Today] 09/25/2026, 03:16 PM, +0000 UTC — Thyroid medicine recall receives FDA's highest risk level
    
    Link: https://www.usatoday.com/story/money/consumer-protection/recalls-alerts/2026/09/24/thyroid-tablet-medicine-recall-fda/91916444007/
  - (FDA recall health) [wusa9.com] 09/28/2026, 02:59 PM, +0000 UTC — Blood pressure medication recalled nationwide after failing FDA dissolution testing
    
    Link: https://www.wusa9.com/article/news/nation-world/blood-pressure-medication-recall/507-756358e0-3933-4870-a1f6-5f25d9512046
  - (FDA recall health) [LiveNOW from FOX] 09/24/2026, 07:52 PM, +0000 UTC — Thyroid medication recall upgraded to FDA's highest risk level
    
    Link: https://www.livenowfox.com/news/thyroid-medication-recall-vitruvias-therapeutics-class-i
  - (FDA recall health) [northjersey.com] 09/29/2026, 05:22 PM, +0000 UTC — FDA recalls 25k bottles of blood pressure meds for these products
    
    Link: https://www.northjersey.com/story/news/2026/09/29/fda-recalls-25k-bottles-blood-pressure-medication/92005192007/
  - (FDA recall health) [NewsNation] 09/28/2026, 07:58 PM, +0000 UTC — Blood pressure medication given Class II designation in recall update
    
    Link: https://www.newsnationnow.com/us-news/recalls/blood-pressure-medication-chlorthalidone-class-ii-recall-fda/
  - (FDA recall health) [Houston Chronicle] 09/28/2026, 04:26 PM, +0000 UTC — FDA updates recall of blood pressure medication with Class II risk level
    
    Link: https://www.houstonchronicle.com/news/houston-texas/trending/article/fda-class-ii-chlorthalidone-recall-22448678.php