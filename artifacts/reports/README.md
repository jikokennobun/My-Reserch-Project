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

- `pass65-verdier-dual-recollement-functional-equation-check.json`: verifies the
  Pass-65 finite-model Verdier-dual recollement calculation.  It checks the
  $i^!$ local-support ranks, the signed transpose rule
  $\mathbb D(d_S)=-d_S^T$, duality squared, mod-2 sign collapse, and
  finite-prime naturality.

- `noncommutative-selective-median-check.json`: verifies the Pass-38
  two-residual selective-median construction for an $S_3$ front. The median case
  is fully residuated; the no-median and full-cap controls fail with the
  predicted residual/monotonicity obstructions.
