# Pass 69: Consistency/Cut/Infinite Layer for G2-ZOO

Date: 2026-06-11

This note adds a small but useful layer to G2-ZOO: named APS-level
consistency statements, second-incompleteness variants, a cut/A3 boundary, and
finite certificates for infinite-model phenomena.  The arithmetic reading is
kept explicit but provisional; the machine-checked part is order-theoretic.

## 1. Iterated APS Consistency Tower

For an AMS/preAPS

$$
S=(L,\le,\Box,\boxtimes,T,\bot),
$$

define the consistency tower

$$
C_0:=T,\qquad C_{n+1}:=\boxtimes C_n.
$$

The following names are now used in G2-ZOO.

| Name | APS statement | Reading |
| --- | --- | --- |
| $\mathrm{Con}^{\mathrm{orb}}_n$ | $C_n\nleq\bot$ | the $n$th iterated consistency assertion is not refutable |
| $\mathrm{G2}_n$ | $C_n\le\bot\Rightarrow T\le\bot$ | $n$th second-incompleteness implication |
| $\mathrm{FG2}_n$ | $C_{n+1}\le C_n$ | formalized descent at level $n$; this is $\mathrm{nFG2}(n)$ |
| $\mathrm{Flat}_{\le N}$ | $C_i,C_j$ are incomparable for checked $0\le i<j\le N$ | no finite consistency iterate has stabilized or descended |
| $\mathrm{CutA3}$ | $x\le\Box y$ and $x\le\boxtimes y$ imply $x\le C_1$ | no provability/refutability collision survives cut closure |

The old arithmetic statements still sit above this layer:
$Con_T^L$ is closest to the single assertion $C_1=\boxtimes T$;
$Con_T^G$ is existential and is better modeled by a family of non-provability
or flatness assertions rather than by one element; $Con_T^S$, $Con_T^H$, and
Rosser consistency are collision-avoidance statements and therefore live near
CutA3 plus the detached-fixed-point geometry.

## 2. Cycle APS Models \(C_m\)

For every $m\ge2$, let

$$
L_m=\{\bot,\top,o_0,\ldots,o_{m-1}\}
$$

with $\bot<o_i<\top$ and the $o_i$ pairwise incomparable.  Put
$T=o_0$, $\Box=\mathrm{id}$, and

$$
\boxtimes\bot=\top,\qquad
\boxtimes\top=\bot,\qquad
\boxtimes o_i=o_{i+1\bmod m}.
$$

Then $C_m$ is an APS.  It is non-collapsed, satisfies G2 vacuously, has no
syntactic $\boxtimes$-fixed point, and has

$$
\mathrm{FG2}_n\quad\text{false for every checked }n.
$$

In particular, finite APS models already approximate the genuine infinite
star-dynamic shift $S_\omega$ from
`research/notes/infinite-ams-aps-raps-models-2026-06-11.tex`: a flat
consistency tower can avoid all finite formalized descent without producing a
fixed point.

## 3. Detached Rosser Period Models \(R_{2k}\)

For every $k\ge1$, form $R_{2k}$ by adding one new middle atom $p$ to
$C_{2k}$ and setting

$$
\boxtimes p=p.
$$

Then A1, A2, and A4 still hold, G2 is still true vacuously, and all checked
$\mathrm{FG2}_n$ fail.  However A3 fails at the single visible collision

$$
x=y=p.
$$

Indeed $p\le\Box p$ and $p\le\boxtimes p$, but
$p\nleq\boxtimes T=o_1$.  Thus

$$
\exists p(p=\boxtimes p)
\not\Rightarrow
\mathrm{FG2}_1
\quad\text{and}\quad
\exists p(p=\boxtimes p)
\not\Rightarrow
\mathrm{CutA3}.
$$

This is the clean G2-ZOO reading of the Rosser phenomenon: the fixed point is
detached from the consistency orbit.  It is not a limit of
$T,\boxtimes T,\boxtimes^2T,\ldots$, and it does not by itself supply cut
elimination or formalized G2.

The existing model `code/models/examples/R4-residuated.json` is the residuated
period-4 member of this detached family.  Pass 69 isolates the additional
cut/A3 diagnosis: adding the detached point preserves the A1/A2/A4 core but
keeps the model below full APS unless A3 is restored.

## 4. Cut Elimination Boundary

APS axiom A3 is the algebraic form of a cut/collision closure principle:

$$
x\le\Box y,\quad x\le\boxtimes y
\quad\Longrightarrow\quad
x\le\boxtimes T.
$$

In a residuated/resource-sensitive reading one first combines the two
resources as

$$
x\otimes x\le \Box y\otimes\boxtimes y.
$$

To recover the one-sorted A3 conclusion from this resource statement, some
diagonal contraction or completion principle must identify the duplicated
resource with the original one.  Hence the practical slogan:

$$
\mathrm{CutA3}
=
\text{collision closure}
+
\text{diagonal contraction/completion}.
$$

This explains the BS16-style separation recorded in
`research/notes/bs16-fiber-residuated-aps.md`: a Jeroslow/refutability fixed
point can exist in the contraction-free layer while the formalized G2 sequent

$$
\Box(\Box\bot\to\bot)\Rightarrow\Box\bot
$$

fails.

## 5. Machine Certificate

The finite certificate is:

- script: `code/scripts/check-pass69.py`
- report: `artifacts/reports/pass69-consistency-cut-infinite-g2-zoo-check.json`

It checks:

- $C_m$ for $2\le m\le12$: APS, no fixed point, G2 true, all checked nFG2
  false, flat orbit;
- $R_{2k}$ for $1\le k\le6$: A1/A2/A4 true, A3 false at the detached fixed
  point, FP-synt true only at $p$, all checked nFG2 false;
- the new statement names $C_n$, $\mathrm{Con}^{\mathrm{orb}}_n$,
  $\mathrm{G2}_n$, $\mathrm{FG2}_n$, $\mathrm{CutA3}$, and
  $\mathrm{Flat}_{\le N}$.

## 6. Open Arithmetic Lift

The next nontrivial step is to decide which of the new APS statements have
stable arithmetic counterparts.

1. Interpret $\mathrm{Con}^{\mathrm{orb}}_n$ as an iterated consistency
   sequence between $Con_T^L$ and the broader $ConLat_T$ family.
2. Identify the exact arithmetic counterpart of CutA3 among $Con_T^S$,
   $Con_T^H$, Rosser consistency, and local reflection principles.
3. Determine whether a fully residuated, integral, contraction-bearing version
   of $R_{2k}$ can keep the detached fixed point without forcing A3 or FG2.
4. Turn the star-dynamic $S_\omega$ proof into a reusable infinite-model
   schema file, since finite JSON models can only certify its finite shadows.
