"""News Desk's code rules. The Judge can't argue its way past these.

Pure functions of one item record (sources.load_news / load_agingwire), tested in test_rules.py.

  noise()     items dropped before the Judge sees them (meeting notices, dataset refreshes, earnings,
              product launches, awards, lawsuits, conference appearances)
  age_days()  days since the item was released
  blocked()   the routes this item may not take, each with a reason
  interested_party()  a claim by someone with a stake in it (company and advocacy releases)
"""
from __future__ import annotations

import re
from datetime import date

PRESS_DAYS = 14     # a press or org release is stale after 14 days (MEA-1864)
NOTICE_DAYS = 42    # a notice, agency release or analysis after 42, unless another peg exists
ROUNDUP_DAYS = 21

NOISE = [
    ("meeting notice", re.compile(r"\b(public |advisory |committee |board )?meetings?\b.*\b(notice|announcement)|"
                                  r"notice of (a )?(public |open |closed )?meeting|sunshine act|committee meeting|"
                                  r"consensus committee", re.I)),
    ("paperwork notice", re.compile(r"information collection|paperwork reduction act|comment request", re.I)),
    ("earnings or investor news", re.compile(r"\b(quarter(ly)?|fiscal) .*\b(results|earnings)\b|\bdividend\b|"
                                             r"\bearnings (call|release)\b|investor (day|conference)", re.I)),
    ("lawsuit or law-firm release", re.compile(r"class action|securities (fraud|litigation)|shareholder|"
                                               r"investigation on behalf|law firm|lawsuit filed|files? (a )?lawsuit", re.I)),
    ("award or ranking", re.compile(r"\b(named|recognized|honored) (as |to |among |by |one of)|\bwins?\b.*\baward|"
                                    r"best places to work|top workplaces", re.I)),
    ("conference appearance", re.compile(r"to (present|participate|ring|speak) at|will (present|host) .*(conference|webcast)", re.I)),
    ("product launch", re.compile(r"\b(launch(es|ed)?|introduc(es|ed)|now available)\b", re.I)),
]
PRESS_ONLY = {"earnings or investor news", "lawsuit or law-firm release", "award or ranking",
              "conference appearance", "product launch"}


def interested_party(item: dict) -> bool:
    return item.get("kind") in ("press_release", "org_release")


def noise(item: dict) -> str:
    """Why this item never reaches the Judge, or ""."""
    if item.get("kind") == "dataset":
        return "dataset refresh"
    text = item.get("title", "")
    for reason, rx in NOISE:
        if reason in PRESS_ONLY and not interested_party(item):
            continue
        if rx.search(text):
            return reason
    return ""


def age_days(item: dict, today: date) -> int:
    for k in ("released", "found"):
        try:
            return max((today - date.fromisoformat(item.get(k) or "")).days, 0)
        except ValueError:
            continue
    return 9999


def stale_after(item: dict) -> int:
    return PRESS_DAYS if interested_party(item) else NOTICE_DAYS


def blocked(item: dict, today: date) -> dict:
    """{route: reason}. A stale item can still be an outline or a brief: those don't need news."""
    days, out = age_days(item, today), {}
    if days > 2 * stale_after(item):
        out["pitch"] = f"released {days} days ago"
    if days > ROUNDUP_DAYS:
        out["roundup"] = f"released {days} days ago"
    if (item.get("coverage") or "").lower() in ("wide", "widely_reported", "saturated"):
        out.setdefault("pitch", "already widely covered")
    return out


def needs_peg(item: dict, today: date) -> bool:
    """Past its freshness window but not twice it: a pitch needs a peg other than the item itself."""
    return stale_after(item) < age_days(item, today) <= 2 * stale_after(item)


def pitch_problem(idea: dict, leads: list[dict]) -> str:
    """Why a pitch idea can't stand, or "". A pitch resting on a claim by an interested party needs
    a named primary source that can test it, unless the Judge marks it a standout (Meagan,
    2026-10-25: "if there's a really interesting or potentially groundbreaking press release keep
    it in"). A standout then goes to the pitch agents flagged to find that test themselves."""
    if any(interested_party(i) for i in leads) and not (idea.get("primary_test") or "").strip() \
       and not idea.get("standout"):
        return "a release's claim with no primary source to test it"
    if not any(i.get("url") for i in leads):
        return "no link to the primary document"
    return ""
