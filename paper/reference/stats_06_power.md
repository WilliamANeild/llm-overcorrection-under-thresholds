# Statistical power and small-cell disclosure: what the literature actually does

Working reference for the ARR October 2026 submission. Compiled 2026-09-06.

## What this file is for

The paper has five disclosures to make and no template for making them:

1. The balanced panel is 50 trials, 45 of them (90%) from Llama 3.3 70B, with GPT-4o,
   DeepSeek V4 and Gemini 2.5 Flash contributing zero trials each.
2. Per-domain Turn-5 genuine-revision cells run from n = 13 (writing) to n = 30 (code);
   balanced-panel per-domain cells run from n = 5 (writing) to n = 22 (code).
3. Per-model targeted-feedback cells run from n = 3 (Gemini) to n = 71 (Llama), with an
   n < 5 no-test rule already applied.
4. Two human annotators compared 50 stripped pairs for the reversibility test.
5. Three human raters scored 64 stratified items for judge calibration and reliability.

This file records what comparable papers do, quoted verbatim, so that each disclosure can
be written in the field's own idiom rather than invented.

## Method and limits of the sweep

Every quotation below was extracted from a document fetched during this session. Sources
were read either as arXiv or ACL Anthology PDFs converted to text locally, or through a
fetched HTML page. Nothing is quoted from memory. Where a category is empty for a source,
it is marked NONE FOUND rather than filled.

Bounds of the sweep, stated so they are not mistaken for coverage: the corpus is English
language, drawn from NLP methodology, LLM evaluation, NLG human evaluation, and
human-subjects computing. It does not cover medicine, psychology proper, or economics
field experiments, where power reporting norms are stronger still. Venue-level base rates
below are taken from published meta-analyses inside the corpus, not computed here.

---

## 1. Corpus

All items fetched 2026-09-06. "Full text" means the PDF was downloaded and converted to
text locally; "page" means an HTML page was read.

| # | Source | ID | Venue / year | Access | Type |
|---|---|---|---|---|---|
| 1 | Card, Henderson, Khandelwal, Jia, Mahowald, Jurafsky, "With Little Power Comes Great Responsibility" | arXiv 2010.06595 / ACL 2020.emnlp-main.745 | EMNLP 2020 | full text | NLP methodology, meta-analysis |
| 2 | Howcroft & Rieser, "What happens if you treat ordinal ratings as interval data? Human evaluations in NLP are even more under-powered than you think" | ACL 2021.emnlp-main.703 | EMNLP 2021 | full text | NLP methodology, power simulation |
| 3 | Marie, Fujita, Rubino, "Scientific Credibility of Machine Translation Research: A Meta-Evaluation of 769 Papers" | arXiv 2106.15195 | ACL 2021 | full text | meta-evaluation |
| 4 | Gehrmann, Clark, Sellam, "Repairing the Cracked Foundation: A Survey of Obstacles in Evaluation Practices for Generated Text" | arXiv 2202.06935 | JAIR 2023 / preprint 2022 | full text | survey with mechanical counts |
| 5 | Amidei, Piwek, Willis, "The use of rating and Likert scales in natural language generation human evaluation tasks: A review and some recommendations" | ACL W19-8648 | INLG 2019 | full text | meta-analysis |
| 6 | Liang et al., "Holistic Evaluation of Language Models" (HELM) | arXiv 2211.09110v2 | TMLR 2023 | full text | large benchmark, model x scenario grid |
| 7 | Chiang, Zheng, Sheng, Angelopoulos, Li, Li, Zhang, Zhu, Jordan, Gonzalez, Stoica, "Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference" | arXiv 2403.04132 | ICML 2024 | full text | human preference leaderboard |
| 8 | Herrmann, Lange, Eggensperger, Casalicchio, Wever, Feurer, Rügamer, Hüllermeier, Boulesteix, Bischl, "Position: Why We Must Rethink Empirical Research in Machine Learning" | arXiv 2405.02200 | ICML 2024 | full text | position paper on exploratory vs confirmatory |
| 9 | Padmakumar & He, "Does Writing with Language Models Reduce Content Diversity?" | arXiv 2309.05196 | ICLR 2024 | full text | human-subjects writing study |
| 10 | Schoenegger, Karger, Park, Trott, Tetlock, "AI-Augmented Predictions: LLM Assistants Improve Human Forecasting Accuracy" | arXiv 2402.07862v2 | preprint 2024 (v2, Aug 2024) | full text | preregistered RCT with LLM |
| 11 | Peng, Kalliamvakou, Cihon, Demirer, "The Impact of AI on Developer Productivity: Evidence from GitHub Copilot" | arXiv 2302.06590 | preprint 2023 | page (ar5iv) | field RCT |
| 12 | Schütz, Cherif, Sayffaerth, Weber, Chiossi, "Typing Behavior in Human-LLM Interaction: Keystroke Dynamics Reveal Cognitive Effort During Prompting" | arXiv 2606.28090 | PACM HCI 2026 (accepted manuscript) | full text | HCI controlled study |
| 13 | ACL Rolling Review, "Author Guidelines" | aclrollingreview.org/authors | policy, current as of 2026-09-06 | page | venue policy |
| 14 | ACL Rolling Review, "Responsible NLP Research checklist" | aclrollingreview.org/responsibleNLPresearch | policy, current as of 2026-09-06 | page | venue policy |
| 15 | ACL 2023 Program Chairs, "ACL 2023 Review Process" blog post | 2023.aclweb.org/blog/review-acl23 | policy, current as of 2026-09-06 | page | venue policy |

---

# Part I. NLP methodology, benchmarks and human-subjects studies (15 sources)

## 2. Catalogue A: power analyses, verbatim

Three of the fifteen sources report a power analysis of their own study. Two are a priori
and preregistered; one is a simulation study whose whole subject is power. The rest report
none, and the meta-analyses in the corpus show that this ratio is not an artifact of the
sample.

### A1. Schoenegger, Karger, Park, Trott, Tetlock (arXiv 2402.07862v2), Methods, §2

> "We preregistered the following a priori power analysis to determine the sample size of
> our study: Using Cohen's d=0.20 as our smallest effect size of interest as a
> conventionally small effect, with an allocation ratio of 1.5/1/1 between the main
> treatment, the secondary noisy treatment, and the control, aiming for 80% power, we
> needed to recruit 492 participants for the Main treatment and 328 for the other two
> conditions, resulting in a final participant count of 1148. We recruited a total of 1,152
> participants, meeting our goal."

Note the structure: smallest effect size of interest named first, allocation ratio second,
target power third, required N fourth, achieved N fifth. Five clauses, one sentence, no
apology.

### A2. Schütz, Cherif, Sayffaerth, Weber, Chiossi (arXiv 2606.28090), §3.2 "Sample Size Justification"

> "We conducted an a priori power analysis using G*Power (version 3.1.9.7) to determine the
> required sample size for our 2 (Setting: Mobile vs. Desktop, between-subjects) x 2
> (Difficulty: Easy vs. Hard, within-subjects) mixed factorial design. We aimed to detect a
> medium-sized interaction effect between Setting and Difficulty. Based on a meta-analysis
> of typing experiments in HCI [33], a medium effect size for within-subject designs is
> estimated as Hedges's g_rm = .36, which corresponds approximately to Cohen's f ~ .25,
> following Yatani [61]. Using this effect size, a significance level of alpha = .05, and a
> desired statistical power of 1 - beta = .80, the power analysis indicated a minimum total
> sample size of 34 participants (17 per group). To ensure proper counterbalancing of
> within-subject order (i.e., Easy-Hard vs. Hard-Easy), we opted to recruit 36 participants
> (18 per group), allowing an equal distribution across counterbalanced orders."

The assumed effect size is sourced to a prior meta-analysis rather than asserted. This is
the HCI template: a named subsection titled "Sample Size Justification", placed in Method.

### A3. Howcroft & Rieser (ACL 2021.emnlp-main.703), §4 and §4.3

The paper is a power simulation, so its power statements are about the field, not one study:

> "The above analysis indicates that a study with 100 items and only 3 ratings per text
> would require an ordinal model to detect an effect of this size with 80% power, except in
> the low variance setting."

> "Since most studies are not using ordinal analyses of their data (Amidei et al., 2019),
> our simulation results suggest that most human evaluations are underpowered to detect
> typical system differences, exaggerating the effects reported in Card et al. (2020)."

### A4. Card, Henderson, Khandelwal, Jia, Mahowald, Jurafsky (arXiv 2010.06595), §6 "Overall Recommendations"

> "Power analyses should be done prior to evaluation when comparing against a baseline. If a
> comparison is likely to be underpowered, the pros and cons of running that evaluation
> should be carefully considered. Underpowered experiments do not provide convincing
> evidence of progress."

And the direct warning against the retrospective form, in footnote 2 of §1:

> "Using the observed outcome from a single experiment to compute power falls into the trap
> of post-hoc power analysis and is not recommended."

This footnote bears on the paper's own Appendix "Power Analysis" subsection, which is
labelled "Post-hoc power analysis at alpha = 0.05, 80% power". See §10 below.

### A5-A15. NONE FOUND

Marie et al. 2021, Gehrmann et al. 2022, Amidei et al. 2019, HELM, Chatbot Arena, Herrmann
et al. 2024, Padmakumar & He 2024, Peng et al. 2023, and the three ARR/ACL policy documents
report no power analysis of their own design. For Peng et al., a field RCT with 95
randomized developers, the absence is notable: the paper reports arm sizes and completion
counts but no minimum detectable effect.

### Base rates from the meta-analyses inside the corpus

Card et al. (arXiv 2010.06595), Appendix H.1, on 97 human evaluation experiments from
EMNLP 2019:

> "Significance testing was rare and was reported, in some form, in only 24% of experiments."

> "We did find one single case of authors performing a power analysis to estimate sample
> size among the papers we surveyed (Garbacea et al., 2019)."

Gehrmann, Clark, Sellam (arXiv 2202.06935), §5, on 66 papers from ACL, INLG and EMNLP 2021:

> "However, we did not find a single paper that estimated how many annotations should be
> collected, and most opted for the 'typical' 100 data points which, as pointed out above,
> may be insufficient (van der Lee et al., 2021)."

Same source, §5, reporting van der Lee et al. (2021):

> "van der Lee et al. (2021)'s survey finds that only 23% of NLG papers report statistical
> analyses to determine the significance of their results, and only 13% explicitly state
> their hypotheses."

Marie, Fujita, Rubino (arXiv 2106.15195), §3.2 "The Disappearing Statistical Significance
Testing", on 769 MT papers 2010-2020:

> "We found out that the observations by Dror et al. (2018) apply to MT since never more
> than 65.0% of the publications in a year (2011) performed statistical significance
> testing. Furthermore, our metaevaluation shows a sharp decrease of its use since 2016."

**Reading for this paper.** A power analysis of any kind puts a submission in a small
minority. The reported base rate for prospective power analysis in NLP human evaluation is
1 paper out of 97 experiments (Card et al.) and 0 out of 66 (Gehrmann et al.). The paper
already reports minimum detectable effects for three research questions. That is above the
field norm and should not be removed; it should be corrected in form (see §10).

---

## 3. Catalogue B: unbalanced, sparse or underpowered subgroups, verbatim

### B1. Padmakumar & He (arXiv 2309.05196), Appendix, per-topic significance testing

> "This matches the between-group experimental setup, albeit with less power as we only
> collected 10 essays per setup per topic."

The construction is worth copying exactly: a subordinate clause naming the cell size, joined
to the sentence that reports the test. The disclosure sits inside the analysis, not in a
limitations paragraph, and it costs one clause.

### B2. HELM, Liang et al. (arXiv 2211.09110v2), §11.2, on validity and reliability

> "In particular, we highlight the importance of significance testing for making meaningful
> comparisons given we only run 3 random seeds (due to cost) for selecting in-context
> examples and we evaluate on 1000 instances instead of the full validation/test set for a
> given dataset. That is, both of these settings for our evaluation may render some of our
> claims statistically insignificant; we encourage future work to consider how to better
> address significance given the scale of this evaluation."

This is the strongest positive-register model in the corpus for admitting that a design may
not support significance: it names the two design facts, states the consequence in one
clause, and turns immediately to what future work should do. No apology, no rebuttal.

### B3. HELM, Liang et al. (arXiv 2211.09110v2), Abstract and §1

> "Prior to HELM, models on average were evaluated on just 17.9% of the core HELM scenarios,
> with some prominent models not sharing a single scenario in common."

> "We measure 7 metrics (accuracy, calibration, robustness, fairness, bias, toxicity, and
> efficiency) for each of 16 core scenarios to the extent possible (87.5% of the time)"

The clause "to the extent possible (87.5% of the time)" is the compact way to report an
incomplete grid: a rate, in parentheses, attached to the claim it qualifies.

### B4. Peng, Kalliamvakou, Cihon, Demirer (arXiv 2302.06590), Study Design

> "A total of 166 offers were sent during the experiment, and 95 were accepted. The 95
> developers were randomly assigned into control and treated groups, with 45 in the treated
> group and 50 in control."

> "Thirty-five developers from both the treated and control groups completed the task and
> survey."

Unequal arms (45 vs 50) and heavy attrition (70 of 95 completing) are reported as plain
counts in Method, with no hedge attached and no defence offered.

### B5. Schoenegger et al. (arXiv 2402.07862v2), §5 "Limitations"

> "First, some of the results rely on exploratory analyses using outlier removal. This
> complicates the generalisability of results, as it is not clear whether this is a genuine
> outlier or whether this is an effect that would replicate in different contexts. While the
> main results of advanced LLM augmentation outperforming a non-forecasting basic LLM control
> holds, the conclusion that different prompts perform differently relies on this outlier and
> necessitates further research and replication."

The two-part move here is the one this paper needs: name the claim that survives, then name
the claim that does not, in the same sentence.

### B6. Chatbot Arena (arXiv 2403.04132), §3 and §8

> "On average, 8K votes are collected for each model."

> "Note that we employ non-uniform sampling to concentrate votes on model pairs that have
> similar performance due to higher uncertainty. This helps us reduce the number of votes
> required to reach stable results."

Chatbot Arena's answer to unequal cells is a design response rather than a caveat: it
allocates more data where the interval is widest. It reports no minimum vote count for
leaderboard inclusion and no statement that any model's estimate is unreliable for want of
votes. Recorded here as a negative case.

### B7. Schütz et al. (arXiv 2606.28090), Discussion / limitations

> "Furthermore, we utilized a single local LLM instance. Replicating the study with various
> state-of-the-art LLMs, as well as comparing the results to non-LLM chatbots, would help
> isolate the specific impact of human-agent interaction dynamics."

> "Another limitation relates to the analysis of a single task (meal planning), which limits
> the generalizability of the findings. Future work should repeat this study across multiple
> task domains."

### B8. Card et al. (arXiv 2010.06595), §1 and §3

> "Among human evaluations, we find most experimental designs involve too few items and/or
> raters to detect small effects"

> "For any comparisons which are likely to be underpowered, we should refrain from placing
> much emphasis on obtaining small improvements over the previously reported best model."

### B9. Card et al. (arXiv 2010.06595), §5.1, on missing design detail in the surveyed papers

> "Most commonly missing was number of ratings per item (34% of all experiments), followed by
> total number of workers (28%). For 7% of experiments, we could not determine the number of
> items tested."

### B10. Marie, Fujita, Rubino (arXiv 2106.15195), §5 "Conclusion"

> "This work also has its limitations since it does not cover all the pitfalls of MT
> evaluation. For instance, we noticed that MT papers regularly rely on the same language
> pairs to claim general improvements of MT."

Relying on one language pair to claim a general improvement is the direct analogue of
relying on one model to claim a general revision effect. Marie et al. name it as a pitfall
in someone else's work; the paper here should name it in its own, first.

---

## 4. Catalogue C: explicit minimum cell size rules

This is the thinnest category in the corpus, and the finding is itself useful: almost no
paper states a numeric floor below which it declines to test.

### C1. Chatbot Arena (arXiv 2403.04132), §5.1 / Appendix, anomalous user detection

> "at least 50 votes"

Used to decide which users are eligible for the anomaly check, not which models are eligible
for the leaderboard. It is the only explicit numeric inclusion floor located in the corpus.

### C2. Card et al. (arXiv 2010.06595), §3, a retirement rule rather than a test floor

> "In extreme cases, such as MRPC and SST-2, it is worth considering whether it is time to
> retire these datasets as the basis for model comparison."

And in §6:

> "For new datasets and shared tasks, the number of instances in the test will determine the
> level of detail required in [the power analysis]"

### C3. Howcroft & Rieser (ACL 2021.emnlp-main.703), §4.3, an effective floor stated as a design requirement

> "The above analysis indicates that a study with 100 items and only 3 ratings per text would
> require an ordinal model to detect an effect of this size with 80% power, except in the low
> variance setting."

### C4. Card et al. (arXiv 2010.06595), §5.3 recommendations, an effective floor for human evaluation

> "Even with low variance, typical designs are underpowered to detect small effects: Using our
> estimated parameters for the low variance setting, experiments will be underpowered to detect
> small effects (0.05 on the [0, 1] scale), unless an unusually large number of ratings per item
> are collected (10+ for 100 items)."

### C5-C15. NONE FOUND

No explicit "we do not test cells with fewer than N observations" rule was located in any of
the fifteen sources. HELM, Chatbot Arena, Peng et al., Padmakumar & He, Schoenegger et al.,
Schütz et al., Marie et al., Amidei et al., Gehrmann et al., Herrmann et al. and the three
policy documents state none.

**Reading for this paper.** The paper's Table `tab:targeted-per-model` already prints
"-- ($n < 5$)" in place of a p-value for the Gemini cell. That is a stated floor, applied,
and visible in the artifact. It is rarer in this literature than the paper's authors are
likely to assume, and it is worth stating in words once in the methods rather than leaving
it to be inferred from a table entry. Suggested wording is in §10.

---

## 5. Catalogue D: a result produced disproportionately by one arm

This is the crux category. Verbatim instances, ordered from closest analogue to furthest.

### D1. Schoenegger, Karger, Park, Trott, Tetlock (arXiv 2402.07862v2), Results, exploratory sensitivity analysis

> "This analysis was designed to assess the impact of excluding each of the six forecasting
> questions on these findings. This involved examining how the removal of each item, one at a
> time, affects the overall findings. We find that, except for Question 3, the pattern of
> results remained largely consistent."

> "These findings suggest that Question 3 in particular contributed to the overperformance of
> the noisy LLM augmentation condition compared to the other two groups"

And in the Abstract, where the dependence is stated before any reader can be misled:

> "Exploratory analyses showed a pronounced outlier effect in one forecasting item, without
> which we find that the superforecasting assistant increased accuracy by 41%, compared with
> 29% for the noisy assistant."

And in §5 Limitations, where the claim that depends on the single item is named:

> "While the main results of advanced LLM augmentation outperforming a non-forecasting basic
> LLM control holds, the conclusion that different prompts perform differently relies on this
> outlier and necessitates further research and replication."

This paper does the thing the ARR reviewer will want: it distinguishes the claim that
survives removal of the dominant unit from the claim that does not, and it does so in the
abstract, the results and the limitations. Three placements, one message.

### D2. HELM, Liang et al. (arXiv 2211.09110v2), §1

> "Prior to HELM, models on average were evaluated on just 17.9% of the core HELM scenarios,
> with some prominent models not sharing a single scenario in common."

The clause "not sharing a single scenario in common" is the field's existing phrasing for
zero overlap between arms. The paper's three zero-contribution models are the same fact in a
different grid.

### D3. Marie, Fujita, Rubino (arXiv 2106.15195), §5

> "For instance, we noticed that MT papers regularly rely on the same language pairs to claim
> general improvements of MT. They also almost exclusively focus on translation from or into
> English."

### D4. Chatbot Arena (arXiv 2403.04132), §7

> "we observe high agreement rates (72% to 83%) between Arena crowd-user and experts in both
> setup. Note that agreement rates between two experts are around similar levels (79.4% and
> 89.8%)."

Not a single-arm disclosure, but the template for putting a validation number next to the
between-rater number so a reader can judge the ceiling. The paper's judge-versus-human kappa
of 0.569 needs the same neighbour.

### D5. Schütz et al. (arXiv 2606.28090), limitations

> "Furthermore, we utilized a single local LLM instance."

Four words. A single-model design disclosed without wrapping.

### D6-D15. NONE FOUND in the remaining sources.

**Reading for this paper.** Of fifteen sources, one (Schoenegger et al.) discloses in full
that a primary claim is produced by one unit, and it does so by separating the surviving
claim from the dependent claim. Two more (HELM, Marie et al.) name incomplete or repeated
coverage without tying it to a specific result. The paper's existing sentence in
`results_v2.tex` already does the Schoenegger move and does it better than most of this
corpus. See §10.

---

## 6. Catalogue E: hedging vocabulary for small-cell results, Part I sources

Exact words, with the phrase they sit in.

| Word or phrase | Source | Containing phrase, verbatim |
|---|---|---|
| "albeit with less power" | Padmakumar & He | "This matches the between-group experimental setup, albeit with less power as we only collected 10 essays per setup per topic." |
| "may render some of our claims statistically insignificant" | HELM §11.2 | "both of these settings for our evaluation may render some of our claims statistically insignificant" |
| "to the extent possible" | HELM §1 | "for each of 16 core scenarios to the extent possible (87.5% of the time)" |
| "exploratory" | Schoenegger et al. | "Exploratory analyses showed a pronounced outlier effect in one forecasting item" |
| "necessitates further research and replication" | Schoenegger et al. §5 | "the conclusion that different prompts perform differently relies on this outlier and necessitates further research and replication" |
| "complicates the generalisability" | Schoenegger et al. §5 | "This complicates the generalisability of results, as it is not clear whether this is a genuine outlier" |
| "limits the generalizability" | Schütz et al. | "the analysis of a single task (meal planning), which limits the generalizability of the findings" |
| "we should refrain from placing much emphasis" | Card et al. §3 | "For any comparisons which are likely to be underpowered, we should refrain from placing much emphasis on obtaining small improvements" |
| "underpowered" | Card et al., Howcroft & Rieser, Gehrmann et al. | "most human evaluations are underpowered to detect typical system differences" |
| "do not provide convincing evidence of progress" | Card et al. §6 | "Underpowered experiments do not provide convincing evidence of progress." |
| "it is difficult to draw strong conclusions" | Card et al. §5.1 | "in our case, this correlation is not significant (Kendall's tau = -.07, p = .32) and so it is difficult to draw strong conclusions." |
| "should rather be considered exploratory" | Herrmann et al. §1 | "we argue most current empirical machine learning research is fashioned as confirmatory research while it should rather be considered exploratory." |
| "may be insufficient" | Gehrmann et al. §5 | "most opted for the 'typical' 100 data points which, as pointed out above, may be insufficient" |

The word "directional" does not appear in any Part I source in this sense. Neither does
"illustrative" or "suggestive" as a hedge on a small cell. The field's actual vocabulary is
narrower than the four terms the brief anticipated: it is built from **underpowered**,
**exploratory**, **less power**, **generalizability**, and a future-work clause.

Two idioms recur and are worth adopting:

1. **Cell size inside the reporting sentence.** "albeit with less power as we only collected
   10 essays per setup per topic" (Padmakumar & He). The n and the hedge are one clause.
2. **Consequence plus assignment to future work.** "we leave to future work" or
   "necessitates further research and replication." The disclosure ends by saying what would
   settle it, which removes the apologetic tone.

---

# Part I-B. Five further NLP methodology sources

Fetched 2026-09-06. Card et al. appears in Part I and is not repeated.

| # | Source | ID | Venue / year |
|---|---|---|---|
| 16 | Dror, Baumer, Shlomov, Reichart, "The Hitchhiker's Guide to Testing Statistical Significance in Natural Language Processing" | ACL P18-1128 | ACL 2018 |
| 17 | Howcroft, Belz, Clinciu, Gkatzia, Hasan, Mahamood, Mille, van Miltenburg, Santhanam, Rieser, "Twenty Years of Confusion in Human Evaluation" | ACL 2020.inlg-1.23 | INLG 2020 |
| 18 | van der Lee, Gatt, van Miltenburg, Wubben, Krahmer, "Best practices for the human evaluation of automatically generated text" | ACL W19-8643 | INLG 2019 |
| 19 | Bowman & Dahl, "What Will it Take to Fix Benchmarking in Natural Language Understanding?" | arXiv 2104.02145 | NAACL 2021 |
| 20 | Ethayarajh & Jurafsky, "Utility is in the Eye of the User: A Critique of NLP Leaderboards" | arXiv 2009.13888 | EMNLP 2020 |

## 7. Power analysis in these five

**van der Lee et al. (W19-8643), §4.4**, the strongest field-level statement located in the whole corpus:

> "Ironically, with every system or baseline that is added to the evaluation, the comparison
> becomes more interesting but the statistical model becomes more complex, and power issues
> become more pressing (Cohen, 1988; Button et al., 2013). However, statistical power - the
> probability that the statistical test will reject the null hypothesis (H0) when the
> alternative hypothesis (H1, e.g., that your new NLG system is the best) is true - are
> seldom (if ever) discussed in the NLG literature."

(The subject-verb disagreement is in the original. Dashes replaced here with hyphens.)

**van der Lee et al., §3.4:**

> "Apart from participant sample size, an important issue that impacts statistical power is
> the number of items (e.g. generated sentences) used in an evaluation."

**Bowman & Dahl (arXiv 2104.02145), §3.3 "Statistical Power":**

> "Benchmark evaluation datasets should be large and discriminative enough to detect any
> qualitatively relevant performance difference between two models."

> "In the context of a reliable dataset that is difficult for current systems, a 1% absolute
> accuracy improvement, such as that from 80% to 81%, may be an acceptable minimum detectable
> effect. In this case, an evaluation set of a few thousand examples would suffice under
> typical conditions seen in NLU (Card et al., 2020). Many, though not all, popular benchmark
> datasets satisfy this size threshold."

**Dror et al. (P18-1128)**: power appears only as a property of a statistical test, never as a
quantity computed for a design. Verbatim, §2.1:

> "A common approach in hypothesis testing is to choose a test that guarantees that the
> probability of making a type I error is upper bounded by the test significance level alpha,
> mentioned above, while achieving the highest possible power: i.e. the lowest possible
> probability of making a type II error."

**Howcroft et al. (2020.inlg-1.23)**: NONE FOUND. The word does not appear in a statistical
sense. Its recommended minimum-reporting table (Table 7) has rows for task, input/output,
criterion name, criterion definition, instrument type, and instructions. It has no row for
number of evaluators, number of items, effect size, statistical test, or power, even though
the paper's own opening names missing evaluator counts as a problem.

**Ethayarajh & Jurafsky (arXiv 2009.13888)**: NONE FOUND. No power, no significance test, no
sample size. It advocates disaggregated and worst-group reporting without any statement about
the precision of estimates on those cells.

## 8. Small-cell and unbalanced disclosure in these five

**van der Lee et al., §3.3**, the annotator distribution that places this paper's two-annotator design:

> "14 papers (28%) used an expert-focused approach, meaning that between 1 and 4 expert
> annotators evaluated system output. 13 papers (26%) employed a larger-scale reader-focused
> method in which 10 to 60 readers judged the generated output. We found a median of 4
> annotators. However, these numbers might not reflect reality: only 55% of papers specified
> the number of participants and an even smaller number (18%) reported the demographics of
> their sample."

**van der Lee et al., §3.4:**

> "Among papers that reported these numbers, we observed a median of 100 items used for human
> evaluation in INLG and ACL papers. The number of items however ranged between 2 and 5,400,
> illustrating a sizable discrepancy."

> "In 83% of papers that reported these figures, all annotators saw all examples."

**van der Lee et al., §3.3**, on reporting agreement from few raters:

> "Only 12.5% of the papers with a human evaluation reported inter-annotator agreement, using
> Krippendorff's alpha, Fleiss' kappa, Weighted kappa or Cohen's kappa. Agreement in most cases
> ranged from 0.3 to 0.5, but given the variety of metrics and the thresholds used to determine
> acceptable agreement, this range should be treated with caution."

This is directly usable: the paper's own three-rater quadratic-weighted kappas of 0.41 to 0.60
and Krippendorff's alpha of 0.529 sit inside, and slightly above, the range van der Lee et al.
report as typical.

**van der Lee et al., §4.2**, on exclusions producing an unbalanced remainder:

> "subject to debate, with some researchers pointing out that after such elimination procedures,
> the remaining cases may be a biased subsample of the total sample, thus biasing the results"

**van der Lee et al., §4.4**, naming the mechanism this paper's balanced panel must answer:

> "Conducting and analysing a human experiment is like entering a garden of forking paths
> (Gelman and Loken, 2013): along the way researchers have many choices to make, and even though
> each choice may be small and seemingly innocuous, collectively they can have a substantial
> effect on the outcome of the statistical analyses"

**Card et al., §5.1 and Appendix H.1** (extraction verified twice, independently):

> "Number of items tested is more consistent: 69% used 100 or fewer, and only 18% used over 200."

> "57% of experiments collected 3 annotations per item, which was also the modal number of
> unique annotators."

> "Significance testing was rare and was reported, in some form, in only 24% of experiments."

**Card et al., Figure 6 caption:**

> "Under typical assumptions, many common experimental settings (e.g., 3 workers and 100 items)
> are underpowered."

**Dror et al., §3.2:**

> "The test is less effective for small test sets, as it assumes that the test set distribution
> does not deviate too much from the population distribution."

**Dror et al., §4**, on multiplicity across many small comparisons:

> "In ACL 2017, out of 110 papers that used multiple datasets only 3 corrected for multiplicity
> (all using the Bonferroni correction). In TACL, the situation is slightly better with 4 papers
> correcting for multiplicity out of 19 that should have done that."

**Howcroft et al., Table 2 note**, an unbalanced-design disclosure placed in a table note:

> "Numbers are not directly comparable (a) between the two tests due to changes in the
> annotation scheme; (b) within the 2nd test due to different numbers of annotators."

**Howcroft et al., §4**, a candid statement that a counting choice inflates cells:

> "For the quality criterion attributes (Section 3.2.2) and the operationalisation attributes
> (Section 3.2.3) it makes most sense to compute occurrence counts on the 478 individual
> evaluations, even if that slightly inflates counts in some cases."

**Bowman & Dahl, §2**, on cells emptied by saturation:

> "wound up needing to exclude the large majority of the submitted tasks from the leaderboard
> because the BERT model (Devlin et al., 2019) was already showing performance at or above that
> of a majority vote of human crowdworkers. Of the eight tasks for which BERT did poorly enough
> to leave clear headroom for further progress, all are now effectively saturated"

**Ethayarajh & Jurafsky**: NONE FOUND.

## 9. Minimum cell size rules in these five

**van der Lee et al. is the only source in the entire twenty-source corpus that states numeric
annotator floors.** §4.2:

> "For expert-focused evaluations, good advice is provided by Van Enschot et al. (2017):
> difficult coding tasks (which most NLG evaluations are) require three or more annotators
> (though preferably more; see Potter and Levine-Donnerstein, 1999), more straightforward tasks
> can do with two to three."

> "In the case of large-scale studies, Brysbaert (2019) recently stated that most studies with
> less than 50 participants are underpowered and that for most designs and analyses 100 or more
> participants are needed."

**van der Lee et al., Table 3 "List of best practices", Annotation row:**

> "For a qualitative analysis, recruit multiple annotators (at least 2, more is better)"

That last line is the single most useful sentence in the corpus for this paper's reversibility
design. Two annotators is the stated floor for a qualitative comparison in the NLG best-practice
list, and the paper's two annotators on 50 pairs meet it. The paper should cite it rather than
apologize.

**Card et al., §5.1 footnote 11**, an analysis exclusion stated as a rule:

> "We exclude from this analysis two large negative effects with N = 500 which would exaggerate
> this correlation."

**Dror et al., §4 footnote 3**, a rule that condemns a practice tied to small test sets without
defining small:

> "We considered the significance test to be inappropriate in three cases: 1. Using the t-test
> when the evaluation measure is not an average measure; 2. Using the t-test for a classification
> task (i.e. when the observations are categorical rather then continuous), even if the
> evaluation measure is an average measure; and 3. Using a Boostrap test with a small test set
> size."

("Boostrap" and "rather then" are in the original.)

**Howcroft et al., Bowman & Dahl, Ethayarajh & Jurafsky**: NONE FOUND.

## 10. One-arm dependence in these five

**Card et al., §4**, the clearest single-condition disclosure in the methodology group:

> "Although these estimates are only based on a single language pair, the models and test sets
> are relatively diverse, and we expect that these estimates will generalize, though better
> estimates could be obtained by fitting this distribution to a new domain of interest."

The shape to copy: name the restriction, state what mitigates it, name what would settle it.
Three clauses, one sentence, no defensive apparatus.

**Card et al., §5.2**, on the convenience basis of its own parameters:

> "To better characterize the typical variation in human evaluations, we rely on a convenience
> sample of several large datasets to estimate these parameters and use them in our simulations
> as a proxy for what we might observe in practice."

**van der Lee et al., §3**, two arms merged on a null, disclosed:

> "We did not observe noticeable differences in evaluation practices between INLG and ACL, which
> is why they are merged for the discussion of the bibliometric study."

**Howcroft et al., §3.3**, a selected-subset reporting choice made visible:

> "We computed, and Table 2 reports, three sets of IAA scores on the V2.0 annotations: for all
> nine annotators separately ('9 solo'), for the 4 consensus annotations ('4 duo'), and for the
> 5 annotators whose solo annotations agreed most with everyone else's, shown in the '5 best'
> column."

**Dror et al., Bowman & Dahl, Ethayarajh & Jurafsky**: NONE FOUND.

---

# Part II. LLM self-correction and revision literature (6 sources)

This is the paper's own neighbourhood, and it is where the norms are weakest. Fetched
2026-09-06 as arXiv HTML full text; no access failures.

| # | Source | ID | Venue |
|---|---|---|---|
| 21 | Huang, Chen, Mishra, Zheng, Yu, Song, Zhou, "Large Language Models Cannot Self-Correct Reasoning Yet" | arXiv 2310.01798v2 | ICLR 2024 |
| 22 | Kamoi, Zhang, Zhang, Han, Zhang, "When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey" | arXiv 2406.01297v3 | TACL 2024 |
| 23 | Madaan et al., "Self-Refine: Iterative Refinement with Self-Feedback" | arXiv 2303.17651v2 | NeurIPS 2023 |
| 24 | Tyen, Mansoor, Carbune, Chen, Mak, "LLMs cannot find reasoning errors, but can correct them given the error location" | arXiv 2311.08516v3 | Findings of ACL 2024 |
| 25 | Sharma et al., "Towards Understanding Sycophancy in Language Models" | arXiv 2310.13548v4 | ICLR 2024 |
| 26 | Shinn, Cassano, Berman, Gopinath, Narasimhan, Yao, "Reflexion: Language Agents with Verbal Reinforcement Learning" | arXiv 2303.11366v4 | NeurIPS 2023 |

## 11. Power analysis: zero of six

None of the six reports a prospective or retrospective power analysis, a minimum detectable
effect, or any sample-size justification on statistical grounds. Sample sizes are justified by
cost, API usage limits, or annotator time. One paper (Self-Refine) reports confidence intervals,
in an appendix. One (Sharma et al.) reports standard errors and Bayesian credible intervals.

## 12. Small-cell and unbalanced disclosure, verbatim

**Huang et al. (arXiv 2310.01798v2), §3.1 "Test Models and Setup"**, the unequal-n design, stated
without being named as unbalanced:

> "For GPT-3.5-Turbo, we employ the full evaluation set. For other models, to reduce the cost, we
> randomly sample 200 questions for each dataset (100 for HotpotQA) for testing."

**Huang et al., §3.3, footnote 1**, a small cell used as grounds to withhold an analysis:

> "We omit the analysis on HotpotQA because the sample size used in the source paper is quite
> small, which may not produce meaningful statistics."

**Huang et al., §4**, correcting a prior paper's small n:

> "The only distinction is that, to reduce result variance, we test on the complete test set of
> GSM8K, compared to their usage of 100 examples."

**Madaan et al. (arXiv 2303.17651v2), Appendix L.2:**

> "Due to budget constraints, we run Self-Refine for N=5 iterations."

> "We also ask human annotators to edit a 60-example subset to assess human performance on this
> task."

**Madaan et al., Table 2 caption**, an ablation in which rows use different base models, disclosed
only in the caption:

> "These experiments were performed with ChatGPT (Code Optimization and Sentiment Reversal) and
> GPT-3.5 (Acronym Generation), and metrics used are defined in Section 3.2."

**Tyen et al. (arXiv 2311.08516v3), §2.1.1**, the model to copy for a deliberately skewed design:

> "Before annotation, we sample a set of 300 traces for each task, where 255 (85%) are
> incorrect_ans, and 45 (15%) are correct_ans. Since human annotation is a limited and expensive
> resource, we chose this distribution to maximise the number of steps containing mistakes and to
> prevent over-saturation of correct steps. We also include some correct_ans traces because some
> may contain logical errors despite the correct answer, and to ensure that the dataset included
> examples of correct steps that are near the end of the trace. To account for this skewed
> distribution, results in section 4 are split according to whether the original trace is
> correct_ans or not."

The last sentence is the whole technique: a skew is disclosed together with the analysis change
made to answer it. That is what the paper's balanced panel needs, and it already has the
equivalent (pooled triangulation against the panel estimate).

**Tyen et al., Table 4 caption**, missing model cells:

> "Due to cost and usage limits, we are unable to provide results indicated by -."

**Tyen et al., Figure 1 caption**, models dropped from a figure for missing data:

> "Graph of mistake location accuracies for each prompting method (excluding GPT-4-Turbo and
> Gemini Pro which we do not have all results for)."

**Tyen et al., §3.2 footnote 7**, a skew distorting an aggregate:

> "Note that the traces in BIG-Bench Mistake are sampled to contain more incorrect_ans traces than
> correct_ans traces (and therefore more incorrect_mis traces than correct_mis traces), so the
> overall mistake location accuracy appears higher for per-step prompting in Table 4, despite the
> poor accuracy for correct_mis traces."

**Tyen et al., §4.1**, on declining to report a contaminated aggregate:

> "This gives a clearer picture than the overall accuracy_ans, which would be skewed by the
> proportion of traces that were originally correct_ans (15%) and incorrect_ans (85%)."

**Sharma et al. (arXiv 2310.13548v4), §4.3 "Dataset"**, the strongest self-limiting statement in
Part II:

> "We create a proof-of-concept dataset of 266 misconceptions."

> "Note that this dataset is an initial proof-of-concept; for a definitive evaluation, we recommend
> a larger dataset with more comprehensive fact-verification."

**Shinn et al. (arXiv 2303.11366v4), Table 3 caption**, a whole ablation restricted to one model and
a hardest-subset, disclosed only in the caption:

> "Pass@1 accuracy for various compromised approaches on the Reflexion approach using GPT-4 as the
> base model on HumanEval Rust - 50 hardest problems"

**Shinn et al., Appendix B.1**, a negative experiment terminated early:

> "We test a two-shot ReAct + Reflexion agent in 100 environments. However, after only four trials,
> we terminate the runs as the agent does not show signs of improvement."

## 13. Minimum cell size rules: zero of six

No paper in Part II states a numeric floor below which it declines to test or report. The closest
is a performance floor rather than a sample-size floor:

**Tyen et al., §5.1:**

> "We can see that the losses in delta-accuracy begins to plateau at 65%."

The Kamoi et al. TACL survey is the notable absence. Its two normative checklists (Tables 7 and 8)
contain roughly fifteen Required and Recommended items, and none concerns evaluation-set size,
number of models, number of datasets, per-cell n, or any measure of uncertainty. Its only
minimum-size item concerns training data:

> "Evaluating the minimum required size of training data that enables self-correction."

**Reading for this paper.** Its "-- ($n < 5$)" table entry is a stated floor that no paper in its
own subfield states. That is worth one methods sentence.

## 14. One-arm dependence, verbatim: the crux catalogue

**Madaan et al., Appendix J**, a universal main claim disaggregated only in an appendix:

> "We find that nearly all of GPT-4 gains are statistically significant, ChatGPT gains are
> significant for 4 out of 7 datasets, and GPT-3.5 gains are significant for 3 out of 7 datasets."

Against the main-text §3.3 claim:

> "Self-Refine consistently improves over base models across all model sizes, and additionally
> outperforms the previous state-of-the-art across all tasks."

This is the failure mode the paper must avoid: a "consistently, all models" claim in the body with
the per-model significance breakdown out of sight. The paper's existing sentence in `results_v2.tex`
already refuses this: "We do not claim 'all models degrade'; we claim that among models that
continue revising, the only powered comparison (Llama, n = 45) shows significant degradation."

**Madaan et al., §4**, on the one open model tried:

> "While Vicuna-13B is capable of generating initial outputs, it struggles significantly with the
> refinement process."

**Shinn et al., Appendix A**, a null on the only open model, reframed as a property of models
rather than a bound on the claim:

> "We further investigated the applicability of trial-and-error problem-solving with models of
> various strengths. We found that the ability to specify self-corrections is an emergent quality
> of stronger, larger models."

(starchat-beta: baseline pass@1 0.26, Reflexion pass@1 0.26. The only standard deviations reported
anywhere in that paper are attached to this null.)

**Tyen et al., §4**, a single-model correction design, disclosed in the body:

> "For our experimental results below, we specifically use the same model (PaLM 2 Unicorn) to
> correct the traces it originally generated, to test its ability to self-correct."

**Tyen et al., §4.2 Discussion**, the closest match in the whole corpus to what this paper needs:

> "As our dataset is highly skewed and only contains 45 correct_ans traces per task, we leave to
> future work a more comprehensive assessment of backtracking, as well as the development of more
> sophisticated ways to incorporate mistake location information into the self-correction loop."

**Tyen et al., §3.1 footnote 6**, a self-evaluation confound removing one model from interpretation:

> "Note that the traces in our dataset are generated using PaLM 2 Unicorn and are sampled according
> to whether the final answer was correct or not. Therefore, we expect that using PaLM 2 itself to
> do mistake finding will produce different and likely biased results."

This is the exact analogue of the paper's evaluator-judges-itself issue with Claude Sonnet 4, and
it is handled in one footnote sentence plus a call for further work.

**Sharma et al., §3.3**, a primary effect size attributed to one model, with the spread named:

> "The user suggesting an incorrect answer can reduce accuracy by up to 27% (LLaMA 2; Fig. 3)."

> "We find consistent trends across all of the assistants (e.g., suggesting an incorrect answer
> reduces accuracy), but the effect sizes differ by assistant, with GPT-4 being the most robust."

**Sharma et al., figure captions**, an arm that does not show the effect, named in the caption:

> "All models except GPT-4 admit mistake on the vast majority of questions."

> "All models except GPT-4 change answers on many questions."

**Sharma et al., §4.1**, a ranking claim qualified rather than asserted:

> "Nevertheless, in Appendix B, we perform a sensitivity analysis and find that matching a user's
> beliefs, biases, and preferences is consistently one of the most predictive features of human
> preferences. However, it is not consistently the most predictive feature - the exact ranking
> depends on the specific experimental condition."

**Kamoi et al., §4**, a negative universal stated with its scope condition attached:

> "Consequently, we conclude that no major work shows successful self-correction of responses from
> LLMs using feedback generated by prompting themselves under fair settings in general tasks."

## 15. Hedging vocabulary in Part II

| Word or phrase | Source | Containing phrase, verbatim |
|---|---|---|
| "quite small, which may not produce meaningful statistics" | Huang et al. fn 1 | "the sample size used in the source paper is quite small, which may not produce meaningful statistics" |
| "to reduce the cost" | Huang et al. §3.1 | "For other models, to reduce the cost, we randomly sample 200 questions" |
| "indicative of" | Huang et al. §3.2 | "the results can only be regarded as indicative of an oracle's performance" |
| "Due to budget constraints" | Madaan et al. App. L.2 | "Due to budget constraints, we run Self-Refine for N=5 iterations." |
| "Due to cost and usage limits" | Tyen et al. Table 4 caption | "Due to cost and usage limits, we are unable to provide results indicated by -." |
| "we leave to future work" | Tyen et al. §4.2 | "we leave to future work a more comprehensive assessment of backtracking" |
| "proof-of-concept" | Sharma et al. §4.3; Tyen et al. Limitations | "We create a proof-of-concept dataset of 266 misconceptions."; "intended as a proof-of-concept" |
| "for a definitive evaluation, we recommend a larger dataset" | Sharma et al. §4.3 | as quoted above |
| "may be unreliable due to collinearity" | Sharma et al. §4.1 fn 2 | "This suggests their individual effects may be unreliable due to collinearity, so we report their combined effect." |
| "initial evidence" | Tyen et al. Conclusion | "We show initial evidence that a dedicated classifier for mistake finding can overcome this bottleneck." |
| "we raise caution" | Kamoi et al. §5.1 | "we raise caution that the way of using external tools or knowledge influences the research questions we can verify" |
| "only true for certain tasks" | Kamoi et al. §7 | "is only true for certain tasks whose verification is exceptionally easy" |

The words "directional", "suggestive" and "illustrative" do not appear as hedges on a small cell
anywhere in Part II. "Exploratory" does not appear either. The operative vocabulary is
**cost-attributed** ("due to cost", "due to budget constraints", "to reduce the cost"),
**status-attributed** ("proof-of-concept", "initial evidence"), and **deferral**
("we leave to future work", "further work is needed").

## 16. Where the disclosure sits in Part II

| Paper | Limitations section exists | Does it name small n or skew? | Does it name model coverage? |
|---|---|---|---|
| Huang et al. | Yes (§7, ICLR-style) | No | No |
| Kamoi et al. | **No** ("limitation" appears zero times) | n/a | n/a |
| Madaan et al. | Yes (§6) | No | Partly (closed-source only) |
| Tyen et al. | **Yes, ACL-mandated** | **Yes** | No |
| Sharma et al. | **No** | n/a | n/a |
| Shinn et al. | Yes (§5) | No | No |

Only Tyen et al. names skewed sampling in its Limitations section, and it is the only ACL-venue
paper of the six. Verbatim, the relevant paragraph:

> "Another limitation is that our paper does not experiment with backtracking on the original
> datasets on BIG-Bench, only showing results on the limited set that we sampled in a skewed
> manner, in order to maximise the value of the human annotators' time. We leave the full
> evaluation to future work as this is beyond the scope of this paper, which is intended as a
> proof-of-concept to show the importance of mistake-finding."

Everywhere else in Part II the sample-size disclosures live in body text, footnotes, table
captions, figure captions and appendices, never consolidated. Tallied across the six papers,
the placements located were: body text 13, appendix 9, table or figure caption 6, footnote 3,
Limitations section 1.

## 17. Annotators in Part II

| Paper | Annotators | Items | Raters per item | Agreement reported |
|---|---|---|---|---|
| Huang et al. | none (no human eval) | -- | -- | -- |
| Kamoi et al. | none (survey) | -- | -- | -- |
| Madaan et al. | **count never stated**; annotators are the authors | 150 per dataset; 100 for dialogue; 60 for code | not stated | none |
| Tyen et al. | **count never stated** | 300 traces per task, 4 tasks | "at least 3" | **Krippendorff's alpha 0.979 to 0.998** |
| Sharma et al. | **count never stated** (plotted only) | 266 misconceptions, 1,330 comparisons | 5 | none |
| Shinn et al. | none | -- | -- | -- |

Three of the six run a human evaluation. **None of the three states how many people did the
rating.** Two of the three report no agreement statistic at all.

**Madaan et al., Appendix C:**

> "The A/B evaluation in our study was conducted by the authors, where a human judge was presented
> with an input, task instruction, and two candidate outputs generated by the baseline method and
> Self-Refine."

**Tyen et al., §2.1.1:**

> "Each trace is annotated by at least 3 annotators. If there are any disagreements, we take the
> majority label. We calculate Krippendorff's alpha (Hayes and Krippendorff, 2007) to measure
> inter-rater reliability (see Table 3)."

**Sharma et al., Appendix D.3:**

> "We collected 5 responses for 266 misconceptions, which overall is 1330 preference comparisons."

---

# Part III. Human evaluation and LLM-as-judge literature (7 sources)

Fetched 2026-09-06 as arXiv or ACL Anthology full text. No access failures.

| # | Source | ID | Venue |
|---|---|---|---|
| 27 | Zheng et al., "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena" | arXiv 2306.05685v4 | NeurIPS 2023 D&B |
| 28 | Chiang & Lee, "Can Large Language Models Be an Alternative to Human Evaluations?" | arXiv 2305.01937v1 | ACL 2023 |
| 29 | Clark, August, Serrano, Haduong, Gururangan, Smith, "All That's 'Human' Is Not Gold" | ACL 2021.acl-long.565 / arXiv 2107.00061 | ACL 2021 |
| 30 | Elangovan, Liu, Xu, Bodapati, Roth, "ConSiDERS-The-Human Evaluation Framework" | arXiv 2405.18638v2 | ACL 2024 |
| 31 | Thomson & Reiter, "A Gold Standard Methodology for Evaluating Accuracy in Data-To-Text Systems" | arXiv 2011.03992v1 | INLG 2020 |
| 32 | Karpinska, Akoury, Iyyer, "The Perils of Using Mechanical Turk to Evaluate Open-Ended Text Generation" | arXiv 2109.06835v1 | EMNLP 2021 |
| 33 | Calderon, Reichart, Dror, "The Alternative Annotator Test for LLM-as-a-Judge" | ACL 2025.acl-long.782 / arXiv 2501.10970 | ACL 2025 |

## 18. Power analysis in Part III

**Clark et al. (2021), §2.3 "Participants"**, the only own-study power analysis in this group and
the closest venue-matched precedent for the paper:

> "To have adequate power in our analyses (based on a power analysis with beta=0.8; Card et al.,
> 2020), we had 130 different evaluators for each of the 6 task settings (3 domains x 2 models).
> Each participant evaluated 5 texts each, giving us a total of 780 participants and 3,900 text
> evaluations."

One clause, in Methods, citing Card et al. The effect size, the alpha and the test are not stated.
This is what an ACL-venue power statement looks like when it exists.

**Calderon, Reichart, Dror (2025)**, an entire ACL 2025 paper devoted to how few annotators and how
few items are defensible. §1:

> "This procedure is simple and requires minimal effort to apply; it involves comparing the LLM to
> a small group of human annotators (at least three) on a modest subset of examples (between 50 and
> 100)."

§5.1 "The Number Of Instances":

> "Regarding the recommended number, beyond the minimum requirement of 30 instances to satisfy the
> normality assumption of the t-test, Figure 2 shows that for epsilon=0.2, in most cases, the LLM
> begins to pass the test before annotating 100 instances, and in half even before 50 instances."

> "the winning rate omega strongly depends on the number of instances. This is because omega
> reflects the number of rejected hypotheses (i.e., the number of annotators the LLM wins), and
> more instances increase the power of the statistical test and the likelihood of rejecting a false
> null hypothesis (the human wins)."

**Zheng et al., Chiang & Lee, Elangovan et al., Thomson & Reiter, Karpinska et al.**: NONE FOUND.
Karpinska et al. justify their n=3 raters and n=200 items by matching the field's modal
configuration, in order to critique it, rather than by power.

Elangovan et al. name the problem without numbers, §3.2 item 4:

> "Low number of participants, or the sample size of the evaluators, is one of the key contributors
> to poor reproducibility Maxwell et al. (2015); Button et al. (2013)."

## 19. Explicit floors in Part III: the most useful material in the whole corpus

**Calderon, Reichart, Dror (2025), Appendix A**, on why three rather than two annotators:

> "While our procedure can be used with two annotators, we believe it is less reliable. With only
> two, the procedure simply checks whether the LLM aligns more with one annotator than the other,
> lacking a consensus signal. This makes results more sensitive to individual biases. With at least
> three annotators, the procedure better evaluates whether the LLM represents the broader group."

**Same source, Appendix A**, on what to do below the item floor:

> "In this case, the normality assumption of the t-test does not hold, so a non-parametric test,
> such as the Wilcoxon signed-rank test, should be used instead."

**Same source, §3**, on the coarseness a three-rater design imposes:

> "the range of its possible values depends on the number of human annotators, making it a coarse
> measure. For instance, with only three annotators, omega value is limited to 0, 1/3, 2/3"

**Same source, Limitations**, naming the way this kind of design is gamed:

> "A potential misuse of our procedure is intentionally comparing the LLM against weak human
> annotators to demonstrate that the LLM outperforms them and justify its use."

> "To ensure sound and transparent testing, researchers should always report the IAA of the human
> annotators. If the IAA is low, the conclusions drawn from the alt-test are less reliable"

**Karpinska et al. (arXiv 2109.06835), Table 1 caption**, the only enforced suppression rule located
anywhere in the 33-source corpus:

> "Last section omits IAA due to the large number of missing datapoints."

**Thomson & Reiter (arXiv 2011.03992), §3.2**, a design-time collapse of rare categories:

> "We could have used separate categories, but have grouped these together because such statements
> are relatively rare (Section 4.3)."

**Thomson & Reiter, §3.4**, an annotator floor justified by a cost-benefit test rather than power:

> "We recommend asking three annotators to annotate each text; this makes the annotation process
> more robust. We experimented with 5 annotators, but this did not have much impact on results,
> while significantly increasing costs and complexity."

**Clark et al., table captions**, a significance floor applied to many small comparisons:

> "* indicates the accuracies significantly better than random (two-sided t-test, for
> Bonferroni-corrected p<0.00333)."

## 20. One-arm dependence in Part III

**Clark et al. (2021), §3.2**, the best-quantified instance in the whole corpus:

> "Even so, the significant difference in overall performance is mainly contributed by the story
> domain; when comparing evaluators' performance with no training to its Examples training
> counterpart, we see a change of 0.019 and 0.062 mean accuracy in the news and recipe domains,
> respectively, versus 0.086 on the story domain."

And the paired disaggregation admission, §3.2:

> "Breaking down the results by domain, however, we find the Examples accuracy did not
> significantly increase over the no-training accuracy when considering any of the three domains
> individually."

That second sentence is the template for the paper's per-domain problem. Clark et al. keep the
aggregate claim, state plainly that no individual domain reaches significance, and name which
domain supplies most of the aggregate. Three facts, no defence.

**Thomson & Reiter, §4.6**, a by-system comparison disclosed before and after the table:

> "The goal of our experiment was not to compare systems, but nonetheless we show in Table 2 the
> average number of accuracy errors in each system. Please keep in mind that we obtained generated
> stories for different games for each of the three systems (in order to get a more varied set of
> texts in our experiments). If our goal was to compare the systems, we would have generated
> stories for the same game for each system."

> "With these caveats in mind, Table 2 suggests that..."

**Karpinska et al., §3.3**, a result that flips depending on which single arm is the reference:

> "Depending on which reference day we compare the GPT-2 output to, GPT-2 is rated similarly to
> human-written stories in terms of all four properties, which indicates that this evaluation is
> uninformative; nevertheless, the majority of surveyed papers use exactly this task design to
> obtain ratings for model-generated output."

**Zheng et al., §3.3**, declining to draw a conclusion from a small cell:

> "Due to limited data and small differences, our study cannot determine whether the models exhibit
> a self-enhancement bias."

**Chiang & Lee, §4.3**, the weakest instance in the corpus, recorded as a counter-example:

> "However, by scrutinizing the human evaluation results, we find that two teachers rate PWWS higher
> than Textfooler while one teacher rates PWWS lower than Textfooler. This indicates that ChatGPT
> actually agrees with the majority of human experts."

A two-to-one split among three raters reported as agreement with "the majority of human experts."
The paper here should not do this with its own two-annotator reversibility result, and does not:
it reports 56.2% with a confidence interval that includes 50% and declines the claim.

**Calderon et al., §5**, refusing to generalize from the model set:

> "Further experiments across varying model sizes are necessary to support broader claims about
> model openness."

## 21. Annotator distribution: placing two raters on 50 pairs and three on 64 items

This is the part of the deliverable the brief asked to be settled with numbers. Everything here is
verbatim from a fetched source.

### Field-level distributions

**Karpinska, Akoury, Iyyer (arXiv 2109.06835), §2**, a survey of 45 papers using crowd raters for
open-ended generation:

> "An alarming number of papers (14) do not even report the number of raters and/or items (6) used
> for evaluation. Of the remaining, most papers (16) obtain ratings from 3 separate AMT workers per
> item. The most common number of items per evaluation is 100 (14). The number of raters per item
> in other studies ranges from 2 to 11, while the number of items ranges from 12 to 1,000."

**Same source, Table A1**, the tabulated distribution:

> "Number of Items: < 100 items (9); 100 items (14); > 100 items (20); not reported (5)"

> "Number of Raters: < 3 raters (3); 3 raters (16); 5 raters (13); > 5 raters (3)"

**van der Lee et al. (W19-8643), §3.3**, INLG and ACL 2018:

> "14 papers (28%) used an expert-focused approach, meaning that between 1 and 4 expert annotators
> evaluated system output. 13 papers (26%) employed a larger-scale reader-focused method in which
> 10 to 60 readers judged the generated output. We found a median of 4 annotators."

**Same source, §3.4:**

> "Among papers that reported these numbers, we observed a median of 100 items used for human
> evaluation in INLG and ACL papers. The number of items however ranged between 2 and 5,400"

**Card et al. (arXiv 2010.06595), §5.1**, EMNLP 2019:

> "57% of experiments collected 3 annotations per item, which was also the modal number of unique
> annotators."

> "Number of items tested is more consistent: 69% used 100 or fewer, and only 18% used over 200."

**Gehrmann, Clark, Sellam (arXiv 2202.06935), §5**, reporting van der Lee et al. 2021:

> "the median number of generated texts in a human evaluation is 100 items"

### Study-level counts, from papers actually read

| Source | Annotators | Items | Raters per item | Agreement reported |
|---|---|---|---|---|
| Clark et al. 2021 | 780 (study 1), 1,170 (study 2) | 5 texts each; 3,900 and 5,850 evaluations | 130 per cell | Krippendorff alpha near 0; alpha <= 0.11 |
| Zheng et al. 2023 | 58 experts; 2,114 unique IPs | 80 questions; ~3K votes | not stated | agreement rates reported |
| Chiang & Lee 2023 | 3 English teachers (+3 more, +3 for attack task) | 400 stories; 100 title pairs | 3 | Krippendorff alpha |
| Thomson & Reiter 2020 | 3 Turkers, from 18 who attempted | 21 stories | 3 | Fleiss kappa 0.79 |
| Karpinska et al. 2021 | 3 teachers + 3 Upwork teachers, plus crowds | 200 + 200 stories | 3 | Krippendorff alpha, some near 0 |
| Calderon et al. 2025 | 3 to 13 per dataset, across 10 datasets | 120 to 6,400 | 2.05 to 7.27 | Fleiss kappa 0.26 to 0.74 |
| Chatbot Arena 2024 | 2 experts (graduate students) | 160 battles | 2 | 72% to 83% agreement |
| Tyen et al. 2024 | count never stated | 300 traces x 4 tasks | at least 3 | Krippendorff alpha 0.979 to 0.998 |
| Sharma et al. 2023 | count never stated | 266 misconceptions, 1,330 comparisons | 5 | none |
| Madaan et al. 2023 | count never stated; the authors | 150 per dataset; 100; 60 | not stated | none |
| Howcroft et al. 2020 | 9 (the authors) | 165 papers | 2 for consensus rounds | Krippendorff alpha with Jaccard |

**Where this paper sits.** Two annotators on 50 pairs and three raters on 64 items are both inside
the observed distribution and neither is at its floor.

- Two raters is above the "< 3 raters" bucket that holds 3 of Karpinska's 45 papers, meets van der
  Lee et al.'s stated best-practice floor for a qualitative comparison ("at least 2, more is
  better"), and equals the Chatbot Arena expert-validation design (2 experts, 160 items) published
  at ICML 2024.
- Three raters is the modal count in every field survey read: 16 of 45 in Karpinska et al., 57% of
  experiments in Card et al., and the recommended floor in both Thomson & Reiter and Calderon et al.
- Fifty items is below the modal 100 and inside Calderon et al.'s stated adequate range
  ("between 50 and 100"), and above their hard floor of 30 for a t-test. The paper uses a bootstrap
  confidence interval rather than a t-test, which sidesteps the normality condition entirely.
- Sixty-four items likewise sits between Calderon's floor of 30 and the modal 100.

**The exposed point is not the counts.** It is the reliability. The paper's Krippendorff alpha of
0.529 on 64 items and its quadratic-weighted kappas of 0.41 to 0.60 land squarely in the range
van der Lee et al. report as typical ("Agreement in most cases ranged from 0.3 to 0.5"), above the
near-zero alphas Clark et al. and Karpinska et al. report for comparable open-ended judgments, and
below the 0.67 convention that Elangovan et al. argue against applying mechanically:

> "NLG tasks have typically reported relatively low IRA, e.g., average Krippendorff's-alpha of 0.62
> Amidei et al. (2019), the standard interpretation is that experiments with scores less than 0.67
> must be deemed unreliable Marzi et al. (2024)."

> "What is considered as 'low' IRA can vary from task to task, as complex tasks or difficult samples
> tend to have low IRA Kim and Park (2023). This is crucially important for interpreting IRA and is
> particularly relevant for NLG evaluation."

> "Hence, while it is mandatory to measure IRA, it is important to ensure that the scores are
> interpreted in the context of the task."

That last sentence is the citation to reach for when a reviewer calls 0.529 low.

## 22. Hedging vocabulary in Part III

| Word or phrase | Source | Containing phrase, verbatim |
|---|---|---|
| "cannot determine" | Zheng et al. §3.3 | "Due to limited data and small differences, our study cannot determine whether the models exhibit a self-enhancement bias." |
| "small-scale study" | Zheng et al. §4 | "MT-bench represents a small-scale study with controlled human evaluation" |
| "preliminary" | Zheng et al. §3.4 | "show some promising preliminary results in Appendix F" |
| "failed to find any evidence" | Clark et al. §2.4 | "we failed to find any evidence that evaluators' accuracy on any one domain for GPT3 differs from the overall GPT3 accuracy" |
| "mainly contributed by" | Clark et al. §3.2 | "the significant difference in overall performance is mainly contributed by the story domain" |
| "not directly comparable" | Clark et al. §6 | "these results are not directly comparable to ours due to differences in the evaluation setup, data, and participants" |
| "With these caveats in mind" | Thomson & Reiter §4.6 | "With these caveats in mind, Table 2 suggests that..." |
| "at least in principle" | Thomson & Reiter §4.6 | "this does show how our methodology can at least in principle be used to evaluate and compare systems" |
| "uninformative" | Karpinska et al. §3.3 | "which indicates that this evaluation is uninformative" |
| "dubious conclusions" | Karpinska et al. §1 | "exhibits high variance and can lead to dubious conclusions" |
| "coarse measure" | Calderon et al. §3 | "making it a coarse measure. For instance, with only three annotators, omega value is limited to 0, 1/3, 2/3" |
| "less reliable" | Calderon et al. Limitations | "If the IAA is low, the conclusions drawn from the alt-test are less reliable" |
| "taken with a grain of salt" | Calderon et al. Limitations | "if the annotators are deemed unsuitable, the study's results should be taken with a grain of salt" |
| "necessary but not sufficient" | Elangovan et al. §3.2 | "a large group of evaluators and a large test set is necessary but not sufficient to ensure that the study is experiment bias-free" |

**"Directional" appears nowhere in the 33-source corpus as a hedge on a small cell.** Neither does
"illustrative" or "suggestive" in that role. This matters for the paper, which currently uses
"directional" twice. The word is not wrong, but it has no precedent in this literature and a
reviewer will read it as a coinage. The three constructions with precedent are:

1. "mainly contributed by X" plus the disaggregated numbers (Clark et al.)
2. "we leave to future work a more comprehensive assessment" (Tyen et al.)
3. "with these caveats in mind, Table N suggests" (Thomson & Reiter)

## 23. Where the disclosure sits, Part III

| Paper | Named Limitations section | Does it hold the small-n disclosure? |
|---|---|---|
| Zheng et al. | Yes (§6) | No. Scope only. The small-n admission is in §3.3 body. |
| Chiang & Lee | Yes | No. Covers factual knowledge, emotion, visual cues. |
| Clark et al. | No (Ethical considerations only) | n/a. Power statement in Methods; one-arm disclosure in Results; failed arm in a footnote. |
| Elangovan et al. | Yes (§5) | No. Domain customization and cognitive-bias scope only. |
| Thomson & Reiter | No | n/a. Caveats placed inline, twice, bracketing the table. |
| Karpinska et al. | No | n/a. The disclosures are the findings. |
| Calderon et al. | Yes | **Yes.** Low IAA, weak-annotator gaming, data contamination. |

---

# Part IV. HCI and human-subjects computing (6 sources)

Fetched 2026-09-06. One access failure and one substitution, reported in §29.

| # | Source | ID | Venue |
|---|---|---|---|
| 34 | Caine, "Local Standards for Sample Size at CHI" | 10.1145/2858036.2858498 | CHI 2016 |
| 35 | Kay, Nelson, Hekler, "Researcher-Centered Design of Statistics: Why Bayesian Statistics Better Fit the Culture and Incentives of HCI" | 10.1145/2858036.2858465 | CHI 2016 |
| 36 | Jakesch, Bhat, Buschek, Zalmanson, Naaman, "Co-Writing with Opinionated Language Models Affects Users' Views" | arXiv 2302.00560v1 | CHI 2023 |
| 37 | Lee, Liang, Yang, "CoAuthor" | arXiv 2201.06796v2 | CHI 2022 |
| 38 | Buçinca, Malaya, Gajos, "To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making" | arXiv 2102.09692v1 | CSCW 2021 |
| 39 | Vasconcelos, Jörke, Grunde-McLaughlin, Gerstenberg, Bernstein, Krishna, "Explanations Can Reduce Overreliance on AI Systems During Decision-Making" | arXiv 2212.06823v2 | CSCW 2023 |

## 24. Power analysis in HCI: thinner than expected

The premise that HCI reports power more often than NLP is only half right. HCI names power more
often; it reports parameters no more completely.

**Jakesch et al. (arXiv 2302.00560v1), §3.5 "Participant recruitment"**, the fullest statement in
the group, and it still omits alpha, software and the numeric effect size:

> "The sample size was calculated based on effect sizes observed in the pilot studies' post-task
> question, 'Overall, would you say social media is good for society?' at a power of 80%."

**Vasconcelos et al. (arXiv 2212.06823v2)**, the same sentence repeated once per study with no
parameters at all:

> "Our sample size comes from a power analysis done on pilot data."

(§5.4, §6.4, §8.4, §9.5, and parenthesized at §7.4, the study with the smallest cells.)

**Buçinca et al. (arXiv 2102.09692v1)** and **Lee et al. (arXiv 2201.06796v2)**: NONE FOUND. Neither
reports a power analysis, a target power, an alpha, an assumed effect size, or any sample-size
justification. Buçinca et al. state a recruitment target of 260 without rationale.

**Caine (CHI 2016)**, the field's own retrospective calculation, and the number a reviewer of this
paper should be told about:

> "On the other hand, especially for quantitative work, it appears that many studies published at
> CHI are underpowered even to find large effects: a two condition, within-subjects study with 17
> participants (the mean for in-person, within-subjects experiments), has a power of 0.49 to find
> a large effect."

**Kay, Nelson, Hekler (CHI 2016)**, on why HCI runs small studies:

> "Due to limited resources and an emphasis on novelty, HCI studies are often conducted with fewer
> participants than a traditional power analysis would suggest is prudent [10,18]."

> "The traditional solution to the problems associated with low-power studies (and one HCI
> researchers are often admonished to adopt) is to spend resources recruiting more participants. In
> other words, the frequentist solution to low power is not to run low-powered studies."

**None of the six names G*Power or any power software, and none states an alpha in a power context.**
The two full G*Power-style templates in this file come from Part I: Schoenegger et al. and
Schütz et al.

## 25. The CHI sample-size distribution

**Caine (CHI 2016)**, from a census of every user study in the 465 CHI 2014 papers:

> "We find that sample size for manuscripts published at CHI ranges from 1 - 916,000 and the most
> common sample size is 12."

> "The most commonly reported sample size was 12. Fifty-seven studies, a full 10% of all user
> studies, reported a sample size of 12. Twenty percent of studies reported a sample size of ten or
> less, half of studies reported a sample size of less than 18 and seventy percent of studies
> reported a sample size of less than 30."

> "The average sample size for within-subjects experiments (17) was smaller than the average for
> between-subjects (26) or mixed designs (25)."

Table 4: range 1 to 916,000; mean 4,119; SD 42,856; median 18; mode 12.

**Caine's argument against a floor**, which is the citation to reach for if a reviewer asks for one:

> "That is, there is no meaningful cut-off point at which a sample size becomes 'too small',
> inadequate or invalid [6]."

> "Therefore, while sample size can be justifiably criticized as inadequate to determine whether
> there is a reliable effect at a certain level of confidence, there is no point at which a sample
> size can be justifiably criticized as 'too small' without qualification."

## 26. Unbalanced and small cells in HCI, verbatim

**Buçinca et al. (arXiv 2102.09692v1), §3.6 "Design and Analysis"**, the most direct treatment of an
unbalanced panel in the entire corpus:

> "Mixed-effects models also properly handle the imbalance in our data (Spilke et al., 2005), due to
> participants being randomly assigned to conditions and not all participants having interacted with
> both categories (CFF and SXAI). Note that unbalanced data can lead to fractional denominator
> degrees of freedom."

Imbalance is not apologized for. It is named, the estimator that tolerates it is named, and the
statistical consequence is stated in one clause.

**Buçinca et al., §3.5 "Participants"**, exclusions and arms collected but not reported:

> "Out of 260 participants, 49 participants were filtered as they selected as an ingredient to
> replace one that was not on the plate for more than 55% of the questions. We noticed that these
> excluded participants had also an accuracy of 0 on the task. An additional 12 participants were
> excluded from the analyses as they were assigned to only exploratory conditions not reported in
> the results."

> "For only one of the participants, the highest level of education received was a pre-high school
> degree."

**Buçinca et al., §3.6**, a non-equivalent comparison arm disclosed rather than hidden:

> "For performance on incorrect model predictions, we also added no AI category to the analysis even
> though participants in that category did not see any model predictions."

**Vasconcelos et al., §7.4 "Participants" (Study 3)**, cells of 15 and 16 against three cells of 85:

> "We recruited an additional N=31 participants from Profilic, using the same exclusion criteria as
> in Study 1. All were placed in the hard condition. 16 were in the incomplete explanation
> condition; 15 were in the salient explanation condition. (Our sample size comes from a power
> analysis done on pilot data.) There were N=85 in each of the prediction only, highlight
> explanation, and written explanation conditions from study 1 and 2. In total, there were N=286
> participants in this study."

**Vasconcelos et al., §7.5 "Results"**, the strongest small-cell handling rule in the corpus, and
the closest published precedent for the paper's per-domain problem:

> "Because we didn't pre-register any hypotheses for this study, we report the means and credible
> intervals for all the pairwise comparisons here, but don't indicate whether the differences are
> credible."

That is: report the estimates and the intervals, withhold the verdict. It is a stronger and cleaner
move than labelling a cell "directional", and it has a CSCW 2023 precedent.

**Vasconcelos et al., §7.6 "Summary"**, the small-cell hedge attached to the claim itself:

> "Although there is more work to be done whether this is the case with more participants, these
> initial findings suggest that people are unlikely to agree with an AI if they know it is
> incorrect."

**Vasconcelos et al., Appendix §12.3.2**, an abandoned study reported rather than buried:

> "Our hypotheses with the prior pre-registration did not appear to have a large effect, so we ended
> the study early at a number of participants far lower than pre-registered; therefore, we do not
> report these values."

**Jakesch et al., §3.5**, unequal arms reported as plain counts with no defence:

> "We recruited 1,506 participants (post-exclusion) for the writing task, corresponding to 507, 508,
> and 491 individuals in the control, techno-optimist, and techno-pessimist treatment groups,
> respectively."

> "Participants who failed the pre-task attention check (8%) were excluded. Six percent of
> participants admitted to the task did not finish it."

**Jakesch et al., §3.4**, unequal labels per item, disclosed with the agreement statistic:

> "We collected one to two labels for each sentence participants wrote and collected labels for a
> sample of the writing assistant's suggestions. In sentences where we collected multiple labels,
> the labels provided by different raters agreed 84.1% of the time (Cohen's kappa=0.76)."

**Lee et al. (arXiv 2201.06796v2), §4.3.1**, attrition and a covariate cell of one:

> "From 201 writers who participated in our qualification round, we qualified 100 writers. Among
> these writers, 63 writers participated in the main round, where 62 writers were native English
> speakers and one was not."

**Lee et al., §4.4**, unequal cells across the two writing types:

> "The dataset contains 830 stories written by 58 writers for creative writing and 615 essays
> written by 49 writers for argumentative writing."

**Caine, Results, Outlier Analysis**, an explicit exclusion rule with its arithmetic shown:

> "Based on this analysis we eliminated all cases that were more than three interquartile ranges away
> from the first or third quartile and the most extreme 5% that were more than 1.5 interquartile
> ranges away from the first or third quartile. There were 41 studies identified as outliers based
> on sample size by setting (in person vs. remote). We omitted these outliers from further analysis
> leaving 519 studies as the final dataset"

**Kay, Nelson, Hekler**, on what small samples do to an estimate, which is the argument for reporting
per-domain cells as intervals rather than as point verdicts:

> "With a frequentist analysis, this increases the probability of what Gelman calls a magnitude error
> [8]: because the confidence intervals are so wide, the only effects that reach significance are
> those that overestimate the effect size."

> "At only 20 participants per condition, in the frequentist world a large effect size (a log odds
> ratio of nearly 1.5) is required to reject the null hypothesis - 3 times the known (because we
> defined it) effect size."

## 27. One-arm dependence in HCI

**Buçinca et al., §6 "Discussion"**, the whole main result qualified in one sentence:

> "The significant improvements in performance stemming from cognitive forcing functions, when
> disaggregated, held mostly for people with high NFC."

**Buçinca et al., §4.1**, an effect that exists at the category level and not for any single design:

> "For all the metrics, there were no significant differences among conditions within either category
> (i.e., simple explainable AI and cognitive forcing functions)."

**Vasconcelos et al., §5.6 "Summary"**, the paper's central claim named as resting on one arm:

> "In summary, explanations do not produce an observable reduction in overreliance in easy or medium
> tasks, but do reduce overreliance in the hard task."

**Vasconcelos et al., Figure 7 caption**, the same in a caption:

> "In the easy and medium-difficulty tasks, we find no differences between prediction and explanation
> conditions. We find that explanations reduce overreliance in the hard task condition."

**Lee et al., §5.1.3**, an effect present in one writing type only:

> "Writing sessions with GPT-3 with high randomness received slightly higher equality and mutuality
> scores in argumentative writing, while the difference was not statistically significant in creative
> writing."

**Lee et al., §5.1.2**, a difference confounded with two factors at once, disclosed:

> "We suspect that this difference could be due to the different writing types (e.g. stories are more
> likely to need new names and locations) and the different sets of decoding parameters (temperature
> and frequency penalty as shown in Figure 2)."

**Jakesch et al., §5.3**, single-topic and single-model restrictions:

> "We only tested whether a language model affected participants' views on a single topic."

> "Further, we only looked at one specific implementation of a writing assistant powered by GPT-3."

**Jakesch et al., §4.2**, heterogeneity including an arm that contributes nothing:

> "About one in four participants did not accept any model suggestion, and one in ten participants
> had more than 75% of their post written by the model."

## 28. Hedging vocabulary in HCI

| Word or phrase | Source | Containing phrase, verbatim |
|---|---|---|
| "As appropriate for an early study" | Jakesch et al. §5.3 | "As appropriate for an early study, our experiment has several limitations" |
| "initial evidence" | Jakesch et al. §5.3 | "Our results provide initial evidence that language models in writing assistance tasks affect users' views." |
| "exploratory" | Buçinca et al. §3.4; Vasconcelos et al. §7 | "3 additional exploratory designs not reported in this paper"; "This experiment is exploratory and therefore does not have pre-registration." |
| "held mostly for" | Buçinca et al. §6 | "when disaggregated, held mostly for people with high NFC" |
| "albeit not significantly so" | Buçinca et al. | "Low NFC participants reported on average higher trust (M=3.92) than high NFC participants (M=3.70), albeit not significantly so" |
| "don't indicate whether the differences are credible" | Vasconcelos et al. §7.5 | "we report the means and credible intervals for all the pairwise comparisons here, but don't indicate whether the differences are credible" |
| "initial findings suggest" | Vasconcelos et al. §7.6 | "these initial findings suggest that people are unlikely to agree with an AI if they know it is incorrect" |
| "notable" (in place of "significant") | Vasconcelos et al. §5.5 etc. | "We adopt the convention of saying that a comparison is notable if the 95% credible interval of the posterior distribution excludes 0" |
| "preliminary evidence" | Lee et al. §5.2 | "CoAuthor may provide preliminary evidence for formulating hypotheses regarding interaction design" |
| "further experiments with interventions are necessary" | Lee et al. §5.2 | "Note that we use simplified definitions and generate hypotheses based on correlations. To validate the hypotheses, further experiments with interventions are necessary." |
| "no meaningful cut-off point" | Caine, Introduction | "there is no meaningful cut-off point at which a sample size becomes 'too small', inadequate or invalid" |
| "magnitude error" | Kay et al. | "this increases the probability of what Gelman calls a magnitude error" |

"Not powered to detect", "directional", "should be interpreted as suggestive" and "we treat these as
descriptive" appear in **none** of the six HCI sources.

## 29. Access failures and substitutions

**Cockburn, Gutwin, Dix (2018), "HARK No More: On the Preregistration of CHI Experiments", CHI 2018,
DOI 10.1145/3173574.3173715: NOT OBTAINED.** Routes attempted and their outcomes: ACM Digital
Library PDF returned HTTP 403; Semantic Scholar reports `isOpenAccess: false` and
`openAccessPdf.status: CLOSED`; OpenAlex reports `oa_status: closed` with no repository full text;
the first author's own paper page hosts abstract only; the Birmingham and Swansea institutional
repositories hold metadata with no deposited manuscript; ResearchGate returns 403; no arXiv preprint
exists. **Nothing in this file is attributed to that paper.**

**Substitution made:** Kay, Nelson, Hekler (CHI 2016), "Researcher-Centered Design of Statistics",
read in full from the first author's hosted PDF. Same venue, adjacent year, same problem space
(statistical practice norms at CHI, small-n studies, the value of estimates over verdicts). It does
not substitute for the preregistration content of the target.

**Other access notes.** Card et al. (2020): the ACL Anthology landing page returned HTTP 000; the
direct PDF path succeeded, and the arXiv version was also read because it carries Appendices A to I
that the Anthology version omits. Marie et al., Gehrmann et al. and HELM were read from PDF after
the arXiv abstract page proved to contain metadata only. Chatbot Arena was read from PDF for the
same reason. Peng et al. (Copilot RCT) was read only through an ar5iv HTML rendering, so its
quotations are the least directly verified in this file and should be re-checked against the PDF
before any of them is cited.

---

# Part V. Counts and application

## 30. Mechanical counts across the corpus

**Corpus size.** 39 items fetched: 36 research papers and 3 venue policy documents. Of the 36
papers, 21 report an empirical study with cells of their own; the remaining 15 are meta-analyses,
surveys, position papers, or methodological simulations.

### Power analysis

| Count | Value |
|---|---|
| Empirical papers reporting a power analysis for their own design | **5 of 21** |
| Of those, reporting alpha, effect size, target power and resulting N | **2 of 21** |
| Methodological papers whose subject is power in the field | 4 (Card et al., Howcroft & Rieser, Caine, Calderon et al.) |
| Empirical papers naming a power software package | **0 of 21** other than Schütz et al. (G*Power 3.1.9.7) |
| Papers in the self-correction literature (Part II) reporting any power analysis | **0 of 6** |

The five are Schoenegger et al., Schütz et al., Clark et al., Jakesch et al., and Vasconcelos et al.
Only the first two give the full parameter set. Vasconcelos et al. assert "a power analysis done on
pilot data" five times without a single parameter.

### Base rates reported inside the corpus

| Statistic | Source, verbatim reference |
|---|---|
| 1 of 97 human evaluation experiments at EMNLP 2019 performed a power analysis | Card et al., Appendix H.1 |
| 0 of 66 papers at ACL, INLG and EMNLP 2021 estimated how many annotations to collect | Gehrmann et al., §5 |
| 24% of EMNLP 2019 human evaluation experiments reported any significance testing | Card et al., Appendix H.1 |
| 23% of NLG papers report statistical analyses of significance | van der Lee et al. 2021, via Gehrmann et al. §5 |
| 33% of INLG and ACL 2018 papers with human evaluation report a statistical analysis | van der Lee et al. 2019, §3.6 |
| Never more than 65% of MT papers in any year performed significance testing | Marie et al., §3.2 |
| 3 of 110 ACL 2017 papers using multiple datasets corrected for multiplicity | Dror et al., §4 |
| 12.5% of NLG papers with human evaluation reported inter-annotator agreement | van der Lee et al. 2019, §3.3 |
| 18% of papers using human evaluation report IRA | Amidei et al. 2019, via Elangovan et al. §3.2.1 |
| Mode sample size at CHI 2014 is 12; median 18; 70% below 30 | Caine, Results |
| Mean within-subjects CHI experiment has power 0.49 for a large effect | Caine, Discussion |

### Small or unbalanced cell disclosure

| Count | Value |
|---|---|
| Empirical papers disclosing at least one small, sparse or unbalanced cell | **21 of 21** |
| Empirical papers naming the cause of the imbalance (cost, API limits, annotator time) | 8 |
| Empirical papers naming the estimator chosen to tolerate the imbalance | **1** (Buçinca et al., mixed-effects models) |
| Empirical papers changing the analysis in response to a disclosed skew | **2** (Tyen et al., splitting by trace correctness; Vasconcelos et al., withholding credibility verdicts) |

### Minimum cell size rules

| Count | Value |
|---|---|
| Papers stating a numeric floor below which they decline to test | **0 of 36** |
| Papers stating a numeric annotator or item floor as a recommendation | **3** (van der Lee et al.: at least 2, three or more; Thomson & Reiter: three; Calderon et al.: three annotators, 30 instances, 50 to 100 recommended) |
| Papers enforcing a suppression rule on a reported statistic | **1** (Karpinska et al., Table 1 caption: "Last section omits IAA due to the large number of missing datapoints") |
| Papers stating an analysis exclusion rule with its arithmetic | 2 (Card et al. footnote 11; Caine, Outlier Analysis) |
| Papers arguing explicitly against a floor | 1 (Caine) |

**This is the finding with the most direct bearing on the paper.** Its table entry
"-- ($n < 5$)" is a stated, applied, visible reporting floor, and **no paper in this
39-source corpus does the same for a significance test.** Three papers recommend floors; one
suppresses a statistic in a caption; none pre-states a testing floor and applies it in a results
table. The paper is ahead of its literature on this point and should say so in one methods clause
rather than leave it as a dash.

### Results produced disproportionately by one arm

| Count | Value |
|---|---|
| Empirical papers disclosing some form of single-arm or single-condition dependence | **18 of 21** |
| Of those, quantifying the dominant arm's contribution | **4** (Clark et al., Schoenegger et al., Sharma et al., Madaan et al.) |
| Papers separating the claim that survives from the claim that does not | **3** (Schoenegger et al., Tyen et al., Kamoi et al.) |
| Papers where the disaggregation appears only in an appendix | **3** (Madaan et al., Shinn et al., Sharma et al. in part) |

### Where the disclosure sits

Placements located in this sweep. A single paper often discloses in several places, so these are
placements, not papers.

| Location | Count |
|---|---|
| Results or Discussion body text | 14 |
| Methods or Setup body text | 11 |
| Table or figure caption | 10 |
| Appendix | 8 |
| Footnote | 7 |
| Named Limitations section | 6 |

Of the 13 empirical papers in the corpus that have a named Limitations section, **4 place the
small-cell or single-arm disclosure there**: Tyen et al., Calderon et al., Schoenegger et al., and
Schütz et al. Nine do not, including both HCI papers with a titled Limitations subsection
(Jakesch et al. §5.3 and Vasconcelos et al. §10.4), neither of which mentions sample size, cell size
or power.

**Reading for this paper.** Its eight-item Limitations paragraph in `discussion.tex` already places
five of these disclosures in the Limitations section. That is more than any paper in this corpus
does. The exposure is not under-disclosure; it is that the same facts are stated three times, in
`methods.tex`, `results_v2.tex` and `discussion.tex`, which reads as anxiety rather than rigour.
See §31.

### Hedging vocabulary, by frequency across the corpus

Terms located as hedges on a small or unbalanced cell, with the number of distinct sources using
each:

| Term | Sources |
|---|---|
| "exploratory" | 6 |
| "underpowered" | 5 |
| "preliminary" / "initial evidence" / "initial findings" | 6 |
| "we leave to future work" / "further work is needed" / "further experiments are necessary" | 9 |
| "proof-of-concept" | 3 |
| "due to cost" / "due to budget constraints" / "due to cost and usage limits" | 4 |
| "should be treated with caution" / "taken with a grain of salt" | 2 |
| "less power" / "less reliable" | 3 |
| "cannot determine" / "failed to find any evidence" | 2 |
| **"directional"** | **0** |
| **"suggestive"** (as a hedge on a cell) | **0** |
| **"illustrative"** (as a hedge on a cell) | **0** |
| **"not powered to detect"** | **0** |
| **"we treat these as descriptive"** | **0** |

The four terms the brief anticipated are absent from all 39 sources in this sense. The literature's
vocabulary is narrower and more concrete: it names the **cause** (cost, annotator time, API limits),
the **status** (exploratory, proof-of-concept, initial), and the **remedy** (future work,
replication, more instances).

## 31. How this paper's five disclosures should be worded

Each item below states the fact, the closest published precedent, the wording to use, and where to
put it. The governing principle from the corpus: **name the cell size inside the sentence that
reports the estimate, name the cause, name what would settle it, and say it once.**

### 31.1 The balanced panel is 90% one model, with three models at zero

**Precedent.** Schoenegger et al. §5, separating the surviving claim from the dependent one:
"While the main results of advanced LLM augmentation outperforming a non-forecasting basic LLM
control holds, the conclusion that different prompts perform differently relies on this outlier and
necessitates further research and replication." And HELM §1 for the zero-overlap phrasing: "with
some prominent models not sharing a single scenario in common."

**What the paper already has, in `results_v2.tex` line 78, is better than every precedent in this
corpus except Schoenegger et al.:**

> "We do not claim 'all models degrade'; we claim that among models that continue revising, the only
> powered comparison (Llama, $n = 45$) shows significant degradation."

**Recommendation: keep that sentence and cut its repetitions.** The same fact currently appears in
`methods.tex` line 71 ("The balanced panel is 90% Llama (45/50); only Llama has sufficient power for
within-model inference"), in `results_v2.tex` line 40 and line 78, and in `discussion.tex` limitation
one. Four statements of one fact reads as pre-litigating an objection. The corpus norm is one
statement at the point of the claim plus one line in Limitations.

Keep: the results sentence quoted above, and a single Limitations clause. Cut the methods repetition
to a bare structural note without the power judgment, since the power judgment belongs where the
estimate is reported.

**One addition worth making.** No paper in the corpus states why the other arms are empty as a
substantive finding rather than a data problem, and the paper can:

> "GPT-4o, DeepSeek and Gemini contribute zero balanced-panel trials, not because they maintain
> quality, but because they stop producing genuine revisions before Turn 5."

That sentence is already in `results_v2.tex`. It converts an empty cell into a result. Protect it.

### 31.2 Per-domain Turn-5 cells of 13 to 30

**Precedent.** Two, and they should be combined.

Clark et al. §3.2, for the disaggregation admission stated plainly:
"Breaking down the results by domain, however, we find the Examples accuracy did not significantly
increase over the no-training accuracy when considering any of the three domains individually."

Padmakumar & He, for the cell size inside the reporting clause:
"albeit with less power as we only collected 10 essays per setup per topic."

**Recommendation.** The paper's current sentence in `results_v2.tex` line 117 works, with one
change. It reads:

> "The aggregate degradation pattern is well-powered; per-domain cliff magnitudes should be read as
> directional estimates, not precise per-domain measurements."

Replace "directional estimates, not precise per-domain measurements" with a construction that has
precedent. **"Directional" appears nowhere in 39 sources.** Two options with precedent:

- Clark-style: "the aggregate degradation is well powered; no single domain cell is large enough to
  support a per-domain magnitude claim on its own."
- Vasconcelos-style, which is stronger and cleaner: report the per-domain deltas with intervals and
  decline the verdict. Their §7.5 wording is "we report the means and credible intervals for all the
  pairwise comparisons here, but don't indicate whether the differences are credible."

The second is preferable if per-domain confidence intervals can be computed. It removes the need for
a hedging adjective entirely: the interval does the hedging.

**The parenthetical about creative writing at n=6 should stay**, and it is well judged. It matches
Vasconcelos et al.'s handling of their n=15 arm: state the estimate, state the cell size, decline the
interpretation, name what would settle it.

### 31.3 The small targeted-feedback cells and the n < 5 rule

**Note on the brief.** The paper does not contain a targeted-feedback subset of n=13. The smallest
targeted-feedback cells are Gemini at n=3 and GPT-4o at n=12
(`results_v2.tex`, Table `tab:targeted-per-model`). The n=13 figure in the paper is the writing
domain's Turn-5 cell (Table `tab:domain-variation`). Both are handled under 31.2 and here.

**Precedent.** There is none for a pre-stated testing floor. Karpinska et al.'s caption is the
closest: "Last section omits IAA due to the large number of missing datapoints." Calderon et al.
supply the argument for why a floor is needed, and Thomson & Reiter supply the design-time analogue.

**Recommendation.** State the rule once, in Methods, in words, before it is applied:

> "Cells with fewer than five observations are reported but not tested; the Gemini targeted-feedback
> cell (n = 3) is the only one this excludes."

This costs one sentence, converts a table dash into a pre-stated decision rule, and makes the paper
the only one in this 39-source corpus with an explicit, applied testing floor. Do not defend the
choice of five. State it and move on.

The existing table caption claim "All five powered models show significant improvement" is accurate
under that rule and should stay.

### 31.4 Two annotators on 50 stripped pairs

**Precedent.** Three, and the paper is comfortably inside all of them.

van der Lee et al., Table 3, the NLG best-practice list:
"For a qualitative analysis, recruit multiple annotators (at least 2, more is better)"

Karpinska et al. §2, the survey of 45 papers:
"The number of raters per item in other studies ranges from 2 to 11, while the number of items
ranges from 12 to 1,000."

Chatbot Arena §6.3, an ICML 2024 paper validating a 240,000-vote leaderboard with two experts:
"To assess the quality of crowdsourced votes, we randomly selected 160 battles between GPT-4-Turbo
and Llama-213B, as well as GPT-4-Turbo and GPT-3.5-Turbo-0613. We then asked experts to label their
preference per comparison."

**Recommendation: report the design plainly and do not apologize for it.** The paper's methods
sentence is already correct in register:

> "Two human annotators independently compared stripped Turn 1 and last-genuine-revision outputs for
> the 50 balanced-panel trials, blind to turn identity and position-randomized. Inter-annotator
> agreement: $\kappa = 0.703$ ($n = 50$)."

Kappa of 0.703 on 50 items is higher than the agreement Clark et al. obtain with 780 evaluators
(Krippendorff alpha near zero) and higher than Karpinska et al.'s crowd alphas. **Add nothing about
the annotator count being small.** The eighth limitation in `discussion.tex` currently says the
reversibility result "is near chance" and reports the interval and the unmet pre-set bar. That is the
right disclosure and it is about the effect, not the sample. Leave it there and do not add a
sample-size caveat next to it, which would raise an objection no reviewer has made.

If a reviewer does raise it, the answer is van der Lee et al.'s stated floor plus the Chatbot Arena
precedent, both quoted above.

### 31.5 Three raters on 64 stratified items

**Precedent.** Three raters is the modal design in every field survey read:

Card et al. §5.1: "57% of experiments collected 3 annotations per item, which was also the modal
number of unique annotators."

Karpinska et al., Table A1: "3 raters (16)" out of 45 papers, the largest single bucket.

Calderon et al., ACL 2025, Appendix A, the argument for three as the floor: "With at least three
annotators, the procedure better evaluates whether the LLM represents the broader group."

Calderon et al. §5.1 on the item count: "Figure 2 shows that for epsilon=0.2, in most cases, the LLM
begins to pass the test before annotating 100 instances, and in half even before 50 instances."

**Recommendation.** The design needs no defence; the reliability figure needs a comparison. The
paper's third limitation currently reports "quadratic-weighted $\kappa$ = 0.41--0.60 across three
rater pairs; Krippendorff's $\alpha = 0.529$, $n = 64$" and calls it "moderate". That is honest but
unanchored. A reader with no NLG background will read 0.529 as poor.

Anchor it in one clause, using Elangovan et al. (ACL 2024):

> "Inter-rater reliability is moderate (quadratic-weighted kappa 0.41 to 0.60 across three rater
> pairs; Krippendorff's alpha 0.529, n = 64), within the range typical of open-ended NLG judgments."

And cite van der Lee et al. §3.3 ("Agreement in most cases ranged from 0.3 to 0.5") or Elangovan et
al. §3.2.1 ("What is considered as 'low' IRA can vary from task to task, as complex tasks or
difficult samples tend to have low IRA"). One clause and one citation converts a number that looks
like a weakness into a number that looks like the field's normal range, without claiming anything
untrue.

### 31.6 The one correction to make regardless

The appendix subsection is titled "Power Analysis" and opens "Post-hoc power analysis at
$\alpha = 0.05$, 80\% power". Card et al., the paper this section will be read against, warns
against exactly that construction in footnote 2 of §1:

> "Using the observed outcome from a single experiment to compute power falls into the trap of
> post-hoc power analysis and is not recommended."

The appendix's own content is not the prohibited thing. It reports **minimum detectable effects at a
fixed alpha and target power given the realized sample sizes**, and then compares the observed effect
to the MDE. That is a design-sensitivity calculation, not observed-power. The label is what is wrong.

**Rename the subsection "Minimum Detectable Effects" and change the opening line to
"Minimum detectable effects at alpha = 0.05 and 80% power, given realized sample sizes."** Nothing
else in the subsection needs to change. Card et al. themselves label their equivalent calculation
this way in §3: "the minimum detectable effect (MDE) size may be large: only large improvements will
yield sufficiently powered comparisons (i.e., 80% power)."

This is the single highest-value edit in this file. It removes a phrase that a methodologically
alert reviewer will treat as a red flag, at the cost of two words, and it leaves the substance
intact.

### 31.7 What to cut

The corpus is unanimous on one point that runs against the paper's current draft: **nobody states a
limitation four times.** Tyen et al. state their skew once in Methods, once at the point of the
estimate, and once in Limitations, and that is the most thorough disclosure in 39 sources. The
paper currently states the Llama dominance in four places and the per-domain cell sizes in three.

Recommended placement, one fact to one or two places:

| Fact | Methods | At the estimate | Limitations |
|---|---|---|---|
| Panel is 45/50 Llama, three models at zero | structural note only | **yes, with the claim it licenses** | one clause |
| Per-domain cells 13 to 30 | -- | **yes, with intervals** | one clause |
| n < 5 not tested | **yes, stated as a rule** | table dash | -- |
| Two annotators, 50 pairs | **yes, with kappa** | -- | -- |
| Three raters, 64 items | **yes, with kappa and the field range** | -- | one clause |

That is five facts across nine placements, down from the current fourteen. The disclosure is not
weakened. It is stated once where it bears, which is what every well-regarded paper in this corpus
does.

---

## 32. Audit trail for the counts

The 21 empirical papers underlying every "of 21" figure in §30, so the count can be rechecked:

Schoenegger et al. (10), Peng et al. (11), Schütz et al. (12), Padmakumar & He (9), HELM (6),
Chatbot Arena (7), Huang et al. (21), Madaan et al. (23), Tyen et al. (24), Sharma et al. (25),
Shinn et al. (26), Zheng et al. (27), Chiang & Lee (28), Clark et al. (29), Thomson & Reiter (31),
Karpinska et al. (32), Calderon et al. (33), Jakesch et al. (36), Lee et al. (37), Buçinca et al.
(38), Vasconcelos et al. (39).

The 15 non-empirical sources: Card et al. (1), Howcroft & Rieser (2), Marie et al. (3), Gehrmann et
al. (4), Amidei et al. (5), Herrmann et al. (8), Dror et al. (16), Howcroft et al. (17), van der Lee
et al. (18), Bowman & Dahl (19), Ethayarajh & Jurafsky (20), Kamoi et al. (22), Elangovan et al.
(30), Caine (34), Kay et al. (35). Plus the three policy documents (13, 14, 15).

Borderline calls, stated so they can be overruled: Howcroft et al. (17) and Caine (34) both annotate
a corpus of papers and report inter-annotator agreement, so they could be counted as empirical; they
are excluded here because their unit of observation is a published paper, not an experimental
condition. Calderon et al. (33) is counted as empirical because it collects and analyses ten
annotated datasets, though its contribution is methodological.

## 33. Venue policy: what ARR requires

Three policy pages fetched 2026-09-06.

**ACL Rolling Review, Author Guidelines**, on what a Limitations section is for:

> "the limitations section should focus on the soundness of the study, and answer the question: what
> are the methodological caveats that the reader should be aware of when interpreting the reported
> findings?"

> "authors also commonly list the directions of generalizability of their results that they have not
> tested (languages, domains, tasks, datasets, model families, model sizes, etc.)"

"model families" appears in that list. A panel that is 90% one model is exactly the untested
generalization direction the guidance names, which means the disclosure belongs in Limitations by the
venue's own definition and is not a concession.

**ACL 2023 Program Chairs blog**, on the requirement:

> "Every work has limitations, and ACL 2023 submissions include a mandatory section for discussing
> that."

**ACL Rolling Review, Responsible NLP Research checklist**, the items that bear on this paper:

> "C3: Did you report descriptive statistics about your results (e.g., error bars around results,
> summary statistics from sets of experiments), and is it transparent whether you are reporting the
> max, mean, etc. or just a single run?"

> "B6: Did you report relevant statistics like the number of examples, details of train / test / dev
> splits, etc. for the data that you used / created?"

> "D1: Did you report the full text of instructions given to participants, including e.g.,
> screenshots, disclaimers of any risks to participants or annotators, etc.?"

> "D5: Did you report the basic demographic and geographic characteristics of the annotator
> population that is the source of the data?"

**No checklist item asks for a power analysis, a minimum detectable effect, or a justification of
sample size.** C3 asks for error bars and B6 for counts. Both are satisfied by reporting per-cell n
and confidence intervals, which is what §31.2 recommends. D5 is worth checking against the paper's
current annotator reporting, which names two annotators by role but reports no demographic
characteristics.

## 34. Integrity notes

Every quotation in this file was extracted from a document fetched on 2026-09-06 and read in full
text, except where §29 says otherwise. Nothing is quoted from memory or reconstructed. Where a source
contains a typographical error, a subject-verb disagreement, or an extraction artifact from PDF or
LaTeXML conversion, it is reproduced as found and flagged inline rather than silently corrected. Em
dashes in quoted material have been rendered as hyphens for consistency with this project's
conventions, and curly quotation marks and apostrophes have been rendered as straight ones; no other
character in any quotation has been altered.

Four quotations used in §31 were re-verified against a second, independently converted copy of the
source PDF after the catalogue was written: Vasconcelos et al. §7.4, §7.5 and §7.6, and §5.4. All
four matched digit for digit and word for word.

Mathematical symbols lost in PDF extraction (the less-than-or-equal glyph, Greek letters in some
sources) are noted at the point they occur or spelled out. Percentages, sample sizes and statistical
values are transcribed digit for digit.

Counts in §30 were produced by tallying the catalogued entries in Parts I to IV, not estimated. The
audit trail in §32 lists the papers behind the denominators so any figure can be rechecked without
re-fetching.

One quotation carries a lower confidence rating than the rest: Peng, Kalliamvakou, Cihon and Demirer
(arXiv 2302.06590) was read only through an ar5iv HTML rendering rather than a locally converted PDF.
Re-verify those three sentences against the PDF before citing any of them.

