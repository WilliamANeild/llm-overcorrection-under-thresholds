# Quantitative and technical density of 2026 ACL-venue abstracts

Compiled 2026-09-06. Purpose: calibrate the abstract of a paper going to ARR in October 2026 against what abstracts in the target venues carry, after a reviewer of a 9-abstract sample said the abstract needed "more geek and numbers" and, scanning for its single statistic, missed it.

## Corpus and how it was drawn

Source: ACL Anthology landing pages, one HTTP request per paper, retrieved **2026-09-06**. The abstract was taken from the `div` with class `card-body acl-abstract` on each landing page, parsed by walking `div` nesting to the matching close rather than by assuming a `<span>` follows the heading, then stripped of markup. Abstracts are stored verbatim in `acl2026_abstracts.json`.

**2026 volumes that exist on the Anthology** (checked directly): `2026.acl-long` (2,222 papers excluding front matter), `2026.acl-short` (74), `2026.findings-acl` (2,163), `2026.eacl-long` (394). **`2026.naacl-long` does not exist** (HTTP 404), nor do `2026.emnlp-main` or `2026.starsem-1`; no paper from those was fetched or invented.

**Sampling.** Systematic sample with a fixed random start and a constant stride over each volume's paper list in Anthology order, seeded at 20260906 so the draw is reproducible. Target counts were 20 from `acl-long` (stride 111), 16 from `findings-acl` (stride 135), 8 from `eacl-long` (stride 49), 4 from `acl-short` (stride 18.5). This spreads the draw across the whole volume rather than taking a run of consecutive papers. 48 IDs were drawn; 47 yielded an abstract. `2026.findings-acl.1664` (microCLIP) has no abstract block on its landing page at all and is excluded rather than replaced.

**Bound on the sample.** The draw is unconditional on topic. It was not filtered toward empirical studies of LLM behaviour, because a filtered draw cannot say what the venue norm is. Genre is recorded per paper instead so the comparison can be conditioned. The consequence is that the corpus is dominated by method papers, which is what the volumes are dominated by: 36 of 47 propose a new method or system.

**How things were counted.** Word counts, sentence counts, every numeral count and category, and the position of the first statistic are produced mechanically by script (`scripts/acl2026_abstract_density/03_measure.py`, regex tokenizer and sentence splitter), never by eye. Three things are hand-coded, and are marked as such wherever they appear: paper genre, result valence, and the referent-attachment classification. The naming flags were script-detected and then hand-adjudicated, because "recall", "calibration" and "agreement" occur in these abstracts as ordinary English rather than as metric names; both counts are given.

A numeral is counted as **quantitative** only if it is not part of an identifier. Digits inside model and dataset names (GPT-o3, Gemma-2, Llama-3-8B, MQuAKE-2002, T2I, System-2), four-digit years, and enumeration markers such as "(1)" and "(2)" are counted separately and excluded from the density measure. Both figures are reported below.

## Corpus table

Genre: M = new method or system, B = new benchmark, dataset or resource, A = empirical analysis of model behaviour, P = position. Valence: POS = the principal reported result is that the authors' method works; NEG = the principal reported result is that models fail, are brittle, or an expected effect is absent. Density is quantitative numerals per 100 words.

| Anthology ID | Genre | Val | Words | Sent | Quant numerals | Ident/year digits | Number-words | Per 100w | Result % | First stat at sentence |
|---|---|---|---|---|---|---|---|---|---|---|
| `2026.acl-long.1210` | M | POS | 205 | 8 | 6 | 3 | 2 | 2.93 | 0 | 6/8 |
| `2026.acl-long.1766` | M | POS | 202 | 8 | 5 | 2 | 2 | 2.48 | 2 | 7/8 |
| `2026.acl-long.1877` | M | POS | 212 | 7 | 5 | 0 | 1 | 2.36 | 0 | 5/7 |
| `2026.eacl-long.325` | B | NEG | 171 | 8 | 4 | 0 | 1 | 2.34 | 0 | 4/8 |
| `2026.acl-long.1543` | M | POS | 157 | 8 | 3 | 0 | 0 | 1.91 | 3 | 7/8 |
| `2026.acl-short.38` | A | POS | 161 | 9 | 3 | 1 | 0 | 1.86 | 3 | 8/9 |
| `2026.acl-long.1655` | B | NEG | 189 | 6 | 3 | 0 | 2 | 1.59 | 0 | 4/6 |
| `2026.findings-acl.988` | M | POS | 159 | 7 | 2 | 0 | 1 | 1.26 | 2 | 6/7 |
| `2026.acl-long.544` | M | POS | 177 | 11 | 2 | 0 | 1 | 1.13 | 0 | 8/11 |
| `2026.findings-acl.583` | M | POS | 113 | 5 | 1 | 2 | 1 | 0.88 | 1 | 4/5 |
| `2026.acl-long.1988` | M | POS | 154 | 6 | 1 | 3 | 1 | 0.65 | 1 | 5/6 |
| `2026.findings-acl.1394` | M | POS | 157 | 7 | 1 | 2 | 0 | 0.64 | 1 | 7/7 |
| `2026.acl-long.99` | P | POS | 158 | 5 | 1 | 0 | 0 | 0.63 | 0 | 4/5 |
| `2026.acl-long.988` | M | POS | 163 | 7 | 1 | 0 | 0 | 0.61 | 1 | 5/7 |
| `2026.acl-long.432` | M | POS | 176 | 8 | 1 | 4 | 1 | 0.57 | 0 | 7/8 |
| `2026.findings-acl.1529` | B | NEG | 182 | 7 | 1 | 0 | 1 | 0.55 | 0 | 3/7 |
| `2026.acl-long.1099` | M | POS | 189 | 7 | 0 | 0 | 0 | 0.00 | 0 | none |
| `2026.acl-long.1321` | M | POS | 157 | 6 | 0 | 0 | 0 | 0.00 | 0 | none |
| `2026.acl-long.1432` | M | POS | 203 | 9 | 0 | 0 | 1 | 0.00 | 0 | none |
| `2026.acl-long.2099` | M | POS | 119 | 4 | 0 | 0 | 0 | 0.00 | 0 | none |
| `2026.acl-long.210` | B | NEG | 120 | 6 | 0 | 0 | 1 | 0.00 | 0 | none |
| `2026.acl-long.2210` | M | POS | 169 | 8 | 0 | 0 | 1 | 0.00 | 0 | none |
| `2026.acl-long.321` | M | POS | 151 | 6 | 0 | 0 | 1 | 0.00 | 0 | none |
| `2026.acl-long.655` | M | POS | 163 | 6 | 0 | 0 | 0 | 0.00 | 0 | none |
| `2026.acl-long.766` | M | POS | 122 | 7 | 0 | 0 | 3 | 0.00 | 0 | none |
| `2026.acl-long.877` | M | POS | 136 | 6 | 0 | 0 | 2 | 0.00 | 0 | none |
| `2026.acl-short.1` | M | POS | 154 | 6 | 0 | 0 | 1 | 0.00 | 0 | none |
| `2026.acl-short.20` | M | POS | 154 | 5 | 0 | 0 | 2 | 0.00 | 0 | none |
| `2026.acl-short.57` | M | POS | 73 | 3 | 0 | 0 | 1 | 0.00 | 0 | none |
| `2026.eacl-long.128` | M | POS | 128 | 6 | 0 | 0 | 1 | 0.00 | 0 | none |
| `2026.eacl-long.177` | M | POS | 152 | 7 | 0 | 0 | 1 | 0.00 | 0 | none |
| `2026.eacl-long.226` | A | POS | 192 | 8 | 0 | 2 | 0 | 0.00 | 0 | none |
| `2026.eacl-long.276` | M | POS | 162 | 6 | 0 | 0 | 0 | 0.00 | 0 | none |
| `2026.eacl-long.29` | M | POS | 180 | 8 | 0 | 0 | 2 | 0.00 | 0 | none |
| `2026.eacl-long.374` | A | POS | 129 | 6 | 0 | 0 | 2 | 0.00 | 0 | none |
| `2026.eacl-long.79` | M | POS | 161 | 8 | 0 | 0 | 0 | 0.00 | 0 | none |
| `2026.findings-acl.1123` | M | POS | 193 | 9 | 0 | 0 | 0 | 0.00 | 0 | none |
| `2026.findings-acl.1259` | M | POS | 152 | 6 | 0 | 0 | 1 | 0.00 | 0 | none |
| `2026.findings-acl.177` | M | POS | 131 | 6 | 0 | 0 | 0 | 0.00 | 0 | none |
| `2026.findings-acl.1799` | A | POS | 193 | 10 | 0 | 0 | 1 | 0.00 | 0 | none |
| `2026.findings-acl.1935` | B | POS | 154 | 6 | 0 | 0 | 0 | 0.00 | 0 | none |
| `2026.findings-acl.2070` | B | NEG | 229 | 10 | 0 | 0 | 1 | 0.00 | 0 | none |
| `2026.findings-acl.312` | M | POS | 163 | 7 | 0 | 0 | 2 | 0.00 | 0 | none |
| `2026.findings-acl.42` | M | POS | 155 | 7 | 0 | 0 | 0 | 0.00 | 0 | none |
| `2026.findings-acl.447` | M | POS | 173 | 6 | 0 | 0 | 1 | 0.00 | 0 | none |
| `2026.findings-acl.718` | M | POS | 160 | 8 | 0 | 0 | 0 | 0.00 | 0 | none |
| `2026.findings-acl.853` | M | POS | 166 | 7 | 0 | 1 | 0 | 0.00 | 0 | none |

Titles for every ID are stored with the abstracts in `acl2026_abstracts.json` under `sample_2026_09_06`.

## Distribution of numerals per 100 words

Across all 47 abstracts: **min 0.00 / p25 0.00 / median 0.00 / p75 0.64 / p90 1.88 / max 2.93 / mean 0.48**.

**31 of 47 abstracts (66 percent) contain no quantitative digit at all.** That is what drives the median to zero. The quartiles are therefore not a smooth spread around a typical value: the distribution is a large spike at zero and a thin tail.

| Statistic | Quantitative numerals / 100w | All digit runs / 100w (identifiers, years, enumerators included) |
|---|---|---|
| minimum | 0.00 | 0.00 |
| 25th percentile | 0.00 | 0.00 |
| median | 0.00 | 0.00 |
| 75th percentile | 0.64 | 1.19 |
| 90th percentile | 1.88 | 2.53 |
| maximum | 2.93 | 4.39 |
| mean | 0.48 | 0.73 |

**Where 0.5 sits.** A density of 0.5 numerals per 100 words falls at the **66th percentile**: 31 of 47 abstracts (66 percent) are at or below it. In a 170-word abstract, 0.5 per 100 words is a single statistic. One statistic already puts an abstract above two thirds of this corpus.

**Where 3.5 sits.** A density of 3.5 falls at the **100th percentile**. **No abstract in the sample reaches it.** The maximum observed is 2.93 (2026.acl-long.1210), and only 4 of 47 exceed 2.0. On the all-digit-runs measure, which counts model-name and year digits too, 3.5 sits at the 98th percentile and one abstract reaches 4.39. Writing to 3.5 would put an abstract outside the range this venue produces.

Raw counts rather than rates: 31 abstracts carry 0, 7 abstracts carry 1, 2 abstracts carry 2, 3 abstracts carry 3, 1 abstract carries 4, 2 abstracts carry 5, 1 abstract carries 6 quantitative numerals. The modal abstract has zero; the modal non-zero abstract has one.

Abstract length itself: min 73 / p25 153 / median 161 / p75 178 / p90 197 / max 229 / mean 162 words, min 3 / p25 6 / median 7 / p75 8 / p90 9 / max 11 / mean 7 sentences.

### Numbers written as words

Spelled-out numbers ("three benchmarks", "five national cultures") per abstract: min 0 / p25 0 / median 1 / p75 1 / p90 2 / max 3 / mean 1. 29 of 47 abstracts carry at least one. **13 of 47 carry neither a digit nor a spelled number.** This matters for a reviewer who scans: a spelled number does not catch the eye, and abstracts routinely use one where a digit was available ("across five national cultures and ten culture-sensitive tasks", `2026.acl-long.766`; "four multi-party dialogue datasets", `2026.acl-long.877`).

## What kind of numerals they are

A single numeral can carry more than one tag ("70% on easy tasks" is both a percentage and, in context, a count). Totals are numerals; the second column is abstracts.

| Category | Total numerals | Abstracts with at least one |
|---|---|---|
| Result percentage | 14 | 8 |
| Sample size or count | 12 | 9 |
| p-value | 0 | 0 |
| Effect size | 0 | 0 |
| Scale-point or level figure | 1 | 1 |
| Model / task / dataset count | 3 | 2 |
| Speedup or ratio multiplier | 6 | 1 |
| Model size in parameters | 6 | 3 |
| Metric score (non-percentage) | 2 | 2 |
| Unclassified | 6 | 5 |

**No abstract in the 47 reports a p-value, and none reports an effect size** (Cohen's d, a kappa, a correlation coefficient with a value attached). The inferential-statistics vocabulary of an experimental social science paper is absent from this venue's abstracts. What appears instead is a percentage improvement, a dataset size, a count of models or benchmarks, and occasionally a speedup.

### Among abstracts carrying at least one result percentage

8 of 47 abstracts (17 percent) carry a result percentage. Among those 8: 4 carry 1, 2 carry 2, 2 carry 3. Median 1.5, mean 1.75, maximum 3.

So the convention, where an abstract quantifies a result at all, is **one or two percentages, not a battery**. Half the abstracts that report any percentage report exactly one. The densest, `2026.acl-long.1543` and `2026.acl-short.38`, report three each, and both use them for a range or a contrast rather than a list.

### Which beat the numbers sit in

Position of the first statistic, among the 16 abstracts that have one: sentence min 3.0 / p25 4.0 / median 5.5 / p75 7.0 / p90 7.5 / max 8.0 / mean 5.6, out of a median of 7 sentences. As a fraction of the way through the abstract: min 0.43 / p25 0.71 / median 0.80 / p75 0.88 / p90 0.88 / max 1.00 / mean 0.77.

**14 of 16 put their first statistic in the final third of the abstract; 2 of 16 put one in the first half.** Numbers cluster hard in the results beat and are essentially absent from the motivation and method beats. The motivation beat is qualitative in every abstract in the sample. Where a number appears early it is a resource size in a benchmark paper describing what was built (`2026.findings-acl.1529`, "NLCO covers 43 CO problems", sentence 3 of 7), never a finding.

Within the sentence, the first statistic falls at word min 3.0 / p25 3.8 / median 10.5 / p75 17.0 / p90 23.0 / max 25.0 / mean 11.7 of a sentence averaging 26 words. The median is word 10: mid-sentence, after the subject and verb have named what is being measured.

## First-statistic clauses, verbatim, classified by referent attachment

Every clause below is quoted verbatim from the abstract, bounded by the punctuation around it. Classification is hand-coded. The categories are: **BEFORE**, the thing being measured is named immediately before the numeral, usually joined by "of" or "by"; **AFTER**, the referent follows the numeral as its head noun; **PAREN**, the numeral sits in a parenthetical gloss on a claim made in the preceding main clause; **PRECEDING SUBORDINATE CLAUSE**, the referent sits in a subordinate clause before the one holding the numeral.

### Referent immediately before the numeral, 8 of 16

- `2026.acl-long.1210`: "these optimizations enable EQUIP to achieve geomean speedups of 1.62×"
- `2026.acl-long.1543`: "Experiments on diverse benchmarks show that NeuralFSM consistently outperforms prior baselines by an average margin of 6.74%–19.39%"
- `2026.acl-long.432`: "improving general domain alignment performance by ~10 points on the helpfulness and harmless benchmarks."
- `2026.acl-long.544`: "double-blind expert reviews yielded an average score of 4.80/5.00 across novelty"
- `2026.acl-long.988`: "Continued training on these refined trajectories enables the agent to evolve toward more efficient search patterns and reduces tool-call rounds by about 20% while improving accuracy."
- `2026.acl-long.99`: "PW-MCC ≈ 0.80 for TopK SAEs on LLM activations"
- `2026.acl-short.38`: "Disabling relation-sensitive features leads to performance drops of over 22%"
- `2026.findings-acl.583`: "our method achieves recovery rates of up to 94% on distractor-vulnerable samples."

### Referent after the numeral, 7 of 16

- `2026.acl-long.1655`: "GenomeQA comprises 5,200 samples drawn from multiple biological databases"
- `2026.acl-long.1766`: "Experiments across 7B/14B/32B models demonstrate that TH2T significantly reduces inference costs by over 70% on easy tasks and 40% on complex ones without compromising performance."
- `2026.acl-long.1877`: "Extensive experiments on 4 LLMs ranging from 1.7B to 30B parameters"
- `2026.acl-long.1988`: "Results show that AutoRAN achieves approaching 100% success rate within one or few turns"
- `2026.eacl-long.325`: "It spans 2M examples"
- `2026.findings-acl.1529`: "NLCO covers 43 CO problems and is organized using a four-layer taxonomy of variable types"
- `2026.findings-acl.988`: "showing a 6.81% improvement in generation overall quality over foundation LLMs and 17.19% gain in Insight over strong baselines."

### Numeral in a parenthetical, referent in the preceding main clause, 1 of 16

- `2026.findings-acl.1394`: "7% unsafe on I2P"

### Referent in a preceding subordinate clause, 0 of 16

None.

**8 of 16 name the referent immediately before the numeral; 7 of 16 put it immediately after. Zero of 16 put the referent in a preceding subordinate clause.** In every case in this corpus, the noun that says what the number is a number *of* sits inside the same clause as the number, adjacent to it: "an average margin of 6.74%–19.39%", "speedups of 1.62×", "recovery rates of up to 94%", "5,200 samples", "43 CO problems", "2M examples". A reader can stop at the numeral and read one noun phrase in either direction and have the whole fact.

The single near-exception is `2026.findings-acl.1394`, where the numeral is parenthetical: "SafePatch achieves robust unsafe suppression (7% unsafe on I2P)". Even there the parenthetical is self-describing, and the qualitative claim it glosses stands on its own in the main clause.

This is the direct answer to the reviewer's miss. The construction in our abstract, "Among the revisions that do change quality, 70% lower it", puts the referent in a preceding subordinate clause and leaves the numeral attached to a bare pronoun. **That construction occurs zero times in 47 abstracts and zero times in the prior 9.** The figure was not missed because there was only one of them; it was missed because it is written in a shape this venue's readers are not scanning for. Rewriting it as "70% of quality-changing revisions lower quality" puts the referent after the numeral, which is the second most common pattern here, without adding a single further statistic.

## Naming: artifacts, models, metrics, datasets

Counts are hand-verified. The script's regex count matched the hand count for artifacts, models and datasets; it differed only for metrics, where "recall", "calibration" and "agreement" appear in these abstracts as ordinary English. Both metric figures are given below.

| Signal | Abstracts | Share |
|---|---|---|
| Introduces a named artifact (capitalised name or acronym) | 40/47 | 85% |
| Names at least one quantitative evaluation metric | 16/47 | 34% |
| Names at least one evaluation dataset or benchmark it runs on | 9/47 | 19% |
| Names at least one model by name (GPT, Llama, Gemma, Gemini, Pythia …) | 3/47 | 6% |
| Carries at least one quantitative digit | 16/47 | 34% |
| Carries at least one result percentage | 8/47 | 17% |

Script-detected metric mentions were 18/47 before adjudication; the hand-verified figure is 16/47.

**Naming an artifact is by far the strongest technical signal in this corpus, and it is not close.** 40 of 47 abstracts (85 percent) coin and use a capitalised name for what they built, against 16 of 47 (34 percent) that carry any digit and 8 of 47 (17 percent) that carry a result percentage. The typical abstract in these volumes reads as technical because it names a mechanism, not because it quantifies one.

The 7 abstracts with no named artifact are `2026.acl-long.1099`, `2026.findings-acl.42`, `2026.findings-acl.1259`, `2026.findings-acl.1935`, `2026.eacl-long.29`, `2026.eacl-long.226`, `2026.eacl-long.276`. All 7 of them also carry no quantitative digit, so the two sparse signals coincide exactly: every abstract in the corpus that reports a figure also coins a name.

Naming a model is rare: 3 of 47. "Experiments across 7B/14B/32B models" and "4 LLMs ranging from 1.7B to 30B parameters" are the usual form, giving scale without a vendor name. Naming a dataset is likewise a minority behaviour, 9 of 47; most abstracts say "three QA benchmarks" or "four multi-party dialogue datasets" and leave them unnamed.

Combining the two signals: 16 of 47 abstracts both name an artifact and carry a digit; 24 name an artifact and carry no digit; 0 carry a digit without naming an artifact; 7 do neither.

## Negative and null results versus working methods

Valence is hand-coded from the principal reported result. Genre and valence are almost fully confounded in this sample, and that confound has to be stated rather than analysed away: **5 of the 6 benchmark papers report a negative principal finding, and all 5 negative-valence abstracts are benchmark papers.** No method paper in the sample reports a negative principal result, which is itself the finding: this venue's method abstracts do not publish failures.

| Group | n | Median /100w | p75 | Mean | Zero-digit | With a result % |
|---|---|---|---|---|---|---|
| Negative or null principal result | 5 | 0.55 | 1.59 | 0.90 | 2 | 0 |
| Working-method principal result | 42 | 0.00 | 0.62 | 0.43 | 29 | 8 |
| Benchmark papers (B) | 6 | 0.28 | 1.33 | 0.75 | 3 | 0 |
| Method papers (M) | 36 | 0.00 | 0.62 | 0.43 | 25 | 7 |
| Analysis papers (A) | 4 | 0.00 | 0.47 | 0.47 | 3 | 1 |

**Negative-result abstracts carry *more* numbers, not fewer** (median 0.55 against 0.00, mean 0.90 against 0.43), though with n=5 in the negative cell this is a direction, not an estimate. The mechanism is visible in the text: a paper whose claim is that models fail has to say how much they fail by, or say what the benchmark contains, to make the failure legible. `2026.eacl-long.325` gives "2M examples, 77 models across 11 families, and 9 programming languages" before stating that detector performance "remains far below practical usability". `2026.acl-long.1655` gives "5,200 samples" and "6 to 1,000 base pairs".

None of the five negative abstracts reports a result percentage; all 8 abstracts carrying a result percentage report a positive result. A negative finding in this corpus is quantified by the size of what was tested, not by the size of the failure.

Two of the five negative abstracts carry no digit at all: `2026.acl-long.210` ("We reveal substantial performance variation") and `2026.findings-acl.2070` ("even simple transformations cause a significant performance drop"). Both state the negative finding in words alone and were accepted. So a quantified negative is the denser convention, but an unquantified one is not disqualifying at these venues.

Conditioning on genre rather than valence gives the same ordering: benchmark papers are the densest genre, method papers the sparsest, with analysis papers between them.

## The prior 9-abstract sample was not representative

Re-measuring the 9 abstracts already held in `acl2026_abstracts.json` with the same script: numerals per 100 words min 0.00 / p25 1.01 / median 1.80 / p75 2.68 / p90 4.78 / max 5.98 / mean 2.15; 2 of 9 carry no digit; 6 of 9 carry a result percentage.

Against the systematic sample, that is a different population. **Median density 1.80 against 0.00. Result percentages in 6/9 (67 percent) against 8/47 (17 percent).** The 9 were gathered as topical neighbours of this paper, and abstracts that are topical neighbours of a quantitative behavioural study are themselves quantitative. Calibrating a target density on them overstates the venue norm by roughly a factor of four at the median. That is the concrete reason the 9-paper sample was the wrong instrument, independent of its size.

| Prior-9 abstract | Words | Quant numerals | Per 100w | Result % |
|---|---|---|---|---|
| ZIP *SEM | 160 | 2 | 1.25 | 2 |
| CGM Findings | 189 | 4 | 2.12 | 2 |
| DART Findings | 223 | 10 | 4.48 | 9 |
| MemoryDial Findings | 155 | 0 | 0.00 | 0 |
| DogCat EACL | 198 | 2 | 1.01 | 1 |
| SAGE ACL | 155 | 0 | 0.00 | 0 |
| CommonToWhom ACL | 184 | 11 | 5.98 | 4 |
| ReasoningTraces ACL | 167 | 3 | 1.80 | 1 |
| SCOPE ICML | 149 | 4 | 2.68 | 0 |

Their first-statistic clauses show the same referent attachment as the systematic sample: "a benchmark of 4,180 questions", "a dataset of 9,720 comprehension questions", "Across 45,000 samples from three LRMs", "ZIP achieves 95.8% accuracy compared to 65.8% for LIME", "DART improves Llama-3-8B-Instruct accuracy from 39.0% to 68.8%". Referent adjacent to the numeral in all seven that have one. None uses a preceding subordinate clause.

## What a 200-word abstract in this venue would carry

Scaling the observed rates to 200 words. The corpus median abstract is 161 words, so 200 words is already at the 89th percentile for length.

**At the median.** The median abstract in this corpus contains **zero digits**. It names a coined artifact, states the gap it closes, describes the mechanism in two or three sentences, and closes with an unquantified claim of improvement over baselines on unnamed benchmarks. Writing to the median would mean removing the statistic altogether, which is not the goal here. The median is worth knowing for one reason: it establishes that the reviewer's premise, that the abstract is short on numbers by the standard of the venue, is not what the venue does.

**At the 75th percentile.** The 75th percentile is 0.64 numerals per 100 words, which over 200 words is **1.3 numerals, so one or two**. Concretely, a 200-word abstract at the 75th percentile of this corpus carries:

- one coined, capitalised name for what the paper introduces, used two or three times (85 percent of the corpus does this, so it is not a percentile question, it is the floor);
- one or two figures, most often a single result percentage (the 8 abstracts with any percentage carry a median of 1.5);
- the figure placed in the final third, in the results sentence, with its referent inside the same clause;
- a named metric (34 percent of the corpus) and, less often, a named benchmark (19 percent);
- no p-value, no effect size, no confidence interval; none of the 47 carries one.

**At the 90th percentile**, 1.88 per 100 words, or about 4 numerals in 200 words: a resource size, a count of models or benchmarks evaluated, and two result figures used as a contrast or a range. `2026.acl-long.1877` is the worked example at this level, with "4 LLMs ranging from 1.7B to 30B parameters, across 4 SWA ratios" and "6 strong static head-level methods".

**What none of them do.** No abstract in the corpus reaches 3.5 numerals per 100 words, so a 200-word abstract carrying seven figures would be outside the observed range. Adding numbers past two or three does not move the abstract toward the venue; it moves it away.

### The implication for the reviewer's comment

Two changes are indicated, and neither is "add more numbers".

First, **reattach the referent**. "Among the revisions that do change quality, 70% lower it" is the one construction in the paper's abstract that does not occur anywhere in 56 measured abstracts. Recast so the noun sits against the numeral: "70% of quality-changing revisions lower quality". This costs nothing and is the change that addresses the failure that occurred, which was a scan that did not find the figure.

Second, **the technical signal these venues read is the named artifact, not the digit count**. 85 percent name one; 34 percent carry any digit. If the abstract reads as insufficiently technical, the lever with the larger observed effect is to coin and repeat a name for the construct or the measure, and to name the metric and the models, rather than to raise the numeral count from one to five. Going from one figure to two, placed in the results sentence, moves the abstract from roughly the 66th to the 80th percentile of this corpus; going to five would put it beyond the maximum.

---

Retrieval date for all Anthology pages: 2026-09-06. Sampling seed: 20260906. Measurement and reporting code, with the two hand-coding files: `scripts/acl2026_abstract_density/`. Abstracts stored verbatim in `acl2026_abstracts.json` under `sample_2026_09_06`.
