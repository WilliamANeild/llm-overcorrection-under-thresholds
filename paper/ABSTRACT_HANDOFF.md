# Abstract handoff — context dump for another LLM

You are taking over refinement of the ABSTRACT for an NLP paper. Everything you need is below:
the current text, the ground-truth statistics with sources, the hard style rules, the human's
preferences (learned over many iterations), and the open decisions.

---

## 1. Paper at a glance
- **Title (LOCKED):** *Intrinsic Self-Correction Requires Extrinsic Direction*
- **Venue / deadline:** targeting NAACL, October 2026 deadline. Single author (Liam Neild, Emory).
- **Thesis:** When a user asks a model to revise without saying what is wrong (undirected /
  *intrinsic* revision), the model mostly declines to genuinely revise and, when it does, degrades
  an already-adequate output. A single specific (extrinsic) critique reverses this. The operative
  variable is whether feedback is directed, not whether revision happens. Framed within human-AI
  interaction; the axis is internal vs external feedback (true for humans and models alike).
- **Reframe goal (from advisor Ali):** read as rigorous science, not a practitioner blog post.
  Situate in a field, avoid AI-writing tells, avoid the "X: Y" colon title format.

## 2. CURRENT ABSTRACT (verbatim, file: paper/sections/abstract_v2.tex, wired into main.tex)
> Large language models are absorbing more workplace tasks, increasingly handed to them by users who
> cannot fully judge or direct what comes back. When the output needs improving, those users do the
> only thing they can: ask the model to make it better, without saying what is wrong. Often the
> output is already good enough and the right move is to stop, but neither side can tell, so the
> revising continues. Across five-turn conversations spanning six models, on work that ranges from
> writing code and reasoning over data to business documents and creative writing, models asked to
> revise without direction mostly decline to revise at all, dressing refusal as engagement, and
> genuine revision falls from 39% of responses at the second turn to 13% by the fifth. When they do
> revise, they degrade their own work. Quality falls 0.74 levels on a five-point scale
> (p = 1.01 x 10^-4), the first version is the strongest for every model, and 62% of output tokens
> are spent past the point of peak quality. The failure is one of direction, not capacity: a single
> targeted critique raises quality 1.16 levels and reverses the decline. Measuring any of this takes
> care, since the meta-commentary models wrap around their revisions inflates an automated judge's
> preference for the first draft from 56% to 92%, an effect that nearly vanishes once the commentary
> is stripped. As models take on work their users cannot direct, the remedy is not more iteration but
> evaluation: tell the model what is wrong, or do not ask it to revise.

Current length ~245 words. Numbers in it: 39, 13, 0.74, p=1.01e-4, 62, 1.16, 56, 92 (plus "six",
"five-turn"). Structure: workplace framing -> the behavior -> when-to-stop motivation -> decline
finding -> degradation + tax -> direction fix -> measurement caveat -> actionable close.

## 3. GROUND-TRUTH STATISTICS (every number must trace here; source = results_FINAL.md, the
CORRECTED/primary basis. NEVER use study3_results.json — it is the OLD keyword-classifier analysis
with superseded numbers.)
- Scale: **720** five-turn conversations = **6 models x 40 tasks x 3 runs**; 3,600 model responses.
  Models: Claude Sonnet 4, GPT-4o, Gemini 2.5 Flash, Llama 3.3 70B, Qwen 3 235B, DeepSeek V4.
- Tasks: 40 across **5 domains** (8 each): code, data logic, analysis, writing, creative writing.
  (In the abstract these are described as a RANGE, not counted — see style rule 7.)
- Genuine-revision decline: **39.3% (T2) -> 25.7% (T3) -> 21.4% (T4) -> 13.3% (T5)**. In prose "39% ... to 13%".
- Quality cliff (primary = stripped, balanced panel n=50): **-0.74 levels** on a 5-pt scale,
  **p = 1.01e-4**. (Unstripped -0.94, p=3.3e-6. Llama-only n=45: -0.69, p=3.76e-4.)
- Optimal stopping point **t* = Turn 1 for all six models** ("the first version is the strongest").
- Revision tax: **62.1%** of output tokens spent past t* (aggregate tax 164.2%).
- Targeted feedback: **+1.16 levels** (stripped), p=5.7e-19, n=177 matched pairs. (Unstripped +0.25.)
- Meta-commentary confound: inflates an LLM judge's first-draft preference **56% -> 92%**
  (56.5% -> 91.8% on the 50 balanced pairs); near-vanishes when stripped (human-judge agreement
  kappa=0.569 stripped vs near-chance unstripped).
- Human validation: 3 raters, judge = Claude Sonnet 4 (Spearman r=0.505 vs human mean).
- All six grounding flags (a1-a6) are RESOLVED and reproducible via
  scripts/study3/verify_grounding_flags.py.

## 4. HARD STYLE RULES (non-negotiable; audit before returning any draft)
1. **No em-dashes anywhere** (standing rule for all writing).
2. **No "AI tells":** no rule-of-three tricolons for rhythm, no "not just X but Y" seesaws, no
   significance-adverbs (crucially, notably, quietly, importantly, moreover), no hedge-stacking
   (one hedge per claim max), no over-balanced parallel clauses. Vary sentence length.
3. **Observation verbs** (find/observe/show/falls), not hype verbs. Plain over Latinate.
4. **Modeled on four exemplar abstracts** (on the author's desktop): Kamoi 2024, Laban 2025,
   Huang 2024, Madaan 2024. These use 0-2 numbers and state findings in words; that was the target
   before the human asked for the result numbers back (see preferences).
5. Register audit command:
   `python3 -c "s=open('paper/sections/abstract_v2.tex').read(); print('em-dashes',s.count(chr(8212)))"`

## 5. THE HUMAN'S PREFERENCES / DECISIONS (learned across ~10 iterations — READ THIS)
- **Voice:** likes the ORIGINAL abstract's voice (punchy, real-world): "absorbing more workplace
  tasks", "the only thing they can", "dressing refusal as engagement", and the close "the remedy is
  not more iteration but evaluation: tell the model what is wrong, or do not ask it to revise".
  Dislikes drafts that "sound like one of those papers" (over-templated / generic).
- **Spine:** the abstract should "come from a place of WHEN TO STOP" (the output is already good
  enough, the right move is to stop, but neither side can tell). This is the current organizing idea.
- **Numbers, the tricky part (oscillated):** first said too many numbers / "no other papers write
  with this many numbers so early" -> we stripped to zero. Then pasted the number-heavy original and
  said "dont take those [numbers]" -> we restored 0.74/p, 1.16, 56->92. So the CURRENT stance:
  KEEP the result numbers, but do not overload. Most recent instruction: **do NOT state "forty
  tasks" as a count; describe the RANGE of task types instead** (done). Open question they raised:
  it may still feel like "too many numbers" — the safest single trim is the p-value (abstracts rarely
  carry p-values), but confirm before cutting any number they restored.
- **720:** the human said a raw trial count like "720" is "not something I've ever seen" in an
  abstract; it is currently OUT. A 23-abstract survey confirmed exact raw trial counts almost never
  appear (convention = models x tasks scope, or rounded floors like "200,000+"). Do not reintroduce
  720 unless asked.
- **Human/model framing:** humans self-correct too; do NOT frame it as humans-good-models-bad. The
  correct axis is internal (self-generated) vs external feedback. (Verified anchors, for intro not
  abstract: Huang 2024 "source of feedback ... purely internal ... or external"; Kamoi 2024; human
  side Gehring 1993 error-monitoring, Hattie & Timperley 2007, Dunning 2004 / Davis 2006 weak
  self-assessment.)
- **First sentence must be conceptually correct:** self-correction is a model improving ITS OWN
  output; do not define it "by asking the model" (an earlier draft did this and was wrong).
- Process preference: the human is comfortable with heavy iteration and wants it to be "perfect."
  They value grounding every claim and using multiple drafting/critique passes.

## 6. OPEN DECISIONS for you to resolve with the human
1. Is ~245 words acceptable, or trim toward ~200? (If trimming: cut the p-value first, then compress
   the measurement sentence; do NOT cut the meta-commentary caveat or the targeted-feedback result.)
2. Keep all restored numbers, or drop the p-value?
3. Should the close nod to the title's "intrinsic/extrinsic" wording, or keep the current
   more-actionable "not more iteration but evaluation" close (human currently prefers the latter)?

## 7. Repo pointers
- Abstract: paper/sections/abstract_v2.tex (input into paper/main.tex)
- Full provenance + register audits + number-discipline notes: paper/ABSTRACT_NOTES.md
- Grounded stats ledger + old-vs-corrected basis warnings: results_FINAL.md; also paper/SKELETON.md
- Other rewritten sections (same register): introduction_v2.tex, related_work_v2.tex
- Verify stats: scripts/study3/verify_grounding_flags.py
- Bib: paper/references.bib (66 entries). No local LaTeX toolchain; author compiles on Overleaf.
