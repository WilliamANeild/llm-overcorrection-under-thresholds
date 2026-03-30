# Deep Analysis 1: Between-Model Comparison
============================================================

## Kruskal-Wallis: Overcorrection Across Models
  revision_magnitude: H=53.04, p=0.000000*
  revision_value: H=319.07, p=0.000000*
  threshold_alignment: H=2.41, p=0.299170
  overcorrection: H=25.96, p=0.000002*

## Pairwise Model Comparisons (overcorrection)
  claude-sonnet vs gemini-flash: U=659529.0, p_adj=0.000256*, r=0.084, means=1.62 vs 1.81
  claude-sonnet vs gpt-4o: U=733392.0, p_adj=1.000000, r=-0.0186, means=1.62 vs 1.60
  gemini-flash vs gpt-4o: U=792282.0, p_adj=0.000007*, r=-0.1004, means=1.81 vs 1.60

## Chi-Squared: Revision Gate by Model
  chi2=110.11, dof=4, p=0.000000
  Gate distribution:
    claude-sonnet: decline=18.6%, suggest_minor=31.8%, full_revision=49.6%
    gemini-flash: decline=33.8%, suggest_minor=23.5%, full_revision=42.7%
    gpt-4o: decline=26.6%, suggest_minor=36.6%, full_revision=36.8%

## Threshold Sensitivity Index: (OC@100 - OC@70) / OC@70
  claude-sonnet: OC@70=1.85, OC@100=1.31, TSI=-0.295
  gemini-flash: OC@70=2.20, OC@100=1.21, TSI=-0.448
  gpt-4o: OC@70=1.69, OC@100=1.48, TSI=-0.123

## Response Length by Model (Kruskal-Wallis)
  len_delta: H=887.68, p=0.000000
    claude-sonnet vs gemini-flash: U=12319.0, p_adj=0.000000*, r=0.846
    claude-sonnet vs gpt-4o: U=153846.5, p_adj=0.000000*, r=-0.9231
    gemini-flash vs gpt-4o: U=155159.0, p_adj=0.000000*, r=-0.9395


# Deep Analysis 2: Framing Effects
============================================================

## Pooled Framing Effect (all models)
  revision_magnitude: numeric_mean=2.63, qual_mean=2.55, U=1678002, p=0.053079, r=-0.0358
  revision_value: numeric_mean=2.25, qual_mean=2.26, U=1618493, p=0.959813, r=0.0009
  threshold_alignment: numeric_mean=4.10, qual_mean=4.44, U=1355522, p=0.000000*, r=0.1633
  overcorrection: numeric_mean=1.80, qual_mean=1.56, U=1829211, p=0.000000*, r=-0.1291

## Spearman: threshold vs overcorrection, by framing and model
  claude-sonnet | numeric: rho=-0.143, p=0.0004*
  claude-sonnet | qualitative: rho=-0.163, p=0.0001*
  gemini-flash | numeric: rho=-0.306, p=0.0000*
  gemini-flash | qualitative: rho=-0.295, p=0.0000*
  gpt-4o | numeric: rho=-0.055, p=0.1773
  gpt-4o | qualitative: rho=-0.049, p=0.2338

## Framing Comparison at Each Threshold Level (pooled across models)
  Level 0: numeric_mean=1.81, qual_mean=1.71, p=0.2336, r=-0.0593
  Level 70: numeric_mean=2.07, qual_mean=1.76, p=0.0027*, r=-0.1496
  Level 75: numeric_mean=2.04, qual_mean=1.71, p=0.0003*, r=-0.1836
  Level 80: numeric_mean=1.88, qual_mean=1.65, p=0.0120*, r=-0.1257
  Level 85: numeric_mean=1.85, qual_mean=1.69, p=0.1578, r=-0.0711
  Level 90: numeric_mean=1.74, qual_mean=1.34, p=0.0000*, r=-0.2228
  Level 95: numeric_mean=1.64, qual_mean=1.30, p=0.0000*, r=-0.2135
  Level 100: numeric_mean=1.34, qual_mean=1.32, p=0.9961, r=0.0002


# Deep Analysis 3: Threshold Dose-Response
============================================================

## Baseline (level=0) vs All Threshold Conditions (70-100)
  revision_magnitude: baseline_mean=2.66, threshold_mean=2.58, p=0.387331, r=-0.0242
  revision_value: baseline_mean=2.24, threshold_mean=2.26, p=0.975815, r=0.0008
  threshold_alignment: baseline_mean=4.20, threshold_mean=4.28, p=0.009061*, r=0.0679
  overcorrection: baseline_mean=1.76, threshold_mean=1.67, p=0.016607*, r=-0.0626

## Low (70-80) vs High (90-100) Threshold
  revision_magnitude: low_mean=2.58, high_mean=2.56, p=0.994204, r=-0.0002
  revision_value: low_mean=2.15, high_mean=2.35, p=0.000006*, r=0.0961
  threshold_alignment: low_mean=4.05, high_mean=4.53, p=0.000000*, r=0.2108
  overcorrection: low_mean=1.85, high_mean=1.45, p=0.000000*, r=-0.2034

## Per-Model Overcorrection Trend (mean OC at each level)
  claude-sonnet: slope=-0.00200, R²=0.1272, p=0.3858
    Means by level: {np.int64(0): np.float64(1.65), np.int64(70): np.float64(1.85), np.int64(75): np.float64(1.75), np.int64(80): np.float64(1.72), np.int64(85): np.float64(1.71), np.int64(90): np.float64(1.5), np.int64(95): np.float64(1.49), np.int64(100): np.float64(1.31)}
  gemini-flash: slope=-0.00564, R²=0.2467, p=0.2106
    Means by level: {np.int64(0): np.float64(1.99), np.int64(70): np.float64(2.2), np.int64(75): np.float64(2.17), np.int64(80): np.float64(1.97), np.int64(85): np.float64(1.92), np.int64(90): np.float64(1.59), np.int64(95): np.float64(1.43), np.int64(100): np.float64(1.21)}
  gpt-4o: slope=-0.00124, R²=0.1814, p=0.2927
    Means by level: {np.int64(0): np.float64(1.64), np.int64(70): np.float64(1.69), np.int64(75): np.float64(1.71), np.int64(80): np.float64(1.59), np.int64(85): np.float64(1.69), np.int64(90): np.float64(1.53), np.int64(95): np.float64(1.49), np.int64(100): np.float64(1.48)}

## Adjacent-Level Differences (looking for inflection points)
  claude-sonnet: 0->70: +0.207, 70->75: -0.107, 75->80: -0.027, 80->85: -0.007, 85->90: -0.213, 90->95: -0.013, 95->100: -0.180
  gemini-flash: 0->70: +0.207, 70->75: -0.027, 75->80: -0.200, 80->85: -0.053, 85->90: -0.333, 90->95: -0.153, 95->100: -0.220
  gpt-4o: 0->70: +0.047, 70->75: +0.027, 75->80: -0.120, 80->85: +0.093, 85->90: -0.153, 90->95: -0.040, 95->100: -0.013

## Revision Gate Distribution by Threshold Level
  Level 0: decline=27.6%, suggest_minor=26.2%, full_revision=46.2% (n=450)
  Level 70: decline=28.0%, suggest_minor=29.8%, full_revision=42.2% (n=450)
  Level 75: decline=27.8%, suggest_minor=29.3%, full_revision=42.9% (n=450)
  Level 80: decline=26.7%, suggest_minor=31.3%, full_revision=42.0% (n=450)
  Level 85: decline=25.8%, suggest_minor=30.0%, full_revision=44.2% (n=450)
  Level 90: decline=24.7%, suggest_minor=32.0%, full_revision=43.3% (n=450)
  Level 95: decline=24.7%, suggest_minor=35.1%, full_revision=40.2% (n=450)
  Level 100: decline=25.6%, suggest_minor=31.3%, full_revision=43.1% (n=450)


# Deep Analysis 4: Scenario Effects
============================================================

## Kruskal-Wallis: Overcorrection Across Scenarios
  H=580.57, p=0.000000
  claude-sonnet: H=224.30, p=0.000000*
  gemini-flash: H=100.40, p=0.000000*
  gpt-4o: H=330.03, p=0.000000*

## Pairwise Scenario Comparisons (overcorrection)
  brunch_cancellation vs client_sales_email: p_adj=0.000000*, r=0.4523, means=1.22 vs 1.99
  brunch_cancellation vs coworker_funny_text: p_adj=0.000000*, r=0.441, means=1.22 vs 1.89
  brunch_cancellation vs linkedin_job_announcement: p_adj=0.000000*, r=0.4726, means=1.22 vs 1.99
  brunch_cancellation vs pto_request: p_adj=0.000034*, r=0.101, means=1.22 vs 1.32
  client_sales_email vs pto_request: p_adj=0.000000*, r=-0.3869, means=1.99 vs 1.32
  coworker_funny_text vs pto_request: p_adj=0.000000*, r=-0.3622, means=1.89 vs 1.32
  linkedin_job_announcement vs pto_request: p_adj=0.000000*, r=-0.4075, means=1.99 vs 1.32
  (3 non-significant pairs omitted)

## Formality Analysis
  Formal mean=1.99, Informal mean=1.55
  Mann-Whitney (formal vs informal): U=1308994, p=0.000000*, r=-0.2625

## Response Length by Scenario
  brunch_cancellation: turn2_mean=804, delta_mean=521
  client_sales_email: turn2_mean=1968, delta_mean=764
  coworker_funny_text: turn2_mean=567, delta_mean=297
  linkedin_job_announcement: turn2_mean=1370, delta_mean=489
  pto_request: turn2_mean=1098, delta_mean=619

## Revision Gate by Scenario (Chi-Squared)
  chi2=1269.72, dof=8, p=0.000000


# Deep Analysis 5: Interaction Effects
============================================================

## Model × Framing: Framing Effect Size by Model
  claude-sonnet: numeric_mean=1.77, qual_mean=1.48, r=-0.184, p=0.0000*
  gemini-flash: numeric_mean=1.96, qual_mean=1.66, r=-0.1428, p=0.0000*
  gpt-4o: numeric_mean=1.67, qual_mean=1.54, r=-0.0663, p=0.0241*

## Model × Threshold: Spearman rho per model
  claude-sonnet: rho=-0.1505, p=0.000000*
  gemini-flash: rho=-0.2989, p=0.000000*
  gpt-4o: rho=-0.0532, p=0.065335

## Overcorrection-Value Paradox (Spearman: OC vs revision_value)
  claude-sonnet: rho=0.471, p=0.000000*
  gemini-flash: rho=0.664, p=0.000000*
  gpt-4o: rho=0.550, p=0.000000*

## Sycophancy Signature: revision_magnitude × (5 - threshold_alignment)
  claude-sonnet: mean=2.46, median=0.0
  gemini-flash: mean=3.23, median=0.0
  gpt-4o: mean=2.49, median=0.0
  Kruskal-Wallis: H=3.86, p=0.144893

## Decline Behavior: Conditions with Most Declines
  Total declines: 948 / 3600 (26.3%)
  By model: {'gemini-flash': np.int64(406), 'gpt-4o': np.int64(319), 'claude-sonnet': np.int64(223)}
  By scenario: {'client_sales_email': np.int64(206), 'linkedin_job_announcement': np.int64(197), 'pto_request': np.int64(192), 'brunch_cancellation': np.int64(184), 'coworker_funny_text': np.int64(169)}
  By threshold: {70: np.int64(126), 75: np.int64(125), 0: np.int64(124), 80: np.int64(120), 85: np.int64(116), 100: np.int64(115), 95: np.int64(111), 90: np.int64(111)}
  By framing: {'qualitative': np.int64(495), 'numeric': np.int64(453)}
  By probe_type: {'neutral': np.int64(942), 'leading': np.int64(6)}

## Three-Way Outlier Cells (mean OC ≥ 1 SD above grand mean)
  Grand mean OC=1.68, SD=0.86, threshold=2.54
  (none)


# Deep Analysis 6: Probe Type Effects (Leading vs Neutral)
============================================================

## Pooled Probe Effect
  revision_magnitude: leading_mean=3.21, neutral_mean=1.34, U=2662416, p=0.000000*, r=-0.8489
  revision_value: leading_mean=2.73, neutral_mean=1.31, U=2635895, p=0.000000*, r=-0.8305
  threshold_alignment: leading_mean=3.99, neutral_mean=4.84, U=735665, p=0.000000*, r=0.4891
  overcorrection: leading_mean=1.96, neutral_mean=1.11, U=2227388, p=0.000000*, r=-0.5468

## Per-Model Probe Effect (overcorrection)
  claude-sonnet: leading_mean=1.82, neutral_mean=1.23, r=-0.4084, p=0.000000*
  gemini-flash: leading_mean=2.19, neutral_mean=1.06, r=-0.6649, p=0.000000*
  gpt-4o: leading_mean=1.88, neutral_mean=1.05, r=-0.5566, p=0.000000*

## Revision Gate by Probe Type
  claude-sonnet:
    leading: decline=0.0%, suggest_minor=36.0%, full_revision=64.0%
    neutral: decline=55.8%, suggest_minor=23.5%, full_revision=20.8%
  gemini-flash:
    leading: decline=0.8%, suggest_minor=35.2%, full_revision=64.0%
    neutral: decline=100.0%, suggest_minor=0.0%, full_revision=0.0%
  gpt-4o:
    leading: decline=0.0%, suggest_minor=45.1%, full_revision=54.9%
    neutral: decline=79.8%, suggest_minor=19.5%, full_revision=0.8%

## Decline Rate Comparison (leading vs neutral)
  claude-sonnet | leading: 0/800 declines (0.0%)
  claude-sonnet | neutral: 223/400 declines (55.8%)
  gemini-flash | leading: 6/800 declines (0.8%)
  gemini-flash | neutral: 400/400 declines (100.0%)
  gpt-4o | leading: 0/800 declines (0.0%)
  gpt-4o | neutral: 319/400 declines (79.8%)

## Probe × Threshold: Does probe type moderate threshold sensitivity?
  claude-sonnet | leading: rho=-0.260, p=0.0000*
  claude-sonnet | neutral: rho=0.097, p=0.0538
  gemini-flash | leading: rho=-0.457, p=0.0000*
  gemini-flash | neutral: rho=-0.134, p=0.0072*
  gpt-4o | leading: rho=-0.108, p=0.0021*
  gpt-4o | neutral: rho=-0.009, p=0.8563

## Per-Model Overcorrection Trend by Probe Type
  claude-sonnet | leading: slope=-0.00335, R²=0.1413, p=0.3588
  claude-sonnet | neutral: slope=0.00070, R²=0.2566, p=0.2002
  gemini-flash | leading: slope=-0.00843, R²=0.2789, p=0.1785
  gemini-flash | neutral: slope=-0.00004, R²=0.0001, p=0.9781
  gpt-4o | leading: slope=-0.00177, R²=0.1682, p=0.3128
  gpt-4o | neutral: slope=-0.00018, R²=0.0927, p=0.4634

## Response Length Delta by Probe Type
  claude-sonnet | leading: delta_mean=280, ratio_mean=1.70
  gemini-flash | leading: delta_mean=1332, ratio_mean=3.97
  gpt-4o | leading: delta_mean=1, ratio_mean=1.01
