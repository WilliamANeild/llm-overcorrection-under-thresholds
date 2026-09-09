# Rules: Results

Retrieved 2026-09-02. 19 papers; 33 results-bearing sections read in full, plus 3
discussion/limitations sections read only to fix where claims stop.

Sources were read as arXiv LaTeXML HTML (`arxiv.org/html/<ID>` or
`ar5iv.labs.arxiv.org/html/<ID>`). Every quotation below was pulled from the fetched
document, not from memory. LaTeXML renders each math expression twice (`p = .32
p=.32`); quotations here show it once. Nothing else in any quotation is altered.

What could not be done: no ACL Anthology PDF was parsed (the HTML versions of the
ACL/NAACL papers in this corpus were used instead); Card et al. sections 3 and 4,
Kamoi et al. sections 5 and 6, and Kabir et al. section 5 were read at heading level
only and are excluded from the section count; Vasconcelos et al. Study 4 was read
through its design and hypotheses but not its results, and is excluded.

---

## Corpus

Words = results-section prose only, captions and headings excluded. "Effect sizes"
and "CIs" mean reported inside the results section, not in an appendix.

| # | Paper | ID | Organisation | Words | Effect sizes | CIs |
|---|---|---|---|---|---|---|
| 1 | Huang et al., *LLMs Cannot Self-Correct Reasoning Yet* | 2310.01798 | by experiment | 2,893 | no | no |
| 2 | Kamoi et al., *When Can LLMs Actually Correct Their Own Mistakes?* | 2406.01297 | by finding (bold run-in claims) | 1,619 | no | no |
| 3 | Laban et al., *LLMs Get Lost in Multi-Turn Conversation* | 2505.06120 | by analysis type | 1,183 | no | no |
| 4 | Sharma et al., *Towards Understanding Sycophancy* | 2310.13548 | by finding (claim headings) | 3,383 | yes (regression coefficients) | 50/95% credible, caption only |
| 5 | Stechly et al., *GPT-4 Doesn't Know It's Wrong* | 2310.12397 | by experiment | 1,246 | no | no |
| 6 | Tyen et al., *LLMs Cannot Find Reasoning Errors* | 2311.08516 | by experiment | 2,630 | no | no |
| 7 | Madaan et al., *Self-Refine* | 2303.17651 | table, then ablations | 827 | no | no |
| 8 | Zheng et al., *MT-Bench / LLM-as-a-Judge* | 2306.05685 | by limitation, then agreement | 2,532 | no | no |
| 9 | Bansal et al., *Does the Whole Exceed its Parts?* | 2006.14779 | by measure | 2,108 | no | 95%, caption only |
| 10 | Buçinca et al., *To Trust or to Think* | 2102.09692 | by measure | 720 | no | no |
| 11 | Vasconcelos et al., *Explanations Can Reduce Overreliance* | 2212.06823 | by study, then by hypothesis | 3,128 | yes (posterior means) | 95% credible, in prose |
| 12 | Si et al., *Can LLMs Generate Novel Research Ideas?* | 2409.04109 | by statistical test | 1,957 | yes (means and SDs, correlations) | no |
| 13 | Valmeekam et al., *Self-critiquing Their Own Plans* | 2310.08118 | by experiment | 758 | no | no |
| 14 | Olausson et al., *Is Self-Repair a Silver Bullet?* | 2306.09896 | by finding | 2,289 | yes (ratios, SDs) | no |
| 15 | Card et al., *With Little Power Comes Great Responsibility* | 2010.06595 | by evaluation type | 4,095 | yes (MDEs throughout) | no |
| 16 | Kabir et al., *Who Answers It Better?* | 2308.02312 | by research question | 2,430 | no | no |
| 17 | Anon. 2026, *Mid-2025 LLM-Assistance on Novice Performance in Biology* | 2602.16703 | by finding (headings state nulls) | 1,716 | yes (RR, OR) | 95% CI and CrI, in prose |
| 18 | Anon. 2026, *Reliability without Validity* | 2606.19544 | by hypothesis | 1,757 | yes (deltas in pp) | no |
| 19 | Wang et al., *LLMs are not Fair Evaluators* | 2305.17926 | by experiment | 1,261 | no | no |

**Organisation, counted.** By experiment or study: 8 (Huang, Stechly, Tyen,
Valmeekam, Vasconcelos, Wang, Laban, Olausson in part). By finding, with the heading
stating the claim: 6 (Sharma, Si, Olausson, Kamoi, 2602.16703, 2606.19544). By
measure or instrument: 3 (Bansal, Buçinca, Madaan). By research question: 1 (Kabir,
the only paper numbering RQ1 through RQ8 in its headings). By statistical test: 1
(Si, whose three subsections are three aggregation levels of the same comparison).

None of the 19 organises the results by table.

---

## Structure and headings (verbatim collection)

### Subsection headings that state the finding

Sharma et al. (2310.13548):
> 3.1 AI Assistants Can Give Biased Feedback
> 3.2 AI Assistants Can Be Easily Swayed
> 3.3 AI Assistants Can Provide Answers that Conform to User Beliefs
> 3.4 AI Assistant Responses Sometimes Mimic User Mistakes
> 4.3.1 Humans and PMs Sometimes Prefer Sycophantic Responses

Si et al. (2409.04109):
> 5 Main Result: AI Ideas Are Rated More Novel Than Expert Ideas
> 6.1 Human Experts May Not Be Giving Their Best Ideas
> 6.3 Reviewing Ideas is Inherently Subjective
> 7.1 LLMs Lack Diversity in Idea Generation
> 7.2 LLMs Cannot Evaluate Ideas Reliably

Olausson et al. (2306.09896):
> 4.1 Self-repair requires strong models and diverse initial samples
> 4.2 GPT-4 feedback improves GPT-3.5 repair
> 4.3 Human feedback significantly improves the success rate of GPT-4 repair

2602.16703, the closest structural analogue to this paper:
> 2.2 LLM access did not significantly increase success across the viral reverse genetics workflow
> 2.3 Post-hoc pooled analysis suggests modest uplift across core task sequence
> 2.4 LLM access accelerates progress through experimental protocols
> 2.5 Exploratory subgroup analyses did not identify effect moderators
> 2.6 LLM usage patterns and perceived usefulness suggest capability and elicitation constraints

2606.19544:
> 4.1 Kappa Deflation Is Universal
> 4.3 Cross-Benchmark Rank Instability
> 4.6 Consistency Falls on Hard Benchmarks
> 4.7 The Consistency-Bias Paradox

Zheng et al. (2306.05685), one instance among topic headings:
> 4.2 High agreement between GPT-4 and Humans

Note that four of these five sets state a limit or a failure in a heading, not only a
success. A heading that names a null is normal in this literature.

### Headings phrased as a question

Huang et al. (2310.01798):
> 3 Can Large Language Models Self-Correct Reasoning?
> 3.2.1 Why does the performance not increase, but instead decrease?

Sharma et al. (2310.13548):
> 4.1 What Behavior Is Incentivized By Human Preference Data?
> 4.3 How Often Do Humans and Preference Models Prefer Truthful Responses?
> 4.3.2 How Effective Is The Claude 2 PM At Reducing Sycophancy?

### Topic headings (the majority form)

Stechly et al.: `4.1 Backprompting as Self-Critique`, `4.2 Verification by LLM`,
`4.3 Inside the Backprompt Chain`. Laban et al.: `6.1 Average Performance
Findings`, `6.2 Aptitude vs. Reliability Analysis`, `6.3 Gradual Sharding
Experiment`. Valmeekam et al.: `5.1 Effect of self-critiquing on plan generation`.
Buçinca et al.: `4.1 Objective measures`, `4.2 Subjective measures`, `4.3 Subjective
measures vs. objective measures`. Bansal et al.: `4.1 Effect of Explanation on Team
performance`.

### Research-question headings

Kabir et al. (2308.02312) is the only paper in the corpus that numbers RQs in the
headings, and it splits results by instrument first, then RQ:
> 4. Manual Analysis Results / 4.1 RQ1: Overall Correctness and Quality
> 4.2 RQ2: Fine-Grained Issues / 4.3 RQ3: Effects of Question Type
> 6. User Study Results / 6.1 RQ6: Differentiating ChatGPT answers from SO answers
> 6.2 RQ7: Assessing Correctness of ChatGPT Answers / 6.3 RQ8: Factors for User Preference

### Bolded run-in paragraph headings

Nine of 19 papers use them in the results section. Counts of distinct run-ins:
Sharma 23, Zheng 14, Huang 9, Kamoi 7 (at subsection level), Card 5, Olausson 3,
Tyen 3, Bansal 2, Vasconcelos 2.

**The strictest template is Sharma et al.**, which repeats a fixed pair inside every
subsection:
> **Experiment Details** ... **Results** ...

and varies it only when the design demands: `**Dataset**`, `**Model**`, `**Best-of-N
Experiment Details**`, `**RLHF Experiment Details**`, `**Prompt and Response
Details**`, `**PM Results**`, `**Human Data Collection**`, `**Human Feedback
Results**`.

**Run-ins that name the finding rather than the topic** are the more useful form and
the rarer one. Verbatim:

- Kamoi et al.: `**Negative Results.**`, `**Unfair Settings.**`, `**Tasks in which
  Self-Correction is Exceptionally Effective.**`, `**Bottleneck is in Feedback
  Generation.**`, `**Unfair self-correction with external information.**`
- Bansal et al.: `**We did not observe a significant difference between
  Explain-Top-1 and Explain-Top-2**`
- Madaan et al.: `**Non-monotonic increase in output quality for acronym
  generation**`
- Buçinca et al.: `**Detailed analysis of decisions when model predictions were
  incorrect.**`
- Huang et al.: `**Empirical Analysis.**`, `**Intuitive Explanation.**`
- Olausson et al.: `**Data collection methodology.**`, `**Quantitative Analysis.**`,
  `**Qualitative Analysis.**`
- Zheng et al.: `**Position bias**`, `**Verbosity bias**`, `**Self-enhancement
  bias.**`, `**Limited capability in grading math and reasoning questions.**`,
  `**Swapping positions.**`, `**Few-shot judge.**`
- Tyen et al.: `**Direct trace-level prompting**`, `**Direct step-level prompting**`,
  `**CoT step-level prompting**`

Terminal punctuation is inconsistent across the corpus and inside single papers
(Zheng writes both `**Position bias**` and `**Self-enhancement bias.**`). Pick one
and hold it.

### Where a subsection restates its own conclusion

Vasconcelos et al. is the only paper that splits every study into a short `Results`
subsection stating the estimation procedure and decision rule, then a separate
`Summary` subsection stating hypothesis-by-hypothesis outcomes. That separation is
what lets the null results sit in plain sight without argument around them.

---

## Statistical reporting conventions (with counts)

### What gets reported, out of 19 results sections

| Element | Count | Papers |
|---|---|---|
| No inferential statistic of any kind | **11 / 19** | Huang, Kamoi, Laban, Stechly, Tyen, Madaan, Zheng, Valmeekam, Olausson, Wang, 2606.19544 |
| Named statistical test | 8 / 19 | Sharma, Bansal, Buçinca, Vasconcelos, Si, Card, Kabir, 2602.16703 |
| Any p-value in results prose | 6 / 19 | Bansal, Buçinca, Si, Card, Kabir, 2602.16703 |
| Exact p-values (not thresholds only) | 4 / 19 | Bansal, Buçinca, Card, 2602.16703 |
| Threshold p-values only (`p < .05`) | 2 / 19 | Si, Kabir |
| Effect size of any kind | 7 / 19 | Sharma, Vasconcelos, Si, Olausson, Card, 2602.16703, 2606.19544 |
| Effect size with an interval attached | **3 / 19** | Sharma, Vasconcelos, 2602.16703 |
| Confidence or credible interval anywhere in results | **4 / 19** | Sharma (caption), Bansal (caption), Vasconcelos (prose), 2602.16703 (prose and caption) |
| Confidence or credible interval in results **prose** | **2 / 19** | Vasconcelos, 2602.16703 |
| Sample size stated inline for the estimate | 12 / 19 | Bansal, Buçinca, Vasconcelos, Si, Card, Kabir, Olausson, Tyen, Zheng, Huang, 2602.16703, 2606.19544 |
| Standard deviations or standard errors | 6 / 19 | Sharma, Bansal, Si, Olausson, Card, Huang (footnote) |

**The split is disciplinary, not chronological.** Every paper that reports p-values,
CIs, or a named test is either an HCI paper with human subjects (Bansal, Buçinca,
Vasconcelos, Kabir), an NLP paper whose central object is human evaluation (Si,
Card), or a clinical-trial-style report (2602.16703). Every paper in the
self-correction line proper (Huang, Kamoi, Stechly, Tyen, Madaan, Valmeekam,
Olausson, Laban, Wang, Zheng) reports **zero** inferential statistics in its results
section. Sharma reports a Bayesian model with credible intervals but confines the
intervals to a figure caption.

This paper sits across both. It runs an automated multi-model evaluation (the first
tradition) and a blind human pairwise comparison with a pre-committed threshold (the
second). The reporting standard that applies is the second one, because that is
where the contested claim lives.

### Fullest forms observed, verbatim

Bansal et al. (2006.14779), test statistic plus exact p, repeated per dataset:
> the difference was not significant (z=0.85, p=.40). The same was true for Amzbook
> (z=0.81, p=.42) and LSAT (z=0.42, p=.68).

Buçinca et al. (2102.09692), test, df, N, statistic, exact p:
> Distributions of overreliance, human error, and correctness were significantly
> different across categories for overall performance (χ²(2,N=663)=13.30, p=.0013).

Buçinca et al., a null with its statistic still reported and flagged `n.s.`:
> Low NFC participants reported on average higher trust (M=3.92) than high NFC
> participants (M=3.70), albeit not significantly so (F_{1,172.1}=2.89, n.s.).

Card et al. (2010.06595), statistic plus exact p plus the inference declined:
> However, in our case, this correlation is not significant (Kendall's τ=-.07,
> p=.32) and so it is difficult to draw strong conclusions.

Si et al. (2409.04109), means with SDs, named test, correction, threshold p:
> Both AI Ideas (μ=5.64±σ=1.76) and AI Ideas + Human Rerank (μ=5.81±σ=1.66) are
> significantly better than Human Ideas (μ=4.84±σ=1.79) on the novelty score
> (p<0.01).

2602.16703, the fullest form in the corpus: counts, rates, effect size, interval,
exact p, test name, and analysis set, all in one sentence:
> We did not observe a significant difference in the primary outcome, in which only
> 4 of 77 participants (5.2%) in the LLM arm and 5 of 76 (6.6%) in the Internet arm
> met the completion criteria (FAS: Risk Ratio 0.79, 95% CI 0.24-2.62; P = 0.759,
> one-sided Fisher's exact test) (Figure 3, Table 8).

2602.16703, Bayesian estimate with interval and posterior probability, and the
uncertainty named in the same clause:
> the model estimated a risk ratio of 1.32 (95% CrI 0.69-2.35, Pr(RR)>1=77.8%
> (Figure 3)), indicating a positive but uncertain amount of improvement associated
> with LLM access.

Vasconcelos et al. (2212.06823), the decision rule stated inside the results before
any result:
> We adopt the convention of saying that a comparison is notable if the 95% credible
> interval of the posterior distribution excludes 0 and the estimate of the mean is
> positive or negative (depending on the direction of the hypothesis).

### p-value formatting, counted

- Leading zero dropped, two or more decimals, lower-case italic p: Bansal
  (`p=.40`, `p=.42`, `p=.68`, `p=.24`, `p=.22`, `p=.64`, `p=.31`, `p=.28`,
  `p=.87`, `p=.19`, `p=.43`), Buçinca (`p=.0013`, `p=.009`, `p=.02`), Card
  (`p=.32`). 3 papers.
- Leading zero kept, capital P: 2602.16703 (`P = 0.759`, `P = 0.059`, `P = 0.025`,
  `P = 0.90`, `P = 0.27`, `P = 0.12`, `P = 0.38`, `P = 0.020`, `P = 0.075`,
  `P = 0.34`, `P = 0.82`). 1 paper.
- Thresholds only: Si (`p<0.05`, `p<0.01`, `p<0.001` plus star notation in table
  footers), Kabir (`p-value < 0.001`, `p-value < 0.05`, `p-value < 0.01`). 2 papers.
- Very small p written out: Buçinca once, as `p ≪ .0001`.
- **Scientific notation: 0 of 19.** No paper in this corpus writes a p-value as
  `1.5 × 10^-11`.

Star notation appears only in table footers, never in prose, and only in Si:
`*p<0.05; **p<0.01; ***p<0.001`.

### Sample size and underpowered subgroups, disclosed inline

Every disclosure in the corpus is a plain statement of the limit plus what was done
about it. Nine verbatim instances:

> We omit the analysis on HotpotQA because the sample size used in the source paper
> is quite small, which may not produce meaningful statistics. (Huang, footnote 3)

> As our dataset is highly skewed and only contains 45 correct_ans traces per task,
> we leave to future work to assess the effectiveness of backtracking in a more
> comprehensive way. (Tyen, 4.1.2)

> Due to limited data and small differences, our study cannot determine whether the
> models exhibit a self-enhancement bias. (Zheng, 3.3)

> Low completion rates for the individual tasks limited the statistical power of the
> analyses for the primary and secondary outcomes. (2602.16703, 2.3)

> Due to the low number of outcomes for Tasks 3-5, we conducted these analyses
> exclusively on Task 2 (cell culture). (2602.16703, 2.5)

> These analyses were pre-specified in the study's statistical analysis plan prior to
> unblinding, except for LLM and YouTube usage intensity. (2602.16703, 2.5)

> Our sample size comes from a power analysis done on pilot data. (Vasconcelos,
> repeated in the Participants subsection of every study)

> We caution against generalizing this finding beyond our setting: the measurement
> uses a single pairwise rubric and a fixed length-differential operationalization,
> and we do not claim that verbosity bias has been eliminated under arbitrary rubric
> or task variation. (2606.19544, 4.8)

> Underpowered experiments do not provide convincing evidence of progress. (Card, 6)

### Tables and figures against prose

- Median numeric density in results prose: **1.2 numbers per 100 words** (range 0.1
  in Kamoi to 5.2 in 2602.16703; 2606.19544 is an outlier at 13.9). Fifteen of 19
  fall below 2.1.
- Median reference density: **4.4 figure/table references per 1,000 words** (range
  1.6 in Kabir to 15.7 in 2602.16703).
- Every paper announces the exhibit and then states only the numbers it will reason
  from: `Table 1 summarizes the results` (Huang), `Table 1 summarizes results from
  the simulation` (Laban), `Table 2 summarizes the results` (Stechly), `Table 3
  showcases the LLM's performance` (Valmeekam), `The results are shown in Table 6,
  with a complete task-by-task breakdown in Appendix C` (Olausson).
- The extreme case is Madaan et al., whose entire section 5 Results is 82 words and
  does nothing but point at a table:
  > Our main results are presented in Table 3. As shown, Self-Refine significantly
  > improves the quality of outputs generated by the baseline method across all tasks.
- Bansal et al. (3.1 numbers per 100 words) is the corpus's most number-dense
  results prose and is still lower than this paper's draft.

---

## Verbatim catalogue: how negative results are stated

Six constructions, all attested. Each entry is verbatim with its source.

### A. Observation verb, no claim about existence

> We observe that, after self-correction, the model's performance drops on all
> benchmarks. (Huang, 3.2)

> In Appendix B, we test different prompts but find that the performance still does
> not improve. (Huang, 3.2.2)

> We did not observe a significant difference between Explain-Top-1 and
> Explain-Top-2, or that H1 was not supported. (Bansal, 4.1)

> We did not observe significant improvements over the confidence baseline by
> displaying explanations. (Bansal, 4.1)

> Though the third explanation strategy was designed to alleviate the limitations of
> Explain-Top-1 and Explain-Top-2 in our experiments, we did not observe improvements
> from using Adaptive explanations. (Bansal, 4.1)

> We do not observe significant differences between AI-generated ideas and
> human-written ideas on the other metrics. (Si, 5.1)

> We did not observe significant differences in the time-to-completion or median
> attempt counts for the primary composite outcome, or other individual tasks.
> (2602.16703, 2.4)

### B. Flat statement that the thing does not work

> Additional test-time compute (reasoning tokens) does not help models navigate
> multi-turn underspecification, as the two reasoning models included in the
> experiment (o3, Deepseek-R1) deteriorate in similar ways to non-reasoning models.
> (Laban, 6.1)

> From the plots, we can see that for the GPT-3.5 model, the pass@t is lower than or
> equal to the corresponding baseline (black line) for all settings of n_p, n_fr,
> clearly showing that self-repair is not an effective strategy for GPT-3.5.
> (Olausson, 4.1)

> The weighted F1 scores show that prompting for mistakes is a poor strategy for
> determining the correctness of the final answer. (Tyen, 3.3)

> Consequently, we conclude that no major work shows successful self-correction of
> responses from LLMs using feedback generated by prompting themselves under fair
> settings in general tasks. (Kamoi, 4)

> Additionally, when we employ their prompt to refine our outputs, performance even
> diminishes. (Huang, 4)

> performance plummets, only a single instance of the 100 was answered correctly.
> (Stechly, 4.1)

> In other words: blindfolded guessing does just as well as careful, crafted
> feedback. (Stechly, 4.1)

### C. Hedged difficulty

> All three models appear to struggle with our mistake finding dataset. (Tyen, 3.1)

> Interestingly, the amount of feedback provided to the LLM seems to have minimal
> influence on its performance improvement. (Valmeekam, 5.3)

> the detailed feedback on invalid plans doesn't appear to significantly enhance the
> LLM's performance. (Valmeekam, 5.3)

> fixing n_p and increasing n_fr [...] does not appear to be worth the additional
> cost incurred, giving very marginal gains at higher budgets and even decreasing
> performance at lower budgets. (Olausson, 4.1)

> Our overall conclusion is that, despite the common-sense nature of this domain,
> the LLM's verification powers are surprisingly weak. (Stechly, 4.2)

### D. Directional but not significant, named precisely

> They also overrelied less, but not significantly so. (Buçinca, 4.1)

> Overall, participants reported higher trust in the AI in simple explainable AI
> conditions compared to cognitive forcing functions, albeit not significantly so.
> (Buçinca, 4.2)

> Success rates were numerically higher in the LLM arm for four of the five tasks
> (2602.16703, 2.2)

> For comprehensiveness, the average ratings are 3.89 and 3.98 for SO and ChatGPT,
> but this result is not statistically significant. (Kabir, 6)

> Model aptitude degrades in a non-significant way between the full and sharded
> settings, with an average drop of 16%. (Laban, 6.2)

The corpus vocabulary for this state is: **not significant**, **numerically
higher**, **albeit not significantly so**, **but not significantly so**,
**directional**. Never "similar", never "the same", never "no effect".

### E. Negative result given its consequence in the same breath

No paper in the corpus leaves a negative hanging. Every one attaches either a
mechanism or a research consequence immediately.

> As a result, we could not reject our hypothesis H2 that Explain-Top-1 performs
> similar to simply showing confidence. This result motivates the need to develop
> new AI systems and explanation methods that provide true value to team performance
> by supplementing the model's confidence, perhaps working in tandem with confidence
> scores. (Bansal, 4.1)

> Unfortunately, as our experiments show, the effect of using Adaptive did not seem
> sufficient to increase final team accuracy, possibly for two reasons: (1) in high
> confidence regions [...] (2) In low confidence regions [...] This indicates that
> more sophisticated strategies are needed to support humans in both situations.
> (Bansal, 4.1)

> We hypothesise that LLMs' inability to find mistakes is a main contributing factor
> to why LLMs are unable to self-correct reasoning errors. If LLMs are unable to
> identify mistakes, it should be no surprise that they are unable to self-correct
> either. (Tyen, 3.1)

> Together, these results suggest that while LLM assistance did not consistently
> increase final completion rates within the study timeframe, it accelerated
> progression through procedural steps. (2602.16703, 2.4)

### F. Inconclusive declared as inconclusive

> Due to limited data and small differences, our study cannot determine whether the
> models exhibit a self-enhancement bias. Conducting a controlled study is
> challenging because we cannot easily rephrase a response to fit the style of
> another model without changing the quality. (Zheng, 3.3)

> However, high consistency may not imply high accuracy and we are not sure whether
> the few-shot examples will introduce new biases. (Zheng, 3.4)

> However, in our case, this correlation is not significant (Kendall's τ=-.07,
> p=.32) and so it is difficult to draw strong conclusions. (Card, 5.1)

> Our results here and in the next few subsections are so far conflicting.
> (Stechly, 4.1)

> Whether bad feedback itself is worsening the results, or it's merely the case that
> correct responses tend to be earlier in the backprompt sequence [...] is unclear.
> (Stechly, 4.1)

---

## Verbatim catalogue: how null and failed pre-registered tests are reported

**Say this plainly: the template barely exists in this literature.** Of the 19
results sections, **3** report an outcome against a criterion committed to before the
data were seen, and only **2** name a formal pre-registration. **Zero of the eight
anchor self-correction papers pre-registers anything.** A fourth paper (Bansal)
states numbered hypotheses in its design section and reports non-support in the
results without claiming pre-registration.

That scarcity is itself a finding for this paper. There is no ACL-side convention to
copy, and a referee will not have a mental template for it either. The available
models come from CHI/CSCW (Vasconcelos, Bansal) and from clinical-trial reporting
(2602.16703). Following one of them visibly, and saying which, is worth more than
inventing a house style.

### 1. Failed pre-registered primary outcome, made a numbered subsection heading

2602.16703, section 2.2. The heading states the null; the first sentence states what
was pre-registered; the second states the outcome with counts, rates, effect size,
interval, exact p, test, and analysis set:

> **2.2 LLM access did not significantly increase success across the viral reverse
> genetics workflow**
>
> The pre-registered primary outcome was defined as the successful completion of the
> core reverse genetics sequence: cell culture, molecular cloning, and virus
> production (Tasks 2-4). We did not observe a significant difference in the primary
> outcome, in which only 4 of 77 participants (5.2%) in the LLM arm and 5 of 76
> (6.6%) in the Internet arm met the completion criteria (FAS: Risk Ratio 0.79, 95%
> CI 0.24-2.62; P = 0.759, one-sided Fisher's exact test) (Figure 3, Table 8).

The paper's contribution survives because the following four subsections report what
the study *did* establish, each with its own heading, and the last synthesis sentence
states both halves without ranking them rhetorically (quoted in E above).

### 2. Post-hoc analysis labelled post-hoc, in the heading and the verb

> **2.3 Post-hoc pooled analysis suggests modest uplift across core task sequence**
>
> Low completion rates for the individual tasks limited the statistical power of the
> analyses for the primary and secondary outcomes. To address this, we performed a
> post-hoc analysis where we fit a range of Bayesian regression models to aggregate
> evidence across the entire five-task workflow. (2602.16703, 2.3)

Note the ordering: the power limit is stated first, as the reason for the post-hoc
analysis, not as an excuse after it.

### 3. Hypothesis-by-hypothesis reporting, non-support stated with its reason

Vasconcelos et al. (2212.06823), 5.6, the same paragraph reporting supported and
unsupported hypotheses in sequence, with no change of tone:

> We do not find support for H1c; therefore not providing empirical evidence for the
> following claim: in medium-difficulty tasks, there is more overreliance in the
> prediction condition than in the explanation condition. This may be in due part to
> the fact that this condition is not hard enough to see the reductions in cost that
> we expect to see with explanations.

> We do not find support for H1e; therefore, not providing empirical evidence for the
> following claim: there is an interaction effect between participants' Need for
> Cognition (NFC) scores and the type of explanation modality (highlights of
> lackthereof) when measuring overreliance. This could be because the hard task is
> too difficult to demonstrate differences in behavior across peoples' NFC, since most
> people are likely to overrely on the AI's prediction anyway.

And in a table caption, so a reader scanning the exhibits cannot miss it:

> Table 2. Results from study 1. We do not find support for our hypothesis that there
> is an interaction effect of AI Condition and a participants' Need for Cognition
> (NFC) score. We hypothesized that people who are more likely to engage in
> cognitively demanding tasks would have little differences in overreliance levels
> regardless of whether AI explanations were provided or not. However, we did not
> find support for this, which we hypothesize could be due to the fact that, in the
> hard task, even participants with high propensities to engage in effortful thinking
> are likely to overrely.

### 4. Failure to reject, stated as failure to reject

Bansal et al. (2006.14779), 4.1:

> As a result, we could not reject our hypothesis H2 that Explain-Top-1 performs
> similar to simply showing confidence.

> As a result, we could not reject the null hypotheses for either H3 or H4.

### 5. A priori prediction refuted, named and quantified

2606.19544, 4.5, where the section heading is neutral and the refutation is the
second sentence:

> Hypothesis 5 predicted that RewardBench would generate κ values no larger than 0.05
> because it placed all correct human labels in the A position. As we report in Table
> 2 the benchmark data is not consistent with this hypothesis.

### 6. Threshold approached but not cleared

2606.19544, 4.4. This is the closest wording in the corpus to this paper's 56.2%
against a 65% bar:

> Hypothesis 4 predicted an MT-Bench κ spread of at most 5 pp. As we report in Table
> 2, we observe 13.5 pp (0.376 to 0.511) across all 21 judges, narrowing to 6.5 pp
> within the top ten and approaching the H4 ceiling.

### 7. Prediction met only in part

2606.19544, 4.2:

> H2 predicted that the three thinking-architecture judges (GPT-5.4, Gemini 3.1 Pro,
> DeepSeek V3.2) would all fall below 0.05; only Gemini 3.1 Pro (0.038) does so. And
> so, while they reduce position bias relative to cost-efficient models, they do not
> eliminate it.

### 8. Exploratory work marked exploratory, with the inferential claim withheld

Vasconcelos et al., 7, 7.2 and 7.5, three separate statements to the same effect:

> This experiment is exploratory and therefore does not have pre-registration.

> We did not have pre-registered hypotheses for two reasons: (1) this is an
> exploratory study to find if there is a floor effect and (2) our hypotheses relating
> explanation difficulty and overreliance have been confirmed in study 2.

> Because we didn't pre-register any hypotheses for this study, we report the means
> and credible intervals for all the pairwise comparisons here, but don't indicate
> whether the differences are credible.

### 9. Deviation from the pre-registration disclosed in a footnote

Vasconcelos et al., 8.3, footnote 4:

> The pre-registration does not specify a blocked study design.

### 10. Exploratory subgroup analysis with a null, and the pre-specification status
stated for each covariate

> **2.5 Exploratory subgroup analyses did not identify effect moderators**
>
> These analyses were pre-specified in the study's statistical analysis plan prior to
> unblinding, except for LLM and YouTube usage intensity.
>
> Likelihood ratio tests comparing models with and without treatment-by-covariate
> interaction terms did not support moderation by nonverbal reasoning (χ²=0.02, df=1,
> P=0.90), prior biology experience (χ²=1.21, df=1, P=0.27), prior LLM experience
> (χ²=2.43, df=1, P=0.12), or YouTube searches (χ²=0.77, df=1, P=0.38) (Table 15).
> [...] Overall, these analyses identified no subgroups showing substantially
> different treatment effects. (2602.16703, 2.5)

---

## Register: verbs, hedging, where claims stop

### Hedging density

Hedging tokens (`appears`, `seems`, `suggests`, `indicates`, `may`, `might`,
`could`, `likely`, `tends to`, `is consistent with`) per 1,000 words of results
prose. Median across the corpus: **4.9**.

Highest: Valmeekam 10.6, Bansal 10.9, Laban 10.1, Olausson 8.3, Si 8.2.
Lowest: Kamoi 0.6, 2606.19544 1.7, Madaan 2.4, Buçinca 2.8.

The pattern is not "more confident papers hedge less". Laban and Bansal hedge most
and both make strong claims; they hedge the *mechanism* while stating the
*measurement* flatly. Kamoi hedges least because it is a survey stating other
people's results as facts.

### Observation verbs against assertion verbs

Assertion constructions (`we find`, `we show`, `we demonstrate`, `we conclude`,
`our results show`, `this demonstrates`) per 1,000 words:

Kabir 6.2, Sharma 4.7, Huang 2.4, Vasconcelos 2.6, Card 2.0, Reliability 2.8, Zheng
2.8, Tyen 2.3, Olausson 1.7, Laban 5.9, Si 3.1, Wang 4.8, Stechly 0.0, Valmeekam
0.0, Buçinca 0.0, **2602.16703 0.0**.

**The null-result papers use the fewest assertion verbs.** 2602.16703 reports 1,716
words of results without a single "we find" or "we show". It uses instead: *We did
not observe*, *the model estimated*, *Analysis of milestone success [...] showed*,
*Results showed*, *these results suggest*, *this more granular analysis revealed*.
Buçinca and Stechly likewise report their nulls with zero assertion verbs.

For a paper whose central results are negative, this is the discipline: **the verb
should describe what the measurement did, not what the authors decided.**

### Where claims stop

The line is consistent across the corpus. The results section states what was
measured and, at most, one clause of mechanism. Everything wider moves to
Discussion, Implications, or Limitations.

Huang, Results (3.2): flat measurement.
> We observe that, after self-correction, the model's performance drops on all
> benchmarks.

Huang, Discussion (5): the concession and the scope, neither of which appears in the
results.
> First, it is important to reiterate that we are not claiming self-correction is
> useless. [...] For instance, in the reasoning tasks studied in this paper, we did
> not observe any improvement through self-correction.

Tyen, Results (3.1): hedged. Tyen, same subsection's discussion paragraph:
unhedged plus an explicitly marked hypothesis.
> All three models appear to struggle with our mistake finding dataset.
> [...] We show that state-of-the-art LLMs clearly struggle with mistake finding,
> even in the most simple and unambiguous cases.
> [...] We hypothesise that LLMs' inability to find mistakes is a main contributing
> factor to why LLMs are unable to self-correct reasoning errors.

Laban, Results (6.1): the number. Laban, Limitations (9): the direction of the bias
in that number, which never appears in the results.
> Because of the overly simplified conditions of simulation, we believe the
> degradation observed in experiments is most likely an underestimate of LLM
> unreliability, and how frequently LLMs get lost in conversation in real-world
> settings.

Si: section 5 is the three statistical tests and nothing else. Section 6 raises the
alternative explanation for the authors' own positive result (`6.1 Human Experts May
Not Be Giving Their Best Ideas`). Section 7 is a separate limitations-of-LLMs
section. Three separate places, three separate jobs.

**No paper in the corpus states a deployment cost, a dollar figure, or a
recommendation to practitioners inside its results section.** Laban puts all of that
in section 7, `Implications`, with four subsections addressed to four audiences.
Card puts all of it in section 6, `Overall Recommendations`.

---

## Rules (numbered, checkable, each with evidence)

**R1. Report the pre-registered human comparison inside the Results section, not in
Methods and not only in Limitations.** Give it its own subsection. Evidence: all
three corpus papers with a pre-committed criterion report the outcome in the results
(2602.16703 §2.2, Vasconcelos §5.6, 2606.19544 §4.5). Zero report it only elsewhere.
Check: grep the results file for `56.2` and for the bar. Both must appear.

**R2. The subsection heading names the outcome, including when the outcome is a
null.** Evidence: `2.2 LLM access did not significantly increase success across the
viral reverse genetics workflow`; `2.5 Exploratory subgroup analyses did not identify
effect moderators`; `7.2 LLMs Cannot Evaluate Ideas Reliably`; `6.1 Human Experts May
Not Be Giving Their Best Ideas`. Check: every subsection heading can be read as a
sentence about the world, not a topic label.

**R3. State what was committed to, before stating what happened.** Evidence: "The
pre-registered primary outcome was defined as [...]. We did not observe a significant
difference in the primary outcome, in which [...]" (2602.16703 §2.2). "Hypothesis 4
predicted an MT-Bench κ spread of at most 5 pp. As we report in Table 2, we observe
13.5 pp" (2606.19544 §4.4). Check: the bar and the reason for the bar precede the
number that missed it.

**R4. Every inferential comparison reports n, effect size, and an interval, not a p
alone.** Evidence: only 3 of 19 corpus papers attach an interval to an effect size,
but all three are the ones doing human-subjects inference (Sharma, Vasconcelos,
2602.16703), which is what this paper does. A paper with intervals available and only
p-values printed is choosing the weaker of two options it already paid for. Check:
count inferential claims in the section; count intervals; the numbers match.

**R5. Format p-values as exact values to two or three decimals, or as `p < .001`
below that.** Evidence: 0 of 19 corpus papers use scientific notation. Bansal, Buçinca
and Card use `p=.40` style; 2602.16703 uses `P = 0.759`; Si and Kabir use thresholds.
A p of 5.7 × 10^-19 conveys nothing a reader can act on that `p < .001` plus the
effect size does not. Check: no `\times 10^{-` inside a p-value in the file.

**R6. A directional difference that misses significance is called directional or
numerical, never "similar" and never "no difference".** Evidence: "numerically higher
in the LLM arm for four of the five tasks" (2602.16703); "albeit not significantly so"
(Buçinca, twice); "but not significantly so" (Buçinca); "we could not reject our
hypothesis H2 that Explain-Top-1 performs similar to simply showing confidence"
(Bansal, framed as failure to reject rather than as equivalence). Check: no sentence
asserts that two conditions are equal.

**R7. Report the statistic even when the result is null.** Evidence: "albeit not
significantly so (F_{1,172.1}=2.89, n.s.)" (Buçinca); "did not support moderation by
nonverbal reasoning (χ²=0.02, df=1, P=0.90), prior biology experience (χ²=1.21, df=1,
P=0.27) [...]" (2602.16703). Check: every "not significant" in the file has a number
next to it.

**R8. Every negative result is followed immediately by a mechanism or a research
consequence, in the same paragraph.** Evidence: Bansal §4.1 twice, Tyen §3.1,
2602.16703 §2.4. Zero corpus instances of a negative left standing alone. Check: read
each negative paragraph's last sentence; it should say what follows from the result,
not restate it.

**R9. Post-hoc and exploratory analyses are labelled as such in the heading and in
the verb.** Evidence: `2.3 Post-hoc pooled analysis suggests modest uplift`;
`2.5 Exploratory subgroup analyses did not identify effect moderators`; "This
experiment is exploratory and therefore does not have pre-registration"
(Vasconcelos §7); "In an exploratory analysis, we find a interaction between AI
condition and Need for Cognition (NFC) in the medium task" (Vasconcelos §5.6). Check:
any analysis not fixed in advance says so where it appears, not only in an appendix.

**R10. State the power limit before the analysis that works around it, as its
reason.** Evidence: "Low completion rates for the individual tasks limited the
statistical power of the analyses for the primary and secondary outcomes. To address
this, we performed a post-hoc analysis [...]" (2602.16703 §2.3). "Due to the low
number of outcomes for Tasks 3-5, we conducted these analyses exclusively on Task 2"
(2602.16703 §2.5). Check: no underpowered cell is reported without its n and a
statement of what that n permits.

**R11. Use observation verbs for the paper's own negative and null results.**
Evidence: 2602.16703 reports 1,716 words of results with zero `we find`/`we show`
constructions; Buçinca and Stechly likewise report nulls at 0.0 assertion verbs per
1,000 words. Preferred forms attested: *we did not observe*, *we do not observe*,
*results showed*, *the model estimated*, *these results suggest*, *the analysis
revealed*, *we could not reject*, *the data are not consistent with*. Check: for
every claim in the section, ask whether the verb describes the measurement or the
authors' decision.

**R12. Interpretation, recommendations and cost projections leave the Results
section.** Evidence: no corpus results section states a dollar figure or a
practitioner recommendation. Laban puts all of it in §7 `Implications`; Card in §6
`Overall Recommendations`; Huang in §5 `Discussion`. Check: no sentence in the
results advises a reader what to do.

**R13. Announce the exhibit, then state only the numbers the argument uses.**
Evidence: median numeric density across the corpus is 1.2 numbers per 100 words;
Madaan's entire results section is 82 words pointing at one table. Check: numeric
density under roughly 2.5 per 100 words; any number appearing in both a table and
prose is one the following sentence reasons from.

**R14. Report the sample the estimate applies to, positively, instead of denying a
claim nobody made.** Evidence: "unless otherwise specified, results below refer to
the FAS" (2602.16703 §2.1); "Due to the low number of outcomes for Tasks 3-5, we
conducted these analyses exclusively on Task 2 (cell culture)" (2602.16703 §2.5); "we
restrict our analysis to Likert-scale comparisons, which was the most commonly
reported type of evaluation" (Card §5.1). Check: no sentence of the form "we do not
claim X".

**R15. Keep one convention for run-in headings and hold it for the whole section.**
Evidence: 9 of 19 papers use run-ins; Sharma's fixed `Experiment Details` / `Results`
pair is the cleanest, Zheng's mixed punctuation the least clean. Check: all run-ins
end the same way, and all are either topic labels or all are finding statements.

**R16. Give every coined term a definition on first use and then use it without
quotation marks.** Evidence: "We name this phenomenon Lost in Conversation: models
that achieve stellar (90%+) performance in the lab-like setting of fully-specified,
single-turn conversation struggle on the exact same tasks in a more realistic setting
when the conversation is underspecified and multi-turn" (Laban §6.1); "We define the
feedback sycophancy metric to be the mean difference in the feedback positivity
across datasets when a user implies they prefer and disprefer a passage of text"
(Sharma §3.1). Check: every coined term in the section has a defining sentence.

---

## Constructions to avoid, with evidence

**A1. "Significantly" with no test behind it.** Eight of 19 corpus papers do this
(Huang 8 uses / 0 tests, Zheng 9 / 0, Wang 5 / 0, Valmeekam 2 / 0, Olausson 2 / 0,
Madaan 1 / 0, Laban 1 / 0, Tyen 1 / 0), so it is common. It is still a defect, and
worse in a paper that also runs real tests, because the reader cannot tell which uses
are which. Madaan §5 is the clearest case: "Self-Refine significantly improves the
quality of outputs generated by the baseline method across all tasks" is the entire
inferential content of the section and rests on no test. Use *substantially*,
*markedly*, or a number.

**A2. A conclusion stated harder than the estimate.** Contrast Madaan §5 above with
2602.16703 §2.3, which has a positive pooled estimate and still writes "indicating a
positive but uncertain amount of improvement associated with LLM access".

**A3. Reporting only the analysis that cleared.** 2606.19544 reports all seven a
priori hypotheses including the refuted one and the two met in part. Vasconcelos
reports H1a through H1e including two non-supports. Selective reporting of the
hypotheses that worked is the failure this corpus's better papers are visibly
avoiding.

**A4. Equivalence claims from a null.** Nobody in the corpus writes "the two are the
same". Bansal, who has the strongest case for it (three separate non-significant
comparisons), writes "we could not reject our hypothesis H2 that Explain-Top-1
performs similar to simply showing confidence": failure to reject, not proof of
equivalence.

**A5. Pre-emptive rebuttal inside the results.** No corpus results section is laid out
as objection then answer. Where a genuine restriction exists it is stated once, as
the scope of the estimate (R14). The one place the corpus does raise an alternative
explanation for its own finding is Si §6.1, and that gets its own numbered subsection
in a separate section, not a defensive clause inside the main result.

**A6. Scientific-notation p-values.** 0 of 19. See R5.

**A7. Metaphor standing in for a measured quantity in a heading.** The corpus coins
terms (Laban's *Lost in Conversation*, Sharma's *feedback sycophancy*, 2606.19544's
*kappa deflation*) but each is defined the sentence it appears in and each names a
measured construct. A figure used as shorthand for "decline" without a definition is
not the same move.

**A8. An evaluative adjective smuggled into a count.** "Unnecessary revision" states
a judgment; "revision following an output the evaluator rated sufficient" states the
measurement. Corpus practice: Sharma names its constructs operationally in the same
sentence as the number ("the feedback positivity is the frequency with which a
modification results in feedback that is more positive than the baseline prompt").

**A9. A ratio of two ranges presented as an estimated quantity.** State the two
ranges. Corpus practice: 2606.19544 gives both spreads and then the ratio explicitly
as a comparison of spreads ("JudgeBench's κ spread on the same population is 60.4 pp,
a factor of 4.5× wider").

---

## Checklist

Run this against the results file before circulating.

- [ ] The pre-registered human comparison has its own subsection in Results.
- [ ] Its heading states the outcome.
- [ ] The bar, and when it was set, appear before the number that missed it.
- [ ] Every inferential comparison shows n, an effect size, and an interval.
- [ ] No p-value is in scientific notation; anything below .001 reads `p < .001`.
- [ ] Every "not significant" has a statistic beside it.
- [ ] No sentence claims two conditions are equal.
- [ ] Every negative result is followed by a mechanism or a consequence.
- [ ] Every post-hoc or exploratory analysis says so where it appears.
- [ ] Every underpowered cell states its n and what that n permits.
- [ ] The paper's own negative results use observation verbs.
- [ ] No dollar figure, deployment projection, or practitioner recommendation.
- [ ] Numeric density below roughly 2.5 numbers per 100 words of prose.
- [ ] No sentence of the form "we do not claim X".
- [ ] Run-in headings all punctuated the same way and all the same kind.
- [ ] Every coined term is defined on first use.
- [ ] Every number in prose is one the next sentence reasons from.

---

## How this paper's current results section measures up

Assessed against `paper/sections/results_v2.tex` (238 lines, 1,614 words of prose
after stripping LaTeX, tables and figures), read 2026-09-02.

### What already matches the corpus's better practice

1. **Subsection headings state findings.** `Models Mostly Decline to Revise`,
   `Quality Degrades Under Undirected Revision`, `Targeted Feedback Restores
   Quality` are in the style of Sharma, Si, Olausson and 2602.16703. This is the
   minority form in the corpus (6 of 19) and the stronger one. `The Revision Tax` is
   the exception: it labels a topic.
2. **One run-in heading is in the best corpus form.** `Probe phrasing, not output
   quality, controls whether a model revises.` states a finding. The other six
   (`Survival varies by model.`, `Domain variation.`, `Per-model caveats.`, `The
   revision cliff.`, `Over-elaboration rises with revision.`, `Pooled trajectory
   across all genuine revisions.`) are topic labels. Mixing the two kinds inside one
   section is the inconsistency R15 addresses.
3. **A named test with full statistics.** `χ² = 35.63, df = 4, p = 3.4 × 10^-7` gives
   test, statistic and df, which only 8 of 19 corpus papers do at all.
4. **One effect size and one interval already present.** Wilcoxon `r = 0.53` for the
   Llama cliff; `95% CI [36.1%, 42.3%]` for the sufficiency-then-revision rate. Two
   of 19 corpus papers put a CI in results prose, so the section already meets the
   higher standard once.
5. **Per-domain cell sizes disclosed with what they permit.** "per-domain cliff
   magnitudes should be read as directional estimates, not precise per-domain
   measurements" matches Tyen §4.1.2 and 2602.16703 §2.5 exactly.
6. **Compositional bias in the pooled trajectory disclosed unprompted.** No corpus
   paper discloses differential dropout in a pooled estimate this explicitly. This is
   above field practice and should stay.
7. **Measurement-instrument sensitivity disclosed.** The 135-versus-50 balanced-panel
   gap between a keyword classifier and a validated one is the kind of disclosure the
   corpus mostly omits. Keep it.
8. **"Significantly" is used six times and every use has a test behind it.** The
   section avoids A1, which eight of 19 corpus papers do not.

### Gaps, in priority order

**G1 (severe). The pre-registered null is not in the Results section at all.** The
blind human pairwise comparison (56.2%, 41/73, 95% CI [45.2%, 67.1%], against a
pre-set 65% bar with a CI excluding 50%) appears only in `methods.tex` under
`\paragraph{Reversibility}` and as the eighth item in a limitations list in
`discussion.tex`. All three corpus papers with a pre-committed criterion report the
outcome in the results; the closest analogue (2602.16703) makes it subsection 2.2
with a heading that states the null. A reader of the Results section as it stands
does not learn that the paper ran a human validation, let alone that it missed its
bar. Fix: a subsection in Results, after `Quality Degrades Under Undirected
Revision`, on the 2602.16703 model. State the bar and when it was set; state n,
proportion, CI, and the agreement statistic (κ = 0.703); state that the bar was not
cleared; then state the consequence, which the Methods text already words well ("the
pointwise quality degradation is real but not large enough to reliably flip a blind
pairwise preference once meta-commentary is removed").

**G2. Four of five inferential comparisons have no effect size.** Only the Llama
cliff shows `r = 0.53`. The Wilcoxon r is computable for the all-balanced cliff, the
targeted-feedback comparison, and the per-domain tests, and Cramér's V for the χ².
See R4.

**G3. No interval on either of the two estimates the abstract sells.** The -0.74
cliff and the +1.16 targeted gain each appear with a p-value and no interval, and
both are quoted in the abstract and the introduction figure caption. Given that the
paper already computes a CI elsewhere, the omission is conspicuous. See R4.

**G4. Seven p-values are in scientific notation.** `1.01 × 10^-4`, `3.3 × 10^-6`,
`3.76 × 10^-4`, `1.8 × 10^-5`, `5.7 × 10^-19`, `3.4 × 10^-7`, `9.2 × 10^-12`. Zero of
19 corpus papers do this. `p < .001` plus the effect size and interval is the field
form, and a p of 5.7 × 10^-19 invites a referee to ask what the n and the dependence
structure were rather than to read the effect. See R5.

**G5. Two results named in the paper brief are absent from this section.** "Among
revisions that do move quality, 70% move it down (p = 1.5 × 10^-11)" does not appear
in `results_v2.tex` in any form. "Every model's first attempt rates highest" appears
only as the derived statement `t* = Turn 1 for all six models` inside the revision-tax
subsection, which is a different claim (optimal stopping point, not per-model turn-1
ranking) and is placed under a heading about cost. Either these analyses exist and
belong in the quality subsection, or the brief and abstract need correcting to match
what the section reports. Do not add either number without the script that produced
it.

**G6. The revision tax subsection states a dollar projection in the Results.** "$323
per year (Gemini 2.5 Flash) and $65,678 per year (Claude Sonnet 4) for a 500-person
organization" is an extrapolation from token counts and 2025 list prices, hedged as
"an order-of-magnitude indication rather than a precise forecast". The hedge is
correct, and the sentence still does not belong here: no corpus results section
states a deployment cost. Laban's `Implications` and Card's `Overall
Recommendations` are the models. Move it; keep the token-waste percentages, which
are measured. See R12.

**G7. One pre-emptive rebuttal.** "We do not claim 'all models degrade'; we claim
that among models that continue revising, the only powered comparison (Llama, n = 45)
shows significant degradation." The restriction is real and worth stating; the
objection-and-answer shape is not. Corpus form: state the sample the estimate applies
to and stop, as in "unless otherwise specified, results below refer to the FAS"
(2602.16703 §2.1). Rewrite as a positive statement of what the balanced panel
estimates. See R14.

**G8. Numeric density is 4.5 numbers per 100 words of prose against a corpus median
of 1.2.** Only 2602.16703 (5.2) and 2606.19544 (13.9) are higher, and both are
number-reporting papers by design. Several paragraphs restate values already in the
adjacent table: the `Pooled trajectory` paragraph repeats four of the five rows of
Table 4, and the `Domain variation` paragraph repeats most of Table 5. See R13.

**G9. "Unnecessary revision" imports a judgment into a count.** "Nearly two in five
sufficient outputs are followed by an unnecessary revision" treats the evaluator's
sufficiency rating as ground truth about necessity. The measured quantity is
"followed by a genuine revision at the next turn". See A8.

**G10. "Roughly 4-5× more than what it is asked to revise" is arithmetic on two
ranges.** 71.9 pp against 13.5 pp. State both ranges and let the reader see the
comparison, as 2606.19544 does. See A9.

**G11. "The revision cliff" is undefined shorthand.** It appears as a run-in heading
and then as a noun in `\paragraph{Per-model caveats.}` ("within-model cliff", "Its
stripped cliff of -0.69") and in three table captions, without a defining sentence.
Corpus practice is to define a coined term where it is introduced (Laban §6.1,
Sharma §3.1). Either define it once ("we refer to the Turn-1 to Turn-5 quality decline
on balanced-panel trials as X") or use the literal description throughout. See R16.

**G12. Two FLAG comments remain in the file.** `FLAG 2` records an unresolved
0.02 discrepancy between two computations of the balanced-panel cliff (-0.74 against
-0.76) attributed to differing stripping coverage. That is a live measurement
question sitting in a comment rather than in the reproducibility record. Resolve it
or move it to the analysis log before the file goes to a co-author.

### Overall

The section is stronger than the median corpus results section on disclosure of
measurement limits, and weaker than the human-subjects subset of the corpus on
inferential reporting. Its one structural failure is G1: a pre-registered test that
did not clear its bar is documented in the Methods and conceded in the Discussion but
never reported where a reader looks for results. Every corpus paper that faced the
same situation put it in the results, under a heading, with its numbers. Fixing G1,
G2, G3 and G6 would put this section at the top of the corpus for a negative-results
paper.
