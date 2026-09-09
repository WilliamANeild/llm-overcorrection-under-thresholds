# How NLP and human-evaluation papers report inter-rater reliability

Reference note for the ARR October 2026 submission. Built to answer one question: what does
the field actually print next to a reliability coefficient, and what would a reviewer expect
to see next to ours.

**Retrieval date for every item below: 2026-09-06.** Sources were fetched directly (arXiv HTML
at a named version, or the ACL Anthology PDF), converted to text locally, and searched
mechanically for reliability terms. Every quotation below was copied from the fetched text.
Nothing is cited that was not fetched. Version numbers are the version that resolved on the
retrieval date, not necessarily the latest.

Access failures: none. Two arXiv HTML fetches required falling back to an earlier version
(`2406.01297v3` rather than a later one, `2310.08491v2`); both returned full text. No paywalled
or gated source was needed.

---

## 1. Corpus

Thirty papers. Weighted toward LLM-as-judge work and human-evaluation methodology, with four
HCI-venue items and one INLG survey.

Legend for **Coefficient**: `%` = raw or percent agreement; `κ` = Cohen's kappa; `Fleiss` =
Fleiss' kappa; `α` = Krippendorff's alpha; `π` = Scott's pi; `AC1` = Gwet's AC1; `ρ` = Spearman;
`none` = no inter-rater statistic of the paper's own reported anywhere.

| # | Short name | Title | ID / version | Coefficient(s) | Location | n reported alongside |
|---|---|---|---|---|---|---|
| 1 | MT-Bench | Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena | arXiv 2306.05685v4 | % only | Abstract, intro, §4.2 results, App. D.3 | Yes: #votes per cell, 474–1343 |
| 2 | Chatbot Arena | Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference | arXiv 2403.04132v1 | % only | Results, Table 3 | Yes, in table |
| 3 | AlpacaFarm | AlpacaFarm: A Simulation Framework for Methods that Learn from Human Feedback | arXiv 2305.14387v4 | % only | Intro and §4.3 results | Partly (annotator pool sizes) |
| 4 | AlpacaEval-LC | Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators | arXiv 2404.04475v2 | none of its own | – | – |
| 5 | LLMBar | Evaluating Large Language Models at Evaluating Instruction Following | arXiv 2310.07641v2 | % only | Main text + footnote 5 | Yes, in footnote: 18/20 and 57/60 |
| 6 | FairEval | Large Language Models are not Fair Evaluators | arXiv 2305.17926v2 | κ + accuracy(%) | Results §5.1 | Yes: 80 annotated examples |
| 7 | PoLL | Replacing Judges with Juries: Evaluating LLM Generations with a Panel of Diverse Models | arXiv 2404.18796v2 | κ (judge–human only) | §4.1 results, Tables 1, 3–6 | Dataset sizes given, no rater n |
| 8 | Judging the Judges | Judging the Judges: Evaluating Alignment and Vulnerabilities in LLMs-as-Judges | arXiv 2406.12624v6 | π + % (both directions) | §4.1 results; App. B, I | Yes: 3 judges, 1200 questions |
| 9 | Prometheus | Prometheus: Inducing Fine-grained Evaluation Capability in Language Models | arXiv 2310.08491v2 | none (Pearson only) | – | – |
| 10 | Prometheus 2 | Prometheus 2: An Open Source LM Specialized in Evaluating Other LMs | arXiv 2405.01535v2 | α (model self-consistency, not human) | Appendix, Table 14 | 3 sampled generations |
| 11 | BiGGen Bench | The BiGGen Bench: A Principled Benchmark for Fine-grained Evaluation | arXiv 2406.05761v2 | α (human–human) | **Appendix B.3 only**, Table 5 | Yes: 28–40 instances, 3–4 participants, per capability |
| 12 | G-Eval | G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment | arXiv 2303.16634v3 | none of its own (cites another paper's α) | Discussion | – |
| 13 | PandaLM | PandaLM: An Automatic Evaluation Benchmark for LLM Instruction Tuning Optimization | arXiv 2306.05087v2 | κ (human–human) | §4 main text | Partly: 3 experts, 1K filtered from 2.5K |
| 14 | Judge-Bench | LLMs instead of Human Judges? A Large Scale Empirical Study across 20 NLP Evaluation Tasks | arXiv 2406.18403v3 | α (human–human) + κ and ρ (judge–human) | α in **Appendix A, Table 3**; κ/ρ in results | Per-dataset n in Appendix A Table 2 |
| 15 | Chiang & Lee | Can Large Language Models Be an Alternative to Human Evaluation? | arXiv 2305.01937v1 | α + % exact agreement | Results, Table 1 and caption | Yes: 200 stories, 3 English teachers |
| 16 | Clark et al. | All That's 'Human' Is Not Gold: Evaluating Human Evaluation of Generated Text | arXiv 2107.00061v2 | α | Results, Table 1 and §2.4 prose | Yes, per cell |
| 17 | Karpinska et al. | The Perils of Using Mechanical Turk to Evaluate Open-Ended Text Generation | arXiv 2109.06835v1 | α + % exact agreement | Results, Tables 1 and A3 | Yes: 3 raters per story, per condition |
| 18 | Hosking et al. | Human Feedback is not Gold Standard | arXiv 2309.16349v2 | AC1 (Gwet) | Main text, "Quality Control" paragraph | Yes: 5 duplicate annotations on 200 pairs; 900 outputs, 4,440 annotations |
| 19 | ConSiDERS | ConSiDERS-The-Human Evaluation Framework | arXiv 2405.18638v2 | normative (no own data) | §3.2.1 and checklist | – |
| 20 | Amidei et al. | Agreement is overrated: A plea for correlation to assess human evaluation reliability | ACL Anthology W19-8642 (INLG 2019) | survey of all; own case studies use Fleiss κ + Goodman–Kruskal gamma | Results §3, case studies §4 | Survey n = 135 papers; notes item n almost never reported |
| 21 | EvalLM | EvalLM: Interactive Evaluation of LLM Prompts on User-Defined Criteria (CHI) | arXiv 2309.13633v2 | Fleiss κ + raw agreement | §6.1.4 results, Table 1 | Yes: 19 MT-Bench requests |
| 22 | Who Validates the Validators | Who Validates the Validators? (UIST) | arXiv 2404.12272v1 | none reported | mentions IRR as a design concern only | – |
| 23 | HALIE | Evaluating Human-Language Model Interaction (TMLR 09/2023) | arXiv 2212.09746v3 | none | – | – |
| 24 | SummEval | SummEval: Re-evaluating Summarization Evaluation | arXiv 2007.12626v3 | α (called "interval kappa") | Main text, data-collection section | Yes: 100 articles × 16 models, 5 crowd + 3 expert, 12,800 annotations |
| 25 | JudgeBench | JudgeBench: A Benchmark for Evaluating LLM-Based Judges | arXiv 2410.12784v2 | none (argues against human labels) | – | – |
| 26 | DICES / intersectionality | Intersectionality in Conversational AI Safety | arXiv 2306.11530v1 | none, deliberately | §2.2 frames disagreement as signal | – |
| 27 | WildBench | WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild | arXiv 2406.04770v2 | none | – | – |
| 28 | PairS | Aligning with Human Judgement: The Role of Pairwise Preference in LLM Evaluators | arXiv 2403.16950v3 | none | – | – |
| 29 | Sharma et al. | Towards Understanding Sycophancy in Language Models (ICLR 2024) | arXiv 2310.13548v4 | none | – | – |
| 30 | Kamoi et al. | When Can LLMs Actually Correct Their Own Mistakes? | arXiv 2406.01297v3 | none | – | – |

---

## 2. Verbatim catalogue

Every sentence in which a reliability figure is reported, quoted from the fetched text.
Mathematical duplication of the form `κ \kappa` is an artifact of the HTML-to-text conversion
and has been left in place rather than silently edited.

### 1. MT-Bench (2306.05685v4)

Abstract:
> "Our results reveal that strong LLM judges like GPT-4 can match both controlled and crowdsourced human preferences well, achieving over 80% agreement, the same level of agreement between humans."

Introduction:
> "Once addressed, our results from 3K controlled expert votes and 3K crowdsourced human votes in the wild verify that GPT-4 judge match human evaluations at an agreement rate exceeding 80%, achieving the same level of human-human agreement (§ 4.2 , Table 4 )."

Metrics definition, §4.1:
> "We define the agreement between two types of judges as the probability of randomly selected individuals (but not identical) of each type agreeing on a randomly selected question."

Results, §4.2 ("High agreement between GPT-4 and humans"):
> "The agreement under setup S2 (w/o tie) between GPT-4 and humans reaches 85%, which is even higher than the agreement among humans (81%)."

Appendix D.3, on the ceiling being an underestimate:
> "Note that the agreement among humans could be a lower estimation compared to the agreement of GPT4 and humans."

No chance-corrected coefficient appears anywhere in the paper.

### 2. Chatbot Arena (2403.04132v1)

> "The agreement rate between crowd-users, experts, and GPT-4-judge are presented in Table 3 ."

> "To summarize, we observe high agreement rates (72% to 83%) between Arena crowd-user and experts in both setup."

> "Note that agreement rates between two experts are around similar levels (79.4% and 89.8%)."

> "The gap between crowd-vs-expert agreement rate and expert-vs-expert agreement rate (5%-10%) is mostly attributed to crowd user making mistakes or overlooking factual errors in model's response."

> "Overall, the agreement rates presented in Table 3 validate the decent quality of crowd-sourced votes in Chatbot Arena."

### 3. AlpacaFarm (2305.14387v4)

> "As a first baseline, we query GPT-4 with a single prompt (denoted as p sim GPT-4 p_{\text{sim}}^{\text{GPT-4}} ) and we find p sim GPT-4 p_{\text{sim}}^{\text{GPT-4}} has an agreement rate with human annotators that is similar to the agreement rate between humans (65% vs 66%; see results in Section 4.3 )."

> "We begin by computing agreement levels between our simulated annotator and a majority vote of 3 human annotators, comparing this to the agreement level of a held-out human annotator, as shown in Figure 4 ."

> "We find that our evaluator p sim eval p_{\text{sim}}^{\text{eval}} (green) has a 65% agreement rate with the human majority vote, which is similar to the held-out human agreement rate at 66% (blue)."

Annotator screening:
> "Out of an initial pool of 34 annotators, we selected the 16 whose agreement rate was higher than 70% with the authors' annotations."

### 4. Length-Controlled AlpacaEval (2404.04475v2)

The only reliability sentence is about other people's work:
> "While this latter class of algorithms has become sufficiently accurate that they match inter-annotator agreement rates, other works have shown that such measurements are heavily confounded by spurious correlations such as perplexity and length ( Durmus et al., 2022 ) ."

### 5. LLMBar (2310.07641v2)

> "As a result, LLMBar has an expert annotator agreement rate of 94 % 94\% , significantly higher than any of those previous benchmarks."

> "The agreement rate between expert annotators on the sampled LLMBar set is 94% ."

With the sample sizes in a footnote:
> "Human agreement rate is 90% and 95% respectively on the Natural and the Adversarial set 5 5 5 The agreement rate is 18/20 and 57/60 on (sampled) Natural and Adversarial instances respectively. ."

Benchmarking against other papers, and treating their figures as a defect:
> "As a reference, FairEval ( Wang et al., 2023b ) has an average human annotation accuracy of 71.7%; MT-Bench ( Zheng et al., 2023 ) reports a human agreement rate of 63%."

> "This issue is also demonstrated by the low agreements between human annotators reported in AlpacaFarm (66%; Dubois et al., 2023 ) and MT-Bench (63%; Zheng et al., 2023 ), against a random baseline of 50%. When selecting LLM evaluators based on such a low human agreement, we cannot guarantee that the c..."

Also used as a ceiling for the judges:
> "PaLM2-based and GPT-4-based evaluators show much higher accuracy on Adversarial , yet even the best performing GPT-4-based evaluator achieves an average accuracy of 82.8 % 82.8\% on Adversarial , more than 10 % 10\% lower than the human expert agreement rate ( 95 % 95\% )."

### 6. FairEval / "Large Language Models are not Fair Evaluators" (2305.17926v2)

Method:
> "We use the accuracy and kappa correlation coefficient McHugh (2012) with the final majority of human annotation results to measure the performance of different evaluators and evaluation methods."

Results, human–human as the reference line, on n = 80:
> "In detail, the average accuracy and the kappa correlation coefficient of human annotations are 71.7 71.7 % and 0.54 0.54 , respectively"

Judge improvement stated in kappa units:
> "Specifically, the accuracy is improved by 14.3%, and the kappa correlation coefficient is increased from 0.06 0.06 to 0.31 0.31"

A human–human kappa of 0.54 is printed with no verbal label and no defense.

### 7. Replacing Judges with Juries / PoLL (2404.18796v2)

Definition and, unusually for this corpus, an explicit threshold statement:
> "Cohen's kappa measures inter-rater reliability, which quantifies the level of agreement between two or more raters or judges."

> "The kappa statistic takes into account the possibility of agreement occurring by chance, making it a more robust measure than simple percent agreement."

> "Opinions vary on how scores should be interpreted, but in general κ > 0.8 \kappa>0.8 is considered a strong correlation and κ > 0.6 \kappa>0.6 is a moderate correlation."

Values, all judge–human, reported in the results table without further comment:
> "Judge NQ TQA HPQA EM 0.651 0.827 0.662 GPT-4 0.627 0.841 0.830 CMD-R 0.734 0.902 0.815 Haiku 0.749 0.894 0.873 GPT-3.5 0.726 0.859 0.833 PoLL 0.763 0.906 0.867 Table 1: Cohen's Kappa Judge Model Performance on Different Single-hop QA Datasets from KILT"

A kappa of 0.518 is reported in a prompt-ablation table with no apology:
> "Prompt Variant Kappa Zero-shot 0.518 Few-Shot Standard 0.627 ..."

No human–human ceiling is reported.

### 8. Judging the Judges (2406.12624v6)

The paper's central methodological claim:
> "Our research highlights the need for alignment metrics beyond percent agreement, as judges with high agreement can still assign vastly different scores."

Method, with the coefficient change disclosed in a footnote:
> "Alignment We use two metrics to quantify alignment between judges: percent agreement and Scott's Pi coefficient ( Scott, 1955 ) . 2 2 2 In an earlier version of this paper, we used Cohen's kappa ( Cohen, 1960 ) to measure alignment."

> "Scott's Pi, denoted as Scott's π \mathbf{\pi} , is an alignment metric that corrects for chance agreement between two annotators and is considered to provide a more robust measure of alignment."

Human–human ceiling, both coefficients, with n and dispersion:
> "The average alignment between human evaluators and the majority vote yielded a Scott's π \mathbf{\pi} of 96.2 ± 1.07 96.2\pm 1.07 , 3 3 3 The coefficient is scaled by 100 100 for easier comparison with percentage alignment. while the average percentage agreement was 98.52 % ± 0.42 % 98.52\%\pm 0.42\% , exceeding the alignment previously reported in comparable studies ( Zeng et al., 2024 ) ."

> "The inter-human alignment is calculated between three human judges using the answers to 1200 randomly sampled questions answers; the human guidelines can be found in Appendix G ."

Why the two statistics are reported together:
> "This is also visible in the general decline of alignment scores: while Llama-3 8B has a Scott's π \mathbf{\pi} score of only 59, its percent agreement is still well above 80%."

> "For the percent agreement of judge models, we note a 26-point difference between human judgment and EM, while Scott's π \mathbf{\pi} exhibits a more substantial 64-point gap."

Recommendation:
> "We recommend computing both percent agreement and Scott's π \mathbf{\pi} , paired with qualitative analysis, to avoid bias."

### 9. Prometheus (2310.08491v2)

No inter-rater coefficient. Human alignment is reported as Pearson correlation only.

### 10. Prometheus 2 (2405.01535v2)

Krippendorff's alpha is used for model self-consistency across sampled generations, not for human raters:
> "Instead of using error bars, we report the consistency in assessment formats, Krippendorff's alpha for consistency in direct assessment, and transitivity statistics for consistency in pairwise ranking."

> "Table 14: Krippendorff's alpha statistics for evaluator LMs when prompted 3 times via non-deterministic decoding."

Values in that table run from 0.2017 to 0.8976. Reported in an appendix, without labels.

### 11. BiGGen Bench (2406.05761v2)

The whole reliability report is one sentence in Appendix B.3, followed by a table:
> "Do ensure that we gather trustable human annotations, we measure the inter-human agreement statistics while gathering our dataset which is presented in Table 5 ."

> "Capability # Instances # Participants Krippendorff's Alpha grounding 40 4 0.592 reasoning 40 3 0.636 planning 28 4 0.645 safety 32 4 0.708 tool_usage 32 4 0.734 theory of mind 40 4 0.656 instruction following 40 4 0.895 refinement 28 4 0.634 Table 5: The inter-human agreement (Krippendorff's Alpha statistic) during Stage 2: Qualification Stage"

Six of the eight alphas are below 0.7. There is no verbal label, no threshold citation, and no
defense anywhere in the paper. The n per row is given.

### 12. G-Eval (2303.16634v3)

Reports no coefficient of its own. Cites another paper's alpha in the discussion, as an
explanation for its own result:
> "The authors of the original paper found that inter-annotator agreement on judging human-written and LLM-generated summaries is very low, with Krippendorff's alpha at 0.07."

### 13. PandaLM (2306.05087v2)

> "The final IAA amongst the three annotators, as measured by Cohen's Kappa ( Cohen, 1960 ) , yields average scores of 0.85, 0.86, and 0.88 respectively, indicating a relatively high level of reliability for our test dataset."

The high figure is manufactured by filtering:
> "Samples with significant divergences are excluded to ensure the Inter Annotator Agreement (IAA) of each annotator remains larger than 0.85."

> "The filtered test dataset contains 1K samples, while the original unfiltered dataset has 2.5K samples."

And used explicitly as a target for the model:
> "To refine the model's performance assessment compared to human evaluators, we can use the inter-annotator agreement (IAA) of 0.85 as a benchmark."

> "However, setting a realistic target slightly above this human IAA, say around 0.90, offers a challenging yet achievable goal."

Note for our purposes: these are **per-pair** coefficients (three values for three pairs), which
is the same reporting shape as ours.

### 14. Judge-Bench / "LLMs instead of Human Judges?" (2406.18403v3)

Method:
> "H ): Cohen's kappa for categorical annotations and Spearman's correlation for graded annotations."

> "For the former, we compute Spearman's correlation ( ρ \rho ) between model and human judgments; for the latter, we compute Cohen's κ \kappa . • When multiple individual human judgments are available (typically three, see Table 2 in Appendix A ), we estimate an upper bound by computing the average Spearman's ρ \rho or Cohen's κ \kappa between bootstrapped single-rater responses and the aggregated responses across raters."

Human–human alphas, in Appendix A, many of them very low, with no commentary:
> "Dataset Krippendorf's α \alpha Categorical Topical Chat 0.08 QAGS 0.49 DICES-990 0.14 DICES-350-crowdsourced 0.16 Persona Chat 0.33 Inferential strategies 1.0 Graded Dailydialog 0.59 Switchboard 0.57 Persona Chat 0.33 Topical Chat 0.08 Recipe-generation 0.41 NewsRoom 0.11 WMT 2020 En-De 0.5 WMT 2020 Zh-En 0.09 Table 3: Inter-rater agreement for datasets with multiple human annotations."

The ceiling logic, stated positively in the results:
> "Overall, the high degree of variability is not fully accounted for by the inherent difficulty of the annotation tasks, as reflected in the human upper bound. Moreover, except for a few datasets (e.g., QAGS, Recipe-generation, and NewsRoom), model scores remain notably below the upper bound."

> "Whenever multiple human annotations were publicly available for a property (see Table 3 for inter-annotator agreement scores), we computed upper-bound estimates for the correlations achievable by models. The intuition behind these estimates, borrowed from neuroscience Nili et al. (2014) , is that the maximum correlation a model can achieve with aggregated human responses is bounded by the average correlation between single..."

And an explicit statement that human reliability is itself a thing to be checked:
> "Therefore, depending on the task at hand, it may be necessary to validate the reliability of human annotators as well."

### 15. Chiang & Lee (2305.01937v1)

Method, in the results section:
> "We also report the inter-annotator agreement (IAA) among three annotators using Krippendorff's α \alpha ."

> "We report the mean and standard deviation of the Likert scores obtained from LLM evaluation and human evaluation and show the inter-annotator agreement (IAA) using two different metrics: (1) the Krippendorff's α \alpha , and (2) the percentage of the stories where three evaluators give the exact same rating."

Values, printed in Table 1 alongside every mean, for n = 200 stories and three English teachers.
Human raters on human-written stories: alpha 0.33 (grammaticality, 20.5% exact), 0.32
(cohesiveness, 27%), 0.08 (likability, 9.5%), 0.05 (relevance, 8%). On GPT-2-generated stories:
0.10, 0.14, -0.21, -0.03.

The only comment on the low values:
> "Based on the IAA, we also find that the agreements among experts are lower on GPT-2-generated texts and on the likability ."

And the paper's methodological response, citing Amidei:
> "We choose to use the correlation coefficient instead of the inter-annotator agreement score because IAA mainly cares if two annotators agree on the exact ratings, while the correlation coefficient focus on the question: \"when annotator A rates one story higher, does annotator B also rate the story higher?\" ( Amidei et al., 2019 ) ."

### 16. Clark et al. (2107.00061v2)

Method, in the results table caption:
> "In Table 1 , we see other statistics worsen as well between GPT2 and GPT3: how well evaluators identified the machine-generated text ( F 1 F_{1} , precision, and recall), evaluators' agreement (Krippendorff's α \alpha , a measure of annotator agreement that corrects for the probability of random agreement), and the percent of guesses that the text was human-written (% human)."

Values, all near zero, reported as a substantive finding rather than a defect:
> "This was also reflected in the low agreement scores between evaluators, with Krippendorff's α ≈ 0 \alpha\approx 0 across domains."

Table 1 alphas: 0.10, 0.09, 0.03 (GPT2 stories, news, recipes); 0.03, 0.05, 0.00 (GPT3).

### 17. Karpinska et al. (2109.06835v1)

Method, given in every table caption:
> "Inter-annotator agreement (IAA) between the three raters is measured with Krippendorff's α \alpha as well as the percentage of stories for which all three raters exactly agreed on a rating (the latter is subscripted)."

Interpretation attached to the construct, not to a threshold scale:
> "Ratings for likability were lower than in the experiments with less strict qualifications, but likability is a very subjective measure which consistently shows a very low agreement (Krippendorff's α \alpha of -0.04 to 0.11)."

IAA treated as an outcome that varies with conditions:
> "As shown in the second portion of Table 1 , although the first and third days yielded similar mean ratings/agreement in terms of grammar (M=4.00, IAA=0.21 vs M=3.98, IAA=0.18) and coherence (M=4.11, IAA=0.14 vs M=4.05, IAA=0.13), the second day received lower ratings across the board and had overall poor IAA (see Table 1 )."

> "Interestingly, their IAA was higher than the English teachers recruited from the authors' personal networks."

### 18. Hosking et al. (2309.16349v2)

The whole report, in a "Quality Control" paragraph in the main text:
> "We annotate a total of 900 distinct outputs, with a total of 4,440 annotations including quality checks. Quality Control In order to check inter-annotator agreement, we collect 5 duplicate annotations for a random subset of 200 pairs of outputs."

> "We use Gwet's AC1 measure ( Gwet, 2014 ) to assess inter-annotator agreement for the multiply annotated examples, finding good agreement scores of between 0.64 0.64 (for Factuality) and 0.94 0.94 (for Refusal)."

The dispersion is explained by task property, not apologized for:
> "The disparity indicates that annotators found some error types more difficult or subjective than others; refusal is straightforward to detect, whereas checking for factual errors involves significantly more effort."

This is the one paper in the corpus that calls a coefficient of 0.64 "good" in so many words.

### 19. ConSiDERS (2405.18638v2)

The field's normative statement, closest to what a reviewer would hold us to:
> "What is considered as \"low\" IRA can vary from task to task, as complex tasks or difficult samples tend to have low IRA Kim and Park (2023) . This is crucially important for interpreting IRA and is particularly relevant for NLG evaluation. NLG tasks have typically reported relatively low IRA, e.g., average Krippendorff's- α \alpha of 0.62 Amidei et al. (2019) , the standard interpretation is that experiments with scores less than 0.67 must be deemed unreliable Marzi et al. (2024) . For instance, rating \" How good is the generated story? \" is more likely to have a lower IRA compared to \" Is 99 the largest 2-digit number \". Hence, while it is mandatory to measure IRA, it is important to ensure that the scores are interpreted in the context of the task."

> "Performing detailed analysis including computing IRA using multiple metrics such as baseline percentage agreement and visualizing the item-wise agreement scores can help analyze the results."

On why percent agreement and a chance-corrected coefficient tell different stories:
> "We further demonstrate, using a toy example in Appendix A.3 , how disagreement on minority labels can substantially reduce IRA measured using a Krippendorff's- α \alpha while percentage agreement barely changes."

> "In scenario 3, we again just change 1 label, where the % agreement remains the same at 88%, but Krippendorff's- α \alpha drops from 0.24 to -0.06."

The checklist a reviewer could apply directly:
> "Inter-rater agreement 11. Which primary IRA measure did you use? 12. Does the primary measure take into account how the evaluation is designed, such as the aspects defined by Gisev et al. (2013) ? 13. Do you expect your task to be inherently unbalanced? If not, do you report baseline percentage agreement to verify if the observed chance estimation lowers the overall IRA? 14. Is the item-wise IRA higher for some items and not the others? The ones with lower IRA might be pointing to higher complexity tasks. Report on the distribution of items IRA to troubleshoot the problem. 15. Are the qualifications of the human evaluators similar? If not, the disparity in the evaluators' skills can lead to lower IRA. 16. Do you continuously measure IRA for each evaluation? If yes, did you observe a sudden change in IRA?"

On low IRA as a fixable guidelines problem:
> "Low IRA can indicate potential problems with the annotation guidelines, in which case revising the guidelines iteratively can lead to reasonable agreement Iskender et al. (2021) ."

### 20. Amidei, Piwek & Willis (ACL Anthology W19-8642)

Survey scope:
> "We confirmed this trend by analysing papers published over the last 10 years in NLG-specific conferences (in total 135 papers that included some sort of human evaluation study)."

How rarely reliability is reported at all:
> "Indeed, of the 135 papers in our study, just 18% (24 papers) report information about the IAA. Among these, four papers use two different coefficients to measure the IAA. The other 20 use just one coefficient."

Which coefficients, and their empirical distribution in NLG:
> "Coefficient Percent agreement Cohen's κ Krippendorff's α Fleiss's κ Pearson's r Kendall's W Weighted κ κ no better specified # used 7 4 5 5 2 1 1 3 Average 0.69 0.40 0.62 0.53 0.42 0.61 0.07 0.57 Min. 0.44 0.10 0.37 0.29 0.20 0.47 0.07 0.32 Max. 0.94 0.88 0.90 0.78 0.71 0.76 0.07 0.77 Table 3: Average, minimal and maximum IAA value per coefficient."

How rarely a threshold scale is invoked:
> "Between the papers that report the IAA, just 20% of the papers (5 works) make implicit or explicit reference to the interpretation scales used. The IAA interpretation scales reported by these papers are the Krippendorff scale (Krippendorff, 1980, see Table 1) and the Landis and Koch scale (Landis and Koch, 1977, see Table 2)."

The consequence of applying those scales literally:
> "The trend is that in human evaluation of NLG systems the IAA values reached are relatively low. Following the Krippendorff scale of IAA interpretation (Krippendorff, 1980) – which considers the threshold 0.67 as the minimum to be reached in order to get a reliable set of data (see Table 1) – the majority of the evaluations should be discarded."

And the paper's own resolution, which is the standard citation for the move we would make:
> "Following the existing scales of IAA interpretation, for example those of Krippendorff (1980) and Landis and Koch (1977), the majority of the evaluations should be discarded because they are unreliable. However, Sampson and Babarczy (2008), Lommel et al. (2014), Joshi et al. (2016) and Amidei et al. (2018b) suggest that a low level of IAA can be explained with human language variability."

Two reporting gaps it names, both of which bear on what we print:
> "In almost every paper we analysed, the number of items used for the IAA studies was not reported. Likewise, there were few cases in which it was reported whether or not the annotators worked independently."

> "More specifically, between the papers that report the IAA, 37% of the papers (9 works) use a IAA coefficient that is not suitable for the data collected. For example, the use of Fleiss' κ coefficient for data whose level of measurement is interval."

### 21. EvalLM, CHI (2309.13633v2)

Both statistics side by side in the results table:
> "Condition Agreement Fleiss' Kappa Overall-Quality 0.699 0.430 General-Criteria 0.639 0.420 Specific-Criteria 0.713 0.485 Table 1."

The framing sentence, which is the single closest precedent in the corpus for our situation:
> "As a reference, for data points with at least two annotators, the Fleiss' Kappa between two random human annotators was 0.496 (sampled 5 times and averaged), showing that Specific-Criteria agreed with human evaluations to a degree that was similar to human-human agreement."

> "Evaluating on specific criteria showed the highest agreement and Fleiss' kappa with the human evaluations."

Judge–human kappas of 0.42 to 0.485 are printed as a positive result, because the human–human
ceiling is 0.496 and is printed next to them. No verbal label is attached to any of the four numbers.

### 22. Who Validates the Validators, UIST (2404.12272v1)

No coefficient. Inter-rater reliability appears only as a design consideration:
> "Importantly, when allowing multiple users to collaborate on grading, evaluation assistants have to consider inter-rater reliability and handle disagreements, if any."

### 23. HALIE, TMLR 09/2023 (2212.09746v3)

No inter-rater coefficient of any kind.

### 24. SummEval (2007.12626v3)

Method and result in consecutive sentences, with the coefficient explicitly judged inadequate
and the remedy stated:
> "To evaluate the inter-annotator agreement of collected crowd-source and expert annotations we computed the Krippendorff's alpha coefficient ( Krippendorff, 2011 ) ."

> "We found the inter-annotator interval kappa to be below an acceptable range - 0.4920 and 0.4286 for the crowd-source workers and first round of expert annotations accordingly."

> "However, the second round of expert annotations improved the inter-annotator agreement achieving a kappa coefficient of 0.7187."

n:
> "Annotations were collected for 100 articles randomly picked from the CNN/DailyMail test set. To ensure high quality of annotations, each summary was scored by 5 crowd-source and 3 expert workers, amounting to 12800 summary-level annotations."

### 25. JudgeBench (2410.12784v2)

No human inter-rater statistic. The paper instead argues that human labels are the weak link:
> "The core assumption implied in these works is that crowdsourced human annotators will evaluate the responses objectively and not make mistakes. This assumption may hold when the problem is straightforward but falters when the tasks grow more complex."

> "In such cases, human evaluators may mistakenly favor responses that seem more plausible or are simply longer, prioritizing style over correctness—thereby violating the hierarchical framework."

Its only agreement figure is between two automated checkers:
> "In general, we found high rates of agreement between these methods (e.g., 97.7% and 99.5% agreement across 7000 responses to the 14000 MMLU-Pro questions for GPT-4o and Claude-3.5-Sonnet, respectively)."

### 26. DICES / Intersectionality in Conversational AI Safety (2306.11530v1)

No coefficient, by design:
> "Rater disagreement has historically been viewed as a data quality issue. But there is increasing recognition that disagreement is endemic to data annotation and should be viewed as a feature, not a bug ( Geng 2016 ; Liu et al. 2019 ; Klenner, Göhring, and Amsler 2020 ; Basile 2020 ; Prabhakaran, Mostafazadeh Davani, and Diaz 2021 ) , with increasing numbers of researchers in recent years addressing rater disagreement as a meaningful signal"

### 27–30. WildBench, PairS, Sharma et al., Kamoi et al.

None reports an inter-rater coefficient. WildBench uses human annotation for task filtering and
reports no agreement statistic. PairS reports only correlations with pre-existing human
annotations. Sharma et al.'s only reliability sentence is prospective: "We expect this to improve
the reliability of human feedback." Kamoi et al. is a survey and reports none.

---

## 3. Mechanical counts

Denominator is the 30-paper corpus unless stated.

### 3.1 Which coefficient is reported

Counting each coefficient once per paper, for statistics the paper computed on its own data
(a paper reporting two coefficients is counted in two rows):

| Coefficient | Papers | Which |
|---|---|---|
| Raw / percent agreement | 10 | MT-Bench, Chatbot Arena, AlpacaFarm, LLMBar, FairEval, Judging the Judges, Chiang & Lee, Karpinska, EvalLM, Amidei (case studies) |
| Krippendorff's α | 6 (human raters) | BiGGen, Judge-Bench, Chiang & Lee, Clark, Karpinska, SummEval |
| Krippendorff's α (non-human: model self-consistency) | 1 | Prometheus 2 |
| Cohen's κ | 4 | FairEval, PandaLM, Judge-Bench (judge–human), PoLL (judge–human) |
| Fleiss' κ | 2 | EvalLM, Amidei (case studies) |
| Scott's π | 1 | Judging the Judges |
| Gwet's AC1 | 1 | Hosking |
| Quadratic-weighted κ | **0** | none in the corpus |
| Spearman ρ as the judge–human alignment statistic | 1 | Judge-Bench |
| No inter-rater statistic at all | 12 | AlpacaEval-LC, Prometheus, G-Eval, Who Validates the Validators, HALIE, JudgeBench, DICES, WildBench, PairS, Sharma, Kamoi, plus ConSiDERS (normative, no own data) |

Papers reporting **any** human-rater reliability statistic, coefficient or percent: **16 of 30**.
Papers reporting a **chance-corrected coefficient** on human raters: **11 of 30**.
Papers reporting **only** percent agreement: **4** (MT-Bench, Chatbot Arena, AlpacaFarm, LLMBar).

Quadratic-weighted kappa does not appear once in 30 papers. Amidei's survey of 135 NLG papers
found weighted kappa used once, with a value of 0.07.

### 3.2 Do papers report more than one?

**7 of the 16 reporting papers report two or more statistics.** The combinations:

| Combination | Count | Which |
|---|---|---|
| Chance-corrected coefficient + percent/exact agreement | 5 | Judging the Judges (π + %), Chiang & Lee (α + % exact), Karpinska (α + % exact), EvalLM (Fleiss κ + raw agreement), FairEval (κ + accuracy) |
| Human–human coefficient + separate judge–human coefficient | 1 | Judge-Bench (α human–human; κ and ρ judge–human) |
| Two chance-corrected coefficients | 1 | Amidei case studies (Fleiss κ + Goodman–Kruskal gamma), and that pairing is the paper's argument |
| Single statistic only | 9 | MT-Bench, Chatbot Arena, AlpacaFarm, LLMBar, PoLL, BiGGen, PandaLM, Clark, Hosking, SummEval |

The pairing "chance-corrected coefficient plus raw agreement" is the single most common
multi-statistic pattern, and it is what ConSiDERS's checklist item 13 asks for.

### 3.3 Where it is reported

Of the 16 papers reporting something:

| Location | Count | Which |
|---|---|---|
| Results section (prose or results-table caption) | 12 | MT-Bench, Chatbot Arena, AlpacaFarm, LLMBar, FairEval, PoLL, Judging the Judges, Chiang & Lee, Clark, Karpinska, EvalLM, Amidei |
| Methods / data-collection section of the main text | 3 | PandaLM (§4), Hosking ("Quality Control"), SummEval |
| Appendix only | 2 | BiGGen (App. B.3), Judge-Bench (App. A, Table 3) |
| Footnote carries the n or the coefficient choice | 2 | LLMBar (n in footnote 5), Judging the Judges (coefficient switch in footnote 2, scaling in footnote 3) |
| Abstract | 1 | MT-Bench ("over 80% agreement, the same level of agreement between humans") |

Categories overlap where a paper reports in more than one place. The dominant pattern is a
number in the results section with the n in the table or an adjacent footnote.

### 3.4 Benchmarked against human–human agreement as a ceiling

**9 of 30 papers state a human–human figure explicitly as the reference level for a judge or
model.** The phrasings, in full:

| Paper | Phrasing |
|---|---|
| MT-Bench | "achieving the same level of human-human agreement"; "which is even higher than the agreement among humans (81%)" |
| Chatbot Arena | "Note that agreement rates between two experts are around similar levels (79.4% and 89.8%)." |
| AlpacaFarm | "which is similar to the held-out human agreement rate at 66% (blue)" |
| LLMBar | "more than 10 % lower than the human expert agreement rate ( 95 % )" |
| FairEval | "the average accuracy and the kappa correlation coefficient of human annotations are 71.7 % and 0.54 , respectively" |
| Judging the Judges | "The average alignment between human evaluators and the majority vote yielded a Scott's π of 96.2 ± 1.07 ... exceeding the alignment previously reported in comparable studies" |
| Judge-Bench | "we estimate an upper bound by computing the average Spearman's ρ or Cohen's κ between bootstrapped single-rater responses and the aggregated responses across raters"; "model scores remain notably below the upper bound" |
| EvalLM | "As a reference, for data points with at least two annotators, the Fleiss' Kappa between two random human annotators was 0.496 ... showing that Specific-Criteria agreed with human evaluations to a degree that was similar to human-human agreement." |
| PandaLM | "we can use the inter-annotator agreement (IAA) of 0.85 as a benchmark. If our model exceeds this, it indicates strong performance." |

Two of these papers state that the ceiling is a conservative estimate rather than a true bound.
MT-Bench: "Note that the agreement among humans could be a lower estimation compared to the
agreement of GPT4 and humans." Judge-Bench borrows the noise-ceiling construction from
neuroscience (Nili et al. 2014) and says so.

The move is nearly always made **positively**: state the ceiling, state the judge figure, note
the relation, stop. No paper in the corpus raises the low absolute value of the ceiling and then
rebuts it.

### 3.5 Per-pair versus pooled

| Reporting shape | Count | Which |
|---|---|---|
| Per-pair or per-rater coefficients | 2 | PandaLM ("average scores of 0.85, 0.86, and 0.88 respectively" for three annotators), Amidei case studies (pairwise gamma across judge pairs, e.g. "For i = 1, . . . , 6, Ji means judge i") |
| Disaggregated by condition, dataset, criterion or capability (not by rater pair) | 8 | BiGGen (per capability), Judge-Bench (per dataset), Chiang & Lee (per attribute × text type), Clark (per model × domain), Karpinska (per condition × attribute), Hosking (range across criteria), PoLL (per dataset), Prometheus 2 (per model) |
| Pooled single figure only | 6 | MT-Bench, Chatbot Arena, AlpacaFarm, LLMBar, FairEval, SummEval (two rounds) |

Disaggregation is the norm, but it is almost always by **task or criterion**, not by rater pair.
PandaLM is the only LLM-judge paper in the corpus that prints one coefficient per annotator pair,
which is the shape of our three pairwise values.

### 3.6 What n is reported alongside

| n reporting | Count | Which |
|---|---|---|
| Explicit item n next to the coefficient | 10 | MT-Bench (per-cell #votes), LLMBar (footnote, 18/20 and 57/60), FairEval (80), Judging the Judges (1200, 3 judges), BiGGen (28–40 instances, 3–4 participants per row), Chiang & Lee (200 stories, 3 teachers), Clark (per cell), Karpinska (per condition), Hosking (200 pairs × 5, of 900 outputs / 4,440 annotations), SummEval (100 articles, 5 crowd + 3 expert, 12,800 annotations) |
| Partial or indirect | 4 | Chatbot Arena, AlpacaFarm, PandaLM (3 experts; 1K of 2.5K), Judge-Bench (n in a separate appendix table) |
| Absent | 2 | PoLL (dataset sizes but no rater n), EvalLM (19 requests stated a section earlier, not next to Table 1) |

Amidei's survey finding is the relevant base rate: "In almost every paper we analysed, the number
of items used for the IAA studies was not reported."

### 3.7 Verbal labels

| Labelling practice | Count |
|---|---|
| Landis–Koch scale cited and applied to the paper's own coefficient | **0 of 30** |
| Any numeric threshold scale stated before the paper's own coefficients | 1 (PoLL: "κ > 0.8 ... strong ... κ > 0.6 ... moderate", unattributed) |
| A one-word evaluative adjective attached to a coefficient | 4 (Hosking "good"; PandaLM "relatively high level of reliability"; SummEval "below an acceptable range"; Karpinska "very low agreement", "poor IAA") |
| Landis–Koch named at all | 2 (Amidei, as a survey object; Hosking, coincidentally, an author surname in a reference list) |
| Coefficient printed with no verbal characterisation whatsoever | 7 (BiGGen, Judge-Bench, FairEval, EvalLM, Clark's table, Chiang & Lee's table, Prometheus 2) |

Landis and Koch's verbal scale is essentially absent from this literature as an applied device.
Attaching it to our numbers would be atypical, and would import the word "moderate" as a
self-assessment that nothing in the corpus requires.

---

## 4. How a moderate coefficient is handled

Every instance in the corpus of a reported coefficient below 0.7, with how it is characterised.

| Paper | Value(s) below 0.7 | What kind | Characterisation | Defended? |
|---|---|---|---|---|
| BiGGen | α = 0.592, 0.634, 0.636, 0.645, 0.656 (six of eight rows) | human–human | none at all | No. Printed in an appendix table, one sentence of framing, no adjective |
| Judge-Bench | α = 0.08, 0.09, 0.11, 0.14, 0.16, 0.33, 0.41, 0.49, 0.5, 0.57, 0.59 (11 of 14 datasets) | human–human | none | No. Reused as the human upper bound in the analysis |
| Chiang & Lee | α = 0.05 to 0.33 for human raters; 0.01 to 0.71 for LLM raters | human–human and model | "the agreements among experts are lower on GPT-2-generated texts and on the likability" | Not defended. The paper's response is to add Kendall's τ and cite Amidei on why exact-match agreement is the wrong question |
| Clark et al. | α ≈ 0.00 to 0.10 | human–human | "the low agreement scores between evaluators, with Krippendorff's α ≈ 0 across domains" | Not defended. Reported as a finding about the task, alongside contradictory free-text rationales from the same evaluators |
| Karpinska et al. | α = -0.09 to 0.49 across conditions | human–human | "likability is a very subjective measure which consistently shows a very low agreement"; "overall poor IAA" | Explained by construct subjectivity and by rater pool, not defended. IAA is treated as an outcome that responds to the manipulation |
| SummEval | α = 0.4920 (crowd), 0.4286 (expert round 1) | human–human | "below an acceptable range" | Not defended. Fixed: a second expert round reached 0.7187, and that is the figure the dataset ships with |
| EvalLM | Fleiss κ = 0.420, 0.430, 0.485 (judge–human); 0.496 (human–human) | both | none | Defended, once, by the ceiling: "showing that Specific-Criteria agreed with human evaluations to a degree that was similar to human-human agreement" |
| FairEval | κ = 0.54 (human–human); 0.06 to 0.31 (judge–human) | both | none | Not defended. The human figure functions as the reference line for the judge figures |
| PoLL | κ = 0.518 (zero-shot), 0.594, 0.599, 0.509, 0.627, 0.651, 0.662, 0.677 (judge–human) | judge–human | scale stated in advance: "κ > 0.6 is a moderate correlation" | Not defended per value. The scale is stated once, then the table speaks |
| Hosking | AC1 = 0.64 (factuality) | human–human | "good agreement scores of between 0.64 and 0.94" | Not defended; the spread is explained by task difficulty across criteria |
| Prometheus 2 | α = 0.2017 to 0.6976 for most open models | model self-consistency | none | No. Appendix table only |
| Amidei (survey) | field means: Cohen's κ 0.40, Fleiss κ 0.53, α 0.62, weighted κ 0.07, percent agreement 0.69 | survey of 135 NLG papers | "the IAA values reached are relatively low"; under the Krippendorff scale "the majority of the evaluations should be discarded" | Defended at the level of the field: low IAA reflects "human language variability", and correlation should be reported alongside agreement |

Four observations follow from this table.

**Silence is the modal treatment.** Of the twelve entries, seven attach no verbal characterisation
whatsoever to a sub-0.7 coefficient. BiGGen prints six alphas between 0.59 and 0.66 in an appendix
with one sentence of framing and no adjective. Judge-Bench prints eleven alphas below 0.6 and then
uses them as the human ceiling. Neither paper flags, hedges, or apologises. Neither has been
criticised for it in the papers that cite them.

**Where a value is defended, the defense is a ceiling, not an argument.** EvalLM is the clean
case: 0.430 next to 0.496 with one clause connecting them. FairEval does the same without the
connecting clause. No paper in this corpus writes a paragraph explaining why its coefficient is
acceptable. The move is to print the comparison and let it work.

**Where a value is called low, that is a finding, not a confession.** Clark et al. and Karpinska
et al. both report near-zero alphas and both are heavily cited precisely for that. In both cases
the low agreement is the object of study: evaluators cannot tell GPT-3 text from human text, and
crowdworkers cannot rate open-ended generation consistently. Neither paper treats its own alpha
as a threat to its own conclusions, because in both the alpha *is* a conclusion.

**The one paper that calls a value unacceptable also fixes it.** SummEval says "below an
acceptable range" and then reports a second annotation round at 0.7187. The judgment and the
remedy arrive together. A paper that announces its coefficient is inadequate and then proceeds
anyway would be doing something no paper in this corpus does.

**The countervailing risk, stated by LLMBar.** One paper in the corpus does attack others' low
agreement, and it is worth quoting in full because it is the reviewer voice we would be exposed
to: "This issue is also demonstrated by the low agreements between human annotators reported in
AlpacaFarm (66%; Dubois et al., 2023 ) and MT-Bench (63%; Zheng et al., 2023 ), against a random
baseline of 50%. When selecting LLM evaluators based on such a low human agreement, we cannot
guarantee that the c[onclusions hold]". Note what the criticism targets: not the value in
isolation, but the value **relative to its chance baseline** and the inferential weight placed on
it. LLMBar's own answer was to raise agreement to 94% by curating an easier-to-adjudicate
construct, and to report the n (18/20, 57/60) so the reader could check.

---

## 5. What our numbers would need beside them

Our figures, for reference: quadratic-weighted Cohen's kappa ranging from 0.406 to 0.603 across
the three rater pairs on 64 calibration items; Krippendorff's alpha of 0.529 on the 3 × 64 matrix; two
raters on 50 blind pairwise comparisons with 80% raw three-way agreement and Cohen's kappa of
0.703; judge–human agreement at kappa 0.569 and Spearman rho 0.505.

Against this corpus, those numbers are unremarkable. The alpha of 0.529 sits between BiGGen's
lowest (0.592) and Judge-Bench's median, above the Amidei survey mean for Cohen's kappa (0.40) and
Fleiss' kappa (0.53), and below the survey mean for Krippendorff's alpha (0.62). The pairwise
kappa of 0.703 is above every judge–human kappa in EvalLM and above six of eight in PoLL. What
makes the numbers read as weak is not their size. It is that they are not on the page with the
things that make a number legible.

Five items, in order of how much they change the reading.

**1. A human–human ceiling stated next to the judge figure, in one clause.** This is the single
highest-return addition, and nine papers in the corpus do it. Right now the judge–human kappa of
0.569 sits alone, and a reader has no way to know whether 0.569 is close to or far from the best a
judge could do. Put next to it the human–human figure from the same construct and the same items,
and 0.569 stops being an absolute and becomes a ratio. EvalLM's sentence is the template: state
the human–human value, state that it was computed on the subset where it could be, and say in one
clause that the judge figure is at or near it. Judge-Bench's noise-ceiling construction, borrowed
from Nili et al., is the more formal version if the pairwise design supports it.

**2. The n, adjacent to every coefficient.** Ten of the sixteen reporting papers do this, and
Amidei names its absence as the field's most common omission. 64 calibration items with three
raters, and 50 pairwise comparisons with two, are small enough that a reader will want the number
before deciding what the coefficient means; withholding it invites the worse assumption. LLMBar
puts its n in a footnote as a bare fraction (18/20, 57/60) and that is enough. BiGGen puts
`# Instances` and `# Participants` as columns of the reliability table itself, which for a
per-capability breakdown is cleaner.

**3. Raw agreement printed beside every chance-corrected coefficient.** Five of the seven
multi-statistic papers do exactly this, and ConSiDERS's checklist item 13 asks for it by name,
with the reason: a chance-corrected coefficient is depressed by marginal imbalance in a way
percent agreement is not, and the reader cannot tell the two situations apart from one number. We
already have 80% raw three-way agreement on the pairwise task and it is not in the results text.
On the calibration items, percent exact agreement across the three raters is the matching figure,
and Chiang & Lee's subscripted format (alpha with the exact-agreement percentage as a subscript)
puts both in one table cell without adding a column.

**4. The per-pair coefficients kept, with the spread explained by something other than noise.**
Reporting a range of 0.406 to 0.603 is more informative than a pooled figure, and PandaLM shows
that printing one value per pair is an accepted shape. What the corpus adds is that a spread reads
better when it is attributed. Hosking's sentence is the model: the range 0.64 to 0.94 is followed
immediately by "The disparity indicates that annotators found some error types more difficult or
subjective than others", with the mechanism named. If the low pair is low for a reason available
to us (one rater's calibration drifted, one construct is more subjective, one rater saw a
different item order), say which in a clause. If not, print the range and move on rather than
pooling it away, because the pooled alpha of 0.529 is already the pooled summary.

**5. The coefficient choice justified in a half-sentence, not a paragraph.** Quadratic-weighted
kappa appears zero times in thirty papers, so the choice is not self-explanatory to this audience
and one clause naming the ordinal scale will pre-empt the question. ConSiDERS's checklist items 11
and 12 are exactly this, and Amidei's finding that 37% of reporting papers used a coefficient
unsuited to their data level is what makes it worth a clause. Judging the Judges handles the
analogous issue in a footnote, disclosing that it moved from Cohen's kappa to Scott's pi and
putting the reason in an appendix.

**What to leave out.** Do not attach a Landis–Koch label. Zero of thirty papers apply one to their
own coefficient, and importing "moderate" as a self-description volunteers a verdict no reviewer
has asked for. Do not write a paragraph defending the values. No paper in the corpus does, and a
defense signals that the author believes there is something to defend. Do not follow SummEval's
"below an acceptable range" phrasing unless a second annotation round is also being reported,
because that sentence only works when the fix is in the same paragraph.

**The shape this suggests.** Two or three sentences in the results text: the coefficient with its
n; the raw agreement beside it; the human–human figure as the reference for the judge number; and
the per-pair range with its explanation. Then the full per-pair table, per-construct if the
constructs differ, in an appendix. That is BiGGen's and Judge-Bench's placement for the detail and
EvalLM's placement for the sentence that does the work. Nothing in this corpus requires more, and
several of its most-cited papers do considerably less.

---

## 6. Provenance

All 30 items fetched 2026-09-06. Twenty-nine from arXiv HTML at the version stated in the corpus
table; one (Amidei et al.) from `https://aclanthology.org/W19-8642.pdf`, extracted with
`pdftotext`. Sentence extraction was mechanical (regex over the reliability vocabulary:
kappa, κ, Krippendorff, Fleiss, Cohen, Scott's pi, Gwet, inter-annotator, inter-rater, inter-coder,
IAA, agreement rate, percent agreement, raw agreement, reliability), then read in full; counts in
§3 were tallied from that read rather than from the regex hit counts, because the regex also
matches author surnames (Cohen) and unrelated uses of "reliability".

Coverage bounds worth stating: the corpus is English-language, 2019–2025, and weighted toward
LLM-as-judge and NLG human evaluation. It contains three HCI-venue papers (EvalLM, Who Validates
the Validators, HALIE) and no CSCW paper. It does not cover machine-translation quality estimation, where MQM practice and
its own reliability conventions would likely give a different distribution. No claim here should
be read as covering that literature.
