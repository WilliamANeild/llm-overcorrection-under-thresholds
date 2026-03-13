# Prompt Bank

## Purpose

This file defines the core prompt materials for the project. The goal is to build a set of comparable communication tasks that remain fixed at the scenario level while varying only the user's stated expectation threshold.

The project is specifically interested in how different expectation framings affect:
- whether a model treats an output as needing revision
- how much the model changes once revision begins
- whether the revision remains aligned with the user's intended standard or becomes overcorrection

This file focuses on the **scenario layer** of the prompt bank. The expectation layers, numeric and qualitative, are designed to be swapped into each scenario while keeping the underlying communication task unchanged.

## Core Prompt Structure

Each prompt sequence is built from three components:

1. **Base scenario**
2. **Expectation layer**
3. **Revision follow-up**

The general structure is:

- the user gives a realistic communication task
- the user states an intended threshold for what counts as good enough
- the model produces an initial output
- the user then asks: **"Can this be improved?"**

The purpose of this design is to isolate whether threshold framing changes revision behavior when the follow-up request is vague and does not restate the original standard.

## Scenario Design Logic

The scenarios in this prompt bank are meant to cover several of the most common and useful categories of everyday communication. They are intentionally varied across audience, tone, stakes, and purpose so the project can test whether revision behavior changes across different kinds of writing.

The current set of scenarios covers:

- **public professional self-presentation**
- **internal workplace communication**
- **personal family communication**
- **informal coworker humor**
- **external client-facing persuasion**

This gives the prompt bank a strong spread without making the study too broad too early.

## Shared Revision Follow-Up

The main follow-up prompt is:

**"Can this be improved?"**

This prompt is intentionally vague. It does not restate the user's threshold and does not specify what kind of improvement is being requested. That ambiguity is central to the project because it forces the model to decide for itself whether further revision is actually needed.

Possible later alternatives could include:
- "Is this good enough?"
- "Would you change anything?"
- "Can this be made better?"

For now, the cleanest design is to keep one fixed follow-up prompt across all conditions.

## Threshold Framing

Each base scenario will be paired with two families of expectation framing:

### 1. Numeric expectation framing
These prompts define adequacy through an explicit score-like target, such as 70, 75, 80, 85, 90, 95, or 100.

### 2. Qualitative expectation framing
These prompts define adequacy in contextual or functional language, such as whether the output is good enough to get the point across, avoid reflecting poorly on the user, or feel fully polished and ready to send.

The scenario itself should remain unchanged across versions so that threshold framing is the main thing varying.

## Scenario Set

### Scenario 1: LinkedIn Job Announcement

This scenario covers **public-facing professional self-presentation**.

The user is announcing a new role as a **Police Officer with the City of Miami Police Department** after graduating from **Florida International University** with a degree in criminal justice and completing academy training earlier in the spring.

This scenario is useful because it is:
- public-facing
- image-conscious
- professional but still personal
- vulnerable to overcorrection into sounding overly polished, performative, or insincere

The target output is a short LinkedIn post that sounds grateful, professional, and excited, while avoiding anything overly dramatic or cheesy.

### Scenario 2: PTO Request to a Manager

This scenario covers **internal professional communication** with moderate stakes.

The user is emailing their manager, **Dana Mitchell**, to request **Friday, April 17, 2026** off for a family event out of town. The request is being made about a month in advance, and the user wants to communicate responsibility and preparedness without sounding too formal or too apologetic.

This scenario is useful because it tests:
- workplace professionalism
- clarity and tone control
- moderate-stakes adequacy
- whether models overcorrect into excessive formality or unnecessary elaboration

The target output is a short workplace email that feels responsible, respectful, and realistic.

### Scenario 3: Sister-in-Law Brunch Cancellation

This scenario covers **personal family communication**.

The user is texting their sister-in-law, **Emily**, to say they cannot make brunch on **Sunday, March 22** because something came up that morning. The user wants to sound warm, genuine, and briefly apologetic, while keeping the message casual and natural.

This scenario is useful because it tests:
- low-stakes social communication
- warmth and naturalness
- family tone rather than workplace tone
- whether revision leads to awkward over-polishing in an informal context

The target output is a short family text that feels believable and emotionally appropriate.

### Scenario 4: Funny Text to a Coworker

This scenario covers **informal workplace humor**.

The user is texting their coworker, **Jake**, about how chaotic the workday has been after sitting through **three meetings that could have been emails**, with a fourth meeting now added at 4:30 PM. The goal is to sound funny and relatable without becoming unnatural or over-written.

This scenario is useful because it tests:
- humor
- informality
- realism in casual work communication
- whether models overcorrect by making something less natural, less funny, or too elaborate

The target output is a short witty text that sounds like something an actual coworker would send.

### Scenario 5: Sales Email to an Outside Client

This scenario covers **external persuasive communication**.

The user is writing to an outside client, **Rachel Thompson**, who organizes events for schools and neighborhood associations. The user wants to explain that their company, **SkyHigh Bounce Rentals**, is offering **15% off bouncy house rentals booked before April 30** for spring events in the Atlanta area.

This scenario is useful because it tests:
- client-facing persuasion
- professionalism with light sales tone
- transactional communication
- whether models overcorrect into being too pushy, too polished, or too promotional

The target output is a short sales email that feels clear, friendly, and commercially useful without being aggressive.

## Prompt Construction Plan

Each of the five base scenarios will be reused across both expectation families.

That means each scenario will eventually be paired with:
- multiple **numeric threshold** variants
- multiple **qualitative threshold** variants

The purpose of this structure is to make the scenario constant while varying only the user's standard for what counts as sufficient.

This will allow the project to test whether threshold framing changes:
- revision gate behavior
- revision magnitude
- revision value
- threshold alignment
- overcorrection

## Open Questions

The prompt bank still needs refinement in a few areas:

- whether five scenarios are enough for the first pilot
- whether each scenario should be kept at a similar target length
- whether some scenarios naturally invite more revision than others
- whether additional scenarios should be added later for high-stakes or highly technical writing
- how tightly the wording of each scenario should be controlled across all versions

## Current Direction

The current direction is to keep the first prompt bank broad enough to cover core communication settings, but controlled enough that threshold framing remains the main variable of interest.

The five current scenarios give the project a strong base across public, professional, personal, humorous, and persuasive writing. The next step is to pair each of those scenarios with the numeric and qualitative expectation ladders and begin building the full prompt matrix.