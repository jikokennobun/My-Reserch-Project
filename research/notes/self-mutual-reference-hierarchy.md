# Self and Mutual Reference Hierarchy

Source: https://chatgpt.com/share/69fcbd5f-d1c0-83e8-a682-187480ed5d1f

Imported from Research Project handoff: 2026-05-22

Access note: local relay logs identify this share as `Self-reference and mutual
reference`. The reconstruction below keeps the mathematical distinctions from
that Project line: single self-reference, mutual reference, networked
reference, and their APS fixed-point shadows.

## Abstract

Ordinary diagonalization gives one formula that refers to itself. APS records
one shadow of this phenomenon as a syntactic refutability fixed point:

$$
p=\boxtimes p.
$$

The Project discussion asks for a hierarchy that also includes mutually
referential pairs, finite cycles, and graph-shaped systems of reference. This
is not merely a linguistic generalization. In APS, a 2-cycle under
$\boxtimes$ can behave like a fixed point of $\boxtimes^2$ without being a
fixed point of $\boxtimes$. Thus mutual reference is a natural semantic home
for the gap between fixed points, FG2, and the nFG2 hierarchy.

## Background

Let formulas be quotiented by a chosen sameness relation $=_S$, usually
provable equivalence, syntactic equality in a finite model, or equality in a
preorder skeleton. A unary reference operation is written:

$$
F:X\to X.
$$

A self-referential point is:

$$
p=_S F(p).
$$

For APS, the central example is:

$$
F=\boxtimes,
\qquad
p=_S\boxtimes p.
$$

This is the Jeroslow/refutability fixed-point pattern. It must be kept distinct
from the Godel pattern:

$$
p=_S\neg\Box p,
$$

unless $\boxtimes$ is explicitly defined as $\neg\Box$.

## Single Self-Reference

### Definition 1: Self-Reference Instance

A self-reference instance over $(X,=_S)$ is a pair $(F,p)$ such that:

$$
F:X\to X,
\qquad
p=_S F(p).
$$

The class of fixed points of $F$ is:

$$
\mathrm{Fix}_S(F)=\{p\in X:p=_S F(p)\}.
$$

The corresponding cardinal invariant is:

$$
\mathrm{cardFix}_S(F)=|\mathrm{Fix}_S(F)/{=_S}|.
$$

This invariant is crude but useful: it separates absence of self-reference,
unique self-reference, and multiple inequivalent diagonal points.

### APS Reading

For $S=(L,\le,\Box,\boxtimes,T,\bot)$:

$$
\mathrm{Fix}_S(\boxtimes)
=
\{p\in L:p=\boxtimes p\}.
$$

The existence of such a $p$ is `FP-synt` in
`g2-aps-zoo-classification.md`.

## Mutual Reference

### Definition 2: Mutual Pair

A mutual-reference pair consists of two spaces $X,Y$, two maps:

$$
F:Y\to X,
\qquad
G:X\to Y,
$$

and points $(p,q)\in X\times Y$ satisfying:

$$
p=_S F(q),
\qquad
q=_S G(p).
$$

When $X=Y$ and $F=G=\boxtimes$, this becomes a 2-cycle:

$$
p=\boxtimes q,
\qquad
q=\boxtimes p.
$$

If $p\ne q$, the system has mutual reference without single self-reference.

### Lemma 1: Mutual Reference Gives Composite Fixed Points

If $(p,q)$ is a mutual pair for $F:Y\to X$ and $G:X\to Y$, then:

$$
p=_S F(G(p)),
\qquad
q=_S G(F(q)).
$$

Thus $p$ is a fixed point of $F\circ G$ and $q$ is a fixed point of $G\circ F$.

Proof. Substitute $q=_S G(p)$ into $p=_S F(q)$, and similarly substitute
$p=_S F(q)$ into $q=_S G(p)$.

### APS Consequence

For an antitone $\boxtimes$, the composite:

$$
\boxtimes^2:L\to L
$$

is monotone. A mutual pair for $\boxtimes$ is an ordinary fixed point of
$\boxtimes^2$. Therefore the hierarchy:

$$
\mathrm{Fix}(\boxtimes)
\subseteq
\mathrm{Fix}(\boxtimes^2)
$$

is a precise mathematical place where self-reference and mutual reference can
separate.

In finite ZOO models with alternating $\boxtimes$-orbits, a two-cycle can
produce stable even dynamics while blocking a genuine $\boxtimes$-fixed point.

## Networked Reference

### Definition 3: Reference Graph

Let $G=(V,E)$ be a finite directed graph. A graph-shaped reference system over
a family of spaces $(X_v)_{v\in V}$ assigns to each vertex $v$ a map:

$$
F_v:\prod_{u\to v}X_u\to X_v.
$$

A network fixed point is a tuple:

$$
p=(p_v)_{v\in V}\in\prod_{v\in V}X_v
$$

such that for every vertex $v$:

$$
p_v=_S F_v((p_u)_{u\to v}).
$$

This recovers:

- ordinary self-reference when $G$ has one vertex with one loop;
- mutual reference when $G$ is a directed 2-cycle;
- simultaneous diagonalization when $G$ is a complete dependency graph;
- parameterized diagonalization when some vertices are treated as external
  parameters.

### Definition 4: Reference Rank

The reference rank of a system is the least size of a directed graph needed to
represent it up to the chosen equivalence $=_S$:

$$
\rho(F)=
\min\{|V(G)|:F\ \text{is represented by a }G\text{-network}\}.
$$

This is intended as a coarse invariant. One may refine it by cycle length,
treewidth, number of strongly connected components, or definability class of
the maps $F_v$.

## Hierarchy

The hierarchy suggested by the Project discussion is:

$$
\text{single self-reference}
\subseteq
\text{mutual reference}
\subseteq
\text{finite network reference}
\subseteq
\text{parameterized/indexed reference}.
$$

In APS terms this corresponds to:

$$
\mathrm{Fix}(\boxtimes)
\subseteq
\mathrm{Fix}(\boxtimes^2)
\subseteq
\bigcup_{n\ge 1}\mathrm{Fix}(\boxtimes^n)
\subseteq
\text{indexed/fibred fixed-point systems}.
$$

The inclusions should not be assumed strict in every semantics. Strictness is a
model-theoretic question.

## Separation Questions

### Question 1: Mutual Without Self

Find a finite preAPS with:

$$
\mathrm{Fix}(\boxtimes)=\varnothing,
\qquad
\mathrm{Fix}(\boxtimes^2)\ne\varnothing.
$$

This is the cleanest finite witness that mutual reference is strictly weaker
than single self-reference.

### Question 2: FG2 Without Fixed Point

FG2 says:

$$
\boxtimes^2T\le\boxtimes T.
$$

It does not say:

$$
\boxtimes T=\boxtimes^2T.
$$

Thus FG2 can hold because the order compares two orbit points, not because a
fixed point exists. The ZOO already has examples of G2+FG2 without syntactic
fixed point. The mutual-reference task is to explain this in terms of orbit
shape and cycle structure.

### Question 3: Network Reference and nFG2

If the orbit:

$$
T,\boxtimes T,\boxtimes^2T,\ldots
$$

has eventual period $m$, then $\boxtimes^m$ has a fixed point on the orbit.
The nFG2 pattern records order comparisons along this orbit:

$$
\boxtimes^{k+1}T\le\boxtimes^kT.
$$

The problem is to classify which eventual periods and order orientations
produce each nFG2 truth pattern.

## Relation to Diagonalization

Classical diagonalization produces fixed points for unary formula operators.
Mutual reference requires either:

1. simultaneous diagonalization;
2. parameterized fixed-point lemmas;
3. a categorical fixed-point theorem applied to products;
4. a graph-level substitution calculus.

For a two-variable predicate $\Phi(x,y)$, a mutual pair asks for sentences
$P,Q$ such that:

$$
P\leftrightarrow \Phi(\ulcorner P\urcorner,\ulcorner Q\urcorner),
$$

and:

$$
Q\leftrightarrow \Psi(\ulcorner P\urcorner,\ulcorner Q\urcorner).
$$

In categorical notation this is not merely the ordinary diagonal
$X\to X\times X$; it also needs quotation, substitution, and reindexing. See
`smullyan-lawvere-categorical-diagonalization.md`.

## Conjectures

### Conjecture 1: Periodic Reference Spectrum

For finite preAPS models, the hierarchy of reference strengths is captured by
the eventual cycle structure of the $\boxtimes$-action together with the order
relations along the orbit of $T$.

The data to record is:

$$
\left(
\mathrm{period}(T),
\mathrm{preperiod}(T),
\{\boxtimes^{k+1}T\le\boxtimes^kT:k\ge 1\}
\right).
$$

### Conjecture 2: Mutual Reference Does Not Imply FG2

There should be finite models with a nontrivial $\boxtimes^2$-fixed point but
failure of FG2 at $T$. The fixed point may live away from the $T$-orbit, or the
order along the $T$-orbit may point the wrong way.

### Conjecture 3: Network Reference Is Naturally Indexed

A graph-shaped reference system is best represented as an indexed APS over the
category of finite dependency graphs. Reindexing along graph morphisms should
model forgetting variables, duplicating variables, or merging reference nodes.

## Relation to Existing Notes

- `self-existence-sentences.md` treats self-existence and diagonal sentences.
  This note generalizes the fixed-point target from one sentence to systems.
- `g2-fg2-hierarchy.md` supplies the orbit and nFG2 analysis needed for finite
  $\boxtimes$-dynamics.
- `indexed-aps-fibred-algebra.md` supplies the categorical environment for
  parameterized and graph-indexed reference.
- `smullyan-lawvere-categorical-diagonalization.md` gives the substitution and
  quotation machinery needed to construct such systems.

## Verification Tasks

1. Add checker output for $\mathrm{Fix}(\boxtimes^n)$ for small $n$, not only
   $\mathrm{Fix}(\boxtimes)$.
2. Compute the period and preperiod of the $T$-orbit for every finite ZOO model.
3. Search for finite models separating:
   - $\mathrm{Fix}(\boxtimes)$ from $\mathrm{Fix}(\boxtimes^2)$;
   - mutual reference from FG2;
   - all-level nFG2 from syntactic fixed-point existence away from the
     $T$-orbit.
4. Formalize graph-shaped reference systems as an indexed APS construction.
5. Re-export the source share and insert any missing examples or terminology
   from the original Project discussion.
