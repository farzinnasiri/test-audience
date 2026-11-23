#!/usr/bin/env python3
"""Turn free-text synthetic responses into 1-5 Likert distributions with
Semantic Similarity Rating (SSR, Maier et al. 2025, arXiv:2510.08338), using
PyMC Labs' reference implementation (semantic_similarity_rating).

Input JSON:
{
  "anchor_sets": {"<set id>": ["<1>", "<2>", "<3>", "<4>", "<5>"], ...},   # optional
  "responses": [{"variant": "A", "segment": "busy parents", "text": "..."}, ...]
}

Output: a Markdown summary on stdout (or JSON with --json): per variant and per
variant x segment, n, the mean PMF over the 5 points, the expected score, and a
bootstrap 90% interval for the expected score.
"""

import argparse
import json
import sys

import numpy as np

# Authored defaults for "how likely are you to try/buy this". They are NOT the
# paper's anchor sets. Replace them when the question differs (e.g. "pay $8/month").
DEFAULT_ANCHOR_SETS = {
    "plain": [
        "I would definitely not get this.",
        "I probably would not get this.",
        "I might or might not get this, I'm not sure.",
        "I would probably get this.",
        "I would definitely get this.",
    ],
    "conversational": [
        "This isn't for me at all, I'd never use or pay for it.",
        "I'm not convinced, I doubt I'd bother with it.",
        "It's fine, I could go either way on it.",
        "This looks useful, I'd likely give it a try.",
        "I want this, I'd get it right away.",
    ],
}


def bootstrap_interval(pmfs, rng, n_boot=2000, level=0.90):
    scores = pmfs @ np.arange(1, 6)
    if len(scores) < 2:
        return (float("nan"), float("nan"))
    idx = rng.integers(0, len(scores), size=(n_boot, len(scores)))
    means = scores[idx].mean(axis=1)
    lo, hi = np.quantile(means, [(1 - level) / 2, 1 - (1 - level) / 2])
    return (float(lo), float(hi))


def summarize(pmfs, rng):
    mean_pmf = pmfs.mean(axis=0)
    lo, hi = bootstrap_interval(pmfs, rng)
    return {
        "n": int(len(pmfs)),
        "pmf": [round(float(p), 3) for p in mean_pmf],
        "expected": round(float(mean_pmf @ np.arange(1, 6)), 2),
        "interval90": [round(lo, 2), round(hi, 2)],
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input", help="path to the input JSON")
    ap.add_argument("--model", default="all-MiniLM-L6-v2", help="sentence-transformers model (default: package default)")
    ap.add_argument("--temperature", type=float, default=1.0)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--json", action="store_true", help="print JSON instead of Markdown")
    args = ap.parse_args()

    try:
        import polars as po
        from semantic_similarity_rating import ResponseRater
    except ImportError:
        sys.exit(
            "Missing dependency. Run with:\n"
            '  uv run --python 3.12 --with "semantic_similarity_rating @ '
            'git+https://github.com/pymc-labs/semantic-similarity-rating.git" '
            "scripts/ssr_rate.py <input.json>"
        )

    with open(args.input, encoding="utf-8") as f:
        data = json.load(f)
    anchor_sets = data.get("anchor_sets") or DEFAULT_ANCHOR_SETS
    responses = data["responses"]
    for name, sentences in anchor_sets.items():
        if len(sentences) != 5:
            sys.exit(f"anchor set '{name}' must have exactly 5 sentences (1 = lowest, 5 = highest)")
    if not responses:
        sys.exit("no responses")

    rows = {"id": [], "int_response": [], "sentence": []}
    for name, sentences in anchor_sets.items():
        for i, s in enumerate(sentences, start=1):
            rows["id"].append(name)
            rows["int_response"].append(i)
            rows["sentence"].append(s)
    rater = ResponseRater(po.DataFrame(rows), model_name=args.model)

    texts = [r["text"] for r in responses]
    pmfs = rater.get_response_pmfs("mean", texts, temperature=args.temperature)
    rng = np.random.default_rng(args.seed)

    groups = {}
    for r, pmf in zip(responses, pmfs):
        groups.setdefault((r["variant"], None), []).append(pmf)
        if r.get("segment"):
            groups.setdefault((r["variant"], r["segment"]), []).append(pmf)

    result = {
        "anchor_sets": list(anchor_sets),
        "model": args.model,
        "variants": [],
        "variant_segments": [],
    }
    for (variant, segment), rows_ in sorted(groups.items(), key=lambda kv: (kv[0][0], kv[0][1] or "")):
        s = summarize(np.array(rows_), rng)
        s["variant"] = variant
        if segment is None:
            result["variants"].append(s)
        else:
            s["segment"] = segment
            result["variant_segments"].append(s)

    if args.json:
        print(json.dumps(result, indent=2))
        return

    print("SYNTHETIC HYPOTHESIS: not user validation. Relative comparison only.\n")
    print(f"Anchor sets: {', '.join(result['anchor_sets'])} (averaged); embedding model: {args.model}\n")
    print("| Variant | n | P(1) | P(2) | P(3) | P(4) | P(5) | Expected | 90% interval |")
    print("|---|---|---|---|---|---|---|---|---|")
    for s in sorted(result["variants"], key=lambda s: -s["expected"]):
        p = s["pmf"]
        print(f"| {s['variant']} | {s['n']} | {p[0]} | {p[1]} | {p[2]} | {p[3]} | {p[4]} | {s['expected']} | {s['interval90'][0]}–{s['interval90'][1]} |")
    if result["variant_segments"]:
        print("\n| Variant | Segment | n | Expected | 90% interval |")
        print("|---|---|---|---|---|")
        for s in result["variant_segments"]:
            print(f"| {s['variant']} | {s['segment']} | {s['n']} | {s['expected']} | {s['interval90'][0]}–{s['interval90'][1]} |")


if __name__ == "__main__":
    main()
