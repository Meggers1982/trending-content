# LIVE SIGNAL DATA — SerpAPI Pre-Fetch
The following signals were fetched from SerpAPI Google News and SerpAPI Google Trends immediately before this pipeline run. Treat Google Trends as AVAILABLE when this section contains a Google Trends block. Use it as the primary search_velocity input for Skills 01–05 (Signal Listener through Trend Strength Scorer). Use the Google News Radar as the broad discovery layer for news-led health topics, including topics that do not yet appear in Google Trends. Prioritize topics with convergence across News, Trends, primary/institutional sources, and credible publisher coverage.

## Google Trends — 7-Day Interest (US)
  - **health**: latest=87, peak=100, 7d-delta=+6
    Rising related: health insurance giant, health insurance giant nyt, purple yam, neko health, health insurance agency, health care fraud, essentia health, protide health
  - **wellness**: latest=49, peak=100, 7d-delta=-5
    Rising related: julianne hough beauty and wellness, spacecamp wellness, space camp wellness, stc wellness city, quietgrovehaven.com discover insights on wellness, wutawhealth wellness information, healthsciencesforum.com health and wellness coach, parenting wellness infoguide famparentlife
  - **nutrition**: latest=89, peak=100, 7d-delta=-10
    Rising related: kona ice nutrition, supplemental nutrition assistance program, costco churro nutrition, nutrition guide fparentips, bowmar nutrition, fitness nutrition twspoondietary, sports nutrition nebula buy review annalemedia, delicata squash nutrition
  - **fitness**: latest=18, peak=100, 7d-delta=+1
    Rising related: tax software comparison, protein powder review, smart home devices, camping gear essentials, online banking review, coworking space near me, electric bike review, diy home renovation
  - **food safety**: latest=56, peak=100, 7d-delta=+1
    Rising related: museums, food safety violations tennessee valley, how preventable is abusive head trauma?, when a product has been declared unsafe to serve to customers, pathogens grow well between which temperatures, premier food safety login, ready to eat tcs food must be marked with the date, 123 premier food safety
  - **diet**: latest=93, peak=100, 7d-delta=-7
    Rising related: sean omara diet, diet marble cheesecake, sean o'mara diet, the living diet sean o'mara, dr sean omara diet, dr sean o'mara diet, jd vance diet, derrick henry diet
  - **weight loss**: latest=26, peak=100, 7d-delta=+0
    Rising related: what happened when dylan dreyer questioned craig melvin about weight loss on today, cagrisema and zepbound weight loss results, zion williamson weight loss, kate upton weight loss, eli lilly retatrutide weight loss, new weight loss drug, amy schumer weight loss, billy gardell weight loss
  - **mental health**: latest=49, peak=100, 7d-delta=-3
    Rising related: pilot mental health bill, john a. hauser mental health in aviation act, mental health in aviation act, pink clouding mental health, unabomber mental health, ted kaczynski mental health, john a hauser mental health in aviation act, kids mental health foundation
  - **gut health**: latest=52, peak=100, 7d-delta=-3
    Rising related: lactobacillus rhamnosus, gut health documentary netflix, emma pills for gut health, bioma, fermented foods list for gut health, gut health in spanish, stevia and gut health, ibs symptoms

Top rising related queries from Google Trends:
  - health insurance giant
  - health insurance giant nyt
  - purple yam
  - neko health
  - health insurance agency
  - health care fraud
  - essentia health
  - protide health
  - julianne hough beauty and wellness
  - spacecamp wellness
  - space camp wellness
  - stc wellness city
  - quietgrovehaven.com discover insights on wellness
  - wutawhealth wellness information
  - healthsciencesforum.com health and wellness coach
  - parenting wellness infoguide famparentlife
  - kona ice nutrition
  - supplemental nutrition assistance program
  - costco churro nutrition
  - nutrition guide fparentips

## Google News Radar — Recent Health Topics (144 unique across 12 queries; showing 60)
Treat these headlines as the broad radar of news-led health topics. The Signal Listener must consider this radar before narrowing to retained candidates.
  - (health) [Department of Justice (.gov)] 09/25/2026, 04:15 PM, +0000 UTC — Texas Mental Health Clinic Owner Convicted in $26M Scheme to Defraud Military Health Benefits Program
    
    Link: https://www.justice.gov/opa/pr/texas-mental-health-clinic-owner-convicted-26m-scheme-defraud-military-health-benefits
  - (health) [California State Portal | CA.gov] 09/28/2026, 06:48 PM, +0000 UTC — Governor Newsom signs legislation creating non-UPF label, other health bills advancing California’s nation-leading healthcare strategy
    
    Link: https://www.gov.ca.gov/2026/09/28/governor-newsom-signs-legislation-creating-non-upf-label-other-health-bills-advancing-californias-nation-leading-healthcare-strategy/
  - (health) [Dartmouth] 09/29/2026, 05:25 PM, +0000 UTC — Historic $20 Million Gift to Launch Dartmouth Health at Home
    
    Link: https://home.dartmouth.edu/news/2026/09/historic-20-million-gift-launch-dartmouth-health-home
  - (health) [PBS] 09/25/2026, 10:35 PM, +0000 UTC — Health care costs a major concern for voters ahead of midterms
    
    Link: https://www.pbs.org/newshour/show/health-care-costs-a-major-concern-for-voters-ahead-of-midterms
  - (health) [aphis.usda.gov] 09/28/2026, 07:00 AM, +0000 UTC — Current Status of New World Screwworm | Screwworm.gov
    
    Link: https://www.aphis.usda.gov/animals/animal-health/livestock-and-poultry-disease/stop-screwworm/current-status
  - (health) [CalMatters] 09/28/2026, 12:00 PM, +0000 UTC — What will California's next governor do about healthcare? Here are Becerra and Hilton's plans
    
    Link: https://calmatters.org/health/2026/09/california-governor-healthcare-plans-2026/
  - (health) [Healthcare Dive] 09/28/2026, 03:44 PM, +0000 UTC — Insurers say AI could add billions in health costs. Billing companies disagree
    
    Link: https://www.healthcaredive.com/news/insurers-say-ai-could-add-billions-in-health-costs-billing-companies-disag/831497/
  - (health) [Georgia Institute of Technology] 09/24/2026, 06:11 PM, +0000 UTC — Engineers Connect Health Wearables and Implants Using the Body as the Network
    
    Link: https://coe.gatech.edu/news/2026/09/engineers-connect-health-wearables-and-implants-using-body-network
  - (health) [Vatican News] 10/01/2026, 12:07 PM, +0000 UTC — Pope’s October prayer intention: ‘For mental health ministry’
    
    Link: https://www.vaticannews.va/en/pope/news/2026-10/pope-leo-prayer-intention-october-for-mental-health-ministry.html
  - (health) [NPR] 09/26/2026, 09:00 AM, +0000 UTC — Meal deliveries can save money and improve health. Will they survive Medicaid cuts?
    
    Link: https://www.npr.org/2026/09/26/nx-s1-5946434/medically-tailored-meal-deliveries-medicaid-cuts
  - (health) [MPR News] 09/29/2026, 04:11 PM, +0000 UTC — Minnesota health systems HealthPartners, Essentia Health announce plan to merge
    
    Link: https://www.mprnews.org/story/2026/09/29/healthpartners-and-essentia-health-announce-plan-to-merge
  - (health) [World Health Organization (WHO)] 09/25/2026, 04:32 PM, +0000 UTC — World leaders renew commitment to protect the world from future pandemics
    
    Link: https://www.who.int/news/item/25-09-2026-world-leaders-renew-commitment-to-protect-the-world-from-future-pandemics
  - (wellness) [California Department of Corrections and Rehabilitation - CDCR (.gov)] 09/29/2026, 01:46 PM, +0000 UTC — Valley State Prison hosts wellness fair
    
    Link: https://www.cdcr.ca.gov/insidecdcr/2026/09/29/valley-state-prison-hosts-wellness-fair/
  - (wellness) [Marquette Today] 09/30/2026, 09:46 PM, +0000 UTC — Wellness Wednesday: journal decorating, Oct. 7
    
    Link: https://today.marquette.edu/2026/09/wellness-wednesday-journal-decorating-oct-7/
  - (wellness) [People.com] 09/30/2026, 03:11 PM, +0000 UTC — Julianne Hough on Beauty, Wellness and Entering Her ‘Leading Lady Era’ (Exclusive)
    
    Link: https://people.com/julianne-hough-talks-beauty-wellness-dancing-with-the-stars-exclusive-12148999
  - (wellness) [The American Legion] 09/28/2026, 11:46 AM, +0000 UTC — Be the One focus of motorcycle ride, community wellness fair
    
    Link: https://www.legion.org/information-center/news/riders/2026/september/be-the-one-focus-of-motorcycle-ride-community-wellness-fair
  - (wellness) [UAMS News] 09/28/2026, 03:30 PM, +0000 UTC — UAMS-Sponsored Health & Wellness Expo Offers Free Screenings, Other Resources
    
    Link: https://news.uams.edu/2026/09/28/uams-sponsored-health-wellness-expo-offers-free-screenings-other-resources/
  - (wellness) [State University of New York at Fredonia] 09/28/2026, 05:32 PM, +0000 UTC — Fredonia to hold World Mental Health Day Wellness Fair
    
    Link: https://www.fredonia.edu/news/articles/fredonia-hold-world-mental-health-day-wellness-fair
  - (wellness) [City of Champaign (.gov)] 09/29/2026, 07:31 AM, +0000 UTC — 4th Annual Black Mental Health and Wellness Conference Recap
    
    Link: https://champaignil.gov/2026/09/28/4th-annual-black-mental-health-and-wellness-conference-recap/
  - (wellness) [intermiamicf.com] 09/29/2026, 02:06 PM, +0000 UTC — Inter Miami CF and Nu Stadium Host Annual Health and Wellness Fair for Front Office and Sporting Team Members
    
    Link: https://www.intermiamicf.com/news/inter-miami-cf-and-nu-stadium-host-annual-health-and-wellness-fair-for-front-office-and-sporting-team-members
  - (wellness) [The Santa Barbara Independent] 09/29/2026, 10:41 PM, +0000 UTC — Santa Barbara High School Welcomes New-and-Improved Student Wellness Center
    
    Link: https://www.independent.com/2026/09/29/santa-barbara-high-school-welcomes-new-and-improved-student-wellness-center/
  - (wellness) [KCRA] 09/26/2026, 01:38 AM, +0000 UTC — San Joaquin County shelter opens new health and wellness center
    
    Link: https://www.kcra.com/article/san-joaquin-county-shelter-health-and-wellness-center/73896344
  - (wellness) [Buffalo Bills] 09/28/2026, 09:26 PM, +0000 UTC — Highmark Foundation and Buffalo Bills Foundation Unveil "Victory Table" to Expand Access to Healthy Food and Wellness Resources Across Western New York
    
    Link: https://www.buffalobills.com/news/highmark-foundation-and-buffalo-bills-foundation-unveil-victory-table-to-expand-access-to-healthy-food-and-wellness-resources-across-western-new-york
  - (wellness) [The Lutheran Church—Missouri Synod] 09/25/2026, 06:55 PM, +0000 UTC — Church worker wellness: Love for Christ, love for one another
    
    Link: https://reporter.lcms.org/2026/church-worker-wellness-love-for-christ-love-for-one-another/
  - (medical study) [Stanford Medicine] 09/28/2026, 03:36 PM, +0000 UTC — Cutting ultra-processed food from school menus will be tricky, Stanford Medicine study finds
    
    Link: https://med.stanford.edu/news/all-news/2026/09/ultra-processed-school-food.html
  - (medical study) [UToledo News] 09/30/2026, 08:01 AM, +0000 UTC — UToledo Medical Students Set Sail to Study How Lake Erie Shapes Human Health
    
    Link: https://news.utoledo.edu/index.php/09_30_2026/utoledo-medical-students-set-sail-to-study-how-lake-erie-shapes-human-health
  - (medical study) [American Medical Association | AMA] 09/30/2026, 12:09 PM, +0000 UTC — For Match success, look beyond your research publication count
    
    Link: https://www.ama-assn.org/medical-residents/research-during-residency/match-success-look-beyond-your-research-publication
  - (medical study) [Nature] 09/29/2026, 10:42 AM, +0000 UTC — Reproducibility in biomedical research
    
    Link: https://www.nature.com/articles/s41591-026-04667-1
  - (medical study) [Healthcare Dive] 09/28/2026, 03:52 PM, +0000 UTC — Healthcare workers battle persistent long COVID: study
    
    Link: https://www.healthcaredive.com/news/healthcare-workers-battle-persistent-long-covid/831493/
  - (medical study) [GlobeNewswire] 09/29/2026, 12:00 PM, +0000 UTC — Apyx Medical Announces New Clinical Study Demonstrating Renuvion®’s Impact on Skin Quality
    
    Link: https://www.globenewswire.com/news-release/2026/09/29/3370752/0/en/apyx-medical-announces-new-clinical-study-demonstrating-renuvion-s-impact-on-skin-quality.html
  - (medical study) [FEDweek] 10/01/2026, 12:30 AM, +0000 UTC — Medical Costs Sting Even to Those With Insurance, Study Finds
    
    Link: https://www.fedweek.com/retirement-financial-planning/medical-costs-sting-even-to-those-with-insurance-study-finds/
  - (medical study) [News-Medical] 09/28/2026, 08:47 AM, +0000 UTC — Study links insomnia to higher stroke and hospitalization risks
    
    Link: https://www.news-medical.net/news/20260928/Study-links-insomnia-to-higher-stroke-and-hospitalization-risks.aspx
  - (medical study) [The New York Times] 09/26/2026, 11:00 AM, +0000 UTC — Opinion | Why Do Clinical Trials for Cancer Drugs Take So Long?
    
    Link: https://www.nytimes.com/2026/09/26/opinion/clinical-trials-cancer-drugs.html
  - (medical study) [Stanford Medicine] 09/30/2026, 05:24 PM, +0000 UTC — Stanford Medicine-led research shows promise for a lymphedema drug
    
    Link: https://med.stanford.edu/news/all-news/2026/09/lymphedema-drug.html
  - (medical study) [Nature] 09/29/2026, 04:34 AM, +0000 UTC — Risk factors of post-COVID-19 symptoms, a cross-sectional study in patients with asthma and chronic obstructive lung disease
    
    Link: https://www.nature.com/articles/s41533-026-00570-x
  - (medical study) [News-Medical] 09/29/2026, 06:29 PM, +0000 UTC — New study explains how TMEM63B protein regulates cell membranes
    
    Link: https://www.news-medical.net/news/20260929/New-study-explains-how-TMEM63B-protein-regulates-cell-membranes.aspx
  - (clinical trial health) [Nature] 09/25/2026, 10:49 AM, +0000 UTC — Does expansion of clinical trial capacity improve healthcare access?
    
    Link: https://www.nature.com/articles/s41591-026-04683-1
  - (clinical trial health) [UT News] 09/30/2026, 07:00 PM, +0000 UTC — UT Takes Leading Role in National Effort To Modernize Clinical Trials
    
    Link: https://news.utexas.edu/2026/09/30/ut-takes-leading-role-in-national-effort-to-modernize-clinical-trials/
  - (clinical trial health) [HHS.gov] 09/30/2026, 06:26 PM, +0000 UTC — HHS Launches SURPASS and New Efforts to Accelerate Faster, Smarter Clinical Trials
    
    Link: https://www.hhs.gov/press-room/hhs-arpa-h-launch-surpass-modernize-clinical-trials.html
  - (clinical trial health) [Pfizer] 09/30/2026, 12:26 PM, +0000 UTC — How AI Is Helping Match Patients to Clinical Trials Faster
    
    Link: https://www.pfizer.com/news/articles/how_ai_is_helping_match_patients_to_clinical_trials_faster
  - (clinical trial health) [Axios] 09/30/2026, 07:48 PM, +0000 UTC — Exclusive: HHS launches project to speed up clinical trials
    
    Link: https://www.axios.com/2026/09/30/hhs-clinical-trials-redesign
  - (clinical trial health) [St. Louis American] 09/29/2026, 12:00 PM, +0000 UTC — Black patients face barriers to clinical trials
    
    Link: https://www.stlamerican.com/your-health-matters/black-patients-face-barriers-to-clinical-trials/
  - (clinical trial health) [STAT] 09/30/2026, 08:10 PM, +0000 UTC — HHS announces new efforts to speed up, expand clinical trials with AI
    
    Link: https://www.statnews.com/2026/09/30/hhs-arpa-h-clinical-trials-artificial-intelligence-surpass-program/
  - (clinical trial health) [BioPharma Dive] 10/01/2026, 04:07 PM, +0000 UTC — HHS kicks off new programs to speed clinical trials as Chinese competition looms
    
    Link: https://www.biopharmadive.com/news/hhs-clinical-trial-speed-arpa-h-drug-testing/831909/
  - (clinical trial health) [KUT] 10/01/2026, 10:00 AM, +0000 UTC — RFK Jr. announces partnership with Dell Medical School to boost clinical trials in the US
    
    Link: https://www.kut.org/health/2026-10-01/austin-tx-rfk-jr-hhs-clinical-trials-ut-dell-medical-school
  - (clinical trial health) [Fierce Biotech] 09/29/2026, 07:04 PM, +0000 UTC — Canadian $5M accelerated clinical trial program cuts start-up to 45 days
    
    Link: https://www.fiercebiotech.com/cro/canadian-5m-accelerated-clinical-trial-program-cuts-start-45-days
  - (clinical trial health) [National Institutes of Health (NIH) | (.gov)] 09/29/2026, 04:53 PM, +0000 UTC — Antiviral drug did not improve Long COVID symptoms
    
    Link: https://www.nih.gov/news-events/nih-research-matters/antiviral-drug-did-not-improve-long-covid-symptoms
  - (clinical trial health) [The Clinical Trial Vanguard] 09/26/2026, 07:28 AM, +0000 UTC — Platform Trials Are Rewriting the Rules of Evidence Generation. Regulators Haven’t Caught Up.
    
    Link: https://www.clinicaltrialvanguard.com/opinion/platform-trials-are-rewriting-the-rules-of-evidence-generation-regulators-havent-caught-up/
  - (FDA recall health) [NBC 5 Dallas-Fort Worth] 09/29/2026, 10:22 AM, +0000 UTC — FDA recalls more than 13k bottles of blood pressure medication after quality issue
    
    Link: https://www.nbcdfw.com/news/local/recall-alert-local/fda-recalls-more-than-13000-bottles-of-blood-pressure-medication-after-quality-issue/4083976/
  - (FDA recall health) [The Hill] 09/28/2026, 06:54 PM, +0000 UTC — Blood pressure medication recalled nationwide under FDA’s Class II risk level
    
    Link: https://thehill.com/homenews/6115677-blood-pressure-medication-recalled-nationwide-under-fdas-class-ii-risk-level/
  - (FDA recall health) [EatingWell] 09/29/2026, 02:42 PM, +0000 UTC — The FDA Issued a Recall on Sugar Due to Contamination
    
    Link: https://www.eatingwell.com/sugar-recall-sept-2026-12146967
  - (FDA recall health) [dallasnews.com] 09/28/2026, 11:10 PM, +0000 UTC — FDA recalls more than 13,000 bottles of blood pressure medication after quality issue
    
    Link: https://www.dallasnews.com/news/public-health/article/chlorthalidone-blood-pressure-tablets-recalled-fda-22453633.php
  - (FDA recall health) [Good Housekeeping] 09/27/2026, 05:06 PM, +0000 UTC — FDA Announces New Nationwide Blood Pressure Medication Recall
    
    Link: https://www.goodhousekeeping.com/health/a73839435/fda-new-blood-pressure-medicine-recall/
  - (FDA recall health) [USA Today] 09/25/2026, 03:16 PM, +0000 UTC — Thyroid medicine recall receives FDA's highest risk level
    
    Link: https://www.usatoday.com/story/money/consumer-protection/recalls-alerts/2026/09/24/thyroid-tablet-medicine-recall-fda/91916444007/
  - (FDA recall health) [wusa9.com] 09/28/2026, 02:59 PM, +0000 UTC — Blood pressure medication recalled nationwide after failing FDA dissolution testing
    
    Link: https://www.wusa9.com/article/news/nation-world/blood-pressure-medication-recall/507-756358e0-3933-4870-a1f6-5f25d9512046
  - (FDA recall health) [LiveNOW from FOX] 09/24/2026, 07:52 PM, +0000 UTC — Thyroid medication recall upgraded to FDA's highest risk level
    
    Link: https://www.livenowfox.com/news/thyroid-medication-recall-vitruvias-therapeutics-class-i
  - (FDA recall health) [NewsNation] 09/24/2026, 06:11 PM, +0000 UTC — FDA elevates thyroid tablet recall to most serious level
    
    Link: https://www.newsnationnow.com/health/fda-thyroid-tablet-recall-class-i/
  - (FDA recall health) [Houston Chronicle] 09/28/2026, 04:26 PM, +0000 UTC — FDA updates recall of blood pressure medication with Class II risk level
    
    Link: https://www.houstonchronicle.com/news/houston-texas/trending/article/fda-class-ii-chlorthalidone-recall-22448678.php
  - (FDA recall health) [News4JAX] 09/28/2026, 08:15 PM, +0000 UTC — Thousands of bottles of blood pressure medication recalled nationwide
    
    Link: https://www.news4jax.com/news/local/2026/09/28/thousands-of-bottles-of-blood-pressure-medication-recalled-nationwide/
  - (FDA recall health) [Bergen Record] 09/29/2026, 05:24 PM, +0000 UTC — Company recalling 25K bottles of blood pressure medication, FDA says
    
    Link: https://www.northjersey.com/story/news/2026/09/29/fda-recalls-25k-bottles-blood-pressure-medication/92005192007/