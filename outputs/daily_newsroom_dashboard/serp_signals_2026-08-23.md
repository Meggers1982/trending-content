# LIVE SIGNAL DATA — SerpAPI Pre-Fetch
The following signals were fetched from SerpAPI Google News and SerpAPI Google Trends immediately before this pipeline run. Treat Google Trends as AVAILABLE when this section contains a Google Trends block. Use it as the primary search_velocity input for Skills 01–05 (Signal Listener through Trend Strength Scorer). Use the Google News Radar as the broad discovery layer for news-led health topics, including topics that do not yet appear in Google Trends. Prioritize topics with convergence across News, Trends, primary/institutional sources, and credible publisher coverage.

## Google Trends — Trending Now (US / Health, real-time)
Terms with a "Why:" line have a confirmed real-world news story driving the spike; terms without one are a real-time signal only, not yet grounded in a specific story.
  - covid 19
    Why: "Is There a Summer COVID Surge? With Cases Rising in Nearly Every State, Watch for These Symptoms" — TODAY.com
  - brain-eating amoeba
    Why: "Ruston family asks for prayers after 8-year-old diagnosed with brain-eating amoeba" — WWLTV.com

## Google Trends — 7-Day Interest (US)
  - **health**: latest=42, peak=100, 7d-delta=-4
    Rising related: what are the latest health updates from dolly parton and details on her new museum, hayden panettiere mental health, did hayden panettiere have health issues, hayden panettiere health problems, chase stokes health issues, mitch mcconnell health, dolly parton health, medvi health
  - **wellness**: latest=46, peak=100, 7d-delta=-10
    Rising related: circle wellness seattle, civana wellness resort and spa, the wellness company emergency kit, the wellness company medical emergency kit, lerner health and wellness center, social health definition, health definition, definition of wellness
  - **nutrition**: latest=67, peak=100, 7d-delta=-11
    Rising related: cooked versus raw vegetables nutrition, curtain up, generation channel, sundance kid, curtain up channel, action channel, comeback kid, sundance
  - **fitness**: latest=78, peak=100, 7d-delta=-2
    Rising related: eric falstrault fitness transformation, muscle definition over 50 fitness, casio f-b100w fitness tracker, harley pasternak fitness advice, million dollar things .com, planet fitness customer service phone number, planet fitness customer service number, fintechzoom.io
  - **food safety**: latest=15, peak=100, 7d-delta=-9
    Rising related: why are there so many food recalls lately, project 2025 horses, ai apps students safety, which activity is an example of poor personal hygiene, project 2025, when using the fifo method correctly the food stored in the front should be the food that, project 2025 food supply, rfk jr
  - **diet**: latest=85, peak=100, 7d-delta=-15
    Rising related: vegan diet and inflammation, physicians committee vegan diet study, built with science filling diet, builtwithscience filling diet, healthy diet plan for beginners, home bodyweight exercises workout, how to start a youtube channel, best places to visit in casablanca
  - **weight loss**: latest=82, peak=100, 7d-delta=-4
    Rising related: billy gardell weight loss transformation, gabe newell weight loss, tofa weight loss study berkeley, bronson reed, bronson reed weight loss, runway ai video generator, what is medvi, medvi quad
  - **mental health**: latest=38, peak=100, 7d-delta=-8
    Rising related: hayden panettiere mental health, hayden panettiere mental health issues, did hayden panettiere have mental health issues, mychal threets mental health, what is sib in mental health, northern virginia mental health institute, in patient care mental health near me, maternal mental health hotline
  - **gut health**: latest=63, peak=100, 7d-delta=+10
    Rising related: research on family estrangement, mitch mcconnell health, cognition, bristol stool chart usage, years of trump support came undone in 15 minutes in an airport, is farting a sign of good gut health, seneca, good gut health

Top rising related queries from Google Trends:
  - what are the latest health updates from dolly parton and details on her new museum
  - hayden panettiere mental health
  - did hayden panettiere have health issues
  - hayden panettiere health problems
  - chase stokes health issues
  - mitch mcconnell health
  - dolly parton health
  - medvi health
  - circle wellness seattle
  - civana wellness resort and spa
  - the wellness company emergency kit
  - the wellness company medical emergency kit
  - lerner health and wellness center
  - social health definition
  - health definition
  - definition of wellness
  - cooked versus raw vegetables nutrition
  - curtain up
  - generation channel
  - sundance kid

## Google News Radar — Recent Health Topics (144 unique across 12 queries; showing 60)
Treat these headlines as the broad radar of news-led health topics. The Signal Listener must consider this radar before narrowing to retained candidates.
  - (health) [HHS.gov] 08/17/2026, 07:06 PM, +0000 UTC — HHS Awards Over $96 Million to Strengthen Mental Health, Suicide Prevention, and Substance Use Disorder Services
    
    Link: https://www.hhs.gov/press-room/hhs-awards-96-million-mental-health-suicide-prevention-substance-use-services.html
  - (health) [People.com] 08/22/2026, 01:55 AM, +0000 UTC — Dolly Parton Shares Health Update While Announcing Plans for Museum (Exclusive)
    
    Link: https://people.com/dolly-parton-shares-health-update-while-announcing-plans-for-museum-exclusive-12065750
  - (health) [aphis.usda.gov] 08/21/2026, 07:00 AM, +0000 UTC — Confirmed Detections of New World Screwworm | Animal and Plant Health Inspection Service
    
    Link: https://www.aphis.usda.gov/animals/animal-health/livestock-and-poultry-disease/stop-screwworm/current-status/confirmed
  - (health) [Centers for Disease Control and Prevention | CDC (.gov)] 08/19/2026, 07:00 AM, +0000 UTC — Information for Travelers Returning from Ebola-Affected Areas
    
    Link: https://www.cdc.gov/ebola/situation-summary/returning-travelers.html
  - (health) [KFF Health News] 08/18/2026, 07:00 AM, +0000 UTC — Tracking State Rural Health Transformation Plans
    
    Link: https://kffhealthnews.org/rural-health/tracking-state-rural-health-transformation-plans/
  - (health) [International Brotherhood of Teamsters] 08/20/2026, 03:41 PM, +0000 UTC — 10,000 Corewell Health East Nurses Ratify First Teamsters Contract
    
    Link: https://teamster.org/2026/08/10000-corewell-health-east-nurses-ratify-first-teamsters-contract/
  - (health) [Nature] 08/19/2026, 03:24 PM, +0000 UTC — Family genetic designs in MoBa provide insights into health and functioning
    
    Link: https://www.nature.com/articles/s41586-026-10926-5
  - (health) [Think Global Health] 08/20/2026, 07:00 AM, +0000 UTC — Tracking Measles and the World's Vaccine-Preventable Diseases
    
    Link: https://www.thinkglobalhealth.org/article/vaccine-preventable-disease-a-global-tracker
  - (health) [Atrium Health] 08/22/2026, 01:19 AM, +0000 UTC — In partnership with Morehouse School of Medicine Atrium Health commits more than 700 million
    
    Link: https://atriumhealth.org/about-us/newsroom/news/2026/08/in-partnership-with-morehouse-school-of-medicine-atrium-health-commits-more-than-700-million
  - (health) [University of Arizona News] 08/23/2026, 04:58 AM, +0000 UTC — U of A and Gila River Health Care (an entity of the Gila River Indian Community) launch nation's first MD-granting medical school branch within a Tribal Nation
    
    Link: https://news.arizona.edu/news/u-and-gila-river-health-care-entity-gila-river-indian-community-launch-nations-first-md
  - (health) [The New York Times] 08/19/2026, 10:44 PM, +0000 UTC — Senate Health Panel Chairman Voices Strong Reservations About F.D.A. Nominee
    
    Link: https://www.nytimes.com/2026/08/19/us/politics/heidi-overton-cassidy-fda.html
  - (health) [New Jersey Monitor] 08/19/2026, 08:59 PM, +0000 UTC — NJ panel deadlocks on vote to raise health premiums for teachers
    
    Link: https://newjerseymonitor.com/2026/08/19/nj-panel-deadlocks-on-vote-to-raise-health-premiums-for-teachers/
  - (wellness) [GQ] 08/17/2026, 05:13 PM, +0000 UTC — The Latest Dating Dilemma: Wellness Gap Relationships
    
    Link: https://www.gq.com/story/dating-wellness-gap-relationships
  - (wellness) [FOX 13 Tampa Bay] 08/21/2026, 03:26 AM, +0000 UTC — Wellness retreat project
    
    Link: https://www.fox13news.com/news/oxford-exchange-owners-plan-550-acre-wellness-retreat-near-dade-city
  - (wellness) [Marquette Today] 08/20/2026, 04:40 PM, +0000 UTC — Review your benefits with the Total Rewards Guide and Benefits and Wellness website
    
    Link: https://today.marquette.edu/2026/08/review-your-benefits-with-the-total-rewards-guide-and-benefits-and-wellness-website/
  - (wellness) [VA.gov Home | Veterans Affairs] 08/20/2026, 01:36 AM, +0000 UTC — Greenville VA HCC Celebrates Labyrinth Ribbon Cutting: A Pathway to Wellness
    
    Link: https://www.va.gov/durham-health-care/stories/greenville-va-hcc-celebrates-labyrinth-ribbon-cutting-a-pathway-to-wellness/
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
  - (wellness) [KARK] 08/19/2026, 08:00 PM, +0000 UTC — National wellness month
    
    Link: https://www.kark.com/arkansas-style/national-wellness-month/
  - (wellness) [Upper Michigan's Source] 08/20/2026, 12:40 PM, +0000 UTC — How you can promote wellness during National Wellness Month
    
    Link: https://www.uppermichiganssource.com/2026/08/20/how-you-can-promote-wellness-during-national-wellness-month/
  - (wellness) [University of Michigan] 08/21/2026, 12:11 PM, +0000 UTC — BME Graduate Student Council Strengthens Community through Academic, Wellness, and Social Programming
    
    Link: https://bme.umich.edu/2026/08/21/bme-graduate-student-council-strengthens-community-through-academic-wellness-and-social-programming-2/
  - (medical study) [Harvard Medical School] 08/17/2026, 04:05 PM, +0000 UTC — Pilots, Flight Attendants Have Greater Risk of Radiation-Related Cancer Death Than Other Professions
    
    Link: https://hms.harvard.edu/news/pilots-flight-attendants-have-greater-risk-radiation-related-cancer-death-other-professions
  - (medical study) [NPR] 08/19/2026, 03:22 PM, +0000 UTC — A real-world study of Oregon's nonmedical psilocybin program shows promise
    
    Link: https://www.npr.org/2026/08/19/nx-s1-5936443/oregon-psilocybin-ptsd-depression-anxiety
  - (medical study) [Google Research] 08/21/2026, 07:00 AM, +0000 UTC — Advancing AMIE towards expert-level audio-visual clinical consultations
    
    Link: https://research.google/blog/advancing-amie-towards-expert-level-audio-visual-clinical-consultations/
  - (medical study) [Johns Hopkins Medicine] 08/19/2026, 03:53 PM, +0000 UTC — Bacteria Found in Lung Tumors May Boost Immune Response to Cancer
    
    Link: https://www.hopkinsmedicine.org/news/newsroom/news-releases/2026/08/bacteria-found-in-lung-tumors-may-boost-immune-response-to-cancer
  - (medical study) [Michigan Medicine] 08/19/2026, 12:00 PM, +0000 UTC — College of Pharmacy alum advances U-M Medical School addiction research
    
    Link: https://www.michiganmedicine.org/philanthropy-news/college-pharmacy-alum-advances-u-m-medical-school-addiction-research
  - (medical study) [Stanford Medicine] 08/19/2026, 09:51 PM, +0000 UTC — ‘Molecular glue’ turns a cancer driver into a built-in kill switch in Stanford Medicine study
    
    Link: https://med.stanford.edu/news/all-news/2026/08/lymphoma-BCL6-kill-switch.html
  - (medical study) [Nature] 08/19/2026, 10:17 AM, +0000 UTC — Large-scale AI-guided liver malignancy diagnosis: multicenter study and a single-arm trial
    
    Link: https://www.nature.com/articles/s41591-026-04589-y
  - (medical study) [WSJ] 08/19/2026, 09:30 AM, +0000 UTC — Exclusive | Startup to Link ‘Biobanks’ of Patient Tissue to Supercharge AI Medical Research
    
    Link: https://www.wsj.com/pro/venture-capital/startup-to-link-biobanks-of-patient-tissue-to-supercharge-ai-medical-research-55403925
  - (medical study) [WashU Medicine] 08/17/2026, 08:03 PM, +0000 UTC — Laser therapy offers weapon against deadly brain tumors
    
    Link: https://medicine.washu.edu/news/laser-therapy-offers-weapon-against-deadly-brain-tumors/
  - (medical study) [UT Southwestern] 08/21/2026, 03:58 PM, +0000 UTC — Brain activity discovery could transform Parkinson’s treatment: Newsroom
    
    Link: https://www.utsouthwestern.edu/newsroom/articles/year-2026/aug-brain-activity-parkinsons-treatment.html
  - (medical study) [KSWO 7News] 08/20/2026, 12:50 AM, +0000 UTC — State legislators to hold study examining medical marijuana in October
    
    Link: https://www.kswo.com/2026/08/20/state-legislators-hold-study-examining-medical-marijuana-october/
  - (medical study) [STAT] 08/19/2026, 08:34 AM, +0000 UTC — AI has created a shadow medical system
    
    Link: https://www.statnews.com/2026/08/19/ai-doctor-outperforms-chatgpt-oura-quest-ro-hims-medical-system/
  - (clinical trial health) [KFF Health News] 08/19/2026, 09:02 AM, +0000 UTC — You Want To Join a Clinical Trial. Here’s What To Know About the Hurdles.
    
    Link: https://kffhealthnews.org/health-industry/clinical-trials-patients-hhs-easier-advice-on-how-to-enroll-seriously-ill-cancer/
  - (clinical trial health) [The American Journal of Managed Care] 08/21/2026, 08:17 PM, +0000 UTC — Ochsner Health, Paradigm Health Partnership Expands Clinical Trial Access Across the Gulf South
    
    Link: https://www.ajmc.com/view/ochsner-health-paradigm-health-partnership-expands-clinical-trial-access-across-the-gulf-south
  - (clinical trial health) [PR Newswire] 08/18/2026, 10:19 PM, +0000 UTC — Curavit Expands Clinical Research Capabilities with Acquisition of Lindus Health CRO Assets, Accelerating Global Trial Execution for Life Science Sponsors
    
    Link: https://www.prnewswire.com/news-releases/curavit-expands-clinical-research-capabilities-with-acquisition-of-lindus-health-cro-assets-accelerating-global-trial-execution-for-life-science-sponsors-302854586.html
  - (clinical trial health) [Applied Clinical Trials Online] 08/20/2026, 04:05 PM, +0000 UTC — Curavit Acquires Lindus Health Clinical Research Organization Assets to Expand US and European Trial Operations
    
    Link: https://www.appliedclinicaltrialsonline.com/view/curavit-acquires-lindus-health-clinical-research-organization-assets-expand-us-european-trial-operations
  - (clinical trial health) [The Clinical Trial Vanguard] 08/19/2026, 07:32 AM, +0000 UTC — When Your CRO Gets Acquired Mid-Study, Your Site Feels It First
    
    Link: https://www.clinicaltrialvanguard.com/clinical-trial-ops-brief/when-your-cro-gets-acquired-mid-study-your-site-feels-it-first/
  - (clinical trial health) [The New York Times] 08/18/2026, 07:00 AM, +0000 UTC — A Hopeless Diagnosis? Not for This Patient.
    
    Link: https://www.nytimes.com/2026/08/17/science/clinical-trial-jansens-disease-nizar-nih.html
  - (clinical trial health) [South Carolina Daily Gazette] 08/19/2026, 04:18 PM, +0000 UTC — State-funded testing of COVID-19 treatment approved to start 3,000-person clinical trial
    
    Link: https://scdailygazette.com/2026/08/19/state-funded-testing-of-covid-19-treatment-approved-to-start-3000-person-clinical-trial/
  - (clinical trial health) [Clinical Trials Arena] 08/20/2026, 11:01 AM, +0000 UTC — Reforms to UK clinical trial sector showing signs of success
    
    Link: https://www.clinicaltrialsarena.com/news/reforms-to-uk-clinical-trial-sector-showing-signs-of-success/
  - (clinical trial health) [Oncodaily] 08/17/2026, 05:07 PM, +0000 UTC — Accelerating Clinical Trial Approvals Across Africa – Global Health Otherwise
    
    Link: https://oncodaily.com/new-paper-alert/global-health-otherwise-568437
  - (clinical trial health) [News-Medical] 08/20/2026, 05:52 PM, +0000 UTC — Federal and industry sponsors play complementary roles in cancer clinical trials
    
    Link: https://www.news-medical.net/news/20260820/Federal-and-industry-sponsors-play-complementary-roles-in-cancer-clinical-trials.aspx
  - (clinical trial health) [Straits Research] 08/19/2026, 07:00 AM, +0000 UTC — Clinical Trials Market Size, Share, Growth, Analysis, Report, 2034
    
    Link: https://straitsresearch.com/report/clinical-trials-market
  - (clinical trial health) [MedTech Dive] 08/21/2026, 04:30 PM, +0000 UTC — How can wearables be used in clinical trials? FDA outlines best practices
    
    Link: https://www.medtechdive.com/news/how-can-wearables-be-used-in-clinical-trials-fda-outlines-best-practices/828512/
  - (FDA recall health) [The New York Times] 08/19/2026, 07:00 AM, +0000 UTC — F.D.A. Classifies Egg Recall as Class I, for Highest Health Risk
    
    Link: https://www.nytimes.com/2026/08/14/health/fda-egg-recall-salmonella.html
  - (FDA recall health) [CBS News] 08/19/2026, 10:52 PM, +0000 UTC — FDA upgrades recall of frozen blueberries sold at Publix to highest health risk level
    
    Link: https://www.cbsnews.com/news/blueberry-recall-fda-class-1-risk/
  - (FDA recall health) [CIDRAP] 08/17/2026, 08:27 PM, +0000 UTC — FDA heightens egg recall to reflect potential ‘serious adverse health consequences or death’
    
    Link: https://www.cidrap.umn.edu/foodborne-disease/fda-heightens-egg-recall-reflect-potential-serious-adverse-health-consequences-or
  - (FDA recall health) [Axios] 08/22/2026, 09:07 PM, +0000 UTC — Here's why the FDA hit frozen blueberries with its highest risk warning
    
    Link: https://www.axios.com/2026/08/22/frozen-blueberries-recall-fda-high-risk-warning
  - (FDA recall health) [Denver7] 08/18/2026, 12:25 AM, +0000 UTC — FDA upgrades egg recall to highest health-risk level amid string of food safety concerns
    
    Link: https://www.denver7.com/news/local-news/fda-upgrades-egg-recall-to-highest-health-risk-level-amid-string-of-food-safety-concerns
  - (FDA recall health) [The Washington Post] 08/21/2026, 12:15 AM, +0000 UTC — FDA upgrades recall of frozen berries to highest-risk warning
    
    Link: https://www.washingtonpost.com/health/2026/08/20/fda-upgrades-recall-frozen-berries-highest-risk-warning/
  - (FDA recall health) [Centers for Disease Control and Prevention | CDC (.gov)] 08/20/2026, 07:00 AM, +0000 UTC — Cyclospora Outbreak Linked to Iceberg Lettuce | Cyclosporiasis
    
    Link: https://www.cdc.gov/cyclosporiasis/outbreaks/07-26/index.html
  - (FDA recall health) [Healthline] 08/20/2026, 06:18 PM, +0000 UTC — FDA Upgrades Publix Frozen Blueberry Recall to Highest Health Risk Level
    
    Link: https://www.healthline.com/health-news/fda-upgrades-publix-frozen-blueberry-recall-highest-risk-level
  - (FDA recall health) [News On 6] 08/17/2026, 01:33 PM, +0000 UTC — Egg recall linked to salmonella upgraded to highest health risk level by FDA
    
    Link: https://www.newson6.com/tulsa-oklahoma-news/egg-recall-linked-to-salmonella-upgraded-to-highest-health-risk-level-by-fda
  - (FDA recall health) [Ophthalmology Times] 08/20/2026, 11:01 AM, +0000 UTC — FDA recalls eye drop that relieves ocular itch for potential contamination
    
    Link: https://www.ophthalmologytimes.com/view/fda-recall-eye-drop-that-relieves-ocular-itch-potential-contamination
  - (FDA recall health) [11Alive.com] 08/20/2026, 02:42 PM, +0000 UTC — Blueberry recall in 8 states upgraded to FDA's highest health risk level
    
    Link: https://www.11alive.com/article/news/nation-world/blueberry-recall-in-8-states-upgraded-to-most-dangerous-classification/507-13ecdd2b-9e5a-427c-b889-b6d394d180c4
  - (FDA recall health) [88.5 WFDD] 08/20/2026, 09:04 PM, +0000 UTC — FDA moves Publix frozen berry E. coli recall to Class I health risk
    
    Link: https://www.wfdd.org/health-safety/2026-08-20/fda-moves-publix-frozen-berry-e-coli-recall-to-class-i-health-risk