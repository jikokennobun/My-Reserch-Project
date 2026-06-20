# Whittaker Vanishing And Archimedean Repair

Date: 2026-06-14

## Summary

Pass 82 tests the residue of the maximally degenerate principal series
$$
I(s)=\chi_s
$$
under the unipotent radical $U=\epsilon$. Because $I(s)$ is trivial on $U$,
there are no nontrivial Whittaker functionals:
$$
\mathrm{Hom}_U(I(s),\psi)\cong
\begin{cases}
R,& \psi=1,\\
0,& \psi\ne 1.
\end{cases}
$$
Only the constant term survives.

## Main Claims

- **Whittaker vanishing.** Nontrivial finite additive characters exist at
  every level, but their coefficients against the constant $U_N$-action vanish.
  They do not survive as a solid Whittaker model for $I(s)$.
- **Rosser carrier.** The Rosser torsor is not a generic Whittaker
  coefficient. It is the unipotent shear parameter $U=\epsilon$ itself.
- **Archimedean repair.** Adding the real place gives the adelic solenoid
  $$
  \Sigma=(\mathbb R\times\widehat{\mathbb Z})/\mathbb Z\cong\mathbb A/\mathbb Q
  $$
  and, after the Pass 83 correction, the compact exact sequence
  $$
  0\to\widehat{\mathbb Z}\to\Sigma\to\mathbb R/\mathbb Z\to0.
  $$
  The finite phantom $\epsilon=\widehat{\mathbb Z}/\mathbb Z$ is the dense
  quotient $\Sigma/\mathbb R$, not the closed kernel of the projection to
  $\mathbb R/\mathbb Z$.
  This repairs global adelic Fourier duality, but it does not create a
  finite-prime solid morphism $\epsilon\to\mathbb Q$.

## Machine Verification

`code/scripts/check-pass82.py` produced
`artifacts/reports/pass82-whittaker-archimedean-repair-check.json` with overall
PASS. It checks vanishing of nontrivial finite Fourier coefficients, the
$U$-equivariant Hom dimension table, and finite shadows of the solenoid exact
sequence.

## Next Use

Pass 83 should compare the global solenoid $\Sigma$ with the finite phantom
$\epsilon$ as an exact triangle and decide whether global Fourier theory
restricts to only a constant term or also yields a boundary class measuring
the lost finite-prime Weyl flip.
