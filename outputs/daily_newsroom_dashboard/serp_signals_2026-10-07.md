# LIVE SIGNAL DATA — SerpAPI Pre-Fetch
The following signals were fetched from SerpAPI Google News and SerpAPI Google Trends immediately before this pipeline run. Treat Google Trends as AVAILABLE when this section contains a Google Trends block. Use it as the primary search_velocity input for Skills 01–05 (Signal Listener through Trend Strength Scorer). Use the Google News Radar as the broad discovery layer for news-led health topics, including topics that do not yet appear in Google Trends. Prioritize topics with convergence across News, Trends, primary/institutional sources, and credible publisher coverage.

## Google Trends — Trending Now (US / Health, real-time)
Terms with a "Why:" line have a confirmed real-world news story driving the spike; terms without one are a real-time signal only, not yet grounded in a specific story.
  - megan fox 2026
    Why: "Megan Fox Says She’s Had a ‘Lot More Peace’ as a Mom This Time Around: ‘I’ve Been Able to Be Present’ (Exclusive)" — People.com

## Google Trends — 7-Day Interest (US)
  - **health**: latest=99, peak=100, 7d-delta=+9
    Rising related: christa pike health update, health insurance giant nyt, health insurance giant, meritain health provider portal, when is open enrollment for health insurance 2027, world mental health day 2026, costco health insurance, united health care provider portal
  - **wellness**: latest=38, peak=100, 7d-delta=-3
    Rising related: heal wellness lubbock, stc wellness city, julianne hough beauty and wellness, heal wellness, prana wellness club, prana wellness, a cure for wellness, cure for wellness
  - **nutrition**: latest=88, peak=100, 7d-delta=-5
    Rising related: supplemental nutrition assistance program changes, supplemental nutrition assistance program payment changes, kona ice nutrition, supplemental nutrition assistance program, nutrition nest, tradesman nutrition shred reviews, tradesman nutrition shred, best time to visit maldives
  - **fitness**: latest=62, peak=100, 7d-delta=-2
    Rising related: luke combs fitness transformation, george armstrong fitness, cruz control fitness, body lab fitness, how to cancel planet fitness membership online, my fitness pal login, cancel planet fitness membership online, planet
  - **food safety**: latest=100, peak=100, 7d-delta=+24
    Rising related: chipotle food safety 7, food safety certification texas, food safety manager certification practice test, cheapest flights to tokyo, top tourist attractions in paris, what is food safety, state food safety, food safety certification
  - **diet**: latest=82, peak=100, 7d-delta=+1
    Rising related: merv griffin, diet sprite meaning, something wicked, diet beverages vs water weight loss, mind diet brain aging study, f factor diet, diet museum, diet sprite
  - **weight loss**: latest=62, peak=100, 7d-delta=-7
    Rising related: six month tirzepatide weight loss, diet beverages vs water weight loss, astonishing weight loss when glp 1, cbl-514 weight loss injection, eli lilly retatrutide weight loss, explain how wegovy works for weight loss and its common side effects, dj khaled weight loss, explain how zepbound works for weight loss and its primary side effects
  - **mental health**: latest=95, peak=100, 7d-delta=-3
    Rising related: lane johnson mental health, october mental health awareness month, is october mental health awareness month, when is world mental health day 2026, mental health awareness week, world mental health day 2026, world mental health day, when is world mental health day
  - **gut health**: latest=54, peak=100, 7d-delta=+1
    Rising related: recommend the best fermented foods to add to a daily diet for gut health, best laptop for work, l-glutamine for gut health, stewed apples recipe, psyllium husk, foods that improve gut health, gastroenterologist, good gut health

Top rising related queries from Google Trends:
  - christa pike health update
  - health insurance giant nyt
  - health insurance giant
  - meritain health provider portal
  - when is open enrollment for health insurance 2027
  - world mental health day 2026
  - costco health insurance
  - united health care provider portal
  - heal wellness lubbock
  - stc wellness city
  - julianne hough beauty and wellness
  - heal wellness
  - prana wellness club
  - prana wellness
  - a cure for wellness
  - cure for wellness
  - supplemental nutrition assistance program changes
  - supplemental nutrition assistance program payment changes
  - kona ice nutrition
  - supplemental nutrition assistance program

## Google News Radar — Recent Health Topics (144 unique across 12 queries; showing 60)
Treat these headlines as the broad radar of news-led health topics. The Signal Listener must consider this radar before narrowing to retained candidates.
  - (health) [World Health Organization (WHO)] 10/02/2026, 08:13 AM, +0000 UTC — New WHO estimates show changing global health landscape
    
    Link: https://www.who.int/news/item/02-10-2026-new-who-estimates-show-changing-global-health-landscape
  - (health) [Alabama Governor's Office (.gov)] 10/01/2026, 04:48 PM, +0000 UTC — Governor Ivey Announces Additional Alabama Rural Health Transformation Program Grants Totaling Nearly $55 Million
    
    Link: https://governor.alabama.gov/newsroom/2026/10/governor-ivey-announces-additional-alabama-rural-health-transformation-program-grants-totaling-nearly-55-million/
  - (health) [U.S. Embassy & Consulates in Russia (.gov)] 10/06/2026, 06:54 PM, +0000 UTC — Health Alert – U.S. Embassy Moscow, Russia (October 6, 2026)
    
    Link: https://ru.usembassy.gov/health-alert-u-s-embassy-moscow-russia-october-6-2026/
  - (health) [KFF] 10/06/2026, 09:02 AM, +0000 UTC — Poll: Cost of Health Care and Gas Top Voters' Midterm Concerns; Democrats Hold Significant Advantage on Health Care Costs and Cost of Living
    
    Link: https://www.kff.org/public-opinion/poll-cost-of-health-care-and-gas-top-voters-midterm-concerns-democrats-hold-significant-advantage-on-health-care-costs-and-cost-of-living/
  - (health) [HHS.gov] 10/05/2026, 03:30 PM, +0000 UTC — New Regulations Make It Easier to Find, Compare, and Report Healthcare Pricing and Coverage Information
    
    Link: https://www.hhs.gov/press-room/cms-finalizes-healthcare-price-transparency-rules.html
  - (health) [Kettering Health] 10/06/2026, 04:18 PM, +0000 UTC — Kettering Health to End Medicare Advantage Contract with Anthem
    
    Link: https://ketteringhealth.org/kettering-health-to-end-medicare-advantage-contract-with-anthem/
  - (health) [WVU Medicine] 10/01/2026, 01:06 PM, +0000 UTC — WVU Health System welcomes five new hospitals
    
    Link: https://wvumedicine.org/news/article/wvu-medicine/front-page/wvu-health-system-welcomes-five-new-hospitals/
  - (health) [PBS] 10/05/2026, 06:50 PM, +0000 UTC — WATCH: Trump administration issues final rule on transparency in healthcare coverage
    
    Link: https://www.pbs.org/newshour/health/watch-trump-administration-issues-final-rule-on-transparency-in-healthcare-coverage
  - (health) [NPR] 10/05/2026, 09:00 AM, +0000 UTC — From floating saunas to clinical trials: How heat might help mental health
    
    Link: https://www.npr.org/2026/10/05/nx-s1-5979044/sauna-heat-therapy-mental-health-depression
  - (health) [North Carolina Health News] 10/07/2026, 08:30 AM, +0000 UTC — NC treasurer: Atrium affordability program could bankrupt state employees’ health plan
    
    Link: https://www.northcarolinahealthnews.org/2026/10/07/atrium-affordability-program-state-health-plan/
  - (health) [Vatican News] 10/01/2026, 12:07 PM, +0000 UTC — Pope’s October prayer intention: ‘For mental health ministry’
    
    Link: https://www.vaticannews.va/en/pope/news/2026-10/pope-leo-prayer-intention-october-for-mental-health-ministry.html
  - (health) [WPR] 10/02/2026, 10:00 AM, +0000 UTC — Wisconsin governor candidates offer opposing plans to address rising healthcare costs
    
    Link: https://www.wpr.org/news/wisconsin-governor-candidates-offer-opposing-plans-to-address-rising-healthcare-costs
  - (wellness) [Michigan Technological University] 10/02/2026, 06:21 PM, +0000 UTC — Michigan Tech Breaks Ground on Chang K. Park Center for Student Wellness
    
    Link: https://www.mtu.edu/news/2026/10/michigan-tech-breaks-ground-on-chang-k-park-center-for-student-wellness.html
  - (wellness) [Montana Free Press] 10/02/2026, 09:44 PM, +0000 UTC — Financial wellness is a practice
    
    Link: https://montanafreepress.org/2026/10/02/financial-wellness-is-a-practice/
  - (wellness) [WSJ] 10/02/2026, 02:57 PM, +0000 UTC — When Menopause Hit, I Went on a Wellness Binge
    
    Link: https://www.wsj.com/health/wellness/when-menopause-hit-i-went-on-a-wellness-binge-59f85e9d
  - (wellness) [RaleighNC.gov] 10/01/2026, 10:42 PM, +0000 UTC — Raleigh Parks Launches Fall Health and Wellness Pilot Classes
    
    Link: https://raleighnc.gov/parks-and-recreation/news/raleigh-parks-launches-fall-health-and-wellness-pilot-classes
  - (wellness) [Pew Research Center] 10/07/2026, 01:48 PM, +0000 UTC — What Do Health and Wellness Influencers Post About?
    
    Link: https://www.pewresearch.org/data-labs/2026/10/07/what-do-health-and-wellness-influencers-post-about/
  - (wellness) [San Bernardino County (.gov)] 10/01/2026, 08:57 PM, +0000 UTC — County invites community to free Fall Wellness Extravaganza
    
    Link: https://main.sbcounty.gov/2026/10/01/county-invites-community-to-free-fall-wellness-extravaganza/
  - (wellness) [13WHAM-TV] 10/03/2026, 03:32 AM, +0000 UTC — Rochester police introduce first-ever wellness dog
    
    Link: https://13wham.com/news/local/rochester-police-introduce-first-ever-wellness-dog-benson-therapy-rpd-wellness-unit-trauma
  - (wellness) [Condé Nast Traveler] 09/30/2026, 09:32 PM, +0000 UTC — 20 Years After Eat, Pray, Love, Bali Is Still Worth a Wellness Trip—Here's Where
    
    Link: https://www.cntraveler.com/story/20-years-after-eat-pray-love-bali-is-still-worth-a-wellness-trip
  - (wellness) [News at IU] 10/01/2026, 10:15 PM, +0000 UTC — Wellness Week: Take care of you!: Office of Student Life
    
    Link: https://news.iu.edu/studentlife/live/news/53683-wellness-week-take-care-of-you
  - (wellness) [Purdue University] 10/06/2026, 09:04 AM, +0000 UTC — Explore benefits, wellness resources at Wednesday’s Your Path Wellness Fair
    
    Link: https://www.purdue.edu/newsroom/purduetoday/2026/Q4/explore-benefits-wellness-resources-at-wednesdays-your-path-wellness-fair
  - (wellness) [MPR News] 10/07/2026, 06:22 AM, +0000 UTC — Improve your health habits with Wellness Wednesday
    
    Link: https://www.mprnews.org/episode/2026/10/07/improve-your-health-habits-with-wellness-wednesday
  - (wellness) [CU Denver News] 10/06/2026, 03:55 AM, +0000 UTC — CU Denver’s First Wellness Week Will Happen Oct. 12 Through 16
    
    Link: https://news.ucdenver.edu/cu-denvers-first-wellness-week-will-happen-oct-12-through-16/
  - (medical study) [Daily Bruin] 10/04/2026, 04:43 AM, +0000 UTC — UCLA alumnus turns medical school frustrations into AI study app ‘Neural Consult’
    
    Link: https://dailybruin.com/2026/10/03/ucla-alumnus-turns-medical-school-frustrations-into-ai-study-app-neural-consult
  - (medical study) [Nature] 10/02/2026, 11:48 AM, +0000 UTC — Urine cell-free RNA for bladder cancer detection and treatment response prediction
    
    Link: https://www.nature.com/articles/s41591-026-04673-3
  - (medical study) [Stanford Medicine] 10/05/2026, 11:10 PM, +0000 UTC — Stanford University professor Karl Deisseroth wins 2026 Nobel Prize in physiology or medicine
    
    Link: https://med.stanford.edu/news/all-news/2026/10/deisseroth-nobel-prize.html
  - (medical study) [PBS] 10/04/2026, 09:00 PM, +0000 UTC — WATCH: 3 scientists win Nobel Prize in medicine for studying mysteries of the brain
    
    Link: https://www.pbs.org/newshour/health/watch-live-winner-of-the-2026-nobel-prize-in-medicine-is
  - (medical study) [American Psychological Association (APA)] 10/01/2026, 01:17 PM, +0000 UTC — The hidden harms of medical gaslighting
    
    Link: https://www.apa.org/monitor/2026/10/harms-medical-gaslighting
  - (medical study) [ABC7 San Francisco] 10/05/2026, 04:58 PM, +0000 UTC — Karl Deisseroth: Stanford professor wins Nobel Prize in Medicine for optogenetics, new way to study brain using light
    
    Link: https://abc7news.com/post/karl-deisseroth-stanford-professor-wins-nobel-prize-medicine-optogenetics-new-study-brain-using-light/19910448/
  - (medical study) [Harvard Health] 10/02/2026, 06:23 PM, +0000 UTC — People who walk more or walk faster live longer, study finds
    
    Link: https://www.health.harvard.edu/heart-health/people-who-walk-more-or-walk-faster-live-longer-study-finds
  - (medical study) [VCU News] 10/06/2026, 01:08 PM, +0000 UTC — Popular TikTok docs have big influence on Gen Z followers, new VCU research finds
    
    Link: https://news.vcu.edu/article/popular-tiktok-docs-have-big-influence-on-gen-z-followers-new-vcu-research-finds
  - (medical study) [NeuroNews International] 10/06/2026, 10:16 AM, +0000 UTC — NeuWire Medical announces US FDA IDE approval for STROKE-REWIRE pivotal study
    
    Link: https://neuronewsinternational.com/neuwire-medical-announces-us-fda-ide-approval-for-stroke-rewire-pivotal-study/
  - (medical study) [University of Cincinnati] 10/06/2026, 03:54 AM, +0000 UTC — UC emergency physician receives $2.5 million NIH research grant
    
    Link: https://www.uc.edu/news/articles/2026/10/n21435212.html
  - (medical study) [Froedtert & MCW] 10/06/2026, 04:58 PM, +0000 UTC — Froedtert ThedaCare Hospitals Recognized by Vizient as 2026 Birnbaum Quality Leadership Top Performers
    
    Link: https://www.froedtert.com/news/froedtert-thedacare-hospitals-recognized-vizient-2026-birnbaum-quality-leadership-top
  - (medical study) [Lockton] 10/07/2026, 05:19 AM, +0000 UTC — Lockton SAGE for Clinical Trials Simplifies Global Trial Insurance Management
    
    Link: https://global.lockton.com/us/en/news-insights/lockton-sage-for-clinical-trials-simplifies-global-trial-insurance-management
  - (clinical trial health) [HHS.gov] 09/30/2026, 06:26 PM, +0000 UTC — HHS Launches SURPASS and New Efforts to Accelerate Faster, Smarter Clinical Trials
    
    Link: https://www.hhs.gov/press-room/hhs-arpa-h-launch-surpass-modernize-clinical-trials.html
  - (clinical trial health) [UT News] 09/30/2026, 07:00 PM, +0000 UTC — UT Takes Leading Role in National Effort To Modernize Clinical Trials
    
    Link: https://news.utexas.edu/2026/09/30/ut-takes-leading-role-in-national-effort-to-modernize-clinical-trials/
  - (clinical trial health) [Axios] 09/30/2026, 10:22 PM, +0000 UTC — Exclusive: HHS launches project to speed up clinical trials
    
    Link: https://www.axios.com/2026/09/30/hhs-clinical-trials-redesign
  - (clinical trial health) [University of Nevada, Las Vegas | UNLV] 10/05/2026, 10:49 PM, +0000 UTC — Clinical Research Trials Bring Innovative Women’s Healthcare to Southern Nevada
    
    Link: https://www.unlv.edu/news/article/clinical-research-trials-bring-innovative-womens-healthcare-southern-nevada
  - (clinical trial health) [BioSpace] 10/01/2026, 02:40 PM, +0000 UTC — US government launches AI-driven programs to overhaul clinical trials
    
    Link: https://www.biospace.com/drug-development/us-government-launches-ai-driven-programs-to-overhaul-clinical-trials
  - (clinical trial health) [STAT] 09/30/2026, 08:11 PM, +0000 UTC — HHS announces new efforts to speed up, expand clinical trials with AI
    
    Link: https://www.statnews.com/2026/09/30/hhs-arpa-h-clinical-trials-artificial-intelligence-surpass-program/
  - (clinical trial health) [Pfizer] 10/03/2026, 03:48 AM, +0000 UTC — How AI Is Helping Match Patients to Clinical Trials Faster
    
    Link: https://www.pfizer.com/news/articles/how_ai_is_helping_match_patients_to_clinical_trials_faster
  - (clinical trial health) [UNC Health] 10/01/2026, 07:29 PM, +0000 UTC — UNC Health Advances Gene Therapy Research for Rett Syndrome
    
    Link: https://news.unchealthcare.org/2026/10/unc-health-advances-gene-therapy-research-for-rett-syndrome/
  - (clinical trial health) [Healthcare IT News] 10/06/2026, 02:49 PM, +0000 UTC — Ochsner uses AI to widen clinical trial screening
    
    Link: https://www.healthcareitnews.com/news/ochsner-uses-ai-widen-clinical-trial-screening
  - (clinical trial health) [BioPharma Dive] 10/01/2026, 04:07 PM, +0000 UTC — HHS kicks off new programs to speed clinical trials as Chinese competition looms
    
    Link: https://www.biopharmadive.com/news/hhs-clinical-trial-speed-arpa-h-drug-testing/831909/
  - (clinical trial health) [KUT] 10/01/2026, 10:00 AM, +0000 UTC — RFK Jr. announces partnership with Dell Medical School to boost clinical trials in the US
    
    Link: https://www.kut.org/health/2026-10-01/austin-tx-rfk-jr-hhs-clinical-trials-ut-dell-medical-school
  - (clinical trial health) [Medical Daily] 10/02/2026, 02:30 PM, +0000 UTC — HHS Launches AI Clinical Trial Program Without a Disclosed Budget, Leaving Key Patient Data Privacy Questions Open
    
    Link: https://www.medicaldaily.com/hhs-arpa-h-surpass-ai-clinical-trials-budget-privacy-479420
  - (FDA recall health) [U.S. Food and Drug Administration (.gov)] 10/05/2026, 12:00 AM, +0000 UTC — Outbreak Investigation of E. coli O145:H28: Frozen Blueberries (July 2026)
    
    Link: https://www.fda.gov/food/outbreaks-foodborne-illness/outbreak-investigation-e-coli-o145h28-frozen-blueberries-july-2026
  - (FDA recall health) [ABC7 Eyewitness News] 10/05/2026, 10:05 PM, +0000 UTC — FDA recalls 122,000 cases of Gatorade sold across 37 states
    
    Link: https://abc7ny.com/story/fda-recalls-122000-cases-gatorade-undeclared-dyes/19910004/
  - (FDA recall health) [The New York Times] 10/03/2026, 09:01 PM, +0000 UTC — F.D.A. Classifies Salad Dressing Recall to Highest Health Risk
    
    Link: https://www.nytimes.com/2026/10/03/health/fda-recall-salata-salad-dressing-salmonella.html
  - (FDA recall health) [ABC News - Breaking News, Latest News and Videos] 10/06/2026, 03:02 AM, +0000 UTC — Over 122K cases of Gatorade recalled due to undeclared food dyes, FDA says
    
    Link: https://abcnews.com/GMA/Food/122k-cases-gatorade-recalled-due-undeclared-food-dyes/story?id=137002347
  - (FDA recall health) [Health.com] 10/05/2026, 04:38 PM, +0000 UTC — FDA Announces Gatorade Recall in 37 States After Bottles Were Found to Have Undeclared Food Dyes
    
    Link: https://www.health.com/gatorade-recall-october-2026-12159566
  - (FDA recall health) [El Paso Times] 10/06/2026, 11:50 AM, +0000 UTC — FDA recalls Gatorade in Texas over unlisted food coloring
    
    Link: https://www.elpasotimes.com/story/news/texasregion/2026/10/06/gatorade-recall-in-texas-lot-numbers-products-health-risks/92106375007/
  - (FDA recall health) [Good Housekeeping] 10/02/2026, 06:29 PM, +0000 UTC — FDA Elevates Salad Dressing Recall to Highest Risk Level—Here’s Everything You Need to Know
    
    Link: https://www.goodhousekeeping.com/food-recipes/a73996982/fda-salad-dressing-recall/
  - (FDA recall health) [Medscape] 10/06/2026, 01:43 PM, +0000 UTC — FDA Recall Problems Raise Questions About Safety, Liability
    
    Link: https://www.medscape.com/viewarticle/fda-device-recall-problems-raise-questions-about-patient-2026a10011cz
  - (FDA recall health) [Healthline] 10/02/2026, 08:02 PM, +0000 UTC — FDA Issues Class II Blood Pressure Medication Recall, Over 13,000 Bottles Affected
    
    Link: https://www.healthline.com/health-news/blood-pressure-medication-nationwide-recall-fda
  - (FDA recall health) [Montgomery Advertiser] 10/05/2026, 07:01 PM, +0000 UTC — Gatorade recall 2026 expands to Alabama. Check these bottles
    
    Link: https://www.montgomeryadvertiser.com/story/news/2026/10/05/fda-announces-major-gatorade-recall-2026-is-alabama-affected/92107184007/
  - (FDA recall health) [Detroit Free Press] 10/06/2026, 05:55 PM, +0000 UTC — Gatorade sold in Michigan recalled. Why you should return it
    
    Link: https://www.freep.com/story/news/health/2026/10/06/gatorade-recall-michigan-fda-food-dye/92118542007/
  - (FDA recall health) [The Healthy] 10/05/2026, 07:26 PM, +0000 UTC — Sports Drink Recall: FDA Flags Issue With Four Popular Flavors
    
    Link: https://www.thehealthy.com/news/gatorade-sports-drink-recall-october-2026/