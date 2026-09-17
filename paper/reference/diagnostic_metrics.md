# Diagnostic metrics

Measured 2026-09-17 by `scripts/introduction_corpus/08_advanced_metrics.py` over the 69 cached
papers (45 excluding Ali's 24), plus direct checks on the corpus for features the script counts
per-paper rather than per-word. These are the measures a referee reacts to. The length and
readability censuses describe the manuscript; these say how it will be received.

## How rare our statistical practice is

Of the 69 cached papers, presence of each feature anywhere in the body:

| feature | papers | share |
|---|---:|---:|
| any p-value | 11 | 16% |
| any confidence interval | 8 | 12% |
| any nonparametric test or bootstrap | 15 | 22% |
| any mention of pre-registration | 1 | 1% |

Our paper carries all four throughout, and reports a threshold set in advance that was not met.
On the last row it is close to alone in the corpus. This is the paper's strongest asset and it is
currently presented as a limitation rather than as method discipline.

The per-1000-word rates below therefore read as "far above the field" because the field median is
zero, not because our reporting is excessive.

| per 1000 words | ours | p25 | median | p75 | Emami |
|---|---:|---:|---:|---:|---:|
| p-values | 3.5 | 0.0 | 0.0 | 0.0 | 0.0 |
| confidence intervals | 0.9 | 0.0 | 0.0 | 0.0 | 0.0 |
| sample sizes | 2.3 | 0.0 | 0.0 | 0.0 | 0.0 |
| effect sizes | 0.7 | 0.0 | 0.0 | 0.2 | 0.2 |

## Where we sit outside the field, and what it costs

| per 1000 words | ours | p25 | median | p75 | Emami | |
|---|---:|---:|---:|---:|---:|---|
| hedge words | 1.4 | 3.2 | 4.6 | 6.0 | 5.1 | far below |
| first person (we/our) | 8.8 | 14.9 | 17.9 | 23.5 | 12.9 | below |
| numerals | 87.6 | 52.5 | 60.7 | 69.0 | 77.0 | above everyone |

**Hedging.** A third of the field's rate. Claims are stated flatly, which is the register the voice
rules ask for, and it is also what produces the reviewer comment that authors overclaim. Mitigated
by the paper stating "we do not claim" explicitly in three places.

**Numerals.** Above the corpus p75 and above Ali's own rate. This is the mechanism behind the
Methods readability result in `prose_census.md`: prose at this numeral density is hard to read
whatever its sentence length.

**First person.** Below the field, consistent with the standing instruction to minimise it.

## Citation recency

| | ours | corpus |
|---|---:|---:|
| cited works in the live build | 36 | |
| median age | 2.0 years | 3.0 years |
| share 2 years old or newer | 67% | 23% |
| share 7 years old or older | 6% | 16% |

Reads current. The risk on the other side is a bibliography a referee reads as thin on
foundations. The paper does reach back, with Skitka 1999 and Parasuraman and Manzey 2010.

## Reproducibility disclosure

Present: model versions named, temperature stated, prompt text quoted, sample filters stated,
human validation described.

**Absent: any code or data availability statement, and any compute or cost statement.** The
Responsible NLP checklist asks for both, and an incomplete checklist is a named desk-rejection
ground. Note that any repository link must be anonymised for review.

## Terminology consistency

One concept should carry one name. Counts across the live build:

- **The intervention has two names and the mapping is never stated.** "targeted" 11 times (abstract
  1, methods 2, results 7, conclusion 1); "directed" 4 times (results 3, discussion 1). No sentence
  in the paper says these are the same thing. The abstract promises "a single targeted critique"
  while the Discussion's lead paragraph is titled "Evaluate, then direct". The negative pole is
  consistent: "undirected" 16 times, "generic" 6.
- **The stopping point has four names:** "quality-optimal stopping point" (3), "quality-maximizing
  stopping point" (1), "quality-optimal turn" (1), "optimal turn" (1).
- **The threshold has two:** "sufficiency threshold" (2), "sufficient threshold" (1).
- **"meta-wrapping"** appears once at `methods.tex:60` for what the paper otherwise calls
  meta-commentary.

**Correction to the script's own output.** It groups meta-response with meta-commentary and reports
three variants of one concept. Those are two distinct concepts in this paper: a meta-response is a
reply carrying no new task content, meta-commentary is the boilerplate wrapper around a revision
that the stripping procedure removes. Only "meta-wrapping" is a genuine third name.

---

# Terminology sweep, whole build, 2026-09-17

Run by `scripts/introduction_corpus/09_terminology_sweep.py` across all nine live section files
including the appendix. Four detection routes rather than a list of suspects: modifier phrases
sharing a technical head noun, hyphen and spacing variants, capitalisation of defined terms, and
which word names each role. Every flag below was then read in context, because three of the four
routes produced false positives worth recording so they are not chased again.

## Genuine inconsistencies

**1. The LLM scorer is called both "evaluator" and "judge".** A principled split is available and
mostly honoured: "evaluator" for our own selected scorer, "judge" for the general practice the
related work discusses. The paper crosses it in four places. The Methods subsection titled
**Judge Calibration** opens "Six candidate **evaluators** were scored against three human raters."
Limitations says "the highest human-correlation **judge**". The stripping validation says human
annotators "agreed with the LLM **judge**". And one appendix sentence uses both for the same thing:
"selecting our **evaluator** empirically through a six-model **judge** calibration."

**2. The intervention is called both "targeted" and "directed", with the mapping never stated.**
"targeted" 11 times (abstract, methods, results, conclusion); "directed" 4 (results, discussion).
The abstract promises "a single targeted critique"; the Discussion's lead paragraph is titled
"Evaluate, then direct". The negative pole is consistent: "undirected" 16, "generic" 6.

**3. The stopping point carries four names:** "quality-optimal stopping point" (3),
"quality-maximizing stopping point" (1), "quality-optimal turn" (1), "optimal turn" (1).

**4. "sufficient threshold"** appears once where the paper otherwise says "sufficiency threshold".

**5. "meta-wrapping"** appears once at `methods.tex:60` for what is otherwise meta-commentary.

**6. Lowercase "turn 1"** in the heading `\paragraph{The task, as given at turn 1.}` at
`sections/_fig1_appendix.tex`, where the paper otherwise writes Turn~1 throughout.

## Checked and clean, so do not chase these again

**Scale-level capitalisation is principled.** Quoted and capitalised ("Sufficient", "Functional")
names the level on the six-level scale; lowercase is the ordinary adjective or the threshold
condition. Correct at every occurrence.

**Hyphenation is correct English throughout.** Hyphenated when attributive ("five-turn design",
"first-turn outputs"), open when the phrase is a noun ("each conversation runs five turns", "at the
first turn"). The detector flagged this as a variant pair; it is not one.

**"Turn" plus a number is capitalised everywhere** except the one appendix heading above. The other
apparent lowercase hits are TikZ node names (`turn1`, `turn2`) in a figure and one sentence where a
percentage happens to follow "at the next turn".

**"raters" and "annotators" name two different groups doing two different tasks, consistently.**
"Raters" is always the three humans who scored quality on the 1--5 scale over 64 stratified samples.
"Annotators" is always the two humans who worked on stripped content, for the pairwise reversibility
comparison and the stripping validation. Every one of the twelve occurrences respects the split.

## A clarity gap rather than an inconsistency

Because the split above is never declared, a reader meets "three human raters" in one Methods
subsection and "two human annotators" in another and cannot tell whether there are two people,
three, or five. Only the Ethics Statement resolves it, by saying the raters are "the first author and
two research assistants", from which the two annotators can be inferred to be a subset. The body
never says so.
