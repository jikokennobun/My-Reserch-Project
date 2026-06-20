# Borel-Torsor Rosser Phantom

Date: 2026-06-21

## Summary

Pass 89 states the Rosser phantom as a single Borel-torsor /
extension-class theorem.  In the APS/Rosser model developed in the repository,
the Guaspari-Solovay witness-comparison Cech class, the
$\varprojlim^1(\mathbb Z,\times m)$ phantom, the all-prime quotient
$\epsilon=\widehat{\mathbb Z}/\mathbb Z$, the finite-adele extension
$$
0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0,
$$
and the hyperbolic Borel shear orbit for
$\mathbb Q^\times\ltimes\epsilon$ are presentations of the same torsor class.

## Main Claims

- **Witness-to-phantom bridge.** A Rosser witness-comparison Cech cocycle maps
  to its class in $\operatorname{coker}\delta$, identified with
  $\widehat{\mathbb Z}_m/\mathbb Z$ or $\epsilon$.
- **Phantom-to-adele bridge.** Pushing out
  $0\to\mathbb Z\to\widehat{\mathbb Z}\to\epsilon\to0$ along
  $\mathbb Z\to\mathbb Q$ gives the finite-adele extension
  $0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0$.
- **Borel level.** Strict integral marking is rigid; forgetting it leaves the
  Levi $\mathbb Q^\times$; the full
  $\mathbb Q^\times\ltimes\epsilon$ appears only in the hyperbolic realization
  $H=\epsilon\oplus\mathbb Q$.
- **Gauge invariance.** Changing Guaspari-Solovay witness choices changes
  representatives, sections, and finite Loeb lifts by coboundaries, but it
  preserves the torsor class, finite conductor restrictions, radical support,
  and finite-adele extension line.

## Machine Verification

`code/scripts/check-pass89.py` produced
`artifacts/reports/pass89-borel-torsor-rosser-phantom-check.json` with overall
PASS.  It checks finite Cech windows where representatives change but classes
are preserved, affine Borel shadows
$(\mathbb Z/N)^\times\ltimes\mathbb Z/N$, singleton strict marked
stabilizers, and the invariant/non-invariant split under witness changes.

## Next Use

Pass 90 should make this torsor theorem functorial across conductor and
radical maps, comparing $m$-adic variants with the all-prime
$\epsilon$ case in one natural diagram.
