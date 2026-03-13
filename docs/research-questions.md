# Research Questions

## Main Research Question

How do threshold framing and model conditioning shape whether a large language model decides an output should be revised and how much it changes once revision begins?

More specifically, this project asks whether LLM revision behavior stays calibrated to the user’s intended threshold or whether models continue optimizing beyond what the user actually asked for.

## Secondary Research Questions

- Do LLMs say an output can be improved too often, even when it already appears to satisfy the user’s intended threshold?
- Do different forms of threshold framing, especially numeric thresholds versus user-defined contextual thresholds, produce different revision behavior?
- When a model revises, does it make meaningful improvements or simply larger, more aggressive, or more polished changes?
- Under what conditions does revision become miscalibrated relative to the user’s stated standard?
- How much of this behavior appears to come from the interaction between threshold framing, prompt wording, and model conditioning?

## Working Definitions

**Threshold framing** refers to the way the user defines an acceptable target standard for the output. This may be expressed numerically, such as “this needs to be at least a 90,” or contextually, such as “make it good enough that nobody will think poorly of me.”

**Model conditioning** refers to the background instruction, setup, or prompting context that may shape how strongly the model tends to revise, improve, or continue optimizing an output.

**Overcorrection** refers to revision that goes beyond the user’s intended threshold and makes changes that are unnecessary, overly aggressive, or misaligned with the user’s actual goal.

**Miscalibrated revision behavior** refers to revision behavior that does not appropriately match the user’s stated standard, either because the model revises when it should not or because it revises more aggressively than the situation requires.

## Boundary of the Claim

This project is not asking whether revision is beneficial in an absolute sense. It is asking whether revision is appropriate relative to the standard the user originally set.

The core claim is that LLMs may be biased toward continued fixing, refining, and upgrading even when the output is already sufficient for the user’s stated purpose.