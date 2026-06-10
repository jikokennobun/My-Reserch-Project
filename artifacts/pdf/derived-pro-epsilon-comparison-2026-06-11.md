# Derived Pro-Cokernel and the Recollement Class

Date: 2026-06-11

## Summary

Pass 70 compares two presentations of the Loeb-Rosser phantom:

1. the derived pro-cokernel from the inverse-limit exact sequence;
2. the recollement extension class $\epsilon_S$ from the Loeb-Rosser
   bicomplex/six-functor package.

For a finite prime set $S$, define

$$
M_{S,k}=\prod_{p\in S}p^k.
$$

The levelwise sequence

$$
0\to M_{S,k}\mathbb Z\to\mathbb Z\to\mathbb Z/M_{S,k}\mathbb Z\to0
$$

gives

$$
\varprojlim_k \mathbb Z/M_{S,k}\mathbb Z
=
\widehat{\mathbb Z}_S
=
\prod_{p\in S}\mathbb Z_p,
$$

and therefore

$$
\varprojlim\nolimits^1(M_{S,k}\mathbb Z)
\cong
\widehat{\mathbb Z}_S/\mathbb Z.
$$

## The Comparison

The natural projection from the global derived pro-cokernel to the product of
local derived cokernels is

$$
\widehat{\mathbb Z}_S/\mathbb Z
\longrightarrow
\prod_{p\in S}(\mathbb Z_p/\mathbb Z).
$$

Its kernel is made of tuples represented by ordinary integers in each
coordinate, modulo the single diagonal integer:

$$
\ker =
\mathbb Z^S/\Delta\mathbb Z
\cong
\mathbb Z^{|S|-1}.
$$

Hence the extension

$$
0\to
\mathbb Z^S/\Delta\mathbb Z
\to
\widehat{\mathbb Z}_S/\mathbb Z
\to
\prod_{p\in S}(\mathbb Z_p/\mathbb Z)
\to0
$$

is exactly the recollement class $\epsilon_S$.

## Signed Shadow

After choosing a base prime $p_0\in S$, the boundary matrix is

$$
d_S:\mathbb Z^S\to\mathbb Z^{|S|-1},
\qquad
d_S(x)=(x_p-x_{p_0})_{p\ne p_0}.
$$

It has kernel $\Delta\mathbb Z$ and is surjective.  On finite-prime,
character-normalized shadows, duality sends

$$
d_S\mapsto -d_S^T,
$$

so

$$
D_{\mathrm{ch}}(\epsilon_S)=-\epsilon_S^\vee.
$$

## Verification

The checker
`code/scripts/check-pass70.py` produces
`artifacts/reports/pass70-derived-pro-epsilon-comparison-check.json`.

It verifies for $|S|=1,\ldots,5$ that:

- CRT finite shadows for $M_{S,k}$, $1\le k\le4$, are bijective;
- $\Delta:\mathbb Z\to\mathbb Z^S$ is primitive;
- $d_S:\mathbb Z^S\to\mathbb Z^{|S|-1}$ is surjective;
- $\ker d_S$ is the diagonal by rank;
- $-d_S^T$ double-dualizes back to $d_S$.

The remaining open problem is not the algebraic comparison.  It is the
all-prime topological duality normalization: formulate the restricted-product
LCA, condensed, or solid category in which the finite signed laws assemble
without collapsing products to finite-support direct sums.
