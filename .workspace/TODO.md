# TODO

Deadline: ARR October 12, 2026 (confirmed 2026-09-02). Liam's own target for a finished
version is September 28, 2026. Six weeks from today.

Dependency chain: abstract (DONE 2026-09-08) -> introduction -> Figure 1 ->
methods/discussion/conclusion -> ARR submission mechanics (anonymise, page limit,
checklist). The introduction is now the head of the chain.

## Pending

- [ ] Complete the Responsible NLP Research checklist — added 2026-09-21
  - **Done when:** every one of the 18 subquestions has an answer that is true of the submitted paper, and no answer claims something the paper does not contain
  - Draft with all 23 questions sourced: `.workspace/notes/responsible_nlp_checklist_draft.md`. Nine already Yes. Six are No and cheap: LICENSE and a licence sentence (B2), model citations with dated identifiers in Methods (B1), a compute paragraph (C1, numbers measured), requirements.txt (C4), one sentence each for B3/D3/D5, and the four-vs-five-domain error in the Ethics Statement
  - Three are yours alone: the A2 risk scope, whether the RAs were compensated (D2), and the E disclosure of AI assistance
  - One external: whether Emory requires an IRB determination (D4)
  - An incomplete or misleading checklist is a named desk-reject ground, so this is not optional polish

- [ ] Confirm the co-authorship with Ali before 2026-10-12 — added 2026-09-17
  - **Done when:** he has agreed in writing to be listed as second author, and the affiliation and email in `main.tex` are confirmed by him
  - DECIDED 2026-09-17: Ali Emami is second author. `main.tex` now carries him. This also resolves the service-contributor requirement, since faculty with two or more major-CL publications qualify automatically
  - He has NOT been asked yet. The author list cannot be changed after submission ("no changes to the list of authors are allowed"), and every listed author is notified of the submission and reviews, so his agreement has to come first
  - Affiliation and email were inferred, not supplied: his 2026 papers (arXiv 2607.05113, 2504.07385) give Emory University and the pattern `aemami@emory.edu`, while his 2025 papers give Brock, so he has moved institutions. Both fields need his confirmation
  - He must also have an OpenReview profile with affiliation history, career status, email and ORCID. The policy says violations "will lead to desk rejection"
  - Reviewer registration for ALL authors is due 2026-10-15, three days after submission

- [ ] Complete the OpenReview profile before submission — added 2026-09-17
  - **Done when:** the profile carries affiliation history, career status, email, ORCID, and DBLP or ACL Anthology links where they exist
  - "All authors and service contributors MUST have OpenReview profiles with accurate affiliation history, career status, emails, ORCID and, where applicable, DBLP and ACL Anthology links. Violations will lead to desk rejection." An ORCID takes minutes to register and is named explicitly
  - Reviewer registration for ALL authors is due October 15, three days after submission. The dates page says non-compliance "may result in desk rejection or sanctions"

- [ ] Decide which rescore basis the Llama cliff reports, and state the effect-size divisor — added 2026-09-07, narrowed 2026-09-17
  - **Done when:** `results_v2.tex:78-80` reports a delta and a p-value from the same basis, and the paper says which N the effect-size z is divided by
  - NARROWED 2026-09-17. This was logged as two discrepancies. The effect-size one is withdrawn: the paper's r = 0.55 is correct and the 2026-09-07 recomputation that called it unmatched had dropped the tie correction. Verified twice, independently; the reasoning is recorded in `results_FINAL.md` under the withdrawn item
  - WHAT REMAINS IS REAL: `results_v2.tex:78-80` prints Llama's stripped cliff as -0.69 with p = 3.76e-4. The -0.69 is from the 50-pair rescore (whose own p is 2.98e-4) and the p-value is from the full 3,600-output rescore (whose own delta is -0.67). Either pairing is internally consistent; the current one is not. The preceding paragraph is entirely on the full rescore
  - No longer a table defect. `tab:cliff` was removed in the page cut and both numbers moved into prose unchanged, so `FLAG 2` at `results_v2.tex:192-195` records the all-balanced switch and does not mention that the per-model figure was left on the old basis
  - Also state the divisor: tie-corrected z over sqrt(trial count) gives 0.55; over sqrt(non-zero differences) gives 0.70. Same result, and a 270-paper survey found one paper that says which

- [ ] Resolve the sample mismatch in the paper's central contrast — added 2026-09-17
  - **Done when:** the abstract, introduction and `results_v2.tex:162` either compare quantities measured on the same population, or say plainly that they do not
  - `scripts/study3/phase6_targeted_feedback.py:215` filters to `level <= 3`, so the +1.16 targeted-feedback gain was measured ONLY on outputs the evaluator had rated not sufficient. `methods.tex:78` states this correctly
  - The -0.74 cliff, the 27.5% figure and the abstract's framing are all about work that WAS sufficient. `results_v2.tex:162` sets the two against each other directly, and the abstract turns it into "naming the fault reverses the effect"
  - The paper's own exploratory analysis cuts against that reading: section 4c reports undirected revision is already POSITIVE on insufficient input (+0.41, n = 194), which is the population +1.16 was measured in
  - The +1.16 remains a valid like-for-like comparison against the model's own generic revision on those same level 1-3 items. What it cannot carry is the claim about already-sufficient work. This is Liam's call on framing, not a number to change

- [ ] Fix the two float captions that describe a different computation than the one printed — added 2026-09-17
  - **Done when:** `tab:domain-variation` and `tab:pairwise` describe what they contain
  - `tab:domain-variation` (`appendix.tex:355-362`) prints UNPAIRED per-domain deltas while the caption and `results_v2.tex:102-105` attach paired-Wilcoxon p-values to them. The magnitudes differ materially: data_logic prints -1.01 and the tested decline is -0.53; creative prints -0.82 against -0.58. The printed T1 mean is all 144 trials per domain, the tested T1 mean is only trials reaching T5
  - `tab:pairwise` (`appendix.tex:186-197`) captions itself "Significant pairwise comparisons (Bonferroni-corrected, q < 0.05)" and prints six of the nine comparisons that meet that rule. The three omitted are Claude numeric 70 vs 100, Claude qualitative 70 vs 100, and Gemini numeric 0 vs 70 (r = +0.21, the only positive sign among the nine, and the one running against the claim two lines above). Those three are exactly the ones that lose significance under the Benjamini-Hochberg pass in `stats_report.txt:185-190`, which is a defensible reason to drop them, but then the caption should say FDR rather than Bonferroni. Also "q" conventionally denotes an FDR value and these are Bonferroni

- [ ] Rewrite the §4b direction-analysis prose in your own voice — added 2026-09-06, rescoped 2026-09-08
  - **Done when:** the `TKTK Liam` comment block above `paper/sections/results_v2.tex:63` is gone and the paragraph reads in your register
  - RESCOPED 2026-09-08: the reporting gap is closed. `results_v2.tex:63-72` now carries 199 down against 87 up among 286 movers, 69.6%, exact binomial 95% CI [63.9%, 74.9%], sign test p = 1.48e-11, the 411/113 (27.5%) sufficiency result, the per-model and per-domain table, and the unstripped 76.6% beside it. `methods.tex:82-84` defines the baseline as the most recent turn with genuinely new content
  - What remains is voice only: the paragraph carries a `TKTK` note saying the statistical scaffolding was written to match the surrounding register and asks you to rewrite it without changing the numbers
  - The stale note on this item claimed the analysis was absent from the body. That was true on 2026-09-07 and is not true now
- [ ] Work through the remaining claim-audit findings sentence by sentence — added 2026-09-05
  - **Done when:** every one of the 36 flagged claim-source pairs is either corrected in the prose, re-cited, or deliberately left with a recorded reason
  - Consolidated list: `paper/reference/claim_audit_SUMMARY.md`. Per-pair evidence in `claim_audit_chunk1-4.md`
  - DONE so far: the Laban accumulation claim, which appeared in four sentences across the introduction and related work
  - RE-TRIAGED 2026-09-16 against the live sentences rather than the 2026-09-05 ones. Full record appended to `paper/reference/claim_audit_SUMMARY.md`
  - The severe pass is DONE. 8 keys were retired outright by the page cut (`tsui2025selfcorrection`, the three industry sources, both overthinking papers, `sui2025efficient`, `claudecode2025loop`). 3 sentences were repaired by the intro and related-work rewrites (vendor guidance, fluent presentation, sustained pressure). 2 were fixed 2026-09-16: the instruction-tuning attribution that `perez2023discovering` contradicts, and the topic-drift clause that neither `zhang2020dialogpt` nor `thoppilan2022lamda` supports, which was cut at Liam's direction
  - `panickssery2024llm` with `koo2024benchmarking` was checked and is clean: CoBBLEr carries the position-bias half, so one key per bias in a shared bracket is fair
  - WHAT REMAINS is three mild decisions, none of which puts a claim in danger: `singhal2023long` studies RLHF reward models under a sentence whose subject is judges; `skitka1999automation` is unreachable but `parasuraman2010complacency` carries the clause verbatim; `ye2024justice` supports "stylistic" but not "formatting", since none of CALM's 12 biases is a formatting bias
  - `zhang2020dialogpt` and `thoppilan2022lamda` are now cited only by the retired `sections/related_work.tex`, which is not in `main.tex`

- [ ] Decide the four bibliography items left open by the audit — added 2026-09-05
  - **Done when:** each of the four has a decision recorded and, where needed, an edit made
  - REDUCED TO ONE 2026-09-16: `mckinsey2025stateofai`, `gartner2026agentic` and `claudecode2025loop` are all uncited in the live build now. The page cut removed the paragraphs that carried them, so all three decisions are moot. Only the key rename below remains
  - `laban2025lost` key: the entry is now correct (Fourteenth ICLR, 2026, Outstanding Paper Award) but the key still says 2025. Renaming touches 8 call sites.

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
  - The rater table is already anonymised (2026-09-16, key at `.workspace/reference/rater_key.md`). What remains is source-level only and does not print: the author block above, a `TKTK Liam` comment at `results_v2.tex:53`, a comment crediting Tania's rewrite at `introduction_v2.tex:3`, and absolute paths containing the username in `figures/gen_fig3_model_trajectories.py:174` and `gen_fig4_revision_tax.py:81`. Neither of those two scripts is referenced by any live section, so they may simply be dead
  - `sections/introduction.tex` is the retired v1 file. It is not in `main.tex` and it includes `figures/fig1_combined_v3.pdf`, one of the retired fabricated teasers, which no longer exists on disk. Harmless to the build but a trap for a later session
  - The exact ARR requirements are being retrieved verbatim into `paper/rules/09_limitations_ethics.md`; use that file, not memory

- [ ] Clear the 11 orphan section backups — added 2026-09-16
  - **Done when:** `paper/sections/` holds no `.bak` file, and any whose content is not in git history has been checked first
  - Found while verifying the reversibility item. The 2026-09-14 batch was removed at commit e7d228b; these 11 predate it: `.appendix.tex.bak_2026-09-08`, `.introduction_v2.tex.bak`, `.introduction_v2.tex.bak2`, `.methods.tex.bak`, `.related_work.tex.bak`, `.related_work_v2.tex.bak`, `.related_work_v2.tex.bak2`, `.related_work_v2.tex.bak4`, `.results_v2.tex.bak3`, `.results_v2.tex.bak_2026-09-08`, `results_OLD_DO_NOT_USE.tex.bak`
  - The last one carries no leading dot, so the `.gitignore` pattern added at e7d228b does not catch it

- [ ] Merge the paragraph stubs in related work and results — added 2026-09-16 — blocked on: Tania's notes on those sections
  - **Done when:** both sections sit inside the corpus band for words per paragraph, with no words added or cut
  - Related work averages 65 words per paragraph against a corpus p25 of 102 (paragraphs run 120, 66, 62, 59, 49, 35); results averages 64 against 78. Both pass length and fail paragraph length, which is what trimming every paragraph a little instead of cutting whole claims produces
  - Measured in `paper/reference/prose_census.md`. Merging related work's six run-in clusters to four puts it near 111 words per paragraph
  - Blocked deliberately: she is reading these two sections now, and her notes would collide with the merge

- [ ] Draft the Responsible NLP Checklist answers on AI assistance — added 2026-09-17
  - **Done when:** the checklist answers exist in `.workspace/notes/` for Liam to paste into OpenReview, naming the scope of coding assistance and the locations of any AI-drafted text
  - Policy re-verified live 2026-09-17 at `https://aclrollingreview.org/cfp`, section "AI Writing/Coding Assistance Policy", and it is word-for-word what `rules/09_limitations_ethics.md` recorded on 2026-09-02. Binding sentence: generative AI "use for writing or coding, as well as its scope, must be disclosed in the Responsible NLP Checklist"
  - Cases (a) language polishing and (b) short-form input assistance are explicitly exempt and cover most prose help. The obligations that bite here are the opening sentence on coding, case (c) literature search (which asks for citation accuracy rather than a disclosure line, and the bibliography and claim audits are that work), and case (d) low-novelty text, which asks authors to "specify where such automatically generated text was used"
  - Case (d) locations in the live build: the `TKTK` block above `results_v2.tex:53` and the reversibility subsection assembled 2026-09-16. Both are marked in the source
  - CORRECTION to the 2026-09-17 plan: it said an Acknowledgements section was required and missing. The checklist disclosure is required at submission; the Acknowledgements detail is camera-ready, and acknowledgements come out of an anonymous submission anyway. There is no missing section in the submitted draft
  - Liam's call on case (e), new ideas. The design, research questions and framing are his

## Completed




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
