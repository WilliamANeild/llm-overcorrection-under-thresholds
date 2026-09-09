# Reporting null results and unmet pre-registered thresholds: a 75-paper verbatim survey

Compiled 2026-09-06. Purpose: establish, from fetched primary sources, how four
literatures word (a) a statistically null result, (b) a pre-registered threshold that
was not cleared, (c) the difference between "no difference" and "we could not detect
one", and (d) an effect that is significant uncontrolled and null once a control is
added. Written to inform the wording of two results in the ARR October 2026
submission. Nothing in the project's analysis was changed by this work.

## 1. What was fetched, and how quotations were produced

Every quotation below was extracted mechanically from a full text held on disk, never
from an abstract, a search snippet, or memory. arXiv papers were fetched as
`arxiv.org/html/<id>` (LaTeXML HTML); PMC papers as NCBI E-utilities
`efetch db=pmc retmode=xml`, which returns the JATS full text for open-access items.
Both were tag-stripped, section headings were preserved as explicit markers, and
sentences were split and pattern-matched by script. Counts in section 3 are
script-produced, not eyeballed.

Two consequences of the extraction to keep in mind when reading the quotes:

- Inline math, figure and table cross-references, and citation markers were removed.
  Where a quotation contains a gap such as `( , rows 8-13; )` or `(all BF 01 > 6.6)`,
  the missing material is a reference or a rendered formula, not an omission of words.
- Sentence boundaries were placed by script. A few quotations run two sentences
  together where the source had an abbreviation or a decimal the splitter kept intact.
  No words were altered, inserted, or reordered.

**Retrieval dates.** The 47 self-correction papers were fetched into this project's
working directory on 2026-09-02 and 2026-09-03. Everything else was fetched
2026-09-06. Four of the older files were re-fetched live on 2026-09-06 and the exact
quoted strings confirmed present and unchanged (`2401.02009`, `2409.14509`,
`2206.05802`, `2511.22173`); those four are marked "verified 2026-09-06" in the
catalogues.

**Coverage this survey does not claim.** It reads English-language full texts only.
The clinical arm is limited to PMC open access, which under-represents the major
general medical journals. CSCW is represented only through its arXiv preprints, and
CHI likewise: the ACM Digital Library serves no machine-readable full text for
non-open items, so no paper is cited here from a venue whose text could not be
fetched. The self-correction arm is the corpus already assembled for this project and
is not a fresh systematic sample.

## 2. Corpus

75 papers in four arms.

### Arm A: LLM self-correction and self-refinement (47 papers, arXiv, retrieved 2026-09-02/03)

The project's existing corpus. Individually listed in `meta.json` in the working
directory; the ones quoted below are named in the catalogues with their arXiv
identifiers. Includes the canonical self-correction papers (Reflexion `2303.11366`,
Self-Refine `2303.17651`, `2310.01798`, `2310.12397`, `2311.08516`, `2406.01297`,
`2308.03188`, `2206.05802`).

### Arm B: NLP statistical methodology (2 papers, arXiv, retrieved 2026-09-06)

| ID | Title | Source |
|---|---|---|
| 2010.06595v1 | With Little Power Comes Great Responsibility | arXiv cs.CL |
| 1809.01448v1 | Appendix: Recommended Statistical Significance Tests for NLP Tasks | arXiv cs.CL |

The second is the appendix document only, 12k characters; it is counted in the corpus
but nothing is quoted from it.

### Arm C: HCI and behavioural experiments (12 papers, arXiv, retrieved 2026-09-06)

| ID | Title | Category |
|---|---|---|
| 2202.12883v4 | Human Detection of Political Speech Deepfakes across Transcripts, Audio, and Video | cs.HC |
| 2308.03903v1 | Average Estimates in Line Graphs Are Biased Toward Areas of Higher Variability | cs.HC |
| 2401.07058v1 | Does More Advice Help? The Effects of Second Opinions in AI-Assisted Decision Making | cs.HC |
| 2401.13744v3 | Conformal Prediction Sets Improve Human Decision Making | cs.LG |
| 2403.00582v2 | To Trust or Distrust AI: A Questionnaire Validation Study | cs.HC |
| 2409.09047v2 | AI Meets the Classroom: When Do Large Language Models Harm Learning? | cs.CY |
| 2410.03703v2 | Human Creativity in the Age of LLMs | cs.HC |
| 2411.02405v1 | Accuracy nudges are not effective against non-harmful deepfakes | cs.HC |
| 2411.14652v2 | Reranking partisan animosity in algorithmic social media feeds alters affective polarization | cs.CY |
| 2502.08554v1 | Fostering Appropriate Reliance on Large Language Models | cs.HC |
| 2604.04432v1 | Croissant Charts: Modulating the Performance of Normal Distribution Visualizations with Affordances | cs.HC |
| 2605.07912v3 | Sycophantic AI makes human interaction feel more effortful and less satisfying over time | cs.HC |

Selected by arXiv API queries `all:"preregistered" AND cat:cs.HC` and
`all:"pre-registered" AND cat:cs.HC`, taking items whose full HTML was available.

### Arm D: Psychology and clinical trials (14 papers, PMC, retrieved 2026-09-06)

| PMCID | Journal | Year | Title (truncated) |
|---|---|---|---|
| PMC6408382 | Royal Society Open Science | 2019 | Violent video game engagement is not associated with adolescents' aggressive behaviour: evidence from a registered report |
| PMC8742248 | Nature Human Behaviour | 2021 | A multi-country test of brief reappraisal interventions on emotions during the COVID-19 pandemic |
| PMC10123837 | Psychological Medicine | 2023 | Null results of oxytocin and vasopressin administration on mentalizing in a large fMRI sample |
| PMC10598029 | Nature Communications | 2023 | Nivolumab and ipilimumab in recurrent or refractory cancer of unknown primary: a phase II trial |
| PMC11825285 | J. Personality and Social Psychology | 2025 | Are women really (not) more talkative than men? A registered report of binary gender similarities |
| PMC12079821 | Molecular Cancer | 2025 | Perioperative nivolumab and chemotherapy in locally advanced squamous cell carcinoma of the oesophagus |
| PMC12618885 | Communications Psychology | 2025 | Improving statistical reporting in psychology |
| PMC13043209 | J. Experimental Psychology: General | 2025 | Arbitrary stimuli are not devalued by stopping action: a registered replication |
| PMC13442687 | J. Neuromuscular Diseases | 2026 | A randomized, double-blind, placebo-controlled study of losmapimod in patients with FSHD |
| PMC13450069 | J. Cross-Cultural Psychology | 2026 | Relationship Attributions Are Not Universal |
| PMC13456834 | Nature | 2026 | Investigating the replicability of the social and behavioural sciences |
| PMC13460065 | J. Medical Internet Research | 2026 | Internet Attachment-Based Compassion Therapy for Adults With Chronic Medical Conditions |
| PMC13504836 | BMJ Mental Health | 2026 | Therapist-guided and self-guided internet-based behavioural activation versus treatment as usual |
| PMC13520383 | Respiratory Research | 2026 | The LTI-01-2001 phase 2a trial of intrapleural LTI-01 |

## 3. Counts

Per-paper presence of each practice, computed by regular expression over the full
text of all 75 papers.

| Practice | Arm A: self-correction (47) | Arm B: NLP methods (2) | Arm C: HCI (12) | Arm D: psych/clinical (14) | Total (75) |
|---|---|---|---|---|---|
| Pre-registration named (`preregistered`, `preregistration`, `registered report`) | **0** | 1 | **12** | **12** | 25 |
| Any registration-family marker (adds `prespecified`, `osf.io`, `clinicaltrials.gov`, `ISRCTN`, `EudraCT`) | **1** | 1 | 12 | 14 | 28 |
| Equivalence test (`equivalence test`, `TOST`, `two one-sided`, `SESOI`, `ROPE`, `non-inferiority margin`) | **0** | 0 | **0** | **7** | 7 |
| Bayes factor or explicit evidence-for-the-null | **0** | 0 | **0** | **5** | 5 |
| Power analysis, minimum detectable effect, or sample-size calculation | **0** | 1 | 7 | 9 | 17 |
| At least one null-result sentence | 15 | 1 | 10 | 14 | 40 |

**Null-result sentences, total occurrences:** Arm A 32, Arm B 3, Arm C 57, Arm D 157
(249 overall).

Two things follow mechanically. Not one of the 47 self-correction papers names a
pre-registration, and not one reports an equivalence test, a Bayes factor, or a power
analysis. This corroborates the project's earlier survey finding (3 of 19 papers
reporting against any criterion fixed before the data, 2 naming a formal
pre-registration, none of the eight canonical papers pre-registering) from a larger and
differently-drawn sample. The convention this paper needs does not exist in its home
literature and has to be imported.

### Where null results sit

Sentence-level placement, by arm:

| Section | Arm A | Arm C | Arm D |
|---|---|---|---|
| Results | 4 | 32 | 63 |
| Methods | 8 | 8 | 63 |
| Discussion | 1 | 5 | 27 |
| Introduction | 7 | 1 | 0 |
| Limitations | 3 | 0 | 0 |
| Abstract | 0 | 4 | 0 |
| Conclusion | 2 | 1 | 0 |
| Appendix | 3 | 6 | 0 |
| Back-matter | 3 | 0 | 0 |
| Related work | 1 | 0 | 1 |

Paper-level placement (how many papers put at least one null somewhere):

| Section | Arm A (47) | Arm C (12) | Arm D (14) |
|---|---|---|---|
| Results | 4 | 8 | 11 |
| Discussion | 1 | 5 | 9 |
| Methods | 6 | 3 | 8 |
| Limitations | 2 | 0 | 0 |
| Abstract | 0 | 3 | 0 |
| Introduction | 4 | 1 | 0 |

The distribution differs sharply by arm and the difference is the whole story. In
Arms C and D a null is a Results-section object: it is where the reader expects a
result, it gets a test statistic and an interval, and it is carried into the
Discussion. In Arm A the modal location for a null is the Methods section or an
appendix, attached to an ablation or a sanity check, and only four of 47 papers state
a null in Results. Three Arm A papers state a null in Limitations, which is the
placement that reads as an apology. No Arm C or D paper does this.

Arm D's high Methods count is not nulls being buried. It is the pre-registered
analysis plan describing in advance what will count as a null, which is a different
act; see section 7.

## 4. Verbatim catalogue: null and non-significant results

Classified as **flat** (stated with its statistic and no editorial), **power-caveated**
(paired with a statement about what the design could detect), **uniformity** (the null
is used affirmatively as evidence that something does not vary), or **buried** (stated
only in an appendix, a methods aside, or a footnote-equivalent, with no reference from
the Results narrative).

### 4.1 Flat

> "The mean (SD) change from baseline at Week 48 was 0.011 (0.070) in the losmapimod
> group and 0.005 (0.068) in the placebo group; the difference in least squares means
> (2-sided 95% confidence interval [CI]) was 0.003 (-0.014, 0.020), p = 0.7501 ( )."
> — PMC13442687, Results

> "The primary endpoint, change in DUX4-driven gene expression in muscle biopsies
> performed in STIR + muscles, showed no differences from baseline in the losmapimod
> and placebo groups and no difference between groups."
> — PMC13442687, Results

> "Results from this model showed that neither the linear ( p = 0.402) nor the
> parabolic ( p = 0.624) predictors were statistically significant."
> — PMC6408382, Results

> "Violent game engagement was not a statistically significant linear ( p = 0.98) or
> nonlinear ( p = 0.07) predictor of aggressive behaviour."
> — PMC6408382, Results

> "In each sample, there was a significant main effect of Value (all p's < .005) and no
> significant interaction (all p's > .128)."
> — PMC13043209, Results

> "There was no significant difference in incidence of treatment failure within 7 days
> of initiation of treatment between LTI-01 and placebo groups using the protocol
> definition of treatment failure (Table )."
> — PMC13520383, Results

> "We found that reappraisal interventions (versus both control conditions combined)
> did not significantly change intentions to follow stay-at-home orders ( B = 0.009 ±
> 0.024, t (15.04) = 0.38, P = 0.709, d = 0.005, 95% CI = [-0.023, 0.032]) or to wash
> hands ( B = 0.034 ± 0.020, t (20,740) = 1.69, P = 0.091, d = 0.022, 95% CI = [-0.004,
> 0.048])."
> — PMC8742248, Results

> "No significant differences between treatment groups were found in accuracy ( a ) or
> reaction time ( b ) for either mentalizing or action understanding, when comparing
> either OT or AVP to placebo (see online Supplemental results)."
> — PMC10123837, Results

> "However, the proportion of participants willing to share the real news headline was
> not significantly different between the control and treatment conditions ( private:
> Fisher's exact p = 0.661, 1-sided p = 0.345; public: Fisher's exact p = 0.682,
> 1-sided p = 0.350)"
> — arXiv 2411.02405v1, Results

> "Fisher's exact tests showed that the accuracy nudge did not significantly affect
> participants' intentions to share the deepfake video ( private: Fisher's exact p =
> 0.429, 1-sided p = 0.229; public: Fisher's exact p = 0.300, 1-sided p = 0.169)."
> — arXiv 2411.02405v1, Results

> "No significant time×condition interactions were found for any DASS-21 subscale."
> — PMC13460065, Results

> "A similar analysis, reported in the , examined variation of replication success by
> publication year across papers and did not show a significant effect by year ( p =
> 0.14)."
> — PMC13456834, Results

Note the invariant across all twelve: the statistic travels with the sentence. Not one
says "was not significant" and stops.

### 4.2 Power-caveated

> "The study may have been underpowered to detect response differences, as the sample
> size calculation was based on the continuous CDRS-R rather than binary outcomes."
> — PMC13504836, Discussion

> "Finally, the trial was not powered to detect between-group differences in secondary
> measures and may therefore have been underpowered to identify smaller, yet potentially
> meaningful effects."
> — PMC13504836, Discussion

> "As a result, the trial was underpowered and all analyses were exploratory."
> — PMC10598029, Discussion

> "However, due to the limited sample size and the resulting low events per variable
> ratio, the analysis remains inconclusive regarding the predictive value of TMB in CUP
> patients with poor performance status and high disease burden , ."
> — PMC10598029, Discussion

> "While within-group improvements in self-compassion and self-criticism align with
> patterns observed in other CBIs [ , - ], and theoretical models link self-compassion
> with self-care behaviors and social connectedness [ - ], this study was likely
> underpowered to detect modest between-group differences given the high attrition rates
> observed [ ]."
> — PMC13460065, Discussion

> "Due to limited data and small differences, our study cannot determine whether the
> models exhibit a self-enhancement bias."
> — arXiv 2306.05685 (LLM-as-a-judge), Limitations

The last is the only power-shaped caveat found anywhere in Arm A, and it names no
power calculation.

### 4.3 Null used affirmatively as evidence of uniformity

This is the class our domain-homogeneity result belongs to, and it is thin everywhere.

> "In the Exposure phase, the mean originality was similar across conditions, as
> indicated by the Kruskal-Wallis H test ( H (2) = 3.78, p = 0.151)."
> — arXiv 2410.03703v2, Results

Statistically the closest published analogue to our chi-squared of 3.02 on 4 degrees of
freedom: a small omnibus statistic, a p-value in the same neighbourhood, and a sentence
that states uniformity as the finding rather than reporting a failure to reject.

> "In the Exposure rounds, the average median cosine distance between ideas was similar
> across all conditions ( p > 0.05), which is unexpected."
> — arXiv 2410.03703v2, Results

> "The proportion of participants reporting at least one adverse event was similar
> across groups: 56% in therapist-guided I-BA (41 participants), 55% in self-guided I-BA
> (40 participants) and 55% in TAU (40 participants)."
> — PMC13504836, Methods

> "All other outcomes showed similar baseline values across groups."
> — PMC13460065, Methods

> "Stimuli associated with inhibition did not have lower value, and both equivalence
> testing and Bayesian analyses showed evidence that stimuli associated with inhibition
> did not differ in their value from those not associated with inhibition."
> — PMC13043209, Discussion

> "The sensitivity analyses for the full sample provided no evidence that any of the
> three methodological variables had a credible effect on the magnitude of the estimated
> gender difference in WPD."
> — PMC11825285, Results

> "Thus, these null findings do not appear to result from a failure of the Why/How task
> to elicit mentalizing or mirror networks."
> — PMC10123837, Discussion

> "human performance conditioned on set size was comparable between the settings."
> — arXiv 2401.13744v3, Results

The contrasting move, a heterogeneity claim asserted positively, appears twice in Arm A:

> "This finding indicates that the multi-turn capabilities of models are not uniform
> across domains and validates the importance of benchmarking models across a wide
> variety of tasks to investigate model capabilities."
> — arXiv 2505.06120, Results

> "This discrepancy between InstructGPT and GPT3 suggests that the impact of LLMs on
> content homogenization is not uniform."
> — arXiv 2309.05196, Results

Neither reports a homogeneity test statistic. Uniformity claims in Arm A are made from
inspecting per-domain numbers, not from a test. A reported chi-squared with degrees of
freedom would be above the arm's current standard rather than a concession.

### 4.4 Buried

All from Arm A.

> "Any effect goes away when controlling for number of critiques found."
> — arXiv 2206.05802, Appendix E figure caption (verified 2026-09-06)

The whole reporting of a control that eliminates an effect, in a caption in Appendix E,
with no corresponding sentence in the paper's Results.

> "Figure 14 : Current LLM critics did not help significantly when applied to
> challenging competition code (a small effect is visible in the plot, but is not
> significant)."
> — arXiv 2407.00215, figure caption

> "An ablation experiment is conducted in Appendix D that implements several different
> prompts and we find prompt variations do not significantly affect DG-Diff ."
> — arXiv 2404.04298, Methods

> "According to the findings presented in Table 7 , alterations in prompt wording do not
> significantly affect performance."
> — arXiv 2404.04298, back matter

> "However, after only 4 trials, we terminated the baseline and Reflexion runs as the
> agent did not show improvement in accuracy (Fig. 6) and was not generating helpful,
> intuitive self-reflections."
> — arXiv 2303.11366 (Reflexion), Limitations

> "In addition, we include an inconclusive attempt to improve performance on the WebShop
> benchmark and provide a discussion that highlights a few limitations of this approach."
> — arXiv 2303.11366 (Reflexion), Conclusion

> "Comparing model scores, we find no significant difference in writing quality across
> the three models."
> — arXiv 2409.14509, Methods (verified 2026-09-06)

The same paper does bring that null forward, which is the exception in Arm A:

> "Surprisingly, there are no significant differences in perceived writing quality or
> types of edits needed across texts generated by different large language models
> (GPT-4, Claude 3.5, Llama 3.1)."
> — arXiv 2409.14509, Conclusion (verified 2026-09-06)

> "Across various LLMs and tasks, the performance gains from reflection are not
> significant, and occasionally detrimental. In cases of incorrect initial responses,
> only 15.1% of incorrect responses are corrected through reflection."
> — arXiv 2401.02009, Introduction (verified 2026-09-06)

> "As shown in Table 1 , we observe no significant accuracy changes before and after
> reflection." / "This explains why there is no discernible difference in performance
> pre- and post-reflection."
> — arXiv 2401.02009, Introduction (verified 2026-09-06)

None of the Arm A nulls above reports a test statistic, an interval, or a threshold. In
every case "significant" is doing informal work.

## 5. Verbatim catalogue: a pre-registered threshold that was not met

**This pattern is genuinely rare, and the count is the finding.** Search terms and
result, stated so the sweep can be repeated:

A sentence-level conjunction was required across all 75 full texts: one regular
expression matching `pre-?regist|pre-?specifi|prespecifi|a priori|predetermined|
pre-?defined|pre-?planned|primary (endpoint|outcome)|registered report`, and a second
matching `did not (meet|reach|exceed|cross|achieve|attain|clear|support|confirm)|
was not met|were not met|not achieved|fell (short|below)|failed to (meet|reach|exceed|
support)|below (the|our)|not supported|was not confirmed|no support for`.

**Result: 5 sentences, in 4 papers, all clinical trials. Zero in Arm A. Zero in Arm B.
Zero in Arm C.** A looser single-sided sweep on the not-met expression alone returned 30
sentences across 17 papers, of which 25 were false positives (statistical assumptions
not met, medians not reached, enrolment targets, model-fit thresholds, similarity
thresholds in a method).

### The five

> "Therefore, the primary endpoint for this study was not met. Subsequently reported p
> values are nominal."
> — PMC13442687, Results

The complete report, immediately after the estimate, its 95 percent interval and its
p-value. One sentence for the verdict, one sentence demoting everything downstream.
No hedge, no consolation, no reinterpretation of the endpoint.

> "Although the REACH study did not meet its primary endpoint, the study design and data
> from the study are presented here to report the findings since they are of great
> interest for the FSHD community and may be useful for future studies."
> — PMC13442687, Introduction

> "Although the REACH study did not meet its primary endpoint, study design and data
> from the study may inform future studies of FSHD therapies."
> — PMC13442687, Conclusion

The unmet endpoint is stated in the Introduction, the Results, and the Conclusion. It is
never softened and never withheld until late.

> "First, because the primary endpoint was not met, additional follow-up is required to
> determine whether immunotherapy confers long-term survival benefits."
> — PMC12079821, Discussion (limitations)

> "The primary endpoint, the difference in pCR rates between the two groups, was not
> statistically significant (15% vs. 13.3%, P = 0.832)."
> — PMC12079821, Discussion

### The closest analogue to our 65 percent bar

Not caught by the conjunction above because it says "did not reach" a "suggested
threshold" rather than a pre-registered one, but it is the single best model in the
corpus for a fixed bar that a real estimate fell under:

> "Although therapist-guided I-BA was associated with a statistically significant
> difference compared with TAU (estimated mean difference -4.68 points on CDRS-R), this
> did not reach the suggested threshold of six points for clinical meaningfulness. Thus,
> the clinical impact of I-BA was smaller than expected and should be interpreted with
> caution. However, it is worth noting that 4.68 points correspond to an effect size of
> approximately 0.50, which falls within the range typically reported in adolescent
> psychotherapy trials ( g =0.29-0.55 depending on comparator) and is smaller than
> effects observed in adult trials, particularly when usual care is the comparator."
> — PMC13504836, Discussion

The three-move structure is worth naming: state the estimate, state flatly that the bar
was not cleared, then place the estimate against an external reference distribution so
the reader can size it. The third move is not a defence of the result. It is the
information the reader needs to know what a 4.68 means, and it works because it cites a
range from outside the paper rather than arguing.

### Adjacent: a pre-registered criterion that returned "inconclusive" rather than "not met"

> "The results therefore provide ultimately--and unfortunately, despite the sample size
> of > 2,000 participants, more than five-fold the original sample size-- inconclusive
> evidence as there is neither sufficient statistical information to confidently conclude
> that women speak practically more WPD than men, nor that the two genders speak a
> practically equivalent number of WPD."
> — PMC11825285, Results

> "Regarding the magnitude, the Credible Interval shows that a gender difference as small
> as 316 WPD (clearly trivial) or as large as 1,824 WPD (potentially meaningful) is
> ultimately plausible given the data, thereby rendering the test of our pre-registered
> prediction inconclusive."
> — PMC11825285, Discussion

> "Unfortunately, though, despite the considerable sample size(s), all parameter
> estimates carried large statistical uncertainty and, except for the gender difference
> in early and middle adulthood, provide inconclusive evidence regarding whether (on the
> basis of the pre-registered ±1,000 WPD ROPE criterion) the two (binary) genders
> ultimately differ in a practically meaningful way in how many words they speak on a
> daily basis."
> — PMC11825285, Conclusion

> "Having to commit to (and justify) a definitive ROPE prior to the analyses is a key way
> in which the registered report format guards against confirmation bias through post-hoc
> (implicit) use of researchers' degrees of freedom."
> — PMC11825285, Methods

This is the structural match for our pairwise study. The interval spans values on both
sides of the criterion, so the paper reports the test as inconclusive at the realized
sample size and says which two conclusions the data fail to separate. It does not report
this as a negative result, and it does not report it as a failure.

## 6. "No difference" against "we could not detect a difference": exact phrasings

The distinction is made explicitly in Arm D, occasionally in Arm B, and essentially
never in Arm A.

**Phrasings that assert no difference.** Each is backed in its source by an equivalence
test, a Bayes factor, or a pre-registered interval; none stands on a non-significant
p-value alone.

> "both equivalence testing and Bayesian analyses showed evidence that stimuli
> associated with inhibition did not differ in their value from those not associated
> with inhibition" — PMC13043209
>
> "Bayes Factor results showed substantial evidence in favor of the null hypothesis (all
> BF 01 > 6.6)." — PMC13043209
>
> "equivalence tests run on the Stopping condition showed that the two Stopping groups
> were statistically equivalent (all p's < .001)." — PMC13043209
>
> "the Bayes factor indicated strong evidence in favour of the null hypothesis"
> — PMC8742248
>
> "we concluded this observed effect relating violent gaming to aggressive behaviour was
> both statistically and practically insignificant." — PMC6408382

**Phrasings that assert only a failure to detect.**

> "the analysis remains inconclusive regarding the predictive value of TMB"
> — PMC10598029
>
> "the trial was underpowered and all analyses were exploratory." — PMC10598029
>
> "this study was likely underpowered to detect modest between-group differences"
> — PMC13460065
>
> "the trial was not powered to detect between-group differences in secondary measures"
> — PMC13504836
>
> "our study cannot determine whether the models exhibit a self-enhancement bias."
> — arXiv 2306.05685
>
> "Thus, the data were inconclusive, and further research with increased statistical
> power is warranted." — PMC12618885, quoting its own recommended template
>
> "inconclusive results at this sample size would be an important message for the field."
> — PMC8742248

**The decision rule stated in advance.** Two papers write down, before analysis, which
of the two readings each possible outcome will get. This is the mechanism that makes the
distinction reportable rather than arguable.

> "If we obtained non-significant results from the frequentist approach, we used Bayes
> factors to help us interpret non-significant results and differentiate between
> insensitive results and those that reveal good enough evidence supporting the null
> hypothesis."
> — PMC8742248, Methods

> "Gender difference estimates for which the 95% High Density Interval (HDI) fell
> completely within a ± 1,000 words ROPE centered around a zero difference were
> interpreted as practically equivalent; those for which the 95% HDI fell completely
> outside of a ± 1,000 words ROPE were interpreted as support for the existence of a
> gender difference; and those for which the 95% HDI fell partially within and partially
> outside a ± 1,000 words ROPE were interpreted as providing inconclusive evidence."
> — PMC11825285, Methods

A three-way mapping from interval position to conclusion, fixed before the data. It
converts our second case from a judgment call into a lookup.

**The methodological statement of why the distinction matters**, from the corpus's own
methods paper:

> "Importantly, note that if we do find a significant difference, this does not imply
> that the experiment had high power."
> — arXiv 2010.06595 (With Little Power Comes Great Responsibility), Introduction

> "Underpowered experiments make it more difficult to discern the difference between
> statistical noise and meaningful model improvements, and increase the chances of
> exaggerated findings."
> — arXiv 2010.06595, Abstract

> "By meta-analyzing a set of existing NLP papers and datasets, we characterize typical
> power for a variety of settings and conclude that underpowered experiments are common
> in the NLP literature."
> — arXiv 2010.06595, Abstract

> "Similarly, based on reasonable assumptions, we find that the most typical experimental
> design for human rating studies will be underpowered to detect small model differences,
> of the sort that are frequently studied."
> — arXiv 2010.06595, Abstract

That last sentence is the citation for our second case: an NLP-venue paper establishing
that human rating studies of the size we ran are typically underpowered for effects of
the size we found.

## 7. Verbatim catalogue: an effect that vanishes once a control is added

This is the crux for our first result. Papers that report both estimates side by side
and name the control:

### The fullest model in the corpus

> "In the prespecified analysis, therapist-guided I-BA was significantly more efficacious
> than TAU in reducing clinician-rated depressive symptoms at the primary endpoint (~6
> months post randomisation). Self-guided I-BA showed a similar pattern but did not
> significantly outperform TAU. However, sensitivity analyses showed that statistical
> significance depended on model specification. A model allowing individual variability
> in change over time (random slopes) provided a better fit to the data. The between-group
> difference was no longer statistically significant, although effect estimates remained
> similar in magnitude and direction. In contrast, post hoc analyses adjusting for
> baseline depressive severity (without random slopes) yielded statistically significant
> effects for both I-BA groups compared with TAU. Together, these findings indicate that
> while the statistical significance of the results was sensitive to alternative analytic
> approaches, the magnitude and direction of the results remained constant."
> — PMC13504836, Discussion, opening of Principal findings

Every element our first result needs: the pre-specified estimate named as pre-specified;
the alternative specification named and justified on its own terms (better fit, not a
better answer); the significance change stated flatly; and the closing sentence
separating what moved (significance) from what did not (magnitude and direction). It
reads as a description of the estimate's behaviour, not as a retreat.

Two further sentences from the same paper, both stating the pattern compactly:

> "Although effect estimates remained similar in magnitude and direction, between-group
> effects were attenuated and no longer statistically significant at the primary
> endpoint."
> — PMC13504836, Results

> "Although the prespecified random-intercept model showed a statistically significant
> effect for therapist-guided I-BA compared with TAU, a random-slopes model, which
> provided better fit to the data, yielded non-significant results."
> — PMC13504836, Discussion

### The vanishing read as substantive, not as a robustness failure

> "After controlling for the gap, the direct effect of sycophancy on social satisfaction
> was no longer significant ( ), suggesting that what reduced satisfaction was not how
> the AI felt on its own, but how close it came to the humans in participants' lives."
> — arXiv 2605.07912v3, Results

The control is not a threat the effect survived or failed. Including it identifies which
of two mechanisms is operating, and the disappearance of the direct effect is the
evidence. The immediately preceding text names the mediation explicitly:

> "The shift in social satisfaction was mediated by this narrowing gap, not by feeling
> understood by AI on its own (indirect effect , 95% CI , 41% mediated)."
> — arXiv 2605.07912v3, Results

This is the closest published model for reporting our meta-commentary control as
informative rather than destructive, if the control is in fact absorbing a mechanism
rather than absorbing noise.

### The pre-registered correction that removes the result, stated flatly

> "However, none of these effects are significant after adjusting for multiple hypothesis
> testing as preregistered (Appendix S6 )."
> — arXiv 2411.14652v2, appendix

> "After adjusting the p-values for multiple hypothesis testing, none of the covariates
> reach statistical significance."
> — arXiv 2411.14652v2, appendix

Same paper, the opposite outcome reported in the same register:

> "The results, summarized in Table S32 , show that our core findings remain robust: the
> treatment variable remains statistically significant even after accounting for these
> events."
> — arXiv 2411.14652v2, appendix

### Both columns reported in one sentence

> "As in the model-free analysis, LLM access increased the volume of topics covered in
> the Learning Phase (column 3, ), but it did not affect understanding when we control
> for subjects' progress during the Learning Phase (column 2, = 0.359)."
> — arXiv 2409.09047v2, Results

The uncontrolled and controlled estimates are given as adjacent table columns and
narrated in one sentence, with the control named.

### Attenuation reported with both estimates

> "Upon adjusting for ECOG and metastasis burden score, the favorable effect of TMB on OS
> only slightly decreased (HR 0.45, 95% CI 0.11-1.79; p = 0.26), while the effect on PFS
> was attenuated again (HR 0.70, 95% CI 0.18-2.67; p = 0.60; Table )."
> — PMC10598029, Results

### The Arm A treatment of the same situation

> "Any effect goes away when controlling for number of critiques found."
> — arXiv 2206.05802, Appendix E figure caption (verified 2026-09-06)

Nine words, in an appendix caption, with no estimate on either side of the control and
no mention in the Results. This is the only instance in 47 self-correction papers of an
effect reported as eliminated by a control, and it shows what the arm's current practice
looks like.

## 8. Equivalence tests, Bayes factors and power analyses supporting a null

**Frequency: equivalence tests in 7 of 75 papers, Bayes factors in 5 of 75, power or
minimum-detectable-effect analyses in 17 of 75. All 7 equivalence tests and all 5 Bayes
factors are in Arm D. Arms A and C contain none of either.**

### Equivalence testing against an external benchmark

> "In order to know if the effect observed was practically significant, we directly
> compared the standardized semi-partial correlation coefficients to the best existing
> meta-analytic effect size estimate identified by Hilgard et al . [ ], using the two one-
> sided tests procedure [ ]. In this test, we contextualized the observed effect size
> estimate in terms of whether it is inferior (i.e. smaller), equivalent (i.e. falls
> within the same range as) or is superior (i.e. larger) to findings present in the
> existing literature [ ], and in line with proposed minimum practical media effect sizes
> [ - ]. The semi-partial effect relating violent gaming to aggressive behaviour was r =
> 0.01. Further, we derived a 95% coincidence interval around this point estimate that
> ranged from -0.08 to 0.10 using a bootstrapping approach with 10 000 iterations. Given
> this effect, r = 0.01 (95% CI = -0.08 to 0.10), did not overlap with, and was clearly
> inferior to, r = 0.21 (95% CI = 0.20-0.22), we concluded this observed effect relating
> violent gaming to aggressive behaviour was both statistically and practically
> insignificant."
> — PMC6408382, Results, section headed "Equivalence testing"

The benchmark is the published meta-analytic estimate, not zero. The comparison is
between two intervals, and the conclusion is a positive statement about where the
estimate sits relative to the literature.

### Setting the equivalence bound before the data, and justifying it

> "Considering different scenarios, we settled on a ± 1,000 words ROPE because (a) it
> aligns well with the original effect size estimate from report (women spoke about 546
> words per day more than men) (b) it aligns well with an effect-size based approach to
> determining the ROPE (extrapolating from the original study data, a δ = ± .10
> difference should translate to roughly ± 800 words), and (c) the general public tends to
> construe the magnitude of the gender difference in daily word use in multiples of one
> thousand words (e.g., 20,000 vs. 7,000 words), suggesting that anything less than 1,000
> words would likely be considered trivial (e.g., 15,900 vs. 15,100 words)."
> — PMC11825285, Methods

Three independent justifications for one number: the prior literature, an effect-size
convention, and what a lay reader would call trivial. A model for defending our 65
percent, which currently has no stated derivation.

> "Yet, broadening the ROPE for determining practical equivalence biases towards
> successful replication."
> — PMC11825285, Methods

### Bayes factors used to separate insensitivity from evidence

> "Although we used the frequentist approach for confirmatory analyses, we also reported
> Bayes factors for every result to gain information about the strength of evidence
> provided by the data comparing the null and alternative hypotheses ."
> — PMC8742248, Methods

> "Another outcome (negative state emotions; , row 9) revealed no significant difference
> between types of reappraisal, and the Bayes factor indicated strong evidence in favour
> of the null hypothesis."
> — PMC8742248, Results

> "The Bayes factors indicated strong evidence in favour of the null hypothesis for one
> outcome (positive state emotions; , row 12) and inconclusive evidence for another
> outcome (positive emotions about the COVID-19 situation; , row 13)."
> — PMC8742248, Results

Two non-significant outcomes, two different conclusions, separated by the Bayes factor.

> "Equivalence tests were computed using the two one-sided t-test (TOST) procedure ( ) in
> Python." / "The statistical software JASP ( ) was used to compute Bayes Factors."
> — PMC13043209, Methods

> "All statistical tests were performed in MATLAB (MathWorks, Natick, MA, USA) and report
> p values, CIs, effect size, Bayes factors (BF), and equivalence tests."
> — PMC10123837, Methods

A paper whose title begins "Null results of..." reports all five quantities for every
test as a matter of routine.

### Minimum detectable effect, reported post hoc alongside the observed effect

> "To contextualize the results, Table S18 reports the observed and post-hoc Minimum
> Detectable Effects (MDE) for each of the engagement metrics discussed above."
> — arXiv 2411.14652v2, Methods

> "Reduced Exposure Increased Exposure Metric Observed Effect MDE Observed Effect MDE
> Number of Sessions (Daily) -0.06 0.14 -0.04 0.17 Time spent (Daily in Minutes) -4.71
> 5.02 -1.76 6.31 Number of Views (Total) -170.00 249.41 -132.00 254.99 [...] Table S18 :
> Engagement: Observed and post-hoc Minimum Detectable Effects (MDE) in the two
> experiments (power = 0.8, )."
> — arXiv 2411.14652v2, Methods (`[...]` marks four further table rows omitted here)

The only instance in the arXiv arms of a null being paired with what the design could
have detected, and it is a table of two columns: observed effect next to MDE, one row
per outcome. Directly transferable to our pairwise study.

### The recommended template, from a methods paper

> "Rather than estimating the required sample size, sensitivity analysis identifies the
> smallest effect size that the study is capable of reliably detecting given the available
> sample, chosen alpha level, and desired power ."
> — PMC12618885, Methods

> "Thus, the data were inconclusive, and further research with increased statistical power
> is warranted ." Equivalence testing can complement classical hypothesis testing by
> allowing researchers to assess whether an observed effect is too small to be considered
> practically worthwhile or important ."
> — PMC12618885, Methods

> "Instead, one can write that a p -value was on the threshold of statistical
> significance."
> — PMC12618885

## 9. Two phrasings observed in the corpus that are best not copied

Both appear in fetched papers, so they are real practice, and both invite the reading we
are trying to avoid.

> "In the second prespecified endpoint analysis, treatment failure was defined as needed
> for rescue therapy (other IET or surgery) as determined by the treating physician at 7
> days, the 400,000 U and 800,000 U LTI-01 dose groups showed nonsignificant trends
> towards improved outcomes."
> — PMC13520383, Results

> "However, although these differences were not statistically significant, the direction
> of the results suggests that the accuracy nudge may have slightly increased
> participants' intentions to share both true and false videos."
> — arXiv 2411.02405v1, Results

"Nonsignificant trends towards" and "although not significant, the direction suggests"
read as an author arguing with the result. Where the direction genuinely matters, the
corpus's better instrument is the interval and the minimum detectable effect, which state
the same information without asking the reader for credit.

## 10. Wording the two results in this paper

Both of our cases have a published structural match in this corpus. Neither needs to be
written apologetically, and in both the convention that makes them read as findings is
the same: name the criterion before the number, give the interval, and say what the
interval does and does not exclude.

### 10.1 Domain homogeneity, and the contrast that moves under the control

Two claims are entangled here and should be separated in the prose, because they are
answers to different questions and one of them is clean.

**The homogeneity result is a clean finding and should be stated as one.** A chi-squared
of 3.02 on 4 degrees of freedom is small relative to its degrees of freedom; the five
domains give no indication of differing. Written the way `2410.03703` writes its
Kruskal-Wallis, that is one sentence in Results with its statistic, followed by the
decision it licenses:

> **[Proposed wording, not a quotation.]** The effect does not differ detectably across
> the five task domains (χ² = 3.02, df = 4, p = 0.555), and results are therefore
> reported pooled across domains.

The second clause is what turns the null into a finding: the homogeneity test is being
used for the thing homogeneity tests are for, which is to license pooling. State the
decision and the null has done work. Note that no Arm A paper making a uniformity or
heterogeneity claim reports any test at all (section 4.3), so a reported statistic with
degrees of freedom is above the arm's standard.

If a stronger claim than "no detectable difference" is wanted, it needs an equivalence
bound fixed in advance, on the pattern of PMC11825285: the largest cross-domain
difference that would still count as the same effect. Without such a bound the honest
statement is the one above, and it is enough for the pooling decision.

**The contrast that moves from p = 0.019 to p = 0.151 should be reported as one estimate
under two specifications, with the control named, following PMC13504836.** The elements,
in order:

1. Name which specification is the registered primary. Everything else is secondary and
   should be labelled so. PMC13442687's device is the model: after the primary verdict,
   "Subsequently reported p values are nominal."
2. Give both estimates side by side, with intervals, in adjacent table columns, and
   narrate them in one sentence naming the control. `2409.09047` does this in a single
   sentence referring to two columns.
3. State what changed and what did not, in that order, in the paper's own words. The
   PMC13504836 formulation is "the statistical significance of the results was sensitive
   to alternative analytic approaches, the magnitude and direction of the results
   remained constant." Whether that is true of our estimates is a matter for the numbers;
   if the point estimate is materially unchanged and only the interval widens, saying so
   is both accurate and the strongest available framing.
4. Say what the meta-commentary control absorbs. This is the decision that determines how
   the pair should read, and it is not a writing decision. If the control removes a
   mechanism that is part of the effect, the uncontrolled estimate is the total effect
   and the controlled estimate is the direct effect, and the pair is a mediation result
   in the shape of `2605.07912`: the disappearance identifies the channel and is
   reportable as such. If the control removes a confound, the controlled estimate is the
   estimate and the uncontrolled one is an upper bound. The two readings license
   different sentences and the paper should commit to one on substantive grounds, stated
   plainly, rather than presenting both estimates without saying which is the estimate.

What to avoid: describing the controlled result as "no longer significant" without the
accompanying magnitude statement, which reads as a robustness failure; and reporting only
whichever of the two is preferred, which is the concealment the corpus's methods papers
are written against.

### 10.2 The 65 percent bar and the 56.2 percent result

The structural match is PMC11825285, not PMC13442687, and the difference matters.
PMC13442687's endpoint was missed with an interval that excluded any meaningful effect.
Ours is missed with an interval, 45.2 to 67.1, that contains both 50 percent and the 65
percent criterion. The result is therefore inconclusive with respect to the
pre-registered test, not negative, and those are different claims. Saying so is the
accurate reading and also the stronger one.

Suggested shape, drawing the verdict sentence from PMC13442687 and the interval reading
from PMC11825285:

> **[Proposed wording, not a quotation.]** The pre-registered success criterion was 65
> percent preference for the revised output
> in blind pairwise comparison. Observed preference was 56.2 percent (95% CI 45.2 to
> 67.1). The criterion was not met. The interval contains both 50 percent and the 65
> percent criterion, so at this sample size the study does not separate no preference
> from the pre-registered target; the test is inconclusive rather than negative. [Report
> the minimum detectable effect at the realized n, and the n required to separate the two
> hypotheses.]

The elements that do the work:

1. **The criterion is stated before the number.** This is what distinguishes a
   pre-registered report from a post-hoc one, and reading order is how a referee sees it.
2. **The verdict is one flat sentence.** "The criterion was not met." No hedge, no
   softening adverb, no "only". PMC13442687 states its unmet endpoint three times, in the
   Introduction, the Results and the Conclusion, and never softens it once.
3. **The interval is read explicitly against both hypotheses it fails to separate.** This
   is the move that converts a miss into an informative result, and it is exactly what
   PMC11825285 does when it writes that both a trivial and a meaningful value "is
   ultimately plausible given the data, thereby rendering the test of our pre-registered
   prediction inconclusive."
4. **The minimum detectable effect is reported.** `2411.14652`'s Table S18 is the format:
   observed effect and MDE as adjacent columns. This is the quantity that tells the
   reader whether the study was capable of clearing the bar it set, and its absence is
   what makes an unmet threshold read as a failure rather than a bound.
5. **Everything downstream is marked nominal or exploratory.** PMC13442687: "Subsequently
   reported p values are nominal." PMC10598029: "the trial was underpowered and all
   analyses were exploratory."
6. **The criterion is not redefined after the fact.** PMC11825285 notes in its Methods
   that loosening the bound "biases towards successful replication," which is the reason
   not to.

Two further points worth considering for placement. Every Arm C and Arm D paper in this
corpus reports its nulls in Results and carries them into the Discussion, and three Arm C
papers put a null in the abstract, including one whose title is its null result
(`2411.02405`, "Accuracy nudges are not effective against non-harmful deepfakes"). None
puts a primary null in Limitations. Three Arm A papers do, and that placement is the one
that reads as an apology.

And on how the pre-registration itself should be framed: given that 0 of 47
self-correction papers in this corpus name a pre-registration, an equivalence test, a
Bayes factor, or a power analysis, a fixed criterion that the paper reports against and
does not clear is a stronger methodological position than an unregistered study reporting
56.2 percent as a success would have been. That is a fact about the corpus and belongs
wherever the paper describes its design. It should be stated once, as a design
description, and not argued.

## 11. Files behind this document

All working files are in the session scratchpad, outside the project tree, and are not
part of the repository:
`/private/tmp/claude-501/-Users-liamneild-Desktop-School-llm-overcorrection-under-thresholds/00744317-e5e0-44e6-9b65-e83966797521/scratchpad/lit/`

They comprise the fetched HTML and JATS XML (`full/`, `raw/`, `verify/`), the
tag-stripped text with section markers (`txt2/`), the extraction and counting scripts
(`strip2.py`, `scan2.py`, `pmcfetch.py`, `pmcsearch.py`, `axsearch.py`, `ctx2.py`), and
the machine-produced hit and manifest files (`hits2.json`, `manifest.json`,
`audit.json`, `meta.json`). Re-running `strip2.py` then `scan2.py` reproduces every count
in section 3 from the fetched sources.
