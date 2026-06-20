# Dense Phantom Boundary And Action Obstruction

Date: 2026-06-20

## Summary

Pass 84 studies the dense quotient
$$
\mathbb R\to\Sigma\to\epsilon=\widehat{\mathbb Z}/\mathbb Z,
\qquad
\Sigma=(\mathbb R\times\widehat{\mathbb Z})/\mathbb Z.
$$
The topological quotient $\epsilon$ is indiscrete, so it has no nontrivial
continuous maps to Hausdorff targets.  The finite-prime phantom survives only
as a solid derived boundary.

## Main Claims

- **Indiscrete quotient.** Since $\mathbb Z$ is dense in
  $\widehat{\mathbb Z}$, every nonempty open subset of $\widehat{\mathbb Z}$
  saturates to all of $\widehat{\mathbb Z}$ under addition by $\mathbb Z$.
  Hence $\widehat{\mathbb Z}/\mathbb Z$ is indiscrete and its Hausdorff
  reflection is $0$.
- **No continuous translation action.** Any continuous homomorphism from
  $\epsilon$ to the compact Hausdorff solenoid $\Sigma$ is zero.  Therefore
  the Borel unipotent $U=\epsilon$ does not act by nontrivial continuous
  translations on $\Sigma$.
- **Derived Weyl replacement.** In the solid derived category,
  $$
  D\epsilon\simeq\mathbb Q[-1],
  \qquad
  \mathrm{Ext}^1_{\mathrm{Solid}}(\epsilon,\mathbb Q)\simeq\mathbb Q.
  $$
  The missing Weyl flip $\epsilon\to\mathbb Q$ is replaced by the degree-$1$
  finite-adele extension
  $$
  0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0.
  $$

## Machine Verification

`code/scripts/check-pass84.py` produced
`artifacts/reports/pass84-dense-phantom-boundary-action-check.json` with
overall PASS.  It checks finite saturated-open shadows, finite continuous maps
from an indiscrete quotient to discrete targets, character descent, and the
absence of finite degree-$0$ Weyl shadows into $\mathbb Q$.

## Next Use

Pass 85 should build an explicit two-term complex model comparing
$[\mathbb Z\to\widehat{\mathbb Z}]$, $[\mathbb R\to\Sigma]$, and
$[\mathbb Q\to\mathbb A_f]$, then identify which quasi-isomorphisms preserve
the Borel shear class.
