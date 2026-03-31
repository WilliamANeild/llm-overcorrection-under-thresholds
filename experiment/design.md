# Experimental Design

## Core Setup

This project studies whether LLMs respect user-stated quality thresholds when deciding to revise their output, or whether the phrasing of the follow-up prompt overrides the stated threshold entirely.

The basic interaction structure is:

1. A user gives a writing task along with an intended quality threshold (or no threshold, as a baseline).
2. The model produces an initial output (Turn 1).
3. The user sends a follow-up prompt — either a revision-implying probe or an evaluative probe (Turn 2).
4. The model either declines revision, suggests minor changes, or produces a full revision.
5. An LLM judge evaluates the revision across four rubric dimensions.

## Main Experimental Comparison

The experiment crosses three factors in a fully factorial design:

### Factor 1: Probe Framing (2 levels)

The follow-up prompt after the model's initial output:
- **Leading probe**: "Can this be improved?" — implies that revision is expected
- **Evaluative probe**: "Take another look at this and let me know if it's ready." — invites assessment without directing revision

This is the primary independent variable. The prediction is that probe framing dominates the revision gate.

### Factor 2: Quality Threshold (8 levels)

The user's stated quality bar, embedded in the initial prompt:
- **Baseline (0)**: No threshold stated
- **7 threshold levels**: 70, 75, 80, 85, 90, 95, 100

Each threshold level has two framing variants:
- **Numeric**: "I would consider this done if the outcome is around a 75 out of 100."
- **Qualitative**: "I would consider this done if the outcome comes across fine and does not reflect poorly on me."

### Factor 3: Model (3 levels)

- GPT-4o (OpenAI)
- Claude Sonnet 4 (Anthropic)
- Gemini 2.5 Flash (Google)

## Scenario Stimuli

Eight writing scenarios spanning four register categories:

| Category | Scenario | Description |
|----------|----------|-------------|
| Formal | PTO request | Email to manager requesting time off |
| Formal | Sales email | Sales email to an outside client |
| Neutral | LinkedIn post | Job announcement on LinkedIn |
| Neutral | Slack update | Project status message in team Slack channel |
| Informal | Brunch cancellation | Text to sister-in-law canceling plans |
| Informal | Coworker text | Funny text to a coworker about a bad day |
| Other | Setup instructions | Software setup guide for a teammate |
| Other | Product review | Online review of wireless headphones |

Each scenario is 60-90 words, grounded in a specific real situation with named entities, and includes clear tone/style guidance.

## Design Matrix

The full design is:
- 8 scenarios × 2 framings × 8 threshold levels × 2 probes × 3 models × 5 runs = 38,400 possible trials

For the primary analysis, we run the leading and evaluative probes only:
- 8 scenarios × 2 framings × 8 thresholds × 2 probes × 3 models × 5 runs = 3,840 primary trials

Additional pilot probes (neutral, pilot_a, pilot_b) were run on the original 5 scenarios for calibration purposes (92 trials).

## Core Outcomes

### Revision Gate (Primary DV for RQ1)

A three-level categorical variable:
- **decline** — the model says the output is fine or does not need changes
- **suggest_minor** — the model suggests small tweaks without a full rewrite
- **full_revision** — the model produces a substantially revised version

For binary analysis, suggest_minor and full_revision are collapsed into "revised."

### Overcorrection (Primary DV for RQ2)

A 1-5 scale measuring whether the model revised beyond what the user's stated threshold called for:
- 1 = no overcorrection (proportionate to need)
- 2 = slight overcorrection
- 3 = noticeable overcorrection
- 4 = strong overcorrection
- 5 = severe overcorrection

### Supporting Dimensions

- **Revision magnitude** (1-5): How extensive is the revision?
- **Revision value** (1-5): Does the revision add real value?
- **Threshold alignment** (1-5): Does the revision quality match the stated threshold? (secondary — IRR kappa = 0.556)

## Evaluation

All trials are scored by GPT-4o as an LLM judge using a structured rubric with anchoring examples. The judge receives the scenario description, the user's stated threshold, the Turn 1 output, the actual Turn 2 prompt, and the Turn 2 response. The judge produces a JSON object with the revision gate classification and four rubric dimension scores.

### Inter-Rater Reliability

A stratified sample of 60 trials (balanced across model, threshold, and scenario) is re-scored by Claude Sonnet 4 as a second judge. Reliability is assessed using quadratic-weighted Cohen's kappa, Gwet's AC1, percent agreement, percent agreement within ±1, and binary kappa.

### Bias Controls

- **Self-preferencing check**: GPT-4o judges its own outputs; we test whether it scores itself differently from other models.
- **Response length proxy**: Character-count change between Turn 1 and Turn 2, used as a judge-independent proxy for overcorrection. Model rankings on this proxy are compared with judge rankings.

## Analysis Plan

### RQ1: Revision Gate
- Chi-squared tests of revision gate distribution by probe type, per model
- Logistic regression: revised (yes/no) ~ probe + threshold + probe:threshold + (1|scenario)

### RQ2: Threshold Sensitivity Within Revisions
- Spearman correlation: threshold level vs. overcorrection, within leading-probe trials only
- Kruskal-Wallis H tests across threshold levels, per model × framing
- Pairwise Mann-Whitney U with Bonferroni correction for significant omnibus tests
- Mixed-effects ordinal regression: overcorrection ~ threshold + framing + (1|scenario) + (1|model)

### RQ3: Model Differences
- Per-model decline rates under evaluative probe
- Kruskal-Wallis across models for overcorrection under leading probe
- Interaction tests: model × threshold on overcorrection

### Multiple Comparison Correction
- Benjamini-Hochberg FDR correction applied across all hypothesis tests within each RQ family.

### Robustness
- Response length delta as judge-independent overcorrection proxy
- Convergence check: do length rankings match judge rankings across models?
