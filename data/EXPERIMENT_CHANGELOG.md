# Experiment Changelog

## v2 (2026-03-30) — Rubric Revision + Probe Type Addition

### Changes from v1

**1. New experimental factor: probe_type (leading vs neutral)**
- v1 used only "Can this be improved?" (a leading question that presupposes revision)
- v2 adds "Please review this output." as a neutral probe condition
- This doubles the design: 3 models x 5 scenarios x 2 framings x 8 thresholds x **2 probes** x 5 runs = 2,400 trials
- Rationale: Adversarial review (#1 FATAL) identified that the leading probe confounds pragmatic compliance with overcorrection. The neutral probe separates these.

**2. Revised judge rubric (threshold_alignment + overcorrection)**
- threshold_alignment: Now explicitly defines "exceeds threshold = misaligned", adds concrete anchoring examples, handles baseline condition
- overcorrection: Now references user's stated threshold, adds behavioral anchors (formality inflation, length expansion, register elevation)
- revision_magnitude and revision_value: Unchanged (kappa > 0.6)
- Rationale: IRR council debate found kappa=0.082 on threshold_alignment and 0.419 on overcorrection — rubric ambiguity was the root cause

**3. Normalized threshold text phrasing**
- v1: Levels 70-95 used "only really needs to be" (low-bar framing); level 100 used "needs to be as close to... as possible" (aspirational framing). This introduced a confound at the top of the scale.
- v2: All levels use uniform "I would consider this done if the outcome is around..." structure
- v1 qualitative: Level 95 said "difficult to improve in any meaningful way" (behavioral cue to not revise); level 100 said "almost no room for improvement"
- v2 qualitative: Removed all behavioral cues. Descriptions vary only in quality level.
- Rationale: Adversarial review #6 and #18

**4. Enhanced IRR pipeline**
- Stratified sampling (balanced across model/threshold/scenario) instead of random 15%
- Added: Gwet's AC1, confusion matrices per dimension, % agreement, % within +/-1, binary kappa
- Decision thresholds from council debate applied automatically

**5. Trial ID format change**
- v1: `{model}__{scenario}__{framing}__{level}__run{N}`
- v2: `{model}__{scenario}__{framing}__{level}__{probe_type}__run{N}`

### v1 Data Preserved
- `data/raw_responses/trials_v1_backup.jsonl` — all 1,200 v1 trials
- `data/processed/scored_trials_v1_backup.jsonl` — all 1,200 v1 scored trials
- `data/generated_prompts/prompt_matrix_v1_backup.json` — v1 prompt matrix
- `data/analysis/irr_council_debate.md` — council debate that motivated changes
- `data/analysis/adversarial_critique.md` — adversarial review that identified probe confound

### Files Modified
- `prompts/config/thresholds.json` — new probe_types, normalized threshold text
- `scripts/config.py` — added PROBE_TYPES
- `scripts/utils.py` — make_trial_id includes probe_type
- `scripts/generate_prompt_matrix.py` — iterates over probe types
- `scripts/run_experiment.py` — includes probe_type in trials, --probe-type filter
- `scripts/evaluate.py` — revised rubric, probe_type in records, enhanced IRR
- `scripts/analyze.py` — probe type analyses (leading vs neutral comparisons)
- `scripts/deep_analysis.py` — Analysis 6: Probe Type Effects
- `scripts/visualize.py` — fig10 (probe comparison), fig11 (probe x threshold interaction)
