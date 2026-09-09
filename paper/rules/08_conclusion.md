# Rules: Conclusion

Retrieved 2026-09-02 (ARR policy pages 2026-09-03 UTC). 25 conclusions read in full, in the
LaTeXML HTML rendering served at `https://arxiv.org/html/<ID>`. Four further papers were opened
and found to have no conclusion section at all; they are recorded below because their absence is
itself evidence.

Everything quoted here was fetched and read in this session. Nothing is reconstructed from memory.
Word counts are computed from the extracted paragraph text of each conclusion section, excluding
the section heading and excluding acknowledgements paragraphs that the renderer folds into the
same block (this affected only Prometheus, 2310.08491).

## Corpus

25 papers with a conclusion section. "Venue" is the arXiv record's own comment field where it
states one; "not stated" means the arXiv record does not name a venue and I did not verify it
elsewhere. "Nums" records whether at least one quantitative *result* value from the paper's own
experiments appears in the conclusion (model names such as GPT-4, section cross-references,
citation years and dataset-scale counts do not count).

| Paper | arXiv ID | Venue (per arXiv comment) | Words | Paras | Nums | Final-sentence type |
|---|---|---|---|---|---|---|
| Kamoi et al., When Can LLMs Actually Correct Their Own Mistakes? | 2406.01297 | TACL 2024 | 55 | 1 | no | contribution restatement |
| Chiang et al., Chatbot Arena | 2403.04132 | not stated | 59 | 1 | no | artifact release |
| Zheng et al., Judging LLM-as-a-Judge (MT-Bench) | 2306.05685 | NeurIPS 2023 D&B | 64 | 1 | **yes** | attributed knowledge claim |
| Wang et al., MINT | 2309.10691 | not stated | 66 | 1 | no | pointer to appendix |
| Shinn et al., Reflexion | 2303.11366 | not stated | 67 | 1 | no | future-work gesture |
| Sharma et al., Towards Understanding Sycophancy | 2310.13548 | not stated | 78 | 1 | no | broader implication |
| Chan et al., ChatEval | 2308.07201 | not stated | 82 | 1 | no | attributed knowledge claim |
| Zhang et al., Exploring Collaboration Mechanisms for LLM Agents | 2310.02124 | ACL 2024 Main | 82 | 1 | no | future-work gesture |
| Wu et al., CollabLLM | 2502.00640 | ICML 2025 (Outstanding Paper) | 86 | 1 | no | attributed knowledge claim |
| Li et al., PRD: Peer Rank and Discussion | 2307.02762 | TMLR | 87 | 1 | no | future-work gesture |
| Lee et al., CoAuthor | 2201.06796 | not stated (CHI 2022 format) | 101 | 1 | no | call to the community |
| Laban et al., LLMs Get Lost In Multi-Turn Conversation | 2505.06120 | not stated | 102 | 1 | no | call to the community |
| Kwan et al., MT-Eval | 2401.16745 | not stated (ACL template) | 106 | 1 | no | broader implication |
| Pan et al., Automatically Correcting LLMs (survey) | 2308.03188 | Work in Progress, v2 | 107 | 1 | no | artifact release |
| Madaan et al., Self-Refine | 2303.17651 | not stated | 115 | 1 | no | artifact release |
| Kim et al., Prometheus 2 | 2405.01535 | EMNLP 2024 Main | 121 | 1 | no | call to the community |
| Xu et al., Pride and Prejudice (self-bias) | 2402.11436 | not stated (ACL template) | 123 | 1 | no | attributed knowledge claim |
| Wang et al., LLMs are not Fair Evaluators | 2305.17926 | not stated | 135 | 1 | no | artifact release |
| Tyen et al., LLMs cannot find reasoning errors | 2311.08516 | ACL 2024 Findings | 138 | 2 | no | future work + artifact release |
| Kim et al., Prometheus | 2310.08491 | not stated | 158 | 1 | **yes** | call to the community |
| Olausson et al., Is Self-Repair a Silver Bullet? | 2306.09896 | ICLR 2024 | 165 | 1 | **yes** | attributed knowledge claim |
| Stechly et al., GPT-4 Doesn't Know It's Wrong | 2310.12397 | not stated (18 pages) | 191 | 1 | no | broader implication |
| Chen et al., Teaching LLMs to Self-Debug | 2304.05128 | not stated | 277 | 2 | **yes** | future-work gesture |
| Valmeekam/Stechly et al., Self-Verification Limitations | 2402.08115 | not stated | 316 | 3 | no | positioning within prior work |
| Huang et al., LLMs Cannot Self-Correct Reasoning Yet | 2310.01798 | ICLR 2024 | 575 | 4 | no | call to the community |

Papers opened that have **no conclusion section**, and what they end on instead:

| Paper | arXiv ID | Last main-body section |
|---|---|---|
| Lee et al., Evaluating Human-Language Model Interaction (HALIE) | 2212.09746 | Discussion |
| Kim et al., Language Models can Solve Computer Tasks (RCI) | 2303.17491 | Limitations, then Discussion |
| Du et al., Improving Factuality and Reasoning through Multiagent Debate | 2305.14325 | Limitations and Discussion |
| Dubois et al., Length-Controlled AlpacaEval | 2404.04475 | Discussion |

4 of 29 papers in this space ship with no conclusion section. All four are non-*ACL formats
(NeurIPS/ICLR/TMLR/arXiv). None of the six ACL-template papers in the corpus omits it. For an ARR
submission the conclusion is effectively obligatory by convention, but it is a *short* obligation.

## Length and structure (with counts)

**Length.** n = 25. Minimum 55 words (Kamoi 2406.01297). Maximum 575 (Huang 2310.01798). Median
**106**. Mean 138. Lower quartile 80, upper quartile 148.

- 15 of 25 (60%) are under 120 words.
- 19 of 25 (76%) are 150 words or fewer.
- 22 of 25 (88%) are 200 words or fewer.
- Only 3 exceed 200 words: Chen 2304.05128 (277), Stechly 2402.08115 (316), Huang 2310.01798 (575).

Restricting to the six papers formatted on the ACL template (2311.08516, 2310.02124, 2405.01535,
2401.16745, 2402.11436, 2505.06120): 82, 102, 106, 121, 123, 138 words. Median 113.5, mean 112.
**No ACL-template paper in the corpus has a conclusion longer than 138 words.**

**Paragraphs.** 21 of 25 (84%) are a single paragraph. 4 are multi-paragraph: Chen 2304.05128 (2),
Tyen 2311.08516 (2), Stechly 2402.08115 (3), Huang 2310.01798 (4). Every one of the six ACL-template
conclusions is one or two paragraphs; five of the six are one.

**Result restatement.** Classifying each conclusion by whether it restates findings with numbers,
qualitatively, or not at all:

- **With at least one numeric result: 4 of 25 (16%).** Zheng 2306.05685 ("an agreement rate of over
  80%"); Olausson 2306.09896 ("increased the number of repaired programs which pass all unit tests
  by 1.58x"); Kim 2310.08491 ("the quality of the feedback was preferred over GPT-4 58.62% of the
  time"); Chen 2304.05128 ("improves the baseline by 2-3%", "a performance gain of 9%", "increases
  the baseline accuracy by up to 12%").
- **Qualitatively, no numbers: 16 of 25 (64%).** 2303.11366, 2305.17926, 2307.02762, 2308.07201,
  2310.01798, 2310.02124, 2310.12397, 2310.13548, 2311.08516, 2401.16745, 2402.08115, 2402.11436,
  2405.01535, 2406.01297, 2502.00640, 2505.06120.
- **Neither, contributions and artifacts only: 5 of 25 (20%).** 2201.06796, 2303.17651, 2308.03188,
  2309.10691, 2403.04132.

The load-carrying observation for this paper: **every negative-result paper in the corpus restates
its finding qualitatively and none of them restates it with statistics.** Stechly 2310.12397 (191
words), Huang 2310.01798 (575), Xu 2402.11436 (123), Tyen 2311.08516 (138) and Laban 2505.06120
(102) contain zero result numbers between them. Where a number does appear it is in a
method-improvement paper reporting a gain (Chen, Zheng, Kim, Olausson), and even Olausson's single
number (1.58x) is there to support a *negative* conclusion about the model's own feedback.

**Opening move.** 20 of 25 (80%) open with a first-person restatement of what the paper did: 16
with the literal frame "In this paper/work/study, we..." (2201.06796, 2303.11366, 2304.05128,
2305.17926, 2306.05685, 2307.02762, 2308.03188, 2308.07201, 2309.10691, 2310.08491, 2310.12397,
2311.08516, 2402.08115, 2402.11436, 2403.04132, 2505.06120) and 4 with a bare "We
present/introduce/provide/investigated" (2303.17651, 2306.09896, 2405.01535, 2406.01297).

The 5 that do not are worth studying, because they are the ones whose conclusions carry a claim
rather than a summary:

- Huang 2310.01798: "Our work shows that current LLMs struggle to self-correct their reasoning
  without external feedback."
- Sharma 2310.13548: "Despite the clear utility of human feedback data for producing high-quality AI
  assistants, such data has predictable limitations."
- Wu 2502.00640: "Multiturn human-LLM collaborations are increasingly prevalent in real-world
  applications."
- Kwan 2401.16745: "MT-Eval represents an important first step in systematically evaluating and
  understanding LLMs' multi-turn conversational abilities."
- Zhang 2310.02124: "This study has highlighted the potential of collaboration mechanisms with LLMs."

**Citations and new material.** 22 of 25 conclusions contain no citation at all. Three cite: Li
2307.02762 (one), Huang 2310.01798 (four), Stechly 2402.08115 (three bracket references). Two more
contain a bare URL to a released resource (Madaan 2303.17651, Pan 2308.03188).

## Verbatim catalogue: every final sentence, classified

All 25, in the order of the corpus table. Retrieved 2026-09-02 from `arxiv.org/html/<ID>`.

**Attributed knowledge claim (5)**

1. Zheng et al., 2306.05685: "Our results reveal that strong LLMs can achieve an agreement rate of
   over 80%, on par with the level of agreement among human experts, establishing a foundation for
   an LLM-based evaluation framework."
2. Olausson et al., 2306.09896: "Our results suggest that self-repair is not a silver bullet for
   code generation, and that current models are held back by their inability to reliably produce
   accurate and useful feedback on why the code is wrong."
3. Chan et al., 2308.07201: "Our qualitative analysis of the discussion process conveys insightful
   intuitions about how a text is evaluated by ChatEval and substantiates our approach's ability to
   support comprehensive evaluations akin to human judgment, thereby demonstrating the reliability
   and efficacy of our framework."
4. Xu et al., 2402.11436: "Finally, our research suggests that larger models are more resistant to
   self-bias, and incorporating external feedback significantly reduces bias, leading to performance
   improvements in LLMs."
5. Wu et al., 2502.00640: "Through extensive simulated and real-world evaluations, we demonstrate
   that CollabLLM is highly effective, efficient, and engaging, while also generalizing well to new
   tasks and interactions, advancing the frontiers of human-centered LLMs."

**Future-work gesture (5)**

6. Shinn et al., 2303.11366: "In future work, Reflexion could be used to employ more advanced
   techniques that have been thoroughly studied in traditional RL settings, such as value learning
   in natural language or off-policy exploration techniques."
7. Chen et al., 2304.05128: "Our preliminary results suggest that model-generated feedback messages
   about semantic errors do not provide additional benefits on top of line-by-line code explanation,
   and future work can explore techniques to predict more informative error messages."
8. Li et al., 2307.02762: "In the future, we plan to investigate how the general peer evaluation
   process benefits the LLMs in learning to access their own answer and answering new questions
   Nicol et al. (2014)."
9. Zhang et al., 2310.02124: "Moving forward, a deeper exploration into the multi-agent society is
   warranted, focusing on collaboration behavior refinement; integrating further insights from
   social psychology could also guide the development of socially aware NLP systems."
10. Tyen et al., 2311.08516: "We leave the development of more sophisticated methods to future work,
    and release our dataset BIG-Bench Mistake to encourage this direction of research."

**Call to the community (5)**

11. Lee et al., 2201.06796: "We encourage fellow researchers to use, analyze, and extend CoAuthor,
    based on their respective design goals and research perspectives."
12. Huang et al., 2310.01798: "Broadly speaking, equal effort should be invested in designing the
    prompts for initial response generation and for self-correction; otherwise, the results could be
    misleading."
13. Kim et al., 2310.08491: "We hope that our work could stimulate future work on using open-source
    LLMs as evaluators instead of solely relying on proprietary LLMs."
14. Kim et al., 2405.01535: "We hope that our work encourages more research on using open-source LMs
    as evaluators."
15. Laban et al., 2505.06120: "Additional experiments reveal that known remediations that work for
    simpler settings (such as agent-like concatenation or decreasing temperature during generation)
    are ineffective in multi-turn settings, and we call on LLM builders to prioritize the reliability
    of models in multi-turn settings."

**Artifact or resource release (4)**

16. Madaan et al., 2303.17651: "To this end, we make all our code, data and prompts anonymously
    available at https://selfrefine.info/."
17. Wang et al., 2305.17926: "We provide our code and human annotations to support future studies
    and enhance the evaluation of generative models."
18. Pan et al., 2308.03188: "To aid in this effort, we create a continually-updated reading list in
    a GitHub repository: https://github.com/teacherpeterpan/self-correction-llm-papers."
19. Chiang et al., 2403.04132: "Our dataset including 100K pairwise preference votes will be
    released for future research."

**Broader implication (3)**

20. Sharma et al., 2310.13548: "Our work motivates the development of model oversight methods that
    go beyond using unaided, non-expert human ratings."
21. Stechly et al., 2310.12397: "Our results thus raise legitimate questions about claims of the
    effectiveness of iterative prompting, adding further fuel to the skepticism surrounding the
    reasoning capabilities of LLMs."
22. Kwan et al., 2401.16745: "We believe this work not only sheds light on the current limitations
    of LLM's multi-turn conversational abilities, it also paves the way for further efforts to close
    the identified gap and develop robust conversational models capable of multi-turn interactions."

**Contribution restatement (1)**

23. Kamoi et al., 2406.01297: "To tackle these issues, we categorize research questions and
    frameworks in self-correction research and provide a checklist for conducting appropriate
    experiments."

**Positioning within prior work (1)**

24. Valmeekam/Stechly et al., 2402.08115: "Similar architectures have already shown some success
    [35], and previous work has proposed the general LLM-Modulo framework [23] which the current
    work fits into."

**Pointer to another section (1)**

25. Wang et al., 2309.10691: "We refer to Appendix A for a discussion of limitations and future
    work."

**Restatement of the named phenomenon as the final sentence: 0 of 25.** Laban 2505.06120 restates
"LLMs get lost in conversation" but places it second, not last.

**Instruction to the reader, phrased as an imperative: 0 of 25.**

Not one conclusion in the corpus ends on a bare imperative addressed to the reader. Nothing of the
form "Stop asking X", "Use Y", "Implement Z". The three sentences that come closest each avoid the
imperative by a deliberate grammatical move:

- Laban 2505.06120 uses first-person performative address to a named third party: "**we call on**
  LLM builders to prioritize...". The authors are the subject; the reader is not.
- Huang 2310.01798 uses an impersonal passive with a modal: "equal effort **should be invested**".
  No agent is addressed.
- Lee 2201.06796 uses a first-person verb of invitation with a third-person object: "**We encourage
  fellow researchers to**...".

The same holds inside the body of the conclusions, not only at the end. Reading all 25 in full, no
conclusion contains a sentence-initial bare imperative to the reader. Huang's prescriptive material,
which is the most instruction-like passage in the corpus, is uniformly framed as "we encourage
future work...", "it is important to include...", "equal effort should be invested". Stechly's
2402.08115 prescription is framed as "**Our proposal**, based on the case studies we've performed in
this paper**, is**, when possible, to embed LLMs in systems which...".

The convention is unambiguous and the corpus is unanimous: **prescription is permitted, the
imperative mood is not.** The prescription is carried by a first-person verb ("we call on", "we
encourage", "our proposal is"), a modal with an impersonal subject ("should be", "deserves", "is
warranted"), or an implication clause ("our work motivates").

## Future work: where it lives and how it is worded

**Where.** Five papers give future work its own real estate outside the conclusion and then do not
repeat it: Pan 2308.03188 ("Research Gaps and Future Directions", a full section before the
conclusion), Kamoi 2406.01297 ("Future Directions", a full section before the conclusion), Laban
2505.06120 ("Implications", a full section before the conclusion), Wang 2309.10691 ("Limitations and
Future Work" in the appendix, with the conclusion's last sentence merely pointing at it), and Zhang
2310.02124, which folds it into the section title itself ("Conclusion and Future Work").

**How much.** 8 of 25 conclusions contain an explicit, substantive future-work statement
(2303.11366, 2304.05128, 2307.02762, 2309.10691, 2310.01798, 2310.02124, 2311.08516, 2402.08115). A
further 3 contain only a hope-statement (2303.17651, 2310.08491, 2405.01535). **7 of 25 contain no
forward gesture of any kind**: 2306.05685, 2306.09896, 2308.07201, 2310.12397, 2402.11436,
2406.01297, 2502.00640.

The pattern that matters here: **the papers reporting a negative or corrective finding are
disproportionately the ones that end without future work.** Stechly 2310.12397, Olausson 2306.09896,
Xu 2402.11436 and Kamoi 2406.01297 all close on the claim itself. A negative finding is a completed
result; gesturing at future work after it reads as softening the result.

**Wording, verbatim.** When future work is present it takes one of four forms and no others:

- Explicit plan, first person: "In the future, **we plan to** investigate how the general peer
  evaluation process benefits the LLMs..." (Li 2307.02762)
- Deferral: "**We leave** the development of more sophisticated methods **to future work**, and
  release our dataset BIG-Bench Mistake to encourage this direction of research." (Tyen 2311.08516);
  "**We consider** improving the model's ability to conduct all these steps **as important future
  work**." (Chen 2304.05128)
- Impersonal warrant: "Moving forward, a deeper exploration into the multi-agent society **is
  warranted**..." (Zhang 2310.02124)
- Hope: "**We hope that** our work could stimulate future work on using open-source LLMs as
  evaluators..." (Kim 2310.08491); "**We hope that** our work encourages more research on using
  open-source LMs as evaluators." (Kim 2405.01535); "**We hope that** our iterative approach will
  help drive further research in this area." (Madaan 2303.17651)

Huang 2310.01798 is the outlier and shows the cost of the alternative. Its "Conclusion and
Discussion" runs 575 words, of which 458 are three named prescriptions to the field, each with a
bold lead-in: "Leveraging external feedback for correction", "Evaluating self-correction against
baselines with comparable inference costs", "Putting equal efforts into prompt design". That is
four times the corpus median, and the paper pays for it by renaming the section.

## Earning a declarative title

Six papers in the corpus carry a title that is a declarative claim or a question demanding an
answer. What each does in the conclusion:

**Huang 2310.01798, "Large Language Models Cannot Self-Correct Reasoning Yet."** The conclusion does
**not** repeat the title. Its first sentence is: "Our work shows that current LLMs struggle to
self-correct their reasoning **without external feedback**." Three things are happening. The verb
softens from *cannot* to *struggle to*. A condition is attached ("without external feedback") that
the bare title omits. And the title's "Yet" is honoured by the next sentence: "This implies that
expecting these models to inherently recognize and rectify their reasoning mistakes is overly
optimistic **so far**."

The title claim in its hard form is asserted not in the conclusion but as a **body section heading**:
Section 3 is titled "LLMs Cannot Self-Correct Reasoning Intrinsically". The conclusion then states
the same claim in the qualified form the evidence supports, and spends the remaining 80% of its
words telling the field how to evaluate self-correction properly. **A declarative title is earned in
the section that reports the evidence; the conclusion states the qualified version and moves on.**

**Laban 2505.06120, "LLMs Get Lost In Multi-Turn Conversation."** The conclusion repeats the coined
phrase verbatim in its second sentence and immediately operationalizes it: "**LLMs get lost in
conversation**, which materializes as a significant decrease in reliability as models struggle to
maintain context across turns, make premature assumptions, and over-rely on their previous
responses." The phenomenon name is restated and then cashed out into the three concrete behaviours
that constitute it. It is not restated a second time, and it is not the final sentence.

**Tyen 2311.08516, "LLMs cannot find reasoning errors, but can correct them given the error
location."** The two-part title is restated as a two-part finding in the conclusion's second
sentence: "We find that LLMs generally struggle to find mistakes, but, when given mistake location
information, are able to correct outputs to boost performance." Same softening as Huang: *cannot*
becomes *generally struggle to*. The third sentence then converts the finding into a mechanism
claim: "We therefore hypothesise that mistake finding is an important bottleneck preventing
self-corrections strategies from performing well on reasoning tasks."

**Olausson 2306.09896, "Is Self-Repair a Silver Bullet for Code Generation?"** The title is a
question and the **final sentence answers it in the title's own words**: "Our results suggest that
self-repair **is not a silver bullet for code generation**, and that current models are held back by
their inability to reliably produce accurate and useful feedback on why the code is wrong." This is
the cleanest instance in the corpus of a conclusion closing the loop a title opened.

**Sharma 2310.13548, "Towards Understanding Sycophancy in Language Models."** The title's named
phenomenon appears twice in a 78-word conclusion ("we found sycophantic behavior across five AI
assistants"; "humans and preference models favoring sycophantic responses plays a role").

**Kamoi 2406.01297, "When Can LLMs Actually Correct Their Own Mistakes?"** The counter-example. Its
55-word conclusion does **not** answer its own title question; it describes what the survey did
("we categorize research questions and frameworks... and provide a checklist"). This is a survey and
the answer is the body of the paper, but the effect is that the title's question goes unanswered on
the last page.

**The pattern across all six.** A declarative title is earned by (i) restating the claim once, early
in the conclusion, (ii) in a *softened and conditioned* form the evidence supports, and (iii)
immediately attaching the mechanism or the condition that makes it true. Not one of them repeats the
title verbatim, and not one of them puts the title claim in the final sentence.

## Overlap with the abstract

Measured as the share of the conclusion's word 4-grams that also appear in the abstract, computed
over all 25 papers.

- Median: **3.1%**.
- Two papers share nothing: Shinn 2303.11366 and Wu 2502.00640 (0%).
- Four exceed 10%: Kamoi 2406.01297 (21.8%), Lee 2201.06796 (17.2%), Chen 2304.05128 (12.3%),
  Olausson 2306.09896 (10.2%).
- 14 of 25 share at least five 4-grams.

Reuse of the *concepts* is universal; reuse of the *wording* is minimal and, where it is high, it is
concentrated in proper nouns and dataset descriptions rather than in claim sentences (CoAuthor's
"63 writers and four instances of GPT-3 across 1445 writing sessions"; Chen's "improves the baseline
by 2-3%"; Kamoi, a 55-word conclusion where any repetition dominates the denominator). The two
papers with the highest genuine claim overlap, Olausson and Chen, are both repeating an experimental
setup phrase, not a claim.

Conclusion: **restating the abstract's claim in the abstract's words is not the convention.** The
same finding is stated again in fresh sentences that can afford to be blunter, because by the last
page the evidence is on the table.

## Limitations placement, and what it does to the conclusion

The current ARR Call for Papers, retrieved 2026-09-02 from https://aclrollingreview.org/cfp, states
verbatim that a long paper may consist of:

> up to eight (8) pages of content
>
> unlimited extra space **after the conclusion** for limitations (required, see below) and optional
> section on ethical considerations (we recommend it to be titled 'Ethical considerations')
>
> plus unlimited pages of references

and, under "Limitations (required section)":

> Authors are required to discuss the limitations of their work in a dedicated section titled
> "Limitations". This section should be included at the end of the paper, before the references, and
> it will not count toward the page limit. This includes both, long and short papers. Papers without
> a limitations section will be desk rejected.

The corpus bears this out. All six ACL-template papers place Limitations after the conclusion:
2311.08516 (Conclusion > Limitations), 2401.16745 (Conclusion > Limitations), 2402.11436 (Conclusion
> Acknowledgements > Limitations > Ethical Statement), 2405.01535 (Conclusion > Acknowledgements >
Limitations), 2310.02124 (Conclusion and Future Work > Limitations), 2505.06120 (Conclusion >
Limitations). Two ICLR papers do the same (2310.01798: Conclusion and Discussion > Limitations and
Broader Impact). Three papers place Limitations *before* the conclusion, all non-ACL formats
(2303.11366, 2303.17651, 2306.09896).

Three consequences for what an ARR conclusion can do:

1. **The conclusion is the last section inside the eight-page budget.** Every word in it competes
   with a table, a figure or a paragraph of results. Limitations and ethics are free; the conclusion
   is not. This is the strongest argument for the corpus median of ~106 words.
2. **Caveats do not belong in the conclusion, because there is a free section for them twelve lines
   later.** A hedge in the conclusion spends paid space to do a job that unpaid space is required to
   do anyway, and it blunts the claim in the process.
3. **The conclusion is not the reader's last impression of the paper.** Limitations is. A conclusion
   that pre-empts objections is arguing with a critic who is about to get a dedicated section
   anyway.

## Rules

Each rule states the evidence it rests on.

**R1. Target 100 to 140 words. Do not exceed 170.** Corpus median 106; ACL-template median 113.5;
15 of 25 under 120; no ACL-template conclusion above 138. The three conclusions above 200 words are
all non-ACL formats and one of them renames the section to license the length.

**R2. One paragraph. Two only if the second does distinct work.** 21 of 25 are a single paragraph;
five of the six ACL-template conclusions are. Where a second paragraph exists it carries a separate
object: Tyen's second paragraph is about the trained classifier, a different contribution from the
first paragraph's finding.

**R3. Open with the claim, not with "In this paper, we...", when the paper's result is negative.**
20 of 25 use the summary frame, but the five that do not include every paper whose conclusion
carries a claim rather than a summary: Huang ("Our work shows that..."), Sharma ("Despite the clear
utility of human feedback data..."), Wu, Kwan, Zhang. A paper whose title is a declarative claim has
already promised a claim; opening on a procedural summary defers it.

**R4. Restate the finding qualitatively. Carry at most one number, and only if it is the number the
title depends on.** 16 of 25 restate qualitatively; only 4 use any result statistic; **zero of the
five negative-result papers use one**. Statistical apparatus (p-values, confidence intervals, sample
sizes, panel descriptions) appears in **no conclusion in the corpus**. Not one of the 25 contains a
p-value.

**R5. State the claim in its conditioned form, not its title form.** Huang softens "Cannot" to
"struggle to" and adds "without external feedback". Tyen softens "cannot find" to "generally struggle
to find" and keeps "given mistake location information". The conditioned form is the defensible one,
and it is also the one that says something.

**R6. Name the paper's phenomenon once, and cash it out immediately.** Laban: "LLMs get lost in
conversation, which materializes as a significant decrease in reliability as models struggle to
maintain context across turns, make premature assumptions, and over-rely on their previous
responses." Sharma names sycophancy twice in 78 words. Naming without operationalizing is the
failure mode.

**R7. Never end on an imperative addressed to the reader.** 0 of 25. If a prescription belongs in
the conclusion, carry it with a first-person verb ("we call on", "we encourage", "our proposal is"),
a modal with an impersonal subject ("should be invested", "deserves", "is warranted"), or an
implication clause ("our work motivates the development of").

**R8. Choose one closing move and commit to it.** The corpus distribution: attributed knowledge
claim 5, future-work gesture 5, call to the community 5, artifact release 4, broader implication 3,
contribution restatement 1, positioning 1, pointer 1. For a paper reporting a negative finding with
a declarative title, the two live options are the attributed knowledge claim (Olausson, Xu) and the
call to a named third party (Laban). Do not stack three closing moves in three consecutive
sentences.

**R9. If future work already has a home elsewhere, do not repeat it here.** Pan, Kamoi, Laban and
Wang all give it a section and keep it out of the conclusion; Wang's last sentence is a bare
cross-reference. 7 of 25 conclusions contain no forward gesture at all, and four of those seven are
the corpus's negative-result papers.

**R10. No citations, no new evidence, no new construct.** 22 of 25 cite nothing. The three that cite
are a survey-adjacent framework proposal (2402.08115), a paper that renamed its section "Conclusion
and Discussion" (2310.01798), and one incidental reference (2307.02762). New material in a
conclusion is acceptable only when the section title announces that it is more than a conclusion.

**R11. Restate the claim in fresh words, not the abstract's words.** Median 4-gram overlap with the
abstract is 3.1%; two papers share nothing at all. The high-overlap cases are repeating setup
descriptions, not claims.

**R12. Put no caveat, hedge or anticipated objection in the conclusion.** ARR requires a Limitations
section immediately after it, outside the page limit, and the CFP states that section "should not
introduce new methods, analysis, or results" but exists precisely to hold the caveats. A hedge here
spends paid page space to weaken the claim.

**R13. Do not address separate audiences in parallel clauses.** No conclusion in the corpus
addresses more than one audience, and none uses a "For X... For Y... For Z..." construction. Laban,
the only paper that names an audience, names exactly one ("LLM builders") and names it once.

## Constructions to avoid, with evidence

**"For users, ... For organizations, ... For the field, ..."** Zero instances of a multi-audience
parallel construction across 25 conclusions. It is a slide-deck move. Laban 2505.06120 shows the
convention: one audience, named once, in the same clause as the ask.

**Sentence-initial bare imperatives ("Stop asking...", "Evaluate first...", "Implement...").** Zero
instances across 25 conclusions, at any position, not only the final sentence.

**p-values, confidence intervals and test statistics.** Zero instances across 25 conclusions. Four
conclusions carry a percentage or a ratio; none carries an inferential statistic. A conclusion that
reads "(-0.74 levels on stripped content, balanced panel, p = 1.01e-4)" is reporting a results table
on the last page.

**Self-assessment of the work's importance.** Kwan 2401.16745 ("MT-Eval represents an important
first step... it also paves the way for further efforts") and Chan 2308.07201 ("thereby
demonstrating the reliability and efficacy of our framework") are the corpus's two weakest closings
precisely because the sentence's job is to tell the reader the work is good. Compare Olausson's
final sentence, which states a fact about models and lets the reader draw the assessment.

**Repeating the title verbatim.** Zero instances. Huang, Tyen, Laban and Olausson all restate the
title claim in altered words. A verbatim repeat reads as having nothing further to say.

**Hedged prescription stacked on hedged prescription.** Huang's 575-word conclusion is the only one
in the corpus that stacks three named prescriptions, and it renames itself "Conclusion and
Discussion" to do so. If three prescriptions are needed, they belong in the discussion.

**Announcing the section's own structure** ("The fix is...", "The implication is...", "In sum").
None of the 25 uses a meta-label to introduce its own claim. The claim is simply stated.

## Checklist

Before the conclusion is finished, all of these must be true.

- [ ] 100 to 140 words; hard ceiling 170.
- [ ] One paragraph, or two where the second carries a distinct contribution.
- [ ] First sentence states the finding, not the procedure, and not "In this paper we...".
- [ ] The title's claim is restated exactly once, in its conditioned form, with the condition that
      makes it true attached in the same sentence.
- [ ] Zero p-values. Zero confidence intervals. Zero sample sizes. At most one number, and only if
      the claim cannot be stated without it.
- [ ] Zero citations.
- [ ] Nothing appears here that has not already appeared in the results or discussion.
- [ ] No caveat, no hedge, no anticipated objection: those belong in Limitations, which follows and
      is free.
- [ ] Wording is fresh, not lifted from the abstract.
- [ ] Exactly one closing move, in one sentence.
- [ ] The final sentence is not an imperative and does not address the reader as "you".
- [ ] No more than one audience is named, and only if naming it is the closing move.
- [ ] No sentence whose job is to say the work is important.

## How this paper's current conclusion measures up

Assessed against `paper/sections/conclusion.tex` as of 2026-09-02. It is 168 words in 2 paragraphs
and 7 sentences.

**Length.** 168 words puts it above the corpus median of 106 and above every ACL-template
conclusion in the corpus (highest: 138). Only 5 of 25 papers are longer, and three of those are
formats with no page limit pressure. Against R1 it is roughly 30 words over. Trim to ~130.

**Sentence 1 opens on the finding, which is right.** "When LLMs are given repeated undirected
revision opportunities, most decline to genuinely revise..., and those that do revise get worse."
This is the Huang/Sharma opening and it suits a paper with a declarative title. Keep it.

**Sentence 2 is a results table.** "The revision cliff is real (-0.74 levels on stripped content,
balanced panel, p = 1.01 x 10^-4), consistent across task domains, and costly (62.1% of output
tokens wasted, with the quality-optimal stopping point at Turn 1 for all six models tested)." No
conclusion in the corpus of 25 contains a p-value, a panel description or a stripping condition.
Four contain any result statistic at all, and none of the five negative-result papers contains one.
The phrase "is real" is also doing defensive work, answering a doubt the reader has not raised.
Against R4 and R12, this sentence should carry the finding qualitatively and drop the parentheses:
the size, the panel and the p-value are the results section's job.

**The 1.16 result is the paper's title claim and currently arrives fourth, wrapped in another
p-value.** "Intrinsic Self-Correction Requires Extrinsic Direction" is a claim about *direction*.
The directed-critique result is what earns it. Following Huang and Tyen, this belongs in the first
or second sentence, stated as the conditioned claim, without the statistics: models revise
effectively when told what is wrong and degrade their work when they are not.

**The close is the largest departure from the convention.** The last three sentences are:

> For organizations, the implication is to implement quality gates before revision loops. For users,
> the implication is to stop asking "can this be improved?" and start specifying what is wrong. For
> the field, the implication is that multi-turn revision robustness deserves evaluation alongside
> single-turn capability.

Three problems, each with a count behind it.

1. **The three-audience parallel construction appears zero times in 25 conclusions.** No paper in
   this literature addresses organizations, users and the field in consecutive clauses. Laban is the
   only paper that names an audience at all, and it names one.
2. **The middle sentence is an instruction to the reader** ("stop asking... and start specifying"),
   which is the construction that occurs zero times in 25 conclusions in any position. The infinitive
   framing ("the implication is to stop asking") does not change the register; it is still telling
   the reader what to do.
3. **Three closing moves are stacked**, so none of them is the close. Against R8, one move should
   carry it.

The third sentence, on revision robustness deserving evaluation alongside single-turn capability, is
the closest thing here to a corpus-conventional ending: it is an impersonal modal ("deserves"),
directed at the research community, and it is the claim the paper is best placed to make to an ARR
audience. It is also the discussion's third paragraph in compressed form, which is where it already
lives.

**Suggested shape**, matching Laban's and Olausson's closings, for the author to write in his own
words: two sentences of finding (undirected revision degrades output and mostly does not happen at
all; a single targeted critique reverses both), one sentence naming the mechanism the title asserts
(the constraint is direction, not capacity), one closing sentence in the Laban form (a first-person
call, or an impersonal modal, addressed to one audience, on evaluating revision robustness alongside
single-turn capability). Roughly 130 words, one paragraph, no parentheses, no statistics.

**One format issue outside the conclusion itself, but bearing on it.** `paper/sections/discussion.tex`
ends with `\section{Limitations}`, and `main.tex` inputs `discussion` before `conclusion`. The
Limitations section is therefore currently *before* the conclusion and *inside* the eight-page
budget. The ARR CFP (retrieved 2026-09-02, https://aclrollingreview.org/cfp) states that the free
space is "after the conclusion" and that the section "should be included at the end of the paper,
before the references". Moving Limitations after the conclusion recovers roughly a third of a page
of body text and complies with the stated placement. It also changes what the conclusion has to do:
once Limitations follows it, the conclusion has no reason to hedge at all.
