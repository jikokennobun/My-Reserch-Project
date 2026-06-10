# Restricted-Product Adelic Duality and the Loeb-Rosser Phantom

Date: 2026-06-11

## Abstract

Pass 67 checks finite conductor shadows of the restricted product
$$\mathbb A_f=\prod_p'(\mathbb Q_p,\mathbb Z_p).$$
The finite local pieces have the expected self-duality, but the phantom
$\widehat{\mathbb Z}/\mathbb Z$ is not visible at any fixed finite conductor level.  It must be
treated as a derived/pro quotient.

## Main Result

For a prime $p$ and conductor $k\ge1$, use
$$p^{-k}\mathbb Z_p/p^k\mathbb Z_p\cong\mathbb Z/p^{2k}\mathbb Z$$
with pairing
$$\langle x,y\rangle=\frac{xy}{p^{2k}}\in\mathbb Q/\mathbb Z.$$
The integral lattice $\mathbb Z_p/p^k\mathbb Z_p$ corresponds to
$p^k\mathbb Z/p^{2k}\mathbb Z$ and is self-annihilating.  Finite products of these local windows
remain self-dual.

In conductor-normalized coordinates, the Loeb-Rosser boundary still dualizes by signed transpose:
$$D(d_S)=-d_S^T,\qquad D^2(d_S)=d_S.$$

The obstruction appears at the diagonal quotient.  For each finite conductor
$N=\prod p^{e_p}$, CRT gives
$$\mathbb Z/N\mathbb Z\cong\prod_{p\mid N}\mathbb Z/p^{e_p}\mathbb Z.$$
So the finite-level quotient by the diagonal is zero.  The phantom
$\widehat{\mathbb Z}/\mathbb Z$ is therefore a limiting derived/pro phenomenon, not an ordinary
finite-stage quotient.

## Verification

The checker `code/scripts/check-pass67.py` generated
`artifacts/reports/pass67-restricted-product-adelic-duality-check.json`.

Verified facts:

- local conductor quotients for $p=2,3,5,7$ have nondegenerate pairings;
- the integral lattice is self-annihilating in each tested local window;
- finite product windows preserve the self-annihilating lattice;
- signed boundary transpose checks pass for $s=1,\ldots,7$;
- CRT diagonal maps are surjective for $N=6,12,90,420$.

## Remaining Gap

Pass 68 should choose the exact category for the quotient: pro-abelian derived cokernel,
condensed/solid quotient, or an exact-category extension class recovering the Loeb-Rosser
phantom from levelwise-zero finite quotients.
