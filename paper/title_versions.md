# Title versions

Every candidate considered, in order. Evidence base: `paper/rules/01_title.md`, a 54-title
corpus retrieved 2026-09-02 from arXiv CS. Key findings used throughout: colon titles are
32 of 54 and rising to 77% of 2025 titles; plain declaratives 9 of 54; median 9.5 words with
39 of 54 between 6 and 12; colon heads are names or claims, never descriptions, median 3
words; every negative title in the corpus bounds its claim; "intrinsic self-correction" is
field-standard (7 arXiv titles, 24 records) while "extrinsic direction" returns 1 arXiv
record total, a 2018 graphene physics paper.

## CURRENT (set 2026-09-03)

**Worse on Request, Better on Critique: Self-Correction on Work That Is Already Sufficient**

13 words. Colon form. Head is a claim, not a description. Bounded by "already sufficient",
which is also the condition that distinguishes this work from RefineBench. Carries the
field-standard term "self-correction" for discoverability. Echoes the abstract: critique x2,
request x2, sufficient x2, self-correction x1.

## Superseded

- **The More You Ask, The Worse It Gets: How LLMs Waste Tokens Revising Past Their Own Best
  Output** (v1). Retired after the mentor call: over-weighted tokens, misrepresented scope.
- **Intrinsic Self-Correction Requires Extrinsic Direction** (locked 2026-07, retired
  2026-09-03). Two faults found by the title research: "Requires" is an unbounded universal
  claim that 720 trials do not establish, and "extrinsic direction" is not this field's
  vocabulary. Zero echo in the abstract for either half.

## Round 1, ten themes (2026-09-02)

1. Undirected Revision Degrades More Often Than It Improves
2. Language Models Decline to Revise Without Saying So
3. Intrinsic Self-Correction Rarely Improves Without External Feedback
4. Language Models Cannot Tell When Their Work Is Finished
5. What the User Cannot Name, the Model Cannot Fix
6. Revision Requests Without Direction Overwrite Sufficient Work
7. Quality Degrades Under Self-Revision in Ways Readers Barely Notice
8. Models Improve Their Own Work Only When Told What Is Wrong
9. First Drafts Are the Best Drafts Under Undirected Revision
10. Undirected Revision Spends Tokens to Lower Quality

## Round 2, blending intrinsic/undirected/sufficient/feedback

1. Intrinsic Self-Correction Degrades Work That Is Already Sufficient
2. Undirected Revision Degrades Work That External Feedback Repairs
3. Intrinsic Self-Correction Lowers Quality More Often Than It Raises It
4. Intrinsic Self-Correction Requires External Feedback to Improve Sufficient Work
5. Undirected Revision Rarely Improves and Often Degrades Sufficient Work
6. Models Cannot Tell When Sufficient Work Needs No Revision
7. Intrinsic Self-Correction Degrades Sufficient Work Until It Is Directed
8. Without External Feedback, Revision Degrades Already-Sufficient Work
9. Asked to Improve Sufficient Work, Models Make It Worse
10. Models Revise Sufficient Work Into Worse Work

## Round 3, mixed forms, ranked

1. Intrinsic Self-Correction Degrades Work That Is Already Sufficient
2. Make It Better: What Undirected Revision Does to Sufficient Work
3. Undirected Revision Rarely Improves and Often Degrades Sufficient Work
4. Intrinsic Self-Correction Requires External Feedback to Improve Sufficient Work
5. Overcorrection: Undirected Revision of Already-Sufficient Model Output
6. Models Cannot Tell When Sufficient Work Needs No Revision
7. Undirected Revision Degrades Work That External Feedback Repairs
8. Nothing to Fix: Undirected Revision of Already-Sufficient Output
9. Can Models Tell When Their Work Is Finished?
10. Intrinsic Self-Correction Degrades Sufficient Work Until It Is Directed

## Author draft (Liam, 2026-09-03)

> "Improvement that destroys?": Undirected model revision degrades sufficient work that
> external feedback could have fixed.

Not carried forward as written. "Destroys" is unbounded and unsupported: 60% of revisions do
not move the quality level at all, and blind readers pick the first draft only 56% of the
time. "Could have fixed" claims a counterfactual the targeted-feedback phase does not test in
that form. 15 words against a median of 9.5. What was kept: the question head, the paradox,
"undirected model revision", "sufficient work", and the external-feedback contrast.

## Round 4, question and first-person heads

1. Can You Make It Better? Undirected Revision Degrades Already-Sufficient Work
2. I'm Not Sure, Can You Make It Better? Undirected Revision Degrades Sufficient Work
3. Improvement Without Direction: Model Revision Degrades Work That Was Already Sufficient
4. Improvement That Costs: Undirected Model Revision Lowers the Quality of Sufficient Work
5. Undirected Model Revision Degrades Sufficient Work That Direction Would Improve
6. Is This Good Enough? Undirected Revision of Already-Sufficient Model Output
7. Worse On Request: Undirected Revision of Sufficient Model Output
8. Just Make It Better: What Undirected Revision Costs Sufficient Work
9. The Price of Asking Again: Undirected Revision Degrades Sufficient Work
10. Asked to Improve, Models Make Sufficient Work Worse

## Round 5, carrying the feedback-repair component

1. Undirected Revision Degrades Sufficient Work That One Critique Restores
2. Can You Make It Better? Undirected Revision Degrades Work a Single Critique Restores
3. Improvement Without Direction: Model Revision Degrades Work a Critique Repairs
4. Direction Repairs What Undirected Revision Degrades
5. Is This Good Enough? Undirected Revision Degrades Work That One Critique Restores
6. Undirected Model Revision Degrades Sufficient Work That Direction Restores
7. Worse On Request, Better On Critique: Undirected Revision of Sufficient Work
8. Models Degrade Sufficient Work Without Direction and Restore It With One Critique
9. I'm Not Sure, Can You Make It Better? Undirected Revision Degrades Work One Critique Restores
10. One Critique Restores What Five Undirected Turns Destroy

## Round 6, refining the author's parallel head

Head fixed as **Worse on Request, Better on Critique:**

1. Undirected Revision of Already-Sufficient Work
2. Undirected Revision of Sufficient Model Output
3. What Undirected Revision Does to Sufficient Work
4. Undirected Revision Across Six Models and Forty Tasks
5. (head variant) Worse on Asking, Better on Telling

## Round 7, tails that add a second beat

1. What Models Do When Nothing Needs Fixing
2. Model Revision When Nothing Needs Fixing
3. Why Models Revise Sufficient Work and Make It Worse   <- author's pick
4. Five Turns of Undirected Revision Across Six Models
5. Most Revision Requests Produce No Revision at All
6. Measuring Undirected Revision Against Targeted Critique
7. The Cost of Revising Work That Was Already Good

## Round 8, fixing the repeated word

The author's pick repeated "Worse" twice, six words apart.

1. Why Models Revise Sufficient Work
2. Why Models Revise Work That Needs No Revision
3. Why Models Keep Revising Sufficient Work
4. Why Models Revise Sufficient Work Anyway
5. Why Models Revise Sufficient Work and Degrade It   <- author's fix

## Round 9, final

Author's fix assessed against the corpus. Strengths: bounded, strong abstract echo, head is a
claim, avoids saturated constructions, no imperative. Costs: 14 words against a median of 9.5;
6-word head against a median of 3; no field vocabulary at all, so it is not discoverable by
this literature's own keywords; head and tail both state the degradation.

Adopted instead, keeping the head untouched and buying back discoverability:

**Worse on Request, Better on Critique: Self-Correction on Work That Is Already Sufficient**

What it gives up: "and Degrade It", and the "why".
