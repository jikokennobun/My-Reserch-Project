# APS from Arithmetic / Realization Kernel

Source: https://chatgpt.com/share/6a023ac5-ad64-83e8-93af-d2ba789ca554

Imported from Research Project handoff: 2026-05-22

## Topic

APS from arithmetic, intensional equivalence, and realization kernels.

## Working Summary

This note should explain how an APS can be extracted from arithmetical syntax or realizability: formulas are identified by an intensional equivalence or realization kernel rather than by plain extensional truth.

## Detailed Reconstruction

The Project discussion frames the issue as an abstract arithmetic completeness
problem. Given a modal or APS logic $L$, one can define two maps:

$$
\mathrm{Prov}(L)
=
\{Pr_T(x):Pr_T\text{ arithmetically satisfies the principles of }L\},
$$

and for a class $\mathcal C$ of provability predicates:

$$
\mathrm{Log}(\mathcal C)
=
\bigcap_{Pr_T\in\mathcal C}PL(Pr_T).
$$

Then:

$$
L\subseteq \mathrm{Log}(\mathrm{Prov}(L))
$$

is the soundness direction. The hard direction is completeness:

$$
L=\mathrm{Log}(\mathrm{Prov}(L)).
$$

The thread proposes an APS analogue of this problem.

## Realization Kernels

Let

$$
f:\mathrm{MFm}\to\mathrm{ArithFm}
$$

be a realization from modal/APS formulas to arithmetic formulas, preserving
some operations such as $\Box$, $\boxtimes$, $T$, and $\bot$. The soundness
direction is:

$$
L\vdash \varphi
\Rightarrow
T\vdash f(\varphi).
$$

The reverse direction is not automatic:

$$
T\vdash f(\varphi)
\nRightarrow
L\vdash\varphi.
$$

The obstruction is that $f$ can collapse intensional distinctions. Two
different modal formulas may have arithmetically equivalent realizations:

$$
T\vdash f(\varphi)\leftrightarrow f(\psi),
$$

without $L$ proving:

$$
L\vdash \varphi\leftrightarrow\psi.
$$

Define the realization kernel:

$$
\ker_T(f)=
\{(\varphi,\psi):T\vdash f(\varphi)\leftrightarrow f(\psi)\}.
$$

The realization is faithful over $L$ when:

$$
(\varphi,\psi)\in\ker_T(f)
\Rightarrow
L\vdash\varphi\leftrightarrow\psi.
$$

This is the missing condition behind many attempted reverse implications.

## Rule Versus Theorem

The conversation emphasizes a distinction between theorem inclusion and rule
reflection. A statement such as

$$
L\subseteq PL(Pr_T)
$$

usually means that every theorem of $L$ is arithmetically valid under $Pr_T$.
It does not automatically mean that every rule of $L$ is reflected uniformly
inside arithmetic.

For example, an equivalence rule:

$$
\frac{A\leftrightarrow B}{\Box A\leftrightarrow\Box B}
$$

requires a uniform internal principle:

$$
T\vdash A\leftrightarrow B
\Rightarrow
T\vdash Pr_T(\ulcorner A\urcorner)\leftrightarrow Pr_T(\ulcorner B\urcorner).
$$

Individual arithmetic coincidences do not prove such a uniform rule.

## Reflection Spectrum

The thread proposes classifying provability predicates by reflection-collapse
profiles:

$$
RS(Pr_T)=
\{(n,m):T\vdash \Box^n\varphi\to\Box^m\varphi
\text{ uniformly in }\varphi\}.
$$

This gives an arithmetic analogue of orbit-collapse invariants already used in
the finite G2-ZOO.

## APS Extraction Problem

Given arithmetic syntax and a provability/refutability pair, construct:

$$
L_S,\quad \le_S,\quad \Box,\quad \boxtimes
$$

by quotienting formulas not by truth, but by a chosen intensional equivalence.
The central question is which quotient is appropriate:

- provable equivalence in $T$;
- equality under a realization kernel;
- equivalence preserving $\Box$ and $\boxtimes$;
- a finer syntactic congruence preserving fixed-point data.

The choice determines whether fixed points and G2 principles reflect back from
arithmetic to APS.

## Next Tasks

- Extract the proposed construction of $L_S$, $\le_S$, $\Box$, and $\boxtimes$.
- Clarify what "intensional equivalence" means in this setting.
- Relate realization kernels to definability and fixed point reflection.
