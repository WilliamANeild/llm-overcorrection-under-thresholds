# Statistical notation in abstracts at human-subjects venues

Compiled 2026-09-06. Every abstract quoted here was fetched on that date from the
source named in its entry. Nothing in this file is quoted from memory or from a
secondary description.

The question is whether the near-absence of statistical notation observed in a
9-abstract sample of 2026 ACL-venue papers is an ACL convention or a general one,
and in particular whether venues where human subjects and inter-rater reliability
are central write abstracts differently.

## 1. Sources, access, and sampling

### 1.1 What was reachable and what was not

| Source | Endpoint | Result |
|---|---|---|
| ACM Digital Library | `dl.acm.org/doi/10.1145/3613904.3642697` | **403 Forbidden** |
| ACM Digital Library | `dl.acm.org/doi/abs/10.1145/3610186` | **403 Forbidden** |
| ACM Digital Library | `dl.acm.org/action/doSearch` | **403 Forbidden** |
| arXiv API | `export.arxiv.org/api/query` | 200, used |
| ACL Anthology | `aclanthology.org/volumes/2026.tacl-1/` | 200 |
| ACL Anthology XML | `raw.githubusercontent.com/acl-org/acl-anthology/master/data/xml/` | 200, used |
| PubMed E-utilities | `eutils.ncbi.nlm.nih.gov/entrez/eutils/` | 200, used |

The ACM Digital Library refused every request, on article pages and on the search
endpoint, both with a default client and with a desktop browser user-agent string.
No CHI or CSCW abstract in this file comes from the ACM version of record. All CHI
and CSCW text is the author's arXiv preprint abstract. Preprint and camera-ready
abstracts are usually the same text but are not guaranteed to be, and that is a
limit on every CHI and CSCW count below.

### 1.2 How each sample was drawn

**CHI and CSCW.** The arXiv API was queried for `cat:cs.HC` combined with
comment-field matches on "CHI 2026", "CHI 2025", "CSCW 2026", "CSCW 2025", and
"CSCW", sorted by submission date descending, 200 records per query. That returned
685 records, 576 unique after deduplication. Records were then filtered to remove
anything whose comment names a workshop, late-breaking work, poster, doctoral
consortium, demo, alt.chi, symposium, or position paper; to require acceptance or
proceedings language in the comment; and to require at least one of LLM, large
language model, GPT, ChatGPT, language model, generative AI, AI assistant,
conversational agent, or chatbot in the abstract. That left **112 abstracts, 65 CHI
and 47 CSCW**. The 22 abstracts quoted in the corpus table are a systematic draw
from that list sorted by venue then date descending: every fifth CHI record to a cap
of 12, every fourth CSCW record to a cap of 10. All counts reported by family use
the full 112, not the 22.

**TACL.** The complete ACL Anthology XML for volumes `2025.tacl` and `2026.tacl` was
parsed, giving **116 papers with abstracts** (82 from 2025, 34 from 2026). The 12
abstracts in the corpus table are every third paper of the 2026 volume. Counts use
the full 116.

**Psychology and behavioural science.** PubMed was searched for title-or-abstract
matches on "large language model", ChatGPT, LLM, LLMs, "generative AI", "AI chatbot",
or "conversational agent", restricted to fifteen named journals, published 2024
through 2026, with an abstract present. The query returned 842 hits; the **300 most
recent** were fetched in full. Journal composition of those 300: Journal of Medical
Internet Research 138, Frontiers in Psychology 107, PNAS 24, PNAS Nexus 11, Behavior
Research Methods 10, Nature Human Behaviour 4, British Journal of Psychology 3,
Cognition 2, Cognitive Science 1. The 14 abstracts in the corpus table are a
journal-stratified draw with per-journal quotas, excluding titles or abstract
openings matching review, meta-analysis, protocol, scoping, bibliometric,
commentary, editorial, viewpoint, or umbrella, and excluding abstracts under 80
words. Counts use the full 300 and are also broken out by journal.

**ACL comparison baseline.** The nine abstracts already held in
`paper/reference/acl2026_abstracts.json` were re-measured with the same numeral
counter used here, and reproduce the previously reported median of 1.9 numerals per
100 words exactly (median 1.92). The density comparison in section 5 is therefore
like-for-like.

### 1.3 Bounds on the sampling

Five limits are worth stating, because each one bounds a count below.

The arXiv route finds only CHI and CSCW papers whose authors post a preprint and
name the venue in the comment field. Authors who do not preprint are invisible to
it. Requiring an LLM or AI term in the abstract narrows further, to the
language-model slice of CHI and CSCW rather than those conferences as a whole. That
slice is the right comparison class for a human-AI interaction paper, but it is not
a random sample of CHI.

PubMed indexes psychology unevenly. Journal of Experimental Psychology: General,
Psychological Science, and Judgment and Decision Making returned nothing under this
query. The psychology family is consequently dominated by two open-access journals,
Frontiers in Psychology and the Journal of Medical Internet Research, and section 4
reports them separately for that reason.

The ACL baseline is nine abstracts. It sets the comparison point the question asked
for, and it is small.

### 1.4 How counting was done

Counting is mechanical. A regular-expression detector was applied uniformly to every
abstract in every pool, matching thirteen core categories: Cohen's kappa; Cronbach's
or Krippendorff's alpha, ICC, and inter-rater or inter-annotator or inter-coder
agreement; chi-squared; Spearman's rho; Cohen's d and the phrase "effect size";
Pearson's r and correlation coefficients; eta-squared; F and ANOVA; t, Wilcoxon,
Mann-Whitney and Kruskal-Wallis; p-values and the phrase "statistically
significant"; confidence intervals; odds ratios and regression coefficients written
as beta; and means with standard deviations. Three further categories were tracked
but held outside the "core statistic" count: the word "significant" used without
notation, regression and mediation vocabulary used without a coefficient, and
sample-size notation of the form N= or n=.

Each pattern requires either a named statistic or a numeral attached to a symbol, so
that a bare letter in ordinary prose does not match. The detector was checked against
raw substring searches over the same pools; the loose searches produced obvious
false positives ("social" matching CI, "machine" matching chi, "meta" matching eta)
that the detector correctly excludes. Every sentence the detector flagged was read
and is quoted in section 3, so the reader can check the classification rather than
trust it.

Numeral density is the count of digit runs (a run being a maximal sequence of digits
with embedded commas or decimal points, so that "95%" and "0.011" and "1,250" each
count once) divided by whitespace-delimited words, times 100.
## 2. Corpus table (48 abstracts, the verbatim-quoted sample)

All retrieved 2026-09-06. "Core stat" lists notation categories the detector matched;
"N=" marks an explicit sample-size figure; density is numerals per 100 words.


### 2.1 HCI: CHI and CSCW (arXiv author preprints)

| # | Venue | ID | Title (truncated) | Words | Num. | Dens. | N= | Core stat |
|---|---|---|---|---|---|---|---|---|
| 1 | CHI (arXiv preprint) | 2606.09840v1 | Envisioning Sensemaking in Multi-Human, Multi-Agent Collaborat | 191 | 0 | 0.0 | - | none |
| 2 | CHI (arXiv preprint) | 2604.03542v1 | Amplifying Rural Educators' Perspectives: A Qualitative Study  | 150 | 1 | 0.67 | - | none |
| 3 | CHI (arXiv preprint) | 2603.13116v1 | Memory Printer: Exploring Everyday Reminiscing by Combining Sl | 172 | 1 | 0.58 | - | none |
| 4 | CHI (arXiv preprint) | 2603.07956v1 | From Daily Song to Daily Self: Supporting Reflective Songwriti | 154 | 0 | 0.0 | - | none |
| 5 | CHI (arXiv preprint) | 2602.20876v1 | When LLMs Enter Everyday Feminism on Chinese Social Media: Opp | 147 | 3 | 2.04 | - | none |
| 6 | CHI (arXiv preprint) | 2602.14407v1 | "I Felt Bad After We Ignored Her": Understanding How Interface | 177 | 1 | 0.56 | - | none |
| 7 | CHI (arXiv preprint) | 2602.11567v1 | Behavioral Indicators of Overreliance During Interaction with  | 146 | 1 | 0.68 | - | none |
| 8 | CHI (arXiv preprint) | 2504.15549v1 | Do It For Me vs. Do It With Me: Investigating User Perceptions | 145 | 2 | 1.38 | yes | none |
| 9 | CHI (arXiv preprint) | 2503.05899v1 | Towards Understanding the Use of MLLM-Enabled Applications for | 169 | 8 | 4.73 | - | none |
| 10 | CHI (arXiv preprint) | 2502.17348v1 | How Scientists Use Large Language Models to Program | 116 | 0 | 0.0 | - | none |
| 11 | CHI (arXiv preprint) | 2502.11267v1 | Prompting in the Dark: Assessing Human Performance in Prompt E | 162 | 2 | 1.23 | - | none |
| 12 | CHI (arXiv preprint) | 2502.01390v1 | Plan-Then-Execute: An Empirical Study of User Trust and Team P | 266 | 3 | 1.13 | yes | none |
| 13 | CSCW (arXiv preprint) | 2606.31762v1 | Investigating LLM-Powered Dissenting Minority Support in Power | 149 | 2 | 1.34 | - | none |
| 14 | CSCW (arXiv preprint) | 2604.14266v1 | "I Just Don't Want My Work Being Fed Into The AI Blender": Que | 135 | 1 | 0.74 | - | none |
| 15 | CSCW (arXiv preprint) | 2601.02775v2 | Expecting Too Much, Getting Too Little: Exploring the Challeng | 217 | 4 | 1.84 | yes | none |
| 16 | CSCW (arXiv preprint) | 2508.11030v3 | Families' Vision of Generative AI Agents for Household Safety  | 190 | 1 | 0.53 | - | none |
| 17 | CSCW (arXiv preprint) | 2508.03355v1 | Remini: Leveraging Chatbot-Mediated Mutual Reminiscence for Pr | 180 | 2 | 1.11 | yes | none |
| 18 | CSCW (arXiv preprint) | 2505.00821v3 | Should AI Mimic People? Understanding AI-Supported Writing Tec | 176 | 1 | 0.57 | - | none |
| 19 | CSCW (arXiv preprint) | 2502.09577v2 | Polymind: Parallel Visual Diagramming with Large Language Mode | 153 | 0 | 0.0 | - | none |
| 20 | CSCW (arXiv preprint) | 2412.08185v3 | Exploring Multidimensional Checkworthiness: Designing AI-assis | 176 | 1 | 0.57 | - | none |
| 21 | CSCW (arXiv preprint) | 2408.02574v4 | DanModCap: Designing a Danmaku Moderation Tool for Video-Shari | 195 | 0 | 0.0 | - | none |
| 22 | CSCW (arXiv preprint) | 2406.19528v3 | Harnessing LLMs for Automated Video Content Analysis: An Explo | 180 | 2 | 1.11 | - | none |

### 2.2 TACL 2026 (ACL Anthology)

| # | Venue | ID | Title (truncated) | Words | Num. | Dens. | N= | Core stat |
|---|---|---|---|---|---|---|---|---|
| 1 | TACL 2026 | 2026.tacl-1.1 | ActiveLLM: Large Language Model-Based Active Learning for Text | 156 | 3 | 1.92 | - | none |
| 2 | TACL 2026 | 2026.tacl-1.4 | CorefInst: Leveraging LLMs for Multilingual Coreference Resolu | 139 | 7 | 5.04 | - | none |
| 3 | TACL 2026 | 2026.tacl-1.7 | What Can String Probability Tell Us About Grammaticality? | 150 | 4 | 2.67 | - | none |
| 4 | TACL 2026 | 2026.tacl-1.10 | MultiBLiMP 1.0: A Massively Multilingual Benchmark of Linguist | 70 | 6 | 8.57 | - | none |
| 5 | TACL 2026 | 2026.tacl-1.13 | Accelerating Language Model Workflows with Prompt Choreography | 103 | 3 | 2.91 | - | none |
| 6 | TACL 2026 | 2026.tacl-1.16 | IssueBench: Millions of Realistic Prompts for Measuring Issue  | 208 | 4 | 1.92 | - | none |
| 7 | TACL 2026 | 2026.tacl-1.19 | MERLIN: A Testbed for Multilingual Multimodal Entity Recogniti | 113 | 5 | 4.42 | - | none |
| 8 | TACL 2026 | 2026.tacl-1.22 | Automatic Reviewers Fail to Detect Faulty Reasoning in Researc | 139 | 1 | 0.72 | - | none |
| 9 | TACL 2026 | 2026.tacl-1.25 | Ev2R: Evaluating Evidence Retrieval in Automated Fact-Checking | 149 | 5 | 3.36 | - | none |
| 10 | TACL 2026 | 2026.tacl-1.28 | Can Large Language Models Generalize Analogy Solving Like Chil | 140 | 0 | 0.0 | - | none |
| 11 | TACL 2026 | 2026.tacl-1.31 | Beyond One-Size-Fits-All: Inversion Learning for Highly Effect | 123 | 0 | 0.0 | - | none |
| 12 | TACL 2026 | 2026.tacl-1.34 | A Systematic Assessment of Language Models with Linguistic Min | 135 | 2 | 1.48 | - | none |

### 2.3 Psychology and behavioural science (PubMed)

| # | Venue | ID | Title (truncated) | Words | Num. | Dens. | N= | Core stat |
|---|---|---|---|---|---|---|---|---|
| 1 | Proc Natl Acad Sci U S A | PMID 42691082 | Leveraging generative AI for causal inference with unstructure | 151 | 3 | 1.99 | - | none |
| 2 | J Med Internet Res | PMID 42696728 | Evaluating a Guideline-Integrated Clinical Interaction Framewo | 450 | 43 | 9.56 | - | p_value |
| 3 | J Med Internet Res | PMID 42696525 | Large Language Models for Heterogeneous Data Mining in Liver D | 445 | 29 | 6.52 | - | none |
| 4 | Nat Hum Behav | PMID 42693267 | Mourning the loss of AI companions. | 157 | 18 | 11.46 | - | cohens_d, CI |
| 5 | Proc Natl Acad Sci U S A | PMID 42647129 | Sensory context improves language prediction in humans and LLM | 244 | 0 | 0.0 | - | none |
| 6 | PNAS Nexus | PMID 42614865 | Like humans, language models demonstrate face-to-character bia | 210 | 17 | 8.1 | - | none |
| 7 | Front Psychol | PMID 42676375 | Source matters, AI anxiety less so: comparing employee reactio | 220 | 1 | 0.45 | yes | none |
| 8 | Front Psychol | PMID 42666257 | Dual pathways of generative AI use: role ambiguity and self-ef | 243 | 1 | 0.41 | - | none |
| 9 | PNAS Nexus | PMID 42583036 | Fragile preferences: A deep dive into order effects in large l | 213 | 0 | 0.0 | - | none |
| 10 | Behav Res Methods | PMID 42552500 | Simulating insufficient effort responding with large language  | 248 | 7 | 2.82 | yes | none |
| 11 | Br J Psychol | PMID 41578606 | Neurodivergence and well-being: The fulfilment of fundamental  | 192 | 4 | 2.08 | - | none |
| 12 | Behav Res Methods | PMID 42509529 | Adding LLMs to the psycholinguistic norming toolbox: A practic | 247 | 2 | 0.81 | - | rho, r_corr |
| 13 | Cognition | PMID 41795476 | People defer to AI moral advice, but not blindly. | 248 | 3 | 1.21 | - | none |
| 14 | Cogn Sci | PMID 42329828 | Large Language Models Estimate Fine-Grained Human Color-Concep | 211 | 4 | 1.9 | - | none |
## 3. Verbatim catalogue

Every sentence below is quoted exactly as it appears in the retrieved abstract.
Unicode (κ, β, χ2, η, ≤, ρ) is reproduced as retrieved. Where PubMed supplies a
structured-abstract label (RESULTS:, METHODS:) the label is part of the retrieved
text and is kept. Retrieval date for every item: 2026-09-06.


### 3.1 CHI and CSCW: complete census of statistical notation in the 112-abstract pool

Three abstracts out of 112 carry any core statistic. All three are CHI; all three
carry a p-value and nothing else. Complete, not a sample.

**CHI — arXiv 2603.06926v1** — MindfulAgents: Personalizing Mindfulness Meditation via an Expert-Aligned Multi-Agent System  
<https://arxiv.org/abs/2603.06926v1> — comment: "Accepted by CHI 2026; Zhihan Jiang and Yuang Fan contributed equally as second authors"

> In a formative lab study (N=13), MindfulAgents significantly improved in-session engagement (p = 0.011) and self-awareness (p = 0.014), and reduced momentary stress (p = 0.020).

> Furthermore, a four-week deployment study (N=62) demonstrated a notable increase in long-term engagement (p = 0.002) and level of mindfulness (p = 0.023).

**CHI — arXiv 2602.18962v2** — NeuroWise: A Multi-Agent LLM "Glass-Box" System for Practicing Double-Empathy Communication with Autistic Partners  
<https://arxiv.org/abs/2602.18962v2> — comment: "Accepted to ACM CHI 2026"

> In a between-subjects study (N=30), NeuroWise was rated as helpful by all participants and showed a significant condition-time effect on deficit-based attributions (p=0.02): NeuroWise users reduced deficit framing, while baseline users shifted toward blaming autistic "deficits" after difficult interactions.

> NeuroWise users also completed conversations more efficiently (37% fewer turns, p=0.03).

**CHI — arXiv 2602.12432v1** — KeySense: LLM-Powered Hands-Down, Ten-Finger Typing on Commodity Touchscreens  
<https://arxiv.org/abs/2602.12432v1> — comment: "16 pages, 11 figures. Accepted to appear in the Proceedings of the ACM CHI Conference on Human Factors in Computing Systems (CHI 2026). This version corresponds to the accepted manuscript"

> A 12-participant study shows clear ergonomic and performance benefits: compared with the conventional hover-style keyboard, users rated KeySense as markedly less physically demanding (NASA-TLX median 1.5 vs 4.0), and after brief practice typed significantly faster (WPM 28.3 vs 26.2, p < 0.01).


### 3.2 CHI and CSCW: complete census of sample-size notation in the 112-abstract pool

Twenty abstracts of 112 (18 percent) state a sample size in the form N= or n=.
This is the only quantitative notation that appears with any regularity in this family.

> [CSCW, arXiv 2604.27905v2] In this paper, we first derive user requirements for a comment-based CNR tool from literature and a formative study (N=12).

> [CSCW, arXiv 2601.18966v1] We evaluate this theory through a pre-registered experiment (N=1250) where users predict behavior of 25 social media feed ranking algorithms that vary on these criteria.

> [CSCW, arXiv 2601.02775v2] In the follow-up study, we designed an interface with two features, response variants and feedback variants, and evaluated it across six groups (N = 180, 30 participants each) to assess whether these features support users' sense of agency, competence, and relatedness.

> [CSCW, arXiv 2508.03355v1] In a mixed-method, both between- and within- subjects study (N = 48, 24 dyads), we compare Remini to a baseline chatbot that offers minimal memory-trigger prompts.

> [CSCW, arXiv 2505.01000v5] With the initial prototype, we conducted a formative study (N=10) and identified the potential benefits and risks of such an adaptive scheduling tool.

> [CSCW, arXiv 2505.01000v5] Then, after enhancing the system, we conducted two controlled experiments, one each for attendees and organizers (total N=66).

> [CSCW, arXiv 2310.13712v3] We conducted a formative study in an undergraduate computer science classroom (N=145) and a controlled experiment on Prolific (N=356) to explore the impact of four pedagogically informed guidance strategies on the learners' performance, confidence and trust in LLMs.

> [CHI, arXiv 2604.10883v1] Through log data (N=30) and interviews (N=10), we examine how entrepreneurs build resilience through collective AI literacy development-encompassing adoption, adaptation, and refusal of AI.

> [CHI, arXiv 2604.06008v1] Workshops (N=30) revealed key design requirements -- support for Roman Urdu, use of subsidized platforms, and an expert -- curated knowledge base.

> [CHI, arXiv 2603.16614v1] CoEmpaTeam deploys three avatars who significantly differ in their personality, validated by a technical evaluation and an online experiment (n=90).

> [CHI, arXiv 2603.06926v1] In a formative lab study (N=13), MindfulAgents significantly improved in-session engagement (p = 0.011) and self-awareness (p = 0.014), and reduced momentary stress (p = 0.020).

> [CHI, arXiv 2603.06926v1] Furthermore, a four-week deployment study (N=62) demonstrated a notable increase in long-term engagement (p = 0.002) and level of mindfulness (p = 0.023).

> [CHI, arXiv 2603.03727v2] We presented these to parents (N=24) and asked whether they found them concerning, why, and how they would prefer the responses to be modified and communicated.

> [CHI, arXiv 2602.18962v2] In a between-subjects study (N=30), NeuroWise was rated as helpful by all participants and showed a significant condition-time effect on deficit-based attributions (p=0.02): NeuroWise users reduced deficit framing, while baseline users shifted toward blaming autistic "deficits" after difficult interactions.

> [CHI, arXiv 2602.15569v2] We investigate feedback timing and verbosity from agentic LLM-based in-car assistants through a controlled, mixed-methods study (N=45) comparing planned steps and intermediate results feedback against silent operation with final-only response.

> [CHI, arXiv 2504.15549v1] In a user study (N=20) across data analysis and visual design tasks, GuidedCopilot outperformed AutoCopilot in user control, software utility, and learnability, especially for exploratory and creative tasks, while AutoCopilot saved time for simpler visual tasks.

> [CHI, arXiv 2504.15549v1] A follow-up design exploration (N=10) enhanced GuidedCopilot with task-and state-aware features, including in-context preview clips and adaptive instructions.

> [CHI, arXiv 2504.12943v2] Using a Research through Design approach, we conducted a week-long field study followed by interviews and design activities (N = 22), which uncovered how participants created diverse chatbot personas for emotional reliance, confronting stressors, connecting to intellectual discourse, reflecting mirrored selves, etc.

> [CHI, arXiv 2502.18681v1] We validated the effectiveness of \textsc{COALA} through user studies with domain experts (N=2+2) and researchers with relevant experience (N=8).

> [CHI, arXiv 2502.18641v1] Through a user study (N=12) and technical evaluations, we found that WhatELSE enables authors to perceive and edit the narrative space and generates engaging interactive narratives at play-time.

> [CHI, arXiv 2502.16062v1] A user study (N=24) demonstrated that our approach reduces participants' cognitive load, fosters creativity, and enhances the metaphorical richness of visual blend ideation.

> [CHI, arXiv 2502.07628v2] To address these issues, we conducted a formative study (N=7) to identify the workflow and design space, including four core factors (Function, Subject Matter, Style, and Method of Expression) and a key element (Pattern).

> [CHI, arXiv 2502.07628v2] A user study (N=16) and an expert evaluation (N=3) demonstrated that HarmonyCut effectively provided relevant knowledge, aiding the ideation of diverse paper-cutting designs and maintaining design quality within the design space to ensure alignment between form and cultural connotation.

> [CHI, arXiv 2502.01390v1] We conducted an empirical study (N = 248) of LLM agents as daily assistants in six commonly occurring tasks with different levels of risk typically associated with them (e.g., flight ticket booking and credit card payments).


### 3.3 TACL: complete census of statistical notation in the 116-abstract pool

Two abstracts of 116. One is a sampling hyperparameter, not a test statistic;
the other states annotator agreement in words with no coefficient. Complete, not a sample.

**TACL 2025 — 2025.tacl-1.35** — REAL Sampling: Boosting Factuality and Diversity of Open-ended Generation by Extrapolating the Entropy of an Infinitely Large LM  
<https://aclanthology.org/2025.tacl-1.35/>

> After combined with contrastive decoding, REAL sampling outperforms 13 sampling methods, and generates texts that are more factual than the greedy sampling and more diverse than the nucleus sampling with p = 0.5.

**TACL 2026 — 2026.tacl-1.6** — Localizing Factual Inconsistencies in Attributable Text Generation  
<https://aclanthology.org/2026.tacl-1.6/>

> We first demonstrate the effectiveness of the QASemConsistency methodology for human annotation, by collecting crowdsourced annotations of granular consistency errors, while achieving a substantial inter-annotator agreement.


### 3.4 Psychology and health: complete census of inter-rater reliability sentences (300-abstract PubMed pool)

Fifty-six sentences across the pool. Every one is from a structured-abstract journal.

**J Med Internet Res 2026 — PMID 42686197 — doi:10.2196/95780**  
<https://pubmed.ncbi.nlm.nih.gov/42686197/>

> Extraction performance was assessed using exact-match accuracy, weighted F1-scores, Cohen κ statistics, and tolerance-based agreement thresholds for tumor size.

> Weighted F1-scores ranged from 0.87 for histology to 0.995 for sex, while Cohen κ values ranged from 0.85 for N stage to 0.99 for sex.

**J Med Internet Res 2026 — PMID 42647856 — doi:10.2196/96002**  
<https://pubmed.ncbi.nlm.nih.gov/42647856/>

> RIGHT assessments showed consistent reliability (ICC=0.80-0.88).

> Without additional guidance, agent-human agreement was moderate (ICC=0.608-0.629).

> In validation beyond rehabilitation, DeepSeek-R1 maintained stable agreement (ICC=0.711) and completed appraisals in 5.44 minutes compared to 11.18 minutes for humans.

**J Med Internet Res 2026 — PMID 42647045 — doi:10.2196/86251**  
<https://pubmed.ncbi.nlm.nih.gov/42647045/>

> The PP-LLM demonstrated almost perfect agreement with the reference standard (Gwet κ=0.959, 95% CI 0.937-0.981), comparable to two human readers (reader 1: κ=0.943; reader 2: κ=0.934), with no statistically significant difference in C-RADS classification accuracy.

**J Med Internet Res 2026 — PMID 42627683 — doi:10.2196/92407**  
<https://pubmed.ncbi.nlm.nih.gov/42627683/>

> Model performance was evaluated against expert assessment using accuracy, F1-scores, and Cohen κ.

> To assess interrater reliability and establish a human benchmark, a stratified 10% (n=65) subset was independently annotated by a second clinician, and Cohen κ was calculated between annotators and between each model and the primary expert.

> RESULTS: Interrater agreement between the 2 clinical annotators yielded a Cohen κ of 0.75, providing a human benchmark for model performance interpretation.

> For binary classification, accuracies ranged from 0.93 to 0.94, with weighted F1-scores of 0.93-0.95 and Cohen κ of 0.76-0.79, approaching the human interrater benchmark.

> CONCLUSIONS: LLMs demonstrated promising accuracy in classifying postoperative complications from discharge letters in a zero-shot setting, with performance approaching the upper bound of human interrater agreement.

**Front Psychol 2026 — PMID 42661697 — doi:10.3389/fpsyg.2026.1887565**  
<https://pubmed.ncbi.nlm.nih.gov/42661697/>

> RESULTS: The instructors rated the materials favorably for academic fidelity (M = 4.24), proficiency appropriateness (M = 4.36), and teachability (M = 4.31), with acceptable inter-rater reliability, ICC(2, k) = 0.84.

**J Med Internet Res 2026 — PMID 42594845 — doi:10.2196/98374**  
<https://pubmed.ncbi.nlm.nih.gov/42594845/>

> The human baseline was validated through double-coding by 2 independent researchers, achieving an acceptable intercoder reliability (α=0.703).

> In deductive application, however, both models systematically overcoded compared to the human consensus (181 and 183 codes vs 138), resulting in low intercoder reliability against the human baseline (α=0.487) for GPT-5 and (α=0.507) for Gemini.

**J Med Internet Res 2026 — PMID 42580688 — doi:10.2196/98026**  
<https://pubmed.ncbi.nlm.nih.gov/42580688/>

> The gold standard was the consensus diagnosis by 3 senior intensivists (>10 years' EICU experience; Fleiss κ=0.82).

**J Med Internet Res 2026 — PMID 42579604 — doi:10.2196/92374**  
<https://pubmed.ncbi.nlm.nih.gov/42579604/>

> Interrater agreement was quantified with Gwet AC1.

> Interrater agreement was moderate (Gwet AC1=0.58, 95% CI 0.42-0.75; P<.001).

**J Med Internet Res 2026 — PMID 42546264 — doi:10.2196/90046**  
<https://pubmed.ncbi.nlm.nih.gov/42546264/>

> Human evaluation was reported in 94/157 (59.9%) studies, but interrater reliability was reported in 26/94 (27.7%) studies.

**J Med Internet Res 2026 — PMID 42525870 — doi:10.2196/93393**  
<https://pubmed.ncbi.nlm.nih.gov/42525870/>

> Reference authenticity was independently verified by 2 reviewers (XH and WH) using a 5-category scheme (V/PV/F/G/NR [V: Verifiable, PV: Partially Verifiable, F: Fabricated, G: Guideline-Based, Nonspecific, and NR: No References]), with consensus after canonical-source reverification (Cohen κ=0.702 preadjudication).

**J Med Internet Res 2026 — PMID 42520216 — doi:10.2196/93890**  
<https://pubmed.ncbi.nlm.nih.gov/42520216/>

> Diagnostic performance was assessed by receiver operating characteristic analysis with DeLong testing; agreement was quantified using squared weighted κ and Cohen κ; and stability was measured using Krippendorff α and Fleiss κ.

> For C-TIRADS classification, DeepSeek-R1 showed substantial agreement with radiologists, exceeding ChatGPT-4o (κ=0.770 vs 0.688; Δκ=0.082, 95% CI 0.048-0.122).

> Both models yielded moderate, comparable agreement with clinicians on management recommendations (κ=0.606 vs 0.608).

> Stability was near perfect for C-TIRADS classification (α=0.864 vs 0.866) and management recommendations (κ=0.853 vs.

> 0.849) in both models; however, DeepSeek-R1 showed markedly greater stability than ChatGPT-4o in benign-malignant differentiation (κ=0.869 vs 0.609; Δκ=0.260, 95% CI 0.191-0.321).

**J Med Internet Res 2026 — PMID 42497411 — doi:10.2196/92931**  
<https://pubmed.ncbi.nlm.nih.gov/42497411/>

> The questionnaire showed high internal consistency (Cronbach α=0.902) and generally positive attitudes, with no significant differences between physician groups (P=.11 to P=.78).

**J Med Internet Res 2026 — PMID 42497362 — doi:10.2196/97802**  
<https://pubmed.ncbi.nlm.nih.gov/42497362/>

> Interrater reliability was assessed using the quadratic weighted Cohen κ, intraclass correlation coefficient, and Spearman rank correlation coefficient.

> RESULTS: Interrater reliability analyses indicated moderate agreement between evaluators.

> Because the correctness, clarity, and conciseness rubric showed only moderate interrater reliability, the case-based comparisons should be interpreted as preliminary signals rather than definitive evidence of between-model differences.

**J Med Internet Res 2026 — PMID 42461978 — doi:10.2196/90364**  
<https://pubmed.ncbi.nlm.nih.gov/42461978/>

> Interrater reliability was assessed using the intraclass correlation coefficient.

**J Med Internet Res 2026 — PMID 42430720 — doi:10.2196/85840**  
<https://pubmed.ncbi.nlm.nih.gov/42430720/>

> GPT-4o was benchmarked against human reviewers using sensitivity, specificity, and weighted Cohen κ.

> Although there was substantial agreement with humans in the quality assessment (Cohen κ=0.778, 95% CI 0.710-0.846), the model exhibited optimism and positional biases due to reliance on probabilistic language patterns rather than structured clinical reasoning.

**J Med Internet Res 2026 — PMID 42430199 — doi:10.2196/85290**  
<https://pubmed.ncbi.nlm.nih.gov/42430199/>

> For topic classification, interannotator and human-LLM agreement were evaluated on a manually labeled subset to benchmark models of varying sizes.

> RESULTS: When metrics were arithmetically averaged across all annotation tasks, the best-performing LLM achieved agreement levels comparable to human annotation (accuracy=79.18%, SD 0.20%; κ=0.736, SD 0.003; F1-score=0.727, SD 0.006), approaching interannotator agreement (accuracy=81.65%; κ=0.767; F1-score=0.758), demonstrating strong stability and scalability.

**Front Psychol 2026 — PMID 42488041 — doi:10.3389/fpsyg.2026.1833118**  
<https://pubmed.ncbi.nlm.nih.gov/42488041/>

> RESULTS AND DISCUSSION: The proposed hybrid approach achieved an overall diagnostic agreement of 83.3% with manual clinical scoring, a Cohen's κ of 0.74 (substantial agreement), and demonstrated complete output stability across five independent runs.

> After excluding two technically compromised audio recordings, adjusted accuracy reached 90.9% with κ = 0.86.

**J Med Internet Res 2026 — PMID 42418253 — doi:10.2196/93237**  
<https://pubmed.ncbi.nlm.nih.gov/42418253/>

> Domain experts conducted a pilot evaluation to align interpretation criteria prior to independently assessing the final dataset, yielding an interexpert agreement (Fleiss κ) of 0.762 across 337 drug-level assessments.

> Agreement with expert assessments was quantified using Cohen κ, weighted κ, and accuracy metrics.

> Internal consistency across repeated inferences was evaluated using Fleiss κ.

> Cohen κ ranged from 0.368 to 0.641, weighted κ ranged from 0.641 to 0.821, accuracy ranged from 0.583 to 0.804, and balanced accuracy ranged from 0.513 to 0.735.

> Fleiss κ ranged from 0.730 to 0.915, corresponding to substantial to almost perfect agreement.

> The highest Cohen κ was observed for Gemini 2.5 Flash with CoT prompting (0.641).

> Gemini 2.5 Flash with CoT-self-consistency prompting showed a Cohen κ of 0.640 and achieved the highest observed point estimates for weighted κ (0.821), accuracy (0.804), and Fleiss κ (0.915), although the gains over other prompting strategies were modest.

**J Med Internet Res 2026 — PMID 42348906 — doi:10.2196/88834**  
<https://pubmed.ncbi.nlm.nih.gov/42348906/>

> Raw agreement between raters was 62% (153/248), and the mean of the pairwise weighted κ coefficients was 0.19 (SD 0.30; slight agreement).

> Interrater agreement was slight, which may suggest inadequate training of raters, unclear definitions, or a limitation of using the PDQI for this task.

**J Med Internet Res 2026 — PMID 42302307 — doi:10.2196/92852**  
<https://pubmed.ncbi.nlm.nih.gov/42302307/>

> Statistical analyses included Spearman ρ, Cronbach α, intraclass correlation coefficients, Friedman tests with Dunn multiple comparisons, and paired Wilcoxon signed-rank tests.

**J Med Internet Res 2026 — PMID 42247415 — doi:10.2196/87802**  
<https://pubmed.ncbi.nlm.nih.gov/42247415/>

> Interrater reliability was assessed using intraclass correlation coefficients (ICCs), and performance differences were assessed based on 4-rater consensus scores and Friedman and Wilcoxon tests.

> RESULTS: DeepSeek R1 demonstrated excellent interrater reliability across most quality dimensions (ICC ≥0.75).

**J Med Internet Res 2026 — PMID 42237583 — doi:10.2196/86692**  
<https://pubmed.ncbi.nlm.nih.gov/42237583/>

> Agreement with expert interpretation was low, with Cohen κ indicating poor-to-fair concordance (κ≤0.39).

**J Med Internet Res 2026 — PMID 42190235 — doi:10.2196/84444**  
<https://pubmed.ncbi.nlm.nih.gov/42190235/>

> Interrater variability in assigning scores ranged from 4.2% (n=3) to 85.8% (n=6) among primary health care professionals.

**J Med Internet Res 2026 — PMID 42077206 — doi:10.2196/94855**  
<https://pubmed.ncbi.nlm.nih.gov/42077206/>

> The construction phases were (1) exploratory corpus characterization, (2) iterative development of a 35-aspect hierarchical health outcome ontology, and (3) precision-optimized rule-based classification, validated through precision validation (stratified sample of n=500), recall estimation (n=510), external validation on 5 held-out channels (n=12,653 comments), large language model-assisted interrater reliability assessment, and transformer baseline comparison against Bidirectional Encoder Representations from Transformers (BERT) and Robustly Optimized BERT Pretraining Approach (ROBERTa) classifiers.

**J Med Internet Res 2026 — PMID 42066286 — doi:10.2196/88766**  
<https://pubmed.ncbi.nlm.nih.gov/42066286/>

> Interreviewer agreement was assessed using Cohen kappa coefficient.

**J Med Internet Res 2026 — PMID 42054561 — doi:10.2196/89850**  
<https://pubmed.ncbi.nlm.nih.gov/42054561/>

> A gold standard dataset of 100 intensive care unit nursing records was annotated by 3 senior nurses and finalized via consensus, with interrater reliability quantified using the Fleiss κ.

> RESULTS: Interrater agreement was substantial, with Fleiss κ=0.6449 for diagnoses and κ=0.6180 for interventions.

**J Med Internet Res 2026 — PMID 41950508 — doi:10.2196/87057**  
<https://pubmed.ncbi.nlm.nih.gov/41950508/>

> As this first round of validation surpassed our a priori threshold of ≥80% agreement and a Cohen κ of ≥0.61 between evaluators, no further rounds of development and validation were undertaken.

> Pilot validation showed a percent agreement of 86.1% and a Cohen κ of 0.70 between assessors.

**J Med Internet Res 2026 — PMID 41945643 — doi:10.2196/82579**  
<https://pubmed.ncbi.nlm.nih.gov/41945643/>

> Interrater reliability was quantified with Gwet AC1.


### 3.5 Behavioural-science journals: complete census of statistical notation

PNAS, PNAS Nexus, Nature Human Behaviour, Behavior Research Methods, Cognition,
Cognitive Science, British Journal of Psychology. Nine abstracts of 55 carry a core statistic.

**Nat Hum Behav 2026 — PMID 42693267 — doi:10.1038/s41562-026-02569-3**  
<https://pubmed.ncbi.nlm.nih.gov/42693267/>

> Both updates increased negativity, loss framing and restoration desires (Replika negative posts, +24.7 percentage points, 95% CI 20.1 to 29.2; ChatGPT, +13.0 percentage points, 95% CI 10.8 to 15.2), with larger Replika (versus ChatGPT) increases in sadness (d = 2.67 versus 1.41) and negative mental health (d = 1.72 versus 0.63).

> Replika users reported closeness exceeding common human ties (versus friend d = 0.47) and anticipated mourning higher than other technologies (d = 0.32-0.57).

**Nat Hum Behav 2026 — PMID 42637914 — doi:10.1038/s41562-026-02553-x**  
<https://pubmed.ncbi.nlm.nih.gov/42637914/>

> To examine the effects of such language, we conducted a human-subjects experiment (N = 1, 105), finding that readers frequently indicate abstracts with this phrasing provide causal evidence but that methodological labels (β = -0.4, 95% confidence interval -0.56 to -0.19) and associational wording (β = -0.3, 95% confidence interval -0.43 to -0.07) reduce this tendency.

**Nat Hum Behav 2026 — PMID 42637911 — doi:10.1038/s41562-026-02550-0**  
<https://pubmed.ncbi.nlm.nih.gov/42637911/>

> While core content is retained when LLMs polish and rewrite texts, LLMs also homogenize writing styles, reducing writing-complexity variance by a statistically significant 21-50% across datasets and models (P ≤ 0.05), and amplify patterns associated with dominant characteristics while suppressing others, emphasizing conformity over individuality.

**Nat Hum Behav 2026 — PMID 42552393 — doi:10.1038/s41562-026-02516-2**  
<https://pubmed.ncbi.nlm.nih.gov/42552393/>

> Smaller social networks were associated with reporting companionship as the primary chatbot use (β = -0.03; 95% confidence interval (CI), (-0.05, -0.01)), which in turn was associated with lower well-being (β = -0.48; 95% CI, (-0.70, -0.25)).

> For self-reported companionship usage, this association was stronger when interactions were intensive (β = -0.31; 95% CI, (-0.56, -0.06)) and highly disclosive (β = -0.38; 95% CI, (-0.63, -0.14)).

**Behav Res Methods 2026 — PMID 42509529 — doi:10.3758/s13428-026-03129-3**  
<https://pubmed.ncbi.nlm.nih.gov/42509529/>

> Using base models, we achieved a Spearman correlation of 0.8 with human ratings, which increased to 0.9 when employing fine-tuned models.

**Proc Natl Acad Sci U S A 2026 — PMID 42446982 — doi:10.1073/pnas.2606495123**  
<https://pubmed.ncbi.nlm.nih.gov/42446982/>

> Across three datasets, AI analyst-produced analyses exhibit substantial dispersion in effect sizes, [Formula: see text]-values, and conclusions.

**Behav Res Methods 2026 — PMID 42209884 — doi:10.3758/s13428-026-03058-1**  
<https://pubmed.ncbi.nlm.nih.gov/42209884/>

> These methods, tested in divergent thinking response scoring, each show statistically significant positive results, with improvements in correlation with human judges (from r = 0.781 to r = 0.823) and reduction in error.

**Behav Res Methods 2026 — PMID 42171863 — doi:10.3758/s13428-026-03052-7**  
<https://pubmed.ncbi.nlm.nih.gov/42171863/>

> Across the meta-research literature, these tasks usually range from extracting verbatim information (e.g., the number of participants in a study, effect sizes, or whether a study is preregistered) to making subjective inferences.

**Br J Psychol 2026 — PMID 39037067 — doi:10.1111/bjop.12720**  
<https://pubmed.ncbi.nlm.nih.gov/39037067/>

> Our findings show that asking for multiple responses in a single prompt, using an 'explain first, rate later' design, is both cost-effective and accurate (r = .62, .59 and .33 for novelty, feasibility and value, respectively).


### 3.6 Frontiers in Psychology: complete census of statistical notation

Twenty-eight abstracts of 107 carry a core statistic.

**Front Psychol 2026 — PMID 42661697 — doi:10.3389/fpsyg.2026.1887565**  
<https://pubmed.ncbi.nlm.nih.gov/42661697/>

> RESULTS: The instructors rated the materials favorably for academic fidelity (M = 4.24), proficiency appropriateness (M = 4.36), and teachability (M = 4.31), with acceptable inter-rater reliability, ICC(2, k) = 0.84.

> Automated structural-complexity indicators showed limited separation ( η p 2 = 0 .

> Differentiated-AI exceeded unified-AI most strongly among high-proficiency learners (d = 1.40), followed by a moderate advantage among low-proficiency learners (d = 0.60) and a small difference among intermediate learners (d = 0.16).

> The omnibus reading-comprehension interaction identified this heterogeneity, F(4, 126) = 7.43, p < 0.001, and η p 2 = 0 .

**Front Psychol 2026 — PMID 42656304 — doi:10.3389/fpsyg.2026.1897845**  
<https://pubmed.ncbi.nlm.nih.gov/42656304/>

> RESULTS: Group C scored significantly higher than Groups A and B on course satisfaction, professional competence, and psychological empowerment (all p < 0.001).

> Psychological empowerment showed a significant indirect association with learning outcomes (indirect effect = 0.22, 95% CI [0.12, 0.34]), with meaning and autonomy as the core dimensions.

> Humble mentor leadership significantly moderated the engagement-empowerment path within Group C (β = 0.24, p < 0.001), with the conditional indirect effect significant only under high humble leadership.

**Front Psychol 2026 — PMID 42656298 — doi:10.3389/fpsyg.2026.1922716**  
<https://pubmed.ncbi.nlm.nih.gov/42656298/>

> In the structural model (R 2 = 0.60), the strongest drivers were impulsivity (β = 0.40) and anthropomorphic attachment (β = 0.28), with a smaller contribution from AI anxiety (β = 0.15); trust was non-significant.

> Perceived AI literacy was modestly protective (β = -0.19), stronger in the full model than its zero-order correlation (r = -0.14)-a suppression effect, because more AI-literate students also trusted AI more and sat within more AI-reliant peer groups.

**Front Psychol 2026 — PMID 42597755 — doi:10.3389/fpsyg.2026.1932185**  
<https://pubmed.ncbi.nlm.nih.gov/42597755/>

> Data were analyzed using descriptive statistics, Pearson correlation analysis, confirmatory factor analysis (CFA), and structural equation modeling (SEM).

**Front Psychol 2026 — PMID 42583176 — doi:10.3389/fpsyg.2026.1860895**  
<https://pubmed.ncbi.nlm.nih.gov/42583176/>

> RESULTS: In the synthetic calibration, institutional trust is positively associated with AI service trust (IT → AST β = 0.607) and negatively associated with risk perception (IT → RP β = -0.271); risk perception is negatively associated with AI service trust (RP → AST β = -0.459); and AI service trust is positively associated with behavioral intention (AST → BI β = 0.424).

> The same directional pattern appears in the human-validation pilot (IT → AST β = 0.357; IT → RP β = -0.240; RP → AST β = -0.513; AST → BI β = 0.650).

> Scenario means also align with the simulation pattern (Pearson r = 0.803 for AST and r = 0.875 for BI across the nine cells), with the lowest pilot AST (3.667) and BI (3.413) in the fully automated high-risk condition.

**Front Psychol 2026 — PMID 42577402 — doi:10.3389/fpsyg.2026.1875025**  
<https://pubmed.ncbi.nlm.nih.gov/42577402/>

> RESULTS: A one-sided Wilcoxon signed-rank test showed significant improvement with LLM support [W(6) = 21.0, p = 0.0156, r = 0.879], with median accuracy increasing from 43.3% to 93.3% (median gain = 42.3%).

> Five of six students showed higher accuracy under the LLM-assisted condition, and no clear evidence of a sequence or carryover effect was detected (Mann-Whitney U = 7.0, p = 0.3758).

> Domain-level analyses indicated significant gains in all four categories (p < 0.05).

**Front Psychol 2026 — PMID 42553175 — doi:10.3389/fpsyg.2026.1842819**  
<https://pubmed.ncbi.nlm.nih.gov/42553175/>

> Furthermore, self-directed learning significantly moderated the path from learning motivation to hope, and the overall moderated mediation effect was statistically significant.

**Front Psychol 2026 — PMID 42553128 — doi:10.3389/fpsyg.2026.1884187**  
<https://pubmed.ncbi.nlm.nih.gov/42553128/>

> RESULTS: GenAI acceptance was significantly associated with PAD (total effect = 0.563, 95% CI [0.512, 0.615]).

> The serial indirect association involving both teaching innovation and learning motivation accounted for an additional 5.15% (effect = 0.029, 95% CI [0.018, 0.041]).

**Front Psychol 2026 — PMID 42539548 — doi:10.3389/fpsyg.2026.1834334**  
<https://pubmed.ncbi.nlm.nih.gov/42539548/>

> Crucially, we identify an "Authenticity Paradox": the lack of traditional human touch in AIGC does not alienate Generation Z; rather, the resulting "mindful friction"-quantified by a significant negative path effect between sentiment and identity ( β = - 0.370 ) -functions as a subcultural filter.

**Front Psychol 2026 — PMID 42539384 — doi:10.3389/fpsyg.2026.1794715**  
<https://pubmed.ncbi.nlm.nih.gov/42539384/>

> RESULTS: The results revealed that emotional expression accuracy differed significantly between human-composed and AI-generated music for rage (χ2 = 40.66, p < 0.001, Cramer's V = 0.27), ecstasy (χ2 = 25.53, p < 0.001, V = 0.21), and terror (χ2 = 16.46, p < 0.001, V = 0.17), whereas no significant difference was observed for grief (χ2 = 2.44, p = 0.12, V = 0.07).

> Across emotions, the largest accuracy gap was observed for rage (25.40%), followed by ecstasy (21.50%) and terror (17.00%), while the difference for grief was comparatively smaller (4.20%) and not statistically significant.

**Front Psychol 2026 — PMID 42495203 — doi:10.3389/fpsyg.2026.1848385**  
<https://pubmed.ncbi.nlm.nih.gov/42495203/>

> Among the two mediating pathways, ALT use demonstrates a small but significant partial mediating effect, whereas the HMS pathway is not statistically significant.

**Front Psychol 2026 — PMID 42488061 — doi:10.3389/fpsyg.2026.1875736**  
<https://pubmed.ncbi.nlm.nih.gov/42488061/>

> CONCLUSION: Continued DeepSeek use followed a cognitive-affective-behavioral sequence: perceived ease of use and usefulness drove satisfaction, which in turn predicted continuance intention (β = 0.769), while task-technology fit provided an independent behavioral pathway (β = 0.157), together accounting for actual continued use (β = 0.732).

**Front Psychol 2026 — PMID 42488041 — doi:10.3389/fpsyg.2026.1833118**  
<https://pubmed.ncbi.nlm.nih.gov/42488041/>

> RESULTS AND DISCUSSION: The proposed hybrid approach achieved an overall diagnostic agreement of 83.3% with manual clinical scoring, a Cohen's κ of 0.74 (substantial agreement), and demonstrated complete output stability across five independent runs.

> After excluding two technically compromised audio recordings, adjusted accuracy reached 90.9% with κ = 0.86.

**Front Psychol 2026 — PMID 42488035 — doi:10.3389/fpsyg.2026.1885211**  
<https://pubmed.ncbi.nlm.nih.gov/42488035/>

> Exploratory analyses indicated that high self-efficacy exhibited a potential buffering tendency against the negative correlation between FLA and WTC, though this interaction did not reach statistical significance (p = 0.068).

**Front Psychol 2026 — PMID 42459608 — doi:10.3389/fpsyg.2026.1878514**  
<https://pubmed.ncbi.nlm.nih.gov/42459608/>

> RESULTS: T1 LCU positively predicted T2a SRL (β = 0.345, p < 0.001) and T2b ASE (β = 0.118, p = 0.002), and T2a SRL positively predicted T2b ASE (β = 0.244, p < 0.001).

> Indirect effects from LCU to both T3 outcomes were supported through SRL, ASE, and the SRL-to-ASE sequence; no residual direct LCU-to-outcome paths remained statistically significant after these mechanisms were included.

**Front Psychol 2026 — PMID 42445257 — doi:10.3389/fpsyg.2026.1861001**  
<https://pubmed.ncbi.nlm.nih.gov/42445257/>

> Factor analyses identified two distinct latent constructs: perceived Impact of AI and AI-related Concerns, negatively correlated (r = -0.34, p < 0.001).

> Perceived Impact was positively predicted by age (β = 0.17), STEM (β = 0.19), Health/Agricultural/Veterinary sciences (β = 0.23), Economics/Law/Social Sciences (β = 0.16), and regular AI use, while negatively predicted by female gender (β = -0.09) and non-use (β = -0.35).

> AI-related Concerns were positively predicted by female gender (β = 0.21) and non-regular use (never: β = 0.20; occasionally: β = 0.29), and negatively by STEM (β = -0.11) and Health sciences (β = -0.15).

**Front Psychol 2026 — PMID 42433492 — doi:10.3389/fpsyg.2026.1834791**  
<https://pubmed.ncbi.nlm.nih.gov/42433492/>

> Data are analyzed using Pearson correlation and Hayes's PROCESS macro (Model 4) with 5,000 bootstrap resamples.

**Front Psychol 2026 — PMID 42427376 — doi:10.3389/fpsyg.2026.1847607**  
<https://pubmed.ncbi.nlm.nih.gov/42427376/>

> ANCOVA showed greater experimental-group gains in learner autonomy (partial η2 = 0.247), SRL strategies (partial η2 = 0.215), and intrinsic L2 motivation (partial η2 = 0.183), with no parallel effect on extrinsic goal orientation-a dissociation consistent with SDT.

**Front Psychol 2026 — PMID 42382618 — doi:10.3389/fpsyg.2026.1870870**  
<https://pubmed.ncbi.nlm.nih.gov/42382618/>

> Because the survey sample is small and self-selected, and because the query log is a convenience sample clustered at the student level, this is a descriptive analysis: we report effect sizes and predictive accuracy as within-corpus summaries and do not generalize to other cohorts.

> We summarized the corpus with frequencies, Cramer's V (reported descriptively, with Bonferroni-corrected p-values), Kruskal-Wallis comparisons, and a 5-fold cross-validated logistic regression.

**Front Psychol 2026 — PMID 42427383 — doi:10.3389/fpsyg.2026.1835593**  
<https://pubmed.ncbi.nlm.nih.gov/42427383/>

> In Task 1, the scripted group gained 5.75 more points on average than the non-scripted group, and the regression coefficient was 7.09, with an exact permutation test yielding p = 0.0286.

> Third, the script did not substantially increase effective feedback uptake, but it redirected revision toward the argument level; argument-level revision was positively associated with score gain (r = 0.755, p = 0.0304).

**Front Psychol 2026 — PMID 42338563 — doi:10.3389/fpsyg.2026.1848745**  
<https://pubmed.ncbi.nlm.nih.gov/42338563/>

> RESULTS: Generative AI demonstrated a significant positive effect on intellectual outcomes (Hedges' g = 1.096, 95% CI 0.087 to 2.104, p = 0.033) and a smaller but significant positive effect on social emotional outcomes (Hedges' g = 0.301, 95% CI 0.048 to 0.553, p = 0.020).

> The difference between the two outcome domains was not statistically significant (coefficient = -0.739, p = 0.252).

**Front Psychol 2026 — PMID 42293911 — doi:10.3389/fpsyg.2026.1859317**  
<https://pubmed.ncbi.nlm.nih.gov/42293911/>

> Pearson correlations were used to examine bivariate associations, and regression and PROCESS Model 6 analyses were conducted after controlling for sex, age, and grade to estimate specific and serial statistical indirect effects.

> Statistical indirect effects were tested using 5,000 bootstrap resamples and 95% confidence intervals (CIs).

> RESULTS: Perceived usefulness of generative AI for learning was positively associated with generative AI dependency (total association: β = 0.303, p < 0.001).

> It was negatively associated with metacognitive self-regulation (β = -0.260, p < 0.001) and positively associated with academic procrastination (β = 0.254, p < 0.001).

> Metacognitive self-regulation was negatively associated with academic procrastination (β = -0.218, p < 0.001) and generative AI dependency (β = -0.154, p < 0.001), whereas academic procrastination was positively associated with generative AI dependency (β = 0.224, p < 0.001).

> After metacognitive self-regulation and academic procrastination were entered, the direct association remained significant (β = 0.194, p < 0.001).

> The unstandardized statistical indirect effects via metacognitive self-regulation, academic procrastination, and the serial path involving both variables were 0.035 (95% CI [0.0236, 0.0479]), 0.050 (95% CI [0.0374, 0.0635]), and 0.011 (95% CI [0.0078, 0.0150]), respectively; the total statistical indirect effect was 0.096 (95% CI [0.0787, 0.1150]).

**Front Psychol 2026 — PMID 42293945 — doi:10.3389/fpsyg.2026.1826980**  
<https://pubmed.ncbi.nlm.nih.gov/42293945/>

> RESULTS: The findings revealed that perceived ease of use significantly predicted perceived usefulness (β = 0.648, p < 0.001) and directly influenced actual use (β = 0.311, p < 0.001).

> Perceived usefulness significantly predicted attitudes toward use (β = 0.638, p < 0.001), while attitudes toward use significantly affected actual use (β = 0.399, p < 0.001).

> In addition, pedagogical AI self-efficacy strongly predicted perceived ease of use (β = 0.647, p < 0.001) and indirectly contributed to technology acceptance.

**Front Psychol 2026 — PMID 42272743 — doi:10.3389/fpsyg.2026.1830103**  
<https://pubmed.ncbi.nlm.nih.gov/42272743/>

> At posttest, the experimental group scored significantly higher on writing proficiency (M = 15.23 vs.

> 11.91; large effect) and DCTS total (M = 89.84 vs.

**Front Psychol 2026 — PMID 42272713 — doi:10.3389/fpsyg.2026.1756148**  
<https://pubmed.ncbi.nlm.nih.gov/42272713/>

> Data analysis involved Pearson's correlations and hierarchical multiple regression.

> Attitudes toward GenAI had the strongest correlation with TSE-AI (r = 0.75, p < 0.001), followed by AISC (r = 0.69, p < 0.001) and GDC (r = 0.58, p < 0.001).

> After accounting for demographic factors, TSE-AI was the most significant predictor (β = 0.48, p < 0.001), with AISC (β = 0.25, p < 0.001) and GDC (β = 0.11, p = 0.015) also contributing.

**Front Psychol 2026 — PMID 42220377 — doi:10.3389/fpsyg.2026.1758670**  
<https://pubmed.ncbi.nlm.nih.gov/42220377/>

> METHODS: This study conducted a three-level meta-analysis of 36 empirical studies, synthesizing 132 effect sizes from 7,229 participants.

**Front Psychol 2026 — PMID 42183496 — doi:10.3389/fpsyg.2026.1831770**  
<https://pubmed.ncbi.nlm.nih.gov/42183496/>

> RESULTS: AI awareness and application negatively predicted autonomy (β = -0.190 and -0.332, respectively), while AI evaluation and ethics positively predicted competence (β = 0.315, 0.326) and relatedness (β = 0.333, 0.419).

> Contrary to predictions from social comparison and technostress theories, AI awareness positively predicted competence (β = 0.142) and relatedness (β = 0.172).

**Front Psychol 2026 — PMID 42094331 — doi:10.3389/fpsyg.2026.1755145**  
<https://pubmed.ncbi.nlm.nih.gov/42094331/>

> Results indicated statistically significant differences in both the prominence and ranking of values across groups.

> Effect-size estimates further indicated very large human-AI discrepancies, particularly in the religious (d = 2.21) and theoretical domains (d = 1.22).


### 3.7 Journal of Medical Internet Research: systematic every-third sample of notation-carrying abstracts

Sixty-seven of 138 JMIR abstracts carry a core statistic. Quoting all of them would
dominate the catalogue, so this is a mechanical every-third selection from that list
of 67, in retrieval order, giving 23 abstracts. Section 3.4 above already quotes the
reliability sentences from the full 138.

**JMIR 2026 — PMID 42696728 — doi:10.2196/95162**  
<https://pubmed.ncbi.nlm.nih.gov/42696728/>

> RESULTS: In the structured-input experiment, StoneAgent achieved higher performance than the standard LLM across metabolic specificity, guideline adherence, and actionability, with median case-level scores of 5.00 (IQR 5.00-5.00) vs 3.00 (IQR 2.75-3.92) for metabolic specificity, 5.00 (IQR 5.00-5.00) vs 3.67 (IQR 3.08-4.00) for guideline adherence, and 5.00 (IQR 5.00-5.00) vs 3.00 (IQR 2.67-3.33) for actionability (all P<.001).

> Safety pass rates were 100% (30/30) for StoneAgent and 83.3% (25/30) for the standard LLM (exact McNemar P=.06).

> Safety pass rates were 100% (30/30) for StoneAgent and 90% (27/30) for the standard LLM (exact McNemar P=.25).

**JMIR 2026 — PMID 42647856 — doi:10.2196/96002**  
<https://pubmed.ncbi.nlm.nih.gov/42647856/>

> After introducing a structured guideline appraisal workbook, agreement among human experts improved markedly-mean intraclass correlation coefficients (ICCs) increased from -0.09 to 0.66 to 0.84-0.92 across AGREE II domains.

> English-language guidelines outperformed Chinese-language guidelines in scope and purpose (mean 74.64, SD 15.4 vs mean 68.88, SD 13.9; P=.004) and applicability (mean 39.14, SD 18.6 vs mean 27.54, SD 16.7; P<.001).

> Backward-elimination logistic regression revealed external review as an associated process characteristic (odds ratio 20.39, 95% CI 4.66-89.27; P<.001).

> RIGHT assessments showed consistent reliability (ICC=0.80-0.88).

> Meta-analysis of RIGHT reporting rates showed lower reporting among Chinese-language than English-language guidelines (risk difference [RD] -0.07, 95% CI -0.13 to -0.02, 95% prediction interval [PI] -0.39 to 0.24) and among guidelines published before vs after RIGHT release (RD -0.19, 95% CI -0.26 to -0.13, 95% PI -0.56 to 0.17).

> Without additional guidance, agent-human agreement was moderate (ICC=0.608-0.629).

> In validation beyond rehabilitation, DeepSeek-R1 maintained stable agreement (ICC=0.711) and completed appraisals in 5.44 minutes compared to 11.18 minutes for humans.

**JMIR 2026 — PMID 42647045 — doi:10.2196/86251**  
<https://pubmed.ncbi.nlm.nih.gov/42647045/>

> The PP-LLM demonstrated almost perfect agreement with the reference standard (Gwet κ=0.959, 95% CI 0.937-0.981), comparable to two human readers (reader 1: κ=0.943; reader 2: κ=0.934), with no statistically significant difference in C-RADS classification accuracy.

**JMIR 2026 — PMID 42623484 — doi:10.2196/92499**  
<https://pubmed.ncbi.nlm.nih.gov/42623484/>

> RESULTS: At full coverage (Top@100%), LabBridge achieved 81% to 90% LOINC mapping accuracy across 5 LLMs on both Chinese and English datasets, outperforming all baseline methods (P<.01).

**JMIR 2026 — PMID 42600074 — doi:10.2196/94140**  
<https://pubmed.ncbi.nlm.nih.gov/42600074/>

> The safety UI bundle increased verification intention (mean 4.72, SD 0.63 vs 4.41, SD 0.59 on a 7-point scale; adjusted β=0.293, 95% CI 0.128-0.457; P<.001).

> Reliance intention did not increase (mean 4.97, SD 0.54 vs 5.03, SD 0.58; adjusted β=-0.105, 95% CI -0.239 to 0.029; P=.13).

> Trust calibration improved (trust calibration index: mean -0.29, SD 1.43 vs 0.29, SD 1.43; adjusted β=-0.567, 95% CI -1.005 to -0.129; P=.01).

> Expansion of optional source information was numerically higher, although the adjusted CI included the null (42% vs 27%; adjusted odds ratio [OR]=1.76, 95% CI 0.95-3.27; P=.07).

> Comprehension remained high and similar across arms (mean 6.33, SD 1.14 vs 6.32, SD 1.08; adjusted β=-0.132, 95% CI -0.428 to 0.163; P=.38).

> Perceived trustworthiness was modestly lower in the Safety UI arm (mean 5.20, SD 0.61 vs 5.39, SD 0.66; adjusted β=-0.199, 95% CI -0.382 to -0.016; P=.03).

**JMIR 2026 — PMID 42579604 — doi:10.2196/92374**  
<https://pubmed.ncbi.nlm.nih.gov/42579604/>

> Interrater agreement was moderate (Gwet AC1=0.58, 95% CI 0.42-0.75; P<.001).

> Differences in model preference were significant (Cochran Q=48.2; P<.001).

> Pairwise McNemar tests showed model 3 was preferred significantly more often than model 1 and model 2 (both P<.001), while model 1 versus model 2 did not differ after Bonferroni correction.

**JMIR 2026 — PMID 42574465 — doi:10.2196/86467**  
<https://pubmed.ncbi.nlm.nih.gov/42574465/>

> The SOAP Rewrite+ LLM Embeddings Classifier (GritLM-SOAP) achieved the highest mean F1-score (72.53%; 95% CI 62.40%-81.82%), while BioBERT-SOAP weighted achieved the highest mean recall (76.34%; 95% CI 62.69%-89.66%).

**JMIR 2026 — PMID 42561411 — doi:10.2196/89963**  
<https://pubmed.ncbi.nlm.nih.gov/42561411/>

> Statistical analysis was performed using generalized estimating equations (GEE), Friedman tests, and Wilcoxon signed-rank tests with Bonferroni correction.

> RESULTS: LLMs demonstrated significantly higher diagnostic accuracy for COPD compared to RP across all metrics (P<.001).

> For COPD, ranking performance was high and comparable among all models (MRR range: 0.82-0.89; P=.71).

> In RP, diagnostic performance differed significantly among models (MRR range: 0.10-0.39; P<.001).

**JMIR 2026 — PMID 42537013 — doi:10.2196/97772**  
<https://pubmed.ncbi.nlm.nih.gov/42537013/>

> RESULTS: Among the 46,823 screening-related posts, overall sentiment distributions showed no practically meaningful cross-cultural divergence (Cohen d=0.049); however, domain-specific analyses revealed sharp disparities in barrier prevalence.

> Furthermore, sentiment scores for mammography were significantly more negative than those for ultrasound alone (P<.001, Cohen d=0.264), and pain-related descriptors for ultrasound spiked from 5.0% (106/2110, ultrasound alone) to 18.2% (733/4017) when performed concurrently with mammography.

**JMIR 2026 — PMID 42525870 — doi:10.2196/93393**  
<https://pubmed.ncbi.nlm.nih.gov/42525870/>

> Friedman tests with Kendall W assessed overall differences; paired Wilcoxon tests with Bonferroni correction (adjusted α=.005) and rank-biserial r with Hodges-Lehmann 95% CIs were used post hoc.

> Reference authenticity was independently verified by 2 reviewers (XH and WH) using a 5-category scheme (V/PV/F/G/NR [V: Verifiable, PV: Partially Verifiable, F: Fabricated, G: Guideline-Based, Nonspecific, and NR: No References]), with consensus after canonical-source reverification (Cohen κ=0.702 preadjudication).

> RESULTS: Models differed significantly (caregiver: χ²4=77.5, W=0.538, P<.001; expert: χ²4=62.2, W=0.676, P<.001).

> DeepSeek ranked second (4.0 both), with superior Empathy versus ChatGPT-4o (r=-0.343; P<.001).

> Expert-caregiver agreement was strong (Spearman ρ=0.89; P=.04).

> Citation accuracy diverged sharply: OpenEvidence was fully verifiable (V=100%, F=0%), whereas DeepSeek and Zhipu Qingyan showed the highest fabrication (F of 33% and 24%, respectively); Gemini-2.5-Pro fabricated none but used nonspecific guideline citations (G=85%).

**JMIR 2026 — PMID 42497411 — doi:10.2196/92931**  
<https://pubmed.ncbi.nlm.nih.gov/42497411/>

> RESULTS: Claude Sonnet 4.5, ChatGPT-5.0, and Gemini 2.5 Pro each achieved 90% (36/40) primary-diagnosis accuracy, whereas DeepSeek-V3.2 achieved 67.5% (27/40; Cochran Q P<.001).

> In the primary mixed-effects logistic regression analysis, physician seniority group and LLM assistance stage were significantly associated with diagnostic correctness (both P<.001), whereas the group-by-stage interaction was not significant (P=.10).

> The questionnaire showed high internal consistency (Cronbach α=0.902) and generally positive attitudes, with no significant differences between physician groups (P=.11 to P=.78).

**JMIR 2026 — PMID 42462074 — doi:10.2196/97136**  
<https://pubmed.ncbi.nlm.nih.gov/42462074/>

> Professional evaluation showed high overall quality scores from both clinicians and the external LLM, with no significant difference between evaluators (mean total scores 18.15, SD 1.36 vs 18.28, SD 1.26; P=.55).

> Both patients and family members rated the reports highly, with no significant between-group difference in total scores (17.61, SD 1.60 vs 17.62, SD 1.03; P=.95).

> Subgroup analyses showed greater perceived benefit among older patients and outpatients (both P<.001); these subgroup findings should be considered exploratory given the lack of adjustment for multiple comparisons.

> Patients with chronic heart failure, reduced left ventricular ejection fraction (≤40%), and left ventricular enlargement (>55 mm) reported higher scores for addressing concerns (all P<.001).

> Anxiety scores increased significantly after conventional report release and decreased significantly after reading the patient-friendly report (both P<.001).

> Older patients (>60 y) and outpatients showed significantly higher anxiety change rates than their counterparts (both P<.001).

> The reduction in anxiety was positively correlated with subjective anxiety relief ratings (r=0.531; P<.001).

**JMIR 2026 — PMID 42452955 — doi:10.2196/90692**  
<https://pubmed.ncbi.nlm.nih.gov/42452955/>

> RESULTS: All knowledge-enhanced models significantly outperformed baseline in overall accuracy (baseline 68% vs fine-tuning 92.7%, RAG 91.3%, fine-tuning+RAG 97.3%; P<.001).

**JMIR 2026 — PMID 42430720 — doi:10.2196/85840**  
<https://pubmed.ncbi.nlm.nih.gov/42430720/>

> GPT-4o was benchmarked against human reviewers using sensitivity, specificity, and weighted Cohen κ.

> In children, denosumab produced the greatest 12-month increase in lumbar spine aBMD (25.49%, 95% CI 17.14%-33.84%).

> In adults, setrusumab at 12 months yielded the highest improvement (9.38%, 95% CI 6.5%-12.26%).

> Although there was substantial agreement with humans in the quality assessment (Cohen κ=0.778, 95% CI 0.710-0.846), the model exhibited optimism and positional biases due to reliance on probabilistic language patterns rather than structured clinical reasoning.

**JMIR 2026 — PMID 42418253 — doi:10.2196/93237**  
<https://pubmed.ncbi.nlm.nih.gov/42418253/>

> Domain experts conducted a pilot evaluation to align interpretation criteria prior to independently assessing the final dataset, yielding an interexpert agreement (Fleiss κ) of 0.762 across 337 drug-level assessments.

> Agreement with expert assessments was quantified using Cohen κ, weighted κ, and accuracy metrics.

> Internal consistency across repeated inferences was evaluated using Fleiss κ.

> Cohen κ ranged from 0.368 to 0.641, weighted κ ranged from 0.641 to 0.821, accuracy ranged from 0.583 to 0.804, and balanced accuracy ranged from 0.513 to 0.735.

> Fleiss κ ranged from 0.730 to 0.915, corresponding to substantial to almost perfect agreement.

> The highest Cohen κ was observed for Gemini 2.5 Flash with CoT prompting (0.641).

> Gemini 2.5 Flash with CoT-self-consistency prompting showed a Cohen κ of 0.640 and achieved the highest observed point estimates for weighted κ (0.821), accuracy (0.804), and Fleiss κ (0.915), although the gains over other prompting strategies were modest.

**JMIR 2026 — PMID 42379144 — doi:10.2196/88697**  
<https://pubmed.ncbi.nlm.nih.gov/42379144/>

> Using a random-effects model with Hartung-Knapp-Sidik-Jonkman adjustment, AI-driven chatbots showed a small-to-moderate reduction in depressive symptoms compared with control conditions, but the effect was not statistically significant (SMD=-0.46, 95% CI -1.02 to 0.10; P=.01; 95% prediction interval -1.50 to 0.58).

> Although overall effects were not statistically significant, emotional responsiveness, structured feedback, and interaction frequency were consistently associated with higher adherence.

**JMIR 2026 — PMID 42361337 — doi:10.2196/90547**  
<https://pubmed.ncbi.nlm.nih.gov/42361337/>

> A total of 5 LLMs performed significantly worse than humans (Holm-adjusted P≤.003 for all). gpt-oss-120b, o1, and o3-mini models achieved the highest F1-scores of all the evaluated LLMs.

> There was no significant difference in model accuracy among the top tier models (Claude 3.5 Sonnet, gpt-oss-20b, gpt-oss-120b, o1, o1-mini, and o3-mini), though GPT-4o achieved significantly lower accuracy than o1 (Bonferroni-adjusted P=.04).

**JMIR 2026 — PMID 42302307 — doi:10.2196/92852**  
<https://pubmed.ncbi.nlm.nih.gov/42302307/>

> Statistical analyses included Spearman ρ, Cronbach α, intraclass correlation coefficients, Friedman tests with Dunn multiple comparisons, and paired Wilcoxon signed-rank tests.

> The deployed retrieval-augmented model integrating the authoritative textbooks and the optimal LLM DeepSeek R1, HPHME-Xplus-RAG, achieved remarkable improvement in multidimensional scores compared to baseline DeepSeek R1 (median 8.00 [IQR 7.88-8.00] vs median 7.63 [IQR 7.38-7.88]; P<.001, r_rb=0.68, indicating a large effect).

**JMIR 2026 — PMID 42228942 — doi:10.2196/86498**  
<https://pubmed.ncbi.nlm.nih.gov/42228942/>

> Receiver operating characteristic analysis for discrimination and Spearman correlation between accuracy and each confidence metric was conducted.

> Top Weighted Score, a hybrid metric combining response frequency and self-reported confidence, was the only metric achieving statistically significant correlations across all 4 models: Gemini-3-Pro (ρ=0.52), GPT-5 (ρ=0.43), Claude-4.5-Sonnet (ρ=0.30), and GPT-4o (ρ=0.22).

> Receiver operating characteristic analysis revealed that Top Weighted Score demonstrated the highest discriminative ability, with area under the curve values of 0.826 (95% CI 0.731-0.920) for Gemini-3-Pro and 0.767 (95% CI 0.668-0.866) for GPT-5.

**JMIR 2026 — PMID 42077206 — doi:10.2196/94855**  
<https://pubmed.ncbi.nlm.nih.gov/42077206/>

> The construction phases were (1) exploratory corpus characterization, (2) iterative development of a 35-aspect hierarchical health outcome ontology, and (3) precision-optimized rule-based classification, validated through precision validation (stratified sample of n=500), recall estimation (n=510), external validation on 5 held-out channels (n=12,653 comments), large language model-assisted interrater reliability assessment, and transformer baseline comparison against Bidirectional Encoder Representations from Transformers (BERT) and Robustly Optimized BERT Pretraining Approach (ROBERTa) classifiers.

> RESULTS: The framework identified 1790 positive health outcome reports (1790/43,111, 4.15% prevalence), achieving 97.6% (488/500) precision (95% CI 95.7%-98.6%) and estimated 56.2% recall (95% CI 43.4%-67.9%).

> Significant channel-level variation was observed (χ²10=927.5; P<.001), with positive outcome rates ranging from 1.32% to 10.40% (odds ratio 8.68, 95% CI 7.10-10.61).

**JMIR 2026 — PMID 42066286 — doi:10.2196/88766**  
<https://pubmed.ncbi.nlm.nih.gov/42066286/>

> Interreviewer agreement was assessed using Cohen kappa coefficient.

**JMIR 2026 — PMID 42013456 — doi:10.2196/89540**  
<https://pubmed.ncbi.nlm.nih.gov/42013456/>

> Performance was assessed with micro- and macroaveraged F1-score and Matthews correlation coefficient (MCC), each reported with 95% bootstrap CIs.

> RESULTS: The LoRA-LLaMA-3 model achieved a micro-F1-score of 0.780 (95% CI 0.769-0.792) and an MCC of 0.533 (95% CI 0.518-0.546), outperforming other LLM baselines.

> Among all models, XGBoost obtained the highest scores (micro-F1-score of 0.815, 95% CI 0.804-0.826; macro-F1-score of 0.348, 95% CI 0.334-0.361; MCC 0.613, 95% CI 0.599-0.626).

> Ablation experiments identified dropout = 0.3, learning rate = 3×10-5, temperature = 0.1, and top-P= 0.1 as the optimal hyperparameter settings.

**JMIR 2026 — PMID 41945643 — doi:10.2196/82579**  
<https://pubmed.ncbi.nlm.nih.gov/41945643/>

> Paired accuracies were compared with the McNemar test to determine whether there was a statistically significant difference.

> RESULTS: Interreader agreement for RI-RADS was almost perfect for sLLM-augmented MERs (AC1 0.97, 95% CI 0.94-0.99) and moderate for clinician MERs (AC1 0.43, 95% CI 0.34-0.52).

> Overall protocol accuracy was 93.1% (566/608; 95% CI 89.6-96.6) for the sLLM, 91.4% (556/608; 95% CI 87.6-95.3) for Rad 3, and 92.1% (560/608; 95% CI 88.4-95.8) for Rad 4 (sLLM vs Rad 3 P=.23 vs Rad 4 P=.40).

> Region or coverage accuracy was similar (sLLM: 579/608, 95.2%; Rad 3: 585/608, 96.2%; Rad 4: 573/608, 94.2%; P=.46 and P=.36).

> Contrast decisions were more accurate using the sLLM at 94.4% (574/608; 95% CI 91.3-97.5) vs Rad 3 at 92.1% (560/608; 95% CI 88.4-95.8; P=.027) and were not significantly different to Rad 4 at 92.9% (565/608; 95% CI 89.4-96.4; P=.16).

> Subspecialty analyses showed similar patterns, with the sLLM outperforming Rad 4 for musculoskeletal MRI contrast decisions (96.6% vs 91.1%; P=.006) and matching readers elsewhere.

## 4. Counts by venue family

Each cell is the number of abstracts in that pool containing at least one match for
the statistic, with the percentage of the pool in parentheses. Denominators are the
full pools described in section 1.2, not the 48-abstract quoted sample. The three
italicised rows are tracked but excluded from "any of the above", because none of
them is statistical notation.

| Statistic | CHI | CSCW | TACL | ACL9 | Behav | FrontPsy | JMIR |
|---|---|---|---|---|---|---|---|
| kappa | 0 | 0 | 0 | 0 | 0 | 1 (1%) | 15 (11%) |
| alpha / ICC / IRR | 0 | 0 | 1 (1%) | 0 | 0 | 1 (1%) | 12 (9%) |
| chi-squared | 0 | 0 | 0 | 0 | 0 | 1 (1%) | 4 (3%) |
| rho / Spearman | 0 | 0 | 0 | 0 | 1 (2%) | 0 | 5 (4%) |
| d / effect size | 0 | 0 | 0 | 0 | 3 (5%) | 4 (4%) | 4 (3%) |
| r / Pearson | 0 | 0 | 0 | 0 | 3 (5%) | 9 (8%) | 10 (7%) |
| eta-squared | 0 | 0 | 0 | 0 | 0 | 2 (2%) | 2 (1%) |
| F / ANOVA | 0 | 0 | 0 | 0 | 0 | 1 (1%) | 2 (1%) |
| t / Wilcoxon | 0 | 0 | 0 | 0 | 0 | 2 (2%) | 11 (8%) |
| p-value | 3 (5%) | 0 | 1 (1%) | 0 | 2 (4%) | 16 (15%) | 48 (35%) |
| confidence interval | 0 | 0 | 0 | 0 | 3 (5%) | 4 (4%) | 31 (22%) |
| OR / beta | 0 | 0 | 0 | 0 | 2 (4%) | 11 (10%) | 9 (7%) |
| M / SD | 0 | 0 | 0 | 0 | 0 | 2 (2%) | 0 |
| **any of the above** | 3 (5%) | 0 (0%) | 2 (2%) | 0 (0%) | 9 (16%) | 28 (26%) | 67 (49%) |
| *sample size N= (non-core)* | 14 (22%) | 6 (13%) | 0 | 0 | 6 (11%) | 10 (9%) | 38 (28%) |
| *"significant" w/o notation (non-core)* | 10 (15%) | 10 (21%) | 26 (22%) | 1 (11%) | 13 (24%) | 59 (55%) | 59 (43%) |
| *regression/mediation words (non-core)* | 2 (3%) | 9 (19%) | 1 (1%) | 0 | 3 (5%) | 48 (45%) | 16 (12%) |

### 4.1 Two matches in that table are not what the category name implies

Honest reading requires two corrections, both of which push the headline lower rather
than higher.

The single TACL p-value match is `p = 0.5`, the nucleus-sampling threshold in
2025.tacl.35, quoted in full at section 3.3. It is a decoding hyperparameter, not a
test statistic. The single TACL alpha match is the phrase "substantial
inter-annotator agreement" in 2026.tacl.6, stated in words with no coefficient
attached. Corrected for both, **116 TACL abstracts contain zero numeric statistical
notation of any kind.**

The three CHI p-value matches are genuine. All three appear in the same form: a
p-value in parentheses immediately after a named outcome, with no test statistic, no
degrees of freedom, and no effect size. Section 3.1 quotes all three in full.

### 4.2 What the split shows

The result runs against the premise of the question. Human subjects are not what
drives statistical notation into an abstract.

CHI and CSCW are the two venues in this comparison where every paper is a
human-subjects paper, and they have the lowest notation rate of any family measured:
3 of 112, all three being a bare p-value at CHI, and zero at CSCW. TACL, which is
not a human-subjects venue, is at zero. The nine-abstract ACL baseline is also at
zero. Meanwhile the Journal of Medical Internet Research reaches 49 percent and
Frontiers in Psychology 26 percent.

What separates the high-notation journals from the low-notation venues is not
subject matter but abstract format. JMIR and Frontiers both use structured abstracts
with mandatory BACKGROUND / METHODS / RESULTS / CONCLUSIONS headings, and a RESULTS
heading creates a slot that a numeric result is expected to fill. Conference
abstracts at CHI, CSCW, TACL and ACL are single unstructured paragraphs, and in that
form the same result is written in words. The behavioural journals that use
unstructured or lightly structured abstracts sit between the two: PNAS, PNAS Nexus,
Nature Human Behaviour, Behavior Research Methods, Cognition, Cognitive Science and
the British Journal of Psychology together reach 16 percent, and 5 of those 55
abstracts state a confidence interval or a d.

So the convention is venue-dependent, but the dividing line is structured versus
unstructured abstracts, not human subjects versus not.

## 5. Numeral density

Numerals per 100 words. The rightmost column is the share of each pool denser than
1.92, the median of the nine 2026 ACL-venue abstracts already held in
`paper/reference/acl2026_abstracts.json`, re-measured here with the same counter.

| Pool | n | min | p10 | q1 | median | q3 | p90 | max | mean | share 0 | share >1.9 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| CHI (n=65) | 65 | 0.0 | 0.0 | 0.56 | 0.69 | 1.69 | 3.49 | 6.85 | 1.37 | 16/65 (25%) | 14/65 (22%) |
| CSCW (n=47) | 47 | 0.0 | 0.0 | 0.23 | 0.7 | 1.31 | 1.58 | 4.4 | 0.86 | 12/47 (26%) | 2/47 (4%) |
| HCI combined (n=112) | 112 | 0.0 | 0.0 | 0.35 | 0.69 | 1.41 | 2.74 | 6.85 | 1.16 | 28/112 (25%) | 16/112 (14%) |
| TACL (n=116) | 116 | 0.0 | 0.0 | 0.0 | 0.9 | 2.17 | 3.46 | 8.57 | 1.45 | 35/116 (30%) | 39/116 (34%) |
| PSY all PubMed (n=300) | 300 | 0.0 | 0.33 | 0.8 | 2.46 | 7.26 | 10.99 | 33.33 | 4.63 | 27/300 (9%) | 169/300 (56%) |
| PSY: JMIR (n=138) | 138 | 0.0 | 1.01 | 2.45 | 6.79 | 10.25 | 13.47 | 25.84 | 7.07 | 6/138 (4%) | 109/138 (79%) |
| PSY: Front Psychol (n=107) | 107 | 0.0 | 0.35 | 0.48 | 1.23 | 2.94 | 6.03 | 33.33 | 2.73 | 8/107 (7%) | 40/107 (37%) |
| PSY: PNAS+PNAS Nexus+NatHumBehav+BRM+Cognition+CogSci+BrJPsych (n=55) | 55 | 0.0 | 0.0 | 0.41 | 1.26 | 2.8 | 5.46 | 12.42 | 2.22 | 13/55 (24%) | 20/55 (36%) |
| ACL 2026 baseline file (n=9) | 9 | 0.0 | 0.81 | 1.25 | 1.92 | 2.82 | 5.37 | 5.98 | 2.46 | 1/9 (11%) | 4/9 (44%) |

CHI at 0.69 and CSCW at 0.70 are roughly a third the density of the ACL baseline.
TACL at 0.90 is under half of it, and the ACL baseline's own 1.92 sits at the 65th
percentile of the TACL distribution, so the nine-abstract file is numerically denser
than TACL abstracts typically are. A quarter of CHI and CSCW abstracts contain no
digit at all.

The psychology family is the only one that is reliably dense, and again it splits by
format: JMIR at a median of 6.79 is an order of magnitude above CHI, while the
unstructured behavioural journals sit at 1.26, which is below the ACL baseline.

An abstract carrying one percentage and no other numeral has a density near 0.5 for
a 200-word abstract. That is the CHI median region, below the TACL median, and below
the ACL baseline. It is unremarkable at all four conference venues and would read as
thin only against JMIR.

## 6. How the notation is written where it appears

Counted over the full 300-abstract PubMed pool, since the conference families supply
almost no instances.

**Symbol, not spelled name.** Kappa appears as the Greek letter in 18 instances of
"Cohen κ" against 1 of "Cohen kappa"; there are zero instances of `kappa = value`
against 17 of `κ = value`. Alpha is likewise always α ("Cronbach α" 2, "Cronbach
alpha" 0). Confidence intervals are written "95% CI" 119 times against "95%
confidence interval" 4 times. Cohen's d is written as a bare `d = value` 11 times
and spelled "Cohen's d" zero times.

**Named by variant.** Agreement coefficients are almost never bare. The pool contains
Cohen κ, Fleiss κ, Gwet κ and Gwet AC1, weighted κ, squared weighted κ, quadratic
weighted Cohen κ, Krippendorff α, and ICC(2,k). The variant is what is named; the
symbol follows it.

**With n, without degrees of freedom.** Sample size is reported constantly: 136
instances of `n = value`. Degrees of freedom are almost never reported. Across 300
abstracts there is one `F(4, 126)`, one `t (1)`, one `W(6)`, and zero instances of
chi-squared with degrees of freedom against 4 instances of `χ2 =` written bare. The
convention in an abstract is the coefficient and its value, sometimes a confidence
interval, and the sample size, but not the full test-statistic apparatus that would
appear in a results section.

**House style varies on p.** JMIR writes capital P with a leading-dot decimal
(`P<.001`, `P=.11`); Frontiers and the behavioural journals write lowercase p with a
leading zero (`p = 0.011`, `p < 0.001`). Of 195 p-value instances, 74 use the
leading-dot form.

## 7. Inter-rater reliability in abstracts

Abstracts reporting inter-rater reliability exist, and they are concentrated almost
entirely in one place. Section 3.4 quotes the complete census: 56 sentences, drawn
from the 300-abstract PubMed pool, of which all but two are from JMIR and the
remaining two from Frontiers in Psychology.

Across **112 CHI and CSCW abstracts and 116 TACL abstracts, not one reports an
inter-rater reliability coefficient.** A broader search over all 576 unfiltered
cs.HC records returned nine matches on the word "reliability", and reading them
shows every one is the ordinary English word applied to systems, infrastructure or
model behaviour ("the reliability of support", "LLM reliability such as
hallucinations", "evaluator reliability, uncertainty, and variance"), not a
psychometric coefficient. This matters for a paper with a coding scheme: CHI and
CSCW papers routinely code qualitative data, and they routinely do not put the
agreement statistic in the abstract.

The one conference instance of the concept is TACL 2026.tacl-1.6, which states it in
words with no number:

> We first demonstrate the effectiveness of the QASemConsistency methodology for human annotation, by collecting crowdsourced annotations of granular consistency errors, while achieving a substantial inter-annotator agreement.

Where a coefficient does appear, the standard phrasings are narrow. Reliability is
either declared as a method ("Interrater reliability was assessed using the
intraclass correlation coefficient"), reported with a verbal band attached
("Interrater agreement was substantial, with Fleiss κ=0.6449 for diagnoses"), or
used as a benchmark for a model ("approaching the human interrater benchmark"). That
third form, human agreement as the ceiling against which a model is measured, is the
one that would translate most naturally into an NLP abstract, and it is the only one
of the three that appears with a rhetorical purpose rather than as a compliance
statement.

## 8. What an ARR abstract can carry

For a paper submitted through ARR that argues within human-AI interaction, the two
audiences are closer together than the question assumes. ACL-venue abstracts, TACL
abstracts, CHI abstracts and CSCW abstracts all write results in words, with a
numeral or two, and no test statistics. The convention that would clash is not the
HCI one; it is the structured-abstract convention of health and psychology journals,
and no reviewer at either target venue expects it.

**Reads as normal to both audiences.**

A participant or item count written as N=. This is the most common piece of
quantitative notation in the HCI family, though it is a minority practice rather than
a norm: 22 percent of CHI abstracts and 13 percent of CSCW abstracts state it. Of the
65 abstracts in the HCI pool that describe an empirical study, 14 give the sample size
in N= form and 51 do not, so an abstract that names a study without numbering it is
the more common pattern. N= is also the most frequent numeric convention in the
psychology pool, at 54 of 300. TACL abstracts do not use it at all. Either choice is
defensible at these venues; what the corpus supports is that including it is normal,
not that omitting it is a lapse.

A percentage or a plain effect magnitude attached to a named outcome, in the form
already present in the current abstract. Both families do this constantly, and both
do it without attaching a test.

A single p-value in parentheses after the primary comparison, if one comparison
genuinely carries the claim. Three CHI abstracts do exactly this, and the form is
consistent: outcome named, p in parentheses, nothing else. It is uncommon rather than
odd. It buys precision at the cost of looking slightly more clinical than the median
CHI abstract, and it should be used once if at all, not three times.

**Reads as out of place to at least one audience.**

Kappa, Krippendorff's alpha, or any agreement coefficient. Zero instances across 228
conference abstracts. Putting one in the abstract would mark the paper as written to
a journal convention rather than a conference one, at both venues simultaneously.
The coefficient belongs in the body, and the abstract can say that annotation was
reliable without quantifying it, as 2026.tacl-1.6 does.

Confidence intervals, F, t, chi-squared, eta-squared, and Cohen's d. Zero instances
across CHI, CSCW, TACL and the ACL baseline. These appear only in structured-abstract
journals and in a small number of behavioural-journal abstracts. Any of them in an
ARR abstract would read as imported from a different literature.

Degrees of freedom. Even the journals that report test statistics in abstracts drop
the degrees of freedom: one `F(df1, df2)` and one `t(df)` in 300 abstracts. There is
no venue in this comparison where `F(1, 47) = 8.32` in an abstract is conventional.

Greek letters generally. Every Greek-letter instance in the entire corpus is from
PubMed. None appears in 112 CHI and CSCW abstracts, 116 TACL abstracts, or the nine
ACL abstracts.

**On density.** The current abstract, with one percentage, sits near the CHI median
and below the TACL and ACL medians. There is room to add one or two numerals without
approaching the upper quartile of any conference family, and no evidence that a
denser abstract reads as more rigorous at these venues: a quarter of CHI and CSCW
abstracts have no digits at all, and the ACL baseline's densest entries are reporting
benchmark scores rather than inferential statistics.

The move with the best support in this corpus is therefore to add the sample size in
N= form and, if one comparison is genuinely primary, a single bare p-value beside it,
and to leave every agreement coefficient, interval and test statistic in the body.
