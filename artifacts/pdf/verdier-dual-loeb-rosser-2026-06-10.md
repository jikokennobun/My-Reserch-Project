# Verdier-Dual Loeb-Rosser Recollement

Date: 2026-06-10

## Abstract

Pass 65 studies the second recollement triangle for the finite generic-point model
$X_S=\{\eta\}\sqcup\{(p):p\in S\}$ of the Loeb-Rosser dictionary.  Pass 64 used the triangle
$j_!j^*\to\mathrm{id}\to i_*i^*$.  This pass uses
$$i_*i^!\to\mathrm{id}\to Rj_*j^*,$$
and checks the finite Verdier-dual form of the mixed class $\epsilon_S$.

## Main Result

The $i^!$ / local-support spine is the two-term complex
$$\mathbb Z\xrightarrow{\Delta}\mathbb Z^S,\qquad 1\mapsto(1,\ldots,1).$$
Therefore
$$H^0(i^!)=0,\qquad H^1(i^!)\cong\operatorname{coker}\Delta\cong\mathbb Z^{|S|-1}.$$
So the Rosser horizontal lattice has both a $j_!$ presentation and an $i^!$ closed-support
presentation.

Let
$$d_S:\mathbb Z^S\to\mathbb Z^{|S|-1},\qquad (x_p)\mapsto(x_p-x_{p_0})_{p\ne p_0}$$
represent the recollement boundary / mixed class $\epsilon_S$.  On the finite matrix spine,
Verdier duality sends
$$d_S\longmapsto -d_S^T,$$
so the finite functional equation is
$$\mathbb D(\epsilon_S)=-\epsilon_S^\vee.$$
The sign is invisible over $\mathbb F_2$ but is visible over $\mathbb Z$ as an orientation datum of
the gluing triangle.

## Verification

The checker `code/scripts/check-pass65.py` generated
`artifacts/reports/pass65-verdier-dual-recollement-functional-equation-check.json`.

Verified facts:

- for $s=1,\ldots,7$, $\ker\Delta=0$ and $\operatorname{coker}\Delta$ has rank $s-1$;
- $d_S$ and $-d_S^T$ have the same rank $s-1$;
- duality squared returns $d_S$;
- the sign disappears modulo $2$;
- finite-prime restriction maps commute with both $d_S$ and the dual boundary.

## Remaining Gap

This is a finite Alexandrov-space computation.  The honest $\mathrm{Spec}\,\mathbb Z$ lift still
requires a dualizing normalization and a calculation of the duals of $\mathbb Z_p/\mathbb Z$ and
$\widehat{\mathbb Z}_S/\mathbb Z$, with product/direct-sum behavior tracked explicitly.
