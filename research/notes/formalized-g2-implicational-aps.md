# Formalized G2 in Implicational APS

Source: https://chatgpt.com/share/6a1ac9e4-2f80-8322-8d1a-9da8dce59177

Imported: 2026-05-30

## Core Idea

This thread refines the relation between G2 and FG2 by treating G2 not merely as
the external implication

$$
\boxtimes T\le \bot \Longrightarrow T\le \bot,
$$

but as a family of local or formalized principles inside an APS with implication
or a way to internalize sequents.

Let

$$
d:=\boxtimes T.
$$

The ordinary G2/FG2 contrast becomes:

$$
\mathrm{G2}:\quad d\le \bot\Rightarrow T\le \bot,
$$

$$
\mathrm{FG2}:\quad \boxtimes d\le d.
$$

The discussion proposes that the interval between them should be studied by
localized formalization principles, not only by iterating $\boxtimes$.

## Local Formalized G2

For an APS with implication-like structure, define:

$$
\mathrm{LG2}(a):\quad d\le a \Longrightarrow \boxtimes a\le d.
$$

For a family $\Gamma\subseteq L$:

$$
\mathrm{LG2}(\Gamma):\quad
\forall a\in\Gamma\,(d\le a\Rightarrow \boxtimes a\le d).
$$

If implication satisfies

$$
x\le y \Longleftrightarrow T\le x\to y,
$$

then the same rule can be written as the Horn-style principle:

$$
T\le d\to a \Longrightarrow T\le \boxtimes a\to d.
$$

The thread stresses that this should first be treated as a quasi-equation or
rule. Treating it as the single proposition

$$
T\le (d\to a)\to(\boxtimes a\to d)
$$

would impose a much stronger structure.

## Two Candidate Hierarchies

The APS-only hierarchy is:

$$
\mathrm{FG2}_n:\quad \boxtimes^{n+1}T\le \boxtimes^nT
$$

with ordinary FG2 as $\mathrm{FG2}_1$.

The stronger internal-formalization hierarchy uses intermediate consistency or
resource assumptions $q$:

$$
\mathrm{FG2}\Rightarrow \mathrm{FG2}[q_n]\Rightarrow
\cdots\Rightarrow \mathrm{FG2}[q_0]\Rightarrow \mathrm{FG2}[C]\Rightarrow
\mathrm{G2}.
$$

The useful research distinction is:

- $\boxtimes$-iteration is easy to state in bare APS.
- $q$-indexed or implication-indexed formalization requires additional
  internal syntax, implication, or sequent-object structure.
- The interval between G2 and FG2 may become genuinely strict only after this
  extra internalization layer is made precise.

## Next Tasks

- Decide whether $\mathrm{LG2}(a)$ should be added to the G2-ZOO checker as a
  finite-model predicate.
- Formalize $\mathrm{FG2}[q]$ in the existing order-only APS language or record
  exactly which implication structure it needs.
- Compare $\mathrm{FG2}_n$ with the existing n-FG2 orbit condition in
  [g2-fg2-hierarchy.md](g2-fg2-hierarchy.md).
- Search for finite models separating $\mathrm{LG2}(a)$, $\mathrm{FG2}[q]$, G2,
  and ordinary FG2.
