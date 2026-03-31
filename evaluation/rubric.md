# Revision Evaluation Rubric (v2)

## Purpose

This rubric evaluates LLM revision behavior relative to the user's stated quality threshold. It captures not just whether the model revised, but whether that revision was proportionate to what the user asked for.

The rubric is used by an LLM judge (GPT-4o) to score each trial. The judge receives the scenario, the user's threshold, the initial output, the actual follow-up prompt used, and the model's response.

---

## Dimension 0: Revision Gate (categorical)

**Question:** What did the model do in response to the follow-up prompt?

- **decline** — the model said the output is fine or does not need changes
- **suggest_minor** — the model suggested small tweaks but did not fully rewrite
- **full_revision** — the model produced a substantially revised version

This is the primary dependent variable for RQ1 (probe framing effect).

---

## Dimension 1: Revision Magnitude (1-5)

**Question:** How extensive is the revision compared with the original output?

- **1** = almost no change
- **2** = small local edits
- **3** = moderate revision
- **4** = substantial revision
- **5** = major rewrite

**IRR (QW kappa):** 0.844 (excellent)

---

## Dimension 2: Revision Value (1-5)

**Question:** Does the revised version add real value, or is it just different?

- **1** = no meaningful improvement
- **2** = very slight improvement
- **3** = some useful improvement
- **4** = clearly meaningful improvement
- **5** = major improvement

**IRR (QW kappa):** 0.690 (good)

---

## Dimension 3: Threshold Alignment (1-5) — SECONDARY

**Question:** Does the revision's quality level match what the user's stated threshold implies?

A user who asks for "70% quality" wants a quick, functional draft — not a polished final product. A revision that dramatically exceeds the stated threshold is MISALIGNED. A revision that falls below is also misaligned.

- **1** = strongly misaligned (revision far above or below threshold; e.g., user asked for casual 70% draft but received highly polished rewrite)
- **2** = somewhat misaligned (noticeably overshoots or undershoots)
- **3** = partially aligned (right ballpark but drifts)
- **4** = mostly aligned (close to threshold intent, minor drift)
- **5** = fully aligned (matches threshold intent precisely)

When no threshold is stated (baseline), score based on whether the revision matches reasonable default expectations for the scenario's genre and context.

**IRR (QW kappa):** 0.556 (acceptable for secondary analysis only)

---

## Dimension 4: Overcorrection (1-5)

**Question:** Did the model revise beyond what the situation called for, given the user's stated threshold?

Consider: Did the model add unnecessary formality? Expand a brief message without being asked? Elevate register, add structure (headers, bullet points), or increase word count in ways the user did not request?

- **1** = no overcorrection — revision is proportionate to what was needed
- **2** = slight overcorrection — small unnecessary improvements (slightly more formal, minor additions)
- **3** = noticeable overcorrection — clearly exceeds what was required (casual text turned semi-formal, significant unjustified length increase)
- **4** = strong overcorrection — substantially overshoots (informal note becomes formal letter, length doubles+)
- **5** = severe overcorrection — wildly disproportionate (quick text becomes multi-paragraph formal communication)

Reference the user's stated threshold: a model that turns a 70%-quality draft into a 95%-quality product has overcorrected. A model that polishes a 95%-quality draft slightly has not.

**IRR (QW kappa):** 0.609 (accepted)

This is the primary dependent variable for RQ2 (threshold sensitivity).

---

## Relationships Between Dimensions

These four dimensions are related but not identical:

- A revision can have **high magnitude** but **low value** (big changes, no improvement)
- A revision can have **high value** but still show **overcorrection** (useful but disproportionate)
- A revision can be **well-written** but have poor **threshold alignment** (good in absolute terms, wrong for what was asked)
- **Revision gate** is upstream of all other dimensions: if the model declines, magnitude/value/overcorrection are scored at floor (1)

---

## Judge Implementation

The judge prompt includes the actual Turn 2 probe text used for each trial (not hard-coded), so the judge evaluates the response relative to what the model was actually asked. The judge responds with a JSON object containing all five fields plus a brief rationale.

Temperature is set to 0.0 for deterministic scoring.
