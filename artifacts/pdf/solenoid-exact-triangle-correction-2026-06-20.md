# Solenoid Exact-Triangle Correction

Date: 2026-06-20

## Summary

Pass 83 corrects the exact-row comparison between the full adelic solenoid
$$
\Sigma=(\mathbb R\times\widehat{\mathbb Z})/\mathbb Z\cong\mathbb A/\mathbb Q
$$
and the finite phantom
$$
\epsilon=\widehat{\mathbb Z}/\mathbb Z.
$$
Projection to the real circle has kernel $\widehat{\mathbb Z}$, not
$\epsilon$.  The phantom appears instead as the quotient of $\Sigma$ by the
dense real line.

## Correct Rows

The compact Hausdorff solenoid row is
$$
0\to\widehat{\mathbb Z}\to\Sigma\to\mathbb R/\mathbb Z\to0.
$$
The finite-prime phantom row is the dense quotient
$$
\mathbb R\to\Sigma\to\epsilon=\widehat{\mathbb Z}/\mathbb Z\to0.
$$
Thus $\epsilon$ is not a closed subgroup of $\Sigma$ and should not be called
the kernel of $\Sigma\to\mathbb R/\mathbb Z$.

## Nonsplitting

The compact row does not split continuously.  Its Pontryagin dual is
$$
0\to\mathbb Z\to\mathbb Q\to\mathbb Q/\mathbb Z\to0,
$$
and this row cannot split because any section
$\mathbb Q/\mathbb Z\to\mathbb Q$ would send torsion to torsion in
$\mathbb Q$, which is torsion-free.

## Fourier Boundary

Global characters $\widehat{\Sigma}\cong\mathbb Q$ restrict to the closed
profinite kernel as
$$
\mathbb Q\to\mathbb Q/\mathbb Z.
$$
Only the trivial finite character descends further to
$\epsilon=\widehat{\mathbb Z}/\mathbb Z$, because descent requires killing the
dense diagonal copy of $\mathbb Z$.  The finite-prime Fourier content is
therefore a boundary quotient $\mathbb Q/\mathbb Z$, not a degree-zero
Whittaker or Fourier character of $\epsilon$.

## Machine Verification

`code/scripts/check-pass83.py` produced
`artifacts/reports/pass83-solenoid-exact-triangle-correction-check.json` with
overall PASS.  It checks finite dual rows
$0\to\mathbb Z\xrightarrow{\times N}\mathbb Z\to\mathbb Z/N\to0$, the
nonsplitting obstruction for nontrivial $N$, finite character descent, and the levelwise-zero
cokernel that forces $\epsilon$ to be read as derived/non-Hausdorff phantom
data.

## Next Use

The next pass should formulate the derived/solid exact triangle behind
$\mathbb R\to\Sigma\to\epsilon$ and identify the boundary object
$\mathbb Q/\mathbb Z$ as the precise replacement for the missing finite-prime
Weyl flip.
