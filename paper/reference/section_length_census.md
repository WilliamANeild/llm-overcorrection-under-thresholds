# Section length and float census

Measured 2026-09-14 by `scripts/introduction_corpus/06_section_census.py` over the 69 cached
full papers (the same cache built for the introduction corpus), split into the whole corpus and
the 24 papers by Ali Emami. Counts are mechanical: top-level `\section` spans from the rendered
arXiv HTML, floats excluded from word counts, citations counted as `href="#bib.bib"` anchors.
Nothing here is estimated.

## Words per top-level section

| section | n | p25 | median | p75 | Emami median | Emami n |
|---|---:|---:|---:|---:|---:|---:|
| introduction | 66 | 561 | 658 | 768 | 583 | 24 |
| related work | 62 | 310 | 402 | 526 | 397 | 24 |
| method | 34 | 609 | 906 | 1182 | 633 | 13 |
| results | 47 | 723 | 1109 | 1345 | 916 | 23 |
| discussion | 15 | 225 | 568 | 735 | too few to report | 4 |
| conclusion | 65 | 76 | 106 | 138 | 102 | 24 |

## Floats and structure

Body figures p25 3 / median 5 / p75 6. Body tables p25 3 / median 4 / p75 6. Median figures per
table 1.25. Top-level sections p25 6 / median 6 / p75 7. Display equations p25 0 / median 2 / p75 9.

## This supersedes `rules/04_related_work.md` R2

R2's 550-to-900 target came from 22 sections and sat above its own stated NLP mean of 543. The
62-section median is 402. R2 is corrected in place; the correction records why.

## Where our paper sits, 2026-09-14

| section | ours | band (p25 to p75) | |
|---|---:|---|---|
| introduction | 759 | 561 to 768 | pass |
| related work | 445 | 310 to 526 | pass |
| method | 967 | 609 to 1182 | pass, above Ali's 633 |
| results | 1036 | 723 to 1345 | pass |
| discussion | 496 | 225 to 735 | pass |
| conclusion | 113 | 76 to 138 | pass |
| body figures | 5 | 3 to 6 | pass |
| body tables | 3 | 3 to 6 | pass |
| sections | 6 | 6 to 7 | pass |

Methods at 967 is inside the corpus band but half again Ali's own median. It is the one place
where our length departs from his habit rather than from the field's.
