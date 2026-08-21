# LIVE SIGNAL DATA — SerpAPI Pre-Fetch
The following signals were fetched from SerpAPI Google News and SerpAPI Google Trends immediately before this pipeline run. Treat Google Trends as AVAILABLE when this section contains a Google Trends block. Use it as the primary search_velocity input for Skills 01–05 (Signal Listener through Trend Strength Scorer). Use the Google News Radar as the broad discovery layer for news-led health topics, including topics that do not yet appear in Google Trends. Prioritize topics with convergence across News, Trends, primary/institutional sources, and credible publisher coverage.

## Google Trends — Trending Now (US / Health, real-time)
Terms with a "Why:" line have a confirmed real-world news story driving the spike; terms without one are a real-time signal only, not yet grounded in a specific story.
  - executive order
    Why: "Opinion | I helped develop the rotavirus vaccine. Trump’s overhaul makes me sick." — The Washington Post

## Google Trends — 7-Day Interest (US)
  - **health**: latest=67, peak=100, 7d-delta=-9
    Rising related: hayden panettiere mental health, did hayden panettiere have health issues, hayden panettiere health problems, mitch mcconnell health, novant health new hanover regional medical center, sprinter health careers, dignity health sports park, zocalo health careers
  - **wellness**: latest=70, peak=100, 7d-delta=-11
    Rising related: circle wellness seattle, barker wellness, social health definition, the wellness company medical emergency kit, koniver wellness, routine wellness shampoo and conditioner reviews, civana wellness resort and spa, the wellness company emergency kit
  - **nutrition**: latest=92, peak=100, 7d-delta=+7
    Rising related: curtain up, action channel, sundance kid, unicorn frappe nutrition facts, blue moon, supplemental nutrition assistance program, nutrition facts, nutrition label
  - **fitness**: latest=56, peak=100, 7d-delta=-1
    Rising related: eric falstrault fitness transformation, casio f-b100w fitness tracker, million dollar things .com, fintechzoom.io, how to cancel planet fitness membership online, planet fitness customer service phone number, planet fitness customer service number, planet fitness customer service
  - **food safety**: latest=29, peak=100, 7d-delta=-7
    Rising related: local health codes establish requirements for all of the following subjects except, blueberry recall, ai apps students safety, bitcoin price august 20 2026, moderna melanoma vaccine, which activity is an example of poor personal hygiene, trump iran latest today, dog food
  - **diet**: latest=73, peak=100, 7d-delta=-6
    Rising related: vegan diet and inflammation, plant-based diet, miranda kerr diet, what is the difference between diet coke and coke zero, whats the difference between diet coke and coke zero, difference between coke zero and diet coke, mind diet, diet coke
  - **weight loss**: latest=89, peak=100, 7d-delta=+22
    Rising related: billy gardell weight loss transformation, gabe newell weight loss, gabe newell, best glp 1 supplement for weight loss, bronson reed, bronson reed weight loss, bridget fonda weight loss, tucker carlson weight loss
  - **mental health**: latest=57, peak=100, 7d-delta=-20
    Rising related: hayden panettiere mental health, hayden panettiere mental health issues, did hayden panettiere have mental health issues, mychal threets mental health, northern virginia mental health institute, selena gomez mental health company, physical health definition, maternal mental health hotline
  - **gut health**: latest=47, peak=100, 7d-delta=+2
    Rising related: research on family estrangement, bristol stool chart usage, best morning drink for gut health, is apple cider vinegar good for gut health, gut health dietitian, l glutamine benefits, how to fix gut health fast, good gut health

Top rising related queries from Google Trends:
  - hayden panettiere mental health
  - did hayden panettiere have health issues
  - hayden panettiere health problems
  - mitch mcconnell health
  - novant health new hanover regional medical center
  - sprinter health careers
  - dignity health sports park
  - zocalo health careers
  - circle wellness seattle
  - barker wellness
  - social health definition
  - the wellness company medical emergency kit
  - koniver wellness
  - routine wellness shampoo and conditioner reviews
  - civana wellness resort and spa
  - the wellness company emergency kit
  - curtain up
  - action channel
  - sundance kid
  - unicorn frappe nutrition facts

## Google News Radar — Recent Health Topics (144 unique across 12 queries; showing 60)
Treat these headlines as the broad radar of news-led health topics. The Signal Listener must consider this radar before narrowing to retained candidates.
  - (health) [HHS.gov] 08/17/2026, 07:06 PM, +0000 UTC — HHS Awards Over $96 Million to Strengthen Mental Health, Suicide Prevention, and Substance Use Disorder Services
    
    Link: https://www.hhs.gov/press-room/hhs-awards-96-million-mental-health-suicide-prevention-substance-use-services.html
  - (health) [ICRC] 08/19/2026, 08:03 AM, +0000 UTC — Protection of health care
    
    Link: https://www.icrc.org/en/law-and-policy/protection-health-care
  - (health) [Nature] 08/20/2026, 10:21 AM, +0000 UTC — The hallmarks of skeletal muscle health
    
    Link: https://www.nature.com/articles/s42255-026-01595-9
  - (health) [International Brotherhood of Teamsters] 08/20/2026, 03:41 PM, +0000 UTC — 10,000 Corewell Health East Nurses Ratify First Teamsters Contract
    
    Link: https://teamster.org/2026/08/10000-corewell-health-east-nurses-ratify-first-teamsters-contract/
  - (health) [Axios] 08/16/2026, 10:00 AM, +0000 UTC — How AI could bring Mayo-quality health care to everyone
    
    Link: https://www.axios.com/2026/08/16/ai-mayo-clinic-health-care-fix-jim-vandehei
  - (health) [MPR News] 08/15/2026, 12:00 PM, +0000 UTC — Health insurance rates expected to climb again for Minnesotans in 2027
    
    Link: https://www.mprnews.org/story/2026/08/15/minnesota-health-insurance-rates-expected-to-climb-in-2027
  - (health) [University of Arizona News] 08/19/2026, 02:56 AM, +0000 UTC — U of A and Gila River Health Care (an entity of the Gila River Indian Community) launch nation's first MD-granting medical school branch within a Tribal Nation
    
    Link: https://news.arizona.edu/news/u-and-gila-river-health-care-entity-gila-river-indian-community-launch-nations-first-md
  - (health) [VTDigger] 08/17/2026, 03:18 PM, +0000 UTC — Dartmouth Health says it needs to close telehealth services for emergency and intensive care
    
    Link: https://vtdigger.org/2026/08/17/dartmouth-health-says-it-needs-to-close-telehealth-services-for-emergency-and-intensive-care/
  - (health) [New Jersey Monitor] 08/19/2026, 08:59 PM, +0000 UTC — NJ panel deadlocks on vote to raise health premiums for teachers
    
    Link: https://newjerseymonitor.com/2026/08/19/nj-panel-deadlocks-on-vote-to-raise-health-premiums-for-teachers/
  - (health) [The New York Times] 08/20/2026, 02:32 PM, +0000 UTC — Senate Health Panel Chairman Voices Strong Reservations About F.D.A. Nominee
    
    Link: https://www.nytimes.com/2026/08/19/us/politics/heidi-overton-cassidy-fda.html
  - (health) [CNBC] 08/16/2026, 07:58 PM, +0000 UTC — Top U.S. commander acknowledges mental health issues on USS Lincoln
    
    Link: https://www.cnbc.com/2026/08/16/top-us-commander-acknowledges-mental-health-issues-on-uss-lincoln.html
  - (health) [NPR] 08/18/2026, 07:03 PM, +0000 UTC — In Good Health: Finding A Primary Care Physician : 1A
    
    Link: https://www.npr.org/2026/08/18/nx-s1-5936484/in-good-health-finding-a-primary-care-physician
  - (wellness) [GQ] 08/17/2026, 05:13 PM, +0000 UTC — The Latest Dating Dilemma: Wellness Gap Relationships
    
    Link: https://www.gq.com/story/dating-wellness-gap-relationships
  - (wellness) [Marquette Today] 08/20/2026, 04:40 PM, +0000 UTC — Review your benefits with the Total Rewards Guide and Benefits and Wellness website
    
    Link: https://today.marquette.edu/2026/08/review-your-benefits-with-the-total-rewards-guide-and-benefits-and-wellness-website/
  - (wellness) [FOX 13 Tampa Bay] 08/21/2026, 03:26 AM, +0000 UTC — Wellness retreat project
    
    Link: https://www.fox13news.com/news/oxford-exchange-owners-plan-550-acre-wellness-retreat-near-dade-city
  - (wellness) [UNM Newsroom] 08/18/2026, 10:12 PM, +0000 UTC — COEHS wellness services strengthen communities, prepare future professionals
    
    Link: https://news.unm.edu/news/coehs-wellness-services-strengthen-communities-prepare-future-professionals
  - (wellness) [PR Newswire] 08/14/2026, 03:00 PM, +0000 UTC — FERRERO GROUP TO ACQUIRE PURELY ELIZABETH, A LEADING U.S. MODERN WELLNESS BRAND
    
    Link: https://www.prnewswire.com/news-releases/ferrero-group-to-acquire-purely-elizabeth-a-leading-us-modern-wellness-brand-302851234.html
  - (wellness) [WFAA] 08/20/2026, 06:39 PM, +0000 UTC — 'Maxxing': When wellness trends push too far
    
    Link: https://www.wfaa.com/article/news/nation-world/maxxing-when-wellness-trends-push-too-far-social-media/507-66db9ae3-36a1-4437-92d3-f9f3c898156b
  - (wellness) [BYU Life Sciences] 08/18/2026, 02:00 PM, +0000 UTC — The Arroyo Lab: Bridging Metabolic Research and Maternal Wellness
    
    Link: https://lifesciences.byu.edu/the-arroyo-lab-bridging-metabolic-research-and-maternal-wellness
  - (wellness) [The Santa Barbara Independent] 08/19/2026, 08:10 PM, +0000 UTC — County Behavioral Wellness Accepting Annual Applications for John Kovacs Scholarship Awards
    
    Link: https://www.independent.com/2026/08/19/county-behavioral-wellness-accepting-annual-applications-for-john-kovacs-scholarship-awards-3/
  - (wellness) [KARK] 08/19/2026, 08:00 PM, +0000 UTC — National wellness month
    
    Link: https://www.kark.com/arkansas-style/national-wellness-month/
  - (wellness) [Finovate] 08/19/2026, 04:15 PM, +0000 UTC — 9 Fintechs Personalizing Customer Engagement and Financial Wellness
    
    Link: https://finovate.com/9-fintechs-personalizing-customer-engagement-and-financial-wellness/
  - (wellness) [Upper Michigan's Source] 08/20/2026, 12:40 PM, +0000 UTC — How you can promote wellness during National Wellness Month
    
    Link: https://www.uppermichiganssource.com/2026/08/20/how-you-can-promote-wellness-during-national-wellness-month/
  - (wellness) [MLB.com] 08/19/2026, 07:41 PM, +0000 UTC — MLB Together teaches mental wellness at RBI World Series
    
    Link: https://www.mlb.com/news/rbi-world-series-mlb-together-mental-wellness-event-2026
  - (medical study) [Harvard Medical School] 08/17/2026, 04:05 PM, +0000 UTC — Pilots, Flight Attendants Have Greater Risk of Radiation-Related Cancer Death Than Other Professions
    
    Link: https://hms.harvard.edu/news/pilots-flight-attendants-have-greater-risk-radiation-related-cancer-death-other-professions
  - (medical study) [University of Nebraska Medical Center] 08/18/2026, 07:31 PM, +0000 UTC — Medical research highlights, summer 2026
    
    Link: https://www.unmc.edu/newsroom/2026/08/18/medical-research-highlights-summer-2026/
  - (medical study) [NPR] 08/19/2026, 03:22 PM, +0000 UTC — A real-world study of Oregon's nonmedical psilocybin program shows promise
    
    Link: https://www.npr.org/2026/08/19/nx-s1-5936443/oregon-psilocybin-ptsd-depression-anxiety
  - (medical study) [Michigan Medicine] 08/19/2026, 12:00 PM, +0000 UTC — College of Pharmacy alum advances U-M Medical School addiction research
    
    Link: https://www.michiganmedicine.org/philanthropy-news/college-pharmacy-alum-advances-u-m-medical-school-addiction-research
  - (medical study) [Stanford Medicine] 08/19/2026, 09:51 PM, +0000 UTC — ‘Molecular glue’ turns a cancer driver into a built-in kill switch in Stanford Medicine study
    
    Link: https://med.stanford.edu/news/all-news/2026/08/lymphoma-BCL6-kill-switch.html
  - (medical study) [RAPS] 08/18/2026, 12:00 PM, +0000 UTC — Study highlights limits of premarket evaluation for identifying recalls of high-risk medical devices
    
    Link: https://www.raps.org/resource/study-highlights-limits-of-premarket-evaluation-for-identifying-recalls-of-high-risk-medical-devices.html
  - (medical study) [American Cancer Society Press Room] 08/18/2026, 02:02 PM, +0000 UTC — County-Level Medical Debt Linked to Advanced-Stage Cancers and Worse Survival Among Newly Diagnosed U.S. Adults
    
    Link: https://pressroom.cancer.org/medical-debt-linked-to-worse-survival
  - (medical study) [Nature] 08/19/2026, 10:08 AM, +0000 UTC — Genomic meta-analyses of binge-eating behavior and anorexia nervosa yield insights into the unique and shared biology of eating disorder phenotypes
    
    Link: https://www.nature.com/articles/s44220-026-00698-2
  - (medical study) [WSJ] 08/19/2026, 09:30 AM, +0000 UTC — Exclusive | Startup to Link ‘Biobanks’ of Patient Tissue to Supercharge AI Medical Research
    
    Link: https://www.wsj.com/pro/venture-capital/startup-to-link-biobanks-of-patient-tissue-to-supercharge-ai-medical-research-55403925
  - (medical study) [University of South Florida] 08/19/2026, 02:35 PM, +0000 UTC — USF Health research reveals new clues about how space travel may affect women’s health
    
    Link: https://www.usf.edu/health/news/2026/usf-health-research-reveals-new-clues-about-how-space-travel-may-affect-womens-health.aspx
  - (medical study) [WashU Medicine] 08/17/2026, 08:03 PM, +0000 UTC — Laser therapy offers weapon against deadly brain tumors
    
    Link: https://medicine.washu.edu/news/laser-therapy-offers-weapon-against-deadly-brain-tumors/
  - (medical study) [KSWO 7News] 08/20/2026, 12:50 AM, +0000 UTC — State legislators to hold study examining medical marijuana in October
    
    Link: https://www.kswo.com/2026/08/20/state-legislators-hold-study-examining-medical-marijuana-october/
  - (clinical trial health) [KFF Health News] 08/19/2026, 09:02 AM, +0000 UTC — You Want To Join a Clinical Trial. Here’s What To Know About the Hurdles.
    
    Link: https://kffhealthnews.org/health-industry/clinical-trials-patients-hhs-easier-advice-on-how-to-enroll-seriously-ill-cancer/
  - (clinical trial health) [Mass General Brigham] 08/18/2026, 07:00 AM, +0000 UTC — Mass General Brigham Launches Clinical Trials Focused on Home Hospital Treatment for Dementia and Behavioral Health Conditions
    
    Link: https://www.massgeneralbrigham.org/en/newsroom/clinical-trials-of-home-hospital-treatment-for-dementia
  - (clinical trial health) [The Clinical Trial Vanguard] 08/19/2026, 07:32 AM, +0000 UTC — When Your CRO Gets Acquired Mid-Study, Your Site Feels It First
    
    Link: https://www.clinicaltrialvanguard.com/clinical-trial-ops-brief/when-your-cro-gets-acquired-mid-study-your-site-feels-it-first/
  - (clinical trial health) [The New York Times] 08/18/2026, 07:00 AM, +0000 UTC — A Hopeless Diagnosis? Not for This Patient.
    
    Link: https://www.nytimes.com/2026/08/17/science/clinical-trial-jansens-disease-nizar-nih.html
  - (clinical trial health) [Applied Clinical Trials Online] 08/18/2026, 03:48 PM, +0000 UTC — Syneos Health Expands AI Ecosystem With Three New Platform Partnerships
    
    Link: https://www.appliedclinicaltrialsonline.com/view/syneos-health-expands-ai-ecosystem-three-new-platform-partnerships
  - (clinical trial health) [PR Newswire] 08/18/2026, 10:19 PM, +0000 UTC — Curavit Expands Clinical Research Capabilities with Acquisition of Lindus Health CRO Assets, Accelerating Global Trial Execution for Life Science Sponsors
    
    Link: https://www.prnewswire.com/news-releases/curavit-expands-clinical-research-capabilities-with-acquisition-of-lindus-health-cro-assets-accelerating-global-trial-execution-for-life-science-sponsors-302854586.html
  - (clinical trial health) [South Carolina Daily Gazette] 08/19/2026, 04:18 PM, +0000 UTC — State-funded testing of COVID-19 treatment approved to start 3,000-person clinical trial
    
    Link: https://scdailygazette.com/2026/08/19/state-funded-testing-of-covid-19-treatment-approved-to-start-3000-person-clinical-trial/
  - (clinical trial health) [Clinical Trials Arena] 08/20/2026, 11:01 AM, +0000 UTC — Reforms to UK clinical trial sector showing signs of success
    
    Link: https://www.clinicaltrialsarena.com/news/reforms-to-uk-clinical-trial-sector-showing-signs-of-success/
  - (clinical trial health) [Oncodaily] 08/17/2026, 05:07 PM, +0000 UTC — Accelerating Clinical Trial Approvals Across Africa – Global Health Otherwise
    
    Link: https://oncodaily.com/new-paper-alert/global-health-otherwise-568437
  - (clinical trial health) [ABC News - Breaking News, Latest News and Videos] 08/19/2026, 06:34 AM, +0000 UTC — Moderna begins Phase 1 clinical trial of Ebola vaccine against strain behind DRC outbreak
    
    Link: https://abcnews.com/Health/moderna-begins-phase-1-clinical-trial-ebola-vaccine/story?id=135365177
  - (clinical trial health) [American Hospital Association] 08/15/2026, 07:53 PM, +0000 UTC — West Virginia University Health System's clinical trial offers hope for a rare and deadly blood cancer
    
    Link: https://www.aha.org/tellingthehospitalstory/stories/university-west-virginia-clinical-trial-offers-hope-rare-and-deadly-blood-cancer
  - (clinical trial health) [News-Medical] 08/20/2026, 05:52 PM, +0000 UTC — Federal and industry sponsors play complementary roles in cancer clinical trials
    
    Link: https://www.news-medical.net/news/20260820/Federal-and-industry-sponsors-play-complementary-roles-in-cancer-clinical-trials.aspx
  - (FDA recall health) [The New York Times] 08/19/2026, 07:00 AM, +0000 UTC — F.D.A. Classifies Egg Recall as Class I, for Highest Health Risk
    
    Link: https://www.nytimes.com/2026/08/14/health/fda-egg-recall-salmonella.html
  - (FDA recall health) [CBS News] 08/19/2026, 10:52 PM, +0000 UTC — FDA upgrades recall of frozen blueberries sold at Publix to highest health risk level
    
    Link: https://www.cbsnews.com/news/blueberry-recall-fda-class-1-risk/
  - (FDA recall health) [CIDRAP] 08/17/2026, 08:27 PM, +0000 UTC — FDA heightens egg recall to reflect potential ‘serious adverse health consequences or death’
    
    Link: https://www.cidrap.umn.edu/foodborne-disease/fda-heightens-egg-recall-reflect-potential-serious-adverse-health-consequences-or
  - (FDA recall health) [El Paso Times] 08/15/2026, 02:51 PM, +0000 UTC — FDA upgrades egg recall to Class I. What it means
    
    Link: https://www.elpasotimes.com/story/news/health/2026/08/15/egg-recall-upgraded-by-fda-to-class-i-what-that-means/91317478007/
  - (FDA recall health) [Time Magazine] 08/15/2026, 03:47 PM, +0000 UTC — Salmonella Egg Recall Is Now Class I, the FDA’s Highest Risk Level
    
    Link: https://time.com/article/2026/08/15/eggs-recalled-for-salmonella-upgraded-to-highest-fda-risk-level/
  - (FDA recall health) [Denver7] 08/18/2026, 12:25 AM, +0000 UTC — FDA upgrades egg recall to highest health-risk level amid string of food safety concerns
    
    Link: https://www.denver7.com/news/local-news/fda-upgrades-egg-recall-to-highest-health-risk-level-amid-string-of-food-safety-concerns
  - (FDA recall health) [11Alive.com] 08/20/2026, 02:42 PM, +0000 UTC — Blueberry recall in 8 states upgraded to FDA's highest health risk level
    
    Link: https://www.11alive.com/article/news/nation-world/blueberry-recall-in-8-states-upgraded-to-most-dangerous-classification/507-13ecdd2b-9e5a-427c-b889-b6d394d180c4
  - (FDA recall health) [Healthline] 08/20/2026, 06:18 PM, +0000 UTC — FDA Upgrades Publix Frozen Blueberry Recall to Highest Health Risk Level
    
    Link: https://www.healthline.com/health-news/fda-upgrades-publix-frozen-blueberry-recall-highest-risk-level
  - (FDA recall health) [Health.com] 08/18/2026, 06:58 PM, +0000 UTC — The FDA Just Announced a Recall on Bladder Medication Nationwide
    
    Link: https://www.health.com/bladder-medication-recall-august-2026-12062630
  - (FDA recall health) [The Washington Post] 08/21/2026, 12:15 AM, +0000 UTC — FDA upgrades recall of frozen berries to highest-risk warning
    
    Link: https://www.washingtonpost.com/health/2026/08/20/fda-upgrades-recall-frozen-berries-highest-risk-warning/
  - (FDA recall health) [Ophthalmology Times] 08/20/2026, 11:01 AM, +0000 UTC — FDA recalls eye drop that relieves ocular itch for potential contamination
    
    Link: https://www.ophthalmologytimes.com/view/fda-recall-eye-drop-that-relieves-ocular-itch-potential-contamination
  - (FDA recall health) [dw.com] 08/15/2026, 03:55 AM, +0000 UTC — US: 19 million eggs recalled over salmonella risk
    
    Link: https://www.dw.com/en/us-food-and-drug-administration-fda-recalls-19-million-eggs-over-salmonella-risk/a-78378361