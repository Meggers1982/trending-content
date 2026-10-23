# LIVE SIGNAL DATA — SerpAPI Pre-Fetch
The following signals were fetched from SerpAPI Google News and SerpAPI Google Trends immediately before this pipeline run. Treat Google Trends as AVAILABLE when this section contains a Google Trends block. Use it as the primary search_velocity input for Skills 01–05 (Signal Listener through Trend Strength Scorer). Use the Google News Radar as the broad discovery layer for news-led health topics, including topics that do not yet appear in Google Trends. Prioritize topics with convergence across News, Trends, primary/institutional sources, and credible publisher coverage.

## Google Trends — Trending Now (US / Health, real-time)
Terms with a "Why:" line have a confirmed real-world news story driving the spike; terms without one are a real-time signal only, not yet grounded in a specific story.
  - marshall faulk
    Why: "Marshall Faulk, Hall of Famer and Southern coach, reveals Parkinson's diagnosis" — ESPN

## Google Trends — 7-Day Interest (US)
  - **health**: latest=84, peak=100, 7d-delta=+3
    Rising related: what did the new study find about daily tea drinking and heart health, tea heart health, womens health task force, billy joel health, trump health, health insurance, mental health, my health
  - **wellness**: latest=31, peak=100, 7d-delta=-3
    Rising related: bon secours wellness arena, bon secours wellness arena greenville sc, wellness center, health and wellness, wellness spa, wellness clinic, family wellness, wellness check
  - **nutrition**: latest=82, peak=100, 7d-delta=-9
    Rising related: abbott spin off nutrition business, nutrition sources nyt, abbott nutrition, bk nutrition, inspira nutrition, what is dark nutrition, dark nutrition, persimmon nutrition
  - **fitness**: latest=57, peak=100, 7d-delta=-5
    Rising related: planet fitness closing locations, wolf fitness owner, michael becktel, brown bear hunter encounter video, oura smart ring new fitness metrics, tea heart health, lego daft punk, wolf fitness mullica hill
  - **food safety**: latest=86, peak=100, 7d-delta=+8
    Rising related: food safety consortium, what does haccp stand for in food safety, best pizza near me, what is food safety, state food safety, food safety certification, food safety training, food safety plan
  - **diet**: latest=83, peak=100, 7d-delta=+0
    Rising related: dzne diet study biological aging, trisha yearwood diet and zumba, diet coke costume, diet coke, mediterranean diet, healthy diet, keto diet, science diet
  - **weight loss**: latest=51, peak=100, 7d-delta=-2
    Rising related: trisha yearwood weight loss, trisha yearwood, john goodman weight loss journey, trisha yearwood weight loss journey, trisha yearwood weight loss transformation, novo cagrisema weight loss results, glp-1 weight loss usage statistics, paula deen weight loss
  - **mental health**: latest=68, peak=100, 7d-delta=-5
    Rising related: teen mental health treatment malibu ca visionsteen.com, teen mental health treatment malibu ca visionsteen, amber glenn mental health, coinlaw.io, elizabeth holmes mental health, elizabeth holmes mental health diagnosis, north american mental health services, my bib
  - **gut health**: latest=61, peak=100, 7d-delta=+1
    Rising related: hack your health the secrets of your gut, best kombucha for gut health, gut health and mental health, probiotics for women, is kombucha good for gut health, what is gut health, gut health foods, probiotics

Top rising related queries from Google Trends:
  - what did the new study find about daily tea drinking and heart health
  - tea heart health
  - womens health task force
  - billy joel health
  - trump health
  - health insurance
  - mental health
  - my health
  - bon secours wellness arena
  - bon secours wellness arena greenville sc
  - wellness center
  - health and wellness
  - wellness spa
  - wellness clinic
  - family wellness
  - wellness check
  - abbott spin off nutrition business
  - nutrition sources nyt
  - abbott nutrition
  - bk nutrition

## Google News Radar — Recent Health Topics (144 unique across 12 queries; showing 60)
Treat these headlines as the broad radar of news-led health topics. The Signal Listener must consider this radar before narrowing to retained candidates.
  - (health) [KFF] 10/22/2026, 09:01 AM, +0000 UTC — 2026 Employer Health Benefits Survey
    
    Link: https://www.kff.org/health-costs/2026-employer-health-benefits-survey/
  - (health) [HHS.gov] 10/19/2026, 03:52 PM, +0000 UTC — President Trump Signs Historic Executive Order to Advance Women’s Health, Championed by First Lady Melania Trump
    
    Link: https://www.hhs.gov/press-room/trump-flotus-womens-health-executive-order-new-nih-division.html
  - (health) [Nature] 10/21/2026, 04:37 PM, +0000 UTC — The anatomy of a personal health agent
    
    Link: https://www.nature.com/articles/s41586-026-11161-8
  - (health) [Hackensack Meridian Health] 10/20/2026, 02:40 PM, +0000 UTC — Hackensack Meridian Health and Hunterdon Health Sign Definitive Agreement to Merge
    
    Link: https://www.hackensackmeridianhealth.org/en/news/2026/10/20/hackensack-meridian-health-and-hunterdon-health-sign-definitive-agreement-to-merge
  - (health) [NPR] 10/22/2026, 09:00 AM, +0000 UTC — High health costs squeeze workers, even if you have good insurance through a job
    
    Link: https://www.npr.org/2026/10/22/nx-s1-6008153/health-insurance-costs-kff-commonwealth
  - (health) [The New York Times] 10/22/2026, 09:03 AM, +0000 UTC — Employers Shift Rising Health Care Costs Onto Millions of Workers
    
    Link: https://www.nytimes.com/2026/10/22/business/health-insurance-costs-workers-premiums-deductibles.html
  - (health) [Commonwealth Fund] 10/22/2026, 12:00 PM, +0000 UTC — The State of Health Insurance Coverage in 2026
    
    Link: https://www.commonwealthfund.org/publications/surveys/2026/oct/state-health-insurance-coverage-2026-biennial-survey
  - (health) [PBS] 10/19/2026, 07:16 PM, +0000 UTC — WATCH: Trump and first lady unveil new task force on women's health research
    
    Link: https://www.pbs.org/newshour/politics/watch-trump-and-first-lady-unveil-new-task-force-on-womens-health-research
  - (health) [World Health Organization (WHO)] 10/19/2026, 07:00 AM, +0000 UTC — One in four doctors nearing retirement age as WHO warns of global health workforce gap
    
    Link: https://www.who.int/news/item/18-09-2026-one-in-four-doctors-nearing-retirement-age-as-who-warns-of-global-health-workforce-gap
  - (health) [Time Magazine] 10/22/2026, 09:00 AM, +0000 UTC — Health Care Costs Are Becoming Unsustainable
    
    Link: https://time.com/article/2026/10/22/us-health-care-costs-becoming-unsustainable/
  - (health) [MPR News] 10/21/2026, 08:33 PM, +0000 UTC — CentraCare healthcare system to acquire Stellis Health in merger of central Minnesota providers
    
    Link: https://www.mprnews.org/story/2026/10/21/centracare-healthcare-system-to-acquire-stellis-health
  - (health) [ABC7 Los Angeles] 10/19/2026, 04:45 PM, +0000 UTC — Donald Trump signs order aimed at boosting women's health research, a plan backed by First Lady Melania Trump
    
    Link: https://abc7.com/post/live-donald-trump-signs-order-aimed-boosting-womens-health-research-plan-backed-first-lady-melania/19955237/
  - (wellness) [CNN] 10/22/2026, 06:59 PM, +0000 UTC — ‘Wellness darties’: Inside Gen Z’s sober workout parties
    
    Link: https://www.cnn.com/2026/10/22/us/video/wellness-darties-college-students-find-new-way-to-party
  - (wellness) [WSJ] 10/19/2026, 05:21 PM, +0000 UTC — For Wellness Fans, Gummies Are Out. The New Craze Is Supplement Strips.
    
    Link: https://www.wsj.com/health/wellness/supplement-strips-stripit-sleep-or-die-0f69c8d7
  - (wellness) [WFSB] 10/17/2026, 10:57 AM, +0000 UTC — Officer fatally shoots person during overnight wellness check in Bristol, police say
    
    Link: https://www.wfsb.com/2026/10/17/bristol-officer-fatally-shoots-person-during-overnight-wellness-check-police-say/
  - (wellness) [DVIDS] 10/22/2026, 05:23 PM, +0000 UTC — News - Fort McCoy Wellness Fair draws strong participation in 2026
    
    Link: https://www.dvidshub.net/news/577622/fort-mccoy-wellness-fair-draws-strong-participation-2026
  - (wellness) [The Guardian] 10/19/2026, 11:05 AM, +0000 UTC — ‘Keep away from the doctor’: a visit to an influencer’s wellness event, where the advice could kill
    
    Link: https://www.theguardian.com/society/2026/oct/18/influencers-wellness-event-cheshire-barbara-oneill-australian
  - (wellness) [Marquette Today] 10/21/2026, 06:50 PM, +0000 UTC — Counting Sheep Challenge: Strive for quality sleep and earn My Wellness Points
    
    Link: https://today.marquette.edu/2026/10/counting-sheep-challenge-strive-for-quality-sleep-and-earn-my-wellness-points/
  - (wellness) [Purdue University] 10/21/2026, 09:00 AM, +0000 UTC — Free health and wellness coaching available for Greater Lafayette, Purdue community
    
    Link: https://www.purdue.edu/newsroom/purduetoday/2026/Q4/free-health-and-wellness-coaching-available-for-greater-lafayette-purdue-community
  - (wellness) [WUSA9] 10/22/2026, 03:12 AM, +0000 UTC — Therme DC wellness resort plan sparks debate on Ward 8 community impact and costs
    
    Link: https://www.wusa9.com/article/news/community/therme-dc-wellness-resort-plan-sparks-debate-ward-8-community-impact-and-costs/65-207322dd-1b30-4cff-9d07-81d6e8624f2f
  - (wellness) [State University of New York at Fredonia] 10/19/2026, 01:44 PM, +0000 UTC — University to host conference on mental wellness
    
    Link: https://www.fredonia.edu/news/articles/university-host-conference-mental-wellness
  - (wellness) [Georgia Tech News Center] 10/21/2026, 12:00 PM, +0000 UTC — Generating Buzz: A Culture of Wellness at Georgia Tech
    
    Link: https://news.gatech.edu/features/2026/10/generating-buzz-culture-wellness-georgia-tech
  - (wellness) [Case Western Reserve University] 10/22/2026, 02:47 PM, +0000 UTC — Learn what to expect at the 2026 Benefits & Wellness Fair
    
    Link: https://case.edu/news/learn-what-expect-2026-benefits-wellness-fair
  - (wellness) [Glossy] 10/21/2026, 09:18 AM, +0000 UTC — Wellness consumers are overwhelmed. Is a subscription box the answer?
    
    Link: https://www.glossy.co/beauty/wellness/wellness-consumers-are-overwhelmed-is-a-subscription-box-the-answer/
  - (medical study) [Stanford Medicine] 10/21/2026, 06:06 PM, +0000 UTC — ‘Digital twins’ of immune system in pregnancy identify drugs to prevent early labor, Stanford Medicine-led study finds
    
    Link: https://med.stanford.edu/news/all-news/2026/10/preterm-labor-drug.html
  - (medical study) [New Jersey Monitor] 10/21/2026, 11:01 AM, +0000 UTC — Insured patients struggle to schedule mental healthcare, study shows
    
    Link: https://newjerseymonitor.com/2026/10/21/insured-patients-struggle-to-schedule-mental-healthcare-study-shows/
  - (medical study) [Nature] 10/21/2026, 10:33 AM, +0000 UTC — Global, regional and national burden of pertussis in 1990–2023: a Global Burden of Disease study
    
    Link: https://www.nature.com/articles/s41591-026-04660-8
  - (medical study) [WCAX] 10/17/2026, 01:09 PM, +0000 UTC — New center unveiled to study sleep disorders at Rutland Regional Medical Center
    
    Link: https://www.wcax.com/2026/10/17/new-center-unveiled-study-sleep-disorders-rutland-regional-medical-center/
  - (medical study) [News-Medical] 10/22/2026, 07:45 PM, +0000 UTC — Study defines average human genome and normal genetic disease risk
    
    Link: https://www.news-medical.net/news/20261022/Study-defines-average-human-genome-and-normal-genetic-disease-risk.aspx
  - (medical study) [Psychiatric Times] 10/20/2026, 01:27 PM, +0000 UTC — Phase 2 Clinical Study Initiated: Evaluating NBI-'567 for the Treatment of Adults With Alzheimer Disease
    
    Link: https://www.psychiatrictimes.com/view/phase-2-clinical-study-initiated-evaluating-nbi--567-for-the-treatment-of-adults-with-alzheimer-disease
  - (medical study) [National Institutes of Health (NIH) | (.gov)] 10/19/2026, 10:30 PM, +0000 UTC — Statement from NIH Director Jay Bhattacharya and NIAID Acting Director John H. Powers III on the New NIH Vaccinology and Immunology Center
    
    Link: https://www.nih.gov/about-nih/nih-director/statements/statement-nih-director-jay-bhattacharya-niaid-acting-director-john-h-powers-iii-new-nih-vaccinology-immunology-center
  - (medical study) [Medical Xpress] 10/21/2026, 03:20 PM, +0000 UTC — CAR T-cell therapy shows lasting improvements in stiff person syndrome, study finds
    
    Link: https://medicalxpress.com/news/2026-10-car-cell-therapy-stiff-person.html
  - (medical study) [The Clinical Trial Vanguard] 10/21/2026, 06:50 AM, +0000 UTC — FDA AI Guidance Requires Sponsors to Validate Clinical Trial Algorithms
    
    Link: https://www.clinicaltrialvanguard.com/news/fda-ai-guidance-requires-sponsors-to-validate-clinical-trial-algorithms/
  - (medical study) [Medical Economics] 10/22/2026, 08:26 PM, +0000 UTC — AI system outperforms physicians on diagnostic accuracy in Microsoft study
    
    Link: https://www.medicaleconomics.com/view/ai-system-outperforms-physicians-on-diagnostic-accuracy-in-microsoft-study
  - (medical study) [Stanford HAI] 10/20/2026, 12:11 AM, +0000 UTC — Measuring What Medical AI Can Actually Do
    
    Link: https://hai.stanford.edu/news/measuring-what-medical-ai-can-actually-do
  - (medical study) [Nature] 10/17/2026, 10:18 AM, +0000 UTC — A scoping review of bias in large AI models for medicine and healthcare
    
    Link: https://www.nature.com/articles/s44528-026-00041-2
  - (clinical trial health) [Applied Clinical Trials] 10/20/2026, 04:03 PM, +0000 UTC — Syneos Health, Optum Partner on Adaptive Clinical Development Model
    
    Link: https://www.appliedclinicaltrialsonline.com/view/syneos-health-optum-adaptive-clinical-development-model-partnership
  - (clinical trial health) [Healthcare IT News] 10/21/2026, 01:40 PM, +0000 UTC — Oracle and AstraZeneca to collaborate on 'smarter' clinical trials
    
    Link: https://www.healthcareitnews.com/news/oracle-and-astrazeneca-collaborate-smarter-clinical-trials
  - (clinical trial health) [Reuters] 10/20/2026, 04:10 PM, +0000 UTC — AstraZeneca partners with Oracle for AI-driven clinical trials
    
    Link: https://www.reuters.com/legal/litigation/astrazeneca-partners-with-oracle-ai-driven-clinical-trials-2026-10-20/
  - (clinical trial health) [Morgan Griffith (.gov)] 10/22/2026, 08:17 PM, +0000 UTC — Chairman Griffith Helps Lead Effort to Revamp Rural Patient Access to Clinical Trials, Accelerate New Treatments to Market
    
    Link: https://morgangriffith.house.gov/news/documentsingle.aspx?DocumentID=405855
  - (clinical trial health) [News-Medical] 10/19/2026, 04:32 PM, +0000 UTC — First patient dosed in Phase 1 clinical trial of new cancer drug
    
    Link: https://www.news-medical.net/news/20261019/First-patient-dosed-in-Phase-1-clinical-trial-of-new-cancer-drug.aspx
  - (clinical trial health) [The Clinical Trial Vanguard] 10/19/2026, 06:40 AM, +0000 UTC — Wearable Devices Face Accuracy Gaps in Clinical Trial Endpoints
    
    Link: https://www.clinicaltrialvanguard.com/news/wearable-devices-face-accuracy-gaps-in-clinical-trial-endpoints/
  - (clinical trial health) [Oncodaily] 10/18/2026, 09:57 PM, +0000 UTC — Ruiling Yuan: Building Trust and Health Literacy to Expand Clinical Trial Participation
    
    Link: https://oncodaily.com/community/ruiling-yuan-611800
  - (clinical trial health) [pharmaphorum] 10/22/2026, 10:06 AM, +0000 UTC — Clinical trial setup times fall sharply in UK
    
    Link: https://pharmaphorum.com/news/clinical-trial-setup-times-fall-sharply-uk
  - (clinical trial health) [Clinical Trials Arena] 10/21/2026, 09:46 AM, +0000 UTC — AstraZeneca and Oracle collaborate to test AI in clinical trial recruitment
    
    Link: https://www.clinicaltrialsarena.com/news/astrazeneca-oracle-test-ai-clinical-trial/
  - (clinical trial health) [UC San Diego Today] 10/21/2026, 05:09 PM, +0000 UTC — UC San Diego Joins ARPA-H-Funded Initiative to Launch Drug-Testing Platform for Alzheimer’s Disease
    
    Link: https://today.ucsd.edu/story/uc-san-diego-joins-arpa-h-funded-initiative-to-launch-drug-testing-platform-for-alzheimers-disease
  - (clinical trial health) [Medscape] 10/21/2026, 08:57 AM, +0000 UTC — Med Op-Ed: Time Toxicity, Clinical Trial Access, and RECIST
    
    Link: https://www.medscape.com/viewarticle/med-op-ed-time-toxicity-clinical-trial-access-and-recist-2026a10013hh
  - (clinical trial health) [Science Daily] 10/23/2026, 11:04 AM, +0000 UTC — Breakthrough PTSD treatment achieves 68% remission rate in clinical trial
    
    Link: https://www.sciencedaily.com/releases/2026/10/261022081309.htm
  - (FDA recall health) [Health.com] 10/21/2026, 06:29 PM, +0000 UTC — FDA Announces Nationwide Recall of More Than 4 Million Tubes of Toothpaste
    
    Link: https://www.health.com/toothpaste-recall-october-2026-12186381
  - (FDA recall health) [Good Housekeeping] 10/21/2026, 02:53 PM, +0000 UTC — FDA Announces Nationwide Recall of GLP-1 Medications–Here's the Full List of Products
    
    Link: https://www.goodhousekeeping.com/health/a74204439/glp-1-recall-tirzepatide-injections/
  - (FDA recall health) [KCRA] 10/20/2026, 08:48 PM, +0000 UTC — FDA recalls 4.3 million tubes of adult and children's toothpaste
    
    Link: https://www.kcra.com/article/fda-brush-budies-toothpaste-recall-nationwide/74195828
  - (FDA recall health) [FOX 5 New York] 10/21/2026, 03:58 PM, +0000 UTC — What to know about GLP-1s and cannabis use
    
    Link: https://www.fox5ny.com/news/fda-recalls-glp-1-drug-sterility-concerns
  - (FDA recall health) [Fox Business] 10/20/2026, 08:57 PM, +0000 UTC — GLP-1 injections recalled nationwide over sterility concerns
    
    Link: https://www.foxbusiness.com/healthcare/glp-1-injections-recalled-nationwide-over-sterility-concerns
  - (FDA recall health) [USA Today] 10/22/2026, 08:05 PM, +0000 UTC — Over 4 million tubes of toothpaste recalled. See affected products
    
    Link: https://www.usatoday.com/story/money/consumer-protection/recalls-alerts/2026/10/21/toothpaste-recall-brush-buddies-evo/92344819007/
  - (FDA recall health) [The Healthy] 10/20/2026, 07:00 AM, +0000 UTC — Toothpaste Recall: Over 4 Million Tubes Recalled Nationwide
    
    Link: https://www.thehealthy.com/news/toothpaste-recall-october-2026/
  - (FDA recall health) [Prevention] 10/22/2026, 06:23 PM, +0000 UTC — More Than 4 Million Tubes of Toothpaste Recalled Nationwide, FDA Warns
    
    Link: https://www.prevention.com/health/a74220169/toothpaste-recall-fda/
  - (FDA recall health) [Newsweek] 10/20/2026, 02:57 PM, +0000 UTC — Cheese Recall Update In 13 States As FDA Issues Highest Risk Warning
    
    Link: https://www.newsweek.com/cheese-recall-states-highest-warning-issued-e-coli-12592463
  - (FDA recall health) [kare11.com] 10/21/2026, 06:26 PM, +0000 UTC — Toothpaste recall for more than 4 million tubes includes ones for kids
    
    Link: https://www.kare11.com/article/news/nation-world/toothpaste-recall-list-brush-buddies-evo-aru/507-eba20cac-f7d6-45d5-af44-49f612d9d3b9
  - (FDA recall health) [MedShadow Foundation] 10/21/2026, 04:27 PM, +0000 UTC — FDA Recalls and Warnings: Epilepsy Drug Mix-Up, Subpotent Thyroid Medication, and More
    
    Link: https://medshadow.org/drug-updates-recalls/fda-recalls-and-warnings/levoxyl-amlodipine-olmesartan/
  - (FDA recall health) [News12 | Long Island] 10/23/2026, 11:58 AM, +0000 UTC — Fda Recalls More Than 4 Million Tubes Of Toothpaste
    
    Link: https://longisland.news12.com/fda-recalls-more-than-4-million-tubes-of-toothpaste