# TODO

Deadline: ARR October 12, 2026 (confirmed 2026-09-02). Liam's own target for a finished
version is September 28, 2026. Six weeks from today.

Dependency chain: abstract (DONE 2026-09-08) -> introduction -> Figure 1 ->
methods/discussion/conclusion -> ARR submission mechanics (anonymise, page limit,
checklist). The introduction is now the head of the chain.

## Pending

Dependency chain: Tania's notes -> abstract/intro close + paragraph stubs -> ARR mechanics.
Ali's agreement -> his OpenReview profile -> author list frozen at submission.

### Unblocked

- [ ] Complete the Responsible NLP Research checklist — added 2026-09-21
  - **Done when:** every one of the 18 subquestions has an answer that is true of the submitted paper, and no answer claims something the paper does not contain
  - Draft with all answers sourced: `.workspace/notes/responsible_nlp_checklist_draft.md`. LICENSE, requirements.txt and the Ethics Statement domain count are done. Remaining: model citations with dated identifiers in Methods, a compute paragraph (numbers measured), and one sentence each for B2/B3 (licence and API terms), B5 (language is English), D3 (consent) and D5 (rater demographics)
  - Three are yours alone: the A2 risk scope, whether the RAs were compensated (D2), and the E disclosure of AI assistance
- [ ] Decide whether to link an artifact in the submission, and anonymise it if so — added 2026-09-21
  - **Done when:** either the submission links an anonymised mirror carrying no author name, or the decision not to link one is recorded here
  - `github.com/WilliamANeild/stet` is public under your own name. ARR requires any artifact link in a submission to be anonymous, so this URL cannot go in the paper. An anonymised mirror is a separate job from the repo itself
- [ ] Complete the OpenReview profile before submission — added 2026-09-17
  - **Done when:** the profile carries affiliation history, career status, email, ORCID, and DBLP or ACL Anthology links where they exist
  - Yours regardless of what Ali decides. A missing ORCID is a desk rejection
- [ ] Work through the remaining claim-audit findings sentence by sentence — added 2026-09-05
  - **Done when:** every one of the 36 flagged claim-source pairs is either corrected in the prose, re-cited, or deliberately left with a recorded reason
  - The largest remaining body of work on the manuscript itself
- [ ] State which N the effect-size r divides by, and record r in the ledger and Table 3 — added 2026-09-02, narrowed 2026-09-21
  - **Done when:** the paper says whether r divides by all 50 trials or by the non-zero differences, r appears in the ledger's stripped-cliff section and in Table 3, and `RECOMPUTE_TODO.md` is deleted
  - Verified 2026-09-21: the printed r = 0.55 is the tie-corrected value on N = 50 and is correct; the paper prints it and r = 0.658 without naming either divisor. `RECOMPUTE_TODO.md` still exists

- [ ] Record that the design document's domain prediction is not supported — added 2026-09-02
  - **Done when:** the outcome of the "Key prediction" at `experiment/study3_revision_yield_design.md:117` is stated in the paper, and `results_FINAL.md` records that the objectivity gradient holds unstripped (p=0.019) and disappears stripped (p=0.151)
  - Half done 2026-09-21: the ledger records it; no live section mentions it. A pre-registered prediction that failed should be stated
- [ ] Reference or drop the 11 unreferenced appendix floats — added 2026-09-08, recounted 2026-09-21
  - **Done when:** every appendix float is pointed at from prose, or removed
  - 11 of 14 are unreferenced: tab:regression, fig:pipeline, fig:probe-cliff, fig:threshold-ladder, fig:dose-response, tab:pairwise, tab:judge-calibration, tab:human-agreement, tab:direction, tab:pooled-trajectory, tab:domain-variation. Was 13; the Study 1 reliability pair was fixed 2026-09-20
- [ ] Rewrite the §4b direction-analysis prose in your own voice — added 2026-09-06, rescoped 2026-09-08
  - **Done when:** the `TKTK Liam` comment block above `paper/sections/results_v2.tex:63` is gone and the paragraph reads in your register
  - Comment still present 2026-09-21. It also trips preflight's placeholder check and carries your name in source
- [ ] Update the ABSTRACT section of paper/SKELETON.md to describe the abstract that shipped — added 2026-09-08
  - **Done when:** `paper/SKELETON.md` section ABSTRACT lists the beats and numbers of the final abstract
  - Confirmed stale 2026-09-21: it still specifies a 150-180 word target and beats built on figures the shipped abstract does not use, and predates STET entirely
- [ ] Tidy what a visitor sees at the top level — added 2026-09-21
  - **Done when:** `emami_update.excalidraw`, `RECOMPUTE_TODO.md` and `worker_trials_OLD_WRONG_PROBE.jsonl` are each removed, renamed or deliberately kept with a reason recorded
  - The repo is public with a README now. `emami_update.excalidraw` names Ali before he has agreed to be an author; the trials file's own name says its data is wrong
- [ ] Clear the orphan section backup — added 2026-09-16, recounted 2026-09-21
  - **Done when:** `paper/sections/` holds no `.bak` file, and any whose content is not in git history has been checked first
  - Down to one: `sections/results_OLD_DO_NOT_USE.tex.bak`. Was 11
- [ ] Decide whether the added emphasis in Figure 1 stays — added 2026-09-05
  - **Done when:** the bold in the task and the highlighting in Turn 1 are either kept with the caption declaring them (current state) or removed

### Blocked

- [ ] Confirm the co-authorship with Ali before 2026-10-12 — added 2026-09-17 — blocked on: your decision on when to ask
  - **Done when:** he has agreed in writing to be listed as second author, and the affiliation and email in `main.tex` are confirmed by him
  - The only item gated on another person and the only one whose lead time you do not control. His affiliation in `main.tex` (Emory, aemami@emory.edu) was verified correct against two 2026 papers on 2026-09-20
- [ ] Decide whether the abstract and introduction close on the same claim — added 2026-09-10 — blocked on: Tania's answer
  - **Done when:** both closes state the same claim, or the split is recorded as deliberate with a reason
- [ ] Merge the paragraph stubs in related work and results — added 2026-09-16 — blocked on: Tania's notes on those sections
  - **Done when:** both sections sit inside the corpus band for words per paragraph, with no words added or cut
- [ ] ARR submission mechanics — added 2026-09-02 — blocked on: the checklist and the author list
  - **Done when:** `paper/main.tex` compiles anonymised with no author name or affiliation, Limitations sits unnumbered after the Conclusion, the body is within the ARR long-paper page limit, and the Responsible NLP Research checklist is completed
  - Three of the four hold already as of 2026-09-21: the anonymised build is clean, Limitations is unnumbered and follows the Conclusion, and the body ends on page 8. Only the checklist remains

## Completed


- [x] Write the targeted-feedback repair findings into results_FINAL.md — added 2026-09-03, done 2026-09-21
  - `results_FINAL.md` section 18. All values re-derived from the data on 2026-09-21 and reproduce exactly: 169/177 = 95.5% reaching level 4+, the 113 degraded-from-sufficient inputs splitting 13 genuine / 100 meta, the 13-trial row 4.15 -> 2.69 -> 4.77 at p = 0.000488, and the meta inputs averaging 1.06. The section states plainly that the 100 meta rows are not evidence of repair
- [x] Regenerate the momentum PDFs or delete them — added 2026-09-08, done 2026-09-20
  - Verified 2026-09-21: no live section points at any `data/figures/momentum/*.pdf`. The appendix uses the PNG, and the dose-response figure was regenerated with the model-name normalisation
- [x] Resolve the sample mismatch in the paper's central contrast — added 2026-09-17, done 2026-09-21
  - Verified: `results_v2.tex` now reads "A critique naming the fault raises quality by 1.16 levels on work rated below the sufficiency threshold", and the paragraph above names the cliff's population (Turn 1 mean 3.66, 33 of 50 beginning above the threshold). The two populations are stated rather than conflated
- [x] Fix the two float captions that describe a different computation than the one printed — added 2026-09-17, done 2026-09-21
  - Verified: `tab:domain-variation` describes the paired Wilcoxon on stripped content over trials with a genuine Turn-5 revision, and `tab:pairwise` describes the Bonferroni-within-model and Benjamini-Hochberg-across-analysis correction. Both now match what they print
- [x] Decide the four bibliography items left open by the audit — added 2026-09-05, done 2026-09-21
  - Three were made moot by the page cut. The fourth, the `laban2025lost` key reading 2025 for a 2026 paper, was verified correct in its printed fields on 2026-09-20 (ICLR 2026, Outstanding Paper Award, confirmed on the ICLR blog). The key itself does not print; renaming it touches eight call sites and is not worth doing
- [x] Rewrite methods, discussion and conclusion; move Limitations after the Conclusion — added 2026-09-02, done 2026-09-21
  - The Discussion was cut entirely on Tania's evidence, and Limitations is unnumbered and follows the Conclusion in `main.tex`. The section rewrites happened across the v2 sections




- [x] Verify every reference in the live build — added 2026-09-20, done 2026-09-20
  - All 36 checked against the ACL Anthology, ICLR/NeurIPS proceedings, Crossref, the arXiv API or the publisher's page. All exist; no fabrication, no misattribution. Four entries completed with published pages; two Findings papers retyped from @article to @inproceedings
  - The ICLR 2026 Outstanding Paper Award on `laban2025lost` is confirmed by the ICLR blog; "Outstanding Paper" is the official term. The related-work claim that Laban et al. find the effect threshold-shaped was verified against their gradual sharding experiment rather than their wording, and holds
  - Record: `paper/reference/citation_verification_2026-09-20.md`
- [x] Decide what to do with the 25 uncorrected decline-phrase rows — added 2026-09-20, done 2026-09-20
  - DECIDED 2026-09-20: sample stays as published. Panel 50, genuine rate 24.9%. Applying the discriminator to all 35 gives -0.74 on 42 trials; removing the ten gives -0.75 on 52. No number in the paper moves under any of the three, so the published sample stands. Evidence: `scripts/study3/audit_hand_corrections.py`, `results_FINAL.md` section 15
- [x] Resolve the duplicate model labels in the Study 2 dose-response figure — added 2026-09-08, done 2026-09-20
  - `scripts/visualize_momentum.py` now maps the short names to the canonical ones before concat and asserts exactly three models survive, so the split series cannot come back silently. The in-figure title was removed at the same time
- [x] Make Figures 7 and 8 legible in print — added 2026-09-20, done 2026-09-20
  - Both drew canvases far wider than the column they are included at, scaling type under 4pt. Figure 8's canvas went 16.5in to 9.6in with type set explicitly; Figure 7 became a horizontal bar chart so five quoted probe wordings each get a full line
- [x] Correct the Methods description of the ten hand-corrected labels — added 2026-09-20, done 2026-09-20
  - It claimed each was "a decline that restated the prior output in full"; four reproduce none of the preceding turn. Now says the model reproduced its earlier answer alongside the refusal, which holds for all ten
- [x] Check the two citations the claim audit never covered — added 2026-09-05, done 2026-09-17
  - Both abstracts fetched and read. `mizrahi2024state` studies benchmarks that "rely on a single instruction template" and the brittleness of "single-prompt evaluations"; `sclar2024quantifying` studies "prompt formatting" against "the currently-standard practice of reporting performance on a single format". Both are about one prompt, not one turn, so neither supported the sentence citing them
  - The audit had also classified `liang2023holistic` NOT SUPPORTED for "current models perform well", quoting HELM reporting "essentially chance accuracy at 50.1%" and declining "the universal claim that models that perform well are always desirable". HELM does support the single-answer reference-scored form, which the other two keys were carrying, so the citations were effectively swapped
  - Opening sentence rewritten 2026-09-17 at Liam's direction: HELM now carries the single-turn reference-scored form, the paper's own first-turn sufficiency (631 of 720, matching `results_v2.tex:108` and `results_FINAL.md:120`) carries the performance half, and both prompt-format keys are retired from the live build
  - Introduction is 767 words against a p75 of 768, so the addition was tightened rather than allowed to push the section out of band. Both builds still end the body on page 8
  - The claim audit now covers every citation in the live build with nothing outstanding above the three mild scope decisions

- [x] Make the anonymised review build a switch rather than a submission-day edit — added 2026-09-17, done 2026-09-17
  - `main.tex` now carries `\newif\ifreview \reviewfalse` driving the acl package options, so the submission build is a one-word edit rather than a hand-modified package line
  - `build_check.py` rewritten to compile and report BOTH builds. Line numbers and the suppressed author block change the layout, so the two can disagree and the review build is the one the limit must hold against. Both currently report body ends p8, 16 pages, no warnings
  - It fails loudly if `main.tex` stops carrying the switch, rather than silently checking one build twice

- [x] Anonymise the rater names in the appendix before submission — added 2026-09-08, done 2026-09-16
  - `appendix.tex` Table 13 now reads Rater A/B/C. Mapping recorded outside the submitted source at `.workspace/reference/rater_key.md`: A is Liam, B is Sophie, C is Troy. Agreement figures unchanged
  - Swept the whole live build rather than the three flagged lines. Nothing identifying prints in the PDF now except the author block, which is the submission-mechanics item

- [x] Move the blind pairwise reversibility result out of Limitations and into Results — added 2026-09-02, done 2026-09-16
  - New subsection `sec:reversibility` in Results reports 41 of 73 decided comparisons (56.2%, bootstrap 95% CI [45.2%, 67.1%], 27 ties of 100 pooled, kappa 0.703) and the pre-set 65% bar that was not cleared. Numbers taken from `results_FINAL.md`, not from the stale backup that also held them
  - `methods.tex` had said "The outcome is reported in the Limitations." It now points at the Results subsection
  - The Limitations entry is reduced to a restatement that refers back, so Limitations no longer introduces a result
  - Paid for on the page budget by moving the post-hoc input-level figure to Appendix Supplementary Figures (its paragraph already states both numbers, so only the visual moved) and by cutting 16 words where the Discussion defined revision robustness a second time. Body still ends page 8 and every section benchmark still passes; figures per table improved from 1.67 to 1.33 against a median of 1.25

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
