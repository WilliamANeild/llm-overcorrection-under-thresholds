# Deep Analysis 1: Between-Model Comparison
============================================================

## Kruskal-Wallis: Overcorrection Across Models
  revision_magnitude: H=25.37, p=0.000003*
  revision_value: H=119.05, p=0.000000*
  threshold_alignment: H=16.19, p=0.000305*
  overcorrection: H=4.55, p=0.102561

## Pairwise Model Comparisons (overcorrection)
  claude-sonnet vs gemini-flash: U=326165.0, p_adj=0.120252, r=0.0497, means=1.45 vs 1.57
  claude-sonnet vs gpt-4o: U=333616.5, p_adj=0.404048, r=0.0361, means=1.45 vs 1.50
  gemini-flash vs gpt-4o: U=351258.5, p_adj=1.000000, r=-0.0161, means=1.57 vs 1.50

## Chi-Squared: Revision Gate by Model
  chi2=108.19, dof=4, p=0.000000
  Gate distribution:
    claude-sonnet: decline=30.3%, suggest_minor=31.2%, full_revision=38.5%
    gemini-flash: decline=50.7%, suggest_minor=15.1%, full_revision=34.2%
    gpt-4o: decline=36.0%, suggest_minor=31.5%, full_revision=32.5%

## Threshold Sensitivity Index: (OC@100 - OC@70) / OC@70
  claude-sonnet: OC@70=1.63, OC@100=1.20, TSI=-0.262
  gemini-flash: OC@70=1.86, OC@100=1.21, TSI=-0.349
  gpt-4o: OC@70=1.59, OC@100=1.45, TSI=-0.086

## Response Length by Model (Kruskal-Wallis)
  len_delta: H=498.57, p=0.000000
    claude-sonnet vs gemini-flash: U=202410.0, p_adj=0.000000*, r=0.4102
    claude-sonnet vs gpt-4o: U=483029.5, p_adj=0.000000*, r=-0.3956
    gemini-flash vs gpt-4o: U=534385.5, p_adj=0.000000*, r=-0.5459


# Deep Analysis 2: Framing Effects
============================================================

## Pooled Framing Effect (all models)
  revision_magnitude: numeric_mean=2.28, qual_mean=2.31, U=768708, p=0.703828, r=0.0084
  revision_value: numeric_mean=2.11, qual_mean=2.17, U=756918, p=0.285647, r=0.0236
  threshold_alignment: numeric_mean=4.34, qual_mean=4.55, U=697596, p=0.000001*, r=0.1001
  overcorrection: numeric_mean=1.60, qual_mean=1.40, U=859134, p=0.000000*, r=-0.1083

## Spearman: threshold vs overcorrection, by framing and model
  claude-sonnet | numeric: rho=-0.044, p=0.3678
  claude-sonnet | qualitative: rho=-0.198, p=0.0001*
  gemini-flash | numeric: rho=-0.180, p=0.0002*
  gemini-flash | qualitative: rho=-0.167, p=0.0008*
  gpt-4o | numeric: rho=-0.068, p=0.1542
  gpt-4o | qualitative: rho=-0.019, p=0.7004

## Framing Comparison at Each Threshold Level (pooled across models)
  Level 0: numeric_mean=1.56, qual_mean=1.57, p=0.9216, r=0.0054
  Level 70: numeric_mean=1.83, qual_mean=1.53, p=0.0112*, r=-0.1419
  Level 75: numeric_mean=1.72, qual_mean=1.49, p=0.0271*, r=-0.1252
  Level 80: numeric_mean=1.66, qual_mean=1.44, p=0.0361*, r=-0.1221
  Level 85: numeric_mean=1.71, qual_mean=1.45, p=0.0152*, r=-0.1448
  Level 90: numeric_mean=1.59, qual_mean=1.27, p=0.0002*, r=-0.2086
  Level 95: numeric_mean=1.38, qual_mean=1.22, p=0.0283*, r=-0.1132
  Level 100: numeric_mean=1.30, qual_mean=1.27, p=0.6108, r=-0.0267


# Deep Analysis 3: Threshold Dose-Response
============================================================

## Baseline (level=0) vs All Threshold Conditions (70-100)
  revision_magnitude: baseline_mean=2.23, threshold_mean=2.30, p=0.465676, r=0.0233
  revision_value: baseline_mean=2.06, threshold_mean=2.16, p=0.174559, r=0.0434
  threshold_alignment: baseline_mean=4.41, threshold_mean=4.45, p=0.425294, r=0.023
  overcorrection: baseline_mean=1.56, threshold_mean=1.50, p=0.272021, r=-0.0315

## Low (70-80) vs High (90-100) Threshold
  revision_magnitude: low_mean=2.24, high_mean=2.34, p=0.008237*, r=0.0676
  revision_value: low_mean=2.01, high_mean=2.28, p=0.000000*, r=0.1307
  threshold_alignment: low_mean=4.31, high_mean=4.61, p=0.000000*, r=0.1303
  overcorrection: low_mean=1.62, high_mean=1.34, p=0.000000*, r=-0.1377

## Per-Model Overcorrection Trend (mean OC at each level)
  claude-sonnet: slope=-0.00133, R²=0.0839, p=0.4865
    Means by level: {np.int64(0): np.float64(1.44), np.int64(70): np.float64(1.63), np.int64(75): np.float64(1.58), np.int64(80): np.float64(1.48), np.int64(85): np.float64(1.56), np.int64(90): np.float64(1.36), np.int64(95): np.float64(1.32), np.int64(100): np.float64(1.2)}
  gemini-flash: slope=-0.00327, R²=0.2075, p=0.2566
    Means by level: {np.int64(0): np.float64(1.65), np.int64(70): np.float64(1.86), np.int64(75): np.float64(1.7), np.int64(80): np.float64(1.71), np.int64(85): np.float64(1.62), np.int64(90): np.float64(1.47), np.int64(95): np.float64(1.27), np.int64(100): np.float64(1.21)}
  gpt-4o: slope=-0.00177, R²=0.3663, p=0.1118
    Means by level: {np.int64(0): np.float64(1.59), np.int64(70): np.float64(1.59), np.int64(75): np.float64(1.54), np.int64(80): np.float64(1.47), np.int64(85): np.float64(1.55), np.int64(90): np.float64(1.47), np.int64(95): np.float64(1.31), np.int64(100): np.float64(1.45)}

## Adjacent-Level Differences (looking for inflection points)
  claude-sonnet: 0->70: +0.183, 70->75: -0.045, 75->80: -0.101, 80->85: +0.080, 85->90: -0.200, 90->95: -0.040, 95->100: -0.120
  gemini-flash: 0->70: +0.208, 70->75: -0.155, 75->80: +0.008, 80->85: -0.093, 85->90: -0.150, 90->95: -0.200, 95->100: -0.060
  gpt-4o: 0->70: -0.006, 70->75: -0.044, 75->80: -0.071, 80->85: +0.079, 85->90: -0.080, 90->95: -0.160, 95->100: +0.140

## Revision Gate Distribution by Threshold Level
  Level 0: decline=39.1%, suggest_minor=28.7%, full_revision=32.2% (n=345)
  Level 70: decline=46.8%, suggest_minor=19.1%, full_revision=34.2% (n=325)
  Level 75: decline=44.8%, suggest_minor=19.9%, full_revision=35.3% (n=317)
  Level 80: decline=41.0%, suggest_minor=24.3%, full_revision=34.8% (n=305)
  Level 85: decline=37.3%, suggest_minor=25.0%, full_revision=37.7% (n=300)
  Level 90: decline=33.0%, suggest_minor=31.7%, full_revision=35.3% (n=300)
  Level 95: decline=31.0%, suggest_minor=33.3%, full_revision=35.7% (n=300)
  Level 100: decline=38.0%, suggest_minor=26.3%, full_revision=35.7% (n=300)


# Deep Analysis 4: Scenario Effects
============================================================

## Kruskal-Wallis: Overcorrection Across Scenarios
  H=186.86, p=0.000000
  claude-sonnet: H=62.78, p=0.000000*
  gemini-flash: H=25.18, p=0.000046*
  gpt-4o: H=146.73, p=0.000000*

## Pairwise Scenario Comparisons (overcorrection)
  brunch_cancellation vs client_sales_email: p_adj=0.000000*, r=0.3337, means=1.21 vs 1.73
  brunch_cancellation vs coworker_funny_text: p_adj=0.000000*, r=0.3362, means=1.21 vs 1.68
  brunch_cancellation vs linkedin_job_announcement: p_adj=0.000000*, r=0.2446, means=1.21 vs 1.60
  brunch_cancellation vs pto_request: p_adj=0.021569*, r=0.0824, means=1.21 vs 1.30
  client_sales_email vs pto_request: p_adj=0.000000*, r=-0.2664, means=1.73 vs 1.30
  coworker_funny_text vs pto_request: p_adj=0.000000*, r=-0.2635, means=1.68 vs 1.30
  linkedin_job_announcement vs pto_request: p_adj=0.000000*, r=-0.1755, means=1.60 vs 1.30
  (3 non-significant pairs omitted)

## Formality Analysis
  Formal mean=1.66, Informal mean=1.44
  Mann-Whitney (formal vs informal): U=569652, p=0.000000*, r=-0.1281

## Response Length by Scenario
  brunch_cancellation: turn2_mean=702, delta_mean=429
  client_sales_email: turn2_mean=1554, delta_mean=321
  coworker_funny_text: turn2_mean=532, delta_mean=275
  linkedin_job_announcement: turn2_mean=1076, delta_mean=180
  pto_request: turn2_mean=910, delta_mean=433

## Revision Gate by Scenario (Chi-Squared)
  chi2=513.95, dof=8, p=0.000000


# Deep Analysis 5: Interaction Effects
============================================================

## Model × Framing: Framing Effect Size by Model
  claude-sonnet: numeric_mean=1.55, qual_mean=1.33, r=-0.145, p=0.0000*
  gemini-flash: numeric_mean=1.68, qual_mean=1.45, r=-0.1013, p=0.0035*
  gpt-4o: numeric_mean=1.57, qual_mean=1.43, r=-0.0816, p=0.0180*

## Model × Threshold: Spearman rho per model
  claude-sonnet: rho=-0.1142, p=0.000986*
  gemini-flash: rho=-0.1788, p=0.000000*
  gpt-4o: rho=-0.0507, p=0.143331

## Overcorrection-Value Paradox (Spearman: OC vs revision_value)
  claude-sonnet: rho=0.515, p=0.000000*
  gemini-flash: rho=0.737, p=0.000000*
  gpt-4o: rho=0.709, p=0.000000*

## Sycophancy Signature: revision_magnitude × (5 - threshold_alignment)
  claude-sonnet: mean=1.68, median=0.0
  gemini-flash: mean=2.15, median=0.0
  gpt-4o: mean=2.01, median=0.0
  Kruskal-Wallis: H=11.19, p=0.003709

## Decline Behavior: Conditions with Most Declines
  Total declines: 972 / 2492 (39.0%)
  By model: {'gemini-flash': np.int64(420), 'gpt-4o': np.int64(301), 'claude-sonnet': np.int64(251)}
  By scenario: {'linkedin_job_announcement': np.int64(266), 'brunch_cancellation': np.int64(215), 'pto_request': np.int64(174), 'coworker_funny_text': np.int64(160), 'client_sales_email': np.int64(157)}
  By threshold: {70: np.int64(152), 75: np.int64(142), 0: np.int64(135), 80: np.int64(125), 100: np.int64(114), 85: np.int64(112), 90: np.int64(99), 95: np.int64(93)}
  By framing: {'numeric': np.int64(504), 'qualitative': np.int64(468)}
  By probe_type: {'pilot_c': np.int64(902), 'neutral': np.int64(49), 'pilot_b': np.int64(21)}

## Three-Way Outlier Cells (mean OC ≥ 1 SD above grand mean)
  Grand mean OC=1.51, SD=0.74, threshold=2.24
  (none)


# Deep Analysis 6: Probe Type Effects (Leading vs Neutral)
============================================================

## Pooled Probe Effect
  revision_magnitude: leading_mean=3.34, neutral_mean=1.02, U=59759, p=0.000000*, r=-0.992
  revision_value: leading_mean=3.00, neutral_mean=1.02, U=59790, p=0.000000*, r=-0.993
  threshold_alignment: leading_mean=4.01, neutral_mean=4.72, U=14901, p=0.000000*, r=0.5033
  overcorrection: leading_mean=1.93, neutral_mean=1.12, U=47409, p=0.000000*, r=-0.5803

## Per-Model Probe Effect (overcorrection)
  claude-sonnet: leading_mean=1.82, neutral_mean=1.00, r=-0.6175, p=0.000003*
  gemini-flash: leading_mean=2.13, neutral_mean=1.38, r=-0.4909, p=0.000426*
  gpt-4o: leading_mean=1.85, neutral_mean=1.00, r=-0.6375, p=0.000002*

## Revision Gate by Probe Type
  claude-sonnet:
    leading: decline=0.0%, suggest_minor=26.8%, full_revision=73.2%
    neutral: decline=100.0%, suggest_minor=0.0%, full_revision=0.0%
    pilot_a: decline=0.0%, suggest_minor=100.0%, full_revision=0.0%
    pilot_b: decline=50.0%, suggest_minor=50.0%, full_revision=0.0%
    pilot_c: decline=57.8%, suggest_minor=35.8%, full_revision=6.5%
  gemini-flash:
    leading: decline=0.0%, suggest_minor=29.2%, full_revision=70.8%
    neutral: decline=93.8%, suggest_minor=6.2%, full_revision=0.0%
    pilot_a: decline=0.0%, suggest_minor=100.0%, full_revision=0.0%
    pilot_b: decline=100.0%, suggest_minor=0.0%, full_revision=0.0%
    pilot_c: decline=99.8%, suggest_minor=0.2%, full_revision=0.0%
  gpt-4o:
    leading: decline=0.0%, suggest_minor=39.5%, full_revision=60.5%
    neutral: decline=100.0%, suggest_minor=0.0%, full_revision=0.0%
    pilot_a: decline=0.0%, suggest_minor=50.0%, full_revision=50.0%
    pilot_b: decline=100.0%, suggest_minor=0.0%, full_revision=0.0%
    pilot_c: decline=68.0%, suggest_minor=25.5%, full_revision=6.5%

## Decline Rate Comparison (leading vs neutral)
  claude-sonnet | leading: 0/400 declines (0.0%)
  claude-sonnet | neutral: 17/17 declines (100.0%)
  claude-sonnet | pilot_a: 0/6 declines (0.0%)
  claude-sonnet | pilot_b: 3/6 declines (50.0%)
  claude-sonnet | pilot_c: 231/400 declines (57.8%)
  gemini-flash | leading: 0/400 declines (0.0%)
  gemini-flash | neutral: 15/16 declines (93.8%)
  gemini-flash | pilot_a: 0/6 declines (0.0%)
  gemini-flash | pilot_b: 6/6 declines (100.0%)
  gemini-flash | pilot_c: 399/400 declines (99.8%)
  gpt-4o | leading: 0/400 declines (0.0%)
  gpt-4o | neutral: 17/17 declines (100.0%)
  gpt-4o | pilot_a: 0/6 declines (0.0%)
  gpt-4o | pilot_b: 12/12 declines (100.0%)
  gpt-4o | pilot_c: 272/400 declines (68.0%)

## Probe × Threshold: Does probe type moderate threshold sensitivity?
  claude-sonnet | leading: rho=-0.341, p=0.0000*
  claude-sonnet | neutral: rho=nan, p=nan
  claude-sonnet | pilot_a: rho=nan, p=nan
  claude-sonnet | pilot_b: rho=-0.200, p=0.7040
  claude-sonnet | pilot_c: rho=0.069, p=0.1688
  gemini-flash | leading: rho=-0.480, p=0.0000*
  gemini-flash | neutral: rho=0.227, p=0.3975
  gemini-flash | pilot_a: rho=-0.316, p=0.5415
  gemini-flash | pilot_b: rho=nan, p=nan
  gemini-flash | pilot_c: rho=-0.045, p=0.3702
  gpt-4o | leading: rho=-0.202, p=0.0000*
  gpt-4o | neutral: rho=nan, p=nan
  gpt-4o | pilot_a: rho=-0.707, p=0.1161
  gpt-4o | pilot_b: rho=nan, p=nan
  gpt-4o | pilot_c: rho=0.042, p=0.3969

## Per-Model Overcorrection Trend by Probe Type
  claude-sonnet | leading: slope=-0.00420, R²=0.1621, p=0.3227
  claude-sonnet | neutral: slope=0.00000, R²=nan, p=nan
  claude-sonnet | pilot_c: slope=0.00031, R²=0.0211, p=0.7315
  gemini-flash | leading: slope=-0.00834, R²=0.3311, p=0.1356
  gemini-flash | neutral: slope=0.01370, R²=0.2991, p=0.4531
  gemini-flash | pilot_c: slope=0.00012, R²=0.0114, p=0.8012
  gpt-4o | leading: slope=-0.00390, R²=0.3787, p=0.1044
  gpt-4o | neutral: slope=0.00000, R²=nan, p=nan
  gpt-4o | pilot_b: slope=0.00000, R²=nan, p=nan
  gpt-4o | pilot_c: slope=0.00011, R²=0.0072, p=0.8411

## Response Length Delta by Probe Type
  claude-sonnet | leading: delta_mean=270, ratio_mean=1.69
  claude-sonnet | neutral: delta_mean=130, ratio_mean=1.18
  claude-sonnet | pilot_a: delta_mean=-24, ratio_mean=0.96
  claude-sonnet | pilot_b: delta_mean=345, ratio_mean=1.49
  claude-sonnet | pilot_c: delta_mean=134, ratio_mean=1.58
  gemini-flash | leading: delta_mean=1321, ratio_mean=4.04
  gemini-flash | neutral: delta_mean=176, ratio_mean=1.34
  gemini-flash | pilot_a: delta_mean=1619, ratio_mean=3.09
  gemini-flash | pilot_b: delta_mean=259, ratio_mean=1.45
  gemini-flash | pilot_c: delta_mean=77, ratio_mean=1.84
  gpt-4o | leading: delta_mean=-5, ratio_mean=1.00
  gpt-4o | neutral: delta_mean=-220, ratio_mean=0.71
  gpt-4o | pilot_a: delta_mean=328, ratio_mean=1.46
  gpt-4o | pilot_b: delta_mean=60, ratio_mean=1.08
  gpt-4o | pilot_c: delta_mean=166, ratio_mean=1.39
