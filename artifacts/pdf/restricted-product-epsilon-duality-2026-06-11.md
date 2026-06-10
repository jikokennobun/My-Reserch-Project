# Restricted-Product Epsilon Duality

Date: 2026-06-11

## Summary

Pass 71 formulates the all-prime signed duality statement for the
Loeb-Rosser class without treating
$\widehat{\mathbb Z}/\mathbb Z$ as an ordinary Hausdorff locally compact
quotient.

The all-prime object is

$$
\epsilon_{\mathbb P}
=
\{\epsilon_S\}_{S\subset\mathbb P,\ |S|<\infty}
$$

together with the derived pro-cokernel

$$
\varprojlim\nolimits^1(N_n\mathbb Z)
\cong
\widehat{\mathbb Z}/\mathbb Z.
$$

For finite $S$, each shadow remains the Pass-70 extension

$$
0\to
\mathbb Z^S/\Delta\mathbb Z
\to
\widehat{\mathbb Z}_S/\mathbb Z
\to
\prod_{p\in S}(\mathbb Z_p/\mathbb Z)
\to0.
$$

## Support-Preserving Duality

The ordinary dual of an infinite product only sees finite-support continuous
characters.  Therefore the all-prime duality cannot be stated as a bare product
duality.

Instead, it must use restricted products with conductor and lattice data:

$$
\prod_p'(A_p,L_p).
$$

At conductor $k$, the local finite window is

$$
p^{-k}\mathbb Z_p/p^k\mathbb Z_p,
$$

and the integral lattice

$$
\mathbb Z_p/p^k\mathbb Z_p
$$

is self-annihilating under the normalized conductor pairing.

## Signed Law

Choose a base prime $p_0\in S$.  The finite boundary is

$$
d_S(x)=(x_p-x_{p_0})_{p\ne p_0}.
$$

The all-prime statement

$$
D_{\mathrm{res}}(\epsilon_{\mathbb P})
=
-\epsilon_{\mathbb P}^{\vee}
$$

means that every finite prime/conductor shadow satisfies

$$
D(d_S)=-d_S^T,
$$

duality squared returns $d_S$, and all finite-prime restriction squares
commute.

This is a pro-restricted finite-shadow theorem.  It is not yet a full proof in
a selected LCA-sheaf, condensed, solid, or hybrid exact category.

## Verification

The checker
`code/scripts/check-pass71.py` produces
`artifacts/reports/pass71-restricted-product-epsilon-duality-check.json`.

It verifies that:

- finite boundary matrices commute with prefix restriction through six primes;
- signed transposes commute with the same restrictions;
- conductor windows for $p=2,3,5,7$ and $k=1,2$ have self-annihilating
  integral lattices;
- finite-prefix support counts separate restricted-product product profiles
  from bounded finite-support dual profiles.

The remaining problem is categorical: construct the ambient exact category and
prove that this finite-shadow law is an actual all-prime duality theorem there.
