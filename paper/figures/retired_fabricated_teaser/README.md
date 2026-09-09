# Retired: the fabricated-content teaser figure

Moved here 2026-09-05. Kept for history; not part of any build.

Every file in this folder belongs to the Figure 1 that was rejected at the mentor call.
Two independent problems, both disqualifying:

1. The transcript was an invented five-turn exchange about a spring-sale email, escalating
   to author-introduced misspellings ("DEER VALLUED CUSTMER RACHELL!!"). It also showed
   four different escalating user prompts, where the study used one fixed neutral probe at
   every turn, so it depicted a harsher intervention than the design used and understated
   the paper's own result.
2. The chart's data was invented, not merely unlabelled. `build_fig1.py` hardcoded
   `quality_norm = [1.0, 0.82, 0.6, 0.35, 0.12]` and `cost_norm = [0.1, 0.32, 0.55, 0.78,
   1.0]`, normalized series chosen to produce a crossing, on an axis labelled only High and
   Low. The strapline "response quality dropped by half while token cost increased ~165%"
   was computed from them.

What replaced it: `paper/figures/gen_fig1.py`, which builds Figure 1 by reading the real
trial `s3_worker__llama-3.3-70b__quarterly_sales__run3` out of the data files at build
time, so the figure cannot drift from the analysis.

What was worth keeping and was kept: the bubble grammar, the coloured left-edge accent bar
keyed to the turn's score, the score printed in the right margin under a small grey label,
generous leading, and the restrained palette.
