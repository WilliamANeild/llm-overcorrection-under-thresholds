# Effect-size and interval reporting in NLP and human-AI interaction

Retrieval date for every item below: **2026-09-06**. Source: arXiv HTML full text
(`https://arxiv.org/html/<id>`). Nothing here is cited from an abstract, a title, or
memory. Every quoted sentence was taken from the fetched HTML of the version named.

## 1. How the sample was drawn

The earlier survey in this project used a hand-picked set of 19 results sections. This
sweep uses a mechanical frame instead, so the two samples are selected on different
criteria and the earlier count can be tested rather than restated.

Frame, in order of application:

1. arXiv API queries, submitted-date descending, 60 results each, run 2026-09-06:
   - `cat:cs.CL AND abs:"user study"`
   - `cat:cs.CL AND abs:"human evaluation"`
   - `cat:cs.CL AND abs:"participants"`
   - `cat:cs.HC AND abs:"user study" AND abs:"large language model"`
   - `cat:cs.HC AND abs:"participants" AND abs:"LLM"`
2. Deduplicate, restrict to submissions dated 2024-01-01 or later. Result: **273 papers**.
3. Fetch arXiv HTML for all 273.
4. Strip tags, and strip MathML `<annotation>` elements first so LaTeX source is not
   duplicated into the text. Result: **270 usable text extractions** (the screening pool).
5. Screen for at least one inferential-test keyword anywhere in the full text
   (Wilcoxon, Mann-Whitney, Kruskal, Friedman, t-test, ANOVA, chi-square, sign test,
   McNemar, binomial test, mixed-effects, bootstrap, permutation test).
6. Order the survivors by submission date and take the 12 most recent with primary
   category `cs.CL` and the 12 most recent with primary category `cs.HC`, skipping any
   paper whose keyword hits turned out to be bibliography artifacts rather than tests
   the paper ran.

Note on step 5: the screen conditions on running a test, not on reporting an effect
size. That is the denominator that makes the question answerable. A paper that never
tests anything cannot fail to report an effect size alongside a test.

**Papers skipped at step 6, with reasons.** `2609.00832v1` (TWIX): the only ANOVA and
mixed-effects strings are in the reference list; the paper runs no inferential test.
`2608.30866v1`: the "Friedman" hit is the surname in "Bender and Friedman (2018)". Both
were replaced by the next paper down the date-ordered list.

**Access failures.** Three of 273 downloads returned zero bytes (`2608.04910v1`,
`2608.00839v1`, `2604.05226v1`). Twenty-three returned an arXiv "no HTML available"
page rather than a rendered paper; these are pre-2024 LaTeX submissions or PDF-only
deposits. Neither group is in any count below. No paper in the final 24 failed to
retrieve.

**One exclusion for provenance.** The working directory already held 27 text files with
names such as `karpinska2021.txt` and `alpacaeval_lc.txt` from earlier work. They are
not from this fetch and are excluded from every count. Only files whose basename is an
arXiv identifier from this session's download list are counted.

**Normalization disclosed.** arXiv HTML renders inline math as MathML with per-character
spans. Stripping tags therefore inserts spaces inside symbols, so `SD` reads as `S D`
and `\eta_p^2` reads as `η p 2`. Quotations below preserve the extracted text as-is,
spacing included. No word was changed, added, or removed inside any quotation.

## 2. Corpus table

Community is the arXiv primary category. "Result type" codes whether the paper's main
claim is that a proposed method or system works (W) or is a null, a limitation, or a
descriptive characterization (N). "ES" is the strict code: a named standardized or
scale-free effect-size statistic reported alongside a hypothesis test. "CI prose" means
a numeric interval attached to an estimate in running body text, not only in a figure
caption, an axis, or a table cell.

| # | arXiv id | Community | Submitted | Result type | Tests run | ES | ES measure | CI prose |
|---|---|---|---|---|---|---|---|---|
| 1 | 2609.02651v1 | cs.CL | 2026-09-02 | N | Pearson correlation | no | (r is the estimand) | no |
| 2 | 2609.02480v1 | cs.CL | 2026-09-02 | W | Wilcoxon signed-rank, exact McNemar, bootstrap | yes | Cohen's d_z | yes |
| 3 | 2609.02122v1 | cs.CL | 2026-09-02 | N | Mann-Whitney U, z-tests, OLS | no | none | yes |
| 4 | 2609.01202v1 | cs.CL | 2026-09-01 | W | Wilcoxon signed-rank, Mann-Whitney U, percentile bootstrap | no | none | no |
| 5 | 2609.00685v1 | cs.CL | 2026-09-01 | W | Mann-Whitney U, mixed-effects logistic | yes | odds ratio | no |
| 6 | 2609.00491v1 | cs.CL | 2026-08-31 | N | unnamed significance tests | no | none | no |
| 7 | 2608.30719v1 | cs.CL | 2026-08-31 | W | exact McNemar, bootstrap | no | none | no (table only) |
| 8 | 2608.29995v1 | cs.CL | 2026-08-30 | W | RM-ANOVA, Cochran's Q, paired t, chi-square, GEE | yes | Cohen's d_z, odds ratio | no (caption only) |
| 9 | 2608.29446v1 | cs.CL | 2026-08-29 | N | mixed-effects logistic, chi-square, Holm, bootstrap | yes | odds ratio | yes |
| 10 | 2608.28467v1 | cs.CL | 2026-08-28 | N | exact McNemar, bootstrap | no | none | no (table only) |
| 11 | 2608.26638v2 | cs.CL | 2026-08-27 | W | paired permutation, Z-test, bootstrap | no | raw mean difference | yes |
| 12 | 2608.23705v2 | cs.CL | 2026-08-24 | N | Mann-Whitney U, Kendall tau-b | no | (tau-b is the estimand) | no |
| 13 | 2609.01588v1 | cs.HC | 2026-09-01 | N | linear mixed-effects | no | none | no |
| 14 | 2608.27932v1 | cs.HC | 2026-08-28 | N | 2x2 ANOVA, Welch t, mixed-effects | no | none | no (figure only) |
| 15 | 2608.24224v1 | cs.HC | 2026-08-25 | W | Friedman, Wilcoxon signed-rank | yes | Kendall's W | no |
| 16 | 2608.21177v1 | cs.HC | 2026-08-21 | N | RM-ANOVA, paired t, Pearson, MixedLM | yes | eta-squared, Cohen's d | no |
| 17 | 2608.19551v2 | cs.HC | 2026-08-20 | N | linear mixed model, NB-GLM, chi-square | no | none | no |
| 18 | 2608.19083v1 | cs.HC | 2026-08-19 | N | 2x2 ANOVA, Mann-Whitney U, SEM, bootstrap | yes | partial eta-squared, Hedges' g | yes |
| 19 | 2608.14113v1 | cs.HC | 2026-08-14 | N | between-subjects ANOVA | yes | Cohen's f | no |
| 20 | 2608.10337v1 | cs.HC | 2026-08-11 | W | Wilcoxon signed-rank, paired t | no | none | no |
| 21 | 2608.09698v1 | cs.HC | 2026-08-10 | W | Wilcoxon signed-rank, FDR | yes | r = abs(Z)/sqrt(N) | no |
| 22 | 2608.06151v1 | cs.HC | 2026-08-06 | W | OLS with robust SE, chi-square, logistic | yes | Cohen's d, odds ratio | yes |
| 23 | 2607.27938v1 | cs.HC | 2026-07-30 | W | Wilcoxon signed-rank | no | none | no |
| 24 | 2607.27697v1 | cs.HC | 2026-07-30 | W | RM-ANOVA, Friedman, Wilcoxon, paired t, chi-square | no | none | no |

## 3. Verbatim catalogue

Every sentence in this section is quoted exactly as extracted from the fetched HTML.
Spacing inside math expressions is an artifact of MathML rendering and is left
untouched. Papers reporting no effect size are listed in section 3.3 with the
significance-only sentence that stands in its place, since the absence is the finding.

### 3.1 cs.CL papers that report an effect size

**2609.02480v1, PragAlign (retrieved 2026-09-06).** Wilcoxon signed-rank with paired
Cohen's d_z and bootstrap intervals on the raw difference.

> "Compared with one-shot generation, full PragAlign produced a mean paired quality improvement of 0.0177, with a bootstrap 95% confidence interval of [0.0145, 0.0209]."

> "The difference was significant under a Wilcoxon signed-rank test ( p < .001 ), with a paired standardized effect size of d z = 0.38 ."

> "The paired initial-to-final quality improvement had a large within-dialogue effect size ( d z = 1.54 )."

> "Compared with the no-emotion condition, full PragAlign improved aggregate quality by 0.0113 on average, with a bootstrap 95% confidence interval of [0.0081, 0.0145]."

> "The Wilcoxon signed-rank test was significant ( p < .001 ), and the paired acceptance difference was also significant under McNemar’s test ( p < .001 )."

> "Compared with the no-feedback baseline, the mean aggregate-quality difference was small: 0.0024, with a bootstrap 95% confidence interval of [-0.0002, 0.0051]."

> "The Wilcoxon signed-rank test was not significant ( p = .103 ), indicating no reliable difference in continuous aggregate quality."

> "The mean aggregate-quality difference was -0.0003, with a bootstrap 95% confidence interval of [-0.0028, 0.0023]."

> "The Wilcoxon signed-rank test was not significant ( p = .992 ), and the paired acceptance difference was also not significant ( p = .688 )."

Table 5 header, verbatim: "Comparison Mean Diff. 95% CI Wilcoxon p d z Full Acc." with
rows carrying d_z values of 0.24, 0.06 and -0.01 for the three ablations.

**2609.00685v1, Visual Framing for News Stance Detection (retrieved 2026-09-06).** Odds
ratios from a mixed-effects logistic model, no intervals.

> "A mixed-effects logistic regression, with presentation condition as a fixed effect and random intercepts for participants and articles, further showed that all three comparison conditions had significantly lower odds of correct stance identification than VFStance : text-only ( OR = 0.708 , p = 0.001 ), original ( OR = 0.620 , p < 0.0001 ), and naïve ( OR = 0.697 , p = 0.0006 )."

**2608.29995v1, Generating Clinical Vignettes (retrieved 2026-09-06).** Paired Cohen's
d_z throughout, with an explicit appeal to the conventional 0.8 threshold.

> "Condition contrasts use omnibus RM-ANOVA (ordinal, d f = ( 2,218 ) ) or Cochran’s Q ( Cochran, 1950 ) (binary), then Bonferroni-corrected paired t -tests / proportion contrasts with paired Cohen’s d z ."

> "The within-persona cross-model cosine similarity (MPNet) is highest in full ( μ = 0.792 ), intermediate in no-formulation ( 0.767 ), lowest in zero-shot ( 0.737 ); all three pairwise differences are significant (paired t , n = 500 , p < 10 − 48 ), full-vs-zero-shot is the largest contrast ( d z = 1.52 )."

> "All six bars are above the conventional “large effect” threshold of 0.8 ; the full-vs-zero-shot contrast is larger under BGE ( + 1.61 ) than under MPNet ( + 1.52 )."

> "First, we report Cohen’s d z rather than between-subject d because the design is within-persona; the unstandardised mean differences are small (under 0.05 on a [ − 1 , 1 ] similarity scale) but the within-persona variance of the contrast is even smaller, which is what drives the large effect sizes."

> "Of the items tested, only Sense of current Threat goes from sizable to negligible at matched length ( d z falls from + 0.27 to + 0.03 )."

> "GEE confirms all contrasts (full-vs-zero-shot OR = 0.05 , z = − 18.5 ; full-vs-no-formulation OR = 0.17 ; no-form-vs-zero-shot OR = 0.30 ; all p < 10 − 15 ; Appendix V )."

**2608.29446v1, Whose Assessment of Distress (retrieved 2026-09-06).** The one paper in
the 24 that consistently pairs its effect size with an interval, because the effect size
is an odds ratio from a fitted model.

> "For distress, raters in the contextualized IG condition showed significantly higher agreement with the aggregate than raters in the uncontextualized OG condition ( β = 0.17 , 95% CI [ 0.01 , 0.33 ] , p = .035 )."

> "This corresponds to OR = 1.18 (95% CI [ 1.01 , 1.39 ] ), where IG raters have about 18% higher odds of matching the aggregate and a modest difference in raw agreement (IG: 82.3%; OG: 80.5%)."

> "For support-seeking, there was no evidence of an IG advantage ( β = 0.003 , 95% CI [ − 0.17 , 0.18 ] , p = .977 ; IG: 77.5%; OG: 77.1%)."

> "As shown in Figure 2 , the effect is concentrated in the parenting communities: r/Mommit ( OR = 1.61 , 95% CI [ 1.11 , 2.34 ] , p = .013 , p holm = .078 ) and r/daddit ( OR = 1.57 , 95% CI [ 1.08 , 2.27 ] , p = .018 , p holm = .088 ), with IG raters in these communities having roughly 1.6 × the odds of matching the aggregate."

> "The contrast is weaker in r/NonBinary ( OR = 1.40 , p = .095 ) and negligible elsewhere, including r/Veterans ( OR = 0.91 , p = .615 )."

> "For distress, the effect is driven by r/daddit, the only RQ1a contrast that survives Holm correction ( OR = 7.34 , 95% CI [ 2.43 , 22.23 ] , p = .0004 , p holm = .003 )."

> "For support-seeking, the largest contrast is in r/Veterans and runs in the opposite direction ( OR = 0.06 , 95% CI [ 0.006 , 0.49 ] , p = .009 , p holm = .055 ), which we discuss below."

> "At natural base rates, where subtler expressions of distress predominate, community-specific divergence is substantial: both omnibus interactions become significant, and the largest effect sizes increase several-fold (for distress in r/daddit, from OR = 2.62 to OR = 7.34 )."

### 3.2 cs.HC papers that report an effect size

**2608.09698v1, VeriForge (retrieved 2026-09-06).** This is the closest published match
to the design in the manuscript: paired Wilcoxon, effect size defined as abs(Z) over the
square root of N, FDR-adjusted q values alongside raw p, and a verbal magnitude label
with no convention cited.

> "Statistical Analysis We used two-sided paired Wilcoxon signed-rank tests."

> "We report effect sizes as r = | Z | / N eff ."

> "M = 69.31 ; W = 3.0 , p = .005 , q = .017 , r = .804 ) and lower overall cognitive workload (NASA-TLX Weighted Total: M = 48.58 vs."

> "M = 57.72 ; W = 12.0 , p = .034 , q = .060 , r = .611 ), both with large effect sizes ( fig. 5 )."

> "M = 3.00 ; W = 0.0 , p = .001 , q = .016 , r = .885 ), with 11 of 12 scoring VeriForge higher."

> "P06 described the experience as “essentially frictionless, no window-switching, no context breaks.” P07 noted that manual research would “break my writing flow,” whereas the inline mechanism “genuinely preserves my writing continuity.” The confusion reduction item showed the largest absolute shift of any metric in the study ( Δ = + 35.08 ; p = .002 , q = .016 , r = .886 )."

> "M = 5.75 ; p = .008 , r = .891 )."

> "M = 3.58 ; W = 2.5 , p = .005 , q = .015 , r = .818 )."

> "M = 4.25 ; p = .045 , q = .065 , r = .617 ), as did specificity ( M = 4.17 vs."

> "M = 3.54 ; p = .065 , q = .065 , r = .536 )."

Note: the source renders the square root as a radical glyph that does not survive tag
stripping, so `r = | Z | / N eff` in the extraction is `r = |Z| / sqrt(N_eff)` in the
rendered paper. The sentence is otherwise verbatim.

**2608.19083v1, When Readability and Source Retention Diverge (retrieved 2026-09-06).**
The most complete reporting in the 24: partial eta-squared on every omnibus, Hedges' g
on every planned contrast, and a 95% interval on every mean difference.

> "Hedges’ g was used as the standardized effect size for these simple contrasts."

> "Partial η p 2 is the standardized omnibus effect size."

> "Planned simple rendering contrasts and their standardized effect sizes (Hedges’ g ) are reported in the text."

> "Assuming a medium effect size (Cohen’s ( f = .25 )), ( α = .05 ) , and 95% statistical power, the analysis indicated a minimum required sample size of 210 participants."

> "Perceived Quality (RQ1a and RQ1b) The rendering contrast depended on source-text condition, F ( 1,302 ) = 4.51 , p = .034 , η p 2 = .015 (RQ1b)."

> "For the simple sources, the fidelity-oriented condition received higher quality ratings than the readability-oriented condition, Δ M = .584 , 95% CI [ .248 , .921 ] , p < .001 , Hedges’ g = .567 (RQ1a)."

> "For the complex sources, the two rendering conditions did not differ, Δ M = .018 , 95% CI [ − .376 , .413 ] , p = .927 , g = .014 ."

> "The interactions were significant for perceived intelligence, F ( 1,302 ) = 5.66 , p = .018 , η p 2 = .018 , FDR-adjusted q = .027 ; anthropomorphism, F ( 1,302 ) = 11.56 , p < .001 , η p 2 = .037 , q = .002 ; and trust, F ( 1,302 ) = 4.20 , p = .041 , η p 2 = .014 , q = .041 ."

> "The trust interaction was small and close to the conventional significance threshold and should therefore be interpreted cautiously."

> "For the simple sources, the fidelity-oriented condition received higher ratings of perceived intelligence, Δ M = .404 , 95% CI [ .146 , .662 ] , p = .002 , g = .489 ; anthropomorphism, Δ M = 1.051 , 95% CI [ .401 , 1.701 ] , p = .002 , g = .521 ; and trust, Δ M = .730 , 95% CI [ .132 , 1.329 ] , p = .017 , g = .396 ."

> "The point estimate for anthropomorphism was negative in this condition ( Δ M = − .497 , 95% CI [ − 1.124 , .129 ] , p = .119 , Hedges’ g = − .253 ), but the confidence interval included zero."

> "Averaged across rendering conditions, perceived intelligence was lower in the complex-source condition than in the simple-source condition, F ( 1,302 ) = 15.98 , p < .001 , η p 2 = .050 ."

> "A Mann–Whitney U test showed a significant difference between the two conditions, U = 607.50 , Z = − 18.20 , p < .001 , supporting the intended contrast in perceived source-text complexity."

The Mann-Whitney sentence is worth noting on its own: this paper computes Hedges' g for
every parametric contrast and reports the Mann-Whitney with U, Z and p and no effect
size, even though it has the Z in hand.

**2608.06151v1, Reducing belief in conspiracy theories (retrieved 2026-09-06).** Cohen's
d on every treatment effect, standardized by the pooled pre-treatment SD, with intervals
on the unstandardized coefficient rather than on d.

> "Results Main effects To test the effect of the LLM dialogue intervention on conspiratorial thinking about the Trump and Kirk assassination attempts, we follow Costello et al. 2 and conducted OLS regression with robust standard errors predicting the post-treatment rating using condition while controlling for pre-treatment rating for each of the four measures (note that this is mathematically identical to predicting pre-to-post change using condition while controlling for pre-treatment rating); we also report Cohen’s d standardizing effects by pooled pre-treatment standard deviation."

> "In both experiments, the LLM Debunking Dialogue reliably reduced participants’ belief in the conspiracy theory they had personally articulated via open-ended questions (0–100 scale), both relative to the Irrelevant Dialogue control (Trump: b = − 6.95 , p < .001 , d = .38 ; Kirk: b = − 7.56 , p < .001 , d = .38 ), and the static Information List (Trump: b = − 5.60 , 95% CI [ − 9.72 , − 1.48 ] , p = .004 , d = .32 ; Kirk: b = − 6.56 , 95% CI [ − 9.62 , − 3.49 ] , p < .001 , d = .35 ; Figure 1 )."

> "The Debunking Dialogue did increase trust in the official explanation for the Kirk assassination relative to the irrelevant dialogue ( b = 5.19 , 95% CI [ 2.34 , 8.04 ] , p < .001 , d = .19 ; although the difference with the Informational List condition was not significant: b = 2.27 , 95% CI [ − 0.62 , 5.15 ] , p = .16 , d = .08 )."

> "Perhaps as a result of thus having less baseline conspiratorial signal, our first pre-registered analysis finds no significant effect of receiving the Kirk debunking treatment when predicting LDS conspiracy belief, b = − .115 , 95% CI [ − 2.73 , 2.50 ] , p = .93 , d = − .005 ; Figure 3 C."

> "Both predicting belief using Kirk treatment assignment controlling for initial Kirk conspiratorial belief ( b = − 2.96 , 95% CI [ − 5.92 , .003 ] , p = .05 , d = − 0.12 ; Figure 3 D) and the Lin et al."

> "Participants who were in the Debunking Dialogue condition in the first experiment were significantly less likely to believe that only a select few will ever know the truth about the second assassination attempt (OR = .52 , 95% CI [ .31 , .84 ] , p = .009 ; Figure 3 A—including the selection of “another group not listed here” as conspiracy belief yields OR = .44 , 95% CI [ .23 , .80 ] , p = .008 ); and that the truth of the matter will be hidden from most people (OR = .48 , 95% CI [ .29 , .78 ] , p = .004 ; Figure 3 B)."

**2608.21177v1, From Search Agents to Dissemination Interfaces (retrieved 2026-09-06).**
Eta-squared on every ANOVA line including the nulls, Cohen's d on the paired t.

> "As illustrated in Fig 3 , the analysis revealed a significant main effect of the search agent on trust in health-related information, F ( 1 , 20 ) = 6.73 , p = .017 , and η 2 = .057 ."

> "Trust levels did not show significant changes across different types of search tasks, F ( 2 , 40 ) = 0.63 , p = .480 , with η 2 = .006 ."

> "The interaction between search agents and task types was not significant, F ( 2 , 40 ) = 0.20 , p = .777 , and η 2 = .002 ."

> "The trust scores in Google and ChatGPT as search agents are statistically significant with the difference in means as 0.27, t (21)=-2.53, p =.02, Cohen’s d =0.55 (see in Fig 3 )."

> "Participants A power analysis using G*Power ( Faul et al., 2007 ) indicated that a minimum of 20 participants were needed to detect a medium effect size of 0.25 with an alpha level of .05 and 80% power."

**2608.14113v1, Search or Chat (retrieved 2026-09-06).** A pure null paper that reports
Cohen's f on both null tests, which is the practice this manuscript should follow.

> "Description of the Sample With an apriori power analysis, we determined a required sample size of 202 participants, expecting a moderate effect ( f = 0.25 ), a significance threshold α = 0.05 2 = 0.025 due to testing two hypotheses, a desired power of (1- β) = 0.9 and planning to test two groups (i.e., search engine, chatbot) with between-subjects ANOVAs."

> "Results of an ANOVA indicate no difference in argument expansion between search engine and chatbot ( F ( 1,192 ) = 0.37 , p = .55 , f = .04 )."

> "An ANOVA indicated no difference in critical reasoning between the search and the chatbot ( F ( 1,192 ) = 0.085 , p = .77 , f = .02 )."

**2608.24224v1, Aura (retrieved 2026-09-06).** Kendall's W on the Friedman omnibus,
nothing on the post-hoc Wilcoxon tests.

> "A Friedman test confirmed a significant global effect ( χ 2 = 12.90 , p = .002 , W = 0.323 ), with post-hoc Wilcoxon tests showing a significant reduction against Llama-3 ( p < .001 )."

> "As detailed in Table 2 , Aura yielded the highest normalized learning gain ( g = 0.59 ± 0.22 ) compared to GPT-4o ( 0.54 ± 0.33 ) and Llama-3 ( 0.41 ± 0.38 ), and significantly outperformed the latter ( p = .028 , Wilcoxon; global Friedman p = .167 )."

(The `g` in that second sentence is Hake's normalized learning gain, a domain measure,
not Hedges' g. It is not an effect size and is not counted as one.)

### 3.3 The fourteen papers with no effect size, and what stands in its place

These are the sentences that carry the paper's main quantitative claim. Each reports a
test statistic and a p value and stops.

**2607.27938v1, VizPilot (cs.HC).** Wilcoxon signed-rank throughout, n = 16, p values only.

> "Given the non-parametric nature of our ordinal survey data and paired task times, all statistical comparisons between the two conditions were conducted using the Wilcoxon signed-rank test."

> "Participants using VizPilot ( M viz = 194.38 , S D = 92.42 ) were significantly faster than those relying on the text baseline ( M base = 262.86 , S D = 150.79 ), saving an average of 68 seconds, a statistically significant improvement ( p = 0.039 ) confirming that our VizPilot accelerates insight extraction."

**2608.10337v1, Narrative Keyframing (cs.HC).** Wilcoxon signed-rank, n = 12, W and p
reported, no effect size and no interval anywhere.

> "Analysis: For quantitative measures in the post-condition standardized surveys, we employed the Wilcoxon signed-rank test to account for the small sample size and the non-normal distribution of the data."

> "To analyze the exit comparative questionnaire, we conducted a one-sample Wilcoxon signed-rank test using the neutral rating (4) as the population mean following prior work ( Yen et al., 2024 )."

> "Specifically, the system helped users better think through the task ( M = 6.92 vs. 4.83 , W = 45.00 , p = .004 ∗ ∗ ) and was perceived as significantly more transparent regarding its generative processes ( M = 6.42 vs. 4.00 , W = 55.00 , p = .003 ∗ ∗ )."

> "Crucially for creative tasks, our system scored significantly higher in exploration ( M = 6.58 vs. 4.58 , W = 45.00 , p = .004 ∗ ∗ ) and expressiveness ( M = 6.58 vs. 5.08 , W = 45.00 , p = .004 ∗ ∗ ), suggesting that the our system allowed users to better explore the design space of characterization and express their creative intent in storytelling."

> "In the comparative survey, participants reported that it better supported their control over how each character’s perspective was reflected in the final story ( M = 6.00 , S D = 1.41 , V = 73.50 , p = .003 ∗ ∗ ), as well as their ability to deliberately shape each character’s portrayal at different points in the story ( M = 6.42 , S D = 0.79 , V = 78.00 , p < .001 ∗ ∗ ∗ )."

**2607.27697v1, DP-LENS (cs.HC).** A full mixed parametric and non-parametric protocol,
n = 18, and not one effect size.

> "For normally distributed outcomes ( p > .05 ) , we used one-way repeated-measures ANOVA; sphericity was evaluated with Mauchly’s test, and Greenhouse–Geisser correction was applied when necessary."

> "For non-normal data ( p < .05 ) , we used Friedman tests."

> "Significant main effects were followed by Bonferroni-corrected pairwise comparisons using paired t-tests for parametric data and Wilcoxon signed-rank tests for nonparametric data."

> "As Mauchly’s test indicated a violation of sphericity ( p < .001 ), the Greenhouse-Geisser correction was applied ( F ( 2 , 34 ) = 5.26 , p = .026 )."

> "In the Vortex dataset, 11 participants (61.1%) preferred DP-LENS, compared with 5 (27.8%) for V-SLICE and 2 (11.1%) for WIM-NAV; this distribution differed significantly from chance ( χ 2 ( 2 ) = 7.00 , p = .030 )."

> "In the PointCloud dataset, 14 participants (77.8%) preferred DP-LENS, 4 (22.2%) preferred V-SLICE, and none preferred WIM-NAV ( χ 2 ( 2 ) = 17.33 , p < .001 ).In the Vessel dataset, 17 out of 18 participants(94.4%) preferred DP-LENS, with the remaining participant selecting V-SLICE and none selecting WIM-NAV ( χ 2 ( 2 ) = 30.33 , p < .001 )."

That last pair is directly comparable to a sign test on preference counts. The paper
reports chi-squared against chance, no interval on the proportion and no effect size.

**2608.27932v1, Graphionale (cs.HC).** Regression coefficients and contrast deltas, no
standardized effect size, intervals in figures only.

> "The rationale format × task modality interaction was significant across all four trust-calibration metrics (Appropriate Trust: b = 0.049 , p < .001 ; Over-Trust: b = − 0.064 , p = .005 ; Under-Trust: b = − 0.040 , p = .004 ; Error Correction: b = 0.090 , p < .001 )."

> "Point estimates and 95% CIs are shown in Figure 3 ."

> "Collapsed across difficulty, graphical rationales significantly reduced Over-Trust ( Δ = − 0.144 , p = .033 ) and increased Error Correction ( Δ = + 0.127 , p = .040 )."

> "Where graphical rationales objectively reduced over-trust and improved error correction, participants rated the experience lower on Satisfaction ( Δ = − 0.76 , p = .017 ), Usability ( Δ = − 0.72 , p = .013 ), and Learning Gain ( Δ = − 0.82 , p = .013 ), and reported higher Task Load ( Δ = + 0.53 , p = .045 )."

**2608.19551v2, Delegating or Doing (cs.HC).** Chi-squared statistics from GLMs, no
effect size, no interval.

> "A linear mixed model revealed no significant effect of interaction mode on task execution time, F ( 2 , 64.6 ) = 0.26 , p = .772 ."

> "A Negative Binomial generalized linear model revealed a significant effect of interaction mode on clicks, NB-GLM , χ 2 ( 2 ) = 37.50 , p < .001 , and the omnibus test also revealed a significant effect of interaction mode, χ 2 ( 2 ) = 38.20 , p < .001 ."

> "Post-hoc pairwise comparisons indicated significant differences between Hybrid and AI-First ( p < .001 ), Hybrid and Traditional ( p = .047 ), and AI-First and Traditional ( p < .001 )."

**2609.01588v1, Designing Proactive Thought Partners for Writing (cs.HC).**

> "A linear mixed-effects model with participant as a random effect showed that satisfaction increased significantly with session index ( b = 0.33 , S E = 0.16 , p = .036 ), indicating that participants became progressively more satisfied with the probe as they gained experience over the course of the deployment."

**2609.02122v1, AI agents reshape consensus formation (cs.CL).** Mann-Whitney U reported
with U and p and no effect size, twelve times, while means carry bootstrap intervals.

> "Compared with the pure-human baseline group (mean consensus strength = 0.695), consensus strength at the low agent proportion (12.5%) increases by 8.0% on average ( z = 3.282 , p = 0.001 )."

> "However, at the intermediate proportions (33.3%, 50%), consensus formation is significantly impaired, dropping by 23.1% ( z = − 12.326 , p < 0.001 ) and 14.5% ( z = − 6.156 , p < 0.001 ), respectively."

> "However, starting from 33.3%, this asymmetry reverses: humans move toward agents significantly more than agents move toward humans (33.3%: U = 104 , p = 0.007 ; 50%: U = 129 , p < 0.001 ; 75%: U = 103 , p < 0.001 ), indicating that agent-led assimilation becomes the dominant mode of linguistic convergence as agent proportion increases."

> "From human-led consensus to agent-led consensus, concreteness decreases significantly from 2.986 (95% CI: [2.954, 3.017]) to 2.724 (95% CI: [2.704, 2.745]; Mann–Whitney U = 12914 , p < 0.001 ), indicating that agent-led consensus relies more on abstract descriptions."

> "Perceived AI identity exerts a significant negative effect ( β = − 0.463 , 95% CI=[-0.671, -0.254], p < 0.001 )."

> "At 12.5%, agents tended to move more toward the human linguistic space than humans moved toward the agent space (average movement 0.822 for agents and 0.575 for humans, Mann–Whitney U = 18 , p = 0.135 ), though this does not reach significance given the small number of agents in this condition ( n = 3 )."

This is the standard pattern for a Mann-Whitney in this literature: the group means get
intervals, the test itself does not get an effect size.

**2609.01202v1, TrialGPT 2.0 (cs.CL).** Percentile bootstrap intervals on every reported
rate, Wilcoxon signed-rank for the paired comparisons, no effect size.

> "Statistical comparisons used two-sided Wilcoxon signed-rank tests for paired reviews and a two-sided Mann-Whitney U test between clinicians."

> "Statistical comparisons between assisted and unassisted screening times used two-sided Wilcoxon signed-rank tests at the case level."

> "For these metrics, 95% confidence intervals were computed by percentile bootstrap over cases with 10,000 resamples (Fig. 3 b)."

> "For individual benchmark results, approximate 95% confidence intervals were computed as the mean ± 1.96 standard errors across patient queries."

**2608.30719v1, Mind the Gap (cs.CL).** Exact McNemar with bootstrap intervals in a
table, percentage-point margins in prose, no effect size.

> "All six same-seed FAR/FTR comparisons against DPO are significant under McNemar tests ( p ≤ 3 × 10 − 3 ; full per-seed results in Appendix E.1 )."

> "First, the FAR/FTR advantage replicates at the individual-run level: all six same-seed comparisons against DPO are significant under McNemar tests ( p ≤ 3 × 10 − 3 ), with net margins of + 14.4 – + 42.5 percentage points for FAR and + 13.3 – + 36.7 for FTR."

> "Table 5: Primary-run evaluation on the held-out test set ( n = 278 ; 120 warranted and 158 aligned contexts). 95% bootstrap CIs (B=2,000)."

**2608.28467v1, Stranger, Fan, or Peer (cs.CL).** Exact McNemar on 4,375 matched pairs
with bootstrap intervals, effects stated in percentage points, no standardized effect
size. It says so explicitly.

> "With model, training regime, and evaluation condition fixed, each of the 4,375 test dialogues gives a matched Strangers / Fan pair, so we test correctness with two-sided exact McNemar tests and report 95% confidence intervals from 10,000 bootstrap resamples Table 6 )."

> "However, we do not claim that the exact effect sizes will transfer unchanged to other model families or scales."

> "First, training under Fan rather than Strangers does not itself increase leakage into the interlocutor’s turns ( − 0.09 pp, p = 0.85 ) or identification accuracy ( + 0.75 pp, p = 0.21 ): the disclosure has to occur at inference to matter."

> "Under Trn Strangers , moving inference from Strangers to Fan raises leakage by 0.91 pp ( p = 0.007 ); under Trn Fan , Trn Peers , and Trn I+I- the same change is not significant (all p > 0.3 )."

**2608.26638v2, Which Metrics Save the Most Human Annotation (cs.CL).** A methods paper
about intervals and tests. It uses "effect size" to mean the unstandardized mean
difference, and states the WMT convention for non-parametric testing.

> "The first is parametric vs. non-parametric inference : standard PPI yields parametric hypothesis tests and confidence intervals, whereas WMT shared tasks have traditionally relied on non-parametric procedures, such as the sign test ( Callison-Burch et al., 2012 ) , bootstrap resampling ( Bojar et al., 2016 ) , and the Wilcoxon signed-rank test ( Kocmi et al., 2025 )."

> "The dominant parametric choice for MT/NLG is the paired t -test ( van der Lee et al., 2021 ) ; non-parametric alternatives including Wilcoxon signed-rank ( Kocmi et al., 2025 ) and rank-sum ( Kocmi et al., 2023 ) , paired bootstrap ( Koehn, 2004 ) , and the paired permutation test (also known as the approximate randomization test ( Graham et al., 2014 ) ), are widely used and often preferred."

> "The effect size is expressed in the original scale of the human scores and is not normalized."

> "However, since p-values are not effect sizes or calibrated probabilities, this is best understood as a heuristic measure of agreement."

**2608.23705v2, The Limits of Automatic Evaluation of Creativity (cs.CL).** Kendall tau-b
as the estimand, verbal magnitude labels with no convention named.

> "The vast majority of correlation coefficients fall within the [ − 0.2 , 0.2 ] range, indicating very weak to negligible relationships."

> "Furthermore, Surprise displays a near-zero correlation ( τ b = 0.01 , p = 0.867 ), providing strong evidence that the LLM’s assessment of narrative unpredictability is fundamentally misaligned with the human experience of surprise."

> "Even among the seven statistically significant ( p < 0.05 ) dimensions, the strength of the agreement remains remarkably weak."

> "The highest correlation observed in the entire study occurs for Elaboration ( τ b = 0.31 , p < 0.001 )."

**2609.02651v1, WinoQueer-NL (cs.CL).** Interprets a correlation by variance explained
rather than by a magnitude convention.

> "Only nine of the thirteen models have a p-value<0.05, but due to the large sample sizes even the largest effect ( r = 0.1189 for XLM-RoBERTa (Base)) explains under 1.5% of variance ( r 2 ≈ 0.014 )."

**2609.00491v1, MemeBridge (cs.CL).** Significance claimed without naming a test.

> "For the multiple-choice task, 17.1% of all responses selected the human-assumed distractor ( D 1 ), while 24.0% selected the LLM-generated distractor ( D 2 ), indicating that Chinese participants were significantly more misled by the LLM-generated distractor than the human-assumed distractor ( p < 0.001 )."

### 3.4 Non-parametric effect-size practice outside the 24, from the same 270-paper pool

These are supplementary and are not in the 24-paper counts. They answer the specific
question about what accompanies a rank test.

**2608.11200v1, ConVAWG (cs.CL, retrieved 2026-09-06).** Matched-pairs rank-biserial
correlation, plus Kendall's W on the Friedman omnibus, plus bootstrap intervals on the
paired difference. This is the most complete non-parametric reporting found anywhere in
the pool.

> "Table 4 reports, for each baseline, the paired mean difference to ConVAWG with a 95% bootstrap percentile confidence interval (10,000 resamples over personas), the two-sided paired Wilcoxon signed-rank p -value with Holm-Bonferroni correction across the eight baselines, and the matched-pairs rank-biserial correlation r as effect size."

> "A Friedman test (the non-parametric repeated-measures ANOVA) across the nine systems rejects the null hypothesis of equal quality on all three aggregates: Avg-D χ 2 ( 8 ) = 317.2 , Avg-G χ 2 ( 8 ) = 298.8 , and Avg χ 2 ( 8 ) = 325.8 (all p < 10 − 4 ), with Kendall’s W of 0.79, 0.75, and 0.81 respectively, indicating strong concordance across personas in how the systems rank."

> "Excluding the GPT-5.2 judge, the remaining three-judge average ranks ConVAWG first on both aggregates (Avg 4.85 vs. 4.75 for DiaSynth, the strongest baseline; Avg-D 4.84 vs. 4.78), and every Holm-corrected Wilcoxon comparison against the eight baselines remains significant on both Avg and Avg-D (all p < 10 − 4 , r ≥ + 0.78 ); removing the backbone judge thus widens rather than narrows ConVAWG’s margin, consistent with the self-preference direction documented in the global-metric analysis below."

**2606.26614v2, HiLSVA (cs.HC, retrieved 2026-09-06).** Cliff's delta with Kendall's W,
and a verbal label attached to a non-significant test.

> "Because each participant experienced all three modes, we tested these differences with a Friedman test, which was not significant ( χ 2 ( 2 ) = 5.09 , p = 0.078 , Kendall’s W = 0.19 [ 35 ] ); Holm-corrected pairwise Wilcoxon tests likewise showed no significant pair, though full-auto versus mix-initiative had a large effect size (Cliff’s δ = − 0.51 [ 14 ] )."

> "Collapsing the two expert groups ( n = 7 ), experts rated the system slightly lower than non-experts ( 4.51 vs. 4.87 ; Mann-Whitney p = 0.080 , Cliff’s δ = − 0.63 ), consistent with non-experts benefiting more from agent assistance while expert users judged it more critically."

**2604.10575v1, NexusAI (cs.HC, retrieved 2026-09-06).** Announces effect size r for
Wilcoxon without defining the formula.

> "Data Analysis For all subjective and structural metrics, we performed Wilcoxon signed-rank tests to compare paired scores between NexusAI and the baseline."

> "For each test, we report the level of significance ( p ) and the effect size ( r ) to characterize the magnitude of the observed effects."

**2607.08912v1, MemeBuddy (cs.HC, retrieved 2026-09-06).** Kendall's W for Friedman and
r for the post-hoc Wilcoxon, both relegated to an appendix, with a magnitude label and
an implicit threshold.

> "Friedman tests showed a significant effect of condition on Intent Clarity for all models (Gemini Flash: χ 2 ( 2 ) = 28.34 , p < .001 , W = 0.142 ; Gemini Pro: χ 2 ( 2 ) = 9.64 , p = .008 , W = 0.048 ; GPT: χ 2 ( 2 ) = 19.18 , p < .001 , W = 0.096 ; Gemma: χ 2 ( 2 ) = 29.49 , p < .001 , W = 0.147 ), with small effect sizes."

> "C.2 Effect Sizes Table 9 shows Kendall’s W for Friedman tests on Intent Clarity ."

> "All effect sizes are small ( W ≤ 0.15 ), indicating that although condition differences are statistically significant, their practical impact on comprehensibility is limited."

> "C.3 Pairwise Effect Sizes Table 10 reports representative Wilcoxon signed-rank effect sizes ( r )."

**2607.10711v1, Lottery and Sprint Arcade (cs.HC, retrieved 2026-09-06).** The only paper
in the pool that puts an interval on the rank-test effect size r itself, and it does so
to argue a null.

> "As shown in Fig. 2 , pairwise Wilcoxon tests with multiple-comparison correction revealed no statistically reliable differences between groups for NASA-TLX, Post Survey items, or UEQ scales (all corrected p values non-significant; | r | ranged from 0.02 to 0.17, 95% CIs spanning zero)."

> "Observed effect sizes were consistently small ( | r | ranged from 0.02 to 0.17, with 95% CIs spanning zero), suggesting no practically meaningful differences across groups."

> "While this sample is sufficient for exploratory analyses, the statistical power of pairwise Wilcoxon tests at these group sizes is limited, particularly for detecting small effects."

**2604.06211v2, Illocutionary Explanation Planning (cs.CL, retrieved 2026-09-06).**
Cohen's d_z reported alongside Wilcoxon signed-rank, with verbal labels tied to
conventional benchmarks.

> "Following a Shapiro-Wilk normality test, non-parametric Wilcoxon signed-rank tests were used for FActScore and number of adherent clauses (since they were not normally distributed), while paired t-tests were applied to mean semantic similarity."

> "Adherence is often lower for larger models, though the trend is not monotonic across model families. 5 RQ2: Illocutionary Macro-Planning for Source-Faithful Explanations Figure 1: Source faithfulness across six LLM , with one-sided p-values (significant in bold), Cohen’s dz effect sizes, and 95% confidence intervals (CI)."

> "These gains in adherent clauses are supported by small-to-medium Cohen’s dz effect sizes across models ( d z = 0.367 for Mistral up to d z = 0.550 for Llama 3-70B) indicating consistent, statistically reliable increases in factuality."

> "Finally, the Cohen’s d values for the Mann-Whitney U tests above are between 0.19 to 0.34, indicating small effect sizes by conventional benchmarks."

> "An a priori power analysis confirmed that this dataset exceeds the 74-question minimum needed for the paired RQ2 comparisons (assuming a small-to-moderate effect size of Cohen’s d z = 0.3 , 1 − β ≥ 0.8 , and α ≤ 0.05 ) [ 30 ]."

**Interval methods for proportions across the whole 270-paper pool.** Three papers use a
Wilson score interval, and no paper uses an exact binomial (Clopper-Pearson) interval.

> "Appendix D Statistical Analysis D.1 Confidence intervals Table 7 reports Wilson 95% CIs for every cell in the main results tables." (2605.10930v2, cs.HC)

> "Bars are Wilson 95% CI." (2608.29995v1, cs.CL)

> "Each query has exactly one gold description; we report top- k retrieval accuracy ( k = 1 , 5 , 10 ) against the full vocabulary, with Wilson 95% CIs." (2609.03788v1, cs.CV)

> "Table I itself reports only point estimates and Wilson CIs; every p -value in this section, starting here, is instead from a separate paired exact McNemar test on the same items, comparing two of the table’s accuracy figures at a time." (2609.03788v1, cs.CV)

> "Sample sizes are modest ( n = 100 – 200 ): across Table I ’s 36 cells the average Wilson CI half-width is ± 5.7 pp, which bounds how small an effect this design can resolve in general, including the TS2 arm-vs-control comparison above." (2609.03788v1, cs.CV)

## 4. Counts

All counts are over the 24-paper corpus unless a line says "270-paper pool."

### 4.1 Effect size, any measure

| Denominator | Reports a named effect size alongside a test | Rate |
|---|---|---|
| All 24 | 10 | 42% |
| cs.CL (12) | 4 | 33% |
| cs.HC (12) | 6 | 50% |

Which measure, counting a paper once per measure it uses:

| Measure | Papers (of 24) |
|---|---|
| Cohen's d or d_z | 3 (2609.02480, 2608.29995, 2608.06151) |
| odds ratio | 4 (2609.00685, 2608.29995, 2608.29446, 2608.06151) |
| partial eta-squared or eta-squared | 2 (2608.19083, 2608.21177) |
| Hedges' g | 1 (2608.19083) |
| Cohen's f | 1 (2608.14113) |
| Kendall's W | 1 (2608.24224) |
| r = abs(Z)/sqrt(N) | 1 (2608.09698) |
| Cliff's delta | 0 |
| rank-biserial correlation | 0 |
| Cramer's V | 0 |

Across the full 270-paper pool, counting a paper if the measure is named anywhere in its
text: Cohen's d or d_z in 21, odds ratio in 12, eta-squared in 11, Kendall's W in 8 (of
which 5 use it as the effect size for a rank test and 3 use it as an inter-rater agreement
statistic), Cohen's f in 6, Hedges' g in 2 (one of them only inside a power calculation),
Cliff's delta in 1, rank-biserial correlation in 1, Cramer's V in 0. The phrase "effect
size" appears anywhere in 40 of 270, which means roughly 85% of these papers never write
the words. These are string counts checked by reading the matched sentence, so
bibliography artifacts are excluded: "Hedges" also appears as the surname in a citation to
Lakoff's paper on hedges, and "Cohen" appears far more often as Cohen's kappa than as
Cohen's d.

### 4.2 Confidence intervals

| | All 24 | cs.CL (12) | cs.HC (12) |
|---|---|---|---|
| Numeric interval in running prose | 5 (21%) | 3 | 2 |
| Numeric interval anywhere (prose, table, or caption) | 9 (38%) | 6 | 3 |
| No numeric interval anywhere | 15 (62%) | 6 | 9 |

The quantity the interval sits on, for the 9 papers that report one: an unstandardized
mean or proportion difference (5), a regression coefficient beta or b (4), an odds ratio
(2), a group mean (2), a metric score such as F1 or accuracy (3). Papers can appear in
more than one row.

**An interval on the effect size itself: 2 of 24, and 0 of 24 for a standardized effect
size.** The two are 2608.29446 and 2608.06151, and in both cases the effect size that
carries the interval is an odds ratio, which comes with an interval automatically
because it is a model coefficient. Not one paper in the 24 reports a d, g, r,
eta-squared, f, Kendall's W, Cliff's delta or rank-biserial with an interval on it.
Across the whole 270-paper pool, exactly one paper does it (2607.10711v1, quoted in 3.4,
reporting abs(r) from 0.02 to 0.17 with intervals spanning zero).

**Against the earlier survey.** The earlier hand-picked survey found effect size with an
interval in 3 of 19 results sections and intervals in prose in 2 of 19. This differently
selected sample of 24 gives 2 of 24 for an effect size with an interval (both odds
ratios), and 5 of 24 for a numeric interval in prose. The two estimates are consistent:
both put effect-size-with-interval in the 8 to 16 percent range, and prose intervals in
the 10 to 21 percent range. The earlier finding survives the test.

### 4.3 Verbal magnitude labels and the conventions behind them

Nine of 24 papers attach a verbal label (small, medium, moderate, large, negligible,
weak) to some quantity. Only 4 of those attach it to an effect size in a results claim:
2609.02480 ("a large within-dialogue effect size"), 2608.29995 ("above the conventional
'large effect' threshold of 0.8"), 2608.09698 ("both with large effect sizes"), and
2608.19083 ("The trust interaction was small").

**Which convention.** Only one paper in the 24 names a numeric threshold and a source:
2608.29995 cites Cohen (1988) in its reference list and writes "the conventional 'large
effect' threshold of 0.8". Three papers state a convention only inside a power analysis,
where G*Power supplies it: 2608.19083 and 2608.27932 both use "medium effect size
(Cohen's f = .25)", and 2608.14113 uses "a moderate effect ( f = 0.25 )". Two papers
supply their own implicit threshold rather than citing one: 2607.08912 with "All effect
sizes are small ( W ≤ 0.15 )" and 2608.23705 with "The vast majority of correlation
coefficients fall within the [-0.2, 0.2] range, indicating very weak to negligible
relationships". In the supplementary set, 2604.06211 writes "indicating small effect
sizes by conventional benchmarks" without naming which.

The pattern is that the label is used more often than the convention is cited. Nobody in
this sample cites the r thresholds for a rank-test effect size (Cohen's 0.1 / 0.3 / 0.5)
by source, including the paper that computes r as abs(Z)/sqrt(N).

### 4.4 What accompanies a non-parametric test

Restricting to the 36 papers in the 270-pool that run a Wilcoxon test of any kind:

| Effect size accompanying Wilcoxon | Papers |
|---|---|
| None at all | 27 of 36 (75%) |
| r, computed or implied from Z | 5 (2608.09698, 2604.10575, 2607.08912, 2607.10711, 2604.22237) |
| Cohen's d or d_z applied to the paired differences | 3 (2604.06211, 2608.06549, 2609.02480) |
| Kendall's W, named (Friedman omnibus only, never the pairwise test) | 3 (2606.26614, 2607.08912, 2608.11200) |
| rank-biserial correlation | 1 (2608.11200) |
| Cliff's delta | 1 (2606.26614) |

Rows overlap: 2608.11200 and 2606.26614 each appear twice. One further paper
(2608.24224) reports "W = 0.323" for a Friedman without naming the statistic, which is
Kendall's W by context and is not counted in the named row.

**Is abs(Z)/sqrt(N) the convention?** It is the most common named effect size for a
Wilcoxon in this literature, but it is not dominant, and it is not usually written out.
Only one paper in the entire 270-paper pool states the formula (2608.09698: "We report
effect sizes as r = |Z| / sqrt(N_eff)"). Four others report an r for Wilcoxon without
saying how it was computed. The competing conventions are Cohen's d_z applied to the
paired differences (which is what a reviewer from the psychology side may prefer, and
what 2609.02480 and 2604.06211 do), and matched-pairs rank-biserial correlation (which
is what a statistician would prefer, and which exactly one paper uses). Kendall's W
is named in three of them, and in all three it is attached to the Friedman omnibus, never
to a pairwise Wilcoxon.

There is no house style. Reporting r = abs(Z)/sqrt(N) with the formula stated is at the
top of the observed practice, not outside it.

**Sign tests and exact binomial intervals.** The sign test is named exactly once in the
270-paper pool, and there as a citation to WMT practice rather than a test the paper
runs (2608.26638). No paper in the pool runs a sign test on its own data. No paper uses
an exact binomial (Clopper-Pearson) interval. Three use a Wilson score interval on a
proportion, and 49 use a bootstrap. The bootstrap is described in a consistent register:
"a bootstrap 95% confidence interval of [0.0145, 0.0209]", "95% bootstrap percentile
confidence interval (10,000 resamples over personas)", "95% confidence intervals were
computed by percentile bootstrap over cases with 10,000 resamples", "95% bootstrap CIs
(B=2,000)". Papers name the resample count and the interval type (percentile) and stop.

### 4.5 Negative and null results versus working-method results

Coding: W means the paper's main claim is that a proposed method or system works; N
means the main claim is a null, a limitation, or a descriptive characterization. Twelve
of each.

| Group | Reports an effect size | Rate | Reports a prose interval | Rate |
|---|---|---|---|---|
| Working method (W, n = 12) | 6 | 50% | 3 | 25% |
| Null, negative, or descriptive (N, n = 12) | 4 | 33% | 2 | 17% |

Between-paper, the two groups are close and the direction runs mildly against the
hypothesis: papers with a working method report effect sizes slightly more often, not
less. With n = 12 per cell this difference is not worth interpreting.

The within-paper pattern is the one that matters and it runs the other way. Papers that
report effect sizes at all attach them to their own null results without exception:

- 2608.14113 reports f = .04 and f = .02 on two ANOVAs that find nothing, and those are
  the paper's entire quantitative result.
- 2608.19083 reports "Δ M = .018 , 95% CI [ − .376 , .413 ] , p = .927 , g = .014" and
  "Δ M = − .497 , 95% CI [ − 1.124 , .129 ] , p = .119 , Hedges’ g = − .253 , but the
  confidence interval included zero" for its null contrasts.
- 2609.02480 reports d_z = 0.06 and d_z = -0.01 for the two ablations where the Wilcoxon
  fails to reject.
- 2608.06151 reports "d = − .005" and "d = − 0.12" on its null follow-up analyses.
- 2607.10711 (supplementary) states abs(r) from 0.02 to 0.17 with intervals spanning
  zero and uses that, not the p values, to argue the null.

So the effect size is the instrument for arguing a null when a paper has one. The
papers that report no effect size argue their nulls from p alone: 2608.19551 with
"F ( 2 , 64.6 ) = 0.26 , p = .772", 2609.02122 with "does not reach significance",
2608.09698 with "did not survive correction".

## 5. Assessment for the manuscript

The design in question: a paired Wilcoxon signed-rank on n = 50 with r = 0.658 computed
as abs(Z)/sqrt(N), companion values around 0.53, a sign test on 286 non-ties at 69.6%
with an exact 95% binomial interval of 63.9 to 74.9, and chi-squared tests.

### 5.1 What this literature expects alongside each piece

**The Wilcoxon with r = 0.658.** Expected: the test statistic (W or V), the exact or
approximate p, and n. Half the papers stop there. Reporting r at all puts the paper in
the top third of the 270-paper pool, and stating the formula puts it in a set of one.
The paper should therefore keep the formula, because it is the thing almost nobody
supplies and the thing a methods-minded reviewer will otherwise ask for. Nothing in this
sample reports a bootstrap interval on r, so its absence will not be noticed. Its
presence would be unusual in a good way and would cost two numbers.

The one genuine risk is the choice of r itself. The rank-based alternative a statistician
would name first is the matched-pairs rank-biserial correlation, and exactly one paper in
the pool uses it (2608.11200, which reports it as "the matched-pairs rank-biserial
correlation r as effect size"). A reviewer who prefers it will say so. The cheapest
defense is a single sentence in the analysis subsection saying r is defined as
abs(Z)/sqrt(N) and citing a source for the 0.1 / 0.3 / 0.5 thresholds if a verbal label
is used anywhere. No paper in the sample does this, which is exactly why it is the
inexpensive edge.

**The verbal label.** At r = 0.658 a "large" label is available under the standard r
convention. Four of 24 papers use a label; only one names a numeric threshold with a
source. Using the label is normal; using it with a citation is above convention. If the
label is used, use it once, at the first report, and not on every line.

**The sign test at 69.6% with an exact 95% interval of 63.9 to 74.9.** This is where the
manuscript departs from the sample most sharply, and the departure is favorable. No paper
in the 270-paper pool runs a sign test on its own data, and none uses an exact binomial
interval. The closest comparators handle preference counts with a chi-squared against
chance and no interval (2607.27697: "11 participants (61.1%) preferred DP-LENS ... this
distribution differed significantly from chance ( χ 2 ( 2 ) = 7.00 , p = .030 )"), or
with a Wilson interval (three papers). A reviewer will not have seen an exact binomial
interval in this venue recently, so the manuscript should name the method rather than
assume it reads as standard: "exact binomial (Clopper-Pearson) 95% interval" rather than
"exact 95% CI". One clause of definition removes the only ambiguity.

What is genuinely unusual and should be flagged as deliberate: reporting the number of
non-ties (286) as the denominator. Nothing in this sample explains its denominator for a
paired proportion. Stating it plainly is a strength; stating it in passing invites a
reviewer to wonder what the tie count was, so give both.

**The chi-squared tests.** The convention here is stark: 6 papers in the 24 run a
chi-squared and none reports Cramer's V or any other association measure. Cramer's V
appears zero times in 270 papers. Adding it would be correct and would read as
unfamiliar; omitting it matches every comparator. If association strength matters to the
argument, the observed practice is to report the underlying percentages side by side,
which several papers do (2608.29446: "86.3% vs. 62.7%"; 2608.06151: "9.7 percentage
points less").

### 5.2 What would be unusual

Unusual in a way that helps, and cheap to keep:

- Stating the effect-size formula. One paper in 270 does it.
- An interval on the effect size. Two of 24 have one, both via odds ratios, and zero have
  one on a standardized effect size.
- An exact binomial interval on a proportion. Zero of 270.
- Reporting the effect size on the null comparisons as well as the significant ones.
  Every paper in the sample that reports effect sizes at all does this, so it is expected
  conditional on reporting them, and it is the practice this manuscript should follow
  without exception.

Unusual in a way that would draw a question:

- A verbal magnitude label with no convention cited, if the label is doing argumentative
  work. Nine papers label; one cites a threshold with a source. The label is normal, the
  uncited label carrying an argument is where a referee will push.
- r = abs(Z)/sqrt(N) with no definition. Four of the five papers that report r for a
  Wilcoxon leave the formula unstated, which means a referee reading r = 0.658 has no way
  to know whether it is that formula, a rank-biserial, or a Pearson correlation. Define
  it once.
- Any implication that abs(Z)/sqrt(N) is the field's standard. It is the most common
  named choice, but 75% of papers running a Wilcoxon report no effect size at all, so
  there is no standard to invoke. Describe it as the measure used, not the convention.

Not unusual, and not worth adding:

- Cramer's V on the chi-squared tests.
- Bootstrap intervals on the Wilcoxon effect size, unless they are wanted for their own
  sake. No comparator has them, and their absence is invisible.
- A power analysis. Four of 24 report one, all in HCI, all through G*Power, and all
  before the fact. A post-hoc power statement would read as odd; a minimum detectable
  effect statement would read as unusually careful.

### 5.3 The community split, stated plainly

The two communities differ less than expected on whether an effect size appears (33% for
cs.CL, 50% for cs.HC) and more on what kind. cs.CL papers that report one reach for an
odds ratio from a fitted model (4 of 4 cs.CL cases involve an OR or a d from a model),
and their intervals come from bootstraps over items or systems. cs.HC papers reach for
the psychology inventory: eta-squared, Cohen's d, Cohen's f, Kendall's W, r from Z, all
of which arrive through G*Power and the standard analysis packages. Sample sizes explain
part of it. The cs.HC corpus splits into small lab studies (12, 12, 16, 16, 18, 20 and
22 participants in 2608.10337, 2608.09698, 2609.01588, 2607.27938, 2607.27697,
2608.24224 and 2608.21177), where a p value alone says almost nothing and an effect size
is the only available statement of magnitude, and two large online experiments
(2608.19083 with 306 participants and 2608.06151 with roughly 1,950), which report the
fullest effect-size and interval sets in the corpus. The cs.CL evaluations mostly run
hundreds to thousands of items, where p values fall below 10^-15 and magnitude has to be
argued from the raw difference instead.

A paper submitted to an NLP venue that reports a rank-test effect size with its formula,
a sign test with an exact binomial interval, and effect sizes on its nulls is reporting
above the convention of both communities on every one of those three counts.

## 6. Reproduction

Queries, identifiers, and dates are in section 1. The screening pool is 270 arXiv HTML
documents retrieved 2026-09-06. Counts in section 4 were produced by string matching over
the extracted text, then checked by reading the matched sentences, which are the ones
quoted in section 3. Where a regular expression and a reading disagreed, the reading
governs, and both cases are noted: the abs(Z)/sqrt(N) formula in 2608.09698 was missed by
pattern matching because the radical glyph does not survive tag stripping, and the
Friedman and ANOVA hits in 2608.30866 and 2609.00832 were bibliography artifacts.
