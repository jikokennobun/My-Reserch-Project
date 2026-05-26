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

Pass 12 found the minimal same-carrier order repair. Adding the single relation
\(\bot\le c\) to `M4-G2FG2FP` makes the order into the diamond
\(\bot<p<T\), \(\bot<c<T\), \(p\parallel c\). The resulting model
`M4-G2FG2FP-order-plus-bot-c-residuated` has a full residuated monoid expansion
with unit \(p\), while preserving the G2+FG2+FP-reachable behavior. The tensor
has \(p\) as unit, \(\bot\) as zero, \(T\otimes T=T\), \(T\otimes c=c\), and
\(c\otimes c=\bot\).

The conceptual reading is now sharper. In `M4-G2FG2FP`, the constant named
\(\bot\) is not initially a least element: \(\bot\le p\) and \(\bot\le T\), but
\(\bot\not\le c\). The repair \(\bot\le c\) is therefore exactly the missing
instance of **bottom discipline**
\[
\forall x,\quad \bot\le x.
\]
Proof-theoretically, this is an ex-falso or absurdity-weakening principle for
the \(c\)-branch. Algebraically, it turns the order into the four-element
Boolean lattice with atoms \(p\) and \(c\), so residual fibers that previously
had no principal maximum can become principal. The repair is therefore not a
random order edge; it is the minimal bounded-order/lattice completion of the M4
witness. The remaining question is whether bottom discipline is intended in the
APS package under study, especially in the BS16 contraction-free setting.

## Next Tasks

- Define "residuated dcpo" carefully.
- Check which residuals are Scott-continuous or preserve meets/joins.
- Compare quantale completion with MacNeille completion.
- Find examples where completion creates a fixed point not present syntactically.
- Connect Galatos-Jipsen-Kowalski-Ono style residuated lattices with APS/G2-ZOO.
- Test bottom discipline against the BS16/resource-sensitive reading: decide
  whether ex-falso weakening is acceptable without reintroducing hidden
  contraction.
- Search whether the \(D_N\) nFG2-depth family admits analogous finite
  residuated repairs.

## Related References and Drive Files

- Galatos, Jipsen, Kowalski, Ono, *Residuated Lattices: An Algebraic Glimpse at Substructural Logics*.
- [algebraic_reverse_math_g2_aps.pdf](https://drive.google.com/file/d/1JoGMqK-9uQqC2Qp3490G2ZJvMj9N5DTe)
- [Incompleteness_Algebraic_Reverse_Mathematics_Thesis_コピー.pdf](https://drive.google.com/file/d/1p1r0-FLjAF9x9d_OvXm1HqgC1xF_NYk_)
- [APS_dissertation.pdf](https://drive.google.com/file/d/1VtS6tSvhUcoIG01fWprIrxGKZ3vZPjxc)
