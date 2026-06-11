# Presentation-Level Universal Property of H-epsilon

Date: 2026-06-11

## Summary

Pass 73 proves the universal property currently available for
$\mathcal H_\epsilon$.

The result is deliberately limited: it is a presentation-level universal
property among support-preserving certificate targets.  It is not yet a
faithful embedding into LCA sheaves, condensed/solid abelian groups, or a
canonical exact pro-category.

## Certificate Targets

A support-preserving certificate target for $\epsilon_{\mathbb P}$ supplies
images of five generator families:

1. finite conductor windows $W_{S,k}$ and lattices $L_{S,k}$;
2. Loeb-Rosser boundaries $d_S$;
3. restriction maps for finite prime inclusions;
4. signed duality maps $d_S\mapsto -d_S^T$;
5. the derived pro-Ab lcm tower $K_n=N_n\mathbb Z$.

It is admissible when these images satisfy the finite/pro relations already
checked for $\mathcal H_\epsilon$: finite exactness, restriction composition,
signed-dual compatibility, conductor bookkeeping, and non-Mittag-Leffler pro
growth.

## Universal Property

Since $\mathcal H_\epsilon$ is presented by exactly these generators and
relations, every admissible support-preserving certificate target $C$ receives
a unique generator-preserving functor

$$
\mathcal H_\epsilon\to C.
$$

Thus $\mathcal H_\epsilon$ is initial among admissible support-preserving
certificate targets.

## Minimality

Each generator family is necessary:

- without conductor windows, local support-preserving duality is untyped;
- without boundaries $d_S$, the finite class $\epsilon_S$ is undefined;
- without restrictions, finite shadows do not assemble to
  $\epsilon_{\mathbb P}$;
- without signed duality, the functional equation is untyped;
- without the lcm tower, finite CRT levels remain zero and
  $\widehat{\mathbb Z}/\mathbb Z$ is lost.

## Verification

The checker
`code/scripts/check-pass73.py` produces
`artifacts/reports/pass73-h-epsilon-universal-property-check.json`.

It verifies:

- finite conductor normal forms through six primes and $k\le3$;
- pro normal forms through $N_{24}$;
- restriction and signed-dual relations;
- lcm-tower cofinality and non-Mittag-Leffler growth;
- unique generator-preserving functors into admissible targets;
- obstruction witnesses for targets omitting any generator family.

The remaining problem is external realization: construct a faithful exact
functor from $\mathcal H_\epsilon$ into LCA sheaves, condensed/solid groups, or
an exact pro-category with restricted-product generators, or prove a no-go
theorem for such a realization.
