# LIVE SIGNAL DATA — SerpAPI Pre-Fetch
The following signals were fetched from SerpAPI Google News and SerpAPI Google Trends immediately before this pipeline run. Treat Google Trends as AVAILABLE when this section contains a Google Trends block. Use it as the primary search_velocity input for Skills 01–05 (Signal Listener through Trend Strength Scorer). Use the Google News Radar as the broad discovery layer for news-led health topics, including topics that do not yet appear in Google Trends. Prioritize topics with convergence across News, Trends, primary/institutional sources, and credible publisher coverage.

## Google Trends — Trending Now (US / Health, real-time)
Terms with a "Why:" line have a confirmed real-world news story driving the spike; terms without one are a real-time signal only, not yet grounded in a specific story.
  - fiji hiv
    Why: "Fiji declares HIV emergency. One in 60 people now have the virus as drug crisis fuels outbreak" — CNN
  - nicole saphier
    Why: "What a social media influencer turned surgeon general could mean for public health in the US" — CNN

## Google Trends — 7-Day Interest (US)
  - **health**: latest=93, peak=100, 7d-delta=-5
    Rising related: devoted health careers, health gadgets, mitch mcconnell health, mental health, health insurance, behavioral health, health department, university health
  - **wellness**: latest=78, peak=100, 7d-delta=-3
    Rising related: wizard wellness nasal spray, wizard wellness, naturaplug health and wellness, blackwood wellness dispensary, parenting wellness infoguide famparentlife, earthly wellness, greenheal.net wellness coach, wellness darties
  - **nutrition**: latest=80, peak=100, 7d-delta=-6
    Rising related: optimum nutrition protein beer, optimum nutrition beer, supplemental nutrition assistance program, acorn squash nutrition, nutrition facts, what is nutrition, nutrition label, nutrition near me
  - **fitness**: latest=62, peak=100, 7d-delta=-1
    Rising related: pentagon military fitness standards, female marines combat fitness test, jill brown fitness, helena christensen fitness routine strength training, new army fitness test, google fitbit air screenless fitness & health tracker, carrie sisson fitness advice aging, army fitness test
  - **food safety**: latest=72, peak=100, 7d-delta=+4
    Rising related: splenda chemical safety research, one of the most important reasons for using only reliable water sources is to reduce, best thai food near me, what does fifo stand for in food safety, what is a type of contaminant that can cause foodborne illness? chemical preservatives organic ingredients cholesterol parasites, ias brand safety, which food safety practice will help prevent biological hazards, icev
  - **diet**: latest=81, peak=100, 7d-delta=+3
    Rising related: dr. james stone egg diet, history of soybeans in us diet, wes anderson, wes anderson movies, dash4d diet a1c levels reduction, diet coke costume, when did diet coke come out, diet coke
  - **weight loss**: latest=33, peak=100, 7d-delta=-3
    Rising related: shokz.com, chrissy metz weight loss, glp 1, embody, medvi weight loss, medvi, weight loss medication, weight loss pills
  - **mental health**: latest=96, peak=100, 7d-delta=+8
    Rising related: mental health women villakalima, mental health women villakalima.com, teen mental health treatment, elizabeth holmes mental health diagnosis, world mental health day, mental health specialist, what is mental health, mental health services
  - **gut health**: latest=27, peak=100, 7d-delta=+2
    Rising related: seed probiotics, adhd and gut health, ryze mushroom coffee, best mushroom coffee for gut health, probiotics for dogs gut health, best milk for gut health, l glutamine for gut health, best bone broth for gut health

Top rising related queries from Google Trends:
  - devoted health careers
  - health gadgets
  - mitch mcconnell health
  - mental health
  - health insurance
  - behavioral health
  - health department
  - university health
  - wizard wellness nasal spray
  - wizard wellness
  - naturaplug health and wellness
  - blackwood wellness dispensary
  - parenting wellness infoguide famparentlife
  - earthly wellness
  - greenheal.net wellness coach
  - wellness darties
  - optimum nutrition protein beer
  - optimum nutrition beer
  - supplemental nutrition assistance program
  - acorn squash nutrition

## Google News Radar — Recent Health Topics (144 unique across 12 queries; showing 60)
Treat these headlines as the broad radar of news-led health topics. The Signal Listener must consider this radar before narrowing to retained candidates.
  - (health) [House Committee on Energy and Commerce (.gov)] 09/15/2026, 02:30 PM, +0000 UTC — Health Hearing: Examining Legislative Proposals to Reform Medicare Provider Payment and Bolster Health Care Cybersecurity
    
    Link: https://energycommerce.house.gov/events/health-hearing-examining-legislative-proposals-to-reform-medicare-provider-payment-and-bolster-health-care-cybersecurity
  - (health) [Apple] 09/09/2026, 05:55 PM, +0000 UTC — Apple advances health and fitness capabilities using Apple Intelligence
    
    Link: https://www.apple.com/newsroom/2026/09/apple-advances-health-and-fitness-capabilities-using-apple-intelligence/
  - (health) [NPR] 09/16/2026, 10:00 AM, +0000 UTC — Senators question Trump's picks for top health positions, including surgeon general
    
    Link: https://www.npr.org/2026/09/16/nx-s1-5968780/trump-rfk-jr-health-nomination-surgeon-general
  - (health) [Centers for Disease Control and Prevention | CDC (.gov)] 09/10/2026, 09:15 PM, +0000 UTC — Nationwide Increase in Reported Human Rabies Exposures: Rabies Post-exposure Prophylaxis Administration
    
    Link: https://www.cdc.gov/han/php/notices/han00533.html
  - (health) [Office of Governor Tate Reeves (.gov)] 09/14/2026, 03:39 PM, +0000 UTC — Governor Reeves Announces 167 Rural Health Transformation Program Awards Totaling More Than $104 Million
    
    Link: https://governorreeves.ms.gov/governor-reeves-announces-167-rural-health-transformation-program-awards-totaling-more-than-104-million/
  - (health) [World Health Organization (WHO)] 09/15/2026, 06:36 PM, +0000 UTC — Third meeting of the Global Initiative on AI for Health
    
    Link: https://www.who.int/news-room/events/detail/2026/09/16/default-calendar/third-meeting-of-the-global-initiative-on-ai-for-health
  - (health) [aphis.usda.gov] 09/11/2026, 07:00 AM, +0000 UTC — Current Status of New World Screwworm | Screwworm.gov
    
    Link: https://www.aphis.usda.gov/animals/animal-health/livestock-and-poultry-disease/stop-screwworm/current-status
  - (health) [Nature] 09/12/2026, 03:34 PM, +0000 UTC — Young minds in distress: Exploring the global rise in youth mental health diagnoses
    
    Link: https://www.nature.com/articles/s41380-026-03884-x
  - (health) [Aeon] 09/10/2026, 10:04 AM, +0000 UTC — The curio cabinet of medieval mental health
    
    Link: https://aeon.co/essays/the-curio-cabinet-of-medieval-mental-health
  - (health) [WPR] 09/09/2026, 08:23 PM, +0000 UTC — SSM St. Mary’s nurses in Madison file federal labor complaint against health system
    
    Link: https://www.wpr.org/news/ssm-st-marys-nurses-madison-file-federal-labor-complaint-against-health-system
  - (health) [VTDigger] 09/15/2026, 09:37 PM, +0000 UTC — Hundreds of layoffs announced at the 2 largest healthcare networks Vermonters rely on
    
    Link: https://vtdigger.org/2026/09/15/hundreds-of-layoffs-announced-at-the-two-largest-healthcare-networks/
  - (health) [The New York Times] 09/14/2026, 01:58 PM, +0000 UTC — Trump Administration Moves to Integrate A.I. Into Medical Care Despite Concerns
    
    Link: https://www.nytimes.com/2026/09/14/health/ai-doctors-medicare-fda.html
  - (wellness) [The New York Times] 09/13/2026, 07:00 AM, +0000 UTC — Trading Keggers for ‘Wellness Darties’
    
    Link: https://www.nytimes.com/2026/09/11/style/wellness-darties-college-gen-z-tiktok.html
  - (wellness) [World Health Organization (WHO)] 09/16/2026, 10:42 AM, +0000 UTC — Mental health at work
    
    Link: https://www.who.int/news-room/fact-sheets/detail/mental-health-at-work
  - (wellness) [vogue.com] 09/11/2026, 09:30 AM, +0000 UTC — Meet the Wellness Brands Riding the Anti-Optimization Wave
    
    Link: https://www.vogue.com/article/meet-the-wellness-brands-riding-the-anti-optimization-wave
  - (wellness) [Montgomery County, MD (.gov)] 09/11/2026, 08:00 AM, +0000 UTC — Montgomery County to Host a Free Health and Wellness Fair on Saturday, Sept. 19 in White Oak
    
    Link: https://www.montgomerycountymd.gov/news/montgomery-county-host-free-health-wellness-fair-saturday-sept-19-white-oak
  - (wellness) [Purdue University] 09/15/2026, 10:07 AM, +0000 UTC — Upcoming Road to Retirement conference offers financial wellness, retirement resources for every stage of employee journey
    
    Link: https://www.purdue.edu/newsroom/purduetoday/2026/Q3/upcoming-road-to-retirement-conference-offers-financial-wellness-retirement-resources-for-every-stage-of-employee-journey
  - (wellness) [hklaw.com] 09/11/2026, 09:36 PM, +0000 UTC — Wellness Check: Analyzing Regulatory Risk Facing Innovative Health Platforms
    
    Link: https://www.hklaw.com/en/insights/publications/2026/09/wellness-check-analyzing-regulatory-risk-facing
  - (wellness) [Liberty University] 09/14/2026, 07:51 PM, +0000 UTC — Beyond the gym: Sharon Olowoyo expand's Liberty's approach to Health and Wellness | Liberty Champion
    
    Link: https://www.liberty.edu/champion/2026/09/14/beyond-the-gym-sharon-olowoyo-expands-libertys-approach-to-health-and-wellness/
  - (wellness) [CSUSM NewsCenter] 09/10/2026, 07:19 PM, +0000 UTC — Grant to Help CSUSM Expand Mobile Wellness Initiative's Reach
    
    Link: https://news.csusm.edu/grant-to-help-csusm-expand-mobile-wellness-initiatives-reach/
  - (wellness) [UKNow] 09/15/2026, 07:00 AM, +0000 UTC — UK’s Be Healthy Bash returns Sept. 19 with free health and wellness resources
    
    Link: https://uknow.uky.edu/uk-healthcare/uk-s-be-healthy-bash-returns-sept-19-free-health-and-wellness-resources
  - (wellness) [dvidshub.net] 09/11/2026, 08:54 PM, +0000 UTC — News - DCMA leadership prioritizes workforce wellness year-round
    
    Link: https://www.dvidshub.net/news/574494/dcma-leadership-prioritizes-workforce-wellness-year-round
  - (wellness) [Cobb County School District] 09/10/2026, 07:00 AM, +0000 UTC — Dickerson Earns National Recognition for Student Health and Wellness
    
    Link: https://www.cobbk12.org/dickerson/dickerson-earns-national-recognition-for-student-health-and-wellness.137189
  - (wellness) [University of Scranton] 09/14/2026, 08:04 PM, +0000 UTC — Employee Wellness Program To Offer Flu Shots, Fall Classes
    
    Link: https://news.scranton.edu/articles/2026/09/ann-chew-flu-wellness.shtml
  - (medical study) [Nature] 09/14/2026, 01:19 PM, +0000 UTC — Prospective evidence for conversational medical AI is hard, but non-negotiable
    
    Link: https://www.nature.com/articles/s41591-026-04639-5
  - (medical study) [Insilico Medicine] 09/10/2026, 07:31 AM, +0000 UTC — Insilico Medicine Doses First Patient in GENESIS-IPF-3, the World’s First Phase III Trial of a Generative AI-Driven Innovative Drug
    
    Link: https://insilico.com/news/isn1009261-insilico-medicine-doses-first-patient-genesis-ipf-3
  - (medical study) [brief.umn.edu] 09/15/2026, 12:00 PM, +0000 UTC — Aimee Osgood uses patient-led research to drive medical progress
    
    Link: https://brief.umn.edu/feature/aimee-osgood-uses-patient-led-research-drive-medical-progress
  - (medical study) [American Medical Association | AMA] 09/14/2026, 12:06 PM, +0000 UTC — Why some medical student research gets published—and some doesn’t
    
    Link: https://www.ama-assn.org/medical-students/succeed-medical-school/why-some-medical-student-research-gets-published-and-some
  - (medical study) [Healthcare Dive] 09/11/2026, 03:15 PM, +0000 UTC — Health spending tied to rise in premiums, new study finds
    
    Link: https://www.healthcaredive.com/news/health-spending-tied-to-rise-premiums-new-study-finds-jama/830144/
  - (medical study) [Yahoo Finance] 09/14/2026, 10:30 AM, +0000 UTC — Multi4 Medical Publishes Landmark Clinical Study in Prestigious BJUI - Initiates First Patient Treatments in Europe
    
    Link: https://finance.yahoo.com/healthcare/articles/multi4-medical-publishes-landmark-clinical-103000042.html
  - (medical study) [University of Hawaii System] 09/15/2026, 02:01 AM, +0000 UTC — UH medical students uncover promising HS football injury trend
    
    Link: https://www.hawaii.edu/news/2026/09/14/hs-football-injury-study/
  - (medical study) [The Harvard Crimson] 09/10/2026, 07:00 AM, +0000 UTC — Harvard and Yale Researchers Awarded $46 Million to Study Autism’s Origin in the Brain
    
    Link: https://www.thecrimson.com/article/2026/9/11/autism-origins-hms-grant/
  - (medical study) [News-Medical] 09/14/2026, 05:03 AM, +0000 UTC — More data, more answers? A 1.9 million-person health study shows why scale has limits
    
    Link: https://www.news-medical.net/news/20260914/More-data-more-answers-A-19-million-person-health-study-shows-why-scale-has-limits.aspx
  - (medical study) [FOX 9 Minneapolis-St. Paul] 09/12/2026, 09:55 PM, +0000 UTC — Inside Minnesota's cannabis safety checks
    
    Link: https://www.fox9.com/news/medical-cannabis-study-shows-cancer-patients-report-symptom-relief-2026
  - (medical study) [UVA Health] 09/09/2026, 08:15 PM, +0000 UTC — Trial Testing Out-of-Body Experiences Yields Unexpected Twist
    
    Link: https://www.uvahealth.com/news/trial-testing-out-of-body-experiences-yields-unexpected-twist
  - (medical study) [clinicalleader.com] 09/16/2026, 12:40 PM, +0000 UTC — Accelerating Chronic Disease Clinical Study Reports With AI-Enabled Medical Writing And Expert Oversight
    
    Link: https://www.clinicalleader.com/doc/accelerating-chronic-disease-clinical-study-reports-with-ai-enabled-medical-writing-and-expert-oversight-0001
  - (clinical trial health) [Florida International University] 09/16/2026, 03:19 PM, +0000 UTC — FIU/Baptist Health physician-researchers explore ways to expand clinical trial participation
    
    Link: https://news.fiu.edu/2026/fiubaptist-health-physician-researchers-explore-ways-to-expand-clinical-trial-participation
  - (clinical trial health) [University of Miami] 09/16/2026, 01:02 PM, +0000 UTC — ResearchPass Puts Clinical Trial Information at Participants’ Fingertips
    
    Link: https://news.med.miami.edu/researchpass-clinical-trial-digital-wallet/
  - (clinical trial health) [The Business Journals] 09/15/2026, 01:54 PM, +0000 UTC — How Advocate Health is mobilizing one of the nation’s largest clinical research networks to serve more communities
    
    Link: https://www.bizjournals.com/charlotte/news/2026/09/15/advocate-health-clinical-research-networks-serve.html
  - (clinical trial health) [Applied Clinical Trials Online] 09/10/2026, 06:57 PM, +0000 UTC — Recruitment in the Age of AI: Q&A with John Worden, Javara
    
    Link: https://www.appliedclinicaltrialsonline.com/view/recruitment-age-ai-john-worden-javara
  - (clinical trial health) [The Clinical Trial Vanguard] 09/16/2026, 07:31 AM, +0000 UTC — “Hard to Reach” Is a Sponsor Operations Failure, Not a Population Problem
    
    Link: https://www.clinicaltrialvanguard.com/clinical-trial-ops-brief/hard-to-reach-is-a-sponsor-operations-failure-not-a-population-problem/
  - (clinical trial health) [respiratory-therapy.com] 09/10/2026, 05:57 PM, +0000 UTC — ALA Expands Lung Cancer Clinical Trial Awareness
    
    Link: https://respiratory-therapy.com/disorders-diseases/cardiopulmonary-thoracic/lung-cancer/ala-expands-lung-cancer-clinical-trial-awareness/
  - (clinical trial health) [The Atlantic] 09/10/2026, 06:45 AM, +0000 UTC — Humanizing the Clinical Trial Experience Through Patient Engagement - Sponsor Content - Lilly
    
    Link: https://www.theatlantic.com/sponsored/lilly-2026/humanizing-clinical-trial/4131/
  - (clinical trial health) [Yahoo Finance] 09/10/2026, 12:45 PM, +0000 UTC — Optimi Health to Initiate Phase 2 Clinical Trial Evaluating Psilocybin-Assisted Therapy for Major Depressive Disorder
    
    Link: https://finance.yahoo.com/healthcare/articles/optimi-health-initiate-phase-2-124500744.html
  - (clinical trial health) [Medscape] 09/16/2026, 06:58 AM, +0000 UTC — Can Medical Evidence Be Trusted Without Scrutiny?
    
    Link: https://www.medscape.com/viewarticle/can-medical-evidence-be-trusted-without-scrutiny-2026a1000yap
  - (clinical trial health) [Fierce Biotech] 09/15/2026, 06:09 PM, +0000 UTC — FDA launches pilot program to speed up sluggish phase 1 trials
    
    Link: https://www.fiercebiotech.com/biotech/fda-launches-pilot-program-speed-sluggish-phase-1-trials
  - (clinical trial health) [University of Colorado Anschutz] 09/11/2026, 05:19 AM, +0000 UTC — There Aren’t Enough Clinical Trials on Suicide Prevention. A New Analysis Asks Why.
    
    Link: https://news.cuanschutz.edu/emergency-medicine/stanley-suicide-prevention-study
  - (clinical trial health) [HCI Innovation Group] 09/10/2026, 10:13 AM, +0000 UTC — Platform to Accelerate Clinical Research at Rush University System for Health
    
    Link: https://www.hcinnovationgroup.com/clinical-it/learning-health-systems-research/news/55403893/platform-to-accelerate-clinical-research-at-rush-university-system-for-health
  - (FDA recall health) [fda.gov] 09/11/2026, 12:00 AM, +0000 UTC — Outbreak Investigation of E. coli O145:H28: Frozen Blueberries (July 2026)
    
    Link: https://www.fda.gov/food/outbreaks-foodborne-illness/outbreak-investigation-e-coli-o145h28-frozen-blueberries-july-2026
  - (FDA recall health) [NewsNation] 09/10/2026, 08:38 PM, +0000 UTC — Epinephrine injection recalled over potentially fatal health risks: FDA
    
    Link: https://www.newsnationnow.com/us-news/recalls/epinephrine-injection-recalled-health-risks-fda/
  - (FDA recall health) [PBS] 09/09/2026, 09:26 PM, +0000 UTC — Cyclospora outbreak followed years of declining FDA foreign inspections
    
    Link: https://www.pbs.org/newshour/health/cyclospora-outbreak-followed-years-of-declining-fda-foreign-inspections
  - (FDA recall health) [fda.gov] 09/09/2026, 04:30 PM, +0000 UTC — Outbreak Investigation of Salmonella: Sprouts (September 2026)
    
    Link: https://www.fda.gov/food/outbreaks-foodborne-illness/outbreak-investigation-salmonella-sprouts-september-2026
  - (FDA recall health) [today.com] 09/11/2026, 02:24 PM, +0000 UTC — Walmart Great Value Berries Recalled for Possible E. Coli Contamination. See the Full List
    
    Link: https://www.today.com/health/recall/walmart-berry-recall-great-value-e-coli-rcna597212
  - (FDA recall health) [EatingWell] 09/14/2026, 07:29 PM, +0000 UTC — The FDA Warns This Common Cookware May Leach Lead—Here’s What’s Safe to Use Instead
    
    Link: https://www.eatingwell.com/fda-lead-leaching-cookware-replacements-amazon-12114030
  - (FDA recall health) [The Hill] 09/09/2026, 05:50 PM, +0000 UTC — Supplements for dogs recalled over salmonella risks
    
    Link: https://thehill.com/policy/healthcare/6079358-dog-supplements-recalled-salmonella/?email=467cb6399cb7df64551775e431052b43a775c749&emaila=12a6d4d069cd56cfddaa391c24eb7042&emailb=054528e7403871c79f668e49dd3c44b1ec00c7f611bf9388f76bb2324d6ca5f3&utm_source=Sailthru&utm_medium=email&utm_campaign=09.09.26%20Health%20Care%20JC
  - (FDA recall health) [MedShadow Foundation] 09/14/2026, 07:21 PM, +0000 UTC — FDA Recalls and Warnings: Zicam Nasal Swabs Recalled, Foreign Pills Found in Trazodone Bottles
    
    Link: https://medshadow.org/drug-updates-recalls/fda-recalls-and-warnings/zicam-recall-foreign-pills-found-in-trazodone-bottles/
  - (FDA recall health) [News4JAX] 09/15/2026, 05:14 PM, +0000 UTC — FDA recalls six hand soap products over bacterial contamination risk
    
    Link: https://www.news4jax.com/news/2026/09/15/fda-recalls-six-hand-soap-products-over-bacterial-contamination-risk/
  - (FDA recall health) [health.com] 09/16/2026, 03:09 PM, +0000 UTC — FDA Announces Hand Soap Recall in 15 States—Thousands of Bottles May Contain Bacteria
    
    Link: https://www.health.com/hand-soap-recall-september-2026-12123997
  - (FDA recall health) [insights.citeline.com] 09/16/2026, 05:03 AM, +0000 UTC — US FDA Warning To Bausch + Lomb Suggests Potential For Recall, Production Interruption
    
    Link: https://insights.citeline.com/hbw-insight/health/policy-and-regulation/recalls/us-fda-warning-to-bausch-lomb-suggests-potential-for-recall-production-interruption-GQSU2KCNLFCYDEJKGYSSRBIX6M/
  - (FDA recall health) [thehealthy.com] 09/14/2026, 06:06 PM, +0000 UTC — Hand Soaps Recalled in 15 States for Bacterial Contamination Risk
    
    Link: https://www.thehealthy.com/news/hand-soap-recall-september-2026/