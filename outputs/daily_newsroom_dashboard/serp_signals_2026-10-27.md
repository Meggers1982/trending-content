# LIVE SIGNAL DATA — SerpAPI Pre-Fetch
The following signals were fetched from SerpAPI Google News and SerpAPI Google Trends immediately before this pipeline run. Treat Google Trends as AVAILABLE when this section contains a Google Trends block. Use it as the primary search_velocity input for Skills 01–05 (Signal Listener through Trend Strength Scorer). Use the Google News Radar as the broad discovery layer for news-led health topics, including topics that do not yet appear in Google Trends. Prioritize topics with convergence across News, Trends, primary/institutional sources, and credible publisher coverage.

## Google Trends — Trending Now (US / Health, real-time)
Terms with a "Why:" line have a confirmed real-world news story driving the spike; terms without one are a real-time signal only, not yet grounded in a specific story.
  - missouri attorney general
    Why: "Mo. Attorney General sends prescription manufacturer Eli Lilly cease-and-desist over drug price policy" — KMOV
  - ebola
    Why: "Congo’s Ebola outbreak tops 10,000 cases as authorities race to slow the spread in African countries" — NBC News
  - jennifer shuford
    Why: "Trump-Appointed CDC Deputy Director Jennifer Shuford Resigns After 4 Months" — The New York Times

## Google Trends — 7-Day Interest (US)
  - **health**: latest=98, peak=100, 7d-delta=+2
    Rising related: what did the new study find about daily tea drinking and heart health, tea heart health, risant health, womens health task force, health ledger, health care fraud, health care, health insurance
  - **wellness**: latest=35, peak=100, 7d-delta=-4
    Rising related: total thai wellness, viral tiktok trends, aura points / aura slang, kitchen tech upgrades, non-toxic air fryer, trending beauty hacks, digital side hustles, minimalist lifestyle trend
  - **nutrition**: latest=95, peak=100, 7d-delta=-4
    Rising related: nutrition sources nyt, abbott spin off nutrition business, beller nutrition, abbott nutrition news, sp nutrition magnesium bisglycinate gummies review, abbott nutrition, supplemental nutrition assistance program, what is dark nutrition
  - **fitness**: latest=58, peak=100, 7d-delta=-2
    Rising related: planet fitness closing locations, la fitness shutting down gyms, fitbit edge alternative fitness trackers, james webb space telescope, brown bear hunter encounter video, planet fitness locations, tea heart health, salam fitness and aquatics
  - **food safety**: latest=68, peak=100, 7d-delta=+0
    Rising related: aluminum foil leftover food safety, mailing paper checks safety risks, all of the following bacteria can cause foodborne illness except, the food and drug administration sets standards for advertising. product labeling. the environment. traffic safety., according to the video, how was the banking act of 1933 a reaction to the great depression?, food should be stored at least which distance from the floor, icev, eating undercooked chicken can cause
  - **diet**: latest=96, peak=100, 7d-delta=-2
    Rising related: humanin shmoose mediterranean diet study, dzne diet study biological aging, trisha yearwood diet and zumba, diet coke advent calendar, diet coke, mediterranean, mediterranean diet, healthy diet
  - **weight loss**: latest=57, peak=100, 7d-delta=-8
    Rising related: trisha yearwood, trisha yearwood weight loss, john goodman weight loss journey, trisha yearwood weight loss journey, glp-1 weight loss usage statistics, eli lilly weight loss ads ruling, trisha yearwood weight loss transformation, menopause glp 1 weight loss studies
  - **mental health**: latest=84, peak=100, 7d-delta=-11
    Rising related: mental health women villakalima, teen mental health treatment malibu ca visionsteen.com, mental health women villakalima.com, teen mental health treatment malibu ca visionsteen, amber glenn mental health, paul hilse reddit, my bib, north american mental health services
  - **gut health**: latest=54, peak=100, 7d-delta=-2
    Rising related: vitamin shoppe, hack your health the secrets of your gut, how to restore gut health after antibiotics, leaky gut syndrome, ion gut health, aloe vera juice for gut health, how to take apple cider vinegar for gut health, tempeh

Top rising related queries from Google Trends:
  - what did the new study find about daily tea drinking and heart health
  - tea heart health
  - risant health
  - womens health task force
  - health ledger
  - health care fraud
  - health care
  - health insurance
  - total thai wellness
  - viral tiktok trends
  - aura points / aura slang
  - kitchen tech upgrades
  - non-toxic air fryer
  - trending beauty hacks
  - digital side hustles
  - minimalist lifestyle trend
  - nutrition sources nyt
  - abbott spin off nutrition business
  - beller nutrition
  - abbott nutrition news

## Google News Radar — Recent Health Topics (144 unique across 12 queries; showing 60)
Treat these headlines as the broad radar of news-led health topics. The Signal Listener must consider this radar before narrowing to retained candidates.
  - (health) [Centers for Disease Control and Prevention | CDC (.gov)] 10/23/2026, 07:00 AM, +0000 UTC — One Health Day Communications Toolkit
    
    Link: https://www.cdc.gov/one-health/php/trainings-events/one-health-day.html
  - (health) [KFF] 10/23/2026, 07:00 AM, +0000 UTC — Americans’ Challenges with Health Care Costs
    
    Link: https://www.kff.org/health-costs/americans-challenges-with-health-care-costs/
  - (health) [Nature] 10/21/2026, 04:37 PM, +0000 UTC — The anatomy of a personal health agent
    
    Link: https://www.nature.com/articles/s41586-026-11161-8
  - (health) [Commonwealth Fund] 10/22/2026, 12:00 PM, +0000 UTC — The State of Health Insurance Coverage in 2026
    
    Link: https://www.commonwealthfund.org/publications/surveys/2026/oct/state-health-insurance-coverage-2026-biennial-survey
  - (health) [HHS.gov] 10/26/2026, 03:30 PM, +0000 UTC — HHS Finalizes HTI-5 Deregulatory Rule to Encourage Innovation and Reduce Health IT Certification Program Compliance Costs
    
    Link: https://www.hhs.gov/press-room/hhs-finalizes-hti-5-deregulatory-rule.html
  - (health) [USDA (.gov)] 10/23/2026, 07:00 AM, +0000 UTC — Screwworm.gov | Animal and Plant Health Inspection Service
    
    Link: https://www.aphis.usda.gov/animals/animal-health/livestock-and-poultry-disease/stop-screwworm
  - (health) [The New York Times] 10/22/2026, 09:03 AM, +0000 UTC — Employers Shift Rising Health Care Costs Onto Millions of Workers
    
    Link: https://www.nytimes.com/2026/10/22/business/health-insurance-costs-workers-premiums-deductibles.html
  - (health) [World Health Organization (WHO)] 10/21/2026, 07:00 AM, +0000 UTC — Burns
    
    Link: https://www.who.int/news-room/fact-sheets/detail/burns
  - (health) [NPR] 10/22/2026, 09:00 AM, +0000 UTC — High health costs squeeze workers, even if you have good insurance through a job
    
    Link: https://www.npr.org/2026/10/22/nx-s1-6008153/health-insurance-costs-kff-commonwealth
  - (health) [UNM HSC Newsroom] 10/27/2026, 04:35 AM, +0000 UTC — Update on Cybersecurity Event at UNM Health Sciences Center
    
    Link: https://hscnews.unm.edu/news/ambulance-traffic-diverted-clinical-appointments-cancelled-and-classes-cancelled-due-to-cybersecurity-issue-at-unm-hsc
  - (health) [Peterson-KFF Health System Tracker] 10/22/2026, 07:00 AM, +0000 UTC — How much is health spending expected to grow?
    
    Link: https://www.healthsystemtracker.org/chart-collection/how-much-is-health-spending-expected-to-grow/
  - (health) [U.S. Food and Drug Administration (.gov)] 10/22/2026, 12:00 AM, +0000 UTC — FDA Food Code
    
    Link: https://www.fda.gov/food/retail-food-protection/fda-food-code
  - (wellness) [CNN] 10/22/2026, 06:59 PM, +0000 UTC — ‘Wellness darties’: Inside Gen Z’s sober workout parties
    
    Link: https://www.cnn.com/2026/10/22/us/video/wellness-darties-college-students-find-new-way-to-party
  - (wellness) [Breast Cancer Research Foundation | BCRF] 10/20/2026, 06:00 PM, +0000 UTC — 5 Health and Wellness Gifts That Help Fund Breast Cancer Research
    
    Link: https://www.bcrf.org/blog/health-wellness-gifts-breast-cancer-research/
  - (wellness) [The New York Times] 10/22/2026, 07:00 AM, +0000 UTC — While Advising Kennedy, Top Aide Had More Than $25 Million Stake in Wellness Company
    
    Link: https://www.nytimes.com/2026/04/24/health/calley-means-truemed-trump-health-savings.html
  - (wellness) [NBC 5 Dallas-Fort Worth] 10/23/2026, 08:51 PM, +0000 UTC — Iconic Dallas Granada Theater sells to New York based wellness brand
    
    Link: https://www.nbcdfw.com/news/local/historic-granada-theater-sells-to-new-york-based-wellness-brand/4095056/
  - (wellness) [The Santa Barbara Independent] 10/23/2026, 08:19 PM, +0000 UTC — San Marcos High School Breaks Ground on Building Community Wellness Project
    
    Link: https://www.independent.com/2026/10/23/san-marcos-high-school-breaks-ground-on-building-community-wellness-project/
  - (wellness) [Purdue University] 10/21/2026, 09:00 AM, +0000 UTC — Free health and wellness coaching available for Greater Lafayette, Purdue community
    
    Link: https://www.purdue.edu/newsroom/purduetoday/2026/Q4/free-health-and-wellness-coaching-available-for-greater-lafayette-purdue-community
  - (wellness) [DVIDS] 10/22/2026, 05:23 PM, +0000 UTC — News - Fort McCoy Wellness Fair draws strong participation in 2026
    
    Link: https://www.dvidshub.net/news/577622/fort-mccoy-wellness-fair-draws-strong-participation-2026
  - (wellness) [Case Western Reserve University] 10/22/2026, 02:47 PM, +0000 UTC — Learn what to expect at the 2026 Benefits & Wellness Fair
    
    Link: https://case.edu/news/learn-what-expect-2026-benefits-wellness-fair
  - (wellness) [KTVU] 10/23/2026, 12:55 PM, +0000 UTC — Bay Area entrepreneurs part of growing "Wellness Event" economy
    
    Link: https://www.ktvu.com/news/womens-wellness-experiences-popularity
  - (wellness) [Binghamton University] 10/26/2026, 03:37 PM, +0000 UTC — 75,000-square-foot expansion ushers in new era of wellness at Binghamton’s East Gym
    
    Link: https://www.binghamton.edu/news/story/6550/east-gym-ushers-in-a-new-era-of-wellness-at-binghamton-university
  - (wellness) [Carroll College] 10/22/2026, 07:00 AM, +0000 UTC — Know. Support. Connect.: A Campus Wellness Initiative
    
    Link: https://www.carroll.edu/news-events/news/know-support-connect-campus-wellness-initiative
  - (wellness) [Native News Online] 10/23/2026, 05:29 PM, +0000 UTC — Alaska Native Communities Get $375K for Health and Wellness
    
    Link: https://nativenewsonline.net/health/alaska-native-communities-get-375k-for-health-and-wellness/
  - (medical study) [Stanford Medicine] 10/21/2026, 06:06 PM, +0000 UTC — ‘Digital twins’ of immune system in pregnancy identify drugs to prevent early labor, Stanford Medicine-led study finds
    
    Link: https://med.stanford.edu/news/all-news/2026/10/preterm-labor-drug.html
  - (medical study) [The Cancer Letter] 10/23/2026, 09:40 PM, +0000 UTC — The $8.4B bond makes a long-term investment in a field with life-saving power
    
    Link: https://cancerletter.com/perspective/20261023_4/
  - (medical study) [VCU Health] 10/26/2026, 09:42 PM, +0000 UTC — VCU receives $3.8 million NIH grant to study potential heart failure therapy
    
    Link: https://www.vcuhealth.org/news/vcu-receives-38-million-nih-grant-to-study-potential-heart-failure-therapy/
  - (medical study) [Nature] 10/21/2026, 10:33 AM, +0000 UTC — Global, regional and national burden of pertussis in 1990–2023: a Global Burden of Disease study
    
    Link: https://www.nature.com/articles/s41591-026-04660-8
  - (medical study) [Ohio Capital Journal] 10/27/2026, 08:02 AM, +0000 UTC — Medical debt hit 1 in 4 Americans and 1 in 5 Ohioans last year, even the insured, study shows
    
    Link: https://ohiocapitaljournal.com/2026/10/27/medical-debt-hit-1-in-4-americans-and-1-in-5-ohioans-last-year-even-the-insured-study-shows/
  - (medical study) [The University of Oklahoma] 10/26/2026, 08:47 PM, +0000 UTC — Weight-loss surgery produces lasting diabetes remission, long-term study finds
    
    Link: http://ou.edu/content/news/articles/2026/october/weight-loss-surgery-lasting-diabetes-remission-long-term-study
  - (medical study) [Yale School of Medicine] 10/23/2026, 03:03 PM, +0000 UTC — Study Reveals Amino Acid Can Diminish Age-Related Inflammation
    
    Link: https://medicine.yale.edu/news-article/amino-acid-diminishes-age-related-inflammation/
  - (medical study) [Penn Medicine] 10/23/2026, 01:34 PM, +0000 UTC — What makes you, you? Massive study maps the genetics of personality
    
    Link: https://www.pennmedicine.org/news/massive-study-maps-the-genetics-of-personality
  - (medical study) [www.dicardiology.com] 10/23/2026, 04:59 PM, +0000 UTC — First U.S. Patients Enrolled in Clinical Study Evaluating Pulmonary Artery Denervation
    
    Link: https://www.dicardiology.com/content/first-us-patients-enrolled-clinical-study-evaluating-pulmonary-artery-denervation
  - (medical study) [News-Medical] 10/22/2026, 07:45 PM, +0000 UTC — Study defines average human genome and normal genetic disease risk
    
    Link: https://www.news-medical.net/news/20261022/Study-defines-average-human-genome-and-normal-genetic-disease-risk.aspx
  - (medical study) [National Institutes of Health (NIH) | (.gov)] 10/23/2026, 04:30 PM, +0000 UTC — A precision T-cell therapy stalls treatment-resistant cancers in clinical trial
    
    Link: https://www.nih.gov/news-events/news-releases/precision-t-cell-therapy-stalls-treatment-resistant-cancers-clinical-trial
  - (medical study) [the University of South Florida] 10/22/2026, 07:34 PM, +0000 UTC — USF Health, Tampa General study finds metastatic colorectal cancer’s immune defenses may begin outside the cancer cell, challenging view held for decades
    
    Link: https://www.usf.edu/health/news/2026/usf-health-tampa-general-study-finds-metastatic-colorectal-cancers-immune-defenses-may-begin-outside-the-cancer-cell.aspx
  - (clinical trial health) [The American Journal of Managed Care] 10/23/2026, 05:42 AM, +0000 UTC — Ochsner Health, Paradigm Health Partnership Expands Clinical Trial Access Across the Gulf South
    
    Link: https://www.ajmc.com/view/ochsner-health-paradigm-health-partnership-expands-clinical-trial-access-across-the-gulf-south
  - (clinical trial health) [Healthcare IT News] 10/21/2026, 01:40 PM, +0000 UTC — Oracle and AstraZeneca to collaborate on 'smarter' clinical trials
    
    Link: https://www.healthcareitnews.com/news/oracle-and-astrazeneca-collaborate-smarter-clinical-trials
  - (clinical trial health) [Cleveland Clinic Newsroom] 10/26/2026, 05:11 PM, +0000 UTC — Cleveland Clinic and Dyania’s Work on AI in Clinical Trial Matching Earns 2026 Gartner Eye on Innovation Award
    
    Link: https://newsroom.clevelandclinic.org/2026/10/26/cleveland-clinic-and-dyanias-work-on-ai-in-clinical-trial-matching-earns-2026-gartner-eye-on-innovation-award
  - (clinical trial health) [Applied Clinical Trials Online] 10/20/2026, 05:49 PM, +0000 UTC — AstraZeneca and Oracle Outline AI Collaboration for Clinical Trial Recruitment and Safety Monitoring
    
    Link: https://www.appliedclinicaltrialsonline.com/view/astrazeneca-oracle-ai-collaboration-clinical-trial-recruitment-safety-monitoring
  - (clinical trial health) [Science Daily] 10/23/2026, 11:04 AM, +0000 UTC — Breakthrough PTSD treatment achieves 68% remission rate in clinical trial
    
    Link: https://www.sciencedaily.com/releases/2026/10/261022081309.htm
  - (clinical trial health) [The Clinical Trial Vanguard] 10/27/2026, 01:08 PM, +0000 UTC — AI Is Already Inside the Doctor’s Visit. The Question Is Whether It’s Helping or Hunting for Billable Findings.
    
    Link: https://www.clinicaltrialvanguard.com/clinical-bellwether/ai-is-already-inside-the-doctors-visit-the-question-is-whether-its-helping-or-hunting-for-billable-findings/
  - (clinical trial health) [pharmaphorum] 10/22/2026, 10:06 AM, +0000 UTC — Clinical trial setup times fall sharply in UK
    
    Link: https://pharmaphorum.com/news/clinical-trial-setup-times-fall-sharply-uk
  - (clinical trial health) [Al Jazeera] 10/24/2026, 12:42 AM, +0000 UTC — WHO announces start of Ebola vaccine clinical trial in DR Congo
    
    Link: https://www.aljazeera.com/news/2026/10/24/who-announces-start-of-ebola-vaccine-clinical-trial-in-dr-congo
  - (clinical trial health) [Milken Institute] 10/22/2026, 07:00 AM, +0000 UTC — Milken Institute Statement of Support for Legislative Efforts to Modernize Clinical Trials and Accelerate Cures
    
    Link: https://milkeninstitute.org/content-hub/policy-perspectives/statement-support/milken-institute-statement-support-legislative-efforts-modernize-clinical-trials-and-accelerate
  - (clinical trial health) [Fierce Biotech] 10/27/2026, 09:00 AM, +0000 UTC — BMS joins 3-year partnership to boost participation in cancer trials
    
    Link: https://www.fiercebiotech.com/cro/bms-partners-healthcare-improvement-organization-expand-access-cancer-clinical-trials
  - (clinical trial health) [Medscape] 10/21/2026, 08:57 AM, +0000 UTC — Med Op-Ed: Time Toxicity, Clinical Trial Access, and RECIST
    
    Link: https://www.medscape.com/viewarticle/med-op-ed-time-toxicity-clinical-trial-access-and-recist-2026a10013hh
  - (clinical trial health) [News-Medical] 10/22/2026, 08:47 PM, +0000 UTC — Clinical trial establishes effective HIV dosing regimen for full-term newborns
    
    Link: https://www.news-medical.net/news/20261022/Clinical-trial-establishes-effective-HIV-dosing-regimen-for-full-term-newborns.aspx
  - (FDA recall health) [Health.com] 10/21/2026, 06:29 PM, +0000 UTC — FDA Announces Nationwide Recall of More Than 4 Million Tubes of Toothpaste
    
    Link: https://www.health.com/toothpaste-recall-october-2026-12186381
  - (FDA recall health) [Good Housekeeping] 10/21/2026, 02:49 PM, +0000 UTC — FDA Announces Nationwide Recall of GLP-1 Medications–Here's the Full List of Products
    
    Link: https://www.goodhousekeeping.com/health/a74204439/glp-1-recall-tirzepatide-injections/
  - (FDA recall health) [LiveNOW from FOX] 10/21/2026, 03:58 PM, +0000 UTC — What to know about GLP-1s and cannabis use
    
    Link: https://www.livenowfox.com/news/fda-recalls-glp-1-drug-sterility-concerns
  - (FDA recall health) [USA Today] 10/21/2026, 04:01 PM, +0000 UTC — Over 4 million tubes of toothpaste recalled. See affected products
    
    Link: https://www.usatoday.com/story/money/consumer-protection/recalls-alerts/2026/10/21/toothpaste-recall-brush-buddies-evo/92344819007/
  - (FDA recall health) [Prevention] 10/22/2026, 06:23 PM, +0000 UTC — FDA Announces Nationwide Toothpaste Recall Affecting More Than 4 Million Tubes
    
    Link: https://www.prevention.com/health/a74220169/toothpaste-recall-fda/
  - (FDA recall health) [Deseret News] 10/22/2026, 07:04 PM, +0000 UTC — 4.3 million tubes of toothpaste — including kids’ — recalled
    
    Link: https://www.deseret.com/lifestyle/2026/10/22/childrens-toothpaste-recall-fda-class2-millions-pritam-international-private-limited/
  - (FDA recall health) [Fox Business] 10/20/2026, 08:57 PM, +0000 UTC — GLP-1 injections recalled nationwide over sterility concerns
    
    Link: https://www.foxbusiness.com/healthcare/glp-1-injections-recalled-nationwide-over-sterility-concerns
  - (FDA recall health) [News12 | New Jersey] 10/23/2026, 12:22 PM, +0000 UTC — Fda Recalls More Than 4 Million Tubes Of Toothpaste
    
    Link: https://newjersey.news12.com/2026/10/23/fda-recalls-more-than-4-million-tubes-of-toothpaste/2utI8VS4sJ89ajROCk7rgP
  - (FDA recall health) [MedShadow Foundation] 10/21/2026, 04:27 PM, +0000 UTC — FDA Recalls and Warnings: Epilepsy Drug Mix-Up, Subpotent Thyroid Medication, and More
    
    Link: https://medshadow.org/drug-updates-recalls/fda-recalls-and-warnings/levoxyl-amlodipine-olmesartan/
  - (FDA recall health) [KOCO] 10/20/2026, 08:48 PM, +0000 UTC — FDA recalls 4.3 million tubes of adult and children's toothpaste
    
    Link: https://www.koco.com/article/fda-brush-budies-toothpaste-recall-nationwide/74195828
  - (FDA recall health) [NewsNation] 10/23/2026, 02:09 PM, +0000 UTC — More than 4 million tubes of toothpaste recalled nationwide: FDA
    
    Link: https://www.newsnationnow.com/us-news/recalls/4m-tubes-toothpaste-recalled-nationwide-fda/
  - (FDA recall health) [kare11.com] 10/21/2026, 06:26 PM, +0000 UTC — Toothpaste recall for more than 4 million tubes includes ones for kids
    
    Link: https://www.kare11.com/article/news/nation-world/toothpaste-recall-list-brush-buddies-evo-aru/507-eba20cac-f7d6-45d5-af44-49f612d9d3b9