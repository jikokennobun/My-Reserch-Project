# APS Cardinal Invariants and Fixed Point Spectrum

Source: https://chatgpt.com/share/6a0b7536-836c-83ab-ae90-5eb16748d05e

Imported from Research Project handoff: 2026-05-22

Rechecked from user-supplied shared-link batch: 2026-05-30

## Topic

APS and cardinal invariants such as $\lvert\mathrm{Fix}_{\boxtimes}(S)\rvert$.

## Working Summary

The fixed point set of $\boxtimes$ can be treated as an invariant of an APS. Classifying possible sizes and structures of fixed point sets may distinguish G2/FG2 behavior and finite/countable/non-countable models.

The 2026-05-30 batch confirms this note as the local home for the
`Fix_{\boxtimes}(S)` / fixed-point spectrum direction. No duplicate note was
created.

The refreshed share expands the idea from simple fixed-point counting to a
Tukey/relational-system reading of the G2-ZOO. A G2-style principle can often
be rewritten in the form

$$
\forall x\in X\,\exists y\in Y\,R(x,y),
$$

and then assigned a witness-family invariant

$$
\kappa(R)=
\min\{\lvert D\rvert:D\subseteq Y\text{ and }\forall x\in X\,\exists y\in D\,R(x,y)\}.
$$

This is the same abstract pattern as classical cardinal characteristics such as
the dominating number:

$$
\mathfrak d=\min\{\lvert D\rvert:D\subseteq \omega^\omega
\text{ and }\forall f\in\omega^\omega\,\exists g\in D\,f\le^* g\}.
$$

The share also sketches a "bouquet APS" construction: arbitrary relational
systems are represented by named Jeroslow fixed points, giving a route from
Tukey reductions to APS/G2-ZOO reductions.

## File References in Share

The shared conversation reports generated PDF/TeX artifacts named
`g2_zoo_cardinal_invariants.pdf` and `g2_zoo_cardinal_invariants.tex`.
The URLs shown there are `sandbox:/mnt/data/...` links from the ChatGPT session,
so they are not directly readable from this local repository environment. If
those files are exported to the Google Drive artifact inbox, they should be
imported with `code/scripts/sync-chatgpt-project-artifacts.ps1`.

## Next Tasks

- Define $\mathrm{Fix}_{\boxtimes}(S)$.
- List possible invariants: cardinality, order type, closure properties, definable subset.
- Build finite examples in `code/models/`.
- Formalize G2-ZOO relational systems and Tukey reductions.
- Reconstruct or import the referenced `g2_zoo_cardinal_invariants` PDF/TeX
  artifact when available.
