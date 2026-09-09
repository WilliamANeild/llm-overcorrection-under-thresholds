# Abstract rewrite plan

Started 2026-09-02. Working one step at a time with Liam; he writes, Claude scaffolds.

## Source material
- Current draft (v11): `paper/abstract_versions/v11_liam_2026-09-02.md` (260 words)
- In-build version (v10): `paper/abstract_versions/v10_in_build.tex`
- Calibration corpus: `paper/reference/neighbor_abstracts.md` (8 abstracts, retrieved 2026-09-02)
- Number ledger: `results_FINAL.md`

## Word budget
Field median across the 8 neighbors: 174 words. Target: 195.
Existing material must fall from 260 to ~145 to make room for ~50 words of prior work and gap.

| Beat | Now | Target |
|---|---|---|
| Opening + problem setup | 87 | 45 |
| Prior work + gap | 0 | 50 |
| Method | 34 | 30 |
| Findings | 119 | 55 |
| Close | 20 | 20 |

## Phase A. Frame decisions (blockers for everything else)
- [x] A1. Number FORMAT settled 2026-09-02 (numerals or nothing). Count still open.
- [x] A1b. ONE result statistic, settled 2026-09-02 (Liam: "i like having the one").
      The 70% asymmetry, stated as an exact percentage, carried with its domain scope.
      0.74 and 1.16 go qualitative: only 1 of 48 abstracts reports an effect in scale
      points and 0 of 48 name a rating scale.
- [ ] A1b-old. Number register: Laban (one chaperoned result %) / Sharma (no result numbers) / Madaan (one scale + one result)
  - Done when: chosen and recorded here as a constraint
  - Evidence: 6 of 8 neighbors carry no result statistic; the 2 that do use exact percentages, never spelled fractions
- [x] A2-headline settled 2026-09-02: the degradation ASYMMETRY leads; the 75% non-revision
      rate sits beside it as support, not first. Liam: "the first stat isnt really our
      headline. the second is."
- [x] A2. Gap axis SETTLED 2026-09-03: already-sufficient output.
- [ ] A2-old. Gap axis: A feedback-source / B no-error-to-find / C single-round
  - Done when: an axis is chosen, or a fourth is named
  - Note: B matches the gap already registered in paper/REVISION_PLAN.md beat 4
- [x] A3. Closing claim SETTLED 2026-09-03 (see decisions log)
- [ ] A3-old. The closing claim, stated as knowledge, in one sentence, in Liam's words
  - Done when: the claim is written here

## Phase B. Setup
- [ ] B1. Opening sentence: keep as is, or make the object of study the grammatical subject
- [ ] B2. Compress problem setup 4 sentences / 87 words to 2 sentences / ~45; strip "wasteful", "blindly", "unneeded", "properly", and the moralizing about users
- [ ] B3. Placement of the prior-work pair: after the opening (Kamoi/Huang) or after the user-problem setup as the pivot into the gap
- [ ] B4. Draft the prior-work sentence (~25 words) - blocked on: A2, B3
- [ ] B5. Draft the gap sentence (~25 words), one connective spent once - blocked on: A2, B4

## Phase C. Method and findings
- [ ] C1. Method sentence on "In this work, we"; add the 40 tasks so scope reads models x tasks; cut "put to the test" and "wasteful"
- [ ] C2. "Two honest responses" setup: keep / compress to ~12 words / move to the introduction. Costs 28 words, half the findings budget
- [ ] C3. Finding 1, the decline. Includes the correctness fix: "cosmetic edits" misstates the classifier's META class (declines and restatements) - blocked on: A1, C2
- [ ] C4. Finding 2, the quality drop; whether 0.74 appears - blocked on: A1
- [ ] C5. Finding 3, targeted feedback. "Half again as much" divides 1.16 (n=177 targeted set) by 0.74 (n=50 balanced panel). Cross-sample ratio, not a measured quantity. Restate or drop - blocked on: A1

## Phase D. Close and caveat
- [ ] D1. Meta-commentary caveat (judge first-draft preference 56% to 92% before stripping): in or out, decided explicitly
- [ ] D2. Draft the close, executing A3 as an attributed knowledge claim - blocked on: A3, C5

## Phase E. Whole-object passes
- [ ] E1. Length cut to 195 or under - blocked on: all of B, C, D
- [ ] E2. Register audit: em dashes, prose colons (3 at present), tricolons, not-X-but-Y, significance adverbs, stacked hedges, assertion verbs, sentence-length variation, no sentence-final prepositions
- [ ] E3. Coherence pass: read aloud; title, abstract and intro paragraph 1 share vocabulary; "intrinsic self-correction" and "extrinsic direction" appear
- [ ] E4. Install as v12 in paper/sections/abstract_v2.tex, rebuild PDF, archive the prior version

## Decisions log

### 2026-09-02 - Number FORMAT settled (part of A1)
Numerals or nothing. Percentages written with numerals, or the quantity stated
qualitatively with no fraction named. No spelled fractions in any form.
Evidence: across all 8 neighbor abstracts, zero spelled fractions. Laban "39%",
Madaan "~20% absolute" / "7 diverse tasks", Sharma "a non-negligible fraction of
the time" (names no fraction). Nothing else carries a proportion.
Kills from v11: "roughly two in five", "one in eight".
Still open in A1: HOW MANY numbers, which depends on the headline.

### 2026-09-02 - New analysis, not yet in the ledger
Direction of every genuine revision, computed in `.workspace/scratch/revision_direction.py`.
Same 720 trials, same GENUINE/META labels, same 6->2 recode as results_FINAL.md.
Comparison: each genuine revision's level vs the score of the most recent turn whose
content was genuinely new (LOCF over genuine content).
  Stripped, n=718:   27.7% worse / 60.2% same / 12.1% better
  Unstripped, n=718: 34.1% worse / 55.4% same / 10.4% better
  Among quality-moving revisions, stripped: 69.6% worse (199 vs 87),
    sign test p=1.48e-11, 95% CI [63.9%, 74.9%]
  Holds in every model: worse > better for all six (gemini n=8, too small alone)
  Balanced panel trial-level T1 vs T5, stripped: 52% worse / 38% same / 10% better;
    among movers 26 worse vs 5 better, p=9.61e-05
Advantage over the -0.74 cliff: uses all 718 revisions across all 6 models, needs no
balanced panel (which is 45/50 Llama and has 3 models contributing zero trials).
IF THIS REACHES THE PAPER: write it into results_FINAL.md and move the script to
scripts/study3/, per the project rule on manuscript-cited numbers.

### 2026-09-02 - Constraint on how hard the abstract can claim degradation
The blind human pairwise T1-vs-T5 study on stripped content did NOT clear its
pre-registered bar: 56.2% T1-preference among non-ties, 95% CI [45.2%, 67.1%],
bar was >=65% with CI excluding 50. Model judge on the same stripped pairs: 56.5%,
agreeing with humans at kappa 0.569. So absolute level scoring and blind pairwise
preference point different ways, and it is not a judge-reliability problem.
Consequence: the abstract can claim revision is far more likely to hurt than help.
It cannot claim the work is reliably ruined without sending a reviewer to Section 7.


### 2026-09-02 - Headline settled
LEAD: among revisions that move quality, 70% move it down (p=1.48e-11, holds in all six models).
SUPPORT, stated second: 75% of replies to a request for improvement contain no revision at all.
Rationale: the paper is about what revision does to the work, not about how often it happens.
The non-revision rate stays in because without it the reader cannot tell that most requests
produce nothing, but it is the second sentence, not the first.


### 2026-09-02 - Abstract corpus extended to 48 (agent research)
Median 178 words / 8 sentences; 28 of 48 sit at 150-200; only 3 exceed 245 (v11 is 260).
31 of 48 carry ZERO result statistics; corpus median is 0; of the 17 carrying any, 12 carry
two or fewer. Result statistics are exact percentages 40 times.
0 of 48 spelled fractions across 8,604 words. 0 of 48 closing imperatives (closers:
knowledge claim 27, resource release 11, contribution restatement 6, future work 4).
0 of 48 em dashes. 0 uses of "prove". 0 name a rating scale; 1 reports an effect in scale
points. Observation verbs beat assertion verbs 27 to 11.
v11 also rounds AWAY from the computed values: 39% -> "two in five" (40), 13% -> "one in
eight" (12.5), 1.568 -> "half again" (1.5).
The in-build v10 (180 words) sits at the corpus median on length, rhythm, move order and
closing form. Rebuild strategy: set v11's opening sentence and its "two honest responses"
move into v10's skeleton rather than starting from either draft whole.

### 2026-09-02 - Domain effect is NULL once meta-commentary is stripped
Computed in `.workspace/scratch/domain_asymmetry.py`. Same sample, same labels, same recode.
Stripped, % of quality-moving revisions that move down, by domain:
  writing 79.1 (n=118), creative 73.1 (145), code 67.0 (196), analysis 65.9 (125),
  data_logic 65.9 (134)
  chi-square across 5 domains: p = 0.555. Code vs creative Fisher p = 0.468.
  Objective (code+data_logic) 66.7% vs subjective (creative+writing) 75.8%: Fisher p = 0.151.
UNSTRIPPED the same contrast looks real: objective 71.2% vs subjective 83.9%, Fisher p = 0.019.
So the apparent objectivity gradient is a meta-commentary artifact, consistent with ledger M5
(creative shows the largest stripping shift because commentary is most prevalent there).
CONSEQUENCE: `experiment/study3_revision_yield_design.md` line 117 states as a "Key prediction"
that the overcorrection gap widens from Code to Creative on the objectivity spectrum. That
prediction is NOT supported on stripped content. This is the second registered prediction the
corrected analysis does not confirm, after the 65% reversibility bar. Report both honestly;
0 of 31 surveyed papers report any pre-registered threshold.
FOR THE ABSTRACT: no domain contrast. Uniformity is the claim, carried as a scope-fence
("across five domains"), which is what the field does with a headline statistic.
What DOES differ by domain is willingness to revise, not outcome: genuine revision rate
code 34.0%, creative 25.2%, data_logic 23.3%, analysis 21.7%, writing 20.5%.


### 2026-09-03 - RefineBench, and the gap re-cut
Verified directly from arXiv 2511.22173 (fetched 2026-09-03), not taken on an agent's word.
RefineBench: Evaluating Refinement Capability of Language Models via Checklists.
Lee, Kim, Lee, Moon, Hwang, Kim, Neubig, Welleck, Choi. Submitted 27 November 2025.
1,000 problems, 11 domains, checklist evaluation, five turns, two modes: guided refinement
(natural language feedback) and self-refinement (no guidance). Motivates itself on prior work
testing refinement on verifiable tasks while users pose open-ended queries. Finds self-refinement
barely moves frontier models (Gemini 2.5 Pro +1.8%, DeepSeek-R1 -0.1%) while guided refinement
reaches near-perfect within five turns.
Overlap with this paper: guided vs unguided, five turns, open-ended tasks, direction is what
makes revision work. Eleven months old at our deadline, CMU authors. Must be cited.
Added to paper/references.bib as lee2025refinebench.

WHAT SURVIVES, and it is the gap we now claim:
RefineBench measures whether a model can refine responses that are WRONG (baselines 31.3%, 29.1%
on hard problems). This paper measures what undirected revision does to work that is ALREADY
SUFFICIENT (87.6% of T1 outputs rated sufficient). Different question.
Also only ours: the direction asymmetry (revision actively degrades rather than merely failing to
improve); the non-revision finding (75% of replies contain no revision, requiring a validated
response classifier no corpus paper has); and the meta-commentary stripping pass (no precedent
across the 38-paper scale survey).
NO LONGER AVAILABLE as a gap: "nobody has measured unguided refinement on open-ended tasks".

### 2026-09-03 - Domain result stays out of the abstract (agent research, 47 papers)
Only 5 of 47 abstracts state a per-task difference, and in each the contrast is the paper's
central question. Of 24 papers whose main results tables ARE a full per-task breakdown, 23 keep
the aggregate in the abstract and none promotes a contrast. That is our position exactly.
Uniformity reaches the abstract nearly twice as often as difference: 9 papers, one adverb plus
the task count. "Across all evaluated tasks." "Consistently across four varied free-form
text-generation tasks." "Across six generation tasks."
For our p=0.019 becoming p=0.151 under stripping: 5 papers model the move. Convention is uniform,
report the CONTROLLED estimate as the finding, print the uncontrolled one beside it, name the
control in the same sentence. Huang prints Madaan's numbers next to his own in one table.
No paper in 47 frames a disappearing contrast or a null moderation as a limitation of its own
work, so ours does not go in Limitations either.


### 2026-09-03 - A3, the closing claim, SETTLED
"These results indicate that undirected revision lowers the quality of work that was
already sufficient, and that a single critique naming the fault reverses the effect."
26 words. Evidence as grammatical subject (20 of 27 knowledge-claim closers do this).
Observation verb. No imperative (0 of 48 close on one). Carries claim 2 (the asymmetry),
claim 1 (direction not capacity), and the already-sufficient gap axis.
Liam ranked the themes: land on 2 and 1, with a little of 6 (first draft is the peak)
and 10 (the damage is hard to see). 6 and 10 go in the findings sentences above the
close, not inside it.
PRECISION NOTE: the targeted-feedback result is a paired comparison of a critique-driven
revision against the model's own undirected revision at the next turn (n=177, +1.16
stripped, p=5.7e-19). "Reverses the effect" compresses a direction that flips from down
to up; the exact claim is the paired comparison, not a reversal of the whole trajectory.

PHASE A COMPLETE. A1 format (numerals or nothing), A1b count (one result statistic, the
70%), A2 gap axis (already-sufficient output), A3 close (above).


### 2026-09-03 - v12 drafted sentence by sentence, installed, built
Nine sentences settled one at a time with Liam. Full text in
paper/abstract_versions/v12_draft.txt and installed at paper/sections/abstract_v2.tex.
Superseded v10 saved at paper/abstract_versions/v10_superseded_2026-09-03.tex.
210 words / 9 sentences / 23.3 words per sentence (corpus mean 23.2).
E2 REGISTER AUDIT PASSED: 0 em dashes, 0 colons, 0 semicolons, 0 spelled fractions,
0 assertion verbs, 0 significance adverbs, 0 not-X-but-Y, 0 imperatives, 1 result
statistic (70%), 2 observation verbs, 2 hedges (largely, slightly), no sentence-final
preposition, sentence lengths 13/29/29/23/29/20/18/23/26.
STILL OPEN:
  E1 - a 12-word trim to 198 is drafted and NOT applied. 210 sits above the 150-200 band
       holding 28 of 48 corpus abstracts. Trim: S2 "what is wrong with it" -> "what is
       wrong" (-3); S3 cut "largely" (-1); S5 "and contrast requests that name no fault
       with" -> "contrasting undirected requests with" (-4); S8 "to the final version" ->
       "to the last" (-1); S9 drop "a single critique" (-3, also removes the third use of
       "critique" in 210 words).
  E3 - the title's terms are not echoed in the abstract. Blocked on the title decision,
       which is still open across the ten candidates.
Build: tectonic, 16 pages, 0 undefined references. PDF copied to
~/Desktop/"Neild - Undirected Revision - 2026-09-03.pdf" for Tania.


### 2026-09-03 - TITLE CHANGED
FROM: Intrinsic Self-Correction Requires Extrinsic Direction
TO:   Worse on Request, Better on Critique: Self-Correction on Work That Is Already Sufficient
Set in paper/main.tex. Full candidate history in paper/title_versions.md.
Reasons the old title went: "Requires" is unbounded where every negative title in the
54-title corpus bounds its claim; "extrinsic direction" returns 1 arXiv record total (a 2018
graphene physics paper); and neither half was echoed anywhere in the abstract.
E3 SATISFIED: abstract echo is critique x2, request x2, sufficient x2, self-correction x1.

OPEN, needs Liam's hand, not mine:
  introduction_v2.tex:82 still closes on the retired title: "Intrinsic self-correction, on
  its own, is not enough; it requires extrinsic direction." That sentence was written to earn
  a title that no longer exists and now points at nothing. It is prose, so he rewrites it.


### 2026-09-04 - v13 installed after Tania's feedback
Tania returned three full rewrites rather than the comprehension read that was asked for,
having first scanned nine 2026 ACL/EACL/ICML abstracts. Feedback and analysis:
`.workspace/notes/abstract_feedback_tania_2026-09-03.md`. Her sources fetched verbatim to
`paper/reference/acl2026_abstracts.json`.

HER SOURCES SETTLE THREE THINGS (median of 9: 169 words, 7 sentences, 1 percentage):
  - p-values are OUT. 0 of 9 ACL 2026 sources carry one; 0 of 48 in the arXiv corpus.
    Her own drafts carry two each.
  - Length: her sources' median is 169. Her drafts run 244/315/250. Ours is closer to her
    stated target than hers are.
  - Percentages: the arXiv corpus (31 of 48 with none) UNDERSTATED our venue. 5 of 9 ACL
    2026 abstracts carry at least one, median 1, max 9. The A1b one-statistic decision
    stands and is better supported than before.

TAKEN: her opening question, merged so the user-side framing survives in sentence 2 at a
cost of 3 words rather than 12. Ali's positioning objection outranks a better hook.
DECLINED: "the revision tax" (the abstract mentions no cost anywhere, and one-statistic
discipline means it would arrive unsupported; it stays in ledger Section 6) and
"a choice single-turn benchmarks never test" (shifts the gap toward multi-turn, which is
RefineBench's ground; our gap survives only on the already-sufficient axis).
FIXED: "cannot" appeared 4 times in 200 words; sentence 2 reverts to "could not do
themselves" and "unable to name", and sentence 3 takes her tighter "with a specific
critique".

STILL OPEN: no comprehension read. She rewrote instead of reporting what she understood,
so we still have no evidence about whether the abstract lands on a first reading.
