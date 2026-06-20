# Metaplectic Borel No-Flip

Date: 2026-06-14

## Summary

Pass 80 tests whether the finite Weil/metaplectic symmetry descends to the
solid phantom. At every finite level the usual Weyl flip exists, but the
solid limit has no map $\epsilon\to\mathbb Q$. The surviving symmetry is only
the Borel group
$$
B=\mathbb Q^\times\ltimes\epsilon,
$$
the affine group preserving the $\epsilon$ polarization.

## Main Claims

- **Finite levels are fully symplectic.** For $\mathbb Z/N$, the group
  $\mathrm{SL}_2(\mathbb Z/N)$ has the expected Bruhat decomposition, Weyl
  element, and finite Fourier transform.
- **Limit wall.** The lower-left entry needed for the Weyl flip would be a
  solid morphism $\epsilon\to\mathbb Q$, but
  $\mathrm{Hom}_{\mathrm{Solid}}(\epsilon,\mathbb Q)=0$.
- **No metaplectic descent.** The finite Fourier transforms $F_N$ are unitary,
  satisfy $F_N^4=I$, and have Gauss sums of the expected norm, but their
  candidate limit lies in the vanished Hom group.

## Machine Verification

`code/scripts/check-pass80.py` produced
`artifacts/reports/pass80-metaplectic-borel-noflip-check.json` with overall
PASS. It verifies finite $\mathrm{SL}_2$ order/Bruhat identities, Weyl-flip
properties, the one-sided Hom tower, and the finite Weil transform checks.

## Next Use

The pass identifies the representation-theoretic wall for the next stage:
the phantom has an affine/Borel action, but no Weyl operator and hence no
self-dual Fourier functional equation.
