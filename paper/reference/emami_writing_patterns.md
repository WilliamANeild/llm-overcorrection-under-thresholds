# Ali Emami's writing, measured

Compiled 2026-09-08. **24 of his NLP introductions** fetched as arXiv LaTeXML HTML and
counted by the same script used for the venue corpus
(`scripts/introduction_corpus/02_fetch_intros.py`), so every number here is directly
comparable to `paper/rules/03_introduction.md` Part 2.

**Coverage.** The arXiv author search for "Ali Emami" returns a second researcher of the
same name who publishes on photonic time crystals and quantum many-body systems; those
papers are excluded and are not his. Titles were read from the arXiv records for 28
papers. One introduction (2402.13372, LREC-COLING) extracts 0 citation anchors because
of its template and is excluded from citation statistics only.

## The measurements, against the ACL-family venue corpus

| Measure | **Emami (n=24)** | ACL-family corpus (n=25) | |
|---|---:|---:|---|
| Introduction words, median | **583** | 658 | He writes **shorter** than the venue |
| p75 / max | 663 / 990 | 768 / 862 | |
| Paragraphs, median | 6 | 6 | Same. But 8 of 24 run 8 or more |
| Words per paragraph, median | 97 | ~95 | Same |
| Citation references, median | **14** | 17 | **Below** the venue median |
| Citations per 100 words, median | 2.5 | 2.9 | Slightly below |
| Citations in paragraph 1, median | 5 | 6 | Same |
| Citations in the last two blocks | 0 | 0 | Same |
| **References a figure in the introduction** | **20 of 24 (83%)** | 27 of 44 (61%) | **His strongest divergence** |
| Opens on a rhetorical question | 0 of 24 | 0 of 44 | Absolute in both |

## Four trends worth acting on

**1. He writes short introductions.** Median 583 words against a venue median of 658.
Our draft at 996 is **413 words over his median** and 134 over the venue maximum. Length
is the single largest gap between this draft and his practice.

**2. He puts a figure in the introduction, and it is close to a rule.** 20 of 24, against
61% for the venue. Our draft references Figure 1, so this is already right, and the
figure earns its place under his practice more than under the venue's.

**3. He is not a "sea of blue" maximalist.** His median is 14 citation references, below
the venue's 17. Our draft's 13 is essentially at his median already. **The citation
problem in our draft is mostly a length problem**: 13 references in 996 words is 1.3 per
100, but the same 13 in 700 words is 1.9, and 18 references in 700 words is 2.6, which is
his median. Cutting length does about half the work.

**4. Openers are shorter than the venue's but not aphoristic as a rule.** His median
opening sentence is 22.5 words against the venue's 25.5, and only 4 of 24 run under 15
words. He does write the short declarative opener, at roughly twice the venue rate, and
some are very good:

> "Most users meet an LLM before they actually meet it." (2607.05113)
> "Memorization is central to understanding language model behavior." (2604.05074)
> "Chain-of-Thought prompting transformed how we use Large Language Models." (2502.03418)
> "State-of-the-art large language models (LLMs) silently 'correct' African American English." (2607.06845)

**This corrects `rules/03` Part 1 item 5**, which flagged our 10-word opener ("Large
language models are evaluated, for the most part, alone.") as "a stylistic fragment where
the corpus is flat," with no analogue in 23 papers. Measured against the person reading
the draft, it has four analogues in 24 and sits in a form he uses. The finding was right
about the general corpus and wrong about this reader.

His other favoured opener is the contrast hook, which is worth knowing because our paper
has exactly that shape available:

> "Large language models can explain quantum mechanics and write sophisticated code, yet
> often fail to parse sentences like 'The cat that the dog chased...'" (2510.20543)

## Titles: the sharpest deviation in our paper

**26 of 28 of his titles are two-part**, split by a colon, a question mark, or an
exclamation. 93%. Only two are a single clause.

The recurring form is an evocative or plain-language first half, then a technical
description:

- *Rating the Pitch, Not the Product: User Evaluations of LLMs Reflect Expectations More Than Performance*
- *The Dog the Cat Chased Stumped the Model: Measuring When Language Models Abandon Structure for Shortcuts*
- *Common to Whom? Regional Cultural Commonsense and LLM Bias in India*
- *Can We Afford The Perfect Prompt? Balancing Cost and Accuracy with the Economical Prompting Index*
- *Subtle Biases Need Subtler Measures: Dual Metrics for Evaluating Representative and Affinity Bias*
- *Beyond Content: How Grammatical Gender Shapes Visual Representation in Text-to-Image Models*

Nine of 28 lead with a named artifact (DART, SCOPE, SAGE, STOP!, EvoGrad, MirrorStories,
Memory Dial, WSC+, NYT-Connections). Three carry a question.

**Our title, "Intrinsic Self-Correction Requires Extrinsic Direction", is a single clause
with no break.** That is the 2-of-28 form. It is a good sentence and it states the claim,
but it is the one place where the paper does not look like his.

Note that a question title is available to us and is attested in his set three times,
which matters because the abstract already opens on one and the introduction cannot.
