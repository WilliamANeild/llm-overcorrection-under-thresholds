# Rules: Introduction

Retrieved 2026-09-02. 23 introductions read in full. Every rule names its evidence.

**Method.** Each paper was fetched as arXiv LaTeXML HTML (`arxiv.org/html/<id><version>`), the
`<section>` element whose heading matched "Introduction" was isolated, and paragraphs, list
items, figure captions, citation anchors (`href="#bib.bib*"`) and cross-references were counted
mechanically rather than by eye. Word counts exclude figure captions. Citation counts are
**individual bibliography references**, not citation groups: `(Madaan et al., 2023; Huang et al.,
2024)` counts as two, which is the number the advisor's "sea of blue" test is about. Every
quotation below was re-verified against the extracted text by string match before being written
here.

**Coverage and limits.** All 23 papers were reached in HTML and all 23 introductions were read in
full. No paywall was encountered. Three limits worth stating. (1) The corpus is arXiv-only,
because ACL Anthology serves PDFs whose paragraph structure cannot be counted reliably; the
consequence is that camera-ready introductions may differ slightly from the version counted here,
so the arXiv version is recorded for every paper. (2) Venue is reported only where the arXiv record states one; where it does not, the table says so
rather than guessing, so the ACL-venue comparisons below rest on the five confirmed cases. (3)
Saunders et al. carries no venue in its arXiv record and reads as a laboratory technical report; it
is included because it is the origin of the "recognizing errors is easier than avoiding them"
premise that Kamoi's opening sentence cites, and its 11-paragraph structure is flagged as an
outlier wherever it affects a count.

---

## Corpus

| # | First author, short title | arXiv ID (version) | Venue *(as stated in arXiv metadata)* | Body paras | List items | Words | Citations | Cites/100w | Beats present |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Lee, CoAuthor | 2201.06796 v2 | CHI 2022 | 6 | 0 | 721 | 21 | 2.9 | field, problem, prior, gap, approach, results, contrib(prose) |
| 2 | Saunders, Self-critiquing models | 2206.05802 v2 | not stated | 11 | 0 | 745 | 17 | 2.1 | field, problem, prior, approach, contrib(numbered prose) |
| 3 | Lee, Evaluating Human-LM Interaction (HALIE) | 2212.09746 v5 | not stated (Stanford CRFM) | 6 | 4 | 911 | 25 | 2.7 | field, gap, problem, approach, results, contrib(list) |
| 4 | Shinn, Reflexion | 2303.11366 v4 | not stated | 6 | 4 | 672 | 10 | 1.5 | field, prior, gap, approach, results, contrib(list) |
| 5 | Madaan, Self-Refine | 2303.17651 v2 | not stated | 4 | 0 | 570 | 13 | 2.3 | problem, prior, gap, field, approach, results |
| 6 | Zheng, Judging LLM-as-a-Judge (MT-Bench) | 2306.05685 v4 | NeurIPS 2023 Datasets and Benchmarks Track | 6 | 0 | 664 | 21 | 3.2 | field, problem, approach, prior, gap, results, contrib(prose) |
| 7 | Pan, Automatically Correcting LLMs (survey) | 2308.03188 v2 | not stated ("Work in Progress") | 5 | 0 | 676 | 53 | 7.8 | field, problem, prior x3, gap, roadmap |
| 8 | Wei, Simple synthetic data reduces sycophancy | 2308.03958 v2 | not stated | 5 | 0 | 473 | 15 | 3.2 | field, problem, approach, results (no gap sentence) |
| 9 | Huang, LLMs Cannot Self-Correct Reasoning Yet | 2310.01798 v2 | ICLR 2024 | 6 | 0 | 638 | 36 | 5.6 | field, prior, gap, approach, results x3, implication |
| 10 | Stechly, GPT-4 Doesn't Know It's Wrong | 2310.12397 v1 | not stated | 5 | 0 | 705 | 16 | 2.3 | field, prior, gap, approach, results x2, roadmap |
| 11 | Sharma, Towards Understanding Sycophancy | 2310.13548 v4 | not stated | 6 | 0 | 651 | 16 | 2.5 | field, prior, gap, approach+results x4, implication |
| 12 | Shridhar, The ART of LLM Refinement | 2311.07961 v1 | not stated | 3 | 0 | 474 | 17 | 3.6 | field, prior, gap, results, approach |
| 13 | Tyen, LLMs cannot find reasoning errors | 2311.08516 v3 | **ACL 2024 Findings** | 7 | 4 | 594 | 16 | 2.7 | field, prior x2, gap/move, results x2, contrib(list) |
| 14 | Kwan, MT-Eval | 2401.16745 v1 | not stated | 5 | 4 | 517 | 4 | 0.8 | field, problem, gap, approach x2, results, contrib(list) |
| 15 | Bai, MT-Bench-101 | 2402.14762 v3 | **ACL 2024** | 5 | 4 | 580 | 14 | 2.4 | field, prior, gap, approach x3, findings(list) |
| 16 | Lin, CriticBench | 2402.14809 v4 | **ACL 2024 Findings** | 4 | 5 | 513 | 25 | 4.9 | field, prior, gap, approach, contrib(list) |
| 17 | Chiang, Chatbot Arena | 2403.04132 v1 | not stated | 8 | 4 | 799 | 7 | 0.9 | field, problem, prior, gap, problem, approach, results, contrib(list) |
| 18 | Shankar, Who Validates the Validators? (EvalGen) | 2404.12272 v1 | not stated | 6 | 0 | 788 | 18 | 2.3 | field, prior, gap, approach x2, results, roadmap |
| 19 | Panickssery, LLM Evaluators Recognize Their Own Generations | 2404.13076 v1 | not stated | 5 | 4 | 425 | 18 | 4.2 | field, problem, gap/question, approach, findings(list) |
| 20 | Kamoi, When Can LLMs Actually Correct Their Own Mistakes? | 2406.01297 v3 | **TACL 2024**, 12: 1417-1440 | 8 | 5 | 659 | 21 | 3.2 | field, prior, gap, approach, results, RQ list, roadmap |
| 21 | Liu, RM-Bench | 2410.16184 v1 | not stated | 5 | 0 | 775 | 27 | 3.5 | field, problem/desiderata, prior, gap, approach, results |
| 22 | Sirdeshmukh, MultiChallenge | 2501.17399 v2 | not stated | 5 | 0 | 585 | 13 | 2.2 | field, problem, prior, gap, approach x2, results |
| 23 | Laban, LLMs Get Lost In Multi-Turn Conversation | 2505.06120 v1 | not stated | 8 | 0 | 651 | 8 | 1.2 | field, problem, prior, gap, approach x3, implication, roadmap |

*Venue is reported only where the arXiv listing states it (the `Comments` or `Journal ref` field),
checked 2026-09-02. "Not stated" means the arXiv record gives no venue; several of these papers
have since appeared at conferences, but that was not verified here and is not asserted. First
authors and titles were read from the fetched HTML of each paper. Five venues are confirmed as
ACL-family or ACL-adjacent: Tyen (ACL 2024 Findings), Bai (ACL 2024), Lin (ACL 2024 Findings),
Kamoi (TACL 2024), plus Huang (ICLR 2024), Zheng (NeurIPS 2023 D&B) and Lee (CHI 2022).*

**Distribution.**

| Measure | Min | Median | Mean | Max |
|---|---|---|---|---|
| Words (excl. figure captions) | 425 | **651** | 643 | 911 |
| Body paragraphs | 3 | **6** | 5.9 | 11 |
| Blocks (paragraphs + list items) | 3 | 6 | 7.5 | 13 |
| Citations (individual references) | 4 | **17** | 18.7 | 53 |
| Citations per 100 words | 0.8 | **2.7** | 3.0 | 7.8 |
| Words per paragraph | 47 | 95 | 96 | 158 |

---

## The beat structure (with counts)

Eight functions were labelled paragraph by paragraph across all 23 papers. A paragraph can carry
two beats; the counts below are papers in which the beat appears at all.

| Beat | Papers | Where it sits |
|---|---|---|
| **Field** (what area this is, what it does well) | 23/23 | Always paragraph 1, usually its first sentence |
| **Prior work** (named, argued, not listed) | 23/23 | Paragraph 1 in 12 papers, paragraph 2 in 8 |
| **Problem** (the thing that motivates the study) | 15/23 | Paragraph 1 or 2 |
| **Gap** (an explicit sentence saying what is not settled) | 22/23 | Paragraph 1 in 8, paragraph 2 in 9, paragraph 3 in 5 |
| **Approach** ("In this work, we…") | 23/23 | Block 2 or 3 in 19 of 21 papers with an identifiable pivot |
| **Results previewed** | 21/23 | Second half of the introduction, always |
| **Contributions enumerated** | 12/23 | Final block, never earlier |
| **Roadmap** ("the rest of the paper…") | 5/23 | Final paragraph |

**The canonical order, present in 19 of 23 papers:**
field → prior work → gap → approach → results → (contributions).

**Where the pivot to "what we did" sits.** 21 of 23 papers contain an identifiable
first-person method pivot. In 19 of them it falls in **block 2 or block 3** of the introduction.
Fixed phrasings, counted: `In this paper/work, we` (8 papers), `To this end` / `To bridge
the/this gap` / `To address this` (6), `To study this` (2), `We therefore` (1), `We develop /
propose / study` unprefaced (4). Two papers have no pivot: Pan's survey (2308.03188) and Tyen
(2311.08516), which reaches its move by a contrast sentence instead ("While previous work
typically present self-correction as a single process, we divide it into…").

**Where the field is named.** Every paper names its area in the first two sentences, by a noun
phrase in subject position rather than by a claim about importance. Counted usages across the
corpus: `human-LM interaction` / `human-LLM interaction` (7), `interaction design` / `the HCI
community` (9), `LLM-as-a-judge` (7), `self-correction research` (5), `scalable oversight` (2),
`reward model` (29, in one paper). The two most transferable models for a paper that must
situate itself in human-AI interaction:

- HALIE (2212.09746, P2): *"Our goal is to evaluate human-LM interaction instead of just model
  completions."*
- CoAuthor (2201.06796, P3): *"In this paper, we investigate how HCI researchers can examine LMs'
  generative capabilities to inform interaction design."*

**Negative-result papers frame positively by relocating the claim, not by attacking prior work.**
Six papers in the corpus report a negative or deflationary result (Huang 2310.01798, Stechly
2310.12397, Tyen 2311.08516, Kamoi 2406.01297, Sharma 2310.13548, Laban 2505.06120). None
disparages the work it revises. Three moves recur:

1. **Attribute the optimism, then bound it rather than deny it.** Huang: *"Contrary to the
   optimism surrounding self-correction (Madaan et al., 2023; Kim et al., 2023; Shinn et al.,
   2023; Pan et al., 2023, inter alia), our findings indicate that LLMs struggle to self-correct
   their reasoning in this setting."* The scope-fence is "in this setting," and the optimists are
   cited by name in the same sentence that limits them.
2. **Locate the discrepancy in a condition, not in an error.** Huang again: *"we observe that the
   improvements in these studies result from using oracle labels to guide the self-correction
   process, and the improvements vanish when oracle labels are not available."* The prior result
   stands; what changes is what it was measuring.
3. **Convert the negative into a positive object of study.** Tyen splits self-correction into two
   named components so the negative result attaches to one of them and a positive result attaches
   to the other: mistake finding fails, output correction succeeds given the mistake location.
   Kamoi converts the whole conflict into a taxonomy: *"These conflicting observations indicate
   that further analysis of self-correction is needed."*

---

## Verbatim catalogue of gap statements (all 23, quoted exactly)

Each entry is the sentence or short run of sentences that does the gap work, transcribed from the
version named in the corpus table and verified by string match. Where the gap depends on a
preceding scope-fence, the fence is included.

**1. CoAuthor, 2201.06796 v2, paragraph 2 → 3.**
> "Answers to such questions guide early interaction design process. Without them, envisioning how
> an LM may serve writers' needs—or when and how it may fall short—becomes a shot in the dark."
> … "Examining such variable capabilities requires more than interviewing its users (Yang et al.,
> 2019) or tinkering with the model."

*Construction: a conditional absence ("Without them…"), then a "requires more than X or Y"
sentence that names the two existing methods and declines to call either wrong.*

**2. Saunders et al., 2206.05802 v2, paragraph 2.**
> "However, fully evaluating correctness of code or veracity of facts about the world requires a
> lot of effort and expertise. Techniques to train systems from human feedback [NR+00, Wes16,
> CLB+17, JMD20, NMS+21, SCC+22], fundamentally depend on humans' ability to demonstrate and
> evaluate the quality of model outputs. This leads to the problem of scalable oversight [AOS+16]:
> How can we effectively provide feedback to models on tasks that are difficult for humans to
> evaluate?"

*Construction: the gap is stated as a named, cited problem in the field, then restated as a
question. Not "nobody has done X" but "this is the field's open problem, here it is."*

**3. HALIE, 2212.09746 v5, paragraphs 1 and 2.**
> "However, these models are at present primarily evaluated non-interactively: given an input
> text, a model generates a completion with the focus solely on the quality of the completion.
> We are interested in building a unified evaluation framework for human-LM interaction (where
> dialogue is a subset) that is inspired by, but also extends beyond dialogue systems. Almost all
> benchmarks, even those with a diverse range of tasks, such as GEM (Gehrmann et al., 2021) and
> HELM (Liang et al., 2022), encode this non-interactive view."
> … "But as a community, if we explicitly or implicitly optimize for non-interactive performance,
> will this improve interactive performance?"

*Construction: "at present primarily," which concedes exceptions without listing them, then the
exceptions are conceded anyway in a footnote. The gap closes as a first-person-plural question
addressed to the field.*

**4. Reflexion, 2303.11366 v4, paragraph 1.**
> "Since they rely on massive models with an enormous number of parameters, such approaches have
> been so far limited to using in-context examples as a way of teaching the agents, since more
> traditional optimization schemes like reinforcement learning with gradient descent require
> substantial amounts of compute and time."

*Construction: "have been so far limited to," which states a constraint on prior work rather than
a failure of it, and gives the reason in the same sentence.*

**5. Self-Refine, 2303.17651 v2, paragraph 1.**
> "Iterative refinement typically involves training a refinement model that relies on
> domain-specific data (e.g., Reid and Neubig (2022); Schick et al. (2022a); Welleck et al.
> (2022)). Other approaches that rely on external supervision or reward models require large
> training sets or expensive human annotations (Madaan et al., 2021; Ouyang et al., 2022), which
> may not always be feasible to obtain. These limitations underscore the need for an effective
> refinement approach that can be applied to various tasks without requiring extensive
> supervision."

*Construction: two sentences of cited prior work, each ending in a cost, then one sentence that
converts the two costs into a requirement. The requirement is the design brief for the method.*

**6. MT-Bench, 2306.05685 v4, paragraphs 2 and 4.**
> "This misalignment of conventional benchmarks underscores the core problem driving this paper:
> the need for a robust and scalable automated method to evaluate LLM alignment with human
> preferences."
> … "This approach has been tried in our earlier blog post [8] and other concurrent or follow-up
> work [5, 29, 14, 12, 52, 18, 33, 40, 7, 43]. However, there has not been a systematic study of
> this approach."

*Construction: the strongest negative in the corpus ("there has not been a systematic study") is
made safe by the sentence before it, which cites ten pieces of work doing the thing. The claim is
about the absence of a study, not the absence of the practice.*

**7. Pan et al., 2308.03188 v2, paragraph 3.**
> "However, this approach has two primary drawbacks: it can be costly due to the manual labor
> involved, and it lacks real-time capabilities as humans cannot provide instant feedback."

*Construction: a survey's gap is a property of a method, enumerated, with no claim about what
anyone has failed to do.*

**8. Wei et al., 2308.03958 v2 — no gap sentence.**
The only paper in the corpus with no sentence that states what is unsettled. Its paragraph 1
motivates by consequence instead: *"As these models may one day be able to solve problems that
humans cannot solve, it is important to ensure that models are aligned and avoid reward hacking
(Amodei et al., 2016; Saunders et al., 2022; Bowman et al., 2022)…"* It is also the shortest
introduction in the corpus (473 words) and one of two with no contributions list and no roadmap.

**9. Huang et al., 2310.01798 v2, paragraph 2.**
> "However, the underlying mechanics and efficacy of self-correction in LLMs remain underexplored.
> A fundamental question arises: If an LLM possesses the ability to self-correct, why doesn't it
> simply offer the correct answer in its initial attempt?"

*Construction: "remain underexplored" alone would be weak; the question that follows is what does
the work, because it is answerable and it exposes a tension inside the prior claim rather than
outside it.*

**10. Stechly et al., 2310.12397 v1, paragraph 1.**
> "This belief seem to rest largely on the assumption that verification of correctness should be
> easier than generation for many reasoning problems–a rather classical argument from
> computational complexity. There are grounds to be skeptical of this assumption as complexity of
> the reasoning task should be irrelevant to LLM performance if what they are doing is approximate
> retrieval."

*Construction: the gap is an unexamined assumption, named, attributed to the belief rather than to
any author, then given a reason to doubt. No one is said to be wrong.*

**11. Sharma et al., 2310.13548 v4, paragraph 1.**
> "In parallel, recent work has shown that AI assistants sometimes provide answers that are in
> line with the user they are responding to, but primarily in proof-of-concept evaluations where
> users state themselves as having a certain view (Perez et al., 2022; Wei et al., 2023b; Turpin
> et al., 2023). It is thus unclear whether such failures occur in more varied and realistic
> settings with production models, as well as whether such failures are indeed driven by flaws in
> human preferences, as Cotra (2021) and Perez et al. (2022) hypothesize."

*The cleanest model in the corpus for this paper. The gap is built in two moves: a scope-fence on
prior work ("but primarily in proof-of-concept evaluations where…") followed by "It is thus
unclear whether." The fence names the exact condition prior work ran under, so the gap is a
consequence of the fence rather than an assertion about the literature.*

**12. ART, 2311.07961 v1, paragraph 1.**
> "Developing models that consistently evaluate and correct their errors would be a valuable step
> towards building more reliable language models."

*Construction: gap as a stated desideratum, in the conditional. The shortest form in the corpus.*

**13. Tyen et al., 2311.08516 v3, paragraph 4.**
> "While previous work typically present self-correction as a single process, we divide it into
> mistake finding and output correction to better understand each component individually."

*Construction: the gap and the contribution are one sentence. Prior work is characterized by what
it treats as unitary, not by what it gets wrong, and the paper's move is the decomposition.*

**14. MT-Eval, 2401.16745 v1, paragraph 1.**
> "The ability of LLMs to engage in multi-turn conversations is often overlooked in existing
> evaluation frameworks. For instance, MMLU (Hendrycks et al., 2020) evaluates language
> understanding in multiple tasks using single queries, and MT-Bench (Zheng et al., 2023b)
> evaluates conversational ability using two-turn interactions without considering more turns and
> various conversation types."

*Construction: "often overlooked" is hedged and would be unfalsifiable alone; the "For instance"
sentence that follows names two benchmarks and says exactly what each does, which is what makes
the claim checkable.*

**15. MT-Bench-101, 2402.14762 v3, paragraph 1.**
> "Early studies like MT-bench Zheng et al. (2024) mainly focus on two-turn dialogues and
> coarse-grained abilities, not sufficiently covering the complexity of real-world multi-turn
> dialogue scenarios. This indicates a considerable scope for improvement in current benchmarks
> for multi-turn dialogues, underscoring the urgent need to develop a comprehensive benchmark that
> can effectively compare the chat abilities of LLMs in multi-turn dialogues."

**16. CriticBench, 2402.14809 v4, paragraph 2.**
> "However, a comprehensive understanding of LLMs' critical reasoning abilities remains elusive.
> Prior research (Lightman et al., 2023; Li et al., 2024; Luo et al., 2024) has focused on a narrow
> range of models and datasets and has yielded inconsistent findings (Madaan et al., 2023; Huang
> et al., 2024), underscoring the need for a thorough investigation."

*Construction: the gap is the inconsistency between two cited camps, which is the same structure
Kamoi uses. Note that the papers reported as inconsistent are cited in the sentence that says so.*

**17. Chatbot Arena, 2403.04132 v1, paragraph 3.**
> "Consequently, current benchmarks fail to adequately address the needs of state-of-the-art LLMs,
> particularly in evaluating user preferences. Thus, there is an urgent necessity for an open,
> live evaluation platform based on human preference that can more accurately mirror real-world
> usage."

*Construction: three enumerated limitations in the preceding sentences ("Firstly… Secondly…
Furthermore…"), then "Consequently" and "Thus." The gap is derived, not asserted.*

**18. EvalGen, 2404.12272 v1, paragraph 2.**
> "Yet many existing systems do not include support for verifying the quality of LLM-generated
> evaluations, asking users to simply trust these outputs. How can users reap the efficiency
> benefits of LLM-assisted evaluation of LLM outputs, while minimizing or avoiding misalignment?
> How can we help users validate the validators?"

*Construction: a quantified claim about existing systems ("many," not "no"), then two questions,
the second of which is the paper's title.*

**19. Self-Recognition, 2404.13076 v1, paragraph 3.**
> "Towards understanding and mitigating self-preference, we study self-recognition—an LLM's
> capability of recognizing its own outputs. We ask: Is self-preference truly self-preference, in
> the sense that the LLM prefers a text because it was generated by itself?"

*Construction: no negative claim about the literature at all. The gap is a question about the
interpretation of an accepted finding.*

**20. Kamoi et al., 2406.01297 v3, paragraphs 1 and 2.**
> "However, recent studies also report negative results indicating that LLMs cannot self-correct
> (Huang et al., 2024a; Gou et al., 2024; Li et al., 2024b; Chen et al., 2024f) or even self-detect
> (Chen and Shu, 2024; Tyen et al., 2024; Hong et al., 2024; Jiang et al., 2024; Kamoi et al.,
> 2024) their own mistakes at least in certain conditions. These conflicting observations indicate
> that further analysis of self-correction is needed."
> … "First, our analysis finds that prior studies often do not define their research questions in
> detail. As a result, many papers fail to provide appropriate experiments to evaluate the research
> questions they implicitly target."

*The strongest negative in the corpus appears later, in paragraph 3, and is fenced twice: "In
general tasks, no prior work shows reliable evidence of successful self-correction with in-context
learning." Note "in general tasks" and "reliable evidence." Kamoi never writes an unfenced "no
prior work."*

**21. RM-Bench, 2410.16184 v1, paragraphs 2 and 3.**
> "Despite their significance, benchmarks for reward models remain under-explored compared to the
> rapid advancements in aligned language model evaluation, namely the policy model (Hendrycks et
> al., 2020; bench authors, 2023; Chiang et al., 2024; Hendrycks et al., 2021)."
> … "However, to reduce construction costs, they often use a stronger LM to generate the better
> response and a weaker LM for the worse response. This design makes it difficult to assess a
> reward model's sensitivity to subtle changes, as the responses are generated by different LMs."

*Construction: the gap is a design consequence of prior work, with the reason prior work made that
choice stated sympathetically ("to reduce construction costs") before the consequence.*

**22. MultiChallenge, 2501.17399 v2, paragraph 2.**
> "Some of them, such as the widely adopted MT-Bench (Zheng et al., 2023), are saturated by
> frontier LLMs with near-perfect results (Achiam et al., 2023; Yang et al., 2024). Others (He et
> al., 2024) focus more on multi-turn explicit instruction following, missing the opportunity to
> assess the actual set of mixed model capabilities required in conducting natural multi-turn
> conversations with human users."

*Construction: "Some of them… Others…", which partitions the prior work exhaustively and gives
each partition its own limitation. The partition is what makes the gap non-arbitrary.*

**23. Laban et al., 2505.06120 v1, paragraphs 1 and 2.**
> "Though studies of LLM conversation logs have confirmed that underspecification in user
> instructions is prevalent [27], LLM systems are typically evaluated in single-turn,
> fully-specified settings."
> … "Even though a growing body of work proposes to evaluate LLMs in a multi-turn fashion, we
> identify in our review (Section 2) that most prior work treats the conversation as episodic:
> conversation turns might relate to each other, but the conversation can effectively be decomposed
> as an array of subtasks that can be evaluated in isolation. We argue that episodic tasks move
> away from what is prevalent in human conversation: underspecification [91, 27]."

*The second-cleanest model for this paper. Three properties worth copying: (a) "we identify in our
review (Section 2)", which makes the gap a reported finding of the paper's own related-work
section rather than an unsupported claim; (b) "most prior work," never "no prior work"; (c) the
gap is a property of the prior designs ("episodic") given a name, so the paper's contribution is
the complement of that name.*

### What the catalogue shows

| Feature | Count |
|---|---|
| Gap stated with `However,` at sentence start | 16 uses across 11/23 papers |
| Gap or contrast opened with `While` / `Although` / `Though` / `Even though` / `Despite` | 8 uses in 7/23 |
| `Yet` or `But` sentence-initial | 3 uses in 2/23 |
| `remain(s) underexplored / elusive / unclear` | 3 uses in 3/23 |
| `no prior work` / `to our knowledge` / `there has not been` | 4 uses in 3/23, **all four scope-fenced** |
| `the need for` / `urgent necessity` / `underscores the need` | 8 uses in 8/23 |
| The literal word `gap` | 5 uses in 3/23 |
| Gap closed as a **question** rather than a statement | 6/23 (Saunders, HALIE, MT-Bench premise, EvalGen, Panickssery, Huang) |

**The dominant construction is not a negative claim about the literature.** It is a two-sentence
pair: sentence one states what prior work does *and the condition it does it under*; sentence two
says that a different condition is therefore unsettled. Sharma, Laban, RM-Bench, MultiChallenge
and MT-Eval all use exactly this. The fence is in the first sentence, which is why the second can
be short and flat.

---

## Citation density rules

**The advisor's "sea of blue" is real, and it is concentrated.**

| Measure | Value |
|---|---|
| Citations per introduction, median | **17** (mean 18.7, range 4 to 53) |
| Citations per 100 words, median | **2.7** (mean 3.0) |
| Citations in paragraph 1, median | **9** |
| Median share of a paper's introduction citations landing in paragraph 1 | **47%** |
| Median share landing in the **first half** of the blocks | **88%** (mean 81%) |
| Blocks with **zero** citations | 98 of 173 (**57%**) |
| Papers whose final block has zero citations | 18/23 |

**The claim that the introduction is sparse and argumentative while related work is dense and
taxonomic is confirmed.** Citation density was computed for the Related Work / Background section
of every paper that has one (21 of 23; MT-Bench and Pan's survey have no such section).

| | Median cites/100 words |
|---|---|
| Introduction | 2.5 |
| Related Work / Background | **6.3** |

Related work is denser than the introduction in **19 of 21** papers, at a median ratio of
**2.8×**. Extremes: Chatbot Arena 7.7× (0.9 vs 6.8), Laban 4.8× (1.2 vs 5.9), MT-Bench-101 4.7×
(2.4 vs 11.3). The two exceptions are Huang (5.6 intro vs 2.8 related work) and Wei (3.3 vs 2.7);
both are papers whose introduction is doing the survey work because the argument is a
reinterpretation of a literature.

**The shape within the introduction is a front-loaded ramp, not a plateau.** Paragraph 1 carries
roughly half the citations; the results and contributions blocks carry almost none. Three papers
put more than 20 citations in a single opening paragraph: Pan (24 in P1, 53 total), Huang (14 in
P1, 36 total), Kamoi (21 in P1, 21 total, meaning the survey cites nothing after its first
paragraph).

### Rules

- **Target 17 to 25 individual citation references** across the introduction. Below 13 is the
  bottom quartile of this corpus and is what "too few citations" means numerically.
- **Put 8 to 12 of them in paragraph 1.** Paragraph 1's job is to establish that the area exists
  and has a literature; that is done with citations, not with adjectives.
- **Cite in groups of three to five where a claim is a field-level generalization**, singly where
  a claim is attributable. Huang's P1 uses one group of three and one of eleven; Kamoi's P1 uses
  nine groups totalling 21 references in 218 words.
- **The last two blocks carry no citations.** Results and contributions are the paper's own; 18 of
  23 papers put zero citations in the final block.
- **Do not move the related-work taxonomy forward.** The introduction cites to argue: each
  citation in the corpus is attached to a claim about what that work established or assumed. The
  enumeration by category belongs in Section 2, where density triples.

---

## Length and proportion rules

- **Target 650 words.** Median 651, mean 643, interquartile range roughly 570 to 775. The longest
  in the corpus is 911 (HALIE, a preprint with no page-limit pressure). The four papers with a
  confirmed ACL-family venue run 513 (CriticBench), 580 (MT-Bench-101), 594 (Tyen) and 659 (Kamoi,
  a TACL survey). Confirmed ACL-family papers cluster **at or below** the overall median, because
  the introduction competes with an eight-page body.
- **Six paragraphs.** Median 6, mean 5.9. Four of the strongest introductions run four to six
  (Self-Refine 4, Huang 6, Sharma 6, Laban 8 short ones). Eleven paragraphs (Saunders) only works
  because five of them are numbered contribution entries.
- **95 to 110 words per paragraph.** Corpus median 95. Paragraphs over 200 words appear (Kamoi P1
  at 218, RM-Bench P2 at 212, HALIE P3 at 237) but each is a single enumerated structure, not
  continuous argument.
- **No paragraph in the corpus is under 30 words except a list stem** ("Our main findings are as
  follows:", six words). A short paragraph is a stem or it is a mistake.
- **Proportion.** Across the corpus, roughly the first 40% of the introduction is field, prior work
  and gap; the middle 20% is approach; the last 40% is results and contributions. In Laban, five of
  eight paragraphs are results and implications.
- **The contributions list, if present, is the final block, and it is 4 to 5 items of 15 to 45
  words each.** 12 of 23 papers enumerate contributions or findings; 9 do so as a bulleted list, 3
  in numbered prose (CoAuthor "First… Second… Finally", MT-Bench "(1)… and (2)", Saunders
  "(1)…(5)"). Median item length in the corpus is 23 words.
- **A roadmap paragraph is optional and uncommon: 5 of 23.** Four of the five are surveys or papers
  with a non-standard section order (Pan, Kamoi, EvalGen, Stechly, Laban). For a standard empirical
  ACL paper, omit it.

---

## Register: tense, voice, verbs, hedging

Counts over all 653 sentences in the 23 introductions.

| Measure | Count |
|---|---|
| Sentences beginning with `We` / `Our` / `In this paper, we` / `To X, we` | 153 (**23%**) |
| Sentences containing a passive construction | 71 (**11%**) |
| Present-tense first-person result verbs (`we find`, `we show`, `we observe`…) | 105 |
| Past-tense first-person result verbs (`we found`, `we showed`…) | 7 |

- **First person plural, present tense, is the default.** The ratio of present to past result verbs
  is 15:1. Write "we find," "we observe," "our results indicate," never "we found." The four
  exceptions in the corpus are EvalGen and HALIE describing a user study that happened at a
  particular time ("We performed an off-line verification…", "the 1015 interaction traces we
  collected"), which is the one licensed use of the past.
- **Passive voice is rare in the paper's own claims and common in claims about the field.** The
  passive concentrates in the field beat: "these models are at present primarily evaluated
  non-interactively" (HALIE), "LLM systems are typically evaluated in single-turn, fully-specified
  settings" (Laban), "AI assistants are typically trained to produce outputs that humans rate
  highly" (Sharma), "Extensive studies on self-correction have been conducted" (Kamoi). Use the
  passive to state what the field does; use the active for what this paper does.
- **Opening sentences are flat and copular.** Not one of the 23 opens with a rhetorical question,
  a scenario, or a claim about importance. The two shortest and most transferable:
  - Kamoi: *"Self-correction is a popular approach to improve responses from large language models
    (LLMs) by refining them using LLMs during inference (Bai et al., 2022; Madaan et al., 2023),
    under the hypothesis that recognizing errors is easier than avoiding them (Saunders et al.,
    2022)."*
  - Panickssery: *"Self-evaluation is becoming a prominent part of the large language model (LLM)
    lifecycle."*
- **Result verbs are observation verbs with the data or the phenomenon as subject where possible.**
  Laban: *"we observed that models engaged in multi-turn underspecified conversations achieved an
  average performance of 65%–a 25-point drop from single-turn performances of 90%."* Huang: *"our
  findings indicate that LLMs struggle to self-correct their reasoning in this setting."* Sharma:
  *"our results indicate that sycophancy occurs across a variety of models and settings."*
- **Hedging is one clause, attached to scope, and never doubled.** "at least in certain conditions"
  (Kamoi), "in this setting" (Huang), "but not reliably" (Sharma), "primarily in proof-of-concept
  evaluations" (Sharma), "most prior work" (Laban). No paper in the corpus writes "may potentially"
  or "could possibly."
- **Numbers appear in the results beat and are always chaperoned.** 14 of 23 introductions state at
  least one number. Every one carries its referent and its comparison: "65%–a 25-point drop from
  single-turn performances of 90%" (Laban), "5-40% absolute improvement" over "direct generation
  from strong LLMs" (Self-Refine), "less than 50% accuracy… despite reaching near perfect scores on
  existing multi-turn evaluation benchmarks" (MultiChallenge), "only 69.5% accuracy. Compared to
  random guessing (50% accuracy)" (RM-Bench). A bare percentage does not appear anywhere in the
  corpus.

---

## Rules (numbered, checkable)

1. **Open with a copular sentence that names the object of study, and cite it.**
   Evidence: 23/23 introductions open on a statement about the area, none on a hook or question.
   Median citations in paragraph 1 is 9. Check: does sentence 1 contain a noun phrase naming the
   thing this paper studies, and does paragraph 1 carry 8 or more citation references?

2. **Name the field in the first two sentences, as a noun phrase in subject or object position.**
   Evidence: HALIE P2 "Our goal is to evaluate human-LM interaction"; CoAuthor P3 "how HCI
   researchers can examine LMs' generative capabilities to inform interaction design"; Saunders P2
   "the problem of scalable oversight [AOS+16]". Check: can a reader name the subfield and its
   conference after two sentences?

3. **Total 17 to 25 citation references, at a density of 2.5 to 3.5 per 100 words.**
   Evidence: corpus median 17 references, 2.7 per 100 words. Below 13 is the bottom quartile.

4. **Front-load: about half the citations in paragraph 1, about 85% in the first half.**
   Evidence: median 47% of citations in P1, median 88% in the first half of blocks.

5. **Zero citations in the results and contributions blocks.**
   Evidence: 18/23 papers have zero citations in their final block; 57% of all blocks in the corpus
   carry no citation at all.

6. **Keep the related-work taxonomy out.** The introduction runs a dialectic over four to six named
   works; Section 2 runs the enumeration.
   Evidence: related work is 2.8× denser in citations at the median, denser in 19 of 21 papers.

7. **State the gap in two sentences: a scope-fence on prior work, then a consequence.**
   Evidence: Sharma ("but primarily in proof-of-concept evaluations where users state themselves as
   having a certain view" → "It is thus unclear whether such failures occur in more varied and
   realistic settings"), Laban, RM-Bench, MultiChallenge, MT-Eval all use this pair. Check: does the
   sentence before the gap sentence name the condition prior work ran under?

8. **Never write an unfenced universal negative.** Only 3 of 23 papers use "no prior work" or "to
   our knowledge," and all four instances are fenced.
   Evidence: Kamoi, "In general tasks, no prior work shows reliable evidence of successful
   self-correction with in-context learning" (fenced by task class and by "reliable evidence").
   MT-Bench, "However, there has not been a systematic study of this approach," immediately after a
   sentence citing ten works that use the approach. Check: is there a task class, feedback source,
   setting, or evidence standard inside the negative sentence?

9. **Attribute the position you are bounding, in the same sentence that bounds it.**
   Evidence: Huang, "Contrary to the optimism surrounding self-correction (Madaan et al., 2023; Kim
   et al., 2023; Shinn et al., 2023; Pan et al., 2023, inter alia), our findings indicate that LLMs
   struggle to self-correct their reasoning in this setting."

10. **Pivot to the method in block 2 or 3, with a fixed phrase.**
    Evidence: 19 of 21 papers with an identifiable pivot place it in block 2 or 3. `In this
    paper/work, we` (8), `To this end` / `To bridge this gap` / `To address this` (6), `To study
    this` (2). Check: is there a sentence starting with one of these by the end of paragraph 3?

11. **Preview results with the phenomenon as grammatical subject and an observation verb.**
    Evidence: Laban "models engaged in multi-turn underspecified conversations achieved an average
    performance of 65%"; Huang "the performance after self-correction even deteriorates"; Sharma
    "sycophancy occurs across a variety of models and settings."

12. **Chaperone every number with its referent and its comparison.**
    Evidence: 14/23 introductions state numbers; no bare percentage appears in the corpus. Laban's
    "65%–a 25-point drop from single-turn performances of 90%" is the model.

13. **Write in present-tense first person plural. Reserve the passive for statements about the
    field.**
    Evidence: 105 present-tense first-person result verbs against 7 past; 11% of sentences contain a
    passive, concentrated in field-beat sentences.

14. **One hedge per claim, attached to scope.**
    Evidence: "at least in certain conditions" (Kamoi), "in this setting" (Huang), "but not
    reliably" (Sharma), "most prior work" (Laban).

15. **Six paragraphs, about 650 words, 95 to 110 words each.**
    Evidence: corpus medians of 6 paragraphs, 651 words, 95 words per paragraph. ACL-venue papers in
    the corpus run 474 to 594 words.

16. **If a figure is referenced, reference it in the first three blocks, and let it show the
    phenomenon rather than the architecture.**
    Evidence: 13 of 23 introductions reference a figure or table; 11 reference Figure 1 specifically.
    Placement is block 1 (Kamoi, Wei), block 2 (MT-Bench, Reflexion, MT-Eval, MT-Bench-101, Chatbot
    Arena) or block 3 (Self-Refine, HALIE). MT-Bench's is the clearest model: *"As a demonstration,
    we show conversation histories with two models on an MMLU question in Figure 1."* Two papers
    reference a figure only at the end (Saunders, Panickssery), and both are figure-per-contribution
    lists.

17. **Enumerate contributions only if there are four or five of them, and put the list last.**
    Evidence: 12/23 enumerate; 9 as bullets, 3 in numbered prose; median item 23 words; every
    instance is the final block. 11 papers enumerate nothing and close on an implication sentence
    instead, which is the more common choice among the negative-result papers (Huang, Stechly,
    Sharma, Laban).

18. **Omit the roadmap.** Only 5 of 23 have one, and four of those are surveys or papers with a
    non-standard section order.

19. **Close on the implication, not on a summary.**
    Evidence: Huang P6, *"In light of our findings, we provide insights into the nuances of LLMs'
    self-correction capabilities and initiate discussions to encourage future research focused on
    exploring methods that can genuinely correct reasoning."* Sharma P6, *"Our work motivates the
    development of training methods that go beyond using unaided, non-expert human ratings."* Laban
    P7, *"Our findings highlight a gap between how LLMs are used in practice and how the models are
    being evaluated."*

20. **Every practical recommendation in the introduction must be a consequence of a measurement
    reported in the same paragraph.** Laban is the only paper in the corpus that reaches
    recommendations in the introduction, and it does so in the roadmap paragraph, attributed to a
    later section: *"We provide actionable recommendations based on small-scale experiments and make
    a concrete call-to-action to LLM builders."* Advice that arrives before or without its
    measurement is what makes an introduction read as practitioner writing rather than as science.

---

## Constructions to avoid, with evidence

| Avoid | Why, from the corpus | Use instead |
|---|---|---|
| A hook, question, or scenario as the first sentence | 0 of 23 openers are hooks. All 23 are declarative statements about the area. | "X is a popular approach to Y (cite, cite)." (Kamoi) |
| "As LLMs become increasingly capable…" | No paper in the corpus opens on a trend clause without a citation attached. The closest, Huang's "The rapid advancements in the domain of artificial intelligence have ushered in the era of Large Language Models," is the most criticized sentence in this corpus's style. | Name the object of study directly (Panickssery: "Self-evaluation is becoming a prominent part of the large language model (LLM) lifecycle.") |
| "No work has studied X" | 0 unfenced instances in 23 papers. All 4 universal negatives carry a fence. | "In general tasks, no prior work shows reliable evidence of…" (Kamoi) |
| "Prior work fails to…" as a claim about authors | The corpus attaches failure to designs and conditions, never to researchers. RM-Bench: "However, to reduce construction costs, they often use a stronger LM…" gives prior work its reason before its limitation. | "This design makes it difficult to assess…" (RM-Bench) |
| An uncited paragraph 1 | Median 9 citations in P1; the minimum in the corpus is 1 (Laban, which compensates with a dense Section 2 at 5.9 per 100 words). | Three to five citation groups in the opening paragraph |
| A bare percentage | 0 instances in 653 sentences. | "65%–a 25-point drop from single-turn performances of 90%" (Laban) |
| Past-tense result verbs | 7 instances against 105 present. | "we find," "we observe," "our results indicate" |
| Doubled hedges ("may potentially," "could possibly") | 0 instances. | One scope clause |
| A results paragraph carrying citations | 18 of 23 final blocks have zero. | Cite in the first half; assert in the second |
| A roadmap in a standard empirical paper | 5 of 23, four of them surveys or non-standard layouts. | Close on the implication (rule 19) |
| Contributions list of 2 to 3 items | Corpus lists run 4 to 5 items. Two-item claims are made in prose (MT-Bench: "This paper makes two contributions: (1)… and (2)…"). | Either 4 to 5 bullets or one prose sentence |
| Introducing a term without attributing it | "intrinsic self-correction" is defined and attributed on first use by Huang ("we first define the concept of intrinsic self-correction, a scenario wherein…") and used with attribution by Kamoi and Tyen. | Define on first use, or cite the definer |

---

## Checklist

Run this against the draft before it goes to the advisor.

**Structure**
- [ ] Six paragraphs, one beat each: field, problem, prior work, gap, approach, results.
- [ ] The field is named as a noun phrase within the first two sentences.
- [ ] The method pivot ("In this work, we…") falls in paragraph 2 or 3.
- [ ] The results beat occupies the last 40% of the introduction.
- [ ] Closes on an implication sentence, not a summary and not a roadmap.

**Citations**
- [ ] 17 to 25 individual citation references in total.
- [ ] 8 or more in paragraph 1.
- [ ] Roughly 85% of them in the first three paragraphs.
- [ ] Zero in the final two paragraphs.
- [ ] Density between 2.5 and 3.5 per 100 words.
- [ ] Every cited work is attached to a claim about what it established or assumed, not listed.

**The gap**
- [ ] The sentence before the gap sentence names the condition prior work ran under.
- [ ] The gap sentence contains a fence (task class, feedback source, setting, or evidence
      standard).
- [ ] No universal negative appears unfenced.
- [ ] The position being bounded is cited in the sentence that bounds it.
- [ ] No sentence says or implies that prior work is wrong.

**Prose**
- [ ] First sentence is declarative and copular, with citations.
- [ ] Present tense throughout; no "we found."
- [ ] Passive voice used only for statements about what the field does.
- [ ] Every number carries a referent and a comparison.
- [ ] One hedge per claim.
- [ ] 650 words plus or minus 100.

---

## How this paper's current introduction measures up

Assessed against `paper/sections/introduction_v2.tex` (6 paragraphs) and the six-beat plan in
`paper/writer/outline.json` (target 850 words).

### Measured

| Measure | This draft | Corpus median | Verdict |
|---|---|---|---|
| Paragraphs | 6 | 6 | On target |
| Words | **970** | 651 | **Longest in the 23-paper corpus** (max observed 911) |
| Words per paragraph | 162 | 95 | 1.7× the median |
| Citation references | **13** | 17 | Bottom quartile |
| Citations per 100 words | **1.3** | 2.7 | 20th percentile; only MT-Eval (0.8), Chatbot Arena (0.9) and Laban (1.2) are lower |
| Citations in paragraph 1 | **4** | 9 | Less than half the median |
| Citations in final two paragraphs | 0 | 0 | On target |
| Share of citations in first half | 85% | 88% | On target |
| Em dashes | 0 | n/a | On target |
| Figure referenced | **No** | 13/23 do | See below |
| Contributions list | No | 11/23 also have none | Acceptable |
| Roadmap | No | 18/23 also have none | On target |

### What the draft already does at corpus standard

- **The gap paragraph (P4) uses the corpus's dominant construction.** "These results bracket the
  question we ask but do not answer it" followed by two sentences that characterize what the
  self-refinement and multi-turn literatures each study, then "Neither measures what happens in the
  case a non-expert user actually creates." That is Sharma's fence-then-consequence pattern, and
  "Neither measures" is correctly bounded to the two literatures just named rather than to the
  field. It is one of the better gap paragraphs measured against this corpus.
- **The prior-work paragraph (P3) runs a dialectic, not a list.** Madaan optimistic, Huang doubtful,
  Kamoi adjudicating, Laban the parallel case. Four works, four functions, in 142 words. This is the
  Kamoi/Tyen structure.
- **"Intrinsic self-correction" is attributed on first use** to Kamoi and Huang, which is what the
  corpus does with a borrowed term.
- **Tense and voice are correct.** Present throughout, eight first-person plural uses across 970
  words, passive reserved for the field beat ("Large language models are evaluated, for the most
  part, alone").
- **Numbers are chaperoned.** "39% of responses at the second turn to 13% at the fifth" carries both
  its denominator and its comparison, which is the Laban standard.

### What falls outside the corpus

1. **Length. 970 words is longer than every introduction measured, including an unrefereed preprint with no page limit.** The four confirmed ACL-family papers run 513 to 659, and three of the four are under 600. The outline targets 850, which
   is already above the corpus maximum for an ACL paper; the draft overshoots that by 120. P6 alone
   is 223 words, longer than any single non-enumerated paragraph in the corpus. **Cut to 650 to
   700.** The material to cut is identified in item 4.

2. **Citation count. 13 references at 1.3 per 100 words puts this in the bottom quartile on both
   measures, which is the numeric content of the advisor's complaint.** The specific shortfall is
   paragraph 1: 4 references against a corpus median of 9. Paragraph 1 currently cites HELM, the
   Anthropic index, Laban and the underspecification paper. It needs three to five more, grouped,
   attached to the two claims it already makes: that single-turn benchmark evaluation is the norm
   (a group of three or four benchmark papers alongside HELM, in the HALIE manner: "Almost all
   benchmarks, even those with a diverse range of tasks, such as GEM (Gehrmann et al., 2021) and
   HELM (Liang et al., 2022), encode this non-interactive view"), and that deployment is collaborative and multi-turn (a group
   alongside the Anthropic index). Paragraph 2 at 3 references and paragraph 4 at 2 are also thin;
   the gap paragraph in particular cites only Kamoi and Huang while making claims about two
   literatures, and should carry the two or three multi-turn works it characterizes. Reaching 20 to
   24 references is achievable without adding a sentence, by converting single citations to groups.

3. **No figure is referenced.** 13 of 23 introductions reference one, 11 of them Figure 1, and in
   the papers closest to this one it shows the phenomenon rather than the design: MT-Bench shows two
   conversation histories, Wei shows a sycophantic exchange. The outline's own note on beat 2 says
   "This is where Figure 1 could go if you want the reader to see the phenomenon before the argument
   for it." Given that the paper's central object is a conversational behavior that is easy to state
   and hard to picture, a Figure 1 showing one conversation degrading across five turns, referenced
   at the end of paragraph 2, would follow the corpus and would carry some of the load paragraph 6
   is currently carrying in prose.

4. **Paragraph 6 does four jobs and exceeds the corpus's longest continuous paragraph.** It reports
   RQ1, RQ2 and RQ3, then the meta-commentary finding, then the evaluation argument, then the
   practical recommendation, then the title. Two problems follow. First, the recommendation ("the
   practical remedy is to supply the direction the model cannot generate for itself: to withhold the
   request to revise until there is a specific weakness to direct it at") is the sentence most
   likely to read as practitioner advice, which is the advisor's stated objection. In the corpus,
   only Laban reaches a recommendation in the introduction, and it defers it to a named later
   section rather than stating it. Second, the methodological finding about judge bias is a
   contribution of the paper, and in the corpus a second contribution of that kind gets its own
   short paragraph rather than a subordinate clause. **Split P6 into a findings paragraph (RQ1, RQ2,
   RQ3) and a short closing paragraph (the judge-bias finding, then the evaluation implication, then
   the title sentence), and cut the practical recommendation to the Discussion.** That is also where
   most of the 300 surplus words are.

5. **The opening sentence is a stylistic fragment where the corpus is flat.** "Large language models
   are evaluated, for the most part, alone." The comma-bounded qualifier and the terminal "alone"
   make it an aphorism; no opener in 23 papers has this shape. It is also uncited, where the median
   opener carries citations. Compare Laban's opener, which does the same work with the same
   flatness the corpus uses: "Today's large language models (LLMs) function as conversational
   interfaces (e.g., ChatGPT, Gemini, Claude), enabling users to interact with the LLM through
   multiple conversation turns." A closer model still, because it states the evaluation practice
   directly: HALIE's "However, these models are at present primarily evaluated non-interactively:
   given an input text, a model generates a completion with the focus solely on the quality of the
   completion."

6. **"It is also, we find, where the collaboration quietly fails."** (P2 close.) This is a
   theatrical closer of a kind that appears nowhere in the corpus, and "quietly" is an evaluative
   adverb doing no measurement work. The corpus ends its problem paragraphs on the object of study
   or on a question (EvalGen: "How can we help users validate the validators?"). Replace with a flat
   statement of what the paper measures, or with the question the paper answers.

### Assessment of the outline

The six-beat plan in `writer/outline.json` matches the corpus order exactly (field → problem →
prior work → gap → approach → results), which is the sequence 19 of 23 papers use. Three
adjustments the evidence supports:

- **Lower `targetWords` from 850 to 680.** 850 exceeds the ACL-venue maximum in this corpus by
  more than 250 words.
- **Beat 1's `cites` list has three keys; the corpus median for paragraph 1 is nine references.**
  Raise it to six or seven keys, grouped.
- **Beat 6's open decision ("numbers here or qualitative?") is settled by the corpus: state
  numbers.** 14 of 23 introductions state at least one, and every one of the negative-result papers
  that has a headline magnitude states it (Laban 65% and 25 points, Huang qualitative but with the
  oracle-label mechanism named, MultiChallenge "less than 50%"). Keeping 39% and 13% is right, and
  the RQ3 reversal should carry a magnitude too, since it is the finding the title rests on.

---

# Part 2: extended corpus, ACL-family venues (added 2026-09-08)

## Why this part exists

Part 1 rests on 23 introductions of which only **four** carry a confirmed ACL-family
venue. This paper goes to ARR with a page limit, so those four were carrying the length
and citation targets on their own. This part extends the corpus to **44 introductions,
26 of them with an ACL-family venue stated in the arXiv record**, and recomputes every
distribution split by venue.

**Method.** Candidates were found through the arXiv API by querying `cat:cs.CL` against
each venue string in the `comment` and `journal_ref` fields, intersected with this
paper's own related-work topic terms (`paper/SKELETON.md` section 2). 341 candidates
carried a stated ACL-family venue; the 22 closest on title relevance were fetched.
Venue is read from the record and never inferred: a paper whose record states no venue
is counted in the "not stated" group, not against ACL.

Counting is by script, not by eye: `scripts/introduction_corpus/02_fetch_intros.py`
isolates the `<section>` whose heading matches "Introduction", takes the outermost
`ltx_para` blocks with nested `ltx_item` removed to its own block, and counts
`href="#bib.bib"` anchors as individual bibliography references. Raw HTML is cached at
`.workspace/reference/intro_corpus/html/` so every count reproduces without refetching.
Retrieved 2026-09-08.

**Calibration against Part 1.** All 22 of the original papers reachable in HTML were
recounted with the new script. **Citations match Part 1 exactly on 21 of 22** and
paragraphs on 19 of 22. Word counts run a systematic 5 to 8 percent higher because Part
1 excluded contribution-list items from its word total and reported them in a separate
column, where this pass folds any list not marked up as `ltx_item` into its parent
paragraph. The two passes are measuring the same thing; the offset is the convention,
not a disagreement. Where Part 1 and Part 2 differ, **Part 2 governs**, because all 44
papers are counted one way.

**Coverage and limits.** Saunders 2206.05802 has no LaTeXML HTML (a 2022 paper) and is
excluded: 44 of 45 attempted. One paper, 2503.12556, collapses to a single 379-word
block, which is an extraction artifact rather than a one-paragraph introduction; it is
excluded from the headline targets below, and excluding it moves the median word count
by 6. The corpus remains arXiv-only for the reason Part 1 gives.

## The targets, ACL-family only (n = 25)

| Measure | p25 | **Median** | p75 | Max |
|---|---:|---:|---:|---:|
| Introduction words | 561 | **658** | 768 | 862 |
| Paragraphs | 4 | **6** | 7 | 10 |
| Citation references | 14 | **17** | 22 | 26 |
| Citations per 100 words | 2.08 | **2.9** | 3.29 | 4.41 |
| Citations in paragraph 1 | 4 | **6** | 10 | 21 |
| Citations in the last two blocks | 0 | **0** | 2 | 13 |

## Three corrections to Part 1

1. **The length target loosens.** Part 1 says 650 words and cites an ACL-family range of
   513 to 659 from four papers. On 25 papers the ACL-family median is **658** with p75 at
   **768** and a maximum of **862**. The target is right; the ceiling is not as tight as
   four papers made it look. **650 to 750 is comfortably inside the venue.**

2. **The paragraph-1 citation rule was set too high.** Part 1 says 8 to 12 citations in
   paragraph 1, from a corpus median of 9. That median came from a preprint-heavy sample:
   the papers with no stated venue have a paragraph-1 median of **9**, and the ACL-family
   papers have a median of **6** (p75 10). **Six to ten is the ACL-family target.**

3. **The figure convention is stronger than Part 1 measured.** 27 of 44 introductions
   (61%) reference a figure, against Part 1's 13 of 23 (57%).

## What Part 1 got right, now on 44 papers

- **No introduction opens on a rhetorical question. 0 of 44.** Part 1 measured 0 of 23.
  This is the firmest finding in either part. The abstract may open on a question; the
  introduction may not.
- **The last two blocks carry no citations.** Median 0 in every split.
- Median 6 paragraphs holds across the whole corpus and both splits.

## Section-count benchmark (n = 26 ACL-family, counted from the same HTML)

Part 1 had no data on this and `rules/05` covers only methods subsections. Counted here
as top-level `\section` headings before the references or appendix, with Limitations and
Ethics excluded because ARR treats them as unnumbered.

| Measure | p25 | **Median** | p75 | Max |
|---|---:|---:|---:|---:|
| Top-level sections | 6 | **6** | 7 | 13 |
| Subsections before the appendix | 8 | **9** | 11 | 15 |

**Six top-level sections is the norm**, and it is exactly the standard arc: Introduction,
Related Work, Methods, Results, Discussion, Conclusion. Seven is common; anything past
eight is a survey or a multi-study paper.

## How this paper measures up, re-measured 2026-09-08

Against `paper/sections/introduction_v2.tex` as it stands, and `paper/main.tex` for
structure. This supersedes the assessment in Part 1, which was measured at 970 words and
predates both the figure reference and the finalized abstract.

| Measure | This draft | ACL-family target | Verdict |
|---|---|---|---|
| Introduction words | **996** | median 658, max 862 | **Over the corpus maximum** by 134 |
| Paragraphs | 7 | median 6, p75 7 | In band |
| Citation references | **13** | median 17, p25 14 | **Below p25** |
| Citations per 100 words | **1.3** | median 2.9, p25 2.08 | **Below p25** |
| Citations in paragraph 1 | **4** | median 6, p25 4 | At p25, no longer the outlier Part 1 called it |
| Citations in last two blocks | 0 | median 0 | On target |
| Opens on a question | No | 0 of 44 do | On target |
| References a figure | Yes | 27 of 44 do | On target. Part 1's "no figure is referenced" is stale |
| Top-level sections | 6 | median 6 | On target |
| Subsections before appendix | 12 | median 9, p75 11, max 15 | Above p75, inside max |

**The two live problems are length and citations, and they pull against each other.**
The draft needs roughly 250 words cut and 4 to 9 citation references added. Both are
achievable together, because Part 1 item 2 identifies the citations as convertible from
singles to groups without adding a sentence, and Part 1 item 4 identifies paragraph 7 as
carrying most of the surplus.

The methods subsection count (8) remains a separate finding under `rules/05` (median 3,
no paper above 5); the 12 here is the whole-paper figure and is a different measure.
