# Mapping-Space Shear Initiality

Date: 2026-06-21

## Summary

Pass 87 upgrades the finite-adele shear-pushout universal property to a derived
mapping-space statement.  For a shear-marked target
$$
M=(0\to D\to E\to\epsilon\to0),
$$
the restriction map
$$
\operatorname{Map}(C_{\mathbb Q},M)\to
\operatorname{Map}(C_{\mathbb Z},M)
$$
has homotopy fiber
$$
\mathbf R\operatorname{Map}(\mathbb Q/\mathbb Z,D),
$$
because the cofiber of $\mathbb Z\to\mathbb Q$ is $\mathbb Q/\mathbb Z$.

## Main Claims

- **Fiber formula.** The obstruction to extending a shear-marked map from
  $C_{\mathbb Z}$ to $C_{\mathbb Q}$ is exactly
  $\mathbf R\operatorname{Map}(\mathbb Q/\mathbb Z,D)$.
- **Contractible uniquely divisible case.** If $D$ is uniquely divisible, then
  $\operatorname{Hom}(\mathbb Q/\mathbb Z,D)=0$ and higher Ext obstructions
  vanish, so the fiber is contractible.
- **Torsion decoration.** If $D$ has torsion-divisible summand $T$, then
  $\mathbf R\operatorname{Map}(\mathbb Q/\mathbb Z,T)$ contributes extra
  components.  Strict initiality either excludes $T$ or decorates the model by
  choosing this boundary component.

## Machine Verification

`code/scripts/check-pass87.py` produced
`artifacts/reports/pass87-mapping-space-shear-initiality-check.json` with
overall PASS.  It records the cofiber/fiber sequence, verifies contractible
finite torsion tests for $\mathbb Q$-vector kernels, and shows that a
rank-$r$ torsion-divisible finite shadow has $N^r$ boundary components at
modulus $N$.

## Next Use

Pass 88 should compute the derived automorphism/stabilizer of the final
finite-adele shear extension and compare it with the solid Borel
$\mathbb Q^\times\ltimes\epsilon$.
