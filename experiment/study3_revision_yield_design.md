# Study 3: Revision Yield - The Complete Experiment Design

## Central Thesis

LLMs systematically over-revise not because their outputs need improvement, but because conversational context distorts their quality judgment. This wastes user resources, degrades output quality, and misallocates completion authority.

Studies 1-2 established the behavior. Study 3 establishes the mechanism, the cost, and the solution.

## Key Concepts

### Revision Yield

**Revision Yield** is the quality improvement gained per token spent on revision.

- **Marginal Revision Yield (MRY)**: Quality gained per token on a specific revision turn
- **Cumulative Revision Yield (CRY)**: Total quality improvement divided by total revision tokens
- **Cost-Adjusted Revision Yield (CARY)**: Quality weighted by exponential cost penalty (adapted from EPI, McDonald et al. COLING 2025)
- **Diminishing Return Point (DRP)**: The first turn where MRY drops to zero or below
- **Overcorrection**: When the working model revises beyond the DRP

### Formal Definitions

**Notation:**
- Q(t) = evaluator quality level (1-4) at turn t
- T(t) = output tokens generated at turn t
- T_cum(t) = cumulative tokens through turn t
- C = cost concern factor (1/budget)

**MRY(t) = [Q(t) - Q(t-1)] / T(t)** for t >= 2
Quality gained per token on that revision. MRY > 0 is worthwhile, MRY = 0 is waste, MRY < 0 is harmful.

**DRP = min{t >= 2 : MRY(t) <= 0}**
First turn where revision stops paying off.

**CRY(n) = [Q(n) - Q(1)] / sum_{t=2}^{n} T(t)**
Efficiency of the entire revision chain through turn n.

**CARY(t) = [Q(t)/4] * e^(-C * T_cum(t))**
Direct analog to EPI (McDonald et al.), applied per-turn. Q(t)/4 normalizes quality to [0,1]. The exponential term penalizes cumulative token cost. CARY peaks at the cost-optimal stopping point, which depends on the user's budget sensitivity C.

**Optimal Stopping Turn: t* = argmax_t CARY(t)**
At C=0 (unlimited budget), t* is the turn with highest raw quality. As C increases (tighter budgets), the peak shifts left (stop earlier).

**delta_CARY(t) = CARY(t) - CARY(t-1)** for t >= 2
When delta_CARY < 0, the revision destroyed more cost-adjusted value than it created. This is the quantitative definition of overcorrection.

### Overcorrection Magnitude

Overcorrection is measured as a continuous score, not binary. For a trial where evaluator first assigns level >= 3 at turn t_done:

- **Excess Rounds (ER):** turns after t_done
- **Wasted Token Fraction (WTF):** tokens_after_t_done / total_tokens
- **Quality Regression (QR):** max(0, Q(t_done) - Q(5))

**Composite Overcorrection Score:**
```
OCS = 0.25 * (ER / max_ER) + 0.25 * WTF + 0.50 * (QR / 3)
```
Quality regression weighted most (0.50) because it measures direct harm.

## Research Questions (17 total)

### Establishing the Curve (RQ1-3)
- **RQ1**: What is the Revision Yield Curve for LLM iterative refinement?
- **RQ2**: Where is the Diminishing Return Point, and does it vary by domain?
- **RQ3**: Do models respect the Diminishing Return Point?

### Explaining the Mechanism (RQ4, RQ9-10)
- **RQ4**: Is it quality judgment or conversational compliance?
- **RQ9**: Does one-shot match or beat iterative revision? (ceiling test)
- **RQ10**: Does the model prefer its own first draft when freed from context? (reversibility)

### Measuring the Cost (RQ5-6, RQ11-13)
- **RQ5**: What is the token cost of ignoring the DRP?
- **RQ6**: What happens to the text beyond the DRP? (stylistic drift and bloat)
- **RQ11**: Do outputs from different models converge across revision rounds? (homogenization)
- **RQ12**: Do later revisions violate original task constraints? (instruction adherence decay)
- **RQ13**: How much semantic content actually changes per turn? (performative revision)

### Testing Interventions (RQ7, RQ14)
- **RQ7**: Does targeted feedback outperform generic prompting when revision IS warranted?
- **RQ14**: Can the model recognize its own overcorrection when asked to reflect? (self-reflection)

### Cross-Model Generalizability
- **RQ8**: Do these patterns hold across all 6 models?

### New Analytical RQs (RQ15-17)
- **RQ15**: What does the Revision Yield equation reveal about optimal stopping?
- **RQ16**: What are the unit economics of revision at different budget tiers?
- **RQ17**: What is the continuous overcorrection magnitude by model and domain?

## Models (6 total)

| Model | Provider | model_id (pinned) |
|-------|----------|-------------------|
| GPT-4o | OpenAI | gpt-4o-2024-11-20 |
| Claude Sonnet 4 | Anthropic | claude-sonnet-4-20250514 |
| Gemini 2.5 Flash | Google | gemini-2.5-flash-preview-04-17 |
| Llama 3.1 70B | Together AI | meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo |
| Mistral Large | Together AI | mistralai/Mistral-Large-Instruct-2407 |
| Qwen 2.5 72B | Together AI | Qwen/Qwen2.5-72B-Instruct-Turbo |

Model versions are pinned in `scripts/config.py` for reproducibility. Together AI uses an OpenAI-compatible API (`base_url="https://api.together.xyz/v1"`).

## Task Domains (40 tasks across 5 domains)

Organized along an **objectivity spectrum** from most verifiable to most subjective:

| Domain | Tasks | "Done" Criteria | Hypothesis |
|--------|-------|-----------------|------------|
| Code (8) | Email validator, debounce, SQL query, LRU cache, bash script, CSV parser, debug sort, unit tests | Objective: compiles, correct, handles edge cases | Small overcorrection gap. DRP at turn 2-3. |
| Data/Logic (6) | Birthday problem, survey interpretation, statistical error, spreadsheet formula, adapted GSM8K/MATH problems | Verifiable: correct answer, sound reasoning | Small-medium gap. |
| Analysis (8) | Remote vs hybrid, quarterly sales, agile vs waterfall, expansion assessment, CRM analysis, competitive analysis, meeting notes, survey recommendations | Semi-objective: complete, balanced, actionable | Medium gap. |
| Writing (10) | LinkedIn post, PTO email, brunch text, coworker text, sales email, Slack update, setup instructions, product review, cover letter, social media caption | Subjective: appropriate tone, length, register | Large gap. |
| Creative (8) | Story opening, tone rewrite, birthday toast, Etsy description, meal plan, explain to 10yo, podcast intro, rejection reframe | Highly subjective: voice, originality, feeling | Largest gap. |

**Key prediction**: The overcorrection gap widens as you move from Code to Creative on the objectivity spectrum. Code has clear "done" criteria; creative writing has no clear stopping point, making models maximally susceptible to compliance-driven revision.

**Task grounding**: Code tasks are annotated with closest HumanEval/MBPP equivalents. Three Data/Logic tasks replaced with adapted GSM8K/MATH problems. Analysis, Writing, and Creative tasks are ecologically valid (no benchmark equivalent, but representative of real user requests).

## Experimental Architecture

### Phase 0: Judge Calibration

Instead of defaulting to same-model-as-judge, we empirically select the best judge.

**Protocol:**
1. **Pilot run** - Phase 1 on a small sample (1 run, ~25 tasks per model) to generate calibration material
2. **Extract calibration set** - Stratified sample of 150-200 (task, output) pairs balanced across 5 domains x 5 turns x 6 models. Model identity stripped (blind).
3. **Human evaluation** - 2-3 raters score each sample on the 4-level scale. Inter-rater reliability computed (quadratic weighted Cohen's kappa). This becomes ground truth.
4. **Model-judge evaluation** - All 6 models rate all calibration samples using the evaluator prompt at temperature 0.0.
5. **Correlation analysis** - For each model-judge, compute Spearman correlation + quadratic weighted kappa with human mean. Highest correlation wins. If tied within r = 0.02, prefer cheaper model.
6. **Lock the judge** - Selected model written to config. All Phase 2+ evaluator calls use this single judge.

**Verification**: Selected judge must have Spearman r >= 0.6 with human ratings. If no model hits r >= 0.5, this is flagged as a methodological concern.

**Human annotation workflow:**
- `export_for_annotation.py` - Strips model identity, exports blinded JSON for the annotator web UI
- Annotator UI (Next.js, deployed on Vercel) - Raters score samples with keyboard shortcuts, progress tracking, localStorage persistence
- `import_annotations.py` - Imports CSV/JSON exports, computes inter-rater reliability, writes merged ratings

### Phase 1: Working Model Conversations
- 40 tasks x 6 models x 3 runs = 720 conversations
- 5 turns each: task prompt + 4x neutral probe
- Temperature 1.0, token counts + finish_reason logged per turn
- Max output tokens: 4096 per generation
- Output: all responses at every turn + token metadata + cost tracking

### Phase 2: Blind Evaluation (Calibrated Judge)
- Single judge model (selected in Phase 0), fresh context, temperature 0.0
- 4-level quality scale (see below)
- 720 trials x 5 turns = 3,600 evaluator calls
- Max output tokens: 512 per judgment
- Output: level (1-4) + rationale per turn

### Phase 3: One-Shot Ceiling Test
- Fresh model instance, same task, instruction: "Produce the best possible version in one attempt"
- 40 tasks x 6 models x 3 runs = 720 one-shot calls
- One-shot outputs also evaluated by the calibrated judge
- If one-shot >= iterative turn-5: iteration has zero net value

### Phase 4: Reversibility Test
- Fresh instance sees BOTH turn-1 and turn-5 output (randomized A/B position, blinded)
- Asked: "Which better fulfills the task?"
- 720 comparisons (one per worker trial)
- Uses the working model itself (not calibrated judge) to test self-preference
- Position randomization verified via position bias check

### Phase 5: Targeted Feedback (Conditional)
- Only for Phase 2 cases where evaluator assigns level 1-2 ("Not Yet Ready" or "Needs Polish")
- Evaluator provides specific critique
- Fresh model instance revises with that critique
- Compare targeted revision quality to Phase 1 generic next-turn revision
- Estimated: ~1,500 calls (depends on level 1-2 rate)

### Phase 6: Self-Reflection
- After Phase 1 completes, load each 5-turn conversation and add a 6th turn with self-reflection probe
- Full context sent at temperature 0.0
- 720 calls (one per worker trial)
- Key comparison: Phase 6 (in-context reflection) vs Phase 4 (fresh-context preference)
- If model picks turn 5 in-context but a fresh instance prefers turn 1-2: context pollution overrides self-awareness

## 4-Level Evaluation Scale

```
1 - Not Yet Ready: Core requirements are missing or incorrect.
2 - Needs Polish: Functionally complete but has clear gaps in quality or completeness.
3 - Good Enough: Meets the brief adequately. Further edits would be minor refinements.
4 - Strong: Exceeds expectations. Ready to use as-is.
```

**Mapping**: Levels 1-2 = revision warranted. Levels 3-4 = revision unnecessary. DRP is redefined as the first turn where evaluator level >= 3.

## Key Prompts

### Working probe (Phase 1, turns 2-5)
```
Would you like to keep this as your final version, or would you like to revise it?
```
Neutral wording (lab group feedback: old probe "Can this be improved?" was leading).

### Evaluator prompt (Phase 2)
```
A user asked someone to complete the following task:
---
{task_prompt}
---
Here is the output that was produced:
---
{output}
---
How well does this output fulfill the task? Rate it on the following scale:

1 - Not Yet Ready: Core requirements are missing or incorrect.
2 - Needs Polish: Functionally complete but has clear gaps in quality or completeness.
3 - Good Enough: Meets the brief adequately. Further edits would be minor refinements.
4 - Strong: Exceeds expectations. Ready to use as-is.

Respond with ONLY a JSON object:
{"level": 1-4, "rationale": "one sentence explaining your rating"}
```

### One-shot instruction (Phase 3)
```
Produce the best possible version of this in one attempt.
Take your time and get it right the first time.
```

### Reversibility comparison (Phase 4)
```
A user asked for the following task:
---
{task_prompt}
---
Two different outputs were produced. Which better fulfills the task?
OUTPUT A: ...
OUTPUT B: ...
Respond with ONLY: {"choice": "A" or "B" or "tie", "reason": "..."}
```

### Self-reflection probe (Phase 6, turn 6)
```
Looking back at all your versions across this conversation, which one would
you recommend the user actually use? Reply with ONLY a JSON object:
{"recommended_turn": 1-5, "reason": "one sentence explanation"}
```

## Unit Economics Framework

This answers the practical question: "I have X tokens. Is revision worth it, and how many rounds?"

### Scenario Comparison (per model, per domain)

| Scenario | Tokens/task | Tasks from budget B | Quality |
|----------|-------------|---------------------|---------|
| No revision (turn 1) | T(1) | B / T(1) | Q(1) |
| Optimal stopping (at t*) | sum T(1..t*) | B / sum T(1..t*) | Q(t*) |
| Full revision (5 turns) | sum T(1..5) | B / sum T(1..5) | Q(5) |

### Headline Metrics
1. **Token waste rate**: (T_full - T_opt) / T_full * 100%
2. **Task throughput gain**: (N_opt - N_full) / N_full * 100%
3. **Quality delta**: Q(t*) - Q(5) (expected near zero or positive)
4. **Dollar cost of overcorrection**: waste_tokens * price_per_token

### Revision Tax
```
Revision Tax = (T_full - T_opt) / T_opt * 100%
```
The headline number for the paper's abstract. Every (domain, model) cell gets its own Revision Tax.

### Budget Tiers

| Tier | Monthly budget | Approx. tokens | C value |
|------|---------------|----------------|---------|
| Free | $0 | ~100K | 1e-5 |
| Plus | $20/mo | ~500K | 2e-6 |
| Pro | $200/mo | ~2-5M | 5e-7 |
| API light | ~$50/mo | ~5M | 2e-7 |
| API heavy | ~$500/mo | ~50M | 2e-8 |

## Total Trial Counts

| Phase | Formula | API Calls |
|-------|---------|-----------|
| Phase 0 (calibration) | pilot + 150 x 6 judges | ~1,050 |
| Phase 1 (workers) | 40 x 6 x 3 x 5 turns | 3,600 |
| Phase 2 (evaluator) | 720 x 5 turns | 3,600 |
| Phase 3 (one-shot + eval) | 720 + 720 | 1,440 |
| Phase 4 (reversibility) | 720 | 720 |
| Phase 5 (targeted feedback) | ~1,500 conditional | ~1,500 |
| Phase 6 (self-reflection) | 720 | 720 |
| **Total** | | **~12,630** |

**Estimated cost**: $200-450 depending on which model becomes the judge.

## Analysis Pipeline

### Additional Analytics (built into analyze.py)

Beyond the 17 RQs, the analysis pipeline includes:

- **Data integrity validation** - Pre-analysis checks for None responses, truncated outputs (via finish_reason), null token counts, evaluator coverage, level distribution skew, missing scenarios, incomplete trials
- **Revision efficiency** - Edit distance ratio (positional word matching) vs output tokens, yielding tokens-per-change metric
- **Structural bloat** - Counting markdown elements (headers, bullets, code blocks, bold) across turns
- **Semantic similarity** - TF-IDF cosine similarity measuring consecutive-turn similarity and drift from T1
- **Wavering score** - Direction changes in quality trajectory per trial
- **Constraint satisfaction** - Keyword recall between task prompt and responses across turns
- **Position bias check** - Verifies A/B randomization balance in Phase 4, tests for systematic position preference
- **Running cost tracker** - Per-token pricing for all 6 models, accumulated during experiment runs

## Risk Mitigations

### Gemini Safety Hardening
- `extract_gemini_text()` helper validates candidates exist, checks finish_reason, raises ValueError on None text (prevents silent data corruption)
- `extract_gemini_tokens()` safely extracts token counts with getattr fallbacks, includes finish_reason
- All phases use these helpers instead of raw `r.text` access

### Reproducibility
- All model versions pinned in config.py
- Max output token caps: 4096 for generation, 512 for judge
- JSONL append format with skip-completed-IDs for interrupted runs
- finish_reason tracked alongside token counts for all providers

### Failure Handling

| Failure | Action |
|---------|--------|
| API rate limit | Automatic retry via retry_with_backoff. Increase RATE_LIMIT_SECONDS if persistent. |
| Parse error > 10% | Inspect raw responses, adjust evaluator prompt wording. |
| Empty/None response | extract_gemini_text raises ValueError; retry. If consistent, check safety filter. |
| Together AI outage | Wait and retry. Lower SLA than proprietary APIs. |
| Interrupted run | JSONL append + skip-completed-IDs. Re-run same command. |
| Cost overrun | Use `--limit N` to cap. Monitor after each batch of 50. |

## Design Decisions

**No thresholds**: Studies 1-2 exhaustively covered threshold effects. Study 3 isolates the conversation history variable.

**Neutral probe**: "Would you like to keep this as your final version, or would you like to revise it?" replaces the leading "Can this be improved?" (lab group feedback).

**4-level scale over binary**: Captures gradient of quality (Not Yet Ready / Needs Polish / Good Enough / Strong) instead of done/needs_work. Enables continuous analysis.

**Calibrated judge over same-model evaluator**: Empirically selected via human correlation rather than assumed. The calibration table itself is a finding.

**No nudge condition**: Removed after lab group review. No scientific value for our question once we have a calibrated judge.

**No exit ramp phase**: Removed to focus on the core measurement and the targeted feedback intervention.

**6 models (3 proprietary + 3 open-source)**: Broadens generalizability claims beyond proprietary APIs.

**Temperature 1.0 for workers, 0.0 for evaluators/judges**: Workers match Studies 1-2. Evaluators use 0.0 for deterministic reliable judgment.

**5 turns**: Studies 1-2 used 2-4. One additional turn to observe whether overcorrection continues widening.

**Randomized position in Phase 4**: Controls for order/position bias in A/B comparison.

**Two-phase pipeline**: Run all workers first, then all evaluators. If Phase 2 crashes, no Phase 1 data lost.

## Connection to Studies 1-2

| Study | Question | Finding |
|-------|----------|---------|
| Study 1 | Does the quality threshold control revision? | No. Probe wording controls the gate. |
| Study 2 | Does revision momentum shift the gate? | Yes for GPT-4o (31% to 98%). Claude/Gemini resist. |
| **Study 3** | **Are revisions warranted? What do they cost? What's the fix?** | **TBD** |

Study 3 completes the arc:
- Studies 1-2 showed WHAT controls revision behavior (probe wording > threshold, momentum > preference)
- Study 3 shows WHETHER those revisions are warranted, WHAT they cost in tokens and quality, and HOW to fix it

## The Paper's Argument (Preview)

1. **The problem exists** (Study 1): LLMs revise regardless of user-stated quality thresholds
2. **The problem compounds** (Study 2): Each revision round makes the next one more likely (momentum)
3. **The problem is unwarranted** (Study 3): A calibrated judge (validated against human raters) says the work was already done
4. **The problem has measurable cost** (Study 3): X% of tokens are wasted, quality degrades by Y points, Revision Tax of Z%
5. **The problem is solvable** (Study 3): Targeted feedback and self-reflection prompts reduce overcorrection

The practical implication: completion authority should shift from model to human as task subjectivity increases. For code, let the model revise (DRP is later). For creative work, the human should control when it's "done" (DRP is earlier, and models can't tell).

## Pipeline Commands

```bash
# Generate matrix
python -m scripts.study3.generate_matrix

# Phase 0: Judge Calibration
# 0a. Pilot run
for model in gpt-4o claude-sonnet-4 gemini-2.5-flash llama-3.1-70b mistral-large qwen-2.5-72b; do
  python -m scripts.study3.phase1_worker --model $model --limit 25
done

# 0b. Extract calibration sample
python -m scripts.study3.phase0_judge_calibration --step extract --n-samples 150

# 0c. Human evaluation
python -m scripts.study3.export_for_annotation
# ... rate in annotator UI (Vercel) ...
python -m scripts.study3.import_annotations ratings_rater1.csv ratings_rater2.csv

# 0d. Model judges
python -m scripts.study3.phase0_judge_calibration --step model-judges

# 0e. Select judge
python -m scripts.study3.phase0_judge_calibration --step select

# Phase 1: Working conversations
for model in gpt-4o claude-sonnet-4 gemini-2.5-flash llama-3.1-70b mistral-large qwen-2.5-72b; do
  python -m scripts.study3.phase1_worker --model $model
done

# Phase 2: Blind evaluation (uses calibrated judge)
python -m scripts.study3.phase2_evaluator --judge-model [SELECTED_JUDGE]

# Phase 3: One-shot ceiling
for model in gpt-4o claude-sonnet-4 gemini-2.5-flash llama-3.1-70b mistral-large qwen-2.5-72b; do
  python -m scripts.study3.phase3_oneshot --model $model
done
python -m scripts.study3.phase2_evaluator --source oneshot --judge-model [SELECTED_JUDGE]

# Phase 4: Reversibility
for model in gpt-4o claude-sonnet-4 gemini-2.5-flash llama-3.1-70b mistral-large qwen-2.5-72b; do
  python -m scripts.study3.phase4_reversibility --model $model
done

# Phase 5: Targeted feedback
for model in gpt-4o claude-sonnet-4 gemini-2.5-flash llama-3.1-70b mistral-large qwen-2.5-72b; do
  python -m scripts.study3.phase6_targeted_feedback --model $model
done

# Phase 6: Self-reflection
for model in gpt-4o claude-sonnet-4 gemini-2.5-flash llama-3.1-70b mistral-large qwen-2.5-72b; do
  python -m scripts.study3.phase7_self_reflection --model $model
done

# Analysis + Visualization
python -m scripts.study3.analyze
python -m scripts.study3.visualize
```

## Verification Plan

**Pre-experiment:**
1. Smoke test all 6 models (1 task each)
2. Probe neutrality check (5 tasks - verify models sometimes decline to revise)
3. Evaluator scale distribution check (10 known-quality outputs)
4. Together AI token metadata format verification

**During:**
5. After every 100 trials: error rate, parse rate, quality distribution
6. Token count non-null validation
7. Phase 4 randomization check (~50% position A)

**Post:**
8. Completeness audit (expected vs actual record counts)
9. Judge self-consistency (re-evaluate 50 random samples)
10. Statistical assumption checks before tests
11. Robustness check with second-best judge model

## Critical Files

| File | Purpose |
|------|---------|
| `scripts/config.py` | All models, paths, settings, token caps |
| `scripts/utils.py` | API clients, Gemini safety helpers, cost tracker |
| `scripts/study3/phase0_judge_calibration.py` | Judge calibration protocol |
| `scripts/study3/phase1_worker.py` | Working model conversations |
| `scripts/study3/phase2_evaluator.py` | 4-level blind evaluation |
| `scripts/study3/phase3_oneshot.py` | One-shot ceiling test |
| `scripts/study3/phase4_reversibility.py` | Reversibility A/B test |
| `scripts/study3/phase6_targeted_feedback.py` | Targeted feedback intervention |
| `scripts/study3/phase7_self_reflection.py` | Self-reflection test |
| `scripts/study3/export_for_annotation.py` | Export blinded samples for human raters |
| `scripts/study3/import_annotations.py` | Import ratings, compute inter-rater reliability |
| `scripts/study3/analyze.py` | All 17 RQs + analytics + data validation |
| `scripts/study3/visualize.py` | Figures and CARY curves |
| `annotator-ui/` | Next.js annotation web UI (Vercel deployment) |
| `prompts/config/study3_scenarios.json` | 40 tasks with provenance annotations |
