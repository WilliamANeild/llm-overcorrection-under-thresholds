# How an abstract introduces a coined term, and what the coinage buys

Compiled 2026-09-06. Purpose: decide whether the paper going to ARR in October 2026 should put
one of its three candidate coinages ("revision tax", "revision robustness", "undirected
revision") into its abstract, where it would sit, and what a definition costs in words. The
comparison corpus is 39 abstracts, 2023 to 2026, each of which introduces a coined term for a
phenomenon, a measure, or a setting rather than for a released system.

## Corpus and how it was drawn

**Source and retrieval.** Every abstract was fetched from its arXiv landing page
(`https://arxiv.org/abs/<id>`), one HTTP request per paper, on **2026-09-06**. The abstract was
taken from the `blockquote` with class `abstract`, the title from the `h1` with class
`title mathjax`, and both were stripped of markup and whitespace-normalised by script
(`02_fetch.py`). Nothing was retyped by hand. All 54 requested pages returned HTTP 200 and
parsed; there were no access failures at the fetch stage. The arXiv Atom API
(`export.arxiv.org/api/query`) was tried first for title-to-identifier resolution and returned
HTTP 429 after eight queries; that path was abandoned in favour of direct landing-page fetches,
and every identifier below is confirmed by its fetched title matching the paper sought.

**Sampling method, stated plainly.** This is a **purposive** sample, not a random one. Candidate
papers were assembled from three sources: (i) the five anchors named in the brief; (ii) the
overthinking, self-correction, multi-turn-degradation, LLM-judge-bias and AI-safety literatures,
enumerated from memory of the field and then verified by fetching each landing page and checking
the returned title; (iii) three web searches for 2026 arXiv work on multi-turn and revision
phenomena, which added the six most recent items. 54 papers were fetched and read in full; 39
were kept because their abstract introduces a coined term, and 15 were dropped, with reasons
given in the "Screened out" section below.

**Bounds on the sample.** The draw is deliberately conditioned on the outcome of interest, so
it can say what a coinage-carrying abstract looks like and cannot say what fraction of abstracts
carry a coinage. It over-represents negative-result and behavioural-analysis papers, because those
are the papers that name failures. Every identifier here is an arXiv identifier, and the venue
of eventual publication was not checked paper by paper, so no claim is made about how many of the
39 appeared at an ACL-family venue. Anything the sample says about digit density or abstract length is
therefore a statement about this genre, not about the venue, and the venue baseline used for
comparison throughout is the separate 47-abstract systematic sample of 2026 ACL, Findings and
EACL abstracts already held in `acl2026_density.md` (median 161 words, 31 of 47 carrying no
quantitative digit).

**How things were counted.** Word counts, sentence counts, sentence position, term recurrence,
title presence, definition-span word counts and numeral counts are produced mechanically by
script (`03_measure.py`, `04_code.py`, `05_stats.py`) with a regex tokenizer and a sentence
splitter that protects decimals and the usual abbreviations. Five fields are hand-coded and are
marked as such wherever they appear: the coined term itself, the definition span, the kind
(phenomenon / metric / condition), the definedness class, and the rhetorical position
(setup / finding / close). Every hand-coded definition span was checked by script to be a verbatim
substring of the fetched abstract; all 38 spans verified, and the one abstract with no definition
span is recorded as such.

A numeral is counted as **quantitative** only if it is not part of an identifier. Digits inside
model and dataset names (GPT-4, o1-like, Llama-3, GSM8K, MATH500, DeepSeek R1, Claude 3.7),
four-digit years, and enumeration markers such as "(1)" are counted separately as identifier
digits and excluded from the quantitative count. Both figures appear in the table.

**Definedness classes.** DEFINED: the definition sits in the same sentence as the term, as an
appositive, a relative clause, or a colon expansion. ADJACENT: the term is named bare and the
definition is the immediately preceding sentence. GESTURED: something is said about the term but
no genus-and-difference definition is given. USED: the term appears with nothing attached.

## Corpus table

Kind: phenomenon = a behaviour; metric = a measured quantity; condition = a setting or threshold.
Position gives the sentence carrying the term, out of the abstract's sentence count, with the
hand-coded rhetorical role. Occurrences count the whole term family in the abstract, including
abbreviations and adjectival forms.

| arXiv ID | Coined term (verbatim) | Kind | Novel/est. | Definedness | Def. words | Position | Occ. in abstract | In title | Words | Quant. digits | Ident. digits |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `2302.00093` | distractibility | metric | novel | defined | 11 | 3/6 (setup) | 2 | no | 141 | 0 | 0 |
| `2302.09664` | semantic entropy | metric | novel | defined | 10 | 4/6 (setup) | 2 | no | 114 | 0 | 0 |
| `2305.14251` | FACTSCORE | metric | novel | defined | 26 | 2/6 (setup) | 10 | yes | 208 | 4 | 4 |
| `2308.12032` | Instruction-Following Difficulty (IFD) | metric | novel | defined | 13 | 3/7 (setup) | 4 | no | 155 | 1 | 0 |
| `2504.10694` | the jailbreak tax | metric | novel | defined | 9 | 5/8 (finding) | 2 | yes | 181 | 1 | 0 |
| `2507.02778` | Self-Correction Blind Spot | metric | novel | defined | 10 | 4/8 (finding) | 4 | yes | 215 | 5 | 0 |
| `2601.00624` | YapScore | metric | novel | defined | 9 | 5/9 (setup) | 3 | no | 222 | 1 | 0 |
| `2604.28031` | the knows-but-violates (KBV) rate | metric | novel | defined | 6 | 5/9 (finding) | 3 | no | 178 | 7 | 0 |
| `2606.16011` | answer stability | metric | novel | gestured | 27 | 3/10 (setup) | 1 | no | 197 | 6 | 0 |
| `2305.13534` | hallucination snowballing | phenomenon | novel | defined | 16 | 5/5 (close) | 1 | no | 114 | 2 | 2 |
| `2305.15852` | self-contradiction | phenomenon | novel | defined | 11 | 2/11 (setup) | 5 | no | 194 | 3 | 1 |
| `2305.17493` | Model Collapse | phenomenon | novel | adjacent | 21 | 8/11 (finding) | 1 | no | 201 | 0 | 3 |
| `2305.19118` | Degeneration-of-Thought (DoT) | phenomenon | novel | defined | 26 | 3/9 (finding) | 3 | no | 229 | 0 | 0 |
| `2306.05685` | self-enhancement bias | phenomenon | novel | used | -- | 3/8 (setup) | 1 | no | 184 | 1 | 3 |
| `2309.06256` | the alignment tax | phenomenon | established | defined | 3 | 1/10 (setup) | 4 | yes | 246 | 0 | 4 |
| `2309.12288` | the Reversal Curse | phenomenon | novel | adjacent | 26 | 3/12 (finding) | 3 | yes | 257 | 2 | 5 |
| `2309.17453` | attention sink | phenomenon | novel | defined | 15 | 5/11 (finding) | 3 | yes | 239 | 2 | 1 |
| `2310.01798` | intrinsic self-correction | condition | novel | defined | 21 | 5/7 (setup) | 1 | no | 142 | 0 | 0 |
| `2310.13548` | sycophancy | phenomenon | established | defined | 9 | 2/9 (setup) | 5 | yes | 164 | 0 | 0 |
| `2311.08596` | the FlipFlop effect | phenomenon | novel | adjacent | 19 | 4/6 (finding) | 1 | no | 188 | 3 | 0 |
| `2402.11436` | self-bias | phenomenon | novel | defined | 7 | 3/8 (setup) | 3 | yes | 153 | 0 | 3 |
| `2404.13076` | self-preference | phenomenon | novel | defined | 19 | 3/8 (setup) | 3 | no | 165 | 1 | 1 |
| `2406.05946` | shallow safety alignment | phenomenon | novel | adjacent | 22 | 4/10 (setup) | 3 | no | 208 | 0 | 0 |
| `2406.07358` | sandbagging | phenomenon | novel | defined | 5 | 3/11 (setup) | 3 | yes | 203 | 1 | 1 |
| `2406.10162` | specification gaming | phenomenon | established | defined | 16 | 1/9 (setup) | 5 | no | 198 | 0 | 0 |
| `2411.07858` | Verbosity Compensation (VC) | phenomenon | novel | defined | 25 | 2/13 (finding) | 7 | yes | 268 | 5 | 6 |
| `2412.14093` | alignment faking | phenomenon | novel | defined | 17 | 1/10 (setup) | 6 | yes | 309 | 3 | 0 |
| `2412.21187` | overthinking | phenomenon | novel | defined | 12 | 4/7 (setup) | 2 | yes | 147 | 0 | 4 |
| `2501.18585` | underthinking | phenomenon | novel | defined | 19 | 2/8 (finding) | 3 | yes | 172 | 0 | 4 |
| `2502.08235` | overthinking | phenomenon | novel | adjacent | 12 | 2/10 (setup) | 10 | yes | 182 | 3 | 0 |
| `2502.17424` | emergent misalignment | phenomenon | novel | adjacent | 12 | 6/16 (finding) | 4 | yes | 227 | 0 | 2 |
| `2503.00555` | Safety Tax | phenomenon | novel | adjacent | 15 | 6/8 (finding) | 1 | yes | 163 | 0 | 0 |
| `2503.08679` | Implicit Post-Hoc Rationalization | phenomenon | novel | adjacent | 20 | 4/7 (finding) | 2 | no | 219 | 4 | 1 |
| `2505.06120` | get lost (in multi-turn conversation) | phenomenon | novel | gestured | 16 | 8/8 (close) | 2 | yes | 188 | 2 | 0 |
| `2505.13988` | the hallucination tax | phenomenon | novel | defined | 15 | 3/7 (finding) | 1 | yes | 174 | 2 | 0 |
| `2505.16894` | attention-locking | condition | novel | defined | 10 | 5/7 (finding) | 1 | no | 178 | 1 | 6 |
| `2505.22630` | stochastic chameleons | phenomenon | novel | defined | 14 | 6/6 (close) | 1 | yes | 214 | 1 | 1 |
| `2506.11930` | Feedback Friction | phenomenon | novel | defined | 7 | 7/10 (finding) | 2 | yes | 223 | 1 | 0 |
| `2510.07777` | context drift | phenomenon | novel | defined | 12 | 2/8 (setup) | 3 | no | 218 | 0 | 0 |

Two notes on the table. `2311.08596` names two things: the setting ("the FlipFlop experiment",
sentence 2) and the behaviour ("the FlipFlop effect", sentence 4); the row records the behaviour,
and the family "FlipFlop" occurs 4 times across the abstract. `2505.22630` likewise names
"class-based (mis)generalization" at sentence 4 and "stochastic chameleons" at sentence 6; the row
records the title term.

## Verbatim introduction catalogue

Each entry gives the sentence that introduces the term, quoted exactly as fetched, with its
position and the measured properties beneath it.

**`2302.00093` — distractibility**  
*Large Language Models Can Be Easily Distracted by Irrelevant Context* (31 Jan 2023; retrieved 2026-09-06)

> In this work, we investigate the distractibility of large language models, i.e., how the model problem-solving accuracy can be influenced by irrelevant context.

Sentence 3 of 6. Metric. Defined in the same sentence. Definition span (11 words): "how the model problem-solving accuracy can be influenced by irrelevant context". Term appears 2 times in the abstract; absent in the title. Abstract 141 words, 0 quantitative digits.

**`2302.09664` — semantic entropy**  
*Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation* (19 Feb 2023; retrieved 2026-09-06)

> To overcome these challenges we introduce semantic entropy -- an entropy which incorporates linguistic invariances created by shared meanings.

Sentence 4 of 6. Metric. Defined in the same sentence. Definition span (10 words): "an entropy which incorporates linguistic invariances created by shared meanings". Term appears 2 times in the abstract; absent in the title. Abstract 114 words, 0 quantitative digits.

**`2305.13534` — hallucination snowballing**  
*How Language Model Hallucinations Can Snowball* (22 May 2023; retrieved 2026-09-06)

> We refer to this phenomenon as hallucination snowballing: an LM over-commits to early mistakes, leading to more mistakes that it otherwise would not make.

Sentence 5 of 5. Phenomenon. Defined in the same sentence. Definition span (16 words): "an LM over-commits to early mistakes, leading to more mistakes that it otherwise would not make". Term appears 1 time in the abstract; absent in the title. Abstract 114 words, 2 quantitative digits.

**`2305.14251` — FACTSCORE**  
*FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation* (23 May 2023; retrieved 2026-09-06)

> In this paper, we introduce FACTSCORE, a new evaluation that breaks a generation into a series of atomic facts and computes the percentage of atomic facts supported by a reliable knowledge source.

Sentence 2 of 6. Metric. Defined in the same sentence. Definition span (26 words): "a new evaluation that breaks a generation into a series of atomic facts and computes the percentage of atomic facts supported by a reliable knowledge source". Term appears 10 times in the abstract; present in the title. Abstract 208 words, 4 quantitative digits.

**`2305.15852` — self-contradiction**  
*Self-contradictory Hallucinations of Large Language Models: Evaluation, Detection and Mitigation* (25 May 2023; retrieved 2026-09-06)

> An important instance of this problem is self-contradiction, where the LM generates two contradictory sentences within the same context.

Sentence 2 of 11. Phenomenon. Defined in the same sentence. Definition span (11 words): "where the LM generates two contradictory sentences within the same context". Term appears 5 times in the abstract; absent in the title. Abstract 194 words, 3 quantitative digits.

**`2305.17493` — Model Collapse**  
*The Curse of Recursion: Training on Generated Data Makes Models Forget* (27 May 2023; retrieved 2026-09-06)

> We refer to this effect as Model Collapse and show that it can occur in Variational Autoencoders, Gaussian Mixture Models and LLMs.

Sentence 8 of 11. Phenomenon. Defined in the immediately preceding sentence. Definition span (21 words): "use of model-generated content in training causes irreversible defects in the resulting models, where tails of the original content distribution disappear". Term appears 1 time in the abstract; absent in the title. Abstract 201 words, 0 quantitative digits.

**`2305.19118` — Degeneration-of-Thought (DoT)**  
*Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate* (30 May 2023; retrieved 2026-09-06)

> However, our study shows that such reflection-style methods suffer from the Degeneration-of-Thought (DoT) problem: once the LLM has established confidence in its solutions, it is unable to generate novel thoughts later through reflection even if its initial stance is incorrect.

Sentence 3 of 9. Phenomenon. Defined in the same sentence. Definition span (26 words): "once the LLM has established confidence in its solutions, it is unable to generate novel thoughts later through reflection even if its initial stance is incorrect". Term appears 3 times in the abstract; absent in the title. Abstract 229 words, 0 quantitative digits.

**`2306.05685` — self-enhancement bias**  
*Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena* (9 Jun 2023; retrieved 2026-09-06)

> We examine the usage and limitations of LLM-as-a-judge, including position, verbosity, and self-enhancement biases, as well as limited reasoning ability, and propose solutions to mitigate some of them.

Sentence 3 of 8. Phenomenon. Used with no definition. No definition span. Term appears 1 time in the abstract; absent in the title. Abstract 184 words, 1 quantitative digits. Also coins: position bias; verbosity bias.

**`2308.12032` — Instruction-Following Difficulty (IFD)**  
*From Quantity to Quality: Boosting LLM Performance with Self-Guided Data Selection for Instruction Tuning* (23 Aug 2023; retrieved 2026-09-06)

> Our key innovation, the Instruction-Following Difficulty (IFD) metric, emerges as a pivotal metric to identify discrepancies between a model's expected responses and its intrinsic generation capability.

Sentence 3 of 7. Metric. Defined in the same sentence. Definition span (13 words): "to identify discrepancies between a model's expected responses and its intrinsic generation capability". Term appears 4 times in the abstract; absent in the title. Abstract 155 words, 1 quantitative digits.

**`2309.06256` — the alignment tax**  
*Mitigating the Alignment Tax of RLHF* (12 Sep 2023; retrieved 2026-09-06)

> LLMs acquire a wide range of abilities during pre-training, but aligning LLMs under Reinforcement Learning with Human Feedback (RLHF) can lead to forgetting pretrained abilities, which is also known as the alignment tax.

Sentence 1 of 10. Phenomenon. Defined in the same sentence. Definition span (3 words): "forgetting pretrained abilities". Term appears 4 times in the abstract; present in the title. Abstract 246 words, 0 quantitative digits.

**`2309.12288` — the Reversal Curse**  
*The Reversal Curse: LLMs trained on "A is B" fail to learn "B is A"* (21 Sep 2023; retrieved 2026-09-06)

> This is the Reversal Curse.

Sentence 3 of 12. Phenomenon. Defined in the immediately preceding sentence. Definition span (26 words): "If a model is trained on a sentence of the form "A is B", it will not automatically generalize to the reverse direction "B is A"". Term appears 3 times in the abstract; present in the title. Abstract 257 words, 2 quantitative digits.

**`2309.17453` — attention sink**  
*Efficient Streaming Language Models with Attention Sinks* (29 Sep 2023; retrieved 2026-09-06)

> We observe an interesting phenomenon, namely attention sink, that keeping the KV of initial tokens will largely recover the performance of window attention.

Sentence 5 of 11. Phenomenon. Defined in the same sentence. Definition span (15 words): "that keeping the KV of initial tokens will largely recover the performance of window attention". Term appears 3 times in the abstract; present in the title. Abstract 239 words, 2 quantitative digits.

**`2310.01798` — intrinsic self-correction**  
*Large Language Models Cannot Self-Correct Reasoning Yet* (3 Oct 2023; retrieved 2026-09-06)

> Central to our investigation is the notion of intrinsic self-correction, whereby an LLM attempts to correct its initial responses based solely on its inherent capabilities, without the crutch of external feedback.

Sentence 5 of 7. Condition. Defined in the same sentence. Definition span (21 words): "whereby an LLM attempts to correct its initial responses based solely on its inherent capabilities, without the crutch of external feedback". Term appears 1 time in the abstract; absent in the title. Abstract 142 words, 0 quantitative digits.

**`2310.13548` — sycophancy**  
*Towards Understanding Sycophancy in Language Models* (20 Oct 2023; retrieved 2026-09-06)

> But human feedback may also encourage model responses that match user beliefs over truthful ones, a behaviour known as sycophancy.

Sentence 2 of 9. Phenomenon. Defined in the same sentence. Definition span (9 words): "model responses that match user beliefs over truthful ones". Term appears 5 times in the abstract; present in the title. Abstract 164 words, 0 quantitative digits.

**`2311.08596` — the FlipFlop effect**  
*Are You Sure? Challenging LLMs Leads to Performance Drops in The FlipFlop Experiment* (14 Nov 2023; retrieved 2026-09-06)

> A systematic study of ten LLMs on seven classification tasks reveals that models flip their answers on average 46% of the time and that all models see a deterioration of accuracy between their first and final prediction, with an average drop of 17% (the FlipFlop effect).

Sentence 4 of 6. Phenomenon. Defined in the immediately preceding sentence. Definition span (19 words): "all models see a deterioration of accuracy between their first and final prediction, with an average drop of 17%". Term appears 1 time in the abstract; absent in the title. Abstract 188 words, 3 quantitative digits. Also coins: the FlipFlop experiment.

**`2402.11436` — self-bias**  
*Pride and Prejudice: LLM Amplifies Self-Bias in Self-Refinement* (18 Feb 2024; retrieved 2026-09-06)

> In this paper, we formally define LLM's self-bias - the tendency to favor its own generation - using two statistics.

Sentence 3 of 8. Phenomenon. Defined in the same sentence. Definition span (7 words): "the tendency to favor its own generation". Term appears 3 times in the abstract; present in the title. Abstract 153 words, 0 quantitative digits.

**`2404.13076` — self-preference**  
*LLM Evaluators Recognize and Favor Their Own Generations* (15 Apr 2024; retrieved 2026-09-06)

> One such bias is self-preference, where an LLM evaluator scores its own outputs higher than others' while human annotators consider them of equal quality.

Sentence 3 of 8. Phenomenon. Defined in the same sentence. Definition span (19 words): "where an LLM evaluator scores its own outputs higher than others' while human annotators consider them of equal quality". Term appears 3 times in the abstract; absent in the title. Abstract 165 words, 1 quantitative digits. Also coins: self-recognition.

**`2406.05946` — shallow safety alignment**  
*Safety Alignment Should Be Made More Than Just a Few Tokens Deep* (10 Jun 2024; retrieved 2026-09-06)

> We refer to this issue as shallow safety alignment.

Sentence 4 of 10. Phenomenon. Defined in the immediately preceding sentence. Definition span (22 words): "safety alignment can take shortcuts, wherein the alignment adapts a model's generative distribution primarily over only its very first few output tokens". Term appears 3 times in the abstract; absent in the title. Abstract 208 words, 0 quantitative digits.

**`2406.07358` — sandbagging**  
*AI Sandbagging: Language Models can Strategically Underperform on Evaluations* (11 Jun 2024; retrieved 2026-09-06)

> These conflicting interests lead to the problem of sandbagging, which we define as strategic underperformance on an evaluation.

Sentence 3 of 11. Phenomenon. Defined in the same sentence. Definition span (5 words): "strategic underperformance on an evaluation". Term appears 3 times in the abstract; present in the title. Abstract 203 words, 1 quantitative digits.

**`2406.10162` — specification gaming**  
*Sycophancy to Subterfuge: Investigating Reward-Tampering in Large Language Models* (14 Jun 2024; retrieved 2026-09-06)

> In reinforcement learning, specification gaming occurs when AI systems learn undesired behaviors that are highly rewarded due to misspecified training goals.

Sentence 1 of 9. Phenomenon. Defined in the same sentence. Definition span (16 words): "occurs when AI systems learn undesired behaviors that are highly rewarded due to misspecified training goals". Term appears 5 times in the abstract; absent in the title. Abstract 198 words, 0 quantitative digits. Also coins: reward-tampering.

**`2411.07858` — Verbosity Compensation (VC)**  
*Verbosity $\neq$ Veracity: Demystify Verbosity Compensation Behavior of Large Language Models* (12 Nov 2024; retrieved 2026-09-06)

> In this paper, we discover an understudied type of undesirable behavior of LLMs, which we term Verbosity Compensation (VC), similar to the hesitation behavior of humans under uncertainty, where they respond with excessive words such as repeating questions, introducing ambiguity, or providing excessive enumeration.

Sentence 2 of 13. Phenomenon. Defined in the same sentence. Definition span (25 words): "similar to the hesitation behavior of humans under uncertainty, where they respond with excessive words such as repeating questions, introducing ambiguity, or providing excessive enumeration". Term appears 7 times in the abstract; present in the title. Abstract 268 words, 5 quantitative digits.

**`2412.14093` — alignment faking**  
*Alignment faking in large language models* (18 Dec 2024; retrieved 2026-09-06)

> We present a demonstration of a large language model engaging in alignment faking: selectively complying with its training objective in training to prevent modification of its behavior out of training.

Sentence 1 of 10. Phenomenon. Defined in the same sentence. Definition span (17 words): "selectively complying with its training objective in training to prevent modification of its behavior out of training". Term appears 6 times in the abstract; present in the title. Abstract 309 words, 3 quantitative digits. Also coins: alignment-faking reasoning.

**`2412.21187` — overthinking**  
*Do NOT Think That Much for 2+3=? On the Overthinking of o1-Like LLMs* (30 Dec 2024; retrieved 2026-09-06)

> This paper presents the first comprehensive study on the prevalent issue of overthinking in these models, where excessive computational resources are allocated for simple problems with minimal benefit.

Sentence 4 of 7. Phenomenon. Defined in the same sentence. Definition span (12 words): "where excessive computational resources are allocated for simple problems with minimal benefit". Term appears 2 times in the abstract; present in the title. Abstract 147 words, 0 quantitative digits.

**`2501.18585` — underthinking**  
*Thoughts Are All Over the Place: On the Underthinking of o1-Like LLMs* (30 Jan 2025; retrieved 2026-09-06)

> However, we identify a phenomenon we term underthinking, where o1-like LLMs frequently switch between different reasoning thoughts without sufficiently exploring promising paths to reach a correct solution.

Sentence 2 of 8. Phenomenon. Defined in the same sentence. Definition span (19 words): "where o1-like LLMs frequently switch between different reasoning thoughts without sufficiently exploring promising paths to reach a correct solution". Term appears 3 times in the abstract; present in the title. Abstract 172 words, 0 quantitative digits. Also coins: thought switching penalty (TIP).

**`2502.08235` — overthinking**  
*The Danger of Overthinking: Examining the Reasoning-Action Dilemma in Agentic Tasks* (12 Feb 2025; retrieved 2026-09-06)

> This paper introduces and analyzes overthinking in LRMs.

Sentence 2 of 10. Phenomenon. Defined in the immediately preceding sentence. Definition span (12 words): "A phenomenon where models favor extended internal reasoning chains over environmental interaction". Term appears 10 times in the abstract; present in the title. Abstract 182 words, 3 quantitative digits. Also coins: Analysis Paralysis; Rogue Actions; Premature Disengagement; overthinking score.

**`2502.17424` — emergent misalignment**  
*Emergent Misalignment: Narrow finetuning can produce broadly misaligned LLMs* (24 Feb 2025; retrieved 2026-09-06)

> We call this emergent misalignment.

Sentence 6 of 16. Phenomenon. Defined in the immediately preceding sentence. Definition span (12 words): "Training on the narrow task of writing insecure code induces broad misalignment". Term appears 4 times in the abstract; present in the title. Abstract 227 words, 0 quantitative digits.

**`2503.00555` — Safety Tax**  
*Safety Tax: Safety Alignment Makes Your Large Reasoning Models Less Reasonable* (1 Mar 2025; retrieved 2026-09-06)

> The discovered trade-off, which we name Safety Tax, should shed light on future endeavors of safety research on LRMs.

Sentence 6 of 8. Phenomenon. Defined in the immediately preceding sentence. Definition span (15 words): "there exists a trade-off between reasoning and safety capability with the sequential LRM production pipeline". Term appears 1 time in the abstract; present in the title. Abstract 163 words, 0 quantitative digits.

**`2503.08679` — Implicit Post-Hoc Rationalization**  
*Chain-of-Thought Reasoning In The Wild Is Not Always Faithful* (11 Mar 2025; retrieved 2026-09-06)

> We present preliminary evidence that this is due to models' implicit biases towards Yes or No, labeling this Implicit Post-Hoc Rationalization.

Sentence 4 of 7. Phenomenon. Defined in the immediately preceding sentence. Definition span (20 words): "models sometimes produce superficially coherent arguments to justify systematically answering Yes to both or No to both, despite the contradiction". Term appears 2 times in the abstract; absent in the title. Abstract 219 words, 4 quantitative digits. Also coins: Unfaithful Illogical Shortcuts.

**`2504.10694` — the jailbreak tax**  
*The Jailbreak Tax: How Useful are Your Jailbreak Outputs?* (14 Apr 2025; retrieved 2026-09-06)

> Our evaluation of eight representative jailbreaks across five utility benchmarks reveals a consistent drop in model utility in jailbroken responses, which we term the jailbreak tax.

Sentence 5 of 8. Metric. Defined in the same sentence. Definition span (9 words): "a consistent drop in model utility in jailbroken responses". Term appears 2 times in the abstract; present in the title. Abstract 181 words, 1 quantitative digits.

**`2505.06120` — get lost (in multi-turn conversation)**  
*LLMs Get Lost In Multi-Turn Conversation* (9 May 2025; retrieved 2026-09-06)

> In simpler terms, we discover that *when LLMs take a wrong turn in a conversation, they get lost and do not recover*.

Sentence 8 of 8. Phenomenon. Gestured at, not defined. Definition span (16 words): "when LLMs take a wrong turn in a conversation, they get lost and do not recover". Term appears 2 times in the abstract; present in the title. Abstract 188 words, 2 quantitative digits. Also coins: aptitude / unreliability decomposition.

**`2505.13988` — the hallucination tax**  
*The Hallucination Tax of Reinforcement Finetuning* (20 May 2025; retrieved 2026-09-06)

> In this work, we identify and systematically study a critical side effect of RFT, which we term the hallucination tax: a degradation in refusal behavior causing models to produce hallucinated answers to unanswerable questions confidently.

Sentence 3 of 7. Phenomenon. Defined in the same sentence. Definition span (15 words): "a degradation in refusal behavior causing models to produce hallucinated answers to unanswerable questions confidently". Term appears 1 time in the abstract; present in the title. Abstract 174 words, 2 quantitative digits.

**`2505.16894` — attention-locking**  
*Shadows in the Attention: Contextual Perturbation and Representation Drift in the Dynamics of Hallucination in LLMs* (22 May 2025; retrieved 2026-09-06)

> Results reveal (1) monotonic growth of hallucination frequency and representation drift that plateaus after 5--7 rounds; (2) relevant context drives deeper semantic assimilation, producing high-confidence "self-consistent" hallucinations, whereas irrelevant context induces topic-drift errors anchored by attention re-routing; and (3) convergence of JS-Drift ($\sim0.69$) and Spearman-Drift ($\sim0$) marks an "attention-locking" threshold beyond which hallucinations solidify and become resistant to correction.

Sentence 5 of 7. Condition. Defined in the same sentence. Definition span (10 words): "threshold beyond which hallucinations solidify and become resistant to correction". Term appears 1 time in the abstract; absent in the title. Abstract 178 words, 1 quantitative digits.

**`2505.22630` — stochastic chameleons**  
*Stochastic Chameleons: Irrelevant Context Hallucinations Reveal Class-Based (Mis)Generalization in LLMs* (28 May 2025; retrieved 2026-09-06)

> Our findings provide a more nuanced perspective on the stochastic parrot argument: through form-based training, LLMs can exhibit generalization leveraging abstractions, albeit in unreliable ways based on contextual cues -- what we term stochastic chameleons.

Sentence 6 of 6. Phenomenon. Defined in the same sentence. Definition span (14 words): "LLMs can exhibit generalization leveraging abstractions, albeit in unreliable ways based on contextual cues". Term appears 1 time in the abstract; present in the title. Abstract 214 words, 1 quantitative digits. Also coins: class-based (mis)generalization.

**`2506.11930` — Feedback Friction**  
*Feedback Friction: LLMs Struggle to Fully Incorporate External Feedback* (13 Jun 2025; retrieved 2026-09-06)

> Surprisingly, even under these near-ideal conditions, solver models consistently show resistance to feedback, a limitation that we term Feedback Friction.

Sentence 7 of 10. Phenomenon. Defined in the same sentence. Definition span (7 words): "solver models consistently show resistance to feedback". Term appears 2 times in the abstract; present in the title. Abstract 223 words, 1 quantitative digits.

**`2507.02778` — Self-Correction Blind Spot**  
*Self-Correction Bench: Uncovering and Addressing the Self-Correction Blind Spot in Large Language Models* (3 Jul 2025; retrieved 2026-09-06)

> Testing 14 open-source non-reasoning models reveals a 64.5% Self-Correction Blind Spot: models correct external errors but fail on identical internal ones, proving the capability exists but is not activated.

Sentence 4 of 8. Metric. Defined in the same sentence. Definition span (10 words): "models correct external errors but fail on identical internal ones". Term appears 4 times in the abstract; present in the title. Abstract 215 words, 5 quantitative digits.

**`2510.07777` — context drift**  
*Drift No More? Context Equilibria in Multi-Turn LLM Interactions* (9 Oct 2025; retrieved 2026-09-06)

> A recurring challenge in this setting is context drift: the gradual divergence of a model's outputs from goal-consistent behavior across turns.

Sentence 2 of 8. Phenomenon. Defined in the same sentence. Definition span (12 words): "the gradual divergence of a model's outputs from goal-consistent behavior across turns". Term appears 3 times in the abstract; absent in the title. Abstract 218 words, 0 quantitative digits.

**`2601.00624` — YapScore**  
*Do Chatbot LLMs Talk Too Much? The YapBench Benchmark* (2 Jan 2026; retrieved 2026-09-06)

> Our primary metric, YapScore, measures excess response length beyond the baseline in characters, enabling comparisons across models without relying on any specific tokenizer.

Sentence 5 of 9. Metric. Defined in the same sentence. Definition span (9 words): "measures excess response length beyond the baseline in characters". Term appears 3 times in the abstract; absent in the title. Abstract 222 words, 1 quantitative digits. Also coins: YapIndex.

**`2604.28031` — the knows-but-violates (KBV) rate**  
*Models Recall What They Violate: Constraint Adherence in Multi-Turn LLM Ideation* (30 Apr 2026; retrieved 2026-09-06)

> The knows-but-violates (KBV) rate, measuring constraint non-compliance despite preserved recall, ranges from 8% to 99% across models.

Sentence 5 of 9. Metric. Defined in the same sentence. Definition span (6 words): "measuring constraint non-compliance despite preserved recall". Term appears 3 times in the abstract; absent in the title. Abstract 178 words, 7 quantitative digits.

**`2606.16011` — answer stability**  
*Who Flips? Self- and Cross-Model Counterarguments Reveal Answer Instability in LLMs* (14 Jun 2026; retrieved 2026-09-06)

> We introduce a controlled protocol for evaluating answer stability: after a model answers a multiple-choice question correctly, we challenge the model's answer with a coherent argument for an incorrect option and measure whether the model flips.

Sentence 3 of 10. Metric. Gestured at, not defined. Definition span (27 words): "after a model answers a multiple-choice question correctly, we challenge the model's answer with a coherent argument for an incorrect option and measure whether the model flips". Term appears 1 time in the abstract; absent in the title. Abstract 197 words, 6 quantitative digits.
## Counts

### Where a coinage sits: setup, finding, or close

Hand-coded by what the sentence does. **Setup 20, finding 16, close 3, of 39.**

The mechanical version of the same question, sentence position as a fraction of the abstract:
first third 17, middle third 17, last third 5. Three abstracts put the term in the final sentence
(`2305.13534` hallucination snowballing, `2505.06120` get lost, `2505.22630` stochastic
chameleons) and three put it in the first (`2412.14093` alignment faking, `2309.06256` the
alignment tax, `2406.10162` specification gaming).

The two positions do different work, and the difference is visible in what surrounds them.

A **setup** coinage names the object of study before any result. It is almost always attached to
a definition on the spot, and the sentence carries no number: median quantitative digits for the
20 setup abstracts is 0.5 against 1.5 for the 16 finding abstracts. "In reinforcement learning,
specification gaming occurs when AI systems learn undesired behaviors that are highly rewarded due
to misspecified training goals" is the whole first sentence of `2406.10162`, and everything after
it is about that named thing.

A **finding** coinage names something the paper has just shown. The naming clause is short,
often a subordinate tail on a result sentence, and the definition either precedes it or is folded
into the same clause: "solver models consistently show resistance to feedback, a limitation that
we term Feedback Friction" (`2506.11930`); "which we term the jailbreak tax" (`2504.10694`);
"The discovered trade-off, which we name Safety Tax" (`2503.00555`).

A **close** coinage restates the paper in plain words after the results are in, and it is the
rarest of the three (3 of 39). All three are the plain-language sentence: "We refer to this
phenomenon as hallucination snowballing: an LM over-commits to early mistakes, leading to more
mistakes that it otherwise would not make"; "In simpler terms, we discover that when LLMs take a
wrong turn in a conversation, they get lost and do not recover"; "what we term stochastic
chameleons". The nearest neighbour of this paper is in that group, and its close is the only place
in the abstract where the title phrase is echoed.

### Is a coined term defined on introduction, and in how many words

**28 of 39 are DEFINED in the same sentence. 8 are ADJACENT, defined in the sentence immediately
before. 2 are GESTURED at. 1 is USED with nothing attached.** So 36 of 39 carry a definition
within one sentence of the name, and 38 of 39 carry a definition somewhere.

Definition length, counted mechanically on the verbatim span:

| Class | n | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|---|
| DEFINED (same sentence) | 28 | 3 | 9 | 12 | 16 | 26 | 13.3 |
| ADJACENT (previous sentence) | 8 | 12 | 15 | 19.5 | 21 | 26 | 18.4 |
| GESTURED | 2 | 16 | 16 | 21.5 | 27 | 27 | 21.5 |
| All with a span | 38 | 3 | 10 | 14.5 | 19 | 27 | 14.8 |

The full distribution of the 28 same-sentence definitions, in words:
3, 5, 6, 7, 7, 9, 9, 9, 10, 10, 10, 11, 11, 12, 12, 13, 14, 15, 15, 16, 16, 17, 19, 19, 21, 25,
26, 26.

**A definition costs a median of 12 words and a quarter of them cost 9 or fewer.** The shortest
are the ones that need no machinery: "forgetting pretrained abilities" (3 words, `2309.06256`),
"strategic underperformance on an evaluation" (5, `2406.07358`), "measuring constraint
non-compliance despite preserved recall" (6, `2604.28031`), "the tendency to favor its own
generation" (7, `2402.11436`), "solver models consistently show resistance to feedback"
(7, `2506.11930`). The longest are the ones carrying a mechanism as well as a meaning: 26 words
for FActScore, which has to say what the metric computes, and 26 for Degeneration-of-Thought,
which has to say what the model does and when.

The grammar is stable across the corpus. **14 of the 39 use an explicit naming formula** in the
introducing sentence: "we term" (6), "we refer to this as" (3), "we define" (2), "we call this",
"we name", "labeling this" (1 each). **2 of the 39 attribute the term instead of claiming it**,
with "known as" (`2310.13548` sycophancy, `2309.06256` the alignment tax). The remaining 23 name
the thing without announcing that they are naming it. **8 of the 39 naming sentences use a colon**
to carry the definition. No definition in the corpus runs to a second sentence.

### Do coinage-carrying abstracts run longer than 161 words

Yes, and by a wide margin. **Median 194 words against the 161-word median of the 47-abstract
ACL 2026 systematic sample. 32 of the 39 run longer than 161 words.**

| | min | p25 | median | p75 | max | mean |
|---|---|---|---|---|---|---|
| Words | 114 | 172 | 194 | 218 | 309 | 194.3 |
| Sentences | 5 | 7 | 8 | 10 | 16 | 8.7 |

Two things are worth separating here. The corpus median of 194 is 33 words above the venue
median, but the definition itself accounts for only about 12 of those words. The rest is genre:
these are behavioural-analysis and negative-result papers, which run longer than the method papers
that dominate an unfiltered ACL volume. The reading that survives is the narrow one. **A coinage
plus its definition costs on the order of 12 to 15 words**, and abstracts that spend them are not
short abstracts.

The seven abstracts at or below the 161-word venue median show the floor: 114 words
(`2302.09664` semantic entropy, `2305.13534` hallucination snowballing), 141
(`2302.00093` distractibility), 142 (`2310.01798` intrinsic self-correction), 147
(`2412.21187` overthinking), 153 (`2402.11436` self-bias), 155 (`2308.12032` IFD). Each of the
seven defines its term. A coinage does not require a long abstract.

### Is a metric coinage handled differently from a phenomenon coinage

**9 of the 39 coinages are metrics, 28 are phenomena, 2 are conditions.** Three differences are
visible, and the third is the one that matters for this paper.

**Position.** Metric coinages go in the setup: 6 of 9 setup, 3 of 9 finding, 0 close. Phenomenon
coinages spread: 13 setup, 12 finding, 3 close. A metric is machinery the reader needs before the
results, so it arrives before them. A phenomenon can be named at any point, including after the
evidence for it.

**Definedness.** 8 of 9 metric coinages are defined in the same sentence; the ninth
(`2606.16011` answer stability) is gestured at by describing the protocol. No metric in the corpus
is left undefined. Among phenomena, 18 of 28 are defined in the same sentence, 8 in the preceding
one, and 2 carry no definition.

**Does a coined metric arrive with its number attached.** Mostly not. **4 of 9 metric coinages
give the metric's own value anywhere in the abstract, and only 2 of 9 give it in the naming
sentence.** The two that fuse the number to the name are:

> Testing 14 open-source non-reasoning models reveals a 64.5% Self-Correction Blind Spot: models
> correct external errors but fail on identical internal ones, proving the capability exists but
> is not activated. (`2507.02778`)

> The knows-but-violates (KBV) rate, measuring constraint non-compliance despite preserved recall,
> ranges from 8% to 99% across models. (`2604.28031`)

Both are 2026 papers, and both read as a single move: the name, its definition, and its magnitude
in one sentence. Two more attach the value one or two sentences later: the jailbreak tax
(`2504.10694`, "a drop of up to 92% in accuracy" in the next sentence) and FActScore
(`2305.14251`, "ChatGPT only achieves 58%"). The remaining five name the metric and never report
a value for it: IFD, semantic entropy, distractibility, YapScore, answer stability. YapScore is
the sharpest case, since the paper is a benchmark whose whole purpose is that number, and the
abstract reports only "an order-of-magnitude spread in median excess length".

Across the whole corpus, only **4 of 39 naming sentences carry a quantitative digit at all**
(`2507.02778`, `2604.28031`, `2311.08596` the FlipFlop effect, `2505.16894` attention-locking).
Naming and quantifying are usually two different sentences.

### Does coining co-occur with carrying digits

Weakly, and the effect runs through genre rather than through the coinage.

**24 of 39 coinage abstracts carry at least one quantitative digit; 15 carry none.** Median 1,
p75 2, max 7, mean 1.6. The venue baseline from the 47-abstract ACL 2026 sample is 31 of 47
carrying no quantitative digit at all, median 0.

So a coinage abstract is roughly twice as likely to carry a digit as an unfiltered venue abstract
(62% against 34%). But the naming sentence itself is almost never the sentence carrying it (4 of
39), and 15 coinage abstracts carry no digit anywhere while still naming and defining a term.
`2503.00555` names Safety Tax in a 163-word abstract with zero digits. `2406.05946` names shallow
safety alignment in 208 words with zero digits. **Naming a thing and quantifying it are separable,
and roughly two in five of these abstracts do the first without the second.**

### How often does a paper coin more than one term, and does it read as cluttered

**11 of 39 abstracts coin more than one term.** The counts, with the second and further terms:

| ID | Primary | Additional | Abstract words |
|---|---|---|---|
| `2306.05685` | self-enhancement bias | position bias; verbosity bias | 184 |
| `2311.08596` | the FlipFlop effect | the FlipFlop experiment | 188 |
| `2404.13076` | self-preference | self-recognition | 165 |
| `2406.10162` | specification gaming | reward-tampering | 198 |
| `2412.14093` | alignment faking | alignment-faking reasoning | 309 |
| `2501.18585` | underthinking | thought switching penalty (TIP) | 172 |
| `2502.08235` | overthinking | Analysis Paralysis; Rogue Actions; Premature Disengagement; overthinking score | 182 |
| `2503.08679` | Implicit Post-Hoc Rationalization | Unfaithful Illogical Shortcuts | 219 |
| `2505.06120` | get lost | the aptitude / unreliability decomposition | 188 |
| `2505.22630` | stochastic chameleons | class-based (mis)generalization | 214 |
| `2601.00624` | YapScore | YapIndex | 222 |

Multi-coinage abstracts are not longer (median 188 words against 195.5 for single-coinage) and
carry no more digits (median 1 in both). The reader can judge the clutter directly. The two ends
of the range:

> This paper introduces and analyzes overthinking in LRMs. A phenomenon where models favor
> extended internal reasoning chains over environmental interaction. Through experiments on
> software engineering tasks using SWE Bench Verified, we observe three recurring patterns:
> Analysis Paralysis, Rogue Actions, and Premature Disengagement. We propose a framework to study
> these behaviors, which correlates with human expert assessments, and analyze 4018 trajectories.
> We observe that higher overthinking scores correlate with decreased performance [...]
> (`2502.08235`, five named things in 182 words)

> One such bias is self-preference, where an LLM evaluator scores its own outputs higher than
> others' while human annotators consider them of equal quality. But do LLMs actually recognize
> their own outputs when they give those texts higher scores, or is it just a coincidence? In this
> paper, we investigate if self-recognition capability contributes to self-preference.
> (`2404.13076`, two named things in 165 words, each defined, and the second is the mechanism for
> the first)

The pattern across the 11: multi-coinage reads cleanly when the second term is **subordinate** to
the first, either its mechanism (`2404.13076` self-recognition explains self-preference;
`2505.22630` class-based misgeneralization produces stochastic chameleons), its measure
(`2502.08235` overthinking score for overthinking; `2601.00624` YapIndex aggregates YapScore), or
its setting (`2311.08596` the FlipFlop experiment produces the FlipFlop effect). It reads as a
list when the terms are **coordinate**: `2306.05685` gives "position, verbosity, and
self-enhancement biases" in one clause, none of them defined, and the three are indistinguishable
from each other on the page.

### What happens when a term is used without being defined

Three abstracts in the corpus name something without defining it. In two of the three the term was
already established in the literature, and in the third the definition is carried by the title.

**`2306.05685` (self-enhancement bias), USED.** "We examine the usage and limitations of
LLM-as-a-judge, including position, verbosity, and self-enhancement biases, as well as limited
reasoning ability, and propose solutions to mitigate some of them." Not established at the time:
this abstract is where the three names enter the LLM-judge literature, and none of them is
defined. The result is that the terms function as a list of topics rather than as claims, and the
reader who does not already know what self-enhancement bias means learns nothing about it from
the abstract.

**`2505.06120` (get lost), GESTURED.** "In simpler terms, we discover that when LLMs take a wrong
turn in a conversation, they get lost and do not recover." The phrase is not defined as a term,
and it works anyway, because the two sentences before it have already given the mechanism
(assumptions in early turns, premature final solutions, over-reliance on them) and the sentence
before that has given the decomposition into aptitude and unreliability. The plain-language
sentence is a summary of a definition already delivered, not a substitute for one.

**`2606.16011` (answer stability), GESTURED.** "We introduce a controlled protocol for evaluating
answer stability: after a model answers a multiple-choice question correctly, we challenge the
model's answer with a coherent argument for an incorrect option and measure whether the model
flips." The colon expansion defines the protocol, not the quantity, and the number that is
eventually reported is a flip rate rather than a stability value. The term never acquires a
referent.

Three further abstracts use a term that **is** established and attribute it as such, and all three
still define it: sycophancy ("a behaviour known as sycophancy", with the definition ahead of the
attribution, `2310.13548`), the alignment tax ("which is also known as the alignment tax", 3-word
definition, `2309.06256`), and specification gaming (defined in the first sentence, `2406.10162`).
**Established terms in this corpus are defined at a rate of 3 of 3; the terms that go undefined
are the new ones.** That is the reverse of what convenience would suggest, and it is the strongest
regularity in this section: an author who has just coined a term is the one most likely to assume
the reader can infer it.

### Screened out, and why

15 of the 54 fetched papers were dropped. The reasons divide into two groups, and the first group
is directly informative.

**Coinage in the title, absent from the abstract (4 papers).** Verified by string search on the
fetched abstract text.

| ID | Title coinage | Occurrences in abstract |
|---|---|---|
| `2307.03172` | "Lost in the Middle" | 0 ("lost" appears 0 times) |
| `2506.06941` | "The Illusion of Thinking" | 0 ("illusion" appears 0 times) |
| `2401.05566` | "Sleeper Agents" | 0 |
| `2604.14414` | "The Autocorrelation Blind Spot" | 0 ("blind spot" appears 0 times) |

"Lost in the middle" is now the field's standard name for the position effect, and it entered the
field from a title that the abstract never uses. The abstract instead describes the effect twice
in plain words ("performance is often highest when relevant information occurs at the beginning or
end of the input context, and significantly degrades when models must access relevant information
in the middle of long contexts"). This is a live alternative to putting a coinage in an abstract:
put it in the title, and let the abstract describe the thing.

**No coined term anywhere in the abstract (11 papers).** `2406.01297` (Kamoi, the self-correction
survey named as an anchor: the abstract contains no coinage, and "direct refinement" does not
appear in it, nor does "refinement"), `2305.04388`, `2310.12397`, `2311.08516`, `2402.08939`,
`2311.07911`, `2505.05410`, `2412.18547`, `2509.06770`, `2602.04210`, `2606.10315`. Several of
these name a released artifact (IFEval, BIG-Bench Mistake, R-GSM, MaxFlip, Scalable Interactive
Oversight), which the brief excludes.

One note for the project record rather than for this question: the abstract of `2601.00624`
(YapBench) names YapScore and YapIndex and **does not contain the string "tax" at all**. The
manuscript's related-work paragraph describes "the independently coined ``YapTax'' of
\citet{borisov2026yapbench}". That term may well appear in the paper body, but it is not in the
abstract, so the body should be checked before the sentence stands.

## What the evidence supports for this paper's three candidates

The live abstract (`paper/sections/abstract_v2.tex`, v13) runs 196 words in 9 sentences with one
result statistic, measured by the same script used above. It uses "undirected" three times and
contains neither "tax" nor "robust". Against the corpus, its length sits just above the corpus
p25 (172) and 35 words above the venue median (161), and its digit count of 1 is exactly the
corpus median.

### The state of each candidate, measured

| Candidate | Kind | Already in the abstract | Definition, verbatim | Def. words | Corpus position for this kind |
|---|---|---|---|---|---|
| undirected revision | condition | Yes, 3 times, already defined on first use | "that carry no information about what to change" | 8 | setup (13 of 28 phenomena, 6 of 9 metrics) |
| revision robustness | phenomenon (a property) | No | "a model's willingness to leave sufficient work alone" | 8 | close, but only 3 of 39 sit there |
| revision tax | metric | No | "the tokens spent past the quality-optimal stopping point" | 8 | setup (6 of 9 metric coinages); 0 of 9 in the close |

All three definitions come in at 8 words, below the corpus median of 12 and at the corpus p25 of
9. **None of the three is expensive.** The question is not cost, it is placement and whether the
rest of the abstract carries the topic the term opens.

### undirected revision: already a coinage, and it should stay unannounced

Sentence 2 of the current abstract reads: "a user unable to name what is wrong falls back on
undirected requests that carry no information about what to change." That is the corpus's standard
setup move performed in full: the term, in the setup, with an 8-word relative-clause definition
attached on first use. It is then used twice more, putting recurrence at 3, exactly the corpus
median.

The only change the corpus would suggest is whether to announce it, and the corpus says no. **14
of 39 abstracts use an explicit naming formula ("we term", "we call this"); 23 of 39 name the
thing without announcing that they are naming it.** "Undirected" is a plain English modifier, and
"which we call undirected revision" would spend four words claiming ownership of a word the reader
would otherwise absorb without friction. Leave it as it is.

### revision tax: keep it out, and the reason is topical, not budgetary

The prior decision recorded in `ABSTRACT_NOTES.md` was to decline it because it "opens a cost
topic nothing else here supports". The corpus supports that decision on independent grounds.

**Metric coinages in this corpus sit in the setup: 6 of 9 setup, 3 of 9 finding, 0 of 9 close.**
A metric is machinery, and machinery arrives before the results that use it. A revision tax
introduced in the setup would commit the abstract to a cost frame from sentence 2 or 3 onward, and
the current abstract's argument is about quality, not tokens. The sentence budget is the smaller
problem: a setup sentence establishing token cost as the axis runs 15 to 20 words on top of the
8-word definition, taking a 196-word abstract to roughly 220, which is the corpus p75.

**5 of 9 metric coinages never report the metric's own value in the abstract** (IFD, semantic
entropy, distractibility, YapScore, answer stability), and those five read as the weakest of the
nine, because a named quantity with no magnitude gives the reader a label and no fact. The revision
tax has a magnitude (62.1% of tokens generated past the peak), so it would not have that problem.
But the abstract currently carries one statistic. Adding a second, on an axis nothing else in the
abstract touches, is what the number-discipline pass already rejected twice.

If the paper does put it in later, the two 2026 abstracts show the form that works, and both do the
whole job in one sentence: `2507.02778` ("Testing 14 open-source non-reasoning models reveals a
64.5% Self-Correction Blind Spot: models correct external errors but fail on identical internal
ones") and `2604.28031` ("The knows-but-violates (KBV) rate, measuring constraint non-compliance
despite preserved recall, ranges from 8% to 99% across models"). Name, definition, magnitude,
one sentence, roughly 25 to 30 words.

### revision robustness: the one candidate with a place to go, and the placement has a cost

This is the paper's proposal, and it currently lives in the discussion and the conclusion. Putting
it in the abstract means putting it in the close, because it is a claim about what the field should
measure and nothing earlier in the abstract prepares it.

The corpus is thin there and the thinness is informative. **3 of 39 coinages sit in the final
sentence, and all three restate a finding in plain words rather than proposing anything**:
hallucination snowballing ("an LM over-commits to early mistakes"), get lost ("when LLMs take a
wrong turn in a conversation, they get lost and do not recover"), stochastic chameleons ("LLMs can
exhibit generalization leveraging abstractions, albeit in unreliable ways"). None of the three
closes on a recommendation. The nearest neighbour is in that group, and the move it makes is
restating the paper's finding in the plainest available words, not asking the field for anything.

Two consequences follow.

First, a close of the form "Revision robustness, a model's willingness to leave sufficient work
alone, deserves evaluation alongside first-turn capability" (the version in Tania's draft) would
be doing something no abstract in this corpus does: ending on a proposal rather than on the result.
That is not a reason it cannot work, but it should be chosen knowingly, and it displaces the
current close, which states the finding and its reversal ("undirected revision lowers the quality
of work that was already sufficient, and that naming the fault reverses the effect"). The corpus
says the current close is the one that matches the genre.

Second, if the term is wanted in the abstract without giving up the finding-close, the corpus's
other option is the **finding** position, 16 of 39, where the naming clause is a short tail on a
result sentence. The existing sentence 8 is the natural host, because it already reports the
property: "For every model the first draft rates highest, and blind readers prefer it to the final
version only slightly more often than chance." A tail naming the absent property costs about 10
words and does not disturb the close.

### What to do

**One coinage, not three.** 11 of 39 abstracts coin more than one term, and the ones that read
cleanly are the ones where each further term is subordinate to the first: its mechanism, its
measure, or its setting. The three candidates here do form that hierarchy (undirected revision is
the condition, revision robustness is the property it tests, the revision tax is the cost of
failing it), so a two-term abstract is defensible in principle. But the corpus's clean multi-term
abstracts name the subordinate term in the same clause as the primary one, and none of them
introduces a second axis of measurement. Two of these three would.

The ranking the evidence supports:

1. **Keep "undirected revision" where it is.** It is already the abstract's coinage, already in
   the corpus-standard setup position, already defined in 8 words on first use, already at the
   median recurrence, and unannounced, which is the majority form. Nothing needs to change.
2. **Add "revision robustness" only if it can be attached to sentence 8 as a short tail**, at a
   cost of roughly 10 words, rather than as a new closing proposal. If it must be the close, that
   is a deliberate departure from the genre, made against 3 of 3 close-position exemplars.
3. **Leave "revision tax" out of the abstract.** Its position in this corpus is the setup, and the
   setup is the one place the current abstract cannot carry a cost topic without rewriting its
   argument. It reads well where it is, in the results.

The strongest single warning the corpus gives is not about placement. **The one abstract that
names new terms and defines none of them (`2306.05685`, "position, verbosity, and self-enhancement
biases") is also the one whose terms read as a list of topics rather than as claims, and all three
established terms in the corpus are defined despite being established.** Whatever goes in, define
it in the same sentence, in 8 to 12 words. That is what 28 of 39 abstracts do, and it is the one
thing every strong exemplar here has in common.

## Files

- Fetched abstracts, verbatim, with retrieval dates: `.workspace/scratch/coinage_abstracts.json`
- Coded corpus with mechanical measurements: `.workspace/scratch/coinage_coded.json`
- Scripts: `.workspace/scratch/coinage_scripts/` (`02_fetch.py`, `03_measure.py`, `04_code.py`,
  `05_stats.py`, `06_tables.py`)
