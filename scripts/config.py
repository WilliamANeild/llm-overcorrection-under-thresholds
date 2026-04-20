"""Central configuration for the experiment pipeline."""

from pathlib import Path

# ── Project root ──
ROOT = Path(__file__).resolve().parent.parent

# ── Data paths ──
PROMPT_MATRIX_PATH = ROOT / "data" / "generated_prompts" / "prompt_matrix.json"
TRIALS_PATH = ROOT / "data" / "raw_responses" / "trials.jsonl"
METADATA_PATH = ROOT / "data" / "raw_responses" / "experiment_metadata.jsonl"
SCORED_TRIALS_JSONL = ROOT / "data" / "processed" / "scored_trials.jsonl"
SCORED_TRIALS_CSV = ROOT / "data" / "processed" / "scored_trials.csv"
STATS_DIR = ROOT / "data" / "analysis"

# Summary CSVs
SUMMARY_BY_CONDITION_CSV = ROOT / "data" / "processed" / "summary_by_condition.csv"
SUMMARY_BY_MODEL_CSV = ROOT / "data" / "processed" / "summary_by_model.csv"
SUMMARY_BY_MODEL_CONDITION_CSV = ROOT / "data" / "processed" / "summary_by_model_condition.csv"
SUMMARY_BY_SCENARIO_CSV = ROOT / "data" / "processed" / "summary_by_scenario.csv"

# ── Momentum experiment paths ──
MOMENTUM_MATRIX_PATH = ROOT / "data" / "generated_prompts" / "momentum_matrix.json"
MOMENTUM_TRIALS_PATH = ROOT / "data" / "raw_responses" / "momentum_trials.jsonl"
MOMENTUM_SCORED_PATH = ROOT / "data" / "processed" / "momentum_scored.jsonl"
MOMENTUM_SCORED_CSV = ROOT / "data" / "processed" / "momentum_scored.csv"
MOMENTUM_STATS_DIR = ROOT / "data" / "analysis" / "momentum"
MOMENTUM_FIGURES_DIR = ROOT / "data" / "figures" / "momentum"

# ── Momentum settings ──
MOMENTUM_DOSES = [1, 2, 3]
MOMENTUM_THRESHOLDS = [0, 75, 90, 100]
LEADING_PROBE = "Can this be improved?"
EVALUATIVE_PROBE = "Take another look at this and let me know if it's ready."

# ── Reverse momentum experiment paths ──
REVERSE_MOMENTUM_MATRIX_PATH = ROOT / "data" / "generated_prompts" / "reverse_momentum_matrix.json"
REVERSE_MOMENTUM_TRIALS_PATH = ROOT / "data" / "raw_responses" / "reverse_momentum_trials.jsonl"
REVERSE_MOMENTUM_SCORED_PATH = ROOT / "data" / "processed" / "reverse_momentum_scored.jsonl"
REVERSE_MOMENTUM_SCORED_CSV = ROOT / "data" / "processed" / "reverse_momentum_scored.csv"

# ── Reverse momentum settings ──
AFFIRMING_PROBE = "This looks great, no changes needed."

# ── Prompt config paths ──
SCENARIOS_PATH = ROOT / "prompts" / "config" / "scenarios.json"
THRESHOLDS_PATH = ROOT / "prompts" / "config" / "thresholds.json"

# ── Models ──
MODELS = {
    "gpt-4o": {
        "provider": "openai",
        "model_id": "gpt-4o",
    },
    "claude-sonnet-4": {
        "provider": "anthropic",
        "model_id": "claude-sonnet-4-20250514",
    },
    "gemini-2.5-flash": {
        "provider": "google",
        "model_id": "gemini-2.5-flash",
    },
}

RUNS_PER_CELL = 3

# ── API settings ──
MAX_RETRIES = 8
RETRY_BACKOFF_BASE = 2

RATE_LIMIT_SECONDS = {
    "openai": 0.5,
    "anthropic": 0.5,
    "google": 4.0,
}

# ── Judge settings ──
JUDGE_MODEL = "gpt-4o"
JUDGE_PROVIDER = "openai"
SECOND_JUDGE_MODEL = "claude-sonnet-4-20250514"
SECOND_JUDGE_PROVIDER = "anthropic"
