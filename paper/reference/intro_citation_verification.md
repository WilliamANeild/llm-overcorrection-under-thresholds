# Citations added to the introduction, and what was checked

Verified 2026-09-08. Each entry records the claim the citation is attached to, the source
text checked, and where that text was read. Nothing was added on the strength of a title.

## 1. `mizrahi2024state` and `sclar2024quantifying` — paragraph A

**Attached to:** "A model is handed a fully specified task, produces one answer, and is
scored against a reference."

**Placement note.** These two support the *form* of evaluation. They do **not** support
"current models perform well," which stays with `liang2023holistic` (HELM). The sentence
was split so each citation carries only what its source establishes.

`mizrahi2024state`, arXiv 2401.00595v3, abstract read 2026-09-08 via the arXiv API:

> "These benchmarks typically rely on a single instruction template for evaluating all
> LLMs on a specific task."

`sclar2024quantifying`, arXiv 2310.11324v2, abstract read 2026-09-08 via the arXiv API:

> "...instead of the currently-standard practice of reporting performance on a single
> format."

Both state directly that single-prompt, single-output evaluation is the standard form.
That is the claim, and neither is being asked to carry more.

## 2. `tyen2024llms` — paragraph D

**Attached to:** a new sentence, "\citet{tyen2024llms} isolate that seam directly: models
struggle to find their own reasoning errors, but correct them reliably once the location
is supplied."

Source: arXiv 2311.08516v3, abstract read from the local cache at
`.workspace/reference/intro_corpus/html/2311.08516.html`, fetched 2026-09-08:

> "we show that poor self-correction performance stems from LLMs' inability to find
> logical mistakes, rather than their ability to correct a known mistake"

> "we test the correction abilities of LLMs -- separately from mistake finding -- using a
> backtracking setup that feeds ground truth mistake location information to the model. We
> show that this boosts downstream task performance across our 5 reasoning tasks,
> indicating that LLMs' correction abilities are robust."

This is the closest published support for the paper's own thesis: the failure is in
locating the fault, not in repairing it, and supplying the location restores performance.

## Candidates considered and not used

- `shinn2023reflexion`, `zhang2024small`, `qu2024recursive`: real and relevant, but no
  sentence in the introduction makes a claim they would support. Adding them would be
  padding, which the corpus rule forbids: every citation is attached to a claim about what
  that work established.
- `copilot2025agentmode` and other vendor pages: not used. The bibliography audit already
  found one vendor citation (`claudecode2025loop`) attached to something its source does
  not say.

## One weakness this pass did not fix

Paragraph E refers to "the multi-turn literature" in the plural, but only
`laban2025lost` is cited for it anywhere in the introduction. Either a second multi-turn
work is needed or the phrase should be singular. Nothing currently in `references.bib`
fills that gap.
