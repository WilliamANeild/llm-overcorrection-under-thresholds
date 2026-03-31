# Project Notes

## Current Project Framing

The project studies whether user-stated quality thresholds actually constrain LLM revision behavior, or whether the phrasing of a follow-up prompt overrides the threshold entirely.

The original hypothesis was that LLMs would overcorrect — revising beyond what users asked for, especially at low stated thresholds. What we found is more specific: the decision to revise at all is controlled entirely by prompt phrasing, not by the quality threshold. Thresholds only modulate revision intensity within already-triggered revisions.

## Core Findings

### Finding 1: Binary Compliance Cliff
A revision-implying follow-up ("Can this be improved?") produces near-100% revision compliance across all three models, all eight scenarios, and all threshold levels. An evaluative follow-up ("Take another look at this and let me know if it's ready") produces 62-100% decline rates depending on model. Quality thresholds have zero effect on this binary decision.

### Finding 2: Latent Threshold Sensitivity
Within the leading-probe condition (where revision is universal), higher stated thresholds are associated with less overcorrection. Spearman rho ranges from -0.14 (GPT-4o) to -0.50 (Gemini Flash). This means models CAN calibrate to thresholds — but only within revisions that have already been triggered.

### Finding 3: Model-Specific Revision Disposition
All three models behave identically under the leading probe (~100% revision). Under the evaluative probe, they diverge sharply:
- Gemini Flash: 99.7% decline (almost never revises)
- GPT-4o: 68.6% decline
- Claude Sonnet: 62.0% decline

## Why This Matters

Users routinely state quality preferences ("this just needs to be a 70") and then follow up with casual questions like "can this be improved?" They assume the threshold constrains the model's behavior. It does not — at least not at the revision gate.

This is an alignment issue: the model possesses the ability to calibrate to user preferences (the within-revision dose-response proves this), but the pragmatic force of the follow-up prompt prevents that ability from reaching the decision that matters most — whether to revise at all.

## Dataset

- **3,932 scored trials** (3,840 primary + 92 pilot)
- 3 models × 8 scenarios × 2 framings × 8 threshold levels × 2 probes × 5 runs
- Scored by GPT-4o judge with structured rubric
- IRR verified with Claude Sonnet as second judge (n=60 stratified sample)
- Response length proxy converges with judge rankings across all 3 models

## Target Venue

ACL or EMNLP. Paper being prepared with support from a research lab at Emory University.
