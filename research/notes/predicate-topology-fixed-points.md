# Predicate Topology and Fixed Points

## Source and Provenance

- Original Project share: <https://chatgpt.com/share/69fbf42a-8de0-83e8-8cff-9b51f13a16c0>
- Imported from Research Project handoff: `2026-05-22`
- Access status on `2026-06-10`: the watched ChatGPT share remained unreachable
  from this environment, so the reconstruction below separates prior handoff
  material from a directly accessible Drive artifact.
- Drive supplement: `domain_stable_ams_aps_raps_models.pdf`
  (`https://drive.google.com/file/d/1dSzWJT0EnT4fHONge6gajqk1wWBKJrkK/view`)
  fetched through the Google Drive connector on `2026-06-10`.

## Abstract

This note studies the topological and domain-theoretic line inside the APS
program: can one build large families of APS or residuated APS models from
Scott opens, stable domains, event structures, coherence spaces, and related
semantic objects, and what do those models say about G2, FG2, and
$\boxtimes$-fixed points? The main conclusion of the Drive supplement is
negative in a precise way: many natural domain-theoretic constructions give
complete APS or RAPS models, but in nontrivial cases they typically refute G2,
refute FG2, and admit no $\boxtimes$-fixed point. This turns domain semantics
into a systematic source of counterexamples and sharpens the role of A3/A4 and
fixed-point hypotheses.

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

This note now links three existing strands.

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

## Verification Tasks

- Compare the Scott-frame counterexample scheme with finite models already in
  `code/models/` to isolate which failures are essentially infinitary.
- Build a small formal table recording, for each semantic family, the truth
  values of A1-A4, G2, FG2, and `Fix boxtimes`.
- Test whether the repository's current completion constructions preserve A3 or
  only preserve A1/A2/A4.
