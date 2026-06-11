# Intrinsic Projector Realization

Date: 2026-06-11

## Summary

Pass 75 replaces the explicit support and stage tags from the tagged
restricted pro-Ab realization by internal projectors.

The new target is still a certificate target, not yet an LCA-sheaf or
condensed realization.  The progress is that support and stage data are no
longer external labels.

## Projectors

Support is encoded by commuting Boolean idempotents $e_p$:

$$
e_S=\prod_{p\in S}e_p,
\qquad
e_Se_T=e_{S\cap T}.
$$

The lcm tower stage is encoded by projectors $q_n$:

$$
q_nq_m=q_{\min(n,m)}.
$$

The realization

$$
\rho_{\mathrm{proj}}:\mathcal H_\epsilon\to
\mathcal R_\epsilon^{\mathrm{proj}}
$$

sends finite conductor windows, Loeb-Rosser boundaries, restrictions, signed
duals, and lcm stages to finite/pro abelian data equipped with these projector
actions.

## Result

The projector-enriched realization is faithful on the five generator families
in the checked finite/pro window.

The plain target that forgets projector actions is still not faithful.  Thus
the support and stage structure are mathematically necessary.

A companion no-go checker is also integrated: ordinary exact 1-category
realization is insufficient because the
$\widehat{\mathbb Z}/\mathbb Z$ term is recovered by $R^1\varprojlim$, not by a
finite exact cone.

## Verification

The main checker
`code/scripts/check-pass75.py` produces
`artifacts/reports/pass75-intrinsic-projector-realization-check.json`.

It verifies:

- 75 projector-enriched generators through six primes, $k\le3$, and $N_{24}$;
- zero collisions for projector signatures;
- 12 collisions in the plain target;
- Boolean support-projector relations;
- 576 stage-projector relations;
- restriction source/target recovery by projector action.

The integrated companion checker
`code/scripts/check-pass73-exact-obstruction.py` produces
`artifacts/reports/pass73-exact-realization-obstruction-check.json` and records
the ordinary exact-category obstruction.

The next task is to realize $e_p$ and $q_n$ naturally in an established target:
for example as support projectors on a finite-prime stratified site and a
derived pro-stage filtration carrying $\varprojlim^1$.
