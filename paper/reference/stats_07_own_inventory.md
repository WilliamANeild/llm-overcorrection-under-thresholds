# Statistics inventory and manuscript reconciliation

Compiled 2026-09-06. Read-only audit. Nothing was computed, re-run, or edited.

**Sources of truth used:** `results_FINAL.md` (Study 3 ledger, read in full),
`MOMENTUM_SUMMARY.md` (Study 2), `data/study3/analysis/revision_direction.json`
and `data/study3/analysis/study3_results.json` (computed JSON outputs).

**Live manuscript:** `paper/main.tex` inputs `sections/abstract_v2.tex`,
`introduction_v2.tex`, `related_work_v2.tex`, `methods.tex`, `results_v2.tex`,
`discussion.tex`, `conclusion.tex`, `appendix.tex`. `appendix.tex` in turn inputs
`sections/_fig1_appendix.tex`, so that file is live too. `abstract.tex`,
`introduction.tex`, `related_work.tex`, `results_OLD_DO_NOT_USE.tex.bak` and the
dot-prefixed `.bak` / `.bak2` files are not inputted and were excluded.

Values are quoted exactly as each location writes them. Where a ledger value and a
manuscript value differ only in rounding or in scientific-notation formatting, the
row is marked "match (rounded)" and the two forms are both shown.

---

## 1. Complete inventory of ledger statistics, with manuscript status

### Ledger §1 — Classifier

| Quantity | Value | Test | n | Effect size | CI | In manuscript? |
|---|---|---|---|---|---|---|
| GENUINE label count | 718 | — | 2,880 post-T1 obs | — | — | Yes. Methods §Response Classification, "(718/2,880)"; Results ¶Decline behavior, "(718/2,880)" |
| META label count | 2,162 | — | 2,880 | — | — | Only as complement: Conclusion "75\% of post-Turn~1 outputs are meta-responses"; Results "the remaining 86.7\% are meta-responses" (T5 only) |
| Genuine share of post-T1 outputs | 24.9% (derived 718/2,880) | — | 2,880 | — | — | Yes. Methods "24.9\%"; Results "only 24.9\%" |
| Manual corrections applied | 10 (GENUINE→META); 6 Llama, 2 DeepSeek, 1 Qwen, 1 Claude | — | — | — | — | Partly. Methods: "Ten classifications were manually corrected". Per-model breakdown not in paper |
| Correction rate | 10/718 = 1.4% | — | 718 | — | — | Yes. Methods "(1.4\% correction rate)" |
| Keyword-classifier balanced panel | 135 trials | — | 720 | — | — | Yes. Results ¶Decline behavior, "135 ``balanced panel'' trials" |
| LLM-classifier balanced panel | 50 trials | — | 720 | — | — | Yes. Results "yielding 50 balanced-panel trials"; Methods Edge Case Framework "The 50 trials (6.9\%)" |
| Classifier disagreement | 85 trials | — | — | — | — | Yes. Results "The 85-trial gap" |

### Ledger §2 — The cliff (balanced panel)

| Quantity | Value | Test | n | Effect size | CI | In manuscript? |
|---|---|---|---|---|---|---|
| Balanced-panel T1 mean | 3.66 | — | 50 | — | — | Yes. Results ¶The revision cliff; Fig. quality-trajectory caption |
| Balanced-panel T5 mean (unstripped) | 2.72 | — | 50 | — | — | **No** |
| Cliff delta (unstripped) | −0.94 | Wilcoxon signed-rank | 50 | r = 0.658 | — | Yes, value and p. Results ¶cliff and Table cliff, "($-0.94$, $p = 3.3 \times 10^{-6}$)"; Appendix Power Analysis, "$\Delta = 0.94$ unstripped ... $p = 3.32 \times 10^{-6}$ (Wilcoxon, $r = 0.658$)" |
| Cliff p (unstripped) | 3.32e-06 | Wilcoxon | 50 | — | — | Yes, as "$3.3 \times 10^{-6}$" (Results) and "$3.32 \times 10^{-6}$" (Appendix) |
| Cliff effect size (unstripped) | r = 0.658 | — | 50 | r = 0.658 | — | Yes, Appendix Power Analysis only |
| Llama cliff (unstripped) | T1 3.53, T5 2.71, Δ −0.82 | Wilcoxon | 45 | r = 0.639 | — | Delta and p yes (Table cliff, "($-0.82$, $p = 1.8 \times 10^{-5}$)"); T1/T5 means and r = 0.639 **no** |
| Llama cliff p | 1.81e-05 | Wilcoxon | 45 | — | — | Yes, as "$1.8 \times 10^{-5}$" |
| Qwen cliff | T1 5.00, T5 2.00, Δ −3.00 | none (n<5) | 3 | — | — | Delta yes: Results ¶Per-model caveats, "Qwen ($n = 3$, $\Delta = -3.00$)". Means no |
| Claude cliff | T1 4.50, T5 4.00, Δ −0.50 | none (n<5) | 2 | — | — | Delta yes: "Claude ($n = 2$, $\Delta = -0.50$)". Means no |
| GPT-4o / DeepSeek / Gemini balanced panel | 0 trials each | — | 0 | — | — | Yes. Results ¶Survival and ¶Per-model caveats |
| Stripped cliff, all | −0.76 (§2 table) / −0.74 (Stripped Sensitivity, "Balanced Panel Cliff") | — | 50 | — | — | **−0.74 only.** See mismatch M1 |
| Stripped cliff T5 mean | 2.92 | — | 50 | — | — | Yes. Results ¶cliff, "2.92 at Turn~5"; Fig. caption "(3.66$\to$2.92)" |
| Meta inflation, all | 0.18 (19%) with −0.76; "21\% smaller" with −0.74 | — | 50 | — | — | 21\% in Table cliff. 19\% not used. See M1 |
| Stripped cliff, Llama | −0.69 | — | 45 | — | — | Yes. Results ¶cliff table and ¶Per-model caveats |
| Meta inflation, Llama | 0.13 (16%) | — | 45 | — | — | Yes. Table cliff, "16\%" |
| Llama excl. near-trivial | −0.79 unstripped / −0.69 stripped | Wilcoxon | 39 | r = 0.628 | — | **No.** Disclosure not carried into the paper |
| Near-trivial edit disclosure | 6 of 45 trials >0.95 similarity; 4 character-identical | — | 45 | — | — | **No** |
| Revision-style similarity (Llama) | mean SequenceMatcher 0.50, median 0.51; other models 0.15–0.34 | — | — | — | — | **No** |
| Wholesale-rewrite drops | DeepSeek −1.71 (n=7 at T5), Qwen −3.00 (n=6), Llama −0.81 (n=64) | — | varies | — | — | **No** |

### Ledger §3 — Revision rate by turn

| Quantity | Value | Test | n | In manuscript? |
|---|---|---|---|---|
| T2 genuine rate | 283/720 = 39.3% | — | 720 | Yes. Results Table revision-rate; Results ¶Probe phrasing "39.3\% at Turn~2"; Intro "39\%" |
| T3 genuine rate | 185/720 = 25.7% | — | 720 | Yes. Table revision-rate |
| T4 genuine rate | 154/720 = 21.4% | — | 720 | Yes. Table revision-rate |
| T5 genuine rate | 96/720 = 13.3% | — | 720 | Yes. Table revision-rate; Results prose; Intro "13\%" |

### Ledger §4 — Revision despite sufficiency

| Quantity | Value | Test | n | Effect size | CI | In manuscript? |
|---|---|---|---|---|---|---|
| T1 sufficiency rate | 631/720 (87.6%) | — | 720 | — | — | Yes. Methods Edge Case Framework, "(87.6\%, after 6$\to$2 recode)" |
| Revision-despite-sufficiency | 368/938 = 39.2% | — | 938 sufficient turns | — | bootstrap 95% CI [36.1%, 42.3%] (1000 resamples, seed 42) | Yes. Results ¶Revision despite sufficiency, "39.2\% ... (368/938 sufficient turns, 95\% CI [36.1\%, 42.3\%]" |
| Bootstrap CI | [36.1%, 42.3%] | percentile bootstrap | 938 | — | — | Yes, but the resampling method is not named in the paper |

### Ledger §4b — Direction of revisions (added 2026-09-03)

| Quantity | Value | Test | n | Effect size | CI | In manuscript? |
|---|---|---|---|---|---|---|
| Overall stripped: worse / same / better | 199 (27.7%) / 432 (60.2%) / 87 (12.1%) | — | 718 | — | — | **No** |
| Movers, stripped | 286 | — | 718 | — | — | **No** |
| Share of movers worse, stripped | 69.6% | one-sided binomial sign test | 286 movers | — | Clopper-Pearson 95% [63.9%, 74.9%] | **Abstract only**, as "70\%": "Among the revisions that do change quality, 70\% lower it". No Results home |
| Sign p, stripped | 1.48e-11 | sign test | 286 | — | — | **No** |
| Overall unstripped worse/same/better | 245 (34.1%) / 398 (55.4%) / 75 (10.4%); movers 320; 76.6% worse | sign test | 718 | — | [71.5%, 81.1%] | **No** |
| Sign p, unstripped | 1.66e-22 | sign test | 718 | — | — | **No** |
| Per-model, stripped (6 rows) | gemini 8 / 100.0% / p 0.062; deepseek 31 / 85.7% / 0.0065; gpt-4o 40 / 80.0% / 0.0059; qwen 90 / 74.5% / 0.00031; llama 353 / 68.9% / 8.0e-06; claude 196 / 58.5% / 0.11 | sign test | 8–353 | — | — | **No** |
| Per-domain, stripped (5 rows) | writing 118 / 79.1% / 8.5e-05; creative 145 / 73.1% / 0.0006; code 196 / 67.0% / 0.00036; analysis 125 / 65.9% / 0.024; data_logic 134 / 65.9% / 0.024 | sign test | 118–196 | — | — | **No** (Abstract asserts "the pattern holds across all five domains" without the numbers) |
| Domain homogeneity | chi2 = 3.02, dof = 4, p = 0.555 | chi-square | 718 | — | — | **No** |
| Objectivity gradient, stripped | objective 98/49 = 66.7% worse; subjective 72/23 = 75.8% worse; Fisher p = 0.151 | Fisher exact | 242 movers | — | — | **No** |
| Objectivity gradient, unstripped | 109/44 = 71.2%; 94/18 = 83.9%; Fisher p = 0.019 | Fisher exact | — | — | — | **No** |
| Unstripped domain chi-square | p = 0.205 | chi-square | 718 | — | — | **No** |
| Registered-prediction outcome | objectivity-gradient prediction supported unstripped (0.019), not supported stripped (0.151) | — | — | — | — | **No.** Ledger marks this "BEARS ON A REGISTERED PREDICTION" and the second registered prediction not confirmed |
| Trial-level balanced panel, stripped | worse 52.0% / same 38.0% / better 10.0%; 26 vs 5; sign p 9.61e-05 | sign test | 50 | — | — | **No** |
| Trial-level balanced panel, unstripped | 62.0% / 30.0% / 8.0%; 31 vs 4; sign p 1.73e-06 | sign test | 50 | — | — | **No** |

Note on the ledger's own presentation: the §4b trial-level table heads its column
"movers" but prints "26 / 5" and "31 / 4", which are the worse/better counts, not the
mover totals (31 and 35 respectively per `revision_direction.json`). Reported, not
resolved.

### Ledger §5 and M2 — Targeted feedback

| Quantity | Value | Test | n | In manuscript? |
|---|---|---|---|---|
| Targeted mean, unstripped | 4.68 | — | 177 | Yes. Table targeted-feedback, "(4.68)" |
| Generic mean, unstripped | 4.43 | — | 177 | Yes. Table targeted-feedback, "(4.43)" |
| Delta, unstripped | +0.25 | Wilcoxon signed-rank | 177 | Yes. Results ¶targeted, "unstripped: $+0.25$, $p = 0.004$"; Table "($+0.25$)" |
| p, unstripped | 3.75e-03 | Wilcoxon | 177 | Yes, two forms: prose "$p = 0.004$", table "($3.8 \times 10^{-3}$)" |
| Targeted mean, stripped | 4.68 | — | 177 | Yes. Table targeted-feedback |
| Generic mean, stripped | 3.53 | — | 177 | Yes. Table; Fig. targeted-dumbbell caption |
| Delta, stripped | +1.16 | Wilcoxon | 177 | Yes. Results, Table, Fig. caption, Conclusion |
| p, stripped | 5.74e-19 | Wilcoxon | 177 | Yes, as "$5.7 \times 10^{-19}$" |
| Targeted-side meta prevalence | 9/177 = 5% | — | 177 | Yes. Results ¶targeted, "(9/177 = 5\%)" |
| Targeted mean shift under stripping | 4.68 → 4.63 | — | 177 | **No** |
| Per-model stripped: claude | 51, +0.31, p 0.012 | Wilcoxon | 51 | Yes, p as "$1.2 \times 10^{-2}$" |
| Per-model stripped: deepseek | 19, +1.05, p 0.012 | Wilcoxon | 19 | Yes, p as "$1.2 \times 10^{-2}$" |
| Per-model stripped: gemini | 3, +2.33, no test (n<5) | — | 3 | Yes, "-- ($n < 5$)" |
| Per-model stripped: gpt-4o | 12, +1.33, p 0.008 | Wilcoxon | 12 | Yes, but printed "$7.8 \times 10^{-3}$". See M3 |
| Per-model stripped: llama | 71, +1.62, p 9.2e-12 | Wilcoxon | 71 | Yes |
| Per-model stripped: qwen | 21, +1.48, p 4.5e-04 | Wilcoxon | 21 | Yes |
| Per-model unstripped (S14, 6 rows) | claude +0.51 p 0.004; deepseek +1.58 p 0.005; gemini +1.00 n<5; gpt-4o −0.17 p 0.750; llama −0.17 p 0.027; qwen +0.00 p 1.000 | Wilcoxon | 3–71 | **No** (paper says only "on unstripped text, only Claude and DeepSeek showed significant effects") |
| Superseded values | +2.00 (n=424); +0.79 (n=106, discarded as unverifiable) | — | — | Correctly absent |

### Ledger §6 and S7 — Revision tax

| Quantity | Value | n | In manuscript? |
|---|---|---|---|
| t* for all six models | T1 | 720 trials | Yes. Results ¶tax, Table revision-tax |
| Gemini tax / waste / $ | 30.6 / 23.4 / $0.0001 | 120 | Tax and waste yes (Table); $/task no |
| DeepSeek | 118.9 / 54.3 / $0.0005 | 120 | Tax and waste yes; $/task no |
| GPT-4o | 125.8 / 55.7 / $0.0053 | 120 | Tax and waste yes; $/task no |
| Qwen | 198.6 / 66.5 / $0.0009 | 120 | Tax and waste yes; $/task no |
| Claude | 251.6 / 71.6 / $0.0182 | 120 | Tax and waste yes; $/task no |
| Llama | 436.0 / 81.3 / $0.0013 | 120 | Tax and waste yes; $/task no |
| Aggregate waste fraction | 62.1% | 720 | Yes. Results, Table, Conclusion; Discussion as "62\%" |
| Aggregate tax | 164.2% | 720 | Yes. Results ¶tax and Table |
| Total wasted tokens | 653,070 | 720 | **No** |
| GPT-4o t* sensitivity | would be T5 without min_n floor (3 trials at T5, mean 4.0 vs T1 3.99 on n=120) | 120 | **No** |
| Pricing table | $0.40 / $0.55 / $0.88 / $0.90 / $10.00 / $15.00 per 1M output tokens | — | **No** as a table. The "roughly 37-fold spread" in Results is derived from it ($15.00/$0.40) |
| Enterprise annual projection | $323 (Gemini) to $65,678 (Claude); intermediate $1,969 / $3,250 / $4,680 / $18,972 | — | Endpoints only. Results ¶tax quotes "\$323" and "\$65{,}678"; the four intermediate models **no** |
| Monthly figures | $27 / $164 / $271 / $390 / $1,581 / $5,473 | — | **No** |
| Projection assumptions | 500 employees, 30 tasks/employee/day, 20 workdays/month | — | Partly: "for a 500-person organization". Tasks/day and workdays **no** |

### Ledger §7 — Reversibility (human annotation)

| Quantity | Value | Test | n | CI | In manuscript? |
|---|---|---|---|---|---|
| Liam T1-preferred | 19 (38%) | — | 50 | — | **No** |
| Troy T1-preferred | 22 (44%) | — | 50 | — | **No** |
| Combined T1-preferred | 41 (41%) | — | 100 | — | **No** as a share of all judgments |
| Revision-preferred | Liam 13 (26%), Troy 19 (38%), combined 32 (32%) | — | — | — | **No** |
| Ties | Liam 18 (36%), Troy 9 (18%), combined 27 (27%) | — | — | — | **No** |
| Non-tie T1-preference | Liam 19/32 (59.4%), Troy 22/41 (53.7%), **combined 41/73 (56.2%)** | — | 73 | bootstrap 95% [45.2%, 67.1%] | Combined only. **Methods** ¶Reversibility, "56.2\% of non-tie decisions (41/73, 95\% CI [45.2\%, 67.1\%])"; Discussion Limitations as "56\%". Per-annotator **no**. Not in Results |
| Pre-committed bar | ≥65% with CI excluding 50%; NOT CLEARED | — | — | — | Yes. Methods ¶Reversibility; Discussion Limitations "a pre-set success bar of 65\% that was not cleared" |
| Raw 3-way agreement | 40/50 (80%) | — | 50 | — | **No** |
| Cohen's kappa (raw) | 0.703 | Cohen's κ, 3-way labels | 50 | — | Yes. Methods ¶Reversibility, "$\kappa = 0.703$ ($n = 50$)". Test not named as Cohen's there |
| Cohen's kappa (decoded) | 0.701 | Cohen's κ | 50 | — | **No** |
| Disagreement composition | 10 pairs (8 Liam-tie vs Troy-decided, 1 full flip, 1 Liam-tie vs Troy-T1) | — | 50 | — | **No** |
| Position bias | A chosen 38/73 (52.1%), CI [39.7%, 63.0%] | — | 73 | [39.7%, 63.0%] | **No** |
| Length bias | longer output chosen 40/73 (54.8%) | — | 73 | — | **No** |
| Model judge, unstripped, same 50 pairs | 45/49 (91.8%) T1-pref, 1 tie | — | 49 | — | **No** |
| Model judge, unstripped, full 720 | 669/720 (92.9%) | — | 720 | — | **No** |
| Model judge, stripped, 50 pairs | 26/46 (56.5%), 4 ties | — | 46 | — | **No** |
| Liam vs judge | n 31, 77.4%, κ 0.541 | Cohen's κ | 31 | — | **No** |
| Troy vs judge | n 39, 79.5%, κ 0.589 | Cohen's κ | 39 | — | **No** |
| Human majority vs judge | n 30, 80.0%, κ 0.595 | Cohen's κ | 30 | — | **No** |
| All pooled vs judge | n 70, 78.6%, **κ 0.569** | Cohen's κ | 70 | — | Kappa yes. Methods ¶Meta-Commentary Stripping, "$\kappa = 0.569$". n = 70 and the 78.6% agreement **no** |
| Unstripped human-judge kappa | −0.07 to +0.02 | Cohen's κ | — | — | Yes. Methods, "($\kappa$ between $-0.07$ and $+0.02$)" |

### Ledger §8 — Meta-wrapping asymmetry

| Quantity | Value | n | In manuscript? |
|---|---|---|---|
| Revision side: preamble | 38/50 (76%) | 50 | **No** |
| Revision side: postamble | 24/50 (48%) | 50 | **No** |
| Revision side: either | 42/50 (84%) | 50 | Yes. Methods ¶Meta-Commentary Stripping, "84\% of revision-side outputs" |
| T1: preamble | 4/50 (8%) | 50 | **No** |
| T1: postamble | 5/50 (10%) | 50 | **No** |
| T1: either | 7/50 (14%) | 50 | Yes. Methods, "compared to 14\% of Turn~1 outputs" |
| Per-turn meta prevalence | T1 14%, T2 92%, T3 85%, T4 79%, T5 68% | — | **No.** Ledger carries a FLAG that this breakdown needs scope verification before citing. Correctly not cited |
| Judge inflation attributable to asymmetry | 56.5% → 91.8% on the same 50 pairs | 50 | **No numerically.** Discussion states the two-directional bias qualitatively only |

### Ledger §9 — Reversibility, stratified

| Quantity | Value | n | In manuscript? |
|---|---|---|---|
| By last revision turn | T2 9/17 (52.9%); T3 11/21 (52.4%); T4 17/24 (70.8%); T5 4/11 (36.4%) | 73 | **No** |
| By domain | writing 13/14 (92.9%); analysis 8/12 (66.7%); code 9/20 (45.0%); creative 8/19 (42.1%); data_logic 3/8 (37.5%) | 73 | **No** |

### Ledger §10 — Self-reflection

| Quantity | Value | n | In manuscript? |
|---|---|---|---|
| Mean recommended turn | 2.44 (SD = 1.39) | 720 | **No** |
| Recommend T1 | 288/720 (40.0%) | 720 | **No** |
| Recommend not-last | 90.7% | 720 | **No** |
| Distribution | T1 288, T2 76, T3 176, T4 113, T5 67 | 720 | **No** |

Methods ¶Self-Reflection describes the sub-experiment and states "$n = 720$", but no
self-reflection result is reported anywhere in the paper.

### Ledger §11 — Reliability

| Quantity | Value | Test | n | In manuscript? |
|---|---|---|---|---|
| Liam–Troy QW kappa | 0.406 | quadratic-weighted Cohen's κ | 64 | Yes. Appendix Table human-agreement; Methods as range "0.406 to 0.603" |
| Liam–Sophie QW kappa | 0.578 | QW Cohen's κ | 64 | Yes. Appendix Table human-agreement |
| Sophie–Troy QW kappa | 0.603 | QW Cohen's κ | 64 | Yes. Appendix Table human-agreement |
| Liam–Troy binary / within-1 | 49/64 (76.6%) / 52/64 (81.2%) | — | 64 | Yes. Appendix Table |
| Liam–Sophie binary / within-1 | 50/64 (78.1%) / 61/64 (95.3%) | — | 64 | Yes. Appendix Table |
| Sophie–Troy binary / within-1 | 53/64 (82.8%) / 56/64 (87.5%) | — | 64 | Yes. Appendix Table |
| Krippendorff's alpha | 0.529 | interval-scale α, 3 raters | 3 × 64 | Yes. Methods; Appendix Table; Discussion Limitations |
| Judge–human Spearman | 0.505 (p<0.001) | Spearman | 64 | Yes. Methods ¶Judge Calibration; Appendix Table judge-calibration; Discussion Limitations |
| Judge–human QW kappa | 0.526 | QW Cohen's κ | 64 | Yes, same three places |
| Superseded Liam–Troy kappa | 0.228 (linear-weighted, raw 1–6) | — | 64 | Correctly absent |

### Ledger §12 — Unchanged numbers

| Quantity | Value | In manuscript? |
|---|---|---|
| Study 1 trial count | 3,840 | Yes. Methods ¶Study 1; Appendix §Study 1; Appendix pipeline figure |
| Study 1 gate | 99.9% vs 23.2% | Yes. Methods; Results ¶Probe phrasing; Appendix |
| Study 2 trial count | 1,728 | Yes. Methods ¶Study 2; Appendix §Study 2 |
| Self-reflection mean | 2.44 | **No** |
| T1 sufficiency | 87.6% | Yes. Methods Edge Case Framework |
| Edit ratio | 0.97 (superseded by S4: 0.61) | **No** |

### Ledger S1–S14 — Secondary numbers

| Quantity | Value | Test | n | In manuscript? |
|---|---|---|---|---|
| S1 word-count slope, GENUINE-only | +19.4/turn (p = 1.9e-8) | t-test on per-trial slopes | 356 | **No** |
| S1 word count T1→T5 | 289 → 341 | — | 356 | **No** |
| S1 char count T1→T5 | 1980 → 2426 | — | 356 | **No** |
| S2 total_structure by turn | T1 12.52 (n 720), T2 10.34 (283), T5 9.00 (96) | — | varies | **No** |
| S2 T1→T5 structural drop | 28.1% | — | — | **No** |
| S3 constraint recall slope | +0.002 (p = 0.58, NS) | per-trial polyfit slope | 356 | **No** |
| S3 >10% recall drop T1→T5 | 17.7% (17/96) | — | 96 | **No** |
| S3 recall T1 / T5 | 0.491 / 0.483 | — | — | **No** |
| S4 edit ratio, GENUINE-only | 0.61 | SequenceMatcher on consecutive GENUINE turns | — | **No.** Methods defines an "Edit ratio" metric but reports no value |
| S4 semantic drift T1→T5 | 0.54 → 0.48 | — | 205 | **No.** Methods defines "Semantic similarity" but reports no value |
| S4 drift slope | −0.038 (p = 3.0e-21) | per-trial polyfit | 205 | **No** |
| S5 survival to T5 | llama 64/120 (53.3%); claude 15/120 (12.5%); deepseek 7/120 (5.8%); qwen 6/120 (5.0%); gpt-4o 3/120 (2.5%); gemini 1/120 (0.8%) | — | 120 each | Partly. Results ¶Survival quotes only the endpoints, "0.8\% (Gemini~2.5 Flash: 1/120 trials) to 53.3\% (Llama~3.3~70B: 64/120)". The four middle models **no** (Fig. survival-curves plots them) |
| S5 DRP by model | claude T2 (T1 4.28); gpt-4o T2 (3.99); llama T2 (3.75); qwen T2 (4.35); deepseek T3 (4.48); gemini — (n<5) | — | — | **No.** Methods defines DRP and calls it a "key" analysis; no DRP value is reported |
| S6 LOCF T1 / T5 / delta | 4.11 / 3.60 / −0.51 (p = 1.0e-32) | Wilcoxon paired | 720 | **No** |
| S6 LOCF stripped | T5 3.81, delta −0.30 (p = 3.8e-18) | Wilcoxon paired | 720 | **No** |
| S8 T1 sufficiency discrepancy | 672/720 (93.3%) raw vs 631/720 (87.6%) recoded; 41 trials differ | — | 720 | Only the resolved value, 87.6%, appears. The 93.3% and the 41-trial explanation **no** |
| S9 pooled trajectory, unstripped | T1 4.11 / T2 3.25 / T3 3.01 / T4 2.97 / T5 2.85; Δ −1.26 | — | 720/283/185/154/96 | Yes. Results Table pooled-trajectory, parenthesized column |
| S9 pooled trajectory, stripped | T1 4.11 / T2 3.66 / T3 3.40 / T4 3.34 / T5 3.07; Δ −1.04 | — | same | Yes. Results Table pooled-trajectory, primary column, and shifts +0.41/+0.39/+0.37/+0.22 |
| S10 domain deltas, unstripped | analysis −1.21 (17); code −1.15 (30); creative −1.22 (19); data_logic −1.35 (17); writing −1.31 (13) | — | 13–30 at T5 | Yes. Results Table domain-variation, parenthesized column |
| S10 domain T1/T5 means | analysis 3.98/2.76; code 3.95/2.80; creative 4.12/2.89; data_logic 4.35/3.00; writing 4.16/2.85 | — | — | **No** |
| S11 level-6 rate, unstripped | T1 5.7% (41/720); T2 33.9% (96/283); T3 42.2% (78/185); T4 42.9% (66/154); T5 47.9% (46/96) | — | varies | Endpoints only. Results ¶Over-elaboration, "from 5.7\% at T1 to 47.9\% at T5". T2–T4 **no** |
| S11 level-6 rate, stripped | T1 5.6%; T2 18.0%; T3 28.6%; T4 27.9%; T5 34.4% | — | varies | T5 only, "(34.4\% after meta-commentary stripping)" |

### Ledger M1–M6 — Stripped sensitivity analysis

| Quantity | Value | n | In manuscript? |
|---|---|---|---|
| Stripping scope by turn | T1 69/720 (9.6%); T2 361/720 (50.1%); T3 282/720 (39.2%); T4 278/720 (38.6%); T5 210/720 (29.2%) | 3,600 | **No** per turn |
| Stripping scope, total | 1,200/3,600 (33.3%) | 3,600 | Yes. Methods ¶Meta-Commentary Stripping, "1,200 (33.3\%)" |
| M1 sufficient turns unstripped / stripped | 938 / 1,038 | — | Yes. Results ¶Revision despite sufficiency, "368/938" and "411/1,038" |
| M1 revised-despite rate | 39.2% / 39.6% | — | Yes, both |
| M5 domain deltas, stripped | analysis −1.16; code −1.05; creative −0.82; data_logic −1.01; writing −1.06 | 13–30 | Yes. Results Table domain-variation, primary column, plus shifts +0.05/+0.10/+0.40/+0.34/+0.25 |
| M6 level-6 shifts | −0.1 / −15.9 / −13.5 / −15.0 / −13.5 pp | — | **No** |
| Summary "what moves, what holds" table | 8 rows | — | **No** as a table; its content is carried in prose |

### `MOMENTUM_SUMMARY.md` — Study 2

| Quantity | Value | Test | n | In manuscript? |
|---|---|---|---|---|
| New momentum trials | 1,728 (plus 1,920 cold baseline from Study 1) | — | — | Trial count yes; the 1,920 cold baseline **no** |
| Cold vs warm revision rate | 23.2% vs 44.6% | chi-squared = 376.54, p < 0.0001 | 3,648 | Yes. Appendix §Study 2, "($\chi^2 = 376.54$, $p < 0.0001$)" |
| GPT-4o dose 0→1→2→3 | 31.4 / 98.4 / 99.5 / 97.4% | — | — | Doses 0 and 1 yes ("31.4\% $\to$ 98.4\%"). Doses 2–3 **no** |
| Claude dose 0→1→2→3 | 38.0 / 38.0 / 27.1 / 24.5% | — | — | Doses 0 and 3 yes ("38.0\% $\to$ 24.5\%"). Doses 1–2 **no** |
| Gemini dose 0→1→2→3 | 0.3 / 12.8 / 9.9 / 8.6% | — | — | Doses 0 and 1 yes. Doses 2–3 **no** |
| RQ5 dose-response | Spearman rho = 0.199, p < 0.0001 | Spearman | — | **No** |
| Full revision rate by dose | 3.0 / 22.1 / 26.2 / 24.0% | — | — | **No** |
| RQ6 logistic regression | dose beta = 0.28 (p < 0.0001); threshold p = 0.39; dose × threshold p = 0.51 | logistic | — | Interaction p only. Appendix "($p = 0.51$)". Beta and threshold main effect **no** |
| Overcorrection under momentum | Kruskal-Wallis H = 213.76, p < 0.0001 | Kruskal-Wallis | — | **No** |
| Overcorrection means by dose | 1.09 / 1.25 / 1.31 / 1.33 (of 5), medians 1.0 throughout | — | — | **No** |

---

## 2. Gap list — in the ledger, absent from every live section

Ranked by how much weight the paper's own claims put on the missing number.

| Rank | Statistic | Ledger location | Why it is load-bearing |
|---|---|---|---|
| 1 | The entire direction-of-revisions analysis: 69.6% of movers worse, sign p 1.48e-11, CI [63.9%, 74.9%], n = 718, plus its six per-model and five per-domain rows | §4b | The abstract's only result statistic ("70\% lower it") and its domain claim ("holds across all five domains") both come from here, and the ledger names §4b "the basis for the paper's headline claim as of 2026-09-03". Results reports none of it. The abstract currently states a finding the body never establishes |
| 2 | Model-judge vs human reversibility on the same 50 pairs: 91.8% unstripped vs 56.5% stripped; 92.9% on the full 720 | §7, §8; ledger claims N1/N2 | The Discussion asserts the judge is biased "in two opposing directions at once" and that "leaving it uncontrolled changes the conclusion" (Introduction). Neither statement carries a number anywhere in the paper. This is the ledger's designated methods contribution |
| 3 | Reversibility as a Results finding: 41/73 = 56.2%, κ = 0.703, CI [45.2%, 67.1%], the ≥65% bar, and the per-annotator splits | §7 | The abstract's closing clause ("blind readers prefer it ... only slightly more often than chance") rests on it. It appears only in Methods and one Limitations sentence. There is no Results subsection on reversibility |
| 4 | The objectivity-gradient registered prediction: Fisher p = 0.151 stripped vs 0.019 unstripped; the ledger flags it as the second registered prediction the corrected analysis does not confirm | §4b | A pre-registered prediction that failed is not reported anywhere. The paper reports the failed 65% reversibility bar but not this one |
| 5 | DRP per model (all T2 except DeepSeek T3, Gemini undetermined) | S5 | Methods defines DRP and names it one of the two analyses the binary threshold "drives", then never reports a value |
| 6 | Self-reflection results: mean 2.44 (SD 1.39), 40.0% recommend T1, 90.7% recommend not-last | §10 | Methods describes the sub-experiment and gives its n; the paper reports no outcome. A model that recommends T1 40% of the time is direct evidence for the stopping-point argument in the Discussion |
| 7 | LOCF trajectory: T1 4.11 → T5 3.60, Δ −0.51 (p 1.0e-32); stripped Δ −0.30 (p 3.8e-18), n = 720 | S6, M3 | The only whole-sample (n=720) paired quality test in the ledger. It answers the selection-bias objection the paper raises against its own balanced panel and pooled trajectory, and is dropped |
| 8 | Reversibility stratified by last revision turn and by domain | §9 | Would substantiate the "consistent across task domains" claim in the Conclusion on the human-judgment side |
| 9 | Position and length bias checks: A chosen 38/73 (52.1%) CI [39.7%, 63.0%]; longer chosen 40/73 (54.8%) | §7 | Design validity for the blind pairwise task the paper relies on |
| 10 | Meta-wrapping components: preamble 38/50, postamble 24/50; T1 4/50 and 5/50 | §8 | The paper gives only the "either" totals (84% / 14%) |
| 11 | Content-drift reversals: word-count slope flips to +19.4/turn; constraint recall slope goes NS at +0.002; edit ratio 0.61; structural drop 28.1% | S1–S4 | Methods defines "Semantic similarity" and "Edit ratio" as metrics and reports neither. These are the ledger's corrections of four claims the old draft made |
| 12 | Total wasted tokens 653,070; the six-model pricing table; the four intermediate enterprise projections | §6, S7 | Supporting detail for the cost paragraph |
| 13 | Study 2: Spearman rho = 0.199, Kruskal-Wallis H = 213.76, logistic dose beta = 0.28, dose-2/3 rates, overcorrection means by dose | MOMENTUM_SUMMARY | Appendix reports the chi-squared and the interaction p only; the dose-response test itself is absent |
| 14 | Llama near-trivial-edit sensitivity (n=39, −0.79 unstripped, p 8.69e-05, r 0.628) and the revision-style similarity disclosure | §2 disclosures | Both are ledger-marked audit disclosures; neither is carried into the paper |
| 15 | Stripping scope per turn (9.6% / 50.1% / 39.2% / 38.6% / 29.2%) | Stripped Sensitivity | Only the 33.3% total is given |
| 16 | Level-6 rates at T2–T4 and their stripped shifts | S11, M6 | Endpoints only in Results |
| 17 | Per-model unstripped targeted-feedback table (S14) | S14 | Results asserts "only Claude and DeepSeek showed significant effects" without the numbers |
| 18 | S8 T1-sufficiency reconciliation: 672/720 (93.3%) vs 631/720 (87.6%), 41 trials | S8 | Only the adopted value appears; a reader cannot see why 93.3% was dropped |

---

## 3. Mismatch list — the same quantity with a different value, n, or test

These are correctness problems. Both locations are quoted verbatim.

| # | Quantity | Ledger says | Manuscript says | Manuscript location | Nature |
|---|---|---|---|---|---|
| **M1** | Stripped balanced-panel cliff, and its meta share | Two values coexist. §2 "Stripped Cliff" table: "All (n=50) \| -0.94 \| **-0.76** \| 0.18 (19%)". Stripped Sensitivity "Balanced Panel Cliff": "T1 3.66, T5 2.92, **Delta -0.74**, 21% smaller" | "$-0.74$" throughout, paired with meta share "21\%" in Table~\ref{tab:cliff} | results_v2 ¶The revision cliff, Table cliff, Fig. quality-trajectory caption, Conclusion, Appendix Power Analysis | The paper picks one of two ledger values without saying so in print. Its own source comment (results_v2 lines 235–238, "FLAG 2") records the choice, but a LaTeX comment is invisible to readers. The same table then pairs a full-3,600-rescore row (−0.74 / 21%) with a 50-pair-rescore row (Llama −0.69 / 16%) under one header |
| **M2** | Quality level reached at Turn 5 | Stripped T5 mean = 2.92 on a scale where 2 = "Incomplete", 3 = "Functional" | "a decline of $-0.74$ levels ... This is a drop from between ``Functional'' and ``Sufficient'' to **below ``Incomplete.''**" | results_v2 ¶The revision cliff | 2.92 is *above* Incomplete (2) and just below Functional (3). The scale statement is wrong in the paper's own terms (Methods lists the six levels). Reported as written; the intended phrase is presumably "to below Functional" |
| **M3** | Targeted-feedback p for GPT-4o | "gpt-4o \| 12 \| +1.33 \| **0.008**" (M2 per-model table) | "$7.8 \times 10^{-3}$" | results_v2 Table targeted-per-model | The manuscript states two significant figures the ledger does not carry. 0.008 is consistent with anything from 0.0075 to 0.0085; 7.8e-3 asserts more precision than the source of truth supports. Same pattern, lower stakes, for Claude and DeepSeek ("0.012" → "$1.2 \times 10^{-2}$") |
| **M4** | Provenance date of the API pricing | "based on 2025 output-token prices (Qwen/Llama via Together.ai)"; the pricing table is labeled "Real 2025 API pricing" | Results: "at 2025 API prices". Ethics Statement: "Pricing data is sourced from publicly available API documentation and subscription pages **as of June 2026**" | results_v2 ¶tax; main.tex Ethics Statement | The paper dates the same pricing to two different years in two places, one of which contradicts the ledger |
| **M5** | Whether the effect holds in all five domains | §4b: all five domains individually significant on the sign test (0.024 to 8.5e-05); domain homogeneity chi2 = 3.02, p = 0.555, "The asymmetry does not differ by domain". S10/M5 report per-domain deltas with **no p-values at all** | Abstract: "the pattern holds across all five domains". Results: "four of five reach significance on paired Wilcoxon tests ($p < 0.05$; data\_logic is marginal at $p = 0.058$)" | abstract_v2; results_v2 ¶Domain variation | Two different quantities (direction of revisions vs. size of the T1–T5 delta) are both reported as "the pattern by domain", and they disagree on the count. A reader meets "all five" in the abstract and "four of five" in Results. Separately, the Wilcoxon p-values behind "four of five" and the "$p = 0.058$" are not in the ledger (see orphan O3) |
| **M6** | Scope label on the meta-wrapping counts | §8 Scope: "All counts are from the **50 unstripped reversibility pairs**, stored in `meta_wrapping_asymmetry.json`" | "In our **50 balanced-panel pairs**, 84\% of revision-side outputs contain at least one such wrapper" | methods.tex ¶Meta-Commentary Stripping | Same n and, on the ledger's own account of how the pairs were built, probably the same 50 trials. The two names are not stated anywhere to be the same set. Flagged as unresolved rather than corrected |
| **M7** | Study 1 sample size | §12: "Study 1: 3,840 trials" | Methods and Appendix: "3,840 trials". Results: "Across five probe wordings tested in Study~1 (3 models; $n = 3{,}932$" | methods.tex ¶Study 1 vs results_v2 ¶Probe phrasing | Two Study 1 Ns in one paper. The 92-trial difference reconciles arithmetically against the five per-probe Ns in that sentence (1,920+18+1,920+24+50 = 3,932), i.e. the factorial 3,840 plus 92 pilot trials, but the paper never says so and the ledger carries only 3,840 |

---

## 4. Orphan list — in the manuscript, not traceable to the ledger

| # | Number | Manuscript location | Status |
|---|---|---|---|
| **O1** | Stripped-cliff significance: "$p = 1.01 \times 10^{-4}$" (all balanced, n=50) and "$r = 0.55$"; "$p = 3.76 \times 10^{-4}$" and "$r = 0.53$" (Llama, n=45) | results_v2 ¶cliff, Table cliff, ¶Per-model caveats; Conclusion; Appendix Power Analysis | The ledger gives Wilcoxon p and r for the **unstripped** cliff only (3.32e-06 / 0.658 and 1.81e-05 / 0.639). No stripped p or r appears anywhere in `results_FINAL.md`. This is the paper's headline test statistic, quoted in the Conclusion, with no entry in the source of truth |
| **O2** | Domain revision-rate block: "the model range is 71.9 percentage points (Llama~3.3~70B 73.5\% to Gemini~2.5 Flash 1.7\%, $n = 480$ per model)"; "the domain range is 13.5 percentage points ($n = 576$ per domain)"; "34.0\% of post-Turn~1 code outputs ... vs.\ 20.5--25.2\%"; "$\chi^2 = 35.63$, $df = 4$, $p = 3.4 \times 10^{-7}$"; "$n = 96$ per domain-model cell"; "boosted roughly 10--15 percentage points"; DeepSeek "near floor on all domains (3--10\%)"; "roughly 4--5$\times$ more" | results_v2 ¶Domain variation | None of this is in the ledger. The per-model rates reconcile against the per-model META rates in the file's own FLAG 1 comment (Llama 26.5%, Gemini 98.3%), which is itself not in the ledger. The chi-square, its df, its p, and the 13.5pp domain range have no recorded source |
| **O3** | "four of five reach significance on paired Wilcoxon tests ($p < 0.05$; data\_logic is marginal at $p = 0.058$)" | results_v2 ¶Domain variation | The ledger's per-domain delta tables (S10, M5) carry no p-values. The only per-domain p-values in the ledger are §4b sign tests on a different quantity |
| **O4** | Balanced-panel domain cells: "balanced-panel cells from $n = 5$ (writing) to $n = 22$ (code); only code clears $n \geq 10$"; "Creative writing shows the smallest balanced-panel cliff estimate, $\Delta = -0.17$ at $n = 6$" | results_v2 ¶Domain variation; echoed in Discussion Limitations ("only the code domain clears ten trials") | No per-domain balanced-panel breakdown exists in the ledger |
| **O5** | "Gemini declines in 98.3\% of post-Turn~1 observations" | results_v2 ¶Survival varies by model | Verified in the file's own FLAG 1 LaTeX comment against `genuine_meta_labels.jsonl`, but not recorded in `results_FINAL.md`. Same for the full per-model META series in that comment (DeepSeek 93.5%, GPT-4o 91.7%, Qwen 81.2%, Claude 59.2%, Llama 26.5%) |
| **O6** | Study 1 five-probe block: "$n = 3{,}932$"; "100\%, $n = 18$"; "12.5\%, $n = 24$"; "2.0\%, $n = 50$"; the probe wordings "Is there anything you would change?", "Does it meet the bar?", "What do you think?"; "No probe falls in the 40--99\% range" | results_v2 ¶Probe phrasing; Appendix Fig. probe-cliff caption ("100\% to $\leq$25\% across five pilot probes") | The ledger records only "99.9% vs 23.2%". The three pilot probes and their small Ns have no ledger entry |
| **O7** | Study 1 per-model decline rates: "Gemini~2.5 Flash declined 99.7\%, GPT-4o 68.6\%, Claude Sonnet~4 62.0\%"; Methods "revision drops to 0.3--38\%" | appendix.tex §Study 1; methods.tex ¶Study 1 | Complements of the dose-0 column in `MOMENTUM_SUMMARY.md` (0.3 / 31.4 / 38.0), so they reconcile, but they are not in either designated source as Study 1 results |
| **O8** | Study 1 inferential statistics: "$\chi^2 > 788$, $p < 0.0001$ for all models"; "Kruskal-Wallis $p > 0.40$ for all models"; "Spearman $\rho$: Gemini $-0.50$, Claude $-0.35$, GPT-4o $-0.14$" | appendix.tex §Study 1; methods.tex ¶Study 1 | Not in the ledger |
| **O9** | Ordinal regression table: coefficients 3.47, 3.94, −0.93, −1.04, −1.65, −0.74, −0.85, −1.05, 0.10, 0.15, 0.33, 0.42, 0.52, 1.15; N 3,840 / 3,840 / 1,920; AIC 5,319 / 4,839 / 3,545 | appendix.tex Table regression | Not in the ledger. The table's column headers are also unresolved: "Model A / Model B / Model C" with a caption naming only Model C |
| **O10** | Pairwise threshold comparisons: U = 4935, 4238, 4755, 4084, 4146, 3880; $p_{adj}$ values; r = −0.42, −0.32, −0.25, −0.28, −0.30, −0.21 | appendix.tex Table pairwise | Not in the ledger. Test is unnamed in the table (U statistic implies Mann-Whitney) |
| **O11** | Power analysis: "MDE for proportion difference $= 0.032$. Observed $\approx 0.75$"; "MDE for $\lvert\rho\rvert = 0.064$"; "Panel-level MDE $= 0.5$ levels" | appendix.tex ¶Power Analysis | Not in the ledger |
| **O12** | Judge calibration per-candidate table: DeepSeek 0.340 / 0.398; Qwen 0.272 / 0.017; Llama 0.181 / 0.022; GPT-4o 0.140 / 0.065; Gemini −0.036 / −0.026; and "$p = 2.1 \times 10^{-5}$" for the selected judge | appendix.tex Table judge-calibration; methods.tex ¶Judge Calibration (DeepSeek 0.340, GPT-4o 0.140) | The ledger records only the selected judge's r = 0.505 (p<0.001) and κ = 0.526. The five rejected candidates' statistics, and the exact p, are not in it |
| **O13** | Study 1 and Study 2 inter-rater reliability tables: QW κ 0.844 / 0.690 / 0.609 / 0.556 ($n = 60$); and 0.575 / 0.669 / 0.392 / 0.339 with % agree 68.3 / 76.7 / 71.7 / 38.3 and within-1 85.0 / 88.3 / 90.0 / 85.0 ($n = 60$) | appendix.tex Tables irr and irr-momentum | Not in the ledger, which covers Study 3 human raters only |
| **O14** | Reverse momentum: "suppresses full revision to near-zero across all models: Gemini 0.0\%, GPT-4o 1.0\%, Claude 21.9\%"; Methods "Reverse momentum (one affirming turn) suppresses revision to near-zero" | appendix.tex ¶Reverse Momentum; methods.tex ¶Study 2 | **Neither designated source carries these.** `MOMENTUM_SUMMARY.md` lists "Reverse momentum" under "Open questions / Next steps", i.e. as an experiment not yet run. Underlying data does exist on disk (`data/raw_responses/reverse_momentum_trials.jsonl`, `data/processed/reverse_momentum_scored.jsonl`, three `scripts/*reverse_momentum*.py`), and 21.9 is hard-coded in `paper/figures/gen_fig7_momentum.py`. So the numbers are probably real and `MOMENTUM_SUMMARY.md` is stale, but as of the sources of truth given, three published percentages have no ledger entry. Flagged, not resolved |
| **O15** | Teaser trial figures: "level~4 to level~2", "214 words to 79", "3{,}994 tokens"; and in the appendix, per-turn word counts 214 / 125 / 95 / 79 / 79 and cumulative tokens 407 / 1,040 / 1,854 / 2,838 / 3,994, with levels 4 / 4 / 3 / 2 / 2 | introduction_v2 Fig. teaser caption; _fig1_appendix.tex | Single-trial illustrative values from the raw data, generated by `paper/figures/gen_fig1.py`. Not ledger statistics; listed for completeness |
| **O16** | "combining a roughly 37-fold spread in output price" | results_v2 ¶tax | Arithmetic on the ledger's pricing table ($15.00 / $0.40 = 37.5), which the paper does not print. Derived, not recorded |
| **O17** | "12.4\%" of trials starting below the sufficiency threshold; "(6.9\%)" balanced panel share; "(90\%)" Llama share of the panel | methods.tex Edge Case Framework; results_v2 ¶Survival | Complements/quotients of ledger values (89/720, 50/720, 45/50). Derived and correct, but printed as percentages the ledger does not state |
| **O18** | "$\chi^2 = 376.54$" and dose figures 31.4 / 98.4 / 38.0 / 24.5 / 0.3 / 12.8, "$p = 0.51$" | appendix.tex §Study 2 | Trace cleanly to `MOMENTUM_SUMMARY.md`, not to `results_FINAL.md`. Listed only because §12 of the ledger summarizes Study 2 as "GPT-4o 98% momentum" and nothing else |

---

## 5. Notation audit of the live sections

### Greek-letter statistics

| Symbol | Used for | Where | Consistent? |
|---|---|---|---|
| $\kappa$ | Cohen's kappa in three distinct forms: quadratic-weighted on the 1–5 scale, unweighted 3-way inter-annotator, and human-vs-judge on binary picks | methods 54, 57, 64, 94; discussion 11; appendix Tables human-agreement, judge-calibration, irr, irr-momentum | Symbol used throughout, never spelled. **But the qualifier is dropped where it matters.** Methods ¶Reversibility writes "$\kappa = 0.703$" and ¶Stripping writes "$\kappa = 0.569$" with no weighting named; these are unweighted kappas on categorical picks, while every other $\kappa$ in the paper is quadratic-weighted. A reader sees one symbol for two estimators |
| "QW $\kappa$" | quadratic-weighted Cohen's kappa | methods 54, discussion 11, appendix Tables | The abbreviation is used at methods 54 before it is expanded at methods 57 ("quadratic-weighted Cohen's $\kappa$"). Expanded again in the appendix table caption |
| $\alpha$ | Krippendorff's alpha, interval scale, 3 raters | methods 57; discussion 11; appendix Table human-agreement | Consistent. Always named "Krippendorff's". Also used as the significance level in appendix ¶Power Analysis ("$\alpha = 0.05$") — two meanings for one symbol, though far apart |
| $\chi^2$ | chi-square statistic | results 115; appendix 6, 35 | Symbol throughout, never spelled. Appendix 6 names the test in prose ("Chi-squared tests"); results 115 gives the statistic with no test name in the sentence |
| $\rho$ | Spearman correlation | methods 101 ("Spearman $\rho = -0.14$ to $-0.50$"); appendix 8 ("Spearman $\rho$: ..."); appendix Power Analysis ("$\lvert\rho\rvert = 0.064$") | Symbol used, test named. **Conflicts with the next row** |
| $r$ | (a) Spearman correlation, (b) Wilcoxon effect size, (c) Mann-Whitney effect size | (a) methods 54, discussion 11, appendix Table judge-calibration header "Spearman $r$"; (b) results 78, appendix Power Analysis; (c) appendix Table pairwise header | **The clearest notation problem.** Spearman is $\rho$ in Study 1 contexts and $r$ in judge-calibration contexts, in the same paper. And $r$ then does double duty as a rank-biserial effect size. Three quantities, one letter |
| $\Delta$ | change in mean quality level | results 78, 84, 99, 110, Tables cliff / pooled-trajectory / domain-variation / targeted-feedback; appendix Power Analysis | Consistent |
| $t^*$ | quality-optimal stopping turn | methods 83; results 201, 203, Table revision-tax | Consistent and defined at first use |
| $df$ | chi-square degrees of freedom | results 115 only | Appears once; the appendix chi-squares carry no df. Ledger writes "dof"; paper writes "$df$" |

### p-value formatting

Five different conventions are in use, sometimes for the same number:

1. Scientific with a coefficient: `$p = 1.01 \times 10^{-4}$`, `$3.3 \times 10^{-6}$`, `$3.76 \times 10^{-4}$`, `$1.8 \times 10^{-5}$`, `$5.7 \times 10^{-19}$`, `$9.2 \times 10^{-12}$`, `$4.5 \times 10^{-4}$`, `$7.8 \times 10^{-3}$`, `$1.2 \times 10^{-2}$`, `$3.4 \times 10^{-7}$`, `$3.8 \times 10^{-3}$`, `$2.1 \times 10^{-5}$`, `$3.32 \times 10^{-6}$`
2. Plain decimal: `$p = 0.004$` (results 147), `$p = 0.058$` (results 117), `$p = 0.51$` (appendix 44)
3. Inequality thresholds, three of them: `$p < 0.001$` (methods 54, appendix 230), `$p < 0.0001$` (appendix 6, 35), `$p < 0.05$` (results 117), `$p > 0.40$` (appendix 6), `$<$0.001` unwrapped in the pairwise table
4. Star notation: `$^{**}p<0.01$, $^{***}p<0.001$` (appendix Table regression only)
5. Suppressed with a reason: `-- ($n < 5$)` (results Table targeted-per-model)

Specific inconsistencies:

- **The same p appears twice in two formats within one subsection.** The unstripped targeted-feedback p is `$p = 0.004$` in the prose of results 147 and `($3.8 \times 10^{-3}$)` in Table~\ref{tab:targeted-feedback} directly below it.
- **Coefficient precision varies** from two significant figures (`3.3`, `1.8`, `5.7`) to three (`1.01`, `3.76`, `3.32`) with no rule, including between the two places the same unstripped cliff p is printed: `$3.3 \times 10^{-6}$` in results 69 and `$3.32 \times 10^{-6}$` in the appendix.
- **Three different "very small" thresholds** (`<0.001`, `<0.0001`, and star notation at `p<0.001`) coexist across Methods and Appendix.
- **Spacing around `\times` is inconsistent** in the source: `1.01 \times 10^{-4}` (spaced) vs `1.8\times10^{-5}` does not occur, but `$3.8 \times 10^{-3}$` inside parentheses and `($3.75$e-03)` style never appears — the rendered output is uniform even where the source is not. No rendering defect found.
- **One p is reported with more precision than its source supports** (see mismatch M3).

### Are the tests named?

| Statistic | Test named at the point of use? |
|---|---|
| Balanced-panel cliff | Yes. "Wilcoxon signed-rank" (results 60); "Wilcoxon" (appendix Power Analysis) |
| Llama cliff, per-model cliffs | No. Results 78 gives "$p = 3.76 \times 10^{-4}$ ($r = 0.53$)" with no test named; inherited from the preceding paragraph |
| Domain deltas | Yes. "paired Wilcoxon tests" (results 117) |
| Targeted feedback | **No.** Neither results 147, Table targeted-feedback, nor Table targeted-per-model names Wilcoxon. The ledger specifies Wilcoxon signed-rank on non-zero differences |
| Revision-despite-sufficiency CI | **No.** "95\% CI [36.1\%, 42.3\%]" with no method. Ledger: 1000-resample percentile bootstrap, seed 42 |
| Reversibility CI | **No.** "95\% CI [45.2\%, 67.1\%]" with no method. Same bootstrap in the ledger |
| Reversibility kappa | Partly. "$\kappa = 0.703$" — Cohen's is not named, and the weighting is not stated |
| Human-judge kappa (0.569) | No. Cohen's not named |
| Domain revision-rate test | Statistic and df given ("$\chi^2 = 35.63$, $df = 4$"), test not named in words |
| Judge calibration | Yes. "Spearman" named at methods 54 and in the appendix table caption |
| Human rater agreement | Yes. "quadratic-weighted Cohen's $\kappa$", "Krippendorff's $\alpha$ (interval scale, 3 raters)" |
| Study 1 gate | Yes. "Chi-squared tests", "Kruskal-Wallis", "Spearman" (appendix 6, 8) |
| Study 1 pairwise comparisons | **No.** Table pairwise gives a $U$ column and Bonferroni-corrected $p_{adj}$ without naming Mann-Whitney |
| Study 1 ordinal regression | Yes in the caption ("Ordinal regression") |
| Study 2 gate shift | Yes. "$\chi^2 = 376.54$" with the chi-square symbol; the word "chi-squared" does not appear in the appendix Study 2 section |
| Study 2 threshold interaction | **No.** "Threshold level does not interact with momentum ($p = 0.51$)" — the logistic regression it comes from is not named |

### Effect sizes and intervals

- Effect sizes are reported for the balanced-panel cliff ($r = 0.658$ unstripped, $r = 0.55$ stripped, $r = 0.53$ Llama) and in the Study 1 pairwise table, and nowhere else.
- No effect size accompanies the targeted-feedback deltas, the domain chi-square, the Study 1 or Study 2 chi-squares, or any per-domain Wilcoxon.
- Confidence intervals appear on exactly two quantities (revision-despite-sufficiency and human reversibility). The ledger holds Clopper-Pearson intervals on all eleven §4b direction estimates and a bootstrap interval on the position-bias check, none of which reach the paper.
- Sample sizes are given consistently alongside estimates, in the form "$n = 177$", "(n=50)", "$n = 45$". The one place an n is loose is Results 117's "Turn~5 cells range from $n = 13$ (writing) to $n = 30$ (code)", which is a range rather than the five values.

### Other notation points

- Percentages: "39.3\%" style throughout, one decimal place, consistent. Whole-number rounding appears only where the paper is deliberately loose (Intro "39\%" and "13\%"; Discussion "62\%"; Abstract "70\%").
- Thousands separators: `3{,}932`, `1{,}920`, `3{,}994`, `\$65{,}678` use the braced form inside math; "3,600", "2,880", "1,728", "3,840" use plain commas in text. Both render correctly; the source is not uniform.
- Turn labels alternate between "Turn~1" / "Turn~5" in prose and "T1" / "T5" in tables and in ¶Over-elaboration, which mixes both registers in one paragraph.
- Domain names appear as "data\_logic" (underscore, code-style) in Table domain-variation and in Results 117, and as "Data logic" in Table s3-domains.
