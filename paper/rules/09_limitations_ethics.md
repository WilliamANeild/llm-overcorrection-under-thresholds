# Rules: Limitations and Ethics

Retrieved 2026-09-02. 31 papers fetched and read; 24 Limitations sections and 6 Ethics
sections read in full, plus 7 human-subjects appendices.

> **Note on this file's history, 2026-09-02.** An earlier version of this file, written by
> a sibling agent, opened with a section on the ARR October 2026 submission requirements.
> That section was destroyed when this file was written fresh rather than appended to, and
> it is not recoverable: the file was never committed to git, and the backup at
> `paper/rules/.09_arr_section_backup.md` is byte-identical to the overwriting content
> (MD5 `2e223084ef8762610c81269c4a25aebb`), so it preserves nothing of the original.
> The section below is **not** a restoration of that text. It is an independent retrieval
> of the same policy, made on 2026-09-02 from the official sources named in each
> subsection, and its wording is mine, not the sibling agent's. Because the earlier text no
> longer exists, no comparison between the two retrievals is possible and no discrepancy
> between them can be reported either way. Anything the earlier section covered that is
> absent below was not recovered and should be re-retrieved.

---

## ARR submission requirements, October 2026 cycle

**Sources.** ACL Rolling Review Call for Papers, `https://aclrollingreview.org/cfp`, and
ACL Rolling Review Dates, `https://aclrollingreview.org/dates`. Both retrieved 2026-09-02.
All indented text is quoted verbatim from those pages as fetched on that date.

### Cycle dates

From `https://aclrollingreview.org/dates`, the October 2026 row of the cycle table gives a
submission date of **October 12**, a cycle end of **December 20**, and reviewer
registration, reviews due, author response and meta-review release all listed as **TBA**
as of the retrieval date. The page explains the schedule change:

> This means that instead of 6 cycles a year there will generally be 5, but with more
> reasonable timelines for the review tasks and author response, as well as platform
> maintenance.

Three deadlines beyond submission now carry sanctions:

> Note that in addition to submission and author response dates, the following action
> points are now listed, as non-compliance may result in desk rejection or sanctions...
> Reviewer registration deadline for ALL authors. The registration link will be active in
> the author console immediately upon paper submission. ALL authors must register. Not all
> authors will receive assignments, but non-compliant papers may be desk rejected.

### Page limit

> Long papers may consist of:
> up to eight (8) pages of content
> unlimited extra space after the conclusion for limitations (required, see below) and
> optional section on ethical considerations (we recommend it to be titled 'Ethical
> considerations')
> plus unlimited pages of references

> Submissions that exceed the length requirements, or are missing a limitations section,
> will be desk rejected.

Short papers are the same structure with "up to four (4) pages of content".

For what the Limitations and Ethics sections must contain, and where they sit, see **The
ACL / ARR requirement, quoted verbatim** further down this file, which quotes the same
Call for Papers at greater length.

### Anonymity

> Papers must not include authors' names and affiliations. Furthermore, self-references
> that reveal the authors' identities, e.g., "We previously showed (Smith, 1991)…" must be
> avoided. Instead, use citations such as "Smith previously showed (Smith, 1991)…" Papers
> should not refer, for further detail, to documents that are not available to the
> reviewers.

> Supplementary materials, including any links to repositories, should also be anonymized.
> Links to file hosting services that can track downloads, such as Dropbox, are not
> allowed.

> Submissions that violate these requirements will be desk rejected.

On preprints, the policy is permissive but the incentives are not neutral:

> Beginning February 15, 2024, there is no anonymity period or limitation on posting or
> discussing non-anonymous preprints while the work is under peer review. However, the new
> policy does incentivize anonymous submissions through special paper awards and priority
> in acceptance decisions for borderline papers. You will be asked to select the preprint
> status of the submission on our submission form. If you choose the binding "no
> non-anonymous preprint" option, you commit to not preprinting until the metareviews are
> released, under the penalty of desk rejection.

### Responsible NLP Research checklist

> In addition, we provide a responsible NLP research checklist, which authors must
> complete as part of their paper submission. The content of checklists is used in the
> review process, and incorrect, incomplete or misleading information in the checklist can
> result in desk rejection (please see the checklist instructions). Furthermore, ACL'25
> will resume the publication of responsible NLP checklists for accepted papers for
> improving the overall transparency of the scientific process.

The two checklist questions that govern this file's subject are A1 ("Did you describe the
limitations of your work?") and A2 ("Did you discuss any potential risks of your work?").
Both are quoted at length in the next major section.

### AI writing and coding assistance

> Generally, generative AI tools do not qualify for authorship. Their use for writing or
> coding, as well as its scope, must be disclosed in the Responsible NLP Checklist.
> Details should be included in the Acknowledgements section. For coding assistance,
> details may also be included in the README files.

The policy enumerates six cases. Disclosure is not required for (a) "Assistance purely
with the language of the paper... The use of tools that only assist with proofreading,
like grammar or spell checkers, does not need to be disclosed" or (b) "Short-form input
assistance." Disclosure is required for (c) literature search, where "The usual
requirements for citation accuracy and thoroughness of literature reviews apply", (d)
low-novelty text, where "Authors should specify where such automatically generated text
was used, and convince the reviewers that the generation was checked to be accurate and is
accompanied by relevant and appropriate citations", and (e) new ideas. On (f):

> ACL does not consider a generative model to be an entity that can fulfill the
> requirements of co-authorship.

> In all cases, all authors are fully responsible for the correctness of their methods,
> results, and writing. They should check for potential plagiarism, both of text and code.

And on the text itself:

> The full text of the submissions should be addressed exclusively to the human readers,
> and clearly visible to them. Submissions attempting to manipulate their machine 'readers',
> e.g. via prompt injections, may be desk rejected.

### Authorship and originality

> The author list for submissions should include all (and only) individuals who made
> substantial contributions to the work presented... Please notice that once the paper has
> been submitted, no changes to the list of authors are allowed.

> All submitted papers are expected to describe original, completed and unpublished work.
> See the publication ethics guidelines on re-use of text from other publications (no more
> than 10% total tokens).

### Reviewing requirement

> Submitting to ARR comes with a reviewing requirement. Starting in May 2025, all authors
> are expected to contribute to the review process, unless an exemption applies (e.g.,
> authors new to the community, with insufficient experience, or already serving in
> another capacity). Papers from the teams that do not meet this requirement, and are not
> covered by an exception, may be desk rejected.

> All authors are expected to complete a registration form within 48h hours after
> submission deadline... They must have an updated OpenReview profile, including
> affiliation, semantic scholar link, dblp link, ACL anthology link, and an email address
> where they can receive OpenReview messages.

### Desk-rejection conditions named on the page

Collected from the passages above, a submission may be desk rejected for: exceeding the
page limit; missing a Limitations section; using the Limitations section to introduce new
methods, analysis or results; breaking anonymity in the paper or supplementary materials;
preprinting after choosing the binding no-preprint option; an incorrect, incomplete or
misleading Responsible NLP checklist; prompt-injection or other manipulation of machine
readers; failure of all authors to complete reviewer registration; and violation of the
originality requirements.

---

**Provenance.** The ACL Rolling Review policy text below was fetched from
`https://aclrollingreview.org/cfp` and `https://aclrollingreview.org/responsibleNLPresearch/`
on 2026-09-02 and transcribed verbatim from the fetched page. Every paper quotation was
fetched from `https://arxiv.org/html/<ID>` on 2026-09-02 and transcribed from the fetched
HTML. Nothing in this file is written from memory. Where a quotation contains spacing
oddities around citations or duplicated mathematical symbols, that is an artefact of
arXiv's LaTeX-to-HTML conversion and has been left as fetched.

**What is not covered.** Only arXiv-hosted HTML versions were read. The camera-ready
version in the ACL Anthology can differ from the arXiv version, and for four papers the
arXiv HTML is a pre-mandate preprint with no Limitations section at all (listed below).
The ACL Anthology PDF text was not parsed. Venue attribution comes from the
author-supplied arXiv Comments field as it stood on 2026-09-02 and was not checked
against proceedings. No non-English-language venue was searched.

---

## The ACL / ARR requirement, quoted verbatim

**Source:** ACL Rolling Review, Call for Papers, `https://aclrollingreview.org/cfp`.
Retrieved 2026-09-02.

Under the heading **"Limitations (required section)"**:

> Authors are required to discuss the limitations of their work in a dedicated section
> titled "Limitations". This section should be included at the end of the paper, before
> the references, and it will not count toward the page limit. This includes both, long
> and short papers. Papers without a limitations section will be desk rejected. Note,
> prior to the December 2023 cycle, this was optional.

> Please note that this section should not introduce new methods, analysis, or results.
> We reserve the right to desk reject the submissions that use this section to introduce
> more content that should have been part of the main paper. It can only discuss the
> limitations of the work presented in the main content of the paper.

In the length specification for long papers:

> unlimited extra space after the conclusion for limitations (required, see below) and
> optional section on ethical considerations (we recommend it to be titled 'Ethical
> considerations')

> Submissions that exceed the length requirements, or are missing a limitations section,
> will be desk rejected.

Under the heading **"Ethics Policy"**:

> Authors are required to honour the ethical code set out in the ACL Code of Ethics.

> The consideration of the ethical impact of our research, use of data, and potential
> applications of our work has always been an important consideration, and as artificial
> intelligence is becoming more mainstream, these issues are increasingly pertinent. We
> ask that all authors read the code, and ensure that their work is conformant to this
> code. Authors are encouraged to devote a section of their paper to concerns about the
> ethical impact of the work and to a discussion of broader impacts of the work, which
> will be taken into account in the review process. This discussion does not count
> towards the page limit, as long as it is placed in the end of the paper. In addition,
> we provide a responsible NLP research checklist, which authors must complete as part of
> their paper submission. The content of checklists is used in the review process, and
> incorrect, incomplete or misleading information in the checklist can result in desk
> rejection (please see the checklist instructions).

**Source:** ACL Rolling Review, Responsible NLP Research checklist,
`https://aclrollingreview.org/responsibleNLPresearch/`. Retrieved 2026-09-02.

> A1. Did you describe the limitations of your work?

> Point out any strong assumptions and how robust your results are to violations of these
> assumptions (e.g., independence assumptions, noiseless settings, model
> well-specification, asymptotic approximations only held locally). Reflect on how these
> assumptions might be violated in practice and what the implications would be.

> Reflect on the scope of your claims, e.g., if you only tested your approach on a few
> datasets, languages, or did a few runs. In general, empirical results often depend on
> implicit assumptions, which should be articulated.

> We understand that authors might fear that complete honesty about limitations might be
> used by reviewers as grounds for rejection. It is worth keeping in mind that a worse
> outcome might be if reviewers discover limitations that aren't acknowledged in the
> paper. In general, we advise authors to use their best judgement and recognize that
> individual actions in favor of transparency play an important role in developing norms
> that preserve the integrity of the community. Reviewers will be specifically instructed
> to not penalize honesty concerning limitations.

> A2. Did you discuss any potential risks of your work?

> Examples of risks include potential malicious or unintended harmful effects and uses
> (e.g., disinformation, generating fake profiles, surveillance), environmental impact
> (e.g., training huge models), fairness considerations (e.g., deployment of technologies
> that could further disadvantage or exclude historically disadvantaged groups), privacy
> considerations (e.g., a paper on model/data stealing), and security considerations
> (e.g., adversarial attacks).

**What the policy settles.** The section is titled exactly "Limitations". It sits after
the conclusion and before the references. It does not count against the page limit. It
may not contain new analysis or results. Omitting it is a desk rejection. The ethics
section is optional, encouraged, also excluded from the page limit if placed at the end,
and ARR's preferred title is "Ethical considerations", though "Ethics Statement" is what
most of the corpus uses.

---

## Corpus

31 papers fetched. 24 have a Limitations section that was read in full; 6 of those also
have an Ethics or Ethical Considerations section, read in full. Word counts are of the
section body as rendered in the arXiv HTML, excluding headings, table contents and
acknowledgments.

| Paper | ID | Venue (arXiv comments, 2026-09-02) | Lim. words | Paras | Form | Ethics words |
|---|---|---|---|---|---|---|
| Self-Refine | 2303.17651 | none stated | 184 | 4 | prose, ordinal-linked | none |
| Can LLMs Be an Alternative to Human Evaluations? | 2305.01937 | ACL 2023 main | 262 | 3 | prose | 357 |
| CRITIC | 2305.11738 | ICLR 2024 | 353 | 3 | prose, run-in labels | 226 |
| AlpacaFarm | 2305.14387 | NeurIPS 2023 (spotlight) | 491 | 5 | prose, run-in labels | none |
| Judging LLM-as-a-Judge (MT-Bench) | 2306.05685 | NeurIPS 2023 D&B | 224 | 1 + run-ins | prose, run-in labels | none (societal-impact run-in) |
| Is Self-Repair a Silver Bullet? | 2306.09896 | ICLR 2024 | 298 | 3 | prose, ordinal-linked | none (IRB in body) |
| Style Over Substance | 2307.03025 | work in progress | 130 | 2 | prose, run-in labels | none |
| Creativity Support in the Age of LLMs | 2309.12570 | none stated | 293 | 2 | prose | none |
| Benchmarking Cognitive Biases in LLMs as Evaluators | 2309.17012 | ACL 2024 | 163 | 2 | prose | none |
| LLMs Cannot Self-Correct Reasoning Yet | 2310.01798 | ICLR 2024 | 269 | 2 | prose (merged w/ Broader Impact) | merged |
| LLMs cannot find reasoning errors | 2311.08516 | ACL 2024 Findings | 122 | 2 | prose | none |
| MT-Eval | 2401.16745 | none stated | 109 | 2 | prose | none |
| Humans or LLMs as the Judge? | 2402.10669 | EMNLP 2024 | 354 | 5 | prose, ordinal-linked | 64 |
| MT-Bench-101 | 2402.14762 | ACL 2024 | 40 | 1 | prose | 179 |
| Chatbot Arena | 2403.04132 | none stated | 112 | 1 | prose, run-in label | none |
| Length-Controlled AlpacaEval | 2404.04475 | COLM 2024 | 101 | 1 | prose, ordinal-linked | none |
| LLM Evaluators Recognize and Favor Their Own Generations | 2404.13076 | none stated | 547 | 5 | prose, run-in labels | none |
| Prometheus 2 | 2405.01535 | EMNLP 2024 main | 490 | 4 | prose | none (annotator note in appendix) |
| LLMs instead of Human Judges? (Judge-Bench) | 2406.18403 | ACL 2025 main | 300 | 4 | prose, ordinal-linked | none |
| Can LLMs Generate Novel Research Ideas? | 2409.04109 | none stated | none dedicated | n/a | Q&A discussion instead | 785 |
| Moral Self-correction is Not Innate | 2410.20513 | none stated | 91 | 1 | prose | none |
| The Alternative Annotator Test | 2501.10970 | none stated | 572 | 6 | prose, run-in labels | none |
| LLMs Get Lost In Multi-Turn Conversation | 2505.06120 | none stated | 520 | 3 | prose, ordinal-linked | none |
| Self-Correction Bench | 2507.02778 | COLM 2026 | 147 | 1 | prose | 165 |

**Fetched and read, no dedicated Limitations section in the arXiv HTML** (7): G-Eval
(2303.16634), Large Language Models are not Fair Evaluators (2305.17926), Human Feedback
is not Gold Standard (2309.16349, ICLR 2024), Towards Understanding Sycophancy
(2310.13548), Aligning with Human Judgement (2403.16950, COLM 2024), When Can LLMs
Actually Correct Their Own Mistakes? (2406.01297, TACL 2024), Neither Valid nor Reliable?
(2508.18076). Two of these matter for calibration: Kamoi (2406.01297) is a TACL paper and
TACL does not impose the ARR requirement, so a survey of self-correction with no
Limitations section is not evidence that the section is optional at an ARR venue; and
several are ICLR or NeurIPS papers whose venues have no such mandate. A Preregistration
discussion paper (2302.10086, EACL 2023) was also read for its 104-word Limitations
section.

### Length distribution (23 sections with a measurable word count)

- Range 40 to 572 words. Median 262. Mean 268. First quartile 122, third quartile 354.
- 10 of 23 are under 200 words. 15 of 23 are under 300. 8 of 23 are 300 or more.
- The shortest (MT-Bench-101, 40 words) is a two-sentence statement that the benchmark
  may not cover future multi-turn abilities. The longest (the alt-test, 572 words) works
  through three named failure modes of the proposed procedure.
- **0 of 24 sections use a bulleted or numbered list.** Every one is running prose. Six
  use bold or italic run-in labels at the head of each paragraph; seven link items with
  ordinals in running text ("First... Second... Finally"). The rest are undifferentiated
  paragraphs.

---

## What gets disclosed, categorised with counts

Counts are of the 24 papers whose Limitations section was read in full. A paper is
counted once per category regardless of how many sentences it spends there.

| Category | Count | Papers |
|---|---|---|
| Sample and task coverage (which tasks, datasets, item counts, domains) | 19 / 24 | 2303.17651, 2305.14387, 2306.09896, 2307.03025, 2309.12570, 2309.17012, 2310.01798, 2311.08516, 2402.10669, 2402.14762, 2403.04132, 2404.04475, 2404.13076, 2405.01535, 2406.18403, 2410.20513, 2501.10970, 2505.06120, 2507.02778 |
| Judge or metric validity | 10 / 24 | 2305.01937, 2306.05685, 2401.16745, 2402.10669, 2404.04475, 2404.13076, 2405.01535, 2406.18403, 2409.04109, 2501.10970 |
| Model coverage (which models, how many, which sizes) | 6 / 24 | 2303.17651, 2305.14387, 2309.17012, 2401.16745, 2402.10669, 2507.02778 |
| Generalisation to real users or deployment | 6 / 24 | 2306.09896, 2309.12570, 2311.08516, 2403.04132, 2505.06120, 2507.02778 |
| Annotator quality, recruitment, inter-annotator agreement | 4 / 24 | 2305.14387, 2309.17012, 2402.10669, 2501.10970 |
| Statistical inference, power, causal warrant | 4 / 24 | 2306.09896, 2404.13076, 2409.04109, 2501.10970 |
| Language coverage (English only) | 4 / 24 | 2303.17651, 2405.01535, 2406.18403, 2505.06120 |
| Cost, compute or access constraints | 3 / 24 | 2303.17651, 2309.12570, 2401.16745 |
| Misuse of the contributed method or artifact | 2 / 24 | 2303.17651, 2501.10970 |

Two observations from the distribution. First, task coverage is close to universal and
model coverage is not: three quarters of the corpus tells the reader which tasks were
used and only a quarter tells them how thin the model panel is. Second, statistical power
is the rarest category in the corpus, appearing in four papers, and in only two of those
(2306.09896, 2501.10970) does it appear inside the Limitations section itself.

---

## Verbatim catalogue: limitation sentences, classified by whether a rebuttal is attached

**Classification.** *Bare disclosure* states the limitation and stops, or continues only
to future work. *Disclosure plus mitigation* states the limitation and then says what was
done, or what a reader or future researcher should do, to reduce it. *Disclosure plus
rebuttal* states the limitation and then argues that it does not undermine the paper's
conclusion.

**Totals: 37 sentences. Bare disclosure 17. Disclosure plus mitigation 8. Disclosure plus
rebuttal 12.**

### Bare disclosure (17)

1. 2303.17651: "Another limitation of our work is that we exclusively experiment with datasets in English."
2. 2305.14387: "First, the instructions we considered (even those from the real world-demo in section 4.4 ) are relatively simple and single-turn."
3. 2305.14387: "Second, all models we fine-tuned use a LLaMA 7B as starting point."
4. 2306.05685: "This paper emphasizes helpfulness but largely neglects safety."
5. 2306.05685: "Additionally, within helpfulness, there are multiple dimensions like accuracy, relevance, and creativity, but they are all combined into a single metric in this study."
6. 2306.09896: "Secondly, our experiments focus on self-contained Python programming tasks with executable unit tests. This is quite different from real-world software development tasks, where specifications are often incomplete, there are long contextual dependencies, and tests are unlikely to be available for each individual snippet."
7. 2306.09896: "Finally, our study on human data did not track how much time the participants took to debug the programs. As a result, we can only evaluate the quality of the feedback (and the impact this has on repair)."
8. 2307.03025: "We select only 40 questions from Chiang et al. (2023) . We acknowledge that this limited selection may not capture the full spectrum of question types and variations."
9. 2309.17012: "Some models reach very low valid response rates, which may be due to the prompting format."
10. 2401.16745: "Due to computational limits, our experiments did not include any larger open-source models like Llama2-chat-70B."
11. 2402.10669: "Thirdly, human judges consist of only college students, whose behavior may not generalize to common human judges."
12. 2402.14762: "With LLM technologies rapidly evolving, new multi-turn capabilities are likely to emerge. Consequently, the findings of this study may not encompass all multi-turn abilities."
13. 2404.04475: "Firstly, we only tested our proposed debiasing mechanism on the AlapcaEval benchmark, which uses a set of relatively simple English instructions and a particular prompt for the LLM judge."
14. 2404.13076: "Despite the use of a diverse set of control tasks, our experiments can only provide evidence towards the causal hypothesis without fully validating it."
15. 2405.01535: "One downside of the Prometheus 2 is that it operates only on a 1-5 point Likert scale for absolute evaluation or a comparative evaluation style of 'A is better & B is better'."
16. 2406.18403: "Finally, our work mostly focuses on English-language datasets—with the exception of datasets focussing specifically on machine-translation outputs."
17. 2505.06120: "A third limitation of the work is the focus on text-only tasks in the English language."

### Disclosure plus mitigation (8)

18. 2303.17651: "Further, these models are not free to use, and using them for research requires some funding. Nonetheless, we release our code and model outputs to ensure the reproducibility of our work."
19. 2305.14387: "Although we controlled for those biases by randomizing the order of output in the prompt, and using the same training data for all considered methods, there may be other biases that we have not identified."
20. 2306.09896: "This risks introducing statistical artefacts in our analysis. To minimize this risk, we bounded n p n_{p} and n f ​ r n_{fr} far below N p N_{p} and N f ​ r N_{fr} , respectively, in our self-repair experiments."
21. 2311.08516: "One main limitation of our dataset is that it features tasks that are artificial and unrealistic for real-world applications. We made this choice to minimise ambiguity and subjectivity during the mistake finding process, but further work needs to be done to determine the effectiveness of backtracking in a more realistic setting."
22. 2401.16745: "To further improve the evaluation quality, more advanced prompting or reasoning techniques can be explored, like tree-of-thought ( Yao et al., 2023 ) or self-consistency ( Chen et al., 2023b ) . While these methods require more model inference times, this is a trade-off between evaluation quality and cost."
23. 2405.01535: "Also note that it is crucial to use model-based evaluations in conjunction with human evaluation instead of solely relying on it."
24. 2406.18403: "Indeed, there may be domains where human annotators and LLM evaluators appear aligned simply because they are affected by similar biases. Therefore, depending on the task at hand, it may be necessary to validate the reliability of human annotators as well."
25. 2501.10970: "To ensure sound and transparent testing, researchers should always report the IAA of the human annotators. If the IAA is low, the conclusions drawn from the alt-test are less reliable, and to compensate for this, researchers must use small values of ε ≤ 0.1 \varepsilon\leq 0.1 and annotate more instances."

### Disclosure plus rebuttal (12)

26. 2305.01937: "However, it is important to note that these limitations and potential harms also apply to human evaluation: the bias of human evaluators can affect the human evaluation result ( Lentz and De Jong, 1997 ; Amidei et al., 2018 ) ."
27. 2305.11738: "Nevertheless, such overheads are not exclusive to our technique. Prevalent prompt methodologies, such as ReAct and Self-Consistency, similarly trade-off time for enhanced performance."
28. 2305.14387: "Although we do not expect the previous limitations to significantly affect the usefulness of AlpacaFarm, we encourage users to be vigilant when using any simulator and hope to further validate AlpacaFarm as more datasets and base models become available."
29. 2306.05685 (§3.3): "We identify certain biases and limitations of LLM judges. However, we will also present solutions later and show the agreement between LLM judges and humans is high despite these limitations."
30. 2306.09896: "Furthermore, we note that the standard deviation is very small in our experiments for all values of n p n_{p} and n f ​ r n_{fr} (see the scatter plots in Figures 3 , 4 ), offering increased confidence in our results."
31. 2402.10669: "However, this sort of questions are little in proportion based on our inspection. ... Therefore, we argue that such ambiguity has little effect on the validity of our conclusion."
32. 2402.10669: "Fourthly, since LLM judges are evolving, the conclusions drawn on LLMs may be invalid as they advance. However, the aim of this work is to unveil the biases of current LLMs and hopefully point out a direction for future LLM development."
33. 2404.04475: "Despite these limitations, we show that the correlation with Chatbot Arena increases significantly, which suggests that AlpacaEval-LC takes a step in the right direction."
34. 2404.13076: "Our existing results provide indirect evidence for disproportionate self-preference: the sum of self-preference scores of a pair of LLMs exceeds one, which means that for at least a portion of the dataset they both prefer themselves."
35. 2501.10970: "This property of our procedure can be desirable, as it may help researchers identify potential issues with the annotation process, such as unclear guidelines, unqualified annotators, or the inherent subjectivity of the task."
36. 2505.06120: "The minimal nature of shards is also unrealistic and potentially adversarial, though the gradual sharding experiment finds that different levels of shard granularity lead to similar performance degradations, as soon as conversations occur over two turns or more."
37. 2507.02778: "Our mechanistic analysis deliberately targets two maximally distinct families (Llama and Qwen) at the 7-8B scale to establish existence and causality of the conversational-role direction. Confirming universality beyond these two families is a natural extension that does not affect the causal conclusions within them."

### What the counts show

A rebuttal is **not** expected. Bare disclosure is the single largest class (17 of 37,
46 percent), and the two non-bare classes together are 20 of 37. More useful than the raw
split is where each class appears. Of the 12 rebuttals, 9 are attached to a limitation of
a **method the paper is proposing** (CRITIC's latency, AlpacaFarm's simulator,
AlpacaEval-LC's single benchmark, the alt-test's behaviour under annotator disagreement,
MT-Bench's judge biases, Self-Correction Bench's two model families). Only 3 are attached
to a limitation of the paper's **empirical finding**. The pattern in the corpus is that a
paper contributing an artifact defends the artifact, and a paper reporting a finding
states the limits of the finding and stops.

Two of the rebuttals do real work rather than reassurance, and both do it by naming a
direction of bias grounded in evidence already in the paper: 2505.06120 argues from its
own gradual-sharding experiment that granularity does not change the result, and 2507.02778
argues that the two chosen model families were selected to be maximally distinct. A
rebuttal of this kind is a claim about the design that the reader can check. The other
ten are assertions that the concern is small.

The corpus also supplies a clear negative case. Si, Yang and Hashimoto (2409.04109) have
no Limitations section at all and instead run a Discussion built as four objection-answer
pairs: "Question 1: Do these collected expert ideas represent their best ideas? One might
argue that these ideas submitted by our idea-writing participants might not represent
their best ideas as we discussed in Section 6.1, since most of them came up with the idea
on the spot within a short period. In order to address this concern, we have designed an
experiment where we will compare AI ideas with papers accepted at top-tier AI
conferences." This is the concern-then-rebuttal architecture in its pure form, and it
occupies four consecutive subsections. It is one paper of 31.

---

## Disclosing underpowered subgroups and unmet thresholds

### Underpowered or unbalanced subgroups

Four papers in the corpus disclose a limit on statistical warrant, and the wording is
consistently flat.

- **2409.04109**, in the abstract, on an effect it declines to claim: "We find some signs
  that these gains are correlated with excitement and overall score, and may come at the
  slight expense of feasibility, but our study size did not have sufficient power to
  conclusively identify these effects (Figure 2 )." The same paper handles its per-topic
  breakdown by refusing to interpret it: "Note that due to the smaller sample sizes for
  the per-topic breakdown, most results are not statistically significant and only offer
  an intuitive understanding of the trends."
- **2306.09896** on a resampling design that could manufacture precision: "This risks
  introducing statistical artefacts in our analysis."
- **2404.13076** on causal warrant: "Despite the use of a diverse set of control tasks,
  our experiments can only provide evidence towards the causal hypothesis without fully
  validating it."
- **2501.10970** on what happens when annotators disagree: "When the remaining annotators
  are inconsistent, this introduces high variance in determining who aligns better (the
  LLM or the excluded annotator). Under these conditions, the hypothesis test is unlikely
  to reject the null hypothesis, and the LLM's winning rate remains low."
- **2311.08516** on a deliberately skewed sample: "Another limitation is that our paper
  does not experiment with backtracking on the original datasets on BIG-Bench, only
  showing results on the limited set that we sampled in a skewed manner, in order to
  maximise the value of the human annotators' time."
- **2507.02778** converts an unbounded claim into a bound: "On models' own errors (Section
  4.1 ), the design yields only a lower bound: at least 4.3–10.8% of the errors a model
  commits are ones it demonstrably had the knowledge to catch."

The shared move: name the quantity that is unreliable, say in one clause what that does
to the claim, and downgrade the claim rather than defend it. "Only offer an intuitive
understanding of the trends," "can only provide evidence towards," "yields only a lower
bound." None of the six adds a sentence arguing the result survives anyway.

### Unmet pre-registered thresholds

**No paper in this corpus discloses a pre-registered threshold that its results failed to
meet.** Searching all 31 fetched papers for "pre-regist", "preregist", "pre-specified",
"prespecified" and "pre-committed" returns exactly one hit, in 2409.04109: "We
pre-registered our analysis plan which also includes the link to the cached ideas"
(footnote to `https://osf.io/z6qa4`), and that registration is for a **future** experiment
whose results the paper does not report. No paper reports a decision rule set in advance
and then reports missing it.

The nearest thing the corpus offers is 2409.04109's positionality statement, which is a
disclosure of prior expectation rather than a threshold: "We disclose the authors'
anticipated outcomes of the human study before the experiment was conducted to be
transparent about experimenter biases. Among the three authors, Tatsu and Diyi were
expecting a null result from the study while Chenglei expected AI to be better than
humans."

The field also has a published argument about this gap: Bloem and colleagues' EACL 2023
paper on preregistration in NLP (2302.10086) closes with "our main contribution is a
two-sided discussion of its pros and cons, leaving many questions in the air. Our paper is
intended to get the preregistration debate off ground, not to nail it to the floor." Which
is to say that as of this corpus, preregistration in NLP is a topic of discussion and not
an established reporting practice.

**Consequence for this paper.** There is no template to copy. The reporting standard has
to be borrowed from the underpowered-subgroup wording above, which the field does have,
and applied to a decision rule: state the bar, state the result against it, state that the
bar was not met, and state which claim is therefore not made. Do not add a sentence
arguing the point estimate is encouraging.

---

## LLM-judge validity: how it is limited and disclosed

Ten of 24 papers disclose a limit on their judge or metric. Four patterns, all quoted
verbatim.

**1. The judge is validated against humans, and the validation itself is questioned.**
2406.18403: "One limitation of the experimental design of our work is that correlation
with human judges may not be the most appropriate way to validate LLM evaluators. Indeed,
there may be domains where human annotators and LLM evaluators appear aligned simply
because they are affected by similar biases."

**2. The indirection of the validation is named.** 2405.01535: "In this paper, we used an
indirect method to assess the evaluation capability of evaluator LMs by measuring if they
perform evaluations similar to human evaluators or proprietary LMs, such as GPT-4-1106 and
Claude-3-Opus. However, this may not necessarily be the best approach."

**3. The judge's biases are enumerated with measurements, in the body, not the Limitations
section.** 2306.05685 devotes a 10-paragraph subsection (§3.3, 800 words) to position
bias, verbosity bias and self-enhancement bias, each with a table: "Only GPT-4 outputs
consistent results in more than 60% of cases." The paper's actual Limitations section does
not repeat these; it points back: "We propose preliminary solutions to address the
limitations and biases of LLM-as-a-judge in Section 3.4 , but we anticipate more advanced
methods can be developed."

**4. Self-preference is treated as a measurable quantity rather than a caveat.**
2404.13076 makes the whole paper about it and then limits the claim: "Self-preference can
be justifiable if the LLM's generation is indeed higher quality than the alternative. From
a safety perspective, what we are interested in is disproportionate self-preference, e.g.,
an LLM preferring its own generation even when it's equal or worse quality than the
alternative. This would require controlling for generation quality when measuring
self-preference using groundtruth annotation."

**5. Human agreement is reported as a number and a floor for interpretation.** 2501.10970
is the most explicit standard-setter in the corpus: "To ensure sound and transparent
testing, researchers should always report the IAA of the human annotators. If the IAA is
low, the conclusions drawn from the alt-test are less reliable... We strongly encourage
researchers to disclose detailed information about the annotators and to publish the human
annotations, allowing others to reproduce and validate the results."

What no paper in the corpus does: claim the judge is valid, or present a correlation
coefficient without saying what it licenses. What several do: report the number, then say
plainly which comparisons the coefficient licenses and which it does not.

---

## Ethics statement conventions

Six papers have a dedicated Ethics or Ethical Considerations section, read in full:
2305.01937 (357 words), 2305.11738 (226), 2402.10669 (64), 2402.14762 (179), 2409.04109
(785), 2507.02778 (165). Median 172 words. Two more merge the material elsewhere:
2310.01798 folds it into "Limitations and Broader Impact", and 2306.05685 uses two run-in
paragraphs headed "Data collection and release." and "Societal impacts."

### What they cover

- **Dual use and misuse of the contributed method.** All six. 2402.10669: "In Section 6 ,
  we provide a simple yet effective prompt-based attack on LLM-as-a-judge. Our intention is
  to raise the awareness of the community on developing robust LLM judges, rather than
  encouraging LLM developers to hack existing judges." 2507.02778: "The conversational-role
  direction we identify could in principle be used adversarially, for instance, by steering
  a model away from the external-role state to suppress self-correction. However, this
  requires white-box access to model weights."
- **Data content screening.** 2402.14762: "We have taken rigorous steps to ensure that the
  dataset is devoid of offensive content or personal identity information. However, there
  might still be residual errors or biases due to inadvertent mistakes by GPT-4 or
  oversights by annotators."
- **Release terms and intended use.** 2402.14762: "Lastly, the dataset released in this
  work is intended solely for research and may not be suitable for commercial use without
  additional verification." 2306.05685: "We will clean the Personal Identifiable
  Information (PII) and tag toxic conversations with OpenAI moderation APIs for our dataset
  release."
- **Whether the work displaces human labour.** 2305.01937 spends its statement on this:
  "Is it ethical to replace human evaluation with LLM evaluation? Some may question if this
  paper is suggesting that LLMs are now ready to replace humans and find this idea
  unsettling. As responsible and ethical NLP researchers, we understand these concerns but
  want to make it clear that this is not our intent."
- **Benign nature of the stimuli.** 2507.02778: "Lastly, our error injection methodology
  involves only benign mathematical and logical errors, not harmful content."

### Human annotators: consent, compensation, review

The corpus convention is that the annotator details are stated concretely and with
numbers, and that they usually sit in an appendix rather than in the ethics section. Seven
verbatim instances:

- **2306.05685**: "To invite participants, we obtained their consent by letting them sign an
  application form. We pay them $20 for judging 20 questions, which corresponds to an
  hourly rate of around $35. The participants are mostly graduate students from more than
  ten universities."
- **2305.14387**: "Annotators are recruited from Amazon Mechanical Turk using a
  qualification test of 25 questions. Out of an initial pool of 34 annotators, we selected
  the 16 whose agreement rate was higher than 70% with the authors' annotations. We paid
  the annotators a median hourly rate of $21..."
- **2309.16349**: "Participants were paid 0.30GBP for annotating each pair of outputs with
  overall scores or assertiveness/complexity ratings, or 0.60 for annotating each pair of
  examples for errors. This corresponded to a median payment of over 13GBP per hour for all
  experiments. Participants were recruited using Prolific..."
- **2405.01535**: "The annotation study was designed and administered in accordance with
  [Affiliation X]'s ethical guidelines. Crowd workers were informed of the potential risks
  of participation and researcher contact information before hand in the study consent
  form. The hourly wage and expected study time were informed in the Prolific platform. We
  compensated workers 9 GBP per hour."
- **2306.09896**: "Participants were asked to spend approximately one hour on the study
  overall, and were compensated with a $15 gift card. This study was approved by our
  Institutional Review Board (IRB) and carried out exclusively through an online survey."
- **2305.01937**: "Each teacher is asked to rate 200 GPT-2-generated stories and 200
  human-written stories, and they are paid US$140 for rating 200 stories. Considering that
  the teachers reported that they take at most 5 hours to rate 200 stories, this makes the
  hourly wage at least US$28." And on review: "We do not have an ethical review board or
  anything like that in our institute, so we are not able to get approval from an ethical
  review board. Still, we try our best to follow the ethical guidelines of ACL."
- **2305.17926** benchmarks against a legal floor in a footnote: "The minimum hourly wage
  in the United States is near $7.5, which can be found at https://www.worker.gov/."

Counts: **IRB approval is stated in exactly 1 of the 31 papers fetched** (2306.09896).
One more (2305.01937) states plainly that no review board exists at the institution.
Compensation is stated as a rate in 6 papers. Informed consent is stated in 4
(2306.05685, 2405.01535, 2402.14762, and implicitly 2306.09896 via IRB). Blinding of
annotators to condition is stated in 1 (2305.01937: "The teachers are not told who wrote
the stories before they evaluate the stories. We reveal to them what this project aims to
study after they finish rating all the stories.").

### Synthetic data and model output release

Three of the six ethics statements address synthetic stimuli directly, and all three do so
in one sentence with no elaboration: the errors are benign (2507.02778), the dataset was
screened for offensive content and PII (2402.14762), the data was manually checked by the
authors and has no ethics-related issues (2402.10669: "the dataset used for investigating
the bias of human and LLM judges undergo manual check by the authors and have no
ethics-related issues"). No paper in the corpus withholds model outputs on the grounds
that they might be mistaken for human writing.

---

## Rules

Each rule names the evidence.

**R1. Title the section exactly `Limitations`, unnumbered, after the conclusion and before
the references.** ARR: "a dedicated section titled 'Limitations'. This section should be
included at the end of the paper, before the references." Use `\section*{Limitations}` so
it takes no number. Same for `\section*{Ethics Statement}`, placed after Limitations and
before `\bibliography`.

**R2. Put no new number, table, test or analysis in the Limitations section.** ARR: "this
section should not introduce new methods, analysis, or results... We reserve the right to
desk reject the submissions that use this section to introduce more content that should
have been part of the main paper." Every statistic that appears in Limitations must already
appear in the main text. 2306.05685 models the compliant pattern: its Limitations points
back at §3.4 rather than restating the analysis.

**R3. Write prose. No bullets.** 0 of 24 corpus sections use a list. If the section has
more than three items, use bold run-in labels at the head of each paragraph (2305.14387,
2404.13076, 2501.10970, 2307.03025) or ordinals in running text (2306.09896, 2402.10669,
2406.18403, 2505.06120). Both are established; a bulleted list is not.

**R4. Target 250 to 400 words in three to five paragraphs.** Corpus median 262, third
quartile 354, modal paragraph count 1 to 3. Below 150 words the section reads as
box-ticking (2402.14762's 40 words is the corpus floor and says nothing about that paper's
own design). Above 550 it starts to argue (2501.10970, 2404.13076).

**R5. Open with the limitation, not with an announcement that limitations follow.** 18 of
23 corpus sections open with substance: "The main limitation of our approach is that the
base models need to have sufficient few-shot modeling or instruction-following abilities"
(2303.17651); "A first limitation of our work is the reliance on fully automated
simulation" (2505.06120); "This paper emphasizes helpfulness but largely neglects safety"
(2306.05685). Four open with a throat-clearing sentence (2309.12570, 2309.17012,
2402.10669, 2410.20513), and in each case the sentence adds no information.

**R6. Order by how much the limitation affects the paper's main claim, biggest first.**
2505.06120 spends its first and longest paragraph on the one thing that could overturn its
result (simulated rather than real users) and its last and shortest on English-only.
2507.02778 opens with the caveat on its own headline number. Ordering by the sequence in
which the limitations occurred to the authors, or leaving the most serious one at position
eight, invites a referee to conclude it was buried.

**R7. Default to bare disclosure. Attach a rebuttal only when it is a checkable claim
about the design.** Bare disclosure is the largest class in the corpus (17 of 37
sentences), and 9 of the 12 rebuttals defend a proposed artifact rather than an empirical
finding. The two rebuttals that work cite the paper's own evidence for a direction of bias
(2505.06120's gradual-sharding experiment; 2507.02778's deliberate choice of two maximally
distinct model families). A rebuttal that only asserts the concern is small
("Reassuringly...", "we do not expect this to significantly affect...") adds nothing a
referee will credit.

**R8. Never build the section, or the discussion, as objection then answer.** The one
corpus paper that does (2409.04109, four consecutive "Question N... One might argue...")
is also the one paper of 31 with no Limitations section at all. Nothing in the ARR policy
asks for anticipated objections, and the checklist explicitly promises the opposite:
"Reviewers will be specifically instructed to not penalize honesty concerning
limitations."

**R9. When a quantity is unreliable, downgrade the claim in the same sentence.** The
corpus verb pattern is "can only", "only offer", "yields only": "our experiments can only
provide evidence towards the causal hypothesis without fully validating it" (2404.13076);
"most results are not statistically significant and only offer an intuitive understanding
of the trends" (2409.04109); "the design yields only a lower bound" (2507.02778). Say what
the paper therefore does not claim.

**R10. State model coverage and panel composition with counts.** Only 6 of 24 corpus
papers disclose model coverage at all, which is why a reader who notices an undisclosed
imbalance treats it as concealment rather than convention. 2305.14387: "Second, all models
we fine-tuned use a LLaMA 7B as starting point." 2401.16745: "Due to computational limits,
our experiments did not include any larger open-source models like Llama2-chat-70B."

**R11. Report the judge's human agreement as a number and say what it licenses.** 2501.10970:
"researchers should always report the IAA of the human annotators. If the IAA is low, the
conclusions drawn from the alt-test are less reliable." 2406.18403 goes further and
questions the validation design itself. A correlation reported without an interpretation
clause is the failure the corpus warns against.

**R12. State English-only and single-temperature coverage explicitly.** 4 of 24 disclose
language coverage, and all four do it in one clause at the end of the section
(2303.17651, 2405.01535, 2406.18403, 2505.06120). It costs a sentence and its absence is
an ARR checklist item (A1: "Reflect on the scope of your claims, e.g., if you only tested
your approach on a few datasets, languages, or did a few runs").

**R13. Future work belongs in the Limitations section only as a clause, never as a
paragraph.** 15 of 24 corpus sections gesture at future work, always attached to the
limitation it answers: "We leave the full evaluation to future work as this is beyond the
scope of this paper" (2311.08516); "Determining whether degradation occurs – and if so,
identifying the magnitude – on creative tasks is an important direction for future work"
(2505.06120). Three corpus papers instead run a "Future directions" block inside the
Limitations section (2305.14387, 2306.05685, 2403.04132), which converts the section into
an agenda. Under R2 that block also risks reading as new content.

**R14. In the Ethics Statement, give annotator arrangements as facts with numbers.** How
many raters, how recruited, what relationship to the authors, paid or unpaid and at what
rate, what they were told, and what review the study had. The corpus states rates in 6
papers, consent in 4, IRB in 1. Where there was no board review, say so plainly, as
2305.01937 does: "We do not have an ethical review board or anything like that in our
institute, so we are not able to get approval from an ethical review board."

**R15. In the Ethics Statement, address dual use of the paper's own finding.** All six
corpus ethics statements do. For a paper whose finding is a failure mode, the relevant
question is whether naming it teaches anyone to exploit it; 2507.02778 answers exactly
this and concludes the attack needs white-box weight access.

**R16. Keep the two sections doing separate jobs.** Limitations answers "what should a
reader not conclude from this evidence". Ethics answers "who could be harmed by this work
and what was done about it". 2310.01798 merges them into "Limitations and Broader Impact"
and the result reads as neither. Only 1 of 24 does this.

---

## Constructions to avoid, with evidence

**A single paragraph of eight ordinals.** Corpus paragraph counts are 1, 2 or 3 in 15 of
24 sections, and the two sections with five or more items (2404.13076, 2501.10970)
both break them into separate labelled paragraphs. No corpus section runs more than four
ordinals inside one paragraph.

**"Several limitations qualify these findings."** and its relatives. Content-free openers
appear in 4 of 23 sections and none of them is a strong section. Compare 2505.06120's
opener, which names the limitation in its first eight words.

**"We mitigate this through..."** as a bolt-on to a disclosure of judge dependence. The
corpus reports what was done and separately reports how well it worked; it does not label
the procedure a mitigation. 2305.14387 is the closest: "Although we controlled for those
biases by randomizing the order of output in the prompt... there may be other biases that
we have not identified." Note that the sentence ends on the residual, not on the fix.

**Assertive reassurance.** "Despite these limitations, we show that the correlation with
Chatbot Arena increases significantly, which suggests that AlpacaEval-LC takes a step in
the right direction" (2404.04475) and "Although we do not expect the previous limitations
to significantly affect the usefulness of AlpacaFarm" (2305.14387) are both defending a
proposed artifact. A findings paper that writes the same sentence is arguing with a
referee who has not spoken.

**Announcing a solution before the reader has seen the problem.** 2306.05685 §3.3 opens
"We identify certain biases and limitations of LLM judges. However, we will also present
solutions later and show the agreement between LLM judges and humans is high despite these
limitations." The rebuttal precedes the disclosure, which tells the reader how to feel
before telling them what happened.

**Q&A discussion sections.** 2409.04109's "Question 1... Question 2... Question 3...
Question 4..." is the only instance in 31 papers.

**Captioning what the evidence fails to show.** No corpus limitations section volunteers
an absence that no reader had raised. The material that reads as volunteered is instead
stated as a bound on the claim (2507.02778's lower bound; 2404.13076's "can only provide
evidence towards").

---

## Checklist

Before submission, each line must be answerable yes.

1. Is the section titled exactly `Limitations`, unnumbered, placed after the Conclusion
   and before `\bibliography`?
2. Is the Ethics Statement after Limitations and before `\bibliography`?
3. Does every number in Limitations already appear in the main text? (ARR desk-rejection
   condition.)
4. Is the section 250 to 400 words in three to five paragraphs of prose, with no bullets?
5. Does the first sentence name a limitation rather than announce that limitations follow?
6. Is the limitation that most affects the main claim in first position?
7. Does every item state, in a clause, what the paper therefore does not claim?
8. Is every rebuttal a checkable claim about the design, citing evidence already in the
   paper? Are there no more than one or two?
9. Are model coverage, panel composition, language and temperature each stated with
   counts?
10. Is the judge's agreement with humans given as a number, with a clause saying what it
    licenses?
11. Does the pre-registered decision rule appear in the main text with its bar, its
    result, and the conclusion not drawn?
12. Does future work appear only as clauses attached to individual limitations, never as
    its own paragraph or block?
13. Does the Ethics Statement state rater count, recruitment, relationship to the authors,
    compensation or its absence, what raters were told, and what review the study had?
14. Does the Ethics Statement address dual use of the paper's own finding?
15. Is there no sentence anywhere in either section that raises an objection nobody made in
    order to answer it?

---

## How this paper's current limitations and ethics measure up

### What was read

`paper/sections/discussion.tex` (11 lines; the Limitations material is the final
`\section{Limitations}` block, 234 words, one paragraph, eight ordinals from "First" to
"Eighth") and `paper/main.tex` (the `\section*{Ethics Statement}` block, 97 words, one
paragraph, placed after `\input{sections/conclusion}` and before `\bibliography`).

### Structural findings

**Placement (fails R1, desk-rejection risk).** The Limitations material sits inside
`sections/discussion.tex`, which `main.tex` inputs *before* `sections/conclusion.tex`. ARR
requires the section "at the end of the paper, before the references." Move it to its own
file, input it after the conclusion, and change `\section{Limitations}` to
`\section*{Limitations}` so it is unnumbered and outside the page count. The Ethics
Statement's placement is already correct.

**Form (fails R3, R4, R14).** 234 words in one paragraph with eight ordinals is below the
corpus first quartile in length and above the corpus maximum in items-per-paragraph. No
corpus section runs eight ordinals in one paragraph. Split into four paragraphs at roughly
320 words: panel composition and the human comparison; measurement (judge, scale, rater
agreement, the near-trivial edits); design coverage (synthetic tasks, temperature,
language, probe neutrality); domain-level precision.

**New content (R2 risk).** The current text is the only place several numbers appear in
the form given: the three rater-pair kappa range 0.41 to 0.60, Krippendorff's alpha 0.529
at n = 64, the Turn-5 per-domain cell range of 13 to 30 trials, and the reversibility
confidence interval. Each must appear in Results or Methods first. As written the section
is doing analysis rather than qualifying it.

**Ordering (fails R6).** The reversibility result is item eight of eight. It is the item a
referee will care about most, because it is the one place where a pre-committed bar was
missed. Corpus practice (2505.06120, 2507.02778) puts the caveat on the headline claim
first.

**Sentence 2 needs a disclosure it does not currently make.** "we mitigate this through
six-model calibration selecting the highest human-correlation judge (Spearman r = 0.505,
QW kappa = 0.526)" reports a selection over six candidate evaluators by human correlation,
and then reports that same correlation as the validation. If the calibration items and the
validation items are the same items, the reported correlation is an in-sample maximum over
six choices and is optimistic. Check whether the two sets are disjoint. If they are, say
so in Methods. If they are not, the honest wording is that the judge was chosen for
highest agreement among six candidates and the reported coefficient is the selected
maximum.

**Ethics Statement gaps (fails R14; partially fails R15).** The current 97 words state
that three raters (the first author and two research assistants) rated synthetic text, that
no personal data was collected, and that raters participated voluntarily. Missing against
corpus convention: whether the research assistants were compensated and at what rate, or
paid through an assistantship (6 corpus papers give a rate); what the raters were told and
whether they were blind to condition, which matters here because the first author is one
of the three raters (2305.01937 states blinding explicitly); what institutional review the
study had, or a plain statement that none was required for staff rating machine-generated
text (2305.01937 supplies the wording for the null case); the model versions and dates and
whether the API terms permit the released data; and what is released. The sentence "We do
not release model outputs that could be mistaken for human-written text" is unusual, has
no corpus precedent, and reads as a restriction on the artifact rather than a statement of
what is released; replace it with what the release contains. On dual use, add one sentence:
the paper names a failure mode in deployed assistants, and the question a reader has is
whether naming it enables anything, which it does not, because the described behaviour is
already reachable by any user typing "can this be improved?".

### The five limitations: recommended strength and wording

Each recommendation names the corpus precedent it follows. Numbers in brackets are the
author's to confirm against the Results text before use, since under R2 they must appear
there first.

**1. Panel composition: 45 of 50 trials are Llama, three of six models contribute none.**
*Strength: bare disclosure, first position, both counts given, one clause on what the
estimate therefore is.* Precedent: 2305.14387 ("Second, all models we fine-tuned use a
LLaMA 7B as starting point"), 2401.16745, 2507.02778. Do not attach a mitigation; there
is none, and the corpus does not expect one.

> The balanced panel used for the quality-trajectory estimate contains 50 trials, 45 of them
> from Llama 3.3 70B, and three of the six models contribute none, because they leave the
> revision pool before a within-model comparison is possible. The trajectory estimate is
> therefore a within-Llama estimate. What the six-model evidence supports is the weaker
> claim that no model's quality-optimal stopping point falls after the first turn.

**2. The pre-registered human comparison did not clear its bar: 56.2 percent, CI [45.2,
67.1], bar 65 percent with CI excluding 50.** *Strength: full disclosure of the rule, the
result and the conclusion not drawn. No rebuttal, no note that the point estimate exceeds
50.* There is no corpus precedent for an unmet pre-registered bar, so the wording borrows
the field's underpowered-result register: 2409.04109's "our study size did not have
sufficient power to conclusively identify these effects" and 2507.02778's "the design
yields only a lower bound". The bar, the estimate and the interval belong in Results as a
reported outcome; Limitations restates what is not claimed.

> The blind pairwise comparison of first and last versions was pre-registered with a
> decision rule of 65 percent preference and a confidence interval excluding 50 percent.
> On stripped content it returned 56.2 percent (95 percent CI 45.2 to 67.1) and did not
> meet that rule. The degradation reported here is measured by the judge and by the rater
> panel; we do not claim that a reader comparing two drafts would notice it.

Note what this does for the paper rather than against it: reporting the rule and the miss
is a stronger position than reporting 56.2 percent with no rule, which reads as a weak
result presented as support. The current draft's eighth clause already says "we do not
claim humans can reliably distinguish first from revised drafts", which is the right
sentence in the wrong position.

**3. Quality scored by an LLM judge on a six-level scale, validated against three human
raters.** *Strength: disclosure plus one interpretation clause. Report the coefficients,
then say what they license.* Precedent: 2501.10970 ("researchers should always report the
IAA of the human annotators. If the IAA is low, the conclusions drawn... are less
reliable"), 2406.18403 on the validation design itself, 2405.01535 on indirection.

> Quality is scored by an LLM judge (Claude Sonnet 4) on a six-level scale, chosen from
> six candidate evaluators by agreement with three human raters. Judge-human agreement is
> moderate (Spearman r = 0.505, quadratic-weighted kappa = 0.526), and the human raters
> agree with each other at a comparable level (quadratic-weighted kappa 0.41 to 0.60,
> Krippendorff's alpha = 0.529). A judge that agrees with human raters about as well as
> they agree with each other supports the sign and rough size of a quality change and does
> not support fine distinctions between adjacent levels. The judge also scores outputs
> from its own model family.

The last sentence replaces the current "judges outputs from all models including itself",
and it should not be followed by a defence. 2404.13076 shows the field treats
self-preference as a measurable quantity, so if the paper can report the judge's scores on
its own family against the human raters' scores on the same items, that belongs in
Results.

**4. Six trials with near-trivial edits, four character-identical.** *Strength: bare
disclosure with the counts and the disposition rule.* Precedent: 2311.08516 disclosing a
deliberately skewed sample; 2306.09896 disclosing a resampling design that "risks
introducing statistical artefacts". This is the item most likely to be found by a referee
who opens the released data, and the cheapest to state.

> Six of the 50 balanced-panel trials contain edits at or just above the genuine-revision
> threshold, four of them character-identical between the two versions. They are retained
> under the classification rule set before analysis. [If they were excluded, say excluded
> and give the resulting n.]

Confirm the disposition before writing this; the sentence must match what the code does.

**5. Synthetic scenarios, not observed user conversations.** *Strength: bare disclosure of
the design, plus a direction-of-bias clause only if the paper has evidence for the
direction.* Precedent: 2505.06120, whose entire first limitation is this, and which earns
its direction claim from a within-paper experiment ("the gradual sharding experiment
finds that different levels of shard granularity lead to similar performance
degradations"); also 2311.08516 and 2306.09896.

> The 40 tasks are scenarios written for this study across five domains, not conversations
> observed between users and a deployed assistant, and the revision request is a scripted
> probe rather than a user's own words. Real requests arrive with context, prior turns, and
> a partially specified complaint that the probe does not reproduce, so the conditions here
> are those under which a model has least reason to revise.

The final clause is a direction claim. Include it only if the paper can point to the
balanced-probe design as the evidence for it, in the way 2505.06120 points to its
sharding experiment. If not, stop after "does not reproduce."

### Items to add that are currently absent

English-only coverage, model versions and the dates the API calls were made, and the
single-temperature setting (temperature 1.0 is disclosed; the language and the dates are
not). All three are ARR checklist A1 items and each costs one clause. Combine with the
existing convenience-sample and probe-neutrality items into the third paragraph.
