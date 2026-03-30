# Research Pipeline: LLM Overcorrection Under User-Stated Quality Thresholds

## Current State (as of 2026-03-29)

| Item | Status |
|---|---|
| GPT-4o trials | **Done** (400/400) |
| Claude Sonnet trials | **In progress** |
| Gemini Flash trials | **In progress** |

---

## Phase 0: Data Collection Completion (BLOCKING)

**Tasks:** Finish Claude Sonnet + Gemini Flash trials.

**Go/No-Go to Phase 1:**
- All 1,200 trials present in `trials.jsonl` with `status=success`
- Each of the 80 cells has exactly 5 runs per model (400/400/400)
- Zero missing cells

---

## Phase 0.5: Literature Review + Response Length Analysis (parallel with Phase 0)

Zero dependency on trial completion — do now.

**Task A: Literature review**
- Sycophancy in LLMs, instruction-following fidelity, overcorrection/overrefusal, threshold/satisficing behavior
- Key venues: ACL/EMNLP/NAACL 2024-2025, COLM, NeurIPS/ICML alignment workshops
- Deliverable: annotated bibliography + positioning statement

**Task B: Response length analysis (free metric)**
- Compute `len(turn2_response)` and `len(turn2_response) - len(turn1_response)`
- Deliverable: summary stats + exploratory figure (length delta vs threshold level)

---

## Phase 1: Full Evaluation (LLM-as-Judge)

**Prerequisite:** Phase 0 complete

**Tasks:**
1. Run `evaluate.py` — primary judge (GPT-4o) on all 1,200 trials
2. Run `evaluate.py --irr` — second judge (Claude Sonnet) on 15% sample (~180 trials)

**Go/No-Go to Phase 2:**
1. **Completion:** All 1,200 trials scored. Parse failures < 2%.
2. **IRR:** Quadratic weighted kappa >= 0.60 on ALL four dimensions
   - 0.40-0.60: Flag in limitations, proceed with caution
   - Below 0.40: **STOP.** Revise rubric, re-run evaluation.
3. **Sanity check:** Baseline (threshold=0) shows lower overcorrection than threshold=100

---

## Phase 2: Analysis + Visualization

**Prerequisite:** Phase 1 passes

**Tasks:**
1. `analyze.py` — all statistical tests
2. `visualize.py` — generate all 6 figures
3. Manual review

**Go/No-Go to Phase 3:**
1. **Signal exists:** At least ONE of:
   - Kruskal-Wallis significant (p < 0.05) for overcorrection across thresholds
   - Spearman correlation significant for at least one model
   - Baseline vs. any threshold shows significant Mann-Whitney difference
2. **Effect sizes reportable:** At least one comparison with rank-biserial r >= 0.20
3. **No artifacts:** No floor/ceiling effects. revision_gate is not 100% "full_revision"

**If signal is weak:** Skip Phase 3, go to Phase 4 with null-result framing.

---

## Phase 3: Deep Statistical Exploration (5 Agents, parallel)

1. **Model comparison** — between-model overcorrection differences
2. **Framing effect** — numeric vs. qualitative systematic differences
3. **Threshold dose-response** — monotonicity, inflection points
4. **Scenario sensitivity** — which writing tasks provoke more overcorrection
5. **Interaction effects** — model×framing, model×scenario, framing×threshold

**Go/No-Go to Phase 4:**
- At least 3/5 agents produce significant + interpretable findings
- No unexplainable contradictions

---

## Phase 4: Adversarial Q&A + Sufficiency Audit

**Step 1: Adversarial Q&A**
- Bot A: Attack methodology, stats, judge reliability, generalizability, confounds
- Bot B: Patch each gap with analysis, limitation acknowledgment, or argument

**Step 2: Sufficiency Audit**
- Bot C: Publication-readiness checklist
- Bot D: Address remaining recommendations

**Step 3: Human eval feasibility** (15-min decision point)

**Go/No-Go to Phase 5:**
- All "fatal" flags resolved
- Checklist >= 80% green
- Human eval decision made

---

## Phase 5: Paper Writing

**Step 1 (parallel):** Paper outline + example curation
**Step 2 (sequential):** Methods → Results → Introduction → Discussion → Limitations → Abstract → Related Work
**Step 3:** Publication-quality figures (camera-ready, color-blind-safe)

---

## Phase 6: Venue Selection + Final Polish

**Decision matrix:**
- Strong effects (multiple significant, r >= 0.3): Main conference (EMNLP, ACL, NAACL)
- Moderate effects: Workshop (TrustNLP, Instruction Following)
- Null result: Workshop or short paper

Then: LaTeX template, final proofread, git tag `v1.0-submission`

---

## Critical Risk Register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| IRR kappa < 0.40 | Medium | **Fatal** | Revise rubric, re-run |
| No significant effects | Low-Medium | Narrative shift | Reframe as null result |
| Gemini Flash stalls | Medium | Lose 1 model | Publish with 2; note limitation |
| Judge parse failure > 5% | Low | Reduced N | Retry logic exists; add structured output |
| Reviewer demands human eval | High | Revision request | Preempt in limitations |

---

## Timeline

| Phase | Duration | Cumulative |
|---|---|---|
| 0: Data collection | 1-3 days | Day 1-3 |
| 0.5: Lit review + length | 4-8 hrs (parallel) | Day 1-3 |
| 1: Evaluation | 3-5 hrs | Day 3-4 |
| 2: Analysis + viz | 2-3 hrs | Day 4 |
| 3: Deep stats | 2-4 hrs | Day 4-5 |
| 4: Adversarial + audit | 3-4 hrs | Day 5 |
| 5: Paper writing | 8-12 hrs | Day 5-8 |
| 6: Venue + polish | 3-4 hrs | Day 8-9 |

**Total: ~9 working days**
