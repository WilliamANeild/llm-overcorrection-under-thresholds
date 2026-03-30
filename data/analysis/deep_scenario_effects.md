# Deep Scenario Effects Analysis

> Auto-generated statistical report for the LLM overcorrection study.
> 5 scenarios x 3 models x 2 framings x 8 threshold levels = 1,200 trials.

---

## 1. Kruskal-Wallis: Overcorrection Across Scenarios

**Pooled Kruskal-Wallis: H(4) = 314.168, p = 0.000000, eta^2 = 0.2596**

| Scenario | Mean OC | Median OC | SD | N |
| --- | --- | --- | --- | --- |
| brunch_cancellation | 1.342 | 1.0 | 0.509 | 240 |
| client_sales_email | 1.913 | 2.0 | 0.311 | 240 |
| coworker_funny_text | 1.829 | 2.0 | 0.439 | 240 |
| linkedin_job_announcement | 2.000 | 2.0 | 0.289 | 240 |
| pto_request | 1.546 | 2.0 | 0.515 | 240 |

Interpretation: Significant differences in overcorrection across the five scenarios (p = 0.000000). Effect size eta^2 = 0.2596 (large).



### Per-Model Kruskal-Wallis

| Model | H-statistic | p-value | Effect Size |
| --- | --- | --- | --- |
| claude-sonnet | H(4) = 125.369 | p = 0.000000 | eta^2 = 0.3073 |
| gemini-flash | H(4) = 21.183 | p = 0.000291 | eta^2 = 0.0435 |
| gpt-4o | H(4) = 234.270 | p = 0.000000 | eta^2 = 0.5830 |


## 2. Pairwise Mann-Whitney U with Bonferroni Correction

| Comparison | U | p (raw) | p (Bonferroni) | Effect Size (r) | Sig. |
| --- | --- | --- | --- | --- | --- |
| brunch_cancellation vs client_sales_email | U = 12476 | 0.000000 | 0.000000 | r = 0.567 | *** |
| brunch_cancellation vs coworker_funny_text | U = 15152 | 0.000000 | 0.000000 | r = 0.474 | *** |
| brunch_cancellation vs linkedin_job_announcement | U = 10630 | 0.000000 | 0.000000 | r = 0.631 | *** |
| brunch_cancellation vs pto_request | U = 22860 | 0.000006 | 0.000057 | r = 0.206 | *** |
| client_sales_email vs coworker_funny_text | U = 31222 | 0.012757 | 0.127574 | r = -0.084 | ns |
| client_sales_email vs linkedin_job_announcement | U = 26385 | 0.001664 | 0.016637 | r = 0.084 | * |
| client_sales_email vs pto_request | U = 39272 | 0.000000 | 0.000000 | r = -0.364 | *** |
| coworker_funny_text vs linkedin_job_announcement | U = 24085 | 0.000001 | 0.000006 | r = 0.164 | *** |
| coworker_funny_text vs pto_request | U = 36674 | 0.000000 | 0.000000 | r = -0.273 | *** |
| linkedin_job_announcement vs pto_request | U = 41335 | 0.000000 | 0.000000 | r = -0.435 | *** |

**9 of 10 pairwise comparisons significant after Bonferroni correction.**

Suggestion: Present as a heatmap of pairwise effect sizes (rank-biserial r) with significance annotations.


## 3. Model x Scenario Interaction

### Mean Overcorrection by Model x Scenario

| Model | brunch_cancellation | client_sales_email | coworker_funny_text | linkedin_job_announcement | pto_request |
| --- | --- | --- | --- | --- | --- |
| claude-sonnet | 1.238 | 1.913 | 1.625 | 1.988 | 1.488 |
| gemini-flash | 1.750 | 1.925 | 1.962 | 1.988 | 1.775 |
| gpt-4o | 1.038 | 1.900 | 1.900 | 2.025 | 1.375 |

### Kruskal-Wallis on Models Within Each Scenario

| Scenario | H-statistic | p-value | Effect Size |
| --- | --- | --- | --- |
| brunch_cancellation | H(2) = 84.863 | p = 0.000000 | eta^2 = 0.3496 |
| client_sales_email | H(2) = 0.263 | p = 0.876863 | eta^2 = -0.0073 |
| coworker_funny_text | H(2) = 26.720 | p = 0.000002 | eta^2 = 0.1043 |
| linkedin_job_announcement | H(2) = 0.896 | p = 0.638825 | eta^2 = -0.0047 |
| pto_request | H(2) = 24.956 | p = 0.000004 | eta^2 = 0.0969 |

### Model Rank Variance Across Scenarios (higher = more inconsistent ranking)

  claude-sonnet: rank variance = 0.200, mean rank = 1.70

  gemini-flash: rank variance = 0.450, mean rank = 2.70

  gpt-4o: rank variance = 0.800, mean rank = 1.60



### Scheirer-Ray-Hare Test (non-parametric two-way ANOVA approximation)

| Factor | df | H | p-value |
| --- | --- | --- | --- |
| Model | 2 | 57.942 | 0.000000 |
| Scenario | 4 | 314.168 | 0.000000 |
| Model x Scenario | 8 | 83.811 | 0.000000 |

**Model x Scenario interaction: H(8) = 83.811, p = 0.000000. Significant interaction — models differ in how they overcorrect across tasks.**

Figure suggestion: Grouped bar chart or interaction plot (model x scenario) showing mean overcorrection with 95% CI error bars.


## 4. Scenario x Threshold Interaction

### Mean Overcorrection by Scenario x Threshold Level

| Scenario | 0 | 70 | 75 | 80 | 85 | 90 | 95 | 100 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| brunch_cancellation | 1.30 | 1.33 | 1.43 | 1.27 | 1.37 | 1.23 | 1.57 | 1.23 |
| client_sales_email | 1.97 | 2.00 | 1.97 | 1.97 | 1.97 | 1.97 | 1.83 | 1.63 |
| coworker_funny_text | 1.83 | 1.90 | 1.87 | 1.83 | 1.93 | 1.80 | 1.80 | 1.67 |
| linkedin_job_announcement | 1.97 | 2.07 | 1.90 | 2.00 | 2.17 | 2.00 | 1.93 | 1.97 |
| pto_request | 1.53 | 1.60 | 1.57 | 1.53 | 1.47 | 1.53 | 1.53 | 1.60 |

### Threshold Sensitivity: Spearman rho (threshold_level ~ overcorrection) per Scenario

| Scenario | Spearman rho | p-value | Sig. |
| --- | --- | --- | --- |
| brunch_cancellation | rho = 0.014 | p = 0.829694 | ns |
| client_sales_email | rho = -0.280 | p = 0.000011 | *** |
| coworker_funny_text | rho = -0.107 | p = 0.098364 | ns |
| linkedin_job_announcement | rho = -0.019 | p = 0.770847 | ns |
| pto_request | rho = -0.003 | p = 0.957617 | ns |



### Scheirer-Ray-Hare: Scenario x Threshold Interaction

**Scenario x Threshold interaction: H(28) = 26.344, p = 0.554136. Non-significant — threshold sensitivity is similar across scenarios.**

Most threshold-sensitive scenario: client_sales_email (rho = -0.280)

Least threshold-sensitive scenario: pto_request (rho = -0.003)

Figure suggestion: Line plot of mean overcorrection vs threshold level, one line per scenario, with shaded 95% CI bands.


## 5. Formality Analysis

### Descriptive Statistics by Formality

| Formality | Mean OC | Median OC | SD | N |
| --- | --- | --- | --- | --- |
| formal | 1.956 | 2.0 | 0.303 | 480 |
| informal | 1.585 | 2.0 | 0.533 | 480 |
| neutral | 1.546 | 2.0 | 0.514 | 240 |

**Formal vs Informal: U = 156831, p = 0.000000, rank-biserial r = -0.361. Significant difference.**

Three-group Kruskal-Wallis: H(2) = 186.201, p = 0.000000, eta^2 = 0.1539



### Formal vs Informal by Model

| Model | Mean Formal | Mean Informal | U | p-value | r | Sig. |
| --- | --- | --- | --- | --- | --- | --- |
| claude-sonnet | 1.950 | 1.431 | U = 19304 | p = 0.000000 | r = -0.508 | *** |
| gemini-flash | 1.956 | 1.856 | U = 14058 | p = 0.025233 | r = -0.098 | * |
| gpt-4o | 1.962 | 1.469 | U = 18950 | p = 0.000000 | r = -0.480 | *** |

Interpretation: Formal scenarios involve professionally-coded texts where LLMs may feel more license to 'improve'; informal scenarios have strong personal voice that models may be more reluctant to alter.

Figure suggestion: Violin plot of overcorrection by formality level, faceted by model.


## 6. Response Length Change (len_delta) by Scenario

**Kruskal-Wallis on len_delta: H(4) = 25.422, p = 0.000041, eta^2 = 0.0179**

| Scenario | Mean len_delta | Median len_delta | SD | N |
| --- | --- | --- | --- | --- |
| brunch_cancellation | 520.7 | 351.5 | 568.7 | 240 |
| client_sales_email | 763.7 | 253.0 | 1080.7 | 240 |
| coworker_funny_text | 296.6 | 110.0 | 391.1 | 240 |
| linkedin_job_announcement | 489.4 | 269.0 | 626.8 | 240 |
| pto_request | 619.3 | 299.0 | 747.7 | 240 |

### Spearman: len_delta ~ overcorrection by Scenario

| Scenario | Spearman rho | p-value | Sig. |
| --- | --- | --- | --- |
| brunch_cancellation | rho = 0.585 | p = 0.000000 | *** |
| client_sales_email | rho = 0.057 | p = 0.377108 | ns |
| coworker_funny_text | rho = 0.001 | p = 0.981600 | ns |
| linkedin_job_announcement | rho = -0.008 | p = 0.900351 | ns |
| pto_request | rho = 0.352 | p = 0.000000 | *** |

Interpretation: Large positive len_delta indicates the model substantially expanded the original text during revision. Scenarios with higher len_delta may reflect the model adding unsolicited content.

Figure suggestion: Box plot of len_delta by scenario, with individual data points overlaid (jittered strip plot).


## 7. Revision Gate by Scenario (Chi-Squared)

**Chi-squared test: chi2(8) = 527.102, p = 0.000000**

### Observed Counts

| Scenario | decline | full_revision | suggest_minor |
| --- | --- | --- | --- |
| brunch_cancellation | 1 | 36 | 203 |
| client_sales_email | 0 | 213 | 27 |
| coworker_funny_text | 4 | 213 | 23 |
| linkedin_job_announcement | 0 | 206 | 34 |
| pto_request | 1 | 81 | 158 |

### Proportion of full_revision by Scenario

| Scenario | Count | Proportion |
| --- | --- | --- |
| brunch_cancellation | 36/240 | 0.150 |
| client_sales_email | 213/240 | 0.887 |
| coworker_funny_text | 213/240 | 0.887 |
| linkedin_job_announcement | 206/240 | 0.858 |
| pto_request | 81/240 | 0.338 |

Cramer's V = 0.4686 (medium effect)

Interpretation: Tests whether models are more likely to gate (decline revision) for certain scenario types.

Figure suggestion: Stacked bar chart of revision_gate proportions by scenario.

