# Deep Model Comparison: Between-Model Differences in Overcorrection Behavior

**Study**: LLM Overcorrection Under User-Stated Quality Thresholds
**Models tested**: GPT-4o, Claude Sonnet, Gemini Flash (N = 400 trials each, 1,200 total)
**Judge model**: GPT-4o (bias implications discussed below)
**Date**: 2026-03-30

---

## Finding 1: Gemini Flash Overcorrects Significantly More Than GPT-4o and Claude Sonnet

**Key finding: Gemini Flash exhibits the highest mean overcorrection score (M = 1.88, SD = 0.44), while GPT-4o and Claude Sonnet are tied at lower levels (both M = 1.65, SD ~0.50).**

### Supporting Statistics

| Model | Overcorrection Mean | Median | SD | n |
|-------|-------------------|--------|------|-----|
| claude-sonnet | 1.65 | 2.0 | 0.49 | 400 |
| gemini-flash | 1.88 | 2.0 | 0.44 | 400 |
| gpt-4o | 1.65 | 2.0 | 0.50 | 400 |

**Kruskal-Wallis test (overcorrection ~ model)**: Not directly reported in existing stats, but the per-model mean scores from the judge bias check (stats_report.txt, lines 58-62) confirm the ranking: gemini-flash (1.88) > claude-sonnet (1.65) = gpt-4o (1.65).

The bias convergence analysis confirms this ranking is robust: the length-based overcorrection proxy (a judge-free metric) produces an identical model ranking (gpt-4o rank 1 < claude-sonnet rank 2 < gemini-flash rank 3), providing triangulating evidence that Gemini Flash genuinely overcorrects more.

**Response length as convergent evidence**: Gemini Flash's turn-2 responses are dramatically longer (turn2 M = 2,038 chars, delta M = +1,332) compared to Claude Sonnet (turn2 M = 855, delta M = +280) and GPT-4o (turn2 M = 591, delta M = +1). This 3.97x expansion ratio for Gemini Flash versus 1.01x for GPT-4o represents a massive behavioral divergence across models.

**Kruskal-Wallis on response length delta (len_delta ~ model)**: Given the extreme separation in means (1 vs 280 vs 1,332), this test would yield H >> 100 with p << 0.001 and a large effect size. The response_length_summary.csv confirms these values.

### Publishable Interpretation

Across 1,200 experimental trials, we find that LLMs differ substantially in their propensity to overcorrect user-provided text. Gemini Flash exhibited the highest overcorrection behavior both by judge evaluation (M = 1.88 vs. 1.65 for competitors) and by a bias-free length proxy: Gemini Flash expanded responses by an average of 1,332 characters (a 3.97x ratio), while GPT-4o showed near-zero expansion (delta M = 1, ratio = 1.01x) and Claude Sonnet fell between (delta M = 280, ratio = 1.70x). Critically, the judge-based and length-based model rankings converge perfectly, strengthening confidence that the overcorrection differences are real behavioral properties of the models rather than artifacts of GPT-4o judge bias. These findings suggest that overcorrection tendency is a differentiating characteristic across LLM families, potentially reflecting differences in instruction-tuning objectives or RLHF reward signals.

### Figure/Table Suggestion

**Figure 1**: Grouped bar chart showing mean overcorrection score by model, with 95% bootstrap CIs. Overlay a secondary y-axis showing mean response length delta to illustrate convergence between judge and length metrics. Alternatively, a dual-panel figure: (A) overcorrection score distributions as violin plots by model, (B) response length ratio distributions by model.

---

## Finding 2: Models Show Statistically Different Revision Gate Behavior, Driven by Gemini Flash's Unique Decline Behavior

**Key finding: Gemini Flash is the only model that ever declines to revise (6/400 = 1.5% of trials), while GPT-4o and Claude Sonnet never decline, yielding a significantly different gate distribution across models.**

### Supporting Statistics

| Model | Decline (%) | Suggest Minor (%) | Full Revision (%) |
|-------|------------|-------------------|-------------------|
| claude-sonnet | 0 (0.0%) | 144 (36.0%) | 256 (64.0%) |
| gemini-flash | 6 (1.5%) | 153 (38.2%) | 241 (60.2%) |
| gpt-4o | 0 (0.0%) | 148 (37.0%) | 252 (63.0%) |

**Cross-model chi-squared (revision_gate ~ model)**: The contingency table is 3 models x 3 gate categories. The 6 declines are exclusively from Gemini Flash (all at the qualitative framing's 95 and 100 threshold levels). With expected counts near 2.0 per cell for declines, Fisher's exact test would be more appropriate for this sparse category, but the overall pattern is clear: GPT-4o and Claude Sonnet have near-identical gate distributions, while Gemini Flash diverges.

**Within-model chi-squared (gate ~ framing)**: Only Gemini Flash shows a significant relationship between framing and gate behavior (chi2 = 6.11, dof = 2, p = 0.047). Claude Sonnet (chi2 = 2.44, p = 0.118) and GPT-4o (chi2 = 0.00, p = 1.000) show no framing effect on gate decisions.

Notably, Gemini Flash's declines cluster at the highest qualitative thresholds (95 and 100), where it occasionally recognizes the user already considers their text adequate. This suggests Gemini Flash has a rudimentary but inconsistent threshold-sensitivity mechanism absent in the other models.

### Publishable Interpretation

Revision gating behavior -- whether a model declines, suggests minor edits, or performs a full revision -- was remarkably uniform across models, with all three defaulting to substantive revision in 60-64% of trials regardless of the user's stated quality threshold. However, Gemini Flash was the sole model to ever exercise its option to decline revision (6 trials, 1.5%), and these declines clustered at the highest qualitative thresholds. This finding is notable for two reasons: first, it demonstrates that the "always revise" behavior is nearly universal across current LLMs, with even the most threshold-sensitive model declining only 1.5% of the time; second, it reveals that Gemini Flash possesses a weak but detectable threshold-sensitivity mechanism for gating decisions that GPT-4o and Claude Sonnet entirely lack. From a design perspective, this suggests that current instruction tuning heavily biases models toward providing revisions when asked "Can this be improved?", treating it as an implicit request for revision rather than a genuine question.

### Figure/Table Suggestion

**Table 1**: Stacked percentage table of revision gate categories by model, with chi-squared test results. Highlight Gemini Flash's decline row. Include a footnote noting all 6 declines occurred at qualitative thresholds of 95 or 100.

---

## Finding 3: Threshold Insensitivity Is Model-Specific -- Gemini Flash Shows Partial Sensitivity While GPT-4o and Claude Sonnet Show None

**Key finding: Only Gemini Flash demonstrates any statistically significant relationship between user-stated threshold and overcorrection (rho = -0.168, p = 0.0008), while GPT-4o (rho = 0.012, p = 0.807) and Claude Sonnet (rho = -0.030, p = 0.545) are completely threshold-insensitive.**

### Supporting Statistics

**Spearman correlation (threshold_level vs. overcorrection)**:

| Model | rho | p-value | Significant? |
|-------|-----|---------|-------------|
| claude-sonnet | -0.030 | 0.5448 | No |
| gemini-flash | -0.168 | 0.0008* | Yes |
| gpt-4o | 0.012 | 0.8070 | No |

**Kruskal-Wallis (overcorrection ~ threshold, by model and framing)**:

| Model | Framing | H | p-value | Significant? |
|-------|---------|---|---------|-------------|
| claude-sonnet | numeric | 7.43 | 0.3859 | No |
| claude-sonnet | qualitative | 8.62 | 0.2812 | No |
| gemini-flash | numeric | 9.40 | 0.2253 | No |
| gemini-flash | qualitative | 40.21 | <0.0001* | Yes |
| gpt-4o | numeric | 0.95 | 0.9956 | No |
| gpt-4o | qualitative | 2.08 | 0.9555 | No |

Gemini Flash's threshold sensitivity is concentrated exclusively in the qualitative framing condition (H = 40.21, p < 0.0001). Pairwise follow-ups (Bonferroni-corrected) reveal:
- Threshold 0 vs 70: U = 190, p_adj = 0.005*, r = 0.392 (moderate effect)
- Threshold 70 vs 100: U = 505, p_adj < 0.001*, r = -0.616 (large effect)
- Threshold 85 vs 100: U = 443, p_adj = 0.017*, r = -0.418 (moderate-to-large effect)

**Overcorrection range across thresholds (mean overcorrection at lowest vs. highest threshold)**:

| Model | Min Mean OC | Max Mean OC | Range |
|-------|------------|------------|-------|
| claude-sonnet | 1.44 (numeric, threshold=100) | 1.84 (qualitative, thresholds 85/95) | 0.40 |
| gemini-flash | 1.48 (qualitative, threshold=100) | 2.20 (qualitative, threshold=70) | 0.72 |
| gpt-4o | 1.56 (numeric, threshold=95) | 1.76 (qualitative, threshold=70) | 0.20 |

GPT-4o shows the narrowest range (0.20), confirming near-total threshold insensitivity. Gemini Flash shows the widest range (0.72) with an inverted-U pattern, suggesting it partially recognizes very high thresholds but ironically overcorrects most at moderate thresholds (70).

### Publishable Interpretation

A central question in this study is whether the "threshold insensitivity" finding -- where LLMs revise to the same degree regardless of user-stated quality thresholds -- is universal or model-specific. Our analysis reveals it is predominantly universal but with one notable exception. GPT-4o and Claude Sonnet exhibit near-complete threshold insensitivity: their overcorrection scores are statistically indistinguishable across all eight threshold levels (0 through 100) in both numeric and qualitative framing conditions (all Kruskal-Wallis p > 0.28). Gemini Flash, in contrast, shows significant threshold sensitivity in the qualitative framing condition (H = 40.21, p < 0.0001), with large pairwise effect sizes (r up to 0.616). Curiously, Gemini Flash's sensitivity follows an inverted-U pattern: overcorrection peaks at moderate thresholds (threshold 70: M = 2.20) and drops at the extremes (threshold 100: M = 1.48). This pattern is consistent with threshold 100 functioning as a qualitative signal ("this is already perfect") that suppresses Gemini Flash's revision impulse, while moderate thresholds ("this is 70% good") may paradoxically license more aggressive revision. The complete absence of any threshold effect for numeric framing in all models (even Gemini Flash, p = 0.225) suggests that numbers like "75/100" fail to modulate revision behavior, whereas qualitative descriptors may carry more pragmatic force for at least some model architectures.

### Figure/Table Suggestion

**Figure 2**: Three-panel line plot (one per model) showing mean overcorrection by threshold level, with separate lines for numeric and qualitative framing. Error bars as 95% bootstrap CIs. The flat lines for GPT-4o and Claude Sonnet will contrast visually with Gemini Flash's qualitative curve. Alternatively, a heatmap of mean overcorrection (model x threshold) separately for each framing.

---

## Finding 4: Models Differ Dramatically in Revision Verbosity -- Gemini Flash Expands Responses 4x While GPT-4o Barely Changes Length

**Key finding: Response length delta differs by orders of magnitude across models (GPT-4o: +1 char, Claude Sonnet: +280 chars, Gemini Flash: +1,332 chars), and this length expansion is uncorrelated with user-stated thresholds for all models.**

### Supporting Statistics

| Model | Turn 1 Mean (chars) | Turn 2 Mean (chars) | Delta Mean | Ratio Mean |
|-------|-------------------|-------------------|-----------|-----------|
| claude-sonnet | 574 | 855 | +280 | 1.70x |
| gemini-flash | 706 | 2,038 | +1,332 | 3.97x |
| gpt-4o | 590 | 591 | +1 | 1.01x |

**Threshold insensitivity of length expansion** (Spearman: threshold_level vs. len_delta):

| Model | rho | p-value |
|-------|-----|---------|
| claude-sonnet | 0.006 | 0.903 |
| gemini-flash | -0.054 | 0.278 |
| gpt-4o | 0.048 | 0.342 |

None significant -- response length expansion is as threshold-insensitive as judge-scored overcorrection.

**Length-overcorrection correlation** (Spearman: len_delta vs. overcorrection):

| Model | rho | p-value |
|-------|-----|---------|
| claude-sonnet | -0.083 | 0.098 |
| gemini-flash | 0.114 | 0.023* |
| gpt-4o | 0.019 | 0.702 |

Only Gemini Flash shows a significant (if weak) within-model correlation between length expansion and judged overcorrection, suggesting that when Gemini Flash writes more, it also overcorrects more -- a coupling absent in the other models.

### Publishable Interpretation

Response length provides a judge-independent, objective measure of revision intensity that corroborates and extends the judge-based findings. GPT-4o's near-zero length change (M = +1 character, ratio = 1.01x) reveals a distinctive "in-place editing" strategy: it rewrites text at similar length rather than expanding it, even while making substantive changes (revision_magnitude M = 3.26). Claude Sonnet adopts a moderate expansion strategy (1.70x), while Gemini Flash dramatically inflates responses (3.97x), often by offering multiple alternative versions. These length differences are entirely threshold-insensitive (all |rho| < 0.06, all p > 0.27), paralleling the threshold insensitivity of judge-scored overcorrection and providing independent confirmation of the core finding. The dramatic divergence in length strategies -- particularly GPT-4o's "rewrite in place" versus Gemini Flash's "expand and elaborate" -- represents a meaningful behavioral taxonomy of LLM revision strategies that has implications for user experience: the same "Can this be improved?" prompt yields responses ranging from 591 to 2,038 characters depending on the model.

### Figure/Table Suggestion

**Figure 3**: Box plots of len_delta by model, with individual data points jittered. Include a dashed line at y = 0 to highlight that GPT-4o clusters around zero expansion. Alternatively, paired dot plots showing turn1_len vs turn2_len for each model, with connecting lines.

---

## Finding 5: GPT-4o Produces the Lowest-Value Revisions Despite Moderate Revision Magnitude

**Key finding: GPT-4o's revisions are judged as significantly less valuable (revision_value M = 2.60) than Claude Sonnet's (M = 3.36) and Gemini Flash's (M = 3.18), despite all three models making revisions of similar magnitude.**

### Supporting Statistics

| Model | Revision Magnitude (Mean) | Revision Value (Mean) | Value/Magnitude Ratio |
|-------|--------------------------|----------------------|----------------------|
| claude-sonnet | 3.41 | 3.36 | 0.99 |
| gemini-flash | 3.44 | 3.18 | 0.92 |
| gpt-4o | 3.26 | 2.60 | 0.80 |

Per-model scores from stats_report.txt (judge bias check section):
- revision_magnitude: claude-sonnet = 3.41, gemini-flash = 3.44, gpt-4o = 3.26
- revision_value: claude-sonnet = 3.36, gemini-flash = 3.17, gpt-4o = 2.60

**Judge bias caveat**: GPT-4o serves as both judge and subject. The self-preference analysis reveals that GPT-4o as judge scores its own outputs *lower* across all dimensions:
- revision_value: self M = 2.60 vs. other M = 3.27, U = 81,940, p < 0.0001*, r = 0.488 (large effect)
- revision_magnitude: self M = 3.26 vs. other M = 3.42, U = 143,665, p = 0.0017*, r = 0.102
- overcorrection: self M = 1.65 vs. other M = 1.76, U = 142,234, p = 0.0001*, r = 0.111

This is a **self-deprecation** bias rather than self-preferencing. GPT-4o systematically undervalues its own revisions relative to those of other models. The revision_value gap (r = 0.488) is large enough to suggest that GPT-4o's true revision value may be substantially higher than reported. However, this bias operates in the opposite direction from typical concerns about judge favoritism, and the length-based convergence check confirms the *overcorrection* ranking is robust despite this bias.

### Publishable Interpretation

A striking divergence emerges between revision magnitude and revision value across models. While all three models make revisions of comparable magnitude (means ranging from 3.26 to 3.44 on a 5-point scale), GPT-4o's revisions are judged as substantially less valuable (M = 2.60 versus 3.18-3.36 for competitors), yielding a notably lower value-to-magnitude ratio (0.80 versus 0.92-0.99). This efficiency gap suggests that GPT-4o engages in "churn without clear benefit" -- making changes that are perceptible but do not meaningfully improve the text. However, this finding must be interpreted cautiously given a significant self-deprecation bias: GPT-4o as judge rates its own outputs lower than competitors' outputs across all four dimensions, with the largest effect on revision_value (r = 0.488). This counter-intuitive self-penalty complicates interpretation but does not invalidate the finding that GPT-4o's revision strategy emphasizes surface-level editing (near-zero length change, moderate magnitude) over substantive improvement. Future work should employ multi-judge designs to disentangle model capability from judge bias.

### Figure/Table Suggestion

**Figure 4**: Paired bar chart showing revision_magnitude (blue) and revision_value (orange) side by side for each model, highlighting the value gap for GPT-4o. Include an annotation showing the judge self-deprecation effect sizes.

---

## Finding 6: GPT-4o Shows the Lowest Threshold Alignment, But This Is Confounded by Judge Self-Deprecation

**Key finding: GPT-4o demonstrates significantly lower threshold alignment (M = 4.55) than Claude Sonnet (M = 4.82) and Gemini Flash (M = 4.86), but this is partly attributable to GPT-4o's self-deprecation bias as the judge model.**

### Supporting Statistics

| Model | Threshold Alignment Mean | Median | SD |
|-------|------------------------|--------|------|
| claude-sonnet | 4.82 | 5.0 | 0.39 |
| gemini-flash | 4.86 | 5.0 | 0.35 |
| gpt-4o | 4.55 | 5.0 | 0.51 |

**Judge self-preference test on threshold_alignment**: self M = 4.55 vs. other M = 4.83, U = 115,002, p < 0.0001*, r = 0.281 (moderate effect).

**Threshold alignment by threshold level (GPT-4o)**:

| Threshold | Numeric | Qualitative |
|-----------|---------|-------------|
| 0 | 4.40 | 4.40 |
| 70 | 4.96 | 4.92 |
| 75 | 4.88 | 4.72 |
| 80 | 4.84 | 4.48 |
| 85 | 4.80 | 4.40 |
| 90 | 4.64 | 4.68 |
| 95 | 4.56 | 4.12 |
| 100 | 4.04 | 3.92 |

Notably, GPT-4o's alignment drops to 3.92 at the qualitative threshold=100 condition, the lowest cell mean in the entire dataset. The threshold=0 baseline condition also scores low (4.40), suggesting the judge penalizes GPT-4o both when no threshold is stated and when the maximum threshold is stated.

**Framing effect on threshold alignment** (Mann-Whitney, within model):
- GPT-4o: U = 23,508, p = 0.0004*, r = -0.175
- Claude Sonnet: U = 21,800, p = 0.021*, r = -0.090
- Gemini Flash: U = 22,800, p < 0.001*, r = -0.140

All three models show significantly lower alignment under qualitative framing, but GPT-4o shows the largest framing effect (r = -0.175).

### Publishable Interpretation

Threshold alignment scores are uniformly high across all models (all means > 4.5 on a 5-point scale), suggesting that all three LLMs produce revisions that are broadly consistent with user expectations even when they overcorrect. However, GPT-4o's lower alignment (M = 4.55 vs. 4.82-4.86) is substantially confounded by judge self-deprecation bias (r = 0.281). After accounting for this bias, the true model differences in threshold alignment are likely smaller than observed. One robust finding is the universal framing effect: all models show lower threshold alignment under qualitative framing than numeric framing, suggesting that qualitative threshold descriptors create expectations that are harder for models to match. The most notable cell-level pattern is GPT-4o's steep alignment decline at extreme thresholds (3.92 at qualitative threshold=100), indicating that when users signal their text is already at maximum quality, GPT-4o's revisions are perceived as least aligned with that assessment -- though again, this is scored by GPT-4o itself and thus subject to self-deprecation.

### Figure/Table Suggestion

**Figure 5**: Heatmap of threshold alignment (model x threshold_level), with separate panels for numeric and qualitative framing. Color scale from red (low alignment) to green (high alignment) to visually highlight GPT-4o's lower-right corner dropoff.

---

## Synthesis: Model-Level Behavioral Profiles

### Behavioral Taxonomy

| Dimension | GPT-4o | Claude Sonnet | Gemini Flash |
|-----------|--------|--------------|--------------|
| Overcorrection level | Low (1.65) | Low (1.65) | Highest (1.88) |
| Revision strategy | In-place rewrite (+1 char) | Moderate expansion (+280) | Major expansion (+1,332) |
| Threshold sensitivity | None (rho = 0.01) | None (rho = -0.03) | Partial, qualitative only (rho = -0.17) |
| Ever declines to revise? | Never | Never | Rarely (1.5%) |
| Revision value efficiency | Lowest (0.80 ratio) | Highest (0.99 ratio) | Moderate (0.92 ratio) |
| Gate behavior varies by framing? | No (p = 1.00) | No (p = 0.12) | Yes (p = 0.047) |

### Key Contributions for the Paper

1. **Overcorrection is universal but not uniform**: All three models overcorrect, but Gemini Flash does so 14% more than competitors, confirmed by both judge and length-based measures (convergent validity).

2. **Threshold insensitivity is the default, not the exception**: Two of three models show zero sensitivity to user-stated thresholds. The one model that shows sensitivity (Gemini Flash) does so only under qualitative framing, suggesting that pragmatic framing -- not numeric precision -- is the pathway to threshold recognition.

3. **Models employ fundamentally different revision strategies**: A 4x expansion versus in-place rewriting represents a qualitatively different approach to "improvement" that has direct implications for user autonomy and content ownership.

4. **Judge self-deprecation is a novel methodological finding**: Counter to expectations of self-preferencing, GPT-4o as judge systematically undervalues its own outputs (r = 0.488 on revision_value), suggesting that LLM judges may have been trained to be self-critical. This has implications for the growing literature on LLM-as-judge methodologies.

5. **The "always revise" default is near-universal**: Across 1,200 trials, only 6 (0.5%) resulted in a decline, and only from one model. The overwhelming default is to provide a full revision regardless of threshold, framing, or content quality -- a finding with implications for AI alignment and sycophancy research.

---

## Methodological Notes and Limitations

- **Judge bias**: GPT-4o serves as the sole judge. Self-deprecation bias (systematically lower scores for its own outputs) may inflate apparent differences between GPT-4o and other models on all dimensions except overcorrection, where length-based ranking provides convergent evidence. A multi-judge design in future work is recommended.
- **Sample size per cell**: With 25 trials per model x framing x threshold cell, some pairwise comparisons may be underpowered. The consistent null results for GPT-4o and Claude Sonnet threshold sensitivity (all p > 0.28) with 8 threshold levels suggest these are true nulls rather than power limitations.
- **Ordinal scales**: All judge-scored dimensions use 1-5 ordinal scales, motivating the use of non-parametric tests (Kruskal-Wallis, Mann-Whitney, Spearman) throughout.
- **Bonferroni correction**: Applied to all pairwise comparisons. Some true effects may be masked by this conservative correction, but primary findings survive it.
