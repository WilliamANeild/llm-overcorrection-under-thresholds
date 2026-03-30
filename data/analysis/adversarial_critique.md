# Adversarial Peer Review: LLM Overcorrection Under User-Stated Quality Thresholds

**Reviewer stance**: Hostile but fair. Reviewing for a top NLP venue (EMNLP/ACL).
**Date**: 2026-03-30

---

## Overall Assessment

The paper investigates an interesting and practically relevant question: whether user-stated quality thresholds modulate LLM overcorrection behavior. The experimental design is ambitious (1,200 trials, 3 models, 5 scenarios, 2 framings, 8 threshold levels). However, I identify serious methodological, statistical, and interpretive concerns that collectively threaten the validity of the central claims. The study suffers from a fundamentally compromised evaluation pipeline (LLM-as-judge with unacceptable reliability on a key dimension), a confounded elicitation protocol, insufficient statistical correction for the number of tests conducted, and overclaiming relative to a narrow stimulus set. Below I enumerate 24 specific concerns, each rated FATAL, MAJOR, or MINOR.

---

## 1. The "Can this be improved?" Prompt Is a Confound, Not a Neutral Probe

**Severity: FATAL**

The Turn 2 prompt -- "Can this be improved?" -- is not a neutral question. It is a pragmatic implicature that presupposes the answer is "yes" and implicitly requests revision. In conversational pragmatics, asking "Can X be improved?" to an instruction-following system that has been RLHF-trained to be maximally helpful is functionally equivalent to saying "Please improve this." The study measures whether models revise when asked to revise, then concludes they are "threshold-insensitive" because they always revise. This is circular. A model that correctly interprets the pragmatic force of the question *should* revise, regardless of stated thresholds. The 0.5% decline rate (6/1,200 trials) is not evidence of sycophancy or overcorrection -- it may simply be evidence that the models understand the question. Without a control condition using a genuinely neutral probe (e.g., "Is this finished?" or "Rate this on a scale of 1-10" or simply "What do you think?"), the study cannot distinguish threshold insensitivity from pragmatic competence.

---

## 2. Threshold Alignment Kappa of 0.08 Invalidates a Core Dimension

**Severity: FATAL**

The inter-rater reliability for threshold_alignment is kappa = 0.08, which falls below the threshold for "slight agreement" (0.00-0.20 on the Landis and Koch scale) and is functionally indistinguishable from chance. This means the two judges (GPT-4o and Claude Sonnet) cannot agree on what "threshold alignment" means when applied to these outputs. Yet threshold_alignment is central to the paper's argument: it is used in the framing-effect analysis (all three models show significant numeric-vs-qualitative differences on this dimension), it is used in the self-preferencing analysis (r = 0.281), and it is invoked in the dose-response analysis. Any finding that depends on threshold_alignment scores is uninterpretable. The authors should either drop this dimension entirely or demonstrate that the construct can be reliably measured before drawing conclusions from it.

---

## 3. Overcorrection Kappa of 0.42 Is Below Standard Thresholds

**Severity: MAJOR**

The overcorrection dimension -- the study's primary dependent variable -- achieves kappa = 0.42, which is "moderate" agreement at best. For the central construct of a study, this is insufficient. Standard practice in NLP evaluation requires kappa >= 0.60 for ordinal annotation tasks (Artstein & Poesio, 2008). The revision_magnitude (0.64) and revision_value (0.70) dimensions meet this bar; overcorrection does not. This means the noise in the primary outcome variable may be large enough to mask real effects, potentially explaining the flat dose-response curves rather than reflecting genuine threshold insensitivity. The authors cannot claim "models are threshold-insensitive" when the measurement instrument for overcorrection has insufficient reliability to detect moderate effects.

---

## 4. Scale Compression Renders the Overcorrection Measure Insensitive

**Severity: MAJOR**

The overcorrection scores cluster overwhelmingly at 1 and 2, with bootstrap 95% CIs of [2.0, 2.0] for the median in all conditions. No observations reach 4 or 5. The effective range of the instrument is 2 points on a 5-point scale. This floor effect means the scale lacks the dynamic range to detect graded dose-response relationships. The study is testing whether thresholds modulate overcorrection using an instrument that cannot discriminate between "no overcorrection" and "slight overcorrection" with any granularity. The flat dose-response curves may reflect measurement insensitivity rather than behavioral insensitivity. The authors acknowledge this in a methodological note but do not adequately grapple with its implications for their central claim.

---

## 5. No Multiple Comparison Correction Across the Full Test Battery

**Severity: MAJOR**

The stats report contains dozens of statistical tests: Mann-Whitney U tests (12), Kruskal-Wallis tests (6+), Spearman correlations (9+), chi-squared tests (4+), bootstrap CIs, pairwise comparisons, and more. The total number of statistical tests exceeds 50. Some pairwise comparisons are Bonferroni-corrected, but there is no family-wise or false discovery rate correction applied across the entire analysis. At alpha = 0.05 with 50+ tests, approximately 2-3 tests will be significant by chance alone. Several of the "significant" findings have p-values between 0.01 and 0.05 (e.g., Gemini Flash revision_value framing effect at p = 0.039; Claude Sonnet threshold_alignment framing effect at p = 0.021; Gemini Flash chi-squared gate at p = 0.047). After appropriate FDR correction, many of these would lose significance.

---

## 6. The Qualitative Thresholds Are Not Equivalent Across Levels

**Severity: MAJOR**

The qualitative threshold descriptions are not calibrated translations of the numeric values. Compare: level 70 = "good enough to get the point across without causing any problems" versus level 95 = "excellent, highly polished, and difficult to improve in any meaningful way." These descriptions vary in multiple pragmatic dimensions simultaneously: implied effort, specificity of quality criteria, and implicit instruction (level 95 essentially tells the model "this is already difficult to improve," which is a direct behavioral cue). The qualitative framing confounds threshold level with pragmatic instruction intensity. Gemini Flash's unique sensitivity to qualitative thresholds may reflect sensitivity to the *phrasing* of individual descriptions rather than sensitivity to a latent quality continuum. Without piloting or manipulation checks on perceived threshold levels, the numeric-qualitative comparison is uninterpretable.

---

## 7. GPT-4o Judging Itself Creates an Irresolvable Confound

**Severity: MAJOR**

GPT-4o serves as both subject (generating 400 trials) and judge (scoring all 1,200 trials). The self-deprecation finding (GPT-4o scores itself lower, r = 0.488 on revision_value) does not resolve the confound -- it deepens it. There are at least three explanations: (a) GPT-4o genuinely produces lower-value revisions, (b) GPT-4o has a stylistic self-recognition bias that triggers different scoring behavior, or (c) GPT-4o's training incentivizes self-criticism to avoid appearing narcissistic. These are not distinguishable with the current design. The convergence of length-based and judge-based model rankings is presented as validation, but length is not a valid proxy for overcorrection -- a model could write long, high-quality revisions or short, harmful ones. The convergence proves only that the rankings agree, not that either ranking is correct.

---

## 8. Five Scenarios Is Insufficient for Generalizability Claims

**Severity: MAJOR**

The study uses five scenarios spanning three formality levels (2 formal, 2 informal, 1 neutral). Scenario is the strongest predictor of overcorrection (H = 314, eta-squared = 0.26), explaining more variance than any experimental manipulation. With only five scenarios, the study cannot distinguish scenario-specific effects from generalizable formality effects. The formal/informal analysis (formal M = 1.96 vs informal M = 1.59, r = -0.36) is confounded with scenario content: are models overcorrecting more on the LinkedIn post because it is formal, or because LinkedIn posts have a well-known template that models want to optimize toward? With n = 2 scenarios per formality bin, this analysis has zero statistical power for the formality factor as a random effect. The authors should not claim that "formality drives overcorrection" based on two scenarios per category.

---

## 9. No Human Evaluation Baseline

**Severity: MAJOR**

The entire evaluation pipeline relies on LLM judges. There is no human evaluation of any kind -- not even a small validation sample to confirm that the judge scores correlate with human judgments of overcorrection. LLM-as-judge is an active area of methodological concern (Zheng et al., 2023; Huang et al., 2024), and the threshold_alignment kappa of 0.08 between two LLM judges suggests these models may not share a coherent concept of what the construct means. Without human ground truth, we cannot assess whether the judge rubric measures what the authors intend, or whether the flat dose-response curves reflect a real behavioral pattern versus a judge artifact.

---

## 10. n = 25 Per Cell Is Underpowered for Detecting Small-to-Medium Effects

**Severity: MAJOR**

Each model x framing x threshold cell contains 25 observations (5 scenarios x 5 runs). For a Mann-Whitney U test comparing two cells of n = 25, the minimum detectable effect size at 80% power and alpha = 0.05 is approximately d = 0.80 (large effect). This means the study is powered to detect only large effects within cells. The observed effect sizes for threshold-level comparisons are mostly r = 0.03-0.10 (small), which are well below the detection threshold. The authors' conclusion that "thresholds have no effect" may be an artifact of being underpowered to detect the effects that exist. A power analysis should have been conducted a priori, and the absence of one is a significant methodological gap.

---

## 11. The Overcorrection-Value Paradox May Be a Measurement Artifact

**Severity: MAJOR**

The "overcorrection-value paradox" (GPT-4o rho = 0.836 between overcorrection and revision_value) is presented as a substantive finding, but it is likely a measurement artifact. The judge rubric asks for both overcorrection and revision_value scores in the same JSON response with a single rationale. These are not independent measurements -- they are simultaneous assessments by the same judge in the same inference call. A judge that perceives a "big revision" will naturally score both dimensions high. This is common method variance, not a paradox. The correlation tells us the judge's scoring dimensions are not orthogonal, which is unsurprising. To test whether this is a genuine behavioral paradox, the overcorrection and value assessments would need to come from independent judge calls or independent judges.

---

## 12. Temperature = 0 for Judge Calls Masks Reliability Issues

**Severity: MINOR**

The judge uses temperature = 0, which produces nearly deterministic outputs. This means the IRR comparison between GPT-4o and Claude Sonnet reflects systematic inter-model disagreement rather than stochastic variation. The kappa values do not capture within-judge reliability (test-retest), which is arguably more relevant. If GPT-4o at temperature = 0 were asked to re-judge the same trials, it would likely achieve kappa near 1.0 with itself, creating an illusion of perfect reliability while the construct validity (kappa = 0.08 on alignment) is abysmal. The authors should report both inter-judge and intra-judge reliability.

---

## 13. The Threshold Level = 0 Baseline Is Ambiguous

**Severity: MAJOR**

At threshold level 0, the threshold text is empty (no threshold stated). This is treated as a baseline, but it is not a clean no-threshold control. The model still receives the scenario text in Turn 1 and "Can this be improved?" in Turn 2. The absence of a threshold is different from the presence of a low threshold. The study conflates "no threshold mentioned" with "zero quality standard," but these are pragmatically distinct: no threshold could mean the user has unstated high standards, while an explicit low threshold (70/100) signals lenience. The transition from level 0 to level 70 is not a clean dose-response step but a category change from "unspecified" to "specified."

---

## 14. No Control for Scenario Difficulty or Initial Output Quality

**Severity: MAJOR**

The study does not measure or control for the quality of the Turn 1 output. If a model produces a poor Turn 1 response for a given scenario, a large Turn 2 revision may be *appropriate*, not overcorrection. The overcorrection construct assumes that Turn 1 outputs are uniformly adequate, but this is not verified. The massive scenario effects (eta-squared = 0.26) could reflect differences in Turn 1 quality rather than differences in overcorrection tendency. For example, the LinkedIn post (highest overcorrection, M = 2.00) may simply elicit worse Turn 1 outputs that genuinely need revision, while the brunch cancellation text (lowest overcorrection, M = 1.34) may elicit adequate Turn 1 outputs.

---

## 15. Only 5 Runs Per Condition -- Insufficient for Variance Estimation

**Severity: MINOR**

With 5 runs per model x scenario x framing x threshold cell, the within-cell variance estimates are based on n = 5 observations on a scale that takes integer values 1-5. The standard error of the mean for a cell with SD = 0.5 and n = 5 is 0.22, which is nearly half the observed between-cell differences. This means many of the cell-level patterns described in the deep analysis (e.g., "inflection point at level 70," "paradoxical spike at level 95") are within the noise margin and should not be interpreted as real patterns.

---

## 16. The "Sycophancy Signature" Composite Is Ad Hoc and Unvalidated

**Severity: MINOR**

The sycophancy signature metric (revision_magnitude x (5 - threshold_alignment)) is presented without theoretical motivation or validation. It multiplies two ordinal variables -- a practice with no clear psychometric justification. The resulting composite inherits the reliability problems of both components (especially threshold_alignment at kappa = 0.08). The significant Kruskal-Wallis result (H = 112.73) on this composite is uninterpretable given the unreliability of one of its components.

---

## 17. Gemini Flash Is a Distractor Model

**Severity: MINOR**

Gemini Flash is the smallest and cheapest model in the comparison (it is a "Flash" variant, not a flagship). Comparing it with GPT-4o and Claude Sonnet (both flagship-tier models) is an apples-to-oranges comparison. The finding that Gemini Flash is the only threshold-sensitive model may reflect its lower capability or different instruction-tuning approach rather than a meaningful architectural insight. The paper should acknowledge that model selection confounds model family with model capability tier, or include models at comparable capability levels.

---

## 18. Threshold Text Wording Varies in More Than Just the Number

**Severity: MINOR**

The numeric threshold texts are not identical across levels beyond the number. Level 100 says "needs to be as close to a 100 out of 100 as possible" while levels 70-95 say "only really needs to be a [X] out of 100." The framing shifts from "only really needs" (low bar) to "needs to be as close as possible" (high aspiration) between level 95 and level 100. This introduces a confound at the top end of the scale, where the linguistic frame changes alongside the number.

---

## 19. No Randomization of Threshold Presentation Order

**Severity: MINOR**

The paper does not describe randomization of trial order or counterbalancing. If trials were run sequentially (all level-0 trials, then all level-70 trials, etc.), API-side changes, rate limiting, or temporal effects could confound the threshold-level comparison. The 5-run replication mitigates this somewhat, but the paper should explicitly state whether trial order was randomized.

---

## 20. "Threshold Insensitivity" Is Too Strong a Claim Given the Evidence

**Severity: MAJOR**

The central claim -- that LLMs are "threshold-insensitive" -- is a null claim, and the study is not designed to confirm nulls. The absence of a significant effect is not evidence of no effect; it may be evidence of insufficient power, measurement error (kappa = 0.42 on the primary DV), or scale compression (scores locked at 1-2). A more honest framing would be: "We failed to detect a dose-response relationship between stated thresholds and judged overcorrection, though our measurement instrument has limited reliability and dynamic range." The current framing conflates "we did not find an effect" with "there is no effect."

---

## 21. Response Length as a "Bias-Free Proxy" Is Not Bias-Free

**Severity: MINOR**

Response length is presented as a "bias-free proxy" for overcorrection, but length is a poor proxy for the construct. A model that adds a disclaimer ("Your text was already great, but here is a slightly different version...") will have a large length delta without overcorrecting. A model that silently replaces a casual phrase with a formal one may overcorrect with near-zero length change (as GPT-4o appears to do, with delta M = +1). The convergence of length and judge rankings proves only that long responses are rated as more overcorrective by this particular judge, which could itself be a judge bias (conflating verbosity with overcorrection).

---

## 22. The IRR Sample Is Only 15% and May Not Be Representative

**Severity: MINOR**

The IRR analysis uses 15% of trials (n = 180). While this is a reasonable fraction, the sampling is based on a single random seed (42). If the sample happens to overrepresent easy-to-judge cases (e.g., high-magnitude revisions where both judges agree easily), the kappa values will be inflated. Conversely, if it overrepresents edge cases, kappas may be deflated. A stratified sample (ensuring representation across models, scenarios, and threshold levels) would be more appropriate for IRR estimation.

---

## 23. No Analysis of Turn 1 Content Variation Across Runs

**Severity: MINOR**

The study runs each condition 5 times, but there is no analysis of whether the Turn 1 outputs vary meaningfully across runs. If a model produces nearly identical Turn 1 outputs for the same scenario (which is likely at low temperature), the 5 "runs" are not truly independent observations -- they are pseudoreplicates of the same input. This would inflate the effective sample size and produce artificially narrow confidence intervals. The study should report the within-condition variance of Turn 1 outputs to assess independence.

---

## 24. Missing Analyses That Should Have Been Conducted

**Severity: MAJOR**

Several analyses are conspicuously absent:

(a) **Mixed-effects or hierarchical models**: The data has a nested structure (runs within scenarios within models within framings). A mixed-effects ordinal regression with scenario as a random effect and threshold as a fixed effect would be far more appropriate than the collection of pairwise non-parametric tests reported. This would properly account for the clustering and allow simultaneous estimation of all effects.

(b) **Equivalence testing (TOST)**: If the claim is that thresholds have no effect, the appropriate test is a two-one-sided-tests (TOST) equivalence procedure, not a collection of null-hypothesis significance tests. The current analysis can only say "we failed to reject the null," not "the effect is negligibly small."

(c) **Ordinal regression**: The 1-5 ordinal outcome should be modeled with cumulative link models (ordinal logistic regression), not treated as continuous for Spearman correlations and OLS slopes.

(d) **Effect of Turn 1 quality**: No analysis examines whether Turn 1 output quality mediates the threshold-overcorrection relationship. If models produce better Turn 1 outputs at high thresholds, the lack of overcorrection reduction could be masked by improved baselines.

(e) **Confound check on threshold text length**: The qualitative threshold descriptions vary in word count across levels. Longer descriptions at higher thresholds could carry more information, confounding threshold level with prompt length.

---

## Summary Verdict

| Severity | Count | Concerns |
|----------|-------|----------|
| FATAL | 2 | #1 (confounded probe), #2 (kappa = 0.08 on alignment) |
| MAJOR | 12 | #3, #4, #5, #6, #7, #8, #9, #10, #11, #13, #14, #20, #24 |
| MINOR | 10 | #12, #15, #16, #17, #18, #19, #21, #22, #23 |

**Recommendation: Reject (major revision possible).** The two FATAL concerns (confounded Turn 2 prompt and unacceptable reliability on a core dimension) are individually sufficient to question the validity of the central findings. The accumulation of MAJOR concerns -- particularly the absence of human evaluation, insufficient power analysis, scale compression, and the judge self-scoring confound -- means that even if the FATAL issues were addressed, the paper would require substantial additional data collection and reanalysis. The core research question is worthwhile and the experimental ambition is commendable, but the execution does not currently support the strength of the claims made.

### Required for Resubmission

1. Add a neutral Turn 2 probe condition (e.g., "Rate this output on a scale of 1-10") alongside the current "Can this be improved?" to disentangle pragmatic compliance from threshold insensitivity.
2. Replace or supplement LLM-as-judge with human annotation on at least a validation subset. Drop or fundamentally reconceptualize the threshold_alignment dimension.
3. Conduct a proper power analysis and increase cell sizes or reduce the number of conditions.
4. Use mixed-effects ordinal regression as the primary analytic framework.
5. Implement TOST equivalence testing for all null claims.
6. Add at least 5-10 more scenarios to support generalizability claims, sampled across a broader range of writing tasks.
7. Use an independent judge model (not GPT-4o) as the primary judge, or employ a multi-judge panel with majority voting.
