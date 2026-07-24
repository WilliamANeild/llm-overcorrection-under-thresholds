# Abstract — provenance and register audit

Built in two phases: 2 research agents reverse-engineered the abstracts of the four desktop papers
(Kamoi 2024, Laban 2025, Huang 2024, Madaan 2024); 4 writing agents each drafted one rhetorical beat
with alternatives; the final text was synthesized and audited by hand.

## Template distilled from the four exemplars
1. Flat copular/definitional first sentence, object of study as subject (Kamoi: "Self-correction is
   an approach to improving responses from large language models"; Laban: "LLMs are conversational
   interfaces"). No hook, no "As LLMs become increasingly...".
2. One prior-work / status-quo line.
3. A single gap pivot spent once (Huang "Nevertheless,", Kamoi/Laban "However,"/"Although").
4. Method pivot on the fixed phrase "In this work, we ...".
5. Result sentences with the DATA as grammatical subject and an observation verb (find/confirm/show);
   every number chaperoned by its scope ("39% ... at the second turn", "across six models").
6. Close on the verdict, cool and plain (Huang cools to future work; we land on the thesis). One
   plain/colloquial word where AI would go Latinate ("make it better", "first try").

## Anti-AI-tell audit (all pass)
- em-dashes: 0 ; prose colons: 0
- no rule-of-three tricolons for rhythm; no "not just X but Y" seesaw
- no significance-adverbs (crucially/notably/quietly/importantly/moreover)
- one hedge per claim (only "reliably" in the close)
- sentence-length variation (roughly 15/21/34/26/42/35/35/19 words)
- data-as-subject results: "Genuine revision falls...", "quality falls...", "62% ... are spent...",
  "one specific critique ... raises ...", meta-commentary "lifts ... from 56% to 92%"

## Beat provenance (which candidate won, and the hand-edits)
- Beat 1 (open + setup): agent candidate A (copular "Self-correction is ...", Kamoi-aligned, title
  coherence), lightly reworded.
- Beat 2 (method + decline): agent candidate B, data-as-subject "Genuine revision falls from 39% ...
  to 13%". Dropped "asking for a revision" in S2 for tightness.
- Beat 3 (degradation + tax): agent candidate A, "quality falls by 0.74 levels ... peaks at the first
  turn ... 62% ... spent past that peak".
- Beat 4 (direction + caveat + close): agent candidate B, with two hand-edits: (i) integrated
  "direction rather than capacity" into the preceding clause so it is not a staccato fragment;
  (ii) removed the colon from the measurement sentence ("Measuring this takes care, because ...").

## Every number traces to results_FINAL.md
- 720 conversations, 6 models, 40 tasks (methods)
- 39% (T2) -> 13% (T5) genuine revision (L76-79)
- -0.74 levels, p=1.0e-4 stripped balanced panel (L758)
- t*=Turn 1 for all six models; 62.1% tokens past peak (L128, L149)
- +1.16 levels, p=5.7e-19, n=177 targeted feedback (L676)
- judge first-draft preference 56% -> 92%, near-vanishes stripped (L209, L219)

## v4 number-discipline pass (the important one)
Advisor note: the draft front-loaded ~13 numbers; real abstracts in this space use 0-2. Exemplar
counts: Huang 0, Kamoi 0, Laban 1 (the 39%), Madaan 2. Fix: every RESULT statistic moved to the body
(39->13%, -0.74, p=1e-4, 62%, +1.16, p=5.7e-19/n=177, 56->92%), findings restated qualitatively with
scope carried in words ("for every model the first version is the best one"; "mostly decline to
genuinely revise ... this deepens as the conversation continues"). Only the study scale remains
(720 five-turn conversations, six models, forty tasks), Laban/Madaan-style. Final: 1 numeral, 0 %,
0 p-values, 0 colons, 0 em-dashes, one antithesis ("direction rather than capacity"), plain close.
Built with a fresh writer agent (3 qualitative drafts) + an adversarial critic agent (number audit),
synthesized by hand.

## v5 scale-convention pass (survey of 23 real abstracts)
Two observant agents surveyed how empirical LLM papers state study scale in the abstract (n=23 +
the 4 exemplars). Distribution: scope by models/tasks (bucket c) 48% (plurality); exact raw count
22% but ALWAYS a released-benchmark size in the 1,000s-100,000s (MT-Eval "1170 queries", Malberg
"30,000 tests", red-teaming "214,271 attempts"); rounded floor ("200,000+", "over 240K") only for
large datasets; qualitative/none 18%. A bare mid-size exact N like "720 conversations" appears
essentially NOWHERE and reads as oddly specific and small. Closest analogues Madaan ("across 7
diverse tasks... using GPT-3.5 and GPT-4") and Sharma ("five state-of-the-art AI assistants across
four varied tasks") both use models x tasks scope.
FIX: dropped "720 five-turn conversations" -> "across six models and forty tasks, running five-turn
conversations...". Result: ZERO arabic numerals in the abstract; scale carried by spelled scope
words. The exact "720 = 6 models x 40 tasks x 3 runs" goes in the experimental-setup section.

## v7 LOCKED — internal-vs-external-feedback framing (the correct axis)
Advisor: humans self-correct too; the real distinction is internal vs external feedback. Reframed the
opening on the SOURCE OF FEEDBACK (true for humans and models alike), not a human-vs-model contrast.
Verified, citable anchors (gathered by a research agent; use in intro/related work, NOT the abstract):
- Huang 2024 (arXiv:2310.01798): "A pivotal distinction lies in the source of feedback ... Is it
  purely internal, originating solely from the LLM, or does it draw from external inputs?"; intrinsic
  = "based solely on its inherent capabilities, without the crutch of external feedback."
- Kamoi 2024 (TACL, arXiv:2406.01297): "Intrinsic self-correction prompts LLMs to generate feedback
  on their own responses"; external = tools / knowledge / oracle.
- Human side: Gehring 1993 (Psych Science) "Humans can monitor actions and compensate for errors"
  (internal error-monitoring); Hattie & Timperley 2007 (external feedback d=0.79); Kluger & DeNisi
  1996 FIT (external agent; caveat "over 1/3 ... decreased performance"); Dunning 2004 / Zell &
  Krizan 2014 / Davis 2006 JAMA (self-assessment tracks performance only weakly).
- HONESTY CAVEAT to preserve anywhere we lean on this: external feedback helps ON AVERAGE, not
  uniformly (Kluger & DeNisi). The human/LLM parallel is our framing, not any single source's claim.
Opening now: both people and models revise; what matters is the feedback and whether it comes from
outside; a model told only to "make it better" must correct itself with no external signal (= the
non-expert user's case). Pays off in the close "Intrinsic self-correction ... is not enough; the
direction has to come from outside." TODO(optional): add these 4-6 human-feedback cites to the intro
and a short definitions line in Related Work 2.3 to ground intrinsic/extrinsic.

## If a hard length cap bites
Current ~210 words. Safe further trims: drop "of the six" in S5; shorten the measurement sentence's
tail to "and nearly vanishes once it is removed". Do not cut the meta-commentary caveat or the
targeted-feedback result; both are load-bearing.
