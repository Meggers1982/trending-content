# LIVE SIGNAL DATA — SerpAPI Pre-Fetch
The following signals were fetched from SerpAPI Google News and SerpAPI Google Trends immediately before this pipeline run. Treat Google Trends as AVAILABLE when this section contains a Google Trends block. Use it as the primary search_velocity input for Skills 01–05 (Signal Listener through Trend Strength Scorer). Use the Google News Radar as the broad discovery layer for news-led health topics, including topics that do not yet appear in Google Trends. Prioritize topics with convergence across News, Trends, primary/institutional sources, and credible publisher coverage.

## Google Trends — Trending Now (US / Health, real-time)
Terms with a "Why:" line have a confirmed real-world news story driving the spike; terms without one are a real-time signal only, not yet grounded in a specific story.
  - olmesartan
    Why: "Thousands of blood pressure medication bottles recalled nationwide after pills fail quality test" — Fox Business
  - measles death
    Why: "Child Dies From Measles in New York State’s First Fatal Case in 30 Years" — The New York Times

## Google Trends — 7-Day Interest (US)
  - **health**: latest=91, peak=100, 7d-delta=-1
    Rising related: unitypoint health iowa lutheran hospital, explain the daylight savings schedule, clock adjustment rules, and health effects, michael wilbon health issues, mens mental health month, dignity health sports park, connect for health colorado, health insurance agency, ambetter health insurance
  - **wellness**: latest=52, peak=100, 7d-delta=-8
    Rising related: why did the us ease access to unapproved wellness peptides and what are the safety concerns?, stc wellness city, corporate wellness programs, wellness company emergency kit, the wellness company emergency kit, the wellness company medical emergency kit, ai agents, ai image enhancer
  - **nutrition**: latest=91, peak=100, 7d-delta=+0
    Rising related: supplemental nutrition assistance program state waivers, fda infant formula nutrition updates, kona ice nutrition, deep south nutrition, mcrib nutrition facts, roasted pumpkin seeds nutrition, supplemental nutrition assistance program, pumpkin seed nutrition
  - **fitness**: latest=40, peak=100, 7d-delta=+0
    Rising related: planet fitness customer retention issues, zamaya fitness resort, fitness international ftc lawsuit, university rankings, fitness warrior nation, la fitness halloween hours, google fitbit edge fitness tracker test, is planet fitness open on halloween
  - **food safety**: latest=37, peak=100, 7d-delta=-22
    Rising related: costco food safety alert, world food safety day date, at which temperature can cooked chicken breast be hot held, what does haccp stand for in food safety, safety pins, king county food safety rating, rbs certification, one of the most important reasons for using only reliable water sources is to reduce
  - **diet**: latest=83, peak=100, 7d-delta=-8
    Rising related: diet coke mini fridge, diet coke advent calendar, diet coke fridge, diet coke blanket, diet coke, diet food, mediterranean diet, mediterranean
  - **weight loss**: latest=32, peak=100, 7d-delta=-4
    Rising related: catelynn baltierra weight loss, catelynn lowell 30 lb weight loss, eli lilly retatrutide weight loss results, ashley hinson before weight loss, stevie nicks weight loss, goodrx employer weight loss program, john goodman weight loss interview, eli lilly weight loss sales
  - **mental health**: latest=77, peak=100, 7d-delta=-6
    Rising related: haley stevens mental health, is november men's mental health month, mens mental health month november, is november mens mental health month, november mental health month, when is mens mental health month, mens mental health month, men's mental health month
  - **gut health**: latest=45, peak=100, 7d-delta=-3
    Rising related: hack your health the secrets of your gut, what is gut health, gut health foods, gut health probiotics, probiotics, probiotic gut health, foods for gut health, probiotics for gut health

Top rising related queries from Google Trends:
  - unitypoint health iowa lutheran hospital
  - explain the daylight savings schedule, clock adjustment rules, and health effects
  - michael wilbon health issues
  - mens mental health month
  - dignity health sports park
  - connect for health colorado
  - health insurance agency
  - ambetter health insurance
  - why did the us ease access to unapproved wellness peptides and what are the safety concerns?
  - stc wellness city
  - corporate wellness programs
  - wellness company emergency kit
  - the wellness company emergency kit
  - the wellness company medical emergency kit
  - ai agents
  - ai image enhancer
  - supplemental nutrition assistance program state waivers
  - fda infant formula nutrition updates
  - kona ice nutrition
  - deep south nutrition

## Google News Radar — Recent Health Topics (144 unique across 12 queries; showing 60)
Treat these headlines as the broad radar of news-led health topics. The Signal Listener must consider this radar before narrowing to retained candidates.
  - (health) [KFF] 10/30/2026, 07:28 PM, +0000 UTC — 9 Things to Watch for the 2027 ACA Open Enrollment Period
    
    Link: https://www.kff.org/affordable-care-act/9-things-to-watch-for-the-2027-aca-open-enrollment-period/
  - (health) [County of San Luis Obispo (.gov)] 10/27/2026, 11:21 PM, +0000 UTC — Public Health Confirms Five Shiga toxin-producing E. Coli Cases; Local Farm Suspected as Potential S
    
    Link: https://www.slocounty.ca.gov/departments/slo-health/public-health/department-news/public-health-confirms-five-shiga-toxin-producing-e-coli-cases;-local-farm-suspected-as-potential-s
  - (health) [USDA (.gov)] 10/29/2026, 07:00 AM, +0000 UTC — Screwworm.gov | Animal and Plant Health Inspection Service
    
    Link: https://www.aphis.usda.gov/animals/animal-health/livestock-and-poultry-disease/stop-screwworm
  - (health) [ESPN] 11/02/2026, 07:15 PM, +0000 UTC — Wilbon taking leave of absence from ESPN to address health issues
    
    Link: https://www.espn.com/nba/story/_/id/50360086/wilbon-taking-leave-absence-espn-address-health-issues
  - (health) [Florida State University News] 10/30/2026, 09:41 PM, +0000 UTC — FSU Health opens new research and collaboration building, names it for Florida Ag Commissioner Wilton Simpson
    
    Link: https://news.fsu.edu/news/university-news/2026/10/30/fsu-health-opens-new-research-and-collaboration-building-names-it-for-florida-ag-commissioner-wilton-simpson/
  - (health) [World Health Organization (WHO)] 10/28/2026, 08:04 AM, +0000 UTC — Climate change is a growing health emergency, Lancet Countdown warns
    
    Link: https://www.who.int/news/item/28-10-2026-climate-change-is-a-growing-health-emergency--lancet-countdown-warns
  - (health) [NPR] 11/01/2026, 12:00 PM, +0000 UTC — It's ACA open enrollment time. Here are the changes for health insurance shoppers
    
    Link: https://www.npr.org/2026/11/01/nx-s1-6023423/aca-open-enrollment-health-insurance
  - (health) [Nature] 10/28/2026, 01:17 AM, +0000 UTC — Macrophage biology and immunoregulation in health and disease
    
    Link: https://www.nature.com/articles/s41423-026-01486-9
  - (health) [PBS] 11/02/2026, 10:09 PM, +0000 UTC — Why are Americans paying more for health insurance? Experts give 3 reasons
    
    Link: https://www.pbs.org/newshour/nation/why-health-insurance-premiums-are-rising-according-to-experts
  - (health) [Centers for Disease Control and Prevention | CDC (.gov)] 10/30/2026, 07:00 AM, +0000 UTC — Information for Travelers Returning from Ebola-Affected Areas
    
    Link: https://www.cdc.gov/ebola/situation-summary/returning-travelers.html
  - (health) [Reuters] 10/30/2026, 09:17 PM, +0000 UTC — US health department to remove broad black box warning from three estrogen patch products
    
    Link: https://www.reuters.com/legal/litigation/us-health-department-remove-broad-black-box-warning-three-estrogen-patch-2026-10-30/
  - (health) [World Economic Forum] 10/28/2026, 12:48 PM, +0000 UTC — Global Health Threats: 17 Risks Identified by 2100 | WEF
    
    Link: https://www.weforum.org/stories/health-and-healthcare-systems/global-health-threats-17-risks-identified-2100
  - (wellness) [McKinsey & Company] 11/03/2026, 12:00 AM, +0000 UTC — Future of Wellness 2027: Inside the $2.7 trillion takeover
    
    Link: https://www.mckinsey.com/industries/consumer-packaged-goods/our-insights/future-of-wellness-trends
  - (wellness) [San Bernardino County (.gov)] 10/29/2026, 04:42 PM, +0000 UTC — Celebrating wellness and community across generations
    
    Link: https://main.sbcounty.gov/2026/10/29/celebrating-wellness-and-community-across-generations/
  - (wellness) [Washington and Lee University] 10/28/2026, 09:34 PM, +0000 UTC — How to Earn a Wellness Token for Environmental Wellbeing
    
    Link: https://www.wlu.edu/office-of-sustainability/sustainability-how-to/how-to-earn-a-wellness-token-for-environmental-wellbeing
  - (wellness) [FOX Sports] 11/01/2026, 09:40 PM, +0000 UTC — Kirk cousins discusses his post td "wellness-celly"
    
    Link: https://www.foxsports.com/watch-vertical/fmc-tl39phjh4w7uphyt
  - (wellness) [Meredith College] 11/03/2026, 01:03 PM, +0000 UTC — Meredith College Wellness Day on November 3
    
    Link: https://www.meredith.edu/news/meredith-college-wellness-day-on-november-3/
  - (wellness) [Army.mil] 10/28/2026, 03:52 PM, +0000 UTC — 2026 Fort McCoy Wellness Fair business showcase gave event-goers wide variety of wellness information
    
    Link: https://www.army.mil/article/296401/2026_fort_mccoy_wellness_fair_business_showcase_gave_event_goers_wide_variety_of_wellness_information
  - (wellness) [Texas A&M University-Commerce] 10/27/2026, 08:26 PM, +0000 UTC — ETAMU Professor Builds Global Community Through Wellness Counseling
    
    Link: https://www.etamu.edu/news/etamu-professor-builds-global-community-through-wellness-counseling/
  - (wellness) [Harvard T.H. Chan School of Public Health] 10/28/2026, 04:01 PM, +0000 UTC — Health and wellness for all: Content creation on social media
    
    Link: https://hsph.harvard.edu/news/health-and-wellness-for-all-content-creation-on-social-media/
  - (wellness) [VCU Health] 10/29/2026, 03:51 PM, +0000 UTC — Wellness Week at the VCU Health Hub at 25th helps residents connect with local resources to address health needs
    
    Link: https://www.vcuhealth.org/news/wellness-week-at-the-vcu-health-hub-at-25th-helps-residents-connect-with-local-resources-to-address-health-needs/
  - (wellness) [Skidmore College] 10/29/2026, 07:00 AM, +0000 UTC — Jakob Roze ’16: A full-circle journey in fitness and wellness
    
    Link: https://www.skidmore.edu/news/2026/1029-jakob-roze.php
  - (wellness) [WEAU] 11/01/2026, 11:28 PM, +0000 UTC — Wellness fair brings nontraditional solutions
    
    Link: https://www.weau.com/2026/11/01/wellness-fair-brings-nontraditional-solutions/
  - (wellness) [PwC] 10/29/2026, 02:54 AM, +0000 UTC — Winning in wellness: Creating trust and driving growth
    
    Link: https://www.strategyand.pwc.com/gx/en/industries/consumer-retail/winning-in-wellness.html
  - (medical study) [Stanford Report] 10/27/2026, 08:35 PM, +0000 UTC — Study refines our understanding of long COVID
    
    Link: https://news.stanford.edu/stories/2026/10/long-covid-health-affects-study-design
  - (medical study) [HHMI] 10/28/2026, 07:00 AM, +0000 UTC — PhD and Postdoc Transition Program | Gilliam Fellows
    
    Link: https://www.hhmi.org/programs/gilliam-fellows
  - (medical study) [Penn LDI] 11/03/2026, 11:02 AM, +0000 UTC — Study Highlights Hidden Obstacles to Effective Asthma Care
    
    Link: https://ldi.upenn.edu/our-work/research-updates/study-highlights-hidden-obstacles-to-effective-asthma-care/
  - (medical study) [Science Daily] 11/02/2026, 04:14 AM, +0000 UTC — Even moderate drinking linked to cancer and early death, major study finds
    
    Link: https://www.sciencedaily.com/releases/2026/10/261031221159.htm
  - (medical study) [Universities of Wisconsin] 10/30/2026, 01:07 PM, +0000 UTC — A deeper understanding: UWL students gain medical, cultural experience through Ecuador study abroad
    
    Link: https://www.wisconsin.edu/all-in-wisconsin/story/a-deeper-understanding-uwl-students-gain-medical-cultural-experience-through-ecuador-study-abroad/
  - (medical study) [Purdue University] 10/28/2026, 07:00 AM, +0000 UTC — Researchers in various studies looking for participants
    
    Link: https://www.purdue.edu/newsroom/purduetoday/2026/Q4/researchers-in-various-studies-looking-for-participants
  - (medical study) [Penn State Health News] 11/02/2026, 06:08 PM, +0000 UTC — College of Medicine researcher receives $3.1M grant from NIH to study development of stomach cancer
    
    Link: https://pennstatehealthnews.org/2026/11/college-of-medicine-researcher-receives-3-1m-grant-from-nih-to-study-development-of-stomach-cancer/
  - (medical study) [Medical Xpress] 11/02/2026, 08:20 PM, +0000 UTC — Study shows AI may improve patient discharge summaries
    
    Link: https://medicalxpress.com/news/2026-11-ai-patient-discharge-summaries.html
  - (medical study) [News-Medical] 11/02/2026, 08:12 PM, +0000 UTC — Study uncovers why pulmonary hypertension patients report symptoms of cognitive decline
    
    Link: https://www.news-medical.net/news/20261102/Study-uncovers-why-pulmonary-hypertension-patients-report-symptoms-of-cognitive-decline.aspx
  - (medical study) [Breakthrough T1D] 10/30/2026, 09:45 PM, +0000 UTC — Clinical Trials and Studies Now Enrolling!
    
    Link: https://www.breakthrought1d.org/greaternorthwest/2026/10/30/clinical-trials-and-studies-now-enrolling/
  - (medical study) [www.heart.org] 11/02/2026, 12:05 PM, +0000 UTC — Retired NFL players, notably linemen, had high risk of artery plaque, per independent study
    
    Link: https://newsroom.heart.org/news/retired-nfl-players-notably-linemen-had-high-risk-of-artery-plaque-per-independent-study
  - (medical study) [The Guardian] 11/03/2026, 01:32 PM, +0000 UTC — Babies more likely to have heart defects from Louisiana’s areas with industrial pollution, study finds
    
    Link: https://www.theguardian.com/us-news/2026/nov/04/babies-heart-defects-louisiana-industrial-pollution-study
  - (clinical trial health) [Applied Clinical Trials Online] 10/30/2026, 03:00 PM, +0000 UTC — Walmart and Care Access Plan Three More Clinical Trial Centers in Michigan, Nevada, and Texas
    
    Link: https://www.appliedclinicaltrialsonline.com/view/walmart-care-access-clinical-trial-centers-michigan-nevada-texas
  - (clinical trial health) [KCRG] 10/30/2026, 01:05 PM, +0000 UTC — What to look for in a clinical trial and why older adults should be included
    
    Link: https://www.kcrg.com/2026/10/30/what-look-clinical-trial-why-older-adults-should-be-included/
  - (clinical trial health) [Fierce Healthcare] 10/29/2026, 06:06 PM, +0000 UTC — BCBSMA, Medzown team up to match members with clinical trials
    
    Link: https://www.fiercehealthcare.com/payers/bcbsma-medzown-team-match-members-clinical-trials
  - (clinical trial health) [University of Michigan Health] 11/02/2026, 12:00 PM, +0000 UTC — Patient with rare form of diabetes finds answers in genetic testing, clinical trials
    
    Link: https://www.uofmhealth.org/health-lab/patient-rare-form-diabetes-finds-answers-genetic-testing-clinical-trials
  - (clinical trial health) [Clinical Leader] 11/03/2026, 06:39 AM, +0000 UTC — Brazil's Regulatory Transformation: Expanding Clinical Trial Participation
    
    Link: https://www.clinicalleader.com/doc/brazil-s-regulatory-transformation-expanding-clinical-trial-participation-0001
  - (clinical trial health) [Clinical Trials Arena] 10/28/2026, 05:30 PM, +0000 UTC — Walmart and Care Access to open three clinical trial centres in US
    
    Link: https://www.clinicaltrialsarena.com/news/walmart-care-access-three-trial-centres-us/
  - (clinical trial health) [Nature] 10/28/2026, 07:00 AM, +0000 UTC — Governing accelerated evidence in real-time clinical trials
    
    Link: https://www.nature.com/articles/s43856-026-01909-8
  - (clinical trial health) [HCI Innovation Group] 10/30/2026, 10:59 PM, +0000 UTC — AI and Digital Tools Could Transform Clinical Trials, but Patient Involvement Remains Critical
    
    Link: https://www.hcinnovationgroup.com/analytics-ai/article/55415806/ai-and-digital-tools-could-transform-clinical-trials-but-patient-involvement-remains-critical
  - (clinical trial health) [Cancer Health] 10/28/2026, 09:03 AM, +0000 UTC — Novel Cancer Immunotherapy Drug Generates Promising Clinical Trial Results
    
    Link: https://www.cancerhealth.com/article/novel-cancer-immunotherapy-drug-generates-promising-clinical-trial-results
  - (clinical trial health) [Yahoo Finance] 10/28/2026, 06:15 PM, +0000 UTC — ŌURA Expands Healthcare Research With First Clinical Trial Exploring GLP-1 Treatment Outcomes
    
    Link: https://finance.yahoo.com/healthcare/articles/ura-expands-healthcare-research-first-181500184.html
  - (clinical trial health) [Drug Store News] 10/27/2026, 06:13 PM, +0000 UTC — Walmart, Care Access plan 3 additional clinical trial centers
    
    Link: https://drugstorenews.com/walmart-care-access-plan-3-additional-clinical-trial-centers
  - (clinical trial health) [Community Impact Newspaper] 10/29/2026, 01:12 AM, +0000 UTC — Clinical trial center opens at Greater Houston Walmart | Katy - Fulshear
    
    Link: https://communityimpact.com/katy-fulshear/business/clinical-trial-center-opens-at-greater-houston-walmart/
  - (FDA recall health) [ABC News - Breaking News, Latest News and Videos] 11/02/2026, 02:07 PM, +0000 UTC — Over 122K cases of Gatorade recalled due to undeclared food dyes, FDA says
    
    Link: https://abcnews.com/GMA/Food/122k-cases-gatorade-recalled-due-undeclared-food-dyes/story?id=137002347
  - (FDA recall health) [The Healthy @Reader's Digest] 10/30/2026, 03:17 AM, +0000 UTC — Flour Recall: More Than 4,000 Bags Just Received the FDA’s Highest Risk Warning
    
    Link: https://www.thehealthy.com/news/flour-recall-october-2026/
  - (FDA recall health) [KOCO] 11/03/2026, 10:12 AM, +0000 UTC — FDA recalls thousands of blood pressure bottles, says pills failed quality tests
    
    Link: https://www.koco.com/article/fda-blood-pressure-medication-recall-pills-fail-test/74319583
  - (FDA recall health) [Prevention] 11/03/2026, 03:47 PM, +0000 UTC — FDA Announces 3,700-Bottle Recall of Popular Blood Pressure Medication
    
    Link: https://www.prevention.com/health/a74322378/macleods-pharmaceuticals-blood-pressure-medication-recall-fda/
  - (FDA recall health) [Health.com] 10/27/2026, 07:11 PM, +0000 UTC — FDA Announces Butter Recall in 10 States Due to Yeast, Mold, and E. Coli
    
    Link: https://www.health.com/butter-recall-october-2026-12196755
  - (FDA recall health) [Cardiovascular Business] 10/29/2026, 08:39 PM, +0000 UTC — FDA confirms Class I recall for certain Impella heart pump controllers
    
    Link: https://cardiovascularbusiness.com/topics/clinical/interventional-cardiology/fda-confirms-class-i-recall-certain-impella-heart-pump-controllers
  - (FDA recall health) [CASRAI] 11/01/2026, 05:43 PM, +0000 UTC — FDA Recall Coordinator: Who They Are, How to Find Yours and What to Send
    
    Link: https://casrai.org/guides/fda-recall-coordinator
  - (FDA recall health) [The New York Times] 10/31/2026, 03:43 PM, +0000 UTC — F.D.A. Warns of Snack Bar Linked to Toddler Choking Hazard
    
    Link: https://www.nytimes.com/2026/10/31/well/family/fda-tractor-wheels-choking-hazard.html
  - (FDA recall health) [Good Housekeeping] 10/29/2026, 05:07 PM, +0000 UTC — FDA Recall: Check Your Fridge for This Popular Salad Kit
    
    Link: https://www.goodhousekeeping.com/food-recipes/a74283451/h-e-b-salad-recall/
  - (FDA recall health) [USA Today] 11/03/2026, 01:56 PM, +0000 UTC — Blood pressure medication recalled nationwide. See the affected drug
    
    Link: https://www.usatoday.com/story/money/consumer-protection/recalls-alerts/2026/11/02/blood-pressure-medication-recalled/92563231007/
  - (FDA recall health) [New York Post] 10/28/2026, 03:51 PM, +0000 UTC — FDA recalls butter brand over potential illness caused by E.coli, mold and yeast
    
    Link: https://nypost.com/2026/10/28/lifestyle/fda-recalls-plant-based-miyoko-butter-due-to-e-coli-mold-and-yeast/
  - (FDA recall health) [Reader's Digest] 10/30/2026, 07:00 AM, +0000 UTC — FDA Raises Flour Recall to Its Highest Risk Level
    
    Link: https://www.rd.com/article/fda-raised-its-gluten-free-flour-recall-highest-level/