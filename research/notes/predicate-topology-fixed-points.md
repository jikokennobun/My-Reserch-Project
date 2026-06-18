# Predicate Topology and Fixed Points

## Source and Provenance

- Original Project share: <https://chatgpt.com/share/69fbf42a-8de0-83e8-8cff-9b51f13a16c0>
- Imported from Research Project handoff: `2026-05-22`
- Rechecked from the watchlist on `2026-06-14`: reachable and unchanged at
  `2026-06-14T06:41:52+09:00`.
- Drive supplements:
  - `domain_stable_ams_aps_raps_models.pdf`
    (`https://drive.google.com/file/d/1dSzWJT0EnT4fHONge6gajqk1wWBKJrkK/view`)
    fetched through the Google Drive connector on `2026-06-10`.
  - `ams_aps_domain_theory_research_note.pdf` (Drive created
    `2026-06-13T18:51:38Z`)
  - `unary_operator_fixed_point_spaces.pdf` (Drive created
    `2026-06-13T19:44:23Z`)
  - `karazeris_categorical_domain_theory_commentary.pdf` (Drive created
    `2026-06-18T04:27:40.455Z`, stored under `ChatGPT_Study`)

## Abstract

This note studies the topological and domain-theoretic line inside the APS
program: can one build large families of APS or residuated APS models from
Scott opens, stable domains, event structures, coherence spaces, and related
semantic objects, and what do those models say about G2, FG2, and
$\boxtimes$-fixed points? The June 10 and June 13 Drive supplements force a
two-sided answer. On the negative side, many natural domain-theoretic
constructions give complete APS or RAPS models that in nontrivial cases refute
G2, refute FG2, and admit no $\boxtimes$-fixed point. On the positive side,
the later June 13 notes show that specially engineered algebraic Scott-APS
objects can realize arbitrary fixed-point anti-chains and amplify spectra by
function-space constructions. Domain semantics is therefore not a single
fixed-point source; it is the place where one can see exactly which continuity,
compactness, and A3-locality hypotheses create or block self-reference.

## Background and Notation

We use the repository convention

$$
S=(L,\le,\Box,\boxtimes,T,\bot).
$$

Here $T$ is the designated "provable" element, $\bot$ is the contradiction or
refutability bound, $\Box$ is the positive/provability-like modality, and
$\boxtimes$ is the refutability-like modality. See
[research/definitions.md](C:\Users\20010215fjii\Documents\GitHub\My-Reserch-Project\research\definitions.md)
for the shared APS vocabulary.

The Drive supplement uses a slightly different notation:

- AMS: an abstract modal structure with no APS axioms imposed a priori.
- APS: AMS satisfying A1-A4.
- RAPS: a residuated AMS/APS with product and residuals.

When translating to repository notation, its operator $\Box$ is the positive
modality and its operator $\boxtimes$ is the refutability modality, often
implemented as a pseudocomplement or residual negation.

## Definitions

The domain-theoretic supplement fixes the APS axioms in the familiar form

$$
x\le y \Rightarrow \Box x\le \Box y \text{ and } \boxtimes y\le \boxtimes x,
$$

$$
T\le \boxtimes\bot,
$$

$$
x\le \Box y \text{ and } x\le \boxtimes y \Rightarrow x\le \boxtimes T,
$$

$$
\boxtimes x\le \Box\boxtimes x.
$$

The key semantic constructions in the PDF are:

1. Scott-frame models. For a dcpo $D$, let $L=\mathcal O(D)$ be the frame of
   Scott opens, ordered by inclusion, with
   $$
   T=D,\qquad \bot=\varnothing,\qquad \Box=\mathrm{id},\qquad
   \boxtimes U:=U^\ast:=U\Rightarrow\varnothing.
   $$
2. Stable/coherence models. Use event-structure conflict or biorthogonality to
   define $\boxtimes$ as an orthogonality operator and $\Box$ as identity or
   double-orthogonal closure.
3. Residuated domain models. In a frame, quantale, or residuated lattice, set
   $$
   \boxtimes x := x\Rightarrow \bot
   $$
   and test whether A3 survives.

These are semantic realizations of the general analytic APS strategy: replace
syntactic diagonalization by topology, continuity, orthogonality, or
residuation.

A more categorical variant from the June 18 Karazeris commentary is:

4. Scott topos and powercategory semantics. For a finitely accessible category
   $K$ with finitely presentable subcategory $K_f$, define
   $$
   \sigma K := \mathbf{Set}^{K_f},
   $$
   viewed as the categorical replacement for the Scott topology of an
   algebraic domain. Its upper and lower power constructions are
   $$
   PU(K):=\mathrm{LexCont}(\sigma K,\mathbf{Set}),
   \qquad
   PL(K):=\mathrm{Colim}(\sigma K,\mathbf{Set}).
   $$
   Here $\mathrm{LexCont}$ preserves finite limits and filtered colimits, so it
   categorifies the classical "compact saturated / Scott-open filter" side of
   upper powerdomains.

## Main Reconstruction

The supplement makes four mathematically useful claims.

### Proposition 1. Scott-frame RAPS give a large negative zoo

For any nontrivial frame $H$, the structure

$$
(H,\le,\mathrm{id},(\_)^\ast,1,0)
$$

is a residuated APS, but in every nontrivial case:

$$
\neg \mathrm{G2},\qquad \neg \mathrm{FG2},\qquad
\neg \exists p\,(p=\boxtimes p).
$$

The reason is structural rather than accidental. Since

$$
\boxtimes 1 = 1^\ast = 0,
$$

the antecedent of G2 holds while $1\not\le 0$ in any nontrivial frame, so G2
fails. Likewise

$$
\boxtimes\boxtimes 1 = 0^\ast = 1 \not\le 0 = \boxtimes 1,
$$

so FG2 fails. A fixed point $p=\boxtimes p$ would force
$p=p\wedge p^\ast\le 0$, hence $p=0$, but $0^\ast=1\ne 0$.

This is stronger than the earlier placeholder note: it says that Scott-open
semantics do not merely "suggest topological fixed points"; they systematically
generate countermodels to the fixed-point premise needed for abstract G2.

### Proposition 2. Stable-domain semantics mostly produce refutation operators, not fixed points

The supplement organizes stable semantics in three layers:

1. configuration domains of stable event structures;
2. coherence/biorthogonality spaces;
3. Scott-open or orthogonality-derived RAPS.

In all of these, $\boxtimes$ detects conflict, incompatibility, or orthogonal
disjointness. That gives natural semantics for refutability, but it also makes
$\boxtimes$ too extensional to support nontrivial self-reference. The dominant
pattern is:

- A1, A2, and often A4 are easy.
- A3 survives in pseudocomplement/orthogonality settings only when
  self-conflict collapses to zero.
- Nontrivial $\boxtimes$-fixed points are absent unless one introduces a more
  intensional or paraconsistent notion of conflict.

This clarifies why the old note's generic "continuity may create fixed points"
was too optimistic. Continuity alone is not enough; the semantic reading of
refutation matters.

### Proposition 3. A3 is the true semantic bottleneck

The supplement compares several residuated examples:

- Godel and product t-norm chains satisfy the APS conditions with crisp
  residual negation.
- Lukasiewicz chains fail A3 because
  $$
  x\wedge (x\Rightarrow 0)\not\le 0
  $$
  for interior points such as $x=\tfrac12$.
- Relation quantales also fail A3 because residual negation need not be
  disjoint from the original relation.

So the important question is not "does the semantics have residuals?" but
instead:

$$
\text{when does the residual negation enforce the APS explosion law A3?}
$$

This gives a precise semantic reformulation of the repository's recurrent theme
that G2/FG2 separation is controlled by the interaction between positive and
negative modalities, not by one modality in isolation.

### Proposition 4. Fixed points reappear only after extra structure is added

The supplement does identify routes by which domain-style models can recover
fixed points, but each route adds data beyond plain Scott semantics:

1. complete lattices plus monotone endomorphisms, via Knaster-Tarski;
2. interval or metric semantics plus continuity/contraction, via
   intermediate-value or Banach-style arguments;
3. syntactic self-substitution/repeat operators, via Smullyan-style
   diagonalization;
4. semantic completions that enlarge the carrier enough to solve previously
   unsatisfied recursive equations.

This shows that domain theory is best understood here as a control parameter:
it tells us exactly which completion or continuity assumptions are strong enough
to manufacture fixed points and which are not.

### Proposition 8. Scott-topos semantics localize A3 to finitely presentable approximants

The June 18 Karazeris commentary adds a structural reason for why A3 behaves as
the bottleneck in domain semantics. If a semantic carrier is presented as a
finitely accessible category
$$
K \simeq \mathrm{Flat}(K_f^{op},\mathbf{Set}),
$$
then every object is a filtered colimit of finitely presentable ones, and
finite-limit data is read off from the small category $K_f$. In that setting,
the Scott topos
$$
\sigma K = \mathbf{Set}^{K_f}
$$
is the right replacement for the Scott frame of opens, and upper power
constructions live in
$$
PU(K)=\mathrm{LexCont}(\sigma K,\mathbf{Set}).
$$

This matters for APS because A3 is exactly the clause that mixes a positive and
an antitone modality through a finite-intersection style compatibility:
$$
x\le \Box y,\ x\le \boxtimes y \Rightarrow x\le \boxtimes T.
$$
In Scott-topos language, such a law can only be stable when the finitely
presentable approximants already control the needed finite-limit behavior.
Karazeris's coherent-category criterion packages this as a finite cocone or
`2/3-SFP` condition on $K_f$: common upper-bound data and the identifications
between different finite cocones must already be generated by finite zig-zags
inside $K_f$.

So the categorical reconstruction of the old domain-theory slogan is:

1. filtered-colimit accessibility explains why A3 should first be checked on
   compact or finitely presentable approximants;
2. the upper powercategory explains why "must-like" or refutability-like
   semantics demand finite-limit preservation, not just raw colimit
   preservation;
3. failure of coherence in $K_f$ predicts exactly the kind of pathology where
   natural powerdomain semantics still carry negation or conflict information
   but no longer preserve the intersection behavior required for APS A3.

This refines the earlier note in two ways. First, it says the negative domain
examples are not accidents of pseudocomplementation; they reflect a categorical
instability of finite approximation data. Second, it provides a route for
positive constructions: to build a robust Scott-style APS with A3, one should
engineer the finitely presentable layer so that the relevant cocones, products,
and finite-limit identifications are already coherent before taking any
completion.

### Proposition 5. In algebraic Scott-APS, A3 becomes a compact-basis condition

The June 13 domain-theory memo recasts A3 as a local Horn condition on compact
approximants. If $L$ is an algebraic dcpo and $S=(L,\le,\Box,\boxtimes,T,\bot)$
is Scott-continuous, then the global clause

$$
x\le \Box y \text{ and } x\le \boxtimes y \Rightarrow x\le \boxtimes T
$$

should be checked on compact elements first:

$$
k\in K(L),\ k\le \Box y,\ k\le \boxtimes y \Rightarrow k\le \boxtimes T.
$$

Because every $x$ is the directed join of compact $k\le x$, Scott continuity
then upgrades the compact test to the full A3 law. This is the domain-theoretic
reason A3 behaves more like a local consistency-of-approximants condition than
like a global algebraic identity.

### Proposition 6. Antitone Scott operators have an anti-chain fixed-point geometry

The June 13 supplements also isolate a general principle extending the old APS
anti-chain observation. For any order-reversing Scott-continuous
$f:L^{op}\to L$ on a complete or algebraic domain,

$$
\mathrm{Fix}(f)=\{x : f(x)=x\}
$$

is an anti-chain. Moreover, if $a$ is the least fixed point of $f^2$, then the
interval

$$
[a,f(a)]
$$

is the canonical two-cycle kernel containing every genuine $f$-fixed point.
Transferred back to APS, this says that $\boxtimes$-fixed points never form a
chain-like positive theory region; they sit inside a narrow self-dual kernel of
the antitone dynamics.

### Proposition 7. Engineered Scott-APS can realize arbitrary fixed-point widths

The negative Scott-frame examples are not the whole story. The June 13 memo
constructs algebraic Scott-APS models `Star_\kappa` with

$$
|\mathrm{Fix}_{\boxtimes}(S)|=\kappa
$$

for arbitrary cardinals $\kappa$, and then amplifies spectra by function-space
constructions of the shape $D^X$. So plain frame pseudocomplements kill
fixed points, but custom algebraic Scott-APS domains can realize them sharply.
The real divide is not "domain semantics versus syntax"; it is "natural
extensional negation versus engineered antitone self-duality."

## Examples and Counterexamples

The Drive supplement contains concrete infinite countermodel families worth
remembering.

### Example: $\omega+1$ Scott frame

For $D=\omega+1$, nonempty Scott opens have pseudocomplement $\varnothing$, so
refutability collapses:

$$
\boxtimes U=
\begin{cases}
D & U=\varnothing,\\
\varnothing & U\ne\varnothing.
\end{cases}
$$

This is a complete RAPS, but it destroys G2, FG2, and fixed points. It is a
canonical "refutation collapse" model.

### Example: flat domain $\mathbb N_\bot$

For the flat domain, the Scott frame behaves classically on total values but
nonclassically at $\bot$. This gives an infinite, computable RAPS in which
refutation of a concrete observation is easy, but refutation of undefinedness
is not. It is therefore a good semantic testbed for separating partial
information from contradiction.

### Example: prefix domains

On $\Sigma^{\le\omega}$, $\boxtimes$ is interpreted by prefix incompatibility.
This connects APS refutability to branching computation and event-structure
conflict rather than to ordinary Boolean negation.

### Counterexample: Lukasiewicz chain

The supplement's interval semantics show that even when fixed points of
continuous maps exist, APS explosion can still fail. The interior point
$x=\tfrac12$ witnesses the failure of A3, so continuity of the ambient interval
does not rescue the APS axioms.

## Relation to Existing Notes

This note now links four existing strands.

1. It sharpens
   [analytic-aps.md](C:\Users\20010215fjii\Documents\GitHub\My-Reserch-Project\research\notes\analytic-aps.md)
   by replacing the vague slogan "use domain theory for fixed points" with a
   split verdict: plain Scott-frame semantics usually generate counterexamples,
   while fixed points require extra completion, contraction, or substitution
   structure.
2. It extends
   [residuated-algebra-domain-completion.md](C:\Users\20010215fjii\Documents\GitHub\My-Reserch-Project\research\notes\residuated-algebra-domain-completion.md)
   by giving explicit semantic families where residual negation is available but
   A3 fails, especially Lukasiewicz and relation-quantale models.
3. It supports
   [g2-zoo-topological-taming.md](C:\Users\20010215fjii\Documents\GitHub\My-Reserch-Project\research\notes\g2-zoo-topological-taming.md)
   by showing that topology alone does not tame the zoo; one must specify which
   topological, orthogonality, or completion mechanism is meant.
4. It now also links directly to
   [indexed-aps-fibred-algebra.md](C:\Users\20010215fjii\Documents\GitHub\My-Reserch-Project\research\notes\indexed-aps-fibred-algebra.md):
   Scott toposes and powercategories provide a categorical-semantic layer below
   hyperdoctrines and indexed APS, showing how finite approximation data can
   control substitution-like semantics before one adds quotation or
   diagonalization.

## Open Problems

The Drive supplement raises several concrete follow-up tasks.

1. Characterize Scott-continuous maps $f:D\to D$ for which the induced modal
   pair
   $$
   \Box_f(U)=f^{-1}(U),\qquad \boxtimes(U)=U^\ast
   $$
   satisfies A3 and A4.
2. Measure the "refutation density" of a stable event structure from its
   conflict graph and compare that invariant with G2/FG2 failure patterns.
3. Classify commutative residuated lattices satisfying
   $$
   x\wedge(x\Rightarrow 0)\le 0,
   $$
   especially across Godel, product, Lukasiewicz, BL, MV, and MTL settings.
4. Find a genuinely domain-theoretic or stable-semantic model with a nontrivial
   $\boxtimes$-fixed point, rather than a syntactically imported one.
5. Determine which completions create fixed points that are semantic only and
   which reflect back to definable elements of the original APS.
6. Give necessary and sufficient compact-basis conditions for A3 in algebraic
   Scott-APS, then compare them with the engineered `Star_\kappa` models that
   realize arbitrary anti-chain fixed-point spectra.
7. Characterize finitely accessible categories $K$ and modal data on
   $\sigma K=\mathbf{Set}^{K_f}$ for which the upper powercategory
   $PU(K)=\mathrm{LexCont}(\sigma K,\mathbf{Set})$ supports APS-style A3/A4,
   and decide whether Karazeris's coherent `2/3-SFP` condition is the exact
   categorical shadow of the repository's A3-stability obstruction.

## Verification Tasks

- Compare the Scott-frame counterexample scheme with finite models already in
  `code/models/` to isolate which failures are essentially infinitary.
- Build a small formal table recording, for each semantic family, the truth
  values of A1-A4, G2, FG2, and `Fix boxtimes`.
- Test whether the repository's current completion constructions preserve A3 or
  only preserve A1/A2/A4.
