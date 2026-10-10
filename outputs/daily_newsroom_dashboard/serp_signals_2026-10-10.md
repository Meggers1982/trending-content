# LIVE SIGNAL DATA — SerpAPI Pre-Fetch
The following signals were fetched from SerpAPI Google News and SerpAPI Google Trends immediately before this pipeline run. Treat Google Trends as AVAILABLE when this section contains a Google Trends block. Use it as the primary search_velocity input for Skills 01–05 (Signal Listener through Trend Strength Scorer). Use the Google News Radar as the broad discovery layer for news-led health topics, including topics that do not yet appear in Google Trends. Prioritize topics with convergence across News, Trends, primary/institutional sources, and credible publisher coverage.

## Google Trends — Trending Now (US / Health, real-time)
Terms with a "Why:" line have a confirmed real-world news story driving the spike; terms without one are a real-time signal only, not yet grounded in a specific story.
  - william, prince of wales
    Why: "Prince William Refuses to "Stay Silent" on One Crucial Topic" — Marie Claire
  - shigella infection
    Why: "Sexually transmitted diarrhea is spreading and becoming harder to treat, doctor warns" — Fox News

## Google Trends — 7-Day Interest (US)
  - **health**: latest=42, peak=100, 7d-delta=+3
    Rising related: lane johnson mental health, james talarico mental health, mike ditka health, world mental health day 2026, world mental health day, mental health day, costco health insurance, meritain health provider portal
  - **wellness**: latest=23, peak=100, 7d-delta=-3
    Rising related: elemental wellness club, heal wellness lubbock, cure for wellness, a cure for wellness, heal wellness, elemental wellness, taylor dukes wellness, wellness center
  - **nutrition**: latest=74, peak=100, 7d-delta=-9
    Rising related: supplemental nutrition assistance program new rules, featherstone nutrition, nutrition nest, pet nutrition alliance, nutrition facts, what is nutrition, nutrition label, nutrition calculator
  - **fitness**: latest=24, peak=100, 7d-delta=-3
    Rising related: low resting heart rate fitness trend, onelife fitness martinsburg, fitness studio near me, fitness center near me, my fitness pal login, planet, planet fitness, la fitness
  - **food safety**: latest=36, peak=100, 7d-delta=-4
    Rising related: dented cans food safety risks, walmart product recalls safety notice, baris yucel food safety fine, explain botulism causes, prevention methods, and safety precautions for home food canning, walmart amazon product safety recall, cooperating taking notes and discussing violations are all steps of what, removing an apron before using the restroom is an example of, what is food safety
  - **diet**: latest=69, peak=100, 7d-delta=-13
    Rising related: diet soda weight management study, walter willett daily diet, diet beverages vs water weight loss, designates a diet product, walter willett diet, diet coke onesie, diet coke onesie adult, hills science diet cat food recall
  - **weight loss**: latest=54, peak=100, 7d-delta=-3
    Rising related: diet beverages vs water weight loss, tory johnson weight loss, katy mixon weight loss, katy mixon, explain how wegovy works for weight loss and its common side effects, american housewife, explain how mounjaro works for weight loss and its primary side effects, explain how ozempic works for weight loss and its common side effects
  - **mental health**: latest=58, peak=100, 7d-delta=+18
    Rising related: talarico mental health facility, lane johnson mental health, stephen a smith mental health, james talarico mental health, stephen a smith talks about mental health, spencer pratt, is today world mental health day, is today mental health awareness day
  - **gut health**: latest=55, peak=100, 7d-delta=-3
    Rising related: top tourist attractions in paris, best laptop for work, stewed apples recipe, are bananas good for gut health, recommend the best fermented foods to add to a daily diet for gut health, gut health uk, worst foods for gut health, what is gut health

Top rising related queries from Google Trends:
  - lane johnson mental health
  - james talarico mental health
  - mike ditka health
  - world mental health day 2026
  - world mental health day
  - mental health day
  - costco health insurance
  - meritain health provider portal
  - elemental wellness club
  - heal wellness lubbock
  - cure for wellness
  - a cure for wellness
  - heal wellness
  - elemental wellness
  - taylor dukes wellness
  - wellness center
  - supplemental nutrition assistance program new rules
  - featherstone nutrition
  - nutrition nest
  - pet nutrition alliance

## Google News Radar — Recent Health Topics (144 unique across 12 queries; showing 60)
Treat these headlines as the broad radar of news-led health topics. The Signal Listener must consider this radar before narrowing to retained candidates.
  - (health) [KFF] 10/06/2026, 07:00 AM, +0000 UTC — Current and Historical Public Opinion on Medicare-for-All and Other National Health Plan Proposals
    
    Link: https://www.kff.org/public-opinion/current-and-historical-public-opinion-on-medicare-for-all-and-other-national-health-plan-proposals/
  - (health) [HHS.gov] 10/05/2026, 03:30 PM, +0000 UTC — New Regulations Make It Easier to Find, Compare, and Report Healthcare Pricing and Coverage Information
    
    Link: https://www.hhs.gov/press-room/cms-finalizes-healthcare-price-transparency-rules.html
  - (health) [World Health Organization (WHO)] 10/09/2026, 10:55 AM, +0000 UTC — WHO urges shift from institutional to community-based mental health care
    
    Link: https://www.who.int/news/item/09-10-2026-who-urges-shift-from-institutional-to-community-based-mental-health-care
  - (health) [USDA (.gov)] 10/06/2026, 07:00 AM, +0000 UTC — Screwworm.gov | Unified Government Response To Protect the United States
    
    Link: https://www.aphis.usda.gov/animals/animal-health/livestock-and-poultry-disease/stop-screwworm
  - (health) [U.S. Embassy & Consulates in Russia (.gov)] 10/06/2026, 06:54 PM, +0000 UTC — Health Alert – U.S. Embassy Moscow, Russia (October 6, 2026)
    
    Link: https://ru.usembassy.gov/health-alert-u-s-embassy-moscow-russia-october-6-2026/
  - (health) [National Cancer Institute (.gov)] 10/07/2026, 12:00 PM, +0000 UTC — Cancer Advancement through Partnerships in Research and Infrastructure (CAPRI)
    
    Link: https://www.cancer.gov/about-nci/organization/crchd/innovative-programs/capri
  - (health) [PBS] 10/05/2026, 06:50 PM, +0000 UTC — WATCH: Trump administration issues final rule on transparency in healthcare coverage
    
    Link: https://www.pbs.org/newshour/health/watch-trump-administration-issues-final-rule-on-transparency-in-healthcare-coverage
  - (health) [Health.com] 10/07/2026, 07:00 AM, +0000 UTC — The Best Time to Eat Dinner for Better Metabolism and Sleep, According to Science
    
    Link: https://www.health.com/when-to-eat-dinner-for-better-metabolism-and-sleep-12162013
  - (health) [NPR] 10/05/2026, 09:00 AM, +0000 UTC — From floating saunas to clinical trials: How heat might help mental health
    
    Link: https://www.npr.org/2026/10/05/nx-s1-5979044/sauna-heat-therapy-mental-health-depression
  - (health) [The New York Times] 10/07/2026, 06:36 PM, +0000 UTC — A Public Health-Minded Senator Asks: What Comes After Trump and Kennedy?
    
    Link: https://www.nytimes.com/2026/10/07/us/politics/patty-murray-public-health.html
  - (health) [Think Global Health] 10/06/2026, 07:00 AM, +0000 UTC — Tracking Measles and the World's Vaccine-Preventable Diseases
    
    Link: https://www.thinkglobalhealth.org/article/vaccine-preventable-disease-a-global-tracker
  - (health) [County of San Luis Obispo (.gov)] 10/08/2026, 11:39 PM, +0000 UTC — SLO County Public Health Confirms First Measles Case of 2026
    
    Link: https://www.slocounty.ca.gov/departments/slo-health/public-health/department-news/slo-county-public-health-confirms-first-measles-case-of-2026
  - (wellness) [Pew Research Center] 10/07/2026, 01:48 PM, +0000 UTC — What Do Health and Wellness Influencers Post About?
    
    Link: https://www.pewresearch.org/data-labs/2026/10/07/what-do-health-and-wellness-influencers-post-about/
  - (wellness) [San Diego County News Center] 10/08/2026, 09:02 PM, +0000 UTC — Mental Wellness Begins with a Moment, Don’t Wait to Take Yours
    
    Link: https://www.countynewscenter.com/mental-wellness-begins-with-a-moment-dont-wait-to-take-yours/
  - (wellness) [shrewsbury-ma.gov] 10/08/2026, 12:29 AM, +0000 UTC — Winter Wellness Presentation - October 2026
    
    Link: https://shrewsburyma.gov/CivicAlerts.aspx?AID=9770
  - (wellness) [Inside WFU] 10/08/2026, 02:30 PM, +0000 UTC — New Wellness Concierge tool supports campus mental health
    
    Link: https://inside.wfu.edu/2026/10/new-wellness-concierge-tool-supports-campus-mental-health/
  - (wellness) [Purdue University] 10/06/2026, 09:04 AM, +0000 UTC — Explore benefits, wellness resources at Wednesday’s Your Path Wellness Fair
    
    Link: https://www.purdue.edu/newsroom/purduetoday/2026/Q4/explore-benefits-wellness-resources-at-wednesdays-your-path-wellness-fair
  - (wellness) [Army.mil] 10/08/2026, 03:49 PM, +0000 UTC — Ready anywhere: How virtual wellness coaching fits military life
    
    Link: https://www.army.mil/article-amp/296026/ready_anywhere_how_virtual_wellness_coaching_fits_military_life
  - (wellness) [The Chalkboard Mag] 10/06/2026, 10:40 PM, +0000 UTC — Best Amazon Prime Day Wellness Deals Worth Shopping
    
    Link: https://thechalkboardmag.com/best-amazon-prime-day-wellness-deals/
  - (wellness) [Who What Wear] 10/06/2026, 07:26 PM, +0000 UTC — Wellness Fans, I Just Saved You 3 Hours—Here Are the Best 13 Items to Buy During October Prime Day
    
    Link: https://www.whowhatwear.com/wellness/amazon-big-deal-days-2026-wellness
  - (wellness) [Fierce Pharma] 10/05/2026, 03:57 PM, +0000 UTC — Gilead partners with Calm to roll out disease-specific emotional wellness support
    
    Link: https://www.fiercepharma.com/marketing/gilead-partners-calm-roll-out-disease-specific-emotional-wellness-support
  - (wellness) [Davenport University] 10/07/2026, 02:38 PM, +0000 UTC — Davenport promotes mental wellness during Mental Health Awareness Week
    
    Link: https://post.davenport.edu/academics/davenport-promotes-mental-wellness-during-mental-health-awareness-week/
  - (wellness) [The University of Utah] 10/08/2026, 01:07 AM, +0000 UTC — Student Health & Wellness awarded $500,000 to advance campus suicide prevention
    
    Link: https://attheu.utah.edu/announcements/student-health-wellness-awarded-500000-to-advance-campus-suicide-prevention/
  - (wellness) [SBU News] 10/08/2026, 07:50 PM, +0000 UTC — Feeling Better, Working Better: Employee Wellness Fair Connects Stony Brook Employees With Resources
    
    Link: https://news.stonybrook.edu/university/feeling-better-working-better-employee-wellness-fair-connects-stony-brook-employees-with-resources/
  - (medical study) [Susquehanna University] 10/08/2026, 12:58 PM, +0000 UTC — Alumni win prestigious grants to further medical research
    
    Link: https://www.susqu.edu/alumni-win-prestigious-grants-to-further-medical-research/
  - (medical study) [University of Nebraska Medical Center] 10/08/2026, 02:59 PM, +0000 UTC — Medical research highlights, October 2026
    
    Link: https://www.unmc.edu/newsroom/2026/10/08/medical-research-highlights-october-2026/
  - (medical study) [blog.google] 10/08/2026, 10:43 PM, +0000 UTC — Study in The Lancet suggests AI could improve patient-physician relationships.
    
    Link: https://blog.google/innovation-and-ai/technology/health/amie-clinical-study-lancet/
  - (medical study) [Daily Bruin] 10/04/2026, 04:43 AM, +0000 UTC — UCLA alumnus turns medical school frustrations into AI study app ‘Neural Consult’
    
    Link: https://dailybruin.com/2026/10/03/ucla-alumnus-turns-medical-school-frustrations-into-ai-study-app-neural-consult
  - (medical study) [Stanford Medicine] 10/07/2026, 12:16 AM, +0000 UTC — One year after taking ibogaine, veterans find continued relief from PTSD
    
    Link: https://med.stanford.edu/news/all-news/2026/10/ibogaine-veterans.html
  - (medical study) [Rutgers University] 10/08/2026, 07:07 PM, +0000 UTC — How a U.S. Ban on Lab-Modified Opioids Could Stifle Medical Research
    
    Link: https://www.rutgers.edu/news/how-us-ban-lab-modified-opioids-could-stifle-medical-research
  - (medical study) [Beth Israel Deaconess Medical Center] 10/09/2026, 02:10 PM, +0000 UTC — BIDMC Researchers Conduct First Real-World Study of Safety and Quality of Patient-Facing AI in Primary Care
    
    Link: https://bidmc.org/news-stories/all-news-stories/news/2026/10/bidmc-research-shows-safety-quality-of-ai-in-primary-care
  - (medical study) [PBS] 10/04/2026, 09:00 PM, +0000 UTC — WATCH: 3 scientists win Nobel Prize in medicine for studying mysteries of the brain
    
    Link: https://www.pbs.org/newshour/health/watch-live-winner-of-the-2026-nobel-prize-in-medicine-is
  - (medical study) [The Harvard Crimson] 10/08/2026, 12:00 PM, +0000 UTC — Harvard Medical School Study Reveals How Cells Respond to Viral Infections
    
    Link: https://www.thecrimson.com/article/2026/10/8/harvard-medical-school-cells-study/
  - (medical study) [Pew Research Center] 10/07/2026, 01:48 PM, +0000 UTC — Which Health and Wellness Influencers Talk About Medical Topics? Mostly Healthcare Professionals
    
    Link: https://www.pewresearch.org/data-labs/2026/10/07/which-health-and-wellness-influencers-talk-about-medical-topics-mostly-healthcare-professionals/
  - (medical study) [Nature] 10/09/2026, 10:26 AM, +0000 UTC — AI-assisted scoping review of code sharing in clinical prediction model research
    
    Link: https://www.nature.com/articles/s41591-026-04691-1
  - (medical study) [The New York Times] 10/08/2026, 10:30 PM, +0000 UTC — Clinical Trial Indicates A.I. Chatbots Could Aid Urgent Care
    
    Link: https://www.nytimes.com/2026/10/08/technology/ai-chatbots-urgent-care.html
  - (clinical trial health) [The Clinical Trial Vanguard] 10/09/2026, 06:55 AM, +0000 UTC — Patient-Owned Health Data Model Reduces Clinical Trial Recruitment Redundancy
    
    Link: https://www.clinicaltrialvanguard.com/news/patient-owned-health-data-model-reduces-clinical-trial-recruitment-redundancy/
  - (clinical trial health) [University of Nevada, Las Vegas | UNLV] 10/05/2026, 10:49 PM, +0000 UTC — Clinical Research Trials Bring Innovative Women’s Healthcare to Southern Nevada
    
    Link: https://www.unlv.edu/news/article/clinical-research-trials-bring-innovative-womens-healthcare-southern-nevada
  - (clinical trial health) [Healthcare IT News] 10/06/2026, 02:49 PM, +0000 UTC — Ochsner uses AI to widen clinical trial screening
    
    Link: https://www.healthcareitnews.com/news/ochsner-uses-ai-widen-clinical-trial-screening
  - (clinical trial health) [UC Davis Health] 10/07/2026, 03:06 PM, +0000 UTC — Clinical trial tests AI-assisted medication device for older adults with memory loss
    
    Link: https://health.ucdavis.edu/news/headlines/clinical-trial-tests-ai-assisted-medication-device-for-older-adults-with-memory-loss/2026/09
  - (clinical trial health) [Mount Sinai] 10/05/2026, 08:39 PM, +0000 UTC — Mount Sinai Tisch Cancer Center Cuts Clinical Trial Data-Entry Time by More Than Half With Real-Time EHR-to-EDC Technology
    
    Link: https://www.mountsinai.org/about/newsroom/2026/mount-sinai-tisch-cancer-center-cuts-clinical-trial-data-entry-time-by-more-than-half-with-real-time-ehr-to-edc-tech
  - (clinical trial health) [PR Newswire] 10/08/2026, 01:15 PM, +0000 UTC — Verana Health and Bitfount Collaborate to Simplify Prescreening for Ophthalmic Clinical Trials
    
    Link: https://www.prnewswire.com/news-releases/verana-health-and-bitfount-collaborate-to-simplify-prescreening-for-ophthalmic-clinical-trials-302901571.html
  - (clinical trial health) [Fierce Biotech] 10/07/2026, 03:25 PM, +0000 UTC — ARPA-H unveils Surpass program to accelerate and expand clinical trials
    
    Link: https://www.fiercebiotech.com/cro/arpa-h-unveils-surpass-program-accelerate-and-expand-clinical-trials
  - (clinical trial health) [NBC News] 10/04/2026, 10:00 PM, +0000 UTC — In early clinical trial, people with Type 1 diabetes are able to go off insulin
    
    Link: https://www.nbcnews.com/health/health-news/early-clinical-trial-people-type-1-diabetes-are-able-go-insulin-rcna601171
  - (clinical trial health) [Evanston RoundTable] 10/08/2026, 10:19 PM, +0000 UTC — Endeavor Health joins Chicago Breast Cancer Research Consortium
    
    Link: https://evanstonroundtable.com/2026/10/08/endeavor-health-joins-chicago-breast-cancer-research-consortium/
  - (clinical trial health) [www.apaservices.org] 10/06/2026, 07:00 AM, +0000 UTC — Urging a flexible National Institutes of Health funding framework for future clinical trial investigators
    
    Link: https://www.apaservices.org/advocacy/news/flexible-nih-funding-clinical-trial
  - (clinical trial health) [PBS] 10/03/2026, 08:40 PM, +0000 UTC — Inside the study for a remedy to fight Congo's deadliest Ebola outbreak
    
    Link: https://www.pbs.org/newshour/health/inside-the-study-for-a-remedy-to-fight-congos-deadliest-ebola-outbreak
  - (clinical trial health) [News-Medical] 10/06/2026, 01:55 PM, +0000 UTC — Mount Sinai adopts automated data integration for oncology clinical trials
    
    Link: https://www.news-medical.net/news/20261006/Mount-Sinai-adopts-automated-data-integration-for-oncology-clinical-trials.aspx
  - (FDA recall health) [U.S. Food and Drug Administration (.gov)] 10/05/2026, 12:00 AM, +0000 UTC — Outbreak Investigation of E. coli O145:H28: Frozen Blueberries (July 2026)
    
    Link: https://www.fda.gov/food/outbreaks-foodborne-illness/outbreak-investigation-e-coli-o145h28-frozen-blueberries-july-2026
  - (FDA recall health) [ABC7 Eyewitness News] 10/05/2026, 10:05 PM, +0000 UTC — FDA recalls 122,000 cases of Gatorade sold across 37 states
    
    Link: https://abc7ny.com/story/fda-recalls-122000-cases-gatorade-undeclared-dyes/19910004/
  - (FDA recall health) [The New York Times] 10/03/2026, 09:01 PM, +0000 UTC — F.D.A. Classifies Salad Dressing Recall to Highest Health Risk
    
    Link: https://www.nytimes.com/2026/10/03/health/fda-recall-salata-salad-dressing-salmonella.html
  - (FDA recall health) [ABC News - Breaking News, Latest News and Videos] 10/06/2026, 03:02 AM, +0000 UTC — Over 122K cases of Gatorade recalled due to undeclared food dyes, FDA says
    
    Link: https://abcnews.com/GMA/Food/122k-cases-gatorade-recalled-due-undeclared-food-dyes/story?id=137002347
  - (FDA recall health) [Medscape] 10/06/2026, 01:29 PM, +0000 UTC — FDA Recall Problems Raise Questions About Safety, Liability
    
    Link: https://www.medscape.com/viewarticle/fda-device-recall-problems-raise-questions-about-patient-2026a10011cz
  - (FDA recall health) [Prevention] 10/08/2026, 02:56 PM, +0000 UTC — FDA Updates Nationwide Eye Drop Recall Affecting Millions of Bottles
    
    Link: https://www.prevention.com/health/a74079654/fda-updates-eye-drop-recall/
  - (FDA recall health) [El Paso Times] 10/06/2026, 11:50 AM, +0000 UTC — FDA recalls Gatorade in Texas over unlisted food coloring
    
    Link: https://www.elpasotimes.com/story/news/texasregion/2026/10/06/gatorade-recall-in-texas-lot-numbers-products-health-risks/92106375007/
  - (FDA recall health) [Health.com] 10/05/2026, 04:38 PM, +0000 UTC — FDA Announces Gatorade Recall in 37 States After Bottles Were Found to Have Undeclared Food Dyes
    
    Link: https://www.health.com/gatorade-recall-october-2026-12159566
  - (FDA recall health) [Montgomery Advertiser] 10/05/2026, 07:01 PM, +0000 UTC — Gatorade recall 2026 expands to Alabama. Check these bottles
    
    Link: https://www.montgomeryadvertiser.com/story/news/2026/10/05/fda-announces-major-gatorade-recall-2026-is-alabama-affected/92107184007/
  - (FDA recall health) [NEWStalk 870] 10/09/2026, 08:34 PM, +0000 UTC — Baby-Infant Sleep Aid Recalled by FDA Over Undisclosed Alcohol Content
    
    Link: https://newstalk870.am/fda-recalls-baby-infant-sleep-aid/
  - (FDA recall health) [Detroit Free Press] 10/06/2026, 05:55 PM, +0000 UTC — Gatorade sold in Michigan recalled. Why you should return it
    
    Link: https://www.freep.com/story/news/health/2026/10/06/gatorade-recall-michigan-fda-food-dye/92118542007/
  - (FDA recall health) [The Healthy] 10/09/2026, 05:35 AM, +0000 UTC — Supplement Powder Recall: FDA Warns of Potential ‘Cardiovascular Problems’
    
    Link: https://www.thehealthy.com/news/supplement-powder-recall-october-2026/