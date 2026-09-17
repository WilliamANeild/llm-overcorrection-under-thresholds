# Terminology sweep

Written by `paper/preflight.py`. Flags need reading in context: this sweep has produced false positives before, notably matching
"sufficient threshold" inside the correct phrase "not-sufficient threshold".

```
1. SEVERAL NAMES SHARING ONE HEAD NOUN
   (each group is one head; judge whether the modifiers name one thing)

   content      new task (3);  stripped (3)
   output       complex (2);  initial (2);  post-turn (2)
   probe        balanced (2);  study s balanced (2)
   revision     genuine (11);  undirected (7);  targeted (3);  generic (2);  directed (2)
   turn         single (2);  every (2);  first (2);  next (2)

2. HYPHEN AND SPACING VARIANTS
   turn (70);  turn- (1)
   first turn (2);  first-turn (2)
   five turn (2);  five-turn (2)

3. CAPITALISATION OF DEFINED TERMS
   sufficient         capitalised   4   lower  18
   incomplete         capitalised   2   lower   1
   turn               capitalised  23   lower  47

4. WHO DOES THE SCORING: one word per role?
   evaluator    12   {'introduction_v2': 1, 'methods': 6, 'results_v2': 1, 'limitations': 2, 'appendix': 2}
   judge         9   {'abstract_v2': 1, 'related_work_v2': 3, 'methods': 1, 'discussion': 3, 'limitations': 1}
   rater         9   {'introduction_v2': 1, 'methods': 4, 'limitations': 2, 'appendix': 2}
   annotator     3   {'methods': 2, 'results_v2': 1}
```
