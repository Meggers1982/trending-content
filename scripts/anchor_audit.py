#!/usr/bin/env python3
"""Offline relevance-anchor audit for google_trend_radar.py (MEA-1834).

Replays every saved radar scan in outputs/google_trend_radar/ through the
CURRENT relevance rules (seed anchors, GENERIC_ANCHOR_WORDS, word-boundary
matching, PROFILE_WEAK_ANCHORS, PROFILE_EXCLUSION_TERMS, PROFILE_EXTRA_ANCHORS
and the beauty taxonomy) and reports, per profile:

  FLIP  a saved candidate that was kept when the scan ran but would now be
        rejected, with the reason (review these for lost legit topics);
  NEW   a candidate a scan rejected as off-topic that would now be kept
        (should be empty - the rules only ever tighten);
  KEPT  (with --show-kept) still-kept candidates that only matched a
        single-word anchor, i.e. the ones most likely to be noise next.

By default "was kept" means kept when the scan ran, so a scan from July also
shows junk that later rules (July's "clean"/"care" fix, the August Trending
Now anchor fix) already reject. Pass --baseline-ref <git ref> to compare
against the radar as it stands at that ref instead, which isolates what a
change of yours flips:

    python scripts/anchor_audit.py --baseline-ref origin/main

No SerpAPI calls. Uses profile_relevance_inputs()/relevance_verdict() from the
radar itself, so the audit can't drift from production. Run from repo root:

    python scripts/anchor_audit.py                 # every profile
    python scripts/anchor_audit.py --profile fitness --show-kept
    python scripts/anchor_audit.py --summary       # counts only
    python scripts/anchor_audit.py --baseline-ref origin/main

Rerun it whenever you add a seed, a profile, or an anchor rule - audit every
profile before shipping, not one profile at a time (see CLAUDE.md).
"""
from __future__ import annotations

import argparse
import glob
import importlib.util
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import google_trend_radar as m  # noqa: E402

RADAR_DIR = ROOT / "outputs" / "google_trend_radar"


def profile_rules(profile: str, taxonomy: dict, radar=m) -> dict:
    """Mirror main(): topic defaults to the profile slug, anchors come from
    the curated seed list (build_seed_terms), never Trending Now terms."""
    seeds = radar.build_seed_terms(profile, "", profile, radar.DEFAULT_MAX_SEEDS)
    inputs = radar.profile_relevance_inputs(profile, taxonomy)
    norm = radar.normalize
    return {
        "anchors": radar.relevance_anchors(profile, seeds),
        "substring_anchors": {norm(t) for t in (inputs["extra_anchor_terms"] or []) if norm(t)},
        "weak_anchors": inputs["weak_anchors"],
        "exclusions": {norm(t) for t in (inputs["exclusion_terms"] or []) if norm(t)},
    }


def load_baseline(ref: str, workdir: Path):
    """Import google_trend_radar.py (and its beauty taxonomy) as of a git
    ref, laid out like the repo so its PROJECT_ROOT-relative paths resolve."""
    (workdir / "configs").mkdir(parents=True, exist_ok=True)
    for rel in ("google_trend_radar.py", "configs/beauty_taxonomy.yaml"):
        blob = subprocess.run(
            ["git", "-C", str(ROOT), "show", f"{ref}:{rel}"],
            check=True, capture_output=True,
        ).stdout
        (workdir / rel).write_bytes(blob)
    spec = importlib.util.spec_from_file_location("radar_baseline", workdir / "google_trend_radar.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module  # @dataclass looks its module up here
    spec.loader.exec_module(module)
    return module


def baseline_verdict(radar, profile: str, query: str) -> bool:
    """Would the radar at the baseline ref keep this query?"""
    cache = baseline_verdict.__dict__.setdefault("cache", {})
    if profile not in cache:
        taxonomy = radar.load_taxonomy(radar.BEAUTY_TAXONOMY_PATH)
        if hasattr(radar, "relevance_verdict"):
            cache[profile] = ("new", profile_rules(profile, taxonomy, radar))
        else:
            # Pre-MEA-1834 radar: plain substring anchors, beauty-only
            # substring exclusions (replicates its main()/build_data()).
            seeds = radar.build_seed_terms(profile, "", profile, radar.DEFAULT_MAX_SEEDS)
            anchors = set(radar.relevance_anchors(profile, seeds))
            if profile == "beauty":
                anchors |= {radar.normalize(t) for terms in taxonomy.values() for t in terms}
            anchors |= {radar.normalize(t) for t in getattr(radar, "PROFILE_EXTRA_ANCHORS", {}).get(profile, [])}
            exclusions = set()
            if profile == "beauty":
                exclusions = {radar.normalize(t) for t in radar.load_exclusion_terms(radar.BEAUTY_TAXONOMY_PATH)}
            cache[profile] = ("legacy", (anchors - {""}, exclusions - {""}))
    kind, rules = cache[profile]
    if kind == "new":
        return radar.relevance_verdict(query, **rules)[0]
    anchors, exclusions = rules
    if any(term in query for term in exclusions):
        return False
    return any(anchor in query for anchor in anchors)


def audit_profile(profile: str, taxonomy: dict, baseline=None) -> dict:
    rules = profile_rules(profile, taxonomy)
    files = sorted(glob.glob(str(RADAR_DIR / f"trend_radar_{profile}_*.json")))
    kept_seen: set[str] = set()
    rejected_seen: set[str] = set()
    flips, new_keeps, single_word_kept = [], [], []
    for path in files:
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
        for cand in data.get("candidates", []):
            query = m.normalize(cand.get("topic", ""))
            if not query or query in kept_seen:
                continue
            kept_seen.add(query)
            if baseline is not None and not baseline_verdict(baseline, profile, query):
                continue  # already rejected at the baseline ref
            keep, reason = m.relevance_verdict(query, **rules)
            if not keep:
                flips.append((query, reason))
                continue
            hits = [a for a in rules["anchors"] if m.anchor_matches(a, query)]
            hits += [a for a in rules["substring_anchors"] if a in query]
            if hits and not any(" " in a or a in rules["substring_anchors"] for a in hits):
                single_word_kept.append((query, sorted(set(hits))))
        for item in data.get("rejected", []):
            query = m.normalize(item.get("topic", ""))
            if not query or query in rejected_seen or query in kept_seen:
                continue
            rejected_seen.add(query)
            if baseline is None and not str(item.get("reason", "")).startswith("Off-topic"):
                continue
            if baseline is not None and baseline_verdict(baseline, profile, query):
                continue  # baseline already kept it
            keep, _ = m.relevance_verdict(query, **rules)
            if keep:
                new_keeps.append(query)
    return {
        "files": len(files),
        "kept": len(kept_seen),
        "flips": sorted(flips),
        "new_keeps": sorted(new_keeps),
        "single_word_kept": sorted(single_word_kept),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--profile", action="append", help="Audit only this profile (repeatable).")
    parser.add_argument("--show-kept", action="store_true", help="Also list still-kept single-word-anchor matches.")
    parser.add_argument("--summary", action="store_true", help="Print per-profile counts only.")
    parser.add_argument("--baseline-ref", help="Compare against the radar at this git ref (e.g. origin/main) instead of the decision recorded when each scan ran.")
    args = parser.parse_args()

    taxonomy = m.load_taxonomy()
    profiles = args.profile or list(m.SEED_PROFILES)
    unknown = [p for p in profiles if p not in m.SEED_PROFILES]
    if unknown:
        parser.error(f"unknown profile(s): {', '.join(unknown)}")

    tmp = tempfile.TemporaryDirectory()
    baseline = load_baseline(args.baseline_ref, Path(tmp.name)) if args.baseline_ref else None
    if baseline is not None:
        print(f"Baseline: google_trend_radar.py at {args.baseline_ref}")

    total_flips = total_new = 0
    print(f"{'profile':22} {'scans':>5} {'kept':>5} {'flip':>5} {'new':>4}")
    results = {}
    for profile in profiles:
        result = audit_profile(profile, taxonomy, baseline)
        results[profile] = result
        total_flips += len(result["flips"])
        total_new += len(result["new_keeps"])
        print(f"{profile:22} {result['files']:>5} {result['kept']:>5} {len(result['flips']):>5} {len(result['new_keeps']):>4}")
    print(f"{'TOTAL':22} {'':>5} {'':>5} {total_flips:>5} {total_new:>4}")

    if args.summary:
        return 0
    for profile, result in results.items():
        if not (result["flips"] or result["new_keeps"] or (args.show_kept and result["single_word_kept"])):
            continue
        print(f"\n== {profile}")
        for query, reason in result["flips"]:
            print(f"  FLIP  {query}  [{reason}]")
        for query in result["new_keeps"]:
            print(f"  NEW   {query}")
        if args.show_kept:
            for query, hits in result["single_word_kept"]:
                print(f"  KEPT  {query}  [{', '.join(hits)}]")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
