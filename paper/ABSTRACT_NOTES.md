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

## If a hard length cap bites
Current ~210 words. Safe further trims: drop "of the six" in S5; shorten the measurement sentence's
tail to "and nearly vanishes once it is removed". Do not cut the meta-commentary caveat or the
targeted-feedback result; both are load-bearing.
