# LIVE SIGNAL DATA — SerpAPI Pre-Fetch
The following signals were fetched from SerpAPI Google News and SerpAPI Google Trends immediately before this pipeline run. Treat Google Trends as AVAILABLE when this section contains a Google Trends block. Use it as the primary search_velocity input for Skills 01–05 (Signal Listener through Trend Strength Scorer). Use the Google News Radar as the broad discovery layer for news-led health topics, including topics that do not yet appear in Google Trends. Prioritize topics with convergence across News, Trends, primary/institutional sources, and credible publisher coverage.

## Google Trends — Trending Now (US / Health, real-time)
Terms with a "Why:" line have a confirmed real-world news story driving the spike; terms without one are a real-time signal only, not yet grounded in a specific story.
  - fda chlorthalidone dissolution testing recall
    Why: "Blood pressure medication recalled nationwide after failing FDA dissolution testing" — WUSA9
  - will reeve
    Why: "Will Reeve Reveals Testicular Cancer Diagnosis" — People.com

## Google Trends — 7-Day Interest (US)
  - **health**: latest=98, peak=100, 7d-delta=+3
    Rising related: darrell waltrip health, neko health, salem health, mike ditka health, randy travis health, health insurance agency, sutter health park, health care fraud
  - **wellness**: latest=25, peak=100, 7d-delta=-2
    Rising related: tiktok wellness trends botulism warning, spacecamp wellness, space camp wellness, wellness gadgets, healthsciencesforum.com health and wellness coach, little luxe wellness lodge, quietgrovehaven.com discover insights on wellness, parenting wellness infoguide famparentlife
  - **nutrition**: latest=86, peak=100, 7d-delta=-2
    Rising related: nutrition and sleep quality study, costco churro nutrition, cocoa pebbles nutrition facts, bowmar nutrition, fitness nutrition twspoondietary, delicata squash nutrition, nutrition guide fparentips, golden kiwi nutrition
  - **fitness**: latest=18, peak=100, 7d-delta=-2
    Rising related: tax software comparison, online banking review, standing desk review, diy home renovation, moving company quotes, camping gear essentials, home security camera, organic skincare products
  - **food safety**: latest=57, peak=100, 7d-delta=-18
    Rising related: food safety violations tennessee valley, king county food safety rating, loss of refrigeration is considered an, regulations establish the floor for safety in childcare., food safety certification texas, food safety specialist, food handlers, what is food safety
  - **diet**: latest=94, peak=100, 7d-delta=-3
    Rising related: 12 hour fasting diet fntkdiet, derrick henry diet, full liquid diet foods, diet coke, mediterranean diet, mediterranean, healthy diet, science diet
  - **weight loss**: latest=51, peak=100, 7d-delta=-10
    Rising related: what happened when dylan dreyer questioned craig melvin about weight loss on today, zion williamson weight loss, cagrisema and zepbound weight loss results, kate upton weight loss, zion williamson, cree summer weight loss, joel embiid weight loss, paul hollywood weight loss
  - **mental health**: latest=59, peak=100, 7d-delta=-1
    Rising related: ted kaczynski mental health, unabomber mental health, john a. hauser mental health in aviation act, pilot mental health bill, pink clouding mental health, mental health in aviation act, moccasin bend mental health institute, mental health women villakalima.com
  - **gut health**: latest=53, peak=100, 7d-delta=-7
    Rising related: gastroenterologist, probiotic vs prebiotic, best fermented foods for gut health, is sourdough good for gut health, is sauerkraut good for gut health, sibo symptoms, ibs symptoms, culturelle probiotics

Top rising related queries from Google Trends:
  - darrell waltrip health
  - neko health
  - salem health
  - mike ditka health
  - randy travis health
  - health insurance agency
  - sutter health park
  - health care fraud
  - tiktok wellness trends botulism warning
  - spacecamp wellness
  - space camp wellness
  - wellness gadgets
  - healthsciencesforum.com health and wellness coach
  - little luxe wellness lodge
  - quietgrovehaven.com discover insights on wellness
  - parenting wellness infoguide famparentlife
  - nutrition and sleep quality study
  - costco churro nutrition
  - cocoa pebbles nutrition facts
  - bowmar nutrition

## Google News Radar — Recent Health Topics (144 unique across 12 queries; showing 60)
Treat these headlines as the broad radar of news-led health topics. The Signal Listener must consider this radar before narrowing to retained candidates.
  - (health) [blog.google] 09/24/2026, 05:07 PM, +0000 UTC — Our new health and safety tools are live in the Google Health app.
    
    Link: https://blog.google/products-and-platforms/products/google-health/health-guardian-features-live/
  - (health) [HHS.gov] 09/22/2026, 09:45 PM, +0000 UTC — Indian Health Service Awards $3.5 Million for Tribal Food and Nutrition Initiatives
    
    Link: https://www.hhs.gov/press-room/indian-health-service-awards-3-million-tribal-food-nutrition-initiatives.html
  - (health) [Department of Justice (.gov)] 09/25/2026, 04:15 PM, +0000 UTC — Texas Mental Health Clinic Owner Convicted in $26M Scheme to Defraud Military Health Benefits Program
    
    Link: https://www.justice.gov/opa/pr/texas-mental-health-clinic-owner-convicted-26m-scheme-defraud-military-health-benefits
  - (health) [California State Portal | CA.gov] 09/28/2026, 06:48 PM, +0000 UTC — Governor Newsom signs legislation creating non-UPF label, other health bills advancing California’s nation-leading healthcare strategy
    
    Link: https://www.gov.ca.gov/2026/09/28/governor-newsom-signs-legislation-creating-non-upf-label-other-health-bills-advancing-californias-nation-leading-healthcare-strategy/
  - (health) [PBS] 09/25/2026, 10:35 PM, +0000 UTC — Health care costs a major concern for voters ahead of midterms
    
    Link: https://www.pbs.org/newshour/show/health-care-costs-a-major-concern-for-voters-ahead-of-midterms
  - (health) [who.int] 09/25/2026, 10:09 PM, +0000 UTC — World leaders renew commitment to protect the world from future pandemics
    
    Link: https://www.who.int/news/item/25-09-2026-world-leaders-renew-commitment-to-protect-the-world-from-future-pandemics
  - (health) [NPR] 09/26/2026, 09:00 AM, +0000 UTC — Meal deliveries can save money and improve health. Will they survive Medicaid cuts?
    
    Link: https://www.npr.org/2026/09/26/nx-s1-5946434/medically-tailored-meal-deliveries-medicaid-cuts
  - (health) [Healthcare Dive] 09/28/2026, 03:44 PM, +0000 UTC — Insurers say AI could add billions in health costs. Billing companies disagree
    
    Link: https://www.healthcaredive.com/news/insurers-say-ai-could-add-billions-in-health-costs-billing-companies-disag/831497/
  - (health) [Georgia Institute of Technology] 09/24/2026, 06:11 PM, +0000 UTC — Engineers Connect Health Wearables and Implants Using the Body as the Network
    
    Link: https://coe.gatech.edu/news/2026/09/engineers-connect-health-wearables-and-implants-using-body-network
  - (health) [Reuters] 09/25/2026, 07:13 PM, +0000 UTC — Senate approves mental health legislation for US pilots, air traffic controllers
    
    Link: https://www.reuters.com/business/healthcare-pharmaceuticals/us-senate-approves-legislation-address-pilot-air-traffic-control-mental-health-2026-09-25/
  - (health) [MPR News] 09/29/2026, 04:11 PM, +0000 UTC — Minnesota health systems HealthPartners, Essentia Health announce plan to merge
    
    Link: https://www.mprnews.org/story/2026/09/29/healthpartners-and-essential-health-announce-plan-to-merge
  - (health) [NYC.gov] 09/28/2026, 07:45 PM, +0000 UTC — NYC Health Department Celebrates Opening of New Clubhouse for Adults With Serious Mental Illness in the Bronx
    
    Link: https://www.nyc.gov/site/doh/about/press/pr2026/nyc-health-department-celebrates-new-clubhouse-in-the-bronx.page
  - (wellness) [WCAX] 09/24/2026, 08:18 PM, +0000 UTC — Police search Newport, N.H. wellness spa in human trafficking investigation
    
    Link: https://www.wcax.com/2026/09/24/police-search-newport-wellness-spa-human-trafficking-investigation/
  - (wellness) [cdcr.ca.gov] 09/29/2026, 01:46 PM, +0000 UTC — Valley State Prison hosts wellness fair
    
    Link: https://www.cdcr.ca.gov/insidecdcr/2026/09/29/valley-state-prison-hosts-wellness-fair/
  - (wellness) [WBAL-TV] 09/24/2026, 04:45 PM, +0000 UTC — Events in Baltimore prioritize men's health & wellness
    
    Link: https://www.wbaltv.com/article/mens-health-wellness-events-baltimore/73871922
  - (wellness) [Dartmouth] 09/24/2026, 07:19 PM, +0000 UTC — Teevens Center Expands Role in Student Wellness
    
    Link: https://home.dartmouth.edu/news/2026/09/teevens-center-expands-role-student-wellness
  - (wellness) [Happily Eva After] 09/23/2026, 08:03 AM, +0000 UTC — My Family Wellness Strategies
    
    Link: https://happilyevaafter.com/my-family-wellness-strategies/
  - (wellness) [Inter Miami CF] 09/29/2026, 02:06 PM, +0000 UTC — Inter Miami CF and Nu Stadium Host Annual Health and Wellness Fair for Front Office and Sporting Team Members
    
    Link: https://www.intermiamicf.com/news/inter-miami-cf-and-nu-stadium-host-annual-health-and-wellness-fair-for-front-office-and-sporting-team-members
  - (wellness) [UAMS News] 09/28/2026, 03:30 PM, +0000 UTC — UAMS-Sponsored Health & Wellness Expo Offers Free Screenings, Other Resources
    
    Link: https://news.uams.edu/2026/09/28/uams-sponsored-health-wellness-expo-offers-free-screenings-other-resources/
  - (wellness) [The American Legion] 09/28/2026, 11:46 AM, +0000 UTC — Be the One focus of motorcycle ride, community wellness fair
    
    Link: https://www.legion.org/information-center/news/riders/2026/september/be-the-one-focus-of-motorcycle-ride-community-wellness-fair
  - (wellness) [State University of New York at Fredonia] 09/28/2026, 05:32 PM, +0000 UTC — Fredonia to hold World Mental Health Day Wellness Fair
    
    Link: https://www.fredonia.edu/news/articles/fredonia-hold-world-mental-health-day-wellness-fair
  - (wellness) [University of North Carolina Wilmington | UNCW] 09/25/2026, 10:55 PM, +0000 UTC — Ncflex Miles For Wellness Challenge # 34
    
    Link: https://www.uncw.edu/news/administrative-units/human-resources/2026/09/ncflex-miles-for-wellness-challenge-34.html
  - (wellness) [City of Champaign (.gov)] 09/29/2026, 07:31 AM, +0000 UTC — 4th Annual Black Mental Health and Wellness Conference Recap
    
    Link: https://champaignil.gov/2026/09/28/4th-annual-black-mental-health-and-wellness-conference-recap/
  - (wellness) [carthage.edu] 09/23/2026, 07:00 AM, +0000 UTC — Attend the Carthage Wellness Fair Sept. 30
    
    Link: https://www.carthage.edu/live/news/58021-attend-the-carthage-wellness-fair-sept-30
  - (medical study) [Nature] 09/22/2026, 09:28 PM, +0000 UTC — Performance and safety of a multi-cancer early detection test: the PATHFINDER 2 study
    
    Link: https://www.nature.com/articles/s41591-026-04618-w
  - (medical study) [Stanford Medicine] 09/28/2026, 03:36 PM, +0000 UTC — Cutting ultra-processed food from school menus will be tricky, Stanford Medicine study finds
    
    Link: https://med.stanford.edu/news/all-news/2026/09/ultra-processed-school-food.html
  - (medical study) [Universities of Wisconsin] 09/24/2026, 02:22 PM, +0000 UTC — A deeper understanding: UWL students gain medical, cultural experience through Ecuador study abroad
    
    Link: https://www.wisconsin.edu/all-in-wisconsin/story/a-deeper-understanding-uwl-students-gain-medical-cultural-experience-through-ecuador-study-abroad/
  - (medical study) [medschool.umaryland.edu] 09/25/2026, 04:59 PM, +0000 UTC — 2026 News
    
    Link: https://www.medschool.umaryland.edu/news/2026/new-umsom-research-shows-promising-results-for-health-care-professionals-using-ketogenic-diet-therapy-to-treat-mental-illness.html
  - (medical study) [STAT] 09/23/2026, 10:19 PM, +0000 UTC — Nominee to lead FDA aims to speed up medical research, combat China’s rise
    
    Link: https://www.statnews.com/2026/09/23/heidi-overton-fda-nominee-opening-statement-senate-hearing-clinical-trials/
  - (medical study) [VA News (.gov)] 09/27/2026, 08:30 PM, +0000 UTC — From health research to healthcare
    
    Link: https://news.va.gov/149786/from-health-research-to-healthcare/
  - (medical study) [University of Cincinnati] 09/25/2026, 12:24 AM, +0000 UTC — UC hematology researcher to study bone complications in sickle cell disease
    
    Link: https://www.uc.edu/news/articles/2026/09/uc-hematologist-studies-bone-complications-in-sickle-cell-disease.html
  - (medical study) [ScienceDaily] 09/24/2026, 03:59 AM, +0000 UTC — More REM sleep linked to lower risk of 83 diseases
    
    Link: https://www.sciencedaily.com/releases/2026/09/260923035930.htm
  - (medical study) [NPR] 09/24/2026, 09:00 AM, +0000 UTC — These 6 charts show how NIH research funding has been reshaped under Trump
    
    Link: https://www.npr.org/2026/09/24/nx-s1-5931971/trump-nih-science-funding-disruptions-charts
  - (medical study) [MedPage Today] 09/24/2026, 05:33 PM, +0000 UTC — Is AI Flooding Medical Journals With 'Meaningless' Research?
    
    Link: https://www.medpagetoday.com/special-reports/features/123133
  - (medical study) [WVIR] 09/25/2026, 09:48 PM, +0000 UTC — Icarus Medical seeks adults with knee pain for new brace study
    
    Link: https://www.29news.com/2026/09/25/icarus-medical-seeks-adults-with-knee-pain-new-brace-study/
  - (medical study) [Mayo Clinic News Network] 09/22/2026, 09:30 PM, +0000 UTC — Multicancer blood test detects 17 cancer types in large prospective study
    
    Link: https://newsnetwork.mayoclinic.org/discussion/multicancer-blood-test-detects-17-cancer-types-in-large-prospective-study/
  - (clinical trial health) [nature.com] 09/25/2026, 10:49 AM, +0000 UTC — Does expansion of clinical trial capacity improve healthcare access?
    
    Link: https://www.nature.com/articles/s41591-026-04683-1
  - (clinical trial health) [Pfizer] 09/26/2026, 05:57 PM, +0000 UTC — How AI Is Helping Match Patients to Clinical Trials Faster
    
    Link: https://www.pfizer.com/news/articles/how_ai_is_helping_match_patients_to_clinical_trials_faster
  - (clinical trial health) [Word In Black] 09/22/2026, 08:15 PM, +0000 UTC — Black Patients Aren’t Avoiding Clinical Trials. They Often Aren’t Asked
    
    Link: https://wordinblack.com/2026/09/black-patients-arent-avoiding-clinical-trials-they-often-arent-asked/
  - (clinical trial health) [The Clinical Trial Vanguard] 09/26/2026, 07:28 AM, +0000 UTC — Platform Trials Are Rewriting the Rules of Evidence Generation. Regulators Haven’t Caught Up.
    
    Link: https://www.clinicaltrialvanguard.com/opinion/platform-trials-are-rewriting-the-rules-of-evidence-generation-regulators-havent-caught-up/
  - (clinical trial health) [St. Louis American] 09/29/2026, 12:00 PM, +0000 UTC — Black patients face barriers to clinical trials
    
    Link: https://www.stlamerican.com/your-health-matters/black-patients-face-barriers-to-clinical-trials/
  - (clinical trial health) [Fierce Healthcare] 09/24/2026, 11:00 AM, +0000 UTC — Oracle Health rolls out AI solutions for RCM, oncology as part of broader healthcare, life sciences strategy
    
    Link: https://www.fiercehealthcare.com/health-tech/oracle-health-ai-clinical-financial-research
  - (clinical trial health) [Rethinking Clinical Trials] 09/29/2026, 03:17 PM, +0000 UTC — September 29, 2026: Registration Opens for Pragmatic Trials Workshop at AcademyHealth–NIH Dissemination & Implementation Conference
    
    Link: https://rethinkingclinicaltrials.org/news/september-29-2026-registration-opens-for-pragmatic-trials-workshop-at-academyhealth-nih-dissemination-implementation-conference/
  - (clinical trial health) [UC San Diego Health] 09/22/2026, 08:45 PM, +0000 UTC — Doctor Faced with Cancer Diagnosis Honored by San Diego Padres
    
    Link: https://health.ucsd.edu/news/features/doctor-faced-with-cancer-diagnosis-honored-by-san-diego-padres/
  - (clinical trial health) [PR Newswire] 09/25/2026, 05:00 PM, +0000 UTC — BAYSTATE HEALTH ANNOUNCES PARTICIPATION IN NATIONAL CLINICAL TRIAL FOR ADVANCED BRAIN ANEURYSM TREATMENT
    
    Link: https://www.prnewswire.com/news-releases/baystate-health-announces-participation-in-national-clinical-trial-for-advanced-brain-aneurysm-treatment-302890409.html
  - (clinical trial health) [The Revelator] 09/25/2026, 02:00 PM, +0000 UTC — Climate Policy Has a Sacrifice Problem. My Clinical Trials Kept Solving It by Accident.
    
    Link: https://therevelator.org/climate-policy-diet/
  - (clinical trial health) [TMX Newsfile] 09/26/2026, 02:05 AM, +0000 UTC — Red Light Holland Highlights Publication of Randomized Clinical Trial Showing a Single Dose of Psilocybin Reduced Cocaine Use, with Filament Health Holding the Exclusive License to the Data and Intellectual Property
    
    Link: http://www.newsfilecorp.com/release/296623/Red-Light-Holland-Highlights-Publication-of-Randomized-Clinical-Trial-Showing-a-Single-Dose-of-Psilocybin-Reduced-Cocaine-Use-with-Filament-Health-Holding-the-Exclusive-License-to-the-Data-and-Intellectual-Property
  - (clinical trial health) [Medical Xpress] 09/25/2026, 04:40 PM, +0000 UTC — Radiotherapy after surgery significantly reduces atypical meningioma recurrence, clinical trial finds
    
    Link: https://medicalxpress.com/news/2026-09-radiotherapy-surgery-significantly-atypical-meningioma.html
  - (FDA recall health) [The Hill] 09/28/2026, 06:54 PM, +0000 UTC — Blood pressure medication recalled nationwide under FDA’s Class II risk level
    
    Link: https://thehill.com/homenews/6115677-blood-pressure-medication-recalled-nationwide-under-fdas-class-ii-risk-level/
  - (FDA recall health) [Good Housekeeping] 09/27/2026, 05:06 PM, +0000 UTC — FDA Announces New Nationwide Blood Pressure Medication Recall
    
    Link: https://www.goodhousekeeping.com/health/a73839435/fda-new-blood-pressure-medicine-recall/
  - (FDA recall health) [health.com] 09/24/2026, 04:34 PM, +0000 UTC — FDA Announces Recall on Blood Pressure Medication—More Than 13,000 Bottles Affected Nationwide
    
    Link: https://www.health.com/blood-pressure-medication-recall-september-2026-12138343
  - (FDA recall health) [USA Today] 09/25/2026, 03:16 PM, +0000 UTC — Thyroid medicine recall receives FDA's highest risk level
    
    Link: https://www.usatoday.com/story/money/consumer-protection/recalls-alerts/2026/09/24/thyroid-tablet-medicine-recall-fda/91916444007/
  - (FDA recall health) [cdc.gov] 09/25/2026, 10:00 PM, +0000 UTC — E. coli Outbreak Linked to Raw Milk Cheese
    
    Link: https://www.cdc.gov/ecoli/outbreaks/raw-milk-cheese-09-26/index.html
  - (FDA recall health) [newsnationnow.com] 09/24/2026, 06:11 PM, +0000 UTC — FDA elevates thyroid tablet recall to most serious level
    
    Link: https://www.newsnationnow.com/health/fda-thyroid-tablet-recall-class-i/
  - (FDA recall health) [FOX 13 Tampa Bay] 09/26/2026, 01:40 PM, +0000 UTC — Sugar recall: 1.7 million pounds recalled over possible allergens
    
    Link: https://www.fox13news.com/news/sugar-recall-1-7-million-pounds-recalled-over-possible-allergens
  - (FDA recall health) [NBC 5 Dallas-Fort Worth] 09/29/2026, 10:22 AM, +0000 UTC — FDA recalls more than 13k bottles of blood pressure medication after quality issue
    
    Link: https://www.nbcdfw.com/news/local/recall-alert-local/fda-recalls-more-than-13000-bottles-of-blood-pressure-medication-after-quality-issue/4083976/
  - (FDA recall health) [News4JAX] 09/28/2026, 08:15 PM, +0000 UTC — Thousands of bottles of blood pressure medication recalled nationwide
    
    Link: https://www.news4jax.com/news/local/2026/09/28/thousands-of-bottles-of-blood-pressure-medication-recalled-nationwide/
  - (FDA recall health) [LiveNOW from FOX] 09/24/2026, 07:52 PM, +0000 UTC — Thyroid medication recall upgraded to FDA's highest risk level
    
    Link: https://www.livenowfox.com/news/thyroid-medication-recall-vitruvias-therapeutics-class-i
  - (FDA recall health) [houstonchronicle.com] 09/28/2026, 04:26 PM, +0000 UTC — FDA updates recall of blood pressure medication with Class II risk level
    
    Link: https://www.houstonchronicle.com/news/houston-texas/trending/article/fda-class-ii-chlorthalidone-recall-22448678.php
  - (FDA recall health) [Dallas News] 09/28/2026, 11:10 PM, +0000 UTC — FDA recalls blood pressure medication after quality issue
    
    Link: https://www.dallasnews.com/news/public-health/article/chlorthalidone-blood-pressure-tablets-recalled-fda-22453633.php