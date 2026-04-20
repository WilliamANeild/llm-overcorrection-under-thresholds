# Study 2: Revision Momentum Experiment

## Motivation

Study 1 established a two-stage model of LLM revision behavior: probe phrasing controls the revision gate (Stage 1) while quality thresholds only modulate revision intensity (Stage 2). However, Study 1 tested the gate "cold" -- the model had no prior revision history. In real-world usage, people go back and forth with LLMs across multiple turns. This study tests whether revision history creates momentum that shifts the gate on subsequent turns.

## Core Question

Does a prior revision in the conversation create momentum that shifts the revision gate? If a model has already revised once (or multiple times) under a leading probe, does it continue revising even when the follow-up switches to an evaluative probe?

## Conditions

| Condition | Conversation Structure | Data Source |
|-----------|----------------------|-------------|
| Cold (dose=0) | Task+threshold -> Evaluative probe | Study 1 (pilot_c) |
| Warm dose=1 | Task+threshold -> Leading -> Evaluative | New |
| Warm dose=2 | Task+threshold -> Leading -> Leading -> Evaluative | New |
| Warm dose=3 | Task+threshold -> Leading x3 -> Evaluative | New |

- Leading probe: "Can this be improved?"
- Evaluative probe: "Take another look at this and let me know if it's ready."

## Factor Matrix

- Momentum dose: 1, 2, 3
- Model: GPT-4o, Claude Sonnet 4, Gemini 2.5 Flash
- Threshold: 0, 75, 90, 100 (reduced from 8 levels)
- Framing: numeric, qualitative
- Scenario: all 8 scenarios
- Runs: 3 per cell

**Total new trials**: 3 x 3 x 4 x 2 x 8 x 3 = 1,728

## Research Questions

- **RQ4 (Momentum Gate Shift)**: Does prior revision history increase the revision rate under the evaluative probe, compared to cold baseline?
- **RQ5 (Dose-Response)**: Does revision rate under the evaluative probe increase with the number of prior leading-probe revisions?
- **RQ6 (Threshold x Momentum)**: Does the stated quality threshold modulate momentum?

## Primary DVs

- Revision gate at the evaluative turn (decline / suggest_minor / full_revision)
- Overcorrection at the evaluative turn
- Cumulative quality trajectory across turns

## Statistical Analyses

- Chi-squared: gate distribution at evaluative turn, dose=0 vs dose=1/2/3
- Logistic regression: revised ~ dose + threshold + model + (1|scenario)
- Spearman: dose vs revision rate
- Kruskal-Wallis: overcorrection across doses
- Interaction tests: dose x threshold, dose x model

## Pipeline

1. `scripts/generate_momentum_matrix.py` -- generate prompt matrix
2. `scripts/run_momentum_experiment.py --model <name>` -- run multi-turn conversations
3. `scripts/evaluate_momentum.py` -- score final evaluative turn with LLM judge
4. `scripts/analyze_momentum.py` -- run statistical analyses
5. `scripts/visualize_momentum.py` -- generate figures
