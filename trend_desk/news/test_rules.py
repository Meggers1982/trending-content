"""Tests for News Desk's code rules. Run: python3 -m pytest trend_desk/news -q
Cases are real items from the news digest and AgingWire, 23 to 25 October 2026."""
from datetime import date

from trend_desk.news import rules, run

TODAY = date(2026, 10, 25)


def item(**kw):
    base = {"key": "press-x", "kind": "press_release", "title": "", "url": "https://www.prnewswire.com/x", "source": "news digest",
            "released": "2026-10-24", "found": "2026-10-25", "coverage": ""}
    return {**base, **kw}


def test_noise_is_dropped_before_the_judge():
    assert rules.noise(item(kind="dataset", title="CMS refreshed dataset: Penalties")) == "dataset refresh"
    assert rules.noise(item(kind="notice", title="Notice of Federal Advisory Committee Meeting; Manufactured "
                                                 "Housing Consensus Committee")) == "meeting notice"
    assert rules.noise(item(title="CapCut named among the best AI tools for small business marketing")) == "award or ranking"
    assert rules.noise(item(title="Lassa Introduces Wintus 3 Winter Tyre")) == "product launch"
    assert rules.noise(item(title="Shareholder investigation on behalf of investors in Hims & Hers")) == \
        "lawsuit or law-firm release"


def test_agencies_are_not_held_to_press_noise():
    # "CMS launches" is policy, not a product launch
    assert rules.noise(item(kind="agency", title="CMS launches $275M nurse recruitment push for nursing homes")) == ""
    # trial results are not noise; whether they stand is the Judge's question
    assert rules.noise(item(title="RYBREVANT FASPRO combination posts 77% overall response rate")) == ""


def test_freshness_by_kind():
    press = item(released="2026-10-05")                      # 20 days: past 14, within 28
    assert rules.needs_peg(press, TODAY) and "pitch" not in rules.blocked(press, TODAY)
    assert "pitch" in rules.blocked(item(released="2026-09-20"), TODAY)
    notice = item(kind="notice", released="2026-09-20")       # 35 days: inside 42
    assert not rules.needs_peg(notice, TODAY) and rules.blocked(notice, TODAY) == {"roundup": "released 35 days ago"}
    bls = item(kind="analysis", released="2026-09-01")        # BLS CPI, 54 days: needs another peg
    assert rules.needs_peg(bls, TODAY)


def test_release_pitch_needs_a_test_or_a_standout():
    lead = [item()]
    assert rules.pitch_problem({"primary_test": "", "standout": False}, lead)
    assert rules.pitch_problem({"primary_test": "ClinicalTrials.gov NCT05000000", "standout": False}, lead) == ""
    # Meagan, 2026-10-25: a really interesting or potentially groundbreaking release stays in
    assert rules.pitch_problem({"primary_test": "", "standout": True}, lead) == ""
    # agency and analysis items are primary sources themselves
    assert rules.pitch_problem({"primary_test": "", "standout": False}, [item(kind="agency")]) == ""


def test_apply_enforces_rules_and_flags_standouts():
    data = {"items": {}, "ideas": {}, "runs": []}
    rel = item(key="press-a", title="New drug posts 77% response rate")
    kff = item(key="aw-b", kind="analysis", title="Medigap denial", url="https://www.kff.org/b")
    cands = [run.view(rel, TODAY), run.view(kff, TODAY)]
    base = {"beat": "", "angle": "", "why_now": "", "is_it_real": "", "standout_reason": "", "other_peg": "",
            "audience": "general", "evidence_strength": "moderate", "site": "", "seed_keyword": "", "confidence": "high"}
    result = {"ideas": [{**base, "title": "Drug claim", "keys": ["press-a"], "route": "roundup",
                         "primary_test": "", "standout": False},
                        {**base, "title": "Medigap", "keys": ["aw-b"], "route": "pitch", "primary_test": "",
                         "standout": False}], "drops": []}
    created, dropped = run.apply(data, result, cands, {"press-a": rel, "aw-b": kff}, TODAY)
    assert [c["title"] for c in created] == ["Medigap"]
    assert data["items"]["press-a"]["detail"].startswith("roundup:")
    data = {"items": {}, "ideas": {}, "runs": []}
    result = {"ideas": [{**base, "title": "Drug claim", "keys": ["press-a"], "route": "pitch",
                         "primary_test": "", "standout": True, "standout_reason": "first ever"}], "drops": []}
    created, _ = run.apply(data, result, cands[:1], {"press-a": rel}, TODAY)
    assert created[0]["standout"] and created[0]["needs_independent_test"]


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
    print("ok")
