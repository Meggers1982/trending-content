# LIVE SIGNAL DATA — SerpAPI Pre-Fetch
The following signals were fetched from SerpAPI Google News and SerpAPI Google Trends immediately before this pipeline run. Treat Google Trends as AVAILABLE when this section contains a Google Trends block. Use it as the primary search_velocity input for Skills 01–05 (Signal Listener through Trend Strength Scorer). Use the Google News Radar as the broad discovery layer for news-led health topics, including topics that do not yet appear in Google Trends. Prioritize topics with convergence across News, Trends, primary/institutional sources, and credible publisher coverage.

# SIGNAL INTEGRITY WARNING

SerpAPI stopped answering for google_news partway through this run, so that signal is incomplete below. Other sources ran normally — do not read the gap as an absence of activity.

Treat absence of signal as unknown, not as absence of activity. Say so in signal_summary.notes and lower confidence accordingly.

## Google Trends — Trending Now (US / Health, real-time)
Terms with a "Why:" line have a confirmed real-world news story driving the spike; terms without one are a real-time signal only, not yet grounded in a specific story.
  - alcohol cancer deaths
    Why: "Just one drink a day may increase the risk of dying from numerous cancers" — CNN
  - igho ubiribo
    Why: "Influencer dies after receiving penis enlargement injection in Thailand: report" — New York Post

## Google Trends — 7-Day Interest (US)
  - **health**: latest=33, peak=100, 7d-delta=-2
    Rising related: lionel richie health, jim curtis health, lionel richie health update, reverse health cost, how to check hard drive health, city of kansas city health department, how to check ssd health, how to check laptop battery health
  - **wellness**: latest=30, peak=100, 7d-delta=-5
    Rising related: jennifer lawrence beauty wellness routine, wellness darty, what is a wellness darty, gracie hunt wellness brand backing, stc wellness city, tender gifts birth & wellness center, circle wellness seattle, byu student wellness
  - **nutrition**: latest=61, peak=100, 7d-delta=-10
    Rising related: pollo asado chipotle nutrition, kona ice nutrition, how to read nutrition labels, crumbl nutrition facts, supplemental nutrition assistance program, crumbl cookie nutrition facts, nutrition facts, what is nutrition
  - **fitness**: latest=32, peak=100, 7d-delta=-4
    Rising related: is planet fitness open on labor day, planet fitness labor day hours, andy reid comments on mahomes fitness, physical fitness program, fitness centre, bungee fitness near me, planet fitness annual fee, bungee fitness
  - **food safety**: latest=18, peak=100, 7d-delta=+0
    Rising related: washing cabbage food safety tips, walmart food safety recall mangoes, wilkerson dining facility food safety, up&up baby wipes safety recall, fda baxter international voluntary recall, cyclosporiasis outbreak iceberg lettuce safety, american shoppers food safety concerns, medtronic bravo cf capsule safety alert
  - **diet**: latest=65, peak=100, 7d-delta=-12
    Rising related: cell metabolism keto diet study, mediterranean diet pasta dinner recipe, jd vance weight loss diet, bobby kennedy diet, diet with fat bombs, jd vance diet, serena williams training day diet, what is a detox diet
  - **weight loss**: latest=30, peak=100, 7d-delta=-3
    Rising related: jd vance weight loss, jd vance weight loss white house, best smoothie recipes for weight loss, erin burnett weight loss, avatrade mt4, cider coupon, kelly clarkson weight loss, weight loss service
  - **mental health**: latest=36, peak=100, 7d-delta=-1
    Rising related: pamela cisneros mental health, how social media affects our mental health, is september mental health awareness month, september mental health awareness, september mental health month, what awareness month is september, suicide awareness month, suicide prevention month
  - **gut health**: latest=27, peak=100, 7d-delta=-2
    Rising related: mel robbins podcast, how to improve gut health, magnesium citrate, improve gut health, tempeh, why is gut health important, dysbiosis, resilia

Top rising related queries from Google Trends:
  - lionel richie health
  - jim curtis health
  - lionel richie health update
  - reverse health cost
  - how to check hard drive health
  - city of kansas city health department
  - how to check ssd health
  - how to check laptop battery health
  - jennifer lawrence beauty wellness routine
  - wellness darty
  - what is a wellness darty
  - gracie hunt wellness brand backing
  - stc wellness city
  - tender gifts birth & wellness center
  - circle wellness seattle
  - byu student wellness
  - pollo asado chipotle nutrition
  - kona ice nutrition
  - how to read nutrition labels
  - crumbl nutrition facts

## Google News Radar — Recent Health Topics (72 unique across 12 queries; showing 60)
Treat these headlines as the broad radar of news-led health topics. The Signal Listener must consider this radar before narrowing to retained candidates.
  - (health) [Centers for Disease Control and Prevention | CDC (.gov)] 08/31/2026, 07:00 AM, +0000 UTC — Public Health Data Strategy Milestones for 2026 | The PHDS
    
    Link: https://www.cdc.gov/public-health-data-strategy/php/about/phds-milestones.html
  - (health) [OpenAI] 09/01/2026, 05:02 PM, +0000 UTC — Healthcare organizations can now connect EHR and additional industry data to ChatGPT
    
    Link: https://openai.com/index/chatgpt-connects-health-records-and-healthcare-sources/
  - (health) [Think Global Health] 09/01/2026, 11:55 AM, +0000 UTC — The Future of Global Health: Themes and Thorny Questions
    
    Link: https://www.thinkglobalhealth.org/article/the-future-of-global-health-themes-and-thorny-questions
  - (health) [U.S. Department of War (.gov)] 09/02/2026, 06:41 PM, +0000 UTC — Statement by Chief Pentagon Spokesman, Sean Parnell, on the Clinical Guidance for Health a
    
    Link: https://www.war.gov/News/Releases/Release/Article/4589310/statement-by-chief-pentagon-spokesman-sean-parnell-on-the-clinical-guidance-for/
  - (health) [NASA (.gov)] 09/03/2026, 08:57 PM, +0000 UTC — Request for Information: Help Shape Human Health Research for the Future Moon Base
    
    Link: https://www.nasa.gov/hrp/request-for-information-help-shape-human-health-research-for-the-future-moon-base/
  - (health) [Source New Mexico] 09/01/2026, 07:50 PM, +0000 UTC — New Mexico insurance superintendent approves 24% premium increase on healthcare exchange plans
    
    Link: https://sourcenm.com/2026/09/01/new-mexico-insurance-superintendent-approves-24-premium-increase-on-healthcare-exchange-plans/
  - (health) [University of South Florida] 09/03/2026, 08:54 PM, +0000 UTC — USF Health Morsani College of Medicine ranks No. 1 in the nation for second straight year in Medical School Excellence Index
    
    Link: https://www.usf.edu/health/news/2026/morsani-college-of-medicine-ranks-no-1-in-the-nation-for-second-straight-year.aspx
  - (health) [ECU Health] 08/31/2026, 08:23 PM, +0000 UTC — Eighteen ECU Health Nurses named Great 100 Nurses of North Carolina
    
    Link: https://www.ecuhealth.org/eighteen-ecu-health-nurses-named-great-100-nurses-of-north-carolina/
  - (health) [WBAL-TV] 09/03/2026, 11:21 AM, +0000 UTC — Luminis Health cyber-attack disrupts Anne Arundel Medical Center
    
    Link: https://www.wbaltv.com/article/anne-arundel-medical-center-cyberattack/73596317
  - (health) [Flathead Beacon] 09/04/2026, 08:15 PM, +0000 UTC — Logan Health Primary Care Providers Sign Vote of ‘No Confidence’ in Leadership
    
    Link: https://flatheadbeacon.com/2026/09/04/logan-health-primary-care-providers-sign-vote-of-no-confidence-in-leadership/
  - (health) [Health Policy Watch] 08/31/2026, 03:15 PM, +0000 UTC — United States To Cut Health Funding To 18 Countries 59% By 2030
    
    Link: https://healthpolicy-watch.news/by-2030-us-to-cut-health-funding-to-18-countries-by-59/
  - (health) [mercer.com] 09/04/2026, 02:32 PM, +0000 UTC — Survey: Health benefit costs expected to jump 8.2% in 2027, the biggest increase since 2003
    
    Link: https://www.mercer.com/en-us/insights/us-health-news/survey-health-benefit-costs-expected-to-jump-in-2027/
  - (wellness) [Hackensack Meridian Health] 09/01/2026, 03:32 PM, +0000 UTC — New Hackensack Meridian Health & Wellness Center at Freehold Brings Together Primary and Specialty Care
    
    Link: https://hackensackmeridianhealth.org/en/news/2026/09/01/new-hackensack-meridian-health-wellness-center-at-freehold
  - (wellness) [Marquette Today] 09/02/2026, 07:19 PM, +0000 UTC — New My Wellness program year has begun
    
    Link: https://today.marquette.edu/2026/09/new-my-wellness-program-year-has-begun/
  - (wellness) [Boston Consulting Group] 09/01/2026, 07:49 AM, +0000 UTC — As Wellness Spending Grows, Can Activewear Brands Seize the Opportunity?
    
    Link: https://www.bcg.com/publications/2026/activewear-brands-wellness-growth
  - (wellness) [Employment Law Worldview] 09/03/2026, 06:58 PM, +0000 UTC — Quitting Cold Turkey: Federal Agencies Suspend Enforcement of Back-Pay Requirement for Employee Wellness Incentives, Including Tobacco Cessation Programs (US)
    
    Link: https://www.employmentlawworldview.com/quitting-cold-turkey-federal-agencies-suspend-enforcement-of-back-pay-requirement-for-employee-wellness-incentives-including-tobacco-cessation-programs-us/
  - (wellness) [Fairfield University] 09/04/2026, 04:00 AM, +0000 UTC — SEHD Hosts Second Annual Educator Resiliency and Wellness Institute
    
    Link: https://www.fairfield.edu/news/2026/september/second-educator-resiliency-wellness-institute.html
  - (wellness) [City of Palo Alto (.gov)] 09/01/2026, 06:57 PM, +0000 UTC — Resources to Prioritize Self-Care, Wellness and Wellbeing
    
    Link: https://www.paloalto.gov/News-Articles/City-Manager/Wellness-Month-Resources-to-Prioritize-Self-Care-Wellness-and-Wellbeing
  - (wellness) [IN.gov] 09/02/2026, 10:32 PM, +0000 UTC — Invest in Your Health (State Employee Wellness Program): Optum EAP - Suicide prevention and recovery
    
    Link: https://www.in.gov/investinyourhealth/post/optum-eap-suicide-prevention-and-recovery
  - (wellness) [Illinois State University News] 09/04/2026, 06:05 PM, +0000 UTC — Health Promotion and Wellness offers Mindfulness classes this fall
    
    Link: https://news.illinoisstate.edu/2026/09/health-promotion-and-wellness-offers-mindfulness-classes-this-fall/
  - (wellness) [Ferris State University] 09/01/2026, 09:50 PM, +0000 UTC — Room to breathe: Ferris State expands student wellness resources at its Grand Rapids campus
    
    Link: https://www.ferris.edu/news/archive/2026/room-to-breathe-ferris-state-expands-student-wellness-resources-at-grand-rapids-campus.htm
  - (wellness) [Marshall Health] 09/03/2026, 06:15 PM, +0000 UTC — Marshall Health Network to offer flu shots, health screenings at Senior Wellness Day Sept. 19
    
    Link: https://news.marshallhealth.org/2026/09/03/marshall-health-network-to-offer-flu-shots-health-screenings-at-senior-wellness-day-sept-19/
  - (wellness) [Seyfarth Shaw] 09/04/2026, 02:23 AM, +0000 UTC — Wellness Program FAQs: Agencies Offer Relief on Retroactive Rewards and Clarify Notice Requirements
    
    Link: https://www.seyfarth.com/news-insights/wellness-program-faqs-agencies-offer-relief-on-retroactive-rewards-and-clarify-notice-requirements.html
  - (wellness) [Geauga County Maple Leaf] 09/02/2026, 06:43 PM, +0000 UTC — Inaugural Conference Puts First Responder Wellness in Focus
    
    Link: https://www.geaugamapleleaf.com/news/inaugural-conference-puts-first-responder-wellness-in-focus/
  - (medical study) [UAMS News] 09/04/2026, 02:26 PM, +0000 UTC — UAMS Part of Clinical Study Exploring Blood Pressure Instability Treatment for People With Spinal Cord Injury
    
    Link: https://news.uams.edu/2026/09/04/uams-part-of-clinical-study-exploring-blood-pressure-instability-treatment-for-people-with-spinal-cord-injury/
  - (medical study) [Penn Medicine] 09/01/2026, 12:49 PM, +0000 UTC — Penn launches first advanced proton therapy clinical trial
    
    Link: https://www.pennmedicine.org/news/penn-launches-first-advanced-proton-therapy-clinical-trial
  - (medical study) [American Medical Association | AMA] 09/04/2026, 12:06 PM, +0000 UTC — Using AI to study: Medical students should know the do’s and don’ts
    
    Link: https://www.ama-assn.org/medical-students/succeed-medical-school/using-ai-study-medical-students-should-know-do-s-and-don-ts
  - (medical study) [Mount Sinai] 09/05/2026, 12:10 PM, +0000 UTC — Mount Sinai Researchers Report Largest Study Supporting Three Courses of Radiation for Children With Deadly Brain Tumor
    
    Link: https://www.mountsinai.org/about/newsroom/2026/mount-sinai-researchers-report-largest-study-supporting-three-courses-of-radiation-for-children-with-deadly-brain-tumor
  - (medical study) [Brown University] 09/03/2026, 03:08 PM, +0000 UTC — Transformative $37 million investment will create alliance to advance breakthroughs in aging research, clinical care
    
    Link: https://www.brown.edu/news/2026-09-03/starr-healthspan-innovation-alliance
  - (medical study) [fda.gov] 09/02/2026, 12:00 AM, +0000 UTC — Good Clinical Practices Are Not Optional
    
    Link: https://www.fda.gov/news-events/fda-voices/good-clinical-practices-are-not-optional-fdas-commitment-human-subject-protections-and-gold-standard
  - (medical study) [Marquette Today] 09/01/2026, 02:07 PM, +0000 UTC — Marquette biomedical engineering professor receives NIH grant to study acute respiratory distress syndrome
    
    Link: https://today.marquette.edu/2026/09/marquette-biomedical-engineering-professor-receives-nih-grant-to-study-acute-respiratory-distress-syndrome/
  - (medical study) [University of Miami] 09/02/2026, 11:31 PM, +0000 UTC — U.S. Cancer Deaths Linked to Alcohol Have Doubled Since 1990, Study Finds
    
    Link: https://news.med.miami.edu/alcohol-related-cancer-deaths-double-us-study/
  - (medical study) [Nature] 09/02/2026, 03:18 PM, +0000 UTC — Robust inference and correlates from genetic associations with personality
    
    Link: https://www.nature.com/articles/s41586-026-10992-9
  - (medical study) [Medical Xpress] 09/04/2026, 03:00 PM, +0000 UTC — Health warnings could reduce young people's social media use, study finds
    
    Link: https://medicalxpress.com/news/2026-09-health-young-people-social-media.html
  - (medical study) [Biogen] 09/03/2026, 04:00 AM, +0000 UTC — LEQEMBI® (lecanemab) Subcutaneous Formulation as an Initiation Treatment for Early Alzheimer’s Disease Approved in China
    
    Link: https://investors.biogen.com/news-releases/news-release-details/leqembir-lecanemab-subcutaneous-formulation-initiation-treatment
  - (medical study) [ABC7 Los Angeles] 09/04/2026, 09:16 PM, +0000 UTC — Could dental floss replace shots? Researchers explore new vaccine delivery method
    
    Link: https://abc7.com/story/could-dental-floss-replace-shots-researchers-explore-new-vaccine-delivery-method/19791257/
  - (clinical trial health) [U.S. News & World Report] 09/03/2026, 03:54 PM, +0000 UTC — America Doesn't Have a Science Problem. It Has a Clinical Trial Problem. | US News Opinion
    
    Link: https://www.usnews.com/opinion/articles/2026-09-03/america-doesnt-have-a-science-problem-it-has-a-clinical-trial-problem
  - (clinical trial health) [Dermatology Advisor] 09/04/2026, 04:00 AM, +0000 UTC — Women in Clinical Trials: History and Impact
    
    Link: https://www.dermatologyadvisor.com/features/women-in-clinical-trials-history-impact/
  - (clinical trial health) [University of Utah Health Academic Medical Center] 09/01/2026, 02:26 PM, +0000 UTC — Research Brings Life-Changing Therapy to Cristofer
    
    Link: https://uofuhealth.utah.edu/newsroom/news/2026/09/research-brings-life-changing-therapy-cristofer
  - (clinical trial health) [World Health Organization (WHO)] 09/04/2026, 08:34 AM, +0000 UTC — Singapore research network appointed WHO collaborating centre to strengthen clinical trials capacity across the region
    
    Link: https://www.who.int/westernpacific/newsroom/feature-stories/item/singapore-research-network-appointed-who-collaborating-centre-to-strengthen-clinical-trials-capacity-across-the-region
  - (clinical trial health) [Jefferson City News Tribune] 09/01/2026, 09:00 AM, +0000 UTC — Joining a clinical trial, hurdles to know about
    
    Link: https://www.newstribune.com/news/2026/sep/01/joining-a-clinical-trial-hurdles-to-know-about/
  - (clinical trial health) [discoverhealth.org] 09/03/2026, 07:18 PM, +0000 UTC — Gibbs oncologists advancing prostate cancer treatment through clinical research
    
    Link: https://www.discoverhealth.org/gibbs-oncologists-advancing-prostate-cancer-treatment-through-clinical-research
  - (clinical trial health) [BioPharma APAC] 08/31/2026, 06:49 PM, +0000 UTC — Data4Life, Monash Health Partner to Accelerate Clinical Trials and Real-World Evidence Generation
    
    Link: https://biopharmaapac.com/news/81/8375/data4life-monash-health-partner-to-accelerate-clinical-trials-and-real-world-evidence-generation.html
  - (clinical trial health) [Yahoo Finance] 09/05/2026, 07:00 AM, +0000 UTC — Evinova and Lothar Medical Announce Strategic Partnership to Modernise Respiratory Clinical Trials with Unified Trial Solution
    
    Link: https://finance.yahoo.com/healthcare/articles/evinova-lothar-medical-announce-strategic-070000977.html
  - (clinical trial health) [Morgan Lewis] 09/03/2026, 04:51 PM, +0000 UTC — Women’s Health: Legal and Commercial Considerations for Companies, Investors, and Strategic Partners
    
    Link: https://www.morganlewis.com/pubs/2026/09/womens-health-legal-and-commercial-considerations-for-companies-investors-and-strategic-partners
  - (clinical trial health) [UCI Health] 09/03/2026, 07:00 AM, +0000 UTC — First-in-human study attacks pancreatic cancer with laser light
    
    Link: https://www.ucihealth.org/blog/2026/09/laser-light-pancreatic-cancer-trial
  - (clinical trial health) [The Pennsylvania State University] 09/01/2026, 01:45 PM, +0000 UTC — NIH awards Penn State CTSI $28.2M to improve rural health
    
    Link: https://www.psu.edu/news/clinical-and-translational-science-institute/story/nih-awards-penn-state-ctsi-282m-improve-rural
  - (clinical trial health) [WPRI.com] 09/03/2026, 10:12 PM, +0000 UTC — Brown gets $37 million for aging research, clinical trials
    
    Link: https://www.wpri.com/health/brown-gets-37-million-for-aging-research-clinical-trials/
  - (FDA recall health) [fda.gov] 09/03/2026, 12:00 AM, +0000 UTC — Outbreak Investigation of E. coli: Frozen Blueberries (July 2026)
    
    Link: https://www.fda.gov/food/outbreaks-foodborne-illness/outbreak-investigation-e-coli-o145h28-frozen-blueberries-july-2026
  - (FDA recall health) [NewsNation] 09/04/2026, 03:36 PM, +0000 UTC — Epinephrine injection recalled over potentially fatal health risks: FDA
    
    Link: https://www.newsnationnow.com/us-news/recalls/epinephrine-injection-recalled-health-risks-fda/
  - (FDA recall health) [Healthline] 09/01/2026, 07:31 PM, +0000 UTC — FDA Recalls IV Fluids Due to Fiberglass, Other Hazardous Materials
    
    Link: https://www.healthline.com/health-news/fda-recalls-iv-saline-fluids-fiberglass-stainless-steel-contaminants
  - (FDA recall health) [CT Mirror] 08/31/2026, 01:00 PM, +0000 UTC — A summer of recalls exposes holes in the nation’s food safety net
    
    Link: https://ctmirror.org/2026/08/31/summer-of-recalls-us-food-safety-net/
  - (FDA recall health) [The New Republic] 08/31/2026, 09:02 PM, +0000 UTC — You’re Not Hallucinating: The Amount of Recalled Food Is Skyrocketing
    
    Link: https://newrepublic.com/post/214946/food-recall-fda-list-august-skyrocket
  - (FDA recall health) [The Healthy @Reader's Digest] 09/02/2026, 09:35 PM, +0000 UTC — New Fruit Recalls Affect Products Sold at Walmart and CVS
    
    Link: https://www.thehealthy.com/news/fruit-recalls-walmart-cvs-september-2026/
  - (FDA recall health) [Health.com] 08/31/2026, 02:24 PM, +0000 UTC — FDA Announces Tofu Recall: More Than 10,000 Cases May Be Contaminated With Ink
    
    Link: https://www.health.com/tofu-recall-august-2026-12073618
  - (FDA recall health) [Fortune] 09/02/2026, 05:41 PM, +0000 UTC — American shoppers are so rattled by surging FDA recalls that 67% now avoid a whole food category after just one notice
    
    Link: https://fortune.com/2026/09/02/food-recalls-fda-americans-avoid-food-categories/
  - (FDA recall health) [Centers for Disease Control and Prevention | CDC (.gov)] 09/03/2026, 07:00 AM, +0000 UTC — Cyclospora Outbreak Linked to Iceberg Lettuce | Cyclosporiasis
    
    Link: https://www.cdc.gov/cyclosporiasis/outbreaks/07-26/index.html
  - (FDA recall health) [fda.gov] 09/03/2026, 02:30 PM, +0000 UTC — Outbreak Investigation of Salmonella: Eggs (July 2026)
    
    Link: https://www.fda.gov/food/outbreaks-foodborne-illness/outbreak-investigation-salmonella-eggs-july-2026
  - (FDA recall health) [The Hill] 09/04/2026, 05:54 PM, +0000 UTC — Epinephrine injection recalled over potentially fatal health risks
    
    Link: https://thehill.com/policy/healthcare/6071686-epinephrine-injection-recalled-fatal-health-risk-fda/
  - (FDA recall health) [Star Tribune] 08/31/2026, 06:01 PM, +0000 UTC — Medtronic recall prompts FDA safety alert after 184 serious injuries
    
    Link: https://www.startribune.com/medtronic-recall-bravo-cf-reflux-gastroesophageal/601883787