# Rules: Discussion

Retrieved 2026-09-02. 23 sections read in full.

Every paper below was fetched as HTML (arxiv.org/html/ID, falling back to
ar5iv.labs.arxiv.org/html/ID), converted to text, and the discussion section (or,
where none exists, whatever section carries the discussion function) was extracted
and read end to end. Word counts are from that extracted text; body-word counts run
from the Introduction heading to the References heading and include figure and table
captions, so shares are approximate to about a percentage point. Every quotation
below is verbatim from the fetched HTML. The only edits are the removal of the
extra spaces the converter leaves around inline citations and math, e.g.
`( Huang et al., 2023 )` rendered as `(Huang et al., 2023)`. Nothing was
reconstructed from memory.

**Not accessed.** ACL Anthology PDFs were not parsed; every paper here was available
as arXiv HTML, so the Anthology was not needed. The arXiv API was rate-limited
during this session, so candidate papers were found by web search and then verified
by reading the fetched HTML title, not by API metadata. CHI and UIST papers that
exist only in the ACM DL with no arXiv preprint (Zamfirescu-Pereira et al.,
"Why Johnny Can't Prompt"; Bhat et al. 2022) were **not** read and are not cited
here, though other papers in the corpus cite them.

---

## Corpus

Nine papers are HCI/human-AI-interaction venues or position pieces (marked HCI);
fourteen are core NLP/ML (marked NLP). Audience of implications is coded from the
discussion text only: R = researchers, S = system/interface/agent designers,
M = model or LLM builders, U = end users, — = no implications stated.

| # | Paper | arXiv ID | Type | Separate discussion? | Disc. words | % of body | Subsecs | Audience |
|---|---|---|---|---|---|---|---|---|
| 1 | Huang et al., *LLMs Cannot Self-Correct Reasoning Yet* | 2310.01798 | NLP | Merged: "6 Conclusion and Discussion" | 585 | 14.0 | 0 (3 run-in) | R |
| 2 | Kamoi et al., *When Can LLMs Actually Correct Their Own Mistakes?* | 2406.01297 | NLP | No; function split across "7 Summary of Our Analysis", "8 Checklist", "11 Future Directions" | 575 | 8.9 | 3 | R |
| 3 | Laban et al., *LLMs Get Lost In Multi-Turn Conversation* | 2505.06120 | NLP | Renamed: "7 Implications" | 1828 | 22.8 | 6 | S, M, R, U |
| 4 | Sharma et al., *Towards Understanding Sycophancy* | 2310.13548 | NLP | No; "6 Conclusion" only | 85 | 1.5 | 0 | R, M |
| 5 | Stechly et al., *GPT-4 Doesn't Know It's Wrong* | 2310.12397 | NLP | No; "5 Conclusion" only | 194 | 4.9 | 0 | — |
| 6 | Tyen et al., *LLMs cannot find reasoning errors* | 2311.08516 | NLP | Folded into results: "3.1 Discussion", "4.2 Discussion" | 609 | 10.5 | 0 | R |
| 7 | Madaan et al., *Self-Refine* | 2303.17651 | NLP | Merged: "6 Limitations and Discussion" | 189 | 3.9 | 0 | — |
| 8 | Shinn et al., *Reflexion* | 2303.11366 | NLP | No; "5 Limitations" + "6 Broader impact" | 269 | 5.8 | 1 | R |
| 9 | Valmeekam et al., *Can LLMs Really Improve by Self-critiquing Their Own Plans?* | 2310.08118 | NLP | No; "6 Conclusion and Future Work" | 172 | 7.5 | 0 | — |
| 10 | Jiang et al., *Self-[In]Correct* | 2404.04298 | NLP | Yes: "6 Further Discussion" | 413 | 7.1 | 2 | R |
| 11 | Li et al., *Confidence Matters* | 2402.12563 | NLP | No; "6 Conclusion" + "Limitations" | 254 | 6.0 | 1 | — |
| 12 | Chakrabarty et al., *Creativity Support in the Age of LLMs* | 2309.12570 | HCI | Yes: "7. Discussion" | 714 | 7.9 | 3 | R, M |
| 13 | Wang et al., *Task Supportive and Personalized Human-LLM Interaction* | 2402.06170 | HCI | Merged: "6. Discussion and conclusion" | 717 | 18.9 | 0 (4 run-in) | S, R |
| 14 | Dang et al., *Choice Over Control* | 2303.03199 | HCI | Yes: "9. Discussion" | 2664 | 26.3 | 11 | R, S, M |
| 15 | Shankar et al., *Who Validates the Validators?* | 2404.12272 | HCI | Yes: "8. Discussion" | 1662 | 14.1 | 3 | S, R |
| 16 | Lee et al., *CoAuthor* | 2201.06796 | HCI | Yes: "6. Discussion" | 576 | 6.7 | 5 | R |
| 17 | Ibrahim et al., *Measuring and Mitigating Overreliance* | 2509.08010 | HCI | Yes: "Discussion" | 492 | 7.9 | 3 | R, S |
| 18 | Pang et al., *Understanding the LLM-ification of CHI* | 2501.12557 | HCI | Yes: "5. Discussion" | 5444 | 36.7 | 10 | R |
| 19 | Lee et al., *Evaluating Human-Language Model Interaction* | 2212.09746 | HCI | Yes: "5 Discussion" | 2506 | 17.0 | 17 | R |
| 20 | Ibrahim et al., *Towards Interactive Evaluations for Interaction Harms* | 2405.10632 | HCI | Renamed: "5 Open challenges and ways forward" | 838 | 19.1 | 4 | R, S |
| 21 | Olausson et al., *Is Self-Repair a Silver Bullet?* | 2306.09896 | NLP | No; "5 Limitations" + "6 Conclusion" | 472 | 8.1 | 1 | R |
| 22 | Xu et al., *Pride and Prejudice: LLM Amplifies Self-Bias* | 2402.11436 | NLP | No; "6 Conclusion" + "Limitations" | 126 | 2.5 | 0 | — |
| 23 | Wu et al., *CollabLLM* | 2502.00640 | NLP | No; "8 Conclusion" only | 89 | 1.6 | 0 | — |

### Counts

**Does a separate discussion section exist?**

- **Standalone section titled "Discussion" or "Further Discussion": 8 of 23** — #10, #12, #14, #15, #16, #17, #18, #19.
- **Merged into a compound heading: 3** — "Conclusion and Discussion" (#1), "Limitations and Discussion" (#7), "Discussion and conclusion" (#13).
- **Renamed to a functional heading: 3** — "Implications" (#3), "Open challenges and ways forward" (#20), "Summary of Our Analysis" + "Future Directions" (#2).
- **Folded into results as per-experiment subsections: 1** — Tyen (#6) puts "3.1 Discussion" immediately after the mistake-finding results and "4.2 Discussion" immediately after the correction results.
- **Absent; function carried entirely by Conclusion and Limitations: 8** — #4, #5, #8, #9, #11, #21, #22, #23.

Split by community: **7 of 9 HCI papers** have a standalone Discussion (the other two merge or rename); **1 of 14 core-NLP papers** does (#10). Folding the discussion elsewhere is the NLP default, not a shortcut.

**Length.** Median 575 words, 7.9% of body. Split by community the gap is large: HCI median **838 words**, core-NLP median **262 words**. Range 85 words (Sharma) to 5,444 (LLM-ification of CHI). Only four papers exceed 2,000 words and all four are HCI (#14, #15 at 1,662, #18, #19).

**Second-person address.** The token "you"/"your" appears in the discussion of **4 of 23** papers. Three are inside quoted material and not the authors' own prose: a survey question quoted back to participants (#19: "Did the way you chose to interact with the AI Teammate change over time?"), a participant quotation (#12: MG wrote "Also when you ask it to the mimic the style of a writer..."), and a prompt string a user would type (#3: "Please consolidate everything I've told you so far"). **One paper addresses the reader as "you"** (#18, 43 occurrences), exclusively inside a numbered set of reflective questions for researchers, explicitly framed as "prompts for reflection, not a checklist for completion." **Zero of 23 address an end user as "you."**

**Imperatives.** Three occurrences of an imperative-mood sentence or heading in the whole sample. #15: "Consider the example of word count." #18: "Consider the questions under LLMs as research tools above." #3: two subsection headings, "If time allows, try again." and "Consolidate before retrying." Only Laban's are directed at end users, they sit in §7.4 (the last subsection before the conclusion), and they are immediately walled off: "These two recommendations remain cumbersome for users and can only offer patched solutions rather than a principled approach." **Zero of 23 discussions end on an imperative.** **Zero open with one.**

**Audience of implications** (a paper is counted once per audience it addresses):

- **Researchers: 17** — #1, #2, #3, #4, #6, #8, #10, #12, #13, #14, #15, #16, #17, #18, #19, #20, #21.
- **System / interface / agent designers: 6** — #3, #13, #14, #15, #17, #20.
- **Model or LLM builders: 4** — #3, #4, #12, #14.
- **End users: 1** — #3, and only in a subsection named for that audience.
- **No implications at all: 6** — #5, #7, #9, #11, #22, #23 (#7 and #11 state limitations only).

Laban is the only paper in the sample that segments implications by audience with a subsection per audience, and it is also the only one that speaks to end users at all. **The modal discussion in this literature addresses researchers and nobody else.**

**Future work.** Own top-level section: 1 (#2, "11 Future Directions"). Subsection of the discussion: 2 (#19 "5.4 Future Work"; #15 "8.3 Future Work and Limitations"). Merged into the conclusion heading: 1 (#9, "6 Conclusion and Future Work"). Otherwise dispersed as forward-looking clauses inside discussion, limitations or conclusion paragraphs: 19. Where those clauses concentrate: the **discussion** in 11 papers, a separate **Limitations** section in 6, the **conclusion** in 4.

---

## Structure and headings (verbatim collection)

### Audience-segmented (1 paper)

Laban et al. 2505.06120:
> 7 Implications
> 7.1 Implications for System and Agent Builders
> 7.2 Implications for LLM Builders
> 7.3 Implications for NLP Practitioners
> 7.4 Implications for Users of Conversational Systems
> — If time allows, try again.
> — Consolidate before retrying.

### Theme-per-subsection, each naming a substantive claim or object (the HCI norm)

Dang et al. 2303.03199:
> 9.1. Choice vs. Control
> 9.2. Guiding Suggestions with Diegetic Prompts
> 9.3. Challenges of Integrating Non-Diegetic Prompts
> 9.3.1. Non-Diegetic Prompts Interrupt the Writing Process
> 9.3.2. Non-Diegetic Prompts can be Hard to Write
> 9.4. Perceived Role of the AI
> 9.4.1. Two Perspectives on the Main Role: Proposer vs Transcriber
> 9.4.2. Non-diegetic Prompts Reflect Users' Perception of the AI
> 9.5. Limitiations and Reflections on Methodology
> 9.6. Beyond Writing: Diegetic and Non-diegetic Interaction in Generative Systems
> 9.7. Implications for LLMs and User Interfaces

Shankar et al. 2404.12272:
> 8.1. Implications of Criteria Drift for LLM Evaluation Assistants
> 8.2. Operationalizing Assertions
> 8.3. Future Work and Limitations

Lee et al. 2201.06796:
> 6.1. Datasets as Boundary Objects
> 6.2. Potential Use Cases of CoAuthor
> 6.2.1. Formulate Hypotheses
> 6.2.2. Assess the Plausibility of Hypotheses
> 6.2.3. Train and Evaluate Language Models

2501.12557:
> 5.1. Revealed Growth Opportunities for HCI
> 5.1.1. Beyond language-based applications
> 5.1.2. Beyond empirical and artifact contributions
> 5.1.3. How LLMs impact prototyping standards
> 5.2. Challenges: Validity, Reproducibility, and Consequences
> 5.2.1. Proprietary LLMs raise reproducibility concerns
> 5.2.2. LLM properties introduce additional research validity concerns
> 5.2.3. Consequences, Risks, and Broader Impacts
> 5.3. Guiding questions for HCI researchers using LLMs
> 5.4. Limitations

Lee et al. 2212.09746:
> 5.1 General Challenges in Human Evaluation — Cost. / Reproducibility. / Subjectivity.
> 5.2 General Challenges in Interactive Evaluation — Study design. / Latency. / Harms.
> 5.3 Limitations Specific to Our Experiment Design — Task selection. / User interface design. / Model selection. / System logic design. / User recruitment.
> 5.4 Future Work — Accommodation. / Lasting impact.

### Question-as-heading (3 papers)

2309.12570:
> 7.1. Do current AI safety guardrails prevent writers from exploring more complex and darker topics?
> 7.2. Localized rewriting in well-known authors' styles as a feature for creativity support for emerging writers
> 7.3. Learning to better infer writer intentions can improve suggestion quality

2405.10632:
> 5.1 How can we ethically work with human participants on studying harms? When are user simulations appropriate replacements?
> 5.2 How can we improve researcher access to data for understanding interaction harms?
> 5.3 What infrastructure do we need to facilitate interactive evaluations?
> 5.4 How can interactive evaluations produce actionable findings that guide stakeholder decisions? What are the limitations of controlled studies in capturing broader impacts?

Huang et al. 2310.01798 uses a question heading in **results**, not discussion:
> 3.3 Why does the performance not increase, but instead decrease?

### Run-in bold headings inside a single unnumbered discussion (2 papers)

Huang et al. 2310.01798:
> Leveraging external feedback for correction.
> Evaluating self-correction against baselines with comparable inference costs.
> Putting equal efforts into prompt design.

2402.06170:
> Insights and Implications for System Evaluation:
> Proactive User Interface and System Design:
> Recognizing the Unique Position of Crowd Workers:
> Limitations and Future Directions:

### Tension-per-subsection (1 paper)

2509.08010 opens with a one-sentence roadmap and then three named tensions:
> We close by addressing three tensions that arise in discussions of overreliance on LLMs, each of which informs why we view measurement as a central and urgent research priority.
> The current lack of empirical evidence
> The role of advancing AI capabilities
> Societal vs. technical interventions

### Observations about headings

- **No heading in the sample is a slogan, an imperative sentence, or a bumper sticker.** Every one is either a noun phrase naming an object of study ("Choice vs. Control", "Operationalizing Assertions", "Datasets as Boundary Objects"), an audience label ("Implications for LLM Builders"), a full declarative claim ("Non-Diegetic Prompts Interrupt the Writing Process", "Proprietary LLMs raise reproducibility concerns"), or a question. Laban's two user-facing imperative headings are the sole exception and they are the deepest headings in the paper.
- **Six of eight standalone discussions open with a one-to-three-sentence roadmap** naming what the subsections will do (#15, #16, #17, #18, #19, #20). Example, #15: "Here, we unpack criteria drift and how it affects alignment, discuss the implications of our findings for future LLMOps evaluation assistants, and outline some open questions."

---

## The line between results and discussion

The corpus draws it in a consistent place, and it is not the place a practitioner-advice draft draws it.

**Stays in results.**

1. **The mechanism, when it was measured.** Huang's explanation of why accuracy falls is section **3.3**, inside results, under a question heading, and it is split into "Empirical Analysis." (a count of answer flips) and "Intuitive Explanation." (an argument from prompt conditioning). The discussion contains no mechanism at all.
2. **Decompositions of a headline number.** Laban's finding that aggregate degradation is 16% aptitude loss and 112% unreliability increase is §6.2, in results. So is the sentence that reframes the paper's own construct: "This refines our definition of the lost in conversation phenomenon."
3. **Reconciliation with a prior paper's conflicting result.** Self-[In]Correct's replication of Madaan et al. is §5.3, in results, under the heading "Do Prior Findings in Self-Refinement Contradict Self-[In]Correct?"
4. **Root-cause taxonomies backed by annotation.** Laban's four causes of getting lost are named in §6.2 and detailed in Appendix F.
5. **Per-experiment interpretation.** Tyen puts a "Discussion" subsection directly under each results section, so the interpretation sits with the numbers it interprets.

**Moves to discussion.**

1. **What the finding implies for how the field should run experiments.** Huang: inference-cost baselines, equal prompt-design effort. Kamoi: analyse feedback quality, not only downstream performance.
2. **What the finding implies for what should be built.** Shankar: "Future system designs should support these requirements."
3. **Scope conditions stated as a general rule rather than a result.** Laban §7.3 lists three task properties that predict the effect and closes with a testable prediction: "We hypothesize that LLMs tested on tasks with the aforementioned three properties will likely get lost in conversation."
4. **Connection to a literature outside the paper's own measurements.** Shankar reaching for grading rubrics in education and a 1964 obscenity opinion; Dang reaching for satisficing (Simon) and recognition-over-recall (Nielsen).
5. **New controlled experiments run to answer an objection.** Laban §7.1 and §7.2 each pose a challenge to the paper's premise as a direct question, run an experiment, and report a table. This is the only form in which the corpus lets a discussion carry new numbers.
6. **Methodological limits of the paradigm, not of this study.** Lee et al. §5.1–5.2 separate "General Challenges in Human Evaluation" and "General Challenges in Interactive Evaluation" from "5.3 Limitations Specific to Our Experiment Design."

**The operational test.** A sentence belongs in results if deleting the paper's own data would make it false. It belongs in discussion if deleting the data would make it unsupported but still meaningful. "62% of output tokens fall past the quality-optimal turn" fails without the data: results. "Revision robustness should be evaluated alongside first-turn capability" survives as a proposal: discussion.

---

## Verbatim catalogue: mechanism claims and their hedging

Grouped by hedge strength, weakest hedge last.

**Explicit hypothesis, flagged as such.**

> "We hypothesise that LLMs' inability to find mistakes is a main contributing factor to why LLMs are unable to self-correct reasoning errors. If LLMs are unable to identify mistakes, it should be no surprise that they are unable to self-correct either." — Tyen et al. 2311.08516 §3.1

> "We hypothesize this may be linked to Self-[In]Correct because if the overall ability of LLMs to discriminate is inferior to their ability to generate, it becomes challenging to engage in a virtuous cycle that simultaneously enhances the model's capability to follow instructions and generate self-rewards." — 2404.04298 §6. Note the doubled hedge: *hypothesize* + *may*.

> "We hypothesize that LLMs tested on tasks with the aforementioned three properties will likely get lost in conversation, evidenced by a large drop in averaged performance and reliability in Sharded simulations." — Laban et al. 2505.06120 §7.3. The hedge is paid for with a falsifiable prediction and three named conditions.

**"Suggests" plus a named alternative that the evidence rules out.**

> "Our results show that, with mistake location information available, LLMs can correct their own outputs and improve overall downstream performance. This suggests that the main bottleneck in self-correction methods is the identification of mistakes, rather than the correction process." — Tyen et al. §4.2. The mechanism claim is a *contrast*: X rather than Y, with an experiment separating them.

> "Interestingly, the nature of feedback, whether binary or detailed, did not have a pronounced impact on plan generation performance, suggesting that the core issue lies in the LLM's binary verification capabilities rather than the granularity of feedback." — 2310.08118 §6. Same shape: a null result licenses locating the mechanism elsewhere.

> "Our results suggest that self-repair is not a silver bullet for code generation, and that current models are held back by their inability to reliably produce accurate and useful feedback on why the code is wrong." — Olausson et al. 2306.09896 §6.

> "This suggests an alternative perspective on the self-refine pipeline, indicating that while an LLM may not strictly adhere to instruction-following in terms of quality improvements, it can still improve certain intrinsic text qualities, such as fluency and understandability." — Xu et al. 2402.11436 §4.3.

**Labelled as intuition, kept separate from the measurement.**

> "Intuitive Explanation. If the model is well-aligned and paired with a thoughtfully designed initial prompt, the initial response should already be optimal relative to the prompt and the specific decoding algorithm. Introducing feedback can be viewed as adding an additional prompt, potentially skewing the model towards generating a response that is tailored to this combined input. In an intrinsic self-correction setting, on the reasoning tasks, this supplementary prompt may not offer any extra advantage for answering the question. In fact, it might even bias the model away from producing an optimal response to the initial prompt, resulting in a performance drop." — Huang et al. 2310.01798 §3.3. Four hedges in five sentences (*can be viewed as*, *potentially*, *may not*, *might*), and the paragraph carries a heading that tells the reader it is not evidence.

**Enumerated candidate mechanisms, none selected.**

> "We discuss possible reasons: First, participants might satisfice (Simon, 1996), that is, accept a 'good enough' suggestion rather than trying to 'optimize' it via instructions. ... Second, a known usability principle is recognition over recall (Nielsen, 1994): Users might find it easier to recognize a presented suggestion as suitable (or not), compared to coming up with an instruction and typing it in. Third, convenience might lead participants in the study to accept suggestions without instructions to get through the tasks quickly." — Dang et al. 2303.03199 §9.1. Three candidates, each attached to a named prior construct, none asserted; the paragraph then reports the one comparison that argues against the third.

**Weakly hedged, and paid for by a measurement in the same paper.**

> "Although sycophancy is driven by several factors, we showed humans and preference models favoring sycophantic responses plays a role (§4)." — Sharma et al. 2310.13548 §6. This is the corpus's strongest training-process mechanism claim and it is still hedged twice ("several factors", "plays a role"), with a section reference to the experiment that supports it.

> "The primary reason for this is that false answer options in CommonSenseQA often appear somewhat relevant to the question, and using the self-correction prompt might bias the model to choose another option, leading to a high 'correct ⇒ incorrect' ratio." — Huang et al. §3.3.

> "This may be because GPT-4 and GPT-4-Turbo have higher confidence in their initial answers, or because they are more robust and thus less prone to being biased by the self-correction prompt." — Huang et al. §3.3. Two mechanisms offered as alternatives, neither chosen.

> "This is mainly attributed to a decline in quality performance post-paraphrasing, with LLMs erroneously perceiving these paraphrased outputs as indicative of improvements." — Xu et al. 2402.11436 §4.3.

**Speculation about a training regime, and how it is marked.**

> "Particularly, as chat interfaces have grown significantly in popularity, this dominance has prompted adaptations that prioritize interactive aspects, resulting in a more aligned optimization goal than before. Consequently, we speculate that the gap between non-interactive and interactive performance might have been partially bridged due to these adaptations." — Lee et al. 2212.09746 §5.3. When the claim is about how models were trained and the authors did not train them, the verb is **speculate**, and the sentence sits under "Limitations Specific to Our Experiment Design."

**The pattern.** Not one paper in the sample asserts a training-process origin for a behaviour without either (a) an experiment on preference data or preference models in the same paper (Sharma), or (b) an explicit speculation marker (Lee). Mechanism strength in this literature is a function of what the paper measured, not of how plausible the story is.

---

## Verbatim catalogue: implication sentences that are not advice

### Addressed to researchers (17 papers)

> "Regarding this, we encourage future work proposing new self-correction methods to always include an in-depth inference cost analysis to substantiate claims of performance improvement. Moreover, strong baselines that leverage multiple model responses, like self-consistency, should be used for comparison." — Huang et al. 2310.01798 §6

> "Broadly speaking, equal effort should be invested in designing the prompts for initial response generation and for self-correction; otherwise, the results could be misleading." — Huang et al. §6

> "We recommend that self-correction research analyze the quality of generated feedback in more detail, not only evaluate the downstream performance of the refined responses." — Kamoi et al. 2406.01297 §7

> "Our work motivates the development of model oversight methods that go beyond using unaided, non-expert human ratings." — Sharma et al. 2310.13548 §6. Eighty-five words of conclusion and the implication is a single clause naming a class of method, not a procedure.

> "Further work is needed to elucidate the difference between cross-model evaluation and self-evaluation." — Tyen et al. 2311.08516 §3.1 (footnote)

> "Thus, we encourage the community to analyze trigger moments whenever studying UIs with explicit suggestion triggers." — Dang et al. 2303.03199 §9.2

> "Together, these findings motivate the HCI community to further explore the integration of choice and control via prompting. For example, future work could build on our conceptual lens to envision further UI designs that combine diegetic and non-diegetic prompting, and use our data as a benchmark in their evaluation." — Dang et al. §9.1

> "However, we emphasize that we need to do the evaluation with human users at least once to learn what the ground truth is and see which automatic metrics correlate with the real user evaluation." — Lee et al. 2212.09746 §5.1

> "If possible, we recommend recruiting a large number of diverse users to allow for more flexibility in selecting which models to evaluate and to alleviate concerns of sequential effects." — Lee et al. §5.2

> "Overall, especially given the rapid deployment of LMs, we recommend that future work should actively monitor how these interactions come to affect human language practices (e.g., writing, reading, listening, speaking), culture, well-being, and broader society." — Lee et al. §5.4

> "We urge HCI researchers to more precisely specify what potential errors and biases they identify in their use of LLMs, so that consumers of our research can better understand how the systems built upon these technologies may fail." — 2501.12557 §5.2.2

> "We encourage NLP practitioners to experiment with sharding and release sharded versions of their tasks and instructions alongside fully specified ones." — Laban et al. 2505.06120 §7.3

> "Advancing AI capabilities thus make measuring overreliance more essential, not less, to deploying AI for the benefit of all." — 2509.08010

> "Rather, it can be attributed, in part, to the absence of valid and appropriate methods for measuring overreliance in user-LLM interactions." — 2509.08010

### Addressed to system and interface designers (6 papers)

> "This suggests criteria refinement and grading should happen in tandem in interactive settings, and poses challenges to alignment methods that presume settled, expert labels." — Shankar et al. 2404.12272 §8.1

> "Future system designs should support these requirements. For instance, an evaluator assistant might adjust criteria dynamically as the user grades and gives feedback." — Shankar et al. §8.1

> "In short, relying on an agent-like framework to process information might be limiting, and we argue LLMs should natively support multi-turn interaction." — Laban et al. 2505.06120 §7.1

> "Following established AI interaction guidelines, a separate interface, such as a sidebar or secondary tab, could be deployed to facilitate supportive functions without interruptions on the ongoing conversation with ChatGPT." — 2402.06170 §6

> "Instead, we need more platforms that standardize the foundational elements of human subject studies with AI while maintaining scientific rigor, reducing technical overhead for researchers, and enabling broader participation in AI evaluation." — 2405.10632 §5.3

### Addressed to model builders (4 papers)

> "In this work, we call on LLM builders to prioritize reliability of the models they build, as our experiments demonstrate that the randomness involved in generating text with LLMs leads to catastrophic unreliability in all the models we tested, degrading the quality of responses the average LLM users see." — Laban et al. 2505.06120 §7.2

> "We invite and challenge LLM builders to jointly optimize model aptitude and reliability. A reliable LLM should: (1) achieve similar aptitude in single- and multi-turn settings, (2) have small unreliability (U₁₀⁹⁰ < 15) in multi-turn settings, (3) achieve these at unmodified temperature (T = 1.0), demonstrating that the underlying language model can handle variations that naturally occur in language generation." — Laban et al. §7.2. The recommendation is a numbered specification with a threshold, not an exhortation.

> "This highlights the potential in future research into models that balance safety with controlled risk-taking, guided by writers' values." — 2309.12570 §7.1

> "First, based on our collected non-diegetic prompts these LLMs should be trained to understand a broader range of inputs. For instance, PEER is trained on the imperative-style but we found the keyword-style to be more common." — Dang et al. 2303.03199 §9.7

### Addressed to end users (1 paper, and how it is quarantined)

Laban §7.4 is the whole of the corpus's user-facing advice. Its four moves, in order:

1. **Name the audience in the heading.** "7.4 Implications for Users of Conversational Systems"
2. **Open by stating the fact, not the instruction.** "Users of LLM-based products should be aware of the lack of reliability of LLMs, particularly when used in multi-turn settings."
3. **Declare the count and the register before giving any.** "We make two practical recommendations that can help users of LLM-based systems get the most out of their exchanges."
4. **Attach each recommendation to the experiment that supports it.** "Since LLMs are ineffective at dealing with information dispersed across multiple turns, consolidating instruction requirements into a single instruction is an effective strategy to improve the model's aptitude and reliability (as shown by the Concat experiments)."
5. **Close by disowning the advice as a stopgap.** "These two recommendations remain cumbersome for users and can only offer patched solutions rather than a principled approach. Once future LLMs can more reliably handle multi-turn conversations, the need for such recommendations should be alleviated, allowing users to communicate underspecified instructions over multiple turns naturally with less risk of the model getting lost in conversation."

Steps 3 and 5 are what keep the section from reading as a tip sheet: the advice is bounded in number, sourced to a controlled comparison, and declared temporary.

### The grammatical difference between an implication and advice

Every implication sentence above shares one of three subjects, and none of them is the reader:

- **The finding is the subject:** "This suggests criteria refinement and grading should happen in tandem." / "Our work motivates the development of model oversight methods."
- **A named third-party audience is the subject:** "Future system designs should support these requirements." / "LLM builders should prioritize reliability."
- **The authors are the subject:** "We recommend that self-correction research analyze..." / "We encourage NLP practitioners to..."

Advice, by contrast, makes the reader the subject and the verb imperative: "withhold the request to revise until you can name what is wrong." That sentence form appears **zero times** in 23 discussion sections.

---

## Reconciling conflicting measurements (verbatim examples)

Five worked examples, four of which are directly transferable to an absolute-score-versus-pairwise-preference conflict.

**1. Decompose the aggregate into two components and say which one moved. (Laban §6.2, in results.)**

> "The sharded setting paints a different picture. Model aptitude degrades in a non-significant way between the full and sharded settings, with an average drop of 16%. On the other hand, unreliability skyrockets with an average increase of 112% (more than doubling). ... This refines our definition of the lost in conversation phenomenon: when comparing single- and multi-turn settings, we find that large performance degradations (P̄) are due in large part to increased model unreliability (U), rather than a loss in aptitude (A)."

The word to steal is **"refines."** Two measures pointing different ways is not a contradiction to be explained away; it is a finer statement of what the effect is.

**2. Name the dimension on which the two measures differ, and report both. (Xu et al. 2402.11436 §4.3, in results, under the heading "Self-refinement can improve fluency and understandability but not quality.")**

> "This raises a natural question: if an LLM does not improve its generation quality, does it improve in any other aspects throughout the iterative refine phase? To investigate this, we utilize the learned metric UniEval... Our results, illustrated in Figure 6, show that GPT-4, GPT-3.5-Turbo, and Gemini consistently exhibit improvements in both fluency and understandability. This suggests an alternative perspective on the self-refine pipeline, indicating that while an LLM may not strictly adhere to instruction-following in terms of quality improvements, it can still improve certain intrinsic text qualities, such as fluency and understandability."

The heading states the split as the finding. The conflict is converted into a two-part claim, and neither half is retracted.

**3. Show that the conflicting measure is being driven by an artefact, with the artefact enumerated. (Jiang et al. 2404.04298 §5.3, in results, under "Do Prior Findings in Self-Refinement Contradict Self-[In]Correct?")**

> "Both Huang et al. (2023) and Madaan et al. (2023) suggested LLMs can self-refine on tasks other than reasoning. Does this contradict our assertions? We replicated the experiment outlined in Madaan et al. (2023) and observed the following: (1) For some evaluated tasks, certain aspects can be exploited for artificially amplifying task performance without actually improving with the feedback. ... (2) For some evaluated tasks, the evaluation score assigned by the model for each iteration of self-refine is not monotonically increasing. ... This suggests that the observed improvement may be due to lower initial output quality, as noted in Huang et al. (2023). (3) Quantifying the percentage of times models prefer self-refined subsequent generations to the previous generation, a marginal preference for self-refined generation was observed. ... Our results in Table 5 indicate that models prefer self-refined generations only around 54% of the time."

Note item (3): a preference measure that lands at 54% is reported as **54%, described as "marginal," and used as evidence** rather than discarded as a null. It is not framed as a failure to clear a bar.

**4. State the scope condition under which the effect reverses, with the arithmetic. (Tyen et al. §4.2.)**

> "While our numbers do show that our gains are higher than our losses, it should be noted that changes in the overall accuracy depends on the original accuracy achieved on the task. For example, if the original accuracy on the tracking shuffled objects task was 50%, the new accuracy would be 68.6%. On the other hand, if the accuracy was 99%, the new accuracy would drop to 92.8%."

A conflicting reading is pre-empted by naming the parameter that flips the sign and computing both ends.

**5. Report the task on which your own effect does not appear, and use it to bound the claim. (Laban §7.3.)**

> "Both models we tested – GPT-4o-mini and GPT-4o – do not exhibit degradation in performance in the Sharded setting, with BLEU scores being within 10% difference of each other in all settings. We believe this result reflects that the task can largely be accomplished at the sentence-level ... and that the BLEU score does not adequately capture document-level nuances. In other words, if a task is episodic (i.e., it can be decomposed into turn-level subtasks), the models can avoid getting lost in conversation."

The null is not a limitation. It is the boundary of the construct, and it is stated as such.

**What none of the five does.** None calls its own measures contradictory. None resolves the conflict by declaring one measure the real one and the other an artefact of measurement without evidence for the artefact. None puts the conflict in a limitations list.

---

## Rules (numbered, checkable, each with evidence)

1. **Address researchers first, and make researchers the primary audience.** 17 of 23 discussions state implications for researchers; 1 of 23 states any for end users. Evidence: the audience column of the corpus table. *Check: does the first subsection of the discussion tell a researcher what to do differently, or tell a chatbot user what to type?*

2. **If practical advice for users is included, segment it into its own named subsection, cap it at two or three items, source each to a controlled comparison in this paper, and close by calling it a stopgap.** Evidence: Laban §7.4, the only user-facing implications section in the sample, does all four (see the five-move breakdown above). *Check: can each recommendation be traced to a table in this paper, and does the subsection end by saying the recommendation should become unnecessary?*

3. **Never make the reader the grammatical subject of a directive.** Zero of 23 discussions address an end user as "you." The one paper using "you" (2501.12557) addresses researchers, inside a numbered list explicitly framed as "prompts for reflection, not a checklist for completion." *Check: grep the section for "you", "your", and sentence-initial bare verbs.*

4. **Never open or close on an imperative.** Zero of 23 do either. The three imperatives in the sample are one mid-paragraph "Consider..." in each of two papers and two deep subsection headings in Laban. *Check: first heading and last sentence.*

5. **Headings name an object, an audience, a claim, or a question. Never a slogan.** Evidence: the full verbatim heading collection above; "Choice vs. Control", "Operationalizing Assertions", "Implications for LLM Builders", "Proprietary LLMs raise reproducibility concerns", "Do current AI safety guardrails prevent writers from exploring more complex and darker topics?". *Check: could this heading be printed on a mug?*

6. **Put the mechanism where the measurement is.** Huang's causal account is §3.3 of results; his discussion contains none. Laban's decomposition and root causes are §6.2 and Appendix F. Tyen puts a Discussion subsection under each results section. *Check: is the mechanism paragraph adjacent to the numbers that constrain it?*

7. **Hedge a mechanism in proportion to what was measured.** A mechanism supported by an experiment in this paper gets "plays a role" (Sharma). One supported by a contrast between two of the paper's conditions gets "suggests ... rather than" (Tyen, 2310.08118). One supported by nothing gets "We hypothesise" or a heading reading "Intuitive Explanation" (Huang). One about a training regime the authors did not run gets "we speculate" (Lee et al. §5.3). *Check: for each mechanism sentence, name the table that constrains it. If there is none, the verb is hypothesise or speculate.*

8. **A claim about RLHF or preference training requires either an experiment on preference data or an explicit hypothesis marker plus a citation.** Sharma et al. 2310.13548 is the paper in this literature that measured it, over four experiments, and still wrote "plays a role." *Check: is there a citation, and is the verb honest about the absence of a measurement?*

9. **State a mechanism as a contrast, not as an assertion.** The strongest-reading mechanism sentences in the corpus all take the form *X rather than Y*: "the main bottleneck ... is the identification of mistakes, rather than the correction process" (Tyen); "the core issue lies in the LLM's binary verification capabilities rather than the granularity of feedback" (2310.08118); "due in large part to increased model unreliability, rather than a loss in aptitude" (Laban). *Check: does each mechanism sentence name the alternative it displaces?*

10. **When two of your own measures point different ways, decompose rather than adjudicate.** Evidence: the five worked examples above. The permitted moves are: split the aggregate into components (Laban), name the dimension on which the measures differ and keep both (Xu), demonstrate the artefact driving one of them (Chen §5.3), state the parameter that flips the sign (Tyen), or use the null to bound the construct (Laban §7.3). *Check: does the reconciliation appear in the body as a finding, rather than in a limitations list as a concession?*

11. **A near-chance preference result is a number, not a failure.** Jiang et al. report "models prefer self-refined generations only around 54% of the time" as substantive evidence. *Check: is the pairwise result reported in results with its interval, and interpreted, rather than confessed in limitations?*

12. **Give each implication a named audience in the sentence, or in a heading above it.** "we call on LLM builders", "we encourage NLP practitioners", "Future system designs should", "we urge HCI researchers". *Check: for every "should" in the section, who is the subject?*

13. **A recommendation to builders is a specification, not an exhortation.** Laban's is three numbered criteria with a numeric threshold and a temperature condition. *Check: could a reader tell whether a system met the recommendation?*

14. **New experiments are allowed in the discussion only when they answer a stated objection.** Laban §7.1 and §7.2 each pose the objection as a direct question ("do we need native multi-turn support in LLMs when an agent framework can orchestrate interactions...?"; "does setting the temperature to its lowest setting effectively resolve the reliability concern...?"), run the experiment, and report a table. *Check: is the new number attached to a question the reader would actually ask?*

15. **Open a standalone discussion with a one-to-three-sentence roadmap.** Six of the eight standalone discussions do. *Check: does sentence one say what the subsections will do?*

16. **Length: 600 to 1,800 words, 8 to 20 percent of body.** Corpus median 575 words and 7.9%; HCI median 838. Above 2,000 words only in HCI papers with eleven or more subsections. *Check: word count.*

17. **Future work is dispersed as clauses inside substantive paragraphs, not collected into a list.** Only three papers give it its own heading, and two of those are subsections. *Check: is there a paragraph whose only content is a list of things not done?*

18. **Limitations specific to this study are separated from limitations of the paradigm.** Lee et al. split §5.1–5.2 (challenges in human and interactive evaluation generally) from §5.3 (limitations specific to our experiment design). *Check: would each limitation apply to the next paper that runs this design?*

19. **Cite the closest prior work when reconciling, and reconcile explicitly rather than by omission.** Tyen: "Our findings are in line with and builds upon results from Huang et al. (2023)... In our experiments, we specifically target the models' mistake finding ability and provide results for additional tasks." *Check: does the discussion name the paper a reader will think of, and say how this differs?*

20. **Every number in the discussion has a referent, a unit, and a comparison.** Laban: "an average drop of 16%" against "an average increase of 112%"; Tyen: "68.6%" against "92.8%" with the base rates that produce each. *Check: for each number, 16% of what, compared with what?*

---

## Constructions to avoid, with evidence

**Imperative or slogan headings.** Not one appears in 23 sections outside Laban's two deepest user-facing headings. "Evaluate, then direct." has no analogue anywhere in the corpus.

**Second-person address to a user.** Zero of 23 in author prose. The three papers whose discussions contain "you" all have it inside quotation marks.

**A mechanism asserted about model training with no citation and no hypothesis marker.** The corpus norm is Sharma's four experiments plus "plays a role", or Lee's "we speculate". Nothing in the sample asserts a training origin flatly.

**Advice stacked without a bound.** Laban states the count in advance ("We make two practical recommendations") and disowns them at the end. A discussion that issues advice item after item without a count or a closing bound has no model in this literature.

**Market and industry claims used as evidence.** No paper in the sample argues from spending trends, pricing, or vendor issue trackers in its discussion. The closest thing is Laban's single footnote to a Reddit thread, used to report that "there is anecdotal evidence that early adopters ... are aware" of the phenomenon, explicitly labelled anecdotal and placed after the experimental evidence, not in place of it.

**A conflict between two of the paper's own measures confessed in the limitations list.** No paper does this. All five reconciliation examples put the conflict in the body.

**Pre-emptive objection-and-rebuttal.** One paper does it: Shankar et al. §8.1 opens a paragraph "The reader might wonder when criteria 'settle.'" This is a minority construction (1 of 23) and it runs against this project's own writing rules on pre-emptive defensiveness; the corpus-supported alternative is Laban's, where the objection is posed as a research question and answered with an experiment rather than with an argument.

**"In this section, we..." beyond one sentence.** Roadmaps in the corpus are one to three sentences. 2501.12557's is three and it is the longest.

---

## Checklist

Before the discussion is done, all of the following must be true.

- [ ] The section addresses researchers in its first subsection.
- [ ] Every "should" in the section has a named subject that is not the reader.
- [ ] The section contains no instance of "you" or "your" outside quotation marks.
- [ ] The first heading is not an imperative and not a slogan.
- [ ] The last sentence is not an imperative.
- [ ] Every heading names an object, an audience, a claim, or a question.
- [ ] Every mechanism sentence names the table or section that constrains it, or carries "hypothesise"/"speculate".
- [ ] Every mechanism sentence names the alternative it displaces.
- [ ] Any claim about RLHF or preference training carries a citation.
- [ ] The absolute-score and pairwise results are reconciled in the body as a decomposition, not in limitations as a concession.
- [ ] The near-chance pairwise number is reported with its interval and interpreted.
- [ ] User-facing advice, if present, sits in its own named subsection, is capped and counted, is sourced to a controlled comparison, and is closed as a stopgap.
- [ ] No number appears without a referent and a comparison.
- [ ] Length is 600–1,800 words and 8–20% of body.
- [ ] Future work is not a standalone list.
- [ ] No argument rests on pricing, spending trends, or issue trackers.

---

## How this paper's current discussion measures up

Read: `paper/sections/discussion.tex` (727 words before the Limitations section, plus 235 words of Limitations). Body total across the six included section files is roughly 7,100 words, so the discussion is 10.2% of the paper. **Length and share are fine and sit near the corpus median.** Three run-in bold paragraph headings with no subsections matches Huang (2310.01798) and 2402.06170. **The structure is defensible; the register is not.**

### Where it slips into advice

**1. The opening heading is an imperative slogan.** `\paragraph{Evaluate, then direct.}` Zero of 23 discussions open with an imperative. Zero contain a heading of this form anywhere. This one heading does more to make the section read as a tip sheet than any sentence in it, because it is the first thing a reader sees. The corpus-supported replacement is a heading naming the object: what the paper has is a contrast between undirected and directed revision, so the heading is that contrast, on the model of "Choice vs. Control" (Dang §9.1) or "Aptitude vs. Reliability".

**2. Second-person address to an end user.** "For users, the rule is to withhold the request to revise until you can name what is wrong." This is the only sentence in the section that makes the reader the subject, and it is the sentence the advisor's criticism is about. Nothing comparable exists in 23 sections. Note also "the rule is to": stating a rule for a user is the definitional form of a tip sheet.

**3. The user advice is not segmented, not counted, not sourced, and not bounded.** Laban's four protections are all absent. The advice sits in the same paragraph as a training-process mechanism claim and an architectural recommendation, so a reader cannot tell which audience any given sentence is for. If this advice stays, it needs its own paragraph, an explicit count, a pointer to the targeted-feedback comparison in Results §5.3, and a closing sentence saying the recommendation should become unnecessary.

**4. The RLHF mechanism is the weakest-supported and most strongly-stated claim in the section.** "This has a likely origin in how models are trained: reinforcement from human feedback rewards visible effort, and a model that revises when asked is rated more favorably than one that correctly declines, regardless of whether the revision helped. Over enough such examples, the model learns that the safe response to a revision request is to revise." Three sentences, one hedge ("likely"), zero citations, and no experiment in this paper touches preference data. Sharma et al. 2310.13548 measured exactly this claim across four experiments and wrote "Although sycophancy is driven by several factors, we showed humans and preference models favoring sycophantic responses plays a role." That paper is the citation this passage needs, and its hedging is the model. As written, the passage is also the section's clearest violation of the project's academic-integrity rule against presenting inference as established fact.

**5. The second paragraph argues from costs rather than from measurements.** "Enterprise inference spending is climbing steeply" is uncited. The VSCode and Claude Code issue-tracker references are used as the evidentiary close of the paragraph. No paper in the sample builds a discussion paragraph on spending trends or issue trackers; Laban's one anecdotal citation is explicitly labelled anecdotal and placed after the experiments. The paragraph's own strongest content is already there and is measured: the quality-optimal stopping point is turn one for every model, and 62% of output tokens fall past it. The corpus move is to lead with that and let the reader draw the billing conclusion. The heading, "The cost of undirected revision is real and mostly hidden," also states a verdict rather than naming a subject.

**6. Missing: the tension the paper actually has.** The absolute quality scoring says quality falls substantially; the blind human pairwise comparison of first versus last version is near chance. Grep of `paper/sections/results_v2.tex` finds no mention of the pairwise comparison at all. Its only appearance in the manuscript is Limitation Eight, framed as a failure: "our reversibility result is near chance ... with a confidence interval that includes 50%, and a pre-set success bar of 65% that was not cleared, so we do not claim humans can reliably distinguish first from revised drafts." Every one of the five reconciliation examples in the corpus does the opposite. Jiang et al. report a 54% preference **as evidence**. Xu et al. turn "quality does not improve but fluency does" into the heading of a results subsection. Laban turns a divergence between two measures into "This refines our definition." The transferable move here: the two measures are not in conflict, they are measuring different things, and naming which is the finding. An absolute rubric scores the artefact against a standard; a blind pairwise asks whether a reader without the rubric can tell. That the second is near chance while the first shows a substantial drop is the paper's own version of Laban's aptitude/unreliability split, and it belongs in Results with an interval, not in a limitations list with an unmet bar.

**7. What is already right.** The third paragraph, on revision robustness, is the section's strongest and is in register throughout: it names a construct, argues that current benchmarks do not measure it, gives the reason the two properties come apart, and closes with a researcher-addressed recommendation, "controlling for it should be standard practice." That closing sentence is not an imperative and is addressed to researchers, the audience 17 of 23 discussions in the sample speak to. On the evidence of the corpus, this paragraph should lead the section rather than close it, and the section's centre of gravity should move to it.

**8. Ordering.** The corpus norm is implications ordered by audience with researchers first (Laban is the explicit case; 17 of 23 address researchers at all). Current order is users → cost → researchers. Reversed, with the user advice compressed into a bounded, sourced, self-disowning close on Laban's model, the same content stops reading as a tip sheet without losing anything the paper measured.
