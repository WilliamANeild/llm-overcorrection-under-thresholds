# Introduction / abstract reconciliation

Written 2026-09-08, after the abstract was finalized. Every number below was checked
against `results_FINAL.md` on 2026-09-08. Nothing here is a correction: both documents
carry verified figures. The gap is editorial, about which findings lead the paper.

Liam writes the prose. This file is the audit and the grounding, not a draft.

## The two documents currently lead on different findings

The abstract's results run S5 to S7. The introduction's results paragraph is
`paper/sections/introduction_v2.tex:92-101`.

| # | Abstract leads on | In the introduction? | Ledger |
|---|---|---|---|
| 1 | First drafts sufficient in 88% of trials | **Absent** | 87.6%, 631/720, line 125 |
| 2 | Most replies contain no revision at all | Present, but as a trajectory: 39% at T2 falling to 13% at T5 | pooled 2,162/2,880 = 75.1%, line 10; trajectory 283/720 and 96/720, lines 106 and 109 |
| 3 | Revisions that change quality make it worse 70% of the time | Present qualitatively, "the output tends to get worse". No figure | 69.6%, 199 down against 87 up of 286 movers, line 155 |
| 4 | Where the work was already sufficient, 27% leave it insufficient | **Absent** | 27.5%, 113 of 411, line 218 |
| 5 | For every model the first draft rates highest | Present, "the quality-maximizing stopping point is the first turn" | t* = T1 for all six, line 289 |
| 6 | Blind readers show no reliable preference between first and last | **Absent** | 56.2%, 41/73 non-tie, line 371; interval stated in `methods.tex` and includes 50% |
| 7 | Naming the fault reverses the effect | Present, "a single specific critique reverses the decline" | +1.16 stripped, n=177 |

Drift runs both ways. The introduction also leads on two things the final abstract
dropped:

- **The 39% to 13% trajectory.** The abstract states the same phenomenon as a pooled
  rate instead. Both are verified; they are different cuts of the same labels.
- **The meta-commentary measurement artifact.** The introduction gives it a full clause
  ("biases an automated judge in two opposing directions at once"). The abstract carries
  no measurement-confound beat at all. The abstract's "restating the draft or declining
  while presenting it as compliance" is the model behaviour, not the judge artifact.

## Three decisions, all Liam's

1. **Does the introduction adopt the abstract's three percentages (88, 70, 27), or keep
   leading on 39 to 13?** The abstract dropped the trajectory for the pooled statement.
   If the introduction keeps it, the paper opens on two different cuts of the same data
   in consecutive paragraphs.
2. **Do the two absent findings (27% and the blind-reader null) enter the introduction?**
   The blind-reader result is the one that keeps the degradation claim honest; it is in
   the abstract and in the results, and currently skipped in the introduction.
3. **Does the meta-commentary artifact stay a headline in the introduction** when the
   abstract no longer raises it? Keeping it is defensible, since the introduction has
   room the abstract does not.

## Not in scope here

The introduction's field, problem, prior-work and gap beats were not audited against the
abstract, because the abstract's setup did not change in the final pass. Beats 1 to 4 of
`introduction_v2.tex` are untouched by this.

The `TKTK` placeholder at `introduction_v2.tex:35-41` (the Figure 1 in-text reference) is
a separate open item and is not part of this reconciliation.
