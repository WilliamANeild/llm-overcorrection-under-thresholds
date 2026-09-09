# What an abstract does when the paper releases no system, benchmark or dataset

Scenario 01. Compiled 2026-09-06. Companion to `acl2026_density.md`, which measured a topic-unconditional systematic sample of 47 abstracts from the 2026 volumes and found that 40 of 47 name an artifact, that all 16 abstracts carrying a quantitative digit also name one, and that the 7 naming none carry no digit either. That corpus cannot say whether the artifact and the digit are causally linked, because it holds only 7 artifact-free cases and all 7 sit in one year. This corpus conditions on the artifact-free case directly and across three years.

## Corpus and how it was drawn

Source: ACL Anthology, retrieved **2026-09-06**. Two passes. The volume listing page of each of 17 volumes carries every paper title and, in a collapsed div, every abstract; those pages supplied the pool and the screen. Each drawn paper was then fetched individually and its abstract taken from the `div` with class `card-body acl-abstract` on the landing page, parsed by walking div nesting rather than assuming a `<span>` follows the heading. **The landing-page abstract matched the volume-page copy for all 46 drawn papers**, so nothing rests on the cheaper source.

Volumes: `2024.acl-long`, `2024.acl-short`, `2024.findings-acl`, `2024.emnlp-main`, `2024.findings-emnlp`, `2024.naacl-long`, `2024.eacl-long`, `2025.acl-long`, `2025.acl-short`, `2025.findings-acl`, `2025.emnlp-main`, `2025.findings-emnlp`, `2025.naacl-long`, `2026.acl-long`, `2026.acl-short`, `2026.findings-acl`, `2026.eacl-long`. All 17 returned HTTP 200. **16,644 papers listed** across them, excluding front matter.

**Screening, in three mechanical steps and one hand step.**

1. *Title signal.* A regex for analysis and empirical-study title shapes: an opening interrogative (Do / Does / Can / Are / Is / When / Why / How / What / Which / Who), an opening gerund (Understanding, Investigating, Exploring, Measuring, Probing, Assessing, Evaluating, Rethinking, Revisiting, Auditing, Tracing, Characterizing), "On the ...", "An Analysis of", "A Study of", "An Empirical Study", "A Case Study". **1,545 of 16,644 titles matched (9%).**
2. *Artifact signal in the abstract.* Any of these disqualifies: release language ("we release", "publicly available", "available at", a URL); a coined capitalised name in the title; a coined capitalised name within 70 characters after an introduce, propose, present, develop, construct, build, design, create or curate verb. Of the 1,545 candidates: **253 excluded for release language, 93 for a coined name in the title, 315 for a coined name after a build verb, 7 had no abstract, 877 passed.**
3. *Systematic draw.* Fixed random start and constant stride within each volume, over the passing pool in Anthology order, seeded 20260906, allocated across volumes in proportion to each volume's share of the pool. **46 drawn.**
4. *Hand adjudication.* A drawn paper is kept only if its stated principal contribution is a finding, not a resource and not a performance-improving method. **14 dropped, 32 kept.** Every drop and its reason is in `handcode_no_artifact.json`; the list is reproduced below so a reader can disagree with any of them.

**Papers dropped at step 4, with the reason.**

- `2024.eacl-long.124`: names and releases a corpus it built (the BEAR-FACT corpus)
- `2024.emnlp-main.679`: names a test suite it built (Shortcut Suite)
- `2024.emnlp-main.8`: method paper; principal claim is that the proposed approach reaches state-of-the-art on DAIC-WOZ
- `2025.acl-long.193`: introduces new metrics, a curated benchmark and an alignment method; closes on the method's improvements
- `2025.acl-short.92`: method paper; principal claim is that the proposed aggregation improves metric results on SEEDA
- `2025.emnlp-main.10`: names a metric it defines and offers for use (Ambiguity Rewrite Metric, ARM)
- `2025.emnlp-main.1184`: survey of prior methods, not an empirical study
- `2025.emnlp-main.504`: names a method it built (Faithfulness by Unlearning Reasoning steps, FUR)
- `2025.findings-acl.1069`: systematic literature review, not an empirical study of model behaviour
- `2025.findings-acl.1317`: names a framework it built (HyFairCRS); principal claim is state-of-the-art performance
- `2025.findings-emnlp.1173`: principal contribution is a constructed text-image corpus plus fine-tuned detectors
- `2026.acl-long.45`: names a method it built (weighted in-context influence, wICI); principal claim is that it outperforms baselines
- `2026.findings-acl.1795`: names a benchmark it introduces (the Cross-Cultural, Cross-Modal, Cross-lingual Multimodal (3XCM) benchmark); missed by the mechanical screen because the acronym begins with a digit
- `2026.findings-acl.81`: names a framework it built (Thought Template Augmented LCLMs, ToTAL)

Two of those drops are also failures of the step-2 regex, and are worth recording as such. `2026.findings-acl.1795` introduces the "Cross-Cultural, Cross-Modal, Cross-lingual Multimodal (3XCM) benchmark"; the acronym begins with a digit, so the capitalised-name regex did not see it. `2024.emnlp-main.679` presents "Shortcut Suite", two ordinary capitalised words, which the regex also misses because it looks for internal capitals or a run of three. **The screen is therefore permissive, not strict: it lets artifact papers through, which the hand step then removes, rather than discarding artifact-free papers.** That is the direction of error to prefer here.

**Bounds on this sample.** The draw is conditional on the title matching an analysis shape, so it says nothing about analysis papers whose titles are declarative ("LLMs cannot plan"). It covers ACL, EMNLP, NAACL, EACL and the two Findings volumes for 2024 through 2026 and no other venue, no workshop, and no arXiv preprint. It is a sample of 32, so a proportion near a half carries a standard error of about 9 percentage points; the comparisons below are directions, not estimates. Papers per year: 2024: 12, 2025: 12, 2026: 8.

**How things were counted.** Word counts, sentence counts, and every numeral count and category are produced by `03_measure.py` (regex tokenizer and sentence splitter), never by eye. A numeral counts as *quantitative* only if it is not part of an identifier: digits inside model names (GPT-2, Qwen2.5, o3-mini, TOEFL11), four-digit years, and enumeration markers are counted separately and excluded. Two tokenizer amendments were made for this corpus and applied upstream in `03_measure.py`: a bare list marker introducing a numbered finding ("four key findings: 1. Larger models ...") is an enumerator, not a quantity, and a digit glued to a following all-caps identifier (the 3 in 3XCM) is part of a name. **Re-measuring the existing 47-abstract and 9-abstract corpora under the amended tokenizer changes no count in either**, so the two corpora remain directly comparable. Five things are hand-coded and marked as such throughout: the step-4 genre judgement, what the abstract names and of what kind, whether the paper coins a term of its own, the closing move, and whether each numeral states the size of the experiment or the size of an outcome.

## Corpus table

Names: the kinds of proper name the abstract carries. `model` = a released model named as an object of study; `dataset` = an existing dataset or lexical resource it runs on; `prior` = a named prior method, architecture or construct it tests or uses; `task` = a task it introduces under a borrowed name; `acronym` = a task or subfield abbreviation; `metric` = a field-standard metric abbreviation; `lang` = a natural language. "Cap" is true only when at least one name is a model, dataset, prior method or introduced task; acronyms, standard metrics and language names do not make it true. "Coin" is true when the paper introduces a noun phrase as its own construct and reuses it, whether or not it is capitalised. Density is quantitative numerals per 100 words.

| Anthology ID | Words | Sent | Quant | Ident | Enum | /100w | Res % | Names | Cap | Coin | Closing move |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `2026.findings-acl.616` | 147 | 7 | 4 | 2 | 0 | 2.72 | 0 | lang, model | y | n | knowledge claim |
| `2025.findings-emnlp.801` | 108 | 5 | 2 | 1 | 0 | 1.85 | 0 | acronym, model | y | n | knowledge claim |
| `2025.findings-emnlp.445` | 137 | 5 | 2 | 7 | 2 | 1.46 | 0 | dataset, metric, model | y | n | knowledge claim |
| `2026.acl-long.1444` | 140 | 12 | 2 | 1 | 4 | 1.43 | 0 | model | y | n | call to community |
| `2024.naacl-long.266` | 195 | 7 | 2 | 0 | 0 | 1.03 | 1 | model | y | n | knowledge claim |
| `2025.acl-long.555` | 201 | 12 | 2 | 6 | 0 | 1.00 | 0 | acronym, model | y | n | future work |
| `2025.findings-emnlp.1380` | 152 | 6 | 1 | 0 | 0 | 0.66 | 0 | none | n | n | call to community |
| `2024.findings-emnlp.841` | 194 | 8 | 1 | 1 | 0 | 0.52 | 0 | metric | n | y | knowledge claim |
| `2024.acl-long.544` | 143 | 8 | 0 | 0 | 0 | 0.00 | 0 | none | n | n | call to community |
| `2024.acl-long.813` | 194 | 8 | 0 | 0 | 3 | 0.00 | 0 | acronym, dataset | y | y | future work |
| `2024.acl-short.26` | 134 | 6 | 0 | 0 | 0 | 0.00 | 0 | none | n | n | knowledge claim |
| `2024.emnlp-main.1009` | 188 | 7 | 0 | 0 | 0 | 0.00 | 0 | lang | n | n | knowledge claim |
| `2024.emnlp-main.348` | 173 | 8 | 0 | 0 | 0 | 0.00 | 0 | none | n | n | contribution restatement |
| `2024.findings-acl.316` | 70 | 3 | 0 | 0 | 0 | 0.00 | 0 | acronym | n | n | knowledge claim |
| `2024.findings-acl.724` | 163 | 7 | 0 | 0 | 0 | 0.00 | 0 | model | y | n | knowledge claim |
| `2024.findings-emnlp.191` | 214 | 9 | 0 | 0 | 0 | 0.00 | 0 | acronym | n | n | contribution restatement |
| `2024.findings-emnlp.467` | 183 | 9 | 0 | 0 | 3 | 0.00 | 0 | none | n | y | call to community |
| `2024.naacl-long.4` | 203 | 7 | 0 | 1 | 0 | 0.00 | 0 | model, task | y | n | future work |
| `2025.acl-long.1010` | 151 | 7 | 0 | 0 | 0 | 0.00 | 0 | none | n | n | knowledge claim |
| `2025.acl-long.1449` | 179 | 8 | 0 | 0 | 0 | 0.00 | 0 | acronym | n | n | knowledge claim |
| `2025.emnlp-main.1499` | 105 | 4 | 0 | 0 | 0 | 0.00 | 0 | dataset | y | n | knowledge claim |
| `2025.emnlp-main.828` | 134 | 7 | 0 | 2 | 0 | 0.00 | 0 | model, prior | y | n | contribution restatement |
| `2025.findings-acl.293` | 149 | 8 | 0 | 0 | 0 | 0.00 | 0 | none | n | n | contribution restatement |
| `2025.findings-acl.806` | 198 | 7 | 0 | 0 | 0 | 0.00 | 0 | none | n | y | knowledge claim |
| `2025.naacl-long.119` | 211 | 7 | 0 | 0 | 0 | 0.00 | 0 | none | n | n | knowledge claim |
| `2025.naacl-long.485` | 156 | 7 | 0 | 0 | 0 | 0.00 | 0 | none | n | n | call to community |
| `2026.acl-long.1860` | 181 | 8 | 0 | 0 | 0 | 0.00 | 0 | none | n | y | knowledge claim |
| `2026.acl-long.436` | 103 | 5 | 0 | 0 | 0 | 0.00 | 0 | lang, prior | y | n | knowledge claim |
| `2026.acl-long.853` | 166 | 5 | 0 | 0 | 0 | 0.00 | 0 | prior | y | y | knowledge claim |
| `2026.acl-short.56` | 150 | 6 | 0 | 0 | 2 | 0.00 | 0 | acronym | n | y | knowledge claim |
| `2026.eacl-long.12` | 138 | 7 | 0 | 0 | 0 | 0.00 | 0 | none | n | y | future work |
| `2026.findings-acl.1284` | 141 | 7 | 0 | 0 | 0 | 0.00 | 0 | model | y | n | knowledge claim |

Titles, URLs and the verbatim abstracts are in `acl2026_abstracts.json` under `no_artifact_2024_2026`.

## Do artifact-free abstracts carry digits?

**8 of 32 (25%) carry at least one quantitative digit. 24 of 32 (75%) carry none.**

Raw counts: 24 abstracts carry 0, 2 abstracts carry 1, 5 abstracts carry 2, 1 abstract carries 4. Across all 32 abstracts there are **16 quantitative numerals in total**.

| Statistic | This corpus (32 artifact-free) | 47-abstract 2026 systematic sample |
|---|---|---|
| words, median | 154 | 161 |
| words, p25 / p75 | 138 / 192 | 153 / 178 |
| sentences, median | 7 | 7 |
| numerals per 100 words, median | 0.00 | 0.00 |
| numerals per 100 words, p75 | 0.39 | 0.64 |
| numerals per 100 words, p90 | 1.45 | 1.88 |
| numerals per 100 words, max | 2.72 | 2.93 |
| numerals per 100 words, mean | 0.33 | 0.48 |
| share carrying at least one digit | 25% (8/32) | 34% (16/47) |
| share carrying a result percentage | 3% (1/32) | 17% (8/47) |

**The artifact-free abstract is the same length as the venue median and about a third less dense at the mean.** Median 154 words against 161, and a mean of 0.33 numerals per 100 words against 0.48. The median is zero in both corpora, so the median does not separate them. What separates them is the share carrying any digit, 25% here against 34 percent there, and the mean.

The reduction is concentrated in one place. **1 of the 32 abstracts reports a result percentage** (`2024.naacl-long.266`, "outperforming the accuracy of existing state-of-the-art zero-shot baselines by an average of 9%"), against 8 of 47 in the 2026 sample. **No abstract in this corpus reports a p-value or an effect size**, which matches the 47-abstract corpus exactly: neither carries one.

Spelled-out numbers: 15 of 32 carry at least one, and **15 of 32 carry neither a digit nor a spelled number.**

### What the digits are doing

Each of the 16 quantitative numerals, hand-classified as stating the size of what was tested (SETUP) or how something performed (OUTCOME), with the clause it sits in quoted verbatim.

| Anthology ID | Numeral | Clause, verbatim | Role |
|---|---|---|---|
| `2024.findings-emnlp.841` | 14.4 | up to an SD of 14.4 F1-score | OUTCOME |
| `2024.naacl-long.266` | 8 | a range of 8 audio-classification datasets | SETUP |
| `2024.naacl-long.266` | 9 | by an average of 9% | OUTCOME |
| `2025.acl-long.555` | 47.8K | The reorganized data contains 47.8K samples | SETUP |
| `2025.acl-long.555` | 18 | we benchmark 18 LLMs | SETUP |
| `2025.findings-emnlp.1380` | 95 | a controlled study (n=95) | SETUP |
| `2025.findings-emnlp.445` | 0.7 | Intraclass Correlation Coefficients (ICC) of approximately 0.7 | OUTCOME |
| `2025.findings-emnlp.445` | 0.95 | compared to GPT-4o mini’s 0.95 | OUTCOME |
| `2025.findings-emnlp.801` | 10K | datasets ranging from 10K to 5M sentences | SETUP |
| `2025.findings-emnlp.801` | 5M | datasets ranging from 10K to 5M sentences | SETUP |
| `2026.acl-long.1444` | 0.5B | the Qwen2.5 series (0.5B to 72B) | SETUP |
| `2026.acl-long.1444` | 72B | the Qwen2.5 series (0.5B to 72B) | SETUP |
| `2026.findings-acl.616` | 200 | manually annotated dataset of 200 short videos | SETUP |
| `2026.findings-acl.616` | 71.5 | a belief score of 71.5/100 | OUTCOME |
| `2026.findings-acl.616` | 100 | a belief score of 71.5/100 | SETUP |
| `2026.findings-acl.616` | 35.2 | while o3 performs the worst at 35.2 | OUTCOME |

**10 of 16 numerals state the size of the experiment; 6 state an outcome.** Six of the eight digit-carrying abstracts put a setup figure first, and the two that lead with an outcome (`2024.findings-emnlp.841`, `2025.findings-emnlp.445`) are the two whose finding is itself a dispersion or reliability statistic. Position of the first statistic, as a fraction of the way through the abstract: median 0.55 against 0.80 in the 47-abstract sample. **In an artifact-free abstract the number arrives earlier, because it is describing the experiment rather than reporting its result.**

## What they name instead of a released system

| What the abstract names | Abstracts | Share |
|---|---|---|
| a released model, by name | 10 | 31% |
| a coined phenomenon or construct of its own | 8 | 25% |
| an existing dataset or lexical resource | 3 | 9% |
| a named prior method, architecture or construct | 3 | 9% |
| a task it introduces under a borrowed name | 1 | 3% |
| a field-standard metric abbreviation | 2 | 6% |
| a task or subfield acronym only | 7 | 22% |
| nothing capitalised beyond acronyms and language names | 18 | 56% |
| a metric it defines and gives a name to | 0 | 0% |
| a released artifact of its own, by construction of the sample | 0 | 0% |

**The substitute for a coined system name is a released model name.** 10 of 32 artifact-free abstracts name at least one model. In the 47-abstract 2026 systematic sample only 3 of 47 (6 percent) do; the norm there is "experiments across 7B/14B/32B models" with no vendor. Conditioning on the artifact-free case raises model-naming from 6 percent to 31 percent.

**No abstract in this corpus defines a metric and gives it a name.** 20 of 32 build an instrument to get the finding, and every one of them leaves it unnamed: "an unnamed benchmark", "a configurable framework", "a simple measure of informativeness", "a new evaluation method". Naming the instrument is what the excluded papers do; `2025.emnlp-main.10` names its Ambiguity Rewrite Metric and `2025.emnlp-main.504` names its Faithfulness by Unlearning Reasoning steps, and both are artifact papers as a result.

## Is coining a phenomenon functionally equivalent to naming a released system?

In the 47-abstract sample the two sparse signals coincide exactly: every abstract carrying a digit also names an artifact, and the 7 naming none carry no digit. If a coined phenomenon were doing the same work as a released name, coiners here would carry digits at a higher rate than non-coiners. They do not.

| Group | n | With a digit | Share | Median /100w | Mean /100w |
|---|---|---|---|---|---|
| all artifact-free | 32 | 8 | 25% | 0.00 | 0.33 |
| names something capitalised | 14 | 6 | 43% | 0.00 | 0.68 |
| names nothing capitalised | 18 | 2 | 11% | 0.00 | 0.07 |
| names at least one model | 10 | 6 | 60% | 1.02 | 0.95 |
| names no model | 22 | 2 | 9% | 0.00 | 0.05 |
| coins its own term | 8 | 1 | 12% | 0.00 | 0.07 |
| coins no term | 24 | 7 | 29% | 0.00 | 0.42 |
| built an unnamed instrument | 20 | 5 | 25% | 0.00 | 0.30 |
| built no instrument | 12 | 3 | 25% | 0.00 | 0.40 |

| | carries a digit | carries no digit |
|---|---|---|
| **coins its own term: yes** | 1 | 7 |
| **coins its own term: no** | 7 | 17 |

**No. Coining a phenomenon runs in the opposite direction from naming a released system.** 1 of 8 coiners carries a digit (12%) against 7 of 24 non-coiners (29%). The single coiner that carries one, `2024.findings-emnlp.841`, reports a standard deviation of detector performance, which is a dispersion figure rather than a result percentage. With 8 coiners this is a direction and not an estimate, but the direction is the opposite of the one the equivalence hypothesis predicts, and the mechanism is visible in the text: a coined term is a claim that a phenomenon exists, and the abstract spends its remaining sentences establishing that it exists rather than measuring how large it is.

**The signal that does co-occur with digits is the model name.** 6 of 10 abstracts naming a model carry a digit (60%), against 2 of 22 that name none (9%), and the median density among model-namers is 1.02 against 0.00. This is not surprising once the numeral roles above are read alongside it: 10 of 16 numerals state the size of what was tested, and stating the size of what was tested is the same sentence in which the models get named. "Through experiments across the Qwen2.5 series (0.5B to 72B)" is one clause carrying both signals.

## The coinage catalogue

Every sentence in which an artifact-free paper names its own coined term for the first time, quoted verbatim from the fetched abstract. Ordered by Anthology ID. 8 of 32 abstracts (25%) coin a term.

**`2024.acl-long.813`**: Can Large Language Models be Good Emotional Supporter? Mitigating Preference Bias on Emotional Support Conversation

Term: **preference bias**. Sentence 7 of 8. Digits in the abstract: 0.

> Our findings emphasize that (1) low preference for specific strategies hinders the progress of emotional support, (2) external assistance helps reduce preference bias, and (3) existing LLMs alone cannot become good emotional supporters.

The coined term is first named only in the enumerated findings sentence, seventh of eight.

**`2024.findings-emnlp.467`**: A Study of Implicit Ranking Unfairness in Large Language Models

Term: **implicit ranking unfairness**. Sentence 3 of 9. Digits in the abstract: 0.

> Worse still, in this paper, we identify a subtler form of discrimination in LLMs, termed implicit ranking unfairness, where LLMs exhibit discriminatory ranking patterns based solely on non-sensitive user profiles, such as user names.

**`2024.findings-emnlp.841`**: How You Prompt Matters! Even Task-Oriented Constraints in Instructions Affect LLM-Generated Text Detection

Term: **task-oriented constraints**. Sentence 4 of 8. Digits in the abstract: 1.

> In this paper, we reveal that even task-oriented constraints — constraints that would naturally be included in an instruction and are not related to detection-evasion — cause existing powerful detectors to have a large variance in detection performance.

**`2025.findings-acl.806`**: Do Large Language Models Have “Emotion Neurons”? Investigating the Existence and Role

Term: **emotion neurons**. Sentence 1 of 7. Digits in the abstract: 0.

> This study comprehensively explores whether there actually exist “emotion neurons” within large language models (LLMs) that selectively process and express certain emotions, and what functional role they play.

**`2026.acl-long.1860`**: Assessing the Belief Consistency of Large Language Models on the Logical Conversation Process

Term: **belief consistency**. Sentence 5 of 8. Digits in the abstract: 0.

> We propose a new evaluation method to assess the consistency of LLMs in a multiple-choice question answering format, designed so that any option chosen is correct, allowing for the evaluation of the proposed belief consistency.

**`2026.acl-long.853`**: Is the Attention Matrix Really the Key to Self-Attention in Multivariate Long-Term Time Series Forecasting?

Term: **multi-branch feature extraction**. Sentence 3 of 5. Digits in the abstract: 0.

> This leads to our central hypothesis: the effectiveness of self-attention in this task stems not from the dynamic attention matrix, but from the multi-branch feature extraction inherent in the parallel projections to Query, Key, and Value matrices and their fusion.

**`2026.acl-short.56`**: Exploring Cross-Client Memorization of Training Data in Large Language Models for Federated Learning

Term: **intra- and inter-client memorization**. Sentence 4 of 6. Digits in the abstract: 0.

> We bridge this gap by proposing a framework that quantifies both intra- and inter-client memorization in FL using fine-grained cross-sample memorization measurement across all clients.

The title's phrasing, cross-client memorization, does not appear in the abstract; the abstract's own term is intra- and inter-client memorization.

**`2026.eacl-long.12`**: Understanding Jailbreak Success: A Study of Latent Space Dynamics in Large Language Models

Term: **jailbreak vector**. Sentence 4 of 7. Digits in the abstract: 0.

> We find that it is possible to extract a jailbreak vector from a single class of jailbreaks that works to mitigate jailbreak effectiveness from other, semantically-dissimilar classes.

One further paper defines a term for the reader without coining it, and is recorded separately for that reason.

**`2025.naacl-long.119`**: Exploring the Cost-Effectiveness of Perspective Taking in Crowdsourcing Subjective Assessment: A Case Study of Toxicity Detection

Term: **perspective taking**, borrowed from social psychology and defined in place.

> In this paper, using toxicity evaluation as an example, we explore the feasibility of using perspective taking—that is, asking annotators to take the point of views of a certain subgroup and estimate opinions within that subgroup—as a way to achieve this objective cost-efficiently.

**All 8 coinages are lower-case noun phrases**, not capitalised names and not acronyms: preference bias, implicit ranking unfairness, task-oriented constraints, "emotion neurons", multi-branch feature extraction, belief consistency, intra- and inter-client memorization, jailbreak vector. None is offered as a thing the reader can download. The construction that recurs is definition by contrast with the expected: a subtler form of discrimination, constraints not related to detection-evasion, consistency evaluated where every option is correct, a vector extracted from one jailbreak class that transfers to another. Position follows function: seven of the eight coinages appear between sentence 1 and sentence 5 of an abstract averaging seven sentences, while `2024.acl-long.813` names its term only in sentence 7, inside the enumerated findings.

## How these abstracts close

| Closing move | Abstracts | Share |
|---|---|---|
| knowledge claim | 19 | 59% |
| call to community | 5 | 16% |
| future work | 4 | 12% |
| contribution restatement | 4 | 12% |
| resource release | 0 | 0% |

**19 of 32 close on a knowledge claim**: the last sentence states what is now known about the object studied. "These results argue against a strictly rule-based encoding of German definite articles" (`2026.acl-long.436`). "Our results indicate that the source of performance in self-attention has been misattributed" (`2026.acl-long.853`). "This suggests that output distributions provide sufficient supervisory signal for syntax acquisition" (`2025.findings-emnlp.801`).

5 close by telling the field what to do, 4 on future work, and 4 by restating the contribution without stating a finding. **None closes on a resource**, which is what the corpus was selected to guarantee, so that row is a check on the selection rather than a result.

## Answer: can a paper with nothing to release carry numbers in its abstract, and what must it name?

**Yes, and a quarter of them do.** The correlation in the 47-abstract sample, where zero abstracts carried a digit without naming an artifact, does not survive conditioning on the artifact-free case across three years. Here 8 of 32 abstracts carry a digit while releasing nothing, and 2 of those 8 name no artifact of any kind: `2024.findings-emnlp.841` reports a standard deviation of 14.4 F1 with nothing capitalised in the abstract but the metric abbreviation, and `2025.findings-emnlp.1380` reports a controlled study with 95 participants the same way. **The constraint is real but it is not a prohibition.**

**What the digit needs is not an artifact but a referent the reader already recognises.** In every one of the 8 digit-carrying abstracts the numeral sits in the same clause as the noun it counts, which is the pattern the 47-abstract corpus found without exception: "a range of 8 audio-classification datasets", "47.8K samples", "18 LLMs", "(n=95)", "10K to 5M sentences", "0.5B to 72B", "200 short videos", "an SD of 14.4 F1-score". An artifact paper supplies that recognition by naming what it built. An artifact-free paper supplies it by naming a model, a dataset or a unit of observation the reader already knows.

**Naming a coined phenomenon is not a substitute for naming a system, and the counts run opposite to that hypothesis.** 12 percent of coiners carry a digit against 29 percent of non-coiners. A coinage buys the abstract something else: it gives the finding a subject that fits in one noun phrase, which is why 5 of the 8 coiners close on a knowledge claim. It does not license a number.

**For a paper reporting a behavioural finding about LLM revision with nothing to release, this corpus supports three moves and declines a fourth.** Name the models the finding is about: 31 percent of these abstracts do, and it is the strongest correlate of a digit here. Carry one or two figures with the counted noun inside the same clause, which is what every digit-carrying abstract in both corpora does. Coin a term for the phenomenon and close on a knowledge claim, which 59 percent of these abstracts do. What the corpus declines is the idea that a coinage substitutes for an artifact in licensing quantification, and it declines a higher numeral count: the maximum density here is 2.72 per 100 words and the mean is 0.33, so a 200-word abstract at this corpus's 90th percentile carries about 2.9 figures, and one at the mean carries under one.

---

Retrieval date for all Anthology pages: 2026-09-06. Sampling seed: 20260906. Sampling and fetch: `scripts/acl2026_abstract_density/05_no_artifact_sample.py`. Extraction and measurement: `06_no_artifact_measure.py`. Hand codes, with the coding rule for each: `handcode_no_artifact.json`. This report: `07_write_no_artifact_report.py`. Abstracts stored verbatim in `acl2026_abstracts.json` under `no_artifact_2024_2026`.
