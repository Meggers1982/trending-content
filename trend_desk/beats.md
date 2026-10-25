# Trend Desk: beats and routing guide

The Trend Judge reads this file on every run. It describes who Meagan is as a writer, what each
destination wants, and how to choose between them. Edit it freely; standing rules from her texts
go in `rules.md` instead.

## Who the ideas are for

Meagan Morris is a freelance health and culture journalist with 15 years in search and content.
She also runs her own newsletter and several content sites. Every idea the Judge keeps becomes
work in one of four places, and each place has a different bar.

## Destinations

### pitch: freelance story pitch
Goes to the Daily Pitches agents, which find an outlet and editor, write, edit, fact-check and
build a paused Mailshake draft. Only for ideas an editor would pay for:
- a real story with tension, not a topic ("why everyone is suddenly X" needs evidence it's sudden)
- a news peg or clock, or a trend backed by data a reporter can cite
- her lanes: women's health and the mind (ADHD, mental health, reproductive and menopause health);
  aging, body and metabolism (GLP-1s, obesity, cancer, cardiometabolic, nutrition science, sleep,
  fitness); public health, environment and tech (policy, health AI, insurance, the FDA, heat);
  history, food, the Midwest and internet culture
- not celebrity gossip on its own, not a single product launch, not a press release

### tfm: The Female Model newsletter post
Her newsletter, "Is it real, and can it be done?" Test issues ask whether a trend, claim or
statistic everyone repeats is actually true, with receipts. Themes: AI and authenticity, viral
health and wellness claims, building things you weren't qualified to build, ADHD and systems,
the body (she lost 150 lbs and had a body lift), the house (she is gut-renovating hers), politics,
work and money. Best fit: a claim that is spreading fast and can be checked against evidence.
One post per Wednesday, so only route the strongest one or two "is it real?" ideas per week.

### roundup: Friday roundup item
The Friday issue curates the week in short, sharp items with a take. Good for: quick, timely,
fun or useful trends that don't carry a full piece (a recall, a viral food, a celebrity health
moment with a real hook, a weird stat). Speed matters more than depth. These need no build step;
the roundup outline job picks them up.

### brief: SEO content brief for one of her sites
For steady search demand on a topic one of her sites covers (see `sites.yaml`). Best fit is an
**emerging** trend: rising for weeks, likely to keep being searched, answerable with an evergreen
page. Breaking news is a poor fit because search volume data lags. Name the site and give a seed
keyword (the phrase people would type, not a headline).

## Routing rules

- **One idea, one home.** Pick the single best destination. If an outlet would pay for it, pitch
  first; the newsletter can take it later if the pitch is passed on.
- **Exploding** trends (new this week) suit pitch and roundup. **Emerging** trends (rising 3+
  weeks) suit tfm and brief. Steady ones rarely deserve anything.
- **Cluster.** Several terms about the same story are one idea. "compounded glp-1 recall" and
  "glp-1 recall fda" are one idea with two terms.
- **Already covered.** If a recent idea already covers the story, attach the new terms to it
  (existing_idea_id) instead of making a second idea.
- **Drop noise.** Navigational searches ("gynecologist near me", brand logins), sports scores,
  weather, single celebrity names with no story, product names with no angle, anything nobody
  could write 600 honest words about.
- **Quality bar, not a quota.** Keep everything that clears the bar and nothing that doesn't. A
  day with zero ideas is a fine day.

## Never

- Anything about Hurrdat (her employer), her clients, or her father.
- Her dating life, relationships or sex life as a story angle.
- Ideas that depend on a diagnosis date or years of job tenure.
- The flipped-house and termite story as a pitch (newsletter only).
- Inventing a fact, number, study or source. If the evidence is thin, say so in is_it_real.
