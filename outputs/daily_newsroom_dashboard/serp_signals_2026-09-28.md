# LIVE SIGNAL DATA — SerpAPI Pre-Fetch
The following signals were fetched from SerpAPI Google News and SerpAPI Google Trends immediately before this pipeline run. Treat Google Trends as AVAILABLE when this section contains a Google Trends block. Use it as the primary search_velocity input for Skills 01–05 (Signal Listener through Trend Strength Scorer). Use the Google News Radar as the broad discovery layer for news-led health topics, including topics that do not yet appear in Google Trends. Prioritize topics with convergence across News, Trends, primary/institutional sources, and credible publisher coverage.

## Google Trends — Trending Now (US / Health, real-time)
Terms with a "Why:" line have a confirmed real-world news story driving the spike; terms without one are a real-time signal only, not yet grounded in a specific story.
  - fda chlorthalidone dissolution testing recall
    Why: "FDA Announces New Nationwide Blood Pressure Medication Recall" — Good Housekeeping

## Google Trends — 7-Day Interest (US)
  - **health**: latest=99, peak=100, 7d-delta=+3
    Rising related: darrell waltrip health, neko health, salem health, health insurance agency, health care fraud, mental health, health insurance, health department
  - **wellness**: latest=28, peak=100, 7d-delta=+3
    Rising related: kitchen tech upgrades, wellness olympia, spacecamp wellness, tech gadgets 2025, wags and wellness austin, ai image enhancer, digital side hustles, streaming shows trending
  - **nutrition**: latest=78, peak=100, 7d-delta=+0
    Rising related: nutrition and sleep quality study, costco churro nutrition, cocoa pebbles nutrition facts, fitness nutrition twspoondietary, bowmar nutrition, best laptop for work, delicata squash nutrition, nutrition guide fparentips
  - **fitness**: latest=19, peak=100, 7d-delta=+3
    Rising related: online banking review, standing desk review, diy home renovation, moving company quotes, baby stroller review, tax software comparison, camping gear essentials, organic skincare products
  - **food safety**: latest=39, peak=100, 7d-delta=-21
    Rising related: food safety violations tennessee valley, food safety certification nyc, how to make sushi, food safety temperature chart, what does fifo stand for in food safety, how to bake a cake, best laptop for work, king county food safety rating
  - **diet**: latest=83, peak=100, 7d-delta=-12
    Rising related: 12 hour fasting diet fntkdiet, diet coke, mediterranean diet, healthy diet, science diet, keto diet, liquid diet, carnivore diet
  - **weight loss**: latest=17, peak=100, 7d-delta=-8
    Rising related: what happened when dylan dreyer questioned craig melvin about weight loss on today, zion williamson weight loss, jb pritzker, pritzker weight loss, jb pritzker weight loss, jb pritzker weight loss before and after, lili reinhart weight loss, john goodman weight loss
  - **mental health**: latest=70, peak=100, 7d-delta=-5
    Rising related: ted kaczynski mental health, pilot mental health bill, john a. hauser mental health in aviation act, unabomber mental health, mental health in aviation act, moccasin bend mental health institute, cheapest flights to tokyo, presley gerber mental health
  - **gut health**: latest=0, peak=100, 7d-delta=-51
    Rising related: best fermented foods for gut health, gut health specialist near me, list of fermented foods for gut health, fiber rich foods, top tourist attractions in paris, fermented foods for gut health, best probiotic for gut health and bloating, worst foods for gut health

Top rising related queries from Google Trends:
  - darrell waltrip health
  - neko health
  - salem health
  - health insurance agency
  - health care fraud
  - mental health
  - health insurance
  - health department
  - kitchen tech upgrades
  - wellness olympia
  - spacecamp wellness
  - tech gadgets 2025
  - wags and wellness austin
  - ai image enhancer
  - digital side hustles
  - streaming shows trending
  - nutrition and sleep quality study
  - costco churro nutrition
  - cocoa pebbles nutrition facts
  - fitness nutrition twspoondietary

## Google News Radar — Recent Health Topics (144 unique across 12 queries; showing 60)
Treat these headlines as the broad radar of news-led health topics. The Signal Listener must consider this radar before narrowing to retained candidates.
  - (health) [Centers for Disease Control and Prevention | CDC (.gov)] 09/21/2026, 11:07 PM, +0000 UTC — Youth Health in Focus
    
    Link: https://www.cdc.gov/yrbs/youth-health-in-focus/index.html
  - (health) [blog.google] 09/24/2026, 05:07 PM, +0000 UTC — Our new health and safety tools are live in the Google Health app.
    
    Link: https://blog.google/products-and-platforms/products/google-health/health-guardian-features-live/
  - (health) [Department of Justice (.gov)] 09/25/2026, 04:15 PM, +0000 UTC — Texas Mental Health Clinic Owner Convicted in $26M Scheme to Defraud Military Health Benefits Program
    
    Link: https://www.justice.gov/opa/pr/texas-mental-health-clinic-owner-convicted-26m-scheme-defraud-military-health-benefits
  - (health) [HHS.gov] 09/22/2026, 09:45 PM, +0000 UTC — Indian Health Service Awards $3.5 Million for Tribal Food and Nutrition Initiatives
    
    Link: https://www.hhs.gov/press-room/indian-health-service-awards-3-million-tribal-food-nutrition-initiatives.html
  - (health) [Virginia Department of Health (.gov)] 09/22/2026, 07:00 AM, +0000 UTC — Food Regulations Update 2026
    
    Link: https://www.vdh.virginia.gov/environmental-health/food-safety-in-virginia/food-regulations-update-2026/
  - (health) [NPR] 09/24/2026, 05:14 AM, +0000 UTC — OpenAI's breach of Australian health department website prompts rebuke
    
    Link: https://www.npr.org/2026/09/24/g-s1-144835/openai-breach-australia
  - (health) [ALPA] 09/25/2026, 02:47 PM, +0000 UTC — Pilot-Backed Mental Health Reforms Clear Senate
    
    Link: https://www.alpa.org/press-room/2026/09/pilot-backed-mental-health-reforms-clear-senate
  - (health) [aphis.usda.gov] 09/23/2026, 07:00 AM, +0000 UTC — Current Status of New World Screwworm | Screwworm.gov
    
    Link: https://www.aphis.usda.gov/animals/animal-health/livestock-and-poultry-disease/stop-screwworm/current-status
  - (health) [PBS] 09/25/2026, 10:35 PM, +0000 UTC — Health care costs a major concern for voters ahead of midterms
    
    Link: https://www.pbs.org/newshour/show/health-care-costs-a-major-concern-for-voters-ahead-of-midterms
  - (health) [The New York Times] 09/22/2026, 07:00 AM, +0000 UTC — Dr. Anthony Robbins, Who Expanded Health Care for the Poor, Dies at 85
    
    Link: https://www.nytimes.com/2026/09/13/health/anthony-robbins-dead.html
  - (health) [Fort Worth Report] 09/21/2026, 07:30 PM, +0000 UTC — New $13.5M Texas Health center coming near south Arlington
    
    Link: https://fortworthreport.org/2026/09/21/new-13-5m-texas-health-center-coming-near-south-arlington/
  - (health) [Reuters] 09/25/2026, 07:13 PM, +0000 UTC — Senate approves mental health legislation for US pilots, air traffic controllers
    
    Link: https://www.reuters.com/business/healthcare-pharmaceuticals/us-senate-approves-legislation-address-pilot-air-traffic-control-mental-health-2026-09-25/
  - (wellness) [theconversation.com] 09/22/2026, 12:47 PM, +0000 UTC — How the pro-nicotine ‘wellness’ movement rebranded an addictive drug
    
    Link: https://theconversation.com/how-the-pro-nicotine-wellness-movement-rebranded-an-addictive-drug-290129
  - (wellness) [WCAX] 09/24/2026, 08:18 PM, +0000 UTC — Police search Newport, N.H. wellness spa in human trafficking investigation
    
    Link: https://www.wcax.com/2026/09/24/police-search-newport-wellness-spa-human-trafficking-investigation/
  - (wellness) [WBAL-TV] 09/24/2026, 04:45 PM, +0000 UTC — Events in Baltimore prioritize men's health & wellness
    
    Link: https://www.wbaltv.com/article/mens-health-wellness-events-baltimore/73871922
  - (wellness) [Congresswoman Young Kim (.gov)] 09/25/2026, 05:58 PM, +0000 UTC — Rep. Young Kim Introduces Resolution Supporting Children’s Emotional Wellness
    
    Link: https://youngkim.house.gov/2026/09/25/rep-young-kim-introduces-resolution-supporting-childrens-emotional-wellness/
  - (wellness) [Dartmouth] 09/23/2026, 07:27 PM, +0000 UTC — Teevens Center Expands Role in Student Wellness
    
    Link: https://home.dartmouth.edu/news/2026/09/teevens-center-expands-role-student-wellness
  - (wellness) [today.marquette.edu] 09/23/2026, 02:14 PM, +0000 UTC — Sync fitness tracker to automatically earn My Wellness points throughout the year
    
    Link: https://today.marquette.edu/2026/09/sync-fitness-tracker-to-automatically-earn-my-wellness-points-throughout-the-year/
  - (wellness) [Happily Eva After] 09/23/2026, 08:03 AM, +0000 UTC — My Family Wellness Strategies
    
    Link: https://happilyevaafter.com/my-family-wellness-strategies/
  - (wellness) [legion.org] 09/28/2026, 11:46 AM, +0000 UTC — Be the One focus of motorcycle ride, community wellness fair
    
    Link: https://www.legion.org/information-center/news/riders/2026/september/be-the-one-focus-of-motorcycle-ride-community-wellness-fair
  - (wellness) [UAMS News] 09/28/2026, 03:30 PM, +0000 UTC — UAMS-Sponsored Health & Wellness Expo Offers Free Screenings, Other Resources
    
    Link: https://news.uams.edu/2026/09/28/uams-sponsored-health-wellness-expo-offers-free-screenings-other-resources/
  - (wellness) [University of North Carolina Wilmington | UNCW] 09/25/2026, 10:55 PM, +0000 UTC — Ncflex Miles For Wellness Challenge # 34
    
    Link: https://www.uncw.edu/news/administrative-units/human-resources/2026/09/ncflex-miles-for-wellness-challenge-34.html
  - (wellness) [Carthage College] 09/23/2026, 07:00 AM, +0000 UTC — Attend the Carthage Wellness Fair Sept. 30
    
    Link: https://www.carthage.edu/live/news/58021-attend-the-carthage-wellness-fair-sept-30
  - (wellness) [Case Western Reserve University] 09/23/2026, 11:00 AM, +0000 UTC — Save the date for the Benefits & Wellness Fair at CWRU
    
    Link: https://case.edu/news/save-date-benefits-wellness-fair-cwru
  - (medical study) [Stanford Medicine] 09/22/2026, 04:11 PM, +0000 UTC — Bone marrow transplants offer surprising way to treat mitochondrial disease, Stanford Medicine study shows
    
    Link: https://med.stanford.edu/news/all-news/2026/09/stem-cell-mitochondrial-disease.html
  - (medical study) [Nature] 09/22/2026, 09:28 PM, +0000 UTC — Performance and safety of a multi-cancer early detection test: the PATHFINDER 2 study
    
    Link: https://www.nature.com/articles/s41591-026-04618-w
  - (medical study) [Keck Medicine of USC] 09/21/2026, 09:00 PM, +0000 UTC — U.S. alcohol use falls for first time since the COVID-19 pandemic, but remains above pre-pandemic levels
    
    Link: https://news.keckmedicine.org/us-alcohol-use-falls-for-first-time-since-the-covid-19-pandemic-but-remains-above-pre-pandemic-levels/
  - (medical study) [The New York Times] 09/22/2026, 05:02 PM, +0000 UTC — GLP-1 Prescriptions for People With No Medical Need Are Climbing
    
    Link: https://www.nytimes.com/2026/09/22/well/ozempic-glp1-medical-reason.html
  - (medical study) [wisconsin.edu] 09/24/2026, 02:22 PM, +0000 UTC — A deeper understanding: UWL students gain medical, cultural experience through Ecuador study abroad
    
    Link: https://www.wisconsin.edu/all-in-wisconsin/story/a-deeper-understanding-uwl-students-gain-medical-cultural-experience-through-ecuador-study-abroad/
  - (medical study) [School of Medicine | University of Utah] 09/22/2026, 07:40 PM, +0000 UTC — A Summer of Discovery: Recapping Our 2026 FAER Medical Student Research Fellows
    
    Link: https://medicine.utah.edu/anesthesiology/news/2026/09/summer-of-discovery-recapping-our-2026-faer-medical-student-research
  - (medical study) [News-Medical] 09/28/2026, 08:47 AM, +0000 UTC — Study links insomnia to higher stroke and hospitalization risks
    
    Link: https://www.news-medical.net/news/20260928/Study-links-insomnia-to-higher-stroke-and-hospitalization-risks.aspx
  - (medical study) [STAT] 09/23/2026, 10:19 PM, +0000 UTC — Nominee to lead FDA aims to speed up medical research, combat China’s rise
    
    Link: https://www.statnews.com/2026/09/23/heidi-overton-fda-nominee-opening-statement-senate-hearing-clinical-trials/
  - (medical study) [VA News (.gov)] 09/27/2026, 08:30 PM, +0000 UTC — From health research to healthcare
    
    Link: https://news.va.gov/149786/from-health-research-to-healthcare/
  - (medical study) [ScienceDaily] 09/24/2026, 03:59 AM, +0000 UTC — More REM sleep linked to lower risk of 83 diseases
    
    Link: https://www.sciencedaily.com/releases/2026/09/260923035930.htm
  - (medical study) [University of Cincinnati] 09/25/2026, 12:24 AM, +0000 UTC — UC hematology researcher to study bone complications in sickle cell disease
    
    Link: https://www.uc.edu/news/articles/2026/09/uc-hematologist-studies-bone-complications-in-sickle-cell-disease.html
  - (medical study) [MedPage Today] 09/24/2026, 05:33 PM, +0000 UTC — Is AI Flooding Medical Journals With 'Meaningless' Research?
    
    Link: https://www.medpagetoday.com/special-reports/features/123133
  - (clinical trial health) [Nature] 09/25/2026, 10:49 AM, +0000 UTC — Does expansion of clinical trial capacity improve healthcare access?
    
    Link: https://www.nature.com/articles/s41591-026-04683-1
  - (clinical trial health) [The Clinical Trial Vanguard] 09/24/2026, 07:53 AM, +0000 UTC — Scaling Clinical AI to One Million Patients Taught Us Things No Pilot Study Could
    
    Link: https://www.clinicaltrialvanguard.com/article/intel-brief/scaling-clinical-ai-to-one-million-patients-taught-us-things-no-pilot-study-could/
  - (clinical trial health) [Pfizer] 09/26/2026, 05:57 PM, +0000 UTC — How AI Is Helping Match Patients to Clinical Trials Faster
    
    Link: https://www.pfizer.com/news/articles/how_ai_is_helping_match_patients_to_clinical_trials_faster
  - (clinical trial health) [Word In Black] 09/22/2026, 08:15 PM, +0000 UTC — Black Patients Aren’t Avoiding Clinical Trials. They Often Aren’t Asked
    
    Link: https://wordinblack.com/2026/09/black-patients-arent-avoiding-clinical-trials-they-often-arent-asked/
  - (clinical trial health) [Stock Titan] 09/22/2026, 10:00 AM, +0000 UTC — A new clinical trial platform is backed by 5 million+ annual patient visits
    
    Link: https://www.stocktitan.net/news/WHTCF/well-health-launches-well-research-an-end-to-end-clinical-trial-btdgvwgbp3pt.html
  - (clinical trial health) [Fierce Healthcare] 09/24/2026, 11:00 AM, +0000 UTC — Oracle Health rolls out AI solutions for RCM, oncology as part of broader healthcare, life sciences strategy
    
    Link: https://www.fiercehealthcare.com/health-tech/oracle-health-ai-clinical-financial-research
  - (clinical trial health) [PR Newswire] 09/25/2026, 05:00 PM, +0000 UTC — BAYSTATE HEALTH ANNOUNCES PARTICIPATION IN NATIONAL CLINICAL TRIAL FOR ADVANCED BRAIN ANEURYSM TREATMENT
    
    Link: https://www.prnewswire.com/news-releases/baystate-health-announces-participation-in-national-clinical-trial-for-advanced-brain-aneurysm-treatment-302890409.html
  - (clinical trial health) [UC San Diego Health] 09/22/2026, 08:45 PM, +0000 UTC — Doctor Faced with Cancer Diagnosis Honored by San Diego Padres
    
    Link: https://health.ucsd.edu/news/features/doctor-faced-with-cancer-diagnosis-honored-by-san-diego-padres/
  - (clinical trial health) [UMass Chan Medical School] 09/22/2026, 03:07 PM, +0000 UTC — U.S. Rep. Jake Auchincloss visits UMass Chan to discuss research funding cuts, point-of-care clinical trials
    
    Link: https://www.umassmed.edu/news/articles/2026/09/u.s.-rep.-jake-auchincloss-visits-umass-chan-to-discuss-research-funding-cuts-point-of-care-clinical-trials
  - (clinical trial health) [Yahoo Finance] 09/25/2026, 09:45 PM, +0000 UTC — Global Clinical Trials Market to Reach USD 99.4 Bn. by 2034 at 6.13% CAGR as Personalized Medicine, Decentralized Trials, AI Integration, and Rising Biopharmaceutical R&D Accelerate Market Growth, Reports Maximize Market Research
    
    Link: https://finance.yahoo.com/healthcare/articles/global-clinical-trials-market-reach-214500175.html
  - (clinical trial health) [Medical Xpress] 09/25/2026, 04:40 PM, +0000 UTC — Radiotherapy after surgery significantly reduces atypical meningioma recurrence, clinical trial finds
    
    Link: https://medicalxpress.com/news/2026-09-radiotherapy-surgery-significantly-atypical-meningioma.html
  - (clinical trial health) [The Revelator] 09/25/2026, 02:00 PM, +0000 UTC — Climate Policy Has a Sacrifice Problem. My Clinical Trials Kept Solving It by Accident.
    
    Link: https://therevelator.org/climate-policy-diet/
  - (FDA recall health) [Good Housekeeping] 09/27/2026, 05:06 PM, +0000 UTC — FDA Announces New Nationwide Blood Pressure Medication Recall
    
    Link: https://www.goodhousekeeping.com/health/a73839435/fda-new-blood-pressure-medicine-recall/
  - (FDA recall health) [WBAL-TV] 09/24/2026, 05:17 PM, +0000 UTC — Thyroid medication recall elevated to FDA's highest risk level
    
    Link: https://www.wbaltv.com/article/thyroid-medication-recalled-superpotent-fda-risk-level/73871943
  - (FDA recall health) [health.com] 09/24/2026, 04:34 PM, +0000 UTC — FDA Announces Recall on Blood Pressure Medication—More Than 13,000 Bottles Affected Nationwide
    
    Link: https://www.health.com/blood-pressure-medication-recall-september-2026-12138343
  - (FDA recall health) [USA Today] 09/25/2026, 03:16 PM, +0000 UTC — Thyroid medicine recall receives FDA's highest risk level
    
    Link: https://www.usatoday.com/story/money/consumer-protection/recalls-alerts/2026/09/24/thyroid-tablet-medicine-recall-fda/91916444007/
  - (FDA recall health) [NewsNation] 09/24/2026, 06:11 PM, +0000 UTC — FDA elevates thyroid tablet recall to most serious level
    
    Link: https://www.newsnationnow.com/health/fda-thyroid-tablet-recall-class-i/
  - (FDA recall health) [Dallas News] 09/24/2026, 03:04 PM, +0000 UTC — H-E-B jalapeño products recalled over salmonella risk receive FDA’s highest risk classification
    
    Link: https://www.dallasnews.com/news/public-health/article/h-e-b-jalape-o-recall-receives-fda-s-highest-22447175.php
  - (FDA recall health) [LiveNOW from FOX] 09/24/2026, 07:52 PM, +0000 UTC — Thyroid medication recall upgraded to FDA's highest risk level
    
    Link: https://www.livenowfox.com/news/thyroid-medication-recall-vitruvias-therapeutics-class-i
  - (FDA recall health) [Houston Chronicle] 09/24/2026, 04:59 PM, +0000 UTC — FDA issues top risk warning on recalled 'super potent' thyroid drug
    
    Link: https://www.houstonchronicle.com/news/houston-texas/trending/article/recall-thyroid-medication-fda-warning-22447248.php
  - (FDA recall health) [WUSA9] 09/28/2026, 02:59 PM, +0000 UTC — Blood pressure medication recalled nationwide after failing FDA dissolution testing
    
    Link: https://www.wusa9.com/article/news/nation-world/blood-pressure-medication-recall/507-756358e0-3933-4870-a1f6-5f25d9512046
  - (FDA recall health) [EatingWell] 09/25/2026, 08:51 PM, +0000 UTC — The FDA Recalls Cinnamon Due to Elevated Lead Levels
    
    Link: https://www.eatingwell.com/cinnamon-recall-elevated-lead-levels-12141002
  - (FDA recall health) [NBC 5 Chicago] 09/25/2026, 08:10 PM, +0000 UTC — ‘Superpotent': Thyroid tablet recall upgraded to highest risk level by FDA
    
    Link: https://www.nbcchicago.com/news/local/superpotent-thyroid-tablet-recall-upgraded-to-highest-risk-level-by-fda/3993840/
  - (FDA recall health) [Newsweek] 09/26/2026, 04:22 PM, +0000 UTC — Map Shows States Hit by 1.7M-Pound Sugar Recall as FDA Sets Risk Level
    
    Link: https://www.newsweek.com/fda-class-ii-risk-level-1-7-million-pound-sugar-recall-wheat-allergen-12492685