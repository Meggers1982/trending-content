# LIVE SIGNAL DATA — SerpAPI Pre-Fetch
The following signals were fetched from SerpAPI Google News and SerpAPI Google Trends immediately before this pipeline run. Treat Google Trends as AVAILABLE when this section contains a Google Trends block. Use it as the primary search_velocity input for Skills 01–05 (Signal Listener through Trend Strength Scorer). Use the Google News Radar as the broad discovery layer for news-led health topics, including topics that do not yet appear in Google Trends. Prioritize topics with convergence across News, Trends, primary/institutional sources, and credible publisher coverage.

## Google Trends — 7-Day Interest (US)
  - **health**: latest=35, peak=100, 7d-delta=-1
    Rising related: health insurance giant nyt, health insurance giant, when is open enrollment for health insurance 2027, health insurance agency, ez health, essentia health, health care fraud, united health care provider portal
  - **wellness**: latest=28, peak=100, 7d-delta=-6
    Rising related: tiktok wellness trends botulism warning, julianne hough beauty and wellness, stc wellness city, heal wellness lubbock, bon secours wellness arena, prana wellness club, heal wellness, prana wellness
  - **nutrition**: latest=72, peak=100, 7d-delta=-12
    Rising related: supplemental nutrition assistance program changes, supplemental nutrition assistance program payment changes, kona ice nutrition, supplemental nutrition assistance program, tradesman nutrition shred reviews, tradesman nutrition shred, morphogen nutrition, tradesman nutrition
  - **fitness**: latest=28, peak=100, 7d-delta=-3
    Rising related: george armstrong fitness, luke combs fitness transformation, fitness centre, physical fitness program, city fitness hoboken, how to cancel planet fitness membership online, vasa fitness dearborn, planet
  - **food safety**: latest=35, peak=100, 7d-delta=-12
    Rising related: walmart product recalls safety notice, cat food heavy metals, heavy metals in cat food, when a product has been declared unsafe to serve to customers, premier food safety login, chipotle food safety 7, what agency publishes the food code, one of the most important reasons for using only reliable water sources is to reduce
  - **diet**: latest=75, peak=100, 7d-delta=-3
    Rising related: merv griffin, wc fields, river phoenix, merv, ny giant, mind diet brain aging study, getty images, met halfway
  - **weight loss**: latest=27, peak=100, 7d-delta=+0
    Rising related: six month tirzepatide weight loss, cbl-514 weight loss injection, cagrisema and zepbound weight loss results, eli lilly retatrutide weight loss, dj khaled weight loss, new weight loss drug, amy schumer weight loss, alison hammond weight loss
  - **mental health**: latest=26, peak=100, 7d-delta=-1
    Rising related: christa pike mental health, the kids mental health foundation, kids mental health foundation, is october mental health awareness month, october mental health awareness month, world mental health day 2026, mental illness awareness week, mens mental health awareness month
  - **gut health**: latest=48, peak=100, 7d-delta=-23
    Rising related: gut health in spanish, juice recipes for gut health, align probiotics, is apple cider vinegar good for gut health, anti inflammatory diet, best mushroom coffee for gut health, bioma, is honey good for gut health

Top rising related queries from Google Trends:
  - health insurance giant nyt
  - health insurance giant
  - when is open enrollment for health insurance 2027
  - health insurance agency
  - ez health
  - essentia health
  - health care fraud
  - united health care provider portal
  - tiktok wellness trends botulism warning
  - julianne hough beauty and wellness
  - stc wellness city
  - heal wellness lubbock
  - bon secours wellness arena
  - prana wellness club
  - heal wellness
  - prana wellness
  - supplemental nutrition assistance program changes
  - supplemental nutrition assistance program payment changes
  - kona ice nutrition
  - supplemental nutrition assistance program

## Google News Radar — Recent Health Topics (144 unique across 12 queries; showing 60)
Treat these headlines as the broad radar of news-led health topics. The Signal Listener must consider this radar before narrowing to retained candidates.
  - (health) [World Health Organization (WHO)] 10/02/2026, 09:44 AM, +0000 UTC — New WHO estimates show changing global health landscape
    
    Link: https://www.who.int/news/item/02-10-2026-new-who-estimates-show-changing-global-health-landscape
  - (health) [Alabama Governor's Office (.gov)] 10/01/2026, 04:48 PM, +0000 UTC — Governor Ivey Announces Additional Alabama Rural Health Transformation Program Grants Totaling Nearly $55 Million
    
    Link: https://governor.alabama.gov/newsroom/2026/10/governor-ivey-announces-additional-alabama-rural-health-transformation-program-grants-totaling-nearly-55-million/
  - (health) [Department of Justice (.gov)] 10/01/2026, 07:00 AM, +0000 UTC — Texas Mental Health Clinic Owner Convicted in $26M Scheme to Defraud Military Health Benefits Program
    
    Link: https://www.justice.gov/opa/pr/texas-mental-health-clinic-owner-convicted-26m-scheme-defraud-military-health-benefits
  - (health) [KFF] 09/30/2026, 07:00 AM, +0000 UTC — What Are the Recent Trends in Health Sector Employment
    
    Link: https://www.kff.org/health-costs/what-impact-has-the-coronavirus-pandemic-had-on-health-care-employment/
  - (health) [California State Portal | CA.gov] 09/28/2026, 06:48 PM, +0000 UTC — Governor Newsom signs legislation creating non-UPF label, other health bills advancing California’s nation-leading healthcare strategy
    
    Link: https://www.gov.ca.gov/2026/09/28/governor-newsom-signs-legislation-creating-non-upf-label-other-health-bills-advancing-californias-nation-leading-healthcare-strategy/
  - (health) [Dartmouth] 09/29/2026, 05:25 PM, +0000 UTC — Historic $20 Million Gift to Launch Dartmouth Health at Home
    
    Link: https://home.dartmouth.edu/news/2026/09/historic-20-million-gift-launch-dartmouth-health-home
  - (health) [Center on Budget and Policy Priorities] 09/29/2026, 11:57 AM, +0000 UTC — Health Coverage Tracker: Millions of People Are Losing Coverage Following 2025 Republican Policy Changes
    
    Link: https://www.cbpp.org/research/health/health-coverage-tracker-millions-of-people-are-losing-coverage-following-2025
  - (health) [Think Global Health] 09/29/2026, 07:00 AM, +0000 UTC — Tracking the "America First" Bilateral Health Agreements
    
    Link: https://www.thinkglobalhealth.org/article/tracking-the-america-first-bilateral-health-agreements
  - (health) [WVU Medicine] 10/01/2026, 01:06 PM, +0000 UTC — WVU Health System welcomes five new hospitals
    
    Link: https://wvumedicine.org/news/article/wvu-medicine/front-page/wvu-health-system-welcomes-five-new-hospitals/
  - (health) [Vatican News] 10/01/2026, 12:07 PM, +0000 UTC — Pope’s October prayer intention: ‘For mental health ministry’
    
    Link: https://www.vaticannews.va/en/pope/news/2026-10/pope-leo-prayer-intention-october-for-mental-health-ministry.html
  - (health) [aphis.usda.gov] 09/28/2026, 07:00 AM, +0000 UTC — Current Status of New World Screwworm | Screwworm.gov
    
    Link: https://www.aphis.usda.gov/animals/animal-health/livestock-and-poultry-disease/stop-screwworm/current-status
  - (health) [CalMatters] 09/28/2026, 12:00 PM, +0000 UTC — What will California's next governor do about healthcare? Here are Becerra and Hilton's plans
    
    Link: https://calmatters.org/health/2026/09/california-governor-healthcare-plans-2026/
  - (wellness) [Michigan Technological University] 10/02/2026, 06:21 PM, +0000 UTC — Michigan Tech Breaks Ground on Chang K. Park Center for Student Wellness
    
    Link: https://www.mtu.edu/news/2026/10/michigan-tech-breaks-ground-on-chang-k-park-center-for-student-wellness.html
  - (wellness) [Montana Free Press] 10/02/2026, 09:01 PM, +0000 UTC — Financial wellness is a practice
    
    Link: https://montanafreepress.org/2026/10/02/financial-wellness-is-a-practice/
  - (wellness) [RaleighNC.gov] 10/01/2026, 10:42 PM, +0000 UTC — Raleigh Parks Launches Fall Health and Wellness Pilot Classes
    
    Link: https://raleighnc.gov/parks-and-recreation/news/raleigh-parks-launches-fall-health-and-wellness-pilot-classes
  - (wellness) [Marquette Today] 09/30/2026, 09:46 PM, +0000 UTC — Wellness Wednesday: journal decorating, Oct. 7
    
    Link: https://today.marquette.edu/2026/09/wellness-wednesday-journal-decorating-oct-7/
  - (wellness) [San Bernardino County (.gov)] 10/01/2026, 08:57 PM, +0000 UTC — County invites community to free Fall Wellness Extravaganza
    
    Link: https://main.sbcounty.gov/2026/10/01/county-invites-community-to-free-fall-wellness-extravaganza/
  - (wellness) [News at IU] 10/01/2026, 10:15 PM, +0000 UTC — Wellness Week: Take care of you!: Office of Student Life
    
    Link: https://news.iu.edu/studentlife/live/news/53683-wellness-week-take-care-of-you
  - (wellness) [Civic Media] 09/30/2026, 04:29 PM, +0000 UTC — ‘Grounded in Wellness, United in Our Fight’: 18th annual Black Women’s Wellness Day set for Saturday
    
    Link: https://civicmedia.us/news/2026/09/30/grounded-in-wellness-united-in-our-fight-18th-annual-black-womens-wellness-day-set-for-saturday
  - (wellness) [People.com] 09/30/2026, 03:11 PM, +0000 UTC — Julianne Hough on Beauty, Wellness and Entering Her ‘Leading Lady Era’ (Exclusive)
    
    Link: https://people.com/julianne-hough-talks-beauty-wellness-dancing-with-the-stars-exclusive-12148999
  - (wellness) [Yahoo Creators] 10/01/2026, 08:01 PM, +0000 UTC — The secret to healthy habits isn't doing more. Psychologists say it's 'wellness stacking,' and here's how it works
    
    Link: https://creators.yahoo.com/lifestyle/story/the-secret-to-healthy-habits-isnt-doing-more-psychologists-say-its-wellness-stacking-and-heres-how-it-works-015140677.html
  - (wellness) [The Pennsylvania State University] 10/02/2026, 01:06 PM, +0000 UTC — Alumni’s gift to the School of Music aims to promote student wellness
    
    Link: https://www.psu.edu/news/arts-and-architecture/story/alumnis-gift-school-music-aims-promote-student-wellness
  - (wellness) [The Santa Barbara Independent] 09/29/2026, 10:41 PM, +0000 UTC — Santa Barbara High School Welcomes New-and-Improved Student Wellness Center
    
    Link: https://www.independent.com/2026/09/29/santa-barbara-high-school-welcomes-new-and-improved-student-wellness-center/
  - (wellness) [WSJ] 10/02/2026, 02:58 PM, +0000 UTC — When Menopause Hit, I Went on a Wellness Binge
    
    Link: https://www.wsj.com/health/wellness/when-menopause-hit-i-went-on-a-wellness-binge-59f85e9d
  - (medical study) [med.stanford.edu] 09/30/2026, 05:24 PM, +0000 UTC — Stanford Medicine-led research shows promise for a lymphedema drug
    
    Link: https://med.stanford.edu/news/all-news/2026/09/lymphedema-drug.html
  - (medical study) [Daily Bruin] 10/04/2026, 04:43 AM, +0000 UTC — UCLA alumnus turns medical school frustrations into AI study app ‘Neural Consult’
    
    Link: https://dailybruin.com/2026/10/03/ucla-alumnus-turns-medical-school-frustrations-into-ai-study-app-neural-consult
  - (medical study) [Johns Hopkins Medicine] 09/30/2026, 02:10 PM, +0000 UTC — Decadelong Study Finds Smoking Worsens Sickle Cell Retinopathy
    
    Link: https://www.hopkinsmedicine.org/news/newsroom/news-releases/2026/09/decadelong-study-finds-smoking-worsens-sickle-cell-retinopathy
  - (medical study) [American Medical Association | AMA] 09/30/2026, 12:09 PM, +0000 UTC — For Match success, look beyond your research publication count
    
    Link: https://www.ama-assn.org/medical-residents/research-during-residency/match-success-look-beyond-your-research-publication
  - (medical study) [GlobeNewswire] 09/29/2026, 12:00 PM, +0000 UTC — Apyx Medical Announces New Clinical Study Demonstrating Renuvion®’s Impact on Skin Quality
    
    Link: https://www.globenewswire.com/news-release/2026/09/29/3370752/0/en/apyx-medical-announces-new-clinical-study-demonstrating-renuvion-s-impact-on-skin-quality.html
  - (medical study) [Nature] 09/30/2026, 08:54 PM, +0000 UTC — Is exposomics the key to making personalized medicine a reality?
    
    Link: https://www.nature.com/articles/d41586-026-02958-8
  - (medical study) [PR Newswire] 09/29/2026, 12:00 PM, +0000 UTC — Publication of ROADS Phase 3 Clinical Trial Data in Journal of Clinical Oncology Recommends GammaTile® as a New Standard-of-Care Option for Newly Diagnosed Operable Brain Metastases1
    
    Link: https://www.prnewswire.com/news-releases/publication-of-roads-phase-3-clinical-trial-data-in-journal-of-clinical-oncology-recommends-gammatile-as-a-new-standard-of-care-option-for-newly-diagnosed-operable-brain-metastases1-302892327.html
  - (medical study) [fedweek.com] 10/01/2026, 12:30 AM, +0000 UTC — Medical Costs Sting Even to Those With Insurance, Study Finds
    
    Link: https://www.fedweek.com/retirement-financial-planning/medical-costs-sting-even-to-those-with-insurance-study-finds/
  - (medical study) [University of Miami] 10/02/2026, 01:44 PM, +0000 UTC — Blood Cancer Research Award Advances Lymphoma Clinical Trials
    
    Link: https://news.med.miami.edu/large-b-cell-lymphoma-clinical-trials-award/
  - (medical study) [News-Medical] 09/29/2026, 06:29 PM, +0000 UTC — New study explains how TMEM63B protein regulates cell membranes
    
    Link: https://www.news-medical.net/news/20260929/New-study-explains-how-TMEM63B-protein-regulates-cell-membranes.aspx
  - (medical study) [Harvard Health] 10/02/2026, 07:00 AM, +0000 UTC — People who walk more or walk faster live longer, study finds
    
    Link: https://www.health.harvard.edu/heart-health/people-who-walk-more-or-walk-faster-live-longer-study-finds
  - (medical study) [Medical Xpress] 09/29/2026, 09:40 PM, +0000 UTC — Tiny blood clots help guide blood flow as placenta develops, mouse study finds
    
    Link: https://medicalxpress.com/news/2026-09-tiny-blood-clots-placenta-mouse.html
  - (clinical trial health) [HHS.gov] 09/30/2026, 06:26 PM, +0000 UTC — HHS Launches SURPASS and New Efforts to Accelerate Faster, Smarter Clinical Trials
    
    Link: https://www.hhs.gov/press-room/hhs-arpa-h-launch-surpass-modernize-clinical-trials.html
  - (clinical trial health) [UT News] 09/30/2026, 07:00 PM, +0000 UTC — UT Takes Leading Role in National Effort To Modernize Clinical Trials
    
    Link: https://news.utexas.edu/2026/09/30/ut-takes-leading-role-in-national-effort-to-modernize-clinical-trials/
  - (clinical trial health) [Axios] 09/30/2026, 10:22 PM, +0000 UTC — Exclusive: HHS launches project to speed up clinical trials
    
    Link: https://www.axios.com/2026/09/30/hhs-clinical-trials-redesign
  - (clinical trial health) [Pfizer] 10/03/2026, 03:48 AM, +0000 UTC — How AI Is Helping Match Patients to Clinical Trials Faster
    
    Link: https://www.pfizer.com/news/articles/how_ai_is_helping_match_patients_to_clinical_trials_faster
  - (clinical trial health) [World Health Organization (WHO)] 09/30/2026, 01:27 PM, +0000 UTC — Kazakhstan Summer School strengthens national clinical research capacity
    
    Link: https://www.who.int/news/item/30-09-2026-kazakhstan-summer-school-strengthens-national-clinical-research-capacity
  - (clinical trial health) [BioPharma Dive] 10/01/2026, 04:07 PM, +0000 UTC — HHS kicks off new programs to speed clinical trials as Chinese competition looms
    
    Link: https://www.biopharmadive.com/news/hhs-clinical-trial-speed-arpa-h-drug-testing/831909/
  - (clinical trial health) [Austin American-Statesman] 10/01/2026, 05:58 PM, +0000 UTC — What if clinical trials took four years, not 10? UT will help test that idea
    
    Link: https://www.statesman.com/news/healthcare/article/dell-medical-school-clinical-trial-program-rfk-jr-22455124.php
  - (clinical trial health) [fiercebiotech.com] 09/29/2026, 07:04 PM, +0000 UTC — Canadian $5M accelerated clinical trial program cuts start-up to 45 days
    
    Link: https://www.fiercebiotech.com/cro/canadian-5m-accelerated-clinical-trial-program-cuts-start-45-days
  - (clinical trial health) [STAT] 09/30/2026, 08:10 PM, +0000 UTC — HHS announces new efforts to speed up, expand clinical trials with AI
    
    Link: https://www.statnews.com/2026/09/30/hhs-arpa-h-clinical-trials-artificial-intelligence-surpass-program/
  - (clinical trial health) [St. Louis American] 09/29/2026, 12:00 PM, +0000 UTC — Black patients face barriers to clinical trials
    
    Link: https://www.stlamerican.com/your-health-matters/black-patients-face-barriers-to-clinical-trials/
  - (clinical trial health) [KUT] 10/01/2026, 10:00 AM, +0000 UTC — RFK Jr. announces partnership with Dell Medical School to boost clinical trials in the US
    
    Link: https://www.kut.org/health/2026-10-01/austin-tx-rfk-jr-hhs-clinical-trials-ut-dell-medical-school
  - (clinical trial health) [National Institutes of Health (NIH) | (.gov)] 09/29/2026, 04:53 PM, +0000 UTC — Antiviral drug did not improve Long COVID symptoms
    
    Link: https://www.nih.gov/news-events/nih-research-matters/antiviral-drug-did-not-improve-long-covid-symptoms
  - (FDA recall health) [The New York Times] 10/03/2026, 09:01 PM, +0000 UTC — F.D.A. Classifies Salad Dressing Recall to Highest Health Risk
    
    Link: https://www.nytimes.com/2026/10/03/health/fda-recall-salata-salad-dressing-salmonella.html
  - (FDA recall health) [NBC 5 Dallas-Fort Worth] 09/29/2026, 10:22 AM, +0000 UTC — FDA recalls more than 13k bottles of blood pressure medication after quality issue
    
    Link: https://www.nbcdfw.com/news/local/recall-alert-local/fda-recalls-more-than-13000-bottles-of-blood-pressure-medication-after-quality-issue/4083976/
  - (FDA recall health) [The Hill] 09/28/2026, 06:54 PM, +0000 UTC — Blood pressure medication recalled nationwide under FDA’s Class II risk level
    
    Link: https://thehill.com/homenews/6115677-blood-pressure-medication-recalled-nationwide-under-fdas-class-ii-risk-level/
  - (FDA recall health) [Dallas News] 09/28/2026, 11:10 PM, +0000 UTC — FDA recalls blood pressure medication after quality issue
    
    Link: https://www.dallasnews.com/news/public-health/article/chlorthalidone-blood-pressure-tablets-recalled-fda-22453633.php
  - (FDA recall health) [Good Housekeeping] 09/27/2026, 05:06 PM, +0000 UTC — FDA Announces New Nationwide Blood Pressure Medication Recall
    
    Link: https://www.goodhousekeeping.com/health/a73839435/fda-new-blood-pressure-medicine-recall/
  - (FDA recall health) [AARP] 09/29/2026, 10:15 PM, +0000 UTC — FDA Announces Nationwide Recall of Chlorthalidone Tablets
    
    Link: https://www.aarp.org/health/conditions-treatments/blood-pressure-medication-recall-september-2026/
  - (FDA recall health) [EatingWell] 09/29/2026, 02:42 PM, +0000 UTC — The FDA Issued a Recall on Sugar Due to Contamination
    
    Link: https://www.eatingwell.com/sugar-recall-sept-2026-12146967
  - (FDA recall health) [Healthline] 10/02/2026, 08:02 PM, +0000 UTC — FDA Issues Class II Blood Pressure Medication Recall, Over 13,000 Bottles Affected
    
    Link: https://www.healthline.com/health-news/blood-pressure-medication-nationwide-recall-fda
  - (FDA recall health) [wusa9.com] 09/28/2026, 02:59 PM, +0000 UTC — Blood pressure medication recalled nationwide after failing FDA dissolution testing
    
    Link: https://www.wusa9.com/article/news/nation-world/blood-pressure-medication-recall/507-756358e0-3933-4870-a1f6-5f25d9512046
  - (FDA recall health) [usatoday.com] 09/29/2026, 12:07 PM, +0000 UTC — Blood pressure medication recalled nationwide. See affected drug
    
    Link: https://www.usatoday.com/story/money/consumer-protection/recalls-alerts/2026/09/28/blood-pressure-medication-recall/91991981007/
  - (FDA recall health) [newsnationnow.com] 09/28/2026, 07:58 PM, +0000 UTC — Blood pressure medication given Class II designation in recall update
    
    Link: https://www.newsnationnow.com/us-news/recalls/blood-pressure-medication-chlorthalidone-class-ii-recall-fda/
  - (FDA recall health) [nbcnews.com] 10/02/2026, 10:01 AM, +0000 UTC — FDA issues highest-level recall of salad dressing
    
    Link: https://www.nbcnews.com/video/shorts/fda-issues-highest-level-recall-of-salad-dressing-270903877823