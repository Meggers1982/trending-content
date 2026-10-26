"""Tests for Research Desk's code rules. Run: python3 -m pytest trend_desk/research -q
(or python3 -m trend_desk.research.test_rules without pytest). Cases are real dashboard records."""
from datetime import date

from trend_desk.research import rules, run

TODAY = date(2026, 10, 25)


def study(**kw):
    base = {"pmid": "1", "journal": "Maturitas", "pubdate": "2026 Oct 23", "run_date": "2026-10-24",
            "caveats": "observational design", "fact_check_note": "", "relevance_score": 8,
            "media_coverage": "Not widely covered ✓ (SERPAPI verified)"}
    return {**base, **kw}


def test_online_date_forms():
    assert rules.online_date("2026 Oct 23", "2026-10-24") == (date(2026, 10, 23), "full")
    assert rules.online_date("2026 Nov 24 (Epub 2026 Oct 23)", "2026-10-24") == (date(2026, 10, 23), "epub")
    assert rules.online_date("2026 Dec", "2026-10-24") == (None, "month-only")
    assert rules.online_date("2026", "2026-10-24") == (None, "month-only")
    # A full date weeks after the digest found it is the issue date, not the online date.
    assert rules.online_date("2026 Dec 15", "2026-10-24") == (None, "issue-date")
    assert rules.online_date("2026 Oct-Dec", "2026-10-24")[0] is None


def test_age_falls_back_to_run_date_unverified():
    assert rules.age_days(study(), TODAY) == (2, True)
    assert rules.age_days(study(pubdate="2026 Dec"), TODAY) == (1, False)


def test_aspirin_subgroup_is_never_a_pitch():
    # BJOG, PMID 42919680: "may slash recurrent preterm birth by 90%" from 44 women.
    s = study(caveats="secondary analysis, small sample (N<100 in MVM subgroup; 44 total), "
                      "observational design for subgroup, single-country (Netherlands)")
    f = rules.flags(s)
    assert f["subgroup"] and f["tiny_sample"] and f["single_country"]
    assert "pitch" in rules.blocked(s, TODAY)
    assert "tfm" not in rules.blocked(s, TODAY)


def test_covered_blocks_pitch_only():
    s = study(media_coverage="Already covered by Nature, Bioengineer")
    assert rules.blocked(s, TODAY) == {"pitch": "already covered by the press"}


def test_freshness_windows():
    assert not rules.needs_peg(study(pubdate="2026 Oct 1"), TODAY)          # 24 days
    assert rules.needs_peg(study(pubdate="2026 Sep 10", run_date="2026-09-11"), TODAY)  # 45 days
    old = study(pubdate="2026 Aug 1", run_date="2026-08-02")                # 85 days
    b = rules.blocked(old, TODAY)
    assert "pitch" in b and "roundup" in b and "brief" not in b


def test_preprint_and_animal():
    assert set(rules.blocked(study(journal="medRxiv"), TODAY)) == {"pitch", "tfm", "roundup", "brief"}
    b = rules.blocked(study(caveats="animal model (mice), small sample"), TODAY)
    assert "pitch" in b and "roundup" in b


def test_large_sample_is_not_small():
    s = study(fact_check_note="N=762 confirmed; age range 2-5 years confirmed")
    assert not rules.flags(s)["small_sample"] and rules.blocked(s, TODAY) == {}


def test_apply_enforces_blocks_and_accounts_for_every_pmid():
    studies = {"a": study(pmid="a"), "b": study(pmid="b", media_coverage="Already covered by Nature"),
               "c": study(pmid="c")}
    cands = [run.view(s, TODAY) for s in studies.values()]
    data = {"studies": {}, "ideas": {}, "runs": []}
    result = {"ideas": [
        {"title": "Covered study as a pitch", "pmids": ["b"], "route": "pitch", "beat": "", "angle": "",
         "why_now": "", "is_it_real": "", "evidence_strength": "moderate", "other_peg": "", "audience": "general",
         "site": "", "seed_keyword": "", "confidence": "medium"},
        {"title": "Fresh study as a pitch", "pmids": ["a", "zzz"], "route": "pitch", "beat": "", "angle": "",
         "why_now": "", "is_it_real": "", "evidence_strength": "strong", "other_peg": "", "audience": "both",
         "site": "", "seed_keyword": "", "confidence": "high"}],
        "drops": [], "notes": ""}
    created, dropped = run.apply(data, result, cands, studies, TODAY)
    assert [c["pmids"] for c in created] == [["a"]]          # the invented PMID is ignored
    assert data["studies"]["b"]["status"] == "dropped" and data["studies"]["b"]["reason"] == "rule"
    assert "c" not in data["studies"] and data["passed_over"] == {"c": "2026-10-25"}  # one more look
    run.apply(data, {"ideas": [], "drops": [], "notes": ""}, [cands[2]], studies, TODAY)
    assert data["studies"]["c"]["reason"] == "not-selected" and data["passed_over"] == {}
    assert created[0]["id"].startswith("rd-2026-10-25-") and created[0]["desk"] == "research"


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
            print("ok", name)
