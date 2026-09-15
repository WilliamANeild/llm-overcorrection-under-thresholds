# Tania Neild, review of the introduction, title and Figure 1

Received 2026-09-09, in reply to Liam's email of 2026-09-08 20:47 ("Let me know what you
think on the introduction, title and main image").

Recorded verbatim, including typos, because these are her words. Analysis of the review
lives in a separate file; nothing here is edited.

---

## Her two open issues

> Two open issues…I cannot solve.
>
> This slightly changes from the abstract.
> How much quality falls
>
> Abstract: "quality falls 0.74 levels from the first turn to the fifth (p = 1.01×10⁻⁴)"
> Intro: "70% of the changes that move quality move it down, and where the work was already
> sufficient, 27% of revisions leave it below the threshold."
> Status: this is the main mismatch. Both describe degradation, but in incompatible units,
> mean level change versus proportion of changes. Neither the 70% nor the 27% exists in the
> old body we drew the abstract from, and the 0.74 figure appears nowhere in the new intro.
> Recall we deliberately removed the 70% from the abstract two versions ago because it
> wasn't in the body; the new intro now leads with it, so either the results section gained
> a new analysis or the intro is citing something not yet written up.
>
> Also, we have an issue as our introduction closing and our abstract conclusions are
> slightly off.
>
> Abstract: "Revision robustness, a model's willingness to leaveient work alone, deserves
> evaluation alongside first-turn capability."
> Intro: "Intrinsic self-correction, on its own, is not enough: it requires extrinsic
> direction."
> The abstract ends on an evaluation-methodology recommendation; the intro ends on the
> paper's original title claim. Worth deciding which one the paper is actually arguing for
> and using it in both.
>
> But if you fix those two issues….here is my version. Thoughts?

---

## Her rewritten introduction

> Large language models can draft a policy memo, debug a function, or summarize a quarter
> of sales in one turn, and on benchmarks built around that turn they perform well (Liang
> et al., 2023). Yet the same models, asked four times to improve a sales summary that was
> already adequate, strip out the very explanations the prompt requested (Figure 1). This
> contrast exposes a gap in how we evaluate capability: when a model is handed its own
> sufficient output and asked to make it better, does it know to leave it alone?
>
> The question matters because deployed tasks are rarely singleurn. They are workplace
> tasks carried out with a user who supplies the goal, reacts to the output, and asks for
> changes (Anthropic, 2025a; Laban et al., 2026), and the quality that user receives depends
> on what they can contribute. Real prompts are frequently underspecified, and under
> specification degrades what follows (Yang et al., 2026). The contribution that matters
> most is the ability to say what is wrong. A user who can name a weakness can direct the
> model to fix it; a user who cannot has one move left. Scalable-oversight research
> identifies exactly this condition: users unable to articulate precise intent or validate a
> complex output (Zhou et al., 2026). They ask for the work to be improved without saying
> what improving it would mean, the request vendor guidance is written against (OpenAI,
> 2025; Anthropic, 2025b).
>
> Whether models can improve their own outputs has been studied as self-refinement. Madaan
> et al. (2023) show that a model allowed to critique and rewrite its work can raise its
> quality, and locate the benefit in feedback that is actionable and specific. Subsequent
> work finds the benefit fragile: without external feedback, models struggle to correct
> their own reasoning and at times degrade it, with apparent gains often traceable to leaked
> oracle labels (Huang et al., 2024). A critical survey locates the bottleneck in feedback
> generation rather than in the capacity to revise (Kamoi et al., 2024), and Laban et al.
> (2026) show that accuracy falls across turns when requirements arrive piecewise.
>
> These results share a critical assumption: that the output being revised is wrong.
> Intrinsic self-correction, revision driven by the model's own judgment with no outside
> signal (Huang et al., 2024; Kamoi et al., 2024), is studied on outputs that need repair,
> and multi-turn degradation on tasks whose requirements are incomplete. No study measures
> the case a non-expert user actually creates: a fully specified task, an output that is
> already adequate, and repeated requests to revise that carry no feedback at all. Measuring
> it also requires controlling for an artifact the revision act itself introduces into
> automated evaluation.
>
> Is a sufficient output safe in a model's hands once the user asks for more? We study this
> question directly. A model completes one of forty fully specified tasks, spanning code,
> data logic, analysis, writing, and creative writing, and is then offered, across four
> further turns, a neutral choice to keep its output or revise it, with no indication of
> what to change. Counting the initial draft, each conversation runs five turns. The design
> spans six models, 720 conversations, and 3,600 responses. We ask whether a model revises
> at all (RQ1), whether the output improves or degrades when it does (RQ2), and whether
> failure traces to capacity or to the absence of direction (RQ3). We strip the
> meta-commentary models attach to revisions and validate every quality judgment against
> human raters.
>
> Most of the work being revised did not need it: 88% of the 720 first drafts are already
> sufficient. Asked to improve them without direction, models mostly do not revise: by the
> fifth turn, 86.7% of replies are meta-responses, restatements and declines presented as
> compliance rather than new task content. When they do revise, quality tends to fall,
> dropping 0.74 levels from the first turn to the fifth (p = 1.01×10⁻⁴), and the decline
> holds across all five domains. For all six models the first draft is the
> quality-maximizing stopping point, so every later turn is, on average, spent making the
> work worse or no better. We name this waste the revision tax, the tokens spent past the
> optimal turn, and find it accounts for 62.1% of all output generated. Importantly, the
> failure is one of direction rather than capacity: a single specific critique reverses the
> decline, lifting revised output 1.16 levels above undirected iteration (p = 5.7×10⁻¹⁹).
> Blind readers prefer the first draft to the last in 56% of decisions, an interval that
> includes chance, which is itself the point: the degradation is real, and no-expert
> reliably sees. Intrinsic self-correction, on its own, is not enough; it requires extrinsic
> direction.

---

## Her rationale, in her words

> **My changes**
>
> The opening earns attention faster. His original opened on "Large language models are
> evaluated, for the most part, alone,” An abstract claim. This version opens on a concrete
> failure the reader can picture (a model stripping explanations out of a sales summary it
> was asked to improve) and turns it into the paper's question in three sentences.
>
> The question is stated as a question. Your draft implied the research question across
> several sentences but never posed it crisply. This version ends paragraph one with "does
> it know to leave it alone?", which is the single line a reviewer will carry through the
> paper.
>
> The gap is sharper. The draft said the prior work "bracket the question we ask without
> answering it," which is accurate but soft. This version names the shared assumption
> directly, "these results share a critical assumption: thathe output being revised is
> wrong", which is a cleaner hinge into the contribution.
>
> The findings are front-loaded with numbers. I like numbers…Your original findings
> paragraph described the results qualitatively (models "mostly do not revise," revisions
> "get worse"). This version keeps that prose but attaches the actual figures (86.7%, 0.74,
> 62.1%, 1.16), so a reader skimming the intro alone comes away knowing the magnitude, not
> just the direction.
>
> The revision tax is introduced as a named contribution. Your draft mentioned the waste but
> didn't name it in the intro. Naming it here gives the paper a citable handle and matches
> the abstract.
>
> **Things that I add style wise to be consistent with the other papers..**
>
> A concrete hook, then a one-line question. All four of his intros open on a vivid example
> or contrast and land a crisp question by the end of the first or second paragraph. This
> one does both in paragraph one.
>
> Figure 1 referenced inside the intro as the motivating example, exactly as Taarof
> ("Considerhe scenario in Figure 1") and Thought Injection do.
>
> An explicit gap sentence right before the contribution, the "no study measures / no
> benchmark examines" move that appears in all four.
>
> "We introduce X" with the artifact in bold, his constant.
>
> Enumerated findings with a signposted turn, here "Importantly," which is one of his
> recurring signpost words alongside "critical" and "striking," both also present.
>
> Dense citations quarantined to the related-work paragraph, light citations in the hook.
>
> Length in band. His run ~520 to 700 words; this is ~620, upper-middle.
>
> The closing thesis restates the title. Indica closes by restating its claim; this closes
> on "intrinsic self-correction... requires extrinsic direction," which is the paper's title
> turned into a sentence, his pattern exactly.
>
> The one intentional deviation: Your teachers intros usually place "We introduce X"
> immediately after the gap, whereas here the bolded revision tax appears in the findings
> paragraph instead. That's because this paper's contribution is a finding and a metric
> derived from results, not a benchmark that exists before the experiments, so introducing
> the term before the results would misrepresent it.
