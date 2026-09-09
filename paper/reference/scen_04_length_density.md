# Abstract length against quantitative density in 2026 ACL-venue abstracts

Compiled 2026-09-06. Question: is short-and-dense achievable at these venues, or is density bought
with length? The draft going to ARR in October 2026 is about 200 words and reports one result
figure. Adding a name for the apparatus and a second or third figure pushes it longer, so the
question is what the observed frontier permits at a given length.

## Corpus, sampling, and bounds

Source: ACL Anthology paper landing pages, one HTTP request per paper. Abstract text taken from the
`div` with class `card-body acl-abstract`, parsed by walking `div` nesting to the matching close,
markup stripped. **All 67 pages retrieved 2026-09-06.**

The corpus is two systematic draws over the same four volumes.

| Batch | n | Draw | Seed | Strides |
|---|---|---|---|---|
| A | 47 | 20 `acl-long`, 16 `findings-acl`, 8 `eacl-long`, 4 `acl-short` | 20260906 | 111 / 135 / 49 / 18.5 |
| B | 20 | 8 `acl-long`, 7 `findings-acl`, 3 `eacl-long`, 2 `acl-short` | 20260907 | 277.8 / 309.0 / 131.3 / 37.0 |

Batch A is the draw already held in `acl2026_abstracts.json`; 48 IDs were drawn and 47 yielded an
abstract (`2026.findings-acl.1664` has no abstract block and was excluded, not replaced). Batch B is
a second interleaved systematic pass over the same ordered volume lists with an independent random
start, excluding any ID already in batch A and any ID already known to lack an abstract; where a
draw index landed on an excluded ID the next unused index in volume order was taken. All 20 batch-B
IDs yielded an abstract. **Total n = 67.**

Volume sizes as listed on the Anthology on 2026-09-06: `2026.acl-long` 2,222 papers excluding front
matter, `2026.findings-acl` 2,163, `2026.eacl-long` 394, `2026.acl-short` 74. `2026.naacl-long`,
`2026.emnlp-main` and `2026.starsem-1` return HTTP 404 and no paper from them was fetched.

**Bounds on the sample.** The draw is unconditional on topic and was not filtered toward empirical
studies of model behaviour. It therefore reflects what these volumes are made of, which is mostly
method papers. It says nothing about EMNLP, NAACL, TACL, or any 2025-or-earlier volume, and nothing
about abstracts of papers that were rejected. Batch B is slightly denser than batch A (median 0.67
against 0.00 numerals per 100 words, 6 of 20 with no digit against 31 of 47); the two draws are from
the same volumes by the same procedure, so this is sampling variation at n=20, not a second
population, but it means the pooled figures sit a little above batch A alone.

**How things were counted.** Word counts, sentence counts, numeral counts and categories, quartiles,
correlations, confidence intervals, p-values, beat detections and word-spend tallies are produced
mechanically by `scripts/acl2026_abstract_density/05_length_density.py`, which reuses the measurement
functions of `03_measure.py` unchanged. No figure below was counted by eye. Three things are
hand-adjudicated and are marked HAND wherever they appear: the enumerator override, the
artifact-naming flag, and the reading of what the long-and-sparse abstracts spend their words on.

A numeral counts as **quantitative** only if it is not part of an identifier. Model and dataset name
digits, four-digit years and enumeration markers are counted separately and excluded from the
density measure. Density throughout is quantitative numerals per 100 words.

### HAND: enumerator correction, and the sweep that followed it

`03_measure.py` tags a digit run as an enumeration marker only when it is parenthesised on both
sides, so the half-parenthesised list form "two critical challenges: 1) ... and 2) ..." was scored as
two statistics. On finding this, every quantitative-tagged digit run in all 67 abstracts was printed
with 45 characters of context on each side and read. The form appears in exactly one abstract,
`2026.findings-acl.900`, and its two enumerators are now demoted, taking that abstract from 3
quantitative numerals to 1 and from 1.89 to 0.63 per 100 words. The sweep found no other
misclassification: model-size figures ("7B/14B/32B models", "1.7B to 30B parameters", "fewer than 10M
parameters") are counted as quantitative, which is the choice already made and documented in
`acl2026_density.md`, and every remaining tagged run is a genuine figure. `2026.findings-acl.900` is
in batch B, so no figure in `acl2026_density.md` changes.

The correction matters for the question at hand: before it, that abstract was the third member of the
short-and-dense set, and it is not one.

## The correlation: density is bought with length

| Relationship | n | Pearson r | 95% CI | p | Spearman rho | p |
|---|---|---|---|---|---|---|
| Words vs numerals per 100 words | 67 | **0.457** | 0.243 to 0.628 | 0.0001 | 0.414 | 0.0005 |
| Words vs raw quantitative numeral count | 67 | 0.493 | 0.287 to 0.656 | 0.00002 | 0.449 | 0.00014 |
| Words vs has-any-numeral (point-biserial) | 67 | 0.317 | 0.083 to 0.518 | 0.0089 | 0.331 | 0.0063 |
| Words vs density, abstracts with at least one numeral | 30 | 0.636 | 0.358 to 0.811 | 0.00016 | 0.554 | 0.0015 |
| Words vs number of distinct coined names | 67 | 0.019 | -0.222 to 0.258 | 0.876 | 0.112 | 0.366 |

**The relationship is positive, moderate, and not null.** This is the answer to the question as
posed: density is bought with length in this corpus. And the measure being correlated is already a
rate, not a count, so this is not the arithmetic truism that a longer text has room for more figures.
Longer abstracts are denser *per word*: the median density is 0.00 among abstracts of 160 words or
fewer and 1.03 among abstracts of 180 words or more.

Three qualifications on the size of it.

First, 37 of 67 abstracts contain no quantitative digit at all, so about a third of the correlation
is the length difference between the abstracts that quantify anything and the ones that do not:
median 171.5 words for the 30 that report at least one figure, 156 for the 37 that report none.

Second, the relationship survives conditioning on that. Among the 30 abstracts with at least one
figure, r = 0.636 (n = 30, p = 0.0002). So it is not only that quantifying abstracts are longer; among
abstracts that quantify, the denser ones are longer still.

Third, the slope is small in absolute terms. Regressing words on the quantitative numeral count gives
**8.1 words per additional figure** (intercept 154.7 words). Regressing density on words gives 0.01
numerals per 100 words per additional word, which over the 73-to-229-word range of the corpus is the
full 0-to-2.9 spread.

The one signal that is uncorrelated with length is naming. The count of distinct coined names in an
abstract is unrelated to its length (r = 0.019, p = 0.88, n = 67).

## Short and dense: two abstracts, quoted in full

Definition as specified: below the corpus median length (161 words) and above the 75th percentile of
density (1.025 numerals per 100 words). **Two of 67 abstracts qualify.** The four-way split is:

| | Sparse (density at or below 1.025) | Dense (above 1.025) |
|---|---|---|
| **Short (under 161 words)** | 30 | **2** |
| **Long (161 words or more)** | 20 | 15 |

The cell is not empty, so short-and-dense is achievable, but it is the rarest of the four and it is
rare by a wide margin: 2 of 32 short abstracts reach the upper density quartile, against 15 of 35
long ones.

### `2026.acl-long.1543`, 157 words, 3 quantitative numerals, 1.91 per 100 words

NeuralFSM: Adaptive Multi-Agent Coordination via Learning Finite-State Execution Policy.
https://aclanthology.org/2026.acl-long.1543/ (retrieved 2026-09-06)

> LLM-powered multi-agent systems (MAS) have demonstrated strong performance on complex tasks.
> However, most existing approaches still rely on hand-crafted communication protocols or
> automatically designed communication topologies, which generalize poorly across tasks. We introduce
> NeuralFSM, a state-driven framework that formulates multi-agent problem solving as a finite-state
> execution process. NeuralFSM learns both the state transition distribution and inter-agent
> communication weights from interaction traces using a Temporal Coordination Controller. Rather than
> prioritizing explicit structure generation, the proposed framework uses task context to modulate
> transition and routing decisions, enabling flexible coordination without manual protocol design. To
> improve robustness against noisy or adversarial agents, we incorporate graph regularization during
> training and apply trust-aware message attenuation at runtime. Experiments on diverse benchmarks
> show that NeuralFSM consistently outperforms prior baselines by an average margin of 6.74%–19.39%,
> while substantially reducing token consumption. Moreover, NeuralFSM exhibits strong inherent
> robustness, which is further enhanced by the protection layer, resulting in only a 1.82%
> performance drop under attack.

Eight sentences, 19.6 words each. All three figures are percentages and all three are in the last two
sentences. It fits three figures into 157 words by doing two things: it never names a dataset, a
metric, or a model ("diverse benchmarks", "prior baselines", "token consumption"), and it uses a
range, 6.74%–19.39%, where a list of per-benchmark figures would have been. The range is two numerals
in six words.

### `2026.findings-acl.988`, 159 words, 2 quantitative numerals, 1.26 per 100 words

MASS: Deep Research for Social Sciences with Memory-Augmented Social Simulation.
https://aclanthology.org/2026.findings-acl.988/ (retrieved 2026-09-06)

> Deep Research agents powered by Large Language Models (LLMs) have exhibited extraordinary potential
> in automated paper writing tasks. However, existing systems rely heavily on literature retrieval and
> synthesis through internet and local knowledge bases, often resulting research lacking insight and
> creativity in social science. To address this issue, we propose "Memory-Augmented Social Simulation
> (MASS)”, an innovative paradigm that leverages highly realistic and research-oriented social
> simulations to the creativity and empirical founding of LLMs-generated research. Specifically, MASS
> integrates three core components—dynamic goal-path planning with multi-level social norm restraint
> to guide the simulation, a multi-disciplinary behavior dataset for agent memory cold-start, and a
> structured forgetting mechanism inspired by the Ebbinghaus curve. Together, these ensure simulation
> authenticity and provide a robust empirical foundation for generating innovative scholarly papers.
> Experimental results demonstrate the effectiveness of our method, showing a 6.81% improvement in
> generation overall quality over foundation LLMs and 17.19% gain in Insight over strong baselines.
> Dataset and codes will be released.

Typography, spacing and punctuation in both quotations are reproduced as published, including the
unmatched quotation mark and the em-dash list in `2026.findings-acl.988`.

Seven sentences, 22.7 words each. Both figures are in one sentence, both are result percentages, and
both name what they are measured on in the same clause. The abstract runs a single long method
sentence (the three components, 47 words) instead of three sentences, and names no dataset, metric or
model.

### The attainable frontier at each length

Densest abstract observed at or below each length, over the whole corpus:

| Length ceiling | Densest abstract at or below it | Density |
|---|---|---|
| 73 words | `2026.acl-short.57` | 0.00 |
| 113 words | `2026.findings-acl.583` | 0.88 |
| 157 words | `2026.acl-long.1543` | 1.91 |
| 171 words | `2026.eacl-long.325` | 2.34 |
| 184 words | `2026.findings-acl.1209` | 2.72 |
| 205 words | `2026.acl-long.1210` | 2.93 |

Below the 161-word median, **10 of 32 abstracts report at least one figure, 2 report two or more, and
6 report at least one result percentage**. So one figure below the median is ordinary and two is
unusual but done.

Every short abstract with at least one figure, ordered by density:

| ID | Words | Figures | Per 100w | Result percentages |
|---|---|---|---|---|
| `2026.acl-long.1543` | 157 | 3 | 1.91 | 3 |
| `2026.findings-acl.988` | 159 | 2 | 1.26 | 2 |
| `2026.findings-acl.583` | 113 | 1 | 0.88 | 1 |
| `2026.acl-long.1369` | 147 | 1 | 0.68 | 0 |
| `2026.acl-long.1647` | 151 | 1 | 0.66 | 1 |
| `2026.acl-long.2203` | 153 | 1 | 0.65 | 0 |
| `2026.acl-long.1988` | 154 | 1 | 0.65 | 1 |
| `2026.findings-acl.1394` | 157 | 1 | 0.64 | 1 |
| `2026.acl-long.99` | 158 | 1 | 0.63 | 0 |
| `2026.findings-acl.900` | 159 | 1 | 0.63 | 0 |

## Long and sparse: 20 abstracts, 14 of them with no digit at all

At or above the median length (161 words) and at or below the 75th percentile of density: 20
abstracts, the "long, sparse" cell of the table above. The stricter set, strictly longer than 161
words and containing no quantitative digit whatever, has 14 members, and those are the ones read
below. They range from 162 to 229 words. The six in the first set but not the second are
`2026.eacl-long.79`, which is exactly 161 words with no digit, and five abstracts that report one or two
figures at a density at or below 1.025 (`2026.acl-long.988`, `2026.findings-acl.591`,
`2026.acl-long.432`, `2026.findings-acl.1529`, `2026.acl-long.536`).

Pooled word-spend across the 14, by sentence beat (script-assigned: each sentence goes to one beat by
a fixed priority order, and "other" is a sentence matching no detector, usually a pure contribution
restatement):

| Beat | Words | Share of the 2,562 words |
|---|---|---|
| Method mechanism | 555 | 22% |
| Unquantified result claim | 446 | 17% |
| Gap or limitation | 391 | 15% |
| Unclassified (mostly contribution restatement) | 366 | 14% |
| Evaluation setup | 255 | 10% |
| Implication or closing claim | 244 | 10% |
| Problem framing | 202 | 8% |
| Ablation or further analysis | 95 | 4% |
| Release statement | 8 | 0% |

The same tally over the 17 densest abstracts, for contrast, puts 28% into method mechanism, 13% into
quantified results, and only 4% into problem framing. Dense abstracts do not spend less on method.
They spend less on scene-setting and convert the result sentence from a claim into a figure.

### HAND: what each of the 14 is spending its words on

Classification is by reading. Each abstract gets one primary and, where material, one secondary.

| ID | Words | Primary spend | Secondary | The tell |
|---|---|---|---|---|
| `2026.eacl-long.276` | 162 | Extended setup | Closing restatement | Two motivation sentences of 63 words, then a 40-word final sentence that restates the contribution already stated |
| `2026.acl-long.655` | 163 | Method detail | Extended setup | Three sentences on the similarity graph, spectral clustering and a decoding variant; one unquantified result |
| `2026.findings-acl.312` | 163 | Method detail | Extended setup | A 62-word sentence naming Reasoner, Hybrid Retriever and Corrector; result is "significantly outperforms state-of-the-art approaches" |
| `2026.findings-acl.853` | 166 | Method detail | Extended setup | Four setup sentences before the method; result is "achieving a new state-of-the-art" |
| `2026.acl-long.2210` | 169 | Method detail | Release | Three calibration dimensions plus a GRPO integration, then an unquantified result and a repository URL |
| `2026.findings-acl.447` | 173 | Method detail | Implications | A two-stage recipe with (i) and (ii), then a 45-word analysis-plus-implication closer |
| `2026.eacl-long.29` | 180 | Multiple findings | none | Four consecutive result sentences, none of them quantified: main result, generalization, extension beyond extractive QA, causal interventions |
| `2026.findings-acl.282` | 187 | Multiple findings | Implications | Four findings sentences, then two closing sentences ("provides the first systematic evidence", "pave the way") |
| `2026.acl-long.1099` | 189 | Extended setup | Method detail | Three gap sentences, then a single 66-word method sentence |
| `2026.eacl-long.226` | 192 | Extended setup | Implications | Literature positioning with two inline citations, then a closing sentence on what the field should incorporate |
| `2026.findings-acl.1123` | 193 | Extended setup | Method detail | Five problem-and-gap sentences, roughly 100 words, before the method appears |
| `2026.findings-acl.1799` | 193 | Method detail | Implications, hedging | Method and validation detail, hedged findings ("a potential data leakage", "results indicate"), then "Overall, this work contributes to..." |
| `2026.acl-long.1432` | 203 | Extended setup | Method detail | Four setup sentences including a rhetorical question, then three lettered components |
| `2026.findings-acl.2070` | 229 | Multiple findings | Hedging | The longest abstract in the corpus: problem, a sentence justifying the problem, construction, two findings, a remedy, generality claims, ablations, and a hedged close ("may still be far from what could be termed as a semantic understanding") |

Counts: method detail is the primary spend in 7 of 14, extended setup in 4, multiple unquantified
findings in 3. Implications or a closing restatement is a material secondary in 6. Hedging is a
material spend in 2. Not one of the 14 spends its extra words on quantification, which is what makes
them long and sparse rather than long and dense.

## The word cost of one additional figure

Median length by number of quantitative numerals:

| Figures | n | Median words | Mean | p25 | p75 | Cost of this step, at the median |
|---|---|---|---|---|---|---|
| 0 | 37 | 156 | 155.9 | 141 | 169 | (baseline) |
| 1 | 12 | 157.5 | 157.1 | 152.5 | 165.2 | **+1.5 words** |
| 2 | 7 | 177 | 177.4 | 167.0 | 186.0 | **+19.5 words** |
| 3 or more | 11 | 193 | 189.6 | 177.5 | 203.5 | **+16 words** |

The first figure is free. The second costs about 20 words at the median and the third about 16 more.
The regression of words on figure count, which averages over the whole range rather than reading step
by step, gives 8.1 words per figure.

The same cut on result percentages rather than all figures:

| Result percentages | n | Median words | Mean |
|---|---|---|---|
| 0 | 54 | 161.5 | 162.5 |
| 1 | 5 | 154 | 147.6 |
| 2 or more | 8 | 188.5 | 183.5 |

One result percentage goes with abstracts that are 7.5 words *shorter* than the median at zero, on
n=5. Two or more go with abstracts 34.5 words longer than that. The regression slope is 6.0 words per
result percentage.

What this means for a draft at 200 words with one figure: the first figure has already been bought at
no cost, and a second is the one that has a price. Twenty words is the price at the median, and the
corpus contains one 159-word abstract (`2026.findings-acl.988`) that reports two result percentages
and one 157-word abstract (`2026.acl-long.1543`) that reports three, so the price is an average rather
than a floor. Both of those buy the room the same way, by naming no dataset, no metric and no model.

## The word cost of naming an artifact: it is negative

The `03_measure.py` naming flag was hand-adjudicated across all 67 abstracts, because it has two
failure modes. Hyphenated CamelCase names are not matched by its acronym pattern (false negatives:
`2026.acl-short.57` names FL-MSCL, `2026.findings-acl.447` names Self-Sum). And an abstract
containing only borrowed acronyms, meaning third-party benchmark names, model names or field terms,
plus an introducing verb, is scored as naming an artifact when it names nothing of its own (false
positives: `2026.eacl-long.54`, `2026.acl-long.1099`, and `2026.acl-long.536`, which is titled
ReProbe but never uses the string ReProbe in its abstract). The adjudication is recorded in
`scripts/acl2026_abstract_density/handcode_artifact_naming_67.json`.

Hand-verified: **57 of 67 abstracts (85%) coin and use a name for what they introduce**, the same
share as in batch A alone.

| | n | Median words | Mean words | Mean density |
|---|---|---|---|---|
| Names an artifact | 57 | **160** | 161.7 | 0.66 |
| Names none | 10 | **176** | 176.5 | 0.44 |

**Naming costs nothing. Abstracts that name their artifact are 16 words shorter at the median than
abstracts that do not.** The mechanism is visible in the ten that name none: they have to refer to
their contribution by description every time it comes up, so "an evolutionary, task-agnostic,
strategy-guided, executably-checkable data synthesis framework" (`2026.acl-long.1099`) and "an
adaptive, multi-paradigm, neuro-symbolic inference framework" (`2026.eacl-long.54`) occupy a clause
where a two-syllable name would occupy a word. A coined name is a compression device, not an
expense. The count of distinct names in an abstract is likewise uncorrelated with its length
(r = 0.019, p = 0.88).

The other naming behaviours do have a price, though a small one, and only one of them is measurable:

| Naming behaviour | n named | Median words, named | n unnamed | Median words, unnamed |
|---|---|---|---|---|
| Names at least one evaluation metric | 28 | 161.0 | 39 | 162 |
| Names at least one evaluation dataset | 13 | 161 | 54 | 161.5 |
| Names at least one model | 10 | **175.0** | 57 | **161** |

Naming a metric or a dataset is free at the median. Naming a model by vendor name goes with abstracts
14 words longer, on n=10, and is rare besides.

## Abstracts of 150 to 180 words: what fits

36 of 67 abstracts fall in this band, which straddles the 161-word venue median. Median 159 words,
median 7 sentences, 23.8 words per sentence, median density 0.00, 75th percentile 0.65, maximum 2.34
(`2026.eacl-long.325`, 171 words). **20 of the 36 contain no quantitative digit.** The median abstract
in the band contains 6 of the 10 beats measured; the distribution runs 4 (2 abstracts), 5 (6), 6 (13),
7 (9), 8 (5), 9 (1).

### Beat inventory, 150 to 180 words, n = 36

| Beat | Present | Share | Absent |
|---|---|---|---|
| Gap or limitation statement | 35 | 97% | 1 |
| Method mechanism | 35 | 97% | 1 |
| Result claim (of any kind) | 34 | 94% | 2 |
| Named artifact (HAND) | 30 | 83% | 6 |
| Evaluation setup named or counted | 28 | 78% | 8 |
| Problem framing before the gap | 21 | 58% | 15 |
| Implication or closing claim | 14 | 39% | 22 |
| Ablation or further analysis | 11 | 31% | 25 |
| Release or availability statement | 11 | 31% | 25 |
| Quantified result | 9 | 25% | 27 |

Beat definitions are regex detectors over the abstract text, listed in the `BEATS` table of
`05_length_density.py`; "named artifact" is the hand-adjudicated flag and "quantified result" means at
least one numeral classified as a result percentage, a metric score or a ratio multiplier.

**What a 150-to-180-word abstract in this venue contains.** Six beats. A gap statement, a method
mechanism, a coined name used through the abstract, an evaluation setup, and a result claim are
present in three-quarters or more of them. That is the floor and it consumes the whole budget.

**What it omits.** Three-quarters omit a quantified result. Two-thirds omit an ablation and two-thirds
omit a release statement. Six in ten omit an implication or closing claim. Four in ten open on the gap
with no preceding problem-framing sentence at all.

Two abstracts in the band reach 8 or 9 beats: `2026.acl-long.544` (177 words, 11 sentences, 9 beats,
1.13 per 100 words) and `2026.acl-long.432` (176 words, 8 sentences, 8 beats, 0.57). Both sit at the
top of the band and `2026.acl-long.544` does it by running 16.1 words per sentence against the band
average of 23.8. Fitting a ninth beat into 177 words is done by shortening sentences, not by cutting
another beat.

## Which beats are dropped first

Share of abstracts in each length band containing each beat. Ordered by survival in the shortest band,
so the beats at the top are the ones abandoned first as an abstract gets shorter.

| Beat | 140 words or fewer (n=10) | 141–160 (n=22) | 161–180 (n=16) | Over 180 (n=19) |
|---|---|---|---|---|
| Quantified result | **10%** | 32% | 19% | 42% |
| Ablation or further analysis | **10%** | 27% | 31% | 26% |
| Release statement | **10%** | 23% | 38% | 21% |
| Problem framing before the gap | **20%** | 50% | 69% | 74% |
| Implication or closing claim | **40%** | 41% | 38% | 53% |
| Evaluation setup | 70% | 77% | 81% | 63% |
| Gap or limitation | 80% | 100% | 94% | 95% |
| Result claim | 90% | 95% | 94% | 95% |
| Method mechanism | 100% | 100% | 94% | 100% |
| Named artifact (HAND) | 100% | 86% | 81% | 79% |

Median words per band: 121, 154, 167.5, 193. Median sentences: 6, 6, 8, 8. Median density: 0.00, 0.00,
0.28, 1.03.

**The drop order, shortest first:** quantified result, ablation and release together, problem framing,
implication, then evaluation setup. Nothing below that line is ever dropped. Gap, result claim, method
mechanism and the coined name are present in 80 to 100 percent of even the shortest abstracts, and
naming is the one beat whose prevalence goes *up* as abstracts get shorter, from 79 percent above 180
words to 100 percent at 140 or fewer. The shortest abstracts in this corpus are not short because they
dropped the name. They are short because they dropped the figures, the ablation, and the opening
scene-setting sentence.

The count of beats present rises only slightly with length: median 5 in the shortest band and 6 in each
of the other three (r = 0.296 for words against beat count, p = 0.015, n = 67). Long abstracts are not
mostly covering more beats. They are covering the same six at greater length, plus a quantified result.

## The measured costs applied to a 200-word abstract reporting one figure

The tradeoff is real: r = 0.457 (n = 67, p = 0.0001) between length and numerals per 100 words, and
r = 0.636 (n = 30) among abstracts that quantify at all. Short-and-dense exists, at 2 of 67, so it is
attainable and it is not the norm.

The frontier at 160 words holds 1.91 numerals per 100 words, which in a 160-word abstract is three
figures. Both abstracts on that frontier pay for the figures by naming no dataset, no metric and no
model, and by compressing the method into one long sentence rather than three.

Against the 67-abstract corpus, a 200-word abstract reporting one figure is at the 90th percentile
for length and at the 55th percentile for density (0.5 numerals per 100 words; 37 of 67 abstracts are
at zero, and 55 percent of the corpus is at or below 0.5). The equivalent density percentile in the
47-abstract batch A alone was the 66th, so the second draw moves this figure by 11 points and the
number should be read as approximate. The measured costs of the changes under consideration:

- **A second figure costs about 20 words** at the median (156 to 157.5 to 177 across 0, 1 and 2
  figures), or 8.1 words averaged over the full range. Two abstracts in the corpus fit two or three
  figures into under 160 words, so 20 words is the going rate rather than a requirement.
- **Naming the apparatus costs nothing and saves about 16 words** (median 160 with a name, 176
  without, n = 57 and 10). The abstracts with no name spend a full clause each time they refer to
  their own contribution.
- **Naming a metric or a benchmark costs nothing** at the median (161 either way). Naming a model by
  vendor name goes with 14 more words, on n = 10.
- **The cheapest 20 words to recover**, going by what the shortest abstracts in this corpus give up
  first, are the problem-framing sentence before the gap statement (absent in 8 of 10 abstracts of 140
  words or fewer, present in 74 percent above 180) and the closing implication sentence (absent in 6
  of 10 in the 150-to-180 band). Those two beats are the ones the venue treats as optional at every
  length.

---

Retrieval date for all 67 Anthology pages: 2026-09-06. Sampling seeds 20260906 (batch A, 47) and
20260907 (batch B, 20). Measurement and analysis code:
`scripts/acl2026_abstract_density/05_length_density.py`, reusing `03_measure.py` unchanged. Hand
adjudications: `scripts/acl2026_abstract_density/handcode_artifact_naming_67.json` (artifact naming)
and the enumerator override recorded inline in `05_length_density.py`. Batch-A abstracts are stored
verbatim in `acl2026_abstracts.json` under `sample_2026_09_06`; batch-B abstracts are stored verbatim
in `acl2026_abstracts.json` under `sample2_2026_09_06`.
