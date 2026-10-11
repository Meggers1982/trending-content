# LIVE SIGNAL DATA — SerpAPI Pre-Fetch
The following signals were fetched from SerpAPI Google News and SerpAPI Google Trends immediately before this pipeline run. Treat Google Trends as AVAILABLE when this section contains a Google Trends block. Use it as the primary search_velocity input for Skills 01–05 (Signal Listener through Trend Strength Scorer). Use the Google News Radar as the broad discovery layer for news-led health topics, including topics that do not yet appear in Google Trends. Prioritize topics with convergence across News, Trends, primary/institutional sources, and credible publisher coverage.

## Google Trends — Trending Now (US / Health, real-time)
Terms with a "Why:" line have a confirmed real-world news story driving the spike; terms without one are a real-time signal only, not yet grounded in a specific story.
  - michael strahan
    Why: "Michael Strahan on Helping Daughter Stay Hopeful Through Brain Cancer" — Healthline

## Google Trends — 7-Day Interest (US)
  - **health**: latest=35, peak=100, 7d-delta=-3
    Rising related: lane johnson mental health, mike ditka health, world mental health day 2026, world mental health day, mental health day, meritain health provider portal, costco health insurance, mental health
  - **wellness**: latest=18, peak=100, 7d-delta=-3
    Rising related: elemental wellness club, a cure for wellness, cure for wellness, the cure for wellness, little luxe wellness lodge, taylor dukes wellness, best productivity apps 2025, elemental wellness
  - **nutrition**: latest=70, peak=100, 7d-delta=-3
    Rising related: supplemental nutrition assistance program new rules, nutrition facts, what is nutrition, nutrition label, nutrition calculator, egg nutrition, nutrition near me, optimum nutrition
  - **fitness**: latest=13, peak=100, 7d-delta=-1
    Rising related: low resting heart rate fitness trend, onelife fitness martinsburg, fitness studio near me, netflix new releases, weather forecast today, baby stroller review, moving company quotes, pet insurance cost
  - **food safety**: latest=38, peak=100, 7d-delta=-2
    Rising related: dented cans food safety risks, sleeping children must be woken to conduct the daily health check at arrival., ecolab food safety solutions, ready to eat tcs food must be marked with the date by which it must be sold how many hours, garbage containers used by an operation should be, cooperating taking notes and discussing violations are all steps of what, baris yucel food safety fine, explain botulism causes, prevention methods, and safety precautions for home food canning
  - **diet**: latest=81, peak=100, 7d-delta=-10
    Rising related: diet soda weight management study, walter willett daily diet, diet coke onesie adult, designates a diet product, walter willett diet, diet coke onesie, pink diet coke cans, diet beverages vs water weight loss
  - **weight loss**: latest=54, peak=100, 7d-delta=-11
    Rising related: susan dell weight loss, katy mixon weight loss, american housewife, katy mixon, explain how wegovy works for weight loss and its common side effects, tory johnson weight loss, diet beverages vs water weight loss, explain how zepbound works for weight loss and its primary side effects
  - **mental health**: latest=41, peak=100, 7d-delta=-2
    Rising related: talarico mental health facility, stephen a smith mental health, is talarico in a mental health facility, james talarico mental health, lane johnson mental health, stephen a smith talks about mental health, is today world mental health day, is today mental health awareness day
  - **gut health**: latest=34, peak=100, 7d-delta=-18
    Rising related: recommend the best fermented foods to add to a daily diet for gut health, improving gut health, what is gut health, gut health foods, gut health probiotics, probiotics, foods for gut health, gut health probiotic

Top rising related queries from Google Trends:
  - lane johnson mental health
  - mike ditka health
  - world mental health day 2026
  - world mental health day
  - mental health day
  - meritain health provider portal
  - costco health insurance
  - mental health
  - elemental wellness club
  - a cure for wellness
  - cure for wellness
  - the cure for wellness
  - little luxe wellness lodge
  - taylor dukes wellness
  - best productivity apps 2025
  - elemental wellness
  - supplemental nutrition assistance program new rules
  - nutrition facts
  - what is nutrition
  - nutrition label

## Google News Radar — Recent Health Topics (144 unique across 12 queries; showing 60)
Treat these headlines as the broad radar of news-led health topics. The Signal Listener must consider this radar before narrowing to retained candidates.
  - (health) [KFF] 10/07/2026, 04:28 AM, +0000 UTC — KFF Health Tracking Poll: Health Care Issues in the Lead-Up to the 2026 Midterm Election
    
    Link: https://www.kff.org/public-opinion/kff-health-tracking-poll-health-care-issues-in-the-lead-up-to-the-2026-midterm-election/
  - (health) [HHS.gov] 10/05/2026, 03:30 PM, +0000 UTC — New Regulations Make It Easier to Find, Compare, and Report Healthcare Pricing and Coverage Information
    
    Link: https://www.hhs.gov/press-room/cms-finalizes-healthcare-price-transparency-rules.html
  - (health) [USDA (.gov)] 10/06/2026, 07:00 AM, +0000 UTC — Screwworm.gov | Animal and Plant Health Inspection Service
    
    Link: https://www.aphis.usda.gov/animals/animal-health/livestock-and-poultry-disease/stop-screwworm
  - (health) [World Health Organization (WHO)] 10/09/2026, 10:55 AM, +0000 UTC — WHO urges shift from institutional to community-based mental health care
    
    Link: https://www.who.int/news/item/09-10-2026-who-urges-shift-from-institutional-to-community-based-mental-health-care
  - (health) [U.S. Embassy & Consulates in Russia (.gov)] 10/06/2026, 06:00 PM, +0000 UTC — Health Alert – U.S. Embassy Moscow, Russia (October 6, 2026)
    
    Link: https://ru.usembassy.gov/health-alert-u-s-embassy-moscow-russia-october-6-2026/
  - (health) [National Cancer Institute (.gov)] 10/07/2026, 12:00 PM, +0000 UTC — Cancer Advancement through Partnerships in Research and Infrastructure (CAPRI)
    
    Link: https://www.cancer.gov/about-nci/organization/crchd/innovative-programs/capri
  - (health) [Health.com] 10/07/2026, 07:00 AM, +0000 UTC — The Best Time to Eat Dinner for Better Metabolism and Sleep, According to Science
    
    Link: https://www.health.com/when-to-eat-dinner-for-better-metabolism-and-sleep-12162013
  - (health) [PBS] 10/05/2026, 06:50 PM, +0000 UTC — WATCH: Trump administration issues final rule on transparency in healthcare coverage
    
    Link: https://www.pbs.org/newshour/health/watch-trump-administration-issues-final-rule-on-transparency-in-healthcare-coverage
  - (health) [European Commission] 10/10/2026, 07:10 AM, +0000 UTC — World Mental Health Day: let’s talk and listen
    
    Link: https://commission.europa.eu/news-and-media/news/world-mental-health-day-lets-talk-and-listen-2026-10-10_en
  - (health) [Virginia Department of Health (.gov)] 10/09/2026, 09:27 PM, +0000 UTC — Virginia Department of Health Closes Little Wicomico River to Shellfish Harvesting
    
    Link: https://www.vdh.virginia.gov/news/public-relations-contacts/2026-regional-news-releases/virginia-department-of-health-closes-little-wicomico-river-to-shellfish-harvesting/
  - (health) [NPR] 10/05/2026, 09:00 AM, +0000 UTC — From floating saunas to clinical trials: How heat might help mental health
    
    Link: https://www.npr.org/2026/10/05/nx-s1-5979044/sauna-heat-therapy-mental-health-depression
  - (health) [OHSU News] 10/09/2026, 04:20 PM, +0000 UTC — Late-night eating may be bad for your liver, study suggests
    
    Link: https://news.ohsu.edu/2026/10/09/late-night-eating-may-be-bad-for-your-liver-study-suggests
  - (wellness) [Axios] 10/06/2026, 10:24 AM, +0000 UTC — A massive wellness resort could transform D.C.'s Anacostia waterfront
    
    Link: https://www.axios.com/local/washington-dc/2026/10/06/therme-water-spa-wellness-resort-dmv
  - (wellness) [Pew Research Center] 10/07/2026, 01:48 PM, +0000 UTC — What Do Health and Wellness Influencers Post About?
    
    Link: https://www.pewresearch.org/data-labs/2026/10/07/what-do-health-and-wellness-influencers-post-about/
  - (wellness) [San Diego County News Center] 10/08/2026, 09:02 PM, +0000 UTC — Mental Wellness Begins with a Moment, Don’t Wait to Take Yours
    
    Link: https://www.countynewscenter.com/mental-wellness-begins-with-a-moment-dont-wait-to-take-yours/
  - (wellness) [shrewsbury-ma.gov] 10/08/2026, 12:29 AM, +0000 UTC — Winter Wellness Presentation - October 2026
    
    Link: https://shrewsburyma.gov/CivicAlerts.aspx?AID=9770
  - (wellness) [National Association of Home Builders | NAHB] 10/06/2026, 04:29 PM, +0000 UTC — How NGBS Green +WELLNESS Can Help You Target Key Home Buyer Preferences
    
    Link: https://www.nahb.org/blog/2026/10/ngbs-wellness-certification
  - (wellness) [Inside WFU] 10/08/2026, 02:30 PM, +0000 UTC — New Wellness Concierge tool supports campus mental health
    
    Link: https://inside.wfu.edu/2026/10/new-wellness-concierge-tool-supports-campus-mental-health/
  - (wellness) [Purdue University] 10/06/2026, 09:04 AM, +0000 UTC — Explore benefits, wellness resources at Wednesday’s Your Path Wellness Fair
    
    Link: https://www.purdue.edu/newsroom/purduetoday/2026/Q4/explore-benefits-wellness-resources-at-wednesdays-your-path-wellness-fair
  - (wellness) [Army.mil] 10/08/2026, 03:49 PM, +0000 UTC — Ready anywhere: How virtual wellness coaching fits military life
    
    Link: https://www.army.mil/article-amp/296026/ready_anywhere_how_virtual_wellness_coaching_fits_military_life
  - (wellness) [The Chalkboard Mag] 10/06/2026, 10:40 PM, +0000 UTC — Best Amazon Prime Day Wellness Deals Worth Shopping
    
    Link: https://thechalkboardmag.com/best-amazon-prime-day-wellness-deals/
  - (wellness) [Fierce Pharma] 10/05/2026, 03:57 PM, +0000 UTC — Gilead partners with Calm to roll out disease-specific emotional wellness support
    
    Link: https://www.fiercepharma.com/marketing/gilead-partners-calm-roll-out-disease-specific-emotional-wellness-support
  - (wellness) [Davenport University] 10/07/2026, 02:38 PM, +0000 UTC — Davenport promotes mental wellness during Mental Health Awareness Week
    
    Link: https://post.davenport.edu/academics/davenport-promotes-mental-wellness-during-mental-health-awareness-week/
  - (wellness) [The University of Utah] 10/08/2026, 01:07 AM, +0000 UTC — Student Health & Wellness awarded $500,000 to advance campus suicide prevention
    
    Link: https://attheu.utah.edu/announcements/student-health-wellness-awarded-500000-to-advance-campus-suicide-prevention/
  - (medical study) [blog.google] 10/08/2026, 10:43 PM, +0000 UTC — Study in The Lancet suggests AI could improve patient-physician relationships.
    
    Link: https://blog.google/innovation-and-ai/technology/health/amie-clinical-study-lancet/
  - (medical study) [Susquehanna University] 10/08/2026, 12:58 PM, +0000 UTC — Alumni win prestigious grants to further medical research
    
    Link: https://www.susqu.edu/alumni-win-prestigious-grants-to-further-medical-research/
  - (medical study) [Stanford Medicine] 10/07/2026, 03:09 PM, +0000 UTC — Gut microbes across continents trace ancient human migration
    
    Link: https://med.stanford.edu/news/all-news/2026/10/gut-microbiome-migration.html
  - (medical study) [Beth Israel Deaconess Medical Center] 10/09/2026, 02:10 PM, +0000 UTC — BIDMC Researchers Conduct First Real-World Study of Safety and Quality of Patient-Facing AI in Primary Care
    
    Link: https://bidmc.org/news-stories/all-news-stories/news/2026/10/bidmc-research-shows-safety-quality-of-ai-in-primary-care
  - (medical study) [Rutgers University] 10/08/2026, 07:07 PM, +0000 UTC — How a U.S. Ban on Lab-Modified Opioids Could Stifle Medical Research
    
    Link: https://www.rutgers.edu/news/how-us-ban-lab-modified-opioids-could-stifle-medical-research
  - (medical study) [The Harvard Crimson] 10/08/2026, 12:00 PM, +0000 UTC — Harvard Medical School Study Reveals How Cells Respond to Viral Infections
    
    Link: https://www.thecrimson.com/article/2026/10/8/harvard-medical-school-cells-study/
  - (medical study) [PBS] 10/04/2026, 09:00 PM, +0000 UTC — WATCH: 3 scientists win Nobel Prize in medicine for studying mysteries of the brain
    
    Link: https://www.pbs.org/newshour/health/watch-live-winner-of-the-2026-nobel-prize-in-medicine-is
  - (medical study) [Nature] 10/09/2026, 10:26 AM, +0000 UTC — AI-assisted scoping review of code sharing in clinical prediction model research
    
    Link: https://www.nature.com/articles/s41591-026-04691-1
  - (medical study) [University of Cincinnati] 10/09/2026, 10:59 PM, +0000 UTC — UC researcher to launch national study with $2.5 million NIH grant
    
    Link: https://www.uc.edu/news/articles/2026/10/uc-researcher-to-launch-national-study-with-25-million-nih-grant.html
  - (medical study) [The New York Times] 10/08/2026, 10:30 PM, +0000 UTC — Clinical Trial Indicates A.I. Chatbots Could Aid Urgent Care
    
    Link: https://www.nytimes.com/2026/10/08/technology/ai-chatbots-urgent-care.html
  - (medical study) [Pew Research Center] 10/07/2026, 01:48 PM, +0000 UTC — Which Health and Wellness Influencers Talk About Medical Topics? Mostly Healthcare Professionals
    
    Link: https://www.pewresearch.org/data-labs/2026/10/07/which-health-and-wellness-influencers-talk-about-medical-topics-mostly-healthcare-professionals/
  - (medical study) [Purdue University] 10/07/2026, 07:00 AM, +0000 UTC — Researchers in various studies looking for participants
    
    Link: https://www.purdue.edu/newsroom/purduetoday/2026/Q4/researchers-in-various-studies-looking-for-participants
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
  - (clinical trial health) [NBC News] 10/04/2026, 10:00 PM, +0000 UTC — In early clinical trial, people with Type 1 diabetes are able to go off insulin
    
    Link: https://www.nbcnews.com/health/health-news/early-clinical-trial-people-type-1-diabetes-are-able-go-insulin-rcna601171
  - (clinical trial health) [PR Newswire] 10/08/2026, 02:59 PM, +0000 UTC — Alpheus Medical Opens Enrollment in New Clinical Trial for Butterfly Glioblastoma
    
    Link: https://www.prnewswire.com/news-releases/alpheus-medical-opens-enrollment-in-new-clinical-trial-for-butterfly-glioblastoma-302902632.html
  - (clinical trial health) [Fierce Biotech] 10/07/2026, 03:25 PM, +0000 UTC — ARPA-H unveils Surpass program to accelerate and expand clinical trials
    
    Link: https://www.fiercebiotech.com/cro/arpa-h-unveils-surpass-program-accelerate-and-expand-clinical-trials
  - (clinical trial health) [Keck School of Medicine of USC] 10/07/2026, 02:34 PM, +0000 UTC — USC launches clinical trial of psilocybin and mindfulness meditation for depression
    
    Link: https://keck.usc.edu/news/usc-launches-clinical-trial-of-psilocybin-and-mindfulness-meditation-for-depression/
  - (clinical trial health) [Evanston RoundTable] 10/08/2026, 10:19 PM, +0000 UTC — Endeavor Health joins Chicago Breast Cancer Research Consortium
    
    Link: https://evanstonroundtable.com/2026/10/08/endeavor-health-joins-chicago-breast-cancer-research-consortium/
  - (clinical trial health) [www.apaservices.org] 10/06/2026, 07:00 AM, +0000 UTC — Urging a flexible National Institutes of Health funding framework for future clinical trial investigators
    
    Link: https://www.apaservices.org/advocacy/news/flexible-nih-funding-clinical-trial
  - (clinical trial health) [News-Medical] 10/06/2026, 01:55 PM, +0000 UTC — Mount Sinai adopts automated data integration for oncology clinical trials
    
    Link: https://www.news-medical.net/news/20261006/Mount-Sinai-adopts-automated-data-integration-for-oncology-clinical-trials.aspx
  - (FDA recall health) [U.S. Food and Drug Administration (.gov)] 10/05/2026, 12:00 AM, +0000 UTC — Outbreak Investigation of E. coli O145:H28: Frozen Blueberries (July 2026)
    
    Link: https://www.fda.gov/food/outbreaks-foodborne-illness/outbreak-investigation-e-coli-o145h28-frozen-blueberries-july-2026
  - (FDA recall health) [ABC7 New York] 10/05/2026, 10:05 PM, +0000 UTC — FDA recalls 122,000 cases of Gatorade sold across 37 states
    
    Link: https://abc7ny.com/story/fda-recalls-122000-cases-gatorade-undeclared-dyes/19910004/
  - (FDA recall health) [ABC News - Breaking News, Latest News and Videos] 10/06/2026, 03:02 AM, +0000 UTC — Over 122K cases of Gatorade recalled due to undeclared food dyes, FDA says
    
    Link: https://abcnews.com/GMA/Food/122k-cases-gatorade-recalled-due-undeclared-food-dyes/story?id=137002347
  - (FDA recall health) [Medscape] 10/06/2026, 01:29 PM, +0000 UTC — FDA Device Recall Problems Raise Questions About Patient Safety, Clinician Liability
    
    Link: https://www.medscape.com/viewarticle/fda-device-recall-problems-raise-questions-about-patient-2026a10011cz
  - (FDA recall health) [Health.com] 10/05/2026, 04:38 PM, +0000 UTC — FDA Announces Gatorade Recall in 37 States After Bottles Were Found to Have Undeclared Food Dyes
    
    Link: https://www.health.com/gatorade-recall-october-2026-12159566
  - (FDA recall health) [El Paso Times] 10/06/2026, 11:50 AM, +0000 UTC — FDA recalls Gatorade in Texas over unlisted food coloring
    
    Link: https://www.elpasotimes.com/story/news/texasregion/2026/10/06/gatorade-recall-in-texas-lot-numbers-products-health-risks/92106375007/
  - (FDA recall health) [Prevention] 10/08/2026, 02:56 PM, +0000 UTC — Millions of Bottles of Eye Drops Recalled Nationwide, FDA Warns
    
    Link: https://www.prevention.com/health/a74079654/fda-updates-eye-drop-recall/
  - (FDA recall health) [Montgomery Advertiser] 10/05/2026, 07:01 PM, +0000 UTC — Gatorade recall 2026 expands to Alabama. Check these bottles
    
    Link: https://www.montgomeryadvertiser.com/story/news/2026/10/05/fda-announces-major-gatorade-recall-2026-is-alabama-affected/92107184007/
  - (FDA recall health) [NEWStalk 870] 10/09/2026, 08:34 PM, +0000 UTC — Baby-Infant Sleep Aid Recalled by FDA Over Undisclosed Alcohol Content
    
    Link: https://newstalk870.am/fda-recalls-baby-infant-sleep-aid/
  - (FDA recall health) [WPLG Local 10] 10/09/2026, 08:16 PM, +0000 UTC — FDA: Gatorade recalls 122,000 cases over food dyes
    
    Link: https://www.local10.com/food/2026/10/09/fda-gatorade-recalls-122000-cases-over-food-dyes/
  - (FDA recall health) [Detroit Free Press] 10/06/2026, 05:55 PM, +0000 UTC — Gatorade sold in Michigan recalled. Why you should return it
    
    Link: https://www.freep.com/story/news/health/2026/10/06/gatorade-recall-michigan-fda-food-dye/92118542007/
  - (FDA recall health) [CBS News] 10/05/2026, 02:08 PM, +0000 UTC — PepsiCo recalls 122,000 cases of Gatorade due to undeclared dyes
    
    Link: https://www.cbsnews.com/news/gatorade-recall-undeclared-dyes-pepsico/