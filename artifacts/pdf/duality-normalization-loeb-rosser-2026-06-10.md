# Duality Normalization for the Loeb-Rosser Functional Equation

Date: 2026-06-10

## Abstract

Pass 66 refines the Pass 65 finite Verdier-dual equation
$$\mathbb D(\epsilon_S)=-\epsilon_S^\vee.$$
The finite matrix equation is stable, but the arithmetic-site lift depends on the choice of
duality.  This pass separates the finite-prime character-dual statement from the all-prime
restricted-product problem.

## Main Result

The unshifted $\mathbb Z$-linear dual is not the degree-preserving duality for the local cyclic
layers:
$$\operatorname{Hom}_{\mathbb Z}(\mathbb Z/n,\mathbb Z)=0,\qquad
\operatorname{Ext}^1_{\mathbb Z}(\mathbb Z/n,\mathbb Z)\cong\mathbb Z/n.$$
Thus $R\mathrm{Hom}_{\mathbb Z}(-,\mathbb Z)$ sees the local layers only after a cohomological
shift.

The finite-prime normalization is character duality
$$D_{\mathrm{ch}}(A)=\operatorname{Hom}(A,\mathbb Q/\mathbb Z),$$
for which
$$D_{\mathrm{ch}}(\mathbb Z/n)\cong\mathbb Z/n.$$
For finite $S$, products and direct sums agree, so the Pass 65 signed transpose calculation gives
$$D_{\mathrm{ch}}(\epsilon_S)=-\epsilon_S^\vee.$$

For $S=\mathbb P$, the naive bare product fails: continuous characters of an infinite product have
finite support, so the dual is a direct sum of local characters.  The full adelic statement must
therefore be formulated in a restricted-product / locally compact abelian setting.

## Verification

The checker `code/scripts/check-pass66.py` generated
`artifacts/reports/pass66-duality-normalization-scheme-lift-check.json`.

Verified facts:

- finite cyclic layers have trivial $\operatorname{Hom}(-,\mathbb Z)$ but nontrivial
  $\operatorname{Ext}^1(-,\mathbb Z)$ of the expected order;
- character duality preserves $\mathbb Z/p^k$ for $p=2,3,5,7$ and $k=1,\ldots,4$;
- finite boundary matrices dualize by signed transpose and square back;
- finite product/direct-sum orders agree;
- finite-prefix support counts witness the infinite product/direct-sum obstruction.

## Remaining Gap

Pass 67 should define the restricted-product coefficient for the full prime spectrum and check the
global sign of the boundary class in that topological category.
