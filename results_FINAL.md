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
- **FLAG:** The per-turn breakdown (T1:14%, T2:92%...) was computed in a prior session on a broader set; verify it matches the 50-pair scope or the full 720-trial set before citing.

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
