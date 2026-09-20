# Terminology sweep

Written by `paper/preflight.py`. Flags need reading in context: this sweep has produced false positives before, notably matching
"sufficient threshold" inside the correct phrase "not-sufficient threshold".

```
1. SEVERAL NAMES SHARING ONE HEAD NOUN
   (each group is one head; judge whether the modifiers name one thing)

   content      new task (3);  stripped (3)
   output       complex (2);  initial (2);  already-sufficient (2);  post-turn (2)
   probe        balanced (2);  study s balanced (2)
   revision     genuine (11);  targeted (3);  undirected (3);  generic (2)
   turn         single (2);  every (2);  next (2)

2. HYPHEN AND SPACING VARIANTS
   turn (69);  turn- (1)
   first turn (1);  first-turn (1)
   five turn (2);  five-turn (3)

3. CAPITALISATION OF DEFINED TERMS
   sufficient         capitalised   4   lower  19
   incomplete         capitalised   2   lower   1
   turn               capitalised  26   lower  43

4. WHO DOES THE SCORING: one word per role?
   evaluator    13   {'introduction_v2': 1, 'methods': 6, 'results_v2': 2, 'limitations': 2, 'appendix': 2}
   judge         7   {'abstract_v2': 1, 'related_work_v2': 4, 'methods': 1, 'limitations': 1}
   rater         9   {'introduction_v2': 1, 'methods': 4, 'limitations': 2, 'appendix': 2}
   annotator     3   {'methods': 2, 'results_v2': 1}
```
