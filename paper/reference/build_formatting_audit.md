# What the built PDF actually looks like

Audited 2026-09-08 by building with `tectonic` and reading the rendered pages, not by
reading the source. Build: `paper/builds/main.pdf`, 19 pages.

## 1. Page budget: over by about four pages

The body runs to page 12 at least; the Conclusion (section 7) begins on page 12 and
continues onto 13. ARR allows **8 pages of body** for a long paper, with Limitations,
references and appendices outside the limit.

This is the largest single problem in the build and nothing else on this list competes
with it.

## 2. Table 4 overflows its column and prints across Table 5

`results_v2.tex:114-122` produces **Overfull \hbox, 132.5pt too wide**, in a column of
roughly 230pt. On page 9 the two tables interleave: the header band reads
"Stripped (Unstripped) Turn Stripped (Mean share Unstripped) Shift n", which is Table 4
and Table 5 printed over each other. A reader cannot parse either.

Two further tables overflow: `results_v2.tex:204-212` by 85.7pt, and
`results_v2.tex:171-182` by 17.2pt.

## 3. The three results figures fail conventions the teaser now meets

Figures 2, 3 and 4 (`fig:survival-curves`, `fig:quality-trajectory`,
`fig:targeted-dumbbell`) share four problems:

- **A bold in-figure title duplicating the caption.** "Per-model genuine-revision
  survival", "Quality trajectory under undirected revision", "Targeted feedback restores
  quality" each appear twice on the page, once inside the image and once as the caption's
  opening. No figure in the corpus does this; captions carry the title.
- **The x-axis label collides with the tick labels.** In Figures 2 and 3 "Turn" overlaps
  the "T1 T2 T3 T4 T5" row.
- **The legend sits inside the plot area, over the data.** Ali's figures either put the
  legend outside at the top or label the lines directly at their ends, which is what
  Figure 1 now does.
- **None of the three is referenced from the text** (see `float_reference_audit.md`), so
  they are both malformed and unpointed.

Figure 4 has a further problem: it is a single dumbbell on an otherwise empty axis, using
a full column for two points and one number.

## 4. Figure 1, after the redesign, against Ali's own

| | Figure 1 | Ali's chart-plus-examples figure |
|---|---|---|
| Chart share of height | **34%** | ~55% |
| Direct end-of-line labels | yes | yes |
| Legend inside the plot | no | no |
| In-figure title | no | no |
| Example boxes | plain 1px border, no fill | plain border, no fill |
| Accent bars, badges, rounded cards | none | none |

The remaining gap is proportion: his chart carries more than half the figure, ours a
third. Raising it further means cutting transcript height, which trades the qualitative
evidence for the quantitative.

## What to fix, in order

1. Cut the body to 8 pages. Everything else is cosmetic beside this.
2. Fix the three overfull tables, starting with Table 4.
3. Strip the in-figure titles, move the legends out, fix the axis-label collisions.
4. Add the missing in-text references, or drop the figures that nothing needs. Cutting
   Figure 4 would serve both this and the page budget.
