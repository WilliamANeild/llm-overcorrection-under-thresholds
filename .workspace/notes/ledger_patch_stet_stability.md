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
