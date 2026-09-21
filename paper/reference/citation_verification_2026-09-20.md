# Citation verification, 2026-09-20

All 36 references cited in the live build were checked against an authoritative source:
the ACL Anthology, the ICLR or NeurIPS proceedings, Crossref, the arXiv API, or the
publisher's own page. Every one exists, and every author list, venue and year is correct.
No reference was fabricated, and none is attributed to the wrong authors.

## Method

Cited keys were resolved from `main.tex` rather than assumed, so retired sections do not
enter the check. Sources used, by class:

- arXiv API (`export.arxiv.org/api/query`), bulk id lookup, for title and author lists.
- ACL Anthology `.bib` endpoints, which give the published pages, address and volume.
- Crossref (`api.crossref.org`, and DOI content negotiation) for the journal and ACM entries.
- Conference proceedings and blog pages for award and acceptance claims.

## Checks that could have gone the other way

- **`laban2025lost`** asserts an ICLR 2026 Outstanding Paper Award. Confirmed on the ICLR
  blog announcement of 2026-04-23, which names it as one of two Outstanding Papers. A search
  aggregator reported it as a "Best Paper Award"; the official term is Outstanding Paper, and
  the entry uses the official term. The paper's ICLR virtual page shows no award, so the
  blog is the authority here.
- **The claim that Laban et al. find the effect "threshold-shaped rather than cumulative"**
  (`related_work_v2.tex`). The word "threshold" does not appear in their paper, so this was
  checked against the substance. Their gradual sharding experiment (Section 6) finds models
  get lost "with two-shard instructions and beyond" and that "providing all the information
  at once (1-shard) is the only effective method". The full effect appears at two shards and
  does not deepen with more. That is a threshold shape, and the characterisation holds.
- **`borisov2026yapbench`** and **`zhou2026oversight`** are 2026 preprints that postdate most
  reference lists. Both exist (arXiv:2601.00624 and arXiv:2602.04210) with author lists
  matching exactly, and both are characterised correctly in the paper: YapBench measures
  single-turn over-generation, and Zhou et al. describe users unable to articulate precise
  intent or validate complex outputs.
- **`chen2024humans`** reads "A Study on Judgement Bias" while arXiv says "Judgement Biases".
  The published EMNLP title is the singular, so the entry is right and the preprint differs.
- **`madaan2024self`** (46534--46594) and **`zheng2024judging`** (46595--46623) are adjacent
  in NeurIPS volume 36. The adjacency is real, not a transcription slip.

## Completed in this pass

Four entries were correct but incomplete. Page ranges, addresses and publishers were added
from the Anthology, and two Findings papers were changed from `@article` to `@inproceedings`,
which is what they are:

| key | change |
|-----|--------|
| `chen2024humans` | added pages 8301--8327, Miami |
| `xu2024earth` | added pages 16259--16303, Bangkok |
| `tyen2024llms` | `@article` to `@inproceedings`, `journal` to `booktitle`, pages 13894--13908 |
| `zhang2024small` | `@article` to `@inproceedings`, `journal` to `booktitle`, pages 15637--15653 |

## Known and deliberately not changed

Ten keys carry a year that differs from the entry's `year` field, because the key was made
from the preprint and the entry records the publication: `laban2025lost` (2026),
`yang2025underspecification` (2026), `singhal2023long` (2024), `wu2023style` (2025),
`wei2024simple` (2023), `zhang2024lists` (2025), `ye2024justice` (2025),
`li2024generation` (2025), `madaan2024self` (2023), `zheng2024judging` (2023). Keys do not
print and the printed years are correct. Renaming `laban2025lost` alone touches eight call
sites; it is tracked in `.workspace/TODO.md` as a cosmetic item.

`sections/related_work.tex` is the retired v1 file, is not in `main.tex`, and calls the Laban
award a "Best Paper Award". It does not build and was left alone.
