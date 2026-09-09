# Claim-source audit, chunk 1

12 sentences, 15 claim-source pairs. All sources retrieved 2026-09-05.

Every full text below was read in the body, not the abstract alone. Where a source
was read as arXiv HTML, the section headings quoted are the ones in that rendering.

---

## 1.1 [introduction_v2]

> A model is handed a fully specified task, produces a single answer, and is scored against a reference, and on benchmarks of this form current models perform well \cite{liang2023holistic}.

### liang2023holistic (Liang et al., Holistic Evaluation of Language Models)

**Classification: NOT SUPPORTED**

Source: https://arxiv.org/html/2211.09110 (full text), retrieved 2026-09-05.

The citation sits at the end of the sentence and therefore attaches to "current models
perform well." HELM does not report that. Its own summary of high-level findings
(Section 1.2, "Empirical findings") reports heterogeneity, sharp failures, and near-chance
accuracy in places:

> "For toxicity detection on CivilComments, we find that most models are not particularly accurate: OPT (175B) is one of the most accurate models across all scenarios (Figure 26), but achieves essentially chance accuracy at 50.1%." (Section 1.2, finding 12)

> "Across the 9 core question answering scenarios (§3.3), we observe significant heterogeneity in results" (Section 1.2, finding 8)

> "on NarrativeQA, TNLG v2 (530B) precipitously drops from 72.6% standard accuracy (i.e. the third-most accurate model) to 38.9% accuracy in the presence of robustness perturbations." (Section 1.2, finding 4)

> "CNN/DailyMail and XSUM have been standard benchmarks for summarization for many years, but we find that automated evaluations on these datasets largely fail to discriminate differences we observed in model quality." (Section 1.2, finding 10)

Section 11.1 also declines the general performance reading:

> "Consequently, our results should not be taken as levelling the universal claim that models that perform well are always desirable and models that perform poorly are always undesirable." (Section 11.1, "Relevance for practical use")

Two further problems with the attribution. First, "current models": the 30 models HELM
evaluates are the 2022 cohort, with `text-davinci-002` as the most accurate model on the
core scenarios. Nothing in this paper speaks to models current in 2026. Second, HELM is a
benchmark suite paper, not a results-summary paper about the field; it reports where each
model sits, not that the field as a whole does well.

What HELM *does* support is the first half of the sentence, the description of the
benchmark form:

> "we operationalize scenarios through a list of instances, divided into a training set and one or more test sets. Each instance consists of (i) an input (a string) and (ii) a list of references." (Section 2.1, "Scenarios")

> "We also do not study interactive tasks such as dialogue, which will be discuss in forthcoming companion work associated with this effort (Lee et al., Forthcoming)." (Section 3.2, "Selection")

So the citation is right for "fully specified task, single answer, scored against a
reference" and wrong for "current models perform well."

---

## 1.2 [introduction_v2]

> Increasingly they are workplace tasks carried out in collaboration with a user who supplies the goal, reacts to the output, and asks for changes \cite{anthropic2025economicindex, laban2025lost}.

### anthropic2025economicindex (Anthropic, The Anthropic Economic Index)

**Classification: PARTIALLY SUPPORTED**

Source: https://www.anthropic.com/news/the-anthropic-economic-index, retrieved 2026-09-05.

The "workplace tasks in collaboration with a user" half is supported:

> "Automation versus augmentation. We also looked in more detail at how the tasks were being performed—specifically, at which tasks involved “automation” (where AI directly performs tasks such as formatting a document) versus “augmentation” (where AI collaborates with a user to perform a task)."

> "Overall, we saw a slight lean towards augmentation, with 57% of tasks being augmented and 43% of tasks being automated."

> "Task Iteration: Collaborative refinement process" (figure caption defining the augmentation subtypes)

The word **"Increasingly" is not supported.** This page is the first report in the series
and has no time series at all. It says so:

> "These kinds of longitudinal analyses can give us new insights into AI and the job market. […] We can also monitor the ratio of automation to augmentation, providing signals of areas where automation is becoming more prevalent."

That is a statement of intent to measure the trend later, not a measured trend. Later
reports in the same series (September 2025, January 2026, March 2026, June 2026) do
report the trend, and it runs partly the other way: the directive (automation) share rose
from roughly 27% to 39% between January and August 2025, with automation overtaking
augmentation for the first time in August 2025, before augmentation recovered. A reviewer
who knows the series will read "Increasingly … in collaboration" as contradicted by the
sponsor's own later data. If the trend word is kept, it needs a later report as the
source, and the direction needs restating.

### laban2025lost (Laban et al., LLMs Get Lost In Multi-Turn Conversation)

**Classification: PARTIALLY SUPPORTED**

Source: https://arxiv.org/html/2505.06120 (v1, full text), retrieved 2026-09-05.

Supported for the multi-turn, user-clarifies-over-time picture:

> "Such interaction promises to help users not only when they know what they need (i.e., they can fully specify their requirements in an instruction), but also when they don't. In such cases, users might start with an underspecified instruction and further clarify their needs through turn interactions." (Section 1)

Two departures. First, **"workplace tasks" is not this paper's setting.** Its six tasks
are Code, Database, Actions, Math, Data-to-text and Summary, drawn from existing
single-turn benchmarks; it never characterizes them as occupational or workplace tasks.
Second, the simulated user in this paper **reveals withheld requirements**, one shard per
turn; the user is not described as reacting to the output and asking for changes. The
sharding rules are explicit that the content of each turn is fixed in advance:

> "Sharded simulation then ensures that each turn of conversation reveals at most one shard of information per conversation turn, enforcing that the instruction is gradually revealed through the conversation." (Section 1)

That is a different interaction from the one the sentence describes.

Separate from the claim: the bibtex entry lists this as ICLR 2026 with an Outstanding
Paper Award. The arXiv v1 (May 2025) carries no venue. Confirm the venue and the award
line independently before submission.

---

## 1.3 [introduction_v2]

> What users contribute is often thin: real prompts are frequently underspecified, and underspecification measurably degrades the outputs that follow \cite{yang2025underspecification}.

### yang2025underspecification (Yang et al., What Prompts Don't Say)

**Classification: PARTIALLY SUPPORTED**

Source: https://aclanthology.org/2026.findings-acl.441.pdf (full text), retrieved 2026-09-05.

The measured-degradation half is supported, and there is a number for it:

> "While LLMs perform worse (-22.6% avg.) when a requirement is unspecified (top), they are often (41.1% avg.) able to guess unspecified requirements (≥ 0.98 accuracy), with increased capabilities (bottom)." (Figure 2 caption, p. 9076)

> "prompts regress more often on unspecified requirements: 5.9% requirements regress more than 20% over model updates when they are unspecified – an almost 2x increase compared to specified requirements." (Section 3.3, p. 9076)

The problem is **which prompts.** The paper studies developer-authored application
prompts, and its introduction sets end-user prompts aside explicitly:

> "This issue is less significant for end users, as their prompts are typically one-off and considered successful as long as they yield one satisfactory response throughout their interactions. For LLM application developers, the problem is much more serious, as their prompts need to generalize to many different usage scenarios." (Section 1, p. 9072)

The citing sentence is about what *users* contribute in a chat exchange. The source's own
framing says that population is the one where the problem matters least. The nearest
general statement the paper makes about real prompts is a related-work aside, not a
finding of its own:

> "Instruction-following ensures LLMs meet specified requirements, but real-world prompts are often underspecified" (Related work, p. 9079)

Also worth knowing before leaning on this citation: the paper's own conclusion is not
"more specification is better." It reports the opposite at the top end:

> "we found LLMs' average accuracy starts to drop with more requirements specified (Figure 4): Specifying 19 requirements together yields only an 85.0% average accuracy for gpt-4o." (Section 3.4, p. 9077)

> "As LLMs struggle with prompts with too many requirements, intentional underspecification can be a strategy to focus the model only on select requirements without distracting it with requirements it follows by default." (Section 3.4, Implications, p. 9077)

The sentence as written reads as a clean monotone claim that the source fences.

---

## 1.4 [introduction_v2]

> This is the ordinary condition of a non-expert working above the level at which they could specify a correction, a difficulty that scalable-oversight research identifies as central: users often cannot articulate precise intent or reliably validate a complex output \cite{zhou2026oversight}.

### zhou2026oversight (Zhou et al., Steering LLMs via Scalable Interactive Oversight)

**Classification: SUPPORTED**

Source: https://arxiv.org/html/2602.04210 (full text), retrieved 2026-09-05.

The abstract states the assertion almost word for word:

> "While models excel at execution, users often struggle to guide them effectively due to insufficient domain expertise, the difficulty of articulating precise intent, and the inability to reliably validate complex outputs. It presents a critical challenge in scalable oversight: enabling humans to responsibly steer AI systems on tasks that surpass their own ability to specify or verify." (Abstract)

The body names the two halves as separate bottlenecks:

> "First, the specification gap: users often provide underspecified instructions, either because they lack the knowledge to identify constraints or simply cannot afford the bandwidth to detail them exhaustively […] Second, the verification gap: as models autonomously execute long-horizon tasks, the complexity of their outputs often exceeds the user's capacity to efficiently validate them." (Section 1)

> "These challenges highlight a fundamental scalable oversight problem: enabling humans to steer capabilities that exceed their own (OpenAI, 2023)." (Section 1)

The non-expert framing is also the paper's evaluation design:

> "We validate our approach using the “sandwich” protocol (Bowman et al., 2022), a rigorous evaluation setting where a non-expert user attempts to guide a strong model to achieve tasks that only an expert can verify." (Section 1)

One note, not a defect in the claim. The sentence says "scalable-oversight research
identifies," a claim about a literature, and rests it on one 2026 preprint. The
literature-level citation would be stronger with the works this paper itself points to for
the point: Bowman et al. 2022 for the sandwich protocol, Saunders et al. 2022 for critique,
Irving et al. 2018 for debate.

---

## 1.5 [introduction_v2]

> This undirected request, some version of \emph{make it better}, is among the most common things people ask of these systems, and vendor guidance actively encourages it, advising users to treat the model as a collaborator and to iterate toward a better result \cite{openai2025prompting, anthropic2025prompting}.

### anthropic2025prompting (Anthropic, Prompting Best Practices)

**Classification: NOT SUPPORTED**

Source: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices,
retrieved 2026-09-05. The bib entry points at the `#be-clear-and-direct` anchor.

The section named in the citation URL argues the opposite of the claim. It tells the
reader not to make undirected requests:

> "Be clear and direct
> Claude responds well to clear, explicit instructions. Being specific about your desired output can help enhance results. If you want "above and beyond" behavior, explicitly request it rather than relying on the model to infer this from vague prompts."

> "Be specific about the desired output format and constraints."

The page also warns that vague asks fail to trigger action at all:

> "Claude's latest models are trained for precise instruction following and benefit from explicit direction to use specific tools. If you say "can you suggest some changes," Claude will sometimes provide suggestions rather than implementing them, even if making changes might be what you intended."

The nearest passage to an iteration recommendation is a developer chaining pattern, and it
is criterion-directed rather than undirected:

> "The most common chaining pattern is self-correction: generate a draft → have Claude review it against criteria → have Claude refine based on the review. Each step is a separate API call so you can log, evaluate, or branch at any point."

Nothing on the page advises treating the model as a collaborator. Citing this page, and
this anchor in particular, for "vendor guidance actively encourages it" invites a reviewer
to open the link and find the counter-instruction in the first sentence.

### openai2025prompting (OpenAI, GPT-5 Prompting Guide)

**Classification: NOT SUPPORTED**

Source: https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide,
retrieved 2026-09-05.

Every "iterate" in this guide is the developer iterating on the **prompt**, not a user
iterating with the model toward a better output:

> "as always, remember that prompting is not a one-size-fits-all exercise - we encourage you to run experiments and iterate on the foundation offered here to find the best solution for your problem."

> "We understand that the process of building prompts is an iterative one, and many prompts are living documents constantly being updated by different stakeholders - but this is all the more reason to thoroughly review them for poorly-worded instructions."

> "early testers have found great success using GPT-5 as a meta-prompter for itself. Already, several users have deployed prompt revisions to production that were generated simply by asking GPT-5 what elements could be added to an unsuccessful prompt to elicit a desired behavior, or removed to prevent an undesired one."

The one passage about iterating toward a better result is a prompt snippet in which the
model iterates **internally against a rubric it writes for itself**, inside a single turn,
and the guide is explicit that the rubric is hidden from the user:

> "First, spend time thinking of a rubric until you are confident. […] This rubric is critical to get right, but do not show this to the user. This is for your purposes only. Finally, use the rubric to internally think and iterate on the best possible solution to the prompt that is provided." (Section "Zero-to-one app generation")

That is directed self-evaluation against explicit criteria, which is the thing the paper's
argument contrasts with an undirected "make it better." And the guide's stated position on
vagueness runs against the claim:

> "its careful instruction-following behavior means that poorly-constructed prompts containing contradictory or vague instructions can be more damaging to GPT-5 than to other models"

Neither source uses the word collaborator or advises undirected iteration; both are
addressed to developers building applications, not to users of a chat interface.

Separately: the first clause, "among the most common things people ask of these systems,"
is a frequency claim with no citation attached. Neither cited page carries usage
statistics.

---

## 1.6 [introduction_v2]

> \citet{madaan2024self} show that a model given the chance to critique and rewrite its work can raise its quality, and locate the benefit in feedback that is \emph{actionable} and \emph{specific}: that names a concrete change to a concrete part of the output.

### madaan2024self (Madaan et al., Self-Refine)

**Classification: SUPPORTED**

Source: https://arxiv.org/html/2303.17651 (full text), retrieved 2026-09-05.

The quality claim:

> "Across all evaluated tasks, outputs generated with Self-Refine are preferred by humans and automatic metrics over those generated with the same LLM using conventional one-step generation, improving by ∼20% absolute on average in task performance." (Abstract)

The definitions the sentence paraphrases, verbatim from Section 2:

> "We prompt the model to write feedback that is actionable and specific via fb(k). By 'actionable', we mean the feedback should contain a concrete action that would likely improve the output. By 'specific', we mean the feedback should identify concrete phrases in the output to change."

The benefit is located there by ablation, not only by assertion:

> "The impact of the feedback quality. Feedback quality plays a crucial role in Self-Refine. To quantify its impact, we compare Self-Refine, which utilizes specific, actionable feedback, with two ablations: one using generic feedback and another without feedback […] In Code Optimization, performance slightly dips from 27.5 (Self-Refine feedback) to 26.0 (generic feedback), and further to 24.8 (no feedback). […] This effect is more pronounced in tasks like Sentiment Transfer, where changing from our feedback to generic feedback leads to a significant performance drop (43.2 to 31.2), and the task fails without feedback." (Section 4, Table 2)

The qualitative analysis reinforces that the constraint is on feedback, not on the
rewriting step:

> "Specifically, 33% of unsuccessful cases were due to feedback inaccurately pinpointing the error's location, while 61% were a result of feedback suggesting an inappropriate fix. Only 6% of failures were due to the refiner incorrectly implementing good feedback." (Section 5, "Qualitative Analysis")

One point of hygiene, not of substance: the bibtex year is 2023 (NeurIPS 36, 2023) while
the citation label is `madaan2024self`. Confirm which year the manuscript's citation
command prints.

---

## 1.7 [introduction_v2]

> \citet{huang2024large} report that without external feedback models struggle to correct their own reasoning and at times degrade it, and that apparent gains often trace to information leaked through oracle labels or more informative prompts.

### huang2024large (Huang et al., Large Language Models Cannot Self-Correct Reasoning Yet)

**Classification: SUPPORTED**

Source: https://arxiv.org/html/2310.01798 (full text), retrieved 2026-09-05.

First half, verbatim:

> "In the context of reasoning, our research indicates that LLMs struggle to self-correct their responses without external feedback, and at times, their performance even degrades after self-correction." (Abstract)

> "our findings indicate that LLMs struggle to self-correct their reasoning in this setting. In most instances, the performance after self-correction even deteriorates." (Section 1)

Oracle labels:

> "Upon closer examination, we observe that the improvements in these studies result from using oracle labels to guide the self-correction process, and the improvements vanish when oracle labels are not available." (Section 1)

More informative prompts:

> "Our evaluation reveals that the self-correction improvement claimed by some existing work stems from the sub-optimal prompt for generating initial responses, where self-correction corrects these responses with more informative instructions about the initial task in the feedback prompt. In such cases, simply integrating the feedback into the initial instruction can yield better results, and self-correction again decreases performance." (Section 1)

The verb "report" is right for this source; the paper runs the experiments and states the
findings. Note that "struggle" and "at times degrade" are the source's own hedges and the
sentence keeps them, which is correct: the paper's title says "cannot" but its body says
"struggle" and "in most instances."

---

## 1.8 [introduction_v2]

> A critical survey by \citet{kamoi2024selfcorrection} reaches a compatible conclusion across tasks, locating the bottleneck in feedback generation rather than in the capacity to revise.

### kamoi2024selfcorrection (Kamoi et al., When Can LLMs Actually Correct Their Own Mistakes?)

**Classification: SUPPORTED**

Source: https://arxiv.org/html/2406.01297 (v3, full text), retrieved 2026-09-05.

The claim is a section heading in the source, and the section states both halves of the
contrast the sentence draws:

> "7 Summary of Our Analysis — Bottleneck is in Feedback Generation. Prior studies widely agree that LLMs can refine their responses given reliable feedback (§5). However, generating reliable feedback on their own responses is still observed to be challenging for LLMs without using additional information (§4)." (Section 7)

> "Our analysis highlights that the bottleneck is in the feedback generation (§7)." (Section 1)

"Critical survey" is the paper's own self-description ("In this work, we critically survey
broad papers…", Abstract).

**One wording risk to decide on, not an error I can call.** "Across tasks" can be read as
"in all tasks," and the survey fences that reading. Its stated answer to RQ1 is
task-conditional:

> "In tasks with specific properties that are exceptionally favorable for self-correction (e.g., responses are decomposable), self-correction is effective even with in-context learning. (§4)" (Section 1)

> "Tasks with decomposable responses are one of the few groups of tasks for which verification is clearly easier than generation, which enables intrinsic self-correction. However, many real-world tasks do not satisfy this property." (Section 4)

If "across tasks" is meant as "over the range of tasks the survey covers," it is fine. If a
reader takes it as "in every task," the survey contradicts it.

---

## 1.9 [introduction_v2]

> In parallel, \citet{laban2025lost} show that models lose accuracy across multi-turn conversations when task requirements are revealed gradually, a degradation they attribute to underspecification accumulating over turns.

### laban2025lost (Laban et al., LLMs Get Lost In Multi-Turn Conversation)

**Classification: PARTIALLY SUPPORTED**

Source: https://arxiv.org/html/2505.06120 (v1, full text), retrieved 2026-09-05.

The first half is supported and has a number:

> "Our experiments confirm that all the top open- and closed-weight LLMs we test exhibit significantly lower performance in multi-turn conversations than single-turn, with an average drop of 39% across six generation tasks." (Abstract)

> "every model sees its performance degrade on every task when comparing Full and Sharded performance, with an average degradation of -39%." (Section 6.1)

**The attribution clause misstates the paper.** The authors do not attribute the drop to
underspecification accumulating over turns. They decompose it into aptitude and
reliability and put the weight on reliability:

> "Analysis of 200,000+ simulated conversations decomposes the performance degradation into two components: a minor loss in aptitude and a significant increase in unreliability. We find that LLMs often make assumptions in early turns and prematurely attempt to generate final solutions, on which they overly rely." (Abstract)

> "we find that large performance degradations (P̄) are due in large part to increased model unreliability (U), rather than a loss in aptitude (A)." (Section 6.2)

> "We identify four specific causes: (1) LLMs prematurely propose full answer attempts, making assumptions about problem specifications that lead to confusion (Appendix F.1), (2) they overly rely on previous (incorrect) answer attempts leading to lengthier 'bloated' answers (Section F.2), (3) LLMs overly adjust their answers based on the first and last turn of conversation, evidenced by a loss-of-middle-turns phenomenon (Appendix F.3), and (4) they produce overly verbose answers" (Section 6.2)

Two of the paper's controls are aimed directly at the accumulation reading and rule it out.
The Concat condition shows nothing is lost by the splitting itself:

> "models perform roughly equivalently in the Concat setting, with Concat performance averaging 95.1% of the Full counterpart. This implies that the loss in performance for Sharded is not explained by potential loss of information in sharded instructions" (Section 6.1)

And the gradual sharding experiment shows the effect is a step at two turns rather than
something that builds up as turns accumulate:

> "We find that both models get lost in conversation (a minor degradation in aptitude and a large increase in unreliability) with two-shard instructions and beyond. In other words, the gradual sharding experiment indicates that any conversation that involves underspecification and occurs in two or more turns leads to models getting lost in conversation. For users, the granularity at which information is specified does not majorly impact reliability" (Section 6.3)

> "Notably, we observe this drop in performance even in two-turn conversations" (Section 1)

So "accumulating over turns" is the one thing this experiment was built to test, and it
came back negative. This is the pair in chunk 1 most exposed to a reviewer who knows the
paper.

Minor: "show that models lose accuracy" is fine for the six generation tasks studied, but
the metrics are task-specific scores rather than accuracy throughout; the paper's own word
is "performance."

---

## 1.10 [introduction_v2]

> Revision driven only by the model's own judgment, with no feedback supplied from outside, is what \citet{kamoi2024selfcorrection} and \citet{huang2024large} term \emph{intrinsic} self-correction, and the self-refinement literature studies it alongside revision that does carry a signal, whether generated by the model, supplied by an oracle, or embedded in the prompt, asking in each case whether that signal is enough to improve an output.

### huang2024large

**Classification: SUPPORTED**

Source: https://arxiv.org/html/2310.01798, retrieved 2026-09-05.

> "Central to our investigation is the notion of intrinsic self-correction, whereby an LLM attempts to correct its initial responses based solely on its inherent capabilities, without the crutch of external feedback." (Abstract)

> "Consequently, our focus shifts to self-correction without any external or human feedback. We term this setting intrinsic self-correction." (Section 2)

The three signal types the sentence enumerates are also this paper's three analysed cases:
oracle labels (Section 3), equal-inference-cost baselines and multi-agent debate
(Section 4), and prompt design (Section 5), summarized in its Table 1.

### kamoi2024selfcorrection

**Classification: SUPPORTED**

Source: https://arxiv.org/html/2406.01297, retrieved 2026-09-05.

> "Intrinsic (§4). Intrinsic self-correction prompts LLMs to generate feedback on their own responses." (Section 2.2, "Sources of Feedback")

> "(1) Intrinsic self-correction (Huang et al., 2024a) uses the same model and information for initial response generation and self-correction. Intrinsic self-correction can be used to assess [RQ1] whether LLMs can self-correct based solely on their inherent capabilities." (Section 3.2)

The survey's taxonomy also matches the second half of the sentence: it sorts the
literature by source of feedback into Intrinsic (§4), External Information (§5.1) and
Fine-tuning (§5.2), and separately by whether the framework is realistic or uses oracle
information, and fair or unfair with respect to prompt strength (§3.2).

Two things worth knowing. Kamoi **adopts** the term and credits it to Huang: the
parenthetical "(Huang et al., 2024a)" in the Section 3.2 definition. "Kamoi and Huang
term" reads as joint coinage. Consider whether the sentence should say Huang coined it and
Kamoi adopts it. Second, Kamoi's definition adds a condition the paraphrase drops: the
initial response must be the best-possible one, generated with the same model and
information. That fairness condition is what does the work in the survey's negative
verdict, so it may be worth keeping.

---

## 1.11 [results_v2]

> Our revision tax is adjacent to the independently coined ``YapTax'' of \citet{borisov2026yapbench}, which measures single-turn over-generation on brevity-ideal prompts (excess tokens above a minimal-sufficient baseline $\times$ output price); our metric instead captures multi-turn revision waste, where the model is asked to improve an already-sufficient output and the excess accumulates across turns.

### borisov2026yapbench (Borisov et al., Do Chatbot LLMs Talk Too Much? The YapBench Benchmark)

**Classification: SUPPORTED**

Source: https://arxiv.org/html/2601.00624 (full text), retrieved 2026-09-05.

The formula matches exactly. Section 3.3.2, "Cost-based measure: YapTax":

> "Definition 3 (Excess output tokens). Let Ti(M) ∈ ℕ denote the number of output tokens produced by model M on prompt i, and let Ti(b) denote the number of tokens in the minimal sufficient baseline bi, computed under a fixed tokenizer. We define excess output tokens as ExcessTok_i(M) = max{0, Ti(M) − Ti(b)}."

> "Definition 4 (Per-prompt YapTax (USD)). Let pM be the output-token price for model M in USD per token. The per-prompt YapTax is defined as YapTax_i(M) = ExcessTok_i(M) · pM."

Single-turn and brevity-ideal are the benchmark's own words:

> "Each item consists of a single-turn prompt, a curated minimal sufficient baseline answer, and a category label." (Abstract)

> "YapBench contains over three hundred English prompts spanning three common brevity-ideal settings" (Abstract)

One optional precision. YapTax is a secondary metric in this paper, not its primary one:

> "Our primary metric, YapScore, measures excess response length beyond the baseline, in characters" (Abstract)

> "We complement YapScore with auxiliary analyses, including a cost-oriented metric (YapTax) that estimates the marginal token-priced overhead of over-generation" (Section 1)

"Independently coined" is a claim about the paper's own history rather than about this
source, so it is outside what the source can confirm or deny.

---

## 1.12 [discussion]

> The failure is already visible in deployed agentic systems: public issue trackers document agents stuck in infinite loops editing the same file (VSCode Issue \#257885, Claude Code Issue \#27281) \cite{claudecode2025loop}.

### claudecode2025loop (Claude Code Issue #27281)

**Classification: NOT SUPPORTED**

Source: https://github.com/anthropics/claude-code/issues/27281, retrieved 2026-09-05 via
the GitHub REST API. Issue opened 2026-02-21, state closed, labelled `duplicate`.

The issue is real and it is an infinite loop, but the loop is **not an edit loop**. The
model never edits any file; it repeats the intention to write one and never calls the
tool. Title, verbatim:

> "Agent stuck in infinite loop — repeated 'let me write the document' without executing, burned full context window"

Body, verbatim:

> "During a multi-agent research task, Claude Code got stuck in a loop where it repeatedly stated "let me write the document" across multiple turns without ever actually calling the Write tool."

> "Instead of writing, Claude repeatedly said variations of "let me assemble the document now" without invoking any tool"

> "Actual Behavior: Claude entered a loop of stating intent to write without executing."

So this issue documents zero edits, not repeated edits to one file. Citing it for "stuck in
infinite loops editing the same file" reverses what it says.

The **other** issue named in the sentence, VSCode #257885, does support the claim, and is
the source the sentence needs. It is not in the bib. Verbatim from
https://github.com/microsoft/vscode/issues/257885 (opened 2025-07-25, closed), retrieved
2026-09-05:

> Title: "Copilot Chat agent mode stuck in infinite loop editing the same file over and over"

> "by the end of the chat, the Markdown file in question got a spinning icon next to the file name in its tab, and the Keep/Undo history above the chat box exploded with thousands of references to the same file. The file change counter continued incrementing higher as if there were multiple files being edited. I clicked the stop generating button, and by that time (just about 20 seconds), the counter was already as "2080 files changed"."

Two further problems with the entry itself. The bibtex gives `author={{Anthropic}}` and the
title "Infinite Loop Bug"; the issue was filed by a user, not by Anthropic, and that is not
its title. And VSCode #257885 is named in the prose with no bib entry of its own.

---

## Summary table

| # | Sentence source | Cited work | Classification |
|---|---|---|---|
| 1.1 | introduction_v2 | liang2023holistic | **NOT SUPPORTED** |
| 1.2 | introduction_v2 | anthropic2025economicindex | **PARTIALLY SUPPORTED** |
| 1.2 | introduction_v2 | laban2025lost | **PARTIALLY SUPPORTED** |
| 1.3 | introduction_v2 | yang2025underspecification | **PARTIALLY SUPPORTED** |
| 1.4 | introduction_v2 | zhou2026oversight | SUPPORTED |
| 1.5 | introduction_v2 | anthropic2025prompting | **NOT SUPPORTED** |
| 1.5 | introduction_v2 | openai2025prompting | **NOT SUPPORTED** |
| 1.6 | introduction_v2 | madaan2024self | SUPPORTED |
| 1.7 | introduction_v2 | huang2024large | SUPPORTED |
| 1.8 | introduction_v2 | kamoi2024selfcorrection | SUPPORTED (scope wording flagged) |
| 1.9 | introduction_v2 | laban2025lost | **PARTIALLY SUPPORTED** |
| 1.10 | introduction_v2 | kamoi2024selfcorrection | SUPPORTED |
| 1.10 | introduction_v2 | huang2024large | SUPPORTED |
| 1.11 | results_v2 | borisov2026yapbench | SUPPORTED |
| 1.12 | discussion | claudecode2025loop | **NOT SUPPORTED** |

Totals: 8 SUPPORTED, 4 PARTIALLY SUPPORTED, 4 NOT SUPPORTED (that is 15 pairs; 1.8 counted
as SUPPORTED with a flag). No pair was UNCHECKABLE: every source was reached in full text.

### Items outside the claim audit, noted while reading

- `laban2025lost` bibtex asserts ICLR 2026 and an Outstanding Paper Award; the arXiv v1
  carries no venue. Verify.
- `madaan2024self` label says 2024, entry says NeurIPS 36 (2023). Reconcile.
- `claudecode2025loop` bibtex attributes a user-filed GitHub issue to `{{Anthropic}}` and
  gives a title the issue does not have.
- VSCode Issue #257885 is cited in prose with no bib entry.
