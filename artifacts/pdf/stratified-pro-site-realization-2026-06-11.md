# Finite-Prime Stratified Pro-Site Realization

Date: 2026-06-11

## Summary

Pass 76 builds the first *natural* model for the Pass-75 support and stage
projectors $e_p, q_n$, replacing the abstract idempotents by geometric
operations on a stratified pro-site.

The model is

$$
\mathrm{StratPro}_\epsilon(U,N),
$$

where $U=\{2,3,5,7,11,13\}$ is the checked prime universe carried as a finite
discrete (Stone) space and $N$ is the lcm truncation depth. It is still a
finite-window certificate model, not yet an LCA-sheaf or condensed realization.

## Geometric Projectors

- **Clopen support projectors.** $e_p$ is multiplication by the characteristic
  function $\mathbf 1_{\{p\}}$ of the clopen stratum $\{p\}\subseteq U$, so that
  $e_S=(\cdot)\mathbf 1_S$ and the Boolean relation becomes pointwise idempotent
  multiplication:
  $$
  e_Se_T=(\cdot)\,\mathbf 1_S\mathbf 1_T=(\cdot)\,\mathbf 1_{S\cap T}=e_{S\cap T}.
  $$

- **Pro-stage truncation projectors.** $q_n$ is the prefix truncation of the
  non-Mittag-Leffler lcm tower $K_m=N_m\mathbb Z$ at stage $n$, with
  $q_nq_m=q_{\min(n,m)}$. The truncations remain cofinal, so the derived datum
  $\varprojlim^1 K_m\cong\widehat{\mathbb Z}/\mathbb Z$ survives in the limit.

## Site Factorization

The projector realization factors through the site:

$$
\rho_{\mathrm{proj}}=(\text{forget site})\circ\rho_{\mathrm{site}},\qquad
\rho_{\mathrm{site}}:\mathcal H_\epsilon\to\mathrm{StratPro}_\epsilon(U,N).
$$

**Theorem 76b (site factorization and faithfulness).** On the checked window,
$\rho_{\mathrm{site}}$ is faithful on all five generator families: the site
signature separates the $75$ generators with zero collisions, whereas the plain
tag-forgetting signature collapses them to $50$.

**Theorem 76c (clopen and stage relations).** The clopen support projectors
realize the finite Boolean algebra of strata ($4160$ verified $e_Se_T=e_{S\cap T}$
instances); the stage projectors realize the prefix-truncation chain ($576$
verified $q_nq_m=q_{\min(n,m)}$ instances). The separation is forced exactly at
the plain target's collisions, including repeated lcm stages $N_n=N_{n+1}$ (e.g.
$N_5=N_6=60$, $N_{13}=N_{14}=N_{15}=360360$) distinguished only by the stage
index $n$.

## Machine Verification

`code/scripts/check-pass76.py` ->
`artifacts/reports/pass76-stratified-pro-site-realization-check.json` (overall
PASS): $75$ generators across the five families tested through six primes,
$k\le3$, and lcm stages through $N_{24}$; site and projector global injectivity
each with zero collisions while the plain target has $12$; site family
faithfulness passing on all five families; $4160$ clopen Boolean support
relations and $576$ stage-filtration relations all passing; the factorization of
$\rho_{\mathrm{proj}}$ certified on the window.

## Limit of the Pass

The support and stage projectors now have a genuine geometric reading, but only
on a finite discrete prime universe with a truncated tower. The remaining
problem is to upgrade $\mathrm{StratPro}_\epsilon(U,N)$ to an all-prime derived
exact target -- an LCA sheaf on the profinite prime space, a condensed/solid
abelian object, or a canonical exact pro-category -- and to prove the signed
duality law $D_{\mathrm{res}}(\epsilon_{\mathbb P})=-\epsilon_{\mathbb P}^{\vee}$
there as a genuine all-prime theorem, or to exhibit the derived/non-Hausdorff
barrier that blocks it.
