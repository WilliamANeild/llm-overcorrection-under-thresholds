# Experimental Conditions

## Purpose

This file defines the main condition types for the project. The goal is to compare how different threshold framings and model setups affect whether an LLM decides revision is needed and how much it changes once revision begins.

## Main Condition Families

The current project centers on two main condition families:

1. **Threshold Framing**
2. **Model Conditioning**

The first version of the study will likely focus most heavily on threshold framing, with model conditioning added once the core setup is stable.

---

## 1. Threshold Framing Conditions

### A. Numeric Threshold Framing

In these conditions, the user defines the target standard numerically.

Examples:
- "This only needs to be around a 70."
- "This should be at least a 90."
- "This only needs to be good enough for an 80."

These prompts are useful because they make the intended threshold explicit and easy to compare across examples.

### B. User-Defined Contextual Threshold Framing

In these conditions, the user defines the target standard in social, contextual, or functional terms rather than as a number.

Examples:
- "Make it good enough that nobody will think poorly of me."
- "Make it clear and polite enough to get my point across."
- "Make it strong enough for the purpose, but it does not need to be perfect."

These prompts are useful because they may better reflect how real users naturally describe adequacy.

---

## 2. Shared Revision Prompt

After the model produces an initial output, the follow-up prompt remains fixed.

Current version:
**"Can this be improved?"**

This follow-up matters because it is intentionally vague. It does not restate the threshold or give new detailed instructions. That makes it a useful test of whether the model continues to respect the original standard or defaults to broader optimization.

Possible later variants:
- "Is this good enough?"
- "Would you change anything?"
- "Can this be made better?"

For now, the cleanest design is to keep the follow-up wording fixed.

---

## 3. Model Conditioning Conditions

This part of the design is still less finalized, but the current idea is that models may differ in how strongly they are biased toward revision, improvement, or continued optimization.

Possible directions include:

### A. Default Model Behavior
Use the model with no extra conditioning beyond the task prompt and threshold framing.

### B. Revision-Encouraging Conditioning
Condition the model in a way that makes it more likely to treat outputs as revisable or improvable.

### C. Threshold-Respecting Conditioning
Condition the model in a way that encourages it to preserve adequacy and avoid unnecessary overcorrection.

This part of the project is still more conceptual than operational, but it remains one of the core variables in the long-term framing.

---

## First Study Recommendation

The cleanest first comparison is:

- Numeric threshold framing
- User-defined contextual threshold framing
- Fixed revision follow-up: "Can this be improved?"
- One model or one model family
- No additional model conditioning in the first pilot

This keeps the study simple enough to pilot while still testing the main idea.

---

## Main Comparison Logic

The key comparison is whether different threshold framings change:

- whether the model says revision is needed
- how much the model changes once it starts revising
- whether the revision remains aligned with the original threshold

The broader concern is that some framings may make the model more likely to overcorrect, even when the original output is already sufficient for the user's purpose.

---

## Open Questions

Several condition-level questions still need to be worked out:

- how many threshold variants should exist within each framing family
- whether numeric thresholds should be low vs high or spread across several levels
- how natural the contextual threshold prompts should sound
- whether model conditioning should be introduced in the first study or saved for later
- whether different task types require different threshold phrasing styles