# Introduction writing map

Written 2026-09-08. Targets from `paper/rules/03_introduction.md` Part 2 (ACL-family,
n = 25). Number selection from `paper/reference/intro_number_selection.md`. Figure
decision from `paper/reference/fig1_corpus_check.md`.

**Liam writes the prose.** This is the frame, the budget and the grounding.

## Where the draft stands

996 words, 7 paragraphs, 13 citation references, 4 in paragraph 1. Over the ACL-family
maximum (862) on length and below p25 on both citation measures.

## Target: 700 words, 6 paragraphs, 20-22 citation references

700 sits between the ACL-family median (658) and p75 (768), which is the right place for
a paper carrying three studies. Six paragraphs is the median. The two moves are
independent: **cut roughly 300 words, and add 7 to 9 citation references**, most of which
come from converting single citations to groups rather than adding sentences.

| ¶ | Beat | Now | Target | Cites now → target | What changes |
|---|---|---|---|---|---|
| 1 | Field | 157w, 4c | **110w**, **9c** | 4 → 9 | Add a group of benchmark papers to the single-turn-evaluation claim and a group to the collaborative-deployment claim, in the HALIE manner. The opener stays copular; 0 of 44 introductions open on a question, so the abstract's question does not migrate here |
| 2 | Problem, ending on the figure | 185w + 8w stub, 3c | **130w**, **4c** | 3 → 4 | Absorb the eight-word figure stub at line 41. No paragraph in either corpus is under 30 words except a list stem. This alone takes 7 paragraphs to 6. Cut the theatrical closer ("where the collaboration quietly fails") |
| 3 | Prior work | 150w, 4c | **125w**, **6c** | 4 → 6 | Keep the dialectic (Madaan, Huang, Kamoi, Laban); `rules/03` Part 1 rates it at corpus standard. Add the two or three multi-turn works the gap paragraph characterizes but does not cite |
| 4 | Gap | 147w, 2c | **100w**, **3c** | 2 → 3 | Keep the fence-then-consequence construction, rated one of the better gap paragraphs measured. Tighten only |
| 5 | Approach | 138w, 0c | **95w**, **0c** | 0 | Design, three RQs, stripping, human validation. Zero citations is on target |
| 6 | Results | 223w, 0c | **140w**, **0c** | 0 | The big cut, 83 words. Carries the four numbers below. The judge-bias finding becomes a clause without figures. **The practical recommendation moves to the Discussion**, per `rules/03` Part 1 item 4 |

Totals: 700 words, 22 citation references, 9 in paragraph 1, 0 in the last two.

## The four numbers, and where each lands

All in paragraph 6, each chaperoned by a referent and a comparison, which is the one rule
the corpus never breaks.

1. **88% of first drafts are already sufficient** (87.6%, 631 of 720; `results_FINAL.md`
   line 125). The premise. Without it the reader does not know the work being revised was
   fine.
2. **70% of quality-moving revisions make it worse** (69.6%, 199 down against 87 up among
   286 movers; line 155). The headline, and its comparison is inside it.
3. **27% of revisions to sufficient work leave it insufficient** (27.5%, 113 of 411;
   line 218). The cost.
4. **Blind readers show no reliable preference** (56.2%, 41 of 73, interval includes
   chance; line 371). What keeps claim 2 honest.

Stated as clauses, without figures: the 39%-to-13% decline, the targeted-critique
reversal (direction only, since rating-scale levels are the form the corpus avoids), and
the judge-bias artifact.

## Refinements from the Emami corpus (added 2026-09-08)

Measured in `paper/reference/emami_writing_patterns.md`, n = 24 of his introductions.

- **Length matters more than it looked.** His median introduction is 583 words, below the
  venue's 658. The 700-word target above is already above his median; do not drift up.
- **The citation gap is mostly a length gap.** His median is 14 references, and our draft
  already has 13. At 996 words that reads as 1.3 per 100; the same 13 at 700 words is 1.9,
  and **18 references at 700 words is 2.6, which is his median density**. Revise the
  citation target from 20-22 down to **18**, since 22 would put us above his practice.
- **Keep the opener.** `rules/03` Part 1 item 5 called our 10-word opening a stylistic
  fragment with no analogue in 23 papers. Against his own 24 it has four analogues and
  sits in a form he uses at roughly twice the venue rate. That criticism is withdrawn.
- **The figure reference is right.** He references a figure in 20 of 24 introductions
  (83%) against 61% for the venue, so paragraph 2 ending on Figure 1 matches him closely.

Revised citation line: P1 8, P2 3, P3 5, P4 2, P5 0, P6 0 = **18**.

## What this settles from the reconciliation note

The three open questions in `.workspace/notes/intro_abstract_reconciliation.md` resolve
as: 39→13 stays as a clause without digits, the blind-reader null enters, and the
meta-commentary artifact stays but loses its numbers and its headline position.

## Sequence

1. Fold the figure stub into paragraph 2 (7 paragraphs → 6).
2. Cut paragraph 6 to 140 words, moving the recommendation to the Discussion.
3. Trim paragraphs 1, 2, 4 and 5 to budget.
4. Add citation groups to paragraphs 1 and 3.
5. Re-measure with `scripts/introduction_corpus/03_analyse.py` conventions.
