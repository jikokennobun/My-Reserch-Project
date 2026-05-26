# Residuated Algebra, Domain Theory, and Completion

Source: https://chatgpt.com/share/6a0cbab3-b174-83ab-8a89-db8a746eacda

Imported: 2026-05-22

## Core Idea

\[
\text{residuated algebra}
=
\text{ordered algebra of implication, resource consumption, and weakest preconditions}.
\]

\[
\text{domain theory}
=
\text{order/topology of approximation, limits, and recursive fixed points}.
\]

Their meeting point is:

\[
\text{residuated dcpo / quantale / Scott-continuous residuated structure}.
\]

This is a natural setting for APS because it combines:

- implication and resource sensitivity,
- completion and limits,
- fixed point semantics,
- cut-elimination/completion stability questions.

## Residuated Side

Start with an ordered monoid:

\[
(A,\le,\otimes,e).
\]

Residuals exist when:

\[
a\otimes b\le c
\iff
b\le a\backslash c
\iff
a\le c/b.
\]

For fixed \(a\), the map

\[
L_a(b)=a\otimes b
\]

has right adjoint:

\[
a\backslash -.
\]

This makes implication a weakest-precondition operation.

## Domain-Theoretic Side

In a dcpo or continuous domain, recursive definitions are interpreted by least fixed points of Scott-continuous maps:

\[
\mu F = \bigvee_{n<\omega}F^n(\bot).
\]

The compatibility problem is:

Do \(\otimes,\backslash,/\), \(\Box\), and \(\boxtimes\) preserve directed joins or admit Scott-continuous extensions?

## Candidate Structures

- residuated dcpo
- quantale
- continuous quantale
- domain-enriched residuated lattice
- canonical extension of residuated lattices
- MacNeille completion with residuals

## APS Application

This note supports the broader program:

\[
\text{APS/G2 phenomena}
\quad\text{via}\quad
\text{residuated completions and domain-theoretic fixed points}.
\]

It connects directly to:

- BS16 cut elimination as completion stability.
- Analytic APS as topological/domain-theoretic APS.
- Completion-generated fixed points versus syntactic fixed points.

## Finite Search Result: M4 Obstruction

The non-degenerate finite G2+FG2+FP witness `M4-G2FG2FP` cannot be expanded to a
full residuated ordered monoid on its existing carrier and order. The exhaustive
search report
[../outputs/residuated-search-M4-G2FG2FP.json](../outputs/residuated-search-M4-G2FG2FP.json)
checks every binary tensor with each possible unit and finds no operation that
is associative, monotone, and admits both residuals.

This is a useful obstruction rather than a failure of the program. It says that
the current 4-element witness is genuinely a sparse preAPS artifact. A
residuated G2+FG2+FP witness likely requires at least one of:

- adding new order elements so residual downsets become principal;
- changing the underlying order while preserving the G2/FG2/FP behavior;
- weakening to one-sided or partial residuals;
- searching in a different finite family.

## Next Tasks

- Define "residuated dcpo" carefully.
- Check which residuals are Scott-continuous or preserve meets/joins.
- Compare quantale completion with MacNeille completion.
- Find examples where completion creates a fixed point not present syntactically.
- Connect Galatos-Jipsen-Kowalski-Ono style residuated lattices with APS/G2-ZOO.
- Search for the smallest full-residuated expansion or replacement of
  `M4-G2FG2FP`.

## Related References and Drive Files

- Galatos, Jipsen, Kowalski, Ono, *Residuated Lattices: An Algebraic Glimpse at Substructural Logics*.
- [algebraic_reverse_math_g2_aps.pdf](https://drive.google.com/file/d/1JoGMqK-9uQqC2Qp3490G2ZJvMj9N5DTe)
- [Incompleteness_Algebraic_Reverse_Mathematics_Thesis_コピー.pdf](https://drive.google.com/file/d/1p1r0-FLjAF9x9d_OvXm1HqgC1xF_NYk_)
- [APS_dissertation.pdf](https://drive.google.com/file/d/1VtS6tSvhUcoIG01fWprIrxGKZ3vZPjxc)
