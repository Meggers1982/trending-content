# LIVE SIGNAL DATA — SerpAPI Pre-Fetch
The following signals were fetched from SerpAPI Google News and SerpAPI Google Trends immediately before this pipeline run. Treat Google Trends as AVAILABLE when this section contains a Google Trends block. Use it as the primary search_velocity input for Skills 01–05 (Signal Listener through Trend Strength Scorer). Use the Google News Radar as the broad discovery layer for news-led health topics, including topics that do not yet appear in Google Trends. Prioritize topics with convergence across News, Trends, primary/institutional sources, and credible publisher coverage.

## Google Trends — Trending Now (US / Health, real-time)
Terms with a "Why:" line have a confirmed real-world news story driving the spike; terms without one are a real-time signal only, not yet grounded in a specific story.
  - phil collins
    Why: "Phil Collins' Family 'Prepared For His Death' During Health Crisis, According to Reports" — Yahoo Lifestyle Canada
  - confirmed cyclosporiasis cases 48 states
    Why: "Cyclospora Case Data | Cyclosporiasis" — Centers for Disease Control and Prevention | CDC (.gov)

## Google Trends — 7-Day Interest (US)
  - **health**: latest=28, peak=100, 7d-delta=+0
    Rising related: dolly parton health update, what are the latest health updates from dolly parton and details on her new museum, dolly parton health, tim curry health, dolly parton health issues, what health issues did dolly parton have?, what health issues did dolly parton have, dolly parton breaking news
  - **wellness**: latest=63, peak=100, 7d-delta=-4
    Rising related: patagonia black hole duffel 100l tidal tea, shrek 5, 772-563-4880, ndsu wellness center, und wellness center, activeplayhub achieve your wellness goals with expert insights on fitness, intellectual wellness, naturaplug health and wellness
  - **nutrition**: latest=80, peak=100, 7d-delta=-4
    Rising related: curtain up, cooked versus raw vegetables nutrition, generation channel, curtain up channel, action channel, sundance, comeback kid, sundance kid
  - **fitness**: latest=68, peak=100, 7d-delta=-4
    Rising related: muscle definition over 50 fitness, fintechzoom .io, harley pasternak fitness advice, hospitals, museums, vegetables, baking, vitamins
  - **food safety**: latest=19, peak=100, 7d-delta=-1
    Rising related: project 2025 food supply, project 2025, what does fattom stand for in food safety, food safety recalls, food recalls, what is food safety, fda, food safety certification
  - **diet**: latest=81, peak=100, 7d-delta=-5
    Rising related: washu medicine keto mediterranean diet study, christie brinkley vegan diet, dolly parton diet, designates a diet product, billy bob thornton diet, how to learn english fast, healthy diet plan for beginners, how to start freelancing online
  - **weight loss**: latest=47, peak=100, 7d-delta=+2
    Rising related: billy gardell weight loss transformation, tiffany franco 110 pound weight loss, wynonna judd weight loss, medvi quad reviews, medvi quad, luka doncic weight loss, quad ed, medvi tirzepatide cost
  - **mental health**: latest=60, peak=100, 7d-delta=+0
    Rising related: kyle singler mental health, this type of sex benefits your physical and mental health the most, yayoi kusama mental health, free mental health services near me no insurance, how to improve mental health lwspeakcare, alleviant integrated mental health, mendota mental health institute, in patient care mental health near me
  - **gut health**: latest=54, peak=100, 7d-delta=+3
    Rising related: who isolated radium in 1910, who used acupuncture to relieve pain and congestion, who began public health and sanitation systems, isolated radium in 1910, began public health and sanitation systems, is farting a sign of good gut health, used acupuncture to relieve pain and congestion, resilia

Top rising related queries from Google Trends:
  - dolly parton health update
  - what are the latest health updates from dolly parton and details on her new museum
  - dolly parton health
  - tim curry health
  - dolly parton health issues
  - what health issues did dolly parton have?
  - what health issues did dolly parton have
  - dolly parton breaking news
  - patagonia black hole duffel 100l tidal tea
  - shrek 5
  - 772-563-4880
  - ndsu wellness center
  - und wellness center
  - activeplayhub achieve your wellness goals with expert insights on fitness
  - intellectual wellness
  - naturaplug health and wellness
  - curtain up
  - cooked versus raw vegetables nutrition
  - generation channel
  - curtain up channel

## Google News Radar — Recent Health Topics (144 unique across 12 queries; showing 60)
Treat these headlines as the broad radar of news-led health topics. The Signal Listener must consider this radar before narrowing to retained candidates.
  - (health) [Centers for Disease Control and Prevention | CDC (.gov)] 08/21/2026, 07:00 AM, +0000 UTC — Measles Cases and Outbreaks
    
    Link: https://www.cdc.gov/measles/data-research/index.html
  - (health) [ICRC] 08/24/2026, 11:29 AM, +0000 UTC — Protection of health care
    
    Link: https://www.icrc.org/en/law-and-policy/protection-health-care
  - (health) [Arkansas Governor (.gov)] 08/27/2026, 07:06 PM, +0000 UTC — Sanders Announces Nearly $150 Million Awarded in Rural Health Transformation Funds
    
    Link: https://governor.arkansas.gov/news_post/sanders-announces-nearly-150-million-awarded-in-rural-health-transformation-funds/
  - (health) [Maryland.gov] 08/24/2026, 07:13 PM, +0000 UTC — Pages - Maryland Department of Health declares measles outbreak in three Maryland counties
    
    Link: https://health.maryland.gov/newsroom/Pages/Maryland%20Department%20of%20Health%20declares%20measles%20outbreak%20in%20three%20Maryland%20counties.aspx
  - (health) [aphis.usda.gov] 08/21/2026, 07:00 AM, +0000 UTC — Confirmed Detections of New World Screwworm | Animal and Plant Health Inspection Service
    
    Link: https://www.aphis.usda.gov/animals/animal-health/livestock-and-poultry-disease/stop-screwworm/current-status/confirmed
  - (health) [Clemson University Athletics] 08/26/2026, 08:32 PM, +0000 UTC — Prisma Health Makes Its Mark on Clemson
    
    Link: https://clemsontigers.com/news/2026/08/26/prisma-health-makes-its-mark-on-clemson
  - (health) [Maryland Matters] 08/21/2026, 09:35 AM, +0000 UTC — Maryland launches court-ordered mental health care in Baltimore, some counties
    
    Link: https://marylandmatters.org/2026/08/21/maryland-launches-court-ordered-mental-health-care-in-baltimore-some-counties/
  - (health) [NASA (.gov)] 08/24/2026, 07:00 AM, +0000 UTC — Request for Information: Help Shape Human Health Research for the Future Moon Base
    
    Link: https://www.nasa.gov/hrp/request-for-information-help-shape-human-health-research-for-the-future-moon-base/
  - (health) [Raiders.com] 08/24/2026, 05:02 PM, +0000 UTC — Las Vegas Raiders announce $25 million game-changing gift to Intermountain Health to help build Nevada's first stand-alone children's hospital
    
    Link: https://www.raiders.com/news/las-vegas-raiders-announce-25-million-game-changing-gift-to-intermountain-health-to-help-build-nevada-s-first-stand-alone-children-s-hospital
  - (health) [Iowa Capital Dispatch] 08/25/2026, 10:01 PM, +0000 UTC — Class-action lawsuit claims UnityPoint Health shortchanged hourly workers
    
    Link: https://iowacapitaldispatch.com/2026/08/25/class-action-lawsuit-claims-unitypoint-health-shortchanged-hourly-workers/
  - (health) [People.com] 08/22/2026, 01:55 AM, +0000 UTC — Dolly Parton Shares Health Update While Announcing Plans for Museum (Exclusive)
    
    Link: https://people.com/dolly-parton-shares-health-update-while-announcing-plans-for-museum-exclusive-12065750
  - (health) [ClickOnDetroit | WDIV Local 4] 08/27/2026, 02:16 AM, +0000 UTC — FBI searches Quality Behavioral Health facilities in Detroit, Troy, amid federal investigation
    
    Link: https://www.clickondetroit.com/news/local/2026/08/27/fbi-searches-quality-behavioral-health-facilities-in-detroit-troy-amid-federal-investigation/
  - (wellness) [FOX 13 Tampa Bay] 08/21/2026, 03:26 AM, +0000 UTC — Wellness retreat project
    
    Link: https://www.fox13news.com/news/oxford-exchange-owners-plan-550-acre-wellness-retreat-near-dade-city
  - (wellness) [Yahoo Creators] 08/24/2026, 01:15 PM, +0000 UTC — Wellness stacking: why psychologists say it beats willpower for building healthy habits
    
    Link: https://creators.yahoo.com/lifestyle/story/wellness-stacking-why-psychologists-say-it-beats-willpower-for-building-healthy-habits-015140677.html
  - (wellness) [University of Nebraska Medical Center] 08/25/2026, 09:15 AM, +0000 UTC — Center for Healthy Living integrates fitness, wellness
    
    Link: https://www.unmc.edu/newsroom/2026/08/25/center-for-healthy-living-integrates-fitness-wellness/
  - (wellness) [WFLA] 08/23/2026, 04:18 PM, +0000 UTC — 1 dead, officer hospitalized after attempted wellness check in St. Pete: PCSO
    
    Link: https://www.wfla.com/news/pinellas-county/1-dead-officer-hospitalized-after-attempted-wellness-check-in-st-pete-pcso/
  - (wellness) [VA.gov Home | Veterans Affairs] 08/26/2026, 04:44 PM, +0000 UTC — The Freedom Garden Project: Teaming Up to Grow Veteran Wellness | VA Washington DC health care | Veterans Affairs
    
    Link: https://www.va.gov/washington-dc-health-care/stories/the-freedom-garden-project-teaming-up-to-grow-veteran-wellness/
  - (wellness) [ELLE] 08/26/2026, 09:35 PM, +0000 UTC — The Oura Ring 5 Is the Most Stylish Wellness Device You Can Buy
    
    Link: https://www.elle.com/beauty/health-fitness/a73297148/oura-ring-5-review/
  - (wellness) [Ground Truths | Eric Topol] 08/23/2026, 02:41 PM, +0000 UTC — Deborah Cohen: The Wellness-Industrial Complex
    
    Link: https://erictopol.substack.com/p/deborah-cohen-the-wellness-industrial
  - (wellness) [The New York Times] 08/21/2026, 02:35 PM, +0000 UTC — ‘Spa Weekend’ Review: Girls Gone Wellness
    
    Link: https://www.nytimes.com/2026/08/21/movies/spa-weekend-review.html
  - (wellness) [UCLA Health] 08/24/2026, 09:28 PM, +0000 UTC — Is a wellness drink worth it? Decoding functional beverage labels
    
    Link: https://www.uclahealth.org/news/article/wellness-drink-worth-it-decoding-functional-beverage-labels
  - (wellness) [American Medical Association | AMA] 08/26/2026, 12:06 PM, +0000 UTC — It’s time to rethink how wellness apps, devices are regulated
    
    Link: https://www.ama-assn.org/practice-management/digital-health/it-s-time-rethink-how-wellness-apps-devices-are-regulated
  - (wellness) [Pratt Institute] 08/25/2026, 04:11 PM, +0000 UTC — A Centralized Hub for Student Wellness Opens on Pratt’s Brooklyn Campus
    
    Link: https://www.pratt.edu/news/a-centralized-hub-for-student-wellness-opens-on-pratts-brooklyn-campus/
  - (wellness) [Milwaukee Neighborhood News Service] 08/24/2026, 11:27 PM, +0000 UTC — Post From Community: Wellness Wonderland brings mental health support and family fun to Milwaukee
    
    Link: https://milwaukeenns.org/2026/08/24/post-from-community-wellness-wonderland-brings-mental-health-support-and-family-fun-to-milwaukee/
  - (medical study) [KUOW] 08/26/2026, 06:38 PM, +0000 UTC — UW struggles to see medical research through as Trump administration guts funding
    
    Link: https://www.kuow.org/science/2026-08-26/uw-struggles-to-see-medical-research-through-as-trump-administration-guts-funding
  - (medical study) [NYU Langone Health] 08/25/2026, 05:13 PM, +0000 UTC — NYU Langone Health to Lead New Trial of Ketamine for Pain Relief
    
    Link: https://nyulangone.org/news/nyu-langone-health-lead-new-trial-ketamine-pain-relief
  - (medical study) [Wolters Kluwer] 08/25/2026, 07:48 PM, +0000 UTC — Medical Research Platform | Institutional Partners
    
    Link: https://www.wolterskluwer.com/en/expert-insights/comprehensive-literature-search-multiple-databases
  - (medical study) [Yahoo Sports] 08/25/2026, 03:20 PM, +0000 UTC — Terrifying NFL Discovery: Bombshell New Medical Study Exposes How Many Deceased Players Had CTE
    
    Link: https://sports.yahoo.com/articles/terrifying-nfl-discovery-bombshell-medical-152045510.html
  - (medical study) [WashU Medicine] 08/27/2026, 03:02 PM, +0000 UTC — Low-carb diet delivers added liver benefits beyond weight loss
    
    Link: https://medicine.washu.edu/news/low-carb-diet-delivers-added-liver-benefits-beyond-weight-loss/
  - (medical study) [Medical Xpress] 08/21/2026, 05:00 PM, +0000 UTC — Robotic assisted knee replacement gives same patient outcomes as surgeon-only procedure in clinical trial
    
    Link: https://medicalxpress.com/news/2026-08-robotic-knee-patient-outcomes-surgeon.html
  - (medical study) [Columbia University Irving Medical Center] 08/21/2026, 02:24 AM, +0000 UTC — Depression Stalls Formation of New Brain Cells
    
    Link: https://www.cuimc.columbia.edu/news/depression-stalls-formation-new-brain-cells
  - (medical study) [WSJ] 08/27/2026, 05:43 PM, +0000 UTC — Exclusive | Startup to Link ‘Biobanks’ of Patient Tissue to Supercharge AI Medical Research
    
    Link: https://www.wsj.com/pro/venture-capital/startup-to-link-biobanks-of-patient-tissue-to-supercharge-ai-medical-research-55403925
  - (medical study) [Colorado Public Radio] 08/21/2026, 10:02 AM, +0000 UTC — Immigration policies put stress on the health care of immigrants; new study finds their doctors feel it too.
    
    Link: https://www.cpr.org/2026/08/21/federal-immigration-policies-impact-doctors-study/
  - (medical study) [PR Newswire] 08/26/2026, 10:45 AM, +0000 UTC — Zepbound linked to lower healthcare costs in adults over age 55 with obesity according to a real-world study
    
    Link: https://www.prnewswire.com/news-releases/zepbound-linked-to-lower-healthcare-costs-in-adults-over-age-55-with-obesity-according-to-a-real-world-study-302859960.html
  - (medical study) [Nature] 08/25/2026, 09:09 AM, +0000 UTC — Oligodendrocyte dysfunction in human age-related cognitive decline
    
    Link: https://www.nature.com/articles/s41591-026-04608-y
  - (medical study) [Healthcare Finance News] 08/26/2026, 03:10 PM, +0000 UTC — Eli Lilly study finds Zepbound lowers healthcare costs over time
    
    Link: https://www.healthcarefinancenews.com/news/eli-lilly-study-finds-zepbound-lowers-healthcare-costs-over-time
  - (clinical trial health) [CNN] 08/22/2026, 04:00 PM, +0000 UTC — You want to join a clinical trial. Here’s what to know about the hurdles.
    
    Link: https://www.cnn.com/2026/08/22/health/clinical-trials-what-to-know
  - (clinical trial health) [Cancer Health] 08/25/2026, 03:13 AM, +0000 UTC — Clinical Trials Matter: What Our Patients Say
    
    Link: https://www.cancerhealth.com/article/clinical-trials-matter-patients-say
  - (clinical trial health) [Scientific American] 08/27/2026, 03:55 PM, +0000 UTC — Is the keto diet better than the Mediterranean? New clinical trial reveals health benefits
    
    Link: https://www.scientificamerican.com/article/is-the-keto-diet-better-than-the-mediterranean-new-clinical-trial-reveals-health-benefits/
  - (clinical trial health) [Tufts Now] 08/25/2026, 12:00 PM, +0000 UTC — One Center’s Oversized Impact on Drug Development and Clinical Trials
    
    Link: https://now.tufts.edu/2026/08/25/one-centers-oversized-impact-drug-development-and-clinical-trials
  - (clinical trial health) [PR Newswire] 08/25/2026, 12:01 PM, +0000 UTC — Allegheny Health Network and The START Center for Cancer Research Announce Strategic Collaboration to Expand Patient Access to Early-Phase Cancer Trials
    
    Link: https://www.prnewswire.com/news-releases/allegheny-health-network-and-the-start-center-for-cancer-research-announce-strategic-collaboration-to-expand-patient-access-to-early-phase-cancer-trials-302858392.html
  - (clinical trial health) [Nutrition Insight] 08/21/2026, 04:17 PM, +0000 UTC — Perelel’s Triple-Support protein shows promise for women’s health in clinical trial
    
    Link: https://www.nutritioninsight.com/news/perelel-triple-support-protein-womens-health.html
  - (clinical trial health) [MedTech Dive] 08/21/2026, 04:30 PM, +0000 UTC — How can wearables be used in clinical trials? FDA outlines best practices
    
    Link: https://www.medtechdive.com/news/how-can-wearables-be-used-in-clinical-trials-fda-outlines-best-practices/828512/
  - (clinical trial health) [The Clinical Trial Vanguard] 08/25/2026, 12:09 PM, +0000 UTC — The Oregon Dataset Is Larger Than the Entire History of Psychedelic Trials. So Why Are Regulators Still Looking the Other Way?
    
    Link: https://www.clinicaltrialvanguard.com/clinical-bellwether/the-oregon-dataset-is-larger-than-the-entire-history-of-psychedelic-trials-so-why-are-regulators-still-looking-the-other-way/
  - (clinical trial health) [Newswise] 08/20/2026, 10:30 PM, +0000 UTC — Her Muscles Are Slowly Turning to Bone. She Was the Only American in a Trial That Might Stop It | Newswise
    
    Link: https://www.newswise.com/articles/her-muscles-are-slowly-turning-to-bone-she-was-the-only-american-in-a-trial-that-might-stop-it
  - (clinical trial health) [Medical Xpress] 08/21/2026, 04:20 PM, +0000 UTC — In cancer clinical trials, federal and industry sponsors play complementary roles
    
    Link: https://medicalxpress.com/news/2026-08-cancer-clinical-trials-federal-industry.html
  - (clinical trial health) [The American Journal of Managed Care] 08/21/2026, 07:39 PM, +0000 UTC — Mobile Integrated Health Valuable in Heart Failure, but Payment Lags
    
    Link: https://www.ajmc.com/view/mobile-integrated-health-valuable-in-heart-failure-but-payment-lags
  - (clinical trial health) [WorldHealth.net] 08/21/2026, 05:00 AM, +0000 UTC — Clinical Trial Analytics: From Patient Recruitment to Evidence-Based Innovation
    
    Link: https://worldhealth.net/news/clinical-trial-analytics-recruitment-evidence/
  - (FDA recall health) [fda.gov] 08/24/2026, 03:07 PM, +0000 UTC — Outbreak Investigation of Shiga Toxin-producing E. coli & Salmonella: Sprouts (August 2026)
    
    Link: https://www.fda.gov/food/outbreaks-foodborne-illness/outbreak-investigation-shiga-toxin-producing-e-coli-salmonella-sprouts-august-2026
  - (FDA recall health) [The New York Times] 08/23/2026, 06:12 PM, +0000 UTC — Nearly 40,000 Eye Drop Bottles Are Recalled Over Potential Contamination
    
    Link: https://www.nytimes.com/2026/08/23/health/clear-eyes-eye-drops-fda-recall.html
  - (FDA recall health) [Axios] 08/22/2026, 10:01 AM, +0000 UTC — Here's why the FDA hit frozen blueberries with its highest risk warning
    
    Link: https://www.axios.com/2026/08/22/frozen-blueberries-recall-fda-high-risk-warning
  - (FDA recall health) [The Washington Post] 08/21/2026, 12:15 AM, +0000 UTC — FDA upgrades recall of frozen berries to highest-risk warning
    
    Link: https://www.washingtonpost.com/health/2026/08/20/fda-upgrades-recall-frozen-berries-highest-risk-warning/
  - (FDA recall health) [NewsNation] 08/22/2026, 12:29 PM, +0000 UTC — Food recalls aren’t a success story, former FDA official says
    
    Link: https://www.newsnationnow.com/health/food-recalls-arent-success-story-former-fda-official/
  - (FDA recall health) [The Hill] 08/25/2026, 04:10 PM, +0000 UTC — Thyroid tablets recalled nationwide over potential ‘superpotency’: FDA
    
    Link: https://thehill.com/policy/healthcare/6049169-thyroid-tablets-recalled-nationwide-potential-superpotency-fda/
  - (FDA recall health) [WRAL] 08/21/2026, 03:40 PM, +0000 UTC — Publix frozen berry recall upgraded to FDA’s highest-risk level
    
    Link: https://www.wral.com/consumer/5onyourside/publix-blueberry-recall-upgraded-august-2026/
  - (FDA recall health) [NBC News] 08/21/2026, 05:59 PM, +0000 UTC — Eye drops recalled over possible contamination, FDA reports
    
    Link: https://www.nbcnews.com/health/health-news/eye-drops-sold-nationwide-recalled-possible-contamination-fda-reports-rcna593718
  - (FDA recall health) [The Guardian] 08/22/2026, 03:45 PM, +0000 UTC — 40,000 bottles of eye drops across the US recalled over issues with sterility of product
    
    Link: https://www.theguardian.com/us-news/2026/aug/22/eyedrop-recall-clear-eyes
  - (FDA recall health) [The Healthy @Reader's Digest] 08/21/2026, 12:14 AM, +0000 UTC — Ice Cream Recalled in 3 States for Possible Rubber
    
    Link: https://www.thehealthy.com/news/ice-cream-recall-fda-report-august-2026/
  - (FDA recall health) [MedShadow Foundation] 08/25/2026, 06:21 PM, +0000 UTC — FDA Recalls and Warnings: Levothyroxine and Natural Thyroid Drugs Recalled for Potency Problems
    
    Link: https://medshadow.org/drug-updates-recalls/fda-recalls-and-warnings/subpotent-levothyroxine-sodium-tablets-superpotent-thyroid-tablets/
  - (FDA recall health) [KTALnews.com] 08/27/2026, 07:47 PM, +0000 UTC — FDA recalls popular IV bags over possible fiberglass contamination
    
    Link: https://www.ktalnews.com/health/baxter-sodium-chloride-recall/