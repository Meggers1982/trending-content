# LIVE SIGNAL DATA — SerpAPI Pre-Fetch
The following signals were fetched from SerpAPI Google News and SerpAPI Google Trends immediately before this pipeline run. Treat Google Trends as AVAILABLE when this section contains a Google Trends block. Use it as the primary search_velocity input for Skills 01–05 (Signal Listener through Trend Strength Scorer). Use the Google News Radar as the broad discovery layer for news-led health topics, including topics that do not yet appear in Google Trends. Prioritize topics with convergence across News, Trends, primary/institutional sources, and credible publisher coverage.

## Google Trends — Trending Now (US / Health, real-time)
Terms with a "Why:" line have a confirmed real-world news story driving the spike; terms without one are a real-time signal only, not yet grounded in a specific story.
  - covid flu rsv vaccine recommendations
    Why: "A Guide to Covid, Flu and R.S.V. Vaccines This Fall" — The New York Times
  - kelly ripa
    Why: "Kelly Ripa’s Health Confession Reveals a Habit She Needs to Break" — Yahoo

## Google Trends — 7-Day Interest (US)
  - **health**: latest=86, peak=100, 7d-delta=+0
    Rising related: city of kansas city health department, how to check hard drive health, how to check ssd health, how to check laptop battery health, bachelors in health administration, how to improve gut health, battery health check iphone, phil collins health
  - **wellness**: latest=67, peak=100, 7d-delta=-9
    Rising related: circle wellness seattle, stc wellness city, little luxe wellness lodge, fsu health and wellness center, melaleuca the wellness company, greenheal.net wellness coach, hancock wellness center, wellness center
  - **nutrition**: latest=76, peak=100, 7d-delta=-10
    Rising related: burger king mcdonald's chicken sandwich nutrition, chipotle pollo asado nutrition, usda watermelon rind nutrition data, kona ice nutrition, vade nutrition, how to read nutrition labels, supplemental nutrition assistance program, pet nutrition calculator
  - **fitness**: latest=29, peak=100, 7d-delta=-9
    Rising related: world fitness project, fitness centre, physical fitness program, bungee fitness near me, planet fitness, la fitness, crunch fitness, crunch
  - **food safety**: latest=35, peak=100, 7d-delta=+0
    Rising related: walmart food safety recall mangoes, walmart product recalls safety notice, fda baxter international voluntary recall, cyclosporiasis outbreak iceberg lettuce safety, fda fresh cut produce safety guidance, when checking a foods temperature a food handler should monitor the thermometer until the reading, hiking safety tips, when using the fifo method correctly the food stored in the front should be the food that
  - **diet**: latest=70, peak=100, 7d-delta=-6
    Rising related: the diet that changed my life in four weeks, the diet that changed my life in four weeks i feel 10 years younger, the diet that changed my life, washu medicine keto mediterranean diet study, rose ferguson diet and lifestyle overhaul, is xylitol in diet coke, does diet coke have xylitol, diet coke lip smacker
  - **weight loss**: latest=32, peak=100, 7d-delta=-2
    Rising related: avatrade mt4, best smoothie recipes for weight loss, surfshark review, cider sale, weight loss service, etoro.com, shein download, kelly clarkson weight loss
  - **mental health**: latest=77, peak=100, 7d-delta=+0
    Rising related: is september mental health awareness month, september mental health month, how social media affects our mental health, suicide prevention month, lindsay clancy mental health history, mental health awareness month, when is mental health awareness month, mental health month
  - **gut health**: latest=45, peak=100, 7d-delta=+11
    Rising related: magnesium citrate, how to improve gut health, improve gut health, how to get better gut health, dog gut health chews, celtara gut health, best things for gut health, what is gut health

Top rising related queries from Google Trends:
  - city of kansas city health department
  - how to check hard drive health
  - how to check ssd health
  - how to check laptop battery health
  - bachelors in health administration
  - how to improve gut health
  - battery health check iphone
  - phil collins health
  - circle wellness seattle
  - stc wellness city
  - little luxe wellness lodge
  - fsu health and wellness center
  - melaleuca the wellness company
  - greenheal.net wellness coach
  - hancock wellness center
  - wellness center
  - burger king mcdonald's chicken sandwich nutrition
  - chipotle pollo asado nutrition
  - usda watermelon rind nutrition data
  - kona ice nutrition

## Google News Radar — Recent Health Topics (84 unique across 12 queries; showing 60)
Treat these headlines as the broad radar of news-led health topics. The Signal Listener must consider this radar before narrowing to retained candidates.
  - (health) [The New York Times] 09/02/2026, 10:00 AM, +0000 UTC — Employer Health Costs Are Expected to Spike in 2027
    
    Link: https://www.nytimes.com/2026/09/02/business/health-insurance-increases.html
  - (health) [Courthouse News] 09/02/2026, 10:19 PM, +0000 UTC — Arizona physicians unionize at Banner Health
    
    Link: https://www.courthousenews.com/arizona-physicians-unionize-at-banner-health
  - (health) [California Health Care Foundation] 09/02/2026, 05:09 PM, +0000 UTC — Policy Options to Improve Health Care Affordability: What California Can Learn from Other States
    
    Link: https://www.chcf.org/resource/2026/09/02/policy-options-to-improve-health-care-affordability-what-california-can-learn-from-other-states/
  - (health) [CIDRAP] 09/02/2026, 04:20 PM, +0000 UTC — Public Health Alerts: Cyclosporiasis outbreak in Michigan, May–July 2026—an interim report
    
    Link: https://www.cidrap.umn.edu/public-health-alerts/public-health-alerts-cyclosporiasis-outbreak-michigan-may-july-2026-interim
  - (health) [NYC.gov] 09/03/2026, 03:15 PM, +0000 UTC — NYC Health Department and Public Schools Remind Families to Get School-Age Children Vaccinated Ahead of 2026-27 School Year
    
    Link: https://www.nyc.gov/site/doh/about/press/pr2026/nyc-health-department-remind-school-children-vaccinated-2026-school-year.page
  - (health) [nbcsandiego.com] 09/02/2026, 06:00 AM, +0000 UTC — Mosque shooter's parents sue mental health organization after Islamic Center killings
    
    Link: https://www.nbcsandiego.com/news/local/mosque-shooters-parents-sue-mental-health-organization-after-san-diego-islamic-center-killings/4068413/
  - (health) [House.gov] 09/01/2026, 04:41 PM, +0000 UTC — Kean Introduces Bipartisan Legislation to Expand Access to Veteran Mental Health Services
    
    Link: http://kean.house.gov/media/press-releases/kean-introduces-bipartisan-legislation-expand-access-veteran-mental-health
  - (health) [University of Massachusetts Athletics] 09/01/2026, 07:00 AM, +0000 UTC — UMass Athletics Expands Partnership with Baystate Health
    
    Link: https://umassathletics.com/news/2026/9/1/football-umass-athletics-expands-partnership-with-baystate-health
  - (health) [Politico] 09/02/2026, 06:22 PM, +0000 UTC — House committee subpoenas Oracle’s Ellison about costly veterans health records project
    
    Link: https://www.politico.com/news/2026/09/02/ellison-subpoena-veterans-health-records-01062124
  - (health) [Gonzaga University] 09/02/2026, 08:12 PM, +0000 UTC — How UW-GU Student Research is Transforming Regional Health
    
    Link: https://www.gonzaga.edu/news-events/stories/how-uw-gu-student-research-is-transforming-regional-health
  - (health) [Centers for Disease Control and Prevention | CDC (.gov)] 09/01/2026, 10:27 PM, +0000 UTC — Interim Clinical Considerations for the Use of Seasonal Influenza Vaccines in the United States
    
    Link: https://www.cdc.gov/flu/hcp/vax-summary/seasonal-influenza-vaccines.html
  - (health) [American Medical Association | AMA] 08/31/2026, 12:06 PM, +0000 UTC — Family ties bring 2 generations of physicians together
    
    Link: https://www.ama-assn.org/public-health/prevention-wellness/family-ties-bring-2-generations-physicians-together
  - (wellness) [Nashville Guru] 08/30/2026, 07:00 AM, +0000 UTC — Floating Meditation at R+R Wellness
    
    Link: https://nashvilleguru.com/195709/floating-meditation-at-rr-wellness
  - (wellness) [IN.gov] 09/02/2026, 11:37 PM, +0000 UTC — Invest in Your Health (State Employee Wellness Program): Optum EAP - Suicide prevention and recovery
    
    Link: https://www.in.gov/investinyourhealth/post/optum-eap-suicide-prevention-and-recovery?page=4
  - (wellness) [army.mil] 08/27/2026, 03:38 PM, +0000 UTC — Post ‘Defends Wellness’ at event
    
    Link: https://www.army.mil/article/294919
  - (wellness) [CVS Health] 09/01/2026, 02:17 PM, +0000 UTC — LOVB announces CVS Pharmacy as an Official Health & Wellness Partner
    
    Link: https://www.cvshealth.com/news/community/lovb-announces-cvs-pharmacy-as-an-official-health-wellness-partner.html
  - (wellness) [Miami University RedHawks] 08/28/2026, 06:25 PM, +0000 UTC — Human Performance and Wellness Promotes Czabala, Welcomes Artus
    
    Link: https://miamiredhawks.com/news/2026/8/28/general-human-performance-and-wellness-promotes-czabala-welcomes-artus
  - (wellness) [Ferris State University] 09/01/2026, 09:50 PM, +0000 UTC — Room to breathe: Ferris State expands student wellness resources at its Grand Rapids campus
    
    Link: https://www.ferris.edu/news/archive/2026/room-to-breathe-ferris-state-expands-student-wellness-resources-at-grand-rapids-campus.htm
  - (wellness) [Hackensack Meridian Health] 09/01/2026, 03:32 PM, +0000 UTC — New Hackensack Meridian Health & Wellness Center at Freehold Brings Together Primary and Specialty Care
    
    Link: https://hackensackmeridianhealth.org/en/news/2026/09/01/new-hackensack-meridian-health-wellness-center-at-freehold
  - (wellness) [Azusa Pacific University] 09/01/2026, 08:10 AM, +0000 UTC — APU Receives $312,500 Grant to Train Certified Wellness Coaches to Help Youth
    
    Link: https://www.apu.edu/media/news/release/apu-receives-312500-grant-to-train-certified-wellness-coaches/
  - (wellness) [CSUF News] 08/28/2026, 05:00 PM, +0000 UTC — Total Wellness to Host 2026 Health and Wellness Expo
    
    Link: https://news.fullerton.edu/spotlight/total-wellness-to-host-2026-health-and-wellness-expo/
  - (wellness) [Middlesex Borough (.gov)] 08/28/2026, 04:48 PM, +0000 UTC — Senior Wellness Event
    
    Link: https://www.middlesexboro-nj.gov/latest-news/senior-wellness-event
  - (wellness) [Norwegian Cruise Line Holdings Ltd.] 09/02/2026, 08:23 PM, +0000 UTC — Regent Seven Seas Cruises® Unveils Largest-Ever Spa and Wellness Experience Aboard Seven Seas Prestige
    
    Link: https://www.nclhltd.com/news-media/press-releases/detail/820/regent-seven-seas-cruises-unveils-largest-ever-spa-and
  - (wellness) [Meijer Newsroom] 08/31/2026, 04:20 PM, +0000 UTC — Meijer Puts Wellness Within Reach at In-Store Events
    
    Link: https://newsroom.meijer.com/2026-08-31-Meijer-Puts-Wellness-Within-Reach-at-In-Store-Events
  - (clinical trial health) [Jefferson City News Tribune] 09/01/2026, 09:00 AM, +0000 UTC — Joining a clinical trial, hurdles to know about
    
    Link: https://www.newstribune.com/news/2026/sep/01/joining-a-clinical-trial-hurdles-to-know-about/
  - (clinical trial health) [biopharmaapac.com] 08/31/2026, 06:49 PM, +0000 UTC — Data4Life, Monash Health Partner to Accelerate Clinical Trials and Real-World Evidence Generation
    
    Link: https://biopharmaapac.com/news/81/8375/data4life-monash-health-partner-to-accelerate-clinical-trials-and-real-world-evidence-generation.html
  - (clinical trial health) [Clinical Leader] 08/28/2026, 04:09 AM, +0000 UTC — The Pharmacy Benefit No One Is Managing: Clinical Research As A Care Option
    
    Link: https://www.clinicalleader.com/doc/the-pharmacy-benefit-no-one-is-managing-clinical-research-as-a-care-option-0001
  - (clinical trial health) [OpenAI] 09/01/2026, 05:02 PM, +0000 UTC — Healthcare organizations can now connect EHR and additional industry data to ChatGPT
    
    Link: https://openai.com/index/chatgpt-connects-health-records-and-healthcare-sources/
  - (clinical trial health) [OHSU News] 08/28/2026, 02:23 PM, +0000 UTC — Clinical trial tests new way to treat common inherited heart disease
    
    Link: https://news.ohsu.edu/2026/08/28/clinical-trial-tests-new-way-to-treat-common-inherited-heart-disease
  - (clinical trial health) [The Pennsylvania State University] 09/01/2026, 01:45 PM, +0000 UTC — NIH awards Penn State CTSI $28.2M to improve rural health
    
    Link: https://www.psu.edu/news/clinical-and-translational-science-institute/story/nih-awards-penn-state-ctsi-282m-improve-rural
  - (clinical trial health) [European Medicines Agency (EMA)] 09/02/2026, 08:30 AM, +0000 UTC — Women's health
    
    Link: https://www.ema.europa.eu/en/human-regulatory-overview/research-development/womens-health
  - (clinical trial health) [Medical Xpress] 09/02/2026, 12:20 PM, +0000 UTC — First human clinical trial to test precision form of FLASH proton therapy
    
    Link: https://medicalxpress.com/news/2026-09-human-clinical-trial-precision-proton.html
  - (clinical trial health) [GlobeNewswire] 09/03/2026, 02:11 PM, +0000 UTC — Decentralized Clinical Trial Technology Platform Market to
    
    Link: https://www.globenewswire.com/news-release/2026/09/03/3356067/28124/en/decentralized-clinical-trial-technology-platform-market-to-reach-6-12-billion-by-2030-as-virtual-research-adoption-accelerates.html
  - (clinical trial health) [Business Wire] 09/02/2026, 09:02 PM, +0000 UTC — Segal Trials Kicks Off CISCRP’s 8th Annual Medical Heroes Appreci-A-Thon
    
    Link: https://www.businesswire.com/news/home/20260902685114/en/Segal-Trials-Kicks-Off-CISCRPs-8th-Annual-Medical-Heroes-Appreci-A-Thon
  - (clinical trial health) [Newswise] 09/02/2026, 04:10 PM, +0000 UTC — nference and Rush University System for Health Launch Long-Term Partnership to Advance AI-Enabled Clinical Research and Patient Care | Newswise
    
    Link: https://www.newswise.com/articles/nference-and-rush-university-system-for-health-launch-long-term-partnership-to-advance-ai-enabled-clinical-research-and-patient-care/?ad2f=1&aid=854061
  - (clinical trial health) [fortunebusinessinsights.com] 08/28/2026, 07:00 AM, +0000 UTC — Contract Research Organization (CRO) Services Market Trends
    
    Link: https://www.fortunebusinessinsights.com/industry-reports/contract-research-organization-cro-services-market-100864
  - (FDA recall health) [fda.gov] 08/28/2026, 12:00 AM, +0000 UTC — Early Alert: Angiographic Catheter Issue from Boston Scientific
    
    Link: https://www.fda.gov/medical-devices/medical-device-recalls-and-early-alerts/early-alert-angiographic-catheter-issue-boston-scientific
  - (FDA recall health) [American Hospital Association] 08/28/2026, 09:16 PM, +0000 UTC — FDA issues recall, alerts for certain convenience kits; companies voluntarily recall certain IV fluids
    
    Link: https://www.aha.org/news/headline/2026-08-28-fda-issues-recall-alerts-certain-convenience-kits-companies-voluntarily-recall-certain-iv-fluids
  - (FDA recall health) [The New Republic] 08/31/2026, 09:02 PM, +0000 UTC — You’re Not Hallucinating: The Amount of Recalled Food Is Skyrocketing
    
    Link: https://newrepublic.com/post/214946/food-recall-fda-list-august-skyrocket
  - (FDA recall health) [Fortune] 09/02/2026, 05:41 PM, +0000 UTC — American shoppers are so rattled by surging FDA recalls that 67% now avoid a whole food category after just one notice
    
    Link: https://fortune.com/2026/09/02/food-recalls-fda-americans-avoid-food-categories/
  - (FDA recall health) [health.com] 08/31/2026, 02:24 PM, +0000 UTC — FDA Announces Tofu Recall: More Than 10,000 Cases May Be Contaminated With Ink
    
    Link: https://www.health.com/tofu-recall-august-2026-12073618
  - (FDA recall health) [Star Tribune] 08/31/2026, 06:01 PM, +0000 UTC — Medtronic recall prompts FDA safety alert after 184 serious injuries
    
    Link: https://www.startribune.com/medtronic-recall-bravo-cf-reflux-gastroesophageal/601883787
  - (FDA recall health) [WGN-TV] 08/31/2026, 03:16 AM, +0000 UTC — 2 drugs recalled over potential fiberglass, steel presence
    
    Link: https://wgntv.com/news/medical-watch/2-drugs-recalled-over-potential-fiberglass-steel-presence/
  - (FDA recall health) [Powder & Bulk Solids] 09/02/2026, 10:25 PM, +0000 UTC — 34 FDA Food Recalls Issued in August
    
    Link: https://www.powderbulksolids.com/product-recalls/fda-recall-update-august
  - (FDA recall health) [Stateline] 08/31/2026, 09:08 AM, +0000 UTC — A summer of recalls exposes holes in the nation’s food safety net
    
    Link: https://stateline.org/2026/08/31/a-summer-of-recalls-exposes-holes-in-the-nations-food-safety-net/
  - (FDA recall health) [WSB-TV] 08/28/2026, 05:30 PM, +0000 UTC — FDA: Recalled lettuce should not be available after best-by date passes
    
    Link: https://www.wsbtv.com/news/trending/fda-said-recalled-lettuce-should-not-be-available-after-best-by-date-passes/Z2L7IAGLGZCCDM5RCZNS2SP4G4/
  - (FDA recall health) [medshadow.org] 08/31/2026, 07:44 PM, +0000 UTC — FDA Recalls and Warnings: Black Spots Found on Seizure Med; Alcohol Dependence Drug May Not Dissolve Properly
    
    Link: https://medshadow.org/drug-updates-recalls/fda-recalls-and-warnings/carbamazepine-acamprosate-fda-recall/
  - (FDA recall health) [Yahoo Health] 08/28/2026, 10:14 AM, +0000 UTC — Why Does It Feel Like There’s a New Food Recall Every Day? The Truth, According to Food Safety Experts
    
    Link: https://health.yahoo.com/conditions/infectious/food-poisoning/articles/why-feels-food-recalls-everywhere-101400133.html
  - (mental health) [HHS.gov] 08/31/2026, 09:03 PM, +0000 UTC — HHS Awards $77 Million to Strengthen Substance Use Prevention, Treatment, Crisis Services, and Mental Health Services
    
    Link: https://www.hhs.gov/press-room/samhsa-awards-77-million-substance-use-mental-health-suicide-prevention.html
  - (mental health) [NPR] 08/31/2026, 08:45 PM, +0000 UTC — What does the Lindsay Clancy trial tell us about treating maternal mental health?
    
    Link: https://www.npr.org/2026/08/31/nx-s1-5950315/what-does-the-lindsay-clancy-trial-tell-us-about-treating-maternal-mental-health
  - (mental health) [ABC7 New York] 09/02/2026, 03:21 AM, +0000 UTC — Times Square stabbing: Father of Times Square stabbing suspect speaks out after shot was shot by police
    
    Link: https://abc7ny.com/post/times-square-stabbing-father-suspect-speaks-shot-was-police/19777632/
  - (mental health) [The New York Times] 09/02/2026, 01:38 PM, +0000 UTC — Lindsay Clancy’s Trial Prompts Patients and Doctors to Rethink Postpartum Care
    
    Link: https://www.nytimes.com/2026/09/02/well/doctors-patients-postpartum-mental-health-clancy-trial.html
  - (mental health) [northcarolinahealthnews.org] 09/01/2026, 08:30 AM, +0000 UTC — How a federal grant brought mental health services into schools across 6 North Carolina school districts
    
    Link: https://www.northcarolinahealthnews.org/2026/09/01/mental-health-in-schools-federal-grant-nc/
  - (mental health) [news.va.gov] 08/31/2026, 07:00 AM, +0000 UTC — Support your mental health, one app at a time
    
    Link: https://news.va.gov/149188/support-your-mental-health-one-app-time/
  - (mental health) [FOX 5 DC] 09/01/2026, 10:43 PM, +0000 UTC — Another accused killer released from Virginia mental health facility after insanity plea
    
    Link: https://www.fox5dc.com/news/another-accused-killer-released-from-virginia-mental-health-facility-after-insanity-plea
  - (mental health) [West Virginia University] 09/02/2026, 12:03 PM, +0000 UTC — E-News | Carruth Center offering Mental Health 101 training
    
    Link: https://enews.wvu.edu/articles/2026/09/02/carruth-center-offering-mental-health-101-training
  - (mental health) [BBC] 09/02/2026, 12:21 PM, +0000 UTC — Children as young as six going to A&E in mental health crisis
    
    Link: https://www.bbc.com/news/articles/cn5d2r0zqvdo
  - (mental health) [Mississippi Today] 08/28/2026, 05:30 PM, +0000 UTC — Mississippi’s rural mental health crisis needs immediate action, social worker says
    
    Link: https://mississippitoday.org/2026/08/28/rural-mental-health-crisis-mississipp/
  - (mental health) [lvhn.org] 09/01/2026, 07:15 PM, +0000 UTC — How to Access Mental Health Services
    
    Link: https://www.lvhn.org/news/how-access-lvhn-mental-health-services
  - (mental health) [NBC New York] 09/01/2026, 12:11 PM, +0000 UTC — Times Square stabber had mental health history with police before deadly attack
    
    Link: https://www.nbcnewyork.com/manhattan/times-square-stabber-had-mental-health-history-with-police-before-deadly-attack/6542566/