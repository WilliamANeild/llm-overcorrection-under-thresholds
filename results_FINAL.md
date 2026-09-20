# Study 3 Results -- FINAL (Corrected/Stripped Basis)

Generated: 2026-06-10. All numbers use the corrected LLM classifier (718 GENUINE / 2,162 META)
and stripped meta-commentary where applicable. These are the definitive numbers for paper writing.

---

## 1. CLASSIFIER

- **Final counts:** 718 GENUINE, 2,162 META (total 2,880 post-T1 observations)
- **10 corrections** applied (GENUINE -> META): 6 Llama, 2 DeepSeek, 1 Qwen, 1 Claude
  - All were decline-with-restatement mislabeled as GENUINE
  - Correction rate: 10/718 = **1.4%** of GENUINE labels corrected
- **Validation:** keyword classifier (old) vs LLM classifier (corrected) differ on 85 "complete-revision" trials
  - Old keyword: 135 trials pass "revised at all 5 turns"
  - Corrected LLM: 50 trials have GENUINE at all T2-T5
  - The keyword classifier systematically missed verbose decline-with-restatement responses
- Source: `data/study3/raw_responses/genuine_meta_labels.jsonl`
- **Filter:** Each of 2,880 rows = (trial_id, turn) for turns 2-5 across 720 trials. Field `classifier_label` in {GENUINE, META}. Rows with `[CORRECTED]` in `reason` field are the 10 manual corrections.

---

## 2. THE CLIFF (Quality Trajectory)

### Balanced Panel (GENUINE at all T2-T5)

| Metric | Value |
|--------|-------|
| N | 50 |
| T1 mean | 3.66 |
| T5 mean | 2.72 |
| Delta (T5-T1) | **-0.94** |
| Wilcoxon p | 3.32e-06 |
| Effect size r | 0.658 |

- **Filter:** Select trials where `genuine_meta_labels.jsonl` has `classifier_label == "GENUINE"` at ALL of turns 2, 3, 4, 5. For each, pull `level` from `evaluator_results.jsonl` at turn 1 and turn 5 (keyed by `worker_trial_id` + `turn`). Recode level 6 -> 2. Paired Wilcoxon signed-rank on (T1, T5) pairs. Effect size r = |Z| / sqrt(N).

### Per-Model (balanced panel)

| Model | n | T1 | T5 | Delta | p | r |
|-------|---|----|----|-------|---|---|
| llama-3.3-70b | 45 | 3.53 | 2.71 | **-0.82** | 1.81e-05 | 0.639 |
| qwen-3-235b | 3 | 5.00 | 2.00 | -3.00 | n<5 | -- |
| claude-sonnet-4 | 2 | 4.50 | 4.00 | -0.50 | n<5 | -- |
| gpt-4o | 0 | -- | -- | -- | -- | -- |
| deepseek-v4 | 0 | -- | -- | -- | -- | -- |
| gemini-2.5-flash | 0 | -- | -- | -- | -- | -- |

**NOTE:** GPT-4o, DeepSeek, and Gemini have ZERO balanced-panel trials (no trials with GENUINE at all T2-T5). The balanced panel is 90% Llama. Only Llama's cliff is statistically powered. Claude and Qwen are underpowered (n=2, n=3).

**DISCLOSURE -- Revision Style:** Llama revises incrementally (mean SequenceMatcher similarity to prior turn = 0.50, median 0.51) while other models that revise tend toward wholesale rewrites (mean similarity 0.15--0.34). The cliff is therefore best-powered for incremental-revision behavior. However, wholesale-rewrite models show *steeper* drops when they do comply: DeepSeek -1.71 (n=7 at T5), Qwen -3.00 (n=6), vs Llama -0.81 (n=64). The cliff is not a Llama-specific artifact; it is a general pattern that is only statistically powered in Llama due to its high compliance rate. Audited 2026-06-11.

### Stripped Cliff: significance test (added 2026-09-07, resolving RECOMPUTE_TODO)

The paper printed p and r for the stripped cliff in `results_v2.tex` Table 3, the conclusion
and the appendix, with no entry anywhere in this ledger. Recomputed 2026-09-07 and recorded
here. `RECOMPUTE_TODO.md` asked for exactly this and was closed in error on 2026-09-02.

| Subset | n | T1 | T5 | delta | Wilcoxon W | p | r (N=n) | r (N=non-zero) |
|--------|---|----|----|-------|-----------|---|---------|----------------|
| All balanced | 50 | 3.66 | 2.92 | **-0.74** | 54.5 | **1.01e-4** | 0.536 | 0.681 |
| Llama only | 45 | 3.53 | 2.87 | **-0.67** | 51.5 | **3.76e-4** | 0.514 | 0.652 |

- **Filter:** the 50 balanced-panel trials (GENUINE at all of turns 2-5). Stripped levels at
  turns 1 and 5 from `stripped_rescore_full.jsonl` field `stripped_score`, 6 -> 2 recode
  applied first. Two-sided Wilcoxon signed-rank on the paired values. Non-zero differences:
  31 of 50 all-balanced, 28 of 45 Llama.
- **Both p-values reproduce the printed values exactly.** The numbers were correct; they had
  no recorded provenance.

**TWO DISCREPANCIES, both requiring a decision:**

1. **Effect size. WITHDRAWN 2026-09-17. This discrepancy was an artifact of the 2026-09-07
   recomputation, not a defect in the paper.** The note below is kept for the record.

   > The paper prints r = 0.55 (all) and r = 0.53 (Llama). Recomputation gives 0.536 and 0.514
   > dividing by N = all trials, or 0.681 and 0.652 dividing by N = non-zero differences. The
   > printed values match neither.

   Both candidate values came from an **uncorrected** Wilcoxon z. With the tie-corrected z,
   which is the statistic this ledger's own accepted unstripped figures already use, r = |z|/sqrt(n)
   gives **0.5498 for the all-balanced stripped cliff and 0.5301 for Llama**, which are exactly
   the printed 0.55 and 0.53.

   The consistency check that settles it: the unstripped r of 0.658 recorded at line 34 and
   0.639 at line 42 are not in dispute. Tie-corrected they recompute as 0.6576 and 0.6391, which
   round to the recorded values. Uncorrected they give 0.6416 and 0.6193, which do not. So the
   convention in use throughout is the tie-corrected z over the square root of the trial count,
   and the stripped values follow it precisely.

   Verified twice on 2026-09-17, independently, from `stripped_rescore_full.jsonl` and
   `evaluator_results.jsonl` with the 6->2 recode and the balanced-panel filter as specified
   above. The p-values reproduce exactly as already recorded (1.011e-4 and 3.760e-4).

   **What does survive:** the paper states r without saying which N the z is divided by, and the
   two defensible divisors give 0.55 against 0.70 for the same result. Stating the formula is
   still worth doing. That is a disclosure point, not an error.

2. **Llama delta.** This computation gives -0.67 from the full 3,600-output rescore. The paper
   prints -0.69, which comes from the 50-pair rescore in `stripped_rescore_results.json`. Table 3
   therefore mixes two rescore bases in one table: an all-balanced row on the full rescore and a
   Llama row on the 50-pair rescore. Independently confirms the finding in
   `paper/reference/stats_07_own_inventory.md` (mismatch M1).

### Stripped Cliff (meta-commentary removed, re-scored)

| Subset | Orig cliff | Stripped cliff | Meta inflation |
|--------|-----------|---------------|----------------|
| All (n=50) | -0.94 | **-0.76** | 0.18 (19%) |
| Llama (n=45) | -0.82 | **-0.69** | 0.13 (16%) |
| Llama excl. near-trivial (n=39) | -0.79 | **-0.69** | 0.10 (13%) |

**The cliff is 81% real content degradation, 19% meta-commentary artifact.**

**DISCLOSURE -- Near-Trivial Edits:** 6 of 45 Llama balanced-panel trials contain at least one turn with >0.95 similarity to the prior turn (restatements with minimal change; 4 of these are character-identical, similarity = 1.00). Removing these 6 trials, the Llama cliff is -0.79 (p=8.69e-05, r=0.628) unstripped and -0.69 stripped, compared to -0.82 / -0.69 with all 45. The finding survives; the near-trivial trials account for 0.03 points of the unstripped cliff and zero of the stripped cliff. Affected trial IDs: `agile_vs_waterfall__run1`, `budget_allocation__run2`, `budget_allocation__run3`, `debug_sort__run2`, `sample_size_justification__run3`, `spreadsheet_formula__run3`. Audited 2026-06-11.

- Source (original scores): `data/study3/raw_responses/evaluator_results.jsonl`
- Source (stripped rescore): `data/study3/raw_responses/stripped_rescore_results.json`
- **Filter (stripped rescore):** Same 50 balanced-panel trials. For each, strip meta-commentary from T1 and T5 text using regex preamble/postamble patterns (from `strip_meta_commentary.py`). Re-score stripped text via Claude Sonnet 4 (`claude-sonnet-4-20250514`) at temperature 0 using the same EVAL_PROMPT from `phase2_evaluator.py`. Recode 6 -> 2. Compare original vs stripped scores.

---

## 3. REVISION RATE

| Turn | Genuine revisions | Rate |
|------|-------------------|------|
| T2 | 283/720 | 39.3% |
| T3 | 185/720 | 25.7% |
| T4 | 154/720 | 21.4% |
| T5 | 96/720 | 13.3% |

- **Filter:** For each turn T in {2,3,4,5}, count trials where `genuine_meta_labels.jsonl` has `classifier_label == "GENUINE"` at that turn. Denominator = 720 (all successful trials).
- Source: `data/study3/raw_responses/genuine_meta_labels.jsonl`

---

## 4. REVISION-DESPITE-SUFFICIENCY

| Metric | Value |
|--------|-------|
| T1 sufficiency rate | 631/720 (87.6%) |
| Sufficient turns with revision at next | 368/938 = **39.2%** |
| Bootstrap 95% CI | [36.1%, 42.3%] |

- **Filter:** For every (trial, turn) pair where turn in {1,2,3,4}, pull `level` from `evaluator_results.jsonl` (recode 6 -> 2). If level >= 4 ("sufficient"), check whether `genuine_meta_labels.jsonl` has `classifier_label == "GENUINE"` at turn+1. Numerator = sufficient turns where next turn is GENUINE. Denominator = all sufficient turns (938). Bootstrap: 1000 resamples, percentile CI, seed 42.
- **T1 sufficiency:** Count of trials where evaluator level at turn 1 >= 4 (after 6 -> 2 recode). 631/720 = 87.6%.
- Source: `evaluator_results.jsonl` + `genuine_meta_labels.jsonl`

---

## 4b. DIRECTION OF REVISIONS (added 2026-09-03)

Does a genuine revision lower, leave, or raise the quality level of what it replaced?

- **Script:** `scripts/study3/revision_direction.py`
- **Output:** `data/study3/analysis/revision_direction.json`
- **Sample:** unchanged. The same 720 trials and the same GENUINE/META labels from the
  validated classifier. No sample restriction, no balanced-panel requirement.
- **Filter (exact):** For each trial, walk turns 2-5. Where `genuine_meta_labels.jsonl`
  has `classifier_label == "GENUINE"` at that turn, compare its level against the level
  of the most recent turn whose content was genuinely new: turn 1, or the last turn
  labelled GENUINE. Recode level 6 -> 2 first. Comparing against turn t-1 directly would
  score a revision against a meta-response, whose text is a restatement rather than a
  distinct draft. Direction is `worse` / `same` / `better` on the recoded level.
  Stripped scores from `stripped_rescore_full.jsonl` field `stripped_score`; unstripped
  from `evaluator_results.jsonl` field `level`. Stripped is primary.
- **Tests:** one-sided binomial sign test on worse against better, ties excluded;
  Clopper-Pearson exact 95% CI on the share worse among movers; chi-square on the
  worse-by-better contingency across the five domains; Fisher exact on objective
  (code + data_logic) against subjective (creative + writing).

### Overall (n = 718 genuine revisions)

| Basis | worse | same | better | movers | % of movers worse | 95% CI | sign p |
|-------|-------|------|--------|--------|-------------------|--------|--------|
| **Stripped** | 199 (27.7%) | 432 (60.2%) | 87 (12.1%) | 286 | **69.6%** | [63.9%, 74.9%] | 1.48e-11 |
| Unstripped | 245 (34.1%) | 398 (55.4%) | 75 (10.4%) | 320 | 76.6% | [71.5%, 81.1%] | 1.66e-22 |

Most revisions (60.2% stripped) do not move the level at all, which is partly the
coarseness of a six-level scale. Among those that do move it, the movement is
asymmetric: down about 2.3 times as often as up.

### Per-model (stripped, primary)

| Model | n | worse | same | better | % of movers worse | sign p |
|-------|---|-------|------|--------|-------------------|--------|
| gemini-2.5-flash | 8 | 50.0% | 50.0% | 0.0% | 100.0% | 0.062 |
| deepseek-v4 | 31 | 38.7% | 54.8% | 6.5% | 85.7% | 0.0065 |
| gpt-4o | 40 | 40.0% | 50.0% | 10.0% | 80.0% | 0.0059 |
| qwen-3-235b | 90 | 42.2% | 43.3% | 14.4% | 74.5% | 0.00031 |
| llama-3.3-70b | 353 | 25.8% | 62.6% | 11.6% | 68.9% | 8.0e-06 |
| claude-sonnet-4 | 196 | 19.4% | 66.8% | 13.8% | 58.5% | 0.11 |

**DISCLOSURE:** worse outnumbers better in all six models, but the asymmetry is
individually significant in only four. Claude Sonnet 4 is not significant (p = 0.11)
and Gemini has only 8 genuine revisions. The correct claim is that the direction holds
in every model and reaches significance in four of six, not that every model shows it
significantly. Unstripped, five of six reach significance (Gemini p = 0.062).

### Per-domain (stripped, primary)

| Domain | n | worse | same | better | % of movers worse | sign p |
|--------|---|-------|------|--------|-------------------|--------|
| writing | 118 | 28.8% | 63.6% | 7.6% | 79.1% | 8.5e-05 |
| creative | 145 | 26.2% | 64.1% | 9.7% | 73.1% | 0.0006 |
| code | 196 | 35.2% | 47.4% | 17.3% | 67.0% | 0.00036 |
| analysis | 125 | 23.2% | 64.8% | 12.0% | 65.9% | 0.024 |
| data_logic | 134 | 21.6% | 67.2% | 11.2% | 65.9% | 0.024 |

All five domains individually significant. Domain homogeneity chi-square:
**chi2 = 3.02, dof = 4, p = 0.555.** The asymmetry does not differ by domain.

### The objectivity gradient is a meta-commentary artifact

| Basis | Objective (code + data_logic) | Subjective (creative + writing) | Fisher p |
|-------|-------------------------------|----------------------------------|----------|
| **Stripped** | 98 / 49 = 66.7% worse | 72 / 23 = 75.8% worse | **0.151** |
| Unstripped | 109 / 44 = 71.2% worse | 94 / 18 = 83.9% worse | **0.019** |

Unstripped domain chi-square p = 0.205; stripped p = 0.555.

**BEARS ON A REGISTERED PREDICTION.** `experiment/study3_revision_yield_design.md` line 117
states as a "Key prediction" that the overcorrection gap widens moving from Code to
Creative along the objectivity spectrum. That prediction is supported on unstripped
scores (p = 0.019) and **is not supported once meta-commentary is stripped** (p = 0.151).
This is consistent with Section M5, which records creative as the domain most sensitive
to stripping because commentary is most prevalent there. Report the stripped estimate as
the finding with the unstripped one beside it, naming the control in the same sentence.
This is the second registered prediction the corrected analysis does not confirm, after
the 65% reversibility bar in Section 7.

### Outcome when the input was already sufficient (added 2026-09-07)

Of the genuine revisions whose baseline content was already at level 4 or above, how many
end below level 4?

| Basis | revisions to sufficient input | still sufficient after | no longer sufficient |
|-------|------------------------------|------------------------|----------------------|
| **Stripped** | 411 | 298 (72.5%) | **113 (27.5%)** |

Of the 113 that fall below, 85 land at level 2 and 28 at level 3.

- **Filter:** the same 718 genuine revisions as above. Keep those whose baseline (the most
  recent turn with genuinely new content) is at level >= 4 after the 6 -> 2 recode. Count how
  many have a level < 4 at the revision turn.
- **This is the same set of 411 as Stripped Sensitivity M1** ("Revised despite sufficient",
  411 of 1,038 sufficient turns, 39.6%). Verified 2026-09-07: the two constructions produce
  identical sets, 411 of 411, zero on either side. They coincide because a meta-response
  strips to near-empty text and scores about 1.06, so it can never be a sufficient baseline.
  M1 counts how OFTEN sufficient work is revised; this counts what HAPPENS when it is.

### Magnitude of the change (added 2026-09-07)

| Basis | mean change, all revisions | mean drop when down | median drop | mean rise when up |
|-------|---------------------------|---------------------|-------------|-------------------|
| **Stripped** | **-0.30** | **-1.72** | -2 | +1.45 |
| Unstripped | -0.51 | -1.90 | -2 | +1.32 |

Stripped, 87 of the 199 downward moves fall one level and 112 fall two or more. Drops are both
more frequent and larger than rises.

- **Filter:** signed difference in recoded level between each genuine revision and its baseline,
  same comparison basis as above. Script: `scripts/study3/revision_direction.py`.

### Trial-level, balanced panel (Turn 1 vs Turn 5, n = 50)

| Basis | worse | same | better | movers | sign p |
|-------|-------|------|--------|--------|--------|
| **Stripped** | 52.0% | 38.0% | 10.0% | 26 / 5 | 9.61e-05 |
| Unstripped | 62.0% | 30.0% | 8.0% | 31 / 4 | 1.73e-06 |

### Why this estimator is preferred to the balanced-panel cliff

The cliff in Section 2 rests on 50 trials, 45 of them Llama, with three of six models
contributing zero trials. This analysis uses all 718 genuine revisions across all six
models and needs no balanced panel. It answers the same question with far more of the
data. It is the basis for the paper's headline claim as of 2026-09-03.

---

## 4c. EXPECTED CHANGE BY INPUT LEVEL (added 2026-09-14)

**POST-HOC. Not among the registered predictions.** Computed 2026-09-14 while preparing
figures; it was not part of the pre-registered analysis plan and must be reported as
exploratory wherever it appears.

Expected change in quality level from a single undirected revision, conditioned on the
quality level of the input being revised.

| Input level | n | E[change] | P(down) | P(up) |
|---|---:|---:|---:|---:|
| 2 | 116 | +0.69 | 0.00 | 0.35 |
| 3 | 77 | -0.03 | 0.30 | 0.27 |
| 4 | 394 | -0.43 | 0.28 | 0.06 |
| 5 | 130 | -0.98 | 0.49 | 0.00 |
| **input insufficient (< 4)** | 194 | **+0.41** | | |
| **input sufficient (>= 4)** | 524 | **-0.56** | | |

Level 1 has n = 1 and is omitted from the figure.

- **Filter:** the same 718 genuine revisions as Section 4b. For each trial, walk turns 2-5;
  where `genuine_meta_labels.jsonl` gives GENUINE and `stripped_rescore_full.jsonl` has a
  score, record (baseline level, new level) and advance the baseline. Baseline starts at the
  Turn 1 stripped score. 6 -> 2 recode applied throughout.
- **Sources:** `data/study3/raw_responses/genuine_meta_labels.jsonl`,
  `stripped_rescore_full.jsonl`.
- **Caveat:** conditions on a judge-assigned level, so it inherits the evaluator's error.
  The reliability figures in Section 11 apply.
- **Relation to 4b:** these are the row means of the 4b transition matrix, not an
  independent result. Reporting both would be reporting one analysis twice.

---

## 5. TARGETED FEEDBACK

| Metric | Value |
|--------|-------|
| N | 177 |
| Targeted mean | 4.68 |
| Generic mean | 4.43 |
| Delta | **+0.25** |
| Wilcoxon p | 3.75e-03 |

- **Filter (exact):** Load all 1,047 records from `targeted_feedback_results.jsonl`. Each record has fields `targeted_level`, `generic_next_level`, `worker_trial_id`, `turn`. For each record:
  1. Require `targeted_level` and `generic_next_level` both non-null.
  2. Compute `next_turn = turn + 1`. If next_turn > 5, exclude.
  3. Look up `(worker_trial_id, next_turn)` in `genuine_meta_labels.jsonl`. If `classifier_label != "GENUINE"`, exclude (the generic next-turn output was a decline, not a revision).
  4. Recode: if `targeted_level == 6`, set to 2. If `generic_next_level == 6`, set to 2.
  5. Remaining n=177 pairs. Wilcoxon signed-rank on non-zero differences.
- **What it measures:** "Does a targeted revision (with specific critique) produce higher quality than the model's own genuine generic revision at the next turn?" Answer: yes, by +0.25 levels unstripped (p=0.004), or **+1.16 levels stripped** (p=5.7e-19). The unstripped +0.25 is deflated because meta-commentary on the generic side inflates its score (4.43 unstripped -> 3.53 stripped). Targeted revisions have minimal meta (9/177 = 5%). See Stripped Sensitivity Analysis M2 for details.
- **Supersedes:** The paper's +2.00 (n=424) used the old keyword classifier (`classify_revision()` in `analyze.py`), which let 424 records through because it failed to catch verbose declines. Those declines scored as level 1-2 in the "generic" baseline, inflating the delta to +2.00.
- **Discarded:** +0.79/n=106 was cited from a prior conversation session but is not reproducible from any filter on the current data files. It does not appear in `study3_results.json` or any saved output. Discarded as unverifiable.
- Source: `data/study3/raw_responses/targeted_feedback_results.jsonl` + `genuine_meta_labels.jsonl`

---

### 5b. Targeted feedback by input type (POST-HOC, added 2026-09-20)

**Post-hoc and not pre-registered.** Proposed by the assistant on 2026-09-20 and authorised by
Liam the same day, after the composition of the n=177 arm was found not to be disclosed
anywhere. It is a split the analysis plan did not name, and any use of it in the paper carries
that label.

The 177 pairs of Section 5 were stratified by what the input to the revision actually was. The
input is the turn the targeted critique was written against; its GENUINE/META label comes from
`genuine_meta_labels.jsonl` at that same turn, and turn-1 inputs are unlabelled and counted
with the drafts.

**Composition of the 177:** 109 meta-response inputs (101 of them scored level 1), 37 genuine
revisions, 31 turn-1 drafts.

**Sufficient inputs, corrected 2026-09-20.** An earlier version of this entry said zero inputs
were rated sufficient. That is true on the UNSTRIPPED scale, which is the one
`scripts/study3/phase6_targeted_feedback.py:215` filters on (`level <= 3`), and the unstripped
input levels are 102 at level 1, 17 at level 2 and 58 at level 3. On the STRIPPED scale, which
is the paper's primary basis, the distribution is 100 / 17 / 49 / **11 at level 4**. Stripping
lifted eleven inputs over the threshold.

Those eleven cannot carry an estimate and are not one. All eleven are Llama 3.3 70B, with none
from the other five models. All eleven sit exactly at level 4 and none higher. Ten were rated
level 3 unstripped and one level 2, so every one of them is a case where the two scorings
disagree, which is to say where meta-commentary had depressed the raw score. They are selected
by that disagreement rather than sampled from sufficient work. Their descriptive gain is +1.18,
indistinguishable from the pooled figure and resting on eleven observations from one model.

Measuring the remedy on work that is sufficient on both scales requires rerunning phase 6 with
the filter inverted. Nothing in the existing files substitutes for it.

Stripped basis, the paper's primary estimate. Targeted level against the stripped level of the
model's own generic next-turn revision:

| Input | n | Targeted | Generic (stripped) | Gain | Wilcoxon p |
|-------|--:|---------:|-------------------:|-----:|-----------:|
| Draft or genuine revision | 68 | 4.76 | 3.18 | **+1.59** | 5.44e-11 |
| Meta-response | 109 | 4.63 | 3.74 | +0.89 | 1.04e-09 |
| All (Section 5) | 177 | 4.68 | 3.53 | +1.16 | 5.74e-19 |

Unstripped, for contrast, where the generic side keeps its meta-commentary:

| Input | n | Targeted | Generic | Gain | Wilcoxon p |
|-------|--:|---------:|--------:|-----:|-----------:|
| Draft or genuine revision | 68 | 4.76 | 4.88 | -0.12 | 2.39e-01 |
| Meta-response | 109 | 4.63 | 4.15 | +0.49 | 1.10e-04 |
| All (Section 5) | 177 | 4.68 | 4.43 | +0.25 | 3.75e-03 |

- **Filter (exact):** the Section 5 filter unchanged, then split on the classifier label at the
  input turn. Level 6 recoded to 2 on both sides. Stripped generic level from
  `stripped_rescore_full.jsonl` at turn + 1. All three pooled rows reproduce Section 5 exactly.
- **What it settles.** The +1.16 is not an artefact of the meta-response inputs. It is larger on
  real drafts (+1.59) than on meta-responses (+0.89), and the pooled figure is diluted by them
  rather than carried by them. The unstripped stratification points the opposite way only
  because unstripped generic revisions on real drafts score 4.88, inflated by the
  meta-commentary the stripping procedure removes.
- **What it does not settle.** No input in this arm was already sufficient. The repair is
  demonstrated on work rated 1 to 3 and has never been measured on work rated 4 or above, which
  is the population the paper's cliff, its 27.5% figure and the STET diagnostic all concern.

---

### 5c. Targeted feedback by model (added 2026-09-20)

`tab:targeted-per-model` in the paper had no ledger entry. Recomputed 2026-09-20 and recorded.

| Model | n | Stripped delta | p |
|-------|--:|---------------:|--:|
| Llama 3.3 70B | 71 | +1.62 | 9.2e-12 |
| Qwen 3 235B | 21 | +1.48 | 4.5e-04 |
| GPT-4o | 12 | +1.33 | 7.8e-03 |
| DeepSeek V4 Flash | 19 | +1.05 | **1.5e-02** |
| Claude Sonnet 4 | 51 | +0.31 | 1.2e-02 |
| Gemini 2.5 Flash | 3 | +2.33 | not reported, n < 5 |

- **Filter (exact):** the Section 5 selection, split by `model`. Targeted level against the
  stripped level of the generic next-turn revision, 6 -> 2 recode on both sides. Two-sided
  Wilcoxon signed-rank, scipy defaults (`method='auto'`, `zero_method='wilcox'`), which is the
  convention the other five rows already match to the printed precision.
- **Correction.** The paper printed 1.2e-02 for DeepSeek, which is the value on the Claude row
  directly below it. No test variant reproduces it: exact/wilcox gives 1.34e-02, auto/wilcox
  1.45e-02, pratt and zsplit further away. Corrected to 1.5e-02. The delta, the n and every
  other row were already right, and the conclusion is unchanged since the row was and remains
  significant.
- n sums to 177, matching Section 5.

---

## 6. REVISION TAX

### Method

- **Estimator:** Ratio-of-means aggregate (sum all waste tokens / sum all baseline tokens). NOT mean-of-ratios (which is small-denominator-sensitive and produced 3,125% outliers in early runs).
- **Interpretation:** A -- meta-response tokens COUNT as waste. All post-t* output tokens are waste regardless of whether the turn was GENUINE or META, because the user paid for them. Quality trajectory uses GENUINE-only turns (+ T1) for t* determination.
- **t*:** argmax of mean GENUINE-only quality (6->2 recoded) across turns, requiring min n >= 5 at each turn for eligibility. Result: t* = T1 for all 6 models.
- **Token counting:** API-reported output token counts from `worker_trials.jsonl` field `token_counts[turn_idx]["output"]`. These are actual tokenizer counts returned by each API, not character proxies.
- **Supersedes:** Old Section 6 numbers (7.4%, 19.9%, 42.0%, 95.0%, 142.2%, 262.0%, aggregate 48.0%/92.4%/270,457) were transcribed from a prior session's terminal output and are not saved in any data file. They match no reproducible computation and are discarded.

### Per-Model (Interpretation A, t*=T1 for all)

| Model | t* | Tax % | Waste % | $/task waste |
|-------|-----|-------|---------|-------------|
| gemini-2.5-flash | T1 | 30.6 | 23.4 | $0.0001 |
| deepseek-v4 | T1 | 118.9 | 54.3 | $0.0005 |
| gpt-4o | T1 | 125.8 | 55.7 | $0.0053 |
| qwen-3-235b | T1 | 198.6 | 66.5 | $0.0009 |
| claude-sonnet-4 | T1 | 251.6 | 71.6 | $0.0182 |
| llama-3.3-70b | T1 | 436.0 | 81.3 | $0.0013 |

### Aggregate

| Metric | Value |
|--------|-------|
| Aggregate waste fraction | **62.1%** |
| Aggregate tax | 164.2% |
| Total wasted tokens | 653,070 |

**t* = T1 for all 6 models.** No model benefits from undirected revision on the GENUINE-only quality trajectory. GPT-4o would show t*=T5 without the min_n floor (3 trials at T5 averaging 4.0 vs T1's 3.99 on n=120), which is a small-sample artifact.

### Pricing Table (from `scripts/study3/analyze.py` lines 1515-1523, labeled "Real 2025 API pricing")

| Model | $/1M output tokens |
|-------|-------------------|
| gemini-2.5-flash | $0.40 |
| deepseek-v4 | $0.55 |
| llama-3.3-70b | $0.88 |
| qwen-3-235b | $0.90 |
| gpt-4o | $10.00 |
| claude-sonnet-4 | $15.00 |

**Dollar figures are pricing-tier-dominated** (Claude's $/task is 182x Gemini's despite similar waste%) and based on 2025 output-token prices (Qwen/Llama via Together.ai). These need verification against current rates before citing. **Token-waste % is the robust, pricing-independent number** and should be the primary metric in the paper.

- Source: `worker_trials.jsonl` (token counts, model), `evaluator_results.jsonl` (quality scores), `genuine_meta_labels.jsonl` (GENUINE/META labels)
- **Filter (t*):** For each model, for each turn T in {1..5}, compute mean quality from `evaluator_results.jsonl` (`level`, recoded 6->2) restricted to: T1 for all 120 trials; T2-T5 only where `genuine_meta_labels.jsonl` has `classifier_label == "GENUINE"`. Require n >= 5 at a turn for t* eligibility. t* = argmax of these means.
- **Filter (tax/waste):** For each of 720 trials, extract `token_counts[turn_idx]["output"]` for turns 1-5. Baseline tokens = sum of tokens at turns <= t* (= T1 tokens only, since t*=T1). Waste tokens = sum of tokens at turns > t* (= T2+T3+T4+T5 tokens). Tax % = sum(waste) / sum(baseline) x 100 across all trials of that model. Waste % = sum(waste) / sum(all) x 100. Aggregate = pool all 720 trials.
- **Filter ($/task):** waste_tokens_per_trial x price_per_token. Price from the table above (output tokens only).

---

## 7. REVERSIBILITY (Human Annotation)

### Human Judgments (stripped pairs, n=50)

| Metric | Liam | Troy | Combined |
|--------|------|------|----------|
| T1-preferred | 19 (38%) | 22 (44%) | 41 (41%) |
| Revision-preferred | 13 (26%) | 19 (38%) | 32 (32%) |
| Tie | 18 (36%) | 9 (18%) | 27 (27%) |
| Non-tie T1-pref | 19/32 (59.4%) | 22/41 (53.7%) | **41/73 (56.2%)** |
| Bootstrap 95% CI | -- | -- | [45.2%, 67.1%] |

**Pre-committed bar (>=65%, CI excludes 50%): NOT CLEARED.**

### Inter-Annotator Agreement

| Metric | Value |
|--------|-------|
| Raw 3-way agreement | 40/50 (80%) |
| Cohen's kappa (raw) | 0.703 |
| Cohen's kappa (decoded) | 0.701 |
| Disagreements | 10 pairs (8 = Liam tie vs Troy decided, 1 full flip, 1 Liam tie vs Troy T1) |

### Position & Length Bias

| Metric | Value |
|--------|-------|
| A chosen (decided pairs) | 38/73 (52.1%), CI [39.7%, 63.0%] |
| Longer output chosen | 40/73 (54.8%) |

### Model Judge Comparison

| Source | T1-pref (non-tie) | Ties |
|--------|-------------------|------|
| Model judge, UNSTRIPPED (pairwise, same 50 trials) | 45/49 (91.8%) | 1 |
| Model judge, UNSTRIPPED (full 720, pairwise) | 669/720 (92.9%) | -- |
| Model judge, STRIPPED (pairwise, 50 pairs) | 26/46 (56.5%) | 4 |
| Humans, STRIPPED (50 pairs) | 41/73 (56.2%) | 27 |

### Human-Judge Agreement on Stripped Content

| Comparison | n | Agreement | Kappa |
|------------|---|-----------|-------|
| Liam vs judge | 31 | 77.4% | 0.541 |
| Troy vs judge | 39 | 79.5% | 0.589 |
| Human majority vs judge | 30 | 80.0% | 0.595 |
| All pooled vs judge | 70 | 78.6% | **0.569** |

**vs. unstripped: kappa was -0.07 to +0.02 (near zero).**

- Source (human): `reversibility_judgments_liam.json`, `reversibility_judgments_troy.json`
- Source (key): `reversibility_stripped_key.json`
- Source (judge stripped): `judge_stripped_pairwise.json`
- Source (judge unstripped): `reversibility_results.jsonl`
- **Filter (human judgments):** Load each annotator's 50 judgments (field `judgment` in {A, B, equivalent}). Decode via `reversibility_stripped_key.json`: if judgment matches the side where `A_is == "T1"` or `B_is == "T1"`, count as T1-preferred; if it matches the revision side, count as revision-preferred; "equivalent" = tie. Non-tie T1-pref = T1-preferred / (T1-preferred + revision-preferred). Combined = pool both annotators' decoded judgments (100 total). Bootstrap: 1000 resamples of the 100 pooled non-tie decisions, percentile CI, seed 42.
- **Filter (inter-annotator):** Cohen's kappa on the 50 pairs using 3-way labels (A/B/equivalent for raw; T1/revision/tie for decoded). Disagreements = pairs where Liam != Troy.
- **Filter (position/length bias):** Among combined decided (non-tie) judgments (n=73), count how many chose output A vs B (position bias). For length: compare character counts of chosen vs unchosen output.
- **Filter (model judge):** `judge_stripped_pairwise.json` has fields `pick` (A/B/tie) and `pair_id`. Decode via same key. Agreement with humans: for each (annotator, pair) where both annotator and judge gave non-tie decisions, compare decoded labels. Kappa computed on these matched pairs. Pooled = both annotators' matched pairs concatenated.

---

## 8. META-WRAPPING ASYMMETRY

| Side | Has preamble | Has postamble | Has either |
|------|-------------|--------------|------------|
| Revision (T2-T5) | 38/50 (76%) | 24/50 (48%) | **42/50 (84%)** |
| T1 | 4/50 (8%) | 5/50 (10%) | **7/50 (14%)** |

Meta-commentary prevalence by turn (genuine revisions only):
- T1: 14%, T2: 92%, T3: 85%, T4: 79%, T5: 68%

**This asymmetry inflated the model judge's T1-preference from 56.5% (stripped) to 91.8% (unstripped) on the same 50 pairs.**

- Source: `meta_wrapping_asymmetry.json`
- **Filter:** The 50 unstripped reversibility pairs (`reversibility_human_pairs.json`). For each pair, decode T1 vs revision side via `reversibility_human_key.json`. Apply regex preamble/postamble detectors (patterns in `audit_meta_commentary.py`: PREAMBLE_PATTERNS checked against first 300 chars, POSTAMBLE_PATTERNS checked against last 400 chars). Count hits per side. Per-turn meta-commentary rates: for each turn T in {1..5}, count how many outputs at that turn match any preamble or postamble pattern, divided by total outputs at that turn.
- **Scope:** All counts are from the 50 unstripped reversibility pairs, stored in `meta_wrapping_asymmetry.json`. Raw counts: revision preamble=38, postamble=24, either=42; T1 preamble=4, postamble=5, either=7.
- **FLAG RESOLVED 2026-09-06, DO NOT CITE.** The per-turn breakdown (T1:14%, T2:92%, T3:85%,
  T4:79%, T5:68%) does not reproduce from any of 18 candidate scopes tested. Its T1 matches the
  50-pair scope, its T2 matches GENUINE-only, and its T5 matches the full 720-trial corpus, so
  the series mixes three denominators. It is not cited anywhere in the live manuscript and must
  not be. Two per-turn series that do reproduce, each with a single stated scope, are in
  `paper/reference/stats_08_meta_commentary.md` section 2.

---

## 9. REVERSIBILITY -- STRATIFIED

### By Last Revision Turn (non-tie T1-preference, combined annotators)

| Turn | T1-preferred | n | % |
|------|-------------|---|---|
| T2 | 9 | 17 | 52.9% |
| T3 | 11 | 21 | 52.4% |
| T4 | 17 | 24 | **70.8%** |
| T5 | 4 | 11 | 36.4% |

### By Domain

| Domain | T1-preferred | n | % |
|--------|-------------|---|---|
| writing | 13 | 14 | **92.9%** |
| analysis | 8 | 12 | 66.7% |
| code | 9 | 20 | 45.0% |
| creative | 8 | 19 | 42.1% |
| data_logic | 3 | 8 | 37.5% |

- **Filter (by turn):** From `reversibility_stripped_key.json`, field `last_rev_turn` gives the turn of the revision side. Group the 100 pooled human non-tie decisions (combined annotators) by `last_rev_turn`. Count T1-preferred vs revision-preferred within each group.
- **Filter (by domain):** Same pooled non-tie decisions, grouped by `domain` field from `reversibility_stripped_key.json`.

---

## 10. SELF-REFLECTION

| Metric | Value |
|--------|-------|
| N | 720 |
| Mean recommended turn | 2.44 (SD=1.39) |
| Recommend T1 | 288/720 (40.0%) |
| Recommend not-last | 90.7% |
| Distribution | T1:288, T2:76, T3:176, T4:113, T5:67 |

- Source: `self_reflection_results.jsonl`
- **These numbers are unchanged** (self-reflection does not depend on classifier)
- **Filter:** All 720 records in `self_reflection_results.jsonl`. Field `recommended_turn` (integer 1-5). Mean, SD, and frequency distribution computed over all 720. "Recommend not-last" = records where `recommended_turn != 5` (since T5 was the final turn in the trial).

---

### 10b. Per-domain decline, paired basis (added 2026-09-20)

`tab:domain-variation` printed unpaired deltas while attaching paired-Wilcoxon p-values to
them. The p-values were right; the deltas were a different quantity. The printed T1 mean was
every trial in the domain, while the tested T1 mean is only the trials reaching Turn 5.

| Domain | printed (withdrawn) | paired delta (now printed) | p | n(T5) |
|--------|--------------------:|---------------------------:|----:|------:|
| analysis | -1.16 | **-0.94** | 0.003 | 17 |
| code | -1.05 | **-0.93** | 0.003 | 30 |
| creative | -0.82 | **-0.58** | 0.031 | 19 |
| data_logic | -1.01 | **-0.53** | 0.058 | 17 |
| writing | -1.06 | **-0.77** | 0.008 | 13 |

- **Filter (exact):** trials whose Turn-5 label is GENUINE in `genuine_meta_labels.jsonl`,
  with stripped levels at turns 1 and 5 from `stripped_rescore_full.jsonl`, 6 -> 2 recode
  applied first, domain from `worker_trials.jsonl`. Two-sided Wilcoxon signed-rank on the
  paired values, and the delta reported is the mean paired difference from that same test.
- data_logic was the worst affected: printed as -1.01 against a tested -0.53, an overstatement
  of 91%. Signs and significance are unchanged for every domain, so no conclusion moves.
- Section 10's own filter line records the unpaired basis ("T1 = all 144 per domain, T5 =
  GENUINE at T5 only") and is left as the record of what was previously printed.

---

## 11. RELIABILITY

### Human Inter-Rater Agreement (3 raters, 64 calibration items, 6->2 recode)

| Pair | QW Kappa | Binary (>=4) | Within-1 |
|------|----------|-------------|----------|
| Liam-Troy | 0.406 | 49/64 (76.6%) | 52/64 (81.2%) |
| Liam-Sophie | **0.578** | 50/64 (78.1%) | 61/64 (95.3%) |
| Sophie-Troy | **0.603** | 53/64 (82.8%) | 56/64 (87.5%) |

| Metric | Value |
|--------|-------|
| Krippendorff's alpha (3-rater, interval) | **0.529** |

Note: Sophie re-rated all 64 items (v2) after rubric clarification. Sophie v2 uses a 1-5 scale (no level 6 assigned). Liam-Troy QW kappa of 0.406 supersedes the previously reported 0.228, which was linear-weighted kappa on the raw 1-6 scale without 6->2 recode.

### Judge-Human Agreement

| Metric | Value | Source |
|--------|-------|--------|
| Judge-human Spearman r | 0.505 (p<0.001) | `selected_judge.json` |
| Judge-human QW kappa | 0.526 | `judge_calibration.jsonl` |

- Source: `human_ratings_liam.json`, `human_ratings_troy.json`, `human_ratings_sophie_v2.json`, `selected_judge.json`, `judge_calibration.jsonl`
- **Filter (human QW kappas):** All three raters' `level` fields on the 64 shared calibration items (all 64 items overlap across all 3 raters). Recode level 6 -> 2 before computing. Quadratic-weighted Cohen's kappa on 1-5 scale (sklearn `cohen_kappa_score(weights='quadratic')`). Binary threshold: both raters agree on level >= 4 vs < 4. Within-1: |rater_A - rater_B| <= 1.
- **Filter (Krippendorff's alpha):** Interval-scale alpha over the 3 x 64 rating matrix (after 6->2 recode).
- **Filter (Judge-human Spearman r):** From `selected_judge.json`, Claude Sonnet 4 scores vs averaged human ratings on the 64 calibration samples.
- **Filter (Judge-human QW kappa):** From `judge_calibration.jsonl`, quadratic-weighted kappa between Claude Sonnet 4 scores and averaged human ratings on the 64 calibration samples.

---

## 12. UNCHANGED NUMBERS (not affected by classifier correction)

- Study 1: 3,840 trials, 99.9% vs 23.2% gate, all numbers unchanged
- Study 2: 1,728 trials, momentum numbers unchanged
- Self-reflection: mean 2.44, all numbers unchanged
- T1 sufficiency rate: 87.6% (was "93.3%" in paper -- NEED TO VERIFY which denominator)
- DRP = Turn 2 for all degrading models: unchanged conceptually, but per-model trajectories need recomputation
- Edit ratio 0.97: unchanged (computed on raw text, not affected by classifier)

---

## 13. BENCHMARK STABILITY OVER THE 40 TASKS (added 2026-09-18)

Is a 40-task corpus enough to rank six models on a stable score? The 40 tasks are split
into halves and the ranking from one half is compared against the ranking from the other,
over many random splits. Ten candidate scores are tested.

- **Script:** `scripts/study3/stet_stability.py`
- **Output:** `data/study3/analysis/stet_stability.json`
- **Sample:** unchanged. The same 720 trials (6 models x 40 tasks x 3 runs), the same
  GENUINE/META labels from the validated classifier, the same 6 -> 2 recode. No sample
  restriction and no balanced-panel requirement.
- **Filter (exact):** Every score is computed per (model, task) cell by pooling that
  cell's 3 trials, then summed over the tasks in a half. Join keys are `trial_id` +
  `turn` against `genuine_meta_labels.jsonl` for the GENUINE/META label, `worker_trial_id`
  + `turn` against `evaluator_results.jsonl` for the unstripped level, and `trial_id` +
  `turn` against `stripped_rescore_full.jsonl` for the stripped level. Level 6 is recoded
  to 2 before any comparison. Definitions: *genuine-revision rate* = GENUINE turns / all
  turns 2-5; *revision despite sufficiency* = turns at level >= 4 among turns 1-4 whose
  next turn is GENUINE, over all turns at level >= 4 (the Section 4 and M1 estimator);
  *share left alone* = 1 minus that; *quality delta* = level at turn 5 minus level at
  turn 1, with the last genuinely new content carried forward past meta-responses
  (the S6 LOCF estimator) or as the raw end state; *revision tax* = turn 2-5 output
  tokens over turn-1 output tokens, ratio of means, with t* = T1 for all six models as
  recorded in Section 6; *mean signed change per revision* = the Section 4b and 4c
  estimator, each genuine revision against the most recent turn with genuinely new
  content.
- **Split procedure:** 1,000 random splits of the 40 tasks into halves of 20, drawn with
  `numpy.random.default_rng(20260918)`; a second set of 1,000 domain-stratified splits
  (4 of each domain's 8 tasks per half) drawn from the same generator immediately after.
  Spearman rank correlation between the two halves' six-model score vectors. The task
  bootstrap resamples 40 tasks with replacement, 1,000 draws, seed 20260919. Exact ties
  between models are broken by model index under a stable sort.
- **Seed: 20260918** (bootstrap 20260919). Deterministic.
- **Ledger checks asserted at load:** the script halts unless it reproduces 718/2,880
  GENUINE, 368/938 unstripped and 411/1,038 stripped revision-despite-sufficiency,
  631/720 turn-1 sufficiency, 653,070 wasted output tokens, 164.2% aggregate tax and
  62.1% aggregate waste share. All 15 checks pass on the current data.

### 13.1 Full-40 scores

| Model | Left alone | Rev-desp-suff (str) | Genuine-rev rate | Tax % | LOCF delta (str) | Raw delta (str) | Mean chg / revision |
|-------|-----------:|--------------------:|-----------------:|------:|-----------------:|----------------:|--------------------:|
| gemini-2.5-flash | 0.978 | 0.022 | 0.017 | 30.6 | -0.075 | -2.808 | -1.125 |
| deepseek-v4 | 0.963 | 0.037 | 0.065 | 118.9 | -0.192 | -3.350 | -0.742 |
| gpt-4o | 0.823 | 0.177 | 0.083 | 125.8 | -0.200 | -2.900 | -0.600 |
| qwen-3-235b | 0.684 | 0.316 | 0.188 | 198.6 | -0.450 | -3.192 | -0.600 |
| claude-sonnet-4 | 0.541 | 0.459 | 0.408 | 251.6 | -0.267 | -2.933 | -0.163 |
| llama-3.3-70b | 0.184 | 0.816 | 0.735 | 436.0 | -0.625 | -1.592 | -0.212 |

Share of sufficient outputs left alone is the primary score: it is the behaviour of
interest stated directly, it uses all 720 trials and all six models rather than the
50-trial balanced panel (which holds zero trials for GPT-4o, DeepSeek and Gemini), and it
touches the evaluator only through the level >= 4 binary, which Section 11 records as the
better-validated part of the scale.

### 13.2 Split-half stability, 1,000 random 20/20 splits

Spearman rho between the two halves. With six models the attainable values are discrete:
1.000 is an exact match, 0.943 is one adjacent swap, 0.886 is two.

| Score | mean rho | median | p05 | min | rho = 1 | rho >= 0.8 | order preserved | top model same | bottom model same |
|-------|---------:|-------:|----:|----:|--------:|-----------:|----------------:|---------------:|------------------:|
| Genuine-revision rate | 0.977 | 1.000 | 0.943 | 0.943 | 52.8% | 100.0% | 63.1% | 100.0% | 100.0% |
| Left alone (stripped) | 0.972 | 0.986 | 0.943 | 0.886 | 47.3% | 100.0% | 51.7% | 47.9% | 100.0% |
| Rev-desp-suff, unstripped | 0.984 | 1.000 | 0.943 | 0.886 | 68.9% | 100.0% | 68.9% | 100.0% | 70.0% |
| Revision tax | 0.952 | 0.943 | 0.943 | 0.886 | 19.8% | 100.0% | 19.8% | 100.0% | 100.0% |
| Quality delta, LOCF stripped | 0.639 | 0.696 | 0.200 | -0.118 | 0.0% | 30.9% | 0.0% | 59.2% | 65.5% |
| Quality delta, LOCF unstripped | 0.836 | 0.886 | 0.599 | 0.058 | 1.3% | 67.0% | 3.1% | 98.8% | 24.2% |
| Quality delta, raw end state | 0.838 | 0.829 | 0.657 | 0.314 | 6.5% | 70.1% | 10.1% | 100.0% | 93.8% |
| Mean signed change per revision | 0.580 | 0.657 | -0.086 | -0.783 | 0.4% | 22.1% | 0.6% | 35.2% | 45.6% |
| Sufficient input broken by revision | 0.651 | 0.600 | 0.429 | 0.116 | 1.0% | 22.7% | 1.4% | 96.1% | 96.0% |

Domain-stratified splits give the same picture, slightly better: genuine-revision rate
mean rho 0.985 with the full order preserved in 76.9%, left alone 0.972 and 52.0%,
LOCF stripped 0.674 and 0.0%.

Two scores are undefined in some splits because Gemini produces only 8 genuine revisions
in the whole corpus: mean signed change in 21 of 1,000 splits, sufficient-input-broken in
101 of 1,000.

A single 20-task half reproduces the **full-40** ordering with mean rho 0.989
(genuine-revision rate), 0.986 (left alone), 0.976 (tax) and 0.860 (LOCF stripped).

### 13.3 Where the instability sits: adjacent-pair inversions

Each score is unstable at one adjacent pair and stable everywhere else, and the unstable
pair is always the one separated by a near-zero gap. Share of 20-task halves in which the
full-40 adjacent pair appears inverted:

| Score | Pair | Gap | Inverted in |
|-------|------|----:|------------:|
| Left alone | deepseek-v4 vs gemini-2.5-flash | 0.016 | 23.8% |
| Left alone | all four other adjacent pairs | 0.140 to 0.358 | 0.0% to 0.2% |
| Genuine-revision rate | deepseek-v4 vs gpt-4o | 0.019 | 18.4% |
| Genuine-revision rate | all four other adjacent pairs | 0.048 to 0.327 | 0.0% |
| Rev-desp-suff, unstripped | gemini-2.5-flash vs deepseek-v4 | 0.029 | 13.0% |
| Revision tax | deepseek-v4 vs gpt-4o | 6.9 of 119 | 39.3% |
| Revision tax | qwen-3-235b vs claude-sonnet-4 | 53.0 | 3.0% |
| LOCF delta | gpt-4o vs deepseek-v4 | 0.008 | 44.8% |
| LOCF delta | claude-sonnet-4 vs gpt-4o | 0.067 | 28.7% |
| LOCF delta | llama-3.3-70b vs qwen-3-235b | 0.175 | 16.8% |
| LOCF delta | qwen-3-235b vs claude-sonnet-4 | 0.183 | 13.6% |

The claim the data supports is therefore narrower than "the ranking is stable": on the
behavioural scores the ordering is preserved wherever two models differ by more than
about 3 percentage points and is close to a coin flip where they do not. That is a
property of how similar those two models are, not of the task count, and no number of
tasks resolves a genuine tie. Llama 3.3 70B is the bottom-ranked model in 100% of halves
on all four behavioural scores.

### 13.4 Variance decomposition and the number of tasks each score needs

Two-way decomposition over the 6 x 40 cells, 3 runs pooled per cell. The generalizability
coefficient is G = s2_model / (s2_model + s2_resid / k) for a benchmark of k tasks.

| Score | s2 between models | s2 between tasks | s2 model x task | G at k = 40 | k for G = 0.90 | k for G = 0.95 |
|-------|------------------:|-----------------:|----------------:|------------:|---------------:|---------------:|
| Genuine-revision rate | 0.0758 | 0.0027 | 0.0165 | 0.995 | 2 | 5 |
| Left alone (stripped) | 0.0933 | 0.0054 | 0.0288 | 0.992 (k = 36) | 3 | 6 |
| Revision tax | 19365 | 6484 | 17926 | 0.977 | 9 | 18 |
| Quality delta, LOCF stripped | 0.0314 | 0.0155 | 0.3550 | 0.780 | 102 | 215 |

Left alone uses 36 of the 40 tasks because four Gemini cells have no sufficient turn and
so no denominator (13.7).

For the behavioural scores, 40 tasks is roughly six times more than the number needed to
reach G = 0.95, because between-model variance is 4.6 times the model-by-task residual.
For the quality delta, 40 tasks is about a quarter of what G = 0.90 would require.

### 13.5 The quality-delta scores fail the stability test, and the reason is identifiable

No construction of the turn-1-to-turn-5 quality delta is stable: the full ordering is
preserved in 0.0% of splits (LOCF stripped), 3.1% (LOCF unstripped) and 10.1% (raw end
state), against 51.7% to 68.9% for the behavioural scores.

For the raw end-state version the cause is measurable. Across the six models the raw
stripped delta has **Spearman -1.000 with mean turn-1 quality** (stripped turn-1 means:
llama 3.75, gemini 3.82, gpt-4o 3.98, claude 4.28, qwen 4.36, deepseek 4.48). Mean
stripped level at turn 5 is 1.01 to 1.34 for the five declining models, because a
meta-response strips to near-empty text and scores about 1. The delta is therefore
ordering models by their turn-1 baseline and by how often they emit a meta-response, not
by how much a revision damages the work. The balanced-panel delta cannot be used at all:
45 of its 50 trials are Llama and three models contribute zero (Section 2).

### 13.6 Three of the stable scores are one quantity

Genuine-revision rate, revision-despite-sufficiency and the revision tax produce
**identical** full-40 orderings. Pairwise Spearman among them over the six models is
1.000, and -1.000 against share-left-alone by construction. They are three views of how
often a model revises, not three measures that independently agree. Reporting all three
as converging evidence would be reporting one result three times.

### 13.7 Cell sizes

Each model-task cell holds 3 trials and 12 post-turn-1 turns. Each model-domain cell
holds 24 trials; each task holds 18 trials across all models.

Turn-5 genuine trials by domain, of 144 trials per domain: writing 13, analysis 17,
data_logic 17, creative 19, code 30. This is the 13-to-30 range disclosed in S10.

Turn-5 genuine trials per model and domain, of 24:

| Model | analysis | code | creative | data_logic | writing |
|-------|---------:|-----:|---------:|-----------:|--------:|
| claude-sonnet-4 | 0 | 8 | 3 | 3 | 1 |
| deepseek-v4 | 2 | 1 | 2 | 1 | 1 |
| gemini-2.5-flash | 0 | 0 | 1 | 0 | 0 |
| gpt-4o | 1 | 0 | 2 | 0 | 0 |
| llama-3.3-70b | 14 | 19 | 10 | 12 | 9 |
| qwen-3-235b | 0 | 2 | 1 | 1 | 2 |

Per-model denominators:

| Model | Balanced panel / 120 | Turn-5 genuine / 120 | Sufficient turns (str) | Min task cell | Task cells < 3 |
|-------|---------------------:|---------------------:|-----------------------:|--------------:|---------------:|
| claude-sonnet-4 | 2 | 15 | 266 | 2 | 1 |
| deepseek-v4 | 0 | 7 | 135 | 2 | 1 |
| gemini-2.5-flash | 0 | 1 | 93 | 0 | 16 |
| gpt-4o | 0 | 3 | 130 | 1 | 6 |
| llama-3.3-70b | 45 | 64 | 256 | 1 | 3 |
| qwen-3-235b | 3 | 6 | 158 | 2 | 3 |

179 of the 240 model-task cells contain no turn-5 genuine trial, so any score conditioned
on turn 5 cannot be computed at task level. Four cells have a zero sufficient-turn
denominator, all Gemini and all code tasks: `backup_script`, `debounce_function`,
`debug_sort`, `email_validator`.

### 13.8 Supporting checks

**Task bootstrap at full size** (1,000 draws of 40 tasks with replacement, seed 20260919).
The full-40 ordering is recovered in 81.8% of draws on genuine-revision rate, 77.8% on
left alone, 58.4% on tax and 17.8% on LOCF stripped. Per-model 95% CI on share left
alone: llama [0.123, 0.246], claude [0.487, 0.595], qwen [0.585, 0.782], gpt-4o
[0.742, 0.899], deepseek [0.927, 0.992], gemini [0.948, 1.000]. Every interval is
disjoint from its neighbour except deepseek and gemini.

**Model subsets.** Dropping the two extreme models leaves four mid-pack models
(deepseek, gpt-4o, qwen, claude). On share left alone they split-half at mean rho 0.999
with the order preserved in 99.3% of splits. The stability is not an artefact of Llama's
outlying position. On genuine-revision rate the same four give 0.921 and 63.1%, held down
by the deepseek-to-gpt-4o near-tie. On LOCF delta they give 0.161 and 0.0%.

**Run-to-run.** Each of the 3 runs is a complete 40-task benchmark scored once.
Pairwise Spearman between runs is 0.943 to 0.986 on share left alone, 0.943 to 1.000 on
genuine-revision rate and tax, and 0.609 to 0.725 on LOCF stripped. Generation noise at
temperature 1.0 is the same size as task-sampling noise and separates the two families of
scores the same way.

- Sources: `worker_trials.jsonl` (model, scenario, domain, run, output token counts),
  `genuine_meta_labels.jsonl`, `evaluator_results.jsonl`, `stripped_rescore_full.jsonl`.

---

### 14. Appendix verification sweep (added 2026-09-20)

Every Study 1 and Study 2 number printed in the appendix was recomputed from
`data/processed/scored_trials.jsonl`, `momentum_scored.jsonl`,
`reverse_momentum_scored.jsonl` and `data/analysis/`. Recorded here because Study 1 and
Study 2 have no results ledger of their own.

**Reproduced exactly.** Factorial 8 x 16 x 2 x 3 x 5 = 3,840 (leading 1,920 + pilot_c 1,920);
leading-probe revision 99.9%; evaluative-probe declines Gemini 99.7, GPT-4o 68.6, Claude 62.0;
chi-squared by probe type 914.37 / 1326.89 / 788.96 across all five probe types, so the printed
"> 788" holds; Spearman within the leading probe -0.495 / -0.352 / -0.141; every coefficient,
N and AIC in the ordinal regression table including its star pattern; Study 1 inter-rater
kappas 0.8437 / 0.6899 / 0.6091 / 0.5561 at n = 60; power MDEs 0.032 and 0.0639, which appear
verbatim in `stats_report.txt`; five probe wordings at n = 3,932; dose-0 rates 0.3 / 31.4 / 38.0
pooling to 23.2%; dose 1-3 at 44.6%; chi-squared 376.54; GPT-4o 98.4% at dose 1, Claude 24.5% at
dose 3, Gemini 12.8% at dose 1; the dose-by-threshold interaction at p = 0.51; and the
reverse-momentum rates 0.0 / 1.0 / 21.9.

**Three corrections made.**

1. Study 2 was printed as 1,728 trials, which is the design count. The analysed sample is
   1,813, and the chi-squared of 376.54 reproduces only on 1,813. The appendix now states both.
2. Reverse momentum was printed as suppressing "full revision" to 0.0 / 1.0 / 21.9%. Those are
   the minor-suggestion rates. `full_revision` is 0.0% for all three models. Relabelled.
3. The Study 3 panel-level MDE is printed as 0.5 levels and no computation for it exists in the
   repository. Computed here: the paired difference over the 50 balanced-panel trials has
   sd 1.12 stripped and 1.08 unstripped, giving an MDE at 80% power of **0.44 and 0.43 levels**.
   The printed 0.5 is conservative, so the conclusion that the observed 0.74 and 0.94 exceed it
   holds with room. Left as printed; recorded here so it is no longer unsupported.

**The threshold-versus-gate claim, resolved 2026-09-20.** The appendix had stated "Quality
thresholds do not significantly affect the gate (Kruskal-Wallis $p > 0.40$ for all models)."
No test of threshold against `revision_gate` existed anywhere in the repository. The only
recorded Kruskal-Wallis tests are threshold against `overcorrection`, and four of those six are
significant (claude numeric 0.014, claude qualitative 0.0015, gemini numeric 0.000, gemini
qualitative 0.0014).

Computing the gate version directly, the claim held under 3 of 9 codings and scopes tried and
failed under 6. Liam chose the ordinal coding, which is the natural one for a three-level
outcome and which does **not** support the original sentence.

| Model | H | df | p |
|-------|--:|---:|--:|
| Gemini 2.5 Flash | 1.42 | 7 | 0.985 |
| GPT-4o | 2.01 | 7 | 0.960 |
| Claude Sonnet 4 | **14.33** | 7 | **0.046** |

- **Filter (exact):** `data/processed/scored_trials.jsonl`, factorial scope only (probe_type in
  leading, pilot_c; n = 1,280 per model, 3,840 total). Gate coded 0 for decline, 1 for
  suggest_minor, 2 for full_revision. Kruskal-Wallis across the eight `threshold_level` values.
- The appendix now reports these three figures rather than the unsupported blanket claim, and
  says only Claude reaches significance. The surrounding argument survives: the probe-type
  chi-squared on the same data runs 788.96 to 1326.89, two orders of magnitude larger, so
  phrasing still dominates the gate.

---

# FILE INDEX

## Core Data Files

| Path | Description |
|------|-------------|
| `data/study3/raw_responses/worker_trials.jsonl` | 720 five-turn trials (6 models x 40 tasks x 3 runs) |
| `data/study3/raw_responses/evaluator_results.jsonl` | Per-turn quality scores (6-level scale, field: level) |
| `data/study3/raw_responses/genuine_meta_labels.jsonl` | **Definitive** GENUINE/META labels for all 2,880 post-T1 turns (corrected) |
| `data/study3/raw_responses/self_reflection_results.jsonl` | Self-reflection recommended turns (n=720) |
| `data/study3/raw_responses/reversibility_results.jsonl` | Old model-judge pairwise T1-vs-T5 (n=720, unstripped, SUPERSEDED) |
| `data/study3/raw_responses/targeted_feedback_results.jsonl` | Targeted feedback scores (n=1047, filter to n=177 with corrected classifier) |
| `data/study3/raw_responses/oneshot_trials.jsonl` | One-shot baseline trials |
| `data/study3/raw_responses/confidence_trials.jsonl` | Confidence/self-assessment trials |

## Reversibility Annotation Files

| Path | Description |
|------|-------------|
| `data/study3/raw_responses/reversibility_pairs_stripped.json` | 50 stripped pairs served to annotators (LLM-stripped, 3 manual fixes) |
| `data/study3/raw_responses/reversibility_stripped_key.json` | Answer key: pair_id -> trial_id, model, domain, A_is, B_is |
| `data/study3/raw_responses/reversibility_judgments_liam.json` | Liam's 50 judgments (final, re-graded, 18 equivalent) |
| `data/study3/raw_responses/reversibility_judgments_troy.json` | Troy's 50 judgments (9 equivalent) |
| `data/study3/raw_responses/judge_stripped_pairwise.json` | Model judge (Claude Sonnet 4) pairwise picks on stripped pairs |
| `data/study3/raw_responses/reversibility_human_pairs.json` | 50 unstripped pairs (pre-LLM-stripping) |
| `data/study3/raw_responses/reversibility_human_key.json` | Key for unstripped pairs |
| `data/study3/raw_responses/llm_strip_results.json` | LLM stripping pass results (stripped text, review flags) |
| `data/study3/raw_responses/annotation_dump_50pairs.txt` | Human-readable dump of all 50 stripped pairs |

## Calibration & Reliability

| Path | Description |
|------|-------------|
| `data/study3/raw_responses/calibration_samples.json` | 64 stratified samples for judge calibration |
| `data/study3/raw_responses/judge_calibration.jsonl` | 6-model calibration scores on 64 samples |
| `data/study3/raw_responses/selected_judge.json` | Judge selection results (Claude Sonnet 4 selected) |
| `data/study3/raw_responses/human_ratings_liam.json` | Liam's human calibration ratings |
| `data/study3/raw_responses/human_ratings_troy.json` | Troy's human calibration ratings |
| `data/study3/raw_responses/human_ratings_sophie.json` | Sophie v1 ratings (superseded) |
| `data/study3/raw_responses/human_ratings_sophie_v2.json` | Sophie v2 ratings (64/64, level field, 1-5 scale, re-rated after rubric clarification) |
| `data/study3/raw_responses/human_eval.csv` | Human evaluation export |

## Meta-Commentary Analysis

| Path | Description |
|------|-------------|
| `data/study3/raw_responses/meta_wrapping_asymmetry.json` | Preamble/postamble counts for revision vs T1 side |
| `data/study3/raw_responses/stripped_rescore_results.json` | Re-scored quality on stripped content (50 balanced panel, T1+T5) |

## Other

| Path | Description |
|------|-------------|
| `data/study3/raw_responses/llm_revision_classifier.json` | LLM classifier config/results |
| `data/study3/raw_responses/candidate_finals_for_classification.jsonl` | Candidates sent to LLM classifier |
| `data/study3/raw_responses/sample_classifications.json` | Sample classification examples |
| `data/study3/raw_responses/annotation_id_mapping.json` | ID mapping for annotation UI |
| `data/study3/raw_responses/worker_trials_OLD_WRONG_PROBE.jsonl` | Old trials with wrong probe wording (archived) |

---

# PAPER INTEGRATION MAP

## Claims to Update

| # | Current Draft Claim | Draft Number | Corrected Number | Status | Section | Rewrite Note |
|---|---------------------|-------------|-----------------|--------|---------|-------------|
| 1 | Quality drops 4.27->3.04 (delta -1.23, n=135) | -1.23 | -0.94 (n=50) or -0.76 stripped | **SUPERSEDED** | Results 4.1, Abstract | n=135 was old keyword classifier. New balanced panel n=50. Stripped cliff -0.76. Reframe as "quality drops ~0.8 levels" |
| 2 | Llama improves +1.02 (T1=3.72, T5=4.74) | +1.02 | **-0.82** (T1=3.53, T5=2.71) | **SUPERSEDED** | Results 4.2, Discussion | Llama exception is GONE. Llama now degrades like others. Old +1.02 was artifact of keyword classifier counting decline-with-restatement as genuine. Delete "Llama exception" narrative. |
| 3 | Five of six models degrade | 5/6 | **All 6 degrade** (powered: only Llama) | **SUPERSEDED** | Results 4.2 | All models with sufficient n degrade. But only Llama is powered (n=45). Others have n=0-3 in balanced panel. |
| 4 | 83.7% T1-preference (blind reversibility) | 83.7% | **56.2%** (human, stripped) | **SUPERSEDED** | Results 4.3, Abstract, Discussion | 83.7% was model-judge on unstripped (inflated by meta-wrapping). Human on stripped = 56.2%. Reframe: mild T1-preference, not strong akrasia signal. |
| 5 | 64.3% revision-despite-sufficiency | 64.3% | **39.2%** (CI: 36-42%) | **SUPERSEDED** | Results 4.3, Abstract | Old keyword classifier counted meta as genuine. Corrected: 39.2%. Still shows models revise when they shouldn't, but less extreme. |
| 6 | Targeted feedback +2.0 levels (n=424) | +2.00 | **+1.16** stripped (n=177, p=5.7e-19) | **SUPERSEDED** | Results 4.5, Abstract | Unstripped +0.25 was deflated by meta-commentary inflating generic baseline. Stripped: +1.16, all models benefit. Use stripped delta in paper. |
| 7 | Revision tax 57.4% waste | 57.4% | **62.1%** (Interp A, ratio-of-means) | **SUPERSEDED** | Results 4.6, Abstract | Higher than old keyword (57.4%) because Interp A counts meta-response tokens as waste. Aggregate tax 164.2%. |
| 8 | Claude tax 251.6% | 251.6 | **251.6%** (unchanged under Interp A) | MATCH | Results 4.6, Table 2 | Claude unchanged; Llama now highest (436.0%). All t*=T1. |
| 9 | Llama t*=2 | T2 | **T1** | **SUPERSEDED** | Results 4.6 | Llama no longer improves; t*=T1 like all others |
| 10 | Akrasia gap: 48pp between knowledge and action | 48pp | Much smaller | **SUPERSEDED** | Results 4.3, Discussion | 83.7% -> 56.2%, 64.3% -> 39.2%. Gap collapses. Akrasia framing needs substantial rework. |
| 11 | Self-reflection mean 2.44, 40% T1 | 2.44 | **2.44** | UNCHANGED | Results 4.3 | No change needed |
| 12 | Edit ratio 0.97 | 0.97 | **0.97** | UNCHANGED | Results 4.4 | No change needed |
| 13 | Content drift slopes (instruction adherence, semantic similarity, word count) | various | UNKNOWN | **NEEDS RECOMPUTATION** | Results 4.4 | These were computed on all turns including meta. Need recomputation restricted to GENUINE turns only. |
| 14 | Structural features drop 56% | 56% | UNKNOWN | **NEEDS RECOMPUTATION** | Results 4.4 | Same issue |
| 15 | Constraint loss 58.5% | 58.5% | UNKNOWN | **NEEDS RECOMPUTATION** | Results 4.4 | Same issue |
| 16 | Enterprise projection $21K-$72K | $21-72K | Lower (tax% dropped) | **SUPERSEDED** | Results 4.6 | Recompute from corrected per-model $/task waste |
| 17 | DRP = Turn 2 for all degrading models | T2 | Likely unchanged conceptually | **NEEDS VERIFICATION** | Results 4.1 | Verify on corrected GENUINE-only trajectories |
| 18 | T1 sufficiency 93.3% | 93.3% | **87.6%** (or both: check denominator) | **NEEDS VERIFICATION** | Methods, Results 4.3 | Paper may have used different denominator or pre-6->2 recoding |
| 19 | Study 1: 99.9% vs 23.2% | 99.9/23.2 | **99.9/23.2** | UNCHANGED | Results (appendix) | |
| 20 | Study 2: GPT-4o 98% momentum | 98% | **98%** | UNCHANGED | Results (appendix) | |
| 21 | QWK 0.228, binary 73.4% | 0.228/73.4 | QW kappa 0.41-0.60 (3 pairs), binary 76.6-82.8%, alpha 0.529 | **SUPERSEDED** | Methods 3.3 | Old 0.228 was linear-weighted, 2-rater, no 6->2 recode. Now 3 raters, quadratic-weighted, 6->2 recoded. |

## NEW Claims (not in current draft)

| # | Finding | Number | Section | Note |
|---|---------|--------|---------|------|
| N1 | Meta-commentary inflates LLM-judge T1-preference | 91.8% -> 56.5% stripped (same 50 pairs) | Results (new) | Major methods contribution. Model judges are unreliable on revision comparison unless meta is stripped. |
| N2 | Meta-wrapping asymmetry | 84% revision, 14% T1 | Results/Methods (new) | Confound for any LLM-as-judge revision study. |
| N3 | Human reversibility with inter-annotator agreement | 56.2%, kappa=0.703 | Results (new) | Replaces model-judge reversibility as primary evidence. |
| N4 | Classifier difficulty (verbose decline) | 1.4% correction rate, 85 trials reclassified | Methods (new) | The keyword/LLM classifier gap is itself a finding about model behavior. |
| N5 | Cliff is 81% content degradation, 19% meta-inflation | -0.76 stripped vs -0.94 | Results (new) | Validates cliff survives meta-stripping. |
| N6 | Human-judge agreement improves from kappa ~0 to 0.57 after stripping | 0.57 | Results (new) | Demonstrates meta-commentary is the source of judge-human disagreement. |

---

# SECONDARY NUMBERS (Recomputed on Corrected Basis)

All numbers below use corrected LLM classifier (GENUINE-only), 6->2 recode, computed fresh from source data.

## S1. Content Drift Slopes (GENUINE-only)

| Metric | OLD (all turns) | NEW (GENUINE-only) | Material? |
|--------|----------------|-------------------|-----------|
| Word count slope | -50.9/turn (p=2.8e-19, n=576) | **+19.4/turn** (p=1.9e-8, n=356) | **YES: FLIPS SIGN** |
| Word count T1->T5 | 289->186 | **289->341** | **YES: INCREASES** |
| Char count T1->T5 | 1980->1280 | **1980->2426** | **YES: INCREASES** |

**The word-count decline was entirely a meta-response artifact.** Short decline messages (50-200 chars) drove the old -50.9 slope. Genuine revisions are LONGER than T1.

- **Filter:** For each trial, include T1 (all 720) and turns 2-5 only where `genuine_meta_labels.jsonl` has `classifier_label == "GENUINE"`. Per-trial slope via `scipy.stats.linregress` on (turn, word_count). T-test on n=356 per-trial slopes.

## S2. Structural Features (GENUINE-only)

| Turn | Old total_structure | New total_structure (GENUINE) | n |
|------|--------------------|-----------------------------|---|
| T1 | 7.47 | 12.52 | 720 |
| T2 | ~5.0 | 10.34 | 283 |
| T5 | ~3.3 | 9.00 | 96 |

| Metric | OLD | NEW |
|--------|-----|-----|
| T1->T5 drop | ~56% | **28.1%** |

- **Filter:** Regex counts of headers, bullets, numbered items, code blocks, bold phrases per response. GENUINE-only turns. Old numbers used all turns including meta-responses (which had minimal structure).
- Note: old and new `total_structure` definitions differ slightly (old counted fewer features). The 28.1% drop and new raw counts are the definitive numbers.

## S3. Constraint Satisfaction (GENUINE-only)

| Metric | OLD | NEW | Material? |
|--------|-----|-----|-----------|
| Constraint recall slope | -0.077 (p=7.4e-40, n=576) | **+0.002** (p=0.58, NS, n=356) | **YES: GOES NS** |
| >10% drop T1->T5 | 58.5% | **17.7%** (17/96) | **YES** |
| Recall T1 | 0.491 | 0.491 | Match |
| Recall T5 | 0.290 | **0.483** | **YES** |

**Constraint loss was largely a meta-response artifact.** Meta-responses (short declines) have near-zero keyword overlap with the task prompt, which drove the old -0.077 slope. Genuine revisions maintain ~49% keyword recall across all turns.

- **Filter:** Keyword overlap (words >= 4 chars) between `task_prompt` and response. GENUINE-only turns. Per-trial slope via polyfit. >10% drop = trials with balanced panel (GENUINE at T5) where T1_recall - T5_recall > 0.10.

## S4. Edit Ratio & Semantic Similarity (GENUINE-only)

| Metric | OLD | NEW | Material? |
|--------|-----|-----|-----------|
| Edit ratio (overall) | 0.97 | **0.61** | **YES** |
| Semantic drift T1->T5 | 0.51->0.37 | **0.54->0.48** | Moderate |
| Drift slope | -0.048 (p=2.9e-11, n=428) | **-0.038** (p=3.0e-21, n=205) | Minor |

The old 0.97 edit ratio included meta-responses which repeat content verbatim. Genuine revisions change ~61% of the text.

- **Filter (edit ratio):** `difflib.SequenceMatcher` ratio between consecutive GENUINE turns. 1 - ratio = fraction changed.
- **Filter (semantic sim):** Word-overlap Jaccard between T1 and each GENUINE turn. Per-trial slope via polyfit.

## S5. Per-Model Table

Already in Section 2 (balanced panel n=50: Llama 45, Qwen 3, Claude 2, others 0). No further recomputation needed.

### Survival to T5 (GENUINE-only)

| Model | Survival to T5 |
|-------|---------------|
| llama-3.3-70b | 64/120 (53.3%) |
| claude-sonnet-4 | 15/120 (12.5%) |
| deepseek-v4 | 7/120 (5.8%) |
| qwen-3-235b | 6/120 (5.0%) |
| gpt-4o | 3/120 (2.5%) |
| gemini-2.5-flash | 1/120 (0.8%) |

### DRP (first turn where GENUINE mean quality < T1, min n>=5)

| Model | DRP | T1 mean |
|-------|-----|---------|
| claude-sonnet-4 | T2 | 4.28 |
| gpt-4o | T2 | 3.99 |
| llama-3.3-70b | T2 | 3.75 |
| qwen-3-235b | T2 | 4.35 |
| deepseek-v4 | T3 | 4.48 |
| gemini-2.5-flash | -- (n<5 at all post-T1 turns) | 3.82 |

- **Filter:** Mean quality per turn restricted to GENUINE responses, 6->2 recode. DRP = first turn with mean < T1 mean AND n >= 5.

## S6. LOCF Analysis (GENUINE carry-forward)

| Metric | OLD | NEW |
|--------|-----|-----|
| LOCF T1 | ~4.27 | **4.11** |
| LOCF T5 | ~2.95 | **3.60** |
| LOCF delta | -1.32 | **-0.51** (p=1.0e-32) |
| LOCF delta (stripped) | -- | **-0.30** (p=3.8e-18) |

- **Stripped sensitivity:** LOCF T5 rises from 3.60 to 3.81 after stripping (meta was penalizing quality). Delta shrinks 41% but remains highly significant. See Stripped Sensitivity Analysis M3.
- **Filter:** For each trial, carry forward the last GENUINE-turn quality score. If a turn is META, its LOCF score = the previous GENUINE score. All 720 trials, Wilcoxon on paired T1-vs-T5.

## S7. Enterprise Projection (Interp A pricing)

| Model | $/task waste | Monthly (500-person org) | Annual |
|-------|-------------|------------------------|--------|
| gemini-2.5-flash | $0.0001 | $27 | $323 |
| deepseek-v4 | $0.0005 | $164 | $1,969 |
| qwen-3-235b | $0.0009 | $271 | $3,250 |
| llama-3.3-70b | $0.0013 | $390 | $4,680 |
| gpt-4o | $0.0053 | $1,581 | $18,972 |
| claude-sonnet-4 | $0.0182 | $5,473 | $65,678 |

- **Assumptions:** 500 employees, 30 tasks/employee/day, 20 workdays/month. 2025 API output-token pricing. Interp A (meta tokens count as waste).
- **Supersedes:** Old $21K-$72K range was on old keyword classifier and different pricing assumptions.
- **FLAG:** Dollar figures are pricing-tier-dominated and based on 2025 rates. Range is $323-$65,678/year depending entirely on which model.

## S8. T1 Sufficiency Rate Discrepancy -- RESOLVED

| Version | Rate | Explanation |
|---------|------|-------------|
| Paper draft (93.3%) | 672/720 | Raw scale: level >= 4 includes level 6 as "sufficient" |
| Corrected (87.6%) | 631/720 | 6->2 recode: level 6 becomes 2 (below threshold) |
| Difference | 41 trials | Had T1 level=6 ("Overdone"), recoded to 2 |

**Use 87.6%** (consistent with all other corrected numbers using 6->2 recode).

## S9. Pooled Revision-Only Trajectory (GENUINE-only)

| Turn | OLD (keyword) | NEW (GENUINE-only) | n |
|------|--------------|-------------------|---|
| T1 | 4.34 | **4.11** | 720 |
| T2 | ~3.40 | **3.25** | 283 |
| T3 | ~2.90 | **3.01** | 185 |
| T4 | ~2.70 | **2.97** | 154 |
| T5 | 2.45 | **2.85** | 96 |

Delta T1->T5: OLD -1.89, NEW **-1.26** (unstripped), **-1.04** (stripped).

- **Stripped sensitivity:** Stripping removes meta that penalizes quality (triggers "Overdone"). T5 rises from 2.85 to 3.07. Trajectory is 17% shallower but still monotonically declining. See Stripped Sensitivity Analysis M4.
- **Filter:** Mean quality per turn, T1 = all 720, T2-T5 = GENUINE-only. 6->2 recode.

## S10. Domain-Level Variation (GENUINE-only)

| Domain | T1 | T5 | Delta | n(T5) |
|--------|----|----|-------|-------|
| analysis | 3.98 | 2.76 | -1.21 | 17 |
| code | 3.95 | 2.80 | -1.15 | 30 |
| creative | 4.12 | 2.89 | -1.22 | 19 |
| data_logic | 4.35 | 3.00 | -1.35 | 17 |
| writing | 4.16 | 2.85 | -1.31 | 13 |

All domains degrade. Data_logic has steepest cliff (-1.35 unstripped, -1.01 stripped), code has shallowest (-1.15 unstripped, -1.05 stripped). All T5 n are small (13-30). See Stripped Sensitivity Analysis M5 for stripped values.

- **Filter:** GENUINE-only quality per domain. T1 = all 144 per domain. T5 = GENUINE at T5 only.

## S11. Level 6 "Overdone" Rate (GENUINE-only)

| Turn | OLD (all turns) | NEW (GENUINE-only) |
|------|----------------|-------------------|
| T1 | 3.1% (22/720) | **5.7%** (41/720) |
| T2 | 14.9% | **33.9%** (96/283) |
| T3 | -- | **42.2%** (78/185) |
| T4 | -- | **42.9%** (66/154) |
| T5 | -- | **47.9%** (46/96) |

**Level 6 rate rises sharply in genuine revisions.** The old low rates were diluted by meta-responses (which never score 6). On stripped text, T5 rate drops from 47.9% to **34.4%** -- confirming meta-commentary triggers "Overdone" (~14pp inflation). But even stripped, a third of genuine T5 revisions are still Overdone (real over-polishing, not artifact). See Stripped Sensitivity Analysis M6.

- **Filter:** Count of evaluator level == 6 (pre-recode) per turn, denominator = GENUINE responses at that turn.
- Note: T1 old value (3.1% = 22/720) vs new (5.7% = 41/720) discrepancy may be due to different T1 counting in the old analysis.

## S12. Old Reversibility Sub-Analyses -- SUPERSEDED

Replaced entirely by human annotation (Section 7) and stratified results (Section 9). Delete from paper.

## S13. Momentum Connection -- NARRATIVE ONLY

Study 2 numbers (1,728 trials, GPT-4o 98% momentum) are unchanged (different dataset). Framing adjustment: revision-despite-sufficiency is 39.2% (not 64.3%), so the "every turn is a momentum turn" claim should be softened, but the momentum mechanism (suggestibility drives acquiescence) still applies.

## S14. Targeted Feedback Per-Model (GENUINE-only)

| Model | n | Delta | p | Significant? |
|-------|---|-------|---|-------------|
| claude-sonnet-4 | 51 | +0.51 | 0.004 | Yes |
| deepseek-v4 | 19 | +1.58 | 0.005 | Yes |
| gemini-2.5-flash | 3 | +1.00 | -- (n<5) | Underpowered |
| gpt-4o | 12 | -0.17 | 0.750 | No |
| llama-3.3-70b | 71 | -0.17 | 0.027 | Marginal (wrong direction) |
| qwen-3-235b | 21 | +0.00 | 1.000 | No |

**SUPERSEDED by stripped analysis.** The unstripped per-model story ("only Claude and DeepSeek benefit") was an artifact of meta-commentary inflating the generic baseline for models with verbose meta-wrapping (Llama, Qwen, GPT-4o). On stripped text, ALL powered models show significant positive deltas (+0.31 to +1.62). See Stripped Sensitivity Analysis M2 for the corrected per-model table.

- **Filter:** Same as Section 5 (next-turn GENUINE filter, 6->2 recode). Grouped by model.
- **Supersedes:** Both the old "96-99%" claim AND the intermediate "only 2/6 benefit" finding.

## S15. Sophie v2 Reliability -- RESOLVED

Already fixed in Section 11. Sophie v2 has 64/64 valid ratings. Three-rater QW kappas: 0.406, 0.578, 0.603. Alpha = 0.529.

---

# STRIPPED SENSITIVITY ANALYSIS (Audit Item 8)

All 3,600 outputs (720 trials x 5 turns) were regex-stripped of meta-commentary preambles/postambles
(same validated patterns as the reversibility pairs) and the 1,200 that changed were rescored by
Claude Sonnet 4 at temperature 0 using the identical EVAL_PROMPT. Scores 6->2 recoded.

**Key finding: meta-commentary PENALIZES quality scores** (triggers "Overdone" = level 6), so
stripping makes revisions look BETTER, not worse. The contamination direction is opposite to the
reversibility concern (where meta helped identify the revision side). This means the unstripped
quality trajectory was steeper than reality -- the cliff and LOCF delta were both inflated.

## Stripping Scope

| Turn | Outputs stripped | Rate |
|------|-----------------|------|
| T1 | 69/720 | 9.6% |
| T2 | 361/720 | 50.1% |
| T3 | 282/720 | 39.2% |
| T4 | 278/720 | 38.6% |
| T5 | 210/720 | 29.2% |
| **Total** | **1,200/3,600** | **33.3%** |

Source: `data/study3/raw_responses/stripped_rescore_full.jsonl` (3,600 records, one per trial x turn)

## Metric-by-Metric Comparison

### M1. Revision-Despite-Sufficiency

| Metric | Unstripped | Stripped | Change |
|--------|-----------|---------|--------|
| Sufficient turns (level >= 4) | 938 | 1,038 | +100 |
| Revised despite sufficient | 368 | 411 | +43 |
| **Rate** | **39.2%** | **39.6%** | **+0.4pp** |

**Verdict: HOLDS.** Denominator grows because stripping removes meta that was pushing some scores below 4.
Rate barely changes. Direction and significance unchanged.

### M2. Targeted Feedback

| Version | Targeted mean | Generic mean | Delta | p | n |
|---------|--------------|-------------|-------|---|---|
| Both unstripped | 4.68 | 4.43 | **+0.25** | 3.75e-03 | 177 |
| Both stripped | 4.68 | 3.53 | **+1.16** | 5.74e-19 | 177 |

Targeted revisions have almost no meta-commentary (9/177 = 5% had any to strip; targeted mean barely
changed: 4.68 -> 4.63). Generic revisions have substantial meta-commentary that was INFLATING their
scores (4.43 -> 3.53 stripped). The real advantage of targeted feedback is +1.16 levels, not +0.25.

**Per-model (both-stripped):**

| Model | n | Delta | p |
|-------|---|-------|---|
| claude-sonnet-4 | 51 | +0.31 | 0.012 |
| deepseek-v4 | 19 | +1.05 | 0.012 |
| gemini-2.5-flash | 3 | +2.33 | -- (n<5) |
| gpt-4o | 12 | +1.33 | 0.008 |
| llama-3.3-70b | 71 | +1.62 | 9.2e-12 |
| qwen-3-235b | 21 | +1.48 | 4.5e-04 |

**Verdict: REVERSES the per-model story.** On stripped text, ALL powered models show significant
positive deltas. The old "only Claude and DeepSeek benefit" finding (S14) was an artifact of
meta-commentary inflating the generic baseline for models with verbose meta-wrapping (Llama, Qwen, GPT-4o).

### M3. LOCF Analysis

| Metric | Unstripped | Stripped | Change |
|--------|-----------|---------|--------|
| LOCF T1 | 4.11 | 4.11 | 0 |
| LOCF T5 | 3.60 | 3.81 | +0.21 |
| **Delta** | **-0.51** | **-0.30** | **41% smaller** |
| p-value | 1.0e-32 | 3.8e-18 | Still significant |

**Verdict: HOLDS but attenuated.** Meta-commentary was penalizing carried-forward scores. Real
LOCF degradation is -0.30 levels, not -0.51. Highly significant either way (n=720).

### M4. Pooled Revision-Only Trajectory (GENUINE-only)

| Turn | Unstripped | Stripped | Shift | n |
|------|-----------|---------|-------|---|
| T1 | 4.11 | 4.11 | 0 | 720 |
| T2 | 3.25 | 3.66 | +0.41 | 283 |
| T3 | 3.01 | 3.40 | +0.39 | 185 |
| T4 | 2.97 | 3.34 | +0.37 | 154 |
| T5 | 2.85 | 3.07 | +0.22 | 96 |
| **Delta T1->T5** | **-1.26** | **-1.04** | **17% smaller** | |

**Verdict: HOLDS.** Quality still degrades monotonically. Stripped T5 (3.07) is still below
Sufficient (4.0). But the decline is 17% shallower than unstripped.

### M5. Domain-Level Variation (GENUINE-only)

| Domain | Unstripped delta | Stripped delta | Shift | n(T5) |
|--------|-----------------|---------------|-------|-------|
| analysis | -1.21 | -1.16 | +0.05 | 17 |
| code | -1.15 | -1.05 | +0.10 | 30 |
| creative | -1.22 | -0.82 | +0.40 | 19 |
| data_logic | -1.35 | -1.01 | +0.34 | 17 |
| writing | -1.31 | -1.06 | +0.25 | 13 |

**Verdict: HOLDS for all domains.** Creative shows the largest shift (meta-commentary most
prevalent in creative tasks). All domains still degrade. Direction unchanged everywhere.

### M6. Level-6 "Overdone" Rate (GENUINE-only, pre-recode)

| Turn | Unstripped | Stripped | Shift |
|------|-----------|---------|-------|
| T1 | 5.7% (41/720) | 5.6% (40/720) | -0.1pp |
| T2 | 33.9% (96/283) | 18.0% (51/283) | **-15.9pp** |
| T3 | 42.2% (78/185) | 28.6% (53/185) | **-13.5pp** |
| T4 | 42.9% (66/154) | 27.9% (43/154) | **-15.0pp** |
| T5 | 47.9% (46/96) | 34.4% (33/96) | **-13.5pp** |

**Verdict: CONFIRMS meta preambles trigger "Overdone."** Level-6 rates drop 13-16pp after stripping.
The evaluator interprets "Here's my revised version..." and "Let me know if you'd like changes" as
"unrequested complexity." Even stripped, 34.4% of genuine T5 revisions are still Overdone -- this is
real over-polishing, not just meta-commentary artifact.

### Balanced Panel Cliff (reference, already in Section 2)

| Metric | Unstripped | Stripped | Change |
|--------|-----------|---------|--------|
| T1 | 3.66 | 3.66 | 0 |
| T5 | 2.72 | 2.92 | +0.20 |
| **Delta** | **-0.94** | **-0.74** | **21% smaller** |

Consistent with the earlier 50-pair rescore (19-21% inflation range).

## Summary: What Moves, What Holds

| # | Metric | Unstripped | Stripped | Moves? | Direction? |
|---|--------|-----------|---------|--------|-----------|
| 1 | Rev-despite-suff | 39.2% | 39.6% | No | Same |
| 2 | Targeted feedback | +0.25 | +1.16 | **YES** | Same, much stronger |
| 2b | Targeted per-model | 2/6 benefit | **All benefit** | **YES** | Reverses |
| 3 | LOCF delta | -0.51 | -0.30 | Moderate | Same, attenuated |
| 4 | Pooled trajectory delta | -1.26 | -1.04 | Moderate | Same, attenuated |
| 5 | Domain deltas | -1.15 to -1.35 | -0.82 to -1.16 | Moderate | Same, attenuated |
| 6 | Level-6 at T5 | 47.9% | 34.4% | **YES** | Same, lower |
| -- | Balanced cliff | -0.94 | -0.74 | Moderate | Same (21% smaller) |

**No metric changes direction or loses significance.** The three material movers are:
1. Targeted feedback delta quintuples (+0.25 -> +1.16) and becomes universal across models
2. Level-6 rate drops ~14pp (meta-commentary was triggering "Overdone")
3. LOCF delta nearly halves (-0.51 -> -0.30)

---

# STATUS CHECK

- No scripts mid-run
- No background processes pending
- Server running on port 3847 (PID 96795) -- can be killed when no longer needed
- All judgment files written and verified
- All rescore/judge API calls completed successfully
- No uncommitted analysis artifacts that would be lost
