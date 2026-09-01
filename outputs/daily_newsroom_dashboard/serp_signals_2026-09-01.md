# LIVE SIGNAL DATA — SerpAPI Pre-Fetch
The following signals were fetched from SerpAPI Google News and SerpAPI Google Trends immediately before this pipeline run. Treat Google Trends as AVAILABLE when this section contains a Google Trends block. Use it as the primary search_velocity input for Skills 01–05 (Signal Listener through Trend Strength Scorer). Use the Google News Radar as the broad discovery layer for news-led health topics, including topics that do not yet appear in Google Trends. Prioritize topics with convergence across News, Trends, primary/institutional sources, and credible publisher coverage.

## Google Trends — Trending Now (US / Health, real-time)
Terms with a "Why:" line have a confirmed real-world news story driving the spike; terms without one are a real-time signal only, not yet grounded in a specific story.
  - xylitol cardiovascular risk study
    Why: "This popular sweetener may raise your heart attack, stroke risk" — USA Today

## Google Trends — 7-Day Interest (US)
  - **health**: latest=37, peak=100, 7d-delta=-4
    Rising related: dolly parton death, dolly parton health update, what health issues did dolly parton have, dolly parton health issues, what health issues did dolly parton have?, dolly parton health, willie nelson health, phil collins health
  - **wellness**: latest=94, peak=100, 7d-delta=+13
    Rising related: little luxe wellness lodge, msu student recreation and wellness center, msu wellness center, karma wellness, fsu health and wellness center, wutawhealth wellness advice from whatutalkingboutwillis, student recreation and wellness center, quietgrovehaven.com discover insights on wellness
  - **nutrition**: latest=86, peak=100, 7d-delta=-3
    Rising related: burger king mcdonald's chicken sandwich nutrition, usda watermelon rind nutrition data, kona ice nutrition, supplemental nutrition assistance program, optimum nutrition serious mass, pet nutrition calculator, chick fil a chicken and waffles nutrition, starbucks nutrition calculator
  - **fitness**: latest=48, peak=100, 7d-delta=+8
    Rising related: world fitness project leaderboard, world fitness project, chase stokes body transformation fitness, physical fitness program, fitness centre, holiday fitness, hiking, fitness focus
  - **food safety**: latest=59, peak=100, 7d-delta=+13
    Rising related: walmart food safety recall mangoes, national food safety education month, what does fattom stand for in food safety, premier food safety login, when should hand antiseptics be used, food safety education month, food safety definition, haccp is
  - **diet**: latest=79, peak=100, 7d-delta=+1
    Rising related: the diet that changed my life in four weeks i feel 10 years younger, the diet that changed my life in four weeks, washu medicine keto mediterranean diet study, rose ferguson diet and lifestyle overhaul, dolly parton diet, designates a diet product, is xylitol in diet coke, christie brinkley vegan diet
  - **weight loss**: latest=47, peak=100, 7d-delta=+11
    Rising related: surfshark review, medvi tirzepatide cost, medvi quad reviews, medvi quad, what is medvi, quad mix for ed, quad ed, medvi reviews
  - **mental health**: latest=100, peak=100, 7d-delta=+15
    Rising related: kyle singler mental health, yayoi kusama mental health, september mental health month, suicide prevention month, suicide awareness month, thenervousbreakdown.com mental health, what is mental health, mental health services
  - **gut health**: latest=60, peak=100, 7d-delta=+9
    Rising related: dog gut health chews, seneca, what is gut health, improve gut health, gut health foods, how to improve gut health, probiotics, gut health probiotics

Top rising related queries from Google Trends:
  - dolly parton death
  - dolly parton health update
  - what health issues did dolly parton have
  - dolly parton health issues
  - what health issues did dolly parton have?
  - dolly parton health
  - willie nelson health
  - phil collins health
  - little luxe wellness lodge
  - msu student recreation and wellness center
  - msu wellness center
  - karma wellness
  - fsu health and wellness center
  - wutawhealth wellness advice from whatutalkingboutwillis
  - student recreation and wellness center
  - quietgrovehaven.com discover insights on wellness
  - burger king mcdonald's chicken sandwich nutrition
  - usda watermelon rind nutrition data
  - kona ice nutrition
  - supplemental nutrition assistance program

## Google News Radar — Recent Health Topics (144 unique across 12 queries; showing 60)
Treat these headlines as the broad radar of news-led health topics. The Signal Listener must consider this radar before narrowing to retained candidates.
  - (health) [Arkansas Governor (.gov)] 08/27/2026, 07:06 PM, +0000 UTC — Sanders Announces Nearly $150 Million Awarded in Rural Health Transformation Funds
    
    Link: https://governor.arkansas.gov/news_post/sanders-announces-nearly-150-million-awarded-in-rural-health-transformation-funds/
  - (health) [Iowa Capital Dispatch] 08/25/2026, 10:01 PM, +0000 UTC — Class-action lawsuit claims UnityPoint Health shortchanged hourly workers
    
    Link: https://iowacapitaldispatch.com/2026/08/25/class-action-lawsuit-claims-unitypoint-health-shortchanged-hourly-workers/
  - (health) [Centers for Disease Control and Prevention | CDC (.gov)] 08/27/2026, 07:00 AM, +0000 UTC — Monkeypox in the United States and Around the World: Current Situation
    
    Link: https://www.cdc.gov/monkeypox/situation-summary/index.html
  - (health) [Healthcare Dive] 08/26/2026, 04:07 PM, +0000 UTC — Employers face ‘existential reckoning’ as health costs surge
    
    Link: https://www.healthcaredive.com/news/employers-2027-health-costs-bgh-survey/828734/
  - (health) [The New York Times] 08/26/2026, 11:35 PM, +0000 UTC — Will Meta’s Changes Benefit Young Users’ Mental Health?
    
    Link: https://www.nytimes.com/2026/08/26/well/family/meta-settlement-youth-mental-health.html
  - (health) [NFL.com] 08/27/2026, 02:19 PM, +0000 UTC — Lamar Jackson says health limited his mobility in 2025, will still do 'whatever it takes to win'
    
    Link: https://www.nfl.com/news/ravens-lamar-jackson-health-limited-mobility-2025
  - (health) [Corewell Health Newsroom] 08/27/2026, 01:15 PM, +0000 UTC — Corewell Health Announces $1.7 Billion Investment to Build Stronger Healthcare for Michigan
    
    Link: https://newsroom.corewellhealth.org/news-releases?item=125230
  - (health) [CNBC] 08/28/2026, 11:00 AM, +0000 UTC — Labor Department to propose expansion of association health plans, which could lower insurance costs for some workers
    
    Link: https://www.cnbc.com/2026/08/28/trump-labor-department-proposal-association-health-insurance-plans.html
  - (health) [Vanderbilt Health News] 08/26/2026, 05:07 PM, +0000 UTC — Vanderbilt Health mourns passing of global icon Dolly Parton
    
    Link: https://news.vumc.org/2026/08/26/vanderbilt-health-mourns-passing-of-global-icon-dolly-parton/
  - (health) [pbs.org] 08/26/2026, 10:20 PM, +0000 UTC — Maui residents face health struggles 3 years after wildfires
    
    Link: https://www.pbs.org/newshour/show/maui-residents-face-health-struggles-3-years-after-wildfires
  - (health) [Axios] 08/26/2026, 02:06 PM, +0000 UTC — Scoop: Sword Health to acquire Headspace for up to $300M
    
    Link: https://www.axios.com/pro/health-tech-deals/2026/08/26/sword-health-to-acquire-headspace-300m
  - (health) [CNN] 08/27/2026, 12:01 PM, +0000 UTC — Dolly Parton’s legacy includes an unfortunate reality of caregiving: Not taking care of oneself
    
    Link: https://www.cnn.com/2026/08/27/health/dolly-parton-husband-caregiving-wellness
  - (wellness) [VA News (.gov)] 08/28/2026, 07:00 AM, +0000 UTC — Five organizations with Veterans wellness at the heart of their mission
    
    Link: https://news.va.gov/149155/organizations-veterans-wellness-heart-mission/
  - (wellness) [creators.yahoo.com] 08/29/2026, 07:00 AM, +0000 UTC — Wellness stacking: why psychologists say it beats willpower for building healthy habits
    
    Link: https://creators.yahoo.com/lifestyle/story/wellness-stacking-why-psychologists-say-it-beats-willpower-for-building-healthy-habits-015140677.html
  - (wellness) [army.mil] 08/27/2026, 03:38 PM, +0000 UTC — Post ‘Defends Wellness’ at event
    
    Link: https://www.army.mil/article/294919
  - (wellness) [Miami University RedHawks] 08/28/2026, 06:25 PM, +0000 UTC — Human Performance and Wellness Promotes Czabala, Welcomes Artus
    
    Link: https://miamiredhawks.com/news/2026/8/28/general-human-performance-and-wellness-promotes-czabala-welcomes-artus
  - (wellness) [Grocery Dive] 08/31/2026, 04:06 PM, +0000 UTC — Kroger amplifies wellness focus with in-store events and ‘mini-fests’
    
    Link: https://www.grocerydive.com/news/kroger-wellness-tour-store-events-festivals/829161/
  - (wellness) [Azusa Pacific University] 09/01/2026, 08:10 AM, +0000 UTC — APU Receives $312,500 Grant to Train Certified Wellness Coaches to Help Youth
    
    Link: https://www.apu.edu/media/news/release/apu-receives-312500-grant-to-train-certified-wellness-coaches/
  - (wellness) [CVS Health] 09/01/2026, 02:15 PM, +0000 UTC — LOVB announces CVS Pharmacy as an Official Health & Wellness Partner
    
    Link: https://www.cvshealth.com/news/community/lovb-announces-cvs-pharmacy-as-an-official-health-wellness-partner.html
  - (wellness) [Human Resources University of Michigan |] 08/31/2026, 10:11 PM, +0000 UTC — Invest In Your Mental Wellness
    
    Link: https://hr.umich.edu/about-uhr/uhr-news/invest-your-mental-wellness
  - (wellness) [29news.com] 08/31/2026, 08:36 PM, +0000 UTC — Heart 2 Heart Wellness holds first annual wellness festival
    
    Link: https://www.29news.com/2026/08/31/heart-2-heart-wellness-holds-first-annual-wellness-festival/
  - (wellness) [prnewswire.com] 08/28/2026, 06:00 PM, +0000 UTC — National Release: Kroger Is Improving Wellness in Neighborhoods Across America
    
    Link: https://www.prnewswire.com/news-releases/national-release-kroger-is-improving-wellness-in-neighborhoods-across-america-302862767.html
  - (wellness) [CSUF News] 08/28/2026, 05:00 PM, +0000 UTC — Total Wellness to Host 2026 Health and Wellness Expo
    
    Link: https://news.fullerton.edu/spotlight/total-wellness-to-host-2026-health-and-wellness-expo/
  - (wellness) [Middlesex Borough (.gov)] 08/28/2026, 04:48 PM, +0000 UTC — Senior Wellness Event
    
    Link: https://www.middlesexboro-nj.gov/latest-news/senior-wellness-event
  - (medical study) [KUOW] 08/26/2026, 06:38 PM, +0000 UTC — UW struggles to see medical research through as Trump administration guts funding
    
    Link: https://www.kuow.org/science/2026-08-26/uw-struggles-to-see-medical-research-through-as-trump-administration-guts-funding
  - (medical study) [Augusta University] 08/31/2026, 05:41 PM, +0000 UTC — AU hosts House Blue-Ribbon Study Committee focusing on healthcare
    
    Link: https://jagwire.augusta.edu/au-hosts-house-blue-ribbon-study-committee-focusing-on-healthcare/
  - (medical study) [University of Chicago News] 08/28/2026, 05:00 PM, +0000 UTC — Health care spending gap between high- and low-income Americans widens, study finds
    
    Link: https://news.uchicago.edu/story/health-care-spending-gap-between-high-and-low-income-americans-widens-study-finds
  - (medical study) [New Mexico State University] 08/28/2026, 03:32 PM, +0000 UTC — NMSU, UNLV study: GLP-1s do not cause major psychiatric harm
    
    Link: https://newsroom.nmsu.edu/news/nmsu--unlv-study--glp-1s-do-not-cause-major-psychiatric-harm/s/eee6d3f8-66f0-4974-8cd9-84e547134d7d
  - (medical study) [Nature] 08/26/2026, 09:03 AM, +0000 UTC — Recombinant shingles vaccination and the risk of cardiovascular events
    
    Link: https://www.nature.com/articles/s41591-026-04606-0
  - (medical study) [Newsroom | UCLA] 08/27/2026, 03:18 PM, +0000 UTC — American Indians and Alaska Natives in California face barriers to receiving needed healthcare, UCLA study finds
    
    Link: https://newsroom.ucla.edu/releases/american-indians-alaska-natives-california-face-barriers-healthcare
  - (medical study) [Cytokinetics] 08/28/2026, 09:48 AM, +0000 UTC — Cytokinetics Announces Positive Results from ACACIA-HCM Presented in Hot Line Session at the European Society of Cardiology (ESC) Congress 2026 and Published in The New England Journal of Medicine
    
    Link: https://ir.cytokinetics.com/press-releases/press-release-details/2026/Cytokinetics-Announces-Positive-Results-from-ACACIA-HCM-Presented-in-Hot-Line-Session-at-the-European-Society-of-Cardiology-ESC-Congress-2026-and-Published-in-The-New-England-Journal-of-Medicine/default.aspx
  - (medical study) [The Washington Post] 08/29/2026, 02:18 AM, +0000 UTC — LGBTQ people struggle to get needed health care and pay for it, study finds
    
    Link: https://www.washingtonpost.com/nation/2026/08/28/gay-bisexual-trans-people-struggle-get-health-care-study-says/
  - (medical study) [ABC News - Breaking News, Latest News and Videos] 08/26/2026, 06:23 PM, +0000 UTC — Heat makes emergency rooms busier. Study shows which illness and injuries rise during hot spells
    
    Link: https://abcnews.com/Technology/wireStory/heat-makes-emergency-rooms-busier-study-shows-illness-135982188
  - (medical study) [Harvard Medical School] 08/25/2026, 04:10 PM, +0000 UTC — At Least 1 in 4 Former NFL Players Who Died in 2016-2021 Had CTE at Death, Study Finds
    
    Link: https://hms.harvard.edu/news/least-1-4-former-nfl-players-who-died-2016-2021-had-cte-death-study-finds
  - (medical study) [medicine.washu.edu] 08/27/2026, 03:02 PM, +0000 UTC — Low-carb diet delivers added liver benefits beyond weight loss
    
    Link: https://medicine.washu.edu/news/low-carb-diet-delivers-added-liver-benefits-beyond-weight-loss/
  - (medical study) [FOX 5 Atlanta] 08/27/2026, 04:12 PM, +0000 UTC — Study links medical marijuana access to fewer sick days
    
    Link: https://www.fox5atlanta.com/video/fmc-9qw498li359e4elq
  - (clinical trial health) [The Detroit News] 08/27/2026, 04:34 PM, +0000 UTC — Want to join a clinical trial? Be prepared for hurdles
    
    Link: https://www.detroitnews.com/story/life/wellness/2026/08/27/clinical-trial-illnesses-hurdles-facts/91491105007/
  - (clinical trial health) [Cancer Health] 08/26/2026, 07:23 PM, +0000 UTC — Costs and Geographic Barriers Impact Cancer Clinical Trial Participation
    
    Link: https://www.cancerhealth.com/article/costs-geographic-barriers-impact-cancer-clinical-trial-participation
  - (clinical trial health) [The Clinical Trial Vanguard] 09/01/2026, 12:06 PM, +0000 UTC — Benchmarks Don’t Fail Silently. Agentic AI Does.
    
    Link: https://www.clinicaltrialvanguard.com/clinical-bellwether/benchmarks-dont-fail-silently-agentic-ai-does/
  - (clinical trial health) [CancerNetwork] 08/30/2026, 01:56 PM, +0000 UTC — How Can Health Networks Bring Clinical Trials Directly To Patients?
    
    Link: https://www.cancernetwork.com/shorts/how-can-health-networks-bring-clinical-trials-directly-to-patients-
  - (clinical trial health) [Chemical & Engineering News] 08/28/2026, 01:23 PM, +0000 UTC — As clinical trials surge into Australia, HHS targets US bottlenecks
    
    Link: https://cen.acs.org/pharmaceuticals/drug-development/australia-clinical-drug-trial-fda-trialblazer/104/web/2026/08
  - (clinical trial health) [NYU Langone Health] 08/25/2026, 05:13 PM, +0000 UTC — NYU Langone Health to Lead New Trial of Ketamine for Pain Relief
    
    Link: https://nyulangone.org/news/nyu-langone-health-lead-new-trial-ketamine-pain-relief
  - (clinical trial health) [Post Bulletin] 08/29/2026, 11:48 AM, +0000 UTC — In Southeast Minnesota, clinical trial participation plays a key role in advancing science
    
    Link: https://www.postbulletin.com/health/in-southeast-minnesota-clinical-trial-participation-plays-a-key-role-in-advancing-science
  - (clinical trial health) [biopharmaapac.com] 08/31/2026, 06:49 PM, +0000 UTC — Data4Life, Monash Health Partner to Accelerate Clinical Trials and Real-World Evidence Generation
    
    Link: https://biopharmaapac.com/news/81/8375/data4life-monash-health-partner-to-accelerate-clinical-trials-and-real-world-evidence-generation.html
  - (clinical trial health) [Clinical Leader] 08/28/2026, 04:09 AM, +0000 UTC — The Pharmacy Benefit No One Is Managing: Clinical Research As A Care Option
    
    Link: https://www.clinicalleader.com/doc/the-pharmacy-benefit-no-one-is-managing-clinical-research-as-a-care-option-0001
  - (clinical trial health) [WHYY] 09/01/2026, 12:34 PM, +0000 UTC — ‘Blink of an eye’: Penn researchers launch clinical trial for faster form of cancer radiation therapy
    
    Link: https://whyy.org/articles/flash-proton-radiation-therapy-cancer-clinical-trial-penn/
  - (clinical trial health) [University of Utah Health] 08/25/2026, 05:56 PM, +0000 UTC — U of U Health Awarded $30 Million to Study Treatment for Alcohol Withdrawal Syndrome
    
    Link: https://healthcare.utah.edu/press-releases/2026/08/u-of-u-health-awarded-30-million-study-treatment-alcohol-withdrawal-syndrome
  - (clinical trial health) [Scientific American] 08/27/2026, 03:55 PM, +0000 UTC — Is the keto diet better than the Mediterranean? New clinical trial reveals health benefits
    
    Link: https://www.scientificamerican.com/article/is-the-keto-diet-better-than-the-mediterranean-new-clinical-trial-reveals-health-benefits/
  - (FDA recall health) [fda.gov] 08/26/2026, 12:00 AM, +0000 UTC — Outbreak Investigation of Listeria monocytogenes: Soft Cheese (June 2026)
    
    Link: https://www.fda.gov/food/outbreaks-foodborne-illness/outbreak-investigation-listeria-monocytogenes-soft-cheese-june-2026
  - (FDA recall health) [Centers for Disease Control and Prevention | CDC (.gov)] 08/27/2026, 07:00 AM, +0000 UTC — Cyclospora Outbreak Linked to Iceberg Lettuce | Cyclosporiasis
    
    Link: https://www.cdc.gov/cyclosporiasis/outbreaks/07-26/index.html
  - (FDA recall health) [American Hospital Association] 08/28/2026, 09:16 PM, +0000 UTC — FDA issues recall, alerts for certain convenience kits; companies voluntarily recall certain IV fluids
    
    Link: https://www.aha.org/news/headline/2026-08-28-fda-issues-recall-alerts-certain-convenience-kits-companies-voluntarily-recall-certain-iv-fluids
  - (FDA recall health) [NewsNation] 08/27/2026, 09:02 PM, +0000 UTC — FDA announces drug recalls over potential presence of fiberglass, steel
    
    Link: https://www.newsnationnow.com/us-news/recalls/fda-announces-drug-recalls-over-potential-presence-of-fiberglass-steel/
  - (FDA recall health) [USA Today] 08/28/2026, 01:41 PM, +0000 UTC — Are food recalls increasing under RFK? What the data reveals.
    
    Link: https://www.usatoday.com/story/news/health/2026/08/28/food-recalls-under-rfk-jr-data/91494801007/
  - (FDA recall health) [The Hill] 08/25/2026, 04:10 PM, +0000 UTC — Thyroid tablets recalled nationwide over potential ‘superpotency’: FDA
    
    Link: https://thehill.com/policy/healthcare/6049169-thyroid-tablets-recalled-nationwide-potential-superpotency-fda/
  - (FDA recall health) [People.com] 08/28/2026, 02:19 PM, +0000 UTC — FDA Classifies Guacamole Recall at Highest Risk Level amid Investigation into Salmonella Outbreak Linked to Jalapeño Supplier
    
    Link: https://people.com/whole-foods-guacamole-recall-gets-fda-s-highest-risk-classification-12070208
  - (FDA recall health) [health.com] 08/31/2026, 02:24 PM, +0000 UTC — FDA Announces Tofu Recall: More Than 10,000 Cases May Be Contaminated With Ink
    
    Link: https://www.health.com/tofu-recall-august-2026-12073618
  - (FDA recall health) [MedShadow Foundation] 08/25/2026, 06:21 PM, +0000 UTC — FDA Recalls and Warnings: Levothyroxine and Natural Thyroid Drugs Recalled for Potency Problems
    
    Link: https://medshadow.org/drug-updates-recalls/fda-recalls-and-warnings/subpotent-levothyroxine-sodium-tablets-superpotent-thyroid-tablets/
  - (FDA recall health) [Food Safety Magazine] 08/28/2026, 02:14 PM, +0000 UTC — FDA Explains Recall Classifications to Get Ahead of Cyclospora Outbreak Panic
    
    Link: https://www.food-safety.com/articles/11773-fda-explains-recall-classifications-to-get-ahead-of-cyclospora-outbreak-panic
  - (FDA recall health) [KTALnews.com] 08/27/2026, 07:47 PM, +0000 UTC — FDA recalls popular IV bags over possible fiberglass contamination
    
    Link: https://www.ktalnews.com/health/baxter-sodium-chloride-recall/
  - (FDA recall health) [Star Tribune] 08/31/2026, 06:01 PM, +0000 UTC — Medtronic recall prompts FDA safety alert after 184 serious injuries
    
    Link: https://www.startribune.com/medtronic-recall-bravo-cf-reflux-gastroesophageal/601883787