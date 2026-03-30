"""Central configuration for the experiment pipeline."""

from pathlib import Path

# ── Project root ──
ROOT = Path(__file__).resolve().parent.parent

# ── File paths ──
SCENARIOS_PATH = ROOT / "prompts" / "config" / "scenarios.json"
THRESHOLDS_PATH = ROOT / "prompts" / "config" / "thresholds.json"
PROMPT_MATRIX_PATH = ROOT / "data" / "generated_prompts" / "prompt_matrix.json"
TRIALS_PATH = ROOT / "data" / "raw_responses" / "trials.jsonl"
METADATA_PATH = ROOT / "data" / "raw_responses" / "experiment_metadata.jsonl"
SCORED_TRIALS_JSONL = ROOT / "data" / "processed" / "scored_trials.jsonl"
SCORED_TRIALS_CSV = ROOT / "data" / "processed" / "scored_trials.csv"
SUMMARY_BY_CONDITION_CSV = ROOT / "data" / "processed" / "summary_by_condition.csv"
SUMMARY_BY_MODEL_CSV = ROOT / "data" / "processed" / "summary_by_model.csv"
SUMMARY_BY_MODEL_CONDITION_CSV = ROOT / "data" / "processed" / "summary_by_model_condition.csv"
SUMMARY_BY_SCENARIO_CSV = ROOT / "data" / "processed" / "summary_by_scenario.csv"

# ── Analysis / figures output ──
FIGURES_DIR = ROOT / "data" / "figures"
STATS_DIR = ROOT / "data" / "analysis"

# ── Model configuration ──
MODELS = {
    "gpt-4o": {
        "provider": "openai",
        "model_id": "gpt-4o",
        "env_key": "OPENAI_API_KEY",
    },
    "claude-sonnet": {
        "provider": "anthropic",
        "model_id": "claude-sonnet-4-20250514",
        "env_key": "ANTHROPIC_API_KEY",
    },
    "gemini-flash": {
        "provider": "google",
        "model_id": "gemini-2.5-flash",
        "env_key": "GOOGLE_API_KEY",
    },
}

# Judge model (used for LLM-as-judge evaluation)
JUDGE_MODEL = "gpt-4o"
JUDGE_PROVIDER = "openai"

# Second judge for inter-rater reliability
SECOND_JUDGE_MODEL = "claude-sonnet-4-20250514"
SECOND_JUDGE_PROVIDER = "anthropic"
IRR_SAMPLE_SIZE = 60  # absolute count; stratified across model/threshold/scenario

# ── Rate limiting (seconds between requests per provider) ──
RATE_LIMIT_SECONDS = {
    "openai": 1.0,
    "anthropic": 1.0,
    "google": 1.0,
}

# ── Retry settings ──
MAX_RETRIES = 3
RETRY_BACKOFF_BASE = 2  # seconds: 2, 4, 8

# ── Experiment parameters ──
RUNS_PER_CELL = 5
FRAMINGS = ["numeric", "qualitative"]
PROBE_TYPES = ["leading", "neutral"]
