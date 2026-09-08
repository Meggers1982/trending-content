# LIVE SIGNAL DATA — SerpAPI Pre-Fetch
The following signals were fetched from SerpAPI Google News and SerpAPI Google Trends immediately before this pipeline run. Treat Google Trends as AVAILABLE when this section contains a Google Trends block. Use it as the primary search_velocity input for Skills 01–05 (Signal Listener through Trend Strength Scorer). Use the Google News Radar as the broad discovery layer for news-led health topics, including topics that do not yet appear in Google Trends. Prioritize topics with convergence across News, Trends, primary/institutional sources, and credible publisher coverage.

## Google Trends — Trending Now (US / Health, real-time)
Terms with a "Why:" line have a confirmed real-world news story driving the spike; terms without one are a real-time signal only, not yet grounded in a specific story.
  - pamela anderson
    Why: "Pamela Anderson on Overcoming Hepatitis C at amfAR Venice: Not a Victim" — Variety

## Google Trends — 7-Day Interest (US)
  - **health**: latest=100, peak=100, 7d-delta=+7
    Rising related: reverse health cost, jim curtis health, brett favre health, emma navarro health issues, how to check hard drive health, how to check ssd health, how to check laptop battery health, how to improve gut health
  - **wellness**: latest=77, peak=100, 7d-delta=-7
    Rising related: wellness darty, jennifer lawrence beauty wellness routine, old word for favor, what is a wellness darty, wellness brand with ceo gwyneth paltrow, old word for favor rhymes with toon, tender gifts birth & wellness center, gwyneth paltrow wellness brand
  - **nutrition**: latest=81, peak=100, 7d-delta=-5
    Rising related: how to read nutrition labels, chipotle pollo asado nutrition, nutrition near me, sp nutrition magnesium bisglycinate gummies reviews, shake shack nutrition, evogen nutrition, 7 brew nutrition facts, crumbl nutrition facts
  - **fitness**: latest=31, peak=100, 7d-delta=-8
    Rising related: planet fitness open on labor day, is planet fitness open on labor day, planet fitness labor day hours, planet fitness labor day, la fitness hours labor day, is crunch fitness open on labor day, crunch fitness labor day hours, is la fitness open on labor day
  - **food safety**: latest=64, peak=100, 7d-delta=-8
    Rising related: washing cabbage food safety tips, wilkerson dining facility food safety, up&up baby wipes safety recall, cracked eggs food safety risks, american shoppers food safety concerns, best thai food near me, walmart product recalls safety alerts, ias brand safety
  - **diet**: latest=84, peak=100, 7d-delta=+2
    Rising related: metabolic psychiatry and keto diet, cell metabolism keto diet study, jd vance weight loss diet, bobby kennedy diet, mediterranean diet pasta dinner recipe, diet with fat bombs, serena williams training day diet, jd vance diet
  - **weight loss**: latest=38, peak=100, 7d-delta=-10
    Rising related: jd vance weight loss white house, sites like princess polly, princess polly dupes, jd vance weight loss, erin burnett weight loss, bella maison, bronson reed weight loss, shop sider
  - **mental health**: latest=87, peak=100, 7d-delta=+6
    Rising related: how ai is changing our lives, coco gauff mental health, is september mental health awareness month, pamela cisneros mental health, september mental health awareness month, how social media affects our mental health, september mental health awareness, the importance of learning languages
  - **gut health**: latest=40, peak=100, 7d-delta=-2
    Rising related: how to improve gut health, improve gut health, hack your health the secrets of your gut, gut health supplements for dogs, what is gut health, gut health foods, probiotics, gut health probiotics

Top rising related queries from Google Trends:
  - reverse health cost
  - jim curtis health
  - brett favre health
  - emma navarro health issues
  - how to check hard drive health
  - how to check ssd health
  - how to check laptop battery health
  - how to improve gut health
  - wellness darty
  - jennifer lawrence beauty wellness routine
  - old word for favor
  - what is a wellness darty
  - wellness brand with ceo gwyneth paltrow
  - old word for favor rhymes with toon
  - tender gifts birth & wellness center
  - gwyneth paltrow wellness brand
  - how to read nutrition labels
  - chipotle pollo asado nutrition
  - nutrition near me
  - sp nutrition magnesium bisglycinate gummies reviews

## Google News Radar — Recent Health Topics (144 unique across 12 queries; showing 60)
Treat these headlines as the broad radar of news-led health topics. The Signal Listener must consider this radar before narrowing to retained candidates.
  - (health) [OpenAI] 09/01/2026, 05:02 PM, +0000 UTC — Healthcare organizations can now connect EHR and additional industry data to ChatGPT
    
    Link: https://openai.com/index/chatgpt-connects-health-records-and-healthcare-sources/
  - (health) [Stanford Medicine] 09/04/2026, 05:18 PM, +0000 UTC — Health warnings could reduce young people’s social media use, Stanford Medicine-led study finds
    
    Link: https://med.stanford.edu/news/all-news/2026/09/social-media-warnings.html
  - (health) [NASA (.gov)] 09/03/2026, 08:57 PM, +0000 UTC — Request for Information: Help Shape Human Health Research for the Future Moon Base
    
    Link: https://www.nasa.gov/hrp/request-for-information-help-shape-human-health-research-for-the-future-moon-base/
  - (health) [NYU Langone Health] 09/03/2026, 12:09 PM, +0000 UTC — Some Hair Loss in Men Is Linked to Use of Weight Loss Drugs
    
    Link: https://nyulangone.org/news/some-hair-loss-men-linked-use-weight-loss-drugs
  - (health) [Source New Mexico] 09/01/2026, 07:50 PM, +0000 UTC — New Mexico insurance superintendent approves 24% premium increase on healthcare exchange plans
    
    Link: https://sourcenm.com/2026/09/01/new-mexico-insurance-superintendent-approves-24-premium-increase-on-healthcare-exchange-plans/
  - (health) [U.S. Government Accountability Office (.gov)] 09/01/2026, 06:16 PM, +0000 UTC — VA Electronic Health Record Modernization: Actions Needed to Sustain Accelerated System Deployments
    
    Link: https://www.gao.gov/products/gao-26-109393
  - (health) [WBAL-TV] 09/03/2026, 11:21 AM, +0000 UTC — Luminis Health cyber-attack disrupts Anne Arundel Medical Center
    
    Link: https://www.wbaltv.com/article/anne-arundel-medical-center-cyberattack/73596317
  - (health) [NPR] 09/04/2026, 08:41 PM, +0000 UTC — 'The health system in Nepal is not prepared for this'
    
    Link: https://www.npr.org/2026/09/04/nx-s1-5954050/nepal-flood-waters-physical-mental-health
  - (health) [Flathead Beacon] 09/04/2026, 08:15 PM, +0000 UTC — Logan Health Primary Care Providers Sign Vote of ‘No Confidence’ in Leadership
    
    Link: https://flatheadbeacon.com/2026/09/04/logan-health-primary-care-providers-sign-vote-of-no-confidence-in-leadership/
  - (health) [Think Global Health] 09/03/2026, 07:00 AM, +0000 UTC — Tracking Measles and the World's Vaccine-Preventable Diseases
    
    Link: https://www.thinkglobalhealth.org/article/vaccine-preventable-disease-a-global-tracker
  - (health) [Axios] 09/04/2026, 09:32 AM, +0000 UTC — Large employers drop health benefits as costs rise
    
    Link: https://www.axios.com/2026/09/04/employer-health-insurance-benefit-cut-costs
  - (health) [mercer.com] 09/08/2026, 01:56 PM, +0000 UTC — Survey: Health benefit costs expected to jump 8.2% in 2027, the biggest increase since 2003
    
    Link: https://www.mercer.com/en-us/insights/us-health-news/survey-health-benefit-costs-expected-to-jump-in-2027/
  - (wellness) [Employment Law Worldview] 09/03/2026, 06:58 PM, +0000 UTC — Quitting Cold Turkey: Federal Agencies Suspend Enforcement of Back-Pay Requirement for Employee Wellness Incentives, Including Tobacco Cessation Programs (US)
    
    Link: https://www.employmentlawworldview.com/quitting-cold-turkey-federal-agencies-suspend-enforcement-of-back-pay-requirement-for-employee-wellness-incentives-including-tobacco-cessation-programs-us/
  - (wellness) [VA News (.gov)] 09/02/2026, 07:00 AM, +0000 UTC — Five organizations with Veterans wellness at the heart of their mission
    
    Link: https://news.va.gov/149155/organizations-veterans-wellness-heart-mission/
  - (wellness) [Fairfield University] 09/04/2026, 07:00 AM, +0000 UTC — SEHD Hosts Second Annual Educator Resiliency and Wellness Institute
    
    Link: https://www.fairfield.edu/news/2026/september/second-educator-resiliency-wellness-institute.html
  - (wellness) [Illinois State University News] 09/04/2026, 01:36 PM, +0000 UTC — Skate Park Saturdays create space for wellness and connection
    
    Link: https://news.illinoisstate.edu/2026/09/skate-park-saturdays-create-space-for-wellness-and-connection/
  - (wellness) [IN.gov] 09/02/2026, 10:32 PM, +0000 UTC — Invest in Your Health (State Employee Wellness Program): Optum EAP - Suicide prevention and recovery
    
    Link: https://www.in.gov/investinyourhealth/post/optum-eap-suicide-prevention-and-recovery
  - (wellness) [San Francisco 49ers] 09/06/2026, 04:05 AM, +0000 UTC — 49ers Prepare Educators to Build Positive Sports Culture Through Mental Wellness
    
    Link: https://www.49ers.com/photos/49ers-prepare-educators-to-build-positive-sports-culture-through-mental-wellness
  - (wellness) [Geauga County Maple Leaf] 09/02/2026, 06:43 PM, +0000 UTC — Inaugural Conference Puts First Responder Wellness in Focus
    
    Link: https://www.geaugamapleleaf.com/news/inaugural-conference-puts-first-responder-wellness-in-focus/
  - (wellness) [Purdue University College of Veterinary Medicine] 09/04/2026, 04:55 PM, +0000 UTC — “Paws Up” for Jennifer Danaher – brought to you by the PVM Wellness Committee
    
    Link: https://vet.purdue.edu/news/paws-up-for-jennifer-danaher-brought-to-you-by-the-pvm-wellness-committee.php
  - (wellness) [The University of Maryland, Baltimore] 09/05/2026, 02:40 AM, +0000 UTC — Sept. 14 - 20: Celebrate National Wellness Week with the Wellness Committee
    
    Link: https://elm.umaryland.edu/announcements/2026/Sept-14---20-Celebrate-National-Wellness-Week-with-the-Wellness-Committee.php
  - (wellness) [The New York Times] 09/02/2026, 09:02 AM, +0000 UTC — I Need an IV Drip to Recover From My IV Drip
    
    Link: https://www.nytimes.com/2026/09/02/magazine/iv-drip-vitamin-wellness.html
  - (wellness) [ABC30 Fresno] 09/04/2026, 01:01 AM, +0000 UTC — Study finds young women more likely than men to get health and wellness information from influencers
    
    Link: https://abc30.com/post/study-finds-young-women-more-men-get-health-wellness-information-influencers/19775744/
  - (wellness) [Norwegian Cruise Line Holdings Ltd.] 09/02/2026, 08:23 PM, +0000 UTC — Regent Seven Seas Cruises® Unveils Largest-Ever Spa and Wellness Experience Aboard Seven Seas Prestige
    
    Link: https://www.nclhltd.com/news-media/press-releases/detail/820/regent-seven-seas-cruises-unveils-largest-ever-spa-and
  - (medical study) [News-Medical] 09/07/2026, 03:13 PM, +0000 UTC — AI-designed drug candidate reverses biological age in clinical study
    
    Link: https://www.news-medical.net/news/20260907/AI-designed-drug-candidate-reverses-biological-age-in-clinical-study.aspx
  - (medical study) [American Medical Association | AMA] 09/04/2026, 12:06 PM, +0000 UTC — Using AI to study: Medical students should know the do’s and don’ts
    
    Link: https://www.ama-assn.org/medical-students/succeed-medical-school/using-ai-study-medical-students-should-know-do-s-and-don-ts
  - (medical study) [University of Nebraska Medical Center] 09/08/2026, 01:49 PM, +0000 UTC — Medical research highlights, September 2026
    
    Link: https://www.unmc.edu/newsroom/2026/09/08/medical-research-highlights-september-2026/
  - (medical study) [Nature] 09/03/2026, 06:00 PM, +0000 UTC — A five-phase evaluation framework for diagnostic and predictive medical artificial intelligence
    
    Link: https://www.nature.com/articles/s41746-026-03155-7
  - (medical study) [UAMS News] 09/04/2026, 02:26 PM, +0000 UTC — UAMS Part of Clinical Study Exploring Blood Pressure Instability Treatment for People With Spinal Cord Injury
    
    Link: https://news.uams.edu/2026/09/04/uams-part-of-clinical-study-exploring-blood-pressure-instability-treatment-for-people-with-spinal-cord-injury/
  - (medical study) [brown.edu] 09/03/2026, 03:08 PM, +0000 UTC — Transformative $37 million investment will create alliance to advance breakthroughs in aging research, clinical care
    
    Link: https://www.brown.edu/news/2026-09-03/starr-healthspan-innovation-alliance
  - (medical study) [University of Miami] 09/02/2026, 11:31 PM, +0000 UTC — U.S. Cancer Deaths Linked to Alcohol Have Doubled Since 1990, Study Finds
    
    Link: https://news.med.miami.edu/alcohol-related-cancer-deaths-double-us-study/
  - (medical study) [Yahoo Finance] 09/03/2026, 05:30 AM, +0000 UTC — ONWARD Medical Announces First Implant in New Clinical Feasibility Study Evaluating ARC-IM System to Restore Mobility After Spinal Cord Injury
    
    Link: https://finance.yahoo.com/healthcare/articles/onward-medical-announces-first-implant-053000099.html
  - (medical study) [fda.gov] 09/02/2026, 12:00 AM, +0000 UTC — Good Clinical Practices Are Not Optional
    
    Link: https://www.fda.gov/news-events/fda-voices/good-clinical-practices-are-not-optional-fdas-commitment-human-subject-protections-and-gold-standard
  - (medical study) [MedPage Today] 09/04/2026, 06:32 PM, +0000 UTC — Docs Alarmed by NIH Plan to Redirect Medical Research $$ to Pentagon
    
    Link: https://www.medpagetoday.com/washington-watch/washington-watch/122903
  - (medical study) [Medical Xpress] 09/02/2026, 02:00 PM, +0000 UTC — Urine test identifies more than nine in ten bladder cancers, clinical study finds
    
    Link: https://medicalxpress.com/news/2026-09-urine-ten-bladder-cancers-clinical.html
  - (medical study) [University of Rochester] 09/08/2026, 11:57 AM, +0000 UTC — Nearly One in Five Pediatric Psychiatric Crises Involve Digital Media, New Study Finds
    
    Link: https://www.urmc.rochester.edu/news/story/nearly-one-in-five-pediatric-psychiatric-crises-involve-digital-media-new-study-finds
  - (clinical trial health) [U.S. News & World Report] 09/03/2026, 03:54 PM, +0000 UTC — America Doesn't Have a Science Problem. It Has a Clinical Trial Problem. | US News Opinion
    
    Link: https://www.usnews.com/opinion/articles/2026-09-03/america-doesnt-have-a-science-problem-it-has-a-clinical-trial-problem
  - (clinical trial health) [Dermatology Advisor] 09/04/2026, 04:00 AM, +0000 UTC — Women in Clinical Trials: History and Impact
    
    Link: https://www.dermatologyadvisor.com/features/women-in-clinical-trials-history-impact/
  - (clinical trial health) [The Clinical Trial Vanguard] 09/06/2026, 06:47 AM, +0000 UTC — Signant Health, Lothar Medical Plan Integrated Respiratory Trial Device
    
    Link: https://www.clinicaltrialvanguard.com/news/signant-health-lothar-medical-plan-integrated-respiratory-trial-device/
  - (clinical trial health) [World Health Organization (WHO)] 09/04/2026, 08:34 AM, +0000 UTC — Singapore research network appointed WHO collaborating centre to strengthen clinical trials capacity across the region
    
    Link: https://www.who.int/westernpacific/newsroom/feature-stories/item/singapore-research-network-appointed-who-collaborating-centre-to-strengthen-clinical-trials-capacity-across-the-region
  - (clinical trial health) [nytimes.com] 09/04/2026, 09:00 AM, +0000 UTC — Opinion | This Is the Biggest Obstacle to New Cancer Cures
    
    Link: https://www.nytimes.com/2026/09/04/opinion/clinical-trials-drugs-science.html
  - (clinical trial health) [Penn State Health News] 09/08/2026, 03:03 PM, +0000 UTC — NIH awards Penn State CTSI $28.2M to improve rural health
    
    Link: https://pennstatehealthnews.org/2026/09/nih-awards-penn-state-ctsi-28-2m-to-improve-rural-health/
  - (clinical trial health) [Clinical Leader] 09/04/2026, 04:20 AM, +0000 UTC — 5 Ways To Enrich The Clinical Trial Ecosystem
    
    Link: https://www.clinicalleader.com/doc/ways-to-enrich-the-clinical-trial-ecosystem-0001
  - (clinical trial health) [ABC News - Breaking News, Latest News and Videos] 09/05/2026, 09:31 AM, +0000 UTC — Moderna begins Phase 1 clinical trial of Ebola vaccine against strain behind DRC outbreak
    
    Link: https://abcnews.com/Health/moderna-begins-phase-1-clinical-trial-ebola-vaccine/story?id=135365177
  - (clinical trial health) [UCI Health] 09/03/2026, 07:00 AM, +0000 UTC — First-in-human study attacks pancreatic cancer with laser light
    
    Link: https://www.ucihealth.org/blog/2026/09/laser-light-pancreatic-cancer-trial
  - (clinical trial health) [WPRI.com] 09/03/2026, 10:12 PM, +0000 UTC — Brown gets $37 million for aging research, clinical trials
    
    Link: https://www.wpri.com/health/brown-gets-37-million-for-aging-research-clinical-trials/
  - (clinical trial health) [the-scientist.com] 09/02/2026, 04:15 AM, +0000 UTC — Cancer Clinical Trials Are Excluding the Patients They Are Meant to Help
    
    Link: https://www.the-scientist.com/cancer-clinical-trials-are-excluding-the-patients-they-are-meant-to-help-74951
  - (clinical trial health) [Yahoo Finance] 09/05/2026, 07:00 AM, +0000 UTC — Evinova and Lothar Medical Announce Strategic Partnership to Modernise Respiratory Clinical Trials with Unified Trial Solution
    
    Link: https://finance.yahoo.com/healthcare/articles/evinova-lothar-medical-announce-strategic-070000977.html
  - (FDA recall health) [fda.gov] 09/03/2026, 12:00 AM, +0000 UTC — Outbreak Investigation of E. coli: Frozen Blueberries (July 2026)
    
    Link: https://www.fda.gov/food/outbreaks-foodborne-illness/outbreak-investigation-e-coli-o145h28-frozen-blueberries-july-2026
  - (FDA recall health) [newsnationnow.com] 09/04/2026, 03:36 PM, +0000 UTC — Epinephrine injection recalled over potentially fatal health risks: FDA
    
    Link: https://www.newsnationnow.com/us-news/recalls/epinephrine-injection-recalled-health-risks-fda/
  - (FDA recall health) [Healthline] 09/01/2026, 07:31 PM, +0000 UTC — FDA Recalls IV Fluids Due to Fiberglass, Other Hazardous Materials
    
    Link: https://www.healthline.com/health-news/fda-recalls-iv-saline-fluids-fiberglass-stainless-steel-contaminants
  - (FDA recall health) [The Hill] 09/04/2026, 05:54 PM, +0000 UTC — Epinephrine injection recalled over potentially fatal health risks
    
    Link: https://thehill.com/policy/healthcare/6071686-epinephrine-injection-recalled-fatal-health-risk-fda/
  - (FDA recall health) [fortune.com] 09/02/2026, 05:41 PM, +0000 UTC — American shoppers are so rattled by surging FDA recalls that 67% now avoid a whole food category after just one notice
    
    Link: https://fortune.com/2026/09/02/food-recalls-fda-americans-avoid-food-categories/
  - (FDA recall health) [The Healthy @Reader's Digest] 09/02/2026, 09:35 PM, +0000 UTC — New Fruit Recalls Affect Products Sold at Walmart and CVS
    
    Link: https://www.thehealthy.com/news/fruit-recalls-walmart-cvs-september-2026/
  - (FDA recall health) [Centers for Disease Control and Prevention | CDC (.gov)] 09/03/2026, 07:00 AM, +0000 UTC — Cyclospora Outbreak Linked to Iceberg Lettuce | Cyclosporiasis
    
    Link: https://www.cdc.gov/cyclosporiasis/outbreaks/07-26/index.html
  - (FDA recall health) [fda.gov] 09/03/2026, 02:30 PM, +0000 UTC — Outbreak Investigation of Salmonella: Eggs (July 2026)
    
    Link: https://www.fda.gov/food/outbreaks-foodborne-illness/outbreak-investigation-salmonella-eggs-july-2026
  - (FDA recall health) [nytimes.com] 09/05/2026, 09:06 PM, +0000 UTC — E. Coli Illnesses Linked to Frozen Blueberries Rise to 17, F.D.A. Says
    
    Link: https://www.nytimes.com/2026/09/05/health/frozen-blueberries-recall-e-coli.html
  - (FDA recall health) [EatingWell] 09/03/2026, 04:47 PM, +0000 UTC — The FDA Issued a Recall on Tofu Due to Potential Chemical Contamination
    
    Link: https://www.eatingwell.com/tofu-recall-chemical-contamination-12097001
  - (FDA recall health) [LiveNOW from FOX] 09/02/2026, 01:24 PM, +0000 UTC — Recalled weight loss products are tainted with toxic substance, FDA says
    
    Link: https://www.livenowfox.com/news/recalled-weight-loss-products-tainted-toxic-substance-fda-says
  - (FDA recall health) [aol.com] 09/01/2026, 08:20 PM, +0000 UTC — FDA Announces Nationwide Recall of Popular Dog and Cat Food
    
    Link: https://www.aol.com/articles/fda-announces-nationwide-recall-popular-202017000.html