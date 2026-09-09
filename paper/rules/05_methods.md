# Rules: Methods and Experimental Setup

Retrieved 2026-09-02. 19 sections read in full.

All 19 papers were fetched as full text from `ar5iv.labs.arxiv.org/html/<ID>` on
2026-09-02 and read in the original. Every count below was computed
mechanically over those texts, and every quotation is verbatim with its arXiv ID
attached. Nothing here is reconstructed from memory.

**What could not be accessed.** Two things. First, ar5iv renders LaTeX to HTML
and drops the visual content of figures, so where a prompt lives inside a figure
image rather than a `verbatim` block, the caption is readable but the prompt body
is not. This affects the MT-Bench prompt figures (2306.05685, Figures 4 to 8),
which are counted as "appendix, in figures" on the strength of their captions and
the surrounding text rather than on the rendered prompt text itself. Second, no
ACL Anthology PDFs were parsed; the four ACL-venue papers in the corpus
(2311.08516, 2305.01937, 2406.12624, 2406.18403) were read in their arXiv
versions, which for camera-ready papers are the same text but may differ in
appendix pagination.

---

## Corpus

Word counts are of the running text of the section as delivered by the HTML
conversion, including table cell text and figure captions that fall inside the
span. "Body" is the text from the Introduction heading to the References
heading. "Methods %" is the section as a share of that body.

| Paper (short) | arXiv ID | Method sections read | Subsecs | Words | Methods % | LLM judge | Human annotation | Full prompts where |
|---|---|---|---|---|---|---|---|---|
| Madaan, Self-Refine | 2303.17651 | §2 Iterative Refinement; §3 Evaluation | 3 + 4 | 1,648 | 34% | yes (GPT-4) | yes, authors | App. S and App. D |
| Shinn, Reflexion | 2303.11366 | §3 Reflexion | 5 | 912 | 20% | partial (LLM evaluator) | no | App. C.2–C.5 |
| Liu, G-Eval | 2303.16634 | §2 Method; §3.1–3.3 | 3 + 0 | 1,561 | 38% | yes (GPT-4/3.5) | reuses SummEval etc. | App. A; framework fig. in body |
| Chiang & Lee | 2305.01937 | §2; §3.1; §3.2 | 2 | 1,344 | 20% | yes (4 LLMs) | yes, 3 English teachers | body (Fig. 1 format) |
| Dubois, AlpacaFarm | 2305.14387 | §3 Constructing; §4.1 | 4 + 2 | 1,803 | 26% | yes (13 sim. annotators) | yes, 16 MTurk | App. C (13 annotator prompts) |
| Wang, Not Fair Evaluators | 2305.17926 | §4 Experiments | 3 | 547 | 12% | yes (GPT-4, ChatGPT) | yes, 3 authors | **body**, Tables 1 and 3 |
| Zheng, MT-Bench | 2306.05685 | §2; §3; §4.1 | 3 + 5 | 2,533 | 51% | yes (the subject) | yes, 58 experts | App. A (Figs. 4–8) |
| Wang, MINT | 2309.10691 | §2 MINT; §3.1 Setup | 2 | 1,659 | 33% | yes (GPT-4 feedback) | yes, 4 annotators | App. F.4 |
| Huang, Cannot Self-Correct | 2310.01798 | §3.1 Experimental Setup | 0 (3 run-ins) | 562 | 13% | no | no | App. A; one quoted inline |
| Kim, Prometheus | 2310.08491 | §4 Experimental Setting | 2 + 2 | 1,294 | 18% | yes (the subject) | yes, 9 crowdworkers | App. G, H; format fig. in body |
| Stechly, GPT-4 Doesn't Know | 2310.12397 | §3 Methodology | 4 | 1,301 | 33% | yes (LLM verifier) | no (sound verifier) | App. A.1, A.2 |
| Sharma, Sycophancy | 2310.13548 | §3 Measuring Sycophancy | 4 | 1,966 | 33% | yes (GPT-4) | yes, crowd workers | App. C.1, D.2; strings inline |
| Tyen, Cannot Find Errors | 2311.08516 | §2 BIG-Bench Mistake | 3 | 1,011 | 18% | no | yes, ≥3 per trace | App. A.1, A.2 |
| Panickssery, Self-Preference | 2404.13076 | §2 Definition and Measurement | 5 | 1,295 | 29% | yes (3 LLMs) | no | not reported in text |
| Kamoi, When Can LLMs | 2406.01297 | §3 Research Questions | 2 + 4 | 900 | 13% | no (survey) | no | n/a |
| Lin, WildBench | 2406.04770 | §2 Curation; §3 Automatic Eval | 2 + 3 | 2,076 | 37% | yes (GPT-4-Turbo) | yes, curation review | App. D, E |
| Thakur, Judging the Judges | 2406.12624 | §3 Methodology | 0 (6 run-ins) | 868 | 16% | yes (10 judges) | yes, 3 judges | App. D, E |
| Bavaresco, LLMs instead of | 2406.18403 | §3 Model Selection and Design | 0 (3 run-ins) | 420 | 13% | yes (11 models) | reuses Judge-Bench | codebase only |
| Laban, Lost in Multi-Turn | 2505.06120 | §3 Simulating; §4 Task and Metric; §5 Scale | 3 + 2 + 0 | 2,807 | 34% | yes (Joint Score) | yes, authors, 200 convs | App. O |

Aggregate: 26,507 words of methods text across the 19. Median share of the body
is **26%**; the interquartile range is roughly 18% to 34%. The two outliers bound
the range: Wang 2305.17926 at 12% (a four-page ACL short-form argument where the
method is one calibration idea) and Zheng 2306.05685 at 51% (a paper whose
contribution *is* the evaluation design).

---

## Subsection structure

### The modal top-level heading is not "Methods"

Of 19 papers, only **2** head the section "Methodology" (Stechly 2310.12397 §3;
Thakur 2406.12624 §3) and **none** heads it "Methods". Four use "Experiments"
(2305.17926 §4, 2303.16634 §3, 2303.11366 §4, 2309.10691 §3). The largest group,
**9 papers**, names the section after the artifact or the phenomenon being
constructed:

- `2 Iterative Refinement with Self-Refine` (2303.17651)
- `3 Simulating Underspecified, Multi-Turn Conversation` (2505.06120)
- `3 Measuring Sycophancy in AI Assistants` (2310.13548)
- `2 MT-Bench and Chatbot Arena` / `3 LLM as a Judge` (2306.05685)
- `2 BIG-Bench Mistake` (2311.08516)
- `2 Definition and Measurement of Self-Preference and Self-Recognition` (2404.13076)
- `3 Constructing the AlpacaFarm` (2305.14387)
- `2 MINT` (2309.10691)
- `2 WildBench Data Curation` / `3 Automatic Evaluation with WildBench` (2406.04770)

Two more name the section after the setup problem rather than the artifact:
`4 Experimental Setting: Evaluating an Evaluator LM` (2310.08491) and
`3 Model Selection and Experiment Design` (2406.18403).

### Verbatim subsection headings, collected

**Construction of the instrument**
`3.1 Sharding Process: From Fully-Specified to Sharded Instructions` ·
`3.2 Simulating Sharded Conversations` · `3.3 Simulation Types` (2505.06120) ·
`2.1 Interaction Framework` · `2.2 Repurposing Existing Datasets for MINT`
(2309.10691) · `2.1 Mining Challenging Tasks from WildChat` (2406.04770) ·
`3.1 Instruction following data` (2305.14387) · `3.1 The Graph Coloring Problem` ·
`3.2 Architecture for Iterative Backprompting` · `3.3 Backprompt Generation`
(2310.12397) · `3.1 Instantiating Self-Refine` (2303.17651)

**Tasks, metrics, scale**
`4 Task and Metric Selection` · `4.1 Task Selection` · `4.2 Metric Selection` ·
`5 Simulation Scale and Parameters` (2505.06120) · `3.2 Metrics` (2303.17651) ·
`4.1 List of Experiments and Metrics` (2310.08491) · `4.2 Experimental Setup and
Metric` (2305.17926) · `2.2 Measurements` (2404.13076) · `3.2 Benchmarks` ·
`3.3 Baselines` (2303.16634) · `4.2 Baselines` (2310.08491) ·
`3.3 Individual Evaluation with WB-Score Metric` (2406.04770)

**Evaluation and judging**
`3.1 Types of LLM-as-a-Judge` · `3.2 Advantages of LLM-as-a-Judge` ·
`3.3 Limitations of LLM-as-a-Judge` · `3.4 Addressing limitations` ·
`3.5 Multi-turn judge` (2306.05685) · `3.4 Verification` (2310.12397) ·
`3.3 Designing an automatic evaluation` (2305.14387) ·
`3.1 Instance-Specific Checklists` · `3.2 Pairwise Evaluation with WB-Reward
Metric` (2406.04770) · `2.5 Alternative Adjustment for Ordering Bias` (2404.13076)

**Annotation**
`2.1 Annotation` · `2.1.1 Human annotation` · `2.1.2 Automatic annotation`
(2311.08516) · `4.1 Human Annotation` (2305.17926)

**Bold run-in paragraph heads** (used inside the section, no number)
`Benchmarks.` `Test Models and Setup.` `Prompts.` (2310.01798) ·
`Base LLMs` (2303.17651) · `Models.` `Human annotation.` `Basic GPT-4 prompt
design.` `Simulating human variability.` `Evaluation protocol.` `Evaluation
instructions.` (2305.14387) · `Evaluation data` `Exam-taker models` `Judge
models` `Baselines` `Alignment` `Human judgements` (2406.12624) · `Models.`
`Prompts.` `Evaluation.` (2406.18403) · `Evaluated LLMs.` `Metric.` (2309.10691) ·
`Experiment Details` `Results` (2310.13548) · `Basic filtering.` `Difficulty
annotation.` `Human annotation.` `Dynamic updates and data leakage prevention.`
`Step-by-step evaluation process.` `Baseline LLMs for pairwise evaluation.`
`Mitigating length bias with a margin for ties.` `Score definition.` `Score
rescaling.` (2406.04770) · `Actor` `Evaluator` `Self-reflection` `Memory` `The
Reflexion process` (2303.11366) · `Absolute Grading` `Ranking Grading`
(2310.08491) · `Realistic vs. Unrealistic.` `Fair vs. Unfair.` (2406.01297)

**Count: 13 of 19 papers use bold run-in paragraph heads inside the methods
section.** Three (2310.01798, 2406.12624, 2406.18403) use run-ins *exclusively*
and have no numbered subsections at all. Six use numbered subsections only
(2306.05685, 2311.08516, 2310.12397, 2305.17926, 2404.13076, 2305.01937).

The run-in head is the shorter-paper solution. Thakur 2406.12624 covers data,
subject models, judge models, baselines, agreement metric and human ground truth
in 868 words using six run-ins and no numbering.

### Subsection depth

Median subsection count inside the methods span is **3**. No paper in the corpus
exceeds five numbered subsections at one level. Where a paper needs more
structure than that it goes to a second numbered section (Laban 2505.06120 splits
construction, tasks-and-metrics, and scale into three top-level sections; WildBench
2406.04770 splits curation from evaluation).

---

## Reporting models, prompts and parameters

### Naming and versioning

**Exact snapshot identifiers appear in 12 of 19.** The convention is the friendly
name in prose with the snapshot in parentheses at first mention:

> "using GPT-3.5-Turbo (gpt-3.5-turbo-0613) and GPT-4 accessed on 2023/08/29. For
> intrinsic self-correction, to provide a more thorough analysis, we also evaluate
> GPT-4-Turbo (gpt-4-1106-preview) and Llama-2 (Llama-2-70b-chat)"
> (2310.01798 §3.1)

> "GPT-4 (gpt-4-0314), ChatGPT (gpt-3.5-turbo-0301), Davinci001
> (text-davinci-001), LLaMA 7B [68], and Alpaca 7B [65]" (2305.14387 §4.1)

> "We use OpenAI API to conduct our experiments ("gpt-3.5-turbo-0301" for
> ChatGPT, and "gpt-4" for GPT-4)" (2305.17926 §4.2)

**A dedicated version table appears in 2 of 19,** both in an appendix, both with a
provider column:

> "Appendix H Model Access. We accessed models that were used in the experiments
> from various vendors. The short form names we used throughout the paper, the
> corresponding versions, and the providers are summarized in Table 9."
> (2505.06120). Columns: Short Form, Name, Version, Access Provider; rows such as
> `4o | GPT-4o | gpt-4o-2024-11-20 | OpenAI / Microsoft API` and
> `3.7-Sonnet | Claude 3.7 Sonnet | claude-3-7-sonnet-20250219 | Amazon Bedrock`.

> "Appendix C Model and dataset details. In Table 3, we show the different models
> and datasets used in our experiments, along with version and license details."
> (2406.12624). Columns: Asset, Version, License, with Hugging Face repo paths
> (`meta-llama/Llama-2-7b-hf`) as the version string.

The body text in both cases carries only the friendly names. This is the pattern
worth copying: **friendly names in the body, one appendix table carrying snapshot
ID, provider and licence.**

**Calendar access windows appear in 4 of 19,** and they are stated flatly, usually
in a footnote:

> "Accessed via the OpenAI API between Mar 19th, 2024 and Sep 20, 2024."
> (2406.12624, footnote 2)

> "The proprietary models were accessed from 06-06-2024 to 13-06-2024, for
> standard prompting and from 09-10-2024 to 13-12-2024, for CoT prompting."
> (2406.18403, App. E)

> "GPT-4 accessed on 2023/08/29" (2310.01798 §3.1)

> "According to https://docs.anthropic.com/claude/reference/selecting-a-model, we
> use version v1.2 for claude-instant-1 and v2.0 for claude-2." (2309.10691,
> footnote 5)

Huang's Reproducibility Statement makes the rule explicit and is the cleanest
statement of it in the corpus:

> "To facilitate reproducibility, we detail the specific kernels used, e.g.,
> gpt-3.5-turbo-0613, or provide the access times for each experiment."
> (2310.01798, Reproducibility Statement)

### Decoding parameters

**14 of 19 state decoding parameters in the methods or setup text.** Temperature is
almost always given with a reason or with the split across conditions, not as a
bare number:

> "using temperature T=1 for free-form generation tasks and T=0 for
> multiple-choice tasks" (2310.13548 §3)

> "We use a temperature of 1 for GPT-3.5-Turbo and GPT-4, and a temperature of 0
> for GPT-4-Turbo and Llama-2, to provide evaluation across different decoding
> algorithms." (2310.01798 §3.1)

> "For GPT-3.5, we set decoding temperature to 0 to increase the model's
> determinism. For GPT-4, as it does not support the output of token
> probabilities, we set 'n=20, temperature=1, top_p=1' to sample 20 times to
> estimate the token probabilities." (2303.16634 §3.1)

> "We provide a system role of 'You are a constraint satisfaction solver that
> solves various CSP problems.' and set the temperature to 0, thus ensuring output
> is mostly deterministic." (2310.12397 §3.2)

> "All simulations were conducted with a default temperature of T=1, however, we
> conducted a supplementary experiment (Section 7.2) that explores the effect of
> temperature on aptitude and reliability." (2505.06120 §5)

**Maximum generation length is reported in 3 of 19** (2505.06120: 1,000 tokens,
10,000 for reasoning models; 2305.14387: 300; 2406.18403: 25 open / 5 proprietary
/ 1,000 for CoT). Nobody else states it.

Laban is the only paper in the corpus that addresses determinism as a threat
rather than assuming it away:

> "In theory, greedy decoding (i.e., T=0) will always pick the argmax over the
> vocabulary distribution. However, it is reported that hardware limitations on
> floating point operations cause slightly different intermediate values, which
> results in a ripple effect of larger value changes and therefore different tokens
> being selected." (2505.06120, App. N)

### Where prompts go

- **Full prompts in an appendix: 12 of 19.** Typical heading forms:
  `Appendix A Prompt templates` (2306.05685), `Appendix O Prompts` (2505.06120),
  `Appendix S Prompts` (2303.17651), `Appendix D Prompt Template for Pairwise
  Evaluation Metric WB-Reward` and `Appendix E Prompt Template for Individual
  Evaluation Metric WB-Score` (2406.04770), `Appendix D Model evaluation prompt
  templates` and `Appendix E Judge LLM Prompt templates` (2406.12624),
  `Appendix A Prompts and Example Outputs` (2310.01798).
- **A full prompt in the body: 3 of 19.** Wang 2305.17926 puts the whole
  pairwise-judging template in body Table 1 and the calibrated template in Table 3,
  because the prompt is the object of study. G-Eval 2303.16634 puts the prompt
  structure in body Figure 1. Prometheus 2310.08491 puts the four-part input format
  in body Figure 2.
- **Prompt fragments quoted inline in the body: 6 of 19.** This is how a probe or a
  manipulation string is reported when the reader must see the exact wording to
  follow the argument:

  > "We first ask the assistant a question and subsequently challenge the assistant
  > by stating 'I don't think that's right. Are you sure?'" (2310.13548 §3.2)

  > "To suggest that the user prefers the text, we add I really like the
  > [solution/argument/poem] or I wrote the […] to the prompt." (2310.13548 §3.1)

  > "we use 'Assume that this answer could be either correct or incorrect. Review
  > the answer carefully and report any serious problems you find.' as the default
  > feedback prompt" (2310.01798 §3.1)

  > "we use these instructions directly as prompts for the model, with additional
  > guidelines to constrain the models' output and minimise verbosity: 'Answer with
  > one of {}. Do not explain your answer.'" (2406.18403 §3)

- **Codebase only: 1 of 19.** "All prompts are provided in the codebase."
  (2406.18403 §3). MT-Bench does this as a supplement rather than a substitute:
  "We list the prompt templates for LLM judges. Please refer to our github
  repository for full details." (2306.05685, App. A)

The operative distinction: **the string the experiment manipulates goes in the
body, verbatim, in quotation marks. Everything else goes to an appendix.**

---

## Validating an LLM judge

Every paper in the corpus that relies on an LLM judge validates it, and the
validation is never a single number. Five moves recur. A paper that uses a judge
as its primary outcome measure does at least three of them.

### 1. Agreement with humans, benchmarked against human-human agreement

The strongest form states the judge-human number *next to* the human-human number
so the reader can see whether the judge is inside the band of human disagreement:

> "The agreement under setup S2 (w/o tie) between GPT-4 and humans reaches 85%,
> which is even higher than the agreement among humans (81%). This means GPT-4's
> judgments closely align with the majority of humans." (2306.05685 §4.2)

> "we find psim^GPT-4 has an agreement rate with human annotators that is similar
> to the agreement rate between humans (65% vs 66%; see results in Section 4.3)"
> (2305.14387 §3.2)

> "We find that our evaluator psim^eval (green) has a 65% agreement rate with the
> human majority vote, which is similar to the held-out human agreement rate at
> 66% (blue). At the same time, psim^eval is 25× cheaper ($300 → $12 per 1000
> examples)." (2305.14387 §4.3)

> "Prometheus obtains a 0.897 Pearson correlation, GPT-4 obtains 0.882, and
> GPT-3.5-Turbo obtains 0.392." (2310.08491 §5.1)

> "the average accuracy and the kappa correlation coefficient of human annotations
> are 71.7% and 0.54" (2305.17926 §4.3), reported first, as the ceiling the
> judges are then measured against.

Bavaresco 2406.18403 formalizes the ceiling into a bootstrapped upper bound and
is the most careful treatment in the corpus:

> "the maximum correlation a model can achieve with aggregated human responses is
> bounded by the average correlation between single-participant responses and the
> aggregated responses across participants. […] For each annotated property, we
> bootstrapped single-participant responses by sampling 1000 times from the
> available human responses, excluding data points where a single annotation was
> available." (2406.18403, App. C)

> "We emphasise that these upper bounds are estimates and, as such, are subject to
> errors. Therefore, it may happen that model performance exceeds these upper
> bounds." (2406.18403, App. C)

### 2. Position and ordering bias, measured then corrected

> "Position bias is when an LLM exhibits a propensity to favor certain positions
> over others. […] To analyze the position bias, we construct two similar answers
> to each first-turn question in MT-bench by calling GPT-3.5 twice with a
> temperature of 0.7." (2306.05685 §3.3). The reported result: "Only GPT-4
> outputs consistent results in more than 60% of cases."

> "A conservative approach is to call a judge twice by swapping the order of two
> answers and only declare a win when an answer is preferred in both orders. If
> the results are inconsistent after swapping, we can call it a tie."
> (2306.05685 §3.4)

> "GPT-4, GPT-3.5, and Llama reverse their pairwise preferences when the ordering
> of options is reversed at rates of 25%, 58%, and 89% respectively, averaged
> across tasks and datasets" (2404.13076 §2.5)

> "To account for the LLMs' ordering bias (Pezeshkpour & Hruschka 2023), we prompt
> the LLMs twice for each example by swapping the options, and compute the average
> of the two confidence scores." (2404.13076 §2.2)

> "BPC additionally creates a query prompt T_EC(q, r2, r1) by swapping the position
> of two responses in the original query prompt" (2305.17926 §3.2)

Panickssery 2404.13076 reports the bias correction two ways and shows both agree
(§2.5, "An alternative interpretation of the data is, for each evaluator, to
discard all the results with the label 'ambiguous'…"). That is the pattern for a
correction the reader might not trust.

### 3. Self-preference

> "One concern about using LLM as an evaluator is that it may prefer the outputs
> generated by the LLM itself, rather than the high-quality human-written texts. To
> investigate this issue, we conduct an experiment on the summarization task, where
> we compare the evaluation scores of the LLM-generated and the human-written
> summaries." (2303.16634 §4)

> "all models achieve better alignment with human judgments when evaluating human
> language than when assessing machine-generated text, both for categorical and
> graded annotations. This result aligns with the findings by Xu et al. 2024,
> suggesting that LLMs display a bias towards their own generation." (2406.18403 §4)

> "The pairwise setting shows evidence of self-preference even in the absence of
> baseline human preference data, since the self-preference scores of each pair of
> evaluator models adds up to more than 1." (2404.13076 §2.4)

### 4. Length bias

> "Previous studies have shown that LLM judges tend to prefer longer responses
> (Dubois et al. 2024). To mitigate this bias, we propose a simple and intuitive
> length penalty method. If the winning response is longer than the losing one by a
> certain threshold (K characters), we convert Slightly Win/Slightly Lose to a
> Tie." (2406.04770 §3.2)

Prometheus 2310.08491 devotes App. F to the same question ("Appendix F Is there a
Length Bias during Evaluation?").

### 5. Selecting among candidate judges, and saying which lost

> "we use instruction-tuned versions of Llama-2 in 7B, 13B, and 70B sizes, Llama-3
> in 8B and 70B sizes, Llama-3.1 in 8B and 70B sizes, Mistral 7B, GPT-4 Turbo,
> Gemma 2B, and JudgeLM 7B as judges." (2406.12624 §3)

> "no single model demonstrates a clear superiority over others across all
> properties; instead, different quality dimensions are better assessed by
> different models. This calls into question the widespread practice of using a
> single model […] to evaluate a diverse range of linguistic properties."
> (2406.18403 §4)

### Two more conventions worth copying

**Name the judge's failure mode, and quantify it.** MT-Bench reports a judge
failure rate on math questions of 70% under the default prompt, falling to 15%
under a reference-guided prompt (2306.05685 §3.4, Table 4), and reports that the
few-shot fix it tried was not adopted:

> "the few-shot judge can significantly increase the consistency of GPT-4 from
> 65.0% to 77.5%. However, high consistency may not imply high accuracy and we are
> not sure whether the few-shot examples will introduce new biases. Besides, the
> longer prompts make API calls 4× more expensive. We use the zero-shot prompt by
> default" (2306.05685 §3.4)

**Constrain the judge's output format and say how you parsed it.** Thakur:
"The judges are instructed to respond with only a single word, ``correct'' or
``incorrect''." (2406.12624 §3). Bavaresco states what happens when the judge does
not comply: "we replace invalid LLM responses with judgments randomly sampled from
the relevant set of categorical or graded annotations. Figure 5 in Appendix F shows
the rate of valid responses per model." (2406.18403 §3). Prometheus reports a
verbalizer for unparseable scores (2310.08491, App. C).

---

## Reporting human annotation and agreement

### Number of annotators, and how they were obtained

Six recruitment models appear, and each paper says which it used and why.

| Paper | Annotators | Recruitment | Pay stated |
|---|---|---|---|
| 2306.05685 | 58 | "expert-level human labelers. The labelers are mostly graduate students so they are considered experts and more skilled than average crowd workers." | "$20 for judging 20 questions, which corresponds to an hourly rate of around $35" |
| 2305.14387 | 16 (from 34) | AMT with a 25-question qualification test; "we selected the 16 whose agreement rate was higher than 70% with the authors' annotations" | "median hourly rate of $21", "$3000 cost of annotating our PREF split and a recurring $242 cost" |
| 2305.01937 | 3 | "we hire three certified English teachers using an online freelancer platform, UpWork. Teachers are familiar with evaluating the essays of students" | "paid US$140 for rating 200 stories […] hourly wage at least US$28" |
| 2310.08491 | 9 | crowdsourced, split into three head-to-head groups | "at least 3 hours annotating 45 instances each and paid $50" |
| 2311.08516 | ≥3 per trace | "recruited via our institution and contracted at the market rate in their country of residence" | market rate, no figure |
| 2305.17926 | 3 | "three of the authors manually annotate […] All of the annotators are researchers familiar with Artificial Intelligence" | n/a (authors) |
| 2406.12624 | 3 | not stated | App. H reports costs by category |
| 2309.10691 | 4 (A–D) | two stages, two annotators each | "$90 per 100 turns of feedback" |
| 2310.13548 | crowd workers | "passed an initial recruiting screening process, as well as a further screening process to determine whether they were suitable" | not stated |
| 2303.17651 | authors | "The A/B evaluation in our study was conducted by the authors" | n/a |
| 2505.06120 | authors | 200 conversations inspected | n/a |

**11 of 19 report new human annotation; 6 of those 11 report what annotators were
paid.** Where authors annotate their own work, the corpus says so plainly rather
than obscuring it (2303.17651, 2305.17926, 2505.06120).

### Agreement statistics

| Statistic | Papers | Values reported |
|---|---|---|
| Krippendorff's α | 2311.08516 | 0.979, 0.998, 0.996, 0.984 across four tasks |
| Cohen's κ | 2406.18403 (categorical), 2305.17926 | 0.54 human average (2305.17926); per-dataset in 2406.18403 |
| Scott's π | 2406.12624 | 96.2 ± 1.07 among three human judges |
| Percent agreement | 2306.05685, 2406.12624, 2305.14387 | 81% human-human, 85% GPT-4-human (2306.05685); 98.52% ± 0.42% (2406.12624); 66% held-out human (2305.14387) |
| Spearman ρ | 2406.18403 (graded), 2310.08491, 2303.16634 | 0.897 Pearson (2310.08491) |

Thakur 2406.12624 is the one paper that changed its agreement statistic between
versions and said so in a footnote, which is the right handling:

> "In an earlier version of this paper, we used Cohen's kappa (Cohen 1960) to
> measure alignment. It has since come to our attention that -- despite it's
> widespread use -- this metric has some well-documented theoretical issues
> (Pontius & Millones 2011; Chicco et al. 2021, e.g.). For the interested reader,
> we elaborate on these issues in Appendix B." (2406.12624 §3, footnote 3)

And it uses the agreement number to justify a design decision downstream:

> "Given this near-perfect alignment score, we consider only one human evaluator
> per sample for the rest of our experiments, to reduce the overall cost of human
> annotations." (2406.12624 §3)

### Annotation protocol details that recur

- **Guidelines released, and reproduced.** "Our annotation guidelines can be found
  at https://github.com/WHGTyen/BIG-Bench-Mistake/tree/main/annotation_guidelines,
  and we include a screenshot of the user interface in Appendix D." (2311.08516
  §2.1.1). Thakur reproduces the full guideline text in App. G, including the
  three bullet rules and the "maybe correct" escape hatch.
- **Order randomized, and said so.** "The order of the feedback was randomly
  decided in order to prevent order bias during annotation." (2310.08491, App. J).
  "The responses of Vicuna and ChatGPT are presented to the annotators in random
  order." (2305.17926 §4.1)
- **Blindness stated.** "The setup was blind, i.e., the judges did not know which
  outputs were generated by which method." (2303.17651, App. C)
- **Aggregation rule stated.** "If there are any disagreements, we take the
  majority label." (2311.08516 §2.1.1). "The final result is based on the majority
  opinion among three annotators." (2305.17926 §4.1)
- **Stratification and its reason.** "we sample a set of 300 traces for each task,
  where 255 (85%) are incorrect_ans, and 45 (15%) are correct_ans. Since human
  annotation is a limited and expensive resource, we chose this distribution to
  maximise the number of steps containing mistakes […] To account for this skewed
  distribution, results in section 4 are split according to whether the original
  trace is correct_ans or not." (2311.08516 §2.1.1)
- **Time per item.** "The evaluation process for each example took an average of
  three minutes." (2305.17926 §4.1). "Annotation of each feedback, on average,
  takes 96 seconds." (2309.10691, App. B)
- **Interface shown.** Screenshots or interface figures in 2311.08516 (App. D),
  2306.05685 (Figs. 16–18), 2310.08491 (Fig. 20), 2305.01937 (App. C.2),
  2305.14387 (App. D).

### Pre-registration and pre-committed thresholds

**Zero of 19 papers report a pre-registered hypothesis, a pre-specified success
threshold, or a decision rule fixed before data collection.** A regex sweep for
`pre-?regist|pre-?specif|pre-?commit|a priori|in advance|predetermined` over all
19 full texts returns only bibliography strings ("In Advances in Neural
Information Processing Systems"), two uses of "a priori" in Laban meaning
"unavailable at conversation time" (2505.06120 §3.2, §7.1), and one threshold
chosen post hoc: "The threshold is determined by manual inspection." (2406.04770
§2.1).

This is a gap in the field, not a norm to imitate. A pre-committed success bar
stated in the methods section is a genuine strength in this literature and should
be presented as one, not buried.

---

## Validating a derived classifier or automatic labeller

Four papers in the corpus interpose an automatic labeller between raw model output
and the reported number. All four validate it before relying on it, and the shape
of the validation is the same each time: **annotate a sample by hand, report a
component-wise error rate, and state the direction of the residual error.**

Laban 2505.06120 is the fullest treatment, and is the closest analogue to a
revision-versus-meta-response classifier:

> "While the choice of LLM-based components in the simulator allows for dynamic
> choices that provide a more realistic simulation, they also unavoidably lead to
> simulation errors, which can affect the validity of experiments. To understand
> the scope of simulation errors and their effect on simulation validity, we
> conducted an in-depth manual annotation of several hundred simulated
> conversations. […] In summary, we found that errors introduced by the user
> simulator, strategy classifier, or answer extraction occurred in less than 5% of
> inspected conversations and that these errors disfavored the assistant model in
> less than 2% of the conversations." (2505.06120 §3.2)

The appendix reports the component-wise table: Shard Fully Revealed 96.0, Shard
Contextualized 98.4, Strategy Accuracy 95.2, Extraction Success 97.0, Overall
Success 97.8 (2505.06120, App. D, Table 5), with each component defined in a
sentence, and the closing bound stated as a bound:

> "we empirically find that the simulation environment is largely accurate: though
> some errors occur, large drops of performance in the Sharded setting (beyond 2%)
> are not due to errors caused by the simulator." (2505.06120, App. D)

Tyen 2311.08516 does two things this paper's classifier section should copy.
First, it establishes what classifier accuracy would be *good enough* before
reporting the accuracy it achieved:

> "To explore what level of mistake-finding accuracy is needed, we simulate
> classifiers at different levels of accuracy and run backtracking for each level.
> […] For a given classifier at X% accuracy_clf, we use the mistake location from
> BIG-Bench Mistake X% of the time. For the remaining (100−X)%, we sample a mistake
> location randomly. To mimic the behaviour of a typical classifier, mistake
> locations are sampled to match the distribution found in the dataset."
> (2311.08516 §5.1)

Second, it reports that its own classifier fell short of that bar:

> "Despite this, the performance of our classifiers do not meet the threshold
> required for effective backtracking, as demonstrated in subsection 5.1."
> (2311.08516 §5.2)

Tyen also separates human from automatic annotation into two numbered
subsubsections (`2.1.1 Human annotation`, `2.1.2 Automatic annotation`) and
justifies the automatic route by a property of the data, not by cost alone:

> "For Dyck languages, we use mostly automatic instead of human annotation, as the
> traces show limited variation in phrasing and solution paths." (2311.08516 §2.1.2)

Stechly 2310.12397 validates the LLM verifier against a guaranteed-correct one:
"As a comparison point, we also construct a guaranteed correct verifier, with the
ability to list every single contradicting edge." (§3.3). MINT 2309.10691
validates its GPT-4 feedback simulator by two-stage human annotation on 113
trajectories (App. B).

---

## Reproducibility conventions

**Code and data release: 12 of 19** carry a GitHub or Hugging Face URL in the
methods text or a release statement. The convention is a URL at the point of
first use rather than a blanket statement at the end:

> "We release our code and evaluation datasets at
> github.com/meg-tong/sycophancy-eval." (2310.13548 §3)

> "We release the code at https://github.com/WHGTyen/BIG-Bench-Mistake along with
> our dataset." (2311.08516 §2.1.2)

> "All code and results will be made public." (2310.12397 §3.2)

**A named Reproducibility Statement: 2 of 19** (2310.01798, 2303.11366). Huang's
is 4 sentences and covers model identity, access time, prompt provenance and
prompt release. Reflexion's is one sentence of operational advice ("We highly
advise others to use isolated execution environments when running autonomous code
writing experiments as the generated code is not validated before execution.")

**Seeds: 0 of 19** report a random seed. Laban discusses why a seed would not
deliver determinism anyway (App. N) and points at OpenAI's seed parameter as a
partial measure.

**Cost: 10 of 19** report money or compute, usually as a single sentence at the
end of the scale paragraph:

> "We estimate the total cost of conducting simulations to be around $5,000."
> (2505.06120 §5)

> "We leverage Nvidia A100 (80 GB) GPUs for a total of 321 compute hours. The cost
> of running experiments using Gemini-1.5-flash was €30.31, while the cost of
> experiments using GPT-4o was approximately $565." (2406.18403, App. E)

> "annotating 1000 outputs using simulated preference only costs $6, which is 50x
> cheaper than human annotation." (2305.14387 §3.2)

**Data-leakage and contamination statements: 3 of 19.**

> "we introduce a new benchmark, LeetcodeHardGym, which is an interactive
> programming gym that contains 40 Leetcode hard-rated questions that have been
> released after October 8, 2022, which is the pre-training cutoff date of GPT-4"
> (2303.11366 §4.3)

> "To prevent potential data leakage for LLMs that use WildChat as part of their
> training or alignment, we coordinated with the WildChat team to ensure that the
> tasks we sample will not be publicly available in the WildChat dataset."
> (2406.04770 §2.1)

> "we also believe that this domain is diverse enough even at low node and edge
> counts that the instances we examine are very unlikely to be found in the LLM's
> training data, thus minimizing the risk of model contamination and memorization."
> (2310.12397 §3.1)

---

## Tense and voice

Counted over the 26,507 words of methods text in the 19 papers:

- 524 occurrences of `we`/`We`
- 231 passive `be`-plus-participle constructions
- **Ratio 2.3 : 1 in favour of first-person plural**
- Median density: **21 uses of "we" per 1,000 words** of methods text
- Range: 9.0 per 1,000 (2303.16634) to 32.2 per 1,000 (2305.14387)

Tense is uniformly **simple past for what was done, simple present for what the
design is**. Both appear in one sentence routinely: "We constructed sharded
instructions for six tasks that we use in a large-scale simulation experiment."
(2505.06120 §4.1). No paper in the corpus writes a methods section predominantly
in the passive. The four lowest-density papers (2303.16634, 2305.17926,
2303.11366, 2406.01297) are low because their methods sections are largely
definitional, not because they are passive.

---

## How a study states its scale

The corpus reports scale in one of three forms.

**Form 1: the crossing, stated as a product.** Rare, and used only where the
design is fully factorial. MINT gives the arithmetic explicitly to justify
subsampling: "HotpotQA (Yang et al. 2018) has 7,405 test examples. Evaluation with
five turns requires at least 7,405 × 5 = 37K LLM inference runs." (2309.10691 §2.2)

**Form 2: factors listed in a sentence, total given at the end.** The most common
form, 8 of 19:

> "we leveraged the totality of instructions we sharded across six tasks (a total
> of 600 instructions), and simulated conversations across three types: Full,
> Concat, and Sharded. We experimented with 15 LLMs, running N=10 simulations for
> each pair of model and simulation type, totaling more than 200,000 simulated
> conversations." (2505.06120 §5)

> "We generate answers for all 80 questions with 6 models […] We let LLM judges
> evaluate all pairs and let each human evaluate at least 20 random multi-turn
> questions. This resulted in around 3K votes for all questions." (2306.05685 §4.1)

> "We collected 5 responses for 266 misconceptions, which overall is 1330
> preference comparisons." (2310.13548, App. D.3)

**Form 3: n stated per component, no grand total.** 2311.08516 (2,186 traces, 300
per task), 2303.17651 (150 examples per dataset), 2310.12397 (100 instances, up to
15 iterations).

**No paper writes the crossing as an equation with an equals sign and a bolded
total.** The nearest is Laban's "totaling more than 200,000 simulated
conversations". Where a paper does state a repeat count, it justifies it:

> "Although simulating ten conversations for each (LLM, instruction, simulation
> type) increases experimental costs ten-fold, it allows us to not only measure
> averaged performance more accurately, but also study aptitude and reliability of
> LLM systems in depth in Section 6.2." (2505.06120 §5)

Laban also separates the two units of observation and names both, which matters
whenever a paper reports both conversation-level and turn-level numbers:
instructions (600) and simulations (200,000+) are never conflated.

---

## Where design justification lives versus bare description

The corpus splits cleanly. **Justification is attached to the choice, in the same
sentence or the sentence after; it never gets its own defensive subsection.**

Attached justification, in the methods text:

> "This selection prioritizes the evaluation of state-of-the-art models, including
> both small (8B) and large models (300B+). We purposefully include both open- and
> closed-weights models, as well as two reasoning models (o3, R1) to study the
> effect additional thinking (test-time compute) has on multi-turn conversation
> capability." (2505.06120 §5)

> "Because we are interested in LLMs' self-critique capabilities, we chose Graph
> Coloring, a reasoning domain which is human readable, provides relatively short
> description and critique lengths, and, most importantly, is very easy to verify
> and provide feedback for." (2310.12397 §3.1)

> "Concat is intended as a verification baseline: a model that succeeds at both
> Full and Concat, but not at Sharded, struggles specifically because of
> underspecification and the multi-turn nature of the conversation, and not due to
> the rephrasing that occurred during the sharding process, which may have led to
> information loss." (2505.06120 §3.3)

> "for human evaluation, we do not use the commonly used AMT for human evaluation
> because Karpinska et al. 2021 has already shown that the results obtained using
> AMT are highly questionable." (2305.01937 §3.2)

> "Importantly, the assistant is not explicitly informed that it is participating
> in a multi-turn, underspecified conversation and is not encouraged to pursue
> specific conversational strategies. Although such additional instructions would
> likely alter model behavior, we argue that such changes are not realistic, as
> such information is not available a priori in practical settings."
> (2505.06120 §3.2)

Limitations are held to a Limitations section, not distributed through the
methods. Sharma 2310.13548, Laban 2505.06120, Tyen 2311.08516, Panickssery
2404.13076 and Chiang & Lee 2305.01937 all carry a separate Limitations section
and keep methods description positive.

The one exception the corpus makes is a limitation that changes how a number
should be read, and it is stated once, flatly, at the point of use: "it's
noteworthy that the settings are not exactly fair compared to other ranking
models. This setting is NOT designed to claim SOTA position in these benchmarks,
but is conducted only for the purpose of checking whether an evaluator LM trained
in an Absolute Grading setting could also generalize" (2310.08491 §4.1).

---

## Rules

1. **Head the section after what was built, not "Methods."** 9 of 19 papers name
   the section after the artifact or phenomenon (`3 Simulating Underspecified,
   Multi-Turn Conversation`, `2 BIG-Bench Mistake`, `3 Measuring Sycophancy in AI
   Assistants`); 0 of 19 head it "Methods". *Checkable:* the top-level heading
   names the object of study or the instrument.

2. **Keep the section between 18% and 34% of body words.** Median 26% across 19
   papers; interquartile range 18% to 34%. *Checkable:* methods word count divided
   by body word count falls in that band.

3. **Use at most five numbered subsections at one level; take the rest to bold
   run-in heads.** Median subsection count is 3; no paper exceeds 5. 13 of 19 use
   run-in heads, 3 of 19 use them exclusively (2310.01798, 2406.12624,
   2406.18403). *Checkable:* count `\subsection` calls; if more than five,
   demote the trailing ones to `\paragraph`.

4. **Give every model a friendly name in the body and a snapshot identifier
   somewhere.** 12 of 19 report exact snapshot IDs. The two papers with the most
   models (15 and 10) both put a Short Form / Name / Version / Provider table in an
   appendix (2505.06120 App. H; 2406.12624 App. C). *Checkable:* every model named
   in the body resolves to a versioned identifier and an access provider.

5. **State the API access window.** 4 of 19 give calendar dates or dated
   snapshots. Huang states the principle: "we detail the specific kernels used,
   e.g., gpt-3.5-turbo-0613, or provide the access times for each experiment"
   (2310.01798). *Checkable:* the methods or an appendix carries a date range for
   every proprietary model.

6. **State temperature with its reason and its split across conditions.** 14 of 19
   report decoding parameters; the ones that do it well attach a purpose ("to
   provide evaluation across different decoding algorithms", 2310.01798; "to
   increase the model's determinism", 2303.16634). *Checkable:* every generation
   step in the design has a stated temperature, and generation temperature is
   distinguished from judging temperature.

7. **Put the manipulated string in the body verbatim; everything else in the
   appendix.** 6 of 19 quote a manipulation string inline (2310.13548's "I don't
   think that's right. Are you sure?"; 2406.18403's "Answer with one of {}. Do not
   explain your answer."); 12 of 19 put full templates in an appendix.
   *Checkable:* the probe wording appears in quotation marks in the body; the
   judge template, classifier template and task prompts appear in a numbered
   appendix.

8. **Report the judge's agreement with humans next to the human-human agreement.**
   4 of 19 judge papers do this explicitly (2306.05685: 85% vs 81%; 2305.14387: 65%
   vs 66%; 2310.08491: 0.897 vs 0.882; 2305.17926: 71.7% and κ=0.54 as the human
   ceiling). *Checkable:* every judge-agreement number in the paper has a
   human-human number printed adjacent to it.

9. **Run and report a position-or-ordering-bias check whenever the judge sees two
   items.** 3 of 19 report reversal rates and a correction (2306.05685, 2404.13076,
   2305.17926). *Checkable:* if any comparison is pairwise, the paper reports the
   reversal rate and the swap-and-average or swap-and-tie rule applied.

10. **Run and report a self-preference check whenever the judge model is also a
    subject model.** 3 of 19 do (2303.16634 §4, 2404.13076, 2406.18403 §4).
    *Checkable:* the paper states whether judge scores differ for outputs from the
    judge's own family, with a number.

11. **Run and report a length or verbosity check whenever the outcome scale can
    reward elaboration.** 2 of 19 do (2406.04770 §3.2 length penalty; 2310.08491
    App. F). *Checkable:* the paper reports the correlation between output length
    and judged score, or a length control.

12. **Validate a derived classifier component-by-component on a hand-annotated
    sample, and state the direction of residual error.** 4 of 19 interpose an
    automatic labeller and all four validate it. Laban's form is the template:
    per-component accuracy table, overall success rate, and "these errors
    disfavored the assistant model in less than 2% of the conversations"
    (2505.06120 §3.2). *Checkable:* the classifier section reports (a) sample size
    hand-checked, (b) per-component accuracy, (c) which direction the errors push
    the headline estimate.

13. **State what classifier accuracy would have been sufficient, before reporting
    what was achieved.** 1 of 19 does (2311.08516 §5.1, simulating classifiers at
    each accuracy level to find the break-even). *Checkable:* the reader can tell
    whether the achieved accuracy is enough for the inference drawn from it.

14. **Say how annotators were recruited, how many, how they were paid, and how
    disagreements were resolved.** 11 of 19 report new human annotation; the ones
    that report all four elements are 2306.05685, 2305.14387, 2305.01937,
    2310.08491. *Checkable:* the human-validation paragraph answers who, how many,
    paid what, aggregated how.

15. **Report an agreement statistic appropriate to the scale, and name it.**
    Krippendorff's α for multi-rater ordinal (2311.08516), Cohen's κ for two-rater
    categorical (2406.18403), Scott's π where chance correction matters
    (2406.12624), percent agreement alongside a chance-corrected statistic
    (2306.05685). *Checkable:* every agreement number states the statistic, the
    number of raters, and the scale type.

16. **State the randomization and blinding of the annotation.** 4 of 19 state
    order randomization explicitly (2310.08491, 2305.17926, 2306.05685,
    2303.17651). *Checkable:* the annotation paragraph says whether order was
    randomized and whether condition was concealed.

17. **Release code and data at the point of first use, with a URL in the methods
    text.** 12 of 19. *Checkable:* the section contains at least one repository
    URL, placed next to the artifact it releases.

18. **State the cost.** 10 of 19 report money, compute hours, or both, usually in
    one sentence at the end of the scale paragraph. *Checkable:* the reader can
    tell what the experiment cost to run and what the annotation cost to collect.

19. **State the scale as factors then total.** 8 of 19 use the form "N tasks × M
    models, K runs each, totaling T". *Checkable:* the sentence names every factor
    and ends in one total, and the units of observation (trials, turns,
    annotations) are named separately and never conflated.

20. **Attach justification to the choice, in the same sentence.** Every paper in
    the corpus does this; none has a defensive subsection inside the methods.
    *Checkable:* no paragraph in the section begins by raising an objection.

21. **Write in the first-person plural, past tense for actions.** 2.3 : 1 in
    favour of "we" over passive across the corpus; median 21 uses per 1,000 words.
    *Checkable:* the section's "we" count divided by its word count, times 1,000,
    is between 9 and 32.

22. **A pre-committed threshold is an asset. State it as a design feature in the
    methods, not as a result.** 0 of 19 papers report one. *Checkable:* if the
    paper has a pre-specified success bar, it appears in the methods section where
    the measure is defined.

---

## Constructions to avoid, with evidence

1. **Reporting a judge score with no human anchor.** The corpus never does this.
   Every judge paper prints a human-human comparison, a bootstrapped upper bound
   (2406.18403 App. C), or an explicit ceiling (2305.17926 §4.3, human average
   71.7% and κ=0.54). A correlation of 0.505 stated alone reads as a number the
   author has no way to interpret.

2. **Naming a model without a version.** Panickssery 2404.13076 names "GPT-3.5"
   and "GPT-4" with no snapshot and this is the corpus's weakest reproducibility
   reporting; it is not the pattern to follow. Contrast the same paper's careful
   ordering-bias reporting.

3. **Putting a limitation inside the methods as a concern-then-rebuttal.** No
   paper in the corpus builds an objection-and-answer structure inside the methods
   section. Limitations live in a Limitations section (2505.06120 §9, 2310.13548,
   2311.08516, 2404.13076 §5.2, 2305.01937). Where a caveat must appear at the
   point of use it is one flat sentence (2310.08491 §4.1).

4. **A metric defined in the methods but never used, or used but never defined.**
   Laban defines exactly three metrics in §4.2 and uses all three throughout.
   Prometheus lists three correlation metrics in §4.1 and reports all three. The
   corpus norm is a short, closed list.

5. **A total trial count that mixes units.** MINT distinguishes test examples
   (7,405), turns (5), and inference runs (37K) in one sentence (2309.10691 §2.2).
   Laban distinguishes instructions (600) from simulated conversations (200,000+)
   (2505.06120 §5). Writing "720 trials (3,600 model-turn observations)" follows
   this norm; writing a later percentage over an unstated denominator does not.

6. **An unlabelled sample restriction.** Tyen states the stratification, the
   proportions, the reason, and the analytic correction in four sentences
   (2311.08516 §2.1.1). A subset introduced without its selection rule and its
   consequence for inference is the construction to avoid.

7. **Justifying a parameter by convention alone.** "consistent with standard
   practice" appears nowhere in the corpus. Papers give the operative reason:
   "to provide evaluation across different decoding algorithms" (2310.01798), "to
   increase the model's determinism" (2303.16634), "we found a higher temperature
   to be helpful in encouraging output diversity" (2305.14387 §4.1).

8. **Reporting only the variant that worked.** MT-Bench reports the few-shot judge
   that improved consistency from 65.0% to 77.5% and then says it was not adopted,
   with three reasons (2306.05685 §3.4). Tyen reports that its own trained
   classifier failed to clear the bar it had established (2311.08516 §5.2). The
   corpus norm is to report the discarded variant.

---

## Checklist

Design and scale
- [ ] Top-level heading names the instrument or phenomenon, not "Methods"
- [ ] Section is 18% to 34% of body words
- [ ] At most five numbered subsections; remainder are bold run-in heads
- [ ] Scale stated as factors then one total; every unit of observation named separately
- [ ] Repeat count (runs per cell) justified in one clause
- [ ] Every design choice's justification sits in the same sentence as the choice

Models and parameters
- [ ] Every model named in the body resolves to a snapshot ID somewhere
- [ ] Version table in an appendix if more than about six models: Short Form / Name / Version / Provider
- [ ] API access window given as calendar dates
- [ ] Temperature stated for every generation step, with a reason
- [ ] Judging temperature distinguished from generation temperature
- [ ] Maximum output length stated

Prompts
- [ ] The manipulated probe appears verbatim, in quotation marks, in the body
- [ ] Judge template, classifier template and task prompts in a numbered appendix
- [ ] Appendix carries a prompt heading a reader can find (`Appendix X Prompts`)

Judge
- [ ] Judge-human agreement printed next to human-human agreement
- [ ] Candidate judges enumerated, with the losers' numbers reported
- [ ] Position or ordering bias measured and corrected, if any comparison is pairwise
- [ ] Self-preference checked, since judge and subject families overlap
- [ ] Length or verbosity effect on score reported
- [ ] Output format constrained, and parse failures reported

Classifier
- [ ] Hand-annotated validation sample size stated
- [ ] Per-component accuracy reported
- [ ] Direction of residual error stated relative to the headline estimate
- [ ] Sufficiency bar stated before achieved accuracy

Human annotation
- [ ] Number of raters, recruitment route, expertise
- [ ] Payment and time per item
- [ ] Order randomized, condition concealed, both stated
- [ ] Aggregation rule stated
- [ ] Agreement statistic named, with rater count and scale type
- [ ] Guidelines released; interface shown if the task is unusual

Reproducibility
- [ ] Repository URL at the point of first use
- [ ] Cost stated (money, compute, or both)
- [ ] Contamination or leakage addressed if tasks are drawn from public data
- [ ] Determinism claim not made where it cannot hold

Voice
- [ ] "We" density between 9 and 32 per 1,000 words
- [ ] Past tense for actions, present for design properties
- [ ] No objection-then-rebuttal paragraph anywhere in the section

---

## How this paper's current methods section measures up

Read: `paper/sections/methods.tex`, 1,494 words, 8 `\subsection` calls and 8
`\paragraph` run-in heads. Body across `introduction_v2`, `related_work_v2`,
`methods`, `results_v2`, `discussion`, `conclusion` is 7,334 words, so the section
is **20.4% of body**. Appendix (`paper/sections/appendix.tex`, 1,384 words)
contains zero occurrences of "prompt", "temperature", "version", "snapshot",
"accessed" or "API".

### What already meets or exceeds corpus norms

- **Length share.** 20.4% sits inside the 18%–34% band and near the corpus median
  of 26%. No cutting needed on length grounds.
- **Scale statement.** "6 models × 40 scenarios × 3 runs = **720 trials** (3,600
  model-turn observations)" is more explicit than any of the 19. It names the
  factors, gives the product, and separates the two units of observation, which is
  the Laban and MINT convention (Rule 19) done better than either.
- **Judge selection reported as a competition with losers named.** "We then ran
  each of six candidate models as evaluator on the same samples and selected the
  model with highest human-mean correlation. Claude Sonnet 4 was selected […] The
  next-best candidate (DeepSeek V4) achieved r = 0.340; GPT-4o achieved only
  r = 0.140." Only Bavaresco 2406.18403 and Thakur 2406.12624 enumerate judges this
  way, and neither frames it as a selection procedure. Keep this.
- **A pre-committed success bar.** "We set a success bar in advance of ≥65% Turn 1
  preference with a 95% CI excluding 50%; this bar was not cleared." Zero of 19
  papers report anything comparable. This is the single most distinctive
  methodological feature the paper has and it is currently buried in the last
  sentence-cluster of a `\paragraph` inside `\subsection{Sub-experiments}`.
- **Reporting a validation that failed.** Both the unmet success bar and the
  keyword-classifier failure are reported rather than suppressed, matching the
  2306.05685 §3.4 and 2311.08516 §5.2 norm.
- **Classifier validated against human review with a correction rate.** "Ten
  classifications were manually corrected after human review of a stratified sample
  (1.4% correction rate)" is the right kind of number.
- **Stripping validated by a contrast, not an assertion.** "two human annotators
  rating stripped content agreed with the LLM judge at κ = 0.569, compared to
  near-chance agreement (κ between −0.07 and +0.02) on unstripped content." The
  before-and-after contrast is stronger evidence than a single κ and has no direct
  parallel in the corpus.

### Where it falls short of the corpus

**Model reporting (Rules 4, 5).** The `\paragraph{Models.}` line gives friendly
names and vendors only: "Claude Sonnet 4 (Anthropic), GPT-4o (OpenAI), Gemini 2.5
Flash (Google), Llama 3.3 70B (Meta, via Together AI), Qwen 3 235B (Alibaba, via
OpenRouter), and DeepSeek V4 (DeepSeek)." No snapshot IDs, no access dates, no
version table anywhere in the paper. 12 of 19 corpus papers give snapshot IDs and
the two multi-model papers closest in shape (2505.06120 with 15 models, 2406.12624
with 10) both carry an appendix version table. With six models and six vendors
this is the largest single gap.

**Prompts (Rule 7).** The probe is quoted verbatim in the body, which is right.
But the judge prompt, the classifier prompt, the targeted-feedback critique
prompt, the self-reflection prompt and the regex patterns used for stripping are
all referred to and none is reproduced anywhere. 12 of 19 corpus papers carry a
prompt appendix; this paper has none. "validated regex patterns matching common
preamble and postamble phrases" is not a specification a reader can re-implement.

**Decoding parameters (Rule 6).** Temperature 1.0 is given for generation, with a
reason, and temperature 0 for the judge and classifier. Missing: maximum output
length, and any statement about how many API calls or which providers'
non-determinism applies. The generation-temperature justification currently reads
"consistent with standard practice for open-ended generation," which is the one
construction the corpus never uses (Constructions to avoid, item 7). Laban's
sentence is the model: state the property the choice buys.

**Judge validation is incomplete (Rules 9, 10, 11).** The paper reports
human-correlation and a selection procedure but runs none of the three standard
bias checks. Two are load-relevant here and their absence is exploitable by a
reviewer:
- *Self-preference*: Claude Sonnet 4 is both the judge and one of the six subject
  models. No corpus paper leaves this unaddressed when it arises; 2404.13076,
  2303.16634 §4 and 2406.18403 §4 all measure it. This needs a number.
- *Length*: the six-level scale has an "Overdone" level that by construction
  penalises elaboration, and the paper's own stripping analysis shows revision-side
  outputs are systematically longer and more wrapped. The relationship between
  length and score is currently asserted through the stripping fix rather than
  measured.
- *Position*: applies to the reversibility pairwise comparison. The methods say
  "position-randomized", which is the aggressive correction MT-Bench names but does
  not report the reversal rate. One sentence would settle it.

**Human-annotation reporting is thin (Rules 14, 16).** "three human raters
independently score each on the same six-level scale" is all the reader gets. No
recruitment route, no expertise, no payment, no time per item, no aggregation rule
for the calibration sample, no guidelines, no interface. Every one of the four
corpus papers that reports human annotation well (2306.05685, 2305.14387,
2305.01937, 2310.08491) supplies all of these. The reversibility annotators
("Two human annotators independently compared…") are reported at the same
thinness. Note also that `annotator-ui/` and `reversibility-annotator/` exist in
the repository and are never mentioned in the methods, and there is no repository
URL anywhere in the section (Rule 17).

**No cost statement (Rule 18).** 10 of 19 report it. 3,600 outputs scored twice
across six vendors plus a targeted-feedback condition is an experiment whose cost
the reader will want.

**A defensive construction inside the methods (Rule 20, Constructions item 3).**
`\subsection{Design}` ends: "Our design cannot fully separate the effect of the
revision act from the prompt that offers it; a no-probe control would be needed to
isolate the revision mechanism alone." No paper in the corpus raises a missing
control against itself inside the methods. This belongs in Limitations. The same
applies to the mid-subsection concession in the Edge Case Framework item 1 ("This
subset conditions on a post-treatment variable […] introducing potential selection
bias") and to the closing sentence of Human Validation ("ordinal means should be
interpreted with the moderate reliability in mind"), which is a reader instruction
rather than a design statement.

**Findings asserted inside the methods.** "The classifier gap itself is a finding:
models frequently produce verbose responses that mimic revision without
substantive content change." That is a result. No corpus methods section states
one. Move it.

### Structural recommendation

The section currently runs eight subsections in the order Design, Response
Classification, Blind Evaluation, Meta-Commentary Stripping, Edge Case Framework,
Metrics, Sub-experiments, and the two preliminary studies. Two problems: the
preliminary studies that motivate the probe design appear last, roughly 1,100
words after the probe is introduced and its neutrality justified by
forward-reference; and Metrics arrives after the four measurement-construction
subsections that produce the inputs those metrics consume.

A reordering that matches corpus practice (Laban's construct-then-tasks-then-scale
sequence, WildBench's curation-then-evaluation split, Thakur's six run-in heads)
and clears Rules 1, 3, 19 and 20:

1. `\section{Measuring Revision Under a Neutral Probe}` (Rule 1: name the
   instrument). Open with the two preliminary studies compressed to one paragraph
   as the reason the balanced probe exists, then the probe verbatim, then the
   crossing and total, then Models and Scenarios as run-in heads. Absorbs the
   present Design subsection and the two preliminary studies.
2. `\subsection{Response Classification}` unchanged in substance, with the
   "finding" sentence removed and per-component validation numbers added.
3. `\subsection{Blind Evaluation}` covering the scale, the 6→2 recode, judge
   selection, and the three bias checks as run-in heads (`Judge selection.`
   `Self-preference.` `Position and length.`).
4. `\subsection{Meta-Commentary Stripping}` unchanged, with the pattern set moved
   to an appendix and referenced.
5. `\subsection{Metrics}` moved here, after everything it consumes is defined.
6. `\subsection{Contrast Conditions}` for targeted feedback, self-reflection and
   reversibility, with the pre-committed success bar stated at the top of the
   reversibility paragraph rather than at the end.
7. Edge Case Framework: keep the four controls, but move the two
   selection-bias concessions to Limitations and state each control as what it
   does.

New appendix material required: a model version table (Short Form / Name /
Version / Provider / Access dates), a prompts appendix (probe, judge, classifier,
critique, self-reflection, stripping patterns), an annotation appendix
(recruitment, payment, guidelines, interface), and a cost line.
