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

The original import was intentionally a safe index, not a finished research
note. A more faithful mathematical reading is that the Project discussion
separates three different ways of filling the gap between G2 and FG2:

1. an APS-internal $\boxtimes$-iteration hierarchy;
2. a local Horn-rule hierarchy $\mathrm{LG2}(a)$;
3. an implication- or consistency-parameterized hierarchy
   $\mathrm{FG2}[q]$.

These should not be collapsed into one notion. They require different amounts
of structure and support different finite-model questions.

## Background: APS Fragment Used Here

Let

$$
S=(L,\le,T,\bot,\Box,\boxtimes)
$$

be an APS or pre-APS. The order $x\le y$ is read as abstract derivability from
$x$ to $y$. The operator $\Box$ represents provability and $\boxtimes$
represents refutability. The relevant axioms are:

$$
\mathrm{A1}:\quad
x\le y\Rightarrow \Box x\le \Box y
\quad\text{and}\quad
\boxtimes y\le \boxtimes x,
$$

$$
\mathrm{A2}:\quad T\le \boxtimes\bot,
$$

$$
\mathrm{A3}:\quad
x\le \Box y,\ x\le \boxtimes y
\Rightarrow x\le \boxtimes T,
$$

$$
\mathrm{A4}:\quad
\boxtimes x\le \Box\boxtimes x.
$$

The present note does not assume that $T$ is greatest or that $\bot$ is least
unless explicitly stated. This matters because many finite G2-ZOO examples are
sparse preorders where top/bottom discipline is deliberately not automatic.

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

## Basic Lemmas

### Lemma 1: FG2 Implies G2 Under A1 and A2

Assume A1 and A2. If

$$
\mathrm{FG2}:\quad \boxtimes\boxtimes T\le \boxtimes T
$$

holds, then

$$
\mathrm{G2}:\quad \boxtimes T\le \bot\Rightarrow T\le \bot
$$

holds.

Proof. Put $d=\boxtimes T$. Suppose $d\le\bot$. By antitonicity in A1,

$$
\boxtimes\bot\le \boxtimes d.
$$

By A2, $T\le\boxtimes\bot$. By FG2,
$\boxtimes d=\boxtimes\boxtimes T\le d$. Therefore

$$
T\le\boxtimes\bot\le \boxtimes d\le d\le\bot.
$$

This proves G2. Notice that A3 and A4 are not needed for this implication once
FG2 is given.

### Lemma 2: $\mathrm{LG2}(\bot)$ Implies G2 Under A2

Assume A2. If

$$
\mathrm{LG2}(\bot):\quad d\le\bot\Rightarrow \boxtimes\bot\le d
$$

holds, then G2 holds.

Proof. If $d\le\bot$, then $\mathrm{LG2}(\bot)$ gives $\boxtimes\bot\le d$.
Together with A2:

$$
T\le\boxtimes\bot\le d\le\bot.
$$

Thus $T\le\bot$.

This lemma explains why the local principle is genuinely intermediate: it can
imply ordinary G2 at the particular test object $\bot$, but it does not by
itself assert full FG2.

### Lemma 3: FG2 Gives a Family of Local Instances

If FG2 holds and $d\le a$, then antitonicity gives $\boxtimes a\le\boxtimes d$,
and FG2 gives $\boxtimes d\le d$. Hence

$$
d\le a\Rightarrow \boxtimes a\le d.
$$

Thus FG2 implies $\mathrm{LG2}(a)$ for every $a\in L$. Consequently:

$$
\mathrm{FG2}
\Rightarrow
\forall a\,\mathrm{LG2}(a)
\Rightarrow
\mathrm{LG2}(\bot)
\Rightarrow
\mathrm{G2}.
$$

The strictness of these implications is a finite-model problem.

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

## Implication-Parameterized Reading

The thread also suggests that a more refined hierarchy should use intermediate
assumptions $q$ between a consistency-like element $C$ and $T$. A cautious
template is:

$$
C\le q_0\le q_1\le\cdots\le q_n\le T.
$$

The intended reading is that $\mathrm{FG2}[q]$ formalizes G2 relative to the
amount of consistency/resource encoded by $q$. The thread's slogan chain is:

$$
\mathrm{FG2}
\Rightarrow
\mathrm{FG2}[q_n]
\Rightarrow\cdots\Rightarrow
\mathrm{FG2}[q_0]
\Rightarrow
\mathrm{FG2}[C]
\Rightarrow
\mathrm{G2}.
$$

This should be treated as a program, not yet as a theorem in the current
repository. To make it precise, the following data are needed:

1. a distinguished consistency element $C$;
2. an implication or internal sequent object;
3. a formal definition of $\mathrm{FG2}[q]$;
4. proof obligations showing monotonicity in $q$;
5. finite or syntactic examples separating adjacent levels.

Without this additional structure, the only fully order-theoretic hierarchy
currently available is the $\boxtimes$-iteration hierarchy.

## Finite-Model Test Plan

For each finite APS/preAPS model in `code/models/`, compute:

$$
d=\boxtimes T,
$$

then for every $a\in L$ test:

$$
\mathrm{LG2}(a)
\Longleftrightarrow
d\nleq a\ \text{or}\ \boxtimes a\le d.
$$

This gives a profile:

$$
\mathrm{LG2Profile}(S)=
\{a\in L:\mathrm{LG2}(a)\}.
$$

Natural invariants include:

- whether $\bot\in\mathrm{LG2Profile}(S)$;
- whether $\mathrm{LG2Profile}(S)=L$;
- whether G2 holds without $\mathrm{LG2}(\bot)$;
- whether $\mathrm{LG2Profile}$ is upward or downward closed;
- how $\mathrm{LG2Profile}$ changes under bottom-discipline enforcement and
  residuated expansion.

This is the direct computational bridge from the Project discussion into the
G2-ZOO checker.
