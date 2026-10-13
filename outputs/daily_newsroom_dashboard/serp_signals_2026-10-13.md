# LIVE SIGNAL DATA — SerpAPI Pre-Fetch
The following signals were fetched from SerpAPI Google News and SerpAPI Google Trends immediately before this pipeline run. Treat Google Trends as AVAILABLE when this section contains a Google Trends block. Use it as the primary search_velocity input for Skills 01–05 (Signal Listener through Trend Strength Scorer). Use the Google News Radar as the broad discovery layer for news-led health topics, including topics that do not yet appear in Google Trends. Prioritize topics with convergence across News, Trends, primary/institutional sources, and credible publisher coverage.

## Google Trends — Trending Now (US / Health, real-time)
Terms with a "Why:" line have a confirmed real-world news story driving the spike; terms without one are a real-time signal only, not yet grounded in a specific story.
  - amazon acetaminophen recall aurobindo pharma
    Why: "This Amazon brand of medication is being recalled. See the affected drug" — USA Today
  - retatrutide
    Why: "Beyond Ozempic? New Weight Loss Drug Shows Stunning Results in Major Clinical Trial" — SciTechDaily
  - west nile virus north carolina
    Why: "Two North Carolinians dead from West Nile Virus" — WRAL

## Google Trends — 7-Day Interest (US)
  - **health**: latest=91, peak=100, 7d-delta=+0
    Rising related: talarico mental health, james talarico mental health, mike ditka health, mike love health, lane johnson mental health, world mental health day 2026, world mental health day, explain the health benefits and potential side effects of taking magnesium glycinate daily
  - **wellness**: latest=47, peak=100, 7d-delta=-5
    Rising related: elemental wellness club, little luxe wellness lodge, akumal bay beach & wellness resort, a cure for wellness cast, a cure for wellness, cure for wellness, the cure for wellness, taylor dukes wellness
  - **nutrition**: latest=81, peak=100, 7d-delta=-9
    Rising related: supplemental nutrition assistance program new rules, sava nutrition, organised nutrition, nutrition facts, what is nutrition, nutrition label, nutrition calculator, nutrition near me
  - **fitness**: latest=15, peak=100, 7d-delta=+0
    Rising related: fitness tracker review, coworking space near me, standing desk review, electric cars comparison, learn golang, tax software comparison, air purifier review, online banking review
  - **food safety**: latest=71, peak=100, 7d-delta=-3
    Rising related: dented cans food safety risks, baris yucel food safety fine, what does haccp stand for in food safety, food safety certification texas, what is food safety, food safety certification, state food safety, food safety training
  - **diet**: latest=81, peak=100, 7d-delta=-10
    Rising related: diet soda weight management study, the fatal diet meals, university of liverpool diet soda study, the fatal diet meals drama, walter willett daily diet, walter willett diet, the fatal diet meals short drama, pink diet coke cans
  - **weight loss**: latest=74, peak=100, 7d-delta=+16
    Rising related: susan dell weight loss, shane gillis weight loss, katy mixon weight loss, american housewife, katy mixon, eric stonestreet weight loss, explain how semaglutide works for weight loss and its primary mechanism, tory johnson weight loss
  - **mental health**: latest=88, peak=100, 7d-delta=+2
    Rising related: talarico mental health facility, talarico, james talarico, talarico mental health, james talarico mental health, talerico mental health, stephen a smith mental health, is talarico in a mental health facility
  - **gut health**: latest=50, peak=100, 7d-delta=+4
    Rising related: gut health uk, best way to improve gut health, good gut health, what is gut health, gut health foods, probiotics, gut health probiotics, foods for gut health

Top rising related queries from Google Trends:
  - talarico mental health
  - james talarico mental health
  - mike ditka health
  - mike love health
  - lane johnson mental health
  - world mental health day 2026
  - world mental health day
  - explain the health benefits and potential side effects of taking magnesium glycinate daily
  - elemental wellness club
  - little luxe wellness lodge
  - akumal bay beach & wellness resort
  - a cure for wellness cast
  - a cure for wellness
  - cure for wellness
  - the cure for wellness
  - taylor dukes wellness
  - supplemental nutrition assistance program new rules
  - sava nutrition
  - organised nutrition
  - nutrition facts

## Google News Radar — Recent Health Topics (144 unique across 12 queries; showing 60)
Treat these headlines as the broad radar of news-led health topics. The Signal Listener must consider this radar before narrowing to retained candidates.
  - (health) [blog.google] 10/12/2026, 01:11 PM, +0000 UTC — How we’re making Google Health and Fitbit Air smarter than ever
    
    Link: https://blog.google/products-and-platforms/products/google-health/fitbit-google-health-updates/
  - (health) [KFF] 10/07/2026, 04:28 AM, +0000 UTC — KFF Health Tracking Poll: Health Care Issues in the Lead-Up to the 2026 Midterm Election
    
    Link: https://www.kff.org/public-opinion/kff-health-tracking-poll-health-care-issues-in-the-lead-up-to-the-2026-midterm-election/
  - (health) [OHSU News] 10/09/2026, 04:20 PM, +0000 UTC — Late-night eating may be bad for your liver, study suggests
    
    Link: https://news.ohsu.edu/2026/10/09/late-night-eating-may-be-bad-for-your-liver-study-suggests
  - (health) [World Health Organization (WHO)] 10/09/2026, 10:55 AM, +0000 UTC — WHO urges shift from institutional to community-based mental health care
    
    Link: https://www.who.int/news/item/09-10-2026-who-urges-shift-from-institutional-to-community-based-mental-health-care
  - (health) [North Carolina Health News] 10/07/2026, 08:30 AM, +0000 UTC — NC treasurer: Atrium affordability program could bankrupt state employees’ health plan
    
    Link: https://www.northcarolinahealthnews.org/2026/10/07/atrium-affordability-program-state-health-plan/
  - (health) [Health.com] 10/07/2026, 07:00 AM, +0000 UTC — The Best Time to Eat Dinner for Better Metabolism and Sleep, According to Science
    
    Link: https://www.health.com/when-to-eat-dinner-for-better-metabolism-and-sleep-12162013
  - (health) [Pew Research Center] 10/07/2026, 01:48 PM, +0000 UTC — What Do Health and Wellness Influencers Post About?
    
    Link: https://www.pewresearch.org/data-labs/2026/10/07/what-do-health-and-wellness-influencers-post-about/
  - (health) [European Commission] 10/10/2026, 07:10 AM, +0000 UTC — World Mental Health Day: let’s talk and listen
    
    Link: https://commission.europa.eu/news-and-media/news/world-mental-health-day-lets-talk-and-listen-2026-10-10_en
  - (health) [Virginia Department of Health (.gov)] 10/09/2026, 09:27 PM, +0000 UTC — Virginia Department of Health Closes Little Wicomico River to Shellfish Harvesting
    
    Link: https://www.vdh.virginia.gov/news/public-relations-contacts/2026-regional-news-releases/virginia-department-of-health-closes-little-wicomico-river-to-shellfish-harvesting/
  - (health) [NPR] 10/08/2026, 09:00 AM, +0000 UTC — Medical debt is crushing hospital patients in LA. Health officials may have a fix
    
    Link: https://www.npr.org/2026/10/08/nx-s1-5991633/hospital-california-healthcare-medical-debt
  - (health) [The New York Times] 10/07/2026, 06:36 PM, +0000 UTC — A Public Health-Minded Senator Asks: What Comes After Trump and Kennedy?
    
    Link: https://www.nytimes.com/2026/10/07/us/politics/patty-murray-public-health.html
  - (health) [Notre Dame News] 10/08/2026, 05:54 PM, +0000 UTC — Study finds positive parenting teaches children how to experience joy—and could lead to better mental health
    
    Link: https://news.nd.edu/news/study-finds-positive-parenting-teaches-children-how-to-experience-joyand-could-lead-to-better-mental-health/
  - (wellness) [The New York Times] 10/07/2026, 06:41 PM, +0000 UTC — Video: Wellness Culture Is Coming for Polyester
    
    Link: https://www.nytimes.com/video/style/100000011173558/wellness-culture-is-coming-for-polyester.html
  - (wellness) [shrewsbury-ma.gov] 10/08/2026, 12:29 AM, +0000 UTC — Winter Wellness Presentation - October 2026
    
    Link: https://shrewsburyma.gov/CivicAlerts.aspx?AID=9770
  - (wellness) [San Diego County News Center] 10/08/2026, 09:02 PM, +0000 UTC — Mental Wellness Begins with a Moment, Don’t Wait to Take Yours
    
    Link: https://www.countynewscenter.com/mental-wellness-begins-with-a-moment-dont-wait-to-take-yours/
  - (wellness) [SBU News] 10/08/2026, 07:50 PM, +0000 UTC — Feeling Better, Working Better: Employee Wellness Fair Connects Stony Brook Employees with Resources
    
    Link: https://news.stonybrook.edu/university/feeling-better-working-better-employee-wellness-fair-connects-stony-brook-employees-with-resources/
  - (wellness) [The University of Utah] 10/08/2026, 01:07 AM, +0000 UTC — Student Health & Wellness awarded $500,000 to advance campus suicide prevention
    
    Link: https://attheu.utah.edu/announcements/student-health-wellness-awarded-500000-to-advance-campus-suicide-prevention/
  - (wellness) [New York Post] 10/12/2026, 03:26 PM, +0000 UTC — Exclusive | Gen Z turns college ‘wellness darties’ trend into big business: ‘We have a different mindset’
    
    Link: https://nypost.com/2026/10/12/lifestyle/how-wellness-darties-became-big-business-on-college-campuses/
  - (wellness) [Case Western Reserve University] 10/08/2026, 11:00 AM, +0000 UTC — Complete fall wellness activities to earn incentives in 2027
    
    Link: https://case.edu/news/complete-fall-wellness-activities-earn-incentives-2027
  - (wellness) [National Police Association] 10/09/2026, 07:00 AM, +0000 UTC — The National Police Association Endorses the Officer Wellness and Peer Support Act of 2026
    
    Link: https://nationalpolice.org/the-national-police-association-endorses-the-officer-wellness-and-peer-support-act-of-2026/
  - (wellness) [The Harvard Crimson] 10/07/2026, 07:00 AM, +0000 UTC — Harvard Is Caving to Wellness Culture
    
    Link: https://www.thecrimson.com/article/2026/10/8/nelson-harvard-wellness-culture/
  - (wellness) [The Santa Barbara Independent] 10/09/2026, 04:52 AM, +0000 UTC — Santa Barbara Neighborhood Clinics Hosts 1st Annual Health & Wellness Fair Featuring DJ Darla, Aztec Dancers, and Hourly Games
    
    Link: https://www.independent.com/2026/10/08/santa-barbara-neighborhood-clinics-hosts-1st-annual-health-wellness-fair-featuring-dj-darla-aztec-dancers-and-hourly-games/
  - (wellness) [St. Cloud State TODAY] 10/08/2026, 08:56 PM, +0000 UTC — Puppy Yoga is one of many ways CAPS supports SCSU health and wellness
    
    Link: https://today.stcloudstate.edu/2026/10/08/puppy-yoga-is-one-of-many-ways-caps-is-supporting-health-and-wellness-at-scsu/
  - (wellness) [Army.mil] 10/08/2026, 04:02 PM, +0000 UTC — Ready anywhere: How virtual wellness coaching fits military life
    
    Link: https://www.army.mil/article/296026/ready_anywhere_how_virtual_wellness_coaching_fits_military_life
  - (medical study) [Susquehanna University] 10/08/2026, 12:58 PM, +0000 UTC — Alumni win prestigious grants to further medical research
    
    Link: https://www.susqu.edu/alumni-win-prestigious-grants-to-further-medical-research/
  - (medical study) [blog.google] 10/08/2026, 10:43 PM, +0000 UTC — Study in The Lancet suggests AI could improve patient-physician relationships.
    
    Link: https://blog.google/innovation-and-ai/technology/health/amie-clinical-study-lancet/
  - (medical study) [Beth Israel Deaconess Medical Center] 10/09/2026, 02:10 PM, +0000 UTC — BIDMC Researchers Conduct First Real-World Study of Safety and Quality of Patient-Facing AI in Primary Care
    
    Link: https://bidmc.org/news-stories/all-news-stories/news/2026/10/bidmc-research-shows-safety-quality-of-ai-in-primary-care
  - (medical study) [UT Southwestern] 10/12/2026, 02:31 PM, +0000 UTC — Protein puts brakes on intestinal inflammation, UTSW study finds: Newsroom
    
    Link: https://www.utsouthwestern.edu/newsroom/articles/year-2026/oct-protein-intestinal-inflammation.html
  - (medical study) [Rutgers University] 10/08/2026, 07:07 PM, +0000 UTC — How a U.S. Ban on Lab-Modified Opioids Could Stifle Medical Research
    
    Link: https://www.rutgers.edu/news/how-us-ban-lab-modified-opioids-could-stifle-medical-research
  - (medical study) [Pew Research Center] 10/07/2026, 01:48 PM, +0000 UTC — Which Health and Wellness Influencers Talk About Medical Topics? Mostly Healthcare Professionals
    
    Link: https://www.pewresearch.org/data-labs/2026/10/07/which-health-and-wellness-influencers-talk-about-medical-topics-mostly-healthcare-professionals/
  - (medical study) [Nature] 10/09/2026, 10:26 AM, +0000 UTC — AI-assisted scoping review of code sharing in clinical prediction model research
    
    Link: https://www.nature.com/articles/s41591-026-04691-1
  - (medical study) [University of Cincinnati] 10/09/2026, 10:59 PM, +0000 UTC — UC researcher to launch national study with $2.5 million NIH grant
    
    Link: https://www.uc.edu/news/articles/2026/10/uc-researcher-to-launch-national-study-with-25-million-nih-grant.html
  - (medical study) [The New York Times] 10/08/2026, 10:30 PM, +0000 UTC — Clinical Trial Indicates A.I. Chatbots Could Aid Urgent Care
    
    Link: https://www.nytimes.com/2026/10/08/technology/ai-chatbots-urgent-care.html
  - (medical study) [Azusa Pacific University] 10/12/2026, 08:12 AM, +0000 UTC — Student Spotlight: Mia Pierce ’27 Prepares for Career in Medical Research
    
    Link: https://www.apu.edu/articles/mia-pierce-prepares-for-career-in-medical-research/
  - (medical study) [Medical Xpress] 10/09/2026, 03:00 PM, +0000 UTC — Late-night eating linked to higher rates of fatty liver disease and cirrhosis
    
    Link: https://medicalxpress.com/news/2026-10-late-night-linked-higher-fatty.html
  - (medical study) [News-Medical] 10/07/2026, 07:35 PM, +0000 UTC — Study uncovers a protective role for microglia in Parkinson's disease
    
    Link: https://www.news-medical.net/news/20261007/Study-uncovers-a-protective-role-for-microglia-in-Parkinsons-disease.aspx
  - (clinical trial health) [The Clinical Trial Vanguard] 10/09/2026, 06:55 AM, +0000 UTC — Patient-Owned Health Data Model Reduces Clinical Trial Recruitment Redundancy
    
    Link: https://www.clinicaltrialvanguard.com/news/patient-owned-health-data-model-reduces-clinical-trial-recruitment-redundancy/
  - (clinical trial health) [Clinical Leader] 10/13/2026, 05:18 AM, +0000 UTC — Can A Universal Health Screening Help Stop Clinical Trial Dropouts?
    
    Link: https://www.clinicalleader.com/doc/can-a-universal-health-screening-help-stop-clinical-trial-dropouts-0001
  - (clinical trial health) [Milken Institute] 10/13/2026, 04:02 PM, +0000 UTC — Enabling Access to Clinical Research: An Action Plan for Policy and Practice Change
    
    Link: https://milkeninstitute.org/content-hub/research-and-reports/reports/enabling-access-clinical-research-action-plan-policy-and-practice-change
  - (clinical trial health) [UC Davis Health] 10/07/2026, 03:06 PM, +0000 UTC — Clinical trial tests AI-assisted medication device for older adults with memory loss
    
    Link: https://health.ucdavis.edu/news/headlines/clinical-trial-tests-ai-assisted-medication-device-for-older-adults-with-memory-loss/2026/09
  - (clinical trial health) [The Daily Texan] 10/13/2026, 03:42 AM, +0000 UTC — Dell Medical School partners with federal program to standardize clinical trials
    
    Link: https://thedailytexan.com/2026/10/12/dell-medical-school-partners-with-federal-program-to-standardize-clinical-trials/
  - (clinical trial health) [Clinical Trials Arena] 10/12/2026, 04:53 PM, +0000 UTC — Women’s health landscape shifting, but systemic hurdles remain
    
    Link: https://www.clinicaltrialsarena.com/features/womens-health-landscape-shifting-systemic-hurdles-remain-2/
  - (clinical trial health) [Penn LDI] 10/12/2026, 04:41 PM, +0000 UTC — What Would It Take to Make Clinical Trials More Diverse?
    
    Link: https://ldi.upenn.edu/our-work/research-updates/what-would-it-take-to-make-clinical-trials-more-diverse/
  - (clinical trial health) [PR Newswire] 10/08/2026, 01:15 PM, +0000 UTC — Verana Health and Bitfount Collaborate to Simplify Prescreening for Ophthalmic Clinical Trials
    
    Link: https://www.prnewswire.com/news-releases/verana-health-and-bitfount-collaborate-to-simplify-prescreening-for-ophthalmic-clinical-trials-302901571.html
  - (clinical trial health) [Fierce Biotech] 10/07/2026, 03:25 PM, +0000 UTC — ARPA-H unveils Surpass program to accelerate and expand clinical trials
    
    Link: https://www.fiercebiotech.com/cro/arpa-h-unveils-surpass-program-accelerate-and-expand-clinical-trials
  - (clinical trial health) [Keck School of Medicine of USC] 10/07/2026, 02:34 PM, +0000 UTC — USC launches clinical trial of psilocybin and mindfulness meditation for depression
    
    Link: https://keck.usc.edu/news/usc-launches-clinical-trial-of-psilocybin-and-mindfulness-meditation-for-depression/
  - (clinical trial health) [Business Wire] 10/13/2026, 12:00 PM, +0000 UTC — IgniteData and RealTime Announce Partnership to Expand Clinical Trial Data Transfer Capabilities Across Clinical Research Organizations in the U.S. and Key Global Markets
    
    Link: https://www.businesswire.com/news/home/20261013274056/en/IgniteData-and-RealTime-Announce-Partnership-to-Expand-Clinical-Trial-Data-Transfer-Capabilities-Across-Clinical-Research-Organizations-in-the-U.S.-and-Key-Global-Markets
  - (clinical trial health) [Stock Titan] 10/08/2026, 08:00 PM, +0000 UTC — Global gout cases are expected to rise 70% over 25 years. XORTX plans to apply to study a gout drug in Canada.
    
    Link: https://www.stocktitan.net/news/XRTX/xortx-outlines-anticipated-health-canada-clinical-trial-application-henvf4zhjx9m.html
  - (FDA recall health) [U.S. Food and Drug Administration (.gov)] 10/09/2026, 04:30 PM, +0000 UTC — Outbreak Investigation of Salmonella: Sprouts (September 2026)
    
    Link: https://www.fda.gov/food/outbreaks-foodborne-illness/outbreak-investigation-salmonella-sprouts-september-2026
  - (FDA recall health) [NEWStalk 870] 10/09/2026, 08:34 PM, +0000 UTC — Baby-Infant Sleep Aid Recalled by FDA Over Undisclosed Alcohol Content
    
    Link: https://newstalk870.am/fda-recalls-baby-infant-sleep-aid/
  - (FDA recall health) [Prevention] 10/08/2026, 02:56 PM, +0000 UTC — Millions of Bottles of Eye Drops Recalled Nationwide, FDA Warns
    
    Link: https://www.prevention.com/health/a74079654/fda-updates-eye-drop-recall/
  - (FDA recall health) [U.S. Food and Drug Administration (.gov)] 10/07/2026, 02:00 PM, +0000 UTC — Investigations of Foodborne Illness Outbreaks
    
    Link: https://www.fda.gov/food/outbreaks-foodborne-illness/investigations-foodborne-illness-outbreaks
  - (FDA recall health) [WPLG Local 10] 10/09/2026, 08:16 PM, +0000 UTC — FDA: Gatorade recalls 122,000 cases over food dyes
    
    Link: https://www.local10.com/food/2026/10/09/fda-gatorade-recalls-122000-cases-over-food-dyes/
  - (FDA recall health) [MedShadow Foundation] 10/07/2026, 03:59 PM, +0000 UTC — FDA Recalls and Warnings: Amazon Acetaminophen, Millions of Eye Drops and More Compounded Glutathione
    
    Link: https://medshadow.org/drug-updates-recalls/fda-recalls-and-warnings/amazon-acetaminophen-millions-of-eye-drops-compounded-glutathione/
  - (FDA recall health) [Yahoo] 10/12/2026, 07:55 PM, +0000 UTC — FDA Announces Recall of Smoked Fish Sold in 6 States
    
    Link: https://www.yahoo.com/news/us/articles/fda-announces-recall-smoked-fish-195520545.html
  - (FDA recall health) [ABC News - Breaking News, Latest News and Videos] 10/09/2026, 03:58 PM, +0000 UTC — 1 lot of baby product voluntarily recalled over alcohol content
    
    Link: https://abcnews.com/GMA/Family/1-lot-baby-product-voluntarily-recalled-alcohol-content/story?id=137123138
  - (FDA recall health) [Packaging Digest] 10/12/2026, 10:45 PM, +0000 UTC — Q3 FDA Recalls for Pharma & Medical Packaging Mishaps
    
    Link: https://www.packagingdigest.com/pharma-medical/q3-fda-recalls-for-pharma-medical-packaging-mishaps
  - (FDA recall health) [The Healthy @Reader's Digest] 10/09/2026, 05:35 AM, +0000 UTC — Supplement Powder Recall: FDA Warns of Potential ‘Cardiovascular Problems’
    
    Link: https://www.thehealthy.com/news/supplement-powder-recall-october-2026/
  - (FDA recall health) [WYFF] 10/12/2026, 09:21 AM, +0000 UTC — FDA: Baby supplement sold online recalled after testing discovers undeclared alcohol
    
    Link: https://www.wyff4.com/article/baby-product-sold-online-recall-undeclared-alcohol/74105221
  - (FDA recall health) [Health.com] 10/09/2026, 08:00 PM, +0000 UTC — FDA Announces Pre-Workout Recall After Testing Finds Dangerous Ingredient
    
    Link: https://www.health.com/pre-workout-recall-illegal-ingredient-october-2026-12166677