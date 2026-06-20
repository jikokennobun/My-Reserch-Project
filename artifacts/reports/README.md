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

- `pass89-borel-torsor-rosser-phantom-check.json`: verifies the Pass-89
  finite certificate for the Rosser Borel-torsor theorem. It checks finite
  Cech windows where changing a witness representative by a coboundary
  preserves the class, records affine Borel shadows
  $(\mathbb Z/N)^\times\ltimes\mathbb Z/N$ with singleton strict marked
  stabilizer, and separates invariant torsor data from non-invariant witness
  choices.

- `pass88-shear-extension-stabilizer-check.json`: verifies the Pass-88
  stabilizer split for the finite-adele shear extension. It checks that
  nonzero rational scalars preserve the extension line while only scalar $1$
  preserves the integral marking, records finite Borel shadows
  $(\mathbb Z/N)^\times\ltimes\mathbb Z/N$, and confirms that no derived
  automorphism survives for the final $\mathbb Q$-kernel extension after the
  torsion-boundary decoration rule.

- `pass87-mapping-space-shear-initiality-check.json`: verifies the Pass-87
  finite certificate for the derived mapping-space form of shear initiality. It
  records the cofiber/fiber sequence with homotopy fiber
  $\mathbf R\mathrm{Map}(\mathbb Q/\mathbb Z,D)$, checks contractibility for
  uniquely divisible kernels, and exhibits the $N^r$ finite boundary choices
  contributed by torsion-divisible summands.

- `pass86-shear-pushout-universal-property-check.json`: verifies the Pass-86
  finite certificate for the shear-pushout universal property. It checks unique
  extension from $\mathbb Z$ to bounded denominator localizations into
  $\mathbb Q$-vector kernels, confirms finite/Hausdorff shadows remain killed,
  verifies unique factorization through $C_{\mathbb Q}$ for checked
  finite-dimensional targets, and records the $\mathbb Q/\mathbb Z$ torsion
  caveat showing that arbitrary divisible kernels do not give uniqueness.

- `pass85-two-term-boundary-complex-check.json`: verifies the Pass-85
  two-term complex comparison. It checks that the finite/Hausdorff shadows of
  $[\mathbb Z\to\widehat{\mathbb Z}]$, $[\mathbb R\to\Sigma]$, and
  $[\mathbb Q\to\mathbb A_f]$ are acyclic, that the lcm kernel tower has
  strict non-Mittag-Leffler drops, that the unit residues remain compatible,
  and that only the finite-adele pushout preserves the Borel shear class.

- `pass84-dense-phantom-boundary-action-check.json`: verifies the Pass-84
  dense quotient and action obstruction. It checks that finite shadows of
  $\widehat{\mathbb Z}/\mathbb Z$ have only empty/all saturated opens, that
  continuous maps from the resulting indiscrete quotient to finite Hausdorff
  targets are constant, that only the trivial finite character descends, and
  that finite degree-$0$ Weyl shadows into $\mathbb Q$ vanish.

- `pass83-solenoid-exact-triangle-correction-check.json`: verifies the Pass-83
  correction to the adelic solenoid row. It checks the dual finite rows
  $0\to\mathbb Z\xrightarrow{\times N}\mathbb Z\to\mathbb Z/N\to0$, the
  nonsplitting obstruction, character restriction from global $\mathbb Q$ to
  the profinite kernel, and the fact that only the trivial finite character
  descends to $\epsilon=\widehat{\mathbb Z}/\mathbb Z$ in degree $0$.

- `pass82-whittaker-archimedean-repair-check.json`: verifies the Pass-82
  Whittaker/archimedean residue of the solid Borel. It checks that the
  constant $U_N=\mathbb Z/N$ action has only a trivial Fourier coefficient,
  that nontrivial $U$-Whittaker functionals on $I(s)=\chi_s$ vanish, and that
  finite shadows motivating the archimedean repair are exact; Pass 83 corrects
  the compact solenoid row by replacing the provisional kernel
  $\widehat{\mathbb Z}/\mathbb Z$ with the closed kernel $\widehat{\mathbb Z}$.

- `pass81-degenerate-principal-series-functional-equation-check.json`:
  verifies the Pass-81 degenerate-principal-series wall. It checks finite flag
  varieties and Fourier intertwiners, Gauss-sum $c$-factors, and the limit
  obstruction $\mathrm{Hom}(\epsilon,\mathbb Q)=0$ that prevents a solid
  functional equation.

- `pass80-metaplectic-borel-noflip-check.json`: verifies the Pass-80
  metaplectic no-descent result. It checks finite $\mathrm{SL}_2(\mathbb Z/N)$
  Weyl flips and Fourier transforms, then records that the solid limit has
  only the Borel $\mathbb Q^\times\ltimes\epsilon$ because the flip would live
  in $\mathrm{Hom}(\epsilon,\mathbb Q)=0$.

- `pass79-symplectic-lagrangian-phantom-check.json`: verifies the Pass-79
  hyperbolic-plane correction. It checks that the unique nonzero
  self-pairing of $\epsilon$ lands in degree $2$, that the finite-adele
  extension generates $\mathrm{Ext}^1(\epsilon,\mathbb Q)$, and that the
  resulting form is alternating but degenerate.

- `pass78-solid-reflexivity-phantom-check.json`: verifies the Pass-78
  reflexivity analysis. It checks the degree-one dual of $\epsilon$, the
  double-dual recovery through the unit class, and the antipode sign from the
  odd phantom shift.

- `pass77-derived-solid-realization-check.json`: verifies the Pass-77
  derived/solid realization correction. It records the LCA dual no-go,
  the solid degree shift, and the signed boundary law
  $D(d_S)=-d_S^T$.

- `pass76-stratified-pro-site-realization-check.json`: verifies the Pass-76
  stratified pro-site model. It checks clopen support projectors, pro-stage
  truncation projectors, site factorization, and generator-family faithfulness
  on the finite prime window.

- `pass75-intrinsic-projector-realization-check.json`: verifies the Pass-75
  projector-enriched realization. It replaces explicit support/stage tags by
  Boolean support idempotents and lcm-stage projectors, checks generator-family
  faithfulness, and verifies the projector relations.

- `pass73-exact-realization-obstruction-check.json`: companion no-go check
  integrated during Pass 75. It records why ordinary exact 1-category
  initiality is too strong for $\mathcal H_\epsilon$: the
  $\varprojlim^1$ phantom is derived pro-data, not a finite exact-cone value.

- `pass74-tagged-proab-realization-check.json`: verifies the Pass-74 tagged
  restricted pro-Ab realization test. It checks that tagged signatures are
  faithful on finite conductor windows, Loeb-Rosser boundaries, restrictions,
  signed duality, and lcm pro-stages, and records collisions after forgetting
  support/stage tags.

- `pass73-h-epsilon-universal-property-check.json`: verifies the Pass-73
  presentation-level universal property for $\mathcal H_\epsilon$. It checks
  finite/pro normal forms, restriction and signed-dual relations, admissible
  certificate-target initiality, and minimality obstructions when any required
  generator family is omitted.

- `pass72-hybrid-exact-epsilon-category-check.json`: verifies the Pass-72
  hybrid exact-category candidate for $\epsilon_{\mathbb P}$. It checks finite
  exact shadows, restriction composition, signed-dual restriction compatibility,
  conductor-layer bookkeeping, and the non-Mittag-Leffler lcm tower separating
  finite CRT zero from the derived pro-Ab quotient.

- `pass71-restricted-product-epsilon-duality-check.json`: verifies the Pass-71
  pro-restricted all-prime epsilon package. It checks finite-prime boundary
  naturality, signed-dual naturality, finite conductor self-annihilating
  lattices, and the support-profile gap that rejects bare infinite-product
  duality as the all-prime statement.

- `pass70-derived-pro-epsilon-comparison-check.json`: verifies the Pass-70
  algebraic comparison between the derived pro-cokernel and the Loeb-Rosser
  recollement class. It checks finite CRT shadows, the primitive diagonal
  $\Delta:\mathbb Z\to\mathbb Z^S$, the surjective boundary
  $d_S:\mathbb Z^S\to\mathbb Z^{|S|-1}$ with diagonal kernel, and the finite
  signed-dual shadow $d_S\mapsto-d_S^T$.

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
