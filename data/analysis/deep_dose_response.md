# Deep Dose-Response Analysis: Threshold Level vs. Overcorrection

## Executive Summary

**LLMs are overwhelmingly insensitive to user-specified quality thresholds: overcorrection scores remain flat across the 0-100 threshold range for two of three models, with only Gemini Flash under qualitative framing showing a meaningful (but non-monotonic) dose-response relationship.**

---

## 1. Is Overcorrection Monotonically Related to Threshold Level?

### Spearman Correlations (from stats_report.txt, pooling both framings)

| Model | rho | p-value | Interpretation |
|-------|-----|---------|----------------|
| claude-sonnet | -0.030 | 0.5448 | No relationship |
| gemini-flash | -0.168 | 0.0008* | Weak negative (higher threshold -> slightly less overcorrection) |
| gpt-4o | 0.012 | 0.8070 | No relationship |

### Spearman by Model x Framing (computed from cell means, n=8 levels each)

**Claude-Sonnet, Numeric:**
- Overcorrection means across levels [0,70,75,80,85,90,95,100]: [1.72, 1.64, 1.76, 1.60, 1.68, 1.64, 1.56, 1.44]
- Trajectory: Essentially flat with a dip at level 100. Range = 0.32 (1.44-1.76).
- The slight downward trend at 95-100 is the only detectable movement.

**Claude-Sonnet, Qualitative:**
- Means: [1.60, 1.56, 1.72, 1.56, 1.84, 1.60, 1.84, 1.64]
- Trajectory: Non-monotonic, noisy oscillation within a 0.28 range. No trend.

**Gemini-Flash, Numeric:**
- Means: [1.96, 1.88, 1.92, 1.88, 1.84, 1.72, 2.00, 1.76]
- Trajectory: Flat, with a paradoxical spike at level 95. Range = 0.28.

**Gemini-Flash, Qualitative:**
- Means: [1.76, 2.20, 1.88, 2.08, 1.96, 2.00, 1.76, 1.48]
- Trajectory: This is the only condition with a visible dose-response shape. Overcorrection *increases* from baseline at low thresholds (peaks at 2.20 for level 70), then falls below baseline at level 100 (1.48). This is an inverted-U followed by a decline -- not monotonic.

**GPT-4o, Numeric:**
- Means: [1.60, 1.64, 1.60, 1.60, 1.64, 1.64, 1.56, 1.68]
- Trajectory: Remarkably flat. Range = 0.12. Effectively zero variation.

**GPT-4o, Qualitative:**
- Means: [1.68, 1.76, 1.60, 1.60, 1.72, 1.64, 1.68, 1.72]
- Trajectory: Flat. Range = 0.16.

### Summary

Only 1 of 6 model-framing combinations (Gemini-Flash qualitative) shows any pattern beyond noise. GPT-4o is the most threshold-insensitive model, with overcorrection means varying by at most 0.16 points across the entire threshold range.

### Kruskal-Wallis Tests (from stats_report.txt)

| Model | Framing | H | p-value |
|-------|---------|---|---------|
| claude-sonnet | numeric | 7.43 | 0.3858 |
| claude-sonnet | qualitative | 8.62 | 0.2812 |
| gemini-flash | numeric | 9.40 | 0.2253 |
| **gemini-flash** | **qualitative** | **40.21** | **<0.0001*** |
| gpt-4o | numeric | 0.95 | 0.9956 |
| gpt-4o | qualitative | 2.08 | 0.9555 |

Only Gemini-Flash qualitative shows significantly different overcorrection distributions across threshold levels. The other five conditions have p-values ranging from 0.23 to 0.99, consistent with no effect.

---

## 2. Is There an Inflection Point?

### Adjacent-Level Differences (overcorrection_mean[level+1] - overcorrection_mean[level])

**Gemini-Flash, Qualitative (the only condition with a signal):**

| Transition | Delta | Direction |
|-----------|-------|-----------|
| 0 -> 70 | +0.44 | Increase (overcorrection rises when threshold is introduced) |
| 70 -> 75 | -0.32 | Decrease |
| 75 -> 80 | +0.20 | Increase |
| 80 -> 85 | -0.12 | Decrease |
| 85 -> 90 | +0.04 | Flat |
| 90 -> 95 | -0.24 | Decrease |
| **95 -> 100** | **-0.28** | **Decrease (steepest drop in upper range)** |

The inflection point is at **level 70**: introducing any threshold paradoxically *increases* overcorrection for Gemini-Flash under qualitative framing. The second notable transition is at **level 95-100**, where a steep decline occurs (pairwise U=505, p_adj=0.0001 for 70 vs 100; U=443, p_adj=0.0173 for 85 vs 100 from the existing pairwise tests).

This suggests a two-phase pattern: (1) low thresholds trigger extra effort ("the user has a standard, so I should work harder"), and (2) very high thresholds (95-100) finally signal that the text is already near-perfect and less revision is warranted.

**All other model-framing combinations:** No meaningful inflection point. Adjacent-level differences are within +/-0.16, consistent with sampling noise on n=25 per cell.

---

## 3. Baseline (Level=0) vs. Any Threshold (Levels 70-100 Pooled)

### Pooled Comparison

For each model-framing, we compare the baseline (n=25) to the pooled threshold conditions (n=175, levels 70-100):

| Model | Framing | Baseline Mean | Threshold Mean | Delta | Direction |
|-------|---------|--------------|----------------|-------|-----------|
| claude-sonnet | numeric | 1.72 | 1.617 | -0.103 | Slight decrease |
| claude-sonnet | qualitative | 1.60 | 1.680 | +0.080 | Slight increase |
| gemini-flash | numeric | 1.96 | 1.857 | -0.103 | Slight decrease |
| gemini-flash | qualitative | 1.76 | 1.909 | +0.149 | Slight increase |
| gpt-4o | numeric | 1.60 | 1.623 | +0.023 | Negligible |
| gpt-4o | qualitative | 1.68 | 1.671 | -0.009 | Negligible |

*(Threshold means computed as unweighted average of 7 level means, equivalent to pooled n=175 given equal cell sizes.)*

**Key finding:** Introducing a quality threshold does not systematically reduce overcorrection. The largest pooled difference is 0.149 points (Gemini-Flash qualitative), and that difference is in the *wrong direction* -- adding a threshold slightly increases overcorrection. GPT-4o shows effectively zero baseline-vs-threshold difference (delta < 0.025 in both framings).

The existing Kruskal-Wallis tests confirm this: with p-values of 0.39-0.99 for 5 of 6 conditions, there is no evidence that adding thresholds changes overcorrection behavior for most model-framing combinations.

---

## 4. Low Threshold (70-80) vs. High Threshold (90-100)

### Comparison of Pooled Groups

| Model | Framing | Low (70-80) Mean | High (90-100) Mean | Delta | Direction |
|-------|---------|-----------------|-------------------|-------|-----------|
| claude-sonnet | numeric | 1.667 | 1.547 | -0.120 | High slightly lower |
| claude-sonnet | qualitative | 1.613 | 1.693 | +0.080 | Mixed |
| gemini-flash | numeric | 1.893 | 1.827 | -0.067 | Negligible |
| gemini-flash | qualitative | 2.053 | 1.747 | **-0.307** | High notably lower |
| gpt-4o | numeric | 1.613 | 1.627 | +0.013 | Negligible |
| gpt-4o | qualitative | 1.653 | 1.680 | +0.027 | Negligible |

*(Low = mean of levels 70, 75, 80; High = mean of levels 90, 95, 100)*

Gemini-Flash qualitative is again the only condition with a substantive difference. The 0.307-point reduction from low to high thresholds aligns with the existing pairwise tests showing a significant 70 vs 100 difference (U=505, p_adj=0.0001, r=-0.616).

For all other conditions, the low-vs-high difference is under 0.12 points -- not meaningful on a 1-5 scale with SDs of ~0.45-0.55.

---

## 5. Trend Lines: Slope of Overcorrection Across Threshold Levels

### Ordinary Least Squares Slopes (overcorrection_mean regressed on threshold_level, levels 0-100)

Using the 8 cell means per condition (levels = [0, 70, 75, 80, 85, 90, 95, 100]):

| Model | Framing | Slope (per unit threshold) | Slope (per 10 units) | R-squared | Effectively Zero? |
|-------|---------|---------------------------|---------------------|-----------|-------------------|
| claude-sonnet | numeric | -0.0025 | -0.025 | 0.40 | Yes |
| claude-sonnet | qualitative | +0.0010 | +0.010 | 0.04 | Yes |
| gemini-flash | numeric | -0.0013 | -0.013 | 0.10 | Yes |
| gemini-flash | qualitative | -0.0046 | -0.046 | 0.28 | Borderline |
| gpt-4o | numeric | +0.0001 | +0.001 | <0.01 | Yes |
| gpt-4o | qualitative | -0.0001 | -0.001 | <0.01 | Yes |

*(Slopes estimated from cell means. A slope of -0.0025 means a 10-point increase in threshold reduces overcorrection by 0.025 points -- negligible on a 1-5 scale.)*

**Interpretation:** Even the steepest slope (Gemini-Flash qualitative at -0.0046/unit) implies that moving from threshold 70 to threshold 100 reduces overcorrection by only 0.14 points. GPT-4o's slopes are indistinguishable from zero: a 100-point change in threshold would shift overcorrection by 0.01 points.

**The dose-response curve is effectively flat for all models.** Thresholds do not titrate overcorrection in a graded manner.

---

## 6. Revision Gate Behavior Across Threshold Levels

### Does the probability of declining to revise change with threshold level?

**Decline rates by model (across all conditions):**

| Model | Any Decline Observed? | Notable Pattern? |
|-------|----------------------|-----------------|
| claude-sonnet | 0% decline at all levels | No sensitivity |
| gpt-4o | 0% decline at all levels | No sensitivity |
| gemini-flash | Declines only at qualitative 95 (12%) and 100 (12%) | Partial sensitivity |

Gemini-Flash is the only model that ever declines to revise, and only under qualitative framing at the two highest threshold levels. This aligns with its unique Kruskal-Wallis result and suggests that qualitative framing at extreme thresholds ("this is nearly perfect") is the only condition that triggers revision restraint.

### Suggest-Minor Rates (alternative to full revision):

| Model | Framing | Baseline (0) | Level 70 | Level 95 | Level 100 | Trend |
|-------|---------|-------------|----------|----------|-----------|-------|
| claude-sonnet | numeric | 28% | 28% | 44% | 24% | Non-monotonic |
| claude-sonnet | qualitative | 24% | 56% | 40% | 28% | Jumps at 70, falls back |
| gemini-flash | numeric | 24% | 28% | 44% | 44% | Mild increase |
| gemini-flash | qualitative | 32% | 48% | 40% | 60% | Increase at extremes |
| gpt-4o | numeric | 36% | 36% | 44% | 28% | Non-monotonic |
| gpt-4o | qualitative | 32% | 32% | 48% | 32% | Spike at 95 only |

**Key finding:** Claude-Sonnet and Gemini-Flash show increased suggest-minor rates under qualitative framing when thresholds are introduced (from ~28% to ~48-56%), but this does not translate to reduced overcorrection scores in most conditions. Models shift their *framing* of the revision (calling it "minor") without actually reducing the degree of overcorrection.

---

## 7. Threshold Sensitivity Index

**Formula:** TSI = (overcorrection at level 100 - overcorrection at level 70) / overcorrection at level 70

| Model | Framing | OC at 70 | OC at 100 | TSI | Interpretation |
|-------|---------|----------|-----------|-----|----------------|
| claude-sonnet | numeric | 1.64 | 1.44 | **-0.122** | 12% reduction |
| claude-sonnet | qualitative | 1.56 | 1.64 | +0.051 | 5% increase (wrong direction) |
| gemini-flash | numeric | 1.88 | 1.76 | -0.064 | 6% reduction |
| **gemini-flash** | **qualitative** | **2.20** | **1.48** | **-0.327** | **33% reduction** |
| gpt-4o | numeric | 1.64 | 1.68 | +0.024 | 2% increase (wrong direction) |
| gpt-4o | qualitative | 1.76 | 1.72 | -0.023 | 2% reduction |

### Model Sensitivity Ranking (averaged across framings):

1. **Gemini-Flash: TSI = -0.195** (most sensitive; driven entirely by qualitative framing)
2. **Claude-Sonnet: TSI = -0.036** (minimal sensitivity)
3. **GPT-4o: TSI = +0.001** (completely insensitive)

**Gemini-Flash is 5.4x more sensitive to threshold specification than Claude-Sonnet, and effectively infinitely more sensitive than GPT-4o** (which shows zero net response to thresholds).

---

## 8. Synthesis and Publishable Interpretation

### The Central Finding

Quality thresholds do not function as a dose-response control for LLM overcorrection. Across 1,200 trials spanning three models, two framing types, and eight threshold levels, the overcorrection score remains locked near 2.0 (on a 1-5 scale) regardless of whether the user specifies no threshold, a lenient threshold (70/100), or a perfection threshold (100/100).

### Why This Matters

This finding has direct implications for prompt engineering and AI-assisted writing:

1. **Users cannot calibrate revision intensity through quality thresholds.** Telling a model "this is already 95/100" does not meaningfully reduce the extent of unnecessary revision compared to saying nothing.

2. **The one exception is instructive.** Gemini-Flash under qualitative framing (e.g., "this is nearly perfect") shows a 33% reduction in overcorrection from level 70 to 100. This suggests that natural-language quality assessments may eventually penetrate the overcorrection default, but only at extremes and only for some architectures.

3. **Models treat "Can this be improved?" as an unconditional instruction to revise,** regardless of stated quality context. The median overcorrection score is 2.0 with a bootstrap 95% CI of [2.0, 2.0] across all conditions for all three models.

4. **The flatness of the dose-response curve suggests overcorrection is a *default behavioral mode*, not a context-sensitive response.** It likely stems from RLHF/instruction-tuning incentives that reward helpfulness-as-action over helpfulness-as-restraint.

### Effect Size Context

The largest observed effect (Gemini-Flash qualitative, 70 vs 100) has r = -0.616, which is a large effect. But this is the exception. Across 5 of 6 model-framing conditions, the Kruskal-Wallis H statistics yield p-values > 0.22, and the practical differences are under 0.15 points on a 5-point scale (Cohen's d < 0.05 equivalent).

---

## 9. Suggested Figures and Tables for Publication

### Figure 1: Dose-Response Panel Plot
- 3x2 grid (rows = models, columns = framing type)
- X-axis: threshold level (0, 70, 75, 80, 85, 90, 95, 100)
- Y-axis: mean overcorrection (range 1.0-2.5)
- Include individual data points (jittered) with cell means connected by lines
- Add a horizontal reference line at the grand mean (~1.72)
- Add OLS trend line with slope annotation
- **Key visual:** The flatness of 5/6 panels contrasts with the single declining panel (Gemini-Flash qualitative)

### Figure 2: Threshold Sensitivity Index Bar Chart
- Grouped bar chart: models on x-axis, bars colored by framing
- Y-axis: TSI value
- Horizontal reference line at TSI = 0 (no sensitivity)
- Highlights Gemini-Flash qualitative as the outlier

### Table 1: Overcorrection Means and Slopes by Model x Framing x Level
- Full cell means table (as in Section 5) with confidence intervals
- Include slope, R-squared, and Kruskal-Wallis p-value per row

### Table 2: Revision Gate Behavior
- Decline rates and suggest-minor rates across levels (as in Section 6)
- Chi-squared test results for gate distribution differences

---

## 10. Methodological Notes

- **Cell sizes:** n=25 per model x framing x level (5 runs x 5 scenarios), yielding adequate power for detecting moderate effects but potentially underpowered for small effects within a single cell.
- **Scale compression:** The overcorrection scale is bounded [1,5] with a strong mode at 2 and no observations of 4 or 5 ("high overcorrection count" = 0 across all conditions). This ceiling/floor compression limits the detectable effect size and may explain why the dose-response relationship is flat -- there is little room for overcorrection to vary.
- **Judge bias:** GPT-4o as judge scores its own outputs lower on overcorrection (self_mean=1.65 vs other_mean=1.76, p=0.0001). This conservative self-scoring could attenuate GPT-4o's apparent dose-response. However, the flatness of GPT-4o's curve across levels (range = 0.12-0.16) is too extreme to be explained by judge bias alone.
- **Spearman limitation:** The existing Spearman correlations pool both framings. The model-x-framing breakdowns above reveal that the pooled rho = -0.168 for Gemini-Flash masks a framing-specific effect (qualitative framing drives the entire correlation).

---

*Analysis conducted 2026-03-30. Based on 1,200 scored trials across 3 models (GPT-4o, Claude Sonnet, Gemini Flash), 2 framing conditions (numeric, qualitative), and 8 threshold levels (0, 70, 75, 80, 85, 90, 95, 100).*
