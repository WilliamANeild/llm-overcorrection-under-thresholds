---
name: tania-2026-09-18-two-versions
description: Tania's second review, delivering two full rewrites and the findings-versus-benchmark question
metadata:
  type: reference
---

# Tania Neild, 2026-09-18. Two versions and the framing question

Received by email. Reproduced verbatim below; nothing paraphrased. The two attachments are
saved beside this file as `v2_findings.pdf` (her findings-mode version) and
`v3_benchmark.pdf` (her benchmark-mode version), with text extractions alongside. Note the
extractions interleave the two columns and are unreliable for reading prose.

Her first review, on the introduction, is at
`.workspace/reference/reviews/tania_2026-09-09_introduction.md`.

---

> Ok- we had missed some sections that he had in his other 5 papers. I added them. I compared
> all the style to his 5 of 10 papers. It is attached,
>
> There is one difference....more substance:
>
> The contribution is a finding, not a resource or technique. His highest-profile papers ship a
> benchmark (TaarofBench, CenterBench, Indica) or a method (Thought Injection, ZIP, SCOPE).
> Yours ships a behavioral result plus metrics. That's a legitimate paper and several of his
> are exactly this, but it's the less "flagship" of his two modes.
>
> On the deeper question of whether it's a flagship-mode paper (named resource/method, single
> anchor) or a findings-mode paper (behavioral result, distributed evidence), it's firmly the
> latter, which is real but is his less headline-grabbing register.
>
> So the other copy tries to get to away from just a findings paper and over to a resource or
> technique.
>
> So then I worked to turn it into a benchmark instead of a finding, but only 40 is a small
> benchmark,
> Before the 40 tasks were just the material you ran your experiment on. Nobody judges an
> experiment by how many stimuli it used, as long as the statistics hold. Forty tasks x 6
> models x 3 runs = 720 conversations is plenty of data to support a finding. So in
> findings-mode, 40 was never a problem.
>
> When we changed to make it a bencharmk, it changed the 40 tasks from "material" into "the
> product." A benchmark is its task set -- when you release STET and say "score your model on
> this," the 40 tasks are the thing people download and run. And now the number invites a
> specific question a reviewer will ask: is 40 tasks enough to give a stable, meaningful score?
>
> You have three honest responses:
>
> (a) Frame it as a compact diagnostic on purpose. Argue that STET measures one specific,
> sharply-defined behavior (leaving sufficient work alone), that the behavior is consistent
> enough across tasks that 40 suffices to rank models, and show the ranking is stable (e.g.,
> the model ordering holds if you split the 40 in half). This is writing plus one sobustness
> check, no new tasks. Defensible if the split-half ranking is stable.
> (b) Grow the task set. Expand to 150-300 tasks so per-domain cells are properly powered.
> This is real work -- writing tasks, re-running all six models, re-scoring -- and it's
> arguably a different paper's worth of effort.
> (c) Downgrade the benchmark claim. Call STET a "protocol and diagnostic" rather than a
> "benchmark," which lowers the bar the task count has to clear. Keeps most of this second
> paper's benefit (named, citable, releasable) while dodging the "too small for a benchmark"
> critique.
>
> Lastly, comparing to the other paper, we went from a findings paper, then I tried to make it
> into the benchmark, but 40 might not be strong enough. And technically they could say that
> you lack a method in your paper.. but that will be more tests and experiments
>
> What do you think of the two versions>

---

## The question she is actually asking

Which mode the paper submits in. Findings, or a named releasable artifact. She has built both
and is asking for a decision, not for edits.

## What she supplies with it

- Two complete 13-page rewrites, not comments on ours.
- A claim that we omitted sections Emami uses, which she has added. That claim is checkable
  against `paper/reference/emami_writing_patterns.md`, which measures 24 of his papers.
- A named artifact, STET, which does not exist in our draft.
- Her own diagnosis of the weakness her benchmark version creates, and three ways out of it,
  one of which (a) is decidable from data we already have rather than by argument.
