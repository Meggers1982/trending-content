# LIVE SIGNAL DATA — SerpAPI Pre-Fetch
The following signals were fetched from SerpAPI Google News and SerpAPI Google Trends immediately before this pipeline run. Treat Google Trends as AVAILABLE when this section contains a Google Trends block. Use it as the primary search_velocity input for Skills 01–05 (Signal Listener through Trend Strength Scorer). Use the Google News Radar as the broad discovery layer for news-led health topics, including topics that do not yet appear in Google Trends. Prioritize topics with convergence across News, Trends, primary/institutional sources, and credible publisher coverage.

## Google Trends — Trending Now (US / Health, real-time)
Terms with a "Why:" line have a confirmed real-world news story driving the spike; terms without one are a real-time signal only, not yet grounded in a specific story.
  - infection
    Why: "These common infections can cause cancer. Here’s what can lower your risk." — The Washington Post
  - endeavor health
    Why: "Rush University System for Health and Endeavor Health announce plans to merge" — WGN-TV

## Google Trends — 7-Day Interest (US)
  - **health**: latest=100, peak=100, 7d-delta=+8
    Rising related: talarico mental health, mike ditka health, mike love health, world mental health day 2026, world mental health day, mental health day, mental health, health care
  - **wellness**: latest=50, peak=100, 7d-delta=-1
    Rising related: little luxe wellness lodge, elemental wellness club, spa and wellness locations, cure for wellness, a cure for wellness, wellness gadgets, the cure for wellness, ai agents
  - **nutrition**: latest=92, peak=100, 7d-delta=-5
    Rising related: supplemental nutrition assistance program new rules, sava nutrition, organised nutrition, nutrition solutions, dave's hot chicken nutrition, nutrition facts, what is nutrition, nutrition label
  - **fitness**: latest=13, peak=100, 7d-delta=-1
    Rising related: fitness tracker review, web hosting comparison, travel insurance comparison, electric bike review, solar panel cost, standing desk review, cheap flights new york, electric cars comparison
  - **food safety**: latest=84, peak=100, 7d-delta=+4
    Rising related: dented cans food safety risks, baris yucel food safety fine, national registry of food safety professionals, food safety certification texas, what does haccp stand for in food safety, regulations establish the floor for safety in childcare., what is food safety, food safety certification
  - **diet**: latest=95, peak=100, 7d-delta=-4
    Rising related: walter willett diet, diet soda weight management study, walter willett daily diet, university of liverpool diet soda study, the fatal diet meals short drama, pink diet coke cans, diet coke onesie adult, pink diet coke
  - **weight loss**: latest=55, peak=100, 7d-delta=-2
    Rising related: susan dell weight loss, american housewife, katy mixon weight loss, eric stonestreet weight loss, shane gillis weight loss, katy mixon, erin burnett weight loss, erin burnett
  - **mental health**: latest=85, peak=100, 7d-delta=+0
    Rising related: talarico mental health facility, talarico mental health, talarico, james talarico, james talarico mental health, rj mitte mental health, selma blair mental health, is talarico in a mental health facility
  - **gut health**: latest=49, peak=100, 7d-delta=+4
    Rising related: fermented food for gut health, recommend the best fermented foods to add to a daily diet for gut health, best probiotic foods for gut health, good gut health, what is gut health, gut health foods, gut health probiotics, probiotics

Top rising related queries from Google Trends:
  - talarico mental health
  - mike ditka health
  - mike love health
  - world mental health day 2026
  - world mental health day
  - mental health day
  - mental health
  - health care
  - little luxe wellness lodge
  - elemental wellness club
  - spa and wellness locations
  - cure for wellness
  - a cure for wellness
  - wellness gadgets
  - the cure for wellness
  - ai agents
  - supplemental nutrition assistance program new rules
  - sava nutrition
  - organised nutrition
  - nutrition solutions

## Google News Radar — Recent Health Topics (144 unique across 12 queries; showing 60)
Treat these headlines as the broad radar of news-led health topics. The Signal Listener must consider this radar before narrowing to retained candidates.
  - (health) [blog.google] 10/12/2026, 01:11 PM, +0000 UTC — How we’re making Google Health and Fitbit Air smarter than ever
    
    Link: https://blog.google/products-and-platforms/products/google-health/fitbit-google-health-updates/
  - (health) [World Health Organization (WHO)] 10/09/2026, 10:55 AM, +0000 UTC — WHO urges shift from institutional to community-based mental health care
    
    Link: https://www.who.int/news/item/09-10-2026-who-urges-shift-from-institutional-to-community-based-mental-health-care
  - (health) [OHSU News] 10/09/2026, 04:20 PM, +0000 UTC — Late-night eating may be bad for your liver, study suggests
    
    Link: https://news.ohsu.edu/2026/10/09/late-night-eating-may-be-bad-for-your-liver-study-suggests
  - (health) [PBS] 10/13/2026, 05:35 PM, +0000 UTC — Texas health agency proposes eliminating children’s autism program
    
    Link: https://www.pbs.org/newshour/health/texas-health-agency-proposes-eliminating-childrens-autism-program
  - (health) [European Commission] 10/10/2026, 07:10 AM, +0000 UTC — World Mental Health Day: let’s talk and listen
    
    Link: https://commission.europa.eu/news-and-media/news/world-mental-health-day-lets-talk-and-listen-2026-10-10_en
  - (health) [Vatican News] 10/10/2026, 11:50 AM, +0000 UTC — Rome hosts mental health roundtable inspired by Pope’s prayer intention
    
    Link: https://www.vaticannews.va/en/vatican-city/news/2026-10/mental-health-roundtable-in-rome-inspired-popes-prayer-intention.html
  - (health) [NPR] 10/08/2026, 09:00 AM, +0000 UTC — Medical debt is crushing hospital patients in LA. Health officials may have a fix
    
    Link: https://www.npr.org/2026/10/08/nx-s1-5991633/hospital-california-healthcare-medical-debt
  - (health) [University of Utah Health] 10/13/2026, 05:00 PM, +0000 UTC — University of Utah Health Receives Board Approval to Acquire Land at Salt Lake City’s Power District for New Redwood Health Center
    
    Link: https://healthcare.utah.edu/press-releases/2026/10/university-of-utah-health-receives-board-approval-acquire-land-salt-lake
  - (health) [Notre Dame News] 10/08/2026, 05:54 PM, +0000 UTC — Study finds positive parenting teaches children how to experience joy—and could lead to better mental health
    
    Link: https://news.nd.edu/news/study-finds-positive-parenting-teaches-children-how-to-experience-joyand-could-lead-to-better-mental-health/
  - (health) [The New York Times] 10/07/2026, 06:36 PM, +0000 UTC — A Public Health-Minded Senator Asks: What Comes After Trump and Kennedy?
    
    Link: https://www.nytimes.com/2026/10/07/us/politics/patty-murray-public-health.html
  - (health) [KFF Health News] 10/09/2026, 09:00 AM, +0000 UTC — AI, Tech Leaders Are Lobbying Trump Health Officials in a Government-Run Chat Room
    
    Link: https://kffhealthnews.org/health-industry/ai-tech-lobbying-medicare-medical-records-apps-trump-cms-slack-fda/
  - (health) [Reuters] 10/13/2026, 11:17 PM, +0000 UTC — EXCLUSIVE: Galderma agrees to buy ZO Skin Health for around $1.5 billion, sources say
    
    Link: https://www.reuters.com/world/galderma-agrees-buy-zo-skin-health-around-15-billion-sources-say-2026-10-13/
  - (wellness) [shrewsbury-ma.gov] 10/08/2026, 12:29 AM, +0000 UTC — Winter Wellness Presentation - October 2026
    
    Link: https://shrewsburyma.gov/CivicAlerts.aspx?AID=9770
  - (wellness) [The New York Times] 10/07/2026, 06:41 PM, +0000 UTC — Video: Wellness Culture Is Coming for Polyester
    
    Link: https://www.nytimes.com/video/style/100000011173558/wellness-culture-is-coming-for-polyester.html
  - (wellness) [San Diego County News Center] 10/08/2026, 09:02 PM, +0000 UTC — Mental Wellness Begins with a Moment, Don’t Wait to Take Yours
    
    Link: https://www.countynewscenter.com/mental-wellness-begins-with-a-moment-dont-wait-to-take-yours/
  - (wellness) [Yahoo Creators] 10/09/2026, 09:27 PM, +0000 UTC — Wellness stacking: why psychologists say it beats willpower for building healthy habits
    
    Link: https://creators.yahoo.com/lifestyle/story/wellness-stacking-why-psychologists-say-it-beats-willpower-for-building-healthy-habits-015140677.html
  - (wellness) [SBU News] 10/08/2026, 07:50 PM, +0000 UTC — Feeling Better, Working Better: Employee Wellness Fair Connects Stony Brook Employees with Resources
    
    Link: https://news.stonybrook.edu/university/feeling-better-working-better-employee-wellness-fair-connects-stony-brook-employees-with-resources/
  - (wellness) [New York Post] 10/12/2026, 03:26 PM, +0000 UTC — Exclusive | Gen Z turns college ‘wellness darties’ trend into big business: ‘We have a different mindset’
    
    Link: https://nypost.com/2026/10/12/lifestyle/how-wellness-darties-became-big-business-on-college-campuses/
  - (wellness) [FBI (.gov)] 10/14/2026, 02:39 PM, +0000 UTC — Wellness and Resilience Takeaways from FBI National Academy Session 299 — FBI
    
    Link: https://www.fbi.gov/video-repository/wellness-and-resilience-takeaways-from-fbi-national-academy-session-299-101426.mp4/view
  - (wellness) [Case Western Reserve University] 10/08/2026, 11:00 AM, +0000 UTC — Complete fall wellness activities to earn incentives in 2027
    
    Link: https://case.edu/news/complete-fall-wellness-activities-earn-incentives-2027
  - (wellness) [Talk Business & Politics] 10/13/2026, 04:35 PM, +0000 UTC — Beyond Wellness opens in Rogers
    
    Link: https://talkbusiness.net/2026/10/beyond-wellness-opens-in-rogers/
  - (wellness) [The Santa Barbara Independent] 10/09/2026, 04:52 AM, +0000 UTC — Santa Barbara Neighborhood Clinics Hosts 1st Annual Health & Wellness Fair Featuring DJ Darla, Aztec Dancers, and Hourly Games
    
    Link: https://www.independent.com/2026/10/08/santa-barbara-neighborhood-clinics-hosts-1st-annual-health-wellness-fair-featuring-dj-darla-aztec-dancers-and-hourly-games/
  - (wellness) [Army.mil] 10/08/2026, 04:02 PM, +0000 UTC — Ready anywhere: How virtual wellness coaching fits military life
    
    Link: https://www.army.mil/article/296026/ready_anywhere_how_virtual_wellness_coaching_fits_military_life
  - (wellness) [Centene Corporation] 10/13/2026, 10:18 PM, +0000 UTC — PA Health & Wellness Earns National Recognition Among Top Medicaid Health Plans for Second Consecutive Year
    
    Link: https://investors.centene.com/2026-10-13-PA-Health-Wellness-Earns-National-Recognition-Among-Top-Medicaid-Health-Plans-for-Second-Consecutive-Year
  - (medical study) [Nature] 10/13/2026, 10:23 AM, +0000 UTC — Human–artificial intelligence collaboration for comanaging epilepsy in real time
    
    Link: https://www.nature.com/articles/s41591-026-04680-4
  - (medical study) [UT Southwestern] 10/12/2026, 02:31 PM, +0000 UTC — Protein puts brakes on intestinal inflammation, UTSW study finds: Newsroom
    
    Link: https://www.utsouthwestern.edu/newsroom/articles/year-2026/oct-protein-intestinal-inflammation.html
  - (medical study) [University of Cincinnati] 10/09/2026, 10:59 PM, +0000 UTC — UC researcher to launch national study with $2.5 million NIH grant
    
    Link: https://www.uc.edu/news/articles/2026/10/uc-researcher-to-launch-national-study-with-25-million-nih-grant.html
  - (medical study) [The New York Times] 10/08/2026, 10:30 PM, +0000 UTC — Clinical Trial Indicates A.I. Chatbots Could Aid Urgent Care
    
    Link: https://www.nytimes.com/2026/10/08/technology/ai-chatbots-urgent-care.html
  - (medical study) [Azusa Pacific University] 10/12/2026, 08:12 AM, +0000 UTC — Student Spotlight: Mia Pierce ’27 Prepares for Career in Medical Research
    
    Link: https://www.apu.edu/articles/mia-pierce-prepares-for-career-in-medical-research/
  - (medical study) [Harvard Medical School] 10/13/2026, 12:00 PM, +0000 UTC — A Real-World Study of Patient-Facing AI in Primary Care
    
    Link: https://hms.harvard.edu/news/real-world-study-patient-facing-ai-primary-care
  - (medical study) [News-Medical] 10/07/2026, 07:35 PM, +0000 UTC — Study uncovers a protective role for microglia in Parkinson's disease
    
    Link: https://www.news-medical.net/news/20261007/Study-uncovers-a-protective-role-for-microglia-in-Parkinsons-disease.aspx
  - (medical study) [Medical Xpress] 10/13/2026, 05:20 PM, +0000 UTC — Ketamine relieves pain without 'disconnecting' consciousness, study finds
    
    Link: https://medicalxpress.com/news/2026-10-ketamine-relieves-pain-disconnecting-consciousness.html
  - (medical study) [University of Michigan Health] 10/13/2026, 12:00 PM, +0000 UTC — Depression in OBGYN residents needs more attention, study suggests
    
    Link: https://www.uofmhealth.org/health-lab/depression-obgyn-residents-needs-more-attention-study-suggests
  - (medical study) [Texas Public Radio | TPR] 10/11/2026, 03:00 PM, +0000 UTC — Science & Medicine: UT Health San Antonio study finds magnetic stimulation significantly reduces combat PTSD symptoms
    
    Link: https://www.tpr.org/podcast/petrie-dish/2026-10-11/science-medicine-ut-health-san-antonio-study-finds-magnetic-stimulation-significantly-reduces-combat-ptsd-symptoms
  - (medical study) [Today@Wayne] 10/14/2026, 03:04 PM, +0000 UTC — Dr. Levy receives two research awards in single week
    
    Link: https://today.wayne.edu/medicine/news/2026/10/14/dr-levy-receives-two-research-awards-in-single-week-70349
  - (medical study) [Kean University] 10/09/2026, 07:00 AM, +0000 UTC — Kean Professor Expands Orthopaedic Research Through New Grant
    
    Link: https://www.kean.edu/news/kean-professor-expands-orthopaedic-research-through-new-grant
  - (clinical trial health) [The Clinical Trial Vanguard] 10/09/2026, 06:55 AM, +0000 UTC — Patient-Owned Health Data Model Reduces Clinical Trial Recruitment Redundancy
    
    Link: https://www.clinicaltrialvanguard.com/news/patient-owned-health-data-model-reduces-clinical-trial-recruitment-redundancy/
  - (clinical trial health) [Amazon Web Services (AWS)] 10/13/2026, 04:33 PM, +0000 UTC — The 83% problem: Why clinical trials fail the Global South and how we can close the equity gap
    
    Link: https://aws.amazon.com/blogs/social-impact/the-83-percent-problem-why-clinical-trials-fail-the-global-south-and-how-we-can-close-the-equity-gap/
  - (clinical trial health) [Clinical Leader] 10/13/2026, 05:18 AM, +0000 UTC — Can A Universal Health Screening Help Stop Clinical Trial Dropouts?
    
    Link: https://www.clinicalleader.com/doc/can-a-universal-health-screening-help-stop-clinical-trial-dropouts-0001
  - (clinical trial health) [Clinical Trials Arena] 10/12/2026, 04:53 PM, +0000 UTC — Women’s health landscape shifting, but systemic hurdles remain
    
    Link: https://www.clinicaltrialsarena.com/features/womens-health-landscape-shifting-systemic-hurdles-remain-2/
  - (clinical trial health) [Milken Institute] 10/13/2026, 04:02 PM, +0000 UTC — Enabling Access to Clinical Research: An Action Plan for Policy and Practice Change
    
    Link: https://milkeninstitute.org/content-hub/research-and-reports/reports/enabling-access-clinical-research-action-plan-policy-and-practice-change
  - (clinical trial health) [The Daily Texan] 10/13/2026, 03:42 AM, +0000 UTC — Dell Medical School partners with federal program to standardize clinical trials
    
    Link: https://thedailytexan.com/2026/10/12/dell-medical-school-partners-with-federal-program-to-standardize-clinical-trials/
  - (clinical trial health) [Penn LDI] 10/12/2026, 04:41 PM, +0000 UTC — What Would It Take to Make Clinical Trials More Diverse?
    
    Link: https://ldi.upenn.edu/our-work/research-updates/what-would-it-take-to-make-clinical-trials-more-diverse/
  - (clinical trial health) [PR Newswire] 10/08/2026, 01:15 PM, +0000 UTC — Verana Health and Bitfount Collaborate to Simplify Prescreening for Ophthalmic Clinical Trials
    
    Link: https://www.prnewswire.com/news-releases/verana-health-and-bitfount-collaborate-to-simplify-prescreening-for-ophthalmic-clinical-trials-302901571.html
  - (clinical trial health) [Bulletin of the Atomic Scientists] 10/13/2026, 10:42 PM, +0000 UTC — How prediction markets could distort drug approvals
    
    Link: https://thebulletin.org/2026/10/how-prediction-markets-could-distort-drug-approvals/
  - (clinical trial health) [Keck Medicine of USC] 10/14/2026, 11:00 AM, +0000 UTC — Clinical trial evaluates investigational injection for knee osteoarthritis
    
    Link: https://news.keckmedicine.org/clinical-trial-evaluates-investigational-injection-for-knee-osteoarthritis/
  - (clinical trial health) [Business Wire] 10/13/2026, 12:00 PM, +0000 UTC — IgniteData and RealTime Announce Partnership to Expand Clinical Trial Data Transfer Capabilities Across Clinical Research Organizations in the U.S. and Key Global Markets
    
    Link: https://www.businesswire.com/news/home/20261013274056/en/IgniteData-and-RealTime-Announce-Partnership-to-Expand-Clinical-Trial-Data-Transfer-Capabilities-Across-Clinical-Research-Organizations-in-the-U.S.-and-Key-Global-Markets
  - (clinical trial health) [GlobeNewswire] 10/13/2026, 05:00 PM, +0000 UTC — Medical Marijuana Clinical Trial Landscape Expands as 60+
    
    Link: https://www.globenewswire.com/news-release/2026/10/13/3380030/0/en/medical-marijuana-clinical-trial-landscape-expands-as-60-leading-companies-accelerate-drug-development-delveinsight.html
  - (FDA recall health) [NEWStalk 870] 10/09/2026, 08:34 PM, +0000 UTC — Baby-Infant Sleep Aid Recalled by FDA Over Undisclosed Alcohol Content
    
    Link: https://newstalk870.am/fda-recalls-baby-infant-sleep-aid/
  - (FDA recall health) [Prevention] 10/08/2026, 02:56 PM, +0000 UTC — Millions of Bottles of Eye Drops Recalled Nationwide, FDA Warns
    
    Link: https://www.prevention.com/health/a74079654/fda-updates-eye-drop-recall/
  - (FDA recall health) [WPLG Local 10] 10/09/2026, 08:16 PM, +0000 UTC — FDA: Gatorade recalls 122,000 cases over food dyes
    
    Link: https://www.local10.com/food/2026/10/09/fda-gatorade-recalls-122000-cases-over-food-dyes/
  - (FDA recall health) [Fox 59] 10/08/2026, 02:12 PM, +0000 UTC — Baby product recalled over alcohol content: FDA
    
    Link: https://fox59.com/news/national-world/baby-product-recalled-over-alcohol-content-fda/
  - (FDA recall health) [Yahoo] 10/12/2026, 07:55 PM, +0000 UTC — FDA Announces Recall of Smoked Fish Sold in 6 States
    
    Link: https://www.yahoo.com/news/us/articles/fda-announces-recall-smoked-fish-195520545.html
  - (FDA recall health) [WVTM Channel 13] 10/12/2026, 09:21 AM, +0000 UTC — FDA: Baby supplement sold online recalled after testing discovers undeclared alcohol
    
    Link: https://www.wvtm13.com/article/baby-product-sold-online-recall-undeclared-alcohol/74105221
  - (FDA recall health) [The Healthy @Reader's Digest] 10/09/2026, 05:35 AM, +0000 UTC — Supplement Powder Recall: FDA Warns of Potential ‘Cardiovascular Problems’
    
    Link: https://www.thehealthy.com/news/supplement-powder-recall-october-2026/
  - (FDA recall health) [ABC News - Breaking News, Latest News and Videos] 10/09/2026, 03:58 PM, +0000 UTC — 1 lot of baby product voluntarily recalled over alcohol content
    
    Link: https://abcnews.com/GMA/Family/1-lot-baby-product-voluntarily-recalled-alcohol-content/story?id=137123138
  - (FDA recall health) [Health.com] 10/09/2026, 08:00 PM, +0000 UTC — FDA Announces Pre-Workout Recall After Testing Finds Dangerous Ingredient
    
    Link: https://www.health.com/pre-workout-recall-illegal-ingredient-october-2026-12166677
  - (FDA recall health) [The Tennessean] 10/07/2026, 07:27 PM, +0000 UTC — Tennessee is part of a Gatorade recall. Which products are affected
    
    Link: https://www.tennessean.com/story/news/health/2026/10/07/gatorade-recall-tennessee-undeclared-food-coloring/92137069007/
  - (FDA recall health) [New York Post] 10/12/2026, 03:07 PM, +0000 UTC — FDA recalls baby sleep aid after investigation finds 3 toxic alcohol ingredients not listed on label
    
    Link: https://nypost.com/2026/10/12/lifestyle/popular-baby-gripe-water-recalled-over-toxic-unlisted-alcohols-fda/
  - (FDA recall health) [Dallas News] 10/09/2026, 09:58 PM, +0000 UTC — Pacific Health voluntarily recalls Baby Magic Tea for containing alcohol
    
    Link: https://www.dallasnews.com/news/public-health/article/baby-magic-tea-recall-alcohol-fda-22470633.php