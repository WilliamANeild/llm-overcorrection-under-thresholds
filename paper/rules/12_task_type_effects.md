# Task type and domain effects in this literature

Retrieved 2026-09-02 (one addition 2026-09-03). N papers = 47 fetched and converted to running text; 39 read closely
enough to quote on task type; 8 fetched and checked but yielding nothing on the question
(listed under Limits).

Every paper below was fetched as full text from `arxiv.org/html/<ID>v1` and converted to plain
text locally. Abstracts were taken from `arxiv.org/abs/<ID>`. Nothing here is quoted from
memory. Where a quote comes from the abstract it is marked ABSTRACT; where it comes from the
body the section is named. Quotes preserve the source's own spelling, hyphenation and italics
as rendered.

**Note on versions.** All full texts are the arXiv v1 HTML. Where a camera-ready differs from
v1, the quotes describe v1, which is what was read. Two of the anchor papers (Huang 2310.01798,
Stechly 2310.12397) have later conference versions that were not fetched.

---

## Corpus

"Per-domain breakdown" records whether the paper reports results separately by task or domain
anywhere, and where that reporting lives.

| Paper (first author, short title) | arXiv ID | Task types covered | Per-domain breakdown reported | Finding on task type |
|---|---|---|---|---|
| Kamoi, *When Can LLMs Actually Correct Their Own Mistakes?* | 2406.01297 | survey; reasoning, knowledge, context-based generation, open-ended generation, MT, IR, prompt optimisation | yes, §2.3 task census and §7 "Tasks Suitable for Self-Correction" list; no numeric per-task table | task type is the paper's central conclusion: works where reliable external feedback exists |
| Huang, *LLMs Cannot Self-Correct Reasoning Yet* | 2310.01798 | GSM8K, CommonSenseQA, HotpotQA; plus CommonGen-Hard in §4 | yes, per-dataset tables in §3.2; §4 is a single-task table | scopes its negative claim to reasoning; allows style/safety/preference tasks as the exception |
| Madaan, *Self-Refine* | 2303.17651 | 7: dialogue response, code optimisation, code readability, math reasoning, sentiment reversal, acronym generation, constrained generation | yes, Table 3 in §5 is entirely per-task; Table 4/5 per-task iteration analysis in §6 | claims uniformity ("In all tasks"), then names one per-task exception (acronym generation) in §6 |
| Tyen, *LLMs cannot find reasoning errors* | 2311.08516 | 5 BIG-Bench tasks: word sorting, tracking shuffled objects, logical deduction, multistep arithmetic, Dyck languages | yes, every results table (5, 6, 7, 8) is per-task | opens the ABSTRACT with a style/quality versus logic contrast drawn from prior work |
| Stechly, *GPT-4 Doesn't Know It's Wrong* | 2310.12397 | 1: graph colouring (plus a derived `color_verification` domain) | n/a, single domain | single-domain by design; attributes the apparent iterative-prompting gain to a confound |
| Stechly, *Self-Verification Limitations* | 2402.08115 | 3: Game of 24, graph colouring, STRIPS planning | yes, per-domain tables | reports the effect as holding across all three domains |
| Laban, *LLMs Get Lost In Multi-Turn Conversation* | 2505.06120 | 6: code, database, actions, data-to-text, math, summary | yes, Table 1 in §6.1 is model × task; §6.1 prose reads the breakdown | headline effect uniform across tasks; magnitude "not uniform across domains" |
| Pan, *Automatically Correcting LLMs* (survey) | 2308.03188 | survey; factual correction, reasoning, code synthesis, open-ended generation, MT, summarisation | yes, §6 Applications is organised by domain; no numbers | organises the whole literature by application domain; names open-ended generation as the subjective case |
| Olausson, *Is Self-Repair a Silver Bullet for Code Generation?* | 2306.09896 | code only: HumanEval, APPS | yes, per-dataset and per-difficulty-subset | ABSTRACT reports gains that "vary a lot between subsets of the data" |
| Chen, *Teaching LLMs to Self-Debug* | 2304.05128 | code: Spider (text-to-SQL), TransCoder, MBPP | yes, per-benchmark throughout | ABSTRACT splits results by whether unit tests exist |
| Gou, *CRITIC* | 2305.11738 | 3 families: free-form QA, mathematical program synthesis, toxicity reduction | yes, per-dataset tables | ABSTRACT asserts uniform improvement across three unlike task families |
| Lin, *CriticBench* | 2402.14809 | 5 reasoning domains: mathematical, commonsense, symbolic, coding, algorithmic; 15 datasets | yes, RQ3 is a dedicated subsection §4.2.3 plus Figure 7 | ABSTRACT states a task-dependent variation as finding (2) of 4 |
| Jiang, *SELF-[IN]CORRECT* | 2404.04298 | multiple, incl. MT-Bench | yes, Table 4 per-task | reports one per-task exception against an otherwise uniform result |
| Sharma, *Towards Understanding Sycophancy* | 2310.13548 | 4 free-form text-generation tasks | yes | ABSTRACT asserts consistency across four tasks |
| Kwan, *MT-Eval* | 2401.16745 | 4 task categories | yes, §4.4 and Table 2 by category | gap "persists irrespective of the underlying capabilities of the models" |
| Wang, *MINT* | 2309.10691 | 3 task types: code generation, decision making, reasoning | yes, task-type rows throughout | reports a null on a model-family contrast |
| Dhuliawala, *Chain-of-Verification* | 2309.11495 | list questions, closed-book QA, longform generation | yes, per-task | "consistent performance improvement across all tasks" |
| Zhang, *SummIt* | 2305.14835 | summarisation | yes, per-dataset | "across all datasets, SummIt consistently demonstrates inferior ROUGE scores... while exhibiting significantly higher GPT evaluation scores" |
| Ji, *Mitigating Hallucination via Self-Reflection* | 2310.06271 | medical QA, 5 datasets | yes, per-dataset | "on all five datasets" |
| Chakrabarty, *Can AI writing be salvaged?* | 2409.14509 | literary fiction, creative non-fiction | yes, Figure 4(c) by domain | per-domain difference reported and explicitly hedged as not significant |
| Lee, *CoAuthor* | 2201.06796 | argumentative writing, creative writing | yes, results split by the two | a per-domain contrast reported with one arm not significant |
| Padmakumar, *Does Writing with LMs Reduce Content Diversity?* | 2309.05196 | argumentative essay writing | robustness split moved to Appendix C | reports a robustness null in an appendix table |
| Chakrabarty, *Art or Artifice?* | 2309.14556 | creative writing (short stories), TTCW rubric | yes, per-test | iterative self-revision named only as future work |
| Chakrabarty, *Creativity Support in the Age of LLMs* | 2309.12570 | creative writing, emerging writers | qualitative | qualitative study, no per-domain statistics |
| Saunders, *Self-critiquing models* | 2206.05802 | topic-based summarisation plus a mix of QA and summarisation | yes, Table 4 splits train/test by task type | "gaps are task-specific" |
| Welleck, *Generating Sequences by Learning to Self-Correct* | 2211.00053 | math, lexically constrained generation, toxicity reduction | yes, per-task | per-task sections, no cross-task contrast claim |
| Shinn, *Reflexion* | 2303.11366 | decision-making, reasoning, programming | yes, per-benchmark | per-benchmark reporting |
| Kim, *Language Models can Solve Computer Tasks* (RCI) | 2303.17491 | computer tasks, MiniWoB++ | yes, per-task | task-specific reward functions discussed, not task-type moderation |
| Weng, *Better Reasoners with Self-Verification* | 2212.09561 | arithmetic, commonsense, logical reasoning | yes, per-dataset | per-dataset reporting |
| Shridhar, *The ART of LLM Refinement* | 2311.07961 | math word problems | yes, per-dataset | decides when to refine, not which domain |
| Zheng, *Judging LLM-as-a-Judge* (MT-Bench) | 2306.05685 | 8 MT-Bench categories incl. writing, roleplay, coding, math | yes, per-category figures | judge agreement varies by category |
| Lee, *RefineBench* | 2511.22173 | 11 domains, 239 subjects; verifiable (exact match) and non-verifiable (free-form) task types | yes, "Domain Analysis." run-in heading in §5.2 plus Figure 5 (right) plus Appendix D Table 5 | "overall self-refinement performance is not significant across domains", with descriptive domain variation reported alongside |
| Hong, *Self-Verification Abilities in Logical Reasoning* | 2311.07954 | logical reasoning; 232 fallacy types in the FALLACIES dataset | yes, per-fallacy-category | scopes its negative claim to logical reasoning |
| Zhang, *Self-Contrast* | 2401.02009 | reasoning and translation | yes, per-task | ABSTRACT claims "generality" across two unlike task families |
| Han, *Confidence Matters* | 2402.12563 | 5 datasets, mathematical reasoning and logical consistency | yes, per-dataset, plus an explicit average | "IoE-based Prompt works better on mathematical reasoning and LLC tasks" |
| Liu, *LLMs have Intrinsic Self-Correction Ability* | 2406.15673 | multiple | yes | uniformity claimed across models, not across tasks |
| Zhang, *Understanding the Dark Side* | 2412.14959 | 1 simple task plus 3 complex tasks | yes, the simple/complex split organises the whole paper | effect uniform across task complexity; the failure mode differs by task type |
| McAleese, *LLM Critics Help Catch LLM Bugs* | 2407.00215 | code only | n/a, single domain | §7.10 states code was chosen because it is "an objective domain" |
| Valmeekam, *Can LLMs Really Improve by Self-critiquing Their Own Plans?* | 2310.08118 | planning only | n/a, single domain | single domain; the level of feedback does not change the result |

Eight further papers were fetched and searched but are not quoted on task type; they are named
under Limits so the count is checkable.

---

## What the literature concludes about task type (verbatim catalogue)

This section catalogues the papers that report task type as a **moderator** with a direction. The papers that report the opposite, an effect uniform across task types, are catalogued under "Reporting conventions" below, because their value here is as a register to copy. The verification-availability claim, which is the field's dominant statement about task type, has its own section immediately after this one.

### Papers that report task type as a moderator, with direction

**Lin et al. 2402.14809 (CriticBench), §4.2.3, "RQ3: Impact of Task Type", the whole finding
verbatim:** "**The model's critique and correction capability depends on whether the task focuses
on details or logic.** In Figure 7, we illustrate the variability in critique and correction
capabilities across various task types... Specifically, **the models exhibit weaker critique
performance in detail-oriented algorithmic tasks compared to their generation abilities**...
In contrast, **for mathematical reasoning and code generation tasks, their critique capabilities
surpass generation capabilities.** The ability to correct errors in algorithmic tasks is also
limited, even when the model answers correctly. For mathematical tasks requiring detailed and
logical reasoning, significantly higher accuracy in generation is needed for effective
corrections, **explaining the lack of improvement of math in the self-refine (Madaan et al.,
2023)**. Interestingly, **For the logic-focused Code Generation tasks, improvements are realized
as long as the model's generation performance surpasses that of the original responses'
performance. This result indicates that models, when performing critique and correction, are
easily disrupted by incorrect answers in tasks that focus on details, but not in those that
emphasize logic.**"
Conclusion, §5: "our analysis across different task types found that **models perform better in Q
and C for tasks focused on logic compared to those requiring attention to detail**."
Note that CriticBench's moderator is not objective-versus-subjective and not code-versus-prose. It
is **detail-oriented versus logic-oriented**, and on that axis code groups *with* mathematics, not
against it. Every one of its five domains is a reasoning domain; no open-ended or creative task
appears.

**Saunders et al. 2206.05802, §on scaling:** "Overall, this suggests that **gaps are
task-specific**, and it is not apparent whether we can close the CD gap in general." And the
mechanism offered: "**We believe the CD gap will generally be harder to close for difficult and
realistic tasks.** For example, on topic-based summarization the discriminator may be able to
identify the labeler who gave the answer based on their writing style... **This does not happen
with synthetic tasks.**"
ABSTRACT, hedged: "Larger models write more helpful critiques, and **on most tasks**, are better
at self-critiquing, despite having harder-to-critique outputs."

**Laban et al. 2505.06120, §6.1**, quoted in full under Reporting conventions: the effect is present on
every task; the magnitude is "**not uniform across domains**"; the support is a list of
model-by-task cells, with no moderation test.

**Zhang et al. 2412.14959** states a uniformity claim across a task-complexity contrast: "First, we
demonstrate that **self-correction can fail across a range of tasks, including both simple task
(e.g., simple factual question answering) and complex ones (e.g., decision making).**"
And the ABSTRACT differentiates the *mechanism* by task type rather than the effect: "We identify
intrinsic self-correction can (1) cause LLMs to waver both intermedia and final answers and lead
to prompt bias **on simple factual questions**; (2) introduce human-like cognitive bias **on
complex tasks**."
This is a useful third register: the effect is uniform, the failure *mode* differs by task type.

---

## Code and verifiable tasks versus open-ended generation

### The verification-availability claim: who makes it, on what evidence, how strongly

The claim is that self-correction helps where reliable external feedback or verification exists
and fails where it does not. It is made by seven papers in this corpus, at sharply different
strengths. Ordered from strongest to weakest.

**Kamoi et al. 2406.01297, the strongest statement, and the only one that is a survey conclusion
rather than an experimental result.**
ABSTRACT: "**self-correction works well in tasks that can use reliable external feedback**".
§1: "Specifically, (1) no prior work shows successful self-correction with feedback from prompted
LLMs in general tasks (§4), (2) **self-correction works well in tasks where reliable external
feedback is available** (§5), (3) large-scale fine-tuning enables self-correction (§6), and (4)
some tasks have properties exceptionally suitable for self-correction (§4)."
Bulleted in §1: "• **Self-correction is effective in tasks where reliable external feedback is
available.**"
§7, "Bottleneck is in Feedback Generation": "**Prior studies widely agree that LLMs can refine
their responses given reliable feedback (§5). However, generating reliable feedback on their own
responses is still observed to be challenging for LLMs without using additional information
(§4)**, although self-correction is motivated by the hypothesis that recognizing errors is easier
than avoiding them (Saunders et al., 2022)."
§7, "Tasks Suitable for Self-Correction", the operative taxonomy verbatim:
- "Intrinsic Self-Correction (§4) — **Tasks whose verification tasks are much easier than the
  original tasks** (e.g., tasks whose responses are decomposable or verifiable)"
- "Self-Correction with External Information (§5) — **Tasks for which external tools that provide
  reliable feedback exist (e.g., code generation)**"
- "Self-Correction with External Information (§5) — Tasks for which responses can be utilized to
  obtain useful information that is difficult to obtain before generating initial responses"
- "Self-Correction with Fine-tuning (§6) — Self-correction works in many tasks when large train
  data for self-correction is available"
§4, "Tasks in which Self-Correction is Exceptionally Effective": "Although prior studies show that
intrinsic self-correction is generally difficult, some tasks have properties that enable
self-correction. First, **tasks with decomposable responses**, whose feedback generation can be
reduced into easier tasks, allow to generate reasonable feedback only by prompting LLMs... Second,
**verifiable tasks, in which the correctness of the responses can be verified easily without
external information, are suitable for self-correction**... **These tasks are exceptionally
suitable for self-correction, but many real-world tasks do not satisfy these properties.**"
The evidence is a critical re-reading of the whole literature against a fairness checklist
(Table 4), not new experiments. The strength is unqualified: "works well", "is effective",
stated as a finding, not a hypothesis.

**Chen et al. 2304.05128, the cleanest quantitative evidence, inside a single domain.**
ABSTRACT: "**On the Spider benchmark where there are no unit tests to verify the correctness of
predictions**, Self-Debugging with code explanation consistently improves the baseline by 2-3%...
**On TransCoder and MBPP where unit tests are available**, Self-Debugging improves the baseline
accuracy by up to 12%."
This is the strongest single piece of quantitative support for the claim in the corpus, and it is
worth being precise about what it does and does not show: it compares three code benchmarks that
differ in whether unit tests exist, holding the domain (code) fixed. It is a
verification-availability contrast, not a domain contrast.

**Huang et al. 2310.01798 states the negative half strongly and the positive half by concession.**
Negative half, §5 Discussion: "**self-correction might not be effective when attempting to correct
responses for tasks in which LLMs find it challenging to identify errors in their initial
responses or assess the correctness of those responses.** For instance, in the reasoning tasks
studied in this paper, we did not observe any improvement through self-correction."
Positive half, same section, "Leveraging external feedback for correction": "However, **when we
leverage external feedback for correction, the narrative changes**. For instance, in the study by
Gou et al. (2023), it is demonstrated that LLMs, when interacting with various external tools such
as search engines and calculators, can more effectively verify and correct their responses. Chen
et al. (2023b); Olausson et al. (2023); Pan et al. (2023) show that **by using an executor and
unit tests to ascertain the successful operation of generated code, LLMs can improve their
generation and better solve reasoning tasks**."
And the other named exception, which matters for this paper because it is the subjective case:
"**Self-correction can be effectively employed to make responses align with specific preferences,
such as altering the style of responses or enhancing their safety** (Bai et al., 2022; Ganguli et
al., 2023; Madaan et al., 2023)."
Huang's own evidence is three reasoning datasets. The verification claim is asserted on other
people's evidence, cited, and the paper is explicit that it is doing so.

**Stechly et al. 2402.08115, the sharpest experimental separation of self-verification from sound
verification.**
ABSTRACT: "**We observe significant performance collapse with self-critique and significant
performance gains with sound external verification.**"
Body: "**Across all of our domains, this self-verification systems worsens performance.**" And:
"This setup gives substantial performance gains across all domains, but closer analysis shows that
the level of feedback doesn't seem to matter—as long as **the verifier is sound**, improvement
remains regardless of how much or how little feedback the LLM receives."
Evidence: three formally verifiable domains, GPT-4, with a sound verifier available by
construction. The contrast is verifier soundness, held within domains, not across them.

**Olausson et al. 2306.09896 locates the bottleneck in feedback, not in revision.**
ABSTRACT: "We hypothesize that this is because **self-repair is bottlenecked by the model's
ability to provide feedback on its own code**; using a stronger model to artificially boost the
quality of the feedback, we observe substantially larger performance gains. Similarly, a
small-scale study in which we provide GPT-4 with feedback from human participants suggests that
even for the strongest models, **self-repair still lags far behind what can be achieved with
human-level debugging**."
Body: "Replacing GPT-3.5's explanations of what is wrong with feedback produced by GPT-4 leads to
better self-repair performance, even beating the baseline, no-repair GPT-3.5 approach (50%→54% at
7000 tokens)."

**Tyen et al. 2311.08516, the same bottleneck, stated as a decomposition.**
ABSTRACT: "we show that **poor self-correction performance stems from LLMs' inability to find
logical mistakes, rather than their ability to correct a known mistake**... we test the correction
abilities of LLMs -- separately from mistake finding -- using a backtracking setup that feeds
ground truth mistake location information to the model. We show that this boosts downstream task
performance across our 5 reasoning tasks, indicating that **LLMs' correction abilities are
robust**."
This is the load-bearing result for the present paper's premise: revision capacity is intact; what
is missing is the signal about what to revise.

**Gou et al. 2305.11738 (CRITIC), the constructive version.**
ABSTRACT: "our research highlights **the crucial importance of external feedback in promoting the
ongoing self-improvement of LLMs**."
Body: "Nevertheless, **LLM's self-feedback has limited and task-specific performance compared to
human feedback** [6] and LLMs struggle with verification on truthfulness and reasoning
correctness."

**Pan et al. 2308.03188 (survey) states the availability condition domain by domain.**
§6.2, Reasoning Tasks: "**In most reasoning tasks, no good references from which outputs can be
sanity-checked are readily available** (Choi, 2023)."
Same section, on why arithmetic dominates the literature: "Among different types of reasoning, the
self-correction strategy has been well studied and implemented for arithmetic reasoning, as
outlined in Table 1. **One of the reasons for this skew is the relative ease of verifying
intermediate reasoning steps within arithmetic problems.**"
§6.3, Code Synthesis: "The aforementioned warnings, errors, or outputs are usually fed directly
back into the LLM to guide the code correction process. After all, **compiler failures are a
particularly strong signal that a piece of code will not work, having great utility in guiding LLM
self-correction.**"

### What the same literature says about the subjective and open-ended end

Two of the surveys treat open-ended generation as a distinct case, and both say the feedback there
is different in kind rather than absent.

**Pan et al. 2308.03188, §6.4, "Open-ended Generation", in full:** "In addition to handling pure
factuality issues, **self-correction can be applied to subjective qualities of the generated
text.** These interventions include post-hoc toxicity reduction, enhancing the narrative quality
in story generation (Yang et al., 2022b), and refining response generation in dialogues. **Given
the subjectivity involved in assessing the outputs, these studies often rely on detailed, natural
language feedback and employ an iterative refinement strategy for post-hoc refinement.**"

**Kamoi et al. 2406.01297, §11, "Unexplored Tasks", in full:** "**Difficulty of self-evaluation
differs from task to task (§4), while many studies assume that verification is consistently easier
than generation** (Saunders et al., 2022, e.g.). **We expect that there are unexplored tasks in
which intrinsic self-correction works well.** For example, **LLM-based evaluation is often studied
in open-ended text generation, such as dialogue generation, suggesting that reasonable model-based
feedback is available.**"
This is the most important sentence in the corpus for the present paper's positioning: the survey
that most strongly ties self-correction to verification availability explicitly declines to predict
that open-ended generation will fail, and names it as an open case where model-based feedback may
in fact be available.

**Kamoi's own task census, §2.3, verbatim, with the categories as he draws them:** "Self-correction
has been studied in **Reasoning**: arithmetic reasoning, code generation, proof generation, logical
reasoning, **Knowledge**: closed-book QA, **Context-based Generation**: dialogue generation, text
summarization, **Open-ended Generation**: conditional text generation, story generation,
detoxification, **Others**: machine translation, information retrieval, visual instruction
following, and prompt optimization."
Four of the present paper's five domains map onto Kamoi's categories; creative writing maps onto
"Open-ended Generation: ... story generation", for which he cites exactly one work.


### Does any paper find that CODE behaves differently from open-ended generation?

Not in the direction the question expects. Three findings bear on it, and they point three ways.

**Code is treated as the paradigm of the verifiable domain, and that is why it is studied.**
McAleese et al. 2407.00215, §7.10 "Why code", verbatim: "We focus on code because the domain has
several useful properties: ... **Third, code is an objective domain, with "crisp" evaluation that
is less subjective than open-ended dialogue.** Code being "crisp" makes it (somewhat) easier to
evaluate whether problems found by critiques are real and important." This is the clearest
statement in the corpus of the objective/subjective axis, and note what it is used for: a reason to
*choose* code as the study domain, not a finding about how code behaves under revision.

**Within code, the contrast that matters is verification availability, not the domain.**
Chen et al. 2304.05128 splits its own abstract on whether unit tests exist: 2-3% on Spider "where
there are no unit tests to verify the correctness of predictions", up to 12% "On TransCoder and
MBPP where unit tests are available". Olausson et al. 2306.09896, working entirely inside code,
finds that once cost is held constant the gains "are sometimes not present at all" and that "for
GPT-3.5, the pass rate with repair is lower than or equal to that of the baseline, no-repair
approach at all budgets." Code with a verifier and code without one behave differently; code and
prose are not what is being compared.

**In the one paper that tests a task-type moderator directly, code groups with mathematics against
detail-oriented tasks.** Lin et al. 2402.14809, §4.2.3: "for mathematical reasoning and code
generation tasks, their critique capabilities surpass generation capabilities", against "the models
exhibit weaker critique performance in detail-oriented algorithmic tasks compared to their
generation abilities". The axis is detail versus logic, and code sits on the logic side. There is
no open-ended or creative task in CriticBench to compare against.

**Single-domain negative results on non-code domains do not supply the contrast either.** Valmeekam
et al. 2310.08118 studies planning only: "our findings reveal that **self-critiquing appears to
diminish plan generation performance**, especially when compared to systems with external, sound
verifiers"; "Our results indicate that **the type of feedback—whether it's merely binary
verification or combined with detailed feedback on the errors of the generated plan—doesn't
significantly impact plan generation performance**." Stechly et al. 2310.12397 studies graph
colouring only. Neither runs a second domain, so neither can speak to moderation.

**Conclusion for this paper.** No paper in this corpus reports that code behaves differently from
open-ended generation under undirected self-revision, in either direction. What the literature
reports is that *verification availability* changes the result, and code is simply where
verification is usually available. The two are routinely conflated, and separating them is
available ground.

---

## Creative and subjective writing under iterative revision: what exists

### The searches that were run

arXiv API full-text queries, run 2026-09-03, `max_results=20`, totals as reported by the API's
`opensearch:totalResults` field. Query strings verbatim:

| Query | Total hits | What the hits actually were |
|---|---|---|
| `all:"self-refine" AND all:"creative writing"` | 1 | "Reward Is Enough: LLMs Are In-Context Reinforcement Learners", not about creative writing revision |
| `all:"self-correction" AND all:"creative writing"` | 2 | "Specification Self-Correction: Mitigating In-Context Reward Hacking"; "Polaris: A Gödel Agent Framework", neither about creative writing |
| `all:"iterative refinement" AND all:"creative writing"` | 1 | "Test-Time Scaling in the Wild", not about creative writing |
| `all:"self-revision" AND all:"story generation"` | 0 | none |
| `all:"intrinsic self-correction" AND all:"open-ended generation"` | 0 | none |
| `abs:"self-refine" AND abs:"story"` | 0 | none |
| `all:"self-refine" AND all:"subjective task"` | 2 | free-text rationales in subjective decisions; LLM evaluator self-preference; neither is iterative revision of creative text |
| `all:"self-correction" AND all:"subjective"` | 22 | not individually screened; the term "subjective" appears widely in evaluation discussion |
| `all:"iterative revision" AND all:"large language model"` | 32 | screened by title: research-idea generation, information extraction, scientific computing agents, layout generation, clinical corpora. None on creative or literary revision |
| `all:"self-refinement" AND all:"open-ended"` | 12 | screened by title: recursive self-improvement, robotics failure detection, deep-research agents, RefineBench. One relevant hit (RefineBench) |

**This literature is thin, and the searches above are how that claim is supported.** The bound on
the sweep should be stated plainly: it is arXiv only, English only, phrase-match only, and it does
not cover ACL Anthology, ACM DL (where most of the creative-writing HCI work is published), or
dissertation repositories. Two of the corpus papers below (CoAuthor, Creativity Support) are CHI
papers that happen to be mirrored on arXiv; sibling CHI work that is not mirrored would not have
been found by any query in the table.

### What exists: five papers, none of which is LLM self-revision of creative text without direction

1. **Lee, Liang and Yang 2201.06796 (CoAuthor).** Human-AI collaborative writing across two task
   types, argumentative and creative. Reports per-domain, and reports one arm as null: "Writing
   sessions with GPT-3 with high randomness received slightly higher equality and mutuality scores
   in argumentative writing, **while the difference was not statistically significant in creative
   writing**." Human-in-the-loop drafting, not model self-revision.

2. **Chakrabarty et al. 2309.14556 (Art or Artifice?).** Expert evaluation of LLM-written short
   stories against a 14-test creativity rubric (TTCW). Iterative self-revision appears only as
   future work, and the authors are explicit that it is not what they did: "Assuming that an
   automated method could produce reliable TTCW outcomes, **it could be used in iterative
   algorithms such as Self-Refine (Madaan et al., 2023) to iteratively edit a draft story until it
   passes a large proportion of tests.**" The only iteration they actually run is length matching:
   "we employed an iterative mechanism that prompted the LLM to iteratively expand on its initial
   story until the divergence in word count between the AI-generated and its paired human-written
   story was less than 200."

3. **Chakrabarty et al. 2409.14509 (Can AI writing be salvaged?).** The closest existing work.
   Professional writers with MFAs edit LLM-generated paragraphs in two creative domains: "We
   restrict our focus to generating text in **literary fiction and creative non-fiction**, as these
   genres challenge LLMs with their creativity, emotional nuance, and sophisticated language use."
   8,035 fine-grained expert edits; models then learn from those edits few-shot. The revision
   signal is **human and specific**, which is the opposite of this paper's condition. Self-refine
   appears only in the related-work citation and in a warning: "methods like Iterative
   Self-refinement scenarios, using another language model as an evaluator, may result in reward
   hacking, where the model exploits the evaluator's flaws."

4. **Chakrabarty et al. 2309.12570 (Creativity Support in the Age of LLMs).** Qualitative study
   with emerging writers. No per-domain statistics, no iterative self-revision condition.

5. **Padmakumar and He 2309.05196.** Argumentative essay writing with model assistance; measures
   diversity, not revision quality. One robustness null, reported in the main text and evidenced in
   an appendix: "This result holds across both similarity metrics as well as when the essays are
   compared at the essay level (Table 10 in Appendix C)."

### The one paper that does test open-ended, non-verifiable tasks under undirected self-refinement

**Lee et al. 2511.22173 (RefineBench), retrieved 2026-09-03.** 1,000 problems across 11 domains
with a checklist evaluation, run under two conditions that map almost exactly onto this paper's
design.

The gap statement, §1, verbatim: "**First, whether a LM can refine its answers has largely been
investigated on mathematical problem solving or code. Evaluating refinement in free-form tasks
like essay writing or in other reasoning-heavy domains such as law may lead to different
conclusions.**"

The design, ABSTRACT: "We evaluate two refinement modes: (1) **guided refinement**, where an LM is
provided natural language feedback, and (2) **self-refinement**, where LMs attempt to improve
without guidance."
And the framing, §1: "These refinement requests typically fall into two categories: (1) guided
refinement, where users provide explicit natural language feedback specifying exactly which parts
they want corrected, and (2) **self-refinement, where users ask for revisions without specifying
the problematic elements**. The first scenario requires the ability to precisely adopt the
requested changes, while the second involves reasoning about potential points of dissatisfaction."

The result, ABSTRACT: "In the self-refinement setting, even frontier LMs such as Gemini 2.5 Pro and
GPT-5 achieve modest baseline scores of 31.3% and 29.1%, respectively, and **most models fail to
consistently improve across iterations** (e.g., Gemini-2.5-Pro gains only +1.8%, while DeepSeek-R1
declines by -0.1%). By contrast, in guided refinement, both proprietary LMs and large open-weight
LMs (>70B) can leverage targeted feedback to **refine responses to near-perfect levels within five
turns**."

The mechanism, §5.1, two run-in headings verbatim:
- "**Some LMs possess an ability to refine, but they do not identify what to fix.**" ... "These
  results suggest that LMs contain some inherent refinement ability but struggle to determine the
  items that need to be fixed."
- "**LMs can incorporate provided feedback while struggling with unprovided feedback.**" ... "while
  some LMs are capable of reflecting feedback that is explicitly provided, they may remain limited
  in independently identifying and addressing aspects that require revision without such guidance."

So the field does now contain one benchmark covering non-verifiable free-form domains under
undirected revision. It does **not** contain creative or literary writing as a domain: RefineBench's
11 domains are Math (32%), Humanities/Social Science (19%), Law (14%) and eight others sourced
largely from university examinations, and its own ethics note describes Law and
Humanities/Social Sciences as "**non-verifiable tasks that are relatively subjective**." Fiction,
poetry and narrative craft are absent.

**What this leaves for the present paper.** No paper found in these searches runs undirected
self-revision on creative writing and reports it beside code and analysis domains in one design.
That is a genuine gap, and it should be claimed at that width and no wider: RefineBench already
covers subjective, non-verifiable, non-STEM domains under undirected revision, and it did so before
this paper. The unclaimed ground is creative writing specifically, and the five-domain comparison
within a single instrument.

---

## Where per-domain breakdowns are reported, and whether they reach the abstract

39 papers are in the corpus table. Where each one's per-task or per-domain reporting lives.
Categories are primary locations and do not overlap; secondary locations are noted separately.

**Per-task tables in the results section, with no separate task-type analysis: 24 papers.** The
breakdown is the main results table and nothing more is said about it. Huang 2310.01798; Madaan
2303.17651 (Table 3, §5); Tyen 2311.08516 (Tables 5 to 8); Stechly 2402.08115; Olausson 2306.09896;
Chen 2304.05128; Gou 2305.11738 (Table 1); Jiang 2404.04298 (Table 4); Sharma 2310.13548; Kwan
2401.16745 (Table 2, §4.4); Wang 2309.10691; Dhuliawala 2309.11495; Ji 2310.06271; Lee 2201.06796;
Chakrabarty 2309.14556; Welleck 2211.00053; Shinn 2303.11366; Kim 2303.17491; Weng 2212.09561; Hong
2311.07954; Zhang 2401.02009; Han 2402.12563; Liu 2406.15673; and Laban 2505.06120, which is the
one paper in this group that also spends a paragraph of §6.1 interpreting its own breakdown.

**A dedicated subsection or run-in heading about task type: 3 papers.** Lin 2402.14809, §4.2.3
"RQ3: Impact of Task Type", one of five numbered research questions, supported by Figures 5 and 7
and Appendix D. Lee 2511.22173, "Domain Analysis." as a run-in heading inside §5.2 "In-depth
Analysis", supported by Figure 5 (right) and Appendix D Table 5. Zhang 2412.14959, whose
simple-task versus complex-task split organises the whole paper into §4 and §5.

**A figure as the locus of the breakdown: 2 papers.** Chakrabarty 2409.14509 (Figure 4(c), by
domain); Zheng 2306.05685 (per-category figures).

**An appendix as the locus: 2 papers.** Padmakumar 2309.05196 (Table 10, Appendix C, the robustness
split); Saunders 2206.05802 (Table 4, Appendix A, dataset composition by task type).

**Per-dataset within a single domain, so no cross-domain breakdown is possible: 2 papers.** Zhang
2305.14835 (summarisation); Shridhar 2311.07961 (math word problems).

**A single domain, so no breakdown at all: 3 papers.** Stechly 2310.12397 (graph colouring);
McAleese 2407.00215 (code); Valmeekam 2310.08118 (planning).

**A survey section organised by domain, with no numbers: 2 papers.** Kamoi 2406.01297 (§2.3 task
census, §7 "Tasks Suitable for Self-Correction"); Pan 2308.03188 (§6 Applications, five named
domains).

**Qualitative, no per-domain statistics: 1 paper.** Chakrabarty 2309.12570.

**Secondary appendix locations.** Three papers whose primary locus is elsewhere also push detail to
an appendix: Laban 2505.06120 (Appendices D and F, per-task conversation inspection and per-task
answer-length analysis); Lin 2402.14809 ("For more detailed results, please refer to Appendix D");
Lee 2511.22173 (Appendix D Table 5, per-domain statistics).

**Does it reach the abstract?** 5 of 47 abstracts state a per-task or per-domain difference
(Kamoi, Lin, Tyen, Olausson, Chen) and 9 state uniformity, as counted in the abstract tally below. Of the three
papers with a dedicated task-type analysis section, two put a task-type finding in the abstract
(Lin 2402.14809; Zhang 2412.14959) and one does not (Lee 2511.22173, whose abstract carries only
aggregate self-refinement scores). Of the 24 papers whose main results tables are themselves a full
per-task breakdown, **one** promotes a per-task contrast to the abstract (Olausson 2306.09896,
and its contrast is within a single domain); the other 23 carry the aggregate and the task count
instead.

### Does a task-type contrast reach the ABSTRACT? Full count

All 47 abstracts were read from `arxiv.org/abs/<ID>`, 46 on 2026-09-02 and RefineBench
2511.22173 on 2026-09-03. They sort into four
categories. Counts are exact and every paper behind each count is named.

**Version caution.** Two abstracts differ between the arXiv abstract page (latest version) and the
v1 HTML that was read for the body. Madaan 2303.17651: the abstract page reads "Across all
evaluated tasks, outputs generated with Self-Refine are preferred by humans and automatic metrics
over those generated with the same LLM using conventional one-step generation, improving by ~20%
absolute on average in task performance"; the v1 HTML reads "In all tasks, outputs generated with
Self-Refine are preferred by humans and by automated metrics over those generated directly with
GPT-3.5 and GPT-4, improving on average by absolute ∼20% across tasks." Huang 2310.01798: the
abstract page reads "their performance even degrades after self-correction"; the v1 HTML reads
"at times, their performance might even degrade post self-correction." Both variants are quoted
where used.

### Category A: the abstract states a per-task or per-domain DIFFERENCE. 5 papers, plus 1 partial

1. **Kamoi 2406.01297.** "Our critical survey based on the newly categorized research questions
   shows that (1) no prior work demonstrates successful self-correction with feedback from
   prompted LLMs, **except for studies in tasks that are exceptionally suited for
   self-correction**, (2) **self-correction works well in tasks that can use reliable external
   feedback**, and (3) large-scale fine-tuning enables self-correction."
   This is the strongest case in the corpus: the entire abstract is organised around which tasks
   the method works on. It is a survey, so the task contrast is the contribution.

2. **Lin et al. 2402.14809 (CriticBench).** "Our findings reveal: (1) a linear relationship in GQC
   capabilities, with critique-focused training markedly enhancing performance; (2) **a
   task-dependent variation in correction effectiveness, with logic-oriented tasks being more
   amenable to correction**; (3) GQC knowledge inconsistencies that decrease as model size
   increases; and (4) an intriguing inter-model critiquing dynamic..."
   The task-type result is finding (2) of four, given one clause, with the direction named. It is
   supported by a dedicated results subsection (§4.2.3, "RQ3: Impact of Task Type") and a figure
   (Figure 7). This is the template for a domain result that earns abstract space: a numbered
   finding among several, one clause, direction stated, backed by its own subsection.
   Note the v1 HTML body states the same finding with "critique and correction effectiveness"
   where the abstract page says "correction effectiveness."

3. **Tyen et al. 2311.08516.** Opening sentence: "**While self-correction has shown promise in
   improving LLM outputs in terms of style and quality** (e.g. Chen et al., 2023b; Madaan et al.,
   2023), **recent attempts to self-correct logical or reasoning errors often cause correct
   answers to become incorrect**, resulting in worse performances overall (Huang et al., 2023)."
   The contrast is attributed to prior work, not to this paper's own data, and it is used to
   motivate rather than to report. That is a cheaper way to put a task-type contrast in an
   abstract: cite the field's split rather than claim it yourself.

4. **Olausson et al. 2306.09896.** "We find that when the cost of carrying out repair is taken
   into account, performance gains are often modest, **vary a lot between subsets of the data**,
   and are sometimes not present at all."
   The variation is within a single domain (code, across HumanEval and APPS and across difficulty
   subsets), stated as heterogeneity rather than as a named direction.

5. **Chen et al. 2304.05128 (Self-Debug).** "**On the Spider benchmark where there are no unit
   tests to verify the correctness of predictions**, Self-Debugging with code explanation
   consistently improves the baseline by 2-3%, and improves the prediction accuracy on problems of
   the hardest level by 9%. **On TransCoder and MBPP where unit tests are available**,
   Self-Debugging improves the baseline accuracy by up to 12%."
   A within-code contrast organised entirely by whether external verification exists, with the
   verification condition named inside the sentence rather than in a footnote. The gain is roughly
   four times larger where unit tests exist. This is the single most useful abstract sentence in
   the corpus for the verification-availability claim.

*Partial:* **Kwan et al. 2401.16745 (MT-Eval).** "Our evaluation of 11 well-known LLMs shows that
while closed-source models generally surpass open-source ones, **certain open-source models exceed
GPT-3.5-Turbo in specific tasks**." This is a model-by-task interaction, not a task-type main
effect, and the tasks are not named.

### Category B: the abstract asserts UNIFORMITY across tasks. 9 papers

These are the sentences to imitate for a null domain effect.

1. **Madaan 2303.17651:** "We evaluate Self-Refine **across 7 diverse tasks**, ranging from dialog
   response generation to mathematical reasoning... **Across all evaluated tasks**, outputs
   generated with Self-Refine are preferred by humans and automatic metrics over those generated
   with the same LLM using conventional one-step generation, improving by ~20% absolute on average
   in task performance."
2. **Gou et al. 2305.11738 (CRITIC):** "Comprehensive evaluations involving free-form question
   answering, mathematical program synthesis, and toxicity reduction demonstrate that CRITIC
   **consistently** enhances the performance of LLMs."
3. **Sharma et al. 2310.13548:** "We first demonstrate that five state-of-the-art AI assistants
   **consistently exhibit sycophancy across four varied free-form text-generation tasks**."
   And the closing sentence generalises: "Overall, our results indicate that sycophancy is a
   **general behavior** of state-of-the-art AI assistants."
4. **Tyen et al. 2311.08516:** "We show that this boosts downstream task performance **across our
   5 reasoning tasks**, indicating that LLMs' correction abilities are **robust**."
   Note this paper is in both Category A and Category B: it opens with a borrowed task contrast
   and closes with its own uniformity claim.
5. **Stechly et al. 2402.08115:** "We observe significant performance collapse with self-critique
   and significant performance gains with sound external verification." Stated without task
   qualification although three domains were run; the body supplies "Across all of our domains,
   this self-verification systems worsens performance."
6. **Laban et al. 2505.06120:** "**all** the top open- and closed-weight LLMs we test exhibit
   significantly lower performance in multi-turn conversations than single-turn, with an average
   drop of 39% **across six generation tasks**."
7. **Zhang et al. 2401.02009 (Self-Contrast):** "Experiments conducted on a series of reasoning and
   translation tasks with different LLMs serve to underscore the effectiveness and **generality**
   of our strategy."
8. **Liu et al. 2406.15673:** "we demonstrate that intrinsic self-correction ability is **exhibited
   across multiple existing LLMs**."
9. **Han et al. 2402.12563:** "We conduct extensive experiments and demonstrate that our IoE-based
   Prompt can achieve a **consistent improvement** regarding the accuracy of self-corrected
   responses over the initial answers."

A tenth, hedged, is worth having as a template for "almost uniform": **Saunders et al. 2206.05802:**
"Larger models write more helpful critiques, and **on most tasks**, are better at self-critiquing,
despite having harder-to-critique outputs." "on most tasks" concedes an exception in the abstract
without naming it, and the body supplies "Overall, this suggests that gaps are task-specific."

### Category C: the abstract SCOPES the claim to one task family. 3 papers

Rather than contrast domains, these restrict the claim.

1. **Huang et al. 2310.01798:** "**In the context of reasoning**, our research indicates that LLMs
   struggle to self-correct their responses without external feedback." The title does the same
   work: "Large Language Models Cannot Self-Correct **Reasoning** Yet."
2. **Hong et al. 2311.07954:** "we take a closer look at the self-verification abilities of LLMs
   **in the context of logical reasoning**."
3. **Stechly et al. 2310.12397:** "we set out to systematically investigate the effectiveness of
   iterative prompting of LLMs **in the context of Graph Coloring**, a canonical NP-complete
   reasoning problem."

### Category D: the abstract names the task set but reports only an aggregate

The remainder. Laban 2505.06120 is the clearest instance of a paper that has a full per-task
breakdown table and still gives the abstract only the aggregate plus the task count.

### What this counts to

Of 47 abstracts, **5 state a per-task or per-domain difference outright**, 1 states a
model-by-task interaction, **9 state uniformity across tasks**, and 3 scope the claim to a task
family. So a task-type contrast in an abstract is a minority move, made in roughly one paper in
nine, and in every one of those five cases the contrast is either the paper's central contribution
(Kamoi), a numbered finding backed by its own results subsection (CriticBench), borrowed from
prior work as motivation (Tyen), a statement of heterogeneity rather than direction (Olausson), or
organised around verification availability with the two conditions named (Chen).

**Uniformity across tasks, by contrast, reaches the abstract twice as often as difference does**,
and it is stated flatly, in a single adverb ("consistently", "across all evaluated tasks"), with
the number and the spread of tasks named in the same sentence so the adverb has something to
quantify over. No paper in this corpus apologises for a null task-type effect or reports it as a
limitation.

### The applicable rule for this paper

A per-domain contrast earns abstract space in this literature when it is (a) the paper's central
question, as in Kamoi, or (b) a named research question with its own results subsection and figure,
as in CriticBench. A per-domain breakdown that exists only as the main results tables does not earn
abstract space, and 23 of the 24 papers in that position agree. A **null** domain effect never reaches
an abstract as a null in this corpus; it reaches it as a uniformity claim ("across all evaluated
tasks", "consistently", "across six generation tasks"), which is the same finding stated
positively.

---

---

## Reporting conventions for small per-domain samples and for null domain effects

### Small per-domain cells

**Disclose the cell sizes in a table that shows what was cut. Wang et al. 2309.10691 (MINT)** is
the cleanest example. Per-task-type cells run from 43 to 134 instances. The disclosure is a table
with both the original and the reduced size in adjacent columns: "Task Type / Task Name / Original
Size / Reduced Size in MINT ... Code Generation HumanEval 164 45; MBPP 500 91; Decision Making
ALFWorld 134 134; Reasoning GSM8K 1319 48; HotpotQA 7,405 43; MATH 5,000 100; MMLU 13,985 76;
TheoremQA 800 49; Total 29,307 586". The method is named as a heading, "**Stratified Sub-Sampling
for Efficient Evaluation**", and justified in one sentence: "We use stratified sampling to create a
compact and representative set of 586 examples by ensuring the proportion of correct and incorrect
examples (determined by GPT-3.5) in the sampled set is similar to the dataset before sub-sampling."
The reason for the reduction is put in a footnote as a cost figure rather than as an apology.

**Disclose domain imbalance in one flat sentence. Chakrabarty et al. 2409.14509:** "**The Literary
Fiction genre has a larger representation (80%) in our selection, while the creative non-fiction
genres have a smaller representation.**" And the design control stated equally flatly: "We ensure
that each LLM responds to instruction across all domains in equal proportion."

**Attach the hedge to the comparison, not to the paper. Chakrabarty et al. 2409.14509:** "GPT-4o
and Claude 3.5-Sonnet perform slightly better on creative non-fiction instructions (average 5.2)
compared to Llama3.1-70B (5.0), **though the difference is not statistically significant.**"
The number is given, the direction is given, and the hedge is one trailing clause. No sentence is
spent on the sample being small.

**"suggests" for a small sub-study. Olausson et al. 2306.09896, ABSTRACT:** "**a small-scale study**
in which we provide GPT-4 with feedback from human participants **suggests that** even for the
strongest models, self-repair still lags far behind what can be achieved with human-level
debugging." The size is named as an adjective, the verb is downgraded to "suggests", and the claim
is still made in the abstract.

**Name the single exception rather than aggregating it away. Jiang et al. 2404.04298:** "Our
findings, detailed in Table 4, reveal their DG-Diff **across all tasks are positive except for
Flan-T5-XXL on MT-Bench**."

### Null domain effects: the four registers available

**Register 1: the flat universal, no test, no hedge.** Used when the sign is the same in every
cell. Madaan 2303.17651: "Across all evaluated tasks..."; Gou 2305.11738: "across all datasets,
settings, and LLMs"; Stechly 2402.08115: "Across all of our domains, this self-verification
systems worsens performance"; Laban 2505.06120: "every model sees its performance degrade on every
task"; Zhang 2412.14959: "self-correction can fail across a range of tasks, including both simple
task (e.g., simple factual question answering) and complex ones (e.g., decision making)."
This is the most common register and it requires no statistics.

**Register 2: concede the level, deny the moderation.** Stechly 2402.08115: "The LLM-as-verifier
**ranges in accuracy depending on the domain, but no matter which one**, it maintains significant
false negative and false positive rates." Kwan 2401.16745: "a phenomenon that **persists
irrespective of** the underlying capabilities of the models."
This is the right register for a result whose *magnitude* differs by domain while the *effect*
does not, which is what a non-significant chi-square across five domains alongside visible
descriptive spread describes.

**Register 3: state the null and the descriptive variation in one sentence, null first.**
Lee et al. 2511.22173, §1: "Furthermore, **while overall self-refinement performance is not
significant across domains, we observe meaningful domain-level variation.** In particular, the Law
domain exhibits non-trivial self-refinement for certain models (e.g., Claude-Opus-4.1 and
Gemini-2.5-Pro)."
And the same finding restated in the analysis section, this time variation-first: "Overall, while
LMs tend to struggle with self-refinement on average, **their ability varies considerably across
domains**—with Law showing clear evidence of strong self-refinement capability."
RefineBench is the closest precedent available for this paper's situation, and it does two things
worth copying: it puts the non-significance in the subordinate clause and the observation in the
main clause, and it names the one domain that stands out by name and by model rather than claiming
a general moderation.

**Register 4: the plain statistical null, reported as a finding.** Wang 2309.10691: "We find no
significant difference between open- and closed-source models in terms of Δ_feedback."
Chakrabarty 2409.14509: "**Surprisingly, there are no significant differences** in perceived
writing quality or types of edits needed across texts generated by different large language
models." Lee 2201.06796: "the difference was not statistically significant in creative writing."
Note that in all three the null is about a moderator, never about the paper's main effect, and none
of the three treats it as a shortcoming.

**What no paper in this corpus does.** No paper reports a per-domain contrast as significant and
then, in the same document, reports it as non-significant under a control, without saying which
estimate it stands behind. Where a control changes a conclusion (Huang, Kamoi, Stechly, Olausson),
the controlled estimate is the reported result and the uncontrolled one is shown beside it as the
thing being corrected. That is the only convention in this literature for a p = 0.019 that becomes
p = 0.151 under a control: report the controlled number as the finding, show the uncontrolled one
next to it, and name the control in the same sentence.

---

### The full verbatim catalogue: wording a UNIFORM finding across task types

This is the register to copy if the domain effect is null. Thirteen verbatim examples, sorted by
how directly each states uniformity.

**The strongest form is a bare universal quantifier in the abstract, with the aggregate attached.**

- Madaan et al. 2303.17651, ABSTRACT: "We experiment with 7 diverse tasks, ranging from review
  rewriting to math reasoning, demonstrating that our approach outperforms direct generation.
  **In all tasks**, outputs generated with Self-Refine are preferred by humans and by automated
  metrics over those generated directly with GPT-3.5 and GPT-4, improving on average by absolute
  ∼20% across tasks."
  In the body, §5 Results: "As shown, Self-Refine significantly improves the quality of outputs
  generated by the baseline method **across all tasks**."
  This is the cleanest template available: name the number of tasks, name their spread by naming
  the two extremes, assert the effect holds in all of them, then give one aggregate number. No
  hedge, no per-domain apology.

- Gou et al. 2305.11738 (CRITIC), ABSTRACT: "Comprehensive evaluations involving free-form
  question answering, mathematical program synthesis, and toxicity reduction demonstrate that
  CRITIC **consistently enhances** the performance of LLMs."
  Body, Results: "As seen in Table 1, 1) CRITIC dramatically improves over the model's initial
  CoT results **across all datasets, settings, and LLMs**, requiring only three corrections."
  Note the rhetorical move: the three task families are named individually in the abstract
  precisely so that "consistently" is doing visible work. The spread is the evidence for the
  uniformity, so the spread gets named.

- Sharma et al. 2310.13548, ABSTRACT: "We first demonstrate that five state-of-the-art AI
  assistants **consistently exhibit sycophancy across four varied free-form text-generation
  tasks**."
  "varied" is the load the sentence puts on the task set: uniformity is only interesting if the
  tasks are unlike each other, so the adjective is asserted in the same clause.

**The second form states the universal over the cells of the breakdown table.**

- Laban et al. 2505.06120, §6.1 Average Performance Findings: "At a high level, **every model
  sees its performance degrade on every task** when comparing Full and Sharded performance, with
  an average degradation of -39%."
  And, closing the same subsection's model discussion: "In short, **no matter how strong an LLM's
  single-turn performance is**, we observe large performance degradations in the multi-turn
  setting."
  The abstract keeps only the aggregate: "an average drop of 39% **across six generation tasks**."
  So Laban states the per-cell universal in the results section and lets the abstract carry the
  aggregate with the task count. That is the split this paper should copy if the domain effect is
  null.

- Stechly et al. 2402.08115, Results: "**Across all of our domains**, this self-verification
  systems worsens performance." And: "Our analysis reveals that the verifier LLM's false negative
  rate is significant **across our domains**."
  And the form that concedes level differences while denying moderation: "The LLM-as-verifier
  **ranges in accuracy depending on the domain, but no matter which one**, it maintains
  significant false negative and false positive rates, as illustrated in Table 2."
  That last sentence is the exact register for "the level differs by domain but the effect does
  not." It concedes the descriptive variation in one clause and denies that it changes the
  conclusion in the next, without running or reporting a moderation test.

- Dhuliawala et al. 2309.11495, Results: "We observe a **consistent performance improvement across
  all tasks** from applying the factored CoVe approach compared to joint CoVe."

- Ji et al. 2310.06271, Results: "The experimental results of our method showcase its effectiveness
  across LLMs with varying parameters, including 7B and 175B, **on all five datasets**." And:
  "We observe the superior performance of our method compared to the baselines, as evidenced by
  both classic overlap metrics and hallucination metrics **across all five datasets**."

- Zhang et al. 2305.14835 (SummIt), Results: "It is observed that, **across all datasets**, SummIt
  **consistently** demonstrates inferior ROUGE scores compared to conventional fine-tuning
  approaches, while exhibiting significantly higher GPT evaluation scores."
  Useful because the uniform statement covers a *divergence between two metrics*, not a single
  effect: the pattern, not the sign, is what holds across datasets.

**The third form asserts persistence against a moderator rather than across tasks.**

- Kwan et al. 2401.16745 (MT-Eval), Results: "Our experiment shows a pronounced gap between
  single-turn versus multi-turn performance across current models, **a phenomenon that persists
  irrespective of the underlying capabilities of the models**."
  "persists irrespective of X" is the compact way to report a null moderation without the word
  "null" and without a p-value.

**The fourth form is the explicit statistical null, stated plainly and without apology.**

- Wang et al. 2309.10691 (MINT), Analysis: "**We find no significant difference** between open-
  and closed-source models in terms of Δ_feedback."

- Chakrabarty et al. 2409.14509, Results: "Comparing model scores, we **find no significant
  difference** in writing quality across the three models." And, with the surprise marked:
  "**Surprisingly, there are no significant differences** in perceived writing quality or types of
  edits needed across texts generated by different large language models (GPT-4, Claude 3.5,
  Llama 3.1)."
  The "Surprisingly" is worth noting: a null is reported as a finding with an epistemic marker,
  not buried.

- Padmakumar and He 2309.05196, Results: "**This result holds across both similarity metrics** as
  well as when the essays are compared at the essay level (Table 10 in Appendix C)."
  The robustness split itself is pushed to an appendix table; the main text carries one sentence
  asserting the result survives it.

**Counter-example: the one paper in the corpus that explicitly denies uniformity across domains.**

- Laban et al. 2505.06120, §6.1: "When looking at the task-specific breakdown, some models see
  more muted degradations in certain tasks. For instance, Command-A sees the least degradation on
  the Actions task, while Claude 3.7 Sonnet and GPT-4.1 conserve performance well on Code, and
  Gemini 2.5 Pro in the Data-to-Text task. **This finding indicates that the multi-turn
  capabilities of models are not uniform across domains** and validates the importance of
  benchmarking models across a wide variety of tasks to investigate model capabilities."
  Two things to take from this. First, Laban asserts both the universal ("every model... on every
  task") and the non-uniformity of *magnitude* in the same subsection, without contradiction,
  because the two claims are about different quantities: whether the effect is present, and how
  large it is. Second, the non-uniformity claim is supported by naming individual model-task cells,
  not by a moderation test. No statistical test of the domain contrast appears.

---

### The full verbatim catalogue: wording a contrast that DISAPPEARS under a control

Five papers in the corpus report an apparent self-correction benefit that shrinks, vanishes or
reverses once a control is applied. The register is consistent and worth copying: the effect is
named, the control is named, the corrected estimate is given, and the earlier estimate is
attributed to the missing control rather than to anyone's error.

**1. Huang et al. 2310.01798: the gain reverses under a matched pre-hoc baseline.**
Self-Refine reports a large gain on CommonGen-Hard. Huang re-runs it with a first-attempt prompt
that states the constraint the feedback prompt was implicitly supplying. §4, Table 5, verbatim
rows: "Standard Prompting* 1 44.0* / Self-Correct* 7 67.0* / Standard Prompting* 1 53.0 /
Self-Correct* 7 61.1 / **Standard Prompting (ours) 1 81.8 / Self-Correct* 7 75.1**". The starred
rows are Madaan's; the unstarred are Huang's own. Under the matched baseline the sign flips.
The wording of the diagnosis: "Taking the Constrained Generation (Generative Commonsense
Reasoning) task in Madaan et al. (2023) as an example, where the task involves generating coherent
sentences using 20-30 input concepts: instead of asking the model to identify missing concepts and
then guiding it to incorporate these concepts through feedback, we can simply instruct the model
to include all the concepts from the outset—**a requirement is not explicitly embedded in the
pre-hoc prompt of Madaan et al.**"
And the principle stated generally: "**It is meaningless to employ a well-crafted post-hoc prompt
to guide the model in "self-correcting" a response generated through a poorly constructed pre-hoc
prompt. For a fair comparison, equal effort should be invested in both pre-hoc and post-hoc
prompting.**"
Note the anti-defensive construction: Huang does not accuse, does not hedge, and does not
apologise. He states the control, shows the number, and moves on.

**2. Kamoi et al. 2406.01297: the field-wide version of the same control.**
ABSTRACT: "We first find that prior studies often do not define their research questions in detail
and involve impractical frameworks or **unfair evaluations that over-evaluate self-correction**."
§4, "Unfair Settings": "As in Table 4, we find that many studies use either oracle information in
the self-correction processes (unrealistic frameworks) or weak prompts for generating initial
responses (unfair settings), **which over-evaluate self-correction**. Consequently, we conclude
that **no major work shows successful self-correction of responses from LLMs using feedback
generated by prompting themselves under fair settings in general tasks**."
And the specific charge against Self-Refine: "Self-Refine (Madaan et al., 2023) uses instructions
or few-shot examples that do not correctly correspond to the target task only for initial response
generation, while using appropriate instructions for self-correction, as shown in Table 9 and 10.
**These settings evaluate improvement from weak initial responses, which over-evaluate
self-correction.**"
Kamoi formalises the control as a two-way classification (§3.2, "Fair vs. Unfair"): "**Fair
self-correction represents frameworks that refine the best-possible initial responses.**" and
"**Unfair self-correction... represents frameworks that are practical but do not use the
best-possible initial responses.**" Every surveyed paper is then placed in Table 4 with two
marked columns, "Using Oracle Info for Feedback" and "Weak Prompt for Initial Responses". That
table is the mechanism: the control is applied uniformly to the whole corpus and the papers whose
result survives it are simply the ones with no marks.

**3. Stechly et al. 2310.12397: the gain attributed to a confound rather than to the mechanism.**
ABSTRACT: "(iii) **the correctness and content of the criticisms—whether by LLMs or external
solvers—seems largely irrelevant to the performance of iterative prompting**. We show that the
observed increase in effectiveness is largely due to **the correct solution being fortuitously
present in the top-k completions of the prompt** (and being recognized as such by an external
verifier)."
Body: "This lead us to consider whether the improvement is due to the type of backprompting (as
authors who advocate these types of iterative approaches seem to assume) **or because the answer
just happens to be in the top-K completions** (even if the LLM is itself not cognizant of it)."
And the conclusion: "Even here, we found that **the actual content of iterative back prompts is
not important**, and that the improvements seen can also be obtained by just having the LLM
produce multiple answers, and letting verifier check and pick any correct answer that was
fortuitously generated."
The control here is an ablation of the very thing the mechanism is supposed to be: the content of
the critique is randomised or removed and the effect survives, which is what licenses the
attribution to sampling rather than to correction. This is the closest analogue in the corpus to
stripping meta-commentary and finding the contrast gone.

**4. Stechly et al. 2402.08115: the effect survives but the explanation does not.**
ABSTRACT: "We also note that **merely re-prompting with a sound verifier maintains most of the
benefits of more involved setups**."
Body: "This setup gives substantial performance gains across all domains, **but closer analysis
shows that the level of feedback doesn't seem to matter—as long as the verifier is sound,
improvement remains regardless of how much or how little feedback the LLM receives**."
The construction is: concede the gain, then show that the graded variable which was supposed to
produce it has no effect. "X doesn't seem to matter... regardless of how much or how little" is a
compact and unapologetic way to report a null on the mechanism while keeping the main result.

**5. Olausson et al. 2306.09896: the gain disappears once the cost is held constant.**
ABSTRACT: "We find that **when the cost of carrying out repair is taken into account**,
performance gains are often modest, vary a lot between subsets of the data, and are sometimes not
present at all."
Body, framing the control: "In particular, whether self-repair is a winning strategy or not
ultimately boils down to whether you would—**at an equivalent compute budget**—have had a greater
chance of success if you had simply drawn more code samples i.i.d."
Body, the result: "When taking the cost of doing inspection and repair into account, performance
gains from self-repair can only be seen with GPT-4; **for GPT-3.5, the pass rate with repair is
lower than or equal to that of the baseline, no-repair approach at all budgets.** Even for the
GPT-4 model, performance gains are modest at best (66%→71% pass rate with a budget of 7000
tokens)."
Note the exact phrase "at all budgets": the null is asserted over the whole range of the control
variable rather than at one setting.

### What to take from these five for a contrast that vanishes under a control

- The control is named in the same sentence as the corrected result, never in a footnote:
  "when the cost of carrying out repair is taken into account", "at an equivalent compute budget",
  "under fair settings", "for a fair comparison".
- The uncontrolled number is reported alongside the controlled one rather than suppressed. Huang
  prints Madaan's 44.0→67.0 next to his own 81.8→75.1 in the same table.
- The attribution goes to the missing control, not to a mistake: "over-evaluate self-correction",
  "largely due to the correct solution being fortuitously present in the top-k completions".
- No paper in the corpus frames a disappearing contrast as a limitation of its own work. It is
  reported as the finding.

---

## Rules

Each rule is checkable against the file and names the evidence behind it.

**R1. If the domain effect is null, state it as a uniformity claim in the positive, not as a null
in the negative.** No abstract in this corpus reports "we find no significant domain difference."
Nine report the same fact as "across all evaluated tasks" (Madaan 2303.17651), "consistently" (Gou
2305.11738, Sharma 2310.13548, Han 2402.12563), "across six generation tasks" (Laban 2505.06120),
"across our 5 reasoning tasks" (Tyen 2311.08516), "generality" (Zhang 2401.02009). Evidence: the abstract count below, Category B, 9 papers.

**R2. Attach the task count and the spread of the task set to the uniformity claim, in the same
sentence.** The adverb needs something to quantify over, and naming the two extremes is how this
literature supplies it: "7 diverse tasks, ranging from dialog response generation to mathematical
reasoning" (Madaan); "four **varied** free-form text-generation tasks" (Sharma); "free-form
question answering, mathematical program synthesis, and toxicity reduction" (Gou). Evidence: the abstract count below, Category B.

**R3. Do not put a per-domain contrast in the abstract unless it has its own results subsection.**
Of the three corpus papers with a dedicated task-type analysis section, CriticBench (2402.14809,
§4.2.3) puts it in the abstract, Zhang (2412.14959) puts a task-type split of the failure *mode* in
the abstract, and RefineBench (2511.22173, §5.2 "Domain Analysis.") does not. Of the 24 papers whose
main results tables are the whole breakdown, 23 do not promote a per-task contrast to the abstract.
Evidence: "Where per-domain breakdowns are reported", counts of 24, 3 and 1.

**R4. When a contrast survives in one specification and not in another, report the controlled
estimate as the finding and show the uncontrolled one beside it, naming the control in the same
sentence.** Huang 2310.01798 prints Madaan's 44.0→67.0 next to his own 81.8→75.1 in Table 5.
Olausson 2306.09896 says "when the cost of carrying out repair is taken into account" in the
abstract. Kamoi 2406.01297 says "under fair settings". Stechly 2310.12397 attributes the apparent
gain to "the correct solution being fortuitously present in the top-k completions". Evidence: the disappearing-contrast
catalogue under Reporting conventions, 5 papers.

**R5. Concede a difference in magnitude while denying moderation, if that is what the data show.**
The register exists and is used: "ranges in accuracy depending on the domain, but no matter which
one, it maintains significant false negative and false positive rates" (Stechly 2402.08115);
"persists irrespective of the underlying capabilities of the models" (Kwan 2401.16745). Evidence: the uniform-finding catalogue under
Reporting conventions, Register 2.

**R6. Put the non-significance in the subordinate clause and the observation in the main clause,
then name the one cell that stands out by name.** "while overall self-refinement performance is
not significant across domains, we observe meaningful domain-level variation. In particular, the
Law domain exhibits non-trivial self-refinement for certain models (e.g., Claude-Opus-4.1 and
Gemini-2.5-Pro)" (Lee 2511.22173, §1). Evidence: the uniform-finding catalogue below, Register 3.

**R7. Disclose small per-domain cells in a table showing the original and reduced size side by
side, with the sampling method named and the reason given once.** Wang 2309.10691, Table 1:
"Original Size / Reduced Size in MINT ... Total 29,307 586", with the heading "Stratified
Sub-Sampling for Efficient Evaluation" and the cost given in a footnote. Evidence: "Reporting conventions", MINT.

**R8. Hedge the comparison, not the paper.** Give the number, give the direction, then one
trailing clause: "though the difference is not statistically significant" (Chakrabarty 2409.14509).
Do not spend a sentence on the sample being small. Evidence: "Reporting conventions", three examples.

**R9. Name the single exception rather than aggregating it away.** "across all tasks are positive
except for Flan-T5-XXL on MT-Bench" (Jiang 2404.04298); "on most tasks" (Saunders 2206.05802);
Madaan's own §6 exception, "Non-monotonic increase in output quality for acronym generation", which
concedes "the output quality can fluctuate during the iterative process, improving on one aspect
while losing out on another" for one of seven tasks. Evidence: the abstract count and corpus notes.

**R10. Do not claim the verification-availability result as this paper's finding; it is Kamoi's,
and it is stated more strongly there than any single experiment in this corpus supports.** Kamoi
2406.01297 asserts "self-correction works well in tasks that can use reliable external feedback"
on the basis of a critical re-reading of the literature against a fairness checklist, not on new
experiments. The strongest single quantitative support is Chen 2304.05128's within-code contrast
between benchmarks with and without unit tests. Evidence: "Code and verifiable tasks versus open-ended generation", 7 papers ranked by strength.

**R11. Do not assert that creative writing is unstudied under iterative revision without the
search terms.** Ten arXiv queries are recorded verbatim with hit counts; the bound of the sweep
(arXiv only, English only, phrase-match, no ACL Anthology, no ACM DL, no dissertation
repositories) is stated. Evidence: the creative-writing search table.

**R12. Do not claim RefineBench's ground.** RefineBench (2511.22173) already covers subjective,
non-verifiable, non-STEM domains under undirected self-refinement, and already reports a
domain-level analysis. The unclaimed ground is creative writing as a domain and a five-domain
comparison within one instrument. Evidence: the creative-writing section, RefineBench.

---

## What this paper can and cannot claim about its own domains

**Can claim.** That the effect holds across five domains, stated as a uniformity claim in the
positive, with the number of domains and the spread of the domain set named in the same sentence.
This is the majority move in the literature and it requires no significance test to be defensible:
Madaan, Gou, Sharma, Stechly, Laban and Zhang 2412.14959 all state it from the sign of the effect
in every cell.

**Can claim.** That the magnitude differs by domain while the effect does not, if that is what the
cells show. Register 2 exists for exactly this, and Laban 2505.06120 makes both claims in one
subsection without contradiction.

**Can claim.** That the domain contrast which reaches p = 0.019 on unstripped outputs does not
survive stripping meta-commentary (p = 0.151 objective versus subjective; p = 0.555 across five
domains), reported with the controlled estimate as the finding and the uncontrolled one shown
beside it, with the control named in the same sentence. Four papers in this corpus report exactly
this shape of result and none of them treats it as a limitation.

**Cannot claim** an abstract sentence asserting a domain difference. Five of 47 abstracts do that,
and in every case the contrast is either the paper's central question (Kamoi), a numbered finding
with its own results subsection and figure (CriticBench), borrowed from prior work as motivation
(Tyen), heterogeneity without direction (Olausson), or organised around verification availability
with both conditions named (Chen). A p = 0.555 across five domains is none of these.

**Cannot claim** that objective and subjective tasks behave differently under undirected revision.
The one paper that measures something close, RefineBench, reports "overall self-refinement
performance is not significant across domains" for 11 domains spanning verifiable and
non-verifiable tasks. A null here agrees with the closest existing measurement rather than
contradicting it, which is worth saying in the discussion.

**Cannot claim** that code behaves differently from open-ended generation under self-revision on
this literature's authority. CriticBench 2402.14809, the only paper with a dedicated task-type
finding and a direction, splits its five domains on **detail-oriented versus logic-oriented**, and
on that axis code groups *with* mathematics: "for mathematical reasoning and code generation tasks,
their critique capabilities surpass generation capabilities", against "weaker critique performance
in detail-oriented algorithmic tasks". Code is not the odd one out in the one paper that tested it.

**Cannot claim** to be the first to test undirected revision on non-verifiable tasks. RefineBench
did that, at 1,000 problems across 11 domains, and named the gap in the same words this paper would
use: "Evaluating refinement in free-form tasks like essay writing or in other reasoning-heavy
domains such as law may lead to different conclusions."

**Should claim, if the null holds.** That the mechanism is domain-invariant. That is a stronger
result than a domain contrast would have been, because it says the failure is a property of the
undirected revision request rather than of any particular kind of work, and it is the reading
RefineBench's §5.1 headings already point at: "Some LMs possess an ability to refine, but they do
not identify what to fix"; "LMs can incorporate provided feedback while struggling with unprovided
feedback." Stated that way the null is the finding, not the absence of one.

---

## Limits of this survey

**What was read.** 47 papers fetched as full text from `arxiv.org/html/<ID>v1` on 2026-09-02 (one,
RefineBench 2511.22173, on 2026-09-03) and converted to plain text locally. 39 are quoted in the
corpus table. Every quotation was extracted mechanically from those local text files by regular
expression, not recalled.

**The 8 fetched but not quoted on task type**, named so the count is checkable: Zhang 2305.13534
(*How Language Model Hallucinations Can Snowball*); Chen 2306.03856 (*Iterative Translation
Refinement*); Deng 2311.04205 (*Rephrase and Respond*); Han 2401.07301 (*Small Language Model Can
Self-correct*); Bai 2402.14762 (*MT-Bench-101*); Zhang 2406.02378 (*On the Intrinsic
Self-Correction Capability of LLMs*); Qu 2407.18219 (*Recursive Introspection / RISE*); Kumar
2409.12917 (*Training Language Models to Self-Correct via RL / SCoRe*). Each was searched with the
same regular expressions and yielded nothing that states or tests a task-type effect. RISE and
SCoRe are single-domain or two-domain fine-tuning papers (math, and math plus HumanEval) and do not
report a task-type contrast.

**Version scope.** All body quotations are from arXiv v1 HTML. Abstract quotations are from the
arXiv abstract page, which serves the latest version. Two abstracts differ between the two, and
both variants are printed in the abstract tally. Camera-ready versions were not fetched, and venue metadata
was not verified, so no venue is asserted anywhere in this file. Where an author name appears it
was read from the arXiv author line.

**Coverage bound on the search.** The creative-writing sweep is arXiv only, English only,
phrase-match only, run through the arXiv API's `all:` and `abs:` fields. It does not cover the ACL
Anthology, the ACM Digital Library (where most creative-writing and writing-support HCI work is
published), Google Scholar, or dissertation repositories. Two corpus papers (CoAuthor 2201.06796,
Creativity Support 2309.12570) are CHI papers that happen to be mirrored on arXiv; sibling CHI work
that is not mirrored would not have been found by any query in the table. The claim "this
literature is thin" should therefore be read as bounded to arXiv, and stated that way in the paper.

**What was not done.** No paper's numbers were recomputed. Statements about where a breakdown lives
(table, figure, subsection, appendix) were read from the rendered HTML section headings and figure
and table captions, not from the PDF layout. The counts of abstracts by category were made by
reading all 47 abstracts and classifying them; the classification of Kwan 2401.16745 as "partial"
is a judgment call and is flagged as one. Three papers in the target literature were not read
because they are not on arXiv: no attempt was made to reach ACM DL or ACL Anthology material
during this sweep.

**One asymmetry worth naming.** The corpus over-represents reasoning, mathematics and code, because
that is what the self-correction literature studies. Of the 39 papers in the table, 5 involve
creative or literary writing at all (2201.06796, 2309.05196, 2309.12570, 2309.14556, 2409.14509),
and of those 5, none runs undirected LLM self-revision as its condition. Any claim in the paper
about how the field treats subjective domains rests on those 5 plus the two surveys' brief
treatments (Kamoi §2.3 and §11, Pan §6.4), and should not be stated more widely than that.
