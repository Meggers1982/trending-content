# LIVE SIGNAL DATA — SerpAPI Pre-Fetch
The following signals were fetched from SerpAPI Google News and SerpAPI Google Trends immediately before this pipeline run. Treat Google Trends as AVAILABLE when this section contains a Google Trends block. Use it as the primary search_velocity input for Skills 01–05 (Signal Listener through Trend Strength Scorer). Use the Google News Radar as the broad discovery layer for news-led health topics, including topics that do not yet appear in Google Trends. Prioritize topics with convergence across News, Trends, primary/institutional sources, and credible publisher coverage.

## Google Trends — Trending Now (US / Health, real-time)
Terms with a "Why:" line have a confirmed real-world news story driving the spike; terms without one are a real-time signal only, not yet grounded in a specific story.
  - xylitol artificial sweetener
    Why: "Sweetener used in chewing gum and jam linked to strokes and heart attacks" — The Guardian

## Google Trends — 7-Day Interest (US)
  - **health**: latest=19, peak=100, 7d-delta=+0
    Rising related: dolly parton health update, dolly parton death, tim curry health, dolly parton health, dolly parton health issues, what health issues did dolly parton have?, what health issues did dolly parton have, dolly parton sad news
  - **wellness**: latest=51, peak=100, 7d-delta=-4
    Rising related: patagonia black hole duffel 100l tidal tea, shrek 5, 772-563-4880, civana wellness resort & spa, dimensions of wellness, 8 dimensions of wellness, wellness center, health and wellness
  - **nutrition**: latest=80, peak=100, 7d-delta=+0
    Rising related: cooked versus raw vegetables nutrition, usda watermelon rind nutrition data, chick fil a chicken and waffles nutrition, starbucks nutrition calculator, 100% whey gold standard optimum nutrition, optimum nutrition serious mass, pet nutrition calculator, starbucks nutrition
  - **fitness**: latest=77, peak=100, 7d-delta=-7
    Rising related: harley pasternak fitness advice, world fitness project leaderboard, world fitness project, cnn underscored fitness tracker review, hiking, ai insights dualmedia, fitness focus, holiday fitness
  - **food safety**: latest=13, peak=100, 7d-delta=-2
    Rising related: aluminum foil food storage safety, uc riverside dollar store study, walmart product recalls safety notice, permanent daylight saving time winter sunsets, fromm dog food metal recall, aldi game day snack container, costa rica orange peel ecosystem restoration, raley's grocery store closures
  - **diet**: latest=79, peak=100, 7d-delta=-1
    Rising related: new cholesterol guidelines diet role, washu medicine keto mediterranean diet study, rose ferguson diet and lifestyle overhaul, dolly parton diet, christie brinkley vegan diet, billy bob thornton diet, diet coke, mediterranean diet
  - **weight loss**: latest=43, peak=100, 7d-delta=-1
    Rising related: tiffany franco 110 pound weight loss, medvi quad reviews, medvi quad, medvi.org, joinem reviews, medvi tirzepatide cost, medvi reviews, medvi health
  - **mental health**: latest=42, peak=100, 7d-delta=+1
    Rising related: kyle singler mental health, yayoi kusama mental health, this type of sex benefits your physical and mental health the most, smi mental health, how does social media affect mental health, lindsay clancy mental health history, why is mental health important, define mental health
  - **gut health**: latest=67, peak=100, 7d-delta=+1
    Rising related: onnit total gut health review, who used acupuncture to relieve pain and congestion, earliest people known to maintain accurate health records, gastroenterologist, best time to eat sauerkraut for gut health, seneca, is farting a sign of good gut health, who began public health and sanitation systems

Top rising related queries from Google Trends:
  - dolly parton health update
  - dolly parton death
  - tim curry health
  - dolly parton health
  - dolly parton health issues
  - what health issues did dolly parton have?
  - what health issues did dolly parton have
  - dolly parton sad news
  - patagonia black hole duffel 100l tidal tea
  - shrek 5
  - 772-563-4880
  - civana wellness resort & spa
  - dimensions of wellness
  - 8 dimensions of wellness
  - wellness center
  - health and wellness
  - cooked versus raw vegetables nutrition
  - usda watermelon rind nutrition data
  - chick fil a chicken and waffles nutrition
  - starbucks nutrition calculator

## Google News Radar — Recent Health Topics (144 unique across 12 queries; showing 60)
Treat these headlines as the broad radar of news-led health topics. The Signal Listener must consider this radar before narrowing to retained candidates.
  - (health) [Arkansas Governor (.gov)] 08/27/2026, 07:06 PM, +0000 UTC — Sanders Announces Nearly $150 Million Awarded in Rural Health Transformation Funds
    
    Link: https://governor.arkansas.gov/news_post/sanders-announces-nearly-150-million-awarded-in-rural-health-transformation-funds/
  - (health) [Centers for Disease Control and Prevention | CDC (.gov)] 08/25/2026, 07:00 AM, +0000 UTC — Regional Centers for Public Health Preparedness and Response | Office of Readiness and Response
    
    Link: https://www.cdc.gov/orr/budget-funding/regional-centers.html
  - (health) [Iowa Capital Dispatch] 08/25/2026, 10:01 PM, +0000 UTC — Class-action lawsuit claims UnityPoint Health shortchanged hourly workers
    
    Link: https://iowacapitaldispatch.com/2026/08/25/class-action-lawsuit-claims-unitypoint-health-shortchanged-hourly-workers/
  - (health) [Maryland.gov] 08/24/2026, 07:13 PM, +0000 UTC — Pages - Maryland Department of Health declares measles outbreak in three Maryland counties
    
    Link: https://health.maryland.gov/newsroom/Pages/Maryland%20Department%20of%20Health%20declares%20measles%20outbreak%20in%20three%20Maryland%20counties.aspx
  - (health) [World Health Organization (WHO)] 08/28/2026, 07:00 AM, +0000 UTC — Suicide
    
    Link: https://www.who.int/news-room/fact-sheets/detail/suicide
  - (health) [Raiders.com] 08/24/2026, 05:02 PM, +0000 UTC — Las Vegas Raiders announce $25 million game-changing gift to Intermountain Health to help build Nevada's first stand-alone children's hospital
    
    Link: https://www.raiders.com/news/las-vegas-raiders-announce-25-million-game-changing-gift-to-intermountain-health-to-help-build-nevada-s-first-stand-alone-children-s-hospital
  - (health) [NASA (.gov)] 08/24/2026, 07:00 AM, +0000 UTC — Request for Information: Help Shape Human Health Research for the Future Moon Base
    
    Link: https://www.nasa.gov/hrp/request-for-information-help-shape-human-health-research-for-the-future-moon-base/
  - (health) [Alabama Governor's Office (.gov)] 08/24/2026, 03:01 PM, +0000 UTC — Governor Ivey Announces First Grants in Major New Rural Healthcare Program Totaling More than $144 Million
    
    Link: https://governor.alabama.gov/newsroom/2026/08/governor-ivey-announces-first-grants-in-major-new-rural-healthcare-program-totaling-more-than-144-million/
  - (health) [aphis.usda.gov] 08/24/2026, 07:00 AM, +0000 UTC — Screwworm.gov | Animal and Plant Health Inspection Service
    
    Link: https://www.aphis.usda.gov/animals/animal-health/livestock-and-poultry-disease/stop-screwworm
  - (health) [California State Portal | CA.gov] 08/27/2026, 04:14 PM, +0000 UTC — First Partner Siebel Newsom launches California’s first Social Health Council to strengthen community connection
    
    Link: https://www.gov.ca.gov/2026/08/27/first-partner-siebel-newsom-launches-californias-first-social-health-council-to-strengthen-community-connection/
  - (health) [The New York Times] 08/26/2026, 11:35 PM, +0000 UTC — Will Meta’s Changes Benefit Young Users’ Mental Health?
    
    Link: https://www.nytimes.com/2026/08/26/well/family/meta-settlement-youth-mental-health.html
  - (health) [Healthcare Dive] 08/26/2026, 04:07 PM, +0000 UTC — Employers face ‘existential reckoning’ as health costs surge
    
    Link: https://www.healthcaredive.com/news/employers-2027-health-costs-bgh-survey/828734/
  - (wellness) [Yahoo Creators] 08/29/2026, 10:39 AM, +0000 UTC — Wellness stacking: why psychologists say it beats willpower for building healthy habits
    
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
  - (wellness) [Miami University RedHawks] 08/28/2026, 06:25 PM, +0000 UTC — Human Performance and Wellness Promotes Czabala, Welcomes Artus
    
    Link: https://miamiredhawks.com/news/2026/8/28/general-human-performance-and-wellness-promotes-czabala-welcomes-artus
  - (wellness) [American Medical Association | AMA] 08/26/2026, 12:06 PM, +0000 UTC — It’s time to rethink how wellness apps, devices are regulated
    
    Link: https://www.ama-assn.org/practice-management/digital-health/it-s-time-rethink-how-wellness-apps-devices-are-regulated
  - (wellness) [PR Newswire] 08/28/2026, 06:00 PM, +0000 UTC — National Release: Kroger Is Improving Wellness in Neighborhoods Across America
    
    Link: https://www.prnewswire.com/news-releases/national-release-kroger-is-improving-wellness-in-neighborhoods-across-america-302862767.html
  - (wellness) [CSUF News] 08/28/2026, 05:00 PM, +0000 UTC — Total Wellness to Host 2026 Health and Wellness Expo
    
    Link: https://news.fullerton.edu/spotlight/total-wellness-to-host-2026-health-and-wellness-expo/
  - (wellness) [Middlesex Borough (.gov)] 08/28/2026, 04:48 PM, +0000 UTC — Senior Wellness Event
    
    Link: https://www.middlesexboro-nj.gov/latest-news/senior-wellness-event
  - (wellness) [UTHSC News] 08/28/2026, 02:40 PM, +0000 UTC — Wellness at UT Health Sciences Finds Its Person
    
    Link: https://news.uthsc.edu/wellness-at-ut-health-sciences-finds-its-person/
  - (medical study) [KUOW] 08/26/2026, 06:38 PM, +0000 UTC — UW struggles to see medical research through as Trump administration guts funding
    
    Link: https://www.kuow.org/science/2026-08-26/uw-struggles-to-see-medical-research-through-as-trump-administration-guts-funding
  - (medical study) [New Mexico State University] 08/28/2026, 03:32 PM, +0000 UTC — NMSU, UNLV study: GLP-1s do not cause major psychiatric harm
    
    Link: https://newsroom.nmsu.edu/news/nmsu--unlv-study--glp-1s-do-not-cause-major-psychiatric-harm/s/eee6d3f8-66f0-4974-8cd9-84e547134d7d
  - (medical study) [University of Chicago News] 08/28/2026, 05:00 PM, +0000 UTC — Health care spending gap between high- and low-income Americans widens, study finds
    
    Link: https://news.uchicago.edu/story/health-care-spending-gap-between-high-and-low-income-americans-widens-study-finds
  - (medical study) [Newsroom | UCLA] 08/27/2026, 03:18 PM, +0000 UTC — American Indians and Alaska Natives in California face barriers to receiving needed healthcare, UCLA study finds
    
    Link: https://newsroom.ucla.edu/releases/american-indians-alaska-natives-california-face-barriers-healthcare
  - (medical study) [Healthcare Finance News] 08/26/2026, 03:10 PM, +0000 UTC — Eli Lilly study finds Zepbound lowers healthcare costs over time
    
    Link: https://www.healthcarefinancenews.com/news/eli-lilly-study-finds-zepbound-lowers-healthcare-costs-over-time
  - (medical study) [Nature] 08/26/2026, 09:03 AM, +0000 UTC — Recombinant shingles vaccination and the risk of cardiovascular events
    
    Link: https://www.nature.com/articles/s41591-026-04606-0
  - (medical study) [Stanford Medicine] 08/28/2026, 09:51 PM, +0000 UTC — New gene activation tool may do what CRISPR cannot: work inside the body
    
    Link: https://med.stanford.edu/news/all-news/2026/08/tigra-gene-editing-tool.html
  - (medical study) [The Washington Post] 08/29/2026, 02:18 AM, +0000 UTC — LGBTQ people struggle to get needed health care and pay for it, study finds
    
    Link: https://www.washingtonpost.com/nation/2026/08/28/gay-bisexual-trans-people-struggle-get-health-care-study-says/
  - (medical study) [Cytokinetics] 08/28/2026, 09:48 AM, +0000 UTC — Cytokinetics Announces Positive Results from ACACIA-HCM Presented in Hot Line Session at the European Society of Cardiology (ESC) Congress 2026 and Published in The New England Journal of Medicine
    
    Link: https://ir.cytokinetics.com/press-releases/press-release-details/2026/Cytokinetics-Announces-Positive-Results-from-ACACIA-HCM-Presented-in-Hot-Line-Session-at-the-European-Society-of-Cardiology-ESC-Congress-2026-and-Published-in-The-New-England-Journal-of-Medicine/default.aspx
  - (medical study) [The ASCO Post] 08/27/2026, 07:44 PM, +0000 UTC — Study Evaluates Chemotherapy-Free Quadruplet in HR-Positive, HER2-Positive Metastatic Breast Cancer
    
    Link: https://ascopost.com/news/august-2026/study-evaluates-chemotherapy-free-quadruplet-in-hr-positive-her2-positive-metastatic-breast-cancer/
  - (medical study) [WTTW News] 08/27/2026, 05:03 PM, +0000 UTC — Heat Makes Emergency Rooms Busier. Chicago-Based Study Shows Which Illness and Injuries Rise During Hot Spells
    
    Link: https://news.wttw.com/2026/08/27/heat-makes-emergency-rooms-busier-chicago-based-study-shows-which-illness-and-injuries
  - (medical study) [Medical Xpress] 08/25/2026, 09:00 AM, +0000 UTC — Loneliness rewires the brain to drive alcohol use, preclinical study finds
    
    Link: https://medicalxpress.com/news/2026-08-loneliness-rewires-brain-alcohol-preclinical.html
  - (clinical trial health) [CNN] 08/22/2026, 04:00 PM, +0000 UTC — You want to join a clinical trial. Here’s what to know about the hurdles.
    
    Link: https://www.cnn.com/2026/08/22/health/clinical-trials-what-to-know
  - (clinical trial health) [Cancer Health] 08/25/2026, 03:13 AM, +0000 UTC — Clinical Trials Matter: What Our Patients Say
    
    Link: https://www.cancerhealth.com/article/clinical-trials-matter-patients-say
  - (clinical trial health) [Tufts Now] 08/25/2026, 12:00 PM, +0000 UTC — One Center’s Oversized Impact on Drug Development and Clinical Trials
    
    Link: https://now.tufts.edu/2026/08/25/one-centers-oversized-impact-drug-development-and-clinical-trials
  - (clinical trial health) [Post Bulletin] 08/29/2026, 11:46 AM, +0000 UTC — In Southeast Minnesota, clinical trial participation plays a key role in advancing science
    
    Link: https://www.postbulletin.com/health/in-southeast-minnesota-clinical-trial-participation-plays-a-key-role-in-advancing-science
  - (clinical trial health) [NYU Langone Health] 08/25/2026, 05:13 PM, +0000 UTC — NYU Langone Health to Lead New Trial of Ketamine for Pain Relief
    
    Link: https://nyulangone.org/news/nyu-langone-health-lead-new-trial-ketamine-pain-relief
  - (clinical trial health) [Scientific American] 08/27/2026, 03:55 PM, +0000 UTC — Is the keto diet better than the Mediterranean? New clinical trial reveals health benefits
    
    Link: https://www.scientificamerican.com/article/is-the-keto-diet-better-than-the-mediterranean-new-clinical-trial-reveals-health-benefits/
  - (clinical trial health) [News-Medical] 08/29/2026, 02:54 AM, +0000 UTC — Digital technologies reshape clinical research and public health
    
    Link: https://www.news-medical.net/news/20260828/Digital-technologies-reshape-clinical-research-and-public-health.aspx
  - (clinical trial health) [Clinical Leader] 08/28/2026, 04:09 AM, +0000 UTC — The Pharmacy Benefit No One Is Managing: Clinical Research As A Care Option
    
    Link: https://www.clinicalleader.com/doc/the-pharmacy-benefit-no-one-is-managing-clinical-research-as-a-care-option-0001
  - (clinical trial health) [Chemical & Engineering News] 08/28/2026, 01:23 PM, +0000 UTC — As clinical trials surge into Australia, HHS targets US bottlenecks
    
    Link: https://cen.acs.org/pharmaceuticals/drug-development/australia-clinical-drug-trial-fda-trialblazer/104/web/2026/08
  - (clinical trial health) [OHSU News] 08/28/2026, 02:23 PM, +0000 UTC — Clinical trial tests new way to treat common inherited heart disease
    
    Link: https://news.ohsu.edu/2026/08/28/clinical-trial-tests-new-way-to-treat-common-inherited-heart-disease
  - (clinical trial health) [The Clinical Trial Vanguard] 08/29/2026, 07:27 AM, +0000 UTC — Dubai’s rWGS Scale-Up Rewrites the Diagnostic Playbook — But the Data Infrastructure Problem Stays Unsolved
    
    Link: https://www.clinicaltrialvanguard.com/article/article-deep-dive/dubais-rwgs-scale-up-rewrites-the-diagnostic-playbook-but-the-data-infrastructure-problem-stays-unsolved/
  - (clinical trial health) [Science Daily] 08/29/2026, 01:33 PM, +0000 UTC — Keto diet cut liver fat by 67% in a clinical trial
    
    Link: https://www.sciencedaily.com/releases/2026/08/260828082327.htm
  - (FDA recall health) [fda.gov] 08/24/2026, 03:07 PM, +0000 UTC — Outbreak Investigation of Shiga Toxin-producing E. coli & Salmonella: Sprouts (August 2026)
    
    Link: https://www.fda.gov/food/outbreaks-foodborne-illness/outbreak-investigation-shiga-toxin-producing-e-coli-salmonella-sprouts-august-2026
  - (FDA recall health) [The New York Times] 08/23/2026, 06:12 PM, +0000 UTC — Nearly 40,000 Eye Drop Bottles Are Recalled Over Potential Contamination
    
    Link: https://www.nytimes.com/2026/08/23/health/clear-eyes-eye-drops-fda-recall.html
  - (FDA recall health) [American Hospital Association] 08/28/2026, 09:16 PM, +0000 UTC — FDA issues recall, alerts for certain convenience kits; companies voluntarily recall certain IV fluids
    
    Link: https://www.aha.org/news/headline/2026-08-28-fda-issues-recall-alerts-certain-convenience-kits-companies-voluntarily-recall-certain-iv-fluids
  - (FDA recall health) [Centers for Disease Control and Prevention | CDC (.gov)] 08/27/2026, 07:00 AM, +0000 UTC — Cyclospora Outbreak Linked to Iceberg Lettuce | Cyclosporiasis
    
    Link: https://www.cdc.gov/cyclosporiasis/outbreaks/07-26/index.html
  - (FDA recall health) [NewsNation] 08/27/2026, 09:02 PM, +0000 UTC — FDA announces drug recalls over potential presence of fiberglass, steel
    
    Link: https://www.newsnationnow.com/us-news/recalls/fda-announces-drug-recalls-over-potential-presence-of-fiberglass-steel/
  - (FDA recall health) [USA Today] 08/28/2026, 01:41 PM, +0000 UTC — Are food recalls increasing under RFK? What the data reveals.
    
    Link: https://www.usatoday.com/story/news/health/2026/08/28/food-recalls-under-rfk-jr-data/91494801007/
  - (FDA recall health) [MedShadow Foundation] 08/25/2026, 06:21 PM, +0000 UTC — FDA Recalls and Warnings: Levothyroxine and Natural Thyroid Drugs Recalled for Potency Problems
    
    Link: https://medshadow.org/drug-updates-recalls/fda-recalls-and-warnings/subpotent-levothyroxine-sodium-tablets-superpotent-thyroid-tablets/
  - (FDA recall health) [People.com] 08/28/2026, 02:19 PM, +0000 UTC — FDA Classifies Guacamole Recall at Highest Risk Level amid Investigation into Salmonella Outbreak Linked to Jalapeño Supplier
    
    Link: https://people.com/whole-foods-guacamole-recall-gets-fda-s-highest-risk-classification-12070208
  - (FDA recall health) [Newsweek] 08/27/2026, 11:45 AM, +0000 UTC — Nut Butter Recall Update: FDA Issues Highest Risk Warning
    
    Link: https://www.newsweek.com/nut-butter-recall-update-fda-issues-highest-risk-warning-salmonella-walmart-botticelli-foods-12374520
  - (FDA recall health) [WUSA9] 08/24/2026, 01:44 PM, +0000 UTC — LIST: Here's all the food under recall in the US
    
    Link: https://www.wusa9.com/article/money/personal-finance/recalls/list-food-recalls-us-produce-frozen-pantry/65-b4eeea4a-2820-42f6-a861-64faecfbf37c
  - (FDA recall health) [Good Housekeeping] 08/26/2026, 04:56 PM, +0000 UTC — FDA Announces Recall of Thyroid Medicine Due to Potential “Super Potency”
    
    Link: https://www.goodhousekeeping.com/health/a73525167/thyroid-medication-recall/
  - (FDA recall health) [KTALnews.com] 08/27/2026, 07:47 PM, +0000 UTC — FDA recalls popular IV bags over possible fiberglass contamination
    
    Link: https://www.ktalnews.com/health/baxter-sodium-chloride-recall/