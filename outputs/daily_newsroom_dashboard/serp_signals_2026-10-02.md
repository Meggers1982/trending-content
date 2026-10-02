# LIVE SIGNAL DATA — SerpAPI Pre-Fetch
The following signals were fetched from SerpAPI Google News and SerpAPI Google Trends immediately before this pipeline run. Treat Google Trends as AVAILABLE when this section contains a Google Trends block. Use it as the primary search_velocity input for Skills 01–05 (Signal Listener through Trend Strength Scorer). Use the Google News Radar as the broad discovery layer for news-led health topics, including topics that do not yet appear in Google Trends. Prioritize topics with convergence across News, Trends, primary/institutional sources, and credible publisher coverage.

## Google Trends — Trending Now (US / Health, real-time)
Terms with a "Why:" line have a confirmed real-world news story driving the spike; terms without one are a real-time signal only, not yet grounded in a specific story.
  - brooke eby
    Why: "Remembering Brooke Eby" — ALS Network

## Google Trends — 7-Day Interest (US)
  - **health**: latest=84, peak=100, 7d-delta=+7
    Rising related: health insurance giant nyt, health insurance giant, raoni barcelos health update, when is open enrollment for health insurance 2027, health care fraud, health insurance agency, essentia health, ez health
  - **wellness**: latest=51, peak=100, 7d-delta=+1
    Rising related: julianne hough beauty and wellness, tiktok wellness trends botulism warning, spacecamp wellness, space camp wellness, stc wellness city, wellness olympia, southeastern health and wellness institute, wellness spearstate
  - **nutrition**: latest=88, peak=100, 7d-delta=-1
    Rising related: supplemental nutrition assistance program changes, kona ice nutrition, supplemental nutrition assistance program, sports nutrition nebula buy review annalemedia, fitness nutrition twspoondietary, nutrition guide fparentips, annalemedia.com expert insights on nutrition, nutrition facts
  - **fitness**: latest=17, peak=100, 7d-delta=+0
    Rising related: online banking review, diy home renovation, camping gear essentials, baby stroller review, podcast equipment setup, tax software comparison, protein powder review, moving company quotes
  - **food safety**: latest=88, peak=100, 7d-delta=+5
    Rising related: premier food safety login, a food handlers duties regarding food safety include all of the following practices except to, food safety net services, loss of refrigeration is considered an, a food handlers duties regarding food safety except, which of the following does not help encourage food safety, food safety temperatures, state food safety
  - **diet**: latest=90, peak=100, 7d-delta=-1
    Rising related: mind diet brain aging study, living diet sean o'mara, dr sean omara diet, sean o'mara diet, sean omara diet, dr sean o'mara diet, the living diet sean o'mara, diet marble cheesecake
  - **weight loss**: latest=26, peak=100, 7d-delta=+0
    Rising related: zion williamson weight loss, eli lilly retatrutide weight loss, cagrisema and zepbound weight loss results, zion williamson, eli lilly weight loss results, kate upton weight loss, cc sabathia weight loss, camryn manheim weight loss
  - **mental health**: latest=47, peak=100, 7d-delta=-1
    Rising related: pilot mental health bill, unabomber mental health, ted kaczynski mental health, john a hauser mental health in aviation act, john a. hauser mental health in aviation act, mental health in aviation act, the kids mental health foundation, kids mental health foundation
  - **gut health**: latest=55, peak=100, 7d-delta=+8
    Rising related: is matcha good for gut health, lactobacillus rhamnosus, bioma, celtara gut health, best bone broth for gut health, eczema and gut health, signs of poor gut health, ryze

Top rising related queries from Google Trends:
  - health insurance giant nyt
  - health insurance giant
  - raoni barcelos health update
  - when is open enrollment for health insurance 2027
  - health care fraud
  - health insurance agency
  - essentia health
  - ez health
  - julianne hough beauty and wellness
  - tiktok wellness trends botulism warning
  - spacecamp wellness
  - space camp wellness
  - stc wellness city
  - wellness olympia
  - southeastern health and wellness institute
  - wellness spearstate
  - supplemental nutrition assistance program changes
  - kona ice nutrition
  - supplemental nutrition assistance program
  - sports nutrition nebula buy review annalemedia

## Google News Radar — Recent Health Topics (144 unique across 12 queries; showing 60)
Treat these headlines as the broad radar of news-led health topics. The Signal Listener must consider this radar before narrowing to retained candidates.
  - (health) [KFF] 09/30/2026, 07:00 AM, +0000 UTC — What Are the Recent Trends in Health Sector Employment
    
    Link: https://www.kff.org/health-costs/what-impact-has-the-coronavirus-pandemic-had-on-health-care-employment/
  - (health) [California State Portal | CA.gov] 09/28/2026, 06:48 PM, +0000 UTC — Governor Newsom signs legislation creating non-UPF label, other health bills advancing California’s nation-leading healthcare strategy
    
    Link: https://www.gov.ca.gov/2026/09/28/governor-newsom-signs-legislation-creating-non-upf-label-other-health-bills-advancing-californias-nation-leading-healthcare-strategy/
  - (health) [Dartmouth] 09/29/2026, 05:25 PM, +0000 UTC — Historic $20 Million Gift to Launch Dartmouth Health at Home
    
    Link: https://home.dartmouth.edu/news/2026/09/historic-20-million-gift-launch-dartmouth-health-home
  - (health) [NYU Langone Health] 09/30/2026, 03:36 PM, +0000 UTC — Sugar Amplifies Damage Done to Gut Health by Antibiotics
    
    Link: https://nyulangone.org/news/sugar-amplifies-damage-done-gut-health-antibiotics
  - (health) [WVU Medicine] 10/01/2026, 01:06 PM, +0000 UTC — WVU Health System welcomes five new hospitals
    
    Link: https://wvumedicine.org/news/article/wvu-medicine/front-page/wvu-health-system-welcomes-five-new-hospitals/
  - (health) [Vatican News] 10/01/2026, 12:07 PM, +0000 UTC — Pope’s October prayer intention: ‘For mental health ministry’
    
    Link: https://www.vaticannews.va/en/pope/news/2026-10/pope-leo-prayer-intention-october-for-mental-health-ministry.html
  - (health) [Think Global Health] 09/29/2026, 07:00 AM, +0000 UTC — Tracking the "America First" Bilateral Health Agreements
    
    Link: https://www.thinkglobalhealth.org/article/tracking-the-america-first-bilateral-health-agreements
  - (health) [PBS] 09/25/2026, 10:35 PM, +0000 UTC — Health care costs a major concern for voters ahead of midterms
    
    Link: https://www.pbs.org/newshour/show/health-care-costs-a-major-concern-for-voters-ahead-of-midterms
  - (health) [aphis.usda.gov] 09/28/2026, 07:00 AM, +0000 UTC — Current Status of New World Screwworm | Screwworm.gov
    
    Link: https://www.aphis.usda.gov/animals/animal-health/livestock-and-poultry-disease/stop-screwworm/current-status
  - (health) [NPR] 09/26/2026, 09:00 AM, +0000 UTC — Meal deliveries can save money and improve health. Will they survive Medicaid cuts?
    
    Link: https://www.npr.org/2026/09/26/nx-s1-5946434/medically-tailored-meal-deliveries-medicaid-cuts
  - (health) [CalMatters] 09/28/2026, 12:00 PM, +0000 UTC — What will California's next governor do about healthcare? Here are Becerra and Hilton's plans
    
    Link: https://calmatters.org/health/2026/09/california-governor-healthcare-plans-2026/
  - (health) [who.int] 09/25/2026, 10:09 PM, +0000 UTC — World leaders renew commitment to protect the world from future pandemics
    
    Link: https://www.who.int/news/item/25-09-2026-world-leaders-renew-commitment-to-protect-the-world-from-future-pandemics
  - (wellness) [California Department of Corrections and Rehabilitation - CDCR (.gov)] 09/29/2026, 01:46 PM, +0000 UTC — Valley State Prison hosts wellness fair
    
    Link: https://www.cdcr.ca.gov/insidecdcr/2026/09/29/valley-state-prison-hosts-wellness-fair/
  - (wellness) [RaleighNC.gov] 10/01/2026, 10:42 PM, +0000 UTC — Raleigh Parks Launches Fall Health and Wellness Pilot Classes
    
    Link: https://raleighnc.gov/parks-and-recreation/news/raleigh-parks-launches-fall-health-and-wellness-pilot-classes
  - (wellness) [Marquette Today] 09/30/2026, 09:46 PM, +0000 UTC — Wellness Wednesday: journal decorating, Oct. 7
    
    Link: https://today.marquette.edu/2026/09/wellness-wednesday-journal-decorating-oct-7/
  - (wellness) [San Bernardino County (.gov)] 10/01/2026, 08:57 PM, +0000 UTC — County invites community to free Fall Wellness Extravaganza
    
    Link: https://main.sbcounty.gov/2026/10/01/county-invites-community-to-free-fall-wellness-extravaganza/
  - (wellness) [News at IU] 10/01/2026, 10:15 PM, +0000 UTC — Wellness Week: Take care of you!: Office of Student Life
    
    Link: https://news.iu.edu/studentlife/live/news/53683-wellness-week-take-care-of-you
  - (wellness) [WIRED] 09/27/2026, 09:30 AM, +0000 UTC — Nicotine Is Mounting a Comeback in the Wellness Movement
    
    Link: https://www.wired.com/story/nicotine-is-mounting-a-comeback-in-the-wellness-movement/
  - (wellness) [US Chamber] 09/30/2026, 01:03 PM, +0000 UTC — How Walmart, Ulta, and Amazon Are Growing in Wellness
    
    Link: https://www.uschamber.com/co/good-company/launch-pad/retail-wellness-growth-strategies
  - (wellness) [wsj.com] 10/02/2026, 02:57 PM, +0000 UTC — When Menopause Hit, I Went on a Wellness Binge
    
    Link: https://www.wsj.com/health/wellness/when-menopause-hit-i-went-on-a-wellness-binge-59f85e9d
  - (wellness) [people.com] 09/30/2026, 03:11 PM, +0000 UTC — Julianne Hough on Beauty, Wellness and Entering Her ‘Leading Lady Era’ (Exclusive)
    
    Link: https://people.com/julianne-hough-talks-beauty-wellness-dancing-with-the-stars-exclusive-12148999
  - (wellness) [UAMS News] 09/28/2026, 03:30 PM, +0000 UTC — UAMS-Sponsored Health & Wellness Expo Offers Free Screenings, Other Resources
    
    Link: https://news.uams.edu/2026/09/28/uams-sponsored-health-wellness-expo-offers-free-screenings-other-resources/
  - (wellness) [Civic Media] 09/30/2026, 04:29 PM, +0000 UTC — ‘Grounded in Wellness, United in Our Fight’: 18th annual Black Women’s Wellness Day set for Saturday
    
    Link: https://civicmedia.us/news/2026/09/30/grounded-in-wellness-united-in-our-fight-18th-annual-black-womens-wellness-day-set-for-saturday
  - (wellness) [State University of New York at Fredonia] 09/28/2026, 05:32 PM, +0000 UTC — Fredonia to hold World Mental Health Day Wellness Fair
    
    Link: https://www.fredonia.edu/news/articles/fredonia-hold-world-mental-health-day-wellness-fair
  - (medical study) [Stanford Medicine] 09/30/2026, 05:24 PM, +0000 UTC — Stanford Medicine-led research shows promise for a lymphedema drug
    
    Link: https://med.stanford.edu/news/all-news/2026/09/lymphedema-drug.html
  - (medical study) [UToledo News] 09/30/2026, 08:01 AM, +0000 UTC — UToledo Medical Students Set Sail to Study How Lake Erie Shapes Human Health
    
    Link: https://news.utoledo.edu/index.php/09_30_2026/utoledo-medical-students-set-sail-to-study-how-lake-erie-shapes-human-health
  - (medical study) [hopkinsmedicine.org] 09/30/2026, 02:10 PM, +0000 UTC — Decadelong Study Finds Smoking Worsens Sickle Cell Retinopathy
    
    Link: https://www.hopkinsmedicine.org/news/newsroom/news-releases/2026/09/decadelong-study-finds-smoking-worsens-sickle-cell-retinopathy
  - (medical study) [American Medical Association | AMA] 09/30/2026, 12:09 PM, +0000 UTC — For Match success, look beyond your research publication count
    
    Link: https://www.ama-assn.org/medical-residents/research-during-residency/match-success-look-beyond-your-research-publication
  - (medical study) [HHS.gov] 09/30/2026, 06:26 PM, +0000 UTC — HHS Launches SURPASS and New Efforts to Accelerate Faster, Smarter Clinical Trials
    
    Link: https://www.hhs.gov/press-room/hhs-arpa-h-launch-surpass-modernize-clinical-trials.html
  - (medical study) [GlobeNewswire] 09/29/2026, 12:00 PM, +0000 UTC — Apyx Medical Announces New Clinical Study Demonstrating Renuvion®’s Impact on Skin Quality
    
    Link: https://www.globenewswire.com/news-release/2026/09/29/3370752/0/en/apyx-medical-announces-new-clinical-study-demonstrating-renuvion-s-impact-on-skin-quality.html
  - (medical study) [Healthcare Dive] 09/28/2026, 03:52 PM, +0000 UTC — Healthcare workers battle persistent long COVID: study
    
    Link: https://www.healthcaredive.com/news/healthcare-workers-battle-persistent-long-covid/831493/
  - (medical study) [Nature] 09/29/2026, 04:34 AM, +0000 UTC — Risk factors of post-COVID-19 symptoms, a cross-sectional study in patients with asthma and chronic obstructive lung disease
    
    Link: https://www.nature.com/articles/s41533-026-00570-x
  - (medical study) [FEDweek] 10/01/2026, 12:30 AM, +0000 UTC — Medical Costs Sting Even to Those With Insurance, Study Finds
    
    Link: https://www.fedweek.com/retirement-financial-planning/medical-costs-sting-even-to-those-with-insurance-study-finds/
  - (medical study) [News-Medical] 09/29/2026, 06:29 PM, +0000 UTC — New study explains how TMEM63B protein regulates cell membranes
    
    Link: https://www.news-medical.net/news/20260929/New-study-explains-how-TMEM63B-protein-regulates-cell-membranes.aspx
  - (medical study) [medicalxpress.com] 09/30/2026, 03:40 PM, +0000 UTC — Activating 'energy saver' mode significantly extends lives of animals in preclinical study
    
    Link: https://medicalxpress.com/news/2026-09-energy-saver-mode-significantly-animals.html
  - (medical study) [Foley Hoag] 10/01/2026, 02:21 PM, +0000 UTC — When FDA Oversees Trials Overseas: Foreign Clinical Trial Considerations
    
    Link: https://foleyhoag.com/news-and-insights/publications/alerts-and-updates/2026/september/when-fda-oversees-trials-overseas-foreign-clinical-trial-considerations/
  - (clinical trial health) [UT News] 09/30/2026, 07:00 PM, +0000 UTC — UT Takes Leading Role in National Effort To Modernize Clinical Trials
    
    Link: https://news.utexas.edu/2026/09/30/ut-takes-leading-role-in-national-effort-to-modernize-clinical-trials/
  - (clinical trial health) [Axios] 09/30/2026, 10:22 PM, +0000 UTC — Exclusive: HHS launches project to speed up clinical trials
    
    Link: https://www.axios.com/2026/09/30/hhs-clinical-trials-redesign
  - (clinical trial health) [Pfizer] 09/30/2026, 12:26 PM, +0000 UTC — How AI Is Helping Match Patients to Clinical Trials Faster
    
    Link: https://www.pfizer.com/news/articles/how_ai_is_helping_match_patients_to_clinical_trials_faster
  - (clinical trial health) [World Health Organization (WHO)] 09/30/2026, 01:27 PM, +0000 UTC — Kazakhstan Summer School strengthens national clinical research capacity
    
    Link: https://www.who.int/news/item/30-09-2026-kazakhstan-summer-school-strengthens-national-clinical-research-capacity
  - (clinical trial health) [BioPharma Dive] 10/01/2026, 04:07 PM, +0000 UTC — HHS kicks off new programs to speed clinical trials as Chinese competition looms
    
    Link: https://www.biopharmadive.com/news/hhs-clinical-trial-speed-arpa-h-drug-testing/831909/
  - (clinical trial health) [statnews.com] 09/30/2026, 08:10 PM, +0000 UTC — HHS announces new efforts to speed up, expand clinical trials with AI
    
    Link: https://www.statnews.com/2026/09/30/hhs-arpa-h-clinical-trials-artificial-intelligence-surpass-program/
  - (clinical trial health) [KUT] 10/01/2026, 10:00 AM, +0000 UTC — RFK Jr. announces partnership with Dell Medical School to boost clinical trials in the US
    
    Link: https://www.kut.org/health/2026-10-01/austin-tx-rfk-jr-hhs-clinical-trials-ut-dell-medical-school
  - (clinical trial health) [St. Louis American] 09/29/2026, 12:00 PM, +0000 UTC — Black patients face barriers to clinical trials
    
    Link: https://www.stlamerican.com/your-health-matters/black-patients-face-barriers-to-clinical-trials/
  - (clinical trial health) [Fierce Biotech] 09/29/2026, 07:04 PM, +0000 UTC — Canadian $5M accelerated clinical trial program cuts start-up to 45 days
    
    Link: https://www.fiercebiotech.com/cro/canadian-5m-accelerated-clinical-trial-program-cuts-start-45-days
  - (clinical trial health) [National Institutes of Health (NIH) | (.gov)] 09/29/2026, 04:53 PM, +0000 UTC — Antiviral drug did not improve Long COVID symptoms
    
    Link: https://www.nih.gov/news-events/nih-research-matters/antiviral-drug-did-not-improve-long-covid-symptoms
  - (clinical trial health) [BioSpace] 10/01/2026, 02:40 PM, +0000 UTC — US government launches AI-driven programs to overhaul clinical trials
    
    Link: https://www.biospace.com/drug-development/us-government-launches-ai-driven-programs-to-overhaul-clinical-trials
  - (clinical trial health) [Austin American-Statesman] 10/01/2026, 05:58 PM, +0000 UTC — What if clinical trials took four years, not 10? UT will help test that idea
    
    Link: https://www.statesman.com/news/healthcare/article/dell-medical-school-clinical-trial-program-rfk-jr-22455124.php
  - (FDA recall health) [NBC 5 Dallas-Fort Worth] 09/29/2026, 10:22 AM, +0000 UTC — FDA recalls more than 13k bottles of blood pressure medication after quality issue
    
    Link: https://www.nbcdfw.com/news/local/recall-alert-local/fda-recalls-more-than-13000-bottles-of-blood-pressure-medication-after-quality-issue/4083976/
  - (FDA recall health) [thehill.com] 09/28/2026, 06:54 PM, +0000 UTC — Blood pressure medication recalled nationwide under FDA’s Class II risk level
    
    Link: https://thehill.com/homenews/6115677-blood-pressure-medication-recalled-nationwide-under-fdas-class-ii-risk-level/
  - (FDA recall health) [EatingWell] 09/29/2026, 02:42 PM, +0000 UTC — The FDA Issued a Recall on Sugar Due to Contamination
    
    Link: https://www.eatingwell.com/sugar-recall-sept-2026-12146967
  - (FDA recall health) [dallasnews.com] 09/28/2026, 11:10 PM, +0000 UTC — FDA recalls more than 13,000 bottles of blood pressure medication after quality issue
    
    Link: https://www.dallasnews.com/news/public-health/article/chlorthalidone-blood-pressure-tablets-recalled-fda-22453633.php
  - (FDA recall health) [Good Housekeeping] 09/27/2026, 05:06 PM, +0000 UTC — FDA Announces New Nationwide Blood Pressure Medication Recall
    
    Link: https://www.goodhousekeeping.com/health/a73839435/fda-new-blood-pressure-medicine-recall/
  - (FDA recall health) [Radiology Business] 09/29/2026, 08:17 PM, +0000 UTC — Software glitch prompts recall of PET/CT systems
    
    Link: https://radiologybusiness.com/topics/healthcare-management/healthcare-policy/software-glitch-prompts-recall-petct-systems
  - (FDA recall health) [wusa9.com] 09/28/2026, 02:59 PM, +0000 UTC — Blood pressure medication recalled nationwide after failing FDA dissolution testing
    
    Link: https://www.wusa9.com/article/news/nation-world/blood-pressure-medication-recall/507-756358e0-3933-4870-a1f6-5f25d9512046
  - (FDA recall health) [USA Today] 09/29/2026, 12:07 PM, +0000 UTC — Blood pressure medication recalled nationwide. See affected drug
    
    Link: https://www.usatoday.com/story/money/consumer-protection/recalls-alerts/2026/09/28/blood-pressure-medication-recall/91991981007/
  - (FDA recall health) [NewsNation] 09/28/2026, 07:58 PM, +0000 UTC — Blood pressure medication given Class II designation in recall update
    
    Link: https://www.newsnationnow.com/us-news/recalls/blood-pressure-medication-chlorthalidone-class-ii-recall-fda/
  - (FDA recall health) [AARP] 09/29/2026, 10:15 PM, +0000 UTC — FDA Announces Nationwide Recall of Chlorthalidone Tablets
    
    Link: https://www.aarp.org/health/conditions-treatments/blood-pressure-medication-recall-september-2026/
  - (FDA recall health) [News4JAX] 09/28/2026, 08:15 PM, +0000 UTC — Thousands of bottles of blood pressure medication recalled nationwide
    
    Link: https://www.news4jax.com/news/local/2026/09/28/thousands-of-bottles-of-blood-pressure-medication-recalled-nationwide/
  - (FDA recall health) [qz.com] 09/29/2026, 11:52 AM, +0000 UTC — Inventia Healthcare recalls 25,000+ bottles of blood pressure medication over dissolution failure
    
    Link: https://qz.com/inventia-healthcare-chlorthalidone-recall-dissolution-092926