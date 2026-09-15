# Rules: Related Work

Retrieved 2026-09-02. 22 sections read in full.

All 22 were read as running text from arXiv HTML (`arxiv.org/html/<ID>v1`, falling back to
`ar5iv.labs.arxiv.org/html/<ID>`), not from abstracts or memory. Word counts, citation counts,
cluster sizes and citation-macro ratios below were computed mechanically from the rendered HTML
(`<cite>` elements and their `ltx_citemacro_*` classes), not estimated. Every count names the
papers behind it.

**What could not be accessed.** Two papers in the target literature could not be read because
they are not on arXiv and sit behind the ACM Digital Library: Zamfirescu-Pereira et al., "Why
Johnny Can't Prompt" (CHI 2023) and the CHI-only venue material cited inside Buçinca and
Vasconcelos. Their related-work sections are therefore absent from these counts. Where an arXiv
v1 differs from a camera-ready, the counts describe the v1 HTML, which is what was read. Venue
labels are not asserted below, because venue metadata was not fetched; the ID and the title are
what was verified.

---

## Corpus

Placement is measured against the paper's own method/experiment section. "Before method" means
the section is numbered ahead of the first section that describes what the authors did; "late"
means it sits after the experiments or results.

| Paper (first author, short title) | arXiv ID | Section, placement | Words | Cite elements / works cited | Organisation type |
|---|---|---|---|---|---|
| Madaan, *Self-Refine* | 2303.17651 | §2 of 7, before method | 867 | 38 / 64 | thematic, 4 run-in headings |
| Huang, *LLMs Cannot Self-Correct Reasoning Yet* | 2310.01798 | §2 of 7, before method | 517 | 7 / 14 | narrative, unheaded, conceptual-chronological |
| Kamoi, *When Can LLMs Actually Correct Their Own Mistakes?* | 2406.01297 | §10 of 11, late | 303 | 13 / 29 | thematic, 3 run-in headings |
| Pan, *Automatically Correcting LLMs* (survey) | 2308.03188 | no related-work section; §1 intro does the work | 760 | 24 / 53 | survey funnel in the introduction |
| Tyen, *LLMs cannot find reasoning errors* | 2311.08516 | §5 of 6, late | 268 | 9 / 9 | thematic, 2 run-in headings |
| Stechly, *GPT-4 Doesn't Know It's Wrong* | 2310.12397 | §2 of 5, before method | 193 | 7 / 10 | one narrative paragraph |
| Laban, *LLMs Get Lost In Multi-Turn Conversation* | 2505.06120 | §2 of 9, before method, plus Appendix A (453 w) | 812 | 20 / 41 | narrative, 6 unheaded paragraphs |
| Sharma, *Towards Understanding Sycophancy* | 2310.13548 | §5 of 8, late, plus §2 Background (252 w) before method | 347 | 15 / 22 | thematic, 3 bold run-in headings |
| Zheng, *Judging LLM-as-a-judge* (MT-Bench) | 2306.05685 | no related-work section anywhere; §2.1 Motivation does the work | 517 | 14 / 18 | prior work sorted into three benchmark categories |
| Bansal, *Does the Whole Exceed its Parts?* | 2006.14779 | §2 of 6, before method | 1066 | 26 / 40 | narrative, unheaded |
| Buçinca, *To Trust or to Think* | 2102.09692 | §2 of 8, before method | 1226 | 23 / 40 | thematic, 2 numbered subsections |
| Vasconcelos, *Explanations Can Reduce Overreliance* | 2212.06823 | §2 of 12, before method | 1212 | 27 / 50 | unheaded lead plus 2 numbered subsections |
| Lee, *CoAuthor* | 2201.06796 | §2 of 7, before method | 1727 | 38 / 62 | thematic, 4 numbered subsections, 5 nested |
| Mozannar, *Reading Between the Lines* | 2210.14306 | §2 of 8, before method | 710 | 14 / 17 | narrative, unheaded |
| Shankar, *Who Validates the Validators?* | 2404.12272 | §2 of 9, before method | 1365 | 28 / 36 | thematic, 3 bold run-in headings |
| Bai, *MT-Bench-101* | 2402.14762 | §2 of 6, before method | 418 | 23 / 31 | thematic, 3 run-in headings |
| Kwan, *MT-Eval* | 2401.16745 | §2 of 6, before method | 236 | 6 / 8 | one narrative paragraph |
| Wang, *MINT* | 2309.10691 | §4 of 5, late | 509 | 18 / 39 | thematic, 2 numbered plus 2 run-in |
| Chen, *Teaching LLMs to Self-Debug* | 2304.05128 | §6 of 7, late | 1155 | 32 / 82 | thematic, 5 run-in headings |
| Xu, *The Earth is Flat because…* | 2312.09085 | §7 of 8, late | 697 | 20 / 36 | thematic, 4 bold run-in headings |
| Sharma, *Generative Echo Chamber?* | 2402.05880 | §2 of 8, before method | 1536 | 39 / 66 | thematic, 3 numbered subsections |
| Wu, *AI Chains* | 2110.01691 | §2 of 8, before method | 1255 | 30 / 43 | thematic, 3 numbered subsections |

**Totals.** 17,696 words, 471 citation elements, 810 cited works. Mean 804 words and 36.8 works
per section.

---

## Organisation patterns, with counts

### Placement: 14 before the method, 6 late, 2 with no such section

- **Before the method (14):** Madaan, Huang, Stechly, Laban, Bansal, Buçinca, Vasconcelos, Lee,
  Mozannar, Shankar, Bai, Kwan, Sharma (echo chamber), Wu.
- **Late, after the experiments or results (6):** Kamoi §10 of 11, Tyen §5 of 6, Sharma
  (sycophancy) §5 of 8, Wang §4 of 5, Chen §6 of 7, Xu §7 of 8.
- **No related-work section at all (2):** Pan (a survey; the introduction funnels the literature
  and states the paper's plan) and Zheng (MT-Bench; the string "related work" does not appear
  anywhere in 2306.05685v1, and §2.1 "Motivation" sorts prior benchmarks into three categories
  instead).

Two patterns fall out of the split. Every one of the eight human-computer-interaction papers
places the section before the method. And four of the six late placements (Kamoi, Sharma
sycophancy, Chen, Xu) split the literature in two: a short **Background** section before the
method that defines the terms the paper needs, and a **Related Work** section late that positions
the finished result. Sharma is the clearest instance: §2 "Background: AI Assistants and
Sycophancy" runs 252 words and defines RLHF and the term sycophancy; §5 "Related Work" runs 347
words and says what the paper adds. Laban does the reverse split, keeping the directly competing
literature in §2 (812 words) and moving a second literature to Appendix A (453 words), announced
in one sentence: "The Background (Section 2) reviews the most directly related prior work,
focused on multi-turn evaluation. We now cover other related prior works that have studied
underspecification."

### Length: NLP-venue sections run half the length of HCI-venue ones

- **NLP/ML papers (14):** Madaan 867, Huang 517, Kamoi 303, Pan 760, Tyen 268, Stechly 193,
  Laban 812, Sharma-sycophancy 347, Zheng 517, Bai 418, Kwan 236, Wang 509, Chen 1155, Xu 697.
  Mean **543 words**, median around 500.
- **HCI papers (8):** Bansal 1066, Buçinca 1226, Vasconcelos 1212, Lee 1727, Mozannar 710,
  Shankar 1365, Sharma-echo 1536, Wu 1255. Mean **1262 words**.

The longest NLP section in the corpus is Chen's 1155 words, and it is placed late, where it does
not spend introduction space. The four shortest sections in the whole corpus are all NLP and all
under 310 words: Stechly 193, Kwan 236, Tyen 268, Kamoi 303.

### Organisation type: 15 thematic, 6 narrative, 1 survey taxonomy

- **Thematic clusters with explicit headings (15):** Madaan, Kamoi, Tyen, Sharma-sycophancy,
  Zheng, Buçinca, Vasconcelos, Lee, Shankar, Bai, Wang, Chen, Xu, Sharma-echo, Wu.
- **Continuous narrative with no headings (6):** Huang, Stechly, Laban, Bansal, Mozannar, Kwan.
- **Survey taxonomy by method family (1):** Pan.

Nothing in the corpus is organised chronologically as its top-level principle. Huang is the
nearest, moving from backpropagation through reinforcement learning to RLHF to inference-time
correction, but it is doing conceptual work (narrowing to a definition), not recounting a
timeline.

**Heading form splits by community.** Of the 15 thematic sections, 8 use unnumbered bold run-in
headings, the LaTeX `\paragraph` form (Madaan, Kamoi, Tyen, Sharma-sycophancy, Shankar, Bai,
Chen, Xu), and 7 use numbered subsections (Zheng, Buçinca, Vasconcelos, Lee, Wang, Sharma-echo,
Wu). All eight run-in users are NLP/ML papers; six of the seven numbered users are HCI papers.

### Verbatim subsection headings

Run-in `\paragraph` style, NLP papers:

- Madaan (2303.17651): `Source of feedback` | `Representation of the feedback` |
  `Utilization of feedback` | `Iterative refinement`
- Kamoi (2406.01297), §10: `Self-Detection` | `Editing Human-Written Text` | `Self-Training`
- Tyen (2311.08516): `Datasets` | `Self-correction`
- Sharma sycophancy (2310.13548): `Challenges of Learning from Human Feedback` |
  `Understanding and Demonstrating Sycophancy` | `Preventing Sycophancy`
- Shankar (2404.12272): `Automating Evaluations of Prompts.` |
  `Over-trust and Over-generalization of LLM Behavior.` | `Approaches to Aligning LLMs.`
- Bai (2402.14762): `LLMs for Multi-turn Dialogues` | `Benchmarks for Multi-turn LLMs` |
  `Benchmarks for Fine-grained Abilities`
- Chen (2304.05128): `Language models for code.` | `Prompting techniques.` | `Code repair.` |
  `Training with feedback.` | `Prompting with feedback.`
- Xu (2312.09085): `LLM's Factuality and Hallucination.` | `Knowledge Conflicts in LLM.` |
  `NLP under Input Perturbations, Biases, and Sycophancy.` | `Interactive Testing of LLMs.`
- Wang (2309.10691): `4.1 LLM in Interaction` with run-ins `Interact with Users.` and
  `Interact with Tools.`, then `4.2 Evaluating Interactions`

Numbered style, HCI papers:

- Buçinca (2102.09692): `2.1. Cognitive forcing functions and strategies` |
  `2.2. Overreliance in AI-assisted decision-making`
- Vasconcelos (2212.06823): unheaded lead, then `2.1. Cognitive biases in decision-making` |
  `2.2. Decision-making in behavioral economics`
- Lee (2201.06796): `2.1. Understanding Technological Capabilities` (`2.1.1. Types of
  Understanding`, `2.1.2. Ways to Develop Understandings`) | `2.2. Understanding Language
  Models' Generative Capabilities` (`2.2.1. Language Models' Generative Capabilities`,
  `2.2.2. Challenges in Understanding Generative Capabilities`, `2.2.3. Limitations of
  Traditional Methods`) | `2.3. Datasets in HCI` | `2.4. Datasets in NLP`
- Sharma echo chamber (2402.05880): `2.1. Selective Exposure, Confirmation Bias, and Echo
  Chamber Effect` | `2.2. Human-LM Interaction` | `2.3. Conversational Search`
- Wu (2110.01691): `2.1. Large Language Models` | `2.2. Human-AI Collaboration` |
  `2.3. Workflows in Crowdsourcing`
- Zheng (2306.05685), §2.1: the three category labels are run-in inside the prose,
  `Core-knowledge benchmarks`, `Instruction-following benchmarks`, `Conversational benchmarks`.

Every heading in this list names either a research topic or a research object. Not one is a
rhetorical phrase, a question, or a claim.

### How many clusters, and how many works per cluster

Across the 15 thematic sections the number of top-level headings is 2, 2, 2, 2, 3, 3, 3, 3, 3,
3, 4, 4, 4, 5 and 4 (Lee, counting top level only). **Median 3, mean 3.1, maximum 5** (Chen).
Nothing in the corpus has more than five top-level clusters.

Works per cluster, computed as cited works divided by top-level headings:

- Sharma echo chamber 66/3 = 22.0
- Chen 82/5 = 16.4
- Lee 62/4 = 15.5
- Madaan 64/4 = 16.0
- Wu 43/3 = 14.3
- Shankar 36/3 = 12.0
- Bai 31/3 = 10.3
- Kamoi 29/3 = 9.7
- Xu 36/4 = 9.0
- Buçinca 40/2 = 20.0
- Vasconcelos 50/2 = 25.0
- Wang 39/2 = 19.5
- Sharma sycophancy 22/3 = 7.3
- Zheng 18/3 = 6.0
- Tyen 9/2 = 4.5

Median around 14 works per cluster. The two thinnest, Tyen at 4.5 and Zheng at 6.0, are both
sections that are deliberately minimal and both sit in papers whose contribution is a dataset.

### Citation clusters inside the text

Of the 471 citation elements across the corpus, **304 (64.5 percent) name one work** and
**167 (35.5 percent) group two or more**. Mean works per citation element is 1.72. The largest
single clusters observed: 8 works (Chen), 7 works (Laban, Bansal, Buçinca, Vasconcelos, Wang).
Papers whose citation elements are densest: Chen 2.56 works per element, Kamoi 2.23, Pan 2.21,
Wang 2.17, Laban 2.05. Sparsest: Tyen 1.00 (every citation names exactly one work), Mozannar
1.21, Zheng 1.29, Shankar 1.29.

The "sea of blue" is therefore a minority form even in the densest sections. The usual sentence
names one work; the four-to-seven-work bracket appears when a claim is about the field rather
than about a result, for example Wang's list of seven tool-use papers or Buçinca's list of seven
trust-calibration studies.

### Where disagreement in the literature is represented

Six of the 22 sections stage a live disagreement rather than reporting a settled consensus.
Verbatim:

- **Stechly (2310.12397).** "The conclusions have also been divergent–with some studies
  highlighting the limitations of LLMs in reasoning [12, 2], and others arguing that iterative
  prompting of LLMs can improve their ability to reason."
- **Mozannar (2210.14306).** "This wide dispersion of results raises interesting questions about
  the nature of the utility afforded by neural code completion engines: how, and when, are such
  systems most helpful; and conversely, when do they add additional overhead? This is the central
  question to our work."
- **Vasconcelos (2212.06823).** "Therefore, among studies that report that performance improves
  when an AI gives explanations (Lai and Tan, 2019b; Lai et al., 2020; Buçinca et al., 2020;
  Horne et al., 2019), it is unclear whether explanations truly improve understanding of model
  capabilities, or if they instead serve as a signal for blind trust in a AI that is more accurate
  than the human baseline."
- **Bansal (2006.14779).** "At least two potential causes account for the absence of complementary
  performance in these cases. First, task design may have hindered collaboration… Second, even
  when the task has the potential for complementary performance, it is unclear if the
  collaboration mechanisms under study supported it."
- **Sharma echo chamber (2402.05880).** "However, others challenged these concerns, suggesting
  that the actual selective exposure is less prevalent than theorized (Guess et al., 2018), and
  that there are individuals who actively seek diverse perspectives…"
- **Madaan (2303.17651).** "So far, machine-generated feedback from prompting has yet to be found
  to be beneficial (Saunders et al., 2022a; Bai et al., 2022b). However, in this work provides
  evidence that feedback generated with zero- or few-shots can be helpful."

The shared move: name both sides in one sentence, attach citations to each side, and then say
either what the paper does about the disagreement (Stechly, Mozannar, Bansal) or which side its
own evidence falls on (Madaan). None of the six adjudicates the disagreement in the related-work
section itself, and none characterises either side as mistaken.

Two further instances report a prior result **including its own negative finding**, without
editorial comment, which is the additive way to present a result that limits a competitor:

- **Vasconcelos on Buçinca.** "The authors find that forcing functions successfully reduce
  overreliance on incorrect model predictions. However, they also reduce reliance on correct model
  predictions, yielding no significant differences when humans are not aided by an AI. The authors
  also identified an interesting trade-off: participants performed best in the conditions they
  preferred and trusted the least."
- **Tyen on Reflexion and RCI.** "Previous post-hoc correction methods that are applied to
  reasoning errors include Reflexion (Shinn et al., 2023) and RCI (Kim et al., 2023), both of
  which cause performance deterioration when the oracle label is not used (Huang et al., 2023)."

### Whether the section ends with an explicit "in contrast, we"

Of the 20 sections with a genuine closing paragraph (excluding Pan and Zheng, which have no such
section), **13 end on a self-positioning sentence and 7 do not**.

End on self-positioning: Madaan, Huang, Bansal, Vasconcelos, Lee, Mozannar, Shankar, Kwan, Wang,
Chen, Xu, Sharma-echo, Wu.
Do not: Kamoi, Tyen, Sharma-sycophancy, Bai, Buçinca, Laban, Stechly.

Only three end on a sentence built with an explicit contrastive connective:

- Madaan: "In contrast, our Self-Refine approach includes a scalar value-based stopping criteria
  that overcomes this issue."
- Kwan: "In contrast, our work evaluates LLM's comprehensive ability to conduct multi-turn
  conversations, possibly involving multiple types of dialogue in one session."
- Wang: "Different from prior work, MINT covers a range of diverse tasks and is designed to
  measure the multi-turn interaction capabilities of LLMs with both tools and users that are more
  aligned with real-world applications."

**None of the 22 sections has a standalone final "in contrast, we" paragraph.** The dominant form
is distributed: positioning is attached to the end of each cluster, one or two sentences at a
time. Counting paragraphs that contain a first-person positioning sentence against total
paragraphs: Tyen 3/3, Sharma-sycophancy 3/3, Xu 5/6, Wu 5/6, Madaan 4/5, Laban 4/6, Chen 4/7,
Mozannar 3/5, Sharma-echo 4/9, Lee 6/15, Vasconcelos 3/7, Shankar 3/7, Bansal 2/6, Buçinca 2/9.
Two sections carry no first-person positioning at all: Kamoi §10 and Bai.

---

## Verbatim catalogue of positioning sentences

Every sentence below was copied from the section named. This is the transferable material: each
one differentiates the paper from a named competitor without asserting that the competitor is
wrong.

### A. Complementary-question form (states what the prior work asks, then what this paper asks instead)

1. **Madaan, 2303.17651 §2.** "However, different from these works, our goal is not only to
   generate feedback from LLMs. Rather, we propose soliciting feedback from an LLM on its own
   output, refining the output with feedback, and repeating this feedback-refine process."
2. **Huang, 2310.01798 §2.** "Given that high-quality external feedback is often unavailable—and
   acknowledging its evident advantages—we channel our investigation towards whether LLMs possess
   the inherent capability to rectify their responses. Such an investigation is also essential for
   understanding the capabilities of LLMs. Consequently, we focus on self-correction without any
   external or human feedback. We term this setting intrinsic self-correction."
3. **Xu, 2312.09085 §7.** "Our research explores an orthogonal direction. We introduce a novel
   direction to intentionally induce hallucination to assess LLMs' alignment with their internal
   knowledge and their robustness in the face of misinformation."
4. **Wu, 2110.01691 §2.3.** "Our Chaining approach also aims to address pitfalls of a single LLM
   pass, but the pitfalls are somewhat distinct."
5. **Mozannar, 2210.14306 §2.** "This wide dispersion of results raises interesting questions
   about the nature of the utility afforded by neural code completion engines: how, and when, are
   such systems most helpful; and conversely, when do they add additional overhead? This is the
   central question to our work."

### B. Named-closest-competitor form (names one work as the nearest, then states the difference)

6. **Mozannar, 2210.14306 §2.** "The related work closest to answering this question is that of
   Barke et al. (Barke et al., 2022), who showed that interaction with Copilot falls into two
   broad categories: the programmer is either in 'acceleration mode' where they know what they
   want do, and Copilot serves to make them faster; or they are in 'exploration mode', where they
   are unsure what code to write and Copilot helps them explore. The taxonomy we present in this
   paper, CUPS, enriches this further with granular labels for programmers' intents."
7. **Wu, 2110.01691 §2.2.** "Finally, the closest work to ours might be online interfaces for
   users to interactively create prompts, or interfaces enabling users to perform natural language
   programming of code using a large language model (Jiang et al., 2021). These systems used
   prompt engineering to create a set of programming-related functionality for users. While this
   prior work focused on single prompts, our work looks at how Chaining multiple prompts can
   address a much wider range of human tasks, and evaluate its effects on user experience."
8. **Xu, 2312.09085 §7.** "The most similar work with us is (Wang et al., 2023a), which employs a
   debate setting to investigate whether ChatGPT can refrain from blindly accepting users'
   incorrect opinions on reasoning tasks. The difference in our work is that we explore novel
   strategies to mislead LLMs through persuasive conversation with a primary emphasis on
   factuality."
9. **Shankar, 2404.12272 §2.** "One recent LLM-assisted approach, SPADE (Shankar et al., 2024),
   makes headway on these issues, helping developers generate Python assertion functions for LLM
   outputs from prompt history. Here we leverage a similar algorithmic approach to SPADE, but
   embed it inside an LLM-assisted user interface for evaluator prototyping, EvalGen, that also
   assists with criteria generation, measuring alignment with human preferences, and visualizing
   results."
10. **Zheng, 2306.05685 §2.1.** "Conversational benchmarks, like CoQA [30] and OpenAssistant [19],
    are closest to our intended use cases. However, the diversity and complexity of their
    questions often fall short in challenging the capabilities of the latest chatbots."

### C. Survey-differentiation form (positioning against a close competitor that covers the same ground)

11. **Kamoi, 2406.01297 §9, "Differences from Other Survey".** "Pan et al. (2024) provide a
    comprehensive survey on broad studies related to self-correction. Our work specifically
    focuses on (inference-time) self-correction and provides a more detailed and critical analysis
    of prior work."
12. **Kamoi, 2406.01297 §9.** "Huang et al. (2024) analyze problems in evaluation settings of
    self-correction research, which motivates our work. They focus on analyzing a few papers on
    intrinsic self-correction in reasoning tasks. We provide a more comprehensive analysis of
    self-correction with in-context learning, external tools, and fine-tuning."
13. **Tyen, 2311.08516 §5.** "While their list includes training-time correction strategies such
    as RLHF (Ouyang et al., 2022) and self-improve (Huang et al., 2022), our backtracking method
    falls into the category of post-hoc correction, where the correction process is applied to
    outputs that have already been generated."

Note the second Kamoi sentence: the competitor is credited as the paper's own motivation
("which motivates our work") before the scope difference is stated. That is the most additive
construction in the corpus.

### D. Building-on form (explicit continuity, then the increment)

14. **Sharma sycophancy, 2310.13548 §5.** "Building on their findings, we show sycophancy in
    varied, realistic settings across 5 different AI assistants used in production (§3). Moreover,
    we investigate the role of human feedback in these behaviors (§4)."
15. **Sharma echo chamber, 2402.05880 §2.1.** "Building on these prior works, our research aims to
    investigate whether and how LLM-powered conversational search systems can exacerbate people's
    selective exposure and reduce information diversity. Our experimental design was informed by
    previous HCI research conducting laboratory studies on selective exposure…"
16. **Lee, 2201.06796 §2.1.2.** "This paper adds to this line of research by curating a large
    interaction dataset that can be replayed to provide both holistic and felt understandings."
17. **Sharma echo chamber, 2402.05880 §2.2.** "Our work contributes to the literature on human-LM
    interaction with insights about a new and popular application domain—conversational search, and
    explores whether and how a human bias—selective exposure—interacts with the properties and
    affordances of LLMs to impact people's information consumption."
18. **Vasconcelos, 2212.06823 §2.1.** "We provide another lens through which to view this line of
    work: one that uses a cost-benefit framework where cognitive forcing functions can be viewed as
    manipulations for cost, i.e. by necessitating cognitive effort and analytical thinking."

### E. Design-choice form (differentiates by naming what the paper does, not what others fail to do)

19. **Madaan, 2303.17651 §2.** "In this work, we use NL feedback, since this allows to easily
    provide self-feedback using the same LM that generated the output, while leveraging existing
    pretrained LLMs such as GPT-4."
20. **Madaan, 2303.17651 §2.** "In this work, we avoid training a separate refiner and employ a
    few-shot LLM refiner for multiple domains."
21. **Laban, 2505.06120 §2.** "In our work, we conduct both single-turn and multi-turn conversation
    simulations on a common set of tasks: controlled experiments that precisely allow us to
    identify performance degradations from single- to multi-turn settings."
22. **Laban, 2505.06120 §2.** "We make underspecification the central element of our evaluation
    setting."
23. **Laban, 2505.06120 §2.** "In this work, we focus exclusively on generation tasks that capture
    widely used scenarios in both programming and natural language domains."
24. **Chen, 2304.05128 §6.** "In contrast to prior work on training a separate model for code
    repair, Self-Debugging utilizes pretrained large language models for code, and teaches the
    model to debug via few-shot prompting."
25. **Chen, 2304.05128 §6.** "On the other hand, Self-Debugging enables the model to generate
    feedback messages on its own at test time, and does not require extra training."
26. **Chen, 2304.05128 §6.** "Our prompting format of code explanation is relevant in spirit to
    chain-of-thought prompting, as the line-by-line code explanation in natural language
    facilitates analysis of the code that is useful for the debugging task."
27. **Wang, 2309.10691 §4.2.** "Different from prior work, MINT covers a range of diverse tasks and
    is designed to measure the multi-turn interaction capabilities of LLMs with both tools and
    users that are more aligned with real-world applications."
28. **Kwan, 2401.16745 §2.** "In contrast, our work evaluates LLM's comprehensive ability to
    conduct multi-turn conversations, possibly involving multiple types of dialogue in one
    session."
29. **Madaan, 2303.17651 §2.** "To address this, Welleck et al. (2022) selected the best output by
    relying on knowing the ground truth at test time. In contrast, our Self-Refine approach
    includes a scalar value-based stopping criteria that overcomes this issue."
30. **Lee, 2201.06796 §2.4.** "However, we argue that the underlying assumption of most datasets is
    the full-automation of tasks rather than augmentation. In other words, they do not consider
    interactive settings where users can guide and correct systems' generated outputs, but rather
    expect LMs to generate correct answers alone. As a result, these datasets tend to not capture
    the process of writing, but rather focus on result. In this work, we aim to design reusable and
    expandable datasets that capture the writing process."
31. **Bansal, 2006.14779 §2.** "To better understand the role of explanations in producing
    complementary performance, we conducted user studies that address both of these potential
    causes by (1) enlarging the zone of potential complementarity by controlling AI accuracy to
    match that of an average human… and (2) carefully controlling collaboration mechanisms,
    including explanations and measures of AI confidence."
32. **Stechly, 2310.12397 §2.** "This paper focuses on understanding these sorts of claims–and
    especially of the effectiveness of iterative prompting."
33. **Laban, 2505.06120, Appendix A opening.** "The Background (Section 2) reviews the most
    directly related prior work, focused on multi-turn evaluation. We now cover other related prior
    works that have studied underspecification."

### F. Scope-of-a-gap form (states an absence without attributing failure to anyone)

34. **Buçinca, 2102.09692 §2.2.** "The research community is aware of the risk of overreliance on
    AIs in general and guidelines have been proposed to reduce overtrust… However, to the best of
    our knowledge, there are no specific interventions that are designed explicitly to mitigate
    overreliance on AIs and that are shown empirically to reduce overtrust."
35. **Bai, 2402.14762 §2.** "Despite these efforts, there remains a notable gap in fine-grained
    evaluations for multi-turn interactions."
36. **Laban, 2505.06120 §2.** "Crucially, such works typically simulate episodic conversations:
    each turn in the conversation introduces a subtask that relates to previous conversation turns,
    but can be evaluated in isolation. In this work, we find that episodic tasks overestimate LLM
    performance in multi-turn conversations (see Section 7.3)."
37. **Sharma echo chamber, 2402.05880 §2.3.** "In the second experiment, we further study the
    effects of LLM with manipulated opinion bias on people's information behaviors and
    consumption—an issue that has not been explored for conversational search but can be
    potentially prevalent with the use of LLMs."

### What none of these sentences does

Across all 37, no sentence says a prior paper is wrong, flawed, or inadequate as a paper. The
harshest constructions in the corpus attach the limitation to the **setting** rather than to the
authors, and they occur in only two papers:

- **Kwan, 2401.16745 §2.** "Nevertheless, the dataset's limited sample size poses a challenge,
  with each conversation consisting of only two turns. This constraint hinders the ability to
  broaden the evaluation scope…" and "but its reliance on human participation limits its
  scalability and efficiency across different tasks."
- **Zheng, 2306.05685 §2.1.** "However, the diversity and complexity of their questions often fall
  short in challenging the capabilities of the latest chatbots."

Both attach the limit to a property of the artifact (sample size, question diversity), not to a
judgment about the work. This is the boundary to hold: describe the artifact's coverage, never
the authors' care.

---

## Citation density and form

### Density

- Corpus mean: **36.8 works cited per section**, **4.58 works per 100 words**.
- NLP subset: mean 32.6 works, and denser per word. Kamoi 9.6 works per 100 words, Wang 7.7,
  Madaan 7.4, Bai 7.4, Chen 7.1, Pan 7.0.
- HCI subset: mean 44.3 works, but thinner per word: Buçinca 3.3, Wu 3.4, Lee 3.6, Bansal 3.8,
  Vasconcelos 4.1, Sharma-echo 4.3, Shankar 2.6, Mozannar 2.4.

The two communities buy the same coverage differently. NLP sections cite more per sentence and
describe less; HCI sections describe each work at length and cite less per sentence. A section
that wants both a high citation count and an argument has to use the NLP density and the HCI
sequencing, which is what Chen (82 works, 1155 words) and Sharma-echo (66 works, 1536 words) do.

### Parenthetical versus textual

Counting citation macros across all 471 elements: **302 `\citep` (parenthetical), 132 plain
`\cite`, 37 `\citet` (textual)**. Textual citation is **7.9 percent** of citation elements
overall.

By paper, the highest textual share: Kwan 4 of 6 (67 percent), Xu 6 of 20 (30 percent), Sharma
sycophancy 3 of 15 (20 percent), Lee 6 of 38 (16 percent), Madaan 6 of 38 (16 percent). Papers
with zero textual citations: Huang, Stechly, Laban, Zheng, Bansal, Buçinca, Vasconcelos, Bai,
Wang, Chen, Wu.

The rule the corpus follows is consistent and worth adopting literally: **textual citation is
reserved for a work being characterised individually; parenthetical for a work being counted into
a cluster.** Kwan's section is 67 percent textual because every sentence in it describes one
benchmark. Chen's is 0 percent textual because its 82 works arrive in 32 clusters. Where an
author writes a name in prose but the style file emits brackets, the effect is the same: Bansal
writes "in Lai et al. (Lai et al., 2020), MTurk workers classified deceptive hotel reviews…" and
Mozannar writes "Weisz et al. interviewed developers and found that…" (2210.14306), so the true
rate of individually-named works is higher than the macro count implies.

### Surveys used to compress a literature

Five of the 22 sections use a survey citation as a compression device, and each does it in one
sentence that states what the survey establishes before moving on:

- **Huang, 2310.01798 §2.** "A pivotal distinction lies in the source of feedback (Pan et al.,
  2023): Is it purely internal, originating solely from the LLM, or does it draw from external
  inputs?"
- **Tyen, 2311.08516 §5.** "Pan et al. (2023) present a plethora of self-correction methods in
  recent literature."
- **Sharma sycophancy, 2310.13548 §5.** "Learning from human feedback faces fundamental
  difficulties (Casper et al., 2023)."
- **Pan, 2308.03188 §1.** "One popular line of research involves the use of human feedback to
  evaluate and refine models, as encapsulated in the survey by Fernandes et al. (2023)."
- **Kamoi, 2406.01297 §9.** the whole 84-word section, positioning against two surveys at once.

The compression form is always the same: the survey stands in for a body of work whose internal
distinctions do not matter for the argument, and the sentence says what distinction the survey
supplies. No section cites a survey and then also enumerates the works the survey covers.

### How a literature spanning disciplines is handled

Six sections reach across a disciplinary boundary. The mechanisms are three, and all six use at
least two of them.

**Mechanism 1: name the discipline in the heading.** Lee (2201.06796) is the clearest, with
parallel sections `2.3. Datasets in HCI` and `2.4. Datasets in NLP`, each about the same object
and each written in that field's terms. Vasconcelos names two fields in two headings,
`2.1. Cognitive biases in decision-making` and `2.2. Decision-making in behavioral economics`.
Wu imports a fourth field with `2.3. Workflows in Crowdsourcing`.

**Mechanism 2: name the community in the topic sentence.** Verbatim openers:

- Sharma echo chamber §2.1: "Psychologists have extensively studied people's selective exposure
  bias (Frey, 1986; Hart et al., 2009)…"
- Sharma echo chamber §2.1: "The HCI and broader research and activist communities have had
  long-standing concerns over the negative effect of information and web technologies on the
  diversity of information that people consume."
- Sharma echo chamber §2.2: "HCI researchers have started to explore applications of generative
  language models (LMs) and study human interactions with them before this wave of widely adopted
  LLMs."
- Shankar §2: "The HCI community has extensively studied interactive machine learning (iML)."
- Shankar §2: "In the ML and NLP communities, researchers have explored many ways to align
  LLMs—and their evaluations—to specific user tasks."
- Buçinca §2.1: "Dual processing theory postulates that humans make decisions through one of two
  distinct cognitive processes…"
- Lee §2.4: "Datasets are central to evaluating LMs' generative capabilities in NLP…"

**Mechanism 3: state the disanalogy when importing a foreign literature.** The imported field is
never assumed to transfer. Verbatim:

- **Wu, 2110.01691 §2.3.** "Our Chaining approach also aims to address pitfalls of a single LLM
  pass, but the pitfalls are somewhat distinct. While crowdsourcing focuses more on cognitive load
  and task duration — factors that can affect the performance of human workers (Kulkarni et al.,
  2011) — for LLMs with intensive computing power, their limitations err towards a lack of
  reasoning abilities, high variance of prompt effectiveness, and exposure bias."
- **Vasconcelos, 2212.06823 §2.2.** "To frame this aversion to engaging in effortful thinking in
  economic terms: people weigh the potential benefits of cognitive effort against its perceived
  costs (Navon and Gopher, 1977; Kool and Botvinick, 2018)."
- **Shankar, 2404.12272 §2.** "A broader point is that research in LLMOps optimization tends to
  come from the domains of NLP and ML, where authors generally validate tool performance against
  benchmark datasets with pre-defined metrics, leaving open the question of how well they perform
  in the wild on idiosyncratic user tasks."

**Ordering.** In all six, the non-NLP literature comes first and the NLP literature second, so the
section moves from the general behavioural claim to the computational instance. Sharma echo
chamber goes psychology, then HCI/NLP, then information retrieval. Buçinca goes cognitive
psychology, then AI-assisted decision-making. Vasconcelos goes HCI, then cognitive psychology,
then behavioural economics. Lee is the exception that proves the ordering is about argument and
not seniority: it puts HCI before NLP because its contribution is an HCI artifact.

---

## Rules

Each rule states a checkable condition and names the evidence.

**R1. Place the section before the method, or split it.** Fourteen of 22 place it before the
method; four of the six late placements pair it with a short Background section that runs before
the method (Kamoi, Sharma sycophancy, Chen, Xu). A late-only related work with no earlier
background occurs in only two papers (Tyen, Wang), both dataset papers whose §1 already positions
the contribution. *Check: either the section precedes the method, or a Background section defining
the paper's terms precedes it and the related work sits late.*

**R2. Target 310 to 530 words for an NLP venue. SUPERSEDED 2026-09-14, see the correction below.**
*Check: the compiled section is between 310 and 530 words of prose.*

> **Correction, 2026-09-14.** R2 originally read "target 550 to 900 words," and that floor was
> wrong in two ways. It contradicted its own evidence: the NLP mean stated in the same sentence is
> 543, below the floor it sets, and four of the NLP sections measured here (Kamoi 303, Kwan 236,
> Tyen 268, Stechly 193) sit far below it. And it rested on 22 sections, of which 14 were NLP.
> `scripts/introduction_corpus/06_section_census.py` now measures related-work length across the
> 69 cached papers: n=62, p25 310, median 402, p75 526. Ali's own 24 papers give a median of 397.
> The floor was roughly 150 words above the field median and was set from a small sample.
>
> This is not a cosmetic revision. Acting on the old floor would have meant padding a section that
> already sits above the median, against an 8-page limit. A task to do exactly that was logged on
> 2026-09-14 and has been withdrawn.

**R3. Use three to five thematic clusters, not more.** Median 3, mean 3.1, maximum 5 across the 15
thematically organised sections. Nothing in the corpus exceeds five. *Check: count the
`\paragraph` commands; the number is between 3 and 5.*

**R4. Give each cluster 9 to 16 cited works.** Median across the corpus is about 14 works per
top-level heading; only two sections fall below 7, and both are minimal by design (Tyen 4.5,
Zheng 6.0). A cluster with four or five citations reads as a topic that was raised but not
covered. *Check: works cited divided by number of clusters is at least 9.*

**R5. Organise thematically, and let the headings name research topics.** 15 of 22 are thematic;
6 are unheaded narrative; none is chronological. Every heading in the corpus names a topic or an
object, never a claim or a question. *Check: each heading would still be an accurate label if a
different paper wrote that paragraph.*

**R6. Use `\paragraph` run-in headings, not numbered subsections.** All eight NLP papers with
headings use run-ins (Madaan, Kamoi, Tyen, Sharma sycophancy, Shankar, Bai, Chen, Xu); six of the
seven numbered-subsection users are HCI papers. *Check: no `\subsection` inside the related work.*

**R7. Position at the end of every cluster, not once at the end of the section.** No section in
the corpus has a standalone closing "in contrast, we" paragraph. Tyen and Sharma sycophancy carry
positioning in 3 of 3 paragraphs; Xu 5 of 6; Wu 5 of 6; Madaan 4 of 5. *Check: every `\paragraph`
ends with at least one sentence containing "we", "our", or the paper's own system name.*

**R8. Name the closest competitor explicitly and say what differs, in that order.** Five sections
use the construction (Mozannar, Wu, Xu, Shankar, Zheng), each opening with a phrase like "the
closest work to ours", "the most similar work with us", "closest to our intended use cases", then
describing the competitor's finding on its own terms, then stating the difference in the paper's
own setting. *Check: the closest-work paragraph names one work, states its result in a full
sentence before any contrast, and locates the difference in the setting rather than in the quality
of the work.*

**R9. Credit the competitor as motivation where it is true.** Kamoi's "Huang et al. (2024) analyze
problems in evaluation settings of self-correction research, which motivates our work" is the most
additive sentence in the corpus. *Check: at least one positioning sentence attributes something
the paper owes to the work it is differentiating itself from.*

**R10. State a disagreement in the literature in one sentence with citations on both sides.**
Six sections do this (Stechly, Mozannar, Vasconcelos, Bansal, Sharma echo, Madaan). None
adjudicates in the related-work section. *Check: where results conflict, both positions appear
with their own citations, and the sentence that follows says what this paper does about the
conflict, not who is right.*

**R11. Keep citation elements at roughly 1.5 to 2.0 works each, with about two-thirds naming a
single work.** Corpus mean 1.72; 64.5 percent of elements name one work. Clusters of four to seven
appear only for claims about a field rather than about a result. *Check: no cluster above four
works unless the sentence is a claim about the field.*

**R12. Reserve textual citation for individual characterisation.** 7.9 percent of elements are
`\citet`; the papers with high textual shares (Kwan 67 percent, Xu 30 percent) are the ones
describing one work per sentence. *Check: every `\citet` is followed by a description of what that
work found or did; every `\cite` sits inside a claim about several works.*

**R13. Cite a survey to compress, in one sentence, and do not then enumerate what it covers.**
Five sections do this (Huang, Tyen, Sharma sycophancy, Pan, Kamoi). *Check: each survey citation
appears once, in a sentence that names the distinction or the difficulty it establishes.*

**R14. When the section crosses a disciplinary boundary, name the discipline and state the
disanalogy.** Six sections do this; all six name the community in a heading or a topic sentence,
and three state explicitly why the imported literature does not transfer wholesale (Wu,
Vasconcelos, Shankar). *Check: for every non-NLP literature imported, one sentence says which
field it belongs to and one says what is different about the computational case.*

**R15. Order cross-disciplinary clusters from the behavioural claim to the computational
instance.** Sharma echo (psychology, HCI, IR), Buçinca (psychology, then AI-assisted decisions),
Vasconcelos (HCI, psychology, economics), Wu (LLMs, HCI, crowdsourcing). *Check: the section does
not open on a machine-learning method and then reach back for a human-behaviour justification.*

**R16. Attach any limitation to an artifact's property, never to the authors.** The two harshest
constructions in the corpus (Kwan, Zheng) name sample size, turn count, and question diversity.
No sentence in 22 sections says a paper is flawed. *Check: search the section for evaluative
adjectives applied to prior work and remove each one.*

**R17. Cite peer-reviewed or archival work; cite an industry source only for a measurement it
uniquely reports, and name it in prose.** The corpus does contain non-archival citations, and they
are always individually characterised for a specific number: Mozannar cites a GitHub study
("The study concluded by finding that task completion was reduced by 55% in the Copilot condition
(Kalliamvakou, 2022)") and a Google study ("a study by Google showed than an internal CodeRec
model had a 6% reduction in 'coding iteration time' (Tabachnyk and Nikolov, 2022)"). No section in
the corpus cites a market-research or analyst report, and none groups non-archival sources into a
multi-work cluster. *Check: every non-archival citation appears alone, in a sentence quoting the
number it supplies.*

**R18. Do not write a defensive paragraph.** No section in the corpus raises an objection to its
own design and answers it. Prior negative results are reported as findings about the prior setting
(Tyen on Reflexion and RCI; Vasconcelos on Buçinca), not as anticipated attacks. *Check: no
sentence in the section has the shape "one might worry that X; however".*

---

## Constructions to avoid, with evidence

**Eight or more clusters.** The corpus maximum is five (Chen). Every section with more than four
clusters compensates with high citation density: Chen carries 16.4 works per cluster. A section
with eight clusters and six works each is thinner per topic than anything in the corpus.

**A cluster whose entire evidence is one multi-work bracket.** The corpus does this only for
claims about a field, never for the claim that carries a paragraph. Wang's seven-work tool-use
bracket sits in a sentence that says tools exist; the sentence that positions MINT names no
bracket at all.

**A standalone closing paragraph that begins "In contrast, we".** Zero of 22. The three papers
that use the contrastive connective (Madaan, Kwan, Wang) put it in the final *sentence* of a
paragraph that has already done literature work.

**Headings that state a claim or ask a question.** Zero of the roughly 45 headings collected here
do this. Even Kamoi's argumentative survey uses the flattest possible labels: `Self-Detection`,
`Editing Human-Written Text`, `Self-Training`.

**Evaluative adjectives about prior work.** Absent from 22 sections. Where a limit is stated it is
a property: "limited sample size", "each conversation consisting of only two turns", "reliance on
human participation limits its scalability", "fall short in challenging the capabilities of the
latest chatbots".

**A related-work section that never names its own field.** The corpus repeatedly names the
community it is speaking to: "The HCI community has extensively studied…", "Psychologists have
extensively studied…", "In the ML and NLP communities…", "HCI researchers conducted experiments
to study…", "Prior work on communication and linguistics has identified underspecification as a
common feature of human language". A section built entirely of anonymous openers ("A growing body
of work", "Recent work has shown", "A long line of research") gives a reviewer no field to place
the paper in, which is precisely the advisor's complaint.

**Market-research and analyst reports grouped in a bracket.** Not attested anywhere in the corpus.

---

## Checklist

Run this against the compiled section before submission.

1. [ ] Section sits before the method, or a Background section precedes the method and related
   work sits late. (R1)
2. [ ] Prose under 900 words. (R2)
3. [ ] Between three and five `\paragraph` clusters. (R3)
4. [ ] At least nine cited works per cluster. (R4)
5. [ ] Every heading names a topic or object, not a claim or question. (R5)
6. [ ] Run-in `\paragraph` headings only, no `\subsection`. (R6)
7. [ ] Every cluster ends with a first-person positioning sentence. (R7)
8. [ ] The closest competitor is named, its result stated in full before any contrast, and the
   difference located in the setting. (R8)
9. [ ] At least one positioning sentence credits a competitor as motivation. (R9)
10. [ ] Any conflict in the literature is stated with citations on both sides and no adjudication.
    (R10)
11. [ ] No citation cluster above four works unless the claim is about the field. (R11)
12. [ ] Every `\citet` is followed by what that work found. (R12)
13. [ ] Each survey citation appears once, compressing a distinction. (R13)
14. [ ] Each imported non-NLP literature is named by field and its disanalogy stated. (R14)
15. [ ] Cross-disciplinary clusters run behavioural claim first, computational instance second.
    (R15)
16. [ ] No evaluative adjective is applied to prior work. (R16)
17. [ ] Non-archival citations appear alone, quoting the number they supply. (R17)
18. [ ] No objection-then-rebuttal paragraph. (R18)
19. [ ] Every cited work in the section has a verified bib entry and has actually been read.

---

## How this paper's current related work measures up

Assessed against `paper/sections/related_work_v2.tex` as of 2026-09-02. Measured mechanically:
**1,073 words of prose**, **8 `\paragraph` clusters**, **28 citation elements**, **46 cited
works** across **45 unique keys**, mean cluster 1.64 works, maximum cluster 4, 15 single-work
citations and 13 multi-work, 8 `\citet` (29 percent), 4.3 works per 100 words. All 45 keys resolve
to entries in `paper/references.bib` (66 entries total).

Per cluster:

| Cluster | Words | Cite elements | Works | `\citet` |
|---|---|---|---|---|
| Human-AI interaction and user-side determinants of quality | 165 | 4 | 4 | 1 |
| Over-reliance and automation bias | 150 | 3 | 6 | 0 |
| Intrinsic self-correction and self-refinement | 228 | 7 | 9 | 5 |
| Termination and overthinking | 94 | 3 | 4 | 0 |
| Sycophancy and compliance under pressure | 108 | 3 | 6 | 0 |
| Biases in LLM-as-judge evaluation | 123 | 4 | 9 | 0 |
| Token efficiency and the cost of AI | 65 | 2 | 5 | 1 |
| Multi-turn degradation and closest work | 140 | 2 | 3 | 1 |

### What already matches the corpus

- **Placement (R1).** Before the method. Matches 14 of 22.
- **Positioning at every cluster (R7).** All eight paragraphs end with a first-person positioning
  sentence. Only Tyen and Sharma sycophancy achieve 3 of 3 in the corpus; nothing achieves 8 of 8,
  because nothing has eight clusters. On this dimension the section is stronger than its models.
- **Closest-competitor construction (R8).** "Closest to our work, \citet{laban2025lost} show that
  models lose accuracy across multi-turn conversations when a task's requirements are revealed
  piecewise, and attribute the loss to underspecification accumulating over turns…" then "Our
  setting differs in a way that isolates a distinct cause". This is the Mozannar and Xu form
  exactly: name, state the competitor's finding in full, then locate the difference in the setting.
- **Complementary-question form (R8, R9).** "This literature asks whether a given feedback signal
  is sufficient to improve an output; we ask the complementary question of what happens when the
  signal is absent entirely and the output to be revised is already adequate." This is the
  strongest sentence in the section and belongs to the same family as Huang's intrinsic
  self-correction paragraph and Xu's "orthogonal direction".
- **Additive close (R16).** "The two findings are complementary, one showing failure when
  requirements accumulate and the other showing failure when a sufficient output is revised
  without direction." Nothing in the section disparages prior work. Clean on R16 and R18.
- **Cluster size discipline (R11).** Mean 1.64 works per citation element against a corpus mean of
  1.72; maximum cluster 4 against a corpus maximum of 8. Well inside the norm.
- **Textual citation used for characterisation (R12).** All eight `\citet` uses name a work that is
  then described (Laban, Madaan, Huang, Tyen, Tsui, Kamoi, Borisov). The 29 percent share is above
  the corpus mean of 7.9 percent but matches Xu at 30 percent, and Xu is the closest structural
  analogue in the corpus.
- **Run-in headings (R6).** Correct form.
- **Headings name topics (R5).** All eight are topic labels. None states a claim.

### Where it departs from the corpus

1. **Eight clusters where the corpus maximum is five (R3).** This is the largest single departure.
   Chen has five, Madaan and Xu four, and the median is three. Eight clusters produce a section
   that reads as a survey of adjacent topics rather than an argument with a position.

2. **5.75 works per cluster where the corpus median is about 14 (R4).** Four clusters fall at or
   below six works: Termination and overthinking (4), Human-AI interaction (4), Token efficiency
   (5), Sycophancy (6), and the closest-work cluster (3). Only Tyen (4.5) and Zheng (6.0) are this
   thin in the corpus, and both are minimal sections in dataset papers. This is the mechanical
   shape of the advisor's complaint: the citation count is not low in aggregate (46 works is above
   the NLP mean of 32.6), but it is spread across too many topics for any single topic to look
   covered.

3. **1,073 words, above the NLP mean of 543 and above all but five sections in the corpus (R2).**
   The length is HCI-scale while the venue is NLP. Combined with the cluster count, this suggests
   the same fix twice: fold eight clusters into four or five, and the word count comes down with
   them.

4. **No field is named anywhere (R14, and the advisor's stated objection).** The openers are
   anonymous: "A growing body of work treats…", "a long line of human-factors research indicates",
   "Whether models can improve their own outputs has been studied under the heading of
   self-refinement", "A parallel failure appears within a single response", "Using LLMs to evaluate
   generated text is now standard practice". Only "human-factors research" and
   "scalable-oversight research" come close to naming a community, and neither names it as a field
   the paper is joining. The corpus openers to imitate are Shankar's "The HCI community has
   extensively studied interactive machine learning" and Sharma's "Psychologists have extensively
   studied people's selective exposure bias". The paper's own claim, that this is human-AI
   interaction work about the user side of a revision request, needs the phrase "human-AI
   interaction" or "human-computer interaction" to appear as a field the section is speaking
   inside, not only as a paragraph title.

5. **The four market-research citations (R17).** `menlo2025llmmarket, gartner2026agentic,
   deloitte2026stateofai, mckinsey2025stateofai` appear as a single four-work bracket supporting
   "Enterprise inference spending has risen steeply, roughly doubling in under a year". No section
   in the 22 cites an analyst report, and no section groups non-archival sources. The corpus
   precedent for citing industry (Mozannar on the GitHub and Google studies) names the source in
   prose and quotes the number it supplies. Either name one source and its number, or move the
   spending claim to the introduction or discussion where a motivating figure is conventional.

6. **The disanalogy for the imported literatures is not stated (R14).** Two of the eight clusters
   import non-NLP work: automation bias and complacency from human factors (Skitka, Parasuraman)
   and AI-assisted decision-making from HCI (Bansal, Buçinca, Vasconcelos, Schemmer). The section
   asserts that this explains why the failure is missed, but never says what is different about the
   revision case. Wu's crowdsourcing paragraph is the model: "Our Chaining approach also aims to
   address pitfalls of a single LLM pass, but the pitfalls are somewhat distinct. While
   crowdsourcing focuses more on X… for LLMs… their limitations err towards Y." One sentence saying
   how an undirected revision request differs from an AI recommendation a user accepts or rejects
   would do the same work here.

7. **No competitor is credited as motivation (R9).** The Kamoi construction ("which motivates our
   work") is absent. Kamoi is already cited as the survey that "locates the bottleneck in feedback
   generation rather than in the capacity to revise, the seam on which our finding sits", which is
   close, but the debt runs the other way in the sentence.

8. **No disagreement is staged (R10).** The self-correction paragraph reports Madaan's positive
   result and then the later negative results as a settled progression ("Later work finds the
   benefit contingent on an external signal"). Six corpus sections instead state the disagreement
   as live. Stechly's sentence is the template: some studies find X, others argue Y, and this paper
   is about adjudicating the claim. Given that this paper's whole premise is that the optimistic
   and sceptical results are both real under different conditions, the Stechly framing is available
   and would place the contribution more sharply than the progression framing does.

### Suggested consolidation, keeping every current citation

Four clusters, in the corpus's cross-disciplinary order (R15), reaching 11 to 12 works each:

- **Human-AI interaction and reliance on model output** (merges clusters 1 and 2; 10 works):
  opens by naming human-computer interaction and human-factors research as the fields, and states
  the disanalogy for the revision case.
- **Intrinsic self-correction and its feedback requirement** (cluster 3 unchanged; 9 works): stage
  the Madaan-versus-Huang disagreement as live, then locate this paper's complementary question.
- **Compliance, overthinking, and failure to stop** (merges clusters 4 and 5; 10 works): one
  mechanism paragraph covering the model-side reasons a revision goes past its optimum.
- **Multi-turn evaluation and measurement** (merges clusters 6 and 8; 12 works): LLM-judge bias as
  a measurement problem for exactly this comparison, followed by the Laban positioning, which is
  already the strongest paragraph and should close the section.

The token-efficiency material (cluster 7, 5 works) moves to the introduction or discussion. That
yields four clusters, roughly 750 to 800 words, and about 10 to 12 works per cluster, which lands
inside R2, R3 and R4 without dropping a single citation the section currently has.
