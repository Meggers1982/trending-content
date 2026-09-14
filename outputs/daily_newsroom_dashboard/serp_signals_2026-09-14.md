# LIVE SIGNAL DATA — SerpAPI Pre-Fetch
The following signals were fetched from SerpAPI Google News and SerpAPI Google Trends immediately before this pipeline run. Treat Google Trends as AVAILABLE when this section contains a Google Trends block. Use it as the primary search_velocity input for Skills 01–05 (Signal Listener through Trend Strength Scorer). Use the Google News Radar as the broad discovery layer for news-led health topics, including topics that do not yet appear in Google Trends. Prioritize topics with convergence across News, Trends, primary/institutional sources, and credible publisher coverage.

## Google Trends — Trending Now (US / Health, real-time)
Terms with a "Why:" line have a confirmed real-world news story driving the spike; terms without one are a real-time signal only, not yet grounded in a specific story.
  - measles outbreak pennsylvania
    Why: "Unvaccinated Woman Likely Died of Measles Complications, Pa. County Coroner Says" — The New York Times
  - autopsy
    Why: "A Teen Autopsy Marks the Arrival of a Deadly Drug in San Francisco" — The New York Times

## Google Trends — 7-Day Interest (US)
  - **health**: latest=93, peak=100, 7d-delta=+50
    Rising related: barry melrose health, videra health, brett favre health, sutter health park, devoted health careers, emma navarro health issues, joe biden health, mental health
  - **wellness**: latest=74, peak=100, 7d-delta=+24
    Rising related: wellness darties, wizard wellness nasal spray, wizard wellness, connective wellness, little luxe wellness lodge, civana wellness resort and spa, blackwood wellness dispensary, holistic-hyperbarics.com unlocking ancient remedies for modern wellness
  - **nutrition**: latest=88, peak=100, 7d-delta=+3
    Rising related: optimum nutrition beer, optimum nutrition protein beer, nutrition facts, what is nutrition, nutrition label, nutrition calculator, nutrition near me, egg nutrition
  - **fitness**: latest=33, peak=100, 7d-delta=-35
    Rising related: pentagon military fitness standards, jill brown fitness, carrie sisson fitness advice aging, new army fitness test, helena christensen fitness routine strength training, army fitness test, fitness studio near me, jason walsh celebrity fitness advice
  - **food safety**: latest=74, peak=100, 7d-delta=+29
    Rising related: usda, ias brand safety, food safety jobs near me, food safety definition, food safety compliance, what does fattom stand for in food safety, food safety inspector, what is food safety
  - **diet**: latest=94, peak=100, 7d-delta=+3
    Rising related: dr. james stone egg diet, diet coke, mediterranean diet, keto diet, science diet, liquid diet, carnivore diet, fodmap diet
  - **weight loss**: latest=31, peak=100, 7d-delta=-4
    Rising related: amy slaton weight loss update, chrissy metz weight loss, bronson reed weight loss, kelly osbourne weight loss, lizzo weight loss, glp 1, embody, medvi
  - **mental health**: latest=93, peak=100, 7d-delta=+45
    Rising related: mental health women villakalima, elizabeth holmes mental health diagnosis, elizabeth holmes mental health, which part of your brain is involved in your motivation?, orange county mental health, mental health of jesus, mental health specialist, charlie health
  - **gut health**: latest=29, peak=100, 7d-delta=-8
    Rising related: ryze mushroom coffee reviews, h pylori symptoms, symptoms of bad gut health, ryze mushroom coffee, ryze coffee, best probiotic drink for gut health, l-glutamine for gut health, l-glutamine

Top rising related queries from Google Trends:
  - barry melrose health
  - videra health
  - brett favre health
  - sutter health park
  - devoted health careers
  - emma navarro health issues
  - joe biden health
  - mental health
  - wellness darties
  - wizard wellness nasal spray
  - wizard wellness
  - connective wellness
  - little luxe wellness lodge
  - civana wellness resort and spa
  - blackwood wellness dispensary
  - holistic-hyperbarics.com unlocking ancient remedies for modern wellness
  - optimum nutrition beer
  - optimum nutrition protein beer
  - nutrition facts
  - what is nutrition

## Google News Radar — Recent Health Topics (144 unique across 12 queries; showing 60)
Treat these headlines as the broad radar of news-led health topics. The Signal Listener must consider this radar before narrowing to retained candidates.
  - (health) [Apple] 09/09/2026, 05:55 PM, +0000 UTC — Apple advances health and fitness capabilities using Apple Intelligence
    
    Link: https://www.apple.com/newsroom/2026/09/apple-advances-health-and-fitness-capabilities-using-apple-intelligence/
  - (health) [HHS.gov] 09/08/2026, 06:03 PM, +0000 UTC — HHS Awards More Than $380 Million to Strengthen America’s Behavioral Health System on 988 Day
    
    Link: https://www.hhs.gov/press-room/hhs-awards-380-million-988-suicide-prevention-behavioral-health.html
  - (health) [Centers for Disease Control and Prevention | CDC (.gov)] 09/10/2026, 09:15 PM, +0000 UTC — Nationwide Increase in Reported Human Rabies Exposures: Rabies Post-exposure Prophylaxis Administration
    
    Link: https://www.cdc.gov/han/php/notices/han00533.html
  - (health) [NPR] 09/13/2026, 02:00 PM, +0000 UTC — Actor Tatyana Ali is advocating for Black and Indigenous maternal health
    
    Link: https://www.npr.org/2026/09/13/nx-s1-5966885/birth-black-and-indigenous-maternal-health
  - (health) [Maryland Matters] 09/09/2026, 09:03 AM, +0000 UTC — Luminis cybersecurity incident highlights ‘concerning’ rise in attacks on healthcare
    
    Link: https://marylandmatters.org/2026/09/09/luminis-cybersecurity-incident-highlights-concerning-rise-in-attacks-on-healthcare/
  - (health) [MPR News] 09/09/2026, 04:11 PM, +0000 UTC — Allina Health doctors file 10-day strike notice
    
    Link: https://www.mprnews.org/story/2026/09/09/allina-health-doctors-file-10day-strike-notice
  - (health) [Nature] 09/12/2026, 03:34 PM, +0000 UTC — Young minds in distress: Exploring the global rise in youth mental health diagnoses
    
    Link: https://www.nature.com/articles/s41380-026-03884-x
  - (health) [Time Magazine] 09/08/2026, 12:00 PM, +0000 UTC — More Americans Are Losing Health Insurance—And Everyone Will Pay
    
    Link: https://time.com/article/2026/09/08/losing-health-insurance-affects-everyone/
  - (health) [Aeon] 09/10/2026, 10:04 AM, +0000 UTC — The curio cabinet of medieval mental health
    
    Link: https://aeon.co/essays/the-curio-cabinet-of-medieval-mental-health
  - (health) [World Health Organization (WHO)] 09/09/2026, 01:13 PM, +0000 UTC — Dr Vanessa Kerry appointed to new role as WHO Director-General's Special Envoy for Health Resilience
    
    Link: https://www.who.int/news/item/09-09-2026-dr-vanessa-kerry-appointed-to-new-role-as-who-director-general-s-special-envoy-for-health-resilience
  - (health) [ClickOnDetroit | WDIV Local 4] 09/08/2026, 12:36 PM, +0000 UTC — Trinity Health to cut over 500 jobs in Livonia
    
    Link: https://www.clickondetroit.com/news/local/2026/09/08/trinity-health-to-cut-over-500-jobs-in-livonia/
  - (health) [Healthcare Dive] 09/11/2026, 03:15 PM, +0000 UTC — Health spending tied to rise in premiums, new study finds
    
    Link: https://www.healthcaredive.com/news/health-spending-tied-to-rise-premiums-new-study-finds-jama/830144/
  - (wellness) [The New York Times] 09/14/2026, 02:15 AM, +0000 UTC — Trading Keggers for ‘Wellness Darties’
    
    Link: https://www.nytimes.com/2026/09/11/style/wellness-darties-college-gen-z-tiktok.html
  - (wellness) [Montgomery County, MD (.gov)] 09/11/2026, 08:00 AM, +0000 UTC — Montgomery County to Host a Free Health and Wellness Fair on Saturday, Sept. 19 in White Oak
    
    Link: https://www.montgomerycountymd.gov/news/montgomery-county-host-free-health-wellness-fair-saturday-sept-19-white-oak
  - (wellness) [Holland & Knight] 09/11/2026, 09:36 PM, +0000 UTC — Wellness Check: Analyzing Regulatory Risk Facing Innovative Health Platforms
    
    Link: https://www.hklaw.com/en/insights/publications/2026/09/wellness-check-analyzing-regulatory-risk-facing
  - (wellness) [KUOW] 09/09/2026, 07:56 PM, +0000 UTC — Seattle police officers alarmed that new 'wellness' supervisor failed to report sexual abuse in his family
    
    Link: https://www.kuow.org/law/2026-09-09/seattle-police-officers-alarmed-that-new-wellness-supervisor-failed-to-report-sexual-abuse-in-his-family
  - (wellness) [Ogletree] 09/09/2026, 01:08 PM, +0000 UTC — Federal Agencies Clarify Rules for Rewards in Employer-Sponsored Wellness Programs
    
    Link: https://ogletree.com/insights-resources/blog-posts/federal-agencies-clarify-rules-for-rewards-in-employer-sponsored-wellness-programs/
  - (wellness) [businessoffashion.com] 09/08/2026, 12:07 PM, +0000 UTC — Dior Pushes ‘Haute Wellness’ Strategy
    
    Link: https://www.businessoffashion.com/articles/beauty/dior-beauty-wellness-strategy/
  - (wellness) [DVIDS] 09/11/2026, 08:54 PM, +0000 UTC — News - DCMA leadership prioritizes workforce wellness year-round
    
    Link: https://www.dvidshub.net/news/574494/dcma-leadership-prioritizes-workforce-wellness-year-round
  - (wellness) [CSUSM NewsCenter] 09/10/2026, 07:19 PM, +0000 UTC — Grant to Help CSUSM Expand Mobile Wellness Initiative's Reach
    
    Link: https://news.csusm.edu/grant-to-help-csusm-expand-mobile-wellness-initiatives-reach/
  - (wellness) [NBC News] 09/09/2026, 11:44 PM, +0000 UTC — College kids attend ‘Wellness Darties’ as Gen-Z looks for more sober events
    
    Link: https://www.nbcnews.com/video/college-kids-swap-kegs-for-kettle-bells-with-new-healthy-party-trend-269589061508
  - (wellness) [Cobb County School District] 09/10/2026, 07:00 AM, +0000 UTC — Dodgen Earns National Recognition for Student Health and Wellness
    
    Link: https://www.cobbk12.org/dodgen/dodgen-earns-national-recognition-for-student-health-and-wellness.137192
  - (wellness) [Business Insider] 09/10/2026, 09:11 AM, +0000 UTC — I was laid off from Amazon. After struggling to relax as a working mom, I went all in on my wellness side hustle.
    
    Link: https://www.businessinsider.com/laid-off-amazon-worker-relax-wellness-travel-business-side-hustle-2026-9
  - (wellness) [independent.com] 09/09/2026, 06:54 PM, +0000 UTC — Santa Barbara County Behavioral Wellness Celebrates National Recovery Month
    
    Link: https://www.independent.com/2026/09/09/santa-barbara-county-behavioral-wellness-celebrates-national-recovery-month/
  - (medical study) [Insilico Medicine] 09/10/2026, 07:31 AM, +0000 UTC — Insilico Medicine Doses First Patient in GENESIS-IPF-3, the World’s First Phase III Trial of a Generative AI-Driven Innovative Drug
    
    Link: https://insilico.com/news/isn1009261-insilico-medicine-doses-first-patient-genesis-ipf-3
  - (medical study) [American Medical Association | AMA] 09/14/2026, 12:06 PM, +0000 UTC — Why some medical student research gets published—and some doesn’t
    
    Link: https://www.ama-assn.org/medical-students/succeed-medical-school/why-some-medical-student-research-gets-published-and-some
  - (medical study) [Yahoo Finance] 09/14/2026, 10:30 AM, +0000 UTC — Multi4 Medical Publishes Landmark Clinical Study in Prestigious BJUI - Initiates First Patient Treatments in Europe
    
    Link: https://finance.yahoo.com/healthcare/articles/multi4-medical-publishes-landmark-clinical-103000042.html
  - (medical study) [Nature] 09/14/2026, 10:27 AM, +0000 UTC — Prospective evidence for conversational medical AI is hard, but non-negotiable
    
    Link: https://www.nature.com/articles/s41591-026-04639-5
  - (medical study) [University of Colorado Anschutz] 09/11/2026, 05:19 AM, +0000 UTC — There Aren’t Enough Clinical Trials on Suicide Prevention. A New Analysis Asks Why.
    
    Link: https://news.cuanschutz.edu/emergency-medicine/stanley-suicide-prevention-study
  - (medical study) [med.stanford.edu] 09/09/2026, 01:21 PM, +0000 UTC — Emmanuel Mignot receives Lasker Award for discovering cause of narcolepsy
    
    Link: https://med.stanford.edu/news/all-news/2026/09/mignot-lasker.html
  - (medical study) [University of South Carolina] 09/09/2026, 07:00 AM, +0000 UTC — Floyd School of Medicine Professor Awarded Funding for Lung Injury Research
    
    Link: https://www.sc.edu/study/colleges_schools/medicine/about_the_school/news/2026/evans_nih_grant.php
  - (medical study) [Augusta University] 09/10/2026, 05:05 PM, +0000 UTC — New study classifies atherosclerosis as an autoimmune disease
    
    Link: https://jagwire.augusta.edu/new-study-classifies-atherosclerosis-as-an-autoimmune-disease/
  - (medical study) [news-medical.net] 09/09/2026, 05:33 PM, +0000 UTC — New study evaluates medical and surgical treatments for mitral regurgitation
    
    Link: https://www.news-medical.net/news/20260909/New-study-evaluates-medical-and-surgical-treatments-for-mitral-regurgitation.aspx
  - (medical study) [National Association of Manufacturers - NAM] 09/09/2026, 08:58 PM, +0000 UTC — Protolabs to Support MIT Research on Defense, Medical Innovation Scaling
    
    Link: https://nam.org/protolabs-to-support-mit-research-on-defense-medical-innovation-scaling/
  - (medical study) [The Harvard Crimson] 09/11/2026, 12:00 PM, +0000 UTC — Harvard and Yale Researchers Awarded $46 Million to Study Autism’s Origin in the Brain
    
    Link: https://www.thecrimson.com/article/2026/9/11/autism-origins-hms-grant/
  - (medical study) [UVA Health] 09/09/2026, 08:15 PM, +0000 UTC — Trial Testing Out-of-Body Experiences Yields Unexpected Twist
    
    Link: https://www.uvahealth.com/news/trial-testing-out-of-body-experiences-yields-unexpected-twist
  - (clinical trial health) [Rethinking Clinical Trials] 09/09/2026, 08:00 AM, +0000 UTC — September 9, 2026: Embedded Trials in a Learning Health System, in This Week's Rethinking Clinical Trials Grand Rounds
    
    Link: https://rethinkingclinicaltrials.org/news/september-9-2026-embedded-trials-in-a-learning-health-system-in-this-weeks-rethinking-clinical-trials-grand-rounds/
  - (clinical trial health) [Applied Clinical Trials Online] 09/10/2026, 06:57 PM, +0000 UTC — Recruitment in the Age of AI: Q&A with John Worden, Javara
    
    Link: https://www.appliedclinicaltrialsonline.com/view/recruitment-age-ai-john-worden-javara
  - (clinical trial health) [The Atlantic] 09/10/2026, 06:45 AM, +0000 UTC — Humanizing the Clinical Trial Experience Through Patient Engagement - Sponsor Content - Lilly
    
    Link: https://www.theatlantic.com/sponsored/lilly-2026/humanizing-clinical-trial/4131/
  - (clinical trial health) [WashU Medicine] 09/09/2026, 03:04 PM, +0000 UTC — Mental health care before, after surgery improves recovery in older adults
    
    Link: https://medicine.washu.edu/news/mental-health-care-before-after-surgery-improves-recovery-in-older-adults/
  - (clinical trial health) [Penn State Health News] 09/08/2026, 03:03 PM, +0000 UTC — NIH awards Penn State CTSI $28.2M to improve rural health
    
    Link: https://pennstatehealthnews.org/2026/09/nih-awards-penn-state-ctsi-28-2m-to-improve-rural-health/
  - (clinical trial health) [respiratory-therapy.com] 09/10/2026, 05:57 PM, +0000 UTC — ALA Expands Lung Cancer Clinical Trial Awareness
    
    Link: https://respiratory-therapy.com/disorders-diseases/cardiopulmonary-thoracic/lung-cancer/ala-expands-lung-cancer-clinical-trial-awareness/
  - (clinical trial health) [The Clinical Trial Vanguard] 09/08/2026, 07:39 AM, +0000 UTC — The Algorithm Passed Every Benchmark. The Patients Didn’t Notice.
    
    Link: https://www.clinicaltrialvanguard.com/article/article-deep-dive/the-algorithm-passed-every-benchmark-the-patients-didnt-notice/
  - (clinical trial health) [PR Newswire] 09/14/2026, 12:34 PM, +0000 UTC — Four Years After Disrupting Clinical Trial Diversity at DPHARM, Acclinate Is Back to Disrupt the Data Behind It
    
    Link: https://www.prnewswire.com/news-releases/four-years-after-disrupting-clinical-trial-diversity-at-dpharm-acclinate-is-back-to-disrupt-the-data-behind-it-302876824.html
  - (clinical trial health) [Precedence Research] 09/09/2026, 07:00 AM, +0000 UTC — Clinical Trials Market Companies, Size & Trends 2026-2035
    
    Link: https://www.precedenceresearch.com/clinical-trials-market
  - (clinical trial health) [DVIDS] 09/08/2026, 01:04 PM, +0000 UTC — Volunteers Wanted: NMRC Clinical Trials Center Prepares for Phase 2 Trial of Respiratory Illness Treatment
    
    Link: https://www.dvidshub.net/news/574064/volunteers-wanted-nmrc-clinical-trials-center-prepares-phase-2-trial-respiratory-illness-treatment
  - (clinical trial health) [Yahoo Finance] 09/10/2026, 12:45 PM, +0000 UTC — Optimi Health to Initiate Phase 2 Clinical Trial Evaluating Psilocybin-Assisted Therapy for Major Depressive Disorder
    
    Link: https://finance.yahoo.com/healthcare/articles/optimi-health-initiate-phase-2-124500744.html
  - (clinical trial health) [Psychiatric Times] 09/10/2026, 09:10 PM, +0000 UTC — New Phase 2 Clinical Trial Initiating in 2027: Evaluating Psilocybin-Assisted Therapy for Major Depressive Disorder
    
    Link: https://www.psychiatrictimes.com/view/new-phase-2-clinical-trial-initiating-in-2027-evaluating-psilocybin-assisted-therapy-for-major-depressive-disorder
  - (FDA recall health) [fda.gov] 09/09/2026, 04:30 PM, +0000 UTC — Outbreak Investigation of Salmonella: Sprouts (September 2026)
    
    Link: https://www.fda.gov/food/outbreaks-foodborne-illness/outbreak-investigation-salmonella-sprouts-september-2026
  - (FDA recall health) [NewsNation] 09/10/2026, 08:38 PM, +0000 UTC — Epinephrine injection recalled over potentially fatal health risks: FDA
    
    Link: https://www.newsnationnow.com/us-news/recalls/epinephrine-injection-recalled-health-risks-fda/
  - (FDA recall health) [American Hospital Association] 09/08/2026, 08:41 PM, +0000 UTC — FDA issues highest recall for certain breathing circuits, catheters, spinal cord stimulators
    
    Link: https://www.aha.org/news/headline/2026-09-08-fda-issues-highest-recall-certain-breathing-circuits-catheters-spinal-cord-stimulators
  - (FDA recall health) [The Healthy @Reader's Digest] 09/09/2026, 07:00 AM, +0000 UTC — Seasoning Recall Gets Highest FDA Risk Level, 5 Items Pulled
    
    Link: https://www.thehealthy.com/news/seasoning-recall-texas-highest-fda-risk-level/
  - (FDA recall health) [pbs.org] 09/09/2026, 09:26 PM, +0000 UTC — Cyclospora outbreak followed years of declining FDA foreign inspections
    
    Link: https://www.pbs.org/newshour/health/cyclospora-outbreak-followed-years-of-declining-fda-foreign-inspections
  - (FDA recall health) [MedShadow Foundation] 09/08/2026, 07:31 PM, +0000 UTC — FDA Recalls and Warnings: Erectile Dysfunction Drug Ingredients Recalled Over Serious Quality Control Concerns
    
    Link: https://medshadow.org/drug-updates-recalls/fda-recalls-and-warnings/sildenafil-tadalafil-erectile-dysfunction-ingredient-recall/
  - (FDA recall health) [TODAY.com] 09/11/2026, 02:24 PM, +0000 UTC — Walmart Great Value Berries Recalled for Possible E. Coli Contamination. See the Full List
    
    Link: https://www.today.com/health/recall/walmart-berry-recall-great-value-e-coli-rcna597212
  - (FDA recall health) [thehill.com] 09/09/2026, 05:50 PM, +0000 UTC — Supplements for dogs recalled over salmonella risks
    
    Link: https://thehill.com/policy/healthcare/6079358-dog-supplements-recalled-salmonella/?email=467cb6399cb7df64551775e431052b43a775c749&emaila=12a6d4d069cd56cfddaa391c24eb7042&emailb=054528e7403871c79f668e49dd3c44b1ec00c7f611bf9388f76bb2324d6ca5f3&utm_source=Sailthru&utm_medium=email&utm_campaign=09.09.26%20Health%20Care%20JC
  - (FDA recall health) [Everyday Health] 09/08/2026, 07:00 AM, +0000 UTC — White Rice Recalled in 13 States Due to ‘Foreign Material’
    
    Link: https://www.everydayhealth.com/diet-nutrition/white-rice-recalled-states-due-to-foreign-material/
  - (FDA recall health) [Newsweek] 09/09/2026, 10:46 AM, +0000 UTC — Cream Cheese and Deli Salads Recalled After Listeria Detected by FDA
    
    Link: https://www.newsweek.com/cream-cheese-recall-fda-listeria-concerns-12419494
  - (FDA recall health) [cdc.gov] 09/11/2026, 07:00 AM, +0000 UTC — E. coli Outbreak Linked to Frozen Blueberries
    
    Link: https://www.cdc.gov/ecoli/outbreaks/blueberries-07-26/index.html
  - (FDA recall health) [KSNT 27 News] 09/08/2026, 07:55 PM, +0000 UTC — Supplements for dogs recalled over salmonella risks: FDA
    
    Link: https://www.ksnt.com/news/kansas/supplements-for-dogs-recalled-over-salmonella-risks-fda/