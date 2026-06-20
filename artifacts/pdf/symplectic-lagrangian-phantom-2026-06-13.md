# Symplectic Lagrangian Phantom

Date: 2026-06-13

## Summary

Pass 79 asks whether $\epsilon$ itself is a symplectic object. The corrected
answer is subtler: $\epsilon$ has a unique nonzero derived self-pairing, but
that pairing is degree-shifted, alternating, and degenerate. The right
nondegenerate finite picture is a hyperbolic pair with complementary
Lagrangians $\epsilon$ and $\mathbb Q$.

## Main Claims

- **No intrinsic Darboux form.** The candidate pairing
  $\epsilon\otimes\epsilon\to\mathbb Z[m]$ is nonzero only for $m=2$.
- **Finite-adele generator.** The extension
  $0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0$
  generates $\mathrm{Ext}^1_{\mathrm{Solid}}(\epsilon,\mathbb Q)$.
- **Alternating but degenerate.** The odd degree gives the swap sign $-1$, so
  the pairing is alternating. Its adjoint is not an isomorphism.
- **Hyperbolic correction.** Finite pairings
  $\mathbb Z/N\times\mathbb Z/N\to\mathbb Q/\mathbb Z$ are perfect; the
  symplectic object should be read as a hyperbolic plane with two
  complementary Lagrangians.

## Machine Verification

`code/scripts/check-pass79.py` produced
`artifacts/reports/pass79-symplectic-lagrangian-phantom-check.json` with
overall PASS. It checks vanishing of `RHom(Zhat,Q)`, the degree table for
self-pairings, the finite-adele extension class, the alternating sign, and the
Darboux/projector no-go.

## Next Use

This pass sets up the later metaplectic question: if $\epsilon$ and
$\mathbb Q$ are complementary Lagrangians, the decisive test is whether the
Weyl flip $\epsilon\to\mathbb Q$ survives in the solid limit.
