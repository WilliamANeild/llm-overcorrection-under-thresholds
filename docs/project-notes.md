# Project Notes

## Current Project Framing

The project studies whether user-stated quality thresholds actually constrain LLM revision behavior, or whether the phrasing of a follow-up prompt overrides the threshold entirely.

The original hypothesis was that LLMs would overcorrect — revising beyond what users asked for, especially at low stated thresholds. What we found is more specific: the decision to revise at all is controlled entirely by prompt phrasing, not by the quality threshold. Thresholds only modulate revision intensity within already-triggered revisions.

## Core Findings

### Finding 1: Binary Compliance Cliff
A revision-implying follow-up ("Can this be improved?") produces near-100% revision compliance across all three models, all eight scenarios, and all threshold levels. An evaluative follow-up ("Take another look at this and let me know if it's ready") produces 62-100% decline rates depending on model. Quality thresholds have zero effect on this binary decision.

### Finding 2: Latent Threshold Sensitivity (Weak to Moderate)
Within the leading-probe condition (where revision is universal), higher stated thresholds are associated with less overcorrection — but the effect size varies substantially across models:
- Gemini 2.5 Flash: ρ = −0.50 (moderate)
- Claude Sonnet 4: ρ = −0.35 (weak-to-moderate)
- GPT-4o: ρ = −0.14 (weak)

This means models possess some threshold calibration ability, but it ranges from barely detectable (GPT-4o) to moderate (Gemini). Importantly, this calibration only operates within revisions that have already been triggered — it never reaches the revision gate.

### Finding 3: Model-Specific Revision Disposition
All three models behave identically under the leading probe (~100% revision). Under the evaluative probe, they diverge sharply:
- Gemini Flash: 99.7% decline (almost never revises)
- GPT-4o: 68.6% decline
- Claude Sonnet: 62.0% decline

## Theoretical Contribution: Two-Stage Revision Decision Model

We propose a two-stage model (see `docs/two-stage-model.md`) in which the decision to revise and the calibration of that revision are governed by independent mechanisms:

- **Stage 1 (Revision Gate):** Controlled entirely by follow-up prompt phrasing. Thresholds have zero effect.
- **Stage 2 (Revision Intensity):** Modulated by the user's stated threshold. Effect is weak (GPT-4o) to moderate (Gemini).

The two stages are independent: the probe × threshold interaction is not significant in ordinal regression.

## Why This Matters

Users routinely state quality preferences ("this just needs to be a 70") and then follow up with casual questions like "can this be improved?" They assume the threshold constrains the model's behavior. It does not — at least not at the revision gate.

This is a specific alignment failure: models possess the ability to calibrate to user preferences (Stage 2 proves this), but this ability is gated behind a decision mechanism (Stage 1) that ignores those same preferences. The practical consequence is that the calibration ability users would most benefit from is never activated in typical conversational flows.

## Dataset

- **3,932 scored trials** (3,840 primary + 92 pilot)
- 3 models × 8 scenarios × 2 framings × 8 threshold levels × 2 probes × 5 runs
- Scored by GPT-4o judge with structured rubric
- IRR verified with Claude Sonnet as second judge (n=60 stratified sample)
- Response length proxy converges with judge rankings across all 3 models

## Target Venue

ACL or EMNLP. Paper being prepared with support from a research lab at Emory University.
