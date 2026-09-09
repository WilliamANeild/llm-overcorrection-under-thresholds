# Bibliography audit, consolidated

Run 2026-09-05 across four agents. Per-entry evidence, with URLs and retrieval dates and
paste-ready corrected entries, is in `bib_audit_chunk1.md` through `bib_audit_chunk4.md`.

## Counts

| | chunk 1 | chunk 2 | chunk 3 | chunk 4 | total |
|---|---|---|---|---|---|
| VERIFIED | 9 | 6 | 8 | 4 | **27** |
| FIELD ERRORS | 8 | 9 | 9 | 11 | **37** |
| UNVERIFIABLE | 0 | 1 | 0 | 1 | **2** |
| NOT FOUND | 0 | 1 | 0 | 0 | **1** |
| | 17 | 17 | 17 | 16 | **67** |

27 of 67 clean. One entry removed 2026-09-05, so the file now holds 66.

## Error classes, worst first

**1. Wrong author lists (10 entries).** Plausible, well-formed, and belonging to other
people. `zhou2024calibrated` (real authors Kalai and Vempala; the key encodes a surname
belonging to nobody on the paper), `huang2024large` (6 of 7 wrong), `mizrahi2024state`
(5 of 6), `zhang2024lists` (5 of 6, plus a trailing "and others" implying authors who do
not exist), `li2024generation` (5 wrong, 6 missing), `wei2024simple` (3 non-authors added,
Denny Zhou omitted), `chen2025overthinking` (all 5 wrong), `borisov2026yapbench` (3 of 4
given names), `zhou2026oversight` (9 hidden, last author moved to third),
`sui2025efficient` (1 dropped).

**2. Fabricated text (2 entries).** `sclar2024quantifying` carries an invented subtitle.
`goldman2026tokens` cites a title Goldman never published, under the wrong analyst's given
name; the underlying claim is sound.

**3. Wrong identifiers (1 entry).** `ranaldi2023large` points at arXiv 2311.12193, a
computer-vision paper. Correct ID 2311.09410.

**4. Preprint overtaken by publication (11 entries).** madaan2024self (NeurIPS 2023),
panickssery2024llm (NeurIPS 2024), singhal2023long (COLM 2024), ghosal2025overthinking
(NeurIPS 2025), tsui2025selfcorrection (COLM 2026, retitled), sharma2024towards (ICLR
2024), koo2024benchmarking (Findings ACL 2024), ye2024justice (ICLR 2025),
huang2024large (ICLR 2024), li2024generation (EMNLP 2025), chen2024overthinking (ICML
2025, retitled), zhou2024calibrated (STOC 2024).

**5. Wrong years (5 entries).** madaan2024self -> 2023, wei2024simple -> 2023,
zheng2024judging -> 2023, yang2025underspecification -> 2026, ye2024justice -> 2025.

**6. Venue ordinal errors (1 entry, class flagged for re-check).** `laban2025lost` is the
FOURTEENTH ICLR, 2026, not the Thirteenth, 2025. The award is real but is an Outstanding
Paper Award; ICLR 2026 has no "Best Paper" category. Key should be laban2026lost.

**7. Truncated author lists behind "and others" (6+ entries).** schulhoff2024prompt hides
21 of 31; zhou2026oversight hides 9; zheng2024judging hides 3; sharma2024towards,
koo2024benchmarking, ye2024justice all truncate.

**8. Structural (1 entry).** `zhang2020dialogpt` is an `@article` with a proceedings name
in `journal=`, which typesets wrongly under acl_natbib. All facts correct.

**9. Web sources that moved or cannot be reached (4 entries).** anthropic2025prompting
(moved to platform.claude.com, retitled), openai2025sycophancy (title truncated; page 403s
to bots), thompson2026aicost ("Era" not "Phase"), mckinsey2025stateofai (UNVERIFIABLE; the
URL is a rolling annual landing page now serving the 2026 survey, so the link no longer
reaches the cited report), gartner2026agentic (UNVERIFIABLE; no URL, no document ID, and
the 5-30x figure never terminates at a Gartner document).

**10. Claim-source mismatch (1 entry).** `claudecode2025loop` supports a sentence in
`discussion.tex` about "agents stuck in infinite loops editing the same file". Claude Code
issue #27281 is real but describes restated intent with no tool call, not file editing.
The VSCode issue #257885 does support the claim and has no bib entry at all; one key is
standing in for two citations.

## Removed

`kim2024language`, 2026-09-05, on Liam's instruction. "Language Models Can Improve Their
Own Reasoning---and Sometimes They Can't" does not exist; arXiv:2401.12294 is a hep-th
superfluid paper; the author list was Prometheus 2's.

## What this pattern implies

Thirty-seven errors whose dominant class is well-formed but wrong author lists is not what
a stale bibliography looks like. It is what model-generated citations look like. The
`claudecode2025loop` mismatch shows the same failure reaching past the bibliography into
the prose: a real source cited for something it does not say. Any other content in the
paper from the same origin needs checking against its sources, not just its formatting.

## Not done

This audit verified METADATA: does the work exist, and are the fields right. It did NOT
verify that each cited work supports the claim the paper attaches to it. That is a
separate pass and `claudecode2025loop` shows it is needed.
