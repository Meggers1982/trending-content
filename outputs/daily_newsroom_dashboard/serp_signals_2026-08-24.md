# LIVE SIGNAL DATA — SerpAPI Pre-Fetch
The following signals were fetched from SerpAPI Google News and SerpAPI Google Trends immediately before this pipeline run. Treat Google Trends as AVAILABLE when this section contains a Google Trends block. Use it as the primary search_velocity input for Skills 01–05 (Signal Listener through Trend Strength Scorer). Use the Google News Radar as the broad discovery layer for news-led health topics, including topics that do not yet appear in Google Trends. Prioritize topics with convergence across News, Trends, primary/institutional sources, and credible publisher coverage.

## Google Trends — Trending Now (US / Health, real-time)
Terms with a "Why:" line have a confirmed real-world news story driving the spike; terms without one are a real-time signal only, not yet grounded in a specific story.
  - arch
    Why: "Arch Manning wears these Warby Parker glasses on and off the field" — USA Today
  - runny
    Why: "What is salmonella, how does it spread and are eggs safe to eat?" — The Guardian

## Google Trends — 7-Day Interest (US)
  - **health**: latest=73, peak=100, 7d-delta=-5
    Rising related: what are the latest health updates from dolly parton and details on her new museum, dolly parton health, medvi health, women s health clinic, mitch mcconnell health, dolly parton health update, king charles health, bioma health
  - **wellness**: latest=73, peak=100, 7d-delta=-9
    Rising related: ocean state community wellness, civana wellness resort and spa, lerner health and wellness center, und wellness center, the wellness company emergency kit, the wellness company medical emergency kit, health definition, social health definition
  - **nutrition**: latest=75, peak=100, 7d-delta=-4
    Rising related: curtain up, generation channel, curtain up channel, cooked versus raw vegetables nutrition, sundance kid, action kid, sundance, action channel
  - **fitness**: latest=73, peak=100, 7d-delta=-7
    Rising related: eric falstrault fitness transformation, muscle definition over 50 fitness, casio f-b100w fitness tracker, harley pasternak fitness advice, planet fitness customer service phone number, million dollar things .com, planet fitness customer service number, planet fitness customer service
  - **food safety**: latest=99, peak=100, 7d-delta=+78
    Rising related: project 2025 food supply, uc riverside dollar store study, permanent daylight saving time winter sunsets, why are there so many food recalls lately, chewy cat food, ai apps students safety, how preventable is abusive head trauma, project 2025 food safety
  - **diet**: latest=79, peak=100, 7d-delta=+0
    Rising related: vegan diet and inflammation, physicians committee vegan diet study, home bodyweight exercises workout, healthy diet plan for beginners, ai tools you should know in 2026, how to start a youtube channel, uefa champions league news, how to save money fast
  - **weight loss**: latest=65, peak=100, 7d-delta=-1
    Rising related: billy gardell weight loss transformation, gabe newell weight loss, tofa weight loss study berkeley, uc berkeley weight loss research, medvi quad reviews, medvi tirzepatide cost, medvi quad, quad ed
  - **mental health**: latest=52, peak=100, 7d-delta=-13
    Rising related: mychal threets mental health, how to improve mental health lwspeakcare, social health definition, inpatient mental health facilities near me, mental health treatment, mental health treatment center, physical health definition, what is mental health
  - **gut health**: latest=40, peak=100, 7d-delta=-60
    Rising related: dr. andrew t. chan soda study, dreyer's outshine fruit bars recall, research on family estrangement, years of trump support came undone in 15 minutes in an airport, best supplements for gut health and weight loss, bristol stool chart usage, is farting a sign of good gut health, seneca

Top rising related queries from Google Trends:
  - what are the latest health updates from dolly parton and details on her new museum
  - dolly parton health
  - medvi health
  - women s health clinic
  - mitch mcconnell health
  - dolly parton health update
  - king charles health
  - bioma health
  - ocean state community wellness
  - civana wellness resort and spa
  - lerner health and wellness center
  - und wellness center
  - the wellness company emergency kit
  - the wellness company medical emergency kit
  - health definition
  - social health definition
  - curtain up
  - generation channel
  - curtain up channel
  - cooked versus raw vegetables nutrition

## Google News Radar — Recent Health Topics (144 unique across 12 queries; showing 60)
Treat these headlines as the broad radar of news-led health topics. The Signal Listener must consider this radar before narrowing to retained candidates.
  - (health) [HHS.gov] 08/17/2026, 07:06 PM, +0000 UTC — HHS Awards Over $96 Million to Strengthen Mental Health, Suicide Prevention, and Substance Use Disorder Services
    
    Link: https://www.hhs.gov/press-room/hhs-awards-96-million-mental-health-suicide-prevention-substance-use-services.html
  - (health) [aphis.usda.gov] 08/21/2026, 07:00 AM, +0000 UTC — Confirmed Detections of New World Screwworm | Animal and Plant Health Inspection Service
    
    Link: https://www.aphis.usda.gov/animals/animal-health/livestock-and-poultry-disease/stop-screwworm/current-status/confirmed
  - (health) [Centers for Disease Control and Prevention | CDC (.gov)] 08/19/2026, 07:00 AM, +0000 UTC — Information for Travelers Returning from Ebola-Affected Areas
    
    Link: https://www.cdc.gov/ebola/situation-summary/returning-travelers.html
  - (health) [KFF Health News] 08/18/2026, 07:00 AM, +0000 UTC — Tracking State Rural Health Transformation Plans
    
    Link: https://kffhealthnews.org/rural-health/tracking-state-rural-health-transformation-plans/
  - (health) [University of California, Riverside] 08/18/2026, 05:50 PM, +0000 UTC — The hidden health cost of dollar store groceries
    
    Link: https://news.ucr.edu/articles/2026/08/18/hidden-health-cost-dollar-store-groceries
  - (health) [International Brotherhood of Teamsters] 08/20/2026, 03:41 PM, +0000 UTC — 10,000 Corewell Health East Nurses Ratify First Teamsters Contract
    
    Link: https://teamster.org/2026/08/10000-corewell-health-east-nurses-ratify-first-teamsters-contract/
  - (health) [Nature] 08/19/2026, 03:24 PM, +0000 UTC — Family genetic designs in MoBa provide insights into health and functioning
    
    Link: https://www.nature.com/articles/s41586-026-10926-5
  - (health) [Atrium Health] 08/22/2026, 01:19 AM, +0000 UTC — In partnership with Morehouse School of Medicine Atrium Health commits more than 700 million
    
    Link: https://atriumhealth.org/about-us/newsroom/news/2026/08/in-partnership-with-morehouse-school-of-medicine-atrium-health-commits-more-than-700-million
  - (health) [Think Global Health] 08/20/2026, 07:00 AM, +0000 UTC — Tracking Measles and the World's Vaccine-Preventable Diseases
    
    Link: https://www.thinkglobalhealth.org/article/vaccine-preventable-disease-a-global-tracker
  - (health) [University of Arizona News] 08/23/2026, 04:58 AM, +0000 UTC — U of A and Gila River Health Care (an entity of the Gila River Indian Community) launch nation's first MD-granting medical school branch within a Tribal Nation
    
    Link: https://news.arizona.edu/news/u-and-gila-river-health-care-entity-gila-river-indian-community-launch-nations-first-md
  - (health) [Axios] 08/20/2026, 09:01 PM, +0000 UTC — Employer health costs: Why it could be another tough year
    
    Link: https://www.axios.com/2026/08/20/health-care-costs-employers-rising
  - (health) [New Jersey Monitor] 08/19/2026, 08:59 PM, +0000 UTC — NJ panel deadlocks on vote to raise health premiums for teachers
    
    Link: https://newjerseymonitor.com/2026/08/19/nj-panel-deadlocks-on-vote-to-raise-health-premiums-for-teachers/
  - (wellness) [Yahoo Creators] 08/23/2026, 02:00 PM, +0000 UTC — Wellness stacking: why psychologists say it beats willpower for building healthy habits
    
    Link: https://creators.yahoo.com/lifestyle/story/wellness-stacking-why-psychologists-say-it-beats-willpower-for-building-healthy-habits-015140677.html
  - (wellness) [GQ] 08/17/2026, 05:13 PM, +0000 UTC — The Latest Dating Dilemma: Wellness Gap Relationships
    
    Link: https://www.gq.com/story/dating-wellness-gap-relationships
  - (wellness) [FOX 13 Tampa Bay] 08/21/2026, 03:26 AM, +0000 UTC — Wellness retreat project
    
    Link: https://www.fox13news.com/news/oxford-exchange-owners-plan-550-acre-wellness-retreat-near-dade-city
  - (wellness) [Marquette Today] 08/20/2026, 04:40 PM, +0000 UTC — Review your benefits with the Total Rewards Guide and Benefits and Wellness website
    
    Link: https://today.marquette.edu/2026/08/review-your-benefits-with-the-total-rewards-guide-and-benefits-and-wellness-website/
  - (wellness) [WFLA] 08/23/2026, 04:18 PM, +0000 UTC — 1 dead, officer hospitalized after attempted wellness check in St. Pete: PCSO
    
    Link: https://www.wfla.com/news/pinellas-county/1-dead-officer-hospitalized-after-attempted-wellness-check-in-st-pete-pcso/
  - (wellness) [VA.gov Home | Veterans Affairs] 08/20/2026, 01:36 AM, +0000 UTC — Greenville VA HCC Celebrates Labyrinth Ribbon Cutting: A Pathway to Wellness
    
    Link: https://www.va.gov/durham-health-care/stories/greenville-va-hcc-celebrates-labyrinth-ribbon-cutting-a-pathway-to-wellness/
  - (wellness) [Harvard T.H. Chan School of Public Health] 08/21/2026, 05:28 PM, +0000 UTC — What Happens When the Screen Goes Off? Lessons on Digital Wellness from Mississippi
    
    Link: https://hsph.harvard.edu/field-education-and-practice/news/what-happens-when-the-screen-goes-off-lessons-on-digital-wellness-from-mississippi/
  - (wellness) [Ground Truths | Eric Topol] 08/23/2026, 02:41 PM, +0000 UTC — Deborah Cohen: The Wellness-Industrial Complex
    
    Link: https://erictopol.substack.com/p/deborah-cohen-the-wellness-industrial
  - (wellness) [University of Evansville Athletics] 08/22/2026, 01:49 AM, +0000 UTC — Ali Adams promoted to Assistant AD for Student-Athlete Health & Wellness
    
    Link: https://gopurpleaces.com/news/2026/8/21/general-releases-ali-adams-promoted-to-assistant-ad-for-student-athlete-health-wellness.aspx
  - (wellness) [WBAL-TV] 08/21/2026, 09:38 PM, +0000 UTC — Waterfront Wellness combines scenic views with working out
    
    Link: https://www.wbaltv.com/article/inner-harbor-free-fitness-program-baltimore/73495869
  - (wellness) [Condé Nast Traveler] 08/18/2026, 08:43 PM, +0000 UTC — Is Traveling for Stargazing the Next Big Wellness Craze? These Hotels Are Betting on It
    
    Link: https://www.cntraveler.com/story/is-traveling-for-stargazing-the-next-big-wellness-craze-these-hotels-are-betting-on-it
  - (wellness) [Hartford Hospital] 08/21/2026, 02:17 PM, +0000 UTC — 10 Wellness Trends Everyone’s Trying Right Now. Here’s What Actually Works
    
    Link: https://hartfordhospital.org/about-hh/news-center/news-detail?articleId=74682
  - (medical study) [Harvard Medical School] 08/17/2026, 04:05 PM, +0000 UTC — Pilots, Flight Attendants Have Greater Risk of Radiation-Related Cancer Death Than Other Professions
    
    Link: https://hms.harvard.edu/news/pilots-flight-attendants-have-greater-risk-radiation-related-cancer-death-other-professions
  - (medical study) [NPR] 08/19/2026, 03:22 PM, +0000 UTC — A real-world study of Oregon's nonmedical psilocybin program shows promise
    
    Link: https://www.npr.org/2026/08/19/nx-s1-5936443/oregon-psilocybin-ptsd-depression-anxiety
  - (medical study) [UMass Chan Medical School] 08/24/2026, 04:17 AM, +0000 UTC — UMass Chan researchers study psychedelic medication for adjustment disorder in people with serious medical conditions
    
    Link: https://www.umassmed.edu/news/articles/2026/08/umass-chan-researchers-study-psychedelic-medication-for-adjustment-disorder-in-people-with-serious-medical-conditions/
  - (medical study) [Johns Hopkins Medicine] 08/19/2026, 03:53 PM, +0000 UTC — Bacteria Found in Lung Tumors May Boost Immune Response to Cancer
    
    Link: https://www.hopkinsmedicine.org/news/newsroom/news-releases/2026/08/bacteria-found-in-lung-tumors-may-boost-immune-response-to-cancer
  - (medical study) [Michigan Medicine] 08/19/2026, 12:00 PM, +0000 UTC — College of Pharmacy alum advances U-M Medical School addiction research
    
    Link: https://www.michiganmedicine.org/philanthropy-news/college-pharmacy-alum-advances-u-m-medical-school-addiction-research
  - (medical study) [PR Newswire] 08/19/2026, 11:00 AM, +0000 UTC — Galmed Announces Successful First-in-Human Proof-of-Concept Clinical Study Results for Colospan's Novel Intraoperative Tissue Assessment Technology
    
    Link: https://www.prnewswire.com/news-releases/galmed-announces-successful-first-in-human-proof-of-concept-clinical-study-results-for-colospans-novel-intraoperative-tissue-assessment-technology-302855153.html
  - (medical study) [Nature] 08/19/2026, 10:17 AM, +0000 UTC — Large-scale AI-guided liver malignancy diagnosis: multicenter study and a single-arm trial
    
    Link: https://www.nature.com/articles/s41591-026-04589-y
  - (medical study) [WSJ] 08/19/2026, 09:30 AM, +0000 UTC — Exclusive | Startup to Link ‘Biobanks’ of Patient Tissue to Supercharge AI Medical Research
    
    Link: https://www.wsj.com/pro/venture-capital/startup-to-link-biobanks-of-patient-tissue-to-supercharge-ai-medical-research-55403925
  - (medical study) [Stanford Medicine] 08/19/2026, 09:51 PM, +0000 UTC — ‘Molecular glue’ turns a cancer driver into a built-in kill switch in Stanford Medicine study
    
    Link: https://med.stanford.edu/news/all-news/2026/08/lymphoma-BCL6-kill-switch.html
  - (medical study) [WashU Medicine] 08/17/2026, 08:03 PM, +0000 UTC — Laser therapy offers weapon against deadly brain tumors
    
    Link: https://medicine.washu.edu/news/laser-therapy-offers-weapon-against-deadly-brain-tumors/
  - (medical study) [UT Southwestern] 08/21/2026, 03:58 PM, +0000 UTC — Brain activity discovery could transform Parkinson’s treatment: Newsroom
    
    Link: https://www.utsouthwestern.edu/newsroom/articles/year-2026/aug-brain-activity-parkinsons-treatment.html
  - (medical study) [KSWO 7News] 08/20/2026, 12:50 AM, +0000 UTC — State legislators to hold study examining medical marijuana in October
    
    Link: https://www.kswo.com/2026/08/20/state-legislators-hold-study-examining-medical-marijuana-october/
  - (clinical trial health) [CNN] 08/22/2026, 04:00 PM, +0000 UTC — You want to join a clinical trial. Here’s what to know about the hurdles.
    
    Link: https://www.cnn.com/2026/08/22/health/clinical-trials-what-to-know
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
  - (clinical trial health) [Nutrition Insight] 08/21/2026, 04:17 PM, +0000 UTC — Perelel’s Triple-Support protein shows promise for women’s health in clinical trial
    
    Link: https://www.nutritioninsight.com/news/perelel-triple-support-protein-womens-health.html
  - (clinical trial health) [News-Medical] 08/20/2026, 05:52 PM, +0000 UTC — Federal and industry sponsors play complementary roles in cancer clinical trials
    
    Link: https://www.news-medical.net/news/20260820/Federal-and-industry-sponsors-play-complementary-roles-in-cancer-clinical-trials.aspx
  - (clinical trial health) [Straits Research] 08/19/2026, 07:00 AM, +0000 UTC — Clinical Trials Market Size, Share, Growth, Analysis, Report, 2034
    
    Link: https://straitsresearch.com/report/clinical-trials-market
  - (FDA recall health) [The New York Times] 08/19/2026, 07:00 AM, +0000 UTC — F.D.A. Classifies Egg Recall as Class I, for Highest Health Risk
    
    Link: https://www.nytimes.com/2026/08/14/health/fda-egg-recall-salmonella.html
  - (FDA recall health) [CBS News] 08/19/2026, 10:52 PM, +0000 UTC — FDA upgrades recall of frozen blueberries sold at Publix to highest health risk level
    
    Link: https://www.cbsnews.com/news/blueberry-recall-fda-class-1-risk/
  - (FDA recall health) [CIDRAP] 08/17/2026, 08:27 PM, +0000 UTC — FDA heightens egg recall to reflect potential ‘serious adverse health consequences or death’
    
    Link: https://www.cidrap.umn.edu/foodborne-disease/fda-heightens-egg-recall-reflect-potential-serious-adverse-health-consequences-or
  - (FDA recall health) [fda.gov] 08/18/2026, 12:00 AM, +0000 UTC — Early Alert: Convenience Kit Issue from Becton Dickinson
    
    Link: https://www.fda.gov/medical-devices/medical-device-recalls-and-early-alerts/early-alert-convenience-kit-issue-becton-dickinson
  - (FDA recall health) [Axios] 08/22/2026, 10:01 AM, +0000 UTC — Here's why the FDA hit frozen blueberries with its highest risk warning
    
    Link: https://www.axios.com/2026/08/22/frozen-blueberries-recall-fda-high-risk-warning
  - (FDA recall health) [Denver7] 08/18/2026, 12:25 AM, +0000 UTC — FDA upgrades egg recall to highest health-risk level amid string of food safety concerns
    
    Link: https://www.denver7.com/news/local-news/fda-upgrades-egg-recall-to-highest-health-risk-level-amid-string-of-food-safety-concerns
  - (FDA recall health) [The Washington Post] 08/21/2026, 12:15 AM, +0000 UTC — FDA upgrades recall of frozen berries to highest-risk warning
    
    Link: https://www.washingtonpost.com/health/2026/08/20/fda-upgrades-recall-frozen-berries-highest-risk-warning/
  - (FDA recall health) [Centers for Disease Control and Prevention | CDC (.gov)] 08/20/2026, 07:00 AM, +0000 UTC — Cyclospora Outbreak Linked to Iceberg Lettuce | Cyclosporiasis
    
    Link: https://www.cdc.gov/cyclosporiasis/outbreaks/07-26/index.html
  - (FDA recall health) [Healthline] 08/20/2026, 06:18 PM, +0000 UTC — FDA Upgrades Publix Frozen Blueberry Recall to Highest Health Risk Level
    
    Link: https://www.healthline.com/health-news/fda-upgrades-publix-frozen-blueberry-recall-highest-risk-level
  - (FDA recall health) [NewsNation] 08/22/2026, 12:29 PM, +0000 UTC — Food recalls aren’t a success story, former FDA official says
    
    Link: https://www.newsnationnow.com/health/food-recalls-arent-success-story-former-fda-official/
  - (FDA recall health) [11Alive.com] 08/20/2026, 02:42 PM, +0000 UTC — Blueberry recall in 8 states upgraded to FDA's highest health risk level
    
    Link: https://www.11alive.com/article/news/nation-world/blueberry-recall-in-8-states-upgraded-to-most-dangerous-classification/507-13ecdd2b-9e5a-427c-b889-b6d394d180c4
  - (FDA recall health) [Ophthalmology Times] 08/20/2026, 11:01 AM, +0000 UTC — FDA recalls eye drop that relieves ocular itch for potential contamination
    
    Link: https://www.ophthalmologytimes.com/view/fda-recall-eye-drop-that-relieves-ocular-itch-potential-contamination