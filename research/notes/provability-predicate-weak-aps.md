# Provability Predicate in Weak APS

Source: https://chatgpt.com/share/6a1ac9ff-0b20-83a5-8adf-2ce37a8708d1

Imported: 2026-05-30

## Core Idea

This thread treats Feferman-, Shavrukov-, Rosser-, and KD-style provability
predicates as controlled failures of the APS axioms rather than as irrelevant
non-examples.

The organizing contrast is:

$$
\text{standard }\Sigma_1\text{-provability}
\leadsto
\text{GL/K4-like APS with A4},
$$

$$
\text{Feferman/Shavrukov/KD-like provability}
\leadsto
\text{serial weak-APS with controlled A4 failure}.
$$

Thus these predicates are useful test cases for measuring exactly where APS
needs the introspection-like axiom A4 in order to yield G2/FG2 behavior.

## APS Translation

Starting from a Lindenbaum preorder:

$$
[\varphi]\le [\psi] \Longleftrightarrow T\vdash \varphi\to\psi,
$$

one can define:

$$
\Box[\varphi]=[Pr(\ulcorner\varphi\urcorner)],
$$

$$
\boxtimes[\varphi]=[Pr(\ulcorner\neg\varphi\urcorner)].
$$

For standard provability, this tends toward the familiar GL/K4 discipline. For
Feferman or Shavrukov style predicates, seriality can remain while the
refutability-introspection component corresponding to A4 fails.

## Research Reading

The thread suggests a "weak APS" layer:

- A1/A2-like monotonicity and seriality behavior may survive.
- A4 becomes a graded or partially failing condition.
- KD, Rosser, and Feferman examples can act as calibrating witnesses.
- The G2 theorem should be decomposed into the exact use of A4, rather than
  stated only as an all-or-nothing APS theorem.

## Next Tasks

- Add a weak-APS vocabulary note: which of A1--A4 are retained, weakened, or
  replaced.
- Record finite algebraic analogues of KD-seriality and A4 failure.
- Compare with Rosser-style predicates in the G2/FG2 hierarchy notes.
- Avoid treating Feferman/Shavrukov predicates as standard APS examples until
  the A4 failure mode is explicitly marked.
