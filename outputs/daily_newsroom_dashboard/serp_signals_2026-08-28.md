# LIVE SIGNAL DATA — SerpAPI Pre-Fetch
The following signals were fetched from SerpAPI Google News and SerpAPI Google Trends immediately before this pipeline run. Treat Google Trends as AVAILABLE when this section contains a Google Trends block. Use it as the primary search_velocity input for Skills 01–05 (Signal Listener through Trend Strength Scorer). Use the Google News Radar as the broad discovery layer for news-led health topics, including topics that do not yet appear in Google Trends. Prioritize topics with convergence across News, Trends, primary/institutional sources, and credible publisher coverage.

## Google Trends — Trending Now (US / Health, real-time)
Terms with a "Why:" line have a confirmed real-world news story driving the spike; terms without one are a real-time signal only, not yet grounded in a specific story.
  - brain eating amoeba north carolina
    Why: "NC teen has rare brain infection likely caused by swimming. Where did exposure happen? Are you safe?" — WRAL

## Google Trends — 7-Day Interest (US)
  - **health**: latest=26, peak=100, 7d-delta=+3
    Rising related: dolly parton health update, dolly parton death, dolly parton health, what are the latest health updates from dolly parton and details on her new museum, tim curry health, dolly parton health issues, what health issues did dolly parton have, what health issues did dolly parton have?
  - **wellness**: latest=67, peak=100, 7d-delta=+9
    Rising related: patagonia black hole duffel 100l tidal tea, shrek 5, 772-563-4880, lithuania men's national basketball team, little luxe wellness lodge, ndsu wellness center, mashouf wellness center, activeplayhub achieve your wellness goals with expert insights on fitness
  - **nutrition**: latest=90, peak=100, 7d-delta=+7
    Rising related: cooked versus raw vegetables nutrition, usda watermelon rind nutrition data, chick fil a chicken and waffles nutrition, starbucks nutrition calculator, sp nutrition magnesium bisglycinate gummies, chick fil a nutrition, nutrition facts, nutrition calculator
  - **fitness**: latest=66, peak=100, 7d-delta=+0
    Rising related: harley pasternak fitness advice, fintechzoom .io, world fitness project, hospitals, museums, baking, vegetables, meditation
  - **food safety**: latest=18, peak=100, 7d-delta=+1
    Rising related: aluminum foil food storage safety, uc riverside dollar store study, walmart product recalls safety notice, project 2025 chapter 10, permanent daylight saving time winter sunsets, raley's grocery store closures, aldi game day snack container, fromm dog food metal recall
  - **diet**: latest=83, peak=100, 7d-delta=+4
    Rising related: new cholesterol guidelines diet role, washu medicine keto mediterranean diet study, dolly parton diet, christie brinkley vegan diet, rose ferguson diet and lifestyle overhaul, designates a diet product, billy bob thornton diet, change your diet change your mind
  - **weight loss**: latest=45, peak=100, 7d-delta=+5
    Rising related: tiffany franco 110 pound weight loss, wynonna judd weight loss, medvi quad reviews, quad medvi, medvi.org, medvi reviews, joinem reviews, medvi tirzepatide cost
  - **mental health**: latest=65, peak=100, 7d-delta=+5
    Rising related: kyle singler mental health, yayoi kusama mental health, this type of sex benefits your physical and mental health the most, how to improve mental health lwspeakcare, why is mental health important, what is mental health, mental health services, mental health counseling
  - **gut health**: latest=41, peak=100, 7d-delta=-7
    Rising related: seneca, best time to eat sauerkraut for gut health, is farting a sign of good gut health, dog gut health supplement, how to restore gut health after antibiotics, gut microbiome and mental health, ag1, dog gut health chews

Top rising related queries from Google Trends:
  - dolly parton health update
  - dolly parton death
  - dolly parton health
  - what are the latest health updates from dolly parton and details on her new museum
  - tim curry health
  - dolly parton health issues
  - what health issues did dolly parton have
  - what health issues did dolly parton have?
  - patagonia black hole duffel 100l tidal tea
  - shrek 5
  - 772-563-4880
  - lithuania men's national basketball team
  - little luxe wellness lodge
  - ndsu wellness center
  - mashouf wellness center
  - activeplayhub achieve your wellness goals with expert insights on fitness
  - cooked versus raw vegetables nutrition
  - usda watermelon rind nutrition data
  - chick fil a chicken and waffles nutrition
  - starbucks nutrition calculator

## Google News Radar — Recent Health Topics (144 unique across 12 queries; showing 60)
Treat these headlines as the broad radar of news-led health topics. The Signal Listener must consider this radar before narrowing to retained candidates.
  - (health) [Arkansas Governor (.gov)] 08/27/2026, 07:06 PM, +0000 UTC — Sanders Announces Nearly $150 Million Awarded in Rural Health Transformation Funds
    
    Link: https://governor.arkansas.gov/news_post/sanders-announces-nearly-150-million-awarded-in-rural-health-transformation-funds/
  - (health) [Iowa Capital Dispatch] 08/25/2026, 10:01 PM, +0000 UTC — Class-action lawsuit claims UnityPoint Health shortchanged hourly workers
    
    Link: https://iowacapitaldispatch.com/2026/08/25/class-action-lawsuit-claims-unitypoint-health-shortchanged-hourly-workers/
  - (health) [Maryland.gov] 08/24/2026, 07:13 PM, +0000 UTC — Pages - Maryland Department of Health declares measles outbreak in three Maryland counties
    
    Link: https://health.maryland.gov/newsroom/Pages/Maryland%20Department%20of%20Health%20declares%20measles%20outbreak%20in%20three%20Maryland%20counties.aspx
  - (health) [Alabama Governor's Office (.gov)] 08/24/2026, 03:01 PM, +0000 UTC — Governor Ivey Announces First Grants in Major New Rural Healthcare Program Totaling More than $144 Million
    
    Link: https://governor.alabama.gov/newsroom/2026/08/governor-ivey-announces-first-grants-in-major-new-rural-healthcare-program-totaling-more-than-144-million/
  - (health) [NASA (.gov)] 08/24/2026, 07:00 AM, +0000 UTC — Request for Information: Help Shape Human Health Research for the Future Moon Base
    
    Link: https://www.nasa.gov/hrp/request-for-information-help-shape-human-health-research-for-the-future-moon-base/
  - (health) [Raiders.com] 08/24/2026, 05:02 PM, +0000 UTC — Las Vegas Raiders announce $25 million game-changing gift to Intermountain Health to help build Nevada's first stand-alone children's hospital
    
    Link: https://www.raiders.com/news/las-vegas-raiders-announce-25-million-game-changing-gift-to-intermountain-health-to-help-build-nevada-s-first-stand-alone-children-s-hospital
  - (health) [aphis.usda.gov] 08/24/2026, 07:00 AM, +0000 UTC — Screwworm.gov | Animal and Plant Health Inspection Service
    
    Link: https://www.aphis.usda.gov/animals/animal-health/livestock-and-poultry-disease/stop-screwworm
  - (health) [California State Portal | CA.gov] 08/27/2026, 04:14 PM, +0000 UTC — First Partner Siebel Newsom launches California’s first Social Health Council to strengthen community connection
    
    Link: https://www.gov.ca.gov/2026/08/27/first-partner-siebel-newsom-launches-californias-first-social-health-council-to-strengthen-community-connection/
  - (health) [ClickOnDetroit | WDIV Local 4] 08/27/2026, 02:16 AM, +0000 UTC — FBI searches Quality Behavioral Health facilities in Detroit, Troy, amid federal investigation
    
    Link: https://www.clickondetroit.com/news/local/2026/08/27/fbi-searches-quality-behavioral-health-facilities-in-detroit-troy-amid-federal-investigation/
  - (health) [Axios] 08/26/2026, 02:06 PM, +0000 UTC — Scoop: Sword Health to acquire Headspace for up to $300M
    
    Link: https://www.axios.com/pro/health-tech-deals/2026/08/26/sword-health-to-acquire-headspace-300m
  - (health) [The New York Times] 08/26/2026, 11:35 PM, +0000 UTC — Will Meta’s Changes Protect Teen Mental Health on Social Media? Experts React.
    
    Link: https://www.nytimes.com/2026/08/26/well/family/meta-settlement-youth-mental-health.html
  - (health) [PBS] 08/26/2026, 10:20 PM, +0000 UTC — Maui residents face health struggles 3 years after wildfires
    
    Link: https://www.pbs.org/newshour/show/maui-residents-face-health-struggles-3-years-after-wildfires
  - (wellness) [Yahoo Creators] 08/24/2026, 01:15 PM, +0000 UTC — Wellness stacking: why psychologists say it beats willpower for building healthy habits
    
    Link: https://creators.yahoo.com/lifestyle/story/wellness-stacking-why-psychologists-say-it-beats-willpower-for-building-healthy-habits-015140677.html
  - (wellness) [WFLA] 08/23/2026, 04:18 PM, +0000 UTC — 1 dead, officer hospitalized after attempted wellness check in St. Pete: PCSO
    
    Link: https://www.wfla.com/news/pinellas-county/1-dead-officer-hospitalized-after-attempted-wellness-check-in-st-pete-pcso/
  - (wellness) [VA.gov Home | Veterans Affairs] 08/26/2026, 04:44 PM, +0000 UTC — The Freedom Garden Project: Teaming Up to Grow Veteran Wellness | VA Washington DC health care | Veterans Affairs
    
    Link: https://www.va.gov/washington-dc-health-care/stories/the-freedom-garden-project-teaming-up-to-grow-veteran-wellness/
  - (wellness) [Ground Truths | Eric Topol] 08/23/2026, 02:41 PM, +0000 UTC — Deborah Cohen: The Wellness-Industrial Complex
    
    Link: https://erictopol.substack.com/p/deborah-cohen-the-wellness-industrial
  - (wellness) [army.mil] 08/27/2026, 03:38 PM, +0000 UTC — Post ‘Defends Wellness’ at event
    
    Link: https://www.army.mil/article/294919
  - (wellness) [ELLE] 08/26/2026, 09:35 PM, +0000 UTC — The Oura Ring 5 Is the Most Stylish Wellness Device You Can Buy
    
    Link: https://www.elle.com/beauty/health-fitness/a73297148/oura-ring-5-review/
  - (wellness) [American Medical Association | AMA] 08/26/2026, 12:06 PM, +0000 UTC — It’s time to rethink how wellness apps, devices are regulated
    
    Link: https://www.ama-assn.org/practice-management/digital-health/it-s-time-rethink-how-wellness-apps-devices-are-regulated
  - (wellness) [Pratt Institute] 08/25/2026, 04:11 PM, +0000 UTC — A Centralized Hub for Student Wellness Opens on Pratt’s Brooklyn Campus
    
    Link: https://www.pratt.edu/news/a-centralized-hub-for-student-wellness-opens-on-pratts-brooklyn-campus/
  - (wellness) [CSUF News] 08/28/2026, 05:00 PM, +0000 UTC — Total Wellness to Host 2026 Health and Wellness Expo
    
    Link: https://news.fullerton.edu/spotlight/total-wellness-to-host-2026-health-and-wellness-expo/
  - (wellness) [Miami University RedHawks] 08/28/2026, 06:25 PM, +0000 UTC — Human Performance and Wellness Promotes Czabala, Welcomes Artus
    
    Link: https://miamiredhawks.com/news/2026/8/28/general-human-performance-and-wellness-promotes-czabala-welcomes-artus
  - (wellness) [UTHSC News] 08/28/2026, 02:40 PM, +0000 UTC — Wellness at UT Health Sciences Finds Its Person
    
    Link: https://news.uthsc.edu/wellness-at-ut-health-sciences-finds-its-person/
  - (wellness) [Modern War Institute -] 08/27/2026, 10:13 AM, +0000 UTC — Soldier Wellness is Unit Readiness: One Brigade’s Public-Private Prevention Experiment
    
    Link: https://mwi.westpoint.edu/soldier-wellness-is-unit-readiness-one-brigades-public-private-prevention-experiment/
  - (medical study) [KUOW] 08/26/2026, 06:38 PM, +0000 UTC — UW struggles to see medical research through as Trump administration guts funding
    
    Link: https://www.kuow.org/science/2026-08-26/uw-struggles-to-see-medical-research-through-as-trump-administration-guts-funding
  - (medical study) [New Mexico State University] 08/28/2026, 03:32 PM, +0000 UTC — NMSU, UNLV study: GLP-1s do not cause major psychiatric harm
    
    Link: https://newsroom.nmsu.edu/news/nmsu--unlv-study--glp-1s-do-not-cause-major-psychiatric-harm/s/eee6d3f8-66f0-4974-8cd9-84e547134d7d
  - (medical study) [Wolters Kluwer] 08/25/2026, 07:48 PM, +0000 UTC — Medical Research Platform | Institutional Partners
    
    Link: https://www.wolterskluwer.com/en/expert-insights/comprehensive-literature-search-multiple-databases
  - (medical study) [Newsroom | UCLA] 08/27/2026, 03:18 PM, +0000 UTC — American Indians and Alaska Natives in California face barriers to receiving needed healthcare, UCLA study finds
    
    Link: https://newsroom.ucla.edu/releases/american-indians-alaska-natives-california-face-barriers-healthcare
  - (medical study) [Nature] 08/26/2026, 11:23 AM, +0000 UTC — Patient factors in medical artificial intelligence: a systematic review
    
    Link: https://www.nature.com/articles/s44360-026-00190-2
  - (medical study) [Cytokinetics] 08/28/2026, 09:48 AM, +0000 UTC — Cytokinetics Announces Positive Results from ACACIA-HCM Presented in Hot Line Session at the European Society of Cardiology (ESC) Congress 2026 and Published in The New England Journal of Medicine
    
    Link: https://ir.cytokinetics.com/press-releases/press-release-details/2026/Cytokinetics-Announces-Positive-Results-from-ACACIA-HCM-Presented-in-Hot-Line-Session-at-the-European-Society-of-Cardiology-ESC-Congress-2026-and-Published-in-The-New-England-Journal-of-Medicine/default.aspx
  - (medical study) [PR Newswire] 08/26/2026, 10:45 AM, +0000 UTC — Zepbound linked to lower healthcare costs in adults over age 55 with obesity according to a real-world study
    
    Link: https://www.prnewswire.com/news-releases/zepbound-linked-to-lower-healthcare-costs-in-adults-over-age-55-with-obesity-according-to-a-real-world-study-302859960.html
  - (medical study) [The ASCO Post] 08/27/2026, 07:44 PM, +0000 UTC — Study Evaluates Chemotherapy-Free Quadruplet in HR-Positive, HER2-Positive Metastatic Breast Cancer
    
    Link: https://ascopost.com/news/august-2026/study-evaluates-chemotherapy-free-quadruplet-in-hr-positive-her2-positive-metastatic-breast-cancer/
  - (medical study) [University of Rochester] 08/26/2026, 06:07 PM, +0000 UTC — New Retina Model Sheds Light on Early Vision Loss in Batten Disease
    
    Link: https://www.urmc.rochester.edu/news/story/new-retina-model-sheds-light-on-early-vision-loss-in-batten-disease
  - (medical study) [Medical Xpress] 08/24/2026, 01:05 PM, +0000 UTC — Can you slow the aging process? Study reveals which interventions might help
    
    Link: https://medicalxpress.com/news/2026-08-aging-reveals-interventions.html
  - (medical study) [Healthcare Finance News] 08/26/2026, 03:10 PM, +0000 UTC — Eli Lilly study finds Zepbound lowers healthcare costs over time
    
    Link: https://www.healthcarefinancenews.com/news/eli-lilly-study-finds-zepbound-lowers-healthcare-costs-over-time
  - (medical study) [WashU Medicine] 08/27/2026, 03:02 PM, +0000 UTC — Low-carb diet delivers added liver benefits beyond weight loss
    
    Link: https://medicine.washu.edu/news/low-carb-diet-delivers-added-liver-benefits-beyond-weight-loss/
  - (clinical trial health) [CNN] 08/22/2026, 04:00 PM, +0000 UTC — You want to join a clinical trial. Here’s what to know about the hurdles.
    
    Link: https://www.cnn.com/2026/08/22/health/clinical-trials-what-to-know
  - (clinical trial health) [Cancer Health] 08/25/2026, 03:13 AM, +0000 UTC — Clinical Trials Matter: What Our Patients Say
    
    Link: https://www.cancerhealth.com/article/clinical-trials-matter-patients-say
  - (clinical trial health) [Tufts Now] 08/25/2026, 12:00 PM, +0000 UTC — One Center’s Oversized Impact on Drug Development and Clinical Trials
    
    Link: https://now.tufts.edu/2026/08/25/one-centers-oversized-impact-drug-development-and-clinical-trials
  - (clinical trial health) [NYU Langone Health] 08/25/2026, 05:13 PM, +0000 UTC — NYU Langone Health to Lead New Trial of Ketamine for Pain Relief
    
    Link: https://nyulangone.org/news/nyu-langone-health-lead-new-trial-ketamine-pain-relief
  - (clinical trial health) [Scientific American] 08/27/2026, 03:55 PM, +0000 UTC — Is the keto diet better than the Mediterranean? New clinical trial reveals health benefits
    
    Link: https://www.scientificamerican.com/article/is-the-keto-diet-better-than-the-mediterranean-new-clinical-trial-reveals-health-benefits/
  - (clinical trial health) [PR Newswire] 08/25/2026, 12:01 PM, +0000 UTC — Allegheny Health Network and The START Center for Cancer Research Announce Strategic Collaboration to Expand Patient Access to Early-Phase Cancer Trials
    
    Link: https://www.prnewswire.com/news-releases/allegheny-health-network-and-the-start-center-for-cancer-research-announce-strategic-collaboration-to-expand-patient-access-to-early-phase-cancer-trials-302858392.html
  - (clinical trial health) [Clinical Leader] 08/28/2026, 04:09 AM, +0000 UTC — The Pharmacy Benefit No One Is Managing: Clinical Research As A Care Option
    
    Link: https://www.clinicalleader.com/doc/the-pharmacy-benefit-no-one-is-managing-clinical-research-as-a-care-option-0001
  - (clinical trial health) [Chemical & Engineering News] 08/28/2026, 01:23 PM, +0000 UTC — As clinical trials surge into Australia, HHS targets US bottlenecks
    
    Link: https://cen.acs.org/pharmaceuticals/drug-development/australia-clinical-drug-trial-fda-trialblazer/104/web/2026/08
  - (clinical trial health) [The Clinical Trial Vanguard] 08/25/2026, 12:09 PM, +0000 UTC — The Oregon Dataset Is Larger Than the Entire History of Psychedelic Trials. So Why Are Regulators Still Looking the Other Way?
    
    Link: https://www.clinicaltrialvanguard.com/clinical-bellwether/the-oregon-dataset-is-larger-than-the-entire-history-of-psychedelic-trials-so-why-are-regulators-still-looking-the-other-way/
  - (clinical trial health) [News-Medical] 08/27/2026, 04:19 PM, +0000 UTC — Alliance releases new film highlighting the critical role of clinical trials
    
    Link: https://www.news-medical.net/news/20260827/Alliance-releases-new-film-highlighting-the-critical-role-of-clinical-trials.aspx
  - (clinical trial health) [MarketsandMarkets] 08/25/2026, 11:21 PM, +0000 UTC — North America Al in Clinical Trials Market (2024-2029)
    
    Link: https://www.marketsandmarkets.com/Market-Reports/geography/ai-in-clinical-trials-market/north-america
  - (clinical trial health) [Pharmaceutical Commerce] 08/25/2026, 01:09 PM, +0000 UTC — Health Care Doesn't Have a Data Problem. It Has an Activation Problem.
    
    Link: https://www.pharmaceuticalcommerce.com/view/healthcare-doesn-t-have-a-data-problem-it-has-an-activation-problem-
  - (FDA recall health) [fda.gov] 08/24/2026, 03:07 PM, +0000 UTC — Outbreak Investigation of Shiga Toxin-producing E. coli & Salmonella: Sprouts (August 2026)
    
    Link: https://www.fda.gov/food/outbreaks-foodborne-illness/outbreak-investigation-shiga-toxin-producing-e-coli-salmonella-sprouts-august-2026
  - (FDA recall health) [Axios] 08/22/2026, 10:01 AM, +0000 UTC — Here's why the FDA hit frozen blueberries with its highest risk warning
    
    Link: https://www.axios.com/2026/08/22/frozen-blueberries-recall-fda-high-risk-warning
  - (FDA recall health) [The New York Times] 08/23/2026, 06:12 PM, +0000 UTC — Nearly 40,000 Eye Drop Bottles Are Recalled Over Potential Contamination
    
    Link: https://www.nytimes.com/2026/08/23/health/clear-eyes-eye-drops-fda-recall.html
  - (FDA recall health) [NewsNation] 08/22/2026, 12:29 PM, +0000 UTC — Food recalls aren’t a success story, former FDA official says
    
    Link: https://www.newsnationnow.com/health/food-recalls-arent-success-story-former-fda-official/
  - (FDA recall health) [Good Housekeeping] 08/25/2026, 02:27 PM, +0000 UTC — FDA Announces Nationwide Recall of Popular Dog Food Due to Possible Contamination
    
    Link: https://www.goodhousekeeping.com/relationships/pets/a73520788/fromm-dog-food-recall/
  - (FDA recall health) [MedShadow Foundation] 08/25/2026, 06:21 PM, +0000 UTC — FDA Recalls and Warnings: Levothyroxine and Natural Thyroid Drugs Recalled for Potency Problems
    
    Link: https://medshadow.org/drug-updates-recalls/fda-recalls-and-warnings/subpotent-levothyroxine-sodium-tablets-superpotent-thyroid-tablets/
  - (FDA recall health) [The Guardian] 08/22/2026, 03:45 PM, +0000 UTC — 40,000 bottles of eye drops across the US recalled over issues with sterility of product
    
    Link: https://www.theguardian.com/us-news/2026/aug/22/eyedrop-recall-clear-eyes
  - (FDA recall health) [People.com] 08/28/2026, 02:19 PM, +0000 UTC — FDA Classifies Guacamole Recall at Highest Risk Level amid Investigation into Salmonella Outbreak Linked to Jalapeño Supplier
    
    Link: https://people.com/whole-foods-guacamole-recall-gets-fda-s-highest-risk-classification-12070208
  - (FDA recall health) [The Healthy @Reader's Digest] 08/28/2026, 01:42 PM, +0000 UTC — FDA: 12 Herbal Supplements Have Been Recalled
    
    Link: https://www.thehealthy.com/news/herbal-supplement-recalls-august-2026/
  - (FDA recall health) [Food Safety Magazine] 08/28/2026, 02:14 PM, +0000 UTC — FDA Explains Recall Classifications to Get Ahead of Cyclospora Outbreak Panic
    
    Link: https://www.food-safety.com/articles/11773-fda-explains-recall-classifications-to-get-ahead-of-cyclospora-outbreak-panic
  - (FDA recall health) [USA Today] 08/28/2026, 01:41 PM, +0000 UTC — Are food recalls increasing under RFK? What the data reveals.
    
    Link: https://www.usatoday.com/story/news/health/2026/08/28/food-recalls-under-rfk-jr-data/91494801007/
  - (FDA recall health) [KTALnews.com] 08/27/2026, 07:47 PM, +0000 UTC — FDA recalls popular IV bags over possible fiberglass contamination
    
    Link: https://www.ktalnews.com/health/baxter-sodium-chloride-recall/