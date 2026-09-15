# Figures: what the corpus does, what we have, and what our findings could support

Compiled 2026-09-10. Corpus counts are by script over the 69 cached papers at
`.workspace/reference/intro_corpus/html/`, via
`scripts/introduction_corpus/05_figure_census.py`. Body and back matter are split at the
bibliography, so appendix floats are not counted as body floats. Subfigure panels are not
counted separately from their parent.

---

## 1. How many floats a paper of this kind carries

| | p25 | **Median** | p75 | Max |
|---|---:|---:|---:|---:|
| **Body figures**, whole corpus (n=69) | 3 | **5** | 6 | 14 |
| **Body tables**, whole corpus | 3 | **4** | 6 | 10 |
| Body figures, Ali Emami (n=24) | 4 | **5** | 6 | 9 |
| Body tables, Ali Emami | 3 | **4** | 5 | 9 |
| Appendix figures, whole corpus | 1 | 5 | 8 | 38 |
| Appendix tables, whole corpus | 2 | 6 | 11 | 41 |

**Body figures per body table: median 1.25**, in both the whole corpus and Emami's own.
**Body floats combined: median 9** (Emami 10).

## 2. Where we sit

| | Ours | Corpus | |
|---|---:|---:|---|
| Body figures | **3** | median 5 | **29th percentile** |
| Body tables | **9** | median 4 | at p75+, corpus max is 10 |
| **Figures per table** | **0.33** | **1.25** | about a quarter of normal |
| Body floats combined | 12 | median 9 | above median |
| Appendix figures / tables | 4 / 6 | 5 / 6 | normal |

**The problem is not that we have too few floats. It is the mix.** We carry roughly the
normal amount of evidence and present almost all of it as tables. Three figures against
nine tables is the inverse of every comparison group measured.

## 3. Caption length

| | p25 | Median | p75 | p90 |
|---|---:|---:|---:|---:|
| Corpus figure captions (n=717) | 8 | **16** | 36 | 57 |
| Corpus table captions (n=818) | 10 | **22** | 36 | 61 |

Ours: figure captions median 22, table captions median 28. Both run long, and Figure 1 at
146 words is far outside anything measured. That is a known and accepted cost of its
provenance declarations, but it should not become the house style for new figures.

## 4. Findings with no float in the body at all

Read against `results_FINAL.md`. Each of these is asserted in prose and shown nowhere.

| Ledger | Finding | Status |
|---|---|---|
| **§8** | **Meta-wrapping asymmetry.** 84% of revision outputs carry a wrapper against 14% of first drafts, and it moves an automated judge from 56.5% to 91.8% preference for the first draft | **No body float.** The Discussion calls this the paper's methods contribution and it is invisible |
| **§7** | **Human reversibility.** 56.2% first-draft preference, 41 of 73, interval includes chance, pre-registered 65% bar not cleared | **No body float.** Appendix tables only. This is the honesty check on the whole degradation claim |
| §4 | Revision despite sufficiency, 39.2% of sufficient turns get revised anyway | **No float** |
| §4b | Outcome when the input was already sufficient: 411 revisions, 298 stay sufficient, 113 fall below | No float; the number appears in prose |

§8 is the strongest candidate in the paper. It is a two-directional bias, which is exactly
what a figure shows and a sentence does not.

## 5. Tables that would carry better as figures

| Table | What it holds | Why a figure |
|---|---|---|
| `tab:direction` | 6 model rows and 5 domain rows, each an n, a % down, and a p | Eleven rows of one quantity. A dot plot with a reference line at 50% reads instantly; the table does not |
| `tab:revision-tax` | 6 models, tax %, waste %, $/task | Ranked bars. The 30.6% to 436% spread is the point and a table flattens it |
| `tab:targeted-per-model` | per-model targeted vs generic | A dumbbell per model. This is the figure cut earlier as Figure 4, which was weak only because it was pooled to a single pair |

Converting these three would take us from 3 figures and 9 tables to **6 and 6**, which is
the corpus median for figures and puts the ratio at 1.00 against a median of 1.25.

## 6. Standards any new figure inherits

From `rules/10_figures_tables.md` and the Figure 1 work:

- Helvetica throughout, matching Figure 1; no Apple system UI font
- No in-figure title. The caption carries it. This was a defect in Figures 2 and 3
- Legend outside the data area, or direct end-of-line labels
- Rendered at print width (3.17in single column) so type is not resampled
- Included as PDF, never PNG
- Axis limits must contain the data. Figure 2 was clipping Llama at 90% against a 72% cap
- Colour encodes one thing only; black is structure, colour is data
- Every number computed at build time from the data files, never hand-entered
- Caption at or under about 57 words, the corpus p90, unless declarations require more

## 7. What this does not settle

Whether the body has room. The paper currently runs to about page 12 against ARR's
8-page limit, and figures cost more space than the tables they would replace. Any figure
programme has to be decided together with the page cut, not before it.
