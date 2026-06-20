# Derived Solid Realization

Date: 2026-06-12

## Summary

Pass 77 corrects the target for the all-prime phantom
$$
\epsilon=\widehat{\mathbb Z}/\mathbb Z.
$$
The ordinary LCA route is too small: the dense diagonal image kills continuous
characters, so the LCA dual of $\epsilon$ is zero. The useful realization is
instead derived/solid. In that setting the profinite completion contributes a
degree shift:
$$
\widehat{\mathbb Z}^{\,*}\simeq(\mathbb Q/\mathbb Z)[-1],
$$
and the phantom survives as a derived object rather than as an ordinary exact
LCA quotient.

## Main Claims

- **LCA no-go.** Finite shadows show that the annihilator of the dense
  diagonal image is trivial at every checked lcm stage.
- **Solid degree shift.** For each finite stage $\mathbb Z/N$, Hom into
  $\mathbb Z$ vanishes while $\mathrm{Ext}^1(\mathbb Z/N,\mathbb Z)$ has order
  $N$.
- **Signed boundary law.** The finite boundary
  $d_S:\mathbb Z^S\to\mathbb Z^{|S|-1}$ has diagonal kernel, is surjective,
  and dualizes as $D(d_S)=-d_S^T$ with $D^2=\mathrm{id}$.

## Machine Verification

`code/scripts/check-pass77.py` produced
`artifacts/reports/pass77-derived-solid-realization-check.json` with overall
PASS. It checks the LCA annihilator no-go, the solid degree-one dual tower,
and the signed dual boundary law for support sets of sizes $2$ through $6$.

## Next Use

This pass fixes the ambient category for the later $\epsilon$ analysis:
subsequent symplectic, metaplectic, and automorphic statements must be read in
the derived/solid target, not in ordinary LCA groups.
