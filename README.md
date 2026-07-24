# Code Smells Practice Project

A hands-on repo for learning to recognize and fix common code smells in Python.
Each folder covers one smell: a short explanation, a deliberately "bad" practice
script demonstrating it, and (kept separately, see below) a reference solution.

Source material / definitions: [Refactoring Guru — Code Smells](https://refactoring.guru/refactoring/smells)

## Smells covered (in order of importance)

1. Duplicate Code
2. Long Method
3. Large Class
4. Comments
5. Dead Code
6. Speculative Generality
7. Long Parameter List
8. Data Clumps

## How to use this repo

1. **Pick a smell folder**, starting from #1 if you're new to this.
2. **Run `Code_smell_bad.py`** and note its output.
3. **Refactor `Code_smell_good.py` yourself.** The goal is always: fix the
   structure, but keep the printed output identical to before your changes.
   That's your correctness check — if the output changes, you fixed the
   wrong thing.
4. **Only after you've made a real attempt**, compare your version against
   the reference solution for that smell.
5. Move to the next folder and repeat.

Don't skip straight to the solution. The value of this exercise is in
struggling with the "why does this feel wrong" question before seeing the
answer — reading a clean version without attempting your own teaches you
much less than writing one and comparing.

## Requirements

- Python 3.10+ (some scripts use f-string features and standard library
  only — no external packages needed)

## Contributing / feedback

If you spot a bug in a practice script or think a smell's explanation could
be clearer, open an issue or a PR.