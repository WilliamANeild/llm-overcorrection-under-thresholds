# Evaluation Rubric

## Purpose

The central evaluation problem in this project is distinguishing between revisions that are simply larger and revisions that are actually meaningful relative to the user’s intended threshold.

A model may revise aggressively without making a change that is genuinely useful for the user’s stated goal. The rubric is therefore meant to evaluate revision quality, not just revision quantity.

## Core Evaluation Question

When a model revises an output after being asked "Can this be improved?", does the revision meaningfully improve the output relative to the original threshold, or does it reflect unnecessary overcorrection?

## Main Dimensions

### 1. Revision Gate

This dimension captures whether the model treats the original output as needing revision at all.

Questions:
- Does the model claim the output can be improved?
- Does it actually revise, or only comment on possible improvement?
- Does it frame revision as necessary, optional, or minor?

### 2. Revision Magnitude

This dimension captures how much the revised output changes relative to the original.

Questions:
- How extensive are the edits?
- Are the changes local or substantial?
- Does the revision alter wording, structure, tone, meaning, or all of the above?

This dimension is meant to capture amount of change, not value.

### 3. Revision Value

This dimension captures whether the revision actually adds value relative to the user’s stated threshold.

Questions:
- Does the revision better satisfy the threshold the user originally gave?
- Does it improve the output in a way that matters for the stated purpose?
- Does it make the output more aligned with what the user needed, rather than simply more polished?

### 4. Overcorrection

This dimension captures whether the model goes beyond the user’s intended standard.

Questions:
- Does the model revise more aggressively than the threshold seems to justify?
- Does it make changes that feel unnecessary for the stated purpose?
- Does it behave as though “better in general” matters more than “good enough for this user”?

## Working Rubric Categories

A revision may eventually be classified into one of the following broad categories:

### 1. No Revision Needed
The original output already appears to satisfy the intended threshold, and further revision is unnecessary.

### 2. Minor but Appropriate Revision
The model makes limited changes that are aligned with the threshold and improve the output without overshooting the user’s goal.

### 3. Meaningful and Appropriate Revision
The model makes a substantial revision that clearly improves the output in a way that fits the user’s stated standard.

### 4. Unnecessary Revision
The model revises, but the changes do not add meaningful value relative to the intended threshold.

### 5. Overcorrection
The model revises in a way that exceeds the user’s intended standard, producing changes that are too strong, too polished, too aggressive, or otherwise misaligned with the original goal.

## Main Open Issue

The biggest unresolved question is how to define meaningful revision in a way that is clean, defensible, and consistent.

In particular, the project still needs to decide how much weight to place on:
- surface-level change
- semantic change
- threshold alignment
- human judgment of usefulness

## Current Direction

The current direction is to treat revision evaluation as a combination of:
- whether revision occurred
- how much the output changed
- whether the change was actually valuable relative to the threshold

The rubric will likely need peer feedback and several rounds of refinement before it is stable enough for a full pilot.