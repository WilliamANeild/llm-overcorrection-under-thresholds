# Number extract

Written by `paper/extract_numbers.py`. Sections read: sections/abstract_v2.tex, sections/introduction_v2.tex, sections/related_work_v2.tex, sections/methods.tex, sections/results_v2.tex, sections/discussion.tex, sections/conclusion.tex, sections/limitations.tex, sections/appendix.tex, sections/_fig1_appendix.tex.

- 764 numerals in the paper, of which 264 are structural (turn indices, scale levels, cross-references, citation years, typesetting dimensions) and set aside.
- 500 evidential numerals remain.
- 1805 numerals across `results_FINAL.md`, `MOMENTUM_SUMMARY.md`, `PIPELINE.md`.
- 79 paper values do not appear anywhere in the ledger as a literal string. That is a starting point, not a finding: a paper may state 87.6% where the ledger states 631/720, and a rounded value will not match.

## Paper values with no literal match in the ledger

| value | where | kind | float? | context |
|---|---|---|---|---|
| `88` | sections/abstract_v2.tex:34 | percentage |  | ss 5 domains, contrasting undirected requests with a single targeted critique. First drafts are sufficient in 88\% of trials, and most replies contain |
| `840` | sections/appendix.tex:112 | mean or delta | yes | l=gray!10] (crossing) { Fully factorial: $8 \times 16 \times 2 \times 3 \times 5$ runs $= \mathbf{3{,}840}$ primary trials }; \draw[arr] (scenarios.so |
| `0.2` | sections/appendix.tex:115 | mean or delta | yes | \times 3 \times 5$ runs $= \mathbf{3{,}840}$ primary trials }; \draw[arr] (scenarios.south) -- ++(0,-0.2) -| (crossing.north -| scenarios); \draw[arr] |
| `3.47` | sections/appendix.tex:18 | mean or delta | yes | oprule \textbf{Predictor} & \textbf{Model A} & \textbf{Model B} & \textbf{Model C} \\ \midrule is\_leading & $3.47^{***}$ & $3.94^{***}$ & --- \\ thre |
| `3.94` | sections/appendix.tex:18 | mean or delta | yes | Predictor} & \textbf{Model A} & \textbf{Model B} & \textbf{Model C} \\ \midrule is\_leading & $3.47^{***}$ & $3.94^{***}$ & --- \\ threshold & $-0.93^ |
| `4935` | sections/appendix.tex:188 | mean or delta | yes | mparison} & \textbf{$U$} & \textbf{$p_{\text{adj}}$} & \textbf{$r$} \\ \midrule Gemini (num.) & 70 vs.\ 100 & 4935 & $<$0.001 & $-$0.42 \\ Gemini (num |
| `0.42` | sections/appendix.tex:188 | mean or delta | yes | U$} & \textbf{$p_{\text{adj}}$} & \textbf{$r$} \\ \midrule Gemini (num.) & 70 vs.\ 100 & 4935 & $<$0.001 & $-$0.42 \\ Gemini (num.) & 85 vs.\ 100 & 42 |
| `4238` | sections/appendix.tex:189 | mean or delta | yes | tbf{$r$} \\ \midrule Gemini (num.) & 70 vs.\ 100 & 4935 & $<$0.001 & $-$0.42 \\ Gemini (num.) & 85 vs.\ 100 & 4238 & $<$0.001 & $-$0.32 \\ Gemini (num |
| `0.32` | sections/appendix.tex:189 | mean or delta | yes | Gemini (num.) & 70 vs.\ 100 & 4935 & $<$0.001 & $-$0.42 \\ Gemini (num.) & 85 vs.\ 100 & 4238 & $<$0.001 & $-$0.32 \\ Gemini (num.) & 0 vs.\ 100 & 475 |
| `0.93` | sections/appendix.tex:19 | mean or delta | yes | xtbf{Model B} & \textbf{Model C} \\ \midrule is\_leading & $3.47^{***}$ & $3.94^{***}$ & --- \\ threshold & $-0.93^{***}$ & $-1.04^{***}$ & $-1.65^{** |
| `1.65` | sections/appendix.tex:19 | mean or delta | yes | \\ \midrule is\_leading & $3.47^{***}$ & $3.94^{***}$ & --- \\ threshold & $-0.93^{***}$ & $-1.04^{***}$ & $-1.65^{***}$ \\ is\_qualitative & $-0.74^{ |
| `4755` | sections/appendix.tex:190 | mean or delta | yes | $<$0.001 & $-$0.42 \\ Gemini (num.) & 85 vs.\ 100 & 4238 & $<$0.001 & $-$0.32 \\ Gemini (num.) & 0 vs.\ 100 & 4755 & 0.002 & $-$0.25 \\ Gemini (qual.) |
| `4084` | sections/appendix.tex:191 | mean or delta | yes | & $<$0.001 & $-$0.32 \\ Gemini (num.) & 0 vs.\ 100 & 4755 & 0.002 & $-$0.25 \\ Gemini (qual.) & 0 vs.\ 100 & 4084 & 0.002 & $-$0.28 \\ Claude (num.) & |
| `4146` | sections/appendix.tex:192 | mean or delta | yes | 55 & 0.002 & $-$0.25 \\ Gemini (qual.) & 0 vs.\ 100 & 4084 & 0.002 & $-$0.28 \\ Claude (num.) & 85 vs.\ 100 & 4146 & $<$0.001 & $-$0.30 \\ Claude (qua |
| `3880` | sections/appendix.tex:193 | mean or delta | yes | 0.002 & $-$0.28 \\ Claude (num.) & 85 vs.\ 100 & 4146 & $<$0.001 & $-$0.30 \\ Claude (qual.) & 85 vs.\ 100 & 3880 & 0.024 & $-$0.21 \\ \bottomrule \en |
| `0.85` | sections/appendix.tex:20 | mean or delta | yes | *}$ & --- \\ threshold & $-0.93^{***}$ & $-1.04^{***}$ & $-1.65^{***}$ \\ is\_qualitative & $-0.74^{***}$ & $-0.85^{***}$ & $-1.05^{***}$ \\ Claude So |
| `920` | sections/appendix.tex:204 | percentage |  | t-hoc power analysis at $\alpha = 0.05$, 80\% power: \begin{itemize} \item \textbf{Study~1 RQ1} ($N = 1{,}920$ per probe): MDE for proportion differen |
| `0.032` | sections/appendix.tex:204 | count or denominator |  | r: \begin{itemize} \item \textbf{Study~1 RQ1} ($N = 1{,}920$ per probe): MDE for proportion difference $= 0.032$. Observed $\approx 0.75$. Massively o |
| `0.75` | sections/appendix.tex:204 | count or denominator |  | em \textbf{Study~1 RQ1} ($N = 1{,}920$ per probe): MDE for proportion difference $= 0.032$. Observed $\approx 0.75$. Massively overpowered. \item \tex |
| `920` | sections/appendix.tex:205 | count or denominator |  | ifference $= 0.032$. Observed $\approx 0.75$. Massively overpowered. \item \textbf{Study~1 RQ2} ($N = 1{,}920$ leading-probe): MDE for $|\rho| = 0.064 |
| `0.064` | sections/appendix.tex:205 | count or denominator |  | 0.75$. Massively overpowered. \item \textbf{Study~1 RQ2} ($N = 1{,}920$ leading-probe): MDE for $|\rho| = 0.064$. All observed correlations exceed thi |
| `3.32` | sections/appendix.tex:206 | p-value |  | the paired test is the balanced panel ($n = 50$ trials with genuine revision at all turns), which yields $p = 3.32 \times 10^{-6}$ (Wilcoxon, $r = 0.6 |
| `0.33` | sections/appendix.tex:21 | mean or delta | yes | **}$ \\ is\_qualitative & $-0.74^{***}$ & $-0.85^{***}$ & $-1.05^{***}$ \\ Claude Sonnet & $0.10$ & $0.15$ & $0.33^{**}$ \\ Gemini Flash & $0.42^{***} |
| `0.42` | sections/appendix.tex:22 | mean or delta | yes | 74^{***}$ & $-0.85^{***}$ & $-1.05^{***}$ \\ Claude Sonnet & $0.10$ & $0.15$ & $0.33^{**}$ \\ Gemini Flash & $0.42^{***}$ & $0.52^{***}$ & $1.15^{***} |
| `0.52` | sections/appendix.tex:22 | mean or delta | yes | .85^{***}$ & $-1.05^{***}$ \\ Claude Sonnet & $0.10$ & $0.15$ & $0.33^{**}$ \\ Gemini Flash & $0.42^{***}$ & $0.52^{***}$ & $1.15^{***}$ \\ Scenario F |
| `0.340` | sections/appendix.tex:221 | reliability or effect size | yes | textbf{Spearman $r$} & \textbf{QW $\kappa$} \\ \midrule Claude Sonnet 4 & $0.505$ & $0.526$ \\ DeepSeek V4 & $0.340$ & $0.398$ \\ Qwen 3 235B & $0.272 |
| `0.398` | sections/appendix.tex:221 | reliability or effect size | yes | arman $r$} & \textbf{QW $\kappa$} \\ \midrule Claude Sonnet 4 & $0.505$ & $0.526$ \\ DeepSeek V4 & $0.340$ & $0.398$ \\ Qwen 3 235B & $0.272$ & $0.017 |
| `0.272` | sections/appendix.tex:222 | reliability or effect size | yes | \kappa$} \\ \midrule Claude Sonnet 4 & $0.505$ & $0.526$ \\ DeepSeek V4 & $0.340$ & $0.398$ \\ Qwen 3 235B & $0.272$ & $0.017$ \\ Llama 3.3 70B & $0.1 |
| `0.017` | sections/appendix.tex:222 | mean or delta | yes | \ \midrule Claude Sonnet 4 & $0.505$ & $0.526$ \\ DeepSeek V4 & $0.340$ & $0.398$ \\ Qwen 3 235B & $0.272$ & $0.017$ \\ Llama 3.3 70B & $0.181$ & $0.0 |
| `0.181` | sections/appendix.tex:223 | mean or delta | yes | & $0.505$ & $0.526$ \\ DeepSeek V4 & $0.340$ & $0.398$ \\ Qwen 3 235B & $0.272$ & $0.017$ \\ Llama 3.3 70B & $0.181$ & $0.022$ \\ GPT-4o & $0.140$ & $ |
| `0.022` | sections/appendix.tex:223 | mean or delta | yes | & $0.526$ \\ DeepSeek V4 & $0.340$ & $0.398$ \\ Qwen 3 235B & $0.272$ & $0.017$ \\ Llama 3.3 70B & $0.181$ & $0.022$ \\ GPT-4o & $0.140$ & $0.065$ \\  |
| `0.140` | sections/appendix.tex:224 | mean or delta | yes | k V4 & $0.340$ & $0.398$ \\ Qwen 3 235B & $0.272$ & $0.017$ \\ Llama 3.3 70B & $0.181$ & $0.022$ \\ GPT-4o & $0.140$ & $0.065$ \\ Gemini 2.5 Flash & $ |
| `0.065` | sections/appendix.tex:224 | mean or delta | yes | 340$ & $0.398$ \\ Qwen 3 235B & $0.272$ & $0.017$ \\ Llama 3.3 70B & $0.181$ & $0.022$ \\ GPT-4o & $0.140$ & $0.065$ \\ Gemini 2.5 Flash & $-0.036$ &  |
| `0.036` | sections/appendix.tex:225 | count or denominator | yes | $0.272$ & $0.017$ \\ Llama 3.3 70B & $0.181$ & $0.022$ \\ GPT-4o & $0.140$ & $0.065$ \\ Gemini 2.5 Flash & $-0.036$ & $-0.026$ \\ \bottomrule \end{tab |
| `0.026` | sections/appendix.tex:225 | reliability or effect size | yes | $0.017$ \\ Llama 3.3 70B & $0.181$ & $0.022$ \\ GPT-4o & $0.140$ & $0.065$ \\ Gemini 2.5 Flash & $-0.036$ & $-0.026$ \\ \bottomrule \end{tabular} \cap |
| `2.1` | sections/appendix.tex:228 | p-value | yes | elected as the Study~3 evaluator, with the highest human correlation of the six candidates ($r = 0.505$, $p = 2.1 \times 10^{-5}$). Gemini 2.5 Flash w |
| `5,319` | sections/appendix.tex:26 | mean or delta | yes | $0.52^{***}$ & $1.15^{***}$ \\ Scenario FEs & No & Yes & Yes \\ \midrule $N$ & 3,840 & 3,840 & 1,920 \\ AIC & 5,319 & 4,839 & 3,545 \\ \bottomrule \en |
| `4,839` | sections/appendix.tex:26 | mean or delta | yes | **}$ & $1.15^{***}$ \\ Scenario FEs & No & Yes & Yes \\ \midrule $N$ & 3,840 & 3,840 & 1,920 \\ AIC & 5,319 & 4,839 & 3,545 \\ \bottomrule \end{tabula |
| `3,545` | sections/appendix.tex:26 | mean or delta | yes | 1.15^{***}$ \\ Scenario FEs & No & Yes & Yes \\ \midrule $N$ & 3,840 & 3,840 & 1,920 \\ AIC & 5,319 & 4,839 & 3,545 \\ \bottomrule \end{tabular} \capt |
| `0.844` | sections/appendix.tex:264 | reliability or effect size | yes | \toprule \textbf{Dimension} & \textbf{QW $\kappa$} & \textbf{Interpretation} \\ \midrule Revision magnitude & 0.844 & Excellent \\ Revision value & 0. |
| `0.690` | sections/appendix.tex:265 | reliability or effect size | yes | QW $\kappa$} & \textbf{Interpretation} \\ \midrule Revision magnitude & 0.844 & Excellent \\ Revision value & 0.690 & Good \\ Overcorrection & 0.609 & |
| `0.609` | sections/appendix.tex:266 | mean or delta | yes | tion} \\ \midrule Revision magnitude & 0.844 & Excellent \\ Revision value & 0.690 & Good \\ Overcorrection & 0.609 & Acceptable \\ Threshold alignmen |
| `0.556` | sections/appendix.tex:267 | mean or delta | yes | & Excellent \\ Revision value & 0.690 & Good \\ Overcorrection & 0.609 & Acceptable \\ Threshold alignment & 0.556 & Marginal \\ \bottomrule \end{tabu |
| `60` | sections/appendix.tex:270 | count or denominator | yes | \\ \bottomrule \end{tabular} \caption{Inter-rater reliability for Study~1 (GPT-4o vs.\ Claude Sonnet~4, $n = 60$).} \label{tab:irr} \end{table} \begin |
| `0.575` | sections/appendix.tex:281 | percentage | yes | Dimension} & \textbf{QW $\kappa$} & \textbf{\% Agree} & \textbf{\% Within 1} \\ \midrule Revision magnitude & 0.575 & 68.3 & 85.0 \\ Revision value &  |
| `68.3` | sections/appendix.tex:281 | percentage | yes | n} & \textbf{QW $\kappa$} & \textbf{\% Agree} & \textbf{\% Within 1} \\ \midrule Revision magnitude & 0.575 & 68.3 & 85.0 \\ Revision value & 0.669 &  |
| `85.0` | sections/appendix.tex:281 | percentage | yes | extbf{QW $\kappa$} & \textbf{\% Agree} & \textbf{\% Within 1} \\ \midrule Revision magnitude & 0.575 & 68.3 & 85.0 \\ Revision value & 0.669 & 76.7 &  |
| `0.669` | sections/appendix.tex:282 | percentage | yes | tbf{\% Agree} & \textbf{\% Within 1} \\ \midrule Revision magnitude & 0.575 & 68.3 & 85.0 \\ Revision value & 0.669 & 76.7 & 88.3 \\ Overcorrection &  |
| `76.7` | sections/appendix.tex:282 | percentage | yes | gree} & \textbf{\% Within 1} \\ \midrule Revision magnitude & 0.575 & 68.3 & 85.0 \\ Revision value & 0.669 & 76.7 & 88.3 \\ Overcorrection & 0.392 &  |
| `88.3` | sections/appendix.tex:282 | percentage | yes | \textbf{\% Within 1} \\ \midrule Revision magnitude & 0.575 & 68.3 & 85.0 \\ Revision value & 0.669 & 76.7 & 88.3 \\ Overcorrection & 0.392 & 71.7 & 9 |
| `0.392` | sections/appendix.tex:283 | mean or delta | yes | \midrule Revision magnitude & 0.575 & 68.3 & 85.0 \\ Revision value & 0.669 & 76.7 & 88.3 \\ Overcorrection & 0.392 & 71.7 & 90.0 \\ Threshold alignme |
| `71.7` | sections/appendix.tex:283 | mean or delta | yes | Revision magnitude & 0.575 & 68.3 & 85.0 \\ Revision value & 0.669 & 76.7 & 88.3 \\ Overcorrection & 0.392 & 71.7 & 90.0 \\ Threshold alignment & 0.33 |
| `90.0` | sections/appendix.tex:283 | mean or delta | yes | on magnitude & 0.575 & 68.3 & 85.0 \\ Revision value & 0.669 & 76.7 & 88.3 \\ Overcorrection & 0.392 & 71.7 & 90.0 \\ Threshold alignment & 0.339 & 38 |
| `0.339` | sections/appendix.tex:284 | count or denominator | yes | 85.0 \\ Revision value & 0.669 & 76.7 & 88.3 \\ Overcorrection & 0.392 & 71.7 & 90.0 \\ Threshold alignment & 0.339 & 38.3 & 85.0 \\ \bottomrule \end{ |
| `38.3` | sections/appendix.tex:284 | count or denominator | yes | Revision value & 0.669 & 76.7 & 88.3 \\ Overcorrection & 0.392 & 71.7 & 90.0 \\ Threshold alignment & 0.339 & 38.3 & 85.0 \\ \bottomrule \end{tabular} |
| `85.0` | sections/appendix.tex:284 | count or denominator | yes | n value & 0.669 & 76.7 & 88.3 \\ Overcorrection & 0.392 & 71.7 & 90.0 \\ Threshold alignment & 0.339 & 38.3 & 85.0 \\ \bottomrule \end{tabular} \capti |
| `60` | sections/appendix.tex:287 | count or denominator | yes | ignment & 0.339 & 38.3 & 85.0 \\ \bottomrule \end{tabular} \caption{Inter-rater reliability for Study~2 ($n = 60$).} \label{tab:irr-momentum} \end{tab |
| `0.01` | sections/appendix.tex:29 | p-value | yes | tabular} \caption{Ordinal regression (overcorrection $\sim$ predictors). Model C: leading-probe only. $^{**}p<0.01$, $^{***}p<0.001$. Reference: GPT-4 |
| `0.006` | sections/appendix.tex:308 | mean or delta | yes | 4 & 196 & 58.5 & 0.11 \\ Qwen 3 235B & 90 & 74.5 & $<0.001$ \\ GPT-4o & 40 & 80.0 & 0.006 \\ DeepSeek-V4 & 31 & 85.7 & 0.007 \\ Gemini 2.5 Flash & 8 & |
| `0.007` | sections/appendix.tex:309 | mean or delta | yes | & 90 & 74.5 & $<0.001$ \\ GPT-4o & 40 & 80.0 & 0.006 \\ DeepSeek-V4 & 31 & 85.7 & 0.007 \\ Gemini 2.5 Flash & 8 & 100.0 & 0.062 \\ \midrule \multicolu |
| `920` | sections/appendix.tex:34 | percentage |  | be improved?'' and ``Is there anything you would change?'') trigger near-universal revision (99.9\%, $n = 1{,}920$; 100\%, $n = 18$). The three probes |
| `920` | sections/appendix.tex:34 | percentage |  | bar?,'' and ``What do you think?'') produce single-digit to low-double-digit revision rates (23.2\%, $n = 1{,}920$; 12.5\%, $n = 24$; 2.0\%, $n = 50$) |
| `0.058` | sections/appendix.tex:362 | p-value | yes | ipped content. All domains show negative deltas; 4/5 are significant ($p < 0.05$), data\_logic marginal ($p = 0.058$). Per-domain $n$(T5) limits preci |
| `99.7` | sections/appendix.tex:4 | percentage |  | Take another look and let me know if it's ready''), revision rates varied by model: Gemini~2.5 Flash declined 99.7\%, GPT-4o 68.6\%, Claude Sonnet~4 6 |
| `68.6` | sections/appendix.tex:4 | percentage |  | ok and let me know if it's ready''), revision rates varied by model: Gemini~2.5 Flash declined 99.7\%, GPT-4o 68.6\%, Claude Sonnet~4 62.0\%. Chi-squa |
| `21.9` | sections/appendix.tex:54 | percentage |  | changes needed'') suppresses full revision to near-zero across all models: Gemini 0.0\%, GPT-4o 1.0\%, Claude 21.9\% (all minor suggestions). The gate |
| `788` | sections/appendix.tex:6 | p-value |  | 0\%. Chi-squared tests confirm the revision gate distribution differs significantly by probe type ($\chi^2 > 788$, $p < 0.0001$ for all models). Quali |
| `0.14` | sections/appendix.tex:8 | reliability or effect size |  | thresholds produce moderately less overcorrection (Spearman $\rho$: Gemini $-0.50$, Claude $-0.35$, GPT-4o $-0.14$), but this calibration is locked be |
| `62` | sections/discussion.tex:12 | percentage |  | und. The first is wasted generation: the quality-optimal stopping point is the first turn for every model, so 62\% of output tokens fall past it. The  |
| `88` | sections/introduction_v2.tex:76 | percentage |  | ns and validate every quality judgment against human raters. Most of the work being revised did not need it: 88\% of the 720 first drafts are already  |
| `86.7` | sections/introduction_v2.tex:78 | percentage |  | already sufficient. Asked to improve them without direction, models mostly do not revise: by the fifth turn, 86.7\% of replies are meta-responses, res |
| `71.9` | sections/results_v2.tex:101 | count or denominator |  | stant, model identity explains far more variation in genuine-revision rate than task domain: a model range of 71.9 percentage points against a domain  |
| `13.5` | sections/results_v2.tex:102 | reliability or effect size |  | in genuine-revision rate than task domain: a model range of 71.9 percentage points against a domain range of 13.5. All five domains show negative stri |
| `9.2` | sections/results_v2.tex:150 | p-value | yes | c} \toprule Model & $n$ & Stripped $\Delta$ & $p$ \\ \midrule Llama 3.3 70B & 71 & $+1.62$ & $9.2 \times 10^{-12}$ \\ Qwen 3 235B & 21 & $+1.48$ & $4. |
| `7.8` | sections/results_v2.tex:152 | p-value | yes | 9.2 \times 10^{-12}$ \\ Qwen 3 235B & 21 & $+1.48$ & $4.5 \times 10^{-4}$ \\ GPT-4o & 12 & $+1.33$ & $7.8 \times 10^{-3}$ \\ DeepSeek V4 & 19 & $+1.05 |
| `1.2` | sections/results_v2.tex:153 | p-value | yes | $4.5 \times 10^{-4}$ \\ GPT-4o & 12 & $+1.33$ & $7.8 \times 10^{-3}$ \\ DeepSeek V4 & 19 & $+1.05$ & $1.2 \times 10^{-2}$ \\ Claude Sonnet 4 & 51 & $+ |
| `1.2` | sections/results_v2.tex:154 | p-value | yes | es 10^{-3}$ \\ DeepSeek V4 & 19 & $+1.05$ & $1.2 \times 10^{-2}$ \\ Claude Sonnet 4 & 51 & $+0.31$ & $1.2 \times 10^{-2}$ \\ Gemini 2.5 Flash & 3 & $+ |
| `1.7` | sections/results_v2.tex:65 | p-value |  | .5~Flash contributes only eight genuine revisions. Unstripped, the same share is 76.6\% (245 against 75, $p = 1.7 \times 10^{-22}$). \paragraph{The ef |
| `3.76` | sections/results_v2.tex:80 | p-value |  | he only model with power to detect a within-model cliff; its stripped cliff of $-0.69$ is significant at $p = 3.76 \times 10^{-4}$. GPT-4o, DeepSeek a |

## Every evidential value in the paper

| value | where | kind | float? | context |
|---|---|---|---|---|
| `6` | sections/abstract_v2.tex:32 | bare number |  | ned the work that is already sufficient and gets revised anyway. We run five-turn revision conversations with 6 models on 40 tasks across 5 domains, c |
| `40` | sections/abstract_v2.tex:32 | bare number |  | that is already sufficient and gets revised anyway. We run five-turn revision conversations with 6 models on 40 tasks across 5 domains, contrasting un |
| `5` | sections/abstract_v2.tex:32 | percentage |  | sufficient and gets revised anyway. We run five-turn revision conversations with 6 models on 40 tasks across 5 domains, contrasting undirected request |
| `88` | sections/abstract_v2.tex:34 | percentage |  | ss 5 domains, contrasting undirected requests with a single targeted critique. First drafts are sufficient in 88\% of trials, and most replies contain |
| `70` | sections/abstract_v2.tex:36 | percentage |  | stating the draft or declining while presenting it as compliance. Revisions that change quality make it worse 70\% of the time, and where the work was |
| `27` | sections/abstract_v2.tex:36 | percentage |  | nce. Revisions that change quality make it worse 70\% of the time, and where the work was already sufficient, 27\% of them leave it insufficient. For  |
| `1` | sections/appendix.tex:1 | bare number |  | \section{Study 1: The Revision Gate} \label{sec:appendix-study1} Study~1 tests whether user-stated quality thresholds constra |
| `3` | sections/appendix.tex:112 | mean or delta | yes | fill=gray!10] (crossing) { Fully factorial: $8 \times 16 \times 2 \times 3 \times 5$ runs $= \mathbf{3{,}840}$ primary trials }; \draw[arr] (scenarios |
| `840` | sections/appendix.tex:112 | mean or delta | yes | l=gray!10] (crossing) { Fully factorial: $8 \times 16 \times 2 \times 3 \times 5$ runs $= \mathbf{3{,}840}$ primary trials }; \draw[arr] (scenarios.so |
| `0` | sections/appendix.tex:115 | mean or delta | yes | 2 \times 3 \times 5$ runs $= \mathbf{3{,}840}$ primary trials }; \draw[arr] (scenarios.south) -- ++(0,-0.2) -| (crossing.north -| scenarios); \draw[ar |
| `0.2` | sections/appendix.tex:115 | mean or delta | yes | \times 3 \times 5$ runs $= \mathbf{3{,}840}$ primary trials }; \draw[arr] (scenarios.south) -- ++(0,-0.2) -| (crossing.north -| scenarios); \draw[arr] |
| `1` | sections/appendix.tex:138 | bare number | yes | Judge} (GPT-4o, $T{=}0$) }; \draw[arr] (turn2) -- (judge); \end{tikzpicture} \caption{Study~1 experimental pipeline. Four factors crossed in a fully f |
| `3,840` | sections/appendix.tex:138 | bare number | yes | picture} \caption{Study~1 experimental pipeline. Four factors crossed in a fully factorial design produce 3,840 trials.} \label{fig:pipeline} \end{fig |
| `1` | sections/appendix.tex:158 | percentage | yes | ludegraphics[width=\columnwidth]{figures/10_probe_calibration_cliff.pdf} \caption{Compliance cliff (Study~1 pilot). Revision rates drop from 100\% to  |
| `100` | sections/appendix.tex:158 | percentage | yes | gures/10_probe_calibration_cliff.pdf} \caption{Compliance cliff (Study~1 pilot). Revision rates drop from 100\% to $\leq$25\% across five pilot probes |
| `25` | sections/appendix.tex:158 | percentage | yes | calibration_cliff.pdf} \caption{Compliance cliff (Study~1 pilot). Revision rates drop from 100\% to $\leq$25\% across five pilot probes with no interm |
| `1` | sections/appendix.tex:165 | bare number | yes | es/02_threshold_ladder.pdf} \caption{Overcorrection by threshold level within leading-probe trials (Study~1).} \label{fig:threshold-ladder} \end{figur |
| `1` | sections/appendix.tex:179 | bare number |  | ection{Full Statistical Tables} \label{sec:appendix-stats} \subsection{Pairwise Threshold Comparisons (Study 1)} \begin{table}[h] \centering \small \b |
| `3.47` | sections/appendix.tex:18 | mean or delta | yes | oprule \textbf{Predictor} & \textbf{Model A} & \textbf{Model B} & \textbf{Model C} \\ \midrule is\_leading & $3.47^{***}$ & $3.94^{***}$ & --- \\ thre |
| `3.94` | sections/appendix.tex:18 | mean or delta | yes | Predictor} & \textbf{Model A} & \textbf{Model B} & \textbf{Model C} \\ \midrule is\_leading & $3.47^{***}$ & $3.94^{***}$ & --- \\ threshold & $-0.93^ |
| `70` | sections/appendix.tex:188 | mean or delta | yes | } & \textbf{Comparison} & \textbf{$U$} & \textbf{$p_{\text{adj}}$} & \textbf{$r$} \\ \midrule Gemini (num.) & 70 vs.\ 100 & 4935 & $<$0.001 & $-$0.42  |
| `100` | sections/appendix.tex:188 | mean or delta | yes | tbf{Comparison} & \textbf{$U$} & \textbf{$p_{\text{adj}}$} & \textbf{$r$} \\ \midrule Gemini (num.) & 70 vs.\ 100 & 4935 & $<$0.001 & $-$0.42 \\ Gemin |
| `4935` | sections/appendix.tex:188 | mean or delta | yes | mparison} & \textbf{$U$} & \textbf{$p_{\text{adj}}$} & \textbf{$r$} \\ \midrule Gemini (num.) & 70 vs.\ 100 & 4935 & $<$0.001 & $-$0.42 \\ Gemini (num |
| `0.001` | sections/appendix.tex:188 | mean or delta | yes | & \textbf{$U$} & \textbf{$p_{\text{adj}}$} & \textbf{$r$} \\ \midrule Gemini (num.) & 70 vs.\ 100 & 4935 & $<$0.001 & $-$0.42 \\ Gemini (num.) & 85 vs |
| `0.42` | sections/appendix.tex:188 | mean or delta | yes | U$} & \textbf{$p_{\text{adj}}$} & \textbf{$r$} \\ \midrule Gemini (num.) & 70 vs.\ 100 & 4935 & $<$0.001 & $-$0.42 \\ Gemini (num.) & 85 vs.\ 100 & 42 |
| `85` | sections/appendix.tex:189 | mean or delta | yes | adj}}$} & \textbf{$r$} \\ \midrule Gemini (num.) & 70 vs.\ 100 & 4935 & $<$0.001 & $-$0.42 \\ Gemini (num.) & 85 vs.\ 100 & 4238 & $<$0.001 & $-$0.32  |
| `100` | sections/appendix.tex:189 | mean or delta | yes | & \textbf{$r$} \\ \midrule Gemini (num.) & 70 vs.\ 100 & 4935 & $<$0.001 & $-$0.42 \\ Gemini (num.) & 85 vs.\ 100 & 4238 & $<$0.001 & $-$0.32 \\ Gemin |
| `4238` | sections/appendix.tex:189 | mean or delta | yes | tbf{$r$} \\ \midrule Gemini (num.) & 70 vs.\ 100 & 4935 & $<$0.001 & $-$0.42 \\ Gemini (num.) & 85 vs.\ 100 & 4238 & $<$0.001 & $-$0.32 \\ Gemini (num |
| `0.001` | sections/appendix.tex:189 | mean or delta | yes | \ \midrule Gemini (num.) & 70 vs.\ 100 & 4935 & $<$0.001 & $-$0.42 \\ Gemini (num.) & 85 vs.\ 100 & 4238 & $<$0.001 & $-$0.32 \\ Gemini (num.) & 0 vs. |
| `0.32` | sections/appendix.tex:189 | mean or delta | yes | Gemini (num.) & 70 vs.\ 100 & 4935 & $<$0.001 & $-$0.42 \\ Gemini (num.) & 85 vs.\ 100 & 4238 & $<$0.001 & $-$0.32 \\ Gemini (num.) & 0 vs.\ 100 & 475 |
| `0.93` | sections/appendix.tex:19 | mean or delta | yes | xtbf{Model B} & \textbf{Model C} \\ \midrule is\_leading & $3.47^{***}$ & $3.94^{***}$ & --- \\ threshold & $-0.93^{***}$ & $-1.04^{***}$ & $-1.65^{** |
| `1.04` | sections/appendix.tex:19 | mean or delta | yes | \textbf{Model C} \\ \midrule is\_leading & $3.47^{***}$ & $3.94^{***}$ & --- \\ threshold & $-0.93^{***}$ & $-1.04^{***}$ & $-1.65^{***}$ \\ is\_quali |
| `1.65` | sections/appendix.tex:19 | mean or delta | yes | \\ \midrule is\_leading & $3.47^{***}$ & $3.94^{***}$ & --- \\ threshold & $-0.93^{***}$ & $-1.04^{***}$ & $-1.65^{***}$ \\ is\_qualitative & $-0.74^{ |
| `0` | sections/appendix.tex:190 | mean or delta | yes | 100 & 4935 & $<$0.001 & $-$0.42 \\ Gemini (num.) & 85 vs.\ 100 & 4238 & $<$0.001 & $-$0.32 \\ Gemini (num.) & 0 vs.\ 100 & 4755 & 0.002 & $-$0.25 \\ G |
| `100` | sections/appendix.tex:190 | mean or delta | yes | 935 & $<$0.001 & $-$0.42 \\ Gemini (num.) & 85 vs.\ 100 & 4238 & $<$0.001 & $-$0.32 \\ Gemini (num.) & 0 vs.\ 100 & 4755 & 0.002 & $-$0.25 \\ Gemini ( |
| `4755` | sections/appendix.tex:190 | mean or delta | yes | $<$0.001 & $-$0.42 \\ Gemini (num.) & 85 vs.\ 100 & 4238 & $<$0.001 & $-$0.32 \\ Gemini (num.) & 0 vs.\ 100 & 4755 & 0.002 & $-$0.25 \\ Gemini (qual.) |
| `0.002` | sections/appendix.tex:190 | mean or delta | yes | 1 & $-$0.42 \\ Gemini (num.) & 85 vs.\ 100 & 4238 & $<$0.001 & $-$0.32 \\ Gemini (num.) & 0 vs.\ 100 & 4755 & 0.002 & $-$0.25 \\ Gemini (qual.) & 0 vs |
| `0.25` | sections/appendix.tex:190 | mean or delta | yes | \\ Gemini (num.) & 85 vs.\ 100 & 4238 & $<$0.001 & $-$0.32 \\ Gemini (num.) & 0 vs.\ 100 & 4755 & 0.002 & $-$0.25 \\ Gemini (qual.) & 0 vs.\ 100 & 408 |
| `0` | sections/appendix.tex:191 | mean or delta | yes | .\ 100 & 4238 & $<$0.001 & $-$0.32 \\ Gemini (num.) & 0 vs.\ 100 & 4755 & 0.002 & $-$0.25 \\ Gemini (qual.) & 0 vs.\ 100 & 4084 & 0.002 & $-$0.28 \\ C |
| `100` | sections/appendix.tex:191 | mean or delta | yes | & 4238 & $<$0.001 & $-$0.32 \\ Gemini (num.) & 0 vs.\ 100 & 4755 & 0.002 & $-$0.25 \\ Gemini (qual.) & 0 vs.\ 100 & 4084 & 0.002 & $-$0.28 \\ Claude ( |
| `4084` | sections/appendix.tex:191 | mean or delta | yes | & $<$0.001 & $-$0.32 \\ Gemini (num.) & 0 vs.\ 100 & 4755 & 0.002 & $-$0.25 \\ Gemini (qual.) & 0 vs.\ 100 & 4084 & 0.002 & $-$0.28 \\ Claude (num.) & |
| `0.002` | sections/appendix.tex:191 | mean or delta | yes | .001 & $-$0.32 \\ Gemini (num.) & 0 vs.\ 100 & 4755 & 0.002 & $-$0.25 \\ Gemini (qual.) & 0 vs.\ 100 & 4084 & 0.002 & $-$0.28 \\ Claude (num.) & 85 vs |
| `0.28` | sections/appendix.tex:191 | mean or delta | yes | .32 \\ Gemini (num.) & 0 vs.\ 100 & 4755 & 0.002 & $-$0.25 \\ Gemini (qual.) & 0 vs.\ 100 & 4084 & 0.002 & $-$0.28 \\ Claude (num.) & 85 vs.\ 100 & 41 |
| `85` | sections/appendix.tex:192 | mean or delta | yes | vs.\ 100 & 4755 & 0.002 & $-$0.25 \\ Gemini (qual.) & 0 vs.\ 100 & 4084 & 0.002 & $-$0.28 \\ Claude (num.) & 85 vs.\ 100 & 4146 & $<$0.001 & $-$0.30 \ |
| `100` | sections/appendix.tex:192 | mean or delta | yes | 0 & 4755 & 0.002 & $-$0.25 \\ Gemini (qual.) & 0 vs.\ 100 & 4084 & 0.002 & $-$0.28 \\ Claude (num.) & 85 vs.\ 100 & 4146 & $<$0.001 & $-$0.30 \\ Claud |
| `4146` | sections/appendix.tex:192 | mean or delta | yes | 55 & 0.002 & $-$0.25 \\ Gemini (qual.) & 0 vs.\ 100 & 4084 & 0.002 & $-$0.28 \\ Claude (num.) & 85 vs.\ 100 & 4146 & $<$0.001 & $-$0.30 \\ Claude (qua |
| `0.001` | sections/appendix.tex:192 | mean or delta | yes | & $-$0.25 \\ Gemini (qual.) & 0 vs.\ 100 & 4084 & 0.002 & $-$0.28 \\ Claude (num.) & 85 vs.\ 100 & 4146 & $<$0.001 & $-$0.30 \\ Claude (qual.) & 85 vs |
| `0.30` | sections/appendix.tex:192 | mean or delta | yes | \\ Gemini (qual.) & 0 vs.\ 100 & 4084 & 0.002 & $-$0.28 \\ Claude (num.) & 85 vs.\ 100 & 4146 & $<$0.001 & $-$0.30 \\ Claude (qual.) & 85 vs.\ 100 & 3 |
| `85` | sections/appendix.tex:193 | mean or delta | yes | \ 100 & 4084 & 0.002 & $-$0.28 \\ Claude (num.) & 85 vs.\ 100 & 4146 & $<$0.001 & $-$0.30 \\ Claude (qual.) & 85 vs.\ 100 & 3880 & 0.024 & $-$0.21 \\  |
| `100` | sections/appendix.tex:193 | mean or delta | yes | 4084 & 0.002 & $-$0.28 \\ Claude (num.) & 85 vs.\ 100 & 4146 & $<$0.001 & $-$0.30 \\ Claude (qual.) & 85 vs.\ 100 & 3880 & 0.024 & $-$0.21 \\ \bottomr |
| `3880` | sections/appendix.tex:193 | mean or delta | yes | 0.002 & $-$0.28 \\ Claude (num.) & 85 vs.\ 100 & 4146 & $<$0.001 & $-$0.30 \\ Claude (qual.) & 85 vs.\ 100 & 3880 & 0.024 & $-$0.21 \\ \bottomrule \en |
| `0.024` | sections/appendix.tex:193 | mean or delta | yes | & $-$0.28 \\ Claude (num.) & 85 vs.\ 100 & 4146 & $<$0.001 & $-$0.30 \\ Claude (qual.) & 85 vs.\ 100 & 3880 & 0.024 & $-$0.21 \\ \bottomrule \end{tabu |
| `0.21` | sections/appendix.tex:193 | mean or delta | yes | \ Claude (num.) & 85 vs.\ 100 & 4146 & $<$0.001 & $-$0.30 \\ Claude (qual.) & 85 vs.\ 100 & 3880 & 0.024 & $-$0.21 \\ \bottomrule \end{tabular} \capti |
| `0.05` | sections/appendix.tex:196 | reliability or effect size | yes | & $-$0.21 \\ \bottomrule \end{tabular} \caption{Significant pairwise comparisons (Bonferroni-corrected, $q < 0.05$).} \label{tab:pairwise} \end{table} |
| `0.74` | sections/appendix.tex:20 | mean or delta | yes | **}$ & $3.94^{***}$ & --- \\ threshold & $-0.93^{***}$ & $-1.04^{***}$ & $-1.65^{***}$ \\ is\_qualitative & $-0.74^{***}$ & $-0.85^{***}$ & $-1.05^{** |
| `0.85` | sections/appendix.tex:20 | mean or delta | yes | *}$ & --- \\ threshold & $-0.93^{***}$ & $-1.04^{***}$ & $-1.65^{***}$ \\ is\_qualitative & $-0.74^{***}$ & $-0.85^{***}$ & $-1.05^{***}$ \\ Claude So |
| `1.05` | sections/appendix.tex:20 | mean or delta | yes | eshold & $-0.93^{***}$ & $-1.04^{***}$ & $-1.65^{***}$ \\ is\_qualitative & $-0.74^{***}$ & $-0.85^{***}$ & $-1.05^{***}$ \\ Claude Sonnet & $0.10$ &  |
| `0.05` | sections/appendix.tex:202 | percentage |  | 0.05$).} \label{tab:pairwise} \end{table} \subsection{Power Analysis} Post-hoc power analysis at $\alpha = 0.05$, 80\% power: \begin{itemize} \item \t |
| `80` | sections/appendix.tex:202 | percentage |  | .} \label{tab:pairwise} \end{table} \subsection{Power Analysis} Post-hoc power analysis at $\alpha = 0.05$, 80\% power: \begin{itemize} \item \textbf{ |
| `1` | sections/appendix.tex:204 | percentage |  | er Analysis} Post-hoc power analysis at $\alpha = 0.05$, 80\% power: \begin{itemize} \item \textbf{Study~1 RQ1} ($N = 1{,}920$ per probe): MDE for pro |
| `1` | sections/appendix.tex:204 | percentage |  | Post-hoc power analysis at $\alpha = 0.05$, 80\% power: \begin{itemize} \item \textbf{Study~1 RQ1} ($N = 1{,}920$ per probe): MDE for proportion diffe |
| `920` | sections/appendix.tex:204 | percentage |  | t-hoc power analysis at $\alpha = 0.05$, 80\% power: \begin{itemize} \item \textbf{Study~1 RQ1} ($N = 1{,}920$ per probe): MDE for proportion differen |
| `0.032` | sections/appendix.tex:204 | count or denominator |  | r: \begin{itemize} \item \textbf{Study~1 RQ1} ($N = 1{,}920$ per probe): MDE for proportion difference $= 0.032$. Observed $\approx 0.75$. Massively o |
| `0.75` | sections/appendix.tex:204 | count or denominator |  | em \textbf{Study~1 RQ1} ($N = 1{,}920$ per probe): MDE for proportion difference $= 0.032$. Observed $\approx 0.75$. Massively overpowered. \item \tex |
| `1` | sections/appendix.tex:205 | count or denominator |  | for proportion difference $= 0.032$. Observed $\approx 0.75$. Massively overpowered. \item \textbf{Study~1 RQ2} ($N = 1{,}920$ leading-probe): MDE for |
| `1` | sections/appendix.tex:205 | count or denominator |  | on difference $= 0.032$. Observed $\approx 0.75$. Massively overpowered. \item \textbf{Study~1 RQ2} ($N = 1{,}920$ leading-probe): MDE for $|\rho| = 0 |
| `920` | sections/appendix.tex:205 | count or denominator |  | ifference $= 0.032$. Observed $\approx 0.75$. Massively overpowered. \item \textbf{Study~1 RQ2} ($N = 1{,}920$ leading-probe): MDE for $|\rho| = 0.064 |
| `0.064` | sections/appendix.tex:205 | count or denominator |  | 0.75$. Massively overpowered. \item \textbf{Study~1 RQ2} ($N = 1{,}920$ leading-probe): MDE for $|\rho| = 0.064$. All observed correlations exceed thi |
| `3` | sections/appendix.tex:206 | count or denominator |  | 920$ leading-probe): MDE for $|\rho| = 0.064$. All observed correlations exceed this. \item \textbf{Study~3} ($N = 720$ trials, balanced panel $n = 50 |
| `720` | sections/appendix.tex:206 | count or denominator |  | ing-probe): MDE for $|\rho| = 0.064$. All observed correlations exceed this. \item \textbf{Study~3} ($N = 720$ trials, balanced panel $n = 50$): Panel |
| `50` | sections/appendix.tex:206 | count or denominator |  | 64$. All observed correlations exceed this. \item \textbf{Study~3} ($N = 720$ trials, balanced panel $n = 50$): Panel-level MDE $= 0.5$ levels. Observ |
| `0.5` | sections/appendix.tex:206 | count or denominator |  | tions exceed this. \item \textbf{Study~3} ($N = 720$ trials, balanced panel $n = 50$): Panel-level MDE $= 0.5$ levels. Observed $\Delta = 0.94$ unstri |
| `0.94` | sections/appendix.tex:206 | count or denominator |  | xtbf{Study~3} ($N = 720$ trials, balanced panel $n = 50$): Panel-level MDE $= 0.5$ levels. Observed $\Delta = 0.94$ unstripped ($0.74$ after meta-comm |
| `0.74` | sections/appendix.tex:206 | count or denominator |  | 720$ trials, balanced panel $n = 50$): Panel-level MDE $= 0.5$ levels. Observed $\Delta = 0.94$ unstripped ($0.74$ after meta-commentary stripping), b |
| `50` | sections/appendix.tex:206 | p-value |  | tary stripping), both exceeding the MDE. The effective sample for the paired test is the balanced panel ($n = 50$ trials with genuine revision at all  |
| `3.32` | sections/appendix.tex:206 | p-value |  | the paired test is the balanced panel ($n = 50$ trials with genuine revision at all turns), which yields $p = 3.32 \times 10^{-6}$ (Wilcoxon, $r = 0.6 |
| `10` | sections/appendix.tex:206 | p-value |  | est is the balanced panel ($n = 50$ trials with genuine revision at all turns), which yields $p = 3.32 \times 10^{-6}$ (Wilcoxon, $r = 0.658$) on the  |
| `6` | sections/appendix.tex:206 | p-value |  | s the balanced panel ($n = 50$ trials with genuine revision at all turns), which yields $p = 3.32 \times 10^{-6}$ (Wilcoxon, $r = 0.658$) on the unstr |
| `0.658` | sections/appendix.tex:206 | p-value |  | ($n = 50$ trials with genuine revision at all turns), which yields $p = 3.32 \times 10^{-6}$ (Wilcoxon, $r = 0.658$) on the unstripped cliff; the stri |
| `0.74` | sections/appendix.tex:206 | p-value |  | elds $p = 3.32 \times 10^{-6}$ (Wilcoxon, $r = 0.658$) on the unstripped cliff; the stripped cliff ($\Delta = 0.74$) has $p = 1.01 \times 10^{-4}$ ($r |
| `1.01` | sections/appendix.tex:206 | p-value |  | times 10^{-6}$ (Wilcoxon, $r = 0.658$) on the unstripped cliff; the stripped cliff ($\Delta = 0.74$) has $p = 1.01 \times 10^{-4}$ ($r = 0.55$). \end{ |
| `10` | sections/appendix.tex:206 | p-value |  | }$ (Wilcoxon, $r = 0.658$) on the unstripped cliff; the stripped cliff ($\Delta = 0.74$) has $p = 1.01 \times 10^{-4}$ ($r = 0.55$). \end{itemize} \se |
| `4` | sections/appendix.tex:206 | p-value |  | ilcoxon, $r = 0.658$) on the unstripped cliff; the stripped cliff ($\Delta = 0.74$) has $p = 1.01 \times 10^{-4}$ ($r = 0.55$). \end{itemize} \section |
| `0.55` | sections/appendix.tex:206 | p-value |  | r = 0.658$) on the unstripped cliff; the stripped cliff ($\Delta = 0.74$) has $p = 1.01 \times 10^{-4}$ ($r = 0.55$). \end{itemize} \section{Evaluator |
| `0.10` | sections/appendix.tex:21 | mean or delta | yes | {***}$ & $-1.65^{***}$ \\ is\_qualitative & $-0.74^{***}$ & $-0.85^{***}$ & $-1.05^{***}$ \\ Claude Sonnet & $0.10$ & $0.15$ & $0.33^{**}$ \\ Gemini F |
| `0.15` | sections/appendix.tex:21 | mean or delta | yes | $-1.65^{***}$ \\ is\_qualitative & $-0.74^{***}$ & $-0.85^{***}$ & $-1.05^{***}$ \\ Claude Sonnet & $0.10$ & $0.15$ & $0.33^{**}$ \\ Gemini Flash & $0 |
| `0.33` | sections/appendix.tex:21 | mean or delta | yes | **}$ \\ is\_qualitative & $-0.74^{***}$ & $-0.85^{***}$ & $-1.05^{***}$ \\ Claude Sonnet & $0.10$ & $0.15$ & $0.33^{**}$ \\ Gemini Flash & $0.42^{***} |
| `0.42` | sections/appendix.tex:22 | mean or delta | yes | 74^{***}$ & $-0.85^{***}$ & $-1.05^{***}$ \\ Claude Sonnet & $0.10$ & $0.15$ & $0.33^{**}$ \\ Gemini Flash & $0.42^{***}$ & $0.52^{***}$ & $1.15^{***} |
| `0.52` | sections/appendix.tex:22 | mean or delta | yes | .85^{***}$ & $-1.05^{***}$ \\ Claude Sonnet & $0.10$ & $0.15$ & $0.33^{**}$ \\ Gemini Flash & $0.42^{***}$ & $0.52^{***}$ & $1.15^{***}$ \\ Scenario F |
| `1.15` | sections/appendix.tex:22 | mean or delta | yes | 1.05^{***}$ \\ Claude Sonnet & $0.10$ & $0.15$ & $0.33^{**}$ \\ Gemini Flash & $0.42^{***}$ & $0.52^{***}$ & $1.15^{***}$ \\ Scenario FEs & No & Yes & |
| `4` | sections/appendix.tex:220 | reliability or effect size | yes | }} \toprule \textbf{Candidate Judge} & \textbf{Spearman $r$} & \textbf{QW $\kappa$} \\ \midrule Claude Sonnet 4 & $0.505$ & $0.526$ \\ DeepSeek V4 & $ |
| `0.505` | sections/appendix.tex:220 | reliability or effect size | yes | oprule \textbf{Candidate Judge} & \textbf{Spearman $r$} & \textbf{QW $\kappa$} \\ \midrule Claude Sonnet 4 & $0.505$ & $0.526$ \\ DeepSeek V4 & $0.340 |
| `0.526` | sections/appendix.tex:220 | reliability or effect size | yes | xtbf{Candidate Judge} & \textbf{Spearman $r$} & \textbf{QW $\kappa$} \\ \midrule Claude Sonnet 4 & $0.505$ & $0.526$ \\ DeepSeek V4 & $0.340$ & $0.398 |
| `0.340` | sections/appendix.tex:221 | reliability or effect size | yes | textbf{Spearman $r$} & \textbf{QW $\kappa$} \\ \midrule Claude Sonnet 4 & $0.505$ & $0.526$ \\ DeepSeek V4 & $0.340$ & $0.398$ \\ Qwen 3 235B & $0.272 |
| `0.398` | sections/appendix.tex:221 | reliability or effect size | yes | arman $r$} & \textbf{QW $\kappa$} \\ \midrule Claude Sonnet 4 & $0.505$ & $0.526$ \\ DeepSeek V4 & $0.340$ & $0.398$ \\ Qwen 3 235B & $0.272$ & $0.017 |
| `3` | sections/appendix.tex:222 | reliability or effect size | yes | extbf{QW $\kappa$} \\ \midrule Claude Sonnet 4 & $0.505$ & $0.526$ \\ DeepSeek V4 & $0.340$ & $0.398$ \\ Qwen 3 235B & $0.272$ & $0.017$ \\ Llama 3.3  |
| `0.272` | sections/appendix.tex:222 | reliability or effect size | yes | \kappa$} \\ \midrule Claude Sonnet 4 & $0.505$ & $0.526$ \\ DeepSeek V4 & $0.340$ & $0.398$ \\ Qwen 3 235B & $0.272$ & $0.017$ \\ Llama 3.3 70B & $0.1 |
| `0.017` | sections/appendix.tex:222 | mean or delta | yes | \ \midrule Claude Sonnet 4 & $0.505$ & $0.526$ \\ DeepSeek V4 & $0.340$ & $0.398$ \\ Qwen 3 235B & $0.272$ & $0.017$ \\ Llama 3.3 70B & $0.181$ & $0.0 |
| `3.3` | sections/appendix.tex:223 | mean or delta | yes | e Sonnet 4 & $0.505$ & $0.526$ \\ DeepSeek V4 & $0.340$ & $0.398$ \\ Qwen 3 235B & $0.272$ & $0.017$ \\ Llama 3.3 70B & $0.181$ & $0.022$ \\ GPT-4o &  |
| `0.181` | sections/appendix.tex:223 | mean or delta | yes | & $0.505$ & $0.526$ \\ DeepSeek V4 & $0.340$ & $0.398$ \\ Qwen 3 235B & $0.272$ & $0.017$ \\ Llama 3.3 70B & $0.181$ & $0.022$ \\ GPT-4o & $0.140$ & $ |
| `0.022` | sections/appendix.tex:223 | mean or delta | yes | & $0.526$ \\ DeepSeek V4 & $0.340$ & $0.398$ \\ Qwen 3 235B & $0.272$ & $0.017$ \\ Llama 3.3 70B & $0.181$ & $0.022$ \\ GPT-4o & $0.140$ & $0.065$ \\  |
| `0.140` | sections/appendix.tex:224 | mean or delta | yes | k V4 & $0.340$ & $0.398$ \\ Qwen 3 235B & $0.272$ & $0.017$ \\ Llama 3.3 70B & $0.181$ & $0.022$ \\ GPT-4o & $0.140$ & $0.065$ \\ Gemini 2.5 Flash & $ |
| `0.065` | sections/appendix.tex:224 | mean or delta | yes | 340$ & $0.398$ \\ Qwen 3 235B & $0.272$ & $0.017$ \\ Llama 3.3 70B & $0.181$ & $0.022$ \\ GPT-4o & $0.140$ & $0.065$ \\ Gemini 2.5 Flash & $-0.036$ &  |
| `2.5` | sections/appendix.tex:225 | count or denominator | yes | Qwen 3 235B & $0.272$ & $0.017$ \\ Llama 3.3 70B & $0.181$ & $0.022$ \\ GPT-4o & $0.140$ & $0.065$ \\ Gemini 2.5 Flash & $-0.036$ & $-0.026$ \\ \botto |
| `0.036` | sections/appendix.tex:225 | count or denominator | yes | $0.272$ & $0.017$ \\ Llama 3.3 70B & $0.181$ & $0.022$ \\ GPT-4o & $0.140$ & $0.065$ \\ Gemini 2.5 Flash & $-0.036$ & $-0.026$ \\ \bottomrule \end{tab |
| `0.026` | sections/appendix.tex:225 | reliability or effect size | yes | $0.017$ \\ Llama 3.3 70B & $0.181$ & $0.022$ \\ GPT-4o & $0.140$ & $0.065$ \\ Gemini 2.5 Flash & $-0.036$ & $-0.026$ \\ \bottomrule \end{tabular} \cap |
| `64` | sections/appendix.tex:228 | reliability or effect size | yes | Gemini 2.5 Flash & $-0.036$ & $-0.026$ \\ \bottomrule \end{tabular} \caption{Judge calibration results ($n = 64$ stratified samples each; Spearman cor |
| `4` | sections/appendix.tex:228 | reliability or effect size | yes | results ($n = 64$ stratified samples each; Spearman correlation against the human rater mean). Claude Sonnet~4 was selected as the Study~3 evaluator,  |
| `3` | sections/appendix.tex:228 | p-value | yes | d samples each; Spearman correlation against the human rater mean). Claude Sonnet~4 was selected as the Study~3 evaluator, with the highest human corr |
| `0.505` | sections/appendix.tex:228 | p-value | yes | onnet~4 was selected as the Study~3 evaluator, with the highest human correlation of the six candidates ($r = 0.505$, $p = 2.1 \times 10^{-5}$). Gemin |
| `2.1` | sections/appendix.tex:228 | p-value | yes | elected as the Study~3 evaluator, with the highest human correlation of the six candidates ($r = 0.505$, $p = 2.1 \times 10^{-5}$). Gemini 2.5 Flash w |
| `10` | sections/appendix.tex:228 | p-value | yes | the Study~3 evaluator, with the highest human correlation of the six candidates ($r = 0.505$, $p = 2.1 \times 10^{-5}$). Gemini 2.5 Flash was anti-cor |
| `5` | sections/appendix.tex:228 | p-value | yes | tudy~3 evaluator, with the highest human correlation of the six candidates ($r = 0.505$, $p = 2.1 \times 10^{-5}$). Gemini 2.5 Flash was anti-correlat |
| `2.5` | sections/appendix.tex:228 | p-value | yes | tor, with the highest human correlation of the six candidates ($r = 0.505$, $p = 2.1 \times 10^{-5}$). Gemini 2.5 Flash was anti-correlated with human |
| `0.578` | sections/appendix.tex:242 | percentage | yes | n{tabular}{@{}lrrr@{}} \toprule Rater pair & QW $\kappa$ & Binary & Within 1 \\ \midrule Rater A -- Rater B & 0.578 & 78.1\% & 95.3\% \\ Rater B -- Ra |
| `78.1` | sections/appendix.tex:242 | percentage | yes | r}{@{}lrrr@{}} \toprule Rater pair & QW $\kappa$ & Binary & Within 1 \\ \midrule Rater A -- Rater B & 0.578 & 78.1\% & 95.3\% \\ Rater B -- Rater C &  |
| `95.3` | sections/appendix.tex:242 | percentage | yes | r@{}} \toprule Rater pair & QW $\kappa$ & Binary & Within 1 \\ \midrule Rater A -- Rater B & 0.578 & 78.1\% & 95.3\% \\ Rater B -- Rater C & 0.603 & 8 |
| `0.603` | sections/appendix.tex:243 | percentage | yes | $\kappa$ & Binary & Within 1 \\ \midrule Rater A -- Rater B & 0.578 & 78.1\% & 95.3\% \\ Rater B -- Rater C & 0.603 & 82.8\% & 87.5\% \\ Rater A -- Ra |
| `82.8` | sections/appendix.tex:243 | percentage | yes | & Binary & Within 1 \\ \midrule Rater A -- Rater B & 0.578 & 78.1\% & 95.3\% \\ Rater B -- Rater C & 0.603 & 82.8\% & 87.5\% \\ Rater A -- Rater C & 0 |
| `87.5` | sections/appendix.tex:243 | percentage | yes | & Within 1 \\ \midrule Rater A -- Rater B & 0.578 & 78.1\% & 95.3\% \\ Rater B -- Rater C & 0.603 & 82.8\% & 87.5\% \\ Rater A -- Rater C & 0.406 & 76 |
| `0.406` | sections/appendix.tex:244 | percentage | yes | -- Rater B & 0.578 & 78.1\% & 95.3\% \\ Rater B -- Rater C & 0.603 & 82.8\% & 87.5\% \\ Rater A -- Rater C & 0.406 & 76.6\% & 81.2\% \\ \midrule All t |
| `76.6` | sections/appendix.tex:244 | percentage | yes | r B & 0.578 & 78.1\% & 95.3\% \\ Rater B -- Rater C & 0.603 & 82.8\% & 87.5\% \\ Rater A -- Rater C & 0.406 & 76.6\% & 81.2\% \\ \midrule All three ($ |
| `81.2` | sections/appendix.tex:244 | percentage | yes | 78 & 78.1\% & 95.3\% \\ Rater B -- Rater C & 0.603 & 82.8\% & 87.5\% \\ Rater A -- Rater C & 0.406 & 76.6\% & 81.2\% \\ \midrule All three ($\alpha$)  |
| `0.529` | sections/appendix.tex:246 | percentage | yes | & 0.603 & 82.8\% & 87.5\% \\ Rater A -- Rater C & 0.406 & 76.6\% & 81.2\% \\ \midrule All three ($\alpha$) & 0.529 & --- & --- \\ Evaluator -- Human M |
| `0.526` | sections/appendix.tex:247 | percentage | yes | C & 0.406 & 76.6\% & 81.2\% \\ \midrule All three ($\alpha$) & 0.529 & --- & --- \\ Evaluator -- Human Mean & 0.526 & --- & --- \\ \bottomrule \end{ta |
| `3,840` | sections/appendix.tex:25 | mean or delta | yes | Gemini Flash & $0.42^{***}$ & $0.52^{***}$ & $1.15^{***}$ \\ Scenario FEs & No & Yes & Yes \\ \midrule $N$ & 3,840 & 3,840 & 1,920 \\ AIC & 5,319 & 4, |
| `3,840` | sections/appendix.tex:25 | mean or delta | yes | Flash & $0.42^{***}$ & $0.52^{***}$ & $1.15^{***}$ \\ Scenario FEs & No & Yes & Yes \\ \midrule $N$ & 3,840 & 3,840 & 1,920 \\ AIC & 5,319 & 4,839 & 3 |
| `1,920` | sections/appendix.tex:25 | mean or delta | yes | $0.42^{***}$ & $0.52^{***}$ & $1.15^{***}$ \\ Scenario FEs & No & Yes & Yes \\ \midrule $N$ & 3,840 & 3,840 & 1,920 \\ AIC & 5,319 & 4,839 & 3,545 \\  |
| `64` | sections/appendix.tex:250 | reliability or effect size | yes | \\ Evaluator -- Human Mean & 0.526 & --- & --- \\ \bottomrule \end{tabular} \caption{Human rater agreement on 64 stratified samples (6$\to$2 recode ap |
| `6` | sections/appendix.tex:250 | reliability or effect size | yes | ean & 0.526 & --- & --- \\ \bottomrule \end{tabular} \caption{Human rater agreement on 64 stratified samples (6$\to$2 recode applied before analysis,  |
| `2` | sections/appendix.tex:250 | reliability or effect size | yes | 0.526 & --- & --- \\ \bottomrule \end{tabular} \caption{Human rater agreement on 64 stratified samples (6$\to$2 recode applied before analysis, 3 rate |
| `3` | sections/appendix.tex:250 | reliability or effect size | yes | end{tabular} \caption{Human rater agreement on 64 stratified samples (6$\to$2 recode applied before analysis, 3 raters). QW $\kappa$: quadratic-weight |
| `0.001` | sections/appendix.tex:250 | p-value | yes | q 4$) vs.\ not. Within-1: ratings differ by $\leq 1$ level. Evaluator--Human Mean: Spearman $r = 0.505$ ($p < 0.001$).} \label{tab:human-agreement} \e |
| `1` | sections/appendix.tex:254 | p-value |  | tor--Human Mean: Spearman $r = 0.505$ ($p < 0.001$).} \label{tab:human-agreement} \end{table} \section{Study 1 Inter-Rater Reliability} \label{sec:app |
| `5,319` | sections/appendix.tex:26 | mean or delta | yes | $0.52^{***}$ & $1.15^{***}$ \\ Scenario FEs & No & Yes & Yes \\ \midrule $N$ & 3,840 & 3,840 & 1,920 \\ AIC & 5,319 & 4,839 & 3,545 \\ \bottomrule \en |
| `4,839` | sections/appendix.tex:26 | mean or delta | yes | **}$ & $1.15^{***}$ \\ Scenario FEs & No & Yes & Yes \\ \midrule $N$ & 3,840 & 3,840 & 1,920 \\ AIC & 5,319 & 4,839 & 3,545 \\ \bottomrule \end{tabula |
| `3,545` | sections/appendix.tex:26 | mean or delta | yes | 1.15^{***}$ \\ Scenario FEs & No & Yes & Yes \\ \midrule $N$ & 3,840 & 3,840 & 1,920 \\ AIC & 5,319 & 4,839 & 3,545 \\ \bottomrule \end{tabular} \capt |
| `0.844` | sections/appendix.tex:264 | reliability or effect size | yes | \toprule \textbf{Dimension} & \textbf{QW $\kappa$} & \textbf{Interpretation} \\ \midrule Revision magnitude & 0.844 & Excellent \\ Revision value & 0. |
| `0.690` | sections/appendix.tex:265 | reliability or effect size | yes | QW $\kappa$} & \textbf{Interpretation} \\ \midrule Revision magnitude & 0.844 & Excellent \\ Revision value & 0.690 & Good \\ Overcorrection & 0.609 & |
| `0.609` | sections/appendix.tex:266 | mean or delta | yes | tion} \\ \midrule Revision magnitude & 0.844 & Excellent \\ Revision value & 0.690 & Good \\ Overcorrection & 0.609 & Acceptable \\ Threshold alignmen |
| `0.556` | sections/appendix.tex:267 | mean or delta | yes | & Excellent \\ Revision value & 0.690 & Good \\ Overcorrection & 0.609 & Acceptable \\ Threshold alignment & 0.556 & Marginal \\ \bottomrule \end{tabu |
| `1` | sections/appendix.tex:270 | count or denominator | yes | hreshold alignment & 0.556 & Marginal \\ \bottomrule \end{tabular} \caption{Inter-rater reliability for Study~1 (GPT-4o vs.\ Claude Sonnet~4, $n = 60$ |
| `4` | sections/appendix.tex:270 | count or denominator | yes | Marginal \\ \bottomrule \end{tabular} \caption{Inter-rater reliability for Study~1 (GPT-4o vs.\ Claude Sonnet~4, $n = 60$).} \label{tab:irr} \end{tabl |
| `60` | sections/appendix.tex:270 | count or denominator | yes | \\ \bottomrule \end{tabular} \caption{Inter-rater reliability for Study~1 (GPT-4o vs.\ Claude Sonnet~4, $n = 60$).} \label{tab:irr} \end{table} \begin |
| `1` | sections/appendix.tex:279 | percentage | yes | bular}{@{}lccc@{}} \toprule \textbf{Dimension} & \textbf{QW $\kappa$} & \textbf{\% Agree} & \textbf{\% Within 1} \\ \midrule Revision magnitude & 0.57 |
| `0.575` | sections/appendix.tex:281 | percentage | yes | Dimension} & \textbf{QW $\kappa$} & \textbf{\% Agree} & \textbf{\% Within 1} \\ \midrule Revision magnitude & 0.575 & 68.3 & 85.0 \\ Revision value &  |
| `68.3` | sections/appendix.tex:281 | percentage | yes | n} & \textbf{QW $\kappa$} & \textbf{\% Agree} & \textbf{\% Within 1} \\ \midrule Revision magnitude & 0.575 & 68.3 & 85.0 \\ Revision value & 0.669 &  |
| `85.0` | sections/appendix.tex:281 | percentage | yes | extbf{QW $\kappa$} & \textbf{\% Agree} & \textbf{\% Within 1} \\ \midrule Revision magnitude & 0.575 & 68.3 & 85.0 \\ Revision value & 0.669 & 76.7 &  |
| `0.669` | sections/appendix.tex:282 | percentage | yes | tbf{\% Agree} & \textbf{\% Within 1} \\ \midrule Revision magnitude & 0.575 & 68.3 & 85.0 \\ Revision value & 0.669 & 76.7 & 88.3 \\ Overcorrection &  |
| `76.7` | sections/appendix.tex:282 | percentage | yes | gree} & \textbf{\% Within 1} \\ \midrule Revision magnitude & 0.575 & 68.3 & 85.0 \\ Revision value & 0.669 & 76.7 & 88.3 \\ Overcorrection & 0.392 &  |
| `88.3` | sections/appendix.tex:282 | percentage | yes | \textbf{\% Within 1} \\ \midrule Revision magnitude & 0.575 & 68.3 & 85.0 \\ Revision value & 0.669 & 76.7 & 88.3 \\ Overcorrection & 0.392 & 71.7 & 9 |
| `0.392` | sections/appendix.tex:283 | mean or delta | yes | \midrule Revision magnitude & 0.575 & 68.3 & 85.0 \\ Revision value & 0.669 & 76.7 & 88.3 \\ Overcorrection & 0.392 & 71.7 & 90.0 \\ Threshold alignme |
| `71.7` | sections/appendix.tex:283 | mean or delta | yes | Revision magnitude & 0.575 & 68.3 & 85.0 \\ Revision value & 0.669 & 76.7 & 88.3 \\ Overcorrection & 0.392 & 71.7 & 90.0 \\ Threshold alignment & 0.33 |
| `90.0` | sections/appendix.tex:283 | mean or delta | yes | on magnitude & 0.575 & 68.3 & 85.0 \\ Revision value & 0.669 & 76.7 & 88.3 \\ Overcorrection & 0.392 & 71.7 & 90.0 \\ Threshold alignment & 0.339 & 38 |
| `0.339` | sections/appendix.tex:284 | count or denominator | yes | 85.0 \\ Revision value & 0.669 & 76.7 & 88.3 \\ Overcorrection & 0.392 & 71.7 & 90.0 \\ Threshold alignment & 0.339 & 38.3 & 85.0 \\ \bottomrule \end{ |
| `38.3` | sections/appendix.tex:284 | count or denominator | yes | Revision value & 0.669 & 76.7 & 88.3 \\ Overcorrection & 0.392 & 71.7 & 90.0 \\ Threshold alignment & 0.339 & 38.3 & 85.0 \\ \bottomrule \end{tabular} |
| `85.0` | sections/appendix.tex:284 | count or denominator | yes | n value & 0.669 & 76.7 & 88.3 \\ Overcorrection & 0.392 & 71.7 & 90.0 \\ Threshold alignment & 0.339 & 38.3 & 85.0 \\ \bottomrule \end{tabular} \capti |
| `2` | sections/appendix.tex:287 | count or denominator | yes | shold alignment & 0.339 & 38.3 & 85.0 \\ \bottomrule \end{tabular} \caption{Inter-rater reliability for Study~2 ($n = 60$).} \label{tab:irr-momentum}  |
| `60` | sections/appendix.tex:287 | count or denominator | yes | ignment & 0.339 & 38.3 & 85.0 \\ \bottomrule \end{tabular} \caption{Inter-rater reliability for Study~2 ($n = 60$).} \label{tab:irr-momentum} \end{tab |
| `0.01` | sections/appendix.tex:29 | p-value | yes | tabular} \caption{Ordinal regression (overcorrection $\sim$ predictors). Model C: leading-probe only. $^{**}p<0.01$, $^{***}p<0.001$. Reference: GPT-4 |
| `0.001` | sections/appendix.tex:29 | p-value | yes | n{Ordinal regression (overcorrection $\sim$ predictors). Model C: leading-probe only. $^{**}p<0.01$, $^{***}p<0.001$. Reference: GPT-4o.} \label{tab:r |
| `3.3` | sections/appendix.tex:305 | percentage | yes | \toprule & $n$ & \% down & $p$ \\ \midrule \multicolumn{4}{@{}l}{\emph{By model}} \\ Llama 3.3 70B & 353 & 68.9 & $<0.001$ \\ Claude Sonnet 4 & 196 &  |
| `353` | sections/appendix.tex:305 | percentage | yes | & $n$ & \% down & $p$ \\ \midrule \multicolumn{4}{@{}l}{\emph{By model}} \\ Llama 3.3 70B & 353 & 68.9 & $<0.001$ \\ Claude Sonnet 4 & 196 & 58.5 & 0. |
| `68.9` | sections/appendix.tex:305 | percentage | yes | n$ & \% down & $p$ \\ \midrule \multicolumn{4}{@{}l}{\emph{By model}} \\ Llama 3.3 70B & 353 & 68.9 & $<0.001$ \\ Claude Sonnet 4 & 196 & 58.5 & 0.11  |
| `0.001` | sections/appendix.tex:305 | mean or delta | yes | own & $p$ \\ \midrule \multicolumn{4}{@{}l}{\emph{By model}} \\ Llama 3.3 70B & 353 & 68.9 & $<0.001$ \\ Claude Sonnet 4 & 196 & 58.5 & 0.11 \\ Qwen 3 |
| `4` | sections/appendix.tex:306 | mean or delta | yes | \multicolumn{4}{@{}l}{\emph{By model}} \\ Llama 3.3 70B & 353 & 68.9 & $<0.001$ \\ Claude Sonnet 4 & 196 & 58.5 & 0.11 \\ Qwen 3 235B & 90 & 74.5 & $< |
| `196` | sections/appendix.tex:306 | mean or delta | yes | lticolumn{4}{@{}l}{\emph{By model}} \\ Llama 3.3 70B & 353 & 68.9 & $<0.001$ \\ Claude Sonnet 4 & 196 & 58.5 & 0.11 \\ Qwen 3 235B & 90 & 74.5 & $<0.0 |
| `58.5` | sections/appendix.tex:306 | mean or delta | yes | umn{4}{@{}l}{\emph{By model}} \\ Llama 3.3 70B & 353 & 68.9 & $<0.001$ \\ Claude Sonnet 4 & 196 & 58.5 & 0.11 \\ Qwen 3 235B & 90 & 74.5 & $<0.001$ \\ |
| `0.11` | sections/appendix.tex:306 | mean or delta | yes | @{}l}{\emph{By model}} \\ Llama 3.3 70B & 353 & 68.9 & $<0.001$ \\ Claude Sonnet 4 & 196 & 58.5 & 0.11 \\ Qwen 3 235B & 90 & 74.5 & $<0.001$ \\ GPT-4o |
| `3` | sections/appendix.tex:307 | mean or delta | yes | del}} \\ Llama 3.3 70B & 353 & 68.9 & $<0.001$ \\ Claude Sonnet 4 & 196 & 58.5 & 0.11 \\ Qwen 3 235B & 90 & 74.5 & $<0.001$ \\ GPT-4o & 40 & 80.0 & 0. |
| `90` | sections/appendix.tex:307 | mean or delta | yes | lama 3.3 70B & 353 & 68.9 & $<0.001$ \\ Claude Sonnet 4 & 196 & 58.5 & 0.11 \\ Qwen 3 235B & 90 & 74.5 & $<0.001$ \\ GPT-4o & 40 & 80.0 & 0.006 \\ Dee |
| `74.5` | sections/appendix.tex:307 | mean or delta | yes | .3 70B & 353 & 68.9 & $<0.001$ \\ Claude Sonnet 4 & 196 & 58.5 & 0.11 \\ Qwen 3 235B & 90 & 74.5 & $<0.001$ \\ GPT-4o & 40 & 80.0 & 0.006 \\ DeepSeek- |
| `0.001` | sections/appendix.tex:307 | mean or delta | yes | & 353 & 68.9 & $<0.001$ \\ Claude Sonnet 4 & 196 & 58.5 & 0.11 \\ Qwen 3 235B & 90 & 74.5 & $<0.001$ \\ GPT-4o & 40 & 80.0 & 0.006 \\ DeepSeek-V4 & 31 |
| `40` | sections/appendix.tex:308 | mean or delta | yes | laude Sonnet 4 & 196 & 58.5 & 0.11 \\ Qwen 3 235B & 90 & 74.5 & $<0.001$ \\ GPT-4o & 40 & 80.0 & 0.006 \\ DeepSeek-V4 & 31 & 85.7 & 0.007 \\ Gemini 2. |
| `80.0` | sections/appendix.tex:308 | mean or delta | yes | Sonnet 4 & 196 & 58.5 & 0.11 \\ Qwen 3 235B & 90 & 74.5 & $<0.001$ \\ GPT-4o & 40 & 80.0 & 0.006 \\ DeepSeek-V4 & 31 & 85.7 & 0.007 \\ Gemini 2.5 Flas |
| `0.006` | sections/appendix.tex:308 | mean or delta | yes | 4 & 196 & 58.5 & 0.11 \\ Qwen 3 235B & 90 & 74.5 & $<0.001$ \\ GPT-4o & 40 & 80.0 & 0.006 \\ DeepSeek-V4 & 31 & 85.7 & 0.007 \\ Gemini 2.5 Flash & 8 & |
| `31` | sections/appendix.tex:309 | mean or delta | yes | en 3 235B & 90 & 74.5 & $<0.001$ \\ GPT-4o & 40 & 80.0 & 0.006 \\ DeepSeek-V4 & 31 & 85.7 & 0.007 \\ Gemini 2.5 Flash & 8 & 100.0 & 0.062 \\ \midrule  |
| `85.7` | sections/appendix.tex:309 | mean or delta | yes | 35B & 90 & 74.5 & $<0.001$ \\ GPT-4o & 40 & 80.0 & 0.006 \\ DeepSeek-V4 & 31 & 85.7 & 0.007 \\ Gemini 2.5 Flash & 8 & 100.0 & 0.062 \\ \midrule \multi |
| `0.007` | sections/appendix.tex:309 | mean or delta | yes | & 90 & 74.5 & $<0.001$ \\ GPT-4o & 40 & 80.0 & 0.006 \\ DeepSeek-V4 & 31 & 85.7 & 0.007 \\ Gemini 2.5 Flash & 8 & 100.0 & 0.062 \\ \midrule \multicolu |
| `2.5` | sections/appendix.tex:310 | mean or delta | yes | .001$ \\ GPT-4o & 40 & 80.0 & 0.006 \\ DeepSeek-V4 & 31 & 85.7 & 0.007 \\ Gemini 2.5 Flash & 8 & 100.0 & 0.062 \\ \midrule \multicolumn{4}{@{}l}{\emph |
| `8` | sections/appendix.tex:310 | mean or delta | yes | GPT-4o & 40 & 80.0 & 0.006 \\ DeepSeek-V4 & 31 & 85.7 & 0.007 \\ Gemini 2.5 Flash & 8 & 100.0 & 0.062 \\ \midrule \multicolumn{4}{@{}l}{\emph{By domai |
| `100.0` | sections/appendix.tex:310 | mean or delta | yes | o & 40 & 80.0 & 0.006 \\ DeepSeek-V4 & 31 & 85.7 & 0.007 \\ Gemini 2.5 Flash & 8 & 100.0 & 0.062 \\ \midrule \multicolumn{4}{@{}l}{\emph{By domain}} \ |
| `0.062` | sections/appendix.tex:310 | mean or delta | yes | & 40 & 80.0 & 0.006 \\ DeepSeek-V4 & 31 & 85.7 & 0.007 \\ Gemini 2.5 Flash & 8 & 100.0 & 0.062 \\ \midrule \multicolumn{4}{@{}l}{\emph{By domain}} \\  |
| `4` | sections/appendix.tex:312 | mean or delta | yes | k-V4 & 31 & 85.7 & 0.007 \\ Gemini 2.5 Flash & 8 & 100.0 & 0.062 \\ \midrule \multicolumn{4}{@{}l}{\emph{By domain}} \\ Writing & 118 & 79.1 & $<0.001 |
| `118` | sections/appendix.tex:313 | mean or delta | yes | h & 8 & 100.0 & 0.062 \\ \midrule \multicolumn{4}{@{}l}{\emph{By domain}} \\ Writing & 118 & 79.1 & $<0.001$ \\ Creative & 145 & 73.1 & $<0.001$ \\ Co |
| `79.1` | sections/appendix.tex:313 | mean or delta | yes | & 100.0 & 0.062 \\ \midrule \multicolumn{4}{@{}l}{\emph{By domain}} \\ Writing & 118 & 79.1 & $<0.001$ \\ Creative & 145 & 73.1 & $<0.001$ \\ Code & 1 |
| `0.001` | sections/appendix.tex:313 | mean or delta | yes | & 0.062 \\ \midrule \multicolumn{4}{@{}l}{\emph{By domain}} \\ Writing & 118 & 79.1 & $<0.001$ \\ Creative & 145 & 73.1 & $<0.001$ \\ Code & 196 & 67. |
| `145` | sections/appendix.tex:314 | mean or delta | yes | ticolumn{4}{@{}l}{\emph{By domain}} \\ Writing & 118 & 79.1 & $<0.001$ \\ Creative & 145 & 73.1 & $<0.001$ \\ Code & 196 & 67.0 & $<0.001$ \\ Analysis |
| `73.1` | sections/appendix.tex:314 | mean or delta | yes | mn{4}{@{}l}{\emph{By domain}} \\ Writing & 118 & 79.1 & $<0.001$ \\ Creative & 145 & 73.1 & $<0.001$ \\ Code & 196 & 67.0 & $<0.001$ \\ Analysis & 125 |
| `0.001` | sections/appendix.tex:314 | mean or delta | yes | l}{\emph{By domain}} \\ Writing & 118 & 79.1 & $<0.001$ \\ Creative & 145 & 73.1 & $<0.001$ \\ Code & 196 & 67.0 & $<0.001$ \\ Analysis & 125 & 65.9 & |
| `196` | sections/appendix.tex:315 | mean or delta | yes | ng & 118 & 79.1 & $<0.001$ \\ Creative & 145 & 73.1 & $<0.001$ \\ Code & 196 & 67.0 & $<0.001$ \\ Analysis & 125 & 65.9 & 0.024 \\ Data logic & 134 &  |
| `67.0` | sections/appendix.tex:315 | mean or delta | yes | & 118 & 79.1 & $<0.001$ \\ Creative & 145 & 73.1 & $<0.001$ \\ Code & 196 & 67.0 & $<0.001$ \\ Analysis & 125 & 65.9 & 0.024 \\ Data logic & 134 & 65. |
| `0.001` | sections/appendix.tex:315 | mean or delta | yes | 18 & 79.1 & $<0.001$ \\ Creative & 145 & 73.1 & $<0.001$ \\ Code & 196 & 67.0 & $<0.001$ \\ Analysis & 125 & 65.9 & 0.024 \\ Data logic & 134 & 65.9 & |
| `125` | sections/appendix.tex:316 | mean or delta | yes | ive & 145 & 73.1 & $<0.001$ \\ Code & 196 & 67.0 & $<0.001$ \\ Analysis & 125 & 65.9 & 0.024 \\ Data logic & 134 & 65.9 & 0.024 \\ \bottomrule \end{ta |
| `65.9` | sections/appendix.tex:316 | mean or delta | yes | & 145 & 73.1 & $<0.001$ \\ Code & 196 & 67.0 & $<0.001$ \\ Analysis & 125 & 65.9 & 0.024 \\ Data logic & 134 & 65.9 & 0.024 \\ \bottomrule \end{tabula |
| `0.024` | sections/appendix.tex:316 | mean or delta | yes | 145 & 73.1 & $<0.001$ \\ Code & 196 & 67.0 & $<0.001$ \\ Analysis & 125 & 65.9 & 0.024 \\ Data logic & 134 & 65.9 & 0.024 \\ \bottomrule \end{tabular} |
| `134` | sections/appendix.tex:317 | mean or delta | yes | de & 196 & 67.0 & $<0.001$ \\ Analysis & 125 & 65.9 & 0.024 \\ Data logic & 134 & 65.9 & 0.024 \\ \bottomrule \end{tabular} \caption{Direction of genu |
| `65.9` | sections/appendix.tex:317 | mean or delta | yes | & 196 & 67.0 & $<0.001$ \\ Analysis & 125 & 65.9 & 0.024 \\ Data logic & 134 & 65.9 & 0.024 \\ \bottomrule \end{tabular} \caption{Direction of genuine |
| `0.024` | sections/appendix.tex:317 | mean or delta | yes | & 196 & 67.0 & $<0.001$ \\ Analysis & 125 & 65.9 & 0.024 \\ Data logic & 134 & 65.9 & 0.024 \\ \bottomrule \end{tabular} \caption{Direction of genuine |
| `2` | sections/appendix.tex:322 | mean or delta | yes | ; the percentage is computed over the subset whose quality level moves. Sign test, one-sided. A $\chi^2$ test of homogeneity across the five domains d |
| `2` | sections/appendix.tex:323 | p-value | yes | , one-sided. A $\chi^2$ test of homogeneity across the five domains does not reject uniformity ($\chi^2 = 3.02$, $\mathrm{df} = 4$, $p = 0.555$).} \la |
| `3.02` | sections/appendix.tex:323 | p-value | yes | e-sided. A $\chi^2$ test of homogeneity across the five domains does not reject uniformity ($\chi^2 = 3.02$, $\mathrm{df} = 4$, $p = 0.555$).} \label{ |
| `4` | sections/appendix.tex:323 | p-value | yes | $ test of homogeneity across the five domains does not reject uniformity ($\chi^2 = 3.02$, $\mathrm{df} = 4$, $p = 0.555$).} \label{tab:direction} \en |
| `0.555` | sections/appendix.tex:323 | p-value | yes | homogeneity across the five domains does not reject uniformity ($\chi^2 = 3.02$, $\mathrm{df} = 4$, $p = 0.555$).} \label{tab:direction} \end{table} \ |
| `4.11` | sections/appendix.tex:334 | mean or delta | yes | \begin{tabular}{lcccc} \toprule Turn & Stripped & (Unstripped) & Shift & $n$ \\ \midrule T1 & 4.11 & (4.11) & 0 & 720 \\ T2 & 3.66 & (3.25) & +0.41 &  |
| `4.11` | sections/appendix.tex:334 | mean or delta | yes | abular}{lcccc} \toprule Turn & Stripped & (Unstripped) & Shift & $n$ \\ \midrule T1 & 4.11 & (4.11) & 0 & 720 \\ T2 & 3.66 & (3.25) & +0.41 & 283 \\ T |
| `0` | sections/appendix.tex:334 | mean or delta | yes | lcccc} \toprule Turn & Stripped & (Unstripped) & Shift & $n$ \\ \midrule T1 & 4.11 & (4.11) & 0 & 720 \\ T2 & 3.66 & (3.25) & +0.41 & 283 \\ T3 & 3.40 |
| `720` | sections/appendix.tex:334 | mean or delta | yes | c} \toprule Turn & Stripped & (Unstripped) & Shift & $n$ \\ \midrule T1 & 4.11 & (4.11) & 0 & 720 \\ T2 & 3.66 & (3.25) & +0.41 & 283 \\ T3 & 3.40 & ( |
| `3.66` | sections/appendix.tex:335 | mean or delta | yes | Turn & Stripped & (Unstripped) & Shift & $n$ \\ \midrule T1 & 4.11 & (4.11) & 0 & 720 \\ T2 & 3.66 & (3.25) & +0.41 & 283 \\ T3 & 3.40 & (3.01) & +0.3 |
| `3.25` | sections/appendix.tex:335 | mean or delta | yes | & Stripped & (Unstripped) & Shift & $n$ \\ \midrule T1 & 4.11 & (4.11) & 0 & 720 \\ T2 & 3.66 & (3.25) & +0.41 & 283 \\ T3 & 3.40 & (3.01) & +0.39 & 1 |
| `0.41` | sections/appendix.tex:335 | mean or delta | yes | ed & (Unstripped) & Shift & $n$ \\ \midrule T1 & 4.11 & (4.11) & 0 & 720 \\ T2 & 3.66 & (3.25) & +0.41 & 283 \\ T3 & 3.40 & (3.01) & +0.39 & 185 \\ T4 |
| `283` | sections/appendix.tex:335 | mean or delta | yes | nstripped) & Shift & $n$ \\ \midrule T1 & 4.11 & (4.11) & 0 & 720 \\ T2 & 3.66 & (3.25) & +0.41 & 283 \\ T3 & 3.40 & (3.01) & +0.39 & 185 \\ T4 & 3.34 |
| `3.40` | sections/appendix.tex:336 | mean or delta | yes | ft & $n$ \\ \midrule T1 & 4.11 & (4.11) & 0 & 720 \\ T2 & 3.66 & (3.25) & +0.41 & 283 \\ T3 & 3.40 & (3.01) & +0.39 & 185 \\ T4 & 3.34 & (2.97) & +0.3 |
| `3.01` | sections/appendix.tex:336 | mean or delta | yes | \\ \midrule T1 & 4.11 & (4.11) & 0 & 720 \\ T2 & 3.66 & (3.25) & +0.41 & 283 \\ T3 & 3.40 & (3.01) & +0.39 & 185 \\ T4 & 3.34 & (2.97) & +0.37 & 154 \ |
| `0.39` | sections/appendix.tex:336 | mean or delta | yes | midrule T1 & 4.11 & (4.11) & 0 & 720 \\ T2 & 3.66 & (3.25) & +0.41 & 283 \\ T3 & 3.40 & (3.01) & +0.39 & 185 \\ T4 & 3.34 & (2.97) & +0.37 & 154 \\ T5 |
| `185` | sections/appendix.tex:336 | mean or delta | yes | T1 & 4.11 & (4.11) & 0 & 720 \\ T2 & 3.66 & (3.25) & +0.41 & 283 \\ T3 & 3.40 & (3.01) & +0.39 & 185 \\ T4 & 3.34 & (2.97) & +0.37 & 154 \\ T5 & 3.07  |
| `3.34` | sections/appendix.tex:337 | mean or delta | yes | (4.11) & 0 & 720 \\ T2 & 3.66 & (3.25) & +0.41 & 283 \\ T3 & 3.40 & (3.01) & +0.39 & 185 \\ T4 & 3.34 & (2.97) & +0.37 & 154 \\ T5 & 3.07 & (2.85) & + |
| `2.97` | sections/appendix.tex:337 | mean or delta | yes | & 0 & 720 \\ T2 & 3.66 & (3.25) & +0.41 & 283 \\ T3 & 3.40 & (3.01) & +0.39 & 185 \\ T4 & 3.34 & (2.97) & +0.37 & 154 \\ T5 & 3.07 & (2.85) & +0.22 &  |
| `0.37` | sections/appendix.tex:337 | mean or delta | yes | \\ T2 & 3.66 & (3.25) & +0.41 & 283 \\ T3 & 3.40 & (3.01) & +0.39 & 185 \\ T4 & 3.34 & (2.97) & +0.37 & 154 \\ T5 & 3.07 & (2.85) & +0.22 & 96 \\ \mid |
| `154` | sections/appendix.tex:337 | mean or delta | yes | T2 & 3.66 & (3.25) & +0.41 & 283 \\ T3 & 3.40 & (3.01) & +0.39 & 185 \\ T4 & 3.34 & (2.97) & +0.37 & 154 \\ T5 & 3.07 & (2.85) & +0.22 & 96 \\ \midrul |
| `3.07` | sections/appendix.tex:338 | mean or delta | yes | 25) & +0.41 & 283 \\ T3 & 3.40 & (3.01) & +0.39 & 185 \\ T4 & 3.34 & (2.97) & +0.37 & 154 \\ T5 & 3.07 & (2.85) & +0.22 & 96 \\ \midrule $\Delta$ (T1- |
| `2.85` | sections/appendix.tex:338 | mean or delta | yes | .41 & 283 \\ T3 & 3.40 & (3.01) & +0.39 & 185 \\ T4 & 3.34 & (2.97) & +0.37 & 154 \\ T5 & 3.07 & (2.85) & +0.22 & 96 \\ \midrule $\Delta$ (T1--T5) & $ |
| `0.22` | sections/appendix.tex:338 | mean or delta | yes | \\ T3 & 3.40 & (3.01) & +0.39 & 185 \\ T4 & 3.34 & (2.97) & +0.37 & 154 \\ T5 & 3.07 & (2.85) & +0.22 & 96 \\ \midrule $\Delta$ (T1--T5) & $\mathbf{-1 |
| `96` | sections/appendix.tex:338 | mean or delta | yes | T3 & 3.40 & (3.01) & +0.39 & 185 \\ T4 & 3.34 & (2.97) & +0.37 & 154 \\ T5 & 3.07 & (2.85) & +0.22 & 96 \\ \midrule $\Delta$ (T1--T5) & $\mathbf{-1.04 |
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
| `1.04` | sections/appendix.tex:340 | mean or delta | yes | (2.97) & +0.37 & 154 \\ T5 & 3.07 & (2.85) & +0.22 & 96 \\ \midrule $\Delta$ (T1--T5) & $\mathbf{-1.04}$ & ($-1.26$) & & \\ \bottomrule \end{tabular}  |
| `1.26` | sections/appendix.tex:340 | mean or delta | yes | 37 & 154 \\ T5 & 3.07 & (2.85) & +0.22 & 96 \\ \midrule $\Delta$ (T1--T5) & $\mathbf{-1.04}$ & ($-1.26$) & & \\ \bottomrule \end{tabular} \caption{Poo |
| `720` | sections/appendix.tex:343 | bare number | yes | bular} \caption{Pooled mean quality by turn, restricted to genuine revisions (GENUINE-only at T2--T5, all 720 at T1). Stripped scores are primary. $n$ |
| `1.16` | sections/appendix.tex:355 | mean or delta | yes | lrrrr} \toprule Domain & Stripped & Unstr. & Shift & $n_{\text{T5}}$ \\ \midrule analysis & $-1.16$ & ($-1.21$) & +0.05 & 17 \\ code & $-1.05$ & ($-1. |
| `1.21` | sections/appendix.tex:355 | mean or delta | yes | \toprule Domain & Stripped & Unstr. & Shift & $n_{\text{T5}}$ \\ \midrule analysis & $-1.16$ & ($-1.21$) & +0.05 & 17 \\ code & $-1.05$ & ($-1.15$) &  |
| `0.05` | sections/appendix.tex:355 | mean or delta | yes | Domain & Stripped & Unstr. & Shift & $n_{\text{T5}}$ \\ \midrule analysis & $-1.16$ & ($-1.21$) & +0.05 & 17 \\ code & $-1.05$ & ($-1.15$) & +0.10 & 3 |
| `17` | sections/appendix.tex:355 | mean or delta | yes | in & Stripped & Unstr. & Shift & $n_{\text{T5}}$ \\ \midrule analysis & $-1.16$ & ($-1.21$) & +0.05 & 17 \\ code & $-1.05$ & ($-1.15$) & +0.10 & 30 \\ |
| `1.05` | sections/appendix.tex:356 | mean or delta | yes | tr. & Shift & $n_{\text{T5}}$ \\ \midrule analysis & $-1.16$ & ($-1.21$) & +0.05 & 17 \\ code & $-1.05$ & ($-1.15$) & +0.10 & 30 \\ creative & $-0.82$ |
| `1.15` | sections/appendix.tex:356 | mean or delta | yes | & $n_{\text{T5}}$ \\ \midrule analysis & $-1.16$ & ($-1.21$) & +0.05 & 17 \\ code & $-1.05$ & ($-1.15$) & +0.10 & 30 \\ creative & $-0.82$ & ($-1.22$) |
| `0.10` | sections/appendix.tex:356 | mean or delta | yes | xt{T5}}$ \\ \midrule analysis & $-1.16$ & ($-1.21$) & +0.05 & 17 \\ code & $-1.05$ & ($-1.15$) & +0.10 & 30 \\ creative & $-0.82$ & ($-1.22$) & +0.40  |
| `30` | sections/appendix.tex:356 | mean or delta | yes | $ \\ \midrule analysis & $-1.16$ & ($-1.21$) & +0.05 & 17 \\ code & $-1.05$ & ($-1.15$) & +0.10 & 30 \\ creative & $-0.82$ & ($-1.22$) & +0.40 & 19 \\ |
| `0.82` | sections/appendix.tex:357 | mean or delta | yes | nalysis & $-1.16$ & ($-1.21$) & +0.05 & 17 \\ code & $-1.05$ & ($-1.15$) & +0.10 & 30 \\ creative & $-0.82$ & ($-1.22$) & +0.40 & 19 \\ data\_logic &  |
| `1.22` | sections/appendix.tex:357 | mean or delta | yes | -1.16$ & ($-1.21$) & +0.05 & 17 \\ code & $-1.05$ & ($-1.15$) & +0.10 & 30 \\ creative & $-0.82$ & ($-1.22$) & +0.40 & 19 \\ data\_logic & $-1.01$ & ( |
| `0.40` | sections/appendix.tex:357 | mean or delta | yes | $-1.21$) & +0.05 & 17 \\ code & $-1.05$ & ($-1.15$) & +0.10 & 30 \\ creative & $-0.82$ & ($-1.22$) & +0.40 & 19 \\ data\_logic & $-1.01$ & ($-1.35$) & |
| `19` | sections/appendix.tex:357 | mean or delta | yes | ) & +0.05 & 17 \\ code & $-1.05$ & ($-1.15$) & +0.10 & 30 \\ creative & $-0.82$ & ($-1.22$) & +0.40 & 19 \\ data\_logic & $-1.01$ & ($-1.35$) & +0.34  |
| `1.01` | sections/appendix.tex:358 | mean or delta | yes | & $-1.05$ & ($-1.15$) & +0.10 & 30 \\ creative & $-0.82$ & ($-1.22$) & +0.40 & 19 \\ data\_logic & $-1.01$ & ($-1.35$) & +0.34 & 17 \\ writing & $-1.0 |
| `1.35` | sections/appendix.tex:358 | mean or delta | yes | & ($-1.15$) & +0.10 & 30 \\ creative & $-0.82$ & ($-1.22$) & +0.40 & 19 \\ data\_logic & $-1.01$ & ($-1.35$) & +0.34 & 17 \\ writing & $-1.06$ & ($-1. |
| `0.34` | sections/appendix.tex:358 | mean or delta | yes | ) & +0.10 & 30 \\ creative & $-0.82$ & ($-1.22$) & +0.40 & 19 \\ data\_logic & $-1.01$ & ($-1.35$) & +0.34 & 17 \\ writing & $-1.06$ & ($-1.31$) & +0. |
| `17` | sections/appendix.tex:358 | mean or delta | yes | 10 & 30 \\ creative & $-0.82$ & ($-1.22$) & +0.40 & 19 \\ data\_logic & $-1.01$ & ($-1.35$) & +0.34 & 17 \\ writing & $-1.06$ & ($-1.31$) & +0.25 & 13 |
| `1.06` | sections/appendix.tex:359 | mean or delta | yes | e & $-0.82$ & ($-1.22$) & +0.40 & 19 \\ data\_logic & $-1.01$ & ($-1.35$) & +0.34 & 17 \\ writing & $-1.06$ & ($-1.31$) & +0.25 & 13 \\ \bottomrule \e |
| `1.31` | sections/appendix.tex:359 | mean or delta | yes | & ($-1.22$) & +0.40 & 19 \\ data\_logic & $-1.01$ & ($-1.35$) & +0.34 & 17 \\ writing & $-1.06$ & ($-1.31$) & +0.25 & 13 \\ \bottomrule \end{tabular}  |
| `0.25` | sections/appendix.tex:359 | mean or delta | yes | $) & +0.40 & 19 \\ data\_logic & $-1.01$ & ($-1.35$) & +0.34 & 17 \\ writing & $-1.06$ & ($-1.31$) & +0.25 & 13 \\ \bottomrule \end{tabular} \caption{ |
| `13` | sections/appendix.tex:359 | mean or delta | yes | .40 & 19 \\ data\_logic & $-1.01$ & ($-1.35$) & +0.34 & 17 \\ writing & $-1.06$ & ($-1.31$) & +0.25 & 13 \\ \bottomrule \end{tabular} \caption{Quality |
| `4` | sections/appendix.tex:362 | p-value | yes | bular} \caption{Quality decline (T1--T5) by domain on stripped content. All domains show negative deltas; 4/5 are significant ($p < 0.05$), data\_logi |
| `5` | sections/appendix.tex:362 | p-value | yes | lar} \caption{Quality decline (T1--T5) by domain on stripped content. All domains show negative deltas; 4/5 are significant ($p < 0.05$), data\_logic  |
| `0.05` | sections/appendix.tex:362 | p-value | yes | y decline (T1--T5) by domain on stripped content. All domains show negative deltas; 4/5 are significant ($p < 0.05$), data\_logic marginal ($p = 0.058 |
| `0.058` | sections/appendix.tex:362 | p-value | yes | ipped content. All domains show negative deltas; 4/5 are significant ($p < 0.05$), data\_logic marginal ($p = 0.058$). Per-domain $n$(T5) limits preci |
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
| `2` | sections/appendix.tex:43 | count or denominator |  | $n = 720$), consistent with this pattern. \section{Study 2: Momentum} \label{sec:appendix-study2} Study~2 tests whether prior revision rounds shift th |
| `1,728` | sections/appendix.tex:43 | percentage |  | tudy2} Study~2 tests whether prior revision rounds shift the revision gate on a subsequent evaluative probe (1,728 trials). Without prior revision (do |
| `0` | sections/appendix.tex:43 | p-value |  | rounds shift the revision gate on a subsequent evaluative probe (1,728 trials). Without prior revision (dose~0), models revised 23.2\%; after 1--3 pri |
| `23.2` | sections/appendix.tex:43 | p-value |  | evision gate on a subsequent evaluative probe (1,728 trials). Without prior revision (dose~0), models revised 23.2\%; after 1--3 prior rounds, this ri |
| `1` | sections/appendix.tex:43 | p-value |  | n a subsequent evaluative probe (1,728 trials). Without prior revision (dose~0), models revised 23.2\%; after 1--3 prior rounds, this rises to 44.6\%  |
| `3` | sections/appendix.tex:43 | p-value |  | subsequent evaluative probe (1,728 trials). Without prior revision (dose~0), models revised 23.2\%; after 1--3 prior rounds, this rises to 44.6\% ($\c |
| `44.6` | sections/appendix.tex:43 | p-value |  | 1,728 trials). Without prior revision (dose~0), models revised 23.2\%; after 1--3 prior rounds, this rises to 44.6\% ($\chi^2 = 376.54$, $p < 0.0001$) |
| `2` | sections/appendix.tex:43 | p-value |  | Without prior revision (dose~0), models revised 23.2\%; after 1--3 prior rounds, this rises to 44.6\% ($\chi^2 = 376.54$, $p < 0.0001$). Model-level d |
| `376.54` | sections/appendix.tex:43 | p-value |  | hout prior revision (dose~0), models revised 23.2\%; after 1--3 prior rounds, this rises to 44.6\% ($\chi^2 = 376.54$, $p < 0.0001$). Model-level dive |
| `0.0001` | sections/appendix.tex:43 | p-value |  | ision (dose~0), models revised 23.2\%; after 1--3 prior rounds, this rises to 44.6\% ($\chi^2 = 376.54$, $p < 0.0001$). Model-level divergence is dram |
| `31.4` | sections/appendix.tex:47 | p-value |  | 6\% ($\chi^2 = 376.54$, $p < 0.0001$). Model-level divergence is dramatic: \begin{itemize} \item GPT-4o: 31.4\% $\to$ 98.4\% at dose~1 (near-total syc |
| `98.4` | sections/appendix.tex:47 | p-value |  | = 376.54$, $p < 0.0001$). Model-level divergence is dramatic: \begin{itemize} \item GPT-4o: 31.4\% $\to$ 98.4\% at dose~1 (near-total sycophantic shif |
| `1` | sections/appendix.tex:47 | percentage |  | 0.0001$). Model-level divergence is dramatic: \begin{itemize} \item GPT-4o: 31.4\% $\to$ 98.4\% at dose~1 (near-total sycophantic shift) \item Claude  |
| `4` | sections/appendix.tex:48 | percentage |  | emize} \item GPT-4o: 31.4\% $\to$ 98.4\% at dose~1 (near-total sycophantic shift) \item Claude Sonnet~4: 38.0\% $\to$ 24.5\% at dose~3 (declines under |
| `38.0` | sections/appendix.tex:48 | percentage |  | ze} \item GPT-4o: 31.4\% $\to$ 98.4\% at dose~1 (near-total sycophantic shift) \item Claude Sonnet~4: 38.0\% $\to$ 24.5\% at dose~3 (declines under mo |
| `24.5` | sections/appendix.tex:48 | percentage |  | GPT-4o: 31.4\% $\to$ 98.4\% at dose~1 (near-total sycophantic shift) \item Claude Sonnet~4: 38.0\% $\to$ 24.5\% at dose~3 (declines under momentum) \i |
| `3` | sections/appendix.tex:48 | percentage |  | $\to$ 98.4\% at dose~1 (near-total sycophantic shift) \item Claude Sonnet~4: 38.0\% $\to$ 24.5\% at dose~3 (declines under momentum) \item Gemini~2.5  |
| `2.5` | sections/appendix.tex:49 | percentage |  | ic shift) \item Claude Sonnet~4: 38.0\% $\to$ 24.5\% at dose~3 (declines under momentum) \item Gemini~2.5 Flash: 0.3\% $\to$ 12.8\% at dose~1 (modest  |
| `0.3` | sections/appendix.tex:49 | percentage |  | \item Claude Sonnet~4: 38.0\% $\to$ 24.5\% at dose~3 (declines under momentum) \item Gemini~2.5 Flash: 0.3\% $\to$ 12.8\% at dose~1 (modest shift from |
| `12.8` | sections/appendix.tex:49 | percentage |  | ude Sonnet~4: 38.0\% $\to$ 24.5\% at dose~3 (declines under momentum) \item Gemini~2.5 Flash: 0.3\% $\to$ 12.8\% at dose~1 (modest shift from near-zer |
| `1` | sections/appendix.tex:49 | percentage |  | 8.0\% $\to$ 24.5\% at dose~3 (declines under momentum) \item Gemini~2.5 Flash: 0.3\% $\to$ 12.8\% at dose~1 (modest shift from near-zero) \end{itemize |
| `0` | sections/appendix.tex:52 | p-value |  | t from near-zero) \end{itemize} The momentum effect is a step function: the entire shift occurs between dose~0 and dose~1, with no additional gain at  |
| `1` | sections/appendix.tex:52 | p-value |  | -zero) \end{itemize} The momentum effect is a step function: the entire shift occurs between dose~0 and dose~1, with no additional gain at higher dose |
| `0.51` | sections/appendix.tex:52 | p-value |  | ~0 and dose~1, with no additional gain at higher doses. Threshold level does not interact with momentum ($p = 0.51$). \paragraph{Reverse Momentum.} A  |
| `0.0` | sections/appendix.tex:54 | percentage |  | ack (``This looks great, no changes needed'') suppresses full revision to near-zero across all models: Gemini 0.0\%, GPT-4o 1.0\%, Claude 21.9\% (all  |
| `1.0` | sections/appendix.tex:54 | percentage |  | oks great, no changes needed'') suppresses full revision to near-zero across all models: Gemini 0.0\%, GPT-4o 1.0\%, Claude 21.9\% (all minor suggesti |
| `21.9` | sections/appendix.tex:54 | percentage |  | changes needed'') suppresses full revision to near-zero across all models: Gemini 0.0\%, GPT-4o 1.0\%, Claude 21.9\% (all minor suggestions). The gate |
| `2` | sections/appendix.tex:6 | p-value |  | 62.0\%. Chi-squared tests confirm the revision gate distribution differs significantly by probe type ($\chi^2 > 788$, $p < 0.0001$ for all models). Qu |
| `788` | sections/appendix.tex:6 | p-value |  | 0\%. Chi-squared tests confirm the revision gate distribution differs significantly by probe type ($\chi^2 > 788$, $p < 0.0001$ for all models). Quali |
| `0.0001` | sections/appendix.tex:6 | p-value |  | quared tests confirm the revision gate distribution differs significantly by probe type ($\chi^2 > 788$, $p < 0.0001$ for all models). Quality thresho |
| `0.40` | sections/appendix.tex:6 | p-value |  | $, $p < 0.0001$ for all models). Quality thresholds do not significantly affect the gate (Kruskal-Wallis $p > 0.40$ for all models). Within the leadin |
| `0.50` | sections/appendix.tex:8 | reliability or effect size |  | leading-probe condition, higher thresholds produce moderately less overcorrection (Spearman $\rho$: Gemini $-0.50$, Claude $-0.35$, GPT-4o $-0.14$), b |
| `0.35` | sections/appendix.tex:8 | reliability or effect size |  | ondition, higher thresholds produce moderately less overcorrection (Spearman $\rho$: Gemini $-0.50$, Claude $-0.35$, GPT-4o $-0.14$), but this calibra |
| `0.14` | sections/appendix.tex:8 | reliability or effect size |  | thresholds produce moderately less overcorrection (Spearman $\rho$: Gemini $-0.50$, Claude $-0.35$, GPT-4o $-0.14$), but this calibration is locked be |
| `1.01` | sections/conclusion.tex:3 | p-value |  | hat do revise get worse. The revision cliff is real ($-0.74$ levels on stripped content, balanced panel, $p = 1.01 \times 10^{-4}$), consistent across |
| `10` | sections/conclusion.tex:3 | p-value |  | e get worse. The revision cliff is real ($-0.74$ levels on stripped content, balanced panel, $p = 1.01 \times 10^{-4}$), consistent across task domain |
| `4` | sections/conclusion.tex:3 | p-value |  | worse. The revision cliff is real ($-0.74$ levels on stripped content, balanced panel, $p = 1.01 \times 10^{-4}$), consistent across task domains, and |
| `1.16` | sections/conclusion.tex:6 | p-value |  | odels tested). The fix is targeted feedback, not more turns. When told what to fix, models produce revisions 1.16 quality levels higher than generic i |
| `5.7` | sections/conclusion.tex:6 | p-value |  | urns. When told what to fix, models produce revisions 1.16 quality levels higher than generic iteration ($p = 5.7 \times 10^{-19}$). Intrinsic self-co |
| `10` | sections/conclusion.tex:6 | p-value |  | told what to fix, models produce revisions 1.16 quality levels higher than generic iteration ($p = 5.7 \times 10^{-19}$). Intrinsic self-correction, o |
| `19` | sections/conclusion.tex:6 | p-value |  | what to fix, models produce revisions 1.16 quality levels higher than generic iteration ($p = 5.7 \times 10^{-19}$). Intrinsic self-correction, on its |
| `62` | sections/discussion.tex:12 | percentage |  | und. The first is wasted generation: the quality-optimal stopping point is the first turn for every model, so 62\% of output tokens fall past it. The  |
| `3.3` | sections/introduction_v2.tex:20 | mean or delta | yes | rected revision removes content the user asked for.} One trial of the quarterly sales summary task (Llama~3.3~70B, run~3). The prompt is shown in exce |
| `3` | sections/introduction_v2.tex:20 | mean or delta | yes | on removes content the user asked for.} One trial of the quarterly sales summary task (Llama~3.3~70B, run~3). The prompt is shown in excerpt; model ou |
| `283` | sections/introduction_v2.tex:27 | bare number | yes | series is the mean over every genuine revision at that index across all six models, whose $n$ falls from 283 to 96 as models stop producing genuine re |
| `96` | sections/introduction_v2.tex:27 | bare number | yes | is the mean over every genuine revision at that index across all six models, whose $n$ falls from 283 to 96 as models stop producing genuine revisions |
| `720` | sections/introduction_v2.tex:71 | bare number |  | f what to change. Counting the initial draft, each conversation runs five turns. The design spans six models, 720 conversations and 3,600 responses. W |
| `3,600` | sections/introduction_v2.tex:71 | bare number |  | ting the initial draft, each conversation runs five turns. The design spans six models, 720 conversations and 3,600 responses. We ask whether a model  |
| `88` | sections/introduction_v2.tex:76 | percentage |  | ns and validate every quality judgment against human raters. Most of the work being revised did not need it: 88\% of the 720 first drafts are already  |
| `720` | sections/introduction_v2.tex:76 | percentage |  | ate every quality judgment against human raters. Most of the work being revised did not need it: 88\% of the 720 first drafts are already sufficient.  |
| `86.7` | sections/introduction_v2.tex:78 | percentage |  | already sufficient. Asked to improve them without direction, models mostly do not revise: by the fifth turn, 86.7\% of replies are meta-responses, res |
| `70` | sections/introduction_v2.tex:79 | percentage |  | sponses, restatements and declines presented as compliance rather than new task content. When they do revise, 70\% of the changes that move quality mo |
| `50` | sections/introduction_v2.tex:80 | p-value |  | rather than new task content. When they do revise, 70\% of the changes that move quality move it down. On the 50 trials that revise at every turn, qua |
| `0.74` | sections/introduction_v2.tex:80 | p-value |  | 70\% of the changes that move quality move it down. On the 50 trials that revise at every turn, quality falls 0.74 levels from first to fifth ($p = 1. |
| `1.01` | sections/introduction_v2.tex:81 | p-value |  | move it down. On the 50 trials that revise at every turn, quality falls 0.74 levels from first to fifth ($p = 1.01 \times 10^{-4}$), a decline that is |
| `10` | sections/introduction_v2.tex:81 | p-value |  | . On the 50 trials that revise at every turn, quality falls 0.74 levels from first to fifth ($p = 1.01 \times 10^{-4}$), a decline that is negative in |
| `4` | sections/introduction_v2.tex:81 | p-value |  | the 50 trials that revise at every turn, quality falls 0.74 levels from first to fifth ($p = 1.01 \times 10^{-4}$), a decline that is negative in all  |
| `62.1` | sections/introduction_v2.tex:83 | percentage |  | ty-optimal stopping point, and we name the tokens spent past it the \textbf{revision tax}, which accounts for 62.1\% of all output generated. The fail |
| `1.16` | sections/introduction_v2.tex:86 | p-value |  | ne of direction rather than capacity: a single specific critique reverses the decline, lifting revised output 1.16 levels above undirected iteration ( |
| `5.7` | sections/introduction_v2.tex:87 | p-value |  | e specific critique reverses the decline, lifting revised output 1.16 levels above undirected iteration ($p = 5.7 \times 10^{-19}$). Blind readers sho |
| `10` | sections/introduction_v2.tex:87 | p-value |  | critique reverses the decline, lifting revised output 1.16 levels above undirected iteration ($p = 5.7 \times 10^{-19}$). Blind readers shown the firs |
| `19` | sections/introduction_v2.tex:87 | p-value |  | que reverses the decline, lifting revised output 1.16 levels above undirected iteration ($p = 5.7 \times 10^{-19}$). Blind readers shown the first and |
| `56` | sections/introduction_v2.tex:88 | p-value |  | cted iteration ($p = 5.7 \times 10^{-19}$). Blind readers shown the first and last drafts prefer the first in 56\% of decisions, an interval that incl |
| `3.3` | sections/limitations.tex:3 | count or denominator |  | ion{Limitations} Several limitations qualify these findings. First, the balanced panel is dominated by Llama~3.3~70B ($n = 45$ of 50); other models ex |
| `45` | sections/limitations.tex:3 | count or denominator |  | s} Several limitations qualify these findings. First, the balanced panel is dominated by Llama~3.3~70B ($n = 45$ of 50); other models exit the revisio |
| `50` | sections/limitations.tex:3 | count or denominator |  | eral limitations qualify these findings. First, the balanced panel is dominated by Llama~3.3~70B ($n = 45$ of 50); other models exit the revision pool |
| `4` | sections/limitations.tex:3 | bare number |  | exit the revision pool too quickly for powered within-model comparison. Second, the evaluator (Claude Sonnet~4) judges outputs from all models includi |
| `0.505` | sections/limitations.tex:3 | reliability or effect size |  | mitigate this through six-model calibration selecting the highest human-correlation evaluator (Spearman $r = 0.505$, QW $\kappa = 0.526$). Third, inte |
| `0.526` | sections/limitations.tex:3 | reliability or effect size |  | h six-model calibration selecting the highest human-correlation evaluator (Spearman $r = 0.505$, QW $\kappa = 0.526$). Third, inter-rater reliability  |
| `0.41` | sections/limitations.tex:3 | reliability or effect size |  | $r = 0.505$, QW $\kappa = 0.526$). Third, inter-rater reliability is moderate (quadratic-weighted $\kappa$ = 0.41--0.60 across three rater pairs; Krip |
| `0.60` | sections/limitations.tex:3 | reliability or effect size |  | 0.505$, QW $\kappa = 0.526$). Third, inter-rater reliability is moderate (quadratic-weighted $\kappa$ = 0.41--0.60 across three rater pairs; Krippendo |
| `0.529` | sections/limitations.tex:3 | reliability or effect size |  | lity is moderate (quadratic-weighted $\kappa$ = 0.41--0.60 across three rater pairs; Krippendorff's $\alpha = 0.529$, $n = 64$). Fourth, all trials us |
| `64` | sections/limitations.tex:3 | reliability or effect size |  | ate (quadratic-weighted $\kappa$ = 0.41--0.60 across three rater pairs; Krippendorff's $\alpha = 0.529$, $n = 64$). Fourth, all trials used temperatur |
| `1.0` | sections/limitations.tex:3 | reliability or effect size |  | .60 across three rater pairs; Krippendorff's $\alpha = 0.529$, $n = 64$). Fourth, all trials used temperature~1.0; revision behavior at lower temperat |
| `40` | sections/limitations.tex:3 | mean or delta |  | 64$). Fourth, all trials used temperature~1.0; revision behavior at lower temperatures may differ. Fifth, our 40 tasks represent a convenience sample  |
| `5` | sections/limitations.tex:3 | bare number |  | provide a stronger baseline. Seventh, our per-domain quality estimates rest on small per-domain samples: Turn-5 genuine-revision cells range from 13 t |
| `13` | sections/limitations.tex:3 | bare number |  | , our per-domain quality estimates rest on small per-domain samples: Turn-5 genuine-revision cells range from 13 to 30 trials, and only the code domai |
| `30` | sections/limitations.tex:3 | bare number |  | per-domain quality estimates rest on small per-domain samples: Turn-5 genuine-revision cells range from 13 to 30 trials, and only the code domain clea |
| `8` | sections/methods.tex:20 | bare number | yes | begin{tabular}{@{}lrl@{}} \toprule \textbf{Domain} & \textbf{$n$} & \textbf{Example tasks} \\ \midrule Code & 8 & Debounce function, email validator \ |
| `8` | sections/methods.tex:21 | bare number | yes | extbf{$n$} & \textbf{Example tasks} \\ \midrule Code & 8 & Debounce function, email validator \\ Data logic & 8 & Discount stacking, scheduling \\ Ana |
| `8` | sections/methods.tex:22 | bare number | yes | Code & 8 & Debounce function, email validator \\ Data logic & 8 & Discount stacking, scheduling \\ Analysis & 8 & Quarterly sales summary, policy memo |
| `8` | sections/methods.tex:23 | bare number | yes | logic & 8 & Discount stacking, scheduling \\ Analysis & 8 & Quarterly sales summary, policy memo \\ Writing & 8 & PTO request, LinkedIn announcement \ |
| `8` | sections/methods.tex:24 | bare number | yes | & 8 & Quarterly sales summary, policy memo \\ Writing & 8 & PTO request, LinkedIn announcement \\ Creative & 8 & Story opening, tone rewrite \\ \botto |
| `8` | sections/methods.tex:27 | bare number | yes | ve & 8 & Story opening, tone rewrite \\ \bottomrule \end{tabular} \caption{Task domains. Each domain contains 8 scenarios spanning typical enterprise  |
| `2` | sections/methods.tex:34 | bare number |  | domains} \end{table} \subsection{Response Classification} \label{sec:methods-classifier} At each turn $\geq 2$, the model's response is classified as  |
| `1.4` | sections/methods.tex:34 | percentage |  | ssifier's higher rate. Ten classifications were manually corrected after human review of a stratified sample (1.4\% correction rate). The classifier g |
| `64` | sections/methods.tex:50 | p-value |  | scale. \paragraph{Evaluator Calibration.} Six candidate evaluators were scored against three human raters on 64 stratified samples; Claude Sonnet~4 ha |
| `64` | sections/methods.tex:55 | bare number |  | {sec:evaluator-calibration} reports all six. \paragraph{Human Validation.} Three raters independently scored 64 stratified samples on the same scale ( |
| `6` | sections/methods.tex:55 | reliability or effect size |  | \paragraph{Human Validation.} Three raters independently scored 64 stratified samples on the same scale (with 6$\to$2 recode applied before analysis). |
| `2` | sections/methods.tex:55 | reliability or effect size |  | raph{Human Validation.} Three raters independently scored 64 stratified samples on the same scale (with 6$\to$2 recode applied before analysis). Pairw |
| `0.406` | sections/methods.tex:55 | reliability or effect size |  | scale (with 6$\to$2 recode applied before analysis). Pairwise quadratic-weighted Cohen's $\kappa$ ranges from 0.406 to 0.603; Krippendorff's $\alpha = |
| `0.603` | sections/methods.tex:55 | reliability or effect size |  | th 6$\to$2 recode applied before analysis). Pairwise quadratic-weighted Cohen's $\kappa$ ranges from 0.406 to 0.603; Krippendorff's $\alpha = 0.529$ ( |
| `50` | sections/methods.tex:60 | percentage |  | revised version...'') and postambles (``Let me know if you'd like any changes'') to revision outputs. In our 50 balanced-panel pairs, 84\% of revision |
| `3,600` | sections/methods.tex:62 | bare number |  | rdone'' criterion on boilerplate rather than content. To control for this, we strip meta-commentary from all 3,600 outputs using validated regex patte |
| `3,600` | sections/methods.tex:62 | percentage |  | from all 3,600 outputs using validated regex patterns matching common preamble and postamble phrases. Of the 3,600 outputs, 1,200 (33.3\%) were modifi |
| `1,200` | sections/methods.tex:62 | percentage |  | outputs using validated regex patterns matching common preamble and postamble phrases. Of the 3,600 outputs, 1,200 (33.3\%) were modified by stripping |
| `33.3` | sections/methods.tex:62 | percentage |  | s using validated regex patterns matching common preamble and postamble phrases. Of the 3,600 outputs, 1,200 (33.3\%) were modified by stripping and r |
| `4` | sections/methods.tex:62 | percentage |  | tamble phrases. Of the 3,600 outputs, 1,200 (33.3\%) were modified by stripping and rescored by Claude Sonnet~4 at temperature~0 using the identical e |
| `0` | sections/methods.tex:62 | percentage |  | f the 3,600 outputs, 1,200 (33.3\%) were modified by stripping and rescored by Claude Sonnet~4 at temperature~0 using the identical evaluation prompt. |
| `50` | sections/methods.tex:62 | reliability or effect size |  | ng and rescored by Claude Sonnet~4 at temperature~0 using the identical evaluation prompt. Validation: on the 50 balanced-panel pairs, two human annot |
| `0.569` | sections/methods.tex:62 | reliability or effect size |  | 50 balanced-panel pairs, two human annotators rating stripped content agreed with the evaluator at $\kappa = 0.569$, compared to near-chance agreement |
| `6` | sections/methods.tex:7 | bare number |  | estimate of behaviour under the revision-implying prompts that dominate in practice. The experiment crosses 6 models $\times$ 40 scenarios $\times$ 3  |
| `40` | sections/methods.tex:7 | bare number |  | iour under the revision-implying prompts that dominate in practice. The experiment crosses 6 models $\times$ 40 scenarios $\times$ 3 runs $=$ \textbf{ |
| `3` | sections/methods.tex:7 | mean or delta |  | n-implying prompts that dominate in practice. The experiment crosses 6 models $\times$ 40 scenarios $\times$ 3 runs $=$ \textbf{720 trials} (3,600 mod |
| `720` | sections/methods.tex:7 | mean or delta |  | that dominate in practice. The experiment crosses 6 models $\times$ 40 scenarios $\times$ 3 runs $=$ \textbf{720 trials} (3,600 model-turn observation |
| `3,600` | sections/methods.tex:7 | mean or delta |  | in practice. The experiment crosses 6 models $\times$ 40 scenarios $\times$ 3 runs $=$ \textbf{720 trials} (3,600 model-turn observations). All genera |
| `1.0` | sections/methods.tex:7 | mean or delta |  | rios $\times$ 3 runs $=$ \textbf{720 trials} (3,600 model-turn observations). All generation uses temperature~1.0, to maximize output diversity and av |
| `177` | sections/methods.tex:78 | count or denominator |  | ch is then blind-evaluated. This tests whether specific feedback outperforms the generic revision probe ($n = 177$ paired comparisons after filtering  |
| `4` | sections/methods.tex:9 | mean or delta |  | no-probe control would be needed to isolate the revision mechanism alone. \paragraph{Models.} Claude Sonnet~4 (Anthropic), GPT-4o (OpenAI), Gemini~2.5 |
| `2.5` | sections/methods.tex:9 | mean or delta |  | olate the revision mechanism alone. \paragraph{Models.} Claude Sonnet~4 (Anthropic), GPT-4o (OpenAI), Gemini~2.5 Flash (Google), Llama~3.3~70B (Meta,  |
| `3.3` | sections/methods.tex:9 | mean or delta |  | sm alone. \paragraph{Models.} Claude Sonnet~4 (Anthropic), GPT-4o (OpenAI), Gemini~2.5 Flash (Google), Llama~3.3~70B (Meta, via Together AI), Qwen~3~2 |
| `3` | sections/methods.tex:9 | mean or delta |  | Sonnet~4 (Anthropic), GPT-4o (OpenAI), Gemini~2.5 Flash (Google), Llama~3.3~70B (Meta, via Together AI), Qwen~3~235B (Alibaba, via OpenRouter), and De |
| `71.9` | sections/results_v2.tex:101 | count or denominator |  | stant, model identity explains far more variation in genuine-revision rate than task domain: a model range of 71.9 percentage points against a domain  |
| `13.5` | sections/results_v2.tex:102 | reliability or effect size |  | in genuine-revision rate than task domain: a model range of 71.9 percentage points against a domain range of 13.5. All five domains show negative stri |
| `631` | sections/results_v2.tex:108 | percentage |  | ). \paragraph{Revision despite sufficiency.} The evaluator rated 87.6\% of first-turn outputs as sufficient (631/720), so most trials begin with work  |
| `720` | sections/results_v2.tex:108 | percentage |  | \paragraph{Revision despite sufficiency.} The evaluator rated 87.6\% of first-turn outputs as sufficient (631/720), so most trials begin with work tha |
| `0.74` | sections/results_v2.tex:132 | count or denominator |  | rst draft. This bounds what the degradation means in practice without touching what it measures. The drop of 0.74 levels is not large enough to revers |
| `4.68` | sections/results_v2.tex:139 | p-value |  | n, substantially improves it; we call these targeted revisions. On stripped content, targeted revisions score 4.68 against 3.53 for the model's own ge |
| `3.53` | sections/results_v2.tex:139 | p-value |  | lly improves it; we call these targeted revisions. On stripped content, targeted revisions score 4.68 against 3.53 for the model's own generic next-tu |
| `1.16` | sections/results_v2.tex:139 | p-value |  | content, targeted revisions score 4.68 against 3.53 for the model's own generic next-turn revision, a gain of 1.16 levels ($p = 5.7 \times 10^{-19}$,  |
| `5.7` | sections/results_v2.tex:139 | p-value |  | revisions score 4.68 against 3.53 for the model's own generic next-turn revision, a gain of 1.16 levels ($p = 5.7 \times 10^{-19}$, $n = 177$; unstrip |
| `10` | sections/results_v2.tex:139 | p-value |  | core 4.68 against 3.53 for the model's own generic next-turn revision, a gain of 1.16 levels ($p = 5.7 \times 10^{-19}$, $n = 177$; unstripped: 4.68 a |
| `19` | sections/results_v2.tex:139 | p-value |  | 4.68 against 3.53 for the model's own generic next-turn revision, a gain of 1.16 levels ($p = 5.7 \times 10^{-19}$, $n = 177$; unstripped: 4.68 agains |
| `177` | sections/results_v2.tex:139 | p-value |  | t 3.53 for the model's own generic next-turn revision, a gain of 1.16 levels ($p = 5.7 \times 10^{-19}$, $n = 177$; unstripped: 4.68 against 4.43, $+0 |
| `4.68` | sections/results_v2.tex:139 | p-value |  | el's own generic next-turn revision, a gain of 1.16 levels ($p = 5.7 \times 10^{-19}$, $n = 177$; unstripped: 4.68 against 4.43, $+0.25$, $p = 0.004$) |
| `4.43` | sections/results_v2.tex:139 | p-value |  | ric next-turn revision, a gain of 1.16 levels ($p = 5.7 \times 10^{-19}$, $n = 177$; unstripped: 4.68 against 4.43, $+0.25$, $p = 0.004$). The unstrip |
| `0.25` | sections/results_v2.tex:139 | p-value |  | -turn revision, a gain of 1.16 levels ($p = 5.7 \times 10^{-19}$, $n = 177$; unstripped: 4.68 against 4.43, $+0.25$, $p = 0.004$). The unstripped comp |
| `0.004` | sections/results_v2.tex:139 | p-value |  | on, a gain of 1.16 levels ($p = 5.7 \times 10^{-19}$, $n = 177$; unstripped: 4.68 against 4.43, $+0.25$, $p = 0.004$). The unstripped comparison under |
| `3.3` | sections/results_v2.tex:150 | p-value | yes | ll \begin{tabular}{lccc} \toprule Model & $n$ & Stripped $\Delta$ & $p$ \\ \midrule Llama 3.3 70B & 71 & $+1.62$ & $9.2 \times 10^{-12}$ \\ Qwen 3 235 |
| `71` | sections/results_v2.tex:150 | p-value | yes | gin{tabular}{lccc} \toprule Model & $n$ & Stripped $\Delta$ & $p$ \\ \midrule Llama 3.3 70B & 71 & $+1.62$ & $9.2 \times 10^{-12}$ \\ Qwen 3 235B & 21 |
| `1.62` | sections/results_v2.tex:150 | p-value | yes | ular}{lccc} \toprule Model & $n$ & Stripped $\Delta$ & $p$ \\ \midrule Llama 3.3 70B & 71 & $+1.62$ & $9.2 \times 10^{-12}$ \\ Qwen 3 235B & 21 & $+1. |
| `9.2` | sections/results_v2.tex:150 | p-value | yes | c} \toprule Model & $n$ & Stripped $\Delta$ & $p$ \\ \midrule Llama 3.3 70B & 71 & $+1.62$ & $9.2 \times 10^{-12}$ \\ Qwen 3 235B & 21 & $+1.48$ & $4. |
| `10` | sections/results_v2.tex:150 | p-value | yes | rule Model & $n$ & Stripped $\Delta$ & $p$ \\ \midrule Llama 3.3 70B & 71 & $+1.62$ & $9.2 \times 10^{-12}$ \\ Qwen 3 235B & 21 & $+1.48$ & $4.5 \time |
| `12` | sections/results_v2.tex:150 | p-value | yes | Model & $n$ & Stripped $\Delta$ & $p$ \\ \midrule Llama 3.3 70B & 71 & $+1.62$ & $9.2 \times 10^{-12}$ \\ Qwen 3 235B & 21 & $+1.48$ & $4.5 \times 10^ |
| `3` | sections/results_v2.tex:151 | p-value | yes | Stripped $\Delta$ & $p$ \\ \midrule Llama 3.3 70B & 71 & $+1.62$ & $9.2 \times 10^{-12}$ \\ Qwen 3 235B & 21 & $+1.48$ & $4.5 \times 10^{-4}$ \\ GPT-4 |
| `21` | sections/results_v2.tex:151 | p-value | yes | $\Delta$ & $p$ \\ \midrule Llama 3.3 70B & 71 & $+1.62$ & $9.2 \times 10^{-12}$ \\ Qwen 3 235B & 21 & $+1.48$ & $4.5 \times 10^{-4}$ \\ GPT-4o & 12 &  |
| `1.48` | sections/results_v2.tex:151 | p-value | yes | a$ & $p$ \\ \midrule Llama 3.3 70B & 71 & $+1.62$ & $9.2 \times 10^{-12}$ \\ Qwen 3 235B & 21 & $+1.48$ & $4.5 \times 10^{-4}$ \\ GPT-4o & 12 & $+1.33 |
| `4.5` | sections/results_v2.tex:151 | p-value | yes | \\ \midrule Llama 3.3 70B & 71 & $+1.62$ & $9.2 \times 10^{-12}$ \\ Qwen 3 235B & 21 & $+1.48$ & $4.5 \times 10^{-4}$ \\ GPT-4o & 12 & $+1.33$ & $7.8  |
| `10` | sections/results_v2.tex:151 | p-value | yes | rule Llama 3.3 70B & 71 & $+1.62$ & $9.2 \times 10^{-12}$ \\ Qwen 3 235B & 21 & $+1.48$ & $4.5 \times 10^{-4}$ \\ GPT-4o & 12 & $+1.33$ & $7.8 \times  |
| `4` | sections/results_v2.tex:151 | p-value | yes | Llama 3.3 70B & 71 & $+1.62$ & $9.2 \times 10^{-12}$ \\ Qwen 3 235B & 21 & $+1.48$ & $4.5 \times 10^{-4}$ \\ GPT-4o & 12 & $+1.33$ & $7.8 \times 10^{- |
| `12` | sections/results_v2.tex:152 | p-value | yes | 71 & $+1.62$ & $9.2 \times 10^{-12}$ \\ Qwen 3 235B & 21 & $+1.48$ & $4.5 \times 10^{-4}$ \\ GPT-4o & 12 & $+1.33$ & $7.8 \times 10^{-3}$ \\ DeepSeek  |
| `1.33` | sections/results_v2.tex:152 | p-value | yes | 1.62$ & $9.2 \times 10^{-12}$ \\ Qwen 3 235B & 21 & $+1.48$ & $4.5 \times 10^{-4}$ \\ GPT-4o & 12 & $+1.33$ & $7.8 \times 10^{-3}$ \\ DeepSeek V4 & 19 |
| `7.8` | sections/results_v2.tex:152 | p-value | yes | 9.2 \times 10^{-12}$ \\ Qwen 3 235B & 21 & $+1.48$ & $4.5 \times 10^{-4}$ \\ GPT-4o & 12 & $+1.33$ & $7.8 \times 10^{-3}$ \\ DeepSeek V4 & 19 & $+1.05 |
| `10` | sections/results_v2.tex:152 | p-value | yes | 10^{-12}$ \\ Qwen 3 235B & 21 & $+1.48$ & $4.5 \times 10^{-4}$ \\ GPT-4o & 12 & $+1.33$ & $7.8 \times 10^{-3}$ \\ DeepSeek V4 & 19 & $+1.05$ & $1.2 \t |
| `3` | sections/results_v2.tex:152 | p-value | yes | 12}$ \\ Qwen 3 235B & 21 & $+1.48$ & $4.5 \times 10^{-4}$ \\ GPT-4o & 12 & $+1.33$ & $7.8 \times 10^{-3}$ \\ DeepSeek V4 & 19 & $+1.05$ & $1.2 \times  |
| `19` | sections/results_v2.tex:153 | p-value | yes | 21 & $+1.48$ & $4.5 \times 10^{-4}$ \\ GPT-4o & 12 & $+1.33$ & $7.8 \times 10^{-3}$ \\ DeepSeek V4 & 19 & $+1.05$ & $1.2 \times 10^{-2}$ \\ Claude Son |
| `1.05` | sections/results_v2.tex:153 | p-value | yes | +1.48$ & $4.5 \times 10^{-4}$ \\ GPT-4o & 12 & $+1.33$ & $7.8 \times 10^{-3}$ \\ DeepSeek V4 & 19 & $+1.05$ & $1.2 \times 10^{-2}$ \\ Claude Sonnet 4  |
| `1.2` | sections/results_v2.tex:153 | p-value | yes | $4.5 \times 10^{-4}$ \\ GPT-4o & 12 & $+1.33$ & $7.8 \times 10^{-3}$ \\ DeepSeek V4 & 19 & $+1.05$ & $1.2 \times 10^{-2}$ \\ Claude Sonnet 4 & 51 & $+ |
| `10` | sections/results_v2.tex:153 | p-value | yes | 10^{-4}$ \\ GPT-4o & 12 & $+1.33$ & $7.8 \times 10^{-3}$ \\ DeepSeek V4 & 19 & $+1.05$ & $1.2 \times 10^{-2}$ \\ Claude Sonnet 4 & 51 & $+0.31$ & $1.2 |
| `2` | sections/results_v2.tex:153 | p-value | yes | -4}$ \\ GPT-4o & 12 & $+1.33$ & $7.8 \times 10^{-3}$ \\ DeepSeek V4 & 19 & $+1.05$ & $1.2 \times 10^{-2}$ \\ Claude Sonnet 4 & 51 & $+0.31$ & $1.2 \ti |
| `4` | sections/results_v2.tex:154 | p-value | yes | $+1.33$ & $7.8 \times 10^{-3}$ \\ DeepSeek V4 & 19 & $+1.05$ & $1.2 \times 10^{-2}$ \\ Claude Sonnet 4 & 51 & $+0.31$ & $1.2 \times 10^{-2}$ \\ Gemini |
| `51` | sections/results_v2.tex:154 | p-value | yes | .33$ & $7.8 \times 10^{-3}$ \\ DeepSeek V4 & 19 & $+1.05$ & $1.2 \times 10^{-2}$ \\ Claude Sonnet 4 & 51 & $+0.31$ & $1.2 \times 10^{-2}$ \\ Gemini 2. |
| `0.31` | sections/results_v2.tex:154 | p-value | yes | $7.8 \times 10^{-3}$ \\ DeepSeek V4 & 19 & $+1.05$ & $1.2 \times 10^{-2}$ \\ Claude Sonnet 4 & 51 & $+0.31$ & $1.2 \times 10^{-2}$ \\ Gemini 2.5 Flash |
| `1.2` | sections/results_v2.tex:154 | p-value | yes | es 10^{-3}$ \\ DeepSeek V4 & 19 & $+1.05$ & $1.2 \times 10^{-2}$ \\ Claude Sonnet 4 & 51 & $+0.31$ & $1.2 \times 10^{-2}$ \\ Gemini 2.5 Flash & 3 & $+ |
| `10` | sections/results_v2.tex:154 | p-value | yes | \\ DeepSeek V4 & 19 & $+1.05$ & $1.2 \times 10^{-2}$ \\ Claude Sonnet 4 & 51 & $+0.31$ & $1.2 \times 10^{-2}$ \\ Gemini 2.5 Flash & 3 & $+2.33$ & -- ( |
| `2` | sections/results_v2.tex:154 | p-value | yes | DeepSeek V4 & 19 & $+1.05$ & $1.2 \times 10^{-2}$ \\ Claude Sonnet 4 & 51 & $+0.31$ & $1.2 \times 10^{-2}$ \\ Gemini 2.5 Flash & 3 & $+2.33$ & -- ($n  |
| `2.5` | sections/results_v2.tex:155 | p-value | yes | 9 & $+1.05$ & $1.2 \times 10^{-2}$ \\ Claude Sonnet 4 & 51 & $+0.31$ & $1.2 \times 10^{-2}$ \\ Gemini 2.5 Flash & 3 & $+2.33$ & -- ($n < 5$) \\ \botto |
| `3` | sections/results_v2.tex:155 | p-value | yes | & $1.2 \times 10^{-2}$ \\ Claude Sonnet 4 & 51 & $+0.31$ & $1.2 \times 10^{-2}$ \\ Gemini 2.5 Flash & 3 & $+2.33$ & -- ($n < 5$) \\ \bottomrule \end{t |
| `2.33` | sections/results_v2.tex:155 | p-value | yes | \times 10^{-2}$ \\ Claude Sonnet 4 & 51 & $+0.31$ & $1.2 \times 10^{-2}$ \\ Gemini 2.5 Flash & 3 & $+2.33$ & -- ($n < 5$) \\ \bottomrule \end{tabular} |
| `5` | sections/results_v2.tex:155 | p-value | yes | \\ Claude Sonnet 4 & 51 & $+0.31$ & $1.2 \times 10^{-2}$ \\ Gemini 2.5 Flash & 3 & $+2.33$ & -- ($n < 5$) \\ \bottomrule \end{tabular} \caption{Target |
| `0.74` | sections/results_v2.tex:162 | mean or delta |  | en undirected and directed revision is the central practical finding: undirected revision degrades quality by 0.74 levels over five turns, while a sin |
| `1.16` | sections/results_v2.tex:162 | mean or delta |  | ted revision degrades quality by 0.74 levels over five turns, while a single directed revision improves it by 1.16 levels. The problem is not revision |
| `81.3` | sections/results_v2.tex:172 | percentage |  | -tax}). Per-model waste ranges from 23.4\% (Gemini, which declines early and generates few post-T1 tokens) to 81.3\% (Llama, which continues revising  |
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
| `50` | sections/results_v2.tex:38 | percentage |  | s} shows the per-model survival curves; only Llama sustains revision to the final turn. The balanced panel of 50 trials with genuine revision at all t |
| `45` | sections/results_v2.tex:38 | percentage |  | revision to the final turn. The balanced panel of 50 trials with genuine revision at all turns is composed of 45 Llama trials (90\%), 3 Qwen, and 2 Cl |
| `90` | sections/results_v2.tex:38 | percentage |  | inal turn. The balanced panel of 50 trials with genuine revision at all turns is composed of 45 Llama trials (90\%), 3 Qwen, and 2 Claude; GPT-4o, Dee |
| `3` | sections/results_v2.tex:38 | percentage |  | rn. The balanced panel of 50 trials with genuine revision at all turns is composed of 45 Llama trials (90\%), 3 Qwen, and 2 Claude; GPT-4o, DeepSeek,  |
| `2` | sections/results_v2.tex:38 | percentage |  | nced panel of 50 trials with genuine revision at all turns is composed of 45 Llama trials (90\%), 3 Qwen, and 2 Claude; GPT-4o, DeepSeek, and Gemini c |
| `718` | sections/results_v2.tex:57 | percentage |  | Under Undirected Revision} \paragraph{Revisions lower quality more often than they raise it.} Across all 718 genuine revisions, a revision leaves the  |
| `60.2` | sections/results_v2.tex:57 | percentage |  | often than they raise it.} Across all 718 genuine revisions, a revision leaves the quality level unchanged in 60.2\% of cases, lowers it in 27.7\%, an |
| `27.7` | sections/results_v2.tex:58 | percentage |  | oss all 718 genuine revisions, a revision leaves the quality level unchanged in 60.2\% of cases, lowers it in 27.7\%, and raises it in 12.1\%. Restric |
| `12.1` | sections/results_v2.tex:58 | percentage |  | ions, a revision leaves the quality level unchanged in 60.2\% of cases, lowers it in 27.7\%, and raises it in 12.1\%. Restricting to the 286 revisions |
| `286` | sections/results_v2.tex:58 | percentage |  | quality level unchanged in 60.2\% of cases, lowers it in 27.7\%, and raises it in 12.1\%. Restricting to the 286 revisions that move the level at all, |
| `199` | sections/results_v2.tex:59 | p-value |  | s, lowers it in 27.7\%, and raises it in 12.1\%. Restricting to the 286 revisions that move the level at all, 199 move it down and 87 move it up, a sh |
| `87` | sections/results_v2.tex:59 | p-value |  | %, and raises it in 12.1\%. Restricting to the 286 revisions that move the level at all, 199 move it down and 87 move it up, a share of 69.6\% (exact  |
| `69.6` | sections/results_v2.tex:59 | p-value |  | . Restricting to the 286 revisions that move the level at all, 199 move it down and 87 move it up, a share of 69.6\% (exact binomial 95\% CI $[63.9\%, |
| `95` | sections/results_v2.tex:60 | p-value |  | 6 revisions that move the level at all, 199 move it down and 87 move it up, a share of 69.6\% (exact binomial 95\% CI $[63.9\%, 74.9\%]$; sign test $p |
| `63.9` | sections/results_v2.tex:60 | p-value |  | s that move the level at all, 199 move it down and 87 move it up, a share of 69.6\% (exact binomial 95\% CI $[63.9\%, 74.9\%]$; sign test $p = 1.48 \t |
| `74.9` | sections/results_v2.tex:60 | p-value |  | ove the level at all, 199 move it down and 87 move it up, a share of 69.6\% (exact binomial 95\% CI $[63.9\%, 74.9\%]$; sign test $p = 1.48 \times 10^ |
| `1.48` | sections/results_v2.tex:60 | p-value |  | move it down and 87 move it up, a share of 69.6\% (exact binomial 95\% CI $[63.9\%, 74.9\%]$; sign test $p = 1.48 \times 10^{-11}$). Of the 411 revisi |
| `10` | sections/results_v2.tex:60 | p-value |  | n and 87 move it up, a share of 69.6\% (exact binomial 95\% CI $[63.9\%, 74.9\%]$; sign test $p = 1.48 \times 10^{-11}$). Of the 411 revisions whose i |
| `11` | sections/results_v2.tex:60 | p-value |  | 87 move it up, a share of 69.6\% (exact binomial 95\% CI $[63.9\%, 74.9\%]$; sign test $p = 1.48 \times 10^{-11}$). Of the 411 revisions whose input w |
| `411` | sections/results_v2.tex:60 | p-value |  | , a share of 69.6\% (exact binomial 95\% CI $[63.9\%, 74.9\%]$; sign test $p = 1.48 \times 10^{-11}$). Of the 411 revisions whose input was already at |
| `0.11` | sections/results_v2.tex:63 | p-value |  | . It is significant in four of the six models individually; Claude Sonnet~4 does not reach significance ($p = 0.11$) and Gemini~2.5~Flash contributes  |
| `2.5` | sections/results_v2.tex:64 | p-value |  | t in four of the six models individually; Claude Sonnet~4 does not reach significance ($p = 0.11$) and Gemini~2.5~Flash contributes only eight genuine |
| `76.6` | sections/results_v2.tex:64 | p-value |  | nce ($p = 0.11$) and Gemini~2.5~Flash contributes only eight genuine revisions. Unstripped, the same share is 76.6\% (245 against 75, $p = 1.7 \times  |
| `245` | sections/results_v2.tex:65 | p-value |  | = 0.11$) and Gemini~2.5~Flash contributes only eight genuine revisions. Unstripped, the same share is 76.6\% (245 against 75, $p = 1.7 \times 10^{-22} |
| `75` | sections/results_v2.tex:65 | p-value |  | Gemini~2.5~Flash contributes only eight genuine revisions. Unstripped, the same share is 76.6\% (245 against 75, $p = 1.7 \times 10^{-22}$). \paragrap |
| `1.7` | sections/results_v2.tex:65 | p-value |  | .5~Flash contributes only eight genuine revisions. Unstripped, the same share is 76.6\% (245 against 75, $p = 1.7 \times 10^{-22}$). \paragraph{The ef |
| `10` | sections/results_v2.tex:65 | p-value |  | ntributes only eight genuine revisions. Unstripped, the same share is 76.6\% (245 against 75, $p = 1.7 \times 10^{-22}$). \paragraph{The effect depend |
| `22` | sections/results_v2.tex:65 | p-value |  | utes only eight genuine revisions. Unstripped, the same share is 76.6\% (245 against 75, $p = 1.7 \times 10^{-22}$). \paragraph{The effect depends on  |
| `194` | sections/results_v2.tex:71 | count or denominator |  | c:supp-figures}): revision raises quality when the input falls below the sufficiency threshold ($+0.41$, $n = 194$) and lowers it when the input is al |
| `0.56` | sections/results_v2.tex:72 | count or denominator |  | ls below the sufficiency threshold ($+0.41$, $n = 194$) and lowers it when the input is already sufficient ($-0.56$, $n = 524$). \paragraph{The revisi |
| `524` | sections/results_v2.tex:72 | count or denominator |  | sufficiency threshold ($+0.41$, $n = 194$) and lowers it when the input is already sufficient ($-0.56$, $n = 524$). \paragraph{The revision cliff.} In |
| `50` | sections/results_v2.tex:75 | count or denominator |  | lowers it when the input is already sufficient ($-0.56$, $n = 524$). \paragraph{The revision cliff.} In the 50 balanced-panel trials (genuine revision |
| `3.3` | sections/results_v2.tex:75 | p-value |  | urn~5, a decline of $-0.74$ levels (Wilcoxon signed-rank $p = 1.01 \times 10^{-4}$; unstripped: $-0.94$, $p = 3.3 \times 10^{-6}$), of which 21\% is a |
| `10` | sections/results_v2.tex:75 | p-value |  | cline of $-0.74$ levels (Wilcoxon signed-rank $p = 1.01 \times 10^{-4}$; unstripped: $-0.94$, $p = 3.3 \times 10^{-6}$), of which 21\% is attributable |
| `6` | sections/results_v2.tex:75 | p-value |  | of $-0.74$ levels (Wilcoxon signed-rank $p = 1.01 \times 10^{-4}$; unstripped: $-0.94$, $p = 3.3 \times 10^{-6}$), of which 21\% is attributable to me |
| `21` | sections/results_v2.tex:75 | p-value |  | els (Wilcoxon signed-rank $p = 1.01 \times 10^{-4}$; unstripped: $-0.94$, $p = 3.3 \times 10^{-6}$), of which 21\% is attributable to meta-commentary  |
| `3.3` | sections/results_v2.tex:78 | count or denominator |  | ient'' to just below ``Functional.'' \paragraph{Per-model caveats.} The balanced panel is dominated by Llama~3.3~70B ($n = 45$), the only model with p |
| `45` | sections/results_v2.tex:78 | count or denominator |  | below ``Functional.'' \paragraph{Per-model caveats.} The balanced panel is dominated by Llama~3.3~70B ($n = 45$), the only model with power to detect  |
| `0.69` | sections/results_v2.tex:79 | p-value |  | y Llama~3.3~70B ($n = 45$), the only model with power to detect a within-model cliff; its stripped cliff of $-0.69$ is significant at $p = 3.76 \times |
| `3.76` | sections/results_v2.tex:80 | p-value |  | he only model with power to detect a within-model cliff; its stripped cliff of $-0.69$ is significant at $p = 3.76 \times 10^{-4}$. GPT-4o, DeepSeek a |
| `10` | sections/results_v2.tex:80 | p-value |  | l with power to detect a within-model cliff; its stripped cliff of $-0.69$ is significant at $p = 3.76 \times 10^{-4}$. GPT-4o, DeepSeek and Gemini co |
| `4` | sections/results_v2.tex:80 | p-value |  | h power to detect a within-model cliff; its stripped cliff of $-0.69$ is significant at $p = 3.76 \times 10^{-4}$. GPT-4o, DeepSeek and Gemini contrib |
| `50` | sections/results_v2.tex:95 | count or denominator | yes | \caption{Quality trajectory under undirected revision (stripped scores). Solid blue: balanced panel ($n = 50$, genuine revision at all turns), showing |
| `0.74` | sections/results_v2.tex:95 | count or denominator | yes | olid blue: balanced panel ($n = 50$, genuine revision at all turns), showing the headline cliff of $\Delta = -0.74$ (3.66$\to$2.92). Dashed gray: pool |
| `3.66` | sections/results_v2.tex:95 | count or denominator | yes | ue: balanced panel ($n = 50$, genuine revision at all turns), showing the headline cliff of $\Delta = -0.74$ (3.66$\to$2.92). Dashed gray: pooled genu |
| `2.92` | sections/results_v2.tex:95 | count or denominator | yes | ced panel ($n = 50$, genuine revision at all turns), showing the headline cliff of $\Delta = -0.74$ (3.66$\to$2.92). Dashed gray: pooled genuine-only  |

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
- `1` (results_FINAL.md:73, reliability or effect size) 1. **Effect size.** The paper prints r = 0.55 (all) and r = 0.53 (Llama). Recomputation gives
- `0.55` (results_FINAL.md:73, reliability or effect size) 1. **Effect size.** The paper prints r = 0.55 (all) and r = 0.53 (Llama). Recomputation gives
- `0.53` (results_FINAL.md:73, reliability or effect size) 1. **Effect size.** The paper prints r = 0.55 (all) and r = 0.53 (Llama). Recomputation gives
- `0.536` (results_FINAL.md:74, count or denominator) 0.536 and 0.514 dividing by N = all trials, or 0.681 and 0.652 dividing by N = non-zero
- `0.514` (results_FINAL.md:74, count or denominator) 0.536 and 0.514 dividing by N = all trials, or 0.681 and 0.652 dividing by N = non-zero
- `0.681` (results_FINAL.md:74, count or denominator) 0.536 and 0.514 dividing by N = all trials, or 0.681 and 0.652 dividing by N = non-zero
- `0.652` (results_FINAL.md:74, count or denominator) 0.536 and 0.514 dividing by N = all trials, or 0.681 and 0.652 dividing by N = non-zero
- `270` (results_FINAL.md:76, count or denominator) a survey of 270 papers found only one that states which N it divides by.
- `2` (results_FINAL.md:78, mean or delta) 2. **Llama delta.** This computation gives -0.67 from the full 3,600-output rescore. The paper
- `0.67` (results_FINAL.md:78, mean or delta) 2. **Llama delta.** This computation gives -0.67 from the full 3,600-output rescore. The paper
- `3,600` (results_FINAL.md:78, mean or delta) 2. **Llama delta.** This computation gives -0.67 from the full 3,600-output rescore. The paper
- `0.69` (results_FINAL.md:79, mean or delta) prints -0.69, which comes from the 50-pair rescore in `stripped_rescore_results.json`. Table 3
- `50` (results_FINAL.md:79, mean or delta) prints -0.69, which comes from the 50-pair rescore in `stripped_rescore_results.json`. Table 3
- `3` (results_FINAL.md:79, mean or delta) prints -0.69, which comes from the 50-pair rescore in `stripped_rescore_results.json`. Table 3
- `50` (results_FINAL.md:81, bare number) Llama row on the 50-pair rescore. Independently confirms the finding in

### [results_FINAL.md] 2. THE CLIFF (Quality Trajectory) -- Stripped Cliff (meta-commentary removed, re-scored)

*- **Filter:** the 50 balanced-panel trials (GENUINE at all of turns 2-5). Stripped levels at*

- `50` (results_FINAL.md:88, percentage) | All (n=50) | -0.94 | **-0.76** | 0.18 (19%) |
- `0.94` (results_FINAL.md:88, percentage) | All (n=50) | -0.94 | **-0.76** | 0.18 (19%) |
- `0.76` (results_FINAL.md:88, percentage) | All (n=50) | -0.94 | **-0.76** | 0.18 (19%) |
- `0.18` (results_FINAL.md:88, percentage) | All (n=50) | -0.94 | **-0.76** | 0.18 (19%) |
- `19` (results_FINAL.md:88, percentage) | All (n=50) | -0.94 | **-0.76** | 0.18 (19%) |
- `45` (results_FINAL.md:89, percentage) | Llama (n=45) | -0.82 | **-0.69** | 0.13 (16%) |
- `0.82` (results_FINAL.md:89, percentage) | Llama (n=45) | -0.82 | **-0.69** | 0.13 (16%) |
- `0.69` (results_FINAL.md:89, percentage) | Llama (n=45) | -0.82 | **-0.69** | 0.13 (16%) |
- `0.13` (results_FINAL.md:89, percentage) | Llama (n=45) | -0.82 | **-0.69** | 0.13 (16%) |
- `16` (results_FINAL.md:89, percentage) | Llama (n=45) | -0.82 | **-0.69** | 0.13 (16%) |
- `39` (results_FINAL.md:90, percentage) | Llama excl. near-trivial (n=39) | -0.79 | **-0.69** | 0.10 (13%) |
- `0.79` (results_FINAL.md:90, percentage) | Llama excl. near-trivial (n=39) | -0.79 | **-0.69** | 0.10 (13%) |
- `0.69` (results_FINAL.md:90, percentage) | Llama excl. near-trivial (n=39) | -0.79 | **-0.69** | 0.10 (13%) |
- `0.10` (results_FINAL.md:90, percentage) | Llama excl. near-trivial (n=39) | -0.79 | **-0.69** | 0.10 (13%) |
- `13` (results_FINAL.md:90, percentage) | Llama excl. near-trivial (n=39) | -0.79 | **-0.69** | 0.10 (13%) |
- `81` (results_FINAL.md:92, percentage) **The cliff is 81% real content degradation, 19% meta-commentary artifact.**
- `19` (results_FINAL.md:92, percentage) **The cliff is 81% real content degradation, 19% meta-commentary artifact.**
- `6` (results_FINAL.md:94, p-value) **DISCLOSURE -- Near-Trivial Edits:** 6 of 45 Llama balanced-panel trials contain at least one turn with >0.95 similarity to the prior turn (restatements with minimal change; 4 of these are character-
- `45` (results_FINAL.md:94, p-value) **DISCLOSURE -- Near-Trivial Edits:** 6 of 45 Llama balanced-panel trials contain at least one turn with >0.95 similarity to the prior turn (restatements with minimal change; 4 of these are character-
- `0.95` (results_FINAL.md:94, p-value) **DISCLOSURE -- Near-Trivial Edits:** 6 of 45 Llama balanced-panel trials contain at least one turn with >0.95 similarity to the prior turn (restatements with minimal change; 4 of these are character-
- `4` (results_FINAL.md:94, p-value) **DISCLOSURE -- Near-Trivial Edits:** 6 of 45 Llama balanced-panel trials contain at least one turn with >0.95 similarity to the prior turn (restatements with minimal change; 4 of these are character-
- `1.00` (results_FINAL.md:94, p-value) **DISCLOSURE -- Near-Trivial Edits:** 6 of 45 Llama balanced-panel trials contain at least one turn with >0.95 similarity to the prior turn (restatements with minimal change; 4 of these are character-
- `6` (results_FINAL.md:94, p-value) **DISCLOSURE -- Near-Trivial Edits:** 6 of 45 Llama balanced-panel trials contain at least one turn with >0.95 similarity to the prior turn (restatements with minimal change; 4 of these are character-
- `0.79` (results_FINAL.md:94, p-value) **DISCLOSURE -- Near-Trivial Edits:** 6 of 45 Llama balanced-panel trials contain at least one turn with >0.95 similarity to the prior turn (restatements with minimal change; 4 of these are character-
- `8` (results_FINAL.md:94, p-value) **DISCLOSURE -- Near-Trivial Edits:** 6 of 45 Llama balanced-panel trials contain at least one turn with >0.95 similarity to the prior turn (restatements with minimal change; 4 of these are character-
- `05` (results_FINAL.md:94, p-value) **DISCLOSURE -- Near-Trivial Edits:** 6 of 45 Llama balanced-panel trials contain at least one turn with >0.95 similarity to the prior turn (restatements with minimal change; 4 of these are character-
- `0.628` (results_FINAL.md:94, p-value) **DISCLOSURE -- Near-Trivial Edits:** 6 of 45 Llama balanced-panel trials contain at least one turn with >0.95 similarity to the prior turn (restatements with minimal change; 4 of these are character-
- `0.69` (results_FINAL.md:94, p-value) **DISCLOSURE -- Near-Trivial Edits:** 6 of 45 Llama balanced-panel trials contain at least one turn with >0.95 similarity to the prior turn (restatements with minimal change; 4 of these are character-
- `0.82` (results_FINAL.md:94, p-value) **DISCLOSURE -- Near-Trivial Edits:** 6 of 45 Llama balanced-panel trials contain at least one turn with >0.95 similarity to the prior turn (restatements with minimal change; 4 of these are character-
- `0.69` (results_FINAL.md:94, p-value) **DISCLOSURE -- Near-Trivial Edits:** 6 of 45 Llama balanced-panel trials contain at least one turn with >0.95 similarity to the prior turn (restatements with minimal change; 4 of these are character-
- `45` (results_FINAL.md:94, p-value) **DISCLOSURE -- Near-Trivial Edits:** 6 of 45 Llama balanced-panel trials contain at least one turn with >0.95 similarity to the prior turn (restatements with minimal change; 4 of these are character-
- `0.03` (results_FINAL.md:94, p-value) **DISCLOSURE -- Near-Trivial Edits:** 6 of 45 Llama balanced-panel trials contain at least one turn with >0.95 similarity to the prior turn (restatements with minimal change; 4 of these are character-
- `2026` (results_FINAL.md:94, p-value) **DISCLOSURE -- Near-Trivial Edits:** 6 of 45 Llama balanced-panel trials contain at least one turn with >0.95 similarity to the prior turn (restatements with minimal change; 4 of these are character-
- `06` (results_FINAL.md:94, p-value) **DISCLOSURE -- Near-Trivial Edits:** 6 of 45 Llama balanced-panel trials contain at least one turn with >0.95 similarity to the prior turn (restatements with minimal change; 4 of these are character-
- `11` (results_FINAL.md:94, p-value) **DISCLOSURE -- Near-Trivial Edits:** 6 of 45 Llama balanced-panel trials contain at least one turn with >0.95 similarity to the prior turn (restatements with minimal change; 4 of these are character-
- `50` (results_FINAL.md:98, bare number) - **Filter (stripped rescore):** Same 50 balanced-panel trials. For each, strip meta-commentary from T1 and T5 text using regex preamble/postamble patterns (from `strip_meta_commentary.py`). Re-score 
- `4` (results_FINAL.md:98, bare number) - **Filter (stripped rescore):** Same 50 balanced-panel trials. For each, strip meta-commentary from T1 and T5 text using regex preamble/postamble patterns (from `strip_meta_commentary.py`). Re-score 
- `4` (results_FINAL.md:98, bare number) - **Filter (stripped rescore):** Same 50 balanced-panel trials. For each, strip meta-commentary from T1 and T5 text using regex preamble/postamble patterns (from `strip_meta_commentary.py`). Re-score 
- `20250514` (results_FINAL.md:98, bare number) - **Filter (stripped rescore):** Same 50 balanced-panel trials. For each, strip meta-commentary from T1 and T5 text using regex preamble/postamble patterns (from `strip_meta_commentary.py`). Re-score 
- `0` (results_FINAL.md:98, bare number) - **Filter (stripped rescore):** Same 50 balanced-panel trials. For each, strip meta-commentary from T1 and T5 text using regex preamble/postamble patterns (from `strip_meta_commentary.py`). Re-score 
- `6` (results_FINAL.md:98, bare number) - **Filter (stripped rescore):** Same 50 balanced-panel trials. For each, strip meta-commentary from T1 and T5 text using regex preamble/postamble patterns (from `strip_meta_commentary.py`). Re-score 
- `2` (results_FINAL.md:98, bare number) - **Filter (stripped rescore):** Same 50 balanced-panel trials. For each, strip meta-commentary from T1 and T5 text using regex preamble/postamble patterns (from `strip_meta_commentary.py`). Re-score 

### [results_FINAL.md] 3. REVISION RATE

*- **Filter (stripped rescore):** Same 50 balanced-panel trials. For each, strip meta-commentary from T1 and T5 text using regex preamble/postamble patterns (from `strip_meta_commentary.py`). Re-score stripped text via Claude Sonnet 4 (`claude-sonnet-4-20250514`) at temperature 0 using the same EVAL_*

- `3` (results_FINAL.md:102, bare number) ## 3. REVISION RATE
- `283` (results_FINAL.md:106, percentage) | T2 | 283/720 | 39.3% |
- `720` (results_FINAL.md:106, percentage) | T2 | 283/720 | 39.3% |
- `39.3` (results_FINAL.md:106, percentage) | T2 | 283/720 | 39.3% |
- `185` (results_FINAL.md:107, percentage) | T3 | 185/720 | 25.7% |
- `720` (results_FINAL.md:107, percentage) | T3 | 185/720 | 25.7% |
- `25.7` (results_FINAL.md:107, percentage) | T3 | 185/720 | 25.7% |
- `154` (results_FINAL.md:108, percentage) | T4 | 154/720 | 21.4% |
- `720` (results_FINAL.md:108, percentage) | T4 | 154/720 | 21.4% |
- `21.4` (results_FINAL.md:108, percentage) | T4 | 154/720 | 21.4% |
- `96` (results_FINAL.md:109, percentage) | T5 | 96/720 | 13.3% |
- `720` (results_FINAL.md:109, percentage) | T5 | 96/720 | 13.3% |
- `13.3` (results_FINAL.md:109, percentage) | T5 | 96/720 | 13.3% |
- `2` (results_FINAL.md:111, bare number) - **Filter:** For each turn T in {2,3,4,5}, count trials where `genuine_meta_labels.jsonl` has `classifier_label == "GENUINE"` at that turn. Denominator = 720 (all successful trials).
- `3` (results_FINAL.md:111, bare number) - **Filter:** For each turn T in {2,3,4,5}, count trials where `genuine_meta_labels.jsonl` has `classifier_label == "GENUINE"` at that turn. Denominator = 720 (all successful trials).
- `4` (results_FINAL.md:111, bare number) - **Filter:** For each turn T in {2,3,4,5}, count trials where `genuine_meta_labels.jsonl` has `classifier_label == "GENUINE"` at that turn. Denominator = 720 (all successful trials).
- `5` (results_FINAL.md:111, bare number) - **Filter:** For each turn T in {2,3,4,5}, count trials where `genuine_meta_labels.jsonl` has `classifier_label == "GENUINE"` at that turn. Denominator = 720 (all successful trials).
- `720` (results_FINAL.md:111, bare number) - **Filter:** For each turn T in {2,3,4,5}, count trials where `genuine_meta_labels.jsonl` has `classifier_label == "GENUINE"` at that turn. Denominator = 720 (all successful trials).

### [results_FINAL.md] 4. REVISION-DESPITE-SUFFICIENCY

*- **Filter:** For each turn T in {2,3,4,5}, count trials where `genuine_meta_labels.jsonl` has `classifier_label == "GENUINE"` at that turn. Denominator = 720 (all successful trials).*

- `4` (results_FINAL.md:116, bare number) ## 4. REVISION-DESPITE-SUFFICIENCY
- `631` (results_FINAL.md:120, percentage) | T1 sufficiency rate | 631/720 (87.6%) |
- `720` (results_FINAL.md:120, percentage) | T1 sufficiency rate | 631/720 (87.6%) |
- `87.6` (results_FINAL.md:120, percentage) | T1 sufficiency rate | 631/720 (87.6%) |
- `368` (results_FINAL.md:121, percentage) | Sufficient turns with revision at next | 368/938 = **39.2%** |
- `938` (results_FINAL.md:121, percentage) | Sufficient turns with revision at next | 368/938 = **39.2%** |
- `39.2` (results_FINAL.md:121, percentage) | Sufficient turns with revision at next | 368/938 = **39.2%** |
- `95` (results_FINAL.md:122, percentage) | Bootstrap 95% CI | [36.1%, 42.3%] |
- `36.1` (results_FINAL.md:122, percentage) | Bootstrap 95% CI | [36.1%, 42.3%] |
- `42.3` (results_FINAL.md:122, percentage) | Bootstrap 95% CI | [36.1%, 42.3%] |
- `1` (results_FINAL.md:124, confidence interval) - **Filter:** For every (trial, turn) pair where turn in {1,2,3,4}, pull `level` from `evaluator_results.jsonl` (recode 6 -> 2). If level >= 4 ("sufficient"), check whether `genuine_meta_labels.jsonl`
- `2` (results_FINAL.md:124, confidence interval) - **Filter:** For every (trial, turn) pair where turn in {1,2,3,4}, pull `level` from `evaluator_results.jsonl` (recode 6 -> 2). If level >= 4 ("sufficient"), check whether `genuine_meta_labels.jsonl`
- `3` (results_FINAL.md:124, confidence interval) - **Filter:** For every (trial, turn) pair where turn in {1,2,3,4}, pull `level` from `evaluator_results.jsonl` (recode 6 -> 2). If level >= 4 ("sufficient"), check whether `genuine_meta_labels.jsonl`
- `4` (results_FINAL.md:124, confidence interval) - **Filter:** For every (trial, turn) pair where turn in {1,2,3,4}, pull `level` from `evaluator_results.jsonl` (recode 6 -> 2). If level >= 4 ("sufficient"), check whether `genuine_meta_labels.jsonl`
- `6` (results_FINAL.md:124, confidence interval) - **Filter:** For every (trial, turn) pair where turn in {1,2,3,4}, pull `level` from `evaluator_results.jsonl` (recode 6 -> 2). If level >= 4 ("sufficient"), check whether `genuine_meta_labels.jsonl`
- `2` (results_FINAL.md:124, confidence interval) - **Filter:** For every (trial, turn) pair where turn in {1,2,3,4}, pull `level` from `evaluator_results.jsonl` (recode 6 -> 2). If level >= 4 ("sufficient"), check whether `genuine_meta_labels.jsonl`
- `4` (results_FINAL.md:124, confidence interval) - **Filter:** For every (trial, turn) pair where turn in {1,2,3,4}, pull `level` from `evaluator_results.jsonl` (recode 6 -> 2). If level >= 4 ("sufficient"), check whether `genuine_meta_labels.jsonl`
- `1` (results_FINAL.md:124, confidence interval) - **Filter:** For every (trial, turn) pair where turn in {1,2,3,4}, pull `level` from `evaluator_results.jsonl` (recode 6 -> 2). If level >= 4 ("sufficient"), check whether `genuine_meta_labels.jsonl`
- `938` (results_FINAL.md:124, confidence interval) - **Filter:** For every (trial, turn) pair where turn in {1,2,3,4}, pull `level` from `evaluator_results.jsonl` (recode 6 -> 2). If level >= 4 ("sufficient"), check whether `genuine_meta_labels.jsonl`
- `1000` (results_FINAL.md:124, confidence interval) - **Filter:** For every (trial, turn) pair where turn in {1,2,3,4}, pull `level` from `evaluator_results.jsonl` (recode 6 -> 2). If level >= 4 ("sufficient"), check whether `genuine_meta_labels.jsonl`
- `42` (results_FINAL.md:124, confidence interval) - **Filter:** For every (trial, turn) pair where turn in {1,2,3,4}, pull `level` from `evaluator_results.jsonl` (recode 6 -> 2). If level >= 4 ("sufficient"), check whether `genuine_meta_labels.jsonl`
- `1` (results_FINAL.md:125, turn index) - **T1 sufficiency:** Count of trials where evaluator level at turn 1 >= 4 (after 6 -> 2 recode). 631/720 = 87.6%.
- `4` (results_FINAL.md:125, turn index) - **T1 sufficiency:** Count of trials where evaluator level at turn 1 >= 4 (after 6 -> 2 recode). 631/720 = 87.6%.
- `6` (results_FINAL.md:125, turn index) - **T1 sufficiency:** Count of trials where evaluator level at turn 1 >= 4 (after 6 -> 2 recode). 631/720 = 87.6%.
- `2` (results_FINAL.md:125, turn index) - **T1 sufficiency:** Count of trials where evaluator level at turn 1 >= 4 (after 6 -> 2 recode). 631/720 = 87.6%.
- `631` (results_FINAL.md:125, turn index) - **T1 sufficiency:** Count of trials where evaluator level at turn 1 >= 4 (after 6 -> 2 recode). 631/720 = 87.6%.
- `720` (results_FINAL.md:125, turn index) - **T1 sufficiency:** Count of trials where evaluator level at turn 1 >= 4 (after 6 -> 2 recode). 631/720 = 87.6%.
- `87.6` (results_FINAL.md:125, turn index) - **T1 sufficiency:** Count of trials where evaluator level at turn 1 >= 4 (after 6 -> 2 recode). 631/720 = 87.6%.

### [results_FINAL.md] 4b. DIRECTION OF REVISIONS (added 2026-09-03)

*- **Filter:** For every (trial, turn) pair where turn in {1,2,3,4}, pull `level` from `evaluator_results.jsonl` (recode 6 -> 2). If level >= 4 ("sufficient"), check whether `genuine_meta_labels.jsonl` has `classifier_label == "GENUINE"` at turn+1. Numerator = sufficient turns where next turn is GENU*

- `2026` (results_FINAL.md:130, bare number) ## 4b. DIRECTION OF REVISIONS (added 2026-09-03)
- `09` (results_FINAL.md:130, bare number) ## 4b. DIRECTION OF REVISIONS (added 2026-09-03)
- `03` (results_FINAL.md:130, bare number) ## 4b. DIRECTION OF REVISIONS (added 2026-09-03)
- `720` (results_FINAL.md:136, bare number) - **Sample:** unchanged. The same 720 trials and the same GENUINE/META labels from the
- `2` (results_FINAL.md:138, bare number) - **Filter (exact):** For each trial, walk turns 2-5. Where `genuine_meta_labels.jsonl`
- `5` (results_FINAL.md:138, bare number) - **Filter (exact):** For each trial, walk turns 2-5. Where `genuine_meta_labels.jsonl`
- `1` (results_FINAL.md:140, turn index) of the most recent turn whose content was genuinely new: turn 1, or the last turn
- `6` (results_FINAL.md:141, bare number) labelled GENUINE. Recode level 6 -> 2 first. Comparing against turn t-1 directly would
- `2` (results_FINAL.md:141, bare number) labelled GENUINE. Recode level 6 -> 2 first. Comparing against turn t-1 directly would
- `1` (results_FINAL.md:141, bare number) labelled GENUINE. Recode level 6 -> 2 first. Comparing against turn t-1 directly would
- `95` (results_FINAL.md:147, percentage) Clopper-Pearson exact 95% CI on the share worse among movers; chi-square on the

### [results_FINAL.md] 4b. DIRECTION OF REVISIONS (added 2026-09-03) -- Overall (n = 718 genuine revisions)

*- **Filter (exact):** For each trial, walk turns 2-5. Where `genuine_meta_labels.jsonl`*

- `718` (results_FINAL.md:151, count or denominator) ### Overall (n = 718 genuine revisions)
- `95` (results_FINAL.md:153, percentage) | Basis | worse | same | better | movers | % of movers worse | 95% CI | sign p |
- `199` (results_FINAL.md:155, percentage) | **Stripped** | 199 (27.7%) | 432 (60.2%) | 87 (12.1%) | 286 | **69.6%** | [63.9%, 74.9%] | 1.48e-11 |
- `27.7` (results_FINAL.md:155, percentage) | **Stripped** | 199 (27.7%) | 432 (60.2%) | 87 (12.1%) | 286 | **69.6%** | [63.9%, 74.9%] | 1.48e-11 |
- `432` (results_FINAL.md:155, percentage) | **Stripped** | 199 (27.7%) | 432 (60.2%) | 87 (12.1%) | 286 | **69.6%** | [63.9%, 74.9%] | 1.48e-11 |
- `60.2` (results_FINAL.md:155, percentage) | **Stripped** | 199 (27.7%) | 432 (60.2%) | 87 (12.1%) | 286 | **69.6%** | [63.9%, 74.9%] | 1.48e-11 |
- `87` (results_FINAL.md:155, percentage) | **Stripped** | 199 (27.7%) | 432 (60.2%) | 87 (12.1%) | 286 | **69.6%** | [63.9%, 74.9%] | 1.48e-11 |
- `12.1` (results_FINAL.md:155, percentage) | **Stripped** | 199 (27.7%) | 432 (60.2%) | 87 (12.1%) | 286 | **69.6%** | [63.9%, 74.9%] | 1.48e-11 |
- `286` (results_FINAL.md:155, percentage) | **Stripped** | 199 (27.7%) | 432 (60.2%) | 87 (12.1%) | 286 | **69.6%** | [63.9%, 74.9%] | 1.48e-11 |
- `69.6` (results_FINAL.md:155, percentage) | **Stripped** | 199 (27.7%) | 432 (60.2%) | 87 (12.1%) | 286 | **69.6%** | [63.9%, 74.9%] | 1.48e-11 |
- `63.9` (results_FINAL.md:155, percentage) | **Stripped** | 199 (27.7%) | 432 (60.2%) | 87 (12.1%) | 286 | **69.6%** | [63.9%, 74.9%] | 1.48e-11 |
- `74.9` (results_FINAL.md:155, percentage) | **Stripped** | 199 (27.7%) | 432 (60.2%) | 87 (12.1%) | 286 | **69.6%** | [63.9%, 74.9%] | 1.48e-11 |
- `1` (results_FINAL.md:155, percentage) | **Stripped** | 199 (27.7%) | 432 (60.2%) | 87 (12.1%) | 286 | **69.6%** | [63.9%, 74.9%] | 1.48e-11 |
- `11` (results_FINAL.md:155, percentage) | **Stripped** | 199 (27.7%) | 432 (60.2%) | 87 (12.1%) | 286 | **69.6%** | [63.9%, 74.9%] | 1.48e-11 |
- `245` (results_FINAL.md:156, percentage) | Unstripped | 245 (34.1%) | 398 (55.4%) | 75 (10.4%) | 320 | 76.6% | [71.5%, 81.1%] | 1.66e-22 |
- `34.1` (results_FINAL.md:156, percentage) | Unstripped | 245 (34.1%) | 398 (55.4%) | 75 (10.4%) | 320 | 76.6% | [71.5%, 81.1%] | 1.66e-22 |
- `398` (results_FINAL.md:156, percentage) | Unstripped | 245 (34.1%) | 398 (55.4%) | 75 (10.4%) | 320 | 76.6% | [71.5%, 81.1%] | 1.66e-22 |
- `55.4` (results_FINAL.md:156, percentage) | Unstripped | 245 (34.1%) | 398 (55.4%) | 75 (10.4%) | 320 | 76.6% | [71.5%, 81.1%] | 1.66e-22 |
- `75` (results_FINAL.md:156, percentage) | Unstripped | 245 (34.1%) | 398 (55.4%) | 75 (10.4%) | 320 | 76.6% | [71.5%, 81.1%] | 1.66e-22 |
- `10.4` (results_FINAL.md:156, percentage) | Unstripped | 245 (34.1%) | 398 (55.4%) | 75 (10.4%) | 320 | 76.6% | [71.5%, 81.1%] | 1.66e-22 |
- `320` (results_FINAL.md:156, percentage) | Unstripped | 245 (34.1%) | 398 (55.4%) | 75 (10.4%) | 320 | 76.6% | [71.5%, 81.1%] | 1.66e-22 |
- `76.6` (results_FINAL.md:156, percentage) | Unstripped | 245 (34.1%) | 398 (55.4%) | 75 (10.4%) | 320 | 76.6% | [71.5%, 81.1%] | 1.66e-22 |
- `71.5` (results_FINAL.md:156, percentage) | Unstripped | 245 (34.1%) | 398 (55.4%) | 75 (10.4%) | 320 | 76.6% | [71.5%, 81.1%] | 1.66e-22 |
- `81.1` (results_FINAL.md:156, percentage) | Unstripped | 245 (34.1%) | 398 (55.4%) | 75 (10.4%) | 320 | 76.6% | [71.5%, 81.1%] | 1.66e-22 |
- `1` (results_FINAL.md:156, percentage) | Unstripped | 245 (34.1%) | 398 (55.4%) | 75 (10.4%) | 320 | 76.6% | [71.5%, 81.1%] | 1.66e-22 |
- `22` (results_FINAL.md:156, percentage) | Unstripped | 245 (34.1%) | 398 (55.4%) | 75 (10.4%) | 320 | 76.6% | [71.5%, 81.1%] | 1.66e-22 |
- `60.2` (results_FINAL.md:158, percentage) Most revisions (60.2% stripped) do not move the level at all, which is partly the
- `2.3` (results_FINAL.md:160, mean or delta) asymmetric: down about 2.3 times as often as up.

### [results_FINAL.md] 4b. DIRECTION OF REVISIONS (added 2026-09-03) -- Per-model (stripped, primary)

*- **Filter (exact):** For each trial, walk turns 2-5. Where `genuine_meta_labels.jsonl`*

- `2.5` (results_FINAL.md:166, percentage) | gemini-2.5-flash | 8 | 50.0% | 50.0% | 0.0% | 100.0% | 0.062 |
- `8` (results_FINAL.md:166, percentage) | gemini-2.5-flash | 8 | 50.0% | 50.0% | 0.0% | 100.0% | 0.062 |
- `50.0` (results_FINAL.md:166, percentage) | gemini-2.5-flash | 8 | 50.0% | 50.0% | 0.0% | 100.0% | 0.062 |
- `50.0` (results_FINAL.md:166, percentage) | gemini-2.5-flash | 8 | 50.0% | 50.0% | 0.0% | 100.0% | 0.062 |
- `0.0` (results_FINAL.md:166, percentage) | gemini-2.5-flash | 8 | 50.0% | 50.0% | 0.0% | 100.0% | 0.062 |
- `100.0` (results_FINAL.md:166, percentage) | gemini-2.5-flash | 8 | 50.0% | 50.0% | 0.0% | 100.0% | 0.062 |
- `0.062` (results_FINAL.md:166, percentage) | gemini-2.5-flash | 8 | 50.0% | 50.0% | 0.0% | 100.0% | 0.062 |
- `31` (results_FINAL.md:167, percentage) | deepseek-v4 | 31 | 38.7% | 54.8% | 6.5% | 85.7% | 0.0065 |
- `38.7` (results_FINAL.md:167, percentage) | deepseek-v4 | 31 | 38.7% | 54.8% | 6.5% | 85.7% | 0.0065 |
- `54.8` (results_FINAL.md:167, percentage) | deepseek-v4 | 31 | 38.7% | 54.8% | 6.5% | 85.7% | 0.0065 |
- `6.5` (results_FINAL.md:167, percentage) | deepseek-v4 | 31 | 38.7% | 54.8% | 6.5% | 85.7% | 0.0065 |
- `85.7` (results_FINAL.md:167, percentage) | deepseek-v4 | 31 | 38.7% | 54.8% | 6.5% | 85.7% | 0.0065 |
- `0.0065` (results_FINAL.md:167, percentage) | deepseek-v4 | 31 | 38.7% | 54.8% | 6.5% | 85.7% | 0.0065 |
- `40` (results_FINAL.md:168, percentage) | gpt-4o | 40 | 40.0% | 50.0% | 10.0% | 80.0% | 0.0059 |
- `40.0` (results_FINAL.md:168, percentage) | gpt-4o | 40 | 40.0% | 50.0% | 10.0% | 80.0% | 0.0059 |
- `50.0` (results_FINAL.md:168, percentage) | gpt-4o | 40 | 40.0% | 50.0% | 10.0% | 80.0% | 0.0059 |
- `10.0` (results_FINAL.md:168, percentage) | gpt-4o | 40 | 40.0% | 50.0% | 10.0% | 80.0% | 0.0059 |
- `80.0` (results_FINAL.md:168, percentage) | gpt-4o | 40 | 40.0% | 50.0% | 10.0% | 80.0% | 0.0059 |
- `0.0059` (results_FINAL.md:168, percentage) | gpt-4o | 40 | 40.0% | 50.0% | 10.0% | 80.0% | 0.0059 |
- `3` (results_FINAL.md:169, percentage) | qwen-3-235b | 90 | 42.2% | 43.3% | 14.4% | 74.5% | 0.00031 |
- `90` (results_FINAL.md:169, percentage) | qwen-3-235b | 90 | 42.2% | 43.3% | 14.4% | 74.5% | 0.00031 |
- `42.2` (results_FINAL.md:169, percentage) | qwen-3-235b | 90 | 42.2% | 43.3% | 14.4% | 74.5% | 0.00031 |
- `43.3` (results_FINAL.md:169, percentage) | qwen-3-235b | 90 | 42.2% | 43.3% | 14.4% | 74.5% | 0.00031 |
- `14.4` (results_FINAL.md:169, percentage) | qwen-3-235b | 90 | 42.2% | 43.3% | 14.4% | 74.5% | 0.00031 |
- `74.5` (results_FINAL.md:169, percentage) | qwen-3-235b | 90 | 42.2% | 43.3% | 14.4% | 74.5% | 0.00031 |
- `0.00031` (results_FINAL.md:169, percentage) | qwen-3-235b | 90 | 42.2% | 43.3% | 14.4% | 74.5% | 0.00031 |
- `3.3` (results_FINAL.md:170, percentage) | llama-3.3-70b | 353 | 25.8% | 62.6% | 11.6% | 68.9% | 8.0e-06 |
- `353` (results_FINAL.md:170, percentage) | llama-3.3-70b | 353 | 25.8% | 62.6% | 11.6% | 68.9% | 8.0e-06 |
- `25.8` (results_FINAL.md:170, percentage) | llama-3.3-70b | 353 | 25.8% | 62.6% | 11.6% | 68.9% | 8.0e-06 |
- `62.6` (results_FINAL.md:170, percentage) | llama-3.3-70b | 353 | 25.8% | 62.6% | 11.6% | 68.9% | 8.0e-06 |
- `11.6` (results_FINAL.md:170, percentage) | llama-3.3-70b | 353 | 25.8% | 62.6% | 11.6% | 68.9% | 8.0e-06 |
- `68.9` (results_FINAL.md:170, percentage) | llama-3.3-70b | 353 | 25.8% | 62.6% | 11.6% | 68.9% | 8.0e-06 |
- `8` (results_FINAL.md:170, percentage) | llama-3.3-70b | 353 | 25.8% | 62.6% | 11.6% | 68.9% | 8.0e-06 |
- `06` (results_FINAL.md:170, percentage) | llama-3.3-70b | 353 | 25.8% | 62.6% | 11.6% | 68.9% | 8.0e-06 |
- `4` (results_FINAL.md:171, percentage) | claude-sonnet-4 | 196 | 19.4% | 66.8% | 13.8% | 58.5% | 0.11 |
- `196` (results_FINAL.md:171, percentage) | claude-sonnet-4 | 196 | 19.4% | 66.8% | 13.8% | 58.5% | 0.11 |
- `19.4` (results_FINAL.md:171, percentage) | claude-sonnet-4 | 196 | 19.4% | 66.8% | 13.8% | 58.5% | 0.11 |
- `66.8` (results_FINAL.md:171, percentage) | claude-sonnet-4 | 196 | 19.4% | 66.8% | 13.8% | 58.5% | 0.11 |
- `13.8` (results_FINAL.md:171, percentage) | claude-sonnet-4 | 196 | 19.4% | 66.8% | 13.8% | 58.5% | 0.11 |
- `58.5` (results_FINAL.md:171, percentage) | claude-sonnet-4 | 196 | 19.4% | 66.8% | 13.8% | 58.5% | 0.11 |
- `0.11` (results_FINAL.md:171, percentage) | claude-sonnet-4 | 196 | 19.4% | 66.8% | 13.8% | 58.5% | 0.11 |
- `4` (results_FINAL.md:174, p-value) individually significant in only four. Claude Sonnet 4 is not significant (p = 0.11)
- `0.11` (results_FINAL.md:174, p-value) individually significant in only four. Claude Sonnet 4 is not significant (p = 0.11)
- `8` (results_FINAL.md:175, bare number) and Gemini has only 8 genuine revisions. The correct claim is that the direction holds
- `0.062` (results_FINAL.md:177, p-value) significantly. Unstripped, five of six reach significance (Gemini p = 0.062).

### [results_FINAL.md] 4b. DIRECTION OF REVISIONS (added 2026-09-03) -- Per-domain (stripped, primary)

*- **Filter (exact):** For each trial, walk turns 2-5. Where `genuine_meta_labels.jsonl`*

- `118` (results_FINAL.md:183, percentage) | writing | 118 | 28.8% | 63.6% | 7.6% | 79.1% | 8.5e-05 |
- `28.8` (results_FINAL.md:183, percentage) | writing | 118 | 28.8% | 63.6% | 7.6% | 79.1% | 8.5e-05 |
- `63.6` (results_FINAL.md:183, percentage) | writing | 118 | 28.8% | 63.6% | 7.6% | 79.1% | 8.5e-05 |
- `7.6` (results_FINAL.md:183, percentage) | writing | 118 | 28.8% | 63.6% | 7.6% | 79.1% | 8.5e-05 |
- `79.1` (results_FINAL.md:183, percentage) | writing | 118 | 28.8% | 63.6% | 7.6% | 79.1% | 8.5e-05 |
- `8` (results_FINAL.md:183, percentage) | writing | 118 | 28.8% | 63.6% | 7.6% | 79.1% | 8.5e-05 |
- `05` (results_FINAL.md:183, percentage) | writing | 118 | 28.8% | 63.6% | 7.6% | 79.1% | 8.5e-05 |
- `145` (results_FINAL.md:184, percentage) | creative | 145 | 26.2% | 64.1% | 9.7% | 73.1% | 0.0006 |
- `26.2` (results_FINAL.md:184, percentage) | creative | 145 | 26.2% | 64.1% | 9.7% | 73.1% | 0.0006 |
- `64.1` (results_FINAL.md:184, percentage) | creative | 145 | 26.2% | 64.1% | 9.7% | 73.1% | 0.0006 |
- `9.7` (results_FINAL.md:184, percentage) | creative | 145 | 26.2% | 64.1% | 9.7% | 73.1% | 0.0006 |
- `73.1` (results_FINAL.md:184, percentage) | creative | 145 | 26.2% | 64.1% | 9.7% | 73.1% | 0.0006 |
- `0.0006` (results_FINAL.md:184, percentage) | creative | 145 | 26.2% | 64.1% | 9.7% | 73.1% | 0.0006 |
- `196` (results_FINAL.md:185, percentage) | code | 196 | 35.2% | 47.4% | 17.3% | 67.0% | 0.00036 |
- `35.2` (results_FINAL.md:185, percentage) | code | 196 | 35.2% | 47.4% | 17.3% | 67.0% | 0.00036 |
- `47.4` (results_FINAL.md:185, percentage) | code | 196 | 35.2% | 47.4% | 17.3% | 67.0% | 0.00036 |
- `17.3` (results_FINAL.md:185, percentage) | code | 196 | 35.2% | 47.4% | 17.3% | 67.0% | 0.00036 |
- `67.0` (results_FINAL.md:185, percentage) | code | 196 | 35.2% | 47.4% | 17.3% | 67.0% | 0.00036 |
- `0.00036` (results_FINAL.md:185, percentage) | code | 196 | 35.2% | 47.4% | 17.3% | 67.0% | 0.00036 |
- `125` (results_FINAL.md:186, percentage) | analysis | 125 | 23.2% | 64.8% | 12.0% | 65.9% | 0.024 |
- `23.2` (results_FINAL.md:186, percentage) | analysis | 125 | 23.2% | 64.8% | 12.0% | 65.9% | 0.024 |
- `64.8` (results_FINAL.md:186, percentage) | analysis | 125 | 23.2% | 64.8% | 12.0% | 65.9% | 0.024 |
- `12.0` (results_FINAL.md:186, percentage) | analysis | 125 | 23.2% | 64.8% | 12.0% | 65.9% | 0.024 |
- `65.9` (results_FINAL.md:186, percentage) | analysis | 125 | 23.2% | 64.8% | 12.0% | 65.9% | 0.024 |
- `0.024` (results_FINAL.md:186, percentage) | analysis | 125 | 23.2% | 64.8% | 12.0% | 65.9% | 0.024 |
- `134` (results_FINAL.md:187, percentage) | data_logic | 134 | 21.6% | 67.2% | 11.2% | 65.9% | 0.024 |
- `21.6` (results_FINAL.md:187, percentage) | data_logic | 134 | 21.6% | 67.2% | 11.2% | 65.9% | 0.024 |
- `67.2` (results_FINAL.md:187, percentage) | data_logic | 134 | 21.6% | 67.2% | 11.2% | 65.9% | 0.024 |
- `11.2` (results_FINAL.md:187, percentage) | data_logic | 134 | 21.6% | 67.2% | 11.2% | 65.9% | 0.024 |
- `65.9` (results_FINAL.md:187, percentage) | data_logic | 134 | 21.6% | 67.2% | 11.2% | 65.9% | 0.024 |
- `0.024` (results_FINAL.md:187, percentage) | data_logic | 134 | 21.6% | 67.2% | 11.2% | 65.9% | 0.024 |
- `3.02` (results_FINAL.md:190, p-value) **chi2 = 3.02, dof = 4, p = 0.555.** The asymmetry does not differ by domain.
- `4` (results_FINAL.md:190, p-value) **chi2 = 3.02, dof = 4, p = 0.555.** The asymmetry does not differ by domain.
- `0.555` (results_FINAL.md:190, p-value) **chi2 = 3.02, dof = 4, p = 0.555.** The asymmetry does not differ by domain.

### [results_FINAL.md] 4b. DIRECTION OF REVISIONS (added 2026-09-03) -- The objectivity gradient is a meta-commentary artifact

*- **Filter (exact):** For each trial, walk turns 2-5. Where `genuine_meta_labels.jsonl`*

- `98` (results_FINAL.md:196, percentage) | **Stripped** | 98 / 49 = 66.7% worse | 72 / 23 = 75.8% worse | **0.151** |
- `49` (results_FINAL.md:196, percentage) | **Stripped** | 98 / 49 = 66.7% worse | 72 / 23 = 75.8% worse | **0.151** |
- `66.7` (results_FINAL.md:196, percentage) | **Stripped** | 98 / 49 = 66.7% worse | 72 / 23 = 75.8% worse | **0.151** |
- `72` (results_FINAL.md:196, percentage) | **Stripped** | 98 / 49 = 66.7% worse | 72 / 23 = 75.8% worse | **0.151** |
- `23` (results_FINAL.md:196, percentage) | **Stripped** | 98 / 49 = 66.7% worse | 72 / 23 = 75.8% worse | **0.151** |
- `75.8` (results_FINAL.md:196, percentage) | **Stripped** | 98 / 49 = 66.7% worse | 72 / 23 = 75.8% worse | **0.151** |
- `0.151` (results_FINAL.md:196, percentage) | **Stripped** | 98 / 49 = 66.7% worse | 72 / 23 = 75.8% worse | **0.151** |
- `109` (results_FINAL.md:197, percentage) | Unstripped | 109 / 44 = 71.2% worse | 94 / 18 = 83.9% worse | **0.019** |
- `44` (results_FINAL.md:197, percentage) | Unstripped | 109 / 44 = 71.2% worse | 94 / 18 = 83.9% worse | **0.019** |
- `71.2` (results_FINAL.md:197, percentage) | Unstripped | 109 / 44 = 71.2% worse | 94 / 18 = 83.9% worse | **0.019** |
- `94` (results_FINAL.md:197, percentage) | Unstripped | 109 / 44 = 71.2% worse | 94 / 18 = 83.9% worse | **0.019** |
- `18` (results_FINAL.md:197, percentage) | Unstripped | 109 / 44 = 71.2% worse | 94 / 18 = 83.9% worse | **0.019** |
- `83.9` (results_FINAL.md:197, percentage) | Unstripped | 109 / 44 = 71.2% worse | 94 / 18 = 83.9% worse | **0.019** |
- `0.019` (results_FINAL.md:197, percentage) | Unstripped | 109 / 44 = 71.2% worse | 94 / 18 = 83.9% worse | **0.019** |
- `0.205` (results_FINAL.md:199, p-value) Unstripped domain chi-square p = 0.205; stripped p = 0.555.
- `0.555` (results_FINAL.md:199, p-value) Unstripped domain chi-square p = 0.205; stripped p = 0.555.
- `117` (results_FINAL.md:201, bare number) **BEARS ON A REGISTERED PREDICTION.** `experiment/study3_revision_yield_design.md` line 117
- `0.019` (results_FINAL.md:204, p-value) scores (p = 0.019) and **is not supported once meta-commentary is stripped** (p = 0.151).
- `0.151` (results_FINAL.md:204, p-value) scores (p = 0.019) and **is not supported once meta-commentary is stripped** (p = 0.151).
- `65` (results_FINAL.md:209, percentage) the 65% reversibility bar in Section 7.
- `7` (results_FINAL.md:209, percentage) the 65% reversibility bar in Section 7.

### [results_FINAL.md] 4b. DIRECTION OF REVISIONS (added 2026-09-03) -- Outcome when the input was already sufficient (added 2026-09-07)

*- **Filter (exact):** For each trial, walk turns 2-5. Where `genuine_meta_labels.jsonl`*

- `2026` (results_FINAL.md:211, bare number) ### Outcome when the input was already sufficient (added 2026-09-07)
- `09` (results_FINAL.md:211, bare number) ### Outcome when the input was already sufficient (added 2026-09-07)
- `07` (results_FINAL.md:211, bare number) ### Outcome when the input was already sufficient (added 2026-09-07)
- `4` (results_FINAL.md:213, bare number) Of the genuine revisions whose baseline content was already at level 4 or above, how many
- `4` (results_FINAL.md:214, bare number) end below level 4?
- `411` (results_FINAL.md:218, percentage) | **Stripped** | 411 | 298 (72.5%) | **113 (27.5%)** |
- `298` (results_FINAL.md:218, percentage) | **Stripped** | 411 | 298 (72.5%) | **113 (27.5%)** |
- `72.5` (results_FINAL.md:218, percentage) | **Stripped** | 411 | 298 (72.5%) | **113 (27.5%)** |
- `113` (results_FINAL.md:218, percentage) | **Stripped** | 411 | 298 (72.5%) | **113 (27.5%)** |
- `27.5` (results_FINAL.md:218, percentage) | **Stripped** | 411 | 298 (72.5%) | **113 (27.5%)** |
- `113` (results_FINAL.md:220, bare number) Of the 113 that fall below, 85 land at level 2 and 28 at level 3.
- `85` (results_FINAL.md:220, bare number) Of the 113 that fall below, 85 land at level 2 and 28 at level 3.
- `2` (results_FINAL.md:220, bare number) Of the 113 that fall below, 85 land at level 2 and 28 at level 3.
- `28` (results_FINAL.md:220, bare number) Of the 113 that fall below, 85 land at level 2 and 28 at level 3.
- `3` (results_FINAL.md:220, bare number) Of the 113 that fall below, 85 land at level 2 and 28 at level 3.
- `718` (results_FINAL.md:222, bare number) - **Filter:** the same 718 genuine revisions as above. Keep those whose baseline (the most
- `4` (results_FINAL.md:223, bare number) recent turn with genuinely new content) is at level >= 4 after the 6 -> 2 recode. Count how
- `6` (results_FINAL.md:223, bare number) recent turn with genuinely new content) is at level >= 4 after the 6 -> 2 recode. Count how
- `2` (results_FINAL.md:223, bare number) recent turn with genuinely new content) is at level >= 4 after the 6 -> 2 recode. Count how
- `4` (results_FINAL.md:224, bare number) many have a level < 4 at the revision turn.
- `411` (results_FINAL.md:225, count or denominator) - **This is the same set of 411 as Stripped Sensitivity M1** ("Revised despite sufficient",
- `411` (results_FINAL.md:226, percentage) 411 of 1,038 sufficient turns, 39.6%). Verified 2026-09-07: the two constructions produce
- `1,038` (results_FINAL.md:226, percentage) 411 of 1,038 sufficient turns, 39.6%). Verified 2026-09-07: the two constructions produce
- `39.6` (results_FINAL.md:226, percentage) 411 of 1,038 sufficient turns, 39.6%). Verified 2026-09-07: the two constructions produce
- `2026` (results_FINAL.md:226, percentage) 411 of 1,038 sufficient turns, 39.6%). Verified 2026-09-07: the two constructions produce
- `09` (results_FINAL.md:226, percentage) 411 of 1,038 sufficient turns, 39.6%). Verified 2026-09-07: the two constructions produce
- `07` (results_FINAL.md:226, percentage) 411 of 1,038 sufficient turns, 39.6%). Verified 2026-09-07: the two constructions produce
- `411` (results_FINAL.md:227, count or denominator) identical sets, 411 of 411, zero on either side. They coincide because a meta-response
- `411` (results_FINAL.md:227, count or denominator) identical sets, 411 of 411, zero on either side. They coincide because a meta-response
- `1.06` (results_FINAL.md:228, mean or delta) strips to near-empty text and scores about 1.06, so it can never be a sufficient baseline.

### [results_FINAL.md] 4b. DIRECTION OF REVISIONS (added 2026-09-03) -- Magnitude of the change (added 2026-09-07)

*- **Filter:** the same 718 genuine revisions as above. Keep those whose baseline (the most*

- `2026` (results_FINAL.md:231, bare number) ### Magnitude of the change (added 2026-09-07)
- `09` (results_FINAL.md:231, bare number) ### Magnitude of the change (added 2026-09-07)
- `07` (results_FINAL.md:231, bare number) ### Magnitude of the change (added 2026-09-07)
- `0.30` (results_FINAL.md:235, mean or delta) | **Stripped** | **-0.30** | **-1.72** | -2 | +1.45 |
- `1.72` (results_FINAL.md:235, mean or delta) | **Stripped** | **-0.30** | **-1.72** | -2 | +1.45 |
- `2` (results_FINAL.md:235, mean or delta) | **Stripped** | **-0.30** | **-1.72** | -2 | +1.45 |
- `1.45` (results_FINAL.md:235, mean or delta) | **Stripped** | **-0.30** | **-1.72** | -2 | +1.45 |
- `0.51` (results_FINAL.md:236, mean or delta) | Unstripped | -0.51 | -1.90 | -2 | +1.32 |
- `1.90` (results_FINAL.md:236, mean or delta) | Unstripped | -0.51 | -1.90 | -2 | +1.32 |
- `2` (results_FINAL.md:236, mean or delta) | Unstripped | -0.51 | -1.90 | -2 | +1.32 |
- `1.32` (results_FINAL.md:236, mean or delta) | Unstripped | -0.51 | -1.90 | -2 | +1.32 |
- `87` (results_FINAL.md:238, bare number) Stripped, 87 of the 199 downward moves fall one level and 112 fall two or more. Drops are both
- `199` (results_FINAL.md:238, bare number) Stripped, 87 of the 199 downward moves fall one level and 112 fall two or more. Drops are both
- `112` (results_FINAL.md:238, bare number) Stripped, 87 of the 199 downward moves fall one level and 112 fall two or more. Drops are both

### [results_FINAL.md] 4b. DIRECTION OF REVISIONS (added 2026-09-03) -- Trial-level, balanced panel (Turn 1 vs Turn 5, n = 50)

*- **Filter:** signed difference in recoded level between each genuine revision and its baseline,*

- `1` (results_FINAL.md:244, count or denominator) ### Trial-level, balanced panel (Turn 1 vs Turn 5, n = 50)
- `5` (results_FINAL.md:244, count or denominator) ### Trial-level, balanced panel (Turn 1 vs Turn 5, n = 50)
- `50` (results_FINAL.md:244, count or denominator) ### Trial-level, balanced panel (Turn 1 vs Turn 5, n = 50)
- `52.0` (results_FINAL.md:248, percentage) | **Stripped** | 52.0% | 38.0% | 10.0% | 26 / 5 | 9.61e-05 |
- `38.0` (results_FINAL.md:248, percentage) | **Stripped** | 52.0% | 38.0% | 10.0% | 26 / 5 | 9.61e-05 |
- `10.0` (results_FINAL.md:248, percentage) | **Stripped** | 52.0% | 38.0% | 10.0% | 26 / 5 | 9.61e-05 |
- `26` (results_FINAL.md:248, percentage) | **Stripped** | 52.0% | 38.0% | 10.0% | 26 / 5 | 9.61e-05 |
- `5` (results_FINAL.md:248, percentage) | **Stripped** | 52.0% | 38.0% | 10.0% | 26 / 5 | 9.61e-05 |
- `9` (results_FINAL.md:248, percentage) | **Stripped** | 52.0% | 38.0% | 10.0% | 26 / 5 | 9.61e-05 |
- `05` (results_FINAL.md:248, percentage) | **Stripped** | 52.0% | 38.0% | 10.0% | 26 / 5 | 9.61e-05 |
- `62.0` (results_FINAL.md:249, percentage) | Unstripped | 62.0% | 30.0% | 8.0% | 31 / 4 | 1.73e-06 |
- `30.0` (results_FINAL.md:249, percentage) | Unstripped | 62.0% | 30.0% | 8.0% | 31 / 4 | 1.73e-06 |
- `8.0` (results_FINAL.md:249, percentage) | Unstripped | 62.0% | 30.0% | 8.0% | 31 / 4 | 1.73e-06 |
- `31` (results_FINAL.md:249, percentage) | Unstripped | 62.0% | 30.0% | 8.0% | 31 / 4 | 1.73e-06 |
- `4` (results_FINAL.md:249, percentage) | Unstripped | 62.0% | 30.0% | 8.0% | 31 / 4 | 1.73e-06 |
- `1` (results_FINAL.md:249, percentage) | Unstripped | 62.0% | 30.0% | 8.0% | 31 / 4 | 1.73e-06 |
- `06` (results_FINAL.md:249, percentage) | Unstripped | 62.0% | 30.0% | 8.0% | 31 / 4 | 1.73e-06 |

### [results_FINAL.md] 4b. DIRECTION OF REVISIONS (added 2026-09-03) -- Why this estimator is preferred to the balanced-panel cliff

*- **Filter:** signed difference in recoded level between each genuine revision and its baseline,*

- `2` (results_FINAL.md:253, bare number) The cliff in Section 2 rests on 50 trials, 45 of them Llama, with three of six models
- `50` (results_FINAL.md:253, bare number) The cliff in Section 2 rests on 50 trials, 45 of them Llama, with three of six models
- `45` (results_FINAL.md:253, bare number) The cliff in Section 2 rests on 50 trials, 45 of them Llama, with three of six models
- `718` (results_FINAL.md:254, bare number) contributing zero trials. This analysis uses all 718 genuine revisions across all six
- `2026` (results_FINAL.md:256, count or denominator) data. It is the basis for the paper's headline claim as of 2026-09-03.
- `09` (results_FINAL.md:256, count or denominator) data. It is the basis for the paper's headline claim as of 2026-09-03.
- `03` (results_FINAL.md:256, count or denominator) data. It is the basis for the paper's headline claim as of 2026-09-03.

### [results_FINAL.md] 4c. EXPECTED CHANGE BY INPUT LEVEL (added 2026-09-14)

*- **Filter:** signed difference in recoded level between each genuine revision and its baseline,*

- `2026` (results_FINAL.md:260, bare number) ## 4c. EXPECTED CHANGE BY INPUT LEVEL (added 2026-09-14)
- `09` (results_FINAL.md:260, bare number) ## 4c. EXPECTED CHANGE BY INPUT LEVEL (added 2026-09-14)
- `14` (results_FINAL.md:260, bare number) ## 4c. EXPECTED CHANGE BY INPUT LEVEL (added 2026-09-14)
- `2026` (results_FINAL.md:262, bare number) **POST-HOC. Not among the registered predictions.** Computed 2026-09-14 while preparing
- `09` (results_FINAL.md:262, bare number) **POST-HOC. Not among the registered predictions.** Computed 2026-09-14 while preparing
- `14` (results_FINAL.md:262, bare number) **POST-HOC. Not among the registered predictions.** Computed 2026-09-14 while preparing
- `2` (results_FINAL.md:271, mean or delta) | 2 | 116 | +0.69 | 0.00 | 0.35 |
- `116` (results_FINAL.md:271, mean or delta) | 2 | 116 | +0.69 | 0.00 | 0.35 |
- `0.69` (results_FINAL.md:271, mean or delta) | 2 | 116 | +0.69 | 0.00 | 0.35 |
- `0.00` (results_FINAL.md:271, mean or delta) | 2 | 116 | +0.69 | 0.00 | 0.35 |
- `0.35` (results_FINAL.md:271, mean or delta) | 2 | 116 | +0.69 | 0.00 | 0.35 |
- `3` (results_FINAL.md:272, mean or delta) | 3 | 77 | -0.03 | 0.30 | 0.27 |
- `77` (results_FINAL.md:272, mean or delta) | 3 | 77 | -0.03 | 0.30 | 0.27 |
- `0.03` (results_FINAL.md:272, mean or delta) | 3 | 77 | -0.03 | 0.30 | 0.27 |
- `0.30` (results_FINAL.md:272, mean or delta) | 3 | 77 | -0.03 | 0.30 | 0.27 |
- `0.27` (results_FINAL.md:272, mean or delta) | 3 | 77 | -0.03 | 0.30 | 0.27 |
- `4` (results_FINAL.md:273, mean or delta) | 4 | 394 | -0.43 | 0.28 | 0.06 |
- `394` (results_FINAL.md:273, mean or delta) | 4 | 394 | -0.43 | 0.28 | 0.06 |
- `0.43` (results_FINAL.md:273, mean or delta) | 4 | 394 | -0.43 | 0.28 | 0.06 |
- `0.28` (results_FINAL.md:273, mean or delta) | 4 | 394 | -0.43 | 0.28 | 0.06 |
- `0.06` (results_FINAL.md:273, mean or delta) | 4 | 394 | -0.43 | 0.28 | 0.06 |
- `5` (results_FINAL.md:274, mean or delta) | 5 | 130 | -0.98 | 0.49 | 0.00 |
- `130` (results_FINAL.md:274, mean or delta) | 5 | 130 | -0.98 | 0.49 | 0.00 |
- `0.98` (results_FINAL.md:274, mean or delta) | 5 | 130 | -0.98 | 0.49 | 0.00 |
- `0.49` (results_FINAL.md:274, mean or delta) | 5 | 130 | -0.98 | 0.49 | 0.00 |
- `0.00` (results_FINAL.md:274, mean or delta) | 5 | 130 | -0.98 | 0.49 | 0.00 |
- `4` (results_FINAL.md:275, mean or delta) | **input insufficient (< 4)** | 194 | **+0.41** | | |
- `194` (results_FINAL.md:275, mean or delta) | **input insufficient (< 4)** | 194 | **+0.41** | | |
- `0.41` (results_FINAL.md:275, mean or delta) | **input insufficient (< 4)** | 194 | **+0.41** | | |
- `4` (results_FINAL.md:276, mean or delta) | **input sufficient (>= 4)** | 524 | **-0.56** | | |
- `524` (results_FINAL.md:276, mean or delta) | **input sufficient (>= 4)** | 524 | **-0.56** | | |
- `0.56` (results_FINAL.md:276, mean or delta) | **input sufficient (>= 4)** | 524 | **-0.56** | | |
- `1` (results_FINAL.md:278, count or denominator) Level 1 has n = 1 and is omitted from the figure.
- `1` (results_FINAL.md:278, count or denominator) Level 1 has n = 1 and is omitted from the figure.
- `718` (results_FINAL.md:280, bare number) - **Filter:** the same 718 genuine revisions as Section 4b. For each trial, walk turns 2-5;
- `2` (results_FINAL.md:280, bare number) - **Filter:** the same 718 genuine revisions as Section 4b. For each trial, walk turns 2-5;
- `5` (results_FINAL.md:280, bare number) - **Filter:** the same 718 genuine revisions as Section 4b. For each trial, walk turns 2-5;
- `1` (results_FINAL.md:283, bare number) Turn 1 stripped score. 6 -> 2 recode applied throughout.
- `6` (results_FINAL.md:283, bare number) Turn 1 stripped score. 6 -> 2 recode applied throughout.
- `2` (results_FINAL.md:283, bare number) Turn 1 stripped score. 6 -> 2 recode applied throughout.
- `11` (results_FINAL.md:287, bare number) The reliability figures in Section 11 apply.

### [results_FINAL.md] 5. TARGETED FEEDBACK

*- **Filter:** the same 718 genuine revisions as Section 4b. For each trial, walk turns 2-5;*

- `5` (results_FINAL.md:293, bare number) ## 5. TARGETED FEEDBACK
- `177` (results_FINAL.md:297, bare number) | N | 177 |
- `4.68` (results_FINAL.md:298, mean or delta) | Targeted mean | 4.68 |
- `4.43` (results_FINAL.md:299, mean or delta) | Generic mean | 4.43 |
- `0.25` (results_FINAL.md:300, mean or delta) | Delta | **+0.25** |
- `3` (results_FINAL.md:301, reliability or effect size) | Wilcoxon p | 3.75e-03 |
- `03` (results_FINAL.md:301, reliability or effect size) | Wilcoxon p | 3.75e-03 |
- `1,047` (results_FINAL.md:303, bare number) - **Filter (exact):** Load all 1,047 records from `targeted_feedback_results.jsonl`. Each record has fields `targeted_level`, `generic_next_level`, `worker_trial_id`, `turn`. For each record:
- `1` (results_FINAL.md:304, bare number) 1. Require `targeted_level` and `generic_next_level` both non-null.
- `2` (results_FINAL.md:305, bare number) 2. Compute `next_turn = turn + 1`. If next_turn > 5, exclude.
- `1` (results_FINAL.md:305, bare number) 2. Compute `next_turn = turn + 1`. If next_turn > 5, exclude.
- `5` (results_FINAL.md:305, bare number) 2. Compute `next_turn = turn + 1`. If next_turn > 5, exclude.
- `3` (results_FINAL.md:306, bare number) 3. Look up `(worker_trial_id, next_turn)` in `genuine_meta_labels.jsonl`. If `classifier_label != "GENUINE"`, exclude (the generic next-turn output was a decline, not a revision).
- `4` (results_FINAL.md:307, bare number) 4. Recode: if `targeted_level == 6`, set to 2. If `generic_next_level == 6`, set to 2.
- `6` (results_FINAL.md:307, bare number) 4. Recode: if `targeted_level == 6`, set to 2. If `generic_next_level == 6`, set to 2.
- `2` (results_FINAL.md:307, bare number) 4. Recode: if `targeted_level == 6`, set to 2. If `generic_next_level == 6`, set to 2.
- `6` (results_FINAL.md:307, bare number) 4. Recode: if `targeted_level == 6`, set to 2. If `generic_next_level == 6`, set to 2.
- `2` (results_FINAL.md:307, bare number) 4. Recode: if `targeted_level == 6`, set to 2. If `generic_next_level == 6`, set to 2.
- `5` (results_FINAL.md:308, reliability or effect size) 5. Remaining n=177 pairs. Wilcoxon signed-rank on non-zero differences.
- `177` (results_FINAL.md:308, reliability or effect size) 5. Remaining n=177 pairs. Wilcoxon signed-rank on non-zero differences.
- `0.25` (results_FINAL.md:309, p-value) - **What it measures:** "Does a targeted revision (with specific critique) produce higher quality than the model's own genuine generic revision at the next turn?" Answer: yes, by +0.25 levels unstripp
- `0.004` (results_FINAL.md:309, p-value) - **What it measures:** "Does a targeted revision (with specific critique) produce higher quality than the model's own genuine generic revision at the next turn?" Answer: yes, by +0.25 levels unstripp
- `1.16` (results_FINAL.md:309, p-value) - **What it measures:** "Does a targeted revision (with specific critique) produce higher quality than the model's own genuine generic revision at the next turn?" Answer: yes, by +0.25 levels unstripp
- `5` (results_FINAL.md:309, p-value) - **What it measures:** "Does a targeted revision (with specific critique) produce higher quality than the model's own genuine generic revision at the next turn?" Answer: yes, by +0.25 levels unstripp
- `19` (results_FINAL.md:309, p-value) - **What it measures:** "Does a targeted revision (with specific critique) produce higher quality than the model's own genuine generic revision at the next turn?" Answer: yes, by +0.25 levels unstripp
- `0.25` (results_FINAL.md:309, p-value) - **What it measures:** "Does a targeted revision (with specific critique) produce higher quality than the model's own genuine generic revision at the next turn?" Answer: yes, by +0.25 levels unstripp
- `4.43` (results_FINAL.md:309, p-value) - **What it measures:** "Does a targeted revision (with specific critique) produce higher quality than the model's own genuine generic revision at the next turn?" Answer: yes, by +0.25 levels unstripp
- `3.53` (results_FINAL.md:309, p-value) - **What it measures:** "Does a targeted revision (with specific critique) produce higher quality than the model's own genuine generic revision at the next turn?" Answer: yes, by +0.25 levels unstripp
- `9` (results_FINAL.md:309, p-value) - **What it measures:** "Does a targeted revision (with specific critique) produce higher quality than the model's own genuine generic revision at the next turn?" Answer: yes, by +0.25 levels unstripp
- `177` (results_FINAL.md:309, p-value) - **What it measures:** "Does a targeted revision (with specific critique) produce higher quality than the model's own genuine generic revision at the next turn?" Answer: yes, by +0.25 levels unstripp
- `5` (results_FINAL.md:309, p-value) - **What it measures:** "Does a targeted revision (with specific critique) produce higher quality than the model's own genuine generic revision at the next turn?" Answer: yes, by +0.25 levels unstripp
- `2.00` (results_FINAL.md:310, count or denominator) - **Supersedes:** The paper's +2.00 (n=424) used the old keyword classifier (`classify_revision()` in `analyze.py`), which let 424 records through because it failed to catch verbose declines. Those de
- `424` (results_FINAL.md:310, count or denominator) - **Supersedes:** The paper's +2.00 (n=424) used the old keyword classifier (`classify_revision()` in `analyze.py`), which let 424 records through because it failed to catch verbose declines. Those de
- `424` (results_FINAL.md:310, count or denominator) - **Supersedes:** The paper's +2.00 (n=424) used the old keyword classifier (`classify_revision()` in `analyze.py`), which let 424 records through because it failed to catch verbose declines. Those de
- `1` (results_FINAL.md:310, count or denominator) - **Supersedes:** The paper's +2.00 (n=424) used the old keyword classifier (`classify_revision()` in `analyze.py`), which let 424 records through because it failed to catch verbose declines. Those de
- `2` (results_FINAL.md:310, count or denominator) - **Supersedes:** The paper's +2.00 (n=424) used the old keyword classifier (`classify_revision()` in `analyze.py`), which let 424 records through because it failed to catch verbose declines. Those de
- `2.00` (results_FINAL.md:310, count or denominator) - **Supersedes:** The paper's +2.00 (n=424) used the old keyword classifier (`classify_revision()` in `analyze.py`), which let 424 records through because it failed to catch verbose declines. Those de
- `0.79` (results_FINAL.md:311, count or denominator) - **Discarded:** +0.79/n=106 was cited from a prior conversation session but is not reproducible from any filter on the current data files. It does not appear in `study3_results.json` or any saved out
- `106` (results_FINAL.md:311, count or denominator) - **Discarded:** +0.79/n=106 was cited from a prior conversation session but is not reproducible from any filter on the current data files. It does not appear in `study3_results.json` or any saved out

### [results_FINAL.md] 6. REVISION TAX

*- **Filter (exact):** Load all 1,047 records from `targeted_feedback_results.jsonl`. Each record has fields `targeted_level`, `generic_next_level`, `worker_trial_id`, `turn`. For each record:*

- `6` (results_FINAL.md:316, bare number) ## 6. REVISION TAX

### [results_FINAL.md] 6. REVISION TAX -- Method

*- **Filter (exact):** Load all 1,047 records from `targeted_feedback_results.jsonl`. Each record has fields `targeted_level`, `generic_next_level`, `worker_trial_id`, `turn`. For each record:*

- `3,125` (results_FINAL.md:320, percentage) - **Estimator:** Ratio-of-means aggregate (sum all waste tokens / sum all baseline tokens). NOT mean-of-ratios (which is small-denominator-sensitive and produced 3,125% outliers in early runs).
- `6` (results_FINAL.md:322, bare number) - **t*:** argmax of mean GENUINE-only quality (6->2 recoded) across turns, requiring min n >= 5 at each turn for eligibility. Result: t* = T1 for all 6 models.
- `2` (results_FINAL.md:322, bare number) - **t*:** argmax of mean GENUINE-only quality (6->2 recoded) across turns, requiring min n >= 5 at each turn for eligibility. Result: t* = T1 for all 6 models.
- `5` (results_FINAL.md:322, bare number) - **t*:** argmax of mean GENUINE-only quality (6->2 recoded) across turns, requiring min n >= 5 at each turn for eligibility. Result: t* = T1 for all 6 models.
- `6` (results_FINAL.md:322, bare number) - **t*:** argmax of mean GENUINE-only quality (6->2 recoded) across turns, requiring min n >= 5 at each turn for eligibility. Result: t* = T1 for all 6 models.
- `6` (results_FINAL.md:324, percentage) - **Supersedes:** Old Section 6 numbers (7.4%, 19.9%, 42.0%, 95.0%, 142.2%, 262.0%, aggregate 48.0%/92.4%/270,457) were transcribed from a prior session's terminal output and are not saved in any data
- `7.4` (results_FINAL.md:324, percentage) - **Supersedes:** Old Section 6 numbers (7.4%, 19.9%, 42.0%, 95.0%, 142.2%, 262.0%, aggregate 48.0%/92.4%/270,457) were transcribed from a prior session's terminal output and are not saved in any data
- `19.9` (results_FINAL.md:324, percentage) - **Supersedes:** Old Section 6 numbers (7.4%, 19.9%, 42.0%, 95.0%, 142.2%, 262.0%, aggregate 48.0%/92.4%/270,457) were transcribed from a prior session's terminal output and are not saved in any data
- `42.0` (results_FINAL.md:324, percentage) - **Supersedes:** Old Section 6 numbers (7.4%, 19.9%, 42.0%, 95.0%, 142.2%, 262.0%, aggregate 48.0%/92.4%/270,457) were transcribed from a prior session's terminal output and are not saved in any data
- `95.0` (results_FINAL.md:324, percentage) - **Supersedes:** Old Section 6 numbers (7.4%, 19.9%, 42.0%, 95.0%, 142.2%, 262.0%, aggregate 48.0%/92.4%/270,457) were transcribed from a prior session's terminal output and are not saved in any data
- `142.2` (results_FINAL.md:324, percentage) - **Supersedes:** Old Section 6 numbers (7.4%, 19.9%, 42.0%, 95.0%, 142.2%, 262.0%, aggregate 48.0%/92.4%/270,457) were transcribed from a prior session's terminal output and are not saved in any data
- `262.0` (results_FINAL.md:324, percentage) - **Supersedes:** Old Section 6 numbers (7.4%, 19.9%, 42.0%, 95.0%, 142.2%, 262.0%, aggregate 48.0%/92.4%/270,457) were transcribed from a prior session's terminal output and are not saved in any data
- `48.0` (results_FINAL.md:324, percentage) - **Supersedes:** Old Section 6 numbers (7.4%, 19.9%, 42.0%, 95.0%, 142.2%, 262.0%, aggregate 48.0%/92.4%/270,457) were transcribed from a prior session's terminal output and are not saved in any data
- `92.4` (results_FINAL.md:324, percentage) - **Supersedes:** Old Section 6 numbers (7.4%, 19.9%, 42.0%, 95.0%, 142.2%, 262.0%, aggregate 48.0%/92.4%/270,457) were transcribed from a prior session's terminal output and are not saved in any data
- `270,457` (results_FINAL.md:324, percentage) - **Supersedes:** Old Section 6 numbers (7.4%, 19.9%, 42.0%, 95.0%, 142.2%, 262.0%, aggregate 48.0%/92.4%/270,457) were transcribed from a prior session's terminal output and are not saved in any data

### [results_FINAL.md] 6. REVISION TAX -- Per-Model (Interpretation A, t*=T1 for all)

*- **Filter (exact):** Load all 1,047 records from `targeted_feedback_results.jsonl`. Each record has fields `targeted_level`, `generic_next_level`, `worker_trial_id`, `turn`. For each record:*

- `2.5` (results_FINAL.md:330, mean or delta) | gemini-2.5-flash | T1 | 30.6 | 23.4 | $0.0001 |
- `30.6` (results_FINAL.md:330, mean or delta) | gemini-2.5-flash | T1 | 30.6 | 23.4 | $0.0001 |
- `23.4` (results_FINAL.md:330, mean or delta) | gemini-2.5-flash | T1 | 30.6 | 23.4 | $0.0001 |
- `0.0001` (results_FINAL.md:330, mean or delta) | gemini-2.5-flash | T1 | 30.6 | 23.4 | $0.0001 |
- `118.9` (results_FINAL.md:331, mean or delta) | deepseek-v4 | T1 | 118.9 | 54.3 | $0.0005 |
- `54.3` (results_FINAL.md:331, mean or delta) | deepseek-v4 | T1 | 118.9 | 54.3 | $0.0005 |
- `0.0005` (results_FINAL.md:331, mean or delta) | deepseek-v4 | T1 | 118.9 | 54.3 | $0.0005 |
- `125.8` (results_FINAL.md:332, mean or delta) | gpt-4o | T1 | 125.8 | 55.7 | $0.0053 |
- `55.7` (results_FINAL.md:332, mean or delta) | gpt-4o | T1 | 125.8 | 55.7 | $0.0053 |
- `0.0053` (results_FINAL.md:332, mean or delta) | gpt-4o | T1 | 125.8 | 55.7 | $0.0053 |
- `3` (results_FINAL.md:333, mean or delta) | qwen-3-235b | T1 | 198.6 | 66.5 | $0.0009 |
- `198.6` (results_FINAL.md:333, mean or delta) | qwen-3-235b | T1 | 198.6 | 66.5 | $0.0009 |
- `66.5` (results_FINAL.md:333, mean or delta) | qwen-3-235b | T1 | 198.6 | 66.5 | $0.0009 |
- `0.0009` (results_FINAL.md:333, mean or delta) | qwen-3-235b | T1 | 198.6 | 66.5 | $0.0009 |
- `4` (results_FINAL.md:334, mean or delta) | claude-sonnet-4 | T1 | 251.6 | 71.6 | $0.0182 |
- `251.6` (results_FINAL.md:334, mean or delta) | claude-sonnet-4 | T1 | 251.6 | 71.6 | $0.0182 |
- `71.6` (results_FINAL.md:334, mean or delta) | claude-sonnet-4 | T1 | 251.6 | 71.6 | $0.0182 |
- `0.0182` (results_FINAL.md:334, mean or delta) | claude-sonnet-4 | T1 | 251.6 | 71.6 | $0.0182 |
- `3.3` (results_FINAL.md:335, mean or delta) | llama-3.3-70b | T1 | 436.0 | 81.3 | $0.0013 |
- `436.0` (results_FINAL.md:335, mean or delta) | llama-3.3-70b | T1 | 436.0 | 81.3 | $0.0013 |
- `81.3` (results_FINAL.md:335, mean or delta) | llama-3.3-70b | T1 | 436.0 | 81.3 | $0.0013 |
- `0.0013` (results_FINAL.md:335, mean or delta) | llama-3.3-70b | T1 | 436.0 | 81.3 | $0.0013 |

### [results_FINAL.md] 6. REVISION TAX -- Aggregate

*- **Filter (exact):** Load all 1,047 records from `targeted_feedback_results.jsonl`. Each record has fields `targeted_level`, `generic_next_level`, `worker_trial_id`, `turn`. For each record:*

- `62.1` (results_FINAL.md:341, percentage) | Aggregate waste fraction | **62.1%** |
- `164.2` (results_FINAL.md:342, percentage) | Aggregate tax | 164.2% |
- `653,070` (results_FINAL.md:343, bare number) | Total wasted tokens | 653,070 |
- `6` (results_FINAL.md:345, count or denominator) **t* = T1 for all 6 models.** No model benefits from undirected revision on the GENUINE-only quality trajectory. GPT-4o would show t*=T5 without the min_n floor (3 trials at T5 averaging 4.0 vs T1's 3
- `3` (results_FINAL.md:345, count or denominator) **t* = T1 for all 6 models.** No model benefits from undirected revision on the GENUINE-only quality trajectory. GPT-4o would show t*=T5 without the min_n floor (3 trials at T5 averaging 4.0 vs T1's 3
- `4.0` (results_FINAL.md:345, count or denominator) **t* = T1 for all 6 models.** No model benefits from undirected revision on the GENUINE-only quality trajectory. GPT-4o would show t*=T5 without the min_n floor (3 trials at T5 averaging 4.0 vs T1's 3
- `3.99` (results_FINAL.md:345, count or denominator) **t* = T1 for all 6 models.** No model benefits from undirected revision on the GENUINE-only quality trajectory. GPT-4o would show t*=T5 without the min_n floor (3 trials at T5 averaging 4.0 vs T1's 3
- `120` (results_FINAL.md:345, count or denominator) **t* = T1 for all 6 models.** No model benefits from undirected revision on the GENUINE-only quality trajectory. GPT-4o would show t*=T5 without the min_n floor (3 trials at T5 averaging 4.0 vs T1's 3

### [results_FINAL.md] 6. REVISION TAX -- Pricing Table (from `scripts/study3/analyze.py` lines 1515-1523, labeled "Real 2025 API pricing")

*- **Filter (exact):** Load all 1,047 records from `targeted_feedback_results.jsonl`. Each record has fields `targeted_level`, `generic_next_level`, `worker_trial_id`, `turn`. For each record:*

- `1515` (results_FINAL.md:347, bare number) ### Pricing Table (from `scripts/study3/analyze.py` lines 1515-1523, labeled "Real 2025 API pricing")
- `1523` (results_FINAL.md:347, bare number) ### Pricing Table (from `scripts/study3/analyze.py` lines 1515-1523, labeled "Real 2025 API pricing")
- `2025` (results_FINAL.md:347, bare number) ### Pricing Table (from `scripts/study3/analyze.py` lines 1515-1523, labeled "Real 2025 API pricing")
- `2.5` (results_FINAL.md:351, mean or delta) | gemini-2.5-flash | $0.40 |
- `0.40` (results_FINAL.md:351, mean or delta) | gemini-2.5-flash | $0.40 |
- `0.55` (results_FINAL.md:352, mean or delta) | deepseek-v4 | $0.55 |
- `3.3` (results_FINAL.md:353, mean or delta) | llama-3.3-70b | $0.88 |
- `0.88` (results_FINAL.md:353, mean or delta) | llama-3.3-70b | $0.88 |
- `3` (results_FINAL.md:354, mean or delta) | qwen-3-235b | $0.90 |
- `0.90` (results_FINAL.md:354, mean or delta) | qwen-3-235b | $0.90 |
- `10.00` (results_FINAL.md:355, mean or delta) | gpt-4o | $10.00 |
- `4` (results_FINAL.md:356, mean or delta) | claude-sonnet-4 | $15.00 |
- `15.00` (results_FINAL.md:356, mean or delta) | claude-sonnet-4 | $15.00 |
- `2025` (results_FINAL.md:358, percentage) **Dollar figures are pricing-tier-dominated** (Claude's $/task is 182x Gemini's despite similar waste%) and based on 2025 output-token prices (Qwen/Llama via Together.ai). These need verification agai
- `1` (results_FINAL.md:361, bare number) - **Filter (t*):** For each model, for each turn T in {1..5}, compute mean quality from `evaluator_results.jsonl` (`level`, recoded 6->2) restricted to: T1 for all 120 trials; T2-T5 only where `genuin
- `6` (results_FINAL.md:361, bare number) - **Filter (t*):** For each model, for each turn T in {1..5}, compute mean quality from `evaluator_results.jsonl` (`level`, recoded 6->2) restricted to: T1 for all 120 trials; T2-T5 only where `genuin
- `2` (results_FINAL.md:361, bare number) - **Filter (t*):** For each model, for each turn T in {1..5}, compute mean quality from `evaluator_results.jsonl` (`level`, recoded 6->2) restricted to: T1 for all 120 trials; T2-T5 only where `genuin
- `120` (results_FINAL.md:361, bare number) - **Filter (t*):** For each model, for each turn T in {1..5}, compute mean quality from `evaluator_results.jsonl` (`level`, recoded 6->2) restricted to: T1 for all 120 trials; T2-T5 only where `genuin
- `5` (results_FINAL.md:361, bare number) - **Filter (t*):** For each model, for each turn T in {1..5}, compute mean quality from `evaluator_results.jsonl` (`level`, recoded 6->2) restricted to: T1 for all 120 trials; T2-T5 only where `genuin
- `720` (results_FINAL.md:362, percentage) - **Filter (tax/waste):** For each of 720 trials, extract `token_counts[turn_idx]["output"]` for turns 1-5. Baseline tokens = sum of tokens at turns <= t* (= T1 tokens only, since t*=T1). Waste tokens
- `1` (results_FINAL.md:362, percentage) - **Filter (tax/waste):** For each of 720 trials, extract `token_counts[turn_idx]["output"]` for turns 1-5. Baseline tokens = sum of tokens at turns <= t* (= T1 tokens only, since t*=T1). Waste tokens
- `5` (results_FINAL.md:362, percentage) - **Filter (tax/waste):** For each of 720 trials, extract `token_counts[turn_idx]["output"]` for turns 1-5. Baseline tokens = sum of tokens at turns <= t* (= T1 tokens only, since t*=T1). Waste tokens
- `100` (results_FINAL.md:362, percentage) - **Filter (tax/waste):** For each of 720 trials, extract `token_counts[turn_idx]["output"]` for turns 1-5. Baseline tokens = sum of tokens at turns <= t* (= T1 tokens only, since t*=T1). Waste tokens
- `100` (results_FINAL.md:362, percentage) - **Filter (tax/waste):** For each of 720 trials, extract `token_counts[turn_idx]["output"]` for turns 1-5. Baseline tokens = sum of tokens at turns <= t* (= T1 tokens only, since t*=T1). Waste tokens
- `720` (results_FINAL.md:362, percentage) - **Filter (tax/waste):** For each of 720 trials, extract `token_counts[turn_idx]["output"]` for turns 1-5. Baseline tokens = sum of tokens at turns <= t* (= T1 tokens only, since t*=T1). Waste tokens

### [results_FINAL.md] 7. REVERSIBILITY (Human Annotation)

*- **Filter ($/task):** waste_tokens_per_trial x price_per_token. Price from the table above (output tokens only).*

- `7` (results_FINAL.md:367, bare number) ## 7. REVERSIBILITY (Human Annotation)

### [results_FINAL.md] 7. REVERSIBILITY (Human Annotation) -- Human Judgments (stripped pairs, n=50)

*- **Filter ($/task):** waste_tokens_per_trial x price_per_token. Price from the table above (output tokens only).*

- `50` (results_FINAL.md:369, count or denominator) ### Human Judgments (stripped pairs, n=50)
- `19` (results_FINAL.md:373, percentage) | T1-preferred | 19 (38%) | 22 (44%) | 41 (41%) |
- `38` (results_FINAL.md:373, percentage) | T1-preferred | 19 (38%) | 22 (44%) | 41 (41%) |
- `22` (results_FINAL.md:373, percentage) | T1-preferred | 19 (38%) | 22 (44%) | 41 (41%) |
- `44` (results_FINAL.md:373, percentage) | T1-preferred | 19 (38%) | 22 (44%) | 41 (41%) |
- `41` (results_FINAL.md:373, percentage) | T1-preferred | 19 (38%) | 22 (44%) | 41 (41%) |
- `41` (results_FINAL.md:373, percentage) | T1-preferred | 19 (38%) | 22 (44%) | 41 (41%) |
- `13` (results_FINAL.md:374, percentage) | Revision-preferred | 13 (26%) | 19 (38%) | 32 (32%) |
- `26` (results_FINAL.md:374, percentage) | Revision-preferred | 13 (26%) | 19 (38%) | 32 (32%) |
- `19` (results_FINAL.md:374, percentage) | Revision-preferred | 13 (26%) | 19 (38%) | 32 (32%) |
- `38` (results_FINAL.md:374, percentage) | Revision-preferred | 13 (26%) | 19 (38%) | 32 (32%) |
- `32` (results_FINAL.md:374, percentage) | Revision-preferred | 13 (26%) | 19 (38%) | 32 (32%) |
- `32` (results_FINAL.md:374, percentage) | Revision-preferred | 13 (26%) | 19 (38%) | 32 (32%) |
- `18` (results_FINAL.md:375, percentage) | Tie | 18 (36%) | 9 (18%) | 27 (27%) |
- `36` (results_FINAL.md:375, percentage) | Tie | 18 (36%) | 9 (18%) | 27 (27%) |
- `9` (results_FINAL.md:375, percentage) | Tie | 18 (36%) | 9 (18%) | 27 (27%) |
- `18` (results_FINAL.md:375, percentage) | Tie | 18 (36%) | 9 (18%) | 27 (27%) |
- `27` (results_FINAL.md:375, percentage) | Tie | 18 (36%) | 9 (18%) | 27 (27%) |
- `27` (results_FINAL.md:375, percentage) | Tie | 18 (36%) | 9 (18%) | 27 (27%) |
- `19` (results_FINAL.md:376, percentage) | Non-tie T1-pref | 19/32 (59.4%) | 22/41 (53.7%) | **41/73 (56.2%)** |
- `32` (results_FINAL.md:376, percentage) | Non-tie T1-pref | 19/32 (59.4%) | 22/41 (53.7%) | **41/73 (56.2%)** |
- `59.4` (results_FINAL.md:376, percentage) | Non-tie T1-pref | 19/32 (59.4%) | 22/41 (53.7%) | **41/73 (56.2%)** |
- `22` (results_FINAL.md:376, percentage) | Non-tie T1-pref | 19/32 (59.4%) | 22/41 (53.7%) | **41/73 (56.2%)** |
- `41` (results_FINAL.md:376, percentage) | Non-tie T1-pref | 19/32 (59.4%) | 22/41 (53.7%) | **41/73 (56.2%)** |
- `53.7` (results_FINAL.md:376, percentage) | Non-tie T1-pref | 19/32 (59.4%) | 22/41 (53.7%) | **41/73 (56.2%)** |
- `41` (results_FINAL.md:376, percentage) | Non-tie T1-pref | 19/32 (59.4%) | 22/41 (53.7%) | **41/73 (56.2%)** |
- `73` (results_FINAL.md:376, percentage) | Non-tie T1-pref | 19/32 (59.4%) | 22/41 (53.7%) | **41/73 (56.2%)** |
- `56.2` (results_FINAL.md:376, percentage) | Non-tie T1-pref | 19/32 (59.4%) | 22/41 (53.7%) | **41/73 (56.2%)** |
- `95` (results_FINAL.md:377, percentage) | Bootstrap 95% CI | -- | -- | [45.2%, 67.1%] |
- `45.2` (results_FINAL.md:377, percentage) | Bootstrap 95% CI | -- | -- | [45.2%, 67.1%] |
- `67.1` (results_FINAL.md:377, percentage) | Bootstrap 95% CI | -- | -- | [45.2%, 67.1%] |
- `65` (results_FINAL.md:379, percentage) **Pre-committed bar (>=65%, CI excludes 50%): NOT CLEARED.**
- `50` (results_FINAL.md:379, percentage) **Pre-committed bar (>=65%, CI excludes 50%): NOT CLEARED.**

### [results_FINAL.md] 7. REVERSIBILITY (Human Annotation) -- Inter-Annotator Agreement

*- **Filter ($/task):** waste_tokens_per_trial x price_per_token. Price from the table above (output tokens only).*

- `3` (results_FINAL.md:385, percentage) | Raw 3-way agreement | 40/50 (80%) |
- `40` (results_FINAL.md:385, percentage) | Raw 3-way agreement | 40/50 (80%) |
- `50` (results_FINAL.md:385, percentage) | Raw 3-way agreement | 40/50 (80%) |
- `80` (results_FINAL.md:385, percentage) | Raw 3-way agreement | 40/50 (80%) |
- `0.703` (results_FINAL.md:386, reliability or effect size) | Cohen's kappa (raw) | 0.703 |
- `0.701` (results_FINAL.md:387, reliability or effect size) | Cohen's kappa (decoded) | 0.701 |
- `10` (results_FINAL.md:388, bare number) | Disagreements | 10 pairs (8 = Liam tie vs Troy decided, 1 full flip, 1 Liam tie vs Troy T1) |
- `8` (results_FINAL.md:388, bare number) | Disagreements | 10 pairs (8 = Liam tie vs Troy decided, 1 full flip, 1 Liam tie vs Troy T1) |
- `1` (results_FINAL.md:388, bare number) | Disagreements | 10 pairs (8 = Liam tie vs Troy decided, 1 full flip, 1 Liam tie vs Troy T1) |
- `1` (results_FINAL.md:388, bare number) | Disagreements | 10 pairs (8 = Liam tie vs Troy decided, 1 full flip, 1 Liam tie vs Troy T1) |

### [results_FINAL.md] 7. REVERSIBILITY (Human Annotation) -- Position & Length Bias

*- **Filter ($/task):** waste_tokens_per_trial x price_per_token. Price from the table above (output tokens only).*

- `38` (results_FINAL.md:394, percentage) | A chosen (decided pairs) | 38/73 (52.1%), CI [39.7%, 63.0%] |
- `73` (results_FINAL.md:394, percentage) | A chosen (decided pairs) | 38/73 (52.1%), CI [39.7%, 63.0%] |
- `52.1` (results_FINAL.md:394, percentage) | A chosen (decided pairs) | 38/73 (52.1%), CI [39.7%, 63.0%] |
- `39.7` (results_FINAL.md:394, percentage) | A chosen (decided pairs) | 38/73 (52.1%), CI [39.7%, 63.0%] |
- `63.0` (results_FINAL.md:394, percentage) | A chosen (decided pairs) | 38/73 (52.1%), CI [39.7%, 63.0%] |
- `40` (results_FINAL.md:395, percentage) | Longer output chosen | 40/73 (54.8%) |
- `73` (results_FINAL.md:395, percentage) | Longer output chosen | 40/73 (54.8%) |
- `54.8` (results_FINAL.md:395, percentage) | Longer output chosen | 40/73 (54.8%) |

### [results_FINAL.md] 7. REVERSIBILITY (Human Annotation) -- Model Judge Comparison

*- **Filter ($/task):** waste_tokens_per_trial x price_per_token. Price from the table above (output tokens only).*

- `50` (results_FINAL.md:401, percentage) | Model judge, UNSTRIPPED (pairwise, same 50 trials) | 45/49 (91.8%) | 1 |
- `45` (results_FINAL.md:401, percentage) | Model judge, UNSTRIPPED (pairwise, same 50 trials) | 45/49 (91.8%) | 1 |
- `49` (results_FINAL.md:401, percentage) | Model judge, UNSTRIPPED (pairwise, same 50 trials) | 45/49 (91.8%) | 1 |
- `91.8` (results_FINAL.md:401, percentage) | Model judge, UNSTRIPPED (pairwise, same 50 trials) | 45/49 (91.8%) | 1 |
- `1` (results_FINAL.md:401, percentage) | Model judge, UNSTRIPPED (pairwise, same 50 trials) | 45/49 (91.8%) | 1 |
- `720` (results_FINAL.md:402, percentage) | Model judge, UNSTRIPPED (full 720, pairwise) | 669/720 (92.9%) | -- |
- `669` (results_FINAL.md:402, percentage) | Model judge, UNSTRIPPED (full 720, pairwise) | 669/720 (92.9%) | -- |
- `720` (results_FINAL.md:402, percentage) | Model judge, UNSTRIPPED (full 720, pairwise) | 669/720 (92.9%) | -- |
- `92.9` (results_FINAL.md:402, percentage) | Model judge, UNSTRIPPED (full 720, pairwise) | 669/720 (92.9%) | -- |
- `50` (results_FINAL.md:403, percentage) | Model judge, STRIPPED (pairwise, 50 pairs) | 26/46 (56.5%) | 4 |
- `26` (results_FINAL.md:403, percentage) | Model judge, STRIPPED (pairwise, 50 pairs) | 26/46 (56.5%) | 4 |
- `46` (results_FINAL.md:403, percentage) | Model judge, STRIPPED (pairwise, 50 pairs) | 26/46 (56.5%) | 4 |
- `56.5` (results_FINAL.md:403, percentage) | Model judge, STRIPPED (pairwise, 50 pairs) | 26/46 (56.5%) | 4 |
- `4` (results_FINAL.md:403, percentage) | Model judge, STRIPPED (pairwise, 50 pairs) | 26/46 (56.5%) | 4 |
- `50` (results_FINAL.md:404, percentage) | Humans, STRIPPED (50 pairs) | 41/73 (56.2%) | 27 |
- `41` (results_FINAL.md:404, percentage) | Humans, STRIPPED (50 pairs) | 41/73 (56.2%) | 27 |
- `73` (results_FINAL.md:404, percentage) | Humans, STRIPPED (50 pairs) | 41/73 (56.2%) | 27 |
- `56.2` (results_FINAL.md:404, percentage) | Humans, STRIPPED (50 pairs) | 41/73 (56.2%) | 27 |
- `27` (results_FINAL.md:404, percentage) | Humans, STRIPPED (50 pairs) | 41/73 (56.2%) | 27 |

### [results_FINAL.md] 7. REVERSIBILITY (Human Annotation) -- Human-Judge Agreement on Stripped Content

*- **Filter ($/task):** waste_tokens_per_trial x price_per_token. Price from the table above (output tokens only).*

- `31` (results_FINAL.md:410, percentage) | Liam vs judge | 31 | 77.4% | 0.541 |
- `77.4` (results_FINAL.md:410, percentage) | Liam vs judge | 31 | 77.4% | 0.541 |
- `0.541` (results_FINAL.md:410, percentage) | Liam vs judge | 31 | 77.4% | 0.541 |
- `39` (results_FINAL.md:411, percentage) | Troy vs judge | 39 | 79.5% | 0.589 |
- `79.5` (results_FINAL.md:411, percentage) | Troy vs judge | 39 | 79.5% | 0.589 |
- `0.589` (results_FINAL.md:411, percentage) | Troy vs judge | 39 | 79.5% | 0.589 |
- `30` (results_FINAL.md:412, percentage) | Human majority vs judge | 30 | 80.0% | 0.595 |
- `80.0` (results_FINAL.md:412, percentage) | Human majority vs judge | 30 | 80.0% | 0.595 |
- `0.595` (results_FINAL.md:412, percentage) | Human majority vs judge | 30 | 80.0% | 0.595 |
- `70` (results_FINAL.md:413, percentage) | All pooled vs judge | 70 | 78.6% | **0.569** |
- `78.6` (results_FINAL.md:413, percentage) | All pooled vs judge | 70 | 78.6% | **0.569** |
- `0.569` (results_FINAL.md:413, percentage) | All pooled vs judge | 70 | 78.6% | **0.569** |
- `0.07` (results_FINAL.md:415, reliability or effect size) **vs. unstripped: kappa was -0.07 to +0.02 (near zero).**
- `0.02` (results_FINAL.md:415, reliability or effect size) **vs. unstripped: kappa was -0.07 to +0.02 (near zero).**
- `50` (results_FINAL.md:421, confidence interval) - **Filter (human judgments):** Load each annotator's 50 judgments (field `judgment` in {A, B, equivalent}). Decode via `reversibility_stripped_key.json`: if judgment matches the side where `A_is == "
- `100` (results_FINAL.md:421, confidence interval) - **Filter (human judgments):** Load each annotator's 50 judgments (field `judgment` in {A, B, equivalent}). Decode via `reversibility_stripped_key.json`: if judgment matches the side where `A_is == "
- `1000` (results_FINAL.md:421, confidence interval) - **Filter (human judgments):** Load each annotator's 50 judgments (field `judgment` in {A, B, equivalent}). Decode via `reversibility_stripped_key.json`: if judgment matches the side where `A_is == "
- `100` (results_FINAL.md:421, confidence interval) - **Filter (human judgments):** Load each annotator's 50 judgments (field `judgment` in {A, B, equivalent}). Decode via `reversibility_stripped_key.json`: if judgment matches the side where `A_is == "
- `42` (results_FINAL.md:421, confidence interval) - **Filter (human judgments):** Load each annotator's 50 judgments (field `judgment` in {A, B, equivalent}). Decode via `reversibility_stripped_key.json`: if judgment matches the side where `A_is == "
- `50` (results_FINAL.md:422, reliability or effect size) - **Filter (inter-annotator):** Cohen's kappa on the 50 pairs using 3-way labels (A/B/equivalent for raw; T1/revision/tie for decoded). Disagreements = pairs where Liam != Troy.
- `3` (results_FINAL.md:422, reliability or effect size) - **Filter (inter-annotator):** Cohen's kappa on the 50 pairs using 3-way labels (A/B/equivalent for raw; T1/revision/tie for decoded). Disagreements = pairs where Liam != Troy.
- `73` (results_FINAL.md:423, count or denominator) - **Filter (position/length bias):** Among combined decided (non-tie) judgments (n=73), count how many chose output A vs B (position bias). For length: compare character counts of chosen vs unchosen o

### [results_FINAL.md] 8. META-WRAPPING ASYMMETRY

*- **Filter (model judge):** `judge_stripped_pairwise.json` has fields `pick` (A/B/tie) and `pair_id`. Decode via same key. Agreement with humans: for each (annotator, pair) where both annotator and judge gave non-tie decisions, compare decoded labels. Kappa computed on these matched pairs. Pooled = *

- `8` (results_FINAL.md:428, bare number) ## 8. META-WRAPPING ASYMMETRY
- `38` (results_FINAL.md:432, percentage) | Revision (T2-T5) | 38/50 (76%) | 24/50 (48%) | **42/50 (84%)** |
- `50` (results_FINAL.md:432, percentage) | Revision (T2-T5) | 38/50 (76%) | 24/50 (48%) | **42/50 (84%)** |
- `76` (results_FINAL.md:432, percentage) | Revision (T2-T5) | 38/50 (76%) | 24/50 (48%) | **42/50 (84%)** |
- `24` (results_FINAL.md:432, percentage) | Revision (T2-T5) | 38/50 (76%) | 24/50 (48%) | **42/50 (84%)** |
- `50` (results_FINAL.md:432, percentage) | Revision (T2-T5) | 38/50 (76%) | 24/50 (48%) | **42/50 (84%)** |
- `48` (results_FINAL.md:432, percentage) | Revision (T2-T5) | 38/50 (76%) | 24/50 (48%) | **42/50 (84%)** |
- `42` (results_FINAL.md:432, percentage) | Revision (T2-T5) | 38/50 (76%) | 24/50 (48%) | **42/50 (84%)** |
- `50` (results_FINAL.md:432, percentage) | Revision (T2-T5) | 38/50 (76%) | 24/50 (48%) | **42/50 (84%)** |
- `84` (results_FINAL.md:432, percentage) | Revision (T2-T5) | 38/50 (76%) | 24/50 (48%) | **42/50 (84%)** |
- `4` (results_FINAL.md:433, percentage) | T1 | 4/50 (8%) | 5/50 (10%) | **7/50 (14%)** |
- `50` (results_FINAL.md:433, percentage) | T1 | 4/50 (8%) | 5/50 (10%) | **7/50 (14%)** |
- `8` (results_FINAL.md:433, percentage) | T1 | 4/50 (8%) | 5/50 (10%) | **7/50 (14%)** |
- `5` (results_FINAL.md:433, percentage) | T1 | 4/50 (8%) | 5/50 (10%) | **7/50 (14%)** |
- `50` (results_FINAL.md:433, percentage) | T1 | 4/50 (8%) | 5/50 (10%) | **7/50 (14%)** |
- `10` (results_FINAL.md:433, percentage) | T1 | 4/50 (8%) | 5/50 (10%) | **7/50 (14%)** |
- `7` (results_FINAL.md:433, percentage) | T1 | 4/50 (8%) | 5/50 (10%) | **7/50 (14%)** |
- `50` (results_FINAL.md:433, percentage) | T1 | 4/50 (8%) | 5/50 (10%) | **7/50 (14%)** |
- `14` (results_FINAL.md:433, percentage) | T1 | 4/50 (8%) | 5/50 (10%) | **7/50 (14%)** |
- `14` (results_FINAL.md:436, percentage) - T1: 14%, T2: 92%, T3: 85%, T4: 79%, T5: 68%
- `92` (results_FINAL.md:436, percentage) - T1: 14%, T2: 92%, T3: 85%, T4: 79%, T5: 68%
- `85` (results_FINAL.md:436, percentage) - T1: 14%, T2: 92%, T3: 85%, T4: 79%, T5: 68%
- `79` (results_FINAL.md:436, percentage) - T1: 14%, T2: 92%, T3: 85%, T4: 79%, T5: 68%
- `68` (results_FINAL.md:436, percentage) - T1: 14%, T2: 92%, T3: 85%, T4: 79%, T5: 68%
- `56.5` (results_FINAL.md:438, percentage) **This asymmetry inflated the model judge's T1-preference from 56.5% (stripped) to 91.8% (unstripped) on the same 50 pairs.**
- `91.8` (results_FINAL.md:438, percentage) **This asymmetry inflated the model judge's T1-preference from 56.5% (stripped) to 91.8% (unstripped) on the same 50 pairs.**
- `50` (results_FINAL.md:438, percentage) **This asymmetry inflated the model judge's T1-preference from 56.5% (stripped) to 91.8% (unstripped) on the same 50 pairs.**
- `50` (results_FINAL.md:441, bare number) - **Filter:** The 50 unstripped reversibility pairs (`reversibility_human_pairs.json`). For each pair, decode T1 vs revision side via `reversibility_human_key.json`. Apply regex preamble/postamble det
- `300` (results_FINAL.md:441, bare number) - **Filter:** The 50 unstripped reversibility pairs (`reversibility_human_pairs.json`). For each pair, decode T1 vs revision side via `reversibility_human_key.json`. Apply regex preamble/postamble det
- `400` (results_FINAL.md:441, bare number) - **Filter:** The 50 unstripped reversibility pairs (`reversibility_human_pairs.json`). For each pair, decode T1 vs revision side via `reversibility_human_key.json`. Apply regex preamble/postamble det
- `1` (results_FINAL.md:441, bare number) - **Filter:** The 50 unstripped reversibility pairs (`reversibility_human_pairs.json`). For each pair, decode T1 vs revision side via `reversibility_human_key.json`. Apply regex preamble/postamble det
- `50` (results_FINAL.md:442, bare number) - **Scope:** All counts are from the 50 unstripped reversibility pairs, stored in `meta_wrapping_asymmetry.json`. Raw counts: revision preamble=38, postamble=24, either=42; T1 preamble=4, postamble=5,
- `38` (results_FINAL.md:442, bare number) - **Scope:** All counts are from the 50 unstripped reversibility pairs, stored in `meta_wrapping_asymmetry.json`. Raw counts: revision preamble=38, postamble=24, either=42; T1 preamble=4, postamble=5,
- `24` (results_FINAL.md:442, bare number) - **Scope:** All counts are from the 50 unstripped reversibility pairs, stored in `meta_wrapping_asymmetry.json`. Raw counts: revision preamble=38, postamble=24, either=42; T1 preamble=4, postamble=5,
- `42` (results_FINAL.md:442, bare number) - **Scope:** All counts are from the 50 unstripped reversibility pairs, stored in `meta_wrapping_asymmetry.json`. Raw counts: revision preamble=38, postamble=24, either=42; T1 preamble=4, postamble=5,
- `4` (results_FINAL.md:442, bare number) - **Scope:** All counts are from the 50 unstripped reversibility pairs, stored in `meta_wrapping_asymmetry.json`. Raw counts: revision preamble=38, postamble=24, either=42; T1 preamble=4, postamble=5,
- `5` (results_FINAL.md:442, bare number) - **Scope:** All counts are from the 50 unstripped reversibility pairs, stored in `meta_wrapping_asymmetry.json`. Raw counts: revision preamble=38, postamble=24, either=42; T1 preamble=4, postamble=5,
- `7` (results_FINAL.md:442, bare number) - **Scope:** All counts are from the 50 unstripped reversibility pairs, stored in `meta_wrapping_asymmetry.json`. Raw counts: revision preamble=38, postamble=24, either=42; T1 preamble=4, postamble=5,
- `2026` (results_FINAL.md:443, percentage) - **FLAG RESOLVED 2026-09-06, DO NOT CITE.** The per-turn breakdown (T1:14%, T2:92%, T3:85%,
- `09` (results_FINAL.md:443, percentage) - **FLAG RESOLVED 2026-09-06, DO NOT CITE.** The per-turn breakdown (T1:14%, T2:92%, T3:85%,
- `06` (results_FINAL.md:443, percentage) - **FLAG RESOLVED 2026-09-06, DO NOT CITE.** The per-turn breakdown (T1:14%, T2:92%, T3:85%,
- `14` (results_FINAL.md:443, percentage) - **FLAG RESOLVED 2026-09-06, DO NOT CITE.** The per-turn breakdown (T1:14%, T2:92%, T3:85%,
- `92` (results_FINAL.md:443, percentage) - **FLAG RESOLVED 2026-09-06, DO NOT CITE.** The per-turn breakdown (T1:14%, T2:92%, T3:85%,
- `85` (results_FINAL.md:443, percentage) - **FLAG RESOLVED 2026-09-06, DO NOT CITE.** The per-turn breakdown (T1:14%, T2:92%, T3:85%,
- `79` (results_FINAL.md:444, percentage) T4:79%, T5:68%) does not reproduce from any of 18 candidate scopes tested. Its T1 matches the
- `68` (results_FINAL.md:444, percentage) T4:79%, T5:68%) does not reproduce from any of 18 candidate scopes tested. Its T1 matches the
- `18` (results_FINAL.md:444, percentage) T4:79%, T5:68%) does not reproduce from any of 18 candidate scopes tested. Its T1 matches the
- `50` (results_FINAL.md:445, bare number) 50-pair scope, its T2 matches GENUINE-only, and its T5 matches the full 720-trial corpus, so
- `720` (results_FINAL.md:445, bare number) 50-pair scope, its T2 matches GENUINE-only, and its T5 matches the full 720-trial corpus, so
- `2` (results_FINAL.md:448, bare number) `paper/reference/stats_08_meta_commentary.md` section 2.

### [results_FINAL.md] 9. REVERSIBILITY -- STRATIFIED

*- **Filter:** The 50 unstripped reversibility pairs (`reversibility_human_pairs.json`). For each pair, decode T1 vs revision side via `reversibility_human_key.json`. Apply regex preamble/postamble detectors (patterns in `audit_meta_commentary.py`: PREAMBLE_PATTERNS checked against first 300 chars, P*

- `9` (results_FINAL.md:452, bare number) ## 9. REVERSIBILITY -- STRATIFIED

### [results_FINAL.md] 9. REVERSIBILITY -- STRATIFIED -- By Last Revision Turn (non-tie T1-preference, combined annotators)

*- **Filter:** The 50 unstripped reversibility pairs (`reversibility_human_pairs.json`). For each pair, decode T1 vs revision side via `reversibility_human_key.json`. Apply regex preamble/postamble detectors (patterns in `audit_meta_commentary.py`: PREAMBLE_PATTERNS checked against first 300 chars, P*

- `9` (results_FINAL.md:458, percentage) | T2 | 9 | 17 | 52.9% |
- `17` (results_FINAL.md:458, percentage) | T2 | 9 | 17 | 52.9% |
- `52.9` (results_FINAL.md:458, percentage) | T2 | 9 | 17 | 52.9% |
- `11` (results_FINAL.md:459, percentage) | T3 | 11 | 21 | 52.4% |
- `21` (results_FINAL.md:459, percentage) | T3 | 11 | 21 | 52.4% |
- `52.4` (results_FINAL.md:459, percentage) | T3 | 11 | 21 | 52.4% |
- `17` (results_FINAL.md:460, percentage) | T4 | 17 | 24 | **70.8%** |
- `24` (results_FINAL.md:460, percentage) | T4 | 17 | 24 | **70.8%** |
- `70.8` (results_FINAL.md:460, percentage) | T4 | 17 | 24 | **70.8%** |
- `4` (results_FINAL.md:461, percentage) | T5 | 4 | 11 | 36.4% |
- `11` (results_FINAL.md:461, percentage) | T5 | 4 | 11 | 36.4% |
- `36.4` (results_FINAL.md:461, percentage) | T5 | 4 | 11 | 36.4% |

### [results_FINAL.md] 9. REVERSIBILITY -- STRATIFIED -- By Domain

*- **Filter:** The 50 unstripped reversibility pairs (`reversibility_human_pairs.json`). For each pair, decode T1 vs revision side via `reversibility_human_key.json`. Apply regex preamble/postamble detectors (patterns in `audit_meta_commentary.py`: PREAMBLE_PATTERNS checked against first 300 chars, P*

- `13` (results_FINAL.md:467, percentage) | writing | 13 | 14 | **92.9%** |
- `14` (results_FINAL.md:467, percentage) | writing | 13 | 14 | **92.9%** |
- `92.9` (results_FINAL.md:467, percentage) | writing | 13 | 14 | **92.9%** |
- `8` (results_FINAL.md:468, percentage) | analysis | 8 | 12 | 66.7% |
- `12` (results_FINAL.md:468, percentage) | analysis | 8 | 12 | 66.7% |
- `66.7` (results_FINAL.md:468, percentage) | analysis | 8 | 12 | 66.7% |
- `9` (results_FINAL.md:469, percentage) | code | 9 | 20 | 45.0% |
- `20` (results_FINAL.md:469, percentage) | code | 9 | 20 | 45.0% |
- `45.0` (results_FINAL.md:469, percentage) | code | 9 | 20 | 45.0% |
- `8` (results_FINAL.md:470, percentage) | creative | 8 | 19 | 42.1% |
- `19` (results_FINAL.md:470, percentage) | creative | 8 | 19 | 42.1% |
- `42.1` (results_FINAL.md:470, percentage) | creative | 8 | 19 | 42.1% |
- `3` (results_FINAL.md:471, percentage) | data_logic | 3 | 8 | 37.5% |
- `8` (results_FINAL.md:471, percentage) | data_logic | 3 | 8 | 37.5% |
- `37.5` (results_FINAL.md:471, percentage) | data_logic | 3 | 8 | 37.5% |
- `100` (results_FINAL.md:473, bare number) - **Filter (by turn):** From `reversibility_stripped_key.json`, field `last_rev_turn` gives the turn of the revision side. Group the 100 pooled human non-tie decisions (combined annotators) by `last_r

### [results_FINAL.md] 10. SELF-REFLECTION

*- **Filter (by domain):** Same pooled non-tie decisions, grouped by `domain` field from `reversibility_stripped_key.json`.*

- `10` (results_FINAL.md:478, bare number) ## 10. SELF-REFLECTION
- `720` (results_FINAL.md:482, bare number) | N | 720 |
- `2.44` (results_FINAL.md:483, mean or delta) | Mean recommended turn | 2.44 (SD=1.39) |
- `1.39` (results_FINAL.md:483, mean or delta) | Mean recommended turn | 2.44 (SD=1.39) |
- `288` (results_FINAL.md:484, percentage) | Recommend T1 | 288/720 (40.0%) |
- `720` (results_FINAL.md:484, percentage) | Recommend T1 | 288/720 (40.0%) |
- `40.0` (results_FINAL.md:484, percentage) | Recommend T1 | 288/720 (40.0%) |
- `90.7` (results_FINAL.md:485, percentage) | Recommend not-last | 90.7% |
- `288` (results_FINAL.md:486, bare number) | Distribution | T1:288, T2:76, T3:176, T4:113, T5:67 |
- `76` (results_FINAL.md:486, bare number) | Distribution | T1:288, T2:76, T3:176, T4:113, T5:67 |
- `176` (results_FINAL.md:486, bare number) | Distribution | T1:288, T2:76, T3:176, T4:113, T5:67 |
- `113` (results_FINAL.md:486, bare number) | Distribution | T1:288, T2:76, T3:176, T4:113, T5:67 |
- `67` (results_FINAL.md:486, bare number) | Distribution | T1:288, T2:76, T3:176, T4:113, T5:67 |
- `720` (results_FINAL.md:490, bare number) - **Filter:** All 720 records in `self_reflection_results.jsonl`. Field `recommended_turn` (integer 1-5). Mean, SD, and frequency distribution computed over all 720. "Recommend not-last" = records whe
- `1` (results_FINAL.md:490, bare number) - **Filter:** All 720 records in `self_reflection_results.jsonl`. Field `recommended_turn` (integer 1-5). Mean, SD, and frequency distribution computed over all 720. "Recommend not-last" = records whe
- `5` (results_FINAL.md:490, bare number) - **Filter:** All 720 records in `self_reflection_results.jsonl`. Field `recommended_turn` (integer 1-5). Mean, SD, and frequency distribution computed over all 720. "Recommend not-last" = records whe
- `720` (results_FINAL.md:490, bare number) - **Filter:** All 720 records in `self_reflection_results.jsonl`. Field `recommended_turn` (integer 1-5). Mean, SD, and frequency distribution computed over all 720. "Recommend not-last" = records whe
- `5` (results_FINAL.md:490, bare number) - **Filter:** All 720 records in `self_reflection_results.jsonl`. Field `recommended_turn` (integer 1-5). Mean, SD, and frequency distribution computed over all 720. "Recommend not-last" = records whe

### [results_FINAL.md] 11. RELIABILITY

*- **Filter:** All 720 records in `self_reflection_results.jsonl`. Field `recommended_turn` (integer 1-5). Mean, SD, and frequency distribution computed over all 720. "Recommend not-last" = records where `recommended_turn != 5` (since T5 was the final turn in the trial).*

- `11` (results_FINAL.md:494, bare number) ## 11. RELIABILITY

### [results_FINAL.md] 11. RELIABILITY -- Human Inter-Rater Agreement (3 raters, 64 calibration items, 6->2 recode)

*- **Filter:** All 720 records in `self_reflection_results.jsonl`. Field `recommended_turn` (integer 1-5). Mean, SD, and frequency distribution computed over all 720. "Recommend not-last" = records where `recommended_turn != 5` (since T5 was the final turn in the trial).*

- `3` (results_FINAL.md:496, bare number) ### Human Inter-Rater Agreement (3 raters, 64 calibration items, 6->2 recode)
- `64` (results_FINAL.md:496, bare number) ### Human Inter-Rater Agreement (3 raters, 64 calibration items, 6->2 recode)
- `6` (results_FINAL.md:496, bare number) ### Human Inter-Rater Agreement (3 raters, 64 calibration items, 6->2 recode)
- `2` (results_FINAL.md:496, bare number) ### Human Inter-Rater Agreement (3 raters, 64 calibration items, 6->2 recode)
- `4` (results_FINAL.md:498, bare number) | Pair | QW Kappa | Binary (>=4) | Within-1 |
- `1` (results_FINAL.md:498, bare number) | Pair | QW Kappa | Binary (>=4) | Within-1 |
- `0.406` (results_FINAL.md:500, percentage) | Liam-Troy | 0.406 | 49/64 (76.6%) | 52/64 (81.2%) |
- `49` (results_FINAL.md:500, percentage) | Liam-Troy | 0.406 | 49/64 (76.6%) | 52/64 (81.2%) |
- `64` (results_FINAL.md:500, percentage) | Liam-Troy | 0.406 | 49/64 (76.6%) | 52/64 (81.2%) |
- `76.6` (results_FINAL.md:500, percentage) | Liam-Troy | 0.406 | 49/64 (76.6%) | 52/64 (81.2%) |
- `52` (results_FINAL.md:500, percentage) | Liam-Troy | 0.406 | 49/64 (76.6%) | 52/64 (81.2%) |
- `64` (results_FINAL.md:500, percentage) | Liam-Troy | 0.406 | 49/64 (76.6%) | 52/64 (81.2%) |
- `81.2` (results_FINAL.md:500, percentage) | Liam-Troy | 0.406 | 49/64 (76.6%) | 52/64 (81.2%) |
- `0.578` (results_FINAL.md:501, percentage) | Liam-Sophie | **0.578** | 50/64 (78.1%) | 61/64 (95.3%) |
- `50` (results_FINAL.md:501, percentage) | Liam-Sophie | **0.578** | 50/64 (78.1%) | 61/64 (95.3%) |
- `64` (results_FINAL.md:501, percentage) | Liam-Sophie | **0.578** | 50/64 (78.1%) | 61/64 (95.3%) |
- `78.1` (results_FINAL.md:501, percentage) | Liam-Sophie | **0.578** | 50/64 (78.1%) | 61/64 (95.3%) |
- `61` (results_FINAL.md:501, percentage) | Liam-Sophie | **0.578** | 50/64 (78.1%) | 61/64 (95.3%) |
- `64` (results_FINAL.md:501, percentage) | Liam-Sophie | **0.578** | 50/64 (78.1%) | 61/64 (95.3%) |
- `95.3` (results_FINAL.md:501, percentage) | Liam-Sophie | **0.578** | 50/64 (78.1%) | 61/64 (95.3%) |
- `0.603` (results_FINAL.md:502, percentage) | Sophie-Troy | **0.603** | 53/64 (82.8%) | 56/64 (87.5%) |
- `53` (results_FINAL.md:502, percentage) | Sophie-Troy | **0.603** | 53/64 (82.8%) | 56/64 (87.5%) |
- `64` (results_FINAL.md:502, percentage) | Sophie-Troy | **0.603** | 53/64 (82.8%) | 56/64 (87.5%) |
- `82.8` (results_FINAL.md:502, percentage) | Sophie-Troy | **0.603** | 53/64 (82.8%) | 56/64 (87.5%) |
- `56` (results_FINAL.md:502, percentage) | Sophie-Troy | **0.603** | 53/64 (82.8%) | 56/64 (87.5%) |
- `64` (results_FINAL.md:502, percentage) | Sophie-Troy | **0.603** | 53/64 (82.8%) | 56/64 (87.5%) |
- `87.5` (results_FINAL.md:502, percentage) | Sophie-Troy | **0.603** | 53/64 (82.8%) | 56/64 (87.5%) |
- `3` (results_FINAL.md:506, mean or delta) | Krippendorff's alpha (3-rater, interval) | **0.529** |
- `0.529` (results_FINAL.md:506, mean or delta) | Krippendorff's alpha (3-rater, interval) | **0.529** |
- `64` (results_FINAL.md:508, reliability or effect size) Note: Sophie re-rated all 64 items (v2) after rubric clarification. Sophie v2 uses a 1-5 scale (no level 6 assigned). Liam-Troy QW kappa of 0.406 supersedes the previously reported 0.228, which was li
- `1` (results_FINAL.md:508, reliability or effect size) Note: Sophie re-rated all 64 items (v2) after rubric clarification. Sophie v2 uses a 1-5 scale (no level 6 assigned). Liam-Troy QW kappa of 0.406 supersedes the previously reported 0.228, which was li
- `5` (results_FINAL.md:508, reliability or effect size) Note: Sophie re-rated all 64 items (v2) after rubric clarification. Sophie v2 uses a 1-5 scale (no level 6 assigned). Liam-Troy QW kappa of 0.406 supersedes the previously reported 0.228, which was li
- `6` (results_FINAL.md:508, reliability or effect size) Note: Sophie re-rated all 64 items (v2) after rubric clarification. Sophie v2 uses a 1-5 scale (no level 6 assigned). Liam-Troy QW kappa of 0.406 supersedes the previously reported 0.228, which was li
- `0.406` (results_FINAL.md:508, reliability or effect size) Note: Sophie re-rated all 64 items (v2) after rubric clarification. Sophie v2 uses a 1-5 scale (no level 6 assigned). Liam-Troy QW kappa of 0.406 supersedes the previously reported 0.228, which was li
- `0.228` (results_FINAL.md:508, reliability or effect size) Note: Sophie re-rated all 64 items (v2) after rubric clarification. Sophie v2 uses a 1-5 scale (no level 6 assigned). Liam-Troy QW kappa of 0.406 supersedes the previously reported 0.228, which was li
- `1` (results_FINAL.md:508, reliability or effect size) Note: Sophie re-rated all 64 items (v2) after rubric clarification. Sophie v2 uses a 1-5 scale (no level 6 assigned). Liam-Troy QW kappa of 0.406 supersedes the previously reported 0.228, which was li
- `6` (results_FINAL.md:508, reliability or effect size) Note: Sophie re-rated all 64 items (v2) after rubric clarification. Sophie v2 uses a 1-5 scale (no level 6 assigned). Liam-Troy QW kappa of 0.406 supersedes the previously reported 0.228, which was li
- `6` (results_FINAL.md:508, reliability or effect size) Note: Sophie re-rated all 64 items (v2) after rubric clarification. Sophie v2 uses a 1-5 scale (no level 6 assigned). Liam-Troy QW kappa of 0.406 supersedes the previously reported 0.228, which was li
- `2` (results_FINAL.md:508, reliability or effect size) Note: Sophie re-rated all 64 items (v2) after rubric clarification. Sophie v2 uses a 1-5 scale (no level 6 assigned). Liam-Troy QW kappa of 0.406 supersedes the previously reported 0.228, which was li

### [results_FINAL.md] 11. RELIABILITY -- Judge-Human Agreement

*- **Filter:** All 720 records in `self_reflection_results.jsonl`. Field `recommended_turn` (integer 1-5). Mean, SD, and frequency distribution computed over all 720. "Recommend not-last" = records where `recommended_turn != 5` (since T5 was the final turn in the trial).*

- `0.505` (results_FINAL.md:514, p-value) | Judge-human Spearman r | 0.505 (p<0.001) | `selected_judge.json` |
- `0.001` (results_FINAL.md:514, p-value) | Judge-human Spearman r | 0.505 (p<0.001) | `selected_judge.json` |
- `0.526` (results_FINAL.md:515, reliability or effect size) | Judge-human QW kappa | 0.526 | `judge_calibration.jsonl` |
- `64` (results_FINAL.md:518, reliability or effect size) - **Filter (human QW kappas):** All three raters' `level` fields on the 64 shared calibration items (all 64 items overlap across all 3 raters). Recode level 6 -> 2 before computing. Quadratic-weighted
- `64` (results_FINAL.md:518, reliability or effect size) - **Filter (human QW kappas):** All three raters' `level` fields on the 64 shared calibration items (all 64 items overlap across all 3 raters). Recode level 6 -> 2 before computing. Quadratic-weighted
- `3` (results_FINAL.md:518, reliability or effect size) - **Filter (human QW kappas):** All three raters' `level` fields on the 64 shared calibration items (all 64 items overlap across all 3 raters). Recode level 6 -> 2 before computing. Quadratic-weighted
- `6` (results_FINAL.md:518, reliability or effect size) - **Filter (human QW kappas):** All three raters' `level` fields on the 64 shared calibration items (all 64 items overlap across all 3 raters). Recode level 6 -> 2 before computing. Quadratic-weighted
- `2` (results_FINAL.md:518, reliability or effect size) - **Filter (human QW kappas):** All three raters' `level` fields on the 64 shared calibration items (all 64 items overlap across all 3 raters). Recode level 6 -> 2 before computing. Quadratic-weighted
- `1` (results_FINAL.md:518, reliability or effect size) - **Filter (human QW kappas):** All three raters' `level` fields on the 64 shared calibration items (all 64 items overlap across all 3 raters). Recode level 6 -> 2 before computing. Quadratic-weighted
- `5` (results_FINAL.md:518, reliability or effect size) - **Filter (human QW kappas):** All three raters' `level` fields on the 64 shared calibration items (all 64 items overlap across all 3 raters). Recode level 6 -> 2 before computing. Quadratic-weighted
- `4` (results_FINAL.md:518, reliability or effect size) - **Filter (human QW kappas):** All three raters' `level` fields on the 64 shared calibration items (all 64 items overlap across all 3 raters). Recode level 6 -> 2 before computing. Quadratic-weighted
- `4` (results_FINAL.md:518, reliability or effect size) - **Filter (human QW kappas):** All three raters' `level` fields on the 64 shared calibration items (all 64 items overlap across all 3 raters). Recode level 6 -> 2 before computing. Quadratic-weighted
- `1` (results_FINAL.md:518, reliability or effect size) - **Filter (human QW kappas):** All three raters' `level` fields on the 64 shared calibration items (all 64 items overlap across all 3 raters). Recode level 6 -> 2 before computing. Quadratic-weighted
- `1` (results_FINAL.md:518, reliability or effect size) - **Filter (human QW kappas):** All three raters' `level` fields on the 64 shared calibration items (all 64 items overlap across all 3 raters). Recode level 6 -> 2 before computing. Quadratic-weighted
- `3` (results_FINAL.md:519, bare number) - **Filter (Krippendorff's alpha):** Interval-scale alpha over the 3 x 64 rating matrix (after 6->2 recode).
- `64` (results_FINAL.md:519, bare number) - **Filter (Krippendorff's alpha):** Interval-scale alpha over the 3 x 64 rating matrix (after 6->2 recode).
- `6` (results_FINAL.md:519, bare number) - **Filter (Krippendorff's alpha):** Interval-scale alpha over the 3 x 64 rating matrix (after 6->2 recode).
- `2` (results_FINAL.md:519, bare number) - **Filter (Krippendorff's alpha):** Interval-scale alpha over the 3 x 64 rating matrix (after 6->2 recode).
- `4` (results_FINAL.md:520, reliability or effect size) - **Filter (Judge-human Spearman r):** From `selected_judge.json`, Claude Sonnet 4 scores vs averaged human ratings on the 64 calibration samples.
- `64` (results_FINAL.md:520, reliability or effect size) - **Filter (Judge-human Spearman r):** From `selected_judge.json`, Claude Sonnet 4 scores vs averaged human ratings on the 64 calibration samples.
- `4` (results_FINAL.md:521, reliability or effect size) - **Filter (Judge-human QW kappa):** From `judge_calibration.jsonl`, quadratic-weighted kappa between Claude Sonnet 4 scores and averaged human ratings on the 64 calibration samples.
- `64` (results_FINAL.md:521, reliability or effect size) - **Filter (Judge-human QW kappa):** From `judge_calibration.jsonl`, quadratic-weighted kappa between Claude Sonnet 4 scores and averaged human ratings on the 64 calibration samples.

### [results_FINAL.md] 12. UNCHANGED NUMBERS (not affected by classifier correction)

*- **Filter (Judge-human QW kappa):** From `judge_calibration.jsonl`, quadratic-weighted kappa between Claude Sonnet 4 scores and averaged human ratings on the 64 calibration samples.*

- `12` (results_FINAL.md:525, bare number) ## 12. UNCHANGED NUMBERS (not affected by classifier correction)
- `1` (results_FINAL.md:527, percentage) - Study 1: 3,840 trials, 99.9% vs 23.2% gate, all numbers unchanged
- `3,840` (results_FINAL.md:527, percentage) - Study 1: 3,840 trials, 99.9% vs 23.2% gate, all numbers unchanged
- `99.9` (results_FINAL.md:527, percentage) - Study 1: 3,840 trials, 99.9% vs 23.2% gate, all numbers unchanged
- `23.2` (results_FINAL.md:527, percentage) - Study 1: 3,840 trials, 99.9% vs 23.2% gate, all numbers unchanged
- `2` (results_FINAL.md:528, bare number) - Study 2: 1,728 trials, momentum numbers unchanged
- `1,728` (results_FINAL.md:528, bare number) - Study 2: 1,728 trials, momentum numbers unchanged
- `2.44` (results_FINAL.md:529, mean or delta) - Self-reflection: mean 2.44, all numbers unchanged
- `87.6` (results_FINAL.md:530, percentage) - T1 sufficiency rate: 87.6% (was "93.3%" in paper -- NEED TO VERIFY which denominator)
- `93.3` (results_FINAL.md:530, percentage) - T1 sufficiency rate: 87.6% (was "93.3%" in paper -- NEED TO VERIFY which denominator)
- `2` (results_FINAL.md:531, bare number) - DRP = Turn 2 for all degrading models: unchanged conceptually, but per-model trajectories need recomputation
- `0.97` (results_FINAL.md:532, mean or delta) - Edit ratio 0.97: unchanged (computed on raw text, not affected by classifier)

### [results_FINAL.md] Core Data Files

*- **Filter (Judge-human QW kappa):** From `judge_calibration.jsonl`, quadratic-weighted kappa between Claude Sonnet 4 scores and averaged human ratings on the 64 calibration samples.*

- `720` (results_FINAL.md:542, bare number) | `data/study3/raw_responses/worker_trials.jsonl` | 720 five-turn trials (6 models x 40 tasks x 3 runs) |
- `6` (results_FINAL.md:542, bare number) | `data/study3/raw_responses/worker_trials.jsonl` | 720 five-turn trials (6 models x 40 tasks x 3 runs) |
- `40` (results_FINAL.md:542, bare number) | `data/study3/raw_responses/worker_trials.jsonl` | 720 five-turn trials (6 models x 40 tasks x 3 runs) |
- `3` (results_FINAL.md:542, bare number) | `data/study3/raw_responses/worker_trials.jsonl` | 720 five-turn trials (6 models x 40 tasks x 3 runs) |
- `6` (results_FINAL.md:543, bare number) | `data/study3/raw_responses/evaluator_results.jsonl` | Per-turn quality scores (6-level scale, field: level) |
- `2,880` (results_FINAL.md:544, bare number) | `data/study3/raw_responses/genuine_meta_labels.jsonl` | **Definitive** GENUINE/META labels for all 2,880 post-T1 turns (corrected) |
- `720` (results_FINAL.md:545, count or denominator) | `data/study3/raw_responses/self_reflection_results.jsonl` | Self-reflection recommended turns (n=720) |
- `720` (results_FINAL.md:546, count or denominator) | `data/study3/raw_responses/reversibility_results.jsonl` | Old model-judge pairwise T1-vs-T5 (n=720, unstripped, SUPERSEDED) |
- `1047` (results_FINAL.md:547, count or denominator) | `data/study3/raw_responses/targeted_feedback_results.jsonl` | Targeted feedback scores (n=1047, filter to n=177 with corrected classifier) |
- `177` (results_FINAL.md:547, count or denominator) | `data/study3/raw_responses/targeted_feedback_results.jsonl` | Targeted feedback scores (n=1047, filter to n=177 with corrected classifier) |

### [results_FINAL.md] Reversibility Annotation Files

*- **Filter (Judge-human QW kappa):** From `judge_calibration.jsonl`, quadratic-weighted kappa between Claude Sonnet 4 scores and averaged human ratings on the 64 calibration samples.*

- `50` (results_FINAL.md:555, bare number) | `data/study3/raw_responses/reversibility_pairs_stripped.json` | 50 stripped pairs served to annotators (LLM-stripped, 3 manual fixes) |
- `3` (results_FINAL.md:555, bare number) | `data/study3/raw_responses/reversibility_pairs_stripped.json` | 50 stripped pairs served to annotators (LLM-stripped, 3 manual fixes) |
- `50` (results_FINAL.md:557, bare number) | `data/study3/raw_responses/reversibility_judgments_liam.json` | Liam's 50 judgments (final, re-graded, 18 equivalent) |
- `18` (results_FINAL.md:557, bare number) | `data/study3/raw_responses/reversibility_judgments_liam.json` | Liam's 50 judgments (final, re-graded, 18 equivalent) |
- `50` (results_FINAL.md:558, bare number) | `data/study3/raw_responses/reversibility_judgments_troy.json` | Troy's 50 judgments (9 equivalent) |
- `9` (results_FINAL.md:558, bare number) | `data/study3/raw_responses/reversibility_judgments_troy.json` | Troy's 50 judgments (9 equivalent) |
- `4` (results_FINAL.md:559, bare number) | `data/study3/raw_responses/judge_stripped_pairwise.json` | Model judge (Claude Sonnet 4) pairwise picks on stripped pairs |
- `50` (results_FINAL.md:560, bare number) | `data/study3/raw_responses/reversibility_human_pairs.json` | 50 unstripped pairs (pre-LLM-stripping) |
- `50` (results_FINAL.md:563, bare number) | `data/study3/raw_responses/annotation_dump_50pairs.txt` | Human-readable dump of all 50 stripped pairs |

### [results_FINAL.md] Calibration & Reliability

*- **Filter (Judge-human QW kappa):** From `judge_calibration.jsonl`, quadratic-weighted kappa between Claude Sonnet 4 scores and averaged human ratings on the 64 calibration samples.*

- `64` (results_FINAL.md:569, bare number) | `data/study3/raw_responses/calibration_samples.json` | 64 stratified samples for judge calibration |
- `6` (results_FINAL.md:570, bare number) | `data/study3/raw_responses/judge_calibration.jsonl` | 6-model calibration scores on 64 samples |
- `64` (results_FINAL.md:570, bare number) | `data/study3/raw_responses/judge_calibration.jsonl` | 6-model calibration scores on 64 samples |
- `4` (results_FINAL.md:571, bare number) | `data/study3/raw_responses/selected_judge.json` | Judge selection results (Claude Sonnet 4 selected) |
- `64` (results_FINAL.md:575, count or denominator) | `data/study3/raw_responses/human_ratings_sophie_v2.json` | Sophie v2 ratings (64/64, level field, 1-5 scale, re-rated after rubric clarification) |
- `64` (results_FINAL.md:575, count or denominator) | `data/study3/raw_responses/human_ratings_sophie_v2.json` | Sophie v2 ratings (64/64, level field, 1-5 scale, re-rated after rubric clarification) |
- `1` (results_FINAL.md:575, count or denominator) | `data/study3/raw_responses/human_ratings_sophie_v2.json` | Sophie v2 ratings (64/64, level field, 1-5 scale, re-rated after rubric clarification) |
- `5` (results_FINAL.md:575, count or denominator) | `data/study3/raw_responses/human_ratings_sophie_v2.json` | Sophie v2 ratings (64/64, level field, 1-5 scale, re-rated after rubric clarification) |

### [results_FINAL.md] Meta-Commentary Analysis

*- **Filter (Judge-human QW kappa):** From `judge_calibration.jsonl`, quadratic-weighted kappa between Claude Sonnet 4 scores and averaged human ratings on the 64 calibration samples.*

- `50` (results_FINAL.md:583, bare number) | `data/study3/raw_responses/stripped_rescore_results.json` | Re-scored quality on stripped content (50 balanced panel, T1+T5) |

### [results_FINAL.md] Claims to Update

*- **Filter (Judge-human QW kappa):** From `judge_calibration.jsonl`, quadratic-weighted kappa between Claude Sonnet 4 scores and averaged human ratings on the 64 calibration samples.*

- `1` (results_FINAL.md:603, count or denominator) | 1 | Quality drops 4.27->3.04 (delta -1.23, n=135) | -1.23 | -0.94 (n=50) or -0.76 stripped | **SUPERSEDED** | Results 4.1, Abstract | n=135 was old keyword classifier. New balanced panel n=50. Strip
- `4.27` (results_FINAL.md:603, count or denominator) | 1 | Quality drops 4.27->3.04 (delta -1.23, n=135) | -1.23 | -0.94 (n=50) or -0.76 stripped | **SUPERSEDED** | Results 4.1, Abstract | n=135 was old keyword classifier. New balanced panel n=50. Strip
- `3.04` (results_FINAL.md:603, count or denominator) | 1 | Quality drops 4.27->3.04 (delta -1.23, n=135) | -1.23 | -0.94 (n=50) or -0.76 stripped | **SUPERSEDED** | Results 4.1, Abstract | n=135 was old keyword classifier. New balanced panel n=50. Strip
- `1.23` (results_FINAL.md:603, count or denominator) | 1 | Quality drops 4.27->3.04 (delta -1.23, n=135) | -1.23 | -0.94 (n=50) or -0.76 stripped | **SUPERSEDED** | Results 4.1, Abstract | n=135 was old keyword classifier. New balanced panel n=50. Strip
- `135` (results_FINAL.md:603, count or denominator) | 1 | Quality drops 4.27->3.04 (delta -1.23, n=135) | -1.23 | -0.94 (n=50) or -0.76 stripped | **SUPERSEDED** | Results 4.1, Abstract | n=135 was old keyword classifier. New balanced panel n=50. Strip
- `1.23` (results_FINAL.md:603, count or denominator) | 1 | Quality drops 4.27->3.04 (delta -1.23, n=135) | -1.23 | -0.94 (n=50) or -0.76 stripped | **SUPERSEDED** | Results 4.1, Abstract | n=135 was old keyword classifier. New balanced panel n=50. Strip
- `0.94` (results_FINAL.md:603, count or denominator) | 1 | Quality drops 4.27->3.04 (delta -1.23, n=135) | -1.23 | -0.94 (n=50) or -0.76 stripped | **SUPERSEDED** | Results 4.1, Abstract | n=135 was old keyword classifier. New balanced panel n=50. Strip
- `50` (results_FINAL.md:603, count or denominator) | 1 | Quality drops 4.27->3.04 (delta -1.23, n=135) | -1.23 | -0.94 (n=50) or -0.76 stripped | **SUPERSEDED** | Results 4.1, Abstract | n=135 was old keyword classifier. New balanced panel n=50. Strip
- `0.76` (results_FINAL.md:603, count or denominator) | 1 | Quality drops 4.27->3.04 (delta -1.23, n=135) | -1.23 | -0.94 (n=50) or -0.76 stripped | **SUPERSEDED** | Results 4.1, Abstract | n=135 was old keyword classifier. New balanced panel n=50. Strip
- `4.1` (results_FINAL.md:603, count or denominator) | 1 | Quality drops 4.27->3.04 (delta -1.23, n=135) | -1.23 | -0.94 (n=50) or -0.76 stripped | **SUPERSEDED** | Results 4.1, Abstract | n=135 was old keyword classifier. New balanced panel n=50. Strip
- `135` (results_FINAL.md:603, count or denominator) | 1 | Quality drops 4.27->3.04 (delta -1.23, n=135) | -1.23 | -0.94 (n=50) or -0.76 stripped | **SUPERSEDED** | Results 4.1, Abstract | n=135 was old keyword classifier. New balanced panel n=50. Strip
- `50` (results_FINAL.md:603, count or denominator) | 1 | Quality drops 4.27->3.04 (delta -1.23, n=135) | -1.23 | -0.94 (n=50) or -0.76 stripped | **SUPERSEDED** | Results 4.1, Abstract | n=135 was old keyword classifier. New balanced panel n=50. Strip
- `0.76` (results_FINAL.md:603, count or denominator) | 1 | Quality drops 4.27->3.04 (delta -1.23, n=135) | -1.23 | -0.94 (n=50) or -0.76 stripped | **SUPERSEDED** | Results 4.1, Abstract | n=135 was old keyword classifier. New balanced panel n=50. Strip
- `0.8` (results_FINAL.md:603, count or denominator) | 1 | Quality drops 4.27->3.04 (delta -1.23, n=135) | -1.23 | -0.94 (n=50) or -0.76 stripped | **SUPERSEDED** | Results 4.1, Abstract | n=135 was old keyword classifier. New balanced panel n=50. Strip
- `2` (results_FINAL.md:604, mean or delta) | 2 | Llama improves +1.02 (T1=3.72, T5=4.74) | +1.02 | **-0.82** (T1=3.53, T5=2.71) | **SUPERSEDED** | Results 4.2, Discussion | Llama exception is GONE. Llama now degrades like others. Old +1.02 was
- `1.02` (results_FINAL.md:604, mean or delta) | 2 | Llama improves +1.02 (T1=3.72, T5=4.74) | +1.02 | **-0.82** (T1=3.53, T5=2.71) | **SUPERSEDED** | Results 4.2, Discussion | Llama exception is GONE. Llama now degrades like others. Old +1.02 was
- `3.72` (results_FINAL.md:604, mean or delta) | 2 | Llama improves +1.02 (T1=3.72, T5=4.74) | +1.02 | **-0.82** (T1=3.53, T5=2.71) | **SUPERSEDED** | Results 4.2, Discussion | Llama exception is GONE. Llama now degrades like others. Old +1.02 was
- `4.74` (results_FINAL.md:604, mean or delta) | 2 | Llama improves +1.02 (T1=3.72, T5=4.74) | +1.02 | **-0.82** (T1=3.53, T5=2.71) | **SUPERSEDED** | Results 4.2, Discussion | Llama exception is GONE. Llama now degrades like others. Old +1.02 was
- `1.02` (results_FINAL.md:604, mean or delta) | 2 | Llama improves +1.02 (T1=3.72, T5=4.74) | +1.02 | **-0.82** (T1=3.53, T5=2.71) | **SUPERSEDED** | Results 4.2, Discussion | Llama exception is GONE. Llama now degrades like others. Old +1.02 was
- `0.82` (results_FINAL.md:604, mean or delta) | 2 | Llama improves +1.02 (T1=3.72, T5=4.74) | +1.02 | **-0.82** (T1=3.53, T5=2.71) | **SUPERSEDED** | Results 4.2, Discussion | Llama exception is GONE. Llama now degrades like others. Old +1.02 was
- `3.53` (results_FINAL.md:604, mean or delta) | 2 | Llama improves +1.02 (T1=3.72, T5=4.74) | +1.02 | **-0.82** (T1=3.53, T5=2.71) | **SUPERSEDED** | Results 4.2, Discussion | Llama exception is GONE. Llama now degrades like others. Old +1.02 was
- `2.71` (results_FINAL.md:604, mean or delta) | 2 | Llama improves +1.02 (T1=3.72, T5=4.74) | +1.02 | **-0.82** (T1=3.53, T5=2.71) | **SUPERSEDED** | Results 4.2, Discussion | Llama exception is GONE. Llama now degrades like others. Old +1.02 was
- `4.2` (results_FINAL.md:604, mean or delta) | 2 | Llama improves +1.02 (T1=3.72, T5=4.74) | +1.02 | **-0.82** (T1=3.53, T5=2.71) | **SUPERSEDED** | Results 4.2, Discussion | Llama exception is GONE. Llama now degrades like others. Old +1.02 was
- `1.02` (results_FINAL.md:604, mean or delta) | 2 | Llama improves +1.02 (T1=3.72, T5=4.74) | +1.02 | **-0.82** (T1=3.53, T5=2.71) | **SUPERSEDED** | Results 4.2, Discussion | Llama exception is GONE. Llama now degrades like others. Old +1.02 was
- `3` (results_FINAL.md:605, count or denominator) | 3 | Five of six models degrade | 5/6 | **All 6 degrade** (powered: only Llama) | **SUPERSEDED** | Results 4.2 | All models with sufficient n degrade. But only Llama is powered (n=45). Others have n=
- `5` (results_FINAL.md:605, count or denominator) | 3 | Five of six models degrade | 5/6 | **All 6 degrade** (powered: only Llama) | **SUPERSEDED** | Results 4.2 | All models with sufficient n degrade. But only Llama is powered (n=45). Others have n=
- `6` (results_FINAL.md:605, count or denominator) | 3 | Five of six models degrade | 5/6 | **All 6 degrade** (powered: only Llama) | **SUPERSEDED** | Results 4.2 | All models with sufficient n degrade. But only Llama is powered (n=45). Others have n=
- `6` (results_FINAL.md:605, count or denominator) | 3 | Five of six models degrade | 5/6 | **All 6 degrade** (powered: only Llama) | **SUPERSEDED** | Results 4.2 | All models with sufficient n degrade. But only Llama is powered (n=45). Others have n=
- `4.2` (results_FINAL.md:605, count or denominator) | 3 | Five of six models degrade | 5/6 | **All 6 degrade** (powered: only Llama) | **SUPERSEDED** | Results 4.2 | All models with sufficient n degrade. But only Llama is powered (n=45). Others have n=
- `45` (results_FINAL.md:605, count or denominator) | 3 | Five of six models degrade | 5/6 | **All 6 degrade** (powered: only Llama) | **SUPERSEDED** | Results 4.2 | All models with sufficient n degrade. But only Llama is powered (n=45). Others have n=
- `0` (results_FINAL.md:605, count or denominator) | 3 | Five of six models degrade | 5/6 | **All 6 degrade** (powered: only Llama) | **SUPERSEDED** | Results 4.2 | All models with sufficient n degrade. But only Llama is powered (n=45). Others have n=
- `3` (results_FINAL.md:605, count or denominator) | 3 | Five of six models degrade | 5/6 | **All 6 degrade** (powered: only Llama) | **SUPERSEDED** | Results 4.2 | All models with sufficient n degrade. But only Llama is powered (n=45). Others have n=
- `4` (results_FINAL.md:606, percentage) | 4 | 83.7% T1-preference (blind reversibility) | 83.7% | **56.2%** (human, stripped) | **SUPERSEDED** | Results 4.3, Abstract, Discussion | 83.7% was model-judge on unstripped (inflated by meta-wrapp
- `83.7` (results_FINAL.md:606, percentage) | 4 | 83.7% T1-preference (blind reversibility) | 83.7% | **56.2%** (human, stripped) | **SUPERSEDED** | Results 4.3, Abstract, Discussion | 83.7% was model-judge on unstripped (inflated by meta-wrapp
- `83.7` (results_FINAL.md:606, percentage) | 4 | 83.7% T1-preference (blind reversibility) | 83.7% | **56.2%** (human, stripped) | **SUPERSEDED** | Results 4.3, Abstract, Discussion | 83.7% was model-judge on unstripped (inflated by meta-wrapp
- `56.2` (results_FINAL.md:606, percentage) | 4 | 83.7% T1-preference (blind reversibility) | 83.7% | **56.2%** (human, stripped) | **SUPERSEDED** | Results 4.3, Abstract, Discussion | 83.7% was model-judge on unstripped (inflated by meta-wrapp
- `4.3` (results_FINAL.md:606, percentage) | 4 | 83.7% T1-preference (blind reversibility) | 83.7% | **56.2%** (human, stripped) | **SUPERSEDED** | Results 4.3, Abstract, Discussion | 83.7% was model-judge on unstripped (inflated by meta-wrapp
- `83.7` (results_FINAL.md:606, percentage) | 4 | 83.7% T1-preference (blind reversibility) | 83.7% | **56.2%** (human, stripped) | **SUPERSEDED** | Results 4.3, Abstract, Discussion | 83.7% was model-judge on unstripped (inflated by meta-wrapp
- `56.2` (results_FINAL.md:606, percentage) | 4 | 83.7% T1-preference (blind reversibility) | 83.7% | **56.2%** (human, stripped) | **SUPERSEDED** | Results 4.3, Abstract, Discussion | 83.7% was model-judge on unstripped (inflated by meta-wrapp
- `5` (results_FINAL.md:607, percentage) | 5 | 64.3% revision-despite-sufficiency | 64.3% | **39.2%** (CI: 36-42%) | **SUPERSEDED** | Results 4.3, Abstract | Old keyword classifier counted meta as genuine. Corrected: 39.2%. Still shows model
- `64.3` (results_FINAL.md:607, percentage) | 5 | 64.3% revision-despite-sufficiency | 64.3% | **39.2%** (CI: 36-42%) | **SUPERSEDED** | Results 4.3, Abstract | Old keyword classifier counted meta as genuine. Corrected: 39.2%. Still shows model
- `64.3` (results_FINAL.md:607, percentage) | 5 | 64.3% revision-despite-sufficiency | 64.3% | **39.2%** (CI: 36-42%) | **SUPERSEDED** | Results 4.3, Abstract | Old keyword classifier counted meta as genuine. Corrected: 39.2%. Still shows model
- `39.2` (results_FINAL.md:607, percentage) | 5 | 64.3% revision-despite-sufficiency | 64.3% | **39.2%** (CI: 36-42%) | **SUPERSEDED** | Results 4.3, Abstract | Old keyword classifier counted meta as genuine. Corrected: 39.2%. Still shows model
- `36` (results_FINAL.md:607, percentage) | 5 | 64.3% revision-despite-sufficiency | 64.3% | **39.2%** (CI: 36-42%) | **SUPERSEDED** | Results 4.3, Abstract | Old keyword classifier counted meta as genuine. Corrected: 39.2%. Still shows model
- `42` (results_FINAL.md:607, percentage) | 5 | 64.3% revision-despite-sufficiency | 64.3% | **39.2%** (CI: 36-42%) | **SUPERSEDED** | Results 4.3, Abstract | Old keyword classifier counted meta as genuine. Corrected: 39.2%. Still shows model
- `4.3` (results_FINAL.md:607, percentage) | 5 | 64.3% revision-despite-sufficiency | 64.3% | **39.2%** (CI: 36-42%) | **SUPERSEDED** | Results 4.3, Abstract | Old keyword classifier counted meta as genuine. Corrected: 39.2%. Still shows model
- `39.2` (results_FINAL.md:607, percentage) | 5 | 64.3% revision-despite-sufficiency | 64.3% | **39.2%** (CI: 36-42%) | **SUPERSEDED** | Results 4.3, Abstract | Old keyword classifier counted meta as genuine. Corrected: 39.2%. Still shows model
- `6` (results_FINAL.md:608, p-value) | 6 | Targeted feedback +2.0 levels (n=424) | +2.00 | **+1.16** stripped (n=177, p=5.7e-19) | **SUPERSEDED** | Results 4.5, Abstract | Unstripped +0.25 was deflated by meta-commentary inflating generi
- `2.0` (results_FINAL.md:608, p-value) | 6 | Targeted feedback +2.0 levels (n=424) | +2.00 | **+1.16** stripped (n=177, p=5.7e-19) | **SUPERSEDED** | Results 4.5, Abstract | Unstripped +0.25 was deflated by meta-commentary inflating generi
- `424` (results_FINAL.md:608, p-value) | 6 | Targeted feedback +2.0 levels (n=424) | +2.00 | **+1.16** stripped (n=177, p=5.7e-19) | **SUPERSEDED** | Results 4.5, Abstract | Unstripped +0.25 was deflated by meta-commentary inflating generi
- `2.00` (results_FINAL.md:608, p-value) | 6 | Targeted feedback +2.0 levels (n=424) | +2.00 | **+1.16** stripped (n=177, p=5.7e-19) | **SUPERSEDED** | Results 4.5, Abstract | Unstripped +0.25 was deflated by meta-commentary inflating generi
- `1.16` (results_FINAL.md:608, p-value) | 6 | Targeted feedback +2.0 levels (n=424) | +2.00 | **+1.16** stripped (n=177, p=5.7e-19) | **SUPERSEDED** | Results 4.5, Abstract | Unstripped +0.25 was deflated by meta-commentary inflating generi
- `177` (results_FINAL.md:608, p-value) | 6 | Targeted feedback +2.0 levels (n=424) | +2.00 | **+1.16** stripped (n=177, p=5.7e-19) | **SUPERSEDED** | Results 4.5, Abstract | Unstripped +0.25 was deflated by meta-commentary inflating generi
- `5` (results_FINAL.md:608, p-value) | 6 | Targeted feedback +2.0 levels (n=424) | +2.00 | **+1.16** stripped (n=177, p=5.7e-19) | **SUPERSEDED** | Results 4.5, Abstract | Unstripped +0.25 was deflated by meta-commentary inflating generi
- `19` (results_FINAL.md:608, p-value) | 6 | Targeted feedback +2.0 levels (n=424) | +2.00 | **+1.16** stripped (n=177, p=5.7e-19) | **SUPERSEDED** | Results 4.5, Abstract | Unstripped +0.25 was deflated by meta-commentary inflating generi
- `4.5` (results_FINAL.md:608, p-value) | 6 | Targeted feedback +2.0 levels (n=424) | +2.00 | **+1.16** stripped (n=177, p=5.7e-19) | **SUPERSEDED** | Results 4.5, Abstract | Unstripped +0.25 was deflated by meta-commentary inflating generi
- `0.25` (results_FINAL.md:608, p-value) | 6 | Targeted feedback +2.0 levels (n=424) | +2.00 | **+1.16** stripped (n=177, p=5.7e-19) | **SUPERSEDED** | Results 4.5, Abstract | Unstripped +0.25 was deflated by meta-commentary inflating generi
- `1.16` (results_FINAL.md:608, p-value) | 6 | Targeted feedback +2.0 levels (n=424) | +2.00 | **+1.16** stripped (n=177, p=5.7e-19) | **SUPERSEDED** | Results 4.5, Abstract | Unstripped +0.25 was deflated by meta-commentary inflating generi
- `7` (results_FINAL.md:609, percentage) | 7 | Revision tax 57.4% waste | 57.4% | **62.1%** (Interp A, ratio-of-means) | **SUPERSEDED** | Results 4.6, Abstract | Higher than old keyword (57.4%) because Interp A counts meta-response tokens as
- `57.4` (results_FINAL.md:609, percentage) | 7 | Revision tax 57.4% waste | 57.4% | **62.1%** (Interp A, ratio-of-means) | **SUPERSEDED** | Results 4.6, Abstract | Higher than old keyword (57.4%) because Interp A counts meta-response tokens as
- `57.4` (results_FINAL.md:609, percentage) | 7 | Revision tax 57.4% waste | 57.4% | **62.1%** (Interp A, ratio-of-means) | **SUPERSEDED** | Results 4.6, Abstract | Higher than old keyword (57.4%) because Interp A counts meta-response tokens as
- `62.1` (results_FINAL.md:609, percentage) | 7 | Revision tax 57.4% waste | 57.4% | **62.1%** (Interp A, ratio-of-means) | **SUPERSEDED** | Results 4.6, Abstract | Higher than old keyword (57.4%) because Interp A counts meta-response tokens as
- `4.6` (results_FINAL.md:609, percentage) | 7 | Revision tax 57.4% waste | 57.4% | **62.1%** (Interp A, ratio-of-means) | **SUPERSEDED** | Results 4.6, Abstract | Higher than old keyword (57.4%) because Interp A counts meta-response tokens as
- `57.4` (results_FINAL.md:609, percentage) | 7 | Revision tax 57.4% waste | 57.4% | **62.1%** (Interp A, ratio-of-means) | **SUPERSEDED** | Results 4.6, Abstract | Higher than old keyword (57.4%) because Interp A counts meta-response tokens as
- `164.2` (results_FINAL.md:609, percentage) | 7 | Revision tax 57.4% waste | 57.4% | **62.1%** (Interp A, ratio-of-means) | **SUPERSEDED** | Results 4.6, Abstract | Higher than old keyword (57.4%) because Interp A counts meta-response tokens as
- `8` (results_FINAL.md:610, percentage) | 8 | Claude tax 251.6% | 251.6 | **251.6%** (unchanged under Interp A) | MATCH | Results 4.6, Table 2 | Claude unchanged; Llama now highest (436.0%). All t*=T1. |
- `251.6` (results_FINAL.md:610, percentage) | 8 | Claude tax 251.6% | 251.6 | **251.6%** (unchanged under Interp A) | MATCH | Results 4.6, Table 2 | Claude unchanged; Llama now highest (436.0%). All t*=T1. |
- `251.6` (results_FINAL.md:610, percentage) | 8 | Claude tax 251.6% | 251.6 | **251.6%** (unchanged under Interp A) | MATCH | Results 4.6, Table 2 | Claude unchanged; Llama now highest (436.0%). All t*=T1. |
- `251.6` (results_FINAL.md:610, percentage) | 8 | Claude tax 251.6% | 251.6 | **251.6%** (unchanged under Interp A) | MATCH | Results 4.6, Table 2 | Claude unchanged; Llama now highest (436.0%). All t*=T1. |
- `4.6` (results_FINAL.md:610, percentage) | 8 | Claude tax 251.6% | 251.6 | **251.6%** (unchanged under Interp A) | MATCH | Results 4.6, Table 2 | Claude unchanged; Llama now highest (436.0%). All t*=T1. |
- `2` (results_FINAL.md:610, percentage) | 8 | Claude tax 251.6% | 251.6 | **251.6%** (unchanged under Interp A) | MATCH | Results 4.6, Table 2 | Claude unchanged; Llama now highest (436.0%). All t*=T1. |
- `436.0` (results_FINAL.md:610, percentage) | 8 | Claude tax 251.6% | 251.6 | **251.6%** (unchanged under Interp A) | MATCH | Results 4.6, Table 2 | Claude unchanged; Llama now highest (436.0%). All t*=T1. |
- `9` (results_FINAL.md:611, mean or delta) | 9 | Llama t*=2 | T2 | **T1** | **SUPERSEDED** | Results 4.6 | Llama no longer improves; t*=T1 like all others |
- `2` (results_FINAL.md:611, mean or delta) | 9 | Llama t*=2 | T2 | **T1** | **SUPERSEDED** | Results 4.6 | Llama no longer improves; t*=T1 like all others |
- `4.6` (results_FINAL.md:611, mean or delta) | 9 | Llama t*=2 | T2 | **T1** | **SUPERSEDED** | Results 4.6 | Llama no longer improves; t*=T1 like all others |
- `10` (results_FINAL.md:612, percentage) | 10 | Akrasia gap: 48pp between knowledge and action | 48pp | Much smaller | **SUPERSEDED** | Results 4.3, Discussion | 83.7% -> 56.2%, 64.3% -> 39.2%. Gap collapses. Akrasia framing needs substantia
- `4.3` (results_FINAL.md:612, percentage) | 10 | Akrasia gap: 48pp between knowledge and action | 48pp | Much smaller | **SUPERSEDED** | Results 4.3, Discussion | 83.7% -> 56.2%, 64.3% -> 39.2%. Gap collapses. Akrasia framing needs substantia
- `83.7` (results_FINAL.md:612, percentage) | 10 | Akrasia gap: 48pp between knowledge and action | 48pp | Much smaller | **SUPERSEDED** | Results 4.3, Discussion | 83.7% -> 56.2%, 64.3% -> 39.2%. Gap collapses. Akrasia framing needs substantia
- `56.2` (results_FINAL.md:612, percentage) | 10 | Akrasia gap: 48pp between knowledge and action | 48pp | Much smaller | **SUPERSEDED** | Results 4.3, Discussion | 83.7% -> 56.2%, 64.3% -> 39.2%. Gap collapses. Akrasia framing needs substantia
- `64.3` (results_FINAL.md:612, percentage) | 10 | Akrasia gap: 48pp between knowledge and action | 48pp | Much smaller | **SUPERSEDED** | Results 4.3, Discussion | 83.7% -> 56.2%, 64.3% -> 39.2%. Gap collapses. Akrasia framing needs substantia
- `39.2` (results_FINAL.md:612, percentage) | 10 | Akrasia gap: 48pp between knowledge and action | 48pp | Much smaller | **SUPERSEDED** | Results 4.3, Discussion | 83.7% -> 56.2%, 64.3% -> 39.2%. Gap collapses. Akrasia framing needs substantia
- `11` (results_FINAL.md:613, percentage) | 11 | Self-reflection mean 2.44, 40% T1 | 2.44 | **2.44** | UNCHANGED | Results 4.3 | No change needed |
- `2.44` (results_FINAL.md:613, percentage) | 11 | Self-reflection mean 2.44, 40% T1 | 2.44 | **2.44** | UNCHANGED | Results 4.3 | No change needed |
- `40` (results_FINAL.md:613, percentage) | 11 | Self-reflection mean 2.44, 40% T1 | 2.44 | **2.44** | UNCHANGED | Results 4.3 | No change needed |
- `2.44` (results_FINAL.md:613, percentage) | 11 | Self-reflection mean 2.44, 40% T1 | 2.44 | **2.44** | UNCHANGED | Results 4.3 | No change needed |
- `2.44` (results_FINAL.md:613, percentage) | 11 | Self-reflection mean 2.44, 40% T1 | 2.44 | **2.44** | UNCHANGED | Results 4.3 | No change needed |
- `4.3` (results_FINAL.md:613, percentage) | 11 | Self-reflection mean 2.44, 40% T1 | 2.44 | **2.44** | UNCHANGED | Results 4.3 | No change needed |
- `12` (results_FINAL.md:614, mean or delta) | 12 | Edit ratio 0.97 | 0.97 | **0.97** | UNCHANGED | Results 4.4 | No change needed |
- `0.97` (results_FINAL.md:614, mean or delta) | 12 | Edit ratio 0.97 | 0.97 | **0.97** | UNCHANGED | Results 4.4 | No change needed |
- `0.97` (results_FINAL.md:614, mean or delta) | 12 | Edit ratio 0.97 | 0.97 | **0.97** | UNCHANGED | Results 4.4 | No change needed |
- `0.97` (results_FINAL.md:614, mean or delta) | 12 | Edit ratio 0.97 | 0.97 | **0.97** | UNCHANGED | Results 4.4 | No change needed |
- `4.4` (results_FINAL.md:614, mean or delta) | 12 | Edit ratio 0.97 | 0.97 | **0.97** | UNCHANGED | Results 4.4 | No change needed |
- `13` (results_FINAL.md:615, mean or delta) | 13 | Content drift slopes (instruction adherence, semantic similarity, word count) | various | UNKNOWN | **NEEDS RECOMPUTATION** | Results 4.4 | These were computed on all turns including meta. Need
- `4.4` (results_FINAL.md:615, mean or delta) | 13 | Content drift slopes (instruction adherence, semantic similarity, word count) | various | UNKNOWN | **NEEDS RECOMPUTATION** | Results 4.4 | These were computed on all turns including meta. Need
- `14` (results_FINAL.md:616, percentage) | 14 | Structural features drop 56% | 56% | UNKNOWN | **NEEDS RECOMPUTATION** | Results 4.4 | Same issue |
- `56` (results_FINAL.md:616, percentage) | 14 | Structural features drop 56% | 56% | UNKNOWN | **NEEDS RECOMPUTATION** | Results 4.4 | Same issue |
- `56` (results_FINAL.md:616, percentage) | 14 | Structural features drop 56% | 56% | UNKNOWN | **NEEDS RECOMPUTATION** | Results 4.4 | Same issue |
- `4.4` (results_FINAL.md:616, percentage) | 14 | Structural features drop 56% | 56% | UNKNOWN | **NEEDS RECOMPUTATION** | Results 4.4 | Same issue |
- `15` (results_FINAL.md:617, percentage) | 15 | Constraint loss 58.5% | 58.5% | UNKNOWN | **NEEDS RECOMPUTATION** | Results 4.4 | Same issue |
- `58.5` (results_FINAL.md:617, percentage) | 15 | Constraint loss 58.5% | 58.5% | UNKNOWN | **NEEDS RECOMPUTATION** | Results 4.4 | Same issue |
- `58.5` (results_FINAL.md:617, percentage) | 15 | Constraint loss 58.5% | 58.5% | UNKNOWN | **NEEDS RECOMPUTATION** | Results 4.4 | Same issue |
- `4.4` (results_FINAL.md:617, percentage) | 15 | Constraint loss 58.5% | 58.5% | UNKNOWN | **NEEDS RECOMPUTATION** | Results 4.4 | Same issue |
- `16` (results_FINAL.md:618, percentage) | 16 | Enterprise projection $21K-$72K | $21-72K | Lower (tax% dropped) | **SUPERSEDED** | Results 4.6 | Recompute from corrected per-model $/task waste |
- `21` (results_FINAL.md:618, percentage) | 16 | Enterprise projection $21K-$72K | $21-72K | Lower (tax% dropped) | **SUPERSEDED** | Results 4.6 | Recompute from corrected per-model $/task waste |
- `4.6` (results_FINAL.md:618, percentage) | 16 | Enterprise projection $21K-$72K | $21-72K | Lower (tax% dropped) | **SUPERSEDED** | Results 4.6 | Recompute from corrected per-model $/task waste |
- `17` (results_FINAL.md:619, mean or delta) | 17 | DRP = Turn 2 for all degrading models | T2 | Likely unchanged conceptually | **NEEDS VERIFICATION** | Results 4.1 | Verify on corrected GENUINE-only trajectories |
- `2` (results_FINAL.md:619, mean or delta) | 17 | DRP = Turn 2 for all degrading models | T2 | Likely unchanged conceptually | **NEEDS VERIFICATION** | Results 4.1 | Verify on corrected GENUINE-only trajectories |
- `4.1` (results_FINAL.md:619, mean or delta) | 17 | DRP = Turn 2 for all degrading models | T2 | Likely unchanged conceptually | **NEEDS VERIFICATION** | Results 4.1 | Verify on corrected GENUINE-only trajectories |
- `18` (results_FINAL.md:620, percentage) | 18 | T1 sufficiency 93.3% | 93.3% | **87.6%** (or both: check denominator) | **NEEDS VERIFICATION** | Methods, Results 4.3 | Paper may have used different denominator or pre-6->2 recoding |
- `93.3` (results_FINAL.md:620, percentage) | 18 | T1 sufficiency 93.3% | 93.3% | **87.6%** (or both: check denominator) | **NEEDS VERIFICATION** | Methods, Results 4.3 | Paper may have used different denominator or pre-6->2 recoding |
- `93.3` (results_FINAL.md:620, percentage) | 18 | T1 sufficiency 93.3% | 93.3% | **87.6%** (or both: check denominator) | **NEEDS VERIFICATION** | Methods, Results 4.3 | Paper may have used different denominator or pre-6->2 recoding |
- `87.6` (results_FINAL.md:620, percentage) | 18 | T1 sufficiency 93.3% | 93.3% | **87.6%** (or both: check denominator) | **NEEDS VERIFICATION** | Methods, Results 4.3 | Paper may have used different denominator or pre-6->2 recoding |
- `4.3` (results_FINAL.md:620, percentage) | 18 | T1 sufficiency 93.3% | 93.3% | **87.6%** (or both: check denominator) | **NEEDS VERIFICATION** | Methods, Results 4.3 | Paper may have used different denominator or pre-6->2 recoding |
- `6` (results_FINAL.md:620, percentage) | 18 | T1 sufficiency 93.3% | 93.3% | **87.6%** (or both: check denominator) | **NEEDS VERIFICATION** | Methods, Results 4.3 | Paper may have used different denominator or pre-6->2 recoding |
- `2` (results_FINAL.md:620, percentage) | 18 | T1 sufficiency 93.3% | 93.3% | **87.6%** (or both: check denominator) | **NEEDS VERIFICATION** | Methods, Results 4.3 | Paper may have used different denominator or pre-6->2 recoding |
- `19` (results_FINAL.md:621, percentage) | 19 | Study 1: 99.9% vs 23.2% | 99.9/23.2 | **99.9/23.2** | UNCHANGED | Results (appendix) | |
- `1` (results_FINAL.md:621, percentage) | 19 | Study 1: 99.9% vs 23.2% | 99.9/23.2 | **99.9/23.2** | UNCHANGED | Results (appendix) | |
- `99.9` (results_FINAL.md:621, percentage) | 19 | Study 1: 99.9% vs 23.2% | 99.9/23.2 | **99.9/23.2** | UNCHANGED | Results (appendix) | |
- `23.2` (results_FINAL.md:621, percentage) | 19 | Study 1: 99.9% vs 23.2% | 99.9/23.2 | **99.9/23.2** | UNCHANGED | Results (appendix) | |
- `99.9` (results_FINAL.md:621, percentage) | 19 | Study 1: 99.9% vs 23.2% | 99.9/23.2 | **99.9/23.2** | UNCHANGED | Results (appendix) | |
- `23.2` (results_FINAL.md:621, percentage) | 19 | Study 1: 99.9% vs 23.2% | 99.9/23.2 | **99.9/23.2** | UNCHANGED | Results (appendix) | |
- `99.9` (results_FINAL.md:621, percentage) | 19 | Study 1: 99.9% vs 23.2% | 99.9/23.2 | **99.9/23.2** | UNCHANGED | Results (appendix) | |
- `23.2` (results_FINAL.md:621, percentage) | 19 | Study 1: 99.9% vs 23.2% | 99.9/23.2 | **99.9/23.2** | UNCHANGED | Results (appendix) | |
- `20` (results_FINAL.md:622, percentage) | 20 | Study 2: GPT-4o 98% momentum | 98% | **98%** | UNCHANGED | Results (appendix) | |
- `2` (results_FINAL.md:622, percentage) | 20 | Study 2: GPT-4o 98% momentum | 98% | **98%** | UNCHANGED | Results (appendix) | |
- `98` (results_FINAL.md:622, percentage) | 20 | Study 2: GPT-4o 98% momentum | 98% | **98%** | UNCHANGED | Results (appendix) | |
- `98` (results_FINAL.md:622, percentage) | 20 | Study 2: GPT-4o 98% momentum | 98% | **98%** | UNCHANGED | Results (appendix) | |
- `98` (results_FINAL.md:622, percentage) | 20 | Study 2: GPT-4o 98% momentum | 98% | **98%** | UNCHANGED | Results (appendix) | |
- `21` (results_FINAL.md:623, percentage) | 21 | QWK 0.228, binary 73.4% | 0.228/73.4 | QW kappa 0.41-0.60 (3 pairs), binary 76.6-82.8%, alpha 0.529 | **SUPERSEDED** | Methods 3.3 | Old 0.228 was linear-weighted, 2-rater, no 6->2 recode. Now 
- `0.228` (results_FINAL.md:623, percentage) | 21 | QWK 0.228, binary 73.4% | 0.228/73.4 | QW kappa 0.41-0.60 (3 pairs), binary 76.6-82.8%, alpha 0.529 | **SUPERSEDED** | Methods 3.3 | Old 0.228 was linear-weighted, 2-rater, no 6->2 recode. Now 
- `73.4` (results_FINAL.md:623, percentage) | 21 | QWK 0.228, binary 73.4% | 0.228/73.4 | QW kappa 0.41-0.60 (3 pairs), binary 76.6-82.8%, alpha 0.529 | **SUPERSEDED** | Methods 3.3 | Old 0.228 was linear-weighted, 2-rater, no 6->2 recode. Now 
- `0.228` (results_FINAL.md:623, percentage) | 21 | QWK 0.228, binary 73.4% | 0.228/73.4 | QW kappa 0.41-0.60 (3 pairs), binary 76.6-82.8%, alpha 0.529 | **SUPERSEDED** | Methods 3.3 | Old 0.228 was linear-weighted, 2-rater, no 6->2 recode. Now 
- `73.4` (results_FINAL.md:623, percentage) | 21 | QWK 0.228, binary 73.4% | 0.228/73.4 | QW kappa 0.41-0.60 (3 pairs), binary 76.6-82.8%, alpha 0.529 | **SUPERSEDED** | Methods 3.3 | Old 0.228 was linear-weighted, 2-rater, no 6->2 recode. Now 
- `0.41` (results_FINAL.md:623, percentage) | 21 | QWK 0.228, binary 73.4% | 0.228/73.4 | QW kappa 0.41-0.60 (3 pairs), binary 76.6-82.8%, alpha 0.529 | **SUPERSEDED** | Methods 3.3 | Old 0.228 was linear-weighted, 2-rater, no 6->2 recode. Now 
- `0.60` (results_FINAL.md:623, percentage) | 21 | QWK 0.228, binary 73.4% | 0.228/73.4 | QW kappa 0.41-0.60 (3 pairs), binary 76.6-82.8%, alpha 0.529 | **SUPERSEDED** | Methods 3.3 | Old 0.228 was linear-weighted, 2-rater, no 6->2 recode. Now 
- `3` (results_FINAL.md:623, percentage) | 21 | QWK 0.228, binary 73.4% | 0.228/73.4 | QW kappa 0.41-0.60 (3 pairs), binary 76.6-82.8%, alpha 0.529 | **SUPERSEDED** | Methods 3.3 | Old 0.228 was linear-weighted, 2-rater, no 6->2 recode. Now 
- `76.6` (results_FINAL.md:623, percentage) | 21 | QWK 0.228, binary 73.4% | 0.228/73.4 | QW kappa 0.41-0.60 (3 pairs), binary 76.6-82.8%, alpha 0.529 | **SUPERSEDED** | Methods 3.3 | Old 0.228 was linear-weighted, 2-rater, no 6->2 recode. Now 
- `82.8` (results_FINAL.md:623, percentage) | 21 | QWK 0.228, binary 73.4% | 0.228/73.4 | QW kappa 0.41-0.60 (3 pairs), binary 76.6-82.8%, alpha 0.529 | **SUPERSEDED** | Methods 3.3 | Old 0.228 was linear-weighted, 2-rater, no 6->2 recode. Now 
- `0.529` (results_FINAL.md:623, percentage) | 21 | QWK 0.228, binary 73.4% | 0.228/73.4 | QW kappa 0.41-0.60 (3 pairs), binary 76.6-82.8%, alpha 0.529 | **SUPERSEDED** | Methods 3.3 | Old 0.228 was linear-weighted, 2-rater, no 6->2 recode. Now 
- `3.3` (results_FINAL.md:623, percentage) | 21 | QWK 0.228, binary 73.4% | 0.228/73.4 | QW kappa 0.41-0.60 (3 pairs), binary 76.6-82.8%, alpha 0.529 | **SUPERSEDED** | Methods 3.3 | Old 0.228 was linear-weighted, 2-rater, no 6->2 recode. Now 
- `0.228` (results_FINAL.md:623, percentage) | 21 | QWK 0.228, binary 73.4% | 0.228/73.4 | QW kappa 0.41-0.60 (3 pairs), binary 76.6-82.8%, alpha 0.529 | **SUPERSEDED** | Methods 3.3 | Old 0.228 was linear-weighted, 2-rater, no 6->2 recode. Now 
- `2` (results_FINAL.md:623, percentage) | 21 | QWK 0.228, binary 73.4% | 0.228/73.4 | QW kappa 0.41-0.60 (3 pairs), binary 76.6-82.8%, alpha 0.529 | **SUPERSEDED** | Methods 3.3 | Old 0.228 was linear-weighted, 2-rater, no 6->2 recode. Now 
- `6` (results_FINAL.md:623, percentage) | 21 | QWK 0.228, binary 73.4% | 0.228/73.4 | QW kappa 0.41-0.60 (3 pairs), binary 76.6-82.8%, alpha 0.529 | **SUPERSEDED** | Methods 3.3 | Old 0.228 was linear-weighted, 2-rater, no 6->2 recode. Now 
- `2` (results_FINAL.md:623, percentage) | 21 | QWK 0.228, binary 73.4% | 0.228/73.4 | QW kappa 0.41-0.60 (3 pairs), binary 76.6-82.8%, alpha 0.529 | **SUPERSEDED** | Methods 3.3 | Old 0.228 was linear-weighted, 2-rater, no 6->2 recode. Now 
- `3` (results_FINAL.md:623, percentage) | 21 | QWK 0.228, binary 73.4% | 0.228/73.4 | QW kappa 0.41-0.60 (3 pairs), binary 76.6-82.8%, alpha 0.529 | **SUPERSEDED** | Methods 3.3 | Old 0.228 was linear-weighted, 2-rater, no 6->2 recode. Now 
- `6` (results_FINAL.md:623, percentage) | 21 | QWK 0.228, binary 73.4% | 0.228/73.4 | QW kappa 0.41-0.60 (3 pairs), binary 76.6-82.8%, alpha 0.529 | **SUPERSEDED** | Methods 3.3 | Old 0.228 was linear-weighted, 2-rater, no 6->2 recode. Now 
- `2` (results_FINAL.md:623, percentage) | 21 | QWK 0.228, binary 73.4% | 0.228/73.4 | QW kappa 0.41-0.60 (3 pairs), binary 76.6-82.8%, alpha 0.529 | **SUPERSEDED** | Methods 3.3 | Old 0.228 was linear-weighted, 2-rater, no 6->2 recode. Now 

### [results_FINAL.md] NEW Claims (not in current draft)

*- **Filter (Judge-human QW kappa):** From `judge_calibration.jsonl`, quadratic-weighted kappa between Claude Sonnet 4 scores and averaged human ratings on the 64 calibration samples.*

- `91.8` (results_FINAL.md:629, percentage) | N1 | Meta-commentary inflates LLM-judge T1-preference | 91.8% -> 56.5% stripped (same 50 pairs) | Results (new) | Major methods contribution. Model judges are unreliable on revision comparison unles
- `56.5` (results_FINAL.md:629, percentage) | N1 | Meta-commentary inflates LLM-judge T1-preference | 91.8% -> 56.5% stripped (same 50 pairs) | Results (new) | Major methods contribution. Model judges are unreliable on revision comparison unles
- `50` (results_FINAL.md:629, percentage) | N1 | Meta-commentary inflates LLM-judge T1-preference | 91.8% -> 56.5% stripped (same 50 pairs) | Results (new) | Major methods contribution. Model judges are unreliable on revision comparison unles
- `84` (results_FINAL.md:630, percentage) | N2 | Meta-wrapping asymmetry | 84% revision, 14% T1 | Results/Methods (new) | Confound for any LLM-as-judge revision study. |
- `14` (results_FINAL.md:630, percentage) | N2 | Meta-wrapping asymmetry | 84% revision, 14% T1 | Results/Methods (new) | Confound for any LLM-as-judge revision study. |
- `56.2` (results_FINAL.md:631, percentage) | N3 | Human reversibility with inter-annotator agreement | 56.2%, kappa=0.703 | Results (new) | Replaces model-judge reversibility as primary evidence. |
- `0.703` (results_FINAL.md:631, percentage) | N3 | Human reversibility with inter-annotator agreement | 56.2%, kappa=0.703 | Results (new) | Replaces model-judge reversibility as primary evidence. |
- `1.4` (results_FINAL.md:632, percentage) | N4 | Classifier difficulty (verbose decline) | 1.4% correction rate, 85 trials reclassified | Methods (new) | The keyword/LLM classifier gap is itself a finding about model behavior. |
- `85` (results_FINAL.md:632, percentage) | N4 | Classifier difficulty (verbose decline) | 1.4% correction rate, 85 trials reclassified | Methods (new) | The keyword/LLM classifier gap is itself a finding about model behavior. |
- `81` (results_FINAL.md:633, percentage) | N5 | Cliff is 81% content degradation, 19% meta-inflation | -0.76 stripped vs -0.94 | Results (new) | Validates cliff survives meta-stripping. |
- `19` (results_FINAL.md:633, percentage) | N5 | Cliff is 81% content degradation, 19% meta-inflation | -0.76 stripped vs -0.94 | Results (new) | Validates cliff survives meta-stripping. |
- `0.76` (results_FINAL.md:633, percentage) | N5 | Cliff is 81% content degradation, 19% meta-inflation | -0.76 stripped vs -0.94 | Results (new) | Validates cliff survives meta-stripping. |
- `0.94` (results_FINAL.md:633, percentage) | N5 | Cliff is 81% content degradation, 19% meta-inflation | -0.76 stripped vs -0.94 | Results (new) | Validates cliff survives meta-stripping. |
- `0` (results_FINAL.md:634, reliability or effect size) | N6 | Human-judge agreement improves from kappa ~0 to 0.57 after stripping | 0.57 | Results (new) | Demonstrates meta-commentary is the source of judge-human disagreement. |
- `0.57` (results_FINAL.md:634, reliability or effect size) | N6 | Human-judge agreement improves from kappa ~0 to 0.57 after stripping | 0.57 | Results (new) | Demonstrates meta-commentary is the source of judge-human disagreement. |
- `0.57` (results_FINAL.md:634, reliability or effect size) | N6 | Human-judge agreement improves from kappa ~0 to 0.57 after stripping | 0.57 | Results (new) | Demonstrates meta-commentary is the source of judge-human disagreement. |
- `6` (results_FINAL.md:640, bare number) All numbers below use corrected LLM classifier (GENUINE-only), 6->2 recode, computed fresh from source data.
- `2` (results_FINAL.md:640, bare number) All numbers below use corrected LLM classifier (GENUINE-only), 6->2 recode, computed fresh from source data.

### [results_FINAL.md] S1. Content Drift Slopes (GENUINE-only)

*- **Filter (Judge-human QW kappa):** From `judge_calibration.jsonl`, quadratic-weighted kappa between Claude Sonnet 4 scores and averaged human ratings on the 64 calibration samples.*

- `50.9` (results_FINAL.md:646, p-value) | Word count slope | -50.9/turn (p=2.8e-19, n=576) | **+19.4/turn** (p=1.9e-8, n=356) | **YES: FLIPS SIGN** |
- `2` (results_FINAL.md:646, p-value) | Word count slope | -50.9/turn (p=2.8e-19, n=576) | **+19.4/turn** (p=1.9e-8, n=356) | **YES: FLIPS SIGN** |
- `19` (results_FINAL.md:646, p-value) | Word count slope | -50.9/turn (p=2.8e-19, n=576) | **+19.4/turn** (p=1.9e-8, n=356) | **YES: FLIPS SIGN** |
- `576` (results_FINAL.md:646, p-value) | Word count slope | -50.9/turn (p=2.8e-19, n=576) | **+19.4/turn** (p=1.9e-8, n=356) | **YES: FLIPS SIGN** |
- `19.4` (results_FINAL.md:646, p-value) | Word count slope | -50.9/turn (p=2.8e-19, n=576) | **+19.4/turn** (p=1.9e-8, n=356) | **YES: FLIPS SIGN** |
- `1` (results_FINAL.md:646, p-value) | Word count slope | -50.9/turn (p=2.8e-19, n=576) | **+19.4/turn** (p=1.9e-8, n=356) | **YES: FLIPS SIGN** |
- `8` (results_FINAL.md:646, p-value) | Word count slope | -50.9/turn (p=2.8e-19, n=576) | **+19.4/turn** (p=1.9e-8, n=356) | **YES: FLIPS SIGN** |
- `356` (results_FINAL.md:646, p-value) | Word count slope | -50.9/turn (p=2.8e-19, n=576) | **+19.4/turn** (p=1.9e-8, n=356) | **YES: FLIPS SIGN** |
- `289` (results_FINAL.md:647, bare number) | Word count T1->T5 | 289->186 | **289->341** | **YES: INCREASES** |
- `186` (results_FINAL.md:647, bare number) | Word count T1->T5 | 289->186 | **289->341** | **YES: INCREASES** |
- `289` (results_FINAL.md:647, bare number) | Word count T1->T5 | 289->186 | **289->341** | **YES: INCREASES** |
- `341` (results_FINAL.md:647, bare number) | Word count T1->T5 | 289->186 | **289->341** | **YES: INCREASES** |
- `1980` (results_FINAL.md:648, bare number) | Char count T1->T5 | 1980->1280 | **1980->2426** | **YES: INCREASES** |
- `1280` (results_FINAL.md:648, bare number) | Char count T1->T5 | 1980->1280 | **1980->2426** | **YES: INCREASES** |
- `1980` (results_FINAL.md:648, bare number) | Char count T1->T5 | 1980->1280 | **1980->2426** | **YES: INCREASES** |
- `2426` (results_FINAL.md:648, bare number) | Char count T1->T5 | 1980->1280 | **1980->2426** | **YES: INCREASES** |
- `50` (results_FINAL.md:650, mean or delta) **The word-count decline was entirely a meta-response artifact.** Short decline messages (50-200 chars) drove the old -50.9 slope. Genuine revisions are LONGER than T1.
- `200` (results_FINAL.md:650, mean or delta) **The word-count decline was entirely a meta-response artifact.** Short decline messages (50-200 chars) drove the old -50.9 slope. Genuine revisions are LONGER than T1.
- `50.9` (results_FINAL.md:650, mean or delta) **The word-count decline was entirely a meta-response artifact.** Short decline messages (50-200 chars) drove the old -50.9 slope. Genuine revisions are LONGER than T1.
- `720` (results_FINAL.md:652, count or denominator) - **Filter:** For each trial, include T1 (all 720) and turns 2-5 only where `genuine_meta_labels.jsonl` has `classifier_label == "GENUINE"`. Per-trial slope via `scipy.stats.linregress` on (turn, word
- `2` (results_FINAL.md:652, count or denominator) - **Filter:** For each trial, include T1 (all 720) and turns 2-5 only where `genuine_meta_labels.jsonl` has `classifier_label == "GENUINE"`. Per-trial slope via `scipy.stats.linregress` on (turn, word
- `5` (results_FINAL.md:652, count or denominator) - **Filter:** For each trial, include T1 (all 720) and turns 2-5 only where `genuine_meta_labels.jsonl` has `classifier_label == "GENUINE"`. Per-trial slope via `scipy.stats.linregress` on (turn, word
- `356` (results_FINAL.md:652, count or denominator) - **Filter:** For each trial, include T1 (all 720) and turns 2-5 only where `genuine_meta_labels.jsonl` has `classifier_label == "GENUINE"`. Per-trial slope via `scipy.stats.linregress` on (turn, word

### [results_FINAL.md] S2. Structural Features (GENUINE-only)

*- **Filter:** For each trial, include T1 (all 720) and turns 2-5 only where `genuine_meta_labels.jsonl` has `classifier_label == "GENUINE"`. Per-trial slope via `scipy.stats.linregress` on (turn, word_count). T-test on n=356 per-trial slopes.*

- `7.47` (results_FINAL.md:658, mean or delta) | T1 | 7.47 | 12.52 | 720 |
- `12.52` (results_FINAL.md:658, mean or delta) | T1 | 7.47 | 12.52 | 720 |
- `720` (results_FINAL.md:658, mean or delta) | T1 | 7.47 | 12.52 | 720 |
- `5.0` (results_FINAL.md:659, mean or delta) | T2 | ~5.0 | 10.34 | 283 |
- `10.34` (results_FINAL.md:659, mean or delta) | T2 | ~5.0 | 10.34 | 283 |
- `283` (results_FINAL.md:659, mean or delta) | T2 | ~5.0 | 10.34 | 283 |
- `3.3` (results_FINAL.md:660, mean or delta) | T5 | ~3.3 | 9.00 | 96 |
- `9.00` (results_FINAL.md:660, mean or delta) | T5 | ~3.3 | 9.00 | 96 |
- `96` (results_FINAL.md:660, mean or delta) | T5 | ~3.3 | 9.00 | 96 |
- `56` (results_FINAL.md:664, percentage) | T1->T5 drop | ~56% | **28.1%** |
- `28.1` (results_FINAL.md:664, percentage) | T1->T5 drop | ~56% | **28.1%** |
- `28.1` (results_FINAL.md:667, percentage) - Note: old and new `total_structure` definitions differ slightly (old counted fewer features). The 28.1% drop and new raw counts are the definitive numbers.

### [results_FINAL.md] S3. Constraint Satisfaction (GENUINE-only)

*- **Filter:** Regex counts of headers, bullets, numbered items, code blocks, bold phrases per response. GENUINE-only turns. Old numbers used all turns including meta-responses (which had minimal structure).*

- `0.077` (results_FINAL.md:673, p-value) | Constraint recall slope | -0.077 (p=7.4e-40, n=576) | **+0.002** (p=0.58, NS, n=356) | **YES: GOES NS** |
- `7` (results_FINAL.md:673, p-value) | Constraint recall slope | -0.077 (p=7.4e-40, n=576) | **+0.002** (p=0.58, NS, n=356) | **YES: GOES NS** |
- `40` (results_FINAL.md:673, p-value) | Constraint recall slope | -0.077 (p=7.4e-40, n=576) | **+0.002** (p=0.58, NS, n=356) | **YES: GOES NS** |
- `576` (results_FINAL.md:673, p-value) | Constraint recall slope | -0.077 (p=7.4e-40, n=576) | **+0.002** (p=0.58, NS, n=356) | **YES: GOES NS** |
- `0.002` (results_FINAL.md:673, p-value) | Constraint recall slope | -0.077 (p=7.4e-40, n=576) | **+0.002** (p=0.58, NS, n=356) | **YES: GOES NS** |
- `0.58` (results_FINAL.md:673, p-value) | Constraint recall slope | -0.077 (p=7.4e-40, n=576) | **+0.002** (p=0.58, NS, n=356) | **YES: GOES NS** |
- `356` (results_FINAL.md:673, p-value) | Constraint recall slope | -0.077 (p=7.4e-40, n=576) | **+0.002** (p=0.58, NS, n=356) | **YES: GOES NS** |
- `10` (results_FINAL.md:674, percentage) | >10% drop T1->T5 | 58.5% | **17.7%** (17/96) | **YES** |
- `58.5` (results_FINAL.md:674, percentage) | >10% drop T1->T5 | 58.5% | **17.7%** (17/96) | **YES** |
- `17.7` (results_FINAL.md:674, percentage) | >10% drop T1->T5 | 58.5% | **17.7%** (17/96) | **YES** |
- `17` (results_FINAL.md:674, percentage) | >10% drop T1->T5 | 58.5% | **17.7%** (17/96) | **YES** |
- `96` (results_FINAL.md:674, percentage) | >10% drop T1->T5 | 58.5% | **17.7%** (17/96) | **YES** |
- `0.491` (results_FINAL.md:675, mean or delta) | Recall T1 | 0.491 | 0.491 | Match |
- `0.491` (results_FINAL.md:675, mean or delta) | Recall T1 | 0.491 | 0.491 | Match |
- `0.290` (results_FINAL.md:676, mean or delta) | Recall T5 | 0.290 | **0.483** | **YES** |
- `0.483` (results_FINAL.md:676, mean or delta) | Recall T5 | 0.290 | **0.483** | **YES** |
- `0.077` (results_FINAL.md:678, percentage) **Constraint loss was largely a meta-response artifact.** Meta-responses (short declines) have near-zero keyword overlap with the task prompt, which drove the old -0.077 slope. Genuine revisions maint
- `49` (results_FINAL.md:678, percentage) **Constraint loss was largely a meta-response artifact.** Meta-responses (short declines) have near-zero keyword overlap with the task prompt, which drove the old -0.077 slope. Genuine revisions maint
- `4` (results_FINAL.md:680, p-value) - **Filter:** Keyword overlap (words >= 4 chars) between `task_prompt` and response. GENUINE-only turns. Per-trial slope via polyfit. >10% drop = trials with balanced panel (GENUINE at T5) where T1_re
- `10` (results_FINAL.md:680, p-value) - **Filter:** Keyword overlap (words >= 4 chars) between `task_prompt` and response. GENUINE-only turns. Per-trial slope via polyfit. >10% drop = trials with balanced panel (GENUINE at T5) where T1_re
- `0.10` (results_FINAL.md:680, p-value) - **Filter:** Keyword overlap (words >= 4 chars) between `task_prompt` and response. GENUINE-only turns. Per-trial slope via polyfit. >10% drop = trials with balanced panel (GENUINE at T5) where T1_re

### [results_FINAL.md] S4. Edit Ratio & Semantic Similarity (GENUINE-only)

*- **Filter:** Keyword overlap (words >= 4 chars) between `task_prompt` and response. GENUINE-only turns. Per-trial slope via polyfit. >10% drop = trials with balanced panel (GENUINE at T5) where T1_recall - T5_recall > 0.10.*

- `0.97` (results_FINAL.md:686, mean or delta) | Edit ratio (overall) | 0.97 | **0.61** | **YES** |
- `0.61` (results_FINAL.md:686, mean or delta) | Edit ratio (overall) | 0.97 | **0.61** | **YES** |
- `0.51` (results_FINAL.md:687, mean or delta) | Semantic drift T1->T5 | 0.51->0.37 | **0.54->0.48** | Moderate |
- `0.37` (results_FINAL.md:687, mean or delta) | Semantic drift T1->T5 | 0.51->0.37 | **0.54->0.48** | Moderate |
- `0.54` (results_FINAL.md:687, mean or delta) | Semantic drift T1->T5 | 0.51->0.37 | **0.54->0.48** | Moderate |
- `0.48` (results_FINAL.md:687, mean or delta) | Semantic drift T1->T5 | 0.51->0.37 | **0.54->0.48** | Moderate |
- `0.048` (results_FINAL.md:688, p-value) | Drift slope | -0.048 (p=2.9e-11, n=428) | **-0.038** (p=3.0e-21, n=205) | Minor |
- `2` (results_FINAL.md:688, p-value) | Drift slope | -0.048 (p=2.9e-11, n=428) | **-0.038** (p=3.0e-21, n=205) | Minor |
- `11` (results_FINAL.md:688, p-value) | Drift slope | -0.048 (p=2.9e-11, n=428) | **-0.038** (p=3.0e-21, n=205) | Minor |
- `428` (results_FINAL.md:688, p-value) | Drift slope | -0.048 (p=2.9e-11, n=428) | **-0.038** (p=3.0e-21, n=205) | Minor |
- `0.038` (results_FINAL.md:688, p-value) | Drift slope | -0.048 (p=2.9e-11, n=428) | **-0.038** (p=3.0e-21, n=205) | Minor |
- `3` (results_FINAL.md:688, p-value) | Drift slope | -0.048 (p=2.9e-11, n=428) | **-0.038** (p=3.0e-21, n=205) | Minor |
- `21` (results_FINAL.md:688, p-value) | Drift slope | -0.048 (p=2.9e-11, n=428) | **-0.038** (p=3.0e-21, n=205) | Minor |
- `205` (results_FINAL.md:688, p-value) | Drift slope | -0.048 (p=2.9e-11, n=428) | **-0.038** (p=3.0e-21, n=205) | Minor |
- `0.97` (results_FINAL.md:690, percentage) The old 0.97 edit ratio included meta-responses which repeat content verbatim. Genuine revisions change ~61% of the text.
- `61` (results_FINAL.md:690, percentage) The old 0.97 edit ratio included meta-responses which repeat content verbatim. Genuine revisions change ~61% of the text.
- `1` (results_FINAL.md:692, bare number) - **Filter (edit ratio):** `difflib.SequenceMatcher` ratio between consecutive GENUINE turns. 1 - ratio = fraction changed.

### [results_FINAL.md] S5. Per-Model Table

*- **Filter (semantic sim):** Word-overlap Jaccard between T1 and each GENUINE turn. Per-trial slope via polyfit.*

- `2` (results_FINAL.md:697, count or denominator) Already in Section 2 (balanced panel n=50: Llama 45, Qwen 3, Claude 2, others 0). No further recomputation needed.
- `50` (results_FINAL.md:697, count or denominator) Already in Section 2 (balanced panel n=50: Llama 45, Qwen 3, Claude 2, others 0). No further recomputation needed.
- `45` (results_FINAL.md:697, count or denominator) Already in Section 2 (balanced panel n=50: Llama 45, Qwen 3, Claude 2, others 0). No further recomputation needed.
- `3` (results_FINAL.md:697, count or denominator) Already in Section 2 (balanced panel n=50: Llama 45, Qwen 3, Claude 2, others 0). No further recomputation needed.
- `2` (results_FINAL.md:697, count or denominator) Already in Section 2 (balanced panel n=50: Llama 45, Qwen 3, Claude 2, others 0). No further recomputation needed.
- `0` (results_FINAL.md:697, count or denominator) Already in Section 2 (balanced panel n=50: Llama 45, Qwen 3, Claude 2, others 0). No further recomputation needed.

### [results_FINAL.md] S5. Per-Model Table -- Survival to T5 (GENUINE-only)

*- **Filter (semantic sim):** Word-overlap Jaccard between T1 and each GENUINE turn. Per-trial slope via polyfit.*

- `3.3` (results_FINAL.md:703, percentage) | llama-3.3-70b | 64/120 (53.3%) |
- `64` (results_FINAL.md:703, percentage) | llama-3.3-70b | 64/120 (53.3%) |
- `120` (results_FINAL.md:703, percentage) | llama-3.3-70b | 64/120 (53.3%) |
- `53.3` (results_FINAL.md:703, percentage) | llama-3.3-70b | 64/120 (53.3%) |
- `4` (results_FINAL.md:704, percentage) | claude-sonnet-4 | 15/120 (12.5%) |
- `15` (results_FINAL.md:704, percentage) | claude-sonnet-4 | 15/120 (12.5%) |
- `120` (results_FINAL.md:704, percentage) | claude-sonnet-4 | 15/120 (12.5%) |
- `12.5` (results_FINAL.md:704, percentage) | claude-sonnet-4 | 15/120 (12.5%) |
- `7` (results_FINAL.md:705, percentage) | deepseek-v4 | 7/120 (5.8%) |
- `120` (results_FINAL.md:705, percentage) | deepseek-v4 | 7/120 (5.8%) |
- `5.8` (results_FINAL.md:705, percentage) | deepseek-v4 | 7/120 (5.8%) |
- `3` (results_FINAL.md:706, percentage) | qwen-3-235b | 6/120 (5.0%) |
- `6` (results_FINAL.md:706, percentage) | qwen-3-235b | 6/120 (5.0%) |
- `120` (results_FINAL.md:706, percentage) | qwen-3-235b | 6/120 (5.0%) |
- `5.0` (results_FINAL.md:706, percentage) | qwen-3-235b | 6/120 (5.0%) |
- `3` (results_FINAL.md:707, percentage) | gpt-4o | 3/120 (2.5%) |
- `120` (results_FINAL.md:707, percentage) | gpt-4o | 3/120 (2.5%) |
- `2.5` (results_FINAL.md:707, percentage) | gpt-4o | 3/120 (2.5%) |
- `2.5` (results_FINAL.md:708, percentage) | gemini-2.5-flash | 1/120 (0.8%) |
- `1` (results_FINAL.md:708, percentage) | gemini-2.5-flash | 1/120 (0.8%) |
- `120` (results_FINAL.md:708, percentage) | gemini-2.5-flash | 1/120 (0.8%) |
- `0.8` (results_FINAL.md:708, percentage) | gemini-2.5-flash | 1/120 (0.8%) |

### [results_FINAL.md] S5. Per-Model Table -- DRP (first turn where GENUINE mean quality < T1, min n>=5)

*- **Filter (semantic sim):** Word-overlap Jaccard between T1 and each GENUINE turn. Per-trial slope via polyfit.*

- `5` (results_FINAL.md:710, bare number) ### DRP (first turn where GENUINE mean quality < T1, min n>=5)
- `4` (results_FINAL.md:714, mean or delta) | claude-sonnet-4 | T2 | 4.28 |
- `4.28` (results_FINAL.md:714, mean or delta) | claude-sonnet-4 | T2 | 4.28 |
- `3.99` (results_FINAL.md:715, mean or delta) | gpt-4o | T2 | 3.99 |
- `3.3` (results_FINAL.md:716, mean or delta) | llama-3.3-70b | T2 | 3.75 |
- `3.75` (results_FINAL.md:716, mean or delta) | llama-3.3-70b | T2 | 3.75 |
- `3` (results_FINAL.md:717, mean or delta) | qwen-3-235b | T2 | 4.35 |
- `4.35` (results_FINAL.md:717, mean or delta) | qwen-3-235b | T2 | 4.35 |
- `4.48` (results_FINAL.md:718, mean or delta) | deepseek-v4 | T3 | 4.48 |
- `2.5` (results_FINAL.md:719, mean or delta) | gemini-2.5-flash | -- (n<5 at all post-T1 turns) | 3.82 |
- `5` (results_FINAL.md:719, mean or delta) | gemini-2.5-flash | -- (n<5 at all post-T1 turns) | 3.82 |
- `3.82` (results_FINAL.md:719, mean or delta) | gemini-2.5-flash | -- (n<5 at all post-T1 turns) | 3.82 |
- `6` (results_FINAL.md:721, bare number) - **Filter:** Mean quality per turn restricted to GENUINE responses, 6->2 recode. DRP = first turn with mean < T1 mean AND n >= 5.
- `2` (results_FINAL.md:721, bare number) - **Filter:** Mean quality per turn restricted to GENUINE responses, 6->2 recode. DRP = first turn with mean < T1 mean AND n >= 5.
- `5` (results_FINAL.md:721, bare number) - **Filter:** Mean quality per turn restricted to GENUINE responses, 6->2 recode. DRP = first turn with mean < T1 mean AND n >= 5.

### [results_FINAL.md] S6. LOCF Analysis (GENUINE carry-forward)

*- **Filter:** Mean quality per turn restricted to GENUINE responses, 6->2 recode. DRP = first turn with mean < T1 mean AND n >= 5.*

- `4.27` (results_FINAL.md:727, mean or delta) | LOCF T1 | ~4.27 | **4.11** |
- `4.11` (results_FINAL.md:727, mean or delta) | LOCF T1 | ~4.27 | **4.11** |
- `2.95` (results_FINAL.md:728, mean or delta) | LOCF T5 | ~2.95 | **3.60** |
- `3.60` (results_FINAL.md:728, mean or delta) | LOCF T5 | ~2.95 | **3.60** |
- `1.32` (results_FINAL.md:729, p-value) | LOCF delta | -1.32 | **-0.51** (p=1.0e-32) |
- `0.51` (results_FINAL.md:729, p-value) | LOCF delta | -1.32 | **-0.51** (p=1.0e-32) |
- `1` (results_FINAL.md:729, p-value) | LOCF delta | -1.32 | **-0.51** (p=1.0e-32) |
- `32` (results_FINAL.md:729, p-value) | LOCF delta | -1.32 | **-0.51** (p=1.0e-32) |
- `0.30` (results_FINAL.md:730, p-value) | LOCF delta (stripped) | -- | **-0.30** (p=3.8e-18) |
- `3` (results_FINAL.md:730, p-value) | LOCF delta (stripped) | -- | **-0.30** (p=3.8e-18) |
- `18` (results_FINAL.md:730, p-value) | LOCF delta (stripped) | -- | **-0.30** (p=3.8e-18) |
- `3.60` (results_FINAL.md:732, percentage) - **Stripped sensitivity:** LOCF T5 rises from 3.60 to 3.81 after stripping (meta was penalizing quality). Delta shrinks 41% but remains highly significant. See Stripped Sensitivity Analysis M3.
- `3.81` (results_FINAL.md:732, percentage) - **Stripped sensitivity:** LOCF T5 rises from 3.60 to 3.81 after stripping (meta was penalizing quality). Delta shrinks 41% but remains highly significant. See Stripped Sensitivity Analysis M3.
- `41` (results_FINAL.md:732, percentage) - **Stripped sensitivity:** LOCF T5 rises from 3.60 to 3.81 after stripping (meta was penalizing quality). Delta shrinks 41% but remains highly significant. See Stripped Sensitivity Analysis M3.
- `720` (results_FINAL.md:733, reliability or effect size) - **Filter:** For each trial, carry forward the last GENUINE-turn quality score. If a turn is META, its LOCF score = the previous GENUINE score. All 720 trials, Wilcoxon on paired T1-vs-T5.

### [results_FINAL.md] S7. Enterprise Projection (Interp A pricing)

*- **Filter:** For each trial, carry forward the last GENUINE-turn quality score. If a turn is META, its LOCF score = the previous GENUINE score. All 720 trials, Wilcoxon on paired T1-vs-T5.*

- `500` (results_FINAL.md:737, bare number) | Model | $/task waste | Monthly (500-person org) | Annual |
- `2.5` (results_FINAL.md:739, mean or delta) | gemini-2.5-flash | $0.0001 | $27 | $323 |
- `0.0001` (results_FINAL.md:739, mean or delta) | gemini-2.5-flash | $0.0001 | $27 | $323 |
- `27` (results_FINAL.md:739, mean or delta) | gemini-2.5-flash | $0.0001 | $27 | $323 |
- `323` (results_FINAL.md:739, mean or delta) | gemini-2.5-flash | $0.0001 | $27 | $323 |
- `0.0005` (results_FINAL.md:740, mean or delta) | deepseek-v4 | $0.0005 | $164 | $1,969 |
- `164` (results_FINAL.md:740, mean or delta) | deepseek-v4 | $0.0005 | $164 | $1,969 |
- `1,969` (results_FINAL.md:740, mean or delta) | deepseek-v4 | $0.0005 | $164 | $1,969 |
- `3` (results_FINAL.md:741, mean or delta) | qwen-3-235b | $0.0009 | $271 | $3,250 |
- `0.0009` (results_FINAL.md:741, mean or delta) | qwen-3-235b | $0.0009 | $271 | $3,250 |
- `271` (results_FINAL.md:741, mean or delta) | qwen-3-235b | $0.0009 | $271 | $3,250 |
- `3,250` (results_FINAL.md:741, mean or delta) | qwen-3-235b | $0.0009 | $271 | $3,250 |
- `3.3` (results_FINAL.md:742, mean or delta) | llama-3.3-70b | $0.0013 | $390 | $4,680 |
- `0.0013` (results_FINAL.md:742, mean or delta) | llama-3.3-70b | $0.0013 | $390 | $4,680 |
- `390` (results_FINAL.md:742, mean or delta) | llama-3.3-70b | $0.0013 | $390 | $4,680 |
- `4,680` (results_FINAL.md:742, mean or delta) | llama-3.3-70b | $0.0013 | $390 | $4,680 |
- `0.0053` (results_FINAL.md:743, mean or delta) | gpt-4o | $0.0053 | $1,581 | $18,972 |
- `1,581` (results_FINAL.md:743, mean or delta) | gpt-4o | $0.0053 | $1,581 | $18,972 |
- `18,972` (results_FINAL.md:743, mean or delta) | gpt-4o | $0.0053 | $1,581 | $18,972 |
- `4` (results_FINAL.md:744, mean or delta) | claude-sonnet-4 | $0.0182 | $5,473 | $65,678 |
- `0.0182` (results_FINAL.md:744, mean or delta) | claude-sonnet-4 | $0.0182 | $5,473 | $65,678 |
- `5,473` (results_FINAL.md:744, mean or delta) | claude-sonnet-4 | $0.0182 | $5,473 | $65,678 |
- `65,678` (results_FINAL.md:744, mean or delta) | claude-sonnet-4 | $0.0182 | $5,473 | $65,678 |
- `500` (results_FINAL.md:746, bare number) - **Assumptions:** 500 employees, 30 tasks/employee/day, 20 workdays/month. 2025 API output-token pricing. Interp A (meta tokens count as waste).
- `30` (results_FINAL.md:746, bare number) - **Assumptions:** 500 employees, 30 tasks/employee/day, 20 workdays/month. 2025 API output-token pricing. Interp A (meta tokens count as waste).
- `20` (results_FINAL.md:746, bare number) - **Assumptions:** 500 employees, 30 tasks/employee/day, 20 workdays/month. 2025 API output-token pricing. Interp A (meta tokens count as waste).
- `2025` (results_FINAL.md:746, bare number) - **Assumptions:** 500 employees, 30 tasks/employee/day, 20 workdays/month. 2025 API output-token pricing. Interp A (meta tokens count as waste).
- `2025` (results_FINAL.md:748, bare number) - **FLAG:** Dollar figures are pricing-tier-dominated and based on 2025 rates. Range is $323-$65,678/year depending entirely on which model.
- `323` (results_FINAL.md:748, bare number) - **FLAG:** Dollar figures are pricing-tier-dominated and based on 2025 rates. Range is $323-$65,678/year depending entirely on which model.
- `65,678` (results_FINAL.md:748, bare number) - **FLAG:** Dollar figures are pricing-tier-dominated and based on 2025 rates. Range is $323-$65,678/year depending entirely on which model.

### [results_FINAL.md] S8. T1 Sufficiency Rate Discrepancy -- RESOLVED

*- **Filter:** For each trial, carry forward the last GENUINE-turn quality score. If a turn is META, its LOCF score = the previous GENUINE score. All 720 trials, Wilcoxon on paired T1-vs-T5.*

- `93.3` (results_FINAL.md:754, percentage) | Paper draft (93.3%) | 672/720 | Raw scale: level >= 4 includes level 6 as "sufficient" |
- `672` (results_FINAL.md:754, percentage) | Paper draft (93.3%) | 672/720 | Raw scale: level >= 4 includes level 6 as "sufficient" |
- `720` (results_FINAL.md:754, percentage) | Paper draft (93.3%) | 672/720 | Raw scale: level >= 4 includes level 6 as "sufficient" |
- `4` (results_FINAL.md:754, percentage) | Paper draft (93.3%) | 672/720 | Raw scale: level >= 4 includes level 6 as "sufficient" |
- `6` (results_FINAL.md:754, percentage) | Paper draft (93.3%) | 672/720 | Raw scale: level >= 4 includes level 6 as "sufficient" |
- `87.6` (results_FINAL.md:755, percentage) | Corrected (87.6%) | 631/720 | 6->2 recode: level 6 becomes 2 (below threshold) |
- `631` (results_FINAL.md:755, percentage) | Corrected (87.6%) | 631/720 | 6->2 recode: level 6 becomes 2 (below threshold) |
- `720` (results_FINAL.md:755, percentage) | Corrected (87.6%) | 631/720 | 6->2 recode: level 6 becomes 2 (below threshold) |
- `6` (results_FINAL.md:755, percentage) | Corrected (87.6%) | 631/720 | 6->2 recode: level 6 becomes 2 (below threshold) |
- `2` (results_FINAL.md:755, percentage) | Corrected (87.6%) | 631/720 | 6->2 recode: level 6 becomes 2 (below threshold) |
- `6` (results_FINAL.md:755, percentage) | Corrected (87.6%) | 631/720 | 6->2 recode: level 6 becomes 2 (below threshold) |
- `2` (results_FINAL.md:755, percentage) | Corrected (87.6%) | 631/720 | 6->2 recode: level 6 becomes 2 (below threshold) |
- `41` (results_FINAL.md:756, bare number) | Difference | 41 trials | Had T1 level=6 ("Overdone"), recoded to 2 |
- `6` (results_FINAL.md:756, bare number) | Difference | 41 trials | Had T1 level=6 ("Overdone"), recoded to 2 |
- `2` (results_FINAL.md:756, bare number) | Difference | 41 trials | Had T1 level=6 ("Overdone"), recoded to 2 |
- `87.6` (results_FINAL.md:758, percentage) **Use 87.6%** (consistent with all other corrected numbers using 6->2 recode).
- `6` (results_FINAL.md:758, percentage) **Use 87.6%** (consistent with all other corrected numbers using 6->2 recode).
- `2` (results_FINAL.md:758, percentage) **Use 87.6%** (consistent with all other corrected numbers using 6->2 recode).

### [results_FINAL.md] S9. Pooled Revision-Only Trajectory (GENUINE-only)

*- **Filter:** For each trial, carry forward the last GENUINE-turn quality score. If a turn is META, its LOCF score = the previous GENUINE score. All 720 trials, Wilcoxon on paired T1-vs-T5.*

- `4.34` (results_FINAL.md:764, mean or delta) | T1 | 4.34 | **4.11** | 720 |
- `4.11` (results_FINAL.md:764, mean or delta) | T1 | 4.34 | **4.11** | 720 |
- `720` (results_FINAL.md:764, mean or delta) | T1 | 4.34 | **4.11** | 720 |
- `3.40` (results_FINAL.md:765, mean or delta) | T2 | ~3.40 | **3.25** | 283 |
- `3.25` (results_FINAL.md:765, mean or delta) | T2 | ~3.40 | **3.25** | 283 |
- `283` (results_FINAL.md:765, mean or delta) | T2 | ~3.40 | **3.25** | 283 |
- `2.90` (results_FINAL.md:766, mean or delta) | T3 | ~2.90 | **3.01** | 185 |
- `3.01` (results_FINAL.md:766, mean or delta) | T3 | ~2.90 | **3.01** | 185 |
- `185` (results_FINAL.md:766, mean or delta) | T3 | ~2.90 | **3.01** | 185 |
- `2.70` (results_FINAL.md:767, mean or delta) | T4 | ~2.70 | **2.97** | 154 |
- `2.97` (results_FINAL.md:767, mean or delta) | T4 | ~2.70 | **2.97** | 154 |
- `154` (results_FINAL.md:767, mean or delta) | T4 | ~2.70 | **2.97** | 154 |
- `2.45` (results_FINAL.md:768, mean or delta) | T5 | 2.45 | **2.85** | 96 |
- `2.85` (results_FINAL.md:768, mean or delta) | T5 | 2.45 | **2.85** | 96 |
- `96` (results_FINAL.md:768, mean or delta) | T5 | 2.45 | **2.85** | 96 |
- `1.89` (results_FINAL.md:770, mean or delta) Delta T1->T5: OLD -1.89, NEW **-1.26** (unstripped), **-1.04** (stripped).
- `1.26` (results_FINAL.md:770, mean or delta) Delta T1->T5: OLD -1.89, NEW **-1.26** (unstripped), **-1.04** (stripped).
- `1.04` (results_FINAL.md:770, mean or delta) Delta T1->T5: OLD -1.89, NEW **-1.26** (unstripped), **-1.04** (stripped).
- `2.85` (results_FINAL.md:772, percentage) - **Stripped sensitivity:** Stripping removes meta that penalizes quality (triggers "Overdone"). T5 rises from 2.85 to 3.07. Trajectory is 17% shallower but still monotonically declining. See Stripped
- `3.07` (results_FINAL.md:772, percentage) - **Stripped sensitivity:** Stripping removes meta that penalizes quality (triggers "Overdone"). T5 rises from 2.85 to 3.07. Trajectory is 17% shallower but still monotonically declining. See Stripped
- `17` (results_FINAL.md:772, percentage) - **Stripped sensitivity:** Stripping removes meta that penalizes quality (triggers "Overdone"). T5 rises from 2.85 to 3.07. Trajectory is 17% shallower but still monotonically declining. See Stripped
- `720` (results_FINAL.md:773, bare number) - **Filter:** Mean quality per turn, T1 = all 720, T2-T5 = GENUINE-only. 6->2 recode.
- `6` (results_FINAL.md:773, bare number) - **Filter:** Mean quality per turn, T1 = all 720, T2-T5 = GENUINE-only. 6->2 recode.
- `2` (results_FINAL.md:773, bare number) - **Filter:** Mean quality per turn, T1 = all 720, T2-T5 = GENUINE-only. 6->2 recode.

### [results_FINAL.md] S10. Domain-Level Variation (GENUINE-only)

*- **Filter:** Mean quality per turn, T1 = all 720, T2-T5 = GENUINE-only. 6->2 recode.*

- `3.98` (results_FINAL.md:779, mean or delta) | analysis | 3.98 | 2.76 | -1.21 | 17 |
- `2.76` (results_FINAL.md:779, mean or delta) | analysis | 3.98 | 2.76 | -1.21 | 17 |
- `1.21` (results_FINAL.md:779, mean or delta) | analysis | 3.98 | 2.76 | -1.21 | 17 |
- `17` (results_FINAL.md:779, mean or delta) | analysis | 3.98 | 2.76 | -1.21 | 17 |
- `3.95` (results_FINAL.md:780, mean or delta) | code | 3.95 | 2.80 | -1.15 | 30 |
- `2.80` (results_FINAL.md:780, mean or delta) | code | 3.95 | 2.80 | -1.15 | 30 |
- `1.15` (results_FINAL.md:780, mean or delta) | code | 3.95 | 2.80 | -1.15 | 30 |
- `30` (results_FINAL.md:780, mean or delta) | code | 3.95 | 2.80 | -1.15 | 30 |
- `4.12` (results_FINAL.md:781, mean or delta) | creative | 4.12 | 2.89 | -1.22 | 19 |
- `2.89` (results_FINAL.md:781, mean or delta) | creative | 4.12 | 2.89 | -1.22 | 19 |
- `1.22` (results_FINAL.md:781, mean or delta) | creative | 4.12 | 2.89 | -1.22 | 19 |
- `19` (results_FINAL.md:781, mean or delta) | creative | 4.12 | 2.89 | -1.22 | 19 |
- `4.35` (results_FINAL.md:782, mean or delta) | data_logic | 4.35 | 3.00 | -1.35 | 17 |
- `3.00` (results_FINAL.md:782, mean or delta) | data_logic | 4.35 | 3.00 | -1.35 | 17 |
- `1.35` (results_FINAL.md:782, mean or delta) | data_logic | 4.35 | 3.00 | -1.35 | 17 |
- `17` (results_FINAL.md:782, mean or delta) | data_logic | 4.35 | 3.00 | -1.35 | 17 |
- `4.16` (results_FINAL.md:783, mean or delta) | writing | 4.16 | 2.85 | -1.31 | 13 |
- `2.85` (results_FINAL.md:783, mean or delta) | writing | 4.16 | 2.85 | -1.31 | 13 |
- `1.31` (results_FINAL.md:783, mean or delta) | writing | 4.16 | 2.85 | -1.31 | 13 |
- `13` (results_FINAL.md:783, mean or delta) | writing | 4.16 | 2.85 | -1.31 | 13 |
- `1.35` (results_FINAL.md:785, mean or delta) All domains degrade. Data_logic has steepest cliff (-1.35 unstripped, -1.01 stripped), code has shallowest (-1.15 unstripped, -1.05 stripped). All T5 n are small (13-30). See Stripped Sensitivity Anal
- `1.01` (results_FINAL.md:785, mean or delta) All domains degrade. Data_logic has steepest cliff (-1.35 unstripped, -1.01 stripped), code has shallowest (-1.15 unstripped, -1.05 stripped). All T5 n are small (13-30). See Stripped Sensitivity Anal
- `1.15` (results_FINAL.md:785, mean or delta) All domains degrade. Data_logic has steepest cliff (-1.35 unstripped, -1.01 stripped), code has shallowest (-1.15 unstripped, -1.05 stripped). All T5 n are small (13-30). See Stripped Sensitivity Anal
- `1.05` (results_FINAL.md:785, mean or delta) All domains degrade. Data_logic has steepest cliff (-1.35 unstripped, -1.01 stripped), code has shallowest (-1.15 unstripped, -1.05 stripped). All T5 n are small (13-30). See Stripped Sensitivity Anal
- `13` (results_FINAL.md:785, mean or delta) All domains degrade. Data_logic has steepest cliff (-1.35 unstripped, -1.01 stripped), code has shallowest (-1.15 unstripped, -1.05 stripped). All T5 n are small (13-30). See Stripped Sensitivity Anal
- `30` (results_FINAL.md:785, mean or delta) All domains degrade. Data_logic has steepest cliff (-1.35 unstripped, -1.01 stripped), code has shallowest (-1.15 unstripped, -1.05 stripped). All T5 n are small (13-30). See Stripped Sensitivity Anal
- `144` (results_FINAL.md:787, bare number) - **Filter:** GENUINE-only quality per domain. T1 = all 144 per domain. T5 = GENUINE at T5 only.

### [results_FINAL.md] S11. Level 6 "Overdone" Rate (GENUINE-only)

*- **Filter:** GENUINE-only quality per domain. T1 = all 144 per domain. T5 = GENUINE at T5 only.*

- `6` (results_FINAL.md:789, bare number) ## S11. Level 6 "Overdone" Rate (GENUINE-only)
- `3.1` (results_FINAL.md:793, percentage) | T1 | 3.1% (22/720) | **5.7%** (41/720) |
- `22` (results_FINAL.md:793, percentage) | T1 | 3.1% (22/720) | **5.7%** (41/720) |
- `720` (results_FINAL.md:793, percentage) | T1 | 3.1% (22/720) | **5.7%** (41/720) |
- `5.7` (results_FINAL.md:793, percentage) | T1 | 3.1% (22/720) | **5.7%** (41/720) |
- `41` (results_FINAL.md:793, percentage) | T1 | 3.1% (22/720) | **5.7%** (41/720) |
- `720` (results_FINAL.md:793, percentage) | T1 | 3.1% (22/720) | **5.7%** (41/720) |
- `14.9` (results_FINAL.md:794, percentage) | T2 | 14.9% | **33.9%** (96/283) |
- `33.9` (results_FINAL.md:794, percentage) | T2 | 14.9% | **33.9%** (96/283) |
- `96` (results_FINAL.md:794, percentage) | T2 | 14.9% | **33.9%** (96/283) |
- `283` (results_FINAL.md:794, percentage) | T2 | 14.9% | **33.9%** (96/283) |
- `42.2` (results_FINAL.md:795, percentage) | T3 | -- | **42.2%** (78/185) |
- `78` (results_FINAL.md:795, percentage) | T3 | -- | **42.2%** (78/185) |
- `185` (results_FINAL.md:795, percentage) | T3 | -- | **42.2%** (78/185) |
- `42.9` (results_FINAL.md:796, percentage) | T4 | -- | **42.9%** (66/154) |
- `66` (results_FINAL.md:796, percentage) | T4 | -- | **42.9%** (66/154) |
- `154` (results_FINAL.md:796, percentage) | T4 | -- | **42.9%** (66/154) |
- `47.9` (results_FINAL.md:797, percentage) | T5 | -- | **47.9%** (46/96) |
- `46` (results_FINAL.md:797, percentage) | T5 | -- | **47.9%** (46/96) |
- `96` (results_FINAL.md:797, percentage) | T5 | -- | **47.9%** (46/96) |
- `6` (results_FINAL.md:799, percentage) **Level 6 rate rises sharply in genuine revisions.** The old low rates were diluted by meta-responses (which never score 6). On stripped text, T5 rate drops from 47.9% to **34.4%** -- confirming meta-
- `6` (results_FINAL.md:799, percentage) **Level 6 rate rises sharply in genuine revisions.** The old low rates were diluted by meta-responses (which never score 6). On stripped text, T5 rate drops from 47.9% to **34.4%** -- confirming meta-
- `47.9` (results_FINAL.md:799, percentage) **Level 6 rate rises sharply in genuine revisions.** The old low rates were diluted by meta-responses (which never score 6). On stripped text, T5 rate drops from 47.9% to **34.4%** -- confirming meta-
- `34.4` (results_FINAL.md:799, percentage) **Level 6 rate rises sharply in genuine revisions.** The old low rates were diluted by meta-responses (which never score 6). On stripped text, T5 rate drops from 47.9% to **34.4%** -- confirming meta-
- `6` (results_FINAL.md:801, bare number) - **Filter:** Count of evaluator level == 6 (pre-recode) per turn, denominator = GENUINE responses at that turn.
- `3.1` (results_FINAL.md:802, percentage) - Note: T1 old value (3.1% = 22/720) vs new (5.7% = 41/720) discrepancy may be due to different T1 counting in the old analysis.
- `22` (results_FINAL.md:802, percentage) - Note: T1 old value (3.1% = 22/720) vs new (5.7% = 41/720) discrepancy may be due to different T1 counting in the old analysis.
- `720` (results_FINAL.md:802, percentage) - Note: T1 old value (3.1% = 22/720) vs new (5.7% = 41/720) discrepancy may be due to different T1 counting in the old analysis.
- `5.7` (results_FINAL.md:802, percentage) - Note: T1 old value (3.1% = 22/720) vs new (5.7% = 41/720) discrepancy may be due to different T1 counting in the old analysis.
- `41` (results_FINAL.md:802, percentage) - Note: T1 old value (3.1% = 22/720) vs new (5.7% = 41/720) discrepancy may be due to different T1 counting in the old analysis.
- `720` (results_FINAL.md:802, percentage) - Note: T1 old value (3.1% = 22/720) vs new (5.7% = 41/720) discrepancy may be due to different T1 counting in the old analysis.

### [results_FINAL.md] S12. Old Reversibility Sub-Analyses -- SUPERSEDED

*- **Filter:** Count of evaluator level == 6 (pre-recode) per turn, denominator = GENUINE responses at that turn.*

- `7` (results_FINAL.md:806, bare number) Replaced entirely by human annotation (Section 7) and stratified results (Section 9). Delete from paper.
- `9` (results_FINAL.md:806, bare number) Replaced entirely by human annotation (Section 7) and stratified results (Section 9). Delete from paper.

### [results_FINAL.md] S13. Momentum Connection -- NARRATIVE ONLY

*- **Filter:** Count of evaluator level == 6 (pre-recode) per turn, denominator = GENUINE responses at that turn.*

- `2` (results_FINAL.md:810, percentage) Study 2 numbers (1,728 trials, GPT-4o 98% momentum) are unchanged (different dataset). Framing adjustment: revision-despite-sufficiency is 39.2% (not 64.3%), so the "every turn is a momentum turn" cla
- `1,728` (results_FINAL.md:810, percentage) Study 2 numbers (1,728 trials, GPT-4o 98% momentum) are unchanged (different dataset). Framing adjustment: revision-despite-sufficiency is 39.2% (not 64.3%), so the "every turn is a momentum turn" cla
- `98` (results_FINAL.md:810, percentage) Study 2 numbers (1,728 trials, GPT-4o 98% momentum) are unchanged (different dataset). Framing adjustment: revision-despite-sufficiency is 39.2% (not 64.3%), so the "every turn is a momentum turn" cla
- `39.2` (results_FINAL.md:810, percentage) Study 2 numbers (1,728 trials, GPT-4o 98% momentum) are unchanged (different dataset). Framing adjustment: revision-despite-sufficiency is 39.2% (not 64.3%), so the "every turn is a momentum turn" cla
- `64.3` (results_FINAL.md:810, percentage) Study 2 numbers (1,728 trials, GPT-4o 98% momentum) are unchanged (different dataset). Framing adjustment: revision-despite-sufficiency is 39.2% (not 64.3%), so the "every turn is a momentum turn" cla

### [results_FINAL.md] S14. Targeted Feedback Per-Model (GENUINE-only)

*- **Filter:** Count of evaluator level == 6 (pre-recode) per turn, denominator = GENUINE responses at that turn.*

- `4` (results_FINAL.md:816, mean or delta) | claude-sonnet-4 | 51 | +0.51 | 0.004 | Yes |
- `51` (results_FINAL.md:816, mean or delta) | claude-sonnet-4 | 51 | +0.51 | 0.004 | Yes |
- `0.51` (results_FINAL.md:816, mean or delta) | claude-sonnet-4 | 51 | +0.51 | 0.004 | Yes |
- `0.004` (results_FINAL.md:816, mean or delta) | claude-sonnet-4 | 51 | +0.51 | 0.004 | Yes |
- `19` (results_FINAL.md:817, mean or delta) | deepseek-v4 | 19 | +1.58 | 0.005 | Yes |
- `1.58` (results_FINAL.md:817, mean or delta) | deepseek-v4 | 19 | +1.58 | 0.005 | Yes |
- `0.005` (results_FINAL.md:817, mean or delta) | deepseek-v4 | 19 | +1.58 | 0.005 | Yes |
- `2.5` (results_FINAL.md:818, mean or delta) | gemini-2.5-flash | 3 | +1.00 | -- (n<5) | Underpowered |
- `3` (results_FINAL.md:818, mean or delta) | gemini-2.5-flash | 3 | +1.00 | -- (n<5) | Underpowered |
- `1.00` (results_FINAL.md:818, mean or delta) | gemini-2.5-flash | 3 | +1.00 | -- (n<5) | Underpowered |
- `5` (results_FINAL.md:818, mean or delta) | gemini-2.5-flash | 3 | +1.00 | -- (n<5) | Underpowered |
- `12` (results_FINAL.md:819, mean or delta) | gpt-4o | 12 | -0.17 | 0.750 | No |
- `0.17` (results_FINAL.md:819, mean or delta) | gpt-4o | 12 | -0.17 | 0.750 | No |
- `0.750` (results_FINAL.md:819, mean or delta) | gpt-4o | 12 | -0.17 | 0.750 | No |
- `3.3` (results_FINAL.md:820, mean or delta) | llama-3.3-70b | 71 | -0.17 | 0.027 | Marginal (wrong direction) |
- `71` (results_FINAL.md:820, mean or delta) | llama-3.3-70b | 71 | -0.17 | 0.027 | Marginal (wrong direction) |
- `0.17` (results_FINAL.md:820, mean or delta) | llama-3.3-70b | 71 | -0.17 | 0.027 | Marginal (wrong direction) |
- `0.027` (results_FINAL.md:820, mean or delta) | llama-3.3-70b | 71 | -0.17 | 0.027 | Marginal (wrong direction) |
- `3` (results_FINAL.md:821, mean or delta) | qwen-3-235b | 21 | +0.00 | 1.000 | No |
- `21` (results_FINAL.md:821, mean or delta) | qwen-3-235b | 21 | +0.00 | 1.000 | No |
- `0.00` (results_FINAL.md:821, mean or delta) | qwen-3-235b | 21 | +0.00 | 1.000 | No |
- `1.000` (results_FINAL.md:821, mean or delta) | qwen-3-235b | 21 | +0.00 | 1.000 | No |
- `0.31` (results_FINAL.md:823, mean or delta) **SUPERSEDED by stripped analysis.** The unstripped per-model story ("only Claude and DeepSeek benefit") was an artifact of meta-commentary inflating the generic baseline for models with verbose meta-
- `1.62` (results_FINAL.md:823, mean or delta) **SUPERSEDED by stripped analysis.** The unstripped per-model story ("only Claude and DeepSeek benefit") was an artifact of meta-commentary inflating the generic baseline for models with verbose meta-
- `5` (results_FINAL.md:825, bare number) - **Filter:** Same as Section 5 (next-turn GENUINE filter, 6->2 recode). Grouped by model.
- `6` (results_FINAL.md:825, bare number) - **Filter:** Same as Section 5 (next-turn GENUINE filter, 6->2 recode). Grouped by model.
- `2` (results_FINAL.md:825, bare number) - **Filter:** Same as Section 5 (next-turn GENUINE filter, 6->2 recode). Grouped by model.
- `96` (results_FINAL.md:826, percentage) - **Supersedes:** Both the old "96-99%" claim AND the intermediate "only 2/6 benefit" finding.
- `99` (results_FINAL.md:826, percentage) - **Supersedes:** Both the old "96-99%" claim AND the intermediate "only 2/6 benefit" finding.
- `2` (results_FINAL.md:826, percentage) - **Supersedes:** Both the old "96-99%" claim AND the intermediate "only 2/6 benefit" finding.
- `6` (results_FINAL.md:826, percentage) - **Supersedes:** Both the old "96-99%" claim AND the intermediate "only 2/6 benefit" finding.

### [results_FINAL.md] S15. Sophie v2 Reliability -- RESOLVED

*- **Filter:** Same as Section 5 (next-turn GENUINE filter, 6->2 recode). Grouped by model.*

- `11` (results_FINAL.md:830, count or denominator) Already fixed in Section 11. Sophie v2 has 64/64 valid ratings. Three-rater QW kappas: 0.406, 0.578, 0.603. Alpha = 0.529.
- `64` (results_FINAL.md:830, count or denominator) Already fixed in Section 11. Sophie v2 has 64/64 valid ratings. Three-rater QW kappas: 0.406, 0.578, 0.603. Alpha = 0.529.
- `64` (results_FINAL.md:830, count or denominator) Already fixed in Section 11. Sophie v2 has 64/64 valid ratings. Three-rater QW kappas: 0.406, 0.578, 0.603. Alpha = 0.529.
- `0.406` (results_FINAL.md:830, count or denominator) Already fixed in Section 11. Sophie v2 has 64/64 valid ratings. Three-rater QW kappas: 0.406, 0.578, 0.603. Alpha = 0.529.
- `0.578` (results_FINAL.md:830, count or denominator) Already fixed in Section 11. Sophie v2 has 64/64 valid ratings. Three-rater QW kappas: 0.406, 0.578, 0.603. Alpha = 0.529.
- `0.603` (results_FINAL.md:830, count or denominator) Already fixed in Section 11. Sophie v2 has 64/64 valid ratings. Three-rater QW kappas: 0.406, 0.578, 0.603. Alpha = 0.529.
- `0.529` (results_FINAL.md:830, count or denominator) Already fixed in Section 11. Sophie v2 has 64/64 valid ratings. Three-rater QW kappas: 0.406, 0.578, 0.603. Alpha = 0.529.
- `8` (results_FINAL.md:834, bare number) # STRIPPED SENSITIVITY ANALYSIS (Audit Item 8)
- `3,600` (results_FINAL.md:836, bare number) All 3,600 outputs (720 trials x 5 turns) were regex-stripped of meta-commentary preambles/postambles
- `720` (results_FINAL.md:836, bare number) All 3,600 outputs (720 trials x 5 turns) were regex-stripped of meta-commentary preambles/postambles
- `5` (results_FINAL.md:836, bare number) All 3,600 outputs (720 trials x 5 turns) were regex-stripped of meta-commentary preambles/postambles
- `1,200` (results_FINAL.md:837, bare number) (same validated patterns as the reversibility pairs) and the 1,200 that changed were rescored by
- `4` (results_FINAL.md:838, bare number) Claude Sonnet 4 at temperature 0 using the identical EVAL_PROMPT. Scores 6->2 recoded.
- `0` (results_FINAL.md:838, bare number) Claude Sonnet 4 at temperature 0 using the identical EVAL_PROMPT. Scores 6->2 recoded.
- `6` (results_FINAL.md:838, bare number) Claude Sonnet 4 at temperature 0 using the identical EVAL_PROMPT. Scores 6->2 recoded.
- `2` (results_FINAL.md:838, bare number) Claude Sonnet 4 at temperature 0 using the identical EVAL_PROMPT. Scores 6->2 recoded.
- `6` (results_FINAL.md:840, bare number) **Key finding: meta-commentary PENALIZES quality scores** (triggers "Overdone" = level 6), so

### [results_FINAL.md] Stripping Scope

*- **Filter:** Same as Section 5 (next-turn GENUINE filter, 6->2 recode). Grouped by model.*

- `69` (results_FINAL.md:849, percentage) | T1 | 69/720 | 9.6% |
- `720` (results_FINAL.md:849, percentage) | T1 | 69/720 | 9.6% |
- `9.6` (results_FINAL.md:849, percentage) | T1 | 69/720 | 9.6% |
- `361` (results_FINAL.md:850, percentage) | T2 | 361/720 | 50.1% |
- `720` (results_FINAL.md:850, percentage) | T2 | 361/720 | 50.1% |
- `50.1` (results_FINAL.md:850, percentage) | T2 | 361/720 | 50.1% |
- `282` (results_FINAL.md:851, percentage) | T3 | 282/720 | 39.2% |
- `720` (results_FINAL.md:851, percentage) | T3 | 282/720 | 39.2% |
- `39.2` (results_FINAL.md:851, percentage) | T3 | 282/720 | 39.2% |
- `278` (results_FINAL.md:852, percentage) | T4 | 278/720 | 38.6% |
- `720` (results_FINAL.md:852, percentage) | T4 | 278/720 | 38.6% |
- `38.6` (results_FINAL.md:852, percentage) | T4 | 278/720 | 38.6% |
- `210` (results_FINAL.md:853, percentage) | T5 | 210/720 | 29.2% |
- `720` (results_FINAL.md:853, percentage) | T5 | 210/720 | 29.2% |
- `29.2` (results_FINAL.md:853, percentage) | T5 | 210/720 | 29.2% |
- `1,200` (results_FINAL.md:854, percentage) | **Total** | **1,200/3,600** | **33.3%** |
- `3,600` (results_FINAL.md:854, percentage) | **Total** | **1,200/3,600** | **33.3%** |
- `33.3` (results_FINAL.md:854, percentage) | **Total** | **1,200/3,600** | **33.3%** |
- `3,600` (results_FINAL.md:856, bare number) Source: `data/study3/raw_responses/stripped_rescore_full.jsonl` (3,600 records, one per trial x turn)

### [results_FINAL.md] Metric-by-Metric Comparison -- M1. Revision-Despite-Sufficiency

*- **Filter:** Same as Section 5 (next-turn GENUINE filter, 6->2 recode). Grouped by model.*

- `4` (results_FINAL.md:864, bare number) | Sufficient turns (level >= 4) | 938 | 1,038 | +100 |
- `938` (results_FINAL.md:864, bare number) | Sufficient turns (level >= 4) | 938 | 1,038 | +100 |
- `1,038` (results_FINAL.md:864, bare number) | Sufficient turns (level >= 4) | 938 | 1,038 | +100 |
- `100` (results_FINAL.md:864, bare number) | Sufficient turns (level >= 4) | 938 | 1,038 | +100 |
- `368` (results_FINAL.md:865, bare number) | Revised despite sufficient | 368 | 411 | +43 |
- `411` (results_FINAL.md:865, bare number) | Revised despite sufficient | 368 | 411 | +43 |
- `43` (results_FINAL.md:865, bare number) | Revised despite sufficient | 368 | 411 | +43 |
- `39.2` (results_FINAL.md:866, percentage) | **Rate** | **39.2%** | **39.6%** | **+0.4pp** |
- `39.6` (results_FINAL.md:866, percentage) | **Rate** | **39.2%** | **39.6%** | **+0.4pp** |
- `0` (results_FINAL.md:866, percentage) | **Rate** | **39.2%** | **39.6%** | **+0.4pp** |
- `4` (results_FINAL.md:868, bare number) **Verdict: HOLDS.** Denominator grows because stripping removes meta that was pushing some scores below 4.

### [results_FINAL.md] Metric-by-Metric Comparison -- M2. Targeted Feedback

*- **Filter:** Same as Section 5 (next-turn GENUINE filter, 6->2 recode). Grouped by model.*

- `4.68` (results_FINAL.md:875, mean or delta) | Both unstripped | 4.68 | 4.43 | **+0.25** | 3.75e-03 | 177 |
- `4.43` (results_FINAL.md:875, mean or delta) | Both unstripped | 4.68 | 4.43 | **+0.25** | 3.75e-03 | 177 |
- `0.25` (results_FINAL.md:875, mean or delta) | Both unstripped | 4.68 | 4.43 | **+0.25** | 3.75e-03 | 177 |
- `3` (results_FINAL.md:875, mean or delta) | Both unstripped | 4.68 | 4.43 | **+0.25** | 3.75e-03 | 177 |
- `03` (results_FINAL.md:875, mean or delta) | Both unstripped | 4.68 | 4.43 | **+0.25** | 3.75e-03 | 177 |
- `177` (results_FINAL.md:875, mean or delta) | Both unstripped | 4.68 | 4.43 | **+0.25** | 3.75e-03 | 177 |
- `4.68` (results_FINAL.md:876, mean or delta) | Both stripped | 4.68 | 3.53 | **+1.16** | 5.74e-19 | 177 |
- `3.53` (results_FINAL.md:876, mean or delta) | Both stripped | 4.68 | 3.53 | **+1.16** | 5.74e-19 | 177 |
- `1.16` (results_FINAL.md:876, mean or delta) | Both stripped | 4.68 | 3.53 | **+1.16** | 5.74e-19 | 177 |
- `5` (results_FINAL.md:876, mean or delta) | Both stripped | 4.68 | 3.53 | **+1.16** | 5.74e-19 | 177 |
- `19` (results_FINAL.md:876, mean or delta) | Both stripped | 4.68 | 3.53 | **+1.16** | 5.74e-19 | 177 |
- `177` (results_FINAL.md:876, mean or delta) | Both stripped | 4.68 | 3.53 | **+1.16** | 5.74e-19 | 177 |
- `9` (results_FINAL.md:878, percentage) Targeted revisions have almost no meta-commentary (9/177 = 5% had any to strip; targeted mean barely
- `177` (results_FINAL.md:878, percentage) Targeted revisions have almost no meta-commentary (9/177 = 5% had any to strip; targeted mean barely
- `5` (results_FINAL.md:878, percentage) Targeted revisions have almost no meta-commentary (9/177 = 5% had any to strip; targeted mean barely
- `4.68` (results_FINAL.md:879, mean or delta) changed: 4.68 -> 4.63). Generic revisions have substantial meta-commentary that was INFLATING their
- `4.63` (results_FINAL.md:879, mean or delta) changed: 4.68 -> 4.63). Generic revisions have substantial meta-commentary that was INFLATING their
- `4.43` (results_FINAL.md:880, mean or delta) scores (4.43 -> 3.53 stripped). The real advantage of targeted feedback is +1.16 levels, not +0.25.
- `3.53` (results_FINAL.md:880, mean or delta) scores (4.43 -> 3.53 stripped). The real advantage of targeted feedback is +1.16 levels, not +0.25.
- `1.16` (results_FINAL.md:880, mean or delta) scores (4.43 -> 3.53 stripped). The real advantage of targeted feedback is +1.16 levels, not +0.25.
- `0.25` (results_FINAL.md:880, mean or delta) scores (4.43 -> 3.53 stripped). The real advantage of targeted feedback is +1.16 levels, not +0.25.
- `4` (results_FINAL.md:886, mean or delta) | claude-sonnet-4 | 51 | +0.31 | 0.012 |
- `51` (results_FINAL.md:886, mean or delta) | claude-sonnet-4 | 51 | +0.31 | 0.012 |
- `0.31` (results_FINAL.md:886, mean or delta) | claude-sonnet-4 | 51 | +0.31 | 0.012 |
- `0.012` (results_FINAL.md:886, mean or delta) | claude-sonnet-4 | 51 | +0.31 | 0.012 |
- `19` (results_FINAL.md:887, mean or delta) | deepseek-v4 | 19 | +1.05 | 0.012 |
- `1.05` (results_FINAL.md:887, mean or delta) | deepseek-v4 | 19 | +1.05 | 0.012 |
- `0.012` (results_FINAL.md:887, mean or delta) | deepseek-v4 | 19 | +1.05 | 0.012 |
- `2.5` (results_FINAL.md:888, mean or delta) | gemini-2.5-flash | 3 | +2.33 | -- (n<5) |
- `3` (results_FINAL.md:888, mean or delta) | gemini-2.5-flash | 3 | +2.33 | -- (n<5) |
- `2.33` (results_FINAL.md:888, mean or delta) | gemini-2.5-flash | 3 | +2.33 | -- (n<5) |
- `5` (results_FINAL.md:888, mean or delta) | gemini-2.5-flash | 3 | +2.33 | -- (n<5) |
- `12` (results_FINAL.md:889, mean or delta) | gpt-4o | 12 | +1.33 | 0.008 |
- `1.33` (results_FINAL.md:889, mean or delta) | gpt-4o | 12 | +1.33 | 0.008 |
- `0.008` (results_FINAL.md:889, mean or delta) | gpt-4o | 12 | +1.33 | 0.008 |
- `3.3` (results_FINAL.md:890, mean or delta) | llama-3.3-70b | 71 | +1.62 | 9.2e-12 |
- `71` (results_FINAL.md:890, mean or delta) | llama-3.3-70b | 71 | +1.62 | 9.2e-12 |
- `1.62` (results_FINAL.md:890, mean or delta) | llama-3.3-70b | 71 | +1.62 | 9.2e-12 |
- `9` (results_FINAL.md:890, mean or delta) | llama-3.3-70b | 71 | +1.62 | 9.2e-12 |
- `12` (results_FINAL.md:890, mean or delta) | llama-3.3-70b | 71 | +1.62 | 9.2e-12 |
- `3` (results_FINAL.md:891, mean or delta) | qwen-3-235b | 21 | +1.48 | 4.5e-04 |
- `21` (results_FINAL.md:891, mean or delta) | qwen-3-235b | 21 | +1.48 | 4.5e-04 |
- `1.48` (results_FINAL.md:891, mean or delta) | qwen-3-235b | 21 | +1.48 | 4.5e-04 |
- `4` (results_FINAL.md:891, mean or delta) | qwen-3-235b | 21 | +1.48 | 4.5e-04 |
- `04` (results_FINAL.md:891, mean or delta) | qwen-3-235b | 21 | +1.48 | 4.5e-04 |

### [results_FINAL.md] Metric-by-Metric Comparison -- M3. LOCF Analysis

*- **Filter:** Same as Section 5 (next-turn GENUINE filter, 6->2 recode). Grouped by model.*

- `4.11` (results_FINAL.md:901, mean or delta) | LOCF T1 | 4.11 | 4.11 | 0 |
- `4.11` (results_FINAL.md:901, mean or delta) | LOCF T1 | 4.11 | 4.11 | 0 |
- `0` (results_FINAL.md:901, mean or delta) | LOCF T1 | 4.11 | 4.11 | 0 |
- `3.60` (results_FINAL.md:902, mean or delta) | LOCF T5 | 3.60 | 3.81 | +0.21 |
- `3.81` (results_FINAL.md:902, mean or delta) | LOCF T5 | 3.60 | 3.81 | +0.21 |
- `0.21` (results_FINAL.md:902, mean or delta) | LOCF T5 | 3.60 | 3.81 | +0.21 |
- `0.51` (results_FINAL.md:903, percentage) | **Delta** | **-0.51** | **-0.30** | **41% smaller** |
- `0.30` (results_FINAL.md:903, percentage) | **Delta** | **-0.51** | **-0.30** | **41% smaller** |
- `41` (results_FINAL.md:903, percentage) | **Delta** | **-0.51** | **-0.30** | **41% smaller** |
- `1` (results_FINAL.md:904, mean or delta) | p-value | 1.0e-32 | 3.8e-18 | Still significant |
- `32` (results_FINAL.md:904, mean or delta) | p-value | 1.0e-32 | 3.8e-18 | Still significant |
- `3` (results_FINAL.md:904, mean or delta) | p-value | 1.0e-32 | 3.8e-18 | Still significant |
- `18` (results_FINAL.md:904, mean or delta) | p-value | 1.0e-32 | 3.8e-18 | Still significant |
- `0.30` (results_FINAL.md:907, count or denominator) LOCF degradation is -0.30 levels, not -0.51. Highly significant either way (n=720).
- `0.51` (results_FINAL.md:907, count or denominator) LOCF degradation is -0.30 levels, not -0.51. Highly significant either way (n=720).
- `720` (results_FINAL.md:907, count or denominator) LOCF degradation is -0.30 levels, not -0.51. Highly significant either way (n=720).

### [results_FINAL.md] Metric-by-Metric Comparison -- M4. Pooled Revision-Only Trajectory (GENUINE-only)

*- **Filter:** Same as Section 5 (next-turn GENUINE filter, 6->2 recode). Grouped by model.*

- `4.11` (results_FINAL.md:913, mean or delta) | T1 | 4.11 | 4.11 | 0 | 720 |
- `4.11` (results_FINAL.md:913, mean or delta) | T1 | 4.11 | 4.11 | 0 | 720 |
- `0` (results_FINAL.md:913, mean or delta) | T1 | 4.11 | 4.11 | 0 | 720 |
- `720` (results_FINAL.md:913, mean or delta) | T1 | 4.11 | 4.11 | 0 | 720 |
- `3.25` (results_FINAL.md:914, mean or delta) | T2 | 3.25 | 3.66 | +0.41 | 283 |
- `3.66` (results_FINAL.md:914, mean or delta) | T2 | 3.25 | 3.66 | +0.41 | 283 |
- `0.41` (results_FINAL.md:914, mean or delta) | T2 | 3.25 | 3.66 | +0.41 | 283 |
- `283` (results_FINAL.md:914, mean or delta) | T2 | 3.25 | 3.66 | +0.41 | 283 |
- `3.01` (results_FINAL.md:915, mean or delta) | T3 | 3.01 | 3.40 | +0.39 | 185 |
- `3.40` (results_FINAL.md:915, mean or delta) | T3 | 3.01 | 3.40 | +0.39 | 185 |
- `0.39` (results_FINAL.md:915, mean or delta) | T3 | 3.01 | 3.40 | +0.39 | 185 |
- `185` (results_FINAL.md:915, mean or delta) | T3 | 3.01 | 3.40 | +0.39 | 185 |
- `2.97` (results_FINAL.md:916, mean or delta) | T4 | 2.97 | 3.34 | +0.37 | 154 |
- `3.34` (results_FINAL.md:916, mean or delta) | T4 | 2.97 | 3.34 | +0.37 | 154 |
- `0.37` (results_FINAL.md:916, mean or delta) | T4 | 2.97 | 3.34 | +0.37 | 154 |
- `154` (results_FINAL.md:916, mean or delta) | T4 | 2.97 | 3.34 | +0.37 | 154 |
- `2.85` (results_FINAL.md:917, mean or delta) | T5 | 2.85 | 3.07 | +0.22 | 96 |
- `3.07` (results_FINAL.md:917, mean or delta) | T5 | 2.85 | 3.07 | +0.22 | 96 |
- `0.22` (results_FINAL.md:917, mean or delta) | T5 | 2.85 | 3.07 | +0.22 | 96 |
- `96` (results_FINAL.md:917, mean or delta) | T5 | 2.85 | 3.07 | +0.22 | 96 |
- `1.26` (results_FINAL.md:918, percentage) | **Delta T1->T5** | **-1.26** | **-1.04** | **17% smaller** | |
- `1.04` (results_FINAL.md:918, percentage) | **Delta T1->T5** | **-1.26** | **-1.04** | **17% smaller** | |
- `17` (results_FINAL.md:918, percentage) | **Delta T1->T5** | **-1.26** | **-1.04** | **17% smaller** | |
- `3.07` (results_FINAL.md:920, mean or delta) **Verdict: HOLDS.** Quality still degrades monotonically. Stripped T5 (3.07) is still below
- `4.0` (results_FINAL.md:921, percentage) Sufficient (4.0). But the decline is 17% shallower than unstripped.
- `17` (results_FINAL.md:921, percentage) Sufficient (4.0). But the decline is 17% shallower than unstripped.

### [results_FINAL.md] Metric-by-Metric Comparison -- M5. Domain-Level Variation (GENUINE-only)

*- **Filter:** Same as Section 5 (next-turn GENUINE filter, 6->2 recode). Grouped by model.*

- `1.21` (results_FINAL.md:927, mean or delta) | analysis | -1.21 | -1.16 | +0.05 | 17 |
- `1.16` (results_FINAL.md:927, mean or delta) | analysis | -1.21 | -1.16 | +0.05 | 17 |
- `0.05` (results_FINAL.md:927, mean or delta) | analysis | -1.21 | -1.16 | +0.05 | 17 |
- `17` (results_FINAL.md:927, mean or delta) | analysis | -1.21 | -1.16 | +0.05 | 17 |
- `1.15` (results_FINAL.md:928, mean or delta) | code | -1.15 | -1.05 | +0.10 | 30 |
- `1.05` (results_FINAL.md:928, mean or delta) | code | -1.15 | -1.05 | +0.10 | 30 |
- `0.10` (results_FINAL.md:928, mean or delta) | code | -1.15 | -1.05 | +0.10 | 30 |
- `30` (results_FINAL.md:928, mean or delta) | code | -1.15 | -1.05 | +0.10 | 30 |
- `1.22` (results_FINAL.md:929, mean or delta) | creative | -1.22 | -0.82 | +0.40 | 19 |
- `0.82` (results_FINAL.md:929, mean or delta) | creative | -1.22 | -0.82 | +0.40 | 19 |
- `0.40` (results_FINAL.md:929, mean or delta) | creative | -1.22 | -0.82 | +0.40 | 19 |
- `19` (results_FINAL.md:929, mean or delta) | creative | -1.22 | -0.82 | +0.40 | 19 |
- `1.35` (results_FINAL.md:930, mean or delta) | data_logic | -1.35 | -1.01 | +0.34 | 17 |
- `1.01` (results_FINAL.md:930, mean or delta) | data_logic | -1.35 | -1.01 | +0.34 | 17 |
- `0.34` (results_FINAL.md:930, mean or delta) | data_logic | -1.35 | -1.01 | +0.34 | 17 |
- `17` (results_FINAL.md:930, mean or delta) | data_logic | -1.35 | -1.01 | +0.34 | 17 |
- `1.31` (results_FINAL.md:931, mean or delta) | writing | -1.31 | -1.06 | +0.25 | 13 |
- `1.06` (results_FINAL.md:931, mean or delta) | writing | -1.31 | -1.06 | +0.25 | 13 |
- `0.25` (results_FINAL.md:931, mean or delta) | writing | -1.31 | -1.06 | +0.25 | 13 |
- `13` (results_FINAL.md:931, mean or delta) | writing | -1.31 | -1.06 | +0.25 | 13 |

### [results_FINAL.md] Metric-by-Metric Comparison -- M6. Level-6 "Overdone" Rate (GENUINE-only, pre-recode)

*- **Filter:** Same as Section 5 (next-turn GENUINE filter, 6->2 recode). Grouped by model.*

- `6` (results_FINAL.md:936, bare number) ### M6. Level-6 "Overdone" Rate (GENUINE-only, pre-recode)
- `5.7` (results_FINAL.md:940, percentage) | T1 | 5.7% (41/720) | 5.6% (40/720) | -0.1pp |
- `41` (results_FINAL.md:940, percentage) | T1 | 5.7% (41/720) | 5.6% (40/720) | -0.1pp |
- `720` (results_FINAL.md:940, percentage) | T1 | 5.7% (41/720) | 5.6% (40/720) | -0.1pp |
- `5.6` (results_FINAL.md:940, percentage) | T1 | 5.7% (41/720) | 5.6% (40/720) | -0.1pp |
- `40` (results_FINAL.md:940, percentage) | T1 | 5.7% (41/720) | 5.6% (40/720) | -0.1pp |
- `720` (results_FINAL.md:940, percentage) | T1 | 5.7% (41/720) | 5.6% (40/720) | -0.1pp |
- `0` (results_FINAL.md:940, percentage) | T1 | 5.7% (41/720) | 5.6% (40/720) | -0.1pp |
- `33.9` (results_FINAL.md:941, percentage) | T2 | 33.9% (96/283) | 18.0% (51/283) | **-15.9pp** |
- `96` (results_FINAL.md:941, percentage) | T2 | 33.9% (96/283) | 18.0% (51/283) | **-15.9pp** |
- `283` (results_FINAL.md:941, percentage) | T2 | 33.9% (96/283) | 18.0% (51/283) | **-15.9pp** |
- `18.0` (results_FINAL.md:941, percentage) | T2 | 33.9% (96/283) | 18.0% (51/283) | **-15.9pp** |
- `51` (results_FINAL.md:941, percentage) | T2 | 33.9% (96/283) | 18.0% (51/283) | **-15.9pp** |
- `283` (results_FINAL.md:941, percentage) | T2 | 33.9% (96/283) | 18.0% (51/283) | **-15.9pp** |
- `15` (results_FINAL.md:941, percentage) | T2 | 33.9% (96/283) | 18.0% (51/283) | **-15.9pp** |
- `42.2` (results_FINAL.md:942, percentage) | T3 | 42.2% (78/185) | 28.6% (53/185) | **-13.5pp** |
- `78` (results_FINAL.md:942, percentage) | T3 | 42.2% (78/185) | 28.6% (53/185) | **-13.5pp** |
- `185` (results_FINAL.md:942, percentage) | T3 | 42.2% (78/185) | 28.6% (53/185) | **-13.5pp** |
- `28.6` (results_FINAL.md:942, percentage) | T3 | 42.2% (78/185) | 28.6% (53/185) | **-13.5pp** |
- `53` (results_FINAL.md:942, percentage) | T3 | 42.2% (78/185) | 28.6% (53/185) | **-13.5pp** |
- `185` (results_FINAL.md:942, percentage) | T3 | 42.2% (78/185) | 28.6% (53/185) | **-13.5pp** |
- `13` (results_FINAL.md:942, percentage) | T3 | 42.2% (78/185) | 28.6% (53/185) | **-13.5pp** |
- `42.9` (results_FINAL.md:943, percentage) | T4 | 42.9% (66/154) | 27.9% (43/154) | **-15.0pp** |
- `66` (results_FINAL.md:943, percentage) | T4 | 42.9% (66/154) | 27.9% (43/154) | **-15.0pp** |
- `154` (results_FINAL.md:943, percentage) | T4 | 42.9% (66/154) | 27.9% (43/154) | **-15.0pp** |
- `27.9` (results_FINAL.md:943, percentage) | T4 | 42.9% (66/154) | 27.9% (43/154) | **-15.0pp** |
- `43` (results_FINAL.md:943, percentage) | T4 | 42.9% (66/154) | 27.9% (43/154) | **-15.0pp** |
- `154` (results_FINAL.md:943, percentage) | T4 | 42.9% (66/154) | 27.9% (43/154) | **-15.0pp** |
- `15` (results_FINAL.md:943, percentage) | T4 | 42.9% (66/154) | 27.9% (43/154) | **-15.0pp** |
- `47.9` (results_FINAL.md:944, percentage) | T5 | 47.9% (46/96) | 34.4% (33/96) | **-13.5pp** |
- `46` (results_FINAL.md:944, percentage) | T5 | 47.9% (46/96) | 34.4% (33/96) | **-13.5pp** |
- `96` (results_FINAL.md:944, percentage) | T5 | 47.9% (46/96) | 34.4% (33/96) | **-13.5pp** |
- `34.4` (results_FINAL.md:944, percentage) | T5 | 47.9% (46/96) | 34.4% (33/96) | **-13.5pp** |
- `33` (results_FINAL.md:944, percentage) | T5 | 47.9% (46/96) | 34.4% (33/96) | **-13.5pp** |
- `96` (results_FINAL.md:944, percentage) | T5 | 47.9% (46/96) | 34.4% (33/96) | **-13.5pp** |
- `13` (results_FINAL.md:944, percentage) | T5 | 47.9% (46/96) | 34.4% (33/96) | **-13.5pp** |
- `6` (results_FINAL.md:946, bare number) **Verdict: CONFIRMS meta preambles trigger "Overdone."** Level-6 rates drop 13-16pp after stripping.
- `13` (results_FINAL.md:946, bare number) **Verdict: CONFIRMS meta preambles trigger "Overdone."** Level-6 rates drop 13-16pp after stripping.
- `34.4` (results_FINAL.md:948, percentage) "unrequested complexity." Even stripped, 34.4% of genuine T5 revisions are still Overdone -- this is

### [results_FINAL.md] Metric-by-Metric Comparison -- Balanced Panel Cliff (reference, already in Section 2)

*- **Filter:** Same as Section 5 (next-turn GENUINE filter, 6->2 recode). Grouped by model.*

- `2` (results_FINAL.md:951, bare number) ### Balanced Panel Cliff (reference, already in Section 2)
- `3.66` (results_FINAL.md:955, mean or delta) | T1 | 3.66 | 3.66 | 0 |
- `3.66` (results_FINAL.md:955, mean or delta) | T1 | 3.66 | 3.66 | 0 |
- `0` (results_FINAL.md:955, mean or delta) | T1 | 3.66 | 3.66 | 0 |
- `2.72` (results_FINAL.md:956, mean or delta) | T5 | 2.72 | 2.92 | +0.20 |
- `2.92` (results_FINAL.md:956, mean or delta) | T5 | 2.72 | 2.92 | +0.20 |
- `0.20` (results_FINAL.md:956, mean or delta) | T5 | 2.72 | 2.92 | +0.20 |
- `0.94` (results_FINAL.md:957, percentage) | **Delta** | **-0.94** | **-0.74** | **21% smaller** |
- `0.74` (results_FINAL.md:957, percentage) | **Delta** | **-0.94** | **-0.74** | **21% smaller** |
- `21` (results_FINAL.md:957, percentage) | **Delta** | **-0.94** | **-0.74** | **21% smaller** |
- `50` (results_FINAL.md:959, percentage) Consistent with the earlier 50-pair rescore (19-21% inflation range).
- `19` (results_FINAL.md:959, percentage) Consistent with the earlier 50-pair rescore (19-21% inflation range).
- `21` (results_FINAL.md:959, percentage) Consistent with the earlier 50-pair rescore (19-21% inflation range).

### [results_FINAL.md] Summary: What Moves, What Holds

*- **Filter:** Same as Section 5 (next-turn GENUINE filter, 6->2 recode). Grouped by model.*

- `1` (results_FINAL.md:965, percentage) | 1 | Rev-despite-suff | 39.2% | 39.6% | No | Same |
- `39.2` (results_FINAL.md:965, percentage) | 1 | Rev-despite-suff | 39.2% | 39.6% | No | Same |
- `39.6` (results_FINAL.md:965, percentage) | 1 | Rev-despite-suff | 39.2% | 39.6% | No | Same |
- `2` (results_FINAL.md:966, mean or delta) | 2 | Targeted feedback | +0.25 | +1.16 | **YES** | Same, much stronger |
- `0.25` (results_FINAL.md:966, mean or delta) | 2 | Targeted feedback | +0.25 | +1.16 | **YES** | Same, much stronger |
- `1.16` (results_FINAL.md:966, mean or delta) | 2 | Targeted feedback | +0.25 | +1.16 | **YES** | Same, much stronger |
- `2` (results_FINAL.md:967, count or denominator) | 2b | Targeted per-model | 2/6 benefit | **All benefit** | **YES** | Reverses |
- `6` (results_FINAL.md:967, count or denominator) | 2b | Targeted per-model | 2/6 benefit | **All benefit** | **YES** | Reverses |
- `3` (results_FINAL.md:968, mean or delta) | 3 | LOCF delta | -0.51 | -0.30 | Moderate | Same, attenuated |
- `0.51` (results_FINAL.md:968, mean or delta) | 3 | LOCF delta | -0.51 | -0.30 | Moderate | Same, attenuated |
- `0.30` (results_FINAL.md:968, mean or delta) | 3 | LOCF delta | -0.51 | -0.30 | Moderate | Same, attenuated |
- `4` (results_FINAL.md:969, mean or delta) | 4 | Pooled trajectory delta | -1.26 | -1.04 | Moderate | Same, attenuated |
- `1.26` (results_FINAL.md:969, mean or delta) | 4 | Pooled trajectory delta | -1.26 | -1.04 | Moderate | Same, attenuated |
- `1.04` (results_FINAL.md:969, mean or delta) | 4 | Pooled trajectory delta | -1.26 | -1.04 | Moderate | Same, attenuated |
- `5` (results_FINAL.md:970, mean or delta) | 5 | Domain deltas | -1.15 to -1.35 | -0.82 to -1.16 | Moderate | Same, attenuated |
- `1.15` (results_FINAL.md:970, mean or delta) | 5 | Domain deltas | -1.15 to -1.35 | -0.82 to -1.16 | Moderate | Same, attenuated |
- `1.35` (results_FINAL.md:970, mean or delta) | 5 | Domain deltas | -1.15 to -1.35 | -0.82 to -1.16 | Moderate | Same, attenuated |
- `0.82` (results_FINAL.md:970, mean or delta) | 5 | Domain deltas | -1.15 to -1.35 | -0.82 to -1.16 | Moderate | Same, attenuated |
- `1.16` (results_FINAL.md:970, mean or delta) | 5 | Domain deltas | -1.15 to -1.35 | -0.82 to -1.16 | Moderate | Same, attenuated |
- `6` (results_FINAL.md:971, percentage) | 6 | Level-6 at T5 | 47.9% | 34.4% | **YES** | Same, lower |
- `6` (results_FINAL.md:971, percentage) | 6 | Level-6 at T5 | 47.9% | 34.4% | **YES** | Same, lower |
- `47.9` (results_FINAL.md:971, percentage) | 6 | Level-6 at T5 | 47.9% | 34.4% | **YES** | Same, lower |
- `34.4` (results_FINAL.md:971, percentage) | 6 | Level-6 at T5 | 47.9% | 34.4% | **YES** | Same, lower |
- `0.94` (results_FINAL.md:972, percentage) | -- | Balanced cliff | -0.94 | -0.74 | Moderate | Same (21% smaller) |
- `0.74` (results_FINAL.md:972, percentage) | -- | Balanced cliff | -0.94 | -0.74 | Moderate | Same (21% smaller) |
- `21` (results_FINAL.md:972, percentage) | -- | Balanced cliff | -0.94 | -0.74 | Moderate | Same (21% smaller) |
- `1` (results_FINAL.md:975, mean or delta) 1. Targeted feedback delta quintuples (+0.25 -> +1.16) and becomes universal across models
- `0.25` (results_FINAL.md:975, mean or delta) 1. Targeted feedback delta quintuples (+0.25 -> +1.16) and becomes universal across models
- `1.16` (results_FINAL.md:975, mean or delta) 1. Targeted feedback delta quintuples (+0.25 -> +1.16) and becomes universal across models
- `2` (results_FINAL.md:976, bare number) 2. Level-6 rate drops ~14pp (meta-commentary was triggering "Overdone")
- `6` (results_FINAL.md:976, bare number) 2. Level-6 rate drops ~14pp (meta-commentary was triggering "Overdone")
- `3` (results_FINAL.md:977, mean or delta) 3. LOCF delta nearly halves (-0.51 -> -0.30)
- `0.51` (results_FINAL.md:977, mean or delta) 3. LOCF delta nearly halves (-0.51 -> -0.30)
- `0.30` (results_FINAL.md:977, mean or delta) 3. LOCF delta nearly halves (-0.51 -> -0.30)
- `3847` (results_FINAL.md:985, bare number) - Server running on port 3847 (PID 96795) -- can be killed when no longer needed
- `96795` (results_FINAL.md:985, bare number) - Server running on port 3847 (PID 96795) -- can be killed when no longer needed

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
