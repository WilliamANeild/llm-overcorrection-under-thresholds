# How a negative or limiting finding is built, beat by beat: a 53-abstract segmentation

Compiled 2026-09-06. Purpose: give the ARR October 2026 submission a measured template for an abstract whose shape is "undirected revision requests mostly produce nothing, the revisions that occur lower quality more often than they raise it, and a targeted critique reverses this". That is a negative principal finding with a positive counterpart at the end, and the questions that matter are where the counterpart sits, how much room it gets, how the negative is fenced, and whether the venue expects numbers.

## 1. What was fetched, and how the counts were produced

**Sources.** Two corpora, both fetched live on **2026-09-06**.

- **Corpus A**, the segmented corpus: 53 abstracts, retrieved from arXiv. 40 through the arXiv Atom API (`export.arxiv.org/api/query?id_list=`), 23 through the `arxiv.org/abs/` landing pages, from which the abstract was taken verbatim out of the `citation_abstract` meta tag. The API route began returning HTTP 429 partway through the second batch; the landing-page route was used for the remainder and yields the same text. Abstract text is the version of record on arXiv as of the retrieval date; where a paper appeared at an ACL-family or other venue, the venue is recorded from the arXiv comment or journal reference field.
- **Corpus B**, the venue baseline for the digit question: 239 abstracts from the ACL Anthology 2026 volumes, one HTTP request per paper, abstract taken from the `acl-abstract` div. Sampling and extraction are described in section 6.

**How the segmentation was done.** Each abstract was split into sentences by the same script tokenizer used in `acl2026_density.md` (`scripts/acl2026_abstract_density/03_measure.py`), so sentence boundaries are mechanical. Beat labels are **hand-assigned to those script-produced sentences**. Nine labels are used:

| Code | Beat |
|---|---|
| F | field or setup |
| P | prior work |
| G | gap or tension |
| M | method |
| N | the negative finding |
| S | a scope fence on the negative finding |
| C | a positive or constructive counterpart |
| X | mechanism |
| I | implication or close |

A slash (`N/X`) marks one sentence carrying two beats; a plus (`N+C`) marks a sentence in which the negative and its counterpart sit side by side.

**How the quotations were produced.** Every quoted string in sections 4 and 5 was written into a coding file and then **verified by script as an exact substring of the fetched abstract**. All 192 fencing clauses, all negative-finding sentences, all positive-counterpart sentences and all named fixes passed that check with zero mismatches. Word counts of the negative and positive spans use the same tokenizer as the density measure, so the proportions in section 3 are counted, not estimated.

**What is hand-coded, and therefore judgment.** Beat labels; which span counts as the negative finding; which span counts as the positive counterpart; which clauses count as fences; the close beat; whether a fix is named; and the valence coding of Corpus B. The classification of fences into ten types in section 4 is produced by a disclosed regular-expression rule set applied in a fixed order, then read back and hand-checked; the rules are in the working file `fenceclass.py`. Everything else is script output.

**Bounds this survey does not exceed.** Corpus A is a **purposive** corpus, not a random draw: seven anchors were given, and the remaining 46 were assembled by working outward from those anchors through the self-correction, reasoning-limits, planning, evaluation-bias and long-context literatures. It over-represents well-known papers, which is what makes it useful as a template and what makes it unusable as an estimate of how the average negative-results abstract is written. Inclusion required that the paper's **principal reported result** be that models fail, do not improve, are brittle, or that an expected effect is absent. Papers whose principal result is that the authors' own method works, even where the abstract opens on a negative premise, were screened out and are listed in section 7. Only English-language abstracts were read. One anchor, Valmeekam's PlanBench (`2206.10498`), falls outside the stated 2023-2026 window (first posted 2022-06-21) and is excluded; the planning anchor is `2305.15771` instead.

## 2. Corpus A

Ordered by first arXiv submission. `Beats` gives the label of every sentence in order. Density is quantitative numerals per 100 words, counted by the script that excludes model-name digits, four-digit years and enumeration markers.

| # | arXiv ID | Venue | Posted | Title | W | S | Density | Beats |
|---|---|---|---|---|---|---|---|---|
| 1 | `2302.00093` | ICML 2023 | 2023-01-31 | Large Language Models Can Be Easily Distracted by Irrelevant Context | 141 | 6 | 0.00 | `F G M M N C` |
| 2 | `2304.15004` | NeurIPS 2023 | 2023-04-28 | Are Emergent Abilities of Large Language Models a Mirage? | 222 | 6 | 0.00 | `P F N/X X M N/I` |
| 3 | `2305.04388` | NeurIPS 2023 | 2023-05-07 | Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting | 222 | 10 | 0.90 | `F F F N N N N N I I` |
| 4 | `2305.13534` | arXiv (cs.CL) | 2023-05-22 | How Language Model Hallucinations Can Snowball | 114 | 5 | 1.75 | `F G/X M C N/X` |
| 5 | `2305.15771` | NeurIPS 2023 | 2023-05-25 | On the Planning Abilities of Large Language Models : A Critical Investigation | 178 | 6 | 0.56 | `F/M M M N C C` |
| 6 | `2305.17926` | arXiv (cs.CL) | 2023-05-29 | Large Language Models are not Fair Evaluators | 214 | 6 | 2.34 | `N N N C C I` |
| 7 | `2305.18654` | NeurIPS 2023 | 2023-05-29 | Faith and Fate: Limits of Transformers on Compositionality | 165 | 8 | 0.00 | `F G G M M M N/X X` |
| 8 | `2305.19555` | arXiv (cs.CL) | 2023-05-31 | Large Language Models Are Not Strong Abstract Reasoners | 174 | 7 | 0.00 | `F G F G M N C/I` |
| 9 | `2306.05836` | ICLR 2024 | 2023-06-09 | Can Large Language Models Infer Causation from Correlation? | 229 | 10 | 0.44 | `F P/G M M M N S/N I I I` |
| 10 | `2306.08189` | *SEM 2023 | 2023-06-14 | Language models are not naysayers: An analysis of language models on negation benchmarks | 125 | 5 | 0.00 | `P G F/M M N` |
| 11 | `2306.09896` | ICLR 2024 | 2023-06-16 | Is Self-Repair a Silver Bullet for Code Generation? | 189 | 7 | 0.00 | `F P G M N X/C N` |
| 12 | `2307.02477` | NAACL 2024 | 2023-07-05 | Reasoning or Reciting? Exploring the Capabilities and Limitations of Language Models Through Counterfactual Tasks | 130 | 6 | 0.77 | `F G M C+N X I` |
| 13 | `2307.03172` | TACL 2024 | 2023-07-06 | Lost in the Middle: How Language Models Use Long Contexts | 145 | 5 | 0.00 | `G M N N I` |
| 14 | `2308.03762` | arXiv (cs.CL), position paper | 2023-07-21 | GPT-4 Can't Reason | 126 | 4 | 0.79 | `F G/N M N` |
| 15 | `2308.11483` | arXiv (cs.CL) | 2023-08-22 | Large Language Models Sensitivity to The Order of Options in Multiple-Choice Questions | 241 | 10 | 2.49 | `F P G M N X X X C C` |
| 16 | `2309.01809` | ACL 2024 | 2023-09-04 | Are Emergent Abilities in Large Language Models just In-Context Learning? | 181 | 7 | 0.55 | `P P G M N I N/I` |
| 17 | `2309.03882` | ICLR 2024 | 2023-09-07 | Large Language Models Are Not Robust Multiple Choice Selectors | 182 | 7 | 0.55 | `F N X C C C I` |
| 18 | `2309.12288` | ICLR 2024 | 2023-09-21 | The Reversal Curse: LLMs trained on "A is B" fail to learn "B is A" | 252 | 13 | 0.79 | `N N N N N N/X S M/N S M M N I` |
| 19 | `2309.13638` | TMLR 2024 | 2023-09-24 | Embers of Autoregression: Understanding Large Language Models Through the Problem They are Trained to Solve | 266 | 10 | 0.75 | `F X X X X M/N N N I I` |
| 20 | `2309.17012` | ACL 2024 | 2023-09-29 | Benchmarking Cognitive Biases in Large Language Models as Evaluators | 199 | 8 | 1.51 | `N P M M N N I/N I` |
| 21 | `2310.01798` | ICLR 2024 | 2023-10-03 | Large Language Models Cannot Self-Correct Reasoning Yet | 142 | 7 | 0.00 | `F G P M M/S N/S I` |
| 22 | `2310.04815` | arXiv (cs.LG) | 2023-10-07 | Critique Ability of Large Language Models | 270 | 14 | 0.37 | `F F M/F F F M M M N N N N C I` |
| 23 | `2310.08118` | arXiv (cs.AI) | 2023-10-12 | Can Large Language Models Really Improve by Self-critiquing Their Own Plans? | 172 | 7 | 0.00 | `P/G M M M N N I` |
| 24 | `2310.12397` | arXiv (cs.AI) | 2023-10-19 | GPT-4 Doesn't Know It's Wrong: An Analysis of Iterative Prompting for Reasoning Problems | 255 | 9 | 0.00 | `F/G G M M M M N X I` |
| 25 | `2310.13548` | ICLR 2024 | 2023-10-20 | Towards Understanding Sycophancy in Language Models | 164 | 9 | 0.00 | `F G M N M X X X N/X` |
| 26 | `2311.00059` | ICLR 2024 | 2023-10-31 | The Generative AI Paradox: "What It Can Create, It May Not Understand" | 256 | 9 | 0.00 | `F G G X X X M N+C I` |
| 27 | `2311.04076` | TACL 2024 | 2023-11-07 | Do LLMs exhibit human-like response biases? A case study in survey design | 222 | 9 | 0.00 | `F G M M M N N I I` |
| 28 | `2311.08516` | ACL 2024 Findings | 2023-11-14 | LLMs cannot find reasoning errors, but can correct them given the error location | 202 | 8 | 0.50 | `P/G X M/N M C C C I` |
| 29 | `2311.10054` | Findings of EMNLP 2024 | 2023-11-16 | When "A Helpful Assistant" Is Not Really Helpful: Personas in System Prompts Do Not Improve Performances of Large Language Models | 233 | 11 | 2.15 | `F F F G M M N S N/S S/I I` |
| 30 | `2401.00595` | TACL 2024 | 2023-12-31 | State of What Art? A Call for Multi-Prompt LLM Evaluation | 130 | 6 | 3.08 | `F G M/N C C C/I` |
| 31 | `2402.08115` | arXiv (cs.AI) | 2024-02-12 | On the Self-Verification Limitations of Large Language Models on Reasoning and Planning Tasks | 221 | 9 | 0.45 | `F/G G G M M M M N+C C` |
| 32 | `2402.08939` | ICML 2024 | 2024-02-14 | Premise Order Matters in Reasoning with Large Language Models | 165 | 6 | 0.61 | `F N N/X N M/N M/N` |
| 33 | `2402.10669` | EMNLP 2024 | 2024-02-16 | Humans or LLMs as the Judge? A Study on Judgement Biases | 150 | 7 | 0.00 | `F G M M N N I` |
| 34 | `2402.11436` | ACL 2024 | 2024-02-18 | Pride and Prejudice: LLM Amplifies Self-Bias in Self-Refinement | 152 | 8 | 0.00 | `P/G X M M N N/X C I` |
| 35 | `2402.14848` | ACL 2024 | 2024-02-19 | Same Task, More Tokens: the Impact of Input Length on the Reasoning Performance of Large Language Models | 164 | 8 | 0.00 | `F G M M N N/S N I` |
| 36 | `2402.16837` | ACL 2024 | 2024-02-26 | Do Large Language Models Latently Perform Multi-Hop Reasoning? | 232 | 10 | 0.43 | `F/M M M M M C S/N N N I` |
| 37 | `2402.17644` | Findings of ACL 2024 | 2024-02-27 | Are LLMs Capable of Data-based Statistical and Causal Reasoning? Benchmarking Advanced Quantitative Reasoning with Data | 174 | 9 | 2.87 | `F/G M M M M N N N I` |
| 38 | `2404.03602` | COLM 2024 | 2024-04-04 | Evaluating LLMs at Detecting Errors in LLM Responses | 220 | 11 | 2.73 | `F G G M M M N N N N I` |
| 39 | `2404.13076` | COLM 2024 | 2024-04-15 | LLM Evaluators Recognize and Favor Their Own Generations | 165 | 8 | 0.00 | `F G G G M C/N N I` |
| 40 | `2405.00332` | NeurIPS 2024 D&B | 2024-05-01 | A Careful Examination of Large Language Model Performance on Grade School Arithmetic | 203 | 8 | 1.97 | `F G M M M N X S/C` |
| 41 | `2406.01297` | TACL 2024 | 2024-06-03 | When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs | 174 | 7 | 0.00 | `F P G M N C N+C` |
| 42 | `2406.11050` | EMNLP 2024 | 2024-06-16 | A Peek into Token Bias: Large Language Models Are Not Yet Genuine Reasoners | 136 | 7 | 0.00 | `M M M M N S/N I` |
| 43 | `2406.12158` | arXiv (cs.CL) | 2024-06-18 | LLMs Are Prone to Fallacies in Causal Inference | 181 | 6 | 0.00 | `P G G M N C+N` |
| 44 | `2409.12183` | ICLR 2025 | 2024-09-18 | To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning | 190 | 9 | 1.58 | `F G M C+N N M C+N I/C I` |
| 45 | `2409.13373` | arXiv (cs.AI) | 2024-09-20 | LLMs Still Can't Plan; Can LRMs? A Preliminary Evaluation of OpenAI's o1 on PlanBench | 209 | 8 | 0.00 | `F F P N P M C+N I` |
| 46 | `2410.05229` | ICLR 2025 | 2024-10-07 | GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models | 268 | 12 | 0.37 | `F F G M M M N N N X N I` |
| 47 | `2411.15862` | arXiv (cs.CL) | 2024-11-24 | Do LLMs Really Think Step-by-step In Implicit Reasoning? | 157 | 8 | 0.00 | `F P G M M N C N/S` |
| 48 | `2411.17501` | arXiv (cs.LG) | 2024-11-26 | The Limits of Inference Scaling Through Resampling | 182 | 8 | 0.55 | `P P N X X N N N` |
| 49 | `2503.13657` | arXiv (cs.AI) | 2025-03-17 | Why Do Multi-Agent LLM Systems Fail? | 224 | 12 | 2.68 | `N G G M M M M M M M/N I I` |
| 50 | `2505.05410` | arXiv (cs.CL) | 2025-05-08 | Reasoning Models Don't Always Say What They Think | 185 | 5 | 1.62 | `F G M/N S+I I` |
| 51 | `2505.06120` | arXiv (cs.CL) | 2025-05-09 | LLMs Get Lost In Multi-Turn Conversation | 186 | 8 | 1.08 | `F F G M N X X N` |
| 52 | `2506.06941` | NeurIPS 2025 | 2025-06-07 | The Illusion of Thinking: Understanding the Strengths and Limitations of Reasoning Models via the Lens of Problem Complexity | 253 | 11 | 0.00 | `F G G G M M N N N+C N I` |
| 53 | `2506.11930` | arXiv (cs.CL) | 2025-06-13 | Feedback Friction: LLMs Struggle to Fully Incorporate External Feedback | 223 | 10 | 0.00 | `P G G M M M N N X I` |

Venue spread: arXiv (cs.CL) (9), ICLR 2024 (7), ACL 2024 (5), arXiv (cs.AI) (5), NeurIPS 2023 (4), TACL 2024 (4), arXiv (cs.LG) (2), EMNLP 2024 (2), COLM 2024 (2), ICLR 2025 (2), ICML 2023 (1), *SEM 2023 (1), NAACL 2024 (1), arXiv (cs.CL), position paper (1), TMLR 2024 (1), ACL 2024 Findings (1), Findings of EMNLP 2024 (1), ICML 2024 (1), Findings of ACL 2024 (1), NeurIPS 2024 D&B (1), NeurIPS 2025 (1).

Year of first posting: 2023 (30), 2024 (18), 2025 (5).

Median abstract: **185 words, 8 sentences**.

## 3. The beat matrix

Presence of each beat anywhere in the abstract, and where the beat first appears as a fraction of the way through.

| Beat | Abstracts carrying it | Share | Median first position (fraction through) |
|---|---|---|---|
| F (field/setup) | 40/53 | 75% | 0.12 |
| P (prior work) | 17/53 | 32% | 0.20 |
| G (gap/tension) | 39/53 | 74% | 0.25 |
| M (method) | 49/53 | 92% | 0.45 |
| N (negative finding) | 53/53 | 100% | 0.64 |
| S (scope fence) | 10/53 | 19% | 0.74 |
| C (positive counterpart) | 24/53 | 45% | 0.86 |
| X (mechanism) | 20/53 | 38% | 0.55 |
| I (implication/close) | 36/53 | 68% | 1.00 |

Every abstract in the corpus carries a negative-finding beat by construction. What the table shows is what surrounds it: **a gap or tension beat in 39 of 53**, a method beat in 49, a mechanism beat in 20, and an implication beat in 36. The prior-work beat is the one most often skipped: 36 of 53 abstracts name no prior work at all, folding it into the gap sentence instead.

Collapsing repeated adjacent beats, the most common opening runs are:

- `F G M` in 21 abstracts
- `F P G` in 4 abstracts
- `P G M` in 3 abstracts
- `F M N` in 2 abstracts
- `P X M` in 2 abstracts
- `P F N` in 1 abstracts
- `F N I` in 1 abstracts
- `N C I` in 1 abstracts

## 4. The positive counterpart: how many, where, and how much room

A **positive counterpart** is counted when the abstract states, as its own result, that something in the same study does work: a condition, an intervention, a comparison arm, or a remedy the authors ran. A sentence merely proposing future work does not count.

**29 of 53 abstracts (55 percent) carry one.**

| Where the counterpart sits relative to the negative finding | Count |
|---|---|
| After it, in a later sentence | 22 |
| Inside the same sentence | 4 |
| Before it, in an earlier sentence | 3 |

**Proportioning.** Counting the words in the spans quoted verbatim in sections 5 and 8:

| | Median | Mean | Range |
|---|---|---|---|
| Words given to the negative finding | 31 | 32.6 | 7-64 |
| Words given to the positive counterpart | 18 | 22.1 | 7-58 |
| Ratio, counterpart to negative | 0.64 | 0.81 | 0.20-3.86 |

**The counterpart gets about two thirds of the words the negative gets.** Its median share of the combined negative-plus-positive text is **39 percent**. In only 5 of 29 abstracts does the counterpart run longer than the negative finding: `2402.08115` (3.9x), `2311.08516` (2.3x), `2305.15771` (1.7x), `2302.00093` (1.0x), `2307.02477` (1.0x).

Those four ACL-family cases are worth looking at directly, because the shape of the paper going to ARR is theirs: Tyen's `2311.08516` spends one sentence on the failure to find errors and three on what works once the error location is supplied; Valmeekam's `2305.15771` spends one sentence on the 12 percent autonomous success rate and two on the LLM-Modulo setting; `2302.00093` spends one on the distraction effect and one on the mitigations; `2308.11483` spends one on the reordering gap and one on the calibration that closes part of it.

The tightest instance of the shape is `2402.08115`, which puts both halves in a single balanced sentence: "We observe significant performance collapse with self-critique and significant performance gains with sound external verification." Seven words for the failure, eight for the remedy, one main verb.

## 5. How the negative finding is fenced

A **fencing clause** is any span whose work is to restrict the scope, magnitude, or certainty of the negative claim, or to grant an exception to it. **All 53 abstracts carry at least one.** The corpus contains **192 fencing clauses**, a median of **4 per abstract** (mean 3.6, range 1 to 7).

| Fence type | Clauses | Share |
|---|---|---|
| TASK / DOMAIN restriction: where the claim was measured | 43 | 22% |
| FREQUENCY / PREVALENCE hedge | 30 | 16% |
| CONDITION: the negative holds only under a stated condition | 28 | 15% |
| MODEL / SYSTEM restriction: which models the claim covers | 25 | 13% |
| EPISTEMIC hedge: modal or evidential softening | 18 | 9% |
| CONCESSION: a clause granting that something does work | 18 | 9% |
| MAGNITUDE cap: the size of the failure is bounded | 11 | 6% |
| SCOPE-WIDENING: the negative asserted to hold broadly | 7 | 4% |
| EVIDENCE-BASE restriction: how much evidence stands behind it | 6 | 3% |
| COMPARATOR: the negative is stated relative to a named baseline | 6 | 3% |

Two observations from the distribution. First, **the most common fence is not a hedge but a coordinate**: naming the task, the benchmark or the domain the claim was measured on (43 clauses, 22 percent), followed by naming the condition under which the failure occurs (28) and naming which models were covered (25). Taken together those three account for 50 percent of all fencing in the corpus. The negative claim is narrowed by stating where it was measured, not by softening the verb. Second, **7 clauses run the other way**: they widen the claim by asserting it holds across models, settings or dataset versions. Negative-results abstracts fence and un-fence in the same breath, and both moves are load-carrying.

### 5.1 The full catalogue, verbatim, by fence type

Every clause below is an exact substring of the fetched abstract, verified by script.

**TASK / DOMAIN restriction: where the claim was measured** (43)

- `2305.04388` — "on a suite of 13 tasks from BIG-Bench Hard, when testing with GPT-3.5 from OpenAI and Claude 1.0 from Anthropic"
- `2305.15771` — "in commonsense planning tasks"
- `2305.15771` — "across the domains"
- `2305.17926` — "in the evaluation paradigm of adopting large language models~(LLMs), e.g., GPT-4, as a referee to score and compare the quality of responses generated by candidate models"
- `2305.18654` — "across three representative compositional tasks -- multi-digit multiplication, logic grid puzzles, and a classic dynamic programming problem"
- `2305.19555` — "on abstract reasoning tasks"
- `2306.08189` — "several limitations including"
- `2306.09896` — "in many settings"
- `2307.02477` — "Across a suite of 11 tasks"
- `2308.11483` — "on different benchmarks"
- `2308.11483` — "on the task of multiple-choice questions"
- `2309.03882` — "in MCQs"
- `2309.13638` — "in low-probability situations"
- `2310.01798` — "In the context of reasoning,"
- `2310.08118` — "in the context of planning"
- `2310.08118` — "for planning tasks"
- `2310.12397` — "in the context of Graph Coloring"
- `2310.13548` — "across four varied free-form text-generation tasks"
- `2311.00059` — "in measures of understanding"
- `2311.00059` — "across both language and image modalities"
- `2311.08516` — "across our 5 reasoning tasks"
- `2311.08516` — "logical or reasoning errors"
- `2401.00595` — "across 6.5M instances, involving 20 different LLMs and 39 tasks from 3 benchmarks"
- `2401.00595` — "for specific use cases"
- `2402.08115` — "in three domains: Game of 24, Graph Coloring, and STRIPS planning"
- `2402.08115` — "in the context of reasoning and planning"
- `2402.08939` — "in the domain of reasoning tasks"
- `2402.08939` — "in deductive reasoning tasks"
- `2402.08939` — "on a variety of LLMs"
- `2402.10669` — "to various degrees"
- `2402.14848` — "on our reasoning dataset"
- `2402.16837` — "for the prompts of certain relation types"
- `2402.16837` — "on average"
- `2402.17644` — "in data analysis and causal reasoning"
- `2409.12183` — "primarily on tasks involving math or logic"
- `2409.12183` — "On MMLU"
- `2409.13373` — "on this benchmark"
- `2411.15862` — "susceptible to the format of the problem"
- `2411.17501` — "on HumanEval and MBPP, whose unit tests have limited coverage"
- `2503.13657` — "on popular benchmarks"
- `2503.13657` — "across models (GPT4, Claude 3, Qwen2.5, CodeLlama) and tasks (coding, math, general agent)"
- `2505.06120` — "across six generation tasks"
- `2506.06941` — "across scales"

**FREQUENCY / PREVALENCE hedge** (30)

- `2304.15004` — "alleged"
- `2305.04388` — "frequently"
- `2305.13534` — "in some cases"
- `2305.13534` — "often"
- `2306.09896` — "often"
- `2306.09896` — "vary a lot between subsets of the data"
- `2306.09896` — "sometimes"
- `2307.02477` — "often"
- `2307.03172` — "often"
- `2308.03762` — "at present"
- `2309.01809` — "purported"
- `2309.13638` — "In many cases"
- `2310.01798` — "at times"
- `2310.04815` — "for most LLMs"
- `2310.04815` — "often emerges only when models are sufficiently large"
- `2310.04815` — "In particular"
- `2310.04815` — "Models tend to"
- `2310.13548` — "a non-negligible fraction of the time"
- `2310.13548` — "sometimes"
- `2311.04076` — "generally"
- `2311.08516` — "generally"
- `2311.08516` — "often"
- `2311.10054` — "often"
- `2402.08939` — "In particular"
- `2406.01297` — "often"
- `2411.17501` — "often"
- `2503.13657` — "often minimal"
- `2505.05410` — "for most settings and models tested"
- `2505.05410` — "often below 20%"
- `2505.06120` — "often"

**CONDITION: the negative holds only under a stated condition** (28)

- `2302.00093` — "when irrelevant information is included"
- `2304.15004` — "for a particular task and model family, when analyzing fixed model outputs"
- `2305.18654` — "without necessarily"
- `2305.19555` — "even when applying techniques that have been shown to improve performance on other NLP tasks"
- `2306.05836` — "they can only perform causal inference in in-distribution settings when variable names and textual expressions used in the queries are similar to those in the training set"
- `2306.09896` — "when the cost of carrying out repair is taken into account"
- `2308.11483` — "when answer options are reordered"
- `2308.11483` — "even when using demonstrations in a few-shot setting"
- `2309.13638` — "even in deterministic settings where probability should not matter"
- `2310.01798` — "without external feedback"
- `2310.01798` — "based solely on its inherent capabilities, without the crutch of external feedback"
- `2311.04076` — "if at all"
- `2311.08516` — "even in highly objective, unambiguous cases"
- `2401.00595` — "obtained via single-prompt evaluations"
- `2404.13076` — "out of the box"
- `2406.12158` — "if the order is randomized"
- `2409.12183` — "unless the question or model's response contains an equals sign"
- `2410.05229` — "when only the numerical values in the question are altered in the GSM-Symbolic benchmark"
- `2411.15862` — "when prompted"
- `2411.17501` — "when verifiers are imperfect and have a non-zero probability of producing false positives"
- `2505.05410` — "in at least 1% of examples where they use the hint"
- `2505.05410` — "in settings like ours where CoT reasoning is not necessary"
- `2505.05410` — "even without training against a CoT monitor"
- `2506.06941` — "beyond certain complexities"
- `2506.06941` — "up to a point"
- `2506.06941` — "under same inference compute"
- `2506.11930` — "even under these near-ideal conditions"
- `2506.11930` — "high-confidence predictions remain resistant to external correction"

**MODEL / SYSTEM restriction: which models the claim covers** (25)

- `2302.00093` — "cutting-edge prompting techniques"
- `2305.15771` — "with the best model (GPT-4)"
- `2305.19555` — "currently"
- `2306.08189` — "current-generation LLMs"
- `2306.08189` — "with varying model sizes and prompts"
- `2306.09896` — "even for the strongest models"
- `2307.03172` — "current language models"
- `2307.03172` — "even for explicitly long-context models"
- `2309.03882` — "modern LLMs"
- `2309.03882` — "with 20 LLMs on three benchmarks"
- `2309.12288` — "auto-regressive"
- `2310.04815` — "Even top-performing LLMs"
- `2310.08118` — "Using GPT-4, a state-of-the-art LLM, for both generation and verification"
- `2310.12397` — "state of the art"
- `2310.13548` — "five state-of-the-art AI assistants"
- `2311.04076` — "particularly in models that have undergone RLHF"
- `2311.04076` — "of nine models"
- `2402.10669` — "even the cutting-edge judges"
- `2402.17644` — "The strongest model GPT-4"
- `2402.17644` — "Among open-source models"
- `2404.03602` — "Top LLMs like GPT-4 and Claude 3"
- `2406.01297` — "with feedback from prompted LLMs"
- `2406.11050` — "most LLMs"
- `2409.13373` — "current LLMs and new LRMs"
- `2505.06120` — "all the top open- and closed-weight LLMs we test"

**EPISTEMIC hedge: modal or evidential softening** (18)

- `2304.15004` — "may not be"
- `2305.04388` — "can systematically misrepresent"
- `2305.18654` — "suggest"
- `2307.03172` — "can degrade"
- `2309.01809` — "Our findings suggest"
- `2309.03882` — "primarily stems from"
- `2309.17012` — "may still be unable"
- `2310.08118` — "appears to"
- `2310.12397` — "seems to indicate"
- `2310.12397` — "seems largely irrelevant"
- `2310.13548` — "likely driven in part by"
- `2311.00059` — "may not be contingent upon understanding capability"
- `2404.13076` — "straightforward confounders"
- `2405.00332` — "suggesting that some models may have partially memorized GSM8k"
- `2406.11050` — "with statistical guarantee"
- `2406.11050` — "largely depends on"
- `2411.15862` — "suggesting they may just rely on experience rather than strict step-by-step reasoning"
- `2411.17501` — "may have"

**CONCESSION: a clause granting that something does work** (18)

- `2305.04388` — "can be plausible yet misleading"
- `2307.02477` — "while current LMs may possess abstract task-solving skills to an extent"
- `2308.03762` — "despite its occasional flashes of analytical brilliance"
- `2309.12288` — "It is worth noting, however, that if "A is B" appears in-context, models can deduce the reverse relationship."
- `2311.00059` — "although models can outperform humans in generation"
- `2311.04076` — "even if a model shows a significant change in the same direction as humans"
- `2311.10054` — "Nevertheless, further analysis suggests that the gender, type, and domain of the persona can all influence the resulting prediction accuracies."
- `2311.10054` — "while adding a persona may lead to performance gains in certain settings"
- `2402.11436` — "while the self-refine pipeline improves the fluency and understandability of model outputs"
- `2402.14848` — "although at different intensities"
- `2402.16837` — "However, the utilization is highly contextual, varying across different types of prompts."
- `2404.03602` — "sensitive to small changes in prompts but remains challenging to improve"
- `2405.00332` — "Nevertheless, many models, especially those on the frontier, show minimal signs of overfitting"
- `2406.01297` — "except for studies in tasks that are exceptionally suited for self-correction"
- `2406.01297` — "in tasks that can use reliable external feedback"
- `2406.11050` — "While they may perform well on classic problems"
- `2406.12158` — "while LLMs can correctly deduce the absence of causal relations from temporal and spatial relations"
- `2409.13373` — "while o1's performance is a quantum improvement on the benchmark, outpacing the competition"

**MAGNITUDE cap: the size of the failure is bounded** (11)

- `2305.04388` — "by as much as 36%"
- `2305.15771` — "rather limited"
- `2306.05836` — "somewhat mitigated"
- `2306.05836` — "almost close to random"
- `2308.11483` — "approximately 13% to 75%"
- `2402.16837` — "rather moderate and only substantial for the first hop"
- `2404.13076` — "non-trivial accuracy"
- `2405.00332` — "up to 8%"
- `2409.12183` — "almost identical"
- `2410.05229` — "up to 65%"
- `2410.05229` — "noticeable variance"

**SCOPE-WIDENING: the negative asserted to hold broadly** (7)

- `2309.12288` — "The Reversal Curse is robust across model sizes and model families and is not alleviated by data augmentation."
- `2309.17012` — "average of 40% of comparisons across all models"
- `2402.11436` — "in all examined LLMs across multiple languages and tasks"
- `2405.00332` — "with several families of models showing evidence of systematic overfitting across almost all model sizes"
- `2410.05229` — "across all state-of-the-art models"
- `2411.15862` — "in both situations"
- `2411.17501` — "regardless of compute budget"

**EVIDENCE-BASE restriction: how much evidence stands behind it** (6)

- `2305.13534` — "at least one"
- `2306.09896` — "a small-scale study"
- `2308.03762` — "a small collection of 21 diverse reasoning problems"
- `2308.03762` — "detailed qualitative evaluation"
- `2404.03602` — "error detectors based on 12 LLMs"
- `2506.11930` — "models' confidence on specific questions, measured by semantic entropy"

**COMPARATOR: the negative is stated relative to a named baseline** (6)

- `2305.19555` — "in contrast with other natural language tasks"
- `2307.02477` — "compared to the default conditions"
- `2310.08118` — "especially when compared to systems with external, sound verifiers"
- `2311.10054` — "across a range of questions compared to the control setting where no persona is added"
- `2402.08939` — "relative to the original GSM8K benchmark"
- `2402.14848` — "at much shorter input lengths than their technical maximum"

## 6. Do negative-result abstracts carry more digits? No.

The prior note in `acl2026_density.md` put the ACL 2026 venue median at 0.00 quantitative numerals per 100 words on a systematic sample of 47 abstracts, and a 5-paper look at negative-results papers suggested they carry more. That comparison had two problems: five papers is not a sample, and the five were arXiv preprints of analysis papers while the venue baseline was dominated by camera-ready method papers, so valence was confounded with genre, venue and posting route. This section separates them.

### 6.1 A larger venue sample, and a correction to the venue median

A fresh systematic sample was drawn from the same four ACL Anthology 2026 volumes with the same procedure and a new seed (20260907): a random start and a constant stride over each volume's paper list in Anthology order, 100 from `2026.acl-long` (N=2222), 80 from `2026.findings-acl` (N=2163), 40 from `2026.eacl-long` (N=394), 20 from `2026.acl-short` (N=74). 240 IDs drawn, 239 yielded an abstract; `2026.findings-acl.2161` has no abstract block on its landing page and is excluded rather than replaced. **The new sample shares no paper with the earlier 47.** Density is measured by the identical script.

| Sample | n | min | p25 | median | p75 | max | mean | zero-digit |
|---|---|---|---|---|---|---|---|---|
| ACL 2026, prior sample | 47 | 0.00 | 0.00 | **0.00** | 0.64 | 2.93 | 0.48 | 31 (66%) |
| ACL 2026, new sample | 239 | 0.00 | 0.00 | **0.56** | 1.44 | 5.85 | 0.90 | 111 (46%) |
| ACL 2026, both pooled | 286 | 0.00 | 0.00 | **0.49** | 1.36 | 5.85 | 0.83 | 142 (50%) |

**The venue median is not 0.00.** On the larger draw it is 0.56, and on the pooled 286 distinct abstracts it is 0.49. The earlier figure came from a sample in which 31 of 47 abstracts (66 percent) carried no quantitative digit; in the new draw the share is 111 of 239 (46 percent). The two proportions differ by about 2.5 standard errors, which is a large but not impossible sampling swing, and the pooled figure is the one to use: **half of ACL 2026 abstracts carry no quantitative digit, and the median abstract carries about 0.5 numerals per 100 words.** Any calibration built on "the venue median is zero" should be revised.

### 6.2 Valence within the venue, which removes the confound

All 239 new abstracts were valence-coded. A deliberately broad regular-expression screen was run over the results half of each abstract (the sentences from the midpoint on), flagging 128; every flagged abstract was read and adjudicated by hand. The screen's recall was checked against the 47 abstracts whose valence had already been hand-coded: it caught 4 of the 5 negative ones. Because that recall is imperfect, the 111 unflagged abstracts were additionally screened by title, and the 19 whose titles suggested a deficiency finding were read in full; 10 of those proved negative. The remaining 92 unflagged abstracts were treated as positive without being read, which is the one place this coding could still be losing negatives.

Valence rule, applied uniformly: **negative** if the abstract's principal reported result is that models fail, are brittle, do not improve, or that an expected effect is absent; **positive** otherwise, including papers that open on a deficiency and whose principal result is that the authors' remedy works. **44 of 239 abstracts (18 percent) are negative.**

| Group | n | min | p25 | median | p75 | max | mean | zero-digit |
|---|---|---|---|---|---|---|---|---|
| ACL 2026, negative valence | 44 | 0.00 | 0.00 | **0.24** | 1.26 | 5.41 | 0.92 | 22 (50%) |
| ACL 2026, positive valence | 195 | 0.00 | 0.00 | **0.60** | 1.45 | 5.85 | 0.89 | 89 (46%) |
| Corpus A (this survey) | 53 | 0.00 | 0.00 | **0.43** | 0.99 | 3.08 | 0.70 | 24 (45%) |

A two-sided permutation test on the same-venue, same-year comparison, 20,000 relabelings with a fixed seed: the difference in medians is -0.35 (p = 0.29) and the difference in means is 0.02 (p = 0.91). **Within the venue, negative-result abstracts do not carry more digits than positive ones. If anything the median runs the other way.** The share carrying at least one quantitative numeral is 50 percent for negative abstracts and 54 percent for positive ones.

Corpus A sits at a median of 0.43, statistically indistinguishable from both venue groups and from the pooled venue figure of 0.49. **The earlier 5-paper impression was noise.** The practical reading for the ARR abstract is that a negative finding earns no licence to add numbers and incurs no obligation to: one or two figures attached to the principal result is what the venue does, in either valence.

Two bounds on this. The valence coding of Corpus B is a single coder's, unblinded, and the marginal cases (a benchmark paper that reports a deficiency and then a remedy) were decided by whether the results run **leads** with the deficiency. And the 92 unread positive-coded abstracts could contain a few negatives; if they are systematically low-digit, the negative group's median would fall further, which would strengthen rather than weaken the conclusion.

## 7. Where the negative finding sits, how the abstract closes, and whether a fix is named

### 7.1 Negative finding before or after the method sentence

| Position of the principal negative finding | Count | Share |
|---|---|---|
| After the method sentence | 41 | 77% |
| Before any method sentence | 9 | 17% |
| In the same sentence as the method | 3 | 6% |

**77 percent state the method first.** The nine that lead with the finding are `2305.04388`, `2305.17926`, `2309.03882`, `2309.12288`, `2309.17012`, `2402.08939`, `2409.13373`, `2411.17501`, `2503.13657`. They divide into two kinds: papers whose title is already the finding and whose first sentence simply asserts it (`2309.12288` "We expose a surprising failure of generalization"; `2309.17012` "Large Language Models are cognitively biased judges."; `2503.13657`), and papers where the negative is a premise the rest of the abstract explains (`2411.17501`, `2309.03882`). Leading with the finding buys emphasis and costs the reader the setup; every one of the nine has a title that carries the claim on its own, which is what makes the opening survivable.

### 7.2 What the abstract lands on

| Final beat | Count | Share |
|---|---|---|
| an implication, recommendation, or resource release | 30 | 57% |
| the negative finding, restated | 14 | 26% |
| the positive counterpart | 6 | 11% |
| a mechanism | 1 | 2% |
| a scope fence that limits the negative | 1 | 2% |
| a scope fence that doubles as a positive counterpart | 1 | 2% |

**30 of 53 land on an implication**, 14 land back on the negative, and only 6 land on the positive counterpart. Two land on a fence: `2405.00332` closes on "Nevertheless, many models, especially those on the frontier, show minimal signs of overfitting", and `2311.10054` closes on "the effect of each persona can be largely random". Closing on the counterpart is the rarest of the three common options and is what the papers structurally closest to the ARR submission do: `2406.01297`, `2305.15771`, `2402.08115`, `2302.00093`, `2308.11483`, `2401.00595`.

### 7.3 Naming what would fix it

**20 of 53 abstracts (38 percent) name a remedy** rather than gesturing at future work. The remedies cluster tightly. Reliable external feedback or an external verifier: `2406.01297`, `2305.15771`, `2402.08115`, `2310.08118`, `2402.11436`, `2306.09896`. Supplying the model with information it cannot find on its own: `2311.08516` (ground-truth error location), `2411.15862` (training rather than prompting). A calibration or debiasing procedure: `2305.17926`, `2309.03882`, `2308.11483`. A change in evaluation practice: `2304.15004`, `2401.00595`, `2305.04388`. Applying the technique selectively rather than by default: `2409.12183`.

Named fixes, verbatim:

- `2302.00093` — "decoding with self-consistency and adding to the prompt an instruction that tells the language model to ignore the irrelevant information"
- `2304.15004` — "linear or continuous metrics produce smooth, continuous predictable changes in model performance"
- `2305.04388` — "Building more transparent and explainable systems will require either improving CoT faithfulness through targeted efforts or abandoning CoT in favor of alternative methods."
- `2305.15771` — "external verifiers can help provide feedback on the generated plans and back-prompt the LLM for better plan generation"
- `2305.17926` — "we propose a calibration framework with three simple yet effective strategies"
- `2305.19555` — "guiding LLM generation to follow causal paths could help improve the generalisation and reasoning abilities of LLMs"
- `2306.09896` — "using a stronger model to artificially boost the quality of the feedback"
- `2308.11483` — "two approaches to calibrate LLMs' predictions"
- `2309.03882` — "a label-free, inference-time debiasing method, called PriDe"
- `2310.04815` — "a simple yet effective baseline named self-check"
- `2310.08118` — "systems with external, sound verifiers"
- `2311.08516` — "a backtracking setup that feeds ground truth mistake location information to the model"
- `2401.00595` — "to evaluate LLMs with a set of diverse prompts instead"
- `2402.08115` — "sound external verification"
- `2402.11436` — "larger model size and external feedback with accurate assessment"
- `2406.01297` — "reliable external feedback"
- `2409.12183` — "CoT can be applied selectively"
- `2411.15862` — "But when trained, they indeed calculate intermediate steps."
- `2503.13657` — "demonstrating improvement headrooms from better MAS design"
- `2506.11930` — "sampling-based strategies like progressive temperature increases and explicit rejection of previously attempted incorrect answers"

## 8. The negative findings, verbatim

Every sentence or clause below is the span coded as the paper's negative finding, quoted exactly. Ordered by first posting so the constructions can be read against each other and against the year.

**`2302.00093`** — Large Language Models Can Be Easily Distracted by Irrelevant Context (ICML 2023, 2023-01-31)

> We use this benchmark to measure the distractibility of cutting-edge prompting techniques for large language models, and find that the model performance is dramatically decreased when irrelevant information is included.

**`2304.15004`** — Are Emergent Abilities of Large Language Models a Mirage? (NeurIPS 2023, 2023-04-28)

> Via all three analyses, we provide evidence that alleged emergent abilities evaporate with different metrics or with better statistics, and may not be a fundamental property of scaling AI models.

**`2305.04388`** — Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting (NeurIPS 2023, 2023-05-07)

> However, we find that CoT explanations can systematically misrepresent the true reason for a model's prediction.

**`2305.13534`** — How Language Model Hallucinations Can Snowball (arXiv (cs.CL), 2023-05-22)

> We refer to this phenomenon as hallucination snowballing: an LM over-commits to early mistakes, leading to more mistakes that it otherwise would not make.

**`2305.15771`** — On the Planning Abilities of Large Language Models : A Critical Investigation (NeurIPS 2023, 2023-05-25)

> Our findings reveal that LLMs' ability to generate executable plans autonomously is rather limited, with the best model (GPT-4) having an average success rate of ~12% across the domains.

**`2305.17926`** — Large Language Models are not Fair Evaluators (arXiv (cs.CL), 2023-05-29)

> In this paper, we uncover a systematic bias in the evaluation paradigm of adopting large language models~(LLMs), e.g., GPT-4, as a referee to score and compare the quality of responses generated by candidate models.

> We find that the quality ranking of candidate responses can be easily hacked by simply altering their order of appearance in the context.

**`2305.18654`** — Faith and Fate: Limits of Transformers on Compositionality (NeurIPS 2023, 2023-05-29)

> Our empirical findings suggest that transformer LLMs solve compositional tasks by reducing multi-step compositional reasoning into linearized subgraph matching, without necessarily developing systematic problem-solving skills.

**`2305.19555`** — Large Language Models Are Not Strong Abstract Reasoners (arXiv (cs.CL), 2023-05-31)

> We perform extensive evaluations of state-of-the-art LLMs, showing that they currently achieve very limited performance in contrast with other natural language tasks, even when applying techniques that have been shown to improve performance on other NLP tasks.

**`2306.05836`** — Can Large Language Models Infer Causation from Correlation? (ICLR 2024, 2023-06-09)

> Through our experiments, we identify a key shortcoming of LLMs in terms of their causal inference skills, and show that these models achieve almost close to random performance on the task.

**`2306.08189`** — Language models are not naysayers: An analysis of language models on negation benchmarks (*SEM 2023, 2023-06-14)

> Through systematic experimentation with varying model sizes and prompts, we show that LLMs have several limitations including insensitivity to the presence of negation, an inability to capture the lexical semantics of negation, and a failure to reason under negation.

**`2306.09896`** — Is Self-Repair a Silver Bullet for Code Generation? (ICLR 2024, 2023-06-16)

> We find that when the cost of carrying out repair is taken into account, performance gains are often modest, vary a lot between subsets of the data, and are sometimes not present at all.

**`2307.02477`** — Reasoning or Reciting? Exploring the Capabilities and Limitations of Language Models Through Counterfactual Tasks (NAACL 2024, 2023-07-05)

> but nevertheless find that performance substantially and consistently degrades compared to the default conditions

**`2307.03172`** — Lost in the Middle: How Language Models Use Long Contexts (TACL 2024, 2023-07-06)

> We find that performance can degrade significantly when changing the position of relevant information, indicating that current language models do not robustly make use of information in long input contexts.

**`2308.03762`** — GPT-4 Can't Reason (arXiv (cs.CL), position paper, 2023-07-21)

> Based on this analysis, the paper concludes that, despite its occasional flashes of analytical brilliance, GPT-4 at present is utterly incapable of reasoning.

**`2308.11483`** — Large Language Models Sensitivity to The Order of Options in Multiple-Choice Questions (arXiv (cs.CL), 2023-08-22)

> Investigating the sensitivity of LLMs towards the order of options in multiple-choice questions, we demonstrate a considerable performance gap of approximately 13% to 75% in LLMs on different benchmarks, when answer options are reordered, even when using demonstrations in a few-shot setting.

**`2309.01809`** — Are Emergent Abilities in Large Language Models just In-Context Learning? (ACL 2024, 2023-09-04)

> Our findings suggest that purported emergent abilities are not truly emergent, but result from a combination of in-context learning, model memory, and linguistic knowledge.

**`2309.03882`** — Large Language Models Are Not Robust Multiple Choice Selectors (ICLR 2024, 2023-09-07)

> This work shows that modern LLMs are vulnerable to option position changes in MCQs due to their inherent "selection bias", namely, they prefer to select specific option IDs as answers (like "Option A").

**`2309.12288`** — The Reversal Curse: LLMs trained on "A is B" fail to learn "B is A" (ICLR 2024, 2023-09-21)

> We expose a surprising failure of generalization in auto-regressive large language models (LLMs).

> If a model is trained on a sentence of the form "A is B", it will not automatically generalize to the reverse direction "B is A".

> Thus, models do not generalize a prevalent pattern in their training set: if "A is B" occurs, "B is A" is more likely to occur.

**`2309.13638`** — Embers of Autoregression: Understanding Large Language Models Through the Problem They are Trained to Solve (TMLR 2024, 2023-09-24)

> In many cases, the experiments reveal surprising failure modes.

**`2309.17012`** — Benchmarking Cognitive Biases in Large Language Models as Evaluators (ACL 2024, 2023-09-29)

> Large Language Models are cognitively biased judges.

> We find that LLMs are biased text quality evaluators, exhibiting strong indications on our bias benchmark (average of 40% of comparisons across all models) within each of their evaluations that question their robustness as evaluators.

**`2310.01798`** — Large Language Models Cannot Self-Correct Reasoning Yet (ICLR 2024, 2023-10-03)

> In the context of reasoning, our research indicates that LLMs struggle to self-correct their responses without external feedback, and at times, their performance even degrades after self-correction.

**`2310.04815`** — Critique Ability of Large Language Models (arXiv (cs.LG), 2023-10-07)

> Critique is generally challenging for most LLMs, and this capability often emerges only when models are sufficiently large.

> In particular, self-critique is especially difficult.

**`2310.08118`** — Can Large Language Models Really Improve by Self-critiquing Their Own Plans? (arXiv (cs.AI), 2023-10-12)

> Using GPT-4, a state-of-the-art LLM, for both generation and verification, our findings reveal that self-critiquing appears to diminish plan generation performance, especially when compared to systems with external, sound verifiers and the LLM verifiers in that system produce a notable number of false positives, compromising the system's reliability.

> Additionally, the nature of feedback, whether binary or detailed, showed minimal impact on plan generation.

**`2310.12397`** — GPT-4 Doesn't Know It's Wrong: An Analysis of Iterative Prompting for Reasoning Problems (arXiv (cs.AI), 2023-10-19)

> The study seems to indicate that (i) LLMs are bad at solving graph coloring instances (ii) they are no better at verifying a solution--and thus are not effective in iterative modes with LLMs critiquing LLM-generated solutions (iii) the correctness and content of the criticisms--whether by LLMs or external solvers--seems largely irrelevant to the performance of iterative prompting.

**`2310.13548`** — Towards Understanding Sycophancy in Language Models (ICLR 2024, 2023-10-20)

> We first demonstrate that five state-of-the-art AI assistants consistently exhibit sycophancy across four varied free-form text-generation tasks.

**`2311.00059`** — The Generative AI Paradox: "What It Can Create, It May Not Understand" (ICLR 2024, 2023-10-31)

> they consistently fall short of human capabilities in measures of understanding, as well as weaker correlation between generation and understanding performance, and more brittleness to adversarial inputs

**`2311.04076`** — Do LLMs exhibit human-like response biases? A case study in survey design (TACL 2024, 2023-11-07)

> Our comprehensive evaluation of nine models shows that popular open and commercial LLMs generally fail to reflect human-like behavior, particularly in models that have undergone RLHF.

**`2311.08516`** — LLMs cannot find reasoning errors, but can correct them given the error location (ACL 2024 Findings, 2023-11-14)

> Firstly, we benchmark several state-of-the-art LLMs on their mistake-finding ability and demonstrate that they generally struggle with the task, even in highly objective, unambiguous cases.

**`2311.10054`** — When "A Helpful Assistant" Is Not Really Helpful: Personas in System Prompts Do Not Improve Performances of Large Language Models (Findings of EMNLP 2024, 2023-11-16)

> Through extensive analysis of 4 popular families of LLMs and 2,410 factual questions, we demonstrate that adding personas in system prompts does not improve model performance across a range of questions compared to the control setting where no persona is added.

**`2401.00595`** — State of What Art? A Call for Multi-Prompt LLM Evaluation (TACL 2024, 2023-12-31)

> In this paper, we comprehensively analyze the brittleness of results obtained via single-prompt evaluations across 6.5M instances, involving 20 different LLMs and 39 tasks from 3 benchmarks.

**`2402.08115`** — On the Self-Verification Limitations of Large Language Models on Reasoning and Planning Tasks (arXiv (cs.AI), 2024-02-12)

> We observe significant performance collapse with self-critique

**`2402.08939`** — Premise Order Matters in Reasoning with Large Language Models (ICML 2024, 2024-02-14)

> However, in the domain of reasoning tasks, we discover a frailty: LLMs are surprisingly brittle to the ordering of the premises, despite the fact that such ordering does not alter the underlying task.

**`2402.10669`** — Humans or LLMs as the Judge? A Study on Judgement Biases (EMNLP 2024, 2024-02-16)

> Results show that human and LLM judges are vulnerable to perturbations to various degrees, and that even the cutting-edge judges possess considerable biases.

**`2402.11436`** — Pride and Prejudice: LLM Amplifies Self-Bias in Self-Refinement (ACL 2024, 2024-02-18)

> We find that self-bias is prevalent in all examined LLMs across multiple languages and tasks.

> Our analysis reveals that while the self-refine pipeline improves the fluency and understandability of model outputs, it further amplifies self-bias.

**`2402.14848`** — Same Task, More Tokens: the Impact of Input Length on the Reasoning Performance of Large Language Models (ACL 2024, 2024-02-19)

> Our findings show a notable degradation in LLMs' reasoning performance at much shorter input lengths than their technical maximum.

**`2402.16837`** — Do Large Language Models Latently Perform Multi-Hop Reasoning? (ACL 2024, 2024-02-26)

> However, the utilization is highly contextual, varying across different types of prompts.

> Also, on average, the evidence for the second hop and the full multi-hop traversal is rather moderate and only substantial for the first hop.

**`2402.17644`** — Are LLMs Capable of Data-based Statistical and Causal Reasoning? Benchmarking Advanced Quantitative Reasoning with Data (Findings of ACL 2024, 2024-02-27)

> The strongest model GPT-4 achieves an accuracy of 58%, which has much room for improvement.

> Analysis reveals that models encounter difficulties in data analysis and causal reasoning, and struggle in using causal knowledge and provided data simultaneously.

**`2404.03602`** — Evaluating LLMs at Detecting Errors in LLM Responses (COLM 2024, 2024-04-04)

> Our findings show: 1) Top LLMs like GPT-4 and Claude 3 detect errors made by LLMs at very low recall, and all LLM-based error detectors perform much worse than humans.

> 4) Popular approaches to improving LLMs, including self-consistency and majority vote, do not improve the error detection performance.

**`2404.13076`** — LLM Evaluators Recognize and Favor Their Own Generations (COLM 2024, 2024-04-15)

> By fine-tuning LLMs, we discover a linear correlation between self-recognition capability and the strength of self-preference bias; using controlled experiments, we show that the causal explanation resists straightforward confounders.

**`2405.00332`** — A Careful Examination of Large Language Model Performance on Grade School Arithmetic (NeurIPS 2024 D&B, 2024-05-01)

> When evaluating leading open- and closed-source LLMs on GSM1k, we observe accuracy drops of up to 8%, with several families of models showing evidence of systematic overfitting across almost all model sizes.

**`2406.01297`** — When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs (TACL 2024, 2024-06-03)

> We first find that prior studies often do not define their research questions in detail and involve impractical frameworks or unfair evaluations that over-evaluate self-correction.

> no prior work demonstrates successful self-correction with feedback from prompted LLMs, except for studies in tasks that are exceptionally suited for self-correction

**`2406.11050`** — A Peek into Token Bias: Large Language Models Are Not Yet Genuine Reasoners (EMNLP 2024, 2024-06-16)

> The findings in this study suggest, with statistical guarantee, that most LLMs still struggle with logical reasoning.

**`2406.12158`** — LLMs Are Prone to Fallacies in Causal Inference (arXiv (cs.CL), 2024-06-18)

> We find that: (a) LLMs are susceptible to inferring causal relations from the order of two entity mentions in text (e.g. X mentioned before Y implies X causes Y); (b) if the order is randomized, LLMs still suffer from the post hoc fallacy, i.e. X occurs before Y (temporal relation) implies X causes Y.

**`2409.12183`** — To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning (ICLR 2025, 2024-09-18)

> with much smaller gains on other types of tasks

> On MMLU, directly generating the answer without CoT leads to almost identical accuracy as CoT unless the question or model's response contains an equals sign, indicating symbolic operations and reasoning.

> but it underperforms relative to using a symbolic solver

**`2409.13373`** — LLMs Still Can't Plan; Can LRMs? A Preliminary Evaluation of OpenAI's o1 on PlanBench (arXiv (cs.AI), 2024-09-20)

> Despite the slew of new private and open source LLMs since GPT3, progress on this benchmark has been surprisingly slow.

> it is still far from saturating it

**`2410.05229`** — GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models (ICLR 2025, 2024-10-07)

> Our findings reveal that LLMs exhibit noticeable variance when responding to different instantiations of the same question.

> Specifically, the performance of all models declines when only the numerical values in the question are altered in the GSM-Symbolic benchmark.

> Furthermore, we investigate the fragility of mathematical reasoning in these models and show that their performance significantly deteriorates as the number of clauses in a question increases.

**`2411.15862`** — Do LLMs Really Think Step-by-step In Implicit Reasoning? (arXiv (cs.CL), 2024-11-24)

> The results surprisingly indicate that when prompted, LLMs hardly think about intermediate steps, suggesting they may just rely on experience rather than strict step-by-step reasoning.

**`2411.17501`** — The Limits of Inference Scaling Through Resampling (arXiv (cs.LG), 2024-11-26)

> However, we show that this approach is fundamentally limited when verifiers are imperfect and have a non-zero probability of producing false positives.

**`2503.13657`** — Why Do Multi-Agent LLM Systems Fail? (arXiv (cs.AI), 2025-03-17)

> Despite enthusiasm for Multi-Agent LLM Systems (MAS), their performance gains on popular benchmarks are often minimal.

**`2505.05410`** — Reasoning Models Don't Always Say What They Think (arXiv (cs.CL), 2025-05-08)

> for most settings and models tested, CoTs reveal their usage of hints in at least 1% of examples where they use the hint, but the reveal rate is often below 20%

**`2505.06120`** — LLMs Get Lost In Multi-Turn Conversation (arXiv (cs.CL), 2025-05-09)

> Our experiments confirm that all the top open- and closed-weight LLMs we test exhibit significantly lower performance in multi-turn conversations than single-turn, with an average drop of 39% across six generation tasks.

**`2506.06941`** — The Illusion of Thinking: Understanding the Strengths and Limitations of Reasoning Models via the Lens of Problem Complexity (NeurIPS 2025, 2025-06-07)

> Through extensive experiments, we show that LRMs face a complete accuracy collapse beyond certain complexities.

> We found that LRMs have limitations in exact computation: they fail to use explicit algorithms and reason inconsistently across scales.

**`2506.11930`** — Feedback Friction: LLMs Struggle to Fully Incorporate External Feedback (arXiv (cs.CL), 2025-06-13)

> Surprisingly, even under these near-ideal conditions, solver models consistently show resistance to feedback, a limitation that we term Feedback Friction.

### 8.1 What the constructions have in common

Reading the 70 spans together, four grammatical patterns account for nearly all of them.

- **Attributed finding.** "We find that", "Our findings reveal that", "Our results show that", "Our experiments confirm that", "we demonstrate that", "The findings in this study suggest". The claim is grammatically the authors' observation, not a property of the world. This is the default and it is nearly universal.
- **Negated capability with a named limit.** "LLMs struggle to self-correct their responses without external feedback"; "they generally struggle with the task, even in highly objective, unambiguous cases"; "popular open and commercial LLMs generally fail to reflect human-like behavior, particularly in models that have undergone RLHF". The fence is welded into the same clause as the verb, which is what keeps the sentence from reading as an overclaim.
- **Direction of change rather than level.** "performance even degrades after self-correction"; "a notable degradation in LLMs' reasoning performance"; "significantly lower performance in multi-turn conversations than single-turn"; "accuracy drops of up to 8%". Stating a change against a stated comparator is the commonest way the corpus quantifies a failure, and it is the construction the ARR paper's central result already has.
- **Null stated as a comparison to a control.** Only three abstracts state a genuine null, and all three name the control explicitly: `2311.10054` ("does not improve model performance across a range of questions compared to the control setting where no persona is added"), `2404.03602` ("do not improve the error detection performance"), `2310.08118` ("showed minimal impact on plan generation"). None of the three writes "no effect"; all three write "does not improve X relative to Y".

The construction the corpus avoids is the bare universal. Only `2308.03762` writes one ("GPT-4 at present is utterly incapable of reasoning"), and it is a position paper that spends its preceding clause conceding "its occasional flashes of analytical brilliance" and its temporal fence "at present".

## 9. The positive counterparts, verbatim

The 29 spans coded as a positive counterpart.

**`2302.00093`** — Large Language Models Can Be Easily Distracted by Irrelevant Context

> We also identify several approaches for mitigating this deficiency, such as decoding with self-consistency and adding to the prompt an instruction that tells the language model to ignore the irrelevant information.

**`2305.13534`** — How Language Model Hallucinations Can Snowball

> Crucially, we find that ChatGPT and GPT-4 can identify 67% and 87% of their own mistakes, respectively.

**`2305.15771`** — On the Planning Abilities of Large Language Models : A Critical Investigation

> However, the results in the LLM-Modulo setting show more promise.

> In the LLM-Modulo setting, we demonstrate that LLM-generated plans can improve the search process for underlying sound planners and additionally show that external verifiers can help provide feedback on the generated plans and back-prompt the LLM for better plan generation.

**`2305.17926`** — Large Language Models are not Fair Evaluators

> We also manually annotate the "win/tie/lose" outcomes of responses from ChatGPT and Vicuna-13B in the Vicuna Benchmark's question prompt, and extensive experiments demonstrate that our approach successfully mitigates evaluation bias, resulting in closer alignment with human judgments.

**`2306.05836`** — Can Large Language Models Infer Causation from Correlation?

> This shortcoming is somewhat mitigated when we try to re-purpose LLMs for this skill via finetuning

**`2306.09896`** — Is Self-Repair a Silver Bullet for Code Generation?

> using a stronger model to artificially boost the quality of the feedback, we observe substantially larger performance gains

**`2307.02477`** — Reasoning or Reciting? Exploring the Capabilities and Limitations of Language Models Through Counterfactual Tasks

> Across a suite of 11 tasks, we observe nontrivial performance on the counterfactual variants

**`2308.11483`** — Large Language Models Sensitivity to The Order of Options in Multiple-Choice Questions

> To validate our conjecture, we conduct various experiments and adopt two approaches to calibrate LLMs' predictions, leading to up to 8 percentage points improvement across different models and benchmarks.

**`2309.03882`** — Large Language Models Are Not Robust Multiple Choice Selectors

> We demonstrate that it achieves interpretable and transferable debiasing with high computational efficiency.

**`2309.12288`** — The Reversal Curse: LLMs trained on "A is B" fail to learn "B is A"

> It is worth noting, however, that if "A is B" appears in-context, models can deduce the reverse relationship.

**`2310.04815`** — Critique Ability of Large Language Models

> To this end, we introduce a simple yet effective baseline named self-check, which leverages self-critique to improve task performance for various models.

**`2311.00059`** — The Generative AI Paradox: "What It Can Create, It May Not Understand"

> although models can outperform humans in generation

**`2311.08516`** — LLMs cannot find reasoning errors, but can correct them given the error location

> We show that this boosts downstream task performance across our 5 reasoning tasks, indicating that LLMs' correction abilities are robust.

> Finally, we show that it is possible to obtain mistake location information without ground truth labels or in-domain training data.

> We train a small classifier with out-of-domain data, which exhibits stronger mistake-finding performance than prompting a large model.

**`2311.10054`** — When "A Helpful Assistant" Is Not Really Helpful: Personas in System Prompts Do Not Improve Performances of Large Language Models

> while aggregating results from the best persona for each question significantly improves prediction accuracy

**`2401.00595`** — State of What Art? A Call for Multi-Prompt LLM Evaluation

> To improve robustness of the analysis, we propose to evaluate LLMs with a set of diverse prompts instead.

**`2402.08115`** — On the Self-Verification Limitations of Large Language Models on Reasoning and Planning Tasks

> and significant performance gains with sound external verification

> We also note that merely re-prompting with a sound verifier maintains most of the benefits of more involved setups.

**`2402.11436`** — Pride and Prejudice: LLM Amplifies Self-Bias in Self-Refinement

> To mitigate such biases, we discover that larger model size and external feedback with accurate assessment can significantly reduce bias in the self-refine pipeline, leading to actual performance improvement in downstream tasks.

**`2402.16837`** — Do Large Language Models Latently Perform Multi-Hop Reasoning?

> We find strong evidence of latent multi-hop reasoning for the prompts of certain relation types, with the reasoning pathway used in more than 80% of the prompts.

**`2404.13076`** — LLM Evaluators Recognize and Favor Their Own Generations

> We discover that, out of the box, LLMs such as GPT-4 and Llama 2 have non-trivial accuracy at distinguishing themselves from other LLMs and humans.

**`2405.00332`** — A Careful Examination of Large Language Model Performance on Grade School Arithmetic

> Nevertheless, many models, especially those on the frontier, show minimal signs of overfitting, and all models broadly demonstrate generalization to novel math problems guaranteed to not be in their training data.

**`2406.01297`** — When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs

> self-correction works well in tasks that can use reliable external feedback, and (3) large-scale fine-tuning enables self-correction

**`2406.11050`** — A Peek into Token Bias: Large Language Models Are Not Yet Genuine Reasoners

> While they may perform well on classic problems

**`2406.12158`** — LLMs Are Prone to Fallacies in Causal Inference

> while LLMs can correctly deduce the absence of causal relations from temporal and spatial relations

**`2409.12183`** — To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning

> Our results show that CoT gives strong performance benefits primarily on tasks involving math or logic

> Much of CoT's gain comes from improving symbolic execution

> Our results indicate that CoT can be applied selectively, maintaining performance while saving inference costs.

**`2409.13373`** — LLMs Still Can't Plan; Can LRMs? A Preliminary Evaluation of OpenAI's o1 on PlanBench

> while o1's performance is a quantum improvement on the benchmark, outpacing the competition

**`2411.15862`** — Do LLMs Really Think Step-by-step In Implicit Reasoning?

> But when trained, they indeed calculate intermediate steps.

**`2505.05410`** — Reasoning Models Don't Always Say What They Think

> These results suggest that CoT monitoring is a promising way of noticing undesired behaviors during training and evaluations

**`2506.06941`** — The Illusion of Thinking: Understanding the Strengths and Limitations of Reasoning Models via the Lens of Problem Complexity

> (2) medium-complexity tasks where LRMs demonstrates advantage

**`2506.11930`** — Feedback Friction: LLMs Struggle to Fully Incorporate External Feedback

> which yield improvements but still fail to help models achieve target performance

## 10. Papers screened out, and why

Recording these keeps the inclusion rule auditable and gives a second, contrasting shape to compare against.

**Outside the date window.** `2206.10498` (PlanBench, first posted 2022-06-21) despite being the Valmeekam planning anchor; `2305.15771` is used in its place.

**Fetched, read, and screened out because the principal reported result is that the authors' method works.** These are the mirror image of the target shape: a negative premise in the setup, a positive result. They are worth reading precisely because the ARR paper must not be mistaken for one of them.

| arXiv ID | Title | Why excluded |
|---|---|---|
| `2401.02009` | Self-Contrast: Better Reflection Through Inconsistent Solving Perspectives (ACL 2024) | Negative premise (intrinsic reflection is unstable) but the reported result is that the proposed method works |
| `2311.07961` | The ART of LLM Refinement: Ask, Refine, and Trust | Negative premise, result is a +5 point gain from the authors' method |
| `2402.12563` | Confidence Matters: Revisiting Intrinsic Self-Correction Capabilities of LLMs | Result is that the authors' If-or-Else prompt improves self-correction |
| `2404.17140` | Small Language Models Need Strong Verifiers to Self-Correct Reasoning (Findings of ACL 2024) | Result is improved self-correction from the authors' pipeline, with limitations noted last |
| `2406.02378` | On the Intrinsic Self-Correction Capability of LLMs | Result is that intrinsic self-correction converges to improved performance |
| `2412.02674` | Mind the Gap: Examining the Self-Improvement Capabilities of LLMs (ICLR 2025) | Principal result is a scaling regularity, not a deficiency |
| `2406.10400` | Self-Reflection Makes Large Language Models Safer, Less Biased, and Ideologically Neutral | Carries both halves but the principal claim is the positive one |
| `2305.18153` | Do Large Language Models Know What They Don't Know? (Findings of ACL 2023) | Principal result is that self-knowledge is present; the limitation is the closing beat only |
| `2310.09820` | Assessing the Reliability of Large Language Model Knowledge | Principal result is that the authors' metric works |

**Access failures.** One. The arXiv Atom API returned HTTP 429 during the second fetch batch and did not recover; those 23 abstracts were taken from the `arxiv.org/abs/` landing pages instead and every one was obtained. No abstract in Corpus A is missing or paraphrased. In Corpus B, one of 240 sampled Anthology pages (`2026.findings-acl.2161`) serves no abstract block and was dropped.

## 11. The beat order and proportioning that fits "undirected fails, directed works"

### 11.1 The eight closest structural analogues

Twenty-nine abstracts carry a positive counterpart, but most pair a deficiency in the models with a remedy the authors built. The submission's shape is narrower: **two conditions, both run inside the same study, one of which fails and one of which works**. Eight abstracts in the corpus have exactly that.

| arXiv ID | The contrast | W | S | Neg words | Pos words | Pos/neg | Neg at sentence | Pos at sentence | Lands on |
|---|---|---|---|---|---|---|---|---|---|
| `2311.08516` | unprompted error-finding fails / correction works once the location is supplied | 202 | 8 | 25 | 58 | 2.32 | 3/8 | 5/8 | an implication |
| `2305.15771` | autonomous planning fails / LLM-Modulo with an external verifier works | 178 | 6 | 29 | 50 | 1.72 | 4/6 | 5/6 | the positive |
| `2402.08115` | self-critique collapses / sound external verification gains | 221 | 9 | 7 | 27 | 3.86 | 8/9 | 8/9 | the positive |
| `2411.15862` | prompted implicit reasoning absent / trained implicit reasoning present | 157 | 8 | 25 | 8 | 0.32 | 6/8 | 7/8 | the negative |
| `2409.12183` | CoT gives little outside math and logic / large gains inside them | 190 | 9 | 48 | 40 | 0.83 | 4/9 | 4/9 | an implication |
| `2302.00093` | irrelevant context degrades accuracy / two named mitigations recover it | 141 | 6 | 30 | 31 | 1.03 | 5/6 | 6/6 | the positive |
| `2306.09896` | self-repair gains are modest / stronger feedback produces large gains | 189 | 7 | 34 | 18 | 0.53 | 5/7 | 6/7 | the negative |
| `2406.01297` | no success with feedback from prompted LLMs / success with reliable external feedback and with fine-tuning | 174 | 7 | 47 | 17 | 0.36 | 5/7 | 7/7 | the positive |

Their medians: **183 words, 7 sentences, 29 words on the failure, 29 on the counterpart** (ratio 0.93), the negative landing about 71 percent of the way through and the counterpart about 87 percent, **4 fencing clauses**, and a digit density of 0.23 per 100 words.

Note the difference from the corpus as a whole: in the full 53 the counterpart runs at 0.64 of the negative, but **in these eight it runs at parity**. When the contrast is between two conditions the authors ran, rather than between a model deficiency and an authors' fix, the two arms get roughly equal room. That is the proportioning the ARR abstract should use.

### 11.2 The order these eight converge on

Collapsing their beat sequences, seven of the eight follow the same order, and the one exception (`2402.08115`) differs only by fusing the two result beats into one sentence:

```
F/P  ->  G  ->  M  ->  N (+ its fences)  ->  C  ->  close
```
- **F/P, one to two sentences.** What the practice is and that it is widely used. Six of the eight open by naming the technique, not by naming the models.
- **G, one sentence.** The tension: it is not known when the technique helps, or the evidence is mixed. Present in 44 of the 53.
- **M, one to three sentences.** What was run, and in these eight the method sentence does specific work: it names the two conditions, which is what licenses the contrast that follows. `2311.08516` spends a whole sentence establishing that correction was tested "separately from mistake finding"; `2306.09896` establishes that the cost of repair is counted.
- **N, one sentence, fenced inside the clause.** Median 29 words in this subgroup.
- **C, one to three sentences, immediately after.** No transitional paragraph, no restatement of the negative. `2305.15771` uses a four-word pivot sentence ("However, the results in the LLM-Modulo setting show more promise.") and then a full sentence of substance.
- **Close.** Four of the eight land on the counterpart, two on the negative, two on an implication.

### 11.3 What this implies for the submission, stated as choices

The paper reports three things: undirected requests mostly produce no revision; the revisions that occur lower quality more often than they raise it; a targeted critique reverses this. That is one more negative than any abstract in the corpus carries before its counterpart, and the corpus suggests how to handle it.

1. **Two negatives, one sentence, or two short ones.** `2310.12397` and `2404.03602` are the corpus's precedent for stacking negatives, and both use an enumerated list ((i)(ii)(iii), or 1) 2) 3) 4)) rather than separate sentences. `2505.05410` does the same with three numbered findings inside one sentence. Enumeration inside one sentence is how this corpus fits several negatives into a results beat without the abstract turning into a list.
2. **Put the method sentence first.** 77 percent of the corpus does, and in the eight closest analogues the method sentence is what makes the contrast legible: it has to name the undirected condition and the targeted condition as two arms of one design before either result is stated. Leading with the finding is available but every abstract that does it has a title that states the claim on its own.
3. **Give the targeted-critique result about as many words as the two negatives together.** Not fewer, which is what the full corpus median would suggest, and not a token clause. The eight two-condition papers run at parity.
4. **Fence in the clause, not in a following sentence.** The corpus's dominant fence is a coordinate: the task, the domain, the model set, or the condition, welded into the same clause as the failure verb. Four fences is the median. A separate sentence that walks back the finding appears in only two of 53 and both read as concessions the authors were forced into.
5. **Land on the counterpart or on an implication, not on the negative.** Only 14 of 53 restate the negative last, and those are papers with no counterpart to land on. With a counterpart in hand, the corpus's own practice is to close on it (`2406.01297`, `2305.15771`, `2402.08115`, `2302.00093`) or on what it implies (`2409.12183`).
6. **Name the fix, because the counterpart already is one.** 38 percent of the corpus names a remedy, and the papers that pair a failing condition with a working one are naming it by construction. The targeted critique is the named fix; it does not need a separate future-work sentence behind it.
7. **One or two numbers, in the results beat.** The venue median is about half a numeral per 100 words and negative valence does not change it. The eight analogues sit at 0.23. In a 185-word abstract that is one figure, and the corpus puts it on the size of the failure or on the size of the reversal, not on the sample.

### 11.4 The one gap the corpus does not fill

No abstract in the 53 reports **a null and a harmful effect and a reversal**, which is the submission's actual three-part result. The nearest is `2306.09896`, whose negative is itself three-part ("performance gains are often modest, vary a lot between subsets of the data, and are sometimes not present at all") and which fits all three into one sentence with a shared subject and three coordinated predicates. That construction, one subject and a series of predicates rather than a series of sentences, is the one the submission's first two findings can borrow directly.

