# Experimental Design

## Core Setup

This project studies how large language models respond to user-defined quality thresholds during revision.

The basic interaction structure is:

1. A user gives a task along with an intended threshold or target standard.
2. The model produces an initial output.
3. The user gives no further detailed guidance and instead asks: **"Can this be improved?"**
4. The model either declines revision or proposes a revised version.
5. The project evaluates both whether the model chooses to revise and how much the revised output changes.

The goal is to test whether the model’s revision behavior remains calibrated to the user’s intended threshold or whether it continues optimizing beyond what the user actually wanted.

## Main Experimental Comparison

The current comparison of interest is between two forms of threshold framing:

### 1. Numeric Threshold Framing
Examples:
- "This only needs to be around a 70."
- "This should be at least a 90."
- "This only needs to be good enough for an 80."

### 2. User-Defined Contextual Threshold Framing
Examples:
- "Make it good enough that nobody will think poorly of me."
- "Make it clear and polite enough to get my point across."
- "Make it strong enough for the purpose, but it does not need to be perfect."

The project asks whether these different framing styles change:
- whether the model says further improvement is needed
- how aggressively the model revises once revision begins

## Core Outcomes

### Revision Gate
Whether the model decides the output can or should be improved at all.

This is the first decision point in the interaction. A model may:
- decline revision
- suggest minor improvements
- immediately produce a revised version

### Revision Magnitude
How much the model changes once it decides to revise.

This is currently the main dependent variable of interest. The project is especially concerned with whether models produce larger-than-necessary changes relative to the user’s stated threshold.

### Revision Value
Whether the revision is actually meaningful relative to the original threshold.

This remains the main open evaluation issue. A revision may be larger without being better aligned to the user’s intended standard.

## Main Design Logic

The current design is meant to isolate a simple but important question:

When a user signals that a response only needs to meet a certain threshold, does the model later respect that threshold when asked if the output can be improved, or does it behave as though all revision opportunities should be pursued?

The design therefore focuses on the interaction between:
- threshold framing
- prompt wording
- model conditioning
- revision behavior

## Open Design Questions

Several design details still need to be refined:

- how to measure revision magnitude cleanly
- how to distinguish meaningful revision from larger revision
- how to operationalize model conditioning
- which task types best fit the project
- whether to compare multiple models or keep the first study within one model family

## Current Direction

The current direction is to keep the setup simple, defensible, and easy to pilot. The first version of the study will likely prioritize:
- a small set of controlled task types
- a comparison between numeric and contextual threshold framing
- a fixed follow-up revision prompt
- a rubric-based evaluation of revision value