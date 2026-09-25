# LIVE SIGNAL DATA — SerpAPI Pre-Fetch
The following signals were fetched from SerpAPI Google News and SerpAPI Google Trends immediately before this pipeline run. Treat Google Trends as AVAILABLE when this section contains a Google Trends block. Use it as the primary search_velocity input for Skills 01–05 (Signal Listener through Trend Strength Scorer). Use the Google News Radar as the broad discovery layer for news-led health topics, including topics that do not yet appear in Google Trends. Prioritize topics with convergence across News, Trends, primary/institutional sources, and credible publisher coverage.

## Google Trends — Trending Now (US / Health, real-time)
Terms with a "Why:" line have a confirmed real-world news story driving the spike; terms without one are a real-time signal only, not yet grounded in a specific story.
  - dengue fever
    Why: "Hillsborough County declares state of emergency as dengue fever cases reach 170" — WFLA
  - muscle
    Why: "Aging muscles may be losing strength for a reason scientists missed" — ScienceDaily

## Google Trends — 7-Day Interest (US)
  - **health**: latest=73, peak=100, 7d-delta=-8
    Rising related: darrell waltrip health, salem health, neko health, upperline health, health gadgets, health holiday, aca health insurance, medvi tirzepatide cost
  - **wellness**: latest=23, peak=100, 7d-delta=-3
    Rising related: kitchen tech upgrades, ai personal assistant, trending beauty hacks, viral tiktok trends, tech gadgets 2025, ai image enhancer, harmony wellness spa, non-toxic air fryer
  - **nutrition**: latest=67, peak=100, 7d-delta=-13
    Rising related: nutrition and sleep quality study, cheapest flights to tokyo, best time to visit maldives, how to bake a cake, how to make sushi, best laptop for work, top tourist attractions in paris, best pizza near me
  - **fitness**: latest=27, peak=100, 7d-delta=-4
    Rising related: cloud storage pricing, electric cars comparison, web hosting comparison, learn golang, air purifier review, dog training tips, best vpn service, digital marketing course
  - **food safety**: latest=17, peak=100, 7d-delta=-9
    Rising related: food safety violations tennessee valley, cheapest flights to tokyo, best time to visit maldives, best laptop for work, how to bake a cake, how to make sushi, top tourist attractions in paris, best pizza near me
  - **diet**: latest=70, peak=100, 7d-delta=-13
    Rising related: optimized mediterranean diet, paleolithic diet, 12 hour fasting diet fntkdiet, diet coke ghost blanket, ccho diet, diet coke, mediterranean diet, mediterranean
  - **weight loss**: latest=13, peak=100, 7d-delta=-4
    Rising related: outnet, what happened when dylan dreyer questioned craig melvin about weight loss on today, jb pritzker weight loss, elavate, loop earplugs coupon, healthletic, kelly clarkson weight loss, bubble io
  - **mental health**: latest=67, peak=100, 7d-delta=+5
    Rising related: presley gerber mental health, how to bake a cake, cheapest flights to tokyo, top tourist attractions in paris, best time to visit maldives, best laptop for work, did lizzie borden have mental health issues, lizzie borden mental health
  - **gut health**: latest=14, peak=100, 7d-delta=-4
    Rising related: lidl near me, cheapest flights to tokyo, maggie q gut health, holistic gut health doctor near me, signs of bad gut health, list of fermented foods for gut health, gut health and autism, the gut health md

Top rising related queries from Google Trends:
  - darrell waltrip health
  - salem health
  - neko health
  - upperline health
  - health gadgets
  - health holiday
  - aca health insurance
  - medvi tirzepatide cost
  - kitchen tech upgrades
  - ai personal assistant
  - trending beauty hacks
  - viral tiktok trends
  - tech gadgets 2025
  - ai image enhancer
  - harmony wellness spa
  - non-toxic air fryer
  - nutrition and sleep quality study
  - cheapest flights to tokyo
  - best time to visit maldives
  - how to bake a cake

## Google News Radar — Recent Health Topics (144 unique across 12 queries; showing 60)
Treat these headlines as the broad radar of news-led health topics. The Signal Listener must consider this radar before narrowing to retained candidates.
  - (health) [Centers for Disease Control and Prevention | CDC (.gov)] 09/21/2026, 11:07 PM, +0000 UTC — Youth Health in Focus
    
    Link: https://www.cdc.gov/yrbs/youth-health-in-focus/index.html
  - (health) [aphis.usda.gov] 09/21/2026, 07:00 AM, +0000 UTC — Screwworm.gov | Unified Government Response To Protect the United States
    
    Link: https://www.aphis.usda.gov/animals/animal-health/livestock-and-poultry-disease/stop-screwworm
  - (health) [blog.google] 09/24/2026, 05:07 PM, +0000 UTC — Our new health and safety tools are live in the Google Health app.
    
    Link: https://blog.google/products-and-platforms/products/google-health/health-guardian-features-live/
  - (health) [HHS.gov] 09/22/2026, 09:45 PM, +0000 UTC — Indian Health Service Awards $3.5 Million for Tribal Food and Nutrition Initiatives
    
    Link: https://www.hhs.gov/press-room/indian-health-service-awards-3-million-tribal-food-nutrition-initiatives.html
  - (health) [axios.com] 09/21/2026, 10:24 AM, +0000 UTC — Trump administration takes on mental health parity
    
    Link: https://www.axios.com/2026/09/21/mental-health-parity-trump-administration-rules
  - (health) [NPR] 09/24/2026, 05:14 AM, +0000 UTC — OpenAI's breach of Australian health department website prompts rebuke
    
    Link: https://www.npr.org/2026/09/24/g-s1-144835/openai-breach-australia
  - (health) [The New York Times] 09/22/2026, 07:00 AM, +0000 UTC — Dr. Anthony Robbins, Who Expanded Health Care for the Poor, Dies at 85
    
    Link: https://www.nytimes.com/2026/09/13/health/anthony-robbins-dead.html
  - (health) [The Washington Post] 09/20/2026, 07:18 PM, +0000 UTC — Even medical professionals are skipping health insurance because of high prices
    
    Link: https://www.washingtonpost.com/health/2026/09/21/even-medical-professionals-are-skipping-health-insurance-because-high-prices/
  - (health) [World Health Organization (WHO)] 09/21/2026, 08:19 AM, +0000 UTC — New WHO report calls for stronger ethics oversight of AI-related health research
    
    Link: https://www.who.int/news/item/21-09-2026-new-who-report-calls-for-stronger-ethics-oversight-of-ai-related-health-research
  - (health) [fortworthreport.org] 09/21/2026, 07:30 PM, +0000 UTC — New $13.5M Texas Health center coming near south Arlington
    
    Link: https://fortworthreport.org/2026/09/21/new-13-5m-texas-health-center-coming-near-south-arlington/
  - (health) [Nature] 09/22/2026, 10:07 AM, +0000 UTC — Why girls have worse mental health than boys
    
    Link: https://www.nature.com/articles/s41562-026-02577-3
  - (health) [PBS] 09/19/2026, 06:48 PM, +0000 UTC — Congo begins Ebola vaccinations for health workers in the epicenter of the outbreak
    
    Link: https://www.pbs.org/newshour/world/congo-begins-ebola-vaccinations-for-health-workers-in-the-epicenter-of-the-outbreak
  - (wellness) [The Washington Post] 09/20/2026, 05:00 PM, +0000 UTC — Guest Column | I’m a pulmonologist. Here’s why new wellness claims about nicotine worry me.
    
    Link: https://www.washingtonpost.com/health/2026/09/20/im-pulmonologist-heres-why-new-wellness-claims-about-nicotine-worry-me/
  - (wellness) [The Conversation] 09/22/2026, 12:47 PM, +0000 UTC — How the pro-nicotine ‘wellness’ movement rebranded an addictive drug
    
    Link: https://theconversation.com/how-the-pro-nicotine-wellness-movement-rebranded-an-addictive-drug-290129
  - (wellness) [WCAX] 09/24/2026, 08:18 PM, +0000 UTC — Police search Newport, N.H. wellness spa in human trafficking investigation
    
    Link: https://www.wcax.com/2026/09/24/police-search-newport-wellness-spa-human-trafficking-investigation/
  - (wellness) [Alaska Public Media] 09/22/2026, 10:42 PM, +0000 UTC — Haines to get $2.4M for community wellness initiative
    
    Link: https://alaskapublic.org/news/alaska-desk/2026-09-22/haines-to-get-2-4m-for-community-wellness-initiative
  - (wellness) [WBAL-TV] 09/24/2026, 04:45 PM, +0000 UTC — Events in Baltimore prioritize men's health & wellness
    
    Link: https://www.wbaltv.com/article/mens-health-wellness-events-baltimore/73871922
  - (wellness) [United States Coast Guard (.mil)] 09/22/2026, 03:20 PM, +0000 UTC — Welcome to the new CG Civilian Wellness EAP
    
    Link: https://www.mycg.uscg.mil/News/Article/4608297/welcome-to-the-new-cg-civilian-wellness-eap/
  - (wellness) [UC Davis College of Engineering] 09/23/2026, 10:35 PM, +0000 UTC — Adding Wellness to the Engineering Education Equation
    
    Link: https://engineering.ucdavis.edu/news/adding-wellness-engineering-education-equation
  - (wellness) [UW-Milwaukee] 09/22/2026, 08:00 PM, +0000 UTC — Four Reasons Why You Should Schedule a SHAW Wellness Visit – Student Health and Wellness Center
    
    Link: https://uwm.edu/wellness/four-reasons-why-you-should-schedule-a-shaw-wellness-visit/
  - (wellness) [Marquette Today] 09/23/2026, 02:14 PM, +0000 UTC — Sync fitness tracker to automatically earn My Wellness points throughout the year
    
    Link: https://today.marquette.edu/2026/09/sync-fitness-tracker-to-automatically-earn-my-wellness-points-throughout-the-year/
  - (wellness) [bop.gov] 09/21/2026, 07:00 AM, +0000 UTC — Suicide Prevention, Wellness and Support
    
    Link: https://www.bop.gov/news/20260921-video-message-from-the-director-suicide-prevention-welln.jsp
  - (wellness) [Happily Eva After] 09/23/2026, 08:03 AM, +0000 UTC — My Family Wellness Strategies
    
    Link: https://happilyevaafter.com/my-family-wellness-strategies/
  - (wellness) [Dartmouth] 09/23/2026, 07:27 PM, +0000 UTC — Teevens Center Expands Role in Student Wellness
    
    Link: https://home.dartmouth.edu/news/2026/09/teevens-center-expands-role-student-wellness
  - (medical study) [Nature] 09/22/2026, 09:28 PM, +0000 UTC — Performance and safety of a multi-cancer early detection test: the PATHFINDER 2 study
    
    Link: https://www.nature.com/articles/s41591-026-04618-w
  - (medical study) [The New York Times] 09/22/2026, 05:02 PM, +0000 UTC — GLP-1 Prescriptions for People With No Medical Need Are Climbing
    
    Link: https://www.nytimes.com/2026/09/22/well/ozempic-glp1-medical-reason.html
  - (medical study) [Keck Medicine of USC] 09/21/2026, 09:00 PM, +0000 UTC — U.S. alcohol use falls for first time since the COVID-19 pandemic, but remains above pre-pandemic levels
    
    Link: https://news.keckmedicine.org/us-alcohol-use-falls-for-first-time-since-the-covid-19-pandemic-but-remains-above-pre-pandemic-levels/
  - (medical study) [Universities of Wisconsin] 09/24/2026, 02:22 PM, +0000 UTC — A deeper understanding: UWL students gain medical, cultural experience through Ecuador study abroad
    
    Link: https://www.wisconsin.edu/all-in-wisconsin/story/a-deeper-understanding-uwl-students-gain-medical-cultural-experience-through-ecuador-study-abroad/
  - (medical study) [YaleNews] 09/18/2026, 06:19 PM, +0000 UTC — Study links soaring health care spending to higher insurance premiums
    
    Link: https://news.yale.edu/2026/09/18/study-links-soaring-health-care-spending-higher-insurance-premiums
  - (medical study) [Stanford Medicine] 09/22/2026, 04:11 PM, +0000 UTC — Bone marrow transplants offer surprising way to treat mitochondrial disease, Stanford Medicine study shows
    
    Link: https://med.stanford.edu/news/all-news/2026/09/stem-cell-mitochondrial-disease.html
  - (medical study) [University of Utah Health Academic Medical Center] 09/23/2026, 04:10 PM, +0000 UTC — Helping Faculty Turn Teaching Questions Into Medical Education Research
    
    Link: https://uofuhealth.utah.edu/notes/2026/09/helping-faculty-turn-teaching-questions-medical-education-research
  - (medical study) [Mayo Clinic News Network] 09/22/2026, 09:30 PM, +0000 UTC — Multicancer blood test detects 17 cancer types in large prospective study
    
    Link: https://newsnetwork.mayoclinic.org/discussion/multicancer-blood-test-detects-17-cancer-types-in-large-prospective-study/
  - (medical study) [ScienceDaily] 09/24/2026, 03:59 AM, +0000 UTC — More REM sleep linked to lower risk of 83 diseases
    
    Link: https://www.sciencedaily.com/releases/2026/09/260923035930.htm
  - (medical study) [STAT] 09/23/2026, 10:19 PM, +0000 UTC — Nominee to lead FDA aims to speed up medical research, combat China’s rise
    
    Link: https://www.statnews.com/2026/09/23/heidi-overton-fda-nominee-opening-statement-senate-hearing-clinical-trials/
  - (medical study) [Research Horizons] 09/23/2026, 11:29 PM, +0000 UTC — Earlier HCT Improves Survival for Youth with Shwachman-Diamond Syndrome
    
    Link: https://scienceblog.cincinnatichildrens.org/earlier-hct-improves-survival-for-youth-with-shwachman-diamond-syndrome/
  - (medical study) [news-medical.net] 09/25/2026, 12:01 PM, +0000 UTC — Study explains how stroke promotes aggressive glioma tumor growth
    
    Link: https://www.news-medical.net/news/20260925/Study-explains-how-stroke-promotes-aggressive-glioma-tumor-growth.aspx
  - (clinical trial health) [Pfizer] 09/23/2026, 08:07 PM, +0000 UTC — How AI Is Helping Match Patients to Clinical Trials Faster
    
    Link: https://www.pfizer.com/news/articles/how_ai_is_helping_match_patients_to_clinical_trials_faster
  - (clinical trial health) [The Clinical Trial Vanguard] 09/24/2026, 07:53 AM, +0000 UTC — Scaling Clinical AI to One Million Patients Taught Us Things No Pilot Study Could
    
    Link: https://www.clinicaltrialvanguard.com/article/intel-brief/scaling-clinical-ai-to-one-million-patients-taught-us-things-no-pilot-study-could/
  - (clinical trial health) [University of Miami] 09/24/2026, 06:07 PM, +0000 UTC — Breaking Barriers to Cancer Clinical Trial Participation
    
    Link: https://news.med.miami.edu/cancer-clinical-trial-access-barriers/
  - (clinical trial health) [STAT] 09/21/2026, 08:33 AM, +0000 UTC — ClinicalTrials.gov needs a pregnancy and lactation checkbox
    
    Link: https://www.statnews.com/2026/09/21/clinical-trials-website-pregnant-lactating-patients-checkbox/
  - (clinical trial health) [Stock Titan] 09/22/2026, 10:00 AM, +0000 UTC — A new clinical trial platform is backed by 5 million+ annual patient visits
    
    Link: https://www.stocktitan.net/news/WHTCF/well-health-launches-well-research-an-end-to-end-clinical-trial-btdgvwgbp3pt.html
  - (clinical trial health) [Word In Black] 09/22/2026, 08:15 PM, +0000 UTC — Black Patients Aren’t Avoiding Clinical Trials. They Often Aren’t Asked
    
    Link: https://wordinblack.com/2026/09/black-patients-arent-avoiding-clinical-trials-they-often-arent-asked/
  - (clinical trial health) [reflector.com] 09/23/2026, 01:00 PM, +0000 UTC — Free health screenings, clinical trial set
    
    Link: https://www.reflector.com/enterprise/news/local/free-health-screenings-clinical-trial-set/article_edcd6989-3acb-46f5-aae1-a2ee15946c17.html
  - (clinical trial health) [UC San Diego Health] 09/22/2026, 08:45 PM, +0000 UTC — Doctor Faced with Cancer Diagnosis Honored by San Diego Padres
    
    Link: https://health.ucsd.edu/news/features/doctor-faced-with-cancer-diagnosis-honored-by-san-diego-padres/
  - (clinical trial health) [Fierce Healthcare] 09/24/2026, 11:00 AM, +0000 UTC — Oracle Health rolls out AI solutions for RCM, oncology as part of broader healthcare, life sciences strategy
    
    Link: https://www.fiercehealthcare.com/health-tech/oracle-health-ai-clinical-financial-research
  - (clinical trial health) [UMass Chan Medical School] 09/22/2026, 03:07 PM, +0000 UTC — U.S. Rep. Jake Auchincloss visits UMass Chan to discuss research funding cuts, point-of-care clinical trials
    
    Link: https://www.umassmed.edu/news/articles/2026/09/u.s.-rep.-jake-auchincloss-visits-umass-chan-to-discuss-research-funding-cuts-point-of-care-clinical-trials
  - (clinical trial health) [PR Newswire] 09/24/2026, 04:33 PM, +0000 UTC — Cedar Health Research Appoints Jody Staggs Chief Executive Officer
    
    Link: https://www.prnewswire.com/news-releases/cedar-health-research-appoints-jody-staggs-chief-executive-officer-302889543.html
  - (clinical trial health) [ABC News - Breaking News, Latest News and Videos] 09/24/2026, 05:28 PM, +0000 UTC — Moderna begins Phase 1 clinical trial of Ebola vaccine against strain behind DRC outbreak
    
    Link: https://abcnews.com/Health/moderna-begins-phase-1-clinical-trial-ebola-vaccine/story?id=135365177
  - (FDA recall health) [USA Today] 09/25/2026, 03:16 PM, +0000 UTC — Thyroid medicine recall receives FDA's highest risk level
    
    Link: https://www.usatoday.com/story/money/consumer-protection/recalls-alerts/2026/09/24/thyroid-tablet-medicine-recall-fda/91916444007/
  - (FDA recall health) [LiveNOW from FOX] 09/24/2026, 07:52 PM, +0000 UTC — Thyroid medication recall upgraded to FDA's highest risk level
    
    Link: https://www.livenowfox.com/news/thyroid-medication-recall-vitruvias-therapeutics-class-i
  - (FDA recall health) [WBAL-TV] 09/24/2026, 05:17 PM, +0000 UTC — Thyroid medication recall elevated to FDA's highest risk level
    
    Link: https://www.wbaltv.com/article/thyroid-medication-recalled-superpotent-fda-risk-level/73871943
  - (FDA recall health) [health.com] 09/24/2026, 04:34 PM, +0000 UTC — FDA Announces Recall on Blood Pressure Medication—More Than 13,000 Bottles Affected Nationwide
    
    Link: https://www.health.com/blood-pressure-medication-recall-september-2026-12138343
  - (FDA recall health) [Dallas News] 09/24/2026, 03:04 PM, +0000 UTC — H-E-B jalapeño products recalled over salmonella risk receive FDA’s highest risk classification
    
    Link: https://www.dallasnews.com/news/public-health/article/h-e-b-jalape-o-recall-receives-fda-s-highest-22447175.php
  - (FDA recall health) [newsnationnow.com] 09/24/2026, 06:11 PM, +0000 UTC — FDA elevates thyroid tablet recall to most serious level
    
    Link: https://www.newsnationnow.com/health/fda-thyroid-tablet-recall-class-i/
  - (FDA recall health) [Yahoo] 09/19/2026, 01:53 PM, +0000 UTC — FDA assigns Class II warning to hand soaps recalled in 15 states over bacteria risk
    
    Link: https://www.yahoo.com/news/us/articles/fda-assigns-class-ii-warning-135300851.html
  - (FDA recall health) [Houston Chronicle] 09/24/2026, 04:59 PM, +0000 UTC — FDA issues top risk warning on recalled 'super potent' thyroid drug
    
    Link: https://www.houstonchronicle.com/news/houston-texas/trending/article/recall-thyroid-medication-fda-warning-22447248.php
  - (FDA recall health) [ABC News - Breaking News, Latest News and Videos] 09/25/2026, 08:15 AM, +0000 UTC — Egg recall linked to salmonella upgraded to highest risk level by FDA
    
    Link: https://abcnews.com/GMA/Food/19-million-eggs-voluntarily-recalled-potential-salmonella-contamination/story?id=135028861
  - (FDA recall health) [TODAY.com] 09/25/2026, 02:58 PM, +0000 UTC — Over 160,000 Pounds of Meat Recalled Due to Lack of Inspection, Receives Highest Risk Level From USDA
    
    Link: https://www.today.com/health/recall/massive-meat-recall-usda-inspection-false-label-rcna599435
  - (FDA recall health) [MedShadow Foundation] 09/21/2026, 10:39 PM, +0000 UTC — FDA Recalls and Warnings: Third Glutathione Recall Issued Over Endotoxin Contamination
    
    Link: https://medshadow.org/drug-updates-recalls/fda-recalls-and-warnings/third-glutathione-injection-recall-endotoxin-contamination/
  - (FDA recall health) [Today's Medical Developments] 09/24/2026, 06:00 AM, +0000 UTC — Artificial intelligence could reduce medical device recalls, study suggests
    
    Link: https://www.todaysmedicaldevelopments.com/news/artificial-intelligence-could-reduce-medical-device-recalls-study-suggests/