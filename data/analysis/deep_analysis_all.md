# Deep Analysis 1: Between-Model Comparison
============================================================

## Kruskal-Wallis: Overcorrection Across Models
  revision_magnitude: H=10.52, p=0.005197*
  revision_value: H=229.91, p=0.000000*
  threshold_alignment: H=111.56, p=0.000000*
  overcorrection: H=57.94, p=0.000000*

## Pairwise Model Comparisons (overcorrection)
  claude-sonnet vs gemini-flash: U=62718.0, p_adj=0.000000*, r=0.216, means=1.65 vs 1.88
  claude-sonnet vs gpt-4o: U=80268.5, p_adj=1.000000, r=-0.0034, means=1.65 vs 1.65
  gemini-flash vs gpt-4o: U=97497.5, p_adj=0.000000*, r=-0.2187, means=1.88 vs 1.65

## Chi-Squared: Revision Gate by Model
  chi2=12.76, dof=4, p=0.012524
  Gate distribution:
    claude-sonnet: decline=0.0%, suggest_minor=36.0%, full_revision=64.0%
    gemini-flash: decline=1.5%, suggest_minor=38.2%, full_revision=60.2%
    gpt-4o: decline=0.0%, suggest_minor=37.0%, full_revision=63.0%

## Threshold Sensitivity Index: (OC@100 - OC@70) / OC@70
  claude-sonnet: OC@70=1.60, OC@100=1.54, TSI=-0.038
  gemini-flash: OC@70=2.04, OC@100=1.62, TSI=-0.206
  gpt-4o: OC@70=1.70, OC@100=1.70, TSI=0.000

## Response Length by Model (Kruskal-Wallis)
  len_delta: H=887.68, p=0.000000
    claude-sonnet vs gemini-flash: U=12319.0, p_adj=0.000000*, r=0.846
    claude-sonnet vs gpt-4o: U=153846.5, p_adj=0.000000*, r=-0.9231
    gemini-flash vs gpt-4o: U=155159.0, p_adj=0.000000*, r=-0.9395


# Deep Analysis 2: Framing Effects
============================================================

## Pooled Framing Effect (all models)
  revision_magnitude: numeric_mean=3.43, qual_mean=3.31, U=189640, p=0.080825, r=-0.0536
  revision_value: numeric_mean=3.08, qual_mean=3.01, U=188108, p=0.146570, r=-0.045
  threshold_alignment: numeric_mean=4.81, qual_mean=4.67, U=204172, p=0.000000*, r=-0.1343
  overcorrection: numeric_mean=1.71, qual_mean=1.75, U=174225, p=0.233475, r=0.0321

## Spearman: threshold vs overcorrection, by framing and model
  claude-sonnet | numeric: rho=-0.149, p=0.0350*
  claude-sonnet | qualitative: rho=0.087, p=0.2208
  gemini-flash | numeric: rho=-0.098, p=0.1691
  gemini-flash | qualitative: rho=-0.230, p=0.0011*
  gpt-4o | numeric: rho=0.015, p=0.8305
  gpt-4o | qualitative: rho=0.009, p=0.9002

## Framing Comparison at Each Threshold Level (pooled across models)
  Level 0: numeric_mean=1.76, qual_mean=1.68, p=0.3118, r=-0.0757
  Level 70: numeric_mean=1.72, qual_mean=1.84, p=0.1942, r=0.0997
  Level 75: numeric_mean=1.76, qual_mean=1.73, p=0.7519, r=-0.0231
  Level 80: numeric_mean=1.69, qual_mean=1.75, p=0.6358, r=0.037
  Level 85: numeric_mean=1.72, qual_mean=1.84, p=0.2468, r=0.0901
  Level 90: numeric_mean=1.67, qual_mean=1.75, p=0.2715, r=0.0834
  Level 95: numeric_mean=1.71, qual_mean=1.76, p=0.4259, r=0.0597
  Level 100: numeric_mean=1.63, qual_mean=1.61, p=0.8686, r=-0.0133


# Deep Analysis 3: Threshold Dose-Response
============================================================

## Baseline (level=0) vs All Threshold Conditions (70-100)
  revision_magnitude: baseline_mean=3.65, threshold_mean=3.33, p=0.000678*, r=-0.1576
  revision_value: baseline_mean=3.17, threshold_mean=3.03, p=0.028389*, r=-0.1028
  threshold_alignment: baseline_mean=4.66, threshold_mean=4.75, p=0.015727*, r=0.0924
  overcorrection: baseline_mean=1.72, threshold_mean=1.73, p=0.953980, r=0.0024

## Low (70-80) vs High (90-100) Threshold
  revision_magnitude: low_mean=3.34, high_mean=3.30, p=0.558970, r=-0.0207
  revision_value: low_mean=2.95, high_mean=3.09, p=0.009109*, r=0.0938
  threshold_alignment: low_mean=4.87, high_mean=4.64, p=0.000000*, r=-0.2275
  overcorrection: low_mean=1.75, high_mean=1.69, p=0.074259, r=-0.0555

## Per-Model Overcorrection Trend (mean OC at each level)
  claude-sonnet: slope=-0.00028, R²=0.0125, p=0.7918
    Means by level: {np.int64(0): np.float64(1.66), np.int64(70): np.float64(1.6), np.int64(75): np.float64(1.74), np.int64(80): np.float64(1.58), np.int64(85): np.float64(1.76), np.int64(90): np.float64(1.62), np.int64(95): np.float64(1.7), np.int64(100): np.float64(1.54)}
  gemini-flash: slope=-0.00077, R²=0.0396, p=0.6365
    Means by level: {np.int64(0): np.float64(1.86), np.int64(70): np.float64(2.04), np.int64(75): np.float64(1.9), np.int64(80): np.float64(1.98), np.int64(85): np.float64(1.9), np.int64(90): np.float64(1.86), np.int64(95): np.float64(1.88), np.int64(100): np.float64(1.62)}
  gpt-4o: slope=0.00015, R²=0.0128, p=0.7894
    Means by level: {np.int64(0): np.float64(1.64), np.int64(70): np.float64(1.7), np.int64(75): np.float64(1.6), np.int64(80): np.float64(1.6), np.int64(85): np.float64(1.68), np.int64(90): np.float64(1.64), np.int64(95): np.float64(1.62), np.int64(100): np.float64(1.7)}

## Adjacent-Level Differences (looking for inflection points)
  claude-sonnet: 0->70: -0.060, 70->75: +0.140, 75->80: -0.160, 80->85: +0.180, 85->90: -0.140, 90->95: +0.080, 95->100: -0.160
  gemini-flash: 0->70: +0.180, 70->75: -0.140, 75->80: +0.080, 80->85: -0.080, 85->90: -0.040, 90->95: +0.020, 95->100: -0.260
  gpt-4o: 0->70: +0.060, 70->75: -0.100, 75->80: +0.000, 80->85: +0.080, 85->90: -0.040, 90->95: -0.020, 95->100: +0.080

## Revision Gate Distribution by Threshold Level
  Level 0: decline=0.0%, suggest_minor=29.3%, full_revision=70.7% (n=150)
  Level 70: decline=0.0%, suggest_minor=38.0%, full_revision=62.0% (n=150)
  Level 75: decline=0.0%, suggest_minor=39.3%, full_revision=60.7% (n=150)
  Level 80: decline=0.0%, suggest_minor=42.0%, full_revision=58.0% (n=150)
  Level 85: decline=0.0%, suggest_minor=36.0%, full_revision=64.0% (n=150)
  Level 90: decline=0.0%, suggest_minor=32.7%, full_revision=67.3% (n=150)
  Level 95: decline=2.0%, suggest_minor=43.3%, full_revision=54.7% (n=150)
  Level 100: decline=2.0%, suggest_minor=36.0%, full_revision=62.0% (n=150)


# Deep Analysis 4: Scenario Effects
============================================================

## Kruskal-Wallis: Overcorrection Across Scenarios
  H=314.17, p=0.000000
  claude-sonnet: H=125.37, p=0.000000*
  gemini-flash: H=21.18, p=0.000291*
  gpt-4o: H=234.27, p=0.000000*

## Pairwise Scenario Comparisons (overcorrection)
  brunch_cancellation vs client_sales_email: p_adj=0.000000*, r=0.5668, means=1.34 vs 1.91
  brunch_cancellation vs coworker_funny_text: p_adj=0.000000*, r=0.4739, means=1.34 vs 1.83
  brunch_cancellation vs linkedin_job_announcement: p_adj=0.000000*, r=0.6309, means=1.34 vs 2.00
  brunch_cancellation vs pto_request: p_adj=0.000057*, r=0.2063, means=1.34 vs 1.55
  client_sales_email vs linkedin_job_announcement: p_adj=0.016637*, r=0.0839, means=1.91 vs 2.00
  client_sales_email vs pto_request: p_adj=0.000000*, r=-0.3636, means=1.91 vs 1.55
  coworker_funny_text vs linkedin_job_announcement: p_adj=0.000006*, r=0.1637, means=1.83 vs 2.00
  coworker_funny_text vs pto_request: p_adj=0.000000*, r=-0.2734, means=1.83 vs 1.55
  linkedin_job_announcement vs pto_request: p_adj=0.000000*, r=-0.4352, means=2.00 vs 1.55
  (1 non-significant pairs omitted)

## Formality Analysis
  Formal mean=1.96, Informal mean=1.59
  Mann-Whitney (formal vs informal): U=156831, p=0.000000*, r=-0.3614

## Response Length by Scenario
  brunch_cancellation: turn2_mean=804, delta_mean=521
  client_sales_email: turn2_mean=1968, delta_mean=764
  coworker_funny_text: turn2_mean=567, delta_mean=297
  linkedin_job_announcement: turn2_mean=1370, delta_mean=489
  pto_request: turn2_mean=1098, delta_mean=619

## Revision Gate by Scenario (Chi-Squared)
  chi2=527.10, dof=8, p=0.000000


# Deep Analysis 5: Interaction Effects
============================================================

## Model × Framing: Framing Effect Size by Model
  claude-sonnet: numeric_mean=1.63, qual_mean=1.67, r=0.0344, p=0.4761
  gemini-flash: numeric_mean=1.87, qual_mean=1.89, r=0.015, p=0.7131
  gpt-4o: numeric_mean=1.62, qual_mean=1.68, r=0.0509, p=0.2944

## Model × Threshold: Spearman rho per model
  claude-sonnet: rho=-0.0304, p=0.544789
  gemini-flash: rho=-0.1676, p=0.000763*
  gpt-4o: rho=0.0123, p=0.806999

## Overcorrection-Value Paradox (Spearman: OC vs revision_value)
  claude-sonnet: rho=0.303, p=0.000000*
  gemini-flash: rho=0.431, p=0.000000*
  gpt-4o: rho=0.836, p=0.000000*

## Sycophancy Signature: revision_magnitude × (5 - threshold_alignment)
  claude-sonnet: mean=0.62, median=0.0
  gemini-flash: mean=0.55, median=0.0
  gpt-4o: mean=1.68, median=0.0
  Kruskal-Wallis: H=112.73, p=0.000000

## Decline Behavior: Conditions with Most Declines
  Total declines: 6 / 1200 (0.5%)
  By model: {'gemini-flash': np.int64(6)}
  By scenario: {'coworker_funny_text': np.int64(4), 'pto_request': np.int64(1), 'brunch_cancellation': np.int64(1)}
  By threshold: {95: np.int64(3), 100: np.int64(3)}
  By framing: {'qualitative': np.int64(6)}

## Three-Way Outlier Cells (mean OC ≥ 1 SD above grand mean)
  Grand mean OC=1.73, SD=0.49, threshold=2.21
  (none)
