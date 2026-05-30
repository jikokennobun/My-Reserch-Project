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

The first import was intentionally short. The mathematical point of the Project
thread is sharper: nonstandard provability predicates should be used as a
calibration scale for weakened APS axioms. They are not merely failures of the
standard theorem; they mark which exact derivability or introspection
conditions are doing the work.

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

## Derivability Conditions as APS Conditions

Let $Pr(x)$ be a provability predicate for a background theory $T$. The usual
Hilbert-Bernays-Löb style conditions can be read as algebraic constraints:

1. monotonicity or necessitation-like behavior:

   $$
   T\vdash \varphi\to\psi
   \Rightarrow
   T\vdash Pr(\ulcorner\varphi\urcorner)\to Pr(\ulcorner\psi\urcorner);
   $$

2. closure of provability under modus ponens;
3. positive introspection:

   $$
   T\vdash Pr(\ulcorner\varphi\urcorner)
   \to
   Pr(\ulcorner Pr(\ulcorner\varphi\urcorner)\urcorner).
   $$

In APS language, the $\Box$-part of A1 reflects monotonicity of provability,
while the $\boxtimes$-part of A1 reflects antitonicity of refutability:

$$
[\varphi]\le[\psi]
\Rightarrow
\boxtimes[\psi]\le\boxtimes[\varphi].
$$

A4 says:

$$
\boxtimes x\le \Box\boxtimes x.
$$

Under the Lindenbaum reading this is a refutability-introspection principle:

$$
Pr(\ulcorner\neg\varphi\urcorner)
\Rightarrow
Pr(\ulcorner Pr(\ulcorner\neg\varphi\urcorner)\urcorner).
$$

Thus A4 is not a harmless modal ornament. It encodes that refutability claims
are themselves provably recognized.

## Weak APS Packages

Define a weak APS package by specifying which APS conditions are retained.
Useful candidates are:

### Serial Weak APS

Retain A1 and A2, but do not assume A4:

$$
\mathrm{wAPS}_{D}:=\mathrm{A1}+\mathrm{A2}.
$$

This is the natural algebraic home for KD-like behavior. A2,

$$
T\le\boxtimes\bot,
$$

acts like a seriality or consistency-style axiom: the absurdity $\bot$ is
refutable from the standpoint of $T$.

### A3-Weak APS

Retain A1, A2, and A3, but not A4:

$$
\mathrm{wAPS}_{A3}:=\mathrm{A1}+\mathrm{A2}+\mathrm{A3}.
$$

A3 still expresses incompatibility between provability and refutability:

$$
x\le\Box y,\ x\le\boxtimes y
\Rightarrow x\le\boxtimes T.
$$

This package can still reason about collision of proof and refutation, but it
does not know that refutation is provably recognizable.

### A4-Graded APS

Instead of assuming full A4 for all $x$, record the set

$$
\mathrm{A4Profile}(S)=
\{x\in L:\boxtimes x\le\Box\boxtimes x\}.
$$

This lets Feferman/Shavrukov/Rosser-like examples be treated as partial APS
rather than discarded as failures.

## Exact Use in the G2 Argument

The standard Beklemishev-Shamkanov route has two stages:

1. obtain a Jeroslow-style fixed point:

   $$
   p={}_S\boxtimes p;
   $$

2. use APS axioms to derive G2 and FG2.

The fixed-point existence itself is not an APS axiom. It comes from syntax,
diagonalization, or sequentiality. The APS part then uses A1--A4 to convert
that fixed point into G2/FG2.

The weak-APS project asks:

- Which part of G2 survives under A1+A2 only?
- Which part needs A3?
- Which step needs A4?
- Can Rosser-style predicates satisfy enough of the argument to yield a
  Rosser-G2 but not FG2?

This is a more precise research program than merely saying that nonstandard
provability predicates do not fit APS.

## Finite Algebraic Calibration

For a finite preAPS model $S$, compute:

$$
\mathrm{A4Profile}(S)=
\{x:\boxtimes x\le\Box\boxtimes x\}.
$$

Also compute:

$$
\mathrm{G2}(S),\quad
\mathrm{FG2}(S),\quad
\mathrm{FP}_{\mathrm{synt}}(S).
$$

Then classify models by:

- A4 full / partial / empty;
- G2 true or false;
- FG2 true or false;
- syntactic fixed point present or absent.

This will produce finite analogues of:

$$
\text{GL-like}\quad\text{versus}\quad\text{KD/Rosser/Feferman-like}
$$

behavior.

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
- Extend `check-g2-zoo.py` with an `A4Profile` or weak-APS report.
