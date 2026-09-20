#!/usr/bin/env python3
"""
Check the ten hand-corrected classifier labels: what they are, whether the Methods
description of them holds, how many comparable rows were left uncorrected, and whether
the balanced-panel cliff depends on any of it.

Written 2026-09-20 after an audit found the ten `[CORRECTED]` records carry no code trace
and no stated decision rule. The Methods sentence describing them rests on this check, so
the script lives in the analysis tree rather than in .workspace/.

    python3 scripts/study3/audit_hand_corrections.py

Input:  data/study3/raw_responses/genuine_meta_labels.jsonl
        data/study3/raw_responses/worker_trials.jsonl
        data/study3/raw_responses/stripped_rescore_full.jsonl
Output: stdout only. Results are recorded in results_FINAL.md section 15.
"""
import collections
import json
import re
import sys
from pathlib import Path

from scipy.stats import wilcoxon

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "data" / "study3" / "raw_responses"

# The discriminator that selects the ten: an explicit refusal to revise at the head of the
# response. Matched against the first 240 characters, which is where the refusal sits in
# every one of the ten; deeper in the text the same phrases appear inside genuine revisions
# as reported speech.
HEAD_CHARS = 240
DECLINE = re.compile(
    r"(i'?d like to keep|i would like to keep"
    r"|keep (this|the original|the very first|it) as (my |the )?final"
    r"|no (further )?(revision|change)s? (are |is )?needed|no revisions? needed"
    r"|this is (my|the) final)", re.I)

# Sentences shorter than this are boilerplate ("Here it is again.") and match everywhere.
MIN_SENTENCE = 25


def norm(s):
    return re.sub(r"\s+", " ", s or "").strip().lower()


def recode(level):
    """Level 6 recodes to level 2 throughout the project."""
    return 2 if level == 6 else level


def load():
    trials = {}
    for line in (RAW / "worker_trials.jsonl").open(encoding="utf8"):
        r = json.loads(line)
        trials[r["trial_id"]] = r
    rows = [json.loads(l) for l in (RAW / "genuine_meta_labels.jsonl").open(encoding="utf8")]
    scores = {}
    for line in (RAW / "stripped_rescore_full.jsonl").open(encoding="utf8"):
        r = json.loads(line)
        scores[(r["trial_id"], r["turn"])] = r["stripped_score"]
    return trials, rows, scores


def containment(resp, i):
    """Largest share of any EARLIER turn's substantive sentences reappearing at turn i."""
    cur, best = norm(resp[i]), 0.0
    for j in range(i):
        sents = [s for s in re.split(r"(?<=[.!?])\s+|\n+", resp[j] or "")
                 if len(s.strip()) > MIN_SENTENCE]
        if sents:
            best = max(best, sum(1 for s in sents if norm(s) in cur) / len(sents))
    return best


def response_at(trials, row):
    t = trials.get(row["trial_id"])
    if not t:
        return None, None
    i = row["turn"] - 1
    if i < 1 or i >= len(t["responses"]) or not t["responses"][i]:
        return None, None
    return t["responses"], i


def cliff(ids, scores, label):
    pairs = [(recode(scores[(t, 1)]), recode(scores[(t, 5)])) for t in sorted(ids)
             if (t, 1) in scores and (t, 5) in scores]
    first = [a for a, _ in pairs]
    last = [b for _, b in pairs]
    deltas = [b - a for a, b in pairs]
    w, p = wilcoxon(first, last)
    mean = lambda xs: sum(xs) / len(xs)
    print(f"  {label:<28} n={len(pairs):<3} T1 {mean(first):.2f}  T5 {mean(last):.2f}  "
          f"delta {mean(deltas):+.2f}  W {w}  p {p:.2e}  non-zero {sum(1 for d in deltas if d)}")
    return round(mean(deltas), 2), len(pairs)


def main():
    trials, rows, scores = load()

    corrected = [r for r in rows if "[CORRECTED]" in str(r["reason"])]
    assert len(corrected) == 10, f"expected 10 corrected records, found {len(corrected)}"
    assert all(r["classifier_label"] == "META" for r in corrected), \
        "a corrected record is not labelled META; the correction direction has changed"

    print("The ten hand corrections")
    for r in corrected:
        resp, i = response_at(trials, r)
        head = bool(DECLINE.search(norm(resp[i])[:HEAD_CHARS])) if resp else None
        print(f"  {r['trial_id'][:50]:<50} t{r['turn']}  "
              f"containment {containment(resp, i):.2f}  refusal-at-head {head}")

    genuine = [r for r in rows if r["classifier_label"] == "GENUINE"]
    matched = []
    for r in genuine:
        resp, i = response_at(trials, r)
        if resp and DECLINE.search(norm(resp[i])[:HEAD_CHARS]):
            matched.append(r)
    print(f"\nGENUINE rows screened: {len(genuine)}")
    print(f"Rows matching the same discriminator, left uncorrected: {len(matched)}")
    assert len(genuine) == 718, f"genuine label count moved: {len(genuine)}"
    assert len(matched) == 25, f"uncorrected match count moved: {len(matched)}"

    by_trial = collections.defaultdict(dict)
    for r in rows:
        by_trial[r["trial_id"]][r["turn"]] = r["classifier_label"]
    panel = {t for t, d in by_trial.items() if all(d.get(k) == "GENUINE" for k in (2, 3, 4, 5))}
    drop = {r["trial_id"] for r in matched} & panel
    assert len(panel) == 50, f"balanced panel is no longer 50 trials: {len(panel)}"

    print(f"\nBalanced panel {len(panel)} trials; applying the rule would remove {len(drop)}")
    print("Cliff, both ways:")
    published, n_pub = cliff(panel, scores, "as published")
    applied, _ = cliff(panel - drop, scores, "rule applied")
    cliff({t for t in panel if "llama" in t}, scores, "llama only, as published")
    cliff({t for t in panel - drop if "llama" in t}, scores, "llama only, rule applied")

    # The published figure is the check on the whole reconstruction, not a result.
    assert (published, n_pub) == (-0.74, 50), \
        f"the published cliff no longer reproduces: {published} on n={n_pub}"
    print(f"\nThe published -0.74 reproduces. The rule-applied panel gives {applied:+.2f}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
