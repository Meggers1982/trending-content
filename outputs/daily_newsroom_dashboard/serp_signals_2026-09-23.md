# LIVE SIGNAL DATA — SerpAPI Pre-Fetch
The following signals were fetched from SerpAPI Google News and SerpAPI Google Trends immediately before this pipeline run. Treat Google Trends as AVAILABLE when this section contains a Google Trends block. Use it as the primary search_velocity input for Skills 01–05 (Signal Listener through Trend Strength Scorer). Use the Google News Radar as the broad discovery layer for news-led health topics, including topics that do not yet appear in Google Trends. Prioritize topics with convergence across News, Trends, primary/institutional sources, and credible publisher coverage.

## Google Trends — Trending Now (US / Health, real-time)
Terms with a "Why:" line have a confirmed real-world news story driving the spike; terms without one are a real-time signal only, not yet grounded in a specific story.
  - measles
    Why: "Why the CDC is excluding measles deaths in Pennsylvania even as outbreak appears to be ‘accelerating’" — The Guardian

## Google Trends — 7-Day Interest (US)
  - **health**: latest=85, peak=100, 7d-delta=-6
    Rising related: xi jinping health, health gadgets, how to check ssd health, how to check hard drive health, salem health, how to check laptop battery health, how to improve gut health, health holiday
  - **wellness**: latest=27, peak=100, 7d-delta=-4
    Rising related: bakari silverback wellness exam, grocery delivery near me, grocery near me, circle wellness fremont, circle wellness spa, circle wellness seattle, circle wellness, energy wellness center
  - **nutrition**: latest=58, peak=100, 7d-delta=-10
    Rising related: cheapest flights to tokyo, best time to visit maldives, best laptop for work, top tourist attractions in paris, how to bake a cake, how to make sushi, best pizza near me, how to read nutrition labels
  - **fitness**: latest=31, peak=100, 7d-delta=+0
    Rising related: digital marketing course, python tutorial, cloud storage pricing, web hosting comparison, learn golang, air purifier review, netflix new releases, solar panel cost
  - **food safety**: latest=33, peak=100, 7d-delta=+3
    Rising related: best pizza near me, best time to visit maldives, cheapest flights to tokyo, how to make sushi, chipotle palantir food safety partnership, roti canai near me, machine learning algorithms, drunken noodles near me
  - **diet**: latest=60, peak=100, 7d-delta=-4
    Rising related: optimized mediterranean diet, matt damon diet, lion diet, what is the lion diet, what is a detox diet, high fat low carb diet, lions diet, diet coke
  - **weight loss**: latest=17, peak=100, 7d-delta=-2
    Rising related: best smoothie recipes for weight loss, paypal app, eddie bauer website, shop lc jewelry, lc jewelry, colon boom, vid iq, shoplc com
  - **mental health**: latest=72, peak=100, 7d-delta=-3
    Rising related: presley gerber mental health, best time to visit maldives, did lizzie borden have mental health issues, lizzie borden mental health, how to bake a cake, best laptop for work, mental health is a state of well-being that..., what is mental health
  - **gut health**: latest=16, peak=100, 7d-delta=-1
    Rising related: improve gut health, how to improve gut health, holistic gut health doctor near me, best supplements for gut health and bloating, good gut health, what is gut health, gut health foods, gut health probiotics

Top rising related queries from Google Trends:
  - xi jinping health
  - health gadgets
  - how to check ssd health
  - how to check hard drive health
  - salem health
  - how to check laptop battery health
  - how to improve gut health
  - health holiday
  - bakari silverback wellness exam
  - grocery delivery near me
  - grocery near me
  - circle wellness fremont
  - circle wellness spa
  - circle wellness seattle
  - circle wellness
  - energy wellness center
  - cheapest flights to tokyo
  - best time to visit maldives
  - best laptop for work
  - top tourist attractions in paris

## Google News Radar — Recent Health Topics (144 unique across 12 queries; showing 60)
Treat these headlines as the broad radar of news-led health topics. The Signal Listener must consider this radar before narrowing to retained candidates.
  - (health) [KFF] 09/18/2026, 07:00 AM, +0000 UTC — A Closer Look at the $50 Billion Rural Health Transformation Program
    
    Link: https://www.kff.org/medicaid/a-closer-look-at-the-50-billion-rural-health-transformation-program/
  - (health) [The University of Oklahoma] 09/22/2026, 08:47 PM, +0000 UTC — A Game Changer: Harold Hamm commits largest gift in OU history to lift health of Oklahoma, name Health Campus
    
    Link: https://ou.edu/news/articles/2026/September/harold-hamm-largest-gift-health-campus
  - (health) [World Health Organization (WHO)] 09/21/2026, 07:59 AM, +0000 UTC — New WHO report calls for stronger ethics oversight of AI-related health research
    
    Link: https://www.who.int/news/item/21-09-2026-new-who-report-calls-for-stronger-ethics-oversight-of-ai-related-health-research
  - (health) [ClickOnDetroit | WDIV Local 4] 09/23/2026, 09:00 AM, +0000 UTC — Quality Behavioral Health named in $18.8M federal case alleging Medicaid fraud, forced labor
    
    Link: https://www.clickondetroit.com/news/local/2026/09/23/quality-behavioral-health-named-in-dollar188m-federal-case-alleging-medicaid-fraud-forced-labor/
  - (health) [Arkansas Advocate] 09/17/2026, 08:36 PM, +0000 UTC — Alice Walton says Bentonville healthcare campus to expand Arkansans’ access to specialty care
    
    Link: https://arkansasadvocate.com/2026/09/17/alice-walton-says-bentonville-healthcare-campus-to-expand-arkansans-access-to-specialty-care/
  - (health) [The Washington Post] 09/20/2026, 07:18 PM, +0000 UTC — Even medical professionals are skipping health insurance because of high prices
    
    Link: https://www.washingtonpost.com/health/2026/09/21/even-medical-professionals-are-skipping-health-insurance-because-high-prices/
  - (health) [Centers for Disease Control and Prevention | CDC (.gov)] 09/21/2026, 11:07 PM, +0000 UTC — Youth Health in Focus
    
    Link: https://www.cdc.gov/yrbs/youth-health-in-focus/index.html
  - (health) [time.com] 09/16/2026, 06:35 PM, +0000 UTC — The Surprising Health Benefits of Reading a Book
    
    Link: https://time.com/article/2026/09/16/health-benefits-reading-books-for-pleasure/
  - (health) [Flathead Beacon] 09/18/2026, 10:22 AM, +0000 UTC — Logan Health Nurses Ratify New Contract with Immediate 18% Raise
    
    Link: https://flatheadbeacon.com/2026/09/18/logan-health-nurses-ratify-new-contract-with-immediate-18-raise/
  - (health) [The Guardian] 09/20/2026, 09:53 PM, +0000 UTC — Trump reportedly to form health funding board that could veto ‘woke’ initiatives
    
    Link: https://www.theguardian.com/us-news/2026/sep/20/trump-order-nih-health-research-funding-board
  - (health) [Healthinsurance.org] 09/18/2026, 07:00 AM, +0000 UTC — Health insurance premium increases for 2027: Proposed rates by state and what consumers should know
    
    Link: https://www.healthinsurance.org/blog/health-insurance-premium-increases-for-2027-proposed-rates-by-state-and-what-consumers-should-know/
  - (health) [PBS] 09/19/2026, 06:48 PM, +0000 UTC — Congo begins Ebola vaccinations for health workers in the epicenter of the outbreak
    
    Link: https://www.pbs.org/newshour/world/congo-begins-ebola-vaccinations-for-health-workers-in-the-epicenter-of-the-outbreak
  - (wellness) [The Washington Post] 09/20/2026, 05:00 PM, +0000 UTC — Guest Column | I’m a pulmonologist. Here’s why new wellness claims about nicotine worry me.
    
    Link: https://www.washingtonpost.com/health/2026/09/20/im-pulmonologist-heres-why-new-wellness-claims-about-nicotine-worry-me/
  - (wellness) [nytimes.com] 09/17/2026, 09:02 AM, +0000 UTC — Wellness-Focused Real Estate Is Betting on a Boom
    
    Link: https://www.nytimes.com/2026/09/17/realestate/wellness-focused-real-estate-is-betting-on-a-boom.html
  - (wellness) [CNBC] 09/18/2026, 11:00 AM, +0000 UTC — Why more companies are fighting over consumers' beauty, health and wellness spending
    
    Link: https://www.cnbc.com/2026/09/18/beauty-health-wellness-consumer-spending.html
  - (wellness) [The Conversation] 09/22/2026, 12:47 PM, +0000 UTC — How the pro-nicotine ‘wellness’ movement rebranded an addictive drug
    
    Link: https://theconversation.com/how-the-pro-nicotine-wellness-movement-rebranded-an-addictive-drug-290129
  - (wellness) [Alaska Public Media] 09/22/2026, 10:42 PM, +0000 UTC — Haines to get $2.4M for community wellness initiative
    
    Link: https://alaskapublic.org/news/alaska-desk/2026-09-22/haines-to-get-2-4m-for-community-wellness-initiative
  - (wellness) [mycg.uscg.mil] 09/22/2026, 03:20 PM, +0000 UTC — Welcome to the new CG Civilian Wellness EAP
    
    Link: https://www.mycg.uscg.mil/News/Article/4608297/welcome-to-the-new-cg-civilian-wellness-eap/
  - (wellness) [wpr.org] 09/17/2026, 10:00 AM, +0000 UTC — Aurora Health Care 'health and wellness hub' going into closed school building in Milwaukee
    
    Link: https://www.wpr.org/news/aurora-health-care-wellness-hub-closed-school-building-milwaukee
  - (wellness) [UW-Milwaukee] 09/22/2026, 08:00 PM, +0000 UTC — Four Reasons Why You Should Schedule a SHAW Wellness Visit – Student Health and Wellness Center
    
    Link: https://uwm.edu/wellness/four-reasons-why-you-should-schedule-a-shaw-wellness-visit/
  - (wellness) [WBAL-TV] 09/22/2026, 04:26 PM, +0000 UTC — Black Men's Wellness Day to offer free health screenings
    
    Link: https://www.wbaltv.com/article/baltimore-black-mens-wellness-day-free-health-screenings/73836490
  - (wellness) [happilyevaafter.com] 09/23/2026, 08:03 AM, +0000 UTC — My Family Wellness Strategies
    
    Link: https://happilyevaafter.com/my-family-wellness-strategies/
  - (wellness) [people.com] 09/17/2026, 09:24 PM, +0000 UTC — Workers Hold Silverback Gorilla Bakari’s Hand During His First Wellness Checkup at Disney’s Animal Kingdom
    
    Link: https://people.com/workers-hold-gorillas-hand-during-disney-wellness-checkup-12126619
  - (wellness) [Drake University Newsroom] 09/17/2026, 02:30 PM, +0000 UTC — The Harkin Institute Announces Victoria Brenton as New Wellness and Nutrition Director
    
    Link: https://news.drake.edu/2026/09/17/the-harkin-institute-announces-victoria-brenton-as-new-wellness-and-nutrition-director/
  - (medical study) [Stanford Medicine] 09/18/2026, 02:13 PM, +0000 UTC — Human brain is two separate organs, Stanford Medicine-led research finds
    
    Link: https://med.stanford.edu/news/all-news/2026/09/two-separate-brains.html
  - (medical study) [nytimes.com] 09/22/2026, 05:02 PM, +0000 UTC — Many Americans Use GLP-1 Drugs Without a Medical Reason, Study Shows
    
    Link: https://www.nytimes.com/2026/09/22/well/ozempic-glp1-medical-reason.html
  - (medical study) [Nature] 09/22/2026, 09:28 PM, +0000 UTC — Performance and safety of a multi-cancer early detection test: the PATHFINDER 2 study
    
    Link: https://www.nature.com/articles/s41591-026-04618-w
  - (medical study) [msmagazine.com] 09/21/2026, 11:29 PM, +0000 UTC — Decades of Male-Focused Medical Research Could Bias Healthcare AI
    
    Link: https://msmagazine.com/2026/09/21/male-focused-medical-research-gender-bias-healthcare-ai/
  - (medical study) [YaleNews] 09/18/2026, 06:19 PM, +0000 UTC — Study links soaring health care spending to higher insurance premiums
    
    Link: https://news.yale.edu/2026/09/18/study-links-soaring-health-care-spending-higher-insurance-premiums
  - (medical study) [The Guardian] 09/17/2026, 09:01 PM, +0000 UTC — Hundreds of ageing Americans may not get results of Alzheimer’s study due to Trump cuts
    
    Link: https://www.theguardian.com/us-news/2026/sep/17/trump-cuts-alzheimers-disease-study
  - (medical study) [Medical Xpress] 09/20/2026, 09:00 PM, +0000 UTC — Study reveals surprising cause of immune challenges in people with Down syndrome
    
    Link: https://medicalxpress.com/news/2026-09-reveals-immune-people-syndrome.html
  - (medical study) [South Florida Hospital News] 09/18/2026, 02:11 PM, +0000 UTC — New Stroke Recovery Study at Sarasota Memorial
    
    Link: https://southfloridahospitalnews.com/2026/09/18/new-stroke-recovery-study-at-sarasota-memorial/
  - (medical study) [Hospice News] 09/18/2026, 08:31 PM, +0000 UTC — Research: Setting Impacts Hospice Quality; Medical Decision Makers Predominantly Women
    
    Link: https://hospicenews.com/2026/09/18/research-setting-impacts-hospice-quality-medical-decision-makers-predominantly-women/
  - (medical study) [University of Cincinnati] 09/18/2026, 06:56 PM, +0000 UTC — UC emergency medicine physicians safely eliminate thousands of unnecessary CT scans
    
    Link: https://www.uc.edu/news/articles/2026/09/uc-emergency-medicine-cuts-unnecessary-ct-scans-low-risk-trauma.html
  - (medical study) [News-Medical] 09/18/2026, 05:13 PM, +0000 UTC — Study identifies brain mechanism behind pregnancy-related food cravings
    
    Link: https://www.news-medical.net/news/20260918/Study-identifies-brain-mechanism-behind-pregnancy-related-food-cravings.aspx
  - (medical study) [University of Colorado Anschutz] 09/22/2026, 09:24 PM, +0000 UTC — A Family with Deep CU Ties Supports a Home-Grown Study Seeking a Better Leukemia Treatment
    
    Link: https://news.cuanschutz.edu/cancer-center/kent-shelton-aml-trial
  - (clinical trial health) [Florida International University] 09/16/2026, 04:05 PM, +0000 UTC — FIU/Baptist Health physician-researchers explore ways to expand clinical trial participation
    
    Link: https://news.fiu.edu/2026/fiubaptist-health-physician-researchers-explore-ways-to-expand-clinical-trial-participation
  - (clinical trial health) [Newswise] 09/21/2026, 01:00 PM, +0000 UTC — Expert Available: How Health Systems Can Help Address America’s Clinical Trial Bottleneck | Newswise
    
    Link: https://www.newswise.com/articles/expert-available-how-health-systems-can-help-address-america-s-clinical-trial-bottleneck
  - (clinical trial health) [STAT] 09/21/2026, 08:33 AM, +0000 UTC — ClinicalTrials.gov needs a pregnancy and lactation checkbox
    
    Link: https://www.statnews.com/2026/09/21/clinical-trials-website-pregnant-lactating-patients-checkbox/
  - (clinical trial health) [Applied Clinical Trials] 09/16/2026, 05:03 PM, +0000 UTC — Benchmarking Study Finds Clinical Trial Performance Is Shaped by Operating Model Design, Not Sourcing Strategy
    
    Link: https://www.appliedclinicaltrialsonline.com/view/benchmarking-study-finds-clinical-trial-performance-operating-model-design-sourcing-strategy
  - (clinical trial health) [Stock Titan] 09/22/2026, 10:00 AM, +0000 UTC — A new clinical trial platform is backed by 5 million+ annual patient visits
    
    Link: https://www.stocktitan.net/news/WHTCF/well-health-launches-well-research-an-end-to-end-clinical-trial-btdgvwgbp3pt.html
  - (clinical trial health) [Word In Black] 09/22/2026, 08:15 PM, +0000 UTC — Black Patients Aren’t Avoiding Clinical Trials. They Often Aren’t Asked
    
    Link: https://wordinblack.com/2026/09/black-patients-arent-avoiding-clinical-trials-they-often-arent-asked/
  - (clinical trial health) [medicalxpress.com] 09/17/2026, 10:30 PM, +0000 UTC — HIV injections work better than tablets for young people, clinical trial finds
    
    Link: https://medicalxpress.com/news/2026-09-hiv-tablets-young-people-clinical.html
  - (clinical trial health) [Rethinking Clinical Trials] 09/17/2026, 02:19 PM, +0000 UTC — September 17, 2026: IMPACT Collaboratory Seeks Applicants for 2027 Health Care Systems Scholars Program
    
    Link: https://rethinkingclinicaltrials.org/news/september-17-2026-impact-collaboratory-seeks-applicants-for-2027-health-care-systems-scholars-program/
  - (clinical trial health) [hcinnovationgroup.com] 09/17/2026, 06:39 AM, +0000 UTC — ResearchPass Puts Clinical Trial Info on Participants’ Smartphones
    
    Link: https://www.hcinnovationgroup.com/clinical-it/learning-health-systems-research/news/55405529/researchpass-puts-clinical-trial-info-on-participants-smartphones
  - (clinical trial health) [KFF Health News] 09/18/2026, 09:03 AM, +0000 UTC — The Drugs and Devices Have Been on the Market for Years. But FDA-Ordered Studies Still Aren’t Done.
    
    Link: https://kffhealthnews.org/health-industry/fda-approval-drugs-medical-devices-postmarket-studies-safety-delays-amgen-tavneos/
  - (clinical trial health) [UC San Diego Health] 09/22/2026, 08:45 PM, +0000 UTC — Doctor Faced with Cancer Diagnosis Honored by San Diego Padres
    
    Link: https://health.ucsd.edu/news/features/doctor-faced-with-cancer-diagnosis-honored-by-san-diego-padres/
  - (clinical trial health) [The University of North Carolina at Chapel Hill] 09/17/2026, 04:31 PM, +0000 UTC — UNC Health, School of Medicine leaders build connections in Ireland
    
    Link: https://www.unc.edu/posts/2026/09/17/unc-health-school-of-medicine-leaders-build-connections-in-ireland/
  - (FDA recall health) [Scripps News] 09/17/2026, 02:00 AM, +0000 UTC — FDA warns recalled hand soaps may contain harmful bacteria
    
    Link: https://www.scrippsnews.com/health/fda-warns-recalled-hand-soaps-may-contain-harmful-bacteria
  - (FDA recall health) [FOX 5 Atlanta] 09/16/2026, 08:32 PM, +0000 UTC — FDA recalls hand soaps sold in Georgia over bacteria risk
    
    Link: https://www.fox5atlanta.com/news/fda-recalls-hand-soaps-sold-georgia-over-bacteria-risk
  - (FDA recall health) [FOX 9 Minneapolis-St. Paul] 09/16/2026, 07:37 PM, +0000 UTC — FDA recalls hand soap sold in 15 states due to risk of bacteria
    
    Link: https://www.fox9.com/news/fda-hand-soap-recall-states-bacteria-risk
  - (FDA recall health) [Dallas News] 09/18/2026, 01:25 AM, +0000 UTC — FDA designates hand soap recall in Texas, 14 other states as Class II
    
    Link: https://www.dallasnews.com/news/public-health/article/hand-soap-recall-texas-designated-class-ii-fda-22436809.php
  - (FDA recall health) [NBC News] 09/17/2026, 06:08 PM, +0000 UTC — Check your bathroom: This hand soap was just recalled in 15 states
    
    Link: https://www.nbcnews.com/select/shopping/intercon-hand-soap-recall-2026-rcna598380
  - (FDA recall health) [facebook.com] 09/23/2026, 02:20 PM, +0000 UTC — CHECK YOUR CABINETS: The FDA has issued an urgent recall for bottles of popular blood pressure medication.
    
    Link: https://www.facebook.com/Boston25News/posts/check-your-cabinets-the-fda-has-issued-an-urgent-recall-for-bottles-of-popular-b/1579000200928307/
  - (FDA recall health) [citizen-times.com] 09/16/2026, 04:26 PM, +0000 UTC — Ingles hand soap, others recalled in NC for bacterial contamination
    
    Link: https://www.citizen-times.com/story/news/health/2026/09/16/fda-recalls-hand-soap-sold-in-north-carolina-ingles/91790211007/
  - (FDA recall health) [WLOS] 09/17/2026, 08:16 PM, +0000 UTC — FDA recalls hand soaps from Ingles over potential bacterial contamination
    
    Link: https://wlos.com/news/local/fda-recalls-hand-soaps-laura-lynn-ingles-markets-potential-bacterial-contamination-food-drug-administration-honey-apple-crisp-pear-scent-foaming-liquid
  - (FDA recall health) [New York Post] 09/17/2026, 04:44 PM, +0000 UTC — Popular Walmart and Target frozen dessert recalled nationwide due to contamination
    
    Link: https://nypost.com/2026/09/17/lifestyle/so-delicious-ice-cream-recalled-nationwide-over-stones-found-in-pints-fda/
  - (FDA recall health) [Yahoo] 09/19/2026, 01:53 PM, +0000 UTC — FDA assigns Class II warning to hand soaps recalled in 15 states over bacteria risk
    
    Link: https://www.yahoo.com/news/us/articles/fda-assigns-class-ii-warning-135300851.html
  - (FDA recall health) [NBC 5 Chicago] 09/16/2026, 07:50 PM, +0000 UTC — Hand soap recall issued for products distributed in 16 states, including Illinois
    
    Link: https://www.nbcchicago.com/news/local/hand-soap-recall-issued-for-products-sold-in-15-states-including-illinois/3989902/
  - (FDA recall health) [abcnews.com] 09/21/2026, 07:00 AM, +0000 UTC — Egg recall linked to salmonella upgraded to highest risk level by FDA
    
    Link: https://abcnews.com/GMA/Food/19-million-eggs-voluntarily-recalled-potential-salmonella-contamination/story?id=135028861