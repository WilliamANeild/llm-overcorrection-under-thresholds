# Study scale in this literature

Retrieved 2026-09-02. 38 papers.

Method. Every number below was read in a fetched document: the arXiv abstract page for the
verbatim abstract, and the arXiv HTML render (`arxiv.org/html/<ID>`, falling back to
`ar5iv.labs.arxiv.org/html/<ID>` or the PDF) for the experimental setup. No study's size was
recalled or estimated. Where a paper states a total, it is marked *stated*; where a total is the
product of numbers the paper states separately, it is marked *derived* and the arithmetic is
shown. Where neither was available, the cell reads "not determinable" rather than carrying a
guess.

Two distinctions govern the whole document and must travel with any use of it.

**Benchmark release versus controlled experiment.** A benchmark release is built to be large:
its instance count is a design target, and evaluating 21 models on 4,208 turns is what the
artifact is for. A controlled experiment holds a design fixed and varies one thing, and its N is
governed by how many cells the design has. Comparing 720 conversations against a
200,000-conversation simulation or a 240,000-vote arena without saying which is which produces a
meaningless ratio. The two are tabulated and summarised separately throughout.

**Unit mismatch on "tasks."** In this literature a "task" almost always means a task type or a
dataset: GSM8K, HumanEval, Spider. This paper's "40 tasks" are individual scenarios grouped into
5 domains. The comparable unit to the field's task count is the 5 domains; the 40 scenarios are
closer to what the field calls instances. Both readings are given wherever the comparison turns
on it, because reporting only the flattering one would be a unit substitution rather than a
finding.

---

## Corpus

Type: **B** = benchmark or dataset release, **C** = controlled experiment, **S** = survey.
"Instances" is the trial, episode, conversation or problem count of the main experiment.

| # | Paper (first author, short title) | ID | Type | Models | Tasks / datasets | Instances (main experiment) | Scored outputs | Turns / iterations | Human annotators / judgements |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Madaan, *Self-Refine* | 2303.17651 | C | 3 primary (GPT-3.5, ChatGPT, GPT-4); Codex, Vicuna-13B on subsets | 7 | 4,441 summed across tasks (1,000 / 372 / 1,000 / 300 / 1,319 / 250 / 200) *derived* | not determinable (up to 9 calls per instance) | up to 4 refine iterations | authors as raters; ~450 A/B judgements (150 examples on each of 3 tasks) |
| 2 | Huang, *LLMs Cannot Self-Correct Reasoning Yet* | 2310.01798 | C | 4 | 3 | GPT-3.5 on full sets (1,319 / 1,221 / 100); other models 200 / 200 / 100 | not stated | max 2 correction rounds, 3 calls per round | none |
| 3 | Kamoi, *When Can LLMs Actually Correct Their Own Mistakes?* | 2406.01297 | S | n/a | n/a | paper count not stated | n/a | n/a | none |
| 4 | Pan, *Automatically Correcting LLMs* | 2308.03188 | S | n/a | n/a | 71 methods catalogued (count of table rows, *derived*) | n/a | n/a | none |
| 5 | Tyen, *LLMs cannot find reasoning errors* | 2311.08516 | C + release | 5 | 5 | 2,186 CoT traces | not determinable | up to 8 resamples at the mistake step | at least 3 per trace on ~1,200 traces, so at least 3,600 annotations *derived*; Krippendorff alpha 0.979 to 0.998; headcount not determinable |
| 6 | Stechly, *GPT-4 Doesn't Know It's Wrong* | 2310.12397 | C | 1 (GPT-4) | 1 (graph colouring) | 100 | 500 in the verification sub-experiment (5 colouring types x 100) *derived* | up to 16 queries per instance | none |
| 7 | Laban, *LLMs Get Lost In Multi-Turn Conversation* | 2505.06120 | C (simulation) | 15 | 6 | 600 sharded instructions; 200,000+ simulated conversations *stated* | 200,000+ conversations *stated* | equal to shard count; sharding study grows 2 to 8 | several hundred conversations inspected; count not stated |
| 8 | Sharma, *Towards Understanding Sycophancy* | 2310.13548 | C | 5 | 4 free-form tasks plus 5 QA datasets | varies by sub-study; 266 misconceptions; 15K preference pairs analysed | not stated | single exchange | 5 humans per pair on the misconception set; total not stated |
| 9 | Kwan, *MT-Eval* | 2401.16745 | B | 11 | 4 categories | 168 dialogues, 1,170 turns | 12,870 (1,170 x 11) *derived*, plus single-turn counterparts | mean 6.96, range 3 to 12 | 5 graduate students on 180 instances, so ~900 judgements *derived*; Cohen kappa 0.58 |
| 10 | Bai, *MT-Bench-101* | 2402.14762 | B | 21 | 13 | 1,388 dialogues, 4,208 turns | 88,368 (4,208 x 21) *derived* | 3.03 mean *derived* | 5 annotators screened the set; 5 experts rated 100 dialogues |
| 11 | Wang, *MINT* | 2309.10691 | B | 20 | 8 datasets | 586, filtered from 29,307 | not stated | k in {1,2,3,4,5} | 2 annotators on 113 trajectories |
| 12 | Zheng, *MT-Bench and Chatbot Arena* | 2306.05685 | B | 6 (MT-Bench); 50+ (Arena) | 8 categories | MT-Bench 80 questions, 160 question-turns; Arena open | 960 (80 x 6 x 2) *derived* | 2 (MT-Bench) | MT-Bench 58 experts, ~3,000 votes; Arena ~30,000 votes from 2,114 IPs |
| 13 | Liu, *G-Eval* | 2303.16634 | C | 2 evaluator backbones | 2 tasks, 3 benchmarks | not determinable: the paper states no dataset sizes | not determinable | single rating | none new; correlates against existing human ratings |
| 14 | Kim, *Prometheus* | 2310.08491 | B | Prometheus 13B against GPT-4 and ChatGPT | 4 eval benchmarks | Feedback Collection 1K rubrics, 20K instructions; eval sets 80 / 80 / 200 / 221 | 100K responses and feedback *stated* | single rating | 9 crowdworkers in three groups of 3; item count not determinable |
| 15 | Dubois, *AlpacaFarm* | 2305.14387 | B | 11 | 1 instruction set | 10,000 preference pairs; 805 eval instructions | 10,000 pairs *stated* | single turn | 16 annotators retained from a pool of 34; 10,000 pairs; 13 simulated annotators |
| 16 | Chiang, *Chatbot Arena* | 2403.04132 | B | more than 50 | open prompts | ~240,000 votes | ~480,000 responses (240K x 2) *derived lower bound* | not determinable | ~90,000 users, ~240,000 votes, 100+ languages |
| 17 | Shinn, *Reflexion* | 2303.11366 | C | GPT-3, GPT-3.5, GPT-4; StarChat-beta in an ablation | 5 datasets in 3 families | AlfWorld 134, HotpotQA 100, LeetcodeHardGym 40; HumanEval and MBPP counts not stated | not determinable | 12 trials (AlfWorld); until 3 consecutive failures (HotpotQA) | none |
| 18 | Chen, *Teaching LLMs to Self-Debug* | 2304.05128 | C | 4 | 3 | TransCoder 560, MBPP 500, Spider dev size not stated | not determinable | max 10 debugging turns, most succeed within 3 | none |
| 19 | Olausson, *Is Self-Repair a Silver Bullet?* | 2306.09896 | C + human study | 3 | 2 | APPS 300 tasks; HumanEval count not stated | repair-tree design, not reducible to one total | one feedback and one repair round in the human arm | 16 participants (15 graduate students, 1 engineer); 40 programs each seen by 2, so 80 judgements *derived* |
| 20 | Valmeekam, *Can LLMs Really Improve by Self-critiquing?* | 2310.08118 | C | 1 (GPT-4) | 1 (Blocksworld) | 100 | not stated; mean 3.48 iterations | cap 15 | none; VAL is the verifier |
| 21 | Valmeekam, *PlanBench* | 2206.10498 | B | 2 | 8 task types, 2 domains plus obfuscated variants | Blocksworld 600 (+500 for generalisation), Logistics 285; ~26,250 prompts | ~52,500 (26,250 x 2) *derived* | single turn | none |
| 22 | Qu, *Recursive Introspection (RISE)* | 2407.18219 | C | 3 fine-tuned, 2 comparators | 2 | not determinable: dataset sizes sit in an appendix that could not be retrieved | not determinable | 5-turn introspection; 2 training iterations | none |
| 23 | Lee, *CoAuthor* | 2201.06796 | B | 1 (GPT-3, 4 instances) | 2 tasks, 20 prompts | 1,445 writing sessions | ~17,051 queries (1,445 x 11.8) *derived* | 11.8 queries per session | 63 writers |
| 24 | Bansal, *Does the Whole Exceed its Parts?* | 2006.14779 | C | 1 per dataset | 3 datasets, 5 conditions each | 1,626 recruited, ~1,439 retained | n/a | single-shot per item | ~1,439 participants; ~56,950 decisions (475x50 + 464x50 + 500x20) *derived* |
| 25 | Bucinca, *To Trust or to Think* | 2102.09692 | C | 1 simulated AI | 1 task, 6 conditions | 260 recruited, 199 retained | n/a | 24 scored trials each | 199 participants; 4,776 decisions (199 x 24) *derived* |
| 26 | Vasconcelos, *Explanations Can Reduce Overreliance* | 2212.06823 | C | 1 simulated AI | 1 task, 5 studies | N=731 across five studies; Study 1 N=340 | n/a | 30 test trials (Study 1) | 731 participants; Study 1 alone ~10,200 decisions *derived*; total across studies not determinable |
| 27 | Chiang and Lee, *Can LLMs Be an Alternative to Human Evaluations?* | 2305.01937 | C | 4 evaluator LLMs | 2 | 400 stories, 300 adversarial pairs | 400 stories rated 3x by three of the LLMs, 1x by ChatGPT | single rating | 3 certified teachers on 700 items, 2,100 ratings *derived* |
| 28 | Shankar, *Who Validates the Validators?* | 2404.12272 | C (qualitative) | not determinable | 2 offline pipelines, 1 study task | 84 medical and 100 product outputs; 100 tweets in the study | 184 offline outputs | iterative interface use | 9 industry practitioners; grading varied by participant, "some stopped after 10 grades"; 2 authors graded all outputs |
| 29 | Xu, *The Earth is Flat because...* | 2312.09085 | C | 5 | 3 source QA datasets | 1,952 entries, from 1,500 curated questions | not stated | up to 4 | 5 annotators for validation; 2 authors examined 48 failed generations |
| 30 | Panickssery, *LLM Evaluators Recognize and Favor Their Own Generations* | 2404.13076 | C | 3 | 2 (XSUM, CNN/DailyMail) | 1,000 articles from each, 2,000 total | not stated | single rating | none new |
| 31 | Wu, *CollabLLM* | 2502.00640 | C + benchmark | 4 variants, 2 baselines | 3 datasets | MediumDocEdit 100, BigCodeBench 600, MATH-Chat 200 | 500 train conversations per set, 2,303 / 2,627 / 2,527 turns | at least 8 in the user study | 201 MTurk judges |
| 32 | Mozannar, *Reading Between the Lines* | 2210.14306 | C | n/a (studies deployed Copilot) | 1 coding session per participant | 21 participants, 21 sessions | 1,024 suggestions shown, 34.0 percent accepted (a second passage in the paper says 1,096; see limits) | not applicable; accept and reject events | 21 participants self-labelled their own sessions; 3,137 CUPS labels, mean 149.38 each |
| 33 | Wu, *AI Chains* | 2110.01691 | C | not determinable | 2 task types (Review, Flashcard), 1 per participant | 20 participants | 40 trials (20 x 2 interfaces) *derived* | not determinable | 20 participants as subjects; judgement total not stated |
| 34 | Sharma, *Generative Echo Chamber?* | 2402.05880 | C | n/a (search-system type is the manipulation) | 1 topic per participant; 3 conditions (Study 1), 2x3 (Study 2) | Study 1 N=115 of 124; Study 2 N=223 | n/a | open-ended search sessions | 2 researchers, blind to condition, coded 2,450 items (391 + 794 + 265 + 1,000) *derived*; Cohen kappa 0.91 on queries, 0.95 on sentences |
| 35 | Zeng, *LLMBar* | 2310.07641 | B | 5 evaluator backbones | 1 benchmark, 2 sets (Natural, Adversarial) | 419 curated pairs (Natural 100; Adversarial 319 = 134 + 92 + 47 + 46) | each pair queried twice per evaluator per strategy, 8 strategies | 2 queries per pair for order control | authors annotated; 80 instances double-assigned, 94 percent agreement (90 Natural, 95 Adversarial) |
| 36 | Yuan, *Self-Rewarding Language Models* | 2401.10020 | C | 1 base (Llama 2 70B) across 3 iterations | AlpacaEval 2.0 plus held-out set | IFT 3,200 seed; EFT 1,630 train / 541 eval; AlpacaEval 805 prompts; 256 head-to-head | AIFT(M1) 3,964 preference pairs, AIFT(M2) 6,942 *stated*; 4 candidates per prompt | 3 training iterations; judge sampled 3x and averaged | 3 annotators, all paper authors, on 50 instructions, so 150 judgements *derived* |
| 37 | Xu, *Pride and Prejudice: LLM Amplifies Self-Bias* | 2402.11436 | C | 6 | 3 task types, 3 dataset sources | 600 (translation 4 pairs x 100, CommonGen Hard 100, MATH 100) | not stated | up to 10 refinement iterations | 1 graduate student on 50 examples; 1,200 samples annotated in total *stated*; 6 hours |
| 38 | Krishna, *Effects of Iterative Prompting on Truthfulness* | 2402.06625 | C | 1 (GPT-3.5) | 1 (TruthfulQA) | 817 questions across 38 categories; multiple-choice subset size not separately stated | not stated | 10 iterations | none |

**This paper, Study 3, for comparison.** 6 models, 40 scenarios in 5 domains, 3 runs per cell,
720 conversations, 5 turns, 3,600 scored outputs; 2,880 post-Turn-1 responses classified; all
3,600 outputs re-scored after meta-commentary stripping; a 177-pair targeted-feedback contrast;
50 blind pairwise comparisons by 2 annotators; 64 items rated by 3 raters; 6 candidate judges
compared. Human judgements total 292 (2 x 50 plus 3 x 64).

---

## Distributions

### Controlled experiments

Model counts, restricted to the 18 studies that compare LLMs (the human-subject studies use one
simulated assistant or a deployed tool and are excluded from this quantity):

> 1, 1, 1, 1, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 15

Median 3. Mean 3.78. Range 1 to 15. Thirteen of the 18 evaluate 4 or fewer, and four evaluate a
single model.

Task or dataset counts, same 18 studies:

> 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 5, 6, 7

Median 2.5. Mean 2.83. Range 1 to 7. No controlled experiment in the set exceeds 7 task types.

Instances in the main experiment, for the 16 controlled studies where a count is determinable:

> 100, 100, 266, 300, 600, 700, 805, 817, 900, 1,060, 1,952, 2,000, 2,186, 2,640, 4,441, 200,000

Median 858.5. Dropping Laban as an outlier leaves a median of 817. Range 100 to 200,000, and the
distribution is heavily right-skewed by that single simulation study.

Scored outputs: only 3 of the 18 controlled LLM studies state or permit derivation of a total
(Laban at 200,000+ conversations, Self-Rewarding at 3,964 and 6,942 preference pairs, Stechly at
500 in one sub-experiment). The rest report a design and leave the product implicit. This is the
sparsest column in the table.

### Benchmark releases

Model counts across the 10 releases:

> 1, 2, 3, 5, 6, 11, 11, 20, 21, 50+

Median 8.5. Range 1 to more than 50.

Task or dataset counts across the 9 releases with a fixed task set:

> 1, 1, 2, 4, 4, 8, 8, 8, 13

Median 4. Range 1 to 13.

Scored outputs, stated or derivable, across 8 releases:

> 960; 10,000; 12,870; 17,051; 52,500; 88,368; 100,000; ~480,000

Median 34,776. Range 960 to roughly 480,000.

The two families behave in opposite directions, and the contrast is the reason they cannot share
a distribution. Benchmark releases run many models over a fixed task set: median 8.5 models.
Controlled experiments run few models with more conditions per model: median 3 models. A model
count that is unremarkable for a benchmark is near the top of the controlled range.

---

## Where this paper sits

**6 models.** Against the 18 controlled LLM experiments, 6 exceeds 16 of them and ties a
seventeenth; only Laban's 15 is larger. That is the 89th percentile, rank 2 of 19 once inserted,
against a median of 3 and a mean of 3.78. Against the 10 benchmark releases, 6 exceeds 4 of them,
the 40th percentile, against a median of 8.5. So: a lot for a controlled experiment, ordinary for
a benchmark. The comparison that fits the design is the first one.

The tie matters more than the rank. Xu's self-bias paper evaluates exactly six models on three
task types, was accepted to ACL 2024 Main, and states the count in its abstract without
qualification: "We analyze six LLMs (GPT-4, GPT-3.5, Gemini, LLaMA2, Mixtral and DeepSeek) on
translation, constrained text generation, and mathematical reasoning tasks." That is the register
available here, and it is a direct precedent at the same venue for the same model count.

**40 tasks in 5 domains.** Read as domains, 5 exceeds 15 of the 18 controlled experiments, the
83rd percentile, against a median of 2.5. Read as scenarios, 40 exceeds every controlled
experiment in the set and every benchmark release except MT-Bench-101's 13 task types, but this
reading compares scenarios against task types and is not a like-for-like measure. The defensible
statement is the first: 5 domains is above the controlled median of 2.5, and the 40 scenarios
inside them give 8 per domain where most studies in the set run one task type per domain.

**720 conversations.** Against the 16 controlled experiments with a determinable instance count,
720 exceeds 6, the 38th percentile, against a median of 858.5. Just below the median, and
comfortably inside the range: five studies in the set run 300 or fewer, including the two
most-cited negative results on self-correction (Stechly at 100, Valmeekam at 100) and Xu's
six-model self-bias study at 600.

**3,600 scored outputs.** Against benchmark releases, 3,600 exceeds 1 of 8, the 12th percentile,
against a median of 34,776. Against controlled experiments the distribution is too thin for a
percentile, because only three other controlled studies state a total at all. The more
informative observation is that stating the number is itself uncommon: 9 of 38 papers give a
total output count, and 6 of those 9 are benchmark releases.

**5 turns.** Among the multi-turn studies, MT-Eval runs a mean of 6.96 turns (range 3 to 12),
MT-Bench-101 a mean of 3.03, Zheng's MT-Bench exactly 2, Xu up to 4, MINT up to 5, CollabLLM at
least 8, and Laban a count equal to the shard count. Five turns sits mid-range.

**Replication within cell.** Three runs per cell is not the norm for open-ended generation work
in this set, though repeated sampling is standard in the code and reasoning papers: Laban runs
10 simulations per pair, RISE samples 16, Self-Debug samples 10, Stechly samples 5 and 15,
Self-Rewarding samples 4 candidates per prompt and averages its judge over 3 draws, and Reflexion
averages over 8 trials in one appendix. Among the evaluation and multi-turn benchmarks (MT-Eval,
MT-Bench-101, MINT, Zheng), no repeated-run design was found.

---

## How papers state their own scale

Verbatim abstract claims, benchmark releases first.

- Bai, MT-Bench-101: "we construct a three-tier hierarchical ability taxonomy comprising 4208
  turns across 1388 multi-turn dialogues in 13 distinct tasks" and "We then evaluate 21 popular
  LLMs based on MT-Bench-101, conducting comprehensive analyses from both ability and task
  perspectives."
- Kwan, MT-Eval: "we create single-turn versions of the 1170 multi-turn queries and compare
  performance. Our evaluation of 11 well-known LLMs shows..."
- Wang, MINT: "Our analysis of 20 open- and closed-source LLMs offers intriguing findings."
- Zheng, MT-Bench: "The MT-bench questions, 3K expert votes, and 30K conversations with human
  preferences are publicly available"
- Kim, Prometheus: "we first construct the Feedback Collection, a new dataset that consists of 1K
  fine-grained score rubrics, 20K instructions, and 100K responses and language feedback
  generated by GPT-4"
- Dubois, AlpacaFarm: "we train and evaluate eleven models on 10k pairs of real human feedback"
- Chiang, Chatbot Arena: "The platform has been operational for several months, amassing over
  240K votes."
- Lee, CoAuthor: "CoAuthor captures rich interactions between 63 writers and four instances of
  GPT-3 across 1445 writing sessions."

Controlled experiments.

- Laban: "Analysis of 200,000+ simulated conversations decomposes the performance degradation
  into two components: a minor loss in aptitude and a significant increase in unreliability."
- Madaan: "We evaluate Self-Refine across 7 diverse tasks, ranging from dialog response
  generation to mathematical reasoning, using state-of-the-art (GPT-3.5, ChatGPT, and GPT-4)
  LLMs."
- Sharma: "We first demonstrate that five state-of-the-art AI assistants consistently exhibit
  sycophancy across four varied free-form text-generation tasks."
- Bucinca: "We conducted an experiment (N=199), in which we compared our three cognitive forcing
  designs to two simple explainable AI approaches and to a no-AI baseline."
- Wu, CollabLLM: "Finally, we conduct a large user study with 201 judges, where CollabLLM
  increases user satisfaction by 17.6% and reduces user spent time by 10.4%."
- Tyen: "we show that this boosts downstream task performance across our 5 reasoning tasks"
- Mozannar: "Our study of 21 programmers, who completed coding tasks and retrospectively labeled
  their sessions with CUPS, showed that CUPS can help us understand how programmers interact with
  code-recommendation systems, revealing inefficiencies and time costs."
- Wu, AI Chains: "In a 20-person user study, we found that Chaining not only improved the quality
  of task outcomes, but also significantly enhanced system transparency, controllability, and
  sense of collaboration."
- Xu, self-bias: "We analyze six LLMs (GPT-4, GPT-3.5, Gemini, LLaMA2, Mixtral and DeepSeek) on
  translation, constrained text generation, and mathematical reasoning tasks."
- Zeng, LLMBar: "The authors manually curated 419 pairs of outputs, one adhering to instructions
  while the other diverging, yet may possess deceptive qualities that mislead an LLM evaluator,
  e.g., a more engaging tone."
- Yuan, Self-Rewarding: "Fine-tuning Llama 2 70B on three iterations of our approach yields a
  model that outperforms many existing systems on the AlpacaEval 2.0 leaderboard, including
  Claude 2, Gemini Pro, and GPT-4 0613."

**Abstracts that state no scale at all.** Huang, Stechly, G-Eval, Vasconcelos, Chiang and Lee,
Valmeekam (self-critique), PlanBench, Reflexion (performance figures only), Bansal (three
datasets, no N), Panickssery, Shankar, Sharma (echo chamber), Krishna, and both surveys. That is
roughly 16 of 38. Stating scale in the abstract is close to a coin flip in this literature, not
an expectation.

### Do small-N controlled studies apologise?

Almost never. Across 38 papers exactly one applies a diminutive to its own sample, and it is
attached to a human study rather than a model experiment. None of the four papers that run a
single model (Stechly, Valmeekam, Self-Rewarding, Krishna) qualifies that choice anywhere in its
text, and none of the papers with fewer than five annotators defends the panel size.

- Olausson, in the abstract: "a small-scale study in which we provide GPT-4 with feedback from
  human participants suggests that even for the strongest models, self-repair still lags far
  behind what can be achieved with human-level debugging." Sixteen participants and 80
  judgements. The qualifier does not soften the claim that follows it.

Four papers disclose a resource constraint flatly, with no apology and no defence:

- Huang: "For other models, to reduce the cost, we randomly sample 200 questions for each dataset
  (100 for HotpotQA) for testing."
- Qu, RISE: "Due to computational constraints, we were not able to perform more than two
  iterations of training with RISE, and no more than one iteration when the supervision comes
  from the learner itself."
- Valmeekam, self-critique, in the conclusion: "we plan to conduct more extensive experiments
  with respect to the number of instances, the number of domains and prompting methods."
- Wang, MINT, framing a reduction as a design choice rather than a shortfall: "we construct a
  subset of 586 challenging and representative instances."

One justifies its N formally:

- Vasconcelos, repeated across four of five studies: "Our sample size comes from a power analysis
  done on pilot data."

One bounds a secondary analysis by its N without conceding anything about its primary result,
which is the most precise handling of the question in the corpus:

- Mozannar: "Due to the limited number of participants, these results are not sufficient to
  determine the influence of programmer experience or Copilot experience on behavior." The
  sentence restricts the subgroup analysis only. The paper's main conclusions are stated at full
  strength on the same 21 participants.

The two most-cited negative results on self-correction are also the two smallest studies in the
corpus, and neither defends its size anywhere in the text. Stechly runs one model, one task and
100 instances, and states it in a single flat sentence: "For the following experiments, we
generated 100 instances with an average of 24 edges each spread across node counts from 10 to
17." Valmeekam runs one model, one domain and 100 instances: "We generate 100 random instances
for evaluation across various methods." Neither abstract mentions a number. The field's norm for
a controlled experiment is to state the design plainly and let the result argue for itself.

---

## Human annotation scale

Annotator headcounts across the 17 papers where a count was found:

> 1, 2, 2, 2, 3, 3, 5, 5, 5, 5, 9, 9, 16, 16, 20, 21, 58, 63, 199, 201, 731, 1,439, ~90,000

Median 16. Range 1 to roughly 90,000.

Human judgement totals, for the 15 papers where a total is stated or derivable:

> 80, 150, 160, 450, 900, 1,200, 2,100, 2,450, 3,000, 3,137, 3,600, 4,776, 10,000, 56,950, ~240,000

Median 2,450.

This paper contributes 2 annotators on 50 pairs and 3 raters on 64 items, so 292 judgements in
total. On headcount, 2 sits at the 9th percentile and 3 at the 22nd, against a median of 16.
Neither is the minimum: Xu's self-bias paper, at ACL 2024 Main, employs "one graduate student to
annotate 50 examples," which makes any agreement statistic impossible by construction. On
judgement volume, 292 exceeds 3 of 15, the 20th percentile, against a median of 2,450. Three
papers are smaller: Olausson at 80, Self-Rewarding at 150, LLMBar at 160.

Small annotator panels are therefore a standing practice in this literature rather than an
anomaly, and the comparison that matters is what those annotators cover and what is reported
about their agreement. Sharma's two coders handle 2,450 items at Cohen's kappa 0.91 and 0.95.
LLMBar's authors double-assign 80 instances and report 94 percent agreement. Self-Rewarding uses
three author-annotators on 50 instructions with majority voting. MINT's two annotators handle 113
trajectories. This paper's two annotators handle 50 pairs at kappa 0.703, and its three raters
handle 64 items with four agreement statistics reported. The headcount is ordinary for the
literature; the item count is low; the reliability reporting is above the norm.

Three of the corpus's human panels are the paper's own authors rather than recruited raters
(Madaan, LLMBar, Self-Rewarding). This paper's three raters are named individuals and one is an
author, which places it in the same practice.

The nearest comparators by design are small. MINT uses 2 annotators on 113 trajectories. Chiang
and Lee use 3 certified teachers across 700 items. MT-Eval uses 5 graduate students on 180
instances. Olausson uses 16 participants producing 80 judgements. Above that the counts jump to
crowd scale: 58 experts and 3,000 votes in Zheng, 16 screened annotators over 10,000 pairs in
AlpacaFarm, 201 judges in CollabLLM, 90,000 users in Chatbot Arena.

Where this paper is unusual is not volume but reliability reporting. Papers in the corpus that
report an inter-annotator statistic at all: Tyen (Krippendorff alpha, 0.979 to 0.998), MT-Eval
(Cohen kappa 0.58), Sharma's echo-chamber study (Cohen kappa 0.91 and 0.95), LLMBar (94 percent
raw agreement on 80 double-assigned instances), and AlpacaFarm (a 70 percent agreement screen
used to select annotators). That is 5 of the 23 papers with human annotation. This paper reports pairwise
quadratic-weighted Cohen's kappa (0.406 to 0.603), Krippendorff's alpha (0.529), binary
threshold agreement (76.6 to 82.8 percent), within-one-level agreement (81.2 to 95.3 percent),
and a separate kappa of 0.703 on the pairwise study. It also uses the human ratings to select
among 6 candidate judges rather than adopting GPT-4 by default, which no paper in the corpus was
found to do: MT-Eval, MT-Bench-101, Prometheus and G-Eval all adopt a GPT-4-family judge and
report correlation afterward.

The honest summary: the annotation is at the bottom of the corpus on volume and near the top on
how much is reported about its reliability and how it was used.

---

## Re-scoring and robustness passes: how common

The question is whether any paper re-scores all of its outputs a second time under an
alternative treatment. Across 38 papers, six do something in the neighbourhood, and the
distinctions between them matter.

- **Stechly (2310.12397)** re-scores the whole iterative-prompting set under an alternative
  decision rule: "We can relax our analysis of the LLM self-critique case by labeling an instance
  as correct if at any point during the backprompt chain, the LLM generated a correct coloring,"
  set against scoring only the final round. This is the closest analogue in the corpus, and it
  changes the rule applied to fixed outputs.
- **Zheng (2306.05685)** re-queries the same pairwise items with the two answers swapped: "A
  conservative approach is to call a judge twice by swapping the order of two answers and only
  declare a win when an answer is preferred in both orders." A second pass over the same items,
  for position bias.
- **Zeng, LLMBar (2310.07641)** does the same thing systematically: "For each output pair, we
  query the evaluator twice with swapped orders." Every pair, every evaluator, every strategy.
- **Yuan, Self-Rewarding (2401.10020)** scores each item three times and averages, which reduces
  judge variance under identical preprocessing rather than varying the treatment.
- **Chen, Self-Debug (2304.05128)** re-runs TransCoder and MBPP without unit-test execution as an
  ablation, which changes the feedback available rather than re-scoring fixed outputs.
- **Qu, RISE (2407.18219)** evaluates the same test sets under several inference protocols
  (with-oracle and without-oracle), which compares protocols rather than re-scoring generated
  content.

None of the 38 transforms the scored artifact itself and re-scores the whole set. That is what
this paper does: all 3,600 outputs are stripped of meta-commentary with validated patterns, the
1,200 that change (33.3 percent) are re-scored by the same judge at the same temperature with
the identical prompt, and the stripped scores become the primary estimates rather than a
robustness appendix. The distinction from Stechly, Zheng and LLMBar is real. Stechly varies the scoring rule; Zheng
and LLMBar vary the presentation order; Self-Rewarding varies nothing and averages. This varies
the text being scored, which is the thing the measurement was suspected of confounding. Within
the bound of this 38-paper survey, that pass appears to be without precedent here, and the effect
it isolates is large: the judge's preference for the first draft moves from 92 percent to 56
percent.

The nearest thing in the corpus to a paper worrying about the same confound is Panickssery, which
shows that evaluators favour their own generations, and Xu's self-bias paper, which shows
self-refinement amplifies that bias across six models. Both diagnose the problem. Neither
neutralises it by transforming the scored text and re-running the evaluation.

---

## What this paper can honestly claim about its own scale

Supported by the distributions above, and stated at the strength the numbers carry.

1. **Six models is at the top of the controlled range.** Above 16 of 18 controlled LLM
   experiments in this corpus, against a median of 3. Say "six models" and, if a comparison is
   wanted, that controlled studies in this literature typically run three. Do not claim it is
   large against benchmark releases, where the median is 8.5. Xu's ACL 2024 self-bias paper runs
   the same six and states it in one clause with no qualifier, which is the model to copy.
2. **Five domains is above the controlled median of 2.5;** 40 scenarios means 8 per domain rather
   than the single dataset per domain that is usual here. State the domain count as the task
   count and the scenario count as what sits inside it. Presenting 40 against other papers' task
   counts would compare scenarios to datasets.
3. **720 conversations is mid-range and just below the median of 858.5,** and there is no reason
   to dress it up. Two of the most-cited results in this exact debate run 100 instances each and
   state it in one sentence without defence. The convention this corpus supports is a flat
   statement of the design.
4. **The fully crossed design is worth stating where the raw N is not.** Six models by 40
   scenarios by 3 runs is a complete factorial with within-cell replication. Most controlled
   studies in the corpus do not cross all models against all tasks, and among the multi-turn
   evaluation benchmarks no repeated-run design was found.
5. **The re-scoring pass is the strongest scale-and-rigour claim available,** and it is a claim
   about design rather than size. No paper in this corpus re-scores its full output set after
   transforming the scored text. Stechly's relaxed-rule pass and Zheng's order-swap pass are the
   nearest precedents and are different operations. This can be stated positively and once.
6. **The judge selection is uncommon.** Six candidate evaluators compared against a human rater
   mean, with the winner chosen on correlation. The evaluation papers in this corpus adopt a
   GPT-4-family judge and report agreement afterward. Given that GPT-4o placed fifth of six here
   and Gemini 2.5 Flash was anti-correlated, the selection changed the instrument.
7. **Do not claim scale on human annotation.** Two annotators over 50 pairs and 3 over 64 items
   sits at the 9th and 22nd percentile on headcount and the 20th on volume. It is not the
   smallest in the corpus, and small panels are standard practice here, but it is not a strength
   to advertise. What can be claimed is the reliability reporting, which exceeds all but four
   papers in the set, and the fact that the pairwise study reports a success bar set in advance
   that was not cleared. Reporting a bar you did not clear is rarer than any sample size.
8. **Stating 3,600 scored outputs is itself above convention.** Only 9 of 38 papers state a total
   output count, and 6 of those 9 are benchmark releases. The number is small against benchmarks
   and unplaceable against controlled experiments, because controlled experiments here mostly do
   not report it.

---

## Limits of this survey

**Every intended paper was retrieved.** All 38 are read from a fetched document. The corpus is
still a convenience sample rather than a systematic review: it is the anchor papers this project
already engages plus the neighbours named around them, so it over-represents self-correction
critiques and multi-turn evaluation and under-represents reward modelling, agent benchmarks and
the non-English evaluation literature.

**Not every quantity exists for every paper.** Scored-output totals are missing for most of the
corpus because most papers do not state them; that absence is reported as a finding rather than
filled by multiplication where the crossing was not confirmed. G-Eval states no dataset sizes
anywhere in its body text, verified on two independent fetches. RISE's dataset sizes sit in an
appendix that could not be retrieved. Reflexion and Olausson do not restate HumanEval's size, and
Self-Debug does not restate Spider's development-set size; the well-known values were not
substituted from memory.

**Derived totals are not the papers' own claims.** Every cell marked *derived* is a product of
numbers the paper states separately, and in some cases the full crossing it assumes was not
confirmed in the text. Madaan's 4,441 is a sum across tasks that may not all have been run on all
three models. MT-Bench-101's 88,368 assumes every model was run on every turn.

**Four internal inconsistencies were left unresolved rather than adjudicated.** Laban states "more
than 200,000 simulated conversations," while the stated components (15 models, 600 instructions,
3 simulation types, 10 runs) multiply to 270,000; the stated figure is used above. MINT says "4
closed- and 16 open-source LLMs" but names five closed-source models. Mozannar reports 1,024
suggestions in one passage and 1,096 in another. Prometheus reports its human win rate as 58.67
percent in one place and 58.62 percent in another. In each case the paper's own primary statement
is what appears in the table.

**Three cells rest on a single reading.** AI Chains' model identity could not be confirmed: one
retrieval named LaMDA at 137 billion parameters, another found nothing, so the cell reads not
determinable. Shankar's aggregate human-grade total was not located despite repeated fetches, and
the paper itself describes grading behaviour without totalling it ("some stopped after 10
grades"). Xu's total generation count admits two conflicting derivations (23,424 and 13,500) from
numbers the paper states separately, so neither is recorded.

**Percentiles rest on small denominators.** The controlled-experiment distributions have 16 to 18
members and the benchmark distributions have 9 or 10. The human-subject studies without a model
comparison (Bansal, Bucinca, Vasconcelos, Mozannar, AI Chains, Sharma's echo chamber) enter the
human-annotation distributions and the verbatim catalogue but not the model, task or instance
counts. A percentile computed on 18 observations moves by roughly 5 points with one addition, so
the ranks above should be read as positions in a named set rather than as estimates of a
population quantile.

**The distributions moved once already.** An earlier pass of this document, built on 31 papers,
put 6 models at the 93rd percentile and the controlled instance median at 1,060. Adding seven
papers moved those to the 89th percentile and 858.5, and turned "2 annotators is the corpus
minimum" into "one paper uses a single annotator." The direction of movement was not uniform, so
do not assume a larger corpus would keep pushing the same way.

**Type labels are judgements.** The benchmark-versus-controlled split is assigned from what each
paper does, and four papers sit on the boundary: Tyen and CollabLLM release an artifact while
running a controlled comparison, Laban runs a controlled design at simulation scale, and Zheng
releases two artifacts of very different kinds in one paper. Each is marked with both labels
where it matters.
