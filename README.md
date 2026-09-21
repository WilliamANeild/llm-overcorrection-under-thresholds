# STET

**A diagnostic for whether a language model leaves already-sufficient work alone.**

Code and data for *Worse on Request, Better on Critique: Self-Correction on Work That Is
Already Sufficient*.

STET is the editor's mark for "let it stand". The question it measures is what a model does
when its output is already good enough and the user asks for an improvement without saying
what to improve.

---

## What the study does

A model is given a fully specified task and produces a draft. It is then asked, four more
times, the same neutral question:

> Would you like to keep this as your final version, or would you like to revise it?

The probe offers an explicit way out at every turn and names nothing to fix. Six models, 40
tasks, 3 runs each: **720 five-turn conversations and 3,600 model-turn outputs**. Every output
is scored on a six-level quality scale by a blind evaluator, validated against three human
raters.

The design isolates a case the literature mostly skips. Self-correction research asks whether
a model can repair work that is wrong. This asks what it does to work that is right.

## What it finds

- **88% of first drafts are already sufficient** (631 of 720), so most of what follows is
  revision that was not needed.
- **Models mostly do not revise.** Only 24.9% of post-first-turn outputs contain genuine new
  content (718 of 2,880); by the fifth turn it is 13.3%. The rest are declines, restatements
  and commentary presented as compliance.
- **When they do revise, it usually gets worse.** Of revisions that move the quality level at
  all, 69.6% move it down. On the 50 conversations that revise at every turn, quality falls
  0.74 levels from first draft to fifth (p = 1.01 × 10⁻⁴).
- **Naming the fault reverses it.** On work rated below sufficient, one targeted critique
  produces revisions 1.16 levels better than undirected iteration (n = 177, p = 5.7 × 10⁻¹⁹).
- **62.1% of all output tokens are generated past the point of peak quality.**

The STET score itself is the share of already-sufficient output a model leaves alone:

| Model | Leaves sufficient work alone |
|---|---:|
| Gemini 2.5 Flash | 97.8% |
| DeepSeek V4 Flash | 96.3% |
| GPT-4o | 82.3% |
| Qwen 3 235B | 68.4% |
| Claude Sonnet 4 | 54.1% |
| Llama 3.3 70B | 18.4% |

Across 1,000 random splits of the 40 tasks the model ranking holds at mean Spearman ρ = 0.972,
and a generalizability decomposition gives G = 0.992, so 40 tasks is more than the measurement
needs. The quality decline is reported as a finding rather than as a score, because it does
**not** rank models stably: it would need roughly 215 tasks to do so.

## The tasks

`data/study3/generated_prompts/study3_matrix.json` holds all 40, eight in each of five
domains: code, data logic, analysis, writing, creative. Each record carries a `scenario_id`,
the `task_prompt` given at turn 1, and the probe repeated at turns 2 through 5.

The tasks are fully specified on purpose. A task with missing requirements would confound
"the model degraded good work" with "the model guessed at what was missing".

## Layout

| Path | Contents |
|---|---|
| `data/study3/` | The main study: trials, evaluator scores, stripped rescores, human ratings |
| `data/figures/` | Generated figures (the paper symlinks to these) |
| `scripts/study3/` | The study, `phase0` through `phase7`, in run order |
| `scripts/` | Shared config, analysis and figure generation |
| `paper/` | LaTeX source, figures, and the build and verification tools |
| `results_FINAL.md` | The analysis ledger. **Every number carries the filter it was computed under** |
| `PIPELINE.md`, `MOMENTUM_SUMMARY.md` | Records for Studies 1 and 2, reported in the appendix |
| `experiment/`, `docs/` | Design documents and research questions, written before the runs |
| `evaluation/rubric.md` | The six-level quality scale |
| `annotator-ui/`, `reversibility-annotator/` | The interfaces used for human rating |
| `prompts/` | Prompt bank and configuration |

`results_FINAL.md` is the file to read if you want to check a number in the paper. It is
organised by result, and each entry states its sample definition, joins, recodes and test
before giving the value.

## Reproducing

The analysis runs from the committed data and needs no API keys:

```bash
pip install -r requirements.txt
python3 scripts/study3/stet_stability.py      # split-half and generalizability
python3 scripts/study3/audit_hand_corrections.py
python3 scripts/visualize.py                  # regenerates data/figures/
cd paper && python3 build_check.py            # compiles the paper, needs tectonic
```

Several scripts assert their expected inputs at load and fail loudly rather than producing a
different result under the same name.

Regenerating the **trials** is a different matter: it costs real API calls across five
providers, and the models behind these names change. Copy `.env.example` to `.env` and supply
keys, then run `scripts/study3/phase1_worker.py` onward. The exact endpoints used were:

| Paper name | Identifier |
|---|---|
| GPT-4o | `gpt-4o-2024-11-20` |
| Claude Sonnet 4 | `claude-sonnet-4-20250514` |
| Gemini 2.5 Flash | `gemini-2.5-flash` |
| Llama 3.3 70B | `meta-llama/Llama-3.3-70B-Instruct-Turbo` (Together) |
| Qwen 3 235B | `Qwen/Qwen3-235B-A22B-Instruct-2507-tput` (Together) |
| DeepSeek V4 Flash | `deepseek-v4-flash` |

Generation ran at temperature 1.0; evaluation at temperature 0.

## One measurement note

Models wrap revisions in boilerplate ("Here's my revised version...", "Let me know if you'd
like any changes"). In a stratified sample, 84% of revision-side outputs carry at least one
such wrapper against 14% of first drafts. That asymmetry lets an automated judge identify the
revision side by its packaging, and it is large enough to reverse the measured direction of
the effect.

Every quality estimate here is therefore computed **after stripping meta-commentary**, with
the unstripped value reported alongside. Any study comparing first-draft and revised outputs
with an LLM judge inherits the same confound.

## Licence

- **Data** (`data/`, including the 40 tasks, conversations, scores and human ratings):
  [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- **Code** (`scripts/`, `paper/*.py`): MIT
- The manuscript in `paper/` is under neither.

See [`LICENSE`](LICENSE).

## Citation

The paper is under review. Until it appears, cite the repository:

```bibtex
@misc{stet2026,
  title  = {Worse on Request, Better on Critique: Self-Correction on Work That Is Already Sufficient},
  author = {Neild, Liam},
  year   = {2026},
  note   = {https://github.com/WilliamANeild/stet}
}
```
