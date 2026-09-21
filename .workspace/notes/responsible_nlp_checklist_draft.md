# Responsible NLP Research checklist — draft answers

Drafted 2026-09-21 against the current ARR form (aclrollingreview.org/responsibleNLPresearch,
retrieved 2026-09-21): five parent questions, A through E, with 18 subquestions.

Every answer below is sourced. Where the honest answer is **No**, the entry says what would
make it Yes and roughly what that costs, because an incomplete or misleading checklist is a
named desk-reject ground and a false Yes is worse than an honest No.

**Nine answers are already Yes on the paper as it stands. Six are No and are cheap to fix.
Three are judgment calls that are yours.**

---

## A. For every submission

### A1. Did you describe the limitations of your work? — **YES**

Section: `Limitations` (unnumbered, after the Conclusion). Eight numbered points covering
panel composition (Llama 45 of 50), evaluator self-judging, moderate inter-rater reliability,
temperature 1.0 only, the 40 tasks being a convenience sample, probe priming, small per-domain
cells, and the blind comparison not clearing its pre-set bar.

Nothing to do. This is one of the stronger limitations sections I have read against the corpus.

### A2. Did you discuss any potential risks of your work? — **JUDGMENT CALL**

Section: `Ethics Statement` (in `main.tex`, before the bibliography).

What it covers: human evaluation by three raters, no personal data, synthetic scenarios, no
sensitive content, no release of outputs mistakable for human text, and the provenance of
pricing data.

What the form asks for that it does not cover: harmful uses, dual use, environmental impact,
and impacted stakeholders. The form's own guidance says reviewers will not penalise
transparency.

**Your call.** Answering Yes is defensible as written. If you want it stronger, the honest
additions are that the work is diagnostic rather than generative (it produces no model or
capability that could be misused), and the compute footprint, which is small and now
quantified under C1.

**One error, now fixed (2026-09-21):** the Ethics Statement said the scenarios span "code, data
logic, analysis, and writing tasks" where there are five domains. It now reads "code, data
logic, analysis, writing, and creative writing tasks", matching Table 1 and Methods §3.1.

---

## B. Did you use or create scientific artifacts? — **YES, both**

**Used:** six commercial LLM APIs. **Created:** 40 task prompts across five domains, 720
five-turn conversations (3,600 model-turn outputs), human ratings on 64 stratified samples and
50 pairwise comparisons, and the STET diagnostic.

### B1. Did you cite the creators of artifacts you used? — **NO**

`sections/methods.tex` contains **zero citations**. The six models are named with their
providers in §3.1 (Claude Sonnet 4, GPT-4o, Gemini 2.5 Flash, Llama 3.3 70B, Qwen 3 235B,
DeepSeek V4 Flash) but nothing is cited, and no software package is cited either.

To make this Yes: cite the model cards or technical reports for the six models, and the
packages the analysis uses (scipy, numpy, pandas). Exact pinned model identifiers are already
in `scripts/config.py` and should go in the paper:

| paper name | identifier used |
|---|---|
| GPT-4o | `gpt-4o-2024-11-20` |
| Claude Sonnet 4 | `claude-sonnet-4-20250514` |
| Gemini 2.5 Flash | `gemini-2.5-flash` |
| Llama 3.3 70B | `meta-llama/Llama-3.3-70B-Instruct-Turbo` (via Together) |
| Qwen 3 235B | `Qwen/Qwen3-235B-A22B-Instruct-2507-tput` (via Together) |
| DeepSeek V4 Flash | `deepseek-v4-flash` |

Dated identifiers matter here beyond the checklist: "GPT-4o" without a date is not reproducible,
because the endpoint moves.

### B2. Did you discuss the license or terms for use/distribution? — **NO, half fixed**

**Decided 2026-09-21: CC BY 4.0 for the data, MIT for the code.** `LICENSE` now states the
split (data under CC BY 4.0 with attribution and change indication; code under MIT; the
manuscript under neither).

Two things still open:

- **The copyright line reads "Copyright (c) 2026 Liam Neild".** If Ali's co-authorship is
  confirmed, decide then whether he joins it. Do not change it before he has agreed to be an
  author.
- **The paper still says nothing about licensing**, which is what B2 actually asks. One
  sentence in the Ethics Statement or the appendix covering both the released licences and
  the fact that the six models were accessed through their providers' paid APIs under those
  providers' terms. That sentence is yours to write; it also answers B3.

### B3. Did you discuss if use was consistent with intended use? — **NO**

Not stated anywhere. The substance is straightforward: all six models were accessed through
their providers' paid APIs for research use, and the study generates synthetic workplace
scenarios rather than eliciting anything the terms restrict.

### B4. Did you discuss steps to check for identifying information or offensive content? — **PARTIAL**

The Ethics Statement asserts no personal data and no sensitive content. It does not say how
that was checked.

The honest description is that the scenarios were authored rather than scraped, so the
question is one of construction rather than detection. Worth saying explicitly, because
"authored, not collected" is a complete answer to B4 and reads as evasive if left implicit.

### B5. Did you provide documentation of artifacts? — **PARTIAL**

Table 1 gives the five domains with 8 scenarios each and example tasks. **The language of the
data is never stated.** The form asks for this specifically and it is a common reviewer
complaint. All tasks and outputs are English.

### B6. Did you report relevant statistics? — **YES**

720 trials, 3,600 model-turn outputs, 2,880 post-Turn-1 classifications, Table 1's per-domain
counts, per-turn n in Table 2 and Table 12, and per-domain Turn-5 cells in Table 13. There is
no train/test/dev split because nothing is trained.

---

## C. Did you run computational experiments? — **YES**

### C1. Did you report model parameters, computational budget, and infrastructure? — **NO**

Nothing on compute appears in the paper. It is all API inference, no training and no GPUs, so
the honest report is small and worth stating plainly:

- **Parameter counts:** published for three (Llama 3.3 70B; Qwen 3 235B with 22B active;
  DeepSeek V4 Flash undisclosed) and not published for GPT-4o, Claude Sonnet 4 or
  Gemini 2.5 Flash. Say so rather than omitting the row.
- **Infrastructure:** hosted APIs only. No local GPU use. No training or fine-tuning.
- **Budget, measured:** the 720 Study 3 generation trials consumed **3,016,008 input tokens and
  1,050,833 output tokens** (computed 2026-09-21 from `token_counts` in `worker_trials.jsonl`).
  The evaluation, targeted-feedback and stripping stages do **not** record token counts, so the
  total across the project is higher and is not recoverable from what was saved. State the
  measured figure and say what it excludes; do not estimate the rest.
- **Scale of the other studies:** Study 1 is 3,840 primary trials (3,932 scored with pilots),
  Study 2 is 1,728 by design and 1,813 analysed.
- Output was capped at 8,192 tokens for generation and 512 for judging.

### C2. Did you discuss experimental setup, hyperparameter search, and best values? — **YES**

Methods §3.1 states temperature 1.0 for generation, with the reason (output diversity, avoiding
low-temperature ceiling effects), and §3.3 states temperature 0 for the evaluator. **No
hyperparameter search was run**, which is itself the correct answer and should be stated rather
than left blank: there is nothing tuned, so there is no tuning set and no risk of selection on
the outcome.

### C3. Did you report descriptive statistics about results? — **YES**

Exact test statistics throughout with named tests and n: Wilcoxon signed-rank with W and exact
p, bootstrap and exact binomial confidence intervals, sign tests, Mann-Whitney U with
rank-biserial effect sizes, Bonferroni within-model and Benjamini-Hochberg across the analysis.
Error bars on Figures 2, 6 and 8. Single-run reporting is not an issue because every estimate
pools three runs per cell.

### C4. Did you report implementation details for existing packages? — **NO, half fixed**

`requirements.txt` now exists, derived from the actual imports across `scripts/` and `paper/`
by ast parse rather than a pip freeze, so it lists direct dependencies only: numpy, scipy,
pandas, statsmodels, scikit-learn, matplotlib, seaborn, pillow, the three model-API clients,
python-dotenv, tqdm and playwright.

**Its header says plainly that the pinned versions are the authoring environment on
2026-09-21 and not the versions that produced the published numbers**, because the environment
was never pinned at the time. That is the honest statement and it should not be upgraded into
a provenance claim in the paper.

`textstat` is imported by two readability scripts and is not installed, so those two do not
currently run. No number in the paper depends on them.

Still to do: the paper itself names no package and no version. One appendix line covering the
analysis stack answers C4.

---

## D. Did you use human annotators or research with human participants? — **YES**

Three raters: the first author and two research assistants, anonymised in the paper as Rater
A/B/C. Two tasks: quality rating on 64 stratified samples, and 50 blind pairwise comparisons.

### D1. Did you report full text of instructions given to participants? — **PARTIAL**

The pairwise task's instructions survive verbatim in
`data/study3/human_validation/INSTRUCTIONS.md` (forced choice, no ties; judge on task
fulfilment, completeness, correctness, clarity; do not treat length as quality; 30 to 60
seconds per pair). That text is short enough to reproduce in the appendix as is.

The rating task's rater-facing instructions are **not separately preserved**. The six-level
rubric exists as the evaluator prompt in `scripts/study3/phase2_evaluator.py`, and the paper
paraphrases it in §3.3, but whether the raters saw that exact wording is not recorded. Do not
claim they did.

### D2. Did you report information about recruitment and payment adequacy? — **ANSWERED 2026-09-21**

**Neither rater was compensated.** Both are colleagues who agreed when asked. There was no
recruitment platform, no payment, and no wage question to assess, which is the honest answer
and a common one for annotation done by collaborators rather than crowdworkers.

The Ethics Statement already says the raters "participated voluntarily", which is accurate but
does not state the absence of payment. The form asks for it, so one clause should say so
plainly: three raters, the first author and two colleagues, unpaid and not recruited through a
platform.

Do not dress this up. Unpaid annotation by collaborators is normal and defensible; unpaid
annotation described as though it were a managed recruitment is not.

### D3. Did you discuss whether and how consent was obtained? — **NO**

Not documented anywhere. For two named collaborators rating synthetic text this is a short
statement, not a procedure.

### D4. Was the data collection protocol approved by an ethics review board? — **NO**

No IRB record exists in the project. Answering No is correct and normal here: no human-subjects
data was collected, the raters assessed machine-generated text, and this is the kind of study
that is typically exempt or not human-subjects research at all.

**Worth confirming with Emory rather than asserting.** The form explicitly notes that lack of
approval does not remove the obligation to discuss societal impact, which A2 covers.

### D5. Did you report demographic and geographic characteristics of annotators? — **NO**

Not reported. The form wants this, and it wants you to say whether characteristics were
self-reported or inferred. Three raters at one US university is the substance; say only what
the raters agree to and mark it self-reported.

---

## E. Did you use AI assistants in your research, coding, or writing? — **YES, must disclose**

This is not optional and it is the question most likely to be answered carelessly. The
disclosure must be accurate about scope. What is true of this project, as far as the repo
shows: AI assistance was used in analysis code, figure generation, verification sweeps and
editing, while the research questions, design and prose are the authors'.

**Write this one yourself.** It is a statement about your own process, I am a party to it, and
an inaccurate scope claim here is the kind of thing that is both easy to avoid and very bad to
get wrong. The ACL publications ethics policy on authorship is the governing document.

---

## What to do next, in order

**Six No answers, roughly a half-day in total:**

1. `LICENSE` and a licence sentence (B2) — your decision on which licence.
2. Model citations and dated identifiers in Methods (B1) — mechanical, and improves
   reproducibility independent of the checklist.
3. A compute paragraph (C1) — the numbers are measured and above.
4. `requirements.txt` with confirmed versions (C4).
5. One sentence each for B3, D3, D5.
6. Fix the four-domain / five-domain error in the Ethics Statement (A2).

**Three that are yours alone:** the A2 risk scope, the D2 compensation fact, and the E
disclosure.

**One thing to confirm externally:** whether Emory requires an IRB determination for D4.

Most of this lands in the appendix or the Ethics Statement, both outside the 8-page body, so
the page budget is not at risk. The model citations in Methods are the exception and will cost
a few lines inside the body.
