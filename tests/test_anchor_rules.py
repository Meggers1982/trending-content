"""Relevance-anchor rules for google_trend_radar.py (MEA-1834).

Offline only: no SerpAPI calls. Rules are built exactly as main() builds
them (topic = profile slug, curated seeds, profile_relevance_inputs()).
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import google_trend_radar as m  # noqa: E402


def keeps(profile: str, query: str) -> bool:
    seeds = m.build_seed_terms(profile, "", profile, m.DEFAULT_MAX_SEEDS)
    inputs = m.profile_relevance_inputs(profile, m.load_taxonomy())
    keep, _ = m.relevance_verdict(
        query,
        m.relevance_anchors(profile, seeds),
        substring_anchors={m.normalize(t) for t in (inputs["extra_anchor_terms"] or [])},
        weak_anchors=inputs["weak_anchors"],
        exclusions={m.normalize(t) for t in (inputs["exclusion_terms"] or [])},
    )
    return keep


# --- 1. Off-topic queries from the 2026-10-31 audit are rejected -----------

REJECTED = [
    ("fitness", "ps5 games running on xbox hardware"),
    ("fitness", "green bay packers running back trade"),
    ("fitness", "why is desantis not running for governor"),
    ("fitness", "bruno mars longest running number one"),
    ("fitness", "lanterns show running joke analysis"),
    ("fitness", "scud running"),
    ("fitness", "how to make a latte at home"),
    ("fitness", "home insurance quotes"),
    ("adhd-focus", "metals focus gold price forecast 2027"),
    ("adhd-focus", "hcps focus"),
    ("food-safety", "nhtsa toyota rav4 recall notice"),
    ("food-safety", "hyundai vehicle fire risk recall"),
    ("food-safety", "ford sudden power loss recall"),
    ("food-safety", "clorox recall"),
    ("food-safety", "levothyroxine recall"),
    ("food-safety", "eye drop recall"),
    ("food-safety", "upup baby wipes safety recall"),
    ("food-safety", "chinese food near me"),
    ("food-safety", "costco food court"),
    ("food-safety", "restaurant depot"),
    ("food-safety", "email marketing for restaurants"),
    ("food-safety", "usda workforce reorganization impacts"),
    ("food-safety", "crossword clue"),
    ("mental-health", "tropical depression edouard"),
    ("mental-health", "danakil depression ethiopia"),
    ("mental-health", "dodge demon burnout"),
    ("mental-health", "burnout revenge soundtrack"),
    ("mental-health", "bangkok stem cell therapy"),
    ("mental-health", "nad therapy near me"),
    ("mental-health", "breast cancer awareness month"),
    ("diet", "diet coke advent calendar"),
    ("diet", "science diet cat food"),
    ("diet", "what is a macro in excel"),
    ("public-health", "recall election results"),
    ("public-health", "nhtsa toyota rav4 recall notice"),
    ("habits-body", "stock market plunge"),
    ("screening-prevention", "cancer horoscope today"),
    ("gut-health", "jay glazer mental health"),
    ("sleep", "revolver sleep token"),
    ("beauty", "beauty in black renewed season 4"),
]


@pytest.mark.parametrize("profile,query", REJECTED)
def test_off_topic_rejected(profile, query):
    assert not keeps(profile, query)


# --- 2. Legit matches still pass -------------------------------------------

KEPT = [
    ("fitness", "running shoes for beginners"),
    ("fitness", "running plans for beginners"),
    ("fitness", "best running shoes 2025"),
    ("fitness", "baltimore running festival photos"),
    ("fitness", "home workout for beginners"),
    ("adhd-focus", "adhd focus tips"),
    ("adhd-focus", "how to improve focus"),
    ("adhd-focus", "vyvanse shortage"),
    ("food-safety", "listeria cheese recall"),
    ("food-safety", "granola recall"),
    ("food-safety", "egg recall california"),
    ("food-safety", "which eggs are recalled"),
    ("food-safety", "tofu recall"),
    ("food-safety", "beef recall today"),
    ("food-safety", "food recall"),
    ("food-safety", "cyclospora outbreak"),
    ("food-safety", "restaurant inspection scores"),
    ("food-safety", "cross contamination"),
    ("food-safety", "food poisoning symptoms"),
    ("mental-health", "postpartum depression"),
    ("mental-health", "how to deal with burnout at work"),
    ("mental-health", "erp therapy"),
    ("mental-health", "cognitive behavioral therapy"),
    ("mental-health", "suicide awareness month"),
    ("mental-health", "mental health awareness"),
    ("diet", "keto friendly snacks"),
    ("diet", "macro tracking app"),
    ("diet", "university of liverpool diet soda study"),
    ("diet", "low fodmap diets"),
    ("public-health", "amlodipine recall"),
    ("habits-body", "cold plunge benefits"),
    ("screening-prevention", "skin cancer screening"),
    ("gut-health", "gut health foods"),
    ("gut-health", "what naturally kills bad bacteria in the gut"),
    ("womens-health", "menstrual cramps"),
    ("beauty", "skin barrier repair cream"),
    ("beauty", "versed rich barrier cream"),
    ("weight-loss", "glp-1 weight regain"),
]


@pytest.mark.parametrize("profile,query", KEPT)
def test_legit_kept(profile, query):
    assert keeps(profile, query)


# --- Matching primitives ---------------------------------------------------

def test_single_word_anchor_respects_word_boundaries():
    assert not m.anchor_matches("cross", "crossword")
    assert not m.anchor_matches("stress", "distress definition")
    assert m.anchor_matches("recall", "toyota recalls")
    assert m.anchor_matches("recall", "which eggs are recalled")
    assert m.anchor_matches("inflammatory", "anti-inflammatory diet")
    assert m.anchor_matches("glp-1", "glp-1s and muscle")


def test_phrase_anchor_is_substring():
    assert m.anchor_matches("food safety", "food safety tips")


def test_context_terms_match_at_word_start():
    assert m.term_at_word_start("egg", "egg recall")
    assert m.term_at_word_start("egg", "eggs recalled")
    assert not m.term_at_word_start("egg", "reggae festival")
    assert not m.term_at_word_start("ford", "affordable meals")


def test_build_data_records_reason_for_weak_anchor_rejection():
    inputs = m.profile_relevance_inputs("food-safety")
    candidates = [
        m.Candidate("nhtsa toyota rav4 recall notice", radar_score=80),
        m.Candidate("listeria cheese recall", radar_score=80),
    ]
    rejected: list[dict] = []
    seeds = m.build_seed_terms("food-safety", "", "food-safety", m.DEFAULT_MAX_SEEDS)
    data = m.build_data(
        "food-safety", "US", "now 7-d", seeds, candidates, rejected,
        extra_anchor_terms=inputs["extra_anchor_terms"],
        exclusion_terms=inputs["exclusion_terms"],
        anchor_seeds=seeds,
        weak_anchors=inputs["weak_anchors"],
    )
    kept = [c["topic"] for c in data["candidates"]]
    assert kept == ["listeria cheese recall"]
    reasons = {r["topic"]: r["reason"] for r in data["rejected"]}
    assert "weak anchor 'recall'" in reasons["nhtsa toyota rav4 recall notice"]
