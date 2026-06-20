# Shear Pushout Universal Property

Date: 2026-06-21

## Summary

Pass 86 states the correct universal property of the finite-adele shear
extension
$$
C_{\mathbb Q}=[\mathbb Q\to\mathbb A_f].
$$
It is the pushout of
$$
C_{\mathbb Z}=[\mathbb Z\to\widehat{\mathbb Z}]
$$
along $\mathbb Z\hookrightarrow\mathbb Q$ and is initial among
shear-marked quotient models with uniquely divisible, i.e. $\mathbb Q$-linear,
kernel.

## Main Claims

- **Initial pushout.** If
  $0\to D\to E\to\epsilon\to0$ is a shear-marked model receiving
  $C_{\mathbb Z}$ and $D$ is uniquely divisible, then the map
  $\mathbb Z\to D$ extends uniquely to $\mathbb Q\to D$.  Hence the model
  factors uniquely through $C_{\mathbb Q}$.
- **Finite-shadow stability.** The pushout does not create ordinary finite
  cokernels: integer residues already cover every checked finite quotient, so
  finite/Hausdorff shadows remain acyclic.
- **Torsion caveat.** The naive statement for arbitrary divisible kernels is
  false.  The maps
  $$
  \mathbb Q\to\mathbb Q/\mathbb Z,\qquad q\mapsto kq\bmod\mathbb Z
  $$
  restrict identically on $\mathbb Z$ but differ on fractions.  Thus torsion
  divisible summands must be excluded or given extra shear data.

## Machine Verification

`code/scripts/check-pass86.py` produced
`artifacts/reports/pass86-shear-pushout-universal-property-check.json` with
overall PASS.  It checks bounded denominator localizations, finite residue
acyclicity, unique factorization through checked $\mathbb Q$-vector targets,
and the $\mathbb Q/\mathbb Z$ counterexample to naive divisible-kernel
initiality.

## Next Use

Pass 87 should upgrade this finite certificate to a mapping-space statement in
$D(\mathrm{Solid})$, identifying the homotopy fiber of shear-marked maps out of
$C_{\mathbb Q}$ and deciding how torsion-divisible summands are excluded or
decorated.
