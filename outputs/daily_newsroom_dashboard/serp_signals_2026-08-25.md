# LIVE SIGNAL DATA — SerpAPI Pre-Fetch
The following signals were fetched from SerpAPI Google News and SerpAPI Google Trends immediately before this pipeline run. Treat Google Trends as AVAILABLE when this section contains a Google Trends block. Use it as the primary search_velocity input for Skills 01–05 (Signal Listener through Trend Strength Scorer). Use the Google News Radar as the broad discovery layer for news-led health topics, including topics that do not yet appear in Google Trends. Prioritize topics with convergence across News, Trends, primary/institutional sources, and credible publisher coverage.

## Google Trends — Trending Now (US / Health, real-time)
Terms with a "Why:" line have a confirmed real-world news story driving the spike; terms without one are a real-time signal only, not yet grounded in a specific story.
  - vitruvias therapeutics hyperthyroidism risk recall
    Why: "Thyroid medication recalled as product can be 'superpotent,' FDA says" — WTHR

## Google Trends — 7-Day Interest (US)
  - **health**: latest=83, peak=100, 7d-delta=+0
    Rising related: what are the latest health updates from dolly parton and details on her new museum, chase stokes health issues, medvi health, dolly parton health, women s health clinic, dolly parton health update, neko health, king charles health
  - **wellness**: latest=72, peak=100, 7d-delta=-13
    Rising related: patagonia black hole duffel 100l tidal tea, shrek 5, civana wellness resort and spa, definition of wellness, routine wellness shampoo and conditioner reviews, us wellness meats, stack wellness cafe, wellness center
  - **nutrition**: latest=84, peak=100, 7d-delta=+5
    Rising related: curtain up, cooked versus raw vegetables nutrition, sundance kid, blue moon, nutrition channel, nutrition kid, dunkin nutrition calculator, supplemental nutrition assistance program
  - **fitness**: latest=68, peak=100, 7d-delta=-4
    Rising related: eric falstrault fitness transformation, muscle definition over 50 fitness, harley pasternak fitness advice, fintechzoom .io, hospitals, vegetables, million dollar things .com, fintechzoom.io
  - **food safety**: latest=22, peak=100, 7d-delta=+5
    Rising related: uc riverside dollar store study, project 2025 food supply, permanent daylight saving time winter sunsets, aldi game day snack container, ai apps students safety, project 2025 food, project 2025 food safety, project 2025
  - **diet**: latest=82, peak=100, 7d-delta=-4
    Rising related: vegan diet and inflammation, billy bob thornton diet, best free apps for productivity, healthy diet plan for beginners, best places to visit in casablanca, ai tools you should know in 2026, home bodyweight exercises workout, how to start freelancing online
  - **weight loss**: latest=63, peak=100, 7d-delta=+3
    Rising related: billy gardell weight loss transformation, gabe newell weight loss, tofa weight loss study berkeley, medvi quad reviews, medvi quad, quad ed, what is medvi, joinembody
  - **mental health**: latest=60, peak=100, 7d-delta=-5
    Rising related: free mental health services near me no insurance, what is sib in mental health, mychal threets mental health, in patient care mental health near me, how to improve mental health lwspeakcare, northern virginia mental health institute, definition of social health, inpatient mental health facilities near me
  - **gut health**: latest=62, peak=100, 7d-delta=-23
    Rising related: is farting a sign of good gut health, began public health and sanitation systems, seneca, importance of gut health, what is gut health, gut health foods, improve gut health, gut health probiotics

Top rising related queries from Google Trends:
  - what are the latest health updates from dolly parton and details on her new museum
  - chase stokes health issues
  - medvi health
  - dolly parton health
  - women s health clinic
  - dolly parton health update
  - neko health
  - king charles health
  - patagonia black hole duffel 100l tidal tea
  - shrek 5
  - civana wellness resort and spa
  - definition of wellness
  - routine wellness shampoo and conditioner reviews
  - us wellness meats
  - stack wellness cafe
  - wellness center
  - curtain up
  - cooked versus raw vegetables nutrition
  - sundance kid
  - blue moon

## Google News Radar — Recent Health Topics (144 unique across 12 queries; showing 60)
Treat these headlines as the broad radar of news-led health topics. The Signal Listener must consider this radar before narrowing to retained candidates.
  - (health) [Atrium Health] 08/22/2026, 01:19 AM, +0000 UTC — In partnership with Morehouse School of Medicine Atrium Health commits more than 700 million
    
    Link: https://atriumhealth.org/about-us/newsroom/news/2026/08/in-partnership-with-morehouse-school-of-medicine-atrium-health-commits-more-than-700-million
  - (health) [Maryland.gov] 08/24/2026, 07:13 PM, +0000 UTC — Pages - Maryland Department of Health declares measles outbreak in three Maryland counties
    
    Link: https://health.maryland.gov/newsroom/Pages/Maryland%20Department%20of%20Health%20declares%20measles%20outbreak%20in%20three%20Maryland%20counties.aspx
  - (health) [aphis.usda.gov] 08/21/2026, 07:00 AM, +0000 UTC — Confirmed Detections of New World Screwworm | Animal and Plant Health Inspection Service
    
    Link: https://www.aphis.usda.gov/animals/animal-health/livestock-and-poultry-disease/stop-screwworm/current-status/confirmed
  - (health) [nature.com] 08/20/2026, 10:21 AM, +0000 UTC — The hallmarks of skeletal muscle health
    
    Link: https://www.nature.com/articles/s42255-026-01595-9
  - (health) [Centers for Disease Control and Prevention | CDC (.gov)] 08/19/2026, 07:00 AM, +0000 UTC — Information for Travelers Returning from Ebola-Affected Areas
    
    Link: https://www.cdc.gov/ebola/situation-summary/returning-travelers.html
  - (health) [International Brotherhood of Teamsters] 08/20/2026, 03:41 PM, +0000 UTC — 10,000 Corewell Health East Nurses Ratify First Teamsters Contract
    
    Link: https://teamster.org/2026/08/10000-corewell-health-east-nurses-ratify-first-teamsters-contract/
  - (health) [Axios] 08/20/2026, 09:01 PM, +0000 UTC — Employer health costs: Why it could be another tough year
    
    Link: https://www.axios.com/2026/08/20/health-care-costs-employers-rising
  - (health) [Raiders.com] 08/24/2026, 05:02 PM, +0000 UTC — Las Vegas Raiders announce $25 million game-changing gift to Intermountain Health to help build Nevada's first stand-alone children's hospital
    
    Link: https://www.raiders.com/news/las-vegas-raiders-announce-25-million-game-changing-gift-to-intermountain-health-to-help-build-nevada-s-first-stand-alone-children-s-hospital
  - (health) [Think Global Health] 08/20/2026, 07:00 AM, +0000 UTC — Tracking Measles and the World's Vaccine-Preventable Diseases
    
    Link: https://www.thinkglobalhealth.org/article/vaccine-preventable-disease-a-global-tracker
  - (health) [University of Arizona News] 08/19/2026, 02:56 AM, +0000 UTC — U of A and Gila River Health Care (an entity of the Gila River Indian Community) launch nation's first MD-granting medical school branch within a Tribal Nation
    
    Link: https://news.arizona.edu/news/u-and-gila-river-health-care-entity-gila-river-indian-community-launch-nations-first-md
  - (health) [New Jersey Monitor] 08/19/2026, 08:59 PM, +0000 UTC — NJ panel deadlocks on vote to raise health premiums for teachers
    
    Link: https://newjerseymonitor.com/2026/08/19/nj-panel-deadlocks-on-vote-to-raise-health-premiums-for-teachers/
  - (health) [The New York Times] 08/19/2026, 10:44 PM, +0000 UTC — Senate Health Panel Chairman Voices Strong Reservations About F.D.A. Nominee
    
    Link: https://www.nytimes.com/2026/08/19/us/politics/heidi-overton-cassidy-fda.html
  - (wellness) [FOX 13 Tampa Bay] 08/21/2026, 03:26 AM, +0000 UTC — Wellness retreat project
    
    Link: https://www.fox13news.com/news/oxford-exchange-owners-plan-550-acre-wellness-retreat-near-dade-city
  - (wellness) [Yahoo Creators] 08/24/2026, 01:15 PM, +0000 UTC — Wellness stacking: why psychologists say it beats willpower for building healthy habits
    
    Link: https://creators.yahoo.com/lifestyle/story/wellness-stacking-why-psychologists-say-it-beats-willpower-for-building-healthy-habits-015140677.html
  - (wellness) [Marquette Today] 08/20/2026, 04:40 PM, +0000 UTC — Review your benefits with the Total Rewards Guide and Benefits and Wellness website
    
    Link: https://today.marquette.edu/2026/08/review-your-benefits-with-the-total-rewards-guide-and-benefits-and-wellness-website/
  - (wellness) [VA.gov Home | Veterans Affairs] 08/20/2026, 01:36 AM, +0000 UTC — Greenville VA HCC Celebrates Labyrinth Ribbon Cutting: A Pathway to Wellness
    
    Link: https://www.va.gov/durham-health-care/stories/greenville-va-hcc-celebrates-labyrinth-ribbon-cutting-a-pathway-to-wellness/
  - (wellness) [WFLA] 08/23/2026, 04:18 PM, +0000 UTC — 1 dead, officer hospitalized after attempted wellness check in St. Pete: PCSO
    
    Link: https://www.wfla.com/news/pinellas-county/1-dead-officer-hospitalized-after-attempted-wellness-check-in-st-pete-pcso/
  - (wellness) [The New York Times] 08/21/2026, 02:35 PM, +0000 UTC — ‘Spa Weekend’ Review: Girls Gone Wellness
    
    Link: https://www.nytimes.com/2026/08/21/movies/spa-weekend-review.html
  - (wellness) [Ground Truths | Eric Topol] 08/23/2026, 02:41 PM, +0000 UTC — Deborah Cohen: The Wellness-Industrial Complex
    
    Link: https://erictopol.substack.com/p/deborah-cohen-the-wellness-industrial
  - (wellness) [University of Evansville Athletics] 08/22/2026, 01:49 AM, +0000 UTC — Ali Adams promoted to Assistant AD for Student-Athlete Health & Wellness
    
    Link: https://gopurpleaces.com/news/2026/8/21/general-releases-ali-adams-promoted-to-assistant-ad-for-student-athlete-health-wellness.aspx
  - (wellness) [Condé Nast Traveler] 08/18/2026, 08:43 PM, +0000 UTC — Is Traveling for Stargazing the Next Big Wellness Craze? These Hotels Are Betting on It
    
    Link: https://www.cntraveler.com/story/is-traveling-for-stargazing-the-next-big-wellness-craze-these-hotels-are-betting-on-it
  - (wellness) [University of Nebraska Medical Center] 08/25/2026, 09:15 AM, +0000 UTC — Center for Healthy Living integrates fitness, wellness
    
    Link: https://www.unmc.edu/newsroom/2026/08/25/center-for-healthy-living-integrates-fitness-wellness/
  - (wellness) [WBAL-TV] 08/21/2026, 09:38 PM, +0000 UTC — Waterfront Wellness combines scenic views with working out
    
    Link: https://www.wbaltv.com/article/inner-harbor-free-fitness-program-baltimore/73495869
  - (wellness) [UCLA Health] 08/24/2026, 09:28 PM, +0000 UTC — Is a wellness drink worth it? Decoding functional beverage labels
    
    Link: https://www.uclahealth.org/news/article/wellness-drink-worth-it-decoding-functional-beverage-labels
  - (medical study) [NPR] 08/19/2026, 03:22 PM, +0000 UTC — A real-world study of Oregon's nonmedical psilocybin program shows promise
    
    Link: https://www.npr.org/2026/08/19/nx-s1-5936443/oregon-psilocybin-ptsd-depression-anxiety
  - (medical study) [Mount Sinai] 08/23/2026, 06:02 AM, +0000 UTC — Mount Sinai Study Finds Chemotherapy-Free Treatment Shows Promise for Some Patients With Metastatic Breast Cancer
    
    Link: https://www.mountsinai.org/about/newsroom/2026/mount-sinai-study-finds-chemotherapy-free-treatment-shows-promise-for-some-patients-with-metastatic-breast-cancer
  - (medical study) [Stanford Medicine] 08/19/2026, 09:51 PM, +0000 UTC — ‘Molecular glue’ turns a cancer driver into a built-in kill switch in Stanford Medicine study
    
    Link: https://med.stanford.edu/news/all-news/2026/08/lymphoma-BCL6-kill-switch.html
  - (medical study) [UMass Chan Medical School] 08/24/2026, 04:17 AM, +0000 UTC — UMass Chan researchers study psychedelic medication for adjustment disorder in people with serious medical conditions
    
    Link: https://www.umassmed.edu/news/articles/2026/08/umass-chan-researchers-study-psychedelic-medication-for-adjustment-disorder-in-people-with-serious-medical-conditions/
  - (medical study) [OHSU News] 08/19/2026, 03:09 PM, +0000 UTC — Study finds sustained benefit for people using Oregon psilocybin services
    
    Link: https://news.ohsu.edu/2026/08/19/study-finds-sustained-benefit-for-people-using-oregon-psilocybin-services
  - (medical study) [WSJ] 08/25/2026, 09:12 AM, +0000 UTC — Exclusive | Startup to Link ‘Biobanks’ of Patient Tissue to Supercharge AI Medical Research
    
    Link: https://www.wsj.com/pro/venture-capital/startup-to-link-biobanks-of-patient-tissue-to-supercharge-ai-medical-research-55403925
  - (medical study) [Nature] 08/19/2026, 10:17 AM, +0000 UTC — Large-scale AI-guided liver malignancy diagnosis: multicenter study and a single-arm trial
    
    Link: https://www.nature.com/articles/s41591-026-04589-y
  - (medical study) [MassDevice] 08/20/2026, 08:07 PM, +0000 UTC — Monteris Medical study shows critical survival factors for brain tumor patients
    
    Link: https://www.massdevice.com/monteris-medical-nueroblate-brain-tumor-study/
  - (medical study) [Ohio State News] 08/24/2026, 04:55 PM, +0000 UTC — Illicit fentanyl use is more than double medical use in US
    
    Link: https://news.osu.edu/illicit-fentanyl-use-is-more-than-double-medical-use-in-us/
  - (medical study) [University of California, Riverside] 08/21/2026, 03:49 PM, +0000 UTC — Study suggests new antibody therapy for tick-borne disease
    
    Link: https://news.ucr.edu/articles/2026/08/21/study-suggests-new-antibody-therapy-tick-borne-disease
  - (medical study) [Independent Institute] 08/21/2026, 12:36 AM, +0000 UTC — Artificial Intelligence Collides with FDA Bureaucracy: News Article
    
    Link: https://www.independent.org/article/2026/08/20/artificial-intelligence-fda/
  - (medical study) [Medical Xpress] 08/21/2026, 05:00 PM, +0000 UTC — Robotic assisted knee replacement gives same patient outcomes as surgeon-only procedure in clinical trial
    
    Link: https://medicalxpress.com/news/2026-08-robotic-knee-patient-outcomes-surgeon.html
  - (clinical trial health) [KFF Health News] 08/19/2026, 09:02 AM, +0000 UTC — You Want To Join a Clinical Trial. Here’s What To Know About the Hurdles.
    
    Link: https://kffhealthnews.org/health-industry/clinical-trials-patients-hhs-easier-advice-on-how-to-enroll-seriously-ill-cancer/
  - (clinical trial health) [The American Journal of Managed Care] 08/21/2026, 08:17 PM, +0000 UTC — Ochsner Health, Paradigm Health Partnership Expands Clinical Trial Access Across the Gulf South
    
    Link: https://www.ajmc.com/view/ochsner-health-paradigm-health-partnership-expands-clinical-trial-access-across-the-gulf-south
  - (clinical trial health) [PR Newswire] 08/18/2026, 10:19 PM, +0000 UTC — Curavit Expands Clinical Research Capabilities with Acquisition of Lindus Health CRO Assets, Accelerating Global Trial Execution for Life Science Sponsors
    
    Link: https://www.prnewswire.com/news-releases/curavit-expands-clinical-research-capabilities-with-acquisition-of-lindus-health-cro-assets-accelerating-global-trial-execution-for-life-science-sponsors-302854586.html
  - (clinical trial health) [Cancer Health] 08/25/2026, 03:13 AM, +0000 UTC — Clinical Trials Matter: What Our Patients Say
    
    Link: https://www.cancerhealth.com/article/clinical-trials-matter-patients-say
  - (clinical trial health) [The Clinical Trial Vanguard] 08/19/2026, 07:32 AM, +0000 UTC — When Your CRO Gets Acquired Mid-Study, Your Site Feels It First
    
    Link: https://www.clinicaltrialvanguard.com/clinical-trial-ops-brief/when-your-cro-gets-acquired-mid-study-your-site-feels-it-first/
  - (clinical trial health) [Applied Clinical Trials Online] 08/20/2026, 04:05 PM, +0000 UTC — Curavit Acquires Lindus Health Clinical Research Organization Assets to Expand US and European Trial Operations
    
    Link: https://www.appliedclinicaltrialsonline.com/view/curavit-acquires-lindus-health-clinical-research-organization-assets-expand-us-european-trial-operations
  - (clinical trial health) [Clinical Trials Arena] 08/20/2026, 11:01 AM, +0000 UTC — Reforms to UK clinical trial sector showing signs of success
    
    Link: https://www.clinicaltrialsarena.com/news/reforms-to-uk-clinical-trial-sector-showing-signs-of-success/
  - (clinical trial health) [South Carolina Daily Gazette] 08/19/2026, 04:18 PM, +0000 UTC — State-funded testing of COVID-19 treatment approved to start 3,000-person clinical trial
    
    Link: https://scdailygazette.com/2026/08/19/state-funded-testing-of-covid-19-treatment-approved-to-start-3000-person-clinical-trial/
  - (clinical trial health) [Nutrition Insight] 08/21/2026, 04:17 PM, +0000 UTC — Perelel’s Triple-Support protein shows promise for women’s health in clinical trial
    
    Link: https://www.nutritioninsight.com/news/perelel-triple-support-protein-womens-health.html
  - (clinical trial health) [MedTech Dive] 08/21/2026, 04:30 PM, +0000 UTC — How can wearables be used in clinical trials? FDA outlines best practices
    
    Link: https://www.medtechdive.com/news/how-can-wearables-be-used-in-clinical-trials-fda-outlines-best-practices/828512/
  - (clinical trial health) [Straits Research] 08/19/2026, 07:00 AM, +0000 UTC — Clinical Trials Market Size, Share, Growth, Analysis, Report, 2034
    
    Link: https://straitsresearch.com/report/clinical-trials-market
  - (clinical trial health) [Flow Space] 08/19/2026, 06:06 PM, +0000 UTC — 8 Shocking Facts About Women in Medical Research That Will Make You Say, ‘Seriously?’
    
    Link: https://www.theflowspace.com/interpersonal-health/access-equity/women-clinical-trials-statistics-3039955/
  - (FDA recall health) [The New York Times] 08/19/2026, 07:00 AM, +0000 UTC — F.D.A. Classifies Egg Recall as Class I, for Highest Health Risk
    
    Link: https://www.nytimes.com/2026/08/14/health/fda-egg-recall-salmonella.html
  - (FDA recall health) [CBS News] 08/19/2026, 10:52 PM, +0000 UTC — FDA upgrades recall of frozen blueberries sold at Publix to highest health risk level
    
    Link: https://www.cbsnews.com/news/blueberry-recall-fda-class-1-risk/
  - (FDA recall health) [fda.gov] 08/21/2026, 05:01 PM, +0000 UTC — Outbreak Investigation of Shiga Toxin-producing E. coli & Salmonella: Sprouts (August 2026)
    
    Link: https://www.fda.gov/food/outbreaks-foodborne-illness/outbreak-investigation-shiga-toxin-producing-e-coli-salmonella-sprouts-august-2026
  - (FDA recall health) [Axios] 08/22/2026, 10:01 AM, +0000 UTC — Here's why the FDA hit frozen blueberries with its highest risk warning
    
    Link: https://www.axios.com/2026/08/22/frozen-blueberries-recall-fda-high-risk-warning
  - (FDA recall health) [The Washington Post] 08/21/2026, 12:15 AM, +0000 UTC — FDA upgrades recall of frozen berries to highest-risk warning
    
    Link: https://www.washingtonpost.com/health/2026/08/20/fda-upgrades-recall-frozen-berries-highest-risk-warning/
  - (FDA recall health) [Healthline] 08/20/2026, 06:18 PM, +0000 UTC — FDA Upgrades Publix Frozen Blueberry Recall to Highest Health Risk Level
    
    Link: https://www.healthline.com/health-news/fda-upgrades-publix-frozen-blueberry-recall-highest-risk-level
  - (FDA recall health) [Centers for Disease Control and Prevention | CDC (.gov)] 08/20/2026, 07:00 AM, +0000 UTC — Cyclospora Outbreak Linked to Iceberg Lettuce | Cyclosporiasis
    
    Link: https://www.cdc.gov/cyclosporiasis/outbreaks/07-26/index.html
  - (FDA recall health) [NewsNation] 08/22/2026, 12:29 PM, +0000 UTC — Food recalls aren’t a success story, former FDA official says
    
    Link: https://www.newsnationnow.com/health/food-recalls-arent-success-story-former-fda-official/
  - (FDA recall health) [11Alive.com] 08/20/2026, 02:42 PM, +0000 UTC — Blueberry recall in 8 states upgraded to FDA's highest health risk level
    
    Link: https://www.11alive.com/article/news/nation-world/blueberry-recall-in-8-states-upgraded-to-most-dangerous-classification/507-13ecdd2b-9e5a-427c-b889-b6d394d180c4
  - (FDA recall health) [88.5 WFDD] 08/20/2026, 09:04 PM, +0000 UTC — FDA moves Publix frozen berry E. coli recall to Class I health risk
    
    Link: https://www.wfdd.org/health-safety/2026-08-20/fda-moves-publix-frozen-berry-e-coli-recall-to-class-i-health-risk
  - (FDA recall health) [WRAL] 08/21/2026, 03:40 PM, +0000 UTC — Publix frozen berry recall upgraded to FDA’s highest-risk level
    
    Link: https://www.wral.com/consumer/5onyourside/publix-blueberry-recall-upgraded-august-2026/
  - (FDA recall health) [Good Housekeeping] 08/19/2026, 07:43 PM, +0000 UTC — FDA Announces Nationwide Recall of Popular Ice Pops Sold at Multiple Retailers—Here’s the Full List
    
    Link: https://www.goodhousekeeping.com/food-products/a73468917/outshine-fruit-bars-recall/