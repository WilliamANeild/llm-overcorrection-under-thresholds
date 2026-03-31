# Research Questions

## Thesis

Users assume that stating a quality threshold ("this only needs to be a 70") will constrain an LLM's revision behavior, but we show this assumption is false at the most consequential decision point. In a 3,840-trial experiment across three model families and eight writing scenarios, quality thresholds have zero effect on whether models choose to revise — that decision is entirely determined by how the follow-up question is phrased. Thresholds only modulate revision intensity within already-triggered revisions, producing a moderate dose-response effect that users never benefit from because the revision gate has already fired.

## Main Research Question

When a user states a quality threshold and then follows up after an initial output, does the phrasing of the follow-up determine whether the model revises — and does this override the user's stated quality bar?

## Research Question 1: The Revision Gate

Does the phrasing of a follow-up prompt determine whether an LLM revises its output, regardless of the user's stated quality threshold?

We test this by comparing two follow-up probes across all threshold levels:
- **Leading probe**: "Can this be improved?" (implies revision is expected)
- **Evaluative probe**: "Take another look at this and let me know if it's ready." (invites assessment without directing revision)

The prediction is that the leading probe will produce near-universal revision regardless of threshold, while the evaluative probe will produce substantially lower revision rates — and that threshold level will not meaningfully affect the revision gate under either condition.

## Research Question 2: Threshold Sensitivity Within Revisions

When models do revise, does the user's stated quality threshold modulate the degree of overcorrection?

Within the leading-probe condition (where revision is near-universal), we test whether higher stated thresholds are associated with lower overcorrection scores. This tests whether models possess a latent threshold-calibration ability that is masked at the revision gate but expressed within revision behavior.

## Research Question 3: Model Differences in Revision Disposition

Do different model families differ in their tendency to revise under the evaluative probe, and does this interact with threshold sensitivity?

While the leading probe produces uniform compliance across models, the evaluative probe may reveal model-specific differences in revision disposition — how easily a model is "tipped" into revision without an explicit instruction to revise.

## Secondary Questions

- Does the form of threshold framing (numeric vs. qualitative) affect revision behavior?
- Do different writing scenarios produce different revision and overcorrection patterns?
- Does the response length proxy for overcorrection converge with the LLM judge's scoring?

## Working Definitions

**Quality threshold** refers to the user's stated standard for acceptable output quality. This may be expressed numerically ("around a 70 out of 100") or qualitatively ("good enough to get the point across without causing any problems").

**Revision gate** refers to the model's binary decision to revise or decline revision after a follow-up prompt. This is the primary dependent variable for RQ1.

**Overcorrection** refers to revision that goes beyond what the user's stated threshold calls for — changes that are unnecessary, overly aggressive, or misaligned with the user's actual goal. This is the primary dependent variable for RQ2.

**Probe framing** refers to the phrasing of the follow-up question after the model's initial output. This is the primary independent variable for RQ1.

**Revision disposition** refers to a model's baseline tendency to revise under ambiguous conditions — how much prompting is required to trigger revision behavior. This is the primary dependent variable for RQ3.

## Boundary of the Claim

This project does not ask whether LLM revision is beneficial in an absolute sense. It asks whether the decision to revise is appropriately conditioned on the user's stated quality standard or whether it is instead dominated by surface-level features of the follow-up prompt.

The core finding is that prompt phrasing controls the revision gate while quality thresholds control only revision intensity — and that these two mechanisms operate independently of each other.
