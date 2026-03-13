# Prompt Bank

## Purpose

This file collects early prompt structures for the project. The goal is to build a set of comparable prompt examples that differ mainly in threshold framing while keeping the overall task and revision setup consistent.

The current project is especially interested in how different threshold framings affect whether a model chooses to revise and how much it changes once revision begins.

## Core Prompt Structure

Each prompt sequence currently has three parts:

1. **Task**
2. **Threshold framing**
3. **Revision follow-up**

Basic pattern:

- user gives a task
- user defines an intended quality threshold
- model produces an initial output
- user asks: **"Can this be improved?"**

## Threshold Framing Families

### 1. Numeric Threshold Framing

These prompts define adequacy using a number or score-like target.

Examples:

- "Write this so it would be around a 70."
- "Make this at least a 90."
- "This only needs to be good enough for an 80."
- "Please make this around an 85, not necessarily perfect."

### 2. User-Defined Contextual Threshold Framing

These prompts define adequacy in social, functional, or contextual terms.

Examples:

- "Make it good enough that nobody will think poorly of me."
- "Make it clear and polite enough to get my point across."
- "Make it strong enough for the purpose, but it does not need to be perfect."
- "Make it good enough to sound thoughtful and competent."

## Shared Revision Prompt

The main follow-up prompt is:

**"Can this be improved?"**

This prompt is intentionally vague. It does not restate the original threshold and does not specify what kind of improvement is being requested. That ambiguity is central to the design.

Possible later alternatives:
- "Is this good enough?"
- "Would you change anything?"
- "Can this be made better?"

For now, the project should likely keep one fixed follow-up prompt.

## Early Task Types

The first prompt bank will probably work best if it uses tasks that are easy to compare across conditions.

Possible task types:
- short professional emails
- short written responses
- message polishing or rewriting tasks
- low-stakes persuasive or explanatory writing
- simple communication tasks with obvious audience goals

The initial priority is not task diversity. It is consistency across threshold conditions.

## Example Prompt Templates

### Template A: Numeric Threshold

**User prompt:**  
Write a short email declining an invitation. Make it at least a 90. I want it to sound polite and professional.

**Follow-up:**  
Can this be improved?

---

### Template B: Contextual Threshold

**User prompt:**  
Write a short email declining an invitation. Make it good enough that nobody will think poorly of me. I want it to sound polite and professional.

**Follow-up:**  
Can this be improved?

---

### Template C: Numeric Threshold, Lower Standard

**User prompt:**  
Write a short email declining an invitation. This only needs to be around a 70. I just want it to be acceptable and clear.

**Follow-up:**  
Can this be improved?

---

### Template D: Contextual Threshold, Functional Standard

**User prompt:**  
Write a short email declining an invitation. Make it clear and polite enough to get my point across. It does not need to be perfect.

**Follow-up:**  
Can this be improved?

## Open Prompt Questions

The prompt bank still needs refinement in several areas:

- how many threshold examples should exist per framing family
- whether thresholds should vary by difficulty or stakes
- whether certain task types naturally favor numeric or contextual thresholds
- how consistent the wording should be across prompts
- whether the first prompt bank should stay entirely within one writing domain

## Current Direction

The first version of the prompt bank should stay narrow and controlled. The main goal is to create comparable prompts where the threshold framing changes but the task remains stable.

That will make it easier to observe whether threshold language affects revision gate behavior, revision magnitude, and eventual overcorrection.