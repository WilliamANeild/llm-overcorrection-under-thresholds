# Abstract feedback from Tania Neild, received 2026-09-03

Sent v12 (210-word build) with the prompt "Read this once, then without looking back,
tell me in your own words what you think it found."

She did not answer that question. She rewrote the abstract three times, having first
scanned nine 2026 ACL/EACL/ICML papers to derive a target style. Her framing: "Here is
what I came up with. Keeping his style in mind. I struggled with three slightly
different versions trying to cut it. It is very math and stats based."

Typos in the source are preserved verbatim below ("for every mode", "an domains",
"declined or risions", "models wrevisions").

---

## Version A

Do language models know when a good answer should be left alone? Self-correction research asks whether a model can repair a response that is wrong, and finds it can with a specific critique and largely cannot without one; unexamined is the case where the work is already sufficient and gets revised anyway. We study this case across 720 five-turn conversations spanning six models, forty tasks, and five domains, offering at every turn a neutral option to keep or revise. Most models decline to genuinely revise: by the fifth turn, 86.7% of replies are meta-responses, restatements and declines presented as compliance. Among the revisions that do occur, quality falls 0.74 levels from the first turn to the fifth (p = 1.01×10⁻⁴), the decline appears in all five domains, and the first turn is the quality-maximizing stopping point for every mode We introduce the revision tax, the output spent past that point, and find it consumes 62.1% of all tokens generated. Notably, a single specific critique reverses the decline, lifting revisions 1.16 levels above undirected iteration (p = 5.7×10⁻¹⁹) across all five adequately powered models. Undirected and directed revision are not two points on a spectrum; they are close to opposites, and the failure is one of direction, not capacity. Blind readers prefer the first draft only slightly more often than chance once the meta-commentary wrapped around revisions is stripped away. Revision robustness, a model's willingness to leave sufficient work alone, deserves evaluation alongside first-turn capability.

## Version B

Large language models are routinely asked to improve outputs that are already good enough, and when given no direction beyond "make it better," they do not simply fail to help, they make things worse. We test this directly across six models, forty tasks, an domains, running 720 five-turn conversations in which a model is offered, at every turn, a neutral choice to keep its work or revise it with no stated fault. Most models decline to genuinely revise at all: by the fifth turn, 86.7% of replies are meta-responses, restatements or declines dressed up as engagement. Among the revisions that do occur, quality falls. On the trials where genuine revision happens at every turn, mean quality drops 0.74 levels from the first turn to the fifth (p = 1.01×10⁻⁴), and the first turn is the quality-maximizing stopping point for every model we test. A single specific critique reverses this entirely, lifting revised output 1.16 levels above a model's own undirected revision (p = 5.7×10⁻¹⁹) across all five adequately powered models. The failure traces to feedback, not capacity: the same model that degrades its own sufficient work without direction improves it substantially once told what is wrong. We also show that the polite wrapping models attach to declined or risions corrupts automated judgment of these conversations in two directions at once, inflating preference for the earlier draft while depressing the measured quality of the later one, and that controlling for it is necessary to see the true effect. Undirected iteration is not a milder form of directed revision, it is close to its opposite, and in our data it wastes 62% of tokens spent past the optimal stopping point. We argue that a model's willingness to leave a sufficient answer alone deserves evaluation as rigorous as its ability to produce one, and that the fix is not more turns but an evaluation step before every revision.

## Version C

Do language models know when a good answer should be left alone? Asked to improve work that is already sufficient, with no indication of what is wrong, a model faces a choice that single-turn benchmarks never test: keep it or revise it. We study this choice directly across 720 five-turn conversations spanning six models, forty tasks, and five domains, offering at every turn a neutral option to keep or revise. Most models decline to genuinely revise: by the fifth turn, 86.7% of replies are meta-responses, polite declines and restatements that change nothing yet read as engagement. Among the revisions that do occur, quality falls 0.74 levels from the first turn to the fifth (p = 1.01×10⁻⁴), and the first turn is the quality-maximizing stopping point for every model tested. We introduce the revision tax, the output spent past that point, and find it consumes 62.1% of all tokens generated. Notably, a single specific critique reverses the decline entirely, lifting revisions 1.16 levels above undirected iteration (p = 5.7×10⁻¹⁹) across all five adequately powered models. Undirected and directed revision are not two points on a spectrum; they are close to opposites, and the failure is one of direction, not capacity. Three human raters and a blind pairwise study of 50 trials show readers prefer the first draft only 56% of the time, near chance, once the meta-commentary models wrevisions is stripped away. Our findings suggest that revision robustness, a model's willingness to leave sufficient work alone, deserves evaluation alongside first-turn capability.

---

## The nine 2026 papers she derived the style from

1. ZIP: Quantifying Which Words Matter in Zero-Shot Instructional Prompts (*SEM 2026) https://aclanthology.org/2026.starsem-conference.30/
2. If Only My CGM Could Speak: A Privacy-Preserving Agent for Question Answering over Continuous Glucose Data (Findings of ACL 2026) https://aclanthology.org/2026.findings-acl.891/
3. DART: Mitigating Harm Drift in Difference-Aware LLMs via Distill-Audit-Repair Training (Findings of ACL 2026) https://aclanthology.org/2026.findings-acl.244/
4. Memory Dial: A Training Framework for Controllable Memorization in Language Models (Findings of ACL 2026) https://aclanthology.org/2026.findings-acl.179/
5. The Dog the Cat Chased Stumped the Model: Measuring When Language Models Abandon Structure for Shortcuts (EACL 2026) https://aclanthology.org/2026.eacl-long.19/
6. SAGE: A Search-AuGmented Evaluation of Large Language Models on Free-Form QA (ACL 2026) https://aclanthology.org/2026.acl-long.66/
7. Common to Whom? Regional Cultural Commonsense and LLM Bias in India (ACL 2026) https://aclanthology.org/2026.acl-long.249/
8. Reasoning Traces Shape Outputs but Models Won't Say So (ACL 2026) https://aclanthology.org/2026.acl-long.1986/
9. SCOPE: Selective Conformal Optimized Pairwise LLM Judging (ICML 2026) https://arxiv.org/abs/2602.13110

---

# Analysis, 2026-09-04

Her nine sources were fetched from the ACL Anthology and arXiv and counted mechanically.
Verbatim abstracts saved at `paper/reference/acl2026_abstracts.json`.

| paper | words | sentences | % statistics | p-values |
|---|---|---|---|---|
| ZIP (*SEM 2026) | 162 | 5 | 2 | 0 |
| CGM (Findings ACL 2026) | 192 | 11 | 2 | 0 |
| DART (Findings ACL 2026) | 232 | 8 | 9 | 0 |
| Memory Dial (Findings ACL 2026) | 158 | 6 | 0 | 0 |
| Dog the Cat (EACL 2026) | 201 | 9 | 0 | 0 |
| SAGE (ACL 2026) | 157 | 7 | 0 | 0 |
| Common to Whom (ACL 2026) | 186 | 7 | 4 | 0 |
| Reasoning Traces (ACL 2026) | 169 | 8 | 1 | 0 |
| SCOPE (ICML 2026) | 142 | 5 | 0 | 0 |
| **median** | **169** | **7** | **1** | **0** |

Her own drafts: A 244 words / 6 statistics / 2 p-values; B 315 / 6 / 2; C 250 / 7 / 2.
Ours (v12.2): 197 words / 1 statistic / 0 p-values.

## What this settles

1. **P-values are out.** 0 of 9 ACL 2026 sources carry one; 0 of 48 in the arXiv corpus.
   Both corpora agree. Her drafts carry two each.
2. **Length.** Her sources' median is 169. Her drafts run 47 to 118 words over it. Our 197
   is closer to her stated target than her drafts are.
3. **Percentages: I was too strict.** 5 of 9 ACL 2026 abstracts carry at least one, median 1,
   max 9 (DART). The arXiv corpus (31 of 48 with none) understated what our venue does.
   One result statistic is comfortably normal; the A1b decision stands and is better
   supported than before.

## What to take from her drafts

- The opening question: "Do language models know when a good answer should be left alone?"
- "The revision tax" promoted from ledger Section 6 into the abstract as a named coinage.
- "a choice that single-turn benchmarks never test" as a compressed gap statement.

## Errors in her drafts, do not carry forward

- Version C: "Three human raters and a blind pairwise study of 50 trials". The blind
  pairwise study had TWO raters (Liam, Troy) on 50 pairs (ledger §7). The three raters
  were the separate 64-item calibration (ledger §11).
- All versions imply the decline is confirmed separately in five domains. Stripped, the
  domain differences are NOT significant (chi-square p = 0.555) and the objectivity
  gradient that looks real unstripped (p = 0.019) disappears. Claim uniformity, not five
  confirmations. See ledger §4b.
- Typos in the source: "for every mode", "an domains", "declined or risions",
  "models wrevisions".

## Still outstanding

She did not answer the comprehension question that was asked (read once, say back what it
found). We still have no evidence on whether the abstract lands on a first reading.

---

# Second round of feedback, 2026-09-06

Verbatim, in full:

> It needs more geek and numbers.
>
> Also I'm scanning for that 70% and I did not see it. I was scan for all geek numbers I
> could get. I missed it. Where was that.
>
> Siri tried to "help" me.

## What she was reading

The v12 text emailed 2026-09-03, which does contain the figure, in sentence 7 of 9:
"Among the revisions that do change quality, 70% lower it, and the pattern holds across
all five domains."

So the 70% was present, she went looking for it deliberately, and she did not find it.
That is a placement finding, not a content one, and it is the closest thing we have to
the comprehension read that was asked for.
