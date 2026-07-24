# Grounded Skeleton — "Intrinsic Self-Correction Requires Extrinsic Direction"

Every beat below is a phrased topic sentence + its grounding.
- `[D: ...]` = our data, with source (results_FINAL.md = corrected/primary basis).
- `[C: ...]` = citation key(s) in references.bib (66 entries).
- `[TODO-SRC]` = number currently in the paper whose origin file must be located before submission (see flags a1–a6 at bottom).
- Register: no em-dashes, no staccato, measured/scope-fenced observation verbs. Stripped scores are primary; unstripped in parentheses.

---

## ABSTRACT (target ~150–180 words)
1. **Field hook.** Language models are evaluated alone, but deployed in collaboration with users who supply the goal and ask for changes; the quality a user receives depends on what they can contribute to the exchange. `[C: laban2025lost, anthropic2025economicindex]`
2. **The behavior.** The commonest user-side move, asking a model to revise without saying what is wrong, is exactly the move available to users who cannot judge the output. `[C: yang2025underspecification, zhou2026oversight]`
3. **Scale + finding 1 (decline).** Across 720 five-turn conversations spanning six models and forty tasks, undirected revision requests mostly fail to produce revision: genuine revision falls from 39% of responses at the second turn to 13% at the fifth. `[D: 720; 6; 40; 39.3%→13.3%, results_FINAL.md L76–79]`
4. **Finding 2 (degradation).** When models do revise, quality declines by 0.74 levels on a five-point scale (p = 1.0e-4), and the quality-optimal stopping point is the first turn for every model. `[D: −0.74 stripped, p=1.01e-4, results_FINAL.md L758; t*=T1 all, L128]`
5. **Finding 3 (direction is the variable).** A single targeted critique raises quality 1.16 levels, reversing the decline; the problem is the absence of direction, not the capacity to revise. `[D: +1.16, p=5.7e-19, n=177, results_FINAL.md L676]`
6. **Measurement caution.** Measuring any of this requires stripping the meta-commentary models wrap around revisions, which biases an automated judge from 56% to 92% preference for the first draft and nearly vanishes once removed. `[D: 56.5%→91.8%, results_FINAL.md L209; κ 0.569 vs near-chance, L219]`
7. **Takeaway.** Intrinsic self-correction is not enough; it requires direction supplied from outside.

---

## 1. INTRODUCTION  (drafted in introduction_v2.tex; beat map for reference)
1. **Field.** Models are evaluated alone and do well, but the tasks that motivate deployment are human-in-the-loop; quality is a property of the interaction. `[C: liang2023holistic, anthropic2025economicindex, laban2025lost]` `[C: yang2025underspecification]`
2. **Problem.** The one move available to a user who cannot name a fault is undirected revision ("make it better"), which vendor guidance encourages. `[C: zhou2026oversight, openai2025prompting, anthropic2025prompting]`
3. **Prior work.** Self-refinement optimism (Madaan) → fragility without external feedback (Huang) → survey locating the bottleneck in feedback (Kamoi) → multi-turn underspecification (Laban). `[C: madaan2024self, huang2024large, kamoi2024selfcorrection, laban2025lost]`
4. **Gap.** None measures undirected (intrinsic) revision of an already-adequate output across turns, controlling for the meta-commentary artifact. `[C: kamoi2024selfcorrection, huang2024large]`
5. **Contribution + how.** 720 conversations, neutral probe, three RQs, meta-stripping, human validation. `[D: design]`
6. **Results + why it matters.** Decline + degradation + targeted-feedback reversal + the confound; revision robustness deserves evaluation. Closes: "Intrinsic self-correction, on its own, is not enough; it requires extrinsic direction."

---

## 2. RELATED WORK  (one paragraph per theme; each a citation cluster = "sea of blue")

### 2.1 Human-AI interaction and user-side determinants of quality  *(NEW framing paragraph, lead)*
1. **Topic.** A growing body of work treats output quality not as a fixed model property but as an outcome of the interaction, shaped by what the user contributes. `[C: laban2025lost, yang2025underspecification, anthropic2025economicindex]`
2. **Underspecification.** Real prompts are routinely underspecified, and underspecification measurably degrades and destabilizes outputs. `[C: yang2025underspecification]`
3. **Oversight gap.** Users frequently cannot articulate precise intent or validate complex outputs, the condition under which undirected revision is the only available move. `[C: zhou2026oversight]`
4. **Positioning.** We locate the revision request as a user-side variable and ask how its most impoverished form, direction-free revision, affects quality.

### 2.2 Over-reliance and automation bias  *(NEW; the backbone of "why the cost is hidden")*
1. **Topic.** When users cannot verify an output, they tend to accept it, a tendency documented across decades of automation research. `[C: skitka1999automation, parasuraman2010complacency]`
2. **Modern AI-assisted decisions.** Explanations and fluent presentation raise acceptance without improving users' ability to tell right from wrong. `[C: bansal2021whole, bucinca2021trust]`
3. **Reliance as cost-benefit.** Users rely rather than pay the cost of verification, so degraded output passes uncaught. `[C: vasconcelos2023explanations, schemmer2023reliance]`
4. **Link to us.** This is why a quiet quality decline in undirected revision is absorbed rather than noticed, and why the token cost is paid regardless.

### 2.3 Intrinsic self-correction and self-refinement
1. **Optimistic origin.** Self-Refine shows a model can improve its own output, and locates the benefit in feedback that is actionable and specific. `[C: madaan2024self]`
2. **Fragility.** Without external feedback, models struggle to correct reasoning and sometimes degrade it; apparent gains trace to oracle labels or more informative prompts. `[C: huang2024large]`
3. **Mechanism (error location).** Models cannot reliably find their own errors but can fix them when the location is supplied externally. `[C: tyen2024llms, tsui2025selfcorrection]`
4. **Verifier dependence.** Reliable self-correction depends on a strong external verifier or on training, not on intrinsic prompting. `[C: zhang2024small, qu2024recursive]`
5. **Survey + synthesis.** A critical survey locates the bottleneck in feedback generation rather than revision capacity, the exact seam our result sits on. `[C: kamoi2024selfcorrection, kim2024language, shinn2023reflexion]`

### 2.4 Termination and overthinking (knowing when to stop)
1. **Single-response analog.** Reasoning models continue past a completion point and degrade their own answers, a failure to terminate. `[C: chen2024overthinking, chen2025overthinking, ghosal2025overthinking]`
2. **Landscape.** Efficient-reasoning work frames "knowing when to stop" as an open problem. `[C: sui2025efficient]`
3. **Our extension.** Inside a response this manifests as overthinking; across responses it manifests as our revision cliff. The optimal stopping point exists in both and is overshot.

### 2.5 Sycophancy and caving under pressure
1. **Single-turn sycophancy.** Instruction-tuned models comply and avoid disagreement even when inaction is more helpful. `[C: perez2023discovering, sharma2024towards, wei2024simple, openai2025sycophancy]`
2. **Multi-turn caving.** Under repeated pressure or persuasion, correct outputs get revised toward worse ones. `[C: xu2024earth, fanous2025syceval]`
3. **Our extension.** The revision probe is a mild recurring pressure to comply, and the same mechanism produces cumulative degradation.

### 2.6 LLM-as-judge biases (the measurement confound)
1. **Standard practice + known biases.** LLM judges are standard but exhibit self-preference, position, and verbosity biases. `[C: zheng2024judging, panickssery2024llm, koo2024benchmarking, singhal2023long, li2024generation]`
2. **Style over substance.** Judges reward stylistic and formatting cues over content, and this is exploitable. `[C: wu2023style, zhang2024lists, chen2024humans, ye2024justice]`
3. **Our contribution to this thread.** Meta-commentary is precisely such a style cue; any study comparing first-draft and revised outputs with an LLM judge inherits this confound, and we show it flips the conclusion.

### 2.7 Token efficiency and AI cost
1. **Spend is rising.** Enterprise inference spend roughly doubled in under a year, and multi-turn agentic workflows drive the growth. `[C: menlo2025llmmarket, gartner2026agentic, deloitte2026stateofai, mckinsey2025stateofai]`
2. **Adjacent metric.** Our revision tax is adjacent to single-turn over-generation metrics but captures multi-turn revision waste. `[C: borisov2026yapbench]`

### 2.8 Closest work (contrast)  *(keep the Laban contrast sharp)*
- Laban shows multi-turn accuracy loss from underspecification accumulating across turns; ours is fully specified and already sufficient, so degradation is caused by the revision act itself. Complementary, distinct mechanism. `[C: laban2025lost]`

---

## 3. METHODS

### 3.1 Design
1. **Probe.** Five-turn design; neutral probe "Would you like to keep this as your final version, or would you like to revise it?" offers an off-ramp each turn. `[D: methods.tex L5]`
2. **Scale.** 6 models × 40 scenarios × 3 runs = 720 trials (3,600 model-turn observations), temperature 1.0. `[D: results_FINAL.md L343, L637]`
3. **Formalization (VARIANT A or B, TBD).** Index turns by i; define Q_m(i) and i* = argmax_i Q_m(i); we find i*=1 for all models. `[D: t*=T1 all, results_FINAL.md L128]` `[see _formalization_variants.tex]`
4. **Models + scenarios.** Six models named; 40 scenarios across five domains (8 each). `[D: methods.tex L9–29]`
5. **Honest scope note.** Cannot separate the revision act from the probe that offers it; a no-probe control would isolate the mechanism. `[limitation, keep]`

### 3.2 Response classification (genuine vs meta)
1. **Two classes.** At each turn ≥2, classify genuine revision vs meta-response. `[D: methods.tex L31–34]`
2. **Keyword classifier failed.** It missed verbose decline-with-restatement, over-counting revision (135 apparent balanced-panel trials). `[D: 135, results_FINAL.md L15]`
3. **Validated LLM classifier.** Claude Sonnet 4 at T=0; 24.9% genuine (718/2,880); 10 manual corrections (1.4%); yields 50 balanced-panel trials. `[D: 718/2,880, methods.tex L34; 10 corr, results_FINAL.md L11; 50, L16]`
4. **The gap is itself a finding.** 85-trial gap = verbose declines mimicking revision. `[D: 85, results_FINAL.md L14]`

### 3.3 Blind evaluation and the 6→2 recode
1. **Six-level rubric.** Levels 1–6, with 4 = sufficiency threshold. `[D: methods.tex L38–47]`
2. **Non-monotonic Level 6.** "Overdone" is below "Sufficient," so recode 6→2 to a monotonic 1–5 scale. `[D: methods.tex L49–50]`
3. **Judge calibration.** Six candidate judges scored 64 stratified samples vs human mean; Claude Sonnet 4 selected (Spearman r=0.505, QW κ=0.526); next best DeepSeek r=0.340, GPT-4o r=0.140. `[D: results_FINAL.md L315–316; methods.tex L54]` `[TODO-SRC: full candidate table Qwen/Gemini/Llama rows, flag a2]`
4. **Human validation.** Three raters, 64 samples; QW κ 0.406–0.603, Krippendorff α=0.529; binary ≥4 agreement 76.6–82.8%; within-1 81.2–95.3%; binary threshold is the better-validated metric. `[D: methods.tex L57; results_FINAL.md L301–307]`

### 3.4 Meta-commentary stripping
1. **The asymmetry.** 84% of revision-side outputs carry a wrapper vs 14% of Turn-1 outputs. `[D: 84%/14%, results_FINAL.md L238–239; methods.tex L62]`
2. **The confound.** Judges identify the revision side by its wrapping and may trigger "Overdone" on boilerplate. `[C: wu2023style, zhang2024lists]`
3. **Procedure.** Strip all 3,600 outputs with validated regex; 33.3% (1,200) modified and rescored by the same judge at T=0. `[D: 33.3%, results_FINAL.md L655; methods.tex L64]`
4. **Validation.** On 50 balanced pairs, two humans rating stripped content agree with the judge at κ=0.569 vs near-chance (−0.07 to +0.02) on unstripped. All quality results report stripped as primary. `[D: results_FINAL.md L219–221; methods.tex L64]`

### 3.5 Edge-case framework (four controls)
1. Balanced-panel subset (n=50), with selection-bias caveat. `[D: methods.tex L70]`
2. Per-model trajectories (panel is 90% Llama; only Llama powered). `[D: 45/50, results_FINAL.md L42]`
3. T1 quality stratification (12.4% below threshold, 87.6% sufficient). `[D: 87.6%, results_FINAL.md L90]`
4. Compositional audit of the revision-only pool. `[D: methods.tex L73]`

### 3.6 Metrics
- Revision yield; DRP; revision-despite-sufficiency; OCS; revision tax = (T_full − T_t*)/T_t* × 100; semantic similarity (MiniLM); edit ratio (1 − LCS). `[D: methods.tex L78–86]`

### 3.7 Sub-experiments
1. **Targeted feedback.** For outputs rated 1–3, a second instance gets output + specific critique; n=177 matched pairs. `[D: methods.tex L90]`
2. **Self-reflection.** Model shown all versions, asked which to use (n=720). `[D: methods.tex L92]`
3. **Reversibility.** Two humans compare stripped T1 vs last-genuine-revision, blind + position-randomized; κ=0.703; T1 chosen 56.2% of non-tie (CI includes 50%); pre-set 65% bar not cleared. `[D: results_FINAL.md L182–194; methods.tex L94]`

### 3.8 Preliminary gate experiments (Studies 1–2, appendix)
1. **Study 1 (3,840).** Leading probe → 99.9% revise regardless of threshold; evaluative probe → single-digit to low-double-digit; gate is semantic not graded. `[D: appendix L3–8; results_FINAL.md L328]`
2. **Study 2 (1,728).** One prior revision round shifts the gate (GPT-4o 31%→98%); reverse momentum suppresses to near-zero. `[D: appendix L34–46]`
3. **Motivation.** Study 3's neutral probe is a conservative choice; real-world revision-implying prompts would show larger effects.

---

## 4. RESULTS

### 4.1 Models mostly decline to revise
1. **Headline.** Genuine revision declines across turns: 39.3% (T2) → 25.7% → 21.4% → 13.3% (T5). `[D: results_FINAL.md L76–79]`
2. **Decline is verbose and content-shaped.** Keyword vs LLM classifier gap (135 vs 50) = verbose decline-with-restatement. `[D: L14–16]`
3. **Survival varies by model.** Llama 53.3% (64/120) to Gemini 0.8% (1/120). `[D: L504–509]` `[TODO-SRC: "Gemini declines in 98.3%", flag a1]`
4. **Panel composition.** 50 balanced trials = 45 Llama, 3 Qwen, 2 Claude; GPT-4o/DeepSeek/Gemini contribute zero. `[D: L42–47]`
5. **Probe phrasing controls the gate.** Study-1 bimodality; Study-3 neutral probe lands at 39.3% (T2). `[D: results_v2.tex L51]` `[TODO-SRC: pilot n's 18/24/50/3,932, flag a3]`

### 4.2 Quality degrades under undirected revision
1. **The cliff.** Balanced panel: stripped 3.66→2.92, Δ=−0.74 (p=1.01e-4); unstripped −0.94 (p=3.3e-6). `[D: results_FINAL.md L758, L28–34]`
2. **Per-model caveat.** Only Llama powered: stripped −0.69 (p=3.76e-4, r=0.53); Qwen n=3 Δ=−3.00, Claude n=2 Δ=−0.50 directional; do not claim "all models degrade." `[D: L58, L43–44]`
3. **Over-elaboration rises.** Level-6 "Overdone" 5.7% (T1) → 47.9% (T5), 34.4% after stripping; corrects a Llama raw-mean artifact. `[D: L595–599, L741–745]`
4. **Pooled trajectory (triangulation).** Stripped 4.11→3.07, Δ=−1.04 (unstripped −1.26); compositional-bias caveat; direction consistent. `[D: L714–719]`
5. **Domain variation.** Model identity explains far more than domain (model range 71.9pp vs domain 13.5pp); code elicits most revision (implicit critique built in). `[D: results_v2.tex L115]` `[TODO-SRC: variance stats/χ²=35.63, flag a5]`; all 5 domains negative, 4/5 significant, data_logic marginal. `[D: L728–732]` `[TODO-SRC: per-domain p-values, flag a4]`
6. **Revision despite sufficiency.** 39.2% (368/938) of sufficient outputs are revised next turn (stripped 39.6%). `[D: L91–92]`

### 4.3 Targeted feedback restores quality
1. **Headline.** Stripped targeted 4.68 vs generic 3.53, Δ=+1.16 (p=5.7e-19, n=177); unstripped +0.25 (p=3.8e-3). `[D: L676]`
2. **Why unstripped understates.** Targeted revisions carry minimal meta (9/177 = 5%). `[D: L679]`
3. **Per-model.** All five powered models significant; stripping reveals Llama/Qwen/GPT-4o benefit whose generic baselines were meta-inflated. `[D: L687–692]`
4. **Central contrast.** Undirected −0.74 vs directed +1.16: the problem is direction, not capacity. `[D: as above]`

### 4.4 The revision tax
1. **t* = Turn 1 for all six models.** All post-T1 tokens are waste under a quality criterion. `[D: L128, L151]`
2. **Magnitude.** 62.1% of output tokens spent past t*; aggregate tax 164.2%; per-model 23.4% (Gemini) to 81.3% (Llama). `[D: L147–149; per-model L137–142]`
3. **Framing.** Adjacent to YapTax but multi-turn. `[C: borisov2026yapbench]`
4. **(Optional) enterprise projection.** $323–$65,678/yr per 500-person org. `[D: results_FINAL.md S7 L536–549]` `[decide whether to restore; currently dropped]`

---

## 5. DISCUSSION

### 5.1 Evaluate, then direct
1. **Opposites, not a spectrum.** Undirected degrades; a single critique improves. Failure is of will-under-no-direction, not capacity. `[D: −0.74 vs +1.16]`
2. **Likely training origin.** RLHF rewards visible effort, so revising-when-asked is reinforced over correctly declining. `[C: singhal2023long, skalse2022defining, sharma2024towards]`
3. **Remedy.** Users: withhold the request until you can name the fault. Systems: put an evaluation step before the revision step. `[C: madaan2024self (actionable+specific)]`

### 5.2 The cost is real and mostly hidden
1. **Absorbed loss.** A user who cannot tell degraded from improved absorbs the loss, and pays the tokens regardless. `[C: bucinca2021trust, vasconcelos2023explanations, parasuraman2010complacency]`
2. **Two compounding costs.** Wasted generation past t* (62%) plus verbose meta-responses that change nothing. `[D: 62.1%, L149; meta share]`
3. **Scales with adoption.** Agentic multi-turn workflows are where undirected loops live; caps bound spend but not the error. `[C: gartner2026agentic, menlo2025llmmarket, claudecode2025loop]`

### 5.3 Revision robustness deserves measurement
1. **Wrong place.** Benchmarks score first answers; first drafts are already sufficient 87.6% of the time. `[D: 87.6%, L90]`
2. **Two properties come apart.** Strong first-draft quality is not the willingness to stop; standard eval measures neither. `[C: liang2023holistic]`
3. **Proposal.** Evaluate revision robustness (hand a model its own sufficient output; will it decline to worsen it?) alongside first-turn capability.
4. **Measurement caveat generalizes.** Any first-vs-revised LLM-judge comparison inherits the meta-commentary confound; stripping should be standard. `[C: wu2023style, zhang2024lists, panickssery2024llm]`

---

## 6. LIMITATIONS  (keep the honest eight, grounded)
1. Panel dominated by Llama (45/50). `[D: L42]`
2. Evaluator judges all models including itself; mitigated by calibration (r=0.505). `[D: L315]`
3. Moderate inter-rater reliability (κ 0.41–0.60, α=0.529). `[D: L301–307]`
4. Temperature 1.0 only. `[D: methods.tex L7]`
5. 40 tasks are a convenience sample. `[D: methods.tex L11]`
6. Neutral probe may still prime revision; no-probe control needed. `[keep]`
7. Small per-domain cells; magnitudes directional. `[D: L728–732]`
8. Reversibility near chance after stripping (56%, CI includes 50%, 65% bar not cleared). `[D: L182–185]`

---

## 7. CONCLUSION
1. **Restate the two failures.** Most decline to genuinely revise; those that revise get worse. `[D: 39→13%; −0.74]`
2. **The fix.** Targeted feedback, not more turns (+1.16). `[D: L676]`
3. **Three audiences.** Users: specify the fault. Systems: quality gate before revision loop. Field: evaluate revision robustness alongside single-turn capability.
4. **Close on the title.** Intrinsic self-correction requires extrinsic direction.

---

## OPEN GROUNDING FLAGS (must resolve before submission)
- **a1** "Gemini declines in 98.3%" (results_v2.tex L40): inferred, not computed. Compute per-turn Gemini META count or soften to "near-universally."
- **a2** Judge candidate table rows for Qwen/Gemini/Llama + QW κ (appendix): source is `selected_judge.json`/`judge_calibration.jsonl`; locate and cite.
- **a3** Study-1 pilot probe n's (18/24/50/3,932) in results_v2.tex L51: from an unprovided Study-1 pilot file; locate or drop.
- **a4** Per-domain Wilcoxon p-values (4/5 sig, data_logic p=0.058): deltas sourced, p-values not; recompute.
- **a5** Domain-vs-model variance stats (71.9pp/13.5pp, χ²=35.63, code 34.0%): not in provided data files; locate the computation or recompute.
- **a6** Enterprise projection ($323–$65,678): exists in results_FINAL.md S7 but dropped from draft; decide restore vs cut.
- **basis note** study3_results.json is the OLD keyword-classifier analysis. Never cite its rq* rates; results_FINAL.md is the corrected primary basis. Old superseded numbers (68/50/42/35% rates, 62.4% RDS, +2.00 targeted, 93.3%/83.7% reversibility, balanced n=135) must never re-enter the paper.
- **bib note** New bib entries use first author + "and others" where full author lists were not verified; complete author lists before submission. Two keys chen2024overthinking (2412.21187) and chen2025overthinking (2508.17627) are distinct papers; keep both, consider renaming for clarity.
