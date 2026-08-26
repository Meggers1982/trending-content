# LIVE SIGNAL DATA — SerpAPI Pre-Fetch
The following signals were fetched from SerpAPI Google News and SerpAPI Google Trends immediately before this pipeline run. Treat Google Trends as AVAILABLE when this section contains a Google Trends block. Use it as the primary search_velocity input for Skills 01–05 (Signal Listener through Trend Strength Scorer). Use the Google News Radar as the broad discovery layer for news-led health topics, including topics that do not yet appear in Google Trends. Prioritize topics with convergence across News, Trends, primary/institutional sources, and credible publisher coverage.

## Google Trends — Trending Now (US / Health, real-time)
Terms with a "Why:" line have a confirmed real-world news story driving the spike; terms without one are a real-time signal only, not yet grounded in a specific story.
  - vitruvias therapeutics superpotent medication recall
    Why: "Thyroid tablets recalled because they could be ‘superpotent,' lead to hyperthyroidism" — NBC 5 Chicago
  - measles
    Why: "Two Unvaccinated People Died From Measles in Pennsylvania, Officials Say" — The New York Times

## Google Trends — 7-Day Interest (US)
  - **health**: latest=33, peak=100, 7d-delta=+0
    Rising related: dolly parton health update, dolly parton death, what are the latest health updates from dolly parton and details on her new museum, dolly parton health, dolly parton health issues, what health issues did dolly parton have, what health issues did dolly parton have?, dolly parton breaking news
  - **wellness**: latest=75, peak=100, 7d-delta=-6
    Rising related: shrek 5, patagonia black hole duffel 100l tidal tea, ocean state community wellness, chc wellbeing, passport health, ndsu wellness center, und wellness center, wellness kitchen auburn
  - **nutrition**: latest=82, peak=100, 7d-delta=-2
    Rising related: curtain up, cooked versus raw vegetables nutrition, sundance kid, sundance, action kid, curtain up channel, action channel, comeback kid
  - **fitness**: latest=68, peak=100, 7d-delta=-9
    Rising related: eric falstrault fitness transformation, muscle definition over 50 fitness, hospitals, planet fitness, la fitness, crunch, crunch fitness, fitness near me
  - **food safety**: latest=22, peak=100, 7d-delta=-17
    Rising related: aluminum foil food storage safety, chapter 13 project 2025, uc riverside dollar store study, permanent daylight saving time winter sunsets, project 2025 food supply, project 2025 chapter 10, aldi game day snack container, alan jackson final tour retirement
  - **diet**: latest=82, peak=100, 7d-delta=-3
    Rising related: vegan diet and inflammation, dolly parton diet, christie brinkley vegan diet, billy bob thornton diet, healthy diet plan for beginners, uefa champions league news, morning routine for success, best side hustles for students
  - **weight loss**: latest=53, peak=100, 7d-delta=-7
    Rising related: billy gardell weight loss transformation, tiffany franco 110 pound weight loss, gabe newell weight loss, wynonna judd weight loss, medvi quad reviews, joinembody, quad ed, medvi tirzepatide cost
  - **mental health**: latest=60, peak=100, 7d-delta=+1
    Rising related: kyle singler mental health, mychal threets mental health, how to improve mental health lwspeakcare, inpatient mental health facilities near me, mental health treatment center, what is mental health, mental health services, mental health treatment
  - **gut health**: latest=80, peak=100, 7d-delta=+7
    Rising related: is farting a sign of good gut health, seneca, who began public health and sanitation systems, began public health and sanitation systems, who used acupuncture to relieve pain and congestion, food for gut health, good gut health, what is gut health

Top rising related queries from Google Trends:
  - dolly parton health update
  - dolly parton death
  - what are the latest health updates from dolly parton and details on her new museum
  - dolly parton health
  - dolly parton health issues
  - what health issues did dolly parton have
  - what health issues did dolly parton have?
  - dolly parton breaking news
  - shrek 5
  - patagonia black hole duffel 100l tidal tea
  - ocean state community wellness
  - chc wellbeing
  - passport health
  - ndsu wellness center
  - und wellness center
  - wellness kitchen auburn
  - curtain up
  - cooked versus raw vegetables nutrition
  - sundance kid
  - sundance

## Google News Radar — Recent Health Topics (144 unique across 12 queries; showing 60)
Treat these headlines as the broad radar of news-led health topics. The Signal Listener must consider this radar before narrowing to retained candidates.
  - (health) [People.com] 08/25/2026, 06:04 PM, +0000 UTC — Dolly Parton Spoke About Going Through ‘Hard Times with My Health’ 4 Days Before Her Death at 80 (Exclusive)
    
    Link: https://people.com/dolly-parton-spoke-about-health-hard-times-four-days-before-death-exclusive-12065830
  - (health) [Centers for Disease Control and Prevention | CDC (.gov)] 08/21/2026, 07:00 AM, +0000 UTC — Measles Cases and Outbreaks
    
    Link: https://www.cdc.gov/measles/data-research/index.html
  - (health) [ICRC] 08/24/2026, 11:29 AM, +0000 UTC — Protection of health care
    
    Link: https://www.icrc.org/en/law-and-policy/protection-health-care
  - (health) [Atrium Health] 08/22/2026, 01:19 AM, +0000 UTC — In partnership with Morehouse School of Medicine Atrium Health commits more than 700 million
    
    Link: https://atriumhealth.org/about-us/newsroom/news/2026/08/in-partnership-with-morehouse-school-of-medicine-atrium-health-commits-more-than-700-million
  - (health) [Maryland.gov] 08/24/2026, 07:13 PM, +0000 UTC — Pages - Maryland Department of Health declares measles outbreak in three Maryland counties
    
    Link: https://health.maryland.gov/newsroom/Pages/Maryland%20Department%20of%20Health%20declares%20measles%20outbreak%20in%20three%20Maryland%20counties.aspx
  - (health) [aphis.usda.gov] 08/21/2026, 07:00 AM, +0000 UTC — Confirmed Detections of New World Screwworm | Animal and Plant Health Inspection Service
    
    Link: https://www.aphis.usda.gov/animals/animal-health/livestock-and-poultry-disease/stop-screwworm/current-status/confirmed
  - (health) [Alabama Governor's Office (.gov)] 08/24/2026, 03:01 PM, +0000 UTC — Governor Ivey Announces First Grants in Major New Rural Healthcare Program Totaling More than $144 Million
    
    Link: https://governor.alabama.gov/newsroom/2026/08/governor-ivey-announces-first-grants-in-major-new-rural-healthcare-program-totaling-more-than-144-million/
  - (health) [Nature] 08/20/2026, 10:21 AM, +0000 UTC — The hallmarks of skeletal muscle health
    
    Link: https://www.nature.com/articles/s42255-026-01595-9
  - (health) [International Brotherhood of Teamsters] 08/20/2026, 03:41 PM, +0000 UTC — 10,000 Corewell Health East Nurses Ratify First Teamsters Contract
    
    Link: https://teamster.org/2026/08/10000-corewell-health-east-nurses-ratify-first-teamsters-contract/
  - (health) [Axios] 08/20/2026, 09:01 PM, +0000 UTC — Employer health costs: Why it could be another tough year
    
    Link: https://www.axios.com/2026/08/20/health-care-costs-employers-rising
  - (health) [Raiders.com] 08/24/2026, 05:02 PM, +0000 UTC — Las Vegas Raiders announce $25 million game-changing gift to Intermountain Health to help build Nevada's first stand-alone children's hospital
    
    Link: https://www.raiders.com/news/las-vegas-raiders-announce-25-million-game-changing-gift-to-intermountain-health-to-help-build-nevada-s-first-stand-alone-children-s-hospital
  - (health) [Think Global Health] 08/20/2026, 07:00 AM, +0000 UTC — Tracking Measles and the World's Vaccine-Preventable Diseases
    
    Link: https://www.thinkglobalhealth.org/article/vaccine-preventable-disease-a-global-tracker
  - (wellness) [FOX 13 Tampa Bay] 08/21/2026, 03:26 AM, +0000 UTC — Wellness retreat project
    
    Link: https://www.fox13news.com/news/oxford-exchange-owners-plan-550-acre-wellness-retreat-near-dade-city
  - (wellness) [Yahoo Creators] 08/24/2026, 01:15 PM, +0000 UTC — Wellness stacking: why psychologists say it beats willpower for building healthy habits
    
    Link: https://creators.yahoo.com/lifestyle/story/wellness-stacking-why-psychologists-say-it-beats-willpower-for-building-healthy-habits-015140677.html
  - (wellness) [WFLA] 08/23/2026, 04:18 PM, +0000 UTC — 1 dead, officer hospitalized after attempted wellness check in St. Pete: PCSO
    
    Link: https://www.wfla.com/news/pinellas-county/1-dead-officer-hospitalized-after-attempted-wellness-check-in-st-pete-pcso/
  - (wellness) [The New York Times] 08/21/2026, 02:35 PM, +0000 UTC — ‘Spa Weekend’ Review: Girls Gone Wellness
    
    Link: https://www.nytimes.com/2026/08/21/movies/spa-weekend-review.html
  - (wellness) [Ground Truths | Eric Topol] 08/23/2026, 02:41 PM, +0000 UTC — Deborah Cohen: The Wellness-Industrial Complex
    
    Link: https://erictopol.substack.com/p/deborah-cohen-the-wellness-industrial
  - (wellness) [University of Evansville Athletics] 08/22/2026, 01:49 AM, +0000 UTC — Ali Adams promoted to Assistant AD for Student-Athlete Health & Wellness
    
    Link: https://gopurpleaces.com/news/2026/8/21/general-releases-ali-adams-promoted-to-assistant-ad-for-student-athlete-health-wellness.aspx
  - (wellness) [University of Nebraska Medical Center] 08/25/2026, 09:15 AM, +0000 UTC — Center for Healthy Living integrates fitness, wellness
    
    Link: https://www.unmc.edu/newsroom/2026/08/25/center-for-healthy-living-integrates-fitness-wellness/
  - (wellness) [WBAL-TV] 08/21/2026, 09:38 PM, +0000 UTC — Waterfront Wellness combines scenic views with working out
    
    Link: https://www.wbaltv.com/article/inner-harbor-free-fitness-program-baltimore/73495869
  - (wellness) [UCLA Health] 08/24/2026, 09:28 PM, +0000 UTC — Is a wellness drink worth it? Decoding functional beverage labels
    
    Link: https://www.uclahealth.org/news/article/wellness-drink-worth-it-decoding-functional-beverage-labels
  - (wellness) [Hartford Hospital] 08/21/2026, 02:17 PM, +0000 UTC — 10 Wellness Trends Everyone’s Trying Right Now. Here’s What Actually Works
    
    Link: https://hartfordhospital.org/about-hh/news-center/news-detail?articleId=74682
  - (wellness) [Pratt Institute] 08/25/2026, 04:11 PM, +0000 UTC — A Centralized Hub for Student Wellness Opens on Pratt’s Brooklyn Campus
    
    Link: https://www.pratt.edu/news/a-centralized-hub-for-student-wellness-opens-on-pratts-brooklyn-campus/
  - (wellness) [Forbes] 08/24/2026, 01:15 PM, +0000 UTC — Smart Glasses Set To Transform Healthcare And Wellness
    
    Link: https://www.forbes.com/sites/sanjitsinghdang/2026/08/24/smart-glasses-set-to-transform-healthcare-and-wellness/
  - (medical study) [NPR] 08/19/2026, 03:22 PM, +0000 UTC — A real-world study of Oregon's nonmedical psilocybin program shows promise
    
    Link: https://www.npr.org/2026/08/19/nx-s1-5936443/oregon-psilocybin-ptsd-depression-anxiety
  - (medical study) [NYU Langone Health] 08/25/2026, 05:13 PM, +0000 UTC — NYU Langone Health to Lead New Trial of Ketamine for Pain Relief
    
    Link: https://nyulangone.org/news/nyu-langone-health-lead-new-trial-ketamine-pain-relief
  - (medical study) [Stanford Medicine] 08/19/2026, 09:51 PM, +0000 UTC — ‘Molecular glue’ turns a cancer driver into a built-in kill switch in Stanford Medicine study
    
    Link: https://med.stanford.edu/news/all-news/2026/08/lymphoma-BCL6-kill-switch.html
  - (medical study) [Wolters Kluwer] 08/25/2026, 07:48 PM, +0000 UTC — Medical Research Platform | Institutional Partners
    
    Link: https://www.wolterskluwer.com/en/expert-insights/comprehensive-literature-search-multiple-databases
  - (medical study) [UMass Chan Medical School] 08/24/2026, 04:17 AM, +0000 UTC — UMass Chan researchers study psychedelic medication for adjustment disorder in people with serious medical conditions
    
    Link: https://www.umassmed.edu/news/articles/2026/08/umass-chan-researchers-study-psychedelic-medication-for-adjustment-disorder-in-people-with-serious-medical-conditions/
  - (medical study) [OHSU News] 08/19/2026, 03:09 PM, +0000 UTC — Study finds sustained benefit for people using Oregon psilocybin services
    
    Link: https://news.ohsu.edu/2026/08/19/study-finds-sustained-benefit-for-people-using-oregon-psilocybin-services
  - (medical study) [Yahoo Sports] 08/25/2026, 03:20 PM, +0000 UTC — Terrifying NFL Discovery: Bombshell New Medical Study Exposes How Many Deceased Players Had CTE
    
    Link: https://sports.yahoo.com/articles/terrifying-nfl-discovery-bombshell-medical-152045510.html
  - (medical study) [UT Southwestern] 08/21/2026, 03:58 PM, +0000 UTC — Brain activity discovery could transform Parkinson’s treatment: Newsroom
    
    Link: https://www.utsouthwestern.edu/newsroom/articles/year-2026/aug-brain-activity-parkinsons-treatment.html
  - (medical study) [University of Miami] 08/25/2026, 02:06 PM, +0000 UTC — REACH Study Aims to Make School Success a Measure of Children’s Health
    
    Link: https://news.med.miami.edu/reach-study-school-performance-childrens-health/
  - (medical study) [Medical Xpress] 08/25/2026, 09:00 AM, +0000 UTC — Loneliness rewires the brain to drive alcohol use, preclinical study finds
    
    Link: https://medicalxpress.com/news/2026-08-loneliness-rewires-brain-alcohol-preclinical.html
  - (medical study) [Columbia University Irving Medical Center] 08/21/2026, 02:24 AM, +0000 UTC — Depression Stalls Formation of New Brain Cells
    
    Link: https://www.cuimc.columbia.edu/news/depression-stalls-formation-new-brain-cells
  - (medical study) [DVIDS] 08/21/2026, 07:30 PM, +0000 UTC — News - 2026 NMRC Interns Conclude Summer Program, Present Work for Navy Medicine R&D
    
    Link: https://www.dvidshub.net/news/573007/2026-nmrc-interns-conclude-summer-program-present-work-navy-medicine-rd
  - (clinical trial health) [CNN] 08/22/2026, 04:00 PM, +0000 UTC — You want to join a clinical trial. Here’s what to know about the hurdles.
    
    Link: https://www.cnn.com/2026/08/22/health/clinical-trials-what-to-know
  - (clinical trial health) [The American Journal of Managed Care] 08/21/2026, 08:17 PM, +0000 UTC — Ochsner Health, Paradigm Health Partnership Expands Clinical Trial Access Across the Gulf South
    
    Link: https://www.ajmc.com/view/ochsner-health-paradigm-health-partnership-expands-clinical-trial-access-across-the-gulf-south
  - (clinical trial health) [Cancer Health] 08/25/2026, 03:13 AM, +0000 UTC — Clinical Trials Matter: What Our Patients Say
    
    Link: https://www.cancerhealth.com/article/clinical-trials-matter-patients-say
  - (clinical trial health) [Applied Clinical Trials Online] 08/20/2026, 04:05 PM, +0000 UTC — Curavit Acquires Lindus Health Clinical Research Organization Assets to Expand US and European Trial Operations
    
    Link: https://www.appliedclinicaltrialsonline.com/view/curavit-acquires-lindus-health-clinical-research-organization-assets-expand-us-european-trial-operations
  - (clinical trial health) [Tufts Now] 08/25/2026, 12:00 PM, +0000 UTC — One Center’s Oversized Impact on Drug Development and Clinical Trials
    
    Link: https://now.tufts.edu/2026/08/25/one-centers-oversized-impact-drug-development-and-clinical-trials
  - (clinical trial health) [Clinical Trials Arena] 08/20/2026, 11:01 AM, +0000 UTC — Reforms to UK clinical trial sector showing signs of success
    
    Link: https://www.clinicaltrialsarena.com/news/reforms-to-uk-clinical-trial-sector-showing-signs-of-success/
  - (clinical trial health) [PR Newswire] 08/25/2026, 12:01 PM, +0000 UTC — Allegheny Health Network and The START Center for Cancer Research Announce Strategic Collaboration to Expand Patient Access to Early-Phase Cancer Trials
    
    Link: https://www.prnewswire.com/news-releases/allegheny-health-network-and-the-start-center-for-cancer-research-announce-strategic-collaboration-to-expand-patient-access-to-early-phase-cancer-trials-302858392.html
  - (clinical trial health) [Nutrition Insight] 08/21/2026, 04:17 PM, +0000 UTC — Perelel’s Triple-Support protein shows promise for women’s health in clinical trial
    
    Link: https://www.nutritioninsight.com/news/perelel-triple-support-protein-womens-health.html
  - (clinical trial health) [South Carolina Daily Gazette] 08/19/2026, 04:18 PM, +0000 UTC — State-funded testing of COVID-19 treatment approved to start 3,000-person clinical trial
    
    Link: https://scdailygazette.com/2026/08/19/state-funded-testing-of-covid-19-treatment-approved-to-start-3000-person-clinical-trial/
  - (clinical trial health) [MedTech Dive] 08/21/2026, 04:30 PM, +0000 UTC — How can wearables be used in clinical trials? FDA outlines best practices
    
    Link: https://www.medtechdive.com/news/how-can-wearables-be-used-in-clinical-trials-fda-outlines-best-practices/828512/
  - (clinical trial health) [The Clinical Trial Vanguard] 08/20/2026, 07:33 AM, +0000 UTC — When Your CRO Gets Acquired, Your Site Activation Timeline Pays the Price
    
    Link: https://www.clinicaltrialvanguard.com/clinical-trial-ops-brief/when-your-cro-gets-acquired-your-site-activation-timeline-pays-the-price/
  - (clinical trial health) [Flow Space] 08/19/2026, 06:06 PM, +0000 UTC — 8 Shocking Facts About Women in Medical Research That Will Make You Say, ‘Seriously?’
    
    Link: https://www.theflowspace.com/interpersonal-health/access-equity/women-clinical-trials-statistics-3039955/
  - (FDA recall health) [CBS News] 08/19/2026, 10:52 PM, +0000 UTC — FDA upgrades recall of frozen blueberries sold at Publix to highest health risk level
    
    Link: https://www.cbsnews.com/news/blueberry-recall-fda-class-1-risk/
  - (FDA recall health) [fda.gov] 08/24/2026, 03:07 PM, +0000 UTC — Outbreak Investigation of Shiga Toxin-producing E. coli & Salmonella: Sprouts (August 2026)
    
    Link: https://www.fda.gov/food/outbreaks-foodborne-illness/outbreak-investigation-shiga-toxin-producing-e-coli-salmonella-sprouts-august-2026
  - (FDA recall health) [Axios] 08/22/2026, 10:01 AM, +0000 UTC — Here's why the FDA hit frozen blueberries with its highest risk warning
    
    Link: https://www.axios.com/2026/08/22/frozen-blueberries-recall-fda-high-risk-warning
  - (FDA recall health) [Healthline] 08/20/2026, 06:18 PM, +0000 UTC — FDA Upgrades Publix Frozen Blueberry Recall to Highest Health Risk Level
    
    Link: https://www.healthline.com/health-news/fda-upgrades-publix-frozen-blueberry-recall-highest-risk-level
  - (FDA recall health) [The Washington Post] 08/21/2026, 12:15 AM, +0000 UTC — FDA upgrades recall of frozen berries to highest-risk warning
    
    Link: https://www.washingtonpost.com/health/2026/08/20/fda-upgrades-recall-frozen-berries-highest-risk-warning/
  - (FDA recall health) [Centers for Disease Control and Prevention | CDC (.gov)] 08/20/2026, 07:00 AM, +0000 UTC — Cyclospora Outbreak Linked to Iceberg Lettuce | Cyclosporiasis
    
    Link: https://www.cdc.gov/cyclosporiasis/outbreaks/07-26/index.html
  - (FDA recall health) [NewsNation] 08/22/2026, 12:29 PM, +0000 UTC — Food recalls aren’t a success story, former FDA official says
    
    Link: https://www.newsnationnow.com/health/food-recalls-arent-success-story-former-fda-official/
  - (FDA recall health) [The New York Times] 08/23/2026, 06:12 PM, +0000 UTC — Nearly 40,000 Eye Drop Bottles Are Recalled Over Potential Contamination
    
    Link: https://www.nytimes.com/2026/08/23/health/clear-eyes-eye-drops-fda-recall.html
  - (FDA recall health) [88.5 WFDD] 08/20/2026, 09:04 PM, +0000 UTC — FDA moves Publix frozen berry E. coli recall to Class I health risk
    
    Link: https://www.wfdd.org/health-safety/2026-08-20/fda-moves-publix-frozen-berry-e-coli-recall-to-class-i-health-risk
  - (FDA recall health) [WRAL] 08/21/2026, 03:40 PM, +0000 UTC — Publix frozen berry recall upgraded to FDA’s highest-risk level
    
    Link: https://www.wral.com/consumer/5onyourside/publix-blueberry-recall-upgraded-august-2026/
  - (FDA recall health) [Health.com] 08/19/2026, 02:54 PM, +0000 UTC — FDA Announces Nationwide Recall of Popular Fruit Bars—Products May Contain Glass
    
    Link: https://www.health.com/outshine-fruit-bars-recall-august-2026-12063179
  - (FDA recall health) [Good Housekeeping] 08/19/2026, 07:43 PM, +0000 UTC — FDA Announces Nationwide Recall of Popular Ice Pops Sold at Multiple Retailers—Here’s the Full List
    
    Link: https://www.goodhousekeeping.com/food-products/a73468917/outshine-fruit-bars-recall/