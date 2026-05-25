# Open Problems

## Core Separations

- Separate \(\exists p(p=\boxtimes p)\) from \(\mathrm{FG2}\).
- Separate \(\exists p(p=\boxtimes p)\) from \(\exists p(p=\neg\Box p)\).
- Characterize when \(MND4\)-preAPS plus a Godel-style fixed point collapses.
- Find finite nontrivial models with primitive \(\boxtimes\)-fixed points.

## Completion and Fixed Points

- When does a fixed point in a MacNeille/canonical/ideal completion reflect to a formula-definable fixed point?
- Formulate the completion-reflection square \(L\to\widehat L\) for \(\boxtimes\)
  and identify the exact principal/compact/definable condition needed to round a
  completion fixed point back to \(L\).
- For MacNeille completion, define the order-dual extension convention for
  antitone \(\boxtimes\) and test whether fixed points can be non-principal cuts.
- **[Resolved at size 3]** Search for a non-principal MacNeille completion fixed
  point that has no syntactic \(\boxtimes\)-fixed point. The model
  `three-element-nolattice-nosynt` achieves this: \(L=\{0,a,b\}\) with
  \(0<a,b\), \(a\parallel b\), \(\boxtimes:0\mapsto a,a\mapsto 0,b\mapsto 0\)
  has no syntactic fixed point and has a non-principal completion fixed point
  \(\{0,a,b\}\) under the correct \(L^{op}\)-closure extension. The next
  question is which APS axiom packages allow or rule out this configuration.
- **[New]** Separate "principal" from "reflected" for completion fixed points.
  A principal completion fixed point \(q=i(a)\) need not satisfy \(\boxtimes a=a\).
  Example: `three-chain-antitone` gives principal completion fixed point \(i(t)\)
  with \(\boxtimes t = b\neq t\). Characterize when every principal completion
  fixed point is reflected.
- **[New]** Which APS/preAPS axioms (A1--A4, G2, FG2, MND4) force all completion
  fixed points to be principal? Which force them to be reflected?
- Which APS axioms survive completion?
- Which extensions of \(\Box\) and \(\boxtimes\) are canonical or stable?
- Can completion stability be tied to cut elimination in the Ciabattoni-Galatos-Terui style?

## Domain and Topology

- Define analytic APS so that diagonalization is replaced by a topological/domain-theoretic fixed point theorem.
- Determine which topological conditions tame the G2-ZOO.
- Classify APS where \(\boxtimes\) is continuous, antitone, or representable by a dual operator.

## Categorical/AAL Direction

- Formulate indexed/fibered APS as a fibration or hyperdoctrine-like structure.
- Identify the categorical diagonal/quotation structure needed for APS fixed points.
- Relate generalized proof structures to APS order and modalities.

## Model Classification

- Classify 3- and 4-element APS/preAPS models satisfying selected axiom packages.
- Compute \(|\mathrm{Fix}_{\boxtimes}(S)|\) as a model invariant.
- Build machine-checkable finite models under `models/`.
