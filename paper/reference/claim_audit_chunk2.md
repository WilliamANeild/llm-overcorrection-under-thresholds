# Claim audit, chunk 2

Source of sentences: `paper/sections/related_work_v2.tex`, paragraphs "Human-AI interaction
and user-side determinants of quality", "Over-reliance and automation bias", and the opening
of "Intrinsic self-correction and self-refinement".

8 sentences, 11 claim-source pairs. All sources fetched 2026-09-05 unless noted.

---

## 2.1

> Deployment data show that models are increasingly applied to open-ended workplace tasks rather than the closed, fully specified problems on which they are benchmarked \cite{anthropic2025economicindex}.

### anthropic2025economicindex — PARTIALLY SUPPORTED

Source: https://www.anthropic.com/news/the-anthropic-economic-index
Page dated "Feb 10, 2025". Retrieved 2026-09-05 (full page HTML fetched and read).

What the source does say, verbatim:

> "The Index's initial report provides first-of-its-kind data and analysis based on millions
> of anonymized conversations on Claude.ai, revealing the clearest picture yet of how AI is
> being incorporated into real-world tasks across the modern economy."

> "Today, usage is concentrated in software development and technical writing tasks."

> "Overall, we saw a slight lean towards augmentation, with 57% of tasks being augmented and
> 43% of tasks being automated."

> "We chose tasks according to the classification made by the U.S. Department of Labor, which
> maintains a database of around 20,000 specific work-related tasks called the Occupational
> Information Network, or O*NET."

Three ways the sentence goes past the source.

1. **"increasingly" asserts a trend the cited report does not report.** The February 2025
   report is a single cross-sectional snapshot of roughly one million Claude.ai conversations.
   The page states the trend analysis as future work, not as a finding: "we'll repeat many of
   the analyses above over time to help track the societal and economic changes that are likely
   to occur." Later Economic Index releases do report changes over time; this URL and this
   entry point at the first report.

2. **The benchmark contrast is absent from the source.** The page contains no comparison
   between deployment tasks and benchmark tasks, and never characterises tasks as "open-ended"
   or "closed, fully specified." That contrast is the citing author's framing, not the Index's.

3. **"workplace tasks" is qualified by the source itself.** Under Caveats: "We can't know for
   certain whether someone using Claude for a task was completing a task for work." The data
   are Claude.ai Free and Pro conversations, filtered to occupational-task relevance, not
   enterprise or API traffic: "We also only analyze data from Claude.ai Free and Pro plans,
   rather than API, Team, or Enterprise users."

What is supported: that deployment data map real Claude usage onto O*NET occupational tasks
across the economy, and that usage leans toward augmentation. What is not: the time trend, the
benchmark contrast, and the open-ended/closed dichotomy.

---

## 2.2

> In that setting the user's instructions are often thin: real prompts are frequently underspecified, and underspecification measurably degrades and destabilizes the outputs that follow \cite{yang2025underspecification}.

### yang2025underspecification — PARTIALLY SUPPORTED

Source: https://aclanthology.org/2026.findings-acl.441.pdf (PDF downloaded and read in full).
Retrieved 2026-09-05.

The "degrades and destabilizes" half is well supported, with numbers.

Degrades (Section 3.2, p. 9075):

> "Unsurprisingly, we generally observe that LLM+Prompts are less likely to implement a
> requirement when unspecified – accuracy drops by an average of 22.6% (and up to 93.1%)
> compared to when the requirement is explicitly stated (Figure 2)."

Destabilizes (Section 3.2, p. 9076, and Section 3.3):

> "While LLMs are often able to guess unspecified requirements, we found them less robust with
> unspecified requirements across different prompts: Different prompts can guess unspecified
> requirements completely differently. On average, they have a standard deviation of 8.9%, a
> more than 2x increase compared to when they are specified."

> "5.9% requirements regress more than 20% over model updates when they are unspecified – an
> almost 2x increase compared to specified requirements (Figure 3)."

The scope shift is in "the user's instructions" and "real prompts." This paper is about
**application developers' system prompts**, and it explicitly sets end-user prompts aside
(Section 1, p. 9072):

> "This issue is less significant for end users, as their prompts are typically one-off and
> considered successful as long as they yield one satisfactory response throughout their
> interactions. For LLM application developers, the problem is much more serious, as their
> prompts need to generalize to many different usage scenarios."

The prompts studied are constructed by the authors, not harvested from users: "We use a cyclic
design to construct prompts, where each one includes N consecutive requirements (with N set to
10)." The nearest thing to a prevalence claim about real prompts is about developer prompts:
"65.2% requirements found from existing developer prompts are guessed by LLMs when unspecified.
This indicates that the prompts resulting from existing practices often contain information
that might be redundant to LLMs' default behaviors."

So: the degradation and instability findings transfer; the prevalence claim about *users'*
real prompts is the citing sentence's own extension, and the preceding sentence in the
paragraph (2.1) has already placed the reader in a workplace end-user setting, which is the
setting this paper says it is not about. Note also that Laban et al. (2505.06120, cited two
sentences later) does make the end-user prevalence claim, attributing it to Herlihy et al.

---

## 2.3

> The difficulty is most acute for non-expert users, whom scalable-oversight research identifies as frequently unable to articulate precise intent or to validate a complex output \cite{zhou2026oversight}.

### zhou2026oversight — SUPPORTED

Source: https://arxiv.org/html/2602.04210v1 (full HTML fetched and read).
Retrieved 2026-09-05.

Abstract, verbatim:

> "While models excel at execution, users often struggle to guide them effectively due to
> insufficient domain expertise, the difficulty of articulating precise intent, and the
> inability to reliably validate complex outputs. It presents a critical challenge in scalable
> oversight: enabling humans to responsibly steer AI systems on tasks that surpass their own
> ability to specify or verify."

Introduction, verbatim, naming both halves as named gaps:

> "First, the specification gap: users often provide underspecified instructions, either
> because they lack the knowledge to identify constraints or simply cannot afford the bandwidth
> to detail them exhaustively (Hadfield-Menell et al., 2017; Ray, 2025; Ge et al., 2025).
> Second, the verification gap: as models autonomously execute long-horizon tasks, the
> complexity of their outputs often exceeds the user's capacity to efficiently validate them
> (Wu et al., 2021; Xi et al., 2025)."

Problem formalization, verbatim, tying it to non-experts specifically:

> "The weak human (non-expert): The user H cannot fully specify their intent or reliably verify
> execution outcomes due to limited cognitive bandwidth or insufficient software development
> expertise."

The paper is framed around non-experts throughout (sandwiching protocol, non-expert user
simulator, "enables non-experts to produce expert-level Product Requirement Documents").

One thing the author should know rather than a defect in the citation: the sentence says
"scalable-oversight research identifies," and this is one arXiv preprint from February 2026
standing for the field. The paper itself attributes the two gaps to prior work
(Hadfield-Menell et al. 2017; Wu et al. 2021; Ray 2025; Ge et al. 2025) rather than
establishing them; it establishes a remedy for them. The verb "identifies" is compatible with
that, so the claim holds as written, but a second, older citation would make the field-level
attribution stand on its own.

---

## 2.4

> \citet{laban2025lost} show that this dependence compounds across turns, with accuracy falling when requirements are revealed gradually.

### laban2025lost — PARTIALLY SUPPORTED

Source: https://arxiv.org/html/2505.06120v1 and https://arxiv.org/abs/2505.06120 (full HTML
fetched and read). Retrieved 2026-09-05.

The second half is squarely supported. Design (Section 3):

> "Sharded simulation then ensures that each turn of conversation reveals at most one shard of
> information per conversation turn, enforcing that the instruction is gradually revealed
> through the conversation."

Result (abstract):

> "Our experiments confirm that all the top open- and closed-weight LLMs we test exhibit
> significantly lower performance in multi-turn conversations than single-turn, with an average
> drop of 39% across six generation tasks."

The first half, "compounds across turns," is contradicted by the paper's own test of exactly
that question. Section 6.3, the gradual sharding experiment, varies shard-set size from 2 to 8
holding task complexity fixed, and finds a step at the first split rather than accumulation:

> "We find that both models get lost in conversation (a minor degradation in aptitude and a
> large increase in unreliability) with two-shard instructions and beyond. In other words, the
> gradual sharding experiment indicates that any conversation that involves underspecification
> and occurs in two or more turns leads to models getting lost in conversation. For users, the
> granularity at which information is specified does not majorly impact reliability: providing
> all the information at once (1-shard) is the only effective method to improve reliability."

Two turns costs as much as eight. The degradation does not grow with the number of turns, which
is what "compounds across turns" claims.

Two passages sit nearer to "compounds" but do not carry it: an appendix note that "model answer
attempts get 'bloated' over turns of conversations," and a limitations remark about "compounding
effect of subtle non-determinism over tokens and turns." Neither is a finding that accuracy
falls further with each additional turn.

Also worth noting for accuracy of the number, though the sentence uses none: the abstract says
39%, Figure 1's caption in the same version says -35%, and the paper's decomposition is a 16%
aptitude drop against a 112% increase in unreliability. "Accuracy" is a loose word for the
paper's metric, which averages heterogeneous per-task scores across six generation tasks
including summarization and data-to-text.

---

## 2.5

> Automation bias, the tendency to accept a machine's recommendation and to under-scrutinize it, is documented across decades of studies and affects experts and novices alike \cite{skitka1999automation, parasuraman2010complacency}.

### parasuraman2010complacency — SUPPORTED

Source: https://depositonce.tu-berlin.de/bitstreams/cafd2873-814b-4c59-bab1-addd42e249d2/download
(author copy of Human Factors 52(3):381-410; PDF downloaded and read). Retrieved 2026-09-05.

Structured abstract, verbatim, covering the review scope and the expert/novice claim:

> "Objective: Our aim was to review empirical studies of complacency and bias in human
> interaction with automated and decision support systems and provide an integrated theoretical
> model for their explanation."

> "Automation bias results in making both omission and commission errors when decision aids are
> imperfect. Automation bias occurs in both naive and expert participants, cannot be prevented
> by training or instructions, and can affect decision making in individuals as well as in
> teams."

The definition half, p. 391-392, verbatim:

> "Mosier and Skitka (1996) defined automation bias as resulting from people's using the
> outcome of the decision aid 'as a heuristic replacement for vigilant information seeking and
> processing' (p. 205)."

> "Automation bias eventually can lead to decisions that are not based on a thorough analysis
> of all available information but that are strongly biased by the automatically generated
> advice."

This one citation carries the whole sentence: the definition, the decades of studies, and the
experts-and-novices clause.

### skitka1999automation — UNCHECKABLE (full text), with a scope caveat that is checkable

Source attempted: https://doi.org/10.1006/ijhc.1999.0252. Elsevier, closed access.
Attempted and failed on 2026-09-05: ScienceDirect article page (HTTP 403), ACM DL mirror
(HTTP 403), Semantic Scholar page (empty body returned), SciSpace (empty body returned),
Crossref API (no abstract deposited), OpenAlex (no abstract deposited), Unpaywall (`"oa_status":
"closed"`, `"oa_locations": []`, `"has_repository_copy": false`), scholar.archive.org (no hit).
No verbatim text from the paper itself could be obtained.

What is verifiable about it, from Parasuraman and Manzey's description of this exact study
(p. 393 of the source above), verbatim:

> "provided in a laboratory experiment comparing the performance of nonpilots in a low-fidelity
> flight simulation task with and without automation support, the Workload/Performance
> Simulation (W/PANES; Skitka, Mosier & Burdick, 1999). Participants had to perform three tasks
> simultaneously... During the experiment, automation failures occurred, six in which the
> automation failed to prompt the participants of a critical event and another six in which it
> gave a wrong directive. Only 59% of the former were correctly identified and responded to by
> the participants"

On that secondary evidence, Skitka et al. 1999 tested **nonpilots only**. It is therefore
evidence for automation bias in novices, not for the "experts and novices alike" clause the
sentence attaches to both citations jointly. It is also a single 1999 experiment, so "documented
across decades of studies" is not a description of it. Both of those clauses rest entirely on
Parasuraman and Manzey. The co-citation is not wrong, but only one of the two works supports
the two distinguishing clauses of the sentence.

---

## 2.6

> In AI-assisted decision-making the same pattern holds: fluent explanations and confident presentation raise users' acceptance of model output without improving their ability to separate correct outputs from incorrect ones \cite{bansal2021whole, bucinca2021trust}.

### bansal2021whole — PARTIALLY SUPPORTED

Source: https://arxiv.org/html/2006.14779v3 (full HTML fetched and read). Retrieved 2026-09-05.
Published version: CHI '21, doi 10.1145/3411764.3445717.

The explanations half is exactly this paper's finding. Abstract, verbatim:

> "While we observed complementary improvements from AI augmentation, they were not increased
> by explanations. Rather, explanations increased the chance that humans will accept the AI's
> recommendation, regardless of its correctness."

Introduction, verbatim:

> "We observed complementary performance on every task, but — surprisingly — explanations did
> not appear to offer benefit compared to simply displaying the AI's confidence. Notably,
> explanations increased reliance on recommendations even when the AI was incorrect."

Results, Section 5.1, verbatim:

> "Split the team performance by whether the AI made a mistake (Figure 4B), we observe that
> explaining the top prediction lead to better accuracy when the AI recommendation was correct
> but worse when the AI was incorrect, as in our pilot study."

The overstatement is the phrase "and confident presentation." In Bansal et al., displayed
confidence is the **control condition**, not a manipulation shown to raise acceptance:

> "For both domains, we ran two baseline conditions: unassisted users (Human), as well as a
> simple AI assistance that shows the AI's recommendation and confidence but no explanation
> (Team (Conf))."

> "We did not observe significant improvements over the confidence baseline by displaying
> explanations."

Their confidence-adaptive explanation strategy in fact moved acceptance the other way:
"Across the three datasets, Adaptive explanations successfully reduced the human's tendency to
blindly trust the AI (i.e., decreased agreement) when it was uncertain and more likely to be
incorrect." So this work supports "fluent explanations raise acceptance without improving
discrimination" and does not support the confidence clause bundled into the same sentence.

### bucinca2021trust — PARTIALLY SUPPORTED

Source: https://arxiv.org/pdf/2102.09692 (PDF downloaded and read). Retrieved 2026-09-05.
Published version: PACM HCI 5(CSCW1), Article 188, doi 10.1145/3449287.

What the paper's own experiment establishes, Section 4.1, verbatim:

> "When the top AI predictions were incorrect, however, cognitive forcing functions improved
> the objective metrics (i.e., overall performance, carb source detection performance, carb
> reduction and flavor similarity) significantly more compared to simple explainable AI. Yet,
> performance of participants that completed the task with no AI assistance—no AI category—was
> significantly higher than that of participants' in either cognitive forcing functions or
> simple explainable AI categories when they saw incorrect model predictions."

That last clause does support the "without improving their ability to separate correct from
incorrect" half: with a simple explanation interface, people did worse on incorrect predictions
than people with no AI at all.

Two problems with the rest.

1. **The design has no explanation-versus-no-explanation contrast**, so the paper cannot show
   that explanations *raise* acceptance. Its conditions are a no-AI baseline, two simple
   explainable-AI conditions, and three cognitive-forcing conditions; the reported contrast is
   cognitive forcing against simple explainable AI. The claim that adding explanations increases
   overreliance appears in this paper only as a characterisation of prior work, in the abstract:
   "Adding explanations to the AI decisions does not appear to reduce the overreliance and some
   studies suggest that it might even increase it." That is the paper's motivation, not its
   result.

2. **The confidence clause is contradicted by the one condition that tests it.** The
   "uncertainty" condition displayed confidence alongside the explanation: "the uncertainty
   condition was like the explanation, except that participants were also shown a confidence
   prompt 'The AI is X % confident in its suggestion.'" Both sit in the simple-explainable-AI
   category, and Section 4.1 reports: "For all the metrics, there were no significant
   differences among conditions within either category (i.e., simple explainable AI and
   cognitive forcing functions)." Showing confidence changed nothing.

---

## 2.7

> Reliance behaves as a cost-benefit trade-off in which users accept the model's answer rather than pay the cognitive cost of verifying it, so a degraded output can pass uncaught \cite{vasconcelos2023explanations, schemmer2023reliance}.

### vasconcelos2023explanations — SUPPORTED

Source: https://arxiv.org/pdf/2212.06823 (PDF downloaded and read; v2, 26 Jan 2023).
Retrieved 2026-09-05. Published version: PACM HCI 7(CSCW1), Article 129, doi 10.1145/3579605.

Abstract, verbatim:

> "our paper argues that people strategically choose whether or not to engage with an AI
> explanation... To achieve this, we formalize this strategic choice in a cost-benefit
> framework, where the costs and benefits of engaging with the task are weighed against the
> costs and benefits of relying on the AI."

Section 3, verbatim, and this is the sentence's claim almost word for word:

> "In the context of human-AI decision making, this framework suggests that people compare the
> potential benefits of engaging with the task (i.e. professional accomplishment, monetary
> reward) weighed against its inherent costs (i.e. cognitive effort, time). People are likely
> to overrely if engaging with the task is not the optimal strategy. When people choose to
> engage with the task, they are adopting one of two strategies: either they do the task alone,
> ignoring any AI support, or they verify the AI's prediction, sometimes using AI generated
> explanations if they are present."

Empirically borne out across the five studies (N = 731): task difficulty, explanation
difficulty, and monetary compensation all moved overreliance in the directions the framework
predicts. The concluding sentence of the abstract states the verification-cost mechanism
directly: "some of the null effects found in literature could be due in part to the explanation
not sufficiently reducing the costs of verifying the AI's prediction."

### schemmer2023reliance — NOT SUPPORTED

Source: https://arxiv.org/html/2302.02187v2 (full HTML fetched and read). Retrieved 2026-09-05.
Published version: IUI '23.

This paper contains no cost-benefit account of reliance. A case-insensitive search of the full
text returns zero occurrences of "cost," "cognitive effort," "effortful," "heuristic,"
"dual-process," "verify," or "verification." Its theory is trust-and-confidence based, not
effort based. Section 4, verbatim, is the whole of its causal model:

> "In 1992, Lee and Moray (1992), already discussed the influence of self-confidence and trust
> as predominant attitudes for reliance decisions. Therefore, in the following, we discuss
> potential impacts on trust and the change in self-confidence induced through explanations and
> their impact on AoR."

Its hypotheses are H1a/H1b (explanations affect the two AoR dimensions), H2/H3 (change in
self-confidence), H4/H5 (trust). Its contribution and findings, Section 7, verbatim:

> "The main contribution of our work is the theoretical development of AR. So far, terms like
> ''appropriate trust'', ''calibrated trust'' and AR were often used interchangeably in prior
> research. We provide clarity by defining AR and putting the terms in perspective. Second, we
> derive a granular, two-dimensional measurement concept---Appropriateness of Reliance (AoR)."

> "On the other hand, our results show that explanations do not influence the RSR. While this
> may sound disappointing at first, it also shows that the claim that explanations would reduce
> overreliance (Bansal et al., 2021; Buçinca et al., 2021) does not seem to hold for all kinds
> of tasks."

The paper is a legitimate source for "explanations do not reliably improve people's rejection
of incorrect advice" (which is closer to sentence 2.6's territory) and for a measurement
vocabulary for reliance. It is not a source for reliance as a cost-benefit trade-off against
the cognitive cost of verification.

Where that claim does come from, if a second citation is wanted alongside Vasconcelos:
Buçinca et al. 2021 (already cited in the preceding sentence) grounds it in dual-process
theory, "we posit that people rarely engage analytically with each individual AI recommendation
and explanation, and instead develop general heuristics about whether and when to follow the AI
suggestions"; and Parasuraman and Manzey 2010 (already cited two sentences earlier) states the
same mechanism as the cognitive-miser hypothesis, "One is the tendency of humans to choose the
road of least cognitive effort in decision making, the so-called cognitive-miser hypothesis."

---

## 2.8

> \citet{madaan2024self} show that a model prompted to critique and rewrite its work can raise its quality, and locate the benefit in feedback that is \emph{actionable} and \emph{specific}, naming a concrete change to a concrete part of the output.

### madaan2024self — SUPPORTED

Source: https://arxiv.org/html/2303.17651v2 (full HTML fetched and read). Retrieved 2026-09-05.

The quality claim, abstract, verbatim:

> "Across all evaluated tasks, outputs generated with Self-Refine are preferred by humans and
> automatic metrics over those generated with the same LLM using conventional one-step
> generation, improving by ~20% absolute on average in task performance."

The definitions, Section 2, verbatim, and they match the citing sentence's gloss exactly:

> "We prompt the model to write feedback that is actionable and specific via fb(k). By
> 'actionable', we mean the feedback should contain a concrete action that would likely improve
> the output. By 'specific', we mean the feedback should identify concrete phrases in the output
> to change."

The paper does not merely define these; it isolates them experimentally, which is what
"locate the benefit in" requires. Section 5, verbatim:

> "To quantify its impact, we compare Self-Refine, which utilizes specific, actionable feedback,
> with two ablations: one using generic feedback and another without feedback... In Code
> Optimization, performance slightly dips from 27.5 (Self-Refine feedback) to 26.0 (generic
> feedback), and further to 24.8 (no feedback)... This effect is more pronounced in tasks like
> Sentiment Transfer, where changing from our feedback to generic feedback leads to a significant
> performance drop (43.2 to 31.2), and the task fails without feedback. Similarly, in Acronym
> Generation, without actionable feedback, performance drops from 56.4 to 48.0, even with
> iterative refinements. These results highlight the importance of specific, actionable feedback
> in our approach."

And the error analysis puts the failures on the feedback rather than the rewriting, which is the
seam the paragraph goes on to use:

> "Specifically, 33% of unsuccessful cases were due to feedback inaccurately pinpointing the
> error's location, while 61% were a result of feedback suggesting an inappropriate fix. Only 6%
> of failures were due to the refiner incorrectly implementing good feedback."

Not a claim problem, but a bibliographic one the author may want to settle: the key is
`madaan2024self` while the entry's `year` field is 2023, so `\citet` renders "Madaan et al.
(2023)". NeurIPS 36 is the 2023 conference, proceedings issued 2024.

---

## Summary table

| # | Sentence topic | Cited work | Classification |
|---|---|---|---|
| 2.1 | Deployment on open-ended workplace tasks vs benchmarks | anthropic2025economicindex | PARTIALLY SUPPORTED |
| 2.2 | Real prompts underspecified; degrades and destabilizes output | yang2025underspecification | PARTIALLY SUPPORTED |
| 2.3 | Non-experts cannot articulate intent or validate output | zhou2026oversight | SUPPORTED |
| 2.4 | Dependence compounds across turns; accuracy falls | laban2025lost | PARTIALLY SUPPORTED |
| 2.5 | Automation bias, decades of studies, experts and novices | parasuraman2010complacency | SUPPORTED |
| 2.5 | Automation bias, decades of studies, experts and novices | skitka1999automation | UNCHECKABLE |
| 2.6 | Explanations and confidence raise acceptance, not discrimination | bansal2021whole | PARTIALLY SUPPORTED |
| 2.6 | Explanations and confidence raise acceptance, not discrimination | bucinca2021trust | PARTIALLY SUPPORTED |
| 2.7 | Reliance as cost-benefit trade-off against verification cost | vasconcelos2023explanations | SUPPORTED |
| 2.7 | Reliance as cost-benefit trade-off against verification cost | schemmer2023reliance | NOT SUPPORTED |
| 2.8 | Self-refinement raises quality; benefit in actionable, specific feedback | madaan2024self | SUPPORTED |

Totals: 4 SUPPORTED, 5 PARTIALLY SUPPORTED, 1 NOT SUPPORTED, 1 UNCHECKABLE.
