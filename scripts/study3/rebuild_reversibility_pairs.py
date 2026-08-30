#!/usr/bin/env python3
"""Rebuild 50-pair reversibility annotation set using clean LLM classifier labels."""

import json, sys, random, hashlib
from pathlib import Path
from collections import defaultdict

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from scripts.utils import load_jsonl
from scripts.config import S3_WORKER_TRIALS_PATH

DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "study3" / "raw_responses"

# Load LLM labels
llm_map = {}  # (trial_id, turn) -> classifier_label
with open(DATA_DIR / "genuine_meta_labels.jsonl") as f:
    for line in f:
        r = json.loads(line)
        llm_map[(r["trial_id"], r["turn"])] = r["classifier_label"]

# Load trials
trials = load_jsonl(S3_WORKER_TRIALS_PATH)
trials = [t for t in trials if t.get("status") == "success"]

# For each trial, find the latest turn labeled GENUINE (post-T1)
eligible = []
for trial in trials:
    last_genuine_turn = None
    for turn in [5, 4, 3, 2]:  # search from latest
        if llm_map.get((trial["trial_id"], turn)) == "GENUINE":
            last_genuine_turn = turn
            break
    if last_genuine_turn is not None:
        eligible.append({
            "trial_id": trial["trial_id"],
            "model": trial["model"],
            "domain": trial["domain"],
            "task_prompt": trial["task_prompt"],
            "t1_text": trial["responses"][0],
            "last_genuine_turn": last_genuine_turn,
            "last_genuine_text": trial["responses"][last_genuine_turn - 1],
        })

print(f"Eligible trials (have at least one genuine post-T1 revision): {len(eligible)} / {len(trials)}")

# Stratification report
print(f"\nBy model:")
model_counts = defaultdict(int)
for e in eligible:
    model_counts[e["model"]] += 1
for m in sorted(model_counts):
    print(f"  {m:<22} {model_counts[m]}")

print(f"\nBy domain:")
domain_counts = defaultdict(int)
for e in eligible:
    domain_counts[e["domain"]] += 1
for d in sorted(domain_counts):
    print(f"  {d:<22} {domain_counts[d]}")

# Stratified sampling: draw proportionally from model x domain cells
random.seed(20260609)

cells = defaultdict(list)
for e in eligible:
    cells[(e["model"], e["domain"])].append(e)

# First pass: one from each cell that has entries (up to 50)
selected = []
cell_keys = list(cells.keys())
random.shuffle(cell_keys)

for key in cell_keys:
    if len(selected) >= 50:
        break
    pool = cells[key]
    pick = random.choice(pool)
    selected.append(pick)

# If under 50, draw more from remaining pool
if len(selected) < 50:
    selected_ids = {s["trial_id"] for s in selected}
    remaining = [e for e in eligible if e["trial_id"] not in selected_ids]
    random.shuffle(remaining)
    while len(selected) < 50 and remaining:
        selected.append(remaining.pop(0))

print(f"\nSelected {len(selected)} pairs")

# Verify stratification of selected
print(f"\nSelected by model:")
sel_model = defaultdict(int)
for s in selected:
    sel_model[s["model"]] += 1
for m in sorted(sel_model):
    print(f"  {m:<22} {sel_model[m]}")

print(f"\nSelected by domain:")
sel_domain = defaultdict(int)
for s in selected:
    sel_domain[s["domain"]] += 1
for d in sorted(sel_domain):
    print(f"  {d:<22} {sel_domain[d]}")

# Build pairs with randomized A/B position
pairs = []
key_entries = []
a_is_t1_count = 0

for s in selected:
    # Generate opaque pair_id
    h = hashlib.md5(s["trial_id"].encode()).hexdigest()[:8].upper()
    pair_id = f"P{h}"

    # Randomize position
    if random.random() < 0.5:
        output_a = s["t1_text"]
        output_b = s["last_genuine_text"]
        a_is = "T1"
        b_is = f"T{s['last_genuine_turn']}"
        a_is_t1_count += 1
    else:
        output_a = s["last_genuine_text"]
        output_b = s["t1_text"]
        a_is = f"T{s['last_genuine_turn']}"
        b_is = "T1"

    pairs.append({
        "pair_id": pair_id,
        "task_prompt": s["task_prompt"],
        "output_A": output_a,
        "output_B": output_b,
    })

    key_entries.append({
        "pair_id": pair_id,
        "trial_id": s["trial_id"],
        "model": s["model"],
        "domain": s["domain"],
        "last_rev_turn": s["last_genuine_turn"],
        "A_is": a_is,
        "B_is": b_is,
    })

print(f"\nA/B position split: A=T1 in {a_is_t1_count}/{len(pairs)} ({a_is_t1_count/len(pairs)*100:.0f}%), A=revision in {len(pairs)-a_is_t1_count}/{len(pairs)} ({(len(pairs)-a_is_t1_count)/len(pairs)*100:.0f}%)")

# Verify: every "final" side is GENUINE-labeled
print(f"\nVerification: checking all 'final revision' sides are GENUINE-labeled...")
failures = 0
for i, (s, k) in enumerate(zip(selected, key_entries)):
    tid = s["trial_id"]
    rev_turn = s["last_genuine_turn"]
    label = llm_map.get((tid, rev_turn), "MISSING")
    if label != "GENUINE":
        print(f"  FAIL: pair {k['pair_id']} trial {tid} T{rev_turn} labeled {label}")
        failures += 1
    # Also check text is not a short decline
    rev_text = s["last_genuine_text"]
    if len(rev_text) < 100:
        print(f"  WARNING: pair {k['pair_id']} revision text very short ({len(rev_text)} chars)")
print(f"  Failures: {failures}")
print(f"  All final-revision sides are GENUINE-labeled: {'YES' if failures == 0 else 'NO'}")

# Check for any decline phrases in the revision text (belt and suspenders)
decline_phrases = [
    "keep this as my final", "this is my final version",
    "i'd like to keep this", "i would like to keep this",
    "no changes needed", "no improvements needed",
    "no further changes", "nothing to improve",
]
decline_hits = 0
for s in selected:
    head = s["last_genuine_text"][:300].lower()
    for phrase in decline_phrases:
        if phrase in head:
            print(f"  DECLINE-PHRASE HIT: {s['trial_id']} T{s['last_genuine_turn']} contains '{phrase}'")
            decline_hits += 1
            break
print(f"  Decline-phrase hits in revision text: {decline_hits}")

# Last genuine turn distribution
print(f"\nLast genuine turn distribution in selected:")
turn_dist = defaultdict(int)
for s in selected:
    turn_dist[s["last_genuine_turn"]] += 1
for t in sorted(turn_dist):
    print(f"  T{t}: {turn_dist[t]}")

# Save files
pairs_path = DATA_DIR / "reversibility_human_pairs.json"
key_path = DATA_DIR / "reversibility_human_key.json"
liam_path = DATA_DIR / "reversibility_judgments_liam.json"
troy_path = DATA_DIR / "reversibility_judgments_troy.json"

# Pairs (annotation site data)
with open(pairs_path, "w") as f:
    json.dump(pairs, f, indent=2)
print(f"\nSaved {len(pairs)} pairs -> {pairs_path}")

# Key (not exposed to annotators)
with open(key_path, "w") as f:
    json.dump(key_entries, f, indent=2)
print(f"Saved key -> {key_path}")

# Null judgment files
null_judgments = [{"pair_id": p["pair_id"], "task_prompt": p["task_prompt"],
                   "output_A": p["output_A"], "output_B": p["output_B"],
                   "judgment": None} for p in pairs]
with open(liam_path, "w") as f:
    json.dump(null_judgments, f, indent=2)
with open(troy_path, "w") as f:
    json.dump(null_judgments, f, indent=2)
print(f"Saved null judgment files for liam and troy")

print(f"\nDONE. Ready for annotation.")
