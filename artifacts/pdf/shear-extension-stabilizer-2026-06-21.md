# Shear Extension Stabilizer

Date: 2026-06-21

## Summary

Pass 88 computes the stabilizer of the final finite-adele shear extension
$$
0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0
$$
and separates it from the full solid Borel
$\mathbb Q^\times\ltimes\epsilon$.

## Main Claims

- **Strict marked rigidity.** As an object under
  $C_{\mathbb Z}\to C_{\mathbb Q}$, the extension has trivial automorphism
  group.  The marked integral unit forces scalar $1$, and Pass 87 removes
  derived ambiguity for the $\mathbb Q$-kernel.
- **Extension-line stabilizer.** Forgetting the integral marking but preserving
  the finite-adele Ext line leaves stabilizer $\mathbb Q^\times$, acting by
  nonzero rational scalars.
- **Borel comparison.** The full Borel $\mathbb Q^\times\ltimes\epsilon$ is
  recovered only at the hyperbolic-plane level
  $H=\epsilon\oplus\mathbb Q$, where $\epsilon$ is the unipotent shear
  parameter rather than an endpoint-fixing automorphism of the bare exact row.

## Machine Verification

`code/scripts/check-pass88.py` produced
`artifacts/reports/pass88-shear-extension-stabilizer-check.json` with overall
PASS.  It checks rational scalar behavior, finite affine Borel shadows
$(\mathbb Z/N)^\times\ltimes\mathbb Z/N$, singleton strict unit stabilizers,
and absence of residual derived automorphisms after the torsion-boundary
decoration rule.

## Next Use

Pass 89 should consolidate Passes 80-88 as a Borel-torsor / extension-class
theorem for the Rosser phantom and state the bridge back to the APS/Rosser
unit-torsor line.
