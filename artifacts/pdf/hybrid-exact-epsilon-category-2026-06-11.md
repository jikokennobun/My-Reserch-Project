# Hybrid Exact Category for the All-Prime Epsilon Class

Date: 2026-06-11

## Summary

Pass 72 defines a candidate bookkeeping category
$\mathcal H_\epsilon$ for the all-prime Loeb-Rosser class
$\epsilon_{\mathbb P}$.

The point is to keep two pieces of information simultaneously:

1. finite conductor restricted-product support;
2. the derived pro-Ab diagonal quotient
   $\widehat{\mathbb Z}/\mathbb Z$.

This avoids two false simplifications:

- treating $\widehat{\mathbb Z}/\mathbb Z$ as an ordinary Hausdorff LCA
  quotient;
- replacing all-prime product support by finite-support characters.

## The Candidate Category

An object of $\mathcal H_\epsilon$ has finite shadows

$$
(S,k,W_{S,k},L_{S,k},d_S),
$$

where $S$ is a finite prime set, $k\ge1$,

$$
W_{S,k}
=
\prod_{p\in S}
(p^{-k}\mathbb Z_p/p^k\mathbb Z_p),
$$

and

$$
L_{S,k}
=
\prod_{p\in S}
(\mathbb Z_p/p^k\mathbb Z_p).
$$

The boundary is

$$
d_S:\mathbb Z^S\to\mathbb Z^{|S|-1},
\qquad
d_S(x)=(x_p-x_{p_0})_{p\ne p_0}.
$$

The second layer is the lcm kernel tower

$$
K_n=N_n\mathbb Z,
\qquad
N_n=\operatorname{lcm}(1,\ldots,n).
$$

## Hybrid Exactness

A sequence is hybrid-exact if:

- all finite conductor shadows are exact;
- the pro layer is interpreted through $R^1\varprojlim$ and supplies

$$
\varprojlim\nolimits^1K_n
\cong
\widehat{\mathbb Z}/\mathbb Z.
$$

The candidate duality is

$$
\mathbb D_{\mathcal H}(d_S)=-d_S^T.
$$

The pro layer is retained as derived pro-Ab data, not as a Hausdorff quotient.

## Verification

The checker
`code/scripts/check-pass72.py` produces
`artifacts/reports/pass72-hybrid-exact-epsilon-category-check.json`.

It verifies:

- exact finite shadows for $|S|=1,\ldots,6$;
- primitive signed-dual images;
- restriction composition for all chains among the first six primes;
- signed-dual compatibility with those restrictions;
- conductor-layer bookkeeping through $k=1,2,3$;
- lcm-tower cofinality for moduli up to $24$;
- non-Mittag-Leffler growth of the lcm kernel tower.

The remaining problem is external validation: prove a universal property for
$\mathcal H_\epsilon$, or embed it faithfully into LCA sheaves,
condensed/solid abelian groups, or an exact pro-category with
restricted-product generators.
