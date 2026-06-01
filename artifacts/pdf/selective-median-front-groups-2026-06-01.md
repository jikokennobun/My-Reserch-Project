---
title: "Selective Median Front Groups in Bottom-Disciplined B_N"
date: "2026-06-01"
---

# Selective Median Front Groups

This note summarizes autonomous discussion passes 36--38 of the APS/G2-ZOO
ledger. The setting is the bottom-disciplined $B_N$ family with APS orbit

$$
T\mapsto a_1\mapsto \cdots \mapsto a_{N+1}\mapsto s\mapsto s,
$$

true bottom $b$, helper top $U$, and the order relations $b\le x\le U$ plus
$s\le a_{N+1}$.

## Problem

The front $F_k=\{a_1,\ldots,a_k\}$ can carry orthogonal idempotents in the
front-shifted tensor, but same-order group fronts are rigid: the diagonal
residual fiber strands the incomparable pair $\{T,e_G\}$, where $T$ is the
global monoid unit and $e_G$ is the local group identity. With no additional
join below $U$, the fiber has no principal maximum.

## Capped Front

A full cap $c$ above the entire front does not repair the obstruction. In
$B_N^{\mathrm{cap}}$, antitonicity forces

$$
\boxtimes c=b,
$$

so the APS orbit profile is preserved. But monotonicity ejects the cap from the
relevant fibers: if $p\le c$ and $p\otimes p=p$, then

$$
p\otimes c\ge p\otimes p=p.
$$

For any target $t$ with $p\not\le t$, the cap cannot lie in
$\{x:p\otimes x\le t\}$. Hence ceilings above the whole front cannot repair
fibers whose obstruction sits at or below the front.

## Selective Median

The successful repair is the single selective median

$$
m=T\vee e_G,\qquad b,T,e_G\le m\le U,
$$

with $m$ incomparable to non-identity front atoms and the tail. For abelian
cyclic fronts $\mathbb Z/2,\ldots,\mathbb Z/5$, the checker
`code/scripts/check-selective-median-bound.py` verifies a commutative fully
residuated tensor in which

$$
a_j\backslash a_j=\{b,T,e_G,m\}
$$

has principal maximum $m$.

## Non-Abelian Test

Pass 38 drops commutativity and checks the smallest non-abelian front,
$F_6\cong S_3$. The tensor keeps the group product on the front, makes $m$ a
two-sided identity on front atoms, and sends front-tail, tail-front, median-tail,
tail-median, and nonzero $U$ interactions to $U$.

The report `artifacts/reports/noncommutative-selective-median-check.json`
verifies associativity, two-sided monotonicity, unit, and principality of every
left and right residual fiber. Both diagonal fibers are principal:

$$
a_j\backslash a_j=\{b,T,e_G,m\}=a_j/a_j,
$$

with maximum $m$. The forced antitone value remains $\boxtimes m=b$. The
no-median and full-cap controls fail with the predicted residual and
monotonicity obstructions.

## Current Conjecture

Every finite group $G$ should fit as the front of a two-residuated
$B_N^{\mathrm{med}}(G)$ after adjoining the single median $m=T\vee e_G$.
The remaining proof task is to write the uniform finite-group theorem:
associativity follows from the group block plus collapse blocks, while left and
right residuals follow from bijectivity of left and right translations in $G$.
