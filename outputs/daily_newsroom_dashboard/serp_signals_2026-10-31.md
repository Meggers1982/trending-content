# LIVE SIGNAL DATA — SerpAPI Pre-Fetch
The following signals were fetched from SerpAPI Google News and SerpAPI Google Trends immediately before this pipeline run. Treat Google Trends as AVAILABLE when this section contains a Google Trends block. Use it as the primary search_velocity input for Skills 01–05 (Signal Listener through Trend Strength Scorer). Use the Google News Radar as the broad discovery layer for news-led health topics, including topics that do not yet appear in Google Trends. Prioritize topics with convergence across News, Trends, primary/institutional sources, and credible publisher coverage.

## Google Trends — Trending Now (US / Health, real-time)
Terms with a "Why:" line have a confirmed real-world news story driving the spike; terms without one are a real-time signal only, not yet grounded in a specific story.
  - richard norton peptides
    Why: "Richard Norton, actor and martial artist, died after peptides triggered heart attack, coroner says" — NBC News

## Google Trends — 7-Day Interest (US)
  - **health**: latest=39, peak=100, 7d-delta=-2
    Rising related: explain the daylight savings schedule, clock adjustment rules, and health effects, university rankings, health insurance agency, fairmount behavioral health system, connect for health colorado, career development, online learning, health insurance
  - **wellness**: latest=31, peak=100, 7d-delta=-6
    Rising related: why did the us ease access to unapproved wellness peptides and what are the safety concerns?, corporate wellness programs, the wellness company medical emergency kit, the wellness company emergency kit, sh wellness spa, employee wellness programs, aura points / aura slang, ai image enhancer
  - **nutrition**: latest=66, peak=100, 7d-delta=-11
    Rising related: supplemental nutrition assistance program state waivers, fda infant formula nutrition updates, sp nutrition magnesium bisglycinate gummies review, mcrib nutrition facts, skin nutrition botanicals, supplemental nutrition assistance program, pumpkin seed nutrition facts, pumpkin seed nutrition
  - **fitness**: latest=39, peak=100, 7d-delta=-12
    Rising related: la fitness shutting down gyms, planet fitness customer retention issues, fitness international ftc lawsuit, sharon stone daily fitness routine, fitness warrior nation, fitbit edge alternative fitness trackers, is planet fitness open on halloween, physical fitness program
  - **food safety**: latest=20, peak=100, 7d-delta=-1
    Rising related: aluminum foil leftover food safety, world food safety day date, mailing paper checks safety risks, abrasive cleaners cause friction which, walmart great value fruit cocktail recall, what are the most important food safety features to look for when selecting flooring, wall, and ceiling materials?, an emergency that disrupts the normal water supply may require the use of, what is a type of contaminant that can cause foodborne illness? chemical preservatives organic ingredients cholesterol parasites
  - **diet**: latest=74, peak=100, 7d-delta=-9
    Rising related: diet coke advent calendar, humanin shmoose mediterranean diet study, diet coke mini fridge, diet coke fridge, diet coke blanket, diet coke logo, diet coke, mediterranean
  - **weight loss**: latest=32, peak=100, 7d-delta=-9
    Rising related: eli lilly weight loss ads ruling, gracie abrams weight loss, eli lilly retatrutide weight loss results, glp-1 weight loss wardrobe changes, goodrx employer weight loss program, eli lilly weight loss sales, morgan nobody wants this, morgan nobody wants this weight loss
  - **mental health**: latest=33, peak=100, 7d-delta=-9
    Rising related: coinlaw.io, mental health in aviation act, companies history, anygamble.com, mental health women villakalima, at what rate does the liver process alcohol per hour? .016% .008% .032% .064%, teen mental health treatment malibu ca visionsteen.com, shelley duvall mental health
  - **gut health**: latest=47, peak=100, 7d-delta=-12
    Rising related: hack your health the secrets of your gut, true or bystander behavior can be defined as seeing a problem and then taking appropriate action. true false, at what rate does the liver process alcohol per hour? .016% .008% .032% .064%, zoe gut health bar, signs of poor gut health, best for gut health, what is gut health, gut health foods

Top rising related queries from Google Trends:
  - explain the daylight savings schedule, clock adjustment rules, and health effects
  - university rankings
  - health insurance agency
  - fairmount behavioral health system
  - connect for health colorado
  - career development
  - online learning
  - health insurance
  - why did the us ease access to unapproved wellness peptides and what are the safety concerns?
  - corporate wellness programs
  - the wellness company medical emergency kit
  - the wellness company emergency kit
  - sh wellness spa
  - employee wellness programs
  - aura points / aura slang
  - ai image enhancer
  - supplemental nutrition assistance program state waivers
  - fda infant formula nutrition updates
  - sp nutrition magnesium bisglycinate gummies review
  - mcrib nutrition facts

## Google News Radar — Recent Health Topics (144 unique across 12 queries; showing 60)
Treat these headlines as the broad radar of news-led health topics. The Signal Listener must consider this radar before narrowing to retained candidates.
  - (health) [CBS News] 10/25/2026, 10:08 PM, +0000 UTC — MedStar Health expert warns parents about illnesses affecting teens and college students
    
    Link: https://www.cbsnews.com/baltimore/news/medstar-health-expert-warns-parents-illnesses-affecting-teens-and-college-students/
  - (health) [County of San Luis Obispo (.gov)] 10/27/2026, 11:21 PM, +0000 UTC — Public Health Confirms Five Shiga toxin-producing E. Coli Cases; Local Farm Suspected as Potential S
    
    Link: https://www.slocounty.ca.gov/departments/slo-health/public-health/department-news/public-health-confirms-five-shiga-toxin-producing-e-coli-cases;-local-farm-suspected-as-potential-s
  - (health) [Centers for Disease Control and Prevention | CDC (.gov)] 10/28/2026, 07:00 AM, +0000 UTC — Interim Guidance for Public Health Assessment and Management of Travelers from Countries Affected by the 2026 Ebola Outbreak
    
    Link: https://www.cdc.gov/ebola/php/emergency-guidance/index.html
  - (health) [KFF] 10/28/2026, 07:00 AM, +0000 UTC — Explaining Health Care Reform: Questions About Health Insurance Subsidies
    
    Link: https://www.kff.org/affordable-care-act/explaining-health-care-reform-questions-about-health-insurance-subsidies/
  - (health) [UNESCO] 10/26/2026, 07:00 AM, +0000 UTC — Safe learning environments: Preventing and addressing violence in and around school
    
    Link: https://www.unesco.org/en/health-education/safe-learning-environments
  - (health) [Florida State University News] 10/30/2026, 09:41 PM, +0000 UTC — FSU Health opens new research and collaboration building, names it for Florida Ag Commissioner Wilton Simpson
    
    Link: https://news.fsu.edu/news/university-news/2026/10/30/fsu-health-opens-new-research-and-collaboration-building-names-it-for-florida-ag-commissioner-wilton-simpson/
  - (health) [Department of Land and Natural Resources (.gov)] 10/31/2026, 04:07 AM, +0000 UTC — 10/30/26 – HEALTH AND SAFETY RISKS FOR KONA COAST AFTER SPERM WHALE CARCASS TOWED FROM HONOKŌHAU HARBOR
    
    Link: https://dlnr.hawaii.gov/blog/2026/10/30/nr26-134/
  - (health) [CalMatters] 10/30/2026, 12:18 AM, +0000 UTC — Fact check: Did Trump invest more money in rural California health ahead of the election?
    
    Link: https://calmatters.org/health/2026/10/trump-california-rural-health-fact-check/
  - (health) [UVA Health] 10/30/2026, 06:57 PM, +0000 UTC — UVA Health Acquires State Farm Site on Pantops
    
    Link: https://www.uvahealth.com/news/uva-health-acquires-state-farm-site-on-pantops
  - (health) [The Washington Post] 10/25/2026, 04:00 PM, +0000 UTC — 3 mental health habits that may help with your blood pressure
    
    Link: https://www.washingtonpost.com/wellness/2026/10/25/3-mental-health-habits-that-may-help-with-your-blood-pressure/
  - (health) [Reuters] 10/30/2026, 09:17 PM, +0000 UTC — US health department to remove broad black box warning from three estrogen patch products
    
    Link: https://www.reuters.com/legal/litigation/us-health-department-remove-broad-black-box-warning-three-estrogen-patch-2026-10-30/
  - (health) [California State Portal | CA.gov] 10/30/2026, 07:58 PM, +0000 UTC — AFTER RECORD REDUCTIONS IN HOMELESSNESS: Governor Newsom announces opening of first Prop 1-funded behavioral health facility
    
    Link: https://www.gov.ca.gov/2026/10/30/after-record-reductions-in-homelessness-governor-newsom-announces-opening-of-first-prop-1-funded-behavioral-health-facility/
  - (wellness) [San Bernardino County (.gov)] 10/29/2026, 04:42 PM, +0000 UTC — Celebrating wellness and community across generations
    
    Link: https://main.sbcounty.gov/2026/10/29/celebrating-wellness-and-community-across-generations/
  - (wellness) [ABC News - Breaking News, Latest News and Videos] 10/28/2026, 10:33 PM, +0000 UTC — Some wellness peptides will become widely available, HHS says
    
    Link: https://abcnews.com/Health/wellness-peptides-become-widely-hhs/story?id=137650076
  - (wellness) [Army.mil] 10/28/2026, 07:42 PM, +0000 UTC — Fort McCoy Wellness Fair draws strong participation in 2026
    
    Link: https://www.army.mil/article-amp/296403/fort_mccoy_wellness_fair_draws_strong_participation_in_2026
  - (wellness) [Rolling Stone] 10/27/2026, 01:45 AM, +0000 UTC — The Best Health & Wellness Gifts for a More Wholesome Holiday
    
    Link: https://www.rollingstone.com/product-recommendations/gift-guide/best-health-wellness-gifts-1235647943/
  - (wellness) [Texas A&M University-Commerce] 10/27/2026, 08:26 PM, +0000 UTC — ETAMU Professor Builds Global Community Through Wellness Counseling
    
    Link: https://www.etamu.edu/news/etamu-professor-builds-global-community-through-wellness-counseling/
  - (wellness) [DocWireNews] 10/30/2026, 10:03 AM, +0000 UTC — Wellness Programs Won’t Fix Physician Burnout Alone
    
    Link: https://www.docwirenews.com/post/wellness-programs-wont-fix-a-broken-workplace-ama-leader-says
  - (wellness) [VCU Health] 10/29/2026, 03:51 PM, +0000 UTC — Wellness Week at the VCU Health Hub at 25th helps residents connect with local resources to address health needs
    
    Link: https://www.vcuhealth.org/news/wellness-week-at-the-vcu-health-hub-at-25th-helps-residents-connect-with-local-resources-to-address-health-needs/
  - (wellness) [Binghamton University] 10/26/2026, 03:37 PM, +0000 UTC — 75,000-square-foot expansion ushers in new era of wellness at Binghamton’s East Gym
    
    Link: https://www.binghamton.edu/news/story/6550/east-gym-ushers-in-a-new-era-of-wellness-at-binghamton-university
  - (wellness) [New Noise Magazine] 10/30/2026, 02:52 PM, +0000 UTC — Album Review: Genital Shame – Wellness Plan
    
    Link: https://newnoisemagazine.com/reviews/album-review-genital-shame-wellness-plan/
  - (wellness) [Harvard T.H. Chan School of Public Health] 10/28/2026, 04:01 PM, +0000 UTC — Health and wellness for all: Content creation on social media
    
    Link: https://hsph.harvard.edu/news/health-and-wellness-for-all-content-creation-on-social-media/
  - (wellness) [Case Western Reserve University] 10/30/2026, 11:00 AM, +0000 UTC — 2027 benelect open enrollment and Virtual Benefits & Wellness Fair begin Nov. 2
    
    Link: https://case.edu/news/2027-benelect-open-enrollment-and-virtual-benefits-wellness-fair-begin-nov-2
  - (wellness) [KRBD] 10/28/2026, 06:53 PM, +0000 UTC — Ketchikan Wellness Coalition Report
    
    Link: https://www.krbd.org/2026/10/28/ketchikan-wellness-coalition-report/
  - (medical study) [Stanford Report] 10/27/2026, 08:35 PM, +0000 UTC — Study refines our understanding of long COVID
    
    Link: https://news.stanford.edu/stories/2026/10/long-covid-health-affects-study-design
  - (medical study) [HHMI] 10/28/2026, 07:00 AM, +0000 UTC — PhD and Postdoc Transition Program | Gilliam Fellows
    
    Link: https://www.hhmi.org/programs/gilliam-fellows
  - (medical study) [Ohio Capital Journal] 10/27/2026, 08:02 AM, +0000 UTC — Medical debt hit 1 in 4 Americans and 1 in 5 Ohioans last year, even the insured, study shows
    
    Link: https://ohiocapitaljournal.com/2026/10/27/medical-debt-hit-1-in-4-americans-and-1-in-5-ohioans-last-year-even-the-insured-study-shows/
  - (medical study) [Nature] 10/29/2026, 11:01 AM, +0000 UTC — An agentic AI system enhances clinical detection of immune-related adverse events in a multi-phase validation study
    
    Link: https://www.nature.com/articles/s43018-026-01264-6
  - (medical study) [Memorial Sloan Kettering Cancer Center] 10/25/2026, 04:00 AM, +0000 UTC — FDA Approves Immunotherapy-Only Approach for Some Rectal Cancers: What Patients Need To Know
    
    Link: https://www.mskcc.org/news/rectal-cancer-disappears-after-experimental-use-immunotherapy
  - (medical study) [Fierce Healthcare] 10/29/2026, 12:00 PM, +0000 UTC — Oura, UC San Diego Health collaborate to study GLP-1 outcomes using continuous smart ring data
    
    Link: https://www.fiercehealthcare.com/health-tech/oura-uc-san-diego-health-study-glp-1-outcomes-using-continuous-smart-ring-data
  - (medical study) [News-Medical] 10/26/2026, 12:01 AM, +0000 UTC — Beer, wine or spirits: A large study finds different mortality patterns for each
    
    Link: https://www.news-medical.net/news/20261025/Beer-wine-or-spirits-A-large-study-finds-different-mortality-patterns-for-each.aspx
  - (medical study) [Pew Research Center] 10/29/2026, 01:56 PM, +0000 UTC — Americans Are Open to AI in Healthcare, but Want Humans Making Final Calls
    
    Link: https://www.pewresearch.org/science/2026/10/29/americans-are-open-to-ai-in-healthcare-but-want-humans-making-final-calls/
  - (medical study) [Universities of Wisconsin] 10/27/2026, 02:17 PM, +0000 UTC — A deeper understanding: UWL students gain medical, cultural experience through Ecuador study abroad
    
    Link: https://www.wisconsin.edu/all-in-wisconsin/story/a-deeper-understanding-uwl-students-gain-medical-cultural-experience-through-ecuador-study-abroad/
  - (medical study) [Purdue University] 10/28/2026, 07:00 AM, +0000 UTC — Researchers in various studies looking for participants
    
    Link: https://www.purdue.edu/newsroom/purduetoday/2026/Q4/researchers-in-various-studies-looking-for-participants
  - (medical study) [CIDRAP] 10/26/2026, 06:45 PM, +0000 UTC — Medical assistants talk to families about vaccines in about half of visits, study finds
    
    Link: https://www.cidrap.umn.edu/childhood-vaccines/medical-assistants-talk-families-about-vaccines-about-half-visits-study-finds
  - (medical study) [Yahoo Sports] 10/28/2026, 07:08 PM, +0000 UTC — New study estimates that nearly 75% of former NFL players had CTE at death
    
    Link: https://sports.yahoo.com/nfl/article/new-study-estimates-that-nearly-75-of-former-nfl-players-had-cte-at-death-190841288.html
  - (clinical trial health) [Applied Clinical Trials Online] 10/30/2026, 03:00 PM, +0000 UTC — Walmart and Care Access Plan Three More Clinical Trial Centers in Michigan, Nevada, and Texas
    
    Link: https://www.appliedclinicaltrialsonline.com/view/walmart-care-access-clinical-trial-centers-michigan-nevada-texas
  - (clinical trial health) [Fierce Healthcare] 10/29/2026, 06:06 PM, +0000 UTC — BCBSMA, Medzown team up to match members with clinical trials
    
    Link: https://www.fiercehealthcare.com/payers/bcbsma-medzown-team-match-members-clinical-trials
  - (clinical trial health) [Cleveland Clinic Newsroom] 10/26/2026, 05:11 PM, +0000 UTC — Cleveland Clinic and Dyania’s Work on AI in Clinical Trial Matching Earns 2026 Gartner Eye on Innovation Award
    
    Link: https://newsroom.clevelandclinic.org/2026/10/26/cleveland-clinic-and-dyanias-work-on-ai-in-clinical-trial-matching-earns-2026-gartner-eye-on-innovation-award
  - (clinical trial health) [KXII] 10/30/2026, 01:05 PM, +0000 UTC — What to look for in a clinical trial and why older adults should be included
    
    Link: https://www.kxii.com/2026/10/30/what-look-clinical-trial-why-older-adults-should-be-included/
  - (clinical trial health) [Yahoo Finance] 10/28/2026, 06:15 PM, +0000 UTC — ŌURA Expands Healthcare Research With First Clinical Trial Exploring GLP-1 Treatment Outcomes
    
    Link: https://finance.yahoo.com/healthcare/articles/ura-expands-healthcare-research-first-181500184.html
  - (clinical trial health) [BioBuzz] 10/30/2026, 12:20 PM, +0000 UTC — Zealic Health and Coriqa Clinical Announce Strategic Partnership to Redefine Clinical Trial Execution — From Reactive to Proactive
    
    Link: https://biobuzz.io/news/zealic-health-and-coriqa-clinical-announce-strategic-partnership-to-redefine-clinical-trial/
  - (clinical trial health) [Drug Store News] 10/27/2026, 06:13 PM, +0000 UTC — Walmart, Care Access plan 3 additional clinical trial centers
    
    Link: https://drugstorenews.com/walmart-care-access-plan-3-additional-clinical-trial-centers
  - (clinical trial health) [Community Impact Newspaper] 10/29/2026, 01:12 AM, +0000 UTC — Clinical trial center opens at Greater Houston Walmart | Katy - Fulshear
    
    Link: https://communityimpact.com/katy-fulshear/business/clinical-trial-center-opens-at-greater-houston-walmart/
  - (clinical trial health) [NPR] 10/30/2026, 09:45 PM, +0000 UTC — Ebola vaccine trials begin in DRC
    
    Link: https://www.npr.org/2026/10/30/nx-s1-6020612/ebola-vaccine-trials-begin-in-drc
  - (clinical trial health) [Cancer Health] 10/28/2026, 09:03 AM, +0000 UTC — Novel Cancer Immunotherapy Drug Generates Promising Clinical Trial Results
    
    Link: https://www.cancerhealth.com/article/novel-cancer-immunotherapy-drug-generates-promising-clinical-trial-results
  - (clinical trial health) [News-Medical] 10/31/2026, 03:02 AM, +0000 UTC — New database offers insights into psychedelic use outside clinical trials
    
    Link: https://www.news-medical.net/news/20261030/New-database-offers-insights-into-psychedelic-use-outside-clinical-trials.aspx
  - (clinical trial health) [Medical Marketing and Media] 10/29/2026, 09:00 PM, +0000 UTC — How clinical trial recruitment is learning to meet patients where they are
    
    Link: https://www.mmm-online.com/features/clinical-trial-recruitment-meeting-patients-where-they-are/
  - (FDA recall health) [Cardiovascular Business] 10/29/2026, 08:39 PM, +0000 UTC — FDA confirms Class I recall for certain Impella heart pump controllers
    
    Link: https://cardiovascularbusiness.com/topics/clinical/interventional-cardiology/fda-confirms-class-i-recall-certain-impella-heart-pump-controllers
  - (FDA recall health) [The Healthy @Reader's Digest] 10/30/2026, 03:17 AM, +0000 UTC — Flour Recall: More Than 4,000 Bags Just Received the FDA’s Highest Risk Warning
    
    Link: https://www.thehealthy.com/news/flour-recall-october-2026/
  - (FDA recall health) [Health.com] 10/27/2026, 07:11 PM, +0000 UTC — FDA Announces Butter Recall in 10 States Due to Yeast, Mold, and E. Coli
    
    Link: https://www.health.com/butter-recall-october-2026-12196755
  - (FDA recall health) [Prevention] 10/28/2026, 04:18 PM, +0000 UTC — 1,304 Cases of Plant-Based Butter Recalled Over Potential Mold and E. coli, FDA Warns
    
    Link: https://www.prevention.com/health/a74273046/prosperity-organic-foods-butter-recall-fda/
  - (FDA recall health) [ABC News - Breaking News, Latest News and Videos] 10/28/2026, 05:09 PM, +0000 UTC — Plant-based butter recalled over yeast, mold and E.coli concerns receives FDA risk classification
    
    Link: https://abcnews.com/Health/plant-based-butter-recalled-yeast-mold-ecoli-concerns/story?id=137635485
  - (FDA recall health) [Detroit Free Press] 10/28/2026, 02:03 AM, +0000 UTC — Walmart Great Value fruit cocktail recalled. Is Michigan affected?
    
    Link: https://www.freep.com/story/entertainment/dining/2026/10/27/recall-great-value-walmart-fruit-cocktail-michigan-fda/92456963007/
  - (FDA recall health) [New York Post] 10/28/2026, 03:51 PM, +0000 UTC — FDA recalls butter brand over potential illness caused by E.coli, mold and yeast
    
    Link: https://nypost.com/2026/10/28/lifestyle/fda-recalls-plant-based-miyoko-butter-due-to-e-coli-mold-and-yeast/
  - (FDA recall health) [The Hill] 10/28/2026, 11:29 AM, +0000 UTC — Recalled butter sold in 10 states receives risk warning: FDA
    
    Link: https://thehill.com/homenews/state-watch/6175447-miyokos-creamery-butter-recalled/
  - (FDA recall health) [KLTV.com] 10/30/2026, 04:00 PM, +0000 UTC — Ground cinnamon recalled ahead of holiday season due to elevated lead risk, FDA says
    
    Link: https://www.kltv.com/2026/10/30/ground-cinnamon-recalled-ahead-holiday-season-due-elevated-lead-risk-fda-says/
  - (FDA recall health) [MassLive.com] 10/29/2026, 04:06 PM, +0000 UTC — Butter sold in New England under FDA’s second-highest recall level
    
    Link: https://www.masslive.com/business/2026/10/butter-sold-in-new-england-under-fdas-second-highest-recall-level.html
  - (FDA recall health) [PetfoodIndustry] 10/27/2026, 07:19 PM, +0000 UTC — FDA warns two Darwin’s cat food lots contain Salmonella
    
    Link: https://www.petfoodindustry.com/safety-quality/pet-food-recalls/news/15975598/fda-warns-two-darwins-cat-food-lots-contain-salmonella
  - (FDA recall health) [The Business Journals] 10/28/2026, 06:53 PM, +0000 UTC — Cary firm recalls GLP-1 injections following FDA scrutiny
    
    Link: https://www.bizjournals.com/triangle/news/2026/10/28/apothecary-pharma-recall-tirzepatide-fda-glp1.html