# Figure 1 checked against the figure corpus

Assessed 2026-09-08 against `paper/rules/10_figures_tables.md` (22 papers) and the
extended introduction corpus in `rules/03` Part 2 (44 introductions).

## Provenance: settled, and worth stating plainly

`paper/figures/gen_fig1.py` reads trial `s3_worker__llama-3.3-70b__quarterly_sales__run3`
out of the data files at build time, so the figure cannot drift from the analysis. It
replaced a teaser whose transcript and chart series were both invented; that one is
retired with a written record at `figures/retired_fabricated_teaser/README.md`. Nothing
in the current figure is hand-entered.

## Against the twelve real-transcript conventions

| Convention (`rules/10`) | Figure 1 | |
|---|---|---|
| Name the exact checkpoint | "Llama 3.3 70B" | Present. Ten of twelve corpus papers name the checkpoint; ours names family and size, not a dated build, because the data files record `llama-3.3-70b` |
| Name the task and its source | "quarterly sales task, run 3" | Present |
| State a layout key in the caption | Bold, highlighting, and the accent bar are all declared | Present. Six of twelve do this |
| Declare elision and mark it in the figure | "Bracketed ellipses mark omissions"; `[...]` in the figure | Present, and it is the CoAuthor convention exactly |
| Evaluative annotation small, marginal, factual | Score in the right margin under a small grey label | Present |
| Show the phenomenon, not the design | One conversation degrading across five turns | Present. This is the Laban Figure 1 pattern, the closest model in the corpus |
| Preserve raw model artifacts | Text is meta-commentary-stripped, and the caption says so | Declared, so the reader knows which text is being scored |

Nothing in the checklist fails.

## The open question: does the added emphasis stay?

**Recommendation: keep it, and keep the declaration.**

The reasoning is that the highlighting marks *which span Turn 5 loses*, which is a factual
layout key rather than a verdict. `rules/10` distils the corpus rule as "the evaluative
annotation is small, marginal and factual... never a cartoon and never an adjective," and
six of twelve papers state exactly this kind of key in the caption. Marking the requested
explanations that disappear is the same move as CoAuthor colour-coding provenance.

Two things worth knowing about the disclosure. Thirteen of the 22 corpus papers contain
no provenance hedging phrase anywhere, and the declarations that do appear are for
content that is constructed or partial, not for content that is real. Our caption is
therefore more forthcoming than any paper in the sample. That is the right direction to
err given this figure's history, and it costs a clause.

## One structural finding, and it is not about the figure

The float's in-text anchor is `introduction_v2.tex:41`, a standalone eight-word paragraph
carrying a `TKTK` note. **No paragraph in either corpus is under 30 words except a list
stem.** Folding that reference into the end of paragraph 2, which is where `rules/03`
Part 1 and the outline both say the figure belongs, removes the stub and takes the
introduction from 7 paragraphs to 6, the corpus median.
