# Two-Term Boundary Complex

Date: 2026-06-20

## Summary

Pass 85 compares three two-term models for the finite-prime phantom boundary:
$$
C_{\mathbb Z}=[\mathbb Z\to\widehat{\mathbb Z}],\qquad
C_{\mathbb R}=[\mathbb R\to\Sigma],\qquad
C_{\mathbb Q}=[\mathbb Q\to\mathbb A_f],
$$
where
$$
\Sigma=(\mathbb R\times\widehat{\mathbb Z})/\mathbb Z,\qquad
\epsilon=\widehat{\mathbb Z}/\mathbb Z.
$$
All three complexes have quotient $\epsilon$, but they do not preserve the
same extension data.

## Main Claims

- **Same quotient.** Each complex has injective differential and
  $H^1\cong\epsilon$.
- **Finite/Hausdorff acyclicity.** At every finite modulus the diagonal image
  is all of $\mathbb Z/N$, so ordinary finite cokernels vanish.  Likewise,
  $\mathbb R$ is dense in $\Sigma$ and $\mathbb Q$ is dense in $\mathbb A_f$.
- **Shear-preserving pushout.** The comparison
  $C_{\mathbb Z}\to C_{\mathbb Q}$ is the pushout along
  $\mathbb Z\hookrightarrow\mathbb Q$ and preserves the finite-adele extension
  $$
  0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0.
  $$
  The archimedean row $C_{\mathbb R}$ has the same quotient but not this
  Borel shear class.

## Machine Verification

`code/scripts/check-pass85.py` produced
`artifacts/reports/pass85-two-term-boundary-complex-check.json` with overall
PASS.  It checks dense finite shadows, the non-Mittag-Leffler lcm kernel
tower, compatible unit residues, and the comparison table distinguishing the
shear-preserving finite-adele pushout from the archimedean row.

## Next Use

Pass 86 should state the universal property of
$C_{\mathbb Q}=[\mathbb Q\to\mathbb A_f]$: among quotient models of
$\epsilon$ with divisible kernel, it should be the initial receiver of
$C_{\mathbb Z}$ that preserves the unit/shear class and kills Hausdorff finite
cokernels.
