# Deep Analysis 1: Between-Model Comparison
============================================================

## Kruskal-Wallis: Overcorrection Across Models
  revision_magnitude: H=39.60, p=0.000000*
  revision_value: H=192.91, p=0.000000*
  threshold_alignment: H=12.20, p=0.002247*
  overcorrection: H=8.18, p=0.016770*

## Pairwise Model Comparisons (overcorrection)
  claude-sonnet vs gemini-flash: U=824242.0, p_adj=0.170605, r=0.0372, means=1.48 vs 1.58
  claude-sonnet vs gpt-4o: U=876278.0, p_adj=1.000000, r=-0.0181, means=1.48 vs 1.46
  gemini-flash vs gpt-4o: U=906328.0, p_adj=0.016344*, r=-0.0539, means=1.58 vs 1.46

## Chi-Squared: Revision Gate by Model
  chi2=212.00, dof=4, p=0.000000
  Gate distribution:
    claude-sonnet: decline=31.9%, suggest_minor=26.9%, full_revision=41.3%
    gemini-flash: decline=50.5%, suggest_minor=13.1%, full_revision=36.4%
    gpt-4o: decline=35.6%, suggest_minor=34.5%, full_revision=29.9%

## Threshold Sensitivity Index: (OC@100 - OC@70) / OC@70
  claude-sonnet: OC@70=1.66, OC@100=1.26, TSI=-0.243
  gemini-flash: OC@70=1.87, OC@100=1.23, TSI=-0.346
  gpt-4o: OC@70=1.49, OC@100=1.41, TSI=-0.057

## Response Length by Model (Kruskal-Wallis)
  len_delta: H=567.14, p=0.000000
    claude-sonnet vs gemini-flash: U=568183.5, p_adj=0.000000*, r=0.3363
    claude-sonnet vs gpt-4o: U=1165261.5, p_adj=0.000000*, r=-0.3539
    gemini-flash vs gpt-4o: U=1255928.0, p_adj=0.000000*, r=-0.4604


# Deep Analysis 2: Framing Effects
============================================================

## Pooled Framing Effect (all models)
  revision_magnitude: numeric_mean=2.26, qual_mean=2.30, U=1895574, p=0.288743, r=0.0186
  revision_value: numeric_mean=2.08, qual_mean=2.18, U=1848080, p=0.013880*, r=0.0432
  threshold_alignment: numeric_mean=4.36, qual_mean=4.54, U=1769902, p=0.000000*, r=0.0837
  overcorrection: numeric_mean=1.59, qual_mean=1.42, U=2108076, p=0.000000*, r=-0.0914

## Spearman: threshold vs overcorrection, by framing and model
  claude-sonnet | numeric: rho=-0.068, p=0.0773
  claude-sonnet | qualitative: rho=-0.153, p=0.0001*
  gemini-flash | numeric: rho=-0.197, p=0.0000*
  gemini-flash | qualitative: rho=-0.172, p=0.0000*
  gpt-4o | numeric: rho=-0.034, p=0.3816
  gpt-4o | qualitative: rho=-0.006, p=0.8887

## Framing Comparison at Each Threshold Level (pooled across models)
  Level 0: numeric_mean=1.57, qual_mean=1.58, p=0.7983, r=0.0112
  Level 70: numeric_mean=1.80, qual_mean=1.54, p=0.0091*, r=-0.1165
  Level 75: numeric_mean=1.72, qual_mean=1.48, p=0.0036*, r=-0.1328
  Level 80: numeric_mean=1.66, qual_mean=1.44, p=0.0106*, r=-0.1179
  Level 85: numeric_mean=1.65, qual_mean=1.45, p=0.0190*, r=-0.11
  Level 90: numeric_mean=1.57, qual_mean=1.29, p=0.0000*, r=-0.1854
  Level 95: numeric_mean=1.43, qual_mean=1.27, p=0.0151*, r=-0.1033
  Level 100: numeric_mean=1.29, qual_mean=1.30, p=0.6898, r=0.0167


# Deep Analysis 3: Threshold Dose-Response
============================================================

## Baseline (level=0) vs All Threshold Conditions (70-100)
  revision_magnitude: baseline_mean=2.30, threshold_mean=2.28, p=0.746797, r=-0.0083
  revision_value: baseline_mean=2.09, threshold_mean=2.13, p=0.503795, r=0.0173
  threshold_alignment: baseline_mean=4.39, threshold_mean=4.45, p=0.136773, r=0.0349
  overcorrection: baseline_mean=1.58, threshold_mean=1.49, p=0.114139, r=-0.0368

## Low (70-80) vs High (90-100) Threshold
  revision_magnitude: low_mean=2.24, high_mean=2.31, p=0.009275*, r=0.0528
  revision_value: low_mean=2.01, high_mean=2.23, p=0.000000*, r=0.1137
  threshold_alignment: low_mean=4.33, high_mean=4.59, p=0.000000*, r=0.1212
  overcorrection: low_mean=1.61, high_mean=1.36, p=0.000000*, r=-0.1246

## Per-Model Overcorrection Trend (mean OC at each level)
  claude-sonnet: slope=-0.00155, R²=0.1500, p=0.3431
    Means by level: {np.int64(0): np.float64(1.5), np.int64(70): np.float64(1.66), np.int64(75): np.float64(1.58), np.int64(80): np.float64(1.49), np.int64(85): np.float64(1.54), np.int64(90): np.float64(1.4), np.int64(95): np.float64(1.38), np.int64(100): np.float64(1.26)}
  gemini-flash: slope=-0.00376, R²=0.2791, p=0.1783
    Means by level: {np.int64(0): np.float64(1.71), np.int64(70): np.float64(1.87), np.int64(75): np.float64(1.71), np.int64(80): np.float64(1.73), np.int64(85): np.float64(1.61), np.int64(90): np.float64(1.48), np.int64(95): np.float64(1.31), np.int64(100): np.float64(1.23)}
  gpt-4o: slope=-0.00115, R²=0.3512, p=0.1216
    Means by level: {np.int64(0): np.float64(1.51), np.int64(70): np.float64(1.49), np.int64(75): np.float64(1.52), np.int64(80): np.float64(1.43), np.int64(85): np.float64(1.51), np.int64(90): np.float64(1.41), np.int64(95): np.float64(1.36), np.int64(100): np.float64(1.41)}

## Adjacent-Level Differences (looking for inflection points)
  claude-sonnet: 0->70: +0.156, 70->75: -0.083, 75->80: -0.082, 80->85: +0.044, 85->90: -0.138, 90->95: -0.025, 95->100: -0.119
  gemini-flash: 0->70: +0.160, 70->75: -0.165, 75->80: +0.018, 80->85: -0.114, 85->90: -0.137, 90->95: -0.169, 95->100: -0.081
  gpt-4o: 0->70: -0.023, 70->75: +0.030, 75->80: -0.095, 80->85: +0.080, 85->90: -0.094, 90->95: -0.056, 95->100: +0.050

## Revision Gate Distribution by Threshold Level
  Level 0: decline=37.7%, suggest_minor=27.2%, full_revision=35.0% (n=525)
  Level 70: decline=46.3%, suggest_minor=18.6%, full_revision=35.0% (n=505)
  Level 75: decline=44.3%, suggest_minor=19.1%, full_revision=36.6% (n=497)
  Level 80: decline=43.3%, suggest_minor=19.8%, full_revision=36.9% (n=485)
  Level 85: decline=37.5%, suggest_minor=24.4%, full_revision=38.1% (n=480)
  Level 90: decline=34.0%, suggest_minor=31.2%, full_revision=34.8% (n=480)
  Level 95: decline=32.9%, suggest_minor=30.8%, full_revision=36.2% (n=480)
  Level 100: decline=37.9%, suggest_minor=28.1%, full_revision=34.0% (n=480)


# Deep Analysis 4: Scenario Effects
============================================================

## Kruskal-Wallis: Overcorrection Across Scenarios
  H=238.70, p=0.000000
  claude-sonnet: H=91.17, p=0.000000*
  gemini-flash: H=32.38, p=0.000035*
  gpt-4o: H=197.27, p=0.000000*

## Pairwise Scenario Comparisons (overcorrection)
  brunch_cancellation vs client_sales_email: p_adj=0.000000*, r=0.3337, means=1.21 vs 1.73
  brunch_cancellation vs coworker_funny_text: p_adj=0.000000*, r=0.3362, means=1.21 vs 1.68
  brunch_cancellation vs headphones_review: p_adj=0.000000*, r=0.331, means=1.21 vs 1.69
  brunch_cancellation vs linkedin_job_announcement: p_adj=0.000000*, r=0.2446, means=1.21 vs 1.60
  brunch_cancellation vs setup_instructions: p_adj=0.000000*, r=0.2086, means=1.21 vs 1.48
  brunch_cancellation vs slack_project_update: p_adj=0.000707*, r=0.1161, means=1.21 vs 1.35
  client_sales_email vs pto_request: p_adj=0.000000*, r=-0.2664, means=1.73 vs 1.30
  client_sales_email vs setup_instructions: p_adj=0.000332*, r=-0.1456, means=1.73 vs 1.48
  client_sales_email vs slack_project_update: p_adj=0.000000*, r=-0.2318, means=1.73 vs 1.35
  coworker_funny_text vs pto_request: p_adj=0.000000*, r=-0.2635, means=1.68 vs 1.30
  coworker_funny_text vs setup_instructions: p_adj=0.001493*, r=-0.1341, means=1.68 vs 1.48
  coworker_funny_text vs slack_project_update: p_adj=0.000000*, r=-0.2269, means=1.68 vs 1.35
  headphones_review vs pto_request: p_adj=0.000000*, r=-0.2617, means=1.69 vs 1.30
  headphones_review vs setup_instructions: p_adj=0.001018*, r=-0.1371, means=1.69 vs 1.48
  headphones_review vs slack_project_update: p_adj=0.000000*, r=-0.2261, means=1.69 vs 1.35
  linkedin_job_announcement vs pto_request: p_adj=0.000000*, r=-0.1755, means=1.60 vs 1.30
  linkedin_job_announcement vs slack_project_update: p_adj=0.000080*, r=-0.1415, means=1.60 vs 1.35
  pto_request vs setup_instructions: p_adj=0.000520*, r=0.1308, means=1.30 vs 1.48
  (10 non-significant pairs omitted)

## Formality Analysis
  Formal mean=1.66, Informal mean=1.44
  Mann-Whitney (formal vs informal): U=569652, p=0.000000*, r=-0.1281

## Response Length by Scenario
  brunch_cancellation: turn2_mean=702, delta_mean=429
  client_sales_email: turn2_mean=1554, delta_mean=321
  coworker_funny_text: turn2_mean=532, delta_mean=275
  headphones_review: turn2_mean=1134, delta_mean=-48
  linkedin_job_announcement: turn2_mean=1076, delta_mean=180
  pto_request: turn2_mean=910, delta_mean=433
  setup_instructions: turn2_mean=1508, delta_mean=-230
  slack_project_update: turn2_mean=709, delta_mean=146

## Revision Gate by Scenario (Chi-Squared)
  chi2=580.58, dof=14, p=0.000000


# Deep Analysis 5: Interaction Effects
============================================================

## Model × Framing: Framing Effect Size by Model
  claude-sonnet: numeric_mean=1.56, qual_mean=1.39, r=-0.1141, p=0.0000*
  gemini-flash: numeric_mean=1.70, qual_mean=1.47, r=-0.1047, p=0.0002*
  gpt-4o: numeric_mean=1.51, qual_mean=1.40, r=-0.0576, p=0.0331*

## Model × Threshold: Spearman rho per model
  claude-sonnet: rho=-0.1081, p=0.000090*
  gemini-flash: rho=-0.1878, p=0.000000*
  gpt-4o: rho=-0.0228, p=0.409151

## Overcorrection-Value Paradox (Spearman: OC vs revision_value)
  claude-sonnet: rho=0.533, p=0.000000*
  gemini-flash: rho=0.753, p=0.000000*
  gpt-4o: rho=0.675, p=0.000000*

## Sycophancy Signature: revision_magnitude × (5 - threshold_alignment)
  claude-sonnet: mean=1.72, median=0.0
  gemini-flash: mean=2.21, median=0.0
  gpt-4o: mean=1.81, median=0.0
  Kruskal-Wallis: H=3.85, p=0.145712

## Decline Behavior: Conditions with Most Declines
  Total declines: 1545 / 3932 (39.3%)
  By model: {'gemini-flash': np.int64(660), 'gpt-4o': np.int64(468), 'claude-sonnet': np.int64(417)}
  By scenario: {'linkedin_job_announcement': np.int64(266), 'brunch_cancellation': np.int64(215), 'slack_project_update': np.int64(212), 'headphones_review': np.int64(184), 'setup_instructions': np.int64(177), 'pto_request': np.int64(174), 'coworker_funny_text': np.int64(160), 'client_sales_email': np.int64(157)}
  By threshold: {70: np.int64(234), 75: np.int64(220), 80: np.int64(210), 0: np.int64(198), 100: np.int64(182), 85: np.int64(180), 90: np.int64(163), 95: np.int64(158)}
  By framing: {'numeric': np.int64(808), 'qualitative': np.int64(737)}
  By probe_type: {'pilot_c': np.int64(1474), 'neutral': np.int64(49), 'pilot_b': np.int64(21), 'leading': np.int64(1)}

## Three-Way Outlier Cells (mean OC ≥ 1 SD above grand mean)
  Grand mean OC=1.51, SD=0.72, threshold=2.23
  (none)


# Deep Analysis 6: Probe Type Effects (Leading vs Neutral)
============================================================

## Pooled Probe Effect
  revision_magnitude: leading_mean=3.33, neutral_mean=1.02, U=95639, p=0.000000*, r=-0.9925
  revision_value: leading_mean=2.96, neutral_mean=1.02, U=95658, p=0.000000*, r=-0.9929
  threshold_alignment: leading_mean=4.03, neutral_mean=4.72, U=23426, p=0.000000*, r=0.5119
  overcorrection: leading_mean=1.94, neutral_mean=1.12, U=76796, p=0.000000*, r=-0.5999

## Per-Model Probe Effect (overcorrection)
  claude-sonnet: leading_mean=1.88, neutral_mean=1.00, r=-0.6875, p=0.000000*
  gemini-flash: leading_mean=2.16, neutral_mean=1.38, r=-0.5125, p=0.000202*
  gpt-4o: leading_mean=1.78, neutral_mean=1.00, r=-0.6109, p=0.000003*

## Revision Gate by Probe Type
  claude-sonnet:
    leading: decline=0.0%, suggest_minor=19.8%, full_revision=80.2%
    neutral: decline=100.0%, suggest_minor=0.0%, full_revision=0.0%
    pilot_a: decline=0.0%, suggest_minor=100.0%, full_revision=0.0%
    pilot_b: decline=50.0%, suggest_minor=50.0%, full_revision=0.0%
    pilot_c: decline=62.0%, suggest_minor=33.8%, full_revision=4.2%
  gemini-flash:
    leading: decline=0.2%, suggest_minor=25.5%, full_revision=74.4%
    neutral: decline=93.8%, suggest_minor=6.2%, full_revision=0.0%
    pilot_a: decline=0.0%, suggest_minor=100.0%, full_revision=0.0%
    pilot_b: decline=100.0%, suggest_minor=0.0%, full_revision=0.0%
    pilot_c: decline=99.7%, suggest_minor=0.3%, full_revision=0.0%
  gpt-4o:
    leading: decline=0.0%, suggest_minor=43.9%, full_revision=56.1%
    neutral: decline=100.0%, suggest_minor=0.0%, full_revision=0.0%
    pilot_a: decline=0.0%, suggest_minor=50.0%, full_revision=50.0%
    pilot_b: decline=100.0%, suggest_minor=0.0%, full_revision=0.0%
    pilot_c: decline=68.6%, suggest_minor=26.6%, full_revision=4.8%

## Decline Rate Comparison (leading vs neutral)
  claude-sonnet | leading: 0/640 declines (0.0%)
  claude-sonnet | neutral: 17/17 declines (100.0%)
  claude-sonnet | pilot_a: 0/6 declines (0.0%)
  claude-sonnet | pilot_b: 3/6 declines (50.0%)
  claude-sonnet | pilot_c: 397/640 declines (62.0%)
  gemini-flash | leading: 1/640 declines (0.2%)
  gemini-flash | neutral: 15/16 declines (93.8%)
  gemini-flash | pilot_a: 0/6 declines (0.0%)
  gemini-flash | pilot_b: 6/6 declines (100.0%)
  gemini-flash | pilot_c: 638/640 declines (99.7%)
  gpt-4o | leading: 0/640 declines (0.0%)
  gpt-4o | neutral: 17/17 declines (100.0%)
  gpt-4o | pilot_a: 0/6 declines (0.0%)
  gpt-4o | pilot_b: 12/12 declines (100.0%)
  gpt-4o | pilot_c: 439/640 declines (68.6%)

## Probe × Threshold: Does probe type moderate threshold sensitivity?
  claude-sonnet | leading: rho=-0.352, p=0.0000*
  claude-sonnet | neutral: rho=nan, p=nan
  claude-sonnet | pilot_a: rho=nan, p=nan
  claude-sonnet | pilot_b: rho=-0.200, p=0.7040
  claude-sonnet | pilot_c: rho=0.113, p=0.0043*
  gemini-flash | leading: rho=-0.495, p=0.0000*
  gemini-flash | neutral: rho=0.227, p=0.3975
  gemini-flash | pilot_a: rho=-0.316, p=0.5415
  gemini-flash | pilot_b: rho=nan, p=nan
  gemini-flash | pilot_c: rho=-0.055, p=0.1624
  gpt-4o | leading: rho=-0.141, p=0.0003*
  gpt-4o | neutral: rho=nan, p=nan
  gpt-4o | pilot_a: rho=-0.707, p=0.1161
  gpt-4o | pilot_b: rho=nan, p=nan
  gpt-4o | pilot_c: rho=0.073, p=0.0636

## Per-Model Overcorrection Trend by Probe Type
  claude-sonnet | leading: slope=-0.00456, R²=0.2270, p=0.2326
  claude-sonnet | neutral: slope=0.00000, R²=nan, p=nan
  claude-sonnet | pilot_c: slope=0.00058, R²=0.0966, p=0.4536
  gemini-flash | leading: slope=-0.00876, R²=0.3793, p=0.1040
  gemini-flash | neutral: slope=0.01370, R²=0.2991, p=0.4531
  gemini-flash | pilot_c: slope=0.00006, R²=0.0051, p=0.8663
  gpt-4o | leading: slope=-0.00275, R²=0.3508, p=0.1219
  gpt-4o | neutral: slope=0.00000, R²=nan, p=nan
  gpt-4o | pilot_b: slope=0.00000, R²=nan, p=nan
  gpt-4o | pilot_c: slope=0.00045, R²=0.2059, p=0.2587

## Response Length Delta by Probe Type
  claude-sonnet | leading: delta_mean=236, ratio_mean=1.55
  claude-sonnet | neutral: delta_mean=130, ratio_mean=1.18
  claude-sonnet | pilot_a: delta_mean=-24, ratio_mean=0.96
  claude-sonnet | pilot_b: delta_mean=345, ratio_mean=1.49
  claude-sonnet | pilot_c: delta_mean=57, ratio_mean=1.40
  gemini-flash | leading: delta_mean=1191, ratio_mean=3.54
  gemini-flash | neutral: delta_mean=176, ratio_mean=1.34
  gemini-flash | pilot_a: delta_mean=1619, ratio_mean=3.09
  gemini-flash | pilot_b: delta_mean=259, ratio_mean=1.45
  gemini-flash | pilot_c: delta_mean=-151, ratio_mean=1.48
  gpt-4o | leading: delta_mean=-267, ratio_mean=0.99
  gpt-4o | neutral: delta_mean=-220, ratio_mean=0.71
  gpt-4o | pilot_a: delta_mean=328, ratio_mean=1.46
  gpt-4o | pilot_b: delta_mean=60, ratio_mean=1.08
  gpt-4o | pilot_c: delta_mean=63, ratio_mean=1.25
