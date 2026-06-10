# Consistency/Cut Layer for G2-ZOO

Date: 2026-06-11

## Summary

Pass 69 adds a named APS-level consistency layer to G2-ZOO.  For an
AMS/preAPS

$$
S=(L,\le,\Box,\boxtimes,T,\bot),
$$

define the iterated consistency tower

$$
C_0=T,\qquad C_{n+1}=\boxtimes C_n.
$$

The new statement names are:

- $\mathrm{Con}^{\mathrm{orb}}_n$: $C_n\nleq\bot$.
- $\mathrm{G2}_n$: $C_n\le\bot\Rightarrow T\le\bot$.
- $\mathrm{FG2}_n$: $C_{n+1}\le C_n$, equal to $\mathrm{nFG2}(n)$.
- $\mathrm{Flat}_{\le N}$: distinct values among $C_0,\ldots,C_N$ are pairwise
  incomparable.
- `CutA3`: $x\le\Box y$ and $x\le\boxtimes y$ imply $x\le\boxtimes T$.

`CutA3` is APS axiom A3 read as a cut/collision consistency principle.

## Machine-Checked Families

The checker `code/scripts/check-pass69.py` verifies two families.

First, the cycle models $C_m$ for $2\le m\le12$ are genuine APS models.  Their
middle orbit is an antichain cycle, so the consistency tower is flat at the
level of distinct orbit values.  They have no syntactic $\boxtimes$-fixed point,
G2 holds vacuously, and every checked $\mathrm{nFG2}(k)$ fails.

Second, the detached Rosser period models $R_{2k}$ for $1\le k\le6$ add a
middle atom $p$ with $\boxtimes p=p$.  They preserve A1, A2, A4, G2, and the
flat consistency orbit, but fail A3 exactly at the detached collision
$x=y=p$:

$$
p\le\Box p,\qquad p\le\boxtimes p,\qquad p\nleq\boxtimes T.
$$

Thus primitive refutability fixed points do not by themselves imply formalized
descent or cut/collision closure.

## Open Arithmetic Lift

The order-theoretic certificate should not be read as an arithmetic theorem.
The next tasks are:

1. Interpret $C_n$ and $\mathrm{Con}^{\mathrm{orb}}_n$ inside $ConLat_T$.
2. Identify the arithmetic counterpart of `CutA3`, comparing $Con_T^S$,
   $Con_T^H$, Rosser consistency, local reflection, and cut admissibility.
3. Decide whether residuation, integrality, and contraction force the detached
   Rosser fixed point of $R_{2k}$ back into the consistency orbit.
4. Separately return to the Pass-68 problem of comparing
   $\varprojlim^1(N_n\mathbb Z)$ with the recollement class $\epsilon$.

Detailed note:
`research/notes/g2-zoo-consistency-cut-infinite-pass69.md`

Checker report:
`artifacts/reports/pass69-consistency-cut-infinite-g2-zoo-check.json`
