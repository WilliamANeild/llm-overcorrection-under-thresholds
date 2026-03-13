# Update Notes

## Project Title

**When LLMs Revise Beyond the Intended User-Defined Threshold**  
*How Threshold Framing and Model Conditioning Produce Overcorrection in LLM Revision*

## Core Project Idea

This project studies whether large language models revise beyond the user’s intended standard when asked whether an output can be improved. The central concern is not whether revision is beneficial in an absolute sense, but whether revision is appropriate relative to the threshold the user originally set.

The project focuses on how threshold framing and model conditioning shape revision behavior, especially whether a model chooses to revise at all and how much it changes once revision begins.

## Main Research Question

How do threshold framing and model conditioning shape whether a large language model decides an output should be revised and how much it changes once revision begins?

More specifically, the project asks whether revision behavior stays calibrated to the user’s intended threshold or whether the model continues optimizing beyond what the user actually wanted.

## Current Framing

The project is centered on **miscalibrated revision behavior** and **overcorrection** in LLMs.

The current idea is that overcorrection is not just a model problem or just a prompt problem. It likely comes from the interaction between:

- user threshold
- prompt framing
- model conditioning

## Core Experimental Setup

The current design follows a simple structure:

1. The user gives a task and defines a threshold.
2. The model produces an initial output.
3. The user asks: **"Can this be improved?"**
4. The model either declines revision or revises the output.
5. The project evaluates whether the model revised and how much it changed.

## Main Condition Comparison

The main comparison currently under consideration is between:

### Numeric threshold framing
Examples:
- "This should be at least a 90."
- "This only needs to be around a 70."

### User-defined contextual threshold framing
Examples:
- "Make it good enough that nobody will think poorly of me."
- "Make it clear and polite enough to get my point across."

## Main Outcomes of Interest

### 1. Revision Gate
Whether the model decides the output can or should be improved at all.

### 2. Revision Magnitude
How much the output changes once the model begins revising.

### 3. Revision Value
Whether the revision is actually meaningful relative to the user’s intended threshold.

## Biggest Open Question

The largest unresolved issue is the evaluation rubric.

The project still needs a clean way to distinguish between:
- revisions that are simply larger or more polished
- revisions that are actually meaningful relative to the user’s stated threshold

## Immediate Next Steps

- refine the evaluation rubric
- expand the prompt bank
- tighten the threshold framing conditions
- think through how model conditioning should be introduced
- prepare a clean summary of the setup for future presentation use