# Draft reply to Tania, 2026-09-21

Answering her question: "Did you take in the other comments from my last email or the second
to last. There were missing sections. And I had those comments on findings vs methods etc."

Liam's to edit and send. Substance is checked; register is his call.

---

Most of them, and one I had not, which you were right to raise.

**The sections.** Your version runs Introduction, Related Work, Methods, Results, Conclusion,
Limitations, Ethics Statement. The current draft is that same list. The one deliberate
difference is that our Limitations is unnumbered, because 40 of the 50 papers in the corpus
leave it unnumbered. Worth saying that when you wrote, the draft already had all of those plus
a Discussion, and we then cut the Discussion on your evidence: only 4 of Ali's 24 papers have
one, and 8 of 23 core-NLP papers carry that function in the Conclusion and Limitations
instead, which is your arrangement.

**Findings versus methods.** We went with your (a) and (c) together. STET ships as a named
diagnostic rather than a benchmark, which keeps the citable artifact and steps around the "40
is too small for a benchmark" objection. Then we ran the split-half test you said was
decidable from data we already held, and it came back stronger than you expected. Across 1,000
random splits of the 40 tasks into halves, the model ranking agrees at mean Spearman 0.972,
every split clears 0.8, and Llama is last in all of them. A generalizability decomposition
gives 0.992 at 40 tasks, where 5 tasks would already reach 0.95, because the variance between
models is 3.2 times the model-by-task residual. So 40 is not merely defensible; it is well past
what the measurement needs, and we can say so with a number instead of an argument.

The honest limit is that this holds for one thing only. The quality decline does not rank
models stably: its generalizability is 0.780 and it would need roughly 215 tasks. The reason is
diagnosable. A meta-response strips to near-empty text and scores about 1, so the raw delta
measures how often a model produces meta-responses rather than how much damage it does. That
is why STET scores restraint and the decline stays a finding.

**The close.** This is the one I missed. You flagged on the 9th that the abstract and the
introduction end on different claims and asked which one the paper is arguing. It had been
recorded as waiting on your answer, which was wrong, since you had put the decision to us. The
abstract now ends on your line: revision robustness, a model's willingness to leave sufficient
work alone, deserves evaluation alongside single-turn capability. All three of the abstracts
you sent on the 3rd close on that sentence, and the Conclusion already carried it, so the
abstract was the only one out of step. It keeps the two-sided finding before it, which is how
your Version C is built. 214 words against a corpus ceiling of 229.

**The other thing from the 9th.** The units mismatch is fixed. The abstract and the
introduction both carry the 70% now, and the introduction adds the 0.74, so they are no longer
describing the same degradation in incompatible units.

**One of your style notes I did not take,** and I would rather say so than leave you to spot
it. You suggested a signposted turn in the findings paragraph, "Importantly," as one of Ali's
recurring words. It is in his corpus and you are right about that. I have a standing rule
against relevance tags, sentences that tell the reader a fact matters rather than letting the
fact do it, and "Importantly" is that. The rest of your style additions are in: the concrete
hook, the question at the end of the first paragraph, Figure 1 referenced inside the
introduction, the explicit gap sentence, and the close restating the title. The introduction
runs 759 words against a corpus band of 561 to 768, so it passes, though it sits at the top of
it and above the 700 you measured from four papers.

Attached is the current build.

---

## Notes for Liam, not for the email

- Everything quantitative above is checked. The 0.972 / 0.992 / 3.2x / 0.780 / 215 figures are
  in `results_FINAL.md` section 13, and the abstract word count and intro band come from
  `07_prose_census.py`.
- Cut the "One of your style notes I did not take" paragraph if you would rather not raise it.
  It is honest but it is the only place the reply pushes back on her.
- If you want it shorter, the sections paragraph is the most cuttable; she can see the section
  list in the attachment.
