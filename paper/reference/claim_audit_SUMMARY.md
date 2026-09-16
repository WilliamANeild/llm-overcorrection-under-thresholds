# Claim verification, consolidated

Run 2026-09-05 across four agents. Every citation-bearing sentence in the live build was
checked against the full text of each work it cites. Per-pair evidence, with verbatim
quotations and retrieval dates, is in `claim_audit_chunk1.md` through `claim_audit_chunk4.md`.

## Counts

| | chunk 1 | chunk 2 | chunk 3 | chunk 4 | total |
|---|---|---|---|---|---|
| pairs checked | 15 | 11 | 15 | 19 | **60** |
| clean | 8 | 4 | 6 | 6 | **24** |
| not clean | 7 | 7 | 9 | 13 | **36** |

24 of 60 clean. The same 40% rate as the metadata audit, on a different failure mode.

---

## Class A. The source tested this claim and found the opposite

The most dangerous class. Not an overstatement: the cited paper ran an experiment
designed to answer this question and got the other answer. A reviewer who knows the work
sees it immediately.

**`laban2025lost` cited for accumulation across turns** (three separate sentences: 1.9,
2.4, 4.7). Laban's Section 6.3 gradual-sharding experiment varies shard count from 2 to 8
at fixed task complexity precisely to test accumulation, and reports a step rather than a
ramp: "the granularity at which information is specified does not majorly impact
reliability." Two turns costs as much as eight. The 39% drop is real; the mechanism
attributed to it is not the authors'. They attribute it to unreliability (+112%),
premature answers and over-reliance.

**`fanous2025syceval` cited for sustained multi-turn pressure strengthening sycophancy**
(4.1). Its preemptive, no-history condition scored *higher* than the in-context one,
61.75% against 56.52%.

**`perez2023discovering` cited to locate sycophancy in instruction tuning** (3.7). The
paper reports sycophancy is "similar for models trained with various numbers of RL steps,
including 0 (pretrained LMs)."

**`tsui2025selfcorrection` cited unqualified for "models"** (3.2). Measured on 14
non-reasoning models; the paper explicitly finds reasoning models show "a small, even
negative" blind spot, which inverts the result for the model class this paper studies.

**`bucinca2021trust` and `bansal2021whole` cited for displayed confidence raising
acceptance** (2.6). In both, displayed confidence is the control rather than the
manipulation. Buçinca's uncertainty condition showed no significant difference; Bansal's
confidence-adaptive strategy *reduced* agreement when the AI was uncertain.

## Class B. Sentences where no cited source supports the claim

Four sentences currently have no surviving support at all.

**Intro 1.5, vendor guidance encourages users to iterate toward a better result.** Both
keys argue the opposite. The Anthropic anchor cited says "explicitly request it rather
than relying on the model to infer this from vague prompts." Every "iterate" in the
OpenAI guide is a developer iterating on a prompt, and the guide warns that vague prompts
are "more damaging to GPT-5."

**Related work 4.3, judges favour confident framing.** Supported by none of its four keys.
`panickssery2024llm` never uses the term "position bias"; `singhal2023long` studies RLHF
reward models rather than judges; `wu2023style` manipulates only factual errors, grammar
and length; `chen2024humans` covers emoji and markdown, and its authority bias is fake
citations.

**Related work 4.6, multi-turn coherence degrades with conversation length.** Both keys
fail. `zhang2020dialogpt` evaluated single-turn, and the coherence line is its own
introduction's motivation, cited there to Serban et al. 2017. `thoppilan2022lamda`
evaluates "up to 3 dialog turns" and reports no length-dependent degradation or topic
drift anywhere.

**Related work 4.4, enterprise inference spending.** `deloitte2026stateofai` carries no
spending figure; its only "double" refers to projects in production. `gartner2026agentic`
and `mckinsey2025stateofai` are both unreachable, and the Gartner 5-30x figure is about
tokens per task rather than spend.

## Class C. Overstatements and scope shifts

**`liang2023holistic` cited for models performing well on single-turn benchmarks** (1.1).
HELM's own findings say "most models are not particularly accurate... essentially chance
accuracy at 50.1%," on the 2022 model cohort. It does support the sentence's other half,
that evaluation takes a single-turn reference-scored form.

**`yang2025underspecification` cited for real user prompts being underspecified** (1.3,
2.2). The -22.6% degradation is solid, but the paper studies developer application prompts
and says the issue "is less significant for end users." Its prompts are author-constructed,
so it does not establish frequency in real user behaviour.

**`anthropic2025economicindex` cited with "increasingly"** (1.2, 2.1). This is the first
report in the series and has no time series. Later reports show the directive share rising
27% to 39% through August 2025, so the trend word may point the wrong way.

**`schemmer2023reliance` cited for a cost-benefit account of reliance** (2.7). A full-text
search returns zero hits for "cost", "cognitive effort", "verify", "heuristic" or
"dual-process". Its model is trust and self-confidence based. Vasconcelos alone carries
the sentence; Buçinca or Parasuraman and Manzey, both already cited nearby, would be the
right second citation.

**`chen2025overthinking` and `chen2024overthinking` cited for degradation** (3.5). The
mechanism-to-paper mapping is right: the Reasoning Completion Point is genuinely Wei et
al.'s, and variance-driven non-monotonicity is genuinely Ghosal's. The verb is wrong.
`chen2024overthinking` says redundant reasoning "contributes minimally to accuracy," never
that it degrades. And the degradation language in the other paper exists only in the
superseded v1; v2 removed it and now cites Ghosal for degradation instead.

**Smaller scope shifts:** `shinn2023reflexion` (3.4) supplies feedback from outside the
model and is named by Huang and Tyen as the confound, so its placement implies the
opposite of its role; `tyen2024llms` (3.2) benchmarks predominantly cross-model on
PaLM-2-generated traces and declines in a footnote to generalize to self-evaluation;
`zhang2024small` (3.3) is scoped to small LMs by its own title; `sui2025efficient` (3.6)
is organized around compute cost and does not list termination among its open directions;
`ye2024justice` (4.3) contains no formatting bias among its twelve; `laban2025lost` (1.2)
is not a workplace-task setting.

## Class D. Unreachable

`skitka1999automation` (2.5): Elsevier closed, ScienceDirect and ACM 403, no repository
copy, Unpaywall reports closed access. Parasuraman and Manzey, cited alongside, does
support both the "experts and novices alike" and "decades of studies" clauses verbatim,
and describes Skitka as testing nonpilots.

`gartner2026agentic`, `mckinsey2025stateofai`: see Class B.

## Already known

`claudecode2025loop` (1.12). Confirmed. Claude Code issue #27281 is a loop of stating
intent without calling any tool, with zero edits. VSCode issue #257885 does say "editing
the same file over and over" and is the source the claim needs, but it has no bib entry.

## What this means

These are not citation errors. The bibliography now points at the right papers; these
sentences say things those papers do not say. Roughly a third of the introduction and
related work asserts something its sources do not support, and in five places the cited
paper ran the experiment and got the opposite answer.

This is not fixable by re-citing. The sentences have to change to what the sources
actually establish, which in several cases is a weaker or different claim than the
argument currently leans on.


---

# Re-triage, 2026-09-16

The audit above was run 2026-09-05. The page cut and the introduction and related-work rewrites
have both happened since, so each flagged pair was re-checked against the **live** sentence
rather than the sentence that was audited. Evidence was re-read from the chunk files; nothing
below rests on inference about what a source says.

## Retired by the page cut (8 keys, no longer cited anywhere in the live build)

`tsui2025selfcorrection`, `deloitte2026stateofai`, `gartner2026agentic`, `mckinsey2025stateofai`,
`chen2025overthinking`, `chen2024overthinking`, `sui2025efficient`, `claudecode2025loop`.

This removes the whole of Class B item 4.4 (enterprise spending), the Class D industry pair, and
the `claudecode2025loop` miscitation. Those three TODO entries are discharged by deletion.

## Resolved by the rewrites (3 sentences)

**Intro, vendor guidance.** Audited as "vendor guidance encourages users to iterate toward a
better result," which both sources contradict. The live sentence now reads that this is "the
request vendor guidance is written against," which is what Anthropic ("explicitly request it
rather than relying on the model to infer this from vague prompts") and OpenAI (vague prompts
are "more damaging to GPT-5") actually say. The rewrite moved the claim onto the evidence.

**Related work, fluent presentation.** Audited as "displayed confidence raises acceptance," where
displayed confidence is the control rather than the manipulation in both papers. The live
sentence says "fluent presentation raises acceptance without improving discrimination," which is
Bansal's abstract almost verbatim: "explanations increased the chance that humans will accept the
AI's recommendation, regardless of its correctness." Buçinca's simple-explanation condition
performed worse than no AI on incorrect predictions, which is the same finding.

**Related work, sustained pressure.** Audited as "under sustained multi-turn pressure the effect
strengthens," which `fanous2025syceval` points against. The live sentence drops "strengthens."
What remains is carried: `xu2024earth` runs four-turn escalation with cumulative belief
alteration from 20.7% to 78.2%, and `fanous2025syceval` defines and measures regressive
sycophancy at 14.66%.

## Live and severe (1 sentence)

**Related work, multi-turn degradation.** "Early dialogue systems lose coherence through topic
drift rather than revision" `\cite{zhang2020dialogpt, thoppilan2022lamda}`. Both keys are NOT
SUPPORTED and the rewrite did not touch the part that fails. DialoGPT is evaluated single-turn by
its own abstract, never uses "topic drift," and on multi-turn behaviour points the other way
("able to deal with multi-turn generation better than an RNN counterpart"). Its coherence line is
its own introduction's motivation, attributed to Serban et al. 2017. LaMDA defines a
sensibleness metric but never measures it against conversation length, evaluates on dialogs of up
to 3 turns, and does not contain "topic drift." No re-citing of these two keys fixes this.

## Live and mild (3 decisions, no claim in danger)

**`singhal2023long` under a "judges" subject.** The paper studies RLHF reward models and training
dynamics, not LLM judges. It does use LLM annotators for win rates, so the scope shift is real
but narrow. Either move the key or let the sentence name reward models alongside judges.

**`skitka1999automation` unreachable.** Elsevier closed, no repository copy. `parasuraman2010complacency`,
cited in the same bracket, supports both the "experts and novices alike" and "decades of studies"
clauses verbatim and describes Skitka as testing nonpilots. Keeping it costs nothing; dropping it
costs nothing either.

**`ye2024justice` for formatting.** CALM quantifies 12 biases and none is a formatting bias,
though Verbosity Bias ("favor longer responses") is stylistic. Supported for "stylistic," not for
"formatting."

## Checked and clean

**`panickssery2024llm` with `koo2024benchmarking` for "self-preference and position biases."** The
2026-09-05 note that panickssery does not study position bias is correct, but `koo2024benchmarking`
carries it: CoBBLEr defines order bias and finds 11 of 15 models drawn to the first or last
option. One key per bias in a shared bracket is fair. No change needed.
