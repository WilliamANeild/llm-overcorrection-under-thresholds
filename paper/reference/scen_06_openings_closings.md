# Opening and closing moves in abstracts at this venue

Compiled 2026-09-06. Purpose: give the full attested space of opening and closing moves,
with counts, for the abstract of a paper going to ARR in October 2026. That abstract
currently opens with a question, "Do language models know when a good answer should be
left alone?", and closes on an attributed knowledge claim, "These results indicate that
undirected revision lowers the quality of work that was already sufficient, and that
naming the fault reverses the effect." The question this file answers is which
opening-closing pairs the venue produces, and at what rate.

## Corpus

134 abstracts in five strata. 86 of them form the venue-norm corpus (strata A, A2, B, C);
the 48 topical neighbours (stratum D) are held separately because they were gathered by
topic and are not a probability sample of anything.

| Stratum | Source | n | Drawn how | Retrieved |
|---|---|---|---|---|
| A | ACL Anthology 2026 volumes, wave 1 | 47 | systematic, fixed random start and constant stride per volume, seed 20260906 | 2026-09-06 |
| A2 | ACL Anthology 2026 volumes, wave 2 | 20 | same scheme, seed 20260906007, collisions with wave 1 replaced by the next paper in volume order | 2026-09-06 |
| B | arXiv cs.CL monthly listings, 2025-01 to 2026-08 | 10 | ten month strata at stride 2 over the 20-month window; within each stratum the entry at position `frac x total`, where `frac` advances by 1/10 per stratum from a seeded start of 0.0241 | 2026-09-06 |
| C | prior topical set already held in `acl2026_abstracts.json` | 9 | gathered by topic, not sampled | 2026-09-02 |
| D | topical neighbour corpus in `neighbor_abstracts.md` | 48 | gathered by topic, not sampled | 2026-09-02 |

Strata A, A2 and B are new or extended for this file. Wave 2 drew 8 from `2026.acl-long`
(stride 277.8 over 2,222 papers), 6 from `2026.findings-acl` (stride 360.5 over 2,163),
4 from `2026.eacl-long` (stride 98.5 over 394), 2 from `2026.acl-short` (stride 37.0 over
74). All 20 landing pages returned an abstract; none failed.

The arXiv draw used the monthly listing pages at `arxiv.org/list/cs.CL/<YYYY-MM>`, taking
the total entry count from the page, computing the index, refetching the listing at that
offset and taking the first arXiv identifier there, then reading the abstract from the
paper's own abstract page. Month totals ranged from 1,361 (2025-01) to 2,844 (2026-05).
Three of the ten have a primary category other than cs.CL and are cross-listed into it:
2603.03203 (cs.AI), 2605.15040 (cs.AI), 2607.23597 (cs.CR). They are kept and flagged
rather than replaced, because dropping them would make the frame "papers whose primary
category is cs.CL" rather than "papers listed under cs.CL", which is not the frame the
index page defines.

**Access failures.** The arXiv Atom API at `export.arxiv.org/api/query` returned HTTP 429
on every request for an extended period, from urllib with a descriptive user agent and from
curl alike, so the listing-page route above was used instead and returned all ten. A
background retry against the API with longer backoff did eventually return 9 of the 10
strata, but only after this corpus had been assembled, and its 2025-01 stratum never
returned at all. **That API draw is not used in any count in this file.** It is stored for
audit under `arxiv_cs_cl_2026_09_06_api_unused` in `acl2026_abstracts.json` and flagged
there as unused, because a corpus assembled half from one frame and half from another is
not a sample of anything. The two frames disagree slightly on how many papers a month
contains (2025-03: 1,879 by API, 1,909 by listing), which is a second reason not to mix
them. Nothing else failed: 20 of 20 Anthology pages and 10 of 10 arXiv abstract pages
returned text. No abstract in this file was reconstructed, paraphrased or filled in from
memory.

**A concurrent second wave exists in the same store.** While this file was being built, a
parallel effort added its own 20-abstract second wave to `acl2026_abstracts.json` under
`sample2_2026_09_06`, drawn from the same four volumes with a different seed (20260907) for
`scen_04_length_density.md`. The wave used here is stored separately as
`sample_2026_09_06_wave2`. The two draws are independent and overlap on two papers,
`2026.acl-short.30` and `2026.acl-short.67`; the union of the original 47 and the two waves
is 85 distinct ACL abstracts. Every count in this file uses the 47 plus
`sample_2026_09_06_wave2`, not the other wave.

**Bounds on the sample.** The A and A2 draws are unconditional on topic, so they describe
what these volumes do and are dominated by method papers, which is what the volumes are
dominated by. The B draw is unconditional on topic within cs.CL. Strata C and D were
assembled by topic around self-correction, multi-turn interaction, evaluation and
human-AI interaction, so they over-represent empirical studies of model behaviour and
under-represent method papers. Where the two groups differ, both figures are given. No
stratum covers EMNLP or NAACL 2026: `2026.naacl-long`, `2026.emnlp-main` and
`2026.starsem-1` return HTTP 404 on the Anthology and were confirmed absent rather than
assumed so.

**How things were counted.** Sentence segmentation, word counts, digit-run counts,
question detection and the imperative scan are mechanical, by script, over the stored
abstract text. The opening and closing classifications are hand-coded, one code per
abstract, and every coded sentence is quoted verbatim below so the coding can be checked
against the text rather than taken on trust. Abstract text is quoted exactly as extracted,
including two artifacts of the source pages that are preserved rather than repaired:
`2026.eacl-long.226` reads "attempting tomeasure" and `2026.findings-acl.1394` reads
"bench- marks".

## The coding scheme

**Openings.** One code per abstract, applied to the first sentence.

- **Q** rhetorical question. The first sentence is interrogative and ends in a question mark.
- **DEF** flat copular or near-copular definition of the object of study. "Self-correction is an approach to improving responses from large language models." Also counted here: a sentence whose main assertion characterizes what the object is or requires, without a copula ("Empathetic dialogue requires not only recognizing a user's emotional state but also...", "Generative linguistic steganography conceals secret bits within the sampling randomness of large language models").
- **SQ** status-quo statement about the field: what models, methods or researchers have achieved or currently believe. "Large language models have demonstrated remarkable performance across a wide array of NLP tasks."
- **PROB** problem statement. The main assertion names a deficiency, difficulty or gap.
- **SCENE** scene-setting claim about deployment or use. "Large language models are increasingly deployed in culturally sensitive real-world tasks."
- **FIND** direct statement of the paper's own finding or move, with no preamble. Two varieties occur, and both are counted here: result-first ("In this paper, we uncover a systematic bias in the evaluation paradigm...") and artifact-first ("We present SemanticQA, an evaluation suite designed to...").
- **OTHER** anything else. Zero abstracts required it.

Many openings pair an assertion with a trailing concessive or gap clause ("LLMs excel at
complex reasoning tasks but often suffer from overthinking"). The rule applied throughout
is that the grammatical main assertion sets the code and the trailing clause does not. So
that example is SQ, not PROB. The rule is stated because it decides roughly a quarter of
the codes, and a reader applying the opposite rule would get a different table.

**Closings.** One code per abstract, applied to the last sentence, plus an optional
secondary tag where the sentence makes a clear second move.

- **KNOW_G** attributed knowledge claim, general. The claim is about models, methods or
  the world, and generalizes past the paper's own artifact. "Our findings reveal a gap
  between the reasoning LRMs follow and the reasoning they report."
- **KNOW_A** attributed knowledge claim, own artifact. The claim is attributed to the
  study in exactly the same grammar, but its content is that the authors' own system
  works. "Extensive experiments demonstrate that STRIDE-ED generalizes across diverse
  open-source LLMs and consistently outperforms existing methods."
- **CALL** call to the community.
- **FUTURE** future work.
- **RELEASE** resource or code release.
- **CONTRIB** contribution restatement: what the paper provides, built or did.
- **NAMED** named-phenomenon restatement: the close re-names the phenomenon the paper
  coined and says what kind of thing it is.
- **PRACTICE** implication for practice.
- **IMP** imperative to the reader.
- **OTHER** anything else. Zero abstracts required it.

KNOW_G and KNOW_A are two halves of the brief's single "attributed knowledge claim"
category. They are separated because the split turns out to be the main thing the
cross-tabulation shows, and both the split and the umbrella figure are reported.

## Distribution of openings

| Opening | All 134 | Venue corpus (A+A2+B+C), n=86 | ACL Anthology 2026 only, n=67 | arXiv cs.CL, n=10 | Topical neighbours, n=48 |
|---|---|---|---|---|---|
| SQ status quo | 48 (36%) | 26 (30%) | 22 (33%) | 3 | 22 (46%) |
| DEF definition of the object | 32 (24%) | 22 (26%) | 16 (24%) | 5 | 10 (21%) |
| PROB problem statement | 23 (17%) | 18 (21%) | 14 (21%) | 0 | 5 (10%) |
| SCENE deployment scene-setting | 19 (14%) | 12 (14%) | 10 (15%) | 1 | 7 (15%) |
| FIND finding or move, first | 9 (7%) | 6 (7%) | 5 (7%) | 1 | 3 (6%) |
| Q rhetorical question | 3 (2%) | 2 (2%) | **0** | 0 | 1 (2%) |
| OTHER | 0 | 0 | 0 | 0 | 0 |

Nine in ten abstracts open on the field rather than on the paper: status quo, definition,
problem or deployment scene account for 122 of 134. Opening with the paper's
own move is a minority behaviour at 9 of 134, and opening with a question is rarer still.

**The question opening does not appear once in 67 systematically drawn ACL Anthology 2026
abstracts.** All three question openings in the corpus come from the two topically
gathered strata, where they are 3 of 57. This is the single most consequential number in
the file, and it needs its bound stated plainly: 0 of 67 does not mean the venue rejects
the construction. With a true rate of 2 percent, the chance of drawing zero in 67 is about
26 percent, so the systematic sample is consistent with the construction being rare rather
than absent. What the sample does establish is an upper bound. The 95 percent upper
confidence limit on the rate, given 0 of 67, is 4.4 percent, so a question opening is at
most a one-in-twenty behaviour in these volumes and more likely a one-in-fifty one.

## Distribution of closings

| Closing | All 134 | Venue corpus, n=86 | ACL Anthology 2026 only, n=67 | arXiv cs.CL, n=10 | Topical neighbours, n=48 |
|---|---|---|---|---|---|
| KNOW_A attributed claim, own artifact | 41 (31%) | 33 (38%) | 29 (43%) | 2 | 8 (17%) |
| KNOW_G attributed claim, general | 38 (28%) | 20 (23%) | 15 (22%) | 3 | 18 (38%) |
| RELEASE resource or code | 27 (20%) | 17 (20%) | 12 (18%) | 4 | 10 (21%) |
| CONTRIB contribution restatement | 21 (16%) | 13 (15%) | 8 (12%) | 1 | 8 (17%) |
| FUTURE future work | 4 (3%) | 0 | 0 | 0 | 4 (8%) |
| CALL call to the community | 2 (1%) | 2 (2%) | 2 (3%) | 0 | 0 |
| NAMED named-phenomenon restatement | 1 (1%) | 1 (1%) | 1 (1%) | 0 | 0 |
| PRACTICE implication for practice | 0 primary | 0 | 0 | 0 | 0 |
| IMP imperative to the reader | **0** | **0** | **0** | **0** | **0** |
| OTHER | 0 | 0 | 0 | 0 | 0 |

The attributed knowledge claim, taking KNOW_G and KNOW_A together, is the modal close at
79 of 134 (59 percent), and it is the modal close in every stratum. The split inside it
moves sharply with the kind of paper. In the ACL Anthology draw, which is 36 method papers
out of 47 in the wave where genre was coded, the claim is about the authors' own system in
29 of 44 cases. In the topical neighbour corpus, which is mostly empirical studies of
model behaviour, it is about models in general in 18 of 26.

**PRACTICE never occurs as the main assertion of a closing sentence**, but it occurs 10
times as a second move welded onto a knowledge claim or a contribution restatement:
"...highlighting the importance of jointly learning when and what to summarize for robust
long-horizon agent behavior", "...offering insights into prompt programming and model
optimization for safer AI applications". The practice implication is a trailing participial
clause in this corpus, never a sentence of its own. Secondary-tag counts across all 134:
PRACTICE 10, CALL 2, NAMED 2, FUTURE 1, RELEASE 1.

**FUTURE is a topical-corpus behaviour.** All four future-work closes are in stratum D and
all four are on papers from 2023 (Huang, Pan, Zeng, Chakrabarty). Zero of the 86
venue-corpus abstracts close on future work.

## The cross-tabulation

Rows are openings, columns are closings. The cell is the number of abstracts with that
pair. Empty columns (PRACTICE, IMP, OTHER) are kept so the zeros are visible.

**Venue corpus, n=86.**

| open \ close | KNOW_G | KNOW_A | CALL | FUTURE | RELEASE | CONTRIB | NAMED | PRACTICE | IMP | OTHER | total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Q** | **1** | 0 | 0 | 0 | 0 | **1** | 0 | 0 | 0 | 0 | 2 |
| DEF | 6 | 5 | 0 | 0 | 8 | 3 | 0 | 0 | 0 | 0 | 22 |
| SQ | 4 | 13 | 1 | 0 | 5 | 3 | 0 | 0 | 0 | 0 | 26 |
| PROB | 3 | 9 | 0 | 0 | 3 | 2 | 1 | 0 | 0 | 0 | 18 |
| SCENE | 3 | 6 | 1 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 12 |
| FIND | 3 | 0 | 0 | 0 | 1 | 2 | 0 | 0 | 0 | 0 | 6 |
| total | 20 | 33 | 2 | 0 | 17 | 13 | 1 | 0 | 0 | 0 | 86 |

**All 134.**

| open \ close | KNOW_G | KNOW_A | CALL | FUTURE | RELEASE | CONTRIB | NAMED | PRACTICE | IMP | OTHER | total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Q** | **2** | 0 | 0 | 0 | 0 | **1** | 0 | 0 | 0 | 0 | 3 |
| DEF | 9 | 8 | 0 | 0 | 10 | 5 | 0 | 0 | 0 | 0 | 32 |
| SQ | 13 | 17 | 1 | 4 | 9 | 4 | 0 | 0 | 0 | 0 | 48 |
| PROB | 5 | 9 | 0 | 0 | 5 | 3 | 1 | 0 | 0 | 0 | 23 |
| SCENE | 6 | 6 | 1 | 0 | 1 | 5 | 0 | 0 | 0 | 0 | 19 |
| FIND | 3 | 1 | 0 | 0 | 2 | 3 | 0 | 0 | 0 | 0 | 9 |
| total | 38 | 41 | 2 | 4 | 27 | 21 | 1 | 0 | 0 | 0 | 134 |

### What the table settles about the paper's current pair

**The question opening paired with a general knowledge-claim close is attested.** It occurs
twice in 134, and both instances are close relatives of this paper in subject and in
argument shape:

- `ReasoningTraces (ACL)`, opening "Can we trust the reasoning traces that large reasoning
  models (LRMs) produce?", closing "Our findings reveal a gap between the reasoning LRMs
  follow and the reasoning they report, raising concern that aligned-appearing explanations
  may not be equivalent to genuine alignment."
- `arXiv:2404.04298` (Jiang et al., SELF-[IN]CORRECT), opening "Can LLMs consistently
  improve their previous outputs for better results?", closing "This finding challenges the
  notion that LLMs may be able to enhance their performance only through their own
  judgment."

Both are studies whose result is that a model behaviour does not work as assumed. Neither
is a method paper. The third question opening, `DogCat (EACL)`, closes on a contribution
restatement instead: "CenterBench provides the first framework to identify when models
shift from structural analysis to pattern matching."

**The pairs a question opening is never seen with.** Zero of 134 pair a question opening
with KNOW_A, RELEASE, FUTURE, CALL, NAMED, PRACTICE or IMP. The two attested pairs, Q with
KNOW_G and Q with CONTRIB, cover all three cases.

### Which other cells are empty

The six openings and seven closings that occur at all define 42 cells. **16 of the 42 are
empty across all 134 abstracts, and 19 are empty in the 86-abstract venue corpus.** The
ones worth naming:

- **FIND with KNOW_A** occurs once in 134 and never in the venue corpus. A paper that opens
  by stating its own move rarely closes by reporting that its own system worked; it closes
  on a general claim (3), a contribution restatement (3), or a release (2).
- **SCENE with RELEASE** occurs once in 134 and never in the 86-abstract venue corpus, which
  is the sharpest zero in the table given that SCENE has 12 abstracts and RELEASE has 17.
  An abstract that opens on deployment closes on a claim, not on a link.
- **DEF with CALL, SCENE with FUTURE, PROB with FUTURE, PROB with CALL, FIND with CALL,
  FIND with FUTURE, DEF with FUTURE** are all zero.
- **Every cell in the IMP, PRACTICE and OTHER columns** is zero for every opening type.

## Is an imperative close attested anywhere

**No. Zero of 134.** The earlier count of zero in 48 abstracts holds on a sample nearly
three times as large and drawn a different way.

The scan was mechanical and deliberately wide. Every sentence of every abstract, not only
closings, was tested for a sentence-initial base-form verb against a 60-item list
(Consider, See, Note, Imagine, Suppose, Use, Try, Take, Let, Think, Ask, Read, Look,
Remember, Recall, Compare, Contrast, Treat, Build, Design, Start, Begin, Watch, Check,
Avoid, Adopt, Apply, Assume, Picture, Observe, Notice, Reconsider, Rethink, Ensure, Focus,
Keep, Make, Give, Put, Move, Follow, Choose, Pick, Test, Measure, Report, Cite, Prefer,
Resist, Expect, Suspend, Withhold and others). **It returned zero hits in 134 abstracts,
across all 973 sentences of the corpus, in any position.** Not one abstract in the corpus addresses
the reader with a bare imperative anywhere.

A second scan looked for the softer hortatory form, a closing sentence containing "we
should", "researchers should", "practitioners should", "the field should", "the community
should", "future work should", "one should", "must" or "ought". **Zero of 134.** The
nearest approaches are the two CALL closes, and both route the exhortation through the
paper's own work as the grammatical subject rather than addressing the reader:

- `2026.eacl-long.226`: "Our approach highlights the need to incorporate regularity across
  sets of forms in studies attempting tomeasure efficiency in language."
- `2026.eacl-long.238`: "Guided by our review, we outline opportunities for responsible and
  equitable NLP and conclude with a call for cross-disciplinary partnerships and
  human-centered approaches to ensure that future NLP technologies advance the public good."

Both say "our work shows a need exists". Neither says "do this". The construction "the
field should X" does not occur in this corpus in any position, closing or otherwise.

## How long a question opening is compared with the others

Measured in words of the first sentence, all 134 abstracts.

| Opening | n | min | 25th | median | mean | 75th | max |
|---|---|---|---|---|---|---|---|
| Q | 3 | 10 | n/a | 12.0 | 15.0 | n/a | 23 |
| DEF | 32 | 7 | 15 | 19.0 | 19.8 | 24 | 42 |
| SQ | 48 | 9 | 16 | 19.0 | 21.0 | 25 | 48 |
| FIND | 9 | 13 | 17 | 20.0 | 20.7 | 21 | 35 |
| PROB | 23 | 7 | 16 | 21.0 | 21.3 | 26 | 36 |
| SCENE | 19 | 10 | 13 | 21.0 | 21.8 | 28 | 44 |
| All non-Q | 131 | 7 | 16 | 20.0 | 20.9 | 25 | 48 |

The three question openings are 10, 12 and 23 words. The median non-question opening is
20 words, and only 15 of 131 non-question openings are 12 words or shorter. **A question
opening in this corpus is about 40 percent shorter than the median opening of any other
type**, and two of the three sit in the shortest tenth of all openings.

The three, verbatim, with their word counts:

- 10 words. `arXiv:2404.04298`: "Can LLMs consistently improve their previous outputs for better results?"
- 12 words. `ReasoningTraces (ACL)`: "Can we trust the reasoning traces that large reasoning models (LRMs) produce?"
- 23 words. `DogCat (EACL)`: "When language models correctly parse "The cat that the dog chased meowed," are they analyzing syntax or simply familiar with dogs chasing cats?"

The paper's own opening, "Do language models know when a good answer should be left
alone?", is 12 words, which is the median of the three and matches the ReasoningTraces
construction almost exactly in length and in shape: modal or auxiliary, "we" or the model
class as subject, one embedded relative, no example inside the question.

Two constructions are visible in the three. Two of them (Jiang, ReasoningTraces) are bare
polar questions with no scene inside them. The third (DogCat) puts its example inside
the question and doubles its length to do it, then poses a disjunction rather than a polar
question. The paper's current opening follows the first construction.

## A fourth question-marked opening, which is not a question

`ZIP (*SEM)` opens with a sentence that ends in a question mark but whose main assertion is
declarative: "While zero-shot instructional prompts like "Let's think step-by-step" have
revolutionized Large Language Model performance, we lack systematic understanding of why:
which specific words drive their effectiveness, and how do these patterns vary across tasks
and models?" It is coded PROB, because the sentence asserts a gap and then itemizes it as
two embedded questions after a colon. It is reported here because a mechanical count of
first sentences ending in "?" returns 4, not 3, and the difference is a coding decision
rather than a measurement.

This is a third available construction: state the gap, then let a colon open into the
questions, so the abstract gets the interrogative energy without the abstract's first
grammatical assertion being a question.

## Where question openings get answered

All three question-opening abstracts answer their question. None answers it with a bare
"yes" or "no", none repeats the question, and none uses the words "the answer is".

**`ReasoningTraces (ACL)`, question at sentence 1 of 8.** Answered in two halves and then
sealed at the close.

- Half one, sentence 4 of 8 (0.50 through): "Across 45,000 samples from three LRMs, we find
  that injected hints reliably alter outputs, confirming that reasoning traces causally
  shape model behavior."
- Half two, sentence 5 of 8 (0.63 through): "However, when asked to explain their changed
  answers, models overwhelmingly refuse to disclose the influence: non-disclosure exceeds
  90% for extreme hints across 30,000 follow-up samples."
- Verdict, sentence 8 of 8 (1.00): "Our findings reveal a gap between the reasoning LRMs
  follow and the reasoning they report, raising concern that aligned-appearing explanations
  may not be equivalent to genuine alignment."

**`arXiv:2404.04298` (Jiang et al.), question at sentence 1 of 6.** Answered once, in the
results sentence.

- Sentence 5 of 6 (0.83 through): "In our resulting experimental analysis of several
  open-source and industrial LLMs, we observe that models are not reliably better at
  discriminating among previously-generated alternatives than generating initial responses."
- Sentence 6 of 6 restates the consequence: "This finding challenges the notion that LLMs
  may be able to enhance their performance only through their own judgment."

**`DogCat (EACL)`, question at sentence 1 of 9.** Answered once, in the results sentence, as
"both, and the balance moves".

- Sentence 5 of 9 (0.56 through): "Testing six models reveals that performance gaps between
  plausible and implausible sentences widen systematically with complexity, with models
  showing median gaps up to 26.8 percentage points, quantifying when they abandon structural
  analysis for semantic associations."
- The close does not answer it; it restates the contribution: "CenterBench provides the
  first framework to identify when models shift from structural analysis to pattern
  matching."

The common pattern across all three: the answer arrives in the first results sentence,
between halfway and five-sixths of the way through, and it arrives as a finding sentence
with an ordinary reporting verb ("we find", "we observe", "reveals"), not as an answer
addressed back to the question. The question is a frame the abstract sets and then stops
mentioning.

## Questions that are not openings

Five further abstracts pose a question somewhere other than the first sentence. All five
put it in the first half, and in the ACL Anthology cases it is at sentence 3 in a
seven-to-nine-sentence abstract, immediately before the method beat.

- `2026.acl-long.1432`, sentence 3 of 9: "This situation poses a central question: can we
  automatically create and adapt domain agents in the wild?"
- `2026.acl-long.1766`, sentence 3 of 8: "This observation motivates a fundamental question:
  Can we explicitly bootstrap such ability to alleviate overthinking in LRMs?"
- `2026.findings-acl.190`, sentence 3 of 8: "We develop an oracle counterfactual framework
  for multi-turn problems that asks: how would an agent perform if it could leverage an
  oracle to perfectly execute a specific skill?"
- `CommonToWhom (ACL)`, sentence 2 of 7: "But does cultural commonsense hold uniformly within
  a nation, or does it vary at the sub-national level?"
- `arXiv:2404.13076`, sentence 4 of 8: "But do LLMs actually recognize their own outputs when
  they give those texts higher scores, or is it just a coincidence?"

Two of the ACL cases use the identical framing device, a declarative sentence that names the
question and a colon that delivers it, and in both the very next sentence begins "To this
end, we propose" or "To address these limitations, we propose". So the venue does use the
interrogative, at a rate of 3 in 67 in the systematic ACL draw against 0 in 67 for the
question opening. It uses it as a hinge into the method, one or two sentences in, after the
status quo and the gap have been laid out.

## Whether opening type moves with numeric density or with length

**Length.** Abstract length by opening type, all 134, median words: SCENE 182, PROB 166,
Q 167, SQ 164.5, DEF 163, FIND 151. Median sentence counts are 7 for DEF, SQ and PROB and 8
for SCENE and Q, 6 for FIND. The spread across types is about 30 words on a median of
roughly 165, and the only type that stands apart is FIND, which is both the shortest and the
one with the fewest sentences. An abstract that opens by stating its own move spends fewer
words getting to the point and finishes sooner.

**Density.** Using the hand-verified quantitative-numeral counts already established for the
47 wave-1 abstracts, where a numeral is counted only if it is not part of a model name, a
dataset name, a year or an enumerator:

| Opening | n | median per 100w | mean per 100w | max | abstracts with no quantitative digit |
|---|---|---|---|---|---|
| SQ | 17 | 0.57 | 0.89 | 2.93 | 8 of 17 |
| DEF | 9 | 0.00 | 0.40 | 1.86 | 6 of 9 |
| PROB | 9 | 0.00 | 0.16 | 0.88 | 7 of 9 |
| SCENE | 8 | 0.00 | 0.20 | 1.59 | 7 of 8 |
| FIND | 4 | 0.00 | 0.16 | 0.65 | 3 of 4 |

Status-quo openings are the only type whose median is above zero, and they hold the
densest abstract in the sample. Every other type has a median of zero. With 4 to 17
abstracts per cell this is a direction and not an estimate, and the confound is visible in
the genre cross-tabulation: SQ openings are 14 of 17 method papers and the method papers
are where the improvement percentages sit. There is no question-opening cell in stratum A
at all, so nothing can be said about the density of a question-opening abstract from the
systematic ACL sample.

The practical reading is that opening type does not buy or cost numbers. The density
question and the opening question are close to independent in this corpus, and the choice
of opening can be made on rhetorical grounds without a density consequence.

## Which pairs are available to this paper, and what each implies for the beats between

The paper is an empirical study of model behaviour whose principal result is negative:
undirected revision lowers the quality of work that was already sufficient. In stratum A
the eleven non-method papers (analysis, benchmark and position) close on CONTRIB 4,
RELEASE 3, KNOW_G 2, KNOW_A 1, CALL 1. In stratum D, which is almost entirely this kind of
paper, KNOW_G is the modal close at 18 of 48. So the relevant comparison set for a negative
behavioural finding closes on a general knowledge claim more often than on anything else,
even though the venue as a whole closes on an own-artifact claim.

**1. Question opening with a general knowledge-claim close. Attested, 2 of 134, 0 of 67 in
the systematic ACL draw.** This is what the abstract does now. Both attested instances are
negative-result behavioural studies, which is the same shape as this paper, and both put the
answer to the question in a results sentence between halfway and five-sixths through rather
than answering it early. The beats this pair requires: the question, then the reason the
question is open, then the design, then a results sentence that answers it, then a close that
states what is now known. The evidence says the pair works for exactly this kind of paper
and that it is rare. The cost is not that it is unattested; it is that the systematic draw
did not produce a single instance, so a reviewer's sense of the local norm will not include
it.

**2. Question opening with a contribution-restatement close. Attested, 1 of 134.** DogCat
does this: it asks the question, answers it at sentence 5, and then closes on what the
benchmark provides rather than on what is now known. This pair is available if the paper
wants the last sentence to be about the study's design rather than its finding, but it
spends the strongest position in the abstract on the apparatus, which is the wrong trade for
a paper whose result is the contribution.

**3. Problem-statement opening with a general knowledge-claim close. Attested, 5 of 134, 3
of 86 in the venue corpus.** The gap-first construction. It converts the current first
sentence from a question into an assertion of what is not known, and keeps the close
untouched. The beats are identical to option 1 except that the first sentence is
declarative, which means the second sentence no longer has to justify the question and can
go straight to the deployment scene. This is the closest neighbour to the current abstract
that appears in the venue draw.

**4. Deployment scene-setting with a general knowledge-claim close. Attested, 6 of 134, 3
of 86.** Open on the fact that models are handed work their users cannot check, then the
gap, then design, then finding, then the claim. This is the most common construction among
the behavioural studies in stratum D that report a negative finding (Fanous on sycophancy,
Borchers on teacher revisions, Lee on human-LM interaction). It buys the reader the stakes
before the gap, at the cost of one sentence.

**5. Definition of the object with a general knowledge-claim close. Attested, 9 of 134, 6
of 86.** "Undirected revision is..." The construction the Kamoi survey uses. It suits a
paper that has to define a construct the reader does not already hold. This paper's
construct, revision without a stated fault, is arguably one of those, so the option is real,
but the definition beat costs a sentence that the current opening spends on the question.

**6. Status-quo opening with a general knowledge-claim close. Attested, 13 of 134, 4 of 86.**
The most common opening in the corpus paired with the close the paper already has. It is
the safest available pair and the least distinguishing: 48 of 134 abstracts open this way,
so the first sentence does no work to separate this paper from its neighbours.

**7. Finding-first opening with a general knowledge-claim close. Attested, 3 of 134, 3 of
86.** State the result in sentence one and spend the rest of the abstract on how it was
established. Notably, FIND-opening abstracts are the shortest in the corpus at a median of
151 words and 6 sentences, so this option would need the beats compressed.

**Pairs that are not available.** A closing imperative to the reader is unattested in 134
abstracts and in all 973 of their sentences, so an abstract that ends by telling the reader what
to do would be the only one in the corpus. A closing call to the community is attested twice
and both times the paper's own work is the grammatical subject, so the form available is
"our results show a need exists", not "the field should". A future-work close does not occur
anywhere in the 86-abstract venue corpus. A question opening paired with an own-artifact
performance close, a release close, a future-work close or a call close is unattested in all
134.

**What the beats have to do in every one of the available pairs.** In all three
question-opening abstracts the answer arrives in a results sentence between halfway and
five-sixths of the way through, never in sentence 2, and in the two that close on a general
knowledge claim the closing sentence is the first place that claim appears in its general
form: the results sentences before it report what happened in the study, and only the close
says what is now known about models. The current abstract already does both. That
observation is checked against the three question-opening abstracts, quoted in full in the
answering-sentence section above, and is not a claim about all 38 general-knowledge-claim
closes in the corpus.

## Corpus index: identifier, retrieval date, codes

Titles are as printed on the source page. Stratum C entries were held under working
nicknames when first gathered and no landing-page URL was recorded with them; they are
listed under those nicknames.

| # | Stratum | Identifier | Retrieved | Words | Sent | Opening | Closing | Title |
|---|---|---|---|---|---|---|---|---|
| 1 | A | [2026.acl-long.1099](https://aclanthology.org/2026.acl-long.1099/) | 2026-09-06 | 189 | 7 | SQ | KNOW_A | Powering Verifiable Learning via Automated Evolutionary Data Synthesis |
| 2 | A | [2026.acl-long.1210](https://aclanthology.org/2026.acl-long.1210/) | 2026-09-06 | 204 | 8 | SQ | KNOW_A | EQUIP: EQUivariant preserving In-Place updates for Efficient Token Pr... |
| 3 | A | [2026.acl-long.1321](https://aclanthology.org/2026.acl-long.1321/) | 2026-09-06 | 157 | 6 | SQ | KNOW_A | CURE: Critique-Driven Unified Reinforcement Learning for Test-Time Se... |
| 4 | A | [2026.acl-long.1432](https://aclanthology.org/2026.acl-long.1432/) | 2026-09-06 | 203 | 9 | SCENE | KNOW_A | ReCreate: Reasoning and Creating Domain Agents Driven by Experience |
| 5 | A | [2026.acl-long.1543](https://aclanthology.org/2026.acl-long.1543/) | 2026-09-06 | 157 | 8 | SQ | KNOW_A | NeuralFSM: Adaptive Multi-Agent Coordination via Learning Finite-Stat... |
| 6 | A | [2026.acl-long.1655](https://aclanthology.org/2026.acl-long.1655/) | 2026-09-06 | 189 | 6 | SCENE | CONTRIB | GenomeQA: Benchmarking General Large Language Models for Genome Seque... |
| 7 | A | [2026.acl-long.1766](https://aclanthology.org/2026.acl-long.1766/) | 2026-09-06 | 202 | 8 | SQ | KNOW_A | Think How to Think: Mitigating Overthinking with Autonomous Difficult... |
| 8 | A | [2026.acl-long.1877](https://aclanthology.org/2026.acl-long.1877/) | 2026-09-06 | 212 | 7 | SQ | KNOW_G | BOSCH: Black-Box Binary Optimization for Short-Context Attention-Head... |
| 9 | A | [2026.acl-long.1988](https://aclanthology.org/2026.acl-long.1988/) | 2026-09-06 | 154 | 6 | FIND | KNOW_G/CALL | AutoRAN: Automated Hijacking of Safety Reasoning in Large Reasoning M... |
| 10 | A | [2026.acl-long.2099](https://aclanthology.org/2026.acl-long.2099/) | 2026-09-06 | 119 | 4 | PROB | KNOW_A | GRAD: Generalizing RAG Adaptation with Decoding |
| 11 | A | [2026.acl-long.210](https://aclanthology.org/2026.acl-long.210/) | 2026-09-06 | 119 | 6 | FIND | RELEASE | Revisiting a Pain in the Neck: A Semantic Reasoning Benchmark for Lan... |
| 12 | A | [2026.acl-long.2210](https://aclanthology.org/2026.acl-long.2210/) | 2026-09-06 | 168 | 8 | PROB | RELEASE | TRAC: Teacher-Guided Token Reward with Adaptive Calibration for Robus... |
| 13 | A | [2026.acl-long.321](https://aclanthology.org/2026.acl-long.321/) | 2026-09-06 | 151 | 6 | DEF | KNOW_A | STRIDE-ED: A Strategy-Grounded Stepwise Reasoning Framework for Empat... |
| 14 | A | [2026.acl-long.432](https://aclanthology.org/2026.acl-long.432/) | 2026-09-06 | 175 | 8 | SQ | RELEASE | PAM: Enhancing General Alignment of Large Reasoning Models through Pr... |
| 15 | A | [2026.acl-long.544](https://aclanthology.org/2026.acl-long.544/) | 2026-09-06 | 174 | 11 | DEF | RELEASE | EvoNarrator: Modeling Scientific Evolution for Feasible Hypothesis Ge... |
| 16 | A | [2026.acl-long.655](https://aclanthology.org/2026.acl-long.655/) | 2026-09-06 | 161 | 6 | PROB | KNOW_A/PRACTICE | ModeX: Evaluator-Free Best-of-N Selection for Open-Ended Generation |
| 17 | A | [2026.acl-long.766](https://aclanthology.org/2026.acl-long.766/) | 2026-09-06 | 122 | 7 | SCENE | KNOW_G | Mind the Gap in Cultural Alignment: Task-Aware Culture Management for... |
| 18 | A | [2026.acl-long.877](https://aclanthology.org/2026.acl-long.877/) | 2026-09-06 | 136 | 6 | SQ | KNOW_A | Discourse Coherence and Response-Guided Context Rewriting for Multi-P... |
| 19 | A | [2026.acl-long.988](https://aclanthology.org/2026.acl-long.988/) | 2026-09-06 | 163 | 7 | SQ | KNOW_A/PRACTICE | WebClipper: Efficient Evolution of Web Agents with Graph-based Trajec... |
| 20 | A | [2026.acl-long.99](https://aclanthology.org/2026.acl-long.99/) | 2026-09-06 | 159 | 5 | DEF | CONTRIB | Mechanistic Interpretability Should Prioritize Feature Consistency in... |
| 21 | A | [2026.acl-short.1](https://aclanthology.org/2026.acl-short.1/) | 2026-09-06 | 154 | 6 | DEF | KNOW_A | Punctuation-Steered Representation Fine-Tuning |
| 22 | A | [2026.acl-short.20](https://aclanthology.org/2026.acl-short.20/) | 2026-09-06 | 154 | 5 | SQ | KNOW_A | Reliable Use of Lemmas via Eligibility Reasoning and Section-Aware Re... |
| 23 | A | [2026.acl-short.38](https://aclanthology.org/2026.acl-short.38/) | 2026-09-06 | 161 | 9 | DEF | KNOW_A | UERLens: Understanding Event Relations in Large Language Models |
| 24 | A | [2026.acl-short.57](https://aclanthology.org/2026.acl-short.57/) | 2026-09-06 | 73 | 3 | PROB | KNOW_A | FL-MSCL: A Unified Figurative Language Detection Model Driven by Mult... |
| 25 | A | [2026.eacl-long.128](https://aclanthology.org/2026.eacl-long.128/) | 2026-09-06 | 128 | 6 | FIND | CONTRIB | Argumentation and Judgement Factors: LLM-based Discovery and Applicat... |
| 26 | A | [2026.eacl-long.177](https://aclanthology.org/2026.eacl-long.177/) | 2026-09-06 | 152 | 7 | SCENE | KNOW_G | FaithLM: Towards Faithful Explanations for Large Language Models |
| 27 | A | [2026.eacl-long.226](https://aclanthology.org/2026.eacl-long.226/) | 2026-09-06 | 192 | 8 | SQ | CALL | Recursive numeral systems are highly regular and easy to process |
| 28 | A | [2026.eacl-long.276](https://aclanthology.org/2026.eacl-long.276/) | 2026-09-06 | 162 | 6 | DEF | CONTRIB | Multi-Token Completion for Text Anonymization |
| 29 | A | [2026.eacl-long.29](https://aclanthology.org/2026.eacl-long.29/) | 2026-09-06 | 178 | 8 | PROB | KNOW_G | Detecting (Un)answerability in Large Language Models with Linear Dire... |
| 30 | A | [2026.eacl-long.325](https://aclanthology.org/2026.eacl-long.325/) | 2026-09-06 | 170 | 8 | SQ | RELEASE | AICD Bench: A Challenging Benchmark for AI-Generated Code Detection |
| 31 | A | [2026.eacl-long.374](https://aclanthology.org/2026.eacl-long.374/) | 2026-09-06 | 129 | 6 | DEF | KNOW_G | Are All Prompt Components Value-Neutral? Understanding the Heterogene... |
| 32 | A | [2026.eacl-long.79](https://aclanthology.org/2026.eacl-long.79/) | 2026-09-06 | 161 | 8 | SCENE | KNOW_A | SearchLLM: Detecting LLM Paraphrased Text by Measuring the Similarity... |
| 33 | A | [2026.findings-acl.1123](https://aclanthology.org/2026.findings-acl.1123/) | 2026-09-06 | 193 | 9 | SCENE | KNOW_A | Memory Matters More: Event-Centric Memory as a Logic Map for Agent Se... |
| 34 | A | [2026.findings-acl.1259](https://aclanthology.org/2026.findings-acl.1259/) | 2026-09-06 | 152 | 6 | DEF | KNOW_A | Think Before you Write: QA-Guided Reasoning for Character Description... |
| 35 | A | [2026.findings-acl.1394](https://aclanthology.org/2026.findings-acl.1394/) | 2026-09-06 | 156 | 7 | SQ | KNOW_A | Beyond the Safety Tax: Mitigating Unsafe Text-to-Image Generation via... |
| 36 | A | [2026.findings-acl.1529](https://aclanthology.org/2026.findings-acl.1529/) | 2026-09-06 | 180 | 7 | PROB | RELEASE | Reasoning in a Combinatorial and Constrained World: Benchmarking LLMs... |
| 37 | A | [2026.findings-acl.177](https://aclanthology.org/2026.findings-acl.177/) | 2026-09-06 | 131 | 6 | SQ | KNOW_A | Subgraph-Guided Executable Logical Form Generation for Knowledge Base... |
| 38 | A | [2026.findings-acl.1799](https://aclanthology.org/2026.findings-acl.1799/) | 2026-09-06 | 191 | 10 | SCENE | CONTRIB | Do LLM Agents Really Mimic Humans? Diagnosing and Aligning Microecono... |
| 39 | A | [2026.findings-acl.1935](https://aclanthology.org/2026.findings-acl.1935/) | 2026-09-06 | 154 | 6 | SQ | CONTRIB | Parametric Knowledge is Not All You Need: Toward Honest Large Languag... |
| 40 | A | [2026.findings-acl.2070](https://aclanthology.org/2026.findings-acl.2070/) | 2026-09-06 | 231 | 10 | FIND | KNOW_G | LLMs are Brittle to Simple Code Transformations: Introducing CETBench... |
| 41 | A | [2026.findings-acl.312](https://aclanthology.org/2026.findings-acl.312/) | 2026-09-06 | 163 | 7 | PROB | KNOW_A | Iterative Self-Correction for Text-Driven Person Re-Identification wi... |
| 42 | A | [2026.findings-acl.42](https://aclanthology.org/2026.findings-acl.42/) | 2026-09-06 | 155 | 7 | SQ | KNOW_A | Bridging the Culture Gap: A Framework for LLM-Driven Socio-Cultural L... |
| 43 | A | [2026.findings-acl.447](https://aclanthology.org/2026.findings-acl.447/) | 2026-09-06 | 173 | 6 | DEF | KNOW_G | Self-Sum: Teaching an Agent to Decide Itself When and What to Summarize |
| 44 | A | [2026.findings-acl.583](https://aclanthology.org/2026.findings-acl.583/) | 2026-09-06 | 113 | 5 | PROB | NAMED | The Mechanics of Interference: Defusing Distractors in RAG via Sparse... |
| 45 | A | [2026.findings-acl.718](https://aclanthology.org/2026.findings-acl.718/) | 2026-09-06 | 160 | 8 | SCENE | KNOW_A | LPO: Towards Accurate GUI Agent Interaction via Location Preference O... |
| 46 | A | [2026.findings-acl.853](https://aclanthology.org/2026.findings-acl.853/) | 2026-09-06 | 166 | 7 | PROB | KNOW_A | Multi-Hop Knowledge Editing via Critic-Guided Multi-Agent Reasoning |
| 47 | A | [2026.findings-acl.988](https://aclanthology.org/2026.findings-acl.988/) | 2026-09-06 | 158 | 7 | SQ | RELEASE | MASS: Deep Research for Social Sciences with Memory-Augmented Social ... |
| 48 | A2 | [2026.acl-long.1118](https://aclanthology.org/2026.acl-long.1118/) | 2026-09-06 | 166 | 7 | PROB | RELEASE | LAMCL: A Length-aware Momentum Contrastive Learning Framework for Mul... |
| 49 | A2 | [2026.acl-long.1396](https://aclanthology.org/2026.acl-long.1396/) | 2026-09-06 | 196 | 10 | SCENE | KNOW_A | Towards Interpretable Tabular Reasoning: Enhancing LLM Reasoning on T... |
| 50 | A2 | [2026.acl-long.1674](https://aclanthology.org/2026.acl-long.1674/) | 2026-09-06 | 181 | 7 | PROB | KNOW_A | PICTURE: Enhancing Theory-of-Mind in Large Language Models by Reveali... |
| 51 | A2 | [2026.acl-long.1951](https://aclanthology.org/2026.acl-long.1951/) | 2026-09-06 | 213 | 10 | DEF | RELEASE | From Proof to Program: Characterizing Tool-Induced Reasoning Hallucin... |
| 52 | A2 | [2026.acl-long.285](https://aclanthology.org/2026.acl-long.285/) | 2026-09-06 | 188 | 6 | DEF | RELEASE | UniSpec: Training-Free Speculative Decoding for Robust LLM Accelerati... |
| 53 | A2 | [2026.acl-long.563](https://aclanthology.org/2026.acl-long.563/) | 2026-09-06 | 135 | 7 | PROB | KNOW_A | PRISM: Probabilistic Reward Model with Inherent Structural Modeling |
| 54 | A2 | [2026.acl-long.7](https://aclanthology.org/2026.acl-long.7/) | 2026-09-06 | 147 | 7 | SQ | KNOW_G | Different types of syntactic agreement recruit the same units within ... |
| 55 | A2 | [2026.acl-long.840](https://aclanthology.org/2026.acl-long.840/) | 2026-09-06 | 152 | 7 | DEF | KNOW_G | TalkLoRA: Communication-Aware Mixture of Low-Rank Adaptation for Larg... |
| 56 | A2 | [2026.acl-short.30](https://aclanthology.org/2026.acl-short.30/) | 2026-09-06 | 179 | 7 | DEF | RELEASE | CheckMIABench: Firm Foundations For Membership Inference Attacks on L... |
| 57 | A2 | [2026.acl-short.67](https://aclanthology.org/2026.acl-short.67/) | 2026-09-06 | 92 | 4 | FIND | KNOW_G | T⋆: Progressive Block Scaling for Masked Diffusion Language Models Th... |
| 58 | A2 | [2026.eacl-long.139](https://aclanthology.org/2026.eacl-long.139/) | 2026-09-06 | 173 | 6 | PROB | KNOW_G | Safe-Unsafe Concept Separation Emerges from a Single Direction in Lan... |
| 59 | A2 | [2026.eacl-long.238](https://aclanthology.org/2026.eacl-long.238/) | 2026-09-06 | 104 | 4 | SCENE | CALL | NLP for Social Good: A Survey and Outlook of Challenges, Opportunitie... |
| 60 | A2 | [2026.eacl-long.336](https://aclanthology.org/2026.eacl-long.336/) | 2026-09-06 | 188 | 8 | SQ | RELEASE | Incentivizing Strong Reasoning from Weak Supervision |
| 61 | A2 | [2026.eacl-long.41](https://aclanthology.org/2026.eacl-long.41/) | 2026-09-06 | 150 | 6 | SQ | KNOW_A | SCoNE: a Self-Correcting and Noise-Augmented Method for Complex Biolo... |
| 62 | A2 | [2026.findings-acl.1272](https://aclanthology.org/2026.findings-acl.1272/) | 2026-09-06 | 103 | 6 | DEF | KNOW_G | ClimateCause: Complex and Implicit Causal Structures in Climate Reports |
| 63 | A2 | [2026.findings-acl.1632](https://aclanthology.org/2026.findings-acl.1632/) | 2026-09-06 | 164 | 6 | DEF | KNOW_G/PRACTICE | Multilingual Tokenization through the Lens of Indian Languages: Chall... |
| 64 | A2 | [2026.findings-acl.190](https://aclanthology.org/2026.findings-acl.190/) | 2026-09-06 | 211 | 8 | SQ | CONTRIB/FUTURE | LUMINA: Long-horizon Understanding for Multi-turn Interactive Agents |
| 65 | A2 | [2026.findings-acl.1993](https://aclanthology.org/2026.findings-acl.1993/) | 2026-09-06 | 164 | 7 | PROB | KNOW_A | PsychePass: Calibrating LLM Therapeutic Competence via Trajectory-Anc... |
| 66 | A2 | [2026.findings-acl.551](https://aclanthology.org/2026.findings-acl.551/) | 2026-09-06 | 151 | 7 | DEF | CONTRIB | Infusing Theory of Mind into Socially Intelligent LLM Agents |
| 67 | A2 | [2026.findings-acl.911](https://aclanthology.org/2026.findings-acl.911/) | 2026-09-06 | 121 | 6 | SQ | KNOW_G/CALL | OMHBench: Benchmarking Balanced and Grounded Omni-Modal Multi-Hop Rea... |
| 68 | B | [arXiv:2501.00353](https://arxiv.org/abs/2501.00353) | 2026-09-06 | 153 | 8 | SQ | RELEASE | RAG-Instruct: Boosting LLMs with Diverse Retrieval-Augmented Instruct... |
| 69 | B | [arXiv:2503.03340](https://arxiv.org/abs/2503.03340) | 2026-09-06 | 152 | 5 | DEF | KNOW_A | EnigmaToM: Improve LLMs' Theory-of-Mind Reasoning Capabilities with N... |
| 70 | B | [arXiv:2505.12625](https://arxiv.org/abs/2505.12625) | 2026-09-06 | 198 | 10 | SQ | KNOW_G | R1dacted: Investigating Local Censorship in DeepSeek's R1 Language Model |
| 71 | B | [arXiv:2507.10972](https://arxiv.org/abs/2507.10972) | 2026-09-06 | 137 | 5 | SQ | KNOW_A | Teach Me Sign: Stepwise Prompting LLM for Sign Language Production |
| 72 | B | [arXiv:2509.17641](https://arxiv.org/abs/2509.17641) | 2026-09-06 | 145 | 7 | DEF | RELEASE | AuditoryBench++: Can Language Models Understand Auditory Knowledge wi... |
| 73 | B | [arXiv:2511.16811](https://arxiv.org/abs/2511.16811) | 2026-09-06 | 105 | 4 | FIND | CONTRIB | From Representation to Enactment: The ABC Framework of the Translatin... |
| 74 | B | [arXiv:2601.19923](https://arxiv.org/abs/2601.19923) | 2026-09-06 | 179 | 7 | SCENE | KNOW_G | Structure-BiEval: A Self-Supervised, Dual-Track Framework for Decoupl... |
| 75 | B | [arXiv:2603.03203](https://arxiv.org/abs/2603.03203) | 2026-09-06 | 128 | 6 | DEF | RELEASE | No Memorization, No Detection: Output Distribution-Based Contaminatio... |
| 76 | B | [arXiv:2605.15040](https://arxiv.org/abs/2605.15040) | 2026-09-06 | 246 | 11 | DEF | KNOW_G | Orchard: An Open-Source Agentic Modeling Framework |
| 77 | B | [arXiv:2607.23597](https://arxiv.org/abs/2607.23597) | 2026-09-06 | 207 | 10 | DEF | RELEASE | HiTMS: A High-Throughput Multi-Stream Linguistic Steganography Framework |
| 78 | C | CGM (Findings) | 2026-09-02 | 190 | 11 | DEF | RELEASE | CGM (Findings) |
| 79 | C | CommonToWhom (ACL) | 2026-09-02 | 184 | 7 | PROB | CONTRIB | CommonToWhom (ACL) |
| 80 | C | DART (Findings) | 2026-09-02 | 230 | 8 | PROB | KNOW_G | DART (Findings) |
| 81 | C | DogCat (EACL) | 2026-09-02 | 199 | 9 | Q | CONTRIB | DogCat (EACL) |
| 82 | C | MemoryDial (Findings) | 2026-09-02 | 156 | 6 | SQ | CONTRIB | MemoryDial (Findings) |
| 83 | C | ReasoningTraces (ACL) | 2026-09-02 | 167 | 8 | Q | KNOW_G | ReasoningTraces (ACL) |
| 84 | C | SAGE (ACL) | 2026-09-02 | 155 | 7 | PROB | KNOW_A | SAGE (ACL) |
| 85 | C | SCOPE (ICML) | 2026-09-02 | 142 | 5 | SCENE | KNOW_A | SCOPE (ICML) |
| 86 | C | ZIP (*SEM) | 2026-09-02 | 160 | 5 | PROB | CONTRIB/PRACTICE | ZIP (*SEM) |
| 87 | D | [arXiv:2211.00053](https://arxiv.org/abs/2211.00053) | 2026-09-02 | 155 | 6 | DEF | KNOW_A | Welleck et al. — Generating Sequences by Learning to Self-Correct |
| 88 | D | [arXiv:2211.03622](https://arxiv.org/abs/2211.03622) | 2026-09-02 | 151 | 5 | FIND | CONTRIB/RELEASE | Perry et al. — Do Users Write More Insecure Code with AI Assistants? |
| 89 | D | [arXiv:2212.09251](https://arxiv.org/abs/2212.09251) | 2026-09-02 | 197 | 10 | SQ | KNOW_G | Perez et al. — Discovering Language Model Behaviors with Model-Writte... |
| 90 | D | [arXiv:2212.09746](https://arxiv.org/abs/2212.09746) | 2026-09-02 | 170 | 7 | SCENE | KNOW_G | Lee et al. — Evaluating Human-Language Model Interaction |
| 91 | D | [arXiv:2302.06590](https://arxiv.org/abs/2302.06590) | 2026-09-02 | 76 | 5 | SQ | KNOW_G/PRACTICE | Peng et al. — The Impact of AI on Developer Productivity: Evidence fr... |
| 92 | D | [arXiv:2303.11366](https://arxiv.org/abs/2303.11366) | 2026-09-02 | 178 | 7 | SCENE | CONTRIB | Shinn et al. — Reflexion: Language Agents with Verbal Reinforcement L... |
| 93 | D | [arXiv:2303.16634](https://arxiv.org/abs/2303.16634) | 2026-09-02 | 184 | 9 | PROB | RELEASE | Liu et al. — G-Eval: NLG Evaluation using GPT-4 with Better Human Ali... |
| 94 | D | [arXiv:2303.17651](https://arxiv.org/abs/2303.17651) | 2026-09-02 | 173 | 7 | PROB | KNOW_G | Madaan et al. — Self-Refine: Iterative Refinement with Self-Feedback |
| 95 | D | [arXiv:2304.05128](https://arxiv.org/abs/2304.05128) | 2026-09-02 | 220 | 8 | SQ | KNOW_A | Chen et al. — Teaching Large Language Models to Self-Debug |
| 96 | D | [arXiv:2305.11738](https://arxiv.org/abs/2305.11738) | 2026-09-02 | 166 | 7 | SQ | KNOW_G | Gou et al. — CRITIC: Large Language Models Can Self-Correct with Tool... |
| 97 | D | [arXiv:2305.17926](https://arxiv.org/abs/2305.17926) | 2026-09-02 | 213 | 6 | FIND | RELEASE | Wang et al. — Large Language Models are not Fair Evaluators |
| 98 | D | [arXiv:2306.05685](https://arxiv.org/abs/2306.05685) | 2026-09-02 | 184 | 8 | PROB | RELEASE | Zheng et al. — Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena |
| 99 | D | [arXiv:2306.09896](https://arxiv.org/abs/2306.09896) | 2026-09-02 | 191 | 7 | SQ | KNOW_G | Olausson et al. — Is Self-Repair a Silver Bullet for Code Generation? |
| 100 | D | [arXiv:2308.03188](https://arxiv.org/abs/2308.03188) | 2026-09-02 | 140 | 7 | SQ | FUTURE | Pan et al. — Automatically Correcting Large Language Models: Surveyin... |
| 101 | D | [arXiv:2308.03958](https://arxiv.org/abs/2308.03958) | 2026-09-02 | 195 | 7 | DEF | RELEASE | Wei et al. — Simple synthetic data reduces sycophancy in large langua... |
| 102 | D | [arXiv:2309.11495](https://arxiv.org/abs/2309.11495) | 2026-09-02 | 106 | 4 | DEF | KNOW_A | Dhuliawala et al. — Chain-of-Verification Reduces Hallucination in La... |
| 103 | D | [arXiv:2309.12570](https://arxiv.org/abs/2309.12570) | 2026-09-02 | 146 | 6 | SQ | FUTURE | Chakrabarty et al. — Creativity Support in the Age of Large Language ... |
| 104 | D | [arXiv:2310.01783](https://arxiv.org/abs/2310.01783) | 2026-09-02 | 278 | 14 | DEF | KNOW_G | Liang et al. — Can large language models provide useful feedback on r... |
| 105 | D | [arXiv:2310.01798](https://arxiv.org/abs/2310.01798) | 2026-09-02 | 142 | 7 | SQ | FUTURE | Huang et al. — Large Language Models Cannot Self-Correct Reasoning Yet |
| 106 | D | [arXiv:2310.07641](https://arxiv.org/abs/2310.07641) | 2026-09-02 | 181 | 7 | SQ | FUTURE | Zeng et al. — Evaluating Large Language Models at Evaluating Instruct... |
| 107 | D | [arXiv:2310.08118](https://arxiv.org/abs/2310.08118) | 2026-09-02 | 172 | 7 | SQ | KNOW_G | Valmeekam et al. — Can Large Language Models Really Improve by Self-c... |
| 108 | D | [arXiv:2310.12397](https://arxiv.org/abs/2310.12397) | 2026-09-02 | 255 | 9 | SQ | KNOW_G | Stechly et al. — GPT-4 Doesn't Know It's Wrong: An Analysis of Iterat... |
| 109 | D | [arXiv:2310.13548](https://arxiv.org/abs/2310.13548) | 2026-09-02 | 164 | 9 | SQ | KNOW_G/NAMED | Sharma et al. — Towards Understanding Sycophancy in Language Models |
| 110 | D | [arXiv:2311.08516](https://arxiv.org/abs/2311.08516) | 2026-09-02 | 202 | 8 | SQ | RELEASE | Tyen et al. — LLMs cannot find reasoning errors, but can correct them... |
| 111 | D | [arXiv:2311.09469](https://arxiv.org/abs/2311.09469) | 2026-09-02 | 190 | 9 | DEF | CONTRIB | Zhang and Choi — Clarify When Necessary: Resolving Ambiguity Through ... |
| 112 | D | [arXiv:2401.02009](https://arxiv.org/abs/2401.02009) | 2026-09-02 | 167 | 10 | SQ | KNOW_A | Zhang et al. — Self-Contrast: Better Reflection Through Inconsistent ... |
| 113 | D | [arXiv:2401.16745](https://arxiv.org/abs/2401.16745) | 2026-09-02 | 185 | 10 | SCENE | RELEASE | Kwan et al. — MT-Eval: A Multi-Turn Capabilities Evaluation Benchmark... |
| 114 | D | [arXiv:2402.03271](https://arxiv.org/abs/2402.03271) | 2026-09-02 | 196 | 6 | DEF | RELEASE | Hu et al. — Uncertainty of Thoughts: Uncertainty-Aware Planning Enhan... |
| 115 | D | [arXiv:2402.06170](https://arxiv.org/abs/2402.06170) | 2026-09-02 | 142 | 8 | DEF | CONTRIB | Wang et al. — Task Supportive and Personalized Human-Large Language M... |
| 116 | D | [arXiv:2402.11436](https://arxiv.org/abs/2402.11436) | 2026-09-02 | 153 | 8 | SQ | RELEASE | Xu et al. — Pride and Prejudice: LLM Amplifies Self-Bias in Self-Refi... |
| 117 | D | [arXiv:2402.12563](https://arxiv.org/abs/2402.12563) | 2026-09-02 | 180 | 9 | SQ | RELEASE | Li et al. — Confidence Matters: Revisiting Intrinsic Self-Correction ... |
| 118 | D | [arXiv:2402.14762](https://arxiv.org/abs/2402.14762) | 2026-09-02 | 174 | 9 | SQ | RELEASE | Bai et al. — MT-Bench-101: A Fine-Grained Benchmark for Evaluating La... |
| 119 | D | [arXiv:2404.04298](https://arxiv.org/abs/2404.04298) | 2026-09-02 | 108 | 6 | Q | KNOW_G | Jiang et al. — SELF-[IN]CORRECT: LLMs Struggle with Discriminating Se... |
| 120 | D | [arXiv:2404.12272](https://arxiv.org/abs/2404.12272) | 2026-09-02 | 219 | 9 | SCENE | CONTRIB | Shankar et al. — Who Validates the Validators? Aligning LLM-Assisted ... |
| 121 | D | [arXiv:2404.13076](https://arxiv.org/abs/2404.13076) | 2026-09-02 | 165 | 8 | SQ | CONTRIB | Panickssery et al. — LLM Evaluators Recognize and Favor Their Own Gen... |
| 122 | D | [arXiv:2404.17140](https://arxiv.org/abs/2404.17140) | 2026-09-02 | 148 | 6 | SQ | KNOW_A | Zhang et al. — Small Language Models Need Strong Verifiers to Self-Co... |
| 123 | D | [arXiv:2406.01297](https://arxiv.org/abs/2406.01297) | 2026-09-02 | 174 | 7 | DEF | KNOW_G | Kamoi et al. — When Can LLMs Actually Correct Their Own Mistakes? A C... |
| 124 | D | [arXiv:2406.01633](https://arxiv.org/abs/2406.01633) | 2026-09-02 | 178 | 8 | FIND | KNOW_A | Herlihy et al. — On Overcoming Miscalibrated Conversational Priors in... |
| 125 | D | [arXiv:2406.12624](https://arxiv.org/abs/2406.12624) | 2026-09-02 | 245 | 9 | SQ | KNOW_G | Thakur et al. — Judging the Judges: Evaluating Alignment and Vulnerab... |
| 126 | D | [arXiv:2409.12917](https://arxiv.org/abs/2409.12917) | 2026-09-02 | 254 | 8 | DEF | KNOW_A | Kumar et al. — Training Language Models to Self-Correct via Reinforce... |
| 127 | D | [arXiv:2502.00640](https://arxiv.org/abs/2502.00640) | 2026-09-02 | 163 | 8 | SQ | KNOW_A | Wu et al. — CollabLLM: From Passive Responders to Active Collaborators |
| 128 | D | [arXiv:2502.08177](https://arxiv.org/abs/2502.08177) | 2026-09-02 | 182 | 8 | SCENE | KNOW_G/PRACTICE | Fanous et al. — SycEval: Evaluating LLM Sycophancy |
| 129 | D | [arXiv:2505.06120](https://arxiv.org/abs/2505.06120) | 2026-09-02 | 186 | 8 | DEF | KNOW_G/NAMED | Laban et al. — LLMs Get Lost In Multi-Turn Conversation |
| 130 | D | [arXiv:2509.06770](https://arxiv.org/abs/2509.06770) | 2026-09-02 | 226 | 8 | SCENE | CONTRIB/PRACTICE | Javaji et al. — Another Turn, Better Output? A Turn-Wise Analysis of ... |
| 131 | D | [arXiv:2510.00777](https://arxiv.org/abs/2510.00777) | 2026-09-02 | 137 | 5 | PROB | KNOW_G/PRACTICE | Choi et al. — In-Place Feedback: Reliable Refinement for Multi-Turn E... |
| 132 | D | [arXiv:2603.27806](https://arxiv.org/abs/2603.27806) | 2026-09-02 | 221 | 9 | SCENE | KNOW_G/PRACTICE | Borchers et al. — Understanding Teacher Revisions of Large Language M... |
| 133 | D | [arXiv:2604.01029](https://arxiv.org/abs/2604.01029) | 2026-09-02 | 201 | 8 | SQ | KNOW_G/PRACTICE | Ning et al. — Revision or Re-Solving? Decomposing Second-Pass Gains i... |
| 134 | D | [arXiv:2606.15583](https://arxiv.org/abs/2606.15583) | 2026-09-02 | 171 | 10 | PROB | CONTRIB | Da Silva et al. — Process-Oriented Evaluation of AI-Assisted Scientif... |

## Catalogue A. Every opening sentence, verbatim, by opening type

### Q (n=3)
- `DogCat (EACL)` [prior topical set, 23 w] close=CONTRIB
  > When language models correctly parse "The cat that the dog chased meowed,” are they analyzing syntax or simply familiar with dogs chasing cats?
- `ReasoningTraces (ACL)` [prior topical set, 12 w] close=KNOW_G
  > Can we trust the reasoning traces that large reasoning models (LRMs) produce?
- `arXiv:2404.04298` [topical neighbours, 10 w] close=KNOW_G
  > Can LLMs consistently improve their previous outputs for better results?

### FIND (n=9)
- `2026.acl-long.1988` [ACL-2026 wave 1, 20 w] close=KNOW_G/CALL
  > This paper presents AutoRAN, the first framework to automate the hijacking of internal safety reasoning in large reasoning models (LRMs).
- `2026.acl-long.210` [ACL-2026 wave 1, 17 w] close=RELEASE
  > We present SemanticQA, an evaluation suite designed to assess language models (LMs) in semantic phrase processing tasks.
- `2026.eacl-long.128` [ACL-2026 wave 1, 21 w] close=CONTRIB
  > In this work, we focus on discovery of legal factors for a specific case type under consideration (e.g., vehicle insurance disputes).
- `2026.findings-acl.2070` [ACL-2026 wave 1, 13 w] close=KNOW_G
  > We study how well LLMs can determine whether two programs are functionally equivalent.
- `2026.acl-short.67` [ACL-2026 wave 2, 17 w] close=KNOW_G
  > We present T⋆, a simple TraceRL-based curriculum for progressive block-size scaling in masked diffusion language models (MDMs).
- `2511.16811` [arXiv cs.CL systematic, 21 w] close=CONTRIB
  > Building on the Extended Mind (EM) theory and radical enactivism, this article suggests an alternative to representation-based models of the mind.
- `arXiv:2211.03622` [topical neighbours, 28 w] close=CONTRIB/RELEASE
  > We conduct the first large-scale user study examining how users interact with an AI Code assistant to solve a variety of security related tasks across different programming languages.
- `arXiv:2305.17926` [topical neighbours, 35 w] close=RELEASE
  > In this paper, we uncover a systematic bias in the evaluation paradigm of adopting large language models (LLMs), e.g., GPT-4, as a referee to score and compare the quality of responses generated by candidate models.
- `arXiv:2406.01633` [topical neighbours, 14 w] close=KNOW_A
  > We explore the use of Large Language Model (LLM-based) chatbots to power recommender systems.

### PROB (n=23)
- `2026.acl-long.2099` [ACL-2026 wave 1, 24 w] close=KNOW_A
  > Retrieval-augmented generation needs generation to follow retrieved evidence across shifting domains and prompt layouts, but training a new stronger model per task is costly.
- `2026.acl-long.2210` [ACL-2026 wave 1, 17 w] close=RELEASE
  > Reinforcement Learning (RL) with sparse outcome rewards suffers from inefficient credit assignment in complex LLM reasoning tasks.
- `2026.acl-long.655` [ACL-2026 wave 1, 27 w] close=KNOW_A/PRACTICE
  > Selecting a single high-quality output from multiple stochastic generations remains a fundamental challenge for large language models (LLMs), particularly in open-ended tasks where no canonical answer exists.
- `2026.acl-short.57` [ACL-2026 wave 1, 21 w] close=KNOW_A
  > Figurative language recognition poses significant challenges in NLP, particularly when distinguishing between fine-grained rhetorical categories such as metaphor, metonymy, and simile.
- `2026.eacl-long.29` [ACL-2026 wave 1, 20 w] close=KNOW_G
  > Large language models (LLMs) often respond confidently to questions even when they lack the necessary information, leading to hallucinated answers.
- `2026.findings-acl.1529` [ACL-2026 wave 1, 28 w] close=RELEASE
  > While large language models (LLMs) have shown strong performance in math and logic reasoning, their ability to handle combinatorial optimization (CO)—searching high-dimensional solution spaces under hard constraints—remains underexplored.
- `2026.findings-acl.312` [ACL-2026 wave 1, 18 w] close=KNOW_A
  > Person Re-Identification (ReID) has long struggled with the semantic gap between low-level visual features and high-level identity concepts.
- `2026.findings-acl.583` [ACL-2026 wave 1, 27 w] close=NAMED
  > Large language models exhibit a critical vulnerability to distractor interference in retrieval-augmented contexts: they fail to prioritize relevant, factually correct documents over topically similar but misleading content.
- `2026.findings-acl.853` [ACL-2026 wave 1, 22 w] close=KNOW_A
  > Knowledge within large language models (LLMs) inevitably lags behind an evolving world, motivating knowledge editing methods that update facts without expensive retraining.
- `2026.acl-long.1118` [ACL-2026 wave 2, 16 w] close=RELEASE
  > Detecting machine-revised text that exhibits subtle lexical differences from the original human-generated text remains a challenge.
- `2026.acl-long.1674` [ACL-2026 wave 2, 16 w] close=KNOW_A
  > Simulating human-like Theory of Mind (ToM) has been a longstanding problem in natural language processing (NLP).
- `2026.acl-long.563` [ACL-2026 wave 2, 21 w] close=KNOW_A
  > Standard evaluators, such as reward models, compress diverse human judgments into a single scalar, conflating valid Subjective Preference with Cognitive Uncertainty.
- `2026.eacl-long.139` [ACL-2026 wave 2, 13 w] close=KNOW_G
  > Ensuring the safety of Large Language Models (LLMs) is a critical alignment challenge.
- `2026.findings-acl.1993` [ACL-2026 wave 2, 24 w] close=KNOW_A
  > While large language models show promise in mental healthcare, evaluating their therapeutic competence remains challenging due to the unstructured and longitudinal nature of counseling.
- `CommonToWhom (ACL)` [prior topical set, 14 w] close=CONTRIB
  > Existing cultural commonsense benchmarks treat nations as monolithic, assuming uniform practices within national boundaries.
- `DART (Findings)` [prior topical set, 30 w] close=KNOW_G
  > Large language models (LLMs) tuned for safety often avoid acknowledging demographic differences, even when such acknowledgment is factually correct (e.g., ancestry-based disease incidence) or contextually justified (e.g., religious hiring preferences).
- `SAGE (ACL)` [prior topical set, 26 w] close=KNOW_A
  > As Large Language Models (LLMs) become increasingly used for question-answering (QA), relying on static, pre-annotated references for evaluation poses significant challenges in cost, scalability, and completeness.
- `ZIP (*SEM)` [prior topical set, 36 w] close=CONTRIB/PRACTICE
  > While zero-shot instructional prompts like "Let’s think step-by-step” have revolutionized Large Language Model performance, we lack systematic understanding of why: which specific words drive their effectiveness, and how do these patterns vary across tasks and models?
- `arXiv:2303.16634` [topical neighbours, 16 w] close=RELEASE
  > The quality of texts generated by natural language generation (NLG) systems is hard to measure automatically.
- `arXiv:2303.17651` [topical neighbours, 17 w] close=KNOW_G
  > Like humans, large language models (LLMs) do not always generate the best output on their first try.
- `arXiv:2306.05685` [topical neighbours, 25 w] close=RELEASE
  > Evaluating large language model (LLM) based chat assistants is challenging due to their broad capabilities and the inadequacy of existing benchmarks in measuring human preferences.
- `arXiv:2510.00777` [topical neighbours, 25 w] close=KNOW_G/PRACTICE
  > LLM-generated drafts often contain subtle factual or logical errors, yet prior work shows that models struggle to reliably integrate multi-turn feedback aimed at fixing them.
- `arXiv:2606.15583` [topical neighbours, 7 w] close=CONTRIB
  > Bad writing hinders the publication of science.

### DEF (n=32)
- `2026.acl-long.321` [ACL-2026 wave 1, 19 w] close=KNOW_A
  > Empathetic dialogue requires not only recognizing a user’s emotional state but also making strategy-aware, context-sensitive decisions throughout response generation.
- `2026.acl-long.544` [ACL-2026 wave 1, 19 w] close=RELEASE
  > Scientific discovery evolution does not emerge in isolation but stems from the structural deepening and recombination of existing functionalities.
- `2026.acl-long.99` [ACL-2026 wave 1, 19 w] close=CONTRIB
  > Sparse Autoencoders (SAEs) are a prominent tool in mechanistic interpretability (MI) for decomposing neural network activations into interpretable features.
- `2026.acl-short.1` [ACL-2026 wave 1, 20 w] close=KNOW_A
  > Representation Fine-tuning (ReFT), a recently proposed parameter-efficient fine-tuning (PeFT) method, significantly improves parameter efficiency by modifying the representation space alone.
- `2026.acl-short.38` [ACL-2026 wave 1, 15 w] close=KNOW_A
  > Events exhibit rich semantic relations that are essential for understanding the unfolding of real-world processes.
- `2026.eacl-long.276` [ACL-2026 wave 1, 23 w] close=CONTRIB
  > Text anonymization is a critical task for enabling research and development in high-stakes domains containing private data, like medicine, law, and social services.
- `2026.eacl-long.374` [ACL-2026 wave 1, 16 w] close=KNOW_G
  > Prompt-based adversarial attacks are a key tool for assessing the robustness of large language models (LLMs).
- `2026.findings-acl.1259` [ACL-2026 wave 1, 18 w] close=KNOW_A
  > Character description generation is an important capability for narrative-focused applications such as summarization, story analysis, and character-driven simulations.
- `2026.findings-acl.447` [ACL-2026 wave 1, 24 w] close=KNOW_G
  > Long-horizon agents operate over extended sequences of reasoning and actions, but this inevitably accumulates context noise, resulting in excessive computational cost and information overload.
- `2026.acl-long.1951` [ACL-2026 wave 2, 15 w] close=RELEASE
  > Tool-augmented Language Models (TaLMs) can invoke external tools to solve problems beyond their parametric capacity.
- `2026.acl-long.285` [ACL-2026 wave 2, 42 w] close=RELEASE
  > Speculative decoding accelerates large language model (LLM) inference through a draft-and-verify paradigm, yet existing methods face three key limitations: reliance on fixed draft templates that ignore device-specific verification costs, lack of mechanisms to assess draft token quality, and suboptimal tree expansion strategies.
- `2026.acl-long.840` [ACL-2026 wave 2, 25 w] close=KNOW_G
  > Low-Rank Adaptation (LoRA) enables parameter-efficient fine-tuning of Large Language Models (LLMs), and recent Mixture-of-Experts (MoE) extensions further enhance flexibility by dynamically combining multiple LoRA experts.
- `2026.acl-short.30` [ACL-2026 wave 2, 16 w] close=RELEASE
  > Membership inference attacks (MIAs) are a canonical way to assess a machine learning model’s privacy properties.
- `2026.findings-acl.1272` [ACL-2026 wave 2, 9 w] close=KNOW_G
  > Understanding climate change requires reasoning over complex causal networks.
- `2026.findings-acl.1632` [ACL-2026 wave 2, 14 w] close=KNOW_G/PRACTICE
  > Tokenization plays a pivotal role in NLP and is fundamental to training language models.
- `2026.findings-acl.551` [ACL-2026 wave 2, 29 w] close=CONTRIB
  > Theory of Mind (ToM)—an understanding of the mental states of others—is a key aspect of human social intelligence, yet, chatbots and LLM-based social agents do not typically integrate it.
- `2503.03340` [arXiv cs.CL systematic, 24 w] close=KNOW_A
  > Theory-of-Mind (ToM), the ability to infer others' perceptions and mental states, is fundamental to human interaction but remains challenging for Large Language Models (LLMs).
- `2509.17641` [arXiv cs.CL systematic, 23 w] close=RELEASE
  > Even without directly hearing sounds, humans can effortlessly reason about auditory properties, such as pitch, loudness, or sound-source associations, drawing on auditory commonsense.
- `2603.03203` [arXiv cs.CL systematic, 19 w] close=RELEASE
  > CDD, or Contamination Detection via output Distribution, identifies data contamination by measuring the peakedness of a model's sampled outputs.
- `2605.15040` [arXiv cs.CL systematic, 25 w] close=KNOW_G
  > Agentic modeling aims to transform LLMs into autonomous agents capable of solving complex tasks through planning, reasoning, tool use, and multi-turn interaction with external environments.
- `2607.23597` [arXiv cs.CL systematic, 14 w] close=RELEASE
  > Generative linguistic steganography conceals secret bits within the sampling randomness of large language models.
- `CGM (Findings)` [prior topical set, 18 w] close=RELEASE
  > Continuous glucose monitors (CGMs) used in diabetes care collect rich personal health data that could improve day-to-day self-management.
- `arXiv:2211.00053` [topical neighbours, 21 w] close=KNOW_A
  > Sequence generation applications require satisfying semantic constraints, such as ensuring that programs are correct, using certain keywords, or avoiding undesirable content.
- `arXiv:2308.03958` [topical neighbours, 36 w] close=RELEASE
  > Sycophancy is an undesirable behavior where models tailor their responses to follow a human user's view even when that view is not objectively correct (e.g., adapting liberal views once a user reveals that they are liberal).
- `arXiv:2309.11495` [topical neighbours, 17 w] close=KNOW_A
  > Generation of plausible yet incorrect factual information, termed hallucination, is an unsolved issue in large language models.
- `arXiv:2310.01783` [topical neighbours, 8 w] close=KNOW_G
  > Expert feedback lays the foundation of rigorous research.
- `arXiv:2311.09469` [topical neighbours, 22 w] close=CONTRIB
  > Resolving ambiguities through interaction is a hallmark of natural language, and modeling this behavior is a core challenge in crafting AI assistants.
- `arXiv:2402.03271` [topical neighbours, 14 w] close=RELEASE
  > In the face of uncertainty, the ability to seek information is of fundamental importance.
- `arXiv:2402.06170` [topical neighbours, 19 w] close=CONTRIB
  > Large language model (LLM) applications, such as ChatGPT, are a powerful tool for online information-seeking (IS) and problem-solving tasks.
- `arXiv:2406.01297` [topical neighbours, 20 w] close=KNOW_G
  > Self-correction is an approach to improving responses from large language models (LLMs) by refining the responses using LLMs during inference.
- `arXiv:2409.12917` [topical neighbours, 24 w] close=KNOW_A
  > Self-correction is a highly desirable capability of large language models (LLMs), yet it has consistently been found to be largely ineffective in modern LLMs.
- `arXiv:2505.06120` [topical neighbours, 7 w] close=KNOW_G/NAMED
  > Large Language Models (LLMs) are conversational interfaces.

### SCENE (n=19)
- `2026.acl-long.1432` [ACL-2026 wave 1, 10 w] close=KNOW_A
  > Large Language Model (LLM) agents are reshaping the industrial landscape.
- `2026.acl-long.1655` [ACL-2026 wave 1, 30 w] close=CONTRIB
  > Large Language Models (LLMs) are increasingly adopted as conversational assistants in genomics, where they are mainly used to reason over biological knowledge, annotations, and analysis outputs through natural language interfaces.
- `2026.acl-long.766` [ACL-2026 wave 1, 12 w] close=KNOW_G
  > Large language models (LLMs) are increasingly deployed in culturally sensitive real-world tasks.
- `2026.eacl-long.177` [ACL-2026 wave 1, 28 w] close=KNOW_G
  > Large language models (LLMs) increasingly produce natural language explanations, yet these explanations often lack faithfulness, and they do not reliably reflect the evidence the model uses to decide.
- `2026.eacl-long.79` [ACL-2026 wave 1, 27 w] close=KNOW_A
  > With the advent of large language models (LLMs), it has become common practice for users to draft text and utilize LLMs to enhance its quality through paraphrasing.
- `2026.findings-acl.1123` [ACL-2026 wave 1, 18 w] close=KNOW_A
  > Large language models (LLMs) are increasingly deployed as intelligent agents that reason, plan, and interact with their environments.
- `2026.findings-acl.1799` [ACL-2026 wave 1, 11 w] close=CONTRIB
  > Large Language Models (LLMs) are increasingly adopted in macroeconomic agent-based modeling(ABM).
- `2026.findings-acl.718` [ACL-2026 wave 1, 21 w] close=KNOW_A
  > The advent of autonomous agents is transforming interactions with Graphical User Interfaces (GUIs) by employing natural language as a powerful intermediary.
- `2026.acl-long.1396` [ACL-2026 wave 2, 12 w] close=KNOW_A
  > Tabular data is widely used in fields such as finance and healthcare.
- `2026.eacl-long.238` [ACL-2026 wave 2, 20 w] close=CALL
  > Natural language processing (NLP) now shapes many aspects of our world, yet its potential for positive social impact is underexplored.
- `2601.19923` [arXiv cs.CL systematic, 44 w] close=KNOW_G
  > As Large Language Models (LLMs) evolve into the core of Web-based autonomous agents and complex Web Information Systems, their ability to faithfully translate natural language into rigorous structured formats has become paramount, as this capability is critical for Web API invocation and data exchange.
- `SCOPE (ICML)` [prior topical set, 21 w] close=KNOW_A
  > Large language models (LLMs) are increasingly used as scalable judges in pairwise evaluation, but they remain prone to miscalibration and biases.
- `arXiv:2212.09746` [topical neighbours, 17 w] close=KNOW_G
  > Many real-world applications of language models (LMs), such as writing assistance and code autocomplete, involve human-LM interaction.
- `arXiv:2303.11366` [topical neighbours, 20 w] close=CONTRIB
  > Large language models (LLMs) have been increasingly used to interact with external environments (e.g., games, compilers, APIs) as goal-driven agents.
- `arXiv:2401.16745` [topical neighbours, 16 w] close=RELEASE
  > Large language models (LLMs) are increasingly relied upon for complex multi-turn conversations across diverse real-world applications.
- `arXiv:2404.12272` [topical neighbours, 28 w] close=CONTRIB
  > Due to the cumbersome nature of human evaluation and limitations of code-based evaluation, Large Language Models (LLMs) are increasingly being used to assist humans in evaluating LLM outputs.
- `arXiv:2502.08177` [topical neighbours, 30 w] close=KNOW_G/PRACTICE
  > Large language models (LLMs) are increasingly applied in educational, clinical, and professional settings, but their tendency for sycophancy -- prioritizing user agreement over independent reasoning -- poses risks to reliability.
- `arXiv:2509.06770` [topical neighbours, 26 w] close=CONTRIB/PRACTICE
  > Large language models (LLMs) are now used in multi-turn workflows, but we still lack a clear way to measure when iteration helps and when it hurts.
- `arXiv:2603.27806` [topical neighbours, 24 w] close=KNOW_G/PRACTICE
  > Large language models (LLMs) increasingly generate formative feedback for students, yet little is known about how teachers revise this feedback before it reaches learners.

### SQ (n=48)
- `2026.acl-long.1099` [ACL-2026 wave 1, 34 w] close=KNOW_A
  > Reliable verifiable data has become a key driver of capability gains in modern language models, enabling stable reinforcement learning with verifiable rewards and effective distillation that transfers competence across math, coding, and agentic tasks.
- `2026.acl-long.1210` [ACL-2026 wave 1, 24 w] close=KNOW_A
  > Token-pruning has emerged as a primary focus in large language models (LLMs) to enhance model efficiency while preserving accuracy, especially for large sequence lengths.
- `2026.acl-long.1321` [ACL-2026 wave 1, 18 w] close=KNOW_A
  > The evolution paradigm of Large Language Models (LLMs) is shifting from scaling training compute to scaling inference-time compute.
- `2026.acl-long.1543` [ACL-2026 wave 1, 11 w] close=KNOW_A
  > LLM-powered multi-agent systems (MAS) have demonstrated strong performance on complex tasks.
- `2026.acl-long.1766` [ACL-2026 wave 1, 22 w] close=KNOW_A
  > Recent Large Reasoning Models (LRMs) excel at complex reasoning tasks but often suffer from overthinking, generating overly long and redundant reasoning trajectories.
- `2026.acl-long.1877` [ACL-2026 wave 1, 23 w] close=KNOW_G
  > Post-training hybridization of large language models (LLMs) often replaces quadratic self-attention with sliding-window attention (SWA) to reduce KV cache usage and improve latency.
- `2026.acl-long.432` [ACL-2026 wave 1, 20 w] close=RELEASE
  > Recent advancements in Large Reasoning Models (LRMs) have showcased strong performance across various reasoning tasks by leveraging System-2 thinking capabilities.
- `2026.acl-long.877` [ACL-2026 wave 1, 20 w] close=KNOW_A
  > Previous research on multi-party dialogue generation has predominantly leveraged structural information inherent in dialogues to directly inform the generation process.
- `2026.acl-long.988` [ACL-2026 wave 1, 22 w] close=KNOW_A/PRACTICE
  > Deep Research systems based on web agents have shown strong potential in solving complex information-seeking tasks, yet their search efficiency remains underexplored.
- `2026.acl-short.20` [ACL-2026 wave 1, 19 w] close=KNOW_A
  > Recent large language models (LLMs) perform strongly on mathematical benchmarks yet often misapply lemmas, importing conclusions without validating assumptions.
- `2026.eacl-long.226` [ACL-2026 wave 1, 16 w] close=CALL
  > Much recent work has shown how cross-linguistic variation is constrained by competing pressures from efficient communication.
- `2026.eacl-long.325` [ACL-2026 wave 1, 19 w] close=RELEASE
  > Large language models (LLMs) are increasingly capable of generating functional source code, raising concerns about authorship, accountability, and security.
- `2026.findings-acl.1394` [ACL-2026 wave 1, 16 w] close=KNOW_A
  > Text-to-image (T2I) generative models have achieved remarkable visual fidelity, yet remain vulnerable to generating unsafe content.
- `2026.findings-acl.177` [ACL-2026 wave 1, 17 w] close=KNOW_A
  > Large Language Models (LLMs) have shown great potential in Knowledge Base Question Answering (KBQA) via semantic parsing.
- `2026.findings-acl.1935` [ACL-2026 wave 1, 30 w] close=CONTRIB
  > Large language models (LLMs) are highly capable of answering questions, but they are often unaware of their own knowledge boundary, i.e., knowing what they know and what they don’t know.
- `2026.findings-acl.42` [ACL-2026 wave 1, 16 w] close=KNOW_A
  > Large language models (LLMs) have demonstrated significant capabilities in solving mathematical problems expressed in natural language.
- `2026.findings-acl.988` [ACL-2026 wave 1, 18 w] close=RELEASE
  > Deep Research agents powered by Large Language Models (LLMs) have exhibited extraordinary potential in automated paper writing tasks.
- `2026.acl-long.7` [ACL-2026 wave 2, 24 w] close=KNOW_G
  > Large language models (LLMs) can reliably distinguish grammatical from ungrammatical sentences, but how grammatical knowledge is represented within the model remains an open question.
- `2026.eacl-long.336` [ACL-2026 wave 2, 41 w] close=RELEASE
  > Large language models (LLMs) have demonstrated impressive performance on reasoning-intensive tasks, but enhancing their reasoning abilities typically relies on either reinforcement learning (RL) with verifiable signals or supervised fine-tuning (SFT) with high-quality long chain-of-thought (CoT) demonstrations, both of which are expensive.
- `2026.eacl-long.41` [ACL-2026 wave 2, 25 w] close=KNOW_A
  > Generative methods have recently gained traction in biological and chemical named entity recognition for their ability to overcome tagging limitations and better capture entity-rich contexts.
- `2026.findings-acl.190` [ACL-2026 wave 2, 32 w] close=CONTRIB/FUTURE
  > Large language models can perform well on many isolated tasks, yet they continue to struggle on multi-turn, long-horizon agentic problems that require skills such as planning, state tracking, and long context processing.
- `2026.findings-acl.911` [ACL-2026 wave 2, 15 w] close=KNOW_G/CALL
  > Multimodal Large Language Models (MLLMs) have increasingly supported omni-modal processing across text, vision, and speech.
- `2501.00353` [arXiv cs.CL systematic, 19 w] close=RELEASE
  > Retrieval-Augmented Generation (RAG) has emerged as a key paradigm for enhancing large language models (LLMs) by incorporating external knowledge.
- `2505.12625` [arXiv cs.CL systematic, 14 w] close=KNOW_G
  > DeepSeek recently released R1, a high-performing large language model (LLM) optimized for reasoning tasks.
- `2507.10972` [arXiv cs.CL systematic, 35 w] close=KNOW_A
  > Large language models, with their strong reasoning ability and rich knowledge, have brought revolution to many tasks of AI, but their impact on sign language generation remains limited due to its complexity and unique rules.
- `MemoryDial (Findings)` [prior topical set, 14 w] close=CONTRIB
  > Memorization in language models is widely studied but remains difficult to isolate and control.
- `arXiv:2212.09251` [topical neighbours, 21 w] close=KNOW_G
  > As language models (LMs) scale, they develop many novel behaviors, good and bad, exacerbating the need to evaluate how they behave.
- `arXiv:2302.06590` [topical neighbours, 9 w] close=KNOW_G/PRACTICE
  > Generative AI tools hold promise to increase human productivity.
- `arXiv:2304.05128` [topical neighbours, 11 w] close=KNOW_A
  > Large language models (LLMs) have achieved impressive performance on code generation.
- `arXiv:2305.11738` [topical neighbours, 10 w] close=KNOW_G
  > Recent developments in large language models (LLMs) have been impressive.
- `arXiv:2306.09896` [topical neighbours, 17 w] close=KNOW_G
  > Large language models have shown remarkable aptitude in code generation, but still struggle to perform complex tasks.
- `arXiv:2308.03188` [topical neighbours, 15 w] close=FUTURE
  > Large language models (LLMs) have demonstrated remarkable performance across a wide array of NLP tasks.
- `arXiv:2309.12570` [topical neighbours, 26 w] close=FUTURE
  > The development of large language models (LLMs) capable of following instructions and engaging in conversational interactions sparked increased interest in their utilization across various support tools.
- `arXiv:2310.01798` [topical neighbours, 19 w] close=FUTURE
  > Large Language Models (LLMs) have emerged as a groundbreaking technology with their unparalleled text generation capabilities across various applications.
- `arXiv:2310.07641` [topical neighbours, 31 w] close=FUTURE
  > As research in large language models (LLMs) continues to accelerate, LLM-based evaluation has emerged as a scalable and cost-effective alternative to human evaluations for comparing the ever increasing list of models.
- `arXiv:2310.08118` [topical neighbours, 27 w] close=KNOW_G
  > There have been widespread claims about Large Language Models (LLMs) being able to successfully verify or self-critique their candidate solutions in reasoning problems in an iterative mode.
- `arXiv:2310.12397` [topical neighbours, 16 w] close=KNOW_G
  > There has been considerable divergence of opinion on the reasoning abilities of Large Language Models (LLMs).
- `arXiv:2310.13548` [topical neighbours, 9 w] close=KNOW_G/NAMED
  > Human feedback is commonly utilized to finetune AI assistants.
- `arXiv:2311.08516` [topical neighbours, 48 w] close=RELEASE
  > While self-correction has shown promise in improving LLM outputs in terms of style and quality (e.g. Chen et al., 2023b; Madaan et al., 2023), recent attempts to self-correct logical or reasoning errors often cause correct answers to become incorrect, resulting in worse performances overall (Huang et al., 2023).
- `arXiv:2401.02009` [topical neighbours, 12 w] close=KNOW_A
  > The reflection capacity of Large Language Model (LLM) has garnered extensive attention.
- `arXiv:2402.11436` [topical neighbours, 20 w] close=RELEASE
  > Recent studies show that large language models (LLMs) improve their performance through self-feedback on certain tasks while degrade on others.
- `arXiv:2402.12563` [topical neighbours, 17 w] close=RELEASE
  > The recent success of Large Language Models (LLMs) has catalyzed an increasing interest in their self-correction capabilities.
- `arXiv:2402.14762` [topical neighbours, 12 w] close=RELEASE
  > The advent of Large Language Models (LLMs) has drastically enhanced dialogue systems.
- `arXiv:2404.13076` [topical neighbours, 23 w] close=CONTRIB
  > Self-evaluation using large language models (LLMs) has proven valuable not only in benchmarking but also methods like reward modeling, constitutional AI, and self-refinement.
- `arXiv:2404.17140` [topical neighbours, 29 w] close=KNOW_A
  > Self-correction has emerged as a promising solution to boost the reasoning performance of large language models (LLMs), where LLMs refine their solutions using self-generated critiques that pinpoint the errors.
- `arXiv:2406.12624` [topical neighbours, 28 w] close=KNOW_G
  > Offering a promising solution to the scalability challenges associated with human evaluation, the LLM-as-a-judge paradigm is rapidly gaining traction as an approach to evaluating large language models (LLMs).
- `arXiv:2502.00640` [topical neighbours, 17 w] close=KNOW_A
  > Large Language Models are typically trained with next-turn rewards, limiting their ability to optimize for long-term interaction.
- `arXiv:2604.01029` [topical neighbours, 28 w] close=KNOW_G/PRACTICE
  > Multi-LLM revision pipelines, in which a second model reviews and improves a draft produced by a first, are widely assumed to derive their gains from genuine error correction.

## Catalogue B. Every closing sentence, verbatim, by closing type

### KNOW_G (n=38)
- `2026.acl-long.1877` [ACL-2026 wave 1] open=SQ
  > Analysis of the selected heads reveals substantial turnover for BOSCH across different SWA ratios, underscoring the importance of performing head-level selection for each target ratio rather than relying on fixed locality rankings.
- `2026.acl-long.1988` [ACL-2026 wave 1] open=FIND +CALL
  > This work reveals that the transparency of the reasoning process itself creates a critical and exploitable attack surface, highlighting the urgent need for new defenses that protect models’ reasoning traces rather than merely their final outputs.
- `2026.acl-long.766` [ACL-2026 wave 1] open=SCENE
  > Our results demonstrate the necessity of task adaptation and modular culture management for effective cultural alignment.
- `2026.eacl-long.177` [ACL-2026 wave 1] open=SCENE
  > These findings highlight that intervention-based evaluation, coupled with iterative optimization, provides a principled route toward faithful and reliable LLM explanations.
- `2026.eacl-long.29` [ACL-2026 wave 1] open=PROB
  > Last, causal interventions show that adding or ablating the directions effectively controls the abstention behavior of the model.
- `2026.eacl-long.374` [ACL-2026 wave 1] open=DEF
  > These results highlight the importance of structural awareness in evaluating and improving the adversarial robustness of LLMs.
- `2026.findings-acl.2070` [ACL-2026 wave 1] open=FIND
  > Our analysis presents deep insights into the working of LLMs for the task of code-equivalence, and points to the fact that they may still be far from what could be termed as a semantic understanding of the underlying code.
- `2026.findings-acl.447` [ACL-2026 wave 1] open=DEF
  > Analysis further reveals that Self-Sum learns to summarize sparsely at meaningful moments and preserves task-relevant information, highlighting the importance of jointly learning when and what to summarize for robust long-horizon agent behavior.
- `2026.acl-long.7` [ACL-2026 wave 2] open=SQ
  > Taken together, these findings reveal that syntactic agreement—a critical marker of syntactic dependencies—constitutes a meaningful category within LLMs’ representational spaces.
- `2026.acl-long.840` [ACL-2026 wave 2] open=DEF
  > These results highlight structured expert communication as a principled and effective enhancement for MoE-based parameter-efficient adaptation.
- `2026.acl-short.67` [ACL-2026 wave 2] open=FIND
  > Our schedule analysis suggests that the learned policy does not simply revert to a strictly left-to-right order; instead, it retains block-size-specific non-monotone updates while improving accuracy.
- `2026.eacl-long.139` [ACL-2026 wave 2] open=PROB
  > Our results show that: (i) the separation between safe and unsafe concepts emerges from a single layer direction in the activation space, (ii) monitoring internal representations provides a significantly more robust safeguarding mechanism compared to traditional evaluative or generative guardrail paradigms.
- `2026.findings-acl.1272` [ACL-2026 wave 2] open=DEF
  > Finally, large language model benchmarking on correlation inference and causal chain reasoning highlights the latter as a key challenge.
- `2026.findings-acl.1632` [ACL-2026 wave 2] open=DEF +PRACTICE
  > Our findings highlight the importance of linguistically informed design choices in multilingual tokenization and offer practical guidance for building effective tokenizers for low-resource and morphologically complex languages.
- `2026.findings-acl.911` [ACL-2026 wave 2] open=SQ +CALL
  > Notably, models struggle when processing the speech modality, underscoring the need for balanced, multi-hop evaluation of omni-modal intelligence.
- `2505.12625` [arXiv cs.CL systematic] open=SQ
  > Our findings reveal possible additional censorship integration likely shaped by design choices during training or alignment, raising concerns about transparency, bias, and governance in language model deployment.
- `2601.19923` [arXiv cs.CL systematic] open=SCENE
  > Furthermore, our findings show that deep recursive nesting poses a consistent challenge for Web agents across varying parameter scales.
- `2605.15040` [arXiv cs.CL systematic] open=DEF
  > Collectively, these results demonstrate that a lightweight, open, harness-agnostic environment layer enables reusable agentic data, training recipes, and evaluation protocols across domains.
- `DART (Findings)` [prior topical set] open=PROB
  > Our results demonstrate that accuracy and safety need not conflict when explicit detection and repair mechanisms are in place.
- `ReasoningTraces (ACL)` [prior topical set] open=Q
  > Our findings reveal a gap between the reasoning LRMs follow and the reasoning they report, raising concern that aligned-appearing explanations may not be equivalent to genuine alignment.
- `arXiv:2212.09251` [topical neighbours] open=SQ
  > Overall, LM-written evaluations are high-quality and let us quickly discover many novel LM behaviors.
- `arXiv:2212.09746` [topical neighbours] open=SCENE
  > In particular, we highlight three cases where the results from non-interactive and interactive metrics diverge and underscore the importance of human-LM interaction for LM evaluation.
- `arXiv:2302.06590` [topical neighbours] open=SQ +PRACTICE
  > Observed heterogenous effects show promise for AI pair programmers to help people transition into software development careers.
- `arXiv:2303.17651` [topical neighbours] open=PROB
  > Our work demonstrates that even state-of-the-art LLMs like GPT-4 can be further improved at test time using our simple, standalone approach.
- `arXiv:2305.11738` [topical neighbours] open=SQ
  > Meanwhile, our research highlights the crucial importance of external feedback in promoting the ongoing self-improvement of LLMs.
- `arXiv:2306.09896` [topical neighbours] open=SQ
  > Similarly, a small-scale study in which we provide GPT-4 with feedback from human participants suggests that even for the strongest models, self-repair still lags far behind what can be achieved with human-level debugging.
- `arXiv:2310.01783` [topical neighbours] open=DEF
  > While our findings show that LLM-generated feedback can help researchers, we also identify several limitations.
- `arXiv:2310.08118` [topical neighbours] open=SQ
  > Collectively, our results cast doubt on the effectiveness of LLMs in a self-critiquing, iterative framework for planning tasks.
- `arXiv:2310.12397` [topical neighbours] open=SQ
  > Our results thus call into question claims about the self-critiquing capabilities of state of the art LLMs.
- `arXiv:2310.13548` [topical neighbours] open=SQ +NAMED
  > Overall, our results indicate that sycophancy is a general behavior of state-of-the-art AI assistants, likely driven in part by human preference judgments favoring sycophantic responses.
- `arXiv:2404.04298` [topical neighbours] open=Q
  > This finding challenges the notion that LLMs may be able to enhance their performance only through their own judgment.
- `arXiv:2406.01297` [topical neighbours] open=DEF
  > Our critical survey based on the newly categorized research questions shows that (1) no prior work demonstrates successful self-correction with feedback from prompted LLMs, except for studies in tasks that are exceptionally suited for self-correction, (2) self-correction works well in tasks that can use reliable external feedback, and (3) large-scale fine-tuning enables self-correction.
- `arXiv:2406.12624` [topical neighbours] open=SQ
  > Lastly, our research rediscovers the importance of using alignment metrics beyond simple percent alignment, showing that judges with high percent agreement can still assign vastly different scores.
- `arXiv:2502.08177` [topical neighbours] open=SCENE +PRACTICE
  > These findings emphasize the risks and opportunities of deploying LLMs in structured and dynamic domains, offering insights into prompt programming and model optimization for safer AI applications.
- `arXiv:2505.06120` [topical neighbours] open=DEF +NAMED
  > In simpler terms, we discover that when LLMs take a wrong turn in a conversation, they get lost and do not recover.
- `arXiv:2510.00777` [topical neighbours] open=PROB +PRACTICE
  > These results suggest that editing errors directly is a more effective paradigm for expert-LLM collaboration.
- `arXiv:2603.27806` [topical neighbours] open=SCENE +PRACTICE
  > Together, these findings characterize how teachers engage with AI-generated feedback in practice and highlight opportunities to design feedback systems that better align with teacher priorities while reducing unnecessary editing effort.
- `arXiv:2604.01029` [topical neighbours] open=SQ +PRACTICE
  > Ultimately, our findings demonstrate that the utility of multi-LLM revision is dynamically bottlenecked by task structure and draft quality, necessitating more targeted pipeline designs rather than blanket revision strategies.

### KNOW_A (n=41)
- `2026.acl-long.1099` [ACL-2026 wave 1] open=SQ
  > The results show that training with our synthesized data yields significant improvements on both the LiveCodeBench and AgentBench-OS tasks, highlighting the robust generalization of our framework.
- `2026.acl-long.1210` [ACL-2026 wave 1] open=SQ
  > EQUIP matches the model accuracy of baseline pruning methods while delivering superior performance.
- `2026.acl-long.1321` [ACL-2026 wave 1] open=SQ
  > Empirical results across diverse mathematical reasoning and code generation benchmarks demonstrate that CURE not only maintains competitive single-turn performance but, more importantly, unlocks effective inference-time scaling, enabling the model to significantly boost accuracy through iterative self-improvement.
- `2026.acl-long.1432` [ACL-2026 wave 1] open=SCENE
  > In experiments across diverse domains, ReCreate consistently outperforms human-designed agents and existing automated agent generation methods, even when starting from minimal seed scaffolds.
- `2026.acl-long.1543` [ACL-2026 wave 1] open=SQ
  > Moreover, NeuralFSM exhibits strong inherent robustness, which is further enhanced by the protection layer, resulting in only a 1.82% performance drop under attack.
- `2026.acl-long.1766` [ACL-2026 wave 1] open=SQ
  > The resultant models exhibit a nascent ability for difficulty-aware reasoning, effectively mitigating behaviors like excessive reflection and looping, thereby paving the way for more cognitively efficient LRMs.
- `2026.acl-long.2099` [ACL-2026 wave 1] open=PROB
  > Across public benchmarks and private settings with no in-domain labels, GRAD improves accuracy with favorable latency, offering strong trade-offs versus scaling while reliably activating helpful objectives and suppressing harmful ones, adaptively to tasks.
- `2026.acl-long.321` [ACL-2026 wave 1] open=DEF
  > Extensive experiments demonstrate that STRIDE-ED generalizes across diverse open-source LLMs and consistently outperforms existing methods on both automatic metrics and human evaluations.
- `2026.acl-long.655` [ACL-2026 wave 1] open=PROB +PRACTICE
  > Across open-ended tasks—including text summarization, code generation, and mathematical reasoning—our approaches consistently outperform standard single- and multi-path baselines, providing a computationally efficient, drop-in solution for robust open-ended text generation.
- `2026.acl-long.877` [ACL-2026 wave 1] open=SQ
  > Comprehensive experiments conducted on four multi-party dialogue datasets substantiate the effectiveness of DRCR.
- `2026.acl-long.988` [ACL-2026 wave 1] open=SQ +PRACTICE
  > Experiments demonstrate that WebClipper compresses tool-call rounds under excellent performance, providing practical insight into balancing effectiveness and efficiency in web agent design.
- `2026.acl-short.1` [ACL-2026 wave 1] open=DEF
  > Furthermore, our analysis of its training speed and memory overhead confirms its greater ease of use and efficiency.
- `2026.acl-short.20` [ACL-2026 wave 1] open=SQ
  > Results show consistent in-domain gains over both a vanilla model and a single-label RL baseline, larger improvements on applicability-breaking perturbations, and parity or modest gains on end-to-end tasks; ablations indicate that the two-section outputs and section-aware reinforcement are both necessary for robustness.
- `2026.acl-short.38` [ACL-2026 wave 1] open=DEF
  > Furthermore, leveraging these interpretable features to train a lightweight classifier significantly improves event relation extraction, achieving F1 gains of up to 24% for causal relations.
- `2026.acl-short.57` [ACL-2026 wave 1] open=PROB
  > Experiments across both unified and single-class benchmarks demonstrate that FL-MSCL achieves competitive performance compared to State-of-the-Art (SOTA) methods, indicating consistent advantages in cross-category generalization and category-specific detection.
- `2026.eacl-long.79` [ACL-2026 wave 1] open=SCENE
  > Furthermore, SearchLLM also helps the detectors prevent paraphrasing attacks.
- `2026.findings-acl.1123` [ACL-2026 wave 1] open=SCENE
  > Experiments on LoCoMo and NarrativeQA demonstrate that CompassMem consistently improves both retrieval and reasoning performance across multiple backbone models.
- `2026.findings-acl.1259` [ACL-2026 wave 1] open=DEF
  > Experiments on two datasets (BookWorm and CroSS) show that QA-guided reasoning improves faithfulness, informativeness, and grounding over strong long-context baselines.
- `2026.findings-acl.1394` [ACL-2026 wave 1] open=SQ
  > Across nudity and multi-category bench- marks and recent adversarial prompt attacks, SafePatch achieves robust unsafe suppression (7% unsafe on I2P) while preserving image quality and semantic alignment.
- `2026.findings-acl.177` [ACL-2026 wave 1] open=SQ
  > Extensive experiments on GrailQA, WebQSP, and GraphQuestions demonstrate that SELF-KBQA achieves state-of-the-art performance.
- `2026.findings-acl.312` [ACL-2026 wave 1] open=PROB
  > Extensive experiments on ReID datasets demonstrate that our method significantly outperforms state-of-the-art approaches, particularly in complex occlusion scenarios.
- `2026.findings-acl.42` [ACL-2026 wave 1] open=SQ
  > Through extensive experiments, we also show that our framework can help mitigate English-centric entity bias and improve robustness when native entities are introduced across various languages.
- `2026.findings-acl.718` [ACL-2026 wave 1] open=SCENE
  > Comprehensive experiments demonstrate LPO’s superior performance, achieving SOTA results across both offline benchmarks and real-world online evaluations.
- `2026.findings-acl.853` [ACL-2026 wave 1] open=PROB
  > Experiments on MQuAKE-2002 and MQuAKE-hard demonstrate that CARE effectively mitigates error propagation, achieving a new state-of-the-art.
- `2026.acl-long.1396` [ACL-2026 wave 2] open=SCENE
  > Extensive experiments demonstrate that LogGER consistently outperforms both tree-based models and state-of-the-art LLM methods on a variety of tabular prediction tasks, achieving superior accuracy and interpretability.
- `2026.acl-long.1674` [ACL-2026 wave 2] open=PROB
  > Experimental results show that PICTURE outperforms existing prompting methods by an average of 7.3% on false-belief tasks.
- `2026.acl-long.563` [ACL-2026 wave 2] open=PROB
  > Furthermore, in downstream Reinforcement Learning, PRISM effectively mitigates reward hacking, yielding policies that are more robust and resilient to distribution shifts.
- `2026.eacl-long.41` [ACL-2026 wave 2] open=SQ
  > Benefiting from these designs, our method outperforms the baselines by 1.80 and 2.73 F1-score on the CHEMDNER and microbial ecology dataset Florilege, highlighting its effectiveness in biological and chemical named entity recognition.
- `2026.findings-acl.1993` [ACL-2026 wave 2] open=PROB
  > Extensive experiments validate the effectiveness of PsychePass and its strong consistency with human expert judgments.
- `2503.03340` [arXiv cs.CL systematic] open=DEF
  > Experimental results on ToMi, HiToM, and FANToM benchmarks show that EnigmaToM significantly improves ToM reasoning across LLMs of varying sizes, particularly excelling in high-order reasoning scenarios.
- `2507.10972` [arXiv cs.CL systematic] open=SQ
  > Experimental results on How2Sign and Phoenix14T datasets demonstrate that our approach effectively leverages both the sign language knowledge and reasoning capabilities of LLM to align the different distribution and grammatical rules between sign and spoken language.
- `SAGE (ACL)` [prior topical set] open=PROB
  > Experimental results on multiple free-form QA benchmarks show that SAGE achieves substantial to perfect agreement with human evaluations.
- `SCOPE (ICML)` [prior topical set] open=SCENE
  > Compared to vanilla baselines, \textsc{Scope} accepts up to $2.4\times$ more judgments under the same risk constraint, demonstrating that BPE enables reliable and high-coverage LLM-based evaluation.
- `arXiv:2211.00053` [topical neighbours] open=DEF
  > We show that Self-Correction improves upon the base generator in three diverse generation tasks - mathematical program synthesis, lexically-constrained generation, and toxicity control - even when the corrector is much smaller than the base generator.
- `arXiv:2304.05128` [topical neighbours] open=SQ
  > Meanwhile, by leveraging feedback messages and reusing failed predictions, Self-Debugging notably improves sample efficiency, and can match or outperform baseline models that generate more than 10x candidate programs.
- `arXiv:2309.11495` [topical neighbours] open=DEF
  > In experiments, we show CoVe decreases hallucinations across a variety of tasks, from list-based questions from Wikidata, closed book MultiSpanQA and longform text generation.
- `arXiv:2401.02009` [topical neighbours] open=SQ
  > Experiments conducted on a series of reasoning and translation tasks with different LLMs serve to underscore the effectiveness and generality of our strategy.
- `arXiv:2404.17140` [topical neighbours] open=SQ
  > Our experimental results show improved self-correction abilities of two models on five datasets spanning math and commonsense reasoning, with notable performance gains when paired with a strong GPT-4-based verifier, though limitations are identified when using a weak self-verifier for determining when to correct.
- `arXiv:2406.01633` [topical neighbours] open=FIND
  > Finally, we show empirically that our lightweight learning approach effectively uses logged conversation data to re-calibrate the response strategies of LLM-based chatbots for recommendation tasks.
- `arXiv:2409.12917` [topical neighbours] open=DEF
  > With Gemini 1.0 Pro and 1.5 Flash models, we find that SCoRe achieves state-of-the-art self-correction performance, improving the base models' self-correction by 15.6% and 9.1% respectively on MATH and HumanEval.
- `arXiv:2502.00640` [topical neighbours] open=SQ
  > Finally, we conduct a large user study with 201 judges, where CollabLLM increases user satisfaction by 17.6% and reduces user spent time by 10.4%.

### NAMED (n=1)
- `2026.findings-acl.583` [ACL-2026 wave 1] open=PROB
  > Successful correction through sparse modifications reveals distractor interference as a localized, systematically addressable phenomenon, opening directions toward universal distractor robustness in LLMs.

### CONTRIB (n=21)
- `2026.acl-long.1655` [ACL-2026 wave 1] open=SCENE
  > GenomeQA establishes a diagnostic benchmark for studying and improving the use of general-purpose LLMs on raw genomic sequences.
- `2026.acl-long.99` [ACL-2026 wave 1] open=DEF
  > Our contributions include: (i) theoretical grounding for strong consistency in the idealized setting of TopK SAEs; (ii) synthetic validation using a model organism, which verifies PW-MCC as a reliable proxy for ground-truth recovery; and (iii) empirical analysis on LLM activations, where PW-MCC correlates with the similarity of automatically generated natural-language feature explanations.
- `2026.eacl-long.128` [ACL-2026 wave 1] open=FIND
  > We construct and evaluate the discovered list of AJFs on two different types of cases (auto-insurance and life insurance) and show their utility in a dispute resolution application.
- `2026.eacl-long.276` [ACL-2026 wave 1] open=DEF
  > Overall, our work explores the under-studied task of what to replace redacted content with and contributes grounded evaluations capturing utility, facilitating future work.
- `2026.findings-acl.1799` [ACL-2026 wave 1] open=SCENE
  > Overall, this work contributes to the development of reliable and grounded economic simulations.
- `2026.findings-acl.1935` [ACL-2026 wave 1] open=SQ
  > In addition, we also propose a novel method for harnessing the pretraining data to build a more honest LLM.
- `2026.findings-acl.190` [ACL-2026 wave 2] open=SQ +FUTURE
  > Our work sheds light on the challenges of multi-turn agentic environments to guide the future efforts in the development of AI agents and language models.
- `2026.findings-acl.551` [ACL-2026 wave 2] open=DEF
  > Our results suggest a step forward in integrating ToM for building socially intelligent LLM agents.
- `2511.16811` [arXiv cs.CL systematic] open=FIND
  > This non-representational account reframes translation as skillful participation in sociocultural practice, where meaning is co-created in real time through embodied interaction with texts, tools, and contexts.
- `CommonToWhom (ACL)` [prior topical set] open=PROB
  > Beyond India, our methodology provides a generalizable framework for evaluating cultural commonsense in any culturally heterogeneous nation, from question design grounded in anthropological taxonomy, to regional data collection, to bias measurement.
- `DogCat (EACL)` [prior topical set] open=Q
  > CenterBench provides the first framework to identify when models shift from structural analysis to pattern matching.
- `MemoryDial (Findings)` [prior topical set] open=SQ
  > Memory Dial provides a controlled experimental framework for studying how memorization behavior emerges and interacts with generalization in language models.
- `ZIP (*SEM)` [prior topical set] open=PROB +PRACTICE
  > Our findings advance prompt science, providing both practical guidance for prompt engineering and theoretical understanding of how instructional language shapes model behavior.
- `arXiv:2211.03622` [topical neighbours] open=FIND +RELEASE
  > Finally, in order to better inform the design of future AI-based Code assistants, we provide an in-depth analysis of participants' language and interaction behavior, as well as release our user interface as an instrument to conduct similar studies in the future.
- `arXiv:2303.11366` [topical neighbours] open=SCENE
  > We also conduct ablation and analysis studies using different feedback signals, feedback incorporation methods, and agent types, and provide insights into how they affect performance.
- `arXiv:2311.09469` [topical neighbours] open=DEF
  > Together, our work lays foundation for studying clarifying interactions with LMs.
- `arXiv:2402.06170` [topical neighbours] open=DEF
  > It offers insights into evaluating human-LLM interactions and emphasizes potential challenges for under served users.
- `arXiv:2404.12272` [topical neighbours] open=SCENE
  > We present our interface and implementation details, a comparison of our algorithm with a baseline approach, and implications for the design of future LLM evaluation assistants.
- `arXiv:2404.13076` [topical neighbours] open=SQ
  > We discuss how self-recognition can interfere with unbiased evaluations and AI safety more generally.
- `arXiv:2509.06770` [topical neighbours] open=SCENE +PRACTICE
  > Together, the framework and metrics make iteration measurable and comparable across models, and signal when to steer, stop, or switch strategies.
- `arXiv:2606.15583` [topical neighbours] open=PROB
  > Our large-scale process-oriented evaluation highlights the perks and pitfalls of both human and LM editing processes as machine-generated texts emerge in scientific communication.

### RELEASE (n=27)
- `2026.acl-long.210` [ACL-2026 wave 1] open=FIND
  > The evaluation harness and data of SemanticQA are available at https://github.com/jacklanda/SemanticQA.
- `2026.acl-long.2210` [ACL-2026 wave 1] open=PROB
  > The code will be available at: https://github.com/JIA-Lab-research/TRAC.
- `2026.acl-long.432` [ACL-2026 wave 1] open=SQ
  > Code is available at https://anonymous.4open.science/r/PAM-RM-02DF.
- `2026.acl-long.544` [ACL-2026 wave 1] open=DEF
  > The code is available at https://github.com/xiyii-star/EvoNarrator.
- `2026.eacl-long.325` [ACL-2026 wave 1] open=SQ
  > The data and the code are available at https://huggingface.co/AICD-bench.
- `2026.findings-acl.1529` [ACL-2026 wave 1] open=PROB
  > The benchmark dataset and code for data generation and evaluation are publicly available.
- `2026.findings-acl.988` [ACL-2026 wave 1] open=SQ
  > Dataset and codes will be released.
- `2026.acl-long.1118` [ACL-2026 wave 2] open=PROB
  > The code is available at https://github.com/hangtze/LAMCL.
- `2026.acl-long.1951` [ACL-2026 wave 2] open=DEF
  > Code and data will be released upon publication.
- `2026.acl-long.285` [ACL-2026 wave 2] open=DEF
  > Our code and benchmark are publicly available.
- `2026.acl-short.30` [ACL-2026 wave 2] open=DEF
  > To facilitate further privacy research, we open-source a modular library for designing and implementing attacks in this setting: https://github.com/safr-ai-lab/pandora_llm.
- `2026.eacl-long.336` [ACL-2026 wave 2] open=SQ
  > Code is at https://github.com/W2SR-ARR/Code.
- `2501.00353` [arXiv cs.CL systematic] open=SQ
  > RAG-Instruct is publicly available at this https URL.
- `2509.17641` [arXiv cs.CL systematic] open=DEF
  > The project page is available at this https URL.
- `2603.03203` [arXiv cs.CL systematic] open=DEF
  > Our code is available at this https URL
- `2607.23597` [arXiv cs.CL systematic] open=DEF
  > GitHub repository for this work is this https URL.
- `CGM (Findings)` [prior topical set] open=DEF
  > We release our code and benchmark to support future work on trustworthy health agents.
- `arXiv:2303.16634` [topical neighbours] open=PROB
  > The code is at this https URL
- `arXiv:2305.17926` [topical neighbours] open=FIND
  > We release our code and human annotation at this URL to facilitate future research.
- `arXiv:2306.05685` [topical neighbours] open=PROB
  > The MT-bench questions, 3K expert votes, and 30K conversations with human preferences are publicly available at this https URL.
- `arXiv:2308.03958` [topical neighbours] open=DEF
  > Code for generating synthetic data for intervention can be found at this https URL.
- `arXiv:2311.08516` [topical neighbours] open=SQ
  > We release our dataset of LLM-generated logical mistakes, BIG-Bench Mistake, to enable further research into locating LLM reasoning mistakes.
- `arXiv:2401.16745` [topical neighbours] open=SCENE
  > MT-Eval is released publicly to encourage future research towards more robust conversational models.
- `arXiv:2402.03271` [topical neighbours] open=DEF
  > Our code has been released here
- `arXiv:2402.11436` [topical neighbours] open=SQ
  > The code and data are released at this https URL.
- `arXiv:2402.12563` [topical neighbours] open=SQ
  > The code is available at this https URL.
- `arXiv:2402.14762` [topical neighbours] open=SQ
  > The data and code are available at this https URL.

### FUTURE (n=4)
- `arXiv:2308.03188` [topical neighbours] open=SQ
  > We also summarize the major applications of this strategy and conclude by discussing future directions and challenges.
- `arXiv:2309.12570` [topical neighbours] open=SQ
  > Our findings from analyzing both the interactions and the survey responses highlight future research directions in creative writing assistance using LLMs.
- `arXiv:2310.01798` [topical neighbours] open=SQ
  > Drawing from these insights, we offer suggestions for future research and practical applications in this field.
- `arXiv:2310.07641` [topical neighbours] open=SQ
  > With LLMBar, we hope to offer more insight into LLM evaluators and foster future research in developing better instruction-following models.

### CALL (n=2)
- `2026.eacl-long.226` [ACL-2026 wave 1] open=SQ
  > Our approach highlights the need to incorporate regularity across sets of forms in studies attempting tomeasure efficiency in language.
- `2026.eacl-long.238` [ACL-2026 wave 2] open=SCENE
  > Guided by our review, we outline opportunities for responsible and equitable NLP and conclude with a call for cross-disciplinary partnerships and human-centered approaches to ensure that future NLP technologies advance the public good.

---

## Provenance

Retrieval dates: 2026-09-06 for strata A, A2 and B; 2026-09-02 for strata C and D, whose
text was already held verbatim in `acl2026_abstracts.json` and `neighbor_abstracts.md` and
was not refetched for this file. Sampling seeds: 20260906 (stratum A, drawn earlier),
20260906007 (strata A2 and B). Abstract text for strata A and C comes from
`paper/reference/acl2026_abstracts.json`; for stratum D from
`paper/reference/neighbor_abstracts.md`; for strata A2 and B it was fetched for this file.
The quantitative-numeral counts in the density section are the hand-verified counts already
published in `paper/reference/acl2026_density.md` for the 47 wave-1 abstracts, joined to the
opening codes here; they were not recomputed.

Sentence segmentation, word counts, question detection, the imperative scan and every count
in the tables above were produced by script over the stored text. Opening and closing codes
are hand-assigned, one per abstract, and each coded sentence is quoted verbatim in the two
catalogues so any code can be checked against the sentence it was assigned to.
