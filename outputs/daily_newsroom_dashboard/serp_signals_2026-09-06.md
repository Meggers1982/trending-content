# LIVE SIGNAL DATA — SerpAPI Pre-Fetch
The following signals were fetched from SerpAPI Google News and SerpAPI Google Trends immediately before this pipeline run. Treat Google Trends as AVAILABLE when this section contains a Google Trends block. Use it as the primary search_velocity input for Skills 01–05 (Signal Listener through Trend Strength Scorer). Use the Google News Radar as the broad discovery layer for news-led health topics, including topics that do not yet appear in Google Trends. Prioritize topics with convergence across News, Trends, primary/institutional sources, and credible publisher coverage.

# SIGNAL INTEGRITY WARNING

SerpAPI stopped answering for google_news partway through this run, so that signal is incomplete below. Other sources ran normally — do not read the gap as an absence of activity. 9 Google News queries were answered via the lighter google_news_light engine instead (labeled [light] below); those articles carry fewer fields than a normal google_news result and should not be treated as full-fidelity.

Treat absence of signal as unknown, not as absence of activity. Say so in signal_summary.notes and lower confidence accordingly.

## Google Trends — 7-Day Interest (US)
  - **health**: latest=41, peak=100, 7d-delta=-1
    Rising related: lionel richie health, reverse health cost, lionel richie health update, how to check hard drive health, how to check ssd health, how to check laptop battery health, how to improve gut health, battery health check iphone
  - **wellness**: latest=89, peak=100, 7d-delta=+46
    Rising related: jennifer lawrence beauty wellness routine, wellness darty, what is a wellness darty, tender gifts birth & wellness center, gracie hunt wellness brand backing, wellness brand with ceo gwyneth paltrow, circle wellness seattle, stc wellness city
  - **nutrition**: latest=73, peak=100, 7d-delta=-12
    Rising related: pollo asado chipotle nutrition, kona ice nutrition, how to read nutrition labels, crumbl nutrition facts, crumbl cookie nutrition facts, nutrition near me, nutrition facts, what is nutrition
  - **fitness**: latest=39, peak=100, 7d-delta=-2
    Rising related: is planet fitness open on labor day, planet fitness labor day hours, la fitness labor day hours, physical fitness program, fitness centre, planet fitness annual fee, bungee fitness near me, bungee fitness
  - **food safety**: latest=16, peak=100, 7d-delta=+2
    Rising related: washing cabbage food safety tips, walmart food safety recall mangoes, up&up baby wipes safety recall, cracked eggs food safety risks, fda baxter international voluntary recall, cyclosporiasis outbreak iceberg lettuce safety, american shoppers food safety concerns, fda fresh cut produce safety guidance
  - **diet**: latest=77, peak=100, 7d-delta=-13
    Rising related: cell metabolism keto diet study, jd vance weight loss diet, mediterranean diet pasta dinner recipe, what is a detox diet, sauerkraut diet, proper diet to lose weight, ketogenic diet, diet drinks at sonic
  - **weight loss**: latest=38, peak=100, 7d-delta=-5
    Rising related: jd vance weight loss white house, jd vance weight loss, best smoothie recipes for weight loss, erin burnett weight loss, kelly clarkson weight loss, weight loss service, medvi health, versace hotel dubai
  - **mental health**: latest=38, peak=100, 7d-delta=+1
    Rising related: pamela cisneros mental health, the importance of learning languages, how ai is changing our lives, is september mental health awareness month, september mental health awareness, september mental health month, how social media affects our mental health, what awareness month is september
  - **gut health**: latest=42, peak=100, 7d-delta=-3
    Rising related: how to improve gut health, improve gut health, magnesium citrate, magnesium for gut health, magnesium glycinate, holistic gut health doctor near me, is farting a sign of good gut health, dysbiosis

Top rising related queries from Google Trends:
  - lionel richie health
  - reverse health cost
  - lionel richie health update
  - how to check hard drive health
  - how to check ssd health
  - how to check laptop battery health
  - how to improve gut health
  - battery health check iphone
  - jennifer lawrence beauty wellness routine
  - wellness darty
  - what is a wellness darty
  - tender gifts birth & wellness center
  - gracie hunt wellness brand backing
  - wellness brand with ceo gwyneth paltrow
  - circle wellness seattle
  - stc wellness city
  - pollo asado chipotle nutrition
  - kona ice nutrition
  - how to read nutrition labels
  - crumbl nutrition facts

## Google News Radar — Recent Health Topics (114 unique across 12 queries; showing 60; 78 tagged [light] came from the google_news_light fallback and carry fewer fields)
Treat these headlines as the broad radar of news-led health topics. The Signal Listener must consider this radar before narrowing to retained candidates.
  - (health) [Centers for Disease Control and Prevention | CDC (.gov)] 08/31/2026, 07:00 AM, +0000 UTC — Public Health Data Strategy Milestones for 2026 | The PHDS
    
    Link: https://www.cdc.gov/public-health-data-strategy/php/about/phds-milestones.html
  - (health) [U.S. Department of War (.gov)] 09/02/2026, 06:41 PM, +0000 UTC — Statement by Chief Pentagon Spokesman, Sean Parnell, on the Clinical Guidance for Health a
    
    Link: https://www.war.gov/News/Releases/Release/Article/4589310/statement-by-chief-pentagon-spokesman-sean-parnell-on-the-clinical-guidance-for/
  - (health) [Think Global Health] 09/01/2026, 11:55 AM, +0000 UTC — The Future of Global Health: Themes and Thorny Questions
    
    Link: https://www.thinkglobalhealth.org/article/the-future-of-global-health-themes-and-thorny-questions
  - (health) [OpenAI] 09/01/2026, 05:02 PM, +0000 UTC — Healthcare organizations can now connect EHR and additional industry data to ChatGPT
    
    Link: https://openai.com/index/chatgpt-connects-health-records-and-healthcare-sources/
  - (health) [NASA (.gov)] 09/03/2026, 08:57 PM, +0000 UTC — Request for Information: Help Shape Human Health Research for the Future Moon Base
    
    Link: https://www.nasa.gov/hrp/request-for-information-help-shape-human-health-research-for-the-future-moon-base/
  - (health) [Source New Mexico] 09/01/2026, 07:50 PM, +0000 UTC — New Mexico insurance superintendent approves 24% premium increase on healthcare exchange plans
    
    Link: https://sourcenm.com/2026/09/01/new-mexico-insurance-superintendent-approves-24-premium-increase-on-healthcare-exchange-plans/
  - (health) [usf.edu] 09/03/2026, 08:54 PM, +0000 UTC — USF Health Morsani College of Medicine ranks No. 1 in the nation for second straight year in Medical School Excellence Index
    
    Link: https://www.usf.edu/health/news/2026/morsani-college-of-medicine-ranks-no-1-in-the-nation-for-second-straight-year.aspx
  - (health) [ecuhealth.org] 08/31/2026, 08:23 PM, +0000 UTC — Eighteen ECU Health Nurses named Great 100 Nurses of North Carolina
    
    Link: https://www.ecuhealth.org/eighteen-ecu-health-nurses-named-great-100-nurses-of-north-carolina/
  - (health) [Stanford Medicine] 09/04/2026, 05:18 PM, +0000 UTC — Health warnings could reduce young people’s social media use, Stanford Medicine-led study finds
    
    Link: https://med.stanford.edu/news/all-news/2026/09/social-media-warnings.html
  - (health) [wbaltv.com] 09/03/2026, 11:21 AM, +0000 UTC — Luminis Health cyber-attack disrupts Anne Arundel Medical Center
    
    Link: https://www.wbaltv.com/article/anne-arundel-medical-center-cyberattack/73596317
  - (health) [flatheadbeacon.com] 09/04/2026, 08:15 PM, +0000 UTC — Logan Health Primary Care Providers Sign Vote of ‘No Confidence’ in Leadership
    
    Link: https://flatheadbeacon.com/2026/09/04/logan-health-primary-care-providers-sign-vote-of-no-confidence-in-leadership/
  - (health) [Health Policy Watch] 08/31/2026, 03:15 PM, +0000 UTC — United States To Cut Health Funding To 18 Countries 59% By 2030
    
    Link: https://healthpolicy-watch.news/by-2030-us-to-cut-health-funding-to-18-countries-by-59/
  - (wellness) [Hackensack Meridian Health] 09/01/2026, 03:32 PM, +0000 UTC — New Hackensack Meridian Health & Wellness Center at Freehold Brings Together Primary and Specialty Care
    
    Link: https://hackensackmeridianhealth.org/en/news/2026/09/01/new-hackensack-meridian-health-wellness-center-at-freehold
  - (wellness) [Boston Consulting Group] 09/01/2026, 07:49 AM, +0000 UTC — As Wellness Spending Grows, Can Activewear Brands Seize the Opportunity?
    
    Link: https://www.bcg.com/publications/2026/activewear-brands-wellness-growth
  - (wellness) [Employment Law Worldview] 09/03/2026, 06:58 PM, +0000 UTC — Quitting Cold Turkey: Federal Agencies Suspend Enforcement of Back-Pay Requirement for Employee Wellness Incentives, Including Tobacco Cessation Programs (US)
    
    Link: https://www.employmentlawworldview.com/quitting-cold-turkey-federal-agencies-suspend-enforcement-of-back-pay-requirement-for-employee-wellness-incentives-including-tobacco-cessation-programs-us/
  - (wellness) [Fairfield University] 09/04/2026, 04:00 AM, +0000 UTC — SEHD Hosts Second Annual Educator Resiliency and Wellness Institute
    
    Link: https://www.fairfield.edu/news/2026/september/second-educator-resiliency-wellness-institute.html
  - (wellness) [City of Palo Alto (.gov)] 09/01/2026, 06:57 PM, +0000 UTC — Resources to Prioritize Self-Care, Wellness and Wellbeing
    
    Link: https://www.paloalto.gov/News-Articles/City-Manager/Wellness-Month-Resources-to-Prioritize-Self-Care-Wellness-and-Wellbeing
  - (wellness) [49ers.com] 09/06/2026, 04:05 AM, +0000 UTC — 49ers Prepare Educators to Build Positive Sports Culture Through Mental Wellness
    
    Link: https://www.49ers.com/photos/49ers-prepare-educators-to-build-positive-sports-culture-through-mental-wellness
  - (wellness) [IN.gov] 09/02/2026, 10:32 PM, +0000 UTC — Invest in Your Health (State Employee Wellness Program): Optum EAP - Suicide prevention and recovery
    
    Link: https://www.in.gov/investinyourhealth/post/optum-eap-suicide-prevention-and-recovery
  - (wellness) [Illinois State University News] 09/04/2026, 01:36 PM, +0000 UTC — Skate Park Saturdays create space for wellness and connection
    
    Link: https://news.illinoisstate.edu/2026/09/skate-park-saturdays-create-space-for-wellness-and-connection/
  - (wellness) [Ferris State University] 09/01/2026, 09:50 PM, +0000 UTC — Room to breathe: Ferris State expands student wellness resources at its Grand Rapids campus
    
    Link: https://www.ferris.edu/news/archive/2026/room-to-breathe-ferris-state-expands-student-wellness-resources-at-grand-rapids-campus.htm
  - (wellness) [Geauga County Maple Leaf] 09/02/2026, 06:43 PM, +0000 UTC — Inaugural Conference Puts First Responder Wellness in Focus
    
    Link: https://www.geaugamapleleaf.com/news/inaugural-conference-puts-first-responder-wellness-in-focus/
  - (wellness) [apu.edu] 09/01/2026, 08:10 AM, +0000 UTC — APU Receives $312,500 Grant to Train Certified Wellness Coaches to Help Youth
    
    Link: https://www.apu.edu/media/news/release/apu-receives-312500-grant-to-train-certified-wellness-coaches/
  - (wellness) [Grocery Dive] 08/31/2026, 04:06 PM, +0000 UTC — Kroger amplifies wellness focus with in-store events and ‘mini-fests’
    
    Link: https://www.grocerydive.com/news/kroger-wellness-tour-store-events-festivals/829161/
  - (medical study) [American Medical Association | AMA] 09/04/2026, 12:06 PM, +0000 UTC — Using AI to study: Medical students should know the do’s and don’ts
    
    Link: https://www.ama-assn.org/medical-students/succeed-medical-school/using-ai-study-medical-students-should-know-do-s-and-don-ts
  - (medical study) [UAMS News] 09/04/2026, 02:26 PM, +0000 UTC — UAMS Part of Clinical Study Exploring Blood Pressure Instability Treatment for People With Spinal Cord Injury
    
    Link: https://news.uams.edu/2026/09/04/uams-part-of-clinical-study-exploring-blood-pressure-instability-treatment-for-people-with-spinal-cord-injury/
  - (medical study) [nature.com] 09/03/2026, 06:00 PM, +0000 UTC — A five-phase evaluation framework for diagnostic and predictive medical artificial intelligence
    
    Link: https://www.nature.com/articles/s41746-026-03155-7
  - (medical study) [Penn Medicine] 09/01/2026, 12:49 PM, +0000 UTC — Penn launches first advanced proton therapy clinical trial
    
    Link: https://www.pennmedicine.org/news/penn-launches-first-advanced-proton-therapy-clinical-trial
  - (medical study) [Brown University] 09/03/2026, 03:08 PM, +0000 UTC — Transformative $37 million investment will create alliance to advance breakthroughs in aging research, clinical care
    
    Link: https://www.brown.edu/news/2026-09-03/starr-healthspan-innovation-alliance
  - (medical study) [mountsinai.org] 09/05/2026, 12:10 PM, +0000 UTC — Mount Sinai Researchers Report Largest Study Supporting Three Courses of Radiation for Children With Deadly Brain Tumor
    
    Link: https://www.mountsinai.org/about/newsroom/2026/mount-sinai-researchers-report-largest-study-supporting-three-courses-of-radiation-for-children-with-deadly-brain-tumor
  - (medical study) [fda.gov] 09/02/2026, 12:00 AM, +0000 UTC — Good Clinical Practices Are Not Optional
    
    Link: https://www.fda.gov/news-events/fda-voices/good-clinical-practices-are-not-optional-fdas-commitment-human-subject-protections-and-gold-standard
  - (medical study) [Marquette Today] 09/01/2026, 02:07 PM, +0000 UTC — Marquette biomedical engineering professor receives NIH grant to study acute respiratory distress syndrome
    
    Link: https://today.marquette.edu/2026/09/marquette-biomedical-engineering-professor-receives-nih-grant-to-study-acute-respiratory-distress-syndrome/
  - (medical study) [Yahoo Finance] 09/03/2026, 05:30 AM, +0000 UTC — ONWARD Medical Announces First Implant in New Clinical Feasibility Study Evaluating ARC-IM System to Restore Mobility After Spinal Cord Injury
    
    Link: https://finance.yahoo.com/healthcare/articles/onward-medical-announces-first-implant-053000099.html
  - (medical study) [University of Miami] 09/02/2026, 11:31 PM, +0000 UTC — U.S. Cancer Deaths Linked to Alcohol Have Doubled Since 1990, Study Finds
    
    Link: https://news.med.miami.edu/alcohol-related-cancer-deaths-double-us-study/
  - (medical study) [Medical Xpress] 09/04/2026, 03:00 PM, +0000 UTC — Health warnings could reduce young people's social media use, study finds
    
    Link: https://medicalxpress.com/news/2026-09-health-young-people-social-media.html
  - (medical study) [Biogen] 09/03/2026, 04:00 AM, +0000 UTC — LEQEMBI® (lecanemab) Subcutaneous Formulation as an Initiation Treatment for Early Alzheimer’s Disease Approved in China
    
    Link: https://investors.biogen.com/news-releases/news-release-details/leqembir-lecanemab-subcutaneous-formulation-initiation-treatment
  - (clinical trial health) [light] [The Clinical Trial Vanguard] 8 hours ago — Signant Health, Lothar Medical Plan Integrated Respiratory Trial Device
    Respiratory clinical trials routinely ask sites to manage three separate devices for spirometry, oscillometry, and fractional exhaled nitric...
    Link: https://www.clinicaltrialvanguard.com/news/signant-health-lothar-medical-plan-integrated-respiratory-trial-device/
  - (clinical trial health) [light] [U.S. News & World Report] 2 days ago — America Doesn't Have a Science Problem. It Has a Clinical Trial Problem. | US News Opinion
    America has never had more promising science – or a greater opportunity to cure disease. Yet every day, patients wait because our clinical...
    Link: https://www.usnews.com/opinion/articles/2026-09-03/america-doesnt-have-a-science-problem-it-has-a-clinical-trial-problem
  - (clinical trial health) [light] [Dermatology Advisor] 2 days ago — Women in Clinical Trials: History and Impact
    Clinical trials have existed in some form for many centuries, be it Dr. James Lind's controlled clinical trial on scurvy in 1747 to biblical...
    Link: https://www.dermatologyadvisor.com/features/women-in-clinical-trials-history-impact/
  - (clinical trial health) [light] [KFF Health News] 2 weeks ago — You Want To Join a Clinical Trial. Here’s What To Know About the Hurdles.
    The Department of Health and Human Services has launched an effort to streamline clinical research, and legislation is pending in Congress.
    Link: https://kffhealthnews.org/health-industry/clinical-trials-patients-hhs-easier-advice-on-how-to-enroll-seriously-ill-cancer/
  - (clinical trial health) [light] [www.discoverhealth.org] 2 days ago — Gibbs oncologists advancing prostate cancer treatment through clinical research
    For many men undergoing treatment for prostate cancer, hot flashes can be an unexpected and disruptive side effect.
    Link: https://www.discoverhealth.org/gibbs-oncologists-advancing-prostate-cancer-treatment-through-clinical-research
  - (clinical trial health) [light] [WPRI.com] 2 days ago — Brown gets $37 million for aging research, clinical trials
    PROVIDENCE, R.I. (WPRI) — A philanthropic group is fronting $37 million to Brown University and Brown University Health to accelerate...
    Link: https://www.wpri.com/health/brown-gets-37-million-for-aging-research-clinical-trials/
  - (clinical trial health) [light] [NBC News] 2 days ago — Clinical trial aims to give more organ transplant patients lives free of harsh drugs
    Doctors have been experimenting with adding stem cells to kidney transplants to get patients off immune-suppressing drugs.
    Link: https://www.nbcnews.com/health/health-news/clinical-trial-aims-give-organ-transplant-patients-lives-free-harsh-dr-rcna595580
  - (clinical trial health) [light] [WSJ] 2 days ago — Exclusive | Drugmakers Halt Autoimmune Trials After Deaths, Life-Threatening Side Effects
    Trial freezes by Novartis and Bristol Myers have triggered race to understand why promising autoimmune treatment turned risky.
    Link: https://www.wsj.com/health/pharma/drugmakers-halt-autoimmune-trials-after-deaths-life-threatening-side-effects-14e786fd
  - (clinical trial health) [light] [Yahoo Finance] 6 days ago — Data4Life and Monash Health Announce Strategic Collaboration to Advance Clinical Research
    Data4Life and Monash Health have partnered to optimize clinical trial design and execution, complemented by educational workshops and...
    Link: https://finance.yahoo.com/healthcare/articles/data4life-monash-health-announce-strategic-130000171.html
  - (FDA recall health) [light] [U.S. Food and Drug Administration (.gov)] 3 days ago — Outbreak Investigation of E. coli O145:H28: Frozen Blueberries (July 2026)
    On September 2, 2026, Frutas y Hortalizas del Sur S.A. expanded their recall to include Great Value-brand Organic Triple Berry Blend 10-oz,...
    Link: https://www.fda.gov/food/outbreaks-foodborne-illness/outbreak-investigation-e-coli-o145h28-frozen-blueberries-july-2026
  - (FDA recall health) [light] [NewsNation] 1 day ago — Epinephrine injection recalled over potentially fatal health risks: FDA
    A pharmaceutical company is recalling three lots of Epinephrine Injection over sterility concerns and the potential presence of particulate...
    Link: https://www.newsnationnow.com/us-news/recalls/epinephrine-injection-recalled-health-risks-fda/
  - (FDA recall health) [light] [The New York Times] 18 hours ago — E. Coli Illnesses Linked to Frozen Blueberries Are Up to 17, F.D.A. Says
    The affected frozen fruit products, which were distributed to 19 states and to retailers like Walmart and Publix, were recalled starting in...
    Link: https://www.nytimes.com/2026/09/05/health/frozen-blueberries-recall-e-coli.html
  - (FDA recall health) [light] [Healthline] 4 days ago — FDA Recalls IV Fluids Due to Fiberglass, Other Hazardous Materials
    The Food and Drug Administration (FDA) announced a recall of saline and other IV fluids manufactured by Baxter International and B. Braun...
    Link: https://www.healthline.com/health-news/fda-recalls-iv-saline-fluids-fiberglass-stainless-steel-contaminants
  - (FDA recall health) [light] [Fortune] 3 days ago — American shoppers are so rattled by surging FDA recalls that 67% now avoid a whole food category after just one notice
    The FDA posted 26 food recall notices in August—and 67% of consumers now say they've avoided an entire food category after a recall.
    Link: https://fortune.com/2026/09/02/food-recalls-fda-americans-avoid-food-categories/
  - (FDA recall health) [light] [The Healthy @Reader's Digest] 3 days ago — New Fruit Recalls Affect Products Sold at Walmart and CVS
    A number of foods have been affected by recalls lately, with one of the most notable involving lettuce linked to Cyclospora.
    Link: https://www.thehealthy.com/news/fruit-recalls-walmart-cvs-september-2026/
  - (FDA recall health) [light] [The Hill] 1 day ago — Epinephrine injection recalled over potentially fatal health risks
    A pharmaceutical company is recalling three lots of Epinephrine Injection over sterility concerns and the potential presence of particulate...
    Link: https://thehill.com/policy/healthcare/6071686-epinephrine-injection-recalled-fatal-health-risk-fda/
  - (FDA recall health) [light] [U.S. Food and Drug Administration (.gov)] 3 days ago — Outbreak Investigation of Salmonella: Eggs (July 2026)
    Recalled eggs are past expiration and should no longer be available for sale. Recalled white shell eggs and brown cage-free shell eggs from...
    Link: https://www.fda.gov/food/outbreaks-foodborne-illness/outbreak-investigation-salmonella-eggs-july-2026
  - (FDA recall health) [light] [Centers for Disease Control and Prevention | CDC (.gov)] 3 days ago — Cyclospora Outbreak Linked to Iceberg Lettuce | Cyclosporiasis
    CDC, FDA, and state and local public health officials continue to investigate a multistate outbreak of Cyclospora infections linked to...
    Link: https://www.cdc.gov/cyclosporiasis/outbreaks/07-26/index.html
  - (FDA recall health) [light] [EatingWell] 2 days ago — The FDA Issued a Recall on Tofu Due to Potential Chemical Contamination
    The FDA recalled 75,250 packages of Hodo's Chili Crisp Lightly Fried Tofu due to potential contamination. The recall affects 29 states;...
    Link: https://www.eatingwell.com/tofu-recall-chemical-contamination-12097001
  - (food safety recall) [light] [Stateline] 6 days ago — A summer of recalls exposes holes in the nation’s food safety net
    Jalapenos. Frozen berries. Beef. Alfalfa sprouts. A summer of food recalls, including the record-shattering cyclosporiasis outbreak tied to...
    Link: https://stateline.org/2026/08/31/a-summer-of-recalls-exposes-holes-in-the-nations-food-safety-net/
  - (food safety recall) [light] [Food Safety News] 13 hours ago — Foods Alive moringa powder recalled because of Salmonella contamination
    Foods Alive Inc of Angola, IN, is recalling its 8-ounce packages of organic moringa leaf powder because they have the potential to be...
    Link: https://www.foodsafetynews.com/2026/09/foods-alive-moringa-powder-recalled-because-of-salmonella-contamination/
  - (food safety recall) [light] [The Atlantic] 4 days ago — The Truth About American Food Safety
    The phrase When it rains, it pours isn't one you like to see applied to outbreaks of foodborne illness, yet here we are.
    Link: https://www.theatlantic.com/health/2026/09/foodborne-illness-recall-cyclospora-summer/688497/
  - (food safety recall) [light] [eFoodAlert] 16 hours ago — Recalls and Alerts: September 4–5, 2026
    eFoodAlert posts links to recalls for English-language countries only. If you are interested in recall information for other countries...
    Link: https://efoodalert.com/2026/09/05/recalls-and-alerts-september-4-5-2026/
  - (food safety recall) [light] [Quality Assurance & Food Safety] 3 days ago — 94% of U.S. Adults Concerned About Frequency of Food Recalls, New Survey Finds
    The new consumer survey, commissioned by GS1 US, also shows that fewer people believe food recalls are effective in protecting public health...
    Link: https://www.qualityassurancemag.com/news/94-percent-of-adults-in-the-united-states-concerned-about-frequency-of-food-recalls-survey-finds/