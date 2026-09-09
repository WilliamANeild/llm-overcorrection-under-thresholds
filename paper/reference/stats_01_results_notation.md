# Statistical notation in RESULTS sections: a 24-paper survey

Purpose: establish what statistical notation a results section in the LLM
self-correction / revision / LLM-as-judge literature reports as a matter of course, and
what is optional, so that the Study 3 analysis ledger (Cohen's kappa, Krippendorff's
alpha, chi-squared, Spearman rho, Wilcoxon, effect sizes) can be translated into
results-section prose at the register the venue expects.

Compiled 2026-09-06. All 24 papers fetched the same day from `arxiv.org/html/<id><v>`.
No paper is cited here that was not fetched and parsed; every quotation is verbatim from
the fetched HTML.

---

## 1. Method, and its limits

**Retrieval.** 24 arXiv HTML renderings fetched 2026-09-06 via `curl` from
`https://arxiv.org/html/<id><version>`, taking the highest available version that
returned more than 60 KB. The exact URL used for each paper is in the corpus table.
All 24 targets returned arXiv's own LaTeXML HTML; no paper needed the `ar5iv` fallback,
and no paper in the intended corpus was unreachable.

**Parsing.** Each document was parsed with BeautifulSoup. Mathematics was recovered from
the `alttext` attribute of each `<math>` element, so `\kappa` and `\alpha` are visible to
the search as LaTeX source rather than being lost as MathML. Every `<p>`, `<li>`, `<td>`,
`<th>`, `<figcaption>` and `ltx_note` element was recorded as a block, tagged with its
placement (prose, table, caption, footnote) and its enclosing section heading. Footnotes
were pulled out before the prose pass, because LaTeXML nests them inside the body
paragraph and they otherwise merge into the sentence that references them.

**Section classification.** Headings were classified as results, methods, appendix, or
other. Level-1 headings set the class; subsections inherit it unless the subheading names
a distinct kind of content. The automatic rule was then hand-corrected for 16 of the 24
papers, because many papers in this literature have no heading called "Results" and
instead name the section after the finding ("LLMs Cannot Self-Correct Reasoning
Intrinsically", "AI Assistants Can Be Easily Swayed", "Agreement Evaluation"). The
overrides are recorded in the working script and are listed per paper in section 3.

**Counting.** Counts are mechanical. Twenty regular expressions were run over every
sentence of every block; a sentence is counted once per statistic it matches, and
duplicate sentences within a paper were removed. The unit is the sentence, not the
occurrence, so a sentence naming both Spearman and Kendall counts once for each. Sentence
splitting is regex-based on terminal punctuation with abbreviation protection, so a small
number of table cells and equation fragments appear as short "sentences"; these are marked
by their `table` placement.

**Known false positives, checked by hand and excluded from the interpretation:**

- `p=0.9` and `p=1` in 2305.01937 and 2303.16634 are nucleus-sampling top-p, not p-values.
- The two `wilcoxon` matches are both spurious ("assigned rank", "human-assigned
  rankings"). **There is no Wilcoxon or Mann-Whitney test anywhere in the 24 papers.**
- `\rho` in 2505.06120 is a shard-order permutation function, not a correlation.
- `\alpha` matches split three ways and must not be pooled: Krippendorff's alpha (4
  papers), a significance level (2403.04132), a Bayesian prior scale (2310.13548), and a
  model-merging weight (2405.01535). Section 5.3 separates them.
- `effect size` in 2310.13548 refers to Bayesian logistic-regression coefficients, not to
  Cohen's d. **No paper in the corpus reports Cohen's d.**

**Bounds of this sweep.** One literature (LLM self-correction, revision, and
LLM-as-judge), one language, arXiv HTML only. The sweep does not cover the ACL Anthology
proceedings versions, which for several of these papers differ from the arXiv version. It
does not cover psycholinguistics, crowdsourcing-methods, or annotation-theory venues,
where reporting conventions are heavier than anything found here.

---

## 2. Corpus

Retrieved 2026-09-06. "Style" records an observation about the document's own sectioning
and template conventions, not a verified venue: papers marked HCI use ACM-style numbered
sections with trailing periods and report a user study; papers marked NLP/ML use the ACL
or NeurIPS section conventions.

| # | arXiv ID | Short title | Style | Source URL |
|---|---|---|---|---|
| 1 | 2201.06796 | CoAuthor: Human-AI Collaborative Writing Dataset | HCI | https://arxiv.org/html/2201.06796v2 |
| 2 | 2206.05802 | Self-critiquing models for assisting human evaluators | NLP/ML | https://arxiv.org/html/2206.05802v2 |
| 3 | 2212.09746 | Evaluating Human-Language Model Interaction | NLP/ML | https://arxiv.org/html/2212.09746v4 |
| 4 | 2303.03199 | Choice Over Control: How Users Write with LLMs | HCI | https://arxiv.org/html/2303.03199v1 |
| 5 | 2303.16634 | G-Eval: NLG Evaluation using GPT-4 | NLP/ML | https://arxiv.org/html/2303.16634v3 |
| 6 | 2303.17651 | Self-Refine: Iterative Refinement with Self-Feedback | NLP/ML | https://arxiv.org/html/2303.17651v2 |
| 7 | 2305.01937 | Can LLMs Be an Alternative to Human Evaluation? | NLP/ML | https://arxiv.org/html/2305.01937v1 |
| 8 | 2305.17926 | Large Language Models are not Fair Evaluators | NLP/ML | https://arxiv.org/html/2305.17926v2 |
| 9 | 2306.05685 | Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena | NLP/ML | https://arxiv.org/html/2306.05685v4 |
| 10 | 2309.12570 | Creativity Support in the Age of LLMs | HCI | https://arxiv.org/html/2309.12570v3 |
| 11 | 2310.01798 | LLMs Cannot Self-Correct Reasoning Yet | NLP/ML | https://arxiv.org/html/2310.01798v2 |
| 12 | 2310.13548 | Towards Understanding Sycophancy in Language Models | NLP/ML | https://arxiv.org/html/2310.13548v4 |
| 13 | 2311.08516 | LLMs cannot find reasoning errors, but can correct them | NLP/ML | https://arxiv.org/html/2311.08516v3 |
| 14 | 2402.11436 | Pride and Prejudice: LLM Amplifies Self-Bias | NLP/ML | https://arxiv.org/html/2402.11436v2 |
| 15 | 2403.04132 | Chatbot Arena | NLP/ML | https://arxiv.org/html/2403.04132v1 |
| 16 | 2404.12272 | Who Validates the Validators? | HCI | https://arxiv.org/html/2404.12272v1 |
| 17 | 2404.13076 | LLM Evaluators Recognize and Favor Their Own Generations | NLP/ML | https://arxiv.org/html/2404.13076v1 |
| 18 | 2405.01535 | Prometheus 2 | NLP/ML | https://arxiv.org/html/2405.01535v2 |
| 19 | 2406.01297 | When Can LLMs Actually Correct Their Own Mistakes? | NLP/ML | https://arxiv.org/html/2406.01297v3 |
| 20 | 2406.12624 | Judging the Judges | NLP/ML | https://arxiv.org/html/2406.12624v4 |
| 21 | 2406.18403 | LLMs instead of Human Judges? | NLP/ML | https://arxiv.org/html/2406.18403v3 |
| 22 | 2410.16184 | RM-Bench | NLP/ML | https://arxiv.org/html/2410.16184v1 |
| 23 | 2505.06120 | LLMs Get Lost In Multi-Turn Conversation | NLP/ML | https://arxiv.org/html/2505.06120v1 |
| 24 | 2509.08010 | Measuring and Mitigating Overreliance | NLP/ML | https://arxiv.org/html/2509.08010v2 |

Six anchors requested for this survey are numbers 23 (Laban), 12 (Sharma), 9 (Zheng),
19 (Kamoi), 11 (Huang) and 13 (Tyen). The other 18 were added weighted toward papers with
a human evaluation or an inter-rater agreement statistic.

---

## 3. Where the results section is, in each paper

Ten of the 24 papers have no heading containing the word "Results". The results-bearing
sections used for the counts:

| arXiv ID | Section(s) counted as results |
|---|---|
| 2201.06796 | 5. Demonstrating Uses of CoAuthor (and 5.x) |
| 2206.05802 | 3 Assisting critique finding; 3.3 Findings; 4 Critique quality results; 5.3 Results |
| 2212.09746 | 3 Experiments (and 3.1 through 3.6) |
| 2303.03199 | 7. Results (and 7.x); 8. Open Feedback |
| 2303.16634 | 3.4 through 3.6 Results for ...; 4 Analysis |
| 2303.17651 | 3.3 Results; 4 Analysis |
| 2305.01937 | 3.3 Experiment Results (and 3.3.x); 4.3 Experiment Result |
| 2305.17926 | 2.2 Revealing the Positional Bias; 4.3 Main Results; 5.1 through 5.4 |
| 2306.05685 | 4 Agreement Evaluation; 4.2; 4.3; 5 Human Preference Benchmark |
| 2309.12570 | 5.1 through 5.3; 6. Feedback from Writers |
| 2310.01798 | 3.2 Results; 3.3; 4 Multi-Agent Debate ...; 5 Prompt Design Issues |
| 2310.13548 | 3 Measuring Sycophancy (and 3.1 to 3.4); 4.1 to 4.3 |
| 2311.08516 | 3 Can LLMs find reasoning mistakes ... (and 3.x); 4 Can LLMs correct ...; 5 |
| 2402.11436 | 4.2 to 4.4; 5 Alleviating Self-Bias |
| 2403.04132 | 6 Data Analysis (and 6.x); 7.1 Ranking system; 7.2 Anomalous Users Detection |
| 2404.12272 | 5.2.2. Results; 7. User Study Findings (and 7.x) |
| 2404.13076 | 2.3 to 2.5; 3.2 Fine-Tuning Results; 3.3 to 3.5 |
| 2405.01535 | 5 Experimental Results (and 5.x); 6 Analyses of Weight Merging (and 6.x) |
| 2406.01297 | 4 Self-Correction with Prompting; 5 ... External Information; 6 Strong Baselines; 7 Summary |
| 2406.12624 | 4 Results (and 4.x); 5 Analysis (and 5.x) |
| 2406.18403 | 4 Results |
| 2410.16184 | 4 Evaluation Results (and 4.x); 5 Correlation with Policy Model (and 5.x) |
| 2505.06120 | 6 Results (and 6.1 to 6.3) |
| 2509.08010 | The current lack of empirical evidence (position paper, no experimental results section) |

---

## 4. Counts

### 4.1 Headline count

465 sentences across the 24 papers contain at least one statistical marker.

Placement of those 465 sentences:

| Placement | Sentences | Share |
|---|---|---|
| Body prose | 328 | 71% |
| Figure or table caption | 92 | 20% |
| Inside a table (cell or header) | 40 | 9% |
| Footnote | 5 | 1% |

### 4.2 Per-statistic counts

Sentence counts. "Papers" is the number of the 24 papers in which the statistic appears
anywhere; "Res.pap" is the number in which it appears inside a results section. Columns
res/meth/app/oth are sentence counts by section class; prose/tab/cap/fn are sentence
counts by placement.

| Statistic | Sents | Papers | res | meth | app | oth | prose | tab | cap | fn | Res.pap |
|---|---|---|---|---|---|---|---|---|---|---|---|
| "significant(ly)" as a word | 221 | 22 | 100 | 7 | 56 | 58 | 181 | 5 | 33 | 2 | 18 |
| Spearman / rho | 39 | 5 | 9 | 11 | 16 | 3 | 21 | 4 | 14 | 0 | 3 |
| p-value | 33 | 7 | 20 | 7 | 6 | 0 | 17 | 9 | 5 | 2 | 5 |
| regression model | 31 | 4 | 5 | 5 | 18 | 3 | 30 | 0 | 1 | 0 | 2 |
| alpha (all senses) | 31 | 7 | 14 | 6 | 9 | 2 | 17 | 11 | 3 | 0 | 4 |
| sigma / standard deviation | 27 | 7 | 7 | 3 | 14 | 3 | 16 | 6 | 5 | 0 | 4 |
| Kendall / tau | 27 | 4 | 16 | 7 | 4 | 0 | 14 | 1 | 11 | 1 | 3 |
| "statistically significant" | 26 | 8 | 14 | 0 | 10 | 2 | 15 | 0 | 10 | 1 | 5 |
| kappa | 24 | 5 | 5 | 6 | 7 | 6 | 11 | 3 | 8 | 2 | 3 |
| Pearson / r | 19 | 6 | 11 | 2 | 5 | 1 | 12 | 0 | 7 | 0 | 5 |
| standard error | 17 | 5 | 11 | 1 | 3 | 2 | 4 | 1 | 12 | 0 | 3 |
| confidence interval | 14 | 5 | 1 | 3 | 8 | 2 | 12 | 0 | 2 | 0 | 1 |
| "effect size" | 13 | 1 | 3 | 0 | 10 | 0 | 7 | 0 | 6 | 0 | 1 |
| bootstrap | 12 | 4 | 1 | 3 | 6 | 2 | 10 | 1 | 1 | 0 | 1 |
| Delta | 12 | 3 | 5 | 0 | 3 | 4 | 6 | 2 | 4 | 0 | 2 |
| Krippendorff | 11 | 4 | 3 | 4 | 3 | 1 | 7 | 1 | 3 | 0 | 2 |
| multiple-comparison correction | 7 | 2 | 0 | 1 | 5 | 1 | 3 | 0 | 4 | 0 | 0 |
| chi-squared | 5 | 1 | 2 | 3 | 0 | 0 | 4 | 0 | 1 | 0 | 1 |
| t-test | 2 | 1 | 2 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 1 |
| Wilcoxon / Mann-Whitney | 0 (2 spurious) | 0 | - | - | - | - | - | - | - | - | 0 |
| ANOVA / Kruskal / Friedman / McNemar / Fisher exact | 0 | 0 | - | - | - | - | - | - | - | - | 0 |
| eta-squared | 0 | 0 | - | - | - | - | - | - | - | - | 0 |
| Cohen's d | 0 | 0 | - | - | - | - | - | - | - | - | 0 |

### 4.3 Which papers report which statistic

| Statistic | Papers reporting it anywhere | Papers reporting it in results |
|---|---|---|
| kappa | 5: 2305.17926, 2309.12570, 2406.12624, 2406.18403, 2509.08010 | 3: 2305.17926, 2309.12570, 2406.18403 |
| Krippendorff's alpha | 4: 2303.16634, 2305.01937, 2311.08516, 2405.01535 | 2: 2303.16634, 2305.01937 |
| Scott's pi | 1: 2406.12624 | 1: 2406.12624 |
| Spearman | 4: 2303.16634, 2405.01535, 2406.12624, 2406.18403 | 3: 2303.16634, 2406.12624, 2406.18403 |
| Kendall's tau | 4: 2303.16634, 2305.01937, 2404.13076, 2405.01535 | 3: 2303.16634, 2305.01937, 2404.13076 |
| Pearson's r | 6: 2201.06796, 2303.16634, 2309.12570, 2405.01535, 2406.12624, 2410.16184 | 5: 2201.06796, 2303.16634, 2309.12570, 2405.01535, 2410.16184 |
| numeric p-value attached to a test | 5: 2212.09746, 2303.03199, 2309.12570, 2406.18403, 2410.16184 | 5: same |
| regression model | 4: 2212.09746, 2303.03199, 2310.13548, 2403.04132 | 2: 2303.03199, 2310.13548 |
| standard error | 5: 2201.06796, 2206.05802, 2212.09746, 2310.13548, 2403.04132 | 3: 2201.06796, 2212.09746, 2310.13548 |
| confidence interval | 5: 2212.09746, 2303.17651, 2403.04132, 2404.12272, 2406.12624 | 1: 2403.04132 |
| multiple-comparison correction | 2: 2212.09746, 2403.04132 | 0 |
| chi-squared | 1: 2403.04132 (as a CLT interval, not a test of association) | 1 |
| t-test | 1: 2305.01937 (Welch) | 1 |
| Tukey-Kramer | 1: 2212.09746 | 1 |

**Six of the 24 papers name no statistical test or coefficient anywhere in the paper**,
outside the loose word "significant": 2306.05685 (Zheng), 2310.01798 (Huang), 2402.11436,
2404.12272, 2406.01297 (Kamoi), and 2505.06120 (Laban). This was checked with a separate
sweep for eponymous and Greek-letter statistics over each full document with
acknowledgements and references removed. 2404.12272's only match is "Likert", a scale
type rather than a statistic; 2505.06120's only Greek letter is a shard-order permutation
function. 2305.17926 is not in this group only because it writes "kappa correlation
coefficient", without naming whose kappa.

---

## 5. Verbatim catalogue, organised by statistic

Every sentence below is quoted verbatim from the fetched HTML. Mathematics appears as
the LaTeX source recovered from the `alttext` attribute, so `\kappa` in a quotation is a
rendered kappa symbol in the published paper, not a literal backslash. Each entry is
tagged `[arXiv ID | section class | placement | section heading]`.


### 5.1 Cohen's kappa, Fleiss' kappa, and the word "kappa"

**RESULTS (5 sentences)**

- `[2305.17926 | results | prose | 4.3 Main Results]`
  > In detail, the average accuracy and the kappa correlation coefficient of human annotations are 71.7 % and 0.54 , respectively; 2) Overall, GPT-4 achieves higher alignment with human judgments compared with ChatGPT, showing its powerful alignment ability with humans; 3) Compared to the commonly used Vanilla evaluation method, our proposed automatic calibration strategies (i.e., EC, MEC and BPC) significantly enhance the alignment between GPT-4 and ChatGPT with human judgments; For instance, by employing the MEC and BPC calibration strategies, ChatGPT demonstrates a notable improvement in both accuracy and the kappa correlation coefficient.

- `[2305.17926 | results | prose | 4.3 Main Results]`
  > Specifically, the accuracy is improved by 14.3%, and the kappa correlation coefficient is increased from 0.06 to 0.31 ; 4) “MEC ( k=3 ) + BPC ( k=3 )” outperforms “MEC ( k=6 )”, demonstrating that LLMs are affected by positional bias, and BPC effectively ensures that LLMs serve as fair evaluators; 5) Our proposed HITLC can effectively enhance the alignment between GPT-4 and ChatGPT with human judgments, requiring only a small amount of human labor.

- `[2305.17926 | results | caption | 5.1 Ablation on Evidence Number k and Temper]`
  > Figure 4: Variation of accuracy and kappa coefficient with a different number of evidence k and sampling temperature t when ChatGPT is used as the evaluator.

- `[2309.12570 | results | footnote | 5.2. Identifying Patterns in User Interactio]`
  > 1414 14 The Fleiss’ kappa of annotations was 0.52 , indicative of moderate agreement on the task.

- `[2406.18403 | results | caption | 4 Results]`
  > Figure 4: Scores (Cohen’s \kappa for categorical annotations and Spearman’s correlation for graded annotations) on test items involving human language vs. machine-generated outputs.

**METHODS (6 sentences)**

- `[2305.17926 | methods | prose | 4.2 Experimental Setup and Metric]`
  > We use the accuracy and kappa correlation coefficient McHugh (2012) with the final majority of human annotation results to measure the performance of different evaluators and evaluation methods.

- `[2406.18403 | methods | table | 2 Construction of Judge-Bench]`
  > Average Cohen’s \kappa

- `[2406.18403 | methods | caption | 2 Construction of Judge-Bench]`
  > Table 1: Scores per dataset for the models with \geq 98% valid response rates (results for all models in Tab. 6, App. H): Cohen’s kappa for categorical annotations and Spearman’s correlation for graded annotations.

- `[2406.18403 | methods | prose | 3 Model Selection and Experiment Design]`
  > For the former, we compute Spearman’s correlation ( \rho ) between model and human judgments; for the latter, we compute Cohen’s \kappa .

- `[2406.18403 | methods | prose | 3 Model Selection and Experiment Design]`
  > • When multiple individual human judgments are available (typically three, see Table 2 in Appendix A), we estimate an upper bound by computing the average Spearman’s \rho or Cohen’s \kappa between bootstrapped single-rater responses and the aggregated responses across raters.

- `[2406.18403 | methods | prose | 3 Model Selection and Experiment Design]`
  > When multiple individual human judgments are available (typically three, see Table 2 in Appendix A), we estimate an upper bound by computing the average Spearman’s \rho or Cohen’s \kappa between bootstrapped single-rater responses and the aggregated responses across raters.

**APPENDIX (7 sentences)**

- `[2406.12624 | appendix | table | Appendix B A brief explanation of the theore]`
  > \kappa\equiv\frac{p_{o}-p_{e}}{1-p_{e}}

- `[2406.18403 | appendix | prose | Appendix C Upper Bound Estimation for Model ]`
  > Alignment was computed as Spearman’s correlation for graded judgments and Cohen’s kappa for categorical judgments.

- `[2406.18403 | appendix | caption | Appendix H Additional Results]`
  > Table 4: Cohen’s kappa for DICES-350-expert and Spearman’s correlation for two WMT 2023 datasets, comparing the original prompt and CoT prompt to few-shot prompts and prompt paraphrases for a selection of models.

- `[2406.18403 | appendix | caption | Appendix H Additional Results]`
  > Table 6: Scores per dataset for all models we evaluate: Cohen’s kappa for categorical annotations and Spearman’s correlation for graded annotations.

- `[2406.18403 | appendix | caption | Appendix H Additional Results]`
  > Table 7: Scores per dataset for all models we evaluate using CoT prompts: Cohen’s kappa for categorical annotations and Spearman’s correlation for graded annotations.

- `[2509.08010 | appendix | table | Validation]`
  > Cohen’s \kappa

- `[2509.08010 | appendix | caption | Validation]`
  > \kappa corresponds to “moderate” agreement.

**OTHER (4 sentences)**

- `[2305.17926 | other | caption | 3.2 Balanced Position Calibration]`
  > Table 4: Accuracy and kappa correlation coefficient of different methods and annotators with the final voting human annotations.

- `[2305.17926 | other | prose | 7 Conclusion]`
  > Interrater reliability: the kappa statistic.

- `[2406.12624 | other | prose | (front matter)]`
  > B A brief explanation of the theoretical issues with Cohen’s kappa

- `[2406.12624 | other | footnote | 3 Methodology]`
  > 33 3 In an earlier version of this paper, we used Cohen’s kappa (Cohen, 1960) to measure alignment.



### 5.2 Krippendorff's alpha

**RESULTS (3 sentences)**

- `[2303.16634 | results | prose | 4 Analysis]`
  > The authors of the original paper found that inter-annotator agreement on judging human-written and LLM-generated summaries is very low, with Krippendorff’s alpha at 0.07.

- `[2305.01937 | results | prose | 3.3 Experiment Results]`
  > We report the mean and standard deviation of the Likert scores obtained from LLM evaluation and human evaluation and show the inter-annotator agreement (IAA) using two different metrics: (1) the Krippendorff’s \alpha , and (2) the percentage of the stories where three evaluators give the exact same rating.

- `[2305.01937 | results | prose | 3.3 Experiment Results]`
  > We also find the Krippendorff’s \alpha of text-davinci-003 is much higher than T0 and text-curie-001, indicating that the rating by text-davinci-003 is more consistent among different samplings of the generated answers.

**METHODS (4 sentences)**

- `[2305.01937 | methods | caption | 3.1 Task Introduction]`
  > We also report the inter-annotator agreement (IAA) among three annotators using Krippendorff’s \alpha .

- `[2311.08516 | methods | prose | 2.1.1 Human annotation]`
  > We calculate Krippendorff’s alpha (Hayes and Krippendorff, 2007) to measure inter-rater reliability (see Table 3).

- `[2311.08516 | methods | table | 2.1.1 Human annotation]`
  > Krippendorff’s \alpha

- `[2311.08516 | methods | caption | 2.1.1 Human annotation]`
  > Table 3: Inter-rater reliability for the human-annotated tasks, measured by Krippendorff’s alpha.

**APPENDIX (3 sentences)**

- `[2405.01535 | appendix | prose | Appendix B Training and Inference Details]`
  > Instead of using error bars, we report the consistency in assessment formats, Krippendorff’s alpha for consistency in direct assessment, and transitivity statistics for consistency in pairwise ranking.

- `[2405.01535 | appendix | caption | Appendix D License]`
  > Table 14: Krippendorff’s alpha statistics for evaluator LMs when prompted 3 times via non-deterministic decoding.

- `[2405.01535 | appendix | prose | Appendix E Consistency of Evaluator LMs]`
  > Following the experimental design from Ye et al. (2023), we choose to inference 3 times and report the Krippendorff’s alpha value.



### 5.3 Scott's pi

**RESULTS (1 sentences)**

- `[2406.12624 | results | prose | 4.2 Exploring consistent patterns in judge m]`
  > Specifically, both contains and Mistral 7B, with Scott’s \mathbf{\pi} values of 64 and 66, respectively, exhibit very high rank correlation with the human scores ( \rho 0.99 and 0.98, respectively, with \sigma 0.02 and 0.03).

**APPENDIX (2 sentences)**

- `[2406.12624 | appendix | prose | Appendix I Statistical reliability of Evalua]`
  > In this section, we further take 5 samples of 300 randomly selected questions from the evaluation set and calculate the mean and standard deviation of Scott’s Pi.

- `[2406.12624 | appendix | prose | Appendix O Leniency Bias]`
  > As shown in Figure 17(b), we observe that the estimated values of P_{c} are highly correlated to the Scott’s \mathbf{\pi} values for the judge models, with a Pearson correlation coefficient of 0.98 .



### 5.4 Spearman correlation and rho

**RESULTS (9 sentences)**

- `[2303.16634 | results | prose | 3.4 Results for Summarization]`
  > We adopt the same approach as Zhong et al. (2022) to evaluate different summarization metrics using summary-level Spearman and Kendall-Tau correlation.

- `[2303.16634 | results | prose | 3.4 Results for Summarization]`
  > G-Eval-4 achieved much higher human correspondence compared with G-Eval-3.5 on both Spearman and Kendall-Tau correlation, which indicates that the larger model size of GPT-4 is beneficial for summarization evaluation.

- `[2303.16634 | results | prose | 3.5 Results for Dialogue Generation]`
  > We calculate the Pearson and Spearman correlation for each turn of the dialogue.

- `[2303.16634 | results | caption | 4 Analysis]`
  > Table 3: Pearson ( r ), Spearman ( \rho ) and Kendall-Tau ( \tau ) correlations of different metrics on QAGS benchmark.

- `[2303.16634 | results | prose | 4 Analysis]`
  > This is reflected by the higher Spearman correlation of G-Eval-4 with probabilities, which is based on the rank order of the scores.

- `[2406.12624 | results | prose | 4.2 Exploring consistent patterns in judge m]`
  > To evaluate this, we compare the rankings assigned by each judge model to the nine exam-taker models by computing their Spearman’s rank correlation coefficients \rho (Spearman, 1904) with the human ranking.

- `[2406.12624 | results | prose | 4.2 Exploring consistent patterns in judge m]`
  > We show the rankings in Figure 3(a), with \rho and corresponding \sigma values in Appendix L.

- `[2406.12624 | results | prose | 4.2 Exploring consistent patterns in judge m]`
  > Specifically, both contains and Mistral 7B, with Scott’s \mathbf{\pi} values of 64 and 66, respectively, exhibit very high rank correlation with the human scores ( \rho 0.99 and 0.98, respectively, with \sigma 0.02 and 0.03).

- `[2406.18403 | results | caption | 4 Results]`
  > Figure 4: Scores (Cohen’s \kappa for categorical annotations and Spearman’s correlation for graded annotations) on test items involving human language vs. machine-generated outputs.

**METHODS (10 sentences)**

- `[2303.16634 | methods | caption | 2 Method]`
  > Table 1: Summary-level Spearman ( \rho ) and Kendall-Tau ( \tau ) correlations of different metrics on SummEval benchmark.

- `[2303.16634 | methods | caption | 3.3 Baselines]`
  > Table 2: Turn-level Spearman ( \rho ) and Kendall-Tau ( \tau ) correlations of different metrics on Topical-Chat benchmark.

- `[2405.01535 | methods | caption | 4 Experimental Setup]`
  > Spearman and Kendall-Tau correlations are reported in Appendix C.

- `[2405.01535 | methods | prose | 4 Experimental Setup]`
  > We use Pearson, Spearman, and Kendall-Tau as performance metrics to measure scoring correlations against reference evaluators.

- `[2406.18403 | methods | table | 2 Construction of Judge-Bench]`
  > Average Spearman’s \rho

- `[2406.18403 | methods | caption | 2 Construction of Judge-Bench]`
  > Table 1: Scores per dataset for the models with \geq 98% valid response rates (results for all models in Tab. 6, App. H): Cohen’s kappa for categorical annotations and Spearman’s correlation for graded annotations.

- `[2406.18403 | methods | caption | 2 Construction of Judge-Bench]`
  > Spearman’s correlations are generally significant ( p<0.05 ), with the exception of the Persona Chat and Topical Chat datasets (see Tab. 6 in Appendix H for more details).

- `[2406.18403 | methods | prose | 3 Model Selection and Experiment Design]`
  > For the former, we compute Spearman’s correlation ( \rho ) between model and human judgments; for the latter, we compute Cohen’s \kappa .

- `[2406.18403 | methods | prose | 3 Model Selection and Experiment Design]`
  > • When multiple individual human judgments are available (typically three, see Table 2 in Appendix A), we estimate an upper bound by computing the average Spearman’s \rho or Cohen’s \kappa between bootstrapped single-rater responses and the aggregated responses across raters.

- `[2406.18403 | methods | prose | 3 Model Selection and Experiment Design]`
  > When multiple individual human judgments are available (typically three, see Table 2 in Appendix A), we estimate an upper bound by computing the average Spearman’s \rho or Cohen’s \kappa between bootstrapped single-rater responses and the aggregated responses across raters.

**APPENDIX (15 sentences)**

- `[2405.01535 | appendix | prose | Appendix C Direct Assessment Results: Extend]`
  > Even when changing the metrics to either Kendall-Tau and Spearman, the overall trends are maintained.

- `[2405.01535 | appendix | caption | Appendix D License]`
  > Table 12: Spearman correlations between reference evaluators (listed on top) and evaluator LMs.

- `[2406.12624 | appendix | prose | Appendix F Metrics for judge models]`
  > For the binary case, the alignment ratio \rho is given as

- `[2406.12624 | appendix | table | Appendix F Metrics for judge models]`
  > \rho=\frac{T_{P}+T_{N}}{T_{P}+F_{P}+T_{N}+F_{N}}.

- `[2406.12624 | appendix | prose | Appendix L Exam-taker model ranking correlat]`
  > In Table 11, We use the Spearman Rank correlation coefficient (Spearman, 1904) to assess the rankings of the exam-taker models.

- `[2406.12624 | appendix | prose | Appendix L Exam-taker model ranking correlat]`
  > To validate these rankings, we randomly select 6 out of 9 exam-taker models across 5 samples, subsequently calculating the mean ( \rho ) and standard deviation ( \sigma ) of the rankings.

- `[2406.12624 | appendix | prose | Appendix L Exam-taker model ranking correlat]`
  > The results reveal that the contains model exhibits the highest stability and \rho among the rankings, while the majority of judge models achieve a coefficient exceeding 0.7, indicating a strong alignment.

- `[2406.12624 | appendix | caption | Appendix L Exam-taker model ranking correlat]`
  > Table 11: Spearman Rank Correlation Coefficient \rho .

- `[2406.18403 | appendix | prose | Appendix C Upper Bound Estimation for Model ]`
  > Alignment was computed as Spearman’s correlation for graded judgments and Cohen’s kappa for categorical judgments.

- `[2406.18403 | appendix | caption | Appendix H Additional Results]`
  > Table 4: Cohen’s kappa for DICES-350-expert and Spearman’s correlation for two WMT 2023 datasets, comparing the original prompt and CoT prompt to few-shot prompts and prompt paraphrases for a selection of models.

- `[2406.18403 | appendix | caption | Appendix H Additional Results]`
  > For Spearman’s correlations, we report the number of significant correlations ( p<0.05 ) for each model and dataset in brackets.

- `[2406.18403 | appendix | caption | Appendix H Additional Results]`
  > Table 6: Scores per dataset for all models we evaluate: Cohen’s kappa for categorical annotations and Spearman’s correlation for graded annotations.

- `[2406.18403 | appendix | caption | Appendix H Additional Results]`
  > Table 7: Scores per dataset for all models we evaluate using CoT prompts: Cohen’s kappa for categorical annotations and Spearman’s correlation for graded annotations.

- `[2406.18403 | appendix | caption | Appendix H Additional Results]`
  > For Spearman’s correlation, we report the number of significant correlations for each model and dataset in brackets.

- `[2505.06120 | appendix | prose | Appendix B Precise Definition of Sharded Ins]`
  > Let \rho(\mathbf{s}_{2..k}) refer to a permutation of the shard ordering, then I(q)=I(\tilde{q})\;\forall\tilde{q}=[s_{1},\rho(\mathbf{s}_{2..k})]

**OTHER (1 sentences)**

- `[2303.16634 | other | prose | (front matter)]`
  > We show that G-Eval with GPT-4 as the backbone model achieves a Spearman correlation of 0.514 with human on summarization task, outperforming all previous methods by a large margin.



### 5.5 Kendall's tau

**RESULTS (16 sentences)**

- `[2303.16634 | results | prose | 3.4 Results for Summarization]`
  > We adopt the same approach as Zhong et al. (2022) to evaluate different summarization metrics using summary-level Spearman and Kendall-Tau correlation.

- `[2303.16634 | results | prose | 3.4 Results for Summarization]`
  > G-Eval-4 achieved much higher human correspondence compared with G-Eval-3.5 on both Spearman and Kendall-Tau correlation, which indicates that the larger model size of GPT-4 is beneficial for summarization evaluation.

- `[2303.16634 | results | caption | 4 Analysis]`
  > Table 3: Pearson ( r ), Spearman ( \rho ) and Kendall-Tau ( \tau ) correlations of different metrics on QAGS benchmark.

- `[2303.16634 | results | prose | 4 Analysis]`
  > Table 1 shows that, on Kendall-Tau correlation, G-Eval-4 with probabilities is inferior to G-Eval-4 without probabilities on SummEval.

- `[2303.16634 | results | prose | 4 Analysis]`
  > We believe this is related to the calculation of Kendall-Tau correlation, which is based on the number of concordant and discordant pairs.

- `[2303.16634 | results | prose | 4 Analysis]`
  > This may result in a higher Kendall-Tau correlation, but it does not reflect the model’s true capacity of evaluating the generated texts.

- `[2305.01937 | results | prose | 3.3.1 Does LLM and Human Evaluators Agree on]`
  > To answer this question, we calculate Kendall’s \tau correlation coefficient between the ratings of text-davinci-003 and English teachers.

- `[2305.01937 | results | prose | 3.3.1 Does LLM and Human Evaluators Agree on]`
  > We calculate Kendall’s \tau for four rating attributes as follows: For each story and each rating attribute, we calculate the average rating of the three English teachers and calculate the average rating of the three scores given by the text-davinci-003 (which is obtained from three independent samples).

- `[2305.01937 | results | prose | 3.3.1 Does LLM and Human Evaluators Agree on]`
  > Next, we calculate Kendall’s \tau correlation coefficient between A and B .

- `[2305.01937 | results | caption | 3.3.1 Does LLM and Human Evaluators Agree on]`
  > Table 2: The Kendall’s \tau correlation coefficient between English teachers and text-davinci-003.

- `[2305.01937 | results | prose | 3.3.1 Does LLM and Human Evaluators Agree on]`
  > The Kendall’s \tau between teacher ratings and LLM ratings is shown in Table 2.

- `[2305.01937 | results | prose | 3.3.1 Does LLM and Human Evaluators Agree on]`
  > We also observe that Kendall’s \tau for different attributes are quite different: relevance has the strongest correlation while grammaticality has the weakest correlation.

- `[2305.01937 | results | prose | 3.3.1 Does LLM and Human Evaluators Agree on]`
  > We also calculate the average Kendall’s \tau between a pair of English teachers, and we find a weak correlation on grammaticality between the rating of two teachers, while the correlation of the rating on relevance is much stronger.

- `[2305.01937 | results | footnote | 3.3.1 Does LLM and Human Evaluators Agree on]`
  > 44 4 When interpreting Kendall’s \tau , |\tau|\in[0,0.1) is considered as very weak correlation, |\tau|\in[0.1,0.2) is considered as weak correlation, |\tau|\in[0.2,0.3) is considered as moderate correlation, and |\tau|\in[0.3,1.0] is considered as strong correlation (Botsch, 2011).

- `[2404.13076 | results | prose | 3.2 Fine-Tuning Results]`
  > For GPT-3.5 on the XSUM dataset, the evaluator prior to fine-tuning has a correlation of 0.41 (Kendall’s \tau ) between correctly recognizing its summary from a pair and preferring its summary from that same pair.

- `[2404.13076 | results | caption | 3.2 Fine-Tuning Results]`
  > Table 1: Correlation (Kendall’s \tau ) between the LLM’s confidence in recognizing its summary and its confidence in preferring the same summary in pairs of examples.

**METHODS (6 sentences)**

- `[2303.16634 | methods | caption | 2 Method]`
  > Table 1: Summary-level Spearman ( \rho ) and Kendall-Tau ( \tau ) correlations of different metrics on SummEval benchmark.

- `[2303.16634 | methods | caption | 2 Method]`
  > G-Eval without probabilities (italicized) should not be considered as a fair comparison to other metrics on \tau , as it leads to many ties in the scores.

- `[2303.16634 | methods | caption | 2 Method]`
  > This results in a higher Kendall-Tau correlation, but it does not fairly reflect the true evaluation ability.

- `[2303.16634 | methods | caption | 3.3 Baselines]`
  > Table 2: Turn-level Spearman ( \rho ) and Kendall-Tau ( \tau ) correlations of different metrics on Topical-Chat benchmark.

- `[2405.01535 | methods | caption | 4 Experimental Setup]`
  > Spearman and Kendall-Tau correlations are reported in Appendix C.

- `[2405.01535 | methods | prose | 4 Experimental Setup]`
  > We use Pearson, Spearman, and Kendall-Tau as performance metrics to measure scoring correlations against reference evaluators.

**APPENDIX (4 sentences)**

- `[2305.01937 | appendix | caption | C.2 Human Evaluation Interface]`
  > Table 6: The Kendall’s \tau correlation coefficient two English teachers.

- `[2305.01937 | appendix | caption | C.2 Human Evaluation Interface]`
  > Three English teachers participate in the rating, so the result in the Table is average over {3\choose 2} Kendall’s \tau .

- `[2405.01535 | appendix | prose | Appendix C Direct Assessment Results: Extend]`
  > Even when changing the metrics to either Kendall-Tau and Spearman, the overall trends are maintained.

- `[2405.01535 | appendix | caption | Appendix D License]`
  > Table 11: Kendall-Tau correlations between reference evaluators (listed on top) and evaluator LMs.



### 5.6 Pearson's r

**RESULTS (11 sentences)**

- `[2201.06796 | results | prose | 5.2.2. Increasing writers’ feeling of owners]`
  > For ownership scores (rated as a 5-point Likert scale) and the fraction of text written by writers, the Pearson correlation coefficient was 0.3 in both creative and argumentative writing, whereas it was 0.1 and 0.0 for satisfaction scores.

- `[2201.06796 | results | prose | 5.2.2. Increasing writers’ feeling of owners]`
  > For ownership score, the Pearson correlation coefficient was 0.1 in both creative and argumentative writing.

- `[2303.16634 | results | prose | 3.5 Results for Dialogue Generation]`
  > We calculate the Pearson and Spearman correlation for each turn of the dialogue.

- `[2303.16634 | results | caption | 4 Analysis]`
  > Table 3: Pearson ( r ), Spearman ( \rho ) and Kendall-Tau ( \tau ) correlations of different metrics on QAGS benchmark.

- `[2309.12570 | results | prose | 5.2. Identifying Patterns in User Interactio]`
  > We observe that the total instruction count and fraction of templated instructions have a Pearson correlation coefficient of -0.37 indicating that users who ask for more instructions tend to use fewer templated ones, instead opting for instructions with a higher level of specificity (Figure 4(b)).

- `[2405.01535 | results | prose | 5.1 Direct Assessment Results]`
  > The scoring decisions of Prometheus 2 models (7B & 8x7B), GPT-4-1106, Claude-3-Opus, and human evaluators all strongly correlate with each other, yielding Pearson correlations higher than 0.5 regardless of the reference evaluator and benchmark.

- `[2405.01535 | results | caption | 5.2 Pairwise Ranking Results]`
  > Table 5: Single-Format Training vs Joint Training vs Weight Merging Pearson correlations between evaluator LMs trained with different methods and GPT-4-1106.

- `[2405.01535 | results | caption | 5.2 Pairwise Ranking Results]`
  > Table 6: Unifying Formats vs Ensembling Pearson correlations with GPT-4-1106 (Vicuna Bench, MT Bench, FLASK) and agreement with human evaluators (HHH Alignment, MT Bench Human Judgment, Auto-J Eval).

- `[2405.01535 | results | prose | 6.3 Quantifying Positive Transfer across Eva]`
  > To illustrate the average performance (colored in black), we adjust the scale by multiplying the Pearson correlations from direct assessment, which originally range from 0 to 1, by 100 before averaging them with the pairwise ranking accuracy.

- `[2410.16184 | results | prose | 5.2 Downstream Task Correlation]`
  > The Pearson correlation coefficient is 0.55 ( p=0.07 ), indicating a moderate positive correlation trending toward significance.

- `[2410.16184 | results | prose | 5.2 Downstream Task Correlation]`
  > In comparison, RewardBench (Lambert et al., 2024) reports a Pearson correlation of r=0.21 ( p=0.51 ) (see Section F in the appendix).

**METHODS (2 sentences)**

- `[2405.01535 | methods | caption | 4 Experimental Setup]`
  > Table 3: Direct Assessment Results Pearson correlations between reference evaluators (listed on top) and evaluator LMs.

- `[2405.01535 | methods | prose | 4 Experimental Setup]`
  > We use Pearson, Spearman, and Kendall-Tau as performance metrics to measure scoring correlations against reference evaluators.

**APPENDIX (5 sentences)**

- `[2405.01535 | appendix | caption | Appendix E Consistency of Evaluator LMs]`
  > Table 16: Pearson correlations between different evaluator models with and without the reference answer and Human.

- `[2405.01535 | appendix | caption | Appendix E Consistency of Evaluator LMs]`
  > Table 17: Pearson correlations and accuracy measurements across various benchmarks for different merging methods.

- `[2406.12624 | appendix | prose | Appendix O Leniency Bias]`
  > As shown in Figure 17(b), we observe that the estimated values of P_{c} are highly correlated to the Scott’s \mathbf{\pi} values for the judge models, with a Pearson correlation coefficient of 0.98 .

- `[2406.12624 | appendix | caption | Appendix O Leniency Bias]`
  > b) Pearson’s correlation coefficient between \pi and P_{c} for judge models.

- `[2410.16184 | appendix | prose | Appendix F Correlation of Reward Bench]`
  > As Figure 7 shows, the policy model correlation in Reward Bench is not satisfactory where the Pearson correlation coefficient is 0.21 with a p -value of 0.51 .

**OTHER (1 sentences)**

- `[2405.01535 | other | prose | 1 Introduction]`
  > On four direct assessment benchmarks (Vicuna Bench, MT Bench, FLASK, Feedback Bench), the Prometheus 2 models demonstrate the highest correlation with both human evaluators and proprietary LM-based judges compared to existing open evaluator LMs, with the Pearson correlation surpassing other baselines by 0.2 units across all datasets.



### 5.7 alpha, and the three things it means in this corpus

**RESULTS (14 sentences)**

- `[2305.01937 | results | prose | 3.3 Experiment Results]`
  > We report the mean and standard deviation of the Likert scores obtained from LLM evaluation and human evaluation and show the inter-annotator agreement (IAA) using two different metrics: (1) the Krippendorff’s \alpha , and (2) the percentage of the stories where three evaluators give the exact same rating.

- `[2305.01937 | results | prose | 3.3 Experiment Results]`
  > We also find the Krippendorff’s \alpha of text-davinci-003 is much higher than T0 and text-curie-001, indicating that the rating by text-davinci-003 is more consistent among different samplings of the generated answers.

- `[2310.13548 | results | table | 4.1 What Behavior Is Incentivized By Human P]`
  > \displaystyle p(R_{A}\text{ preferred to }R_{B}|\phi,\alpha,P)=\sigma\left(\textstyle\sum_{i=1}^{N_{f}}\alpha_{i}\phi_{i}\right),\quad\text{with }p(\alpha_{i})\sim\operatorname{\text{Laplace}}(\mu=0,b=0.01),

- `[2403.04132 | results | prose | 7.1 Ranking system]`
  > A natural follow-up question is whether or not the intervals are doing their job correctly: whether they cover the true BT coefficients with probability at least (and almost exactly) 1-\alpha .

- `[2403.04132 | results | prose | 7.1 Ranking system]`
  > The results can be seen in Figure 6 for the uncorrected intervals The coverage of the intervals behaves as expected, centering around 1-\alpha , regardless of the number of models.

- `[2403.04132 | results | prose | 7.2 Anomalous Users Detection]`
  > As mentioned in Section 5.1, per user we compute five M_{j} and identify the user as anomalous if M_{j}\geq\chi^{2}_{2j,1-\alpha/5} .

- `[2403.04132 | results | prose | 7.2 Anomalous Users Detection]`
  > We present results of two different \alpha (i.e., the significance leval) in Table 5.

- `[2403.04132 | results | caption | 7.2 Anomalous Users Detection]`
  > Table 5: Confusion matrix of different \alpha .

- `[2403.04132 | results | table | 7.2 Anomalous Users Detection]`
  > \alpha=0.1

- `[2403.04132 | results | table | 7.2 Anomalous Users Detection]`
  > \alpha=0.3

- `[2405.01535 | results | caption | 6.1 Weight Merging vs Joint Training]`
  > Performance of Direct Assessment (colored in green) and Pairwise Ranking (colored in blue) when altering the \alpha value to merge evaluator LMs trained on different formats.

- `[2405.01535 | results | prose | 6.3 Quantifying Positive Transfer across Eva]`
  > To explore how training on direct assessment feedback data influences pairwise ranking accuracy and vice versa, we experiment by adjusting the \alpha value during linear merging.

- `[2405.01535 | results | prose | 6.3 Quantifying Positive Transfer across Eva]`
  > For direct assessment benchmarks, evaluator LMs obtain the optimal performance when \alpha is set to 0.5.

- `[2405.01535 | results | prose | 6.3 Quantifying Positive Transfer across Eva]`
  > On the other hand, for pairwise ranking benchmarks, the performance is optimal when \alpha is set to 0.3.

**METHODS (6 sentences)**

- `[2305.01937 | methods | caption | 3.1 Task Introduction]`
  > We also report the inter-annotator agreement (IAA) among three annotators using Krippendorff’s \alpha .

- `[2311.08516 | methods | table | 2.1.1 Human annotation]`
  > Krippendorff’s \alpha

- `[2403.04132 | methods | table | 5 Efficient Approximate Ranking]`
  > \mathbb{P}(s(\mathbb{P})\in\mathcal{C})\geq 1-\alpha,

- `[2403.04132 | methods | prose | 5 Efficient Approximate Ranking]`
  > The uniform validity of \mathcal{C} directly implies that \mathbb{P}(\exists m:R_{m}>\rank(\mathbb{P})_{m})\leq\alpha —i.e., with high probability, no model’s performance is understated.

- `[2403.04132 | methods | prose | 5 Efficient Approximate Ranking]`
  > In other words, we construct the interval \{\xi:T\left\|\hat{V}^{-1/2}(\hat{\xi}-\xi)\right\|\leq\chi^{2}_{1-\alpha,M-1} , where \hat{\xi} is our MLE of the BT coefficients and \hat{V}_{\xi} is the sandwich variance of the logistic regression.

- `[2403.04132 | methods | prose | 5.1 Detecting Anomalous Users]`
  > At 5 randomly chosen values of j between 1 and 100, we identify a user as anomalous if M_{j}\geq\chi^{2}_{2j,1-\alpha/5} .

**APPENDIX (9 sentences)**

- `[2303.17651 | appendix | prose | Appendix J Statistical Confidence Intervals]`
  > Table 13 shows results from Table 1 with Wilson confidence interval Brown et al. (2001) (at \alpha = 99% confidence interval) and statistical significance.

- `[2405.01535 | appendix | prose | Appendix G Merging Method Ablation]`
  > Specifically, this is conducted by normalizing {\theta}_{d} and {\theta}_{p} into unit length and then merging the two weights based on the coefficient \alpha such as: {\theta}_{final}=\alpha\times\frac{{\theta}_{d}}{||{\theta}_{d}||}+(1-\alpha)\times\frac{{\theta}_{p}}{||{\theta}_{p}||} (4)

- `[2405.01535 | appendix | prose | Appendix G Merging Method Ablation]`
  > Specifically, this is conducted by normalizing {\theta}_{d} and {\theta}_{p} into unit length and then merging the two weights based on the coefficient \alpha such as:

- `[2405.01535 | appendix | table | Appendix G Merging Method Ablation]`
  > {\theta}_{final}=\alpha\times\frac{{\theta}_{d}}{||{\theta}_{d}||}+(1-\alpha)\times\frac{{\theta}_{p}}{||{\theta}_{p}||}

- `[2405.01535 | appendix | prose | Appendix G Merging Method Ablation]`
  > • Task Arithmetic merging (Ilharco et al., 2022) which can be expressed as follows: \displaystyle{\theta}_{final}={\theta}_{init}+\alpha\times({\theta}_{d}-{\theta}_{init})+ (5) \displaystyle(1-\alpha)\times({\theta}_{p}-{\theta}_{init}) where {\theta}_{init} is the weight of the base model.

- `[2405.01535 | appendix | table | Appendix G Merging Method Ablation]`
  > \displaystyle{\theta}_{final}={\theta}_{init}+\alpha\times({\theta}_{d}-{\theta}_{init})+

- `[2405.01535 | appendix | table | Appendix G Merging Method Ablation]`
  > \displaystyle(1-\alpha)\times({\theta}_{p}-{\theta}_{init})

- `[2406.18403 | appendix | prose | Appendix A Datasets]`
  > Table 3 reports Krippendorf’s \alpha for those datasets with multiple public human annotations.

- `[2406.18403 | appendix | table | Appendix A Datasets]`
  > Krippendorf’s \alpha

**OTHER (2 sentences)**

- `[2405.01535 | other | table | 3.4 Training Methods & Baselines]`
  > {\theta}_{final}=\alpha\times{\theta}_{d}+(1-\alpha)\times{\theta}_{p}

- `[2405.01535 | other | table | Limitations]`
  > Linear ( \alpha=0.5 )



### 5.8 p-values

**RESULTS (20 sentences)**

- `[2212.09746 | results | caption | 3.6 Metaphor Generation]`
  > These metrics were not found to exhibit any statistically significant differences using a Tukey-Kramer test at the p=0.05 level.

- `[2212.09746 | results | footnote | 3.2 Social Dialogue]`
  > 55 5 Results are denoted by * if models had a significant effect relative to TextDavinci, * if significant relative to TextBabbage, * if significant relative to Davinci, and * if significant relative to Jumbo at the p=0.05 level using a Tukey-Kramer test.

- `[2303.03199 | results | prose | 7. Results]`
  > We report significance at p < 0.05.

- `[2303.03199 | results | table | 7. Results]`
  > s_{1} ( \beta =-1.26, SE=0.11, CI95%=[-1.48, -1.03], p<.0001)

- `[2303.03199 | results | table | 7. Results]`
  > Number * Instruction ( \beta =0.72, SE=0.17, CI95%=[0.39, 1.05], p<.0001)

- `[2303.03199 | results | table | 7. Results]`
  > s_{3} ( \beta =24.59, SE=9.5, CI95%=[5.96, 43.22], p<.01)

- `[2303.03199 | results | table | 7. Results]`
  > s_{1} ( \beta =-0.08, SE=0.01, CI95%=[-0.10, -0.06], p<.0001); i_{yes} ( \beta =-0.06, SE=0.01, CI95%=[-0.09, -0.04], p<.0001)

- `[2303.03199 | results | table | 7. Results]`
  > s_{3} ( \beta =0.05, SE=0.01, CI95%=[0.03, 0.07], p<.0001)

- `[2303.03199 | results | table | 7. Results]`
  > s_{1} ( \beta =-0.03, SE=0.01, CI95%=[-0.05, -0.01], p<.005); i_{yes} ( \beta =-0.05, SE=0.01, CI95%=[-0.07, -0.03], p<.0001)

- `[2303.03199 | results | table | 7. Results]`
  > s_{1} ( \beta =-0.83, SE=0.13, CI95%=[-1.08, -0.57], p<.0001); i_{yes} ( \beta =-0.32, SE=0.14, CI95%=[-0.59, -0.05], p=0.018)

- `[2303.03199 | results | table | 7. Results]`
  > s_{1} ( \beta =1.55, SE=0.78, CI95%=[0.01, 3.08], p=0.049)

- `[2303.03199 | results | table | 7. Results]`
  > s_{1} ( \beta =-0.37, SE=0.14, CI95%=[-0.65, -0.09], p=0.010)

- `[2303.03199 | results | prose | 7.5.1. Perceived Differences for Number of S]`
  > The GEE model estimates that the odds of giving a higher rating with a single suggestion were “ x ” times the odds of that with the list of three suggestions, with x as follows: Single suggestions were rated as significantly more distracting ( x =1.95, p<0.005), less helpful ( x =0.60, p=0.02), leading to more manual editing ( x =1.91, p<0.005), feeling less in control ( x =0.67, p=0.03), and providing less diverse suggestions ( x =0.67, p=0.04).

- `[2303.03199 | results | prose | 7.5.2. Perceived Differences for Instruction]`
  > We found a tradeoff in the perception of instructions: On the negative side, the UIs that allowed users to enter instructions to the AI received ratings of manually editing suggestions significantly more ( x =1.54, p=0.02) and being significantly more distracting ( x =2.03, p<0.0005).

- `[2303.03199 | results | prose | 7.5.2. Perceived Differences for Instruction]`
  > On the positive side, giving instructions was rated significantly better on being able to influence the suggested text ( x =1.92, p<0.001).

- `[2303.03199 | results | prose | 7.5.2. Perceived Differences for Instruction]`
  > Descriptively, it was also rated better on feeling in control of the suggested text (see Q_{10} in Figure 3), although this was not significant ( x =1.42, p=0.058).

- `[2305.01937 | results | prose | 3.3 Experiment Results]`
  > However, the rating differences between the human-written and model-generated stories do not achieve statistical significance for grammaticality and relevance; the p-value obtained by Welch’s t-test is much larger than 0.05 .

- `[2309.12570 | results | footnote | 5.2. Identifying Patterns in User Interactio]`
  > 1313 13 This result is significant at the 5\% level with a p-value for the correlation of 0.04 .

- `[2410.16184 | results | prose | 5.2 Downstream Task Correlation]`
  > The Pearson correlation coefficient is 0.55 ( p=0.07 ), indicating a moderate positive correlation trending toward significance.

- `[2410.16184 | results | prose | 5.2 Downstream Task Correlation]`
  > In comparison, RewardBench (Lambert et al., 2024) reports a Pearson correlation of r=0.21 ( p=0.51 ) (see Section F in the appendix).

**METHODS (7 sentences)**

- `[2305.01937 | methods | prose | 3.1 Task Introduction]`
  > After the model is trained, we randomly select 200 prompts from the testing set of WritingPrompts and make the fine-tuned GPT-2 generate stories based on those prompts using nucleus sampling (Holtzman et al., 2020) with p=0.9 .

- `[2305.01937 | methods | prose | 3.2 LLM Evaluation and Human Evaluation]`
  > We use nucleus sampling with p=0.9 to generate the answer from T0 and InstructGPTs.

- `[2403.04132 | methods | prose | 5.1 Detecting Anomalous Users]`
  > Under the null hypothesis that \mathcal{H}_{A^{\prime}_{i}} is exchangeable with H^{\prime}_{i} , p_{i} is a valid p-value (see Appendix C for a proof).

- `[2403.04132 | methods | prose | 5.1 Detecting Anomalous Users]`
  > Furthermore, the dependence of these p-values asymptotically is negligible.

- `[2403.04132 | methods | prose | 5.1 Detecting Anomalous Users]`
  > With this p-value in hand, we can test against this null hypothesis sequentially by using Fisher’s combination test (Fisher, 1928) along with a variant of the Bonferroni correction.

- `[2403.04132 | methods | prose | 5.1 Detecting Anomalous Users]`
  > (The times are randomly chosen, as to avoid anomalous users strategizing to hack this p-value.) Despite the heuristic application of this procedure, it seems to work well in our small-scale tests reported in Table 5.

- `[2406.18403 | methods | caption | 2 Construction of Judge-Bench]`
  > Spearman’s correlations are generally significant ( p<0.05 ), with the exception of the Persona Chat and Topical Chat datasets (see Tab. 6 in Appendix H for more details).

**APPENDIX (6 sentences)**

- `[2212.09746 | appendix | caption | D.2 Social Dialogue]`
  > Metrics are denoted by \ddagger if models had a significant effect relative to Davinci, at the Bonferroni-corrected significance level of p=.0125 .

- `[2212.09746 | appendix | caption | D.6 Metaphor Generation]`
  > Metrics are denoted by \ddagger if models had a significant effect with a Bonferroni correction, p=0.0125 (see Appendix D.6 for details).

- `[2305.01937 | appendix | prose | B.3 Data Post-processing]`
  > When generating the stories, we adopt nucleus sampling with p=0.9 .

- `[2403.04132 | appendix | prose | Appendix C Valid P-Value]`
  > Consider the p-value

- `[2403.04132 | appendix | prose | Appendix C Valid P-Value]`
  > We will prove that this p-value is valid, i.e., that \mathbb{P}(p_{i}\leq t)\leq t , under the null hypothesis that the vector \mathcal{H}^{\prime}=(H_{t}:A_{t}=A^{\prime}_{i})\|(H^{\prime}_{i}) is exchangeable, where \| denotes the concatenation operator.

- `[2406.18403 | appendix | caption | Appendix H Additional Results]`
  > For Spearman’s correlations, we report the number of significant correlations ( p<0.05 ) for each model and dataset in brackets.



### 5.9 "statistically significant" and significance conventions

**RESULTS (14 sentences)**

- `[2201.06796 | results | prose | 5.1.3. Collaboration Capabilities: Ability t]`
  > Writing sessions with GPT-3 with high randomness received slightly higher equality and mutuality scores in argumentative writing, while the difference was not statistically significant in creative writing.

- `[2212.09746 | results | prose | 3.1.2 Perspectives: Third-party vs. First-pe]`
  > However, assistance from TextDavinci led to statistically significantly higher crossword letter accuracy only for one of the five crossword puzzles; with another puzzle, users actually performed worse with both instruction-tuned models (TextDavinci and TextBabbage).

- `[2212.09746 | results | caption | 3.2 Social Dialogue]`
  > The means, standard errors, and statistical significance are shown in the table.

- `[2212.09746 | results | caption | 3.3 Question Answering]`
  > The numbers indicate means and standard errors, and the markers denote statistical significance,5 conditioning on the use of AI assistance; when the assistance was provided, users queried the system 86% of the time.

- `[2212.09746 | results | caption | 3.4 Crossword Puzzles]`
  > The numbers indicate means and standard errors, and the markers denote statistical significance.5

- `[2212.09746 | results | prose | 3.4 Crossword Puzzles]`
  > Interestingly, this perception of helpfulness is not necessarily reflected in the overall interaction accuracy: as shown in Figure 8, assistance from TextDavinci led to statistically significantly higher crossword letter accuracy only for the SIT crossword puzzle; for the NYT-1 puzzle, users actually performed worse with both instruction tuned models (TextDavinci and TextBabbage).

- `[2212.09746 | results | caption | 3.6 Metaphor Generation]`
  > The numbers indicate means and standard errors (for writing one metaphorical sentence), and the markers denote statistical significance.5

- `[2212.09746 | results | caption | 3.6 Metaphor Generation]`
  > For these outcomes, no results were found to have statistical significance using a Tukey-Kramer test.

- `[2212.09746 | results | caption | 3.6 Metaphor Generation]`
  > These metrics were not found to exhibit any statistically significant differences using a Tukey-Kramer test at the p=0.05 level.

- `[2303.03199 | results | prose | 7. Results]`
  > We report significance at p < 0.05.

- `[2305.01937 | results | prose | 3.3 Experiment Results]`
  > However, the rating differences between the human-written and model-generated stories do not achieve statistical significance for grammaticality and relevance; the p-value obtained by Welch’s t-test is much larger than 0.05 .

- `[2305.01937 | results | prose | 3.3 Experiment Results]`
  > By Welch’s t-test, we find that the higher ratings on human-written stories are all statistically significant.

- `[2305.01937 | results | prose | 3.3 Experiment Results]`
  > ChatGPT rates like human experts and can explain its own decision well: ChatGPT also shows a clear preference for human-written stories, and the preference toward human written-stories is statistically significant.

- `[2309.12570 | results | footnote | 5.2. Identifying Patterns in User Interactio]`
  > 1313 13 This result is significant at the 5\% level with a p-value for the correlation of 0.04 .

**APPENDIX (10 sentences)**

- `[2206.05802 | appendix | prose | E.1 Assistance for comparisons]`
  > Using ensembles of 5 humans as ground truth, we observed statistically significant improvements when using human-written critiques as assistance.

- `[2212.09746 | appendix | prose | B.2 Question Answering]`
  > In addition to replicating the finding of Bowman et al. (2022) that human-LM interaction generally outperforms a human or LM alone, we are able to observe statistically significant patterns in the relative performance of human interactions with different LM’s.

- `[2212.09746 | appendix | caption | D.2 Social Dialogue]`
  > Metrics are denoted by \ddagger if models had a significant effect relative to Davinci, at the Bonferroni-corrected significance level of p=.0125 .

- `[2212.09746 | appendix | caption | D.3 Question Answering]`
  > However, there was also statistically significant higher accuracy in some groups over others, suggesting sample bias.

- `[2212.09746 | appendix | prose | D.6 Metaphor Generation]`
  > The direction of the results were comparable to the main paper, however no statistically significant relationships were found in the linear analysis besides the differences in acceptance and edit distance.

- `[2303.17651 | appendix | caption | Appendix J Statistical Confidence Intervals]`
  > Table 13: Self-Refine results from table 1 with Wilson confidence interval (at 95% confidence interval) and statistical significance.

- `[2303.17651 | appendix | caption | Appendix J Statistical Confidence Intervals]`
  > Gains over Base, that are statistically significant based on these confidence intervals are marked *

- `[2303.17651 | appendix | prose | Appendix J Statistical Confidence Intervals]`
  > Table 13 shows results from Table 1 with Wilson confidence interval Brown et al. (2001) (at \alpha = 99% confidence interval) and statistical significance.

- `[2303.17651 | appendix | prose | Appendix J Statistical Confidence Intervals]`
  > Gains that are statistical significance based on these confidence intervals are marked with an asterisk.

- `[2303.17651 | appendix | prose | Appendix J Statistical Confidence Intervals]`
  > We find that nearly all of GPT-4 gains are statistically significant, ChatGPT gains are significant for 4 out of 7 datasets, and GPT-3.5 gains are significant for 3 out of 7 datasets.

**OTHER (1 sentences)**

- `[2310.01798 | other | prose | 1 Introduction]`
  > However, concerns about their accuracy, reasoning capabilities, and the safety of their generated content have drawn significant attention from the community (Bang et al., 2023; Alkaissi & McFarlane, 2023; Zheng et al., 2023; Shi et al., 2023; Carlini et al., 2021; Huang et al., 2022; Shao et al., 2023; Li et al., 2023; Wei et al., 2023; Zhou et al., 2023b; Zou et al., 2023, inter alia).



### 5.10 t-test

**RESULTS (2 sentences)**

- `[2305.01937 | results | prose | 3.3 Experiment Results]`
  > However, the rating differences between the human-written and model-generated stories do not achieve statistical significance for grammaticality and relevance; the p-value obtained by Welch’s t-test is much larger than 0.05 .

- `[2305.01937 | results | prose | 3.3 Experiment Results]`
  > By Welch’s t-test, we find that the higher ratings on human-written stories are all statistically significant.



### 5.11 chi-squared

**RESULTS (2 sentences)**

- `[2403.04132 | results | caption | 7.1 Ranking system]`
  > The multiplicity correction, in this case a chi-square CLT interval, is technically required for the purpose of calculating the ranking, because it ensures all scores are simultaneously contained in their intervals (and the ranking is a function of all the scores).

- `[2403.04132 | results | prose | 7.2 Anomalous Users Detection]`
  > As mentioned in Section 5.1, per user we compute five M_{j} and identify the user as anomalous if M_{j}\geq\chi^{2}_{2j,1-\alpha/5} .

**METHODS (3 sentences)**

- `[2403.04132 | methods | prose | 5 Efficient Approximate Ranking]`
  > To get the uniform confidence set, we construct the chi-squared interval implied by the central limit theorem using the sandwich estimate of the variance.

- `[2403.04132 | methods | prose | 5 Efficient Approximate Ranking]`
  > In other words, we construct the interval \{\xi:T\left\|\hat{V}^{-1/2}(\hat{\xi}-\xi)\right\|\leq\chi^{2}_{1-\alpha,M-1} , where \hat{\xi} is our MLE of the BT coefficients and \hat{V}_{\xi} is the sandwich variance of the logistic regression.

- `[2403.04132 | methods | prose | 5.1 Detecting Anomalous Users]`
  > At 5 randomly chosen values of j between 1 and 100, we identify a user as anomalous if M_{j}\geq\chi^{2}_{2j,1-\alpha/5} .



### 5.12 "effect size"

**RESULTS (3 sentences)**

- `[2310.13548 | results | prose | 3.3 AI Assistants Can Give Biased Answers]`
  > We find consistent trends across all of the assistants (e.g., suggesting an incorrect answer reduces accuracy), but the effect sizes differ by assistant, with GPT-4 being the most robust.

- `[2310.13548 | results | prose | 4.1 What Behavior Is Incentivized By Human P]`
  > where \alpha_{i}\in\mathbb{R}^{N_{f}} are the effect sizes for each feature, \phi_{i}\in\{-1,0,+1\}^{N_{f}} is the feature vector for each preference comparison, \sigma(\cdot) is the logisitic function, P is the prompt, R_{A} is response A, and R_{B} is response B.

- `[2310.13548 | results | prose | 4.1 What Behavior Is Incentivized By Human P]`
  > We place a Laplace prior over the effect sizes \alpha_{i} with zero mean and scale b=0.01 , which was chosen using a holdout set.

**APPENDIX (10 sentences)**

- `[2310.13548 | appendix | prose | Appendix B Further details and results for §]`
  > We report the effect sizes based on the entire dataset.

- `[2310.13548 | appendix | prose | Appendix B Further details and results for §]`
  > In Fig. 18, we show the posterior correlations of the effect sizes for different features.

- `[2310.13548 | appendix | prose | Appendix B Further details and results for §]`
  > This indicates the individual effect sizes of these features may be unreliable.

- `[2310.13548 | appendix | prose | Appendix B Further details and results for §]`
  > The correlations between the other effect sizes are generally weak (less than 0.3), which suggests that we have sufficient data to determine the effects of individual features.

- `[2310.13548 | appendix | caption | Appendix B Further details and results for §]`
  > Figure 18: Correlations between the posterior effect sizes for different features for §4.1.

- `[2310.13548 | appendix | caption | Appendix B Further details and results for §]`
  > Although we observe some negative correlations in the posterior, we find the the correlations between the effect sizes are generally weak (less than 0.3), which suggests that we have sufficient data to determine the effects of individual features.

- `[2310.13548 | appendix | caption | Appendix B Further details and results for §]`
  > We recalculate the posterior effect sizes for six different data splits, where in each split we exclude 1/6 of the training data.

- `[2310.13548 | appendix | caption | Appendix B Further details and results for §]`
  > If features are highly correlated, their effect sizes would be unreliable and would have large fluctuations depending on the included data.

- `[2310.13548 | appendix | caption | Appendix B Further details and results for §]`
  > We recalculate the posterior effect sizes when a previously observed feature is now unobserved.

- `[2310.13548 | appendix | caption | Appendix B Further details and results for §]`
  > Although the effect sizes of individual features do vary when excluding previously unobserved features, we find consistent trends in the effects of each feature.



### 5.13 Regression models

**RESULTS (5 sentences)**

- `[2303.03199 | results | prose | 7. Results]`
  > For statistical testing we use R (R Core Team, 2020), concretely, (generalised) linear mixed-effects models (LMMs with the packages lme4 (Bates et al., 2015), lmerTest (Kuznetsova et al., 2017)).

- `[2310.13548 | results | prose | 4.1 What Behavior Is Incentivized By Human P]`
  > Our overall approach is to convert human preference comparisons (i.e., “for prompt P, response A is preferable to response B”) into interpretable features e.g., “response A is more truthful and less empathetic than response B.” We then use a Bayesian logistic regression model to map these features to human preferences, thereby allowing us to understand what the human preference data incentivizes in aggregate.

- `[2310.13548 | results | prose | 4.1 What Behavior Is Incentivized By Human P]`
  > Model We use Bayesian logistic regression to predict human preferences from these features:

- `[2310.13548 | results | prose | 4.1 What Behavior Is Incentivized By Human P]`
  > We find our logistic regression model achieves a holdout accuracy of 71.3%, comparable to a 52-billion parameter preference model trained on the same data (Bai et al., 2022a, \sim 72%;).

- `[2310.13548 | results | prose | 4.2 What Behavior Is Incentivized By Models ]`
  > Results We find optimizing model responses using the Claude 2 PM has mixed effects on sycophancy (Fig. 6).

**METHODS (5 sentences)**

- `[2403.04132 | methods | prose | 4 From Pairwise Comparisons to Rankings]`
  > A standard score function in this setting is the vector of Bradley-Terry (BT) coefficients (Bradley & Terry, 1952).

- `[2403.04132 | methods | prose | 4 From Pairwise Comparisons to Rankings]`
  > In the Bradley-Terry model, H_{t}\in\{0,1\} , and the probability model m beats model m^{\prime} is modeled via a logistic relationship:

- `[2403.04132 | methods | prose | 4 From Pairwise Comparisons to Rankings]`
  > Our goal is to estimate the population Bradley-Terry coefficients, i.e., those that minimize the binary cross-entropy:

- `[2403.04132 | methods | prose | 4 From Pairwise Comparisons to Rankings]`
  > Although the BT model technically assumes a parametric form for the model win rates, the seminal results of Huber et al. (1967); White (1982) show that maximum likelihood estimators are still asymptotically normal even when these assumptions do not hold, so long as the so-called “sandwich” covariance matrix is used; see Section 5 for details, and see Appendix B for a nonparametric extension of the Bradley-Terry model.

- `[2403.04132 | methods | prose | 5 Efficient Approximate Ranking]`
  > In other words, we construct the interval \{\xi:T\left\|\hat{V}^{-1/2}(\hat{\xi}-\xi)\right\|\leq\chi^{2}_{1-\alpha,M-1} , where \hat{\xi} is our MLE of the BT coefficients and \hat{V}_{\xi} is the sandwich variance of the logistic regression.

**APPENDIX (18 sentences)**

- `[2212.09746 | appendix | prose | D.1 Methods for statistical analysis]`
  > We ran linear regression models on all of the models against the different survey metrics using the stats package in R, which fits a linear regression against continuous variables using an ordinary least squares method R Core Team (2020).

- `[2212.09746 | appendix | prose | D.1 Methods for statistical analysis]`
  > We checked the assumptions of the regressions held through manual verification of the residuals and Q-Q plots, and we compared the results of our experiments with the linear regression and validated relationships.

- `[2212.09746 | appendix | prose | D.2 Social Dialogue]`
  > The linear regression analysis confirms the results.

- `[2212.09746 | appendix | prose | D.2 Social Dialogue]`
  > Additionally, this specific experiment could be well suited for a mixed effects analysis and could stand to benefit from further question refinement with the help of user feedback.

- `[2212.09746 | appendix | prose | D.4 Crossword Puzzle]`
  > The linear regression results are in Table 14.

- `[2212.09746 | appendix | prose | D.4 Crossword Puzzle]`
  > The added linear regression analysis here demonstrates that, when controlling for error, TextDavinci has the best performance metrics to a significant degree above the other models.

- `[2212.09746 | appendix | prose | D.4 Crossword Puzzle]`
  > Upon verifying the linear regression assumptions, the residual and Q-Q plots indicate that there were certain influential outliers that might be responsible for this lack of clarity.

- `[2212.09746 | appendix | caption | D.5 Text Summarization]`
  > The results were derived using the same ordinary least squares method and linear regression as described previously for the continuous variables (elapsed time, distance, improvement, edit).

- `[2212.09746 | appendix | prose | D.5 Text Summarization]`
  > A linear regression analysis of the summarization task was used to calculate the means and significance for the variables (elapsed time, edit distance, improvement, edit, helpfulness, original consistency, original coherency, original relevance, edited consistency, edited coherency, and edited relevance).

- `[2212.09746 | appendix | prose | D.5 Text Summarization]`
  > The linear regression confirmed this and additionally highlighted the lack of distinction between the bad performers TextBabbage and Jumbo.

- `[2310.13548 | appendix | prose | Appendix B Further details and results for §]`
  > The main results shown in Fig. 5 show the probability that a response comparison with one feature set to +1 and all other features set to 0 is preferred by the Bayesian logistic regression model.

- `[2403.04132 | appendix | prose | Appendix B The Nonparametric Bradley-Terry M]`
  > Nonparametric Bradley-Terry.

- `[2403.04132 | appendix | prose | Appendix B The Nonparametric Bradley-Terry M]`
  > We next consider a nonparametric extension of the Bradley-Terry (BT) model (Bradley & Terry, 1952) to the case where the ranking is not necessarily transitive.

- `[2403.04132 | appendix | prose | Appendix B The Nonparametric Bradley-Terry M]`
  > How is the BT score related to the original Bradley-Terry model?

- `[2403.04132 | appendix | prose | Appendix B The Nonparametric Bradley-Terry M]`
  > In the original Bradley-Terry model, H_{t}\in\{0,1\} , and the probability of model m beating model m^{\prime} is assumed to be given by

- `[2403.04132 | appendix | prose | Appendix B The Nonparametric Bradley-Terry M]`
  > for some unknown parameters \xi_{1},\ldots,\xi_{M} —the Bradley-Terry coefficients.

- `[2403.04132 | appendix | prose | Appendix B The Nonparametric Bradley-Terry M]`
  > The basic goal of the Bradley-Terry model is to estimate these parameters from the observed outcomes.

- `[2403.04132 | appendix | prose | Appendix B The Nonparametric Bradley-Terry M]`
  > Thus, if the parametric BT model is well-specified, the nonparametric version will exactly recover the Bradley-Terry coefficients.

**OTHER (2 sentences)**

- `[2310.13548 | other | prose | 1 Introduction]`
  > To understand what behavior is incentivized by the data, we predict human preference judgments using these features with Bayesian logistic regression.

- `[2403.04132 | other | prose | (front matter)]`
  > B The Nonparametric Bradley-Terry Model



### 5.14 Standard errors

**RESULTS (11 sentences)**

- `[2201.06796 | results | caption | 5.1.1. Language Capabilities: Ability to Gen]`
  > The text written by writers had more spelling and grammar errors compared to \gpt-generated sentences, with a reasonably large drop from 0.037 to 0.033 with the standard error of measurement of 0.001.

- `[2201.06796 | results | caption | 5.1.1. Language Capabilities: Ability to Gen]`
  > The text written by both had contained most diverse vocabulary, with a reasonably large jump from 0.884 (writer) and 0.876 (\gpt) to 0.923 (both) with the standard error of measurement of 0.001.

- `[2201.06796 | results | prose | 5.1.1. Language Capabilities: Ability to Gen]`
  > Overall, the number of errors per word (averaged across all sentences in creative and argumentative writing) was 0.037\pm 0.001 for writers, 0.033\pm 0.001 for GPT-3, and 0.032\pm 0.001 for both (the number next to the average indicates the standard error of measurement).

- `[2212.09746 | results | caption | 3.2 Social Dialogue]`
  > The means, standard errors, and statistical significance are shown in the table.

- `[2212.09746 | results | caption | 3.3 Question Answering]`
  > The numbers indicate means and standard errors, and the markers denote statistical significance,5 conditioning on the use of AI assistance; when the assistance was provided, users queried the system 86% of the time.

- `[2212.09746 | results | caption | 3.4 Crossword Puzzles]`
  > The numbers indicate means and standard errors, and the markers denote statistical significance.5

- `[2212.09746 | results | caption | 3.6 Metaphor Generation]`
  > The numbers indicate means and standard errors (for writing one metaphorical sentence), and the markers denote statistical significance.5

- `[2212.09746 | results | caption | 3.6 Metaphor Generation]`
  > The numbers indicate means and standard errors.

- `[2310.13548 | results | caption | 3.1 AI Assistants Can Give Biased Feedback]`
  > Mean and standard error across domains shown.

- `[2310.13548 | results | caption | 3.2 AI Assistants Can Be Easily Swayed]`
  > Mean and standard error shown.

- `[2310.13548 | results | caption | 3.3 AI Assistants Can Give Biased Answers]`
  > We use free-form variants of TruthfulQA and TriviaQA, and show the mean baseline accuracy alongside mean change in accuracy and standard error.

**METHODS (1 sentences)**

- `[2403.04132 | methods | prose | 5 Efficient Approximate Ranking]`
  > To compute confidence intervals on the BT coefficients, we employ two strategies: (1) the pivot bootstrap (DiCiccio & Efron, 1996), and (2) the “sandwich” robust standard errors outlined in Huber et al. (1967) (see also Freedman (2006) for an outline of the necessary technical assumptions).

**APPENDIX (3 sentences)**

- `[2212.09746 | appendix | prose | D.1 Methods for statistical analysis]`
  > For the main results presented in the paper, we computed group-wise means and standard errors and used the modified Tukey-Kramer post-hoc test to account for unequal group sizes.

- `[2212.09746 | appendix | caption | D.2 Social Dialogue]`
  > The numbers indicate averages and standard errors.

- `[2212.09746 | appendix | caption | D.6 Metaphor Generation]`
  > The numbers indicate means and standard errors.The results are derived from linearly regressing the model types against the metrics using an ordinary least squares method, and the resulting values are the means of the metrics for each model type.

**OTHER (1 sentences)**

- `[2206.05802 | other | table | 1.1 Motivation]`
  > Note: Throughout the paper, all error bars shown either use bootstrapping at the passage level or simply calculate standard error of the mean (when appropriate), and represent z=1 (i.e. one standard deviation on each side).



### 5.15 Confidence intervals

**RESULTS (1 sentences)**

- `[2403.04132 | results | prose | 7.1 Ranking system]`
  > For this experiment, we ran a replay of T=213,576 historical votes from our online platform and calculate the BT coefficients using our earlier-described estimation algorithm with confidence intervals; see Figure 5 for these intervals (with and without multiplicity correction; the formal notion of approximate ranking technically requires multiplicity correction, but it makes the intervals looser).

**METHODS (3 sentences)**

- `[2403.04132 | methods | prose | 5 Efficient Approximate Ranking]`
  > and we construct confidence intervals accordingly.

- `[2403.04132 | methods | prose | 5 Efficient Approximate Ranking]`
  > To compute confidence intervals on the BT coefficients, we employ two strategies: (1) the pivot bootstrap (DiCiccio & Efron, 1996), and (2) the “sandwich” robust standard errors outlined in Huber et al. (1967) (see also Freedman (2006) for an outline of the necessary technical assumptions).

- `[2403.04132 | methods | prose | 5 Efficient Approximate Ranking]`
  > Our sampling rule was to choose the model pair a\in\mathcal{A} proportionally to the reduction in confidence interval size by sampling that pair:

**APPENDIX (8 sentences)**

- `[2212.09746 | appendix | prose | D.4 Crossword Puzzle]`
  > Additionally, although this analysis yields similar patterns of results for the worst performers, the overlapping confidence intervals and lack of significant differences between Jumbo and Davinci indicate that there is less clarity around the worst performer when using a technique that accounts for error and assumes normally distributed residuals.

- `[2212.09746 | appendix | prose | D.6 Metaphor Generation]`
  > However, the results do not conclusively reveal which ones performed better or worse (confirmed by the overlapping confidence intervals) on most metrics.

- `[2303.17651 | appendix | caption | Appendix J Statistical Confidence Intervals]`
  > Table 13: Self-Refine results from table 1 with Wilson confidence interval (at 95% confidence interval) and statistical significance.

- `[2303.17651 | appendix | caption | Appendix J Statistical Confidence Intervals]`
  > Gains over Base, that are statistically significant based on these confidence intervals are marked *

- `[2303.17651 | appendix | prose | Appendix J Statistical Confidence Intervals]`
  > Table 13 shows results from Table 1 with Wilson confidence interval Brown et al. (2001) (at \alpha = 99% confidence interval) and statistical significance.

- `[2303.17651 | appendix | prose | Appendix J Statistical Confidence Intervals]`
  > Gains that are statistical significance based on these confidence intervals are marked with an asterisk.

- `[2403.04132 | appendix | prose | Appendix A Confidence Interval Simulation St]`
  > We conduct a simulation study to evaluate the bootstrap confidence intervals versus the sandwich estimator.

- `[2406.12624 | appendix | prose | Appendix A Limitations]`
  > This sample size also allowed us to conduct manual annotations and error analysis within 75 human hours/200 GPU hours (see Appendix H) and give reliable confidence intervals while also providing the flexibility to compare a range of models.

**OTHER (1 sentences)**

- `[2404.12272 | other | prose | 8.2. Operationalizing Assertions]`
  > One could imagine interfaces similar to creating a “pull request” for a new assertion and soliciting review from a team member, and a workflow similar to continuous integration/continuous deployment (CI/CD) that seamlessly pushes new assertions to production.



### 5.16 Multiple-comparison correction

**METHODS (1 sentences)**

- `[2403.04132 | methods | prose | 5.1 Detecting Anomalous Users]`
  > With this p-value in hand, we can test against this null hypothesis sequentially by using Fisher’s combination test (Fisher, 1928) along with a variant of the Bonferroni correction.

**APPENDIX (5 sentences)**

- `[2212.09746 | appendix | prose | D.1 Methods for statistical analysis]`
  > Significance was assessed at the Bonferroni-corrected level Bland & Altman (1995).

- `[2212.09746 | appendix | caption | D.2 Social Dialogue]`
  > Metrics are denoted by \ddagger if models had a significant effect relative to Davinci, at the Bonferroni-corrected significance level of p=.0125 .

- `[2212.09746 | appendix | caption | D.3 Question Answering]`
  > Metrics are denoted by \ddagger if models had a significant effect with a Bonferroni correction (see Appendix D.3 for details).

- `[2212.09746 | appendix | caption | D.5 Text Summarization]`
  > Metrics are denoted by \ddagger if models had a significant effect with a Bonferroni correction (see Appendix D.5 for details).

- `[2212.09746 | appendix | caption | D.6 Metaphor Generation]`
  > Metrics are denoted by \ddagger if models had a significant effect with a Bonferroni correction, p=0.0125 (see Appendix D.6 for details).



### 5.17 Bootstrap

**RESULTS (1 sentences)**

- `[2206.05802 | results | prose | 3.3 Findings]`
  > Note that our critique model was trained on data from the same pool of labelers—we are essentially leveraging our models to bootstrap our labelers to be more careful at the base task.

**METHODS (3 sentences)**

- `[2403.04132 | methods | prose | 5 Efficient Approximate Ranking]`
  > To compute confidence intervals on the BT coefficients, we employ two strategies: (1) the pivot bootstrap (DiCiccio & Efron, 1996), and (2) the “sandwich” robust standard errors outlined in Huber et al. (1967) (see also Freedman (2006) for an outline of the necessary technical assumptions).

- `[2406.18403 | methods | prose | 3 Model Selection and Experiment Design]`
  > • When multiple individual human judgments are available (typically three, see Table 2 in Appendix A), we estimate an upper bound by computing the average Spearman’s \rho or Cohen’s \kappa between bootstrapped single-rater responses and the aggregated responses across raters.

- `[2406.18403 | methods | prose | 3 Model Selection and Experiment Design]`
  > When multiple individual human judgments are available (typically three, see Table 2 in Appendix A), we estimate an upper bound by computing the average Spearman’s \rho or Cohen’s \kappa between bootstrapped single-rater responses and the aggregated responses across raters.

**APPENDIX (6 sentences)**

- `[2403.04132 | appendix | prose | Appendix A Confidence Interval Simulation St]`
  > We conduct a simulation study to evaluate the bootstrap confidence intervals versus the sandwich estimator.

- `[2403.04132 | appendix | caption | Appendix A Confidence Interval Simulation St]`
  > Figure 13: Replay experiment showing the intervals, coverage, and average interval sizes of the bootstrap and of the sandwich intervals.

- `[2406.18403 | appendix | prose | Appendix C Upper Bound Estimation for Model ]`
  > We applied a similar logic to the human judgments used in the present study and combined it with a bootstrapping approach.

- `[2406.18403 | appendix | prose | Appendix C Upper Bound Estimation for Model ]`
  > For each annotated property, we bootstrapped single-participant responses by sampling 1000 times from the available human responses, excluding data points where a single annotation was available.

- `[2406.18403 | appendix | prose | Appendix C Upper Bound Estimation for Model ]`
  > Next, we computed the alignment between each of the bootstrapped-participant arrays and the array of aggregated responses.

- `[2406.18403 | appendix | prose | Appendix C Upper Bound Estimation for Model ]`
  > In cases where alignment between bootstrapped and aggregated responses could not be computed—because the variance of the bootstrapped responses was null—values were replaced with an average of the ‘non-nan’ correlations.

**OTHER (2 sentences)**

- `[2206.05802 | other | table | 1.1 Motivation]`
  > Note: Throughout the paper, all error bars shown either use bootstrapping at the passage level or simply calculate standard error of the mean (when appropriate), and represent z=1 (i.e. one standard deviation on each side).

- `[2406.12624 | other | prose | 3 Methodology]`
  > In Appendix I, we show with a bootstrapping test that this sample size has low variance for our main result.



### 5.18 sigma and standard deviation

**RESULTS (7 sentences)**

- `[2305.01937 | results | prose | 3.3 Experiment Results]`
  > We report the mean and standard deviation of the Likert scores obtained from LLM evaluation and human evaluation and show the inter-annotator agreement (IAA) using two different metrics: (1) the Krippendorff’s \alpha , and (2) the percentage of the stories where three evaluators give the exact same rating.

- `[2305.01937 | results | caption | 3.3.1 Does LLM and Human Evaluators Agree on]`
  > For each of the four attributes evaluated, the left column is the mean and standard deviation of human-written stories and the right column is those of GPT-2-generated stories.

- `[2310.13548 | results | table | 4.1 What Behavior Is Incentivized By Human P]`
  > \displaystyle p(R_{A}\text{ preferred to }R_{B}|\phi,\alpha,P)=\sigma\left(\textstyle\sum_{i=1}^{N_{f}}\alpha_{i}\phi_{i}\right),\quad\text{with }p(\alpha_{i})\sim\operatorname{\text{Laplace}}(\mu=0,b=0.01),

- `[2310.13548 | results | prose | 4.1 What Behavior Is Incentivized By Human P]`
  > where \alpha_{i}\in\mathbb{R}^{N_{f}} are the effect sizes for each feature, \phi_{i}\in\{-1,0,+1\}^{N_{f}} is the feature vector for each preference comparison, \sigma(\cdot) is the logisitic function, P is the prompt, R_{A} is response A, and R_{B} is response B.

- `[2406.12624 | results | prose | 4.2 Exploring consistent patterns in judge m]`
  > We show the rankings in Figure 3(a), with \rho and corresponding \sigma values in Appendix L.

- `[2406.12624 | results | prose | 4.2 Exploring consistent patterns in judge m]`
  > Specifically, both contains and Mistral 7B, with Scott’s \mathbf{\pi} values of 64 and 66, respectively, exhibit very high rank correlation with the human scores ( \rho 0.99 and 0.98, respectively, with \sigma 0.02 and 0.03).

- `[2410.16184 | results | prose | 5.2 Downstream Task Correlation]`
  > Reward model scores on RM-Bench are standardized using the mean and standard deviation of their performance.

**METHODS (3 sentences)**

- `[2305.01937 | methods | caption | 3.1 Task Introduction]`
  > For each evaluated attribute, we report its mean Likert scale and the standard deviation.

- `[2406.18403 | methods | table | 2 Construction of Judge-Bench]`
  > \sigma

- `[2406.18403 | methods | caption | 2 Construction of Judge-Bench]`
  > ‘ \sigma ’ denotes the standard deviation of the scores across models per dataset (averaged over properties if more than one is judged per dataset).

**APPENDIX (14 sentences)**

- `[2404.12272 | appendix | table | A.1. Assertion Selectivity and Impact on LLM]`
  > \displaystyle\displaystyle\sigma\left(e\right)=\sum_{f\in F}\text{selectivity}\left(f\right)\times f\left(e\right)

- `[2404.12272 | appendix | prose | A.1. Assertion Selectivity and Impact on LLM]`
  > The score \displaystyle\sigma is always non-negative.

- `[2404.12272 | appendix | prose | A.2. Sampling Grades]`
  > Given \displaystyle\sigma scores as previously defined, we consider a number of strategies to sample outputs for grading:

- `[2404.12272 | appendix | prose | A.2. Sampling Grades]`
  > • Highest: Sample the outputs with the highest \displaystyle\sigma .

- `[2404.12272 | appendix | prose | A.2. Sampling Grades]`
  > Highest: Sample the outputs with the highest \displaystyle\sigma .

- `[2404.12272 | appendix | prose | A.2. Sampling Grades]`
  > • Lowest: Sample the outputs with the lowest \displaystyle\sigma , prioritizing outputs that don’t fail any assertions or fail low-selectivity assertions.

- `[2404.12272 | appendix | prose | A.2. Sampling Grades]`
  > Lowest: Sample the outputs with the lowest \displaystyle\sigma , prioritizing outputs that don’t fail any assertions or fail low-selectivity assertions.

- `[2404.12272 | appendix | prose | A.2. Sampling Grades]`
  > • Alternating: Alternate between high and low \displaystyle\sigma , aiming for a diverse sample with both bad and good outputs.

- `[2404.12272 | appendix | prose | A.2. Sampling Grades]`
  > Alternating: Alternate between high and low \displaystyle\sigma , aiming for a diverse sample with both bad and good outputs.

- `[2404.12272 | appendix | prose | A.4. Evaluation of Sampling Policy]`
  > Initially, when users start grading outputs in EvalGen, they might effectively be grading random outputs for the first one or two outputs, as the \displaystyle\sigma scores update and stabilize.

- `[2406.12624 | appendix | prose | Appendix I Statistical reliability of Evalua]`
  > In this section, we further take 5 samples of 300 randomly selected questions from the evaluation set and calculate the mean and standard deviation of Scott’s Pi.

- `[2406.12624 | appendix | prose | Appendix L Exam-taker model ranking correlat]`
  > To validate these rankings, we randomly select 6 out of 9 exam-taker models across 5 samples, subsequently calculating the mean ( \rho ) and standard deviation ( \sigma ) of the rankings.

- `[2406.12624 | appendix | table | Appendix L Exam-taker model ranking correlat]`
  > \sigma

- `[2406.18403 | appendix | caption | Appendix H Additional Results]`
  > For datasets with more than one paraphrased prompt, we report the average and standard deviation across paraphrases.

**OTHER (3 sentences)**

- `[2206.05802 | other | table | 1.1 Motivation]`
  > Note: Throughout the paper, all error bars shown either use bootstrapping at the passage level or simply calculate standard error of the mean (when appropriate), and represent z=1 (i.e. one standard deviation on each side).

- `[2406.12624 | other | caption | 1 Introduction]`
  > Error bars annotate standard deviation across exam-taker models.

- `[2410.16184 | other | table | 2 Preliminaries]`
  > \mathcal{L}_{\text{pref}}=-\mathbb{E}_{(x,y_{c},y_{r})\sim\mathcal{D}_{\text{pref}}}\left[\log\sigma(R_{\psi}(x,y_{c})-R_{\psi}(x,y_{r}))\right]



### 5.19 Delta

**RESULTS (5 sentences)**

- `[2303.17651 | results | caption | 4 Analysis]`
  > Most gains( \Delta ) are in the initial iterations for both Code Opt.

- `[2311.08516 | results | caption | 4 Can LLMs correct reasoning mistakes in CoT]`
  > \Delta accuracy {}_{\text{✓}} refers to differences in accuracyans on the set of traces whose original answer was correctans; \Delta accuracy {}_{\text{✗}} for traces whose original answer was incorrectans.

- `[2311.08516 | results | caption | 5.1 Minimum mistake finding accuracy]`
  > Figure 3: \Delta accuracy {}_{\text{✓}} and \Delta accuracy {}_{\text{✗}} on each dataset as accuracyclf increases.

- `[2311.08516 | results | prose | 5.1 Minimum mistake finding accuracy]`
  > We can see that the losses in \Delta accuracy {}_{\text{✓}} begins to plateau at 65%.

- `[2311.08516 | results | prose | 5.1 Minimum mistake finding accuracy]`
  > In fact, for most tasks, \Delta accuracy {}_{\text{✓}} is already larger than \Delta accuracy {}_{\text{✗}} at around 60-70% accuracyRM.

**APPENDIX (3 sentences)**

- `[2405.01535 | appendix | table | Appendix D License]`
  > \Delta ( \downarrow )

- `[2405.01535 | appendix | caption | Appendix D License]`
  > Smaller \Delta values indicate that evaluator LMs can robustly evaluate across the two different formats.

- `[2405.01535 | appendix | table | Appendix E Consistency of Evaluator LMs]`
  > \Delta

**OTHER (4 sentences)**

- `[2311.08516 | other | prose | (front matter)]`
  > 4.1 Results \Delta accuracy {}_{\text{✓}} \Delta accuracy {}_{\text{✗}} 4.2 Discussion

- `[2311.08516 | other | prose | (front matter)]`
  > 4.1 Results \Delta accuracy {}_{\text{✓}} \Delta accuracy {}_{\text{✗}}

- `[2311.08516 | other | prose | (front matter)]`
  > \Delta accuracy {}_{\text{✓}}

- `[2311.08516 | other | prose | (front matter)]`
  > \Delta accuracy {}_{\text{✗}}



*Note on one catalogue entry:* the line quoted as `[2305.17926 | other | prose | 7 Conclusion]
Interrater reliability: the kappa statistic.` is the title of the McHugh (2012) reference,
which the parser placed in the trailing section because the bibliography follows the
conclusion. It is a citation title, not a claim by the authors.

---

## 6. Form: how the notation is written

### 6.1 Symbol or spelled name

Occurrence counts over the full documents (not sentences), so a table with ten rho headers
counts ten times.

| Form | Occurrences | Papers |
|---|---|---|
| LaTeX `\kappa` | 9 | 3: 2406.12624, 2406.18403, 2509.08010 |
| the word "kappa" | 26 | 5: 2305.17926, 2309.12570, 2406.12624, 2406.18403, 2509.08010 |
| "Cohen's kappa" spelled out | 13 | 2: 2406.12624, 2406.18403 |
| "Cohen's `\kappa`" (name plus symbol) | 7 | 2: 2406.18403, 2509.08010 |
| "Fleiss' kappa" spelled out | 1 | 1: 2309.12570 |
| "Krippendorff's alpha" spelled out | 7 | 3: 2303.16634, 2311.08516, 2405.01535 |
| "Krippendorff's `\alpha`" (name plus symbol) | 4 | 2: 2305.01937, 2311.08516 |
| the word "Spearman" | 34 | 4: 2303.16634, 2405.01535, 2406.12624, 2406.18403 |
| "Spearman's `\rho`" (name plus symbol) | 4 | 2: 2406.12624, 2406.18403 |
| bare LaTeX `\rho` | 32 | 4 |
| the word "Kendall" | 25 | 4: 2303.16634, 2305.01937, 2404.13076, 2405.01535 |
| "Kendall's `\tau`" (name plus symbol) | 12 | 2: 2305.01937, 2404.13076 |
| "Scott's `\pi`" | 28 | 1: 2406.12624 |
| "Scott's Pi" spelled out | 9 | 1: 2406.12624 |
| LaTeX `\beta` (regression coefficient) | 21 | 3: 2303.03199, 2305.17926, 2410.16184 |
| LaTeX `\sigma` | 19 | 5 |
| LaTeX `\chi` | 3 | 1: 2403.04132 |
| LaTeX `\eta` | 0 | 0 |

**The pattern.** No paper in the corpus introduces a bare Greek letter and expects the
reader to know what it is. The convention is the full name plus the symbol on first use,
then either the name or the symbol thereafter, with the symbol taking over inside tables
and captions where space is short. 2406.18403 is the clearest instance: prose reads
"we compute Cohen's `\kappa`", the table header reads "Average Cohen's `\kappa`", and the
figure caption reads "Cohen's `\kappa` for categorical annotations and Spearman's
correlation for graded annotations".

Two papers spell the statistic out in prose and never use the symbol at all
(2303.16634: "Krippendorff's alpha at 0.07"; 2311.08516: "We calculate Krippendorff's
alpha (Hayes and Krippendorff, 2007) to measure inter-rater reliability"). Nothing in the
corpus goes the other way, that is, symbol-only with no name anywhere.

Two papers name a statistic without a symbol or a standard name at all: 2305.17926 calls
it "the kappa correlation coefficient" throughout, citing McHugh (2012), and never says
whose kappa it is.

### 6.2 p-value formatting

Every numeric p-value in the corpus, verbatim, with the paper it comes from:

| Literal string | Count | Papers |
|---|---|---|
| `p<.0001` | 7 | 2303.03199 |
| `p<0.05` | 3 | 2406.18403 |
| `p=0.0125` | 3 | 2212.09746 |
| `p=0.05` | 2 | 2212.09746 |
| `p=.0125` | 2 | 2212.09746 |
| `p<0.005` | 2 | 2303.03199 |
| `p=0.02` | 2 | 2303.03199 |
| `p < 0.05` | 1 | 2303.03199 |
| `p<.01`, `p<.005`, `p<0.0005`, `p<0.001` | 1 each | 2303.03199 |
| `p=0.018`, `p=0.049`, `p=0.010`, `p=0.03`, `p=0.04`, `p=0.058` | 1 each | 2303.03199 |
| `p=0.07`, `p=0.51` | 1 each | 2410.16184 |

Total symbolic instances: 34, across 4 papers.

Excluded as not p-values: `p=0.9` (2305.01937) and `p=1` (2303.16634), both
nucleus-sampling top-p.

One further p-value is written out in words rather than in symbols, in a footnote to a
results section (2309.12570):

> 1313 13 This result is significant at the 5\% level with a p-value for the correlation of 0.04 .

**The pattern.** Only five papers report a numeric p-value attached to a test. Counting
symbolic instances, there are 34 in four papers, and 2303.03199 alone accounts for 22 of
them; 2309.12570 supplies the one prose-worded instance. 2303.03199 is also the only paper
using the leading-decimal APA form (`p<.0001`, `p<.005`); everywhere else the zero is
written (`p<0.05`, `p=0.07`). Nobody uses scientific notation. Exact p-values and threshold
p-values are mixed freely inside the same paper: 2303.03199 writes `p<.0001` for small
values and `p=0.018` for values near the threshold, which is the standard convention.

Asterisk notation appears in two papers and both explain it in a caption or table note
rather than in prose. 2303.17651: "Gains over Base, that are statistically significant
based on these confidence intervals are marked *". 2212.09746 uses `\ddagger` for
Bonferroni-corrected significance and `*` for uncorrected, explained in a footnote to the
figure.

### 6.3 Degrees of freedom, n, and effect size alongside a test

**Zero occurrences.** A regex for `t(df)=`, `F(df1,df2)=`, `chi^2(df)=`, `df =`, and the
phrase "degrees of freedom" returns nothing across all 24 papers. No test statistic
anywhere in the corpus is reported with its degrees of freedom.

The fullest reporting form in the corpus is 2303.03199, which reports coefficient,
standard error, 95% interval and p together, inside table cells rather than in prose:

> `s_{1} ( \beta =-1.26, SE=0.11, CI95%=[-1.48, -1.03], p<.0001)`

> `s_{1} ( \beta =-0.83, SE=0.13, CI95%=[-1.08, -0.57], p<.0001); i_{yes} ( \beta =-0.32, SE=0.14, CI95%=[-0.59, -0.05], p=0.018)`

The same paper's prose reports odds ratios with p and no interval:

> Single suggestions were rated as significantly more distracting ( x =1.95, p<0.005), less helpful ( x =0.60, p=0.02), lead...

Everywhere else the test result is reported bare: the statistic's value and nothing else.
2410.16184 is representative of the middle position, reporting the coefficient and the
p-value with no n and no interval:

> The Pearson correlation coefficient is 0.55 ( p=0.07 ), indicating a moderate positive correlation trending toward significance.

> In comparison, RewardBench (Lambert et al., 2024) reports a Pearson correlation of r=0.21 ( p=0.51 ) (see Section F in the appendix).

Sample size, where it appears at all, appears as a described count in the methods section
("three annotators", "200 prompts", "3K controlled expert votes"), not as an `N=` attached
to a test statistic.

### 6.4 Does the results section name the test, or only the outcome?

Named tests and statistics found inside each paper's results sections, with counts:

| arXiv ID | Named in results |
|---|---|
| 2201.06796 | Pearson (2) |
| 2206.05802 | bootstrap (1) |
| 2212.09746 | Tukey (3) |
| 2303.03199 | mixed-effects (1), GEE (2) |
| 2303.16634 | Spearman (5), Kendall (6), Pearson (2), Krippendorff (2) |
| 2303.17651 | none |
| 2305.01937 | Krippendorff (2), Welch (2), t-test (2), Kendall (8) |
| 2305.17926 | none |
| 2306.05685 | none |
| 2309.12570 | Pearson (1), Fleiss (1) |
| 2310.01798 | none |
| 2310.13548 | logistic regression (3), mixed effects (1) |
| 2311.08516 | none |
| 2402.11436 | none |
| 2403.04132 | chi-squared (1) |
| 2404.12272 | none |
| 2404.13076 | Kendall (2) |
| 2405.01535 | Pearson (4) |
| 2406.01297 | none |
| 2406.12624 | Scott's (11), Spearman (2) |
| 2406.18403 | Cohen's (1), Spearman (1) |
| 2410.16184 | Pearson (2) |
| 2505.06120 | none |
| 2509.08010 | none |

**Ten of 24 results sections name no test and no statistic.** In those papers the results
section reports differences in accuracy, win rate or agreement percentage, and the reader
is given no inferential apparatus at all. This includes four of the six anchors: Zheng
(2306.05685), Huang (2310.01798), Tyen (2311.08516) and Laban (2505.06120).

Where a test is named, it is named in one clause and not explained. 2305.01937 is the
model of the compressed form:

> However, the rating differences between the human-written and model-generated stories do not achieve statistical significance for grammaticality and relevance; the p-value obtained by Welch's t-test is much larger than 0.05 .

> By Welch's t-test, we find that the higher ratings on human-written stories are all statistically significant.

Note what that second sentence omits: no t, no df, no n, no p, no effect size. It names the
test and states the direction, and that is the whole report.

2303.03199 is the only paper that states its inferential procedure as a block at the head
of the results section:

> For statistical testing we use R (R Core Team, 2020), concretely, (generalised) linear mixed-effects models (LMMs with the packages lme4 (Bates et al., 2015), lmerTest (Kuznetsova et al., 2017)).

> ordinal data) with Generalized Estimating Equations (GEEs).

> We report significance at p < 0.05.

### 6.5 Where reliability statistics sit

Placement of the inter-rater reliability statistic in each paper that reports one:

| arXiv ID | Statistic | Where it is defined | Where the value is reported |
|---|---|---|---|
| 2303.16634 | Krippendorff's alpha | nowhere (quoting another paper) | results (4 Analysis) |
| 2305.01937 | Krippendorff's alpha and exact-agreement % | methods (3.1, table caption) | methods table and results prose |
| 2305.17926 | "kappa correlation coefficient" | methods (4.2 Experimental Setup and Metric) | results (4.3 Main Results) |
| 2309.12570 | Fleiss' kappa | nowhere | results, in a footnote |
| 2311.08516 | Krippendorff's alpha | methods (2.1.1 Human annotation) | methods, Table 3 |
| 2405.01535 | Krippendorff's alpha | appendix B | appendix D, Table 14 |
| 2406.12624 | Scott's pi and percent agreement | methods (3 Methodology) | results (4.1) and abstract |
| 2406.18403 | Cohen's kappa | methods (3 Model Selection) | results (4 Results) and Tables 1, 4, 6, 7 |
| 2509.08010 | Cohen's kappa | appendix (Validation) | appendix, Table 4 |

**The pattern.** The definition of the reliability statistic goes in methods; the value
goes wherever the reader needs it, which is usually a table or caption rather than prose.
Of the nine papers reporting a reliability statistic, six report the value in a results
section, two in methods, and two in an appendix (2305.01937 reports it in both methods and
results, which is why the counts sum to ten). One of the six results-section reports is a
footnote, in 2309.12570:

> 1414 14 The Fleiss' kappa of annotations was 0.52 , indicative of moderate agreement on the task.

That footnote is the entire treatment of annotation reliability in that paper, and it is
the only footnote-placed reliability statistic in the corpus. It is worth noting as a
minimum viable form: one sentence, value, and a verbal gloss of what the value means.

The gloss on a kappa or alpha value is common. 2303.16634 writes "very low, with
Krippendorff's alpha at 0.07"; 2309.12570 writes "0.52 , indicative of moderate
agreement"; 2509.08010 writes "`\kappa` corresponds to 'moderate' agreement" and adds
"This moderate level of agreement supports the use of these LLM judge labels for a
descriptive analysis of trends". No paper reports a bare number with no verbal
interpretation.

2406.12624 is the one paper that argues about which reliability coefficient to use, and it
does so in a footnote plus an appendix rather than in the results section:

> 33 3 In an earlier version of this paper, we used Cohen's kappa (Cohen, 1960) to measure alignment.

> We use two metrics to quantify alignment between judges: percent agreement and Scott's Pi coefficient (Scott, 1955).

### 6.6 What stands in for a test when there is no test

The ten papers with no named test do not simply omit uncertainty. Three substitutes recur.

**Error bars described in a caption, with the construction named once.** 2206.05802:

> Note: Throughout the paper, all error bars shown either use bootstrapping at the passage level or simply calculate standard error of the mean (when appropriate), and represent z=1 (i.e. one standard deviation on each side).

2310.13548 does the same in three consecutive figure captions: "Mean and standard error
across domains shown." / "Mean and standard error shown."

**A mean plus or minus a standard deviation written inline.** 2406.12624:

> The average alignment among human evaluators with the majority vote had a Scott's `\mathbf{\pi}` of 96.2\pm 1.07 ,

> and the average percent agreement was 98.52\%\pm 0.42\% .

**A resampling stability check reported as a variance, not a p-value.** 2406.12624 again:

> In Appendix I, we show with a bootstrapping test that this sample size has low variance for our main result.

Laban (2505.06120) uses none of these. Its results section reports no standard deviation,
no interval, no error bar and no p-value, and instead defines three descriptive metrics
over repeated simulations in the methods section (average performance, aptitude,
unreliability) and reports those directly. Its abstract uses "significantly" in the
non-technical sense:

> Our experiments confirm that all the top open- and closed-weight LLMs we test exhibit significantly lower performance in multi-turn conversations than single-turn, with an average drop of 39% across six generation tasks.

That sentence is the corpus norm for the word: "significant(ly)" appears in 22 of 24
papers and in 100 results-section sentences, while "statistically significant" appears in
only 8 papers and 14 results-section sentences. The loose use outnumbers the technical use
roughly seven to one.

---

## 7. What a results section in this literature reports as a matter of course

Ordered from most to least universal, with the count that supports each.

1. **A descriptive statistic with its unit and a comparison.** Universal, 24 of 24.
   Accuracy, win rate, percent agreement, correlation. The number is always given a
   referent in the same sentence.

2. **A verbal interpretation attached to every coefficient.** Universal wherever a
   coefficient appears. No paper reports a bare kappa, alpha, rho or r without saying in
   the same or the next clause what it means ("very low", "moderate agreement", "strong
   alignment", "trending toward significance").

3. **The name of any statistic the reader must interpret, spelled out at least once.**
   Universal among the 10 papers using a Greek-letter statistic (kappa, Krippendorff's
   alpha, rho, tau, Scott's pi). Full name plus symbol on first use is the standard form;
   symbol alone in tables and captions thereafter. Eighteen of the 24 papers name some
   statistic, test or model; the six that name none are listed in section 4.3.

4. **Tables and captions doing the numerical work.** 132 of the 465 statistical sentences
   (28%) are in a caption or a table cell. Captions restate what the statistic is, every
   time, rather than relying on the reader remembering from methods.

5. **The inter-rater reliability statistic, if there is human annotation.** 9 of the 24
   papers report one. Its definition sits in methods; its value sits in a table, a
   caption, results prose, or a footnote, in that rough order of frequency.

## 8. What is optional

1. **Any inferential test at all.** 10 of 24 results sections name none. Four of the six
   anchor papers are in that group. Reporting differences without a test is not
   penalised in this literature.

2. **p-values.** 5 of 24 papers report a numeric p attached to a test, and one paper
   (2303.03199) supplies 22 of the 34 symbolic instances. p-values are close to a marker
   of HCI-style user-study reporting rather than a general expectation.

3. **Degrees of freedom, n, and effect size next to a test statistic.** 0 of 24. This is
   not merely optional, it is absent. Reporting `t(47) = 2.31, p = .026, d = 0.34` would
   be unlike anything in the corpus.

4. **Confidence intervals.** 5 of 24 papers, and only 1 in a results section. Where they
   appear they are usually in an appendix (2303.17651's Appendix J is titled "Statistical
   Confidence Intervals" and holds the entire significance treatment for that paper).

5. **Multiple-comparison correction.** 2 of 24 papers, 0 results-section mentions. Both
   put it in a caption or appendix (2212.09746's Bonferroni corrections, 2403.04132's
   Fisher combination test).

6. **Chi-squared, ANOVA, Wilcoxon, Mann-Whitney, Kruskal-Wallis, Friedman, McNemar,
   Fisher's exact, eta-squared, Cohen's d.** Zero occurrences as a test of the paper's
   own data. The single chi-squared is a central-limit interval in Chatbot Arena's ranking
   method, not a test of association. The only t-test in the corpus is one Welch's t-test
   in 2305.01937.

7. **Bootstrap.** 4 of 24 papers, and used to build an interval or check stability, not to
   produce a p-value.

## 9. What this means for the Study 3 results section

The ledger holds more inferential machinery than any paper in this corpus reports in its
results section. Three observations follow, offered as observations rather than
instructions.

**The reliability statistic is the one thing the corpus expects and the paper must not
omit.** Nine of 24 report one, and every paper with human annotation of the kind Study 3
runs reports one somewhere. The minimum viable form is 2309.12570's single footnote
sentence: statistic, value, verbal gloss. The standard form is 2311.08516's: named in
methods with a citation, value in a table.

**Cohen's kappa and Krippendorff's alpha are both standard here, and neither needs
defending.** Cohen's kappa appears in 2 papers with the name spelled out and 2 more with
the symbol; Krippendorff's alpha in 4. 2406.12624 is the only paper that argues the choice,
and it does so in a footnote and an appendix rather than in results.

**Chi-squared, Wilcoxon and effect sizes have no precedent in this corpus.** That is not a
reason to drop them from the ledger, but it is a reason to expect that putting them in
results prose will read as a different field's register unless each is introduced by name
and given a plain-language reading in the same sentence. Two options are both defensible
against this corpus: report the test in one clause with its outcome and no apparatus
(2305.01937's Welch sentence is the model), or state the inferential procedure once in a
block at the head of the results section and then report bare coefficients with p
(2303.03199's model). The corpus contains no example of the middle path where each test is
reported with df, n and effect size.

**Notation form, if the statistics stay:** spell the full name with the symbol on first
mention (`Cohen's \kappa`, `Krippendorff's \alpha`, `Spearman's \rho`), use the symbol
alone in table headers and captions, write p-values with the leading zero (`p < 0.05`,
`p = 0.03`) unless the paper is going to an HCI venue, and give every coefficient a verbal
reading in the same sentence.

---

## 10. Access notes

- All 24 intended papers were retrieved successfully on 2026-09-06 from
  `arxiv.org/html`. Nothing in the intended corpus was unreachable, and no `ar5iv`
  fallback was needed.
- The ACL Anthology versions were not consulted. For papers published at ACL venues the
  camera-ready may differ from the arXiv version quoted here.
- 2509.08010 is a position paper without an experimental results section. It is retained
  in the corpus because its appendix reports a Cohen's kappa validation of LLM labels
  against hand coding, which is directly comparable to a Study 3 reliability check, but it
  should not be read as evidence about results-section conventions.
- Counts throughout are mechanical, produced by regular expressions over parsed sentences,
  with the hand-checked exclusions listed in section 1. They are reproducible from the
  fetched HTML but the fetched HTML is in a session scratchpad, not in this repository.
