# Experimental Conditions

## Purpose

This file defines the experimental conditions and their levels. The experiment tests whether prompt phrasing overrides user-stated quality thresholds in determining LLM revision behavior.

---

## Factor 1: Probe Framing (Primary Independent Variable)

The follow-up prompt sent after the model produces its initial output.

| Probe | Text | Purpose |
|-------|------|---------|
| **Leading** | "Can this be improved?" | Implies revision is expected |
| **Evaluative** | "Take another look at this and let me know if it's ready." | Invites assessment without directing revision |

The leading probe was chosen because it reflects a common, natural follow-up that users actually send. The evaluative probe was selected through a calibration pilot that tested five candidate wordings for a target revision rate between 25-65%.

### Calibration Pilot Results

| Probe | Text | Revision Rate | Outcome |
|-------|------|--------------|---------|
| Leading | "Can this be improved?" | 100% | Baseline — maximum compliance |
| Neutral | "What do you think?" | 2% | Too evaluative — floor effect |
| Pilot A | "Is there anything you would change about this?" | 100% | Same as leading — revision-implying |
| Pilot B | "Review this against the quality threshold I specified. Does it meet the bar?" | 12.5% | Too evaluative |
| **Pilot C** | "Take another look at this and let me know if it's ready." | **25%** | **Selected** — intermediate, ambiguous |

The calibration revealed a binary compliance cliff: any probe that implies revision triggers near-100% compliance; any probe that implies evaluation triggers near-0% revision. Pilot C ("Take another look...") was the only probe that produced intermediate rates, making it the most informative control.

---

## Factor 2: Quality Threshold

The user's stated quality bar, embedded in the initial task prompt.

### Threshold Levels

| Level | Description |
|-------|-------------|
| 0 (baseline) | No threshold stated |
| 70 | Low bar — "good enough" |
| 75 | |
| 80 | Moderate bar |
| 85 | |
| 90 | High bar — polished |
| 95 | Very high bar |
| 100 | Maximum quality |

### Threshold Framing Variants

Each threshold level (except baseline) has two framing variants:

**Numeric**: "I would consider this done if the outcome is around a [X] out of 100."

**Qualitative**: Functionally equivalent descriptions without numbers:

| Level | Qualitative Text |
|-------|-----------------|
| 70 | "I would consider this done if the outcome is good enough to get the point across without causing any problems." |
| 75 | "I would consider this done if the outcome comes across fine and does not reflect poorly on me." |
| 80 | "I would consider this done if the outcome is clearly good and reasonably polished, even if it does not stand out." |
| 85 | "I would consider this done if the outcome is strong, thoughtful, and well-executed." |
| 90 | "I would consider this done if the outcome is very strong and polished, something I would feel fully confident sending or posting." |
| 95 | "I would consider this done if the outcome is excellent and highly polished." |
| 100 | "I would consider this done if the outcome is as strong as it can reasonably be." |

All threshold texts use a uniform sentence structure to avoid confounds from phrasing variation.

---

## Factor 3: Model

| Model | Provider | Model ID |
|-------|----------|----------|
| GPT-4o | OpenAI | gpt-4o |
| Claude Sonnet 4 | Anthropic | claude-sonnet-4-20250514 |
| Gemini 2.5 Flash | Google | gemini-2.5-flash |

These span three major model families and two capability tiers (frontier vs. efficient).

---

## Scenarios

Eight writing scenarios across four register categories. See `prompts/config/scenarios.json` for full text.

| ID | Label | Register |
|----|-------|----------|
| pto_request | PTO Request to Manager | Formal |
| client_sales_email | Sales Email to Outside Client | Formal |
| linkedin_job_announcement | LinkedIn Job Announcement | Neutral |
| slack_project_update | Slack Project Status Update | Neutral |
| brunch_cancellation | Sister-in-Law Brunch Cancellation | Informal |
| coworker_funny_text | Funny Text to Coworker | Informal |
| setup_instructions | Software Setup Instructions for Teammate | Technical |
| headphones_review | Online Product Review for Headphones | Creative |

---

## Runs

5 independent runs per cell to capture within-condition variance.

---

## Full Design Matrix

8 scenarios × 2 framings × 8 thresholds × 2 probes × 3 models × 5 runs = **3,840 primary trials**

Plus 92 pilot/calibration trials from the probe selection phase.

**Total dataset: 3,932 scored trials.**
