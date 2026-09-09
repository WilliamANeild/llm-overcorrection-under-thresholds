# Rules: Abstract

Retrieved 2026-09-02. 48 abstracts. Every rule names its supporting papers.

The corpus is the eight abstracts already held in `paper/reference/neighbor_abstracts.md`
plus 40 fetched for this file from arXiv abstract pages on 2026-09-02, appended verbatim
to the same file under "Extended neighbor corpus (additions)". Areas covered: LLM
self-correction and self-refinement, multi-turn conversation and underspecification,
sycophancy, LLM-as-judge and evaluation, and human-AI interaction studies of LLM use.

All counts below were computed by script over the 48 stored abstract texts, not read off
by eye. Word counts are whitespace tokens of the abstract body. Sentence splitting
protects decimals and the abbreviations "e.g.", "i.e.", "et al.", "vs.", "cf.". The
result/scale classification of each numeral is a hand coding, and its rule is stated in
the number-discipline section so it can be checked.

---

## Corpus

Result stats = numerals reporting an empirical outcome (accuracy, prevalence, gain,
correlation, test statistic, interval). Scale stats = numerals reporting how big the
study is (models, tasks, datasets, participants, items, turns). Model version numbers
(GPT-4, Gemini 1.5, Vicuna-13B), citation years, and list enumerators (1)(2)(3) are
counted as neither. Close type: **K** = attributed knowledge claim, **R** = resource or
code release, **F** = future-work gesture, **C** = restatement of the contribution,
**I** = imperative addressed to the reader.

| # | Paper | ID | Words | Sents | Result | Scale | Close |
|---|---|---|---:|---:|---:|---:|:-:|
| 1 | Huang et al., LLMs Cannot Self-Correct Reasoning Yet | arXiv:2310.01798 | 142 | 7 | 0 | 0 | F |
| 2 | Kamoi et al., When Can LLMs Actually Correct Their Own Mistakes? | arXiv:2406.01297 | 174 | 7 | 0 | 0 | K |
| 3 | Laban et al., LLMs Get Lost In Multi-Turn Conversation | arXiv:2505.06120 | 186 | 8 | 1 | 2 | K |
| 4 | Madaan et al., Self-Refine | arXiv:2303.17651 | 173 | 7 | 1 | 1 | K |
| 5 | Sharma et al., Towards Understanding Sycophancy | arXiv:2310.13548 | 164 | 9 | 0 | 2 | K |
| 6 | Stechly et al., GPT-4 Doesn't Know It's Wrong | arXiv:2310.12397 | 255 | 9 | 0 | 0 | K |
| 7 | Tyen et al., LLMs cannot find reasoning errors | arXiv:2311.08516 | 202 | 8 | 0 | 1 | R |
| 8 | Pan et al., Automatically Correcting LLMs | arXiv:2308.03188 | 140 | 7 | 0 | 0 | F |
| 9 | Hu et al., Uncertainty of Thoughts | arXiv:2402.03271 | 196 | 6 | 1 | 0 | R |
| 10 | Shinn et al., Reflexion | arXiv:2303.11366 | 178 | 7 | 2 | 0 | C |
| 11 | Chen et al., Teaching LLMs to Self-Debug | arXiv:2304.05128 | 220 | 8 | 4 | 0 | K |
| 12 | Gou et al., CRITIC | arXiv:2305.11738 | 166 | 7 | 0 | 0 | K |
| 13 | Kumar et al., SCoRe | arXiv:2409.12917 | 254 | 8 | 2 | 0 | K |
| 14 | Valmeekam et al., Self-critiquing Their Own Plans? | arXiv:2310.08118 | 172 | 7 | 0 | 0 | K |
| 15 | Olausson et al., Is Self-Repair a Silver Bullet? | arXiv:2306.09896 | 191 | 7 | 0 | 0 | K |
| 16 | Xu et al., Pride and Prejudice (self-bias) | arXiv:2402.11436 | 153 | 8 | 0 | 1 | R |
| 17 | Jiang et al., SELF-[IN]CORRECT | arXiv:2404.04298 | 108 | 6 | 0 | 0 | K |
| 18 | Zheng et al., Judging LLM-as-a-Judge | arXiv:2306.05685 | 184 | 8 | 1 | 3 | R |
| 19 | Panickssery et al., LLM Evaluators Favor Own Generations | arXiv:2404.13076 | 165 | 8 | 0 | 0 | C |
| 20 | Wang et al., LLMs are not Fair Evaluators | arXiv:2305.17926 | 213 | 6 | 1 | 0 | R |
| 21 | Wei et al., Simple synthetic data reduces sycophancy | arXiv:2308.03958 | 195 | 7 | 0 | 1 | R |
| 22 | Perez et al., Model-Written Evaluations | arXiv:2212.09251 | 197 | 10 | 1 | 1 | K |
| 23 | Lee et al., Evaluating Human-Language Model Interaction | arXiv:2212.09746 | 170 | 7 | 0 | 2 | K |
| 24 | Kwan et al., MT-Eval | arXiv:2401.16745 | 185 | 10 | 0 | 2 | R |
| 25 | Bai et al., MT-Bench-101 | arXiv:2402.14762 | 174 | 9 | 0 | 4 | R |
| 26 | Zhang and Choi, Clarify When Necessary | arXiv:2311.09469 | 190 | 9 | 1 | 1 | C |
| 27 | Herlihy et al., Miscalibrated Conversational Priors | arXiv:2406.01633 | 178 | 8 | 0 | 0 | K |
| 28 | Fanous et al., SycEval | arXiv:2502.08177 | 182 | 8 | 20 | 0 | K |
| 29 | Liu et al., G-Eval | arXiv:2303.16634 | 184 | 9 | 1 | 1 | R |
| 30 | Li et al., Confidence Matters | arXiv:2402.12563 | 180 | 9 | 0 | 0 | R |
| 31 | Zeng et al., LLMBar | arXiv:2310.07641 | 181 | 7 | 0 | 1 | F |
| 32 | Thakur et al., Judging the Judges | arXiv:2406.12624 | 245 | 9 | 1 | 2 | K |
| 33 | Wu et al., CollabLLM | arXiv:2502.00640 | 163 | 8 | 4 | 2 | K |
| 34 | Welleck et al., Generating Sequences by Learning to Self-Correct | arXiv:2211.00053 | 155 | 6 | 0 | 1 | K |
| 35 | Zhang et al., Small LMs Need Strong Verifiers | arXiv:2404.17140 | 148 | 6 | 0 | 2 | K |
| 36 | Zhang et al., Self-Contrast | arXiv:2401.02009 | 167 | 10 | 0 | 0 | K |
| 37 | Shankar et al., Who Validates the Validators? | arXiv:2404.12272 | 219 | 9 | 0 | 0 | C |
| 38 | Perry et al., Do Users Write More Insecure Code? | arXiv:2211.03622 | 151 | 5 | 0 | 0 | R |
| 39 | Peng et al., Impact of AI on Developer Productivity | arXiv:2302.06590 | 76 | 5 | 1 | 0 | K |
| 40 | Dhuliawala et al., Chain-of-Verification | arXiv:2309.11495 | 106 | 4 | 0 | 0 | K |
| 41 | Javaji et al., Another Turn, Better Output? | arXiv:2509.06770 | 226 | 8 | 0 | 1 | C |
| 42 | Choi et al., In-Place Feedback | arXiv:2510.00777 | 137 | 5 | 0 | 1 | K |
| 43 | Ning et al., Revision or Re-Solving? | arXiv:2604.01029 | 201 | 8 | 0 | 2 | K |
| 44 | Liang et al., Useful feedback on research papers? | arXiv:2310.01783 | 278 | 14 | 6 | 5 | K |
| 45 | Chakrabarty et al., Creativity Support | arXiv:2309.12570 | 146 | 6 | 0 | 1 | F |
| 46 | Wang et al., Task Supportive and Personalized Interaction | arXiv:2402.06170 | 142 | 8 | 0 | 0 | C |
| 47 | Da Silva et al., Process-Oriented Evaluation of AI-Assisted Writing | arXiv:2606.15583 | 171 | 10 | 0 | 2 | K |
| 48 | Borchers et al., Teacher Revisions of LLM Feedback | arXiv:2603.27806 | 221 | 9 | 5 | 2 | K |

Totals: 8,604 words; 371 sentences; 53 result statistics; 44 scale statistics.
Close types: K 27, R 11, C 6, F 4, **I 0**.

---

## The move structure (with counts)

Seven moves recur. Only four of them are close to obligatory.

**Move 1. Context opener, third person, no numbers, no first person.** Present in all 48.
44 of 48 open with a declarative about the state of the world or a definition of the
object of study; 3 open directly with the authors as subject (Wang 2305.17926 "In this
paper, we uncover"; Herlihy 2406.01633 "We explore"; Perry 2211.03622 "We conduct"); 1
opens with a question (Jiang 2404.04298 "Can LLMs consistently improve their previous
outputs for better results?"). **0 of 48 put a
statistic in the first sentence** (2 carry a numeral, and in both it is a citation year or
a model name: Tyen 2311.08516 "Chen et al., 2023b"; Wang 2305.17926 "GPT-4"). 44 of 48
have no first-person pronoun in it.

Two sub-forms of the declarative opener, and both are live:
- Status-quo or adoption statement, 31 of 48. Huang 2310.01798, Chen 2304.05128 ("LLMs
  have achieved impressive performance on code generation"), Kwan 2401.16745, Borchers
  2603.27806.
- Copular or definitional statement of the object itself, 13 of 48. Kamoi 2406.01297
  ("Self-correction is an approach to..."), Laban 2505.06120 ("LLMs are conversational
  interfaces"), Wei 2308.03958 ("Sycophancy is an undesirable behavior where..."),
  Da Silva 2606.15583 ("Bad writing hinders the publication of science").

**Move 2. Prior work or the state of the literature.** Usually sentence 2, sometimes fused
into sentence 1. Xu 2402.11436 opens on it outright ("Recent studies show that LLMs
improve their performance through self-feedback on certain tasks while degrade on
others"). Tyen 2311.08516 fuses prior work and the gap into a single first sentence with
three inline citations.

**Move 3. The gap pivot.** Present with an explicit contrastive marker in 30 of 48;
absent in 18. Median markers per abstract 1, mean 1.06; distribution 0 in 18 abstracts,
1 in 15, 2 in 10, 3 in 4, 4 in 1. Where a pivot exists it comes early: in 24 of those 30
the first pivot is in sentence 1 or 2. The 18 without an explicit pivot are mostly
method-contribution papers (Madaan 2303.17651, Welleck 2211.00053, Zhang and Choi
2311.09469, Wu 2502.00640) rather than empirical-finding papers; of the 14 abstracts whose
headline is an empirical finding about model behaviour, 11 carry a pivot.

Connectives, by frequency: "However" 17 uses in 15 abstracts; a comma-bound
"yet/but/while/whereas" clause 21 uses in 13 abstracts; sentence-initial
"Although/While/Whereas/Despite" 5 in 5; sentence-initial "But" 3 in 2; sentence-initial
"Yet" 1 in 1; "Nevertheless" 1 in 1. Bare gap phrases without a connective: "To address
this gap/issue" 6, "remains unexamined/unclear/challenging" 4, "overlooking" 4,
"predominantly/primarily focus" 3, "no consensus" 1 (Kamoi 2406.01297), "little is known"
1 (Borchers 2603.27806), "has not been systematically studied" 1 (Liang 2310.01783).

**Move 4. Method and design.** 43 of 48 carry a first-person method marker, and it lands
at a fixed depth: **median sentence 3**, mean 3.02 (sentence 3 in 16 abstracts, 2 in 11,
4 in 10, 1 in 3, 5 in 2, 7 in 1). The fixed-phrase claim from the eight does not survive
the wider sample: "In this work/paper/study" appears in only 15 of 48. The commoner form
is a bare first-person verb: "we present/introduce/propose/develop" in 23 of 48,
"we study/investigate/examine/analyze/evaluate/conduct/perform/explore/test" in 25 of 48.

**Move 5. Findings.** 2 to 4 sentences. Marked by first-person observation verbs in
sentence-initial position or by an evidence noun as subject (see Register).

**Move 6. Closing knowledge claim.** 27 of 48 close on one. In 20 of those 27 the
grammatical subject is the evidence, not the authors: "Overall, our results indicate
that sycophancy is a general behavior" (Sharma 2310.13548), "Our results thus call into
question claims about the self-critiquing capabilities" (Stechly 2310.12397), "These
results suggest that editing errors directly is a more effective paradigm" (Choi
2510.00777), "Ultimately, our findings demonstrate that the utility of multi-LLM revision
is dynamically bottlenecked by task structure and draft quality" (Ning 2604.01029). In 7
the authors are the subject ("we discover", Laban 2505.06120; "We show", Welleck
2211.00053).

**Move 7. Resource release, optional and always last.** 11 of 48 end on a release
sentence; in 7 of those the sentence is a bare "this https URL" line. The knowledge claim
is not omitted in those abstracts, it is moved one sentence earlier. Treat the release
line as outside the argument.

---

## Length and proportion rules

Across 48: **median 178 words, median 8 sentences, 23.2 words per sentence.** Mean 179.2
words, mean 7.7 sentences. Range 76 (Peng 2302.06590) to 278 (Liang 2310.01783).

Distribution of word counts in 25-word buckets: 75-99: 1; 100-124: 2; 125-149: 6;
150-174: 14; 175-199: 14; 200-224: 6; 225-249: 2; 250-274: 2; 275-299: 1. **28 of 48
(58%) fall between 150 and 200 words.** 41 of 48 fall between 137 and 226. Only 3 of 48
exceed 245 words: Stechly 2310.12397 (255), Kumar 2409.12917 (254), Liang 2310.01783
(278). Of those three, two are long because they enumerate a taxonomy or three separate
studies.

Sentence counts: 4 to 14, median 8. **39 of 48 fall in the 6-to-9 band and 33 in the
7-to-9 band.**

Words per sentence, by abstract: median 24.3, range 15.2 (Peng 2302.06590) to 35.5 (Wang
2305.17926). An average above 30 words occurs in 4 of 48 (Hu 2402.03271, Kumar 2409.12917,
Wang 2305.17926, Perry 2211.03622), each of them method-heavy or enumerative.

Proportion, from the position of the first method marker: the setup (context, prior work
and pivot) occupies the first sentence only in 11 abstracts, the first 2 sentences in 16,
and the first 3 in 10. The method therefore arrives around a third of the way in, and the
second half of the abstract is findings plus close.

---

## Number discipline

This is where the corpus is most disciplined and where a draft is most likely to break
register.

### How many statistics an abstract carries

**31 of 48 abstracts (65%) report no result statistic at all.** Their findings are stated
in words: "self-critiquing appears to diminish plan generation performance" (Valmeekam
2310.08118), "models are not reliably better at discriminating among previously-generated
alternatives" (Jiang 2404.04298), "participants who had access to an AI assistant wrote
significantly less secure code" (Perry 2211.03622), "significant performance degradation
in multi-turn settings" (Kwan 2401.16745). The eight-abstract finding that most carry no
result statistic holds at 48, at a slightly lower rate (65% vs 75%).

Of the 17 that do carry one, **10 carry exactly one** and 12 carry two or fewer. Median
result statistics per abstract across the whole corpus is **0**; mean 1.10, which falls to
0.70 once the single outlier is removed. That outlier is Fanous 2502.08177 (SycEval) with
20, the only abstract in 48 that reads as a results table: it carries four p-values, three
Z-statistics and a confidence interval. Nothing else in the corpus comes close; the next
highest is Liang 2310.01783 with 6.

Scale statistics are commoner than result statistics but still sparse: 44 across 48
abstracts, median 0, and **23 of 48 state no scale numerically at all.** Where a scale
figure does appear, 25 of 48 carry at least one and 18 of those carry one or two.

### The form a result statistic takes

Of the 53 result statistics in the corpus, percentages account for the large majority:
a regex sweep finds 26 percentage figures carrying a decimal place across 6 abstracts
(38.1%, 15.6%, 9.1%, 58.19%, 18.5%, 55.8%, 30.85%, 57.4%) and 14 whole-number percentage
figures across 9 abstracts (39%, 91%, 80%, 9%, 12%). The remainder:
- Correlation or AUC values, 2 (Liu 2303.16634 "Spearman correlation of 0.514"; Borchers
  2603.27806 "AUC=0.75").
- p-values, Z-statistics and a confidence interval, 8, all in Fanous 2502.08177.
- Multipliers, 2 (Chen 2304.05128 "more than 10x candidate programs"; Zhang and Choi
  2311.09469 "double the performance gains").
- A raw ratio, 1 (Wang 2305.17926 "beat ChatGPT on 66 over 80 tested queries").
- A range, 2 (Chen 2304.05128 "2-3%"; Perez 2212.09251 "90-100%").
- Rating-scale points, 1 (Thakur 2406.12624 "may still differ with up to 5 points from
  human-assigned scores").

Approximation markers are rare: "~", "roughly", "about", "approximately", "nearly" or
"around" attach to a numeral 4 times in 2 abstracts (Madaan 2303.17651 "~20% absolute on
average"; Borchers 2603.27806 "about 80%", "about 50%", "about 10%"). Both keep the exact
figure and add the hedge in front of it; neither replaces the figure with a word.

### Spelled fractions: the one rule with no exceptions

**0 of 48 abstracts express a result as a spelled fraction of the form "two in five",
"one in eight", "seven in ten", or any other N-in-M construction.** The construction does
not occur once in 8,604 words. The eight-abstract finding is confirmed at six times the
sample.

Fraction words appear at all only twice, and in both cases the exact figure is supplied in
the same clause:

- Liang 2310.01783: "more than half (57.4%) of the users found GPT-4 generated feedback
  helpful/very helpful".
- Borchers 2603.27806: "only about 10% edit more than two-thirds of feedback instances",
  where "two-thirds" is a threshold defining what is being counted, not the count itself.

The rule the corpus follows is not "avoid fractions." It is that **a fraction word may
gloss a figure but may never stand in for it.**

### Rating scales, standard deviations, and units

- **0 of 48 report an effect in standard deviations.**
- **0 of 48 name a rating scale in the abstract** ("five-point scale", "Likert" appear
  zero times).
- **1 of 48 reports an effect in raw rating-scale units**: Thakur 2406.12624, "up to 5
  points from human-assigned scores", and it is a gap between two scores rather than a
  causal movement.

An effect stated as "0.74 levels" therefore has one near-precedent in 48 and no
established convention behind it. The corpus's normal move is to convert to a percentage,
a rate, or a correlation, or to state the direction in words.

### How scale is stated

No abstract in 48 states a crossed design as a product. **"Models × tasks" notation does
not occur; the multiplication sign appears 0 times; no abstract states a total trial
count.** The three forms actually used:

1. **Separate counts, spelled or numeric,** 14 of 48 give a task, dataset, benchmark or
   domain count and 6 give a model count in this form: "six LLMs" (Xu 2402.11436), "7 diverse tasks"
   (Madaan 2303.17651), "our 5 reasoning tasks" (Tyen 2311.08516), "thirteen judge models
   ... nine different examtaker models" (Thakur 2406.12624), "two models on five datasets"
   (Zhang 2404.17140), "five reasoning-intensive benchmarks" (Choi 2510.00777).
2. **A raw N of the corpus or the sample,** used where the N is the point: "200,000+
   simulated conversations" (Laban 2505.06120), "4208 turns across 1388 multi-turn
   dialogues in 13 distinct tasks" (Bai 2402.14762), "419 pairs of outputs" (Zeng
   2310.07641), "3,096 papers ... 1,709 papers ... 308 researchers from 110 US
   institutions" (Liang 2310.01783), "869 keystroke-level edit logs with 240k total edits"
   (Da Silva 2606.15583), "1,349 instances ... from 117 teachers" (Borchers 2603.27806),
   "n=30" (Chakrabarty 2309.12570), "201 judges" (Wu 2502.00640).
3. **Qualitatively, with no number,** in 20 of 48: "several open-source and industrial
   LLMs" (Jiang 2404.04298), "state-of-the-art LLMs" (Tyen 2311.08516), "a series of
   reasoning and translation tasks with different LLMs" (Zhang 2401.02009).

Numbers spelled as words are normal for small counts (a spelled cardinal appears in 21
of 48 abstracts, most often as a model, task or dataset count) and normal for design
parameters
("five-turn", "12-turn" in Javaji 2509.06770). This is the one place spelling out a number
is in register, and it is scale, never result.

---

## Register: verbs, hedges, subjects

**Observation verbs outnumber assertion verbs roughly two to one in first-person results
sentences.** Observation: "we find" 15 uses in 14 abstracts, "we observe" 6 in 6, "we
discover" 5 in 4, "we/experiments confirm" 1 in 1 — 27 uses. Assertion: "we show" 10 uses
in 8 abstracts, "we demonstrate" 1 in 1 — 11 uses.

**"Prove" appears 0 times in 48 abstracts**, in any inflection. This is absolute in the
corpus.

Where the subject is the evidence rather than the authors, the verb set is: "our results
indicate / reveal / show / suggest / demonstrate / call into question / cast doubt on",
"our findings show / demonstrate / reveal", "these findings emphasize / characterize",
"this finding challenges", "our research highlights / rediscovers" — 17 uses in 14
abstracts. In closing sentences specifically the evidence-as-subject construction wins 20
to 7.

Method verbs are uniformly plain: "we present/introduce/propose/develop" 25 uses in 23
abstracts.

**Hedging is one hedge per claim, not three.** Frequencies across 8,604 words: "often" 14
uses in 11 abstracts, "may" 10 in 6, "can be" 10 in 8, "largely/generally" 6 in 5,
"suggest(s)" 5 in 5, "appears/seems" 5 in 4, "likely" 4 in 3, "tends to" 2 in 2, "might"
1 in 1. Negative findings are the place hedges cluster: Stechly 2310.12397 "The study
seems to indicate that...", Valmeekam 2310.08118 "self-critiquing appears to diminish",
Olausson 2306.09896 "suggests that ... self-repair still lags far behind", Thakur
2406.12624 "suggest that caution may be wise". Positive findings are stated flat.

Boosters are present but confined to the setup: "state-of-the-art" 11 uses in 9 abstracts,
"significantly" 10 in 8 (almost always in its statistical sense),
"remarkable/impressive" 4 in 4, all four in a first or second sentence describing
the field rather than the paper's own result.

Punctuation: **0 em dashes in 48 abstracts.** Where a parenthetical break is wanted the
corpus uses a double hyphen (6 uses in 4) or a spaced single hyphen (8 in 4) as arXiv's
plain-text rendering of a dash, a colon (19 in 14), a semicolon (19 in 11), or
parentheses (116 pairs in 42). Question marks: 2, in 2 abstracts.

First person is universal: "we"/"our" appears 207 times across 46 of 48 abstracts. The
two without it are Fanous 2502.08177, which is written throughout in the passive
("Sycophantic behavior was observed in 58.19% of cases"), and Peng 2302.06590, the
shortest abstract in the corpus.

### How negative results and null findings are stated

30 sentences across 20 of 48 abstracts state a negative, null or degradation finding. Four
patterns, all of which name the mechanism rather than the disappointment:

1. **Direction plus condition.** "LLMs struggle to self-correct their responses without
   external feedback, and at times, their performance even degrades after self-correction"
   (Huang 2310.01798). "vague feedback often plateaus or reverses correctness, while
   targeted prompts reliably shift the intended quality axis" (Javaji 2509.06770).
2. **A claim about the prior claim.** "Our results thus call into question claims about
   the self-critiquing capabilities of state of the art LLMs" (Stechly 2310.12397). "This
   finding challenges the notion that LLMs may be able to enhance their performance only
   through their own judgment" (Jiang 2404.04298). "Collectively, our results cast doubt
   on the effectiveness of LLMs in a self-critiquing, iterative framework" (Valmeekam
   2310.08118).
3. **The null stated as a bounded comparison.** "models are not reliably better at
   discriminating among previously-generated alternatives than generating initial
   responses" (Jiang 2404.04298). "we find that better non-interactive performance does
   not always translate to better human-LM interaction" (Lee 2212.09746). "which is not
   correlated with the models' fundamental capabilities" (Kwan 2401.16745).
4. **A positive finding carrying the negative inside it.** "Both humans and LMs often
   target the weakest sections of abstracts, but fail to improve stronger areas" (Da Silva
   2606.15583). "Language Models improve edit outcomes through a mix of local and global
   features, but still actively struggle with global coherence" (Da Silva 2606.15583).

None of the 20 apologizes, and none previews an objection in order to answer it. Two
report a limitation flatly in the closing sentence: "though limitations are identified
when using a weak self-verifier" (Zhang 2404.17140) and "While our findings show that
LLM-generated feedback can help researchers, we also identify several limitations" (Liang
2310.01783).

---

## Rules

**R1. 150 to 200 words, 7 to 9 sentences.** Evidence: 28 of 48 fall in 150-200 words; 33
of 48 fall in 7-9 sentences (39 in 6-9); medians are 178 and 8. Above 245 words, only 3 of 48, and all
three are enumerating a taxonomy or multiple studies. A 260-word abstract would be the
second longest of 49.

**R2. Average 22 to 26 words per sentence.** Corpus mean 23.2; per-abstract median 24.3.
Only 4 of 48 exceed 30.

**R3. Open with a third-person declarative. No statistic, no first person.** Evidence: 0
of 48 openers carry a statistic; 44 of 48 have no first-person pronoun; 44 of 48 are
declaratives about the world or the object of study. Both sub-forms are available:
adoption statement (31 of 48, e.g. Kwan 2401.16745) or definition (13 of 48, e.g. Wei
2308.03958).

**R4. Give prior work one sentence, and position against it rather than around it.**
Evidence: the move is sentence 2 or fused into sentence 1 in nearly every abstract; Tyen
2311.08516 compresses prior work, three citations and the gap into one sentence.

**R5. One gap pivot, in sentence 1 or 2, and one only.** Evidence: median 1 pivot marker
per abstract; among the 30 with a pivot, 24 place the first one in sentence 1 or 2. Use
"However" (15 of 48) or a comma-bound "yet"/"but" clause (13 of 48). Three or more pivot
markers occurs in 5 of 48 and reads as an abstract arguing with itself.

**R6. State the design in one sentence, in first person, at sentence 3.** Evidence: 43 of
48 carry a method marker, median position sentence 3. Do not reach for "In this work" as
the fixed phrase; it is used in only 15 of 48. "We study", "We propose", "We analyze" are
each commoner.

**R7. State scale as separate counts or a raw N, never as a product.** Evidence: 0 of 48
state a crossed design as a product; 0 use a multiplication sign; 14 give a task, dataset
or benchmark count and 6 a model count as separate figures; 8 give a raw corpus N where
the N is itself the point. Spelling small scale counts as words is standard (21 abstracts).

**R8. Carry no more than two result statistics.** Evidence: 31 of 48 carry none; of the 17
that carry any, 12 carry two or fewer; median across the corpus is 0. Four or more occurs
in 5 of 48, and the one abstract with 20 (Fanous 2502.08177) is the corpus's clear
outlier. Each statistic that survives should be the one a reader would quote.

**R9. Every result statistic is an exact figure.** Evidence: 40 of 53 are exact
percentages, 2 are correlation or AUC values. Where an approximator is used it precedes
the exact figure rather than replacing it (Madaan 2303.17651 "~20%"; Borchers 2603.27806
"about 80%").

**R10. Never express a result as a spelled fraction.** Evidence: 0 of 48 use any N-in-M
construction. The two abstracts using a fraction word supply the exact percentage in the
same clause (Liang 2310.01783 "more than half (57.4%)"). This is the strongest single
result in the file and the one most likely to be violated by a draft written for the ear.

**R11. Do not report an effect in raw rating-scale units without converting it.**
Evidence: 0 of 48 report an effect in standard deviations; 0 name a rating scale; 1
reports a gap in scale points (Thakur 2406.12624). A quantity in "levels" carries no
meaning to a reader who has not read the methods. Convert to a rate, a percentage, or a
proportion of the scale, or state the direction in words and leave the magnitude to the
results section.

**R12. Findings sentences take observation verbs.** Evidence: observation verbs (find,
observe, discover, confirm) 27 uses against assertion verbs (show, demonstrate) 11.
"Prove" appears 0 times in 48.

**R13. Close on an attributed knowledge claim with the evidence as grammatical subject.**
Evidence: 27 of 48 close on a knowledge claim, and 20 of those 27 make the evidence the
subject: "our results indicate", "these results suggest", "our findings demonstrate". The
release line, if any, goes after it (11 of 48).

**R14. Never close with an imperative addressed to the reader.** Evidence: **0 of 48.**
Close types are knowledge claim 27, resource release 11, contribution restatement 6,
future-work gesture 4, imperative 0. No sentence in 8,604 words begins with a bare
imperative verb. A closing line of the form "do X, or do not do Y" has no precedent in
this literature. The equivalent content goes in the knowledge-claim frame: not "tell the
model what is wrong", but "models revise effectively only when told what is wrong."

**R15. One hedge per claim, and put the hedges on the negative findings.** Evidence:
hedges are sparse overall (the commonest, "often", is 14 uses across 8,604 words) and
cluster on null and negative results (Stechly 2310.12397, Valmeekam 2310.08118, Olausson
2306.09896, Thakur 2406.12624). Positive findings are stated flat.

**R16. State a negative finding by naming the condition under which it holds.** Evidence:
all 30 negative-finding sentences do this; none apologizes, none raises an objection in
order to rebut it. Huang 2310.01798 and Javaji 2509.06770 are the models to follow.

**R17. No em dashes.** Evidence: 0 in 48. Use a colon (14 abstracts), a semicolon (11), or
parentheses (42).

**R18. Claim only what the design measured.** Evidence: 12 of 48 make a claim about human
behaviour, and every one of them names the study that produced it in the same abstract:
a user study (Chakrabarty 2309.12570, Perry 2211.03622, Shankar 2404.12272, Wang
2402.06170, Choi 2510.00777, Wu 2502.00640, Liang 2310.01783), a controlled experiment
(Peng 2302.06590), or an analysis of logs and edit traces (Herlihy 2406.01633, Da Silva
2606.15583, Borchers 2603.27806, Lee 2212.09746). Five of the twelve also give the N:
"308 researchers from 110 US institutions" (Liang 2310.01783), "an empirical user study
(n=30)" (Chakrabarty 2309.12570), "1,349 instances ... from 117 teachers" (Borchers
2603.27806), "a large user study with 201 judges" (Wu 2502.00640), "869 keystroke-level
edit logs" (Da Silva 2606.15583). Herlihy 2406.01633 is the closest analogue to a claim
about how people prompt, and it earns it: "We first analyze public LLM chat logs to
conclude that query under-specification is common." **No abstract in 48 asserts what users
do on the strength of a model-only experiment.**

---

## Constructions to avoid, with evidence

| Construction | Corpus evidence | Instead |
|---|---|---|
| Spelled fraction as a result ("two in five", "one in eight") | 0 of 48 | The exact percentage |
| "half again as much" for a ratio | 0 of 48 use a spelled multiplier for a computed ratio; the 2 multiplier uses are "10x" and "double" | State both quantities, or the ratio as a figure |
| Closing imperative to the reader | 0 of 48 | Knowledge claim with the evidence as subject (20 of 27 closers) |
| Effect in unexplained scale units ("0.74 levels") | 1 of 48 reports scale points, 0 name the scale | A rate, a percentage, or words |
| Crossed design as a product ("six models by 40 tasks", "720 trials") | 0 of 48; 0 multiplication signs | Separate counts, or the raw N |
| "prove" | 0 of 48 | find, observe, show |
| Em dash | 0 of 48 | colon, semicolon, parentheses, two sentences |
| Three or more contrastive pivots | 5 of 48; median 1 | One pivot in sentence 1 or 2 |
| Evaluative label on the paper's own finding before the evidence ("this wasteful phenomenon") | Evaluative labels do occur (Wei 2308.03958 "Sycophancy is an undesirable behavior"; Fanous 2502.08177 "poses risks to reliability"), but in both the label attaches to a phenomenon already named and established in the literature, not to the paper's own new result | Name the behaviour neutrally in the opener; let the finding carry the judgment |
| A claim about user behaviour with no user study | 12 of 48 make claims about people and all 12 name the study behind them | Confine the claim to what was run, or cite work that measured it |
| Standalone dramatic opener with no content | 0 of 48; every opener carries a proposition | A declarative that states something |
| Rhetorical question opener | 1 of 48 (Jiang 2404.04298) | Available, but it is a minority form |

---

## Checklist

Run in order. Each item is mechanically checkable against the corpus counts above.

1. Word count between 150 and 200. (Median 178; 28 of 48 in band.)
2. Sentence count between 7 and 9. (Median 8; 33 of 48 in the 7-9 band.)
3. Mean sentence length between 22 and 26 words. (Corpus mean 23.2.)
4. First sentence: third person, no statistic, no "we". (0 of 48 openers carry a statistic; 44 of 48 have no "we".)
5. A prior-work sentence exists and positions the paper against something named.
6. Exactly one gap pivot, in sentence 1 or 2. (Median 1.)
7. A design sentence in first person, at or near sentence 3. (Median position 3.)
8. Scale stated as separate counts or a raw N. No product, no multiplication sign. (0 of 48 use a product.)
9. Result statistics: two or fewer. (31 of 48 carry none.)
10. Every result statistic is an exact figure, not a spelled fraction. (0 of 48 spell one.)
11. No effect stated in bare scale units. (1 of 48.)
12. Findings verbs are observation verbs; "prove" absent. (0 of 48.)
13. Closing sentence is a knowledge claim with the evidence as grammatical subject. (20 of 27 closers.)
14. Closing sentence is not an imperative. (0 of 48.)
15. Zero em dashes. (0 of 48.)
16. Every claim maps to something the design measured. (Universal in the corpus.)
17. Hedges: one per claim, concentrated on negative findings.

---

## How this paper's current abstract measures up

Two drafts were assessed: `paper/abstract_versions/v11_liam_2026-09-02.md` (the author's
current draft) and `paper/sections/abstract_v2.tex` (the version in the build). Counts
below were computed by the same script used on the corpus.

### v11 (author draft): 260 words, 10 sentences, 26.0 words per sentence

| Check | Result |
|---|---|
| R1 length | **Fails.** 260 words would be the second longest of 49; only 3 of 48 exceed 245. |
| R2 sentence length | Passes at the edge. 26.0 against a corpus mean of 23.2. |
| R3 opener | **Passes cleanly.** "Large language models are increasingly handed work their users could not do themselves." Third person, no numeral, no first person; the adoption form used by 31 of 48. |
| R4 prior work | **Fails.** No prior-work sentence exists. Sentences 2-4 are a narrative about user psychology, not a positioning move. Every one of the 48 positions itself against something. |
| R5 gap pivot | **Fails.** No contrastive marker anywhere: no "however", no "yet", no "remains", no "prior work has". The 18 corpus abstracts without a pivot are method-contribution papers; this is an empirical-finding paper, and 11 of the 14 comparable ones carry a pivot. |
| R6 design sentence | Passes. "We put this wasteful phenomenon to the test, running five-turn revision conversations across six models" arrives at sentence 5, one later than the median 3. |
| R7 scale | Partial. "five-turn", "six models" are in register. The task count (40), the domain count (5) and the trial count are all absent, so the reader cannot size the study. |
| R8 count of result statistics | Passes on count: three (two in five, one in eight, half again). |
| R9 exact figures | **Fails.** None of the three is exact. |
| R10 spelled fractions | **Fails, and this is the sharpest break.** "roughly two in five responses at the second turn to one in eight by the fifth" and "recovering half again as much quality as undirected revision destroys" are three N-in-M or spelled-multiplier constructions. The construction occurs 0 times in 8,604 words of neighbor abstracts. The three also round away from the computed values: 39% becomes "two in five" (40%), 13% becomes "one in eight" (12.5%), and 1.16/0.74 = 1.568 becomes "half again" (1.5). |
| R11 scale units | Passes by avoidance: the draft states no quantity in levels. |
| R12 verbs | Passes. No "prove"; the results sentences use plain verbs. |
| R13 close: knowledge claim | **Fails.** |
| R14 close: no imperative | **Fails.** "The rule that falls out is plain: tell the model what is wrong, or do not ask it to revise." This is an instruction to the reader, a close type with 0 of 48 precedent. |
| R15 hedging | Passes. "roughly", "often", "mostly", "rarely" are single and placed. |
| R17 em dashes | Passes. Zero. |
| R18 claim only what was measured | **Fails.** Sentences 2-4 assert what users do: "users can neither find flaws nor suggest improvements, and resort to unguided, speculative requests for revision"; "users continue blindly into another round of unneeded revision". The described design is five-turn simulated conversations across six models. The paper's human data is two annotators validating an LLM judge on 50 balanced-panel pairs (`sections/methods.tex`), not a study of user behaviour. All 5 corpus abstracts that make claims about people state the sample that supports them. |
| Evaluative self-labelling | "this wasteful phenomenon" applies the verdict before the evidence. No analogue in 48. |
| Known open item | The file's own header flags that the "cosmetic edits" clause misdescribes the classifier, whose non-genuine class is meta-responses (declines and restatements), not small edits. Still present in sentence 7. |

What v11 does better than the corpus median: the opening sentence is the best in either
draft, and sentence 6 ("a model has two honest responses: attempt the improvement, or
declare the work finished and stand behind it") states the design's logic in a way no
neighbor abstract achieves. Both are worth keeping.

### abstract_v2 (in the build): 180 words, 8 sentences, 22.5 words per sentence

| Check | Result |
|---|---|
| R1, R2 length and rhythm | **Passes on all three at the corpus median.** 180 vs median 178; 8 vs median 8; 22.5 vs mean 23.2. |
| R3 opener | Passes. Adoption form, third person, no numeral. |
| R4 prior work | Passes. Sentence 2 is a clean prior-work move naming what has been examined and what it found. |
| R5 gap pivot | Passes. One pivot, "remains unexamined", sentence 3. The phrase itself has 4 of 48 precedent ("remains unclear/unexamined/challenging"). |
| R6 design sentence | Passes. "We study this setting directly, running five-turn revision conversations with six LLMs on 40 tasks across five domains" at sentence 4, one later than median. |
| R7 scale | Passes. Four separate counts, no product. This is exactly the corpus form. |
| R8 count of result statistics | **Fails.** Four (39%, 13%, 0.74, 1.16). Only 5 of 48 carry four or more, and 31 of 48 carry none. Combined with four scale statistics, eight numerals in 180 words is denser than all but two abstracts in the corpus. |
| R9 exact figures | Passes. All four are exact. |
| R10 spelled fractions | Passes. None. |
| R11 scale units | **Fails.** "reduce quality by 0.74 levels on a five-point scale" and "improving quality by 1.16 levels". 0 of 48 name a rating scale; 1 of 48 reports anything in scale points. |
| R12 verbs | Passes. "declines", "reduce", "reverses", "suggest". No "prove". |
| R13, R14 close | **Passes cleanly.** "These results suggest that intrinsic self-correction fails not from lack of capacity but from lack of direction: models revise effectively only when told what is wrong." Evidence as grammatical subject, hedged with "suggest", no imperative. This is the corpus's most common closing form and it is executed well. |
| R15 hedging | Passes. |
| R17 em dashes | Passes. Zero. |
| R18 claim only what was measured | Passes. Every claim maps to the described design. |

### Two substantive items that are not style

Both are for the author to decide; neither is a wording fix.

1. **The 0.74 figure and the human check point in different directions.** The abstract
   states "Revisions that do occur reduce quality by 0.74 levels". `sections/methods.tex`
   reports that the blind human pairwise comparison chose Turn 1 in 56.2% of non-tie
   decisions, 95% CI [45.2%, 67.1%], that the interval includes 50%, and that the
   pre-registered bar of 65% was not cleared. The methods section states this plainly:
   the degradation "is real but not large enough to reliably flip a blind pairwise
   preference once meta-commentary is removed." An abstract that reports the judge
   estimate without that qualification claims more than the paper establishes. The corpus
   convention for this situation is pattern 4 above: state the finding with the condition
   inside it, as Da Silva 2606.15583 and Javaji 2509.06770 do.

2. **The abstract's numbers are not the paper's headline numbers.** The stated headline is
   that among revisions that move quality 70% move it down, and that 75% of replies to a
   request for improvement contain no revision at all. Neither figure appears in either
   draft. abstract_v2 instead reports the 39%-to-13% genuine-revision decline and the two
   effect sizes. If the 70% and 75% figures are the paper's claim, the abstract is
   reporting a different pair of results from the ones the paper leads with, and under R8
   there is room for two figures, not four.

### What could not be checked

The move-by-move sentence allocation in the corpus was coded from the position of the
first method marker and from the pivot positions, not by hand-labelling all 371 sentences,
so the per-move sentence counts in "The move structure" are boundaries rather than exact
allocations. The result/scale classification of individual numerals is a hand coding and a
reader could reasonably move two or three borderline cases (Perez 2212.09251's "154
datasets", Zhang and Choi 2311.09469's "10% of examples"); no conclusion in this file
turns on those. Publication venue and acceptance status were not checked for any of the 40
new entries, so the corpus mixes accepted conference papers with preprints.
