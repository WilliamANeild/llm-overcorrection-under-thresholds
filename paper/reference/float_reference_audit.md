# Floats that no text points to

Audited 2026-09-08 across every file `paper/main.tex` inputs.

**10 of the 23 floats in the live build are never referenced in any section.** Three are
in Results, seven in the Appendix.

| Label | Type | Defined in | Referenced |
|---|---|---|---|
| `fig:survival-curves` | figure | results_v2 | **never** |
| `fig:quality-trajectory` | figure | results_v2 | **never** |
| `fig:targeted-dumbbell` | figure | results_v2 | **never** |
| `tab:regression` | table | appendix | **never** |
| `fig:pipeline` | figure* | appendix | **never** |
| `fig:probe-cliff` | figure | appendix | **never** |
| `fig:threshold-ladder` | figure | appendix | **never** |
| `fig:dose-response` | figure | appendix | **never** |
| `tab:pairwise`, `tab:judge-calibration`, `tab:human-agreement`, `tab:irr`, `tab:irr-momentum` | tables | appendix | **never** |

Everything else (`fig:teaser`, and every table in methods and results) is referenced.

## Why this is the flow problem, not a formatting nit

Each of the three results figures sits inside the subsection it belongs to, so placement
is already right. What is missing is the sentence that points at it. Two consequences:

1. **LaTeX float placement becomes arbitrary.** With no `\\ref`, there is nothing tying
   the float to a position in the argument, and the figure can drift pages from the
   prose it illustrates.
2. **A reader has no instruction to look.** In the figure corpus (`rules/10`), every
   displayed figure is pointed at from the text; the convention is universal in the 22
   papers surveyed.

## The three results figures, and what each would carry

- `fig:survival-curves` in "Models Mostly Decline to Revise" shows per-model
  genuine-revision survival across turns. This is the natural home for the 39%-to-13%
  trajectory that the writing map moves out of the introduction: the figure can carry it
  so the prose does not have to.
- `fig:quality-trajectory` in "Quality Degrades Under Undirected Revision" shows the
  balanced panel against the pooled series. It is the visual form of the paper's central
  claim and currently no sentence sends the reader to it.
- `fig:targeted-dumbbell` in "Targeted Feedback Restores Quality" shows generic against
  targeted. It is the reversal the title rests on.

## Recommendation

Add one in-text reference per figure, in the paragraph that states the finding the figure
shows. For the appendix floats, either reference them from the appendix prose or drop the
ones nothing needs; seven unreferenced appendix floats is also page budget in a
page-limited submission.
