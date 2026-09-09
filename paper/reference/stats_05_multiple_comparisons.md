# Multiple comparisons in NLP and HCI: what the literature does, and what it says

Retrieved 2026-09-06. All quotations below were taken from documents fetched on that
date and are transcribed verbatim from the fetched text. Nothing here is quoted from
memory, and no document is cited that was not fetched.

This file reports conventions and options. It contains no recommendation about the
analysis of the present paper; specification and sample decisions belong to the author.

---

## 1. How the corpus was built, and what it does not cover

**Sampling.** The corpus was assembled by topic, not by the presence of correction
language, so that the split between correcting and non-correcting papers is not
manufactured by the search. Candidates came from three sources: (a) the project's own
neighbour set in `paper/reference/neighbor_abstracts.md`; (b) arXiv API queries on
topic terms only, run 2026-09-06, namely `abs:"human evaluation" AND abs:"large language
models" AND abs:"annotators"`, `abs:"user study" AND abs:"large language model" AND
cat:cs.HC`, `abs:"LLM" AND abs:"participants" AND abs:"between-subjects"`, and
`abs:"self-correction" AND abs:"large language models"`; (c) five methodological papers
on statistical practice in NLP, added deliberately as reference points and counted
separately from the empirical split.

**Extraction.** Full text was fetched from `arxiv.org/html/<id>` (falling back to
`ar5iv.labs.arxiv.org/html/<id>`) or from ACL Anthology PDFs converted with `pdftotext`.
Classification was done by regular expression over the full text, not by reading
summaries: test names (Wilcoxon, Mann-Whitney, t-test, ANOVA, chi-squared, Kruskal-Wallis,
sign test, McNemar, Fisher exact, bootstrap, permutation, mixed-effects, regression,
binomial, Friedman), correction terms (multiple comparisons, multiple testing, multiple
hypotheses, Bonferroni, Holm, Benjamini, Hochberg, false discovery, FDR, family-wise,
Sidak, Dunn, Tukey, multiplicity, adjusted p), and fencing terms (exploratory, post hoc,
confirmatory, directional, underpowered, interpret with caution, small sample).

**Transcription conventions.** arXiv HTML stores inline mathematics in an `alttext`
attribute, so quoted p-values and Greek letters appear in their LaTeX-ish source form
(`\alpha=.05`, `\chi^{2}(1)=192.43`, `p=4.9317e-06`). Where the HTML rendering drops a
comparison operator, the sentence is not quoted, or the loss is marked `[…]`; no operator
or number has been reconstructed. ACL Anthology PDFs occasionally join words across a
line break (`HolmBonferroni`); such joins are kept as extracted and flagged.

**Bounds of the sweep.** One field pair (computational linguistics and human-computer
interaction), English only, 2017 to 2026, 36 documents. Papers were classified on their
full text as published on arXiv or in the ACL Anthology; supplementary materials,
pre-registrations, and code repositories were not opened, except where the paper itself
quotes them. Psychology, biostatistics, and medicine were not searched, although their
conventions are the source of the correction procedures named here. Two candidates could
not be retrieved: arXiv 2504.14522 returned no usable HTML rendering, and
`aclrollingreview.org/authorguidelines` returns 404 (the live page is
`aclrollingreview.org/authors`). No other access failure occurred.

---

## 2. Corpus

36 documents, all retrieved 2026-09-06. "p-values" counts distinct reported p-value
expressions matched mechanically in the fetched text and is a floor, not a census:
p-values printed only inside table cells or rendered as bare significance stars are not
counted.

### 2a. Empirical papers that report at least one inferential test (19)

| # | ID | Short title | Field | Tests run | p-values | Correction |
|---|---|---|---|---|---|---|
| 1 | arXiv 2211.03622 | Do Users Write More Insecure Code with AI Assistants? | HCI / security | Welch t, chi-squared, logistic regression, across 5 questions and security subgroups | 5 | **Benjamini-Hochberg** |
| 2 | arXiv 2212.07981 | Revisiting the Gold Standard | core NLP | paired bootstrap, permutation, pairwise across systems and ~200 metric pairs | 0 | none |
| 3 | arXiv 2303.17651 | Self-Refine | core NLP | Wilson intervals at 99%, 7 tasks x 3 models = 21 marked comparisons | 0 | none |
| 4 | arXiv 2402.05650 | Rocks Coding, Not Development | HCI / SE | Mann-Whitney U across tasks and measures | 6 | none |
| 5 | arXiv 2406.05063 | Are LLMs More Empathetic than Humans? | core NLP + human subjects | chi-squared tests of independence, omnibus plus pairwise across 5 response groups, positive and negative splits, per rating class | 82 | none |
| 6 | arXiv 2409.13588 | ChainBuddy | HCI | Mann-Whitney, ANOVA, mixed-effects | 2 | **Bonferroni** (via `emmeans`) |
| 7 | arXiv 2409.15436 | Ads that Talk Back | HCI | Shapiro-Wilk, Kruskal-Wallis across 6 groups and many scales | 9 | Tukey HSD post hoc only |
| 8 | arXiv 2505.02699 | LLM-Powered Pedagogical Agents in VR | HCI | two-way ANOVA plus pairwise across 4 groups, many measures | 51 | Tukey HSD post hoc only |
| 9 | arXiv 2505.24803 | Guiding Generative Storytelling with Knowledge Graphs | HCI | Wilcoxon signed-rank across conditions and genres | 5 | none |
| 10 | arXiv 2509.09870 | Vibe Check | HCI | Kruskal-Wallis plus post hoc Mann-Whitney, many constructs | 30 | **Bonferroni** |
| 11 | arXiv 2601.07229 | DiSCo | HCI | binomial test **within each of three domains**, plus chi-squared of homogeneity across domains | 15 | none |
| 12 | arXiv 2601.21460 | Tell Me What I Missed | HCI | independent-samples t-tests, mixed-effects | 5 | none |
| 13 | arXiv 2602.18962 | NeuroWise | HCI | Mann-Whitney U between groups, Wilcoxon within groups, per construct | 7 | none |
| 14 | arXiv 2603.08849 | LLM Use and Critical Thinking Under Time Constraints | HCI | pre-registered ANCOVA, Tukey HSD, Mann-Whitney across many dependent variables | 5 | **Holm-Bonferroni** and Tukey HSD |
| 15 | arXiv 2604.02637 | Train Yourself as an LLM | HCI | Welch t-tests, ANOVA, logistic regression **per scenario** | 8 | none |
| 16 | arXiv 2605.28571 | Not All Uncertainty Is Equal | HCI | mixed-effects, Wald tests, ANOVA, pairwise across 4 conditions | 2 | **Holm** and Tukey |
| 17 | arXiv 2606.29460 | LLM Intervention Explanations in Multi-Party HRI | HCI / HRI | Mann-Whitney U **per theme**, mixed-effects | 0 | none |
| 18 | ACL `2022.emnlp-main.406` | The Authenticity Gap in Human Evaluation | core NLP | two-sided Student t-tests across model pairs | 0 | **Holm-Bonferroni** |
| 19 | ACL `2025.emnlp-main.1476` | The Good, the Bad and the Constructive | core NLP | Welch t-tests across 4 aspects | 0 | none |

### 2b. Empirical papers reporting no inferential test (11)

These use the word "significant" descriptively, or report point estimates and intervals
without a hypothesis test. They are excluded from the correction split.

| ID | Short title | Field | Note |
|---|---|---|---|
| arXiv 2201.06796 | CoAuthor | HCI | dataset paper; no test |
| arXiv 2310.01798 | LLMs Cannot Self-Correct Reasoning Yet | core NLP | accuracy deltas only |
| arXiv 2310.12397 | GPT-4 Doesn't Know It's Wrong | core NLP | counts only |
| arXiv 2310.13548 | Towards Understanding Sycophancy | core NLP | Bayesian logistic regression, posterior effect sizes, no NHST |
| arXiv 2310.14424 | Which Prompts Make The Difference? | core NLP | "significant" used informally |
| arXiv 2310.19740 | Reliability of LLMs as Customized Evaluators | core NLP | agreement coefficients only |
| arXiv 2311.08516 | LLMs cannot find reasoning errors | core NLP | accuracy plus Krippendorff alpha |
| arXiv 2406.01297 | When Can LLMs Actually Correct Their Own Mistakes? | core NLP | survey |
| arXiv 2408.17026 | From Text to Emotion | core NLP | "significant" used informally |
| arXiv 2503.03587 | LLM-Powered Interactive Privacy Policy Assessment | HCI | qualitative |
| arXiv 2505.06120 | LLMs Get Lost In Multi-Turn Conversation | core NLP | "significantly lower", "non-significant" used without a reported test |

### 2c. Methodological and meta papers (6), counted separately

| ID | Short title | Relevance |
|---|---|---|
| ACL `Q17-1033` | Replicability Analysis for NLP: Testing Significance with Multiple Datasets (Dror et al., TACL 2017) | the field's own framework for multiple comparisons across languages and domains |
| ACL `P18-1128` | The Hitchhiker's Guide to Testing Statistical Significance in NLP (Dror et al., ACL 2018) | survey of ACL 2017 and TACL practice, including multiplicity |
| ACL `2020.emnlp-main.745` | With Little Power Comes Great Responsibility (Card et al., EMNLP 2020) | power in NLP experiments and human rating studies |
| ACL `2022.lrec-1.639` | Dynamic Human Evaluation for Relative Model Comparisons | sample size in human evaluation |
| ACL `2025.acl-long.1586` | Robust Estimation of Population-Level Effects in Repeated-Measures NLP Experimental Designs | family-wise error rate in a repeated-measures NLP design |
| arXiv 2608.09280 | Is the ACL Responsible NLP Checklist a Box-Ticking Exercise? | independent transcription of the current checklist; compliance analysis of EMNLP 2025 |

---

## 3. Counts

Denominator: the 19 empirical papers in section 2a that report at least one inferential
test.

| Measure | Count | Share |
|---|---|---|
| Apply a correction across a family of tests | 6 | 6/19 |
| Apply a post-hoc procedure only (Tukey HSD after a significant omnibus), with no correction across the wider set of outcomes | 2 | 2/19 |
| Apply no correction of any kind | 11 | 11/19 |

**Which correction.** Of the 6 that correct: Bonferroni 2 (arXiv 2409.13588, arXiv
2509.09870), Holm-Bonferroni 2 (arXiv 2603.08849, ACL `2022.emnlp-main.406`), Holm
1 (arXiv 2605.28571), Benjamini-Hochberg 1 (arXiv 2211.03622). Permutation-based
family-wise control: 0. False discovery rate outside the single Benjamini-Hochberg
application: 0.

**Disclosure among the 11 that correct nothing.** Sentences discussing multiple
comparisons: **0**. Not one of the eleven names the issue, states the number of tests
run, or says that no correction was applied. Four give an adjacent caveat about sample
size or power (arXiv 2505.24803, arXiv 2602.18962, arXiv 2604.02637, arXiv 2212.07981),
which is a different concern and is quoted in section 4d.

**Disclosure among the 6 that do correct.** One states the reason in words (ACL
`2022.emnlp-main.406`: "Since we make multiple comparisons"). The other five name a
procedure without saying what the family is. In exactly one case the family size is
recoverable from the reported alpha: arXiv 2509.09870 reports `\alpha=.017`, which
implies three comparisons.

**Reliability coefficients.** Across the whole corpus, inter-annotator agreement
statistics (Cohen's kappa, Krippendorff's alpha, ICC, Spearman rho) are reported as point
estimates, sometimes with a confidence interval, and are never treated as a family of
hypothesis tests. No paper applies any correction to them. Ranges across rater pairs or
questions are reported as ranges (arXiv 2211.03622: "ranging from 0.7-0.96 for
correctness and 0.68-0.88 for security"; arXiv 2603.08849: "ICC(2,1) values ranged from
0.70 to 0.82").

**Historical baseline, from the field's own survey.** Dror et al. (ACL 2018) counted the
same thing for ACL 2017 and TACL and found 3/110 and 4/19. The 11/19 no-correction share
measured here is not comparable in denominator (their denominator is papers using
multiple datasets; this one is papers reporting any inferential test), but the direction
agrees.

---

## 4. Verbatim catalogue

Every sentence in the corpus that discusses multiple comparisons, plus the subgroup and
fencing language requested. Transcribed exactly as fetched.

### 4a. Papers that apply a correction

**arXiv 2211.03622, Do Users Write More Insecure Code with AI Assistants?** (retrieved
2026-09-06)

> We correct for multiple regressions via the Benjamini-Hochberg corrections ( 3 ) , and report results in Table 3 .

> The B-H crit column contains the critical values needed for statistical significance after the Benjamini-Hochberg correction.

> This does not pose any problems to our analysis due to the fact that all statistical tests conducted are valid for unequal sample sizes and variances (Welch's t-test and the Chi-squared test for categorical data).

> Note that while this table reports results for the effect of the experiment/control groups, we determine statistical significance of this treatment for particular security buckets (e.g. only "Insecure") using Welch's unequal variance t-test in our main reported results.

**ACL `2022.emnlp-main.406`, The Authenticity Gap in Human Evaluation** (retrieved
2026-09-06). The first quotation contains a PDF line-break join, `HolmBonferroni`,
reproduced as extracted; the same join appears in the second as
`Holm-Bonferronicorrected`.

> For the standard protocol, we use a paired t-test to determine whether the Likert ratings of two systems' outputs are significantly different. Since we make multiple comparisons, we apply the HolmBonferroni correction (Holm, 1979).

> We use two-sided Student's t-tests with Holm-Bonferronicorrected significance at α = 0.10(∗ ), 0.05(∗∗ ), 0.01(∗∗∗ ).

> According to SPA, scrambling the prompt before using DALL-E creates significantly worse images than using the original prompt, as expected (α = 0.01, Holm-Bonferroni-corrected).

**arXiv 2509.09870, Vibe Check** (retrieved 2026-09-06)

> Post hoc Mann–Whitney U comparisons with Bonferroni adjustment ( \alpha=.05 ).

> Bonferroni-adjusted Mann–Whitney U tests ( \alpha=.017 ) showed that the medium condition consistently outperformed the low condition on all identified above (see Figure 7 , Table 3 ).

> Post hoc Mann–Whitney U tests (Bonferroni correction) for pairwise comparisons across three levels Variable Pair U p p_{\mathrm{adj}} r Sig.

> Pairwise comparisons for variables with significant Kruskal–Wallis results. p_{\mathrm{adj}} values are Bonferroni-corrected.

> Post hoc tests (Bonferroni-corrected) showed that the "Well-Aligned" cluster's values for Trust, Likeability, and Intelligence were higher than both other clusters, and values for Enjoyment, Intention to Adopt, and Anthropomorphism were higher than the "Globally-Misaligned" cluster.

**arXiv 2603.08849, Investigating the Effects of LLM Use on Critical Thinking Under Time
Constraints** (retrieved 2026-09-06)

> Following our pre-registration, we conducted an Analysis of Covariance (ANCOVA) analysis to examine the main effects and interaction of LLM access timing and time availability on all dependent variables.

> All tests used a significance level of 0.05. We conducted Tukey's Honestly Significant Difference (HSD) post-hoc tests for pairwise comparisons. Comparisons were performed within each time availability level, comparing all pairs of LLM access timing conditions, and within each LLM access timing condition, comparing time availability.

> Mann-Whitney U tests with Holm-Bonferroni correction revealed significant differences only for time availability: participants under Sufficient time rated higher on interpretation ( U=11234 , p.adj=0.009 ), analysis ( U=11308 , p.adj=0.011 ), and total score ( U=11559 , p.adj=0.027 ).

**arXiv 2605.28571, Not All Uncertainty Is Equal** (retrieved 2026-09-06)

> For participant-level DVs, we conduct a one-way analysis of variance (ANOVA) to compare means across conditions.

> When the omnibus test is significant, we perform post-hoc pairwise comparisons using Tukey's test.

> After fitting the model, we use Wald tests to assess whether the estimated effects of different UQ conditions differ significantly from one another.

**arXiv 2409.13588, ChainBuddy** (retrieved 2026-09-06)

> Post-hoc tests were done via estimated marginal means ( emmeans ) with Bonferroni correction; when including the estimate ( \beta ) and t-statistic ( t ), reported p-values are from emmeans .

### 4b. Post-hoc procedure only, with no correction across the wider outcome set

**arXiv 2409.15436, Ads that Talk Back** (retrieved 2026-09-06)

> We ran a Shapiro-Wilk test, determining that all tested scales were not normally distributed […]

> Kruskal–Wallis tests followed by Tukey HSD found no significant differences between advertising and control conditions on any scale (all p>.05 ; full statistics in Section 5.6 ).

> [LAQ1, Felt Advertising]: A Kruskal-Wallis test revealed significant differences ( H = 32.41 , p = 4.9317e-06 ), with post-hoc Tukey's HSD confirming that users in the advertising conditions (A3.5, A4o, DA3.5, DA4o) felt like they were being advertised to more than those in the controls (C3.5, C4o).

**arXiv 2505.02699, LLM-Powered Pedagogical Agents in VR** (retrieved 2026-09-06)

> Subsequently, we conducted post-hoc Tukey HSD tests to identify specific group differences after identifying significant main effects or interaction effects.

> The post-hoc Tukey HSD test showed that there were significant differences between Group NN and Group NA (MD = -1.15, p < 0.001) and between Group NN and Group RA (MD = -0.75, p = 0.005).

### 4c. Papers running many tests that say nothing about multiplicity

For these eleven the catalogue is empty by construction: a full-text search for
"multiple comparison", "multiple test", "multiple hypothes", "Bonferroni", "Holm",
"Benjamini", "Hochberg", "false discovery", "FDR", "family-wise", "Sidak", "Dunn",
"Tukey", "multiplicity" and "adjusted p" returns nothing in any of them. What follows is
therefore the method sentence each one does give, which is what stands in place of a
statement about the family of tests.

**arXiv 2406.05063, Are LLMs More Empathetic than Humans?** (82 p-values, five response
groups, positive and negative splits, per rating class, plus an appendix of finer
per-emotion analysis)

> To analyze the results from the study we use the chi-square test of independence McHugh (2013) that tests whether there is any statistically significant difference between the proportion of Bad , Okay , and Good ratings of the five response groups.

> For the chi-square test of independence with a medium effect size (0.3) , a significance level (\alpha) of 0.05 , and a power (1-\beta) of 0.95 , the minimal total sample size required is 253 (i.e. at least 51 participants per group).

> This scale was adequate to reveal significant differences in human and LLM-generated empathetic responses, confirming its effectiveness in the context of our research objectives.

**arXiv 2303.17651, Self-Refine** (21 model-by-task comparisons, each marked significant
or not by an asterisk)

> Table 13 shows results from Table 1 with Wilson confidence interval Brown et al. (2001) (at \alpha = 99% confidence interval) and statistical significance. Gains that are statistical significance based on these confidence intervals are marked with an asterisk. We find that nearly all of GPT-4 gains are statistically significant, ChatGPT gains are significant for 4 out of 7 datasets, and GPT-3.5 gains are significant for 3 out of 7 datasets.

> Gains over Base, that are statistically significant based on these confidence intervals are marked *

**arXiv 2212.07981, Revisiting the Gold Standard**

> We use paired bootstrapping for the significance test.

> We note that we use the permutation test instead of the paired bootstrapping test to calculate the statistical significance for metric comparison […]

> We conduct a power analysis of pair-wise metric comparison with around 200 pairs, which corresponds to the chance of a statistical significance result being found.

**arXiv 2402.05650, Rocks Coding, Not Development**

> Therefore, we used non-parametric method Mann Whitney U test (M-U Wilcoxon test) ( Rey and Neuhäuser, 2011 ) to compare the differences.

> Similarly, no statistical significance was detected with the M-U Wilcoxon test results W = 354 and p-value = 0.95 .

**arXiv 2505.24803, Guiding Generative Storytelling with Knowledge Graphs**

> To examine whether a condition (e.g., "with knowledge graph" vs. "without knowledge graph") has a statistically significant impact on participant ratings, we use the Wilcoxon Signed-Rank Test ( Woolson 2005 ) on paired data.

> To properly compute statistical significance (using the Wilcoxon Signed-Rank Test) for a pair of conditions, we only compare ratings from participants who provided responses in both conditions.

**arXiv 2602.18962, NeuroWise**

> Given small sample sizes and ordinal measures, we used non-parametric Mann-Whitney U tests for between-group comparisons and Wilcoxon signed-rank tests for within-group comparisons ( Romano et al., 2006 ) .

**arXiv 2601.21460, Tell Me What I Missed**

> To examine whether the guided GPT condition—prompted under design-informed instructions—affected memory recall differently compared to the default, unguided use of GPT for a recall-statement documenting task, we conducted an independent samples t-test.

**ACL `2025.emnlp-main.1476`, The Good, the Bad and the Constructive**

> The results show that human-written reviews outperform LLM-generated ones across 3 out of 4 aspects with statistically significant differences measured by Welch's t-test (Welch, 1947). On the Helpfulness aspect, where GPT-4 scores are slightly higher, the difference in the reviews is not significant.

### 4d. Per-subgroup families: how the family is framed

This is the closest structural analogue to a per-model or per-domain breakdown. Four
papers in the corpus run a test separately inside each subgroup. None of the four
corrects across the subgroups. They differ in how they present the resulting pattern.

**arXiv 2601.07229, DiSCo. One test per domain, plus a chi-squared of homogeneity across
domains. This is the same shape as a per-domain sign test plus a chi-squared test of
homogeneity.**

> To test whether the observed proportion of preferences for the DiSCo differed significantly from random (0.5) we used a binomial test within each domain. In addition, a chi-square test of independence examined whether the overall preference distribution varied by domain.

> Only the Ski domain showed a statistically significant deviation from chance, with a clear majority preferring the DiSCo summaries […]

> A chi-square test of independence comparing the three domains (Beach, City-center, Ski) confirmed that the distribution of preferences was not uniform across conditions, \chi^{2}(2)=15.6 […]

The single significant domain is reported without a claim that it is confirmatory and
without a correction; the homogeneity test does the work of establishing that the domains
differ, and the per-domain result is stated as a description of where the difference sits.

**arXiv 2604.02637, Train Yourself as an LLM. Three per-scenario logistic regressions
under one significant pooled effect. This is the clearest example of the pattern of
reporting a subgroup breakdown as directional support rather than as an independent
finding.**

> Scenario-wise intervention effects. We also performed three logistic regression models to examine the total intervention effect within each scenario. None of the scenario-specific treatment effects reached statistical significance. Still, all three treatment coefficients were negative, and all odds ratios were below 1, showing a consistent pattern with the significant overall total effect. However, these scenario-wise models were likely underpowered, which we acknowledge as one limitation of our study. Future work with larger samples can investigate scenario-specific effects more precisely.

> Although the indirect effects were not significant, the direct and total effects remained negative and directionally consistent with the main analysis.

> Taken together, these findings suggest that AI-AI benchmark evaluations should be interpreted with caution as direct proxies for human susceptibility to persuasion.

**arXiv 2211.03622, Do Users Write More Insecure Code with AI Assistants? Per-question
and per-security-bucket tests, with the correction applied and the small-sample position
stated in one sentence.**

> Due to small sample sizes, we document when results are statistically significant.

> We found that participants with access to an AI assistant consistently wrote less secure code than those without access to an AI assistant on four of our five questions.

> We note statistically significant differences between experiment and control groups in the text for each […]

**arXiv 2606.29460, LLM Intervention Explanations in Multi-Party HRI. One Mann-Whitney U
per theme, no correction, with the non-significant differences described as a tendency.**

> Although these differences suggest a tendency toward more goal-oriented intervention explanations when roles are differentiated, these variations were not statistically significant.

> The opposer was preferred only for "Highlighting Negotiation Goals" (29 vs. 58), with all differences statistically significant according to two-sided Mann–Whitney U tests […]

### 4e. Confirmatory and exploratory, separated explicitly

One paper in the corpus partitions its analyses into a confirmatory set tied to
pre-stated hypotheses and an exploratory set, and labels the sections that way in the
table of contents. This is the strongest example of the option of framing part of a
result set as exploratory rather than correcting it.

**arXiv 2605.28571, Not All Uncertainty Is Equal** (retrieved 2026-09-06)

Section headings, as rendered: "5 Confirmatory Analysis Results", "6 Exploratory Analysis
Results".

> Confirmatory Analysis Results Here, we report the results of our confirmatory analyses regarding the hypothesis in subsection 4.3 .

> Exploratory Analysis Results In addition to confirmatory analyses, we conducted two exploratory investigations: (1) comparing participants' self-confidence with their confidence in AI, and (2) analyzing qualitative feedback from post-study surveys.

> Although not hypothesized a prior, we observed clear differences between confidence in self ( Baseline : M=4.253, UQ-Output : M=4.094, UQ-Relation :M=3.962, UQ-Token : M=4.161) and confidence in the LLM ( Baseline : M=3.578, UQ-Output : M=3.498, UQ-Relation :M=3.442, UQ-Token : M=3.615) . We therefore conducted an exploratory analysis to further examine this pattern.

> We show model-estimated marginal means from the confirmatory mixed-effects analyses and error bars indicate 95% confidence interval. * denoting p\leq.05 and ** denoting p\leq.01 .

Note the structure: the exploratory analyses still carry Holm-corrected pairwise
comparisons. Labelling them exploratory does not substitute for the correction there; the
two are used together.

### 4f. Language used to fence an underpowered analysis

Collected verbatim across the corpus, including the methodological papers.

> However, these scenario-wise models were likely underpowered, which we acknowledge as one limitation of our study. Future work with larger samples can investigate scenario-specific effects more precisely. (arXiv 2604.02637)

> However, it is important to note that our overall sample size was relatively small, limiting the statistical power of our significance tests. (arXiv 2505.24803)

> Due to small sample sizes, we document when results are statistically significant. (arXiv 2211.03622)

> Given small sample sizes and ordinal measures, we used non-parametric Mann-Whitney U tests for between-group comparisons and Wilcoxon signed-rank tests for within-group comparisons. (arXiv 2602.18962)

> Our within-subjects usability study had a small sample size and compared to a single baseline. (arXiv 2409.13588)

> Moreover, the relatively small sample size used fails to provide sufficient data to arrive at robust statistical conclusions. (arXiv 2406.05063, said of prior work, not of its own study)

> Enjoyment ( \beta=1.347 , p=.196 ; \Delta R^{2}=.012 , p=.172 ), Intention to Adopt ( \beta=1.728 , p=.156 ; \Delta R^{2}=.016 , p=.116 ), and Likeability ( \beta=0.790 , p=.188 ; \Delta R^{2}=.009 , p=.234 ) showed consistent directional trends in the expected direction. (arXiv 2509.09870)

> Although these differences suggest a tendency toward more goal-oriented intervention explanations when roles are differentiated, these variations were not statistically significant. (arXiv 2606.29460)

The recurring construction has three parts: state that the subgroup result did not reach
significance; state the direction and its consistency with the pooled result; name power
as the reason and defer the question to a larger sample. No paper in the corpus uses the
words "we did not correct for multiple comparisons."

### 4g. What the methodological literature says

**ACL `Q17-1033`, Dror, Baumer, Bogomolov and Reichart, Replicability Analysis for
Natural Language Processing: Testing Significance with Multiple Datasets** (retrieved
2026-09-06)

> However, such multiple comparisons pose significant challenges to traditional statistical analysis methods in NLP and can lead to erroneous conclusions.

> This is because although the probability of drawing an erroneous conclusion from a single comparison is small, with multiple comparisons the probability of making one or more false claims may be very high.

> Multiple Comparisons in NLP Multiple comparisons of algorithms over datasets from different languages, domains and genres have become a de-facto standard in many areas of NLP.

> Having a sound statistical framework that can deal with multiple comparisons is hence crucial for the field.

> A classical and very simple method for addressing this problem is named the Bonferroni's procedure, which compensates for the increased probability of making at least one type I error by testing each individual hypothesis at a significance level of α0 = α/N , where α is the predefined bound on this probability and N is the number of hypotheses tested. While Bonferroni's procedure is valid for any dependency among the p−values, the probability of detecting a true effect using this procedure is often very low, because of its strict p−value threshold.

> Below we advocate one of these methods: the Holm procedure (Holm, 1979).

> Importantly for NLP applications, Holm controls the probability of making at least one type I error for any type of dependency between the participating datasets (see a demonstration in Section 6).

> Based on Section 4.3 we suggest to answer the identification question of Section 1 by reporting the rejection list returned by the Holm procedure.

> An alternative, more powerful multiple testing procedure for identification of datasets with effect, is the method in Benjamini and Hochberg (1995), that controls the false discovery rate (FDR), a less strict error criterion than the one considered here.

> As noted in Section 2, we believe that multiple comparisons are integral to NLP research when aiming to develop algorithms that perform well across languages and domains.

In their own tables, the per-dataset results identified by the Holm procedure are marked
with a symbol rather than reported as a list of individually significant datasets:

> ∗ indicates languages identified by the Holm procedure with α = 0.05 .

> ∗ and + indicate domains identified by the Holm procedure with α = 0.05 and α = 0.01, respectively.

**ACL `P18-1128`, Dror, Baumer, Shlomov and Reichart, The Hitchhiker's Guide to Testing
Statistical Significance in Natural Language Processing** (retrieved 2026-09-06). This is
the field's own count of how often the correction is applied.

> While this paper focuses on the correct choice of a significance test, we also checked whether the papers in our sample account for the effect of multiple hypothesis testing when testing statistical significance (see (Dror et al., 2017)). When testing multiple hypotheses, as in the case of comparing the participating algorithms across a large number of datasets, the probability of making one or more false claims may be very high, even if the probability of drawing an erroneous conclusion in each individual comparison is small. In ACL 2017, out of 110 papers that used multiple datasets only 3 corrected for multiplicity (all using the Bonferroni correction). In TACL, the situation is slightly better with 4 papers correcting for multiplicity out of 19 that should have done that.

> The lower part of Table 2 depicts the disturbing reality of statistical significance testing in our research community. Out of the 180 experimental long papers of ACL 2017, only 63 papers included a statistical significance test.

> We note that in this paper we do not deal with the problem of drawing valid conclusions from multiple comparisons between algorithms across a large number of datasets , a.k.a. replicability analysis (see (Dror et al., 2017)).

**ACL `2025.acl-long.1586`, Robust Estimation of Population-Level Effects in
Repeated-Measures NLP Experimental Designs** (retrieved 2026-09-06). A 2025 ACL long
paper that states the family-wise arithmetic explicitly for a six-test design and then
declines to treat correction as the answer.

> In face of the hierarchical structure of the data at hand, one common, though ultimately inadequate approach consists in repeatedly applying the paired t-test. Although the paired t-test is a popular and simple method for within-subject comparisons (e.g., English vs. Spanish), it is generally inadequate for repeated-measures data. It assumes independent pairs—a condition often violated in complex designs with repeated evaluations across multiple tasks and modes. Even if independence is forced by averaging observations, this process removes legitimate variability and yields underpowered analyses, a common issue in NLP research (Card et al., 2020). For example, the hierarchical design presented in this paper would require six tests, which would inflate the family-wise error rate to approximately a 27% at the standard significance level α = 0.05: (P = 1 − αN = 1 − (0.95)6 ≈ 0.27). Although corrections such as Bonferroni, Holm, or FDR exist (Dror et al., 2017), mechanically applying them in a mechanical manner can lead to systematic misinferences (e.g., inflated type II errors) (Nakagawa, 2004), so they should not be relied upon as a universal solution to dependency issues. Furthermore, in small-N designs such as the demonstrated in this paper, these partial tests, having only 2 degrees of freedom, would be markedly underpowered and thus would render the detection of even large effects virtually unfeasible.

**ACL `2020.emnlp-main.745`, Card, Henderson, Khandelwal, Jia, Mahowald and Jurafsky, With
Little Power Comes Great Responsibility** (retrieved 2026-09-06)

> Underpowered experiments make it more difficult to discern the difference between statistical noise and meaningful model improvements, and increase the chances of exaggerated findings.

> In particular, if it is the case that typical experiments in NLP are underpowered, not only would we expect many meaningful improvements to go undetected, we would also expect many apparently significant differences to be exaggerated (Gelman and Carlin, 2014).

> Moreover, significant findings from underpowered experiments are more likely to exaggerate or reverse the true effect – so-called Type-M (magnitude) and Type-S (sign) errors, respectively (Gelman and Carlin, 2014).

> Similarly, based on reasonable assumptions, we find that the most typical experimental design for human rating studies will be underpowered to detect small model differences, of the sort that are frequently studied.

> Many human evaluation studies are likely underpowered: Using the "high variance" parameters (which are typical of most of the datasets we used), the most common design at EMNLP 2019 (3 workers, 100 items) is underpowered unless the effect size is quite large (0.2 or higher on the [0, 1] scale).

> For any comparisons which are likely to be underpowered, we should refrain from placing much emphasis on obtaining small improvements over the previously reported best model.

> Most of the papers from which we collected results did not report a significance test on the test set.

The paper's reference list includes, verbatim as a title:

> The garden of forking paths: Why multiple comparisons can be a problem, even when there is no "fishing expedition" or "p-hacking" and the research hypothesis was posited ahead of time.

**ACL `2022.lrec-1.639`, Dynamic Human Evaluation for Relative Model Comparisons**
(retrieved 2026-09-06)

> A fixed number of annotations can lead to evaluation experiments that are likely to be statistically underpowered to detect the true effects of the corresponding model (Card et al., 2020).

---

## 5. What ARR requires

### 5a. The Responsible NLP Research checklist

Source: https://aclrollingreview.org/responsibleNLPresearch/ , retrieved 2026-09-06.
SHA-256 of the extracted text of the fetched page, first 16 hex characters: 27ab9224ecd40ab6.
The page states no revision date, so the access stamp bounds the currency claim: unchanged
as of 2026-09-06. The checklist is current as of
2026-09-06.

A full-text search of the fetched page for "multiple comparison", "multiplicity",
"Bonferroni", "Holm", "Benjamini", "false discovery", "FDR", "family-wise",
"significance test", "hypothesis test" and "p-value" returns **no match**. The checklist
contains no item on statistical testing and no item on multiple comparisons.

The nearest items, quoted in full:

> C3. Did you report **descriptive statistics** about your results (e.g., error bars around results, summary statistics from sets of experiments), and is it transparent whether you are reporting the max, mean, etc. or just a single run?
>
> Error bars can be computed by running experiments with different random seeds, Clopper–Pearson confidence intervals can be placed around the results (e.g., accuracy), or expected validation performance can be useful tools here.
>
> In all cases, when a result is reported, it should be clear if it is from a single run, the max across N random seeds, the average, etc.
>
> When reporting a result on a test set, be sure to report a result of the same model on the validation set (if available) so others reproducing your work don't need to evaluate on the test set to confirm a reproduction.

> B6. Did you report relevant statistics like the number of examples, details of train / test / dev splits, etc. for the data that you used / created?
>
> Even for commonly-used benchmark datasets, include the number of examples in train / validation / test splits, as these provide necessary context for a reader to understand experimental results. For example, small differences in accuracy on large test sets may be significant, while on small test sets they may not be.

> A1. Did you describe the **limitations** of your work?
>
> Point out any strong assumptions and how robust your results are to violations of these assumptions (e.g., independence assumptions, noiseless settings, model well-specification, asymptotic approximations only held locally). Reflect on how these assumptions might be violated in practice and what the implications would be.
>
> Reflect on the scope of your claims, e.g., if you only tested your approach on a few datasets, languages, or did a few runs. In general, empirical results often depend on implicit assumptions, which should be articulated.

On the standing of the checklist:

> Authors must complete the responsible NLP research checklist as part of their paper submission.

> Submissions that systematically fail to provide either specific relevant sections or justification to the questions relevant for their research will be desk-rejected.

> The questions are framed in terms of transparency: "Did you include [information]?" While it is generally preferable that your paper clearly answers positively to the question, it is perfectly acceptable that it does not, provided a proper justification is given (e.g., "We were unable to find the license for the dataset we used"). Not answering positively to a question is not grounds for rejection.

This reading is corroborated by an independent transcription: arXiv 2608.09280, *Is the
ACL Responsible NLP Checklist a Box-Ticking Exercise? A Large-Scale Analysis of EMNLP
2025* (retrieved 2026-09-06), reproduces the checklist in an appendix and summarises the
item as:

> C3 Statistics Report descriptive statistics and specify whether results are from a single run, mean, maximum, etc.

### 5b. The ARR reviewer guidelines

Source: https://aclrollingreview.org/reviewerguidelines , retrieved 2026-09-06. This
is where the statistical expectation lives, not in the checklist. Two items in the list
of reviewable issues:

> **R1. Analysis issues**
>
> Inappropriate/misleading statistics or data presentation, p-hacking, presenting the 'best' results out of an unknown number of trials (including prompt tuning or engineering), baselines that are not sufficiently well-tuned for a fair comparison (including prompt tuning or engineering).

> **R5. Inappropriate or missing statistical significance assessment**
>
> Ideally, at least the main experimental results should be accompanied by appropriate information about their statistical significance (error bars, confidence intervals, statistical significance tests), details about how this was computed, and discussion of factors of variability and any assumptions. Effect size estimation is also very welcome.

Two adjacent items name the framing risk rather than the arithmetic:

> **R2. Inappropriate scope of the claims**
>
> The authors evaluate a sample that does not represent the population about which the claim is made. E.g., a few QA benchmarks !="reasoning" or "understanding", LLMs of a certain size != LLMs.

> **R3. Hypotheses/speculations presented as conclusions**
>
> Every claim that is made has to be based on evidence or arguments (the authors' or from other work), or clearly marked as conjecture/speculation.

A search of the fetched reviewer guidelines for "multiple comparison", "Bonferroni",
"Holm", "Benjamini", "false discovery", "FDR", "family-wise" and "multiplicity" returns
**no match**. The word "p-hacking" in R1 is the only place the multiplicity family of
concerns is named, and it is named as a presentation offence rather than as a required
procedure.

### 5c. The ARR author guidelines

Source: https://aclrollingreview.org/authors , retrieved 2026-09-06. (The URL
`aclrollingreview.org/authorguidelines` linked from some search results returns 404.) A
full-text search returns no statement on statistical testing or multiple comparisons. The
page points authors to the reviewer guidelines for the issue taxonomy.

### 5d. Summary of the venue requirement

Nothing in the current ARR submission apparatus requires a multiple-comparisons
correction, and nothing asks how many tests were run. R5 requires that the main results
carry a significance assessment with "details about how this was computed"; R1 makes
"presenting the 'best' results out of an unknown number of trials" a reviewable issue;
R3 requires that anything not established by evidence be marked as conjecture. The
obligation the guidelines create is one of disclosure and of matching claim strength to
evidence, not one of applying a named procedure.

---

## 6. Assessment

### 6a. What a careful reviewer would expect for a paper of this test count

The test inventory described (one paired Wilcoxon on a balanced panel; per-model sign
tests across six models; per-domain sign tests across five domains; chi-squared tests of
homogeneity; a targeted-feedback comparison; per-model breakdowns of that comparison;
reliability coefficients over three rater pairs; pairwise threshold comparisons in an
appendix) puts the count of reported inferential tests in the same range as the upper
half of the corpus. Only two papers of the 19 report more p-values than that (arXiv
2406.05063 with 82, arXiv 2505.02699 with 51), and both correct nothing and both would
draw R1 attention on the reviewer guidelines' own terms.

Three expectations follow from what the corpus and the guidelines actually say.

**First, the family has to be visible.** The strongest empirical pattern in the corpus
is not that papers fail to correct. It is that papers which correct do not say what they
corrected over, and papers which do not correct do not say how many tests they ran.
Zero of 19 state the size of the test family in words. One of 19 makes it recoverable
from a reported alpha. A reviewer counting eleven or more reported tests and finding no
statement of the count is in exactly the position R1 describes: results presented "out of
an unknown number of trials." That is the reviewable failure the guidelines name, and it
is a disclosure failure, not an arithmetic one.

**Second, the confirmatory claim and the subgroup pattern are held to different
standards.** Across the four subgroup papers in the corpus, none corrects, and none
presents a per-subgroup positive as an independent finding. Each frames it in one of two
ways: as a description of where a pooled or omnibus result sits (arXiv 2601.07229 uses a
homogeneity test to establish that domains differ, then names which domain drives it), or
as directional consistency with the pooled effect (arXiv 2604.02637). A reviewer who sees
a per-model or per-domain positive stated in the abstract or in a contribution bullet
will read it as a confirmatory claim and will then ask what the family was. A reviewer
who sees the same result inside a paragraph describing the pattern, with the pooled test
carrying the claim, will not.

**Third, the reliability coefficients and the appendix threshold comparisons are not part
of the family in this literature's practice.** No paper in the corpus treats an
inter-annotator agreement coefficient as a hypothesis test or corrects it; agreement is
reported as a point estimate or a range across pairs. Appendix sensitivity comparisons
across thresholds are likewise not presented as confirmatory tests anywhere in the
corpus. Whether that convention is right is a separate question, but it means a reviewer
is unlikely to count them into a family.

### 6b. The options, in order of how much they change

These are the options the corpus displays. They are not exclusive; the corpus contains
papers using several at once.

**Option 1. Apply a correction across the whole set of reported tests.** 6 of 19 do this.
Bonferroni and Holm-Bonferroni are the procedures the corpus uses (5 of 6); Benjamini-
Hochberg appears once. Dror et al. (`Q17-1033`) recommend Holm over Bonferroni for NLP
specifically, because Holm controls the same error rate under any dependency structure
and is uniformly more powerful. The cost is the one Dror et al. name in the same passage
and the one arXiv 2025.acl-long.1586 names for a small-N repeated-measures design:
Bonferroni's threshold is strict enough that the probability of detecting a true effect
"is often very low", and in a small-N design the corrected partial tests "would be
markedly underpowered."

**Option 2. Correct within a declared family and say which family.** This is what
`2022.emnlp-main.406` does in one sentence ("Since we make multiple comparisons, we apply
the HolmBonferroni correction"), and what arXiv 2509.09870 does implicitly by reporting
`\alpha=.017` for a three-way comparison. Declaring the family separates the primary test
from the per-subgroup set, so the correction is applied where the multiplicity is and the
primary test keeps its power.

**Option 3. Split confirmatory from exploratory explicitly, at the section level.** arXiv
2605.28571 does this with named sections. The corpus shows this used alongside a
correction, not instead of one: the exploratory analyses there still carry Holm-corrected
pairwise comparisons. What the split buys is a claim-strength statement the reader cannot
miss, which is what ARR R3 asks for.

**Option 4. Frame subgroup results as directional and name power as the reason.** This is
the most common form in the corpus and has a stable three-part construction: the subgroup
result did not reach significance; the direction is consistent across subgroups and with
the pooled effect; the subgroup models were likely underpowered, and a larger sample would
be needed. arXiv 2604.02637 carries the full form. It does not address the false-positive
side of multiplicity, only the false-negative side, so it fits a set of per-subgroup nulls
better than a set containing a per-subgroup positive.

**Option 5. Disclose the test count and state that no correction was applied.** No paper
in the corpus does this. It is the option the ARR reviewer guidelines most directly ask
for (R1 on unknown numbers of trials, R5 on "details about how this was computed"), and
the one no paper supplies. Doing it would put the paper ahead of every empirical paper
surveyed here on the disclosure dimension while leaving the estimates unchanged.

**Option 6. Let a pooled test carry the claim and demote the per-subgroup tests to
description.** arXiv 2601.07229 is the worked example: the chi-squared test of
homogeneity establishes that the domains differ, and the per-domain tests then say where.
Under this framing the per-domain tests are not a family of confirmatory hypotheses, so
the correction question does not arise for them, and the chi-squared test is the single
test the claim depends on.

### 6c. Where the corpus is silent

No paper in the corpus reports a permutation-based family-wise correction, a pre-
registered alpha allocation across a set of outcomes, or a count of tests run alongside a
count of tests reported. The Dror et al. replicability framework (`Q17-1033`), which is
the NLP-native answer to exactly the across-domains and across-models structure at issue,
appears in the corpus only as a citation inside other methodological papers. It is cited
by arXiv `2025.acl-long.1586` and by `P18-1128`; no empirical paper in this corpus
applies it.
