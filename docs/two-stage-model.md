# Two-Stage Revision Decision Model

## Overview

We propose a two-stage model of LLM revision behavior in which the decision to revise and the calibration of that revision are governed by independent mechanisms operating on different input signals.

---

## Stage 1: The Revision Gate

**Input:** Pragmatic force of the follow-up prompt
**Output:** Binary decision — revise or decline
**Threshold sensitivity:** None

The first stage is a binary gate that determines whether the model will revise its output at all. This gate is controlled entirely by the conversational pragmatics of the follow-up prompt. A prompt that implies revision is expected ("Can this be improved?") triggers near-universal revision (99.9% across 1,920 trials). A prompt that invites evaluation without directing action ("Take another look at this and let me know if it's ready") produces revision rates between 0.3% and 38.0% depending on model.

Critically, the user's stated quality threshold has **zero measurable effect** on the revision gate. Whether the user asked for a 70 or a 100, the model's decision to revise or decline is statistically indistinguishable across all threshold levels (logistic regression: threshold coefficient not significant, p > 0.40 for all models).

### Evidence

- Leading probe: 99.9% revision rate across all models, all thresholds, all scenarios
- Evaluative probe: 0.3%–38.0% revision rate (model-dependent)
- Chi-squared tests: revision gate distribution differs by probe type (p < 0.0001 for all models)
- Quality threshold: no significant effect on gate (Kruskal-Wallis p > 0.40)

---

## Stage 2: Revision Intensity Calibration

**Input:** User's stated quality threshold
**Output:** Degree of overcorrection (1–5 scale)
**Probe sensitivity:** None (operates only within already-triggered revisions)

The second stage governs how aggressively the model revises once the revision gate has fired. Within the leading-probe condition (where revision is universal), higher stated thresholds are associated with lower overcorrection scores, producing a negative dose-response relationship.

This effect varies substantially across models:

| Model | Spearman ρ | Interpretation |
|-------|-----------|----------------|
| Gemini 2.5 Flash | −0.50 | Moderate threshold sensitivity |
| Claude Sonnet 4 | −0.35 | Weak-to-moderate threshold sensitivity |
| GPT-4o | −0.14 | Weak threshold sensitivity |

The ordinal regression (Model C, leading-probe only) confirms this: threshold is a significant predictor of overcorrection (β = −1.65, p < 0.001) after controlling for framing, model, and scenario.

### Evidence

- Spearman correlations: all negative, all significant (p < 0.001 for Gemini and Claude; p < 0.001 for GPT-4o)
- Kruskal-Wallis H: significant threshold effect for Claude (p < 0.02) and Gemini (p < 0.002); not significant for GPT-4o (p > 0.67)
- Ordinal regression Model C: threshold β = −1.65 (p < 0.001)

---

## The Independence of the Two Stages

The two stages operate on different input signals and do not interact:

1. **Stage 1 is insensitive to thresholds.** The revision gate fires at the same rate whether the user says "70" or "100."
2. **Stage 2 is insensitive to probe framing.** Within triggered revisions, the degree of overcorrection is modulated by the threshold, not by which probe triggered the revision.
3. **The interaction term (probe × threshold) is not significant** in ordinal regression, confirming that these are independent mechanisms.

---

## Why This Matters

The two-stage model reveals a specific alignment failure: models possess the ability to calibrate revision behavior to user preferences (Stage 2 proves this), but this ability is gated behind a decision mechanism (Stage 1) that ignores those same preferences. The practical consequence is that users who state quality thresholds and then ask casual follow-up questions receive revisions that are insensitive to their stated standards — not because the model lacks calibration ability, but because it never reaches the calibration stage.

This has direct implications for interface design: any system that exposes user-stated quality preferences must also ensure that the downstream revision trigger does not override those preferences through conversational pragmatics.

---

## Relationship to Existing Work

The two-stage model parallels findings in instruction-following research showing that LLMs are highly sensitive to surface-level features of instructions (phrasing, formatting, position) while being less sensitive to the semantic content of constraints. Our contribution is demonstrating that this sensitivity hierarchy operates at two distinct and independent decision points — the gate and the calibration — rather than as a single unified process.
