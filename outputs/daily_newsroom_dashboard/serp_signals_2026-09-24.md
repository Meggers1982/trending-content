# LIVE SIGNAL DATA — SerpAPI Pre-Fetch
The following signals were fetched from SerpAPI Google News and SerpAPI Google Trends immediately before this pipeline run. Treat Google Trends as AVAILABLE when this section contains a Google Trends block. Use it as the primary search_velocity input for Skills 01–05 (Signal Listener through Trend Strength Scorer). Use the Google News Radar as the broad discovery layer for news-led health topics, including topics that do not yet appear in Google Trends. Prioritize topics with convergence across News, Trends, primary/institutional sources, and credible publisher coverage.

## Google Trends — Trending Now (US / Health, real-time)
Terms with a "Why:" line have a confirmed real-world news story driving the spike; terms without one are a real-time signal only, not yet grounded in a specific story.
  - vitruvias therapeutics thyroid tablet recall
    Why: "Thyroid medicine recall receives FDA's highest risk level" — USA Today

## Google Trends — 7-Day Interest (US)
  - **health**: latest=85, peak=100, 7d-delta=-3
    Rising related: darrell waltrip health, health gadgets, salem health, health holiday, medvi health, mental health, health care, health insurance
  - **wellness**: latest=26, peak=100, 7d-delta=-7
    Rising related: bakari silverback wellness exam, jennifer aniston wellness routine, circle wellness fremont, circle wellness spa, circle wellness spa seattle, circle wellness seattle, little luxe wellness lodge, circle wellness
  - **nutrition**: latest=75, peak=100, 7d-delta=-25
    Rising related: cheapest flights to tokyo, how to bake a cake, top tourist attractions in paris, how to make sushi, best time to visit maldives, best laptop for work, best pizza near me, cocoa pebbles nutrition facts
  - **fitness**: latest=29, peak=100, 7d-delta=-4
    Rising related: python tutorial, learn golang, air purifier review, netflix new releases, solar panel cost, cloud storage pricing, digital marketing course, weather forecast today
  - **food safety**: latest=29, peak=100, 7d-delta=-10
    Rising related: best time to visit maldives, cheapest flights to tokyo, best laptop for work, best pizza near me, top tourist attractions in paris, how to bake a cake, how to make sushi, king county food safety rating
  - **diet**: latest=77, peak=100, 7d-delta=-12
    Rising related: matt damon diet, optimized mediterranean diet, paleolithic diet, lion diet, proper diet to lose weight, diet drinks at sonic, diet coke ghost blanket, diet coke
  - **weight loss**: latest=16, peak=100, 7d-delta=-8
    Rising related: jb pritzker weight loss, elavate, rebel fashion, loop earplugs coupon, loop, ai landing page generator, emergent.sh pricing, bolt new
  - **mental health**: latest=78, peak=100, 7d-delta=+5
    Rising related: presley gerber mental health, did lizzie borden have mental health issues, lizzie borden mental health, best time to visit maldives, how to bake a cake, best laptop for work, my bib, moccasin bend mental health institute
  - **gut health**: latest=8, peak=100, 7d-delta=-12
    Rising related: cheapest flights to tokyo, lidl near me, kimchi recipe, sushi, how to clean gut health, how to check gut health, improve gut health, how to improve gut health

Top rising related queries from Google Trends:
  - darrell waltrip health
  - health gadgets
  - salem health
  - health holiday
  - medvi health
  - mental health
  - health care
  - health insurance
  - bakari silverback wellness exam
  - jennifer aniston wellness routine
  - circle wellness fremont
  - circle wellness spa
  - circle wellness spa seattle
  - circle wellness seattle
  - little luxe wellness lodge
  - circle wellness
  - cheapest flights to tokyo
  - how to bake a cake
  - top tourist attractions in paris
  - how to make sushi

## Google News Radar — Recent Health Topics (144 unique across 12 queries; showing 60)
Treat these headlines as the broad radar of news-led health topics. The Signal Listener must consider this radar before narrowing to retained candidates.
  - (health) [KFF] 09/18/2026, 07:00 AM, +0000 UTC — A Closer Look at the $50 Billion Rural Health Transformation Program
    
    Link: https://www.kff.org/medicaid/a-closer-look-at-the-50-billion-rural-health-transformation-program/
  - (health) [NPR] 09/24/2026, 05:14 AM, +0000 UTC — OpenAI's breach of Australian health department website prompts rebuke
    
    Link: https://www.npr.org/2026/09/24/g-s1-144835/openai-breach-australia
  - (health) [aphis.usda.gov] 09/21/2026, 07:00 AM, +0000 UTC — Screwworm.gov | Unified Government Response To Protect the United States
    
    Link: https://www.aphis.usda.gov/animals/animal-health/livestock-and-poultry-disease/stop-screwworm
  - (health) [OpenAI] 09/24/2026, 04:43 AM, +0000 UTC — Introducing MentalHealthBench
    
    Link: https://openai.com/index/introducing-mentalhealthbench/
  - (health) [Axios] 09/21/2026, 10:24 AM, +0000 UTC — Trump administration takes on mental health parity
    
    Link: https://www.axios.com/2026/09/21/mental-health-parity-trump-administration-rules
  - (health) [ClickOnDetroit | WDIV Local 4] 09/23/2026, 09:00 AM, +0000 UTC — Quality Behavioral Health named in $18.8M federal case alleging Medicaid fraud, forced labor
    
    Link: https://www.clickondetroit.com/news/local/2026/09/23/quality-behavioral-health-named-in-dollar188m-federal-case-alleging-medicaid-fraud-forced-labor/
  - (health) [World Health Organization (WHO)] 09/21/2026, 07:59 AM, +0000 UTC — New WHO report calls for stronger ethics oversight of AI-related health research
    
    Link: https://www.who.int/news/item/21-09-2026-new-who-report-calls-for-stronger-ethics-oversight-of-ai-related-health-research
  - (health) [Arkansas Advocate] 09/17/2026, 08:36 PM, +0000 UTC — Alice Walton says Bentonville healthcare campus to expand Arkansans’ access to specialty care
    
    Link: https://arkansasadvocate.com/2026/09/17/alice-walton-says-bentonville-healthcare-campus-to-expand-arkansans-access-to-specialty-care/
  - (health) [The New York Times] 09/22/2026, 07:00 AM, +0000 UTC — Dr. Anthony Robbins, Who Expanded Health Care for the Poor, Dies at 85
    
    Link: https://www.nytimes.com/2026/09/13/health/anthony-robbins-dead.html
  - (health) [Nature] 09/22/2026, 10:07 AM, +0000 UTC — Why girls have worse mental health than boys
    
    Link: https://www.nature.com/articles/s41562-026-02577-3
  - (health) [The Washington Post] 09/20/2026, 07:18 PM, +0000 UTC — Even medical professionals are skipping health insurance because of high prices
    
    Link: https://www.washingtonpost.com/health/2026/09/21/even-medical-professionals-are-skipping-health-insurance-because-high-prices/
  - (health) [Montana Free Press] 09/17/2026, 09:28 PM, +0000 UTC — Why are state employees’ health insurance rates going up?
    
    Link: https://montanafreepress.org/2026/09/17/montana-state-employees-healthcare-increase/
  - (wellness) [The Washington Post] 09/20/2026, 05:00 PM, +0000 UTC — Guest Column | I’m a pulmonologist. Here’s why new wellness claims about nicotine worry me.
    
    Link: https://www.washingtonpost.com/health/2026/09/20/im-pulmonologist-heres-why-new-wellness-claims-about-nicotine-worry-me/
  - (wellness) [cnbc.com] 09/18/2026, 11:00 AM, +0000 UTC — Why more companies are fighting over consumers' beauty, health and wellness spending
    
    Link: https://www.cnbc.com/2026/09/18/beauty-health-wellness-consumer-spending.html
  - (wellness) [The Conversation] 09/22/2026, 12:47 PM, +0000 UTC — How the pro-nicotine ‘wellness’ movement rebranded an addictive drug
    
    Link: https://theconversation.com/how-the-pro-nicotine-wellness-movement-rebranded-an-addictive-drug-290129
  - (wellness) [mycg.uscg.mil] 09/22/2026, 03:20 PM, +0000 UTC — Welcome to the new CG Civilian Wellness EAP
    
    Link: https://www.mycg.uscg.mil/News/Article/4608297/welcome-to-the-new-cg-civilian-wellness-eap/
  - (wellness) [UC Davis College of Engineering] 09/23/2026, 10:35 PM, +0000 UTC — Adding Wellness to the Engineering Education Equation
    
    Link: https://engineering.ucdavis.edu/news/adding-wellness-engineering-education-equation
  - (wellness) [WBAL-TV] 09/23/2026, 02:58 PM, +0000 UTC — Black Men's Wellness Day to offer free health screenings
    
    Link: https://www.wbaltv.com/article/baltimore-black-mens-wellness-day-free-health-screenings/73836490
  - (wellness) [UW-Milwaukee] 09/22/2026, 08:00 PM, +0000 UTC — Four Reasons Why You Should Schedule a SHAW Wellness Visit – Student Health and Wellness Center
    
    Link: https://uwm.edu/wellness/four-reasons-why-you-should-schedule-a-shaw-wellness-visit/
  - (wellness) [Marquette Today] 09/23/2026, 02:14 PM, +0000 UTC — Sync fitness tracker to automatically earn My Wellness points throughout the year
    
    Link: https://today.marquette.edu/2026/09/sync-fitness-tracker-to-automatically-earn-my-wellness-points-throughout-the-year/
  - (wellness) [Alaska Public Media] 09/22/2026, 10:42 PM, +0000 UTC — Haines to get $2.4M for community wellness initiative
    
    Link: https://alaskapublic.org/news/alaska-desk/2026-09-22/haines-to-get-2-4m-for-community-wellness-initiative
  - (wellness) [Happily Eva After] 09/23/2026, 08:03 AM, +0000 UTC — My Family Wellness Strategies
    
    Link: https://happilyevaafter.com/my-family-wellness-strategies/
  - (wellness) [People.com] 09/17/2026, 09:24 PM, +0000 UTC — Workers Hold Silverback Gorilla Bakari’s Hand During His First Wellness Checkup at Disney’s Animal Kingdom
    
    Link: https://people.com/workers-hold-gorillas-hand-during-disney-wellness-checkup-12126619
  - (wellness) [The New York Times] 09/21/2026, 07:57 PM, +0000 UTC — Woman’s Death After Wellness Spa Injection Is Ruled a Homicide
    
    Link: https://www.nytimes.com/2026/09/21/nyregion/bronx-wellness-center-injection-homicide.html
  - (medical study) [med.stanford.edu] 09/17/2026, 04:19 PM, +0000 UTC — Anti-seizure drug fights aggressive childhood brain tumors, Stanford Medicine-led study shows
    
    Link: https://med.stanford.edu/news/all-news/2026/09/seizure-drug-gliomas.html
  - (medical study) [nature.com] 09/22/2026, 09:28 PM, +0000 UTC — Performance and safety of a multi-cancer early detection test: the PATHFINDER 2 study
    
    Link: https://www.nature.com/articles/s41591-026-04618-w
  - (medical study) [The New York Times] 09/22/2026, 05:02 PM, +0000 UTC — Many Americans Use GLP-1 Drugs Without a Medical Reason, Study Shows
    
    Link: https://www.nytimes.com/2026/09/22/well/ozempic-glp1-medical-reason.html
  - (medical study) [Ms. Magazine] 09/21/2026, 11:29 PM, +0000 UTC — Decades of Male-Focused Medical Research Could Bias Healthcare AI
    
    Link: https://msmagazine.com/2026/09/21/male-focused-medical-research-gender-bias-healthcare-ai/
  - (medical study) [Mayo Clinic News Network] 09/22/2026, 09:30 PM, +0000 UTC — Multicancer blood test detects 17 cancer types in large prospective study
    
    Link: https://newsnetwork.mayoclinic.org/discussion/multicancer-blood-test-detects-17-cancer-types-in-large-prospective-study/
  - (medical study) [YaleNews] 09/18/2026, 06:19 PM, +0000 UTC — Study links soaring health care spending to higher insurance premiums
    
    Link: https://news.yale.edu/2026/09/18/study-links-soaring-health-care-spending-higher-insurance-premiums
  - (medical study) [University of Utah Health Academic Medical Center] 09/23/2026, 04:10 PM, +0000 UTC — Helping Faculty Turn Teaching Questions Into Medical Education Research
    
    Link: https://uofuhealth.utah.edu/notes/2026/09/helping-faculty-turn-teaching-questions-medical-education-research
  - (medical study) [The Guardian] 09/17/2026, 09:01 PM, +0000 UTC — Hundreds of ageing Americans may not get results of Alzheimer’s study due to Trump cuts
    
    Link: https://www.theguardian.com/us-news/2026/sep/17/trump-cuts-alzheimers-disease-study
  - (medical study) [The Clinical Trial Vanguard] 09/24/2026, 07:53 AM, +0000 UTC — Scaling Clinical AI to One Million Patients Taught Us Things No Pilot Study Could
    
    Link: https://www.clinicaltrialvanguard.com/article/intel-brief/scaling-clinical-ai-to-one-million-patients-taught-us-things-no-pilot-study-could/
  - (medical study) [KOKH] 09/23/2026, 03:01 PM, +0000 UTC — Oklahoma medical researchers to study cause of infertility
    
    Link: https://okcfox.com/news/local/oklahoma-medical-researchers-to-study-cause-of-infertility
  - (medical study) [Universities of Wisconsin] 09/24/2026, 02:22 PM, +0000 UTC — A deeper understanding: UWL students gain medical, cultural experience through Ecuador study abroad
    
    Link: https://www.wisconsin.edu/all-in-wisconsin/story/a-deeper-understanding-uwl-students-gain-medical-cultural-experience-through-ecuador-study-abroad/
  - (medical study) [News-Medical] 09/18/2026, 05:13 PM, +0000 UTC — Study identifies brain mechanism behind pregnancy-related food cravings
    
    Link: https://www.news-medical.net/news/20260918/Study-identifies-brain-mechanism-behind-pregnancy-related-food-cravings.aspx
  - (clinical trial health) [Newswise] 09/21/2026, 01:00 PM, +0000 UTC — Expert Available: How Health Systems Can Help Address America’s Clinical Trial Bottleneck | Newswise
    
    Link: https://www.newswise.com/articles/expert-available-how-health-systems-can-help-address-america-s-clinical-trial-bottleneck
  - (clinical trial health) [STAT] 09/21/2026, 08:33 AM, +0000 UTC — ClinicalTrials.gov needs a pregnancy and lactation checkbox
    
    Link: https://www.statnews.com/2026/09/21/clinical-trials-website-pregnant-lactating-patients-checkbox/
  - (clinical trial health) [Word In Black] 09/22/2026, 08:15 PM, +0000 UTC — Black Patients Aren’t Avoiding Clinical Trials. They Often Aren’t Asked
    
    Link: https://wordinblack.com/2026/09/black-patients-arent-avoiding-clinical-trials-they-often-arent-asked/
  - (clinical trial health) [Stock Titan] 09/22/2026, 10:00 AM, +0000 UTC — A new clinical trial platform is backed by 5 million+ annual patient visits
    
    Link: https://www.stocktitan.net/news/WHTCF/well-health-launches-well-research-an-end-to-end-clinical-trial-btdgvwgbp3pt.html
  - (clinical trial health) [Medical Xpress] 09/17/2026, 10:30 PM, +0000 UTC — HIV injections work better than tablets for young people, clinical trial finds
    
    Link: https://medicalxpress.com/news/2026-09-hiv-tablets-young-people-clinical.html
  - (clinical trial health) [reflector.com] 09/23/2026, 01:00 PM, +0000 UTC — Free health screenings, clinical trial set
    
    Link: https://www.reflector.com/enterprise/news/local/free-health-screenings-clinical-trial-set/article_edcd6989-3acb-46f5-aae1-a2ee15946c17.html
  - (clinical trial health) [KFF Health News] 09/18/2026, 09:03 AM, +0000 UTC — The Drugs and Devices Have Been on the Market for Years. But FDA-Ordered Studies Still Aren’t Done.
    
    Link: https://kffhealthnews.org/health-industry/fda-approval-drugs-medical-devices-postmarket-studies-safety-delays-amgen-tavneos/
  - (clinical trial health) [UC San Diego Health] 09/22/2026, 08:45 PM, +0000 UTC — Doctor Faced with Cancer Diagnosis Honored by San Diego Padres
    
    Link: https://health.ucsd.edu/news/features/doctor-faced-with-cancer-diagnosis-honored-by-san-diego-padres/
  - (clinical trial health) [The University of North Carolina at Chapel Hill] 09/17/2026, 04:31 PM, +0000 UTC — UNC Health, School of Medicine leaders build connections in Ireland
    
    Link: https://www.unc.edu/posts/2026/09/17/unc-health-school-of-medicine-leaders-build-connections-in-ireland/
  - (clinical trial health) [OHSU News] 09/22/2026, 09:18 PM, +0000 UTC — PATHFINDER 2 findings advance multi-cancer early detection blood testing
    
    Link: https://news.ohsu.edu/2026/09/22/pathfinder-2-findings-advance-multi-cancer-early-detection-blood-testing
  - (clinical trial health) [Britannica] 09/18/2026, 05:00 AM, +0000 UTC — Medicine - Clinical Research, Evidence-Based, Diagnosis
    
    Link: https://www.britannica.com/science/medicine/Clinical-research
  - (clinical trial health) [tradingview.com] 09/22/2026, 10:00 AM, +0000 UTC — WELL Health Technologies Corp. (WELL) Launches WELL Research Clinical Trials Platform
    
    Link: https://www.tradingview.com/news/tradingview:1a46a4cc041ed:0-well-health-technologies-corp-well-launches-well-research-clinical-trials-platform/
  - (FDA recall health) [Dallas News] 09/18/2026, 01:25 AM, +0000 UTC — FDA designates hand soap recall in Texas, 14 other states as Class II
    
    Link: https://www.dallasnews.com/news/public-health/article/hand-soap-recall-texas-designated-class-ii-fda-22436809.php
  - (FDA recall health) [USA Today] 09/24/2026, 12:18 PM, +0000 UTC — Thyroid medicine recall receives FDA's highest risk level
    
    Link: https://www.usatoday.com/story/money/consumer-protection/recalls-alerts/2026/09/24/thyroid-tablet-medicine-recall-fda/91916444007/
  - (FDA recall health) [NewsNation] 09/23/2026, 10:58 PM, +0000 UTC — FDA elevates thyroid tablet recall to most serious level
    
    Link: https://www.newsnationnow.com/health/fda-thyroid-tablet-recall-class-i/
  - (FDA recall health) [NBC News] 09/17/2026, 06:08 PM, +0000 UTC — Check your bathroom: This hand soap was just recalled in 15 states
    
    Link: https://www.nbcnews.com/select/shopping/intercon-hand-soap-recall-2026-rcna598380
  - (FDA recall health) [Yahoo] 09/19/2026, 01:53 PM, +0000 UTC — FDA assigns Class II warning to hand soaps recalled in 15 states over bacteria risk
    
    Link: https://www.yahoo.com/news/us/articles/fda-assigns-class-ii-warning-135300851.html
  - (FDA recall health) [WLOS] 09/17/2026, 08:16 PM, +0000 UTC — FDA recalls hand soaps from Ingles over potential bacterial contamination
    
    Link: https://wlos.com/news/local/fda-recalls-hand-soaps-laura-lynn-ingles-markets-potential-bacterial-contamination-food-drug-administration-honey-apple-crisp-pear-scent-foaming-liquid
  - (FDA recall health) [New York Post] 09/17/2026, 04:44 PM, +0000 UTC — Popular Walmart and Target frozen dessert recalled nationwide due to contamination
    
    Link: https://nypost.com/2026/09/17/lifestyle/so-delicious-ice-cream-recalled-nationwide-over-stones-found-in-pints-fda/
  - (FDA recall health) [TODAY.com] 09/23/2026, 05:53 PM, +0000 UTC — Over 160,000 Pounds of Meat Recalled Due to Lack of Inspection, Receives Highest Risk Level From USDA
    
    Link: https://www.today.com/health/recall/massive-meat-recall-usda-inspection-false-label-rcna599435
  - (FDA recall health) [MedShadow Foundation] 09/21/2026, 10:39 PM, +0000 UTC — FDA Recalls and Warnings: Third Glutathione Recall Issued Over Endotoxin Contamination
    
    Link: https://medshadow.org/drug-updates-recalls/fda-recalls-and-warnings/third-glutathione-injection-recall-endotoxin-contamination/
  - (FDA recall health) [WGRZ] 09/24/2026, 03:19 PM, +0000 UTC — Thyroid medication recall upgraded to FDA's highest risk level
    
    Link: https://www.wgrz.com/article/news/nation-world/thyroid-medication-recall-upgraded-fda-vitruvias-therapeutics/507-7b634b7f-7828-4a8b-bd64-475ad06d2717
  - (FDA recall health) [The Healthy] 09/17/2026, 09:00 PM, +0000 UTC — Tea Has Been Recalled Nationwide Because of an ‘Unsafe Food Additive’
    
    Link: https://www.thehealthy.com/news/tea-recall-september-2026/
  - (FDA recall health) [todaysmedicaldevelopments.com] 09/24/2026, 06:00 AM, +0000 UTC — Artificial intelligence could reduce medical device recalls, study suggests
    
    Link: https://www.todaysmedicaldevelopments.com/news/artificial-intelligence-could-reduce-medical-device-recalls-study-suggests/