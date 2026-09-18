# LIVE SIGNAL DATA — SerpAPI Pre-Fetch
The following signals were fetched from SerpAPI Google News and SerpAPI Google Trends immediately before this pipeline run. Treat Google Trends as AVAILABLE when this section contains a Google Trends block. Use it as the primary search_velocity input for Skills 01–05 (Signal Listener through Trend Strength Scorer). Use the Google News Radar as the broad discovery layer for news-led health topics, including topics that do not yet appear in Google Trends. Prioritize topics with convergence across News, Trends, primary/institutional sources, and credible publisher coverage.

## Google Trends — Trending Now (US / Health, real-time)
Terms with a "Why:" line have a confirmed real-world news story driving the spike; terms without one are a real-time signal only, not yet grounded in a specific story.
  - porsha williams emergency partial hysterectomy
    Why: "Porsha Williams Always Wanted More Kids. Then She Lost the Choice." — Glamour

## Google Trends — 7-Day Interest (US)
  - **health**: latest=80, peak=100, 7d-delta=-5
    Rising related: videra health, google fitbit air screenless fitness & health tracker, health gadgets, mitch mcconnell health, health plants, health nature, mental health, health insurance
  - **wellness**: latest=71, peak=100, 7d-delta=+2
    Rising related: energy wellness center hickory nc, grocery delivery, bakari silverback wellness exam, grocery near me, wizard wellness nasal spray, circle wellness fremont, energy wellness center, wizard wellness
  - **nutrition**: latest=61, peak=100, 7d-delta=-4
    Rising related: optimum nutrition beer, optimum nutrition protein beer, nutrition information theweeklyhealthiness, five guys nutrition, acorn squash nutrition, nutrition facts, what is nutrition, nutrition near me
  - **fitness**: latest=61, peak=100, 7d-delta=+2
    Rising related: female marines combat fitness test, google fitbit air screenless fitness & health tracker, new army fitness test, meditation, hiking, army fitness test, gardening, museums
  - **food safety**: latest=31, peak=100, 7d-delta=-1
    Rising related: chipotle palantir food safety partnership, splenda chemical safety research, best laptop for work, what is a prepaid sim card, cheapest flights to tokyo, best pizza near me, what is a fermented food, food festivals near me
  - **diet**: latest=63, peak=100, 7d-delta=+2
    Rising related: wes anderson, dash4d diet a1c levels reduction, history of soybeans in us diet, matt damon diet, what is the lion diet, lions diet, the lion diet, lion diet
  - **weight loss**: latest=32, peak=100, 7d-delta=+1
    Rising related: cb1 blockers weight loss study, chrissy metz weight loss, glp 1, embody, medvi, medvi weight loss, weight loss medication, weight loss pills
  - **mental health**: latest=73, peak=100, 7d-delta=-5
    Rising related: did lizzie borden have mental health issues, mental health women villakalima, mental health women villakalima.com, mental health organizations near me, teen mental health treatment malibu ca visionsteen.com, mla citation generator, teen mental health treatment malibu ca visionsteen, what is mental health
  - **gut health**: latest=17, peak=100, 7d-delta=+0
    Rising related: how to restore gut health after antibiotics, leaky gut symptoms, best probiotic yogurt for gut health, how to repair gut health, best supplements for gut health and bloating, how to check gut health, improve gut health, how to improve gut health

Top rising related queries from Google Trends:
  - videra health
  - google fitbit air screenless fitness & health tracker
  - health gadgets
  - mitch mcconnell health
  - health plants
  - health nature
  - mental health
  - health insurance
  - energy wellness center hickory nc
  - grocery delivery
  - bakari silverback wellness exam
  - grocery near me
  - wizard wellness nasal spray
  - circle wellness fremont
  - energy wellness center
  - wizard wellness
  - optimum nutrition beer
  - optimum nutrition protein beer
  - nutrition information theweeklyhealthiness
  - five guys nutrition

## Google News Radar — Recent Health Topics (144 unique across 12 queries; showing 60)
Treat these headlines as the broad radar of news-led health topics. The Signal Listener must consider this radar before narrowing to retained candidates.
  - (health) [House Committee on Energy and Commerce (.gov)] 09/15/2026, 02:30 PM, +0000 UTC — Health Hearing: Examining Legislative Proposals to Reform Medicare Provider Payment and Bolster Health Care Cybersecurity
    
    Link: https://energycommerce.house.gov/events/health-hearing-examining-legislative-proposals-to-reform-medicare-provider-payment-and-bolster-health-care-cybersecurity
  - (health) [Office of Governor Tate Reeves (.gov)] 09/14/2026, 03:39 PM, +0000 UTC — Governor Reeves Announces 167 Rural Health Transformation Program Awards Totaling More Than $104 Million
    
    Link: https://governorreeves.ms.gov/governor-reeves-announces-167-rural-health-transformation-program-awards-totaling-more-than-104-million/
  - (health) [NPR] 09/16/2026, 10:00 AM, +0000 UTC — Senators question Trump's picks for top health positions, including surgeon general
    
    Link: https://www.npr.org/2026/09/16/nx-s1-5968780/trump-rfk-jr-health-nomination-surgeon-general
  - (health) [World Health Organization (WHO)] 09/15/2026, 07:00 AM, +0000 UTC — Mental health at work
    
    Link: https://www.who.int/news-room/fact-sheets/detail/mental-health-at-work
  - (health) [WBAL-TV] 09/17/2026, 08:46 PM, +0000 UTC — Patients file class-action lawsuit over Luminis Health cyberattack
    
    Link: https://www.wbaltv.com/article/luminis-health-aamc-cyberattack-class-action-lawsuit/73779157
  - (health) [Nature] 09/12/2026, 03:34 PM, +0000 UTC — Young minds in distress: Exploring the global rise in youth mental health diagnoses
    
    Link: https://www.nature.com/articles/s41380-026-03884-x
  - (health) [Center on Budget and Policy Priorities] 09/15/2026, 07:00 AM, +0000 UTC — Analyzing the Census Bureau’s 2025 Poverty, Income, and Health Insurance Data
    
    Link: https://www.cbpp.org/blog/analyzing-the-census-bureaus-2025-poverty-income-and-health-insurance-data
  - (health) [Time Magazine] 09/15/2026, 02:40 PM, +0000 UTC — The Signs Caregiving Is Harming Your Health—and How To Protect Yourself
    
    Link: https://time.com/article/2026/09/15/caregiver-stress-health-warning-signs/
  - (health) [VTDigger] 09/15/2026, 09:37 PM, +0000 UTC — Hundreds of layoffs announced at the 2 largest healthcare networks Vermonters rely on
    
    Link: https://vtdigger.org/2026/09/15/hundreds-of-layoffs-announced-at-the-two-largest-healthcare-networks/
  - (health) [mprnews.org] 09/16/2026, 04:00 PM, +0000 UTC — AI diagnoses a major factor in Allina Health's doctors strike
    
    Link: https://www.mprnews.org/story/2026/09/16/allina-healths-doctors-strike-takes-on-ai-diagnoses
  - (health) [NYC Health + Hospitals] 09/17/2026, 05:28 PM, +0000 UTC — NYC Health + Hospitals and Maimonides Health Transaction Moves Forward After New York State Health Planning Council Vote
    
    Link: https://www.nychealthandhospitals.org/pressrelease/nyc-health-hospitals-and-maimonides-health-transaction-moves-forward-after-new-york-state-health-planning-council-vote/
  - (health) [mercy.net] 09/17/2026, 08:16 PM, +0000 UTC — Alice L. Walton Foundation and Mercy Break Ground on AWSOM Whole Health Campus, Marking a New Era for Whole-Person Health in the Heartland
    
    Link: https://www.mercy.net/newsroom/2026-09-17/alice-l--walton-foundation-and-mercy-break-ground-on-awsom-whole0/
  - (wellness) [The New York Times] 09/13/2026, 07:00 AM, +0000 UTC — Trading Keggers for ‘Wellness Darties’
    
    Link: https://www.nytimes.com/2026/09/11/style/wellness-darties-college-gen-z-tiktok.html
  - (wellness) [University of North Carolina School of the Arts] 09/18/2026, 01:49 PM, +0000 UTC — Miles for Wellness 34 registration open now
    
    Link: https://www.uncsa.edu/announcements/20260918-miles-for-wellness.aspx
  - (wellness) [People.com] 09/17/2026, 09:24 PM, +0000 UTC — Workers Hold Silverback Gorilla Bakari’s Hand During His First Wellness Checkup at Disney’s Animal Kingdom
    
    Link: https://people.com/workers-hold-gorillas-hand-during-disney-wellness-checkup-12126619
  - (wellness) [purdue.edu] 09/15/2026, 10:07 AM, +0000 UTC — Upcoming Road to Retirement conference offers financial wellness, retirement resources for every stage of employee journey
    
    Link: https://www.purdue.edu/newsroom/purduetoday/2026/Q3/upcoming-road-to-retirement-conference-offers-financial-wellness-retirement-resources-for-every-stage-of-employee-journey
  - (wellness) [WPR] 09/17/2026, 10:00 AM, +0000 UTC — Aurora Health Care 'health and wellness hub' going into closed school building in Milwaukee
    
    Link: https://www.wpr.org/news/aurora-health-care-wellness-hub-closed-school-building-milwaukee
  - (wellness) [Drake University Newsroom] 09/17/2026, 02:30 PM, +0000 UTC — The Harkin Institute Announces Victoria Brenton as New Wellness and Nutrition Director
    
    Link: https://news.drake.edu/2026/09/17/the-harkin-institute-announces-victoria-brenton-as-new-wellness-and-nutrition-director/
  - (wellness) [Liberty University] 09/14/2026, 07:51 PM, +0000 UTC — Beyond the gym: Sharon Olowoyo expand's Liberty's approach to Health and Wellness | Liberty Champion
    
    Link: https://www.liberty.edu/champion/2026/09/14/beyond-the-gym-sharon-olowoyo-expands-libertys-approach-to-health-and-wellness/
  - (wellness) [The Business Journals] 09/16/2026, 06:27 AM, +0000 UTC — Is the wellness club the new nightclub? A Seattle entrepreneur is betting on it
    
    Link: https://www.bizjournals.com/seattle/news/2026/09/15/sanctuary-wellness-gym-denny-triangle-luxury.html
  - (wellness) [umw.edu] 09/14/2026, 06:58 PM, +0000 UTC — UMW Earns National Recognition for Value, Future Readiness and Student Wellness
    
    Link: https://www.umw.edu/news/2026/09/14/umw-earns-national-recognition-for-value-future-readiness-and-student-wellness/
  - (wellness) [UKNow] 09/15/2026, 07:00 AM, +0000 UTC — UK’s Be Healthy Bash returns Sept. 19 with free health and wellness resources
    
    Link: https://uknow.uky.edu/uk-healthcare/uk-s-be-healthy-bash-returns-sept-19-free-health-and-wellness-resources
  - (wellness) [University of Scranton] 09/14/2026, 08:04 PM, +0000 UTC — Employee Wellness Program To Offer Flu Shots, Fall Classes
    
    Link: https://news.scranton.edu/articles/2026/09/ann-chew-flu-wellness.shtml
  - (wellness) [Case Western Reserve University] 09/15/2026, 11:05 AM, +0000 UTC — Complete 2027 Wellness Incentive Program activities by Nov. 30 deadline
    
    Link: https://case.edu/news/complete-2027-wellness-incentive-program-activities-nov-30-deadline
  - (medical study) [Stanford Medicine] 09/16/2026, 03:05 PM, +0000 UTC — Stanford Medicine team creates advanced model for studying brain development, disorders
    
    Link: https://med.stanford.edu/news/all-news/2026/09/model-to-study-brain-development.html
  - (medical study) [The Guardian] 09/17/2026, 09:01 PM, +0000 UTC — Hundreds of ageing Americans may not get results of Alzheimer’s study due to Trump cuts
    
    Link: https://www.theguardian.com/us-news/2026/sep/17/trump-cuts-alzheimers-disease-study
  - (medical study) [ama-assn.org] 09/15/2026, 03:20 PM, +0000 UTC — AMA and Atalan launch collaboration to advance physician retention research
    
    Link: https://www.ama-assn.org/press-center/ama-press-releases/ama-and-atalan-launch-collaboration-advance-physician-retention
  - (medical study) [OHSU News] 09/17/2026, 02:57 PM, +0000 UTC — Intermittent fasting shows promise in slowing Huntington’s disease progression
    
    Link: https://news.ohsu.edu/2026/09/17/intermittent-fasting-shows-promise-in-slowing-huntingtons-disease-progression
  - (medical study) [uta.edu] 09/16/2026, 11:39 PM, +0000 UTC — UTA study to focus on reducing radiation exposure from medical imaging procedures
    
    Link: https://www.uta.edu/academics/schools-colleges/science/news/2026/09/16/uta-study-to-focus-on-reducing-radiation-exposure-from-medical-imaging-procedures
  - (medical study) [Mayo Clinic News Network] 09/16/2026, 01:00 PM, +0000 UTC — Mayo Clinic first to study minibeam radiotherapy in patients with difficult-to-treat cancers
    
    Link: https://newsnetwork.mayoclinic.org/discussion/mayo-clinic-first-to-study-minibeam-radiotherapy-in-patients-with-difficult-to-treat-cancers/
  - (medical study) [UT Southwestern] 09/16/2026, 04:44 PM, +0000 UTC — Scientists discover metabolite fueling aggressive brain tumor growth: Newsroom
    
    Link: https://www.utsouthwestern.edu/newsroom/articles/year-2026/sept-aggressive-brain-tumor-growth.html
  - (medical study) [Nature] 09/13/2026, 07:41 AM, +0000 UTC — Clinical usability of an explainable AI decision support tool and evaluation of multimodal models in NSCLC
    
    Link: https://www.nature.com/articles/s41591-026-04488-2
  - (medical study) [Medical Xpress] 09/17/2026, 09:00 AM, +0000 UTC — Anti-seizure drug fights aggressive childhood brain tumors, study shows
    
    Link: https://medicalxpress.com/news/2026-09-anti-seizure-drug-aggressive-childhood.html
  - (medical study) [University of Miami] 09/16/2026, 04:03 PM, +0000 UTC — PanCAN Funds Sylvester Study of Blood Test for Pancreatic Cancer
    
    Link: https://news.med.miami.edu/pancan-grant-ctdna-blood-test-pancreatic-cancer/
  - (medical study) [South Florida Hospital News] 09/18/2026, 01:37 PM, +0000 UTC — New Stroke Recovery Study at Sarasota Memorial
    
    Link: https://southfloridahospitalnews.com/2026/09/18/new-stroke-recovery-study-at-sarasota-memorial/
  - (medical study) [Time Magazine] 09/17/2026, 04:01 AM, +0000 UTC — Having Health Insurance Doesn’t Prevent Medical Debt
    
    Link: https://time.com/article/2026/09/17/having-health-insurance-doesnt-prevent-medical-debt/
  - (clinical trial health) [Florida International University] 09/16/2026, 04:05 PM, +0000 UTC — FIU/Baptist Health physician-researchers explore ways to expand clinical trial participation
    
    Link: https://news.fiu.edu/2026/fiubaptist-health-physician-researchers-explore-ways-to-expand-clinical-trial-participation
  - (clinical trial health) [UCI Health] 09/16/2026, 07:00 AM, +0000 UTC — Novel clinical trial cures woman’s uncontrolled hypertension
    
    Link: https://www.ucihealth.org/blog/2026/09/clinical-trial-cures-womans-hypertension
  - (clinical trial health) [The Business Journals] 09/15/2026, 01:54 PM, +0000 UTC — How Advocate Health is mobilizing one of the nation’s largest clinical research networks to serve more communities
    
    Link: https://www.bizjournals.com/charlotte/news/2026/09/15/advocate-health-clinical-research-networks-serve.html
  - (clinical trial health) [appliedclinicaltrialsonline.com] 09/16/2026, 05:03 PM, +0000 UTC — Benchmarking Study Finds Clinical Trial Performance Is Shaped by Operating Model Design, Not Sourcing Strategy
    
    Link: https://www.appliedclinicaltrialsonline.com/view/benchmarking-study-finds-clinical-trial-performance-operating-model-design-sourcing-strategy
  - (clinical trial health) [The Clinical Trial Vanguard] 09/16/2026, 07:31 AM, +0000 UTC — “Hard to Reach” Is a Sponsor Operations Failure, Not a Population Problem
    
    Link: https://www.clinicaltrialvanguard.com/clinical-trial-ops-brief/hard-to-reach-is-a-sponsor-operations-failure-not-a-population-problem/
  - (clinical trial health) [Fierce Biotech] 09/15/2026, 06:09 PM, +0000 UTC — FDA launches pilot program to speed up sluggish phase 1 trials
    
    Link: https://www.fiercebiotech.com/biotech/fda-launches-pilot-program-speed-sluggish-phase-1-trials
  - (clinical trial health) [divisionofresearch.kaiserpermanente.org] 09/17/2026, 04:27 PM, +0000 UTC — Kaiser Permanente’s enrollment in cancer clinical trials reflects the diversity of its patients
    
    Link: https://divisionofresearch.kaiserpermanente.org/clinical-trials-patient-diversity/
  - (clinical trial health) [The Washington Post] 09/17/2026, 04:00 PM, +0000 UTC — FDA-ordered studies of many drugs, devices on the market are not done
    
    Link: https://www.washingtonpost.com/health/2026/09/17/fda-ordered-studies-many-drugs-devices-market-are-not-done/
  - (clinical trial health) [Medical Xpress] 09/17/2026, 10:30 PM, +0000 UTC — HIV injections work better than tablets for young people, clinical trial finds
    
    Link: https://medicalxpress.com/news/2026-09-hiv-tablets-young-people-clinical.html
  - (clinical trial health) [Rethinking Clinical Trials] 09/17/2026, 02:19 PM, +0000 UTC — September 17, 2026: IMPACT Collaboratory Seeks Applicants for 2027 Health Care Systems Scholars Program
    
    Link: https://rethinkingclinicaltrials.org/news/september-17-2026-impact-collaboratory-seeks-applicants-for-2027-health-care-systems-scholars-program/
  - (clinical trial health) [unc.edu] 09/17/2026, 04:31 PM, +0000 UTC — UNC Health, School of Medicine leaders build connections in Ireland
    
    Link: https://www.unc.edu/posts/2026/09/17/unc-health-school-of-medicine-leaders-build-connections-in-ireland/
  - (clinical trial health) [HCI Innovation Group] 09/17/2026, 06:39 AM, +0000 UTC — ResearchPass Puts Clinical Trial Info on Participants’ Smartphones
    
    Link: https://www.hcinnovationgroup.com/clinical-it/learning-health-systems-research/news/55405529/researchpass-puts-clinical-trial-info-on-participants-smartphones
  - (FDA recall health) [Scripps News] 09/17/2026, 02:00 AM, +0000 UTC — FDA warns recalled hand soaps may contain harmful bacteria
    
    Link: https://www.scrippsnews.com/health/fda-warns-recalled-hand-soaps-may-contain-harmful-bacteria
  - (FDA recall health) [FOX 5 Atlanta] 09/16/2026, 08:32 PM, +0000 UTC — FDA recalls hand soap sold in 15 states due to risk of bacteria
    
    Link: https://www.fox5atlanta.com/news/fda-recalls-hand-soaps-sold-georgia-over-bacteria-risk
  - (FDA recall health) [Health.com] 09/16/2026, 03:09 PM, +0000 UTC — FDA Announces Hand Soap Recall in 15 States—Thousands of Bottles May Contain Bacteria
    
    Link: https://www.health.com/hand-soap-recall-september-2026-12123997
  - (FDA recall health) [The Healthy @Reader's Digest] 09/12/2026, 01:32 PM, +0000 UTC — The FDA Just Expanded a Walmart Berries Recall to 11 More States
    
    Link: https://www.thehealthy.com/news/fda-walmart-berries-recall-update-september-2026/
  - (FDA recall health) [WLOS] 09/17/2026, 08:16 PM, +0000 UTC — FDA recalls hand soaps from Ingles over potential bacterial contamination
    
    Link: https://wlos.com/news/local/fda-recalls-hand-soaps-laura-lynn-ingles-markets-potential-bacterial-contamination-food-drug-administration-honey-apple-crisp-pear-scent-foaming-liquid
  - (FDA recall health) [eatingwell.com] 09/14/2026, 07:29 PM, +0000 UTC — The FDA Warns This Common Cookware May Leach Lead—Here’s What’s Safe to Use Instead
    
    Link: https://www.eatingwell.com/fda-lead-leaching-cookware-replacements-amazon-12114030
  - (FDA recall health) [New York Post] 09/17/2026, 04:44 PM, +0000 UTC — Popular Walmart and Target frozen dessert recalled nationwide due to contamination
    
    Link: https://nypost.com/2026/09/17/lifestyle/so-delicious-ice-cream-recalled-nationwide-over-stones-found-in-pints-fda/
  - (FDA recall health) [The Asheville Citizen Times] 09/16/2026, 04:26 PM, +0000 UTC — Ingles hand soap, others recalled in NC for bacterial contamination
    
    Link: https://www.citizen-times.com/story/news/health/2026/09/16/fda-recalls-hand-soap-sold-in-north-carolina-ingles/91790211007/
  - (FDA recall health) [NBC 5 Chicago] 09/16/2026, 07:50 PM, +0000 UTC — Hand soap recall issued for products distributed in 16 states, including Illinois
    
    Link: https://www.nbcchicago.com/news/local/hand-soap-recall-issued-for-products-sold-in-15-states-including-illinois/3989902/
  - (FDA recall health) [WKYC] 09/16/2026, 03:59 PM, +0000 UTC — FDA upgrades hand soap recall to Class II warning over 'potential bacterial contamination'
    
    Link: https://www.wkyc.com/article/news/nation-world/fda-hand-soap-recall-15-states-class-ii-warning/507-6c68423a-e212-4714-b8fd-2ce5ffba8631
  - (FDA recall health) [Dallas News] 09/18/2026, 01:25 AM, +0000 UTC — FDA designates hand soap recall in Texas, 14 other states as Class II
    
    Link: https://www.dallasnews.com/news/public-health/article/hand-soap-recall-texas-designated-class-ii-fda-22436809.php
  - (FDA recall health) [USA Today] 09/16/2026, 06:21 PM, +0000 UTC — Hand soap recalled for infection risk. See affected products
    
    Link: https://www.usatoday.com/story/money/consumer-protection/recalls-alerts/2026/09/16/hand-soap-recall-bacteria-states/91789354007/