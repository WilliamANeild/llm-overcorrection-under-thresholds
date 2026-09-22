# Consistency audit: the paper against the Overdone-at-3 decision

Run 2026-09-22 after the construct decision recorded in `results_FINAL.md` section 20.
Every quantity the paper prints was recomputed under both codings, changing nothing else.
The published coding reproduces exactly in all cases, including Table 13 to three decimals,
which is the check on the reconstruction.

**Headline: less changes than you would expect. Every count survives untouched. Only the
ordinal magnitudes move.**

---

## Survives unchanged, no edit needed

These do not involve level 6's rank, because "sufficient" means level 4 or above and Overdone
is below it under either coding.

| Quantity | Value | Prints at |
|---|---|---|
| First drafts sufficient | 87.6%, 631/720 | `abstract_v2:34`, `introduction_v2:73`, `results_v2:100` |
| Revision-despite-sufficiency | 39.6%, 411/1,038 | `results_v2:102` |
| Sufficient-input revisions ending below | 27.5%, 144/524 | `abstract_v2:34`, `results_v2:58` |
| Input split for revision direction | 524 sufficient, 194 insufficient, 718 total | `results_v2` |
| Meta-response share at Turn 5 | 86.7% | `introduction_v2`, `results_v2` |
| Post-Turn-1 meta share | 75% | `conclusion:3` |
| Genuine-revision rate by turn | 39.3 / 25.7 / 21.4 / 13.3% | Table 2 |
| **All six STET scores** | 97.8 / 96.3 / 82.3 / 68.4 / 54.1 / 18.4% | Table 4 |
| Split-half and generalizability | rho 0.972, G 0.992, 3.2x | `results_v2` 4.6 |

The STET table is the one worth noting: the score is a count of whether a model revised
sufficient work, so it is completely insensitive to this decision. The paper's named artifact
does not move.

## Moves slightly, one digit

| Quantity | Published | Decided | Prints at |
|---|---:|---:|---|
| Of revisions that move quality, share down | 69.6% (199/286) | 68.7% (184/268) | `results_v2:57` |
| Same, rounded in prose | "70%" | rounds to 69% | `abstract_v2:34`, `introduction_v2:76` |
| Targeted-feedback gain | +1.16, p 5.7e-19 | **+1.01, p 1.9e-19** | `results_v2`, abstract, `conclusion` |

The targeted-feedback result is robust: the gain shrinks by 0.15 and the p-value improves.

## Changes materially

| Quantity | Published | Decided | Prints at |
|---|---:|---:|---|
| Balanced-panel cliff | **-0.74**, p 1.01e-4 | **-0.38**, p 4.42e-3 | `introduction_v2:77`, `results_v2:72`, Fig 3 caption `results_v2:89`, `results_v2:122`, `conclusion:3`, `appendix:208` |
| Llama-only cliff | -0.67, p 3.76e-4 | **-0.31**, p 1.80e-2 | `results_v2:74` |
| Pooled trajectory | 4.11 to 3.07, -1.04 | **4.17 to 3.42, -0.75** | `results_v2:80`, Fig 3 caption, `appendix:345` |
| Panel T1 and T5 means | 3.66 and 2.92 | **3.70 and 3.32** | `results_v2:72`, Fig 3 caption |

### Per-domain, Table 13 (`appendix:360-364`)

| Domain | Published | Decided | n |
|---|---:|---:|---:|
| analysis | -0.94, p 0.003 | -0.59, p 0.004 | 17 |
| code | -0.93, p 0.003 | -0.47, p 0.035 | 30 |
| creative | -0.58, p 0.031 | -0.32, p 0.058 | 19 |
| data_logic | -0.53, p 0.058 | -0.24, p 0.206 | 17 |
| writing | -0.77, p 0.008 | **-0.77, p 0.004** | 13 |

All five stay negative. **Significance drops from four of five to three of five**, so the
sentence at `results_v2` reading "four of five reach significance" must change to three, and
`data_logic` moves from marginal to null.

## Not yet verified, must be before any claim

**The revision tax.** `t* = 1` for all six models (`results_v2:161`), 62.1% of tokens past
`t*` (`introduction_v2:78`, `results_v2:161`, `conclusion:3`), and 164.2% measured against
tokens to reach `t*` (`results_v2:163`). All three rest on quality declining across turns. A
raw-argmax proxy suggests `t*` moves later under the decided coding, but the paper uses
`compute_cary` with a token penalty and I have not run it. **Do not restate or defend these
numbers until `compute_cary` has been rerun.** Note separately that `analyze.py:1559` uses
C = 5e-7 where the plan records C = 1e-4.

**The unstripped panel cliff** of -0.94 (`results_v2:72`, `appendix:208`) was not recomputed;
the unstripped evaluator output assigns level 6 at 5.7% of Turn 1 rising to 14.9% at Turn 2,
so it will move too.

**Figures.** Figure 3 (quality trajectory) and Table 12 (pooled mean by turn) are generated
from the recoded scores and must be regenerated.

## Framing: three places the new reading is stronger, not weaker

1. `results_v2:122` currently concedes that "the drop of 0.74 levels is not large enough to
   reverse a blind pairwise preference." Under the decided reading this stops being a
   concession and becomes the mechanism: the later drafts are not worse-looking, they are
   bloated, which is why readers cannot pick the first draft.
2. Limitations item 8 concedes that "the degradation we measure is not one a reader reliably
   notices." Same move: now explained rather than admitted.
3. Section 19b, where human raters scored judge-Overdone items highest at 5.33, stops being
   evidence against the paper and becomes evidence for the mechanism. Those outputs read well;
   they have drifted from the ask.

Figure 1 is already the clean illustration: the model dropped the explanations the prompt
requested and added generic recommendations.

## What has to be decided before editing

- Whether the headline becomes the two-failure-mode result (19 of 50 became overdone,
  p 4.01e-5, while the share below sufficiency did not significantly change) with the ordinal
  -0.38 as support, or stays an ordinal claim at -0.38.
- Whether "Worse on Request" survives as the title.

Neither is settled, and nothing in the manuscript has been edited.
