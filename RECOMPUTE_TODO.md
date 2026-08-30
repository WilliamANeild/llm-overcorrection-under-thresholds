# Recompute: Stripped Cliff p-value and Effect Size

## What is missing

The paper reports a stripped balanced-panel cliff of -0.74 levels (Turn 1 minus Turn 5)
but no p-value or effect size for this stripped cliff exists in results_FINAL.md.
The unstripped cliff (-0.94) has p = 3.32e-06 and r = 0.658 (lines 33-34).

## Test specification

- **Test**: Paired Wilcoxon signed-rank test
- **Sample**: The 50 balanced-panel trials (trials with genuine revision at ALL of turns 2, 3, 4, 5)
- **Paired values**: Stripped Turn 1 score vs. Stripped Turn 5 score (after 6-to-2 recode)
- **Source for stripped scores**: `data/study3/raw_responses/stripped_rescore_full.jsonl` (the full 3,600-output rescore)
- **Source for balanced-panel trial IDs**: trials where `genuine_meta_labels.jsonl` has `classifier_label == "GENUINE"` at all of turns 2, 3, 4, 5
- **Effect size**: r = |Z| / sqrt(N), where Z is the Wilcoxon test statistic and N = 50
- **Also compute for Llama subset**: Same test on the 45 Llama balanced-panel trials

## Output needed

Two values to fill placeholders in the paper:
1. `\pvalstripped` -- the p-value for the stripped cliff (all 50 balanced-panel trials)
2. `\rvalstripped` -- the effect size r for the stripped cliff

Plus the same pair for the Llama-only subset (n=45), which currently shows
`\pvalstripped` in Table 3.

## Placeholder locations in paper

- abstract.tex:2
- results_v2.tex:59 (body text)
- results_v2.tex:68 (Table 3, all-balanced row)
- results_v2.tex:69 (Table 3, Llama row)
- conclusion.tex:3
- appendix.tex:188 (power analysis)

## After recomputing

1. Record the stripped p and r in results_FINAL.md under "Stripped Cliff" (lines 53-67)
2. Replace all `\pvalstripped` and `\rvalstripped` macros in main.tex with the real values
3. Delete the macro definitions from main.tex preamble
4. Delete this file
