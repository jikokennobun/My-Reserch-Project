# Degenerate Principal Series Functional-Equation Wall

Date: 2026-06-14

## Summary

Pass 81 interprets the Pass-80 Borel as a maximally degenerate principal
series. Since the solid symplectic group has collapsed to
$$
\mathrm{Sp}(H)=B=\mathbb Q^\times\ltimes\epsilon,
$$
the flag variety is a point and
$$
I(s)=\mathrm{Ind}_{B}^{\mathrm{Sp}(H)}\chi_s\cong\chi_s.
$$
There is no opposite unipotent cell and no standard intertwiner realizing
$s\leftrightarrow -s$.

## Main Claims

- **Flag collapse.** The finite groups still have nontrivial projective lines
  and Bruhat cells, but the solid limit has
  $\bar U=\mathrm{Hom}(\epsilon,\mathbb Q)=0$.
- **No functional equation.** The standard intertwiner
  $M(w,s):I(s)\to I(-s)$ would integrate over $\bar U$. Since $\bar U=0$ as
  the missing cross-polarization morphism, the solid representation has no
  nonzero Weyl-mediated functional equation.
- **Finite/limit dichotomy.** At every finite level the DFT conjugates
  dilation by $t$ to dilation by $t^{-1}$ and Gauss sums supply the local
  $c$-factor. The symmetry is destroyed only in the solid limit.

## Machine Verification

`code/scripts/check-pass81.py` produced
`artifacts/reports/pass81-degenerate-principal-series-functional-equation-check.json`
with overall PASS. It checks finite flag sizes, the DFT dilation identity,
Gauss-sum norms for primes through $23$, and the limit obstruction separating
the vanished flip tower from the nonzero shear tower.

## Next Use

The remaining automorphic residue is not a functional equation but a possible
constant-term or Whittaker-style functional. That is the question taken up in
Pass 82.
