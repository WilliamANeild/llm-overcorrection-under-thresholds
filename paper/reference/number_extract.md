# Number extract

Written by `paper/extract_numbers.py`. Sections read: sections/abstract_v2.tex, sections/introduction_v2.tex, sections/related_work_v2.tex, sections/methods.tex, sections/results_v2.tex, sections/conclusion.tex, sections/limitations.tex, sections/appendix.tex, sections/_fig1_appendix.tex.

- 866 numerals in the paper, of which 317 are structural (turn indices, scale levels, cross-references, citation years, typesetting dimensions) and set aside.
- 549 evidential numerals remain.
- 3084 numerals across `results_FINAL.md`, `MOMENTUM_SUMMARY.md`, `PIPELINE.md`.
- 97 paper values do not appear anywhere in the ledger as a literal string. That is a starting point, not a finding: a paper may state 87.6% where the ledger states 631/720, and a rounded value will not match.

## Paper values with no literal match in the ledger

| value | where | kind | float? | context |
|---|---|---|---|---|
| `88` | sections/abstract_v2.tex:34 | percentage |  | coring as STET, a diagnostic for whether a model leaves sufficient work alone. First drafts are sufficient in 88\% of trials, and most replies contain |
| `840` | sections/appendix.tex:113 | mean or delta | yes | l=gray!10] (crossing) { Fully factorial: $8 \times 16 \times 2 \times 3 \times 5$ runs $= \mathbf{3{,}840}$ primary trials }; \draw[arr] (scenarios.so |
| `3.94` | sections/appendix.tex:18 | mean or delta | yes | Predictor} & \textbf{Model A} & \textbf{Model B} & \textbf{Model C} \\ \midrule is\_leading & $3.47^{***}$ & $3.94^{***}$ & --- \\ threshold & $-0.93^ |
| `1.65` | sections/appendix.tex:19 | mean or delta | yes | \\ \midrule is\_leading & $3.47^{***}$ & $3.94^{***}$ & --- \\ threshold & $-0.93^{***}$ & $-1.04^{***}$ & $-1.65^{***}$ \\ is\_qualitative & $-0.74^{ |
| `0.85` | sections/appendix.tex:20 | mean or delta | yes | *}$ & --- \\ threshold & $-0.93^{***}$ & $-1.04^{***}$ & $-1.65^{***}$ \\ is\_qualitative & $-0.74^{***}$ & $-0.85^{***}$ & $-1.05^{***}$ \\ Claude So |
| `920` | sections/appendix.tex:206 | percentage |  | t-hoc power analysis at $\alpha = 0.05$, 80\% power: \begin{itemize} \item \textbf{Study~1 RQ1} ($N = 1{,}920$ per probe): MDE for proportion differen |
| `920` | sections/appendix.tex:207 | count or denominator |  | e $= 0.032$. Observed $\approx 0.75$, over twenty times the minimum. \item \textbf{Study~1 RQ2} ($N = 1{,}920$ leading-probe): MDE for $|\rho| = 0.064 |
| `0.064` | sections/appendix.tex:207 | count or denominator |  | ver twenty times the minimum. \item \textbf{Study~1 RQ2} ($N = 1{,}920$ leading-probe): MDE for $|\rho| = 0.064$. All observed correlations exceed thi |
| `4.01` | sections/appendix.tex:208 | p-value |  | ng. The count is powered: 19 of 50 trials became over-elaborated against 1 the other way, exact binomial $p = 4.01 \times 10^{-5}$. On the paired ordi |
| `3.79` | sections/appendix.tex:208 | p-value |  | her way, exact binomial $p = 4.01 \times 10^{-5}$. On the paired ordinal test the unstripped cliff gives $p = 3.79 \times 10^{-4}$ (Wilcoxon, $r = 0.5 |
| `4.42` | sections/appendix.tex:208 | p-value |  | stripped cliff gives $p = 3.79 \times 10^{-4}$ (Wilcoxon, $r = 0.50$ on $N = 50$) and the stripped cliff $p = 4.42 \times 10^{-3}$ ($r = 0.40$). \end{ |
| `0.33` | sections/appendix.tex:21 | mean or delta | yes | **}$ \\ is\_qualitative & $-0.74^{***}$ & $-0.85^{***}$ & $-1.05^{***}$ \\ Claude Sonnet & $0.10$ & $0.15$ & $0.33^{**}$ \\ Gemini Flash & $0.42^{***} |
| `0.52` | sections/appendix.tex:22 | mean or delta | yes | .85^{***}$ & $-1.05^{***}$ \\ Claude Sonnet & $0.10$ & $0.15$ & $0.33^{**}$ \\ Gemini Flash & $0.42^{***}$ & $0.52^{***}$ & $1.15^{***}$ \\ Scenario F |
| `0.398` | sections/appendix.tex:223 | reliability or effect size | yes | $r$} & \textbf{QW $\kappa$} \\ \midrule Claude Sonnet 4 & $0.505$ & $0.526$ \\ DeepSeek V4 Flash & $0.340$ & $0.398$ \\ Qwen 3 235B & $0.272$ & $0.017 |
| `0.272` | sections/appendix.tex:224 | mean or delta | yes | $} \\ \midrule Claude Sonnet 4 & $0.505$ & $0.526$ \\ DeepSeek V4 Flash & $0.340$ & $0.398$ \\ Qwen 3 235B & $0.272$ & $0.017$ \\ Llama 3.3 70B & $0.1 |
| `0.181` | sections/appendix.tex:225 | mean or delta | yes | 05$ & $0.526$ \\ DeepSeek V4 Flash & $0.340$ & $0.398$ \\ Qwen 3 235B & $0.272$ & $0.017$ \\ Llama 3.3 70B & $0.181$ & $0.022$ \\ GPT-4o & $0.140$ & $ |
| `0.036` | sections/appendix.tex:227 | count or denominator | yes | $0.272$ & $0.017$ \\ Llama 3.3 70B & $0.181$ & $0.022$ \\ GPT-4o & $0.140$ & $0.065$ \\ Gemini 2.5 Flash & $-0.036$ & $-0.026$ \\ \bottomrule \end{tab |
| `0.026` | sections/appendix.tex:227 | reliability or effect size | yes | $0.017$ \\ Llama 3.3 70B & $0.181$ & $0.022$ \\ GPT-4o & $0.140$ & $0.065$ \\ Gemini 2.5 Flash & $-0.036$ & $-0.026$ \\ \bottomrule \end{tabular} \cap |
| `2.1` | sections/appendix.tex:230 | p-value | yes | elected as the Study~3 evaluator, with the highest human correlation of the six candidates ($r = 0.505$, $p = 2.1 \times 10^{-5}$). Gemini 2.5 Flash w |
| `0.502` | sections/appendix.tex:244 | percentage | yes | n{tabular}{@{}lrrr@{}} \toprule Rater pair & QW $\kappa$ & Binary & Within 1 \\ \midrule Rater A -- Rater B & 0.502 & 78.1\% & 95.3\% \\ Rater B -- Ra |
| `0.612` | sections/appendix.tex:245 | percentage | yes | $\kappa$ & Binary & Within 1 \\ \midrule Rater A -- Rater B & 0.502 & 78.1\% & 95.3\% \\ Rater B -- Rater C & 0.612 & 82.8\% & 93.8\% \\ Rater A -- Ra |
| `0.478` | sections/appendix.tex:246 | percentage | yes | -- Rater B & 0.502 & 78.1\% & 95.3\% \\ Rater B -- Rater C & 0.612 & 82.8\% & 93.8\% \\ Rater A -- Rater C & 0.478 & 76.6\% & 95.3\% \\ \midrule All t |
| `5,319` | sections/appendix.tex:26 | mean or delta | yes | $0.52^{***}$ & $1.15^{***}$ \\ Scenario FEs & No & Yes & Yes \\ \midrule $N$ & 3,840 & 3,840 & 1,920 \\ AIC & 5,319 & 4,839 & 3,545 \\ \bottomrule \en |
| `4,839` | sections/appendix.tex:26 | mean or delta | yes | **}$ & $1.15^{***}$ \\ Scenario FEs & No & Yes & Yes \\ \midrule $N$ & 3,840 & 3,840 & 1,920 \\ AIC & 5,319 & 4,839 & 3,545 \\ \bottomrule \end{tabula |
| `3,545` | sections/appendix.tex:26 | mean or delta | yes | 1.15^{***}$ \\ Scenario FEs & No & Yes & Yes \\ \midrule $N$ & 3,840 & 3,840 & 1,920 \\ AIC & 5,319 & 4,839 & 3,545 \\ \bottomrule \end{tabular} \capt |
| `0.844` | sections/appendix.tex:268 | reliability or effect size | yes | \toprule \textbf{Dimension} & \textbf{QW $\kappa$} & \textbf{Interpretation} \\ \midrule Revision magnitude & 0.844 & Excellent \\ Revision value & 0. |
| `0.690` | sections/appendix.tex:269 | reliability or effect size | yes | QW $\kappa$} & \textbf{Interpretation} \\ \midrule Revision magnitude & 0.844 & Excellent \\ Revision value & 0.690 & Good \\ Overcorrection & 0.609 & |
| `0.556` | sections/appendix.tex:271 | mean or delta | yes | & Excellent \\ Revision value & 0.690 & Good \\ Overcorrection & 0.609 & Acceptable \\ Threshold alignment & 0.556 & Marginal \\ \bottomrule \end{tabu |
| `0.575` | sections/appendix.tex:285 | percentage | yes | Dimension} & \textbf{QW $\kappa$} & \textbf{\% Agree} & \textbf{\% Within 1} \\ \midrule Revision magnitude & 0.575 & 68.3 & 85.0 \\ Revision value &  |
| `68.3` | sections/appendix.tex:285 | percentage | yes | n} & \textbf{QW $\kappa$} & \textbf{\% Agree} & \textbf{\% Within 1} \\ \midrule Revision magnitude & 0.575 & 68.3 & 85.0 \\ Revision value & 0.669 &  |
| `85.0` | sections/appendix.tex:285 | percentage | yes | extbf{QW $\kappa$} & \textbf{\% Agree} & \textbf{\% Within 1} \\ \midrule Revision magnitude & 0.575 & 68.3 & 85.0 \\ Revision value & 0.669 & 76.7 &  |
| `0.669` | sections/appendix.tex:286 | percentage | yes | tbf{\% Agree} & \textbf{\% Within 1} \\ \midrule Revision magnitude & 0.575 & 68.3 & 85.0 \\ Revision value & 0.669 & 76.7 & 88.3 \\ Overcorrection &  |
| `76.7` | sections/appendix.tex:286 | percentage | yes | gree} & \textbf{\% Within 1} \\ \midrule Revision magnitude & 0.575 & 68.3 & 85.0 \\ Revision value & 0.669 & 76.7 & 88.3 \\ Overcorrection & 0.392 &  |
| `88.3` | sections/appendix.tex:286 | percentage | yes | \textbf{\% Within 1} \\ \midrule Revision magnitude & 0.575 & 68.3 & 85.0 \\ Revision value & 0.669 & 76.7 & 88.3 \\ Overcorrection & 0.392 & 71.7 & 9 |
| `0.392` | sections/appendix.tex:287 | mean or delta | yes | \midrule Revision magnitude & 0.575 & 68.3 & 85.0 \\ Revision value & 0.669 & 76.7 & 88.3 \\ Overcorrection & 0.392 & 71.7 & 90.0 \\ Threshold alignme |
| `71.7` | sections/appendix.tex:287 | mean or delta | yes | Revision magnitude & 0.575 & 68.3 & 85.0 \\ Revision value & 0.669 & 76.7 & 88.3 \\ Overcorrection & 0.392 & 71.7 & 90.0 \\ Threshold alignment & 0.33 |
| `90.0` | sections/appendix.tex:287 | mean or delta | yes | on magnitude & 0.575 & 68.3 & 85.0 \\ Revision value & 0.669 & 76.7 & 88.3 \\ Overcorrection & 0.392 & 71.7 & 90.0 \\ Threshold alignment & 0.339 & 38 |
| `0.339` | sections/appendix.tex:288 | count or denominator | yes | 85.0 \\ Revision value & 0.669 & 76.7 & 88.3 \\ Overcorrection & 0.392 & 71.7 & 90.0 \\ Threshold alignment & 0.339 & 38.3 & 85.0 \\ \bottomrule \end{ |
| `38.3` | sections/appendix.tex:288 | count or denominator | yes | Revision value & 0.669 & 76.7 & 88.3 \\ Overcorrection & 0.392 & 71.7 & 90.0 \\ Threshold alignment & 0.339 & 38.3 & 85.0 \\ \bottomrule \end{tabular} |
| `85.0` | sections/appendix.tex:288 | count or denominator | yes | n value & 0.669 & 76.7 & 88.3 \\ Overcorrection & 0.392 & 71.7 & 90.0 \\ Threshold alignment & 0.339 & 38.3 & 85.0 \\ \bottomrule \end{tabular} \capti |
| `0.01` | sections/appendix.tex:29 | p-value | yes | tabular} \caption{Ordinal regression (overcorrection $\sim$ predictors). Model C: leading-probe only. $^{**}p<0.01$, $^{***}p<0.001$. Reference: GPT-4 |
| `0.006` | sections/appendix.tex:313 | mean or delta | yes | 4 & 196 & 58.5 & 0.11 \\ Qwen 3 235B & 90 & 74.5 & $<0.001$ \\ GPT-4o & 40 & 80.0 & 0.006 \\ DeepSeek-V4-Flash & 31 & 85.7 & 0.007 \\ Gemini 2.5 Flash |
| `0.007` | sections/appendix.tex:314 | mean or delta | yes | & 90 & 74.5 & $<0.001$ \\ GPT-4o & 40 & 80.0 & 0.006 \\ DeepSeek-V4-Flash & 31 & 85.7 & 0.007 \\ Gemini 2.5 Flash & 8 & 100.0 & 0.062 \\ \midrule \mul |
| `920` | sections/appendix.tex:34 | percentage |  | be improved?'' and ``Is there anything you would change?'') trigger near-universal revision (99.9\%, $n = 1{,}920$; 100\%, $n = 18$). The three probes |
| `920` | sections/appendix.tex:34 | percentage |  | bar?,'' and ``What do you think?'') produce single-digit to low-double-digit revision rates (23.2\%, $n = 1{,}920$; 12.5\%, $n = 24$; 2.0\%, $n = 50$) |
| `3.84` | sections/appendix.tex:340 | mean or delta | yes | Turn & Stripped & (Unstripped) & Shift & $n$ \\ \midrule T1 & 4.17 & (4.17) & 0 & 720 \\ T2 & 3.84 & (3.59) & +0.25 & 283 \\ T3 & 3.69 & (3.43) & +0.2 |
| `3.59` | sections/appendix.tex:340 | mean or delta | yes | & Stripped & (Unstripped) & Shift & $n$ \\ \midrule T1 & 4.17 & (4.17) & 0 & 720 \\ T2 & 3.84 & (3.59) & +0.25 & 283 \\ T3 & 3.69 & (3.43) & +0.25 & 1 |
| `3.69` | sections/appendix.tex:341 | mean or delta | yes | ft & $n$ \\ \midrule T1 & 4.17 & (4.17) & 0 & 720 \\ T2 & 3.84 & (3.59) & +0.25 & 283 \\ T3 & 3.69 & (3.43) & +0.25 & 185 \\ T4 & 3.62 & (3.40) & +0.2 |
| `3.43` | sections/appendix.tex:341 | mean or delta | yes | \\ \midrule T1 & 4.17 & (4.17) & 0 & 720 \\ T2 & 3.84 & (3.59) & +0.25 & 283 \\ T3 & 3.69 & (3.43) & +0.25 & 185 \\ T4 & 3.62 & (3.40) & +0.22 & 154 \ |
| `3.62` | sections/appendix.tex:342 | mean or delta | yes | (4.17) & 0 & 720 \\ T2 & 3.84 & (3.59) & +0.25 & 283 \\ T3 & 3.69 & (3.43) & +0.25 & 185 \\ T4 & 3.62 & (3.40) & +0.22 & 154 \\ T5 & 3.42 & (3.33) & + |
| `3.33` | sections/appendix.tex:343 | mean or delta | yes | .25 & 283 \\ T3 & 3.69 & (3.43) & +0.25 & 185 \\ T4 & 3.62 & (3.40) & +0.22 & 154 \\ T5 & 3.42 & (3.33) & +0.08 & 96 \\ \midrule $\Delta$ (T1--T5) & $ |
| `0.08` | sections/appendix.tex:343 | mean or delta | yes | \\ T3 & 3.69 & (3.43) & +0.25 & 185 \\ T4 & 3.62 & (3.40) & +0.22 & 154 \\ T5 & 3.42 & (3.33) & +0.08 & 96 \\ \midrule $\Delta$ (T1--T5) & $\mathbf{-0 |
| `0.84` | sections/appendix.tex:345 | mean or delta | yes | 22 & 154 \\ T5 & 3.42 & (3.33) & +0.08 & 96 \\ \midrule $\Delta$ (T1--T5) & $\mathbf{-0.75}$ & ($-0.84$) & & \\ \bottomrule \end{tabular} \caption{Poo |
| `0.035` | sections/appendix.tex:361 | mean or delta | yes | (T1--T5) & $p$ & $n_{\text{T5}}$ \\ \midrule analysis & $-0.59$ & 0.004 & 17 \\ code & $-0.47$ & 0.035 & 30 \\ creative & $-0.32$ & 0.058 & 19 \\ data |
| `0.206` | sections/appendix.tex:363 | mean or delta | yes | & 17 \\ code & $-0.47$ & 0.035 & 30 \\ creative & $-0.32$ & 0.058 & 19 \\ data\_logic & $-0.24$ & 0.206 & 17 \\ writing & $-0.77$ & 0.004 & 13 \\ \bot |
| `3,016,008` | sections/appendix.tex:408 | bare number |  | sed and their parameter counts are not published. \paragraph{Budget.} The 720 Study~3 conversations consumed 3,016,008 input and 1,050,833 output toke |
| `1,050,833` | sections/appendix.tex:408 | bare number |  | ter counts are not published. \paragraph{Budget.} The 720 Study~3 conversations consumed 3,016,008 input and 1,050,833 output tokens. The evaluation,  |
| `8,192` | sections/appendix.tex:411 | mean or delta |  | le from what was saved. Study~1 ran 3,840 primary trials and Study~2 analysed 1,813. Generation was capped at 8,192 output tokens per call and judging |
| `512` | sections/appendix.tex:412 | mean or delta |  | imary trials and Study~2 analysed 1,813. Generation was capped at 8,192 output tokens per call and judging at 512. \paragraph{Settings.} Generation ra |
| `0.99` | sections/appendix.tex:6 | p-value |  | ng the three gate outcomes ordinally, Kruskal-Wallis across the eight threshold levels gives $H = 1.42$, $p = 0.99$ for Gemini~2.5 Flash and $H = 2.01 |
| `0.96` | sections/appendix.tex:6 | p-value |  | llis across the eight threshold levels gives $H = 1.42$, $p = 0.99$ for Gemini~2.5 Flash and $H = 2.01$, $p = 0.96$ for GPT-4o; only Claude Sonnet~4 r |
| `0.14` | sections/appendix.tex:8 | reliability or effect size |  | thresholds produce moderately less overcorrection (Spearman $\rho$: Gemini $-0.50$, Claude $-0.35$, GPT-4o $-0.14$), but this calibration is hidden be |
| `1.9` | sections/conclusion.tex:5 | p-value |  | the fault does. Told what to fix, a model produces revisions 1.01 levels higher than generic iteration ($p = 1.9 \times 10^{-19}$). Systems should eva |
| `88` | sections/introduction_v2.tex:73 | percentage |  | ns and validate every quality judgment against human raters. Most of the work being revised did not need it: 88\% of the 720 first drafts are already  |
| `86.7` | sections/introduction_v2.tex:75 | percentage |  | already sufficient. Asked to improve them without direction, models mostly do not revise: by the fifth turn, 86.7\% of replies are meta-responses, res |
| `1.9` | sections/introduction_v2.tex:80 | p-value |  | ufficient, a single critique naming the fault lifts the revision 1.01 levels above undirected iteration ($p = 1.9 \times 10^{-19}$). Blind readers sho |
| `71.9` | sections/results_v2.tex:102 | count or denominator |  | ld constant, model identity explains far more variation in genuine-revision rate than task domain: a range of 71.9 percentage points against 13.5. All |
| `4.71` | sections/results_v2.tex:138 | p-value |  | written critique and produced what we call a targeted revision. On stripped content, targeted revisions score 4.71 against 3.70 for the model's own ge |
| `3.70` | sections/results_v2.tex:138 | p-value |  | que and produced what we call a targeted revision. On stripped content, targeted revisions score 4.71 against 3.70 for the model's own generic next-tu |
| `1.9` | sections/results_v2.tex:138 | p-value |  | revisions score 4.71 against 3.70 for the model's own generic next-turn revision, a gain of 1.01 levels ($p = 1.9 \times 10^{-19}$, $n = 177$; unstrip |
| `4.71` | sections/results_v2.tex:138 | p-value |  | el's own generic next-turn revision, a gain of 1.01 levels ($p = 1.9 \times 10^{-19}$, $n = 177$; unstripped: 4.71 against 4.51, $+0.20$, $p = 6.6 \ti |
| `4.51` | sections/results_v2.tex:138 | p-value |  | ric next-turn revision, a gain of 1.01 levels ($p = 1.9 \times 10^{-19}$, $n = 177$; unstripped: 4.71 against 4.51, $+0.20$, $p = 6.6 \times 10^{-3}$) |
| `6.6` | sections/results_v2.tex:138 | p-value |  | on, a gain of 1.01 levels ($p = 1.9 \times 10^{-19}$, $n = 177$; unstripped: 4.71 against 4.51, $+0.20$, $p = 6.6 \times 10^{-3}$). The unstripped com |
| `1.56` | sections/results_v2.tex:148 | p-value | yes | ular}{lccc} \toprule Model & $n$ & Stripped $\Delta$ & $p$ \\ \midrule Llama 3.3 70B & 71 & $+1.56$ & $6.5 \times 10^{-12}$ \\ Qwen 3 235B & 21 & $+1. |
| `1.10` | sections/results_v2.tex:149 | p-value | yes | a$ & $p$ \\ \midrule Llama 3.3 70B & 71 & $+1.56$ & $6.5 \times 10^{-12}$ \\ Qwen 3 235B & 21 & $+1.10$ & $4.5 \times 10^{-4}$ \\ GPT-4o & 12 & $+1.00 |
| `8.8` | sections/results_v2.tex:150 | p-value | yes | 6.5 \times 10^{-12}$ \\ Qwen 3 235B & 21 & $+1.10$ & $4.5 \times 10^{-4}$ \\ GPT-4o & 12 & $+1.00$ & $8.8 \times 10^{-3}$ \\ DeepSeek V4 Flash & 19 &  |
| `4.7` | sections/results_v2.tex:152 | p-value | yes | {-3}$ \\ DeepSeek V4 Flash & 19 & $+0.74$ & $2.0 \times 10^{-2}$ \\ Claude Sonnet 4 & 51 & $+0.25$ & $4.7 \times 10^{-3}$ \\ Gemini 2.5 Flash & 3 & $+ |
| `1.67` | sections/results_v2.tex:153 | p-value | yes | \times 10^{-2}$ \\ Claude Sonnet 4 & 51 & $+0.25$ & $4.7 \times 10^{-3}$ \\ Gemini 2.5 Flash & 3 & $+1.67$ & -- ($n < 5$) \\ \bottomrule \end{tabular} |
| `1.6` | sections/results_v2.tex:173 | percentage |  | only the tokens needed to reach $t^*$, the waste is 164.2\%, so continuing past peak quality produces roughly 1.6 times more text than reaching the op |
| `97.8` | sections/results_v2.tex:189 | percentage | yes | \small \begin{tabular}{@{}lr@{}} \toprule Model & Sufficient output left alone \\ \midrule Gemini 2.5 Flash & 97.8\% \\ DeepSeek V4 Flash & 96.3\% \\  |
| `96.3` | sections/results_v2.tex:190 | percentage | yes | }} \toprule Model & Sufficient output left alone \\ \midrule Gemini 2.5 Flash & 97.8\% \\ DeepSeek V4 Flash & 96.3\% \\ GPT-4o & 82.3\% \\ Qwen 3 235B |
| `82.3` | sections/results_v2.tex:191 | percentage | yes | Sufficient output left alone \\ \midrule Gemini 2.5 Flash & 97.8\% \\ DeepSeek V4 Flash & 96.3\% \\ GPT-4o & 82.3\% \\ Qwen 3 235B & 68.4\% \\ Claude  |
| `68.4` | sections/results_v2.tex:192 | percentage | yes | alone \\ \midrule Gemini 2.5 Flash & 97.8\% \\ DeepSeek V4 Flash & 96.3\% \\ GPT-4o & 82.3\% \\ Qwen 3 235B & 68.4\% \\ Claude Sonnet 4 & 54.1\% \\ Ll |
| `54.1` | sections/results_v2.tex:193 | percentage | yes | Flash & 97.8\% \\ DeepSeek V4 Flash & 96.3\% \\ GPT-4o & 82.3\% \\ Qwen 3 235B & 68.4\% \\ Claude Sonnet 4 & 54.1\% \\ Llama 3.3 70B & 18.4\% \\ \bott |
| `0.80` | sections/results_v2.tex:204 | reliability or effect size |  | random splits of the tasks into halves, the halves agree at mean Spearman $\rho = 0.972$, every split clears $0.80$, and Llama is last in all of them. |
| `3.2` | sections/results_v2.tex:204 | mean or delta |  | over the 36 tasks that carry a denominator, where six would reach $0.95$, because variance between models is 3.2 times the model-by-task residual. Gen |
| `62.7` | sections/results_v2.tex:55 | percentage |  | often than they raise it.} Across all 718 genuine revisions, a revision leaves the quality level unchanged in 62.7\% of cases, lowers it in 25.6\%, an |
| `25.6` | sections/results_v2.tex:56 | percentage |  | oss all 718 genuine revisions, a revision leaves the quality level unchanged in 62.7\% of cases, lowers it in 25.6\%, and raises it in 11.7\%. Restric |
| `11.7` | sections/results_v2.tex:56 | percentage |  | ions, a revision leaves the quality level unchanged in 62.7\% of cases, lowers it in 25.6\%, and raises it in 11.7\%. Restricting to the 268 revisions |
| `62.8` | sections/results_v2.tex:58 | p-value |  | s that move the level at all, 184 move it down and 84 move it up, a share of 68.7\% (exact binomial 95\% CI $[62.8\%, 74.1\%]$; sign test $p = 1.13 \t |
| `74.1` | sections/results_v2.tex:58 | p-value |  | ove the level at all, 184 move it down and 84 move it up, a share of 68.7\% (exact binomial 95\% CI $[62.8\%, 74.1\%]$; sign test $p = 1.13 \times 10^ |
| `1.13` | sections/results_v2.tex:58 | p-value |  | move it down and 84 move it up, a share of 68.7\% (exact binomial 95\% CI $[62.8\%, 74.1\%]$; sign test $p = 1.13 \times 10^{-9}$). Of the 524 revisio |
| `3.70` | sections/results_v2.tex:76 | p-value |  | erial; it does not drop what was asked for. On the ordinal scale, mean quality on stripped content falls from 3.70 to 3.32, a decline of $-0.38$ level |
| `3.32` | sections/results_v2.tex:76 | p-value |  | t does not drop what was asked for. On the ordinal scale, mean quality on stripped content falls from 3.70 to 3.32, a decline of $-0.38$ levels ($p =  |
| `4.42` | sections/results_v2.tex:77 | p-value |  | he ordinal scale, mean quality on stripped content falls from 3.70 to 3.32, a decline of $-0.38$ levels ($p = 4.42 \times 10^{-3}$; unstripped $-0.44$ |
| `3.8` | sections/results_v2.tex:77 | p-value |  | ent falls from 3.70 to 3.32, a decline of $-0.38$ levels ($p = 4.42 \times 10^{-3}$; unstripped $-0.44$, $p = 3.8 \times 10^{-4}$), of which 14\% is a |
| `1.80` | sections/results_v2.tex:83 | p-value |  | he only model with power to detect a within-model cliff; its stripped cliff of $-0.31$ is significant at $p = 1.80 \times 10^{-2}$. GPT-4o, DeepSeek a |

## Every evidential value in the paper

| value | where | kind | float? | context |
|---|---|---|---|---|
| `6` | sections/abstract_v2.tex:32 | bare number |  | ned the work that is already sufficient and gets revised anyway. We run five-turn revision conversations with 6 models on 40 tasks across 5 domains, a |
| `40` | sections/abstract_v2.tex:32 | bare number |  | that is already sufficient and gets revised anyway. We run five-turn revision conversations with 6 models on 40 tasks across 5 domains, adding a targe |
| `5` | sections/abstract_v2.tex:32 | bare number |  | sufficient and gets revised anyway. We run five-turn revision conversations with 6 models on 40 tasks across 5 domains, adding a targeted critique on  |
| `88` | sections/abstract_v2.tex:34 | percentage |  | coring as STET, a diagnostic for whether a model leaves sufficient work alone. First drafts are sufficient in 88\% of trials, and most replies contain |
| `69` | sections/abstract_v2.tex:34 | percentage |  | s restate the draft or decline while presenting it as compliance. Revisions that change quality make it worse 69\% of the time, and the damage has a d |
| `4` | sections/abstract_v2.tex:34 | percentage |  | of the time, and the damage has a direction: over five turns the share of over-elaborated outputs rises from 4\% to 40\% while the share falling below |
| `40` | sections/abstract_v2.tex:34 | percentage |  | time, and the damage has a direction: over five turns the share of over-elaborated outputs rises from 4\% to 40\% while the share falling below suffic |
| `1.01` | sections/abstract_v2.tex:35 | mean or delta |  | ow no reliable preference between it and the last. A critique naming the fault reverses it, lifting revisions 1.01 levels. Revision robustness, a mode |
| `1` | sections/appendix.tex:1 | bare number |  | \section{Study 1: The Revision Gate} \label{sec:appendix-study1} Study~1 tests whether user-stated quality thresholds constra |
| `3` | sections/appendix.tex:113 | mean or delta | yes | fill=gray!10] (crossing) { Fully factorial: $8 \times 16 \times 2 \times 3 \times 5$ runs $= \mathbf{3{,}840}$ primary trials }; \draw[arr] (scenarios |
| `840` | sections/appendix.tex:113 | mean or delta | yes | l=gray!10] (crossing) { Fully factorial: $8 \times 16 \times 2 \times 3 \times 5$ runs $= \mathbf{3{,}840}$ primary trials }; \draw[arr] (scenarios.so |
| `0` | sections/appendix.tex:116 | mean or delta | yes | 2 \times 3 \times 5$ runs $= \mathbf{3{,}840}$ primary trials }; \draw[arr] (scenarios.south) -- ++(0,-0.2) -| (crossing.north -| scenarios); \draw[ar |
| `0.2` | sections/appendix.tex:116 | mean or delta | yes | \times 3 \times 5$ runs $= \mathbf{3{,}840}$ primary trials }; \draw[arr] (scenarios.south) -- ++(0,-0.2) -| (crossing.north -| scenarios); \draw[arr] |
| `1` | sections/appendix.tex:139 | bare number | yes | Judge} (GPT-4o, $T{=}0$) }; \draw[arr] (turn2) -- (judge); \end{tikzpicture} \caption{Study~1 experimental procedure. Four factors crossed in a fully  |
| `3,840` | sections/appendix.tex:139 | bare number | yes | icture} \caption{Study~1 experimental procedure. Four factors crossed in a fully factorial design produce 3,840 trials.} \label{fig:pipeline} \end{fig |
| `1` | sections/appendix.tex:160 | percentage | yes | ludegraphics[width=\columnwidth]{figures/10_probe_calibration_cliff.pdf} \caption{Compliance cliff (Study~1 pilot). Revision rates drop from 100\% to  |
| `100` | sections/appendix.tex:160 | percentage | yes | gures/10_probe_calibration_cliff.pdf} \caption{Compliance cliff (Study~1 pilot). Revision rates drop from 100\% to $\leq$25\% across five pilot probes |
| `25` | sections/appendix.tex:160 | percentage | yes | calibration_cliff.pdf} \caption{Compliance cliff (Study~1 pilot). Revision rates drop from 100\% to $\leq$25\% across five pilot probes with no interm |
| `1` | sections/appendix.tex:167 | bare number | yes | es/02_threshold_ladder.pdf} \caption{Overcorrection by threshold level within leading-probe trials (Study~1).} \label{fig:threshold-ladder} \end{figur |
| `3.47` | sections/appendix.tex:18 | mean or delta | yes | oprule \textbf{Predictor} & \textbf{Model A} & \textbf{Model B} & \textbf{Model C} \\ \midrule is\_leading & $3.47^{***}$ & $3.94^{***}$ & --- \\ thre |
| `3.94` | sections/appendix.tex:18 | mean or delta | yes | Predictor} & \textbf{Model A} & \textbf{Model B} & \textbf{Model C} \\ \midrule is\_leading & $3.47^{***}$ & $3.94^{***}$ & --- \\ threshold & $-0.93^ |
| `1` | sections/appendix.tex:181 | bare number |  | ection{Full Statistical Tables} \label{sec:appendix-stats} \subsection{Pairwise Threshold Comparisons (Study 1)} \begin{table}[h] \centering \small \b |
| `0.93` | sections/appendix.tex:19 | mean or delta | yes | xtbf{Model B} & \textbf{Model C} \\ \midrule is\_leading & $3.47^{***}$ & $3.94^{***}$ & --- \\ threshold & $-0.93^{***}$ & $-1.04^{***}$ & $-1.65^{** |
| `1.04` | sections/appendix.tex:19 | mean or delta | yes | \textbf{Model C} \\ \midrule is\_leading & $3.47^{***}$ & $3.94^{***}$ & --- \\ threshold & $-0.93^{***}$ & $-1.04^{***}$ & $-1.65^{***}$ \\ is\_quali |
| `1.65` | sections/appendix.tex:19 | mean or delta | yes | \\ \midrule is\_leading & $3.47^{***}$ & $3.94^{***}$ & --- \\ threshold & $-0.93^{***}$ & $-1.04^{***}$ & $-1.65^{***}$ \\ is\_qualitative & $-0.74^{ |
| `70` | sections/appendix.tex:190 | mean or delta | yes | } & \textbf{Comparison} & \textbf{$U$} & \textbf{$p_{\text{adj}}$} & \textbf{$r$} \\ \midrule Gemini (num.) & 70 vs.\ 100 & 4935 & $<$0.001 & $-$0.42  |
| `100` | sections/appendix.tex:190 | mean or delta | yes | tbf{Comparison} & \textbf{$U$} & \textbf{$p_{\text{adj}}$} & \textbf{$r$} \\ \midrule Gemini (num.) & 70 vs.\ 100 & 4935 & $<$0.001 & $-$0.42 \\ Gemin |
| `4935` | sections/appendix.tex:190 | mean or delta | yes | mparison} & \textbf{$U$} & \textbf{$p_{\text{adj}}$} & \textbf{$r$} \\ \midrule Gemini (num.) & 70 vs.\ 100 & 4935 & $<$0.001 & $-$0.42 \\ Gemini (num |
| `0.001` | sections/appendix.tex:190 | mean or delta | yes | & \textbf{$U$} & \textbf{$p_{\text{adj}}$} & \textbf{$r$} \\ \midrule Gemini (num.) & 70 vs.\ 100 & 4935 & $<$0.001 & $-$0.42 \\ Gemini (num.) & 85 vs |
| `0.42` | sections/appendix.tex:190 | mean or delta | yes | U$} & \textbf{$p_{\text{adj}}$} & \textbf{$r$} \\ \midrule Gemini (num.) & 70 vs.\ 100 & 4935 & $<$0.001 & $-$0.42 \\ Gemini (num.) & 85 vs.\ 100 & 42 |
| `85` | sections/appendix.tex:191 | mean or delta | yes | adj}}$} & \textbf{$r$} \\ \midrule Gemini (num.) & 70 vs.\ 100 & 4935 & $<$0.001 & $-$0.42 \\ Gemini (num.) & 85 vs.\ 100 & 4238 & $<$0.001 & $-$0.32  |
| `100` | sections/appendix.tex:191 | mean or delta | yes | & \textbf{$r$} \\ \midrule Gemini (num.) & 70 vs.\ 100 & 4935 & $<$0.001 & $-$0.42 \\ Gemini (num.) & 85 vs.\ 100 & 4238 & $<$0.001 & $-$0.32 \\ Gemin |
| `4238` | sections/appendix.tex:191 | mean or delta | yes | tbf{$r$} \\ \midrule Gemini (num.) & 70 vs.\ 100 & 4935 & $<$0.001 & $-$0.42 \\ Gemini (num.) & 85 vs.\ 100 & 4238 & $<$0.001 & $-$0.32 \\ Gemini (num |
| `0.001` | sections/appendix.tex:191 | mean or delta | yes | \ \midrule Gemini (num.) & 70 vs.\ 100 & 4935 & $<$0.001 & $-$0.42 \\ Gemini (num.) & 85 vs.\ 100 & 4238 & $<$0.001 & $-$0.32 \\ Gemini (num.) & 0 vs. |
| `0.32` | sections/appendix.tex:191 | mean or delta | yes | Gemini (num.) & 70 vs.\ 100 & 4935 & $<$0.001 & $-$0.42 \\ Gemini (num.) & 85 vs.\ 100 & 4238 & $<$0.001 & $-$0.32 \\ Gemini (num.) & 0 vs.\ 100 & 475 |
| `0` | sections/appendix.tex:192 | mean or delta | yes | 100 & 4935 & $<$0.001 & $-$0.42 \\ Gemini (num.) & 85 vs.\ 100 & 4238 & $<$0.001 & $-$0.32 \\ Gemini (num.) & 0 vs.\ 100 & 4755 & 0.002 & $-$0.25 \\ G |
| `100` | sections/appendix.tex:192 | mean or delta | yes | 935 & $<$0.001 & $-$0.42 \\ Gemini (num.) & 85 vs.\ 100 & 4238 & $<$0.001 & $-$0.32 \\ Gemini (num.) & 0 vs.\ 100 & 4755 & 0.002 & $-$0.25 \\ Gemini ( |
| `4755` | sections/appendix.tex:192 | mean or delta | yes | $<$0.001 & $-$0.42 \\ Gemini (num.) & 85 vs.\ 100 & 4238 & $<$0.001 & $-$0.32 \\ Gemini (num.) & 0 vs.\ 100 & 4755 & 0.002 & $-$0.25 \\ Gemini (qual.) |
| `0.002` | sections/appendix.tex:192 | mean or delta | yes | 1 & $-$0.42 \\ Gemini (num.) & 85 vs.\ 100 & 4238 & $<$0.001 & $-$0.32 \\ Gemini (num.) & 0 vs.\ 100 & 4755 & 0.002 & $-$0.25 \\ Gemini (qual.) & 0 vs |
| `0.25` | sections/appendix.tex:192 | mean or delta | yes | \\ Gemini (num.) & 85 vs.\ 100 & 4238 & $<$0.001 & $-$0.32 \\ Gemini (num.) & 0 vs.\ 100 & 4755 & 0.002 & $-$0.25 \\ Gemini (qual.) & 0 vs.\ 100 & 408 |
| `0` | sections/appendix.tex:193 | mean or delta | yes | .\ 100 & 4238 & $<$0.001 & $-$0.32 \\ Gemini (num.) & 0 vs.\ 100 & 4755 & 0.002 & $-$0.25 \\ Gemini (qual.) & 0 vs.\ 100 & 4084 & 0.002 & $-$0.28 \\ C |
| `100` | sections/appendix.tex:193 | mean or delta | yes | & 4238 & $<$0.001 & $-$0.32 \\ Gemini (num.) & 0 vs.\ 100 & 4755 & 0.002 & $-$0.25 \\ Gemini (qual.) & 0 vs.\ 100 & 4084 & 0.002 & $-$0.28 \\ Claude ( |
| `4084` | sections/appendix.tex:193 | mean or delta | yes | & $<$0.001 & $-$0.32 \\ Gemini (num.) & 0 vs.\ 100 & 4755 & 0.002 & $-$0.25 \\ Gemini (qual.) & 0 vs.\ 100 & 4084 & 0.002 & $-$0.28 \\ Claude (num.) & |
| `0.002` | sections/appendix.tex:193 | mean or delta | yes | .001 & $-$0.32 \\ Gemini (num.) & 0 vs.\ 100 & 4755 & 0.002 & $-$0.25 \\ Gemini (qual.) & 0 vs.\ 100 & 4084 & 0.002 & $-$0.28 \\ Claude (num.) & 85 vs |
| `0.28` | sections/appendix.tex:193 | mean or delta | yes | .32 \\ Gemini (num.) & 0 vs.\ 100 & 4755 & 0.002 & $-$0.25 \\ Gemini (qual.) & 0 vs.\ 100 & 4084 & 0.002 & $-$0.28 \\ Claude (num.) & 85 vs.\ 100 & 41 |
| `85` | sections/appendix.tex:194 | mean or delta | yes | vs.\ 100 & 4755 & 0.002 & $-$0.25 \\ Gemini (qual.) & 0 vs.\ 100 & 4084 & 0.002 & $-$0.28 \\ Claude (num.) & 85 vs.\ 100 & 4146 & $<$0.001 & $-$0.30 \ |
| `100` | sections/appendix.tex:194 | mean or delta | yes | 0 & 4755 & 0.002 & $-$0.25 \\ Gemini (qual.) & 0 vs.\ 100 & 4084 & 0.002 & $-$0.28 \\ Claude (num.) & 85 vs.\ 100 & 4146 & $<$0.001 & $-$0.30 \\ Claud |
| `4146` | sections/appendix.tex:194 | mean or delta | yes | 55 & 0.002 & $-$0.25 \\ Gemini (qual.) & 0 vs.\ 100 & 4084 & 0.002 & $-$0.28 \\ Claude (num.) & 85 vs.\ 100 & 4146 & $<$0.001 & $-$0.30 \\ Claude (qua |
| `0.001` | sections/appendix.tex:194 | mean or delta | yes | & $-$0.25 \\ Gemini (qual.) & 0 vs.\ 100 & 4084 & 0.002 & $-$0.28 \\ Claude (num.) & 85 vs.\ 100 & 4146 & $<$0.001 & $-$0.30 \\ Claude (qual.) & 85 vs |
| `0.30` | sections/appendix.tex:194 | mean or delta | yes | \\ Gemini (qual.) & 0 vs.\ 100 & 4084 & 0.002 & $-$0.28 \\ Claude (num.) & 85 vs.\ 100 & 4146 & $<$0.001 & $-$0.30 \\ Claude (qual.) & 85 vs.\ 100 & 3 |
| `85` | sections/appendix.tex:195 | mean or delta | yes | \ 100 & 4084 & 0.002 & $-$0.28 \\ Claude (num.) & 85 vs.\ 100 & 4146 & $<$0.001 & $-$0.30 \\ Claude (qual.) & 85 vs.\ 100 & 3880 & 0.024 & $-$0.21 \\  |
| `100` | sections/appendix.tex:195 | mean or delta | yes | 4084 & 0.002 & $-$0.28 \\ Claude (num.) & 85 vs.\ 100 & 4146 & $<$0.001 & $-$0.30 \\ Claude (qual.) & 85 vs.\ 100 & 3880 & 0.024 & $-$0.21 \\ \bottomr |
| `3880` | sections/appendix.tex:195 | mean or delta | yes | 0.002 & $-$0.28 \\ Claude (num.) & 85 vs.\ 100 & 4146 & $<$0.001 & $-$0.30 \\ Claude (qual.) & 85 vs.\ 100 & 3880 & 0.024 & $-$0.21 \\ \bottomrule \en |
| `0.024` | sections/appendix.tex:195 | mean or delta | yes | & $-$0.28 \\ Claude (num.) & 85 vs.\ 100 & 4146 & $<$0.001 & $-$0.30 \\ Claude (qual.) & 85 vs.\ 100 & 3880 & 0.024 & $-$0.21 \\ \bottomrule \end{tabu |
| `0.21` | sections/appendix.tex:195 | mean or delta | yes | \ Claude (num.) & 85 vs.\ 100 & 4146 & $<$0.001 & $-$0.30 \\ Claude (qual.) & 85 vs.\ 100 & 3880 & 0.024 & $-$0.21 \\ \bottomrule \end{tabular} \capti |
| `0.05` | sections/appendix.tex:198 | mean or delta | yes | rows listed are those that also survive Benjamini--Hochberg control across all tests in the analysis at $q < 0.05$. Because the two corrections are ap |
| `0.74` | sections/appendix.tex:20 | mean or delta | yes | **}$ & $3.94^{***}$ & --- \\ threshold & $-0.93^{***}$ & $-1.04^{***}$ & $-1.65^{***}$ \\ is\_qualitative & $-0.74^{***}$ & $-0.85^{***}$ & $-1.05^{** |
| `0.85` | sections/appendix.tex:20 | mean or delta | yes | *}$ & --- \\ threshold & $-0.93^{***}$ & $-1.04^{***}$ & $-1.65^{***}$ \\ is\_qualitative & $-0.74^{***}$ & $-0.85^{***}$ & $-1.05^{***}$ \\ Claude So |
| `1.05` | sections/appendix.tex:20 | mean or delta | yes | eshold & $-0.93^{***}$ & $-1.04^{***}$ & $-1.65^{***}$ \\ is\_qualitative & $-0.74^{***}$ & $-0.85^{***}$ & $-1.05^{***}$ \\ Claude Sonnet & $0.10$ &  |
| `0.05` | sections/appendix.tex:204 | percentage |  | listed.} \label{tab:pairwise} \end{table} \subsection{Power Analysis} Post-hoc power analysis at $\alpha = 0.05$, 80\% power: \begin{itemize} \item \t |
| `80` | sections/appendix.tex:204 | percentage |  | .} \label{tab:pairwise} \end{table} \subsection{Power Analysis} Post-hoc power analysis at $\alpha = 0.05$, 80\% power: \begin{itemize} \item \textbf{ |
| `1` | sections/appendix.tex:206 | percentage |  | er Analysis} Post-hoc power analysis at $\alpha = 0.05$, 80\% power: \begin{itemize} \item \textbf{Study~1 RQ1} ($N = 1{,}920$ per probe): MDE for pro |
| `1` | sections/appendix.tex:206 | percentage |  | Post-hoc power analysis at $\alpha = 0.05$, 80\% power: \begin{itemize} \item \textbf{Study~1 RQ1} ($N = 1{,}920$ per probe): MDE for proportion diffe |
| `920` | sections/appendix.tex:206 | percentage |  | t-hoc power analysis at $\alpha = 0.05$, 80\% power: \begin{itemize} \item \textbf{Study~1 RQ1} ($N = 1{,}920$ per probe): MDE for proportion differen |
| `0.032` | sections/appendix.tex:206 | count or denominator |  | r: \begin{itemize} \item \textbf{Study~1 RQ1} ($N = 1{,}920$ per probe): MDE for proportion difference $= 0.032$. Observed $\approx 0.75$, over twenty |
| `0.75` | sections/appendix.tex:206 | count or denominator |  | em \textbf{Study~1 RQ1} ($N = 1{,}920$ per probe): MDE for proportion difference $= 0.032$. Observed $\approx 0.75$, over twenty times the minimum. \i |
| `1` | sections/appendix.tex:207 | count or denominator |  | portion difference $= 0.032$. Observed $\approx 0.75$, over twenty times the minimum. \item \textbf{Study~1 RQ2} ($N = 1{,}920$ leading-probe): MDE fo |
| `1` | sections/appendix.tex:207 | count or denominator |  | rence $= 0.032$. Observed $\approx 0.75$, over twenty times the minimum. \item \textbf{Study~1 RQ2} ($N = 1{,}920$ leading-probe): MDE for $|\rho| = 0 |
| `920` | sections/appendix.tex:207 | count or denominator |  | e $= 0.032$. Observed $\approx 0.75$, over twenty times the minimum. \item \textbf{Study~1 RQ2} ($N = 1{,}920$ leading-probe): MDE for $|\rho| = 0.064 |
| `0.064` | sections/appendix.tex:207 | count or denominator |  | ver twenty times the minimum. \item \textbf{Study~1 RQ2} ($N = 1{,}920$ leading-probe): MDE for $|\rho| = 0.064$. All observed correlations exceed thi |
| `3` | sections/appendix.tex:208 | count or denominator |  | 920$ leading-probe): MDE for $|\rho| = 0.064$. All observed correlations exceed this. \item \textbf{Study~3} ($N = 720$ trials, balanced panel $n = 50 |
| `720` | sections/appendix.tex:208 | count or denominator |  | ing-probe): MDE for $|\rho| = 0.064$. All observed correlations exceed this. \item \textbf{Study~3} ($N = 720$ trials, balanced panel $n = 50$): Panel |
| `50` | sections/appendix.tex:208 | count or denominator |  | 64$. All observed correlations exceed this. \item \textbf{Study~3} ($N = 720$ trials, balanced panel $n = 50$): Panel-level MDE $= 0.5$ levels on the  |
| `0.5` | sections/appendix.tex:208 | count or denominator |  | tions exceed this. \item \textbf{Study~3} ($N = 720$ trials, balanced panel $n = 50$): Panel-level MDE $= 0.5$ levels on the ordinal scale. The observ |
| `0.44` | sections/appendix.tex:208 | count or denominator |  | nel $n = 50$): Panel-level MDE $= 0.5$ levels on the ordinal scale. The observed ordinal decline is $\Delta = 0.44$ unstripped and $0.38$ stripped, bo |
| `0.38` | sections/appendix.tex:208 | count or denominator |  | evel MDE $= 0.5$ levels on the ordinal scale. The observed ordinal decline is $\Delta = 0.44$ unstripped and $0.38$ stripped, both below that MDE, so  |
| `50` | sections/appendix.tex:208 | count or denominator |  | = 0.44$ unstripped and $0.38$ stripped, both below that MDE, so the ordinal magnitude is not powered at $n = 50$ and is reported as a supporting estim |
| `19` | sections/appendix.tex:208 | p-value |  | owered at $n = 50$ and is reported as a supporting estimate rather than as the finding. The count is powered: 19 of 50 trials became over-elaborated a |
| `50` | sections/appendix.tex:208 | p-value |  | at $n = 50$ and is reported as a supporting estimate rather than as the finding. The count is powered: 19 of 50 trials became over-elaborated against  |
| `1` | sections/appendix.tex:208 | p-value |  | ing estimate rather than as the finding. The count is powered: 19 of 50 trials became over-elaborated against 1 the other way, exact binomial $p = 4.0 |
| `4.01` | sections/appendix.tex:208 | p-value |  | ng. The count is powered: 19 of 50 trials became over-elaborated against 1 the other way, exact binomial $p = 4.01 \times 10^{-5}$. On the paired ordi |
| `10` | sections/appendix.tex:208 | p-value |  | t is powered: 19 of 50 trials became over-elaborated against 1 the other way, exact binomial $p = 4.01 \times 10^{-5}$. On the paired ordinal test the |
| `5` | sections/appendix.tex:208 | p-value |  | powered: 19 of 50 trials became over-elaborated against 1 the other way, exact binomial $p = 4.01 \times 10^{-5}$. On the paired ordinal test the unst |
| `3.79` | sections/appendix.tex:208 | p-value |  | her way, exact binomial $p = 4.01 \times 10^{-5}$. On the paired ordinal test the unstripped cliff gives $p = 3.79 \times 10^{-4}$ (Wilcoxon, $r = 0.5 |
| `10` | sections/appendix.tex:208 | p-value |  | ct binomial $p = 4.01 \times 10^{-5}$. On the paired ordinal test the unstripped cliff gives $p = 3.79 \times 10^{-4}$ (Wilcoxon, $r = 0.50$ on $N = 5 |
| `4` | sections/appendix.tex:208 | p-value |  | nomial $p = 4.01 \times 10^{-5}$. On the paired ordinal test the unstripped cliff gives $p = 3.79 \times 10^{-4}$ (Wilcoxon, $r = 0.50$ on $N = 50$) a |
| `0.50` | sections/appendix.tex:208 | p-value |  | mes 10^{-5}$. On the paired ordinal test the unstripped cliff gives $p = 3.79 \times 10^{-4}$ (Wilcoxon, $r = 0.50$ on $N = 50$) and the stripped clif |
| `50` | sections/appendix.tex:208 | p-value |  | On the paired ordinal test the unstripped cliff gives $p = 3.79 \times 10^{-4}$ (Wilcoxon, $r = 0.50$ on $N = 50$) and the stripped cliff $p = 4.42 \t |
| `4.42` | sections/appendix.tex:208 | p-value |  | stripped cliff gives $p = 3.79 \times 10^{-4}$ (Wilcoxon, $r = 0.50$ on $N = 50$) and the stripped cliff $p = 4.42 \times 10^{-3}$ ($r = 0.40$). \end{ |
| `10` | sections/appendix.tex:208 | p-value |  | ff gives $p = 3.79 \times 10^{-4}$ (Wilcoxon, $r = 0.50$ on $N = 50$) and the stripped cliff $p = 4.42 \times 10^{-3}$ ($r = 0.40$). \end{itemize} \se |
| `3` | sections/appendix.tex:208 | p-value |  | ves $p = 3.79 \times 10^{-4}$ (Wilcoxon, $r = 0.50$ on $N = 50$) and the stripped cliff $p = 4.42 \times 10^{-3}$ ($r = 0.40$). \end{itemize} \section |
| `0.40` | sections/appendix.tex:208 | p-value |  | .79 \times 10^{-4}$ (Wilcoxon, $r = 0.50$ on $N = 50$) and the stripped cliff $p = 4.42 \times 10^{-3}$ ($r = 0.40$). \end{itemize} \section{Evaluator |
| `0.10` | sections/appendix.tex:21 | mean or delta | yes | {***}$ & $-1.65^{***}$ \\ is\_qualitative & $-0.74^{***}$ & $-0.85^{***}$ & $-1.05^{***}$ \\ Claude Sonnet & $0.10$ & $0.15$ & $0.33^{**}$ \\ Gemini F |
| `0.15` | sections/appendix.tex:21 | mean or delta | yes | $-1.65^{***}$ \\ is\_qualitative & $-0.74^{***}$ & $-0.85^{***}$ & $-1.05^{***}$ \\ Claude Sonnet & $0.10$ & $0.15$ & $0.33^{**}$ \\ Gemini Flash & $0 |
| `0.33` | sections/appendix.tex:21 | mean or delta | yes | **}$ \\ is\_qualitative & $-0.74^{***}$ & $-0.85^{***}$ & $-1.05^{***}$ \\ Claude Sonnet & $0.10$ & $0.15$ & $0.33^{**}$ \\ Gemini Flash & $0.42^{***} |
| `0.42` | sections/appendix.tex:22 | mean or delta | yes | 74^{***}$ & $-0.85^{***}$ & $-1.05^{***}$ \\ Claude Sonnet & $0.10$ & $0.15$ & $0.33^{**}$ \\ Gemini Flash & $0.42^{***}$ & $0.52^{***}$ & $1.15^{***} |
| `0.52` | sections/appendix.tex:22 | mean or delta | yes | .85^{***}$ & $-1.05^{***}$ \\ Claude Sonnet & $0.10$ & $0.15$ & $0.33^{**}$ \\ Gemini Flash & $0.42^{***}$ & $0.52^{***}$ & $1.15^{***}$ \\ Scenario F |
| `1.15` | sections/appendix.tex:22 | mean or delta | yes | 1.05^{***}$ \\ Claude Sonnet & $0.10$ & $0.15$ & $0.33^{**}$ \\ Gemini Flash & $0.42^{***}$ & $0.52^{***}$ & $1.15^{***}$ \\ Scenario FEs & No & Yes & |
| `4` | sections/appendix.tex:222 | reliability or effect size | yes | }} \toprule \textbf{Candidate Judge} & \textbf{Spearman $r$} & \textbf{QW $\kappa$} \\ \midrule Claude Sonnet 4 & $0.505$ & $0.526$ \\ DeepSeek V4 Fla |
| `0.505` | sections/appendix.tex:222 | reliability or effect size | yes | oprule \textbf{Candidate Judge} & \textbf{Spearman $r$} & \textbf{QW $\kappa$} \\ \midrule Claude Sonnet 4 & $0.505$ & $0.526$ \\ DeepSeek V4 Flash &  |
| `0.526` | sections/appendix.tex:222 | reliability or effect size | yes | xtbf{Candidate Judge} & \textbf{Spearman $r$} & \textbf{QW $\kappa$} \\ \midrule Claude Sonnet 4 & $0.505$ & $0.526$ \\ DeepSeek V4 Flash & $0.340$ &  |
| `0.340` | sections/appendix.tex:223 | reliability or effect size | yes | {Spearman $r$} & \textbf{QW $\kappa$} \\ \midrule Claude Sonnet 4 & $0.505$ & $0.526$ \\ DeepSeek V4 Flash & $0.340$ & $0.398$ \\ Qwen 3 235B & $0.272 |
| `0.398` | sections/appendix.tex:223 | reliability or effect size | yes | $r$} & \textbf{QW $\kappa$} \\ \midrule Claude Sonnet 4 & $0.505$ & $0.526$ \\ DeepSeek V4 Flash & $0.340$ & $0.398$ \\ Qwen 3 235B & $0.272$ & $0.017 |
| `3` | sections/appendix.tex:224 | reliability or effect size | yes | QW $\kappa$} \\ \midrule Claude Sonnet 4 & $0.505$ & $0.526$ \\ DeepSeek V4 Flash & $0.340$ & $0.398$ \\ Qwen 3 235B & $0.272$ & $0.017$ \\ Llama 3.3  |
| `0.272` | sections/appendix.tex:224 | mean or delta | yes | $} \\ \midrule Claude Sonnet 4 & $0.505$ & $0.526$ \\ DeepSeek V4 Flash & $0.340$ & $0.398$ \\ Qwen 3 235B & $0.272$ & $0.017$ \\ Llama 3.3 70B & $0.1 |
| `0.017` | sections/appendix.tex:224 | mean or delta | yes | rule Claude Sonnet 4 & $0.505$ & $0.526$ \\ DeepSeek V4 Flash & $0.340$ & $0.398$ \\ Qwen 3 235B & $0.272$ & $0.017$ \\ Llama 3.3 70B & $0.181$ & $0.0 |
| `3.3` | sections/appendix.tex:225 | mean or delta | yes | et 4 & $0.505$ & $0.526$ \\ DeepSeek V4 Flash & $0.340$ & $0.398$ \\ Qwen 3 235B & $0.272$ & $0.017$ \\ Llama 3.3 70B & $0.181$ & $0.022$ \\ GPT-4o &  |
| `0.181` | sections/appendix.tex:225 | mean or delta | yes | 05$ & $0.526$ \\ DeepSeek V4 Flash & $0.340$ & $0.398$ \\ Qwen 3 235B & $0.272$ & $0.017$ \\ Llama 3.3 70B & $0.181$ & $0.022$ \\ GPT-4o & $0.140$ & $ |
| `0.022` | sections/appendix.tex:225 | mean or delta | yes | 26$ \\ DeepSeek V4 Flash & $0.340$ & $0.398$ \\ Qwen 3 235B & $0.272$ & $0.017$ \\ Llama 3.3 70B & $0.181$ & $0.022$ \\ GPT-4o & $0.140$ & $0.065$ \\  |
| `0.140` | sections/appendix.tex:226 | mean or delta | yes | lash & $0.340$ & $0.398$ \\ Qwen 3 235B & $0.272$ & $0.017$ \\ Llama 3.3 70B & $0.181$ & $0.022$ \\ GPT-4o & $0.140$ & $0.065$ \\ Gemini 2.5 Flash & $ |
| `0.065` | sections/appendix.tex:226 | mean or delta | yes | 340$ & $0.398$ \\ Qwen 3 235B & $0.272$ & $0.017$ \\ Llama 3.3 70B & $0.181$ & $0.022$ \\ GPT-4o & $0.140$ & $0.065$ \\ Gemini 2.5 Flash & $-0.036$ &  |
| `2.5` | sections/appendix.tex:227 | count or denominator | yes | Qwen 3 235B & $0.272$ & $0.017$ \\ Llama 3.3 70B & $0.181$ & $0.022$ \\ GPT-4o & $0.140$ & $0.065$ \\ Gemini 2.5 Flash & $-0.036$ & $-0.026$ \\ \botto |
| `0.036` | sections/appendix.tex:227 | count or denominator | yes | $0.272$ & $0.017$ \\ Llama 3.3 70B & $0.181$ & $0.022$ \\ GPT-4o & $0.140$ & $0.065$ \\ Gemini 2.5 Flash & $-0.036$ & $-0.026$ \\ \bottomrule \end{tab |
| `0.026` | sections/appendix.tex:227 | reliability or effect size | yes | $0.017$ \\ Llama 3.3 70B & $0.181$ & $0.022$ \\ GPT-4o & $0.140$ & $0.065$ \\ Gemini 2.5 Flash & $-0.036$ & $-0.026$ \\ \bottomrule \end{tabular} \cap |
| `64` | sections/appendix.tex:230 | reliability or effect size | yes | Gemini 2.5 Flash & $-0.036$ & $-0.026$ \\ \bottomrule \end{tabular} \caption{Judge calibration results ($n = 64$ stratified samples each; Spearman cor |
| `4` | sections/appendix.tex:230 | reliability or effect size | yes | results ($n = 64$ stratified samples each; Spearman correlation against the human rater mean). Claude Sonnet~4 was selected as the Study~3 evaluator,  |
| `3` | sections/appendix.tex:230 | p-value | yes | d samples each; Spearman correlation against the human rater mean). Claude Sonnet~4 was selected as the Study~3 evaluator, with the highest human corr |
| `0.505` | sections/appendix.tex:230 | p-value | yes | onnet~4 was selected as the Study~3 evaluator, with the highest human correlation of the six candidates ($r = 0.505$, $p = 2.1 \times 10^{-5}$). Gemin |
| `2.1` | sections/appendix.tex:230 | p-value | yes | elected as the Study~3 evaluator, with the highest human correlation of the six candidates ($r = 0.505$, $p = 2.1 \times 10^{-5}$). Gemini 2.5 Flash w |
| `10` | sections/appendix.tex:230 | p-value | yes | the Study~3 evaluator, with the highest human correlation of the six candidates ($r = 0.505$, $p = 2.1 \times 10^{-5}$). Gemini 2.5 Flash was anti-cor |
| `5` | sections/appendix.tex:230 | p-value | yes | tudy~3 evaluator, with the highest human correlation of the six candidates ($r = 0.505$, $p = 2.1 \times 10^{-5}$). Gemini 2.5 Flash was anti-correlat |
| `2.5` | sections/appendix.tex:230 | p-value | yes | tor, with the highest human correlation of the six candidates ($r = 0.505$, $p = 2.1 \times 10^{-5}$). Gemini 2.5 Flash was anti-correlated with human |
| `0.502` | sections/appendix.tex:244 | percentage | yes | n{tabular}{@{}lrrr@{}} \toprule Rater pair & QW $\kappa$ & Binary & Within 1 \\ \midrule Rater A -- Rater B & 0.502 & 78.1\% & 95.3\% \\ Rater B -- Ra |
| `78.1` | sections/appendix.tex:244 | percentage | yes | r}{@{}lrrr@{}} \toprule Rater pair & QW $\kappa$ & Binary & Within 1 \\ \midrule Rater A -- Rater B & 0.502 & 78.1\% & 95.3\% \\ Rater B -- Rater C &  |
| `95.3` | sections/appendix.tex:244 | percentage | yes | r@{}} \toprule Rater pair & QW $\kappa$ & Binary & Within 1 \\ \midrule Rater A -- Rater B & 0.502 & 78.1\% & 95.3\% \\ Rater B -- Rater C & 0.612 & 8 |
| `0.612` | sections/appendix.tex:245 | percentage | yes | $\kappa$ & Binary & Within 1 \\ \midrule Rater A -- Rater B & 0.502 & 78.1\% & 95.3\% \\ Rater B -- Rater C & 0.612 & 82.8\% & 93.8\% \\ Rater A -- Ra |
| `82.8` | sections/appendix.tex:245 | percentage | yes | & Binary & Within 1 \\ \midrule Rater A -- Rater B & 0.502 & 78.1\% & 95.3\% \\ Rater B -- Rater C & 0.612 & 82.8\% & 93.8\% \\ Rater A -- Rater C & 0 |
| `93.8` | sections/appendix.tex:245 | percentage | yes | & Within 1 \\ \midrule Rater A -- Rater B & 0.502 & 78.1\% & 95.3\% \\ Rater B -- Rater C & 0.612 & 82.8\% & 93.8\% \\ Rater A -- Rater C & 0.478 & 76 |
| `0.478` | sections/appendix.tex:246 | percentage | yes | -- Rater B & 0.502 & 78.1\% & 95.3\% \\ Rater B -- Rater C & 0.612 & 82.8\% & 93.8\% \\ Rater A -- Rater C & 0.478 & 76.6\% & 95.3\% \\ \midrule All t |
| `76.6` | sections/appendix.tex:246 | percentage | yes | r B & 0.502 & 78.1\% & 95.3\% \\ Rater B -- Rater C & 0.612 & 82.8\% & 93.8\% \\ Rater A -- Rater C & 0.478 & 76.6\% & 95.3\% \\ \midrule All three ($ |
| `95.3` | sections/appendix.tex:246 | percentage | yes | 02 & 78.1\% & 95.3\% \\ Rater B -- Rater C & 0.612 & 82.8\% & 93.8\% \\ Rater A -- Rater C & 0.478 & 76.6\% & 95.3\% \\ \midrule All three ($\alpha$)  |
| `0.540` | sections/appendix.tex:248 | percentage | yes | & 0.612 & 82.8\% & 93.8\% \\ Rater A -- Rater C & 0.478 & 76.6\% & 95.3\% \\ \midrule All three ($\alpha$) & 0.540 & --- & --- \\ Evaluator -- Human M |
| `3,840` | sections/appendix.tex:25 | mean or delta | yes | Gemini Flash & $0.42^{***}$ & $0.52^{***}$ & $1.15^{***}$ \\ Scenario FEs & No & Yes & Yes \\ \midrule $N$ & 3,840 & 3,840 & 1,920 \\ AIC & 5,319 & 4, |
| `3,840` | sections/appendix.tex:25 | mean or delta | yes | Flash & $0.42^{***}$ & $0.52^{***}$ & $1.15^{***}$ \\ Scenario FEs & No & Yes & Yes \\ \midrule $N$ & 3,840 & 3,840 & 1,920 \\ AIC & 5,319 & 4,839 & 3 |
| `1,920` | sections/appendix.tex:25 | mean or delta | yes | $0.42^{***}$ & $0.52^{***}$ & $1.15^{***}$ \\ Scenario FEs & No & Yes & Yes \\ \midrule $N$ & 3,840 & 3,840 & 1,920 \\ AIC & 5,319 & 4,839 & 3,545 \\  |
| `0.001` | sections/appendix.tex:252 | p-value | yes | q 4$) vs.\ not. Within-1: ratings differ by $\leq 1$ level. Evaluator--Human Mean: Spearman $r = 0.505$ ($p < 0.001$).} \label{tab:human-agreement} \e |
| `60` | sections/appendix.tex:259 | count or denominator |  | mentum} report quadratic-weighted agreement between two independent model judges on a stratified subsample of 60 outputs from each of Studies~1 and~2. |
| `1` | sections/appendix.tex:259 | count or denominator |  | d agreement between two independent model judges on a stratified subsample of 60 outputs from each of Studies~1 and~2. Threshold alignment is the leas |
| `2` | sections/appendix.tex:259 | count or denominator |  | ement between two independent model judges on a stratified subsample of 60 outputs from each of Studies~1 and~2. Threshold alignment is the least reli |
| `5,319` | sections/appendix.tex:26 | mean or delta | yes | $0.52^{***}$ & $1.15^{***}$ \\ Scenario FEs & No & Yes & Yes \\ \midrule $N$ & 3,840 & 3,840 & 1,920 \\ AIC & 5,319 & 4,839 & 3,545 \\ \bottomrule \en |
| `4,839` | sections/appendix.tex:26 | mean or delta | yes | **}$ & $1.15^{***}$ \\ Scenario FEs & No & Yes & Yes \\ \midrule $N$ & 3,840 & 3,840 & 1,920 \\ AIC & 5,319 & 4,839 & 3,545 \\ \bottomrule \end{tabula |
| `3,545` | sections/appendix.tex:26 | mean or delta | yes | 1.15^{***}$ \\ Scenario FEs & No & Yes & Yes \\ \midrule $N$ & 3,840 & 3,840 & 1,920 \\ AIC & 5,319 & 4,839 & 3,545 \\ \bottomrule \end{tabular} \capt |
| `0.844` | sections/appendix.tex:268 | reliability or effect size | yes | \toprule \textbf{Dimension} & \textbf{QW $\kappa$} & \textbf{Interpretation} \\ \midrule Revision magnitude & 0.844 & Excellent \\ Revision value & 0. |
| `0.690` | sections/appendix.tex:269 | reliability or effect size | yes | QW $\kappa$} & \textbf{Interpretation} \\ \midrule Revision magnitude & 0.844 & Excellent \\ Revision value & 0.690 & Good \\ Overcorrection & 0.609 & |
| `0.609` | sections/appendix.tex:270 | mean or delta | yes | tion} \\ \midrule Revision magnitude & 0.844 & Excellent \\ Revision value & 0.690 & Good \\ Overcorrection & 0.609 & Acceptable \\ Threshold alignmen |
| `0.556` | sections/appendix.tex:271 | mean or delta | yes | & Excellent \\ Revision value & 0.690 & Good \\ Overcorrection & 0.609 & Acceptable \\ Threshold alignment & 0.556 & Marginal \\ \bottomrule \end{tabu |
| `1` | sections/appendix.tex:274 | count or denominator | yes | hreshold alignment & 0.556 & Marginal \\ \bottomrule \end{tabular} \caption{Inter-rater reliability for Study~1 (GPT-4o vs.\ Claude Sonnet~4, $n = 60$ |
| `4` | sections/appendix.tex:274 | count or denominator | yes | Marginal \\ \bottomrule \end{tabular} \caption{Inter-rater reliability for Study~1 (GPT-4o vs.\ Claude Sonnet~4, $n = 60$).} \label{tab:irr} \end{tabl |
| `60` | sections/appendix.tex:274 | count or denominator | yes | \\ \bottomrule \end{tabular} \caption{Inter-rater reliability for Study~1 (GPT-4o vs.\ Claude Sonnet~4, $n = 60$).} \label{tab:irr} \end{table} \begin |
| `1` | sections/appendix.tex:283 | percentage | yes | bular}{@{}lccc@{}} \toprule \textbf{Dimension} & \textbf{QW $\kappa$} & \textbf{\% Agree} & \textbf{\% Within 1} \\ \midrule Revision magnitude & 0.57 |
| `0.575` | sections/appendix.tex:285 | percentage | yes | Dimension} & \textbf{QW $\kappa$} & \textbf{\% Agree} & \textbf{\% Within 1} \\ \midrule Revision magnitude & 0.575 & 68.3 & 85.0 \\ Revision value &  |
| `68.3` | sections/appendix.tex:285 | percentage | yes | n} & \textbf{QW $\kappa$} & \textbf{\% Agree} & \textbf{\% Within 1} \\ \midrule Revision magnitude & 0.575 & 68.3 & 85.0 \\ Revision value & 0.669 &  |
| `85.0` | sections/appendix.tex:285 | percentage | yes | extbf{QW $\kappa$} & \textbf{\% Agree} & \textbf{\% Within 1} \\ \midrule Revision magnitude & 0.575 & 68.3 & 85.0 \\ Revision value & 0.669 & 76.7 &  |
| `0.669` | sections/appendix.tex:286 | percentage | yes | tbf{\% Agree} & \textbf{\% Within 1} \\ \midrule Revision magnitude & 0.575 & 68.3 & 85.0 \\ Revision value & 0.669 & 76.7 & 88.3 \\ Overcorrection &  |
| `76.7` | sections/appendix.tex:286 | percentage | yes | gree} & \textbf{\% Within 1} \\ \midrule Revision magnitude & 0.575 & 68.3 & 85.0 \\ Revision value & 0.669 & 76.7 & 88.3 \\ Overcorrection & 0.392 &  |
| `88.3` | sections/appendix.tex:286 | percentage | yes | \textbf{\% Within 1} \\ \midrule Revision magnitude & 0.575 & 68.3 & 85.0 \\ Revision value & 0.669 & 76.7 & 88.3 \\ Overcorrection & 0.392 & 71.7 & 9 |
| `0.392` | sections/appendix.tex:287 | mean or delta | yes | \midrule Revision magnitude & 0.575 & 68.3 & 85.0 \\ Revision value & 0.669 & 76.7 & 88.3 \\ Overcorrection & 0.392 & 71.7 & 90.0 \\ Threshold alignme |
| `71.7` | sections/appendix.tex:287 | mean or delta | yes | Revision magnitude & 0.575 & 68.3 & 85.0 \\ Revision value & 0.669 & 76.7 & 88.3 \\ Overcorrection & 0.392 & 71.7 & 90.0 \\ Threshold alignment & 0.33 |
| `90.0` | sections/appendix.tex:287 | mean or delta | yes | on magnitude & 0.575 & 68.3 & 85.0 \\ Revision value & 0.669 & 76.7 & 88.3 \\ Overcorrection & 0.392 & 71.7 & 90.0 \\ Threshold alignment & 0.339 & 38 |
| `0.339` | sections/appendix.tex:288 | count or denominator | yes | 85.0 \\ Revision value & 0.669 & 76.7 & 88.3 \\ Overcorrection & 0.392 & 71.7 & 90.0 \\ Threshold alignment & 0.339 & 38.3 & 85.0 \\ \bottomrule \end{ |
| `38.3` | sections/appendix.tex:288 | count or denominator | yes | Revision value & 0.669 & 76.7 & 88.3 \\ Overcorrection & 0.392 & 71.7 & 90.0 \\ Threshold alignment & 0.339 & 38.3 & 85.0 \\ \bottomrule \end{tabular} |
| `85.0` | sections/appendix.tex:288 | count or denominator | yes | n value & 0.669 & 76.7 & 88.3 \\ Overcorrection & 0.392 & 71.7 & 90.0 \\ Threshold alignment & 0.339 & 38.3 & 85.0 \\ \bottomrule \end{tabular} \capti |
| `0.01` | sections/appendix.tex:29 | p-value | yes | tabular} \caption{Ordinal regression (overcorrection $\sim$ predictors). Model C: leading-probe only. $^{**}p<0.01$, $^{***}p<0.001$. Reference: GPT-4 |
| `0.001` | sections/appendix.tex:29 | p-value | yes | n{Ordinal regression (overcorrection $\sim$ predictors). Model C: leading-probe only. $^{**}p<0.01$, $^{***}p<0.001$. Reference: GPT-4o.} \label{tab:r |
| `2` | sections/appendix.tex:291 | count or denominator | yes | shold alignment & 0.339 & 38.3 & 85.0 \\ \bottomrule \end{tabular} \caption{Inter-rater reliability for Study~2 ($n = 60$).} \label{tab:irr-momentum}  |
| `60` | sections/appendix.tex:291 | count or denominator | yes | ignment & 0.339 & 38.3 & 85.0 \\ \bottomrule \end{tabular} \caption{Inter-rater reliability for Study~2 ($n = 60$).} \label{tab:irr-momentum} \end{tab |
| `3.3` | sections/appendix.tex:310 | percentage | yes | \toprule & $n$ & \% down & $p$ \\ \midrule \multicolumn{4}{@{}l}{\emph{By model}} \\ Llama 3.3 70B & 353 & 68.9 & $<0.001$ \\ Claude Sonnet 4 & 196 &  |
| `353` | sections/appendix.tex:310 | percentage | yes | & $n$ & \% down & $p$ \\ \midrule \multicolumn{4}{@{}l}{\emph{By model}} \\ Llama 3.3 70B & 353 & 68.9 & $<0.001$ \\ Claude Sonnet 4 & 196 & 58.5 & 0. |
| `68.9` | sections/appendix.tex:310 | percentage | yes | n$ & \% down & $p$ \\ \midrule \multicolumn{4}{@{}l}{\emph{By model}} \\ Llama 3.3 70B & 353 & 68.9 & $<0.001$ \\ Claude Sonnet 4 & 196 & 58.5 & 0.11  |
| `0.001` | sections/appendix.tex:310 | mean or delta | yes | own & $p$ \\ \midrule \multicolumn{4}{@{}l}{\emph{By model}} \\ Llama 3.3 70B & 353 & 68.9 & $<0.001$ \\ Claude Sonnet 4 & 196 & 58.5 & 0.11 \\ Qwen 3 |
| `4` | sections/appendix.tex:311 | mean or delta | yes | \multicolumn{4}{@{}l}{\emph{By model}} \\ Llama 3.3 70B & 353 & 68.9 & $<0.001$ \\ Claude Sonnet 4 & 196 & 58.5 & 0.11 \\ Qwen 3 235B & 90 & 74.5 & $< |
| `196` | sections/appendix.tex:311 | mean or delta | yes | lticolumn{4}{@{}l}{\emph{By model}} \\ Llama 3.3 70B & 353 & 68.9 & $<0.001$ \\ Claude Sonnet 4 & 196 & 58.5 & 0.11 \\ Qwen 3 235B & 90 & 74.5 & $<0.0 |
| `58.5` | sections/appendix.tex:311 | mean or delta | yes | umn{4}{@{}l}{\emph{By model}} \\ Llama 3.3 70B & 353 & 68.9 & $<0.001$ \\ Claude Sonnet 4 & 196 & 58.5 & 0.11 \\ Qwen 3 235B & 90 & 74.5 & $<0.001$ \\ |
| `0.11` | sections/appendix.tex:311 | mean or delta | yes | @{}l}{\emph{By model}} \\ Llama 3.3 70B & 353 & 68.9 & $<0.001$ \\ Claude Sonnet 4 & 196 & 58.5 & 0.11 \\ Qwen 3 235B & 90 & 74.5 & $<0.001$ \\ GPT-4o |
| `3` | sections/appendix.tex:312 | mean or delta | yes | del}} \\ Llama 3.3 70B & 353 & 68.9 & $<0.001$ \\ Claude Sonnet 4 & 196 & 58.5 & 0.11 \\ Qwen 3 235B & 90 & 74.5 & $<0.001$ \\ GPT-4o & 40 & 80.0 & 0. |
| `90` | sections/appendix.tex:312 | mean or delta | yes | lama 3.3 70B & 353 & 68.9 & $<0.001$ \\ Claude Sonnet 4 & 196 & 58.5 & 0.11 \\ Qwen 3 235B & 90 & 74.5 & $<0.001$ \\ GPT-4o & 40 & 80.0 & 0.006 \\ Dee |
| `74.5` | sections/appendix.tex:312 | mean or delta | yes | .3 70B & 353 & 68.9 & $<0.001$ \\ Claude Sonnet 4 & 196 & 58.5 & 0.11 \\ Qwen 3 235B & 90 & 74.5 & $<0.001$ \\ GPT-4o & 40 & 80.0 & 0.006 \\ DeepSeek- |
| `0.001` | sections/appendix.tex:312 | mean or delta | yes | & 353 & 68.9 & $<0.001$ \\ Claude Sonnet 4 & 196 & 58.5 & 0.11 \\ Qwen 3 235B & 90 & 74.5 & $<0.001$ \\ GPT-4o & 40 & 80.0 & 0.006 \\ DeepSeek-V4-Flas |
| `40` | sections/appendix.tex:313 | mean or delta | yes | laude Sonnet 4 & 196 & 58.5 & 0.11 \\ Qwen 3 235B & 90 & 74.5 & $<0.001$ \\ GPT-4o & 40 & 80.0 & 0.006 \\ DeepSeek-V4-Flash & 31 & 85.7 & 0.007 \\ Gem |
| `80.0` | sections/appendix.tex:313 | mean or delta | yes | Sonnet 4 & 196 & 58.5 & 0.11 \\ Qwen 3 235B & 90 & 74.5 & $<0.001$ \\ GPT-4o & 40 & 80.0 & 0.006 \\ DeepSeek-V4-Flash & 31 & 85.7 & 0.007 \\ Gemini 2. |
| `0.006` | sections/appendix.tex:313 | mean or delta | yes | 4 & 196 & 58.5 & 0.11 \\ Qwen 3 235B & 90 & 74.5 & $<0.001$ \\ GPT-4o & 40 & 80.0 & 0.006 \\ DeepSeek-V4-Flash & 31 & 85.7 & 0.007 \\ Gemini 2.5 Flash |
| `31` | sections/appendix.tex:314 | mean or delta | yes | n 3 235B & 90 & 74.5 & $<0.001$ \\ GPT-4o & 40 & 80.0 & 0.006 \\ DeepSeek-V4-Flash & 31 & 85.7 & 0.007 \\ Gemini 2.5 Flash & 8 & 100.0 & 0.062 \\ \mid |
| `85.7` | sections/appendix.tex:314 | mean or delta | yes | 5B & 90 & 74.5 & $<0.001$ \\ GPT-4o & 40 & 80.0 & 0.006 \\ DeepSeek-V4-Flash & 31 & 85.7 & 0.007 \\ Gemini 2.5 Flash & 8 & 100.0 & 0.062 \\ \midrule \ |
| `0.007` | sections/appendix.tex:314 | mean or delta | yes | & 90 & 74.5 & $<0.001$ \\ GPT-4o & 40 & 80.0 & 0.006 \\ DeepSeek-V4-Flash & 31 & 85.7 & 0.007 \\ Gemini 2.5 Flash & 8 & 100.0 & 0.062 \\ \midrule \mul |
| `2.5` | sections/appendix.tex:315 | mean or delta | yes | 001$ \\ GPT-4o & 40 & 80.0 & 0.006 \\ DeepSeek-V4-Flash & 31 & 85.7 & 0.007 \\ Gemini 2.5 Flash & 8 & 100.0 & 0.062 \\ \midrule \multicolumn{4}{@{}l}{ |
| `8` | sections/appendix.tex:315 | mean or delta | yes | GPT-4o & 40 & 80.0 & 0.006 \\ DeepSeek-V4-Flash & 31 & 85.7 & 0.007 \\ Gemini 2.5 Flash & 8 & 100.0 & 0.062 \\ \midrule \multicolumn{4}{@{}l}{\emph{By |
| `100.0` | sections/appendix.tex:315 | mean or delta | yes | & 40 & 80.0 & 0.006 \\ DeepSeek-V4-Flash & 31 & 85.7 & 0.007 \\ Gemini 2.5 Flash & 8 & 100.0 & 0.062 \\ \midrule \multicolumn{4}{@{}l}{\emph{By domain |
| `0.062` | sections/appendix.tex:315 | mean or delta | yes | & 40 & 80.0 & 0.006 \\ DeepSeek-V4-Flash & 31 & 85.7 & 0.007 \\ Gemini 2.5 Flash & 8 & 100.0 & 0.062 \\ \midrule \multicolumn{4}{@{}l}{\emph{By domain |
| `4` | sections/appendix.tex:317 | mean or delta | yes | -V4-Flash & 31 & 85.7 & 0.007 \\ Gemini 2.5 Flash & 8 & 100.0 & 0.062 \\ \midrule \multicolumn{4}{@{}l}{\emph{By domain}} \\ Writing & 118 & 79.1 & $< |
| `118` | sections/appendix.tex:318 | mean or delta | yes | h & 8 & 100.0 & 0.062 \\ \midrule \multicolumn{4}{@{}l}{\emph{By domain}} \\ Writing & 118 & 79.1 & $<0.001$ \\ Creative & 145 & 73.1 & $<0.001$ \\ Co |
| `79.1` | sections/appendix.tex:318 | mean or delta | yes | & 100.0 & 0.062 \\ \midrule \multicolumn{4}{@{}l}{\emph{By domain}} \\ Writing & 118 & 79.1 & $<0.001$ \\ Creative & 145 & 73.1 & $<0.001$ \\ Code & 1 |
| `0.001` | sections/appendix.tex:318 | mean or delta | yes | & 0.062 \\ \midrule \multicolumn{4}{@{}l}{\emph{By domain}} \\ Writing & 118 & 79.1 & $<0.001$ \\ Creative & 145 & 73.1 & $<0.001$ \\ Code & 196 & 67. |
| `145` | sections/appendix.tex:319 | mean or delta | yes | ticolumn{4}{@{}l}{\emph{By domain}} \\ Writing & 118 & 79.1 & $<0.001$ \\ Creative & 145 & 73.1 & $<0.001$ \\ Code & 196 & 67.0 & $<0.001$ \\ Analysis |
| `73.1` | sections/appendix.tex:319 | mean or delta | yes | mn{4}{@{}l}{\emph{By domain}} \\ Writing & 118 & 79.1 & $<0.001$ \\ Creative & 145 & 73.1 & $<0.001$ \\ Code & 196 & 67.0 & $<0.001$ \\ Analysis & 125 |
| `0.001` | sections/appendix.tex:319 | mean or delta | yes | l}{\emph{By domain}} \\ Writing & 118 & 79.1 & $<0.001$ \\ Creative & 145 & 73.1 & $<0.001$ \\ Code & 196 & 67.0 & $<0.001$ \\ Analysis & 125 & 65.9 & |
| `196` | sections/appendix.tex:320 | mean or delta | yes | ng & 118 & 79.1 & $<0.001$ \\ Creative & 145 & 73.1 & $<0.001$ \\ Code & 196 & 67.0 & $<0.001$ \\ Analysis & 125 & 65.9 & 0.024 \\ Data logic & 134 &  |
| `67.0` | sections/appendix.tex:320 | mean or delta | yes | & 118 & 79.1 & $<0.001$ \\ Creative & 145 & 73.1 & $<0.001$ \\ Code & 196 & 67.0 & $<0.001$ \\ Analysis & 125 & 65.9 & 0.024 \\ Data logic & 134 & 65. |
| `0.001` | sections/appendix.tex:320 | mean or delta | yes | 18 & 79.1 & $<0.001$ \\ Creative & 145 & 73.1 & $<0.001$ \\ Code & 196 & 67.0 & $<0.001$ \\ Analysis & 125 & 65.9 & 0.024 \\ Data logic & 134 & 65.9 & |
| `125` | sections/appendix.tex:321 | mean or delta | yes | ive & 145 & 73.1 & $<0.001$ \\ Code & 196 & 67.0 & $<0.001$ \\ Analysis & 125 & 65.9 & 0.024 \\ Data logic & 134 & 65.9 & 0.024 \\ \bottomrule \end{ta |
| `65.9` | sections/appendix.tex:321 | mean or delta | yes | & 145 & 73.1 & $<0.001$ \\ Code & 196 & 67.0 & $<0.001$ \\ Analysis & 125 & 65.9 & 0.024 \\ Data logic & 134 & 65.9 & 0.024 \\ \bottomrule \end{tabula |
| `0.024` | sections/appendix.tex:321 | mean or delta | yes | 145 & 73.1 & $<0.001$ \\ Code & 196 & 67.0 & $<0.001$ \\ Analysis & 125 & 65.9 & 0.024 \\ Data logic & 134 & 65.9 & 0.024 \\ \bottomrule \end{tabular} |
| `134` | sections/appendix.tex:322 | mean or delta | yes | de & 196 & 67.0 & $<0.001$ \\ Analysis & 125 & 65.9 & 0.024 \\ Data logic & 134 & 65.9 & 0.024 \\ \bottomrule \end{tabular} \caption{Direction of genu |
| `65.9` | sections/appendix.tex:322 | mean or delta | yes | & 196 & 67.0 & $<0.001$ \\ Analysis & 125 & 65.9 & 0.024 \\ Data logic & 134 & 65.9 & 0.024 \\ \bottomrule \end{tabular} \caption{Direction of genuine |
| `0.024` | sections/appendix.tex:322 | mean or delta | yes | & 196 & 67.0 & $<0.001$ \\ Analysis & 125 & 65.9 & 0.024 \\ Data logic & 134 & 65.9 & 0.024 \\ \bottomrule \end{tabular} \caption{Direction of genuine |
| `2` | sections/appendix.tex:327 | mean or delta | yes | ; the percentage is computed over the subset whose quality level moves. Sign test, one-sided. A $\chi^2$ test of homogeneity across the five domains d |
| `2` | sections/appendix.tex:328 | p-value | yes | , one-sided. A $\chi^2$ test of homogeneity across the five domains does not reject uniformity ($\chi^2 = 3.02$, $\mathrm{df} = 4$, $p = 0.555$).} \la |
| `3.02` | sections/appendix.tex:328 | p-value | yes | e-sided. A $\chi^2$ test of homogeneity across the five domains does not reject uniformity ($\chi^2 = 3.02$, $\mathrm{df} = 4$, $p = 0.555$).} \label{ |
| `4` | sections/appendix.tex:328 | p-value | yes | $ test of homogeneity across the five domains does not reject uniformity ($\chi^2 = 3.02$, $\mathrm{df} = 4$, $p = 0.555$).} \label{tab:direction} \en |
| `0.555` | sections/appendix.tex:328 | p-value | yes | homogeneity across the five domains does not reject uniformity ($\chi^2 = 3.02$, $\mathrm{df} = 4$, $p = 0.555$).} \label{tab:direction} \end{table} \ |
| `4.17` | sections/appendix.tex:339 | mean or delta | yes | \begin{tabular}{lcccc} \toprule Turn & Stripped & (Unstripped) & Shift & $n$ \\ \midrule T1 & 4.17 & (4.17) & 0 & 720 \\ T2 & 3.84 & (3.59) & +0.25 &  |
| `4.17` | sections/appendix.tex:339 | mean or delta | yes | abular}{lcccc} \toprule Turn & Stripped & (Unstripped) & Shift & $n$ \\ \midrule T1 & 4.17 & (4.17) & 0 & 720 \\ T2 & 3.84 & (3.59) & +0.25 & 283 \\ T |
| `0` | sections/appendix.tex:339 | mean or delta | yes | lcccc} \toprule Turn & Stripped & (Unstripped) & Shift & $n$ \\ \midrule T1 & 4.17 & (4.17) & 0 & 720 \\ T2 & 3.84 & (3.59) & +0.25 & 283 \\ T3 & 3.69 |
| `720` | sections/appendix.tex:339 | mean or delta | yes | c} \toprule Turn & Stripped & (Unstripped) & Shift & $n$ \\ \midrule T1 & 4.17 & (4.17) & 0 & 720 \\ T2 & 3.84 & (3.59) & +0.25 & 283 \\ T3 & 3.69 & ( |
| `99.9` | sections/appendix.tex:34 | percentage |  | ange (``Can this be improved?'' and ``Is there anything you would change?'') trigger near-universal revision (99.9\%, $n = 1{,}920$; 100\%, $n = 18$). |
| `1` | sections/appendix.tex:34 | percentage |  | his be improved?'' and ``Is there anything you would change?'') trigger near-universal revision (99.9\%, $n = 1{,}920$; 100\%, $n = 18$). The three pr |
| `920` | sections/appendix.tex:34 | percentage |  | be improved?'' and ``Is there anything you would change?'') trigger near-universal revision (99.9\%, $n = 1{,}920$; 100\%, $n = 18$). The three probes |
| `100` | sections/appendix.tex:34 | percentage |  | roved?'' and ``Is there anything you would change?'') trigger near-universal revision (99.9\%, $n = 1{,}920$; 100\%, $n = 18$). The three probes that  |
| `18` | sections/appendix.tex:34 | percentage |  | ``Is there anything you would change?'') trigger near-universal revision (99.9\%, $n = 1{,}920$; 100\%, $n = 18$). The three probes that request asses |
| `23.2` | sections/appendix.tex:34 | percentage |  | Does it meet the bar?,'' and ``What do you think?'') produce single-digit to low-double-digit revision rates (23.2\%, $n = 1{,}920$; 12.5\%, $n = 24$; |
| `1` | sections/appendix.tex:34 | percentage |  | the bar?,'' and ``What do you think?'') produce single-digit to low-double-digit revision rates (23.2\%, $n = 1{,}920$; 12.5\%, $n = 24$; 2.0\%, $n =  |
| `920` | sections/appendix.tex:34 | percentage |  | bar?,'' and ``What do you think?'') produce single-digit to low-double-digit revision rates (23.2\%, $n = 1{,}920$; 12.5\%, $n = 24$; 2.0\%, $n = 50$) |
| `12.5` | sections/appendix.tex:34 | percentage |  | ' and ``What do you think?'') produce single-digit to low-double-digit revision rates (23.2\%, $n = 1{,}920$; 12.5\%, $n = 24$; 2.0\%, $n = 50$). No p |
| `24` | sections/appendix.tex:34 | percentage |  | do you think?'') produce single-digit to low-double-digit revision rates (23.2\%, $n = 1{,}920$; 12.5\%, $n = 24$; 2.0\%, $n = 50$). No probe falls in |
| `2.0` | sections/appendix.tex:34 | percentage |  | u think?'') produce single-digit to low-double-digit revision rates (23.2\%, $n = 1{,}920$; 12.5\%, $n = 24$; 2.0\%, $n = 50$). No probe falls in the  |
| `50` | sections/appendix.tex:34 | percentage |  | produce single-digit to low-double-digit revision rates (23.2\%, $n = 1{,}920$; 12.5\%, $n = 24$; 2.0\%, $n = 50$). No probe falls in the 40--99\% ran |
| `40` | sections/appendix.tex:34 | percentage |  | double-digit revision rates (23.2\%, $n = 1{,}920$; 12.5\%, $n = 24$; 2.0\%, $n = 50$). No probe falls in the 40--99\% range; the gate is semantic, no |
| `99` | sections/appendix.tex:34 | percentage |  | le-digit revision rates (23.2\%, $n = 1{,}920$; 12.5\%, $n = 24$; 2.0\%, $n = 50$). No probe falls in the 40--99\% range; the gate is semantic, not gr |
| `3` | sections/appendix.tex:34 | percentage |  | \%, $n = 24$; 2.0\%, $n = 50$). No probe falls in the 40--99\% range; the gate is semantic, not graded. Study~3's balanced probe (``Would you like to  |
| `3.84` | sections/appendix.tex:340 | mean or delta | yes | Turn & Stripped & (Unstripped) & Shift & $n$ \\ \midrule T1 & 4.17 & (4.17) & 0 & 720 \\ T2 & 3.84 & (3.59) & +0.25 & 283 \\ T3 & 3.69 & (3.43) & +0.2 |
| `3.59` | sections/appendix.tex:340 | mean or delta | yes | & Stripped & (Unstripped) & Shift & $n$ \\ \midrule T1 & 4.17 & (4.17) & 0 & 720 \\ T2 & 3.84 & (3.59) & +0.25 & 283 \\ T3 & 3.69 & (3.43) & +0.25 & 1 |
| `0.25` | sections/appendix.tex:340 | mean or delta | yes | ed & (Unstripped) & Shift & $n$ \\ \midrule T1 & 4.17 & (4.17) & 0 & 720 \\ T2 & 3.84 & (3.59) & +0.25 & 283 \\ T3 & 3.69 & (3.43) & +0.25 & 185 \\ T4 |
| `283` | sections/appendix.tex:340 | mean or delta | yes | nstripped) & Shift & $n$ \\ \midrule T1 & 4.17 & (4.17) & 0 & 720 \\ T2 & 3.84 & (3.59) & +0.25 & 283 \\ T3 & 3.69 & (3.43) & +0.25 & 185 \\ T4 & 3.62 |
| `3.69` | sections/appendix.tex:341 | mean or delta | yes | ft & $n$ \\ \midrule T1 & 4.17 & (4.17) & 0 & 720 \\ T2 & 3.84 & (3.59) & +0.25 & 283 \\ T3 & 3.69 & (3.43) & +0.25 & 185 \\ T4 & 3.62 & (3.40) & +0.2 |
| `3.43` | sections/appendix.tex:341 | mean or delta | yes | \\ \midrule T1 & 4.17 & (4.17) & 0 & 720 \\ T2 & 3.84 & (3.59) & +0.25 & 283 \\ T3 & 3.69 & (3.43) & +0.25 & 185 \\ T4 & 3.62 & (3.40) & +0.22 & 154 \ |
| `0.25` | sections/appendix.tex:341 | mean or delta | yes | midrule T1 & 4.17 & (4.17) & 0 & 720 \\ T2 & 3.84 & (3.59) & +0.25 & 283 \\ T3 & 3.69 & (3.43) & +0.25 & 185 \\ T4 & 3.62 & (3.40) & +0.22 & 154 \\ T5 |
| `185` | sections/appendix.tex:341 | mean or delta | yes | T1 & 4.17 & (4.17) & 0 & 720 \\ T2 & 3.84 & (3.59) & +0.25 & 283 \\ T3 & 3.69 & (3.43) & +0.25 & 185 \\ T4 & 3.62 & (3.40) & +0.22 & 154 \\ T5 & 3.42  |
| `3.62` | sections/appendix.tex:342 | mean or delta | yes | (4.17) & 0 & 720 \\ T2 & 3.84 & (3.59) & +0.25 & 283 \\ T3 & 3.69 & (3.43) & +0.25 & 185 \\ T4 & 3.62 & (3.40) & +0.22 & 154 \\ T5 & 3.42 & (3.33) & + |
| `3.40` | sections/appendix.tex:342 | mean or delta | yes | & 0 & 720 \\ T2 & 3.84 & (3.59) & +0.25 & 283 \\ T3 & 3.69 & (3.43) & +0.25 & 185 \\ T4 & 3.62 & (3.40) & +0.22 & 154 \\ T5 & 3.42 & (3.33) & +0.08 &  |
| `0.22` | sections/appendix.tex:342 | mean or delta | yes | \\ T2 & 3.84 & (3.59) & +0.25 & 283 \\ T3 & 3.69 & (3.43) & +0.25 & 185 \\ T4 & 3.62 & (3.40) & +0.22 & 154 \\ T5 & 3.42 & (3.33) & +0.08 & 96 \\ \mid |
| `154` | sections/appendix.tex:342 | mean or delta | yes | T2 & 3.84 & (3.59) & +0.25 & 283 \\ T3 & 3.69 & (3.43) & +0.25 & 185 \\ T4 & 3.62 & (3.40) & +0.22 & 154 \\ T5 & 3.42 & (3.33) & +0.08 & 96 \\ \midrul |
| `3.42` | sections/appendix.tex:343 | mean or delta | yes | 59) & +0.25 & 283 \\ T3 & 3.69 & (3.43) & +0.25 & 185 \\ T4 & 3.62 & (3.40) & +0.22 & 154 \\ T5 & 3.42 & (3.33) & +0.08 & 96 \\ \midrule $\Delta$ (T1- |
| `3.33` | sections/appendix.tex:343 | mean or delta | yes | .25 & 283 \\ T3 & 3.69 & (3.43) & +0.25 & 185 \\ T4 & 3.62 & (3.40) & +0.22 & 154 \\ T5 & 3.42 & (3.33) & +0.08 & 96 \\ \midrule $\Delta$ (T1--T5) & $ |
| `0.08` | sections/appendix.tex:343 | mean or delta | yes | \\ T3 & 3.69 & (3.43) & +0.25 & 185 \\ T4 & 3.62 & (3.40) & +0.22 & 154 \\ T5 & 3.42 & (3.33) & +0.08 & 96 \\ \midrule $\Delta$ (T1--T5) & $\mathbf{-0 |
| `96` | sections/appendix.tex:343 | mean or delta | yes | T3 & 3.69 & (3.43) & +0.25 & 185 \\ T4 & 3.62 & (3.40) & +0.22 & 154 \\ T5 & 3.42 & (3.33) & +0.08 & 96 \\ \midrule $\Delta$ (T1--T5) & $\mathbf{-0.75 |
| `0.75` | sections/appendix.tex:345 | mean or delta | yes | (3.40) & +0.22 & 154 \\ T5 & 3.42 & (3.33) & +0.08 & 96 \\ \midrule $\Delta$ (T1--T5) & $\mathbf{-0.75}$ & ($-0.84$) & & \\ \bottomrule \end{tabular}  |
| `0.84` | sections/appendix.tex:345 | mean or delta | yes | 22 & 154 \\ T5 & 3.42 & (3.33) & +0.08 & 96 \\ \midrule $\Delta$ (T1--T5) & $\mathbf{-0.75}$ & ($-0.84$) & & \\ \bottomrule \end{tabular} \caption{Poo |
| `720` | sections/appendix.tex:348 | bare number | yes | bular} \caption{Pooled mean quality by turn, restricted to genuine revisions (GENUINE-only at T2--T5, all 720 at T1). Stripped scores are primary. $n$ |
| `0.59` | sections/appendix.tex:360 | mean or delta | yes | r}{lrrr} \toprule Domain & $\Delta$ (T1--T5) & $p$ & $n_{\text{T5}}$ \\ \midrule analysis & $-0.59$ & 0.004 & 17 \\ code & $-0.47$ & 0.035 & 30 \\ cre |
| `0.004` | sections/appendix.tex:360 | mean or delta | yes | \toprule Domain & $\Delta$ (T1--T5) & $p$ & $n_{\text{T5}}$ \\ \midrule analysis & $-0.59$ & 0.004 & 17 \\ code & $-0.47$ & 0.035 & 30 \\ creative & $ |
| `17` | sections/appendix.tex:360 | mean or delta | yes | prule Domain & $\Delta$ (T1--T5) & $p$ & $n_{\text{T5}}$ \\ \midrule analysis & $-0.59$ & 0.004 & 17 \\ code & $-0.47$ & 0.035 & 30 \\ creative & $-0. |
| `0.47` | sections/appendix.tex:361 | mean or delta | yes | $\Delta$ (T1--T5) & $p$ & $n_{\text{T5}}$ \\ \midrule analysis & $-0.59$ & 0.004 & 17 \\ code & $-0.47$ & 0.035 & 30 \\ creative & $-0.32$ & 0.058 & 1 |
| `0.035` | sections/appendix.tex:361 | mean or delta | yes | (T1--T5) & $p$ & $n_{\text{T5}}$ \\ \midrule analysis & $-0.59$ & 0.004 & 17 \\ code & $-0.47$ & 0.035 & 30 \\ creative & $-0.32$ & 0.058 & 19 \\ data |
| `30` | sections/appendix.tex:361 | mean or delta | yes | ) & $p$ & $n_{\text{T5}}$ \\ \midrule analysis & $-0.59$ & 0.004 & 17 \\ code & $-0.47$ & 0.035 & 30 \\ creative & $-0.32$ & 0.058 & 19 \\ data\_logic |
| `0.32` | sections/appendix.tex:362 | mean or delta | yes | }$ \\ \midrule analysis & $-0.59$ & 0.004 & 17 \\ code & $-0.47$ & 0.035 & 30 \\ creative & $-0.32$ & 0.058 & 19 \\ data\_logic & $-0.24$ & 0.206 & 17 |
| `0.058` | sections/appendix.tex:362 | mean or delta | yes | \midrule analysis & $-0.59$ & 0.004 & 17 \\ code & $-0.47$ & 0.035 & 30 \\ creative & $-0.32$ & 0.058 & 19 \\ data\_logic & $-0.24$ & 0.206 & 17 \\ wr |
| `19` | sections/appendix.tex:362 | mean or delta | yes | le analysis & $-0.59$ & 0.004 & 17 \\ code & $-0.47$ & 0.035 & 30 \\ creative & $-0.32$ & 0.058 & 19 \\ data\_logic & $-0.24$ & 0.206 & 17 \\ writing  |
| `0.24` | sections/appendix.tex:363 | mean or delta | yes | & 0.004 & 17 \\ code & $-0.47$ & 0.035 & 30 \\ creative & $-0.32$ & 0.058 & 19 \\ data\_logic & $-0.24$ & 0.206 & 17 \\ writing & $-0.77$ & 0.004 & 13 |
| `0.206` | sections/appendix.tex:363 | mean or delta | yes | & 17 \\ code & $-0.47$ & 0.035 & 30 \\ creative & $-0.32$ & 0.058 & 19 \\ data\_logic & $-0.24$ & 0.206 & 17 \\ writing & $-0.77$ & 0.004 & 13 \\ \bot |
| `17` | sections/appendix.tex:363 | mean or delta | yes | code & $-0.47$ & 0.035 & 30 \\ creative & $-0.32$ & 0.058 & 19 \\ data\_logic & $-0.24$ & 0.206 & 17 \\ writing & $-0.77$ & 0.004 & 13 \\ \bottomrule  |
| `1` | sections/appendix.tex:4 | bare number |  | \section{Study 1: The Revision Gate} \label{sec:appendix-study1} Study~1 tests whether user-stated quality thresholds constrain the decision to revise |
| `8` | sections/appendix.tex:4 | bare number |  | sts whether user-stated quality thresholds constrain the decision to revise. In a fully factorial experiment (8 scenarios $\times$ 16 threshold condit |
| `16` | sections/appendix.tex:4 | bare number |  | ed quality thresholds constrain the decision to revise. In a fully factorial experiment (8 scenarios $\times$ 16 threshold conditions $\times$ 2 probe |
| `2` | sections/appendix.tex:4 | bare number |  | he decision to revise. In a fully factorial experiment (8 scenarios $\times$ 16 threshold conditions $\times$ 2 probes $\times$ 3 models $\times$ 5 ru |
| `3` | sections/appendix.tex:4 | bare number |  | ise. In a fully factorial experiment (8 scenarios $\times$ 16 threshold conditions $\times$ 2 probes $\times$ 3 models $\times$ 5 runs $=$ 3,840 trial |
| `5` | sections/appendix.tex:4 | bare number |  | ctorial experiment (8 scenarios $\times$ 16 threshold conditions $\times$ 2 probes $\times$ 3 models $\times$ 5 runs $=$ 3,840 trials), the follow-up  |
| `3,840` | sections/appendix.tex:4 | bare number |  | eriment (8 scenarios $\times$ 16 threshold conditions $\times$ 2 probes $\times$ 3 models $\times$ 5 runs $=$ 3,840 trials), the follow-up probe's phr |
| `99.9` | sections/appendix.tex:4 | percentage |  | e's phrasing dominates the revision gate. Under the leading probe (``Can this be improved?''), models revised 99.9\% of the time regardless of thresho |
| `2.5` | sections/appendix.tex:4 | percentage |  | valuative probe (``Take another look and let me know if it's ready''), revision rates varied by model: Gemini~2.5 Flash declined 99.7\%, GPT-4o 68.6\% |
| `99.7` | sections/appendix.tex:4 | percentage |  | Take another look and let me know if it's ready''), revision rates varied by model: Gemini~2.5 Flash declined 99.7\%, GPT-4o 68.6\%, Claude Sonnet~4 6 |
| `68.6` | sections/appendix.tex:4 | percentage |  | ok and let me know if it's ready''), revision rates varied by model: Gemini~2.5 Flash declined 99.7\%, GPT-4o 68.6\%, Claude Sonnet~4 62.0\%. Chi-squa |
| `4` | sections/appendix.tex:4 | percentage |  | it's ready''), revision rates varied by model: Gemini~2.5 Flash declined 99.7\%, GPT-4o 68.6\%, Claude Sonnet~4 62.0\%. Chi-squared tests confirm the  |
| `62.0` | sections/appendix.tex:4 | percentage |  | 's ready''), revision rates varied by model: Gemini~2.5 Flash declined 99.7\%, GPT-4o 68.6\%, Claude Sonnet~4 62.0\%. Chi-squared tests confirm the re |
| `3.3` | sections/appendix.tex:404 | mean or delta |  | ogether AI.} \label{tab:endpoints} \end{table} \paragraph{Parameters.} Published for three of the six: Llama~3.3~70B at 70B, Qwen~3~235B at 235B total |
| `3` | sections/appendix.tex:404 | mean or delta |  | ab:endpoints} \end{table} \paragraph{Parameters.} Published for three of the six: Llama~3.3~70B at 70B, Qwen~3~235B at 235B total with 22B active, and |
| `4` | sections/appendix.tex:406 | mean or delta |  | 35B at 235B total with 22B active, and DeepSeek~V4 Flash at 284B total with 13B active. GPT-4o, Claude Sonnet~4 and Gemini~2.5 Flash are closed and th |
| `2.5` | sections/appendix.tex:406 | mean or delta |  | otal with 22B active, and DeepSeek~V4 Flash at 284B total with 13B active. GPT-4o, Claude Sonnet~4 and Gemini~2.5 Flash are closed and their parameter |
| `720` | sections/appendix.tex:408 | mean or delta |  | nnet~4 and Gemini~2.5 Flash are closed and their parameter counts are not published. \paragraph{Budget.} The 720 Study~3 conversations consumed 3,016, |
| `3` | sections/appendix.tex:408 | mean or delta |  | Gemini~2.5 Flash are closed and their parameter counts are not published. \paragraph{Budget.} The 720 Study~3 conversations consumed 3,016,008 input a |
| `3,016,008` | sections/appendix.tex:408 | bare number |  | sed and their parameter counts are not published. \paragraph{Budget.} The 720 Study~3 conversations consumed 3,016,008 input and 1,050,833 output toke |
| `1,050,833` | sections/appendix.tex:408 | bare number |  | ter counts are not published. \paragraph{Budget.} The 720 Study~3 conversations consumed 3,016,008 input and 1,050,833 output tokens. The evaluation,  |
| `1` | sections/appendix.tex:411 | bare number |  | cord token counts, so the project total is higher than this and is not recoverable from what was saved. Study~1 ran 3,840 primary trials and Study~2 a |
| `3,840` | sections/appendix.tex:411 | bare number |  | oken counts, so the project total is higher than this and is not recoverable from what was saved. Study~1 ran 3,840 primary trials and Study~2 analyse |
| `2` | sections/appendix.tex:411 | bare number |  | al is higher than this and is not recoverable from what was saved. Study~1 ran 3,840 primary trials and Study~2 analysed 1,813. Generation was capped  |
| `1,813` | sections/appendix.tex:411 | bare number |  | r than this and is not recoverable from what was saved. Study~1 ran 3,840 primary trials and Study~2 analysed 1,813. Generation was capped at 8,192 ou |
| `8,192` | sections/appendix.tex:411 | mean or delta |  | le from what was saved. Study~1 ran 3,840 primary trials and Study~2 analysed 1,813. Generation was capped at 8,192 output tokens per call and judging |
| `512` | sections/appendix.tex:412 | mean or delta |  | imary trials and Study~2 analysed 1,813. Generation was capped at 8,192 output tokens per call and judging at 512. \paragraph{Settings.} Generation ra |
| `1.0` | sections/appendix.tex:414 | mean or delta |  | pped at 8,192 output tokens per call and judging at 512. \paragraph{Settings.} Generation ran at temperature~1.0 and evaluation at temperature~0. No h |
| `0` | sections/appendix.tex:414 | mean or delta |  | ll and judging at 512. \paragraph{Settings.} Generation ran at temperature~1.0 and evaluation at temperature~0. No hyperparameter search was performed |
| `2` | sections/appendix.tex:43 | count or denominator |  | $n = 720$), consistent with this pattern. \section{Study 2: Momentum} \label{sec:appendix-study2} Study~2 tests whether prior revision rounds shift th |
| `1,728` | sections/appendix.tex:43 | bare number |  | tudy2} Study~2 tests whether prior revision rounds shift the revision gate on a subsequent evaluative probe (1,728 trials by design; 1,813 completed a |
| `1,813` | sections/appendix.tex:43 | bare number |  | ether prior revision rounds shift the revision gate on a subsequent evaluative probe (1,728 trials by design; 1,813 completed and analysed). The dose~ |
| `0` | sections/appendix.tex:43 | bare number |  | vision gate on a subsequent evaluative probe (1,728 trials by design; 1,813 completed and analysed). The dose~0 baseline is the Study~1 evaluative-pro |
| `1` | sections/appendix.tex:43 | percentage |  | ent evaluative probe (1,728 trials by design; 1,813 completed and analysed). The dose~0 baseline is the Study~1 evaluative-probe arm rather than a cel |
| `23.2` | sections/appendix.tex:43 | p-value |  | ne is the Study~1 evaluative-probe arm rather than a cell of this run. Without prior revision, models revised 23.2\% there; after 1--3 prior rounds, t |
| `1` | sections/appendix.tex:43 | p-value |  | aluative-probe arm rather than a cell of this run. Without prior revision, models revised 23.2\% there; after 1--3 prior rounds, this rises to 44.6\%  |
| `3` | sections/appendix.tex:43 | p-value |  | ative-probe arm rather than a cell of this run. Without prior revision, models revised 23.2\% there; after 1--3 prior rounds, this rises to 44.6\% ($\ |
| `44.6` | sections/appendix.tex:43 | p-value |  | cell of this run. Without prior revision, models revised 23.2\% there; after 1--3 prior rounds, this rises to 44.6\% ($\chi^2 = 376.54$, $p < 0.0001$) |
| `2` | sections/appendix.tex:43 | p-value |  | un. Without prior revision, models revised 23.2\% there; after 1--3 prior rounds, this rises to 44.6\% ($\chi^2 = 376.54$, $p < 0.0001$). The shift va |
| `376.54` | sections/appendix.tex:43 | p-value |  | Without prior revision, models revised 23.2\% there; after 1--3 prior rounds, this rises to 44.6\% ($\chi^2 = 376.54$, $p < 0.0001$). The shift varies |
| `0.0001` | sections/appendix.tex:43 | p-value |  | revision, models revised 23.2\% there; after 1--3 prior rounds, this rises to 44.6\% ($\chi^2 = 376.54$, $p < 0.0001$). The shift varies by model: \be |
| `31.4` | sections/appendix.tex:47 | p-value |  | es to 44.6\% ($\chi^2 = 376.54$, $p < 0.0001$). The shift varies by model: \begin{itemize} \item GPT-4o: 31.4\% $\to$ 98.4\% at dose~1 (near-total com |
| `98.4` | sections/appendix.tex:47 | p-value |  | ($\chi^2 = 376.54$, $p < 0.0001$). The shift varies by model: \begin{itemize} \item GPT-4o: 31.4\% $\to$ 98.4\% at dose~1 (near-total compliance at do |
| `1` | sections/appendix.tex:47 | p-value |  | 54$, $p < 0.0001$). The shift varies by model: \begin{itemize} \item GPT-4o: 31.4\% $\to$ 98.4\% at dose~1 (near-total compliance at dose~1) \item Cla |
| `1` | sections/appendix.tex:47 | percentage |  | ries by model: \begin{itemize} \item GPT-4o: 31.4\% $\to$ 98.4\% at dose~1 (near-total compliance at dose~1) \item Claude Sonnet~4: 38.0\% $\to$ 24.5\ |
| `4` | sections/appendix.tex:48 | percentage |  | ze} \item GPT-4o: 31.4\% $\to$ 98.4\% at dose~1 (near-total compliance at dose~1) \item Claude Sonnet~4: 38.0\% $\to$ 24.5\% at dose~3 (declines under |
| `38.0` | sections/appendix.tex:48 | percentage |  | \item GPT-4o: 31.4\% $\to$ 98.4\% at dose~1 (near-total compliance at dose~1) \item Claude Sonnet~4: 38.0\% $\to$ 24.5\% at dose~3 (declines under mom |
| `24.5` | sections/appendix.tex:48 | percentage |  | T-4o: 31.4\% $\to$ 98.4\% at dose~1 (near-total compliance at dose~1) \item Claude Sonnet~4: 38.0\% $\to$ 24.5\% at dose~3 (declines under momentum) \ |
| `3` | sections/appendix.tex:48 | percentage |  | to$ 98.4\% at dose~1 (near-total compliance at dose~1) \item Claude Sonnet~4: 38.0\% $\to$ 24.5\% at dose~3 (declines under momentum) \item Gemini~2.5 |
| `2.5` | sections/appendix.tex:49 | percentage |  | t dose~1) \item Claude Sonnet~4: 38.0\% $\to$ 24.5\% at dose~3 (declines under momentum) \item Gemini~2.5 Flash: 0.3\% $\to$ 12.8\% at dose~1 (modest  |
| `0.3` | sections/appendix.tex:49 | percentage |  | \item Claude Sonnet~4: 38.0\% $\to$ 24.5\% at dose~3 (declines under momentum) \item Gemini~2.5 Flash: 0.3\% $\to$ 12.8\% at dose~1 (modest shift from |
| `12.8` | sections/appendix.tex:49 | percentage |  | ude Sonnet~4: 38.0\% $\to$ 24.5\% at dose~3 (declines under momentum) \item Gemini~2.5 Flash: 0.3\% $\to$ 12.8\% at dose~1 (modest shift from near-zer |
| `1` | sections/appendix.tex:49 | percentage |  | 8.0\% $\to$ 24.5\% at dose~3 (declines under momentum) \item Gemini~2.5 Flash: 0.3\% $\to$ 12.8\% at dose~1 (modest shift from near-zero) \end{itemize |
| `0` | sections/appendix.tex:52 | p-value |  | t from near-zero) \end{itemize} The momentum effect is a step function: the entire shift occurs between dose~0 and dose~1, with no additional gain at  |
| `1` | sections/appendix.tex:52 | p-value |  | -zero) \end{itemize} The momentum effect is a step function: the entire shift occurs between dose~0 and dose~1, with no additional gain at higher dose |
| `0.51` | sections/appendix.tex:52 | p-value |  | ~0 and dose~1, with no additional gain at higher doses. Threshold level does not interact with momentum ($p = 0.51$). \paragraph{Reverse Momentum.} A  |
| `0.0` | sections/appendix.tex:54 | percentage |  | d'') drives full revision to zero in all three models. What revision remains is minor suggestion only: Gemini 0.0\%, GPT-4o 1.0\%, Claude 21.9\%. The  |
| `1.0` | sections/appendix.tex:54 | percentage |  | ll revision to zero in all three models. What revision remains is minor suggestion only: Gemini 0.0\%, GPT-4o 1.0\%, Claude 21.9\%. The gate follows t |
| `21.9` | sections/appendix.tex:54 | percentage |  | zero in all three models. What revision remains is minor suggestion only: Gemini 0.0\%, GPT-4o 1.0\%, Claude 21.9\%. The gate follows the most recent  |
| `1` | sections/appendix.tex:57 | bare number |  | conversational signal in both directions. \section{Procedure Diagrams} The two diagrams below show the Study~1 factorial design and the Study~3 turn s |
| `3` | sections/appendix.tex:57 | bare number |  | ections. \section{Procedure Diagrams} The two diagrams below show the Study~1 factorial design and the Study~3 turn structure. \label{sec:appendix-pip |
| `2` | sections/appendix.tex:6 | p-value |  | 62.0\%. Chi-squared tests confirm the revision gate distribution differs significantly by probe type ($\chi^2 > 788$, $p < 0.0001$ for all models). Qu |
| `788` | sections/appendix.tex:6 | p-value |  | 0\%. Chi-squared tests confirm the revision gate distribution differs significantly by probe type ($\chi^2 > 788$, $p < 0.0001$ for all models). Quali |
| `0.0001` | sections/appendix.tex:6 | p-value |  | quared tests confirm the revision gate distribution differs significantly by probe type ($\chi^2 > 788$, $p < 0.0001$ for all models). Quality thresho |
| `1.42` | sections/appendix.tex:6 | p-value |  | e gate. Coding the three gate outcomes ordinally, Kruskal-Wallis across the eight threshold levels gives $H = 1.42$, $p = 0.99$ for Gemini~2.5 Flash a |
| `0.99` | sections/appendix.tex:6 | p-value |  | ng the three gate outcomes ordinally, Kruskal-Wallis across the eight threshold levels gives $H = 1.42$, $p = 0.99$ for Gemini~2.5 Flash and $H = 2.01 |
| `2.5` | sections/appendix.tex:6 | p-value |  | outcomes ordinally, Kruskal-Wallis across the eight threshold levels gives $H = 1.42$, $p = 0.99$ for Gemini~2.5 Flash and $H = 2.01$, $p = 0.96$ for  |
| `2.01` | sections/appendix.tex:6 | p-value |  | , Kruskal-Wallis across the eight threshold levels gives $H = 1.42$, $p = 0.99$ for Gemini~2.5 Flash and $H = 2.01$, $p = 0.96$ for GPT-4o; only Claud |
| `0.96` | sections/appendix.tex:6 | p-value |  | llis across the eight threshold levels gives $H = 1.42$, $p = 0.99$ for Gemini~2.5 Flash and $H = 2.01$, $p = 0.96$ for GPT-4o; only Claude Sonnet~4 r |
| `4` | sections/appendix.tex:6 | p-value |  | s gives $H = 1.42$, $p = 0.99$ for Gemini~2.5 Flash and $H = 2.01$, $p = 0.96$ for GPT-4o; only Claude Sonnet~4 reaches significance, at $H = 14.33$,  |
| `14.33` | sections/appendix.tex:6 | p-value |  | or Gemini~2.5 Flash and $H = 2.01$, $p = 0.96$ for GPT-4o; only Claude Sonnet~4 reaches significance, at $H = 14.33$, $p = 0.046$. On the same factori |
| `0.046` | sections/appendix.tex:6 | p-value |  | Flash and $H = 2.01$, $p = 0.96$ for GPT-4o; only Claude Sonnet~4 reaches significance, at $H = 14.33$, $p = 0.046$. On the same factorial scope the p |
| `2` | sections/appendix.tex:6 | p-value |  | Sonnet~4 reaches significance, at $H = 14.33$, $p = 0.046$. On the same factorial scope the probe-type $\chi^2$ runs from 742 to 1,268, so phrasing mo |
| `742` | sections/appendix.tex:6 | p-value |  | ches significance, at $H = 14.33$, $p = 0.046$. On the same factorial scope the probe-type $\chi^2$ runs from 742 to 1,268, so phrasing moves the gate |
| `1,268` | sections/appendix.tex:6 | p-value |  | gnificance, at $H = 14.33$, $p = 0.046$. On the same factorial scope the probe-type $\chi^2$ runs from 742 to 1,268, so phrasing moves the gate where  |
| `0.50` | sections/appendix.tex:8 | reliability or effect size |  | leading-probe condition, higher thresholds produce moderately less overcorrection (Spearman $\rho$: Gemini $-0.50$, Claude $-0.35$, GPT-4o $-0.14$), b |
| `0.35` | sections/appendix.tex:8 | reliability or effect size |  | ondition, higher thresholds produce moderately less overcorrection (Spearman $\rho$: Gemini $-0.50$, Claude $-0.35$, GPT-4o $-0.14$), but this calibra |
| `0.14` | sections/appendix.tex:8 | reliability or effect size |  | thresholds produce moderately less overcorrection (Spearman $\rho$: Gemini $-0.50$, Claude $-0.35$, GPT-4o $-0.14$), but this calibration is hidden be |
| `4` | sections/conclusion.tex:3 | p-value |  | evise drift. Sufficient work is not made incomplete but over-elaborated, the share rated Overdone rising from 4\% to 40\% ($p = 4.0 \times 10^{-5}$),  |
| `40` | sections/conclusion.tex:3 | p-value |  | rift. Sufficient work is not made incomplete but over-elaborated, the share rated Overdone rising from 4\% to 40\% ($p = 4.0 \times 10^{-5}$), a fall  |
| `4.0` | sections/conclusion.tex:3 | p-value |  | cient work is not made incomplete but over-elaborated, the share rated Overdone rising from 4\% to 40\% ($p = 4.0 \times 10^{-5}$), a fall of $-0.38$  |
| `1.01` | sections/conclusion.tex:5 | p-value |  | int for all six. More turns do not help; naming the fault does. Told what to fix, a model produces revisions 1.01 levels higher than generic iteration |
| `1.9` | sections/conclusion.tex:5 | p-value |  | the fault does. Told what to fix, a model produces revisions 1.01 levels higher than generic iteration ($p = 1.9 \times 10^{-19}$). Systems should eva |
| `10` | sections/conclusion.tex:5 | p-value |  | does. Told what to fix, a model produces revisions 1.01 levels higher than generic iteration ($p = 1.9 \times 10^{-19}$). Systems should evaluate befo |
| `19` | sections/conclusion.tex:5 | p-value |  | Told what to fix, a model produces revisions 1.01 levels higher than generic iteration ($p = 1.9 \times 10^{-19}$). Systems should evaluate before rev |
| `3.3` | sections/introduction_v2.tex:21 | mean or delta | yes | icient to Incomplete across four identical requests. One trial of the quarterly sales summary task (Llama~3.3~70B, run~3). The prompt is excerpted; mo |
| `3` | sections/introduction_v2.tex:21 | mean or delta | yes | omplete across four identical requests. One trial of the quarterly sales summary task (Llama~3.3~70B, run~3). The prompt is excerpted; model output is |
| `283` | sections/introduction_v2.tex:25 | bare number | yes | series is the mean over every genuine revision at that index across all six models, whose $n$ falls from 283 to 96; the lighter series is this trial,  |
| `96` | sections/introduction_v2.tex:25 | bare number | yes | is the mean over every genuine revision at that index across all six models, whose $n$ falls from 283 to 96; the lighter series is this trial, its mar |
| `720` | sections/introduction_v2.tex:68 | bare number |  | f what to change. Counting the initial draft, each conversation runs five turns. The design spans six models, 720 conversations and 3,600 responses. W |
| `3,600` | sections/introduction_v2.tex:68 | bare number |  | ting the initial draft, each conversation runs five turns. The design spans six models, 720 conversations and 3,600 responses. We ask whether a model  |
| `88` | sections/introduction_v2.tex:73 | percentage |  | ns and validate every quality judgment against human raters. Most of the work being revised did not need it: 88\% of the 720 first drafts are already  |
| `720` | sections/introduction_v2.tex:73 | percentage |  | ate every quality judgment against human raters. Most of the work being revised did not need it: 88\% of the 720 first drafts are already sufficient.  |
| `86.7` | sections/introduction_v2.tex:75 | percentage |  | already sufficient. Asked to improve them without direction, models mostly do not revise: by the fifth turn, 86.7\% of replies are meta-responses, res |
| `69` | sections/introduction_v2.tex:76 | percentage |  | sponses, restatements and declines presented as compliance rather than new task content. When they do revise, 69\% of the changes that move quality mo |
| `50` | sections/introduction_v2.tex:77 | p-value |  | When they do revise, 69\% of the changes that move quality move it down, and the movement has a shape: on the 50 trials that revise at every turn, the |
| `4` | sections/introduction_v2.tex:77 | p-value |  | ment has a shape: on the 50 trials that revise at every turn, the share of over-elaborated outputs rises from 4\% to 40\% ($p = 4.0 \times 10^{-5}$) w |
| `40` | sections/introduction_v2.tex:77 | p-value |  | s a shape: on the 50 trials that revise at every turn, the share of over-elaborated outputs rises from 4\% to 40\% ($p = 4.0 \times 10^{-5}$) while th |
| `4.0` | sections/introduction_v2.tex:77 | p-value |  | on the 50 trials that revise at every turn, the share of over-elaborated outputs rises from 4\% to 40\% ($p = 4.0 \times 10^{-5}$) while the share fal |
| `10` | sections/introduction_v2.tex:77 | p-value |  | rials that revise at every turn, the share of over-elaborated outputs rises from 4\% to 40\% ($p = 4.0 \times 10^{-5}$) while the share falling below  |
| `5` | sections/introduction_v2.tex:77 | p-value |  | that revise at every turn, the share of over-elaborated outputs rises from 4\% to 40\% ($p = 4.0 \times 10^{-5}$) while the share falling below suffic |
| `0.38` | sections/introduction_v2.tex:77 | p-value |  | lling below sufficiency holds. Models add unrequested material rather than drop what was asked for, a fall of 0.38 ordinal levels ($p = 4.4 \times 10^ |
| `4.4` | sections/introduction_v2.tex:77 | p-value |  | lds. Models add unrequested material rather than drop what was asked for, a fall of 0.38 ordinal levels ($p = 4.4 \times 10^{-3}$). For all six models |
| `10` | sections/introduction_v2.tex:77 | p-value |  | add unrequested material rather than drop what was asked for, a fall of 0.38 ordinal levels ($p = 4.4 \times 10^{-3}$). For all six models the first d |
| `3` | sections/introduction_v2.tex:77 | p-value |  | unrequested material rather than drop what was asked for, a fall of 0.38 ordinal levels ($p = 4.4 \times 10^{-3}$). For all six models the first draft |
| `62.1` | sections/introduction_v2.tex:78 | percentage |  | ty-optimal stopping point, and we name the tokens spent past it the \textbf{revision tax}, which accounts for 62.1\% of all output generated. On outpu |
| `1.01` | sections/introduction_v2.tex:79 | p-value |  | of all output generated. On outputs rated insufficient, a single critique naming the fault lifts the revision 1.01 levels above undirected iteration ( |
| `1.9` | sections/introduction_v2.tex:80 | p-value |  | ufficient, a single critique naming the fault lifts the revision 1.01 levels above undirected iteration ($p = 1.9 \times 10^{-19}$). Blind readers sho |
| `10` | sections/introduction_v2.tex:80 | p-value |  | a single critique naming the fault lifts the revision 1.01 levels above undirected iteration ($p = 1.9 \times 10^{-19}$). Blind readers shown the firs |
| `19` | sections/introduction_v2.tex:80 | p-value |  | gle critique naming the fault lifts the revision 1.01 levels above undirected iteration ($p = 1.9 \times 10^{-19}$). Blind readers shown the first and |
| `56` | sections/introduction_v2.tex:81 | p-value |  | cted iteration ($p = 1.9 \times 10^{-19}$). Blind readers shown the first and last drafts prefer the first in 56\% of decisions, an interval that incl |
| `3.3` | sections/limitations.tex:3 | count or denominator |  | on*{Limitations} Several limitations qualify these findings. First, the balanced panel is dominated by Llama~3.3~70B ($n = 45$ of 50); other models ex |
| `45` | sections/limitations.tex:3 | count or denominator |  | s} Several limitations qualify these findings. First, the balanced panel is dominated by Llama~3.3~70B ($n = 45$ of 50); other models exit the revisio |
| `50` | sections/limitations.tex:3 | count or denominator |  | eral limitations qualify these findings. First, the balanced panel is dominated by Llama~3.3~70B ($n = 45$ of 50); other models exit the revision pool |
| `4` | sections/limitations.tex:3 | bare number |  | exit the revision pool too quickly for powered within-model comparison. Second, the evaluator (Claude Sonnet~4) judges outputs from all models includi |
| `0.505` | sections/limitations.tex:3 | reliability or effect size |  | mitigate this through six-model calibration selecting the highest human-correlation evaluator (Spearman $r = 0.505$, QW $\kappa = 0.526$). Third, inte |
| `0.526` | sections/limitations.tex:3 | reliability or effect size |  | h six-model calibration selecting the highest human-correlation evaluator (Spearman $r = 0.505$, QW $\kappa = 0.526$). Third, inter-rater reliability  |
| `0.48` | sections/limitations.tex:3 | reliability or effect size |  | $r = 0.505$, QW $\kappa = 0.526$). Third, inter-rater reliability is moderate (quadratic-weighted $\kappa$ = 0.48--0.61 across three rater pairs; Krip |
| `0.61` | sections/limitations.tex:3 | reliability or effect size |  | 0.505$, QW $\kappa = 0.526$). Third, inter-rater reliability is moderate (quadratic-weighted $\kappa$ = 0.48--0.61 across three rater pairs; Krippendo |
| `0.540` | sections/limitations.tex:3 | reliability or effect size |  | lity is moderate (quadratic-weighted $\kappa$ = 0.48--0.61 across three rater pairs; Krippendorff's $\alpha = 0.540$, $n = 64$). Fourth, all trials us |
| `64` | sections/limitations.tex:3 | reliability or effect size |  | ate (quadratic-weighted $\kappa$ = 0.48--0.61 across three rater pairs; Krippendorff's $\alpha = 0.540$, $n = 64$). Fourth, all trials used temperatur |
| `1.0` | sections/limitations.tex:3 | reliability or effect size |  | .61 across three rater pairs; Krippendorff's $\alpha = 0.540$, $n = 64$). Fourth, all trials used temperature~1.0; revision behavior at lower temperat |
| `40` | sections/limitations.tex:3 | mean or delta |  | 64$). Fourth, all trials used temperature~1.0; revision behavior at lower temperatures may differ. Fifth, our 40 tasks represent a convenience sample  |
| `5` | sections/limitations.tex:3 | bare number |  | ovide a stronger baseline. Seventh, our per-domain quality estimates come from small per-domain samples: Turn-5 genuine-revision cells range from 13 t |
| `13` | sections/limitations.tex:3 | bare number |  | our per-domain quality estimates come from small per-domain samples: Turn-5 genuine-revision cells range from 13 to 30 trials, and only the code domai |
| `30` | sections/limitations.tex:3 | bare number |  | r-domain quality estimates come from small per-domain samples: Turn-5 genuine-revision cells range from 13 to 30 trials, and only the code domain clea |
| `8` | sections/methods.tex:20 | bare number | yes | begin{tabular}{@{}lrl@{}} \toprule \textbf{Domain} & \textbf{$n$} & \textbf{Example tasks} \\ \midrule Code & 8 & Debounce function, email validator \ |
| `8` | sections/methods.tex:21 | bare number | yes | extbf{$n$} & \textbf{Example tasks} \\ \midrule Code & 8 & Debounce function, email validator \\ Data logic & 8 & Discount stacking, scheduling \\ Ana |
| `8` | sections/methods.tex:22 | bare number | yes | Code & 8 & Debounce function, email validator \\ Data logic & 8 & Discount stacking, scheduling \\ Analysis & 8 & Quarterly sales summary, policy memo |
| `8` | sections/methods.tex:23 | bare number | yes | logic & 8 & Discount stacking, scheduling \\ Analysis & 8 & Quarterly sales summary, policy memo \\ Writing & 8 & PTO request, LinkedIn announcement \ |
| `8` | sections/methods.tex:24 | bare number | yes | & 8 & Quarterly sales summary, policy memo \\ Writing & 8 & PTO request, LinkedIn announcement \\ Creative & 8 & Story opening, tone rewrite \\ \botto |
| `8` | sections/methods.tex:27 | bare number | yes | ve & 8 & Story opening, tone rewrite \\ \bottomrule \end{tabular} \caption{Task domains. Each domain contains 8 scenarios spanning typical enterprise  |
| `2` | sections/methods.tex:34 | bare number |  | domains} \end{table} \subsection{Response Classification} \label{sec:methods-classifier} At each turn $\geq 2$, the model's response is classified as  |
| `1.4` | sections/methods.tex:34 | percentage |  | the classifier had read as new content because the model reproduced its earlier answer alongside the refusal (1.4\% of genuine labels). The classifier |
| `1` | sections/methods.tex:47 | bare number |  | nctional''), whose definition is that all components are present with clear weaknesses, producing a monotonic 1--5 scale. Results that are counts rath |
| `5` | sections/methods.tex:47 | bare number |  | ional''), whose definition is that all components are present with clear weaknesses, producing a monotonic 1--5 scale. Results that are counts rather  |
| `64` | sections/methods.tex:50 | p-value |  | which. \paragraph{Evaluator Calibration.} Six candidate evaluators were scored against three human raters on 64 stratified samples; Claude Sonnet~4 ha |
| `50` | sections/methods.tex:60 | percentage |  | (``Let me know if you'd like any changes'') to revision outputs. In a model- and domain-stratified sample of 50 trials with at least one genuine revis |
| `3,600` | sections/methods.tex:62 | bare number |  | rdone'' criterion on boilerplate rather than content. To control for this, we strip meta-commentary from all 3,600 outputs using validated regex patte |
| `3,600` | sections/methods.tex:62 | percentage |  | from all 3,600 outputs using validated regex patterns matching common preamble and postamble phrases. Of the 3,600 outputs, 1,200 (33.3\%) were modifi |
| `1,200` | sections/methods.tex:62 | percentage |  | outputs using validated regex patterns matching common preamble and postamble phrases. Of the 3,600 outputs, 1,200 (33.3\%) were modified by stripping |
| `33.3` | sections/methods.tex:62 | percentage |  | s using validated regex patterns matching common preamble and postamble phrases. Of the 3,600 outputs, 1,200 (33.3\%) were modified by stripping and r |
| `4` | sections/methods.tex:62 | percentage |  | tamble phrases. Of the 3,600 outputs, 1,200 (33.3\%) were modified by stripping and rescored by Claude Sonnet~4 at temperature~0 using the identical e |
| `0` | sections/methods.tex:62 | percentage |  | f the 3,600 outputs, 1,200 (33.3\%) were modified by stripping and rescored by Claude Sonnet~4 at temperature~0 using the identical evaluation prompt. |
| `50` | sections/methods.tex:62 | reliability or effect size |  | rescored by Claude Sonnet~4 at temperature~0 using the identical evaluation prompt. Validation: on those same 50 pairs, two human annotators rating st |
| `0.569` | sections/methods.tex:62 | reliability or effect size |  | : on those same 50 pairs, two human annotators rating stripped content agreed with the evaluator at $\kappa = 0.569$, compared to near-chance agreemen |
| `6` | sections/methods.tex:7 | bare number |  | estimate of behaviour under the revision-implying prompts that dominate in practice. The experiment crosses 6 models $\times$ 40 scenarios $\times$ 3  |
| `40` | sections/methods.tex:7 | bare number |  | iour under the revision-implying prompts that dominate in practice. The experiment crosses 6 models $\times$ 40 scenarios $\times$ 3 runs $=$ \textbf{ |
| `3` | sections/methods.tex:7 | mean or delta |  | n-implying prompts that dominate in practice. The experiment crosses 6 models $\times$ 40 scenarios $\times$ 3 runs $=$ \textbf{720 trials} (3,600 mod |
| `720` | sections/methods.tex:7 | mean or delta |  | that dominate in practice. The experiment crosses 6 models $\times$ 40 scenarios $\times$ 3 runs $=$ \textbf{720 trials} (3,600 model-turn observation |
| `3,600` | sections/methods.tex:7 | mean or delta |  | in practice. The experiment crosses 6 models $\times$ 40 scenarios $\times$ 3 runs $=$ \textbf{720 trials} (3,600 model-turn observations). All genera |
| `1.0` | sections/methods.tex:7 | mean or delta |  | rios $\times$ 3 runs $=$ \textbf{720 trials} (3,600 model-turn observations). All generation uses temperature~1.0, to maximize output diversity and av |
| `177` | sections/methods.tex:78 | count or denominator |  | ch is then blind-evaluated. This tests whether specific feedback outperforms the generic revision probe ($n = 177$ paired comparisons after filtering  |
| `71.9` | sections/results_v2.tex:102 | count or denominator |  | ld constant, model identity explains far more variation in genuine-revision rate than task domain: a range of 71.9 percentage points against 13.5. All |
| `13.5` | sections/results_v2.tex:102 | reliability or effect size |  | lains far more variation in genuine-revision rate than task domain: a range of 71.9 percentage points against 13.5. All five domains show negative str |
| `631` | sections/results_v2.tex:108 | percentage |  | ). \paragraph{Revision despite sufficiency.} The evaluator rated 87.6\% of first-turn outputs as sufficient (631/720), so most trials begin with work  |
| `720` | sections/results_v2.tex:108 | percentage |  | \paragraph{Revision despite sufficiency.} The evaluator rated 87.6\% of first-turn outputs as sufficient (631/720), so most trials begin with work tha |
| `0.38` | sections/results_v2.tex:130 | count or denominator |  | irst draft. This bounds what the degradation means in practice without touching what it measures. The drop of 0.38 levels is not large enough to rever |
| `4.71` | sections/results_v2.tex:138 | p-value |  | written critique and produced what we call a targeted revision. On stripped content, targeted revisions score 4.71 against 3.70 for the model's own ge |
| `3.70` | sections/results_v2.tex:138 | p-value |  | que and produced what we call a targeted revision. On stripped content, targeted revisions score 4.71 against 3.70 for the model's own generic next-tu |
| `1.01` | sections/results_v2.tex:138 | p-value |  | content, targeted revisions score 4.71 against 3.70 for the model's own generic next-turn revision, a gain of 1.01 levels ($p = 1.9 \times 10^{-19}$,  |
| `1.9` | sections/results_v2.tex:138 | p-value |  | revisions score 4.71 against 3.70 for the model's own generic next-turn revision, a gain of 1.01 levels ($p = 1.9 \times 10^{-19}$, $n = 177$; unstrip |
| `10` | sections/results_v2.tex:138 | p-value |  | core 4.71 against 3.70 for the model's own generic next-turn revision, a gain of 1.01 levels ($p = 1.9 \times 10^{-19}$, $n = 177$; unstripped: 4.71 a |
| `19` | sections/results_v2.tex:138 | p-value |  | 4.71 against 3.70 for the model's own generic next-turn revision, a gain of 1.01 levels ($p = 1.9 \times 10^{-19}$, $n = 177$; unstripped: 4.71 agains |
| `177` | sections/results_v2.tex:138 | p-value |  | t 3.70 for the model's own generic next-turn revision, a gain of 1.01 levels ($p = 1.9 \times 10^{-19}$, $n = 177$; unstripped: 4.71 against 4.51, $+0 |
| `4.71` | sections/results_v2.tex:138 | p-value |  | el's own generic next-turn revision, a gain of 1.01 levels ($p = 1.9 \times 10^{-19}$, $n = 177$; unstripped: 4.71 against 4.51, $+0.20$, $p = 6.6 \ti |
| `4.51` | sections/results_v2.tex:138 | p-value |  | ric next-turn revision, a gain of 1.01 levels ($p = 1.9 \times 10^{-19}$, $n = 177$; unstripped: 4.71 against 4.51, $+0.20$, $p = 6.6 \times 10^{-3}$) |
| `0.20` | sections/results_v2.tex:138 | p-value |  | -turn revision, a gain of 1.01 levels ($p = 1.9 \times 10^{-19}$, $n = 177$; unstripped: 4.71 against 4.51, $+0.20$, $p = 6.6 \times 10^{-3}$). The un |
| `6.6` | sections/results_v2.tex:138 | p-value |  | on, a gain of 1.01 levels ($p = 1.9 \times 10^{-19}$, $n = 177$; unstripped: 4.71 against 4.51, $+0.20$, $p = 6.6 \times 10^{-3}$). The unstripped com |
| `10` | sections/results_v2.tex:138 | p-value |  | of 1.01 levels ($p = 1.9 \times 10^{-19}$, $n = 177$; unstripped: 4.71 against 4.51, $+0.20$, $p = 6.6 \times 10^{-3}$). The unstripped comparison und |
| `3` | sections/results_v2.tex:138 | p-value |  | 01 levels ($p = 1.9 \times 10^{-19}$, $n = 177$; unstripped: 4.71 against 4.51, $+0.20$, $p = 6.6 \times 10^{-3}$). The unstripped comparison understa |
| `3.3` | sections/results_v2.tex:148 | p-value | yes | ll \begin{tabular}{lccc} \toprule Model & $n$ & Stripped $\Delta$ & $p$ \\ \midrule Llama 3.3 70B & 71 & $+1.56$ & $6.5 \times 10^{-12}$ \\ Qwen 3 235 |
| `71` | sections/results_v2.tex:148 | p-value | yes | gin{tabular}{lccc} \toprule Model & $n$ & Stripped $\Delta$ & $p$ \\ \midrule Llama 3.3 70B & 71 & $+1.56$ & $6.5 \times 10^{-12}$ \\ Qwen 3 235B & 21 |
| `1.56` | sections/results_v2.tex:148 | p-value | yes | ular}{lccc} \toprule Model & $n$ & Stripped $\Delta$ & $p$ \\ \midrule Llama 3.3 70B & 71 & $+1.56$ & $6.5 \times 10^{-12}$ \\ Qwen 3 235B & 21 & $+1. |
| `6.5` | sections/results_v2.tex:148 | p-value | yes | c} \toprule Model & $n$ & Stripped $\Delta$ & $p$ \\ \midrule Llama 3.3 70B & 71 & $+1.56$ & $6.5 \times 10^{-12}$ \\ Qwen 3 235B & 21 & $+1.10$ & $4. |
| `10` | sections/results_v2.tex:148 | p-value | yes | rule Model & $n$ & Stripped $\Delta$ & $p$ \\ \midrule Llama 3.3 70B & 71 & $+1.56$ & $6.5 \times 10^{-12}$ \\ Qwen 3 235B & 21 & $+1.10$ & $4.5 \time |
| `12` | sections/results_v2.tex:148 | p-value | yes | Model & $n$ & Stripped $\Delta$ & $p$ \\ \midrule Llama 3.3 70B & 71 & $+1.56$ & $6.5 \times 10^{-12}$ \\ Qwen 3 235B & 21 & $+1.10$ & $4.5 \times 10^ |
| `3` | sections/results_v2.tex:149 | p-value | yes | Stripped $\Delta$ & $p$ \\ \midrule Llama 3.3 70B & 71 & $+1.56$ & $6.5 \times 10^{-12}$ \\ Qwen 3 235B & 21 & $+1.10$ & $4.5 \times 10^{-4}$ \\ GPT-4 |
| `21` | sections/results_v2.tex:149 | p-value | yes | $\Delta$ & $p$ \\ \midrule Llama 3.3 70B & 71 & $+1.56$ & $6.5 \times 10^{-12}$ \\ Qwen 3 235B & 21 & $+1.10$ & $4.5 \times 10^{-4}$ \\ GPT-4o & 12 &  |
| `1.10` | sections/results_v2.tex:149 | p-value | yes | a$ & $p$ \\ \midrule Llama 3.3 70B & 71 & $+1.56$ & $6.5 \times 10^{-12}$ \\ Qwen 3 235B & 21 & $+1.10$ & $4.5 \times 10^{-4}$ \\ GPT-4o & 12 & $+1.00 |
| `4.5` | sections/results_v2.tex:149 | p-value | yes | \\ \midrule Llama 3.3 70B & 71 & $+1.56$ & $6.5 \times 10^{-12}$ \\ Qwen 3 235B & 21 & $+1.10$ & $4.5 \times 10^{-4}$ \\ GPT-4o & 12 & $+1.00$ & $8.8  |
| `10` | sections/results_v2.tex:149 | p-value | yes | rule Llama 3.3 70B & 71 & $+1.56$ & $6.5 \times 10^{-12}$ \\ Qwen 3 235B & 21 & $+1.10$ & $4.5 \times 10^{-4}$ \\ GPT-4o & 12 & $+1.00$ & $8.8 \times  |
| `4` | sections/results_v2.tex:149 | p-value | yes | Llama 3.3 70B & 71 & $+1.56$ & $6.5 \times 10^{-12}$ \\ Qwen 3 235B & 21 & $+1.10$ & $4.5 \times 10^{-4}$ \\ GPT-4o & 12 & $+1.00$ & $8.8 \times 10^{- |
| `12` | sections/results_v2.tex:150 | p-value | yes | 71 & $+1.56$ & $6.5 \times 10^{-12}$ \\ Qwen 3 235B & 21 & $+1.10$ & $4.5 \times 10^{-4}$ \\ GPT-4o & 12 & $+1.00$ & $8.8 \times 10^{-3}$ \\ DeepSeek  |
| `1.00` | sections/results_v2.tex:150 | p-value | yes | 1.56$ & $6.5 \times 10^{-12}$ \\ Qwen 3 235B & 21 & $+1.10$ & $4.5 \times 10^{-4}$ \\ GPT-4o & 12 & $+1.00$ & $8.8 \times 10^{-3}$ \\ DeepSeek V4 Flas |
| `8.8` | sections/results_v2.tex:150 | p-value | yes | 6.5 \times 10^{-12}$ \\ Qwen 3 235B & 21 & $+1.10$ & $4.5 \times 10^{-4}$ \\ GPT-4o & 12 & $+1.00$ & $8.8 \times 10^{-3}$ \\ DeepSeek V4 Flash & 19 &  |
| `10` | sections/results_v2.tex:150 | p-value | yes | 10^{-12}$ \\ Qwen 3 235B & 21 & $+1.10$ & $4.5 \times 10^{-4}$ \\ GPT-4o & 12 & $+1.00$ & $8.8 \times 10^{-3}$ \\ DeepSeek V4 Flash & 19 & $+0.74$ & $ |
| `3` | sections/results_v2.tex:150 | p-value | yes | 12}$ \\ Qwen 3 235B & 21 & $+1.10$ & $4.5 \times 10^{-4}$ \\ GPT-4o & 12 & $+1.00$ & $8.8 \times 10^{-3}$ \\ DeepSeek V4 Flash & 19 & $+0.74$ & $2.0 \ |
| `19` | sections/results_v2.tex:151 | p-value | yes | $+1.10$ & $4.5 \times 10^{-4}$ \\ GPT-4o & 12 & $+1.00$ & $8.8 \times 10^{-3}$ \\ DeepSeek V4 Flash & 19 & $+0.74$ & $2.0 \times 10^{-2}$ \\ Claude So |
| `0.74` | sections/results_v2.tex:151 | p-value | yes | & $4.5 \times 10^{-4}$ \\ GPT-4o & 12 & $+1.00$ & $8.8 \times 10^{-3}$ \\ DeepSeek V4 Flash & 19 & $+0.74$ & $2.0 \times 10^{-2}$ \\ Claude Sonnet 4 & |
| `2.0` | sections/results_v2.tex:151 | p-value | yes | times 10^{-4}$ \\ GPT-4o & 12 & $+1.00$ & $8.8 \times 10^{-3}$ \\ DeepSeek V4 Flash & 19 & $+0.74$ & $2.0 \times 10^{-2}$ \\ Claude Sonnet 4 & 51 & $+ |
| `10` | sections/results_v2.tex:151 | p-value | yes | 4}$ \\ GPT-4o & 12 & $+1.00$ & $8.8 \times 10^{-3}$ \\ DeepSeek V4 Flash & 19 & $+0.74$ & $2.0 \times 10^{-2}$ \\ Claude Sonnet 4 & 51 & $+0.25$ & $4. |
| `2` | sections/results_v2.tex:151 | p-value | yes | \ GPT-4o & 12 & $+1.00$ & $8.8 \times 10^{-3}$ \\ DeepSeek V4 Flash & 19 & $+0.74$ & $2.0 \times 10^{-2}$ \\ Claude Sonnet 4 & 51 & $+0.25$ & $4.7 \ti |
| `4` | sections/results_v2.tex:152 | p-value | yes | 0$ & $8.8 \times 10^{-3}$ \\ DeepSeek V4 Flash & 19 & $+0.74$ & $2.0 \times 10^{-2}$ \\ Claude Sonnet 4 & 51 & $+0.25$ & $4.7 \times 10^{-3}$ \\ Gemin |
| `51` | sections/results_v2.tex:152 | p-value | yes | $8.8 \times 10^{-3}$ \\ DeepSeek V4 Flash & 19 & $+0.74$ & $2.0 \times 10^{-2}$ \\ Claude Sonnet 4 & 51 & $+0.25$ & $4.7 \times 10^{-3}$ \\ Gemini 2.5 |
| `0.25` | sections/results_v2.tex:152 | p-value | yes | times 10^{-3}$ \\ DeepSeek V4 Flash & 19 & $+0.74$ & $2.0 \times 10^{-2}$ \\ Claude Sonnet 4 & 51 & $+0.25$ & $4.7 \times 10^{-3}$ \\ Gemini 2.5 Flash |
| `4.7` | sections/results_v2.tex:152 | p-value | yes | {-3}$ \\ DeepSeek V4 Flash & 19 & $+0.74$ & $2.0 \times 10^{-2}$ \\ Claude Sonnet 4 & 51 & $+0.25$ & $4.7 \times 10^{-3}$ \\ Gemini 2.5 Flash & 3 & $+ |
| `10` | sections/results_v2.tex:152 | p-value | yes | DeepSeek V4 Flash & 19 & $+0.74$ & $2.0 \times 10^{-2}$ \\ Claude Sonnet 4 & 51 & $+0.25$ & $4.7 \times 10^{-3}$ \\ Gemini 2.5 Flash & 3 & $+1.67$ & - |
| `3` | sections/results_v2.tex:152 | p-value | yes | pSeek V4 Flash & 19 & $+0.74$ & $2.0 \times 10^{-2}$ \\ Claude Sonnet 4 & 51 & $+0.25$ & $4.7 \times 10^{-3}$ \\ Gemini 2.5 Flash & 3 & $+1.67$ & -- ( |
| `2.5` | sections/results_v2.tex:153 | p-value | yes | 9 & $+0.74$ & $2.0 \times 10^{-2}$ \\ Claude Sonnet 4 & 51 & $+0.25$ & $4.7 \times 10^{-3}$ \\ Gemini 2.5 Flash & 3 & $+1.67$ & -- ($n < 5$) \\ \botto |
| `3` | sections/results_v2.tex:153 | p-value | yes | & $2.0 \times 10^{-2}$ \\ Claude Sonnet 4 & 51 & $+0.25$ & $4.7 \times 10^{-3}$ \\ Gemini 2.5 Flash & 3 & $+1.67$ & -- ($n < 5$) \\ \bottomrule \end{t |
| `1.67` | sections/results_v2.tex:153 | p-value | yes | \times 10^{-2}$ \\ Claude Sonnet 4 & 51 & $+0.25$ & $4.7 \times 10^{-3}$ \\ Gemini 2.5 Flash & 3 & $+1.67$ & -- ($n < 5$) \\ \bottomrule \end{tabular} |
| `5` | sections/results_v2.tex:153 | p-value | yes | \\ Claude Sonnet 4 & 51 & $+0.25$ & $4.7 \times 10^{-3}$ \\ Gemini 2.5 Flash & 3 & $+1.67$ & -- ($n < 5$) \\ \bottomrule \end{tabular} \caption{Target |
| `0.38` | sections/results_v2.tex:160 | mean or delta |  | dels show significant improvement.} \label{tab:targeted-per-model} \end{table} Undirected revision costs 0.38 levels across the balanced panel, 33 of  |
| `33` | sections/results_v2.tex:160 | mean or delta |  | \label{tab:targeted-per-model} \end{table} Undirected revision costs 0.38 levels across the balanced panel, 33 of whose 50 trials begin above the suff |
| `50` | sections/results_v2.tex:160 | mean or delta |  | targeted-per-model} \end{table} Undirected revision costs 0.38 levels across the balanced panel, 33 of whose 50 trials begin above the sufficiency thr |
| `1.01` | sections/results_v2.tex:160 | mean or delta |  | l, 33 of whose 50 trials begin above the sufficiency threshold. A critique naming the fault raises quality by 1.01 levels on work rated below it. \Flo |
| `1.6` | sections/results_v2.tex:173 | percentage |  | only the tokens needed to reach $t^*$, the waste is 164.2\%, so continuing past peak quality produces roughly 1.6 times more text than reaching the op |
| `23.4` | sections/results_v2.tex:173 | percentage |  | peak quality produces roughly 1.6 times more text than reaching the optimum took. Per-model waste ranges from 23.4\% (Gemini, which declines early and |
| `81.3` | sections/results_v2.tex:173 | percentage |  | m took. Per-model waste ranges from 23.4\% (Gemini, which declines early and generates few post-T1 tokens) to 81.3\% (Llama, which continues revising  |
| `2.5` | sections/results_v2.tex:189 | percentage | yes | \centering \small \begin{tabular}{@{}lr@{}} \toprule Model & Sufficient output left alone \\ \midrule Gemini 2.5 Flash & 97.8\% \\ DeepSeek V4 Flash & |
| `97.8` | sections/results_v2.tex:189 | percentage | yes | \small \begin{tabular}{@{}lr@{}} \toprule Model & Sufficient output left alone \\ \midrule Gemini 2.5 Flash & 97.8\% \\ DeepSeek V4 Flash & 96.3\% \\  |
| `96.3` | sections/results_v2.tex:190 | percentage | yes | }} \toprule Model & Sufficient output left alone \\ \midrule Gemini 2.5 Flash & 97.8\% \\ DeepSeek V4 Flash & 96.3\% \\ GPT-4o & 82.3\% \\ Qwen 3 235B |
| `82.3` | sections/results_v2.tex:191 | percentage | yes | Sufficient output left alone \\ \midrule Gemini 2.5 Flash & 97.8\% \\ DeepSeek V4 Flash & 96.3\% \\ GPT-4o & 82.3\% \\ Qwen 3 235B & 68.4\% \\ Claude  |
| `3` | sections/results_v2.tex:192 | percentage | yes | put left alone \\ \midrule Gemini 2.5 Flash & 97.8\% \\ DeepSeek V4 Flash & 96.3\% \\ GPT-4o & 82.3\% \\ Qwen 3 235B & 68.4\% \\ Claude Sonnet 4 & 54. |
| `68.4` | sections/results_v2.tex:192 | percentage | yes | alone \\ \midrule Gemini 2.5 Flash & 97.8\% \\ DeepSeek V4 Flash & 96.3\% \\ GPT-4o & 82.3\% \\ Qwen 3 235B & 68.4\% \\ Claude Sonnet 4 & 54.1\% \\ Ll |
| `4` | sections/results_v2.tex:193 | percentage | yes | 2.5 Flash & 97.8\% \\ DeepSeek V4 Flash & 96.3\% \\ GPT-4o & 82.3\% \\ Qwen 3 235B & 68.4\% \\ Claude Sonnet 4 & 54.1\% \\ Llama 3.3 70B & 18.4\% \\ \ |
| `54.1` | sections/results_v2.tex:193 | percentage | yes | Flash & 97.8\% \\ DeepSeek V4 Flash & 96.3\% \\ GPT-4o & 82.3\% \\ Qwen 3 235B & 68.4\% \\ Claude Sonnet 4 & 54.1\% \\ Llama 3.3 70B & 18.4\% \\ \bott |
| `3.3` | sections/results_v2.tex:194 | percentage | yes | \\ DeepSeek V4 Flash & 96.3\% \\ GPT-4o & 82.3\% \\ Qwen 3 235B & 68.4\% \\ Claude Sonnet 4 & 54.1\% \\ Llama 3.3 70B & 18.4\% \\ \bottomrule \end{tab |
| `18.4` | sections/results_v2.tex:194 | percentage | yes | k V4 Flash & 96.3\% \\ GPT-4o & 82.3\% \\ Qwen 3 235B & 68.4\% \\ Claude Sonnet 4 & 54.1\% \\ Llama 3.3 70B & 18.4\% \\ \bottomrule \end{tabular} \cap |
| `36` | sections/results_v2.tex:198 | bare number | yes | lar} \caption{Share of turns rated sufficient whose next turn is not a genuine revision, stripped basis, over 36 of the 40 tasks; four Gemini cells co |
| `40` | sections/results_v2.tex:198 | bare number | yes | ion{Share of turns rated sufficient whose next turn is not a genuine revision, stripped basis, over 36 of the 40 tasks; four Gemini cells contain no s |
| `1,000` | sections/results_v2.tex:203 | reliability or effect size |  | no denominator.} \label{tab:stet} \end{table} Whether forty tasks rank six models stably is testable. Across 1,000 random splits of the tasks into hal |
| `0.972` | sections/results_v2.tex:203 | reliability or effect size |  | y is testable. Across 1,000 random splits of the tasks into halves, the halves agree at mean Spearman $\rho = 0.972$, every split clears $0.80$, and L |
| `0.80` | sections/results_v2.tex:204 | reliability or effect size |  | random splits of the tasks into halves, the halves agree at mean Spearman $\rho = 0.972$, every split clears $0.80$, and Llama is last in all of them. |
| `0.992` | sections/results_v2.tex:204 | mean or delta |  | 72$, every split clears $0.80$, and Llama is last in all of them. A generalizability decomposition gives $G = 0.992$ over the 36 tasks that carry a de |
| `36` | sections/results_v2.tex:204 | mean or delta |  | clears $0.80$, and Llama is last in all of them. A generalizability decomposition gives $G = 0.992$ over the 36 tasks that carry a denominator, where  |
| `0.95` | sections/results_v2.tex:204 | mean or delta |  | lizability decomposition gives $G = 0.992$ over the 36 tasks that carry a denominator, where six would reach $0.95$, because variance between models i |
| `3.2` | sections/results_v2.tex:204 | mean or delta |  | over the 36 tasks that carry a denominator, where six would reach $0.95$, because variance between models is 3.2 times the model-by-task residual. Gen |
| `1.000` | sections/results_v2.tex:205 | mean or delta |  | the model-by-task residual. Genuine-revision rate and the revision tax order the models identically ($\rho = 1.000$), so we report one of the three. T |
| `283` | sections/results_v2.tex:26 | percentage | yes | \small \begin{tabular}{lcc} \toprule Turn & Genuine revisions & Rate \\ \midrule T2 & 283/720 & 39.3\% \\ T3 & 185/720 & 25.7\% \\ T4 & 154/720 & 21.4 |
| `720` | sections/results_v2.tex:26 | percentage | yes | \small \begin{tabular}{lcc} \toprule Turn & Genuine revisions & Rate \\ \midrule T2 & 283/720 & 39.3\% \\ T3 & 185/720 & 25.7\% \\ T4 & 154/720 & 21.4 |
| `39.3` | sections/results_v2.tex:26 | percentage | yes | \begin{tabular}{lcc} \toprule Turn & Genuine revisions & Rate \\ \midrule T2 & 283/720 & 39.3\% \\ T3 & 185/720 & 25.7\% \\ T4 & 154/720 & 21.4\% \\ T |
| `185` | sections/results_v2.tex:27 | percentage | yes | }{lcc} \toprule Turn & Genuine revisions & Rate \\ \midrule T2 & 283/720 & 39.3\% \\ T3 & 185/720 & 25.7\% \\ T4 & 154/720 & 21.4\% \\ T5 & 96/720 & 1 |
| `720` | sections/results_v2.tex:27 | percentage | yes | c} \toprule Turn & Genuine revisions & Rate \\ \midrule T2 & 283/720 & 39.3\% \\ T3 & 185/720 & 25.7\% \\ T4 & 154/720 & 21.4\% \\ T5 & 96/720 & 13.3\ |
| `25.7` | sections/results_v2.tex:27 | percentage | yes | \toprule Turn & Genuine revisions & Rate \\ \midrule T2 & 283/720 & 39.3\% \\ T3 & 185/720 & 25.7\% \\ T4 & 154/720 & 21.4\% \\ T5 & 96/720 & 13.3\% \ |
| `154` | sections/results_v2.tex:28 | percentage | yes | & Genuine revisions & Rate \\ \midrule T2 & 283/720 & 39.3\% \\ T3 & 185/720 & 25.7\% \\ T4 & 154/720 & 21.4\% \\ T5 & 96/720 & 13.3\% \\ \bottomrule  |
| `720` | sections/results_v2.tex:28 | percentage | yes | nuine revisions & Rate \\ \midrule T2 & 283/720 & 39.3\% \\ T3 & 185/720 & 25.7\% \\ T4 & 154/720 & 21.4\% \\ T5 & 96/720 & 13.3\% \\ \bottomrule \end |
| `21.4` | sections/results_v2.tex:28 | percentage | yes | revisions & Rate \\ \midrule T2 & 283/720 & 39.3\% \\ T3 & 185/720 & 25.7\% \\ T4 & 154/720 & 21.4\% \\ T5 & 96/720 & 13.3\% \\ \bottomrule \end{tabul |
| `96` | sections/results_v2.tex:29 | percentage | yes | \midrule T2 & 283/720 & 39.3\% \\ T3 & 185/720 & 25.7\% \\ T4 & 154/720 & 21.4\% \\ T5 & 96/720 & 13.3\% \\ \bottomrule \end{tabular} \caption{Genuine |
| `720` | sections/results_v2.tex:29 | percentage | yes | \midrule T2 & 283/720 & 39.3\% \\ T3 & 185/720 & 25.7\% \\ T4 & 154/720 & 21.4\% \\ T5 & 96/720 & 13.3\% \\ \bottomrule \end{tabular} \caption{Genuine |
| `13.3` | sections/results_v2.tex:29 | percentage | yes | rule T2 & 283/720 & 39.3\% \\ T3 & 185/720 & 25.7\% \\ T4 & 154/720 & 21.4\% \\ T5 & 96/720 & 13.3\% \\ \bottomrule \end{tabular} \caption{Genuine rev |
| `50` | sections/results_v2.tex:37 | percentage |  | s} shows the per-model survival curves; only Llama sustains revision to the final turn. The balanced panel of 50 trials with genuine revision at all t |
| `45` | sections/results_v2.tex:37 | percentage |  | revision to the final turn. The balanced panel of 50 trials with genuine revision at all turns is composed of 45 Llama trials (90\%), 3 Qwen, and 2 Cl |
| `90` | sections/results_v2.tex:37 | percentage |  | inal turn. The balanced panel of 50 trials with genuine revision at all turns is composed of 45 Llama trials (90\%), 3 Qwen, and 2 Claude; GPT-4o, Dee |
| `3` | sections/results_v2.tex:37 | percentage |  | rn. The balanced panel of 50 trials with genuine revision at all turns is composed of 45 Llama trials (90\%), 3 Qwen, and 2 Claude; GPT-4o, DeepSeek,  |
| `2` | sections/results_v2.tex:37 | percentage |  | nced panel of 50 trials with genuine revision at all turns is composed of 45 Llama trials (90\%), 3 Qwen, and 2 Claude; GPT-4o, DeepSeek, and Gemini c |
| `718` | sections/results_v2.tex:55 | percentage |  | Under Undirected Revision} \paragraph{Revisions lower quality more often than they raise it.} Across all 718 genuine revisions, a revision leaves the  |
| `62.7` | sections/results_v2.tex:55 | percentage |  | often than they raise it.} Across all 718 genuine revisions, a revision leaves the quality level unchanged in 62.7\% of cases, lowers it in 25.6\%, an |
| `25.6` | sections/results_v2.tex:56 | percentage |  | oss all 718 genuine revisions, a revision leaves the quality level unchanged in 62.7\% of cases, lowers it in 25.6\%, and raises it in 11.7\%. Restric |
| `11.7` | sections/results_v2.tex:56 | percentage |  | ions, a revision leaves the quality level unchanged in 62.7\% of cases, lowers it in 25.6\%, and raises it in 11.7\%. Restricting to the 268 revisions |
| `268` | sections/results_v2.tex:56 | percentage |  | quality level unchanged in 62.7\% of cases, lowers it in 25.6\%, and raises it in 11.7\%. Restricting to the 268 revisions that move the level at all, |
| `184` | sections/results_v2.tex:57 | p-value |  | s, lowers it in 25.6\%, and raises it in 11.7\%. Restricting to the 268 revisions that move the level at all, 184 move it down and 84 move it up, a sh |
| `84` | sections/results_v2.tex:57 | p-value |  | %, and raises it in 11.7\%. Restricting to the 268 revisions that move the level at all, 184 move it down and 84 move it up, a share of 68.7\% (exact  |
| `68.7` | sections/results_v2.tex:57 | p-value |  | . Restricting to the 268 revisions that move the level at all, 184 move it down and 84 move it up, a share of 68.7\% (exact binomial 95\% CI $[62.8\%, |
| `95` | sections/results_v2.tex:58 | p-value |  | 8 revisions that move the level at all, 184 move it down and 84 move it up, a share of 68.7\% (exact binomial 95\% CI $[62.8\%, 74.1\%]$; sign test $p |
| `62.8` | sections/results_v2.tex:58 | p-value |  | s that move the level at all, 184 move it down and 84 move it up, a share of 68.7\% (exact binomial 95\% CI $[62.8\%, 74.1\%]$; sign test $p = 1.13 \t |
| `74.1` | sections/results_v2.tex:58 | p-value |  | ove the level at all, 184 move it down and 84 move it up, a share of 68.7\% (exact binomial 95\% CI $[62.8\%, 74.1\%]$; sign test $p = 1.13 \times 10^ |
| `1.13` | sections/results_v2.tex:58 | p-value |  | move it down and 84 move it up, a share of 68.7\% (exact binomial 95\% CI $[62.8\%, 74.1\%]$; sign test $p = 1.13 \times 10^{-9}$). Of the 524 revisio |
| `10` | sections/results_v2.tex:58 | p-value |  | n and 84 move it up, a share of 68.7\% (exact binomial 95\% CI $[62.8\%, 74.1\%]$; sign test $p = 1.13 \times 10^{-9}$). Of the 524 revisions whose in |
| `9` | sections/results_v2.tex:58 | p-value |  | 84 move it up, a share of 68.7\% (exact binomial 95\% CI $[62.8\%, 74.1\%]$; sign test $p = 1.13 \times 10^{-9}$). Of the 524 revisions whose input wa |
| `524` | sections/results_v2.tex:58 | p-value |  | p, a share of 68.7\% (exact binomial 95\% CI $[62.8\%, 74.1\%]$; sign test $p = 1.13 \times 10^{-9}$). Of the 524 revisions whose input was already at |
| `144` | sections/results_v2.tex:58 | p-value |  | = 1.13 \times 10^{-9}$). Of the 524 revisions whose input was already at or above the sufficiency threshold, 144 (27.5\%) end below it. The asymmetry  |
| `27.5` | sections/results_v2.tex:58 | p-value |  | 13 \times 10^{-9}$). Of the 524 revisions whose input was already at or above the sufficiency threshold, 144 (27.5\%) end below it. The asymmetry is p |
| `194` | sections/results_v2.tex:67 | count or denominator |  | c:supp-figures}): revision raises quality when the input falls below the sufficiency threshold ($+0.35$, $n = 194$) and lowers it when the input is al |
| `0.38` | sections/results_v2.tex:68 | count or denominator |  | ls below the sufficiency threshold ($+0.35$, $n = 194$) and lowers it when the input is already sufficient ($-0.38$, $n = 524$). \paragraph{The revisi |
| `524` | sections/results_v2.tex:68 | count or denominator |  | sufficiency threshold ($+0.35$, $n = 194$) and lowers it when the input is already sufficient ($-0.38$, $n = 524$). \paragraph{The revision cliff.} In |
| `50` | sections/results_v2.tex:71 | count or denominator |  | lowers it when the input is already sufficient ($-0.38$, $n = 524$). \paragraph{The revision cliff.} In the 50 balanced-panel trials (genuine revision |
| `4` | sections/results_v2.tex:74 | p-value |  | one moved the other way (exact binomial $p = 4.01 \times 10^{-5}$), taking the share rated ``Overdone'' from 4\% to 40\%, while the share falling belo |
| `40` | sections/results_v2.tex:74 | p-value |  | ved the other way (exact binomial $p = 4.01 \times 10^{-5}$), taking the share rated ``Overdone'' from 4\% to 40\%, while the share falling below suff |
| `5` | sections/results_v2.tex:74 | p-value |  | ing the share rated ``Overdone'' from 4\% to 40\%, while the share falling below sufficiency does not change (5 in, 11 out, $p = 0.21$). Undirected re |
| `11` | sections/results_v2.tex:75 | p-value |  | e share rated ``Overdone'' from 4\% to 40\%, while the share falling below sufficiency does not change (5 in, 11 out, $p = 0.21$). Undirected revision |
| `0.21` | sections/results_v2.tex:75 | p-value |  | ``Overdone'' from 4\% to 40\%, while the share falling below sufficiency does not change (5 in, 11 out, $p = 0.21$). Undirected revision adds unreques |
| `3.70` | sections/results_v2.tex:76 | p-value |  | erial; it does not drop what was asked for. On the ordinal scale, mean quality on stripped content falls from 3.70 to 3.32, a decline of $-0.38$ level |
| `3.32` | sections/results_v2.tex:76 | p-value |  | t does not drop what was asked for. On the ordinal scale, mean quality on stripped content falls from 3.70 to 3.32, a decline of $-0.38$ levels ($p =  |
| `0.38` | sections/results_v2.tex:77 | p-value |  | was asked for. On the ordinal scale, mean quality on stripped content falls from 3.70 to 3.32, a decline of $-0.38$ levels ($p = 4.42 \times 10^{-3}$; |
| `4.42` | sections/results_v2.tex:77 | p-value |  | he ordinal scale, mean quality on stripped content falls from 3.70 to 3.32, a decline of $-0.38$ levels ($p = 4.42 \times 10^{-3}$; unstripped $-0.44$ |
| `10` | sections/results_v2.tex:77 | p-value |  | cale, mean quality on stripped content falls from 3.70 to 3.32, a decline of $-0.38$ levels ($p = 4.42 \times 10^{-3}$; unstripped $-0.44$, $p = 3.8 \ |
| `3` | sections/results_v2.tex:77 | p-value |  | mean quality on stripped content falls from 3.70 to 3.32, a decline of $-0.38$ levels ($p = 4.42 \times 10^{-3}$; unstripped $-0.44$, $p = 3.8 \times  |
| `0.44` | sections/results_v2.tex:77 | p-value |  | tripped content falls from 3.70 to 3.32, a decline of $-0.38$ levels ($p = 4.42 \times 10^{-3}$; unstripped $-0.44$, $p = 3.8 \times 10^{-4}$), of whi |
| `3.8` | sections/results_v2.tex:77 | p-value |  | ent falls from 3.70 to 3.32, a decline of $-0.38$ levels ($p = 4.42 \times 10^{-3}$; unstripped $-0.44$, $p = 3.8 \times 10^{-4}$), of which 14\% is a |
| `10` | sections/results_v2.tex:78 | p-value |  | rom 3.70 to 3.32, a decline of $-0.38$ levels ($p = 4.42 \times 10^{-3}$; unstripped $-0.44$, $p = 3.8 \times 10^{-4}$), of which 14\% is attributable |
| `4` | sections/results_v2.tex:78 | p-value |  | .70 to 3.32, a decline of $-0.38$ levels ($p = 4.42 \times 10^{-3}$; unstripped $-0.44$, $p = 3.8 \times 10^{-4}$), of which 14\% is attributable to m |
| `45` | sections/results_v2.tex:82 | count or denominator |  | es. The count above does not depend on that placement. The balanced panel is dominated by Llama~3.3~70B ($n = 45$), the only model with power to detec |
| `0.31` | sections/results_v2.tex:83 | p-value |  | y Llama~3.3~70B ($n = 45$), the only model with power to detect a within-model cliff; its stripped cliff of $-0.31$ is significant at $p = 1.80 \times |
| `1.80` | sections/results_v2.tex:83 | p-value |  | he only model with power to detect a within-model cliff; its stripped cliff of $-0.31$ is significant at $p = 1.80 \times 10^{-2}$. GPT-4o, DeepSeek a |
| `10` | sections/results_v2.tex:83 | p-value |  | l with power to detect a within-model cliff; its stripped cliff of $-0.31$ is significant at $p = 1.80 \times 10^{-2}$. GPT-4o, DeepSeek and Gemini co |
| `2` | sections/results_v2.tex:83 | p-value |  | h power to detect a within-model cliff; its stripped cliff of $-0.31$ is significant at $p = 1.80 \times 10^{-2}$. GPT-4o, DeepSeek and Gemini contrib |
| `50` | sections/results_v2.tex:98 | count or denominator | yes | \caption{Quality trajectory under undirected revision (stripped scores). Solid blue: balanced panel ($n = 50$, genuine revision at all turns), showing |
| `0.38` | sections/results_v2.tex:98 | count or denominator | yes | lue: balanced panel ($n = 50$, genuine revision at all turns), showing the balanced-panel cliff of $\Delta = -0.38$ (3.70$\to$3.32). Dashed gray: pool |

## The ledgers, by section, with the filter each number was computed under


### [results_FINAL.md] 

- `3` (results_FINAL.md:1, bare number) # Study 3 Results -- FINAL (Corrected/Stripped Basis)
- `2026` (results_FINAL.md:3, bare number) Generated: 2026-06-10. All numbers use the corrected LLM classifier (718 GENUINE / 2,162 META)
- `06` (results_FINAL.md:3, bare number) Generated: 2026-06-10. All numbers use the corrected LLM classifier (718 GENUINE / 2,162 META)
- `10` (results_FINAL.md:3, bare number) Generated: 2026-06-10. All numbers use the corrected LLM classifier (718 GENUINE / 2,162 META)
- `718` (results_FINAL.md:3, bare number) Generated: 2026-06-10. All numbers use the corrected LLM classifier (718 GENUINE / 2,162 META)
- `2,162` (results_FINAL.md:3, bare number) Generated: 2026-06-10. All numbers use the corrected LLM classifier (718 GENUINE / 2,162 META)

### [results_FINAL.md] 1. CLASSIFIER

- `1` (results_FINAL.md:8, bare number) ## 1. CLASSIFIER
- `718` (results_FINAL.md:10, bare number) - **Final counts:** 718 GENUINE, 2,162 META (total 2,880 post-T1 observations)
- `2,162` (results_FINAL.md:10, bare number) - **Final counts:** 718 GENUINE, 2,162 META (total 2,880 post-T1 observations)
- `2,880` (results_FINAL.md:10, bare number) - **Final counts:** 718 GENUINE, 2,162 META (total 2,880 post-T1 observations)
- `10` (results_FINAL.md:11, bare number) - **10 corrections** applied (GENUINE -> META): 6 Llama, 2 DeepSeek, 1 Qwen, 1 Claude
- `6` (results_FINAL.md:11, bare number) - **10 corrections** applied (GENUINE -> META): 6 Llama, 2 DeepSeek, 1 Qwen, 1 Claude
- `2` (results_FINAL.md:11, bare number) - **10 corrections** applied (GENUINE -> META): 6 Llama, 2 DeepSeek, 1 Qwen, 1 Claude
- `1` (results_FINAL.md:11, bare number) - **10 corrections** applied (GENUINE -> META): 6 Llama, 2 DeepSeek, 1 Qwen, 1 Claude
- `1` (results_FINAL.md:11, bare number) - **10 corrections** applied (GENUINE -> META): 6 Llama, 2 DeepSeek, 1 Qwen, 1 Claude
- `10` (results_FINAL.md:13, percentage) - Correction rate: 10/718 = **1.4%** of GENUINE labels corrected
- `718` (results_FINAL.md:13, percentage) - Correction rate: 10/718 = **1.4%** of GENUINE labels corrected
- `1.4` (results_FINAL.md:13, percentage) - Correction rate: 10/718 = **1.4%** of GENUINE labels corrected
- `85` (results_FINAL.md:14, bare number) - **Validation:** keyword classifier (old) vs LLM classifier (corrected) differ on 85 "complete-revision" trials
- `135` (results_FINAL.md:15, bare number) - Old keyword: 135 trials pass "revised at all 5 turns"
- `5` (results_FINAL.md:15, bare number) - Old keyword: 135 trials pass "revised at all 5 turns"
- `50` (results_FINAL.md:16, bare number) - Corrected LLM: 50 trials have GENUINE at all T2-T5
- `2,880` (results_FINAL.md:19, count or denominator) - **Filter:** Each of 2,880 rows = (trial_id, turn) for turns 2-5 across 720 trials. Field `classifier_label` in {GENUINE, META}. Rows with `[CORRECTED]` in `reason` field are the 10 manual correction
- `2` (results_FINAL.md:19, count or denominator) - **Filter:** Each of 2,880 rows = (trial_id, turn) for turns 2-5 across 720 trials. Field `classifier_label` in {GENUINE, META}. Rows with `[CORRECTED]` in `reason` field are the 10 manual correction
- `5` (results_FINAL.md:19, count or denominator) - **Filter:** Each of 2,880 rows = (trial_id, turn) for turns 2-5 across 720 trials. Field `classifier_label` in {GENUINE, META}. Rows with `[CORRECTED]` in `reason` field are the 10 manual correction
- `720` (results_FINAL.md:19, count or denominator) - **Filter:** Each of 2,880 rows = (trial_id, turn) for turns 2-5 across 720 trials. Field `classifier_label` in {GENUINE, META}. Rows with `[CORRECTED]` in `reason` field are the 10 manual correction
- `10` (results_FINAL.md:19, count or denominator) - **Filter:** Each of 2,880 rows = (trial_id, turn) for turns 2-5 across 720 trials. Field `classifier_label` in {GENUINE, META}. Rows with `[CORRECTED]` in `reason` field are the 10 manual correction

### [results_FINAL.md] 2. THE CLIFF (Quality Trajectory)

*- **Filter:** Each of 2,880 rows = (trial_id, turn) for turns 2-5 across 720 trials. Field `classifier_label` in {GENUINE, META}. Rows with `[CORRECTED]` in `reason` field are the 10 manual corrections.*

- `2` (results_FINAL.md:23, bare number) ## 2. THE CLIFF (Quality Trajectory)

### [results_FINAL.md] 2. THE CLIFF (Quality Trajectory) -- Balanced Panel (GENUINE at all T2-T5)

*- **Filter:** Each of 2,880 rows = (trial_id, turn) for turns 2-5 across 720 trials. Field `classifier_label` in {GENUINE, META}. Rows with `[CORRECTED]` in `reason` field are the 10 manual corrections.*

- `50` (results_FINAL.md:29, bare number) | N | 50 |
- `3.66` (results_FINAL.md:30, mean or delta) | T1 mean | 3.66 |
- `2.72` (results_FINAL.md:31, mean or delta) | T5 mean | 2.72 |
- `0.94` (results_FINAL.md:32, mean or delta) | Delta (T5-T1) | **-0.94** |
- `3` (results_FINAL.md:33, reliability or effect size) | Wilcoxon p | 3.32e-06 |
- `06` (results_FINAL.md:33, reliability or effect size) | Wilcoxon p | 3.32e-06 |
- `0.658` (results_FINAL.md:34, mean or delta) | Effect size r | 0.658 |
- `2` (results_FINAL.md:36, turn index) - **Filter:** Select trials where `genuine_meta_labels.jsonl` has `classifier_label == "GENUINE"` at ALL of turns 2, 3, 4, 5. For each, pull `level` from `evaluator_results.jsonl` at turn 1 and turn 5
- `3` (results_FINAL.md:36, turn index) - **Filter:** Select trials where `genuine_meta_labels.jsonl` has `classifier_label == "GENUINE"` at ALL of turns 2, 3, 4, 5. For each, pull `level` from `evaluator_results.jsonl` at turn 1 and turn 5
- `4` (results_FINAL.md:36, turn index) - **Filter:** Select trials where `genuine_meta_labels.jsonl` has `classifier_label == "GENUINE"` at ALL of turns 2, 3, 4, 5. For each, pull `level` from `evaluator_results.jsonl` at turn 1 and turn 5
- `5` (results_FINAL.md:36, turn index) - **Filter:** Select trials where `genuine_meta_labels.jsonl` has `classifier_label == "GENUINE"` at ALL of turns 2, 3, 4, 5. For each, pull `level` from `evaluator_results.jsonl` at turn 1 and turn 5
- `1` (results_FINAL.md:36, turn index) - **Filter:** Select trials where `genuine_meta_labels.jsonl` has `classifier_label == "GENUINE"` at ALL of turns 2, 3, 4, 5. For each, pull `level` from `evaluator_results.jsonl` at turn 1 and turn 5
- `5` (results_FINAL.md:36, turn index) - **Filter:** Select trials where `genuine_meta_labels.jsonl` has `classifier_label == "GENUINE"` at ALL of turns 2, 3, 4, 5. For each, pull `level` from `evaluator_results.jsonl` at turn 1 and turn 5
- `6` (results_FINAL.md:36, turn index) - **Filter:** Select trials where `genuine_meta_labels.jsonl` has `classifier_label == "GENUINE"` at ALL of turns 2, 3, 4, 5. For each, pull `level` from `evaluator_results.jsonl` at turn 1 and turn 5
- `2` (results_FINAL.md:36, turn index) - **Filter:** Select trials where `genuine_meta_labels.jsonl` has `classifier_label == "GENUINE"` at ALL of turns 2, 3, 4, 5. For each, pull `level` from `evaluator_results.jsonl` at turn 1 and turn 5

### [results_FINAL.md] 2. THE CLIFF (Quality Trajectory) -- Per-Model (balanced panel)

*- **Filter:** Select trials where `genuine_meta_labels.jsonl` has `classifier_label == "GENUINE"` at ALL of turns 2, 3, 4, 5. For each, pull `level` from `evaluator_results.jsonl` at turn 1 and turn 5 (keyed by `worker_trial_id` + `turn`). Recode level 6 -> 2. Paired Wilcoxon signed-rank on (T1, T5)*

- `3.3` (results_FINAL.md:42, mean or delta) | llama-3.3-70b | 45 | 3.53 | 2.71 | **-0.82** | 1.81e-05 | 0.639 |
- `45` (results_FINAL.md:42, mean or delta) | llama-3.3-70b | 45 | 3.53 | 2.71 | **-0.82** | 1.81e-05 | 0.639 |
- `3.53` (results_FINAL.md:42, mean or delta) | llama-3.3-70b | 45 | 3.53 | 2.71 | **-0.82** | 1.81e-05 | 0.639 |
- `2.71` (results_FINAL.md:42, mean or delta) | llama-3.3-70b | 45 | 3.53 | 2.71 | **-0.82** | 1.81e-05 | 0.639 |
- `0.82` (results_FINAL.md:42, mean or delta) | llama-3.3-70b | 45 | 3.53 | 2.71 | **-0.82** | 1.81e-05 | 0.639 |
- `1` (results_FINAL.md:42, mean or delta) | llama-3.3-70b | 45 | 3.53 | 2.71 | **-0.82** | 1.81e-05 | 0.639 |
- `05` (results_FINAL.md:42, mean or delta) | llama-3.3-70b | 45 | 3.53 | 2.71 | **-0.82** | 1.81e-05 | 0.639 |
- `0.639` (results_FINAL.md:42, mean or delta) | llama-3.3-70b | 45 | 3.53 | 2.71 | **-0.82** | 1.81e-05 | 0.639 |
- `3` (results_FINAL.md:43, mean or delta) | qwen-3-235b | 3 | 5.00 | 2.00 | -3.00 | n<5 | -- |
- `3` (results_FINAL.md:43, mean or delta) | qwen-3-235b | 3 | 5.00 | 2.00 | -3.00 | n<5 | -- |
- `5.00` (results_FINAL.md:43, mean or delta) | qwen-3-235b | 3 | 5.00 | 2.00 | -3.00 | n<5 | -- |
- `2.00` (results_FINAL.md:43, mean or delta) | qwen-3-235b | 3 | 5.00 | 2.00 | -3.00 | n<5 | -- |
- `3.00` (results_FINAL.md:43, mean or delta) | qwen-3-235b | 3 | 5.00 | 2.00 | -3.00 | n<5 | -- |
- `5` (results_FINAL.md:43, mean or delta) | qwen-3-235b | 3 | 5.00 | 2.00 | -3.00 | n<5 | -- |
- `4` (results_FINAL.md:44, mean or delta) | claude-sonnet-4 | 2 | 4.50 | 4.00 | -0.50 | n<5 | -- |
- `2` (results_FINAL.md:44, mean or delta) | claude-sonnet-4 | 2 | 4.50 | 4.00 | -0.50 | n<5 | -- |
- `4.50` (results_FINAL.md:44, mean or delta) | claude-sonnet-4 | 2 | 4.50 | 4.00 | -0.50 | n<5 | -- |
- `4.00` (results_FINAL.md:44, mean or delta) | claude-sonnet-4 | 2 | 4.50 | 4.00 | -0.50 | n<5 | -- |
- `0.50` (results_FINAL.md:44, mean or delta) | claude-sonnet-4 | 2 | 4.50 | 4.00 | -0.50 | n<5 | -- |
- `5` (results_FINAL.md:44, mean or delta) | claude-sonnet-4 | 2 | 4.50 | 4.00 | -0.50 | n<5 | -- |
- `0` (results_FINAL.md:45, bare number) | gpt-4o | 0 | -- | -- | -- | -- | -- |
- `0` (results_FINAL.md:46, bare number) | deepseek-v4 | 0 | -- | -- | -- | -- | -- |
- `2.5` (results_FINAL.md:47, mean or delta) | gemini-2.5-flash | 0 | -- | -- | -- | -- | -- |
- `0` (results_FINAL.md:47, mean or delta) | gemini-2.5-flash | 0 | -- | -- | -- | -- | -- |
- `90` (results_FINAL.md:49, percentage) **NOTE:** GPT-4o, DeepSeek, and Gemini have ZERO balanced-panel trials (no trials with GENUINE at all T2-T5). The balanced panel is 90% Llama. Only Llama's cliff is statistically powered. Claude and Q
- `2` (results_FINAL.md:49, percentage) **NOTE:** GPT-4o, DeepSeek, and Gemini have ZERO balanced-panel trials (no trials with GENUINE at all T2-T5). The balanced panel is 90% Llama. Only Llama's cliff is statistically powered. Claude and Q
- `3` (results_FINAL.md:49, percentage) **NOTE:** GPT-4o, DeepSeek, and Gemini have ZERO balanced-panel trials (no trials with GENUINE at all T2-T5). The balanced panel is 90% Llama. Only Llama's cliff is statistically powered. Claude and Q
- `0.50` (results_FINAL.md:51, count or denominator) **DISCLOSURE -- Revision Style:** Llama revises incrementally (mean SequenceMatcher similarity to prior turn = 0.50, median 0.51) while other models that revise tend toward wholesale rewrites (mean si
- `0.51` (results_FINAL.md:51, count or denominator) **DISCLOSURE -- Revision Style:** Llama revises incrementally (mean SequenceMatcher similarity to prior turn = 0.50, median 0.51) while other models that revise tend toward wholesale rewrites (mean si
- `0.15` (results_FINAL.md:51, count or denominator) **DISCLOSURE -- Revision Style:** Llama revises incrementally (mean SequenceMatcher similarity to prior turn = 0.50, median 0.51) while other models that revise tend toward wholesale rewrites (mean si
- `0.34` (results_FINAL.md:51, count or denominator) **DISCLOSURE -- Revision Style:** Llama revises incrementally (mean SequenceMatcher similarity to prior turn = 0.50, median 0.51) while other models that revise tend toward wholesale rewrites (mean si
- `1.71` (results_FINAL.md:51, count or denominator) **DISCLOSURE -- Revision Style:** Llama revises incrementally (mean SequenceMatcher similarity to prior turn = 0.50, median 0.51) while other models that revise tend toward wholesale rewrites (mean si
- `7` (results_FINAL.md:51, count or denominator) **DISCLOSURE -- Revision Style:** Llama revises incrementally (mean SequenceMatcher similarity to prior turn = 0.50, median 0.51) while other models that revise tend toward wholesale rewrites (mean si
- `3.00` (results_FINAL.md:51, count or denominator) **DISCLOSURE -- Revision Style:** Llama revises incrementally (mean SequenceMatcher similarity to prior turn = 0.50, median 0.51) while other models that revise tend toward wholesale rewrites (mean si
- `6` (results_FINAL.md:51, count or denominator) **DISCLOSURE -- Revision Style:** Llama revises incrementally (mean SequenceMatcher similarity to prior turn = 0.50, median 0.51) while other models that revise tend toward wholesale rewrites (mean si
- `0.81` (results_FINAL.md:51, count or denominator) **DISCLOSURE -- Revision Style:** Llama revises incrementally (mean SequenceMatcher similarity to prior turn = 0.50, median 0.51) while other models that revise tend toward wholesale rewrites (mean si
- `64` (results_FINAL.md:51, count or denominator) **DISCLOSURE -- Revision Style:** Llama revises incrementally (mean SequenceMatcher similarity to prior turn = 0.50, median 0.51) while other models that revise tend toward wholesale rewrites (mean si
- `2026` (results_FINAL.md:51, count or denominator) **DISCLOSURE -- Revision Style:** Llama revises incrementally (mean SequenceMatcher similarity to prior turn = 0.50, median 0.51) while other models that revise tend toward wholesale rewrites (mean si
- `06` (results_FINAL.md:51, count or denominator) **DISCLOSURE -- Revision Style:** Llama revises incrementally (mean SequenceMatcher similarity to prior turn = 0.50, median 0.51) while other models that revise tend toward wholesale rewrites (mean si
- `11` (results_FINAL.md:51, count or denominator) **DISCLOSURE -- Revision Style:** Llama revises incrementally (mean SequenceMatcher similarity to prior turn = 0.50, median 0.51) while other models that revise tend toward wholesale rewrites (mean si

### [results_FINAL.md] 2. THE CLIFF (Quality Trajectory) -- Stripped Cliff: significance test (added 2026-09-07, resolving RECOMPUTE_TODO)

*- **Filter:** Select trials where `genuine_meta_labels.jsonl` has `classifier_label == "GENUINE"` at ALL of turns 2, 3, 4, 5. For each, pull `level` from `evaluator_results.jsonl` at turn 1 and turn 5 (keyed by `worker_trial_id` + `turn`). Recode level 6 -> 2. Paired Wilcoxon signed-rank on (T1, T5)*

- `2026` (results_FINAL.md:53, bare number) ### Stripped Cliff: significance test (added 2026-09-07, resolving RECOMPUTE_TODO)
- `09` (results_FINAL.md:53, bare number) ### Stripped Cliff: significance test (added 2026-09-07, resolving RECOMPUTE_TODO)
- `07` (results_FINAL.md:53, bare number) ### Stripped Cliff: significance test (added 2026-09-07, resolving RECOMPUTE_TODO)
- `3` (results_FINAL.md:55, bare number) The paper printed p and r for the stripped cliff in `results_v2.tex` Table 3, the conclusion
- `2026` (results_FINAL.md:56, bare number) and the appendix, with no entry anywhere in this ledger. Recomputed 2026-09-07 and recorded
- `09` (results_FINAL.md:56, bare number) and the appendix, with no entry anywhere in this ledger. Recomputed 2026-09-07 and recorded
- `07` (results_FINAL.md:56, bare number) and the appendix, with no entry anywhere in this ledger. Recomputed 2026-09-07 and recorded
- `2026` (results_FINAL.md:57, bare number) here. `RECOMPUTE_TODO.md` asked for exactly this and was closed in error on 2026-09-02.
- `09` (results_FINAL.md:57, bare number) here. `RECOMPUTE_TODO.md` asked for exactly this and was closed in error on 2026-09-02.
- `02` (results_FINAL.md:57, bare number) here. `RECOMPUTE_TODO.md` asked for exactly this and was closed in error on 2026-09-02.
- `50` (results_FINAL.md:61, mean or delta) | All balanced | 50 | 3.66 | 2.92 | **-0.74** | 54.5 | **1.01e-4** | 0.536 | 0.681 |
- `3.66` (results_FINAL.md:61, mean or delta) | All balanced | 50 | 3.66 | 2.92 | **-0.74** | 54.5 | **1.01e-4** | 0.536 | 0.681 |
- `2.92` (results_FINAL.md:61, mean or delta) | All balanced | 50 | 3.66 | 2.92 | **-0.74** | 54.5 | **1.01e-4** | 0.536 | 0.681 |
- `0.74` (results_FINAL.md:61, mean or delta) | All balanced | 50 | 3.66 | 2.92 | **-0.74** | 54.5 | **1.01e-4** | 0.536 | 0.681 |
- `54.5` (results_FINAL.md:61, mean or delta) | All balanced | 50 | 3.66 | 2.92 | **-0.74** | 54.5 | **1.01e-4** | 0.536 | 0.681 |
- `1` (results_FINAL.md:61, mean or delta) | All balanced | 50 | 3.66 | 2.92 | **-0.74** | 54.5 | **1.01e-4** | 0.536 | 0.681 |
- `4` (results_FINAL.md:61, mean or delta) | All balanced | 50 | 3.66 | 2.92 | **-0.74** | 54.5 | **1.01e-4** | 0.536 | 0.681 |
- `0.536` (results_FINAL.md:61, mean or delta) | All balanced | 50 | 3.66 | 2.92 | **-0.74** | 54.5 | **1.01e-4** | 0.536 | 0.681 |
- `0.681` (results_FINAL.md:61, mean or delta) | All balanced | 50 | 3.66 | 2.92 | **-0.74** | 54.5 | **1.01e-4** | 0.536 | 0.681 |
- `45` (results_FINAL.md:62, mean or delta) | Llama only | 45 | 3.53 | 2.87 | **-0.67** | 51.5 | **3.76e-4** | 0.514 | 0.652 |
- `3.53` (results_FINAL.md:62, mean or delta) | Llama only | 45 | 3.53 | 2.87 | **-0.67** | 51.5 | **3.76e-4** | 0.514 | 0.652 |
- `2.87` (results_FINAL.md:62, mean or delta) | Llama only | 45 | 3.53 | 2.87 | **-0.67** | 51.5 | **3.76e-4** | 0.514 | 0.652 |
- `0.67` (results_FINAL.md:62, mean or delta) | Llama only | 45 | 3.53 | 2.87 | **-0.67** | 51.5 | **3.76e-4** | 0.514 | 0.652 |
- `51.5` (results_FINAL.md:62, mean or delta) | Llama only | 45 | 3.53 | 2.87 | **-0.67** | 51.5 | **3.76e-4** | 0.514 | 0.652 |
- `3` (results_FINAL.md:62, mean or delta) | Llama only | 45 | 3.53 | 2.87 | **-0.67** | 51.5 | **3.76e-4** | 0.514 | 0.652 |
- `4` (results_FINAL.md:62, mean or delta) | Llama only | 45 | 3.53 | 2.87 | **-0.67** | 51.5 | **3.76e-4** | 0.514 | 0.652 |
- `0.514` (results_FINAL.md:62, mean or delta) | Llama only | 45 | 3.53 | 2.87 | **-0.67** | 51.5 | **3.76e-4** | 0.514 | 0.652 |
- `0.652` (results_FINAL.md:62, mean or delta) | Llama only | 45 | 3.53 | 2.87 | **-0.67** | 51.5 | **3.76e-4** | 0.514 | 0.652 |
- `50` (results_FINAL.md:64, bare number) - **Filter:** the 50 balanced-panel trials (GENUINE at all of turns 2-5). Stripped levels at
- `2` (results_FINAL.md:64, bare number) - **Filter:** the 50 balanced-panel trials (GENUINE at all of turns 2-5). Stripped levels at
- `5` (results_FINAL.md:64, bare number) - **Filter:** the 50 balanced-panel trials (GENUINE at all of turns 2-5). Stripped levels at
- `1` (results_FINAL.md:65, bare number) turns 1 and 5 from `stripped_rescore_full.jsonl` field `stripped_score`, 6 -> 2 recode
- `5` (results_FINAL.md:65, bare number) turns 1 and 5 from `stripped_rescore_full.jsonl` field `stripped_score`, 6 -> 2 recode
- `6` (results_FINAL.md:65, bare number) turns 1 and 5 from `stripped_rescore_full.jsonl` field `stripped_score`, 6 -> 2 recode
- `2` (results_FINAL.md:65, bare number) turns 1 and 5 from `stripped_rescore_full.jsonl` field `stripped_score`, 6 -> 2 recode
- `31` (results_FINAL.md:67, count or denominator) 31 of 50 all-balanced, 28 of 45 Llama.
- `50` (results_FINAL.md:67, count or denominator) 31 of 50 all-balanced, 28 of 45 Llama.
- `28` (results_FINAL.md:67, count or denominator) 31 of 50 all-balanced, 28 of 45 Llama.
- `45` (results_FINAL.md:67, count or denominator) 31 of 50 all-balanced, 28 of 45 Llama.
- `1` (results_FINAL.md:73, bare number) 1. **Effect size. WITHDRAWN 2026-09-17. This discrepancy was an artifact of the 2026-09-07
- `2026` (results_FINAL.md:73, bare number) 1. **Effect size. WITHDRAWN 2026-09-17. This discrepancy was an artifact of the 2026-09-07
- `09` (results_FINAL.md:73, bare number) 1. **Effect size. WITHDRAWN 2026-09-17. This discrepancy was an artifact of the 2026-09-07
- `17` (results_FINAL.md:73, bare number) 1. **Effect size. WITHDRAWN 2026-09-17. This discrepancy was an artifact of the 2026-09-07
- `2026` (results_FINAL.md:73, bare number) 1. **Effect size. WITHDRAWN 2026-09-17. This discrepancy was an artifact of the 2026-09-07
- `09` (results_FINAL.md:73, bare number) 1. **Effect size. WITHDRAWN 2026-09-17. This discrepancy was an artifact of the 2026-09-07
- `07` (results_FINAL.md:73, bare number) 1. **Effect size. WITHDRAWN 2026-09-17. This discrepancy was an artifact of the 2026-09-07
- `0.55` (results_FINAL.md:76, reliability or effect size) > The paper prints r = 0.55 (all) and r = 0.53 (Llama). Recomputation gives 0.536 and 0.514
- `0.53` (results_FINAL.md:76, reliability or effect size) > The paper prints r = 0.55 (all) and r = 0.53 (Llama). Recomputation gives 0.536 and 0.514
- `0.536` (results_FINAL.md:76, reliability or effect size) > The paper prints r = 0.55 (all) and r = 0.53 (Llama). Recomputation gives 0.536 and 0.514
- `0.514` (results_FINAL.md:76, reliability or effect size) > The paper prints r = 0.55 (all) and r = 0.53 (Llama). Recomputation gives 0.536 and 0.514
- `0.681` (results_FINAL.md:77, count or denominator) > dividing by N = all trials, or 0.681 and 0.652 dividing by N = non-zero differences. The
- `0.652` (results_FINAL.md:77, count or denominator) > dividing by N = all trials, or 0.681 and 0.652 dividing by N = non-zero differences. The
- `0.5498` (results_FINAL.md:82, mean or delta) gives **0.5498 for the all-balanced stripped cliff and 0.5301 for Llama**, which are exactly
- `0.5301` (results_FINAL.md:82, mean or delta) gives **0.5498 for the all-balanced stripped cliff and 0.5301 for Llama**, which are exactly
- `0.55` (results_FINAL.md:83, mean or delta) the printed 0.55 and 0.53.
- `0.53` (results_FINAL.md:83, mean or delta) the printed 0.55 and 0.53.
- `0.658` (results_FINAL.md:85, count or denominator) The consistency check that settles it: the unstripped r of 0.658 recorded at line 34 and
- `34` (results_FINAL.md:85, count or denominator) The consistency check that settles it: the unstripped r of 0.658 recorded at line 34 and
- `0.639` (results_FINAL.md:86, mean or delta) 0.639 at line 42 are not in dispute. Tie-corrected they recompute as 0.6576 and 0.6391, which
- `42` (results_FINAL.md:86, mean or delta) 0.639 at line 42 are not in dispute. Tie-corrected they recompute as 0.6576 and 0.6391, which
- `0.6576` (results_FINAL.md:86, mean or delta) 0.639 at line 42 are not in dispute. Tie-corrected they recompute as 0.6576 and 0.6391, which
- `0.6391` (results_FINAL.md:86, mean or delta) 0.639 at line 42 are not in dispute. Tie-corrected they recompute as 0.6576 and 0.6391, which
- `0.6416` (results_FINAL.md:87, mean or delta) round to the recorded values. Uncorrected they give 0.6416 and 0.6193, which do not. So the
- `0.6193` (results_FINAL.md:87, mean or delta) round to the recorded values. Uncorrected they give 0.6416 and 0.6193, which do not. So the
- `2026` (results_FINAL.md:91, bare number) Verified twice on 2026-09-17, independently, from `stripped_rescore_full.jsonl` and
- `09` (results_FINAL.md:91, bare number) Verified twice on 2026-09-17, independently, from `stripped_rescore_full.jsonl` and
- `17` (results_FINAL.md:91, bare number) Verified twice on 2026-09-17, independently, from `stripped_rescore_full.jsonl` and
- `6` (results_FINAL.md:92, bare number) `evaluator_results.jsonl` with the 6->2 recode and the balanced-panel filter as specified
- `2` (results_FINAL.md:92, bare number) `evaluator_results.jsonl` with the 6->2 recode and the balanced-panel filter as specified
- `1` (results_FINAL.md:93, mean or delta) above. The p-values reproduce exactly as already recorded (1.011e-4 and 3.760e-4).
- `4` (results_FINAL.md:93, mean or delta) above. The p-values reproduce exactly as already recorded (1.011e-4 and 3.760e-4).
- `3` (results_FINAL.md:93, mean or delta) above. The p-values reproduce exactly as already recorded (1.011e-4 and 3.760e-4).
- `4` (results_FINAL.md:93, mean or delta) above. The p-values reproduce exactly as already recorded (1.011e-4 and 3.760e-4).
- `0.55` (results_FINAL.md:96, mean or delta) two defensible divisors give 0.55 against 0.70 for the same result. Stating the formula is
- `0.70` (results_FINAL.md:96, mean or delta) two defensible divisors give 0.55 against 0.70 for the same result. Stating the formula is
- `2` (results_FINAL.md:99, mean or delta) 2. **Llama delta.** This computation gives -0.67 from the full 3,600-output rescore. The paper
- `0.67` (results_FINAL.md:99, mean or delta) 2. **Llama delta.** This computation gives -0.67 from the full 3,600-output rescore. The paper
- `3,600` (results_FINAL.md:99, mean or delta) 2. **Llama delta.** This computation gives -0.67 from the full 3,600-output rescore. The paper
- `0.69` (results_FINAL.md:100, mean or delta) prints -0.69, which comes from the 50-pair rescore in `stripped_rescore_results.json`. Table 3
- `50` (results_FINAL.md:100, mean or delta) prints -0.69, which comes from the 50-pair rescore in `stripped_rescore_results.json`. Table 3
- `3` (results_FINAL.md:100, mean or delta) prints -0.69, which comes from the 50-pair rescore in `stripped_rescore_results.json`. Table 3
- `50` (results_FINAL.md:102, bare number) Llama row on the 50-pair rescore. Independently confirms the finding in

### [results_FINAL.md] 2. THE CLIFF (Quality Trajectory) -- Stripped Cliff (meta-commentary removed, re-scored)

*- **Filter:** the 50 balanced-panel trials (GENUINE at all of turns 2-5). Stripped levels at*

- `50` (results_FINAL.md:109, percentage) | All (n=50) | -0.94 | **-0.76** | 0.18 (19%) |
- `0.94` (results_FINAL.md:109, percentage) | All (n=50) | -0.94 | **-0.76** | 0.18 (19%) |
- `0.76` (results_FINAL.md:109, percentage) | All (n=50) | -0.94 | **-0.76** | 0.18 (19%) |
- `0.18` (results_FINAL.md:109, percentage) | All (n=50) | -0.94 | **-0.76** | 0.18 (19%) |
- `19` (results_FINAL.md:109, percentage) | All (n=50) | -0.94 | **-0.76** | 0.18 (19%) |
- `45` (results_FINAL.md:110, percentage) | Llama (n=45) | -0.82 | **-0.69** | 0.13 (16%) |
- `0.82` (results_FINAL.md:110, percentage) | Llama (n=45) | -0.82 | **-0.69** | 0.13 (16%) |
- `0.69` (results_FINAL.md:110, percentage) | Llama (n=45) | -0.82 | **-0.69** | 0.13 (16%) |
- `0.13` (results_FINAL.md:110, percentage) | Llama (n=45) | -0.82 | **-0.69** | 0.13 (16%) |
- `16` (results_FINAL.md:110, percentage) | Llama (n=45) | -0.82 | **-0.69** | 0.13 (16%) |
- `39` (results_FINAL.md:111, percentage) | Llama excl. near-trivial (n=39) | -0.79 | **-0.69** | 0.10 (13%) |
- `0.79` (results_FINAL.md:111, percentage) | Llama excl. near-trivial (n=39) | -0.79 | **-0.69** | 0.10 (13%) |
- `0.69` (results_FINAL.md:111, percentage) | Llama excl. near-trivial (n=39) | -0.79 | **-0.69** | 0.10 (13%) |
- `0.10` (results_FINAL.md:111, percentage) | Llama excl. near-trivial (n=39) | -0.79 | **-0.69** | 0.10 (13%) |
- `13` (results_FINAL.md:111, percentage) | Llama excl. near-trivial (n=39) | -0.79 | **-0.69** | 0.10 (13%) |
- `81` (results_FINAL.md:113, percentage) **The cliff is 81% real content degradation, 19% meta-commentary artifact.**
- `19` (results_FINAL.md:113, percentage) **The cliff is 81% real content degradation, 19% meta-commentary artifact.**
- `6` (results_FINAL.md:115, p-value) **DISCLOSURE -- Near-Trivial Edits:** 6 of 45 Llama balanced-panel trials contain at least one turn with >0.95 similarity to the prior turn (restatements with minimal change; 4 of these are character-
- `45` (results_FINAL.md:115, p-value) **DISCLOSURE -- Near-Trivial Edits:** 6 of 45 Llama balanced-panel trials contain at least one turn with >0.95 similarity to the prior turn (restatements with minimal change; 4 of these are character-
- `0.95` (results_FINAL.md:115, p-value) **DISCLOSURE -- Near-Trivial Edits:** 6 of 45 Llama balanced-panel trials contain at least one turn with >0.95 similarity to the prior turn (restatements with minimal change; 4 of these are character-
- `4` (results_FINAL.md:115, p-value) **DISCLOSURE -- Near-Trivial Edits:** 6 of 45 Llama balanced-panel trials contain at least one turn with >0.95 similarity to the prior turn (restatements with minimal change; 4 of these are character-
- `1.00` (results_FINAL.md:115, p-value) **DISCLOSURE -- Near-Trivial Edits:** 6 of 45 Llama balanced-panel trials contain at least one turn with >0.95 similarity to the prior turn (restatements with minimal change; 4 of these are character-
- `6` (results_FINAL.md:115, p-value) **DISCLOSURE -- Near-Trivial Edits:** 6 of 45 Llama balanced-panel trials contain at least one turn with >0.95 similarity to the prior turn (restatements with minimal change; 4 of these are character-
- `0.79` (results_FINAL.md:115, p-value) **DISCLOSURE -- Near-Trivial Edits:** 6 of 45 Llama balanced-panel trials contain at least one turn with >0.95 similarity to the prior turn (restatements with minimal change; 4 of these are character-
- `8` (results_FINAL.md:115, p-value) **DISCLOSURE -- Near-Trivial Edits:** 6 of 45 Llama balanced-panel trials contain at least one turn with >0.95 similarity to the prior turn (restatements with minimal change; 4 of these are character-
- `05` (results_FINAL.md:115, p-value) **DISCLOSURE -- Near-Trivial Edits:** 6 of 45 Llama balanced-panel trials contain at least one turn with >0.95 similarity to the prior turn (restatements with minimal change; 4 of these are character-
- `0.628` (results_FINAL.md:115, p-value) **DISCLOSURE -- Near-Trivial Edits:** 6 of 45 Llama balanced-panel trials contain at least one turn with >0.95 similarity to the prior turn (restatements with minimal change; 4 of these are character-
- `0.69` (results_FINAL.md:115, p-value) **DISCLOSURE -- Near-Trivial Edits:** 6 of 45 Llama balanced-panel trials contain at least one turn with >0.95 similarity to the prior turn (restatements with minimal change; 4 of these are character-
- `0.82` (results_FINAL.md:115, p-value) **DISCLOSURE -- Near-Trivial Edits:** 6 of 45 Llama balanced-panel trials contain at least one turn with >0.95 similarity to the prior turn (restatements with minimal change; 4 of these are character-
- `0.69` (results_FINAL.md:115, p-value) **DISCLOSURE -- Near-Trivial Edits:** 6 of 45 Llama balanced-panel trials contain at least one turn with >0.95 similarity to the prior turn (restatements with minimal change; 4 of these are character-
- `45` (results_FINAL.md:115, p-value) **DISCLOSURE -- Near-Trivial Edits:** 6 of 45 Llama balanced-panel trials contain at least one turn with >0.95 similarity to the prior turn (restatements with minimal change; 4 of these are character-
- `0.03` (results_FINAL.md:115, p-value) **DISCLOSURE -- Near-Trivial Edits:** 6 of 45 Llama balanced-panel trials contain at least one turn with >0.95 similarity to the prior turn (restatements with minimal change; 4 of these are character-
- `2026` (results_FINAL.md:115, p-value) **DISCLOSURE -- Near-Trivial Edits:** 6 of 45 Llama balanced-panel trials contain at least one turn with >0.95 similarity to the prior turn (restatements with minimal change; 4 of these are character-
- `06` (results_FINAL.md:115, p-value) **DISCLOSURE -- Near-Trivial Edits:** 6 of 45 Llama balanced-panel trials contain at least one turn with >0.95 similarity to the prior turn (restatements with minimal change; 4 of these are character-
- `11` (results_FINAL.md:115, p-value) **DISCLOSURE -- Near-Trivial Edits:** 6 of 45 Llama balanced-panel trials contain at least one turn with >0.95 similarity to the prior turn (restatements with minimal change; 4 of these are character-
- `50` (results_FINAL.md:119, bare number) - **Filter (stripped rescore):** Same 50 balanced-panel trials. For each, strip meta-commentary from T1 and T5 text using regex preamble/postamble patterns (from `strip_meta_commentary.py`). Re-score 
- `4` (results_FINAL.md:119, bare number) - **Filter (stripped rescore):** Same 50 balanced-panel trials. For each, strip meta-commentary from T1 and T5 text using regex preamble/postamble patterns (from `strip_meta_commentary.py`). Re-score 
- `4` (results_FINAL.md:119, bare number) - **Filter (stripped rescore):** Same 50 balanced-panel trials. For each, strip meta-commentary from T1 and T5 text using regex preamble/postamble patterns (from `strip_meta_commentary.py`). Re-score 
- `20250514` (results_FINAL.md:119, bare number) - **Filter (stripped rescore):** Same 50 balanced-panel trials. For each, strip meta-commentary from T1 and T5 text using regex preamble/postamble patterns (from `strip_meta_commentary.py`). Re-score 
- `0` (results_FINAL.md:119, bare number) - **Filter (stripped rescore):** Same 50 balanced-panel trials. For each, strip meta-commentary from T1 and T5 text using regex preamble/postamble patterns (from `strip_meta_commentary.py`). Re-score 
- `6` (results_FINAL.md:119, bare number) - **Filter (stripped rescore):** Same 50 balanced-panel trials. For each, strip meta-commentary from T1 and T5 text using regex preamble/postamble patterns (from `strip_meta_commentary.py`). Re-score 
- `2` (results_FINAL.md:119, bare number) - **Filter (stripped rescore):** Same 50 balanced-panel trials. For each, strip meta-commentary from T1 and T5 text using regex preamble/postamble patterns (from `strip_meta_commentary.py`). Re-score 

### [results_FINAL.md] 3. REVISION RATE

*- **Filter (stripped rescore):** Same 50 balanced-panel trials. For each, strip meta-commentary from T1 and T5 text using regex preamble/postamble patterns (from `strip_meta_commentary.py`). Re-score stripped text via Claude Sonnet 4 (`claude-sonnet-4-20250514`) at temperature 0 using the same EVAL_*

- `3` (results_FINAL.md:123, bare number) ## 3. REVISION RATE
- `283` (results_FINAL.md:127, percentage) | T2 | 283/720 | 39.3% |
- `720` (results_FINAL.md:127, percentage) | T2 | 283/720 | 39.3% |
- `39.3` (results_FINAL.md:127, percentage) | T2 | 283/720 | 39.3% |
- `185` (results_FINAL.md:128, percentage) | T3 | 185/720 | 25.7% |
- `720` (results_FINAL.md:128, percentage) | T3 | 185/720 | 25.7% |
- `25.7` (results_FINAL.md:128, percentage) | T3 | 185/720 | 25.7% |
- `154` (results_FINAL.md:129, percentage) | T4 | 154/720 | 21.4% |
- `720` (results_FINAL.md:129, percentage) | T4 | 154/720 | 21.4% |
- `21.4` (results_FINAL.md:129, percentage) | T4 | 154/720 | 21.4% |
- `96` (results_FINAL.md:130, percentage) | T5 | 96/720 | 13.3% |
- `720` (results_FINAL.md:130, percentage) | T5 | 96/720 | 13.3% |
- `13.3` (results_FINAL.md:130, percentage) | T5 | 96/720 | 13.3% |
- `2` (results_FINAL.md:132, bare number) - **Filter:** For each turn T in {2,3,4,5}, count trials where `genuine_meta_labels.jsonl` has `classifier_label == "GENUINE"` at that turn. Denominator = 720 (all successful trials).
- `3` (results_FINAL.md:132, bare number) - **Filter:** For each turn T in {2,3,4,5}, count trials where `genuine_meta_labels.jsonl` has `classifier_label == "GENUINE"` at that turn. Denominator = 720 (all successful trials).
- `4` (results_FINAL.md:132, bare number) - **Filter:** For each turn T in {2,3,4,5}, count trials where `genuine_meta_labels.jsonl` has `classifier_label == "GENUINE"` at that turn. Denominator = 720 (all successful trials).
- `5` (results_FINAL.md:132, bare number) - **Filter:** For each turn T in {2,3,4,5}, count trials where `genuine_meta_labels.jsonl` has `classifier_label == "GENUINE"` at that turn. Denominator = 720 (all successful trials).
- `720` (results_FINAL.md:132, bare number) - **Filter:** For each turn T in {2,3,4,5}, count trials where `genuine_meta_labels.jsonl` has `classifier_label == "GENUINE"` at that turn. Denominator = 720 (all successful trials).

### [results_FINAL.md] 4. REVISION-DESPITE-SUFFICIENCY

*- **Filter:** For each turn T in {2,3,4,5}, count trials where `genuine_meta_labels.jsonl` has `classifier_label == "GENUINE"` at that turn. Denominator = 720 (all successful trials).*

- `4` (results_FINAL.md:137, bare number) ## 4. REVISION-DESPITE-SUFFICIENCY
- `631` (results_FINAL.md:141, percentage) | T1 sufficiency rate | 631/720 (87.6%) |
- `720` (results_FINAL.md:141, percentage) | T1 sufficiency rate | 631/720 (87.6%) |
- `87.6` (results_FINAL.md:141, percentage) | T1 sufficiency rate | 631/720 (87.6%) |
- `368` (results_FINAL.md:142, percentage) | Sufficient turns with revision at next | 368/938 = **39.2%** |
- `938` (results_FINAL.md:142, percentage) | Sufficient turns with revision at next | 368/938 = **39.2%** |
- `39.2` (results_FINAL.md:142, percentage) | Sufficient turns with revision at next | 368/938 = **39.2%** |
- `95` (results_FINAL.md:143, percentage) | Bootstrap 95% CI | [36.1%, 42.3%] |
- `36.1` (results_FINAL.md:143, percentage) | Bootstrap 95% CI | [36.1%, 42.3%] |
- `42.3` (results_FINAL.md:143, percentage) | Bootstrap 95% CI | [36.1%, 42.3%] |
- `1` (results_FINAL.md:145, confidence interval) - **Filter:** For every (trial, turn) pair where turn in {1,2,3,4}, pull `level` from `evaluator_results.jsonl` (recode 6 -> 2). If level >= 4 ("sufficient"), check whether `genuine_meta_labels.jsonl`
- `2` (results_FINAL.md:145, confidence interval) - **Filter:** For every (trial, turn) pair where turn in {1,2,3,4}, pull `level` from `evaluator_results.jsonl` (recode 6 -> 2). If level >= 4 ("sufficient"), check whether `genuine_meta_labels.jsonl`
- `3` (results_FINAL.md:145, confidence interval) - **Filter:** For every (trial, turn) pair where turn in {1,2,3,4}, pull `level` from `evaluator_results.jsonl` (recode 6 -> 2). If level >= 4 ("sufficient"), check whether `genuine_meta_labels.jsonl`
- `4` (results_FINAL.md:145, confidence interval) - **Filter:** For every (trial, turn) pair where turn in {1,2,3,4}, pull `level` from `evaluator_results.jsonl` (recode 6 -> 2). If level >= 4 ("sufficient"), check whether `genuine_meta_labels.jsonl`
- `6` (results_FINAL.md:145, confidence interval) - **Filter:** For every (trial, turn) pair where turn in {1,2,3,4}, pull `level` from `evaluator_results.jsonl` (recode 6 -> 2). If level >= 4 ("sufficient"), check whether `genuine_meta_labels.jsonl`
- `2` (results_FINAL.md:145, confidence interval) - **Filter:** For every (trial, turn) pair where turn in {1,2,3,4}, pull `level` from `evaluator_results.jsonl` (recode 6 -> 2). If level >= 4 ("sufficient"), check whether `genuine_meta_labels.jsonl`
- `4` (results_FINAL.md:145, confidence interval) - **Filter:** For every (trial, turn) pair where turn in {1,2,3,4}, pull `level` from `evaluator_results.jsonl` (recode 6 -> 2). If level >= 4 ("sufficient"), check whether `genuine_meta_labels.jsonl`
- `1` (results_FINAL.md:145, confidence interval) - **Filter:** For every (trial, turn) pair where turn in {1,2,3,4}, pull `level` from `evaluator_results.jsonl` (recode 6 -> 2). If level >= 4 ("sufficient"), check whether `genuine_meta_labels.jsonl`
- `938` (results_FINAL.md:145, confidence interval) - **Filter:** For every (trial, turn) pair where turn in {1,2,3,4}, pull `level` from `evaluator_results.jsonl` (recode 6 -> 2). If level >= 4 ("sufficient"), check whether `genuine_meta_labels.jsonl`
- `1000` (results_FINAL.md:145, confidence interval) - **Filter:** For every (trial, turn) pair where turn in {1,2,3,4}, pull `level` from `evaluator_results.jsonl` (recode 6 -> 2). If level >= 4 ("sufficient"), check whether `genuine_meta_labels.jsonl`
- `42` (results_FINAL.md:145, confidence interval) - **Filter:** For every (trial, turn) pair where turn in {1,2,3,4}, pull `level` from `evaluator_results.jsonl` (recode 6 -> 2). If level >= 4 ("sufficient"), check whether `genuine_meta_labels.jsonl`
- `1` (results_FINAL.md:146, turn index) - **T1 sufficiency:** Count of trials where evaluator level at turn 1 >= 4 (after 6 -> 2 recode). 631/720 = 87.6%.
- `4` (results_FINAL.md:146, turn index) - **T1 sufficiency:** Count of trials where evaluator level at turn 1 >= 4 (after 6 -> 2 recode). 631/720 = 87.6%.
- `6` (results_FINAL.md:146, turn index) - **T1 sufficiency:** Count of trials where evaluator level at turn 1 >= 4 (after 6 -> 2 recode). 631/720 = 87.6%.
- `2` (results_FINAL.md:146, turn index) - **T1 sufficiency:** Count of trials where evaluator level at turn 1 >= 4 (after 6 -> 2 recode). 631/720 = 87.6%.
- `631` (results_FINAL.md:146, turn index) - **T1 sufficiency:** Count of trials where evaluator level at turn 1 >= 4 (after 6 -> 2 recode). 631/720 = 87.6%.
- `720` (results_FINAL.md:146, turn index) - **T1 sufficiency:** Count of trials where evaluator level at turn 1 >= 4 (after 6 -> 2 recode). 631/720 = 87.6%.
- `87.6` (results_FINAL.md:146, turn index) - **T1 sufficiency:** Count of trials where evaluator level at turn 1 >= 4 (after 6 -> 2 recode). 631/720 = 87.6%.

### [results_FINAL.md] 4b. DIRECTION OF REVISIONS (added 2026-09-03)

*- **Filter:** For every (trial, turn) pair where turn in {1,2,3,4}, pull `level` from `evaluator_results.jsonl` (recode 6 -> 2). If level >= 4 ("sufficient"), check whether `genuine_meta_labels.jsonl` has `classifier_label == "GENUINE"` at turn+1. Numerator = sufficient turns where next turn is GENU*

- `2026` (results_FINAL.md:151, bare number) ## 4b. DIRECTION OF REVISIONS (added 2026-09-03)
- `09` (results_FINAL.md:151, bare number) ## 4b. DIRECTION OF REVISIONS (added 2026-09-03)
- `03` (results_FINAL.md:151, bare number) ## 4b. DIRECTION OF REVISIONS (added 2026-09-03)
- `720` (results_FINAL.md:157, bare number) - **Sample:** unchanged. The same 720 trials and the same GENUINE/META labels from the
- `2` (results_FINAL.md:159, bare number) - **Filter (exact):** For each trial, walk turns 2-5. Where `genuine_meta_labels.jsonl`
- `5` (results_FINAL.md:159, bare number) - **Filter (exact):** For each trial, walk turns 2-5. Where `genuine_meta_labels.jsonl`
- `1` (results_FINAL.md:161, turn index) of the most recent turn whose content was genuinely new: turn 1, or the last turn
- `6` (results_FINAL.md:162, bare number) labelled GENUINE. Recode level 6 -> 2 first. Comparing against turn t-1 directly would
- `2` (results_FINAL.md:162, bare number) labelled GENUINE. Recode level 6 -> 2 first. Comparing against turn t-1 directly would
- `1` (results_FINAL.md:162, bare number) labelled GENUINE. Recode level 6 -> 2 first. Comparing against turn t-1 directly would
- `95` (results_FINAL.md:168, percentage) Clopper-Pearson exact 95% CI on the share worse among movers; chi-square on the

### [results_FINAL.md] 4b. DIRECTION OF REVISIONS (added 2026-09-03) -- Overall (n = 718 genuine revisions)

*- **Filter (exact):** For each trial, walk turns 2-5. Where `genuine_meta_labels.jsonl`*

- `718` (results_FINAL.md:172, count or denominator) ### Overall (n = 718 genuine revisions)
- `95` (results_FINAL.md:174, percentage) | Basis | worse | same | better | movers | % of movers worse | 95% CI | sign p |
- `199` (results_FINAL.md:176, percentage) | **Stripped** | 199 (27.7%) | 432 (60.2%) | 87 (12.1%) | 286 | **69.6%** | [63.9%, 74.9%] | 1.48e-11 |
- `27.7` (results_FINAL.md:176, percentage) | **Stripped** | 199 (27.7%) | 432 (60.2%) | 87 (12.1%) | 286 | **69.6%** | [63.9%, 74.9%] | 1.48e-11 |
- `432` (results_FINAL.md:176, percentage) | **Stripped** | 199 (27.7%) | 432 (60.2%) | 87 (12.1%) | 286 | **69.6%** | [63.9%, 74.9%] | 1.48e-11 |
- `60.2` (results_FINAL.md:176, percentage) | **Stripped** | 199 (27.7%) | 432 (60.2%) | 87 (12.1%) | 286 | **69.6%** | [63.9%, 74.9%] | 1.48e-11 |
- `87` (results_FINAL.md:176, percentage) | **Stripped** | 199 (27.7%) | 432 (60.2%) | 87 (12.1%) | 286 | **69.6%** | [63.9%, 74.9%] | 1.48e-11 |
- `12.1` (results_FINAL.md:176, percentage) | **Stripped** | 199 (27.7%) | 432 (60.2%) | 87 (12.1%) | 286 | **69.6%** | [63.9%, 74.9%] | 1.48e-11 |
- `286` (results_FINAL.md:176, percentage) | **Stripped** | 199 (27.7%) | 432 (60.2%) | 87 (12.1%) | 286 | **69.6%** | [63.9%, 74.9%] | 1.48e-11 |
- `69.6` (results_FINAL.md:176, percentage) | **Stripped** | 199 (27.7%) | 432 (60.2%) | 87 (12.1%) | 286 | **69.6%** | [63.9%, 74.9%] | 1.48e-11 |
- `63.9` (results_FINAL.md:176, percentage) | **Stripped** | 199 (27.7%) | 432 (60.2%) | 87 (12.1%) | 286 | **69.6%** | [63.9%, 74.9%] | 1.48e-11 |
- `74.9` (results_FINAL.md:176, percentage) | **Stripped** | 199 (27.7%) | 432 (60.2%) | 87 (12.1%) | 286 | **69.6%** | [63.9%, 74.9%] | 1.48e-11 |
- `1` (results_FINAL.md:176, percentage) | **Stripped** | 199 (27.7%) | 432 (60.2%) | 87 (12.1%) | 286 | **69.6%** | [63.9%, 74.9%] | 1.48e-11 |
- `11` (results_FINAL.md:176, percentage) | **Stripped** | 199 (27.7%) | 432 (60.2%) | 87 (12.1%) | 286 | **69.6%** | [63.9%, 74.9%] | 1.48e-11 |
- `245` (results_FINAL.md:177, percentage) | Unstripped | 245 (34.1%) | 398 (55.4%) | 75 (10.4%) | 320 | 76.6% | [71.5%, 81.1%] | 1.66e-22 |
- `34.1` (results_FINAL.md:177, percentage) | Unstripped | 245 (34.1%) | 398 (55.4%) | 75 (10.4%) | 320 | 76.6% | [71.5%, 81.1%] | 1.66e-22 |
- `398` (results_FINAL.md:177, percentage) | Unstripped | 245 (34.1%) | 398 (55.4%) | 75 (10.4%) | 320 | 76.6% | [71.5%, 81.1%] | 1.66e-22 |
- `55.4` (results_FINAL.md:177, percentage) | Unstripped | 245 (34.1%) | 398 (55.4%) | 75 (10.4%) | 320 | 76.6% | [71.5%, 81.1%] | 1.66e-22 |
- `75` (results_FINAL.md:177, percentage) | Unstripped | 245 (34.1%) | 398 (55.4%) | 75 (10.4%) | 320 | 76.6% | [71.5%, 81.1%] | 1.66e-22 |
- `10.4` (results_FINAL.md:177, percentage) | Unstripped | 245 (34.1%) | 398 (55.4%) | 75 (10.4%) | 320 | 76.6% | [71.5%, 81.1%] | 1.66e-22 |
- `320` (results_FINAL.md:177, percentage) | Unstripped | 245 (34.1%) | 398 (55.4%) | 75 (10.4%) | 320 | 76.6% | [71.5%, 81.1%] | 1.66e-22 |
- `76.6` (results_FINAL.md:177, percentage) | Unstripped | 245 (34.1%) | 398 (55.4%) | 75 (10.4%) | 320 | 76.6% | [71.5%, 81.1%] | 1.66e-22 |
- `71.5` (results_FINAL.md:177, percentage) | Unstripped | 245 (34.1%) | 398 (55.4%) | 75 (10.4%) | 320 | 76.6% | [71.5%, 81.1%] | 1.66e-22 |
- `81.1` (results_FINAL.md:177, percentage) | Unstripped | 245 (34.1%) | 398 (55.4%) | 75 (10.4%) | 320 | 76.6% | [71.5%, 81.1%] | 1.66e-22 |
- `1` (results_FINAL.md:177, percentage) | Unstripped | 245 (34.1%) | 398 (55.4%) | 75 (10.4%) | 320 | 76.6% | [71.5%, 81.1%] | 1.66e-22 |
- `22` (results_FINAL.md:177, percentage) | Unstripped | 245 (34.1%) | 398 (55.4%) | 75 (10.4%) | 320 | 76.6% | [71.5%, 81.1%] | 1.66e-22 |
- `60.2` (results_FINAL.md:179, percentage) Most revisions (60.2% stripped) do not move the level at all, which is partly the
- `2.3` (results_FINAL.md:181, mean or delta) asymmetric: down about 2.3 times as often as up.

### [results_FINAL.md] 4b. DIRECTION OF REVISIONS (added 2026-09-03) -- Per-model (stripped, primary)

*- **Filter (exact):** For each trial, walk turns 2-5. Where `genuine_meta_labels.jsonl`*

- `2.5` (results_FINAL.md:187, percentage) | gemini-2.5-flash | 8 | 50.0% | 50.0% | 0.0% | 100.0% | 0.062 |
- `8` (results_FINAL.md:187, percentage) | gemini-2.5-flash | 8 | 50.0% | 50.0% | 0.0% | 100.0% | 0.062 |
- `50.0` (results_FINAL.md:187, percentage) | gemini-2.5-flash | 8 | 50.0% | 50.0% | 0.0% | 100.0% | 0.062 |
- `50.0` (results_FINAL.md:187, percentage) | gemini-2.5-flash | 8 | 50.0% | 50.0% | 0.0% | 100.0% | 0.062 |
- `0.0` (results_FINAL.md:187, percentage) | gemini-2.5-flash | 8 | 50.0% | 50.0% | 0.0% | 100.0% | 0.062 |
- `100.0` (results_FINAL.md:187, percentage) | gemini-2.5-flash | 8 | 50.0% | 50.0% | 0.0% | 100.0% | 0.062 |
- `0.062` (results_FINAL.md:187, percentage) | gemini-2.5-flash | 8 | 50.0% | 50.0% | 0.0% | 100.0% | 0.062 |
- `31` (results_FINAL.md:188, percentage) | deepseek-v4 | 31 | 38.7% | 54.8% | 6.5% | 85.7% | 0.0065 |
- `38.7` (results_FINAL.md:188, percentage) | deepseek-v4 | 31 | 38.7% | 54.8% | 6.5% | 85.7% | 0.0065 |
- `54.8` (results_FINAL.md:188, percentage) | deepseek-v4 | 31 | 38.7% | 54.8% | 6.5% | 85.7% | 0.0065 |
- `6.5` (results_FINAL.md:188, percentage) | deepseek-v4 | 31 | 38.7% | 54.8% | 6.5% | 85.7% | 0.0065 |
- `85.7` (results_FINAL.md:188, percentage) | deepseek-v4 | 31 | 38.7% | 54.8% | 6.5% | 85.7% | 0.0065 |
- `0.0065` (results_FINAL.md:188, percentage) | deepseek-v4 | 31 | 38.7% | 54.8% | 6.5% | 85.7% | 0.0065 |
- `40` (results_FINAL.md:189, percentage) | gpt-4o | 40 | 40.0% | 50.0% | 10.0% | 80.0% | 0.0059 |
- `40.0` (results_FINAL.md:189, percentage) | gpt-4o | 40 | 40.0% | 50.0% | 10.0% | 80.0% | 0.0059 |
- `50.0` (results_FINAL.md:189, percentage) | gpt-4o | 40 | 40.0% | 50.0% | 10.0% | 80.0% | 0.0059 |
- `10.0` (results_FINAL.md:189, percentage) | gpt-4o | 40 | 40.0% | 50.0% | 10.0% | 80.0% | 0.0059 |
- `80.0` (results_FINAL.md:189, percentage) | gpt-4o | 40 | 40.0% | 50.0% | 10.0% | 80.0% | 0.0059 |
- `0.0059` (results_FINAL.md:189, percentage) | gpt-4o | 40 | 40.0% | 50.0% | 10.0% | 80.0% | 0.0059 |
- `3` (results_FINAL.md:190, percentage) | qwen-3-235b | 90 | 42.2% | 43.3% | 14.4% | 74.5% | 0.00031 |
- `90` (results_FINAL.md:190, percentage) | qwen-3-235b | 90 | 42.2% | 43.3% | 14.4% | 74.5% | 0.00031 |
- `42.2` (results_FINAL.md:190, percentage) | qwen-3-235b | 90 | 42.2% | 43.3% | 14.4% | 74.5% | 0.00031 |
- `43.3` (results_FINAL.md:190, percentage) | qwen-3-235b | 90 | 42.2% | 43.3% | 14.4% | 74.5% | 0.00031 |
- `14.4` (results_FINAL.md:190, percentage) | qwen-3-235b | 90 | 42.2% | 43.3% | 14.4% | 74.5% | 0.00031 |
- `74.5` (results_FINAL.md:190, percentage) | qwen-3-235b | 90 | 42.2% | 43.3% | 14.4% | 74.5% | 0.00031 |
- `0.00031` (results_FINAL.md:190, percentage) | qwen-3-235b | 90 | 42.2% | 43.3% | 14.4% | 74.5% | 0.00031 |
- `3.3` (results_FINAL.md:191, percentage) | llama-3.3-70b | 353 | 25.8% | 62.6% | 11.6% | 68.9% | 8.0e-06 |
- `353` (results_FINAL.md:191, percentage) | llama-3.3-70b | 353 | 25.8% | 62.6% | 11.6% | 68.9% | 8.0e-06 |
- `25.8` (results_FINAL.md:191, percentage) | llama-3.3-70b | 353 | 25.8% | 62.6% | 11.6% | 68.9% | 8.0e-06 |
- `62.6` (results_FINAL.md:191, percentage) | llama-3.3-70b | 353 | 25.8% | 62.6% | 11.6% | 68.9% | 8.0e-06 |
- `11.6` (results_FINAL.md:191, percentage) | llama-3.3-70b | 353 | 25.8% | 62.6% | 11.6% | 68.9% | 8.0e-06 |
- `68.9` (results_FINAL.md:191, percentage) | llama-3.3-70b | 353 | 25.8% | 62.6% | 11.6% | 68.9% | 8.0e-06 |
- `8` (results_FINAL.md:191, percentage) | llama-3.3-70b | 353 | 25.8% | 62.6% | 11.6% | 68.9% | 8.0e-06 |
- `06` (results_FINAL.md:191, percentage) | llama-3.3-70b | 353 | 25.8% | 62.6% | 11.6% | 68.9% | 8.0e-06 |
- `4` (results_FINAL.md:192, percentage) | claude-sonnet-4 | 196 | 19.4% | 66.8% | 13.8% | 58.5% | 0.11 |
- `196` (results_FINAL.md:192, percentage) | claude-sonnet-4 | 196 | 19.4% | 66.8% | 13.8% | 58.5% | 0.11 |
- `19.4` (results_FINAL.md:192, percentage) | claude-sonnet-4 | 196 | 19.4% | 66.8% | 13.8% | 58.5% | 0.11 |
- `66.8` (results_FINAL.md:192, percentage) | claude-sonnet-4 | 196 | 19.4% | 66.8% | 13.8% | 58.5% | 0.11 |
- `13.8` (results_FINAL.md:192, percentage) | claude-sonnet-4 | 196 | 19.4% | 66.8% | 13.8% | 58.5% | 0.11 |
- `58.5` (results_FINAL.md:192, percentage) | claude-sonnet-4 | 196 | 19.4% | 66.8% | 13.8% | 58.5% | 0.11 |
- `0.11` (results_FINAL.md:192, percentage) | claude-sonnet-4 | 196 | 19.4% | 66.8% | 13.8% | 58.5% | 0.11 |
- `4` (results_FINAL.md:195, p-value) individually significant in only four. Claude Sonnet 4 is not significant (p = 0.11)
- `0.11` (results_FINAL.md:195, p-value) individually significant in only four. Claude Sonnet 4 is not significant (p = 0.11)
- `8` (results_FINAL.md:196, bare number) and Gemini has only 8 genuine revisions. The correct claim is that the direction holds
- `0.062` (results_FINAL.md:198, p-value) significantly. Unstripped, five of six reach significance (Gemini p = 0.062).

### [results_FINAL.md] 4b. DIRECTION OF REVISIONS (added 2026-09-03) -- Per-domain (stripped, primary)

*- **Filter (exact):** For each trial, walk turns 2-5. Where `genuine_meta_labels.jsonl`*

- `118` (results_FINAL.md:204, percentage) | writing | 118 | 28.8% | 63.6% | 7.6% | 79.1% | 8.5e-05 |
- `28.8` (results_FINAL.md:204, percentage) | writing | 118 | 28.8% | 63.6% | 7.6% | 79.1% | 8.5e-05 |
- `63.6` (results_FINAL.md:204, percentage) | writing | 118 | 28.8% | 63.6% | 7.6% | 79.1% | 8.5e-05 |
- `7.6` (results_FINAL.md:204, percentage) | writing | 118 | 28.8% | 63.6% | 7.6% | 79.1% | 8.5e-05 |
- `79.1` (results_FINAL.md:204, percentage) | writing | 118 | 28.8% | 63.6% | 7.6% | 79.1% | 8.5e-05 |
- `8` (results_FINAL.md:204, percentage) | writing | 118 | 28.8% | 63.6% | 7.6% | 79.1% | 8.5e-05 |
- `05` (results_FINAL.md:204, percentage) | writing | 118 | 28.8% | 63.6% | 7.6% | 79.1% | 8.5e-05 |
- `145` (results_FINAL.md:205, percentage) | creative | 145 | 26.2% | 64.1% | 9.7% | 73.1% | 0.0006 |
- `26.2` (results_FINAL.md:205, percentage) | creative | 145 | 26.2% | 64.1% | 9.7% | 73.1% | 0.0006 |
- `64.1` (results_FINAL.md:205, percentage) | creative | 145 | 26.2% | 64.1% | 9.7% | 73.1% | 0.0006 |
- `9.7` (results_FINAL.md:205, percentage) | creative | 145 | 26.2% | 64.1% | 9.7% | 73.1% | 0.0006 |
- `73.1` (results_FINAL.md:205, percentage) | creative | 145 | 26.2% | 64.1% | 9.7% | 73.1% | 0.0006 |
- `0.0006` (results_FINAL.md:205, percentage) | creative | 145 | 26.2% | 64.1% | 9.7% | 73.1% | 0.0006 |
- `196` (results_FINAL.md:206, percentage) | code | 196 | 35.2% | 47.4% | 17.3% | 67.0% | 0.00036 |
- `35.2` (results_FINAL.md:206, percentage) | code | 196 | 35.2% | 47.4% | 17.3% | 67.0% | 0.00036 |
- `47.4` (results_FINAL.md:206, percentage) | code | 196 | 35.2% | 47.4% | 17.3% | 67.0% | 0.00036 |
- `17.3` (results_FINAL.md:206, percentage) | code | 196 | 35.2% | 47.4% | 17.3% | 67.0% | 0.00036 |
- `67.0` (results_FINAL.md:206, percentage) | code | 196 | 35.2% | 47.4% | 17.3% | 67.0% | 0.00036 |
- `0.00036` (results_FINAL.md:206, percentage) | code | 196 | 35.2% | 47.4% | 17.3% | 67.0% | 0.00036 |
- `125` (results_FINAL.md:207, percentage) | analysis | 125 | 23.2% | 64.8% | 12.0% | 65.9% | 0.024 |
- `23.2` (results_FINAL.md:207, percentage) | analysis | 125 | 23.2% | 64.8% | 12.0% | 65.9% | 0.024 |
- `64.8` (results_FINAL.md:207, percentage) | analysis | 125 | 23.2% | 64.8% | 12.0% | 65.9% | 0.024 |
- `12.0` (results_FINAL.md:207, percentage) | analysis | 125 | 23.2% | 64.8% | 12.0% | 65.9% | 0.024 |
- `65.9` (results_FINAL.md:207, percentage) | analysis | 125 | 23.2% | 64.8% | 12.0% | 65.9% | 0.024 |
- `0.024` (results_FINAL.md:207, percentage) | analysis | 125 | 23.2% | 64.8% | 12.0% | 65.9% | 0.024 |
- `134` (results_FINAL.md:208, percentage) | data_logic | 134 | 21.6% | 67.2% | 11.2% | 65.9% | 0.024 |
- `21.6` (results_FINAL.md:208, percentage) | data_logic | 134 | 21.6% | 67.2% | 11.2% | 65.9% | 0.024 |
- `67.2` (results_FINAL.md:208, percentage) | data_logic | 134 | 21.6% | 67.2% | 11.2% | 65.9% | 0.024 |
- `11.2` (results_FINAL.md:208, percentage) | data_logic | 134 | 21.6% | 67.2% | 11.2% | 65.9% | 0.024 |
- `65.9` (results_FINAL.md:208, percentage) | data_logic | 134 | 21.6% | 67.2% | 11.2% | 65.9% | 0.024 |
- `0.024` (results_FINAL.md:208, percentage) | data_logic | 134 | 21.6% | 67.2% | 11.2% | 65.9% | 0.024 |
- `3.02` (results_FINAL.md:211, p-value) **chi2 = 3.02, dof = 4, p = 0.555.** The asymmetry does not differ by domain.
- `4` (results_FINAL.md:211, p-value) **chi2 = 3.02, dof = 4, p = 0.555.** The asymmetry does not differ by domain.
- `0.555` (results_FINAL.md:211, p-value) **chi2 = 3.02, dof = 4, p = 0.555.** The asymmetry does not differ by domain.

### [results_FINAL.md] 4b. DIRECTION OF REVISIONS (added 2026-09-03) -- The objectivity gradient is a meta-commentary artifact

*- **Filter (exact):** For each trial, walk turns 2-5. Where `genuine_meta_labels.jsonl`*

- `98` (results_FINAL.md:217, percentage) | **Stripped** | 98 / 49 = 66.7% worse | 72 / 23 = 75.8% worse | **0.151** |
- `49` (results_FINAL.md:217, percentage) | **Stripped** | 98 / 49 = 66.7% worse | 72 / 23 = 75.8% worse | **0.151** |
- `66.7` (results_FINAL.md:217, percentage) | **Stripped** | 98 / 49 = 66.7% worse | 72 / 23 = 75.8% worse | **0.151** |
- `72` (results_FINAL.md:217, percentage) | **Stripped** | 98 / 49 = 66.7% worse | 72 / 23 = 75.8% worse | **0.151** |
- `23` (results_FINAL.md:217, percentage) | **Stripped** | 98 / 49 = 66.7% worse | 72 / 23 = 75.8% worse | **0.151** |
- `75.8` (results_FINAL.md:217, percentage) | **Stripped** | 98 / 49 = 66.7% worse | 72 / 23 = 75.8% worse | **0.151** |
- `0.151` (results_FINAL.md:217, percentage) | **Stripped** | 98 / 49 = 66.7% worse | 72 / 23 = 75.8% worse | **0.151** |
- `109` (results_FINAL.md:218, percentage) | Unstripped | 109 / 44 = 71.2% worse | 94 / 18 = 83.9% worse | **0.019** |
- `44` (results_FINAL.md:218, percentage) | Unstripped | 109 / 44 = 71.2% worse | 94 / 18 = 83.9% worse | **0.019** |
- `71.2` (results_FINAL.md:218, percentage) | Unstripped | 109 / 44 = 71.2% worse | 94 / 18 = 83.9% worse | **0.019** |
- `94` (results_FINAL.md:218, percentage) | Unstripped | 109 / 44 = 71.2% worse | 94 / 18 = 83.9% worse | **0.019** |
- `18` (results_FINAL.md:218, percentage) | Unstripped | 109 / 44 = 71.2% worse | 94 / 18 = 83.9% worse | **0.019** |
- `83.9` (results_FINAL.md:218, percentage) | Unstripped | 109 / 44 = 71.2% worse | 94 / 18 = 83.9% worse | **0.019** |
- `0.019` (results_FINAL.md:218, percentage) | Unstripped | 109 / 44 = 71.2% worse | 94 / 18 = 83.9% worse | **0.019** |
- `0.205` (results_FINAL.md:220, p-value) Unstripped domain chi-square p = 0.205; stripped p = 0.555.
- `0.555` (results_FINAL.md:220, p-value) Unstripped domain chi-square p = 0.205; stripped p = 0.555.
- `117` (results_FINAL.md:222, bare number) **BEARS ON A REGISTERED PREDICTION.** `experiment/study3_revision_yield_design.md` line 117
- `0.019` (results_FINAL.md:225, p-value) scores (p = 0.019) and **is not supported once meta-commentary is stripped** (p = 0.151).
- `0.151` (results_FINAL.md:225, p-value) scores (p = 0.019) and **is not supported once meta-commentary is stripped** (p = 0.151).
- `65` (results_FINAL.md:230, percentage) the 65% reversibility bar in Section 7.
- `7` (results_FINAL.md:230, percentage) the 65% reversibility bar in Section 7.

### [results_FINAL.md] 4b. DIRECTION OF REVISIONS (added 2026-09-03) -- Outcome when the input was already sufficient (added 2026-09-07)

*- **Filter (exact):** For each trial, walk turns 2-5. Where `genuine_meta_labels.jsonl`*

- `2026` (results_FINAL.md:232, bare number) ### Outcome when the input was already sufficient (added 2026-09-07)
- `09` (results_FINAL.md:232, bare number) ### Outcome when the input was already sufficient (added 2026-09-07)
- `07` (results_FINAL.md:232, bare number) ### Outcome when the input was already sufficient (added 2026-09-07)
- `4` (results_FINAL.md:234, bare number) Of the genuine revisions whose baseline content was already at level 4 or above, how many
- `4` (results_FINAL.md:235, bare number) end below level 4?
- `411` (results_FINAL.md:239, percentage) | **Stripped** | 411 | 298 (72.5%) | **113 (27.5%)** |
- `298` (results_FINAL.md:239, percentage) | **Stripped** | 411 | 298 (72.5%) | **113 (27.5%)** |
- `72.5` (results_FINAL.md:239, percentage) | **Stripped** | 411 | 298 (72.5%) | **113 (27.5%)** |
- `113` (results_FINAL.md:239, percentage) | **Stripped** | 411 | 298 (72.5%) | **113 (27.5%)** |
- `27.5` (results_FINAL.md:239, percentage) | **Stripped** | 411 | 298 (72.5%) | **113 (27.5%)** |
- `113` (results_FINAL.md:241, bare number) Of the 113 that fall below, 85 land at level 2 and 28 at level 3.
- `85` (results_FINAL.md:241, bare number) Of the 113 that fall below, 85 land at level 2 and 28 at level 3.
- `2` (results_FINAL.md:241, bare number) Of the 113 that fall below, 85 land at level 2 and 28 at level 3.
- `28` (results_FINAL.md:241, bare number) Of the 113 that fall below, 85 land at level 2 and 28 at level 3.
- `3` (results_FINAL.md:241, bare number) Of the 113 that fall below, 85 land at level 2 and 28 at level 3.
- `718` (results_FINAL.md:243, bare number) - **Filter:** the same 718 genuine revisions as above. Keep those whose baseline (the most
- `4` (results_FINAL.md:244, bare number) recent turn with genuinely new content) is at level >= 4 after the 6 -> 2 recode. Count how
- `6` (results_FINAL.md:244, bare number) recent turn with genuinely new content) is at level >= 4 after the 6 -> 2 recode. Count how
- `2` (results_FINAL.md:244, bare number) recent turn with genuinely new content) is at level >= 4 after the 6 -> 2 recode. Count how
- `4` (results_FINAL.md:245, bare number) many have a level < 4 at the revision turn.
- `411` (results_FINAL.md:246, count or denominator) - **This is the same set of 411 as Stripped Sensitivity M1** ("Revised despite sufficient",
- `411` (results_FINAL.md:247, percentage) 411 of 1,038 sufficient turns, 39.6%). Verified 2026-09-07: the two constructions produce
- `1,038` (results_FINAL.md:247, percentage) 411 of 1,038 sufficient turns, 39.6%). Verified 2026-09-07: the two constructions produce
- `39.6` (results_FINAL.md:247, percentage) 411 of 1,038 sufficient turns, 39.6%). Verified 2026-09-07: the two constructions produce
- `2026` (results_FINAL.md:247, percentage) 411 of 1,038 sufficient turns, 39.6%). Verified 2026-09-07: the two constructions produce
- `09` (results_FINAL.md:247, percentage) 411 of 1,038 sufficient turns, 39.6%). Verified 2026-09-07: the two constructions produce
- `07` (results_FINAL.md:247, percentage) 411 of 1,038 sufficient turns, 39.6%). Verified 2026-09-07: the two constructions produce
- `411` (results_FINAL.md:248, count or denominator) identical sets, 411 of 411, zero on either side. They coincide because a meta-response
- `411` (results_FINAL.md:248, count or denominator) identical sets, 411 of 411, zero on either side. They coincide because a meta-response
- `1.06` (results_FINAL.md:249, mean or delta) strips to near-empty text and scores about 1.06, so it can never be a sufficient baseline.

### [results_FINAL.md] 4b. DIRECTION OF REVISIONS (added 2026-09-03) -- Magnitude of the change (added 2026-09-07)

*- **Filter:** the same 718 genuine revisions as above. Keep those whose baseline (the most*

- `2026` (results_FINAL.md:252, bare number) ### Magnitude of the change (added 2026-09-07)
- `09` (results_FINAL.md:252, bare number) ### Magnitude of the change (added 2026-09-07)
- `07` (results_FINAL.md:252, bare number) ### Magnitude of the change (added 2026-09-07)
- `0.30` (results_FINAL.md:256, mean or delta) | **Stripped** | **-0.30** | **-1.72** | -2 | +1.45 |
- `1.72` (results_FINAL.md:256, mean or delta) | **Stripped** | **-0.30** | **-1.72** | -2 | +1.45 |
- `2` (results_FINAL.md:256, mean or delta) | **Stripped** | **-0.30** | **-1.72** | -2 | +1.45 |
- `1.45` (results_FINAL.md:256, mean or delta) | **Stripped** | **-0.30** | **-1.72** | -2 | +1.45 |
- `0.51` (results_FINAL.md:257, mean or delta) | Unstripped | -0.51 | -1.90 | -2 | +1.32 |
- `1.90` (results_FINAL.md:257, mean or delta) | Unstripped | -0.51 | -1.90 | -2 | +1.32 |
- `2` (results_FINAL.md:257, mean or delta) | Unstripped | -0.51 | -1.90 | -2 | +1.32 |
- `1.32` (results_FINAL.md:257, mean or delta) | Unstripped | -0.51 | -1.90 | -2 | +1.32 |
- `87` (results_FINAL.md:259, bare number) Stripped, 87 of the 199 downward moves fall one level and 112 fall two or more. Drops are both
- `199` (results_FINAL.md:259, bare number) Stripped, 87 of the 199 downward moves fall one level and 112 fall two or more. Drops are both
- `112` (results_FINAL.md:259, bare number) Stripped, 87 of the 199 downward moves fall one level and 112 fall two or more. Drops are both

### [results_FINAL.md] 4b. DIRECTION OF REVISIONS (added 2026-09-03) -- Trial-level, balanced panel (Turn 1 vs Turn 5, n = 50)

*- **Filter:** signed difference in recoded level between each genuine revision and its baseline,*

- `1` (results_FINAL.md:265, count or denominator) ### Trial-level, balanced panel (Turn 1 vs Turn 5, n = 50)
- `5` (results_FINAL.md:265, count or denominator) ### Trial-level, balanced panel (Turn 1 vs Turn 5, n = 50)
- `50` (results_FINAL.md:265, count or denominator) ### Trial-level, balanced panel (Turn 1 vs Turn 5, n = 50)
- `52.0` (results_FINAL.md:269, percentage) | **Stripped** | 52.0% | 38.0% | 10.0% | 26 / 5 | 9.61e-05 |
- `38.0` (results_FINAL.md:269, percentage) | **Stripped** | 52.0% | 38.0% | 10.0% | 26 / 5 | 9.61e-05 |
- `10.0` (results_FINAL.md:269, percentage) | **Stripped** | 52.0% | 38.0% | 10.0% | 26 / 5 | 9.61e-05 |
- `26` (results_FINAL.md:269, percentage) | **Stripped** | 52.0% | 38.0% | 10.0% | 26 / 5 | 9.61e-05 |
- `5` (results_FINAL.md:269, percentage) | **Stripped** | 52.0% | 38.0% | 10.0% | 26 / 5 | 9.61e-05 |
- `9` (results_FINAL.md:269, percentage) | **Stripped** | 52.0% | 38.0% | 10.0% | 26 / 5 | 9.61e-05 |
- `05` (results_FINAL.md:269, percentage) | **Stripped** | 52.0% | 38.0% | 10.0% | 26 / 5 | 9.61e-05 |
- `62.0` (results_FINAL.md:270, percentage) | Unstripped | 62.0% | 30.0% | 8.0% | 31 / 4 | 1.73e-06 |
- `30.0` (results_FINAL.md:270, percentage) | Unstripped | 62.0% | 30.0% | 8.0% | 31 / 4 | 1.73e-06 |
- `8.0` (results_FINAL.md:270, percentage) | Unstripped | 62.0% | 30.0% | 8.0% | 31 / 4 | 1.73e-06 |
- `31` (results_FINAL.md:270, percentage) | Unstripped | 62.0% | 30.0% | 8.0% | 31 / 4 | 1.73e-06 |
- `4` (results_FINAL.md:270, percentage) | Unstripped | 62.0% | 30.0% | 8.0% | 31 / 4 | 1.73e-06 |
- `1` (results_FINAL.md:270, percentage) | Unstripped | 62.0% | 30.0% | 8.0% | 31 / 4 | 1.73e-06 |
- `06` (results_FINAL.md:270, percentage) | Unstripped | 62.0% | 30.0% | 8.0% | 31 / 4 | 1.73e-06 |

### [results_FINAL.md] 4b. DIRECTION OF REVISIONS (added 2026-09-03) -- Why this estimator is preferred to the balanced-panel cliff

*- **Filter:** signed difference in recoded level between each genuine revision and its baseline,*

- `2` (results_FINAL.md:274, bare number) The cliff in Section 2 rests on 50 trials, 45 of them Llama, with three of six models
- `50` (results_FINAL.md:274, bare number) The cliff in Section 2 rests on 50 trials, 45 of them Llama, with three of six models
- `45` (results_FINAL.md:274, bare number) The cliff in Section 2 rests on 50 trials, 45 of them Llama, with three of six models
- `718` (results_FINAL.md:275, bare number) contributing zero trials. This analysis uses all 718 genuine revisions across all six
- `2026` (results_FINAL.md:277, count or denominator) data. It is the basis for the paper's headline claim as of 2026-09-03.
- `09` (results_FINAL.md:277, count or denominator) data. It is the basis for the paper's headline claim as of 2026-09-03.
- `03` (results_FINAL.md:277, count or denominator) data. It is the basis for the paper's headline claim as of 2026-09-03.

### [results_FINAL.md] 4c. EXPECTED CHANGE BY INPUT LEVEL (added 2026-09-14)

*- **Filter:** signed difference in recoded level between each genuine revision and its baseline,*

- `2026` (results_FINAL.md:281, bare number) ## 4c. EXPECTED CHANGE BY INPUT LEVEL (added 2026-09-14)
- `09` (results_FINAL.md:281, bare number) ## 4c. EXPECTED CHANGE BY INPUT LEVEL (added 2026-09-14)
- `14` (results_FINAL.md:281, bare number) ## 4c. EXPECTED CHANGE BY INPUT LEVEL (added 2026-09-14)
- `2026` (results_FINAL.md:283, bare number) **POST-HOC. Not among the registered predictions.** Computed 2026-09-14 while preparing
- `09` (results_FINAL.md:283, bare number) **POST-HOC. Not among the registered predictions.** Computed 2026-09-14 while preparing
- `14` (results_FINAL.md:283, bare number) **POST-HOC. Not among the registered predictions.** Computed 2026-09-14 while preparing
- `2` (results_FINAL.md:292, mean or delta) | 2 | 116 | +0.69 | 0.00 | 0.35 |
- `116` (results_FINAL.md:292, mean or delta) | 2 | 116 | +0.69 | 0.00 | 0.35 |
- `0.69` (results_FINAL.md:292, mean or delta) | 2 | 116 | +0.69 | 0.00 | 0.35 |
- `0.00` (results_FINAL.md:292, mean or delta) | 2 | 116 | +0.69 | 0.00 | 0.35 |
- `0.35` (results_FINAL.md:292, mean or delta) | 2 | 116 | +0.69 | 0.00 | 0.35 |
- `3` (results_FINAL.md:293, mean or delta) | 3 | 77 | -0.03 | 0.30 | 0.27 |
- `77` (results_FINAL.md:293, mean or delta) | 3 | 77 | -0.03 | 0.30 | 0.27 |
- `0.03` (results_FINAL.md:293, mean or delta) | 3 | 77 | -0.03 | 0.30 | 0.27 |
- `0.30` (results_FINAL.md:293, mean or delta) | 3 | 77 | -0.03 | 0.30 | 0.27 |
- `0.27` (results_FINAL.md:293, mean or delta) | 3 | 77 | -0.03 | 0.30 | 0.27 |
- `4` (results_FINAL.md:294, mean or delta) | 4 | 394 | -0.43 | 0.28 | 0.06 |
- `394` (results_FINAL.md:294, mean or delta) | 4 | 394 | -0.43 | 0.28 | 0.06 |
- `0.43` (results_FINAL.md:294, mean or delta) | 4 | 394 | -0.43 | 0.28 | 0.06 |
- `0.28` (results_FINAL.md:294, mean or delta) | 4 | 394 | -0.43 | 0.28 | 0.06 |
- `0.06` (results_FINAL.md:294, mean or delta) | 4 | 394 | -0.43 | 0.28 | 0.06 |
- `5` (results_FINAL.md:295, mean or delta) | 5 | 130 | -0.98 | 0.49 | 0.00 |
- `130` (results_FINAL.md:295, mean or delta) | 5 | 130 | -0.98 | 0.49 | 0.00 |
- `0.98` (results_FINAL.md:295, mean or delta) | 5 | 130 | -0.98 | 0.49 | 0.00 |
- `0.49` (results_FINAL.md:295, mean or delta) | 5 | 130 | -0.98 | 0.49 | 0.00 |
- `0.00` (results_FINAL.md:295, mean or delta) | 5 | 130 | -0.98 | 0.49 | 0.00 |
- `4` (results_FINAL.md:296, mean or delta) | **input insufficient (< 4)** | 194 | **+0.41** | | |
- `194` (results_FINAL.md:296, mean or delta) | **input insufficient (< 4)** | 194 | **+0.41** | | |
- `0.41` (results_FINAL.md:296, mean or delta) | **input insufficient (< 4)** | 194 | **+0.41** | | |
- `4` (results_FINAL.md:297, mean or delta) | **input sufficient (>= 4)** | 524 | **-0.56** | | |
- `524` (results_FINAL.md:297, mean or delta) | **input sufficient (>= 4)** | 524 | **-0.56** | | |
- `0.56` (results_FINAL.md:297, mean or delta) | **input sufficient (>= 4)** | 524 | **-0.56** | | |
- `1` (results_FINAL.md:299, count or denominator) Level 1 has n = 1 and is omitted from the figure.
- `1` (results_FINAL.md:299, count or denominator) Level 1 has n = 1 and is omitted from the figure.
- `718` (results_FINAL.md:301, bare number) - **Filter:** the same 718 genuine revisions as Section 4b. For each trial, walk turns 2-5;
- `2` (results_FINAL.md:301, bare number) - **Filter:** the same 718 genuine revisions as Section 4b. For each trial, walk turns 2-5;
- `5` (results_FINAL.md:301, bare number) - **Filter:** the same 718 genuine revisions as Section 4b. For each trial, walk turns 2-5;
- `1` (results_FINAL.md:304, bare number) Turn 1 stripped score. 6 -> 2 recode applied throughout.
- `6` (results_FINAL.md:304, bare number) Turn 1 stripped score. 6 -> 2 recode applied throughout.
- `2` (results_FINAL.md:304, bare number) Turn 1 stripped score. 6 -> 2 recode applied throughout.
- `11` (results_FINAL.md:308, bare number) The reliability figures in Section 11 apply.

### [results_FINAL.md] 4c. EXPECTED CHANGE BY INPUT LEVEL (added 2026-09-14) -- 4d. Why the mean-reversion reading was withdrawn (POST-HOC, added 2026-09-20)

*- **Filter:** the same 718 genuine revisions as Section 4b. For each trial, walk turns 2-5;*

- `2026` (results_FINAL.md:314, bare number) ### 4d. Why the mean-reversion reading was withdrawn (POST-HOC, added 2026-09-20)
- `09` (results_FINAL.md:314, bare number) ### 4d. Why the mean-reversion reading was withdrawn (POST-HOC, added 2026-09-20)
- `20` (results_FINAL.md:314, bare number) ### 4d. Why the mean-reversion reading was withdrawn (POST-HOC, added 2026-09-20)
- `2026` (results_FINAL.md:316, bare number) **Post-hoc.** Proposed and run by the assistant on 2026-09-20 during a final verification pass,
- `09` (results_FINAL.md:316, bare number) **Post-hoc.** Proposed and run by the assistant on 2026-09-20 during a final verification pass,
- `20` (results_FINAL.md:316, bare number) **Post-hoc.** Proposed and run by the assistant on 2026-09-20 during a final verification pass,
- `0.41` (results_FINAL.md:320, count or denominator) sufficiency threshold (+0.41, n = 194) and lowers it on sufficient input (-0.56, n = 524). The
- `194` (results_FINAL.md:320, count or denominator) sufficiency threshold (+0.41, n = 194) and lowers it on sufficient input (-0.56, n = 524). The
- `0.56` (results_FINAL.md:320, count or denominator) sufficiency threshold (+0.41, n = 194) and lowers it on sufficient input (-0.56, n = 524). The
- `524` (results_FINAL.md:320, count or denominator) sufficiency threshold (+0.41, n = 194) and lowers it on sufficient input (-0.56, n = 524). The
- `1` (results_FINAL.md:325, bare number) scenario) cell contains three independent Turn-1 drafts of the same prompt, generated at
- `1.0` (results_FINAL.md:326, mean or delta) temperature 1.0 with no revision anywhere in the procedure. Treating one draft as the "input"
- `2` (results_FINAL.md:332, mean or delta) | 2 | +1.333 | 96 |
- `1.333` (results_FINAL.md:332, mean or delta) | 2 | +1.333 | 96 |
- `96` (results_FINAL.md:332, mean or delta) | 2 | +1.333 | 96 |
- `3` (results_FINAL.md:333, mean or delta) | 3 | +0.537 | 80 |
- `0.537` (results_FINAL.md:333, mean or delta) | 3 | +0.537 | 80 |
- `80` (results_FINAL.md:333, mean or delta) | 3 | +0.537 | 80 |
- `4` (results_FINAL.md:334, mean or delta) | 4 | -0.058 | 824 |
- `0.058` (results_FINAL.md:334, mean or delta) | 4 | -0.058 | 824 |
- `824` (results_FINAL.md:334, mean or delta) | 4 | -0.058 | 824 |
- `5` (results_FINAL.md:335, mean or delta) | 5 | -0.290 | 438 |
- `0.290` (results_FINAL.md:335, mean or delta) | 5 | -0.290 | 438 |
- `438` (results_FINAL.md:335, mean or delta) | 5 | -0.290 | 438 |
- `0.983` (results_FINAL.md:339, mean or delta) | insufficient input | **+0.983** | +0.407 |
- `0.407` (results_FINAL.md:339, mean or delta) | insufficient input | **+0.983** | +0.407 |
- `0.139` (results_FINAL.md:340, mean or delta) | sufficient input | **-0.139** | -0.565 |
- `0.565` (results_FINAL.md:340, mean or delta) | sufficient input | **-0.139** | -0.565 |
- `720` (results_FINAL.md:342, bare number) - **Filter (exact):** all 720 Turn-1 stripped scores from `stripped_rescore_full.jsonl`, 6 -> 2
- `1` (results_FINAL.md:342, bare number) - **Filter (exact):** all 720 Turn-1 stripped scores from `stripped_rescore_full.jsonl`, 6 -> 2
- `6` (results_FINAL.md:342, bare number) - **Filter (exact):** all 720 Turn-1 stripped scores from `stripped_rescore_full.jsonl`, 6 -> 2
- `2` (results_FINAL.md:342, bare number) - **Filter (exact):** all 720 Turn-1 stripped scores from `stripped_rescore_full.jsonl`, 6 -> 2
- `240` (results_FINAL.md:343, count or denominator) recode, grouped into the 240 (model, scenario) cells of 3 runs each; all ordered pairs within
- `3` (results_FINAL.md:343, count or denominator) recode, grouped into the 240 (model, scenario) cells of 3 runs each; all ordered pairs within
- `0.565` (results_FINAL.md:345, mean or delta) - **What survives.** On sufficient input, revision costs -0.565 against a placebo of -0.139, so
- `0.139` (results_FINAL.md:345, mean or delta) - **What survives.** On sufficient input, revision costs -0.565 against a placebo of -0.139, so
- `0.407` (results_FINAL.md:348, mean or delta) - **What does not.** On insufficient input, revision gains +0.407 while simply redrawing the
- `0.983` (results_FINAL.md:349, mean or delta) first draft gains +0.983. Revising below-threshold work does *less* than generating it again.
- `4.2` (results_FINAL.md:351, mean or delta) been removed from both the abstract and Section 4.2. The underlying measurements stay.
- `1.0` (results_FINAL.md:352, mean or delta) - **Caveat on the benchmark.** The placebo mixes judge measurement error with temperature-1.0

### [results_FINAL.md] 5. TARGETED FEEDBACK

*- **Filter (exact):** all 720 Turn-1 stripped scores from `stripped_rescore_full.jsonl`, 6 -> 2*

- `5` (results_FINAL.md:359, bare number) ## 5. TARGETED FEEDBACK
- `177` (results_FINAL.md:363, bare number) | N | 177 |
- `4.68` (results_FINAL.md:364, mean or delta) | Targeted mean | 4.68 |
- `4.43` (results_FINAL.md:365, mean or delta) | Generic mean | 4.43 |
- `0.25` (results_FINAL.md:366, mean or delta) | Delta | **+0.25** |
- `3` (results_FINAL.md:367, reliability or effect size) | Wilcoxon p | 3.75e-03 |
- `03` (results_FINAL.md:367, reliability or effect size) | Wilcoxon p | 3.75e-03 |
- `1,047` (results_FINAL.md:369, bare number) - **Filter (exact):** Load all 1,047 records from `targeted_feedback_results.jsonl`. Each record has fields `targeted_level`, `generic_next_level`, `worker_trial_id`, `turn`. For each record:
- `1` (results_FINAL.md:370, bare number) 1. Require `targeted_level` and `generic_next_level` both non-null.
- `2` (results_FINAL.md:371, bare number) 2. Compute `next_turn = turn + 1`. If next_turn > 5, exclude.
- `1` (results_FINAL.md:371, bare number) 2. Compute `next_turn = turn + 1`. If next_turn > 5, exclude.
- `5` (results_FINAL.md:371, bare number) 2. Compute `next_turn = turn + 1`. If next_turn > 5, exclude.
- `3` (results_FINAL.md:372, bare number) 3. Look up `(worker_trial_id, next_turn)` in `genuine_meta_labels.jsonl`. If `classifier_label != "GENUINE"`, exclude (the generic next-turn output was a decline, not a revision).
- `4` (results_FINAL.md:373, bare number) 4. Recode: if `targeted_level == 6`, set to 2. If `generic_next_level == 6`, set to 2.
- `6` (results_FINAL.md:373, bare number) 4. Recode: if `targeted_level == 6`, set to 2. If `generic_next_level == 6`, set to 2.
- `2` (results_FINAL.md:373, bare number) 4. Recode: if `targeted_level == 6`, set to 2. If `generic_next_level == 6`, set to 2.
- `6` (results_FINAL.md:373, bare number) 4. Recode: if `targeted_level == 6`, set to 2. If `generic_next_level == 6`, set to 2.
- `2` (results_FINAL.md:373, bare number) 4. Recode: if `targeted_level == 6`, set to 2. If `generic_next_level == 6`, set to 2.
- `5` (results_FINAL.md:374, reliability or effect size) 5. Remaining n=177 pairs. Wilcoxon signed-rank on non-zero differences.
- `177` (results_FINAL.md:374, reliability or effect size) 5. Remaining n=177 pairs. Wilcoxon signed-rank on non-zero differences.
- `0.25` (results_FINAL.md:375, p-value) - **What it measures:** "Does a targeted revision (with specific critique) produce higher quality than the model's own genuine generic revision at the next turn?" Answer: yes, by +0.25 levels unstripp
- `0.004` (results_FINAL.md:375, p-value) - **What it measures:** "Does a targeted revision (with specific critique) produce higher quality than the model's own genuine generic revision at the next turn?" Answer: yes, by +0.25 levels unstripp
- `1.16` (results_FINAL.md:375, p-value) - **What it measures:** "Does a targeted revision (with specific critique) produce higher quality than the model's own genuine generic revision at the next turn?" Answer: yes, by +0.25 levels unstripp
- `5` (results_FINAL.md:375, p-value) - **What it measures:** "Does a targeted revision (with specific critique) produce higher quality than the model's own genuine generic revision at the next turn?" Answer: yes, by +0.25 levels unstripp
- `19` (results_FINAL.md:375, p-value) - **What it measures:** "Does a targeted revision (with specific critique) produce higher quality than the model's own genuine generic revision at the next turn?" Answer: yes, by +0.25 levels unstripp
- `0.25` (results_FINAL.md:375, p-value) - **What it measures:** "Does a targeted revision (with specific critique) produce higher quality than the model's own genuine generic revision at the next turn?" Answer: yes, by +0.25 levels unstripp
- `4.43` (results_FINAL.md:375, p-value) - **What it measures:** "Does a targeted revision (with specific critique) produce higher quality than the model's own genuine generic revision at the next turn?" Answer: yes, by +0.25 levels unstripp
- `3.53` (results_FINAL.md:375, p-value) - **What it measures:** "Does a targeted revision (with specific critique) produce higher quality than the model's own genuine generic revision at the next turn?" Answer: yes, by +0.25 levels unstripp
- `9` (results_FINAL.md:375, p-value) - **What it measures:** "Does a targeted revision (with specific critique) produce higher quality than the model's own genuine generic revision at the next turn?" Answer: yes, by +0.25 levels unstripp
- `177` (results_FINAL.md:375, p-value) - **What it measures:** "Does a targeted revision (with specific critique) produce higher quality than the model's own genuine generic revision at the next turn?" Answer: yes, by +0.25 levels unstripp
- `5` (results_FINAL.md:375, p-value) - **What it measures:** "Does a targeted revision (with specific critique) produce higher quality than the model's own genuine generic revision at the next turn?" Answer: yes, by +0.25 levels unstripp
- `2.00` (results_FINAL.md:376, count or denominator) - **Supersedes:** The paper's +2.00 (n=424) used the old keyword classifier (`classify_revision()` in `analyze.py`), which let 424 records through because it failed to catch verbose declines. Those de
- `424` (results_FINAL.md:376, count or denominator) - **Supersedes:** The paper's +2.00 (n=424) used the old keyword classifier (`classify_revision()` in `analyze.py`), which let 424 records through because it failed to catch verbose declines. Those de
- `424` (results_FINAL.md:376, count or denominator) - **Supersedes:** The paper's +2.00 (n=424) used the old keyword classifier (`classify_revision()` in `analyze.py`), which let 424 records through because it failed to catch verbose declines. Those de
- `1` (results_FINAL.md:376, count or denominator) - **Supersedes:** The paper's +2.00 (n=424) used the old keyword classifier (`classify_revision()` in `analyze.py`), which let 424 records through because it failed to catch verbose declines. Those de
- `2` (results_FINAL.md:376, count or denominator) - **Supersedes:** The paper's +2.00 (n=424) used the old keyword classifier (`classify_revision()` in `analyze.py`), which let 424 records through because it failed to catch verbose declines. Those de
- `2.00` (results_FINAL.md:376, count or denominator) - **Supersedes:** The paper's +2.00 (n=424) used the old keyword classifier (`classify_revision()` in `analyze.py`), which let 424 records through because it failed to catch verbose declines. Those de
- `0.79` (results_FINAL.md:377, count or denominator) - **Discarded:** +0.79/n=106 was cited from a prior conversation session but is not reproducible from any filter on the current data files. It does not appear in `study3_results.json` or any saved out
- `106` (results_FINAL.md:377, count or denominator) - **Discarded:** +0.79/n=106 was cited from a prior conversation session but is not reproducible from any filter on the current data files. It does not appear in `study3_results.json` or any saved out

### [results_FINAL.md] 5. TARGETED FEEDBACK -- 5b. Targeted feedback by input type (POST-HOC, added 2026-09-20)

*- **Filter (exact):** Load all 1,047 records from `targeted_feedback_results.jsonl`. Each record has fields `targeted_level`, `generic_next_level`, `worker_trial_id`, `turn`. For each record:*

- `2026` (results_FINAL.md:382, bare number) ### 5b. Targeted feedback by input type (POST-HOC, added 2026-09-20)
- `09` (results_FINAL.md:382, bare number) ### 5b. Targeted feedback by input type (POST-HOC, added 2026-09-20)
- `20` (results_FINAL.md:382, bare number) ### 5b. Targeted feedback by input type (POST-HOC, added 2026-09-20)
- `2026` (results_FINAL.md:384, bare number) **Post-hoc and not pre-registered.** Proposed by the assistant on 2026-09-20 and authorised by
- `09` (results_FINAL.md:384, bare number) **Post-hoc and not pre-registered.** Proposed by the assistant on 2026-09-20 and authorised by
- `20` (results_FINAL.md:384, bare number) **Post-hoc and not pre-registered.** Proposed by the assistant on 2026-09-20 and authorised by
- `177` (results_FINAL.md:385, count or denominator) Liam the same day, after the composition of the n=177 arm was found not to be disclosed
- `177` (results_FINAL.md:389, bare number) The 177 pairs of Section 5 were stratified by what the input to the revision actually was. The
- `5` (results_FINAL.md:389, bare number) The 177 pairs of Section 5 were stratified by what the input to the revision actually was. The
- `1` (results_FINAL.md:391, bare number) `genuine_meta_labels.jsonl` at that same turn, and turn-1 inputs are unlabelled and counted
- `177` (results_FINAL.md:394, bare number) **Composition of the 177:** 109 meta-response inputs (101 of them scored level 1), 37 genuine
- `109` (results_FINAL.md:394, bare number) **Composition of the 177:** 109 meta-response inputs (101 of them scored level 1), 37 genuine
- `101` (results_FINAL.md:394, bare number) **Composition of the 177:** 109 meta-response inputs (101 of them scored level 1), 37 genuine
- `1` (results_FINAL.md:394, bare number) **Composition of the 177:** 109 meta-response inputs (101 of them scored level 1), 37 genuine
- `37` (results_FINAL.md:394, bare number) **Composition of the 177:** 109 meta-response inputs (101 of them scored level 1), 37 genuine
- `31` (results_FINAL.md:395, bare number) revisions, 31 turn-1 drafts.
- `1` (results_FINAL.md:395, bare number) revisions, 31 turn-1 drafts.
- `2026` (results_FINAL.md:397, bare number) **Sufficient inputs, corrected 2026-09-20.** An earlier version of this entry said zero inputs
- `09` (results_FINAL.md:397, bare number) **Sufficient inputs, corrected 2026-09-20.** An earlier version of this entry said zero inputs
- `20` (results_FINAL.md:397, bare number) **Sufficient inputs, corrected 2026-09-20.** An earlier version of this entry said zero inputs
- `215` (results_FINAL.md:399, bare number) `scripts/study3/phase6_targeted_feedback.py:215` filters on (`level <= 3`), and the unstripped
- `3` (results_FINAL.md:399, bare number) `scripts/study3/phase6_targeted_feedback.py:215` filters on (`level <= 3`), and the unstripped
- `102` (results_FINAL.md:400, bare number) input levels are 102 at level 1, 17 at level 2 and 58 at level 3. On the STRIPPED scale, which
- `1` (results_FINAL.md:400, bare number) input levels are 102 at level 1, 17 at level 2 and 58 at level 3. On the STRIPPED scale, which
- `17` (results_FINAL.md:400, bare number) input levels are 102 at level 1, 17 at level 2 and 58 at level 3. On the STRIPPED scale, which
- `2` (results_FINAL.md:400, bare number) input levels are 102 at level 1, 17 at level 2 and 58 at level 3. On the STRIPPED scale, which
- `58` (results_FINAL.md:400, bare number) input levels are 102 at level 1, 17 at level 2 and 58 at level 3. On the STRIPPED scale, which
- `3` (results_FINAL.md:400, bare number) input levels are 102 at level 1, 17 at level 2 and 58 at level 3. On the STRIPPED scale, which
- `100` (results_FINAL.md:401, count or denominator) is the paper's primary basis, the distribution is 100 / 17 / 49 / **11 at level 4**. Stripping
- `17` (results_FINAL.md:401, count or denominator) is the paper's primary basis, the distribution is 100 / 17 / 49 / **11 at level 4**. Stripping
- `49` (results_FINAL.md:401, count or denominator) is the paper's primary basis, the distribution is 100 / 17 / 49 / **11 at level 4**. Stripping
- `11` (results_FINAL.md:401, count or denominator) is the paper's primary basis, the distribution is 100 / 17 / 49 / **11 at level 4**. Stripping
- `4` (results_FINAL.md:401, count or denominator) is the paper's primary basis, the distribution is 100 / 17 / 49 / **11 at level 4**. Stripping
- `3.3` (results_FINAL.md:404, mean or delta) Those eleven cannot carry an estimate and are not one. All eleven are Llama 3.3 70B, with none
- `4` (results_FINAL.md:405, bare number) from the other five models. All eleven sit exactly at level 4 and none higher. Ten were rated
- `3` (results_FINAL.md:406, bare number) level 3 unstripped and one level 2, so every one of them is a case where the two scorings
- `2` (results_FINAL.md:406, bare number) level 3 unstripped and one level 2, so every one of them is a case where the two scorings
- `1.18` (results_FINAL.md:408, mean or delta) by that disagreement rather than sampled from sufficient work. Their descriptive gain is +1.18,
- `6` (results_FINAL.md:411, bare number) Measuring the remedy on work that is sufficient on both scales requires rerunning phase 6 with
- `68` (results_FINAL.md:419, mean or delta) | Draft or genuine revision | 68 | 4.76 | 3.18 | **+1.59** | 5.44e-11 |
- `4.76` (results_FINAL.md:419, mean or delta) | Draft or genuine revision | 68 | 4.76 | 3.18 | **+1.59** | 5.44e-11 |
- `3.18` (results_FINAL.md:419, mean or delta) | Draft or genuine revision | 68 | 4.76 | 3.18 | **+1.59** | 5.44e-11 |
- `1.59` (results_FINAL.md:419, mean or delta) | Draft or genuine revision | 68 | 4.76 | 3.18 | **+1.59** | 5.44e-11 |
- `5` (results_FINAL.md:419, mean or delta) | Draft or genuine revision | 68 | 4.76 | 3.18 | **+1.59** | 5.44e-11 |
- `11` (results_FINAL.md:419, mean or delta) | Draft or genuine revision | 68 | 4.76 | 3.18 | **+1.59** | 5.44e-11 |
- `109` (results_FINAL.md:420, mean or delta) | Meta-response | 109 | 4.63 | 3.74 | +0.89 | 1.04e-09 |
- `4.63` (results_FINAL.md:420, mean or delta) | Meta-response | 109 | 4.63 | 3.74 | +0.89 | 1.04e-09 |
- `3.74` (results_FINAL.md:420, mean or delta) | Meta-response | 109 | 4.63 | 3.74 | +0.89 | 1.04e-09 |
- `0.89` (results_FINAL.md:420, mean or delta) | Meta-response | 109 | 4.63 | 3.74 | +0.89 | 1.04e-09 |
- `1` (results_FINAL.md:420, mean or delta) | Meta-response | 109 | 4.63 | 3.74 | +0.89 | 1.04e-09 |
- `09` (results_FINAL.md:420, mean or delta) | Meta-response | 109 | 4.63 | 3.74 | +0.89 | 1.04e-09 |
- `5` (results_FINAL.md:421, mean or delta) | All (Section 5) | 177 | 4.68 | 3.53 | +1.16 | 5.74e-19 |
- `177` (results_FINAL.md:421, mean or delta) | All (Section 5) | 177 | 4.68 | 3.53 | +1.16 | 5.74e-19 |
- `4.68` (results_FINAL.md:421, mean or delta) | All (Section 5) | 177 | 4.68 | 3.53 | +1.16 | 5.74e-19 |
- `3.53` (results_FINAL.md:421, mean or delta) | All (Section 5) | 177 | 4.68 | 3.53 | +1.16 | 5.74e-19 |
- `1.16` (results_FINAL.md:421, mean or delta) | All (Section 5) | 177 | 4.68 | 3.53 | +1.16 | 5.74e-19 |
- `5` (results_FINAL.md:421, mean or delta) | All (Section 5) | 177 | 4.68 | 3.53 | +1.16 | 5.74e-19 |
- `19` (results_FINAL.md:421, mean or delta) | All (Section 5) | 177 | 4.68 | 3.53 | +1.16 | 5.74e-19 |
- `68` (results_FINAL.md:427, mean or delta) | Draft or genuine revision | 68 | 4.76 | 4.88 | -0.12 | 2.39e-01 |
- `4.76` (results_FINAL.md:427, mean or delta) | Draft or genuine revision | 68 | 4.76 | 4.88 | -0.12 | 2.39e-01 |
- `4.88` (results_FINAL.md:427, mean or delta) | Draft or genuine revision | 68 | 4.76 | 4.88 | -0.12 | 2.39e-01 |
- `0.12` (results_FINAL.md:427, mean or delta) | Draft or genuine revision | 68 | 4.76 | 4.88 | -0.12 | 2.39e-01 |
- `2` (results_FINAL.md:427, mean or delta) | Draft or genuine revision | 68 | 4.76 | 4.88 | -0.12 | 2.39e-01 |
- `01` (results_FINAL.md:427, mean or delta) | Draft or genuine revision | 68 | 4.76 | 4.88 | -0.12 | 2.39e-01 |
- `109` (results_FINAL.md:428, mean or delta) | Meta-response | 109 | 4.63 | 4.15 | +0.49 | 1.10e-04 |
- `4.63` (results_FINAL.md:428, mean or delta) | Meta-response | 109 | 4.63 | 4.15 | +0.49 | 1.10e-04 |
- `4.15` (results_FINAL.md:428, mean or delta) | Meta-response | 109 | 4.63 | 4.15 | +0.49 | 1.10e-04 |
- `0.49` (results_FINAL.md:428, mean or delta) | Meta-response | 109 | 4.63 | 4.15 | +0.49 | 1.10e-04 |
- `1` (results_FINAL.md:428, mean or delta) | Meta-response | 109 | 4.63 | 4.15 | +0.49 | 1.10e-04 |
- `04` (results_FINAL.md:428, mean or delta) | Meta-response | 109 | 4.63 | 4.15 | +0.49 | 1.10e-04 |
- `5` (results_FINAL.md:429, mean or delta) | All (Section 5) | 177 | 4.68 | 4.43 | +0.25 | 3.75e-03 |
- `177` (results_FINAL.md:429, mean or delta) | All (Section 5) | 177 | 4.68 | 4.43 | +0.25 | 3.75e-03 |
- `4.68` (results_FINAL.md:429, mean or delta) | All (Section 5) | 177 | 4.68 | 4.43 | +0.25 | 3.75e-03 |
- `4.43` (results_FINAL.md:429, mean or delta) | All (Section 5) | 177 | 4.68 | 4.43 | +0.25 | 3.75e-03 |
- `0.25` (results_FINAL.md:429, mean or delta) | All (Section 5) | 177 | 4.68 | 4.43 | +0.25 | 3.75e-03 |
- `3` (results_FINAL.md:429, mean or delta) | All (Section 5) | 177 | 4.68 | 4.43 | +0.25 | 3.75e-03 |
- `03` (results_FINAL.md:429, mean or delta) | All (Section 5) | 177 | 4.68 | 4.43 | +0.25 | 3.75e-03 |
- `5` (results_FINAL.md:431, bare number) - **Filter (exact):** the Section 5 filter unchanged, then split on the classifier label at the
- `6` (results_FINAL.md:432, bare number) input turn. Level 6 recoded to 2 on both sides. Stripped generic level from
- `2` (results_FINAL.md:432, bare number) input turn. Level 6 recoded to 2 on both sides. Stripped generic level from
- `1` (results_FINAL.md:433, bare number) `stripped_rescore_full.jsonl` at turn + 1. All three pooled rows reproduce Section 5 exactly.
- `5` (results_FINAL.md:433, bare number) `stripped_rescore_full.jsonl` at turn + 1. All three pooled rows reproduce Section 5 exactly.
- `1.16` (results_FINAL.md:434, mean or delta) - **What it settles.** The +1.16 is not an artefact of the meta-response inputs. It is larger on
- `1.59` (results_FINAL.md:435, mean or delta) real drafts (+1.59) than on meta-responses (+0.89), and the pooled figure is diluted by them
- `0.89` (results_FINAL.md:435, mean or delta) real drafts (+1.59) than on meta-responses (+0.89), and the pooled figure is diluted by them
- `4.88` (results_FINAL.md:437, mean or delta) because unstripped generic revisions on real drafts score 4.88, inflated by the
- `1` (results_FINAL.md:440, bare number) demonstrated on work rated 1 to 3 and has never been measured on work rated 4 or above, which
- `3` (results_FINAL.md:440, bare number) demonstrated on work rated 1 to 3 and has never been measured on work rated 4 or above, which
- `4` (results_FINAL.md:440, bare number) demonstrated on work rated 1 to 3 and has never been measured on work rated 4 or above, which
- `27.5` (results_FINAL.md:441, percentage) is the population the paper's cliff, its 27.5% figure and the STET diagnostic all concern.

### [results_FINAL.md] 5. TARGETED FEEDBACK -- 5c. Targeted feedback by model (added 2026-09-20)

*- **Filter (exact):** the Section 5 filter unchanged, then split on the classifier label at the*

- `2026` (results_FINAL.md:445, bare number) ### 5c. Targeted feedback by model (added 2026-09-20)
- `09` (results_FINAL.md:445, bare number) ### 5c. Targeted feedback by model (added 2026-09-20)
- `20` (results_FINAL.md:445, bare number) ### 5c. Targeted feedback by model (added 2026-09-20)
- `2026` (results_FINAL.md:447, bare number) `tab:targeted-per-model` in the paper had no ledger entry. Recomputed 2026-09-20 and recorded.
- `09` (results_FINAL.md:447, bare number) `tab:targeted-per-model` in the paper had no ledger entry. Recomputed 2026-09-20 and recorded.
- `20` (results_FINAL.md:447, bare number) `tab:targeted-per-model` in the paper had no ledger entry. Recomputed 2026-09-20 and recorded.
- `3.3` (results_FINAL.md:451, mean or delta) | Llama 3.3 70B | 71 | +1.62 | 9.2e-12 |
- `71` (results_FINAL.md:451, mean or delta) | Llama 3.3 70B | 71 | +1.62 | 9.2e-12 |
- `1.62` (results_FINAL.md:451, mean or delta) | Llama 3.3 70B | 71 | +1.62 | 9.2e-12 |
- `9` (results_FINAL.md:451, mean or delta) | Llama 3.3 70B | 71 | +1.62 | 9.2e-12 |
- `12` (results_FINAL.md:451, mean or delta) | Llama 3.3 70B | 71 | +1.62 | 9.2e-12 |
- `3` (results_FINAL.md:452, mean or delta) | Qwen 3 235B | 21 | +1.48 | 4.5e-04 |
- `21` (results_FINAL.md:452, mean or delta) | Qwen 3 235B | 21 | +1.48 | 4.5e-04 |
- `1.48` (results_FINAL.md:452, mean or delta) | Qwen 3 235B | 21 | +1.48 | 4.5e-04 |
- `4` (results_FINAL.md:452, mean or delta) | Qwen 3 235B | 21 | +1.48 | 4.5e-04 |
- `04` (results_FINAL.md:452, mean or delta) | Qwen 3 235B | 21 | +1.48 | 4.5e-04 |
- `12` (results_FINAL.md:453, mean or delta) | GPT-4o | 12 | +1.33 | 7.8e-03 |
- `1.33` (results_FINAL.md:453, mean or delta) | GPT-4o | 12 | +1.33 | 7.8e-03 |
- `7` (results_FINAL.md:453, mean or delta) | GPT-4o | 12 | +1.33 | 7.8e-03 |
- `03` (results_FINAL.md:453, mean or delta) | GPT-4o | 12 | +1.33 | 7.8e-03 |
- `19` (results_FINAL.md:454, mean or delta) | DeepSeek V4 Flash | 19 | +1.05 | **1.5e-02** |
- `1.05` (results_FINAL.md:454, mean or delta) | DeepSeek V4 Flash | 19 | +1.05 | **1.5e-02** |
- `1` (results_FINAL.md:454, mean or delta) | DeepSeek V4 Flash | 19 | +1.05 | **1.5e-02** |
- `02` (results_FINAL.md:454, mean or delta) | DeepSeek V4 Flash | 19 | +1.05 | **1.5e-02** |
- `4` (results_FINAL.md:455, mean or delta) | Claude Sonnet 4 | 51 | +0.31 | 1.2e-02 |
- `51` (results_FINAL.md:455, mean or delta) | Claude Sonnet 4 | 51 | +0.31 | 1.2e-02 |
- `0.31` (results_FINAL.md:455, mean or delta) | Claude Sonnet 4 | 51 | +0.31 | 1.2e-02 |
- `1` (results_FINAL.md:455, mean or delta) | Claude Sonnet 4 | 51 | +0.31 | 1.2e-02 |
- `02` (results_FINAL.md:455, mean or delta) | Claude Sonnet 4 | 51 | +0.31 | 1.2e-02 |
- `2.5` (results_FINAL.md:456, mean or delta) | Gemini 2.5 Flash | 3 | +2.33 | not reported, n < 5 |
- `3` (results_FINAL.md:456, mean or delta) | Gemini 2.5 Flash | 3 | +2.33 | not reported, n < 5 |
- `2.33` (results_FINAL.md:456, mean or delta) | Gemini 2.5 Flash | 3 | +2.33 | not reported, n < 5 |
- `5` (results_FINAL.md:456, mean or delta) | Gemini 2.5 Flash | 3 | +2.33 | not reported, n < 5 |
- `5` (results_FINAL.md:458, bare number) - **Filter (exact):** the Section 5 selection, split by `model`. Targeted level against the
- `6` (results_FINAL.md:459, bare number) stripped level of the generic next-turn revision, 6 -> 2 recode on both sides. Two-sided
- `2` (results_FINAL.md:459, bare number) stripped level of the generic next-turn revision, 6 -> 2 recode on both sides. Two-sided
- `1` (results_FINAL.md:462, mean or delta) - **Correction.** The paper printed 1.2e-02 for DeepSeek, which is the value on the Claude row
- `02` (results_FINAL.md:462, mean or delta) - **Correction.** The paper printed 1.2e-02 for DeepSeek, which is the value on the Claude row
- `1` (results_FINAL.md:463, mean or delta) directly below it. No test variant reproduces it: exact/wilcox gives 1.34e-02, auto/wilcox
- `02` (results_FINAL.md:463, mean or delta) directly below it. No test variant reproduces it: exact/wilcox gives 1.34e-02, auto/wilcox
- `1` (results_FINAL.md:464, mean or delta) 1.45e-02, pratt and zsplit further away. Corrected to 1.5e-02. The delta, the n and every
- `02` (results_FINAL.md:464, mean or delta) 1.45e-02, pratt and zsplit further away. Corrected to 1.5e-02. The delta, the n and every
- `1` (results_FINAL.md:464, mean or delta) 1.45e-02, pratt and zsplit further away. Corrected to 1.5e-02. The delta, the n and every
- `02` (results_FINAL.md:464, mean or delta) 1.45e-02, pratt and zsplit further away. Corrected to 1.5e-02. The delta, the n and every
- `177` (results_FINAL.md:467, bare number) - n sums to 177, matching Section 5.
- `5` (results_FINAL.md:467, bare number) - n sums to 177, matching Section 5.

### [results_FINAL.md] 6. REVISION TAX

*- **Filter (exact):** the Section 5 selection, split by `model`. Targeted level against the*

- `6` (results_FINAL.md:471, bare number) ## 6. REVISION TAX

### [results_FINAL.md] 6. REVISION TAX -- Method

*- **Filter (exact):** the Section 5 selection, split by `model`. Targeted level against the*

- `3,125` (results_FINAL.md:475, percentage) - **Estimator:** Ratio-of-means aggregate (sum all waste tokens / sum all baseline tokens). NOT mean-of-ratios (which is small-denominator-sensitive and produced 3,125% outliers in early runs).
- `6` (results_FINAL.md:477, bare number) - **t*:** argmax of mean GENUINE-only quality (6->2 recoded) across turns, requiring min n >= 5 at each turn for eligibility. Result: t* = T1 for all 6 models.
- `2` (results_FINAL.md:477, bare number) - **t*:** argmax of mean GENUINE-only quality (6->2 recoded) across turns, requiring min n >= 5 at each turn for eligibility. Result: t* = T1 for all 6 models.
- `5` (results_FINAL.md:477, bare number) - **t*:** argmax of mean GENUINE-only quality (6->2 recoded) across turns, requiring min n >= 5 at each turn for eligibility. Result: t* = T1 for all 6 models.
- `6` (results_FINAL.md:477, bare number) - **t*:** argmax of mean GENUINE-only quality (6->2 recoded) across turns, requiring min n >= 5 at each turn for eligibility. Result: t* = T1 for all 6 models.
- `6` (results_FINAL.md:479, percentage) - **Supersedes:** Old Section 6 numbers (7.4%, 19.9%, 42.0%, 95.0%, 142.2%, 262.0%, aggregate 48.0%/92.4%/270,457) were transcribed from a prior session's terminal output and are not saved in any data
- `7.4` (results_FINAL.md:479, percentage) - **Supersedes:** Old Section 6 numbers (7.4%, 19.9%, 42.0%, 95.0%, 142.2%, 262.0%, aggregate 48.0%/92.4%/270,457) were transcribed from a prior session's terminal output and are not saved in any data
- `19.9` (results_FINAL.md:479, percentage) - **Supersedes:** Old Section 6 numbers (7.4%, 19.9%, 42.0%, 95.0%, 142.2%, 262.0%, aggregate 48.0%/92.4%/270,457) were transcribed from a prior session's terminal output and are not saved in any data
- `42.0` (results_FINAL.md:479, percentage) - **Supersedes:** Old Section 6 numbers (7.4%, 19.9%, 42.0%, 95.0%, 142.2%, 262.0%, aggregate 48.0%/92.4%/270,457) were transcribed from a prior session's terminal output and are not saved in any data
- `95.0` (results_FINAL.md:479, percentage) - **Supersedes:** Old Section 6 numbers (7.4%, 19.9%, 42.0%, 95.0%, 142.2%, 262.0%, aggregate 48.0%/92.4%/270,457) were transcribed from a prior session's terminal output and are not saved in any data
- `142.2` (results_FINAL.md:479, percentage) - **Supersedes:** Old Section 6 numbers (7.4%, 19.9%, 42.0%, 95.0%, 142.2%, 262.0%, aggregate 48.0%/92.4%/270,457) were transcribed from a prior session's terminal output and are not saved in any data
- `262.0` (results_FINAL.md:479, percentage) - **Supersedes:** Old Section 6 numbers (7.4%, 19.9%, 42.0%, 95.0%, 142.2%, 262.0%, aggregate 48.0%/92.4%/270,457) were transcribed from a prior session's terminal output and are not saved in any data
- `48.0` (results_FINAL.md:479, percentage) - **Supersedes:** Old Section 6 numbers (7.4%, 19.9%, 42.0%, 95.0%, 142.2%, 262.0%, aggregate 48.0%/92.4%/270,457) were transcribed from a prior session's terminal output and are not saved in any data
- `92.4` (results_FINAL.md:479, percentage) - **Supersedes:** Old Section 6 numbers (7.4%, 19.9%, 42.0%, 95.0%, 142.2%, 262.0%, aggregate 48.0%/92.4%/270,457) were transcribed from a prior session's terminal output and are not saved in any data
- `270,457` (results_FINAL.md:479, percentage) - **Supersedes:** Old Section 6 numbers (7.4%, 19.9%, 42.0%, 95.0%, 142.2%, 262.0%, aggregate 48.0%/92.4%/270,457) were transcribed from a prior session's terminal output and are not saved in any data

### [results_FINAL.md] 6. REVISION TAX -- Per-Model (Interpretation A, t*=T1 for all)

*- **Filter (exact):** the Section 5 selection, split by `model`. Targeted level against the*

- `2.5` (results_FINAL.md:485, mean or delta) | gemini-2.5-flash | T1 | 30.6 | 23.4 | $0.0001 |
- `30.6` (results_FINAL.md:485, mean or delta) | gemini-2.5-flash | T1 | 30.6 | 23.4 | $0.0001 |
- `23.4` (results_FINAL.md:485, mean or delta) | gemini-2.5-flash | T1 | 30.6 | 23.4 | $0.0001 |
- `0.0001` (results_FINAL.md:485, mean or delta) | gemini-2.5-flash | T1 | 30.6 | 23.4 | $0.0001 |
- `118.9` (results_FINAL.md:486, mean or delta) | deepseek-v4 | T1 | 118.9 | 54.3 | $0.0005 |
- `54.3` (results_FINAL.md:486, mean or delta) | deepseek-v4 | T1 | 118.9 | 54.3 | $0.0005 |
- `0.0005` (results_FINAL.md:486, mean or delta) | deepseek-v4 | T1 | 118.9 | 54.3 | $0.0005 |
- `125.8` (results_FINAL.md:487, mean or delta) | gpt-4o | T1 | 125.8 | 55.7 | $0.0053 |
- `55.7` (results_FINAL.md:487, mean or delta) | gpt-4o | T1 | 125.8 | 55.7 | $0.0053 |
- `0.0053` (results_FINAL.md:487, mean or delta) | gpt-4o | T1 | 125.8 | 55.7 | $0.0053 |
- `3` (results_FINAL.md:488, mean or delta) | qwen-3-235b | T1 | 198.6 | 66.5 | $0.0009 |
- `198.6` (results_FINAL.md:488, mean or delta) | qwen-3-235b | T1 | 198.6 | 66.5 | $0.0009 |
- `66.5` (results_FINAL.md:488, mean or delta) | qwen-3-235b | T1 | 198.6 | 66.5 | $0.0009 |
- `0.0009` (results_FINAL.md:488, mean or delta) | qwen-3-235b | T1 | 198.6 | 66.5 | $0.0009 |
- `4` (results_FINAL.md:489, mean or delta) | claude-sonnet-4 | T1 | 251.6 | 71.6 | $0.0182 |
- `251.6` (results_FINAL.md:489, mean or delta) | claude-sonnet-4 | T1 | 251.6 | 71.6 | $0.0182 |
- `71.6` (results_FINAL.md:489, mean or delta) | claude-sonnet-4 | T1 | 251.6 | 71.6 | $0.0182 |
- `0.0182` (results_FINAL.md:489, mean or delta) | claude-sonnet-4 | T1 | 251.6 | 71.6 | $0.0182 |
- `3.3` (results_FINAL.md:490, mean or delta) | llama-3.3-70b | T1 | 436.0 | 81.3 | $0.0013 |
- `436.0` (results_FINAL.md:490, mean or delta) | llama-3.3-70b | T1 | 436.0 | 81.3 | $0.0013 |
- `81.3` (results_FINAL.md:490, mean or delta) | llama-3.3-70b | T1 | 436.0 | 81.3 | $0.0013 |
- `0.0013` (results_FINAL.md:490, mean or delta) | llama-3.3-70b | T1 | 436.0 | 81.3 | $0.0013 |

### [results_FINAL.md] 6. REVISION TAX -- Aggregate

*- **Filter (exact):** the Section 5 selection, split by `model`. Targeted level against the*

- `62.1` (results_FINAL.md:496, percentage) | Aggregate waste fraction | **62.1%** |
- `164.2` (results_FINAL.md:497, percentage) | Aggregate tax | 164.2% |
- `653,070` (results_FINAL.md:498, bare number) | Total wasted tokens | 653,070 |
- `6` (results_FINAL.md:500, count or denominator) **t* = T1 for all 6 models.** No model benefits from undirected revision on the GENUINE-only quality trajectory. GPT-4o would show t*=T5 without the min_n floor (3 trials at T5 averaging 4.0 vs T1's 3
- `3` (results_FINAL.md:500, count or denominator) **t* = T1 for all 6 models.** No model benefits from undirected revision on the GENUINE-only quality trajectory. GPT-4o would show t*=T5 without the min_n floor (3 trials at T5 averaging 4.0 vs T1's 3
- `4.0` (results_FINAL.md:500, count or denominator) **t* = T1 for all 6 models.** No model benefits from undirected revision on the GENUINE-only quality trajectory. GPT-4o would show t*=T5 without the min_n floor (3 trials at T5 averaging 4.0 vs T1's 3
- `3.99` (results_FINAL.md:500, count or denominator) **t* = T1 for all 6 models.** No model benefits from undirected revision on the GENUINE-only quality trajectory. GPT-4o would show t*=T5 without the min_n floor (3 trials at T5 averaging 4.0 vs T1's 3
- `120` (results_FINAL.md:500, count or denominator) **t* = T1 for all 6 models.** No model benefits from undirected revision on the GENUINE-only quality trajectory. GPT-4o would show t*=T5 without the min_n floor (3 trials at T5 averaging 4.0 vs T1's 3

### [results_FINAL.md] 6. REVISION TAX -- Pricing Table (from `scripts/study3/analyze.py` lines 1515-1523, labeled "Real 2025 API pricing")

*- **Filter (exact):** the Section 5 selection, split by `model`. Targeted level against the*

- `1515` (results_FINAL.md:502, bare number) ### Pricing Table (from `scripts/study3/analyze.py` lines 1515-1523, labeled "Real 2025 API pricing")
- `1523` (results_FINAL.md:502, bare number) ### Pricing Table (from `scripts/study3/analyze.py` lines 1515-1523, labeled "Real 2025 API pricing")
- `2025` (results_FINAL.md:502, bare number) ### Pricing Table (from `scripts/study3/analyze.py` lines 1515-1523, labeled "Real 2025 API pricing")
- `2.5` (results_FINAL.md:506, mean or delta) | gemini-2.5-flash | $0.40 |
- `0.40` (results_FINAL.md:506, mean or delta) | gemini-2.5-flash | $0.40 |
- `0.55` (results_FINAL.md:507, mean or delta) | deepseek-v4 | $0.55 |
- `3.3` (results_FINAL.md:508, mean or delta) | llama-3.3-70b | $0.88 |
- `0.88` (results_FINAL.md:508, mean or delta) | llama-3.3-70b | $0.88 |
- `3` (results_FINAL.md:509, mean or delta) | qwen-3-235b | $0.90 |
- `0.90` (results_FINAL.md:509, mean or delta) | qwen-3-235b | $0.90 |
- `10.00` (results_FINAL.md:510, mean or delta) | gpt-4o | $10.00 |
- `4` (results_FINAL.md:511, mean or delta) | claude-sonnet-4 | $15.00 |
- `15.00` (results_FINAL.md:511, mean or delta) | claude-sonnet-4 | $15.00 |
- `2025` (results_FINAL.md:513, percentage) **Dollar figures are pricing-tier-dominated** (Claude's $/task is 182x Gemini's despite similar waste%) and based on 2025 output-token prices (Qwen/Llama via Together.ai). These need verification agai
- `1` (results_FINAL.md:516, bare number) - **Filter (t*):** For each model, for each turn T in {1..5}, compute mean quality from `evaluator_results.jsonl` (`level`, recoded 6->2) restricted to: T1 for all 120 trials; T2-T5 only where `genuin
- `6` (results_FINAL.md:516, bare number) - **Filter (t*):** For each model, for each turn T in {1..5}, compute mean quality from `evaluator_results.jsonl` (`level`, recoded 6->2) restricted to: T1 for all 120 trials; T2-T5 only where `genuin
- `2` (results_FINAL.md:516, bare number) - **Filter (t*):** For each model, for each turn T in {1..5}, compute mean quality from `evaluator_results.jsonl` (`level`, recoded 6->2) restricted to: T1 for all 120 trials; T2-T5 only where `genuin
- `120` (results_FINAL.md:516, bare number) - **Filter (t*):** For each model, for each turn T in {1..5}, compute mean quality from `evaluator_results.jsonl` (`level`, recoded 6->2) restricted to: T1 for all 120 trials; T2-T5 only where `genuin
- `5` (results_FINAL.md:516, bare number) - **Filter (t*):** For each model, for each turn T in {1..5}, compute mean quality from `evaluator_results.jsonl` (`level`, recoded 6->2) restricted to: T1 for all 120 trials; T2-T5 only where `genuin
- `720` (results_FINAL.md:517, percentage) - **Filter (tax/waste):** For each of 720 trials, extract `token_counts[turn_idx]["output"]` for turns 1-5. Baseline tokens = sum of tokens at turns <= t* (= T1 tokens only, since t*=T1). Waste tokens
- `1` (results_FINAL.md:517, percentage) - **Filter (tax/waste):** For each of 720 trials, extract `token_counts[turn_idx]["output"]` for turns 1-5. Baseline tokens = sum of tokens at turns <= t* (= T1 tokens only, since t*=T1). Waste tokens
- `5` (results_FINAL.md:517, percentage) - **Filter (tax/waste):** For each of 720 trials, extract `token_counts[turn_idx]["output"]` for turns 1-5. Baseline tokens = sum of tokens at turns <= t* (= T1 tokens only, since t*=T1). Waste tokens
- `100` (results_FINAL.md:517, percentage) - **Filter (tax/waste):** For each of 720 trials, extract `token_counts[turn_idx]["output"]` for turns 1-5. Baseline tokens = sum of tokens at turns <= t* (= T1 tokens only, since t*=T1). Waste tokens
- `100` (results_FINAL.md:517, percentage) - **Filter (tax/waste):** For each of 720 trials, extract `token_counts[turn_idx]["output"]` for turns 1-5. Baseline tokens = sum of tokens at turns <= t* (= T1 tokens only, since t*=T1). Waste tokens
- `720` (results_FINAL.md:517, percentage) - **Filter (tax/waste):** For each of 720 trials, extract `token_counts[turn_idx]["output"]` for turns 1-5. Baseline tokens = sum of tokens at turns <= t* (= T1 tokens only, since t*=T1). Waste tokens

### [results_FINAL.md] 7. REVERSIBILITY (Human Annotation)

*- **Filter ($/task):** waste_tokens_per_trial x price_per_token. Price from the table above (output tokens only).*

- `7` (results_FINAL.md:522, bare number) ## 7. REVERSIBILITY (Human Annotation)

### [results_FINAL.md] 7. REVERSIBILITY (Human Annotation) -- Human Judgments (stripped pairs, n=50)

*- **Filter ($/task):** waste_tokens_per_trial x price_per_token. Price from the table above (output tokens only).*

- `50` (results_FINAL.md:524, count or denominator) ### Human Judgments (stripped pairs, n=50)
- `19` (results_FINAL.md:528, percentage) | T1-preferred | 19 (38%) | 22 (44%) | 41 (41%) |
- `38` (results_FINAL.md:528, percentage) | T1-preferred | 19 (38%) | 22 (44%) | 41 (41%) |
- `22` (results_FINAL.md:528, percentage) | T1-preferred | 19 (38%) | 22 (44%) | 41 (41%) |
- `44` (results_FINAL.md:528, percentage) | T1-preferred | 19 (38%) | 22 (44%) | 41 (41%) |
- `41` (results_FINAL.md:528, percentage) | T1-preferred | 19 (38%) | 22 (44%) | 41 (41%) |
- `41` (results_FINAL.md:528, percentage) | T1-preferred | 19 (38%) | 22 (44%) | 41 (41%) |
- `13` (results_FINAL.md:529, percentage) | Revision-preferred | 13 (26%) | 19 (38%) | 32 (32%) |
- `26` (results_FINAL.md:529, percentage) | Revision-preferred | 13 (26%) | 19 (38%) | 32 (32%) |
- `19` (results_FINAL.md:529, percentage) | Revision-preferred | 13 (26%) | 19 (38%) | 32 (32%) |
- `38` (results_FINAL.md:529, percentage) | Revision-preferred | 13 (26%) | 19 (38%) | 32 (32%) |
- `32` (results_FINAL.md:529, percentage) | Revision-preferred | 13 (26%) | 19 (38%) | 32 (32%) |
- `32` (results_FINAL.md:529, percentage) | Revision-preferred | 13 (26%) | 19 (38%) | 32 (32%) |
- `18` (results_FINAL.md:530, percentage) | Tie | 18 (36%) | 9 (18%) | 27 (27%) |
- `36` (results_FINAL.md:530, percentage) | Tie | 18 (36%) | 9 (18%) | 27 (27%) |
- `9` (results_FINAL.md:530, percentage) | Tie | 18 (36%) | 9 (18%) | 27 (27%) |
- `18` (results_FINAL.md:530, percentage) | Tie | 18 (36%) | 9 (18%) | 27 (27%) |
- `27` (results_FINAL.md:530, percentage) | Tie | 18 (36%) | 9 (18%) | 27 (27%) |
- `27` (results_FINAL.md:530, percentage) | Tie | 18 (36%) | 9 (18%) | 27 (27%) |
- `19` (results_FINAL.md:531, percentage) | Non-tie T1-pref | 19/32 (59.4%) | 22/41 (53.7%) | **41/73 (56.2%)** |
- `32` (results_FINAL.md:531, percentage) | Non-tie T1-pref | 19/32 (59.4%) | 22/41 (53.7%) | **41/73 (56.2%)** |
- `59.4` (results_FINAL.md:531, percentage) | Non-tie T1-pref | 19/32 (59.4%) | 22/41 (53.7%) | **41/73 (56.2%)** |
- `22` (results_FINAL.md:531, percentage) | Non-tie T1-pref | 19/32 (59.4%) | 22/41 (53.7%) | **41/73 (56.2%)** |
- `41` (results_FINAL.md:531, percentage) | Non-tie T1-pref | 19/32 (59.4%) | 22/41 (53.7%) | **41/73 (56.2%)** |
- `53.7` (results_FINAL.md:531, percentage) | Non-tie T1-pref | 19/32 (59.4%) | 22/41 (53.7%) | **41/73 (56.2%)** |
- `41` (results_FINAL.md:531, percentage) | Non-tie T1-pref | 19/32 (59.4%) | 22/41 (53.7%) | **41/73 (56.2%)** |
- `73` (results_FINAL.md:531, percentage) | Non-tie T1-pref | 19/32 (59.4%) | 22/41 (53.7%) | **41/73 (56.2%)** |
- `56.2` (results_FINAL.md:531, percentage) | Non-tie T1-pref | 19/32 (59.4%) | 22/41 (53.7%) | **41/73 (56.2%)** |
- `95` (results_FINAL.md:532, percentage) | Bootstrap 95% CI | -- | -- | [45.2%, 67.1%] |
- `45.2` (results_FINAL.md:532, percentage) | Bootstrap 95% CI | -- | -- | [45.2%, 67.1%] |
- `67.1` (results_FINAL.md:532, percentage) | Bootstrap 95% CI | -- | -- | [45.2%, 67.1%] |
- `65` (results_FINAL.md:534, percentage) **Pre-committed bar (>=65%, CI excludes 50%): NOT CLEARED.**
- `50` (results_FINAL.md:534, percentage) **Pre-committed bar (>=65%, CI excludes 50%): NOT CLEARED.**

### [results_FINAL.md] 7. REVERSIBILITY (Human Annotation) -- Inter-Annotator Agreement

*- **Filter ($/task):** waste_tokens_per_trial x price_per_token. Price from the table above (output tokens only).*

- `3` (results_FINAL.md:540, percentage) | Raw 3-way agreement | 40/50 (80%) |
- `40` (results_FINAL.md:540, percentage) | Raw 3-way agreement | 40/50 (80%) |
- `50` (results_FINAL.md:540, percentage) | Raw 3-way agreement | 40/50 (80%) |
- `80` (results_FINAL.md:540, percentage) | Raw 3-way agreement | 40/50 (80%) |
- `0.703` (results_FINAL.md:541, reliability or effect size) | Cohen's kappa (raw) | 0.703 |
- `0.701` (results_FINAL.md:542, reliability or effect size) | Cohen's kappa (decoded) | 0.701 |
- `10` (results_FINAL.md:543, bare number) | Disagreements | 10 pairs (8 = Liam tie vs Troy decided, 1 full flip, 1 Liam tie vs Troy T1) |
- `8` (results_FINAL.md:543, bare number) | Disagreements | 10 pairs (8 = Liam tie vs Troy decided, 1 full flip, 1 Liam tie vs Troy T1) |
- `1` (results_FINAL.md:543, bare number) | Disagreements | 10 pairs (8 = Liam tie vs Troy decided, 1 full flip, 1 Liam tie vs Troy T1) |
- `1` (results_FINAL.md:543, bare number) | Disagreements | 10 pairs (8 = Liam tie vs Troy decided, 1 full flip, 1 Liam tie vs Troy T1) |

### [results_FINAL.md] 7. REVERSIBILITY (Human Annotation) -- Position & Length Bias

*- **Filter ($/task):** waste_tokens_per_trial x price_per_token. Price from the table above (output tokens only).*

- `38` (results_FINAL.md:549, percentage) | A chosen (decided pairs) | 38/73 (52.1%), CI [39.7%, 63.0%] |
- `73` (results_FINAL.md:549, percentage) | A chosen (decided pairs) | 38/73 (52.1%), CI [39.7%, 63.0%] |
- `52.1` (results_FINAL.md:549, percentage) | A chosen (decided pairs) | 38/73 (52.1%), CI [39.7%, 63.0%] |
- `39.7` (results_FINAL.md:549, percentage) | A chosen (decided pairs) | 38/73 (52.1%), CI [39.7%, 63.0%] |
- `63.0` (results_FINAL.md:549, percentage) | A chosen (decided pairs) | 38/73 (52.1%), CI [39.7%, 63.0%] |
- `40` (results_FINAL.md:550, percentage) | Longer output chosen | 40/73 (54.8%) |
- `73` (results_FINAL.md:550, percentage) | Longer output chosen | 40/73 (54.8%) |
- `54.8` (results_FINAL.md:550, percentage) | Longer output chosen | 40/73 (54.8%) |

### [results_FINAL.md] 7. REVERSIBILITY (Human Annotation) -- Model Judge Comparison

*- **Filter ($/task):** waste_tokens_per_trial x price_per_token. Price from the table above (output tokens only).*

- `50` (results_FINAL.md:556, percentage) | Model judge, UNSTRIPPED (pairwise, same 50 trials) | 45/49 (91.8%) | 1 |
- `45` (results_FINAL.md:556, percentage) | Model judge, UNSTRIPPED (pairwise, same 50 trials) | 45/49 (91.8%) | 1 |
- `49` (results_FINAL.md:556, percentage) | Model judge, UNSTRIPPED (pairwise, same 50 trials) | 45/49 (91.8%) | 1 |
- `91.8` (results_FINAL.md:556, percentage) | Model judge, UNSTRIPPED (pairwise, same 50 trials) | 45/49 (91.8%) | 1 |
- `1` (results_FINAL.md:556, percentage) | Model judge, UNSTRIPPED (pairwise, same 50 trials) | 45/49 (91.8%) | 1 |
- `720` (results_FINAL.md:557, percentage) | Model judge, UNSTRIPPED (full 720, pairwise) | 669/720 (92.9%) | -- |
- `669` (results_FINAL.md:557, percentage) | Model judge, UNSTRIPPED (full 720, pairwise) | 669/720 (92.9%) | -- |
- `720` (results_FINAL.md:557, percentage) | Model judge, UNSTRIPPED (full 720, pairwise) | 669/720 (92.9%) | -- |
- `92.9` (results_FINAL.md:557, percentage) | Model judge, UNSTRIPPED (full 720, pairwise) | 669/720 (92.9%) | -- |
- `50` (results_FINAL.md:558, percentage) | Model judge, STRIPPED (pairwise, 50 pairs) | 26/46 (56.5%) | 4 |
- `26` (results_FINAL.md:558, percentage) | Model judge, STRIPPED (pairwise, 50 pairs) | 26/46 (56.5%) | 4 |
- `46` (results_FINAL.md:558, percentage) | Model judge, STRIPPED (pairwise, 50 pairs) | 26/46 (56.5%) | 4 |
- `56.5` (results_FINAL.md:558, percentage) | Model judge, STRIPPED (pairwise, 50 pairs) | 26/46 (56.5%) | 4 |
- `4` (results_FINAL.md:558, percentage) | Model judge, STRIPPED (pairwise, 50 pairs) | 26/46 (56.5%) | 4 |
- `50` (results_FINAL.md:559, percentage) | Humans, STRIPPED (50 pairs) | 41/73 (56.2%) | 27 |
- `41` (results_FINAL.md:559, percentage) | Humans, STRIPPED (50 pairs) | 41/73 (56.2%) | 27 |
- `73` (results_FINAL.md:559, percentage) | Humans, STRIPPED (50 pairs) | 41/73 (56.2%) | 27 |
- `56.2` (results_FINAL.md:559, percentage) | Humans, STRIPPED (50 pairs) | 41/73 (56.2%) | 27 |
- `27` (results_FINAL.md:559, percentage) | Humans, STRIPPED (50 pairs) | 41/73 (56.2%) | 27 |

### [results_FINAL.md] 7. REVERSIBILITY (Human Annotation) -- Human-Judge Agreement on Stripped Content

*- **Filter ($/task):** waste_tokens_per_trial x price_per_token. Price from the table above (output tokens only).*

- `31` (results_FINAL.md:565, percentage) | Liam vs judge | 31 | 77.4% | 0.541 |
- `77.4` (results_FINAL.md:565, percentage) | Liam vs judge | 31 | 77.4% | 0.541 |
- `0.541` (results_FINAL.md:565, percentage) | Liam vs judge | 31 | 77.4% | 0.541 |
- `39` (results_FINAL.md:566, percentage) | Troy vs judge | 39 | 79.5% | 0.589 |
- `79.5` (results_FINAL.md:566, percentage) | Troy vs judge | 39 | 79.5% | 0.589 |
- `0.589` (results_FINAL.md:566, percentage) | Troy vs judge | 39 | 79.5% | 0.589 |
- `30` (results_FINAL.md:567, percentage) | Human majority vs judge | 30 | 80.0% | 0.595 |
- `80.0` (results_FINAL.md:567, percentage) | Human majority vs judge | 30 | 80.0% | 0.595 |
- `0.595` (results_FINAL.md:567, percentage) | Human majority vs judge | 30 | 80.0% | 0.595 |
- `70` (results_FINAL.md:568, percentage) | All pooled vs judge | 70 | 78.6% | **0.569** |
- `78.6` (results_FINAL.md:568, percentage) | All pooled vs judge | 70 | 78.6% | **0.569** |
- `0.569` (results_FINAL.md:568, percentage) | All pooled vs judge | 70 | 78.6% | **0.569** |
- `0.07` (results_FINAL.md:570, reliability or effect size) **vs. unstripped: kappa was -0.07 to +0.02 (near zero).**
- `0.02` (results_FINAL.md:570, reliability or effect size) **vs. unstripped: kappa was -0.07 to +0.02 (near zero).**
- `50` (results_FINAL.md:576, confidence interval) - **Filter (human judgments):** Load each annotator's 50 judgments (field `judgment` in {A, B, equivalent}). Decode via `reversibility_stripped_key.json`: if judgment matches the side where `A_is == "
- `100` (results_FINAL.md:576, confidence interval) - **Filter (human judgments):** Load each annotator's 50 judgments (field `judgment` in {A, B, equivalent}). Decode via `reversibility_stripped_key.json`: if judgment matches the side where `A_is == "
- `1000` (results_FINAL.md:576, confidence interval) - **Filter (human judgments):** Load each annotator's 50 judgments (field `judgment` in {A, B, equivalent}). Decode via `reversibility_stripped_key.json`: if judgment matches the side where `A_is == "
- `100` (results_FINAL.md:576, confidence interval) - **Filter (human judgments):** Load each annotator's 50 judgments (field `judgment` in {A, B, equivalent}). Decode via `reversibility_stripped_key.json`: if judgment matches the side where `A_is == "
- `42` (results_FINAL.md:576, confidence interval) - **Filter (human judgments):** Load each annotator's 50 judgments (field `judgment` in {A, B, equivalent}). Decode via `reversibility_stripped_key.json`: if judgment matches the side where `A_is == "
- `50` (results_FINAL.md:577, reliability or effect size) - **Filter (inter-annotator):** Cohen's kappa on the 50 pairs using 3-way labels (A/B/equivalent for raw; T1/revision/tie for decoded). Disagreements = pairs where Liam != Troy.
- `3` (results_FINAL.md:577, reliability or effect size) - **Filter (inter-annotator):** Cohen's kappa on the 50 pairs using 3-way labels (A/B/equivalent for raw; T1/revision/tie for decoded). Disagreements = pairs where Liam != Troy.
- `73` (results_FINAL.md:578, count or denominator) - **Filter (position/length bias):** Among combined decided (non-tie) judgments (n=73), count how many chose output A vs B (position bias). For length: compare character counts of chosen vs unchosen o

### [results_FINAL.md] 8. META-WRAPPING ASYMMETRY

*- **Filter (model judge):** `judge_stripped_pairwise.json` has fields `pick` (A/B/tie) and `pair_id`. Decode via same key. Agreement with humans: for each (annotator, pair) where both annotator and judge gave non-tie decisions, compare decoded labels. Kappa computed on these matched pairs. Pooled = *

- `8` (results_FINAL.md:583, bare number) ## 8. META-WRAPPING ASYMMETRY
- `38` (results_FINAL.md:587, percentage) | Revision (T2-T5) | 38/50 (76%) | 24/50 (48%) | **42/50 (84%)** |
- `50` (results_FINAL.md:587, percentage) | Revision (T2-T5) | 38/50 (76%) | 24/50 (48%) | **42/50 (84%)** |
- `76` (results_FINAL.md:587, percentage) | Revision (T2-T5) | 38/50 (76%) | 24/50 (48%) | **42/50 (84%)** |
- `24` (results_FINAL.md:587, percentage) | Revision (T2-T5) | 38/50 (76%) | 24/50 (48%) | **42/50 (84%)** |
- `50` (results_FINAL.md:587, percentage) | Revision (T2-T5) | 38/50 (76%) | 24/50 (48%) | **42/50 (84%)** |
- `48` (results_FINAL.md:587, percentage) | Revision (T2-T5) | 38/50 (76%) | 24/50 (48%) | **42/50 (84%)** |
- `42` (results_FINAL.md:587, percentage) | Revision (T2-T5) | 38/50 (76%) | 24/50 (48%) | **42/50 (84%)** |
- `50` (results_FINAL.md:587, percentage) | Revision (T2-T5) | 38/50 (76%) | 24/50 (48%) | **42/50 (84%)** |
- `84` (results_FINAL.md:587, percentage) | Revision (T2-T5) | 38/50 (76%) | 24/50 (48%) | **42/50 (84%)** |
- `4` (results_FINAL.md:588, percentage) | T1 | 4/50 (8%) | 5/50 (10%) | **7/50 (14%)** |
- `50` (results_FINAL.md:588, percentage) | T1 | 4/50 (8%) | 5/50 (10%) | **7/50 (14%)** |
- `8` (results_FINAL.md:588, percentage) | T1 | 4/50 (8%) | 5/50 (10%) | **7/50 (14%)** |
- `5` (results_FINAL.md:588, percentage) | T1 | 4/50 (8%) | 5/50 (10%) | **7/50 (14%)** |
- `50` (results_FINAL.md:588, percentage) | T1 | 4/50 (8%) | 5/50 (10%) | **7/50 (14%)** |
- `10` (results_FINAL.md:588, percentage) | T1 | 4/50 (8%) | 5/50 (10%) | **7/50 (14%)** |
- `7` (results_FINAL.md:588, percentage) | T1 | 4/50 (8%) | 5/50 (10%) | **7/50 (14%)** |
- `50` (results_FINAL.md:588, percentage) | T1 | 4/50 (8%) | 5/50 (10%) | **7/50 (14%)** |
- `14` (results_FINAL.md:588, percentage) | T1 | 4/50 (8%) | 5/50 (10%) | **7/50 (14%)** |
- `14` (results_FINAL.md:591, percentage) - T1: 14%, T2: 92%, T3: 85%, T4: 79%, T5: 68%
- `92` (results_FINAL.md:591, percentage) - T1: 14%, T2: 92%, T3: 85%, T4: 79%, T5: 68%
- `85` (results_FINAL.md:591, percentage) - T1: 14%, T2: 92%, T3: 85%, T4: 79%, T5: 68%
- `79` (results_FINAL.md:591, percentage) - T1: 14%, T2: 92%, T3: 85%, T4: 79%, T5: 68%
- `68` (results_FINAL.md:591, percentage) - T1: 14%, T2: 92%, T3: 85%, T4: 79%, T5: 68%
- `56.5` (results_FINAL.md:593, percentage) **This asymmetry inflated the model judge's T1-preference from 56.5% (stripped) to 91.8% (unstripped) on the same 50 pairs.**
- `91.8` (results_FINAL.md:593, percentage) **This asymmetry inflated the model judge's T1-preference from 56.5% (stripped) to 91.8% (unstripped) on the same 50 pairs.**
- `50` (results_FINAL.md:593, percentage) **This asymmetry inflated the model judge's T1-preference from 56.5% (stripped) to 91.8% (unstripped) on the same 50 pairs.**
- `50` (results_FINAL.md:596, bare number) - **Filter:** The 50 unstripped reversibility pairs (`reversibility_human_pairs.json`). For each pair, decode T1 vs revision side via `reversibility_human_key.json`. Apply regex preamble/postamble det
- `300` (results_FINAL.md:596, bare number) - **Filter:** The 50 unstripped reversibility pairs (`reversibility_human_pairs.json`). For each pair, decode T1 vs revision side via `reversibility_human_key.json`. Apply regex preamble/postamble det
- `400` (results_FINAL.md:596, bare number) - **Filter:** The 50 unstripped reversibility pairs (`reversibility_human_pairs.json`). For each pair, decode T1 vs revision side via `reversibility_human_key.json`. Apply regex preamble/postamble det
- `1` (results_FINAL.md:596, bare number) - **Filter:** The 50 unstripped reversibility pairs (`reversibility_human_pairs.json`). For each pair, decode T1 vs revision side via `reversibility_human_key.json`. Apply regex preamble/postamble det
- `50` (results_FINAL.md:597, bare number) - **Scope:** All counts are from the 50 unstripped reversibility pairs, stored in `meta_wrapping_asymmetry.json`. Raw counts: revision preamble=38, postamble=24, either=42; T1 preamble=4, postamble=5,
- `38` (results_FINAL.md:597, bare number) - **Scope:** All counts are from the 50 unstripped reversibility pairs, stored in `meta_wrapping_asymmetry.json`. Raw counts: revision preamble=38, postamble=24, either=42; T1 preamble=4, postamble=5,
- `24` (results_FINAL.md:597, bare number) - **Scope:** All counts are from the 50 unstripped reversibility pairs, stored in `meta_wrapping_asymmetry.json`. Raw counts: revision preamble=38, postamble=24, either=42; T1 preamble=4, postamble=5,
- `42` (results_FINAL.md:597, bare number) - **Scope:** All counts are from the 50 unstripped reversibility pairs, stored in `meta_wrapping_asymmetry.json`. Raw counts: revision preamble=38, postamble=24, either=42; T1 preamble=4, postamble=5,
- `4` (results_FINAL.md:597, bare number) - **Scope:** All counts are from the 50 unstripped reversibility pairs, stored in `meta_wrapping_asymmetry.json`. Raw counts: revision preamble=38, postamble=24, either=42; T1 preamble=4, postamble=5,
- `5` (results_FINAL.md:597, bare number) - **Scope:** All counts are from the 50 unstripped reversibility pairs, stored in `meta_wrapping_asymmetry.json`. Raw counts: revision preamble=38, postamble=24, either=42; T1 preamble=4, postamble=5,
- `7` (results_FINAL.md:597, bare number) - **Scope:** All counts are from the 50 unstripped reversibility pairs, stored in `meta_wrapping_asymmetry.json`. Raw counts: revision preamble=38, postamble=24, either=42; T1 preamble=4, postamble=5,
- `2026` (results_FINAL.md:598, percentage) - **FLAG RESOLVED 2026-09-06, DO NOT CITE.** The per-turn breakdown (T1:14%, T2:92%, T3:85%,
- `09` (results_FINAL.md:598, percentage) - **FLAG RESOLVED 2026-09-06, DO NOT CITE.** The per-turn breakdown (T1:14%, T2:92%, T3:85%,
- `06` (results_FINAL.md:598, percentage) - **FLAG RESOLVED 2026-09-06, DO NOT CITE.** The per-turn breakdown (T1:14%, T2:92%, T3:85%,
- `14` (results_FINAL.md:598, percentage) - **FLAG RESOLVED 2026-09-06, DO NOT CITE.** The per-turn breakdown (T1:14%, T2:92%, T3:85%,
- `92` (results_FINAL.md:598, percentage) - **FLAG RESOLVED 2026-09-06, DO NOT CITE.** The per-turn breakdown (T1:14%, T2:92%, T3:85%,
- `85` (results_FINAL.md:598, percentage) - **FLAG RESOLVED 2026-09-06, DO NOT CITE.** The per-turn breakdown (T1:14%, T2:92%, T3:85%,
- `79` (results_FINAL.md:599, percentage) T4:79%, T5:68%) does not reproduce from any of 18 candidate scopes tested. Its T1 matches the
- `68` (results_FINAL.md:599, percentage) T4:79%, T5:68%) does not reproduce from any of 18 candidate scopes tested. Its T1 matches the
- `18` (results_FINAL.md:599, percentage) T4:79%, T5:68%) does not reproduce from any of 18 candidate scopes tested. Its T1 matches the
- `50` (results_FINAL.md:600, bare number) 50-pair scope, its T2 matches GENUINE-only, and its T5 matches the full 720-trial corpus, so
- `720` (results_FINAL.md:600, bare number) 50-pair scope, its T2 matches GENUINE-only, and its T5 matches the full 720-trial corpus, so
- `2` (results_FINAL.md:603, bare number) `paper/reference/stats_08_meta_commentary.md` section 2.

### [results_FINAL.md] 9. REVERSIBILITY -- STRATIFIED

*- **Filter:** The 50 unstripped reversibility pairs (`reversibility_human_pairs.json`). For each pair, decode T1 vs revision side via `reversibility_human_key.json`. Apply regex preamble/postamble detectors (patterns in `audit_meta_commentary.py`: PREAMBLE_PATTERNS checked against first 300 chars, P*

- `9` (results_FINAL.md:607, bare number) ## 9. REVERSIBILITY -- STRATIFIED

### [results_FINAL.md] 9. REVERSIBILITY -- STRATIFIED -- By Last Revision Turn (non-tie T1-preference, combined annotators)

*- **Filter:** The 50 unstripped reversibility pairs (`reversibility_human_pairs.json`). For each pair, decode T1 vs revision side via `reversibility_human_key.json`. Apply regex preamble/postamble detectors (patterns in `audit_meta_commentary.py`: PREAMBLE_PATTERNS checked against first 300 chars, P*

- `9` (results_FINAL.md:613, percentage) | T2 | 9 | 17 | 52.9% |
- `17` (results_FINAL.md:613, percentage) | T2 | 9 | 17 | 52.9% |
- `52.9` (results_FINAL.md:613, percentage) | T2 | 9 | 17 | 52.9% |
- `11` (results_FINAL.md:614, percentage) | T3 | 11 | 21 | 52.4% |
- `21` (results_FINAL.md:614, percentage) | T3 | 11 | 21 | 52.4% |
- `52.4` (results_FINAL.md:614, percentage) | T3 | 11 | 21 | 52.4% |
- `17` (results_FINAL.md:615, percentage) | T4 | 17 | 24 | **70.8%** |
- `24` (results_FINAL.md:615, percentage) | T4 | 17 | 24 | **70.8%** |
- `70.8` (results_FINAL.md:615, percentage) | T4 | 17 | 24 | **70.8%** |
- `4` (results_FINAL.md:616, percentage) | T5 | 4 | 11 | 36.4% |
- `11` (results_FINAL.md:616, percentage) | T5 | 4 | 11 | 36.4% |
- `36.4` (results_FINAL.md:616, percentage) | T5 | 4 | 11 | 36.4% |

### [results_FINAL.md] 9. REVERSIBILITY -- STRATIFIED -- By Domain

*- **Filter:** The 50 unstripped reversibility pairs (`reversibility_human_pairs.json`). For each pair, decode T1 vs revision side via `reversibility_human_key.json`. Apply regex preamble/postamble detectors (patterns in `audit_meta_commentary.py`: PREAMBLE_PATTERNS checked against first 300 chars, P*

- `13` (results_FINAL.md:622, percentage) | writing | 13 | 14 | **92.9%** |
- `14` (results_FINAL.md:622, percentage) | writing | 13 | 14 | **92.9%** |
- `92.9` (results_FINAL.md:622, percentage) | writing | 13 | 14 | **92.9%** |
- `8` (results_FINAL.md:623, percentage) | analysis | 8 | 12 | 66.7% |
- `12` (results_FINAL.md:623, percentage) | analysis | 8 | 12 | 66.7% |
- `66.7` (results_FINAL.md:623, percentage) | analysis | 8 | 12 | 66.7% |
- `9` (results_FINAL.md:624, percentage) | code | 9 | 20 | 45.0% |
- `20` (results_FINAL.md:624, percentage) | code | 9 | 20 | 45.0% |
- `45.0` (results_FINAL.md:624, percentage) | code | 9 | 20 | 45.0% |
- `8` (results_FINAL.md:625, percentage) | creative | 8 | 19 | 42.1% |
- `19` (results_FINAL.md:625, percentage) | creative | 8 | 19 | 42.1% |
- `42.1` (results_FINAL.md:625, percentage) | creative | 8 | 19 | 42.1% |
- `3` (results_FINAL.md:626, percentage) | data_logic | 3 | 8 | 37.5% |
- `8` (results_FINAL.md:626, percentage) | data_logic | 3 | 8 | 37.5% |
- `37.5` (results_FINAL.md:626, percentage) | data_logic | 3 | 8 | 37.5% |
- `100` (results_FINAL.md:628, bare number) - **Filter (by turn):** From `reversibility_stripped_key.json`, field `last_rev_turn` gives the turn of the revision side. Group the 100 pooled human non-tie decisions (combined annotators) by `last_r

### [results_FINAL.md] 10. SELF-REFLECTION

*- **Filter (by domain):** Same pooled non-tie decisions, grouped by `domain` field from `reversibility_stripped_key.json`.*

- `10` (results_FINAL.md:633, bare number) ## 10. SELF-REFLECTION
- `720` (results_FINAL.md:637, bare number) | N | 720 |
- `2.44` (results_FINAL.md:638, mean or delta) | Mean recommended turn | 2.44 (SD=1.39) |
- `1.39` (results_FINAL.md:638, mean or delta) | Mean recommended turn | 2.44 (SD=1.39) |
- `288` (results_FINAL.md:639, percentage) | Recommend T1 | 288/720 (40.0%) |
- `720` (results_FINAL.md:639, percentage) | Recommend T1 | 288/720 (40.0%) |
- `40.0` (results_FINAL.md:639, percentage) | Recommend T1 | 288/720 (40.0%) |
- `90.7` (results_FINAL.md:640, percentage) | Recommend not-last | 90.7% |
- `288` (results_FINAL.md:641, bare number) | Distribution | T1:288, T2:76, T3:176, T4:113, T5:67 |
- `76` (results_FINAL.md:641, bare number) | Distribution | T1:288, T2:76, T3:176, T4:113, T5:67 |
- `176` (results_FINAL.md:641, bare number) | Distribution | T1:288, T2:76, T3:176, T4:113, T5:67 |
- `113` (results_FINAL.md:641, bare number) | Distribution | T1:288, T2:76, T3:176, T4:113, T5:67 |
- `67` (results_FINAL.md:641, bare number) | Distribution | T1:288, T2:76, T3:176, T4:113, T5:67 |
- `720` (results_FINAL.md:645, bare number) - **Filter:** All 720 records in `self_reflection_results.jsonl`. Field `recommended_turn` (integer 1-5). Mean, SD, and frequency distribution computed over all 720. "Recommend not-last" = records whe
- `1` (results_FINAL.md:645, bare number) - **Filter:** All 720 records in `self_reflection_results.jsonl`. Field `recommended_turn` (integer 1-5). Mean, SD, and frequency distribution computed over all 720. "Recommend not-last" = records whe
- `5` (results_FINAL.md:645, bare number) - **Filter:** All 720 records in `self_reflection_results.jsonl`. Field `recommended_turn` (integer 1-5). Mean, SD, and frequency distribution computed over all 720. "Recommend not-last" = records whe
- `720` (results_FINAL.md:645, bare number) - **Filter:** All 720 records in `self_reflection_results.jsonl`. Field `recommended_turn` (integer 1-5). Mean, SD, and frequency distribution computed over all 720. "Recommend not-last" = records whe
- `5` (results_FINAL.md:645, bare number) - **Filter:** All 720 records in `self_reflection_results.jsonl`. Field `recommended_turn` (integer 1-5). Mean, SD, and frequency distribution computed over all 720. "Recommend not-last" = records whe

### [results_FINAL.md] 10. SELF-REFLECTION -- 10b. Per-domain decline, paired basis (added 2026-09-20)

*- **Filter:** All 720 records in `self_reflection_results.jsonl`. Field `recommended_turn` (integer 1-5). Mean, SD, and frequency distribution computed over all 720. "Recommend not-last" = records where `recommended_turn != 5` (since T5 was the final turn in the trial).*

- `2026` (results_FINAL.md:649, bare number) ### 10b. Per-domain decline, paired basis (added 2026-09-20)
- `09` (results_FINAL.md:649, bare number) ### 10b. Per-domain decline, paired basis (added 2026-09-20)
- `20` (results_FINAL.md:649, bare number) ### 10b. Per-domain decline, paired basis (added 2026-09-20)
- `5` (results_FINAL.md:653, bare number) every trial in the domain, while the tested T1 mean is only the trials reaching Turn 5.
- `1.16` (results_FINAL.md:657, mean or delta) | analysis | -1.16 | **-0.94** | 0.003 | 17 |
- `0.94` (results_FINAL.md:657, mean or delta) | analysis | -1.16 | **-0.94** | 0.003 | 17 |
- `0.003` (results_FINAL.md:657, mean or delta) | analysis | -1.16 | **-0.94** | 0.003 | 17 |
- `17` (results_FINAL.md:657, mean or delta) | analysis | -1.16 | **-0.94** | 0.003 | 17 |
- `1.05` (results_FINAL.md:658, mean or delta) | code | -1.05 | **-0.93** | 0.003 | 30 |
- `0.93` (results_FINAL.md:658, mean or delta) | code | -1.05 | **-0.93** | 0.003 | 30 |
- `0.003` (results_FINAL.md:658, mean or delta) | code | -1.05 | **-0.93** | 0.003 | 30 |
- `30` (results_FINAL.md:658, mean or delta) | code | -1.05 | **-0.93** | 0.003 | 30 |
- `0.82` (results_FINAL.md:659, mean or delta) | creative | -0.82 | **-0.58** | 0.031 | 19 |
- `0.58` (results_FINAL.md:659, mean or delta) | creative | -0.82 | **-0.58** | 0.031 | 19 |
- `0.031` (results_FINAL.md:659, mean or delta) | creative | -0.82 | **-0.58** | 0.031 | 19 |
- `19` (results_FINAL.md:659, mean or delta) | creative | -0.82 | **-0.58** | 0.031 | 19 |
- `1.01` (results_FINAL.md:660, mean or delta) | data_logic | -1.01 | **-0.53** | 0.058 | 17 |
- `0.53` (results_FINAL.md:660, mean or delta) | data_logic | -1.01 | **-0.53** | 0.058 | 17 |
- `0.058` (results_FINAL.md:660, mean or delta) | data_logic | -1.01 | **-0.53** | 0.058 | 17 |
- `17` (results_FINAL.md:660, mean or delta) | data_logic | -1.01 | **-0.53** | 0.058 | 17 |
- `1.06` (results_FINAL.md:661, mean or delta) | writing | -1.06 | **-0.77** | 0.008 | 13 |
- `0.77` (results_FINAL.md:661, mean or delta) | writing | -1.06 | **-0.77** | 0.008 | 13 |
- `0.008` (results_FINAL.md:661, mean or delta) | writing | -1.06 | **-0.77** | 0.008 | 13 |
- `13` (results_FINAL.md:661, mean or delta) | writing | -1.06 | **-0.77** | 0.008 | 13 |
- `5` (results_FINAL.md:663, bare number) - **Filter (exact):** trials whose Turn-5 label is GENUINE in `genuine_meta_labels.jsonl`,
- `1` (results_FINAL.md:664, bare number) with stripped levels at turns 1 and 5 from `stripped_rescore_full.jsonl`, 6 -> 2 recode
- `5` (results_FINAL.md:664, bare number) with stripped levels at turns 1 and 5 from `stripped_rescore_full.jsonl`, 6 -> 2 recode
- `6` (results_FINAL.md:664, bare number) with stripped levels at turns 1 and 5 from `stripped_rescore_full.jsonl`, 6 -> 2 recode
- `2` (results_FINAL.md:664, bare number) with stripped levels at turns 1 and 5 from `stripped_rescore_full.jsonl`, 6 -> 2 recode
- `1.01` (results_FINAL.md:667, mean or delta) - data_logic was the worst affected: printed as -1.01 against a tested -0.53, an overstatement
- `0.53` (results_FINAL.md:667, mean or delta) - data_logic was the worst affected: printed as -1.01 against a tested -0.53, an overstatement
- `91` (results_FINAL.md:668, percentage) of 91%. Signs and significance are unchanged for every domain, so no conclusion moves.
- `10` (results_FINAL.md:669, bare number) - Section 10's own filter line records the unpaired basis ("T1 = all 144 per domain, T5 =
- `144` (results_FINAL.md:669, bare number) - Section 10's own filter line records the unpaired basis ("T1 = all 144 per domain, T5 =

### [results_FINAL.md] 11. RELIABILITY

*- **Filter (exact):** trials whose Turn-5 label is GENUINE in `genuine_meta_labels.jsonl`,*

- `11` (results_FINAL.md:674, bare number) ## 11. RELIABILITY

### [results_FINAL.md] 11. RELIABILITY -- Human Inter-Rater Agreement (3 raters, 64 calibration items, 6->2 recode)

*- **Filter (exact):** trials whose Turn-5 label is GENUINE in `genuine_meta_labels.jsonl`,*

- `3` (results_FINAL.md:676, bare number) ### Human Inter-Rater Agreement (3 raters, 64 calibration items, 6->2 recode)
- `64` (results_FINAL.md:676, bare number) ### Human Inter-Rater Agreement (3 raters, 64 calibration items, 6->2 recode)
- `6` (results_FINAL.md:676, bare number) ### Human Inter-Rater Agreement (3 raters, 64 calibration items, 6->2 recode)
- `2` (results_FINAL.md:676, bare number) ### Human Inter-Rater Agreement (3 raters, 64 calibration items, 6->2 recode)
- `4` (results_FINAL.md:678, bare number) | Pair | QW Kappa | Binary (>=4) | Within-1 |
- `1` (results_FINAL.md:678, bare number) | Pair | QW Kappa | Binary (>=4) | Within-1 |
- `0.406` (results_FINAL.md:680, percentage) | Liam-Troy | 0.406 | 49/64 (76.6%) | 52/64 (81.2%) |
- `49` (results_FINAL.md:680, percentage) | Liam-Troy | 0.406 | 49/64 (76.6%) | 52/64 (81.2%) |
- `64` (results_FINAL.md:680, percentage) | Liam-Troy | 0.406 | 49/64 (76.6%) | 52/64 (81.2%) |
- `76.6` (results_FINAL.md:680, percentage) | Liam-Troy | 0.406 | 49/64 (76.6%) | 52/64 (81.2%) |
- `52` (results_FINAL.md:680, percentage) | Liam-Troy | 0.406 | 49/64 (76.6%) | 52/64 (81.2%) |
- `64` (results_FINAL.md:680, percentage) | Liam-Troy | 0.406 | 49/64 (76.6%) | 52/64 (81.2%) |
- `81.2` (results_FINAL.md:680, percentage) | Liam-Troy | 0.406 | 49/64 (76.6%) | 52/64 (81.2%) |
- `0.578` (results_FINAL.md:681, percentage) | Liam-Sophie | **0.578** | 50/64 (78.1%) | 61/64 (95.3%) |
- `50` (results_FINAL.md:681, percentage) | Liam-Sophie | **0.578** | 50/64 (78.1%) | 61/64 (95.3%) |
- `64` (results_FINAL.md:681, percentage) | Liam-Sophie | **0.578** | 50/64 (78.1%) | 61/64 (95.3%) |
- `78.1` (results_FINAL.md:681, percentage) | Liam-Sophie | **0.578** | 50/64 (78.1%) | 61/64 (95.3%) |
- `61` (results_FINAL.md:681, percentage) | Liam-Sophie | **0.578** | 50/64 (78.1%) | 61/64 (95.3%) |
- `64` (results_FINAL.md:681, percentage) | Liam-Sophie | **0.578** | 50/64 (78.1%) | 61/64 (95.3%) |
- `95.3` (results_FINAL.md:681, percentage) | Liam-Sophie | **0.578** | 50/64 (78.1%) | 61/64 (95.3%) |
- `0.603` (results_FINAL.md:682, percentage) | Sophie-Troy | **0.603** | 53/64 (82.8%) | 56/64 (87.5%) |
- `53` (results_FINAL.md:682, percentage) | Sophie-Troy | **0.603** | 53/64 (82.8%) | 56/64 (87.5%) |
- `64` (results_FINAL.md:682, percentage) | Sophie-Troy | **0.603** | 53/64 (82.8%) | 56/64 (87.5%) |
- `82.8` (results_FINAL.md:682, percentage) | Sophie-Troy | **0.603** | 53/64 (82.8%) | 56/64 (87.5%) |
- `56` (results_FINAL.md:682, percentage) | Sophie-Troy | **0.603** | 53/64 (82.8%) | 56/64 (87.5%) |
- `64` (results_FINAL.md:682, percentage) | Sophie-Troy | **0.603** | 53/64 (82.8%) | 56/64 (87.5%) |
- `87.5` (results_FINAL.md:682, percentage) | Sophie-Troy | **0.603** | 53/64 (82.8%) | 56/64 (87.5%) |
- `3` (results_FINAL.md:686, mean or delta) | Krippendorff's alpha (3-rater, interval) | **0.529** |
- `0.529` (results_FINAL.md:686, mean or delta) | Krippendorff's alpha (3-rater, interval) | **0.529** |
- `64` (results_FINAL.md:688, reliability or effect size) Note: Sophie re-rated all 64 items (v2) after rubric clarification. Sophie v2 uses a 1-5 scale (no level 6 assigned). Liam-Troy QW kappa of 0.406 supersedes the previously reported 0.228, which was li
- `1` (results_FINAL.md:688, reliability or effect size) Note: Sophie re-rated all 64 items (v2) after rubric clarification. Sophie v2 uses a 1-5 scale (no level 6 assigned). Liam-Troy QW kappa of 0.406 supersedes the previously reported 0.228, which was li
- `5` (results_FINAL.md:688, reliability or effect size) Note: Sophie re-rated all 64 items (v2) after rubric clarification. Sophie v2 uses a 1-5 scale (no level 6 assigned). Liam-Troy QW kappa of 0.406 supersedes the previously reported 0.228, which was li
- `6` (results_FINAL.md:688, reliability or effect size) Note: Sophie re-rated all 64 items (v2) after rubric clarification. Sophie v2 uses a 1-5 scale (no level 6 assigned). Liam-Troy QW kappa of 0.406 supersedes the previously reported 0.228, which was li
- `0.406` (results_FINAL.md:688, reliability or effect size) Note: Sophie re-rated all 64 items (v2) after rubric clarification. Sophie v2 uses a 1-5 scale (no level 6 assigned). Liam-Troy QW kappa of 0.406 supersedes the previously reported 0.228, which was li
- `0.228` (results_FINAL.md:688, reliability or effect size) Note: Sophie re-rated all 64 items (v2) after rubric clarification. Sophie v2 uses a 1-5 scale (no level 6 assigned). Liam-Troy QW kappa of 0.406 supersedes the previously reported 0.228, which was li
- `1` (results_FINAL.md:688, reliability or effect size) Note: Sophie re-rated all 64 items (v2) after rubric clarification. Sophie v2 uses a 1-5 scale (no level 6 assigned). Liam-Troy QW kappa of 0.406 supersedes the previously reported 0.228, which was li
- `6` (results_FINAL.md:688, reliability or effect size) Note: Sophie re-rated all 64 items (v2) after rubric clarification. Sophie v2 uses a 1-5 scale (no level 6 assigned). Liam-Troy QW kappa of 0.406 supersedes the previously reported 0.228, which was li
- `6` (results_FINAL.md:688, reliability or effect size) Note: Sophie re-rated all 64 items (v2) after rubric clarification. Sophie v2 uses a 1-5 scale (no level 6 assigned). Liam-Troy QW kappa of 0.406 supersedes the previously reported 0.228, which was li
- `2` (results_FINAL.md:688, reliability or effect size) Note: Sophie re-rated all 64 items (v2) after rubric clarification. Sophie v2 uses a 1-5 scale (no level 6 assigned). Liam-Troy QW kappa of 0.406 supersedes the previously reported 0.228, which was li

### [results_FINAL.md] 11. RELIABILITY -- Judge-Human Agreement

*- **Filter (exact):** trials whose Turn-5 label is GENUINE in `genuine_meta_labels.jsonl`,*

- `0.505` (results_FINAL.md:694, p-value) | Judge-human Spearman r | 0.505 (p<0.001) | `selected_judge.json` |
- `0.001` (results_FINAL.md:694, p-value) | Judge-human Spearman r | 0.505 (p<0.001) | `selected_judge.json` |
- `0.526` (results_FINAL.md:695, reliability or effect size) | Judge-human QW kappa | 0.526 | `judge_calibration.jsonl` |
- `64` (results_FINAL.md:698, reliability or effect size) - **Filter (human QW kappas):** All three raters' `level` fields on the 64 shared calibration items (all 64 items overlap across all 3 raters). Recode level 6 -> 2 before computing. Quadratic-weighted
- `64` (results_FINAL.md:698, reliability or effect size) - **Filter (human QW kappas):** All three raters' `level` fields on the 64 shared calibration items (all 64 items overlap across all 3 raters). Recode level 6 -> 2 before computing. Quadratic-weighted
- `3` (results_FINAL.md:698, reliability or effect size) - **Filter (human QW kappas):** All three raters' `level` fields on the 64 shared calibration items (all 64 items overlap across all 3 raters). Recode level 6 -> 2 before computing. Quadratic-weighted
- `6` (results_FINAL.md:698, reliability or effect size) - **Filter (human QW kappas):** All three raters' `level` fields on the 64 shared calibration items (all 64 items overlap across all 3 raters). Recode level 6 -> 2 before computing. Quadratic-weighted
- `2` (results_FINAL.md:698, reliability or effect size) - **Filter (human QW kappas):** All three raters' `level` fields on the 64 shared calibration items (all 64 items overlap across all 3 raters). Recode level 6 -> 2 before computing. Quadratic-weighted
- `1` (results_FINAL.md:698, reliability or effect size) - **Filter (human QW kappas):** All three raters' `level` fields on the 64 shared calibration items (all 64 items overlap across all 3 raters). Recode level 6 -> 2 before computing. Quadratic-weighted
- `5` (results_FINAL.md:698, reliability or effect size) - **Filter (human QW kappas):** All three raters' `level` fields on the 64 shared calibration items (all 64 items overlap across all 3 raters). Recode level 6 -> 2 before computing. Quadratic-weighted
- `4` (results_FINAL.md:698, reliability or effect size) - **Filter (human QW kappas):** All three raters' `level` fields on the 64 shared calibration items (all 64 items overlap across all 3 raters). Recode level 6 -> 2 before computing. Quadratic-weighted
- `4` (results_FINAL.md:698, reliability or effect size) - **Filter (human QW kappas):** All three raters' `level` fields on the 64 shared calibration items (all 64 items overlap across all 3 raters). Recode level 6 -> 2 before computing. Quadratic-weighted
- `1` (results_FINAL.md:698, reliability or effect size) - **Filter (human QW kappas):** All three raters' `level` fields on the 64 shared calibration items (all 64 items overlap across all 3 raters). Recode level 6 -> 2 before computing. Quadratic-weighted
- `1` (results_FINAL.md:698, reliability or effect size) - **Filter (human QW kappas):** All three raters' `level` fields on the 64 shared calibration items (all 64 items overlap across all 3 raters). Recode level 6 -> 2 before computing. Quadratic-weighted
- `3` (results_FINAL.md:699, bare number) - **Filter (Krippendorff's alpha):** Interval-scale alpha over the 3 x 64 rating matrix (after 6->2 recode).
- `64` (results_FINAL.md:699, bare number) - **Filter (Krippendorff's alpha):** Interval-scale alpha over the 3 x 64 rating matrix (after 6->2 recode).
- `6` (results_FINAL.md:699, bare number) - **Filter (Krippendorff's alpha):** Interval-scale alpha over the 3 x 64 rating matrix (after 6->2 recode).
- `2` (results_FINAL.md:699, bare number) - **Filter (Krippendorff's alpha):** Interval-scale alpha over the 3 x 64 rating matrix (after 6->2 recode).
- `4` (results_FINAL.md:700, reliability or effect size) - **Filter (Judge-human Spearman r):** From `selected_judge.json`, Claude Sonnet 4 scores vs averaged human ratings on the 64 calibration samples.
- `64` (results_FINAL.md:700, reliability or effect size) - **Filter (Judge-human Spearman r):** From `selected_judge.json`, Claude Sonnet 4 scores vs averaged human ratings on the 64 calibration samples.
- `4` (results_FINAL.md:701, reliability or effect size) - **Filter (Judge-human QW kappa):** From `judge_calibration.jsonl`, quadratic-weighted kappa between Claude Sonnet 4 scores and averaged human ratings on the 64 calibration samples.
- `64` (results_FINAL.md:701, reliability or effect size) - **Filter (Judge-human QW kappa):** From `judge_calibration.jsonl`, quadratic-weighted kappa between Claude Sonnet 4 scores and averaged human ratings on the 64 calibration samples.

### [results_FINAL.md] 12. UNCHANGED NUMBERS (not affected by classifier correction)

*- **Filter (Judge-human QW kappa):** From `judge_calibration.jsonl`, quadratic-weighted kappa between Claude Sonnet 4 scores and averaged human ratings on the 64 calibration samples.*

- `12` (results_FINAL.md:705, bare number) ## 12. UNCHANGED NUMBERS (not affected by classifier correction)
- `1` (results_FINAL.md:707, percentage) - Study 1: 3,840 trials, 99.9% vs 23.2% gate, all numbers unchanged
- `3,840` (results_FINAL.md:707, percentage) - Study 1: 3,840 trials, 99.9% vs 23.2% gate, all numbers unchanged
- `99.9` (results_FINAL.md:707, percentage) - Study 1: 3,840 trials, 99.9% vs 23.2% gate, all numbers unchanged
- `23.2` (results_FINAL.md:707, percentage) - Study 1: 3,840 trials, 99.9% vs 23.2% gate, all numbers unchanged
- `2` (results_FINAL.md:708, bare number) - Study 2: 1,728 trials, momentum numbers unchanged
- `1,728` (results_FINAL.md:708, bare number) - Study 2: 1,728 trials, momentum numbers unchanged
- `2.44` (results_FINAL.md:709, mean or delta) - Self-reflection: mean 2.44, all numbers unchanged
- `87.6` (results_FINAL.md:710, percentage) - T1 sufficiency rate: 87.6% (was "93.3%" in paper -- NEED TO VERIFY which denominator)
- `93.3` (results_FINAL.md:710, percentage) - T1 sufficiency rate: 87.6% (was "93.3%" in paper -- NEED TO VERIFY which denominator)
- `2` (results_FINAL.md:711, bare number) - DRP = Turn 2 for all degrading models: unchanged conceptually, but per-model trajectories need recomputation
- `0.97` (results_FINAL.md:712, mean or delta) - Edit ratio 0.97: unchanged (computed on raw text, not affected by classifier)

### [results_FINAL.md] 13. BENCHMARK STABILITY OVER THE 40 TASKS (added 2026-09-18)

*- **Filter (Judge-human QW kappa):** From `judge_calibration.jsonl`, quadratic-weighted kappa between Claude Sonnet 4 scores and averaged human ratings on the 64 calibration samples.*

- `13` (results_FINAL.md:716, bare number) ## 13. BENCHMARK STABILITY OVER THE 40 TASKS (added 2026-09-18)
- `40` (results_FINAL.md:716, bare number) ## 13. BENCHMARK STABILITY OVER THE 40 TASKS (added 2026-09-18)
- `2026` (results_FINAL.md:716, bare number) ## 13. BENCHMARK STABILITY OVER THE 40 TASKS (added 2026-09-18)
- `09` (results_FINAL.md:716, bare number) ## 13. BENCHMARK STABILITY OVER THE 40 TASKS (added 2026-09-18)
- `18` (results_FINAL.md:716, bare number) ## 13. BENCHMARK STABILITY OVER THE 40 TASKS (added 2026-09-18)
- `40` (results_FINAL.md:718, bare number) Is a 40-task corpus enough to rank six models on a stable score? The 40 tasks are split
- `40` (results_FINAL.md:718, bare number) Is a 40-task corpus enough to rank six models on a stable score? The 40 tasks are split
- `720` (results_FINAL.md:724, bare number) - **Sample:** unchanged. The same 720 trials (6 models x 40 tasks x 3 runs), the same
- `6` (results_FINAL.md:724, bare number) - **Sample:** unchanged. The same 720 trials (6 models x 40 tasks x 3 runs), the same
- `40` (results_FINAL.md:724, bare number) - **Sample:** unchanged. The same 720 trials (6 models x 40 tasks x 3 runs), the same
- `3` (results_FINAL.md:724, bare number) - **Sample:** unchanged. The same 720 trials (6 models x 40 tasks x 3 runs), the same
- `6` (results_FINAL.md:725, bare number) GENUINE/META labels from the validated classifier, the same 6 -> 2 recode. No sample
- `2` (results_FINAL.md:725, bare number) GENUINE/META labels from the validated classifier, the same 6 -> 2 recode. No sample
- `3` (results_FINAL.md:728, bare number) cell's 3 trials, then summed over the tasks in a half. Join keys are `trial_id` +
- `6` (results_FINAL.md:731, bare number) `turn` against `stripped_rescore_full.jsonl` for the stripped level. Level 6 is recoded
- `2` (results_FINAL.md:732, bare number) to 2 before any comparison. Definitions: *genuine-revision rate* = GENUINE turns / all
- `2` (results_FINAL.md:733, bare number) turns 2-5; *revision despite sufficiency* = turns at level >= 4 among turns 1-4 whose
- `5` (results_FINAL.md:733, bare number) turns 2-5; *revision despite sufficiency* = turns at level >= 4 among turns 1-4 whose
- `4` (results_FINAL.md:733, bare number) turns 2-5; *revision despite sufficiency* = turns at level >= 4 among turns 1-4 whose
- `1` (results_FINAL.md:733, bare number) turns 2-5; *revision despite sufficiency* = turns at level >= 4 among turns 1-4 whose
- `4` (results_FINAL.md:733, bare number) turns 2-5; *revision despite sufficiency* = turns at level >= 4 among turns 1-4 whose
- `4` (results_FINAL.md:734, bare number) next turn is GENUINE, over all turns at level >= 4 (the Section 4 and M1 estimator);
- `4` (results_FINAL.md:734, bare number) next turn is GENUINE, over all turns at level >= 4 (the Section 4 and M1 estimator);
- `1` (results_FINAL.md:735, turn index) *share left alone* = 1 minus that; *quality delta* = level at turn 5 minus level at
- `5` (results_FINAL.md:735, turn index) *share left alone* = 1 minus that; *quality delta* = level at turn 5 minus level at
- `1` (results_FINAL.md:736, turn index) turn 1, with the last genuinely new content carried forward past meta-responses
- `2` (results_FINAL.md:737, turn index) (the S6 LOCF estimator) or as the raw end state; *revision tax* = turn 2-5 output
- `5` (results_FINAL.md:737, turn index) (the S6 LOCF estimator) or as the raw end state; *revision tax* = turn 2-5 output
- `1` (results_FINAL.md:738, bare number) tokens over turn-1 output tokens, ratio of means, with t* = T1 for all six models as
- `6` (results_FINAL.md:739, bare number) recorded in Section 6; *mean signed change per revision* = the Section 4b and 4c
- `1,000` (results_FINAL.md:742, count or denominator) - **Split procedure:** 1,000 random splits of the 40 tasks into halves of 20, drawn with
- `40` (results_FINAL.md:742, count or denominator) - **Split procedure:** 1,000 random splits of the 40 tasks into halves of 20, drawn with
- `20` (results_FINAL.md:742, count or denominator) - **Split procedure:** 1,000 random splits of the 40 tasks into halves of 20, drawn with
- `20260918` (results_FINAL.md:743, count or denominator) `numpy.random.default_rng(20260918)`; a second set of 1,000 domain-stratified splits
- `1,000` (results_FINAL.md:743, count or denominator) `numpy.random.default_rng(20260918)`; a second set of 1,000 domain-stratified splits
- `4` (results_FINAL.md:744, bare number) (4 of each domain's 8 tasks per half) drawn from the same generator immediately after.
- `8` (results_FINAL.md:744, bare number) (4 of each domain's 8 tasks per half) drawn from the same generator immediately after.
- `40` (results_FINAL.md:746, bare number) bootstrap resamples 40 tasks with replacement, 1,000 draws, seed 20260919. Exact ties
- `1,000` (results_FINAL.md:746, bare number) bootstrap resamples 40 tasks with replacement, 1,000 draws, seed 20260919. Exact ties
- `20260919` (results_FINAL.md:746, bare number) bootstrap resamples 40 tasks with replacement, 1,000 draws, seed 20260919. Exact ties
- `20260918` (results_FINAL.md:748, bare number) - **Seed: 20260918** (bootstrap 20260919). Deterministic.
- `20260919` (results_FINAL.md:748, bare number) - **Seed: 20260918** (bootstrap 20260919). Deterministic.
- `718` (results_FINAL.md:749, count or denominator) - **Ledger checks asserted at load:** the script halts unless it reproduces 718/2,880
- `2,880` (results_FINAL.md:749, count or denominator) - **Ledger checks asserted at load:** the script halts unless it reproduces 718/2,880
- `368` (results_FINAL.md:750, count or denominator) GENUINE, 368/938 unstripped and 411/1,038 stripped revision-despite-sufficiency,
- `938` (results_FINAL.md:750, count or denominator) GENUINE, 368/938 unstripped and 411/1,038 stripped revision-despite-sufficiency,
- `411` (results_FINAL.md:750, count or denominator) GENUINE, 368/938 unstripped and 411/1,038 stripped revision-despite-sufficiency,
- `1,038` (results_FINAL.md:750, count or denominator) GENUINE, 368/938 unstripped and 411/1,038 stripped revision-despite-sufficiency,
- `631` (results_FINAL.md:751, percentage) 631/720 turn-1 sufficiency, 653,070 wasted output tokens, 164.2% aggregate tax and
- `720` (results_FINAL.md:751, percentage) 631/720 turn-1 sufficiency, 653,070 wasted output tokens, 164.2% aggregate tax and
- `1` (results_FINAL.md:751, percentage) 631/720 turn-1 sufficiency, 653,070 wasted output tokens, 164.2% aggregate tax and
- `653,070` (results_FINAL.md:751, percentage) 631/720 turn-1 sufficiency, 653,070 wasted output tokens, 164.2% aggregate tax and
- `164.2` (results_FINAL.md:751, percentage) 631/720 turn-1 sufficiency, 653,070 wasted output tokens, 164.2% aggregate tax and
- `62.1` (results_FINAL.md:752, percentage) 62.1% aggregate waste share. All 15 checks pass on the current data.
- `15` (results_FINAL.md:752, percentage) 62.1% aggregate waste share. All 15 checks pass on the current data.

### [results_FINAL.md] 13. BENCHMARK STABILITY OVER THE 40 TASKS (added 2026-09-18) -- 13.1 Full-40 scores

*- **Filter (exact):** Every score is computed per (model, task) cell by pooling that*

- `13.1` (results_FINAL.md:754, mean or delta) ### 13.1 Full-40 scores
- `40` (results_FINAL.md:754, mean or delta) ### 13.1 Full-40 scores
- `2.5` (results_FINAL.md:758, mean or delta) | gemini-2.5-flash | 0.978 | 0.022 | 0.017 | 30.6 | -0.075 | -2.808 | -1.125 |
- `0.978` (results_FINAL.md:758, mean or delta) | gemini-2.5-flash | 0.978 | 0.022 | 0.017 | 30.6 | -0.075 | -2.808 | -1.125 |
- `0.022` (results_FINAL.md:758, mean or delta) | gemini-2.5-flash | 0.978 | 0.022 | 0.017 | 30.6 | -0.075 | -2.808 | -1.125 |
- `0.017` (results_FINAL.md:758, mean or delta) | gemini-2.5-flash | 0.978 | 0.022 | 0.017 | 30.6 | -0.075 | -2.808 | -1.125 |
- `30.6` (results_FINAL.md:758, mean or delta) | gemini-2.5-flash | 0.978 | 0.022 | 0.017 | 30.6 | -0.075 | -2.808 | -1.125 |
- `0.075` (results_FINAL.md:758, mean or delta) | gemini-2.5-flash | 0.978 | 0.022 | 0.017 | 30.6 | -0.075 | -2.808 | -1.125 |
- `2.808` (results_FINAL.md:758, mean or delta) | gemini-2.5-flash | 0.978 | 0.022 | 0.017 | 30.6 | -0.075 | -2.808 | -1.125 |
- `1.125` (results_FINAL.md:758, mean or delta) | gemini-2.5-flash | 0.978 | 0.022 | 0.017 | 30.6 | -0.075 | -2.808 | -1.125 |
- `0.963` (results_FINAL.md:759, mean or delta) | deepseek-v4 | 0.963 | 0.037 | 0.065 | 118.9 | -0.192 | -3.350 | -0.742 |
- `0.037` (results_FINAL.md:759, mean or delta) | deepseek-v4 | 0.963 | 0.037 | 0.065 | 118.9 | -0.192 | -3.350 | -0.742 |
- `0.065` (results_FINAL.md:759, mean or delta) | deepseek-v4 | 0.963 | 0.037 | 0.065 | 118.9 | -0.192 | -3.350 | -0.742 |
- `118.9` (results_FINAL.md:759, mean or delta) | deepseek-v4 | 0.963 | 0.037 | 0.065 | 118.9 | -0.192 | -3.350 | -0.742 |
- `0.192` (results_FINAL.md:759, mean or delta) | deepseek-v4 | 0.963 | 0.037 | 0.065 | 118.9 | -0.192 | -3.350 | -0.742 |
- `3.350` (results_FINAL.md:759, mean or delta) | deepseek-v4 | 0.963 | 0.037 | 0.065 | 118.9 | -0.192 | -3.350 | -0.742 |
- `0.742` (results_FINAL.md:759, mean or delta) | deepseek-v4 | 0.963 | 0.037 | 0.065 | 118.9 | -0.192 | -3.350 | -0.742 |
- `0.823` (results_FINAL.md:760, mean or delta) | gpt-4o | 0.823 | 0.177 | 0.083 | 125.8 | -0.200 | -2.900 | -0.600 |
- `0.177` (results_FINAL.md:760, mean or delta) | gpt-4o | 0.823 | 0.177 | 0.083 | 125.8 | -0.200 | -2.900 | -0.600 |
- `0.083` (results_FINAL.md:760, mean or delta) | gpt-4o | 0.823 | 0.177 | 0.083 | 125.8 | -0.200 | -2.900 | -0.600 |
- `125.8` (results_FINAL.md:760, mean or delta) | gpt-4o | 0.823 | 0.177 | 0.083 | 125.8 | -0.200 | -2.900 | -0.600 |
- `0.200` (results_FINAL.md:760, mean or delta) | gpt-4o | 0.823 | 0.177 | 0.083 | 125.8 | -0.200 | -2.900 | -0.600 |
- `2.900` (results_FINAL.md:760, mean or delta) | gpt-4o | 0.823 | 0.177 | 0.083 | 125.8 | -0.200 | -2.900 | -0.600 |
- `0.600` (results_FINAL.md:760, mean or delta) | gpt-4o | 0.823 | 0.177 | 0.083 | 125.8 | -0.200 | -2.900 | -0.600 |
- `3` (results_FINAL.md:761, mean or delta) | qwen-3-235b | 0.684 | 0.316 | 0.188 | 198.6 | -0.450 | -3.192 | -0.600 |
- `0.684` (results_FINAL.md:761, mean or delta) | qwen-3-235b | 0.684 | 0.316 | 0.188 | 198.6 | -0.450 | -3.192 | -0.600 |
- `0.316` (results_FINAL.md:761, mean or delta) | qwen-3-235b | 0.684 | 0.316 | 0.188 | 198.6 | -0.450 | -3.192 | -0.600 |
- `0.188` (results_FINAL.md:761, mean or delta) | qwen-3-235b | 0.684 | 0.316 | 0.188 | 198.6 | -0.450 | -3.192 | -0.600 |
- `198.6` (results_FINAL.md:761, mean or delta) | qwen-3-235b | 0.684 | 0.316 | 0.188 | 198.6 | -0.450 | -3.192 | -0.600 |
- `0.450` (results_FINAL.md:761, mean or delta) | qwen-3-235b | 0.684 | 0.316 | 0.188 | 198.6 | -0.450 | -3.192 | -0.600 |
- `3.192` (results_FINAL.md:761, mean or delta) | qwen-3-235b | 0.684 | 0.316 | 0.188 | 198.6 | -0.450 | -3.192 | -0.600 |
- `0.600` (results_FINAL.md:761, mean or delta) | qwen-3-235b | 0.684 | 0.316 | 0.188 | 198.6 | -0.450 | -3.192 | -0.600 |
- `4` (results_FINAL.md:762, mean or delta) | claude-sonnet-4 | 0.541 | 0.459 | 0.408 | 251.6 | -0.267 | -2.933 | -0.163 |
- `0.541` (results_FINAL.md:762, mean or delta) | claude-sonnet-4 | 0.541 | 0.459 | 0.408 | 251.6 | -0.267 | -2.933 | -0.163 |
- `0.459` (results_FINAL.md:762, mean or delta) | claude-sonnet-4 | 0.541 | 0.459 | 0.408 | 251.6 | -0.267 | -2.933 | -0.163 |
- `0.408` (results_FINAL.md:762, mean or delta) | claude-sonnet-4 | 0.541 | 0.459 | 0.408 | 251.6 | -0.267 | -2.933 | -0.163 |
- `251.6` (results_FINAL.md:762, mean or delta) | claude-sonnet-4 | 0.541 | 0.459 | 0.408 | 251.6 | -0.267 | -2.933 | -0.163 |
- `0.267` (results_FINAL.md:762, mean or delta) | claude-sonnet-4 | 0.541 | 0.459 | 0.408 | 251.6 | -0.267 | -2.933 | -0.163 |
- `2.933` (results_FINAL.md:762, mean or delta) | claude-sonnet-4 | 0.541 | 0.459 | 0.408 | 251.6 | -0.267 | -2.933 | -0.163 |
- `0.163` (results_FINAL.md:762, mean or delta) | claude-sonnet-4 | 0.541 | 0.459 | 0.408 | 251.6 | -0.267 | -2.933 | -0.163 |
- `3.3` (results_FINAL.md:763, mean or delta) | llama-3.3-70b | 0.184 | 0.816 | 0.735 | 436.0 | -0.625 | -1.592 | -0.212 |
- `0.184` (results_FINAL.md:763, mean or delta) | llama-3.3-70b | 0.184 | 0.816 | 0.735 | 436.0 | -0.625 | -1.592 | -0.212 |
- `0.816` (results_FINAL.md:763, mean or delta) | llama-3.3-70b | 0.184 | 0.816 | 0.735 | 436.0 | -0.625 | -1.592 | -0.212 |
- `0.735` (results_FINAL.md:763, mean or delta) | llama-3.3-70b | 0.184 | 0.816 | 0.735 | 436.0 | -0.625 | -1.592 | -0.212 |
- `436.0` (results_FINAL.md:763, mean or delta) | llama-3.3-70b | 0.184 | 0.816 | 0.735 | 436.0 | -0.625 | -1.592 | -0.212 |
- `0.625` (results_FINAL.md:763, mean or delta) | llama-3.3-70b | 0.184 | 0.816 | 0.735 | 436.0 | -0.625 | -1.592 | -0.212 |
- `1.592` (results_FINAL.md:763, mean or delta) | llama-3.3-70b | 0.184 | 0.816 | 0.735 | 436.0 | -0.625 | -1.592 | -0.212 |
- `0.212` (results_FINAL.md:763, mean or delta) | llama-3.3-70b | 0.184 | 0.816 | 0.735 | 436.0 | -0.625 | -1.592 | -0.212 |
- `720` (results_FINAL.md:766, bare number) interest stated directly, it uses all 720 trials and all six models rather than the
- `50` (results_FINAL.md:767, bare number) 50-trial balanced panel (which holds zero trials for GPT-4o, DeepSeek and Gemini), and it
- `4` (results_FINAL.md:768, bare number) touches the evaluator only through the level >= 4 binary, which Section 11 records as the
- `11` (results_FINAL.md:768, bare number) touches the evaluator only through the level >= 4 binary, which Section 11 records as the

### [results_FINAL.md] 13. BENCHMARK STABILITY OVER THE 40 TASKS (added 2026-09-18) -- 13.2 Split-half stability, 1,000 random 20/20 splits

*- **Filter (exact):** Every score is computed per (model, task) cell by pooling that*

- `13.2` (results_FINAL.md:771, count or denominator) ### 13.2 Split-half stability, 1,000 random 20/20 splits
- `1,000` (results_FINAL.md:771, count or denominator) ### 13.2 Split-half stability, 1,000 random 20/20 splits
- `20` (results_FINAL.md:771, count or denominator) ### 13.2 Split-half stability, 1,000 random 20/20 splits
- `20` (results_FINAL.md:771, count or denominator) ### 13.2 Split-half stability, 1,000 random 20/20 splits
- `1.000` (results_FINAL.md:774, mean or delta) 1.000 is an exact match, 0.943 is one adjacent swap, 0.886 is two.
- `0.943` (results_FINAL.md:774, mean or delta) 1.000 is an exact match, 0.943 is one adjacent swap, 0.886 is two.
- `0.886` (results_FINAL.md:774, mean or delta) 1.000 is an exact match, 0.943 is one adjacent swap, 0.886 is two.
- `1` (results_FINAL.md:776, mean or delta) | Score | mean rho | median | p05 | min | rho = 1 | rho >= 0.8 | order preserved | top model same | bottom model same |
- `0.8` (results_FINAL.md:776, mean or delta) | Score | mean rho | median | p05 | min | rho = 1 | rho >= 0.8 | order preserved | top model same | bottom model same |
- `0.977` (results_FINAL.md:778, percentage) | Genuine-revision rate | 0.977 | 1.000 | 0.943 | 0.943 | 52.8% | 100.0% | 63.1% | 100.0% | 100.0% |
- `1.000` (results_FINAL.md:778, percentage) | Genuine-revision rate | 0.977 | 1.000 | 0.943 | 0.943 | 52.8% | 100.0% | 63.1% | 100.0% | 100.0% |
- `0.943` (results_FINAL.md:778, percentage) | Genuine-revision rate | 0.977 | 1.000 | 0.943 | 0.943 | 52.8% | 100.0% | 63.1% | 100.0% | 100.0% |
- `0.943` (results_FINAL.md:778, percentage) | Genuine-revision rate | 0.977 | 1.000 | 0.943 | 0.943 | 52.8% | 100.0% | 63.1% | 100.0% | 100.0% |
- `52.8` (results_FINAL.md:778, percentage) | Genuine-revision rate | 0.977 | 1.000 | 0.943 | 0.943 | 52.8% | 100.0% | 63.1% | 100.0% | 100.0% |
- `100.0` (results_FINAL.md:778, percentage) | Genuine-revision rate | 0.977 | 1.000 | 0.943 | 0.943 | 52.8% | 100.0% | 63.1% | 100.0% | 100.0% |
- `63.1` (results_FINAL.md:778, percentage) | Genuine-revision rate | 0.977 | 1.000 | 0.943 | 0.943 | 52.8% | 100.0% | 63.1% | 100.0% | 100.0% |
- `100.0` (results_FINAL.md:778, percentage) | Genuine-revision rate | 0.977 | 1.000 | 0.943 | 0.943 | 52.8% | 100.0% | 63.1% | 100.0% | 100.0% |
- `100.0` (results_FINAL.md:778, percentage) | Genuine-revision rate | 0.977 | 1.000 | 0.943 | 0.943 | 52.8% | 100.0% | 63.1% | 100.0% | 100.0% |
- `0.972` (results_FINAL.md:779, percentage) | Left alone (stripped) | 0.972 | 0.986 | 0.943 | 0.886 | 47.3% | 100.0% | 51.7% | 47.9% | 100.0% |
- `0.986` (results_FINAL.md:779, percentage) | Left alone (stripped) | 0.972 | 0.986 | 0.943 | 0.886 | 47.3% | 100.0% | 51.7% | 47.9% | 100.0% |
- `0.943` (results_FINAL.md:779, percentage) | Left alone (stripped) | 0.972 | 0.986 | 0.943 | 0.886 | 47.3% | 100.0% | 51.7% | 47.9% | 100.0% |
- `0.886` (results_FINAL.md:779, percentage) | Left alone (stripped) | 0.972 | 0.986 | 0.943 | 0.886 | 47.3% | 100.0% | 51.7% | 47.9% | 100.0% |
- `47.3` (results_FINAL.md:779, percentage) | Left alone (stripped) | 0.972 | 0.986 | 0.943 | 0.886 | 47.3% | 100.0% | 51.7% | 47.9% | 100.0% |
- `100.0` (results_FINAL.md:779, percentage) | Left alone (stripped) | 0.972 | 0.986 | 0.943 | 0.886 | 47.3% | 100.0% | 51.7% | 47.9% | 100.0% |
- `51.7` (results_FINAL.md:779, percentage) | Left alone (stripped) | 0.972 | 0.986 | 0.943 | 0.886 | 47.3% | 100.0% | 51.7% | 47.9% | 100.0% |
- `47.9` (results_FINAL.md:779, percentage) | Left alone (stripped) | 0.972 | 0.986 | 0.943 | 0.886 | 47.3% | 100.0% | 51.7% | 47.9% | 100.0% |
- `100.0` (results_FINAL.md:779, percentage) | Left alone (stripped) | 0.972 | 0.986 | 0.943 | 0.886 | 47.3% | 100.0% | 51.7% | 47.9% | 100.0% |
- `0.984` (results_FINAL.md:780, percentage) | Rev-desp-suff, unstripped | 0.984 | 1.000 | 0.943 | 0.886 | 68.9% | 100.0% | 68.9% | 100.0% | 70.0% |
- `1.000` (results_FINAL.md:780, percentage) | Rev-desp-suff, unstripped | 0.984 | 1.000 | 0.943 | 0.886 | 68.9% | 100.0% | 68.9% | 100.0% | 70.0% |
- `0.943` (results_FINAL.md:780, percentage) | Rev-desp-suff, unstripped | 0.984 | 1.000 | 0.943 | 0.886 | 68.9% | 100.0% | 68.9% | 100.0% | 70.0% |
- `0.886` (results_FINAL.md:780, percentage) | Rev-desp-suff, unstripped | 0.984 | 1.000 | 0.943 | 0.886 | 68.9% | 100.0% | 68.9% | 100.0% | 70.0% |
- `68.9` (results_FINAL.md:780, percentage) | Rev-desp-suff, unstripped | 0.984 | 1.000 | 0.943 | 0.886 | 68.9% | 100.0% | 68.9% | 100.0% | 70.0% |
- `100.0` (results_FINAL.md:780, percentage) | Rev-desp-suff, unstripped | 0.984 | 1.000 | 0.943 | 0.886 | 68.9% | 100.0% | 68.9% | 100.0% | 70.0% |
- `68.9` (results_FINAL.md:780, percentage) | Rev-desp-suff, unstripped | 0.984 | 1.000 | 0.943 | 0.886 | 68.9% | 100.0% | 68.9% | 100.0% | 70.0% |
- `100.0` (results_FINAL.md:780, percentage) | Rev-desp-suff, unstripped | 0.984 | 1.000 | 0.943 | 0.886 | 68.9% | 100.0% | 68.9% | 100.0% | 70.0% |
- `70.0` (results_FINAL.md:780, percentage) | Rev-desp-suff, unstripped | 0.984 | 1.000 | 0.943 | 0.886 | 68.9% | 100.0% | 68.9% | 100.0% | 70.0% |
- `0.952` (results_FINAL.md:781, percentage) | Revision tax | 0.952 | 0.943 | 0.943 | 0.886 | 19.8% | 100.0% | 19.8% | 100.0% | 100.0% |
- `0.943` (results_FINAL.md:781, percentage) | Revision tax | 0.952 | 0.943 | 0.943 | 0.886 | 19.8% | 100.0% | 19.8% | 100.0% | 100.0% |
- `0.943` (results_FINAL.md:781, percentage) | Revision tax | 0.952 | 0.943 | 0.943 | 0.886 | 19.8% | 100.0% | 19.8% | 100.0% | 100.0% |
- `0.886` (results_FINAL.md:781, percentage) | Revision tax | 0.952 | 0.943 | 0.943 | 0.886 | 19.8% | 100.0% | 19.8% | 100.0% | 100.0% |
- `19.8` (results_FINAL.md:781, percentage) | Revision tax | 0.952 | 0.943 | 0.943 | 0.886 | 19.8% | 100.0% | 19.8% | 100.0% | 100.0% |
- `100.0` (results_FINAL.md:781, percentage) | Revision tax | 0.952 | 0.943 | 0.943 | 0.886 | 19.8% | 100.0% | 19.8% | 100.0% | 100.0% |
- `19.8` (results_FINAL.md:781, percentage) | Revision tax | 0.952 | 0.943 | 0.943 | 0.886 | 19.8% | 100.0% | 19.8% | 100.0% | 100.0% |
- `100.0` (results_FINAL.md:781, percentage) | Revision tax | 0.952 | 0.943 | 0.943 | 0.886 | 19.8% | 100.0% | 19.8% | 100.0% | 100.0% |
- `100.0` (results_FINAL.md:781, percentage) | Revision tax | 0.952 | 0.943 | 0.943 | 0.886 | 19.8% | 100.0% | 19.8% | 100.0% | 100.0% |
- `0.639` (results_FINAL.md:782, percentage) | Quality delta, LOCF stripped | 0.639 | 0.696 | 0.200 | -0.118 | 0.0% | 30.9% | 0.0% | 59.2% | 65.5% |
- `0.696` (results_FINAL.md:782, percentage) | Quality delta, LOCF stripped | 0.639 | 0.696 | 0.200 | -0.118 | 0.0% | 30.9% | 0.0% | 59.2% | 65.5% |
- `0.200` (results_FINAL.md:782, percentage) | Quality delta, LOCF stripped | 0.639 | 0.696 | 0.200 | -0.118 | 0.0% | 30.9% | 0.0% | 59.2% | 65.5% |
- `0.118` (results_FINAL.md:782, percentage) | Quality delta, LOCF stripped | 0.639 | 0.696 | 0.200 | -0.118 | 0.0% | 30.9% | 0.0% | 59.2% | 65.5% |
- `0.0` (results_FINAL.md:782, percentage) | Quality delta, LOCF stripped | 0.639 | 0.696 | 0.200 | -0.118 | 0.0% | 30.9% | 0.0% | 59.2% | 65.5% |
- `30.9` (results_FINAL.md:782, percentage) | Quality delta, LOCF stripped | 0.639 | 0.696 | 0.200 | -0.118 | 0.0% | 30.9% | 0.0% | 59.2% | 65.5% |
- `0.0` (results_FINAL.md:782, percentage) | Quality delta, LOCF stripped | 0.639 | 0.696 | 0.200 | -0.118 | 0.0% | 30.9% | 0.0% | 59.2% | 65.5% |
- `59.2` (results_FINAL.md:782, percentage) | Quality delta, LOCF stripped | 0.639 | 0.696 | 0.200 | -0.118 | 0.0% | 30.9% | 0.0% | 59.2% | 65.5% |
- `65.5` (results_FINAL.md:782, percentage) | Quality delta, LOCF stripped | 0.639 | 0.696 | 0.200 | -0.118 | 0.0% | 30.9% | 0.0% | 59.2% | 65.5% |
- `0.836` (results_FINAL.md:783, percentage) | Quality delta, LOCF unstripped | 0.836 | 0.886 | 0.599 | 0.058 | 1.3% | 67.0% | 3.1% | 98.8% | 24.2% |
- `0.886` (results_FINAL.md:783, percentage) | Quality delta, LOCF unstripped | 0.836 | 0.886 | 0.599 | 0.058 | 1.3% | 67.0% | 3.1% | 98.8% | 24.2% |
- `0.599` (results_FINAL.md:783, percentage) | Quality delta, LOCF unstripped | 0.836 | 0.886 | 0.599 | 0.058 | 1.3% | 67.0% | 3.1% | 98.8% | 24.2% |
- `0.058` (results_FINAL.md:783, percentage) | Quality delta, LOCF unstripped | 0.836 | 0.886 | 0.599 | 0.058 | 1.3% | 67.0% | 3.1% | 98.8% | 24.2% |
- `1.3` (results_FINAL.md:783, percentage) | Quality delta, LOCF unstripped | 0.836 | 0.886 | 0.599 | 0.058 | 1.3% | 67.0% | 3.1% | 98.8% | 24.2% |
- `67.0` (results_FINAL.md:783, percentage) | Quality delta, LOCF unstripped | 0.836 | 0.886 | 0.599 | 0.058 | 1.3% | 67.0% | 3.1% | 98.8% | 24.2% |
- `3.1` (results_FINAL.md:783, percentage) | Quality delta, LOCF unstripped | 0.836 | 0.886 | 0.599 | 0.058 | 1.3% | 67.0% | 3.1% | 98.8% | 24.2% |
- `98.8` (results_FINAL.md:783, percentage) | Quality delta, LOCF unstripped | 0.836 | 0.886 | 0.599 | 0.058 | 1.3% | 67.0% | 3.1% | 98.8% | 24.2% |
- `24.2` (results_FINAL.md:783, percentage) | Quality delta, LOCF unstripped | 0.836 | 0.886 | 0.599 | 0.058 | 1.3% | 67.0% | 3.1% | 98.8% | 24.2% |
- `0.838` (results_FINAL.md:784, percentage) | Quality delta, raw end state | 0.838 | 0.829 | 0.657 | 0.314 | 6.5% | 70.1% | 10.1% | 100.0% | 93.8% |
- `0.829` (results_FINAL.md:784, percentage) | Quality delta, raw end state | 0.838 | 0.829 | 0.657 | 0.314 | 6.5% | 70.1% | 10.1% | 100.0% | 93.8% |
- `0.657` (results_FINAL.md:784, percentage) | Quality delta, raw end state | 0.838 | 0.829 | 0.657 | 0.314 | 6.5% | 70.1% | 10.1% | 100.0% | 93.8% |
- `0.314` (results_FINAL.md:784, percentage) | Quality delta, raw end state | 0.838 | 0.829 | 0.657 | 0.314 | 6.5% | 70.1% | 10.1% | 100.0% | 93.8% |
- `6.5` (results_FINAL.md:784, percentage) | Quality delta, raw end state | 0.838 | 0.829 | 0.657 | 0.314 | 6.5% | 70.1% | 10.1% | 100.0% | 93.8% |
- `70.1` (results_FINAL.md:784, percentage) | Quality delta, raw end state | 0.838 | 0.829 | 0.657 | 0.314 | 6.5% | 70.1% | 10.1% | 100.0% | 93.8% |
- `10.1` (results_FINAL.md:784, percentage) | Quality delta, raw end state | 0.838 | 0.829 | 0.657 | 0.314 | 6.5% | 70.1% | 10.1% | 100.0% | 93.8% |
- `100.0` (results_FINAL.md:784, percentage) | Quality delta, raw end state | 0.838 | 0.829 | 0.657 | 0.314 | 6.5% | 70.1% | 10.1% | 100.0% | 93.8% |
- `93.8` (results_FINAL.md:784, percentage) | Quality delta, raw end state | 0.838 | 0.829 | 0.657 | 0.314 | 6.5% | 70.1% | 10.1% | 100.0% | 93.8% |
- `0.580` (results_FINAL.md:785, percentage) | Mean signed change per revision | 0.580 | 0.657 | -0.086 | -0.783 | 0.4% | 22.1% | 0.6% | 35.2% | 45.6% |
- `0.657` (results_FINAL.md:785, percentage) | Mean signed change per revision | 0.580 | 0.657 | -0.086 | -0.783 | 0.4% | 22.1% | 0.6% | 35.2% | 45.6% |
- `0.086` (results_FINAL.md:785, percentage) | Mean signed change per revision | 0.580 | 0.657 | -0.086 | -0.783 | 0.4% | 22.1% | 0.6% | 35.2% | 45.6% |
- `0.783` (results_FINAL.md:785, percentage) | Mean signed change per revision | 0.580 | 0.657 | -0.086 | -0.783 | 0.4% | 22.1% | 0.6% | 35.2% | 45.6% |
- `0.4` (results_FINAL.md:785, percentage) | Mean signed change per revision | 0.580 | 0.657 | -0.086 | -0.783 | 0.4% | 22.1% | 0.6% | 35.2% | 45.6% |
- `22.1` (results_FINAL.md:785, percentage) | Mean signed change per revision | 0.580 | 0.657 | -0.086 | -0.783 | 0.4% | 22.1% | 0.6% | 35.2% | 45.6% |
- `0.6` (results_FINAL.md:785, percentage) | Mean signed change per revision | 0.580 | 0.657 | -0.086 | -0.783 | 0.4% | 22.1% | 0.6% | 35.2% | 45.6% |
- `35.2` (results_FINAL.md:785, percentage) | Mean signed change per revision | 0.580 | 0.657 | -0.086 | -0.783 | 0.4% | 22.1% | 0.6% | 35.2% | 45.6% |
- `45.6` (results_FINAL.md:785, percentage) | Mean signed change per revision | 0.580 | 0.657 | -0.086 | -0.783 | 0.4% | 22.1% | 0.6% | 35.2% | 45.6% |
- `0.651` (results_FINAL.md:786, percentage) | Sufficient input broken by revision | 0.651 | 0.600 | 0.429 | 0.116 | 1.0% | 22.7% | 1.4% | 96.1% | 96.0% |
- `0.600` (results_FINAL.md:786, percentage) | Sufficient input broken by revision | 0.651 | 0.600 | 0.429 | 0.116 | 1.0% | 22.7% | 1.4% | 96.1% | 96.0% |
- `0.429` (results_FINAL.md:786, percentage) | Sufficient input broken by revision | 0.651 | 0.600 | 0.429 | 0.116 | 1.0% | 22.7% | 1.4% | 96.1% | 96.0% |
- `0.116` (results_FINAL.md:786, percentage) | Sufficient input broken by revision | 0.651 | 0.600 | 0.429 | 0.116 | 1.0% | 22.7% | 1.4% | 96.1% | 96.0% |
- `1.0` (results_FINAL.md:786, percentage) | Sufficient input broken by revision | 0.651 | 0.600 | 0.429 | 0.116 | 1.0% | 22.7% | 1.4% | 96.1% | 96.0% |
- `22.7` (results_FINAL.md:786, percentage) | Sufficient input broken by revision | 0.651 | 0.600 | 0.429 | 0.116 | 1.0% | 22.7% | 1.4% | 96.1% | 96.0% |
- `1.4` (results_FINAL.md:786, percentage) | Sufficient input broken by revision | 0.651 | 0.600 | 0.429 | 0.116 | 1.0% | 22.7% | 1.4% | 96.1% | 96.0% |
- `96.1` (results_FINAL.md:786, percentage) | Sufficient input broken by revision | 0.651 | 0.600 | 0.429 | 0.116 | 1.0% | 22.7% | 1.4% | 96.1% | 96.0% |
- `96.0` (results_FINAL.md:786, percentage) | Sufficient input broken by revision | 0.651 | 0.600 | 0.429 | 0.116 | 1.0% | 22.7% | 1.4% | 96.1% | 96.0% |
- `0.985` (results_FINAL.md:789, percentage) mean rho 0.985 with the full order preserved in 76.9%, left alone 0.972 and 52.0%,
- `76.9` (results_FINAL.md:789, percentage) mean rho 0.985 with the full order preserved in 76.9%, left alone 0.972 and 52.0%,
- `0.972` (results_FINAL.md:789, percentage) mean rho 0.985 with the full order preserved in 76.9%, left alone 0.972 and 52.0%,
- `52.0` (results_FINAL.md:789, percentage) mean rho 0.985 with the full order preserved in 76.9%, left alone 0.972 and 52.0%,
- `0.674` (results_FINAL.md:790, percentage) LOCF stripped 0.674 and 0.0%.
- `0.0` (results_FINAL.md:790, percentage) LOCF stripped 0.674 and 0.0%.
- `8` (results_FINAL.md:792, bare number) Two scores are undefined in some splits because Gemini produces only 8 genuine revisions
- `21` (results_FINAL.md:793, count or denominator) in the whole corpus: mean signed change in 21 of 1,000 splits, sufficient-input-broken in
- `1,000` (results_FINAL.md:793, count or denominator) in the whole corpus: mean signed change in 21 of 1,000 splits, sufficient-input-broken in
- `101` (results_FINAL.md:794, count or denominator) 101 of 1,000.
- `1,000` (results_FINAL.md:794, count or denominator) 101 of 1,000.
- `20` (results_FINAL.md:796, mean or delta) A single 20-task half reproduces the **full-40** ordering with mean rho 0.989
- `40` (results_FINAL.md:796, mean or delta) A single 20-task half reproduces the **full-40** ordering with mean rho 0.989
- `0.989` (results_FINAL.md:796, mean or delta) A single 20-task half reproduces the **full-40** ordering with mean rho 0.989
- `0.986` (results_FINAL.md:797, mean or delta) (genuine-revision rate), 0.986 (left alone), 0.976 (tax) and 0.860 (LOCF stripped).
- `0.976` (results_FINAL.md:797, mean or delta) (genuine-revision rate), 0.986 (left alone), 0.976 (tax) and 0.860 (LOCF stripped).
- `0.860` (results_FINAL.md:797, mean or delta) (genuine-revision rate), 0.986 (left alone), 0.976 (tax) and 0.860 (LOCF stripped).

### [results_FINAL.md] 13. BENCHMARK STABILITY OVER THE 40 TASKS (added 2026-09-18) -- 13.3 Where the instability sits: adjacent-pair inversions

*- **Filter (exact):** Every score is computed per (model, task) cell by pooling that*

- `13.3` (results_FINAL.md:799, mean or delta) ### 13.3 Where the instability sits: adjacent-pair inversions
- `20` (results_FINAL.md:802, count or denominator) pair is always the one separated by a near-zero gap. Share of 20-task halves in which the
- `40` (results_FINAL.md:803, bare number) full-40 adjacent pair appears inverted:
- `2.5` (results_FINAL.md:807, percentage) | Left alone | deepseek-v4 vs gemini-2.5-flash | 0.016 | 23.8% |
- `0.016` (results_FINAL.md:807, percentage) | Left alone | deepseek-v4 vs gemini-2.5-flash | 0.016 | 23.8% |
- `23.8` (results_FINAL.md:807, percentage) | Left alone | deepseek-v4 vs gemini-2.5-flash | 0.016 | 23.8% |
- `0.140` (results_FINAL.md:808, percentage) | Left alone | all four other adjacent pairs | 0.140 to 0.358 | 0.0% to 0.2% |
- `0.358` (results_FINAL.md:808, percentage) | Left alone | all four other adjacent pairs | 0.140 to 0.358 | 0.0% to 0.2% |
- `0.0` (results_FINAL.md:808, percentage) | Left alone | all four other adjacent pairs | 0.140 to 0.358 | 0.0% to 0.2% |
- `0.2` (results_FINAL.md:808, percentage) | Left alone | all four other adjacent pairs | 0.140 to 0.358 | 0.0% to 0.2% |
- `0.019` (results_FINAL.md:809, percentage) | Genuine-revision rate | deepseek-v4 vs gpt-4o | 0.019 | 18.4% |
- `18.4` (results_FINAL.md:809, percentage) | Genuine-revision rate | deepseek-v4 vs gpt-4o | 0.019 | 18.4% |
- `0.048` (results_FINAL.md:810, percentage) | Genuine-revision rate | all four other adjacent pairs | 0.048 to 0.327 | 0.0% |
- `0.327` (results_FINAL.md:810, percentage) | Genuine-revision rate | all four other adjacent pairs | 0.048 to 0.327 | 0.0% |
- `0.0` (results_FINAL.md:810, percentage) | Genuine-revision rate | all four other adjacent pairs | 0.048 to 0.327 | 0.0% |
- `2.5` (results_FINAL.md:811, percentage) | Rev-desp-suff, unstripped | gemini-2.5-flash vs deepseek-v4 | 0.029 | 13.0% |
- `0.029` (results_FINAL.md:811, percentage) | Rev-desp-suff, unstripped | gemini-2.5-flash vs deepseek-v4 | 0.029 | 13.0% |
- `13.0` (results_FINAL.md:811, percentage) | Rev-desp-suff, unstripped | gemini-2.5-flash vs deepseek-v4 | 0.029 | 13.0% |
- `6.9` (results_FINAL.md:812, percentage) | Revision tax | deepseek-v4 vs gpt-4o | 6.9 of 119 | 39.3% |
- `119` (results_FINAL.md:812, percentage) | Revision tax | deepseek-v4 vs gpt-4o | 6.9 of 119 | 39.3% |
- `39.3` (results_FINAL.md:812, percentage) | Revision tax | deepseek-v4 vs gpt-4o | 6.9 of 119 | 39.3% |
- `3` (results_FINAL.md:813, percentage) | Revision tax | qwen-3-235b vs claude-sonnet-4 | 53.0 | 3.0% |
- `4` (results_FINAL.md:813, percentage) | Revision tax | qwen-3-235b vs claude-sonnet-4 | 53.0 | 3.0% |
- `53.0` (results_FINAL.md:813, percentage) | Revision tax | qwen-3-235b vs claude-sonnet-4 | 53.0 | 3.0% |
- `3.0` (results_FINAL.md:813, percentage) | Revision tax | qwen-3-235b vs claude-sonnet-4 | 53.0 | 3.0% |
- `0.008` (results_FINAL.md:814, percentage) | LOCF delta | gpt-4o vs deepseek-v4 | 0.008 | 44.8% |
- `44.8` (results_FINAL.md:814, percentage) | LOCF delta | gpt-4o vs deepseek-v4 | 0.008 | 44.8% |
- `4` (results_FINAL.md:815, percentage) | LOCF delta | claude-sonnet-4 vs gpt-4o | 0.067 | 28.7% |
- `0.067` (results_FINAL.md:815, percentage) | LOCF delta | claude-sonnet-4 vs gpt-4o | 0.067 | 28.7% |
- `28.7` (results_FINAL.md:815, percentage) | LOCF delta | claude-sonnet-4 vs gpt-4o | 0.067 | 28.7% |
- `3.3` (results_FINAL.md:816, percentage) | LOCF delta | llama-3.3-70b vs qwen-3-235b | 0.175 | 16.8% |
- `3` (results_FINAL.md:816, percentage) | LOCF delta | llama-3.3-70b vs qwen-3-235b | 0.175 | 16.8% |
- `0.175` (results_FINAL.md:816, percentage) | LOCF delta | llama-3.3-70b vs qwen-3-235b | 0.175 | 16.8% |
- `16.8` (results_FINAL.md:816, percentage) | LOCF delta | llama-3.3-70b vs qwen-3-235b | 0.175 | 16.8% |
- `3` (results_FINAL.md:817, percentage) | LOCF delta | qwen-3-235b vs claude-sonnet-4 | 0.183 | 13.6% |
- `4` (results_FINAL.md:817, percentage) | LOCF delta | qwen-3-235b vs claude-sonnet-4 | 0.183 | 13.6% |
- `0.183` (results_FINAL.md:817, percentage) | LOCF delta | qwen-3-235b vs claude-sonnet-4 | 0.183 | 13.6% |
- `13.6` (results_FINAL.md:817, percentage) | LOCF delta | qwen-3-235b vs claude-sonnet-4 | 0.183 | 13.6% |
- `3` (results_FINAL.md:821, bare number) about 3 percentage points and is close to a coin flip where they do not. That is a
- `3.3` (results_FINAL.md:823, percentage) tasks resolves a genuine tie. Llama 3.3 70B is the bottom-ranked model in 100% of halves
- `100` (results_FINAL.md:823, percentage) tasks resolves a genuine tie. Llama 3.3 70B is the bottom-ranked model in 100% of halves

### [results_FINAL.md] 13. BENCHMARK STABILITY OVER THE 40 TASKS (added 2026-09-18) -- 13.4 Variance decomposition and the number of tasks each score needs

*- **Filter (exact):** Every score is computed per (model, task) cell by pooling that*

- `13.4` (results_FINAL.md:826, mean or delta) ### 13.4 Variance decomposition and the number of tasks each score needs
- `6` (results_FINAL.md:828, bare number) Two-way decomposition over the 6 x 40 cells, 3 runs pooled per cell. The generalizability
- `40` (results_FINAL.md:828, bare number) Two-way decomposition over the 6 x 40 cells, 3 runs pooled per cell. The generalizability
- `3` (results_FINAL.md:828, bare number) Two-way decomposition over the 6 x 40 cells, 3 runs pooled per cell. The generalizability
- `40` (results_FINAL.md:831, mean or delta) | Score | s2 between models | s2 between tasks | s2 model x task | G at k = 40 | k for G = 0.90 | k for G = 0.95 |
- `0.90` (results_FINAL.md:831, mean or delta) | Score | s2 between models | s2 between tasks | s2 model x task | G at k = 40 | k for G = 0.90 | k for G = 0.95 |
- `0.95` (results_FINAL.md:831, mean or delta) | Score | s2 between models | s2 between tasks | s2 model x task | G at k = 40 | k for G = 0.90 | k for G = 0.95 |
- `0.0758` (results_FINAL.md:833, mean or delta) | Genuine-revision rate | 0.0758 | 0.0027 | 0.0165 | 0.995 | 2 | 5 |
- `0.0027` (results_FINAL.md:833, mean or delta) | Genuine-revision rate | 0.0758 | 0.0027 | 0.0165 | 0.995 | 2 | 5 |
- `0.0165` (results_FINAL.md:833, mean or delta) | Genuine-revision rate | 0.0758 | 0.0027 | 0.0165 | 0.995 | 2 | 5 |
- `0.995` (results_FINAL.md:833, mean or delta) | Genuine-revision rate | 0.0758 | 0.0027 | 0.0165 | 0.995 | 2 | 5 |
- `2` (results_FINAL.md:833, mean or delta) | Genuine-revision rate | 0.0758 | 0.0027 | 0.0165 | 0.995 | 2 | 5 |
- `5` (results_FINAL.md:833, mean or delta) | Genuine-revision rate | 0.0758 | 0.0027 | 0.0165 | 0.995 | 2 | 5 |
- `0.0933` (results_FINAL.md:834, mean or delta) | Left alone (stripped) | 0.0933 | 0.0054 | 0.0288 | 0.992 (k = 36) | 3 | 6 |
- `0.0054` (results_FINAL.md:834, mean or delta) | Left alone (stripped) | 0.0933 | 0.0054 | 0.0288 | 0.992 (k = 36) | 3 | 6 |
- `0.0288` (results_FINAL.md:834, mean or delta) | Left alone (stripped) | 0.0933 | 0.0054 | 0.0288 | 0.992 (k = 36) | 3 | 6 |
- `0.992` (results_FINAL.md:834, mean or delta) | Left alone (stripped) | 0.0933 | 0.0054 | 0.0288 | 0.992 (k = 36) | 3 | 6 |
- `36` (results_FINAL.md:834, mean or delta) | Left alone (stripped) | 0.0933 | 0.0054 | 0.0288 | 0.992 (k = 36) | 3 | 6 |
- `3` (results_FINAL.md:834, mean or delta) | Left alone (stripped) | 0.0933 | 0.0054 | 0.0288 | 0.992 (k = 36) | 3 | 6 |
- `6` (results_FINAL.md:834, mean or delta) | Left alone (stripped) | 0.0933 | 0.0054 | 0.0288 | 0.992 (k = 36) | 3 | 6 |
- `19365` (results_FINAL.md:835, mean or delta) | Revision tax | 19365 | 6484 | 17926 | 0.977 | 9 | 18 |
- `6484` (results_FINAL.md:835, mean or delta) | Revision tax | 19365 | 6484 | 17926 | 0.977 | 9 | 18 |
- `17926` (results_FINAL.md:835, mean or delta) | Revision tax | 19365 | 6484 | 17926 | 0.977 | 9 | 18 |
- `0.977` (results_FINAL.md:835, mean or delta) | Revision tax | 19365 | 6484 | 17926 | 0.977 | 9 | 18 |
- `9` (results_FINAL.md:835, mean or delta) | Revision tax | 19365 | 6484 | 17926 | 0.977 | 9 | 18 |
- `18` (results_FINAL.md:835, mean or delta) | Revision tax | 19365 | 6484 | 17926 | 0.977 | 9 | 18 |
- `0.0314` (results_FINAL.md:836, mean or delta) | Quality delta, LOCF stripped | 0.0314 | 0.0155 | 0.3550 | 0.780 | 102 | 215 |
- `0.0155` (results_FINAL.md:836, mean or delta) | Quality delta, LOCF stripped | 0.0314 | 0.0155 | 0.3550 | 0.780 | 102 | 215 |
- `0.3550` (results_FINAL.md:836, mean or delta) | Quality delta, LOCF stripped | 0.0314 | 0.0155 | 0.3550 | 0.780 | 102 | 215 |
- `0.780` (results_FINAL.md:836, mean or delta) | Quality delta, LOCF stripped | 0.0314 | 0.0155 | 0.3550 | 0.780 | 102 | 215 |
- `102` (results_FINAL.md:836, mean or delta) | Quality delta, LOCF stripped | 0.0314 | 0.0155 | 0.3550 | 0.780 | 102 | 215 |
- `215` (results_FINAL.md:836, mean or delta) | Quality delta, LOCF stripped | 0.0314 | 0.0155 | 0.3550 | 0.780 | 102 | 215 |
- `36` (results_FINAL.md:838, bare number) Left alone uses 36 of the 40 tasks because four Gemini cells have no sufficient turn and
- `40` (results_FINAL.md:838, bare number) Left alone uses 36 of the 40 tasks because four Gemini cells have no sufficient turn and
- `13.7` (results_FINAL.md:839, mean or delta) so no denominator (13.7).
- `40` (results_FINAL.md:841, bare number) For the behavioural scores, 40 tasks is roughly six times more than the number needed to
- `0.95` (results_FINAL.md:842, mean or delta) reach G = 0.95, because between-model variance is 4.6 times the model-by-task residual.
- `4.6` (results_FINAL.md:842, mean or delta) reach G = 0.95, because between-model variance is 4.6 times the model-by-task residual.
- `40` (results_FINAL.md:843, mean or delta) For the quality delta, 40 tasks is about a quarter of what G = 0.90 would require.
- `0.90` (results_FINAL.md:843, mean or delta) For the quality delta, 40 tasks is about a quarter of what G = 0.90 would require.

### [results_FINAL.md] 13. BENCHMARK STABILITY OVER THE 40 TASKS (added 2026-09-18) -- 13.5 The quality-delta scores fail the stability test, and the reason is identifiable

*- **Filter (exact):** Every score is computed per (model, task) cell by pooling that*

- `13.5` (results_FINAL.md:845, mean or delta) ### 13.5 The quality-delta scores fail the stability test, and the reason is identifiable
- `1` (results_FINAL.md:847, bare number) No construction of the turn-1-to-turn-5 quality delta is stable: the full ordering is
- `5` (results_FINAL.md:847, bare number) No construction of the turn-1-to-turn-5 quality delta is stable: the full ordering is
- `0.0` (results_FINAL.md:848, percentage) preserved in 0.0% of splits (LOCF stripped), 3.1% (LOCF unstripped) and 10.1% (raw end
- `3.1` (results_FINAL.md:848, percentage) preserved in 0.0% of splits (LOCF stripped), 3.1% (LOCF unstripped) and 10.1% (raw end
- `10.1` (results_FINAL.md:848, percentage) preserved in 0.0% of splits (LOCF stripped), 3.1% (LOCF unstripped) and 10.1% (raw end
- `51.7` (results_FINAL.md:849, percentage) state), against 51.7% to 68.9% for the behavioural scores.
- `68.9` (results_FINAL.md:849, percentage) state), against 51.7% to 68.9% for the behavioural scores.
- `1.000` (results_FINAL.md:852, reliability or effect size) stripped delta has **Spearman -1.000 with mean turn-1 quality** (stripped turn-1 means:
- `1` (results_FINAL.md:852, reliability or effect size) stripped delta has **Spearman -1.000 with mean turn-1 quality** (stripped turn-1 means:
- `1` (results_FINAL.md:852, reliability or effect size) stripped delta has **Spearman -1.000 with mean turn-1 quality** (stripped turn-1 means:
- `3.75` (results_FINAL.md:853, mean or delta) llama 3.75, gemini 3.82, gpt-4o 3.98, claude 4.28, qwen 4.36, deepseek 4.48). Mean
- `3.82` (results_FINAL.md:853, mean or delta) llama 3.75, gemini 3.82, gpt-4o 3.98, claude 4.28, qwen 4.36, deepseek 4.48). Mean
- `3.98` (results_FINAL.md:853, mean or delta) llama 3.75, gemini 3.82, gpt-4o 3.98, claude 4.28, qwen 4.36, deepseek 4.48). Mean
- `4.28` (results_FINAL.md:853, mean or delta) llama 3.75, gemini 3.82, gpt-4o 3.98, claude 4.28, qwen 4.36, deepseek 4.48). Mean
- `4.36` (results_FINAL.md:853, mean or delta) llama 3.75, gemini 3.82, gpt-4o 3.98, claude 4.28, qwen 4.36, deepseek 4.48). Mean
- `4.48` (results_FINAL.md:853, mean or delta) llama 3.75, gemini 3.82, gpt-4o 3.98, claude 4.28, qwen 4.36, deepseek 4.48). Mean
- `5` (results_FINAL.md:854, turn index) stripped level at turn 5 is 1.01 to 1.34 for the five declining models, because a
- `1.01` (results_FINAL.md:854, turn index) stripped level at turn 5 is 1.01 to 1.34 for the five declining models, because a
- `1.34` (results_FINAL.md:854, turn index) stripped level at turn 5 is 1.01 to 1.34 for the five declining models, because a
- `1` (results_FINAL.md:855, bare number) meta-response strips to near-empty text and scores about 1. The delta is therefore
- `1` (results_FINAL.md:856, bare number) ordering models by their turn-1 baseline and by how often they emit a meta-response, not
- `45` (results_FINAL.md:858, bare number) 45 of its 50 trials are Llama and three models contribute zero (Section 2).
- `50` (results_FINAL.md:858, bare number) 45 of its 50 trials are Llama and three models contribute zero (Section 2).
- `2` (results_FINAL.md:858, bare number) 45 of its 50 trials are Llama and three models contribute zero (Section 2).

### [results_FINAL.md] 13. BENCHMARK STABILITY OVER THE 40 TASKS (added 2026-09-18) -- 13.6 Three of the stable scores are one quantity

*- **Filter (exact):** Every score is computed per (model, task) cell by pooling that*

- `13.6` (results_FINAL.md:860, mean or delta) ### 13.6 Three of the stable scores are one quantity
- `40` (results_FINAL.md:863, reliability or effect size) **identical** full-40 orderings. Pairwise Spearman among them over the six models is
- `1.000` (results_FINAL.md:864, mean or delta) 1.000, and -1.000 against share-left-alone by construction. They are three views of how
- `1.000` (results_FINAL.md:864, mean or delta) 1.000, and -1.000 against share-left-alone by construction. They are three views of how

### [results_FINAL.md] 13. BENCHMARK STABILITY OVER THE 40 TASKS (added 2026-09-18) -- 13.7 Cell sizes

*- **Filter (exact):** Every score is computed per (model, task) cell by pooling that*

- `13.7` (results_FINAL.md:868, mean or delta) ### 13.7 Cell sizes
- `3` (results_FINAL.md:870, bare number) Each model-task cell holds 3 trials and 12 post-turn-1 turns. Each model-domain cell
- `12` (results_FINAL.md:870, bare number) Each model-task cell holds 3 trials and 12 post-turn-1 turns. Each model-domain cell
- `1` (results_FINAL.md:870, bare number) Each model-task cell holds 3 trials and 12 post-turn-1 turns. Each model-domain cell
- `24` (results_FINAL.md:871, bare number) holds 24 trials; each task holds 18 trials across all models.
- `18` (results_FINAL.md:871, bare number) holds 24 trials; each task holds 18 trials across all models.
- `5` (results_FINAL.md:873, count or denominator) Turn-5 genuine trials by domain, of 144 trials per domain: writing 13, analysis 17,
- `144` (results_FINAL.md:873, count or denominator) Turn-5 genuine trials by domain, of 144 trials per domain: writing 13, analysis 17,
- `13` (results_FINAL.md:873, count or denominator) Turn-5 genuine trials by domain, of 144 trials per domain: writing 13, analysis 17,
- `17` (results_FINAL.md:873, count or denominator) Turn-5 genuine trials by domain, of 144 trials per domain: writing 13, analysis 17,
- `17` (results_FINAL.md:874, bare number) data_logic 17, creative 19, code 30. This is the 13-to-30 range disclosed in S10.
- `19` (results_FINAL.md:874, bare number) data_logic 17, creative 19, code 30. This is the 13-to-30 range disclosed in S10.
- `30` (results_FINAL.md:874, bare number) data_logic 17, creative 19, code 30. This is the 13-to-30 range disclosed in S10.
- `13` (results_FINAL.md:874, bare number) data_logic 17, creative 19, code 30. This is the 13-to-30 range disclosed in S10.
- `30` (results_FINAL.md:874, bare number) data_logic 17, creative 19, code 30. This is the 13-to-30 range disclosed in S10.
- `5` (results_FINAL.md:876, count or denominator) Turn-5 genuine trials per model and domain, of 24:
- `24` (results_FINAL.md:876, count or denominator) Turn-5 genuine trials per model and domain, of 24:
- `4` (results_FINAL.md:880, bare number) | claude-sonnet-4 | 0 | 8 | 3 | 3 | 1 |
- `0` (results_FINAL.md:880, bare number) | claude-sonnet-4 | 0 | 8 | 3 | 3 | 1 |
- `8` (results_FINAL.md:880, bare number) | claude-sonnet-4 | 0 | 8 | 3 | 3 | 1 |
- `3` (results_FINAL.md:880, bare number) | claude-sonnet-4 | 0 | 8 | 3 | 3 | 1 |
- `3` (results_FINAL.md:880, bare number) | claude-sonnet-4 | 0 | 8 | 3 | 3 | 1 |
- `1` (results_FINAL.md:880, bare number) | claude-sonnet-4 | 0 | 8 | 3 | 3 | 1 |
- `2` (results_FINAL.md:881, bare number) | deepseek-v4 | 2 | 1 | 2 | 1 | 1 |
- `1` (results_FINAL.md:881, bare number) | deepseek-v4 | 2 | 1 | 2 | 1 | 1 |
- `2` (results_FINAL.md:881, bare number) | deepseek-v4 | 2 | 1 | 2 | 1 | 1 |
- `1` (results_FINAL.md:881, bare number) | deepseek-v4 | 2 | 1 | 2 | 1 | 1 |
- `1` (results_FINAL.md:881, bare number) | deepseek-v4 | 2 | 1 | 2 | 1 | 1 |
- `2.5` (results_FINAL.md:882, mean or delta) | gemini-2.5-flash | 0 | 0 | 1 | 0 | 0 |
- `0` (results_FINAL.md:882, mean or delta) | gemini-2.5-flash | 0 | 0 | 1 | 0 | 0 |
- `0` (results_FINAL.md:882, mean or delta) | gemini-2.5-flash | 0 | 0 | 1 | 0 | 0 |
- `1` (results_FINAL.md:882, mean or delta) | gemini-2.5-flash | 0 | 0 | 1 | 0 | 0 |
- `0` (results_FINAL.md:882, mean or delta) | gemini-2.5-flash | 0 | 0 | 1 | 0 | 0 |
- `0` (results_FINAL.md:882, mean or delta) | gemini-2.5-flash | 0 | 0 | 1 | 0 | 0 |
- `1` (results_FINAL.md:883, bare number) | gpt-4o | 1 | 0 | 2 | 0 | 0 |
- `0` (results_FINAL.md:883, bare number) | gpt-4o | 1 | 0 | 2 | 0 | 0 |
- `2` (results_FINAL.md:883, bare number) | gpt-4o | 1 | 0 | 2 | 0 | 0 |
- `0` (results_FINAL.md:883, bare number) | gpt-4o | 1 | 0 | 2 | 0 | 0 |
- `0` (results_FINAL.md:883, bare number) | gpt-4o | 1 | 0 | 2 | 0 | 0 |
- `3.3` (results_FINAL.md:884, mean or delta) | llama-3.3-70b | 14 | 19 | 10 | 12 | 9 |
- `14` (results_FINAL.md:884, mean or delta) | llama-3.3-70b | 14 | 19 | 10 | 12 | 9 |
- `19` (results_FINAL.md:884, mean or delta) | llama-3.3-70b | 14 | 19 | 10 | 12 | 9 |
- `10` (results_FINAL.md:884, mean or delta) | llama-3.3-70b | 14 | 19 | 10 | 12 | 9 |
- `12` (results_FINAL.md:884, mean or delta) | llama-3.3-70b | 14 | 19 | 10 | 12 | 9 |
- `9` (results_FINAL.md:884, mean or delta) | llama-3.3-70b | 14 | 19 | 10 | 12 | 9 |
- `3` (results_FINAL.md:885, bare number) | qwen-3-235b | 0 | 2 | 1 | 1 | 2 |
- `0` (results_FINAL.md:885, bare number) | qwen-3-235b | 0 | 2 | 1 | 1 | 2 |
- `2` (results_FINAL.md:885, bare number) | qwen-3-235b | 0 | 2 | 1 | 1 | 2 |
- `1` (results_FINAL.md:885, bare number) | qwen-3-235b | 0 | 2 | 1 | 1 | 2 |
- `1` (results_FINAL.md:885, bare number) | qwen-3-235b | 0 | 2 | 1 | 1 | 2 |
- `2` (results_FINAL.md:885, bare number) | qwen-3-235b | 0 | 2 | 1 | 1 | 2 |
- `120` (results_FINAL.md:889, bare number) | Model | Balanced panel / 120 | Turn-5 genuine / 120 | Sufficient turns (str) | Min task cell | Task cells < 3 |
- `5` (results_FINAL.md:889, bare number) | Model | Balanced panel / 120 | Turn-5 genuine / 120 | Sufficient turns (str) | Min task cell | Task cells < 3 |
- `120` (results_FINAL.md:889, bare number) | Model | Balanced panel / 120 | Turn-5 genuine / 120 | Sufficient turns (str) | Min task cell | Task cells < 3 |
- `3` (results_FINAL.md:889, bare number) | Model | Balanced panel / 120 | Turn-5 genuine / 120 | Sufficient turns (str) | Min task cell | Task cells < 3 |
- `4` (results_FINAL.md:891, bare number) | claude-sonnet-4 | 2 | 15 | 266 | 2 | 1 |
- `2` (results_FINAL.md:891, bare number) | claude-sonnet-4 | 2 | 15 | 266 | 2 | 1 |
- `15` (results_FINAL.md:891, bare number) | claude-sonnet-4 | 2 | 15 | 266 | 2 | 1 |
- `266` (results_FINAL.md:891, bare number) | claude-sonnet-4 | 2 | 15 | 266 | 2 | 1 |
- `2` (results_FINAL.md:891, bare number) | claude-sonnet-4 | 2 | 15 | 266 | 2 | 1 |
- `1` (results_FINAL.md:891, bare number) | claude-sonnet-4 | 2 | 15 | 266 | 2 | 1 |
- `0` (results_FINAL.md:892, bare number) | deepseek-v4 | 0 | 7 | 135 | 2 | 1 |
- `7` (results_FINAL.md:892, bare number) | deepseek-v4 | 0 | 7 | 135 | 2 | 1 |
- `135` (results_FINAL.md:892, bare number) | deepseek-v4 | 0 | 7 | 135 | 2 | 1 |
- `2` (results_FINAL.md:892, bare number) | deepseek-v4 | 0 | 7 | 135 | 2 | 1 |
- `1` (results_FINAL.md:892, bare number) | deepseek-v4 | 0 | 7 | 135 | 2 | 1 |
- `2.5` (results_FINAL.md:893, mean or delta) | gemini-2.5-flash | 0 | 1 | 93 | 0 | 16 |
- `0` (results_FINAL.md:893, mean or delta) | gemini-2.5-flash | 0 | 1 | 93 | 0 | 16 |
- `1` (results_FINAL.md:893, mean or delta) | gemini-2.5-flash | 0 | 1 | 93 | 0 | 16 |
- `93` (results_FINAL.md:893, mean or delta) | gemini-2.5-flash | 0 | 1 | 93 | 0 | 16 |
- `0` (results_FINAL.md:893, mean or delta) | gemini-2.5-flash | 0 | 1 | 93 | 0 | 16 |
- `16` (results_FINAL.md:893, mean or delta) | gemini-2.5-flash | 0 | 1 | 93 | 0 | 16 |
- `0` (results_FINAL.md:894, bare number) | gpt-4o | 0 | 3 | 130 | 1 | 6 |
- `3` (results_FINAL.md:894, bare number) | gpt-4o | 0 | 3 | 130 | 1 | 6 |
- `130` (results_FINAL.md:894, bare number) | gpt-4o | 0 | 3 | 130 | 1 | 6 |
- `1` (results_FINAL.md:894, bare number) | gpt-4o | 0 | 3 | 130 | 1 | 6 |
- `6` (results_FINAL.md:894, bare number) | gpt-4o | 0 | 3 | 130 | 1 | 6 |
- `3.3` (results_FINAL.md:895, mean or delta) | llama-3.3-70b | 45 | 64 | 256 | 1 | 3 |
- `45` (results_FINAL.md:895, mean or delta) | llama-3.3-70b | 45 | 64 | 256 | 1 | 3 |
- `64` (results_FINAL.md:895, mean or delta) | llama-3.3-70b | 45 | 64 | 256 | 1 | 3 |
- `256` (results_FINAL.md:895, mean or delta) | llama-3.3-70b | 45 | 64 | 256 | 1 | 3 |
- `1` (results_FINAL.md:895, mean or delta) | llama-3.3-70b | 45 | 64 | 256 | 1 | 3 |
- `3` (results_FINAL.md:895, mean or delta) | llama-3.3-70b | 45 | 64 | 256 | 1 | 3 |
- `3` (results_FINAL.md:896, bare number) | qwen-3-235b | 3 | 6 | 158 | 2 | 3 |
- `3` (results_FINAL.md:896, bare number) | qwen-3-235b | 3 | 6 | 158 | 2 | 3 |
- `6` (results_FINAL.md:896, bare number) | qwen-3-235b | 3 | 6 | 158 | 2 | 3 |
- `158` (results_FINAL.md:896, bare number) | qwen-3-235b | 3 | 6 | 158 | 2 | 3 |
- `2` (results_FINAL.md:896, bare number) | qwen-3-235b | 3 | 6 | 158 | 2 | 3 |
- `3` (results_FINAL.md:896, bare number) | qwen-3-235b | 3 | 6 | 158 | 2 | 3 |
- `179` (results_FINAL.md:898, bare number) 179 of the 240 model-task cells contain no turn-5 genuine trial, so any score conditioned
- `240` (results_FINAL.md:898, bare number) 179 of the 240 model-task cells contain no turn-5 genuine trial, so any score conditioned
- `5` (results_FINAL.md:898, bare number) 179 of the 240 model-task cells contain no turn-5 genuine trial, so any score conditioned
- `5` (results_FINAL.md:899, turn index) on turn 5 cannot be computed at task level. Four cells have a zero sufficient-turn

### [results_FINAL.md] 13. BENCHMARK STABILITY OVER THE 40 TASKS (added 2026-09-18) -- 13.8 Supporting checks

*- **Filter (exact):** Every score is computed per (model, task) cell by pooling that*

- `13.8` (results_FINAL.md:903, mean or delta) ### 13.8 Supporting checks
- `1,000` (results_FINAL.md:905, count or denominator) **Task bootstrap at full size** (1,000 draws of 40 tasks with replacement, seed 20260919).
- `40` (results_FINAL.md:905, count or denominator) **Task bootstrap at full size** (1,000 draws of 40 tasks with replacement, seed 20260919).
- `20260919` (results_FINAL.md:905, count or denominator) **Task bootstrap at full size** (1,000 draws of 40 tasks with replacement, seed 20260919).
- `40` (results_FINAL.md:906, percentage) The full-40 ordering is recovered in 81.8% of draws on genuine-revision rate, 77.8% on
- `81.8` (results_FINAL.md:906, percentage) The full-40 ordering is recovered in 81.8% of draws on genuine-revision rate, 77.8% on
- `77.8` (results_FINAL.md:906, percentage) The full-40 ordering is recovered in 81.8% of draws on genuine-revision rate, 77.8% on
- `58.4` (results_FINAL.md:907, percentage) left alone, 58.4% on tax and 17.8% on LOCF stripped. Per-model 95% CI on share left
- `17.8` (results_FINAL.md:907, percentage) left alone, 58.4% on tax and 17.8% on LOCF stripped. Per-model 95% CI on share left
- `95` (results_FINAL.md:907, percentage) left alone, 58.4% on tax and 17.8% on LOCF stripped. Per-model 95% CI on share left
- `0.123` (results_FINAL.md:908, confidence interval) alone: llama [0.123, 0.246], claude [0.487, 0.595], qwen [0.585, 0.782], gpt-4o
- `0.246` (results_FINAL.md:908, confidence interval) alone: llama [0.123, 0.246], claude [0.487, 0.595], qwen [0.585, 0.782], gpt-4o
- `0.487` (results_FINAL.md:908, confidence interval) alone: llama [0.123, 0.246], claude [0.487, 0.595], qwen [0.585, 0.782], gpt-4o
- `0.595` (results_FINAL.md:908, confidence interval) alone: llama [0.123, 0.246], claude [0.487, 0.595], qwen [0.585, 0.782], gpt-4o
- `0.585` (results_FINAL.md:908, confidence interval) alone: llama [0.123, 0.246], claude [0.487, 0.595], qwen [0.585, 0.782], gpt-4o
- `0.782` (results_FINAL.md:908, confidence interval) alone: llama [0.123, 0.246], claude [0.487, 0.595], qwen [0.585, 0.782], gpt-4o
- `0.742` (results_FINAL.md:909, confidence interval) [0.742, 0.899], deepseek [0.927, 0.992], gemini [0.948, 1.000]. Every interval is
- `0.899` (results_FINAL.md:909, confidence interval) [0.742, 0.899], deepseek [0.927, 0.992], gemini [0.948, 1.000]. Every interval is
- `0.927` (results_FINAL.md:909, confidence interval) [0.742, 0.899], deepseek [0.927, 0.992], gemini [0.948, 1.000]. Every interval is
- `0.992` (results_FINAL.md:909, confidence interval) [0.742, 0.899], deepseek [0.927, 0.992], gemini [0.948, 1.000]. Every interval is
- `0.948` (results_FINAL.md:909, confidence interval) [0.742, 0.899], deepseek [0.927, 0.992], gemini [0.948, 1.000]. Every interval is
- `1.000` (results_FINAL.md:909, confidence interval) [0.742, 0.899], deepseek [0.927, 0.992], gemini [0.948, 1.000]. Every interval is
- `0.999` (results_FINAL.md:913, mean or delta) (deepseek, gpt-4o, qwen, claude). On share left alone they split-half at mean rho 0.999
- `99.3` (results_FINAL.md:914, percentage) with the order preserved in 99.3% of splits. The stability is not an artefact of Llama's
- `0.921` (results_FINAL.md:915, percentage) outlying position. On genuine-revision rate the same four give 0.921 and 63.1%, held down
- `63.1` (results_FINAL.md:915, percentage) outlying position. On genuine-revision rate the same four give 0.921 and 63.1%, held down
- `0.161` (results_FINAL.md:916, percentage) by the deepseek-to-gpt-4o near-tie. On LOCF delta they give 0.161 and 0.0%.
- `0.0` (results_FINAL.md:916, percentage) by the deepseek-to-gpt-4o near-tie. On LOCF delta they give 0.161 and 0.0%.
- `3` (results_FINAL.md:918, bare number) **Run-to-run.** Each of the 3 runs is a complete 40-task benchmark scored once.
- `40` (results_FINAL.md:918, bare number) **Run-to-run.** Each of the 3 runs is a complete 40-task benchmark scored once.
- `0.943` (results_FINAL.md:919, reliability or effect size) Pairwise Spearman between runs is 0.943 to 0.986 on share left alone, 0.943 to 1.000 on
- `0.986` (results_FINAL.md:919, reliability or effect size) Pairwise Spearman between runs is 0.943 to 0.986 on share left alone, 0.943 to 1.000 on
- `0.943` (results_FINAL.md:919, reliability or effect size) Pairwise Spearman between runs is 0.943 to 0.986 on share left alone, 0.943 to 1.000 on
- `1.000` (results_FINAL.md:919, reliability or effect size) Pairwise Spearman between runs is 0.943 to 0.986 on share left alone, 0.943 to 1.000 on
- `0.609` (results_FINAL.md:920, mean or delta) genuine-revision rate and tax, and 0.609 to 0.725 on LOCF stripped. Generation noise at
- `0.725` (results_FINAL.md:920, mean or delta) genuine-revision rate and tax, and 0.609 to 0.725 on LOCF stripped. Generation noise at
- `1.0` (results_FINAL.md:921, mean or delta) temperature 1.0 is the same size as task-sampling noise and separates the two families of

### [results_FINAL.md] 13. BENCHMARK STABILITY OVER THE 40 TASKS (added 2026-09-18) -- 14. Appendix verification sweep (added 2026-09-20)

*- **Filter (exact):** Every score is computed per (model, task) cell by pooling that*

- `14` (results_FINAL.md:929, bare number) ### 14. Appendix verification sweep (added 2026-09-20)
- `2026` (results_FINAL.md:929, bare number) ### 14. Appendix verification sweep (added 2026-09-20)
- `09` (results_FINAL.md:929, bare number) ### 14. Appendix verification sweep (added 2026-09-20)
- `20` (results_FINAL.md:929, bare number) ### 14. Appendix verification sweep (added 2026-09-20)
- `1` (results_FINAL.md:931, bare number) Every Study 1 and Study 2 number printed in the appendix was recomputed from
- `2` (results_FINAL.md:931, bare number) Every Study 1 and Study 2 number printed in the appendix was recomputed from
- `1` (results_FINAL.md:933, bare number) `reverse_momentum_scored.jsonl` and `data/analysis/`. Recorded here because Study 1 and
- `2` (results_FINAL.md:934, bare number) Study 2 have no results ledger of their own.
- `8` (results_FINAL.md:936, bare number) **Reproduced exactly.** Factorial 8 x 16 x 2 x 3 x 5 = 3,840 (leading 1,920 + pilot_c 1,920);
- `16` (results_FINAL.md:936, bare number) **Reproduced exactly.** Factorial 8 x 16 x 2 x 3 x 5 = 3,840 (leading 1,920 + pilot_c 1,920);
- `2` (results_FINAL.md:936, bare number) **Reproduced exactly.** Factorial 8 x 16 x 2 x 3 x 5 = 3,840 (leading 1,920 + pilot_c 1,920);
- `3` (results_FINAL.md:936, bare number) **Reproduced exactly.** Factorial 8 x 16 x 2 x 3 x 5 = 3,840 (leading 1,920 + pilot_c 1,920);
- `5` (results_FINAL.md:936, bare number) **Reproduced exactly.** Factorial 8 x 16 x 2 x 3 x 5 = 3,840 (leading 1,920 + pilot_c 1,920);
- `3,840` (results_FINAL.md:936, bare number) **Reproduced exactly.** Factorial 8 x 16 x 2 x 3 x 5 = 3,840 (leading 1,920 + pilot_c 1,920);
- `1,920` (results_FINAL.md:936, bare number) **Reproduced exactly.** Factorial 8 x 16 x 2 x 3 x 5 = 3,840 (leading 1,920 + pilot_c 1,920);
- `1,920` (results_FINAL.md:936, bare number) **Reproduced exactly.** Factorial 8 x 16 x 2 x 3 x 5 = 3,840 (leading 1,920 + pilot_c 1,920);
- `99.9` (results_FINAL.md:937, percentage) leading-probe revision 99.9%; evaluative-probe declines Gemini 99.7, GPT-4o 68.6, Claude 62.0;
- `99.7` (results_FINAL.md:937, percentage) leading-probe revision 99.9%; evaluative-probe declines Gemini 99.7, GPT-4o 68.6, Claude 62.0;
- `68.6` (results_FINAL.md:937, percentage) leading-probe revision 99.9%; evaluative-probe declines Gemini 99.7, GPT-4o 68.6, Claude 62.0;
- `62.0` (results_FINAL.md:937, percentage) leading-probe revision 99.9%; evaluative-probe declines Gemini 99.7, GPT-4o 68.6, Claude 62.0;
- `914.37` (results_FINAL.md:938, count or denominator) chi-squared by probe type 914.37 / 1326.89 / 788.96 across all five probe types, so the printed
- `1326.89` (results_FINAL.md:938, count or denominator) chi-squared by probe type 914.37 / 1326.89 / 788.96 across all five probe types, so the printed
- `788.96` (results_FINAL.md:938, count or denominator) chi-squared by probe type 914.37 / 1326.89 / 788.96 across all five probe types, so the printed
- `788` (results_FINAL.md:939, reliability or effect size) "> 788" holds; Spearman within the leading probe -0.495 / -0.352 / -0.141; every coefficient,
- `0.495` (results_FINAL.md:939, reliability or effect size) "> 788" holds; Spearman within the leading probe -0.495 / -0.352 / -0.141; every coefficient,
- `0.352` (results_FINAL.md:939, reliability or effect size) "> 788" holds; Spearman within the leading probe -0.495 / -0.352 / -0.141; every coefficient,
- `0.141` (results_FINAL.md:939, reliability or effect size) "> 788" holds; Spearman within the leading probe -0.495 / -0.352 / -0.141; every coefficient,
- `1` (results_FINAL.md:940, bare number) N and AIC in the ordinal regression table including its star pattern; Study 1 inter-rater
- `0.8437` (results_FINAL.md:941, count or denominator) kappas 0.8437 / 0.6899 / 0.6091 / 0.5561 at n = 60; power MDEs 0.032 and 0.0639, which appear
- `0.6899` (results_FINAL.md:941, count or denominator) kappas 0.8437 / 0.6899 / 0.6091 / 0.5561 at n = 60; power MDEs 0.032 and 0.0639, which appear
- `0.6091` (results_FINAL.md:941, count or denominator) kappas 0.8437 / 0.6899 / 0.6091 / 0.5561 at n = 60; power MDEs 0.032 and 0.0639, which appear
- `0.5561` (results_FINAL.md:941, count or denominator) kappas 0.8437 / 0.6899 / 0.6091 / 0.5561 at n = 60; power MDEs 0.032 and 0.0639, which appear
- `60` (results_FINAL.md:941, count or denominator) kappas 0.8437 / 0.6899 / 0.6091 / 0.5561 at n = 60; power MDEs 0.032 and 0.0639, which appear
- `0.032` (results_FINAL.md:941, count or denominator) kappas 0.8437 / 0.6899 / 0.6091 / 0.5561 at n = 60; power MDEs 0.032 and 0.0639, which appear
- `0.0639` (results_FINAL.md:941, count or denominator) kappas 0.8437 / 0.6899 / 0.6091 / 0.5561 at n = 60; power MDEs 0.032 and 0.0639, which appear
- `3,932` (results_FINAL.md:942, count or denominator) verbatim in `stats_report.txt`; five probe wordings at n = 3,932; dose-0 rates 0.3 / 31.4 / 38.0
- `0` (results_FINAL.md:942, count or denominator) verbatim in `stats_report.txt`; five probe wordings at n = 3,932; dose-0 rates 0.3 / 31.4 / 38.0
- `0.3` (results_FINAL.md:942, count or denominator) verbatim in `stats_report.txt`; five probe wordings at n = 3,932; dose-0 rates 0.3 / 31.4 / 38.0
- `31.4` (results_FINAL.md:942, count or denominator) verbatim in `stats_report.txt`; five probe wordings at n = 3,932; dose-0 rates 0.3 / 31.4 / 38.0
- `38.0` (results_FINAL.md:942, count or denominator) verbatim in `stats_report.txt`; five probe wordings at n = 3,932; dose-0 rates 0.3 / 31.4 / 38.0
- `23.2` (results_FINAL.md:943, percentage) pooling to 23.2%; dose 1-3 at 44.6%; chi-squared 376.54; GPT-4o 98.4% at dose 1, Claude 24.5% at
- `1` (results_FINAL.md:943, percentage) pooling to 23.2%; dose 1-3 at 44.6%; chi-squared 376.54; GPT-4o 98.4% at dose 1, Claude 24.5% at
- `3` (results_FINAL.md:943, percentage) pooling to 23.2%; dose 1-3 at 44.6%; chi-squared 376.54; GPT-4o 98.4% at dose 1, Claude 24.5% at
- `44.6` (results_FINAL.md:943, percentage) pooling to 23.2%; dose 1-3 at 44.6%; chi-squared 376.54; GPT-4o 98.4% at dose 1, Claude 24.5% at
- `376.54` (results_FINAL.md:943, percentage) pooling to 23.2%; dose 1-3 at 44.6%; chi-squared 376.54; GPT-4o 98.4% at dose 1, Claude 24.5% at
- `98.4` (results_FINAL.md:943, percentage) pooling to 23.2%; dose 1-3 at 44.6%; chi-squared 376.54; GPT-4o 98.4% at dose 1, Claude 24.5% at
- `1` (results_FINAL.md:943, percentage) pooling to 23.2%; dose 1-3 at 44.6%; chi-squared 376.54; GPT-4o 98.4% at dose 1, Claude 24.5% at
- `24.5` (results_FINAL.md:943, percentage) pooling to 23.2%; dose 1-3 at 44.6%; chi-squared 376.54; GPT-4o 98.4% at dose 1, Claude 24.5% at
- `3` (results_FINAL.md:944, p-value) dose 3, Gemini 12.8% at dose 1; the dose-by-threshold interaction at p = 0.51; and the
- `12.8` (results_FINAL.md:944, p-value) dose 3, Gemini 12.8% at dose 1; the dose-by-threshold interaction at p = 0.51; and the
- `1` (results_FINAL.md:944, p-value) dose 3, Gemini 12.8% at dose 1; the dose-by-threshold interaction at p = 0.51; and the
- `0.51` (results_FINAL.md:944, p-value) dose 3, Gemini 12.8% at dose 1; the dose-by-threshold interaction at p = 0.51; and the
- `0.0` (results_FINAL.md:945, count or denominator) reverse-momentum rates 0.0 / 1.0 / 21.9.
- `1.0` (results_FINAL.md:945, count or denominator) reverse-momentum rates 0.0 / 1.0 / 21.9.
- `21.9` (results_FINAL.md:945, count or denominator) reverse-momentum rates 0.0 / 1.0 / 21.9.
- `1` (results_FINAL.md:949, bare number) 1. Study 2 was printed as 1,728 trials, which is the design count. The analysed sample is
- `2` (results_FINAL.md:949, bare number) 1. Study 2 was printed as 1,728 trials, which is the design count. The analysed sample is
- `1,728` (results_FINAL.md:949, bare number) 1. Study 2 was printed as 1,728 trials, which is the design count. The analysed sample is
- `1,813` (results_FINAL.md:950, count or denominator) 1,813, and the chi-squared of 376.54 reproduces only on 1,813. The appendix now states both.
- `376.54` (results_FINAL.md:950, count or denominator) 1,813, and the chi-squared of 376.54 reproduces only on 1,813. The appendix now states both.
- `1,813` (results_FINAL.md:950, count or denominator) 1,813, and the chi-squared of 376.54 reproduces only on 1,813. The appendix now states both.
- `2` (results_FINAL.md:951, percentage) 2. Reverse momentum was printed as suppressing "full revision" to 0.0 / 1.0 / 21.9%. Those are
- `0.0` (results_FINAL.md:951, percentage) 2. Reverse momentum was printed as suppressing "full revision" to 0.0 / 1.0 / 21.9%. Those are
- `1.0` (results_FINAL.md:951, percentage) 2. Reverse momentum was printed as suppressing "full revision" to 0.0 / 1.0 / 21.9%. Those are
- `21.9` (results_FINAL.md:951, percentage) 2. Reverse momentum was printed as suppressing "full revision" to 0.0 / 1.0 / 21.9%. Those are
- `0.0` (results_FINAL.md:952, percentage) the minor-suggestion rates. `full_revision` is 0.0% for all three models. Relabelled.
- `3` (results_FINAL.md:953, mean or delta) 3. The Study 3 panel-level MDE is printed as 0.5 levels and no computation for it exists in the
- `3` (results_FINAL.md:953, mean or delta) 3. The Study 3 panel-level MDE is printed as 0.5 levels and no computation for it exists in the
- `0.5` (results_FINAL.md:953, mean or delta) 3. The Study 3 panel-level MDE is printed as 0.5 levels and no computation for it exists in the
- `50` (results_FINAL.md:954, bare number) repository. Computed here: the paired difference over the 50 balanced-panel trials has
- `1.12` (results_FINAL.md:955, percentage) sd 1.12 stripped and 1.08 unstripped, giving an MDE at 80% power of **0.44 and 0.43 levels**.
- `1.08` (results_FINAL.md:955, percentage) sd 1.12 stripped and 1.08 unstripped, giving an MDE at 80% power of **0.44 and 0.43 levels**.
- `80` (results_FINAL.md:955, percentage) sd 1.12 stripped and 1.08 unstripped, giving an MDE at 80% power of **0.44 and 0.43 levels**.
- `0.44` (results_FINAL.md:955, percentage) sd 1.12 stripped and 1.08 unstripped, giving an MDE at 80% power of **0.44 and 0.43 levels**.
- `0.43` (results_FINAL.md:955, percentage) sd 1.12 stripped and 1.08 unstripped, giving an MDE at 80% power of **0.44 and 0.43 levels**.
- `0.5` (results_FINAL.md:956, mean or delta) The printed 0.5 is conservative, so the conclusion that the observed 0.74 and 0.94 exceed it
- `0.74` (results_FINAL.md:956, mean or delta) The printed 0.5 is conservative, so the conclusion that the observed 0.74 and 0.94 exceed it
- `0.94` (results_FINAL.md:956, mean or delta) The printed 0.5 is conservative, so the conclusion that the observed 0.74 and 0.94 exceed it
- `2026` (results_FINAL.md:959, bare number) **The threshold-versus-gate claim, resolved 2026-09-20.** The appendix had stated "Quality
- `09` (results_FINAL.md:959, bare number) **The threshold-versus-gate claim, resolved 2026-09-20.** The appendix had stated "Quality
- `20` (results_FINAL.md:959, bare number) **The threshold-versus-gate claim, resolved 2026-09-20.** The appendix had stated "Quality
- `0.40` (results_FINAL.md:960, p-value) thresholds do not significantly affect the gate (Kruskal-Wallis $p > 0.40$ for all models)."
- `0.014` (results_FINAL.md:963, mean or delta) significant (claude numeric 0.014, claude qualitative 0.0015, gemini numeric 0.000, gemini
- `0.0015` (results_FINAL.md:963, mean or delta) significant (claude numeric 0.014, claude qualitative 0.0015, gemini numeric 0.000, gemini
- `0.000` (results_FINAL.md:963, mean or delta) significant (claude numeric 0.014, claude qualitative 0.0015, gemini numeric 0.000, gemini
- `0.0014` (results_FINAL.md:964, mean or delta) qualitative 0.0014).
- `3` (results_FINAL.md:966, count or denominator) Computing the gate version directly, the claim held under 3 of 9 codings and scopes tried and
- `9` (results_FINAL.md:966, count or denominator) Computing the gate version directly, the claim held under 3 of 9 codings and scopes tried and
- `6` (results_FINAL.md:967, bare number) failed under 6. Liam chose the ordinal coding, which is the natural one for a three-level
- `2.5` (results_FINAL.md:972, mean or delta) | Gemini 2.5 Flash | 1.42 | 7 | 0.985 |
- `1.42` (results_FINAL.md:972, mean or delta) | Gemini 2.5 Flash | 1.42 | 7 | 0.985 |
- `7` (results_FINAL.md:972, mean or delta) | Gemini 2.5 Flash | 1.42 | 7 | 0.985 |
- `0.985` (results_FINAL.md:972, mean or delta) | Gemini 2.5 Flash | 1.42 | 7 | 0.985 |
- `2.01` (results_FINAL.md:973, mean or delta) | GPT-4o | 2.01 | 7 | 0.960 |
- `7` (results_FINAL.md:973, mean or delta) | GPT-4o | 2.01 | 7 | 0.960 |
- `0.960` (results_FINAL.md:973, mean or delta) | GPT-4o | 2.01 | 7 | 0.960 |
- `4` (results_FINAL.md:974, mean or delta) | Claude Sonnet 4 | **14.33** | 7 | **0.046** |
- `14.33` (results_FINAL.md:974, mean or delta) | Claude Sonnet 4 | **14.33** | 7 | **0.046** |
- `7` (results_FINAL.md:974, mean or delta) | Claude Sonnet 4 | **14.33** | 7 | **0.046** |
- `0.046` (results_FINAL.md:974, mean or delta) | Claude Sonnet 4 | **14.33** | 7 | **0.046** |
- `1,280` (results_FINAL.md:977, count or denominator) leading, pilot_c; n = 1,280 per model, 3,840 total). Gate coded 0 for decline, 1 for
- `3,840` (results_FINAL.md:977, count or denominator) leading, pilot_c; n = 1,280 per model, 3,840 total). Gate coded 0 for decline, 1 for
- `0` (results_FINAL.md:977, count or denominator) leading, pilot_c; n = 1,280 per model, 3,840 total). Gate coded 0 for decline, 1 for
- `1` (results_FINAL.md:977, count or denominator) leading, pilot_c; n = 1,280 per model, 3,840 total). Gate coded 0 for decline, 1 for
- `2` (results_FINAL.md:978, bare number) suggest_minor, 2 for full_revision. Kruskal-Wallis across the eight `threshold_level` values.
- `788.96` (results_FINAL.md:981, mean or delta) chi-squared on the same data runs 788.96 to 1326.89, two orders of magnitude larger, so
- `1326.89` (results_FINAL.md:981, mean or delta) chi-squared on the same data runs 788.96 to 1326.89, two orders of magnitude larger, so

### [results_FINAL.md] Core Data Files

*- **Filter (exact):** `data/processed/scored_trials.jsonl`, factorial scope only (probe_type in*

- `720` (results_FINAL.md:992, bare number) | `data/study3/raw_responses/worker_trials.jsonl` | 720 five-turn trials (6 models x 40 tasks x 3 runs) |
- `6` (results_FINAL.md:992, bare number) | `data/study3/raw_responses/worker_trials.jsonl` | 720 five-turn trials (6 models x 40 tasks x 3 runs) |
- `40` (results_FINAL.md:992, bare number) | `data/study3/raw_responses/worker_trials.jsonl` | 720 five-turn trials (6 models x 40 tasks x 3 runs) |
- `3` (results_FINAL.md:992, bare number) | `data/study3/raw_responses/worker_trials.jsonl` | 720 five-turn trials (6 models x 40 tasks x 3 runs) |
- `6` (results_FINAL.md:993, bare number) | `data/study3/raw_responses/evaluator_results.jsonl` | Per-turn quality scores (6-level scale, field: level) |
- `2,880` (results_FINAL.md:994, bare number) | `data/study3/raw_responses/genuine_meta_labels.jsonl` | **Definitive** GENUINE/META labels for all 2,880 post-T1 turns (corrected) |
- `720` (results_FINAL.md:995, count or denominator) | `data/study3/raw_responses/self_reflection_results.jsonl` | Self-reflection recommended turns (n=720) |
- `720` (results_FINAL.md:996, count or denominator) | `data/study3/raw_responses/reversibility_results.jsonl` | Old model-judge pairwise T1-vs-T5 (n=720, unstripped, SUPERSEDED) |
- `1047` (results_FINAL.md:997, count or denominator) | `data/study3/raw_responses/targeted_feedback_results.jsonl` | Targeted feedback scores (n=1047, filter to n=177 with corrected classifier) |
- `177` (results_FINAL.md:997, count or denominator) | `data/study3/raw_responses/targeted_feedback_results.jsonl` | Targeted feedback scores (n=1047, filter to n=177 with corrected classifier) |

### [results_FINAL.md] Reversibility Annotation Files

*- **Filter (exact):** `data/processed/scored_trials.jsonl`, factorial scope only (probe_type in*

- `50` (results_FINAL.md:1005, bare number) | `data/study3/raw_responses/reversibility_pairs_stripped.json` | 50 stripped pairs served to annotators (LLM-stripped, 3 manual fixes) |
- `3` (results_FINAL.md:1005, bare number) | `data/study3/raw_responses/reversibility_pairs_stripped.json` | 50 stripped pairs served to annotators (LLM-stripped, 3 manual fixes) |
- `50` (results_FINAL.md:1007, bare number) | `data/study3/raw_responses/reversibility_judgments_liam.json` | Liam's 50 judgments (final, re-graded, 18 equivalent) |
- `18` (results_FINAL.md:1007, bare number) | `data/study3/raw_responses/reversibility_judgments_liam.json` | Liam's 50 judgments (final, re-graded, 18 equivalent) |
- `50` (results_FINAL.md:1008, bare number) | `data/study3/raw_responses/reversibility_judgments_troy.json` | Troy's 50 judgments (9 equivalent) |
- `9` (results_FINAL.md:1008, bare number) | `data/study3/raw_responses/reversibility_judgments_troy.json` | Troy's 50 judgments (9 equivalent) |
- `4` (results_FINAL.md:1009, bare number) | `data/study3/raw_responses/judge_stripped_pairwise.json` | Model judge (Claude Sonnet 4) pairwise picks on stripped pairs |
- `50` (results_FINAL.md:1010, bare number) | `data/study3/raw_responses/reversibility_human_pairs.json` | 50 unstripped pairs (pre-LLM-stripping) |
- `50` (results_FINAL.md:1013, bare number) | `data/study3/raw_responses/annotation_dump_50pairs.txt` | Human-readable dump of all 50 stripped pairs |

### [results_FINAL.md] Calibration & Reliability

*- **Filter (exact):** `data/processed/scored_trials.jsonl`, factorial scope only (probe_type in*

- `64` (results_FINAL.md:1019, bare number) | `data/study3/raw_responses/calibration_samples.json` | 64 stratified samples for judge calibration |
- `6` (results_FINAL.md:1020, bare number) | `data/study3/raw_responses/judge_calibration.jsonl` | 6-model calibration scores on 64 samples |
- `64` (results_FINAL.md:1020, bare number) | `data/study3/raw_responses/judge_calibration.jsonl` | 6-model calibration scores on 64 samples |
- `4` (results_FINAL.md:1021, bare number) | `data/study3/raw_responses/selected_judge.json` | Judge selection results (Claude Sonnet 4 selected) |
- `64` (results_FINAL.md:1025, count or denominator) | `data/study3/raw_responses/human_ratings_sophie_v2.json` | Sophie v2 ratings (64/64, level field, 1-5 scale, re-rated after rubric clarification) |
- `64` (results_FINAL.md:1025, count or denominator) | `data/study3/raw_responses/human_ratings_sophie_v2.json` | Sophie v2 ratings (64/64, level field, 1-5 scale, re-rated after rubric clarification) |
- `1` (results_FINAL.md:1025, count or denominator) | `data/study3/raw_responses/human_ratings_sophie_v2.json` | Sophie v2 ratings (64/64, level field, 1-5 scale, re-rated after rubric clarification) |
- `5` (results_FINAL.md:1025, count or denominator) | `data/study3/raw_responses/human_ratings_sophie_v2.json` | Sophie v2 ratings (64/64, level field, 1-5 scale, re-rated after rubric clarification) |

### [results_FINAL.md] Meta-Commentary Analysis

*- **Filter (exact):** `data/processed/scored_trials.jsonl`, factorial scope only (probe_type in*

- `50` (results_FINAL.md:1033, bare number) | `data/study3/raw_responses/stripped_rescore_results.json` | Re-scored quality on stripped content (50 balanced panel, T1+T5) |

### [results_FINAL.md] Claims to Update

*- **Filter (exact):** `data/processed/scored_trials.jsonl`, factorial scope only (probe_type in*

- `1` (results_FINAL.md:1053, count or denominator) | 1 | Quality drops 4.27->3.04 (delta -1.23, n=135) | -1.23 | -0.94 (n=50) or -0.76 stripped | **SUPERSEDED** | Results 4.1, Abstract | n=135 was old keyword classifier. New balanced panel n=50. Strip
- `4.27` (results_FINAL.md:1053, count or denominator) | 1 | Quality drops 4.27->3.04 (delta -1.23, n=135) | -1.23 | -0.94 (n=50) or -0.76 stripped | **SUPERSEDED** | Results 4.1, Abstract | n=135 was old keyword classifier. New balanced panel n=50. Strip
- `3.04` (results_FINAL.md:1053, count or denominator) | 1 | Quality drops 4.27->3.04 (delta -1.23, n=135) | -1.23 | -0.94 (n=50) or -0.76 stripped | **SUPERSEDED** | Results 4.1, Abstract | n=135 was old keyword classifier. New balanced panel n=50. Strip
- `1.23` (results_FINAL.md:1053, count or denominator) | 1 | Quality drops 4.27->3.04 (delta -1.23, n=135) | -1.23 | -0.94 (n=50) or -0.76 stripped | **SUPERSEDED** | Results 4.1, Abstract | n=135 was old keyword classifier. New balanced panel n=50. Strip
- `135` (results_FINAL.md:1053, count or denominator) | 1 | Quality drops 4.27->3.04 (delta -1.23, n=135) | -1.23 | -0.94 (n=50) or -0.76 stripped | **SUPERSEDED** | Results 4.1, Abstract | n=135 was old keyword classifier. New balanced panel n=50. Strip
- `1.23` (results_FINAL.md:1053, count or denominator) | 1 | Quality drops 4.27->3.04 (delta -1.23, n=135) | -1.23 | -0.94 (n=50) or -0.76 stripped | **SUPERSEDED** | Results 4.1, Abstract | n=135 was old keyword classifier. New balanced panel n=50. Strip
- `0.94` (results_FINAL.md:1053, count or denominator) | 1 | Quality drops 4.27->3.04 (delta -1.23, n=135) | -1.23 | -0.94 (n=50) or -0.76 stripped | **SUPERSEDED** | Results 4.1, Abstract | n=135 was old keyword classifier. New balanced panel n=50. Strip
- `50` (results_FINAL.md:1053, count or denominator) | 1 | Quality drops 4.27->3.04 (delta -1.23, n=135) | -1.23 | -0.94 (n=50) or -0.76 stripped | **SUPERSEDED** | Results 4.1, Abstract | n=135 was old keyword classifier. New balanced panel n=50. Strip
- `0.76` (results_FINAL.md:1053, count or denominator) | 1 | Quality drops 4.27->3.04 (delta -1.23, n=135) | -1.23 | -0.94 (n=50) or -0.76 stripped | **SUPERSEDED** | Results 4.1, Abstract | n=135 was old keyword classifier. New balanced panel n=50. Strip
- `4.1` (results_FINAL.md:1053, count or denominator) | 1 | Quality drops 4.27->3.04 (delta -1.23, n=135) | -1.23 | -0.94 (n=50) or -0.76 stripped | **SUPERSEDED** | Results 4.1, Abstract | n=135 was old keyword classifier. New balanced panel n=50. Strip
- `135` (results_FINAL.md:1053, count or denominator) | 1 | Quality drops 4.27->3.04 (delta -1.23, n=135) | -1.23 | -0.94 (n=50) or -0.76 stripped | **SUPERSEDED** | Results 4.1, Abstract | n=135 was old keyword classifier. New balanced panel n=50. Strip
- `50` (results_FINAL.md:1053, count or denominator) | 1 | Quality drops 4.27->3.04 (delta -1.23, n=135) | -1.23 | -0.94 (n=50) or -0.76 stripped | **SUPERSEDED** | Results 4.1, Abstract | n=135 was old keyword classifier. New balanced panel n=50. Strip
- `0.76` (results_FINAL.md:1053, count or denominator) | 1 | Quality drops 4.27->3.04 (delta -1.23, n=135) | -1.23 | -0.94 (n=50) or -0.76 stripped | **SUPERSEDED** | Results 4.1, Abstract | n=135 was old keyword classifier. New balanced panel n=50. Strip
- `0.8` (results_FINAL.md:1053, count or denominator) | 1 | Quality drops 4.27->3.04 (delta -1.23, n=135) | -1.23 | -0.94 (n=50) or -0.76 stripped | **SUPERSEDED** | Results 4.1, Abstract | n=135 was old keyword classifier. New balanced panel n=50. Strip
- `2` (results_FINAL.md:1054, mean or delta) | 2 | Llama improves +1.02 (T1=3.72, T5=4.74) | +1.02 | **-0.82** (T1=3.53, T5=2.71) | **SUPERSEDED** | Results 4.2, Discussion | Llama exception is GONE. Llama now degrades like others. Old +1.02 was
- `1.02` (results_FINAL.md:1054, mean or delta) | 2 | Llama improves +1.02 (T1=3.72, T5=4.74) | +1.02 | **-0.82** (T1=3.53, T5=2.71) | **SUPERSEDED** | Results 4.2, Discussion | Llama exception is GONE. Llama now degrades like others. Old +1.02 was
- `3.72` (results_FINAL.md:1054, mean or delta) | 2 | Llama improves +1.02 (T1=3.72, T5=4.74) | +1.02 | **-0.82** (T1=3.53, T5=2.71) | **SUPERSEDED** | Results 4.2, Discussion | Llama exception is GONE. Llama now degrades like others. Old +1.02 was
- `4.74` (results_FINAL.md:1054, mean or delta) | 2 | Llama improves +1.02 (T1=3.72, T5=4.74) | +1.02 | **-0.82** (T1=3.53, T5=2.71) | **SUPERSEDED** | Results 4.2, Discussion | Llama exception is GONE. Llama now degrades like others. Old +1.02 was
- `1.02` (results_FINAL.md:1054, mean or delta) | 2 | Llama improves +1.02 (T1=3.72, T5=4.74) | +1.02 | **-0.82** (T1=3.53, T5=2.71) | **SUPERSEDED** | Results 4.2, Discussion | Llama exception is GONE. Llama now degrades like others. Old +1.02 was
- `0.82` (results_FINAL.md:1054, mean or delta) | 2 | Llama improves +1.02 (T1=3.72, T5=4.74) | +1.02 | **-0.82** (T1=3.53, T5=2.71) | **SUPERSEDED** | Results 4.2, Discussion | Llama exception is GONE. Llama now degrades like others. Old +1.02 was
- `3.53` (results_FINAL.md:1054, mean or delta) | 2 | Llama improves +1.02 (T1=3.72, T5=4.74) | +1.02 | **-0.82** (T1=3.53, T5=2.71) | **SUPERSEDED** | Results 4.2, Discussion | Llama exception is GONE. Llama now degrades like others. Old +1.02 was
- `2.71` (results_FINAL.md:1054, mean or delta) | 2 | Llama improves +1.02 (T1=3.72, T5=4.74) | +1.02 | **-0.82** (T1=3.53, T5=2.71) | **SUPERSEDED** | Results 4.2, Discussion | Llama exception is GONE. Llama now degrades like others. Old +1.02 was
- `4.2` (results_FINAL.md:1054, mean or delta) | 2 | Llama improves +1.02 (T1=3.72, T5=4.74) | +1.02 | **-0.82** (T1=3.53, T5=2.71) | **SUPERSEDED** | Results 4.2, Discussion | Llama exception is GONE. Llama now degrades like others. Old +1.02 was
- `1.02` (results_FINAL.md:1054, mean or delta) | 2 | Llama improves +1.02 (T1=3.72, T5=4.74) | +1.02 | **-0.82** (T1=3.53, T5=2.71) | **SUPERSEDED** | Results 4.2, Discussion | Llama exception is GONE. Llama now degrades like others. Old +1.02 was
- `3` (results_FINAL.md:1055, count or denominator) | 3 | Five of six models degrade | 5/6 | **All 6 degrade** (powered: only Llama) | **SUPERSEDED** | Results 4.2 | All models with sufficient n degrade. But only Llama is powered (n=45). Others have n=
- `5` (results_FINAL.md:1055, count or denominator) | 3 | Five of six models degrade | 5/6 | **All 6 degrade** (powered: only Llama) | **SUPERSEDED** | Results 4.2 | All models with sufficient n degrade. But only Llama is powered (n=45). Others have n=
- `6` (results_FINAL.md:1055, count or denominator) | 3 | Five of six models degrade | 5/6 | **All 6 degrade** (powered: only Llama) | **SUPERSEDED** | Results 4.2 | All models with sufficient n degrade. But only Llama is powered (n=45). Others have n=
- `6` (results_FINAL.md:1055, count or denominator) | 3 | Five of six models degrade | 5/6 | **All 6 degrade** (powered: only Llama) | **SUPERSEDED** | Results 4.2 | All models with sufficient n degrade. But only Llama is powered (n=45). Others have n=
- `4.2` (results_FINAL.md:1055, count or denominator) | 3 | Five of six models degrade | 5/6 | **All 6 degrade** (powered: only Llama) | **SUPERSEDED** | Results 4.2 | All models with sufficient n degrade. But only Llama is powered (n=45). Others have n=
- `45` (results_FINAL.md:1055, count or denominator) | 3 | Five of six models degrade | 5/6 | **All 6 degrade** (powered: only Llama) | **SUPERSEDED** | Results 4.2 | All models with sufficient n degrade. But only Llama is powered (n=45). Others have n=
- `0` (results_FINAL.md:1055, count or denominator) | 3 | Five of six models degrade | 5/6 | **All 6 degrade** (powered: only Llama) | **SUPERSEDED** | Results 4.2 | All models with sufficient n degrade. But only Llama is powered (n=45). Others have n=
- `3` (results_FINAL.md:1055, count or denominator) | 3 | Five of six models degrade | 5/6 | **All 6 degrade** (powered: only Llama) | **SUPERSEDED** | Results 4.2 | All models with sufficient n degrade. But only Llama is powered (n=45). Others have n=
- `4` (results_FINAL.md:1056, percentage) | 4 | 83.7% T1-preference (blind reversibility) | 83.7% | **56.2%** (human, stripped) | **SUPERSEDED** | Results 4.3, Abstract, Discussion | 83.7% was model-judge on unstripped (inflated by meta-wrapp
- `83.7` (results_FINAL.md:1056, percentage) | 4 | 83.7% T1-preference (blind reversibility) | 83.7% | **56.2%** (human, stripped) | **SUPERSEDED** | Results 4.3, Abstract, Discussion | 83.7% was model-judge on unstripped (inflated by meta-wrapp
- `83.7` (results_FINAL.md:1056, percentage) | 4 | 83.7% T1-preference (blind reversibility) | 83.7% | **56.2%** (human, stripped) | **SUPERSEDED** | Results 4.3, Abstract, Discussion | 83.7% was model-judge on unstripped (inflated by meta-wrapp
- `56.2` (results_FINAL.md:1056, percentage) | 4 | 83.7% T1-preference (blind reversibility) | 83.7% | **56.2%** (human, stripped) | **SUPERSEDED** | Results 4.3, Abstract, Discussion | 83.7% was model-judge on unstripped (inflated by meta-wrapp
- `4.3` (results_FINAL.md:1056, percentage) | 4 | 83.7% T1-preference (blind reversibility) | 83.7% | **56.2%** (human, stripped) | **SUPERSEDED** | Results 4.3, Abstract, Discussion | 83.7% was model-judge on unstripped (inflated by meta-wrapp
- `83.7` (results_FINAL.md:1056, percentage) | 4 | 83.7% T1-preference (blind reversibility) | 83.7% | **56.2%** (human, stripped) | **SUPERSEDED** | Results 4.3, Abstract, Discussion | 83.7% was model-judge on unstripped (inflated by meta-wrapp
- `56.2` (results_FINAL.md:1056, percentage) | 4 | 83.7% T1-preference (blind reversibility) | 83.7% | **56.2%** (human, stripped) | **SUPERSEDED** | Results 4.3, Abstract, Discussion | 83.7% was model-judge on unstripped (inflated by meta-wrapp
- `5` (results_FINAL.md:1057, percentage) | 5 | 64.3% revision-despite-sufficiency | 64.3% | **39.2%** (CI: 36-42%) | **SUPERSEDED** | Results 4.3, Abstract | Old keyword classifier counted meta as genuine. Corrected: 39.2%. Still shows model
- `64.3` (results_FINAL.md:1057, percentage) | 5 | 64.3% revision-despite-sufficiency | 64.3% | **39.2%** (CI: 36-42%) | **SUPERSEDED** | Results 4.3, Abstract | Old keyword classifier counted meta as genuine. Corrected: 39.2%. Still shows model
- `64.3` (results_FINAL.md:1057, percentage) | 5 | 64.3% revision-despite-sufficiency | 64.3% | **39.2%** (CI: 36-42%) | **SUPERSEDED** | Results 4.3, Abstract | Old keyword classifier counted meta as genuine. Corrected: 39.2%. Still shows model
- `39.2` (results_FINAL.md:1057, percentage) | 5 | 64.3% revision-despite-sufficiency | 64.3% | **39.2%** (CI: 36-42%) | **SUPERSEDED** | Results 4.3, Abstract | Old keyword classifier counted meta as genuine. Corrected: 39.2%. Still shows model
- `36` (results_FINAL.md:1057, percentage) | 5 | 64.3% revision-despite-sufficiency | 64.3% | **39.2%** (CI: 36-42%) | **SUPERSEDED** | Results 4.3, Abstract | Old keyword classifier counted meta as genuine. Corrected: 39.2%. Still shows model
- `42` (results_FINAL.md:1057, percentage) | 5 | 64.3% revision-despite-sufficiency | 64.3% | **39.2%** (CI: 36-42%) | **SUPERSEDED** | Results 4.3, Abstract | Old keyword classifier counted meta as genuine. Corrected: 39.2%. Still shows model
- `4.3` (results_FINAL.md:1057, percentage) | 5 | 64.3% revision-despite-sufficiency | 64.3% | **39.2%** (CI: 36-42%) | **SUPERSEDED** | Results 4.3, Abstract | Old keyword classifier counted meta as genuine. Corrected: 39.2%. Still shows model
- `39.2` (results_FINAL.md:1057, percentage) | 5 | 64.3% revision-despite-sufficiency | 64.3% | **39.2%** (CI: 36-42%) | **SUPERSEDED** | Results 4.3, Abstract | Old keyword classifier counted meta as genuine. Corrected: 39.2%. Still shows model
- `6` (results_FINAL.md:1058, p-value) | 6 | Targeted feedback +2.0 levels (n=424) | +2.00 | **+1.16** stripped (n=177, p=5.7e-19) | **SUPERSEDED** | Results 4.5, Abstract | Unstripped +0.25 was deflated by meta-commentary inflating generi
- `2.0` (results_FINAL.md:1058, p-value) | 6 | Targeted feedback +2.0 levels (n=424) | +2.00 | **+1.16** stripped (n=177, p=5.7e-19) | **SUPERSEDED** | Results 4.5, Abstract | Unstripped +0.25 was deflated by meta-commentary inflating generi
- `424` (results_FINAL.md:1058, p-value) | 6 | Targeted feedback +2.0 levels (n=424) | +2.00 | **+1.16** stripped (n=177, p=5.7e-19) | **SUPERSEDED** | Results 4.5, Abstract | Unstripped +0.25 was deflated by meta-commentary inflating generi
- `2.00` (results_FINAL.md:1058, p-value) | 6 | Targeted feedback +2.0 levels (n=424) | +2.00 | **+1.16** stripped (n=177, p=5.7e-19) | **SUPERSEDED** | Results 4.5, Abstract | Unstripped +0.25 was deflated by meta-commentary inflating generi
- `1.16` (results_FINAL.md:1058, p-value) | 6 | Targeted feedback +2.0 levels (n=424) | +2.00 | **+1.16** stripped (n=177, p=5.7e-19) | **SUPERSEDED** | Results 4.5, Abstract | Unstripped +0.25 was deflated by meta-commentary inflating generi
- `177` (results_FINAL.md:1058, p-value) | 6 | Targeted feedback +2.0 levels (n=424) | +2.00 | **+1.16** stripped (n=177, p=5.7e-19) | **SUPERSEDED** | Results 4.5, Abstract | Unstripped +0.25 was deflated by meta-commentary inflating generi
- `5` (results_FINAL.md:1058, p-value) | 6 | Targeted feedback +2.0 levels (n=424) | +2.00 | **+1.16** stripped (n=177, p=5.7e-19) | **SUPERSEDED** | Results 4.5, Abstract | Unstripped +0.25 was deflated by meta-commentary inflating generi
- `19` (results_FINAL.md:1058, p-value) | 6 | Targeted feedback +2.0 levels (n=424) | +2.00 | **+1.16** stripped (n=177, p=5.7e-19) | **SUPERSEDED** | Results 4.5, Abstract | Unstripped +0.25 was deflated by meta-commentary inflating generi
- `4.5` (results_FINAL.md:1058, p-value) | 6 | Targeted feedback +2.0 levels (n=424) | +2.00 | **+1.16** stripped (n=177, p=5.7e-19) | **SUPERSEDED** | Results 4.5, Abstract | Unstripped +0.25 was deflated by meta-commentary inflating generi
- `0.25` (results_FINAL.md:1058, p-value) | 6 | Targeted feedback +2.0 levels (n=424) | +2.00 | **+1.16** stripped (n=177, p=5.7e-19) | **SUPERSEDED** | Results 4.5, Abstract | Unstripped +0.25 was deflated by meta-commentary inflating generi
- `1.16` (results_FINAL.md:1058, p-value) | 6 | Targeted feedback +2.0 levels (n=424) | +2.00 | **+1.16** stripped (n=177, p=5.7e-19) | **SUPERSEDED** | Results 4.5, Abstract | Unstripped +0.25 was deflated by meta-commentary inflating generi
- `7` (results_FINAL.md:1059, percentage) | 7 | Revision tax 57.4% waste | 57.4% | **62.1%** (Interp A, ratio-of-means) | **SUPERSEDED** | Results 4.6, Abstract | Higher than old keyword (57.4%) because Interp A counts meta-response tokens as
- `57.4` (results_FINAL.md:1059, percentage) | 7 | Revision tax 57.4% waste | 57.4% | **62.1%** (Interp A, ratio-of-means) | **SUPERSEDED** | Results 4.6, Abstract | Higher than old keyword (57.4%) because Interp A counts meta-response tokens as
- `57.4` (results_FINAL.md:1059, percentage) | 7 | Revision tax 57.4% waste | 57.4% | **62.1%** (Interp A, ratio-of-means) | **SUPERSEDED** | Results 4.6, Abstract | Higher than old keyword (57.4%) because Interp A counts meta-response tokens as
- `62.1` (results_FINAL.md:1059, percentage) | 7 | Revision tax 57.4% waste | 57.4% | **62.1%** (Interp A, ratio-of-means) | **SUPERSEDED** | Results 4.6, Abstract | Higher than old keyword (57.4%) because Interp A counts meta-response tokens as
- `4.6` (results_FINAL.md:1059, percentage) | 7 | Revision tax 57.4% waste | 57.4% | **62.1%** (Interp A, ratio-of-means) | **SUPERSEDED** | Results 4.6, Abstract | Higher than old keyword (57.4%) because Interp A counts meta-response tokens as
- `57.4` (results_FINAL.md:1059, percentage) | 7 | Revision tax 57.4% waste | 57.4% | **62.1%** (Interp A, ratio-of-means) | **SUPERSEDED** | Results 4.6, Abstract | Higher than old keyword (57.4%) because Interp A counts meta-response tokens as
- `164.2` (results_FINAL.md:1059, percentage) | 7 | Revision tax 57.4% waste | 57.4% | **62.1%** (Interp A, ratio-of-means) | **SUPERSEDED** | Results 4.6, Abstract | Higher than old keyword (57.4%) because Interp A counts meta-response tokens as
- `8` (results_FINAL.md:1060, percentage) | 8 | Claude tax 251.6% | 251.6 | **251.6%** (unchanged under Interp A) | MATCH | Results 4.6, Table 2 | Claude unchanged; Llama now highest (436.0%). All t*=T1. |
- `251.6` (results_FINAL.md:1060, percentage) | 8 | Claude tax 251.6% | 251.6 | **251.6%** (unchanged under Interp A) | MATCH | Results 4.6, Table 2 | Claude unchanged; Llama now highest (436.0%). All t*=T1. |
- `251.6` (results_FINAL.md:1060, percentage) | 8 | Claude tax 251.6% | 251.6 | **251.6%** (unchanged under Interp A) | MATCH | Results 4.6, Table 2 | Claude unchanged; Llama now highest (436.0%). All t*=T1. |
- `251.6` (results_FINAL.md:1060, percentage) | 8 | Claude tax 251.6% | 251.6 | **251.6%** (unchanged under Interp A) | MATCH | Results 4.6, Table 2 | Claude unchanged; Llama now highest (436.0%). All t*=T1. |
- `4.6` (results_FINAL.md:1060, percentage) | 8 | Claude tax 251.6% | 251.6 | **251.6%** (unchanged under Interp A) | MATCH | Results 4.6, Table 2 | Claude unchanged; Llama now highest (436.0%). All t*=T1. |
- `2` (results_FINAL.md:1060, percentage) | 8 | Claude tax 251.6% | 251.6 | **251.6%** (unchanged under Interp A) | MATCH | Results 4.6, Table 2 | Claude unchanged; Llama now highest (436.0%). All t*=T1. |
- `436.0` (results_FINAL.md:1060, percentage) | 8 | Claude tax 251.6% | 251.6 | **251.6%** (unchanged under Interp A) | MATCH | Results 4.6, Table 2 | Claude unchanged; Llama now highest (436.0%). All t*=T1. |
- `9` (results_FINAL.md:1061, mean or delta) | 9 | Llama t*=2 | T2 | **T1** | **SUPERSEDED** | Results 4.6 | Llama no longer improves; t*=T1 like all others |
- `2` (results_FINAL.md:1061, mean or delta) | 9 | Llama t*=2 | T2 | **T1** | **SUPERSEDED** | Results 4.6 | Llama no longer improves; t*=T1 like all others |
- `4.6` (results_FINAL.md:1061, mean or delta) | 9 | Llama t*=2 | T2 | **T1** | **SUPERSEDED** | Results 4.6 | Llama no longer improves; t*=T1 like all others |
- `10` (results_FINAL.md:1062, percentage) | 10 | Akrasia gap: 48pp between knowledge and action | 48pp | Much smaller | **SUPERSEDED** | Results 4.3, Discussion | 83.7% -> 56.2%, 64.3% -> 39.2%. Gap collapses. Akrasia framing needs substantia
- `4.3` (results_FINAL.md:1062, percentage) | 10 | Akrasia gap: 48pp between knowledge and action | 48pp | Much smaller | **SUPERSEDED** | Results 4.3, Discussion | 83.7% -> 56.2%, 64.3% -> 39.2%. Gap collapses. Akrasia framing needs substantia
- `83.7` (results_FINAL.md:1062, percentage) | 10 | Akrasia gap: 48pp between knowledge and action | 48pp | Much smaller | **SUPERSEDED** | Results 4.3, Discussion | 83.7% -> 56.2%, 64.3% -> 39.2%. Gap collapses. Akrasia framing needs substantia
- `56.2` (results_FINAL.md:1062, percentage) | 10 | Akrasia gap: 48pp between knowledge and action | 48pp | Much smaller | **SUPERSEDED** | Results 4.3, Discussion | 83.7% -> 56.2%, 64.3% -> 39.2%. Gap collapses. Akrasia framing needs substantia
- `64.3` (results_FINAL.md:1062, percentage) | 10 | Akrasia gap: 48pp between knowledge and action | 48pp | Much smaller | **SUPERSEDED** | Results 4.3, Discussion | 83.7% -> 56.2%, 64.3% -> 39.2%. Gap collapses. Akrasia framing needs substantia
- `39.2` (results_FINAL.md:1062, percentage) | 10 | Akrasia gap: 48pp between knowledge and action | 48pp | Much smaller | **SUPERSEDED** | Results 4.3, Discussion | 83.7% -> 56.2%, 64.3% -> 39.2%. Gap collapses. Akrasia framing needs substantia
- `11` (results_FINAL.md:1063, percentage) | 11 | Self-reflection mean 2.44, 40% T1 | 2.44 | **2.44** | UNCHANGED | Results 4.3 | No change needed |
- `2.44` (results_FINAL.md:1063, percentage) | 11 | Self-reflection mean 2.44, 40% T1 | 2.44 | **2.44** | UNCHANGED | Results 4.3 | No change needed |
- `40` (results_FINAL.md:1063, percentage) | 11 | Self-reflection mean 2.44, 40% T1 | 2.44 | **2.44** | UNCHANGED | Results 4.3 | No change needed |
- `2.44` (results_FINAL.md:1063, percentage) | 11 | Self-reflection mean 2.44, 40% T1 | 2.44 | **2.44** | UNCHANGED | Results 4.3 | No change needed |
- `2.44` (results_FINAL.md:1063, percentage) | 11 | Self-reflection mean 2.44, 40% T1 | 2.44 | **2.44** | UNCHANGED | Results 4.3 | No change needed |
- `4.3` (results_FINAL.md:1063, percentage) | 11 | Self-reflection mean 2.44, 40% T1 | 2.44 | **2.44** | UNCHANGED | Results 4.3 | No change needed |
- `12` (results_FINAL.md:1064, mean or delta) | 12 | Edit ratio 0.97 | 0.97 | **0.97** | UNCHANGED | Results 4.4 | No change needed |
- `0.97` (results_FINAL.md:1064, mean or delta) | 12 | Edit ratio 0.97 | 0.97 | **0.97** | UNCHANGED | Results 4.4 | No change needed |
- `0.97` (results_FINAL.md:1064, mean or delta) | 12 | Edit ratio 0.97 | 0.97 | **0.97** | UNCHANGED | Results 4.4 | No change needed |
- `0.97` (results_FINAL.md:1064, mean or delta) | 12 | Edit ratio 0.97 | 0.97 | **0.97** | UNCHANGED | Results 4.4 | No change needed |
- `4.4` (results_FINAL.md:1064, mean or delta) | 12 | Edit ratio 0.97 | 0.97 | **0.97** | UNCHANGED | Results 4.4 | No change needed |
- `13` (results_FINAL.md:1065, mean or delta) | 13 | Content drift slopes (instruction adherence, semantic similarity, word count) | various | UNKNOWN | **NEEDS RECOMPUTATION** | Results 4.4 | These were computed on all turns including meta. Need
- `4.4` (results_FINAL.md:1065, mean or delta) | 13 | Content drift slopes (instruction adherence, semantic similarity, word count) | various | UNKNOWN | **NEEDS RECOMPUTATION** | Results 4.4 | These were computed on all turns including meta. Need
- `14` (results_FINAL.md:1066, percentage) | 14 | Structural features drop 56% | 56% | UNKNOWN | **NEEDS RECOMPUTATION** | Results 4.4 | Same issue |
- `56` (results_FINAL.md:1066, percentage) | 14 | Structural features drop 56% | 56% | UNKNOWN | **NEEDS RECOMPUTATION** | Results 4.4 | Same issue |
- `56` (results_FINAL.md:1066, percentage) | 14 | Structural features drop 56% | 56% | UNKNOWN | **NEEDS RECOMPUTATION** | Results 4.4 | Same issue |
- `4.4` (results_FINAL.md:1066, percentage) | 14 | Structural features drop 56% | 56% | UNKNOWN | **NEEDS RECOMPUTATION** | Results 4.4 | Same issue |
- `15` (results_FINAL.md:1067, percentage) | 15 | Constraint loss 58.5% | 58.5% | UNKNOWN | **NEEDS RECOMPUTATION** | Results 4.4 | Same issue |
- `58.5` (results_FINAL.md:1067, percentage) | 15 | Constraint loss 58.5% | 58.5% | UNKNOWN | **NEEDS RECOMPUTATION** | Results 4.4 | Same issue |
- `58.5` (results_FINAL.md:1067, percentage) | 15 | Constraint loss 58.5% | 58.5% | UNKNOWN | **NEEDS RECOMPUTATION** | Results 4.4 | Same issue |
- `4.4` (results_FINAL.md:1067, percentage) | 15 | Constraint loss 58.5% | 58.5% | UNKNOWN | **NEEDS RECOMPUTATION** | Results 4.4 | Same issue |
- `16` (results_FINAL.md:1068, percentage) | 16 | Enterprise projection $21K-$72K | $21-72K | Lower (tax% dropped) | **SUPERSEDED** | Results 4.6 | Recompute from corrected per-model $/task waste |
- `21` (results_FINAL.md:1068, percentage) | 16 | Enterprise projection $21K-$72K | $21-72K | Lower (tax% dropped) | **SUPERSEDED** | Results 4.6 | Recompute from corrected per-model $/task waste |
- `4.6` (results_FINAL.md:1068, percentage) | 16 | Enterprise projection $21K-$72K | $21-72K | Lower (tax% dropped) | **SUPERSEDED** | Results 4.6 | Recompute from corrected per-model $/task waste |
- `17` (results_FINAL.md:1069, mean or delta) | 17 | DRP = Turn 2 for all degrading models | T2 | Likely unchanged conceptually | **NEEDS VERIFICATION** | Results 4.1 | Verify on corrected GENUINE-only trajectories |
- `2` (results_FINAL.md:1069, mean or delta) | 17 | DRP = Turn 2 for all degrading models | T2 | Likely unchanged conceptually | **NEEDS VERIFICATION** | Results 4.1 | Verify on corrected GENUINE-only trajectories |
- `4.1` (results_FINAL.md:1069, mean or delta) | 17 | DRP = Turn 2 for all degrading models | T2 | Likely unchanged conceptually | **NEEDS VERIFICATION** | Results 4.1 | Verify on corrected GENUINE-only trajectories |
- `18` (results_FINAL.md:1070, percentage) | 18 | T1 sufficiency 93.3% | 93.3% | **87.6%** (or both: check denominator) | **NEEDS VERIFICATION** | Methods, Results 4.3 | Paper may have used different denominator or pre-6->2 recoding |
- `93.3` (results_FINAL.md:1070, percentage) | 18 | T1 sufficiency 93.3% | 93.3% | **87.6%** (or both: check denominator) | **NEEDS VERIFICATION** | Methods, Results 4.3 | Paper may have used different denominator or pre-6->2 recoding |
- `93.3` (results_FINAL.md:1070, percentage) | 18 | T1 sufficiency 93.3% | 93.3% | **87.6%** (or both: check denominator) | **NEEDS VERIFICATION** | Methods, Results 4.3 | Paper may have used different denominator or pre-6->2 recoding |
- `87.6` (results_FINAL.md:1070, percentage) | 18 | T1 sufficiency 93.3% | 93.3% | **87.6%** (or both: check denominator) | **NEEDS VERIFICATION** | Methods, Results 4.3 | Paper may have used different denominator or pre-6->2 recoding |
- `4.3` (results_FINAL.md:1070, percentage) | 18 | T1 sufficiency 93.3% | 93.3% | **87.6%** (or both: check denominator) | **NEEDS VERIFICATION** | Methods, Results 4.3 | Paper may have used different denominator or pre-6->2 recoding |
- `6` (results_FINAL.md:1070, percentage) | 18 | T1 sufficiency 93.3% | 93.3% | **87.6%** (or both: check denominator) | **NEEDS VERIFICATION** | Methods, Results 4.3 | Paper may have used different denominator or pre-6->2 recoding |
- `2` (results_FINAL.md:1070, percentage) | 18 | T1 sufficiency 93.3% | 93.3% | **87.6%** (or both: check denominator) | **NEEDS VERIFICATION** | Methods, Results 4.3 | Paper may have used different denominator or pre-6->2 recoding |
- `19` (results_FINAL.md:1071, percentage) | 19 | Study 1: 99.9% vs 23.2% | 99.9/23.2 | **99.9/23.2** | UNCHANGED | Results (appendix) | |
- `1` (results_FINAL.md:1071, percentage) | 19 | Study 1: 99.9% vs 23.2% | 99.9/23.2 | **99.9/23.2** | UNCHANGED | Results (appendix) | |
- `99.9` (results_FINAL.md:1071, percentage) | 19 | Study 1: 99.9% vs 23.2% | 99.9/23.2 | **99.9/23.2** | UNCHANGED | Results (appendix) | |
- `23.2` (results_FINAL.md:1071, percentage) | 19 | Study 1: 99.9% vs 23.2% | 99.9/23.2 | **99.9/23.2** | UNCHANGED | Results (appendix) | |
- `99.9` (results_FINAL.md:1071, percentage) | 19 | Study 1: 99.9% vs 23.2% | 99.9/23.2 | **99.9/23.2** | UNCHANGED | Results (appendix) | |
- `23.2` (results_FINAL.md:1071, percentage) | 19 | Study 1: 99.9% vs 23.2% | 99.9/23.2 | **99.9/23.2** | UNCHANGED | Results (appendix) | |
- `99.9` (results_FINAL.md:1071, percentage) | 19 | Study 1: 99.9% vs 23.2% | 99.9/23.2 | **99.9/23.2** | UNCHANGED | Results (appendix) | |
- `23.2` (results_FINAL.md:1071, percentage) | 19 | Study 1: 99.9% vs 23.2% | 99.9/23.2 | **99.9/23.2** | UNCHANGED | Results (appendix) | |
- `20` (results_FINAL.md:1072, percentage) | 20 | Study 2: GPT-4o 98% momentum | 98% | **98%** | UNCHANGED | Results (appendix) | |
- `2` (results_FINAL.md:1072, percentage) | 20 | Study 2: GPT-4o 98% momentum | 98% | **98%** | UNCHANGED | Results (appendix) | |
- `98` (results_FINAL.md:1072, percentage) | 20 | Study 2: GPT-4o 98% momentum | 98% | **98%** | UNCHANGED | Results (appendix) | |
- `98` (results_FINAL.md:1072, percentage) | 20 | Study 2: GPT-4o 98% momentum | 98% | **98%** | UNCHANGED | Results (appendix) | |
- `98` (results_FINAL.md:1072, percentage) | 20 | Study 2: GPT-4o 98% momentum | 98% | **98%** | UNCHANGED | Results (appendix) | |
- `21` (results_FINAL.md:1073, percentage) | 21 | QWK 0.228, binary 73.4% | 0.228/73.4 | QW kappa 0.41-0.60 (3 pairs), binary 76.6-82.8%, alpha 0.529 | **SUPERSEDED** | Methods 3.3 | Old 0.228 was linear-weighted, 2-rater, no 6->2 recode. Now 
- `0.228` (results_FINAL.md:1073, percentage) | 21 | QWK 0.228, binary 73.4% | 0.228/73.4 | QW kappa 0.41-0.60 (3 pairs), binary 76.6-82.8%, alpha 0.529 | **SUPERSEDED** | Methods 3.3 | Old 0.228 was linear-weighted, 2-rater, no 6->2 recode. Now 
- `73.4` (results_FINAL.md:1073, percentage) | 21 | QWK 0.228, binary 73.4% | 0.228/73.4 | QW kappa 0.41-0.60 (3 pairs), binary 76.6-82.8%, alpha 0.529 | **SUPERSEDED** | Methods 3.3 | Old 0.228 was linear-weighted, 2-rater, no 6->2 recode. Now 
- `0.228` (results_FINAL.md:1073, percentage) | 21 | QWK 0.228, binary 73.4% | 0.228/73.4 | QW kappa 0.41-0.60 (3 pairs), binary 76.6-82.8%, alpha 0.529 | **SUPERSEDED** | Methods 3.3 | Old 0.228 was linear-weighted, 2-rater, no 6->2 recode. Now 
- `73.4` (results_FINAL.md:1073, percentage) | 21 | QWK 0.228, binary 73.4% | 0.228/73.4 | QW kappa 0.41-0.60 (3 pairs), binary 76.6-82.8%, alpha 0.529 | **SUPERSEDED** | Methods 3.3 | Old 0.228 was linear-weighted, 2-rater, no 6->2 recode. Now 
- `0.41` (results_FINAL.md:1073, percentage) | 21 | QWK 0.228, binary 73.4% | 0.228/73.4 | QW kappa 0.41-0.60 (3 pairs), binary 76.6-82.8%, alpha 0.529 | **SUPERSEDED** | Methods 3.3 | Old 0.228 was linear-weighted, 2-rater, no 6->2 recode. Now 
- `0.60` (results_FINAL.md:1073, percentage) | 21 | QWK 0.228, binary 73.4% | 0.228/73.4 | QW kappa 0.41-0.60 (3 pairs), binary 76.6-82.8%, alpha 0.529 | **SUPERSEDED** | Methods 3.3 | Old 0.228 was linear-weighted, 2-rater, no 6->2 recode. Now 
- `3` (results_FINAL.md:1073, percentage) | 21 | QWK 0.228, binary 73.4% | 0.228/73.4 | QW kappa 0.41-0.60 (3 pairs), binary 76.6-82.8%, alpha 0.529 | **SUPERSEDED** | Methods 3.3 | Old 0.228 was linear-weighted, 2-rater, no 6->2 recode. Now 
- `76.6` (results_FINAL.md:1073, percentage) | 21 | QWK 0.228, binary 73.4% | 0.228/73.4 | QW kappa 0.41-0.60 (3 pairs), binary 76.6-82.8%, alpha 0.529 | **SUPERSEDED** | Methods 3.3 | Old 0.228 was linear-weighted, 2-rater, no 6->2 recode. Now 
- `82.8` (results_FINAL.md:1073, percentage) | 21 | QWK 0.228, binary 73.4% | 0.228/73.4 | QW kappa 0.41-0.60 (3 pairs), binary 76.6-82.8%, alpha 0.529 | **SUPERSEDED** | Methods 3.3 | Old 0.228 was linear-weighted, 2-rater, no 6->2 recode. Now 
- `0.529` (results_FINAL.md:1073, percentage) | 21 | QWK 0.228, binary 73.4% | 0.228/73.4 | QW kappa 0.41-0.60 (3 pairs), binary 76.6-82.8%, alpha 0.529 | **SUPERSEDED** | Methods 3.3 | Old 0.228 was linear-weighted, 2-rater, no 6->2 recode. Now 
- `3.3` (results_FINAL.md:1073, percentage) | 21 | QWK 0.228, binary 73.4% | 0.228/73.4 | QW kappa 0.41-0.60 (3 pairs), binary 76.6-82.8%, alpha 0.529 | **SUPERSEDED** | Methods 3.3 | Old 0.228 was linear-weighted, 2-rater, no 6->2 recode. Now 
- `0.228` (results_FINAL.md:1073, percentage) | 21 | QWK 0.228, binary 73.4% | 0.228/73.4 | QW kappa 0.41-0.60 (3 pairs), binary 76.6-82.8%, alpha 0.529 | **SUPERSEDED** | Methods 3.3 | Old 0.228 was linear-weighted, 2-rater, no 6->2 recode. Now 
- `2` (results_FINAL.md:1073, percentage) | 21 | QWK 0.228, binary 73.4% | 0.228/73.4 | QW kappa 0.41-0.60 (3 pairs), binary 76.6-82.8%, alpha 0.529 | **SUPERSEDED** | Methods 3.3 | Old 0.228 was linear-weighted, 2-rater, no 6->2 recode. Now 
- `6` (results_FINAL.md:1073, percentage) | 21 | QWK 0.228, binary 73.4% | 0.228/73.4 | QW kappa 0.41-0.60 (3 pairs), binary 76.6-82.8%, alpha 0.529 | **SUPERSEDED** | Methods 3.3 | Old 0.228 was linear-weighted, 2-rater, no 6->2 recode. Now 
- `2` (results_FINAL.md:1073, percentage) | 21 | QWK 0.228, binary 73.4% | 0.228/73.4 | QW kappa 0.41-0.60 (3 pairs), binary 76.6-82.8%, alpha 0.529 | **SUPERSEDED** | Methods 3.3 | Old 0.228 was linear-weighted, 2-rater, no 6->2 recode. Now 
- `3` (results_FINAL.md:1073, percentage) | 21 | QWK 0.228, binary 73.4% | 0.228/73.4 | QW kappa 0.41-0.60 (3 pairs), binary 76.6-82.8%, alpha 0.529 | **SUPERSEDED** | Methods 3.3 | Old 0.228 was linear-weighted, 2-rater, no 6->2 recode. Now 
- `6` (results_FINAL.md:1073, percentage) | 21 | QWK 0.228, binary 73.4% | 0.228/73.4 | QW kappa 0.41-0.60 (3 pairs), binary 76.6-82.8%, alpha 0.529 | **SUPERSEDED** | Methods 3.3 | Old 0.228 was linear-weighted, 2-rater, no 6->2 recode. Now 
- `2` (results_FINAL.md:1073, percentage) | 21 | QWK 0.228, binary 73.4% | 0.228/73.4 | QW kappa 0.41-0.60 (3 pairs), binary 76.6-82.8%, alpha 0.529 | **SUPERSEDED** | Methods 3.3 | Old 0.228 was linear-weighted, 2-rater, no 6->2 recode. Now 

### [results_FINAL.md] NEW Claims (not in current draft)

*- **Filter (exact):** `data/processed/scored_trials.jsonl`, factorial scope only (probe_type in*

- `91.8` (results_FINAL.md:1079, percentage) | N1 | Meta-commentary inflates LLM-judge T1-preference | 91.8% -> 56.5% stripped (same 50 pairs) | Results (new) | Major methods contribution. Model judges are unreliable on revision comparison unles
- `56.5` (results_FINAL.md:1079, percentage) | N1 | Meta-commentary inflates LLM-judge T1-preference | 91.8% -> 56.5% stripped (same 50 pairs) | Results (new) | Major methods contribution. Model judges are unreliable on revision comparison unles
- `50` (results_FINAL.md:1079, percentage) | N1 | Meta-commentary inflates LLM-judge T1-preference | 91.8% -> 56.5% stripped (same 50 pairs) | Results (new) | Major methods contribution. Model judges are unreliable on revision comparison unles
- `84` (results_FINAL.md:1080, percentage) | N2 | Meta-wrapping asymmetry | 84% revision, 14% T1 | Results/Methods (new) | Confound for any LLM-as-judge revision study. |
- `14` (results_FINAL.md:1080, percentage) | N2 | Meta-wrapping asymmetry | 84% revision, 14% T1 | Results/Methods (new) | Confound for any LLM-as-judge revision study. |
- `56.2` (results_FINAL.md:1081, percentage) | N3 | Human reversibility with inter-annotator agreement | 56.2%, kappa=0.703 | Results (new) | Replaces model-judge reversibility as primary evidence. |
- `0.703` (results_FINAL.md:1081, percentage) | N3 | Human reversibility with inter-annotator agreement | 56.2%, kappa=0.703 | Results (new) | Replaces model-judge reversibility as primary evidence. |
- `1.4` (results_FINAL.md:1082, percentage) | N4 | Classifier difficulty (verbose decline) | 1.4% correction rate, 85 trials reclassified | Methods (new) | The keyword/LLM classifier gap is itself a finding about model behavior. |
- `85` (results_FINAL.md:1082, percentage) | N4 | Classifier difficulty (verbose decline) | 1.4% correction rate, 85 trials reclassified | Methods (new) | The keyword/LLM classifier gap is itself a finding about model behavior. |
- `81` (results_FINAL.md:1083, percentage) | N5 | Cliff is 81% content degradation, 19% meta-inflation | -0.76 stripped vs -0.94 | Results (new) | Validates cliff survives meta-stripping. |
- `19` (results_FINAL.md:1083, percentage) | N5 | Cliff is 81% content degradation, 19% meta-inflation | -0.76 stripped vs -0.94 | Results (new) | Validates cliff survives meta-stripping. |
- `0.76` (results_FINAL.md:1083, percentage) | N5 | Cliff is 81% content degradation, 19% meta-inflation | -0.76 stripped vs -0.94 | Results (new) | Validates cliff survives meta-stripping. |
- `0.94` (results_FINAL.md:1083, percentage) | N5 | Cliff is 81% content degradation, 19% meta-inflation | -0.76 stripped vs -0.94 | Results (new) | Validates cliff survives meta-stripping. |
- `0` (results_FINAL.md:1084, reliability or effect size) | N6 | Human-judge agreement improves from kappa ~0 to 0.57 after stripping | 0.57 | Results (new) | Demonstrates meta-commentary is the source of judge-human disagreement. |
- `0.57` (results_FINAL.md:1084, reliability or effect size) | N6 | Human-judge agreement improves from kappa ~0 to 0.57 after stripping | 0.57 | Results (new) | Demonstrates meta-commentary is the source of judge-human disagreement. |
- `0.57` (results_FINAL.md:1084, reliability or effect size) | N6 | Human-judge agreement improves from kappa ~0 to 0.57 after stripping | 0.57 | Results (new) | Demonstrates meta-commentary is the source of judge-human disagreement. |
- `6` (results_FINAL.md:1090, bare number) All numbers below use corrected LLM classifier (GENUINE-only), 6->2 recode, computed fresh from source data.
- `2` (results_FINAL.md:1090, bare number) All numbers below use corrected LLM classifier (GENUINE-only), 6->2 recode, computed fresh from source data.

### [results_FINAL.md] S1. Content Drift Slopes (GENUINE-only)

*- **Filter (exact):** `data/processed/scored_trials.jsonl`, factorial scope only (probe_type in*

- `50.9` (results_FINAL.md:1096, p-value) | Word count slope | -50.9/turn (p=2.8e-19, n=576) | **+19.4/turn** (p=1.9e-8, n=356) | **YES: FLIPS SIGN** |
- `2` (results_FINAL.md:1096, p-value) | Word count slope | -50.9/turn (p=2.8e-19, n=576) | **+19.4/turn** (p=1.9e-8, n=356) | **YES: FLIPS SIGN** |
- `19` (results_FINAL.md:1096, p-value) | Word count slope | -50.9/turn (p=2.8e-19, n=576) | **+19.4/turn** (p=1.9e-8, n=356) | **YES: FLIPS SIGN** |
- `576` (results_FINAL.md:1096, p-value) | Word count slope | -50.9/turn (p=2.8e-19, n=576) | **+19.4/turn** (p=1.9e-8, n=356) | **YES: FLIPS SIGN** |
- `19.4` (results_FINAL.md:1096, p-value) | Word count slope | -50.9/turn (p=2.8e-19, n=576) | **+19.4/turn** (p=1.9e-8, n=356) | **YES: FLIPS SIGN** |
- `1` (results_FINAL.md:1096, p-value) | Word count slope | -50.9/turn (p=2.8e-19, n=576) | **+19.4/turn** (p=1.9e-8, n=356) | **YES: FLIPS SIGN** |
- `8` (results_FINAL.md:1096, p-value) | Word count slope | -50.9/turn (p=2.8e-19, n=576) | **+19.4/turn** (p=1.9e-8, n=356) | **YES: FLIPS SIGN** |
- `356` (results_FINAL.md:1096, p-value) | Word count slope | -50.9/turn (p=2.8e-19, n=576) | **+19.4/turn** (p=1.9e-8, n=356) | **YES: FLIPS SIGN** |
- `289` (results_FINAL.md:1097, bare number) | Word count T1->T5 | 289->186 | **289->341** | **YES: INCREASES** |
- `186` (results_FINAL.md:1097, bare number) | Word count T1->T5 | 289->186 | **289->341** | **YES: INCREASES** |
- `289` (results_FINAL.md:1097, bare number) | Word count T1->T5 | 289->186 | **289->341** | **YES: INCREASES** |
- `341` (results_FINAL.md:1097, bare number) | Word count T1->T5 | 289->186 | **289->341** | **YES: INCREASES** |
- `1980` (results_FINAL.md:1098, bare number) | Char count T1->T5 | 1980->1280 | **1980->2426** | **YES: INCREASES** |
- `1280` (results_FINAL.md:1098, bare number) | Char count T1->T5 | 1980->1280 | **1980->2426** | **YES: INCREASES** |
- `1980` (results_FINAL.md:1098, bare number) | Char count T1->T5 | 1980->1280 | **1980->2426** | **YES: INCREASES** |
- `2426` (results_FINAL.md:1098, bare number) | Char count T1->T5 | 1980->1280 | **1980->2426** | **YES: INCREASES** |
- `50` (results_FINAL.md:1100, mean or delta) **The word-count decline was entirely a meta-response artifact.** Short decline messages (50-200 chars) drove the old -50.9 slope. Genuine revisions are LONGER than T1.
- `200` (results_FINAL.md:1100, mean or delta) **The word-count decline was entirely a meta-response artifact.** Short decline messages (50-200 chars) drove the old -50.9 slope. Genuine revisions are LONGER than T1.
- `50.9` (results_FINAL.md:1100, mean or delta) **The word-count decline was entirely a meta-response artifact.** Short decline messages (50-200 chars) drove the old -50.9 slope. Genuine revisions are LONGER than T1.
- `720` (results_FINAL.md:1102, count or denominator) - **Filter:** For each trial, include T1 (all 720) and turns 2-5 only where `genuine_meta_labels.jsonl` has `classifier_label == "GENUINE"`. Per-trial slope via `scipy.stats.linregress` on (turn, word
- `2` (results_FINAL.md:1102, count or denominator) - **Filter:** For each trial, include T1 (all 720) and turns 2-5 only where `genuine_meta_labels.jsonl` has `classifier_label == "GENUINE"`. Per-trial slope via `scipy.stats.linregress` on (turn, word
- `5` (results_FINAL.md:1102, count or denominator) - **Filter:** For each trial, include T1 (all 720) and turns 2-5 only where `genuine_meta_labels.jsonl` has `classifier_label == "GENUINE"`. Per-trial slope via `scipy.stats.linregress` on (turn, word
- `356` (results_FINAL.md:1102, count or denominator) - **Filter:** For each trial, include T1 (all 720) and turns 2-5 only where `genuine_meta_labels.jsonl` has `classifier_label == "GENUINE"`. Per-trial slope via `scipy.stats.linregress` on (turn, word

### [results_FINAL.md] S2. Structural Features (GENUINE-only)

*- **Filter:** For each trial, include T1 (all 720) and turns 2-5 only where `genuine_meta_labels.jsonl` has `classifier_label == "GENUINE"`. Per-trial slope via `scipy.stats.linregress` on (turn, word_count). T-test on n=356 per-trial slopes.*

- `7.47` (results_FINAL.md:1108, mean or delta) | T1 | 7.47 | 12.52 | 720 |
- `12.52` (results_FINAL.md:1108, mean or delta) | T1 | 7.47 | 12.52 | 720 |
- `720` (results_FINAL.md:1108, mean or delta) | T1 | 7.47 | 12.52 | 720 |
- `5.0` (results_FINAL.md:1109, mean or delta) | T2 | ~5.0 | 10.34 | 283 |
- `10.34` (results_FINAL.md:1109, mean or delta) | T2 | ~5.0 | 10.34 | 283 |
- `283` (results_FINAL.md:1109, mean or delta) | T2 | ~5.0 | 10.34 | 283 |
- `3.3` (results_FINAL.md:1110, mean or delta) | T5 | ~3.3 | 9.00 | 96 |
- `9.00` (results_FINAL.md:1110, mean or delta) | T5 | ~3.3 | 9.00 | 96 |
- `96` (results_FINAL.md:1110, mean or delta) | T5 | ~3.3 | 9.00 | 96 |
- `56` (results_FINAL.md:1114, percentage) | T1->T5 drop | ~56% | **28.1%** |
- `28.1` (results_FINAL.md:1114, percentage) | T1->T5 drop | ~56% | **28.1%** |
- `28.1` (results_FINAL.md:1117, percentage) - Note: old and new `total_structure` definitions differ slightly (old counted fewer features). The 28.1% drop and new raw counts are the definitive numbers.

### [results_FINAL.md] S3. Constraint Satisfaction (GENUINE-only)

*- **Filter:** Regex counts of headers, bullets, numbered items, code blocks, bold phrases per response. GENUINE-only turns. Old numbers used all turns including meta-responses (which had minimal structure).*

- `0.077` (results_FINAL.md:1123, p-value) | Constraint recall slope | -0.077 (p=7.4e-40, n=576) | **+0.002** (p=0.58, NS, n=356) | **YES: GOES NS** |
- `7` (results_FINAL.md:1123, p-value) | Constraint recall slope | -0.077 (p=7.4e-40, n=576) | **+0.002** (p=0.58, NS, n=356) | **YES: GOES NS** |
- `40` (results_FINAL.md:1123, p-value) | Constraint recall slope | -0.077 (p=7.4e-40, n=576) | **+0.002** (p=0.58, NS, n=356) | **YES: GOES NS** |
- `576` (results_FINAL.md:1123, p-value) | Constraint recall slope | -0.077 (p=7.4e-40, n=576) | **+0.002** (p=0.58, NS, n=356) | **YES: GOES NS** |
- `0.002` (results_FINAL.md:1123, p-value) | Constraint recall slope | -0.077 (p=7.4e-40, n=576) | **+0.002** (p=0.58, NS, n=356) | **YES: GOES NS** |
- `0.58` (results_FINAL.md:1123, p-value) | Constraint recall slope | -0.077 (p=7.4e-40, n=576) | **+0.002** (p=0.58, NS, n=356) | **YES: GOES NS** |
- `356` (results_FINAL.md:1123, p-value) | Constraint recall slope | -0.077 (p=7.4e-40, n=576) | **+0.002** (p=0.58, NS, n=356) | **YES: GOES NS** |
- `10` (results_FINAL.md:1124, percentage) | >10% drop T1->T5 | 58.5% | **17.7%** (17/96) | **YES** |
- `58.5` (results_FINAL.md:1124, percentage) | >10% drop T1->T5 | 58.5% | **17.7%** (17/96) | **YES** |
- `17.7` (results_FINAL.md:1124, percentage) | >10% drop T1->T5 | 58.5% | **17.7%** (17/96) | **YES** |
- `17` (results_FINAL.md:1124, percentage) | >10% drop T1->T5 | 58.5% | **17.7%** (17/96) | **YES** |
- `96` (results_FINAL.md:1124, percentage) | >10% drop T1->T5 | 58.5% | **17.7%** (17/96) | **YES** |
- `0.491` (results_FINAL.md:1125, mean or delta) | Recall T1 | 0.491 | 0.491 | Match |
- `0.491` (results_FINAL.md:1125, mean or delta) | Recall T1 | 0.491 | 0.491 | Match |
- `0.290` (results_FINAL.md:1126, mean or delta) | Recall T5 | 0.290 | **0.483** | **YES** |
- `0.483` (results_FINAL.md:1126, mean or delta) | Recall T5 | 0.290 | **0.483** | **YES** |
- `0.077` (results_FINAL.md:1128, percentage) **Constraint loss was largely a meta-response artifact.** Meta-responses (short declines) have near-zero keyword overlap with the task prompt, which drove the old -0.077 slope. Genuine revisions maint
- `49` (results_FINAL.md:1128, percentage) **Constraint loss was largely a meta-response artifact.** Meta-responses (short declines) have near-zero keyword overlap with the task prompt, which drove the old -0.077 slope. Genuine revisions maint
- `4` (results_FINAL.md:1130, p-value) - **Filter:** Keyword overlap (words >= 4 chars) between `task_prompt` and response. GENUINE-only turns. Per-trial slope via polyfit. >10% drop = trials with balanced panel (GENUINE at T5) where T1_re
- `10` (results_FINAL.md:1130, p-value) - **Filter:** Keyword overlap (words >= 4 chars) between `task_prompt` and response. GENUINE-only turns. Per-trial slope via polyfit. >10% drop = trials with balanced panel (GENUINE at T5) where T1_re
- `0.10` (results_FINAL.md:1130, p-value) - **Filter:** Keyword overlap (words >= 4 chars) between `task_prompt` and response. GENUINE-only turns. Per-trial slope via polyfit. >10% drop = trials with balanced panel (GENUINE at T5) where T1_re

### [results_FINAL.md] S4. Edit Ratio & Semantic Similarity (GENUINE-only)

*- **Filter:** Keyword overlap (words >= 4 chars) between `task_prompt` and response. GENUINE-only turns. Per-trial slope via polyfit. >10% drop = trials with balanced panel (GENUINE at T5) where T1_recall - T5_recall > 0.10.*

- `0.97` (results_FINAL.md:1136, mean or delta) | Edit ratio (overall) | 0.97 | **0.61** | **YES** |
- `0.61` (results_FINAL.md:1136, mean or delta) | Edit ratio (overall) | 0.97 | **0.61** | **YES** |
- `0.51` (results_FINAL.md:1137, mean or delta) | Semantic drift T1->T5 | 0.51->0.37 | **0.54->0.48** | Moderate |
- `0.37` (results_FINAL.md:1137, mean or delta) | Semantic drift T1->T5 | 0.51->0.37 | **0.54->0.48** | Moderate |
- `0.54` (results_FINAL.md:1137, mean or delta) | Semantic drift T1->T5 | 0.51->0.37 | **0.54->0.48** | Moderate |
- `0.48` (results_FINAL.md:1137, mean or delta) | Semantic drift T1->T5 | 0.51->0.37 | **0.54->0.48** | Moderate |
- `0.048` (results_FINAL.md:1138, p-value) | Drift slope | -0.048 (p=2.9e-11, n=428) | **-0.038** (p=3.0e-21, n=205) | Minor |
- `2` (results_FINAL.md:1138, p-value) | Drift slope | -0.048 (p=2.9e-11, n=428) | **-0.038** (p=3.0e-21, n=205) | Minor |
- `11` (results_FINAL.md:1138, p-value) | Drift slope | -0.048 (p=2.9e-11, n=428) | **-0.038** (p=3.0e-21, n=205) | Minor |
- `428` (results_FINAL.md:1138, p-value) | Drift slope | -0.048 (p=2.9e-11, n=428) | **-0.038** (p=3.0e-21, n=205) | Minor |
- `0.038` (results_FINAL.md:1138, p-value) | Drift slope | -0.048 (p=2.9e-11, n=428) | **-0.038** (p=3.0e-21, n=205) | Minor |
- `3` (results_FINAL.md:1138, p-value) | Drift slope | -0.048 (p=2.9e-11, n=428) | **-0.038** (p=3.0e-21, n=205) | Minor |
- `21` (results_FINAL.md:1138, p-value) | Drift slope | -0.048 (p=2.9e-11, n=428) | **-0.038** (p=3.0e-21, n=205) | Minor |
- `205` (results_FINAL.md:1138, p-value) | Drift slope | -0.048 (p=2.9e-11, n=428) | **-0.038** (p=3.0e-21, n=205) | Minor |
- `0.97` (results_FINAL.md:1140, percentage) The old 0.97 edit ratio included meta-responses which repeat content verbatim. Genuine revisions change ~61% of the text.
- `61` (results_FINAL.md:1140, percentage) The old 0.97 edit ratio included meta-responses which repeat content verbatim. Genuine revisions change ~61% of the text.
- `1` (results_FINAL.md:1142, bare number) - **Filter (edit ratio):** `difflib.SequenceMatcher` ratio between consecutive GENUINE turns. 1 - ratio = fraction changed.

### [results_FINAL.md] S5. Per-Model Table

*- **Filter (semantic sim):** Word-overlap Jaccard between T1 and each GENUINE turn. Per-trial slope via polyfit.*

- `2` (results_FINAL.md:1147, count or denominator) Already in Section 2 (balanced panel n=50: Llama 45, Qwen 3, Claude 2, others 0). No further recomputation needed.
- `50` (results_FINAL.md:1147, count or denominator) Already in Section 2 (balanced panel n=50: Llama 45, Qwen 3, Claude 2, others 0). No further recomputation needed.
- `45` (results_FINAL.md:1147, count or denominator) Already in Section 2 (balanced panel n=50: Llama 45, Qwen 3, Claude 2, others 0). No further recomputation needed.
- `3` (results_FINAL.md:1147, count or denominator) Already in Section 2 (balanced panel n=50: Llama 45, Qwen 3, Claude 2, others 0). No further recomputation needed.
- `2` (results_FINAL.md:1147, count or denominator) Already in Section 2 (balanced panel n=50: Llama 45, Qwen 3, Claude 2, others 0). No further recomputation needed.
- `0` (results_FINAL.md:1147, count or denominator) Already in Section 2 (balanced panel n=50: Llama 45, Qwen 3, Claude 2, others 0). No further recomputation needed.

### [results_FINAL.md] S5. Per-Model Table -- Survival to T5 (GENUINE-only)

*- **Filter (semantic sim):** Word-overlap Jaccard between T1 and each GENUINE turn. Per-trial slope via polyfit.*

- `3.3` (results_FINAL.md:1153, percentage) | llama-3.3-70b | 64/120 (53.3%) |
- `64` (results_FINAL.md:1153, percentage) | llama-3.3-70b | 64/120 (53.3%) |
- `120` (results_FINAL.md:1153, percentage) | llama-3.3-70b | 64/120 (53.3%) |
- `53.3` (results_FINAL.md:1153, percentage) | llama-3.3-70b | 64/120 (53.3%) |
- `4` (results_FINAL.md:1154, percentage) | claude-sonnet-4 | 15/120 (12.5%) |
- `15` (results_FINAL.md:1154, percentage) | claude-sonnet-4 | 15/120 (12.5%) |
- `120` (results_FINAL.md:1154, percentage) | claude-sonnet-4 | 15/120 (12.5%) |
- `12.5` (results_FINAL.md:1154, percentage) | claude-sonnet-4 | 15/120 (12.5%) |
- `7` (results_FINAL.md:1155, percentage) | deepseek-v4 | 7/120 (5.8%) |
- `120` (results_FINAL.md:1155, percentage) | deepseek-v4 | 7/120 (5.8%) |
- `5.8` (results_FINAL.md:1155, percentage) | deepseek-v4 | 7/120 (5.8%) |
- `3` (results_FINAL.md:1156, percentage) | qwen-3-235b | 6/120 (5.0%) |
- `6` (results_FINAL.md:1156, percentage) | qwen-3-235b | 6/120 (5.0%) |
- `120` (results_FINAL.md:1156, percentage) | qwen-3-235b | 6/120 (5.0%) |
- `5.0` (results_FINAL.md:1156, percentage) | qwen-3-235b | 6/120 (5.0%) |
- `3` (results_FINAL.md:1157, percentage) | gpt-4o | 3/120 (2.5%) |
- `120` (results_FINAL.md:1157, percentage) | gpt-4o | 3/120 (2.5%) |
- `2.5` (results_FINAL.md:1157, percentage) | gpt-4o | 3/120 (2.5%) |
- `2.5` (results_FINAL.md:1158, percentage) | gemini-2.5-flash | 1/120 (0.8%) |
- `1` (results_FINAL.md:1158, percentage) | gemini-2.5-flash | 1/120 (0.8%) |
- `120` (results_FINAL.md:1158, percentage) | gemini-2.5-flash | 1/120 (0.8%) |
- `0.8` (results_FINAL.md:1158, percentage) | gemini-2.5-flash | 1/120 (0.8%) |

### [results_FINAL.md] S5. Per-Model Table -- DRP (first turn where GENUINE mean quality < T1, min n>=5)

*- **Filter (semantic sim):** Word-overlap Jaccard between T1 and each GENUINE turn. Per-trial slope via polyfit.*

- `5` (results_FINAL.md:1160, bare number) ### DRP (first turn where GENUINE mean quality < T1, min n>=5)
- `4` (results_FINAL.md:1164, mean or delta) | claude-sonnet-4 | T2 | 4.28 |
- `4.28` (results_FINAL.md:1164, mean or delta) | claude-sonnet-4 | T2 | 4.28 |
- `3.99` (results_FINAL.md:1165, mean or delta) | gpt-4o | T2 | 3.99 |
- `3.3` (results_FINAL.md:1166, mean or delta) | llama-3.3-70b | T2 | 3.75 |
- `3.75` (results_FINAL.md:1166, mean or delta) | llama-3.3-70b | T2 | 3.75 |
- `3` (results_FINAL.md:1167, mean or delta) | qwen-3-235b | T2 | 4.35 |
- `4.35` (results_FINAL.md:1167, mean or delta) | qwen-3-235b | T2 | 4.35 |
- `4.48` (results_FINAL.md:1168, mean or delta) | deepseek-v4 | T3 | 4.48 |
- `2.5` (results_FINAL.md:1169, mean or delta) | gemini-2.5-flash | -- (n<5 at all post-T1 turns) | 3.82 |
- `5` (results_FINAL.md:1169, mean or delta) | gemini-2.5-flash | -- (n<5 at all post-T1 turns) | 3.82 |
- `3.82` (results_FINAL.md:1169, mean or delta) | gemini-2.5-flash | -- (n<5 at all post-T1 turns) | 3.82 |
- `6` (results_FINAL.md:1171, bare number) - **Filter:** Mean quality per turn restricted to GENUINE responses, 6->2 recode. DRP = first turn with mean < T1 mean AND n >= 5.
- `2` (results_FINAL.md:1171, bare number) - **Filter:** Mean quality per turn restricted to GENUINE responses, 6->2 recode. DRP = first turn with mean < T1 mean AND n >= 5.
- `5` (results_FINAL.md:1171, bare number) - **Filter:** Mean quality per turn restricted to GENUINE responses, 6->2 recode. DRP = first turn with mean < T1 mean AND n >= 5.

### [results_FINAL.md] S6. LOCF Analysis (GENUINE carry-forward)

*- **Filter:** Mean quality per turn restricted to GENUINE responses, 6->2 recode. DRP = first turn with mean < T1 mean AND n >= 5.*

- `4.27` (results_FINAL.md:1177, mean or delta) | LOCF T1 | ~4.27 | **4.11** |
- `4.11` (results_FINAL.md:1177, mean or delta) | LOCF T1 | ~4.27 | **4.11** |
- `2.95` (results_FINAL.md:1178, mean or delta) | LOCF T5 | ~2.95 | **3.60** |
- `3.60` (results_FINAL.md:1178, mean or delta) | LOCF T5 | ~2.95 | **3.60** |
- `1.32` (results_FINAL.md:1179, p-value) | LOCF delta | -1.32 | **-0.51** (p=1.0e-32) |
- `0.51` (results_FINAL.md:1179, p-value) | LOCF delta | -1.32 | **-0.51** (p=1.0e-32) |
- `1` (results_FINAL.md:1179, p-value) | LOCF delta | -1.32 | **-0.51** (p=1.0e-32) |
- `32` (results_FINAL.md:1179, p-value) | LOCF delta | -1.32 | **-0.51** (p=1.0e-32) |
- `0.30` (results_FINAL.md:1180, p-value) | LOCF delta (stripped) | -- | **-0.30** (p=3.8e-18) |
- `3` (results_FINAL.md:1180, p-value) | LOCF delta (stripped) | -- | **-0.30** (p=3.8e-18) |
- `18` (results_FINAL.md:1180, p-value) | LOCF delta (stripped) | -- | **-0.30** (p=3.8e-18) |
- `3.60` (results_FINAL.md:1182, percentage) - **Stripped sensitivity:** LOCF T5 rises from 3.60 to 3.81 after stripping (meta was penalizing quality). Delta shrinks 41% but remains highly significant. See Stripped Sensitivity Analysis M3.
- `3.81` (results_FINAL.md:1182, percentage) - **Stripped sensitivity:** LOCF T5 rises from 3.60 to 3.81 after stripping (meta was penalizing quality). Delta shrinks 41% but remains highly significant. See Stripped Sensitivity Analysis M3.
- `41` (results_FINAL.md:1182, percentage) - **Stripped sensitivity:** LOCF T5 rises from 3.60 to 3.81 after stripping (meta was penalizing quality). Delta shrinks 41% but remains highly significant. See Stripped Sensitivity Analysis M3.
- `720` (results_FINAL.md:1183, reliability or effect size) - **Filter:** For each trial, carry forward the last GENUINE-turn quality score. If a turn is META, its LOCF score = the previous GENUINE score. All 720 trials, Wilcoxon on paired T1-vs-T5.

### [results_FINAL.md] S7. Enterprise Projection (Interp A pricing)

*- **Filter:** For each trial, carry forward the last GENUINE-turn quality score. If a turn is META, its LOCF score = the previous GENUINE score. All 720 trials, Wilcoxon on paired T1-vs-T5.*

- `500` (results_FINAL.md:1187, bare number) | Model | $/task waste | Monthly (500-person org) | Annual |
- `2.5` (results_FINAL.md:1189, mean or delta) | gemini-2.5-flash | $0.0001 | $27 | $323 |
- `0.0001` (results_FINAL.md:1189, mean or delta) | gemini-2.5-flash | $0.0001 | $27 | $323 |
- `27` (results_FINAL.md:1189, mean or delta) | gemini-2.5-flash | $0.0001 | $27 | $323 |
- `323` (results_FINAL.md:1189, mean or delta) | gemini-2.5-flash | $0.0001 | $27 | $323 |
- `0.0005` (results_FINAL.md:1190, mean or delta) | deepseek-v4 | $0.0005 | $164 | $1,969 |
- `164` (results_FINAL.md:1190, mean or delta) | deepseek-v4 | $0.0005 | $164 | $1,969 |
- `1,969` (results_FINAL.md:1190, mean or delta) | deepseek-v4 | $0.0005 | $164 | $1,969 |
- `3` (results_FINAL.md:1191, mean or delta) | qwen-3-235b | $0.0009 | $271 | $3,250 |
- `0.0009` (results_FINAL.md:1191, mean or delta) | qwen-3-235b | $0.0009 | $271 | $3,250 |
- `271` (results_FINAL.md:1191, mean or delta) | qwen-3-235b | $0.0009 | $271 | $3,250 |
- `3,250` (results_FINAL.md:1191, mean or delta) | qwen-3-235b | $0.0009 | $271 | $3,250 |
- `3.3` (results_FINAL.md:1192, mean or delta) | llama-3.3-70b | $0.0013 | $390 | $4,680 |
- `0.0013` (results_FINAL.md:1192, mean or delta) | llama-3.3-70b | $0.0013 | $390 | $4,680 |
- `390` (results_FINAL.md:1192, mean or delta) | llama-3.3-70b | $0.0013 | $390 | $4,680 |
- `4,680` (results_FINAL.md:1192, mean or delta) | llama-3.3-70b | $0.0013 | $390 | $4,680 |
- `0.0053` (results_FINAL.md:1193, mean or delta) | gpt-4o | $0.0053 | $1,581 | $18,972 |
- `1,581` (results_FINAL.md:1193, mean or delta) | gpt-4o | $0.0053 | $1,581 | $18,972 |
- `18,972` (results_FINAL.md:1193, mean or delta) | gpt-4o | $0.0053 | $1,581 | $18,972 |
- `4` (results_FINAL.md:1194, mean or delta) | claude-sonnet-4 | $0.0182 | $5,473 | $65,678 |
- `0.0182` (results_FINAL.md:1194, mean or delta) | claude-sonnet-4 | $0.0182 | $5,473 | $65,678 |
- `5,473` (results_FINAL.md:1194, mean or delta) | claude-sonnet-4 | $0.0182 | $5,473 | $65,678 |
- `65,678` (results_FINAL.md:1194, mean or delta) | claude-sonnet-4 | $0.0182 | $5,473 | $65,678 |
- `500` (results_FINAL.md:1196, bare number) - **Assumptions:** 500 employees, 30 tasks/employee/day, 20 workdays/month. 2025 API output-token pricing. Interp A (meta tokens count as waste).
- `30` (results_FINAL.md:1196, bare number) - **Assumptions:** 500 employees, 30 tasks/employee/day, 20 workdays/month. 2025 API output-token pricing. Interp A (meta tokens count as waste).
- `20` (results_FINAL.md:1196, bare number) - **Assumptions:** 500 employees, 30 tasks/employee/day, 20 workdays/month. 2025 API output-token pricing. Interp A (meta tokens count as waste).
- `2025` (results_FINAL.md:1196, bare number) - **Assumptions:** 500 employees, 30 tasks/employee/day, 20 workdays/month. 2025 API output-token pricing. Interp A (meta tokens count as waste).
- `2025` (results_FINAL.md:1198, bare number) - **FLAG:** Dollar figures are pricing-tier-dominated and based on 2025 rates. Range is $323-$65,678/year depending entirely on which model.
- `323` (results_FINAL.md:1198, bare number) - **FLAG:** Dollar figures are pricing-tier-dominated and based on 2025 rates. Range is $323-$65,678/year depending entirely on which model.
- `65,678` (results_FINAL.md:1198, bare number) - **FLAG:** Dollar figures are pricing-tier-dominated and based on 2025 rates. Range is $323-$65,678/year depending entirely on which model.

### [results_FINAL.md] S8. T1 Sufficiency Rate Discrepancy -- RESOLVED

*- **Filter:** For each trial, carry forward the last GENUINE-turn quality score. If a turn is META, its LOCF score = the previous GENUINE score. All 720 trials, Wilcoxon on paired T1-vs-T5.*

- `93.3` (results_FINAL.md:1204, percentage) | Paper draft (93.3%) | 672/720 | Raw scale: level >= 4 includes level 6 as "sufficient" |
- `672` (results_FINAL.md:1204, percentage) | Paper draft (93.3%) | 672/720 | Raw scale: level >= 4 includes level 6 as "sufficient" |
- `720` (results_FINAL.md:1204, percentage) | Paper draft (93.3%) | 672/720 | Raw scale: level >= 4 includes level 6 as "sufficient" |
- `4` (results_FINAL.md:1204, percentage) | Paper draft (93.3%) | 672/720 | Raw scale: level >= 4 includes level 6 as "sufficient" |
- `6` (results_FINAL.md:1204, percentage) | Paper draft (93.3%) | 672/720 | Raw scale: level >= 4 includes level 6 as "sufficient" |
- `87.6` (results_FINAL.md:1205, percentage) | Corrected (87.6%) | 631/720 | 6->2 recode: level 6 becomes 2 (below threshold) |
- `631` (results_FINAL.md:1205, percentage) | Corrected (87.6%) | 631/720 | 6->2 recode: level 6 becomes 2 (below threshold) |
- `720` (results_FINAL.md:1205, percentage) | Corrected (87.6%) | 631/720 | 6->2 recode: level 6 becomes 2 (below threshold) |
- `6` (results_FINAL.md:1205, percentage) | Corrected (87.6%) | 631/720 | 6->2 recode: level 6 becomes 2 (below threshold) |
- `2` (results_FINAL.md:1205, percentage) | Corrected (87.6%) | 631/720 | 6->2 recode: level 6 becomes 2 (below threshold) |
- `6` (results_FINAL.md:1205, percentage) | Corrected (87.6%) | 631/720 | 6->2 recode: level 6 becomes 2 (below threshold) |
- `2` (results_FINAL.md:1205, percentage) | Corrected (87.6%) | 631/720 | 6->2 recode: level 6 becomes 2 (below threshold) |
- `41` (results_FINAL.md:1206, bare number) | Difference | 41 trials | Had T1 level=6 ("Overdone"), recoded to 2 |
- `6` (results_FINAL.md:1206, bare number) | Difference | 41 trials | Had T1 level=6 ("Overdone"), recoded to 2 |
- `2` (results_FINAL.md:1206, bare number) | Difference | 41 trials | Had T1 level=6 ("Overdone"), recoded to 2 |
- `87.6` (results_FINAL.md:1208, percentage) **Use 87.6%** (consistent with all other corrected numbers using 6->2 recode).
- `6` (results_FINAL.md:1208, percentage) **Use 87.6%** (consistent with all other corrected numbers using 6->2 recode).
- `2` (results_FINAL.md:1208, percentage) **Use 87.6%** (consistent with all other corrected numbers using 6->2 recode).

### [results_FINAL.md] S9. Pooled Revision-Only Trajectory (GENUINE-only)

*- **Filter:** For each trial, carry forward the last GENUINE-turn quality score. If a turn is META, its LOCF score = the previous GENUINE score. All 720 trials, Wilcoxon on paired T1-vs-T5.*

- `4.34` (results_FINAL.md:1214, mean or delta) | T1 | 4.34 | **4.11** | 720 |
- `4.11` (results_FINAL.md:1214, mean or delta) | T1 | 4.34 | **4.11** | 720 |
- `720` (results_FINAL.md:1214, mean or delta) | T1 | 4.34 | **4.11** | 720 |
- `3.40` (results_FINAL.md:1215, mean or delta) | T2 | ~3.40 | **3.25** | 283 |
- `3.25` (results_FINAL.md:1215, mean or delta) | T2 | ~3.40 | **3.25** | 283 |
- `283` (results_FINAL.md:1215, mean or delta) | T2 | ~3.40 | **3.25** | 283 |
- `2.90` (results_FINAL.md:1216, mean or delta) | T3 | ~2.90 | **3.01** | 185 |
- `3.01` (results_FINAL.md:1216, mean or delta) | T3 | ~2.90 | **3.01** | 185 |
- `185` (results_FINAL.md:1216, mean or delta) | T3 | ~2.90 | **3.01** | 185 |
- `2.70` (results_FINAL.md:1217, mean or delta) | T4 | ~2.70 | **2.97** | 154 |
- `2.97` (results_FINAL.md:1217, mean or delta) | T4 | ~2.70 | **2.97** | 154 |
- `154` (results_FINAL.md:1217, mean or delta) | T4 | ~2.70 | **2.97** | 154 |
- `2.45` (results_FINAL.md:1218, mean or delta) | T5 | 2.45 | **2.85** | 96 |
- `2.85` (results_FINAL.md:1218, mean or delta) | T5 | 2.45 | **2.85** | 96 |
- `96` (results_FINAL.md:1218, mean or delta) | T5 | 2.45 | **2.85** | 96 |
- `1.89` (results_FINAL.md:1220, mean or delta) Delta T1->T5: OLD -1.89, NEW **-1.26** (unstripped), **-1.04** (stripped).
- `1.26` (results_FINAL.md:1220, mean or delta) Delta T1->T5: OLD -1.89, NEW **-1.26** (unstripped), **-1.04** (stripped).
- `1.04` (results_FINAL.md:1220, mean or delta) Delta T1->T5: OLD -1.89, NEW **-1.26** (unstripped), **-1.04** (stripped).
- `2.85` (results_FINAL.md:1222, percentage) - **Stripped sensitivity:** Stripping removes meta that penalizes quality (triggers "Overdone"). T5 rises from 2.85 to 3.07. Trajectory is 17% shallower but still monotonically declining. See Stripped
- `3.07` (results_FINAL.md:1222, percentage) - **Stripped sensitivity:** Stripping removes meta that penalizes quality (triggers "Overdone"). T5 rises from 2.85 to 3.07. Trajectory is 17% shallower but still monotonically declining. See Stripped
- `17` (results_FINAL.md:1222, percentage) - **Stripped sensitivity:** Stripping removes meta that penalizes quality (triggers "Overdone"). T5 rises from 2.85 to 3.07. Trajectory is 17% shallower but still monotonically declining. See Stripped
- `720` (results_FINAL.md:1223, bare number) - **Filter:** Mean quality per turn, T1 = all 720, T2-T5 = GENUINE-only. 6->2 recode.
- `6` (results_FINAL.md:1223, bare number) - **Filter:** Mean quality per turn, T1 = all 720, T2-T5 = GENUINE-only. 6->2 recode.
- `2` (results_FINAL.md:1223, bare number) - **Filter:** Mean quality per turn, T1 = all 720, T2-T5 = GENUINE-only. 6->2 recode.

### [results_FINAL.md] S10. Domain-Level Variation (GENUINE-only)

*- **Filter:** Mean quality per turn, T1 = all 720, T2-T5 = GENUINE-only. 6->2 recode.*

- `3.98` (results_FINAL.md:1229, mean or delta) | analysis | 3.98 | 2.76 | -1.21 | 17 |
- `2.76` (results_FINAL.md:1229, mean or delta) | analysis | 3.98 | 2.76 | -1.21 | 17 |
- `1.21` (results_FINAL.md:1229, mean or delta) | analysis | 3.98 | 2.76 | -1.21 | 17 |
- `17` (results_FINAL.md:1229, mean or delta) | analysis | 3.98 | 2.76 | -1.21 | 17 |
- `3.95` (results_FINAL.md:1230, mean or delta) | code | 3.95 | 2.80 | -1.15 | 30 |
- `2.80` (results_FINAL.md:1230, mean or delta) | code | 3.95 | 2.80 | -1.15 | 30 |
- `1.15` (results_FINAL.md:1230, mean or delta) | code | 3.95 | 2.80 | -1.15 | 30 |
- `30` (results_FINAL.md:1230, mean or delta) | code | 3.95 | 2.80 | -1.15 | 30 |
- `4.12` (results_FINAL.md:1231, mean or delta) | creative | 4.12 | 2.89 | -1.22 | 19 |
- `2.89` (results_FINAL.md:1231, mean or delta) | creative | 4.12 | 2.89 | -1.22 | 19 |
- `1.22` (results_FINAL.md:1231, mean or delta) | creative | 4.12 | 2.89 | -1.22 | 19 |
- `19` (results_FINAL.md:1231, mean or delta) | creative | 4.12 | 2.89 | -1.22 | 19 |
- `4.35` (results_FINAL.md:1232, mean or delta) | data_logic | 4.35 | 3.00 | -1.35 | 17 |
- `3.00` (results_FINAL.md:1232, mean or delta) | data_logic | 4.35 | 3.00 | -1.35 | 17 |
- `1.35` (results_FINAL.md:1232, mean or delta) | data_logic | 4.35 | 3.00 | -1.35 | 17 |
- `17` (results_FINAL.md:1232, mean or delta) | data_logic | 4.35 | 3.00 | -1.35 | 17 |
- `4.16` (results_FINAL.md:1233, mean or delta) | writing | 4.16 | 2.85 | -1.31 | 13 |
- `2.85` (results_FINAL.md:1233, mean or delta) | writing | 4.16 | 2.85 | -1.31 | 13 |
- `1.31` (results_FINAL.md:1233, mean or delta) | writing | 4.16 | 2.85 | -1.31 | 13 |
- `13` (results_FINAL.md:1233, mean or delta) | writing | 4.16 | 2.85 | -1.31 | 13 |
- `1.35` (results_FINAL.md:1235, mean or delta) All domains degrade. Data_logic has steepest cliff (-1.35 unstripped, -1.01 stripped), code has shallowest (-1.15 unstripped, -1.05 stripped). All T5 n are small (13-30). See Stripped Sensitivity Anal
- `1.01` (results_FINAL.md:1235, mean or delta) All domains degrade. Data_logic has steepest cliff (-1.35 unstripped, -1.01 stripped), code has shallowest (-1.15 unstripped, -1.05 stripped). All T5 n are small (13-30). See Stripped Sensitivity Anal
- `1.15` (results_FINAL.md:1235, mean or delta) All domains degrade. Data_logic has steepest cliff (-1.35 unstripped, -1.01 stripped), code has shallowest (-1.15 unstripped, -1.05 stripped). All T5 n are small (13-30). See Stripped Sensitivity Anal
- `1.05` (results_FINAL.md:1235, mean or delta) All domains degrade. Data_logic has steepest cliff (-1.35 unstripped, -1.01 stripped), code has shallowest (-1.15 unstripped, -1.05 stripped). All T5 n are small (13-30). See Stripped Sensitivity Anal
- `13` (results_FINAL.md:1235, mean or delta) All domains degrade. Data_logic has steepest cliff (-1.35 unstripped, -1.01 stripped), code has shallowest (-1.15 unstripped, -1.05 stripped). All T5 n are small (13-30). See Stripped Sensitivity Anal
- `30` (results_FINAL.md:1235, mean or delta) All domains degrade. Data_logic has steepest cliff (-1.35 unstripped, -1.01 stripped), code has shallowest (-1.15 unstripped, -1.05 stripped). All T5 n are small (13-30). See Stripped Sensitivity Anal
- `144` (results_FINAL.md:1237, bare number) - **Filter:** GENUINE-only quality per domain. T1 = all 144 per domain. T5 = GENUINE at T5 only.

### [results_FINAL.md] S11. Level 6 "Overdone" Rate (GENUINE-only)

*- **Filter:** GENUINE-only quality per domain. T1 = all 144 per domain. T5 = GENUINE at T5 only.*

- `6` (results_FINAL.md:1239, bare number) ## S11. Level 6 "Overdone" Rate (GENUINE-only)
- `3.1` (results_FINAL.md:1243, percentage) | T1 | 3.1% (22/720) | **5.7%** (41/720) |
- `22` (results_FINAL.md:1243, percentage) | T1 | 3.1% (22/720) | **5.7%** (41/720) |
- `720` (results_FINAL.md:1243, percentage) | T1 | 3.1% (22/720) | **5.7%** (41/720) |
- `5.7` (results_FINAL.md:1243, percentage) | T1 | 3.1% (22/720) | **5.7%** (41/720) |
- `41` (results_FINAL.md:1243, percentage) | T1 | 3.1% (22/720) | **5.7%** (41/720) |
- `720` (results_FINAL.md:1243, percentage) | T1 | 3.1% (22/720) | **5.7%** (41/720) |
- `14.9` (results_FINAL.md:1244, percentage) | T2 | 14.9% | **33.9%** (96/283) |
- `33.9` (results_FINAL.md:1244, percentage) | T2 | 14.9% | **33.9%** (96/283) |
- `96` (results_FINAL.md:1244, percentage) | T2 | 14.9% | **33.9%** (96/283) |
- `283` (results_FINAL.md:1244, percentage) | T2 | 14.9% | **33.9%** (96/283) |
- `42.2` (results_FINAL.md:1245, percentage) | T3 | -- | **42.2%** (78/185) |
- `78` (results_FINAL.md:1245, percentage) | T3 | -- | **42.2%** (78/185) |
- `185` (results_FINAL.md:1245, percentage) | T3 | -- | **42.2%** (78/185) |
- `42.9` (results_FINAL.md:1246, percentage) | T4 | -- | **42.9%** (66/154) |
- `66` (results_FINAL.md:1246, percentage) | T4 | -- | **42.9%** (66/154) |
- `154` (results_FINAL.md:1246, percentage) | T4 | -- | **42.9%** (66/154) |
- `47.9` (results_FINAL.md:1247, percentage) | T5 | -- | **47.9%** (46/96) |
- `46` (results_FINAL.md:1247, percentage) | T5 | -- | **47.9%** (46/96) |
- `96` (results_FINAL.md:1247, percentage) | T5 | -- | **47.9%** (46/96) |
- `6` (results_FINAL.md:1249, percentage) **Level 6 rate rises sharply in genuine revisions.** The old low rates were diluted by meta-responses (which never score 6). On stripped text, T5 rate drops from 47.9% to **34.4%** -- confirming meta-
- `6` (results_FINAL.md:1249, percentage) **Level 6 rate rises sharply in genuine revisions.** The old low rates were diluted by meta-responses (which never score 6). On stripped text, T5 rate drops from 47.9% to **34.4%** -- confirming meta-
- `47.9` (results_FINAL.md:1249, percentage) **Level 6 rate rises sharply in genuine revisions.** The old low rates were diluted by meta-responses (which never score 6). On stripped text, T5 rate drops from 47.9% to **34.4%** -- confirming meta-
- `34.4` (results_FINAL.md:1249, percentage) **Level 6 rate rises sharply in genuine revisions.** The old low rates were diluted by meta-responses (which never score 6). On stripped text, T5 rate drops from 47.9% to **34.4%** -- confirming meta-
- `6` (results_FINAL.md:1251, bare number) - **Filter:** Count of evaluator level == 6 (pre-recode) per turn, denominator = GENUINE responses at that turn.
- `3.1` (results_FINAL.md:1252, percentage) - Note: T1 old value (3.1% = 22/720) vs new (5.7% = 41/720) discrepancy may be due to different T1 counting in the old analysis.
- `22` (results_FINAL.md:1252, percentage) - Note: T1 old value (3.1% = 22/720) vs new (5.7% = 41/720) discrepancy may be due to different T1 counting in the old analysis.
- `720` (results_FINAL.md:1252, percentage) - Note: T1 old value (3.1% = 22/720) vs new (5.7% = 41/720) discrepancy may be due to different T1 counting in the old analysis.
- `5.7` (results_FINAL.md:1252, percentage) - Note: T1 old value (3.1% = 22/720) vs new (5.7% = 41/720) discrepancy may be due to different T1 counting in the old analysis.
- `41` (results_FINAL.md:1252, percentage) - Note: T1 old value (3.1% = 22/720) vs new (5.7% = 41/720) discrepancy may be due to different T1 counting in the old analysis.
- `720` (results_FINAL.md:1252, percentage) - Note: T1 old value (3.1% = 22/720) vs new (5.7% = 41/720) discrepancy may be due to different T1 counting in the old analysis.

### [results_FINAL.md] S12. Old Reversibility Sub-Analyses -- SUPERSEDED

*- **Filter:** Count of evaluator level == 6 (pre-recode) per turn, denominator = GENUINE responses at that turn.*

- `7` (results_FINAL.md:1256, bare number) Replaced entirely by human annotation (Section 7) and stratified results (Section 9). Delete from paper.
- `9` (results_FINAL.md:1256, bare number) Replaced entirely by human annotation (Section 7) and stratified results (Section 9). Delete from paper.

### [results_FINAL.md] S13. Momentum Connection -- NARRATIVE ONLY

*- **Filter:** Count of evaluator level == 6 (pre-recode) per turn, denominator = GENUINE responses at that turn.*

- `2` (results_FINAL.md:1260, percentage) Study 2 numbers (1,728 trials, GPT-4o 98% momentum) are unchanged (different dataset). Framing adjustment: revision-despite-sufficiency is 39.2% (not 64.3%), so the "every turn is a momentum turn" cla
- `1,728` (results_FINAL.md:1260, percentage) Study 2 numbers (1,728 trials, GPT-4o 98% momentum) are unchanged (different dataset). Framing adjustment: revision-despite-sufficiency is 39.2% (not 64.3%), so the "every turn is a momentum turn" cla
- `98` (results_FINAL.md:1260, percentage) Study 2 numbers (1,728 trials, GPT-4o 98% momentum) are unchanged (different dataset). Framing adjustment: revision-despite-sufficiency is 39.2% (not 64.3%), so the "every turn is a momentum turn" cla
- `39.2` (results_FINAL.md:1260, percentage) Study 2 numbers (1,728 trials, GPT-4o 98% momentum) are unchanged (different dataset). Framing adjustment: revision-despite-sufficiency is 39.2% (not 64.3%), so the "every turn is a momentum turn" cla
- `64.3` (results_FINAL.md:1260, percentage) Study 2 numbers (1,728 trials, GPT-4o 98% momentum) are unchanged (different dataset). Framing adjustment: revision-despite-sufficiency is 39.2% (not 64.3%), so the "every turn is a momentum turn" cla

### [results_FINAL.md] S14. Targeted Feedback Per-Model (GENUINE-only)

*- **Filter:** Count of evaluator level == 6 (pre-recode) per turn, denominator = GENUINE responses at that turn.*

- `4` (results_FINAL.md:1266, mean or delta) | claude-sonnet-4 | 51 | +0.51 | 0.004 | Yes |
- `51` (results_FINAL.md:1266, mean or delta) | claude-sonnet-4 | 51 | +0.51 | 0.004 | Yes |
- `0.51` (results_FINAL.md:1266, mean or delta) | claude-sonnet-4 | 51 | +0.51 | 0.004 | Yes |
- `0.004` (results_FINAL.md:1266, mean or delta) | claude-sonnet-4 | 51 | +0.51 | 0.004 | Yes |
- `19` (results_FINAL.md:1267, mean or delta) | deepseek-v4 | 19 | +1.58 | 0.005 | Yes |
- `1.58` (results_FINAL.md:1267, mean or delta) | deepseek-v4 | 19 | +1.58 | 0.005 | Yes |
- `0.005` (results_FINAL.md:1267, mean or delta) | deepseek-v4 | 19 | +1.58 | 0.005 | Yes |
- `2.5` (results_FINAL.md:1268, mean or delta) | gemini-2.5-flash | 3 | +1.00 | -- (n<5) | Underpowered |
- `3` (results_FINAL.md:1268, mean or delta) | gemini-2.5-flash | 3 | +1.00 | -- (n<5) | Underpowered |
- `1.00` (results_FINAL.md:1268, mean or delta) | gemini-2.5-flash | 3 | +1.00 | -- (n<5) | Underpowered |
- `5` (results_FINAL.md:1268, mean or delta) | gemini-2.5-flash | 3 | +1.00 | -- (n<5) | Underpowered |
- `12` (results_FINAL.md:1269, mean or delta) | gpt-4o | 12 | -0.17 | 0.750 | No |
- `0.17` (results_FINAL.md:1269, mean or delta) | gpt-4o | 12 | -0.17 | 0.750 | No |
- `0.750` (results_FINAL.md:1269, mean or delta) | gpt-4o | 12 | -0.17 | 0.750 | No |
- `3.3` (results_FINAL.md:1270, mean or delta) | llama-3.3-70b | 71 | -0.17 | 0.027 | Marginal (wrong direction) |
- `71` (results_FINAL.md:1270, mean or delta) | llama-3.3-70b | 71 | -0.17 | 0.027 | Marginal (wrong direction) |
- `0.17` (results_FINAL.md:1270, mean or delta) | llama-3.3-70b | 71 | -0.17 | 0.027 | Marginal (wrong direction) |
- `0.027` (results_FINAL.md:1270, mean or delta) | llama-3.3-70b | 71 | -0.17 | 0.027 | Marginal (wrong direction) |
- `3` (results_FINAL.md:1271, mean or delta) | qwen-3-235b | 21 | +0.00 | 1.000 | No |
- `21` (results_FINAL.md:1271, mean or delta) | qwen-3-235b | 21 | +0.00 | 1.000 | No |
- `0.00` (results_FINAL.md:1271, mean or delta) | qwen-3-235b | 21 | +0.00 | 1.000 | No |
- `1.000` (results_FINAL.md:1271, mean or delta) | qwen-3-235b | 21 | +0.00 | 1.000 | No |
- `0.31` (results_FINAL.md:1273, mean or delta) **SUPERSEDED by stripped analysis.** The unstripped per-model story ("only Claude and DeepSeek benefit") was an artifact of meta-commentary inflating the generic baseline for models with verbose meta-
- `1.62` (results_FINAL.md:1273, mean or delta) **SUPERSEDED by stripped analysis.** The unstripped per-model story ("only Claude and DeepSeek benefit") was an artifact of meta-commentary inflating the generic baseline for models with verbose meta-
- `5` (results_FINAL.md:1275, bare number) - **Filter:** Same as Section 5 (next-turn GENUINE filter, 6->2 recode). Grouped by model.
- `6` (results_FINAL.md:1275, bare number) - **Filter:** Same as Section 5 (next-turn GENUINE filter, 6->2 recode). Grouped by model.
- `2` (results_FINAL.md:1275, bare number) - **Filter:** Same as Section 5 (next-turn GENUINE filter, 6->2 recode). Grouped by model.
- `96` (results_FINAL.md:1276, percentage) - **Supersedes:** Both the old "96-99%" claim AND the intermediate "only 2/6 benefit" finding.
- `99` (results_FINAL.md:1276, percentage) - **Supersedes:** Both the old "96-99%" claim AND the intermediate "only 2/6 benefit" finding.
- `2` (results_FINAL.md:1276, percentage) - **Supersedes:** Both the old "96-99%" claim AND the intermediate "only 2/6 benefit" finding.
- `6` (results_FINAL.md:1276, percentage) - **Supersedes:** Both the old "96-99%" claim AND the intermediate "only 2/6 benefit" finding.

### [results_FINAL.md] S15. Sophie v2 Reliability -- RESOLVED

*- **Filter:** Same as Section 5 (next-turn GENUINE filter, 6->2 recode). Grouped by model.*

- `11` (results_FINAL.md:1280, count or denominator) Already fixed in Section 11. Sophie v2 has 64/64 valid ratings. Three-rater QW kappas: 0.406, 0.578, 0.603. Alpha = 0.529.
- `64` (results_FINAL.md:1280, count or denominator) Already fixed in Section 11. Sophie v2 has 64/64 valid ratings. Three-rater QW kappas: 0.406, 0.578, 0.603. Alpha = 0.529.
- `64` (results_FINAL.md:1280, count or denominator) Already fixed in Section 11. Sophie v2 has 64/64 valid ratings. Three-rater QW kappas: 0.406, 0.578, 0.603. Alpha = 0.529.
- `0.406` (results_FINAL.md:1280, count or denominator) Already fixed in Section 11. Sophie v2 has 64/64 valid ratings. Three-rater QW kappas: 0.406, 0.578, 0.603. Alpha = 0.529.
- `0.578` (results_FINAL.md:1280, count or denominator) Already fixed in Section 11. Sophie v2 has 64/64 valid ratings. Three-rater QW kappas: 0.406, 0.578, 0.603. Alpha = 0.529.
- `0.603` (results_FINAL.md:1280, count or denominator) Already fixed in Section 11. Sophie v2 has 64/64 valid ratings. Three-rater QW kappas: 0.406, 0.578, 0.603. Alpha = 0.529.
- `0.529` (results_FINAL.md:1280, count or denominator) Already fixed in Section 11. Sophie v2 has 64/64 valid ratings. Three-rater QW kappas: 0.406, 0.578, 0.603. Alpha = 0.529.
- `8` (results_FINAL.md:1284, bare number) # STRIPPED SENSITIVITY ANALYSIS (Audit Item 8)
- `3,600` (results_FINAL.md:1286, bare number) All 3,600 outputs (720 trials x 5 turns) were regex-stripped of meta-commentary preambles/postambles
- `720` (results_FINAL.md:1286, bare number) All 3,600 outputs (720 trials x 5 turns) were regex-stripped of meta-commentary preambles/postambles
- `5` (results_FINAL.md:1286, bare number) All 3,600 outputs (720 trials x 5 turns) were regex-stripped of meta-commentary preambles/postambles
- `1,200` (results_FINAL.md:1287, bare number) (same validated patterns as the reversibility pairs) and the 1,200 that changed were rescored by
- `4` (results_FINAL.md:1288, bare number) Claude Sonnet 4 at temperature 0 using the identical EVAL_PROMPT. Scores 6->2 recoded.
- `0` (results_FINAL.md:1288, bare number) Claude Sonnet 4 at temperature 0 using the identical EVAL_PROMPT. Scores 6->2 recoded.
- `6` (results_FINAL.md:1288, bare number) Claude Sonnet 4 at temperature 0 using the identical EVAL_PROMPT. Scores 6->2 recoded.
- `2` (results_FINAL.md:1288, bare number) Claude Sonnet 4 at temperature 0 using the identical EVAL_PROMPT. Scores 6->2 recoded.
- `6` (results_FINAL.md:1290, bare number) **Key finding: meta-commentary PENALIZES quality scores** (triggers "Overdone" = level 6), so

### [results_FINAL.md] Stripping Scope

*- **Filter:** Same as Section 5 (next-turn GENUINE filter, 6->2 recode). Grouped by model.*

- `69` (results_FINAL.md:1299, percentage) | T1 | 69/720 | 9.6% |
- `720` (results_FINAL.md:1299, percentage) | T1 | 69/720 | 9.6% |
- `9.6` (results_FINAL.md:1299, percentage) | T1 | 69/720 | 9.6% |
- `361` (results_FINAL.md:1300, percentage) | T2 | 361/720 | 50.1% |
- `720` (results_FINAL.md:1300, percentage) | T2 | 361/720 | 50.1% |
- `50.1` (results_FINAL.md:1300, percentage) | T2 | 361/720 | 50.1% |
- `282` (results_FINAL.md:1301, percentage) | T3 | 282/720 | 39.2% |
- `720` (results_FINAL.md:1301, percentage) | T3 | 282/720 | 39.2% |
- `39.2` (results_FINAL.md:1301, percentage) | T3 | 282/720 | 39.2% |
- `278` (results_FINAL.md:1302, percentage) | T4 | 278/720 | 38.6% |
- `720` (results_FINAL.md:1302, percentage) | T4 | 278/720 | 38.6% |
- `38.6` (results_FINAL.md:1302, percentage) | T4 | 278/720 | 38.6% |
- `210` (results_FINAL.md:1303, percentage) | T5 | 210/720 | 29.2% |
- `720` (results_FINAL.md:1303, percentage) | T5 | 210/720 | 29.2% |
- `29.2` (results_FINAL.md:1303, percentage) | T5 | 210/720 | 29.2% |
- `1,200` (results_FINAL.md:1304, percentage) | **Total** | **1,200/3,600** | **33.3%** |
- `3,600` (results_FINAL.md:1304, percentage) | **Total** | **1,200/3,600** | **33.3%** |
- `33.3` (results_FINAL.md:1304, percentage) | **Total** | **1,200/3,600** | **33.3%** |
- `3,600` (results_FINAL.md:1306, bare number) Source: `data/study3/raw_responses/stripped_rescore_full.jsonl` (3,600 records, one per trial x turn)

### [results_FINAL.md] Metric-by-Metric Comparison -- M1. Revision-Despite-Sufficiency

*- **Filter:** Same as Section 5 (next-turn GENUINE filter, 6->2 recode). Grouped by model.*

- `4` (results_FINAL.md:1314, bare number) | Sufficient turns (level >= 4) | 938 | 1,038 | +100 |
- `938` (results_FINAL.md:1314, bare number) | Sufficient turns (level >= 4) | 938 | 1,038 | +100 |
- `1,038` (results_FINAL.md:1314, bare number) | Sufficient turns (level >= 4) | 938 | 1,038 | +100 |
- `100` (results_FINAL.md:1314, bare number) | Sufficient turns (level >= 4) | 938 | 1,038 | +100 |
- `368` (results_FINAL.md:1315, bare number) | Revised despite sufficient | 368 | 411 | +43 |
- `411` (results_FINAL.md:1315, bare number) | Revised despite sufficient | 368 | 411 | +43 |
- `43` (results_FINAL.md:1315, bare number) | Revised despite sufficient | 368 | 411 | +43 |
- `39.2` (results_FINAL.md:1316, percentage) | **Rate** | **39.2%** | **39.6%** | **+0.4pp** |
- `39.6` (results_FINAL.md:1316, percentage) | **Rate** | **39.2%** | **39.6%** | **+0.4pp** |
- `0` (results_FINAL.md:1316, percentage) | **Rate** | **39.2%** | **39.6%** | **+0.4pp** |
- `4` (results_FINAL.md:1318, bare number) **Verdict: HOLDS.** Denominator grows because stripping removes meta that was pushing some scores below 4.

### [results_FINAL.md] Metric-by-Metric Comparison -- M2. Targeted Feedback

*- **Filter:** Same as Section 5 (next-turn GENUINE filter, 6->2 recode). Grouped by model.*

- `4.68` (results_FINAL.md:1325, mean or delta) | Both unstripped | 4.68 | 4.43 | **+0.25** | 3.75e-03 | 177 |
- `4.43` (results_FINAL.md:1325, mean or delta) | Both unstripped | 4.68 | 4.43 | **+0.25** | 3.75e-03 | 177 |
- `0.25` (results_FINAL.md:1325, mean or delta) | Both unstripped | 4.68 | 4.43 | **+0.25** | 3.75e-03 | 177 |
- `3` (results_FINAL.md:1325, mean or delta) | Both unstripped | 4.68 | 4.43 | **+0.25** | 3.75e-03 | 177 |
- `03` (results_FINAL.md:1325, mean or delta) | Both unstripped | 4.68 | 4.43 | **+0.25** | 3.75e-03 | 177 |
- `177` (results_FINAL.md:1325, mean or delta) | Both unstripped | 4.68 | 4.43 | **+0.25** | 3.75e-03 | 177 |
- `4.68` (results_FINAL.md:1326, mean or delta) | Both stripped | 4.68 | 3.53 | **+1.16** | 5.74e-19 | 177 |
- `3.53` (results_FINAL.md:1326, mean or delta) | Both stripped | 4.68 | 3.53 | **+1.16** | 5.74e-19 | 177 |
- `1.16` (results_FINAL.md:1326, mean or delta) | Both stripped | 4.68 | 3.53 | **+1.16** | 5.74e-19 | 177 |
- `5` (results_FINAL.md:1326, mean or delta) | Both stripped | 4.68 | 3.53 | **+1.16** | 5.74e-19 | 177 |
- `19` (results_FINAL.md:1326, mean or delta) | Both stripped | 4.68 | 3.53 | **+1.16** | 5.74e-19 | 177 |
- `177` (results_FINAL.md:1326, mean or delta) | Both stripped | 4.68 | 3.53 | **+1.16** | 5.74e-19 | 177 |
- `9` (results_FINAL.md:1328, percentage) Targeted revisions have almost no meta-commentary (9/177 = 5% had any to strip; targeted mean barely
- `177` (results_FINAL.md:1328, percentage) Targeted revisions have almost no meta-commentary (9/177 = 5% had any to strip; targeted mean barely
- `5` (results_FINAL.md:1328, percentage) Targeted revisions have almost no meta-commentary (9/177 = 5% had any to strip; targeted mean barely
- `4.68` (results_FINAL.md:1329, mean or delta) changed: 4.68 -> 4.63). Generic revisions have substantial meta-commentary that was INFLATING their
- `4.63` (results_FINAL.md:1329, mean or delta) changed: 4.68 -> 4.63). Generic revisions have substantial meta-commentary that was INFLATING their
- `4.43` (results_FINAL.md:1330, mean or delta) scores (4.43 -> 3.53 stripped). The real advantage of targeted feedback is +1.16 levels, not +0.25.
- `3.53` (results_FINAL.md:1330, mean or delta) scores (4.43 -> 3.53 stripped). The real advantage of targeted feedback is +1.16 levels, not +0.25.
- `1.16` (results_FINAL.md:1330, mean or delta) scores (4.43 -> 3.53 stripped). The real advantage of targeted feedback is +1.16 levels, not +0.25.
- `0.25` (results_FINAL.md:1330, mean or delta) scores (4.43 -> 3.53 stripped). The real advantage of targeted feedback is +1.16 levels, not +0.25.
- `4` (results_FINAL.md:1336, mean or delta) | claude-sonnet-4 | 51 | +0.31 | 0.012 |
- `51` (results_FINAL.md:1336, mean or delta) | claude-sonnet-4 | 51 | +0.31 | 0.012 |
- `0.31` (results_FINAL.md:1336, mean or delta) | claude-sonnet-4 | 51 | +0.31 | 0.012 |
- `0.012` (results_FINAL.md:1336, mean or delta) | claude-sonnet-4 | 51 | +0.31 | 0.012 |
- `19` (results_FINAL.md:1337, mean or delta) | deepseek-v4 | 19 | +1.05 | 0.012 |
- `1.05` (results_FINAL.md:1337, mean or delta) | deepseek-v4 | 19 | +1.05 | 0.012 |
- `0.012` (results_FINAL.md:1337, mean or delta) | deepseek-v4 | 19 | +1.05 | 0.012 |
- `2.5` (results_FINAL.md:1338, mean or delta) | gemini-2.5-flash | 3 | +2.33 | -- (n<5) |
- `3` (results_FINAL.md:1338, mean or delta) | gemini-2.5-flash | 3 | +2.33 | -- (n<5) |
- `2.33` (results_FINAL.md:1338, mean or delta) | gemini-2.5-flash | 3 | +2.33 | -- (n<5) |
- `5` (results_FINAL.md:1338, mean or delta) | gemini-2.5-flash | 3 | +2.33 | -- (n<5) |
- `12` (results_FINAL.md:1339, mean or delta) | gpt-4o | 12 | +1.33 | 0.008 |
- `1.33` (results_FINAL.md:1339, mean or delta) | gpt-4o | 12 | +1.33 | 0.008 |
- `0.008` (results_FINAL.md:1339, mean or delta) | gpt-4o | 12 | +1.33 | 0.008 |
- `3.3` (results_FINAL.md:1340, mean or delta) | llama-3.3-70b | 71 | +1.62 | 9.2e-12 |
- `71` (results_FINAL.md:1340, mean or delta) | llama-3.3-70b | 71 | +1.62 | 9.2e-12 |
- `1.62` (results_FINAL.md:1340, mean or delta) | llama-3.3-70b | 71 | +1.62 | 9.2e-12 |
- `9` (results_FINAL.md:1340, mean or delta) | llama-3.3-70b | 71 | +1.62 | 9.2e-12 |
- `12` (results_FINAL.md:1340, mean or delta) | llama-3.3-70b | 71 | +1.62 | 9.2e-12 |
- `3` (results_FINAL.md:1341, mean or delta) | qwen-3-235b | 21 | +1.48 | 4.5e-04 |
- `21` (results_FINAL.md:1341, mean or delta) | qwen-3-235b | 21 | +1.48 | 4.5e-04 |
- `1.48` (results_FINAL.md:1341, mean or delta) | qwen-3-235b | 21 | +1.48 | 4.5e-04 |
- `4` (results_FINAL.md:1341, mean or delta) | qwen-3-235b | 21 | +1.48 | 4.5e-04 |
- `04` (results_FINAL.md:1341, mean or delta) | qwen-3-235b | 21 | +1.48 | 4.5e-04 |

### [results_FINAL.md] Metric-by-Metric Comparison -- M3. LOCF Analysis

*- **Filter:** Same as Section 5 (next-turn GENUINE filter, 6->2 recode). Grouped by model.*

- `4.11` (results_FINAL.md:1351, mean or delta) | LOCF T1 | 4.11 | 4.11 | 0 |
- `4.11` (results_FINAL.md:1351, mean or delta) | LOCF T1 | 4.11 | 4.11 | 0 |
- `0` (results_FINAL.md:1351, mean or delta) | LOCF T1 | 4.11 | 4.11 | 0 |
- `3.60` (results_FINAL.md:1352, mean or delta) | LOCF T5 | 3.60 | 3.81 | +0.21 |
- `3.81` (results_FINAL.md:1352, mean or delta) | LOCF T5 | 3.60 | 3.81 | +0.21 |
- `0.21` (results_FINAL.md:1352, mean or delta) | LOCF T5 | 3.60 | 3.81 | +0.21 |
- `0.51` (results_FINAL.md:1353, percentage) | **Delta** | **-0.51** | **-0.30** | **41% smaller** |
- `0.30` (results_FINAL.md:1353, percentage) | **Delta** | **-0.51** | **-0.30** | **41% smaller** |
- `41` (results_FINAL.md:1353, percentage) | **Delta** | **-0.51** | **-0.30** | **41% smaller** |
- `1` (results_FINAL.md:1354, mean or delta) | p-value | 1.0e-32 | 3.8e-18 | Still significant |
- `32` (results_FINAL.md:1354, mean or delta) | p-value | 1.0e-32 | 3.8e-18 | Still significant |
- `3` (results_FINAL.md:1354, mean or delta) | p-value | 1.0e-32 | 3.8e-18 | Still significant |
- `18` (results_FINAL.md:1354, mean or delta) | p-value | 1.0e-32 | 3.8e-18 | Still significant |
- `0.30` (results_FINAL.md:1357, count or denominator) LOCF degradation is -0.30 levels, not -0.51. Highly significant either way (n=720).
- `0.51` (results_FINAL.md:1357, count or denominator) LOCF degradation is -0.30 levels, not -0.51. Highly significant either way (n=720).
- `720` (results_FINAL.md:1357, count or denominator) LOCF degradation is -0.30 levels, not -0.51. Highly significant either way (n=720).

### [results_FINAL.md] Metric-by-Metric Comparison -- M4. Pooled Revision-Only Trajectory (GENUINE-only)

*- **Filter:** Same as Section 5 (next-turn GENUINE filter, 6->2 recode). Grouped by model.*

- `4.11` (results_FINAL.md:1363, mean or delta) | T1 | 4.11 | 4.11 | 0 | 720 |
- `4.11` (results_FINAL.md:1363, mean or delta) | T1 | 4.11 | 4.11 | 0 | 720 |
- `0` (results_FINAL.md:1363, mean or delta) | T1 | 4.11 | 4.11 | 0 | 720 |
- `720` (results_FINAL.md:1363, mean or delta) | T1 | 4.11 | 4.11 | 0 | 720 |
- `3.25` (results_FINAL.md:1364, mean or delta) | T2 | 3.25 | 3.66 | +0.41 | 283 |
- `3.66` (results_FINAL.md:1364, mean or delta) | T2 | 3.25 | 3.66 | +0.41 | 283 |
- `0.41` (results_FINAL.md:1364, mean or delta) | T2 | 3.25 | 3.66 | +0.41 | 283 |
- `283` (results_FINAL.md:1364, mean or delta) | T2 | 3.25 | 3.66 | +0.41 | 283 |
- `3.01` (results_FINAL.md:1365, mean or delta) | T3 | 3.01 | 3.40 | +0.39 | 185 |
- `3.40` (results_FINAL.md:1365, mean or delta) | T3 | 3.01 | 3.40 | +0.39 | 185 |
- `0.39` (results_FINAL.md:1365, mean or delta) | T3 | 3.01 | 3.40 | +0.39 | 185 |
- `185` (results_FINAL.md:1365, mean or delta) | T3 | 3.01 | 3.40 | +0.39 | 185 |
- `2.97` (results_FINAL.md:1366, mean or delta) | T4 | 2.97 | 3.34 | +0.37 | 154 |
- `3.34` (results_FINAL.md:1366, mean or delta) | T4 | 2.97 | 3.34 | +0.37 | 154 |
- `0.37` (results_FINAL.md:1366, mean or delta) | T4 | 2.97 | 3.34 | +0.37 | 154 |
- `154` (results_FINAL.md:1366, mean or delta) | T4 | 2.97 | 3.34 | +0.37 | 154 |
- `2.85` (results_FINAL.md:1367, mean or delta) | T5 | 2.85 | 3.07 | +0.22 | 96 |
- `3.07` (results_FINAL.md:1367, mean or delta) | T5 | 2.85 | 3.07 | +0.22 | 96 |
- `0.22` (results_FINAL.md:1367, mean or delta) | T5 | 2.85 | 3.07 | +0.22 | 96 |
- `96` (results_FINAL.md:1367, mean or delta) | T5 | 2.85 | 3.07 | +0.22 | 96 |
- `1.26` (results_FINAL.md:1368, percentage) | **Delta T1->T5** | **-1.26** | **-1.04** | **17% smaller** | |
- `1.04` (results_FINAL.md:1368, percentage) | **Delta T1->T5** | **-1.26** | **-1.04** | **17% smaller** | |
- `17` (results_FINAL.md:1368, percentage) | **Delta T1->T5** | **-1.26** | **-1.04** | **17% smaller** | |
- `3.07` (results_FINAL.md:1370, mean or delta) **Verdict: HOLDS.** Quality still degrades monotonically. Stripped T5 (3.07) is still below
- `4.0` (results_FINAL.md:1371, percentage) Sufficient (4.0). But the decline is 17% shallower than unstripped.
- `17` (results_FINAL.md:1371, percentage) Sufficient (4.0). But the decline is 17% shallower than unstripped.

### [results_FINAL.md] Metric-by-Metric Comparison -- M5. Domain-Level Variation (GENUINE-only)

*- **Filter:** Same as Section 5 (next-turn GENUINE filter, 6->2 recode). Grouped by model.*

- `1.21` (results_FINAL.md:1377, mean or delta) | analysis | -1.21 | -1.16 | +0.05 | 17 |
- `1.16` (results_FINAL.md:1377, mean or delta) | analysis | -1.21 | -1.16 | +0.05 | 17 |
- `0.05` (results_FINAL.md:1377, mean or delta) | analysis | -1.21 | -1.16 | +0.05 | 17 |
- `17` (results_FINAL.md:1377, mean or delta) | analysis | -1.21 | -1.16 | +0.05 | 17 |
- `1.15` (results_FINAL.md:1378, mean or delta) | code | -1.15 | -1.05 | +0.10 | 30 |
- `1.05` (results_FINAL.md:1378, mean or delta) | code | -1.15 | -1.05 | +0.10 | 30 |
- `0.10` (results_FINAL.md:1378, mean or delta) | code | -1.15 | -1.05 | +0.10 | 30 |
- `30` (results_FINAL.md:1378, mean or delta) | code | -1.15 | -1.05 | +0.10 | 30 |
- `1.22` (results_FINAL.md:1379, mean or delta) | creative | -1.22 | -0.82 | +0.40 | 19 |
- `0.82` (results_FINAL.md:1379, mean or delta) | creative | -1.22 | -0.82 | +0.40 | 19 |
- `0.40` (results_FINAL.md:1379, mean or delta) | creative | -1.22 | -0.82 | +0.40 | 19 |
- `19` (results_FINAL.md:1379, mean or delta) | creative | -1.22 | -0.82 | +0.40 | 19 |
- `1.35` (results_FINAL.md:1380, mean or delta) | data_logic | -1.35 | -1.01 | +0.34 | 17 |
- `1.01` (results_FINAL.md:1380, mean or delta) | data_logic | -1.35 | -1.01 | +0.34 | 17 |
- `0.34` (results_FINAL.md:1380, mean or delta) | data_logic | -1.35 | -1.01 | +0.34 | 17 |
- `17` (results_FINAL.md:1380, mean or delta) | data_logic | -1.35 | -1.01 | +0.34 | 17 |
- `1.31` (results_FINAL.md:1381, mean or delta) | writing | -1.31 | -1.06 | +0.25 | 13 |
- `1.06` (results_FINAL.md:1381, mean or delta) | writing | -1.31 | -1.06 | +0.25 | 13 |
- `0.25` (results_FINAL.md:1381, mean or delta) | writing | -1.31 | -1.06 | +0.25 | 13 |
- `13` (results_FINAL.md:1381, mean or delta) | writing | -1.31 | -1.06 | +0.25 | 13 |

### [results_FINAL.md] Metric-by-Metric Comparison -- M6. Level-6 "Overdone" Rate (GENUINE-only, pre-recode)

*- **Filter:** Same as Section 5 (next-turn GENUINE filter, 6->2 recode). Grouped by model.*

- `6` (results_FINAL.md:1386, bare number) ### M6. Level-6 "Overdone" Rate (GENUINE-only, pre-recode)
- `5.7` (results_FINAL.md:1390, percentage) | T1 | 5.7% (41/720) | 5.6% (40/720) | -0.1pp |
- `41` (results_FINAL.md:1390, percentage) | T1 | 5.7% (41/720) | 5.6% (40/720) | -0.1pp |
- `720` (results_FINAL.md:1390, percentage) | T1 | 5.7% (41/720) | 5.6% (40/720) | -0.1pp |
- `5.6` (results_FINAL.md:1390, percentage) | T1 | 5.7% (41/720) | 5.6% (40/720) | -0.1pp |
- `40` (results_FINAL.md:1390, percentage) | T1 | 5.7% (41/720) | 5.6% (40/720) | -0.1pp |
- `720` (results_FINAL.md:1390, percentage) | T1 | 5.7% (41/720) | 5.6% (40/720) | -0.1pp |
- `0` (results_FINAL.md:1390, percentage) | T1 | 5.7% (41/720) | 5.6% (40/720) | -0.1pp |
- `33.9` (results_FINAL.md:1391, percentage) | T2 | 33.9% (96/283) | 18.0% (51/283) | **-15.9pp** |
- `96` (results_FINAL.md:1391, percentage) | T2 | 33.9% (96/283) | 18.0% (51/283) | **-15.9pp** |
- `283` (results_FINAL.md:1391, percentage) | T2 | 33.9% (96/283) | 18.0% (51/283) | **-15.9pp** |
- `18.0` (results_FINAL.md:1391, percentage) | T2 | 33.9% (96/283) | 18.0% (51/283) | **-15.9pp** |
- `51` (results_FINAL.md:1391, percentage) | T2 | 33.9% (96/283) | 18.0% (51/283) | **-15.9pp** |
- `283` (results_FINAL.md:1391, percentage) | T2 | 33.9% (96/283) | 18.0% (51/283) | **-15.9pp** |
- `15` (results_FINAL.md:1391, percentage) | T2 | 33.9% (96/283) | 18.0% (51/283) | **-15.9pp** |
- `42.2` (results_FINAL.md:1392, percentage) | T3 | 42.2% (78/185) | 28.6% (53/185) | **-13.5pp** |
- `78` (results_FINAL.md:1392, percentage) | T3 | 42.2% (78/185) | 28.6% (53/185) | **-13.5pp** |
- `185` (results_FINAL.md:1392, percentage) | T3 | 42.2% (78/185) | 28.6% (53/185) | **-13.5pp** |
- `28.6` (results_FINAL.md:1392, percentage) | T3 | 42.2% (78/185) | 28.6% (53/185) | **-13.5pp** |
- `53` (results_FINAL.md:1392, percentage) | T3 | 42.2% (78/185) | 28.6% (53/185) | **-13.5pp** |
- `185` (results_FINAL.md:1392, percentage) | T3 | 42.2% (78/185) | 28.6% (53/185) | **-13.5pp** |
- `13` (results_FINAL.md:1392, percentage) | T3 | 42.2% (78/185) | 28.6% (53/185) | **-13.5pp** |
- `42.9` (results_FINAL.md:1393, percentage) | T4 | 42.9% (66/154) | 27.9% (43/154) | **-15.0pp** |
- `66` (results_FINAL.md:1393, percentage) | T4 | 42.9% (66/154) | 27.9% (43/154) | **-15.0pp** |
- `154` (results_FINAL.md:1393, percentage) | T4 | 42.9% (66/154) | 27.9% (43/154) | **-15.0pp** |
- `27.9` (results_FINAL.md:1393, percentage) | T4 | 42.9% (66/154) | 27.9% (43/154) | **-15.0pp** |
- `43` (results_FINAL.md:1393, percentage) | T4 | 42.9% (66/154) | 27.9% (43/154) | **-15.0pp** |
- `154` (results_FINAL.md:1393, percentage) | T4 | 42.9% (66/154) | 27.9% (43/154) | **-15.0pp** |
- `15` (results_FINAL.md:1393, percentage) | T4 | 42.9% (66/154) | 27.9% (43/154) | **-15.0pp** |
- `47.9` (results_FINAL.md:1394, percentage) | T5 | 47.9% (46/96) | 34.4% (33/96) | **-13.5pp** |
- `46` (results_FINAL.md:1394, percentage) | T5 | 47.9% (46/96) | 34.4% (33/96) | **-13.5pp** |
- `96` (results_FINAL.md:1394, percentage) | T5 | 47.9% (46/96) | 34.4% (33/96) | **-13.5pp** |
- `34.4` (results_FINAL.md:1394, percentage) | T5 | 47.9% (46/96) | 34.4% (33/96) | **-13.5pp** |
- `33` (results_FINAL.md:1394, percentage) | T5 | 47.9% (46/96) | 34.4% (33/96) | **-13.5pp** |
- `96` (results_FINAL.md:1394, percentage) | T5 | 47.9% (46/96) | 34.4% (33/96) | **-13.5pp** |
- `13` (results_FINAL.md:1394, percentage) | T5 | 47.9% (46/96) | 34.4% (33/96) | **-13.5pp** |
- `6` (results_FINAL.md:1396, bare number) **Verdict: CONFIRMS meta preambles trigger "Overdone."** Level-6 rates drop 13-16pp after stripping.
- `13` (results_FINAL.md:1396, bare number) **Verdict: CONFIRMS meta preambles trigger "Overdone."** Level-6 rates drop 13-16pp after stripping.
- `34.4` (results_FINAL.md:1398, percentage) "unrequested complexity." Even stripped, 34.4% of genuine T5 revisions are still Overdone -- this is

### [results_FINAL.md] Metric-by-Metric Comparison -- Balanced Panel Cliff (reference, already in Section 2)

*- **Filter:** Same as Section 5 (next-turn GENUINE filter, 6->2 recode). Grouped by model.*

- `2` (results_FINAL.md:1401, bare number) ### Balanced Panel Cliff (reference, already in Section 2)
- `3.66` (results_FINAL.md:1405, mean or delta) | T1 | 3.66 | 3.66 | 0 |
- `3.66` (results_FINAL.md:1405, mean or delta) | T1 | 3.66 | 3.66 | 0 |
- `0` (results_FINAL.md:1405, mean or delta) | T1 | 3.66 | 3.66 | 0 |
- `2.72` (results_FINAL.md:1406, mean or delta) | T5 | 2.72 | 2.92 | +0.20 |
- `2.92` (results_FINAL.md:1406, mean or delta) | T5 | 2.72 | 2.92 | +0.20 |
- `0.20` (results_FINAL.md:1406, mean or delta) | T5 | 2.72 | 2.92 | +0.20 |
- `0.94` (results_FINAL.md:1407, percentage) | **Delta** | **-0.94** | **-0.74** | **21% smaller** |
- `0.74` (results_FINAL.md:1407, percentage) | **Delta** | **-0.94** | **-0.74** | **21% smaller** |
- `21` (results_FINAL.md:1407, percentage) | **Delta** | **-0.94** | **-0.74** | **21% smaller** |
- `50` (results_FINAL.md:1409, percentage) Consistent with the earlier 50-pair rescore (19-21% inflation range).
- `19` (results_FINAL.md:1409, percentage) Consistent with the earlier 50-pair rescore (19-21% inflation range).
- `21` (results_FINAL.md:1409, percentage) Consistent with the earlier 50-pair rescore (19-21% inflation range).

### [results_FINAL.md] Summary: What Moves, What Holds

*- **Filter:** Same as Section 5 (next-turn GENUINE filter, 6->2 recode). Grouped by model.*

- `1` (results_FINAL.md:1415, percentage) | 1 | Rev-despite-suff | 39.2% | 39.6% | No | Same |
- `39.2` (results_FINAL.md:1415, percentage) | 1 | Rev-despite-suff | 39.2% | 39.6% | No | Same |
- `39.6` (results_FINAL.md:1415, percentage) | 1 | Rev-despite-suff | 39.2% | 39.6% | No | Same |
- `2` (results_FINAL.md:1416, mean or delta) | 2 | Targeted feedback | +0.25 | +1.16 | **YES** | Same, much stronger |
- `0.25` (results_FINAL.md:1416, mean or delta) | 2 | Targeted feedback | +0.25 | +1.16 | **YES** | Same, much stronger |
- `1.16` (results_FINAL.md:1416, mean or delta) | 2 | Targeted feedback | +0.25 | +1.16 | **YES** | Same, much stronger |
- `2` (results_FINAL.md:1417, count or denominator) | 2b | Targeted per-model | 2/6 benefit | **All benefit** | **YES** | Reverses |
- `6` (results_FINAL.md:1417, count or denominator) | 2b | Targeted per-model | 2/6 benefit | **All benefit** | **YES** | Reverses |
- `3` (results_FINAL.md:1418, mean or delta) | 3 | LOCF delta | -0.51 | -0.30 | Moderate | Same, attenuated |
- `0.51` (results_FINAL.md:1418, mean or delta) | 3 | LOCF delta | -0.51 | -0.30 | Moderate | Same, attenuated |
- `0.30` (results_FINAL.md:1418, mean or delta) | 3 | LOCF delta | -0.51 | -0.30 | Moderate | Same, attenuated |
- `4` (results_FINAL.md:1419, mean or delta) | 4 | Pooled trajectory delta | -1.26 | -1.04 | Moderate | Same, attenuated |
- `1.26` (results_FINAL.md:1419, mean or delta) | 4 | Pooled trajectory delta | -1.26 | -1.04 | Moderate | Same, attenuated |
- `1.04` (results_FINAL.md:1419, mean or delta) | 4 | Pooled trajectory delta | -1.26 | -1.04 | Moderate | Same, attenuated |
- `5` (results_FINAL.md:1420, mean or delta) | 5 | Domain deltas | -1.15 to -1.35 | -0.82 to -1.16 | Moderate | Same, attenuated |
- `1.15` (results_FINAL.md:1420, mean or delta) | 5 | Domain deltas | -1.15 to -1.35 | -0.82 to -1.16 | Moderate | Same, attenuated |
- `1.35` (results_FINAL.md:1420, mean or delta) | 5 | Domain deltas | -1.15 to -1.35 | -0.82 to -1.16 | Moderate | Same, attenuated |
- `0.82` (results_FINAL.md:1420, mean or delta) | 5 | Domain deltas | -1.15 to -1.35 | -0.82 to -1.16 | Moderate | Same, attenuated |
- `1.16` (results_FINAL.md:1420, mean or delta) | 5 | Domain deltas | -1.15 to -1.35 | -0.82 to -1.16 | Moderate | Same, attenuated |
- `6` (results_FINAL.md:1421, percentage) | 6 | Level-6 at T5 | 47.9% | 34.4% | **YES** | Same, lower |
- `6` (results_FINAL.md:1421, percentage) | 6 | Level-6 at T5 | 47.9% | 34.4% | **YES** | Same, lower |
- `47.9` (results_FINAL.md:1421, percentage) | 6 | Level-6 at T5 | 47.9% | 34.4% | **YES** | Same, lower |
- `34.4` (results_FINAL.md:1421, percentage) | 6 | Level-6 at T5 | 47.9% | 34.4% | **YES** | Same, lower |
- `0.94` (results_FINAL.md:1422, percentage) | -- | Balanced cliff | -0.94 | -0.74 | Moderate | Same (21% smaller) |
- `0.74` (results_FINAL.md:1422, percentage) | -- | Balanced cliff | -0.94 | -0.74 | Moderate | Same (21% smaller) |
- `21` (results_FINAL.md:1422, percentage) | -- | Balanced cliff | -0.94 | -0.74 | Moderate | Same (21% smaller) |
- `1` (results_FINAL.md:1425, mean or delta) 1. Targeted feedback delta quintuples (+0.25 -> +1.16) and becomes universal across models
- `0.25` (results_FINAL.md:1425, mean or delta) 1. Targeted feedback delta quintuples (+0.25 -> +1.16) and becomes universal across models
- `1.16` (results_FINAL.md:1425, mean or delta) 1. Targeted feedback delta quintuples (+0.25 -> +1.16) and becomes universal across models
- `2` (results_FINAL.md:1426, bare number) 2. Level-6 rate drops ~14pp (meta-commentary was triggering "Overdone")
- `6` (results_FINAL.md:1426, bare number) 2. Level-6 rate drops ~14pp (meta-commentary was triggering "Overdone")
- `3` (results_FINAL.md:1427, mean or delta) 3. LOCF delta nearly halves (-0.51 -> -0.30)
- `0.51` (results_FINAL.md:1427, mean or delta) 3. LOCF delta nearly halves (-0.51 -> -0.30)
- `0.30` (results_FINAL.md:1427, mean or delta) 3. LOCF delta nearly halves (-0.51 -> -0.30)
- `3847` (results_FINAL.md:1435, bare number) - Server running on port 3847 (PID 96795) -- can be killed when no longer needed
- `96795` (results_FINAL.md:1435, bare number) - Server running on port 3847 (PID 96795) -- can be killed when no longer needed

### [results_FINAL.md] 15. The ten hand-corrected classifier labels: scope and sensitivity

*- **Filter:** Same as Section 5 (next-turn GENUINE filter, 6->2 recode). Grouped by model.*

- `15` (results_FINAL.md:1440, bare number) ## 15. The ten hand-corrected classifier labels: scope and sensitivity
- `2026` (results_FINAL.md:1442, bare number) Checked 2026-09-20 after an audit found the ten `[CORRECTED]` records in
- `09` (results_FINAL.md:1442, bare number) Checked 2026-09-20 after an audit found the ten `[CORRECTED]` records in
- `20` (results_FINAL.md:1442, bare number) Checked 2026-09-20 after an audit found the ten `[CORRECTED]` records in
- `0.00` (results_FINAL.md:1450, mean or delta) none of it (sentence containment 0.00 to 0.09); they restate Turn 1 content, not Turn N-1,
- `0.09` (results_FINAL.md:1450, mean or delta) none of it (sentence containment 0.00 to 0.09); they restate Turn 1 content, not Turn N-1,
- `1` (results_FINAL.md:1450, mean or delta) none of it (sentence containment 0.00 to 0.09); they restate Turn 1 content, not Turn N-1,
- `1` (results_FINAL.md:1450, mean or delta) none of it (sentence containment 0.00 to 0.09); they restate Turn 1 content, not Turn N-1,
- `2,880` (results_FINAL.md:1454, bare number) - **Filter:** all 2,880 post-Turn-1 rows in `genuine_meta_labels.jsonl` joined to
- `1` (results_FINAL.md:1454, bare number) - **Filter:** all 2,880 post-Turn-1 rows in `genuine_meta_labels.jsonl` joined to
- `1` (results_FINAL.md:1455, bare number) `worker_trials.jsonl` on `trial_id`, response text taken at `responses[turn-1]`.
- `25` (results_FINAL.md:1456, bare number) Containment is the share of the earlier turn's sentences longer than 25 characters

### [results_FINAL.md] 15. The ten hand-corrected classifier labels: scope and sensitivity -- The ten are not an exhaustive pass

*- **Filter:** all 2,880 post-Turn-1 rows in `genuine_meta_labels.jsonl` joined to*

- `240` (results_FINAL.md:1461, bare number) Applying the discriminator that selects them, an explicit refusal phrase in the first 240
- `25` (results_FINAL.md:1462, bare number) characters, to the rows still labelled GENUINE returns **25 further rows**. Several restate
- `0.91` (results_FINAL.md:1463, mean or delta) more of the earlier turn than any corrected row does (containment up to 0.91 against a
- `0.71` (results_FINAL.md:1464, count or denominator) maximum of 0.71 among the ten). The ten are therefore 10 of at least 35 comparable cases,
- `10` (results_FINAL.md:1464, count or denominator) maximum of 0.71 among the ten). The ten are therefore 10 of at least 35 comparable cases,
- `35` (results_FINAL.md:1464, count or denominator) maximum of 0.71 among the ten). The ten are therefore 10 of at least 35 comparable cases,
- `240` (results_FINAL.md:1468, bare number) - **Filter:** regex on the first 240 characters of the normalised response, matching
- `718` (results_FINAL.md:1470, bare number) "this is my final". 718 GENUINE rows screened, 25 matched.
- `25` (results_FINAL.md:1470, bare number) "this is my final". 718 GENUINE rows screened, 25 matched.

### [results_FINAL.md] 15. The ten hand-corrected classifier labels: scope and sensitivity -- The central result does not depend on them

*- **Filter:** regex on the first 240 characters of the normalised response, matching*

- `25` (results_FINAL.md:1474, bare number) Eight of the 25 sit inside balanced-panel trials, so applying the rule consistently would
- `50` (results_FINAL.md:1475, bare number) take the panel from 50 trials to 42. The cliff is unchanged.
- `42` (results_FINAL.md:1475, bare number) take the panel from 50 trials to 42. The cliff is unchanged.
- `50` (results_FINAL.md:1479, mean or delta) | As published | 50 | 3.66 | 2.92 | **-0.74** | 54.5 | 1.01e-4 | 31 |
- `3.66` (results_FINAL.md:1479, mean or delta) | As published | 50 | 3.66 | 2.92 | **-0.74** | 54.5 | 1.01e-4 | 31 |
- `2.92` (results_FINAL.md:1479, mean or delta) | As published | 50 | 3.66 | 2.92 | **-0.74** | 54.5 | 1.01e-4 | 31 |
- `0.74` (results_FINAL.md:1479, mean or delta) | As published | 50 | 3.66 | 2.92 | **-0.74** | 54.5 | 1.01e-4 | 31 |
- `54.5` (results_FINAL.md:1479, mean or delta) | As published | 50 | 3.66 | 2.92 | **-0.74** | 54.5 | 1.01e-4 | 31 |
- `1` (results_FINAL.md:1479, mean or delta) | As published | 50 | 3.66 | 2.92 | **-0.74** | 54.5 | 1.01e-4 | 31 |
- `4` (results_FINAL.md:1479, mean or delta) | As published | 50 | 3.66 | 2.92 | **-0.74** | 54.5 | 1.01e-4 | 31 |
- `31` (results_FINAL.md:1479, mean or delta) | As published | 50 | 3.66 | 2.92 | **-0.74** | 54.5 | 1.01e-4 | 31 |
- `42` (results_FINAL.md:1480, mean or delta) | Rule applied | 42 | 3.60 | 2.86 | **-0.74** | 51.0 | 3.75e-4 | 28 |
- `3.60` (results_FINAL.md:1480, mean or delta) | Rule applied | 42 | 3.60 | 2.86 | **-0.74** | 51.0 | 3.75e-4 | 28 |
- `2.86` (results_FINAL.md:1480, mean or delta) | Rule applied | 42 | 3.60 | 2.86 | **-0.74** | 51.0 | 3.75e-4 | 28 |
- `0.74` (results_FINAL.md:1480, mean or delta) | Rule applied | 42 | 3.60 | 2.86 | **-0.74** | 51.0 | 3.75e-4 | 28 |
- `51.0` (results_FINAL.md:1480, mean or delta) | Rule applied | 42 | 3.60 | 2.86 | **-0.74** | 51.0 | 3.75e-4 | 28 |
- `3` (results_FINAL.md:1480, mean or delta) | Rule applied | 42 | 3.60 | 2.86 | **-0.74** | 51.0 | 3.75e-4 | 28 |
- `4` (results_FINAL.md:1480, mean or delta) | Rule applied | 42 | 3.60 | 2.86 | **-0.74** | 51.0 | 3.75e-4 | 28 |
- `28` (results_FINAL.md:1480, mean or delta) | Rule applied | 42 | 3.60 | 2.86 | **-0.74** | 51.0 | 3.75e-4 | 28 |
- `45` (results_FINAL.md:1481, mean or delta) | Llama only, as published | 45 | 3.53 | 2.87 | -0.67 | 51.5 | 3.76e-4 | 28 |
- `3.53` (results_FINAL.md:1481, mean or delta) | Llama only, as published | 45 | 3.53 | 2.87 | -0.67 | 51.5 | 3.76e-4 | 28 |
- `2.87` (results_FINAL.md:1481, mean or delta) | Llama only, as published | 45 | 3.53 | 2.87 | -0.67 | 51.5 | 3.76e-4 | 28 |
- `0.67` (results_FINAL.md:1481, mean or delta) | Llama only, as published | 45 | 3.53 | 2.87 | -0.67 | 51.5 | 3.76e-4 | 28 |
- `51.5` (results_FINAL.md:1481, mean or delta) | Llama only, as published | 45 | 3.53 | 2.87 | -0.67 | 51.5 | 3.76e-4 | 28 |
- `3` (results_FINAL.md:1481, mean or delta) | Llama only, as published | 45 | 3.53 | 2.87 | -0.67 | 51.5 | 3.76e-4 | 28 |
- `4` (results_FINAL.md:1481, mean or delta) | Llama only, as published | 45 | 3.53 | 2.87 | -0.67 | 51.5 | 3.76e-4 | 28 |
- `28` (results_FINAL.md:1481, mean or delta) | Llama only, as published | 45 | 3.53 | 2.87 | -0.67 | 51.5 | 3.76e-4 | 28 |
- `38` (results_FINAL.md:1482, mean or delta) | Llama only, rule applied | 38 | 3.47 | 2.76 | -0.71 | 48.0 | 8.45e-4 | 26 |
- `3.47` (results_FINAL.md:1482, mean or delta) | Llama only, rule applied | 38 | 3.47 | 2.76 | -0.71 | 48.0 | 8.45e-4 | 26 |
- `2.76` (results_FINAL.md:1482, mean or delta) | Llama only, rule applied | 38 | 3.47 | 2.76 | -0.71 | 48.0 | 8.45e-4 | 26 |
- `0.71` (results_FINAL.md:1482, mean or delta) | Llama only, rule applied | 38 | 3.47 | 2.76 | -0.71 | 48.0 | 8.45e-4 | 26 |
- `48.0` (results_FINAL.md:1482, mean or delta) | Llama only, rule applied | 38 | 3.47 | 2.76 | -0.71 | 48.0 | 8.45e-4 | 26 |
- `8` (results_FINAL.md:1482, mean or delta) | Llama only, rule applied | 38 | 3.47 | 2.76 | -0.71 | 48.0 | 8.45e-4 | 26 |
- `4` (results_FINAL.md:1482, mean or delta) | Llama only, rule applied | 38 | 3.47 | 2.76 | -0.71 | 48.0 | 8.45e-4 | 26 |
- `26` (results_FINAL.md:1482, mean or delta) | Llama only, rule applied | 38 | 3.47 | 2.76 | -0.71 | 48.0 | 8.45e-4 | 26 |
- `2` (results_FINAL.md:1484, bare number) - **Filter:** balanced panel is GENUINE at all of turns 2-5. Stripped levels at turns 1 and 5
- `5` (results_FINAL.md:1484, bare number) - **Filter:** balanced panel is GENUINE at all of turns 2-5. Stripped levels at turns 1 and 5
- `1` (results_FINAL.md:1484, bare number) - **Filter:** balanced panel is GENUINE at all of turns 2-5. Stripped levels at turns 1 and 5
- `5` (results_FINAL.md:1484, bare number) - **Filter:** balanced panel is GENUINE at all of turns 2-5. Stripped levels at turns 1 and 5
- `6` (results_FINAL.md:1485, bare number) from `stripped_rescore_full.jsonl` field `stripped_score`, 6 -> 2 recode applied first.
- `2` (results_FINAL.md:1485, bare number) from `stripped_rescore_full.jsonl` field `stripped_score`, 6 -> 2 recode applied first.
- `4` (results_FINAL.md:1487, bare number) section 4 exactly, which validates the reconstruction.
- `2026` (results_FINAL.md:1489, bare number) **Decided 2026-09-20: the sample stays as published.** The panel remains 50 trials and the
- `09` (results_FINAL.md:1489, bare number) **Decided 2026-09-20: the sample stays as published.** The panel remains 50 trials and the
- `20` (results_FINAL.md:1489, bare number) **Decided 2026-09-20: the sample stays as published.** The panel remains 50 trials and the
- `50` (results_FINAL.md:1489, bare number) **Decided 2026-09-20: the sample stays as published.** The panel remains 50 trials and the
- `24.9` (results_FINAL.md:1490, percentage) genuine-revision rate remains 24.9% (718/2,880). The alternatives were costed and rejected,
- `718` (results_FINAL.md:1490, percentage) genuine-revision rate remains 24.9% (718/2,880). The alternatives were costed and rejected,
- `2,880` (results_FINAL.md:1490, percentage) genuine-revision rate remains 24.9% (718/2,880). The alternatives were costed and rejected,
- `35` (results_FINAL.md:1491, mean or delta) not overlooked: applying the discriminator to all 35 gives -0.74 on 42 trials (p 3.75e-4),
- `0.74` (results_FINAL.md:1491, mean or delta) not overlooked: applying the discriminator to all 35 gives -0.74 on 42 trials (p 3.75e-4),
- `42` (results_FINAL.md:1491, mean or delta) not overlooked: applying the discriminator to all 35 gives -0.74 on 42 trials (p 3.75e-4),
- `3` (results_FINAL.md:1491, mean or delta) not overlooked: applying the discriminator to all 35 gives -0.74 on 42 trials (p 3.75e-4),
- `4` (results_FINAL.md:1491, mean or delta) not overlooked: applying the discriminator to all 35 gives -0.74 on 42 trials (p 3.75e-4),
- `0.75` (results_FINAL.md:1492, mean or delta) and removing the ten corrections gives -0.75 on 52 trials (p 5.47e-5). No number in the
- `52` (results_FINAL.md:1492, mean or delta) and removing the ten corrections gives -0.75 on 52 trials (p 5.47e-5). No number in the
- `5` (results_FINAL.md:1492, mean or delta) and removing the ten corrections gives -0.75 on 52 trials (p 5.47e-5). No number in the
- `5` (results_FINAL.md:1492, mean or delta) and removing the ten corrections gives -0.75 on 52 trials (p 5.47e-5). No number in the

### [results_FINAL.md] 16. Study 1 probe-type chi-squared on both scopes

*- **Filter:** balanced panel is GENUINE at all of turns 2-5. Stripped levels at turns 1 and 5*

- `16` (results_FINAL.md:1496, bare number) ## 16. Study 1 probe-type chi-squared on both scopes
- `1` (results_FINAL.md:1496, bare number) ## 16. Study 1 probe-type chi-squared on both scopes
- `2026` (results_FINAL.md:1498, bare number) Recorded 2026-09-20. The appendix prints two probe-type chi-squared ranges and they look
- `09` (results_FINAL.md:1498, bare number) Recorded 2026-09-20. The appendix prints two probe-type chi-squared ranges and they look
- `20` (results_FINAL.md:1498, bare number) Recorded 2026-09-20. The appendix prints two probe-type chi-squared ranges and they look
- `788` (results_FINAL.md:1499, bare number) contradictory at a glance, because one minimum (788) is larger than the other (742). They are
- `742` (results_FINAL.md:1499, bare number) contradictory at a glance, because one minimum (788) is larger than the other (742). They are
- `3,932` (results_FINAL.md:1504, p-value) | All five probe types | 3,932 | 914.37 | 1326.89 | 788.96 | "$\chi^2 > 788$, $p < 0.0001$ for all models" |
- `914.37` (results_FINAL.md:1504, p-value) | All five probe types | 3,932 | 914.37 | 1326.89 | 788.96 | "$\chi^2 > 788$, $p < 0.0001$ for all models" |
- `1326.89` (results_FINAL.md:1504, p-value) | All five probe types | 3,932 | 914.37 | 1326.89 | 788.96 | "$\chi^2 > 788$, $p < 0.0001$ for all models" |
- `788.96` (results_FINAL.md:1504, p-value) | All five probe types | 3,932 | 914.37 | 1326.89 | 788.96 | "$\chi^2 > 788$, $p < 0.0001$ for all models" |
- `2` (results_FINAL.md:1504, p-value) | All five probe types | 3,932 | 914.37 | 1326.89 | 788.96 | "$\chi^2 > 788$, $p < 0.0001$ for all models" |
- `788` (results_FINAL.md:1504, p-value) | All five probe types | 3,932 | 914.37 | 1326.89 | 788.96 | "$\chi^2 > 788$, $p < 0.0001$ for all models" |
- `0.0001` (results_FINAL.md:1504, p-value) | All five probe types | 3,932 | 914.37 | 1326.89 | 788.96 | "$\chi^2 > 788$, $p < 0.0001$ for all models" |
- `3,840` (results_FINAL.md:1505, mean or delta) | Factorial scope, leading + evaluative | 3,840 | 857.49 | 1268.10 | 742.18 | "runs from 742 to 1,268" |
- `857.49` (results_FINAL.md:1505, mean or delta) | Factorial scope, leading + evaluative | 3,840 | 857.49 | 1268.10 | 742.18 | "runs from 742 to 1,268" |
- `1268.10` (results_FINAL.md:1505, mean or delta) | Factorial scope, leading + evaluative | 3,840 | 857.49 | 1268.10 | 742.18 | "runs from 742 to 1,268" |
- `742.18` (results_FINAL.md:1505, mean or delta) | Factorial scope, leading + evaluative | 3,840 | 857.49 | 1268.10 | 742.18 | "runs from 742 to 1,268" |
- `742` (results_FINAL.md:1505, mean or delta) | Factorial scope, leading + evaluative | 3,840 | 857.49 | 1268.10 | 742.18 | "runs from 742 to 1,268" |
- `1,268` (results_FINAL.md:1505, mean or delta) | Factorial scope, leading + evaluative | 3,840 | 857.49 | 1268.10 | 742.18 | "runs from 742 to 1,268" |
- `8` (results_FINAL.md:1509, bare number) The factorial scope keeps `probe_type` in {leading, pilot_c}, which is the 8 scenarios x 16
- `16` (results_FINAL.md:1509, bare number) The factorial scope keeps `probe_type` in {leading, pilot_c}, which is the 8 scenarios x 16
- `2` (results_FINAL.md:1510, bare number) threshold conditions x 2 probes x 3 models x 5 runs design; the three small pilot arms
- `3` (results_FINAL.md:1510, bare number) threshold conditions x 2 probes x 3 models x 5 runs design; the three small pilot arms
- `5` (results_FINAL.md:1510, bare number) threshold conditions x 2 probes x 3 models x 5 runs design; the three small pilot arms
- `50` (results_FINAL.md:1511, count or denominator) (neutral n=50, pilot_b n=24, pilot_a n=18) are outside it. All p-values are below 1e-160.
- `24` (results_FINAL.md:1511, count or denominator) (neutral n=50, pilot_b n=24, pilot_a n=18) are outside it. All p-values are below 1e-160.
- `18` (results_FINAL.md:1511, count or denominator) (neutral n=50, pilot_b n=24, pilot_a n=18) are outside it. All p-values are below 1e-160.
- `160` (results_FINAL.md:1511, count or denominator) (neutral n=50, pilot_b n=24, pilot_a n=18) are outside it. All p-values are below 1e-160.

### [results_FINAL.md] 17. Study 1 pairwise threshold comparisons (appendix Table 6)

*- **Filter:** `data/study1/scored_trials.jsonl` as resolved by `scripts/config.SCORED_TRIALS_JSONL`.*

- `17` (results_FINAL.md:1516, bare number) ## 17. Study 1 pairwise threshold comparisons (appendix Table 6)
- `1` (results_FINAL.md:1516, bare number) ## 17. Study 1 pairwise threshold comparisons (appendix Table 6)
- `6` (results_FINAL.md:1516, bare number) ## 17. Study 1 pairwise threshold comparisons (appendix Table 6)
- `2026` (results_FINAL.md:1518, bare number) Recorded 2026-09-20. These six rows were the one outstanding item from the number-ledger
- `09` (results_FINAL.md:1518, bare number) Recorded 2026-09-20. These six rows were the one outstanding item from the number-ledger
- `20` (results_FINAL.md:1518, bare number) Recorded 2026-09-20. These six rows were the one outstanding item from the number-ledger
- `2.5` (results_FINAL.md:1524, mean or delta) | Gemini 2.5 Flash | numeric | 70 vs 100 | 4935 | 4.0e-9 | -0.42 |
- `70` (results_FINAL.md:1524, mean or delta) | Gemini 2.5 Flash | numeric | 70 vs 100 | 4935 | 4.0e-9 | -0.42 |
- `100` (results_FINAL.md:1524, mean or delta) | Gemini 2.5 Flash | numeric | 70 vs 100 | 4935 | 4.0e-9 | -0.42 |
- `4935` (results_FINAL.md:1524, mean or delta) | Gemini 2.5 Flash | numeric | 70 vs 100 | 4935 | 4.0e-9 | -0.42 |
- `4` (results_FINAL.md:1524, mean or delta) | Gemini 2.5 Flash | numeric | 70 vs 100 | 4935 | 4.0e-9 | -0.42 |
- `9` (results_FINAL.md:1524, mean or delta) | Gemini 2.5 Flash | numeric | 70 vs 100 | 4935 | 4.0e-9 | -0.42 |
- `0.42` (results_FINAL.md:1524, mean or delta) | Gemini 2.5 Flash | numeric | 70 vs 100 | 4935 | 4.0e-9 | -0.42 |
- `2.5` (results_FINAL.md:1525, mean or delta) | Gemini 2.5 Flash | numeric | 85 vs 100 | 4238 | 2.0e-5 | -0.32 |
- `85` (results_FINAL.md:1525, mean or delta) | Gemini 2.5 Flash | numeric | 85 vs 100 | 4238 | 2.0e-5 | -0.32 |
- `100` (results_FINAL.md:1525, mean or delta) | Gemini 2.5 Flash | numeric | 85 vs 100 | 4238 | 2.0e-5 | -0.32 |
- `4238` (results_FINAL.md:1525, mean or delta) | Gemini 2.5 Flash | numeric | 85 vs 100 | 4238 | 2.0e-5 | -0.32 |
- `2` (results_FINAL.md:1525, mean or delta) | Gemini 2.5 Flash | numeric | 85 vs 100 | 4238 | 2.0e-5 | -0.32 |
- `5` (results_FINAL.md:1525, mean or delta) | Gemini 2.5 Flash | numeric | 85 vs 100 | 4238 | 2.0e-5 | -0.32 |
- `0.32` (results_FINAL.md:1525, mean or delta) | Gemini 2.5 Flash | numeric | 85 vs 100 | 4238 | 2.0e-5 | -0.32 |
- `2.5` (results_FINAL.md:1526, mean or delta) | Gemini 2.5 Flash | numeric | 0 vs 100 | 4755 | 3.8e-4 | -0.25 |
- `0` (results_FINAL.md:1526, mean or delta) | Gemini 2.5 Flash | numeric | 0 vs 100 | 4755 | 3.8e-4 | -0.25 |
- `100` (results_FINAL.md:1526, mean or delta) | Gemini 2.5 Flash | numeric | 0 vs 100 | 4755 | 3.8e-4 | -0.25 |
- `4755` (results_FINAL.md:1526, mean or delta) | Gemini 2.5 Flash | numeric | 0 vs 100 | 4755 | 3.8e-4 | -0.25 |
- `3` (results_FINAL.md:1526, mean or delta) | Gemini 2.5 Flash | numeric | 0 vs 100 | 4755 | 3.8e-4 | -0.25 |
- `4` (results_FINAL.md:1526, mean or delta) | Gemini 2.5 Flash | numeric | 0 vs 100 | 4755 | 3.8e-4 | -0.25 |
- `0.25` (results_FINAL.md:1526, mean or delta) | Gemini 2.5 Flash | numeric | 0 vs 100 | 4755 | 3.8e-4 | -0.25 |
- `2.5` (results_FINAL.md:1527, mean or delta) | Gemini 2.5 Flash | qualitative | 0 vs 100 | 4084 | 3.9e-4 | -0.28 |
- `0` (results_FINAL.md:1527, mean or delta) | Gemini 2.5 Flash | qualitative | 0 vs 100 | 4084 | 3.9e-4 | -0.28 |
- `100` (results_FINAL.md:1527, mean or delta) | Gemini 2.5 Flash | qualitative | 0 vs 100 | 4084 | 3.9e-4 | -0.28 |
- `4084` (results_FINAL.md:1527, mean or delta) | Gemini 2.5 Flash | qualitative | 0 vs 100 | 4084 | 3.9e-4 | -0.28 |
- `3` (results_FINAL.md:1527, mean or delta) | Gemini 2.5 Flash | qualitative | 0 vs 100 | 4084 | 3.9e-4 | -0.28 |
- `4` (results_FINAL.md:1527, mean or delta) | Gemini 2.5 Flash | qualitative | 0 vs 100 | 4084 | 3.9e-4 | -0.28 |
- `0.28` (results_FINAL.md:1527, mean or delta) | Gemini 2.5 Flash | qualitative | 0 vs 100 | 4084 | 3.9e-4 | -0.28 |
- `4` (results_FINAL.md:1528, mean or delta) | Claude Sonnet 4 | numeric | 85 vs 100 | 4146 | 1.8e-4 | -0.30 |
- `85` (results_FINAL.md:1528, mean or delta) | Claude Sonnet 4 | numeric | 85 vs 100 | 4146 | 1.8e-4 | -0.30 |
- `100` (results_FINAL.md:1528, mean or delta) | Claude Sonnet 4 | numeric | 85 vs 100 | 4146 | 1.8e-4 | -0.30 |
- `4146` (results_FINAL.md:1528, mean or delta) | Claude Sonnet 4 | numeric | 85 vs 100 | 4146 | 1.8e-4 | -0.30 |
- `1` (results_FINAL.md:1528, mean or delta) | Claude Sonnet 4 | numeric | 85 vs 100 | 4146 | 1.8e-4 | -0.30 |
- `4` (results_FINAL.md:1528, mean or delta) | Claude Sonnet 4 | numeric | 85 vs 100 | 4146 | 1.8e-4 | -0.30 |
- `0.30` (results_FINAL.md:1528, mean or delta) | Claude Sonnet 4 | numeric | 85 vs 100 | 4146 | 1.8e-4 | -0.30 |
- `4` (results_FINAL.md:1529, mean or delta) | Claude Sonnet 4 | qualitative | 85 vs 100 | 3880 | 4.8e-3 | -0.21 |
- `85` (results_FINAL.md:1529, mean or delta) | Claude Sonnet 4 | qualitative | 85 vs 100 | 3880 | 4.8e-3 | -0.21 |
- `100` (results_FINAL.md:1529, mean or delta) | Claude Sonnet 4 | qualitative | 85 vs 100 | 3880 | 4.8e-3 | -0.21 |
- `3880` (results_FINAL.md:1529, mean or delta) | Claude Sonnet 4 | qualitative | 85 vs 100 | 3880 | 4.8e-3 | -0.21 |
- `4` (results_FINAL.md:1529, mean or delta) | Claude Sonnet 4 | qualitative | 85 vs 100 | 3880 | 4.8e-3 | -0.21 |
- `3` (results_FINAL.md:1529, mean or delta) | Claude Sonnet 4 | qualitative | 85 vs 100 | 3880 | 4.8e-3 | -0.21 |
- `0.21` (results_FINAL.md:1529, mean or delta) | Claude Sonnet 4 | qualitative | 85 vs 100 | 3880 | 4.8e-3 | -0.21 |
- `4237.5` (results_FINAL.md:1535, mean or delta) (4237.5 and 4083.5). The effect size is the rank-biserial correlation
- `4083.5` (results_FINAL.md:1535, mean or delta) (4237.5 and 4083.5). The effect size is the rank-biserial correlation
- `1` (results_FINAL.md:1536, bare number) `-(2U/(n1*n2) - 1)`, signed so that a higher threshold producing less overcorrection is
- `0` (results_FINAL.md:1540, bare number) 0, 70, 75 and 80 only. The two rows that are scope-sensitive (Gemini numeric 70 vs 100 and
- `70` (results_FINAL.md:1540, bare number) 0, 70, 75 and 80 only. The two rows that are scope-sensitive (Gemini numeric 70 vs 100 and
- `75` (results_FINAL.md:1540, bare number) 0, 70, 75 and 80 only. The two rows that are scope-sensitive (Gemini numeric 70 vs 100 and
- `80` (results_FINAL.md:1540, bare number) 0, 70, 75 and 80 only. The two rows that are scope-sensitive (Gemini numeric 70 vs 100 and
- `70` (results_FINAL.md:1540, bare number) 0, 70, 75 and 80 only. The two rows that are scope-sensitive (Gemini numeric 70 vs 100 and
- `100` (results_FINAL.md:1540, bare number) 0, 70, 75 and 80 only. The two rows that are scope-sensitive (Gemini numeric 70 vs 100 and
- `0` (results_FINAL.md:1541, bare number) 0 vs 100) both use all five probe types, so the table is on one consistent basis. Computing
- `100` (results_FINAL.md:1541, bare number) 0 vs 100) both use all five probe types, so the table is on one consistent basis. Computing
- `4580` (results_FINAL.md:1542, bare number) it on the factorial scope instead would change those two rows to U = 4580 and U = 4188 and
- `4188` (results_FINAL.md:1542, bare number) it on the factorial scope instead would change those two rows to U = 4580 and U = 4188 and

### [results_FINAL.md] 18. Targeted feedback: how far the repair goes, and on what

*- **Filter:** `data/study1/scored_trials.jsonl` as resolved by `scripts.config.SCORED_TRIALS_JSONL`,*

- `18` (results_FINAL.md:1547, bare number) ## 18. Targeted feedback: how far the repair goes, and on what
- `2026` (results_FINAL.md:1549, bare number) Recorded 2026-09-21. These figures were computed in an earlier session and survived only in
- `09` (results_FINAL.md:1549, bare number) Recorded 2026-09-21. These figures were computed in an earlier session and survived only in
- `21` (results_FINAL.md:1549, bare number) Recorded 2026-09-21. These figures were computed in an earlier session and survived only in

### [results_FINAL.md] 18. Targeted feedback: how far the repair goes, and on what -- (a) Where targeted revisions land

*- **Filter:** `data/study1/scored_trials.jsonl` as resolved by `scripts.config.SCORED_TRIALS_JSONL`,*

- `169` (results_FINAL.md:1554, percentage) **169 of 177 targeted revisions reach level 4 or above (95.5%).** The repair does not merely
- `177` (results_FINAL.md:1554, percentage) **169 of 177 targeted revisions reach level 4 or above (95.5%).** The repair does not merely
- `4` (results_FINAL.md:1554, percentage) **169 of 177 targeted revisions reach level 4 or above (95.5%).** The repair does not merely
- `95.5` (results_FINAL.md:1554, percentage) **169 of 177 targeted revisions reach level 4 or above (95.5%).** The repair does not merely
- `177` (results_FINAL.md:1557, bare number) - **Filter:** the same 177 pairs as Section 5. Targeted level recoded 6 -> 2, counted at
- `5` (results_FINAL.md:1557, bare number) - **Filter:** the same 177 pairs as Section 5. Targeted level recoded 6 -> 2, counted at
- `6` (results_FINAL.md:1557, bare number) - **Filter:** the same 177 pairs as Section 5. Targeted level recoded 6 -> 2, counted at
- `2` (results_FINAL.md:1557, bare number) - **Filter:** the same 177 pairs as Section 5. Targeted level recoded 6 -> 2, counted at
- `4` (results_FINAL.md:1558, bare number) `>= 4`.

### [results_FINAL.md] 18. Targeted feedback: how far the repair goes, and on what -- (b) The subset where degradation is visible and the repair reverses it

*- **Filter:** the same 177 pairs as Section 5. Targeted level recoded 6 -> 2, counted at*

- `177` (results_FINAL.md:1562, bare number) Of the 177 pairs, **113 had an input that had degraded from a sufficient Turn 1**: stripped
- `113` (results_FINAL.md:1562, bare number) Of the 177 pairs, **113 had an input that had degraded from a sufficient Turn 1**: stripped
- `1` (results_FINAL.md:1562, bare number) Of the 177 pairs, **113 had an input that had degraded from a sufficient Turn 1**: stripped
- `1` (results_FINAL.md:1563, bare number) Turn 1 at level 4 or above, and the input turn below it. That subset splits sharply:
- `4` (results_FINAL.md:1563, bare number) Turn 1 at level 4 or above, and the input turn below it. That subset splits sharply:
- `13` (results_FINAL.md:1567, mean or delta) | A genuine revision | 13 | 4.15 | 2.69 | **4.77** | 0.000488 |
- `4.15` (results_FINAL.md:1567, mean or delta) | A genuine revision | 13 | 4.15 | 2.69 | **4.77** | 0.000488 |
- `2.69` (results_FINAL.md:1567, mean or delta) | A genuine revision | 13 | 4.15 | 2.69 | **4.77** | 0.000488 |
- `4.77` (results_FINAL.md:1567, mean or delta) | A genuine revision | 13 | 4.15 | 2.69 | **4.77** | 0.000488 |
- `0.000488` (results_FINAL.md:1567, mean or delta) | A genuine revision | 13 | 4.15 | 2.69 | **4.77** | 0.000488 |
- `100` (results_FINAL.md:1568, mean or delta) | A meta-response | 100 | -- | 1.06 | -- | -- |
- `1.06` (results_FINAL.md:1568, mean or delta) | A meta-response | 100 | -- | 1.06 | -- | -- |
- `13` (results_FINAL.md:1570, bare number) The 13-trial row is the cleanest statement of the paper's mechanism: work that was sufficient,
- `100` (results_FINAL.md:1573, bare number) **The 100 meta-response rows are not evidence of repair and must not be reported as though
- `1` (results_FINAL.md:1574, bare number) they were.** A meta-response strips to near-empty text and scores about 1, so "improvement"
- `1.000` (results_FINAL.md:1576, mean or delta) This is the same mechanism that makes the raw stripped delta correlate -1.000 with mean Turn 1
- `1` (results_FINAL.md:1576, mean or delta) This is the same mechanism that makes the raw stripped delta correlate -1.000 with mean Turn 1
- `13` (results_FINAL.md:1577, mean or delta) quality across models (Section 13), and it is why the headline +1.16 is reported on the full
- `1.16` (results_FINAL.md:1577, mean or delta) quality across models (Section 13), and it is why the headline +1.16 is reported on the full
- `177` (results_FINAL.md:1578, bare number) 177 rather than on this subset.
- `1` (results_FINAL.md:1582, turn index) stripped levels at turn 1 and at the input turn. 6 -> 2 recode on both sides. Degraded means
- `6` (results_FINAL.md:1582, turn index) stripped levels at turn 1 and at the input turn. 6 -> 2 recode on both sides. Degraded means
- `2` (results_FINAL.md:1582, turn index) stripped levels at turn 1 and at the input turn. 6 -> 2 recode on both sides. Degraded means
- `4` (results_FINAL.md:1583, reliability or effect size) stripped T1 `>= 4` and stripped input `< 4`. Two-sided Wilcoxon signed-rank on the paired
- `4` (results_FINAL.md:1583, reliability or effect size) stripped T1 `>= 4` and stripped input `< 4`. Two-sided Wilcoxon signed-rank on the paired
- `2026` (results_FINAL.md:1586, bare number) above; every value here was re-derived from the data files on 2026-09-21.
- `09` (results_FINAL.md:1586, bare number) above; every value here was re-derived from the data files on 2026-09-21.
- `21` (results_FINAL.md:1586, bare number) above; every value here was re-derived from the data files on 2026-09-21.

### [results_FINAL.md] 19. The 6 -> 2 recode determines the sign of the central result

*- **Filter:** `targeted_feedback_results.jsonl` joined to `genuine_meta_labels.jsonl` on*

- `19` (results_FINAL.md:1588, bare number) ## 19. The 6 -> 2 recode determines the sign of the central result
- `6` (results_FINAL.md:1588, bare number) ## 19. The 6 -> 2 recode determines the sign of the central result
- `2` (results_FINAL.md:1588, bare number) ## 19. The 6 -> 2 recode determines the sign of the central result
- `2026` (results_FINAL.md:1590, bare number) Found 2026-09-21 during an adversarial read. **This is the most consequential open item in the
- `09` (results_FINAL.md:1590, bare number) Found 2026-09-21 during an adversarial read. **This is the most consequential open item in the
- `21` (results_FINAL.md:1590, bare number) Found 2026-09-21 during an adversarial read. **This is the most consequential open item in the

### [results_FINAL.md] 19. The 6 -> 2 recode determines the sign of the central result -- What was run

*- **Filter:** `targeted_feedback_results.jsonl` joined to `genuine_meta_labels.jsonl` on*

- `6` (results_FINAL.md:1595, bare number) Four codings of level 6 ("Overdone"), on the published balanced panel and the published pooled
- `6` (results_FINAL.md:1598, count or denominator) | Coding of level 6 | Panel delta (n=50) | p | Pooled delta |
- `50` (results_FINAL.md:1598, count or denominator) | Coding of level 6 | Panel delta (n=50) | p | Pooled delta |
- `2` (results_FINAL.md:1600, mean or delta) | **-> 2, as published** | **-0.740** | 1.01e-4 | **-1.04** |
- `0.740` (results_FINAL.md:1600, mean or delta) | **-> 2, as published** | **-0.740** | 1.01e-4 | **-1.04** |
- `1` (results_FINAL.md:1600, mean or delta) | **-> 2, as published** | **-0.740** | 1.01e-4 | **-1.04** |
- `4` (results_FINAL.md:1600, mean or delta) | **-> 2, as published** | **-0.740** | 1.01e-4 | **-1.04** |
- `1.04` (results_FINAL.md:1600, mean or delta) | **-> 2, as published** | **-0.740** | 1.01e-4 | **-1.04** |
- `6` (results_FINAL.md:1601, mean or delta) | left as 6 | **+0.700** | 2.79e-3 | +0.11 |
- `0.700` (results_FINAL.md:1601, mean or delta) | left as 6 | **+0.700** | 2.79e-3 | +0.11 |
- `2` (results_FINAL.md:1601, mean or delta) | left as 6 | **+0.700** | 2.79e-3 | +0.11 |
- `3` (results_FINAL.md:1601, mean or delta) | left as 6 | **+0.700** | 2.79e-3 | +0.11 |
- `0.11` (results_FINAL.md:1601, mean or delta) | left as 6 | **+0.700** | 2.79e-3 | +0.11 |
- `4` (results_FINAL.md:1602, mean or delta) | -> 4 (merely sufficient) | -0.020 | 0.796 | -0.46 |
- `0.020` (results_FINAL.md:1602, mean or delta) | -> 4 (merely sufficient) | -0.020 | 0.796 | -0.46 |
- `0.796` (results_FINAL.md:1602, mean or delta) | -> 4 (merely sufficient) | -0.020 | 0.796 | -0.46 |
- `0.46` (results_FINAL.md:1602, mean or delta) | -> 4 (merely sufficient) | -0.020 | 0.796 | -0.46 |
- `5` (results_FINAL.md:1603, mean or delta) | -> 5 (above sufficient) | +0.340 | 4.94e-2 | +0.34 |
- `0.340` (results_FINAL.md:1603, mean or delta) | -> 5 (above sufficient) | +0.340 | 4.94e-2 | +0.34 |
- `4` (results_FINAL.md:1603, mean or delta) | -> 5 (above sufficient) | +0.340 | 4.94e-2 | +0.34 |
- `2` (results_FINAL.md:1603, mean or delta) | -> 5 (above sufficient) | +0.340 | 4.94e-2 | +0.34 |
- `0.34` (results_FINAL.md:1603, mean or delta) | -> 5 (above sufficient) | +0.340 | 4.94e-2 | +0.34 |
- `6` (results_FINAL.md:1605, bare number) **The headline finding reverses sign and stays significant when level 6 is left alone.** The
- `6` (results_FINAL.md:1611, bare number) applied, which is why it contains no level 6). Balanced panel is GENUINE at turns 2-5.
- `2` (results_FINAL.md:1611, bare number) applied, which is why it contains no level 6). Balanced panel is GENUINE at turns 2-5.
- `5` (results_FINAL.md:1611, bare number) applied, which is why it contains no level 6). Balanced panel is GENUINE at turns 2-5.
- `1` (results_FINAL.md:1612, reliability or effect size) Two-sided Wilcoxon signed-rank on paired turn-1 and turn-5 values.
- `5` (results_FINAL.md:1612, reliability or effect size) Two-sided Wilcoxon signed-rank on paired turn-1 and turn-5 values.

### [results_FINAL.md] 19. The 6 -> 2 recode determines the sign of the central result -- Why it moves the result

*- **Filter:** `stripped_rescore_full.jsonl`, field `stripped_level_raw` for the un-recoded*

- `6` (results_FINAL.md:1616, bare number) Within the panel, the share of outputs scored level 6 rises monotonically across turns:
- `4` (results_FINAL.md:1620, percentage) | scored "Overdone" | 4% | 20% | 26% | 28% | 40% |
- `20` (results_FINAL.md:1620, percentage) | scored "Overdone" | 4% | 20% | 26% | 28% | 40% |
- `26` (results_FINAL.md:1620, percentage) | scored "Overdone" | 4% | 20% | 26% | 28% | 40% |
- `28` (results_FINAL.md:1620, percentage) | scored "Overdone" | 4% | 20% | 26% | 28% | 40% |
- `40` (results_FINAL.md:1620, percentage) | scored "Overdone" | 4% | 20% | 26% | 28% | 40% |
- `2` (results_FINAL.md:1624, bare number) - T1: L2=2, L3=13, L4=29, L5=4, **L6=2**
- `13` (results_FINAL.md:1624, bare number) - T1: L2=2, L3=13, L4=29, L5=4, **L6=2**
- `29` (results_FINAL.md:1624, bare number) - T1: L2=2, L3=13, L4=29, L5=4, **L6=2**
- `4` (results_FINAL.md:1624, bare number) - T1: L2=2, L3=13, L4=29, L5=4, **L6=2**
- `2` (results_FINAL.md:1624, bare number) - T1: L2=2, L3=13, L4=29, L5=4, **L6=2**
- `6` (results_FINAL.md:1625, bare number) - T5: L2=6, L3=3, L4=20, L5=1, **L6=20**
- `3` (results_FINAL.md:1625, bare number) - T5: L2=6, L3=3, L4=20, L5=1, **L6=20**
- `20` (results_FINAL.md:1625, bare number) - T5: L2=6, L3=3, L4=20, L5=1, **L6=20**
- `1` (results_FINAL.md:1625, bare number) - T5: L2=6, L3=3, L4=20, L5=1, **L6=20**
- `20` (results_FINAL.md:1625, bare number) - T5: L2=6, L3=3, L4=20, L5=1, **L6=20**
- `20` (results_FINAL.md:1627, count or denominator) So the measured decline is substantially the statement that 20 of 50 turn-5 outputs are
- `50` (results_FINAL.md:1627, count or denominator) So the measured decline is substantially the statement that 20 of 50 turn-5 outputs are
- `5` (results_FINAL.md:1627, count or denominator) So the measured decline is substantially the statement that 20 of 50 turn-5 outputs are

### [results_FINAL.md] 19. The 6 -> 2 recode determines the sign of the central result -- What this does and does not threaten

*- **Filter:** `stripped_rescore_full.jsonl`, field `stripped_level_raw` for the un-recoded*

- `13` (results_FINAL.md:1635, bare number) levels. Section 13's stability result is untouched.
- `1` (results_FINAL.md:1636, bare number) - **The revision tax is exposed.** It rests on `t* = 1` for all six models, which rests on
- `1559` (results_FINAL.md:1639, bare number) claim is made either way. Note also that `analyze.py:1559` uses C = 5e-7, not the C = 1e-4
- `7` (results_FINAL.md:1639, bare number) claim is made either way. Note also that `analyze.py:1559` uses C = 5e-7, not the C = 1e-4
- `4` (results_FINAL.md:1639, bare number) claim is made either way. Note also that `analyze.py:1559` uses C = 5e-7, not the C = 1e-4
- `1` (results_FINAL.md:1641, bare number) - **The targeted-feedback result is likely robust** (its inputs are level 1-3, where level 6
- `3` (results_FINAL.md:1641, bare number) - **The targeted-feedback result is likely robust** (its inputs are level 1-3, where level 6
- `6` (results_FINAL.md:1641, bare number) - **The targeted-feedback result is likely robust** (its inputs are level 1-3, where level 6

### [results_FINAL.md] 19. The 6 -> 2 recode determines the sign of the central result -- The honest positions available

*- **Filter:** `stripped_rescore_full.jsonl`, field `stripped_level_raw` for the un-recoded*

- `1` (results_FINAL.md:1646, bare number) 1. Keep the recode and disclose the sensitivity, arguing that drift from the ask is a quality
- `4` (results_FINAL.md:1647, percentage) failure. Defensible, and the monotone rise from 4% to 40% is itself a finding worth stating
- `40` (results_FINAL.md:1647, percentage) failure. Defensible, and the monotone rise from 4% to 40% is itself a finding worth stating
- `2` (results_FINAL.md:1649, bare number) 2. Report the decline on a scale that does not require the judgment, e.g. share of turn-5
- `5` (results_FINAL.md:1649, bare number) 2. Report the decline on a scale that does not require the judgment, e.g. share of turn-5
- `6` (results_FINAL.md:1650, bare number) outputs at or above sufficiency, or report level 6 as its own outcome.
- `3` (results_FINAL.md:1651, bare number) 3. Re-run the evaluation on a monotone 1-5 scale with over-elaboration scored separately.
- `1` (results_FINAL.md:1651, bare number) 3. Re-run the evaluation on a monotone 1-5 scale with over-elaboration scored separately.
- `5` (results_FINAL.md:1651, bare number) 3. Re-run the evaluation on a monotone 1-5 scale with over-elaboration scored separately.

### [results_FINAL.md] 19. The 6 -> 2 recode determines the sign of the central result -- 19b. The human raters did not treat "Overdone" as worse

*- **Filter:** `stripped_rescore_full.jsonl`, field `stripped_level_raw` for the un-recoded*

- `2026` (results_FINAL.md:1657, bare number) Checked 2026-09-21. Joining the 64 calibration items to the three human raters through
- `09` (results_FINAL.md:1657, bare number) Checked 2026-09-21. Joining the 64 calibration items to the three human raters through
- `21` (results_FINAL.md:1657, bare number) Checked 2026-09-21. Joining the 64 calibration items to the three human raters through
- `64` (results_FINAL.md:1657, bare number) Checked 2026-09-21. Joining the 64 calibration items to the three human raters through
- `2` (results_FINAL.md:1662, mean or delta) | 2 | 3.00 | 1 |
- `3.00` (results_FINAL.md:1662, mean or delta) | 2 | 3.00 | 1 |
- `1` (results_FINAL.md:1662, mean or delta) | 2 | 3.00 | 1 |
- `3` (results_FINAL.md:1663, mean or delta) | 3 | 2.89 | 3 |
- `2.89` (results_FINAL.md:1663, mean or delta) | 3 | 2.89 | 3 |
- `3` (results_FINAL.md:1663, mean or delta) | 3 | 2.89 | 3 |
- `4` (results_FINAL.md:1664, mean or delta) | 4 (Sufficient) | 4.23 | 34 |
- `4.23` (results_FINAL.md:1664, mean or delta) | 4 (Sufficient) | 4.23 | 34 |
- `34` (results_FINAL.md:1664, mean or delta) | 4 (Sufficient) | 4.23 | 34 |
- `5` (results_FINAL.md:1665, mean or delta) | 5 (Polished) | 4.48 | 22 |
- `4.48` (results_FINAL.md:1665, mean or delta) | 5 (Polished) | 4.48 | 22 |
- `22` (results_FINAL.md:1665, mean or delta) | 5 (Polished) | 4.48 | 22 |
- `6` (results_FINAL.md:1666, mean or delta) | **6 (Overdone)** | **5.33** | **4** |
- `5.33` (results_FINAL.md:1666, mean or delta) | **6 (Overdone)** | **5.33** | **4** |
- `4` (results_FINAL.md:1666, mean or delta) | **6 (Overdone)** | **5.33** | **4** |
- `2` (results_FINAL.md:1670, bare number) as level 2.
- `4` (results_FINAL.md:1672, bare number) - **Filter:** `judge_calibration.jsonl` (judge = claude-sonnet-4, the selected evaluator),
- `4` (results_FINAL.md:1675, count or denominator) - **n = 4 for the level-6 band.** Four items cannot settle the construct, and this is not
- `6` (results_FINAL.md:1675, count or denominator) - **n = 4 for the level-6 band.** Four items cannot settle the construct, and this is not
- `0.228` (results_FINAL.md:1678, reliability or effect size) - The kappa improvement from the recode (Liam-Troy 0.228 to 0.406) is about overall scale
- `0.406` (results_FINAL.md:1678, reliability or effect size) - The kappa improvement from the recode (Liam-Troy 0.228 to 0.406) is about overall scale
- `6` (results_FINAL.md:1679, bare number) coherence and is not evidence that level 6 belongs at the bottom.
- `6` (results_FINAL.md:1681, bare number) This is what makes the level-6 decision substantive rather than clerical: the paper's own

### [results_FINAL.md] 20. Overdone as a distinct failure: the decision and what it gives

*- **Filter:** `judge_calibration.jsonl` (judge = claude-sonnet-4, the selected evaluator),*

- `20` (results_FINAL.md:1684, bare number) ## 20. Overdone as a distinct failure: the decision and what it gives
- `2026` (results_FINAL.md:1686, bare number) **Decided 2026-09-22 (author's construct call):** "Overdone" is worse than Sufficient and
- `09` (results_FINAL.md:1686, bare number) **Decided 2026-09-22 (author's construct call):** "Overdone" is worse than Sufficient and
- `22` (results_FINAL.md:1686, bare number) **Decided 2026-09-22 (author's construct call):** "Overdone" is worse than Sufficient and
- `6` (results_FINAL.md:1688, bare number) faults, and the published 6 -> 2 recode collapses them into one.
- `2` (results_FINAL.md:1688, bare number) faults, and the published 6 -> 2 recode collapses them into one.

### [results_FINAL.md] 20. Overdone as a distinct failure: the decision and what it gives -- The ordering

*- **Filter:** `judge_calibration.jsonl` (judge = claude-sonnet-4, the selected evaluator),*

- `1` (results_FINAL.md:1694, bare number) | 1 | Inadequate | clearly worse |
- `2` (results_FINAL.md:1695, bare number) | 2 | Incomplete, missing requested components | clearly worse |
- `3` (results_FINAL.md:1696, bare number) | 3 | Functional, all components present with clear weaknesses | below sufficient |
- `6` (results_FINAL.md:1697, bare number) | 6 | **Overdone, all components present plus unrequested drift** | **below sufficient, ranked with 3** |
- `3` (results_FINAL.md:1697, bare number) | 6 | **Overdone, all components present plus unrequested drift** | **below sufficient, ranked with 3** |
- `4` (results_FINAL.md:1698, bare number) | 4 | Sufficient | the threshold |
- `5` (results_FINAL.md:1699, bare number) | 5 | Polished | clearly better |

### [results_FINAL.md] 20. Overdone as a distinct failure: the decision and what it gives -- The ordinal result under each placement

*- **Filter:** `judge_calibration.jsonl` (judge = claude-sonnet-4, the selected evaluator),*

- `50` (results_FINAL.md:1707, count or denominator) | Overdone placed at | Panel delta (n=50) | p |
- `2` (results_FINAL.md:1709, mean or delta) | 2, as published | -0.740 | 1.01e-4 |
- `0.740` (results_FINAL.md:1709, mean or delta) | 2, as published | -0.740 | 1.01e-4 |
- `1` (results_FINAL.md:1709, mean or delta) | 2, as published | -0.740 | 1.01e-4 |
- `4` (results_FINAL.md:1709, mean or delta) | 2, as published | -0.740 | 1.01e-4 |
- `3` (results_FINAL.md:1710, mean or delta) | **3, Functional (decided)** | **-0.380** | **4.42e-3** |
- `0.380` (results_FINAL.md:1710, mean or delta) | **3, Functional (decided)** | **-0.380** | **4.42e-3** |
- `4` (results_FINAL.md:1710, mean or delta) | **3, Functional (decided)** | **-0.380** | **4.42e-3** |
- `3` (results_FINAL.md:1710, mean or delta) | **3, Functional (decided)** | **-0.380** | **4.42e-3** |
- `4` (results_FINAL.md:1711, mean or delta) | 4, no penalty | -0.020 | 0.796 |
- `0.020` (results_FINAL.md:1711, mean or delta) | 4, no penalty | -0.020 | 0.796 |
- `0.796` (results_FINAL.md:1711, mean or delta) | 4, no penalty | -0.020 | 0.796 |
- `19` (results_FINAL.md:1713, bare number) - **Filter:** as Section 19. Only the mapping of level 6 changes.
- `6` (results_FINAL.md:1713, bare number) - **Filter:** as Section 19. Only the mapping of level 6 changes.

### [results_FINAL.md] 20. Overdone as a distinct failure: the decision and what it gives -- The stronger result: the two failure modes move in opposite directions

*- **Filter:** as Section 19. Only the mapping of level 6 changes.*

- `50` (results_FINAL.md:1717, bare number) Keeping the faults separate, paired across the 50-trial panel from Turn 1 to Turn 5,
- `1` (results_FINAL.md:1717, bare number) Keeping the faults separate, paired across the 50-trial panel from Turn 1 to Turn 5,
- `5` (results_FINAL.md:1717, bare number) Keeping the faults separate, paired across the 50-trial panel from Turn 1 to Turn 5,
- `19` (results_FINAL.md:1722, mean or delta) | became overdone | 19 | 1 | **+18** | **4.01e-5** |
- `1` (results_FINAL.md:1722, mean or delta) | became overdone | 19 | 1 | **+18** | **4.01e-5** |
- `18` (results_FINAL.md:1722, mean or delta) | became overdone | 19 | 1 | **+18** | **4.01e-5** |
- `4` (results_FINAL.md:1722, mean or delta) | became overdone | 19 | 1 | **+18** | **4.01e-5** |
- `5` (results_FINAL.md:1722, mean or delta) | became overdone | 19 | 1 | **+18** | **4.01e-5** |
- `5` (results_FINAL.md:1723, mean or delta) | became below sufficient | 5 | 11 | -6 | 0.21 |
- `11` (results_FINAL.md:1723, mean or delta) | became below sufficient | 5 | 11 | -6 | 0.21 |
- `6` (results_FINAL.md:1723, mean or delta) | became below sufficient | 5 | 11 | -6 | 0.21 |
- `0.21` (results_FINAL.md:1723, mean or delta) | became below sufficient | 5 | 11 | -6 | 0.21 |
- `4` (results_FINAL.md:1724, mean or delta) | left sufficient or polished | 4 | 16 | -12 | 1.18e-2 |
- `16` (results_FINAL.md:1724, mean or delta) | left sufficient or polished | 4 | 16 | -12 | 1.18e-2 |
- `12` (results_FINAL.md:1724, mean or delta) | left sufficient or polished | 4 | 16 | -12 | 1.18e-2 |
- `1` (results_FINAL.md:1724, mean or delta) | left sufficient or polished | 4 | 16 | -12 | 1.18e-2 |
- `2` (results_FINAL.md:1724, mean or delta) | left sufficient or polished | 4 | 16 | -12 | 1.18e-2 |
- `5` (results_FINAL.md:1726, bare number) Where Turn 5 landed relative to Turn 1: sufficient+ stayed sufficient+ in 17 trials, went
- `1` (results_FINAL.md:1726, bare number) Where Turn 5 landed relative to Turn 1: sufficient+ stayed sufficient+ in 17 trials, went
- `17` (results_FINAL.md:1726, bare number) Where Turn 5 landed relative to Turn 1: sufficient+ stayed sufficient+ in 17 trials, went
- `12` (results_FINAL.md:1727, bare number) overdone in 12, went below sufficient in 4. Seven trials that began below sufficient became
- `4` (results_FINAL.md:1727, bare number) overdone in 12, went below sufficient in 4. Seven trials that began below sufficient became
- `6` (results_FINAL.md:1734, bare number) - **Filter:** panel as above, `stripped_level_raw`. "Overdone" is level 6, "below sufficient"
- `1` (results_FINAL.md:1735, bare number) is 1-3, "sufficient or polished" is 4-5. `scipy.stats.binomtest` on the discordant pairs.
- `3` (results_FINAL.md:1735, bare number) is 1-3, "sufficient or polished" is 4-5. `scipy.stats.binomtest` on the discordant pairs.
- `4` (results_FINAL.md:1735, bare number) is 1-3, "sufficient or polished" is 4-5. `scipy.stats.binomtest` on the discordant pairs.
- `5` (results_FINAL.md:1735, bare number) is 1-3, "sufficient or polished" is 4-5. `scipy.stats.binomtest` on the discordant pairs.

### [results_FINAL.md] 20. Overdone as a distinct failure: the decision and what it gives -- Why this is the better claim

*- **Filter:** panel as above, `stripped_level_raw`. "Overdone" is level 6, "below sufficient"*

- `1` (results_FINAL.md:1739, bare number) 1. It rests on a count of a category the evaluator assigns directly, not on a contested
- `2` (results_FINAL.md:1741, bare number) 2. It explains Section 19b, where the human raters scored judge-Overdone items highest at
- `5.33` (results_FINAL.md:1742, mean or delta) 5.33. Those outputs are not bad-looking; they have drifted from the ask. The raters were
- `3` (results_FINAL.md:1744, mean or delta) 3. It explains Section 4.3, where blind readers could not reliably pick the first draft. A
- `4.3` (results_FINAL.md:1744, mean or delta) 3. It explains Section 4.3, where blind readers could not reliably pick the first draft. A
- `4` (results_FINAL.md:1746, bare number) 4. Figure 1 is exactly this case: the model dropped the explanations the prompt requested and
- `1` (results_FINAL.md:1746, bare number) 4. Figure 1 is exactly this case: the model dropped the explanations the prompt requested and

### [results_FINAL.md] 20. Overdone as a distinct failure: the decision and what it gives -- What it costs

*- **Filter:** panel as above, `stripped_level_raw`. "Overdone" is level 6, "below sufficient"*

- `0.74` (results_FINAL.md:1751, mean or delta) The ordinal cliff restates from -0.74 to -0.38, so the abstract, introduction, Results 4.2 and
- `0.38` (results_FINAL.md:1751, mean or delta) The ordinal cliff restates from -0.74 to -0.38, so the abstract, introduction, Results 4.2 and
- `4.2` (results_FINAL.md:1751, mean or delta) The ordinal cliff restates from -0.74 to -0.38, so the abstract, introduction, Results 4.2 and
- `13` (results_FINAL.md:1754, bare number) score and Section 13's stability are untouched.

### [results_FINAL.md] 21. Carry-through of the Overdone-at-3 decision, 2026-09-22

*- **Filter:** panel as above, `stripped_level_raw`. "Overdone" is level 6, "below sufficient"*

- `21` (results_FINAL.md:1756, bare number) ## 21. Carry-through of the Overdone-at-3 decision, 2026-09-22
- `3` (results_FINAL.md:1756, bare number) ## 21. Carry-through of the Overdone-at-3 decision, 2026-09-22
- `2026` (results_FINAL.md:1756, bare number) ## 21. Carry-through of the Overdone-at-3 decision, 2026-09-22
- `09` (results_FINAL.md:1756, bare number) ## 21. Carry-through of the Overdone-at-3 decision, 2026-09-22
- `22` (results_FINAL.md:1756, bare number) ## 21. Carry-through of the Overdone-at-3 decision, 2026-09-22
- `3` (results_FINAL.md:1758, bare number) `config.OVERDONE_RANK = 3` is now the single definition; six scripts that hardcoded the
- `605` (results_FINAL.md:1760, count or denominator) from their `_raw` counterparts (605 of 3,600 values changed). Every figure below reproduces
- `3,600` (results_FINAL.md:1760, count or denominator) from their `_raw` counterparts (605 of 3,600 values changed). Every figure below reproduces
- `6` (results_FINAL.md:1763, bare number) | Quantity | Old (6→2) | New (6→3) |
- `2` (results_FINAL.md:1763, bare number) | Quantity | Old (6→2) | New (6→3) |
- `6` (results_FINAL.md:1763, bare number) | Quantity | Old (6→2) | New (6→3) |
- `3` (results_FINAL.md:1763, bare number) | Quantity | Old (6→2) | New (6→3) |
- `0.74` (results_FINAL.md:1765, mean or delta) | Panel cliff | -0.74, p 1.01e-4 | **-0.38, p 4.42e-3** |
- `1` (results_FINAL.md:1765, mean or delta) | Panel cliff | -0.74, p 1.01e-4 | **-0.38, p 4.42e-3** |
- `4` (results_FINAL.md:1765, mean or delta) | Panel cliff | -0.74, p 1.01e-4 | **-0.38, p 4.42e-3** |
- `0.38` (results_FINAL.md:1765, mean or delta) | Panel cliff | -0.74, p 1.01e-4 | **-0.38, p 4.42e-3** |
- `4` (results_FINAL.md:1765, mean or delta) | Panel cliff | -0.74, p 1.01e-4 | **-0.38, p 4.42e-3** |
- `3` (results_FINAL.md:1765, mean or delta) | Panel cliff | -0.74, p 1.01e-4 | **-0.38, p 4.42e-3** |
- `0.67` (results_FINAL.md:1766, mean or delta) | Llama-only cliff | -0.67, p 3.76e-4 | **-0.31, p 1.80e-2** |
- `3` (results_FINAL.md:1766, mean or delta) | Llama-only cliff | -0.67, p 3.76e-4 | **-0.31, p 1.80e-2** |
- `4` (results_FINAL.md:1766, mean or delta) | Llama-only cliff | -0.67, p 3.76e-4 | **-0.31, p 1.80e-2** |
- `0.31` (results_FINAL.md:1766, mean or delta) | Llama-only cliff | -0.67, p 3.76e-4 | **-0.31, p 1.80e-2** |
- `1` (results_FINAL.md:1766, mean or delta) | Llama-only cliff | -0.67, p 3.76e-4 | **-0.31, p 1.80e-2** |
- `2` (results_FINAL.md:1766, mean or delta) | Llama-only cliff | -0.67, p 3.76e-4 | **-0.31, p 1.80e-2** |
- `0.94` (results_FINAL.md:1767, mean or delta) | Unstripped panel cliff | -0.94, p 3.32e-6 | **-0.44, p 3.79e-4** |
- `3` (results_FINAL.md:1767, mean or delta) | Unstripped panel cliff | -0.94, p 3.32e-6 | **-0.44, p 3.79e-4** |
- `6` (results_FINAL.md:1767, mean or delta) | Unstripped panel cliff | -0.94, p 3.32e-6 | **-0.44, p 3.79e-4** |
- `0.44` (results_FINAL.md:1767, mean or delta) | Unstripped panel cliff | -0.94, p 3.32e-6 | **-0.44, p 3.79e-4** |
- `3` (results_FINAL.md:1767, mean or delta) | Unstripped panel cliff | -0.94, p 3.32e-6 | **-0.44, p 3.79e-4** |
- `4` (results_FINAL.md:1767, mean or delta) | Unstripped panel cliff | -0.94, p 3.32e-6 | **-0.44, p 3.79e-4** |
- `4.11` (results_FINAL.md:1768, mean or delta) | Pooled T1→T5 | 4.11→3.07, -1.04 | **4.17→3.42, -0.75** |
- `3.07` (results_FINAL.md:1768, mean or delta) | Pooled T1→T5 | 4.11→3.07, -1.04 | **4.17→3.42, -0.75** |
- `1.04` (results_FINAL.md:1768, mean or delta) | Pooled T1→T5 | 4.11→3.07, -1.04 | **4.17→3.42, -0.75** |
- `4.17` (results_FINAL.md:1768, mean or delta) | Pooled T1→T5 | 4.11→3.07, -1.04 | **4.17→3.42, -0.75** |
- `3.42` (results_FINAL.md:1768, mean or delta) | Pooled T1→T5 | 4.11→3.07, -1.04 | **4.17→3.42, -0.75** |
- `0.75` (results_FINAL.md:1768, mean or delta) | Pooled T1→T5 | 4.11→3.07, -1.04 | **4.17→3.42, -0.75** |
- `21` (results_FINAL.md:1769, percentage) | Meta-commentary share of the cliff | 21% | **14%** |
- `14` (results_FINAL.md:1769, percentage) | Meta-commentary share of the cliff | 21% | **14%** |
- `69.6` (results_FINAL.md:1770, percentage) | Revision direction, movers down | 69.6% (199/286) | **68.7% (184/268)** |
- `199` (results_FINAL.md:1770, percentage) | Revision direction, movers down | 69.6% (199/286) | **68.7% (184/268)** |
- `286` (results_FINAL.md:1770, percentage) | Revision direction, movers down | 69.6% (199/286) | **68.7% (184/268)** |
- `68.7` (results_FINAL.md:1770, percentage) | Revision direction, movers down | 69.6% (199/286) | **68.7% (184/268)** |
- `184` (results_FINAL.md:1770, percentage) | Revision direction, movers down | 69.6% (199/286) | **68.7% (184/268)** |
- `268` (results_FINAL.md:1770, percentage) | Revision direction, movers down | 69.6% (199/286) | **68.7% (184/268)** |
- `0.41` (results_FINAL.md:1771, mean or delta) | Mean reversion, input below / at threshold | +0.41 / -0.56 | **+0.35 / -0.38** |
- `0.56` (results_FINAL.md:1771, mean or delta) | Mean reversion, input below / at threshold | +0.41 / -0.56 | **+0.35 / -0.38** |
- `0.35` (results_FINAL.md:1771, mean or delta) | Mean reversion, input below / at threshold | +0.41 / -0.56 | **+0.35 / -0.38** |
- `0.38` (results_FINAL.md:1771, mean or delta) | Mean reversion, input below / at threshold | +0.41 / -0.56 | **+0.35 / -0.38** |
- `1.16` (results_FINAL.md:1772, mean or delta) | Targeted feedback | +1.16, p 5.7e-19 | **+1.01, p 1.9e-19** |
- `5` (results_FINAL.md:1772, mean or delta) | Targeted feedback | +1.16, p 5.7e-19 | **+1.01, p 1.9e-19** |
- `19` (results_FINAL.md:1772, mean or delta) | Targeted feedback | +1.16, p 5.7e-19 | **+1.01, p 1.9e-19** |
- `1.01` (results_FINAL.md:1772, mean or delta) | Targeted feedback | +1.16, p 5.7e-19 | **+1.01, p 1.9e-19** |
- `1` (results_FINAL.md:1772, mean or delta) | Targeted feedback | +1.16, p 5.7e-19 | **+1.01, p 1.9e-19** |
- `19` (results_FINAL.md:1772, mean or delta) | Targeted feedback | +1.16, p 5.7e-19 | **+1.01, p 1.9e-19** |
- `13` (results_FINAL.md:1773, mean or delta) | Domain deltas (Table 13) | -0.94/-0.93/-0.58/-0.53/-0.77 | **-0.59/-0.47/-0.32/-0.24/-0.77** |
- `0.94` (results_FINAL.md:1773, mean or delta) | Domain deltas (Table 13) | -0.94/-0.93/-0.58/-0.53/-0.77 | **-0.59/-0.47/-0.32/-0.24/-0.77** |
- `0.93` (results_FINAL.md:1773, mean or delta) | Domain deltas (Table 13) | -0.94/-0.93/-0.58/-0.53/-0.77 | **-0.59/-0.47/-0.32/-0.24/-0.77** |
- `0.58` (results_FINAL.md:1773, mean or delta) | Domain deltas (Table 13) | -0.94/-0.93/-0.58/-0.53/-0.77 | **-0.59/-0.47/-0.32/-0.24/-0.77** |
- `0.53` (results_FINAL.md:1773, mean or delta) | Domain deltas (Table 13) | -0.94/-0.93/-0.58/-0.53/-0.77 | **-0.59/-0.47/-0.32/-0.24/-0.77** |
- `0.77` (results_FINAL.md:1773, mean or delta) | Domain deltas (Table 13) | -0.94/-0.93/-0.58/-0.53/-0.77 | **-0.59/-0.47/-0.32/-0.24/-0.77** |
- `0.59` (results_FINAL.md:1773, mean or delta) | Domain deltas (Table 13) | -0.94/-0.93/-0.58/-0.53/-0.77 | **-0.59/-0.47/-0.32/-0.24/-0.77** |
- `0.47` (results_FINAL.md:1773, mean or delta) | Domain deltas (Table 13) | -0.94/-0.93/-0.58/-0.53/-0.77 | **-0.59/-0.47/-0.32/-0.24/-0.77** |
- `0.32` (results_FINAL.md:1773, mean or delta) | Domain deltas (Table 13) | -0.94/-0.93/-0.58/-0.53/-0.77 | **-0.59/-0.47/-0.32/-0.24/-0.77** |
- `0.24` (results_FINAL.md:1773, mean or delta) | Domain deltas (Table 13) | -0.94/-0.93/-0.58/-0.53/-0.77 | **-0.59/-0.47/-0.32/-0.24/-0.77** |
- `0.77` (results_FINAL.md:1773, mean or delta) | Domain deltas (Table 13) | -0.94/-0.93/-0.58/-0.53/-0.77 | **-0.59/-0.47/-0.32/-0.24/-0.77** |
- `0.41` (results_FINAL.md:1775, reliability or effect size) | Inter-rater QW kappa range | 0.41-0.60 | **0.48-0.61** |
- `0.60` (results_FINAL.md:1775, reliability or effect size) | Inter-rater QW kappa range | 0.41-0.60 | **0.48-0.61** |
- `0.48` (results_FINAL.md:1775, reliability or effect size) | Inter-rater QW kappa range | 0.41-0.60 | **0.48-0.61** |
- `0.61` (results_FINAL.md:1775, reliability or effect size) | Inter-rater QW kappa range | 0.41-0.60 | **0.48-0.61** |
- `0.529` (results_FINAL.md:1776, mean or delta) | Krippendorff alpha | 0.529 | **0.540** |
- `0.540` (results_FINAL.md:1776, mean or delta) | Krippendorff alpha | 0.529 | **0.540** |
- `1` (results_FINAL.md:1777, percentage) | Within-1 agreement (A-C, B-C) | 81.2%, 87.5% | **95.3%, 93.8%** |
- `81.2` (results_FINAL.md:1777, percentage) | Within-1 agreement (A-C, B-C) | 81.2%, 87.5% | **95.3%, 93.8%** |
- `87.5` (results_FINAL.md:1777, percentage) | Within-1 agreement (A-C, B-C) | 81.2%, 87.5% | **95.3%, 93.8%** |
- `95.3` (results_FINAL.md:1777, percentage) | Within-1 agreement (A-C, B-C) | 81.2%, 87.5% | **95.3%, 93.8%** |
- `93.8` (results_FINAL.md:1777, percentage) | Within-1 agreement (A-C, B-C) | 81.2%, 87.5% | **95.3%, 93.8%** |
- `87.6` (results_FINAL.md:1779, percentage) Unchanged, and verified so rather than assumed: 87.6% of first drafts sufficient (631/720),
- `631` (results_FINAL.md:1779, percentage) Unchanged, and verified so rather than assumed: 87.6% of first drafts sufficient (631/720),
- `720` (results_FINAL.md:1779, percentage) Unchanged, and verified so rather than assumed: 87.6% of first drafts sufficient (631/720),
- `39.6` (results_FINAL.md:1780, percentage) 39.6% revision-despite-sufficiency (411/1,038), 144/524 = 27.5% ending below, all six STET
- `411` (results_FINAL.md:1780, percentage) 39.6% revision-despite-sufficiency (411/1,038), 144/524 = 27.5% ending below, all six STET
- `1,038` (results_FINAL.md:1780, percentage) 39.6% revision-despite-sufficiency (411/1,038), 144/524 = 27.5% ending below, all six STET
- `144` (results_FINAL.md:1780, percentage) 39.6% revision-despite-sufficiency (411/1,038), 144/524 = 27.5% ending below, all six STET
- `524` (results_FINAL.md:1780, percentage) 39.6% revision-despite-sufficiency (411/1,038), 144/524 = 27.5% ending below, all six STET
- `27.5` (results_FINAL.md:1780, percentage) 39.6% revision-despite-sufficiency (411/1,038), 144/524 = 27.5% ending below, all six STET
- `1` (results_FINAL.md:1781, bare number) scores, binary rater agreement, and the revision tax, since **t\* remains Turn 1 for all six
- `7` (results_FINAL.md:1782, bare number) models** under the new placement at both C = 5e-7 and C = 1e-4. Under the old placement
- `4` (results_FINAL.md:1782, bare number) models** under the new placement at both C = 5e-7 and C = 1e-4. Under the old placement
- `7` (results_FINAL.md:1783, count or denominator) C = 5e-7 gave GPT-4o t\* = T5 on n = 3, so the claim is cleaner now than it was.
- `3` (results_FINAL.md:1783, count or denominator) C = 5e-7 gave GPT-4o t\* = T5 on n = 3, so the claim is cleaner now than it was.
- `0.41` (results_FINAL.md:1785, reliability or effect size) Agreement improves slightly under the new placement (kappa floor 0.41 to 0.48, alpha 0.529 to
- `0.48` (results_FINAL.md:1785, reliability or effect size) Agreement improves slightly under the new placement (kappa floor 0.41 to 0.48, alpha 0.529 to
- `0.529` (results_FINAL.md:1785, reliability or effect size) Agreement improves slightly under the new placement (kappa floor 0.41 to 0.48, alpha 0.529 to
- `0.540` (results_FINAL.md:1786, mean or delta) 0.540, within-1 up on two of three pairs), which is a small independent point in its favour.
- `1` (results_FINAL.md:1786, mean or delta) 0.540, within-1 up on two of three pairs), which is a small independent point in its favour.

### [results_FINAL.md] 21. Carry-through of the Overdone-at-3 decision, 2026-09-22 -- One consequence that had to be stated rather than absorbed

*- **Filter:** panel as above, `stripped_level_raw`. "Overdone" is level 6, "below sufficient"*

- `0.5` (results_FINAL.md:1790, count or denominator) The appendix power analysis gives a panel-level MDE of 0.5 levels. The ordinal decline is now
- `0.44` (results_FINAL.md:1791, mean or delta) 0.44 unstripped and 0.38 stripped, **both below that MDE**, so the ordinal magnitude is not
- `0.38` (results_FINAL.md:1791, mean or delta) 0.44 unstripped and 0.38 stripped, **both below that MDE**, so the ordinal magnitude is not
- `50` (results_FINAL.md:1792, count or denominator) powered at n = 50. The appendix now says so, and reports the ordinal cliff as a supporting
- `19` (results_FINAL.md:1793, count or denominator) estimate. The count is powered: 19 of 50 trials became over-elaborated against 1 the other
- `50` (results_FINAL.md:1793, count or denominator) estimate. The count is powered: 19 of 50 trials became over-elaborated against 1 the other
- `1` (results_FINAL.md:1793, count or denominator) estimate. The count is powered: 19 of 50 trials became over-elaborated against 1 the other
- `4` (results_FINAL.md:1794, p-value) way, exact binomial p = 4.01e-5. This is the strongest reason the headline is the count.
- `5` (results_FINAL.md:1794, p-value) way, exact binomial p = 4.01e-5. This is the strongest reason the headline is the count.

### [results_FINAL.md] 21. Carry-through of the Overdone-at-3 decision, 2026-09-22 -- Not recomputed

*- **Filter:** panel as above, `stripped_level_raw`. "Overdone" is level 6, "below sufficient"*

- `0.505` (results_FINAL.md:1798, reliability or effect size) The evaluator-versus-human figures (Spearman r = 0.505, QW kappa = 0.526) could not be
- `0.526` (results_FINAL.md:1798, reliability or effect size) The evaluator-versus-human figures (Spearman r = 0.505, QW kappa = 0.526) could not be
- `0.589` (results_FINAL.md:1799, count or denominator) reproduced on any basis I tried; my reconstruction gives 0.589 / 0.613 under the old placement,
- `0.613` (results_FINAL.md:1799, count or denominator) reproduced on any basis I tried; my reconstruction gives 0.589 / 0.613 under the old placement,

### [MOMENTUM_SUMMARY.md] 

- `2` (MOMENTUM_SUMMARY.md:1, bare number) # Study 2: Momentum Experiment -- Summary for Research Group

### [MOMENTUM_SUMMARY.md] Overview

- `2` (MOMENTUM_SUMMARY.md:5, bare number) Study 2 tests whether prior revision history ("momentum") shifts the revision gate established in Study 1. In Study 1, we found that the follow-up probe's phrasing -- not the stated quality threshold 
- `1` (MOMENTUM_SUMMARY.md:5, bare number) Study 2 tests whether prior revision history ("momentum") shifts the revision gate established in Study 1. In Study 1, we found that the follow-up probe's phrasing -- not the stated quality threshold 
- `1` (MOMENTUM_SUMMARY.md:5, bare number) Study 2 tests whether prior revision history ("momentum") shifts the revision gate established in Study 1. In Study 1, we found that the follow-up probe's phrasing -- not the stated quality threshold 
- `2` (MOMENTUM_SUMMARY.md:5, bare number) Study 2 tests whether prior revision history ("momentum") shifts the revision gate established in Study 1. In Study 1, we found that the follow-up probe's phrasing -- not the stated quality threshold 
- `1` (MOMENTUM_SUMMARY.md:5, bare number) Study 2 tests whether prior revision history ("momentum") shifts the revision gate established in Study 1. In Study 1, we found that the follow-up probe's phrasing -- not the stated quality threshold 
- `2` (MOMENTUM_SUMMARY.md:5, bare number) Study 2 tests whether prior revision history ("momentum") shifts the revision gate established in Study 1. In Study 1, we found that the follow-up probe's phrasing -- not the stated quality threshold 
- `3` (MOMENTUM_SUMMARY.md:5, bare number) Study 2 tests whether prior revision history ("momentum") shifts the revision gate established in Study 1. In Study 1, we found that the follow-up probe's phrasing -- not the stated quality threshold 

### [MOMENTUM_SUMMARY.md] Design

- `0` (MOMENTUM_SUMMARY.md:9, bare number) - **Momentum dose**: 0 (cold baseline from Study 1), 1, 2, or 3 prior leading-probe rounds before the evaluative probe
- `1` (MOMENTUM_SUMMARY.md:9, bare number) - **Momentum dose**: 0 (cold baseline from Study 1), 1, 2, or 3 prior leading-probe rounds before the evaluative probe
- `1` (MOMENTUM_SUMMARY.md:9, bare number) - **Momentum dose**: 0 (cold baseline from Study 1), 1, 2, or 3 prior leading-probe rounds before the evaluative probe
- `2` (MOMENTUM_SUMMARY.md:9, bare number) - **Momentum dose**: 0 (cold baseline from Study 1), 1, 2, or 3 prior leading-probe rounds before the evaluative probe
- `3` (MOMENTUM_SUMMARY.md:9, bare number) - **Momentum dose**: 0 (cold baseline from Study 1), 1, 2, or 3 prior leading-probe rounds before the evaluative probe
- `4` (MOMENTUM_SUMMARY.md:10, mean or delta) - **Models**: GPT-4o, Claude Sonnet 4, Gemini 2.5 Flash
- `2.5` (MOMENTUM_SUMMARY.md:10, mean or delta) - **Models**: GPT-4o, Claude Sonnet 4, Gemini 2.5 Flash
- `0` (MOMENTUM_SUMMARY.md:11, bare number) - **Thresholds**: 0, 75, 90, 100 (reduced from 8 levels in Study 1)
- `75` (MOMENTUM_SUMMARY.md:11, bare number) - **Thresholds**: 0, 75, 90, 100 (reduced from 8 levels in Study 1)
- `90` (MOMENTUM_SUMMARY.md:11, bare number) - **Thresholds**: 0, 75, 90, 100 (reduced from 8 levels in Study 1)
- `100` (MOMENTUM_SUMMARY.md:11, bare number) - **Thresholds**: 0, 75, 90, 100 (reduced from 8 levels in Study 1)
- `8` (MOMENTUM_SUMMARY.md:11, bare number) - **Thresholds**: 0, 75, 90, 100 (reduced from 8 levels in Study 1)
- `1` (MOMENTUM_SUMMARY.md:11, bare number) - **Thresholds**: 0, 75, 90, 100 (reduced from 8 levels in Study 1)
- `8` (MOMENTUM_SUMMARY.md:13, bare number) - **Scenarios**: all 8 from Study 1
- `1` (MOMENTUM_SUMMARY.md:13, bare number) - **Scenarios**: all 8 from Study 1
- `3` (MOMENTUM_SUMMARY.md:14, bare number) - **Runs per cell**: 3
- `1,728` (MOMENTUM_SUMMARY.md:15, bare number) - **Total new trials**: 1,728 (plus 1,920 cold baseline trials from Study 1)
- `1,920` (MOMENTUM_SUMMARY.md:15, bare number) - **Total new trials**: 1,728 (plus 1,920 cold baseline trials from Study 1)
- `1` (MOMENTUM_SUMMARY.md:15, bare number) - **Total new trials**: 1,728 (plus 1,920 cold baseline trials from Study 1)
- `1` (MOMENTUM_SUMMARY.md:16, bare number) - **Judge**: GPT-4o (same as Study 1)

### [MOMENTUM_SUMMARY.md] Key Results -- RQ4: Does revision history shift the gate?

- `23.2` (MOMENTUM_SUMMARY.md:22, p-value) **Yes, overall.** Cold baseline revision rate = 23.2%; warm (dose 1-3) = 44.6%. Chi-squared = 376.54, p < 0.0001.
- `1` (MOMENTUM_SUMMARY.md:22, p-value) **Yes, overall.** Cold baseline revision rate = 23.2%; warm (dose 1-3) = 44.6%. Chi-squared = 376.54, p < 0.0001.
- `3` (MOMENTUM_SUMMARY.md:22, p-value) **Yes, overall.** Cold baseline revision rate = 23.2%; warm (dose 1-3) = 44.6%. Chi-squared = 376.54, p < 0.0001.
- `44.6` (MOMENTUM_SUMMARY.md:22, p-value) **Yes, overall.** Cold baseline revision rate = 23.2%; warm (dose 1-3) = 44.6%. Chi-squared = 376.54, p < 0.0001.
- `376.54` (MOMENTUM_SUMMARY.md:22, p-value) **Yes, overall.** Cold baseline revision rate = 23.2%; warm (dose 1-3) = 44.6%. Chi-squared = 376.54, p < 0.0001.
- `0.0001` (MOMENTUM_SUMMARY.md:22, p-value) **Yes, overall.** Cold baseline revision rate = 23.2%; warm (dose 1-3) = 44.6%. Chi-squared = 376.54, p < 0.0001.
- `0` (MOMENTUM_SUMMARY.md:26, bare number) | Model | Dose 0 | Dose 1 | Dose 2 | Dose 3 |
- `1` (MOMENTUM_SUMMARY.md:26, bare number) | Model | Dose 0 | Dose 1 | Dose 2 | Dose 3 |
- `2` (MOMENTUM_SUMMARY.md:26, bare number) | Model | Dose 0 | Dose 1 | Dose 2 | Dose 3 |
- `3` (MOMENTUM_SUMMARY.md:26, bare number) | Model | Dose 0 | Dose 1 | Dose 2 | Dose 3 |
- `31.4` (MOMENTUM_SUMMARY.md:28, percentage) | GPT-4o | 31.4% | **98.4%** | **99.5%** | **97.4%** |
- `98.4` (MOMENTUM_SUMMARY.md:28, percentage) | GPT-4o | 31.4% | **98.4%** | **99.5%** | **97.4%** |
- `99.5` (MOMENTUM_SUMMARY.md:28, percentage) | GPT-4o | 31.4% | **98.4%** | **99.5%** | **97.4%** |
- `97.4` (MOMENTUM_SUMMARY.md:28, percentage) | GPT-4o | 31.4% | **98.4%** | **99.5%** | **97.4%** |
- `4` (MOMENTUM_SUMMARY.md:29, percentage) | Claude Sonnet 4 | 38.0% | 38.0% | 27.1% | 24.5% |
- `38.0` (MOMENTUM_SUMMARY.md:29, percentage) | Claude Sonnet 4 | 38.0% | 38.0% | 27.1% | 24.5% |
- `38.0` (MOMENTUM_SUMMARY.md:29, percentage) | Claude Sonnet 4 | 38.0% | 38.0% | 27.1% | 24.5% |
- `27.1` (MOMENTUM_SUMMARY.md:29, percentage) | Claude Sonnet 4 | 38.0% | 38.0% | 27.1% | 24.5% |
- `24.5` (MOMENTUM_SUMMARY.md:29, percentage) | Claude Sonnet 4 | 38.0% | 38.0% | 27.1% | 24.5% |
- `2.5` (MOMENTUM_SUMMARY.md:30, percentage) | Gemini 2.5 Flash | 0.3% | 12.8% | 9.9% | 8.6% |
- `0.3` (MOMENTUM_SUMMARY.md:30, percentage) | Gemini 2.5 Flash | 0.3% | 12.8% | 9.9% | 8.6% |
- `12.8` (MOMENTUM_SUMMARY.md:30, percentage) | Gemini 2.5 Flash | 0.3% | 12.8% | 9.9% | 8.6% |
- `9.9` (MOMENTUM_SUMMARY.md:30, percentage) | Gemini 2.5 Flash | 0.3% | 12.8% | 9.9% | 8.6% |
- `8.6` (MOMENTUM_SUMMARY.md:30, percentage) | Gemini 2.5 Flash | 0.3% | 12.8% | 9.9% | 8.6% |
- `31` (MOMENTUM_SUMMARY.md:32, percentage) - **GPT-4o** is extremely susceptible to momentum. A single prior revision round pushes it from 31% to 98% revision rate on the evaluative probe. It treats the conversational frame ("we're revising") 
- `98` (MOMENTUM_SUMMARY.md:32, percentage) - **GPT-4o** is extremely susceptible to momentum. A single prior revision round pushes it from 31% to 98% revision rate on the evaluative probe. It treats the conversational frame ("we're revising") 
- `4` (MOMENTUM_SUMMARY.md:33, percentage) - **Claude Sonnet 4** resists momentum and actually *declines* with more doses (38% to 25%). It appears to treat prior revisions as evidence that the output is already refined.
- `38` (MOMENTUM_SUMMARY.md:33, percentage) - **Claude Sonnet 4** resists momentum and actually *declines* with more doses (38% to 25%). It appears to treat prior revisions as evidence that the output is already refined.
- `25` (MOMENTUM_SUMMARY.md:33, percentage) - **Claude Sonnet 4** resists momentum and actually *declines* with more doses (38% to 25%). It appears to treat prior revisions as evidence that the output is already refined.
- `2.5` (MOMENTUM_SUMMARY.md:34, percentage) - **Gemini 2.5 Flash** barely revises under any condition (0.3-13%). Momentum has a small effect (dose 0 to 1) but it plateaus at a low level.
- `0.3` (MOMENTUM_SUMMARY.md:34, percentage) - **Gemini 2.5 Flash** barely revises under any condition (0.3-13%). Momentum has a small effect (dose 0 to 1) but it plateaus at a low level.
- `13` (MOMENTUM_SUMMARY.md:34, percentage) - **Gemini 2.5 Flash** barely revises under any condition (0.3-13%). Momentum has a small effect (dose 0 to 1) but it plateaus at a low level.
- `0` (MOMENTUM_SUMMARY.md:34, percentage) - **Gemini 2.5 Flash** barely revises under any condition (0.3-13%). Momentum has a small effect (dose 0 to 1) but it plateaus at a low level.
- `1` (MOMENTUM_SUMMARY.md:34, percentage) - **Gemini 2.5 Flash** barely revises under any condition (0.3-13%). Momentum has a small effect (dose 0 to 1) but it plateaus at a low level.

### [MOMENTUM_SUMMARY.md] Key Results -- RQ5: Dose-response

- `0.199` (MOMENTUM_SUMMARY.md:38, p-value) Spearman rho = 0.199, p < 0.0001. Significant but modest because the effect is a **step function, not a gradient** -- the entire shift happens between dose 0 and dose 1. Additional doses add nothing.
- `0.0001` (MOMENTUM_SUMMARY.md:38, p-value) Spearman rho = 0.199, p < 0.0001. Significant but modest because the effect is a **step function, not a gradient** -- the entire shift happens between dose 0 and dose 1. Additional doses add nothing.
- `0` (MOMENTUM_SUMMARY.md:38, p-value) Spearman rho = 0.199, p < 0.0001. Significant but modest because the effect is a **step function, not a gradient** -- the entire shift happens between dose 0 and dose 1. Additional doses add nothing.
- `1` (MOMENTUM_SUMMARY.md:38, p-value) Spearman rho = 0.199, p < 0.0001. Significant but modest because the effect is a **step function, not a gradient** -- the entire shift happens between dose 0 and dose 1. Additional doses add nothing.
- `0` (MOMENTUM_SUMMARY.md:41, percentage) - Dose 0: 3.0%
- `3.0` (MOMENTUM_SUMMARY.md:41, percentage) - Dose 0: 3.0%
- `1` (MOMENTUM_SUMMARY.md:42, percentage) - Dose 1: 22.1%
- `22.1` (MOMENTUM_SUMMARY.md:42, percentage) - Dose 1: 22.1%
- `2` (MOMENTUM_SUMMARY.md:43, percentage) - Dose 2: 26.2%
- `26.2` (MOMENTUM_SUMMARY.md:43, percentage) - Dose 2: 26.2%
- `3` (MOMENTUM_SUMMARY.md:44, percentage) - Dose 3: 24.0%
- `24.0` (MOMENTUM_SUMMARY.md:44, percentage) - Dose 3: 24.0%

### [MOMENTUM_SUMMARY.md] Key Results -- RQ6: Does the threshold interact with momentum?

- `0.28` (MOMENTUM_SUMMARY.md:48, p-value) **No.** Logistic regression: dose is significant (beta = 0.28, p < 0.0001), but threshold (p = 0.39) and the dose x threshold interaction (p = 0.51) are not. Momentum is threshold-blind, just like the
- `0.0001` (MOMENTUM_SUMMARY.md:48, p-value) **No.** Logistic regression: dose is significant (beta = 0.28, p < 0.0001), but threshold (p = 0.39) and the dose x threshold interaction (p = 0.51) are not. Momentum is threshold-blind, just like the
- `0.39` (MOMENTUM_SUMMARY.md:48, p-value) **No.** Logistic regression: dose is significant (beta = 0.28, p < 0.0001), but threshold (p = 0.39) and the dose x threshold interaction (p = 0.51) are not. Momentum is threshold-blind, just like the
- `0.51` (MOMENTUM_SUMMARY.md:48, p-value) **No.** Logistic regression: dose is significant (beta = 0.28, p < 0.0001), but threshold (p = 0.39) and the dose x threshold interaction (p = 0.51) are not. Momentum is threshold-blind, just like the
- `1` (MOMENTUM_SUMMARY.md:48, p-value) **No.** Logistic regression: dose is significant (beta = 0.28, p < 0.0001), but threshold (p = 0.39) and the dose x threshold interaction (p = 0.51) are not. Momentum is threshold-blind, just like the

### [MOMENTUM_SUMMARY.md] Key Results -- Overcorrection under momentum

- `213.76` (MOMENTUM_SUMMARY.md:52, p-value) Kruskal-Wallis H = 213.76, p < 0.0001, but effect is small in practice:
- `0.0001` (MOMENTUM_SUMMARY.md:52, p-value) Kruskal-Wallis H = 213.76, p < 0.0001, but effect is small in practice:
- `0` (MOMENTUM_SUMMARY.md:53, count or denominator) - Dose 0 mean: 1.09 / 5
- `1.09` (MOMENTUM_SUMMARY.md:53, count or denominator) - Dose 0 mean: 1.09 / 5
- `5` (MOMENTUM_SUMMARY.md:53, count or denominator) - Dose 0 mean: 1.09 / 5
- `1` (MOMENTUM_SUMMARY.md:54, count or denominator) - Dose 1 mean: 1.25 / 5
- `1.25` (MOMENTUM_SUMMARY.md:54, count or denominator) - Dose 1 mean: 1.25 / 5
- `5` (MOMENTUM_SUMMARY.md:54, count or denominator) - Dose 1 mean: 1.25 / 5
- `2` (MOMENTUM_SUMMARY.md:55, count or denominator) - Dose 2 mean: 1.31 / 5
- `1.31` (MOMENTUM_SUMMARY.md:55, count or denominator) - Dose 2 mean: 1.31 / 5
- `5` (MOMENTUM_SUMMARY.md:55, count or denominator) - Dose 2 mean: 1.31 / 5
- `3` (MOMENTUM_SUMMARY.md:56, count or denominator) - Dose 3 mean: 1.33 / 5
- `1.33` (MOMENTUM_SUMMARY.md:56, count or denominator) - Dose 3 mean: 1.33 / 5
- `5` (MOMENTUM_SUMMARY.md:56, count or denominator) - Dose 3 mean: 1.33 / 5
- `1.0` (MOMENTUM_SUMMARY.md:58, mean or delta) Medians remain at 1.0 across all doses. Most trials show proportionate revision even under momentum.

### [MOMENTUM_SUMMARY.md] Interpretation

- `1` (MOMENTUM_SUMMARY.md:62, bare number) 1. **The revision gate is not fixed** -- it is modulated by conversational history, but in model-specific ways.
- `2` (MOMENTUM_SUMMARY.md:63, percentage) 2. **GPT-4o's sycophancy is context-dependent** -- it reads conversational history as implicit pressure. One round of "can this be improved?" is enough to flip its gate from ~30% to ~98%.
- `30` (MOMENTUM_SUMMARY.md:63, percentage) 2. **GPT-4o's sycophancy is context-dependent** -- it reads conversational history as implicit pressure. One round of "can this be improved?" is enough to flip its gate from ~30% to ~98%.
- `98` (MOMENTUM_SUMMARY.md:63, percentage) 2. **GPT-4o's sycophancy is context-dependent** -- it reads conversational history as implicit pressure. One round of "can this be improved?" is enough to flip its gate from ~30% to ~98%.
- `3` (MOMENTUM_SUMMARY.md:64, bare number) 3. **Claude's resistance suggests different alignment training** -- it treats prior revisions as evidence the work is done, not as pressure to keep going.
- `4` (MOMENTUM_SUMMARY.md:65, bare number) 4. **Gemini's near-zero baseline means momentum has nothing to amplify** -- the mechanism only operates on models that are already somewhat willing to revise.
- `5` (MOMENTUM_SUMMARY.md:66, p-value) 5. **Thresholds remain invisible to the gate** regardless of conversational context (p = 0.51 for interaction), reinforcing Study 1's central finding.
- `0.51` (MOMENTUM_SUMMARY.md:66, p-value) 5. **Thresholds remain invisible to the gate** regardless of conversational context (p = 0.51 for interaction), reinforcing Study 1's central finding.
- `1` (MOMENTUM_SUMMARY.md:66, p-value) 5. **Thresholds remain invisible to the gate** regardless of conversational context (p = 0.51 for interaction), reinforcing Study 1's central finding.

### [MOMENTUM_SUMMARY.md] Open questions / Next steps

- `1` (MOMENTUM_SUMMARY.md:77, bare number) 1. **Reverse momentum**: Does a prior round of "this looks great, no changes needed" suppress revision *below* the cold baseline? Would confirm the mechanism is about conversational framing, not just 
- `2` (MOMENTUM_SUMMARY.md:78, bare number) 2. **Qualitative analysis of GPT-4o momentum revisions**: Are the dose-1 revisions substantive or surface-level reshuffling?
- `1` (MOMENTUM_SUMMARY.md:78, bare number) 2. **Qualitative analysis of GPT-4o momentum revisions**: Are the dose-1 revisions substantive or surface-level reshuffling?
- `3` (MOMENTUM_SUMMARY.md:79, bare number) 3. **Cross-model prompt transplant**: Feed GPT-4o's momentum conversation histories to Claude/Gemini as few-shot context. Tests whether the effect is in the weights or the context.

### [PIPELINE.md] Current State (as of 2026-03-29)

- `2026` (PIPELINE.md:3, count or denominator) ## Current State (as of 2026-03-29)
- `03` (PIPELINE.md:3, count or denominator) ## Current State (as of 2026-03-29)
- `29` (PIPELINE.md:3, count or denominator) ## Current State (as of 2026-03-29)
- `400` (PIPELINE.md:7, count or denominator) | GPT-4o trials | **Done** (400/400) |
- `400` (PIPELINE.md:7, count or denominator) | GPT-4o trials | **Done** (400/400) |

### [PIPELINE.md] Phase 0: Data Collection Completion (BLOCKING)

- `0` (PIPELINE.md:13, bare number) ## Phase 0: Data Collection Completion (BLOCKING)
- `1` (PIPELINE.md:17, bare number) **Go/No-Go to Phase 1:**
- `1,200` (PIPELINE.md:18, bare number) - All 1,200 trials present in `trials.jsonl` with `status=success`
- `80` (PIPELINE.md:19, count or denominator) - Each of the 80 cells has exactly 5 runs per model (400/400/400)
- `5` (PIPELINE.md:19, count or denominator) - Each of the 80 cells has exactly 5 runs per model (400/400/400)
- `400` (PIPELINE.md:19, count or denominator) - Each of the 80 cells has exactly 5 runs per model (400/400/400)
- `400` (PIPELINE.md:19, count or denominator) - Each of the 80 cells has exactly 5 runs per model (400/400/400)
- `400` (PIPELINE.md:19, count or denominator) - Each of the 80 cells has exactly 5 runs per model (400/400/400)

### [PIPELINE.md] Phase 0.5: Literature Review + Response Length Analysis (parallel with Phase 0)

- `0.5` (PIPELINE.md:24, mean or delta) ## Phase 0.5: Literature Review + Response Length Analysis (parallel with Phase 0)
- `0` (PIPELINE.md:24, mean or delta) ## Phase 0.5: Literature Review + Response Length Analysis (parallel with Phase 0)
- `2024` (PIPELINE.md:30, bare number) - Key venues: ACL/EMNLP/NAACL 2024-2025, COLM, NeurIPS/ICML alignment workshops
- `2025` (PIPELINE.md:30, bare number) - Key venues: ACL/EMNLP/NAACL 2024-2025, COLM, NeurIPS/ICML alignment workshops

### [PIPELINE.md] Phase 1: Full Evaluation (LLM-as-Judge)

- `1` (PIPELINE.md:39, bare number) ## Phase 1: Full Evaluation (LLM-as-Judge)
- `0` (PIPELINE.md:41, bare number) **Prerequisite:** Phase 0 complete
- `1` (PIPELINE.md:44, bare number) 1. Run `evaluate.py` — primary judge (GPT-4o) on all 1,200 trials
- `1,200` (PIPELINE.md:44, bare number) 1. Run `evaluate.py` — primary judge (GPT-4o) on all 1,200 trials
- `2` (PIPELINE.md:45, percentage) 2. Run `evaluate.py --irr` — second judge (Claude Sonnet) on 15% sample (~180 trials)
- `15` (PIPELINE.md:45, percentage) 2. Run `evaluate.py --irr` — second judge (Claude Sonnet) on 15% sample (~180 trials)
- `180` (PIPELINE.md:45, percentage) 2. Run `evaluate.py --irr` — second judge (Claude Sonnet) on 15% sample (~180 trials)
- `2` (PIPELINE.md:47, bare number) **Go/No-Go to Phase 2:**
- `1` (PIPELINE.md:48, percentage) 1. **Completion:** All 1,200 trials scored. Parse failures < 2%.
- `1,200` (PIPELINE.md:48, percentage) 1. **Completion:** All 1,200 trials scored. Parse failures < 2%.
- `2` (PIPELINE.md:48, percentage) 1. **Completion:** All 1,200 trials scored. Parse failures < 2%.
- `2` (PIPELINE.md:49, reliability or effect size) 2. **IRR:** Quadratic weighted kappa >= 0.60 on ALL four dimensions
- `0.60` (PIPELINE.md:49, reliability or effect size) 2. **IRR:** Quadratic weighted kappa >= 0.60 on ALL four dimensions
- `0.40` (PIPELINE.md:50, mean or delta) - 0.40-0.60: Flag in limitations, proceed with caution
- `0.60` (PIPELINE.md:50, mean or delta) - 0.40-0.60: Flag in limitations, proceed with caution
- `0.40` (PIPELINE.md:51, mean or delta) - Below 0.40: **STOP.** Revise rubric, re-run evaluation.
- `3` (PIPELINE.md:52, bare number) 3. **Sanity check:** Baseline (threshold=0) shows lower overcorrection than threshold=100
- `0` (PIPELINE.md:52, bare number) 3. **Sanity check:** Baseline (threshold=0) shows lower overcorrection than threshold=100
- `100` (PIPELINE.md:52, bare number) 3. **Sanity check:** Baseline (threshold=0) shows lower overcorrection than threshold=100

### [PIPELINE.md] Phase 2: Analysis + Visualization

- `2` (PIPELINE.md:56, bare number) ## Phase 2: Analysis + Visualization
- `1` (PIPELINE.md:58, bare number) **Prerequisite:** Phase 1 passes
- `1` (PIPELINE.md:61, bare number) 1. `analyze.py` — all statistical tests
- `2` (PIPELINE.md:62, bare number) 2. `visualize.py` — generate all 6 figures
- `6` (PIPELINE.md:62, bare number) 2. `visualize.py` — generate all 6 figures
- `3` (PIPELINE.md:63, bare number) 3. Manual review
- `3` (PIPELINE.md:65, bare number) **Go/No-Go to Phase 3:**
- `1` (PIPELINE.md:66, bare number) 1. **Signal exists:** At least ONE of:
- `0.05` (PIPELINE.md:67, p-value) - Kruskal-Wallis significant (p < 0.05) for overcorrection across thresholds
- `2` (PIPELINE.md:70, mean or delta) 2. **Effect sizes reportable:** At least one comparison with rank-biserial r >= 0.20
- `0.20` (PIPELINE.md:70, mean or delta) 2. **Effect sizes reportable:** At least one comparison with rank-biserial r >= 0.20
- `3` (PIPELINE.md:71, percentage) 3. **No artifacts:** No floor/ceiling effects. revision_gate is not 100% "full_revision"
- `100` (PIPELINE.md:71, percentage) 3. **No artifacts:** No floor/ceiling effects. revision_gate is not 100% "full_revision"
- `3` (PIPELINE.md:73, bare number) **If signal is weak:** Skip Phase 3, go to Phase 4 with null-result framing.
- `4` (PIPELINE.md:73, bare number) **If signal is weak:** Skip Phase 3, go to Phase 4 with null-result framing.

### [PIPELINE.md] Phase 3: Deep Statistical Exploration (5 Agents, parallel)

- `3` (PIPELINE.md:77, bare number) ## Phase 3: Deep Statistical Exploration (5 Agents, parallel)
- `5` (PIPELINE.md:77, bare number) ## Phase 3: Deep Statistical Exploration (5 Agents, parallel)
- `1` (PIPELINE.md:79, bare number) 1. **Model comparison** — between-model overcorrection differences
- `2` (PIPELINE.md:80, bare number) 2. **Framing effect** — numeric vs. qualitative systematic differences
- `3` (PIPELINE.md:81, bare number) 3. **Threshold dose-response** — monotonicity, inflection points
- `4` (PIPELINE.md:82, bare number) 4. **Scenario sensitivity** — which writing tasks provoke more overcorrection
- `5` (PIPELINE.md:83, bare number) 5. **Interaction effects** — model×framing, model×scenario, framing×threshold
- `4` (PIPELINE.md:85, bare number) **Go/No-Go to Phase 4:**
- `3` (PIPELINE.md:86, count or denominator) - At least 3/5 agents produce significant + interpretable findings
- `5` (PIPELINE.md:86, count or denominator) - At least 3/5 agents produce significant + interpretable findings

### [PIPELINE.md] Phase 4: Adversarial Q&A + Sufficiency Audit

- `4` (PIPELINE.md:91, bare number) ## Phase 4: Adversarial Q&A + Sufficiency Audit
- `1` (PIPELINE.md:93, bare number) **Step 1: Adversarial Q&A**
- `2` (PIPELINE.md:97, bare number) **Step 2: Sufficiency Audit**
- `3` (PIPELINE.md:101, bare number) **Step 3: Human eval feasibility** (15-min decision point)
- `15` (PIPELINE.md:101, bare number) **Step 3: Human eval feasibility** (15-min decision point)
- `5` (PIPELINE.md:103, bare number) **Go/No-Go to Phase 5:**
- `80` (PIPELINE.md:105, percentage) - Checklist >= 80% green

### [PIPELINE.md] Phase 5: Paper Writing

- `5` (PIPELINE.md:110, bare number) ## Phase 5: Paper Writing
- `1` (PIPELINE.md:112, bare number) **Step 1 (parallel):** Paper outline + example curation
- `2` (PIPELINE.md:113, bare number) **Step 2 (sequential):** Methods → Results → Introduction → Discussion → Limitations → Abstract → Related Work
- `3` (PIPELINE.md:114, bare number) **Step 3:** Publication-quality figures (camera-ready, color-blind-safe)

### [PIPELINE.md] Phase 6: Venue Selection + Final Polish

- `6` (PIPELINE.md:118, bare number) ## Phase 6: Venue Selection + Final Polish
- `0.3` (PIPELINE.md:121, mean or delta) - Strong effects (multiple significant, r >= 0.3): Main conference (EMNLP, ACL, NAACL)

### [PIPELINE.md] Critical Risk Register

- `0.40` (PIPELINE.md:133, reliability or effect size) | IRR kappa < 0.40 | Medium | **Fatal** | Revise rubric, re-run |
- `1` (PIPELINE.md:135, bare number) | Gemini Flash stalls | Medium | Lose 1 model | Publish with 2; note limitation |
- `2` (PIPELINE.md:135, bare number) | Gemini Flash stalls | Medium | Lose 1 model | Publish with 2; note limitation |
- `5` (PIPELINE.md:136, percentage) | Judge parse failure > 5% | Low | Reduced N | Retry logic exists; add structured output |

### [PIPELINE.md] Timeline

- `0` (PIPELINE.md:145, bare number) | 0: Data collection | 1-3 days | Day 1-3 |
- `1` (PIPELINE.md:145, bare number) | 0: Data collection | 1-3 days | Day 1-3 |
- `3` (PIPELINE.md:145, bare number) | 0: Data collection | 1-3 days | Day 1-3 |
- `1` (PIPELINE.md:145, bare number) | 0: Data collection | 1-3 days | Day 1-3 |
- `3` (PIPELINE.md:145, bare number) | 0: Data collection | 1-3 days | Day 1-3 |
- `0.5` (PIPELINE.md:146, mean or delta) | 0.5: Lit review + length | 4-8 hrs (parallel) | Day 1-3 |
- `4` (PIPELINE.md:146, mean or delta) | 0.5: Lit review + length | 4-8 hrs (parallel) | Day 1-3 |
- `8` (PIPELINE.md:146, mean or delta) | 0.5: Lit review + length | 4-8 hrs (parallel) | Day 1-3 |
- `1` (PIPELINE.md:146, mean or delta) | 0.5: Lit review + length | 4-8 hrs (parallel) | Day 1-3 |
- `3` (PIPELINE.md:146, mean or delta) | 0.5: Lit review + length | 4-8 hrs (parallel) | Day 1-3 |
- `1` (PIPELINE.md:147, bare number) | 1: Evaluation | 3-5 hrs | Day 3-4 |
- `3` (PIPELINE.md:147, bare number) | 1: Evaluation | 3-5 hrs | Day 3-4 |
- `5` (PIPELINE.md:147, bare number) | 1: Evaluation | 3-5 hrs | Day 3-4 |
- `3` (PIPELINE.md:147, bare number) | 1: Evaluation | 3-5 hrs | Day 3-4 |
- `4` (PIPELINE.md:147, bare number) | 1: Evaluation | 3-5 hrs | Day 3-4 |
- `2` (PIPELINE.md:148, bare number) | 2: Analysis + viz | 2-3 hrs | Day 4 |
- `2` (PIPELINE.md:148, bare number) | 2: Analysis + viz | 2-3 hrs | Day 4 |
- `3` (PIPELINE.md:148, bare number) | 2: Analysis + viz | 2-3 hrs | Day 4 |
- `4` (PIPELINE.md:148, bare number) | 2: Analysis + viz | 2-3 hrs | Day 4 |
- `3` (PIPELINE.md:149, bare number) | 3: Deep stats | 2-4 hrs | Day 4-5 |
- `2` (PIPELINE.md:149, bare number) | 3: Deep stats | 2-4 hrs | Day 4-5 |
- `4` (PIPELINE.md:149, bare number) | 3: Deep stats | 2-4 hrs | Day 4-5 |
- `4` (PIPELINE.md:149, bare number) | 3: Deep stats | 2-4 hrs | Day 4-5 |
- `5` (PIPELINE.md:149, bare number) | 3: Deep stats | 2-4 hrs | Day 4-5 |
- `4` (PIPELINE.md:150, bare number) | 4: Adversarial + audit | 3-4 hrs | Day 5 |
- `3` (PIPELINE.md:150, bare number) | 4: Adversarial + audit | 3-4 hrs | Day 5 |
- `4` (PIPELINE.md:150, bare number) | 4: Adversarial + audit | 3-4 hrs | Day 5 |
- `5` (PIPELINE.md:150, bare number) | 4: Adversarial + audit | 3-4 hrs | Day 5 |
- `5` (PIPELINE.md:151, bare number) | 5: Paper writing | 8-12 hrs | Day 5-8 |
- `8` (PIPELINE.md:151, bare number) | 5: Paper writing | 8-12 hrs | Day 5-8 |
- `12` (PIPELINE.md:151, bare number) | 5: Paper writing | 8-12 hrs | Day 5-8 |
- `5` (PIPELINE.md:151, bare number) | 5: Paper writing | 8-12 hrs | Day 5-8 |
- `8` (PIPELINE.md:151, bare number) | 5: Paper writing | 8-12 hrs | Day 5-8 |
- `6` (PIPELINE.md:152, bare number) | 6: Venue + polish | 3-4 hrs | Day 8-9 |
- `3` (PIPELINE.md:152, bare number) | 6: Venue + polish | 3-4 hrs | Day 8-9 |
- `4` (PIPELINE.md:152, bare number) | 6: Venue + polish | 3-4 hrs | Day 8-9 |
- `8` (PIPELINE.md:152, bare number) | 6: Venue + polish | 3-4 hrs | Day 8-9 |
- `9` (PIPELINE.md:152, bare number) | 6: Venue + polish | 3-4 hrs | Day 8-9 |
- `9` (PIPELINE.md:154, bare number) **Total: ~9 working days**
