# Paper Revision Plan — post-Ali mentor call (NAACL, Oct deadline)

Target: NAACL (San Francisco), October deadline. Goal: reposition the paper to read as
rigorous **human-AI interaction** science, not a practitioner blog post / LinkedIn tip sheet.

The results are considered DONE by the mentor ("you passed the big beast"). This pass is about
**framing, structure, register, title, and figures** — the skeleton first, style second.

---

## PART 1 — DIAGNOSIS: everything Ali flagged + the fix

### A. Scientific framing / positioning (the biggest problem)
| # | Issue (Ali) | Fix |
|---|-------------|-----|
| A1 | Paper reads as practical advice / "pro tip for a Claude user" — helps a reader, not the field. Reviewers (and LLM triage at 30k-submission venues) may filter out low-science papers. | Reframe every claim around *advancing knowledge*, not *advising a user*. Lead with a research question, not a life hack. |
| A2 | Not situated within a research field. It just presents findings. | Situate explicitly in **human-AI interaction**: models are strong on solo benchmarks but real "economic" tasks involve humans; **user-side factors** (e.g. a rushed user who won't give feedback vs. one who iterates) determine output quality. That is a named field with a community. Frame our RQ as a question *within* it. |
| A3 | Missing the standard NLP intro arc. | Adopt the 6-beat skeleton (see Part 2): present field → thicken plot (problem) → prior work → what they didn't do (gap) → our step in (contribution/how) → results → why it matters. Ali's exact words. |
| A4 | Not enough citations; a real intro/related work should be "a sea of blue." | Increase citation density, especially where we introduce the field and prior work. Every field-level claim gets a citation cluster; contested claims get the biggest clusters (per Kamoi). |

### B. Writing register / style
| # | Issue | Fix |
|---|-------|-----|
| B1 | "We show that it does not." reads as LinkedIn, not science. You **convey**, you don't **claim/convince**. | Rewrite assertive hype into measured, attributed, scope-fenced prose. "Our experiments confirm... an average drop of X across N tasks" (Laban), not "we show that it does not." |
| B2 | Claude tells: **em-dashes** (2025's obvious tell) and **staccato** ("The answers are consistent."). | Purge em-dashes (already a standing user rule). Kill one-clause punchy fragments. Vary meter; write like the survey/Laban. |
| B3 | Meter/register is "really off"; first section (abstract) is better because more time spent. | Draft prose myself first (human draft), use LLM for brainstorming/scaffolding only, not copy-paste. Deep-read neighbors to internalize the target sound. |
| B4 | Band-aid fixes (telling Claude "don't do that") won't work. | Rebuild from skeleton up, not surface edits. |

### C. Title
| # | Issue | Fix |
|---|-------|-----|
| C1 | Current title "The More You Ask, The Worse It Gets: How LLMs Waste Tokens Revising Past Their Own Best Output" over-emphasizes **tokens** — the paper is not mainly about tokens. Misrepresents scope. | Retitle around the real thesis: undirected revision degrades quality / models can't self-direct revision. Tokens are a secondary cost result. |
| C2 | "X: Y" colon format is overdone; reviewers are tired of it. Models default to it (all 20 title suggestions have that shape). | Use a bold **5–6 word plain-language** title, **no colon**, ideally a full declarative sentence with one vivid verb we later formalize (cf. "LLMs Get Lost in Multi-Turn Conversation"). Standing out = economics; don't do the first thing everyone does. |

### D. Figures
| # | Issue | Fix |
|---|-------|-----|
| D1 | Main figure (Rachel spring-sale email) uses **fabricated/illustrative** content ("DEER VALLUED CUSTMER"), inspired-by not real. As a scientist Ali doesn't believe it — worst reader reaction is disbelief. Graphics/craft are excellent (shading, grayed-out revisions, layout — keep the craft). | Replace fabricated chat with **real excerpts from our actual data**. Cherry-pick 1–2 genuine trials where quality visibly degrades after over-revision. Keep the visual design; swap the content for real, cited transcript excerpts. |
| D2 | The qualitative "High/Low" token-cost vs. quality crossing-lines graph has **no axis values** — not acceptable. Reads as "they didn't really count tokens." | Either replace with a **real quantitative** plot (actual token counts + quality scores with numeric axes) or **remove** it. Ali leans remove-or-quantify. |
| D3 | Combined figure is **too big** for a cover/teaser figure. | Split: a compact real-data teaser (Fig 1) + possibly a system-design flowchart as a separate figure. |
| D4 | Main figure(s) selection still open. A system-design flowchart is under consideration. | Decide final teaser: one strong real-data example may suffice; flowchart optional. Do this LAST — writing does most of the work. |

### E. Mathematization (optional weight-adder)
| # | Issue | Fix |
|---|-------|-----|
| E1 | Paper feels "light"; could sound heavier "in cool ways." | Formalize key variables. Ali's example: let **I = number of revision iterations**; define quality as a function of I; potentially derive/report the **optimal I\*** per model at which quality peaks (we already have this: I\*=1 / Turn 1). Light notation in Methods, not overkill. Cf. Laban's aptitude/unreliability + P1–P5. |

### F. Process / logistics
- Rebuild intro skeleton (6 beats) via model-assisted brainstorming from the transcript. (Liam)
- Replace fabricated figure content w/ real excerpts. (Liam)
- Replace/remove qualitative token graph. (Liam)
- Deep-read the 4 neighbor papers for tone + citation density. (Liam — in progress via this session)
- Contact Ali in ~1–2 weeks once skeleton is stronger; intensive collab in the month before Oct.
- Housekeeping: hallucinated-citation guard — only cite papers we can actually open/verify.

---

## LOCKED DECISIONS (this cycle)
- **Scope:** full Introduction rewrite first (done: `introduction_v2.tex`), then outward.
- **Fig 1:** REAL story-opening excerpt `s3_worker__llama-3.3-70b__story_opening__run3` [4,4,4,3,2].
  Keep existing visual design; swap fabricated Rachel email for real T1 vs T5 excerpts. Build figure LAST.
- **Token-cost crossing graph:** remove or replace with quantitative (real token counts). Decide at figure step.
- **Mathematization:** keep BOTH variants (`_formalization_variants.tex`), decide at Methods rewrite.
- **Title:** LOCKED = **"Intrinsic Self-Correction Requires Extrinsic Direction"** (research register;
  field-grounded term from Kamoi/Huang; earned in intro opening + closing sentence). Set in main.tex.
- **Register:** no em-dashes, no staccato, measured/scope-fenced observation verbs throughout.

## PART 2 — TARGET INTRO SKELETON (Ali's 6 beats, NLP-standard)
1. **Present the field.** Human-AI interaction: models excel on solo benchmarks, but real economic tasks are human-in-the-loop; output quality is co-determined by user-side behavior.
2. **Thicken the plot (problem).** A dominant user-side behavior is *undirected* revision — "make it better" with no specification of what is wrong — used precisely by users who cannot judge/direct the output.
3. **Prior work.** Self-refinement / self-correction literature (Madaan Self-Refine; Huang; Kamoi survey; Laban multi-turn).
4. **Gap (what they didn't do).** Prior work studies self-correction *with* feedback or *task accuracy* under underspecification; none measures what undirected revision does to *already-sufficient* output quality across turns, controlling for meta-commentary.
5. **Our step in (contribution + how).** 720-conversation, 6-model, 40-task neutral-probe design; validated classifier; meta-commentary stripping; targeted-feedback contrast.
6. **Results + why it matters.** Undirected revision degrades quality and mostly triggers non-revision; targeted feedback reverses it; implication for how human-AI systems should gate revision.

---

## PART 3 — CALIBRATION NOTES FROM NEIGHBOR PAPERS
### Laban 2025 (gold standard to match)
- Title = declarative sentence, plain verb ("get lost"), no colon, scope-bounded; later formalized as the "lost in conversation phenomenon."
- 9-paragraph funnel intro; decomposes the finding and NAMES the phenomenon in the intro.
- Headline number ALWAYS chaperoned by scope ("39% across six generation tasks"); verbs of observation ("our experiments confirm," "we observed"), not assertion.
- Intro citations sparse+argumentative; related work dense+taxonomic (clustered by function); overflow survey pushed to appendix.
- One formal metric block (aptitude A^90 / unreliability U^90_10) turns a scary number into an attributable measured claim.
- Teaser Fig 1 = mixed: illustrative cartoon side panels for pedagogy + REAL-DATA center scatter on the formal axes. Self-contained caption.
- Practical advice sequestered into audience-segmented Implications section, each rec backed by a controlled experiment, framed as provisional stopgap toward a principled fix.

### Kamoi 2024 (the survey — critical-tone model)
- Title = question + genre label, italicized "Actually"; no hype colon.
- Intro P1 fuses field-is-big + field-is-in-conflict; P3 previews findings as a numbered parallel list.
- Register: strong negatives always scope-fenced (task type / feedback source / "no prior work shows..."), attributed ("we find," "our analysis highlights").
- Adopt their terminology: **intrinsic self-correction**, **direct refinement** (revision without explicit feedback — our exact setup), **self-detect** vs **self-correct**, "recognizing errors is easier than avoiding them" (Saunders). Strongest claim carries densest citation cluster.

### Huang 2024 — "Large Language Models Cannot Self-Correct Reasoning Yet" (no colon, declarative)
- Our strongest ally. Best citable line: *"simply integrating the feedback into the initial instruction can yield better results, and self-correction again decreases performance"* — directly contrasts targeted vs undirected. Also: *"LLMs struggle to self-correct their responses without external feedback, and at times, their performance even degrades after self-correction."*
- Term to adopt: **intrinsic self-correction** (no external feedback). Register: scope-fenced negatives, "our research indicates," refinements via nuance paragraphs (oracle labels, equal-cost, prompt design).

### Madaan 2024 — "Self-Refine: Iterative Refinement with Self-Feedback" (colon; the optimistic prior we complicate)
- The prior we sit against. It is fully formalized (M, x, y0, fb_t, y_{t+1}, prompts p_gen/p_fb/p_refine, Algorithm 1) — a template for our own light formalization of iterations I.
- Best citable line (defines what makes feedback work — our targeted half): *"By 'actionable', we mean the feedback should contain a concrete action... By 'specific', we mean the feedback should identify concrete phrases in the output to change."* Self-Refine works because its feedback is targeted, not merely because revision occurs.

---

## PART 4 — FIG 1 REAL-DATA CANDIDATES (mined from 720 trials)
Joined worker_trials.jsonl + stripped_rescore_full.jsonl + genuine_meta_labels.jsonl.
Criteria: balanced panel (genuine revision every turn), starts sufficient, visible monotonic decline.

**TOP PICK — `s3_worker__llama-3.3-70b__story_opening__run3`** (creative, stripped scores [4,4,4,3,2])
- Task: 150-word atmospheric story opening, lighthouse keeper finds something washed ashore.
- Genuine revision every turn. Degradation is VISIBLE to any reader: clean atmospheric prose (T1)
  → progressively overstuffed purple prose by T5 (comma-spliced, over-elaborated, "Overdone").
- Why it wins for a teaser: believable real data, accessible task, the failure mode (over-elaboration)
  is legible without domain expertise. Starts "Sufficient" (4), ends "Incomplete" (2).

**Alt 1 — `s3_worker__llama-3.3-70b__cover_letter__run1`** (writing, [4,4,4,2,2])
- Cover letter gets shorter/more generic; adds self-congratulatory meta ("I think this is a strong
  final version!"). Good, slightly less visually dramatic than the story.

**Alt 2 — `s3_worker__qwen-3-235b__backup_script__run2`** (code, [5,4,2,2,2])
- Biggest clean drop, starts at 5 (Polished). Code degradation is harder to show in a teaser but
  strongest score delta; good if we want a technical example.

Recommendation: lead with story_opening (readability), optionally pair with a code example.

## PART 5 — CITATION INVENTORY
references.bib has 45 entries. Strong for: self-correction (madaan, huang, kamoi, shinn, kim),
multi-turn (laban, zhang2020dialogpt, thoppilan), overthinking (chen2025, ghosal2025), sycophancy
(perez, sharma, wei, openai2025sycophancy), reward hacking (skalse, singhal, goodhart), cost
(menlo, gartner, deloitte, mckinsey, goldman, thompson), prompting advice (openai/anthropic2025prompting).
GAPS to fill for the human-AI-interaction field intro (agent researching): Anthropic Economic Index /
LLM workplace-usage study; underspecification-in-real-prompts; non-expert oversight / expertise gap.

### The dialectic to exploit
Madaan (optimistic: actionable+specific self-feedback helps) vs Huang (skeptical: undirected intrinsic correction degrades; gains trace to oracle labels/informative prompts). **Our thesis sits on the seam: the operative variable is whether feedback is targeted, not whether revision happens.** Kamoi is the survey that adjudicates; Laban is the multi-turn cousin (different mechanism: underspecification vs the revision act itself).
