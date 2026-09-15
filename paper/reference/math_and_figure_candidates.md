# Formalization and figure candidates

Compiled 2026-09-10. Every quantity below is computed from the data files, and each entry
says whether it is already in `results_FINAL.md` or is new.

## What the corpus carries, so we know where we stand

Counted over the 69 cached papers, body only, bibliography excluded.

| | p25 | Median | p75 | Max | Zero |
|---|---:|---:|---:|---:|---:|
| Display equations, whole corpus | 0 | **2** | 9 | 26 | **41% have none** |
| Display equations, Ali Emami (n=24) | 0 | **2.5** | 10 | 22 | 33% have none |
| Inline math expressions, corpus | 19 | 46 | 96 | 285 | |

**Ours: 0 display equations.** Two to four would put us at the median. That is the honest
size of the gap, and it is worth saying plainly that 41% of these papers carry no display
mathematics at all, so quantity of notation is not what makes a paper read as serious. The
case for adding formalization here is that the advisor asked for it, a draft already
exists at `sections/_formalization_variants.tex` (not inputted anywhere), and the paper
currently defines the revision tax only inside a table caption.

---

## Part 1: formalization the data supports

**M1 and M2 already drafted** in `_formalization_variants.tex`, Variant A: the turn index
$i$, expected quality $Q_m(i)$, the stopping point $i^{*}_m = \arg\max_i Q_m(i)$ with the
finding $i^{*}_m = 1$ for every model, and the cliff $Q_m(1) - Q_m(5)$. Ready to install.

**M3, the revision tax, currently has no definition in the body.** It is given only in
`tab:revision-tax`'s caption. As a display equation it becomes citable:

    Tax_m   = sum over i > i*  T_m(i)  /  sum over i <= i*  T_m(i)
    Waste_m = sum over i > i*  T_m(i)  /  sum over all i    T_m(i)

where $T_m(i)$ is output tokens. Aggregate values 164.2% and 62.1% are already in the ledger.

**M4 is new, and it is the strongest of the four.** The paper's thesis stated as one
estimable quantity: the expected change in quality from a single undirected revision,
conditioned on the quality of the input being revised.

| Input level | n | E[change] | P(down) | P(up) |
|---:|---:|---:|---:|---:|
| 2 | 116 | **+0.69** | 0.00 | 0.35 |
| 3 | 77 | −0.03 | 0.30 | 0.27 |
| 4 | 394 | −0.43 | 0.28 | 0.06 |
| 5 | 130 | **−0.98** | 0.49 | 0.00 |
| **input insufficient (<4)** | 194 | **+0.41** | | |
| **input sufficient (>=4)** | 524 | **−0.56** | | |

The sign of the expected change flips at the sufficiency threshold, and the effect is
monotone in input quality: the better the work, the more revision costs. That is the whole
paper in one line, and stated formally it is

    E[ Q(i+1) - Q(i) | Q(i) < 4 ]  = +0.41
    E[ Q(i+1) - Q(i) | Q(i) >= 4 ] = -0.56

**Three cautions on M4, and they are not small.** It is a **new analysis**, run today; it
appears nowhere in `results_FINAL.md`. It is **post-hoc**, not among the registered
predictions. And it conditions on a judge-assigned level, so it inherits that judge's
error. Using it means adding it to the ledger with its filter, deciding how to report a
post-hoc result, and saying in print that it was not pre-registered.

---

## Part 2: figures the data supports

Each was checked for whether the data actually exists.

**G1. Quality transition matrix.** 718 genuine revisions, input level against output level,
15 of 25 cells populated. As a heatmap or an alluvial diagram this shows the 199/432/87
split, the 411-to-113 outcome, and M4's gradient in one object. From level 4: 258 stay, 80
fall to 2, 32 to 3, 24 rise to 5. **Verified available.**

**G2. Model by domain grid.** Revision rate across 6 models and 5 domains. **Every one of
the 30 cells holds exactly 96 observations**, which is as clean as a heatmap ever gets and
means no cell needs a caveat. **Verified available.**

**G3. Paired judge slope, stripped against unstripped.** 3,600 paired observations. This is
§8, the meta-wrapping asymmetry, which the Discussion calls the paper's methods
contribution and which currently has no body float at all. A slope chart or a
scatter with the identity line makes a two-directional bias visible in a way no sentence
does. **Verified available.**

**G4. M4 as a figure.** Expected change against input level, with a zero line. Four points,
a crossing, and error bars. Visually simple, argumentatively the densest thing available.
Blocked on the M4 decision above.

**G5. Three table-to-figure conversions**, from `figure_census_and_gaps.md`:
`tab:direction` to a dot plot, `tab:revision-tax` to ranked bars, `tab:targeted-per-model`
to per-model dumbbells. These add no new analysis and move us from 3 figures and 9 tables
to 6 and 6, against a corpus median of 5 figures and a ratio of 1.25.

---

## The constraint that decides all of this

The body runs to roughly page 12 against ARR's 8-page limit. Figures cost more space than
the tables they replace, and equations cost lines. Nothing here should be installed before
the page cut is planned, because the cut may itself be served by converting tables to
figures that compress better, or may rule out additions entirely.

## One thing worth saying plainly

Complexity that carries information earns its space, and by that measure we are genuinely
short: no display equations against a median of 2, and 3 body figures against a median of
5. Complexity that only looks complex is the thing a referee is trained to find, and the
corpus is evidence it is not expected of us either, since 41% of these papers carry no
display mathematics at all. Every candidate above is on the first list. G2 and G3 happen to
be the most visually elaborate and are also the two best supported by data.
