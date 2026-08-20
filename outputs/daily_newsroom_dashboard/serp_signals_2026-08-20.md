# LIVE SIGNAL DATA — SerpAPI Pre-Fetch
The following signals were fetched from SerpAPI Google News and SerpAPI Google Trends immediately before this pipeline run. Treat Google Trends as AVAILABLE when this section contains a Google Trends block. Use it as the primary search_velocity input for Skills 01–05 (Signal Listener through Trend Strength Scorer). Use the Google News Radar as the broad discovery layer for news-led health topics, including topics that do not yet appear in Google Trends. Prioritize topics with convergence across News, Trends, primary/institutional sources, and credible publisher coverage.

## Google Trends — Trending Now (US / Health, real-time)
Terms with a "Why:" line have a confirmed real-world news story driving the spike; terms without one are a real-time signal only, not yet grounded in a specific story.
  - executive order
    Why: "Opinion | I helped develop the rotavirus vaccine. Trump’s overhaul makes me sick." — The Washington Post
  - va
    Why: "VA boosts EHR modernization contract with Oracle by $17B" — Nextgov/FCW
  - va news
    Why: "Roudebush VA leads nationwide health record system rollout" — WISH-TV

## Google Trends — 7-Day Interest (US)
  - **health**: latest=79, peak=100, 7d-delta=+6
    Rising related: hayden panettiere mental health, did hayden panettiere have health issues, hayden panettiere health problems, mitch mcconnell health, sprinter health careers, novant health new hanover regional medical center, zocalo health careers, dignity health sports park
  - **wellness**: latest=75, peak=100, 7d-delta=-3
    Rising related: circle wellness seattle, koniver wellness, barker wellness, health definition, routine wellness shampoo and conditioner reviews, civana wellness resort and spa, wellness definition, wellness center
  - **nutrition**: latest=84, peak=100, 7d-delta=-5
    Rising related: unicorn frappe nutrition facts, supplemental nutrition assistance program, nutrition facts, nutrition calculator, egg nutrition, optimum nutrition, chipotle nutrition, potato nutrition
  - **fitness**: latest=57, peak=100, 7d-delta=-1
    Rising related: eric falstrault fitness transformation, casio f-b100w fitness tracker, how to cancel planet fitness membership online, planet fitness customer service, cancel planet fitness membership, how do i cancel my planet fitness membership, how to cancel planet fitness membership, group fitness classes
  - **food safety**: latest=32, peak=100, 7d-delta=-4
    Rising related: 2026 food safety recall trends, food safety and standards authority of india, food safety modernization act, pathogens grow well between which temperatures, food safety certification nyc, food safety management, what is food safety, fda
  - **diet**: latest=79, peak=100, 7d-delta=-1
    Rising related: vegan diet and inflammation, plant-based diet, what is the difference between diet coke and coke zero, miranda kerr diet, diet coke, mediterranean diet, keto diet, science diet
  - **weight loss**: latest=59, peak=100, 7d-delta=+0
    Rising related: best glp 1 supplement for weight loss, margaret cho weight loss, bridget fonda weight loss, bronson reed weight loss, nicole byer weight loss, ethan suplee weight loss, jenna ortega before and after weight loss, erin burnett weight loss
  - **mental health**: latest=73, peak=100, 7d-delta=+3
    Rising related: hayden panettiere mental health, hayden panettiere mental health issues, did hayden panettiere have mental health issues, selena gomez mental health company, mychal threets mental health, selena gomez mental health, northern virginia mental health institute, safety plan template for mental health
  - **gut health**: latest=27, peak=100, 7d-delta=-7
    Rising related: bristol stool chart usage, years of trump support came undone in 15 minutes in an airport, mitch mcconnell health, cognition, dreyer's outshine fruit bars recall, holistic gut health doctor near me, gut health specialist near me, is farting a sign of good gut health

Top rising related queries from Google Trends:
  - hayden panettiere mental health
  - did hayden panettiere have health issues
  - hayden panettiere health problems
  - mitch mcconnell health
  - sprinter health careers
  - novant health new hanover regional medical center
  - zocalo health careers
  - dignity health sports park
  - circle wellness seattle
  - koniver wellness
  - barker wellness
  - health definition
  - routine wellness shampoo and conditioner reviews
  - civana wellness resort and spa
  - wellness definition
  - wellness center
  - unicorn frappe nutrition facts
  - supplemental nutrition assistance program
  - nutrition facts
  - nutrition calculator

## Google News Radar — Recent Health Topics (144 unique across 12 queries; showing 60)
Treat these headlines as the broad radar of news-led health topics. The Signal Listener must consider this radar before narrowing to retained candidates.
  - (health) [Centers for Disease Control and Prevention | CDC (.gov)] 08/18/2026, 07:00 AM, +0000 UTC — Surveillance of Cyclosporiasis
    
    Link: https://www.cdc.gov/cyclosporiasis/php/surveillance/index.html
  - (health) [HHS.gov] 08/17/2026, 07:06 PM, +0000 UTC — HHS Awards Over $96 Million to Strengthen Mental Health, Suicide Prevention, and Substance Use Disorder Services
    
    Link: https://www.hhs.gov/press-room/hhs-awards-96-million-mental-health-suicide-prevention-substance-use-services.html
  - (health) [Axios] 08/16/2026, 10:00 AM, +0000 UTC — How AI could bring Mayo-quality health care to everyone
    
    Link: https://www.axios.com/2026/08/16/ai-mayo-clinic-health-care-fix-jim-vandehei
  - (health) [Nature] 08/20/2026, 10:21 AM, +0000 UTC — The hallmarks of skeletal muscle health
    
    Link: https://www.nature.com/articles/s42255-026-01595-9
  - (health) [MPR News] 08/15/2026, 12:00 PM, +0000 UTC — Health insurance rates expected to climb again for Minnesotans in 2027
    
    Link: https://www.mprnews.org/story/2026/08/15/minnesota-health-insurance-rates-expected-to-climb-in-2027
  - (health) [VTDigger] 08/17/2026, 03:18 PM, +0000 UTC — Dartmouth Health says it needs to close telehealth services for emergency and intensive care
    
    Link: https://vtdigger.org/2026/08/17/dartmouth-health-says-it-needs-to-close-telehealth-services-for-emergency-and-intensive-care/
  - (health) [University of Arizona News] 08/19/2026, 02:56 AM, +0000 UTC — U of A and Gila River Health Care (an entity of the Gila River Indian Community) launch nation's first MD-granting medical school branch within a Tribal Nation
    
    Link: https://news.arizona.edu/news/u-and-gila-river-health-care-entity-gila-river-indian-community-launch-nations-first-md
  - (health) [The New York Times] 08/20/2026, 02:32 PM, +0000 UTC — Senate Health Panel Chairman Voices Strong Reservations About F.D.A. Nominee
    
    Link: https://www.nytimes.com/2026/08/19/us/politics/heidi-overton-cassidy-fda.html
  - (health) [CNBC] 08/16/2026, 07:58 PM, +0000 UTC — Top U.S. commander acknowledges mental health issues on USS Lincoln
    
    Link: https://www.cnbc.com/2026/08/16/top-us-commander-acknowledges-mental-health-issues-on-uss-lincoln.html
  - (health) [NPR] 08/18/2026, 07:03 PM, +0000 UTC — In Good Health: Finding A Primary Care Physician : 1A
    
    Link: https://www.npr.org/2026/08/18/nx-s1-5936484/in-good-health-finding-a-primary-care-physician
  - (health) [UN News] 08/14/2026, 04:41 PM, +0000 UTC — An attack on healthcare every six hours, and no one held to account
    
    Link: https://news.un.org/en/story/2026/08/1168144
  - (health) [health.com] 08/18/2026, 02:12 PM, +0000 UTC — 6 Signs Your Gut Health Is Out of Balance
    
    Link: https://www.health.com/signs-gut-health-out-of-balance-12061251
  - (wellness) [GQ] 08/17/2026, 05:13 PM, +0000 UTC — The Latest Dating Dilemma: Wellness Gap Relationships
    
    Link: https://www.gq.com/story/dating-wellness-gap-relationships
  - (wellness) [University of Nebraska Medical Center] 08/18/2026, 09:33 AM, +0000 UTC — Registration open for women’s health and wellness conference
    
    Link: https://www.unmc.edu/newsroom/2026/08/18/registration-open-for-womens-health-and-wellness-conference/
  - (wellness) [The Capitol Forum] 08/14/2026, 07:00 AM, +0000 UTC — FDA Weighs Compounding Approval for Wellness Peptides
    
    Link: https://thecapitolforum.com/a-closer-look-at-fdas-next-steps-following-advisory-committees-recommendation-to-legalize-compounding-for-wellness-peptides/
  - (wellness) [Virginia Department of Corrections (.gov)] 08/17/2026, 04:03 PM, +0000 UTC — VADOC Celebrates Employee Health & Wellness Week
    
    Link: https://vadoc.virginia.gov/news-press-releases/2026/vadoc-celebrates-employee-health-wellness-week/
  - (wellness) [UNM Newsroom] 08/18/2026, 10:12 PM, +0000 UTC — COEHS wellness services strengthen communities, prepare future professionals
    
    Link: https://news.unm.edu/news/coehs-wellness-services-strengthen-communities-prepare-future-professionals
  - (wellness) [Marquette Today] 08/20/2026, 03:06 PM, +0000 UTC — Review your benefits with the Total Rewards Guide and Benefits and Wellness website
    
    Link: https://today.marquette.edu/2026/08/review-your-benefits-with-the-total-rewards-guide-and-benefits-and-wellness-website/
  - (wellness) [UR Now] 08/18/2026, 08:29 PM, +0000 UTC — University of Richmond alum’s wellness app provides a check-in for athletes
    
    Link: https://urnow.richmond.edu/features/article/-/28505/university-of-richmond-alum-s-wellness-app-provides-a-check-in-for-athletes.html?utm_source=news&utm_medium=referral&utm_campaign=features-story
  - (wellness) [MLB.com] 08/19/2026, 07:41 PM, +0000 UTC — MLB Together teaches mental wellness at RBI World Series
    
    Link: https://www.mlb.com/news/rbi-world-series-mlb-together-mental-wellness-event-2026
  - (wellness) [PR Newswire] 08/14/2026, 03:00 PM, +0000 UTC — FERRERO GROUP TO ACQUIRE PURELY ELIZABETH, A LEADING U.S. MODERN WELLNESS BRAND
    
    Link: https://www.prnewswire.com/news-releases/ferrero-group-to-acquire-purely-elizabeth-a-leading-us-modern-wellness-brand-302851234.html
  - (wellness) [BYU Life Sciences] 08/18/2026, 02:00 PM, +0000 UTC — The Arroyo Lab: Bridging Metabolic Research and Maternal Wellness
    
    Link: https://lifesciences.byu.edu/the-arroyo-lab-bridging-metabolic-research-and-maternal-wellness
  - (wellness) [The Santa Barbara Independent] 08/19/2026, 08:10 PM, +0000 UTC — County Behavioral Wellness Accepting Annual Applications for John Kovacs Scholarship Awards
    
    Link: https://www.independent.com/2026/08/19/county-behavioral-wellness-accepting-annual-applications-for-john-kovacs-scholarship-awards-3/
  - (wellness) [KARK] 08/19/2026, 08:00 PM, +0000 UTC — National wellness month
    
    Link: https://www.kark.com/arkansas-style/national-wellness-month/
  - (medical study) [University of Nebraska Medical Center] 08/18/2026, 07:31 PM, +0000 UTC — Medical research highlights, summer 2026
    
    Link: https://www.unmc.edu/newsroom/2026/08/18/medical-research-highlights-summer-2026/
  - (medical study) [Harvard Medical School] 08/17/2026, 04:05 PM, +0000 UTC — Pilots, Flight Attendants Have Greater Risk of Radiation-Related Cancer Death Than Other Professions
    
    Link: https://hms.harvard.edu/news/pilots-flight-attendants-have-greater-risk-radiation-related-cancer-death-other-professions
  - (medical study) [NPR] 08/19/2026, 03:22 PM, +0000 UTC — A real-world study of Oregon's nonmedical psilocybin program shows promise
    
    Link: https://www.npr.org/2026/08/19/nx-s1-5936443/oregon-psilocybin-ptsd-depression-anxiety
  - (medical study) [Michigan Medicine] 08/19/2026, 12:00 PM, +0000 UTC — College of Pharmacy alum advances U-M Medical School addiction research
    
    Link: https://www.michiganmedicine.org/philanthropy-news/college-pharmacy-alum-advances-u-m-medical-school-addiction-research
  - (medical study) [Stanford Medicine] 08/19/2026, 09:51 PM, +0000 UTC — ‘Molecular glue’ turns a cancer driver into a built-in kill switch in Stanford Medicine study
    
    Link: https://med.stanford.edu/news/all-news/2026/08/lymphoma-BCL6-kill-switch.html
  - (medical study) [American Cancer Society Press Room] 08/18/2026, 02:02 PM, +0000 UTC — County-Level Medical Debt Linked to Advanced-Stage Cancers and Worse Survival Among Newly Diagnosed U.S. Adults
    
    Link: https://pressroom.cancer.org/medical-debt-linked-to-worse-survival
  - (medical study) [RAPS] 08/18/2026, 12:00 PM, +0000 UTC — Study highlights limits of premarket evaluation for identifying recalls of high-risk medical devices
    
    Link: https://www.raps.org/resource/study-highlights-limits-of-premarket-evaluation-for-identifying-recalls-of-high-risk-medical-devices.html
  - (medical study) [WSJ] 08/19/2026, 09:30 AM, +0000 UTC — Exclusive | Startup to Link ‘Biobanks’ of Patient Tissue to Supercharge AI Medical Research
    
    Link: https://www.wsj.com/pro/venture-capital/startup-to-link-biobanks-of-patient-tissue-to-supercharge-ai-medical-research-55403925
  - (medical study) [Nature] 08/19/2026, 10:08 AM, +0000 UTC — Genomic meta-analyses of binge-eating behavior and anorexia nervosa yield insights into the unique and shared biology of eating disorder phenotypes
    
    Link: https://www.nature.com/articles/s44220-026-00698-2
  - (medical study) [University of South Florida] 08/19/2026, 02:35 PM, +0000 UTC — USF Health research reveals new clues about how space travel may affect women’s health
    
    Link: https://www.usf.edu/health/news/2026/usf-health-research-reveals-new-clues-about-how-space-travel-may-affect-womens-health.aspx
  - (medical study) [WashU Medicine] 08/17/2026, 08:03 PM, +0000 UTC — Laser therapy offers weapon against deadly brain tumors
    
    Link: https://medicine.washu.edu/news/laser-therapy-offers-weapon-against-deadly-brain-tumors/
  - (medical study) [Spectrum News] 08/14/2026, 12:30 PM, +0000 UTC — Legislative committee studying use of AI in healthcare
    
    Link: https://spectrumnews1.com/wi/milwaukee/news/2026/08/13/artificial-intelligence-healthcare-legislature
  - (clinical trial health) [KFF Health News] 08/19/2026, 09:02 AM, +0000 UTC — You Want To Join a Clinical Trial. Here’s What To Know About the Hurdles.
    
    Link: https://kffhealthnews.org/health-industry/clinical-trials-patients-hhs-easier-advice-on-how-to-enroll-seriously-ill-cancer/
  - (clinical trial health) [Mass General Brigham] 08/18/2026, 07:00 AM, +0000 UTC — Mass General Brigham Launches Clinical Trials Focused on Home Hospital Treatment for Dementia and Behavioral Health Conditions
    
    Link: https://www.massgeneralbrigham.org/en/newsroom/clinical-trials-of-home-hospital-treatment-for-dementia
  - (clinical trial health) [HCI Innovation Group] 08/14/2026, 08:56 AM, +0000 UTC — Ochsner, Paradigm Health Partner to Expand Clinical Trial Access
    
    Link: https://www.hcinnovationgroup.com/clinical-it/learning-health-systems-research/news/55397838/ochsner-paradigm-health-partner-to-expand-clinical-trial-access
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
  - (clinical trial health) [American Hospital Association] 08/15/2026, 07:53 PM, +0000 UTC — West Virginia University Health System's clinical trial offers hope for a rare and deadly blood cancer
    
    Link: https://www.aha.org/tellingthehospitalstory/stories/university-west-virginia-clinical-trial-offers-hope-rare-and-deadly-blood-cancer
  - (clinical trial health) [Oncodaily] 08/17/2026, 05:07 PM, +0000 UTC — Accelerating Clinical Trial Approvals Across Africa – Global Health Otherwise
    
    Link: https://oncodaily.com/new-paper-alert/global-health-otherwise-568437
  - (clinical trial health) [Vanderbilt Health News] 08/18/2026, 03:00 PM, +0000 UTC — Could GLP-1s help treat opioid use disorder? Vanderbilt Health study now enrolling
    
    Link: https://news.vumc.org/2026/08/18/could-glp-1s-help-treat-opioid-use-disorder-vanderbilt-health-study-now-enrolling/
  - (clinical trial health) [Spectrum News] 08/19/2026, 03:52 PM, +0000 UTC — Personalized cancer vaccine shows promise in late-stage clinical trial
    
    Link: https://spectrumlocalnews.com/us/snplus/health-and-medicine/2026/08/19/intismeran-personalized-cancer-vaccine-mrna-melanoma
  - (FDA recall health) [fda.gov] 08/14/2026, 11:07 PM, +0000 UTC — The Hampton Grocers, Inc . Recalls It’s 8 Ounce Packages of “Lacnola Lactation Granola” Because of Possible Health Risk
    
    Link: https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts/hampton-grocers-inc-recalls-its-8-ounce-packages-lacnola-lactation-granola-because-possible-health
  - (FDA recall health) [The New York Times] 08/14/2026, 11:12 PM, +0000 UTC — F.D.A. Classifies Egg Recall as Class I, for Highest Health Risk
    
    Link: https://www.nytimes.com/2026/08/14/health/fda-egg-recall-salmonella.html
  - (FDA recall health) [CBS News] 08/14/2026, 07:57 PM, +0000 UTC — FDA upgrades egg recall linked to salmonella to highest health risk level
    
    Link: https://www.cbsnews.com/news/fda-class-1-egg-recall-salmonella/
  - (FDA recall health) [CIDRAP] 08/17/2026, 08:27 PM, +0000 UTC — FDA heightens egg recall to reflect potential ‘serious adverse health consequences or death’
    
    Link: https://www.cidrap.umn.edu/foodborne-disease/fda-heightens-egg-recall-reflect-potential-serious-adverse-health-consequences-or
  - (FDA recall health) [Time Magazine] 08/15/2026, 03:47 PM, +0000 UTC — Salmonella Egg Recall Is Now Class I, the FDA’s Highest Risk Level
    
    Link: https://time.com/article/2026/08/15/eggs-recalled-for-salmonella-upgraded-to-highest-fda-risk-level/
  - (FDA recall health) [El Paso Times] 08/15/2026, 02:51 PM, +0000 UTC — FDA upgrades egg recall to Class I. What it means
    
    Link: https://www.elpasotimes.com/story/news/health/2026/08/15/egg-recall-upgraded-by-fda-to-class-i-what-that-means/91317478007/
  - (FDA recall health) [The Hill] 08/14/2026, 02:54 PM, +0000 UTC — FDA assigns highest-risk Class I status for recall of nearly 1.6 million cartons of eggs
    
    Link: https://thehill.com/policy/healthcare/6029894-fda-assigns-highest-risk-class-i-status-for-recall-of-nearly-1-6-million-cartons-of-eggs/
  - (FDA recall health) [Denver7] 08/18/2026, 12:25 AM, +0000 UTC — FDA upgrades egg recall to highest health-risk level amid string of food safety concerns
    
    Link: https://www.denver7.com/news/local-news/fda-upgrades-egg-recall-to-highest-health-risk-level-amid-string-of-food-safety-concerns
  - (FDA recall health) [11Alive.com] 08/20/2026, 02:42 PM, +0000 UTC — Blueberry recall in 8 states upgraded to FDA's highest health risk level
    
    Link: https://www.11alive.com/article/news/nation-world/blueberry-recall-in-8-states-upgraded-to-most-dangerous-classification/507-13ecdd2b-9e5a-427c-b889-b6d394d180c4
  - (FDA recall health) [Ophthalmology Times Europe] 08/20/2026, 11:01 AM, +0000 UTC — FDA recalls eye drop that relieves ocular itch for potential contamination
    
    Link: https://www.ophthalmologytimes.com/view/fda-recall-eye-drop-that-relieves-ocular-itch-potential-contamination
  - (FDA recall health) [The Guardian] 08/15/2026, 09:25 PM, +0000 UTC — Massive egg recall in US south and south-west due to salmonella outbreak
    
    Link: https://www.theguardian.com/us-news/2026/aug/15/egg-recall-us-south-and-south-west-salmonella-outbreak
  - (FDA recall health) [dw.com] 08/15/2026, 03:55 AM, +0000 UTC — US: 19 million eggs recalled over salmonella risk
    
    Link: https://www.dw.com/en/us-food-and-drug-administration-fda-recalls-19-million-eggs-over-salmonella-risk/a-78378361