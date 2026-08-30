#!/usr/bin/env python3
"""Strip separable meta-commentary from both sides of reversibility pairs.
Conservative: only strip clearly separable boilerplate paragraphs.
If a paragraph contains task-relevant meaning, keep it.
"""

import json, sys, re, random, hashlib
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "study3" / "raw_responses"

with open(DATA_DIR / "reversibility_human_pairs.json") as f:
    pairs = json.load(f)
with open(DATA_DIR / "reversibility_human_key.json") as f:
    key_list = json.load(f)
    key_map = {k["pair_id"]: k for k in key_list}

# ── Meta-commentary detection ──

# Preamble: entire paragraph is meta if it matches these AND contains no task content signals
PREAMBLE_META = [
    r"(?:i'?d like to|let me|i'?ll|i want to)\s+(?:revise|make|take|offer|give|try|refine|polish|tighten)",
    r"here'?s (?:the|my|a|an|another) (?:revised|improved|updated|final|slightly|new|definitive)",
    r"(?:sure|okay|alright|absolutely)[,!.]?\s+here",
    r"(?:looking|look) (?:back|at (?:it|this|my))",
    r"(?:after|upon) (?:review|re-?reading|careful review|reflection)",
    r"(?:i've|i have) reviewed",
    r"thank(?:s| you) for (?:the|asking|checking|your|this)",
    r"(?:great|good) (?:question|prompt)",
    r"actually,? let me",
    r"considering the response",
    r"(?:this is a )?(?:very )?(?:solid|strong|great|good|excellent) (?:implementation|version|set|start|draft|point)",
    r"you'?re right to ask",
    r"since you(?:'re| are| repeated| asked|'ve)",
    r"i (?:think|believe) (?:i can|we can|it could|the|this|there's)",
    r"i can make (?:some|a few|one|minor)",
    r"(?:after|upon) re-?reading",
    r"i understand (?:the|your|you're)",
    r"i'?m (?:satisfied|happy|confident) with",
    r"(?:the|this) (?:version|response|output|code|email|post|analysis) (?:is|can be|meets|works)",
]

# Postamble: entire paragraph is meta if it matches these
POSTAMBLE_META = [
    r"let me know (?:if|what|how|whether)",
    r"hope this helps",
    r"feel free to",
    r"(?:happy|glad|ready) to (?:help|assist|revise|adjust|make|answer)",
    r"(?:if you'?d like|would you like|if you want) (?:any|me to|further|more|to|a)",
    r"(?:i'?m|we'?re) (?:here|available|happy) (?:to|if)",
    r"(?:just )?let me know",
    r"(?:what do you think|how does (?:this|that) (?:sound|look|work))",
    r"(?:otherwise|if not),? (?:this|it|we|you|consider|go ahead)",
    r"(?:i believe|i think|i'?m confident) (?:this|it|the) (?:version|is|meets|works|feels)",
    r"(?:ready to|you can) (?:use|go|send|share|present|submit)",
    r"(?:i'?ve|i have) made (?:some|minor|a few)",
    r"(?:do you|would you) (?:want|like|need) (?:me to|any)",
    r"(?:this is|consider this|go ahead).{0,30}(?:final|done|ready|yours)",
    r"if (?:this|that) works for you",
    r"(?:if you|you can) (?:have|need|want) any (?:questions|concerns|feedback)",
    r"(?:congratulations|best of luck|good luck)",
    r"please let me know",
]

# Task content signals: if a paragraph contains these, do NOT strip it even if it matches meta
CONTENT_SIGNALS = [
    r"```",                         # code block
    r"^\s*[-*]\s+\*\*",           # markdown list with bold
    r"^\s*\d+\.\s",               # numbered list
    r"^\s*#{1,4}\s",              # markdown headers
    r"\bdef\s+\w+\(",            # python function
    r"\bfunction\s+\w+\(",       # js function
    r"\bclass\s+\w+",            # class definition
    r"^\s*\|.*\|",               # table row
    r"Subject:",                   # email subject line
    r"^(?:Hi|Dear|Hello)\s+\w+", # email greeting (task content for emails)
    r"\$\d+",                     # dollar amounts (analysis content)
    r"\d+%",                      # percentages (analysis content)
    r"(?:domestic|international|express)", # domain-specific for shipping
]

def is_meta_paragraph(text, patterns):
    """Check if a paragraph is purely meta-commentary."""
    text_lower = text.strip().lower()
    if len(text_lower) < 5:
        return False
    # Check for content signals first -- if present, NOT meta
    for sig in CONTENT_SIGNALS:
        if re.search(sig, text, re.MULTILINE | re.IGNORECASE):
            return False
    # Check if it matches any meta pattern
    for pat in patterns:
        if re.search(pat, text_lower):
            return True
    return False


def split_paragraphs(text):
    """Split text into paragraphs at double-newlines, preserving separators."""
    # Split at \n\n but also at \n---\n
    parts = re.split(r'(\n\n+|\n---+\n)', text)
    return parts


def strip_text(text):
    """Strip leading meta-preamble and trailing meta-postamble paragraphs.
    Conservative: only strips clearly separable paragraphs.
    """
    if not text or len(text.strip()) < 50:
        return text

    parts = split_paragraphs(text)

    # Strip leading meta paragraphs
    # Walk forward: strip paragraphs that are purely meta, stop at first content
    strip_front = 0
    i = 0
    while i < len(parts):
        part = parts[i].strip()
        if not part or re.match(r'^---+$', part):
            # separator or empty -- check next
            i += 1
            continue
        if is_meta_paragraph(part, PREAMBLE_META):
            strip_front = i + 1
            # Also consume the following separator
            if i + 1 < len(parts) and not parts[i+1].strip():
                strip_front = i + 2
            i += 1
        else:
            break
        i += 1

    # Strip trailing meta paragraphs
    # Walk backward: strip paragraphs that are purely meta, stop at first content
    strip_back = len(parts)
    i = len(parts) - 1
    while i >= strip_front:
        part = parts[i].strip()
        if not part or re.match(r'^---+$', part):
            i -= 1
            continue
        if is_meta_paragraph(part, POSTAMBLE_META):
            strip_back = i
            # Also consume the preceding separator
            if i - 1 >= strip_front and not parts[i-1].strip():
                strip_back = i - 1
            i -= 1
        else:
            break
        i -= 1

    # Reconstruct
    kept = parts[strip_front:strip_back]
    result = "".join(kept).strip()

    # Safety: if we stripped too aggressively and result is < 30% of original, revert
    if len(result) < len(text.strip()) * 0.3:
        return text.strip()

    return result if result else text.strip()


# ── Process all 50 pairs ──

# Re-randomize A/B positions with new seed
random.seed(20260609_2)  # different seed from original build

stripped_pairs = []
new_key = []
before_after = []  # for verification

for p, k in zip(pairs, key_list):
    # Identify T1 and revision text from ORIGINAL
    if k["A_is"] == "T1":
        t1_orig = p["output_A"]
        rev_orig = p["output_B"]
    else:
        t1_orig = p["output_B"]
        rev_orig = p["output_A"]

    # Strip both sides
    t1_stripped = strip_text(t1_orig)
    rev_stripped = strip_text(rev_orig)

    # Re-randomize position
    if random.random() < 0.5:
        out_a = t1_stripped
        out_b = rev_stripped
        a_is = "T1"
        b_is = f"T{k['last_rev_turn']}"
    else:
        out_a = rev_stripped
        out_b = t1_stripped
        a_is = f"T{k['last_rev_turn']}"
        b_is = "T1"

    # New opaque pair_id (different from original)
    h = hashlib.md5((k["trial_id"] + "_stripped").encode()).hexdigest()[:8].upper()
    new_pair_id = f"S{h}"

    stripped_pairs.append({
        "pair_id": new_pair_id,
        "task_prompt": p["task_prompt"],
        "output_A": out_a,
        "output_B": out_b,
    })

    new_key.append({
        "pair_id": new_pair_id,
        "trial_id": k["trial_id"],
        "model": k["model"],
        "domain": k["domain"],
        "last_rev_turn": k["last_rev_turn"],
        "A_is": a_is,
        "B_is": b_is,
    })

    before_after.append({
        "pair_id": new_pair_id,
        "old_pair_id": p["pair_id"],
        "model": k["model"],
        "domain": k["domain"],
        "t1_orig": t1_orig,
        "t1_stripped": t1_stripped,
        "t1_removed_front": len(t1_orig) - len(t1_stripped) if len(t1_orig) > len(t1_stripped) else 0,
        "rev_orig": rev_orig,
        "rev_stripped": rev_stripped,
        "rev_removed_chars": len(rev_orig) - len(rev_stripped),
    })

# ── Save files ──

# Stripped pairs
stripped_path = DATA_DIR / "reversibility_pairs_stripped.json"
with open(stripped_path, "w") as f:
    json.dump(stripped_pairs, f, indent=2)
print(f"Saved {len(stripped_pairs)} stripped pairs -> {stripped_path}")

# New key
stripped_key_path = DATA_DIR / "reversibility_stripped_key.json"
with open(stripped_key_path, "w") as f:
    json.dump(new_key, f, indent=2)
print(f"Saved key -> {stripped_key_path}")

# Null judgment files
null_judgments = [{"pair_id": p["pair_id"], "task_prompt": p["task_prompt"],
                   "output_A": p["output_A"], "output_B": p["output_B"],
                   "judgment": None} for p in stripped_pairs]
liam_path = DATA_DIR / "reversibility_judgments_liam.json"
troy_path = DATA_DIR / "reversibility_judgments_troy.json"
with open(liam_path, "w") as f:
    json.dump(null_judgments, f, indent=2)
with open(troy_path, "w") as f:
    json.dump(null_judgments, f, indent=2)
print(f"Saved null judgment files (overwritten liam + troy)")

# ── Save meta-wrapping asymmetry summary ──
asymmetry_path = DATA_DIR / "meta_wrapping_asymmetry.json"
asymmetry = {
    "description": "Meta-commentary wrapping asymmetry in reversibility pairs (50 pairs, original unstripped)",
    "revision_side": {
        "has_preamble": 38,
        "has_postamble": 24,
        "has_both": 20,
        "has_either": 42,
        "pure_content": 8,
        "total": 50,
    },
    "t1_side": {
        "has_preamble": 4,
        "has_postamble": 5,
        "has_both": 2,
        "has_either": 7,
        "pure_content": 43,
        "total": 50,
    },
    "asymmetry_delta": {
        "preamble": 34,
        "postamble": 19,
        "either": 35,
    },
    "note": "Meta-commentary is separable boilerplate (preambles like 'Here is my revised version', postambles like 'Let me know if you would like changes'). Not woven into task content."
}
with open(asymmetry_path, "w") as f:
    json.dump(asymmetry, f, indent=2)
print(f"Saved asymmetry summary -> {asymmetry_path}")

# ── A/B position split ──
a_is_t1 = sum(1 for k in new_key if k["A_is"] == "T1")
print(f"\nNew A/B position split: A=T1 in {a_is_t1}/50 ({a_is_t1/50*100:.0f}%), A=rev in {50-a_is_t1}/50 ({(50-a_is_t1)/50*100:.0f}%)")

# ── Stripping summary ──
rev_changed = sum(1 for ba in before_after if ba["rev_removed_chars"] > 0)
t1_changed = sum(1 for ba in before_after if ba["t1_removed_front"] > 0)
rev_chars_removed = [ba["rev_removed_chars"] for ba in before_after if ba["rev_removed_chars"] > 0]
t1_chars_removed = [ba["t1_removed_front"] for ba in before_after if ba["t1_removed_front"] > 0]

print(f"\nStripping summary:")
print(f"  Revision side: {rev_changed}/50 modified")
if rev_chars_removed:
    print(f"    Chars removed: median={sorted(rev_chars_removed)[len(rev_chars_removed)//2]}, max={max(rev_chars_removed)}")
print(f"  T1 side: {t1_changed}/50 modified")
if t1_chars_removed:
    print(f"    Chars removed: median={sorted(t1_chars_removed)[len(t1_chars_removed)//2]}, max={max(t1_chars_removed)}")

# ── 6 Before/After examples ──
# Pick: 2 with heavy revision stripping, 2 with moderate, 1 with T1 stripping, 1 unchanged
print(f"\n{'=' * 80}")
print("BEFORE/AFTER EXAMPLES (6 pairs)")
print("=" * 80)

heavy = sorted([ba for ba in before_after if ba["rev_removed_chars"] > 200], key=lambda x: -x["rev_removed_chars"])
moderate = sorted([ba for ba in before_after if 50 < ba["rev_removed_chars"] <= 200], key=lambda x: -x["rev_removed_chars"])
t1_stripped_list = [ba for ba in before_after if ba["t1_removed_front"] > 0]
unchanged = [ba for ba in before_after if ba["rev_removed_chars"] == 0 and ba["t1_removed_front"] == 0]

examples = []
if len(heavy) >= 2: examples.extend(heavy[:2])
if len(moderate) >= 2: examples.extend(moderate[:2])
if t1_stripped_list: examples.append(t1_stripped_list[0])
if unchanged: examples.append(unchanged[0])

# Fill to 6 if needed
remaining = [ba for ba in before_after if ba not in examples]
random.shuffle(remaining)
while len(examples) < 6 and remaining:
    examples.append(remaining.pop(0))

for i, ba in enumerate(examples, 1):
    print(f"\n  {'=' * 76}")
    print(f"  EXAMPLE #{i} | {ba['model']} | {ba['domain']} | rev_removed={ba['rev_removed_chars']} chars | t1_removed={ba['t1_removed_front']} chars")
    print(f"  {'=' * 76}")

    # Revision side
    print(f"\n  REVISION SIDE (T{[k for k in new_key if k['pair_id'] == ba['pair_id']][0]['last_rev_turn']}):")
    print(f"  --- BEFORE ({len(ba['rev_orig'])} chars) ---")
    print(f"  {ba['rev_orig'][:500]}")
    if len(ba['rev_orig']) > 500:
        print(f"  [...middle...]")
        print(f"  {ba['rev_orig'][-300:]}")
    print(f"  --- AFTER ({len(ba['rev_stripped'])} chars) ---")
    print(f"  {ba['rev_stripped'][:500]}")
    if len(ba['rev_stripped']) > 500:
        print(f"  [...middle...]")
        print(f"  {ba['rev_stripped'][-300:]}")

    # T1 side
    print(f"\n  T1 SIDE:")
    print(f"  --- BEFORE ({len(ba['t1_orig'])} chars) ---")
    print(f"  {ba['t1_orig'][:400]}")
    if len(ba['t1_orig']) > 400:
        print(f"  [... +{len(ba['t1_orig'])-400} chars]")
    print(f"  --- AFTER ({len(ba['t1_stripped'])} chars) ---")
    print(f"  {ba['t1_stripped'][:400]}")
    if len(ba['t1_stripped']) > 400:
        print(f"  [... +{len(ba['t1_stripped'])-400} chars]")
