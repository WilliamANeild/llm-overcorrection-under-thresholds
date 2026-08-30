#!/usr/bin/env python3
"""Detect meta-commentary wrapping in revision-side and T1-side outputs of the 50 pairs."""

import json, sys, re
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "study3" / "raw_responses"

with open(DATA_DIR / "reversibility_human_pairs.json") as f:
    pairs = json.load(f)
with open(DATA_DIR / "reversibility_human_key.json") as f:
    key = {k["pair_id"]: k for k in json.load(f)}

# Preamble patterns (case-insensitive, checked against first ~200 chars)
PREAMBLE_PATTERNS = [
    r"(?:i'?d like to|let me|i'?ll|i want to)\s+(?:revise|make|take|offer|give|try)",
    r"here'?s (?:the|my|a|an) (?:revised|improved|updated|final|slightly|new)",
    r"(?:sure|okay|alright|absolutely)[,!.]?\s+here",
    r"i think (?:i can|we can|it could|there)",
    r"(?:looking|look) (?:back|at (?:it|this|my))",
    r"(?:after|upon) review",
    r"(?:i've|i have) reviewed",
    r"thank(?:s| you) for (?:the|asking|checking|your)",
    r"(?:great|good) question",
    r"actually,? let me",
    r"(?:i'?d like to|i want to) (?:keep|confirm|make)",
    r"considering the response",
    r"(?:this is a )?(?:very )?(?:solid|strong|great|good) (?:implementation|version|set|start|draft)",
    r"you'?re right to ask",
    r"since you(?:'re| are| repeated)",
    r"(?:i can|let me) make (?:some|a few|one|minor)",
    r"(?:the|this) (?:version|script|function|code|email|post|analysis|response) (?:is|can be|could be)",
    r"however,? (?:i|during|to make)",
    r"(?:after|upon) re-?reading",
]

# Postamble patterns (checked against last ~300 chars)
POSTAMBLE_PATTERNS = [
    r"let me know (?:if|what|how)",
    r"hope this helps",
    r"feel free to",
    r"(?:happy|glad) to (?:help|assist|revise|adjust|make)",
    r"(?:if you'?d like|would you like) (?:any|me to|further|more)",
    r"(?:i'?m|we'?re) (?:here|available|happy) (?:to|if)",
    r"(?:just )?let me know",
    r"(?:what do you think|how does (?:this|that) (?:sound|look|work))",
    r"(?:otherwise|if not),? (?:this|it|we)",
    r"(?:i believe|i think|i'?m confident) (?:this|it|the) (?:version|is|meets|works|feels)",
    r"(?:no )?further (?:changes|revisions|adjustments)",
    r"this version (?:feels|is|should)",
    r"(?:ready to|you can) (?:use|go|send|share|present|submit)",
    r"(?:i'?ve|i have) made (?:some|minor|a few)",
    r"(?:do you|would you) (?:want|like|need) (?:me to|any)",
]

def detect_preamble(text):
    head = text[:300].lower()
    for pat in PREAMBLE_PATTERNS:
        m = re.search(pat, head)
        if m:
            return m.group(0), m.start(), m.end()
    return None, None, None

def detect_postamble(text):
    tail = text[-400:].lower()
    for pat in POSTAMBLE_PATTERNS:
        m = re.search(pat, tail)
        if m:
            return m.group(0), len(text) - 400 + m.start(), len(text) - 400 + m.end()
    return None, None, None


# Analyze revision side and T1 side
rev_results = []
t1_results = []

for p in pairs:
    k = key[p["pair_id"]]
    # Identify which output is T1 and which is revision
    if k["A_is"] == "T1":
        t1_text = p["output_A"]
        rev_text = p["output_B"]
    else:
        t1_text = p["output_B"]
        rev_text = p["output_A"]

    # Revision side
    pre_match, pre_start, pre_end = detect_preamble(rev_text)
    post_match, post_start, post_end = detect_postamble(rev_text)
    rev_results.append({
        "pair_id": p["pair_id"],
        "model": k["model"],
        "domain": k["domain"],
        "rev_turn": k["last_rev_turn"],
        "has_preamble": pre_match is not None,
        "preamble": pre_match,
        "has_postamble": post_match is not None,
        "postamble": post_match,
        "rev_text": rev_text,
        "rev_len": len(rev_text),
    })

    # T1 side
    t1_pre, _, _ = detect_preamble(t1_text)
    t1_post, _, _ = detect_postamble(t1_text)
    t1_results.append({
        "pair_id": p["pair_id"],
        "model": k["model"],
        "has_preamble": t1_pre is not None,
        "preamble": t1_pre,
        "has_postamble": t1_post is not None,
        "postamble": t1_post,
        "t1_text": t1_text,
        "t1_len": len(t1_text),
    })

# ═══════════════════════════════════════════════════════════════════════════
# 1. COUNTS
# ═══════════════════════════════════════════════════════════════════════════
print("=" * 80)
print("1. META-COMMENTARY IN REVISION-SIDE OUTPUTS (50 pairs)")
print("=" * 80)

has_pre = sum(1 for r in rev_results if r["has_preamble"])
has_post = sum(1 for r in rev_results if r["has_postamble"])
has_both = sum(1 for r in rev_results if r["has_preamble"] and r["has_postamble"])
has_either = sum(1 for r in rev_results if r["has_preamble"] or r["has_postamble"])
has_neither = 50 - has_either

print(f"\n  Has meta preamble:    {has_pre}/50 ({has_pre/50*100:.0f}%)")
print(f"  Has meta postamble:   {has_post}/50 ({has_post/50*100:.0f}%)")
print(f"  Has both:             {has_both}/50 ({has_both/50*100:.0f}%)")
print(f"  Has either:           {has_either}/50 ({has_either/50*100:.0f}%)")
print(f"  Pure content (neither): {has_neither}/50 ({has_neither/50*100:.0f}%)")

print(f"\n  By model:")
from collections import defaultdict
model_meta = defaultdict(lambda: {"pre": 0, "post": 0, "either": 0, "n": 0})
for r in rev_results:
    m = model_meta[r["model"]]
    m["n"] += 1
    if r["has_preamble"]: m["pre"] += 1
    if r["has_postamble"]: m["post"] += 1
    if r["has_preamble"] or r["has_postamble"]: m["either"] += 1
for model in sorted(model_meta):
    m = model_meta[model]
    print(f"    {model:<22} pre={m['pre']}/{m['n']}  post={m['post']}/{m['n']}  either={m['either']}/{m['n']}")

# ═══════════════════════════════════════════════════════════════════════════
# 2. 8 EXAMPLES WITH META-WRAPPING MARKED
# ═══════════════════════════════════════════════════════════════════════════
print(f"\n{'=' * 80}")
print("2. 8 EXAMPLES WITH META-WRAPPING (marked)")
print("=" * 80)

wrapped = [r for r in rev_results if r["has_preamble"] or r["has_postamble"]]
# Pick diverse: try to get different models and both/pre-only/post-only
import random
random.seed(42)

both_list = [r for r in wrapped if r["has_preamble"] and r["has_postamble"]]
pre_only = [r for r in wrapped if r["has_preamble"] and not r["has_postamble"]]
post_only = [r for r in wrapped if not r["has_preamble"] and r["has_postamble"]]

examples = []
for pool in [both_list, pre_only, post_only]:
    random.shuffle(pool)
    examples.extend(pool[:3])
random.shuffle(examples)
examples = examples[:8]

for i, r in enumerate(examples, 1):
    text = r["rev_text"]
    print(f"\n  --- EXAMPLE #{i} ({r['model']}, T{r['rev_turn']}, {r['domain']}) ---")
    print(f"  Preamble detected: {repr(r['preamble'])}")
    print(f"  Postamble detected: {repr(r['postamble'])}")
    print(f"  Total length: {r['rev_len']} chars")

    # Find where preamble ends (first code block, first blank line after preamble, etc.)
    # Mark by showing first 200 chars and last 200 chars with annotations
    print(f"\n  >>> FIRST 300 CHARS (preamble zone) <<<")
    first = text[:300]
    if r["has_preamble"]:
        # Find end of preamble: typically before the first \n\n or code block
        preamble_end = None
        for marker in ["\n\n", "\n```", "\n---", "\n#", "\n*", "\n-"]:
            idx = text.find(marker)
            if idx > 0 and idx < 500:
                preamble_end = idx
                break
        if preamble_end:
            print(f"  [META-PREAMBLE]: {repr(text[:preamble_end])}")
            print(f"  [CONTENT STARTS at char {preamble_end}]")
        else:
            print(f"  {first}")
    else:
        print(f"  {first}")

    print(f"\n  >>> LAST 300 CHARS (postamble zone) <<<")
    last = text[-300:]
    if r["has_postamble"]:
        # Find start of postamble
        tail = text[-400:]
        post_start = None
        for marker in ["\n\n"]:
            idx = tail.rfind(marker)
            if idx > 0:
                # Check if the text after this is meta
                candidate = tail[idx:].strip()
                candidate_lower = candidate.lower()
                is_meta = any(re.search(pat, candidate_lower) for pat in POSTAMBLE_PATTERNS)
                if is_meta:
                    post_start = len(text) - 400 + idx
                    break
        if post_start:
            print(f"  [CONTENT ENDS at char {post_start}]")
            print(f"  [META-POSTAMBLE]: {repr(text[post_start:])}")
        else:
            print(f"  {last}")
    else:
        print(f"  {last}")
    print(f"  --- END #{i} ---")

# ═══════════════════════════════════════════════════════════════════════════
# 3. T1-SIDE COMPARISON (asymmetry check)
# ═══════════════════════════════════════════════════════════════════════════
print(f"\n{'=' * 80}")
print("3. T1-SIDE META-COMMENTARY (asymmetry check)")
print("=" * 80)

t1_has_pre = sum(1 for r in t1_results if r["has_preamble"])
t1_has_post = sum(1 for r in t1_results if r["has_postamble"])
t1_has_either = sum(1 for r in t1_results if r["has_preamble"] or r["has_postamble"])
t1_has_neither = 50 - t1_has_either

print(f"\n  T1 side:")
print(f"    Has meta preamble:    {t1_has_pre}/50 ({t1_has_pre/50*100:.0f}%)")
print(f"    Has meta postamble:   {t1_has_post}/50 ({t1_has_post/50*100:.0f}%)")
print(f"    Has either:           {t1_has_either}/50 ({t1_has_either/50*100:.0f}%)")
print(f"    Pure content:         {t1_has_neither}/50 ({t1_has_neither/50*100:.0f}%)")

print(f"\n  Revision side (for comparison):")
print(f"    Has meta preamble:    {has_pre}/50 ({has_pre/50*100:.0f}%)")
print(f"    Has meta postamble:   {has_post}/50 ({has_post/50*100:.0f}%)")
print(f"    Has either:           {has_either}/50 ({has_either/50*100:.0f}%)")
print(f"    Pure content:         {has_neither}/50 ({has_neither/50*100:.0f}%)")

print(f"\n  ASYMMETRY:")
print(f"    Preamble: T1 {t1_has_pre}/50 vs Rev {has_pre}/50 (delta: {has_pre - t1_has_pre})")
print(f"    Postamble: T1 {t1_has_post}/50 vs Rev {has_post}/50 (delta: {has_post - t1_has_post})")
print(f"    Either: T1 {t1_has_either}/50 vs Rev {has_either}/50 (delta: {has_either - t1_has_either})")

# By model
print(f"\n  T1 by model:")
t1_model_meta = defaultdict(lambda: {"pre": 0, "post": 0, "either": 0, "n": 0})
for r in t1_results:
    m = t1_model_meta[r["model"]]
    m["n"] += 1
    if r["has_preamble"]: m["pre"] += 1
    if r["has_postamble"]: m["post"] += 1
    if r["has_preamble"] or r["has_postamble"]: m["either"] += 1
for model in sorted(t1_model_meta):
    m = t1_model_meta[model]
    print(f"    {model:<22} pre={m['pre']}/{m['n']}  post={m['post']}/{m['n']}  either={m['either']}/{m['n']}")

# Show 3 T1 examples with meta-wrapping for comparison
t1_wrapped = [r for r in t1_results if r["has_preamble"] or r["has_postamble"]]
if t1_wrapped:
    print(f"\n  T1 examples with meta-wrapping ({len(t1_wrapped)} total, showing 3):")
    random.shuffle(t1_wrapped)
    for i, r in enumerate(t1_wrapped[:3], 1):
        print(f"\n    T1 Example #{i} ({r['model']}):")
        print(f"    Preamble: {repr(r['preamble'])}")
        print(f"    Postamble: {repr(r['postamble'])}")
        print(f"    First 150 chars: {repr(r['t1_text'][:150])}")
        print(f"    Last 150 chars: {repr(r['t1_text'][-150:])}")
