# Tagged Restricted Pro-Ab Realization

Date: 2026-06-11

## Summary

Pass 74 tests the first concrete external realization of
$\mathcal H_\epsilon$.

The target is the tagged restricted pro-Ab certificate category

$$
\mathcal R_\epsilon
=
\mathbf{Pro}^{\mathrm{rp}}_{\mathrm{tag}}(\mathbf{Ab}_{\mathrm{fin}})
\times
\mathbf{Pro}_{\mathrm{tag}}(\mathbf{Ab}).
$$

This is not yet an LCA-sheaf or condensed realization.  It is a concrete
finite/pro target used to test faithfulness on the five generator families.

## Realization Functor

The functor

$$
\rho_{\mathrm{tag}}:\mathcal H_\epsilon\to\mathcal R_\epsilon
$$

sends:

- finite conductor windows to tagged finite abelian group presentations with
  support tag $S$, conductor tag $k$, elementary divisors $(p,2k)$, and lattice
  divisors $(p,k)$;
- Loeb-Rosser boundaries $d_S$ to tagged integer matrices;
- restrictions $S\subseteq S'$ to tagged coordinate-restriction matrices;
- signed duality to $-d_S^T$;
- lcm kernel stages $K_n=N_n\mathbb Z$ to tagged pro-stages $(n,N_n)$.

## Result

On the checked finite/pro window, $\rho_{\mathrm{tag}}$ is faithful on all five
generator families:

1. finite conductor windows;
2. Loeb-Rosser boundaries;
3. restrictions;
4. signed duality;
5. derived pro-Ab lcm stages.

The corresponding plain tag-forgetting target is not faithful.  Restriction
source supports collide after forgetting source tags, and repeated lcm stages
collide after forgetting stage tags.

## Verification

The checker
`code/scripts/check-pass74.py` produces
`artifacts/reports/pass74-tagged-proab-realization-check.json`.

It verifies:

- 75 generators through six primes, conductors $k\le3$, and lcm stages through
  $N_{24}$;
- zero collisions for tagged signatures;
- family faithfulness for all five generator families;
- collisions in the plain tag-forgetting comparison;
- signed-dual double-dual compatibility.

The remaining problem is to make the tags intrinsic: support and stage data
should become genuine structure in an LCA-sheaf, condensed/solid, or canonical
exact pro-category target, or else a no-go theorem should explain why this
cannot be done.
