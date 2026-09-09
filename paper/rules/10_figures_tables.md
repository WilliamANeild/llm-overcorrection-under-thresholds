# Rules: Figures, Tables and Captions

Retrieved 2026-09-02. 22 papers examined.

Method. Captions were extracted mechanically from the arXiv LaTeXML HTML (`arxiv.org/abs/<ID>`)
or ar5iv HTML for each paper, giving 507 numbered captions. Every caption quoted below was read
in that extracted text and is reproduced verbatim, with two mechanical caveats: LaTeX math is
rendered by the extractor as doubled tokens (for example `P¯\overline{P}`) and is elided here as
`[math]`, and en/em dashes and curly quotes are preserved as they appeared. Figure images were
downloaded separately and viewed where a visual judgement was needed; the eleven figures I opened
and looked at are named in the text. Page placement was checked against the PDFs with
`pdftotext`, page by page. Where a claim rests on a caption I read but a figure I did not open,
that is stated.

What I could not do. Laban Figure 6's three sub-panels, Sharma's Figures 1 to 7 and Huang's
Figure 1 are drawn with pgfplots/TikZ rather than included as image files, so they do not appear
as retrievable PNGs in the HTML; I read Laban Figure 6 by rendering page 9 of the PDF at 100 dpi
and viewing it, and I did not render the Sharma or Huang plots. Laban Figure 11 (the example
simulated conversation) has an empty figure body in the arXiv HTML, so I have its caption but
not its contents. Counts of "figures" and "tables" below are counts of distinct numbered captions
found in the HTML, including appendices, with subfigure letters collapsed into their parent
number; they will not always match a hand count of float environments.

---

## Corpus

| # | Paper (short) | arXiv ID | Figs | Tabs | Fig:Tab | Figure 1 type | Fig 1 on p.1 | Median caption (words) |
|---|---|---|---|---|---|---|---|---|
| 1 | Laban, LLMs Get Lost in Multi-Turn Conversation | 2505.06120 | 11 | 9 | 1.22 | **Mixture** (schematic panels + real scatter) | **Yes** | 35 |
| 2 | Madaan, Self-Refine | 2303.17651 | 38 | 17 | 2.24 | Schematic (method diagram) | No (p.2) | 13 |
| 3 | Huang, LLMs Cannot Self-Correct Reasoning Yet | 2310.01798 | 8 | 8 | 1.00 | Real data (stacked bars) | No (p.6) | 13 |
| 4 | Kamoi, When Can LLMs Actually Correct Their Own Mistakes? | 2406.01297 | 3 | 8 | 0.38 | Schematic (method taxonomy) | No (p.2) | 25 |
| 5 | Sharma, Towards Understanding Sycophancy | 2310.13548 | 22 | 5 | 4.40 | Real data (bars, mean and SE) | No (p.3) | 38 |
| 6 | Zheng, Judging LLM-as-a-Judge (MT-Bench) | 2306.05685 | 19 | 14 | 1.36 | **Real transcript, verbatim** | No (p.2) | 17 |
| 7 | Tyen, LLMs Cannot Find Reasoning Errors | 2311.08516 | 4 | 9 | 0.44 | Real data (bars with CIs) | No (p.5) | 34 |
| 8 | Lee, CoAuthor | 2201.06796 | 11 | 5 | 2.20 | **Real writing session, colour-coded** | No (p.2) | 34 |
| 9 | Lee, Evaluating Human-Language Model Interaction (HALIE) | 2212.09746 | 17 | 21 | 0.81 | Schematic (framework cube) | No (p.2) | 62 |
| 10 | Shinn, Reflexion | 2303.11366 | 7 | 5 | 1.40 | Schematic (task illustrations) | No (p.3) | 24 |
| 11 | Dubois, AlpacaFarm | 2305.14387 | 14 | 6 | 2.33 | Schematic (system diagram) | No (p.2) | 24 |
| 12 | Wei, Simple Synthetic Data Reduces Sycophancy | 2308.03958 | 15 | 11 | 1.36 | Example prompt/response pair | **Yes** | 33 |
| 13 | Kim, Prometheus | 2310.08491 | 20 | 9 | 2.22 | Schematic (contrast diagram) | No (p.2) | 29 |
| 14 | Kwan, MT-Eval | 2401.16745 | 3 | 13 | 0.23 | Illustrative task dialogues | No (p.3) | 27 |
| 15 | Bai, MT-Bench-101 | 2402.14762 | 45 | 7 | 6.43 | Illustrative dialogues + cartoon | **Yes** | 9 |
| 16 | Chiang, Chatbot Arena | 2403.04132 | 14 | 5 | 2.80 | Schematic (2x2 classification) | **Yes** | 23 |
| 17 | Panickssery, LLM Evaluators Favor Their Own Generations | 2404.13076 | 8 | 14 | 0.57 | Real data (scatter + fit) | **Yes** | 14 |
| 18 | Sirdeshmukh, MultiChallenge | 2501.17399 | 11 | 5 | 2.20 | Test examples (synthetic, human-edited) | No (p.3) | 10 |
| 19 | Wu, CollabLLM | 2502.00640 | 12 | 8 | 1.50 | Schematic (framework) | **Yes** | 30 |
| 20 | Dang, Diegetic and Non-Diegetic Prompts | 2303.03199 | 9 | 3 | 3.00 | Real UI screenshot | **Yes** | 49 |
| 21 | Shankar, Who Validates the Validators? (EvalGen) | 2404.12272 | 4 | 2 | 2.00 | Schematic (two pipelines) | No (p.3) | 138 |
| 22 | Xu, Pride and Prejudice: LLM Self-Bias | 2402.11436 | 12 | 14 | 0.86 | Real data (bias/skew plot) | **Yes** | 38 |

Ratio. Figures outnumber tables in 14 of 22 papers. The median ratio is 1.44 figures per table;
the range is 0.23 (MT-Eval) to 6.43 (MT-Bench-101). A table-heavy paper is unremarkable in this
literature: Kamoi (0.38), Tyen (0.44), Panickssery (0.57), HALIE (0.81) and Xu (0.86) are all
below parity. **There is no norm requiring more figures than tables.**

---

## The teaser figure

**Every one of the 22 papers has a Figure 1.** None omits it.

**Figure 1 appears on page 1 in 8 of 22** (Laban, Wei, MT-Bench-101, Chatbot Arena, Panickssery,
CollabLLM, Dang, Xu). In three more (Kamoi, AlpacaFarm, MT-Eval) the string "Figure 1" appears on
page 1 only as a prose cross-reference, with the float landing later. The remaining 11 place
Figure 1 on page 2 or later; Huang puts it on page 6 and Tyen on page 5, both of them papers whose
Figure 1 is a results chart rather than a teaser. **Page-1 placement is a real convention but not
a majority one, and it correlates with what the figure is for**: a figure that sets up the problem
goes on page 1, a figure that reports a result goes where the result is discussed.

### Figure 1 content, classified (n = 22)

| Type | Count | Papers |
|---|---|---|
| Method or framework schematic, no data and no content | 9 | Madaan, Kamoi, HALIE, Reflexion, AlpacaFarm, Prometheus, Chatbot Arena, CollabLLM, EvalGen |
| Example content (transcript, prompt/response, screenshot) | 7 | Zheng, CoAuthor, Wei, MT-Eval, MT-Bench-101, MultiChallenge, Dang |
| Real empirical data, plotted | 5 | Huang, Sharma, Tyen, Panickssery, Xu |
| Mixture of schematic and real data in one figure | 1 | Laban |

Within the seven example-content Figure 1s, **three show genuinely real material** (Zheng: a real
transcript from two named models; CoAuthor: a real writing session from the released dataset;
Dang: a screenshot of the real interface) and **four show constructed benchmark items** (Wei,
MT-Eval, MT-Bench-101, MultiChallenge).

### The best examples, described so they can be reproduced

**Laban Figure 1 (viewed; `2505.06120v1/LIC_Teaser.png`, 1620x840).** This is the closest model
for the present paper and it is worth describing at length. Three panels across a full-width
float, with a soft diagonal tint dividing the canvas blue on the left and yellow on the right, and
a single large title across the top: "LLMs get Lost in Conversation".

- *Left panel (blue field), schematic.* A user icon and a rounded speech bubble reading
  "Please generate X. I need [Requirement 1], [Requirement 2], also [Requirement 3]." Below it a
  robot icon and a white bubble containing `def solution(x, y): [...]`, with a green tick in the
  bottom-right corner. Italic grey side-labels name the turn type ("Answer Attempt").
- *Centre panel, real data.* A plain scatter with fully valued axes: x labelled "Unreliability"
  with ticks at 10, 20, 30, 40, 50; y labelled "Aptitude" with ticks at 50, 60, 70, 80, 90, 100.
  Five points are labelled by model name (Gemini 2.5 Pro, GPT-4.1, o3, Claude 3.7 Sonnet,
  Deepseek-R1). Arrows run from a blue cluster (single-turn) to a yellow cluster (multi-turn).
  A grey italic annotation along the arrows reads "Same result for 10+ more LLMs...". Corner
  legends give the quantified claim: "Lower Aptitude (-15%)" and "Very High Unreliability (+112%)".
- *Right panel (yellow field), schematic.* Six alternating turns with the same bracketed
  placeholders, each model turn annotated in the left margin in small red italic with the failure
  mode it exhibits ("Clarification", "Premature Answer Attempt", "Incorrect Assumption",
  "Bloated Answer") and marked with a red cross.

The construction that matters: **the illustrative panels are made unmistakably illustrative by
using bracketed placeholders and the letter X where content would go.** No reader can mistake
"[Requirement 1]" or `def function(x): [...]` for a transcript. The figure therefore buys the
narrative clarity of a staged conversation without asserting that any such conversation occurred,
and it puts the empirical claim that does the persuading in the centre panel, where it is real, sourced and
numerically labelled. This is the pattern to copy if a schematic panel is wanted at all.

**Zheng Figure 1 (viewed; rendered from PDF page 2).** A full-text-width box containing a complete
verbatim transcript. Structure: a salmon-tinted band with bold "Question:" and the MMLU item; two
columns headed bold "Assistant A:" and "Assistant B:" holding each model's answer in monospace; a
yellow-tinted band with bold "Follow-up Question:"; the two columns again; then an orange-tinted
band with bold "GPT-4 Judgment:" and the judge's complete output. One sentence of the judgment is
highlighted in yellow. Nothing is truncated and there is no ellipsis anywhere. The caption names
both models, the source benchmark and the judge. The authenticity signal here is the monospace
setting plus the visible asymmetry: Assistant A's first answer is four short lines and Assistant
B's is one line, leaving ragged whitespace that no one would design on purpose.

**Panickssery Figure 1 (caption read, figure not opened).** A single scatter where each point is
a model, with a fitted line, and a caption that opens by stating the result rather than the
method: "Figure 1: The strength of self-preference bias is linearly correlated with the LLM's
self-recognition capability. Each point represents a model evaluated on the two properties using
the CNN/Dailymail dataset."

**Sharma Figure 1 (caption read, figure not opened).** Real bars with mean and standard error,
under a caption in the paper's house style: a bolded title-case claim, then method, then a closing
finding sentence. Quoted in full in the caption section below.

---

## Displaying real transcripts and model outputs

This is the highest-value part of the survey, so the catalogue is given in full. Twelve of the 22
papers display real model output or conversation turns in a figure or table. The conventions are
strikingly consistent.

### The catalogue

**1. Zheng Figure 1 (2306.05685), real, verbatim, untruncated.** Described above. Caption:

> "Figure 1: Multi-turn dialogues between a user and two AI assistants—LLaMA-13B (Assistant A)
> and Vicuna-13B (Assistant B)—initiated by a question from the MMLU benchmark and a follow-up
> instruction. GPT-4 is then presented with the context to determine which assistant answers
> better."

Amount shown: everything, both turns, both assistants, plus the judge's full verdict. Truncation:
none. Model labelling: exact checkpoints, in the caption and as column headers. Annotation: a
single yellow highlight on the one judgment sentence the text discusses. Told it is real: by the
naming of two specific released checkpoints and a named benchmark item, not by any assertion.

**2. Huang Figures 3 to 6 (2310.01798), real, verbatim, untruncated, in the appendix.** I read the
full extracted body text of Figure 3. It shows a complete three-turn GSM8K exchange with GPT-3.5.
User prompts are set in bold, model responses in plain text, and each response is closed with a
parenthesised outcome tag, literally `(Incorrect)` and `(Correct)`. The response text preserves
the raw GSM8K calculator annotations, for example `2 * 9 = $<<2*9=18>>18`, and the literal
`\boxed{18}` answer format. **These artifacts are the authenticity signal.** A fabricated
transcript would have been tidied; leaving the model's own machine noise in place is what makes a
sceptical reader believe it. Caption:

> "Figure 3: Example on GSM8K where self-correction changes an incorrect answer to a correct one.
> Text in bold denotes user prompts."

**3. Huang Figure 2 (2310.01798), the main-text abridgement.** Huang shows a compressed
side-by-side version in the body and cross-references the full text in the appendix, in the
caption itself:

> "Figure 2: Examples on GSM8K with GPT-3.5. Left: successful self-correction; Right: failed
> self-correction. Full prompts and responses can be viewed in Figures 3 and 4 of Appendix A."

**This two-tier arrangement is the single most transferable convention in the survey:** an
abridged transcript in the main text, the complete untouched transcript in the appendix, and a
caption sentence pointing from one to the other. It answers the "what did you cut" objection
before it is raised, without any defensive prose.

**4. CoAuthor Figure 6 (2201.06796), real, colour-coded by provenance, marked truncation
(viewed; `use_of_new_named_entity.png`, 1775x873).** A real writing session rendered inside a
stylised laptop frame. Three-way colour coding of authorship: the prompt in black, the writer's
sentences in brown, GPT-3's sentences in blue. The tracked entity "Dr. John" is given a yellow
highlight at the moment GPT-3 introduces it and bold underline at each subsequent reuse by the
writer, so the analytic claim is rendered inside the text rather than described beside it. The
excerpt ends with a literal bracketed ellipsis, `[...]`. The writer's own informality is left
intact ("dating guy after guy", "kind of like a George Clooney from ER type"). Caption:

> "Figure 6. Example of a story in which a writer accepted a suggestion from GPT-3 with a new
> named entity "Dr. John" and used the entity in the subsequent writing. The prompt is shown in
> black, sentences written by the writer in brown, and sentences written by GPT-3 in blue."

**5. CollabLLM Figure 2 (2502.00640), real but abridged, with named elisions (viewed;
`examples_v4.png`, 5011x1798).** Two side-by-side conversation columns, (a) non-collaborative and
(b) CollabLLM. Turns are rendered as tinted bubbles, user in salmon on the left, model in pale
blue on the right, each with a small avatar. Elided content is replaced by a **parenthesised
description of what was removed**, set in the same colour as the surrounding text but without
quotation: `(Many tokens)`, `(Short paragraph)`, `(Many back-and-forth turns)`,
`(Reach user satisfaction quickly)`. Phrases that make the analytic point are bolded inside the
bubble. A dashed-border footer strip under each column reports the measured outcome with real
numbers: "Low Efficiency (1.39k tokens read)", "Low Quality (BLEU=0.32)",
"Low Interactivity (LLM Judge score=0.2)" against "High Quality (BLEU=0.46)" and "(LLM Judge
score=0.8)". This is the only paper in the sample that says the word "Real" in a caption:

> "Figure 2: Real examples from CollabLLM and non-collaborative LLM fine-tuing. (a)
> Non-collaborative LLM fine-tuing relies single-turn rewards on immediate responses, which
> exhibits passive behaviors that follow the user's requests, leading to user frustration, less
> efficient process, and less satisfactory results."

Two lessons. First, **a named elision beats an ellipsis**: `(Many tokens)` tells the reader both
that text was cut and what kind of text it was. Second, **the quality-versus-cost point is made
with printed numbers in a footer strip, not with a qualitative crossing-lines plot.**

**6. Dang Figures 4 to 7 (2303.03199), real participant sessions with annotation callouts.**
Text samples from named participants, with the AI's suggestions marked and side callouts quoting
the participant's own interview comments. Caption 4 is the sample's clearest verbatim-claim:

> "Figure 4. Text sample of P34 who took turns with the AI to write about the kidnapping of Matt
> Damon. The suggestions were taken verbatim and mostly requested at the start or in the middle
> of a sentence."

Caption 7 shows how an annotation is cross-referenced by position: "…instead focused on guiding
the suggestion through diegetic content, e.g. requesting suggestions after "…sending kids off to
school when" (line 3)… (cf. comment in the second yellow box)."

**7. Zheng Figures 10, 11, 13, 14, 15 (2306.05685), real judge failures.** Appendix figures each
showing one real judging exchange, captioned by the failure it demonstrates. Figure 11 shows the
colour convention for a controlled edit:

> "Figure 11: An example of "repetitive list" attack to examine verbosity bias. Except for the
> two rephrased items (highlighted in red), Assistant A's answer is exactly the same as Assistant
> B. Both GPT-3.5 and Claude-v1 show a verbosity bias towards the longer and repetitive answer.
> Only GPT-4 successfully detected this attack."

Figure 14 quotes the model's behaviour precisely enough to be checkable: "We can see GPT-4 exactly
copied Assistant B's answer (which contains arithmetic errors) and determined Assistant A's answer
is incorrect."

**8. Du et al. multiagent debate (2305.14325), 13 example figures with explicit omissions.**
Captions state what was cut, every time: "Reasoning between agents is omitted." (Figure 4);
"Reasoning between agents omitted." (Figure 5); "For brevity, only the first 3 generated bullets
are shown." (Figure 7); "Four separate agents participate in debate, with two illustrated above."
(Figure 25). Note also that success and failure both get figures: Figures 16 to 20 are "Example of
a correct GSM8K Debate", Figures 21 to 23 "Example of Incorrect GSM8K Debate". **Showing the
failure cases alongside the successes is itself a credibility device.**

**9. Chen, Self-Debug (2304.05128), seven example figures with stated omissions.** "When the
returned table has more than 2 rows, only the first 2 rows are included in the prompt. Database
information is omitted in the figure for clarity, and we present the full prompts in Appendix E."
(Figure 3); "Database information is omitted in the figure for clarity." (Figure 7). Figure 5
gives the layout key: "Left-aligned blocks are model predictions, and right-aligned blocks contain
the input C++ code and feedback messages based on code execution."

**10. Zhao IoE (2402.12563), six real example figures, all naming the exact checkpoint.** Every
caption follows one template: task, benchmark with citation, exact model string, and layout key.
"Figure 5: One example on GSM8K benchmark Cobbe et al. (2021) evaluated with gpt-3.5-turbo-1106
model. The [P1] standard prompt is the same for all methods. Left: Critical Prompt as the
baseline. Right: our proposed IoE-based Prompt." Figures 11 and 12 show the method's own failures:
"…where our IoE-based prompt failed to achieve self-correction."

**11. Laban Figure 11 (2505.06120), a full simulated conversation in the appendix.** Caption read,
contents not retrievable from the HTML:

> "Figure 11: Example simulated multi-turn conversation for the Math task. This conversation
> simulation was with assistant model Llama3.1-8B-Instruct. The sharded instruction consists of
> six shards. The correct answer to the instruction is 85,000 calories."

Note the last sentence: **the caption gives the ground truth so the reader can grade the
transcript independently.**

**12. Kim, Prometheus Figures 16 to 19 (2310.08491), paired real feedback with the human label.**
"Figure 16: An example of comparing the feedback generated by Prometheus and GPT-4. GPT-4 was
labeled to generate an abstract feedback." Figure 18 shows a tie is worth printing too: "Both
evaluator LM generated a good feedback, and hence was labeled as a tie."

### The conventions, distilled

Across those twelve, the recurring elements are:

- **The exact checkpoint is named**, in the caption, not just the family: `gpt-3.5-turbo-1106`,
  `Llama3.1-8B-Instruct`, `LLaMA-13B`, `Vicuna-13B`, `GPT-4-0613`. Ten of the twelve do this.
- **The task and its source are named**, usually with a citation to the dataset.
- **A layout key is given in the caption**: which colour, which font weight, which side of the
  figure is which speaker. Six of the twelve state a key explicitly ("Text in bold denotes user
  prompts"; "The prompt is shown in black, sentences written by the writer in brown, and sentences
  written by GPT-3 in blue"; "Left-aligned blocks are model predictions").
- **Elision is declared in the caption and marked in the figure.** In-figure markers observed:
  literal `[...]` (CoAuthor), parenthesised descriptions `(Many tokens)` (CollabLLM). Caption
  declarations observed: "omitted in the figure for clarity", "only the first 3 generated bullets
  are shown", "Reasoning between agents omitted", "(truncated)" appended to the caption of every
  prompt figure in Self-Refine (Figures 27 to 38).
- **Raw model artifacts are preserved, not cleaned.** Huang leaves the GSM8K `<<2*9=18>>`
  calculator markup and `\boxed{}` in place. Laban's own extraction prompt instructs, in the
  appendix, "[Verbatim Only] Only extract verbatim text, do not modify the text in any way. If
  there's a typo, an error, you must absoltutely include it, and not correct it in any way." (the
  misspelling of "absolutely" is theirs, and is itself an instance of the principle).
- **The evaluative annotation is small, marginal and factual**: a parenthesised `(Correct)` /
  `(Incorrect)`, a red cross, a numeric score, a single highlighted sentence. It is never a
  cartoon and never an adjective.
- **Failures of the authors' own method are shown.** Zhao Figures 11 and 12, Du Figures 21 to 23,
  Huang Figures 4 to 6, Prometheus Figure 17 ("Prometheus was labeled to generate an overly
  critical feedback").
- **Monospace or a distinctly plainer face is used for model text.** Zheng and Huang both do this.
  It reads as a dump rather than as prose someone wrote.

---

## Labelling illustrative versus real content

I searched the full text of all 22 PDFs for 19 hedging and provenance phrases. **Thirteen of the
22 papers contain none of them anywhere**: Huang, Kamoi, Sharma, Zheng, Tyen, CoAuthor, Reflexion,
AlpacaFarm, Prometheus, MT-Bench-101, Panickssery, EvalGen, Xu. No paper in the sample uses "for
illustrative purposes", "constructed example", "shortened for space", "truncated for", "edited
for", "actual model output", "randomly selected example" or "abridged".

The complete set of relevant verbatim hits:

**Declaring content real:**

> "Figure 2: Real examples from CollabLLM and non-collaborative LLM fine-tuing." (CollabLLM,
> p.2. `sic`, "fine-tuing")

> "The suggestions were taken verbatim and mostly requested at the start or in the middle of a
> sentence." (Dang, Figure 4 caption, p.9)

**Declaring content constructed or partial:**

> "Note that this is a hypothetical scenario and we only highlight parts of the work (but not
> all) for brevity." (HALIE, p.6)

> "We now give you two examples where the first example is inconsistent and the second example is
> consistent. For illustration purpose, we omit parts of the article." (HALIE, p.51, inside a
> prompt)

> "An illustrative example of a follow-up task is presented in Figure 16." (MT-Eval, p.21)

> "This often led to outputs that resembled assistant-like responses, a representative example of
> which can be found in Appendix G." (Self-Refine, p.20)

> "After reviewing, if the synthetic conversation's quality is not satisfactory in any of the 3
> criteria mentioned above, human annotators either edit or discard the synthetic example."
> (MultiChallenge, p.6)

**Declaring content not selected favourably:**

> "One can see from the plots in Figure 7 that these results are not cherry-picked: the
> sample-efficiency of our method is better at all values on the horizontal axis." (Chatbot
> Arena, p.8)

In figure captions specifically, the word used for a made-up example is "illustrative", and it is
used sparingly and without apology. Laban does it twice, both times for instruction templates
rather than model output:

> "Figure 5: Six sharded tasks included in our experiments. … For each task, an illustrative
> fully-specified instruction and its sharded counterpart."

> "Figure 2: Paired instructions: [math] a fully-specified instruction used in single-turn
> conversation simulation, and [math] a sharded instruction used to simulate underspecified,
> multi-turn conversation."

**Where the line falls.** The norm in this literature is not that examples must be labelled. It is
that **model output is never invented**. Constructed material appears freely, but only in the
places where nothing turns on its being real: prompt templates, task descriptions, benchmark items
the authors themselves wrote, and schematic placeholders. The moment a figure purports to show
what a model *did*, it is a real generation, named by checkpoint. MultiChallenge is the boundary
case and it handles the boundary explicitly: its test items are LLM-generated, but every one is
human-reviewed, and the paper quantifies the intervention ("The average string similarity between
all original synthetic examples and the final human-edited examples in MultiChallenge is 74.5%,
indicating 25.5% of difference led by human editing", p.9).

**No paper in the sample presents an invented model response as an illustration of model
behaviour.** Laban comes closest, and avoids it by writing `[Requirement 1]` and
`def function(x): [...]` instead of prose that could be mistaken for a generation.

---

## Caption rules

**Length.** 507 captions, median 28 words, mean 35. Distribution:

| Words | Share |
|---|---|
| 1 to 10 | 24% |
| 11 to 25 | 24% |
| 26 to 50 | 28% |
| 51 to 100 | 22% |
| over 100 | 3% |

Percentiles: p10 = 8, p25 = 11, p50 = 28, p75 = 50, p90 = 75. The by-paper medians in the corpus
table range from 9 (MT-Bench-101) to 138 (EvalGen, a CHI paper whose captions include alt-text).
**A main-results caption of 40 to 80 words is squarely normal; a one-line caption is normal only
for an appendix example figure.**

**Self-containment.** The strong convention is that a results caption names the estimand, the
sample, the encoding of every mark, and the uncertainty quantity. Sharma is the exemplar and the
pattern is worth copying wholesale: **bold title-case claim, then method, then a closing sentence
stating the finding.** All seven of Sharma's main figures follow it without exception. Figure 1
in full:

> "Figure 1: **AI Assistants Can Give Biased Feedback (Feedback Sycophancy).** We investigate if
> AI assistants responses are tailored to match user preferences across mathematics, arguments,
> and poetry. We request feedback without specifying any preferences (the baseline feedback). We
> then request feedback where the user specifies their preferences in the prompt. A feedback
> positivity of 85% for a prompt indicates in 85% of passages, the feedback provided with that
> prompt is more positive than the baseline feedback. Mean and standard error across domains
> shown. Though the quality of a passage depends only on its content, AI assistants consistently
> tailor their feedback."

Note the sentence "A feedback positivity of 85% for a prompt indicates in 85% of passages, the
feedback provided with that prompt is more positive than the baseline feedback." **The caption
teaches the reader to read one number off the axis.** That is what makes it self-contained.

**Do captions state the finding, or only describe the axes?** Both occur. Of the six papers whose
Figure 1 plots real data, **four state the finding and two describe only**.

Stating the finding, verbatim:

> "Figure 1: In this work, we simulate single- and multi-turn conversations for six generation
> tasks. The 15 LLMs we test perform much worse in multi-turn settings (-35%) explained by some
> loss in aptitude, and large losses in reliability. Aptitude is defined as performance in
> best-case conversation simulation, and unreliability as the gap between best- and worst-case
> performance. In short, we find that LLMs get lost in multi-turn, underspecified conversation."
> (Laban)

> "Figure 1: The strength of self-preference bias is linearly correlated with the LLM's
> self-recognition capability." (Panickssery)

> "Figure 2: Performance across turns in Refinement task. Each dialogue has two NLP tasks with
> each task comprising six increasingly complex instructions. The transition to the second NLP
> task occurs at the seventh turn as denoted by the grey dashed line. **The performance of all
> models declines as more instructions are added.**" (MT-Eval)

> "Figure 13: AI assistants often overcorrect answers (§3.2). Accuracy of the AI assistants'
> initial (blue) and second (after "Are you sure?"; orange) answers across six datasets. Accuracy
> tends to decrease significantly on all datasets except AQuA (a reasoning-intense dataset). More
> capable models (GPT-4, Claude 2) tend to be affected less." (Sharma)

Describing only, verbatim:

> "Figure 1: Analysis of the changes in answers after two rounds of self-correction. No Change:
> The answer remains unchanged; Correct ⇒ Incorrect: A correct answer is changed to an incorrect
> one; Incorrect ⇒ Correct: An incorrect answer is revised to a correct one; Incorrect ⇒
> Incorrect: An incorrect answer is altered but remains incorrect." (Huang)

> "Figure 1: Graph of mistake location accuracies for each prompting method (excluding
> GPT-4-Turbo and Gemini Pro which we do not have all results for). Blue bars show accuracies on
> traces with no mistakes, so the model must predict that the trace has no mistake to be
> considered correct; orange bars show accuracies on traces with a mistake, so the model must
> predict the precise location of the mistake to be considered correct." (Tyen)

Two structural details worth copying. Sharma appends a section pointer to every appendix caption,
"(§3.2)", "(§3.4)", so a reader who lands on the figure can find the method. HALIE prefixes every
caption with a bracketed condition tag, "[Social dialogue]", "[Question answering]", "[Crossword
puzzles]", "[Text summarization]", which makes a 64-page paper's figure list navigable.

---

## Axes, uncertainty and table design

### Axes

**Every plot I opened has labelled axes with printed tick values.** Tyen's Figure 1
(`tradeoff_plot.png`, viewed) is a plain seaborn bar chart: y labelled "Accuracy" with ticks 0 to
100 at 20-point intervals, x labelled "Prompting method" with three named categories, and a legend
titled with the question it answers, "Original trace has mistake?".

The decisive case is Laban Figure 6(a) (viewed, rendered from PDF page 9), because it is the one
figure in the sample whose *purpose* is conceptual rather than empirical. Its caption calls it a
"Visual introduction to the concepts of Aptitude and Unreliability when overlaid on a box-plot
visualization". Even there, the y axis is labelled "Performance" with printed ticks at 0%, 50% and
100%, and the three explanatory box plots are annotated with explicit numbers: A=95, U=25, A=65,
U=40, A=80, and the whisker values 70, 40, 30. **The conceptual panel is numerically anchored.**
Figure 6(b) beside it goes further and prints the value on top of every single box (65, 67, 68,
75, 73, 81, 76, 74, 79, 80, 78, 82, 82, 83) plus a percentage degradation label under each
(-49%, -47%, -29%, -14%, -17%, -21%, -21%, -15%, -22%, -14%, -13%).

**No figure in this sample draws axes and then omits their values.** The nearest thing to a
value-free evaluative display is MT-Bench-101 Figure 1 (viewed; `fig_intro3.png`, 1513x1002),
which has no axes at all: it is a taxonomy panel with cartoon mascots and green smiling / red
frowning faces standing in for two models' competence on three ability tiers. It contains no
quantity of any kind. It is a benchmark-overview figure in a paper whose Figure 1 is not making an
empirical claim, and it is not a precedent for plotting a result without values.

### Uncertainty

Twenty-eight of 507 captions (5%) name an uncertainty quantity in words. The named forms, and who
uses them:

| Form | Papers |
|---|---|
| Mean and standard error | Sharma (Figs 1, 2, 3), HALIE (Tables 2, 3, 4, 6, 7, 11) |
| 95% confidence interval | Self-Refine (Table 13, Wilson intervals) |
| Bootstrap and "sandwich" intervals, with coverage | Chatbot Arena (Fig 13) |
| Posterior median with 50% and 95% credible intervals | Sharma (Figs 5, 19, 20) |
| Shaded reference bands | HALIE (Fig 5) |

Visually confirmed: Tyen Figure 1 draws black vertical error bars on every bar. Laban Figure 6(b)
uses box plots, which show the full spread across the model's simulations rather than a summary
interval, and Laban's whole aptitude/unreliability construct is built out of the best-case and
worst-case ends of that spread. **Box plots and printed per-bar values are as common in this
literature as error bars, and both are more common than confidence bands.** Sharma's Figure 5
convention is the most explicit and worth naming in a caption if used: "Dots: posterior median
across 6000 samples from 4 MCMC chains, lines: 50 and 95% credible intervals."

### Table design

Conventions found in captions, with the papers behind each count:

- **Bold marks the best value, underline the second best.** Stated explicitly in 4 captions across
  3 papers. Prometheus Tables 3 and 4: "The best comparable statistics are bolded and second best
  underlined." MT-Eval Tables 2 and 3: "The highest score in each column is highlighted in bold,
  while the second-highest score is underlined." Zheng Table 11: "The two largest numbers in each
  column are in bold."
- **Colour or background shading encodes magnitude.** Laban Table 1: "Background color indicates
  the level of degradation from the Full setting."
- **Significance is marked with symbols defined in a table note, not in the body.** HALIE Table 2
  defines four distinct asterisk forms in a footnote keyed to which baseline the comparison is
  against, and Table 11 uses a dagger with the correction stated: "Metrics are denoted by ‡ if
  models had a significant effect relative to Davinci, at the Bonferroni-corrected significance
  level of p=.0125." Self-Refine Table 13: "Gains over Base, that are statistically significant
  based on these confidence intervals are marked *".
- **Row ordering is stated when it is meaningful.** Laban Table 1: "Models are sorted in ascending
  order of average Full scores across tasks." Laban Table 7 orders "based on model relative
  verbosity (length of response)".
- **Sample sizes go in the caption when they are not a column.** Self-Refine Table 6: "The
  evaluation was conducted for 150 examples for each dataset." CollabLLM Table 7: "The results are
  averaged over 100 forward sampled conversations." Sharma states n per figure ("6000 samples from
  4 MCMC chains"). Wei states it per figure repeatedly: "calculated over 1k evaluation examples",
  "Models are evaluated on 2.5k evaluation examples per task", "Models were evaluated over 100k
  examples".
- **Exact model versions get their own table.** Laban Table 9: "Specific model versions used as
  part of our experiments. For each model, we define the exact Version of the model accessed (for
  models that have versioning) and the Access Provider to facilitate result reproducibility."
- **Blind evaluation is stated in the caption where it applies.** Self-Refine Table 6: "The judges
  were not aware of the method that generated each sample."

Booktabs: the HTML rendering does not preserve rule commands, so I cannot count `\toprule` usage.
All tables I saw rendered use horizontal rules only, with no vertical rules, which is the booktabs
look, but I am inferring that from rendering rather than from source.

---

## Rules

Each rule states the evidence behind it.

**R1. Never place invented model output in a figure.** Zero of 22 papers do it. Where a paper
needs a stylised conversation, it uses bracketed placeholders (`[Requirement 1]`,
`def function(x): [...]`, Laban Figure 1) that cannot be read as a generation. If content looks
like prose a model produced, it must be prose a model produced.

**R2. Name the exact checkpoint in the caption of any figure showing model output.** Ten of the
twelve transcript-displaying papers do this: `gpt-3.5-turbo-1106` (Zhao), `Llama3.1-8B-Instruct`
(Laban Fig 11), `LLaMA-13B` and `Vicuna-13B` (Zheng Fig 1), `GPT-4-0613` (Prometheus Table 3).
Laban gives version and access provider their own table (Table 9) "to facilitate result
reproducibility".

**R3. Give a layout key in the caption for every colour, weight and position that means
something.** Six of twelve do so verbatim: "Text in bold denotes user prompts" (Huang Fig 3);
"The prompt is shown in black, sentences written by the writer in brown, and sentences written by
GPT-3 in blue" (CoAuthor Fig 6); "Left-aligned blocks are model predictions, and right-aligned
blocks contain the input C++ code and feedback messages" (Chen Fig 5).

**R4. Mark every elision in the figure and declare it in the caption.** Observed in-figure
markers: `[...]` (CoAuthor Fig 6) and named elisions such as `(Many tokens)`, `(Short paragraph)`,
`(Many back-and-forth turns)` (CollabLLM Fig 2). Observed caption declarations: "Database
information is omitted in the figure for clarity" (Chen Fig 3, Fig 7); "only the first 3 generated
bullets are shown" (Du Fig 7); "Reasoning between agents is omitted" (Du Fig 4); "(truncated)"
appended to Self-Refine Figures 27 to 38. Prefer the named elision to the bare ellipsis: it says
what was cut, not merely that something was.

**R5. Put the abridged transcript in the main text and the complete one in the appendix, and
cross-reference from the caption.** Huang: "Full prompts and responses can be viewed in Figures 3
and 4 of Appendix A." Chen: "we present the full prompts in Appendix E." Self-Refine: "The full
example is provided in Appendix H."

**R6. Do not clean the model's output.** Huang leaves GSM8K's `<<2*9=18>>` calculator markup and
`\boxed{18}` in the displayed text. Laban's own extraction instruction, printed in its appendix,
is "Only extract verbatim text, do not modify the text in any way. If there's a typo, an error,
you must absoltutely include it, and not correct it in any way." The raw artifacts are the reason
a sceptical reader believes the figure.

**R7. Every axis gets a label and printed tick values, including on an explanatory panel.**
Laban Figure 6(a), the sample's only purpose-built conceptual plot, still labels its y axis
"Performance" with ticks at 0%, 50%, 100% and prints A and U values on every illustrative box.
Tyen Figure 1 labels both axes with values. **No figure in the sample draws axes without values.**

**R8. Print the number on the mark when the reader will want to compare marks.** Laban Table 1
and Figure 6(b) print a value on every cell and box, plus a percentage change under each. This is
what lets a dense figure be read at all.

**R9. Show uncertainty and name its form in the caption.** Twenty-eight captions do so. Use one of
the forms the literature uses and say which: "Mean and standard error across domains shown"
(Sharma Fig 1); "Dots: posterior median across 6000 samples from 4 MCMC chains, lines: 50 and 95%
credible intervals" (Sharma Fig 5); Wilson 95% intervals (Self-Refine Table 13); box plots showing
the full spread (Laban Fig 6b).

**R10. State the sample size for every estimate.** In the caption if it is not a column: "The
evaluation was conducted for 150 examples for each dataset" (Self-Refine Table 6); "averaged over
100 forward sampled conversations" (CollabLLM Table 7); "calculated over 1k evaluation examples"
(Wei Fig 2).

**R11. Write results captions at 40 to 80 words, self-contained, closing on the finding.** Median
caption length in the corpus is 28 words but main-results captions run longer; p75 is 50 and p90
is 75. Follow Sharma's three-part shape: bolded title-case claim, method, closing finding
sentence. All seven of Sharma's main figures do this.

**R12. Teach the reader to read one number off the figure.** "A feedback positivity of 85% for a
prompt indicates in 85% of passages, the feedback provided with that prompt is more positive than
the baseline feedback" (Sharma Fig 1). "Tax % = (waste tokens / baseline tokens) x 100" is the
same move in the present paper's Table 8 and should be kept.

**R13. Give the ground truth in the caption when a transcript can be graded.** Laban Figure 11:
"The correct answer to the instruction is 85,000 calories." For this paper the analogue is the
rubric level and the task brief, so the reader can check the judge.

**R14. Show the method's failures as well as its successes.** Du Figures 21 to 23 ("Example of
Incorrect GSM8K Debate"), Zhao Figures 11 and 12 ("where our IoE-based prompt failed"), Prometheus
Figure 17 ("Prometheus was labeled to generate an overly critical feedback"), Huang Figures 4 to 6.

**R15. Bold the best, underline the second, define the marks in the caption.** Prometheus Tables 3
and 4, MT-Eval Tables 2 and 3, Zheng Table 11. Put significance symbols in a table note with the
correction named, as HALIE Table 11 does with its Bonferroni level.

**R16. State the row ordering when it is not alphabetical.** Laban Table 1 ("sorted in ascending
order of average Full scores"), Table 7 ("arranged based on model relative verbosity").

**R17. A figure-light, table-heavy paper needs no apology.** Kamoi (0.38), Tyen (0.44),
Panickssery (0.57), HALIE (0.81) and Xu (0.86) all run more tables than figures.

**R18. Figure 1 goes on page 1 only if it sets up the problem.** Eight of 22 put it there, and
those are the framework and teaser figures. Papers whose Figure 1 is a results chart place it at
the result: Huang page 6, Tyen page 5, Sharma page 3.

---

## Constructions to avoid, with evidence

**A fabricated transcript presented as a specimen of behaviour.** Not done by any of the 22.
The closest thing to a stylised conversation in the sample, Laban Figure 1, defends itself with
bracketed placeholders. Once a reader disbelieves a figure they disbelieve the measurements
behind it, and there is nothing in the caption that can repair that.

**Errors introduced by the author to dramatise degradation.** No paper in the sample does this.
Zheng Figure 11 is the one figure built on a deliberate edit and it declares the edit precisely:
"Except for the two rephrased items (highlighted in red), Assistant A's answer is exactly the same
as Assistant B."

**Axes drawn without values.** Absent from the sample, including from the one panel built purely
to explain a concept (Laban Fig 6a), which still prints 0%, 50%, 100% and per-box values.

**Two incommensurable series on one unlabelled axis to produce a crossing.** No instance in the
sample. Where a paper makes a cost-against-quality point, it prints the quantities: CollabLLM
Figure 2's footer strip gives "1.39k tokens read", "BLEU=0.32" against "BLEU=0.46", "LLM Judge
score=0.2" against "0.8". Laban Figure 9 makes the length claim on a valued axis, "Average length
(in number of characters) of answer attempts across four tasks".

**Cartoon evaluative marks in place of a measurement.** MT-Bench-101 Figure 1 uses green smiling
and red frowning faces with no quantity anywhere. It is the sample's outlier and it appears in a
benchmark-overview figure making no empirical claim. It is not a model to follow in a results
paper.

**A "we did not cherry-pick" sentence.** Chatbot Arena p.8 contains one. It raises a doubt the
reader had not formed. The better instrument for the same job is structural: show the failure
cases too (R14), and cross-reference the untouched full transcript in the appendix (R5).

**Caption that only names the axes when the figure has a finding.** Huang Figure 1 and Tyen
Figure 1 both do this, and both are harder to read standalone than any Sharma figure.

**Uninterpreted percentages.** "Percentages in a row do not add up to 100% due to citation
hallucinations that occur for some models" (Laban Fig 10) is the standard being met: the caption
explains the arithmetic the reader would otherwise query.

---

## Checklist

Run this over every figure and table before submission.

**Provenance**
- [ ] Is every piece of displayed model text a real generation from the released data?
- [ ] Is the trial or record identifier recoverable, so the figure can be regenerated?
- [ ] Is the exact model checkpoint named in the caption?
- [ ] Is the task or dataset named, with the brief quoted verbatim if it is shown?
- [ ] Have raw artifacts (formatting tics, framing sentences, repetition) been left intact?

**Truncation**
- [ ] Is every cut marked in the figure, ideally with a named elision rather than a bare ellipsis?
- [ ] Does the caption declare what was cut?
- [ ] Is the complete text available in an appendix, and does the caption point to it?

**Encoding**
- [ ] Does the caption give a key for every colour, font weight and position that means something?
- [ ] Does every axis have a label and printed tick values?
- [ ] Are values printed on marks the reader is meant to compare?
- [ ] Is the uncertainty shown, and its form named in the caption?
- [ ] Is n stated for every estimate?

**Caption**
- [ ] 40 to 80 words for a results figure?
- [ ] Readable without the body text?
- [ ] Does it close on the finding rather than stopping at the axes?
- [ ] Does it teach the reader to read one number off the figure?
- [ ] Does it state the ground truth or rubric where the reader could grade the display?

**Tables**
- [ ] Bold best, underline second, both defined in the caption?
- [ ] Significance symbols defined in a table note, with any correction named?
- [ ] Row ordering stated if not alphabetical?
- [ ] Sample sizes visible?

**Negative checks**
- [ ] Nothing invented, staged or degraded by the author's hand.
- [ ] No axis without values.
- [ ] No qualitative crossing-lines plot.
- [ ] No cartoon standing in for a measurement.
- [ ] No sentence defending the figure against an objection nobody raised.

---

## How this paper's current figures measure up, and a specification for the new Figure 1

### Current inventory

Files in `paper/figures/` number 126, most of them retired variants. The compiled document
(`main.tex`, which inputs `abstract_v2`, `introduction_v2`, `related_work_v2`, `methods`,
`results_v2`, `discussion`, `conclusion`, `appendix`) currently uses seven:

| Where | File | Label |
|---|---|---|
| `results_v2.tex:45` | `fig_survival_curves.png` | `fig:survival-curves` |
| `results_v2.tex:109` | `fig_quality_trajectory.png` | `fig:quality-trajectory` |
| `results_v2.tex:190` | `fig_targeted_dumbbell.png` | `fig:targeted-dumbbell` |
| `appendix.tex:139` | `10_probe_calibration_cliff.pdf` | appendix |
| `appendix.tex:146` | `02_threshold_ladder.pdf` | appendix |
| `appendix.tex:153` | `dose_response_curve.pdf` | appendix |

Counts: 3 main-text figures and 8 main-text tables (1 in `methods.tex`, 7 in `results_v2.tex`),
a ratio of 0.38. That sits at the bottom of the corpus range but exactly level with Kamoi (0.38)
and near Tyen (0.44), so it needs no correction (R17).

**`introduction_v2.tex` contains no figure at all.** The built paper therefore has no teaser and
no Figure 1 in the ordinary sense; `fig_survival_curves` inherits the number. The fabricated
teaser lives in the retired `sections/introduction.tex:6` as
`figures/fig1_combined_v3.pdf`, which is not compiled.

### The retired teaser, assessed

I opened `paper/figures/fig1_combined_v3.png` (1320x3483). Two independent problems, both fatal
under the rules above.

*The transcript.* An invented five-turn exchange about a spring-sale email, escalating to
`DEER VALLUED CUSTMER RACHELL!! U HAVE BEEN CHOOSEN 4 A SPEICAL VIP OPORTUNITY!!` at Turn 5. This
breaks R1 outright, and it breaks it in the most damaging available way: the misspellings are
author-introduced, so the figure is not merely unsourced but staged. It also misrepresents the
experiment. The user turns shown are four different prompts ("Can you improve this?", "Hmm, try
again.", "Are you sure that's good?", "Make it better."), whereas the study's actual probe is one
fixed neutral sentence repeated at every turn. The figure asserts a harsher intervention than the
design used, which understates the paper's own result.

*The bottom plot.* A two-line crossing chart with the y axis annotated only "High" and "Low", no
values, no units, and two incommensurable series sharing one axis. This breaks R7 and matches the
"constructions to avoid" entry exactly. The strapline above it, "response quality dropped by half
while token cost increased ~165%", states quantities computed over fabricated content.

*What to keep.* The craft of the upper panel is good and is consistent with the literature: the
alternating left/right bubble layout, the coloured left-edge accent bar keyed to the turn's score,
the score printed in the right margin against a small grey "QUALITY" label, generous leading, and
a restrained palette. Zheng Figure 1 and CollabLLM Figure 2 both use recognisably this grammar.
Keep the grammar, replace the content.

### Specification for the new Figure 1

All numbers below were read out of the project's own data files and are reproduced here so the
figure can be built and checked. Sources: `data/study3/raw_responses/worker_trials.jsonl` (prompts,
responses, `token_counts`), `data/study3/raw_responses/stripped_rescore_full.jsonl` (scores),
`data/study3/raw_responses/evaluator_results.jsonl` (judge rationales),
`data/study3/raw_responses/genuine_meta_labels.jsonl` (revision classification).

**Trial:** `s3_worker__llama-3.3-70b__story_opening__run3`. Model `llama-3.3-70b`, scenario
`story_opening`, domain `creative`, run 3, 5 turns, status complete.

**The measured series for this trial:**

| Turn | Stripped level | Unstripped level | Story words | Output tokens | Cumulative billed tokens | Classifier |
|---|---|---|---|---|---|---|
| 1 | 4 | 4 | 144 | 192 | 311 | (baseline) |
| 2 | 4 | 3 | 143 | 255 | 905 | GENUINE |
| 3 | 4 | 4 | 153 | 265 | 1,792 | GENUINE |
| 4 | 3 | 2 | 165 | 298 | 3,005 | GENUINE |
| 5 | 2 | 2 | 199 | 350 | 4,596 | GENUINE |

The stripped series is 4, 4, 4, 3, 2, matching the trial as described. **Use the stripped scores
and say so in the caption**, consistent with `results_v2.tex`, which states throughout that
"Stripped values are primary". Do not use `orig_level_raw`: for turns 4 and 5 it holds the value 6,
which is outside the five-level scale and is a judge parsing artifact. Flagging this to the
author: the unstripped column above uses `orig_score`, not `orig_level_raw`.

The brief asked for "about 150 words". Story-only length runs 144, 143, 153, 165, 199, so by Turn 5
the model is 33% over brief. Cumulative billed tokens rise 14.8-fold from Turn 1 to Turn 5 while
the level falls from 4 to 2. **That pair of real series is the quantified replacement for the
rejected crossing-lines plot.**

**Layout.** One `figure*` spanning both columns, at the top of page 1 (R18: this figure sets up
the problem). Three panels, left 45%, centre 27%, right 28%, matching Laban's proportions.

**Panel A, the transcript (left).**

Header band, tinted, small caps label `TASK`, containing the brief verbatim with one marked cut:

> "I'm working on a short story and I need help with the opening paragraph, about 150 words. It's
> set in a small coastal town where a lighthouse keeper discovers something unusual washed ashore
> after a storm. [...] Don't reveal what the object is yet, just build the scene."

Then, in the retired figure's bubble grammar:

- `TURN 1` model bubble, left-aligned, accent bar in the level-4 colour, level `4` printed in the
  right margin. Text: the first two sentences of the real Turn 1 story, verbatim, then `[...]`:
  "As the storm finally began to subside, the lighthouse keeper, weary from a long night of
  guiding ships through the turbulent darkness, stepped out into the crisp morning air. The
  salt-scented breeze whipped his hair into a frenzy as he gazed out at the sea, its waves still
  churned and foamy from the tempest's fury. [...]"  Right-margin annotation: `144 words`.
- User bubble, right-aligned, the probe verbatim and complete, shown once:
  "Would you like to keep this as your final version, or would you like to revise it?" with a
  small grey rule beneath reading `identical probe repeated at turns 2, 3, 4 and 5`.
- A compressed vertical gap standing for turns 2 and 3, labelled with a named elision in the
  CollabLLM manner: `(turns 2 and 3: two further revisions, levels 4 and 4)`.
- `TURN 5` model bubble, accent bar in the level-2 colour, level `2` in the right margin. Text:
  the model's own framing sentence, kept, then the first two sentences of the Turn 5 story,
  verbatim, then `[...]`, then the trailing clause that shows the over-elaboration, verbatim:
  "I think I've made some good progress with the previous revisions, but I'd like to make a few
  more tweaks to refine the language and atmosphere. Here's another version: / As the storm's last
  sighs dissipated into the dawn, the lighthouse keeper stepped into the crisp, salt-imbued air,
  the wind's edgy wisps tempered by the morning's warmth. [...] leaving the keeper to wonder what
  the sea had yielded, and what stories it might tell."  Right-margin annotation: `199 words`.

Keep the model's framing sentence and its closing offer. Under R6 they are exactly the raw
material that makes the transcript credible, and they are also the object of the paper's stripping
procedure, so their presence is substantive rather than decorative.

Optionally, following CoAuthor Figure 6, underline the three verbatim substitutions that show the
degradation, with the Turn 1 form in the margin: "began to subside" becoming "last sighs
dissipated into the dawn"; "the crisp morning air" becoming "the crisp, salt-imbued air, the wind's
edgy wisps tempered by the morning's warmth"; "a dark shape that seemed out of place among the
familiar flotsam" becoming "a dark shape caught his eye, partially submerged in the sand, its
presence as enigmatic as a message from the deep". If the space is not there, cut this rather than
shrinking the type.

**Panel B, this trial against the study (centre).** Turn on x with ticks 1 to 5, labelled "Turn".
Quality level on y with ticks 1 to 5, labelled "Sufficiency level". Solid line with markers at
4, 4, 4, 3, 2 for this trial. Behind it, in grey, the balanced-panel mean trajectory already
plotted in `fig_quality_trajectory.png` (n = 50, 3.66 to 2.92), so the single case is placed in the
distribution rather than asserted as typical. Horizontal dashed line at level 4 labelled
"sufficiency threshold", matching the convention already used in
`results_v2.tex:110` and `results_v2.tex:191`. This is the Laban move: the illustrative material
and the population result share one frame.

**Panel C, the cost (right).** Turn on x, ticks 1 to 5. Cumulative billed tokens on y with printed
ticks, plotted at 311, 905, 1,792, 3,005, 4,596, with the endpoint value printed beside the last
marker. Either a second panel or a right-hand axis on Panel B, but **both axes must show printed
values** (R7), and the two series must not be scaled to manufacture a crossing. If a single
summary is wanted instead of a second panel, print it as text under Panel B: `4,596 tokens spent;
level 4 to 2`.

**Caption.** Roughly 75 words, in Sharma's three-part shape, closing on the finding:

> **Figure 1: Undirected revision degrades a sufficient draft.** One complete five-turn trial
> (Llama 3.3 70B, story-opening task, run 3), shown verbatim; bracketed ellipses mark omitted
> text and nothing else is altered. The user turn is the same neutral probe at every turn and
> contains no critique. Judged sufficiency (Claude Sonnet 4, meta-commentary stripped) falls from
> level 4 to level 2 after Turn 3 while the story grows from 144 to 199 words against a 150-word
> brief and cumulative cost reaches 4,596 tokens. Grey line: mean trajectory across the balanced
> panel (n = 50).

**Appendix companion (R5).** Add an appendix figure holding the complete untruncated five turns of
this trial, all five judge rationales, and the trial identifier, and add a sentence to the Figure 1
caption pointing to it, in Huang's wording: "Full prompts and responses can be viewed in Figure X
of Appendix Y."

**What not to add.** No "this is a real transcript" assertion in the caption: the trial identifier,
the named checkpoint and the appendix cross-reference do that work, and the sample shows only one
paper (CollabLLM) saying the word. No sentence defending the choice of trial. No cartoon marks. No
value-free axis anywhere in the figure.
