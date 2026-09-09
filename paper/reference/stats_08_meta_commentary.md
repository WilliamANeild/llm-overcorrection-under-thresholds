# Meta-Commentary Stripping: Descriptive Results Not Yet in the Paper

Generated 2026-09-06. Descriptive only. No sample definition, specification or
observation set was changed. All quality scores use the ledger's 6->2 recode, and
all GENUINE/META labels are the ledger's corrected LLM classifier labels
(718 GENUINE / 2,162 META over 2,880 post-T1 observations).

Analysis code: `.workspace/scratch/meta_commentary_extra_analysis.py`,
`.workspace/scratch/meta_commentary_extra_analysis2.py`,
`.workspace/scratch/meta_scope_sweep3.py`. The stripping functions and regex
pattern lists were copied verbatim into those scripts from
`scripts/study3/stripped_rescore_full.py` and `scripts/study3/audit_meta_commentary.py`.
`strip_meta_commentary.py` was never imported (it has no main guard and overwrites
annotation files on import). No data file was modified.

---

## 0. Two measures, kept apart throughout

The project contains two operational definitions of "this output carries
meta-commentary," and they do not agree. Every number below states which one it uses.

**STRIP.** `chars_removed > 0` in `stripped_rescore_full.jsonl`. This is the
paragraph-level pass that actually produced the rescore: it splits on blank lines,
walks in from both ends, and drops a leading or trailing paragraph only if it matches
a preamble/postamble pattern **and** contains no CONTENT_SIGNALS (code fence, markdown
heading, numbered list, table row, salutation, currency, percentage). It refuses to
strip if the survivor would be under 30 percent of the original.

**DETECT.** The `audit_meta_commentary.py` regexes searched in the first 300 and last
400 characters, with no content veto. This is the measure behind the reported 84 percent
vs 14 percent wrapping asymmetry in Section 8 of the ledger.

Cross-tabulation, all 3,600 outputs:

| | STRIP yes | STRIP no |
|---|---|---|
| **DETECT yes** | 1,128 | 1,153 |
| **DETECT no** | 72 | 1,247 |

DETECT rate 63.4 percent, STRIP rate 33.3 percent. The 1,153-cell is the content veto
doing its work: the regex fires on a sentence that sits inside a paragraph the pass
declines to remove because that paragraph also carries task content. Any claim about
"how much meta-commentary there is" moves by a factor of two depending on which
definition is used, so the paper should name one.

**Filter (this section):** All 3,600 rows of `stripped_rescore_full.jsonl`. STRIP from
the stored `chars_removed`. DETECT recomputed on the original response text pulled from
`worker_trials.jsonl` field `responses[turn-1]`.

**Verification:** `orig_score` in `stripped_rescore_full.jsonl` matches
`evaluator_results.jsonl` `level` with 6->2 recode in 3,600 of 3,600 rows; `orig_level_raw`
matches `level` exactly in 3,600 of 3,600. `was_rescored` is true in exactly the 1,200 rows
with `chars_removed > 0`, and no unrescored row has a changed score.

---

## 1. How much text stripping removes

**Filter:** All 3,600 rows of `stripped_rescore_full.jsonl`. `chars_removed` as stored.
Original length = `len(worker_trials.jsonl responses[turn-1])`. Share = chars_removed /
original length. Percentiles are linear-interpolated.

Corpus totals: 3,928,336 characters across 3,600 outputs; 231,952 removed, or **5.90 percent
of the corpus**. 1,200 of 3,600 outputs (33.3 percent) lost any text.

### Conditional on being stripped (n = 1,200)

| Cut | n | mean | SD | p10 | p25 | median | p75 | p90 | p99 | max | mean share | median share | max share |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| All stripped | 1,200 | 193 | 126 | 66 | 104 | 162 | 257 | 372 | 573 | 1,468 | 21.2% | 14.6% | 69.7% |
| T1 | 69 | 121 | 84 | 44 | 64 | 95 | 157 | 251 | 380 | 414 | 8.8% | 6.1% | 44.9% |
| T2 | 361 | 190 | 119 | 73 | 101 | 152 | 259 | 379 | 526 | 623 | 17.8% | 11.2% | 67.7% |
| T3 | 282 | 213 | 146 | 80 | 114 | 184 | 284 | 374 | 625 | 1,468 | 22.4% | 16.1% | 69.7% |
| T4 | 278 | 194 | 118 | 66 | 107 | 164 | 255 | 372 | 559 | 622 | 24.3% | 18.8% | 69.3% |
| T5 | 210 | 194 | 121 | 50 | 106 | 172 | 258 | 359 | 565 | 604 | 25.5% | 21.9% | 69.1% |

The absolute size of the removed boilerplate is close to constant across turns 2 to 5
(190 to 213 characters on average, medians 152 to 184). The share rises from 17.8 percent
at T2 to 25.5 percent at T5 because the task content shrinks underneath it: mean
unstripped output length falls from 1,980 characters at T1 to 1,174 at T2, 924 at T3, 728
at T4 and 650 at T5. By T5 the median stripped output is 22 percent conversational
wrapper. The distribution has a long right tail: the 99th percentile removes 573
characters, and the largest single removal is 1,468.

### By model (conditional on being stripped)

| Model | n | mean | median | p90 | max | mean share | median share |
|---|---|---|---|---|---|---|---|
| claude-sonnet-4 | 252 | 140 | 120 | 243 | 400 | 15.1% | 9.9% |
| deepseek-v4 | 161 | 225 | 217 | 357 | 660 | 39.4% | 41.1% |
| gemini-2.5-flash | 60 | 142 | 120 | 214 | 604 | 29.2% | 23.7% |
| gpt-4o | 123 | 247 | 208 | 481 | 626 | 21.6% | 18.3% |
| llama-3.3-70b | 333 | 218 | 177 | 391 | 1,468 | 17.9% | 11.7% |
| qwen-3-235b | 271 | 181 | 155 | 373 | 625 | 18.2% | 13.0% |

DeepSeek is the extreme case: when it wraps, the median wrapper is 41 percent of the
response. GPT-4o writes the longest wrappers in absolute terms (mean 247 characters)
but wraps least often among the frequent wrappers.

### By domain (conditional on being stripped)

| Domain | n | mean | median | mean share | median share |
|---|---|---|---|---|---|
| analysis | 215 | 181 | 149 | 21.3% | 14.1% |
| code | 348 | 202 | 172 | 18.0% | 11.4% |
| creative | 208 | 208 | 172 | 24.2% | 19.4% |
| data_logic | 236 | 186 | 157 | 15.8% | 9.6% |
| writing | 193 | 185 | 149 | 30.2% | 27.0% |

Writing carries the highest share removed (median 27 percent) on the shortest outputs
(mean 491 characters unstripped). Code has the highest strip rate but the lowest share,
because code responses are long.

### Unconditional means and strip rates

| Cut | n | mean chars removed | mean original length | removed as % of that cell's text | strip rate |
|---|---|---|---|---|---|
| T1 | 720 | 11.6 | 1,980 | 0.59% | 9.6% |
| T2 | 720 | 95.5 | 1,174 | 8.13% | 50.1% |
| T3 | 720 | 83.4 | 924 | 9.03% | 39.2% |
| T4 | 720 | 75.0 | 728 | 10.30% | 38.6% |
| T5 | 720 | 56.7 | 650 | 8.71% | 29.2% |
| claude-sonnet-4 | 600 | 58.6 | 1,316 | 4.46% | 42.0% |
| deepseek-v4 | 600 | 60.3 | 707 | 8.52% | 26.8% |
| gemini-2.5-flash | 600 | 14.2 | 752 | 1.89% | 10.0% |
| gpt-4o | 600 | 50.7 | 851 | 5.95% | 20.5% |
| llama-3.3-70b | 600 | 121.0 | 1,673 | 7.23% | 55.5% |
| qwen-3-235b | 600 | 81.8 | 1,248 | 6.55% | 45.2% |
| analysis | 720 | 54.0 | 1,056 | 5.11% | 29.9% |
| code | 720 | 97.6 | 2,043 | 4.77% | 48.3% |
| creative | 720 | 60.0 | 648 | 9.27% | 28.9% |
| data_logic | 720 | 61.0 | 1,218 | 5.01% | 32.8% |
| writing | 720 | 49.5 | 491 | 10.09% | 26.8% |

### Strip rate by model and turn (120 outputs per cell)

| Model | T1 | T2 | T3 | T4 | T5 | All |
|---|---|---|---|---|---|---|
| claude-sonnet-4 | 4.2% | 90.0% | 40.8% | 46.7% | 28.3% | 42.0% |
| deepseek-v4 | 5.0% | 27.5% | 35.8% | 35.0% | 30.8% | 26.8% |
| gemini-2.5-flash | 2.5% | 20.8% | 9.2% | 9.2% | 8.3% | 10.0% |
| gpt-4o | 26.7% | 25.8% | 19.2% | 16.7% | 14.2% | 20.5% |
| llama-3.3-70b | 0.0% | 80.0% | 78.3% | 68.3% | 50.8% | 55.5% |
| qwen-3-235b | 19.2% | 56.7% | 51.7% | 55.8% | 42.5% | 45.2% |

Two models depart from the common pattern at T1. GPT-4o wraps 26.7 percent of its first
answers and Qwen 19.2 percent, against 0.0 percent for Llama and 2.5 percent for Gemini.
The turn-1 asymmetry the paper reports is therefore a property of four of the six models,
not all six.

### Strip rate by domain and turn (144 outputs per cell)

| Domain | T1 | T2 | T3 | T4 | T5 | All |
|---|---|---|---|---|---|---|
| analysis | 5.6% | 48.6% | 31.9% | 37.5% | 25.7% | 29.9% |
| code | 11.8% | 74.3% | 59.0% | 52.1% | 44.4% | 48.3% |
| creative | 9.0% | 42.4% | 34.0% | 35.4% | 23.6% | 28.9% |
| data_logic | 15.3% | 45.1% | 36.1% | 34.7% | 32.6% | 32.8% |
| writing | 6.2% | 40.3% | 34.7% | 33.3% | 19.4% | 26.8% |

### Preamble and postamble split of the removed characters

**Filter:** Same 3,600 outputs. The strip walk was rerun with the front and back removals
recorded separately (function copied verbatim from `stripped_rescore_full.py`). Front plus
back reproduces the stored `chars_removed` to within 6 characters in 3,600 of 3,600 rows;
the residual is whitespace trimmed at the join.

Of 231,952 removed characters, 130,104 (56.1 percent) come off the front and 101,723
(43.9 percent) off the back.

| Turn | n stripped | front only | back only | both | mean front | mean back |
|---|---|---|---|---|---|---|
| T1 | 69 | 21 | 39 | 9 | 50 | 71 |
| T2 | 361 | 198 | 64 | 99 | 125 | 65 |
| T3 | 282 | 126 | 78 | 78 | 123 | 90 |
| T4 | 278 | 106 | 102 | 70 | 99 | 96 |
| T5 | 210 | 68 | 95 | 47 | 93 | 101 |

| Model | n stripped | front only | back only | both | mean front | mean back |
|---|---|---|---|---|---|---|
| claude-sonnet-4 | 252 | 187 | 34 | 31 | 106 | 34 |
| deepseek-v4 | 161 | 20 | 98 | 43 | 76 | 149 |
| gemini-2.5-flash | 60 | 22 | 32 | 6 | 57 | 85 |
| gpt-4o | 123 | 23 | 52 | 48 | 131 | 116 |
| llama-3.3-70b | 333 | 223 | 9 | 101 | 159 | 59 |
| qwen-3-235b | 271 | 44 | 153 | 74 | 69 | 112 |

Models have distinguishable wrapping styles. Claude and Llama front-load ("Here is the
revised version"): 74 percent and 67 percent of their stripped outputs are front-only.
DeepSeek and Qwen back-load ("Let me know if you would like any changes"): 61 percent and
56 percent are back-only. GPT-4o does both, on 39 percent of its stripped outputs. Within
a trial the wrapper also migrates from front to back as turns accumulate: front-only falls
from 55 percent of stripped outputs at T2 to 32 percent at T5 while back-only rises from
18 percent to 45 percent.

---

## 2. Meta-commentary prevalence across turns, and the flagged per-turn series

### The flag is correct: the ledger's series does not reproduce

Section 8 of `results_FINAL.md` reports "meta-commentary prevalence by turn (genuine
revisions only): T1 14 percent, T2 92 percent, T3 85 percent, T4 79 percent, T5 68 percent"
and flags it as computed in a prior session on an unknown set. Eighteen candidate scopes
were tested against that series. None reproduces it.

**Filter (sweep):** For each candidate scope, prevalence at turn T = (outputs at turn T
matching the measure) / (outputs at turn T in scope). Scopes and measures as labelled.

| Candidate scope and measure | T1 | T2 | T3 | T4 | T5 |
|---|---|---|---|---|---|
| **Ledger's reported series** | **14** | **92** | **85** | **79** | **68** |
| All 3,600, DETECT | 14.4 | 84.4 | 75.7 | 75.0 | 67.2 |
| All 3,600, STRIP | 9.6 | 50.1 | 39.2 | 38.6 | 29.2 |
| T1 all / post-T1 GENUINE, DETECT | 14.4 | 92.6 | 89.2 | 86.4 | 78.1 |
| T1 all / post-T1 GENUINE, STRIP | 9.6 | 91.2 | 87.0 | 85.1 | 74.0 |
| T1 all / post-T1 keyword-REVISION, DETECT | 14.4 | 91.4 | 86.7 | 85.2 | 73.9 |
| T1 all / post-T1 keyword-REVISION, STRIP | 9.6 | 68.4 | 68.5 | 67.4 | 52.6 |
| GENUINE, DETECT preamble only | 5.6 | 87.3 | 80.0 | 76.6 | 63.5 |
| GENUINE, DETECT postamble only | 11.4 | 42.4 | 44.9 | 39.6 | 39.6 |
| 50 balanced-panel trials, DETECT | 6.0 | 88.0 | 86.0 | 94.0 | 86.0 |
| 50 balanced-panel trials, STRIP | 4.0 | 82.0 | 84.0 | 94.0 | 88.0 |
| 50 reversibility pairs (T1 side; revision side by `last_rev_turn`), DETECT | 14.0 | 90.9 | 85.7 | 81.2 | 77.8 |
| 50 reversibility pairs, strip-pattern DETECT | 14.0 | 100.0 | 100.0 | 81.2 | 88.9 |
| All 3,600, strip-pattern DETECT (300/400 windows) | 14.9 | 89.0 | 77.4 | 74.2 | 64.7 |
| GENUINE, strip-pattern DETECT (300/400 windows) | 14.9 | 93.6 | 91.4 | 88.3 | 78.1 |
| All 3,600, strip-pattern DETECT (whole text) | 22.5 | 89.9 | 79.2 | 76.9 | 67.5 |
| GENUINE, strip-pattern DETECT (whole text) | 22.5 | 95.1 | 94.1 | 92.2 | 84.4 |
| All 3,600, audit DETECT (whole text) | 23.6 | 85.8 | 77.8 | 77.1 | 69.2 |
| 50 balanced-panel trials, strip-pattern DETECT | 6.0 | 88.0 | 90.0 | 96.0 | 90.0 |

The series is not internally consistent with any one scope. Its T1 value (14) matches both
the 50-pair T1 side (7/50 = 14.0 percent) and the full corpus at T1 (14.4 percent); its T2
value (92) matches GENUINE-only DETECT (92.6 percent); its T5 value (68) matches the full
corpus (67.2 percent) but not GENUINE-only (78.1 percent); its T4 value (79) sits between
every candidate. It appears to mix scopes. **Do not cite it.**

Note that the reversibility-pair cells are thin: the revision side splits 11 / 14 / 16 / 9
across T2 to T5, so those percentages move 6 to 11 points per single output.

### Replacement series that do reproduce

Two are defensible, and they answer different questions. State which one is being used.

**(a) All 3,600 outputs, DETECT.** The prevalence of conversational wrapping in the corpus
as delivered, independent of whether a turn was a genuine revision.

| Turn | Preamble | Postamble | Both | Either | n |
|---|---|---|---|---|---|
| T1 | 5.6% | 11.4% | 2.5% | **14.4%** | 720 |
| T2 | 63.7% | 59.0% | 38.3% | **84.4%** | 720 |
| T3 | 46.7% | 54.7% | 25.7% | **75.7%** | 720 |
| T4 | 43.6% | 55.1% | 23.8% | **75.0%** | 720 |
| T5 | 36.0% | 51.2% | 20.0% | **67.2%** | 720 |

**(b) T1 all 720, post-T1 GENUINE revisions only, DETECT.** The prevalence within the
analytic sample the quality trajectory is built on.

| Turn | Preamble | Postamble | Either | n |
|---|---|---|---|---|
| T1 | 5.6% | 11.4% | **14.4%** | 720 |
| T2 | 87.3% | 42.4% | **92.6%** | 283 |
| T3 | 80.0% | 44.9% | **89.2%** | 185 |
| T4 | 76.6% | 39.6% | **86.4%** | 154 |
| T5 | 63.5% | 39.6% | **78.1%** | 96 |

The same series on the STRIP measure: T1 9.6 percent, T2 91.2, T3 87.0, T4 85.1, T5 74.0.

Series (b) is the one that bears on the analysis, and it is materially higher at every
post-T1 turn than the corpus series (a). The turn-1 to turn-2 jump on (b) is 14.4 to 92.6
percent, a 78-point rise.

### Prevalence by model and turn (DETECT, all 3,600, 120 per cell)

| Model | T1 | T2 | T3 | T4 | T5 |
|---|---|---|---|---|---|
| claude-sonnet-4 | 9.2% | 100.0% | 59.2% | 73.3% | 60.8% |
| deepseek-v4 | 7.5% | 88.3% | 86.7% | 83.3% | 66.7% |
| gemini-2.5-flash | 8.3% | 55.8% | 48.3% | 42.5% | 42.5% |
| gpt-4o | 31.7% | 98.3% | 95.8% | 96.7% | 95.0% |
| llama-3.3-70b | 5.8% | 85.8% | 84.2% | 76.7% | 73.3% |
| qwen-3-235b | 24.2% | 78.3% | 80.0% | 77.5% | 65.0% |

Every model wraps more after the first pushback, but the spread is wide. GPT-4o wraps
95 to 97 percent of every post-T1 turn and never comes back down. Gemini stays under
56 percent throughout. Claude wraps every single T2 output (120/120) and then falls to
59 percent by T3.

### Prevalence by domain and turn (DETECT, all 3,600, 144 per cell)

| Domain | T1 | T2 | T3 | T4 | T5 |
|---|---|---|---|---|---|
| analysis | 4.9% | 87.5% | 69.4% | 80.6% | 68.1% |
| code | 14.6% | 81.9% | 78.5% | 79.2% | 70.8% |
| creative | 9.7% | 89.6% | 81.9% | 75.0% | 61.8% |
| data_logic | 15.3% | 76.4% | 66.0% | 69.4% | 63.9% |
| writing | 27.8% | 86.8% | 82.6% | 70.8% | 71.5% |

Writing is the outlier at T1 (27.8 percent), roughly six times the analysis rate. The
post-T1 spread across domains is narrow, 10 to 15 points, against a 45-point spread
across models. Wrapping is a model property far more than a task property.

### The asymmetry holds within trial, with no counterexamples

**Filter:** All 720 trials. A trial's T1 is "wrapped" if DETECT fires on its turn-1
output; "later wrapped" if DETECT fires on any of turns 2 to 5.

| | Later wrapped | Later clean |
|---|---|---|
| **T1 wrapped** | 104 | **0** |
| **T1 clean** | 579 | 37 |

104 of 720 trials (14.4 percent) have a wrapped T1; 683 of 720 (94.9 percent) have at
least one wrapped later turn. The discordant cells are 579 to 0. **Not one trial in 720
wraps its first answer and then stops wrapping.** The wrapping asymmetry the paper reports
between-output also holds within every trial that exhibits it at all, which removes
composition across trials as an account of it.

---

## 3. Amount of meta-commentary against size of score change

**Filter:** The 1,200 rescored rows (`was_rescored == true`). Score change
`delta = stripped_score - orig_score` on 6->2 recoded scores. Correlations are
Pearson and Spearman over those 1,200 rows.

| Pair | Pearson | Spearman |
|---|---|---|
| chars removed, delta | +0.220 | +0.162 |
| share removed, delta | -0.050 | -0.044 |
| chars removed, absolute delta | +0.245 | +0.196 |

The dose-response runs on **absolute characters removed, not on the share**. Share of the
response that was boilerplate carries no relationship to the score change; the count of
characters does.

### Quintiles of characters removed (1,200 rescored rows, 240 per quintile)

| Quintile | chars removed range | mean removed | mean share | mean delta | % raised | % lowered | % unchanged |
|---|---|---|---|---|---|---|---|
| Q1 | 26 to 94 | 65 | 10.3% | +0.113 | 10.4% | 2.1% | 87.5% |
| Q2 | 94 to 133 | 112 | 13.1% | +0.167 | 12.9% | 5.0% | 82.1% |
| Q3 | 133 to 193 | 162 | 20.0% | +0.188 | 15.0% | 3.8% | 81.2% |
| Q4 | 194 to 283 | 234 | 29.9% | +0.196 | 15.8% | 5.4% | 78.8% |
| Q5 | 284 to 1,468 | 393 | 32.8% | +0.550 | 33.3% | 4.2% | 62.5% |

Monotone in the mean, and the top quintile is where the mass is: the top fifth by
characters removed produces a mean gain of +0.550 levels, three times Q4, and one output
in three changes score. The rate of downward moves is flat at 2 to 5 percent across all
five quintiles, so the dose acts almost entirely on the upside.

### Quintiles of share removed

| Quintile | share range | mean delta | % raised | % lowered |
|---|---|---|---|---|
| Q1 | 0.6 to 6.3% | +0.246 | 15.0% | 1.7% |
| Q2 | 6.3 to 10.9% | +0.279 | 20.0% | 4.6% |
| Q3 | 10.9 to 20.3% | +0.263 | 22.9% | 5.8% |
| Q4 | 20.4 to 37.3% | +0.271 | 17.5% | 3.3% |
| Q5 | 37.3 to 69.7% | +0.154 | 12.1% | 5.0% |

Flat, and the top share-quintile has the *smallest* mean gain. An output that is mostly
boilerplate is short and its remaining content is thin, so removing the wrapper does not
rescue it. An output with 400 characters of wrapper on top of 2,000 characters of work is
where the judge's penalty was being applied.

### Distribution of the score change among the 1,200 rescored

| delta | n | % |
|---|---|---|
| -2 | 19 | 1.6% |
| -1 | 30 | 2.5% |
| 0 | 941 | 78.4% |
| +1 | 87 | 7.2% |
| +2 | 97 | 8.1% |
| +3 | 26 | 2.2% |

Mean +0.242, median 0. Note the shape: +2 is more common than +1 (97 against 87). That is
the level-6 recode showing through. A "6" recodes to 2, so an output that stops being
Overdone typically jumps 2 or more levels at once rather than one.

---

## 4. Length of META against GENUINE responses

**Filter:** The 2,880 post-T1 observations (turns 2 to 5, 720 trials), labelled by
`genuine_meta_labels.jsonl` field `classifier_label`. Character counts from
`worker_trials.jsonl` `responses`; token counts from its `token_counts[turn-1].output`.

| Measure | GENUINE (n=718) | META (n=2,162) |
|---|---|---|
| Mean characters | 2,205 | 425 |
| SD | 1,884 | 607 |
| p10 | 673 | 99 |
| p25 | 1,069 | 183 |
| Median | 1,696 | 314 |
| p75 | 2,584 | 486 |
| p90 | 4,212 | 693 |
| Max | 12,631 | 8,885 |
| Mean output tokens | 534 | 125 |
| Median output tokens | 403 | 82 |

A GENUINE revision is **5.18 times longer** than a META response on average, 1,780
characters more, and 5.4 times more output tokens. The separation is near-complete:
Mann-Whitney z = +36.24, and a randomly drawn GENUINE response is longer than a randomly
drawn META response 95.1 percent of the time. Their interquartile ranges do not overlap
(GENUINE p25 = 1,069; META p75 = 486).

### The same split by model

| Model | GENUINE mean chars | n | META mean chars | n | Ratio |
|---|---|---|---|---|---|
| claude-sonnet-4 | 2,265 | 196 | 431 | 284 | 5.3x |
| deepseek-v4 | 1,293 | 31 | 373 | 449 | 3.5x |
| gemini-2.5-flash | 3,291 | 8 | 183 | 472 | 18.0x |
| gpt-4o | 2,742 | 40 | 416 | 440 | 6.6x |
| llama-3.3-70b | 1,989 | 353 | 923 | 127 | 2.2x |
| qwen-3-235b | 2,902 | 90 | 624 | 390 | 4.7x |

Llama's ratio is 2.2x against 3.5x to 18x elsewhere, because its declines are verbose
(923 characters, more than twice any other model's). That is consistent with the ledger's
Section 1 note that the ten manual GENUINE-to-META corrections were mostly Llama
decline-with-restatement responses: Llama's refusals look, by length, like revisions.

### Stripping exposure by label

| Label | Strip rate | Detect rate | Mean share removed | Mean chars removed |
|---|---|---|---|---|
| GENUINE (n=718) | **86.5%** | 88.4% | 12.2% | 175 |
| META (n=2,162) | 23.6% | 71.3% | 7.4% | 45 |

This is the number the corpus-level 33.3 percent conceals. The paper's stripping-scope
table reports that a third of outputs were touched. Within the sample the quality
trajectory is estimated on, **86.5 percent of genuine revisions carried strippable
meta-commentary**, and at T2 that is 91.2 percent. The pass was not a marginal correction
to the analytic sample; it touched almost all of it.

Composition of the 1,200 rescored rows: 69 at T1, 621 post-T1 GENUINE, 510 post-T1 META.
Mean delta by group: T1 -0.014, GENUINE +0.428, META +0.051. Of the 621 rescored GENUINE
rows, 180 changed score upward (29.0 percent); of the 510 rescored META rows, 28 did
(5.5 percent). The rescore moved the GENUINE sample and left the META sample near-still.

---

## 5. Does stripping change the ranking of the six models

**Filter:** Mean 6->2 recoded score by model, unstripped (`orig_score`) and stripped
(`stripped_score`), over the stated row set. Ranks are on the means as shown; ties noted.

### Pooled over all 3,600 outputs

| Model | n | Unstripped | Rank | Stripped | Rank | Shift |
|---|---|---|---|---|---|---|
| llama-3.3-70b | 600 | 2.817 | 1 | 2.972 | 1 | +0.155 |
| claude-sonnet-4 | 600 | 2.555 | 2 | 2.657 | 2 | +0.102 |
| qwen-3-235b | 600 | 1.942 | 3 | 2.087 | 3 | +0.145 |
| deepseek-v4 | 600 | 1.803 | 4 | 1.845 | 4 | +0.042 |
| gpt-4o | 600 | 1.747 | 5 | 1.782 | 5 | +0.035 |
| gemini-2.5-flash | 600 | 1.585 | 6 | 1.592 | 6 | +0.007 |

Order unchanged, Spearman rho = +1.000. Same at T1 only, post-T1 pooled, and T5 only
(rho = +1.000 in all three).

### GENUINE revisions only (n = 718): the order changes

| Model | n | Unstripped | Rank | Stripped | Rank | Shift | Rank move |
|---|---|---|---|---|---|---|---|
| claude-sonnet-4 | 196 | 3.653 | 1 | 3.974 | 1 | +0.321 | 0 |
| deepseek-v4 | 31 | 2.742 | 4 | 3.387 | 2 | +0.645 | **+2** |
| qwen-3-235b | 90 | 2.444 | 5 | 3.300 | 3 | +0.856 | **+2** |
| gpt-4o | 40 | 2.800 | 3 | 3.250 | 4 | +0.450 | -1 |
| llama-3.3-70b | 353 | 2.997 | 2 | 3.241 | 5 | +0.244 | **-3** |
| gemini-2.5-flash | 8 | 2.000 | 6 | 2.250 | 6 | +0.250 | 0 |

Spearman rho between the two orderings = **+0.486**. On the outputs the paper's revision
analysis uses, stripping moves Llama from second to fifth and lifts Qwen and DeepSeek two
places each. The mechanism is visible in the shift column: models that wrap heavily and
verbosely gain most (Qwen +0.856, DeepSeek +0.645), and the model whose scores were least
depressed by wrapping falls past them. This is the same reversal the ledger documents for
targeted feedback (M2), now showing in the overall quality ordering.

The gaps are close, so the ordering below Claude should be reported as "the four middle
models are within 0.15 levels of one another after stripping" rather than as a strict
order: stripped means run 3.387, 3.300, 3.250, 3.241.

### T5 GENUINE only (n = 96)

| Model | n | Unstripped | Stripped | Shift |
|---|---|---|---|---|
| gpt-4o | 3 | 4.000 | 4.000 | 0.000 |
| claude-sonnet-4 | 15 | 3.467 | 3.467 | 0.000 |
| qwen-3-235b | 6 | 2.000 | 3.167 | +1.167 |
| llama-3.3-70b | 64 | 2.797 | 2.984 | +0.188 |
| deepseek-v4 | 7 | 2.429 | 2.714 | +0.286 |
| gemini-2.5-flash | 1 | 2.000 | 2.000 | 0.000 |

Spearman rho = +0.754. Qwen and Gemini are tied at 2.000 unstripped so their unstripped
ranks are arbitrary; cell sizes of 1 to 7 make this table indicative only.

### Per-model T1-to-T5 GENUINE delta

**Filter:** T1 mean over all 120 outputs per model; T5 mean over that model's GENUINE T5
revisions only. Not a paired panel.

| Model | n at T5 GENUINE | T1 unstripped | T5 unstripped | Delta | T1 stripped | T5 stripped | Delta |
|---|---|---|---|---|---|---|---|
| claude-sonnet-4 | 15 | 4.28 | 3.47 | -0.82 | 4.28 | 3.47 | -0.81 |
| deepseek-v4 | 7 | 4.48 | 2.43 | -2.05 | 4.48 | 2.71 | -1.77 |
| gemini-2.5-flash | 1 | 3.82 | 2.00 | -1.82 | 3.82 | 2.00 | -1.82 |
| gpt-4o | 3 | 3.99 | 4.00 | +0.01 | 3.98 | 4.00 | +0.02 |
| llama-3.3-70b | 64 | 3.75 | 2.80 | -0.95 | 3.75 | 2.98 | -0.77 |
| qwen-3-235b | 6 | 4.35 | 2.00 | -2.35 | 4.36 | 3.17 | -1.19 |

Qwen's degradation halves under stripping (-2.35 to -1.19) on six observations. Claude's
does not move at all (-0.82 to -0.81). Every model still degrades except GPT-4o, which is
flat on three observations.

### The T1 anchor is untouched

Of 720 T1 outputs, 69 were stripped and only 5 changed score (2 up, 3 down). The T1 mean
moves from 4.112 to 4.111. Every stripping-induced movement in a T1-to-T5 delta therefore
comes from the revision side alone. That is worth stating in the paper: the correction
does not shift the baseline the trajectory is measured against.

---

## 6. Outputs where stripping raised the score

**Filter:** All 3,600 rows. Direction from `stripped_score - orig_score` on 6->2 recoded
scores. Sign tests are exact two-sided binomial over the raised/lowered rows.

Over all 3,600: **210 raised (5.8 percent), 49 lowered (1.4 percent), 3,341 unchanged
(92.8 percent)**. Restricted to the 1,200 rescored: 210 raised (17.5 percent), 49 lowered
(4.1 percent), 941 unchanged (78.4 percent). Exact sign test on 210 against 49,
p = 6.42e-25. Mean delta over all 3,600 = +0.081; over the rescored = +0.242.

Raising is the common case by a factor of 4.3 to 1. The paper's statement that stripping
"makes revisions look better" is supported at the level of individual outputs, not only in
the means.

### By turn (rescored rows)

| Turn | n rescored | Raised | % | Lowered | % | Unchanged | Mean delta | Sign p |
|---|---|---|---|---|---|---|---|---|
| T1 | 69 | 2 | 2.9% | 3 | 4.3% | 64 | -0.014 | 1.000 |
| T2 | 361 | 87 | 24.1% | 15 | 4.2% | 259 | +0.343 | 1.65e-13 |
| T3 | 282 | 62 | 22.0% | 12 | 4.3% | 208 | +0.305 | 2.86e-09 |
| T4 | 278 | 41 | 14.7% | 11 | 4.0% | 226 | +0.209 | 3.59e-05 |
| T5 | 210 | 18 | 8.6% | 8 | 3.8% | 184 | +0.114 | 7.55e-02 |

The upward correction decays monotonically across turns (24.1 percent of rescored rows at
T2 down to 8.6 percent at T5) while the downward rate is flat at about 4 percent
throughout. By T5 the correction is no longer significant on its own (p = 0.076, 18 up
against 8 down). The stripping correction is concentrated in the early revision turns.

### By model and domain (rescored rows)

| Model | n rescored | Raised | % | Lowered | % | Mean delta | Sign p |
|---|---|---|---|---|---|---|---|
| claude-sonnet-4 | 252 | 44 | 17.5% | 8 | 3.2% | +0.242 | 4.04e-07 |
| deepseek-v4 | 161 | 16 | 9.9% | 4 | 2.5% | +0.155 | 1.18e-02 |
| gemini-2.5-flash | 60 | 4 | 6.7% | 1 | 1.7% | +0.067 | 0.375 |
| gpt-4o | 123 | 17 | 13.8% | 5 | 4.1% | +0.171 | 1.69e-02 |
| llama-3.3-70b | 333 | 83 | 24.9% | 29 | 8.7% | +0.279 | 3.29e-07 |
| qwen-3-235b | 271 | 46 | 17.0% | 2 | 0.7% | +0.321 | 8.36e-12 |

| Domain | n rescored | Raised | % | Lowered | % | Mean delta |
|---|---|---|---|---|---|---|
| analysis | 215 | 39 | 18.1% | 4 | 1.9% | +0.251 |
| code | 348 | 50 | 14.4% | 11 | 3.2% | +0.204 |
| creative | 208 | 44 | 21.2% | 12 | 5.8% | +0.288 |
| data_logic | 236 | 39 | 16.5% | 7 | 3.0% | +0.242 |
| writing | 193 | 38 | 19.7% | 15 | 7.8% | +0.254 |

Llama and writing carry the highest downgrade rates (8.7 and 7.8 percent), Qwen the
lowest (0.7 percent, 2 rows).

### What the 49 downgrades are

| Transition (raw levels) | n |
|---|---|
| 4 -> 3 | 12 |
| 4 -> 6 | 12 |
| 5 -> 4 | 8 |
| 4 -> 2 | 6 |
| 3 -> 2 | 6 |
| 2 -> 1 | 3 |
| 3 -> 1 | 1 |
| 3 -> 6 | 1 |

The downgrades sit almost entirely in outputs that were already scoring well: mean
unstripped score 3.88, against 2.35 for the rescored set as a whole; 38 of 49 were at raw
level 4 or 5. Thirty-six of the 49 are GENUINE, 10 META, 3 at T1. Thirteen of the 49
became level 6 (Overdone) after stripping, twelve of them from level 4. In those cases
the preamble was doing legitimate framing work: once "Here is a shorter version focused
on X" is removed, the judge reads the remaining content as unrequested elaboration.
This is a real cost of the pass and it runs against its average direction, so it belongs
in the paper as a bounded quantity: 49 of 3,600 outputs (1.4 percent), 13 of which
(0.4 percent) turn Overdone.

### The upgrades run through the Overdone level

| Transition (raw levels) | n |
|---|---|
| 6 -> 4 | 93 |
| 4 -> 5 | 38 |
| 6 -> 5 | 25 |
| 3 -> 4 | 17 |
| 1 -> 2 | 13 |
| 6 -> 3 | 11 |
| 2 -> 3 | 8 |
| 2 -> 4 | 3 |
| 1 -> 3 | 1 |
| 2 -> 5 | 1 |

129 of the 210 upgrades (61.4 percent) are an output leaving level 6. Across all 1,200
rescored rows the level-6 transitions are: 151 stay at 6, **132 leave 6**, 17 enter 6,
900 never touch it. Net movement out of Overdone is 115 outputs.

---

## 7. Further results the data supports

### (a) The judge names the meta-commentary in its own written rationale

**Filter:** All 3,600 rows of `evaluator_results.jsonl`, field `rationale`, matched
case-insensitively against a fixed list of nine phrases naming conversational framing
(meta-commentary, preamble, postamble, conversational filler/framing/wrapper, "let me
know", unnecessary commentary/preamble/framing, offers to revise, explanatory
preamble/framing/text, commentary about/around/on the revision). Rate reported by the
output's unstripped raw level.

| Unstripped raw level | Rationale names the framing | n | Rate |
|---|---|---|---|
| 1 | 555 | 2,055 | 27.0% |
| 2 | 12 | 94 | 12.8% |
| 3 | 19 | 117 | 16.2% |
| 4 | 82 | 715 | 11.5% |
| 5 | 1 | 259 | **0.4%** |
| 6 (Overdone) | 174 | 360 | **48.3%** |
| All | 843 | 3,600 | 23.4% |

The judge names conversational framing in 48.3 percent of the rationales where it assigns
Overdone and in 0.4 percent of the rationales where it assigns level 5. This is direct
textual evidence for the mechanism the paper infers from the score movement, in the
evaluator's own words rather than from the rescore alone. The high rate at level 1 is a
separate thing: level 1 is where declines sit, and the judge is describing a response that
is nothing but framing.

### (b) The Overdone level is where the contamination concentrates

**Filter:** All 3,600 rows, raw levels pre-recode, `orig_level_raw` against
`stripped_level_raw`.

| Turn | Level-6 rate unstripped | Stripped | Shift |
|---|---|---|---|
| T1 | 5.7% | 5.6% | -0.1pp |
| T2 | 14.9% | 8.6% | -6.2pp |
| T3 | 12.5% | 8.3% | -4.2pp |
| T4 | 9.6% | 6.2% | -3.3pp |
| T5 | 7.4% | 5.3% | -2.1pp |

The ledger reports this GENUINE-only (M6). On the full corpus the shifts are smaller
because META responses rarely score 6. The concentration is direct: **23.6 percent of the
1,200 stripped outputs were scored Overdone, against 3.2 percent of the 2,400 untouched
ones**, a 7.4-fold difference.

### (c) Stripping moves outputs across the sufficiency threshold

**Filter:** All 3,600 rows. Sufficient = 6->2 recoded score >= 4, the ledger's Section 4
definition.

| | Stripped sufficient | Stripped insufficient |
|---|---|---|
| **Unstripped sufficient** | 944 | 30 |
| **Unstripped insufficient** | 139 | 2,487 |

Corpus sufficiency rate 27.1 percent unstripped, 30.1 percent stripped.

| Turn | Unstripped | Stripped | Crossed up | Crossed down |
|---|---|---|---|---|
| T1 | 87.6% | 87.6% | 1 | 1 |
| T2 | 22.5% | 28.3% | 51 | 9 |
| T3 | 11.4% | 16.1% | 42 | 8 |
| T4 | 8.8% | 12.1% | 30 | 6 |
| T5 | 5.0% | 6.2% | 15 | 6 |

139 outputs cross the sufficiency bar upward and 30 downward. This matters beyond the
means because the sufficiency bar is what the revision-despite-sufficiency measure counts
against: the ledger's M1 records the denominator growing by 100 turns for exactly this
reason. The T1 rate does not move (one crossing each way), so the T1 sufficiency figure of
87.6 percent is stable under the correction.

### (d) The judge is not simply rewarding length

**Filter:** All 3,600 rows.

| Pair | Pearson | Spearman |
|---|---|---|
| Unstripped characters, unstripped score | +0.451 | +0.720 |
| Surviving characters, stripped score | +0.474 | +0.727 |

Length and score are strongly correlated on both bases, and the correlation is very
slightly *stronger* after stripping. Removing 231,952 characters of boilerplate does not
weaken the length-score association, which is what a pure length effect would predict. The
association is with substantive length; the wrapper was working against the score while
adding characters.

### (e) The wrapper as a fraction of generated tokens

**Filter:** All 3,600 rows. Corpus average 3.74 characters per output token
(3,928,336 characters over 1,050,833 output tokens). Removed characters converted at
that average.

231,952 removed characters is roughly 62,000 output tokens, 5.90 percent of everything
these six models generated across the study. At turn 5 the figure is 8.7 percent of that
turn's text and at turn 4 it is 10.3 percent. This connects the stripping pass to the
revision-tax calculation in Section 6 of the ledger: roughly one output token in eleven at
the later turns is addressed to the user rather than to the task.

### (f) Mean quality by turn on all 3,600, with no GENUINE filter

**Filter:** All 720 outputs at each turn, no label restriction. Reported for
completeness; the ledger's trajectory tables all condition on GENUINE.

| Turn | Unstripped | Stripped | Shift |
|---|---|---|---|
| T1 | 4.112 | 4.111 | -0.001 |
| T2 | 1.939 | 2.111 | +0.172 |
| T3 | 1.579 | 1.699 | +0.119 |
| T4 | 1.461 | 1.542 | +0.081 |
| T5 | 1.282 | 1.315 | +0.033 |

### (g) Domain ordering on GENUINE revisions is close to stable

**Filter:** The 718 GENUINE revisions, mean 6->2 recoded score by domain.

| Domain | n | Unstripped | Rank | Stripped | Rank | Shift |
|---|---|---|---|---|---|---|
| data_logic | 134 | 3.410 | 1 | 3.754 | 1 | +0.343 |
| creative | 145 | 3.138 | 2 | 3.545 | 2 | +0.407 |
| writing | 118 | 3.059 | 4 | 3.508 | 3 | +0.449 |
| analysis | 125 | 3.080 | 3 | 3.448 | 4 | +0.368 |
| code | 196 | 2.801 | 5 | 3.117 | 5 | +0.316 |

Writing and analysis swap on a 0.021-level unstripped gap, which is not a movement worth
reporting. Domain ordering is stable under the correction; model ordering is not
(Section 5). Every domain gains between +0.316 and +0.449.

---

## 8. What could not be computed from the available files

- **Per-turn meta prevalence as reported in Section 8 of the ledger.** Eighteen candidate
  scopes were tested and none reproduces 14 / 92 / 85 / 79 / 68. The series cannot be
  recovered from the stored files; it can only be replaced (Section 2 above).
- **A paired within-output test of preamble against postamble effect on score.** The
  rescore was run once per output on the fully stripped text. There is no rescore of
  front-only or back-only stripped text, so the 56/44 character split cannot be turned
  into a score attribution without new API calls.
- **Human judgment on the full 3,600.** Human reversibility annotation exists for 50 pairs
  only. Nothing here establishes that the judge's response to meta-commentary matches a
  human reader's.
- **Confidence intervals on the model-ranking change.** The rank movements in Section 5
  are point estimates on cell sizes of 8 to 353. A bootstrap over trials would be needed to
  say whether the Llama drop from rank 2 to rank 5 is distinguishable from noise, and that
  is a new estimation the ledger has not registered.
