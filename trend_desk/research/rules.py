"""Research Desk's code rules. The Judge can't argue its way past these.

Everything here is a pure function of one study record from the research dashboard, so it is
tested without the network or a model (test_rules.py).

  online_date()   the study's online publication date, never an issue date
  flags()         what the caveats say about the evidence (subgroup, tiny sample, preprint...)
  blocked()       the routes this study may not take, each with a reason
"""
from __future__ import annotations

import re
from datetime import date, timedelta

PITCH_DAYS = 30   # online within 30 days for a pitch (Meagan, 2026-10-25)
HARD_STOP = 60    # 31-60 days needs another peg; past 60 no pitch or roundup at all
TINY_N = 50       # an explicit sample this small never headlines

MONTHS = {m: i for i, m in enumerate(
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], 1)}
FULL = re.compile(r"(\d{4}) ([A-Z][a-z]{2}) (\d{1,2})\b")
EPUB = re.compile(r"Epub (\d{4} [A-Z][a-z]{2} \d{1,2})")
PREPRINT = re.compile(r"\b(medrxiv|biorxiv|psyarxiv|research square|ssrn|preprint)\b", re.I)


def _parse(text: str) -> date | None:
    m = FULL.match(text.strip())
    if not m or m.group(2) not in MONTHS:
        return None
    try:
        return date(int(m.group(1)), MONTHS[m.group(2)], int(m.group(3)))
    except ValueError:
        return None


def online_date(pubdate: str, run_date: str) -> tuple[date | None, str]:
    """(date, basis). basis is "epub", "full", or why there's no usable date.

    PubMed's pubdate is often the issue date ("2026 Dec", or a full date weeks ahead). A full date
    more than 3 days after the digest found the study is an issue date, not an online date."""
    pubdate = (pubdate or "").strip()
    found = date.fromisoformat(run_date) if re.fullmatch(r"\d{4}-\d{2}-\d{2}", run_date or "") else None
    m = EPUB.search(pubdate)
    if m and (d := _parse(m.group(1))):
        return d, "epub"
    d = _parse(pubdate)
    if d is None:
        return None, "month-only" if re.match(r"\d{4}( [A-Z][a-z]{2})?$", pubdate) else "unparsed"
    if found and d > found + timedelta(days=3):
        return None, "issue-date"
    return d, "full"


def age_days(study: dict, today: date) -> tuple[int, bool]:
    """(days since online, verified). Without a usable online date, the day the digest found it
    stands in: digests search recent PubMed entries, so that is close, but it is unverified."""
    d, _ = online_date(study.get("pubdate", ""), study.get("run_date", ""))
    if d:
        return (today - d).days, True
    try:
        return (today - date.fromisoformat(study.get("run_date", ""))).days, False
    except ValueError:
        return 9999, False


def _sample_sizes(text: str) -> list[int]:
    return [int(n) for n in re.findall(r"\b[Nn]\s*[=<≤]\s*(\d{1,6})\b", text) if n.isdigit()] + \
           [int(n) for n in re.findall(r"\b(\d{1,3}) (?:total|participants|patients|women|men|adults|children)\b", text)]


def flags(study: dict) -> dict:
    cav = (study.get("caveats") or "")
    cav = cav if isinstance(cav, str) else "; ".join(map(str, cav))
    text = f"{cav} {study.get('fact_check_note') or ''}".lower()
    sizes = _sample_sizes(f"{cav} {study.get('fact_check_note') or ''}")
    return {
        "subgroup": bool(re.search(r"subgroup|post[- ]hoc|exploratory", text)),
        "tiny_sample": bool(sizes and min(sizes) < TINY_N),
        "small_sample": "small sample" in text or bool(sizes and min(sizes) < 100),
        "preprint": bool(PREPRINT.search(study.get("journal") or "")) or "preprint" in text,
        "animal_or_lab": bool(re.search(r"\b(animal model|mice|mouse|rats?|in vitro|cell line|zebrafish)\b", text)),
        "single_country": "single-country" in text or "single country" in text,
        "observational": "observational" in text,
        "covered": (study.get("media_coverage") or "").lower().startswith("already covered"),
    }


def blocked(study: dict, today: date) -> dict:
    """{route: reason} for every route this study may not take.

    Pitch-only blocks leave tfm and brief open: a widely covered or older study is still fine
    evidence for an outline or an evergreen page."""
    f = flags(study)
    days, _ = age_days(study, today)
    out = {}
    if f["preprint"]:
        return {r: "preprint" for r in ("pitch", "tfm", "roundup", "brief")}
    if f["subgroup"]:
        out["pitch"] = "subgroup or exploratory finding"
    elif f["tiny_sample"]:
        out["pitch"] = f"sample under {TINY_N}"
    elif f["covered"]:
        out["pitch"] = "already covered by the press"
    elif days > HARD_STOP:
        out["pitch"] = f"online more than {HARD_STOP} days ago"
    if days > HARD_STOP:
        out["roundup"] = f"online more than {HARD_STOP} days ago"
    if f["animal_or_lab"]:
        out.setdefault("pitch", "animal or lab study")
        out["roundup"] = "animal or lab study"
    return out


def needs_peg(study: dict, today: date) -> bool:
    """31-60 days old: a pitch is allowed only with a peg other than the paper itself."""
    days, _ = age_days(study, today)
    return PITCH_DAYS < days <= HARD_STOP
