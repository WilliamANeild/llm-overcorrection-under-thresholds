# Revision Evaluation Rubric

## Purpose

This rubric is meant to evaluate whether an LLM revision is actually better relative to the user's intended threshold, rather than simply larger, more polished, or more aggressive.

The core evaluation problem in this project is that revision quality cannot be captured by a single measure. A model can revise a lot without improving the output in a way that matters for the user's stated goal.

This draft rubric therefore evaluates revision behavior across four dimensions:

1. revision magnitude  
2. revision value  
3. threshold alignment  
4. overcorrection  

---

## Dimension 1: Revision Magnitude

**Definition:**  
How much the model changes once it decides to revise.

**Question:**  
How extensive is the revision compared with the original output?

### Scale
- **1** = almost no change
- **2** = small local edits
- **3** = moderate revision
- **4** = substantial revision
- **5** = major rewrite

**What this dimension captures:**  
The size of the revision, not whether the revision was good.

---

## Dimension 2: Revision Value

**Definition:**  
Whether the revision meaningfully improves the output for the user's stated purpose.

**Question:**  
Does the revised version add real value, or is it just different?

### Scale
- **1** = no meaningful improvement
- **2** = very slight improvement
- **3** = some useful improvement
- **4** = clearly meaningful improvement
- **5** = major improvement relative to the task

**What this dimension captures:**  
Whether the revision helps in a way that actually matters.

---

## Dimension 3: Threshold Alignment

**Definition:**  
Whether the revision remains faithful to the standard the user originally set.

**Question:**  
Does the revised version still match the user's intended threshold?

### Scale
- **1** = strongly misaligned with threshold
- **2** = somewhat misaligned
- **3** = partially aligned
- **4** = mostly aligned
- **5** = fully aligned with intended threshold

**What this dimension captures:**  
Whether the model respected the user's actual target rather than defaulting to a broader or stronger standard.

---

## Dimension 4: Overcorrection

**Definition:**  
Whether the model revised beyond what the situation called for.

**Question:**  
Did the model make the output more polished, stronger, or more aggressive than the user actually needed?

### Scale
- **1** = no overcorrection
- **2** = slight overcorrection
- **3** = noticeable overcorrection
- **4** = strong overcorrection
- **5** = severe overcorrection

**What this dimension captures:**  
Whether the model overshot the user's intended standard.

---

## Important Notes

These four dimensions are related, but they are not identical.

- A revision can have **high magnitude** but **low value**
- A revision can have **high value** but still show some **overcorrection**
- A revision can be **well-written** in general but still have poor **threshold alignment**
- A revision can be **substantial** without being useful

That is why the rubric should not collapse everything into a single vague judgment like "better" or "worse."

---

## Working Interpretation

The current logic of the project is:

- first ask whether the model revised at all
- then measure how much it changed
- then evaluate whether the change was useful
- then judge whether it stayed aligned with the user's intended threshold
- then assess whether it overshot into overcorrection

This makes the rubric a structured way to separate:
- bigger change
- better change
- threshold-respecting change
- unnecessarily strong change

---

## Open Questions for Peer Feedback

This draft rubric still needs outside pressure testing.

Main questions:
1. are these the right four dimensions?
2. are any of them redundant?
3. which dimensions should be primary versus secondary?
4. should any dimension use a simpler scale?
5. how should conflicts be handled, such as high value but also moderate overcorrection?

---

## Current Position

This is the first real draft of the evaluation framework.

It is not final, but it turns the main bottleneck of the project into something concrete enough to discuss, critique, and improve.