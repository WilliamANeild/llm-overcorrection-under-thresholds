# TODO

Deadline: ARR October 12, 2026 (confirmed 2026-09-02). Liam's own target for a finished
version is September 28, 2026. Six weeks from today.

Dependency chain: abstract (DONE 2026-09-08) -> introduction -> Figure 1 ->
methods/discussion/conclusion -> ARR submission mechanics (anonymise, page limit,
checklist). The introduction is now the head of the chain.

## Pending

- [ ] Resolve two discrepancies exposed by recomputing the stripped cliff — added 2026-09-07
  - **Done when:** the paper states which N the effect size divides by, and Table 3 no longer mixes two rescore bases
  - The p-values are VERIFIED: 1.01e-4 and 3.76e-4 both reproduce exactly, and are now recorded in `results_FINAL.md`
  - r: paper prints 0.55 and 0.53; recomputation gives 0.536/0.514 dividing by N=trials, or 0.681/0.652 dividing by N=non-zero differences. Printed values match neither
  - Llama delta: paper prints -0.69 from the 50-pair rescore; the full 3,600-output rescore gives -0.67. Table 3 mixes the two bases in one table

- [ ] Rewrite the §4b direction-analysis prose in your own voice — added 2026-09-06, rescoped 2026-09-08
  - **Done when:** the `TKTK Liam` comment block above `paper/sections/results_v2.tex:63` is gone and the paragraph reads in your register
  - RESCOPED 2026-09-08: the reporting gap is closed. `results_v2.tex:63-72` now carries 199 down against 87 up among 286 movers, 69.6%, exact binomial 95% CI [63.9%, 74.9%], sign test p = 1.48e-11, the 411/113 (27.5%) sufficiency result, the per-model and per-domain table, and the unstripped 76.6% beside it. `methods.tex:82-84` defines the baseline as the most recent turn with genuinely new content
  - What remains is voice only: the paragraph carries a `TKTK` note saying the statistical scaffolding was written to match the surrounding register and asks you to rewrite it without changing the numbers
  - The stale note on this item claimed the analysis was absent from the body. That was true on 2026-09-07 and is not true now
- [ ] Work through the remaining claim-audit findings sentence by sentence — added 2026-09-05
  - **Done when:** every one of the 36 flagged claim-source pairs is either corrected in the prose, re-cited, or deliberately left with a recorded reason
  - Consolidated list: `paper/reference/claim_audit_SUMMARY.md`. Per-pair evidence in `claim_audit_chunk1-4.md`
  - DONE so far: the Laban accumulation claim, which appeared in four sentences across the introduction and related work
  - Highest remaining severity: the four sentences with no surviving support (vendor guidance; judges favouring confident framing; multi-turn coherence degrading with length; enterprise spending), then the four remaining Class A cases where the cited paper tested the claim and found the opposite (fanous2025syceval, perez2023discovering, tsui2025selfcorrection, bucinca2021trust with bansal2021whole)

- [ ] Decide the four bibliography items left open by the audit — added 2026-09-05
  - **Done when:** each of the four has a decision recorded and, where needed, an edit made
  - `mckinsey2025stateofai`: UNVERIFIABLE. The URL is a rolling annual landing page now serving the 2026 survey, so the link no longer reaches the report cited. Either find a stable PDF link or drop the citation.
  - `gartner2026agentic`: UNVERIFIABLE. No URL, no document ID, and the 5-30x figure never terminates at a Gartner document in any source chain. Gartner.com blocks automated access.
  - `claudecode2025loop`: the cited Claude Code issue #27281 is real but describes restated intent with no tool call, not "editing the same file". VSCode #257885 does support the claim and has no entry at all. One key currently stands in for two citations.
  - `laban2025lost` key: the entry is now correct (Fourteenth ICLR, 2026, Outstanding Paper Award) but the key still says 2025. Renaming touches 8 call sites.

- [ ] Verify that each cited work supports the claim the paper attaches to it — added 2026-09-05
  - **Done when:** every citation in the live build has been checked against its source for whether the source says what the sentence says it says
  - The metadata audit did NOT do this. `claudecode2025loop` proves the failure mode is present: a real source cited for something it does not say.

- [ ] Anonymise the rater names in the appendix before submission — added 2026-09-08
  - **Done when:** `sections/appendix.tex` names no real person, and an anonymised build contains no author-identifying string
  - `appendix.tex:224-226` names the three annotators as "Liam", "Sophie" and "Troy" in Table 13. Swapping the author block on `main.tex` will NOT catch this: the first name matches the author, so the table de-anonymises the submission on its own. Replace with Rater A/B/C
  - Also check `results_v2.tex:59` and `introduction_v2.tex:3`, which carry "Liam" in LaTeX comments. Comments do not print, but they ship in the source if source is uploaded

- [ ] Resolve the duplicate model labels in the Study 2 dose-response figure — added 2026-09-08
  - **Done when:** the legend names each model once
  - `data/figures/momentum/dose_response_curve.png` legend lists both "claude-sonnet" and "claude-sonnet-4", and both "gemini-flash" and "gemini-2.5-flash". The short-named series carry only a dose-0 point, so the data appears to use two naming conventions for the same models. This is a data question, not a plotting one
  - Source: `scripts/visualize_momentum.py`

- [ ] Regenerate the momentum PDFs or delete them — added 2026-09-08
  - **Done when:** no build points at a file in `data/figures/momentum/*.pdf`, or those PDFs are rebuilt correctly
  - `dose_response_curve.pdf` was corrupt: three overlaid panels with ghosted, repeated titles, rendering as unreadable grey mush in the appendix. `visualize_momentum.py` writes only PNG, and the PNG is correct. The PDFs are dated four hours after the PNGs and were made by some other process. The appendix now points at the PNG
  - The sibling PDFs in that directory were made the same way and are suspect

- [ ] Reference or drop the ten unreferenced APPENDIX floats — added 2026-09-08, narrowed 2026-09-08
  - **Done when:** every appendix float is pointed at from prose, or removed
  - BODY IS DONE: all 12 body floats are now referenced. Figure 4 was cut; Figures 2 and 3 got the pointing sentences they never had (`results_v2.tex`, survival paragraph and pooled-trajectory paragraph)
  - Remaining: `tab:regression`, `fig:pipeline`, `fig:probe-cliff`, `fig:threshold-ladder`, `fig:dose-response`, `tab:pairwise`, `tab:judge-calibration`, `tab:human-agreement`, `tab:irr`, `tab:irr-momentum`
  - 10 of 23 floats are never referenced: `fig:survival-curves`, `fig:quality-trajectory`, `fig:targeted-dumbbell` in Results, plus 7 appendix floats. Audit and per-figure recommendation in `paper/reference/float_reference_audit.md`
  - Placement is already correct; only the pointing sentence is missing. Without a `\ref` the float can drift pages from its prose

- [ ] Decide whether the added emphasis in Figure 1 stays — added 2026-09-05
  - RECOMMENDATION 2026-09-08: keep. Reasoning and the twelve-convention check are in `paper/reference/fig1_corpus_check.md`
  - Figure redesigned 2026-09-08 against real corpus figures (`.workspace/reference/figure_examples/`): removed the coloured left accent bars, the level badges, the card fills, the rounded corners and the Apple UI font; chart height raised from 1.18in to 1.95in with direct end-of-line labels in place of a legend. Previous version at `paper/figures/versions/`
  - Aspect went 1.43:1 to 1.29:1; the figure now occupies about half of page 2 rather than 60%
  - **Done when:** the bold in the task and the highlighting in Turn 1 are either kept with the caption declaring them (current state) or removed
  - Both are authorial marks on quoted text. They mark exactly the requested content that Turn 5 loses, and the caption now says they are added, but it is a judgment call

- [ ] Update the ABSTRACT section of paper/SKELETON.md to describe the abstract that shipped — added 2026-09-08
  - **Done when:** `paper/SKELETON.md` section ABSTRACT lists the beats and numbers of the final abstract
  - It currently specifies a 150-180 word target and seven beats built on 0.74 levels, 1.16 levels, 39%->13% and 56%->92%. The final abstract is 189 words, eight sentences, and carries none of those four figures. The plan document no longer describes the paper

- [ ] Record the stripped-cliff effect size r in results_FINAL.md and Table 3 — added 2026-09-02
  - **Done when:** r appears in the ledger's stripped-cliff section and in `paper/sections/results_v2.tex` Table 3, and `RECOMPUTE_TODO.md` is deleted
  - The stripped p-value (1.01e-4) is already in the paper but was never written back to the ledger

- [ ] Move the blind pairwise reversibility result out of Limitations and into Results — added 2026-09-02
  - **Done when:** `paper/sections/results_v2.tex` reports the 56.2% figure with its CI and the pre-set 65% bar under its own heading, and the Limitations entry becomes a restatement rather than the only appearance
  - Two independent grounds: ARR desk-rejects a Limitations section used to introduce new analysis or results, and 0 of 31 surveyed papers report a pre-registered threshold at all, so ours is a strength currently presented as a failure

- [ ] Record that the design document's domain prediction is not supported — added 2026-09-02
  - **Done when:** the outcome of the "Key prediction" at `experiment/study3_revision_yield_design.md:117` is stated in the paper, and `results_FINAL.md` records that the objectivity gradient holds unstripped (p=0.019) and disappears stripped (p=0.151)

- [ ] Write the targeted-feedback repair findings into results_FINAL.md — added 2026-09-03
  - **Done when:** the ledger's Section 5 carries (a) 169/177 = 95.5% of targeted revisions reaching level 4 or above, and (b) the 13-trial subset where a genuinely revised output had degraded from a sufficient turn 1 (4.15 to 2.69) and one critique restored it to 4.77, Wilcoxon p=0.000488, with the disclosure that the other 100 of those 113 cases had a meta-response as their input, which strips to near-empty text and scores 1.06
  - Both are new as of 2026-09-03 and neither is in the ledger

- [ ] Decide whether the abstract and introduction close on the same claim — added 2026-09-10 — blocked on: Tania's answer
  - **Done when:** both closes state the same claim, or the split is recorded as deliberate with a reason
  - The introduction closes on the thesis ("intrinsic self-correction requires extrinsic direction"); the abstract closes on the finding ("naming the fault reverses the effect"). Compatible but not matched. Her second issue, and the one question put back to her on 2026-09-10

- [ ] Rewrite methods, discussion and conclusion; move Limitations after the Conclusion per ACL format — added 2026-09-02 — blocked on: introduction rewrite
  - **Done when:** the four sections are redrafted and `main.tex` builds with Limitations following the Conclusion

- [ ] ARR submission mechanics — added 2026-09-02 — blocked on: all section rewrites
  - **Done when:** `paper/main.tex` compiles anonymised with no author name or affiliation, Limitations sits unnumbered after the Conclusion, the body is within the ARR long-paper page limit, and the Responsible NLP Research checklist is completed
  - `main.tex` currently carries "Liam Neild, Emory University, liam.neild@emory.edu" and must be anonymised for review
  - The exact ARR requirements are being retrieved verbatim into `paper/rules/09_limitations_ethics.md`; use that file, not memory

## Completed

- [x] Withdrawn: restore Related Work to its own length benchmark — added 2026-09-14, withdrawn 2026-09-14
  - The task was based on a wrong benchmark. `rules/04` R2 set a 550-word floor from 22 sections, above its own stated NLP mean of 543. A 62-section measurement puts the median at 402 and Ali's at 397, so Related Work at 445 words is above both, not 105 below a floor. R2 is corrected in place with the reasoning recorded.

- [x] Cut the body to the ARR 8-page limit — added 2026-09-08
  - **Done when:** sections 1 through 7 fit in 8 pages in the built PDF, with Limitations, references and appendix outside the limit
  - Measured 2026-09-08 from `paper/builds/main.pdf`: the Conclusion begins on page 12. Roughly four pages over
  - This is the largest problem in the build. Details in `paper/reference/build_formatting_audit.md`
  - DONE 2026-09-14. Body 12 -> 8 pages, total 20 -> 16, over nine measured rounds. Body words 6,365 -> 3,816. `paper/build_check.py` reports the body-end page from main.aux and is the check to rerun after any edit
  - Largest single win: Limitations sat before the Conclusion, inside the counted body. ARR excludes it and ACL format puts it after. Moving it beat three rounds of prose cutting
  - Removed content that was promised and never delivered: four metrics defined but never reported, the self-reflection sub-experiment (n=720), and four citations the audits had flagged
  - Both new figures placed: `fig:revision-tax` (replaced its table) and `fig:input-level` (post-hoc, ledger 4c, disclosed in caption and prose)

- [x] Rewrite the sentence at introduction_v2.tex:82 — added 2026-09-03
  - **Done when:** the introduction's closing sentence echoes the current title instead of the retired one
  - It currently reads "Intrinsic self-correction, on its own, is not enough; it requires extrinsic direction", written to earn a title that no longer exists. Liam's prose to write.
  - MOOT 2026-09-14: the introduction was rewritten twice since this was logged; line 82 no longer contains the flagged sentence

- [x] Bring the three results figures up to the standard Figure 1 now meets — added 2026-09-08
  - **Done when:** no in-figure title duplicates its caption, no legend sits over the data, and no axis label collides with tick labels
  - DONE 2026-09-08: titles removed, legends moved above the axes, labelpad added, rendered at print width, includes switched to PDF. Figure 4 was cut entirely
  - ALSO FIXED: Figure 2 was clipping its own data. `ax.set_ylim(-0.02, 0.72)` cut the plot at 72% while Llama peaks at 90.0% (T2) and 80.0% (T3) and Claude at 86.7% (T2), so three of the highest points sat outside the axes. Limit raised to 97%
  - DONE 2026-09-08: in-figure titles deleted, legends moved above the axes, labelpad added, rendered at print width, includes switched to PDF, Figure 2's clipped y-limit fixed, Figure 4 cut

- [x] Fix three overfull tables in Results — added 2026-09-08
  - **Done when:** `tectonic` reports no Overfull \hbox for `sections/results_v2.tex`, and Tables 4 and 5 render separately
  - `results_v2.tex:114-122` (Table 4, tab:cliff) is 132.5pt too wide in a ~230pt column and prints across Table 5 on page 9. Also `:204-212` by 85.7pt and `:171-182` by 17.2pt
  - DONE 2026-09-08: Table 4 restructured, tabcolsep tightened on three tables. tectonic now reports zero overfull boxes for results_v2

- [x] Confirm the final abstract against Tania's comprehension read — added 2026-09-03 — blocked on: Tania's feedback
  - **Done when:** her read is in and the abstract is either left as it stands or amended
  - The abstract is FINAL as of 2026-09-08 and the version numbering is retired: 189 words, 8 sentences, 23.6 words per sentence, design sentence at S4 of 8. It clears every measured band and all 12 register zeroes. The only two departures are chosen: three result percentages against a rule of two or fewer, and the question opener at 0 of 67 ACL 2026 abstracts
  - Installed at `paper/sections/abstract_v2.tex`; text of record at `paper/abstract_versions/abstract_final.txt`; version history in `paper/abstract_versions/`; fix-by-fix record in `.workspace/scratch/abstract_fixes/`
  - CLOSED 2026-09-14: Tania approved the introduction in its entirety. Her rewrite is installed with three corrections; her review is at `.workspace/reference/reviews/tania_2026-09-09_introduction.md`

- [x] Reply to Tania on the introduction review — added 2026-09-10, done 2026-09-10
  - **Done when:** she has been told that both her open issues rested on a stale abstract, what the three corrections were, and the corrected question-opener figure
  - Her two issues quote abstract text that no longer exists: the live abstract carries 70%/27% (matching the intro) and closes on "naming the fault reverses the effect", not "revision robustness". Her worry that the intro cited something unwritten is resolved: §4b is at `results_v2.tex:63-72`
  - Her structural claim "all four of his intros land a crisp question by paragraph 1 or 2" measures at 5 of 24 (21%) across the fuller corpus. Her bold claim holds: 23 of 24
  - Her review verbatim: `.workspace/reference/reviews/tania_2026-09-09_introduction.md`

- [x] Fix the scale statement in results_v2.tex — added 2026-09-06, done 2026-09-07
  - Stripped Turn 5 at 2.92 sits just below Functional (level 3), not below Incomplete (level 2). Text corrected.
- [x] Resolve the five-versus-four domain contradiction — added 2026-09-06, done 2026-09-07
  - Both statements were true of different quantities. The results section now says so explicitly: the pooled trajectory measures how far quality falls (four of five significant), the direction asymmetry measures how often a revision moves it downward (all five significant).

- [x] Verify all 67 bibliography entries against published sources — added 2026-09-02, done 2026-09-05
  - 27 verified, 37 field errors, 2 unverifiable, 1 fabricated. Consolidated at `paper/reference/bib_audit_SUMMARY.md`; per-entry evidence with URLs and retrieval dates across `bib_audit_chunk1-4.md`
  - 36 corrections applied 2026-09-05. Dominant error class was wrong author lists: 10 entries carried plausible, well-formed author lists belonging to other people, including `huang2024large` (6 of 7 wrong) and `zhou2024calibrated` (attributed to four people, written by Kalai and Vempala)
  - Backups: `paper/references.bib.pre_audit_fix.bak` and `paper/references.bib.bak`

- [x] Remove the fabricated citation kim2024language — added 2026-09-05, done 2026-09-05
  - "Language Models Can Improve Their Own Reasoning---and Sometimes They Can't" does not exist. arXiv:2401.12294 is "Nearly critical superfluid: effective field theory and holography" (Bu, Gao, Gao, Li, hep-th). The author list was Prometheus 2's with Juyoung Suk corrupted to "Suk, Se June".
  - Removed from `paper/references.bib` (67 entries to 66), from the citation bracket in `related_work_v2.tex` line 53 (Kamoi's sentence and Reflexion kept, both real and correct), from the sentence it wholly supported in the retired `related_work.tex`, and from `paper/SKELETON.md`. Backups at `paper/references.bib.bak` and the dot-prefixed section backups.

- [x] Rebuild Figure 1 from real transcript data — added 2026-09-02, done 2026-09-05
  - `paper/figures/gen_fig1.py` builds it from `s3_worker__llama-3.3-70b__quarterly_sales__run3` by reading the data files at build time; the figure cannot drift from the analysis
  - Trial switched from the locked story-opening pick: the quarterly-sales failure is checkable against the user's own brief, which the creative-writing one is not
  - Wired into `introduction_v2.tex` as a `figure*` with caption; appendix companion at `sections/_fig1_appendix.tex` carries all five turns and all five judge rationales
  - 4.39in tall at textwidth, 8.1pt body type in print, lands top of page 2
  - 33 files carrying the fabricated content moved to `paper/figures/retired_fabricated_teaser/` with a README explaining both defects

- [x] Settle the title — added 2026-09-03, done 2026-09-03
  - `paper/main.tex` carries "Worse on Request, Better on Critique: Self-Correction on Work That Is Already Sufficient"; full candidate history at `paper/title_versions.md`

- [x] Write the revision-direction analysis into results_FINAL.md and move its script into the analysis tree — added 2026-09-02, done 2026-09-03
  - `results_FINAL.md` Section 4b holds the full analysis with disclosed filters, per-model and per-domain tables, the domain-homogeneity test, and the note that the design document's registered objectivity prediction is not supported once meta-commentary is stripped
  - Script at `scripts/study3/revision_direction.py`, output at `data/study3/analysis/revision_direction.json`; both scratch copies deleted
