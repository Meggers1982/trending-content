# LIVE SIGNAL DATA — SerpAPI Pre-Fetch
The following signals were fetched from SerpAPI Google News and SerpAPI Google Trends immediately before this pipeline run. Treat Google Trends as AVAILABLE when this section contains a Google Trends block. Use it as the primary search_velocity input for Skills 01–05 (Signal Listener through Trend Strength Scorer). Use the Google News Radar as the broad discovery layer for news-led health topics, including topics that do not yet appear in Google Trends. Prioritize topics with convergence across News, Trends, primary/institutional sources, and credible publisher coverage.

## Google Trends — Trending Now (US / Health, real-time)
Terms with a "Why:" line have a confirmed real-world news story driving the spike; terms without one are a real-time signal only, not yet grounded in a specific story.
  - erin andrews
    Why: "Erin Andrews, 48, is determined to welcome second baby after infertility struggles: ‘I’m not done’" — PennLive.com

## Google Trends — 7-Day Interest (US)
  - **health**: latest=94, peak=100, 7d-delta=+1
    Rising related: tim curry health, tim curry health issues, city of kansas city health department, willie nelson health, phil collins health, how to check hard drive health, how to check ssd health, how to check laptop battery health
  - **wellness**: latest=78, peak=100, 7d-delta=+2
    Rising related: little luxe wellness lodge, stc wellness city, beeya wellness, circle wellness seattle, unh health and wellness, msu student recreation and wellness center, wutawhealth wellness advice from whatutalkingboutwillis, fsu health and wellness center
  - **nutrition**: latest=91, peak=100, 7d-delta=+1
    Rising related: usda watermelon rind nutrition data, burger king mcdonald's chicken sandwich nutrition, kona ice nutrition, how to read nutrition labels, supplemental nutrition assistance program, pet nutrition calculator, optimum nutrition serious mass, burger king nutrition
  - **fitness**: latest=34, peak=100, 7d-delta=-3
    Rising related: world fitness project, physical fitness program, fitness centre, planet fitness, la fitness, crunch, crunch fitness, fitness near me
  - **food safety**: latest=56, peak=100, 7d-delta=+20
    Rising related: walmart food safety recall mangoes, 123 premier food safety, what does fattom stand for in food safety, national food safety education month, king county food safety rating, national food safety month, food safety month, center for food safety
  - **diet**: latest=84, peak=100, 7d-delta=+8
    Rising related: the diet that changed my life in four weeks, the diet that changed my life in four weeks i feel 10 years younger, washu medicine keto mediterranean diet study, rose ferguson diet and lifestyle overhaul, what is a detox diet, ketogenic diet, diet coke, mediterranean diet
  - **weight loss**: latest=35, peak=100, 7d-delta=+5
    Rising related: surfshark review, best smoothie recipes for weight loss, medvi tirzepatide cost, medvi quad reviews, em tirzepatide, quad mix for ed, quad ed, medvi.org
  - **mental health**: latest=95, peak=100, 7d-delta=+9
    Rising related: yayoi kusama mental health, is september mental health awareness month, september mental health month, kyle singler mental health, suicide awareness month, lindsay clancy mental health history, suicide prevention month, when is mental health awareness month
  - **gut health**: latest=39, peak=100, 7d-delta=-7
    Rising related: how to improve gut health, celtara gut health, improve gut health, dog gut health chews, is cottage cheese good for gut health, what is gut health, gut health foods, gut health probiotics

Top rising related queries from Google Trends:
  - tim curry health
  - tim curry health issues
  - city of kansas city health department
  - willie nelson health
  - phil collins health
  - how to check hard drive health
  - how to check ssd health
  - how to check laptop battery health
  - little luxe wellness lodge
  - stc wellness city
  - beeya wellness
  - circle wellness seattle
  - unh health and wellness
  - msu student recreation and wellness center
  - wutawhealth wellness advice from whatutalkingboutwillis
  - fsu health and wellness center
  - usda watermelon rind nutrition data
  - burger king mcdonald's chicken sandwich nutrition
  - kona ice nutrition
  - how to read nutrition labels

## Google News Radar — Recent Health Topics (144 unique across 12 queries; showing 60)
Treat these headlines as the broad radar of news-led health topics. The Signal Listener must consider this radar before narrowing to retained candidates.
  - (health) [OpenAI] 09/01/2026, 05:02 PM, +0000 UTC — Healthcare organizations can now connect EHR and additional industry data to ChatGPT
    
    Link: https://openai.com/index/chatgpt-connects-health-records-and-healthcare-sources/
  - (health) [Centers for Disease Control and Prevention | CDC (.gov)] 08/30/2026, 07:00 AM, +0000 UTC — Measles Cases and Outbreaks
    
    Link: https://www.cdc.gov/measles/data-research/index.html
  - (health) [The New York Times] 09/02/2026, 10:00 AM, +0000 UTC — Employer Health Costs Are Expected to Spike in 2027
    
    Link: https://www.nytimes.com/2026/09/02/business/health-insurance-increases.html
  - (health) [news.vumc.org] 08/26/2026, 05:07 PM, +0000 UTC — Vanderbilt Health mourns passing of global icon Dolly Parton
    
    Link: https://news.vumc.org/2026/08/26/vanderbilt-health-mourns-passing-of-global-icon-dolly-parton/
  - (health) [Healthcare Dive] 08/26/2026, 08:06 PM, +0000 UTC — Sword Health to acquire Headspace
    
    Link: https://www.healthcaredive.com/news/sword-health-to-acquire-headspace/828873/
  - (health) [Corewell Health Newsroom] 08/27/2026, 01:15 PM, +0000 UTC — Corewell Health Announces $1.7 Billion Investment to Build Stronger Healthcare for Michigan
    
    Link: https://newsroom.corewellhealth.org/news-releases?item=125230
  - (health) [World Health Organization (WHO)] 08/31/2026, 12:40 PM, +0000 UTC — World Mental Health Day webinar
    
    Link: https://www.who.int/news-room/events/detail/2026/10/09/default-calendar/world-mental-health-day-webinar
  - (health) [washingtonpost.com] 08/28/2026, 05:00 PM, +0000 UTC — Calcium testing for heart health may have limited value for many, study finds
    
    Link: https://www.washingtonpost.com/wellness/2026/08/28/calcium-testing-heart-health-may-have-limited-value-many-new-study-suggests/
  - (health) [UVA Health] 09/01/2026, 04:19 PM, +0000 UTC — UVA Health Bringing Comprehensive Cancer Care to Lynchburg
    
    Link: https://www.uvahealth.com/news/uva-health-bringing-comprehensive-cancer-care-lynchburg
  - (health) [KFF Health News] 08/27/2026, 09:04 AM, +0000 UTC — $50B Rural Health Transformation Program Needs More Transparency, Groups Say
    
    Link: https://kffhealthnews.org/rural-health/rural-health-transformation-program-transparency-50-billion-dollars-state-tracking/
  - (health) [Sanford Health News] 09/01/2026, 01:37 PM, +0000 UTC — Sanford Health, North Memorial Health complete partnership
    
    Link: https://news.sanfordhealth.org/news/sanford-health-north-memorial-health-complete-partnership/
  - (health) [Florida Department of Health in Miami-Dade County (.gov)] 08/31/2026, 11:48 AM, +0000 UTC — DOH-Miami-Dade Issues Water Quality Health Advisory
    
    Link: https://miamidade.floridahealth.gov/2026/08/31/doh-miami-dade-issues-water-quality-health-advisory-9/
  - (wellness) [VA News (.gov)] 08/28/2026, 07:00 AM, +0000 UTC — Five organizations with Veterans wellness at the heart of their mission
    
    Link: https://news.va.gov/149155/organizations-veterans-wellness-heart-mission/
  - (wellness) [army.mil] 08/27/2026, 03:38 PM, +0000 UTC — Post ‘Defends Wellness’ at event
    
    Link: https://www.army.mil/article/294919
  - (wellness) [Boston Consulting Group] 09/01/2026, 07:48 AM, +0000 UTC — As Wellness Spending Grows, Can Activewear Brands Seize the Opportunity?
    
    Link: https://www.bcg.com/publications/2026/activewear-brands-wellness-growth
  - (wellness) [CVS Health] 09/01/2026, 02:17 PM, +0000 UTC — LOVB announces CVS Pharmacy as an Official Health & Wellness Partner
    
    Link: https://www.cvshealth.com/news/community/lovb-announces-cvs-pharmacy-as-an-official-health-wellness-partner.html
  - (wellness) [Miami University RedHawks] 08/28/2026, 06:25 PM, +0000 UTC — Human Performance and Wellness Promotes Czabala, Welcomes Artus
    
    Link: https://miamiredhawks.com/news/2026/8/28/general-human-performance-and-wellness-promotes-czabala-welcomes-artus
  - (wellness) [Azusa Pacific University] 09/01/2026, 08:10 AM, +0000 UTC — APU Receives $312,500 Grant to Train Certified Wellness Coaches to Help Youth
    
    Link: https://www.apu.edu/media/news/release/apu-receives-312500-grant-to-train-certified-wellness-coaches/
  - (wellness) [Grocery Dive] 08/31/2026, 04:06 PM, +0000 UTC — Kroger amplifies wellness focus with in-store events and ‘mini-fests’
    
    Link: https://www.grocerydive.com/news/kroger-wellness-tour-store-events-festivals/829161/
  - (wellness) [Human Resources University of Michigan |] 08/31/2026, 10:11 PM, +0000 UTC — Invest In Your Mental Wellness
    
    Link: https://hr.umich.edu/about-uhr/uhr-news/invest-your-mental-wellness
  - (wellness) [PR Newswire] 08/28/2026, 06:00 PM, +0000 UTC — National Release: Kroger Is Improving Wellness in Neighborhoods Across America
    
    Link: https://www.prnewswire.com/news-releases/national-release-kroger-is-improving-wellness-in-neighborhoods-across-america-302862767.html
  - (wellness) [CSUF News] 08/28/2026, 05:00 PM, +0000 UTC — Total Wellness to Host 2026 Health and Wellness Expo
    
    Link: https://news.fullerton.edu/spotlight/total-wellness-to-host-2026-health-and-wellness-expo/
  - (wellness) [Middlesex Borough (.gov)] 08/28/2026, 04:48 PM, +0000 UTC — Senior Wellness Event
    
    Link: https://www.middlesexboro-nj.gov/latest-news/senior-wellness-event
  - (wellness) [WVIR] 08/31/2026, 08:36 PM, +0000 UTC — Heart 2 Heart Wellness holds first annual wellness festival
    
    Link: https://www.29news.com/2026/08/31/heart-2-heart-wellness-holds-first-annual-wellness-festival/
  - (medical study) [KUOW] 08/26/2026, 06:38 PM, +0000 UTC — UW struggles to see medical research through as Trump administration guts funding
    
    Link: https://www.kuow.org/science/2026-08-26/uw-struggles-to-see-medical-research-through-as-trump-administration-guts-funding
  - (medical study) [University of Chicago News] 08/28/2026, 05:00 PM, +0000 UTC — Health care spending gap between high- and low-income Americans widens, study finds
    
    Link: https://news.uchicago.edu/story/health-care-spending-gap-between-high-and-low-income-americans-widens-study-finds
  - (medical study) [Augusta University] 08/31/2026, 05:41 PM, +0000 UTC — AU hosts House Blue-Ribbon Study Committee focusing on healthcare
    
    Link: https://jagwire.augusta.edu/au-hosts-house-blue-ribbon-study-committee-focusing-on-healthcare/
  - (medical study) [Fresenius Medical Care] 08/27/2026, 07:01 AM, +0000 UTC — Fresenius Medical Care Announces Publication of a Multinational Real-World Evidence Study Associating High-Volume Hemodiafiltration with Lower Mortality Risk Than Conventional Hemodialysis
    
    Link: https://freseniusmedicalcare.com/en/media/newsroom/multinational-real-world-evidence-study-associating-high-volume-hemodiafiltration-with-lower-mortality-risk-than-conventional-hemodialysis/
  - (medical study) [Penn Medicine] 09/01/2026, 12:49 PM, +0000 UTC — Penn launches first advanced proton therapy clinical trial
    
    Link: https://www.pennmedicine.org/news/penn-launches-first-advanced-proton-therapy-clinical-trial
  - (medical study) [Medical Xpress] 08/31/2026, 11:00 PM, +0000 UTC — GLP-1s do not cause major psychiatric harm, according to new study
    
    Link: https://medicalxpress.com/news/2026-08-glp-1s-major-psychiatric.html
  - (medical study) [newsroom.ucla.edu] 08/27/2026, 03:18 PM, +0000 UTC — American Indians and Alaska Natives in California face barriers to receiving needed healthcare, UCLA study finds
    
    Link: https://newsroom.ucla.edu/releases/american-indians-alaska-natives-california-face-barriers-healthcare
  - (medical study) [WashU Medicine] 08/27/2026, 03:02 PM, +0000 UTC — Low-carb diet delivers added liver benefits beyond weight loss
    
    Link: https://medicine.washu.edu/news/low-carb-diet-delivers-added-liver-benefits-beyond-weight-loss/
  - (medical study) [University of Miami] 08/27/2026, 07:53 PM, +0000 UTC — FDA Approval Opens New Chapter in Pancreatic Cancer Treatment
    
    Link: https://news.med.miami.edu/fda-approves-daraxonrasib-pancreatic-cancer-treatment/
  - (medical study) [Georgia Public Broadcasting] 08/31/2026, 06:06 PM, +0000 UTC — States with legal medical marijuana saw fewer people missing work, according to a UGA study
    
    Link: https://www.gpb.org/news/2026/08/31/states-legal-medical-marijuana-saw-fewer-people-missing-work-according-uga-study
  - (medical study) [News-Medical] 08/28/2026, 02:32 AM, +0000 UTC — Study links later-life food insecurity to elevated dementia risk
    
    Link: https://www.news-medical.net/news/20260827/Study-links-later-life-food-insecurity-to-elevated-dementia-risk.aspx
  - (medical study) [University of Rochester] 08/31/2026, 09:25 AM, +0000 UTC — Hidden Immune Cells in the Lung Could Lead to Better Flu Vaccines
    
    Link: https://www.urmc.rochester.edu/news/story/hidden-immune-cells-in-the-lung-could-lead-to-better-flu-vaccines
  - (clinical trial health) [Inquirer.com] 08/26/2026, 06:08 PM, +0000 UTC — You want to join a clinical trial. Here's what to know about the hurdles.
    
    Link: https://www.inquirer.com/health/clinical-trial-how-to-join-what-to-know-20260826.html
  - (clinical trial health) [cancerhealth.com] 08/26/2026, 07:23 PM, +0000 UTC — Costs and Geographic Barriers Impact Cancer Clinical Trial Participation
    
    Link: https://www.cancerhealth.com/article/costs-geographic-barriers-impact-cancer-clinical-trial-participation
  - (clinical trial health) [CancerNetwork] 08/30/2026, 01:56 PM, +0000 UTC — How Can Health Networks Bring Clinical Trials Directly To Patients?
    
    Link: https://www.cancernetwork.com/shorts/how-can-health-networks-bring-clinical-trials-directly-to-patients-
  - (clinical trial health) [postbulletin.com] 08/29/2026, 11:48 AM, +0000 UTC — In Southeast Minnesota, clinical trial participation plays a key role in advancing science
    
    Link: https://www.postbulletin.com/health/in-southeast-minnesota-clinical-trial-participation-plays-a-key-role-in-advancing-science
  - (clinical trial health) [BioPharma APAC] 08/31/2026, 06:49 PM, +0000 UTC — Data4Life, Monash Health Partner to Accelerate Clinical Trials and Real-World Evidence Generation
    
    Link: https://biopharmaapac.com/news/81/8375/data4life-monash-health-partner-to-accelerate-clinical-trials-and-real-world-evidence-generation.html
  - (clinical trial health) [Clinical Leader] 08/28/2026, 04:09 AM, +0000 UTC — The Pharmacy Benefit No One Is Managing: Clinical Research As A Care Option
    
    Link: https://www.clinicalleader.com/doc/the-pharmacy-benefit-no-one-is-managing-clinical-research-as-a-care-option-0001
  - (clinical trial health) [the-scientist.com] 09/02/2026, 04:15 AM, +0000 UTC — Cancer Clinical Trials Are Excluding the Patients They Are Meant to Help
    
    Link: https://www.the-scientist.com/cancer-clinical-trials-are-excluding-the-patients-they-are-meant-to-help-74951
  - (clinical trial health) [ABC News - Breaking News, Latest News and Videos] 08/30/2026, 05:10 PM, +0000 UTC — Moderna begins Phase 1 clinical trial of Ebola vaccine against strain behind DRC outbreak
    
    Link: https://abcnews.com/Health/moderna-begins-phase-1-clinical-trial-ebola-vaccine/story?id=135365177
  - (clinical trial health) [The Pennsylvania State University] 09/01/2026, 01:45 PM, +0000 UTC — NIH awards Penn State CTSI $28.2M to improve rural health
    
    Link: https://www.psu.edu/news/clinical-and-translational-science-institute/story/nih-awards-penn-state-ctsi-282m-improve-rural
  - (clinical trial health) [ASU News] 08/31/2026, 09:48 PM, +0000 UTC — Barrow, ASU embark on one of first clinical trials of ibogaine in the US
    
    Link: https://news.asu.edu/20260831-health-and-medicine-barrow-asu-embark-one-first-clinical-trials-ibogaine-us
  - (clinical trial health) [The Clinical Trial Vanguard] 08/29/2026, 07:27 AM, +0000 UTC — Dubai’s rWGS Scale-Up Rewrites the Diagnostic Playbook — But the Data Infrastructure Problem Stays Unsolved
    
    Link: https://www.clinicaltrialvanguard.com/article/article-deep-dive/dubais-rwgs-scale-up-rewrites-the-diagnostic-playbook-but-the-data-infrastructure-problem-stays-unsolved/
  - (clinical trial health) [News-Medical] 08/29/2026, 02:54 AM, +0000 UTC — Digital technologies reshape clinical research and public health
    
    Link: https://www.news-medical.net/news/20260828/Digital-technologies-reshape-clinical-research-and-public-health.aspx
  - (FDA recall health) [fda.gov] 08/31/2026, 03:07 PM, +0000 UTC — Outbreak Investigation of Shiga Toxin-producing E. coli & Salmonella: Sprouts (August 2026)
    
    Link: https://www.fda.gov/food/outbreaks-foodborne-illness/outbreak-investigation-shiga-toxin-producing-e-coli-salmonella-sprouts-august-2026
  - (FDA recall health) [American Hospital Association] 08/28/2026, 09:16 PM, +0000 UTC — FDA issues recall, alerts for certain convenience kits; companies voluntarily recall certain IV fluids
    
    Link: https://www.aha.org/news/headline/2026-08-28-fda-issues-recall-alerts-certain-convenience-kits-companies-voluntarily-recall-certain-iv-fluids
  - (FDA recall health) [Healthline] 09/01/2026, 07:31 PM, +0000 UTC — FDA Recalls IV Fluids Due to Fiberglass, Other Hazardous Materials
    
    Link: https://www.healthline.com/health-news/fda-recalls-iv-saline-fluids-fiberglass-stainless-steel-contaminants
  - (FDA recall health) [CT Mirror] 08/31/2026, 01:00 PM, +0000 UTC — A summer of recalls exposes holes in the nation’s food safety net
    
    Link: https://ctmirror.org/2026/08/31/summer-of-recalls-us-food-safety-net/
  - (FDA recall health) [Centers for Disease Control and Prevention | CDC (.gov)] 08/27/2026, 07:00 AM, +0000 UTC — Cyclospora Outbreak Linked to Iceberg Lettuce | Cyclosporiasis
    
    Link: https://www.cdc.gov/cyclosporiasis/outbreaks/07-26/index.html
  - (FDA recall health) [Newsweek] 08/27/2026, 11:45 AM, +0000 UTC — Nut Butter Recall Update: FDA Issues Highest Risk Warning
    
    Link: https://www.newsweek.com/nut-butter-recall-update-fda-issues-highest-risk-warning-salmonella-walmart-botticelli-foods-12374520
  - (FDA recall health) [health.com] 08/31/2026, 02:24 PM, +0000 UTC — FDA Announces Tofu Recall: More Than 10,000 Cases May Be Contaminated With Ink
    
    Link: https://www.health.com/tofu-recall-august-2026-12073618
  - (FDA recall health) [Star Tribune] 08/31/2026, 06:01 PM, +0000 UTC — Medtronic recall prompts FDA safety alert after 184 serious injuries
    
    Link: https://www.startribune.com/medtronic-recall-bravo-cf-reflux-gastroesophageal/601883787
  - (FDA recall health) [KTALnews.com] 08/27/2026, 07:47 PM, +0000 UTC — FDA recalls popular IV bags over possible fiberglass contamination
    
    Link: https://www.ktalnews.com/health/baxter-sodium-chloride-recall/
  - (FDA recall health) [The Healthy @Reader's Digest] 09/01/2026, 07:55 PM, +0000 UTC — Olive Oil Recall: Bottles Contained Ingredient ‘Not Approved for Culinary Use,’ Says FDA
    
    Link: https://www.thehealthy.com/news/olive-oil-recall-august-2026/
  - (FDA recall health) [People.com] 08/29/2026, 07:12 PM, +0000 UTC — FDA Issues Update on White Rice Recalled in 13 States Due to Potential Contamination with Foreign Materials
    
    Link: https://people.com/fda-issues-update-lundberg-family-farms-white-rice-jasmine-recall-13-states-12072609
  - (FDA recall health) [newrepublic.com] 08/31/2026, 09:00 PM, +0000 UTC — You’re Not Hallucinating: The Amount of Recalled Food Is Skyrocketing
    
    Link: https://newrepublic.com/post/214946/food-recall-fda-list-august-skyrocket