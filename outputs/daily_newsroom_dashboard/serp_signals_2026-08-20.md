# LIVE SIGNAL DATA — SerpAPI Pre-Fetch
The following signals were fetched from SerpAPI Google News and SerpAPI Google Trends immediately before this pipeline run. Treat Google Trends as AVAILABLE when this section contains a Google Trends block. Use it as the primary search_velocity input for Skills 01–05 (Signal Listener through Trend Strength Scorer). Use the Google News Radar as the broad discovery layer for news-led health topics, including topics that do not yet appear in Google Trends. Prioritize topics with convergence across News, Trends, primary/institutional sources, and credible publisher coverage.

## Google Trends — Trending Now (US / Health, real-time)
Terms with a "Why:" line have a confirmed real-world news story driving the spike; terms without one are a real-time signal only, not yet grounded in a specific story.
  - healthy food
    Why: "Experts Recommend These Foods for Brain Health" — Prevention

## Google Trends — 7-Day Interest (US)
  - **health**: latest=80, peak=100, 7d-delta=-3
    Rising related: mitch mcconnell health, mental health, health insurance, my health, health department, behavioral health, university health, united health
  - **wellness**: latest=83, peak=100, 7d-delta=+1
    Rising related: circle wellness seattle, koniver wellness, social health definition, barker wellness, health definition, routine wellness shampoo and conditioner reviews, the wellness company medical emergency kit, kroger wellness festival 2026
  - **nutrition**: latest=100, peak=100, 7d-delta=+11
    Rising related: supplemental nutrition assistance program, nutrition facts, nutrition calculator, egg nutrition, optimum nutrition, chipotle nutrition, chick fil a nutrition, apple nutrition
  - **fitness**: latest=50, peak=100, 7d-delta=-3
    Rising related: eric falstrault fitness transformation, casio f-b100w fitness tracker, how to cancel planet fitness membership online, planet fitness customer service number, planet fitness customer service, cancel my planet fitness membership, how to cancel my planet fitness membership, group fitness classes
  - **food safety**: latest=38, peak=100, 7d-delta=-2
    Rising related: who should you call first whenever you are in doubt about the immediate health and safety of a child?, blueberry recall, home workout routines, 2026 food safety recall trends, no food or drink sign, california food safety act, bitcoin price august 20 2026, childcare programs are permitted to use 15 passenger vans to transport children.
  - **diet**: latest=82, peak=100, 7d-delta=+0
    Rising related: physicians committee vegan diet study, vegan diet and inflammation, plant-based diet, gluten-free diet, what is the difference between diet coke and coke zero, miranda kerr diet, mind diet, diet coke
  - **weight loss**: latest=60, peak=100, 7d-delta=+2
    Rising related: best glp 1 supplement for weight loss, margaret cho weight loss, bridget fonda weight loss, bronson reed weight loss, nicole byer weight loss, shop lc clearance blowout, erin burnett weight loss, jenna ortega before and after weight loss
  - **mental health**: latest=88, peak=100, 7d-delta=+13
    Rising related: hayden panettiere mental health, hayden panettiere mental health issues, did hayden panettiere have mental health issues, selena gomez mental health company, selena gomez mental health, mychal threets mental health, northern virginia mental health institute, adolescent inpatient mental health facilities near me
  - **gut health**: latest=34, peak=100, 7d-delta=-1
    Rising related: bristol stool chart usage, research on family estrangement, is apple cider vinegar good for gut health, holistic gut health doctor near me, hack your health the secrets of your gut, gut health doctor near me, is sourdough good for gut health, coconut cult

Top rising related queries from Google Trends:
  - mitch mcconnell health
  - mental health
  - health insurance
  - my health
  - health department
  - behavioral health
  - university health
  - united health
  - circle wellness seattle
  - koniver wellness
  - social health definition
  - barker wellness
  - health definition
  - routine wellness shampoo and conditioner reviews
  - the wellness company medical emergency kit
  - kroger wellness festival 2026
  - supplemental nutrition assistance program
  - nutrition facts
  - nutrition calculator
  - egg nutrition

## Google News Radar — Recent Health Topics (144 unique across 12 queries; showing 60)
Treat these headlines as the broad radar of news-led health topics. The Signal Listener must consider this radar before narrowing to retained candidates.
  - (health) [HHS.gov] 08/13/2026, 07:00 PM, +0000 UTC — HHS Announces Historic Investment to Expand Health Center Program, Bringing Primary Care to Nearly 1 Million More Americans
    
  - (health) [Axios] 08/16/2026, 10:00 AM, +0000 UTC — How AI could bring Mayo-quality health care to everyone
    
  - (health) [MPR News] 08/15/2026, 12:00 PM, +0000 UTC — Health insurance rates expected to climb again for Minnesotans in 2027
    
  - (health) [VTDigger] 08/17/2026, 03:18 PM, +0000 UTC — Dartmouth Health says it needs to close telehealth services for emergency and intensive care
    
  - (health) [University of Arizona News] 08/19/2026, 02:56 AM, +0000 UTC — U of A and Gila River Health Care (an entity of the Gila River Indian Community) launch nation's first MD-granting medical school branch within a Tribal Nation
    
  - (health) [The New York Times] 08/19/2026, 10:55 PM, +0000 UTC — Senate Health Panel Chairman Voices Strong Reservations About F.D.A. Nominee
    
  - (health) [CNBC] 08/16/2026, 07:58 PM, +0000 UTC — Top U.S. commander acknowledges mental health issues on USS Lincoln
    
  - (health) [UN News] 08/14/2026, 04:41 PM, +0000 UTC — An attack on healthcare every six hours, and no one held to account
    
  - (health) [health.com] 08/18/2026, 02:12 PM, +0000 UTC — 6 Signs Your Gut Health Is Out of Balance
    
  - (health) [Healthcare Dive] 08/19/2026, 04:42 PM, +0000 UTC — Providence Health Plan to close completely after Medicare Advantage deal falls through
    
  - (health) [NPR] 08/18/2026, 07:03 PM, +0000 UTC — In Good Health: Finding A Primary Care Physician : 1A
    
  - (health) [STAT] 08/18/2026, 08:34 AM, +0000 UTC — How health care costs are undermining America’s public-sector employers
    
  - (wellness) [Colorado College] 08/17/2026, 04:35 AM, +0000 UTC — Wellness Is Everyone’s Business
    
  - (wellness) [University of Nebraska Medical Center] 08/18/2026, 09:33 AM, +0000 UTC — Registration open for women’s health and wellness conference
    
  - (wellness) [The Capitol Forum] 08/14/2026, 07:00 AM, +0000 UTC — FDA Weighs Compounding Approval for Wellness Peptides
    
  - (wellness) [Virginia Department of Corrections (.gov)] 08/17/2026, 04:03 PM, +0000 UTC — VADOC Celebrates Employee Health & Wellness Week
    
  - (wellness) [UNM Newsroom] 08/18/2026, 10:12 PM, +0000 UTC — COEHS wellness services strengthen communities, prepare future professionals
    
  - (wellness) [Marquette Today] 08/20/2026, 03:06 PM, +0000 UTC — Review your benefits with the Total Rewards Guide and Benefits and Wellness website
    
  - (wellness) [UR Now] 08/18/2026, 08:29 PM, +0000 UTC — University of Richmond alum’s wellness app provides a check-in for athletes
    
  - (wellness) [MLB.com] 08/19/2026, 07:41 PM, +0000 UTC — MLB Together teaches mental wellness at RBI World Series
    
  - (wellness) [PR Newswire] 08/14/2026, 03:00 PM, +0000 UTC — FERRERO GROUP TO ACQUIRE PURELY ELIZABETH, A LEADING U.S. MODERN WELLNESS BRAND
    
  - (wellness) [Purdue University] 08/17/2026, 09:07 AM, +0000 UTC — Save the date: 2026 Your Path Wellness Fair coming Oct. 7
    
  - (wellness) [BYU Life Sciences] 08/18/2026, 02:00 PM, +0000 UTC — The Arroyo Lab: Bridging Metabolic Research and Maternal Wellness
    
  - (wellness) [The Santa Barbara Independent] 08/19/2026, 08:10 PM, +0000 UTC — County Behavioral Wellness Accepting Annual Applications for John Kovacs Scholarship Awards
    
  - (medical study) [University of Nebraska Medical Center] 08/18/2026, 07:31 PM, +0000 UTC — Medical research highlights, summer 2026
    
  - (medical study) [Harvard Medical School] 08/17/2026, 04:05 PM, +0000 UTC — Pilots, Flight Attendants Have Greater Risk of Radiation-Related Cancer Death Than Other Professions
    
  - (medical study) [NPR] 08/19/2026, 03:22 PM, +0000 UTC — A real-world study of Oregon's nonmedical psilocybin program shows promise
    
  - (medical study) [Michigan Medicine] 08/19/2026, 12:00 PM, +0000 UTC — College of Pharmacy alum advances U-M Medical School addiction research
    
  - (medical study) [American Cancer Society Press Room] 08/18/2026, 02:02 PM, +0000 UTC — County-Level Medical Debt Linked to Advanced-Stage Cancers and Worse Survival Among Newly Diagnosed U.S. Adults
    
  - (medical study) [RAPS] 08/18/2026, 12:00 PM, +0000 UTC — Study highlights limits of premarket evaluation for identifying recalls of high-risk medical devices
    
  - (medical study) [Stanford Medicine] 08/19/2026, 09:51 PM, +0000 UTC — ‘Molecular glue’ turns a cancer driver into a built-in kill switch in Stanford Medicine study
    
  - (medical study) [WSJ] 08/19/2026, 09:30 AM, +0000 UTC — Exclusive | Startup to Link ‘Biobanks’ of Patient Tissue to Supercharge AI Medical Research
    
  - (medical study) [Nature] 08/19/2026, 10:08 AM, +0000 UTC — Genomic meta-analyses of binge-eating behavior and anorexia nervosa yield insights into the unique and shared biology of eating disorder phenotypes
    
  - (medical study) [University of South Florida] 08/19/2026, 02:35 PM, +0000 UTC — USF Health research reveals new clues about how space travel may affect women’s health
    
  - (medical study) [Spectrum News] 08/14/2026, 12:30 PM, +0000 UTC — Legislative committee studying use of AI in healthcare
    
  - (medical study) [WashU Medicine] 08/17/2026, 08:03 PM, +0000 UTC — Laser therapy offers weapon against deadly brain tumors
    
  - (clinical trial health) [KFF Health News] 08/19/2026, 09:02 AM, +0000 UTC — You Want To Join a Clinical Trial. Here’s What To Know About the Hurdles.
    
  - (clinical trial health) [Mass General Brigham] 08/18/2026, 07:00 AM, +0000 UTC — Mass General Brigham Launches Clinical Trials Focused on Home Hospital Treatment for Dementia and Behavioral Health Conditions
    
  - (clinical trial health) [HCI Innovation Group] 08/14/2026, 08:56 AM, +0000 UTC — Ochsner, Paradigm Health Partner to Expand Clinical Trial Access
    
  - (clinical trial health) [The Clinical Trial Vanguard] 08/19/2026, 07:32 AM, +0000 UTC — When Your CRO Gets Acquired Mid-Study, Your Site Feels It First
    
  - (clinical trial health) [The New York Times] 08/18/2026, 07:00 AM, +0000 UTC — A Hopeless Diagnosis? Not for This Patient.
    
  - (clinical trial health) [Applied Clinical Trials Online] 08/18/2026, 03:48 PM, +0000 UTC — Syneos Health Expands AI Ecosystem With Three New Platform Partnerships
    
  - (clinical trial health) [PR Newswire] 08/18/2026, 10:19 PM, +0000 UTC — Curavit Expands Clinical Research Capabilities with Acquisition of Lindus Health CRO Assets, Accelerating Global Trial Execution for Life Science Sponsors
    
  - (clinical trial health) [South Carolina Daily Gazette] 08/19/2026, 04:18 PM, +0000 UTC — State-funded testing of COVID-19 treatment approved to start 3,000-person clinical trial
    
  - (clinical trial health) [American Hospital Association] 08/15/2026, 07:53 PM, +0000 UTC — West Virginia University Health System's clinical trial offers hope for a rare and deadly blood cancer
    
  - (clinical trial health) [Oncodaily] 08/17/2026, 05:07 PM, +0000 UTC — Accelerating Clinical Trial Approvals Across Africa – Global Health Otherwise
    
  - (clinical trial health) [Spectrum News] 08/19/2026, 03:52 PM, +0000 UTC — Personalized cancer vaccine shows promise in late-stage clinical trial
    
  - (clinical trial health) [Vanderbilt Health News] 08/18/2026, 03:00 PM, +0000 UTC — Could GLP-1s help treat opioid use disorder? Vanderbilt Health study now enrolling
    
  - (FDA recall health) [fda.gov] 08/17/2026, 09:55 PM, +0000 UTC — UPDATED: Oma's Pride Voluntarily Recalls One Lot of Woof Complete Canine Chicken Recipe (6 Lb Bag) Because of Possible Salmonella Health Risk
    
  - (FDA recall health) [The New York Times] 08/14/2026, 11:12 PM, +0000 UTC — F.D.A. Classifies Egg Recall as Class I, for Highest Health Risk
    
  - (FDA recall health) [CBS News] 08/14/2026, 07:57 PM, +0000 UTC — FDA upgrades egg recall linked to salmonella to highest health risk level
    
  - (FDA recall health) [CIDRAP] 08/17/2026, 08:27 PM, +0000 UTC — FDA heightens egg recall to reflect potential ‘serious adverse health consequences or death’
    
  - (FDA recall health) [El Paso Times] 08/15/2026, 02:51 PM, +0000 UTC — FDA upgrades egg recall to Class I. What it means
    
  - (FDA recall health) [Time Magazine] 08/15/2026, 03:47 PM, +0000 UTC — Salmonella Egg Recall Is Now Class I, the FDA’s Highest Risk Level
    
  - (FDA recall health) [The Hill] 08/14/2026, 02:54 PM, +0000 UTC — FDA assigns highest-risk Class I status for recall of nearly 1.6 million cartons of eggs
    
  - (FDA recall health) [Denver7] 08/18/2026, 12:25 AM, +0000 UTC — FDA upgrades egg recall to highest health-risk level amid string of food safety concerns
    
  - (FDA recall health) [Ophthalmology Times Europe] 08/20/2026, 11:01 AM, +0000 UTC — FDA recalls eye drop that relieves ocular itch for potential contamination
    
  - (FDA recall health) [New York Post] 08/13/2026, 07:17 PM, +0000 UTC — Egg recall upgraded to FDA’s highest risk level: ‘Serious adverse health consequences or death’
    
  - (FDA recall health) [The Guardian] 08/15/2026, 09:25 PM, +0000 UTC — Massive egg recall in US south and south-west due to salmonella outbreak
    
  - (FDA recall health) [11Alive.com] 08/20/2026, 02:42 PM, +0000 UTC — Blueberry recall in 8 states upgraded to FDA's highest health risk level
    