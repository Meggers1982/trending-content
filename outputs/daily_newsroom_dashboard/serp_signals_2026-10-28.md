# LIVE SIGNAL DATA — SerpAPI Pre-Fetch
The following signals were fetched from SerpAPI Google News and SerpAPI Google Trends immediately before this pipeline run. Treat Google Trends as AVAILABLE when this section contains a Google Trends block. Use it as the primary search_velocity input for Skills 01–05 (Signal Listener through Trend Strength Scorer). Use the Google News Radar as the broad discovery layer for news-led health topics, including topics that do not yet appear in Google Trends. Prioritize topics with convergence across News, Trends, primary/institutional sources, and credible publisher coverage.

## Google Trends — Trending Now (US / Health, real-time)
Terms with a "Why:" line have a confirmed real-world news story driving the spike; terms without one are a real-time signal only, not yet grounded in a specific story.
  - drug resistance
    Why: "These superbugs pose the biggest threat to Americans, CDC says" — The Washington Post
  - ozempic versus retatrutide a1c study
    Why: "New weight loss drug retatrutide provides double the weight loss of Ozempic, Lilly says" — ABC News - Breaking News, Latest News and Videos
  - nigeria
    Why: "First confirmed Ebola patient in Nigeria evacuated to Switzerland" — CNN

## Google Trends — 7-Day Interest (US)
  - **health**: latest=93, peak=100, 7d-delta=-1
    Rising related: tea heart health, what did the new study find about daily tea drinking and heart health, health care fraud, fairmount behavioral health system, health insurance agency, when is open enrollment for health insurance 2027, advocate health careers, health insurance
  - **wellness**: latest=54, peak=100, 7d-delta=-11
    Rising related: best productivity apps 2025, trending beauty hacks, non-toxic air fryer, aura points / aura slang, ai personal assistant, ai image enhancer, kitchen tech upgrades, tech gadgets 2025
  - **nutrition**: latest=87, peak=100, 7d-delta=-13
    Rising related: beller nutrition, sp nutrition magnesium bisglycinate gummies review, supplemental nutrition assistance program, what is dark nutrition, skin nutrition botanicals, nutrition sources nyt, dark nutrition, organised nutrition reviews
  - **fitness**: latest=52, peak=100, 7d-delta=-2
    Rising related: planet fitness closing locations, la fitness shutting down gyms, planet fitness customer retention issues, fitbit edge alternative fitness trackers, james webb space telescope, streaming shows trending, brown bear hunter encounter video, minimalist lifestyle trend
  - **food safety**: latest=60, peak=100, 7d-delta=-4
    Rising related: aluminum foil leftover food safety, mailing paper checks safety risks, walmart great value fruit cocktail recall, food should be stored at least which distance from the floor, the viral infection hepatitis a can be controlled by, a foodborne illness outbreak consists of, king county food safety rating, national registry of food safety professionals
  - **diet**: latest=84, peak=100, 7d-delta=-8
    Rising related: humanin shmoose mediterranean diet study, diet coke advent calendar, trisha yearwood diet and zumba, diet coke logo, diet coke, mediterranean, mediterranean diet, healthy diet
  - **weight loss**: latest=61, peak=100, 7d-delta=+5
    Rising related: trisha yearwood weight loss journey, glp-1 weight loss usage statistics, eli lilly weight loss ads ruling, ethan klein weight loss, justine lupe weight loss, trisha yearwood weight loss transformation, trisha yearwood, trisha yearwood weight loss
  - **mental health**: latest=84, peak=100, 7d-delta=-9
    Rising related: mental health women villakalima, teen mental health treatment malibu ca visionsteen, teen mental health treatment malibu ca visionsteen.com, mental health women villakalima.com, my bib, what is mental health, mental health services, mental health help
  - **gut health**: latest=44, peak=100, 7d-delta=-4
    Rising related: gut health specialist near me, hack your health the secrets of your gut, butyrate for gut health, how to restore gut health, what is gut health, gut health foods, gut health probiotics, probiotics

Top rising related queries from Google Trends:
  - tea heart health
  - what did the new study find about daily tea drinking and heart health
  - health care fraud
  - fairmount behavioral health system
  - health insurance agency
  - when is open enrollment for health insurance 2027
  - advocate health careers
  - health insurance
  - best productivity apps 2025
  - trending beauty hacks
  - non-toxic air fryer
  - aura points / aura slang
  - ai personal assistant
  - ai image enhancer
  - kitchen tech upgrades
  - tech gadgets 2025
  - beller nutrition
  - sp nutrition magnesium bisglycinate gummies review
  - supplemental nutrition assistance program
  - what is dark nutrition

## Google News Radar — Recent Health Topics (144 unique across 12 queries; showing 60)
Treat these headlines as the broad radar of news-led health topics. The Signal Listener must consider this radar before narrowing to retained candidates.
  - (health) [Centers for Disease Control and Prevention | CDC (.gov)] 10/23/2026, 07:00 AM, +0000 UTC — One Health Day Communications Toolkit
    
    Link: https://www.cdc.gov/one-health/php/trainings-events/one-health-day.html
  - (health) [KFF] 10/23/2026, 07:00 AM, +0000 UTC — Americans’ Challenges with Health Care Costs
    
    Link: https://www.kff.org/health-costs/americans-challenges-with-health-care-costs/
  - (health) [Commonwealth Fund] 10/22/2026, 12:00 PM, +0000 UTC — The State of Health Insurance Coverage in 2026
    
    Link: https://www.commonwealthfund.org/publications/surveys/2026/oct/state-health-insurance-coverage-2026-biennial-survey
  - (health) [County of San Luis Obispo (.gov)] 10/27/2026, 11:21 PM, +0000 UTC — Public Health Confirms Five Shiga toxin-producing E. Coli Cases; Local Farm Suspected as Potential S
    
    Link: https://www.slocounty.ca.gov/departments/slo-health/public-health/department-news/public-health-confirms-five-shiga-toxin-producing-e-coli-cases;-local-farm-suspected-as-potential-s
  - (health) [USDA (.gov)] 10/23/2026, 07:00 AM, +0000 UTC — Screwworm.gov | Animal and Plant Health Inspection Service
    
    Link: https://www.aphis.usda.gov/animals/animal-health/livestock-and-poultry-disease/stop-screwworm
  - (health) [The New York Times] 10/22/2026, 09:03 AM, +0000 UTC — Employers Shift Rising Health Care Costs Onto Millions of Workers
    
    Link: https://www.nytimes.com/2026/10/22/business/health-insurance-costs-workers-premiums-deductibles.html
  - (health) [NPR] 10/22/2026, 09:00 AM, +0000 UTC — High health costs squeeze workers, even if you have good insurance through a job
    
    Link: https://www.npr.org/2026/10/22/nx-s1-6008153/health-insurance-costs-kff-commonwealth
  - (health) [UNM HSC Newsroom] 10/27/2026, 06:04 PM, +0000 UTC — Update on Cybersecurity Event at UNM Health Sciences Center
    
    Link: https://hscnews.unm.edu/news/ambulance-traffic-diverted-clinical-appointments-cancelled-and-classes-cancelled-due-to-cybersecurity-issue-at-unm-hsc
  - (health) [World Health Organization (WHO)] 10/28/2026, 08:04 AM, +0000 UTC — Climate change is a growing health emergency, Lancet Countdown warns
    
    Link: https://www.who.int/news/item/28-10-2026-climate-change-is-a-growing-health-emergency--lancet-countdown-warns
  - (health) [Peterson-KFF Health System Tracker] 10/22/2026, 07:00 AM, +0000 UTC — How much is health spending expected to grow?
    
    Link: https://www.healthsystemtracker.org/chart-collection/how-much-is-health-spending-expected-to-grow/
  - (health) [U.S. Food and Drug Administration (.gov)] 10/22/2026, 12:00 AM, +0000 UTC — FDA Food Code
    
    Link: https://www.fda.gov/food/retail-food-protection/fda-food-code
  - (health) [Health.com] 10/23/2026, 07:00 AM, +0000 UTC — 9 Gut-Healthy Drinks Dietitians Recommend for Better Digestion
    
    Link: https://www.health.com/drinks-to-help-digestion-12188063
  - (wellness) [CNN] 10/22/2026, 06:59 PM, +0000 UTC — ‘Wellness darties’: Inside Gen Z’s sober workout parties
    
    Link: https://www.cnn.com/2026/10/22/us/video/wellness-darties-college-students-find-new-way-to-party
  - (wellness) [The New York Times] 10/22/2026, 07:00 AM, +0000 UTC — While Advising Kennedy, Top Aide Had More Than $25 Million Stake in Wellness Company
    
    Link: https://www.nytimes.com/2026/04/24/health/calley-means-truemed-trump-health-savings.html
  - (wellness) [NBC 5 Dallas-Fort Worth] 10/23/2026, 08:51 PM, +0000 UTC — Iconic Dallas Granada Theater sells to New York based wellness brand
    
    Link: https://www.nbcdfw.com/news/local/historic-granada-theater-sells-to-new-york-based-wellness-brand/4095056/
  - (wellness) [The Santa Barbara Independent] 10/23/2026, 08:19 PM, +0000 UTC — San Marcos High School Breaks Ground on Building Community Wellness Project
    
    Link: https://www.independent.com/2026/10/23/san-marcos-high-school-breaks-ground-on-building-community-wellness-project/
  - (wellness) [DVIDS] 10/22/2026, 05:23 PM, +0000 UTC — News - Fort McCoy Wellness Fair draws strong participation in 2026
    
    Link: https://www.dvidshub.net/news/577622/fort-mccoy-wellness-fair-draws-strong-participation-2026
  - (wellness) [Binghamton University] 10/26/2026, 03:37 PM, +0000 UTC — 75,000-square-foot expansion ushers in new era of wellness at Binghamton’s East Gym
    
    Link: https://www.binghamton.edu/news/story/6550/east-gym-ushers-in-a-new-era-of-wellness-at-binghamton-university
  - (wellness) [Case Western Reserve University] 10/22/2026, 02:47 PM, +0000 UTC — Learn what to expect at the 2026 Benefits & Wellness Fair
    
    Link: https://case.edu/news/learn-what-expect-2026-benefits-wellness-fair
  - (wellness) [Texas A&M University-Commerce] 10/27/2026, 08:26 PM, +0000 UTC — ETAMU Professor Builds Global Community Through Wellness Counseling
    
    Link: https://www.etamu.edu/news/etamu-professor-builds-global-community-through-wellness-counseling/
  - (wellness) [Carroll College] 10/22/2026, 07:00 AM, +0000 UTC — Know. Support. Connect.: A Campus Wellness Initiative
    
    Link: https://www.carroll.edu/news-events/news/know-support-connect-campus-wellness-initiative
  - (wellness) [Forbes] 10/22/2026, 11:00 AM, +0000 UTC — Mahjong Is A Hot Travel Trend—With Wellness, Cocktails And More
    
    Link: https://www.forbes.com/sites/larryolmsted/2026/10/22/mahjong-is-a-hot-travel-trend-with-wellness-cocktails-and-more/
  - (wellness) [Native News Online] 10/23/2026, 05:29 PM, +0000 UTC — Alaska Native Communities Get $375K for Health and Wellness
    
    Link: https://nativenewsonline.net/health/alaska-native-communities-get-375k-for-health-and-wellness/
  - (wellness) [Spencer Fane] 10/23/2026, 04:41 PM, +0000 UTC — WHOOP There It Goes: Wellness Has a New Avenue for Trend Tracking Minus Device-Type Claims
    
    Link: https://www.spencerfane.com/insight/whoop-there-it-goes-wellness-has-a-new-avenue-for-trend-tracking-minus-device-type-claims/
  - (medical study) [Stanford Medicine] 10/21/2026, 06:06 PM, +0000 UTC — ‘Digital twins’ of immune system in pregnancy identify drugs to prevent early labor, Stanford Medicine-led study finds
    
    Link: https://med.stanford.edu/news/all-news/2026/10/preterm-labor-drug.html
  - (medical study) [VCU Health] 10/26/2026, 09:42 PM, +0000 UTC — VCU receives $3.8 million NIH grant to study potential heart failure therapy
    
    Link: https://www.vcuhealth.org/news/vcu-receives-38-million-nih-grant-to-study-potential-heart-failure-therapy/
  - (medical study) [Ohio Capital Journal] 10/27/2026, 08:02 AM, +0000 UTC — Medical debt hit 1 in 4 Americans and 1 in 5 Ohioans last year, even the insured, study shows
    
    Link: https://ohiocapitaljournal.com/2026/10/27/medical-debt-hit-1-in-4-americans-and-1-in-5-ohioans-last-year-even-the-insured-study-shows/
  - (medical study) [Yale School of Medicine] 10/23/2026, 03:03 PM, +0000 UTC — Study Reveals Amino Acid Can Diminish Age-Related Inflammation
    
    Link: https://medicine.yale.edu/news-article/amino-acid-diminishes-age-related-inflammation/
  - (medical study) [The University of Oklahoma] 10/26/2026, 08:47 PM, +0000 UTC — Weight-loss surgery produces lasting diabetes remission, long-term study finds
    
    Link: http://ou.edu/content/news/articles/2026/october/weight-loss-surgery-lasting-diabetes-remission-long-term-study
  - (medical study) [National Institutes of Health (NIH) | (.gov)] 10/23/2026, 04:30 PM, +0000 UTC — A precision T-cell therapy stalls treatment-resistant cancers in clinical trial
    
    Link: https://www.nih.gov/news-events/news-releases/precision-t-cell-therapy-stalls-treatment-resistant-cancers-clinical-trial
  - (medical study) [News-Medical] 10/26/2026, 12:01 AM, +0000 UTC — Beer, wine or spirits: A large study finds different mortality patterns for each
    
    Link: https://www.news-medical.net/news/20261025/Beer-wine-or-spirits-A-large-study-finds-different-mortality-patterns-for-each.aspx
  - (medical study) [Anthropic] 10/27/2026, 08:20 PM, +0000 UTC — Early progress on accelerating drug development with Claude
    
    Link: https://www.anthropic.com/research/early-progress-drug-development
  - (medical study) [Nature] 10/27/2026, 08:15 PM, +0000 UTC — Rethinking the concept of ‘no direct benefit’ in clinical research
    
    Link: https://www.nature.com/articles/s41581-026-01150-5
  - (medical study) [Mayo Clinic News Network] 10/23/2026, 04:36 PM, +0000 UTC — Investigational vaccine generates immune response to KRAS mutations in pancreatic cancer study
    
    Link: https://newsnetwork.mayoclinic.org/discussion/investigational-vaccine-generates-immune-response-to-kras-mutations-in-pancreatic-cancer-study/
  - (medical study) [CIDRAP] 10/26/2026, 06:45 PM, +0000 UTC — Medical assistants talk to families about vaccines in about half of visits, study finds
    
    Link: https://www.cidrap.umn.edu/childhood-vaccines/medical-assistants-talk-families-about-vaccines-about-half-visits-study-finds
  - (medical study) [Science Daily] 10/23/2026, 11:04 AM, +0000 UTC — Breakthrough PTSD treatment achieves 68% remission rate in clinical trial
    
    Link: https://www.sciencedaily.com/releases/2026/10/261022081309.htm
  - (clinical trial health) [The American Journal of Managed Care] 10/23/2026, 05:42 AM, +0000 UTC — Ochsner Health, Paradigm Health Partnership Expands Clinical Trial Access Across the Gulf South
    
    Link: https://www.ajmc.com/view/ochsner-health-paradigm-health-partnership-expands-clinical-trial-access-across-the-gulf-south
  - (clinical trial health) [Morgan Griffith (.gov)] 10/22/2026, 08:17 PM, +0000 UTC — Chairman Griffith Helps Lead Effort to Revamp Rural Patient Access to Clinical Trials, Accelerate New Treatments to Market
    
    Link: https://morgangriffith.house.gov/news/documentsingle.aspx?DocumentID=405855
  - (clinical trial health) [Cleveland Clinic Newsroom] 10/26/2026, 05:11 PM, +0000 UTC — Cleveland Clinic and Dyania’s Work on AI in Clinical Trial Matching Earns 2026 Gartner Eye on Innovation Award
    
    Link: https://newsroom.clevelandclinic.org/2026/10/26/cleveland-clinic-and-dyanias-work-on-ai-in-clinical-trial-matching-earns-2026-gartner-eye-on-innovation-award
  - (clinical trial health) [The Clinical Trial Vanguard] 10/27/2026, 01:08 PM, +0000 UTC — AI Is Already Inside the Doctor’s Visit. The Question Is Whether It’s Helping or Hunting for Billable Findings.
    
    Link: https://www.clinicaltrialvanguard.com/clinical-bellwether/ai-is-already-inside-the-doctors-visit-the-question-is-whether-its-helping-or-hunting-for-billable-findings/
  - (clinical trial health) [pharmaphorum] 10/22/2026, 10:06 AM, +0000 UTC — Clinical trial setup times fall sharply in UK
    
    Link: https://pharmaphorum.com/news/clinical-trial-setup-times-fall-sharply-uk
  - (clinical trial health) [Chain Store Age] 10/27/2026, 07:25 PM, +0000 UTC — Walmart, Care Access to expand in-store clinical trial centers
    
    Link: https://chainstoreage.com/walmart-care-access-expand-store-clinical-trial-centers
  - (clinical trial health) [Applied Clinical Trials Online] 10/28/2026, 11:24 AM, +0000 UTC — What It Would Take to Make Community Trials Accessible and Scalable
    
    Link: https://www.appliedclinicaltrialsonline.com/view/what-would-take-make-community-trials-accessible-scalable
  - (clinical trial health) [Al Jazeera] 10/24/2026, 12:42 AM, +0000 UTC — WHO announces start of Ebola vaccine clinical trial in DR Congo
    
    Link: https://www.aljazeera.com/news/2026/10/24/who-announces-start-of-ebola-vaccine-clinical-trial-in-dr-congo
  - (clinical trial health) [Drug Store News] 10/27/2026, 06:13 PM, +0000 UTC — Walmart, Care Access plan 3 additional clinical trial centers
    
    Link: https://drugstorenews.com/walmart-care-access-plan-3-additional-clinical-trial-centers
  - (clinical trial health) [Clinical Trials Arena] 10/28/2026, 10:11 AM, +0000 UTC — Walmart and Care Access to open three clinical trial centres in US
    
    Link: https://www.clinicaltrialsarena.com/news/walmart-care-access-three-trial-centres-us/?
  - (clinical trial health) [Fierce Biotech] 10/27/2026, 09:00 AM, +0000 UTC — BMS joins 3-year partnership to boost participation in cancer trials
    
    Link: https://www.fiercebiotech.com/cro/bms-partners-healthcare-improvement-organization-expand-access-cancer-clinical-trials
  - (clinical trial health) [News-Medical] 10/22/2026, 08:47 PM, +0000 UTC — Clinical trial establishes effective HIV dosing regimen for full-term newborns
    
    Link: https://www.news-medical.net/news/20261022/Clinical-trial-establishes-effective-HIV-dosing-regimen-for-full-term-newborns.aspx
  - (FDA recall health) [Health.com] 10/21/2026, 06:29 PM, +0000 UTC — FDA Announces Nationwide Recall of More Than 4 Million Tubes of Toothpaste
    
    Link: https://www.health.com/toothpaste-recall-october-2026-12186381
  - (FDA recall health) [U.S. Food and Drug Administration (.gov)] 10/24/2026, 09:01 AM, +0000 UTC — FDA Advises Not to Eat, Sell, or Serve Cold Smoked Sprats Sold by Haifa Smoked Fish, Inc.
    
    Link: https://www.fda.gov/food/alerts-advisories-safety-information/fda-advises-not-eat-sell-or-serve-cold-smoked-sprats-sold-haifa-smoked-fish-inc
  - (FDA recall health) [Deseret News] 10/22/2026, 07:04 PM, +0000 UTC — 4.3 million tubes of toothpaste — including kids’ — recalled
    
    Link: https://www.deseret.com/lifestyle/2026/10/22/childrens-toothpaste-recall-fda-class2-millions-pritam-international-private-limited/
  - (FDA recall health) [The Healthy @Reader's Digest] 10/27/2026, 12:43 AM, +0000 UTC — Butter Recall: FDA Report Cites Concerns of ‘Yeast, Mold, and E. coli’
    
    Link: https://www.thehealthy.com/news/butter-recall-october-2026/
  - (FDA recall health) [Good Housekeeping] 10/22/2026, 01:41 PM, +0000 UTC — FDA Announces Nationwide Recall of Popular Toothpastes—Here’s Everything You Need to Know
    
    Link: https://www.goodhousekeeping.com/what-to-buy/beauty-products/a74208527/toothpaste-recall-brush-buddies/
  - (FDA recall health) [Detroit Free Press] 10/28/2026, 01:51 AM, +0000 UTC — Walmart Great Value fruit cocktail recalled. Is Michigan affected?
    
    Link: https://www.freep.com/story/entertainment/dining/2026/10/27/recall-great-value-walmart-fruit-cocktail-michigan-fda/92456963007/
  - (FDA recall health) [Prevention] 10/22/2026, 06:23 PM, +0000 UTC — More Than 4 Million Tubes of Toothpaste Recalled Nationwide, FDA Warns
    
    Link: https://www.prevention.com/health/a74220169/toothpaste-recall-fda/
  - (FDA recall health) [News12 | New Jersey] 10/23/2026, 12:22 PM, +0000 UTC — Fda Recalls More Than 4 Million Tubes Of Toothpaste
    
    Link: https://newjersey.news12.com/2026/10/23/fda-recalls-more-than-4-million-tubes-of-toothpaste/2utI8VS4sJ89ajROCk7rgP
  - (FDA recall health) [The Hill] 10/28/2026, 11:29 AM, +0000 UTC — Recalled butter sold in 10 states receives risk warning: FDA
    
    Link: https://thehill.com/homenews/state-watch/6175447-miyokos-creamery-butter-recalled/
  - (FDA recall health) [Newsweek] 10/22/2026, 04:08 AM, +0000 UTC — Children’s Toothpaste Among 4M Tubes Recalled Over Potential Health Risk
    
    Link: https://www.newsweek.com/childrens-toothpaste-including-barbie-hot-wheels-brands-among-4m-tubes-recalled-12603015
  - (FDA recall health) [Food Safety News] 10/28/2026, 12:05 AM, +0000 UTC — FDA issues another warning against Darwin's pet food; firm refuses to initiate recall
    
    Link: https://www.foodsafetynews.com/2026/10/fda-issues-another-warning-against-darwins-pet-food-firm-refuses-to-initiate-recall/
  - (FDA recall health) [FOX 8 News] 10/22/2026, 11:10 AM, +0000 UTC — Major toothpaste recall includes more than 4 million tubes, many marketed for kids
    
    Link: https://fox8.com/news/major-toothpaste-recall-includes-more-than-4-million-tubes-many-marketed-for-kids/