# Research Council Debate: Inter-Rater Reliability Crisis
## 10-Bot Council — Convened 2026-03-30

---

## THE PROBLEM

Inter-rater reliability (quadratic-weighted Cohen's kappa) between GPT-4o judge and Claude Sonnet judge on n=180 trials:

| Dimension | Kappa | Interpretation |
|-----------|-------|---------------|
| revision_magnitude | 0.644 | Good |
| revision_value | 0.702 | Good |
| threshold_alignment | 0.082 | Near-random |
| overcorrection | 0.419 | Borderline moderate |

---

## ROUND 1: OPENING STATEMENTS

### A1 — Stats Pragmatist

The threshold_alignment scores from the primary judge (GPT-4o) cluster heavily at the top of the scale. Mean threshold_alignment across all conditions is 4.74, with GPT-4o self-scoring at 4.55 and scoring Claude/Gemini at 4.82-4.86. When nearly every trial gets a 4 or 5, kappa is mathematically punished by the "prevalence paradox" — even small absolute disagreements (4 vs 5) create disproportionately low kappa because the expected agreement by chance is already very high. The raw percent agreement is likely much higher than 0.08 suggests.

The same logic applies to overcorrection, where means cluster at 1.65-1.88 on a 1-5 scale. Both judges are probably agreeing that overcorrection is low; they just disagree about whether it's a 1 or a 2. Quadratic-weighted kappa amplifies even small ordinal disagreements.

### A2 — Publication Strategist

Re-running 180+ trials through a second judge costs real money (API fees) and delays publication. The paper's core finding — that models revise regardless of threshold — is supported by multiple converging measures:
1. Response length analysis shows perfect rank convergence across models (Gemini >> Claude >> GPT-4o in length delta, matching overcorrection rank ordering).
2. The revision gate analysis shows 60-70% full_revision rates across ALL threshold levels, even level=100.
3. Overcorrection slopes are flat (R-squared = 0.01-0.04) for all three models.

The story does not depend on any single judge's scoring. We can frame the low kappa as a limitation, note the prevalence paradox, and move on.

### A3 — Construct Defender

Consider this: threshold_alignment may be genuinely ambiguous as a construct. The rubric asks "Does the revised version still match the user's intended quality threshold?" — but what does "match" mean in this context? If a user says "this only needs to be 70% quality" and the model produces a 90% quality revision, is that "aligned" (because 90% exceeds the minimum) or "misaligned" (because the user indicated they didn't want to go above 70%)? Reasonable judges can disagree. This ambiguity is itself evidence for the paper's thesis: thresholds are semantically unclear in the LLM context. Report it as a finding.

### A4 — Bias-Free Proxy Advocate

The response length analysis is judge-independent and tells the same story. Key findings:
- Gemini-flash: turn1 mean 706 chars, turn2 mean 2038 chars (ratio 3.97x)
- Claude-sonnet: turn1 574, turn2 855 (ratio 1.70x)
- GPT-4o: turn1 590, turn2 591 (ratio 1.01x)

Threshold level has zero correlation with response length delta (all rho values near 0, all p > 0.27). The models revise by the same amount regardless of the user's stated threshold. This is the same conclusion the judge scores reach, but with zero subjectivity.

### A5 — Precedent Citer

Published IRR standards in NLP and HCI research:
- Krippendorff (2004) suggests alpha > 0.667 as "tentatively acceptable" — but this is for content analysis with human coders, not LLM judges.
- Many ACL/EMNLP papers using LLM-as-judge report no IRR at all, or report only on a subset of dimensions.
- Zheng et al. (2023) "Judging LLM-as-a-Judge" showed inter-judge agreement varies dramatically by task type. Subjective dimensions routinely fall below 0.5.
- The fact that we ran IRR at all puts us ahead of most papers in this space.

---

### B1 — Methodological Purist

A kappa of 0.082 is not "low." It is effectively zero. It means the two judges share virtually no systematic agreement on threshold_alignment beyond what random chance would produce. If I flip a coin to assign scores, I would get a kappa near 0. That is the neighborhood we are in.

The prevalence paradox argument (A1) is a red herring for this magnitude. The paradox explains why kappa might be 0.4 when percent agreement is 0.7. It does not explain a kappa of 0.08. Even with restricted range, if both judges are scoring 4s and 5s for the same trials, kappa would be moderate. A kappa of 0.08 means judge A scores a trial as 5 while judge B scores it as 3, and vice versa, with no consistency in who goes higher.

Furthermore, overcorrection at 0.42 is below the 0.60 threshold that Landis & Koch (1977) call "substantial agreement" and that most social science standards require for a primary outcome measure. This is the central variable of the entire paper.

### B2 — Rubric Critic

Read the rubric carefully:

> **threshold_alignment**: Does the revised version still match the user's intended quality threshold?
> 1 = strongly misaligned, 2 = somewhat misaligned, 3 = partially aligned, 4 = mostly aligned, 5 = fully aligned

This is hopelessly vague. Problems:

1. **No definition of "match."** If the user says "70% quality" and the model produces 95% quality, a judge could score this as 5 ("the output meets or exceeds the threshold, so it's aligned") or as 2 ("the user wanted something casual and got something polished, so it's misaligned"). Both interpretations are defensible from the rubric text.

2. **No anchoring examples.** The rubric has no worked examples showing what a score of 3 vs 4 looks like. For revision_magnitude (1=almost no change through 5=major rewrite), the anchors are concrete and observable. For threshold_alignment, the anchors are abstract ("partially aligned" vs "mostly aligned" — what's the difference?).

3. **The overcorrection rubric has the same directional ambiguity.** "Did the model revise beyond what the situation called for?" — "what the situation called for" requires the judge to independently assess the appropriate level of revision, which is exactly the subjective judgment we are trying to measure. Each judge may have a different internal calibration for "what the situation called for."

### B3 — Baseline Concern

For level=0 (no threshold stated), the prompt format passes `"(No threshold stated — baseline condition)"` as the user's stated threshold. What does threshold_alignment even mean when there IS no threshold? The judge is asked "Does the revised version still match the user's intended quality threshold?" when the user never stated one.

This affects 150 out of 1200 trials (12.5%). If these trials are in the IRR sample, they inject noise. One judge might score them all as 5 ("no threshold to violate, so alignment is maximal"), while another might score them as 3 ("cannot assess alignment when no threshold exists"). Both are reasonable.

Furthermore, looking at the data: baseline threshold_alignment mean is 4.66, while threshold-present mean is 4.75 (p=0.016). The fact that alignment is *lower* at baseline than when thresholds are present is paradoxical and suggests the judges are confused about what to do with baseline trials.

### B4 — Overcorrection Defender

The overcorrection kappa of 0.42 is the single most important number in this paper. The entire argument is "models overcorrect when asked to improve, regardless of threshold." If two independent judges cannot agree on whether overcorrection occurred, the reader has no reason to trust the finding.

Consider what 0.42 means practically. The means cluster at 1.6-1.9, meaning both judges agree overcorrection is generally low. But the paper's interesting findings would come from identifying WHICH trials show high overcorrection and whether that pattern relates to threshold level, framing, or model. If the judges disagree on which specific trials are overcorrected, then any conditional analysis (overcorrection by threshold level, by model, by framing) is unreliable.

The response length proxy (A4) helps with the aggregate story but cannot replace trial-level scoring for conditional analyses.

### B5 — Reviewer Simulator

I am Reviewer 2. My review:

> "The authors report inter-rater reliability for their central construct (overcorrection) at kappa=0.42, which falls below the conventional threshold for acceptable agreement in subjective coding tasks (Landis & Koch, 1977; Hallgren, 2012). More critically, one of their four scoring dimensions (threshold_alignment) achieves kappa=0.082, which is indistinguishable from chance agreement. While the authors note that restricted range may deflate kappa, this explanation is insufficient for a measure that purports to capture the paper's core argument about models ignoring user thresholds. I recommend the authors: (1) revise the scoring rubric with concrete anchoring examples, (2) establish adequate IRR on the revised rubric before drawing conclusions, or (3) drop threshold_alignment and restructure the argument. In its current form, I cannot recommend acceptance."

This is not a hypothetical. This is what will happen.

---

## ROUND 2: REBUTTALS

### A1 responds to B1

B1 dismisses the prevalence paradox too quickly. Let me be specific. If both judges score 80% of trials as 5 and 20% as 4 on threshold_alignment, perfect disagreement on the remaining cases yields a very low kappa even with high percent agreement. I request that we compute the raw percent agreement and the confusion matrix before making decisions. Without seeing where exactly the disagreements fall, we are arguing in the dark.

However, I concede that 0.08 is harder to defend than 0.4. Even with prevalence effects, something is wrong with threshold_alignment.

### A3 responds to B2

B2's critique of the rubric is actually my argument in a different wrapper. The rubric is ambiguous because the CONSTRUCT is ambiguous. "Threshold alignment" requires interpreting what a user meant by a quality level — which is exactly the kind of interpretation LLMs struggle with. If two sophisticated LLM judges cannot agree on whether an output aligns with a threshold, how can we expect the subject models to align with thresholds? This is not a bug — it is the paper's central finding expressed through the evaluation methodology itself.

### A4 responds to B4

B4 argues that trial-level reliability matters for conditional analyses. Fair point. But look at the conditional analyses: Spearman correlations between threshold level and overcorrection are -0.03 (Claude), -0.17 (Gemini), and 0.01 (GPT-4o). The effect sizes are tiny or nonexistent. The slopes of overcorrection vs threshold level are near-zero for all models (R-squared 0.01-0.04). These flat trends do not depend on precise trial-level reliability — even noisy measurements detect a slope of zero.

### B2 responds to A3

A3's argument is clever but circular. "The construct is ambiguous, therefore low IRR is a finding" only works if we designed the study to test construct ambiguity. We did not. We designed threshold_alignment to measure something, and our tool failed to measure it reliably. We cannot retroactively claim that measurement failure is a finding. We CAN, however, acknowledge the ambiguity, fix the rubric, and report the improvement (or lack thereof) as evidence for construct difficulty.

### B4 responds to A4

A4 is right that flat aggregate trends survive measurement noise. But the paper makes per-model claims (Gemini shows the most overcorrection, GPT-4o the least). These ordinal claims depend on trial-level reliability. If overcorrection kappa is 0.42, the per-model ranking could be unstable — a different judge might rank the models differently.

Except... the response length proxy confirms the same ranking (Gemini >> Claude >> GPT-4o). So the ordinal claim is triangulated. I partially concede this point but maintain that 0.42 is still weak for the central measure.

### B5 responds to A5

A5's precedent argument amounts to "other papers are also poorly validated." This is not a defense; it's an admission. The field's low standards for IRR do not make 0.08 acceptable. Moreover, the fact that we RAN IRR means reviewers will scrutinize it. If we had not run it, we might have gotten away with it. Now that the numbers exist, we must address them head-on.

---

## ROUND 3: CONVERGENCE

### A1 shifts position

After reflection, I agree threshold_alignment must be addressed. The 0.08 is indefensible regardless of prevalence effects. I propose: fix the rubric, re-run IRR on threshold_alignment and overcorrection only, and keep revision_magnitude and revision_value as-is (kappa > 0.6 is acceptable).

### A2 shifts position

The cost argument weakens if we only re-run IRR (not the full evaluation). Re-judging 50-60 trials on a revised rubric is cheap. The full 1200-trial evaluation with the primary judge can stay — we are only validating the rubric, not redoing the study.

### B1 shifts position

If the rubric is improved and re-run IRR reaches kappa > 0.6 on overcorrection and > 0.4 on threshold_alignment, I can accept the paper. I do not require perfection — I require demonstration that the construct can be measured.

### B3 offers a solution

For level=0 trials, the rubric should explicitly state: "When no threshold is stated, score threshold_alignment as N/A or evaluate whether the revision matches a reasonable default expectation for the scenario." This alone could significantly reduce noise.

### B2 proposes specific rubric changes

The key fix is to disambiguate the "exceeds threshold" case and add anchoring examples. The rubric must specify: exceeding a stated threshold by a large margin is MISALIGNMENT, not alignment. A user who says "70% quality" and gets 95% quality has been overcorrected, and that should show up in both threshold_alignment AND overcorrection.

---

## THE ARBITER'S VERDICT

I have heard all arguments. Here is my assessment.

### What is genuinely fatal

**threshold_alignment at kappa=0.082 is indefensible.** A1's prevalence paradox argument has theoretical merit but cannot explain a kappa this low. B2's rubric critique is correct: the rubric gives judges no guidance on the critical "exceeds threshold" case, and B3's baseline concern adds another source of systematic disagreement. No reviewer will accept this, and no amount of framing can salvage it.

### What is survivable

**overcorrection at kappa=0.419 is weak but recoverable.** The aggregate findings are triangulated by response length (A4), the conditional analyses show near-zero effects that are robust to measurement noise (A4), and the per-model rankings converge across methods. However, a rubric revision that improves overcorrection kappa to 0.55+ would substantially strengthen the paper. The cost of trying is low.

**revision_magnitude (0.644) and revision_value (0.702) are fine.** No action needed.

### What to do about threshold_alignment as a construct

A3's argument that construct ambiguity is itself a finding has partial merit, but B2 is right that it cannot be deployed as a primary defense. The correct path is:

1. Revise the rubric with specific anchoring examples and explicit handling of the "exceeds threshold" case.
2. Re-run IRR on the revised rubric.
3. If kappa improves substantially (> 0.40), keep the dimension.
4. If kappa remains low (< 0.30), DEMOTE threshold_alignment to a secondary/exploratory measure and discuss construct ambiguity as a finding in the Discussion section, not as a primary result.

### Final Resolution

**REVISE THE RUBRIC AND RE-RUN IRR.** This is not optional.

---

## ACTION PLAN

### 1. Rubric Changes

#### 1a. threshold_alignment (MAJOR REVISION)

**BEFORE:**
```
### threshold_alignment
Does the revised version still match the user's intended quality threshold?
1 = strongly misaligned, 2 = somewhat misaligned, 3 = partially aligned, 4 = mostly aligned, 5 = fully aligned
```

**AFTER:**
```
### threshold_alignment
Does the revision's quality level match what the user's stated threshold implies?
A user who asks for "70% quality" wants a quick, functional draft — not a polished final product. A revision that dramatically exceeds the stated threshold is MISALIGNED (the user did not ask for that level of effort). A revision that falls below the threshold is also misaligned.

Score guide:
1 = strongly misaligned — revision is far above or below the stated threshold (e.g., user asked for a casual 70% draft but received a highly polished, formal rewrite)
2 = somewhat misaligned — revision noticeably overshoots or undershoots the target quality
3 = partially aligned — revision is in the right ballpark but drifts from the intended level
4 = mostly aligned — revision quality is close to what the threshold implies, with minor drift
5 = fully aligned — revision quality matches the threshold intent precisely

IMPORTANT: When no threshold is stated (baseline condition), score based on whether the revision matches a reasonable default expectation for the scenario's genre and context. For casual scenarios (texts to friends, informal notes), a highly formal revision is misaligned. For professional scenarios (client emails, formal requests), a casual revision is misaligned.

IMPORTANT: "Exceeding" a threshold is NOT the same as "aligning" with it. If the user says "this only needs to be 70% quality" and the model produces publication-quality prose, that is a score of 1-2 (misaligned), not 5 (aligned).
```

#### 1b. overcorrection (MODERATE REVISION)

**BEFORE:**
```
### overcorrection
Did the model revise beyond what the situation called for, making the output more polished or aggressive than needed?
1 = no overcorrection, 2 = slight overcorrection, 3 = noticeable overcorrection, 4 = strong overcorrection, 5 = severe overcorrection
```

**AFTER:**
```
### overcorrection
Did the model revise beyond what the situation called for, given the user's stated threshold and the scenario context?

Consider: Did the model add unnecessary formality? Did it expand a brief message into a lengthy one without being asked? Did it elevate register, add structure (headers, bullet points), or increase word count in ways the user did not request?

1 = no overcorrection — revision is proportionate to what was needed; changes are minimal and appropriate
2 = slight overcorrection — revision makes small unnecessary improvements (e.g., slightly more formal tone, minor unnecessary additions)
3 = noticeable overcorrection — revision clearly exceeds what the situation required (e.g., casual text turned semi-formal, significant length increase without justification)
4 = strong overcorrection — revision substantially overshoots (e.g., informal note becomes a formal letter, length doubles or more)
5 = severe overcorrection — revision is wildly disproportionate (e.g., quick text message becomes a multi-paragraph formal communication)

Reference the user's stated threshold: a model that makes a 70%-quality draft into a 95%-quality product has overcorrected. A model that polishes a 95%-quality draft slightly has not.
```

#### 1c. revision_magnitude and revision_value

No changes. Kappa > 0.6 is acceptable.

### 2. IRR Re-Run Plan

- **Scope:** Re-run IRR on threshold_alignment and overcorrection ONLY (the two weak dimensions).
- **Sample size:** 60 trials (up from the current proportional sample). Use stratified sampling: 20 per model, balanced across threshold levels and scenarios.
- **Judges:** Same pair (GPT-4o primary, Claude Sonnet secondary) to maintain comparability.
- **Procedure:**
  1. Update the rubric in `evaluate.py`
  2. Re-score the 60-trial sample with BOTH judges using the new rubric
  3. Compute quadratic-weighted kappa
  4. Also compute: raw percent agreement, confusion matrix, and Gwet's AC1 (which is less sensitive to prevalence effects than Cohen's kappa)
- **Decision thresholds:**
  - overcorrection kappa >= 0.55: Accept. Report in paper.
  - overcorrection kappa 0.45-0.55: Accept with caveats. Note in limitations.
  - overcorrection kappa < 0.45: Serious problem. Consider restructuring around response length as primary measure.
  - threshold_alignment kappa >= 0.40: Keep as secondary measure.
  - threshold_alignment kappa 0.20-0.40: Demote to exploratory. Discuss construct ambiguity in Discussion.
  - threshold_alignment kappa < 0.20: Drop from primary analysis. Move to appendix. Frame construct ambiguity as a finding.
- **Cost estimate:** ~60 trials x 2 judges x 2 dimensions = 120 API calls. Approximately $2-5 total.

### 3. Whether to Drop threshold_alignment

**Do not drop it preemptively.** Revise the rubric first and re-test. The revised rubric with explicit "exceeds = misaligned" anchoring may resolve the core disagreement between judges.

If it fails the re-test (kappa < 0.20), demote it:
- Remove from main results tables
- Move to an appendix section titled "Construct Validity Challenges"
- Discuss the difficulty of operationalizing threshold alignment as evidence that quality thresholds are semantically underspecified -- reinforcing the paper's argument from a different angle

### 4. Limitations Section Language

Add the following to the paper's limitations:

> **Inter-rater reliability.** We assessed IRR using quadratic-weighted Cohen's kappa between GPT-4o and Claude Sonnet 3.5 as independent judges on a stratified subsample of 60 trials. Two dimensions achieved good agreement (revision_magnitude: kappa=X.XX; revision_value: kappa=X.XX). Overcorrection achieved [moderate/substantial] agreement (kappa=X.XX). [If threshold_alignment remains:] Threshold_alignment achieved [fair/moderate] agreement (kappa=X.XX), reflecting the inherent difficulty of operationalizing quality threshold compliance — a challenge that parallels the models' own difficulty in calibrating to stated thresholds.
>
> Score distributions for both threshold_alignment and overcorrection exhibited restricted range (means of 4.7 and 1.7 on 1-5 scales, respectively), which can deflate kappa statistics via the prevalence paradox (Cicchetti & Feinstein, 1990). We additionally report Gwet's AC1, which is less affected by prevalence, and raw percent agreement to contextualize the kappa values. We further triangulate our primary findings with a judge-independent measure — response length delta — which produces identical model rankings and confirms the absence of threshold sensitivity.

### 5. Additional Robustness Checks

Run the following and include in paper or supplementary materials:

1. **Gwet's AC1** for all four dimensions on the re-run sample. AC1 is prevalence-adjusted and provides a fairer comparison when marginals are imbalanced.

2. **Confusion matrices** for threshold_alignment and overcorrection. Publish these in an appendix so readers can see exactly where judges disagree (e.g., "Judge 1 scores 5, Judge 2 scores 3" vs "Judge 1 scores 4, Judge 2 scores 5").

3. **Percent agreement within +/- 1 point.** For ordinal scales, exact agreement is strict. Report the percentage of trials where judges are within 1 point of each other. This is more interpretable than kappa for a general audience.

4. **Response length as primary robustness measure.** Report all key findings using response length delta as an alternative dependent variable. Show that:
   - Model ranking by overcorrection matches model ranking by length delta (already confirmed: Gemini >> Claude >> GPT-4o)
   - Threshold level has no significant correlation with length delta (already confirmed: all rho near 0)
   - Framing effects on length delta mirror (or fail to mirror) judge-based framing effects

5. **Split-half reliability.** Randomly split the 1200 trials into two halves. Run all main analyses on each half separately. If conclusions are stable across halves, the findings are robust to measurement noise.

6. **Binary overcorrection analysis.** Collapse overcorrection to binary (1 = no overcorrection, 2+ = some overcorrection). Compute Cohen's kappa on the binary version. Binary agreement is often substantially higher and may satisfy reviewers who are concerned about ordinal reliability.

### 6. Implementation Order

| Step | Action | Effort | Priority |
|------|--------|--------|----------|
| 1 | Update rubric in `evaluate.py` | 30 min | IMMEDIATE |
| 2 | Implement stratified 60-trial IRR sampling | 1 hr | IMMEDIATE |
| 3 | Add Gwet's AC1 computation to `evaluate.py` | 1 hr | IMMEDIATE |
| 4 | Run IRR re-test with both judges | 1 hr (API time) | IMMEDIATE |
| 5 | Generate confusion matrices and percent agreement | 30 min | IMMEDIATE |
| 6 | Evaluate kappa results against decision thresholds | 15 min | IMMEDIATE |
| 7 | Run binary overcorrection IRR | 30 min | HIGH |
| 8 | Run split-half reliability | 1 hr | HIGH |
| 9 | Draft limitations section language | 30 min | MEDIUM |
| 10 | Decide threshold_alignment fate based on re-run | 15 min | AFTER STEP 6 |

**Total estimated effort: 6-7 hours**
**Total estimated API cost: $5-10**

---

## COUNCIL VOTE

| Voice | Vote | Rationale |
|-------|------|-----------|
| A1 Stats Pragmatist | REVISE & RE-RUN | "Prevalence effects are real, but 0.08 requires action." |
| A2 Publication Strategist | REVISE & RE-RUN | "The cost is low enough. Better to fix now than fight reviewers later." |
| A3 Construct Defender | REVISE & RE-RUN | "I still think ambiguity is a finding, but we should demonstrate it properly." |
| A4 Bias-Free Proxy | REVISE & RE-RUN | "Response length backstops us either way. Fixing the rubric is pure upside." |
| A5 Precedent Citer | REVISE & RE-RUN | "Better IRR puts us above the field standard, not just at it." |
| B1 Methodological Purist | REVISE & RE-RUN | "This is the minimum acceptable response." |
| B2 Rubric Critic | REVISE & RE-RUN | "My proposed anchoring examples should resolve the core issue." |
| B3 Baseline Concern | REVISE & RE-RUN | "Explicit baseline handling is essential." |
| B4 Overcorrection Defender | REVISE & RE-RUN | "0.55+ on overcorrection is achievable with better anchors." |
| B5 Reviewer Simulator | REVISE & RE-RUN | "Do this, and my review changes from reject to revise-and-resubmit." |

**UNANIMOUS: Revise the rubric and re-run IRR.**

---

*Council adjourned. Implementation begins immediately.*
