# LIVE SIGNAL DATA — SerpAPI Pre-Fetch
The following signals were fetched from SerpAPI Google News and SerpAPI Google Trends immediately before this pipeline run. Treat Google Trends as AVAILABLE when this section contains a Google Trends block. Use it as the primary search_velocity input for Skills 01–05 (Signal Listener through Trend Strength Scorer). Use the Google News Radar as the broad discovery layer for news-led health topics, including topics that do not yet appear in Google Trends. Prioritize topics with convergence across News, Trends, primary/institutional sources, and credible publisher coverage.

## Google Trends — Trending Now (US / Health, real-time)
Terms with a "Why:" line have a confirmed real-world news story driving the spike; terms without one are a real-time signal only, not yet grounded in a specific story.
  - qc p
    Why: "Quality Control Cofounder Pierre 'P' Thomas Hospitalized After Heart Attack" — TMZ
  - clear eyes eye drops recall
    Why: "Popular eye drops recalled nationwide due to potential contamination" — WTNH.com
  - alfalfa sprouts food poisoning outbreak
    Why: "E coli and salmonella outbreak linked to alfalfa sprouts sickens dozens across multiple states" — Fox Business
  - cyclospora
    Why: "Confirmed cyclospora cases approach 16,000. See where people are sick" — USA Today

## Google Trends — 7-Day Interest (US)
  - **health**: latest=38, peak=100, 7d-delta=-9
    Rising related: hayden panettiere mental health, did hayden panettiere have health issues, hayden panettiere health problems, mitch mcconnell health, medvi health, sprinter health careers, neko health, mental health
  - **wellness**: latest=49, peak=100, 7d-delta=-7
    Rising related: circle wellness seattle, civana wellness resort and spa, routine wellness shampoo and conditioner reviews, health definition, mct wellness reviews, wellness center, health and wellness, wellness spa
  - **nutrition**: latest=73, peak=100, 7d-delta=-21
    Rising related: curtain up, generation channel, blue moon channel, curtain up channel, sundance kid, sundance channel, action channel, blue moon kid
  - **fitness**: latest=85, peak=100, 7d-delta=-1
    Rising related: eric falstrault fitness transformation, muscle definition over 50 fitness, casio f-b100w fitness tracker, million dollar things .com, fintechzoom.io, planet fitness customer service phone number, how to cancel planet fitness membership online, planet fitness customer service number
  - **food safety**: latest=22, peak=100, 7d-delta=-12
    Rising related: no food or drink sign, blueberry recall, ai apps students safety, when using the fifo method correctly the food stored in the front should be the food that, food should be stored at least which distance from the floor, rfk jr, which food safety practice will help prevent biological hazards, which activity is an example of poor personal hygiene
  - **diet**: latest=83, peak=100, 7d-delta=-12
    Rising related: vegan diet and inflammation, physicians committee vegan diet study, builtwithscience filling diet, stone age inspired diet crossword, ayds diet, healthy diet plan for beginners, home bodyweight exercises workout, miranda kerr diet
  - **weight loss**: latest=76, peak=100, 7d-delta=+2
    Rising related: billy gardell weight loss transformation, tofa weight loss study berkeley, gabe newell weight loss, bronson reed weight loss, best glp 1 supplement for weight loss, what is medvi, medvi quad, quad for ed
  - **mental health**: latest=35, peak=100, 7d-delta=-15
    Rising related: hayden panettiere mental health, hayden panettiere mental health issues, mychal threets mental health, physical health definition, what is mental health, mental health services, mental health treatment, mental health center
  - **gut health**: latest=58, peak=100, 7d-delta=+5
    Rising related: bristol stool chart usage, research on family estrangement, dr. andrew t. chan soda study, mitch mcconnell health, is farting a sign of good gut health, dreyer's outshine fruit bars recall, juicing recipes for gut health, best time to eat sauerkraut for gut health

Top rising related queries from Google Trends:
  - hayden panettiere mental health
  - did hayden panettiere have health issues
  - hayden panettiere health problems
  - mitch mcconnell health
  - medvi health
  - sprinter health careers
  - neko health
  - mental health
  - circle wellness seattle
  - civana wellness resort and spa
  - routine wellness shampoo and conditioner reviews
  - health definition
  - mct wellness reviews
  - wellness center
  - health and wellness
  - wellness spa
  - curtain up
  - generation channel
  - blue moon channel
  - curtain up channel

## Google News Radar — Recent Health Topics (144 unique across 12 queries; showing 60)
Treat these headlines as the broad radar of news-led health topics. The Signal Listener must consider this radar before narrowing to retained candidates.
  - (health) [HHS.gov] 08/17/2026, 07:06 PM, +0000 UTC — HHS Awards Over $96 Million to Strengthen Mental Health, Suicide Prevention, and Substance Use Disorder Services
    
    Link: https://www.hhs.gov/press-room/hhs-awards-96-million-mental-health-suicide-prevention-substance-use-services.html
  - (health) [aphis.usda.gov] 08/22/2026, 06:37 AM, +0000 UTC — Confirmed Detections of New World Screwworm | Animal and Plant Health Inspection Service
    
    Link: https://www.aphis.usda.gov/animals/animal-health/livestock-and-poultry-disease/stop-screwworm/current-status/confirmed
  - (health) [Nature] 08/20/2026, 10:21 AM, +0000 UTC — The hallmarks of skeletal muscle health
    
    Link: https://www.nature.com/articles/s42255-026-01595-9
  - (health) [Centers for Disease Control and Prevention | CDC (.gov)] 08/19/2026, 07:00 AM, +0000 UTC — Information for Travelers Returning from Ebola-Affected Areas
    
    Link: https://www.cdc.gov/ebola/situation-summary/returning-travelers.html
  - (health) [International Brotherhood of Teamsters] 08/20/2026, 03:41 PM, +0000 UTC — 10,000 Corewell Health East Nurses Ratify First Teamsters Contract
    
    Link: https://teamster.org/2026/08/10000-corewell-health-east-nurses-ratify-first-teamsters-contract/
  - (health) [Axios] 08/16/2026, 10:00 AM, +0000 UTC — How AI could bring Mayo-quality health care to everyone
    
    Link: https://www.axios.com/2026/08/16/ai-mayo-clinic-health-care-fix-jim-vandehei
  - (health) [The New York Times] 08/19/2026, 10:44 PM, +0000 UTC — Senate Health Panel Chairman Voices Strong Reservations About F.D.A. Nominee
    
    Link: https://www.nytimes.com/2026/08/19/us/politics/heidi-overton-cassidy-fda.html
  - (health) [New Jersey Monitor] 08/19/2026, 08:59 PM, +0000 UTC — NJ panel deadlocks on vote to raise health premiums for teachers
    
    Link: https://newjerseymonitor.com/2026/08/19/nj-panel-deadlocks-on-vote-to-raise-health-premiums-for-teachers/
  - (health) [University of Arizona News] 08/19/2026, 02:56 AM, +0000 UTC — U of A and Gila River Health Care (an entity of the Gila River Indian Community) launch nation's first MD-granting medical school branch within a Tribal Nation
    
    Link: https://news.arizona.edu/news/u-and-gila-river-health-care-entity-gila-river-indian-community-launch-nations-first-md
  - (health) [VTDigger] 08/17/2026, 03:18 PM, +0000 UTC — Dartmouth Health says it needs to close telehealth services for emergency and intensive care
    
    Link: https://vtdigger.org/2026/08/17/dartmouth-health-says-it-needs-to-close-telehealth-services-for-emergency-and-intensive-care/
  - (health) [University of California, Riverside] 08/18/2026, 05:50 PM, +0000 UTC — The hidden health cost of dollar store groceries
    
    Link: https://news.ucr.edu/articles/2026/08/18/hidden-health-cost-dollar-store-groceries
  - (health) [CNBC] 08/16/2026, 07:58 PM, +0000 UTC — Top U.S. commander acknowledges mental health issues on USS Lincoln
    
    Link: https://www.cnbc.com/2026/08/16/top-us-commander-acknowledges-mental-health-issues-on-uss-lincoln.html
  - (wellness) [GQ] 08/17/2026, 05:13 PM, +0000 UTC — The Latest Dating Dilemma: Wellness Gap Relationships
    
    Link: https://www.gq.com/story/dating-wellness-gap-relationships
  - (wellness) [FOX 13 Tampa Bay] 08/21/2026, 03:26 AM, +0000 UTC — Wellness retreat project
    
    Link: https://www.fox13news.com/news/oxford-exchange-owners-plan-550-acre-wellness-retreat-near-dade-city
  - (wellness) [Marquette Today] 08/20/2026, 04:40 PM, +0000 UTC — Review your benefits with the Total Rewards Guide and Benefits and Wellness website
    
    Link: https://today.marquette.edu/2026/08/review-your-benefits-with-the-total-rewards-guide-and-benefits-and-wellness-website/
  - (wellness) [Harvard T.H. Chan School of Public Health] 08/21/2026, 05:28 PM, +0000 UTC — What Happens When the Screen Goes Off? Lessons on Digital Wellness from Mississippi
    
    Link: https://hsph.harvard.edu/field-education-and-practice/news/what-happens-when-the-screen-goes-off-lessons-on-digital-wellness-from-mississippi/
  - (wellness) [University of Evansville Athletics] 08/22/2026, 01:49 AM, +0000 UTC — Ali Adams promoted to Assistant AD for Student-Athlete Health & Wellness
    
    Link: https://gopurpleaces.com/news/2026/8/21/general-releases-ali-adams-promoted-to-assistant-ad-for-student-athlete-health-wellness.aspx
  - (wellness) [Condé Nast Traveler] 08/18/2026, 08:43 PM, +0000 UTC — Is Traveling for Stargazing the Next Big Wellness Craze? These Hotels Are Betting on It
    
    Link: https://www.cntraveler.com/story/is-traveling-for-stargazing-the-next-big-wellness-craze-these-hotels-are-betting-on-it
  - (wellness) [Philadelphia Federal Reserve Bank] 08/21/2026, 06:27 PM, +0000 UTC — Financial Wellness for Older Adults: Understanding the Challenges of an Aging Population
    
    Link: https://www.philadelphiafed.org/calendar-of-events/financial-wellness-for-older-adults-understanding-the-challenges-of-an-aging-population
  - (wellness) [Purdue University College of Veterinary Medicine] 08/21/2026, 03:54 PM, +0000 UTC — “Paws Up” for Lanora Lannan – brought to you by the PVM Wellness Committee
    
    Link: https://vet.purdue.edu/news/paws-up-for-lanora-lannan-brought-to-you-by-the-pvm-wellness-committee.php
  - (wellness) [WFAA] 08/20/2026, 06:39 PM, +0000 UTC — 'Maxxing': When wellness trends push too far
    
    Link: https://www.wfaa.com/article/news/nation-world/maxxing-when-wellness-trends-push-too-far-social-media/507-66db9ae3-36a1-4437-92d3-f9f3c898156b
  - (wellness) [The Santa Barbara Independent] 08/19/2026, 08:10 PM, +0000 UTC — County Behavioral Wellness Accepting Annual Applications for John Kovacs Scholarship Awards
    
    Link: https://www.independent.com/2026/08/19/county-behavioral-wellness-accepting-annual-applications-for-john-kovacs-scholarship-awards-3/
  - (wellness) [AASA, The School Superintendents Association] 08/21/2026, 02:31 PM, +0000 UTC — When Leadership Leads to Wellness: School Health Index (SHI) as a Strategic Tool for Superintendent Decision Making
    
    Link: https://www.aasa.org/resources/resource/when-leadership-leads-to-wellness-school-health-index-(shi)-as-a-strategic-tool-for-superintendent-decision-making
  - (wellness) [KARK] 08/19/2026, 08:00 PM, +0000 UTC — National wellness month
    
    Link: https://www.kark.com/arkansas-style/national-wellness-month/
  - (medical study) [Harvard Medical School] 08/17/2026, 04:05 PM, +0000 UTC — Pilots, Flight Attendants Have Greater Risk of Radiation-Related Cancer Death Than Other Professions
    
    Link: https://hms.harvard.edu/news/pilots-flight-attendants-have-greater-risk-radiation-related-cancer-death-other-professions
  - (medical study) [NPR] 08/19/2026, 03:22 PM, +0000 UTC — A real-world study of Oregon's nonmedical psilocybin program shows promise
    
    Link: https://www.npr.org/2026/08/19/nx-s1-5936443/oregon-psilocybin-ptsd-depression-anxiety
  - (medical study) [Johns Hopkins Medicine] 08/19/2026, 03:53 PM, +0000 UTC — Bacteria Found in Lung Tumors May Boost Immune Response to Cancer
    
    Link: https://www.hopkinsmedicine.org/news/newsroom/news-releases/2026/08/bacteria-found-in-lung-tumors-may-boost-immune-response-to-cancer
  - (medical study) [Stanford Medicine] 08/19/2026, 09:51 PM, +0000 UTC — ‘Molecular glue’ turns a cancer driver into a built-in kill switch in Stanford Medicine study
    
    Link: https://med.stanford.edu/news/all-news/2026/08/lymphoma-BCL6-kill-switch.html
  - (medical study) [Nature] 08/19/2026, 10:17 AM, +0000 UTC — Large-scale AI-guided liver malignancy diagnosis: multicenter study and a single-arm trial
    
    Link: https://www.nature.com/articles/s41591-026-04589-y
  - (medical study) [WSJ] 08/19/2026, 09:30 AM, +0000 UTC — Exclusive | Startup to Link ‘Biobanks’ of Patient Tissue to Supercharge AI Medical Research
    
    Link: https://www.wsj.com/pro/venture-capital/startup-to-link-biobanks-of-patient-tissue-to-supercharge-ai-medical-research-55403925
  - (medical study) [University of South Florida] 08/19/2026, 02:35 PM, +0000 UTC — USF Health research reveals new clues about how space travel may affect women’s health
    
    Link: https://www.usf.edu/health/news/2026/usf-health-research-reveals-new-clues-about-how-space-travel-may-affect-womens-health.aspx
  - (medical study) [WashU Medicine] 08/17/2026, 08:03 PM, +0000 UTC — Laser therapy offers weapon against deadly brain tumors
    
    Link: https://medicine.washu.edu/news/laser-therapy-offers-weapon-against-deadly-brain-tumors/
  - (medical study) [MassDevice] 08/20/2026, 08:07 PM, +0000 UTC — Monteris Medical study shows critical survival factors for brain tumor patients
    
    Link: https://www.massdevice.com/monteris-medical-nueroblate-brain-tumor-study/
  - (medical study) [Independent Institute] 08/21/2026, 12:36 AM, +0000 UTC — Artificial Intelligence Collides with FDA Bureaucracy: News Article
    
    Link: https://www.independent.org/article/2026/08/20/artificial-intelligence-fda/
  - (medical study) [Medical Xpress] 08/19/2026, 01:00 PM, +0000 UTC — Weight-loss drug users turn to social media over doctors for advice, study finds
    
    Link: https://medicalxpress.com/news/2026-08-weight-loss-drug-users-social.html
  - (medical study) [KSWO 7News] 08/20/2026, 12:50 AM, +0000 UTC — State legislators to hold study examining medical marijuana in October
    
    Link: https://www.kswo.com/2026/08/20/state-legislators-hold-study-examining-medical-marijuana-october/
  - (clinical trial health) [KFF Health News] 08/19/2026, 09:02 AM, +0000 UTC — You Want To Join a Clinical Trial. Here’s What To Know About the Hurdles.
    
    Link: https://kffhealthnews.org/health-industry/clinical-trials-patients-hhs-easier-advice-on-how-to-enroll-seriously-ill-cancer/
  - (clinical trial health) [The American Journal of Managed Care] 08/21/2026, 08:17 PM, +0000 UTC — Ochsner Health, Paradigm Health Partnership Expands Clinical Trial Access Across the Gulf South
    
    Link: https://www.ajmc.com/view/ochsner-health-paradigm-health-partnership-expands-clinical-trial-access-across-the-gulf-south
  - (clinical trial health) [Mass General Brigham] 08/18/2026, 07:00 AM, +0000 UTC — Mass General Brigham Launches Clinical Trials Focused on Home Hospital Treatment for Dementia and Behavioral Health Conditions
    
    Link: https://www.massgeneralbrigham.org/en/newsroom/clinical-trials-of-home-hospital-treatment-for-dementia
  - (clinical trial health) [The Clinical Trial Vanguard] 08/19/2026, 07:32 AM, +0000 UTC — When Your CRO Gets Acquired Mid-Study, Your Site Feels It First
    
    Link: https://www.clinicaltrialvanguard.com/clinical-trial-ops-brief/when-your-cro-gets-acquired-mid-study-your-site-feels-it-first/
  - (clinical trial health) [Applied Clinical Trials Online] 08/20/2026, 04:05 PM, +0000 UTC — Curavit Acquires Lindus Health Clinical Research Organization Assets to Expand US and European Trial Operations
    
    Link: https://www.appliedclinicaltrialsonline.com/view/curavit-acquires-lindus-health-clinical-research-organization-assets-expand-us-european-trial-operations
  - (clinical trial health) [The New York Times] 08/18/2026, 07:00 AM, +0000 UTC — A Hopeless Diagnosis? Not for This Patient.
    
    Link: https://www.nytimes.com/2026/08/17/science/clinical-trial-jansens-disease-nizar-nih.html
  - (clinical trial health) [PR Newswire] 08/18/2026, 10:19 PM, +0000 UTC — Curavit Expands Clinical Research Capabilities with Acquisition of Lindus Health CRO Assets, Accelerating Global Trial Execution for Life Science Sponsors
    
    Link: https://www.prnewswire.com/news-releases/curavit-expands-clinical-research-capabilities-with-acquisition-of-lindus-health-cro-assets-accelerating-global-trial-execution-for-life-science-sponsors-302854586.html
  - (clinical trial health) [South Carolina Daily Gazette] 08/19/2026, 04:18 PM, +0000 UTC — State-funded testing of COVID-19 treatment approved to start 3,000-person clinical trial
    
    Link: https://scdailygazette.com/2026/08/19/state-funded-testing-of-covid-19-treatment-approved-to-start-3000-person-clinical-trial/
  - (clinical trial health) [Clinical Trials Arena] 08/20/2026, 11:01 AM, +0000 UTC — Reforms to UK clinical trial sector showing signs of success
    
    Link: https://www.clinicaltrialsarena.com/news/reforms-to-uk-clinical-trial-sector-showing-signs-of-success/
  - (clinical trial health) [American Hospital Association] 08/15/2026, 07:53 PM, +0000 UTC — West Virginia University Health System's clinical trial offers hope for a rare and deadly blood cancer
    
    Link: https://www.aha.org/tellingthehospitalstory/stories/university-west-virginia-clinical-trial-offers-hope-rare-and-deadly-blood-cancer
  - (clinical trial health) [Vanderbilt Health News] 08/18/2026, 03:00 PM, +0000 UTC — Could GLP-1s help treat opioid use disorder? Vanderbilt Health study now enrolling
    
    Link: https://news.vumc.org/2026/08/18/could-glp-1s-help-treat-opioid-use-disorder-vanderbilt-health-study-now-enrolling/
  - (clinical trial health) [MedTech Dive] 08/21/2026, 04:30 PM, +0000 UTC — How can wearables be used in clinical trials? FDA outlines best practices
    
    Link: https://www.medtechdive.com/news/how-can-wearables-be-used-in-clinical-trials-fda-outlines-best-practices/828512/
  - (FDA recall health) [CBS News] 08/19/2026, 10:52 PM, +0000 UTC — FDA upgrades recall of frozen blueberries sold at Publix to highest health risk level
    
    Link: https://www.cbsnews.com/news/blueberry-recall-fda-class-1-risk/
  - (FDA recall health) [The New York Times] 08/19/2026, 07:00 AM, +0000 UTC — F.D.A. Classifies Egg Recall as Class I, for Highest Health Risk
    
    Link: https://www.nytimes.com/2026/08/14/health/fda-egg-recall-salmonella.html
  - (FDA recall health) [CIDRAP] 08/17/2026, 08:27 PM, +0000 UTC — FDA heightens egg recall to reflect potential ‘serious adverse health consequences or death’
    
    Link: https://www.cidrap.umn.edu/foodborne-disease/fda-heightens-egg-recall-reflect-potential-serious-adverse-health-consequences-or
  - (FDA recall health) [El Paso Times] 08/15/2026, 02:51 PM, +0000 UTC — FDA upgrades egg recall to Class I. What it means
    
    Link: https://www.elpasotimes.com/story/news/health/2026/08/15/egg-recall-upgraded-by-fda-to-class-i-what-that-means/91317478007/
  - (FDA recall health) [Time Magazine] 08/15/2026, 03:47 PM, +0000 UTC — Salmonella Egg Recall Is Now Class I, the FDA’s Highest Risk Level
    
    Link: https://time.com/article/2026/08/15/eggs-recalled-for-salmonella-upgraded-to-highest-fda-risk-level/
  - (FDA recall health) [Denver7] 08/18/2026, 12:25 AM, +0000 UTC — FDA upgrades egg recall to highest health-risk level amid string of food safety concerns
    
    Link: https://www.denver7.com/news/local-news/fda-upgrades-egg-recall-to-highest-health-risk-level-amid-string-of-food-safety-concerns
  - (FDA recall health) [The Washington Post] 08/21/2026, 12:15 AM, +0000 UTC — FDA upgrades recall of frozen berries to highest-risk warning
    
    Link: https://www.washingtonpost.com/health/2026/08/20/fda-upgrades-recall-frozen-berries-highest-risk-warning/
  - (FDA recall health) [Centers for Disease Control and Prevention | CDC (.gov)] 08/20/2026, 07:00 AM, +0000 UTC — Cyclospora Outbreak Linked to Iceberg Lettuce | Cyclosporiasis
    
    Link: https://www.cdc.gov/cyclosporiasis/outbreaks/07-26/index.html
  - (FDA recall health) [Healthline] 08/20/2026, 06:18 PM, +0000 UTC — FDA Upgrades Publix Frozen Blueberry Recall to Highest Health Risk Level
    
    Link: https://www.healthline.com/health-news/fda-upgrades-publix-frozen-blueberry-recall-highest-risk-level
  - (FDA recall health) [Ophthalmology Times] 08/20/2026, 11:01 AM, +0000 UTC — FDA recalls eye drop that relieves ocular itch for potential contamination
    
    Link: https://www.ophthalmologytimes.com/view/fda-recall-eye-drop-that-relieves-ocular-itch-potential-contamination
  - (FDA recall health) [11Alive.com] 08/20/2026, 02:42 PM, +0000 UTC — Blueberry recall in 8 states upgraded to FDA's highest health risk level
    
    Link: https://www.11alive.com/article/news/nation-world/blueberry-recall-in-8-states-upgraded-to-most-dangerous-classification/507-13ecdd2b-9e5a-427c-b889-b6d394d180c4
  - (FDA recall health) [88.5 WFDD] 08/20/2026, 09:04 PM, +0000 UTC — FDA moves Publix frozen berry E. coli recall to Class I health risk
    
    Link: https://www.wfdd.org/health-safety/2026-08-20/fda-moves-publix-frozen-berry-e-coli-recall-to-class-i-health-risk