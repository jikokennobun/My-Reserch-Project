# Reports

Machine-generated checker and search reports live here. These are artifacts,
not source code, and they should be cited from research notes when they certify
a finite model, search result, or counterexample.

## Report Contract

A useful report should make the following clear:

1. input model or search space;
2. script and command used;
3. checked properties;
4. result summary;
5. timestamp or commit context when available.

For APS/G2-ZOO reports, include the values of:

$$
\mathrm{G2},
\qquad
\mathrm{FG2},
\qquad
\mathrm{nFG2}(k),
\qquad
\mathrm{FP\text{-}synt},
$$

and any relevant residuation, bottom-discipline, or completion-fixed-point
profile.

## Use in Notes

Research notes should not simply say that a search was run. They should cite
the report path and explain which mathematical claim the report supports. If a
report is exploratory or incomplete, mark it as such.

## Recent Reports

- `pass69-consistency-cut-infinite-g2-zoo-check.json`: verifies the Pass-69
  G2-ZOO expansion layer. It checks cycle APS models with flat consistency
  towers, detached Rosser period preAPS models, the A3/cut boundary, and the
  named statements `Con-orb(n)`, `G2(n)`, `FG2(n)`, `CutA3`, and
  `flat-orbit(N)`.

- `pass68-derived-pro-cokernel-phantom-check.json`: verifies the Pass-68
  derived pro-cokernel recovery of `Zhat/Z`.  It checks lcm-tower cofinality,
  CRT levelwise-zero quotients, non-Mittag-Leffler kernel behavior, zero kernel
  inverse limit, and growth of profinite completion prefixes.

- `pass67-restricted-product-adelic-duality-check.json`: verifies the Pass-67
  restricted-product finite conductor model.  It checks local conductor
  self-duality, self-annihilating integral lattices, product compatibility,
  signed boundary transpose, and CRT finite-level collapse of the diagonal
  quotient.

- `pass66-duality-normalization-scheme-lift-check.json`: verifies the Pass-66
  duality-normalization split.  It checks that plain
  `RHom_Z(-, Z)` is shifted on finite cyclic layers, character duality preserves
  finite `Z/p^k` layers, finite boundaries dualize by signed transpose, and the
  all-prime product/direct-sum gap is real.

- `pass65-verdier-dual-recollement-functional-equation-check.json`: verifies the
  Pass-65 finite-model Verdier-dual recollement calculation.  It checks the
  $i^!$ local-support ranks, the signed transpose rule
  $\mathbb D(d_S)=-d_S^T$, duality squared, mod-2 sign collapse, and
  finite-prime naturality.

- `noncommutative-selective-median-check.json`: verifies the Pass-38
  two-residual selective-median construction for an $S_3$ front. The median case
  is fully residuated; the no-median and full-cap controls fail with the
  predicted residual/monotonicity obstructions.
