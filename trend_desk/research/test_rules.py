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


def test_pattern_pitch_rules():
    def v(pmid, journal, days, flags=()):
        return {"pmid": pmid, "journal": journal, "days_online": days, "flags": list(flags)}
    ok = [v("a", "BMJ", 120), v("b", "JAMA", 80), v("c", "BMJ", 200)]
    assert rules.pattern_problem(ok) == ""
    assert "journals" in rules.pattern_problem([v("a", "BMJ", 10), v("b", "BMJ", 20), v("c", "bmj", 30)])
    assert "90 days" in rules.pattern_problem([v("a", "BMJ", 120), v("b", "JAMA", 95), v("c", "Lancet", 300)])
    assert "human" in rules.pattern_problem(ok[:2] + [v("d", "Cell", 5, ["animal_or_lab"])])
    assert "headline" in rules.pattern_problem([v("a", "BMJ", 50, ["subgroup"])] + ok[1:] + [v("e", "NEJM", 9)])


def test_backlog_apply_allows_old_pattern_pitch_but_not_old_single():
    old = {p: study(pmid=p, journal=j, pubdate=d, run_date=r) for p, j, d, r in [
        ("p1", "BMJ", "2026 Jul 1", "2026-07-02"), ("p2", "JAMA", "2026 Aug 20", "2026-08-21"),
        ("p3", "Lancet", "2026 Jun 10", "2026-06-11"), ("p4", "BMJ", "2026 Jun 1", "2026-06-02")]}
    cands = [run.view(s, TODAY) for s in old.values()]
    base = {"beat": "", "angle": "", "why_now": "", "is_it_real": "", "evidence_strength": "moderate",
            "other_peg": "", "audience": "general", "site": "", "seed_keyword": "", "confidence": "medium"}
    data = {"studies": {}, "ideas": {}, "runs": []}
    result = {"ideas": [{**base, "title": "Three studies, one story", "pmids": ["p2", "p1", "p3"],
                         "route": "pitch", "kind": "pattern"},
                        {**base, "title": "One old study", "pmids": ["p4"], "route": "pitch", "kind": "single"}],
              "drops": [], "notes": ""}
    created, _ = run.apply(data, result, cands, old, TODAY, backlog=True)
    assert [c["kind"] for c in created] == ["pattern"] and created[0]["backlog"] is True
    assert data["studies"]["p4"]["reason"] == "rule"
    # The daily run never builds pattern pitches, even when asked.
    data2 = {"studies": {}, "ideas": {}, "runs": []}
    created2, _ = run.apply(data2, result, cands, old, TODAY)
    assert created2 == [] and data2["studies"]["p2"]["reason"] == "rule"


def test_backlog_view_blocks_old_roundup_and_triaged_pitch():
    from trend_desk.research import backlog
    s = study(pmid="t1", pubdate="2026 Sep 25", run_date="2026-09-26")  # 30 days
    v = backlog.backlog_view(s, TODAY, {"t1": "digest triage"}, {"t1"})
    assert "roundup" in v["blocked"] and "triaged" in v["blocked"]["pitch"] and v["saved"]
    assert "tfm" not in v["blocked"] and "brief" not in v["blocked"]


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
            print("ok", name)


# OpenAlex digests (marketing, career), reshaped by sources.openalex_study (MEA-1865).
from trend_desk.research import sources  # noqa: E402

MAGE = {  # marketing-research-digest, branding 2026-10-24
    "title": "AI-generated video ads beat human-made ones on TikTok", "journal": "Marketing Science",
    "published": "2026-10-14", "work_id": "W7221827692", "doi": "10.1287/mksc.2025.0150", "score": 90,
    "band": "Lead", "evidence_type": "experiments", "sample_size": None, "coverage_state": "unreported",
    "verdict": "✅ Accurate", "verdict_notes": "Design checks out", "caveats": "industry partner; clicks not sales",
    "the_study": "four preregistered field studies", "story_angle_primary": "stop trusting your gut",
}
RUN = {"run_date": "2026-10-24", "topic": "branding"}


def test_openalex_study_takes_the_research_shape():
    s = sources.openalex_study(MAGE, RUN, "Marketing research")
    assert s["pmid"] == "W7221827692" and s["eligible"] and s["relevance_score"] == 9.0
    assert s["pubdate"] == "2026 Oct 14" and s["media_coverage"] == "No coverage found"
    assert rules.blocked(s, TODAY) == {}
    assert not sources.openalex_study({**MAGE, "band": "Strong"}, RUN, "Marketing research")["eligible"]


def test_openalex_first_of_month_is_unverified_but_dated():
    s = sources.openalex_study({**MAGE, "published": "2026-10-01"}, RUN, "Marketing research")
    assert s["pubdate"] == "2026 Oct"
    assert rules.age_days(s, TODAY) == (24, False)  # from the OpenAlex date, not the 60-day-window find date
    v = run.view(s, TODAY)
    assert v["date_verified"] is False


def test_openalex_significant_issues_blocks_everything():
    s = sources.openalex_study({**MAGE, "verdict": "❌ Significant issues"}, RUN, "Marketing research")
    assert set(rules.blocked(s, TODAY)) == {"pitch", "tfm", "roundup", "brief"}


def test_openalex_weak_designs_never_pitch():
    one_time = sources.openalex_study({**MAGE, "evidence_type": "survey"}, RUN, "Career psychology")
    assert "pitch" in rules.blocked(one_time, TODAY) and "roundup" not in rules.blocked(one_time, TODAY)
    # career W7223279808: AI impostor feelings, a longitudinal survey of 329 workers
    waves = sources.openalex_study({**MAGE, "evidence_type": "survey",
                                    "the_study": "a three-wave longitudinal survey of 329 employees"},
                                   RUN, "Career psychology")
    assert "pitch" not in rules.blocked(waves, TODAY)
    for kind in ("qualitative", None):
        s = sources.openalex_study({**MAGE, "evidence_type": kind}, RUN, "Career psychology")
        assert "pitch" in rules.blocked(s, TODAY)
    # PubMed studies have no evidence_type and are never caught by this rule.
    assert not rules.flags(study())["weak_design"]


def test_openalex_widely_reported_is_covered():
    s = sources.openalex_study({**MAGE, "coverage_state": "widely_reported",
                                "covered_by": ["Forbes"]}, RUN, "Marketing research")
    assert s["media_coverage"] == "Already covered: Forbes"
    assert rules.blocked(s, TODAY)["pitch"] == "already covered by the press"
