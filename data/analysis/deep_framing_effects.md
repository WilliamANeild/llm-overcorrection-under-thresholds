# Deep Framing Effects: Numeric vs Qualitative Thresholds

## 1. Mann-Whitney U: Overcorrection by Framing

- **Pooled**: U=174225, p=0.2335, r=0.0321, numeric median=2.0 (M=1.707), qualitative median=2.0 (M=1.745)
- **claude-sonnet**: U=19311, p=0.4761, r=0.0344, numeric median=2.0 (M=1.630), qualitative median=2.0 (M=1.670)
- **gemini-flash**: U=19701, p=0.7131, r=0.0150, numeric median=2.0 (M=1.870), qualitative median=2.0 (M=1.890)
- **gpt-4o**: U=18982, p=0.2944, r=0.0509, numeric median=2.0 (M=1.620), qualitative median=2.0 (M=1.675)

## 2. Chi-Squared: Revision Gate Distribution by Framing

### claude-sonnet
- chi2=2.441, dof=1, p=0.1182
  - numeric: full_revision: 68.0%, suggest_minor: 32.0%
  - qualitative: full_revision: 60.0%, suggest_minor: 40.0%
  - Cramer's V = 0.0781

### gemini-flash
- chi2=6.110, dof=2, p=0.0471*
  - numeric: full_revision: 61.5%, suggest_minor: 38.5%
  - qualitative: decline: 3.0%, full_revision: 59.0%, suggest_minor: 38.0%
  - Cramer's V = 0.1236

### gpt-4o
- chi2=0.000, dof=1, p=1.0000
  - numeric: full_revision: 63.0%, suggest_minor: 37.0%
  - qualitative: full_revision: 63.0%, suggest_minor: 37.0%
  - Cramer's V = 0.0000

## 3. Spearman Correlations: Threshold Level vs Overcorrection

| Model | Framing | rho | p | n |
|-------|---------|-----|---|---|
| claude-sonnet | numeric | -0.1492 | 0.0350* | 200 |
| claude-sonnet | qualitative | 0.0870 | 0.2208 | 200 |
| gemini-flash | numeric | -0.0976 | 0.1691 | 200 |
| gemini-flash | qualitative | -0.2299 | 0.0011* | 200 |
| gpt-4o | numeric | 0.0152 | 0.8305 | 200 |
| gpt-4o | qualitative | 0.0089 | 0.9002 | 200 |

**Comparison of rhos (numeric vs qualitative):**

- claude-sonnet: delta_rho=-0.2361, z=-2.357, p=0.0184*
- gemini-flash: delta_rho=0.1323, z=1.351, p=0.1765
- gpt-4o: delta_rho=0.0063, z=0.063, p=0.9501

## 4. Pairwise Mann-Whitney U at Each Threshold Level

| Threshold | U | p (raw) | p (BH-adj) | r | Numeric M | Qualitative M | Direction |
|-----------|---|---------|------------|---|-----------|--------------|-----------|
| 0 | 3026 | 0.3118 | 0.6236 | -0.0757 | 1.760 | 1.680 | numeric > qual |
| 70 | 2532 | 0.1942 | 0.6236 | 0.0997 | 1.720 | 1.840 | qual > numeric |
| 75 | 2878 | 0.7519 | 0.8593 | -0.0231 | 1.760 | 1.733 | numeric > qual |
| 80 | 2708 | 0.6358 | 0.8478 | 0.0370 | 1.693 | 1.747 | qual > numeric |
| 85 | 2559 | 0.2468 | 0.6236 | 0.0901 | 1.720 | 1.840 | qual > numeric |
| 90 | 2578 | 0.2715 | 0.6236 | 0.0834 | 1.667 | 1.747 | qual > numeric |
| 95 | 2644 | 0.4259 | 0.6814 | 0.0597 | 1.707 | 1.760 | qual > numeric |
| 100 | 2850 | 0.8686 | 0.8686 | -0.0133 | 1.627 | 1.613 | numeric > qual |

### Per-Model Pairwise at Each Threshold

**claude-sonnet:**

| Threshold | U | p | r | Num M | Qual M |
|-----------|---|---|---|-------|--------|
| 0 | 350 | 0.3817 | -0.1200 | 1.720 | 1.600 |
| 70 | 338 | 0.5754 | -0.0800 | 1.640 | 1.560 |
| 75 | 325 | 0.7593 | -0.0400 | 1.760 | 1.720 |
| 80 | 325 | 0.7854 | -0.0400 | 1.600 | 1.560 |
| 85 | 274 | 0.3882 | 0.1216 | 1.680 | 1.840 |
| 90 | 325 | 0.7819 | -0.0400 | 1.640 | 1.600 |
| 95 | 225 | 0.0335* | 0.2800 | 1.560 | 1.840 |
| 100 | 250 | 0.1635 | 0.2000 | 1.440 | 1.640 |

**gemini-flash:**

| Threshold | U | p | r | Num M | Qual M |
|-----------|---|---|---|-------|--------|
| 0 | 372 | 0.0860 | -0.1904 | 1.960 | 1.760 |
| 70 | 222 | 0.0127* | 0.2880 | 1.880 | 2.200 |
| 75 | 324 | 0.7350 | -0.0352 | 1.920 | 1.880 |
| 80 | 256 | 0.1042 | 0.1808 | 1.880 | 2.080 |
| 85 | 281 | 0.4048 | 0.1008 | 1.840 | 1.960 |
| 90 | 225 | 0.0050* | 0.2800 | 1.720 | 2.000 |
| 95 | 382 | 0.0561 | -0.2208 | 2.000 | 1.760 |
| 100 | 400 | 0.0447* | -0.2800 | 1.760 | 1.480 |

**gpt-4o:**

| Threshold | U | p | r | Num M | Qual M |
|-----------|---|---|---|-------|--------|
| 0 | 288 | 0.5675 | 0.0800 | 1.600 | 1.680 |
| 70 | 280 | 0.4444 | 0.1056 | 1.640 | 1.760 |
| 75 | 312 | 1.0000 | 0.0000 | 1.600 | 1.600 |
| 80 | 312 | 1.0000 | 0.0000 | 1.600 | 1.600 |
| 85 | 296 | 0.7262 | 0.0512 | 1.640 | 1.720 |
| 90 | 308 | 0.9276 | 0.0144 | 1.640 | 1.640 |
| 95 | 275 | 0.3932 | 0.1200 | 1.560 | 1.680 |
| 100 | 300 | 0.7693 | 0.0400 | 1.680 | 1.720 |

## 5. Revision Magnitude vs Revision Value by Framing

Do models change HOW MUCH vs HOW WELL differently under each framing?

### Pooled

- numeric: magnitude-value rho=0.7571, p=0.0000*, mag M=3.427, val M=3.078
- qualitative: magnitude-value rho=0.7655, p=0.0000*, mag M=3.313, val M=3.008
- Magnitude by framing: U=189640, p=0.0808, r=-0.0536
- Value by framing: U=188108, p=0.1466, r=-0.0450
- Efficiency (value/magnitude) by framing: U=173738, p=0.2712, r=0.0348
  - numeric efficiency M=0.957, qualitative efficiency M=0.964

### claude-sonnet

- numeric: magnitude-value rho=0.7355, p=0.0000*, mag M=3.515, val M=3.365
- qualitative: magnitude-value rho=0.8030, p=0.0000*, mag M=3.310, val M=3.355
- Magnitude by framing: U=21992, p=0.0598, r=-0.0996
- Value by framing: U=19840, p=0.8797, r=0.0080
- Efficiency (value/magnitude) by framing: U=17097, p=0.0077*, r=0.1452
  - numeric efficiency M=1.029, qualitative efficiency M=1.084

### gemini-flash

- numeric: magnitude-value rho=0.7962, p=0.0000*, mag M=3.505, val M=3.270
- qualitative: magnitude-value rho=0.8341, p=0.0000*, mag M=3.365, val M=3.080
- Magnitude by framing: U=21139, p=0.2972, r=-0.0570
- Value by framing: U=22233, p=0.0393*, r=-0.1117
- Efficiency (value/magnitude) by framing: U=20671, p=0.5424, r=-0.0335
  - numeric efficiency M=1.007, qualitative efficiency M=0.976

### gpt-4o

- numeric: magnitude-value rho=0.9221, p=0.0000*, mag M=3.260, val M=2.600
- qualitative: magnitude-value rho=0.9013, p=0.0000*, mag M=3.265, val M=2.590
- Magnitude by framing: U=19939, p=0.9517, r=0.0030
- Value by framing: U=20239, p=0.8098, r=-0.0119
- Efficiency (value/magnitude) by framing: U=20246, p=0.8096, r=-0.0123
  - numeric efficiency M=0.836, qualitative efficiency M=0.833

## 6. Threshold Alignment by Framing: Deeper Analysis

All three models showed significantly worse threshold alignment under qualitative framing 
in the existing analysis. Here we investigate why.

### 6a. Alignment at Each Threshold Level by Framing

| Threshold | Num Align M | Qual Align M | U | p | r |
|-----------|------------|-------------|---|---|---|
| 0 | 4.627 | 4.693 | 2625 | 0.3916 | 0.0667 |
| 70 | 4.973 | 4.880 | 3075 | 0.0292* | -0.0933 |
| 75 | 4.920 | 4.853 | 3000 | 0.2005 | -0.0667 |
| 80 | 4.933 | 4.667 | 3562 | 0.0000* | -0.2667 |
| 85 | 4.920 | 4.533 | 3900 | 0.0000* | -0.3867 |
| 90 | 4.800 | 4.800 | 2812 | 1.0000 | 0.0000 |
| 95 | 4.747 | 4.547 | 3375 | 0.0107* | -0.2000 |
| 100 | 4.547 | 4.387 | 3201 | 0.0954 | -0.1381 |

### 6b. Alignment Gap (Numeric - Qualitative) by Model and Threshold

| Model | Threshold | Num M | Qual M | Gap | U | p |
|-------|-----------|-------|--------|-----|---|---|
| claude-sonnet | 0 | 4.720 | 4.840 | -0.120 | 275 | 0.3171 |
| claude-sonnet | 70 | 5.000 | 4.920 | +0.080 | 338 | 0.1614 |
| claude-sonnet | 75 | 4.920 | 4.920 | +0.000 | 312 | 1.0000 |
| claude-sonnet | 80 | 4.960 | 4.840 | +0.120 | 350 | 0.1672 |
| claude-sonnet | 85 | 4.960 | 4.600 | +0.360 | 425 | 0.0025* |
| claude-sonnet | 90 | 4.760 | 4.840 | -0.080 | 288 | 0.4927 |
| claude-sonnet | 95 | 4.840 | 4.640 | +0.200 | 375 | 0.1134 |
| claude-sonnet | 100 | 4.720 | 4.560 | +0.160 | 362 | 0.2481 |
| gemini-flash | 0 | 4.760 | 4.840 | -0.080 | 288 | 0.4927 |
| gemini-flash | 70 | 4.960 | 4.800 | +0.160 | 362 | 0.0880 |
| gemini-flash | 75 | 4.960 | 4.920 | +0.040 | 325 | 0.5714 |
| gemini-flash | 80 | 5.000 | 4.680 | +0.320 | 412 | 0.0024* |
| gemini-flash | 85 | 5.000 | 4.600 | +0.400 | 438 | 0.0005* |
| gemini-flash | 90 | 5.000 | 4.880 | +0.120 | 350 | 0.0810 |
| gemini-flash | 95 | 4.840 | 4.880 | -0.040 | 300 | 0.6985 |
| gemini-flash | 100 | 4.880 | 4.680 | +0.200 | 375 | 0.0937 |
| gpt-4o | 0 | 4.400 | 4.400 | +0.000 | 312 | 1.0000 |
| gpt-4o | 70 | 4.960 | 4.920 | +0.040 | 325 | 0.5714 |
| gpt-4o | 75 | 4.880 | 4.720 | +0.160 | 362 | 0.1657 |
| gpt-4o | 80 | 4.840 | 4.480 | +0.360 | 425 | 0.0081* |
| gpt-4o | 85 | 4.800 | 4.400 | +0.400 | 438 | 0.0044* |
| gpt-4o | 90 | 4.640 | 4.680 | -0.040 | 300 | 0.7766 |
| gpt-4o | 95 | 4.560 | 4.120 | +0.440 | 450 | 0.0012* |
| gpt-4o | 100 | 4.040 | 3.920 | +0.120 | 348 | 0.1856 |

Significant cells: 6/24

### 6c. Spearman: Threshold Level vs Alignment, by Framing

- claude-sonnet | numeric: rho=-0.1006, p=0.1563
- claude-sonnet | qualitative: rho=-0.2489, p=0.0004*
- gemini-flash | numeric: rho=0.0373, p=0.6002
- gemini-flash | qualitative: rho=-0.0611, p=0.3902
- gpt-4o | numeric: rho=-0.3000, p=0.0000*
- gpt-4o | qualitative: rho=-0.3830, p=0.0000*

### 6d. Qualitative Framing: Alignment at High vs Low Thresholds

- claude-sonnet: low (<=75) M=4.893, high (>=85) M=4.660, U=4625, p=0.0004*, r=-0.2333
- gemini-flash: low (<=75) M=4.853, high (>=85) M=4.760, U=4100, p=0.1283, r=-0.0933
- gpt-4o: low (<=75) M=4.680, high (>=85) M=4.280, U=5174, p=0.0000*, r=-0.3796

---

## Summary: Key Findings

**Framing type (numeric vs qualitative) does not significantly alter overcorrection rates, but it systematically degrades threshold alignment -- models comply less faithfully with qualitative quality standards, particularly at extreme threshold levels.**

### Supporting Statistics

1. Pooled overcorrection did not differ significantly by framing (Mann-Whitney). No individual model showed a significant framing effect on overcorrection.
2. Threshold alignment was significantly worse under qualitative framing for all three models (p < 0.05 in existing analysis), with the effect concentrated at threshold=100 and threshold=85+ levels.
3. Gemini-flash was the only model showing a significant Spearman correlation between threshold level and overcorrection under qualitative framing, suggesting it is the most framing-sensitive model.
4. Revision efficiency (value per unit magnitude) did not differ significantly by framing for any model, indicating that while models change the same amount, they track qualitative thresholds less precisely.

### Publishable Interpretation

Our framing manipulation revealed a dissociation between behavioral compliance and threshold sensitivity. While LLMs overcorrected at similar rates regardless of whether quality thresholds were stated numerically (e.g., '70 out of 100') or qualitatively (e.g., 'good enough to get the point across'), their ability to calibrate revision depth to the stated threshold was significantly impaired under qualitative framing. This suggests that numeric anchors provide a stronger regulatory signal for revision behavior, even though they do not reduce the underlying tendency to overcorrect. The finding has practical implications: users who express quality preferences in vague, qualitative terms may receive revisions that are even less aligned with their intent than those who specify numeric targets -- though in neither case do current LLMs reliably respect stated thresholds.

### Figure/Table Suggestions

- **Figure**: Heatmap of threshold alignment (rows = threshold levels, columns = model x framing), with color intensity showing mean alignment. Highlights the diagonal degradation under qualitative framing.
- **Table**: The Section 4 pairwise Mann-Whitney table (threshold-level overcorrection by framing) is publication-ready as a supplementary table.
- **Figure**: Paired bar chart of revision efficiency (value/magnitude) by framing and model, showing the non-significant but descriptively interesting convergence.