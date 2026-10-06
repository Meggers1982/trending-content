# LIVE SIGNAL DATA — SerpAPI Pre-Fetch
The following signals were fetched from SerpAPI Google News and SerpAPI Google Trends immediately before this pipeline run. Treat Google Trends as AVAILABLE when this section contains a Google Trends block. Use it as the primary search_velocity input for Skills 01–05 (Signal Listener through Trend Strength Scorer). Use the Google News Radar as the broad discovery layer for news-led health topics, including topics that do not yet appear in Google Trends. Prioritize topics with convergence across News, Trends, primary/institutional sources, and credible publisher coverage.

# SIGNAL INTEGRITY WARNING

SerpAPI stopped answering for google_news partway through this run, so that signal is incomplete below. Other sources ran normally — do not read the gap as an absence of activity. 2 Google News queries were answered via the lighter google_news_light engine instead (labeled [light] below); those articles carry fewer fields than a normal google_news result and should not be treated as full-fidelity.

Treat absence of signal as unknown, not as absence of activity. Say so in signal_summary.notes and lower confidence accordingly.

## Google Trends — Trending Now (US / Health, real-time)
Terms with a "Why:" line have a confirmed real-world news story driving the spike; terms without one are a real-time signal only, not yet grounded in a specific story.
  - national coaches day
    Why: "MADD Launches New Coaches' Guide to Help Prevent Underage Drinking and Substance Use Among Student-Athletes on National Coaches Day" — PR Newswire
  - pittsburgh measles outbreak
    Why: "PA Doctor: Every day I’m seeing the pain & the suffering" — CNN

## Google Trends — 7-Day Interest (US)
  - **health**: latest=97, peak=100, 7d-delta=+7
    Rising related: health insurance giant, when is open enrollment for health insurance 2027, united health care provider portal, scan health plan, devoted health, costco health insurance, health equity login, health care
  - **wellness**: latest=37, peak=100, 7d-delta=-5
    Rising related: heal wellness lubbock, stc wellness city, heal wellness, prana wellness club, prana wellness, routine wellness shampoo and conditioner reviews, a cure for wellness, bon secours wellness arena
  - **nutrition**: latest=93, peak=100, 7d-delta=-4
    Rising related: supplemental nutrition assistance program changes, supplemental nutrition assistance program payment changes, kona ice nutrition, supplemental nutrition assistance program, tradesman nutrition shred reviews, tradesman nutrition shred, tradesman nutrition, top tourist attractions in paris
  - **fitness**: latest=31, peak=100, 7d-delta=+0
    Rising related: george armstrong fitness, luke combs fitness transformation, fitness centre, physical fitness program, how to cancel planet fitness membership online, planet fitness, la fitness, crunch
  - **food safety**: latest=80, peak=100, 7d-delta=-8
    Rising related: walmart product recalls safety notice, chipotle food safety 7, heavy metals in cat food, inspectors normally focus on conformity to this system, a food handlers duties regarding food safety include all of the following practices except to, when a product has been declared unsafe to serve to customers, fifo refers to, what is food safety
  - **diet**: latest=72, peak=100, 7d-delta=-6
    Rising related: merv griffin, diet sprite meaning, mind diet brain aging study, diet beverages vs water weight loss, dr sean o'mara diet, designates a diet product, sean o'mara diet, sean omara diet
  - **weight loss**: latest=26, peak=100, 7d-delta=-2
    Rising related: six month tirzepatide weight loss, diet beverages vs water weight loss, eli lilly retatrutide weight loss, cbl-514 weight loss injection, explain how zepbound works for weight loss and its primary side effects, dj khaled weight loss, eli lilly weight loss results, explain how retatrutide works for weight loss compared to ozempic
  - **mental health**: latest=84, peak=100, 7d-delta=-11
    Rising related: lane johnson mental health, is october mental health awareness month, october mental health awareness month, mental health awareness week, world mental health day 2026, world mental health day, how to bake a cake, best time to visit maldives
  - **gut health**: latest=56, peak=100, 7d-delta=-1
    Rising related: top tourist attractions in paris, fermented foods list for gut health, fiber rich foods, list of fermented foods for gut health, celtara gut health, how to restore gut health, gut health in spanish, magnesium for gut health

Top rising related queries from Google Trends:
  - health insurance giant
  - when is open enrollment for health insurance 2027
  - united health care provider portal
  - scan health plan
  - devoted health
  - costco health insurance
  - health equity login
  - health care
  - heal wellness lubbock
  - stc wellness city
  - heal wellness
  - prana wellness club
  - prana wellness
  - routine wellness shampoo and conditioner reviews
  - a cure for wellness
  - bon secours wellness arena
  - supplemental nutrition assistance program changes
  - supplemental nutrition assistance program payment changes
  - kona ice nutrition
  - supplemental nutrition assistance program

## Google News Radar — Recent Health Topics (139 unique across 12 queries; showing 60; 19 tagged [light] came from the google_news_light fallback and carry fewer fields)
Treat these headlines as the broad radar of news-led health topics. The Signal Listener must consider this radar before narrowing to retained candidates.
  - (health) [NJ.gov] 10/02/2026, 09:49 PM, +0000 UTC — NJ Reminds Residents to Continue to Take Precautions Against Mosquito-Borne Illnesses
    
    Link: https://www.nj.gov/health/news/2026/approved/20261002a.shtml
  - (health) [World Health Organization (WHO)] 10/02/2026, 09:44 AM, +0000 UTC — New WHO estimates show changing global health landscape
    
    Link: https://www.who.int/news/item/02-10-2026-new-who-estimates-show-changing-global-health-landscape
  - (health) [Alabama Governor's Office (.gov)] 10/01/2026, 04:48 PM, +0000 UTC — Governor Ivey Announces Additional Alabama Rural Health Transformation Program Grants Totaling Nearly $55 Million
    
    Link: https://governor.alabama.gov/newsroom/2026/10/governor-ivey-announces-additional-alabama-rural-health-transformation-program-grants-totaling-nearly-55-million/
  - (health) [KFF] 09/30/2026, 07:00 AM, +0000 UTC — What Are the Recent Trends in Health Sector Employment
    
    Link: https://www.kff.org/health-costs/what-impact-has-the-coronavirus-pandemic-had-on-health-care-employment/
  - (health) [HHS.gov] 10/05/2026, 03:30 PM, +0000 UTC — New Regulations Make It Easier to Find, Compare, and Report Healthcare Pricing and Coverage Information
    
    Link: https://www.hhs.gov/press-room/cms-finalizes-healthcare-price-transparency-rules.html
  - (health) [NPR] 10/05/2026, 09:00 AM, +0000 UTC — From floating saunas to clinical trials: How heat might help mental health
    
    Link: https://www.npr.org/2026/10/05/nx-s1-5979044/sauna-heat-therapy-mental-health-depression
  - (health) [WVU Medicine] 10/01/2026, 01:06 PM, +0000 UTC — WVU Health System welcomes five new hospitals
    
    Link: https://wvumedicine.org/news/article/wvu-medicine/front-page/wvu-health-system-welcomes-five-new-hospitals/
  - (health) [PBS] 10/05/2026, 06:50 PM, +0000 UTC — WATCH: Trump administration issues final rule on transparency in healthcare coverage
    
    Link: https://www.pbs.org/newshour/health/watch-trump-administration-issues-final-rule-on-transparency-in-healthcare-coverage
  - (health) [Vatican News] 10/01/2026, 12:07 PM, +0000 UTC — Pope’s October prayer intention: ‘For mental health ministry’
    
    Link: https://www.vaticannews.va/en/pope/news/2026-10/pope-leo-prayer-intention-october-for-mental-health-ministry.html
  - (health) [KFF Health News] 09/30/2026, 09:02 AM, +0000 UTC — US Poised To Boot Legal Immigrants From Medicaid, Including Refugees and Sex-Trafficking Victims
    
    Link: https://kffhealthnews.org/medicaid/immigrants-kicked-off-medicaid-refugees-asylum-seekers-trump-big-beautiful-bill-cbo-2/
  - (health) [GovExec.com] 10/02/2026, 06:38 PM, +0000 UTC — Federal employees’ health insurance premiums to rise by double digits for third straight year
    
    Link: https://www.govexec.com/pay-benefits/2026/10/federal-employees-health-insurance-premiums-rise-double-digits-third-straight-year/416395/
  - (health) [MPR News] 09/29/2026, 11:54 PM, +0000 UTC — For the first time, Minnesota has K-12 health standards. Here’s what to know
    
    Link: https://www.mprnews.org/story/2026/09/29/minnesotas-new-k-12-health-standards-approved
  - (wellness) [Michigan Technological University] 10/02/2026, 06:21 PM, +0000 UTC — Michigan Tech Breaks Ground on Chang K. Park Center for Student Wellness
    
    Link: https://www.mtu.edu/news/2026/10/michigan-tech-breaks-ground-on-chang-k-park-center-for-student-wellness.html
  - (wellness) [Montana Free Press] 10/02/2026, 09:44 PM, +0000 UTC — Financial wellness is a practice
    
    Link: https://montanafreepress.org/2026/10/02/financial-wellness-is-a-practice/
  - (wellness) [WSJ] 10/02/2026, 02:57 PM, +0000 UTC — When Menopause Hit, I Went on a Wellness Binge
    
    Link: https://www.wsj.com/health/wellness/when-menopause-hit-i-went-on-a-wellness-binge-59f85e9d
  - (wellness) [RaleighNC.gov] 10/01/2026, 10:42 PM, +0000 UTC — Raleigh Parks Launches Fall Health and Wellness Pilot Classes
    
    Link: https://raleighnc.gov/parks-and-recreation/news/raleigh-parks-launches-fall-health-and-wellness-pilot-classes
  - (wellness) [13WHAM-TV] 10/03/2026, 03:32 AM, +0000 UTC — Rochester police introduce first-ever wellness dog
    
    Link: https://13wham.com/news/local/rochester-police-introduce-first-ever-wellness-dog-benson-therapy-rpd-wellness-unit-trauma
  - (wellness) [San Bernardino County (.gov)] 10/01/2026, 08:57 PM, +0000 UTC — County invites community to free Fall Wellness Extravaganza
    
    Link: https://main.sbcounty.gov/2026/10/01/county-invites-community-to-free-fall-wellness-extravaganza/
  - (wellness) [Condé Nast Traveler] 09/30/2026, 09:32 PM, +0000 UTC — 20 Years After Eat, Pray, Love, Bali Is Still Worth a Wellness Trip—Here's Where
    
    Link: https://www.cntraveler.com/story/20-years-after-eat-pray-love-bali-is-still-worth-a-wellness-trip
  - (wellness) [News at IU] 10/01/2026, 10:15 PM, +0000 UTC — Wellness Week: Take care of you!: Office of Student Life
    
    Link: https://news.iu.edu/studentlife/live/news/53683-wellness-week-take-care-of-you
  - (wellness) [Purdue University] 10/06/2026, 09:04 AM, +0000 UTC — Explore benefits, wellness resources at Wednesday’s Your Path Wellness Fair
    
    Link: https://www.purdue.edu/newsroom/purduetoday/2026/Q4/explore-benefits-wellness-resources-at-wednesdays-your-path-wellness-fair
  - (wellness) [People.com] 09/30/2026, 03:11 PM, +0000 UTC — Julianne Hough on Beauty, Wellness and Entering Her ‘Leading Lady Era’ (Exclusive)
    
    Link: https://people.com/julianne-hough-talks-beauty-wellness-dancing-with-the-stars-exclusive-12148999
  - (wellness) [CU Denver News] 10/06/2026, 03:55 AM, +0000 UTC — CU Denver’s First Wellness Week Will Happen Oct. 12 Through 16
    
    Link: https://news.ucdenver.edu/cu-denvers-first-wellness-week-will-happen-oct-12-through-16/
  - (wellness) [The Pennsylvania State University] 10/02/2026, 01:06 PM, +0000 UTC — Alumni’s gift to the School of Music aims to promote student wellness
    
    Link: https://www.psu.edu/news/arts-and-architecture/story/alumnis-gift-school-music-aims-promote-student-wellness
  - (medical study) [Daily Bruin] 10/04/2026, 04:43 AM, +0000 UTC — UCLA alumnus turns medical school frustrations into AI study app ‘Neural Consult’
    
    Link: https://dailybruin.com/2026/10/03/ucla-alumnus-turns-medical-school-frustrations-into-ai-study-app-neural-consult
  - (medical study) [Stanford Medicine] 09/29/2026, 06:57 PM, +0000 UTC — Researcher’s sudden death shows wearables’ potential as ‘check-engine light’
    
    Link: https://med.stanford.edu/news/insights/2026/09/sudden-cardiac-death-of-researcher-studying-wearables.html
  - (medical study) [PBS] 10/04/2026, 09:00 PM, +0000 UTC — WATCH: 3 scientists win Nobel Prize in medicine for studying mysteries of the brain
    
    Link: https://www.pbs.org/newshour/health/watch-live-winner-of-the-2026-nobel-prize-in-medicine-is
  - (medical study) [Nature] 10/02/2026, 11:48 AM, +0000 UTC — Urine cell-free RNA for bladder cancer detection and treatment response prediction
    
    Link: https://www.nature.com/articles/s41591-026-04673-3
  - (medical study) [Harvard Health] 10/02/2026, 07:00 AM, +0000 UTC — People who walk more or walk faster live longer, study finds
    
    Link: https://www.health.harvard.edu/heart-health/people-who-walk-more-or-walk-faster-live-longer-study-finds
  - (medical study) [ABC7 San Francisco] 10/05/2026, 04:58 PM, +0000 UTC — Karl Deisseroth: Stanford professor wins Nobel Prize in Medicine for optogenetics, new way to study brain using light
    
    Link: https://abc7news.com/post/karl-deisseroth-stanford-professor-wins-nobel-prize-medicine-optogenetics-new-study-brain-using-light/19910448/
  - (medical study) [Los Angeles Times] 10/05/2026, 03:00 PM, +0000 UTC — ER visits from foreign-born patients fell drastically during ICE raids, study finds
    
    Link: https://www.latimes.com/science/story/2026-10-05/er-visits-foreign-born-patients-fell-ice-raids-study
  - (medical study) [NeuroNews International] 10/06/2026, 10:16 AM, +0000 UTC — NeuWire Medical announces US FDA IDE approval for STROKE-REWIRE pivotal study
    
    Link: https://neuronewsinternational.com/neuwire-medical-announces-us-fda-ide-approval-for-stroke-rewire-pivotal-study/
  - (medical study) [University of Cincinnati] 10/06/2026, 03:54 AM, +0000 UTC — UC emergency physician receives $2.5 million NIH research grant
    
    Link: https://www.uc.edu/news/articles/2026/10/n21435212.html
  - (medical study) [Marijuana Moment] 10/02/2026, 12:02 PM, +0000 UTC — Medical Marijuana Helps People With Autism Reduce Anxiety And Depression, Government Study Shows
    
    Link: https://www.marijuanamoment.net/medical-marijuana-helps-people-with-autism-reduce-anxiety-and-depression-government-study-shows/
  - (medical study) [News-Medical] 10/01/2026, 06:29 PM, +0000 UTC — Study links immune status to herpesvirus retinitis progression
    
    Link: https://www.news-medical.net/news/20261001/Study-links-immune-status-to-herpesvirus-retinitis-progression.aspx
  - (medical study) [Foley Hoag] 10/01/2026, 02:21 PM, +0000 UTC — When FDA Oversees Trials Overseas: Foreign Clinical Trial Considerations
    
    Link: https://foleyhoag.com/news-and-insights/publications/alerts-and-updates/2026/september/when-fda-oversees-trials-overseas-foreign-clinical-trial-considerations/
  - (clinical trial health) [HHS.gov] 09/30/2026, 06:26 PM, +0000 UTC — HHS Launches SURPASS and New Efforts to Accelerate Faster, Smarter Clinical Trials
    
    Link: https://www.hhs.gov/press-room/hhs-arpa-h-launch-surpass-modernize-clinical-trials.html
  - (clinical trial health) [UT News] 09/30/2026, 07:00 PM, +0000 UTC — UT Takes Leading Role in National Effort To Modernize Clinical Trials
    
    Link: https://news.utexas.edu/2026/09/30/ut-takes-leading-role-in-national-effort-to-modernize-clinical-trials/
  - (clinical trial health) [Axios] 09/30/2026, 10:22 PM, +0000 UTC — Exclusive: HHS launches project to speed up clinical trials
    
    Link: https://www.axios.com/2026/09/30/hhs-clinical-trials-redesign
  - (clinical trial health) [BioSpace] 10/01/2026, 02:40 PM, +0000 UTC — US government launches AI-driven programs to overhaul clinical trials
    
    Link: https://www.biospace.com/drug-development/us-government-launches-ai-driven-programs-to-overhaul-clinical-trials
  - (clinical trial health) [Pfizer] 10/03/2026, 03:48 AM, +0000 UTC — How AI Is Helping Match Patients to Clinical Trials Faster
    
    Link: https://www.pfizer.com/news/articles/how_ai_is_helping_match_patients_to_clinical_trials_faster
  - (clinical trial health) [STAT] 09/30/2026, 08:11 PM, +0000 UTC — HHS announces new efforts to speed up, expand clinical trials with AI
    
    Link: https://www.statnews.com/2026/09/30/hhs-arpa-h-clinical-trials-artificial-intelligence-surpass-program/
  - (clinical trial health) [OHSU News] 09/30/2026, 03:11 PM, +0000 UTC — OHSU secures $4.6 million to expand clinical trials in underserved rural communities
    
    Link: https://news.ohsu.edu/2026/09/30/ohsu-secures-4-6-million-to-expand-clinical-trials-in-underserved-rural-communities
  - (clinical trial health) [Healthcare IT News] 10/06/2026, 04:05 PM, +0000 UTC — Ochsner uses AI to widen clinical trial screening
    
    Link: https://www.healthcareitnews.com/news/ochsner-uses-ai-widen-clinical-trial-screening
  - (clinical trial health) [World Health Organization (WHO)] 09/30/2026, 01:27 PM, +0000 UTC — Kazakhstan Summer School strengthens national clinical research capacity
    
    Link: https://www.who.int/news/item/30-09-2026-kazakhstan-summer-school-strengthens-national-clinical-research-capacity
  - (clinical trial health) [KUT] 10/01/2026, 10:00 AM, +0000 UTC — RFK Jr. announces partnership with Dell Medical School to boost clinical trials in the US
    
    Link: https://www.kut.org/health/2026-10-01/austin-tx-rfk-jr-hhs-clinical-trials-ut-dell-medical-school
  - (clinical trial health) [BioPharma Dive] 10/01/2026, 04:07 PM, +0000 UTC — HHS kicks off new programs to speed clinical trials as Chinese competition looms
    
    Link: https://www.biopharmadive.com/news/hhs-clinical-trial-speed-arpa-h-drug-testing/831909/
  - (clinical trial health) [Fierce Biotech] 09/29/2026, 07:04 PM, +0000 UTC — Canadian $5M accelerated clinical trial program cuts start-up to 45 days
    
    Link: https://www.fiercebiotech.com/cro/canadian-5m-accelerated-clinical-trial-program-cuts-start-45-days
  - (FDA recall health) [The New York Times] 10/03/2026, 09:01 PM, +0000 UTC — F.D.A. Classifies Salad Dressing Recall to Highest Health Risk
    
    Link: https://www.nytimes.com/2026/10/03/health/fda-recall-salata-salad-dressing-salmonella.html
  - (FDA recall health) [ABC7 Eyewitness News] 10/05/2026, 10:05 PM, +0000 UTC — FDA recalls 122,000 cases of Gatorade sold across 37 states
    
    Link: https://abc7ny.com/story/fda-recalls-122000-cases-gatorade-undeclared-dyes/19910004/
  - (FDA recall health) [ABC News - Breaking News, Latest News and Videos] 10/06/2026, 03:02 AM, +0000 UTC — Over 122K cases of Gatorade recalled due to undeclared food dyes, FDA says
    
    Link: https://abcnews.com/GMA/Food/122k-cases-gatorade-recalled-due-undeclared-food-dyes/story?id=137002347
  - (FDA recall health) [AARP] 09/29/2026, 10:15 PM, +0000 UTC — FDA Announces Nationwide Recall of Chlorthalidone Tablets
    
    Link: https://www.aarp.org/health/conditions-treatments/blood-pressure-medication-recall-september-2026/
  - (FDA recall health) [El Paso Times] 10/06/2026, 11:50 AM, +0000 UTC — FDA recalls Gatorade in Texas over unlisted food coloring
    
    Link: https://www.elpasotimes.com/story/news/texasregion/2026/10/06/gatorade-recall-in-texas-lot-numbers-products-health-risks/92106375007/
  - (FDA recall health) [Good Housekeeping] 10/02/2026, 06:29 PM, +0000 UTC — FDA Elevates Salad Dressing Recall to Highest Risk Level—Here’s Everything You Need to Know
    
    Link: https://www.goodhousekeeping.com/food-recipes/a73996982/fda-salad-dressing-recall/
  - (FDA recall health) [USA Today] 09/30/2026, 06:09 PM, +0000 UTC — Medication used for high blood pressure recalled. Here's what to know
    
    Link: https://www.usatoday.com/story/news/health/2026/09/30/inventia-healthcare-chlorthalidone-recall/92019617007/
  - (FDA recall health) [Medscape] 10/06/2026, 01:43 PM, +0000 UTC — FDA Recall Problems Raise Questions About Safety, Liability
    
    Link: https://www.medscape.com/viewarticle/fda-device-recall-problems-raise-questions-about-patient-2026a10011cz
  - (FDA recall health) [Montgomery Advertiser] 10/05/2026, 07:01 PM, +0000 UTC — Gatorade recall 2026 expands to Alabama. Check these bottles
    
    Link: https://www.montgomeryadvertiser.com/story/news/2026/10/05/fda-announces-major-gatorade-recall-2026-is-alabama-affected/92107184007/
  - (FDA recall health) [Healthline] 10/02/2026, 08:02 PM, +0000 UTC — FDA Issues Class II Blood Pressure Medication Recall, Over 13,000 Bottles Affected
    
    Link: https://www.healthline.com/health-news/blood-pressure-medication-nationwide-recall-fda
  - (FDA recall health) [NBC News] 10/02/2026, 10:01 AM, +0000 UTC — FDA issues highest-level recall of salad dressing
    
    Link: https://www.nbcnews.com/video/shorts/fda-issues-highest-level-recall-of-salad-dressing-270903877823
  - (FDA recall health) [Health.com] 10/05/2026, 04:38 PM, +0000 UTC — FDA Announces Gatorade Recall in 37 States After Bottles Were Found to Have Undeclared Food Dyes
    
    Link: https://www.health.com/gatorade-recall-october-2026-12159566