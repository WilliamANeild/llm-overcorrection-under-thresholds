# Claim audit, chunk 4 (related work, 7 sentences / 19 claim-source pairs)

Audit performed 2026-09-05. Every source below was fetched on 2026-09-05 unless a
different retrieval date is stated. Classifications are per claim-source pair, judged
against what the citing sentence asserts, not against the general topic of the work.

Where a sentence cites several works at once, each key is judged separately against
the clause it is attached to. Keys that are carried along by their neighbours without
supporting the claim themselves are flagged as such.

---

## 4.1

> Under sustained multi-turn pressure the effect strengthens, with correct answers revised toward incorrect ones when a user pushes back or persists \cite{xu2024earth, fanous2025syceval}.

Two assertions: (a) correct answers get revised toward incorrect ones under user
pushback, and (b) sustaining the pressure across turns strengthens the effect.

### xu2024earth — SUPPORTED

Supports both assertions. The design starts from questions the model answers
correctly and runs a persuasive conversation of up to four turns.

Section 4.3, Finding I (p. 16263):

> "In the first turn, where only the simplest CTRL is used, target LLMs exhibit a proportion of belief alteration ranging from 4.1% to 63.4%. Moreover, as we progress to the fourth turn, the cumulative proportion of belief alteration spans from 20.7% to 78.2%."

Section 4.3, Finding III (p. 16263):

> "Finding III: repetition is more effective than single-turn. In order to gauge the effect of the simplest repetition strategy, we compare MR@4 / MR@1. Our observations in Table 5 reveal a noteworthy increase in the misinformed rate after the repetition of misinformation. Notably, MR of GPT-4 doubled after 3 additional turns of repeating on questions from NQ2."

Section 3 setup: the persuasive conversation "continues up to a maximum of 4 turns."

Scope note, not a defect: the pressure in this paper is a simulated persuader
injecting generated misinformation with rhetorical appeals, not literally "a user
pushes back" on the model's own answer. The sentence's framing is a fair
generalization but a reviewer in this area may read "user pushes back" as narrower
than what Xu et al. run. Also worth knowing: the paper reports GPT-4 as "nearly
immune to repetition" specifically, so the strengthening result is not uniform across
models.

Source: https://aclanthology.org/2024.acl-long.858.pdf (ACL 2024, pp. 16259–16303),
retrieved 2026-09-05.

### fanous2025syceval — PARTIALLY SUPPORTED

Supports assertion (a). Does not support assertion (b), and on the nearest available
comparison the paper points the other way.

On (a), the paper defines and measures exactly the correct-to-incorrect revision:

> "Regressive sycophancy [is] an initially correct response reformed to an incorrect response"

with an overall regressive rate of 14.66% (Claude-Sonnet 18.31%, ChatGPT 14.40%,
Gemini 9.25%).

On (b), the paper does not show sustained multi-turn pressure strengthening the
effect. Its escalation ladder (Simple ⊆ Ethos ⊆ Justification ⊆ Citation) does not
produce monotonically rising sycophancy:

> "simple rebuttals were effective in maximizing progressive sycophancy (Z=6.59, p<0.001) while citation rebuttals produced the most regressive"

and the direct comparison of conversational versus non-conversational pressure runs
against the sentence:

> "Preemptive rebuttals demonstrated significantly higher sycophancy rates than in-context rebuttals (61.75% vs. 56.52%, Z=5.87, p<0.001)."

Preemptive rebuttals carry no conversation history; in-context rebuttals are the
multi-turn condition. The paper's "persistence" measure (78.5%, 95% CI [77.2%,
79.8%]) is defined as "maintaining sycophantic behavior throughout the rebuttal
chain, with at most one transition in behavior" — that is stability of the behavior
once it appears, not intensification under sustained pressure.

**What is wrong:** the clause "under sustained multi-turn pressure the effect
strengthens" is carried entirely by xu2024earth. SycEval is attached to a
strengthening claim it does not make and partially contradicts.

Source: https://arxiv.org/html/2502.08177v3 (AIES 2025; arXiv:2502.08177), retrieved
2026-09-05.

---

## 4.2

> \paragraph{Biases in LLM-as-judge evaluation.} Using LLMs to evaluate generated text is now standard practice \cite{zheng2024judging, li2024generation}, but LLM judges carry biases that our setting activates directly.

### zheng2024judging — SUPPORTED

The paper establishes and validates the practice, which is what the sentence needs it
for. It reports that "strong LLM judges like GPT-4 can match both controlled and
crowdsourced human preferences well, achieving over 80% agreement, the same level of
agreement between humans," and it names the biases the following sentence goes on to
discuss: position bias, verbosity bias, self-enhancement bias, and limited reasoning
ability.

Scope note: this is the 2023 paper that proposed the evaluation protocol; it does not
itself assert that the practice is standard, since at the time it was new. The
"now standard practice" load is carried by li2024generation. Citing zheng as the
establishing reference is conventional and defensible.

Bibliographic note, outside the claim: the entry keys it `zheng2024judging` but
carries `year={2023}` (NeurIPS 2023). The `doi={10.52202/075280-2020}` field does not
resolve to this paper on the NeurIPS proceedings site and should be checked or
dropped before submission.

Source: https://arxiv.org/abs/2306.05685, retrieved 2026-09-05.

### li2024generation — SUPPORTED

Section 5.1, opening sentence:

> "LLM judges are initially proposed for and widely adopted in various evaluation scenarios. For open-ended generation, LLM judges assess the quality of outputs like dialogues, summaries, and creative writing"

and from the introduction:

> "Beyond evaluation, LLMs-as-a-judge has been adopted across the lifecycle for next generations of LLM developments and applications."

Scope note: the abstract calls the area "emerging" and frames the paper as "a
comprehensive survey," so the work is a survey rather than a source of experimental
results. That is fine here — the sentence cites it for the state of practice, not for
a finding. Bibliographic note: the key says 2024 but the entry is EMNLP 2025.

Source: https://aclanthology.org/2025.emnlp-main.138.pdf (EMNLP 2025, pp. 2757–2791),
retrieved 2026-09-05.

---

## 4.3

> Beyond the documented self-preference and position biases \cite{panickssery2024llm, koo2024benchmarking}, judges reward stylistic and formatting cues over substance: verbose outputs score higher regardless of quality \cite{singhal2023long}, and surface features such as lists, boldface, and confident framing raise a judge's score independently of content \cite{wu2023style, zhang2024lists, chen2024humans, ye2024justice}.

This is the densest sentence in the chunk: three clauses, seven keys. Judged clause
by clause.

### panickssery2024llm — PARTIALLY SUPPORTED (clause: "self-preference and position biases")

Supports self-preference. Does not support position bias.

Abstract:

> "One such bias is self-preference, where an LLM evaluator scores its own outputs higher than others' while human annotators consider them of equal quality. [...] By fine-tuning LLMs, we discover a linear correlation between self-recognition capability and the strength of self-preference bias; using controlled experiments, we show that the causal explanation resists straightforward confounders."

On position bias: the terms "position bias", "order bias" and "positional" do not
appear anywhere in the paper. The only occurrence of the string "position" in the
full text is inside a CNN/DailyMail summarization example ("Lewis Hamilton stormed to
pole position at the Bahrain Grand Prix", p. 782 of the extracted text). The paper
cites Zheng et al. for evaluator biases generally, but studies only self-preference.

**What is wrong:** the sentence pairs two keys to a compound noun phrase covering two
biases; panickssery covers only the first. It is carried for "position bias" by
koo2024benchmarking.

Source: https://arxiv.org/pdf/2404.13076 (NeurIPS 2024), retrieved 2026-09-05.

### koo2024benchmarking — SUPPORTED (clause: "self-preference and position biases")

CoBBLEr benchmarks both, under its own names. Order bias is defined as "The tendency
to give preference to an option based on their order (e.g. first, second, or last),"
with the finding that "most models (11/15) tend to be drawn towards either the first-
or last-ordered model in each of the pairwise comparisons," and among models over 40B
parameters "the first-ordered system was strongly favored in over 50%."

Egocentric bias covers self-preference: "the largest models as well as Koala tend to
prefer their own responses (>50%) with the exception of InstructGPT."

Source: https://arxiv.org/html/2309.17012v2 (Findings of ACL 2024, pp. 517–545),
retrieved 2026-09-05.

### singhal2023long — PARTIALLY SUPPORTED (clause: "verbose outputs score higher regardless of quality")

The scope shift is from reward models to LLM judges, and the sentence's grammatical
subject is "judges."

What the paper actually studies, from the abstract:

> "This paper demonstrates, on three diverse settings, that optimizing for response length is, much more than previously thought, a significant factor behind RLHF. Studying the strategies RL optimization uses to maximize reward, we find improvements in reward to largely be driven by increasing response length, instead of other features. [...] Testing a comprehensive set of length-countering interventions, we identify the dominant source of these biases to be reward models, which, by studying training dynamics, we find are non-robust and easily influenced by length biases in preference data."

The object of study is the RLHF reward model and the training dynamics that make it
length-sensitive, not an LLM judge scoring generated text. The paper does use an
LLM-based evaluator for win rates ("This queries 12 OpenAI API-based 'annotators' to
choose between two outputs, and reports pairwise 'win rate' of a model over
another"), but explicitly declines to lean on it for exactly this inference:

> "While useful for additional context, we qualify this metric by noting that it itself may have length biases."

**What is wrong:** the sentence attributes to this paper a finding about judge
scoring behavior that the paper makes about reward models, and it does so in a
sentence whose subject is "judges." The paper also does not test "regardless of
quality" — its claim is that length drives reward improvements, not that quality is
held constant and length still wins. Sources that do make the judge-side claim
directly: zheng2024judging (verbosity bias in MT-Bench), ye2024justice (verbosity
bias, below), and wu2023style (below), all of which are already in this sentence.

Source: https://arxiv.org/html/2310.03716v2 (COLM 2024; arXiv:2310.03716), retrieved
2026-09-05.

### wu2023style — PARTIALLY SUPPORTED (clause: "lists, boldface, and confident framing")

Supports the general style-over-substance point but not the three named features.

The paper's headline finding is:

> "answers with factual errors are rated more favorably than answers that are too short or contained grammatical errors."

Its manipulations are, from the error-type description: factual errors ("made-up
names, wrong numbers, incorrect facts, or incorrect suggestions"), language errors
("spelling errors" and "grammatical mistakes"), and length variation (approximately
100 words versus 50 words). Table 1 shows GPT-4 and Claude-1 both preferring longer
answers.

It does not manipulate lists, boldface, or confident framing. Attached to a clause
naming those three features, this key supports only the length dimension, which the
sentence has already assigned to the previous clause.

Source: https://arxiv.org/html/2307.03025v3 (COLING 2025; arXiv:2307.03025), retrieved
2026-09-05.

### zhang2024lists — SUPPORTED (clause: lists and boldface only)

The strongest key in this clause, and the only one that names lists and bold text
directly and includes an LLM judge among the biased evaluators. Abstract:

> "We observe that many widely-used preference models—including human evaluators, GPT-4, and top-ranking models on the RewardBench benchmark—exhibit strong biases towards specific format patterns, such as lists, links, bold text, and emojis. Furthermore, large language models (LLMs) can exploit these biases to achieve higher rankings on popular benchmarks like AlpacaEval and LMSYS Chatbot Arena."

Section 2.1 pattern statistics report the share of GPT-4-preferred responses carrying
each feature: bold 42.76%, lists 61.73%, exclamation marks 23.34%, emojis 1.99%, with
"GPT-4's preference for these elements is typically stronger than that of humans."

Does not cover "confident framing."

Source: https://arxiv.org/html/2409.11704v2 (ACL 2025, pp. 26940–26961), retrieved
2026-09-05.

### chen2024humans — PARTIALLY SUPPORTED (clause: formatting yes, lists/confident framing no)

Its Beauty Bias is the relevant one and it is defined and operationalized as a
formatting perturbation:

> "or 'lookism', means that someone is privileged because of their good looking. In our context, it refers to the inclination that judges tend to prefer visually appealing content, regardless of its actual validity."

Perturbation: emojis and markdown formatting added without altering semantic meaning.
That covers "boldface" (markdown formatting) and the "independently of content"
qualifier well.

The paper's other biases are Misinformation Oversight (fallacy oversight), Gender,
and Authority. Authority Bias is "the tendency to attribute greater credibility to
statements by their perceived authorities, regardless of the actual evidence," and is
operationalized by adding randomly generated fake references. That is attributed
authority, not the model's own confident framing. Verbosity receives only a minor
appendix treatment (Appendix F.2).

**What is wrong:** supports formatting-as-beauty; does not support "confident framing"
and does not isolate lists.

Source: https://arxiv.org/html/2402.10669v3 (EMNLP 2024; arXiv:2402.10669), retrieved
2026-09-05.

### ye2024justice — PARTIALLY SUPPORTED (clause: "lists, boldface, and confident framing")

CALM quantifies 12 biases, and none of them is a formatting bias. The full Table 1
list, verbatim definitions:

1. Position Bias: "LLM judges exhibit a propensity to favor one answer at certain position over others."
2. Verbosity Bias: "LLM judges favor longer responses, even if they are not as clear, high-quality, or accurate as shorter alternatives."
3. Compassion-Fade Bias: "The tendency to observe different behaviors when given well-known model's name as opposed to anonymized aliases."
4. Bandwagon Bias: "The tendency to give stronger preference to the majority's beliefs regardless of whether they are correct or not."
5. Distraction Bias: "The inclination to give more attention to irrelevant or unimportant details."
6. Fallacy-Oversight Bias: "LLM judges may ignore logical errors in reasoning steps and only focus on the correctness of final results."
7. Authority Bias: "The tendency to assign more credibility to statements made by authority figures, regardless of actual evidence."
8. Sentiment Bias: "The preference for expressions of positive or negative emotions, affecting its judgment of emotional content."
9. Diversity Bias: "Bias may be shown towards certain groups like 'Homosexual', 'Black', 'Female', and 'HIV Positive'."
10. Chain-of-Thought Bias: "The model's evaluation results may vary with and without CoT."
11. Self-Enhancement Bias: "LLM judges may favor the answers generated by themselves."
12. Refinement-Aware Bias: "Telling the model that this is a refined result will lead to different evaluations."

Lists and boldface are absent. The nearest thing to "confident framing" is Authority
Bias (credibility attributed to a named authority) or Sentiment Bias (emotional
valence); neither is the confidence with which a claim is framed. Its Verbosity Bias
does support the *previous* clause of the sentence — which is the clause where
singhal2023long is doing weak work — so this key is attached to the wrong clause.

**What is wrong:** carried along by its neighbours for the formatting claim. Its
genuine contribution to this sentence is verbosity bias, one clause earlier.

Source: https://arxiv.org/html/2410.02736v2 (ICLR 2025; arXiv:2410.02736), retrieved
2026-09-05.

### Sentence-level finding for 4.3

**"Confident framing" is supported by none of the four keys attached to it.** wu2023style
manipulates length and grammar; zhang2024lists manipulates lists, links, bold and
emojis; chen2024humans manipulates emojis, markdown, fake references and gender;
ye2024justice has no formatting or confidence bias among its twelve. Authority bias
(chen, ye) is the nearest neighbour and it is about attributed source authority, not
the assertiveness of the response. This is the item in the chunk most likely to be
caught by a reviewer who works on judge bias.

---

## 4.4

> Enterprise inference spending has risen steeply, roughly doubling in under a year, and the multi-turn agentic workflows driving that growth are where undirected revision loops live \cite{menlo2025llmmarket, gartner2026agentic, deloitte2026stateofai, mckinsey2025stateofai}.

One quantitative claim ("roughly doubling in under a year") followed by an authorial
interpretation. Only one of the four keys supplies the number.

### menlo2025llmmarket — SUPPORTED

> "Model API spending has more than doubled in this brief period—jumping from $3.5 billion (of a total $13.8 billion generative AI spend we estimated last year) to $8.4 billion."

The period is roughly six months (November 2024 report to the mid-2025 update), so
"roughly doubling in under a year" understates rather than overstates. The report
also documents the shift toward inference: "74% of builders now say the majority of
their workloads are inference, up from 48% a year ago," and nearly half of large
enterprises reporting "most or nearly all of their compute is inference-driven—up
from 29% last year."

Scope note: the doubled quantity is **model API spend**, not "inference spending" as
such. The inference share is reported separately as a proportion of workloads, not as
a dollar series. The sentence fuses the two. That is a defensible compression, but
the precise claim Menlo supports is "enterprise model API spend more than doubled in
about six months," and inference is the growing majority of it.

Source: https://menlovc.com/perspective/2025-mid-year-llm-market-update/ (published 31
July 2025), retrieved 2026-09-05.

### gartner2026agentic — UNCHECKABLE

Nothing on gartner.com could be reached: the newsroom press release returned HTTP
403, and both Gartner document pages found by search (7821217, 7839481) returned HTTP
403. The bibtex entry carries no URL, no document ID and no publication date beyond
the year, so a reviewer cannot check it either.

Two flags beyond reachability:

1. The cited title, "Agentic AI Will Drive a 5–30x Increase in Token Consumption per
   Task," does not match any Gartner document title I could locate. The findable
   Gartner titles in this area are "How to Optimize Token Consumption for AI Coding
   Agents" (gartner.com/en/documents/7821217) and "AI Tokenomics: Measuring LLM Usage
   in AI-Enabled Applications" (gartner.com/en/documents/7839481). The 5–30x figure
   itself is widely repeated in secondary trade press attributed to a Gartner March
   2026 analysis, which suggests the title in the bibliography is a paraphrase of the
   finding rather than the document's actual title. That should be resolved before
   submission: a cited title that does not exist is worse than a paywalled citation.
2. Even granting the figure, it concerns **token consumption per task** in agentic
   workflows, not enterprise spending growth. It cannot support the sentence's
   "roughly doubling in under a year" claim, and is attached to a quantitative claim
   about spend that it does not make.

Attempted: https://www.gartner.com/en/newsroom/press-releases/2026-06-24-gartner-predicts-ai-coding-costs-will-surpass-average-developer-salary-by-2028-as-token-consumption-surges (403);
https://www.gartner.com/en/documents/7839481 (403); web search for the exact title
(no match). Attempted 2026-09-05.

### deloitte2026stateofai — NOT SUPPORTED

The page states no figure for AI or inference spending growth, and no doubling of
spend. The only doubling on the page concerns deployment, not money:

> "the number of companies with ≥40% projects in production is set to double in six months"

The page's content is adoption metrics, use cases, governance and workforce
implications. It cannot support "enterprise inference spending has risen steeply,
roughly doubling in under a year."

Source: https://www.deloitte.com/us/en/what-we-do/capabilities/applied-artificial-intelligence/content/state-of-ai-in-the-enterprise.html,
retrieved 2026-09-05.

### mckinsey2025stateofai — UNCHECKABLE

mckinsey.com refused every access route: WebFetch on the article URL returned a
socket hang up and then a 60-second timeout on retry; WebFetch on the report PDF
returned a socket hang up; the Brazilian mirror timed out; direct curl on both the
article and the PDF failed to retrieve a file. The primary text could not be read.

What is attested across multiple independent secondary summaries of the same report
(McKinsey, "The state of AI in 2025: Agents, innovation, and transformation,"
November 2025): 88% of organizations use AI in at least one function, up from 78%;
"Twenty-eight percent of respondents say their organizations are spending more than
10 percent of their total enterprise-wide budget for information and communication
technology on AI technologies"; "60 percent of respondents expect their organizations
to increase their AI investments over the next year"; 23% scaling AI agents in at
least one function, and 40% among organizations above $1 billion revenue, up from 27%.

None of that is a doubling of inference spending in under a year, and no such figure
appears in any coverage of the report I could find. Treat this key as supporting the
agentic-adoption half of the sentence, not the quantitative half — but that reading
is from secondary sources, so the classification stays UNCHECKABLE pending a read of
the report itself.

Attempted 2026-09-05: https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai;
https://www.mckinsey.com/~/media/mckinsey/business%20functions/quantumblack/our%20insights/the%20state%20of%20ai/november%202025/the-state-of-ai-2025-agents-innovation_cmyk-v1.pdf;
https://www.mckinsey.com.br/capabilities/quantumblack/our-insights/the-state-of-ai.

### Sentence-level finding for 4.4

The quantitative claim rests on exactly one of four keys. Deloitte affirmatively does
not contain a spending figure, Gartner is about tokens per task rather than spend and
its title may not be real, and McKinsey could not be opened. The second half of the
sentence — "the multi-turn agentic workflows driving that growth are where undirected
revision loops live" — is the author's own claim; none of the four sources
characterizes agentic loops as undirected or as revision loops. That is fine as
framing but should not read as sourced.

---

## 4.5

> Our revision tax is adjacent to the single-turn over-generation metric of \citet{borisov2026yapbench} but captures a distinct multi-turn cost, the tokens spent revising an already-sufficient output past the point of peak quality.

### borisov2026yapbench — SUPPORTED

Both factual assertions about the cited work check out: it is single-turn, and its
metric is an over-generation metric.

Single-turn:

> "All prompts are evaluated independently in a single-turn setting with no prior context."

The metric:

> "Let i∈ℐ index a prompt with baseline answer length Bi∈ℕ, measured in characters. For a model M, let Li(M)∈ℕ denote the character length of its response to prompt i. The per-prompt YapScore is defined as YapScorei(M) = max{0, Li(M)−Bi}."

The benchmark covers three brevity-ideal categories: short clarifications for
ambiguous inputs, closed-form factual questions, and one-line coding tasks. There is
no multi-turn or revision component anywhere in the paper, which is what the
sentence's contrast requires.

One precision point worth knowing: YapScore is measured in **characters**, not tokens
("enabling comparisons across models without relying on any specific tokenizer").
The sentence says "tokens spent" of the author's own metric, not of YapBench, so
there is no misattribution — but if the paper elsewhere describes YapBench as a token
metric, that would be wrong.

Source: https://arxiv.org/html/2601.00624v1 (arXiv:2601.00624), retrieved 2026-09-05.

---

## 4.6

> Early dialogue systems lose coherence over long conversations \cite{zhang2020dialogpt, thoppilan2022lamda}, a degradation driven by topic drift rather than by revision.

Neither key supports either half of this sentence. This is the weakest pair in the
chunk.

### zhang2020dialogpt — NOT SUPPORTED

The paper reports no measurement of coherence over long conversations and never uses
the term "topic drift." Its own evaluation is explicitly single-turn:

> "DialoGPT extends the Hugging Face PyTorch transformer to attain a performance close to human both in terms of automatic and human evaluation in single-turn dialogue settings."

Where it does speak to multi-turn behavior, it points in the opposite direction from
the sentence:

> "Our observations suggest that the system is able to deal with multi-turn generation better than an RNN counterpart" (Section 4.5, p. 274)

The nearest text on the sentence's topic is in the Introduction, and it is the
paper's **motivation**, attributed to other authors rather than found by this paper:

> "Most open-domain neural response generation systems suffer from content or style inconsistency (Li et al., 2016b; Zhang et al., 2019; Gao et al., 2019c), lack of long-term contextual information (Serban et al., 2017), and blandness (Li et al., 2016a; Zhang et al., 2018; Qin et al., 2019)." (p. 270)

This is the exact pattern to watch for: a paper credited with a finding that is
actually its related-work framing. If the underlying claim is wanted, Serban et al.
(2017) is the work cited there for long-term context loss. The Limitations section
(Section 6, p. 275) covers offensive output and social bias only; it says nothing
about coherence or conversation length.

Source: https://aclanthology.org/2020.acl-demos.30.pdf (ACL 2020 System
Demonstrations, pp. 270–278), retrieved 2026-09-05.

### thoppilan2022lamda — NOT SUPPORTED

LaMDA does define a within-dialog consistency metric. Section 4.1:

> "The first score, sensibleness, measures whether a model's responses make sense in context and do not contradict anything that was said earlier."

But the paper never measures that metric as a function of conversation length, and
"topic drift" does not appear in the text. Its quality evaluation set is short by
construction. Section 5:

> "We evaluate the models based on the model's generated responses to the Mini-Turing Benchmark (MTB) dataset[17], which consists of 1477 dialogs with up to 3 dialog turns. The MTB includes 315 single-turn dialogs, 500 2-turn dialogs, and 662 3-turn dialogs."

Fine-tuning collection dialogs run 14 to 30 turns, but they are training data, not a
length-varying evaluation. The Discussion and limitations (Section 9) names the
paper's own residual quality problems, and none of them is coherence loss over length
or topic drift:

> "while the model generates responses that make sense most of the time, it can still suffer from subtler quality issues. For example, it may repeatedly pledge to respond to a user's question in the future, prematurely try to end the conversation, or make up incorrect details about the user."

**What is wrong:** the sentence attributes to LaMDA a length-dependent degradation
result it does not report, on an evaluation set of at most three turns, plus a causal
attribution to topic drift that appears nowhere in the paper. The causal clause ("a
degradation driven by topic drift rather than by revision") is unsourced by both keys
and is doing real work in the paper's argument, since it is what separates the prior
literature from this paper's mechanism.

Source: https://arxiv.org/abs/2201.08239 (arXiv:2201.08239v3, 10 Feb 2022), full PDF
text extracted and searched, retrieved 2026-09-05.

---

## 4.7

> Closest to our work, \citet{laban2025lost} show that models lose accuracy across multi-turn conversations when a task's requirements are revealed piecewise, and attribute the loss to underspecification accumulating over turns as the model commits to early assumptions it cannot recover from.

### laban2025lost — PARTIALLY SUPPORTED

The first half is right; the attribution in the second half compresses the paper's
explanation in a way that drops the cause closest to this paper's own subject.

First half, supported. Section 3.1 defines the piecewise reveal:

> "sharded instructions, a set of smaller instructions that jointly deliver the same information as the original instruction"

Section 3.2:

> "the assistant is the LLM being evaluated in the simulation, the user (simulated by an LLM) who has access to the entirety of the sharded instruction and is in charge of revealing shards during turns."

Section 6.1:

> "every model sees its performance degrade on every task when comparing Full and Sharded performance, with an average degradation of -39%."

Second half, imprecise. The paper's headline decomposition is not about
underspecification accumulating; it is a reliability collapse. Section 6.2:

> "Model aptitude degrades in a non-significant way between the full and sharded settings, with an average drop of 16%. On the other hand, unreliability skyrockets with an average increase of 112%."

And the causal account is four-part, not one-part. Section 6.2:

> "(1) generate overly verbose responses, leading them to (2) propose final solutions prematurely in conversation, (3) make incorrect assumptions about underspecified details, and (4) rely too heavily on previous (incorrect) answer attempts."

expanded in Appendix F as "Premature Answer Attempts" (F.1), "Answer Bloat" (F.2),
"Over-adjust based on Last Turn" (F.3) and "Overly-verbose Assistant Responses"
(F.4). The paper's summary formulation is:

> "when LLMs take a wrong turn in a conversation, they get lost and do not recover."

**What is wrong, precisely:** the sentence's attribution covers causes (2), (3) and
(4) and drops (1), verbosity and answer bloat. That omission matters here because
verbosity is the cause nearest this paper's own revision-tax construct, so the
sentence understates the overlap with the closest prior work at exactly the point
where a reviewer will look for it. Second, "underspecification accumulating over
turns" is not the paper's mechanism: underspecification is the experimental
manipulation, held roughly constant by design, and what accumulates is unreliability
and reliance on prior wrong attempts.

Bibliographic note, outside the claim: the entry lists ICLR 2026 with an Outstanding
Paper Award. Neither the venue nor the award could be confirmed from the arXiv record
during this audit; verify against the ICLR proceedings before submission.

Source: https://arxiv.org/html/2505.06120v1 (arXiv:2505.06120), retrieved 2026-09-05.

---

## Summary table

| # | Sentence | Cited work | Classification |
|---|---|---|---|
| 1 | 4.1 | xu2024earth | SUPPORTED |
| 2 | 4.1 | fanous2025syceval | PARTIALLY SUPPORTED |
| 3 | 4.2 | zheng2024judging | SUPPORTED |
| 4 | 4.2 | li2024generation | SUPPORTED |
| 5 | 4.3 | panickssery2024llm | PARTIALLY SUPPORTED |
| 6 | 4.3 | koo2024benchmarking | SUPPORTED |
| 7 | 4.3 | singhal2023long | PARTIALLY SUPPORTED |
| 8 | 4.3 | wu2023style | PARTIALLY SUPPORTED |
| 9 | 4.3 | zhang2024lists | SUPPORTED |
| 10 | 4.3 | chen2024humans | PARTIALLY SUPPORTED |
| 11 | 4.3 | ye2024justice | PARTIALLY SUPPORTED |
| 12 | 4.4 | menlo2025llmmarket | SUPPORTED |
| 13 | 4.4 | gartner2026agentic | UNCHECKABLE |
| 14 | 4.4 | deloitte2026stateofai | NOT SUPPORTED |
| 15 | 4.4 | mckinsey2025stateofai | UNCHECKABLE |
| 16 | 4.5 | borisov2026yapbench | SUPPORTED |
| 17 | 4.6 | zhang2020dialogpt | NOT SUPPORTED |
| 18 | 4.6 | thoppilan2022lamda | NOT SUPPORTED |
| 19 | 4.7 | laban2025lost | PARTIALLY SUPPORTED |

Totals: 6 SUPPORTED, 7 PARTIALLY SUPPORTED, 3 NOT SUPPORTED, 2 UNCHECKABLE, 0 WRONG
SOURCE.

Unsourced clauses that no cited key covers, listed separately because they are not
attributable to any single pair:

- 4.3, "confident framing" — none of wu2023style, zhang2024lists, chen2024humans or
  ye2024justice manipulates or measures it.
- 4.4, "the multi-turn agentic workflows driving that growth are where undirected
  revision loops live" — authorial claim; no cited source characterizes agentic
  workflows this way.
- 4.6, "a degradation driven by topic drift rather than by revision" — neither
  DialoGPT nor LaMDA mentions topic drift.
