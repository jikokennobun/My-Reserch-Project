# Self and Mutual Reference Hierarchy

Source: https://chatgpt.com/share/69fcbd5f-d1c0-83e8-a682-187480ed5d1f

Imported from Research Project handoff: 2026-05-22

Access note: local relay logs identify this share as `Self-reference and mutual
reference`. The reconstruction below keeps the mathematical distinctions from
that Project line: single self-reference, mutual reference, networked
reference, and their APS fixed-point shadows.

Relay update on 2026-06-12:

- A new Drive artifact, `ams_aps_self_reference_hierarchy.pdf`
  (`ChatGPT_Research`, created `2026-06-12T19:30:42Z`), gives a durable
  long-form reconstruction of the same line.
- Two later 2026-06-12 supplements sharpen different parts of the same axis:
  `相互不動点階層_反例モデル.pdf` gives a strict `FP_n`-hierarchy countermodel
  program, while Claude's `selfref_mutref.pdf` isolates the `SR` versus
  `MR_2` separation through a finite APS witness `M_5` and a Lopez-style
  product fixed-point obstruction.
- The supplement is broader than the original handoff note: it places mutual
  reference inside a full incompleteness hierarchy running from tautological
  validity up to full self-reference.
- The additions below mark content that is now directly supported by the Drive
  PDF rather than only inferred from the old share title and thin handoff.

Relay update on 2026-06-13:

- A second Drive artifact, `selfref_mutref.pdf`
  (`ChatGPT_Research`, created `2026-06-12T07:23:11Z`), gives a more focused
  separation result for self-reference versus mutual reference.
- The additions below marked with `MR`/`SR` are reconstructed from that newer
  supplement rather than from the original share snapshot.

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

### Proposition 1A: Mutual Reference Collapses to Self-Reference Under Weakening

Let the definable operations form a clone, so projections and weakening are
available. Then:

$$
\mathrm{MR}_{2}\Longrightarrow \mathrm{SR},
$$

and more generally:

$$
\mathrm{MR}_{n+1}\Longrightarrow \mathrm{MR}_{n}.
$$

Proof sketch. Given a unary operator $f$, define:

$$
F(p,q)=f(q),
\qquad
G(p,q)=f(q).
$$

These are definable from $f$ by ignoring the first variable. A mutual pair for
$F,G$ gives:

$$
p=_S f(q),
\qquad
q=_S f(q),
$$

so $q$ is an ordinary fixed point of $f$. The $(n+1)\to n$ reduction is the
same padding argument with a dummy coordinate.

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

### Proposition 2A: Pure Unary Signatures Force SR and MR to Coincide

Assume every definable $n$-ary operation is generated from unary operators,
constants, and composition alone. Then:

$$
\mathrm{SR}\Longleftrightarrow \mathrm{MR}.
$$

Proof sketch. The implication $\mathrm{MR}\Rightarrow\mathrm{SR}$ is
Proposition 1A. Conversely, in a pure unary signature every defining term
depends on at most one coordinate, so a simultaneous system

$$
p_i=_S F_i(p_1,\dots,p_n)
$$

decomposes into unary chains and constants. Each strongly connected component
therefore reduces to an ordinary unary fixed-point problem, which SR solves.

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

## Stronger Hierarchy from the 2026-06-12 Drive Supplement

The Drive supplement makes the intended hierarchy substantially more explicit.
Besides self-reference, mutual reference, and network reference, it introduces
intermediate principles for periodicity, cardinality of fixed points,
computable closure stages, continuous spectra, and code-space diagonalization.

Write:

$$
\mathrm{FSR}(S):
\quad
\forall F\in \mathrm{Def}_1(S)\ \exists p\in S\ (p =_S F(p)).
$$

For mutual-reference of arity $n$, write informally:

$$
\mathrm{MR}_n(S):
\quad
\exists (p_0,\dots,p_{n-1})
\ \forall i<n\
p_i =_S F_i(p_{i+1 \bmod n}).
$$

The supplement's organizing chain is:

$$
\mathrm{FSR}
\Longrightarrow
\mathrm{MR}_\omega
\Longrightarrow
\mathrm{MR}_{<\omega}
\Longrightarrow
\mathrm{SR}(C)
\Longrightarrow
J
\Longrightarrow
\mathrm{FG2}
\Longrightarrow
\mathrm{G2}
\Longrightarrow
\mathrm{Taut}.
$$

Here:

- $\mathrm{SR}(C)$ is self-reference restricted to a chosen class of operators
  $C$;
- $J$ is the Jeroslow/refutability fixed-point principle
  $\exists p\,(p =_S \boxtimes p)$;
- `Taut` is the tautological or purely structural bottom layer.

The forward implications are intended as strength inclusions, not equivalences.
The supplement repeatedly stresses that most reverse implications fail without
extra coding, pairing, or continuity assumptions.

### Proposition 1: Mutual Reference Sits Strictly Above Single Fixed-Point Data

The implication

$$
\mathrm{Fix}_S(\boxtimes)\subseteq \mathrm{Fix}_S(\boxtimes^2)
$$

records only the unary shadow of mutual reference. A genuine mutual-reference
principle remembers ordered pairs, dependency shape, and the distinction
between primitive $\boxtimes$-fixed points and periodic $\boxtimes$-orbits.

Proof sketch. A primitive fixed point $p=\boxtimes p$ gives the degenerate pair
$(p,p)$. But a nontrivial pair $(p,q)$ with
$p=\boxtimes q,\ q=\boxtimes p,\ p\neq q$ determines an orbit of period two,
not a unary fixed point of $\boxtimes$. It is only after passage to
$\boxtimes^2$ that the pair collapses to ordinary fixed-point data.

## Periodic and Orbit Hierarchies

The Drive supplement treats periodic self-reference as a separate axis rather
than a minor variant of the single-point case. For $n\ge 1$, define:

$$
\mathrm{Per}_n(S):
\quad
\exists p\in S\ (\boxtimes^n p =_S p).
$$

The $n=1$ case is exactly the Jeroslow fixed-point principle. For $n>1$ one
gets periodic reference without primitive self-reference. This is the natural
semantic home for even-cycle ZOO models and for the repository's `nFG2` line.

### Proposition 2: Periodic Reference Need Not Collapse to Jeroslow Reference

There are finite preAPS candidates where:

$$
\mathrm{Per}_2(S)\ \text{holds},\qquad
\mathrm{Per}_1(S)\ \text{fails}.
$$

Proof sketch. Any finite model with a genuine two-cycle
$p\mapsto q\mapsto p$ under $\boxtimes$ and no fixed point yields such a
separation. The supplement treats this as a core reason to track cycle length
and not merely existence of one fixed point.

The associated orbit spectrum is:

$$
\mathrm{Spec}_{\boxtimes}(S)
:=
\{n\ge 1:\mathrm{Per}_n(S)\}.
$$

This suggests refining the old reference-rank invariant by eventual period,
preperiod, and location relative to the orbit of $T$.

## Cardinal and Closure-Ordinal Layers

The Drive supplement also isolates two further axes that were only implicit in
the original handoff note.

### Fixed-Point Cardinal Layer

Instead of asking only whether $\mathrm{Fix}_S(\boxtimes)$ is empty, ask for
its size:

$$
\mathrm{Fix}_{\ge \kappa}(S):
\quad
|\mathrm{Fix}_S(\boxtimes)/{=_S}|\ge \kappa.
$$

This covers star-like or branching APS models with many inequivalent detached
fixed points and links directly to the repository's G2-ZOO/cardinal-invariant
line.

### Closure-Ordinal Layer

Let $F:S\to S$ be monotone or antitone and form its transfinite closure tower
from a seed $x_0$:

$$
x_{\alpha+1}=F(x_\alpha),
\qquad
x_\lambda=\sup_{\beta<\lambda}x_\beta
\ \text{when defined}.
$$

The least ordinal at which stabilization occurs is the closure ordinal:

$$
\operatorname{clOrd}_F(x_0)
:=
\min\{\alpha:x_{\alpha+1}=x_\alpha\}.
$$

The supplement treats delayed stabilization and doubled-ordinal constructions
as evidence that "eventual self-reference" has a genuine ordinal hierarchy, not
just a finite cycle hierarchy.

## Finite Counterexample Program from the Supplement

The Drive PDF organizes several now-familiar repository examples into one
single separation table. The key patterns are:

- a two-point inversion APS witnessing that APS axioms alone do not force a
  fixed point;
- a three-point chain or lock model witnessing that G2 can hold while FG2 and
  primitive fixed points fail;
- A3-dropping countermodels showing that a fixed point need not yield FG2
  without the horizontal intersection principle;
- star-like models with arbitrarily many detached fixed points;
- periodic/cycle models realizing nontrivial $\mathrm{Per}_n$ behavior.

### Proposition 3: The Mutual-Reference Line Is a Finite-Model Search Program

The supplement reframes the hierarchy as a search problem over small models:
find finite preAPS or APS witnesses separating

$$
\mathrm{Per}_1,\ \mathrm{Per}_2,\ \mathrm{MR}_n,\ \mathrm{FG2},\ \mathrm{G2},
\ \mathrm{Fix}_{\ge \kappa}.
$$

Proof sketch. Each implication in the hierarchy becomes meaningful only when a
countermodel separates it from the next stronger principle. The supplement's
examples and tables are explicitly arranged as such separation witnesses rather
than only as motivational anecdotes.

## Continuous and Code-Space Layers

The Drive supplement broadens the note beyond finite combinatorics.

### Continuous / Topological Layer

It treats continuous interval models, domain-theoretic fixed-point principles,
and periodic spectra of continuous operators as an intermediate region between
finite combinatorial APS and full syntactic diagonalization.

The point is not that continuity gives full self-reference. Rather:

$$
\text{continuous fixed-point principle}
\not\Rightarrow
\mathrm{FSR},
$$

even though it may force nontrivial fixed points for restricted operator
classes.

### Lawvere-Smullyan / Code-Space Layer

The supplement also locates mutual and full self-reference in a code-space
environment: quotation, substitution, pairing, repeat/diagonal operators, and
weak point-surjectivity.

This suggests the refined implication:

$$
\text{weak point-surjectivity / code space}
\Longrightarrow
\mathrm{SR}(C),
$$

with full FSR appearing when the class $C$ is rich enough to represent all
definable unary operators.

### Product-Fixed-Point Reading of the Separation

The focused `selfref_mutref.pdf` supplement recasts the same issue in
topological/order-theoretic language. A space or poset may have the unary
fixed-point property needed for SR while its square fails the corresponding
product fixed-point property, which blocks MR2.

In that reading:

$$
\mathrm{SR}\ \text{corresponds to FPP on the base space},
$$

while:

$$
\mathrm{MR}_2\ \text{corresponds to FPP on the square}.
$$

So `SR /\ not MR_2` becomes a product-instability phenomenon rather than a
mere syntactic accident.

### Strict Finite-Variable Hierarchy

The companion countermodel supplement `相互不動点階層_反例モデル.pdf` strengthens
the hierarchy in a different direction. It does not only separate unary from
binary reference. It claims that for every `r >= 2` there are computable
infinite AMS/APS models satisfying

$$
\mathrm{FP}_1,\dots,\mathrm{FP}_{r-1}
\qquad\text{but not}\qquad
\mathrm{FP}_r,
$$

where `FP_n` means existence of simultaneous fixed points for every definable
`n`-variable system. In that reading the descending chain

$$
\mathrm{FP}_{<\omega}
\Rightarrow
\cdots
\Rightarrow
\mathrm{FP}_{n+1}
\Rightarrow
\mathrm{FP}_n
\Rightarrow
\cdots
\Rightarrow
\mathrm{FP}_2
\Rightarrow
\mathrm{FP}_1
$$

is strict at every stage over suitable AMS/APS classes.

The proposed mechanism is combinatorial rather than modal: a regular
non-well-founded tree model can be built so that cycles of width `< r` are
solvable, but a full `r`-variable simultaneous reference system forces cycle
width `r` and therefore has no solution. This gives a stronger version of the
user's original intuition: mutual reference is not just "self-reference with
two names", and higher-arity simultaneous reference need not collapse back to
the unary case unless pairing/projection/diagonalization resources are added.

## Relation to Existing Notes (Updated)

- `g2-fg2-hierarchy.md` controls the orbit/preperiod data that the supplement
  promotes to a first-class invariant.
- `aps-cardinal-invariants-fixed-points.md` matches the new fixed-point
  cardinal layer $\mathrm{Fix}_{\ge \kappa}$.
- `predicate-topology-fixed-points.md` carries the continuous/domain side of
  the hierarchy.
- `smullyan-lawvere-categorical-diagonalization.md` supplies the code-space and
  weak-point-surjectivity background for the top end of the hierarchy.

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

### Drive Separation Witnesses

The newer Drive supplement isolates a stronger claim than the original "find a
2-cycle" task: there are APS models satisfying A1-A4 in which:

$$
\mathrm{SR}\wedge\neg\mathrm{MR}_2.
$$

Its finite witness is a five-point APS model $M_5$, built over a three-point
core and reported as machine-checked by exhaustive search. The same supplement
also gives a continuous/topological witness `ALop`, reframing
`SR` versus `MR_2` as a fixed-point-property failure for products.

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

### Conjecture 4: The Main Hierarchy Is Strict over Natural Finite or Computable Classes

The hierarchy

$$
\mathrm{FSR}
\Rightarrow
\mathrm{MR}_\omega
\Rightarrow
\mathrm{MR}_{<\omega}
\Rightarrow
\mathrm{SR}(C)
\Rightarrow
J
\Rightarrow
\mathrm{FG2}
\Rightarrow
\mathrm{G2}
\Rightarrow
\mathrm{Taut}
$$

should admit strict separations by a mixture of finite APS/preAPS models,
computable periodic models, and continuous/domain-theoretic models.

### Conjecture 5: The SR/MR Axis Is Independent from the G2 Axis

There should be APS/preAPS models realizing the following combinations:

$$
\mathrm{SR}\wedge\neg\mathrm{MR}_2,
\qquad
\neg\mathrm{SR}\wedge\mathrm{MR}_2,
\qquad
\mathrm{FG2}\wedge\neg\mathrm{MR}_2,
\qquad
\mathrm{MR}_2\wedge\neg\mathrm{FG2}.
$$

The new Drive material strongly suggests that the first combination is already
realized by finite APS models, while the broad hierarchy PDF gives instance
level examples motivating the second.

## Relation to Existing Notes

- `self-existence-sentences.md` treats self-existence and diagonal sentences.
  This note generalizes the fixed-point target from one sentence to systems.
- `g2-fg2-hierarchy.md` supplies the orbit and nFG2 analysis needed for finite
  $\boxtimes$-dynamics.
- `indexed-aps-fibred-algebra.md` supplies the categorical environment for
  parameterized and graph-indexed reference.
- `smullyan-lawvere-categorical-diagonalization.md` gives the substitution and
  quotation machinery needed to construct such systems.
- `local-fg2-pullback-aps-zoo.md` now gives a theoremhood-only comparison
  semantics that may be relevant when mutual-reference systems fail to collapse
  back into ordinary self-reference.

## Verification Tasks

1. Add checker output for $\mathrm{Fix}(\boxtimes^n)$ for small $n$, not only
   $\mathrm{Fix}(\boxtimes)$.
2. Compute the period and preperiod of the $T$-orbit for every finite ZOO model.
3. Search for finite models separating:
   - $\mathrm{Fix}(\boxtimes)$ from $\mathrm{Fix}(\boxtimes^2)$;
   - mutual reference from FG2;
   - all-level nFG2 from syntactic fixed-point existence away from the
     $T$-orbit.
4. Reconstruct the finite APS witness $M_5$ from `selfref_mutref.pdf` directly
   in `code/models/`, together with a checker for `SR`, `MR_2`, and the
   unary-signature collapse conditions.
5. Translate the Lopez/product obstruction into repository language:
   - identify the precise fixed-point property used by the continuous witness;
   - record how product failure corresponds to `SR` without `MR_2`.
6. Formalize graph-shaped reference systems as an indexed APS construction.
7. Re-export the source share and insert any missing examples or terminology
   from the original Project discussion.
8. Record an explicit hierarchy of principles
   $\mathrm{FSR}, \mathrm{MR}_n, \mathrm{Per}_n, \mathrm{Fix}_{\ge \kappa}$ in
   the repository definitions file and align the note names with that scheme.
9. Search for a finite witness with
   $\mathrm{Per}_2$ but not $\mathrm{Per}_1$, and compare it to the existing
   `nFG2` and detached-fixed-point zoo models.
