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

- `pass105-support-descent-primitive-orientations-check.json`: verifies the
  Pass-105 finite certificate for support descent of all-prime primitive
  orientations. It checks that zero-extension preserves zero-sum,
  primitivity, and the antipode; that zero-extension composes along support
  chains; that deleting coordinates can destroy zero-sum and therefore is not
  a total orientation restriction; that the all-prime object is a filtered
  colimit by zero-padding modulo padded zeros; that no support-symmetric
  primitive orientation exists; and that the correct package is a
  span-stack/Grothendieck object with the `Z/2` boundary-line local system,
  not a plain restriction sheaf.

- `pass104-signed-pro-solid-boundary-object-check.json`: verifies the
  Pass-104 finite/pro certificate for the signed all-prime boundary package.
  It checks that the compatible finite sign residues `{sigma mod N}` assemble
  to the diagonal integer `sigma in Zhat`; that both `+1` and `-1` map to zero
  as points of `epsilon = Zhat/Z`; that the orientation double cover is
  absorbed as a `Z/2` local-system action on the boundary/Yoneda line rather
  than surviving as an epsilon-point cover; and that the minimal package
  carries support, conductor, and sign without introducing a degree-0 Weyl
  map.

- `pass103-signed-boundary-conductor-naturality-check.json`: verifies the
  Pass-103 finite certificate for signed boundary naturality under conductor
  reduction. It checks that multiplying the finite CRT diagonal by
  `sigma = +/-1` remains an isomorphism, so signed finite conductor shadows
  are acyclic; that for `M | N`, the class `sigma mod N` reduces to
  `sigma mod M`; that signed CRT reduction squares commute; that sign loss is
  explained exactly by target modulus `2`; and that support enlargement
  remains only a finite CRT choice/span, not a canonical all-prime map.

- `pass102-sign-local-system-adele-boundary-check.json`: verifies the
  Pass-102 finite certificate for pushing the `Z/2` sign local system through
  the primitive collapse and finite-adele boundary. It checks that finite
  Bockstein shadows are `+/-1 mod N`, visible exactly for `N > 2`; that
  signed primitive collapses remain surjective modulo `N`; that support
  zero-extension preserves the signed boundary class; that one-sided sign
  change negates the Yoneda class while two-sided sign change squares to the
  identity; and that no extra finite bookkeeping or degree-0 Weyl map is
  introduced.

- `pass101-oriented-support-groupoid-antipode-quotient-check.json`: verifies
  the Pass-101 finite certificate for the signed oriented-support action
  groupoid. It checks signed morphism closure
  `d = sigma * e_{S,T}(c)`, multiplicative sign composition, antipode
  involutivity and zero-extension compatibility, loss of sign in the coarse
  quotient `[c]={c,-c}`, restoration by a `Z/2` sign local system, and finite
  `N`-torsion sign visibility with collapse at `N=2`.

- `pass100-orientation-torsor-support-functoriality-check.json`: verifies the
  Pass-100 finite certificate for primitive zero-sum orientation torsors. It
  checks that `O_S={c in Z^S : sum c=0, gcd(c)=1}` is preserved by
  zero-extension along support inclusions, that zero-extension is functorial
  and antipode-equivariant, that restriction from larger to smaller supports
  can fail the zero-sum descent condition, that finite kernel sizes factor
  under support enlargement, and that no nonzero support-symmetric primitive
  orientation exists.

- `pass99-torsion-boundary-constant-term-triangle-check.json`: verifies the
  Pass-99 finite certificate for the exact bridge from
  `T_S=(Q/Z)^S/Delta(Q/Z)` to the all-prime constant-term complex
  `[Q -> A_f]`. It checks that primitive zero-sum functionals descend and
  surject onto `Q/Z`, that the finite-shadow kernel has size `N^(|S|-2)`,
  that the antipode sends `c` to `-c` with mod-2 sign collapse, and that the
  collapse is a noncanonical orientation choice compatible with the no-Weyl
  wall.

- `pass98-torsion-boundary-solid-dual-check.json`: verifies the Pass-98 finite
  certificate comparing the torsion boundary
  `(Q/Z)^S/Delta(Q/Z)` with the all-prime solid dual `D epsilon = Q[-1]`. It
  checks `N^(|S|-1)` torsion counts, equality with the compact finite shadow,
  vanishing of divisible rational mod-`N` quotients, support-projection
  surjectivity and kernel sizes, non-equality of raw degree-0 torsion boundary
  with the shifted solid dual, and compatibility with the canonical
  `0 -> Z -> Q -> Q/Z -> 0` extension/no-Weyl wall.

- `pass97-rationalized-finite-adele-row-check.json`: verifies the Pass-97
  finite certificate for the rationalized finite-adele Loebification row. It
  checks that `Z^S/Delta Z` injects into `Q^S/Delta Q`, that the rational
  kernel has dimension `|S|-1`, that finite quotients of the divisible rational
  kernel vanish, that the old `N^(|S|-1)` finite shadow reappears as
  `N`-torsion in `(Q/Z)^S/Delta(Q/Z)`, and that support projections remain
  surjective/Mittag-Leffler.

- `pass96-constant-term-local-loebification-check.json`: verifies the Pass-96
  finite certificate for comparing the constant-term Borel complex with local
  Loebification. It checks the map
  `[Z -> product Z_p] -> [Z^S -> product Z_p]`, the lost unipotent kernel
  `Z^S/Delta Z`, finite shadow sizes `N^(|S|-1)`, singleton vanishing,
  multi-prime nontriviality, triviality of the diagonal Levi kernel, and the
  local Levi quotient proxy of size `|G|^(|S|-1)`.

- `pass95-boundary-only-borel-constant-term-complex-check.json`: verifies the
  Pass-95 finite certificate for the boundary-only Borel constant-term
  complex. It checks that finite conductor complexes
  `[Z/N -> product Z/p^e]` are CRT-acyclic, conductor reductions commute and
  preserve the Borel unit, support projections commute while zero-insertion is
  only a finite-conductor choice/span, and the all-prime complex
  `Q^x semidirect [Q -> A_f]` has solid boundary
  `A_f/Q = Zhat/Z` with no Whittaker component or standard Weyl intertwiner.

- `pass94-all-prime-borel-jshriek-solid-dual-check.json`: verifies the
  Pass-94 finite certificate for the Verdier/solid dual of the all-prime Borel
  $j_!$ class. It checks finite signed boundary duality
  $D(d_S)=-d_S^T$, duality squared, rank preservation, mod-$2$ sign collapse,
  support-dual behavior, the solid identity $D\epsilon=\mathbb Q[-1]$, the
  degree-$1$ finite-adele boundary, and the absence of a degree-$0$ Weyl flip
  $\epsilon\to\mathbb Q$.

- `pass93-all-prime-borel-jshriek-upgrade-check.json`: verifies the Pass-93
  finite certificate for the all-prime Spec-$\mathbb Z$ Borel $j_!$ upgrade.
  It checks that the generic point is open only on finite subspaces, verifies
  surjective support projections and finite mod-$N$ kernel sizes, separates
  support-direction Mittag-Leffler behavior from the per-prime dilation
  $\varprojlim^1$, and records the all-prime global-Levi Borel coefficient
  with unipotent limit $\widehat{\mathbb Z}/\mathbb Z$.

- `pass92-zariski-generic-borel-descent-check.json`: verifies the Pass-92
  finite certificate for Zariski/generic Borel descent. It checks that
  constant coefficients have no horizontal $H^1$ on the full-simplex
  Zariski cover, that the unipotent $j_!$ ghost has rank $|S|-1$, that finite
  mod-$N$ class sets have size $N^{|S|-1}$, and that the Borel relocation keeps
  the Levi in degree $0$ while comparing the unipotent class with the total
  phantom, finite-adele pushout, and hyperbolic shear orbit.

- `pass91-borel-torsor-descent-obstruction-check.json`: verifies the Pass-91
  finite certificate for the Borel torsor descent obstruction. It checks the
  rank $|S|-1$ horizontal descent defect, finite diagonal-kernel sizes
  $N^{|S|-1}$, failure of the global-Levi Borel to be a sheaf on multi-prime
  supports, local-Levi sheafification in a finite proxy, and that shear
  transports but does not kill descent-kernel lifts.

- `pass90-conductor-functorial-borel-torsors-check.json`: verifies the
  Pass-90 finite certificate for conductor-functorial Borel torsors. It checks
  radical support invariance, confirms that coordinate projection descends on
  diagonal quotient torsors while zero-insertion fails when new primes are
  added, records meet/join comparisons for rad-incomparable supports, and
  verifies finite affine Borel reductions along conductor divisibility.

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
