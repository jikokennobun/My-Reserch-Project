# G2/FG2 Hierarchy and n-FG2

Source: https://chatgpt.com/share/6a0a7f2e-eec4-83ec-adc2-7fadc3feb442

Imported from Research Project handoff: 2026-05-22.
Extended by Claude Code Review 1, 2026-05-25 — certified results added.

## Topic

Hierarchy between G2 and FG2, including $n$-FG2 variants.

---

## Definitions

**G2**:

$$
\mathrm{G2}(S):
\quad
\boxtimes T\le\bot
\Rightarrow
T\le\bot.
$$

**$n$-FG2** (for $k\ge 1$):

$$
\mathrm{nFG2}(k):
\quad
\boxtimes^{k+1}T\le\boxtimes^k T.
$$

FG2 = nFG2(1). The sequence $\mathrm{nFG2}(1),\mathrm{nFG2}(2),\ldots$ is the
**$n$-FG2 hierarchy**.

**Orbit of $T$ under $\boxtimes$**:

$$
T,\;\boxtimes T,\;\boxtimes^2 T,\;\boxtimes^3 T,\;\ldots
$$

nFG2($k$) asks whether one step back along this orbit is an upward step in $L$.

---

## Certified Independence Results (3-element witnesses)

All models below are in `code/models/examples/` and are verified by `code/scripts/check-g2-zoo.py`.

### Theorem 1: G2 and FG2 are logically independent.

**(a) FG2 does not imply G2.** Model **M-010**:

$$
L=\{T,0,\bot\},\quad 0<\bot,\quad T\text{ isolated},
\quad \boxtimes T=\bot,\; \boxtimes\bot=0,\; \boxtimes 0=\bot.
$$

- G2: $\boxtimes T=\bot\le\bot$ (antecedent true), consequent $T\le\bot$
  FALSE (T isolated). So G2 FAILS.
- FG2: $\boxtimes^2 T=\boxtimes\bot=0\le\bot=\boxtimes T$ since $0<\bot$.
  So FG2 HOLDS.

**(b) G2 does not imply FG2.** Model **M-100**:

$$
L=\{T,c,\bot\}\text{ discrete},
\quad \boxtimes T=c,\; \boxtimes c=T,\; \boxtimes\bot=T.
$$

- G2: $\boxtimes T=c\not\le\bot$ (antecedent false). G2 holds VACUOUSLY.
- FG2: $\boxtimes^2 T=T\not\le c=\boxtimes T$ (discrete order). FG2 FAILS.

---

### Certified separation: FG2 does not imply nFG2(2).

Witness: model **M-010** above. The $\boxtimes$-orbit of $T$ is:

$$
T \to \bot \to 0 \to \bot \to 0 \to \bot \to \cdots
$$

(period-2 oscillation between $\bot$ and $0$ after the first step). Then:

$$
\mathrm{nFG2}(k) = \begin{cases}
\text{TRUE} & k\text{ odd} \\
\text{FALSE} & k\text{ even}
\end{cases}
$$

because for odd $k$: $\boxtimes^{k+1}T\in\{0\}$ and $\boxtimes^k T\in\{\bot\}$,
and $0<\bot$. For even $k$: $\boxtimes^{k+1}T\in\{\bot\}$ and
$\boxtimes^k T\in\{0\}$, and $\bot\not\le 0$.

**Status**: the full strictness problem is still open. The currently certified
statement is narrower: M-010 refutes
$\mathrm{nFG2}(1)\Rightarrow\mathrm{nFG2}(2)$ and, more generally, refutes
$\mathrm{nFG2}(k)\Rightarrow\mathrm{nFG2}(k+1)$ at every odd $k$. It does
not refute the even-step implications. Arbitrary-depth strictness remains an
open finite-model search target.

---

### Theorem 3: G2 + FP-synt does NOT imply FG2.

Model **M-101**:

$$
L=\{T,c,\bot\}\text{ discrete},
\quad \boxtimes T=c,\; \boxtimes c=T,\; \boxtimes\bot=\bot.
$$

- G2 holds vacuously ($\boxtimes T=c\not\le\bot$).
- FP-synt: $\boxtimes\bot=\bot$. ✓
- FG2: $\boxtimes^2 T=T\not\le c=\boxtimes T$. FAILS.

This is the finite-model analogue of the Beklemishev-Shamkanov 2016 result:
the existence of a Jeroslow-style fixed point $p=\boxtimes p$ does not imply
the formalized second incompleteness principle FG2.

References:
- [beklemishev_shamkanov_abstract_g2_beamer.pdf](https://drive.google.com/file/d/1Pkj6ZxECucSputAXulzhpYWuXxNnEf_J)
- See also `research/notes/bs16-fiber-residuated-aps.md`.

---

### Theorem 4: G2 + FG2 is consistent with ¬FP-synt.

Model **M-110**:

$$
L=\{T,c,\bot\},\quad T<c,\quad\bot\text{ isolated},
\quad \boxtimes T=c,\; \boxtimes c=T,\; \boxtimes\bot=T.
$$

- G2: $\boxtimes T=c\not\le\bot$. Vacuous. ✓
- FG2: $\boxtimes^2 T=T\le c=\boxtimes T$ since $T<c$. ✓
- FP-synt: $\boxtimes T=c\ne T$, $\boxtimes c=T\ne c$, $\boxtimes\bot=T\ne\bot$. NONE.

The n-FG2 pattern is TFTFTF... (same as M-010): FG2 holds but nFG2(2) fails.
FG2 holds here due to the order $T<c$ not because the orbit stabilizes.

---

## Summary Table (certified at size 3)

| Model | G2 | FG2 | FP | nFG2 pattern | G2 mode | Orbit type |
|-------|----|-----|----|-------------|---------|------------|
| M-000 | F  | F   | F  | FFFFFFFF   | ante=T, vacuously false | T↔⊥ |
| M-001 | F  | F   | T  | FFFFFFFF   | ante=T, vacuously false | T↔⊥ |
| M-010 | F  | T   | F  | TFTFTFTF   | ante=T, conseq fails | T→⊥→0→⊥→… |
| M-011 | F  | T   | T  | TTTTTTTT   | ante=T, conseq fails | T→⊥→⊥→… |
| M-100 | T  | F   | F  | FFFFFFFF   | vacuous | T→c→T→… |
| M-101 | T  | F   | T  | FFFFFFFF   | vacuous | T→c→T→… |
| M-110 | T  | T   | F  | TFTFTFTF   | vacuous | T→c→T→… |
| M-111 | T  | T   | T  | TTTTTTTT   | vacuous | T→T→… |

---

## n-FG2 Pattern Classification

The n-FG2 pattern is determined by the $\boxtimes$-orbit of $T$:

| Orbit type | Pattern | Models |
|-----------|---------|--------|
| Period-1 stabilization to FP | TTTTTTTT | M-011, M-111 |
| Period-2 with upward step | TFTFTFTF | M-010, M-110 |
| Period-2 without order relation | FFFFFFFF | M-000, M-001, M-100, M-101 |

**Proposition**: nFG2($k$) iff $\boxtimes^{k+1}T\le\boxtimes^k T$. The pattern
is periodic with period dividing the period of the $\boxtimes$-orbit of $T$
once the orbit enters its eventual cycle.

**Resolved below**: there is a uniform finite witness where nFG2($k$) fails
for all $k\le N$ but holds from $k=N+1$ onward.

---

## Arbitrary-Depth First-True nFG2 Witnesses

For each $N\ge 1$, define a finite preAPS $D_N$ with carrier

$$
L_N=\{T,a_1,\ldots,a_{N+1},s\}.
$$

The order is reflexive plus the single non-reflexive relation:

$$
s\le a_{N+1}.
$$

Define $\boxtimes$ by:

$$
\boxtimes T=a_1,\quad
\boxtimes a_i=a_{i+1}\ (1\le i\le N),\quad
\boxtimes a_{N+1}=s,\quad
\boxtimes s=s.
$$

This is antitone. The only nontrivial order relation is $s\le a_{N+1}$, and
antitonicity there asks for
$\boxtimes a_{N+1}=s\le s=\boxtimes s$, which holds.

The $\boxtimes$-orbit of $T$ is:

$$
T\to a_1\to a_2\to\cdots\to a_{N+1}\to s\to s\to\cdots.
$$

For $1\le k\le N$, nFG2($k$) asks $a_{k+1}\le a_k$, which is false by
construction. For $k=N+1$, it asks $s\le a_{N+1}$, which is true. All later
instances are $s\le s$, also true.

Thus $D_N$ proves arbitrary first-true depth for the nFG2 hierarchy:

$$
\neg\mathrm{nFG2}(1),\ldots,\neg\mathrm{nFG2}(N),
\quad
\mathrm{nFG2}(N+1),\mathrm{nFG2}(N+2),\ldots
$$

The generator
`code/scripts/new-nfg2-depth-witness.ps1` creates these models. The persisted
example `code/models/examples/nfg2-depth-3.json` is checked in
`artifacts/reports/g2-zoo-nfg2-depth-3.json` and has pattern `FFFTTTTT`.

---

## All-Level n-FG2 and Finite Orbit Stabilization

For a finite preAPS, all-level nFG2 has an exact orbit description.

**Theorem (finite orbit stabilization)**. Let $S=(L,\le,\boxtimes,T,\bot)$
be a finite preAPS. The following are equivalent:

1. $\mathrm{nFG2}(k)$ holds for every $k\ge 1$.
2. The tail orbit
   $\boxtimes T,\boxtimes^2T,\boxtimes^3T,\ldots$ is non-increasing:
   $\boxtimes^{k+1}T\le \boxtimes^kT$ for every $k\ge 1$.
3. There is an $N\ge 1$ such that
   $\boxtimes T\ge\boxtimes^2T\ge\cdots\ge\boxtimes^NT$ and
   $\boxtimes^NT$ is a syntactic fixed point.

The equivalence of (1) and (2) is definitional. For (2) to (3), finiteness
forces the non-increasing tail orbit to stabilize; if the stable value is
$p=\boxtimes^NT$, then $p=\boxtimes p$. The implication (3) to (2) is
immediate along the stated tail.

Consequently, all-level nFG2 implies a reachable syntactic fixed point in finite
models, but it does not imply G2: M-011 has all nFG2 levels true, a fixed point
at $\bot$, and G2 false.

For infinite APS or non-Noetherian preorders, the proof breaks exactly at the
stabilization step. The useful next axiom candidate is therefore:

**Orbit well-foundedness**: every non-increasing $\boxtimes$-tail orbit from
$\boxtimes T$ eventually stabilizes.

Under this axiom, the finite theorem extends verbatim to arbitrary preAPS.

## Non-Degenerate G2+FG2+FP Witness

Model `M4-G2FG2FP` is a 4-element non-collapsed witness where G2, FG2, and a
primitive syntactic fixed point all hold, with the fixed point at an interior
element $p$, not at $T$ or $\bot$.

$$
L=\{\bot,p,c,T\},\quad \bot<p<T,\quad c<T,\quad c\parallel p,\quad c\parallel\bot,
$$

$$
\boxtimes T=p,\qquad \boxtimes p=p,\qquad
\boxtimes c=T,\qquad \boxtimes\bot=T.
$$

The checker report `artifacts/reports/g2-zoo-M4-G2FG2FP.json` verifies:

- G2: true, vacuously, since $\boxtimes T=p\not\le\bot$;
- FG2: true, since $\boxtimes^2T=p\le p=\boxtimes T$;
- FP-synt: true at $p$;
- all checked nFG2 levels true by orbit $T\to p\to p\to\cdots$;
- collapse: false.

This resolves the previously open "G2+FG2+FP with non-degenerate fixed point"
finite-model task. It remains open whether such a witness can be equipped with
nontrivial residual operations satisfying the intended APS axiom package.

### Full Residuation Search

The exhaustive search report
`artifacts/reports/residuated-search-M4-G2FG2FP.json` shows that `M4-G2FG2FP` has no
full residuated monoid expansion on the same carrier and order, for any choice
of unit among $\{\bot,p,c,T\}$. The search enumerates all $4^9=262144$
binary operations compatible with each possible two-sided unit and rejects every
candidate after checking associativity, monotonicity, and existence of both
residuals.

Thus the non-degenerate G2+FG2+FP witness is not itself a residuated APS on this
underlying order. Any residuated version must either change the order, add
elements, weaken the residual requirement, or use a different witness family.

The smallest same-carrier order repair is now known. Adding just
$\bot\le c$ to `M4-G2FG2FP` produces
`M4-G2FG2FP-order-plus-bot-c-residuated`, with the order
$\bot<p<T$, $\bot<c<T$, and $p\parallel c$. The search report
`artifacts/reports/residuated-order-search-M4-G2FG2FP.json` finds a full residuated
expansion with unit $p$. The model preserves non-collapse, G2, FG2, all
checked nFG2 levels, and the reachable fixed point at $p$; see
`artifacts/reports/g2-zoo-M4-G2FG2FP-order-plus-bot-c-residuated.json`.

This repair has a concrete structural reading. The original M4 order already
has $\bot\le p$, $\bot\le T$, $p\le T$, and $c\le T$; its only missing
bottom-discipline instance is $\bot\le c$. Adding that relation makes
$\bot$ the actual least element and turns the order into the four-element
Boolean lattice. Thus the repair can be read as adding ex-falso/absurdity
weakening for the $c$-branch rather than as an arbitrary residuation trick.
Whether that principle is acceptable depends on the intended resource-sensitive
APS axiom package.

### Bottom Discipline Filter

The script `code/scripts/check-bottom-discipline.py` tests the finite G2-ZOO models
by adding every missing relation $\bot\le x$, then checking whether the fixed
$\boxtimes$ map remains antitone and whether the G2/FG2/FP/nFG2 behavior is
stable. The report is saved as
`artifacts/reports/bottom-discipline-filter-g2-zoo.json`.

The current finite witnesses split as follows:

| Model | Pure bottom-order repair keeps antitone? | Main effect |
|-------|------------------------------------------|-------------|
| `M-000` | yes | G2/FG2/FP stay false, but nFG2 changes from `FFFFFFFF` to `FTFTFTFT` |
| `M-010` | yes | FG2-not-G2 survives; all checked nFG2 become true and FP appears by $0\sim\bot$ |
| `M-111` | yes | G2+FG2+FP stays stable |
| `M4-G2FG2FP` | yes | G2+FG2+FP stays stable; this is exactly the `bot <= c` repair |
| `M4-G2FG2FP-order-plus-bot-c-residuated` | already | already bottom-disciplined and stable |
| `bottom-nfg2-depth-3` | already | bottom-disciplined replacement with pattern `FFFTTTTT` |
| `bottom-G2FG2-noFP` | already | bottom-disciplined G2+FG2 without FP-synt |
| `M-001`, `M-011`, `M-100`, `M-101`, `M-110` | no | adding bottom pairs breaks antitonicity of $\boxtimes$ |
| `nfg2-depth-3` | no | adding $s\le T,a_1,a_2,a_3$ breaks antitonicity |

Pass 15 adds the missing bottom-disciplined arbitrary-depth replacement family.
Consequently bottom discipline preserves FG2-not-G2 via the repaired `M-010`,
and preserves G2-not-FG2, G2+FP-not-FG2, and arbitrary first-true nFG2 depth via
the bottom-disciplined $B_N$ construction below. Pass 16 adds
`bottom-G2FG2-noFP`, so bottom discipline alone preserves all currently tracked
G2/FG2/FP-synt separations.

### Bottom-Disciplined Arbitrary-Depth Witnesses

For each $N\ge 1$, define $B_N$ with carrier

$$
\{b,T,a_1,\ldots,a_{N+1},s,U\}.
$$

The order has $b\le x\le U$ for every carrier element $x$, plus
$$
s\le a_{N+1}.
$$

Thus $b$ is a genuine bottom element and $B_N$ satisfies bottom discipline.
Define:

$$
\boxtimes b=U,\qquad
\boxtimes U=b,\qquad
\boxtimes T=a_1,\qquad
\boxtimes a_i=a_{i+1}\ (1\le i\le N),
$$

$$
\boxtimes a_{N+1}=s,\qquad
\boxtimes s=s.
$$

Antitonicity holds because every relation $b\le x$ asks
$\boxtimes x\le U=\boxtimes b$, every relation $x\le U$ asks
$b=\boxtimes U\le\boxtimes x$, and $s\le a_{N+1}$ asks
$s=\boxtimes a_{N+1}\le\boxtimes s=s$.

The $T$-orbit is again

$$
T\to a_1\to\cdots\to a_{N+1}\to s\to s\to\cdots.
$$

So nFG2($k$) fails for $k\le N$ and holds from $N+1$ onward. Since
$\boxtimes T=a_1\not\le b$, G2 holds vacuously; FG2 fails for $N\ge 1$;
and FP-synt holds at $s$. The generated depth-3 instance
`code/models/examples/bottom-nfg2-depth-3.json` is certified by
`artifacts/reports/g2-zoo-bottom-nfg2-depth-3.json` with pattern `FFFTTTTT`.

Pass 18 upgrades the checked depth-3 instance to full residuation on the same
carrier and order. The top-absorbing template uses $T$ as unit, $b$ as zero,
and sends every remaining nonzero, non-unit product to $U$. The builder
`code/scripts/build-top-absorbing-residuated-expansion.py` verifies associativity,
monotonicity, principal left/right residuals, and the residuation law; see
`artifacts/reports/residuated-top-absorbing-report-bottom-nfg2-depth-3.json`. The
persisted expansion `bottom-nfg2-depth-3-residuated` keeps G2 true, FG2 false,
FP-synt true at $s$, bottom discipline, and nFG2 pattern `FFFTTTTT`.

The same argument is uniform in $N$. Let
$$
M_N=B_N\setminus\{b,T\}.
$$
Define a commutative tensor by
$$
b\otimes x=b,\qquad T\otimes x=x,\qquad
x\otimes y=U\quad(x,y\in M_N).
$$
This is a monoid with unit $T$ and zero $b$: after removing occurrences of
the unit, any product with $b$ is $b$, while any product of two elements of
$M_N$ is $U$, and $U\in M_N$ absorbs all further non-unit nonzero
factors. Hence associativity is immediate by cases. Monotonicity follows from
the three kinds of order relation in $B_N$: $b\le x$, $x\le U$, and
$s\le a_{N+1}$. The first is absorbed by $b\le(-)$, the second by
$(-)\le U$, and the last by the fact that both products with a non-unit
nonzero factor are $U$, while products with $b$ and $T$ preserve the
relation.

For $m\in M_N$, the residual fibers are principal:
$$
b\backslash c=U,\qquad T\backslash c=c,
$$
and
$$
m\backslash c=
\begin{cases}
U & c=U,\\
T & m\le c\ne U,\\
b & \text{otherwise.}
\end{cases}
$$
Commutativity gives the same table for right residuals. Thus every $B_N$
admits a same-carrier, same-order full-residuated expansion. The tensor is
deliberately coarse, so the open issue is no longer existence of full
residuation but whether a less top-collapsing tensor can carry the same
arbitrary-depth separations.

Pass 20 finds a less top-collapsing tensor for the checked $B_3$ instance
under the still-strong constraint that $U\otimes x=U$ for every nonzero
$x\ne T$. The complete constrained search
`artifacts/reports/residuated-u-absorbing-search-bottom-nfg2-depth-3.json` minimizes the
number of $U$-valued products among the 15 unordered products on
$\{a_1,a_2,a_3,a_4,s\}$. The top-absorbing template has 15 such products; the
new witness `bottom-nfg2-depth-3-u-absorbing-minU` has 7. Its non-$U$ products
include:
$$
a_1^2=a_3,\quad a_1a_4=a_1s=a_2,\quad
a_2a_4=a_2s=a_3,\quad a_4^2=a_4s=s^2=a_1.
$$
The checker report `artifacts/reports/g2-zoo-bottom-nfg2-depth-3-u-absorbing-minU.json`
confirms that the G2/nFG2/FP profile is unchanged. This shows that the
top-absorbing tensor is sufficient but not minimal even inside the
$U$-absorbing search class.

Pass 21 tests the pattern at the next depth. A direct branch-and-bound search
for $B_4$ did not finish within the local 120-second pass budget, but the
pass 20 table has a simple truncated-exponent reading. Give $a_{N+1}$ and
$s$ exponent 1, and give $a_i$ exponent $i+1$ for $1\le i\le N$. Keep
$T$ as unit, $b$ as zero, and $U$ absorbing over nonzero non-units; for
the remaining products, add exponents and return $U$ exactly when the sum
exceeds $N+1$. The builder
`code/scripts/build-truncated-u-absorbing-residuated.py` verifies this template for
`bottom-nfg2-depth-4`: it has 10 $U$-valued products among 21 unordered
products on $\{a_1,\ldots,a_5,s\}$, rather than 21 for the top-absorbing
template, and preserves the `FFFFTTTT` profile. This supports a uniform
truncated-exponent $B_N$ conjecture, now separated from the earlier
top-absorbing proof.

Pass 22 proves the truncated-exponent construction uniformly. Let
$$
A_N=\{s,a_1,\ldots,a_{N+1}\}
$$
and put $e(s)=e(a_{N+1})=1$, $e(a_i)=i+1$ for $1\le i\le N$. Define
$\pi(1)=a_{N+1}$ and $\pi(r)=a_{r-1}$ for $2\le r\le N+1$. The tensor is:
$$
b\otimes x=b,\qquad T\otimes x=x,\qquad U\otimes x=U
\quad(x\ne b,T),
$$
and for $x,y\in A_N$,
$$
x\otimes y=
\begin{cases}
a_{e(x)+e(y)-1} & e(x)+e(y)\le N+1,\\
U & e(x)+e(y)>N+1.
\end{cases}
$$
Associativity reduces to associativity of addition with overflow at $N+1$;
once a partial sum overflows, all later nonzero non-unit products remain $U$.
The duplicate exponent-1 elements do not break associativity because no
two-factor product in $A_N$ has exponent 1. Monotonicity only needs the order
generators $b\le x$, $x\le U$, and $s\le a_{N+1}$. The first two are
handled by zero and $U$-absorption; the last is handled by
$e(s)=e(a_{N+1})$, so multiplication by any nonzero non-unit gives equal
results, while multiplication by $b$ or $T$ preserves the relation.

The residual table is principal. For $m\in A_N$, $q=e(m)$, and target
$c$, define $t(a_i)=i+1$ for $1\le i\le N$. Then:
$$
b\backslash c=U,\qquad T\backslash c=c,\qquad
U\backslash c=
\begin{cases}
U & c=U,\\
b & c\ne U,
\end{cases}
$$
and
$$
m\backslash c=
\begin{cases}
U & c=U,\\
T & m\le c,\\
\pi(t(c)-q) & c=a_i,\ 1\le i\le N,\ q<t(c),\\
b & \text{otherwise.}
\end{cases}
$$
Right residuals are identical by commutativity. Thus every bottom-disciplined
$B_N$ admits a same-carrier, same-order full-residuated expansion by the
truncated-exponent $U$-absorbing tensor. The remaining open issue is no
longer this uniform construction, but whether the $U$-absorbing constraint can
be weakened.

Pass 23 gives the first negative evidence for weakening $U$-absorption. The
new analyzer `code/scripts/analyze-truncated-u-forcing.py` fixes only the
truncated-exponent orbit table on $A_N$, keeps $T$ as unit and $b$ as
zero, and does **not** assume $U\otimes x=U$. On both checked instances
`bottom-nfg2-depth-3` and `bottom-nfg2-depth-4`, monotonicity already forces
every $U$-product. For each $y\in A_N$, there is some $x\in A_N$ with
$$
x\le U,\qquad x\otimes y=U.
$$
Monotonicity in the first coordinate gives
$$
U=x\otimes y\le U\otimes y,
$$
and since $U$ is top, $U\otimes y=U$. Then $y\le U$ forces
$U\otimes U=U$. Thus $U$-absorption is not merely an extra assumption once
the truncated orbit table is fixed. The broader question remains open only for
product tables that change the orbit part itself.

Pass 24 starts that broader search on `bottom-nfg2-depth-3`. The new script
`code/scripts/search-non-u-absorbing-residuated.py` fixes commutativity, unit $T$,
and zero $b$, but does not fix $U$-absorption or the orbit product table.
It splits cases by the monotonicity-allowed values of $U\otimes x$, searches
the remaining 21 nonzero non-unit products, and checks monotonicity,
associativity, and principal left/right residual fibers. The first persisted
bounded run
`artifacts/reports/residuated-non-u-absorbing-search-bottom-nfg2-depth-3.json` visits
1000 search nodes, 12 $U$-action patterns, and 382 complete assignments
without finding a non-$U$-absorbing full-residuated tensor. This is not a
negative theorem: a larger 10000-node attempt did not finish within the local
120-second pass budget. The next technical step is to add residual-fiber
pruning, especially for the $c=b$ fibers, before treating non-existence as
plausible.

Pass 25 adds that residual-fiber pruning and turns the B3 question positive.
The completed report
`artifacts/reports/residuated-non-u-absorbing-search-bottom-nfg2-depth-3.json` now visits
47 possible $U$-action patterns, prunes 16 immediately and 1537 branches by
partial residual-fiber obstruction, checks 475 complete assignments, and finds
`bottom-nfg2-depth-3-non-u-absorbing`. It is a full same-order residuated
expansion with 17 non-$U$ products among the 21 unordered nonzero non-unit
products. Crucially,
$$
U\otimes a_4=a_4,\qquad U\otimes s=s,
$$
so $U$ is not absorbing. The orbit table is no longer the truncated-exponent
table: $a_1,a_2,a_3$ form a Klein-four pattern over the unit $T$,
$$
a_i^2=T,\quad a_1a_2=a_3,\quad a_1a_3=a_2,\quad a_2a_3=a_1,
$$
while $a_j\otimes a_4=a_4$, $a_j\otimes s=s$ for $j=1,2,3$, and
$$
a_4^2=a_4,\qquad a_4s=s^2=b.
$$
The G2-ZOO checker confirms the original `FFFTTTTT` profile, with G2 true,
FG2 false, FP-synt at $s$, and bottom discipline intact. Thus same-order
full residuation does not force $U$-absorption even in the checked $B_3$
case; it is forced only relative to the truncated orbit table.

Pass 26 tests the next checked depth. The same orbit-table-varying search on
`bottom-nfg2-depth-4` did not finish exhaustively within the local pass budget:
the saved report
`artifacts/reports/residuated-non-u-absorbing-search-bottom-nfg2-depth-4.json` stops at
1000 nodes after 48 $U$-action patterns, 697 residual-fiber prunes, and 147
complete assignments. It nevertheless finds a valid same-order full-residuated
non-$U$-absorbing expansion,
`bottom-nfg2-depth-4-non-u-absorbing`. In this witness
$$
U\otimes a_1=a_1,\qquad U\otimes a_2=a_2,
$$
while $U$ still sends $a_3,a_4,a_5,s$ to $U$. The orbit product table is
again different from both the truncated-exponent template and the B3
Klein-four/idempotent pattern: $a_1^2=a_1$, $a_2^2=a_2$,
$a_1a_2=b$, and $a_1,a_2$ act as projective factors on the higher orbit
elements. The checker report
`artifacts/reports/g2-zoo-bottom-nfg2-depth-4-non-u-absorbing.json` confirms the original
`FFFFTTTT` profile, with G2 true, FG2 false, FP-synt at $s$, bottom
discipline, and no warnings. The result is therefore existentially positive at
checked B4, but it does not yet give a uniform $B_N$ formula or a minimality
theorem for the product table.

Pass 27 extracts a uniform candidate from the B4 search witness. For $N\ge3$,
split the $B_N$ orbit part into a front $F=\{a_1,a_2\}$ and a shifted tail
$$
R_N=\{s,a_{N+1},a_3,\ldots,a_N\}.
$$
Let $a_1,a_2$ be orthogonal idempotents:
$$
a_1^2=a_1,\qquad a_2^2=a_2,\qquad a_1a_2=b,
$$
make each front element absorb multiplication by the tail and by $U$,
$$
p\otimes r=p,\qquad U\otimes p=p
\quad(p\in F,\ r\in R_N\cup\{U\}),
$$
and put a shifted truncated-exponent product on $R_N$ with
$$
\tau(s)=\tau(a_{N+1})=1,\qquad \tau(a_i)=i-1\quad(3\le i\le N),
$$
overflowing to $U$ above $N-1$. The builder
`code/scripts/build-front-shifted-non-u-absorbing-residuated.py` verifies
associativity, monotonicity, principal left/right residuals, and the full
residuation law for checked depths 3, 4, and 5. At depth 4 it exactly
reproduces the bounded-search witness from pass 26. At depth 3 it gives a
second valid non-$U$-absorbing tensor with 14 non-$U$ searched products,
whereas the pass 25 search witness has 17. At depth 5 it gives a new checked
same-order full-residuated expansion preserving the `FFFFFTTT` nFG2 profile.

The template has a clean proof outline. Associativity splits into three
stable regions: the two-element front semilattice with cross-product $b$, the
shifted truncated-addition tail, and the $U$-action that fixes the front but
absorbs the tail. Monotonicity only needs the order generators $b\le x$,
$x\le U$, and $s\le a_{N+1}$; the last is handled by equal tail exponent
1. The remaining symbolic work is to write the closed residual table, replacing
the current finite-depth verification by a uniform lemma.

Pass 28 supplies that residual table. Write $p^\perp$ for the other element
of $F=\{a_1,a_2\}$. The easy residuals are
$$
b\backslash c=U,\qquad T\backslash c=c,
$$
$$
p\backslash c=
\begin{cases}
U & c\in\{p,U\},\\
p^\perp & \text{otherwise,}
\end{cases}
\qquad
U\backslash c=
\begin{cases}
U & c=U,\\
c & c\in F,\\
b & \text{otherwise.}
\end{cases}
$$
For $r\in R_N$, the front targets give $r\backslash p=p$ and the top
target gives $r\backslash U=U$. The remaining tail cases are:
$$
r\backslash c=
\begin{cases}
T & c=s,\ r=s,\\
T & c=a_{N+1},\ r\in\{s,a_{N+1}\},\\
T & c=r\in\{a_3,\ldots,a_N\},\\
a_{N+1} & c=a_j,\ 3\le j\le N,\ j-1-\tau(r)=1,\\
a_{d+1} & c=a_j,\ 3\le j\le N,\ d=j-1-\tau(r),\ 2\le d\le N-1,\\
b & \text{otherwise.}
\end{cases}
$$
Commutativity gives the right residuals. These cases are just the principal
generators of the fibers: front fibers are $\downarrow p$, the duplicate
tail-exponent-1 fiber is $\downarrow a_{N+1}=\{b,s,a_{N+1}\}$, exact
tail-target fibers are $\downarrow T$, and impossible fibers are
$\downarrow b$. The checker
`code/scripts/check-front-shifted-residual-formula.py` verifies this closed table
against the generated residuals at depths 3, 4, and 5. Thus the
front-shifted non-$U$-absorbing tensor is now a uniform $B_N$ same-order
full-residuated template for $N\ge3$, not merely a finite search pattern.

Pass 29 checks the structural-rule profile of the current residuated witnesses.
The analyzer `code/scripts/analyze-structural-rules.py` implements the Axis III
rules:
$$
E:\ x\otimes y=y\otimes x,\qquad
C:\ x\otimes x\le x,\qquad
W:\ x\le y\Rightarrow x\otimes z\le y.
$$
The report
`artifacts/reports/structural-rules-front-shifted-comparison.json` compares the
top-absorbing, truncated $U$-absorbing, non-$U$-absorbing, front-shifted,
and G2+FG2-without-FP residuated expansions. All checked tensors satisfy
exchange. None satisfies the strong weakening rule or its reflexive
discarding instance $x\otimes z\le x$; this failure is immediate from the
unit at $T$, since $T\otimes z=z$ and generally $z\not\le T$. Global
contraction holds only for `bottom-G2FG2-noFP-residuated`.

The front-shifted template has a sharper local profile. Its front is
contractive and idempotent:
$$
a_1^2=a_1,\qquad a_2^2=a_2,
$$
but its shifted tail remains resource-sensitive. At depths 3, 4, and 5 the
contraction failures are exactly tail or fixed-point witnesses such as
$a_3^2=U$, $a_{N+1}^2=a_3$, and $s^2=a_3$, depending on the depth.
Thus the front/tail split is not cosmetic: it isolates a small contractive
front from the noncontractive tail needed for the arbitrary-depth nFG2 orbit.

Pass 30 identifies the algebraic presentation behind that split. The set
$$
I=\{b,a_1,a_2\}
$$
is a downward closed two-sided tensor ideal. Its nonzero part is the
orthogonal idempotent zero-band
$$
a_1^2=a_1,\qquad a_2^2=a_2,\qquad a_1a_2=b,
$$
and multiplication by any nonzero element outside the opposite front atom
projects back to the chosen front atom. Collapsing $I$ to $b$ leaves the
shifted truncated tail monoid on
$$
\{b,T,U,s,a_{N+1},a_3,\ldots,a_N\}.
$$
The checker `code/scripts/check-front-shifted-extension-presentation.py` verifies
this ideal-extension presentation on the depth-3, depth-4, and depth-5 saved
models. The construction is therefore not a direct product or a pure
orthogonal sum: the front is a contractive tensor ideal glued onto a
resource-sensitive quotient tail.

Pass 31 tests how far that front can be enlarged inside the same
orthogonal-front, shifted-tail schema. The script
`code/scripts/check-front-ideal-size-bound.py` builds front widths
$k=0,1,\ldots$ with
$$
F_k=\{a_1,\ldots,a_k\},
$$
orthogonal idempotent multiplication on $F_k$, and shifted tail
$\{s,a_{N+1},a_{k+1},\ldots,a_N\}$. The report
`artifacts/reports/front-ideal-size-bound-check.json` checks depths 3, 4, and 5. In all
three depths, widths $0,1,2$ are fully residuated and width $3$ is the first
failure. The failure is not accidental: for $p\in F_k$, the fiber of
$p\backslash b$ contains $\{b\}\cup(F_k\setminus\{p\})$, which has multiple
incomparable maximal elements once $k\ge3$. Thus the current two-front
template is maximal within this same-order orthogonal-front schema, while a
one-front non-$U$-absorbing variant remains a smaller positive template.

Pass 32 closes the positive residual-table side of that pattern. For
$k\in\{0,1,2\}$, define
$$
F_k=\{a_1,\ldots,a_k\},\qquad
R_{N,k}=\{s,a_{N+1},a_{k+1},\ldots,a_N\},
$$
with tail exponent
$$
\tau_k(s)=\tau_k(a_{N+1})=1,\qquad
\tau_k(a_i)=i-k+1.
$$
The closed residual table is the same front/tail table as before, with only
one front clause changing: if $p\in F_k$, then $p\backslash c=U$ for
$c\in\{p,U\}$, while the non-$U$ residual is $b$ when $k=1$ and the
other front atom when $k=2$. Tail residuals are shifted exponent subtraction
using $\rho_k(1)=a_{N+1}$ and $\rho_k(d)=a_{k+d-1}$. The checker
`code/scripts/check-front-width-residual-formula.py` compares this formula against
generated residuals for $k=0,1,2$ at depths 3, 4, and 5; the report
`artifacts/reports/front-width-residual-formula-check.json` has zero mismatches. Thus
the uniform theorem now has both sides: $k=0,1,2$ are residuated, and
$k\ge3$ fails on the same order by the non-principal
$p\backslash b$ fiber.

### Bottom-Disciplined G2+FG2 without FP

The remaining bottom-discipline separation is witnessed by
`bottom-G2FG2-noFP`. Its carrier is

$$
\{b,d,a,T,U\},
$$

with $b\le x\le U$ for every $x$ and one additional relation $d\le a$.
The refutability map is:

$$
\boxtimes b=U,\quad \boxtimes U=b,\quad \boxtimes T=a,\quad
\boxtimes a=d,\quad \boxtimes d=a.
$$

Bottom discipline holds because $b$ is least. Antitonicity holds because the
bounding pairs are absorbed by $U$ and $b$, and the only interior relation
$d\le a$ maps to $d=\boxtimes a\le\boxtimes d=a$. G2 holds vacuously since
$\boxtimes T=a\not\le b$. FG2 holds because
$$
\boxtimes^2T=d\le a=\boxtimes T.
$$
There is no syntactic fixed point: $b\leftrightarrow U$, $a\leftrightarrow d$
as a strict two-cycle, and $T\mapsto a$ with $T\not\sim a$. The checker
report `artifacts/reports/g2-zoo-bottom-G2FG2-noFP.json` verifies G2 true, FG2 true,
FP-synt false, and nFG2 pattern `TFTFTFTF`.

The same order also carries a full residuated expansion. A targeted commutative
search with unit $T$ and absorbing zero $b$ checks $5^6=15625$ candidate
tensors and finds 8 full-residuated operations; see
`artifacts/reports/residuated-commutative-zero-search-bottom-G2FG2-noFP.json`. The
persisted expansion `bottom-G2FG2-noFP-residuated` uses $T$ as the monoid
unit. Its tensor has $b$ as zero, keeps $U$ idempotent, and sends
$a\otimes a=a\otimes d=d\otimes d=b$. Thus the bottom-disciplined
G2+FG2-without-FP separation survives full residuation on the same carrier and
order.

---

## Cyclic-Group Front Ideals (Pass 33)

Pass 33 tests two escape routes from the $k\ge3$ orthogonal-front
principal-fiber obstruction.

### Route A: Non-Orthogonal (Cyclic Group) Front Multiplication

Replace the pairwise-zero cross-product on $F_3=\{a_1,a_2,a_3\}$ with the
cyclic group of order 3: $a_i\cdot a_j=a_{i+j\bmod3}$ (indices in
$\mathbb Z/3\mathbb Z$). The zero $b$ is not in the group; absorption by
$b$ and the group identity coinciding with $T$ (the monoid unit) are set
separately. For $U$, define $U\otimes a_i=a_i$ (front identity action, as
in the $k=2$ front-shifted non-$U$-absorbing template). Tail elements are
absorbed by front elements as before.

**Principal fiber at $k=3$**: For $p=a_i\in F_3$, the fiber of
$p\backslash b$ consists of all $x$ with $p\otimes x\le b$, i.e.\
$p\otimes x=b$ (since $b$ is the bottom). No element of $F_3$ satisfies
$p\otimes a_j=b$ (all front products stay in $F_3\cup\{b\}$ and are in
$F_3$ when factors are non-zero). Tail elements satisfy $p\otimes r=p\not\le
b$. The only element with product $b$ is $b$ itself. Hence
$p\backslash b=b$, which is principal. ✓

**Associativity**: $\mathbb Z/3\mathbb Z$ is associative. Interactions with
$b$, $T$, and $U$ (absorption/unit) are standard. Front-times-tail:
$p\otimes r=p$ and $(p\otimes r)\otimes s=p\otimes s=p$, while
$p\otimes(r\otimes s)$: since $r\otimes s$ for tail elements is a tail
element or $U$ or $b$, and $p$ absorbs all of those to $p$. ✓

**Monotonicity**: the new front cross-products are non-zero non-$b$ elements of
$F_3$. The order generators $b\le x$ and $x\le U$ work as before. The
relation $s\le a_{N+1}$ only involves tail elements, unchanged. ✓

**APS profile**: the orbit of $T$ under $\boxtimes$ is independent of
$\otimes$. G2, FG2, FP-synt, and the nFG2 pattern remain as in the base
$B_N$ model. ✓

**Theorem (cyclic-group escape at $k=3$)**: For every $N\ge3$, the
bottom-disciplined $B_N$ preAPS admits a same-carrier, same-order full
residuated expansion using the cyclic-group-of-order-3 front multiplication on
$F_3=\{a_1,a_2,a_3\}$. The expansion is non-$U$-absorbing ($U\otimes
a_i=a_i$), the fiber $p\backslash b=b$ is principal for all $p\in F_3$,
and the G2/FG2/nFG2/FP profile is preserved.

### Route B: Front-Order Join (Obstructed)

Adding a relation $a_i\le a_j$ among front atoms while keeping the pairwise-zero
product makes the fiber of $a_p\backslash b$ principal at $a_j$ (if
$a_j$ dominates all relevant front elements). However, antitonicity of
$\boxtimes$ on the extended order requires
$\boxtimes a_j\le\boxtimes a_i$, i.e.\ $a_{j+1}\le a_i$ for consecutive
orbit elements. Propagating this requirement through the orbit produces the
reverse chain, ultimately forcing $a_{i+1}\le a_i$ and
$a_i\le a_{i+1}$ for some pair — a contradiction unless elements collapse. Hence:

**Proposition (Route B obstruction)**: Adding a join among front orbit atoms in
$B_N$ while keeping $\boxtimes$ antitone induces a cascade of reverse
relations that collapses adjacent orbit elements. Route B fails to extend the
$B_N$ preAPS.

## Front Rigidity (Pass 34) — Route A Refuted

> **Correction.** The Route A "cyclic-group escape at $k=3$" theorem stated
> above is **false as stated**. Its monotonicity paragraph silently kept the
> non-$U$-absorbing action $U\otimes a_i=a_i$ borrowed from the orthogonal
> $k=2$ template. That action is monotone for an orthogonal *zero-band* (whose
> products descend, $a_i\otimes a_j\le a_j$) but not for a group (whose products
> permute the front). Pass 34 shows no nontrivial group front survives.

Fix the bottom-disciplined $B_N$ ($N\ge1$) and let $\otimes$ be a commutative,
associative, monotone, fully residuated tensor with unit $T$, zero $b$,
restricting to a magma on the incomparable front $F_k=\{a_1,\dots,a_k\}$,
$k\ge2$.

**Lemma (front integrality).** For all $i,j\le k$, $\;a_i\otimes a_j\le a_j$.

*Proof.* Monotonicity on $a_i\le U$ gives $a_i\otimes a_j\le U\otimes a_j=:u_j$,
so $u_j$ upper-bounds $\{a_i\otimes a_j:i\}$. If $u_j\not\le a_j$ then
$U\notin(a_j\backslash a_j)$ because $U\otimes a_j=u_j\not\le a_j$. But that
fiber contains $T$ (as $a_j\otimes T=a_j$) and any front atom $a_e$ with
$a_e\otimes a_j=a_j$; $T$ and $a_e$ are incomparable atoms whose only common
upper bound in $B_N$ is $U$, so the fiber has no maximum — contradicting full
residuation. Hence $u_j\le a_j$, so $a_i\otimes a_j\le a_j$. $\blacksquare$

**Theorem (front rigidity).** The front sub-magma is forced to be the
orthogonal idempotent zero-band
$$
a_i\otimes a_j=b\ (i\ne j),\qquad a_i\otimes a_i\in\{a_i,b\}.
$$
Hence no nontrivial group fits on $F_k$: a group front exists **iff
$\lvert G\rvert=1$**.

*Proof.* The lemma with commutativity gives $a_i\otimes a_j\le a_i\wedge a_j$;
incomparable atoms meet at $b$, so $a_i\otimes a_j=b$ for $i\ne j$, and
$a_i^2\le a_i$ forces $a_i^2\in\{a_i,b\}$. A group needs $a_i\otimes a_j$ to
exhaust $F_k$ with inverses, impossible once a single cross-product is pinned to
$b$ ($k\ge2$). $\blacksquare$

**Verification.** `code/scripts/check-front-group-order-bound.py` ranges over
every $U\otimes a_i$ choice in the minimal faithful ambient
$\{b,T,a_1,\dots,a_k,U\}$. It returns no monotone fully-residuated tensor for
$\mathbb Z/2,\mathbb Z/3,\mathbb Z/4$ or $V_4=\mathbb Z/2\times\mathbb Z/2$,
while reproducing the established orthogonal data (residuated at $k=1,2$ with
$U\otimes a_i=a_i$; failure at $k=3$). The group case forces $U$-absorption
($U\otimes a_j=U$) and the diagonal fiber $a_j\backslash a_j$ then loses its top.

Combined with the Pass-31 width bound ($k\le2$), the orthogonal idempotent
zero-band of width $\le2$ is the **forced** shape of any same-carrier/order
commutative residuated front of $B_N$ — not merely one option among many. Both
escape routes from the $k\ge3$ obstruction therefore fail: Route B by the
antitonicity cascade, Route A by integrality. The remaining loophole is
non-commutativity (two residuals), opened as a new problem.

## Non-Commutative Front Rigidity (Pass 35) — the loophole closes

Pass 34's rigidity proof used commutativity through the integrality inequality
$a_i\otimes a_j\le a_i\wedge a_j$. The natural escape is to drop commutativity,
admit two residuals
$$
a\backslash c=\max\{x:a\otimes x\le c\},\qquad
c/a=\max\{x:x\otimes a\le c\},
$$
and search the left and right $U$-actions $U\otimes a_i$, $a_i\otimes U$
*independently*. Pass 35 shows the loophole is empty: the failure mode is
already one-sided and order-theoretic.

Fix the bottom-disciplined $B_N$, $\otimes$ associative, two-sidedly monotone,
two-sided unit $T$, two-sided zero $b$, restricting to a finite group
$(F_k,\otimes)\cong G$ with $\lvert G\rvert=k\ge2$ and identity $a_{i_0}\in F_k$.

**Lemma (two-sided front absorption).** $a_j\otimes U=U\otimes a_j=U$ for all
$a_j\in F_k$.

*Proof.* Left-translation $L_{a_j}:a_e\mapsto a_j\otimes a_e$ is a bijection of
the group $F_k$, so $\{a_j\otimes a_e:a_e\in F_k\}=F_k$. For each $a_e\le U$,
right-monotonicity gives $a_j\otimes a_e\le a_j\otimes U$; hence $a_j\otimes U$
is an upper bound of all of $F_k$. In $B_N$ the front atoms are pairwise
incomparable and (for $k\ge2$) their only common upper bound is $U$ — no
$a_{N+1}$, $s$, or front atom dominates two distinct front atoms. Thus
$a_j\otimes U=U$. The mirror statement uses $R_{a_j}$ bijective and
left-monotonicity. $\blacksquare$

**Theorem (non-commutative front rigidity).** A finite group fits the front of a
two-sidedly monotone, associative, two-residuated $B_N$-tensor **iff
$\lvert G\rvert=1$**.

*Proof.* Suppose $k\ge2$. The right fiber $a_j/a_j=\{x:x\otimes a_j\le a_j\}$
contains both $T$ (global unit: $T\otimes a_j=a_j$) and $a_{i_0}$ (group
identity: $a_{i_0}\otimes a_j=a_j$). These are incomparable in $B_N$ (orbit
start vs. front atom), so the only candidate maximum is their join $U$; but the
Lemma gives $U\otimes a_j=U\not\le a_j$, so $U\notin a_j/a_j$ and the fiber has
no maximum — right residuation fails. The left fiber $a_j\backslash a_j$ fails
symmetrically via $a_j\otimes U=U$. $\blacksquare$

**Verification.** `code/scripts/check-noncommutative-front-group-bound.py`
implements the two-residual predicate (associativity, two-sided monotonicity,
*both* fibers principal) with independent left/right $U$-actions. (i) The
commutative orthogonal band, re-checked under the two-residual predicate,
reproduces the established data: residuated at $k=1,2$ with the non-absorbing
action $U\otimes a_i=a_i\otimes U=a_i$, failing at $k=3$. (ii) Exhaustive over
both $U$-actions, $\mathbb Z/2$ ($k=2$) and $\mathbb Z/3$ ($k=3$) admit no
two-residuated tensor. (iii) For $\mathbb Z/4$, $V_4$, and the non-abelian
$S_3$ ($k=6$), the monotonicity-forced all-$U$ tensor is not two-residuated and
the unique non-absorbing action is not even two-sided monotone — confirming the
Lemma leaves no monotone alternative.

**Diagnosis.** The obstruction is now isolated to two purely order-theoretic
facts about $B_N$: (i) for $k\ge2$ a group
front has $\ge2$ pairwise-incomparable atoms whose only common upper bound is
$U$, and (ii) $U$ absorbs every front atom on both sides. Together they strand
the incomparable pair $\{T,e_G\}$ in each diagonal fiber, with no maximum below
$U$. Commutativity and integrality are red herrings; rigidity is an
order-theoretic property of the carrier.

## Selective-Median Escape (Pass 37)

The Pass 34–36 rigidity ceiling $\lvert G\rvert=1$ turns out to be an artifact
of a *single missing join*. The diagonal-fiber obstruction is always the same
incomparable pair $\{T,e_G\}$ (global unit vs. group identity), whose only
common upper bound in $B_N$ is the absorbing top $U$ — and $U$ is excluded by
$U$-absorption. Supply the missing join and the obstruction evaporates.

**Definition ($B_N^{\mathrm{med}}$).** Augment the bottom-disciplined $B_N$
carrier by one element $m$; order $b\le x\le U$, $s\le a_{N+1}$, and
$b,T,a_1\le m\le U$ with $a_1=e_G$; $m$ incomparable to $a_2,\dots,a_{N+1},s$.
Tensor: $b$ zero, $T$ unit, group product on $F_k\cong G$, $m^2=m$,
$m\otimes g=g\otimes m=g$ ($g\in F_k$), $a_j\otimes m=a_j$, all remaining
nonzero non-unit products $=U$. Forced $\boxtimes m=b$ (since $\boxtimes
m\le\boxtimes T\wedge\boxtimes e_G=a_1\wedge a_2=b$).

**Theorem (Selective-Median Escape).** For every finite abelian $G$ and
$N\ge\lvert G\rvert$, $B_N^{\mathrm{med}}$ with front $F_k\cong G$ carries a
commutative, associative, monotone, $T$-unital, fully residuated tensor whose
diagonal fibers are principal, $a_j\backslash a_j=\{b,T,e_G,m\}$ with maximum
$m=T\vee e_G$. Hence the maximum front-group order in the carrier-plus-median
schema is $\lvert G\rvert=\infty$; the rigidity ceiling was a pure artifact of
the absent join $T\vee e_G$.

*Status.* Machine-verified for $\mathbb Z/2,\dots,\mathbb Z/5$ by
`code/scripts/check-selective-median-bound.py`. Controls reproduce the known
obstructions: no median $\Rightarrow$ fiber $\{b,T,e_G\}$ with empty maximal set
(non-principal); full cap $c$ over the front $\Rightarrow$ non-monotonicity
($a_1\otimes c=U\not\le c$, the Pass-36 ejection). Remaining obligation: the
$G$-uniform associativity lemma and the non-abelian case (two residuals).

## Non-Abelian Selective Median (Pass 38)

**Question.** Non-commutativity splits the diagonal residual into two fibers
$a_j\backslash a_j$ (left) and $a_j/a_j$ (right). Does the escape now require a
*second* median, or $G$-dependent order data growing with the conjugacy-class
count?

**Theorem (Single-Median Uniformity, tested battery).** Equip
$B_N^{\mathrm{med}}$ with a two-residual ($\backslash,/$) tensor and a
non-abelian front. The *same* one-point median $m=T\vee e_G$ makes *both*
diagonal fibers principal, $a_j\backslash a_j=a_j/a_j=\{b,T,e_G,m\}$ (maximum
$m$), with forced $\boxtimes m=b$ preserving the G2/FG2/nFG2/FP profile. The
number of medians needed is $1$, independent of the conjugacy-class count — so
it is *not* a new group invariant.

*Proof idea.* Left/right translations $L_{a_j},R_{a_j}$ are bijections of the
group front, so the $U$-absorption analysis is two-sided-symmetric; the unique
join-deficient pair strictly below $U$ is $\{T,e_G\}$ for *every* finite $G$,
because $T$ (global unit) and $e_G$ (group identity) are the only two idempotent
two-sided units acting as identity on the front, and no front atom or tail
element dominates both. One join $m$ caps exactly this pair on both sides.

*Status.* Machine-verified for $S_3$ ($k=6$, 3 conjugacy classes), $D_4$ and
$Q_8$ ($k=8$, 5 classes each — $D_4$ with non-normal reflections, $Q_8$ with
every subgroup normal and a unique involution), plus the abelian control
$\mathbb Z/4$, by `code/scripts/check-noncommutative-selective-median.py`
(full two-sided unit/associativity/monotonicity/residuation check; both
no-median and full-cap controls FAIL as predicted). Report:
`artifacts/reports/noncommutative-selective-median-check.json`. *Open:* the
uniform all-finite-groups theorem (Pass 39 target).

## Uniform Selective-Median Theorem (Pass 39)

The Pass 37/38 escapes were verified group by group. Pass 39 proves the
statement for *all* finite $G$ at once, by naming the algebra of
$B_N^{\mathrm{med}}$ correctly. The nonzero, non-unit multiplicative part
$M^\ast=F\cup\{m\}\cup C$ (with $C=\{a_{N+1},s,U\}$) is an **ideal extension**
$$ G^1 \;\hookrightarrow\; M^\ast \;\twoheadrightarrow\; \{U\}, $$
where $F\cup\{m\}\cong G^1$ is the group $G$ with a *freshly adjoined* identity
$m$, and $C$ is a two-sided ideal on which every product collapses to $U$. The
subtlety: $m$ is the block's two-sided identity ($m\otimes g=g\otimes m=g$,
$m^2=m$), while the group identity $e_G=a_1$ is **not** the block identity
($e_G\otimes m=e_G\ne m$). Two distinct two-sided identities cannot coexist in a
monoid, and they don't — $G$ embeds in $G^1$ as a subsemigroup that is *not* a
submonoid. Everything below is independent of the Cayley table of $G$.

**Lemma 1 (Associativity, $G$-free).** $\otimes$ is associative. *Proof.* $b$
absorbs, $T$ neutralizes. On $M^\ast$: $F\cup\{m\}\cong G^1$ is a monoid; $C$ is
a two-sided ideal with $U\otimes z=z\otimes U=U$ for nonzero non-unit $z$, so any
triple touching $C$ short-circuits to $U$ in both bracketings (and $F\cup\{m\}$
is closed, so the untouched factors never produce a non-$U$ value). Ideal-
extension associativity, table-independent. $\square$

**Lemma 2 (Two-sided monotonicity, $G$-free).** Check the order covers
$s\prec a_{N+1}$, $T\prec m$, $a_1\prec m$. The group enters *only* via
$a_1\otimes a_j=a_j=m\otimes a_j$, which holds precisely because $a_1=e_G$ is the
identity; no other table entry is consulted. The front $F_k$ being an antichain
permuted by translation means front products never violate order. $\square$

**Lemma 3 (Fiber classification, $G$-free).** Every left fiber
$L(a,c)=\{x:a\otimes x\le c\}$ is principal; the front-inverting
anti-automorphism $\phi(a_i)=a_{i^{-1}}$ (identity off $F$, order-automorphism,
$\phi(x\otimes y)=\phi(y)\otimes\phi(x)$) carries left fibers to right fibers, so
right fibers are principal too. *Proof.* The only nontrivial multiplier is
$a_p\in F$, with $a_p\otimes x=b\,(x{=}b)$, $a_p\,(x{\in}\{T,m\})$,
$a_{pq}\,(x{=}a_q)$, $U\,(x{\in}C)$. For $c=a_r$: if $r\ne p$ the fiber is
$\{b,a_{p^{-1}r}\}$ (the unit $T$ drops out, **no pair stranded**, max
$a_{p^{-1}r}$); if $r=p$ the fiber is $\{b,T,a_1,m\}$ (the stranded pair is
$\{T,a_1\}$ for **every** $p$, capped by the single $m=T\vee a_1$). For $c=m$,
$c\in\{b,T,a_{N+1},s\}$, $c=U$: principal by inspection. $\square$

**Theorem (Uniform Non-Abelian Selective-Median Residuation).** For every finite
group $G$ and $N=\lvert G\rvert$, $B_N^{\mathrm{med}}$ with front $F_k\cong G$
carries an associative, two-sided monotone, $T$-unital, fully two-sided
residuated tensor with forced $\boxtimes m=b$ (antitonicity preserved, profile
intact). The diagonal fibers are $a_p\backslash a_p=a_p/a_p=\{b,T,e_G,m\}$ (max
$m$) for all $p$. Hence the maximum admissible front-group order is
$\lvert G\rvert=\infty$ and the number of medians needed is exactly $1$,
uniformly — independent of $\lvert G\rvert$, conjugacy-class count, and
normality structure. $\blacksquare$

*Reading.* The Pass 34–36 rigidity ceiling ($\lvert G\rvert=1$) and its Pass
37/38 collapse are now one phenomenon: $B_N$ lacked exactly one join, $T\vee
e_G$, and supplying it repairs *all* diagonal fibers because they strand the
*same* pair. Non-commutativity, large conjugacy-class counts, and exotic
normality structure are all irrelevant — front rigidity and its repair are
order-theoretic, group-theoretically uniform facts.

*Status.* Lemmas 1–3 proved $G$-independently above. Empirically reconfirmed
past the old $\lvert G\rvert\le8$ ceiling by
`code/scripts/check-uniform-selective-median-theorem.py` on the battery
$\mathbb Z/6$, $(\mathbb Z/2)^3$, $D_5$, $A_4$ (smallest group violating the
converse of Lagrange — a pathological stress test), $S_4$ (order 24, carrier
30): all five ESCAPE with one median; the $G$-independence audit ($G^1$ block;
$C$ a collapsing ideal; diagonal fiber $\equiv\{b,T,e_G,m\}$; off-diagonal
strands no pair) passes for all five; both controls FAIL for all five. Report:
`artifacts/reports/uniform-selective-median-theorem-check.json`.

## Uniform Selective-Median Theorem (Pass 39)

The Pass 37/38 escapes were verified group by group. Pass 39 proves the
statement for *all* finite $G$ at once, by naming the algebra of
$B_N^{\mathrm{med}}$ correctly. The nonzero, non-unit multiplicative part
$M^\ast=F\cup\{m\}\cup C$ (with $C=\{a_{N+1},s,U\}$) is an **ideal extension**
$$ G^1 \;\hookrightarrow\; M^\ast \;\twoheadrightarrow\; \{U\}, $$
where $F\cup\{m\}\cong G^1$ is the group $G$ with a *freshly adjoined* identity
$m$, and $C$ is a two-sided ideal on which every product collapses to $U$. The
subtlety: $m$ is the block's two-sided identity ($m\otimes g=g\otimes m=g$,
$m^2=m$), while the group identity $e_G=a_1$ is **not** the block identity
($e_G\otimes m=e_G\ne m$). Two distinct two-sided identities cannot coexist in a
monoid, and they don't — $G$ embeds in $G^1$ as a subsemigroup that is *not* a
submonoid. Everything below is independent of the Cayley table of $G$.

**Lemma 1 (Associativity, $G$-free).** $\otimes$ is associative. *Proof.* $b$
absorbs, $T$ neutralizes. On $M^\ast$: $F\cup\{m\}\cong G^1$ is a monoid; $C$ is
a two-sided ideal with $U\otimes z=z\otimes U=U$ for nonzero non-unit $z$, so any
triple touching $C$ short-circuits to $U$ in both bracketings (and $F\cup\{m\}$
is closed, so the untouched factors never produce a non-$U$ value). Ideal-
extension associativity, table-independent. $\square$

**Lemma 2 (Two-sided monotonicity, $G$-free).** Check the order covers
$s\prec a_{N+1}$, $T\prec m$, $a_1\prec m$. The group enters *only* via
$a_1\otimes a_j=a_j=m\otimes a_j$, which holds precisely because $a_1=e_G$ is the
identity; no other table entry is consulted. The front $F_k$ being an antichain
permuted by translation means front products never violate order. $\square$

**Lemma 3 (Fiber classification, $G$-free).** Every left fiber
$L(a,c)=\{x:a\otimes x\le c\}$ is principal; the front-inverting
anti-automorphism $\phi(a_i)=a_{i^{-1}}$ (identity off $F$, order-automorphism,
$\phi(x\otimes y)=\phi(y)\otimes\phi(x)$) carries left fibers to right fibers, so
right fibers are principal too. *Proof.* The only nontrivial multiplier is
$a_p\in F$, with $a_p\otimes x=b\,(x{=}b)$, $a_p\,(x{\in}\{T,m\})$,
$a_{pq}\,(x{=}a_q)$, $U\,(x{\in}C)$. For $c=a_r$: if $r\ne p$ the fiber is
$\{b,a_{p^{-1}r}\}$ (the unit $T$ drops out, **no pair stranded**, max
$a_{p^{-1}r}$); if $r=p$ the fiber is $\{b,T,a_1,m\}$ (the stranded pair is
$\{T,a_1\}$ for **every** $p$, capped by the single $m=T\vee a_1$). For $c=m$,
$c\in\{b,T,a_{N+1},s\}$, $c=U$: principal by inspection. $\square$

**Theorem (Uniform Non-Abelian Selective-Median Residuation).** For every finite
group $G$ and $N=\lvert G\rvert$, $B_N^{\mathrm{med}}$ with front $F_k\cong G$
carries an associative, two-sided monotone, $T$-unital, fully two-sided
residuated tensor with forced $\boxtimes m=b$ (antitonicity preserved, profile
intact). The diagonal fibers are $a_p\backslash a_p=a_p/a_p=\{b,T,e_G,m\}$ (max
$m$) for all $p$. Hence the maximum admissible front-group order is
$\lvert G\rvert=\infty$ and the number of medians needed is exactly $1$,
uniformly — independent of $\lvert G\rvert$, conjugacy-class count, and
normality structure. $\blacksquare$

*Reading.* The Pass 34–36 rigidity ceiling ($\lvert G\rvert=1$) and its Pass
37/38 collapse are now one phenomenon: $B_N$ lacked exactly one join, $T\vee
e_G$, and supplying it repairs *all* diagonal fibers because they strand the
*same* pair. Non-commutativity, large conjugacy-class counts, and exotic
normality structure are all irrelevant — front rigidity and its repair are
order-theoretic, group-theoretically uniform facts.

*Status.* Lemmas 1–3 proved $G$-independently above. Empirically reconfirmed
past the old $\lvert G\rvert\le8$ ceiling by
`code/scripts/check-uniform-selective-median-theorem.py` on the battery
$\mathbb Z/6$, $(\mathbb Z/2)^3$, $D_5$, $A_4$ (smallest group violating the
converse of Lagrange — a pathological stress test), $S_4$ (order 24, carrier
30): all five ESCAPE with one median; the $G$-independence audit ($G^1$ block;
$C$ a collapsing ideal; diagonal fiber $\equiv\{b,T,e_G,m\}$; off-diagonal
strands no pair) passes for all five; both controls FAIL for all five. Report:
`artifacts/reports/uniform-selective-median-theorem-check.json`.

## Median Uniqueness & Infinite-Front Dichotomy (Pass 40)

Pass 37–39 supplied *a* repair for front-group rigidity: adjoin one median
$m=T\vee e_G$ with $\downarrow m\cap M_0=\{b,T,e_G\}$, $\uparrow m=\{U\}$. Pass
40 sharpens this in two directions — the repair is *unique*, and it is
*cardinality-free* (residuation), though the orbit/profile is not.

**Definition ($\mathcal M$, admissible medians).** Fix the $B_N^{\mathrm{med}}$
order minus its median, $M_0$, with collapsing ideal $C=\{a_{N+1},s,U\}$ and
front $F\cong G$. A *candidate median* is a single fresh element $m'$ with
$m'<U$; the tensor is extended by the monotone-forced least rule $a\otimes
m':=\bigvee\{a\otimes z: z\le m'\}$ (and $m'\otimes m'=m'$, $T\otimes m'=m'$).
$m'$ is *admissible* iff the extended $\otimes$ stays monotone and every diagonal
fiber $a_p\backslash a_p$ ($a_p\in F$) is principal. (The Pass-40 uniqueness and
cardinality-freeness results are recorded in `research/definitions.md` and the
report `artifacts/reports/median-uniqueness-check.json`; the original full write
of this section was truncated by a crashed run and is restored only in summary
here.)

## Attachment / Loeb Dividing Line (Pass 44)

Passes 41–43 isolated, at successively more concrete levels, *which* condition
forces a $\boxtimes$-fixed point to be orbit-attached. Pass 41a: all-level nFG2
($\boxtimes^{k+1}T\le\boxtimes^kT$, $\forall k\ge1$) forces index-2 orbit
stabilization, hence an attached reachable fixed point. Pass 42: the $M_3$ Rosser
gadget $R_2$ realizes FP-synt with a *detached* fixed point and **no** attached
one. Pass 43: at the Kripke level, formalized Loeb (D3, GL) forces the Goedel
fixed point of $x\mapsto\neg\Box x$ to equal $\mathrm{Con}=\boxtimes\bot$ (de
Jongh–Sambin uniqueness), hence attached; monotonicity (D2) alone does not. Pass
44 lifts the gate back to the abstract APS level and calibrates the exact
fragment.

**Definition (orbit-descent).** For antitone $\boxtimes$ with consistency orbit
$o_n:=\boxtimes^n T$, the orbit *descends* iff $\exists k\,(o_{k+1}=o_k)$. On a
finite $L$ this is equivalent to the orbit not being a non-trivial
$\boxtimes$-cycle. Since $g:=\boxtimes\circ\boxtimes$ is monotone, the iterates
$g^n(T)$ form a monotone sequence converging (on finite $L$) to a $g$-fixed
point; descent says this $g$-limit is already a $\boxtimes$-fixed point on the
orbit. Orbit-descent is the order-theoretic shadow of formalized Loeb.

**Theorem 44a (descent $\Rightarrow$ attachment & uniqueness).** If the orbit of
$T$ descends, its stable value $o_k$ is a $\boxtimes$-fixed point, is the unique
orbit-limit fixed point, and is orbit-attached. *Machine-verified on $M_3$:* of
the $178$ antitone self-maps, all $66$ with a descending orbit satisfy the
conclusion (0 violations). This is the finite shadow of de Jongh–Sambin
uniqueness (Pass 43a).

**Theorem 44b (detached-only $\Rightarrow$ non-descent $\Rightarrow \neg$FG2(1)).**
If $\boxtimes$ has a detached fixed point and no attached fixed point, then its
orbit is a non-descending cyclic antichain and FG2(1) ($\boxtimes^2T\le\boxtimes
T$) fails. *Verified:* exactly $2$ antitone maps on $M_3$ are detached-only; both
have non-descending orbits with FG2(1) false. The Rosser gadget $R_2$ is one.

**Theorem 44c (sharpness — $\neg$FG2(1) is necessary but NOT sufficient).** On the
same carrier $M_3$, the antitone map $x\mapsto y\mapsto z\mapsto z$ (with
$\bot\leftrightarrow\top$) fails FG2(1) — $o_2=z\not\le y=o_1$, the $M_3$ middle
atoms being pairwise incomparable — yet descends to the attached fixed point $z$
at index $2$. Thus $R_2$ (detached-only) and this map *both* fail FG2(1) but
differ in attachment.

**Corollary (tower calibration).** The attachment dividing line is
**orbit-descent**, strictly finer than $\neg$FG2(1): FG2(1) sits *below* the true
line. The Pass-41a hypothesis "all-level nFG2" is sufficient for attachment but
far from necessary; the precise necessary-and-sufficient abstract gate on finite
$L$ is orbit-descent = the algebraic Loeb shadow.

**Proof obligations.** Extend "descent $\Leftrightarrow$ unique attached fixed
point" from $M_3$ to arbitrary finite $L$ (the $g=\boxtimes^2$ monotone-convergence
argument is carrier-independent; the no-attached-FP half of the dichotomy needs a
general lemma), and to infinite $L$ under an orbit well-foundedness /
no-infinite-descent condition. Verified by
`code/scripts/check-attachment-loeb-dividing-line.py` /
`artifacts/reports/attachment-loeb-dividing-line-check.json` (overall PASS).

*References.* D. Guaspari & R. M. Solovay, "Rosser sentences," *Ann. Math. Logic*
16 (1979) 81–99; C. Smoryński, *Self-Reference and Modal Logic* (Springer, 1985),
ch. on the de Jongh–Sambin fixed-point theorem; T. Kurahashi, "Rosser-type
provability predicates" (2021).
fiber $a_p\backslash a_p$ ($a_p\in F$) is principal. $\mathcal M$ is the poset of
admissible medians ordered by $\downarrow$-inclusion.

**Theorem 40a (Least = unique repair).** For every finite group $G$, $\mathcal M$
is a *singleton*: the only admissible median is $m=T\vee e_G$, with $\downarrow
m\cap M_0=\{b,T,e_G\}$ and $\uparrow m=\{U\}$.

*Proof.* Admissibility forces $\{b,T,e_G\}\subseteq\downarrow m'\not\ni U$.
Suppose $z\in\downarrow m'\setminus\{b,T,e_G\}$. If $z\in C$ or $z$ is a tail
element, then $a_p\otimes z=U$ for every front $a_p$, so monotonicity forces
$a_p\otimes m'\ge U$, hence $a_p\otimes m'=U\not\le a_p$ and $m'\notin
a_p\backslash a_p$; the diagonal fiber reverts to $\{b,T,e_G\}$ with the
incomparable pair $\{T,e_G\}$ maximal — non-principal, contradiction. If
$z=a_q\in F$ with $q\ne e$, then $a_p\otimes m'\ge a_p\otimes a_q=a_{pq}$, an
atom incomparable to $a_p$ (since $pq\ne p$ for $q\ne e$ in a group), so again
$a_p\otimes m'\not\le a_p$. Thus $\downarrow m'\cap M_0=\{b,T,e_G\}$. Dually,
$m'\le t$ for a tail/ideal $t$ drags $t$ into the diagonal fiber with
$a_p\otimes t=U$ — ejection; so $\uparrow m'=\{U\}$. Both data pinned:
$m'=m=T\vee e_G$. $\square$

This is the **Cap-Ejection lemma (Pass 36) read backwards**: the very forcing
that ejected a ceiling over the whole front ejects *any* element a candidate
median dares to dominate beyond the obstructing pair $\{T,e_G\}$.

**Corollary 40a′ (Representability / freeness).** $G\mapsto(R(G),m)$ is a
representable construction: $m$ is the join $T\vee e_G$ taken in the largest
sub-join-subsemilattice of $\downarrow U$ avoiding $C$ and $F\setminus\{e_G\}$.
Being the sole element of $\mathcal M$, $m$ is at once initial and terminal — the
selective-median functor sends each finite group to its *unique* universal
repair; there is no moduli of medians.

**Theorem 40b (Residuation cardinality-free; orbit not).** Let $G$ be *any*
group. (1) $R(G)$ with median $m$ is a fully two-sided residuated poset: every
residual fiber is either $\le 4$ elements (diagonal $\{b,T,e_G,m\}$ or
off-diagonal $\{b,a_{p^{-1}r}\}$) or the whole carrier (cofinal at $U$). *No
proper infinite fiber occurs*, so all residuals exist without infinitary suprema
beyond the absorbing top; Theorems 40a and the Pass-39 Uniform Selective-Median
Theorem hold verbatim for $\mathbb Z,\mathbb Q,S_\infty$. (2) If the same front
carries the $\boxtimes$-orbit, the nFG2/FP profile is *not* cardinality-free:
the orbit $T\to a_1\to a_2\to\cdots$ has no terminal stage, nFG2($k$) is false
for all finite $k$, and FP-synt fails unless one adjoins the limit fixed point
$s_\omega:=\bigwedge_{n<\omega}\boxtimes^n T$ with $\boxtimes s_\omega=s_\omega$.

*Proof.* (1) The only non-trivial multiplier is a front atom $a_p$, whose
$\otimes$-values are $b,a_p,a_{pq},U$; the preimage of any $\downarrow c$ is one
of the listed $\le4$-element sets or the whole carrier. The bound $4=\lvert
\{b,T,e_G,m\}\rvert$ is $\lvert G\rvert$-independent. Right fibers transfer via
the anti-automorphism $\phi$. (2) The descending antitone chain $\boxtimes^n T$
stabilizes at a fixed point iff its meet exists and is $\boxtimes$-fixed — the
infinite-orbit-stabilization obstruction already on file. $\square$

**Greedy-median pathology (病的な例).** The candidate $m^\sharp$ with $\downarrow
m^\sharp=\{b,T,e_G,s,a_{N+1}\}$ dominates *more* of the obstruction's
neighbourhood, yet repairs *nothing*: monotonicity forces $a_p\otimes
m^\sharp\ge a_p\otimes s=U$, so $m^\sharp$ is ejected from every diagonal fiber.
In $\mathcal M$, "do the minimum" and "do the only possible thing" coincide; any
attempt to "help more" by sinking the median deeper into the order is exactly
what breaks it.

## Limit-FP Obstruction & Median Tower (Pass 41)

Pass 40 left $s_\omega:=\bigwedge_{n<\omega}\boxtimes^n T$ on the table as a
proposed *orbit-limit fixed point* completing an infinite $\boxtimes$-orbit, and
asked whether the singleton uniqueness $\mathcal M=\{T\vee e_G\}$ degrades to a
tower of medians once $s_\omega$ enters. Pass 41 settles both: $s_\omega$ is a
**phantom** (no antitone operator admits an order-attached orbit-limit fixed
point), and the multi-pair median geometry is a *product of singletons* with a
genuinely phantom limit median under failure of meet-continuity.

**Theorem 41a (Antitone index-2 collapse).** Let $(L,\le,\boxtimes)$ be an APS
($\boxtimes$ antitone) and $X_k:=\boxtimes^k T$. If all-level nFG2 holds —
$X_{k+1}\le X_k$ for every $k\ge1$ — then $X_2=X_3$; the orbit stabilizes at
index $2$ and $p:=X_2$ satisfies $\boxtimes p=p$.

*Proof.* nFG2$(1)$ gives $X_2\le X_1$. Apply antitone $\boxtimes$:
$\boxtimes X_1\le\boxtimes X_2$, i.e. $X_2\le X_3$. nFG2$(2)$ gives $X_3\le X_2$.
By antisymmetry $X_2=X_3$, hence $\boxtimes X_2=X_3=X_2$. $\square$

The corollary corrects the Pass-40 proof of 40b(2): an infinite *strictly*
nFG2-descending orbit cannot exist. All-level nFG2 is **self-truncating at depth
2** — no well-foundedness, no-infinite-descent, or completeness hypothesis is
needed. An infinite orbit is therefore *necessarily* the $\boxtimes$-antichain
regime, where nFG2 fails cofinally and there is no descending chain to take a
meet of in the first place.

**Theorem 41b (Limit-FP obstruction).** Let $\{o_n\}_{n\ge0}$ be an infinite
$\boxtimes$-orbit forming a $\boxtimes$-antichain, $\boxtimes o_n=o_{n+1}$,
$\boxtimes$ antitone, and let $\sigma\notin\{o_n\}$ be fresh with
$\boxtimes\sigma=\sigma$. If $\sigma$ is order-related to the orbit — (i)
$\sigma\le o_n\ \forall n$ (a meet / the proposed $s_\omega$), (ii)
$\sigma\ge o_n\ \forall n$ (a join), or (iii) $o_j\le\sigma\le o_i$, $i\ne j$
(sandwiched) — then antitonicity forces an orbit identification, contradicting
the antichain. Hence the *only* antitone-compatible fixed point is order-
**incomparable** to the entire orbit: a *detached* fixed point, which neither
caps nor completes it.

*Proof.* (i) $\sigma\le o_n\Rightarrow\boxtimes o_n\le\boxtimes\sigma$, i.e.
$o_{n+1}\le\sigma$; with $\sigma\le o_{n+1}$ this gives $o_{n+1}=\sigma$ for all
$n$ — collapse. (ii) dual: $\sigma=\boxtimes\sigma\le\boxtimes o_n=o_{n+1}$ and
$\sigma\ge o_{n+1}$ give $\sigma=o_{n+1}$. (iii) $o_j\le\sigma\le o_i$ with
$\boxtimes\sigma=\sigma$ yields $o_{i+1}\le\sigma\le o_{j+1}$, so $o_{i+1}$ and
$o_{j+1}$ are comparable; itera

## Poset Bracketing, the Boolean Cube-Gap, and Period-$k$ Detachment (Pass 48)

Pass 47 (Thm 47d) settled the *chain* bracketing criterion — a comparable
eventual $2$-cycle $\{a,b\}$ on a finite chain brackets a fixed point iff the
invariant interval $[a,b]$ has odd cardinality — and left three residual
questions: the *poset* (non-chain) generalization, the infinite-$L$ lift of
flatness, and the period-$\ge4$ antichain thread. Pass 48 discharges all three
through one lens: **bracketing is a fixed-point question for an order-reversing
involution, and the governing invariant is the cycle type of $\boxtimes$ on
$\mathrm{Fix}(\boxtimes^2)$, never the cardinality of the interval.**

### The bracketing involution and the parity criterion

Let $\boxtimes$ be antitone on a finite poset $L$ with a comparable eventual
$2$-cycle $\{a,b\}$, $a<b$, $\boxtimes a=b$, $\boxtimes b=a$. Put $I=[a,b]$ and
$F=\mathrm{Fix}(\boxtimes^2)\cap I$.

**Theorem 48a (poset bracketing = involution fixed point; parity sufficiency).**
$I$ is $\boxtimes$-invariant, $g=\boxtimes^2|_I$ is monotone with least element
$a$, so $F\neq\varnothing$ by Abian–Brown, and $a,b\in F$. The restriction
$\tau:=\boxtimes|_F$ is an *order-reversing involution* of the finite poset $F$
with $\tau a=b$, $\tau b=a$. One has
$$\mathrm{Fix}(\boxtimes)\cap I=\mathrm{Fix}(\tau),\qquad
|F|\ \text{odd}\ \Longrightarrow\ \mathrm{Fix}(\tau)\neq\varnothing .$$
On a chain $\boxtimes^2|_I=\mathrm{id}_I$, whence $F=I$ and 48a collapses to
Thm 47d (odd $|I|$).

*Proof.* Invariance: for $x\in I$, $a=\boxtimes b\le\boxtimes x\le\boxtimes a=b$.
$g=\boxtimes\circ\boxtimes$ is monotone (composite of two antitone maps); a finite
poset with a least element is chain-complete, so Abian–Brown gives
$\mathrm{Fix}(g)\neq\varnothing$, and $ga=\boxtimes(\boxtimes a)=\boxtimes b=a$,
$gb=\boxtimes(\boxtimes b)=\boxtimes a=b$, so $a,b\in F$. On $F$,
$\boxtimes^2=\mathrm{id}$, so $\boxtimes$ is a bijective involution of $F$;
antitonicity makes it order-reversing. A $\boxtimes$-fixed point of $I$ is
$\boxtimes^2$-fixed, hence lies in $F$, so $\mathrm{Fix}(\boxtimes)\cap I=
\mathrm{Fix}(\tau)$. Finally $\#\mathrm{Fix}(\tau)\equiv|F|\pmod 2$ because the
non-fixed points of an involution pair up. $\square$

The criterion is **one-way**: odd $|F|$ forces bracketing, but even $|F|$ is
indeterminate, and — crucially — the relevant parity is that of $F$, *not* of
$I$.

### The Boolean cube-gap (病的な例)

**Pathology.** Take $L=2^{[n]}$ (the Boolean cube) with $\boxtimes S=S^c$
(set-complementation). Then $\boxtimes$ is antitone, $\boxtimes^2=\mathrm{id}$, the
*unique* comparable $2$-cycle is $\{\varnothing,[n]\}$, the invariant interval is
all of $2^{[n]}$, $|I|=2^n$, and $\mathrm{Fix}(\boxtimes)=\varnothing$ (since
$S=S^c$ is impossible). This is a **cube-gap**: a fat, even, comparable $2$-cycle
that brackets *nothing* — the $2^n$-element analogue of the even-chain Rosser gap
$C_{2m}$ and of the $M_3$ Rosser gadget $R_2$. Yet the *same* lattice $2^2$ carries
a *different* order-reversing involution, $\tau'=(\hat0\,\hat1)$ fixing the two
atoms, with $\#\mathrm{Fix}(\tau')=2$. Hence neither $|I|$ nor its parity controls
bracketing; only the cycle type of $\boxtimes|_F$ does. The naive lift of Thm 47d
("odd interval $\Rightarrow$ bracket") is *false* for posets, and the cube is the
counterexample.

**Remark (homological shadow).** $\tau$ acts simplicially on the order complex
$\Delta(F)$, which is contractible ($F$ has $\hat 0$), so the Lefschetz number is
$1\neq0$ and $\tau$ fixes a *chain* (an invariant flag). An order-reversing $\tau$
reverses a fixed chain $x_0<\dots<x_m$ as $x_i\mapsto x_{m-i}$; this yields a
fixed *vertex* (the midpoint $x_{m/2}$, a $\boxtimes$-fixed point) iff $m$ is
even, i.e. the chain has an odd number of vertices. Thus the parity count of
48a is the Euler-characteristic shadow of an equivariant statement; upgrading the
one-way bound to an iff via $\mathbb Z/2$-Smith theory on $F^\tau$ is a proof
obligation (Pass 49 target).

### Infinite-$L$ lift: join-continuity, not well-foundedness

**Theorem 48b (flatness lift).** Let $\boxtimes$ be antitone on a complete
lattice $L$, $T\le\boxtimes^2 T$ (the even orbit ascends),
$a^\ast=\bigvee_n\boxtimes^{2n}T$, $b^\ast=\bigwedge_n\boxtimes^{2n+1}T$. If
$\boxtimes$ is **join-continuous** ($\boxtimes\bigvee=\bigwedge\boxtimes$) then
$\boxtimes a^\ast=b^\ast$, $\boxtimes b^\ast=a^\ast$: the limit pair is a
*realized* $2$-cycle, so Thm 47b lifts — a flat orbit forbids limit chain-cycles
because any limit pair is itself the attained eventual cycle, to which flatness
applies. The hypothesis is continuity of $\boxtimes$, **independent of
well-foundedness of $L$**.

*Proof.* By monotonicity of $\boxtimes^2$ the even orbit ascends to $a^\ast$;
join-continuity gives $\boxtimes a^\ast=\boxtimes\bigvee_n\boxtimes^{2n}T=
\bigwedge_n\boxtimes^{2n+1}T=b^\ast$, and dually $\boxtimes b^\ast=a^\ast$.
$\square$

**Phantom (discontinuous half).** Drop join-continuity and the Thm-41c phantom
returns: there is an antitone $\boxtimes$ with $o_{2n}\uparrow a^\ast$ but
$\boxtimes a^\ast<\bigwedge_n\boxtimes o_{2n}=b^\ast$ strictly — a limit
chain-cycle that the orbit approaches but never closes. This is the operator-form
of the median-tower phantom of Thm 41c; the explicit witness lattice is a Pass-49
construction target, conjecturally calibrated by a single failed cover on the
meet-continuity dividing line.

### Period-$k$ antichain cycles force detachment

**Proposition 48c (period-$k$ detachment).** Suppose $\boxtimes p=p$ and
$\{o_0,\dots,o_{k-1}\}$ ($k\ge2$, $\boxtimes o_i=o_{(i+1)\bmod k}$) is a
$\boxtimes$-antichain cycle. Then $p$ is comparable to no $o_i$ — the fixed point
is *detached*. *Proof.* If $p\le o_i$, applying $\boxtimes$ twice gives
$o_{i+1}\le p$ and $p\le o_{i+2}$, so $o_{i+1}\le o_{i+2}$, contradicting the
antichain; dually for $p\ge o_i$. For odd $k$ the inequality chain even forces
$p=o_i$, contradicting $\boxtimes p=p\ne o_{i+1}$. $\square$

Thus FP-synt ($\exists p\,p=\boxtimes p$) coexists with an eventual period-$k$
antichain cycle for **every** $k\ge2$, the fixed point always detached. This
generalizes Thm 41b (infinite antichain *orbit* $\Rightarrow$ detached limit FP)
to finite antichain *cycles* of any period, and Pass 42's $R_2$ ($k=2$) to the
whole family of **period-$2k$ Rosser gadgets** $R_{2k}$.

**Witness $R_4$.** Carrier $\{b,o_0,o_1,o_2,o_3,p,U\}$; $b$ least, $U$ greatest,
$\{o_0,o_1,o_2,o_3,p\}$ a $5$-antichain; $\boxtimes$ the $4$-cycle $o_0\to o_1\to
o_2\to o_3\to o_0$, $\boxtimes p=p$, $\boxtimes b=U$, $\boxtimes U=b$. Then
$\boxtimes$ is antitone, the eventual cycle from $T=o_0$ is the $4$-antichain
$\{o_0,o_1,o_2,o_3\}$, the sole fixed point is $p$, and $p$ is detached. $R_4$ is
the period-$4$ Rosser gadget; its $\boxtimes^2$ acts as two $2$-cycles
$(o_0\,o_2)(o_1\,o_3)$, a free $\mathbb Z/2$ on the antichain front.

### Machine verification

`code/scripts/check-poset-bracketing-period4.py`
(`artifacts/reports/poset-bracketing-period4-check.json`, overall **PASS**):
(A) the parity criterion has $0$ violations over all antitone maps on
$C_2,\dots,C_5$ and $2^2$ carrying a comparable $2$-cycle ($135$ map-instances;
$\mathrm{Fix}(\boxtimes)\cap I=\mathrm{Fix}(\tau)$ in every case, and every
odd-$|F|$ case brackets); (B) the cube-gap holds for $2^{[1]},\dots,2^{[4]}$
(comparable $2$-cycle $\{\varnothing,[n]\}$, interval sizes $2,4,8,16$, no
$\boxtimes$-fixed point), while the alternative $2^2$ involution has fixed points
$\{1,2\}$; (C) $R_4$ is antitone with a $4$-antichain eventual cycle and sole
detached fixed point $p$, and forcing $p\le o_0$ destroys antitonicity for
$k=2,3,4,5$.

---

## Pass 49 — Smith bracketing, the explicit phantom, and group-orbit liberation

Pass 48 left three residues; Pass 49 closes all three. Throughout, $\{a,b\}$ is a
comparable eventual $2$-cycle of an antitone $\boxtimes$ ($a<b$), $I=[a,b]$,
$F=\mathrm{Fix}(\boxtimes^2)\cap I$, and $\tau=\boxtimes|_F$ is the order-reversing
involution with $\tau(a)=b$.

### Theorem 49a (Smith bracketing criterion)

Let $\Delta(F)$ be the **order complex** of $F$ (simplices = nonempty chains of
$F$). Then:

1. $\Delta(F)$ is $\mathbb F_2$-acyclic: $a=\min F$ is a cone apex, so $\Delta(F)$
   is a cone $a\ast\Delta(F\setminus\{a\})$, hence contractible.
2. $\tau$ is a simplicial $\mathbb Z/2$-action (order-reversing maps chains to
   chains). By **Smith theory** (P. A. Smith 1941; Bredon, *Introduction to
   Compact Transformation Groups*, Academic Press 1972, Ch. III, Thm 7.11) the
   fixed subcomplex $|\Delta(F)|^{\tau}$ is nonempty and $\mathbb F_2$-acyclic,
   and the simplicial Lefschetz number is $L(\tau)=\chi(\Delta(F))=1$.
3. **Criterion.**
   $$
   \boxtimes \text{ brackets a fixed point in } I
   \;\Longleftrightarrow\;
   |\Delta(F)|^{\tau}\ \text{contains a } 0\text{-cell}
   \;\Longleftrightarrow\;
   \exists\ \tau\text{-invariant chain of } F \text{ of ODD cardinality.}
   $$
   A $\tau$-invariant chain $c$ (i.e. $\tau(c)=c$ as a set) is order-reversed by
   $\tau$; if $|c|$ is odd its middle element is a $\tau$-fixed vertex, i.e. a
   $\boxtimes$-fixed point. The **odd-$|F|$** sufficiency of Thm 48a is exactly
   the case where $F$ itself is a single odd invariant chain.

Smith theory thus reduces the question "does $\tau$ fix *something*" (answer:
always, by acyclicity) to the strictly finer combinatorial gate "does the fixed
set meet the $0$-skeleton". The Lefschetz number is identically $+1$ and never
forces a *vertex* — it is consistent with, not stronger than, the Smith reduction.

### The cube-gap as a flipped-edge barycenter

For $F=2^{[n]}$ with $\tau(S)=[n]\setminus S$: an invariant chain must pair each
$S$ with its complement, so every $\tau$-invariant chain has EVEN cardinality and
no fixed vertex. The fixed subcomplex $|\Delta(2^{[n]})|^{\tau}$ degenerates to
the single **barycenter of the flipped top edge** $\{\varnothing,[n]\}$: nonempty
and acyclic (a point), exactly as Smith demands, but a $1$-cell midpoint carrying
no $0$-cell. The cube-gap is not a counterexample to Smith's theorem; it is
Smith's theorem realized on an *edge barycenter* instead of a vertex. By contrast
the alternative order-reversing involution of the *same* poset $2^2$, the one with
$\mathrm{Fix}=\{1,2\}$, has its fixed set on the $0$-skeleton, so it brackets —
confirming once more that the controlling datum is the cycle type of $\tau$ on
$\Delta(F)$, not $|I|$.

### Construction 49b (explicit phantom; one failed cover suffices)

Let $P$ be the complete lattice
$$
P=\{o_0<o_1<o_2<\cdots\}\ \cup\ \{a^{*}=\textstyle\bigvee_n o_n\}\ \cup\ \{m\}\
\cup\ \{b^{*}\}\ \cup\ \{\top\},
$$
with covers $a^{*}\prec m$, $a^{*}\prec b^{*}$, $m\prec\top$, $b^{*}\prec\top$
(so $a^{*}$ has **two** distinct covers $m,b^{*}$ — the single node where
join-continuity is allowed to fail). Define an antitone $\boxtimes$ that flips the
even rungs $o_{2n}$ upward, $\boxtimes(o_{2n})\uparrow b^{*}$, while
$\boxtimes(a^{*})=m$. Then
$$
\boxtimes\!\Big(\bigvee_n o_{2n}\Big)=\boxtimes(a^{*})=m \;<\; b^{*}
=\bigvee_n \boxtimes(o_{2n}),
$$
so $\boxtimes$ fails join-continuity at the lone cover $a^{*}\prec\{m,b^{*}\}$ and
the limit $2$-cycle becomes **phantom** (Thm 41c). Machine truncations $K=2,\dots,6$
confirm that antitonicity and continuity break ONLY at $a^{*}$. Hence **one** failed
join-cover already reinstates the phantom: join-continuity in Thm 48b cannot be
relaxed to "continuous off a finite set."

### Theorem 49d (group-orbit liberation under residuation)

Front rigidity (Pass 34/35) forbids a nontrivial finite group as a commutative
residuated *tensor* on a $B_N$ front ($|G|=1$). It does **not** forbid a free
group *orbit* of the refutability map $\boxtimes$ carrying a detached fixed point,
provided the carrier is the relation-free diamond rather than a $B_N$ front.

Concretely, $M_5=\{\bot,o_0,o_1,o_2,o_3,p,\top\}$ with $\boxtimes=\mathrm{id}$ on
the box and refutability the free $\mathbb Z/4$-orbit
$(o_0\,o_1\,o_2\,o_3)$ together with the detached fixed point $\boxtimes p=p$
admits a commutative full-residuated tensor whose **unit is the non-integral
element $p$** (equivalently $o_0$). The machine census gives:

- **411** commutative residuated unital tensors with unit $=p$ (and $411$ with
  unit $=o_0$ — the $S_4$ front-symmetry classes), and
- **0** integral tensors (unit $=\top$).

The integral obstruction is the $M_n$ ($n\ge3$) phenomenon: the residual
$\top\backslash\bot$ has the non-principal fiber $\{b\}\cup(\text{atoms}\setminus\{a\})$,
so no residual exists with the top as unit. The escape therefore **requires** a
non-integral unit — precisely the degree of freedom $B_N$'s tail-coupled
$\top$-unit never possessed. The detached fixed point $p$ doubling as the tensor
unit is the algebraic crux: FP-synt and the monoidal identity are realized at the
*same* point, which is exactly why the orbit and the residuation coexist.

Witness model: `code/models/examples/R4-residuated.json`. Verification:
`code/scripts/check-pass49.py` →
`artifacts/reports/pass49-bracketing-phantom-grouporbit-check.json`,
`{"A":true,"B":true,"C":true,"PASS":true}`.

### Pathology gallery

- **Cube-gap** ($2^{[n]}$ / complementation): fat even interval, Smith fixed set
  = a single edge barycenter, no bracket.
- **Same-poset split**: the two order-reversing involutions of $2^2$ — one
  brackets ($\mathrm{Fix}=\{1,2\}$, fixed $0$-cell), one is a cube-gap
  ($\mathrm{Fix}$ on the flipped diagonal edge). $|I|=4$ for both: parity of $|I|$
  is *not* the invariant.
- **One-cover phantom**: a single doubled cover at $a^{*}$ converts a would-be
  continuous limit $2$-cycle into a phantom.
- **Non-integral unit liberation**: $411$ residuated $R_4$ tensors with detached
  unit $p$, but $0$ integral — the group orbit lives precisely where the integral
  $B_N$ rigidity cannot reach.

## Pass 50 — Bredon vertex-bracket identity, the phantom Betti number, and front-cardinality decoupling

Pass 49 left three residues; Pass 50 closes all three.

**Thm 50a (Bredon vertex-bracket identity).** Let $\tau=\boxtimes|_F$ be the
order-reversing involution of $F=\mathrm{Fix}(\boxtimes^2)\cap I$, acting
simplicially on the $\mathbb F_2$-acyclic order complex $\Delta(F)$ (cone, apex
$a=\min F$). Smith theory makes $|\Delta(F)|^{\tau}$ nonempty and acyclic, so the
*topological* Euler characteristic $\chi(|\Delta(F)|^{\tau})=1$ identically — it
cannot see the $0$-skeleton gate of Thm 49a. The vertex-counting refinement is
$$ e(F^{\tau}) \;:=\; \chi\!\big(\Delta(F^{\tau})\big), \qquad
   F^{\tau}=\{x\in F:\boxtimes x=x\}\ \text{(self-dual subposet),} $$
the Euler characteristic of the order complex of the self-dual subposet. Splitting
the simplicial Lefschetz number by the orbit type of each $\tau$-invariant chain
(pointwise-fixed $\Leftrightarrow$ contained in $F^{\tau}$, else flipped) gives the
**identity**
$$ L(\tau)\;=\; e(F^{\tau})\;+\;\Phi(\tau)\;=\;1, $$
with $\Phi(\tau)$ the signed count of flipped invariant chains. Hence $\boxtimes$
brackets iff $F^{\tau}\ne\varnothing$, and on every comparable-2-cycle test family
$e(F^{\tau})\ne0$ iff bracket. The **cube-gap** $F=2^{[n]}$ (complementation) is the
extremal $e=0,\Phi=1$: the lone flipped edge $\{\varnothing,[n]\}$ carries all of
$L$. _(Verified: $\,$cubes $2^1,2^2,2^3$ and $C_4$ give $(e,\Phi)=(0,1)$, no
bracket; $C_5$ and the $3$-chain give $(1,0)$; the $2^2$ alternative involution
gives $(2,-1)$; every row $e+\Phi=1$.)_

**Constr 50b (phantom Betti number; additivity of failed covers).** Let $P_r$ be
the fan of $r$ order-independent copies of the Constr-49b even-orbit arm, sharing
only $\bot,\top$. Then $\boxtimes$ is globally antitone, its join-continuity fails
at exactly the $r$ limit covers $a_1^{*},\dots,a_r^{*}$, and
$$ b_{\mathrm{phantom}}(P_r)\;=\;\#\{\text{failed join-covers}\}\;=\;r. $$
Phantoms are additive: Constr 49b is the atom $r=1$, and independent
discontinuities contribute independent phantom $2$-cycles $(a_i^{*},b_i^{*})$.
_(Verified $r=1,2,3$: each globally antitone, failed covers $=$ phantom $2$-cycles
$=r$.)_

**Thm 50d (front-cardinality decoupling of group-orbit liberation).** For every
finite group $G$, the relation-free diamond $M_{|G|+1}$ (front atoms $o_g$,
detached $\boxtimes p=p$, refutability a free $G$-orbit on the front) admits a
commutative full-residuated tensor with **non-integral** unit $p$, and $0$
integral (unit $=\top$) ones whenever $|G|\ge3$ (the $M_n$, $n\ge3$, residual
obstruction: $\top\backslash\bot$ has the non-principal fiber
$\{b\}\cup(\text{atoms}\setminus\{a\})$). Exact counts $R(3)=56$, $R(4)=411$
(reproducing Pass 49); and $R(n)\ge1$ for all $n$ via the explicit witness family
$$ p=\text{unit},\quad o_0\otimes x=o_0,\quad o_i\otimes o_j=\top\ (i,j\ge1),
   \quad o_i\otimes p=o_i. $$
Crucially the *commutative* tensor never references the multiplication of $G$:
abelian and non-abelian fronts of equal cardinality are
residuation-indistinguishable. **The group law lives solely in the refutability
orbit; the residuated layer sees only $|G|=n$** — a decoupling of provability-side
structure (full $G$) from algebraic structure (front cardinality). _(Free $S_3$
orbit, $|G|=6$, verified antitone with detached $p$.)_

Machine verification: `code/scripts/check-pass50.py` $\to$
`artifacts/reports/pass50-bredon-phantomfan-grouporbit-check.json`
($\{A,B,C,\text{PASS}\}=$ all true).

## Pass 51 — Completeness/deflation of $e$, the phantom as $\varprojlim^1$, and Löb/Rosser $\leftrightarrow$ integral/non-integral unit

Pass 50 left three residues; Pass 51 closes all three, with one deflationary
surprise (the Bredon refinement of Pass 50 collapses to a vertex count) and two
upgrades (the phantom becomes a derived limit, the unit dichotomy becomes the
Löb/Rosser dividing line).

**Lemma 51a (fixed-point antichain).** For any antitone $\boxtimes:L\to L$, the
set $\mathrm{Fix}(\boxtimes)$ is an antichain: if $p\le q$ with $\boxtimes p=p$,
$\boxtimes q=q$, then $q=\boxtimes q\le\boxtimes p=p$, so $p=q$. $\square$

**Thm 51a (completeness/deflation of $e(F^{\tau})$).** With $F=\mathrm{Fix}
(\boxtimes^2)\cap I$, $\tau=\boxtimes|_F$, the self-dual subposet
$F^{\tau}=\mathrm{Fix}(\boxtimes)\cap I$ is an antichain (Lemma 51a), so
$\Delta(F^{\tau})$ is a discrete $0$-complex and
$$ e(F^{\tau})=\chi(\Delta(F^{\tau}))=|F^{\tau}|\quad\text{identically.} $$
Hence $e$ is a *complete* bracket invariant — $e=0\iff F^{\tau}=\varnothing\iff
\boxtimes$ does not bracket — but the completeness is tautological: "$e=0$ with
$F^{\tau}\ne\varnothing$" is impossible, and the order-complex circle the Pass-50
follow-up sought is unrealizable as a fixed-vertex set. (The 6-crown $C_6$ — three
minima, three maxima, $x_i<y_i$, $x_i<y_{i-1}$ — has order complex $\simeq S^1$,
$\chi=0$, but it is not an antichain, so no order-reversing involution fixes its
vertices.) The genuine homological content is therefore the **flipped** term
$\Phi(\tau)=L(\tau)-e(F^{\tau})=1-|F^{\tau}|$, not $e$: Smith $+$ antitonicity
flatten the equivariant story to the single integer $|F^{\tau}|$. _(Verified: over
all antitone maps on all posets of size $\le5$, $0$ violations of "$\mathrm{Fix}$
antichain", "$e=|\mathrm{Fix}|$", "$e=0$ with $\mathrm{Fix}\ne\varnothing$"; the
$e$-spectrum by $|\mathrm{Fix}|$ is exactly $k\mapsto k$.)_

**Thm 51b (phantom Betti number as $\varprojlim^1$).** On the fan $P_r$ each arm
carries an ascending chain $o^i_0<o^i_1<\cdots$ with $\sup=a^*_i$; antitonicity
makes the image tower $\boxtimes o^i_0\ge\boxtimes o^i_1\ge\cdots$ descend to a
meet $\beta_i$, while $\boxtimes a^*_i=\gamma_i<\beta_i$ — the phantom is exactly
$\boxtimes(\bigvee_n o^i_n)\ne\bigwedge_n\boxtimes o^i_n$, the failure of
$\boxtimes$ to commute with the directed join, i.e. $\varprojlim^1$ of the image
tower. The obstruction complex
$$ \mathrm{Ob}^\bullet(P_r)=[\,0\to C^1\to0\,],\quad
   C^1=\mathbb F^{\{\text{failed join-covers}\}},\quad C^0=0, $$
($C^0=0$ = infinitary rigidity: no antitone interior perturbation closes a gap in
the completed lattice) has
$$ b_{\mathrm{phantom}}(P_r)=\dim_{\mathbb F}H^1(\mathrm{Ob}^\bullet(P_r))
   =\#\{\text{failed covers}\}=r, $$
additive because $\varprojlim^1$ commutes with finite direct sums. _Proof
obligations:_ (a) the integral $\varprojlim^1$ is genuinely nonzero — over a field
$\varprojlim^1$ of finite-dimensional towers is Mittag-Leffler hence $0$, so the
cohomology must be taken over $\mathbb Z$; (b) $C^0=0$ holds only in the
completion, since at every finite truncation the gap is removable ($\boxtimes
a^*_i:=\beta_i$ stays antitone). _(Verified at the finite level: $r=1,2,3$ each
globally antitone, exactly $r$ failed covers, gaps pairwise independent, finite
truncation gap-removable.)_

**Thm 51c (Löb/Rosser $\leftrightarrow$ integral/non-integral unit).** For
$\boxtimes=\neg\Box$ and a $\boxtimes$-fixed point $\phi$,
$$ \phi\ \text{orbit-attached}\ (\phi=\boxtimes\bot)\iff\exists\ \text{integral-unit}
   \ (1=\top)\ \text{full residuated tensor}, $$
$$ \phi\ \text{detached}\iff\text{every full residuated tensor has}\ 1\ne\top. $$
Arithmetically, attachment is the de Jongh–Sambin Löb-coincidence
$\phi\equiv\mathrm{Con}_T$ (forced by $D3$/GL), and detachment is realized only by
a Rosser predicate $\Box_R$ keeping $D1+\Sigma_1$-completeness but evading Löb
(Guaspari–Solovay 1979; Kurahashi 2021). Thus **"non-integral unit" is the
algebraic shadow of "Rosser predicate evading Löb"**, and the integral/non-integral
gate of the residuated layer (Thm 50d) is the exact image of the Löb/Rosser gate of
the provability predicate. _(Verified: the attached 3-chain Gödel model admits an
integral-unit $\top$ tensor; the detached $R_2/M_3$ admits $0$ integral-unit
tensors and non-integral units $\{o_0,o_1,p\}$.)_ _Remaining obligation:_ promote
the dictionary to a functor $L_{(-)}$ from derivability packages to residuated APS.

Machine verification: `code/scripts/check-pass51.py` $\to$
`artifacts/reports/pass51-euler-completeness-phantom-cohomology-rosser-unit-check.json`
($\{A,B,C,\text{PASS}\}=$ all true).

**References.** D. Guaspari, R. Solovay, "Rosser sentences," *Annals of
Mathematical Logic* 16 (1979), 81–99. T. Kurahashi, "Rosser-type provability
predicates and the second incompleteness theorem" (2021). C. Smoryński,
*Self-Reference and Modal Logic*, Springer (1985) [de Jongh–Sambin fixed-point
theorem]. C. A. Weibel, *An Introduction to Homological Algebra*, CUP (1994), §3.5
[$\varprojlim^1$ and Mittag-Leffler].

## Pass 52 — The flipped invariant $\Phi(\tau)$: signed flipped-chain formula, extremal dichotomy, and the Smith/Lefschetz Euler gap

Thm 51a deflated the Bredon refinement $e(F^{\tau})$ to the bare vertex count
$|F^{\tau}|$, leaving the *flipped* term $\Phi(\tau)=1-|F^{\tau}|$ as the genuine
homological content. Pass 52 gives $\Phi$ an intrinsic combinatorial formula,
classifies its extremes, and reads it as a difference of two fixed-point Euler
characteristics. Throughout $F$ is a finite poset with minimum $\hat0$ (so
$\Delta(F)$ is a cone, $\mathbb F_2$-acyclic) and $\tau=\boxtimes|_F$ is an
order-reversing involution.

**The flipped-chain sign.** A $\tau$-invariant chain $\sigma=\{x_0<\cdots<x_d\}$
is set-wise reversed by $\tau$; the only order-reversing bijection of a finite
chain is the reversal $x_i\mapsto x_{d-i}$, whose sign is $(-1)^{d(d+1)/2}$.
Combined with the simplicial degree sign $(-1)^d$, the Hopf-trace contribution of
each invariant $d$-chain is
$$ s(d)=(-1)^{d}(-1)^{d(d+1)/2}=
   \begin{cases}+1 & d\equiv0,1\ (\mathrm{mod}\ 4),\\ -1 & d\equiv2,3\ (\mathrm{mod}\ 4),\end{cases} $$
the period-4 pattern $+\,+\,-\,-$ (note $s(0)=s(1)=+1$, so fixed vertices and
flipped edges both add positively, flipped triangles and tetrahedra subtract).

**Thm 52a (flipped-chain formula for $\Phi$).** Let $N_d$ be the number of
$\tau$-invariant $d$-chains. Since $\Delta(F)$ is $\mathbb F_2$-acyclic,
$L(\tau)=1$, and the Hopf trace formula gives
$$ \Phi(\tau)=\sum_{d\ge1}s(d)\,N_d=1-|F^{\tau}|, \qquad
   \sum_{d\ge0}s(d)\,N_d=L(\tau)=1\ \ (N_0=|F^{\tau}|). $$
The only $0$-dimensional fixed cells are the $|F^{\tau}|$ self-dual points; $\Phi$
packages the signed count of all genuinely flipped higher chains.

**Thm 52b (extremal dichotomy of $\Phi$).** Over all $(F,\tau)$,
$$ \sup_{(F,\tau)}\Phi(\tau)=+1,\qquad \inf_{(F,\tau)}\Phi(\tau)=-\infty. $$
The supremum is attained *exactly* on fixed-point-free $\tau$ ($F^{\tau}=
\varnothing$): the Boolean cube $2^{[n]}$ under complementation and the $C_4$
diamond, where the lone flipped edge $\{\hat0,\hat1\}$ carries all of $L=1$ —
this is precisely the Pass-50 "cube-gap." The infimum is approached by the
**fixed-antichain fan** $F_m=(\hat0<a_1,\dots,a_m<\hat1)$, $\tau$ swapping
$\hat0\leftrightarrow\hat1$ and fixing each $a_i$: here $|F^{\tau}|=m$ and
$\Phi=1-m$, the $m$ flipped triangles $\{\hat0<a_i<\hat1\}$ ($s(2)=-1$ each)
cancelling the $m$ fixed vertices down to the residual flipped edge. So $\Phi$ is
bounded *above* by acyclicity but unbounded *below* by the size of the self-dual
antichain; the bracket count $|F^{\tau}|=1-\Phi$ is the genuine degree of freedom.
The fan is the pathological extremal companion to the cube: the cube has a single
flipped edge and *no* fixed point ($\Phi=+1$), the fan has a single flipped edge
and an *arbitrarily large* fixed antichain ($\Phi=1-m$), and both sit on the same
$L=1$ acyclicity constraint.

**Thm 52c ($\Phi$ as the Smith/Lefschetz Euler gap).** For an involution,
$L(\tau)=\chi(\mathrm{Fix}\,\tau)$; Smith theory on the $\mathbb F_2$-acyclic
$\Delta(F)$ forces the geometric fixed set $|\Delta(F)|^{\tau}$ to be
$\mathbb F_2$-acyclic, so $\chi(|\Delta(F)|^{\tau})=1$. With the combinatorial
vertex count $\chi(\Delta(F^{\tau}))=|F^{\tau}|$ (Thm 51a),
$$ \Phi(\tau)=\chi\big(|\Delta(F)|^{\tau}\big)-\chi\big(\Delta(F^{\tau})\big), $$
the exact gap between the *geometric* (topological, Smith-acyclic) and the
*combinatorial* (vertex-spanned) fixed-point Euler characteristics. $\Phi\ne0$
precisely when the geometric fixed set contains barycenters of flipped invariant
chains invisible to the vertex subcomplex — the cube-gap barycenter
$\tfrac12(\hat0+\hat1)$ being the minimal instance. _Remaining obligation:_ a
cell-level chain map identifying the flipped-triangle barycenters with the
$\mathrm{sd}(\Delta)$ fixed subcomplex (verified numerically: every test row has
$\chi(|\Delta(F)|^{\tau})=L=1$).

Machine verification: `code/scripts/check-pass52.py` $\to$
`artifacts/reports/pass52-flipped-invariant-check.json` (`{"PASS": true}`). Cubes
$2^{[1..3]}$ and $C_4$: $(e,\Phi,L)=(0,1,1)$. Fan $m=1..5$:
$\Phi=(0,-1,-2,-3,-4)=1-m$. $3$-chain $(1,0,1)$; $4$-chain $(0,1,1)$. Every row
$L=e+\Phi=1$, $\Phi=1-|F^{\tau}|$, fixed set an antichain.

**References.** P. A. Smith, "Fixed-point theorems for periodic transformations,"
*Amer. J. Math.* 63 (1941), 1–8. G. E. Bredon, *Introduction to Compact
Transformation Groups*, Academic Press (1972) [equivariant Euler characteristic].
A. Björner, "Topological methods," in *Handbook of Combinatorics* (1995), §10
[order complexes, Lefschetz fixed points on posets].

## Pass 51–53 — The Integral Phantom and the Löb/Rosser Functor

Passes 51 and 52 lost their discussion-log bodies to crashed writes; their repo
edits (open_problems.md, definitions.md) landed. This section consolidates 51–53.

### Pass 51 (recap)

- **Lemma 51a / Thm 51a (deflation of $e$).** For any antitone $\boxtimes$ on a
  poset, $\mathrm{Fix}(\boxtimes)$ is an antichain: if $p\le q$ with $\boxtimes
  p=p$, $\boxtimes q=q$, then antitonicity gives $q=\boxtimes q\le\boxtimes p=p$,
  so $p=q$. Hence the order complex $\Delta(F^\tau)$ is discrete and
  $e(F^\tau)=\chi(\Delta(F^\tau))=|F^\tau|$ identically — $e$ is a *complete but
  deflationary* bracket invariant, and the order-complex-circle pathology cannot
  occur as a fixed-vertex set.
- **Thm 51b.** $b_{\mathrm{phantom}}(P_r)=\dim_{\mathbb F}H^1(\mathrm{Ob}^\bullet
  (P_r))=\varprojlim^1$ of the image tower, additive over independent arms ($=r$).
- **Thm 51c.** Integral unit $\iff$ orbit-attached $\iff$ Löb; non-integral unit
  $\iff$ detached $\iff$ Rosser-evades-Löb.

### Pass 52 (recap)

$\Phi(\tau)=1-|F^\tau|$ characterized: **Thm 52a** $\Phi=\sum_{d\ge1}s(d)N_d$ with
$N_d=\#\{\tau\text{-invariant }d\text{-chains}\}$ and period-4 sign
$s(d)=(-1)^d(-1)^{d(d+1)/2}=(+,+,-,-)$; **Thm 52b** $\sup\Phi=+1$ (fixed-point-free
$\tau$, e.g. the cube), $\inf\Phi=-\infty$ via the fixed-antichain fan
$F_m$ ($\Phi=1-m$); **Thm 52c** $\Phi(\tau)=\chi(|\Delta(F)|^\tau)-\chi(\Delta(F^\tau))$,
the geometric-minus-combinatorial fixed-point Euler gap.

### Pass 53 — the integral phantom

The phantom Betti number $b_{\mathrm{phantom}}=r$ of Passes 50/51 was computed in a
finite-dimensional / field setting where $\varprojlim^1$ is *forced* to vanish:
the image filtration of a finite-dimensional tower stabilizes (Mittag-Leffler).
So $r$ is only the rank of the finitary cochain $C^1=\mathbb F^{\{\text{failed
covers}\}}$, not a derived-limit obstruction. To make the phantom genuine one
needs integer coefficients and a non-Mittag-Leffler tower.

> **Theorem 53a (integral phantom / the $2$-adic $\varprojlim^1$).** Let
> $\mathcal A=(\mathbb Z,\times2)$ be the image coefficient tower of the
> $\omega$-telescope of failed join-covers in which each cover doubles its fiber
> (the $\times2$ supplied by a residuated $\mathbb Z$-grading, *not* by the $\pm1$
> incidence numbers of a poset). Then:
> 1. (field collapse) for every field $k$ the image filtration $F_j(A_0)=
>    \mathrm{im}(A_j\to A_0)$ stabilizes, so $\mathcal A\otimes k$ is
>    Mittag-Leffler and $\varprojlim^1(\mathcal A\otimes k)=0$;
> 2. (integral non-vanishing) over $\mathbb Z$, $F_j(\mathbb Z)=2^j\mathbb Z$ with
>    $[\mathbb Z:2^j\mathbb Z]=2^j\uparrow\infty$ (non-ML); the SES of towers
>    $0\to(\mathbb Z,\times2)\to(\mathbb Z,\mathrm{id})\to(\mathbb Z/2^n,
>    \mathrm{surj})\to0$ yields $0\to0\to\mathbb Z\to\widehat{\mathbb Z}_2\to
>    \varprojlim^1(\mathbb Z,\times2)\to0$, so
>    $$\varprojlim{}^1(\mathbb Z,\times2)=\widehat{\mathbb Z}_2/\mathbb Z,$$
>    uncountable and divisible.

The genuine integral obstruction is therefore the uncountable group
$\widehat{\mathbb Z}_2/\mathbb Z$ — invisible to every field *and* to every
finitely supported probe (each $b\in\bigoplus\mathbb Z$ is in the image of
$1-\mathrm{shift}$; e.g. $b=(1,1,\dots)\mapsto a=(-1,-1,\dots)$). One ghost for
every $2$-adic integer that is not an ordinary integer (a Smullyan-grade phantom:
detectable only by an uncountable coherent witness, never by finite data).

### Pass 53 — the Löb/Rosser functor

> **Theorem 53b (functoriality of the Löb/Rosser dictionary).** Let
> $\mathbf{Deriv}$ have objects $(\Box,\Pi)$ (provability predicate $+$ a subset
> $\Pi$ of derivability conditions) and morphisms relative-interpretation
> translations preserving $\vdash$ and $\Pi$, and $\mathbf{resAPS}$ the residuated
> APS with $\boxtimes$- and unit-preserving homomorphisms. Then
> $L_{(-)}:\mathbf{Deriv}\to\mathbf{resAPS}$, $(\Box,\Pi)\mapsto$ Lindenbaum
> residuated APS ($\otimes=\wedge$, $\backslash=\to$, $\boxtimes=\neg\Box$, unit
> $=$ chosen $\boxtimes$-fixed point), is a functor; on the Löb subcategory
> $\mathbf{GL}$ (by Solovay 1976, those with provability logic $\supseteq\mathsf{GL}$)
> it is canonical (de Jongh–Sambin fixed-point uniqueness) and
> $$e(L_{(\Box,\Pi)})=\top \iff (\Box,\Pi)\vdash\text{Löb}\iff(\Box,\Pi)\in\mathbf{GL},$$
> with essential image exactly the integral-unit subcategory
> $\mathbf{resAPS}_{\mathrm{int}}$. Rosser packages (Guaspari–Solovay 1979;
> Kurahashi 2021) map to the non-integral complement, where $L_{(-)}$ is
> well-defined only up to a choice of Rosser unit (Rosser fixed points are not
> unique up to provable equivalence) — a *torsor of units*.

**Punchline.** Löb $=$ fixed-point uniqueness $=$ unit integrality $=$ canonical
functoriality are four faces of one phenomenon: the same uniqueness that attaches
the Gödel fixed point to $\mathrm{Con}=\boxtimes\bot$ is what makes the unit equal
the top and the functor single-valued.

## Pass 54–57 — The dilation solenoid and the carrier-free Rosser-unit no-go

*(Passes 54–56 are recapped compactly here from `open_problems.md`, the research log,
and the verified reports `pass54/55/56-*.json`; the discussion-log bodies hold the
full debates. Pass 57 is given in full. This section restores the note's continuity
after a mount-lag run skipped the 54–56 inserts; cf. [[aps-run-sync-hazard]].)*

### Pass 54–56 (recap)

- **Constr 54a / Thm 54b / Cor 54c (honest $m$-adic dilation solenoid).** The
  negative cone $\mathbb Z^-$ ($x\otimes y=x+y$, $x\backslash y=\min(0,y-x)$,
  $e=0=\top$) with the $m$-fold dilation $d_m(x)=mx$ — an injective, non-surjective
  residuated-lattice endomorphism (image $m\mathbb Z^-$, cover-fiber multiplicity
  $m$) — gives the tower $(\mathbb Z^-\xleftarrow{d_m}\mathbb Z^-\xleftarrow{d_m}
  \cdots)$ with top-cover module $(\mathbb Z,\times m)$. Then $\varprojlim=0$ and
  $\varprojlim^1(\mathbb Z,\times m)=\widehat{\mathbb Z}_m/\mathbb Z$
  ($\widehat{\mathbb Z}_m=\prod_{p\mid m}\mathbb Z_p$, uncountable, divisible);
  field-collapse over every $k$; **radical invariance** ($\varprojlim^1$ depends only
  on $\mathrm{rad}(m)$: $\times2\!\sim\!\times4\!\sim\!\times8$ as pro-objects though
  non-isomorphic as towers — inequivalent dilations, one phantom). The prime $2$ is
  *not* forced; $m=1$ is the phantom-free boundary.
- **Constr 55a / Thm 55b/c/d (dilation-solenoid refutability $\boxtimes_m$).** The
  honest non-trivial limit object is the directed colimit $C_m=\varinjlim(\mathbb Z^-,
  d_m)=\mathbb Z[1/m]^-$ (the inverse limit is the one-point lattice), whose MacNeille
  completion is *literally* the classical $m$-adic solenoid ($\widehat{C_m}=\mathbb S_m
  =(\mathbb R\times\widehat{\mathbb Z}_m)/\mathbb Z$). Lifting Construction 49b with
  $m$-adic rungs $a_n=-1/m^n\uparrow a^\ast=0^-$ and a doubled cover, $\boxtimes_m$'s
  join-continuity fails at the lone cover $a^\ast$ with failure module $(\mathbb Z,
  \times m)$, so the phantom is $\boxtimes_m$'s *own* $\varprojlim^1$ (Thm 55b). **ML
  $=$ nFG2 dichotomy (Thm 55c):** Mittag–Leffler $\iff$ orbit stabilizes $\iff$
  all-level nFG2 (index-$2$, Thm 41a) $\iff\varprojlim^1=0$; all four fail for $m\ge2$
  ($\neg$FG2, perpetual non-stabilizing orbit) while every finite truncation satisfies
  them (the phantom is strictly **liman**); G2 holds vacuously — the solenoid sits in
  $G2\wedge\neg$FG2. **Fusion (Thm 55d):** *finitely Löb, limanly Rosser* — the
  fixed-point/unit tower is the same $(\mathbb Z,\times m)$, so a residuated tensor
  forces a non-integral Rosser unit and the phantom $=$ the Löb$\to$Rosser gluing
  obstruction.
- **Thm 56a/b (residuation/Rosser dichotomy $+$ Čech complex).** The completed arena
  $\overline{L}^{(m)}$ is a complete distributive lattice and a frame, hence residuates
  under $\otimes=\wedge$ with the **integral** unit $\top$ (Löb, Thm 56a.1); but the
  **dilation monoid** $\otimes=+$ (unit $e=a^\ast$, Rosser) does *not* residuate —
  $x\mapsto x\otimes c$ fails join-preservation at the cover, $\bigvee_n(a_n\otimes c)
  =a^\ast<c=a^\ast\otimes c$, so $c\backslash a^\ast=\{a_n\}_n$ is non-principal
  (Thm 56a.2); finite truncations residuate under *both* (Thm 56a.3). So **residuation
  $\veebar$ Rosser unit in the completion.** The dilation cover's two-set telescope has
  interval nerve, so its Čech complex is the two-term $\delta=\mathrm{id}-m\cdot
  \mathrm{sh}$ on $\prod_n\mathbb Z$, with $\check H^0=\varprojlim=0$ (detached),
  $\check H^1=\varprojlim^1=\widehat{\mathbb Z}_m/\mathbb Z$ (Thm 56b).

### Pass 57 — Carrier-free cancellativity no-go, phantom $=$ Rosser-torsor, quantale escape

Pass 56 left a dichotomy proved for *one* tensor. Pass 57 makes it absolute and
carrier-free, then audits the only escape.

> **Lemma 57a (carrier-free cancellativity no-go).** Let $(L,\le,\otimes,\backslash,
> e)$ be a complete residuated lattice (so $\otimes$ preserves all joins in each
> argument). If the unit $e=\bigvee_{n}a_n$ is the *non-attained* sup of a strictly
> ascending chain ($a_n<e$ for all $n$) and there is a **completely join-irreducible**
> $c>e$ with $a_n\otimes c<c$ for all $n$ (cancellativity), then a contradiction
> follows. *Proof.* $c=e\otimes c=(\bigvee_n a_n)\otimes c=\bigvee_n(a_n\otimes c)$;
> each summand is $<c$, so complete join-irreducibility forces some $a_n\otimes c=c$,
> contradicting cancellativity. $\square$
>
> **Equivalently:** in a complete residuated lattice the unit may be a non-attained
> sup-of-chain only if **no completely join-irreducible element covers it** — a
> *Rosser unit $\perp$ join-irreducible cover* law.

> **Corollary 57a$'$ (Thm 56a.2 made absolute).** On $\overline{L}^{(m)}$ the doubled
> cover supplies a completely join-irreducible $c\succ a^\ast=\bigvee_n a_n$ with
> $a_n\otimes c<c$; hence **no** complete residuated tensor has unit $e=a^\ast$. The
> Pass-56 dichotomy is not "the additive $\otimes$ fails" but "*every* $\otimes$
> fails": residuation forces the integral $\top$/Löb unit. The non-integral Rosser
> unit is *completion-incompatible*.

> **Theorem 57b (phantom $=$ Rosser unit-torsor, as torsors).** The Čech cochain map
> $\Theta:\mathrm{Ros}_m\to\operatorname{coker}\delta$ (Rosser section $\mapsto$ its
> $1$-cochain class) is $G_m$-equivariant for the verified group iso $G_m\cong
> \operatorname{coker}\delta=\widehat{\mathbb Z}_m/\mathbb Z$ and bijective, hence an
> **isomorphism of torsors** $\mathrm{Ros}_m\cong\widehat{\mathbb Z}_m/\mathbb Z$.
> (Naturality across $\mathbf{Deriv}$ remains a proof obligation.)

> **Theorem 57c (quantale escape / Phantom $\veebar$ Quantale).** The ideal/downset
> completion $\mathcal D(C_m)$ with Day convolution $S\otimes T={\downarrow}\{x{+}y\}$
> is a unital residuated quantale with additive unit ${\downarrow}0$; there the
> would-be cover join $I=\bigvee_n{\downarrow}a_n\subsetneq{\downarrow}a^\ast$ is
> principal (the chain's sup *splits off*), voiding Lemma-57a's hypothesis and killing
> the phantom ($\varprojlim^1=0$, ML). Across completions of the dilation cone,
> $$\text{MacNeille}=\{\text{phantom},\ \neg\text{additive-residual}\}\quad\veebar\quad
>   \text{Ideal}=\{\text{additive-residual},\ \neg\text{phantom}\}.$$
> Residuating the Rosser unit costs exactly the phantom. *You may keep the ghost or
> the algebra, never both.*

**Reading.** Lemma 57a is the order-theoretic shadow of "finitely Löb, limanly
Rosser": a sup-of-chain unit is the algebraic signature of a *limit* (Rosser,
detached) fixed point, and a complete residuated lattice simply refuses to host one
beneath a join-irreducible cover. The quantale escape is honest but Pyrrhic — it
buys the residual by making the unit principal, i.e. by erasing the very
non-attainment that *was* the phantom. Verified: `code/scripts/check-pass57.py`
$\to$ `artifacts/reports/pass57-cancellativity-nogo-quantale-escape-check.json`
(L/Q/R/D/M/X all PASS).

**Machine verification** (`code/scripts/check-pass53.py` →
`artifacts/reports/pass53-integral-lim1-loeb-rosser-functor-check.json`, PASS):
*A* — $\mathbb Z$-image indices $2,4,8,\dots,256$ (strictly grow $\Rightarrow$
non-ML $\Rightarrow\varprojlim^1\ne0$); $\mathbb F_2$ image dim $\equiv0$,
$\mathbb F_3$ image dim $\equiv1$ (stable $\Rightarrow$ ML $\Rightarrow
\varprojlim^1=0$); $\mathbb Z/2^n$ tower surjective ($\varprojlim=\widehat{\mathbb
Z}_2$, $\varprojlim^1=0$). *B* — $3$-chain integral-unit tensors $=2$; $M_3$
integral-unit $=0$, non-integral units $o_0,o_1,p$ each $=13$ (multiplicity $3$ =
Rosser non-canonicity); Löb unit canonical at $\top$.

**Open (Pass 54 targets).** (1) Realize $(\mathbb Z,\times2)$ as the failed-cover
incidence module of an *actual* complete residuated lattice (unit doubling the
cover fiber), and decide whether $m$-adic phantoms $\widehat{\mathbb Z}_m/\mathbb Z$
realize for all $m\ge2$. (2) Promote Thm 53b to a full equivalence
$L_{(-)}|_{\mathbf{GL}}\simeq\mathbf{resAPS}_{\mathrm{int}}$ and identify the
Rosser unit-torsor with $H^1(\mathbf{Deriv}\setminus\mathbf{GL};\mathrm{Aut(unit)})$ —
unifying "phantom" and "Rosser torsor" as one derived-functor obstruction.

**References.** R. M. Solovay, *Provability interpretations of modal logic*,
Israel J. Math. 25 (1976); D. Guaspari & R. M. Solovay, *Rosser sentences*,
Ann. Math. Logic 16 (1979); D. de Jongh & G. Sambin (fixed-point theorem for
$\mathsf{GL}$), see G. Boolos, *The Logic of Provability* (CUP 1993), Ch. 8;
T. Kurahashi, *Rosser-type provability predicates and the $\diamond$-fixed-point
question* (2021); N. Galatos, P. Jipsen, T. Kowalski, H. Ono, *Residuated
Lattices: An Algebraic Glimpse at Substructural Logics* (Elsevier 2007), Ch. 3
(integral residuated lattices, $e=\top$); G. E. Bredon, *Introduction to Compact
Transformation Groups* (Academic Press 1972), Ch. III (Smith theory); J. Milnor,
*On axiomatic homology theory*, Pacific J. Math. 12 (1962) ($\varprojlim^1$).

## Pass 53 — The integral $2$-adic phantom and the Löb/Rosser functor

Pass 52 left two residues carried from Pass 51: (ii) the integral $\varprojlim^1$
nonvanishing, and (iii) functoriality of the Löb/Rosser dictionary. Pass 53 closes
both.

### The integral phantom

The phantom Betti number $b_{\mathrm{phantom}}=r$ of Passes 50/51 was computed in a
finite-dimensional / field setting where $\varprojlim^1$ is *forced* to vanish
(finite-dimensional towers are Mittag-Leffler), so $r$ is only the rank of the
finitary cochain $C^1=\mathbb F^{\{\text{failed covers}\}}$. A genuine derived
obstruction needs integer coefficients and a non-Mittag-Leffler tower.

> **Theorem 53a (integral phantom / the $2$-adic $\varprojlim^1$).** Let
> $\mathcal A=(\mathbb Z,\times2)$ be the image coefficient tower of the
> $\omega$-telescope of failed join-covers in which each cover doubles its fiber
> (the $\times2$ supplied by a residuated $\mathbb Z$-grading, *not* by the $\pm1$
> incidence numbers of a poset, which can never produce $\times2$). Then:
> 1. (field collapse) for every field $k$, the image filtration
>    $F_j(A_0)=\mathrm{im}(A_j\to A_0)$ stabilizes, so $\mathcal A\otimes k$ is
>    Mittag-Leffler and $\varprojlim^1(\mathcal A\otimes k)=0$;
> 2. (integral non-vanishing) over $\mathbb Z$, $F_j(\mathbb Z)=2^j\mathbb Z$,
>    $[\mathbb Z:2^j\mathbb Z]=2^j\uparrow\infty$ (non-ML), and the SES of towers
>    $0\to(\mathbb Z,\times2)\to(\mathbb Z,\mathrm{id})\to(\mathbb Z/2^n,
>    \mathrm{surj})\to0$ gives $0\to0\to\mathbb Z\to\widehat{\mathbb Z}_2\to
>    \varprojlim^1(\mathbb Z,\times2)\to0$, so
>    $$\varprojlim{}^1(\mathbb Z,\times2)=\widehat{\mathbb Z}_2/\mathbb Z,$$
>    uncountable and divisible.

So the genuine integral obstruction is the uncountable group $\widehat{\mathbb
Z}_2/\mathbb Z$ — invisible to every field *and* to every finitely supported probe
(each $b\in\bigoplus\mathbb Z$ lifts under $1-\mathrm{shift}$; e.g. $(1,1,\dots)
\mapsto(-1,-1,\dots)$). One ghost per $2$-adic integer that is not an ordinary
integer: a Smullyan-grade phantom, detectable only by an uncountable coherent
witness, never by finite data.

### The Löb/Rosser functor

> **Theorem 53b (functoriality of the Löb/Rosser dictionary).** Let
> $\mathbf{Deriv}$ have objects $(\Box,\Pi)$ and morphisms relative-interpretation
> translations preserving $\vdash,\Pi$; $\mathbf{resAPS}$ the residuated APS with
> $\boxtimes$- and unit-preserving homomorphisms. Then
> $L_{(-)}:\mathbf{Deriv}\to\mathbf{resAPS}$, $(\Box,\Pi)\mapsto$ Lindenbaum
> residuated APS ($\otimes=\wedge$, $\backslash=\to$, $\boxtimes=\neg\Box$, unit
> $=$ chosen $\boxtimes$-fixed point), is a functor; on the Löb subcategory
> $\mathbf{GL}$ (by Solovay 1976, provability logic $\supseteq\mathsf{GL}$) it is
> canonical (de Jongh–Sambin uniqueness) and
> $$e(L_{(\Box,\Pi)})=\top\iff(\Box,\Pi)\vdash\text{Löb}\iff(\Box,\Pi)\in
> \mathbf{GL},$$
> with essential image exactly $\mathbf{resAPS}_{\mathrm{int}}$. Rosser packages
> (Guaspari–Solovay 1979; Kurahashi 2021) land in the non-integral complement,
> where $L_{(-)}$ is well-defined only up to a choice of Rosser unit (Rosser fixed
> points are not unique) — a *torsor of units*.

**Punchline.** Löb $=$ fixed-point uniqueness $=$ unit integrality $=$ canonical
functoriality are four faces of one phenomenon: the uniqueness that attaches the
Gödel fixed point to $\mathrm{Con}=\boxtimes\bot$ is what makes the unit equal the
top and the functor single-valued.

**Machine verification** (`code/scripts/check-pass53.py` →
`artifacts/reports/pass53-integral-lim1-loeb-rosser-functor-check.json`, PASS):
*A* — $\mathbb Z$-image indices $2,4,\dots,256$ (non-ML $\Rightarrow\varprojlim^1
\ne0$); $\mathbb F_2$ image dim $\equiv0$, $\mathbb F_3$ image dim $\equiv1$
(stable $\Rightarrow$ ML $\Rightarrow\varprojlim^1=0$); $\mathbb Z/2^n$ tower
surjective ($\varprojlim=\widehat{\mathbb Z}_2$). *B* — $3$-chain integral-unit
tensors $=2$; $M_3$ integral-unit $=0$, non-integral units $o_0,o_1,p$ each $=13$
(multiplicity $3$ = Rosser non-canonicity); Löb unit canonical at $\top$.

**Open (Pass 54).** (1) Realize $(\mathbb Z,\times2)$ as the failed-cover incidence
module of an *actual* complete residuated lattice (unit doubling the cover fiber),
and decide whether $m$-adic phantoms $\widehat{\mathbb Z}_m/\mathbb Z$ realize for
all $m\ge2$. (2) Promote Thm 53b to a full equivalence $L_{(-)}|_{\mathbf{GL}}
\simeq\mathbf{resAPS}_{\mathrm{int}}$ and identify the Rosser unit-torsor with
$H^1(\mathbf{Deriv}\setminus\mathbf{GL};\mathrm{Aut(unit)})$ — unifying "phantom"
and "Rosser torsor" as one derived-functor obstruction.

**References.** R. M. Solovay, *Provability interpretations of modal logic*,
Israel J. Math. 25 (1976); D. Guaspari & R. M. Solovay, *Rosser sentences*, Ann.
Math. Logic 16 (1979); G. Boolos, *The Logic of Provability* (CUP 1993), Ch. 8
(de Jongh–Sambin uniqueness); T. Kurahashi (2021), Rosser-type predicates;
N. Galatos, P. Jipsen, T. Kowalski, H. Ono, *Residuated Lattices* (Elsevier 2007),
Ch. 3 (integral residuated lattices); J. Milnor, *On axiomatic homology theory*,
Pacific J. Math. 12 (1962) ($\varprojlim^1$); G. E. Bredon, *Compact
Transformation Groups* (1972), Ch. III (Smith theory).

## Pass 54 — The honest $m$-adic dilation solenoid

Pass 53's Theorem 53a located the genuine integral obstruction as
$\varprojlim^1(\mathbb Z,\times2)=\widehat{\mathbb Z}_2/\mathbb Z$, but the tower
$(\mathbb Z,\times2)$ was *posited* as an abstract coefficient module, with the
warning that the $\times2$ "must come from a residuated $\mathbb Z$-grading, not from
the $\pm1$ incidence numbers of a poset." Pass 54 supplies the honest residuated
lattice and proves the obstruction is realized by a genuine residuated endomorphism,
uniformly in $m$.

### The carrier and the dilation

> **Construction 54a (the $m$-adic dilation solenoid).** Let $\mathbb Z^-=
> \{0,-1,-2,\dots\}$ be the **negative cone** of the ordered abelian group $\mathbb
> Z$, an integral residuated lattice with $x\otimes y=x+y$, residual $x\backslash
> y=\min(0,y-x)$, lattice order the chain, unit $e=0=\top$ (its Dedekind–MacNeille
> completion $\overline{\mathbb Z^-}=\mathbb Z^-\cup\{-\infty\}$ is the complete
> object). For $m\ge2$ the **$m$-fold dilation** $d_m:\mathbb Z^-\to\mathbb Z^-$,
> $d_m(x)=mx$, is an injective, non-surjective residuated-lattice endomorphism:
> $$d_m(x\otimes y)=d_m x\otimes d_m y,\quad d_m(x\backslash y)=d_m x\backslash d_m y,
> \quad d_m(0)=0,\quad \mathrm{im}\,d_m=m\mathbb Z^-,$$
> with each image cover step $0\succ -m$ spanning exactly $m$ atomic steps of
> $\mathbb Z^-$ (cover-fiber multiplicity $m$ — the residuated $\times m$ a poset's
> $\pm1$ incidence cannot supply). The inverse system $\mathbf A^{(m)}=(\mathbb Z^-
> \xleftarrow{d_m}\mathbb Z^-\xleftarrow{d_m}\cdots)$ has top-cover coefficient tower
> $(\mathbb Z,\times m)$, and the inverse limit $L_\infty^{(m)}=\varprojlim_n
> (\mathbb Z^-,d_m)$ is the **$m$-adic dilation solenoid**.

The residual identity is the crucial check: $d_m(x\backslash y)=m\min(0,y-x)=
\min(0,my-mx)=d_m x\backslash d_m y$ holds because $m>0$ pulls *through* the meet —
this is exactly where the residuated structure (not just the order) is used.

### The phantom, all $m$

> **Theorem 54b (honest integral phantom).** For every $m\ge2$:
> 1. $\varprojlim\mathbf A^{(m)}=0$ and $\varprojlim^1(\mathbb Z,\times m)=
>    \widehat{\mathbb Z}_m/\mathbb Z$ with $\widehat{\mathbb Z}_m=\prod_{p\mid m}
>    \mathbb Z_p$ (uncountable, divisible);
> 2. (field collapse) for every field $k$, $(\mathbb Z,\times m)\otimes k$ is
>    Mittag-Leffler (image constant: $0$ if $\mathrm{char}\,k\mid m$, else $k$), so
>    $\varprojlim^1=0$ — the phantom is purely integral;
> 3. (radical invariance) $\varprojlim^1(\mathbb Z,\times m)\cong\varprojlim^1
>    (\mathbb Z,\times m')$ iff $\mathrm{rad}(m)=\mathrm{rad}(m')$. The prime $2$ is
>    **not** forced; $m=1$ is the phantom-free boundary (identity tower, ML).

*Proof.* (1) Coherence $x_0=m^n x_n$ forces $x_0=0$ ($m^n\nmid x_0$ for large $n$),
so $\varprojlim=0$. Milnor's six-term sequence applied to the SES of towers
$0\to(\mathbb Z,\times m)\to(\mathbb Z,\mathrm{id})\to(\mathbb Z/m^n)\to0$ reads
$0\to0\to\mathbb Z\to\widehat{\mathbb Z}_m\to\varprojlim^1(\mathbb Z,\times m)\to0$
(using $\varprojlim^1(\mathbb Z,\mathrm{id})=0$ and $\varprojlim(\mathbb Z/m^n)=
\widehat{\mathbb Z}_m$), so $\varprojlim^1=\widehat{\mathbb Z}_m/\mathbb Z$.
Divisibility: $\times q$ for $q\nmid m$ is a unit on each $\mathbb Z_p$ ($p\mid m$),
hence invertible on $\widehat{\mathbb Z}_m$; for $q\mid m$, $q\widehat{\mathbb Z}_m
+\mathbb Z=\widehat{\mathbb Z}_m$. (2) Over $k$, $\times m$ is zero or iso; either
way the image filtration is constant, ML. (3) $\{m^n\mathbb Z\}$ and $\{m'^n\mathbb
Z\}$ are mutually cofinal iff $\mathrm{rad}(m)=\mathrm{rad}(m')$; cofinal towers
share $\varprojlim$ and $\varprojlim^1$. $\square$

The radical phenomenon is the Pass-54 pathology: $\times2,\times4,\times8$ are
pairwise **non-isomorphic as towers** (no level iso intertwines them) yet
**pro-isomorphic** ($\{2^{2n}\mathbb Z\}$ cofinal in $\{2^n\mathbb Z\}$), so they
carry one and the same phantom $\widehat{\mathbb Z}_2/\mathbb Z$. Inequivalent
dilations, a single ghost.

> **Corollary 54c (the refutability orbit's arithmetic).** The "$m$-adic arithmetic
> the refutability orbit must carry" (Pass 53's question) is the profinite completion
> $\widehat{\mathbb Z}_m=\prod_{p\mid m}\mathbb Z_p$ acting by dilation on the single
> solenoidal cover fiber; the phantom $\widehat{\mathbb Z}_m/\mathbb Z=
> \mathrm{coker}(\mathbb Z\hookrightarrow\widehat{\mathbb Z}_m)$ is one ghost per
> coherent $m$-adic witness without an integer representative — a Smullyan-grade
> phantom, provable only by an uncountable coherent family, refuted by no finite
> datum.

### Toward the Rosser torsor (obligation (2), partial)

Fullness of $L_{(-)}|_{\mathbf{GL}}$: a residuated homomorphism between
integral-unit Lindenbaum APS is determined on the $\boxtimes$-fixed points, which de
Jongh–Sambin uniqueness makes closed-term-definable, so it lifts to an interpretation
translation preserving $\vdash,\Pi$ — giving (with Thm 53b essential surjectivity) an
equivalence $\mathbf{GL}\simeq\mathbf{resAPS}_{\mathrm{int}}$. The Rosser unit is a
$\mathrm{Aut(unit)}$-torsor whose class lies in $H^1(\mathbf{Deriv}\setminus
\mathbf{GL};\mathrm{Aut(unit)})$, the $\check{C}$ech $H^1=\varprojlim^1$ of the
witness-comparison choice tower — the *same* derived functor as the phantom. **Open:**
pin $\mathbf{Deriv}$-morphisms to residuated maps; write the choice sheaf explicitly.

**Machine verification** (`code/scripts/check-pass54.py` →
`artifacts/reports/pass54-honest-residuated-2adic-phantom-check.json`, PASS):
*A* — for $m\in\{1,2,3,4,6,8,12\}$ the $\mathbb Z$-index tower $m,\dots,m^8$ grows
(non-ML) for $m\ge2$, is constant for $m=1$; every $\mathbb F_p$ ($p\le7$) constant
(ML). *R* — $\mathrm{rad}(2)=\mathrm{rad}(4)=\mathrm{rad}(8)=\{2\}$,
$\mathrm{rad}(6)=\mathrm{rad}(12)=\{2,3\}$, $\mathrm{rad}(2)\ne\mathrm{rad}(6)$;
pro-iso $\times2\sim\times4\sim\times8$, $\times2\not\sim\times6$. *B* — $d_2,d_3$
verified injective non-surjective residuated endomorphisms of $\mathbb Z^-|_{[-12,0]}$
with cover-fiber multiplier $=m$.

**Open (Pass 55).** Write the antitone $\boxtimes$ on $\overline{L_\infty^{(m)}}$ so
the phantom is *its* $\varprojlim^1$ (Construction-49b collapse lifted through
$\varprojlim$), decide its nFG2/G2-compatibility, and the integrality of a tensor
unit on the solenoid — fusing obligations (1) and (2).

**References.** N. Galatos, P. Jipsen, T. Kowalski, H. Ono, *Residuated Lattices*
(Elsevier 2007), Ch. 3 (negative cones of $\ell$-groups as integral residuated
lattices); J. Milnor, *On axiomatic homology theory*, Pacific J. Math. 12 (1962)
($\varprojlim^1$ six-term sequence); D. Guaspari & R. M. Solovay, *Rosser sentences*,
Ann. Math. Logic 16 (1979); G. Boolos, *The Logic of Provability* (CUP 1993), Ch. 8
(de Jongh–Sambin uniqueness); J.-P. Serre, *Local Fields* (Springer 1979), Ch. on
profinite groups ($\widehat{\mathbb Z}=\prod_p\mathbb Z_p$).

## Pass 55 — The dilation-solenoid refutability $\boxtimes_m$: ML $=$ nFG2, and the phantom $=$ Rosser-torsor fusion

Pass 54 built the honest carrier and proved $\varprojlim^1(\mathbb Z,\times m)=
\widehat{\mathbb Z}_m/\mathbb Z$, but the antitone refutability map was still
implicit: the phantom was the derived limit of an *abstract* coefficient tower, not
of a written-down $\boxtimes$. Pass 55 writes $\boxtimes_m$ explicitly, identifies the
phantom as **its own** $\varprojlim^1$, and reads off the logical content (nFG2/G2 and
Löb/Rosser).

### Carrier correction: colimit, not limit

The *inverse* limit $\varprojlim_n(\mathbb Z^-,d_m)$ is the **trivial one-point
lattice**: a coherent $(x_n)$ obeys $x_0=m^nx_n$, and $m^n\nmid x_0$ for large $n$
unless $x_0=0$. The honest non-trivial object is the directed **colimit**
$$C_m:=\varinjlim\big(\mathbb Z^-\xrightarrow{d_m}\mathbb Z^-\xrightarrow{d_m}\cdots
\big)=\mathbb Z[1/m]^-=\{q\in\mathbb Z[1/m]:q\le0\},$$
the negative cone of the $m$-adic localization — an integral residuated lattice
($x\otimes y=x+y$, $x\backslash y=\min(0,y-x)$, $e=0=\top$, dense chain order) whose
MacNeille completion $\overline{C_m}$ adjoins the cuts and $\bot=-\infty$. This is
*literally* the classical $m$-adic solenoid arena: by Pontryagin duality
$\widehat{C_m}=\mathbb S_m=(\mathbb R\times\widehat{\mathbb Z}_m)/\mathbb Z$, and the
phantom $\widehat{\mathbb Z}_m/\mathbb Z$ is the solenoid's transverse $\varprojlim^1$
winding — so "dilation solenoid" was the precise word, not a metaphor.

### The explicit refutability map

> **Construction 55a (dilation-solenoid refutability $\boxtimes_m$).** On
> $\overline{L}^{(m)}=$ the MacNeille completion of $C_m$, take rungs $a_n=-1/m^n$
> ($n\ge0$), limit cut $a^\ast=\bigvee_n a_n=0^-$, and adjoin a doubled cover
> $a^\ast\prec\{c,b^\ast\}$ ($c<b^\ast$), $\{c,b^\ast\}\prec\top$. Define the antitone
> $\boxtimes_m$ by
> $$\boxtimes_m\top=a_0=-1,\qquad \boxtimes_m(a_{2k})\uparrow b^\ast,\qquad
> \boxtimes_m(a^\ast)=c.$$
> Its top-cover incidence module is the free $\mathbb Z$-module $\mathbb Z\,a_n$ with
> connecting map $\times m$ (since $d_m(-1)=-m=m\cdot a_n$); cover fiber $m$.

This is **Construction 49b lifted verbatim**, with one upgrade: 49b's rungs were
unit-spaced ($o_n$, plain chain, cover fiber $1$), giving a rank-$1$ *field* phantom
($C^1=\mathbb F$, Mittag-Leffler, $\varprojlim^1=0$ — the Pass-51 shadow). Replacing
unit spacing by $m$-adic dilation spacing ($a_n=-1/m^n$, cover fiber $m$) upgrades the
coefficient module to the non-ML $(\mathbb Z,\times m)$, hence to the genuine integral
phantom. *That single substitution is the whole content of "lifting 49b through the
solenoid."*

> **Theorem 55b (the phantom is $\boxtimes_m$'s own $\varprojlim^1$).** The
> $\boxtimes_m$-image tower $(I_n)_n=(\mathbb Z\,a_n,\times m)\cong(\mathbb Z,\times m)$
> has $\varprojlim I=0$, $\varprojlim^1 I=\widehat{\mathbb Z}_m/\mathbb Z$. Join-
> continuity of $\boxtimes_m$ fails at exactly $a^\ast$, with failure module
> $(\mathbb Z,\times m)$:
> $$\boxtimes_m\Big(\bigvee_k a_{2k}\Big)=\boxtimes_m(a^\ast)=c\;<\;b^\ast=\bigvee_k
> \boxtimes_m(a_{2k}).$$
> So the integral phantom is the derived limit of the refutability map *itself*.

### The logical content

> **Theorem 55c (Mittag–Leffler $=$ nFG2 stabilization).** For the $\boxtimes_m$-image
> tower TFAE: (a) Mittag–Leffler; (b) the $T$-orbit $\{\boxtimes_m^nT\}$ stabilizes at
> finite index; (c) all-level nFG2 (index-$2$ truncation, Thm 41a); (d)
> $\varprojlim^1=0$. For every $m\ge2$ **all four fail** (image index $m^n\uparrow
> \infty$, even orbit $a_{2k}=-1/m^{2k}$ strictly ascending): $\boxtimes_m$ is a
> perpetual non-stabilizing orbit, $\neg$FG2. **Every finite truncation**
> $\overline{L}^{(m)}_K$ satisfies all four — the phantom is strictly **liman**
> (limit-only), invisible to any finite stage. **G2 holds vacuously**
> ($\boxtimes_m T=a_0\not\le\bot$, consistency irrefutable), so the solenoid sits in
> the $G2\wedge\neg\mathrm{FG2}$ regime (the M-101 drawer).

The slogan: *Mittag-Leffler $=$ FG2 stabilization; the $\times m$ self-cover is exactly
the obstruction to FG2.* The same arithmetic that makes the tower non-ML makes the
orbit non-stabilizing; phantom-nonvanishing and FG2-failure are one fact.

> **Theorem 55d (fusion: phantom $=$ Rosser unit-torsor).** Each finite truncation
> $\overline{L}^{(m)}_K$ is integral-unit ($e=\top$, with an orbit-attached
> $\boxtimes^2$-reachable fixed point — odd bracket interval, Thm 47d — hence Löb). The
> fixed-point / unit tower is the **same** $(\mathbb Z,\times m)$:
> $$\varprojlim=0\ (\text{no integer global fixed point: detached}\Rightarrow
> \text{non-integral}\Rightarrow\text{Rosser}),\qquad
> \varprojlim^1=\widehat{\mathbb Z}_m/\mathbb Z\ (\text{the unit is a torsor}).$$
> Hence a full residuated tensor on $\overline{L}^{(m)}$ forces a non-integral (Rosser)
> unit, and the obstruction *is* the Pass-54 phantom. **Pass-54 obligations (1)
> [phantom realization] and (2) [Rosser torsor $=H^1$] are one statement:**
> $\varprojlim^1(\mathbb Z,\times m)=\widehat{\mathbb Z}_m/\mathbb Z$ is simultaneously
> the join-continuity-failure module of $\boxtimes_m$ and the Löb$\to$Rosser gluing
> obstruction $H^1(\text{dilation cover};\mathrm{Aut}(\text{unit}))$.

**Punchline (Smullyan-grade).** *Finitely Löb, limanly Rosser.* Every finite floor of
the solenoid is a consistent, Löb-attached, FG2-stabilizing world with an integral
unit; the tower of these worlds fails to glue into a single such world, and the
gluing obstruction — the uncountable $2$-adic ghost $\widehat{\mathbb Z}_m/\mathbb Z$ —
is at once the phantom $2$-cycle, the broken join-continuity, the lost FG2, and the
Rosser non-uniqueness of the unit. One $\varprojlim^1$ wearing four masks.

**Machine verification** (`code/scripts/check-pass55.py` →
`artifacts/reports/pass55-solenoid-boxtimes-lim1-rosser-fusion-check.json`, PASS):
*S* — $C_m=\mathbb Z[1/m]^-$ honest, $d_m$ a residuated embedding (injective, non-
surjective) for $m\in\{2,3\}$. *F* — dilation cover-fiber multiplier $=m$
($d_m(-1)=-m$) for $m\in\{2,3,6\}$. *P* — image tower $(\mathbb Z,\times m)$ non-ML
($\mathbb Z$-index $m,\dots,m^8\uparrow$) for $m\ge2$, every field ML, $m=1$ boundary.
*D* — even orbit strictly ascending (no stabilization $\Rightarrow$ nFG2 fails
cofinally) vs every finite truncation stabilizing (nFG2 holds). *G2* — $\boxtimes_m T
=a_0\not\le\bot$, vacuous. *R* — fixed-point/unit tower $(\mathbb Z,\times m)$:
$\varprojlim=0$ (detached, Rosser), $\varprojlim^1\ne0$ (torsor); finite truncations
integral (Löb).

**Open (Pass 56).** (i) Does $\overline{L}^{(m)}$ (MacNeille completion $+$ doubled
cover) stay a complete **residuated** lattice, or only a preAPS (does the doubled cover
$a^\ast\prec\{c,b^\ast\}$ break the residual, echoing the $M_n$, $n\ge3$, non-principal
fiber)? (ii) Write the $\check{\mathrm C}$ech complex of the dilation cover so Thm-55d's
$H^1=\varprojlim^1$ is a computation, closing Pass-54 obligation (2) at the cochain
level.

**References.** N. Galatos, P. Jipsen, T. Kowalski, H. Ono, *Residuated Lattices*
(Elsevier 2007), Ch. 3 (negative cones, integral residuated lattices); D. van Dantzig,
*Über topologisch homogene Kontinua*, Fund. Math. 15 (1930) (the $m$-adic / dyadic
solenoid); J. Milnor, *On axiomatic homology theory*, Pacific J. Math. 12 (1962)
($\varprojlim^1$); D. Guaspari & R. M. Solovay, *Rosser sentences*, Ann. Math. Logic
16 (1979); G. Boolos, *The Logic of Provability* (CUP 1993), Ch. 8 (de Jongh–Sambin);
R. M. Solovay, *Provability interpretations of modal logic*, Israel J. Math. 25 (1976).

## Pass 56 — Residuation/Rosser dichotomy of the completed solenoid, and the Čech complex of the dilation cover

Pass 55 left two residues of the completed arena $\overline{L}^{(m)}$ (the chain
$C_m=\mathbb Z[1/m]^-$ Dedekind-completed, with the Construction-49b doubled cover
$a^\ast\prec\{c,b^\ast\}\prec\top$ glued at the top): does it remain a complete
*residuated* lattice, and what is the explicit Čech complex realizing
$H^1=\varprojlim^1$? Pass 56 answers both, and the residuation answer is a **clean
dichotomy**: the doubled cover forces a choice between residuation and the Rosser unit.

### The dichotomy

Order-theoretically $\overline{L}^{(m)}$ is a complete chain $[-\infty,a^\ast]$ (where
$a^\ast=\bigvee_n a_n=0^-$ is the Dedekind completion of the dense $m$-adic chain) with
a *finite* $2^2$ diamond $\{a^\ast,c,b^\ast,\top\}$ glued at the shared bound $a^\ast$.
A chain is distributive; a finite distributive top glued along a single bound keeps the
whole lattice distributive; completeness is inherited. The *one* nontrivial directed
join is the cover $a^\ast=\bigvee_n a_n$, and binary meet distributes over it
($c\wedge\bigvee_n a_n=\bigvee_n(c\wedge a_n)=a^\ast$), so $\overline{L}^{(m)}$ is a
**frame** = complete Heyting algebra.

> **Theorem 56a (residuation/Rosser dichotomy).**
> 1. $\overline{L}^{(m)}$ is a complete distributive lattice and a frame, hence a
>    complete residuated lattice under $\otimes=\wedge$ with $x\backslash y=\bigvee\{z:
>    z\wedge x\le y\}$ and the **integral** unit $e=\top$ (the Löb regime).
> 2. The **dilation monoid** $\otimes=+$ (unit $e=a^\ast$, the predicted non-integral
>    Rosser unit, $c,b^\ast$ realized as positive infinitesimals just above $0=a^\ast$)
>    does **not** extend to a residuated structure: for the join-irreducible cover
>    $c\succ a^\ast$, the map $x\mapsto x\otimes c$ fails join-preservation at $a^\ast$,
>    $$\bigvee_n(a_n\otimes c)=\bigvee_n a_n=a^\ast \;<\; c \;=\; e\otimes c=a^\ast\otimes c,$$
>    since each $a_n<e$ gives $a_n\otimes c=a_n<a^\ast$ (infinitesimal shift staying
>    below $0$). The **minimal non-principal fiber** is $c\backslash a^\ast=\{z:z\otimes
>    c\le a^\ast\}=\{a_n\}_n$, whose supremum $a^\ast$ is not attained — the same
>    non-principal-fiber defect as the Pass-49 $M_n$ ($n\ge3$) obstruction, now sited at a
>    *non-attained* cover. Hence the dilation monoid makes $\overline{L}^{(m)}$ only a
>    complete **preAPS**.
> 3. (finite/liman contrast) Every finite truncation $\overline{L}^{(m)}_K$ is a complete
>    residuated lattice under **both** tensors: there $a^\ast=a_K$ is the chain *maximum*,
>    so $c\backslash a^\ast=a_{K-1}$ is principal and the additive tensor residuates.
>    Residuation of the dilation monoid is therefore a *finitely-true, limanly-false*
>    property, sharing its obstruction — join-discontinuity at the lone cover — with the
>    phantom (Thm 55b) and the nFG2/ML failure (Thm 55c).

So residuation and the Rosser unit are **mutually exclusive in the completion**: one may
keep residuation (Heyting, $\wedge$, integral $\top$ — but then Löb, and the dilation/
phantom content is discarded) or the Rosser dilation unit $a^\ast$ (but then only a
preAPS). The phantom and the residuation failure are *one* defect — join-discontinuity at
$a^\ast$ — seen through two maps: $\boxtimes_m$ (gives $\varprojlim^1$) and $\otimes$
(gives the non-principal fiber). **Slogan: finitely residuated, limanly preAPS** — the
residuation face of "finitely Löb, limanly Rosser."

### The Čech complex of the dilation cover

> **Construction/Theorem 56b ($H^1=\varprojlim^1$ at the cochain level).** The mapping
> telescope of $C_m\xrightarrow{d_m}C_m\xrightarrow{d_m}\cdots$ carries the two-set
> even/odd half-telescope cover $\mathcal U=\{U_0,U_1\}$, whose nerve is a single edge
> (an interval). Its $\check{\mathrm C}$ech complex on the dilation coefficient system
> $\underline{\mathbb Z}_{\times m}$ (stalk $\mathbb Z=\mathrm{Aut(unit)}$, restriction
> $\times m$) is the **two-term** complex
> $$\check{\mathrm C}^\bullet:\quad 0\to\underbrace{\textstyle\prod_n\mathbb Z}_{C^0}
>   \xrightarrow{\ \delta=\mathrm{id}-m\cdot\mathrm{sh}\ }
>   \underbrace{\textstyle\prod_n\mathbb Z}_{C^1}\to0,\qquad
>   \delta\big((x_n)\big)=(x_n-m\,x_{n+1}).$$
> Then $\check H^0=\ker\delta=\varprojlim(\mathbb Z,\times m)=0$ (coherence $x_0=m^nx_n$
> forces $x_0=0$ — the **detached** limit fixed point) and
> $$\check H^1=\operatorname{coker}\delta=\varprojlim{}^1(\mathbb Z,\times m)
>   =\widehat{\mathbb Z}_m/\mathbb Z\qquad(\widehat{\mathbb Z}_m=\textstyle\prod_{p\mid m}
>   \mathbb Z_p),$$
> via $x_0=\sum_{k<N}m^ky_k+m^Nx_N$ (partial sums converge $m$-adically; the cokernel is
> the $m$-adic completion modulo the honest integer solutions). The nerve being an
> interval, **only $H^0,H^1$** occur — no higher obstruction — so Thm-55d's
> $H^1(\text{dilation cover};\mathrm{Aut(unit)})=\varprojlim^1$ is a literal cochain
> identity, and the Rosser unit-torsor class is exactly $[(1,0,0,\dots)]\in
> \operatorname{coker}\delta$ (not in $\operatorname{im}\delta$ over $\mathbb Z$, but
> $m$-adically summable). Closes Pass-54 obligation (2) at the cochain level.

Machine-verified `code/scripts/check-pass56.py` $\to$
`artifacts/reports/pass56-solenoid-residuation-survival-cech-check.json` (PASS): *Rh* —
arena distributive, frame law at the cover, $\wedge$ residuates, unit $=\top$ integral;
*Rd* — finite truncations $K=2..8$ have principal cover ($\max=a_{K-1}$), the completion
has $\sup_n(a_n\otimes c)=a^\ast<c=a^\ast\otimes c$ (non-principal fiber); *Dich* —
residuation $\veebar$ Rosser-unit; *C* — $\ker\delta=0$, image indices $m^j\uparrow$ over
$\mathbb Z$ ($m\in\{2,3,6\}$, non-ML), ML over $\mathbb F_p$ ($p\nmid m$), two-term
complex. *Remaining proof obligations:* (i) the carrier-free cancellativity lemma
upgrading 56a.2 from "the natural additive extension fails" to "**no** residuated tensor
with unit $a^\ast$ exists"; (ii) identify $\operatorname{coker}\delta$ with the
Guaspari–Solovay Rosser choice-torsor as a *map of torsors*, not merely an iso of abelian
groups.

**References.** N. Galatos, P. Jipsen, T. Kowalski, H. Ono, *Residuated Lattices*
(Elsevier 2007), Ch. 3 (residuation $=$ join-preservation, principal residual fibers);
B. A. Davey & H. A. Priestley, *Introduction to Lattices and Order* (CUP, 2nd ed. 2002),
Ch. 7 (Dedekind–MacNeille completion, frames); P. T. Johnstone, *Stone Spaces* (CUP
1982), Ch. II (frames/locales); C. A. Weibel, *An Introduction to Homological Algebra*
(CUP 1994), §3.5 ($\varprojlim^1$ as cokernel of $\mathrm{id}-\mathrm{shift}$);
D. Guaspari & R. M. Solovay, *Rosser sentences*, Ann. Math. Logic 16 (1979).

## Pass 58 — The absorbing Rosser cap and the Phantom trichotomy

Pass 57's Lemma 57a forbade a completely join-irreducible cover $c\succ e$ above a
non-attained sup-of-chain (Rosser) unit $e=\bigvee_n a_n$ — but *only under the
strictness hypothesis* $a_n\otimes c<c$ (cancellativity). Is strictness load-bearing
or an artefact of the proof? Pass 58 settles it: strictness is **essential**, exhibited
by an explicit pathological residuated lattice in which the cover *absorbs*.

### The construction

> **Theorem 58a (absorbing Rosser cap $W$; strictness is essential).** Let
> $$ W:\qquad a_0=\bot\;<\;a_1\;<\;a_2\;<\;\cdots\;<\;e\;<\;c\;<\;\top,\qquad e=\bigvee_n a_n, $$
> a complete chain with $e$ the non-attained sup of the strictly ascending $\{a_n\}$,
> $c$ the unique cover of $e$, $\top$ the top. Put the unit at $e$ and define
> $$ x\otimes y=\begin{cases}\bot & x=\bot\text{ or }y=\bot,\\
> \min(x,y) & \bot\ne x,y\le e,\\ \max(x,y) & \text{otherwise (some operand }\ge c).\end{cases} $$
> Then $(W,\le,\otimes,\backslash,e)$ is a **complete commutative residuated lattice**
> in which $e$ is a non-attained sup-of-chain unit, $c$ is a **completely
> join-irreducible** cover of $e$, and $a_n\otimes c=c$ for every $n\ge1$ (**cofinal
> absorption**), while $\bot\otimes x=\bot$. Hence **Lemma 57a fails without
> cancellativity**: a complete residuated Rosser unit *may* carry a join-irreducible
> cover, provided the cover absorbs. *Proof.* Commutativity, associativity (case-split
> on the $\bot$-override versus the $\min/\max$ core), unit law at $e$, and
> monotonicity are routine. $\otimes$ preserves all joins in each argument: the empty
> join is the absorbing law $x\otimes\bot=\bot$, and the unique non-attained join
> $e=\bigvee_n a_n$ satisfies $x\otimes e=\bigvee_n(x\otimes a_n)$ for all $x$ (for
> $x=c$: both $c$, by cofinal absorption; for $x=a_k$: both $a_k$, by Gödel/min
> continuity). Join-preservation on a complete lattice is residuability, so the
> residual exists. Lemma 57a's computation $c=e\otimes c=\bigvee_n(a_n\otimes c)$ now
> holds with **every** summand already $=c$, so complete join-irreducibility is
> *satisfied*, not contradicted. $\square$

Read $W$ as a Gödel chain below the unit, a genuine absorbing zero at $\bot$ (forced:
$\bot=\bigvee\varnothing$ must be $\otimes$-fixed — the subtlety that sinks a naive
"large absorbs all" rule, which would set $c\otimes\bot=c$ and break the adjunction),
and a *large* region $\{c,\top\}$ that swallows the negative cone. The residual fiber
collapses: $c\backslash e=\bigvee\{w:c\otimes w\le e\}=\bigvee\{\bot\}=\bot$,
**principal** — versus the Pass-56 cancellative cover, where $c\backslash e=\{a_n\}_n$
climbs to the non-attained $e$ (non-principal). Same chain, opposite fiber.

### The price: the Phantom trichotomy

> **Theorem 58b (refined dichotomy / Phantom trichotomy).** For a complete residuated
> $\otimes$ with non-attained sup-of-chain unit $e=\bigvee_n a_n$ beneath a completely
> join-irreducible cover $c\succ e$, the action of the chain on $c$ is either
> **cancellative** ($a_n\otimes c<c$ cofinally — *impossible* by Cor 57a$'$; the unit
> is forced integral $\top$/Löb, and the Rosser unit survives only in the
> non-residuated MacNeille arena, fiber $\{a_n\}$ non-principal,
> $\varprojlim^1=\widehat{\mathbb Z}_m/\mathbb Z\ne0$) or **absorbing**
> ($a_n\otimes c=c$ cofinally — *realizable*, by $W$; residual present, fiber
> $c\backslash e=\bot$ principal, image tower $(a_n\otimes c)_n$ constant, ML,
> $\varprojlim^1=0$). With the Pass-57 quantale escape (residual present, cover
> *de-singularized*, $\varprojlim^1=0$) the **three** completions of a Rosser unit
> realize the three pairwise choices among
> $$\{\ \text{residuation},\quad\text{join-irreducible cover},\quad\text{phantom }\varprojlim^1\ \}: $$
> $$\begin{array}{l|ccc}
>  & \text{residual} & \text{cover} & \text{phantom}\\\hline
> \text{MacNeille} & \times & \checkmark & \checkmark\\
> \text{Ideal/quantale} & \checkmark & \times & \times\\
> \text{Absorbing cap }W & \checkmark & \checkmark & \times
> \end{array}$$
> **You may keep any two, never all three.**

The mechanism is uniform across the three vertices: residuation needs the cover fiber
*principal*. MacNeille leaves it non-principal (sup non-attained) — phantom lives,
residual dies. The quantale **splits** the chain's sup off below the cover ($\bigvee_n
\downarrow a_n\subsetneq\downarrow a^\ast$), making the fiber principal by destroying
the cover's join-irreducibility — residual returns, phantom dies. The absorbing cap
**collapses** the fiber to $\{\bot\}$ by idempotent absorption — residual returns, the
cover stays join-irreducible, but the constant image tower is Mittag–Leffler and the
phantom dies. Cancellative $=$ a *free* witness-comparison action (Guaspari–Solovay
re-choice torsor nontrivial); absorbing $=$ a *non-free* (collapsed) action, the
Rosser torsor degenerating to a point. The escape that keeps the cover pays with the
ghost, just as the quantale escape did — *Phantom $\veebar$ (residuation $\wedge$ cover)*.

### Naturality of $\Theta$, partially

> **Proposition 58c (naturality of $\Theta$ on the radical-graded subcategory).**
> Let $\mathbf{Deriv}^{\mathrm{res}}$ have as morphisms the interpretations that are
> simultaneously $\Box$-morphisms and residuated cover-filtration homomorphisms of the
> Lindenbaum APS (carrying the dilation chain $\{a_n\}$ cofinally to $\{a'_n\}$). Such
> a morphism induces a map of dilation towers $(\mathbb Z,\times m)\to(\mathbb Z,\times
> m')$ **iff** $\mathrm{rad}(m)\mid\mathrm{rad}(m')$, and then a map of phantoms
> $\widehat{\mathbb Z}_m/\mathbb Z\to\widehat{\mathbb Z}_{m'}/\mathbb Z$. On the
> **radical-graded** subcategory $\mathbf{Deriv}^{\mathrm{res}}_{\mathrm{rad}}$ (objects
> graded by $\mathrm{rad}(m)$, arrows by radical divisibility),
> $\Theta:\mathrm{Ros}_{(-)}\Rightarrow\varprojlim^1(-)$ is a **natural transformation**
> by snake-lemma naturality of the connecting map $\delta=\mathrm{id}-m\cdot
> \mathrm{sh}$; off it (rad-incompatible moduli) no tower morphism exists. *Naturality
> is governed by, and obstructed exactly by, radical divisibility.* (Carried: a full
> characterization of residuated $\mathbf{Deriv}$-morphisms, and whether the
> rad-obstruction is the only one.)

**Punchline.** Pass 57 said a residuated lattice refuses to host a Rosser unit beneath
a join-irreducible cover; Pass 58 says it *will*, on one condition — the cover must
swallow the whole approach to the unit, and in swallowing it the cover also swallows
the ghost. The cap that admits the Rosser unit is the cap with no phantom: a Smullyan
twist where the only world in which the forbidden object exists is the world where the
thing that made it interesting has vanished.

**Machine verification** (`code/scripts/check-pass58.py` →
`artifacts/reports/pass58-absorbing-rosser-cover-nogo-edge-check.json`, PASS): for
$K\in\{3,4,5,8\}$ the absorbing model $W_K$ is commutative, associative, unital at
$e$, monotone, residuated (adjunction $x\otimes y\le z\iff y\le x\backslash z$ over all
triples), join-preserving in each argument with the empty-join law $x\otimes\bot=\bot$;
cofinal absorption $a_n\otimes c=c$ ($n\ge1$), $\bot\otimes c=\bot$; $c$ a completely
join-irreducible cover; $c\backslash e=\bot$ (principal); $\bigvee_{n\ge1}(a_n\otimes
c)=c$ with the no-go evaded. The cancellative contrast on the same chain has fiber
$c\backslash e=\{a_0,\dots,a_7\}$ (non-principal). *Exec note:* the bash mount lagged
the Windows-path write (160-line truncated copy, SyntaxError at line 161), so per
[[aps-run-sync-hazard]] the run was confirmed by an off-mount inline exec re-deriving
the committed script; `code/scripts/check-pass58.py` (the 169-line source) is ground truth.

**References.** N. Galatos, P. Jipsen, T. Kowalski, H. Ono, *Residuated Lattices*
(Elsevier 2007), Ch. 3 (residuation $=$ join-preservation; $\bot$ as $\otimes$-zero);
B. A. Davey & H. A. Priestley, *Introduction to Lattices and Order* (CUP, 2nd ed. 2002),
Ch. 2–7 (complete chains, join-irreducibility, ideal completions); D. Guaspari &
R. M. Solovay, *Rosser sentences*, Ann. Math. Logic 16 (1979) (the witness-comparison
torsor); C. A. Weibel, *An Introduction to Homological Algebra* (CUP 1994), §3.5
($\varprojlim^1$, snake-lemma naturality).

## Pass 59 — The intermediate absorbing cover and the no-partial-phantom theorem

Pass 58's Phantom trichotomy fixed the two *extremes* of how the sup-of-chain unit
$e=\bigvee_n a_n$ acts on its join-irreducible cover $c\succ e$: pure cancellative
($a_n\otimes c<c$ for all $n$ — forbidden for residuation, Cor 57a$'$) and pure
absorbing ($a_n\otimes c=c$ for all $n\ge1$ — the cap $W$, phantom dead). The natural
worry is that *between* them lies a continuum of "partial phantoms," graded by how
late absorption switches on (the **absorption depth** $d=\inf\{n:a_n\otimes c=c\}$) and
by how badly the cover fails idempotence (the **idempotence defect**
$\iota=[\,c\otimes c\ne c\,]$). Pass 59 shows this picture is wrong in the most
satisfying way: the intermediate lattices genuinely exist, but the phantom does not see
them at all.

**The family $W_{d,\delta}$.** On the chain $a_0=\bot<a_1<\cdots<e<c<\top$ with
$e=\bigvee_n a_n$ non-attained, unit $e$, define
$$x\otimes y=\begin{cases}
\bot & \bot\in\{x,y\},\\
\min(x,y) & x,y\le e,\ \ne\bot,\\
\mathrm{big} & \text{exactly one operand }\mathrm{big}\ (\ge c),\ \mathrm{small}\ge a_d,\\
\mathrm{small} & \text{exactly one operand }\mathrm{big},\ \mathrm{small}<a_d,\\
\max(x,y) & \text{both big},\ \delta=0,\\
\top & \text{both big},\ \delta=1.
\end{cases}$$
Then $a_n\otimes c=c\iff n\ge d$, $a_n\otimes c=a_n<c$ for $1\le n<d$, the unit law
$e\otimes c=c$ holds ($e=a_K$, $K\ge d$), and $c\otimes c=\top\ne c\iff\delta=1$. Each
$W_{d,\delta}$ is a complete commutative residuated lattice (28 machine-checked
instances).

> **Theorem 59a (no partial phantom; the $(d,\iota)$-plane is phantom-flat).** With
> $e,c,\otimes$ as above and $d(\otimes)=\inf\{n:a_n\otimes c=c\}$:
> (1) $(a_n\otimes c)_n$ is non-decreasing with $\bigvee_n(a_n\otimes c)=e\otimes c=c$;
> (2) $d<\infty\Rightarrow$ the fiber tower is eventually constant $=c$ $\Rightarrow$
> Mittag–Leffler $\Rightarrow\varprojlim^1=0$: the phantom is **genuinely $0$**, never
> finitely supported ($\varprojlim^1$ is a tail/pro-invariant — truncating finitely
> many terms changes nothing); (3) $d=\infty\iff a_n\otimes c<c$ cofinally $\Rightarrow$
> no residuated tensor (Cor 57a$'$); (4) $\iota$ is independent of $d$ and localizes at
> the **compact** cover above $c$, not the non-compact cover $e\prec c$ where the
> phantom is pinned — so the whole family has $\varprojlim^1\equiv0$.

> **Corollary 59b (the trichotomy is sharp, not a continuum boundary).** Along the
> absorption axis $\varprojlim^1\in\{0,\widehat{\mathbb Z}_m/\mathbb Z\}$: by **Gray's
> dichotomy** the first derived limit of a tower of *countable* abelian groups is
> either $0$ or of cardinality $2^{\aleph_0}$, so no invariant can take a finite-rank
> intermediate value. The Pass-58 statement "any two of $\{$residuation, join-
> irreducible cover, phantom$\}$, never all three" is therefore *not* the edge of a
> spectrum; $(d,\iota)$ are genuine moduli of the lattice but phantom-flat coordinates,
> and the phantom jumps $0\to2^{\aleph_0}$ only at the single non-residuated wall
> $d=\infty$. *A phantom is all-or-nothing — there are no partial ghosts.*

> **Proposition 59c (depth $=$ nFG2 index $=$ ML $=$ phantom-free).** $d(\otimes)<\infty
> \iff$ the cover-fiber $\boxtimes$-orbit stabilizes $\iff$ all-level nFG2 (Thm 41a) $\iff$
> Mittag–Leffler (Thm 55c) $\iff\varprojlim^1=0$. The phantom is the residue of *perpetual*
> non-stabilization ($\neg$FG2, $d=\infty$), which lives outside residuation.

**Punchline.** Pass 58 found the one cap that hosts a Rosser unit — at the cost of the
ghost. Pass 59 asks whether you can buy *part* of the ghost back by relaxing
idempotence or stalling absorption, and the answer is a categorical no: $\varprojlim^1$
is a two-valued oracle (nothing, or a continuum), blind to every finite knob you can
turn. The intermediate caps are perfectly real lattices that the phantom simply
refuses to distinguish — a Smullyan island of objects invisible to the only instrument
that would make them interesting.

**Machine verification** (`code/scripts/check-pass59.py` →
`artifacts/reports/pass59-intermediate-absorbing-cover-no-partial-phantom-check.json`,
PASS): $K\in\{3,4,5,6\}$, all $1\le d\le K-1$, $\delta\in\{0,1\}$ — 28 models, each
commutative/associative/unital-at-$e$/monotone/join-preserving (with $x\otimes\bot=
\bot$)/residuated; absorption depth exactly $d$; $c\otimes c=\top\iff\delta=1$;
$\bigvee_{n\ge1}(a_n\otimes c)=c$. Finite-depth fiber towers are ML ($\varprojlim^1=0$);
the contrast dilation tower $(\mathbb Z,\times m)$, $m\in\{2,3,4,6\}$, has strictly
increasing image indices $m^k$ (non-ML, the $\widehat{\mathbb Z}_m/\mathbb Z$ phantom),
and no family yields a finite-nonzero cokernel — consistent with Gray's dichotomy.
*Exec note:* run off-mount in `/tmp`; the bash mount served a Pass-53-era stale copy of
the discussion file while Windows-path tools showed it complete through Pass 58, so per
[[aps-run-sync-hazard]] correctness was confirmed off-mount and edits applied via
Windows-path file tools.

**References.** B. I. Gray, *Spaces of the same $n$-type for all $n$*, Topology 5
(1966) 241–243 (the $\varprojlim^1$ $0$-or-uncountable dichotomy for towers of countable
groups); C. A. McGibbon & J. M. Steiner, *Some questions about the first derived functor
of the inverse limit*, J. Pure Appl. Algebra 103 (1995) 325–340; C. A. McGibbon,
*Phantom maps*, in *Handbook of Algebraic Topology* (North-Holland 1995) §1–3; C. A.
Weibel, *An Introduction to Homological Algebra* (CUP 1994), §3.5 (Mittag–Leffler
$\Rightarrow\varprojlim^1=0$); N. Galatos, P. Jipsen, T. Kowalski, H. Ono, *Residuated
Lattices* (Elsevier 2007), Ch. 3.

## Pass 60 — The carrier criterion, sole-obstruction naturality of $\Theta$, and the ZFC-independent $\aleph_1$-phantom

Passes 53–59 built the functor $L_{(-)}$, the dilation-solenoid arenas $C_m=\mathbb
Z[1/m]^-$, the phantom $\varprojlim^1(\mathbb Z,\times m)=\widehat{\mathbb Z}_m/\mathbb
Z$, and (Thm 57b) the torsor iso $\mathrm{Ros}_m\cong\widehat{\mathbb Z}_m/\mathbb Z$ at
each *fixed* $m$. Two gaps remained. First, the comparison transformation
$\Theta:\mathrm{Ros}_{(-)}\Rightarrow\varprojlim^1(-)$ was only checked pointwise; its
**naturality** across moduli was conjectured to live on a radical-graded subcategory
$\mathbf{Deriv}^{\mathrm{res}}_{\mathrm{rad}}$ whose arrows were *decreed* rather than
characterized (Prop 58c). Second, Gray's $0$-or-$2^{\aleph_0}$ dichotomy (Cor 59b) was a
theorem about *countable* towers; its fate under an uncountable cover was open. Pass 60
closes both — the first absolutely, the second by an independence result.

### The carrier forces the grading

> **Theorem 60a (morphism-lifting / carrier criterion).** For $m,m'\ge2$ TFAE:
> (i) there is a residuated cover-filtration map $C_m\to C_{m'}$ of dilation-solenoid
> arenas (Pass 55) preserving $\otimes,\backslash$, the rung filtration $\{a_n\}$, and
> the limit cover $a^\ast$;
> (ii) the localization embeds, $\mathbb Z[1/m]\subseteq\mathbb Z[1/m']$;
> (iii) $\mathrm{rad}(m)\subseteq\mathrm{rad}(m')$, i.e. $\mathrm{rad}(m)\mid
> \mathrm{rad}(m')$.
> Hence $\mathbf{Deriv}^{\mathrm{res}}_{\mathrm{rad}}$ is, up to the rad-grading, the
> **squarefree divisibility lattice** $(\mathcal P_{\mathrm{fin}}(\mathbb P),\subseteq)$
> of finite prime-sets under inclusion, and the pinned morphism class is the
> localization inclusions $\{\iota_{m,m'}:\mathrm{rad}(m)\mid\mathrm{rad}(m')\}$.

*Proof.* (ii)$\Leftrightarrow$(iii): $\mathbb Z[1/m]=\mathbb Z[\{1/p:p\mid m\}]$, so the
inclusion holds iff every $1/p$ ($p\mid m$) is invertible in $\mathbb Z[1/m']$, iff
$p\mid m'$, iff $\mathrm{rad}(m)\subseteq\mathrm{rad}(m')$. (ii)$\Rightarrow$(i): the
negative-cone inclusion $\iota:\mathbb Z[1/m]^-\hookrightarrow\mathbb Z[1/m']^-$
preserves $+$, $\min(0,\cdot)$, order, sends rungs $-1/m^k$ into the finer $m'$-adic
rung filtration and the unique non-attained sup $a^\ast_m=0^-$ to $a^\ast_{m'}=0^-$.
(i)$\Rightarrow$(ii): any $\otimes$-preserving order map fixing $0$ and respecting the
rung filtration restricts to a unital ordered-monoid embedding of negative cones, whose
existence forces $\mathbb Z[1/m]\subseteq\mathbb Z[1/m']$ on denominators. $\square$

So the rad-grading is **not** an external decree (the Prop-58c worry): it is the exact
denominator condition for the *carrier* localizations to nest. The category was right;
Pass 60 supplies its missing universal property.

### Naturality, and the sole obstruction

On the cochain side every arena's phantom is $\check H^1$ of one shape of map,
$\delta_m=\mathrm{id}-m\cdot\mathrm{sh}:\prod_n\mathbb Z\to\prod_n\mathbb Z$
(Thm 56b), with $\check H^1(\delta_m)=\widehat{\mathbb Z}_m/\mathbb Z=(\prod_{p\mid m}
\mathbb Z_p)/\mathbb Z$. The inclusion $\iota$ of Thm 60a induces the **coordinate
insertion** $\widehat{\mathbb Z}_m/\mathbb Z\to\widehat{\mathbb Z}_{m'}/\mathbb Z$
(identity on the shared $\mathbb Z_p$, $0$ on the primes of $m'$ not in $m$, compatible
with the diagonal $\mathbb Z$).

> **Theorem 60b (rad-divisibility is the sole naturality obstruction).** Regard
> $\mathrm{Ros}_{(-)},\ \varprojlim^1(-):\mathbf{Deriv}^{\mathrm{res}}_{\mathrm{rad}}
> \to\mathbf{Tors}$ as $m\mapsto\mathrm{Ros}_m$, $m\mapsto\widehat{\mathbb Z}_m/\mathbb
> Z$, with arrows $\iota_{m,m'}$ acting by coordinate insertion. Then
> $\Theta=(\Theta_m)_m$ is a **natural isomorphism**: for every arrow ($\mathrm{rad}(m)
> \mid\mathrm{rad}(m')$) the square
> $$\begin{array}{ccc}
> \mathrm{Ros}_m & \xrightarrow{\ \Theta_m\ } & \widehat{\mathbb Z}_m/\mathbb Z\\
> \ \downarrow{\scriptstyle\mathrm{Ros}(\iota)} & & \ \downarrow{\scriptstyle\iota_\ast}\\
> \mathrm{Ros}_{m'} & \xrightarrow{\ \Theta_{m'}\ } & \widehat{\mathbb Z}_{m'}/\mathbb Z
> \end{array}$$
> commutes. Rad-divisibility is the **unique** obstruction: a $\Theta$-natural arrow
> $m\to m'$ exists iff $\mathrm{rad}(m)\mid\mathrm{rad}(m')$, and where one exists no
> further condition is needed.

*Proof.* Existence is Thm 60a. Commutativity: $\Theta_m,\Theta_{m'}$ are the identity
cochain isomorphisms (Thm 56b/57b); $\mathrm{Ros}(\iota)$ and $\iota_\ast$ are both
induced by the same cochain inclusion $\prod_n\mathbb Z\hookrightarrow\prod_n\mathbb Z$
intertwining $\delta_m,\delta_{m'}$ on shared coordinates, so by snake-lemma naturality
of the $\varprojlim/\varprojlim^1$ connecting map (Prop 58c) the two induced maps on
$\check H^1$ coincide. Each $\Theta_m$ is bijective (Thm 57b). $\square$

**Slogan.** $\Theta$ is a natural isomorphism of the **phantom presheaf** $S\mapsto
(\prod_{p\in S}\mathbb Z_p)/\mathbb Z$ with the **Rosser-torsor presheaf**, on the prime
spectrum ordered by inclusion of squarefree supports. The Löb/Rosser dictionary is now a
single statement about two presheaves on $\mathrm{Spec}$.

> **Corollary 60c (incomparable-phantom pathology).** $m=6$, $m'=10$ are rad-incomparable
> ($\mathrm{rad}(6)=\{2,3\}$, $\mathrm{rad}(10)=\{2,5\}$): $\mathbf{Deriv}^{\mathrm{res}}
> _{\mathrm{rad}}$ has **no** arrow either way, so naturality between their phantoms
> $(\mathbb Z_2\times\mathbb Z_3)/\mathbb Z$ and $(\mathbb Z_2\times\mathbb Z_5)/\mathbb
> Z$ is mediated only by a common lower bound: the gcd-of-radicals solenoid $C_2$
> ($\mathrm{rad}=\{2\}$) maps into both, and the **shared $2$-adic ghost** $\mathbb Z_2/
> \mathbb Z$ is the image of both $\iota_{2,6}{}_\ast$ and $\iota_{2,10}{}_\ast$. The
> rad-lattice has finite meets ($\gcd$ of radicals) and joins ($\mathrm{lcm}$); $\Theta$
> is a natural iso of lattice-indexed functors, the phantom gluing $2$-adically along the
> join $C_{30}$ and restricting to $C_2$ along the meet.

### The set-theoretic frontier

> **Theorem 60d (Gray's dichotomy is strictly an $\omega$-phenomenon).** Replace the
> ascending front $\{a_n\}_{n<\omega}$ by a strictly ascending $\omega_1$-chain
> $\{a_\xi\}_{\xi<\omega_1}$ with non-attained supremum (a "long cover"), giving the
> cover-fiber inverse system $\mathbf A_{\omega_1}$ indexed by $\omega_1$. Then the
> $0$-or-$2^{\aleph_0}$ dichotomy of Cor 59b **is not a theorem of ZFC** for
> $\mathbf A_{\omega_1}$: up to pro-isomorphism $\mathbf A_{\omega_1}$ is the
> Mardešić–Prasolov strong-homology system, whose derived limit obeys
> $$\varprojlim{}^1\mathbf A_{\omega_1}\ne0\ \text{under CH},\qquad
> \varprojlim{}^1\mathbf A_{\omega_1}=0\ \text{under PFA}.$$
> Hence "a genuinely $\aleph_1$-engendered intermediate phantom exists" is **independent
> of ZFC** — present under CH (Mardešić–Prasolov 1988), killed by $\mathrm{MA}_{\aleph_1}$
> a fortiori PFA (Dow–Simon–Vaughan 1989).

*Reading.* The countable phantom $\widehat{\mathbb Z}_m/\mathbb Z$ is a ZFC-absolute
$2^{\aleph_0}$-object — Gray's dichotomy is a hard theorem precisely because $\omega$ has
countable cofinality and the image filtration is a sequence. At cofinality $\omega_1$ the
derived limit ceases to be absolute: it becomes a forcing-axiom / Suslin-line invariant.
The "intermediate phantom" the Pass-59 [New] item sought therefore *does* exist — but not
as a ZFC-fixed cardinal: it is a **model-dependent ghost**, haunting the CH universe and
exorcised by Martin's Axiom, refuted by no internal datum of either. This is the
no-partial-phantom theorem's sharp boundary: *no partial phantom at $\omega$ (Gray), but a
whole undecidable phantom at $\omega_1$.*

**Machine verification** (`code/scripts/check-pass60.py` →
`artifacts/reports/pass60-rad-obstruction-naturality-theta-check.json`, PASS, run
off-mount per [[aps-run-sync-hazard]]): *A* — over all $144$ pairs from
$\{1,2,3,4,5,6,8,9,10,12,15,30\}$, $\mathbb Z[1/m]\subseteq\mathbb Z[1/m']\iff
\mathrm{rad}(m)\mid\mathrm{rad}(m')$ ($0$ violations, Thm 60a). *B* — image-index tower
$m^k$ strictly increasing (phantom present) iff $m\ge2$; $m=1$ constant. *C* — $\Theta$ is
$G_m=(\mathbb Z/m^K)^\times$-equivariant (the endomorphism/automorphism case of Thm 60b):
$\Theta(u\cdot x)=u\cdot\Theta(x)$ for all units $u$, all sampled $x$, $m\le30$. *D* —
diagonal $\mathbb Z$ compatibly placed in both completions for every rad-divisible pair.
*E* — the $6$/$10$ incomparable pathology (Cor 60c): neither rad divides the other,
shared modulus $=2$, mapping into both. *F* — the rad-grading satisfies reflexivity,
antisymmetry-on-radicals, transitivity (squarefree-divisibility-lattice structure).
Overall PASS.

**References.** S. Mardešić & A. V. Prasolov, *Strong homology is not additive*, Trans.
Amer. Math. Soc. 307 (1988) 725–744 ($\varprojlim^1$ of the relevant $\omega_1$-system is
nonzero under CH); A. Dow, P. Simon & J. E. Vaughan, *Strong homology and the proper
forcing axiom*, Proc. Amer. Math. Soc. 106 (1989) 821–828 (it vanishes under PFA);
B. I. Gray, *Spaces of the same $n$-type for all $n$*, Topology 5 (1966) 241–243; J.-P.
Serre, *Local Fields* (Springer 1979) ($\widehat{\mathbb Z}=\prod_p\mathbb Z_p$);
N. Galatos, P. Jipsen, T. Kowalski, H. Ono, *Residuated Lattices* (Elsevier 2007), Ch. 3
(negative cones, localizations); T. Jech, *Set Theory*, 3rd ed. (Springer 2003), Ch. 16
($\mathrm{MA}_{\aleph_1}$, Suslin's hypothesis, PFA).

## Pass 61 — Descent, sheafification, and the Rosser torsor as the obstruction to descent

Pass 60's closing slogan called $S\mapsto(\prod_{p\in S}\mathbb Z_p)/\mathbb Z$ "the
phantom **sheaf**." Pass 61 takes that word literally and finds it **false in the stated
direction**: the phantom presheaf is not a sheaf, its sheafification *discards* the Rosser
content, and the Rosser torsor is correctly the **obstruction to descent**, not the
sheafification. The correction is clean and turns the Löb/Rosser dictionary into a
sheaf-vs-cosheaf adjunction.

### The presheaf resolution

On the prime lattice $(\mathcal P_{\mathrm{fin}}(\mathbb P),\subseteq)$ with the
prime-cover topology — a sieve covers $S$ iff it contains every singleton $\{p\}$,
$p\in S$, and **restriction is coordinate projection** $\mathcal F(S)\twoheadrightarrow
\mathcal F(S')$ for $S'\subseteq S$ (the *contravariant* "meet $=$ restriction" maps, not
Pass 60's covariant insertions) — resolve the phantom into a short exact sequence of
presheaves of abelian groups:
$$0\ \to\ \underline{\mathbb Z}\ \xrightarrow{\ \Delta\ }\ \mathcal F\ \xrightarrow{\ \pi\ }\ P\ \to\ 0,
\qquad \mathcal F(S)=\prod_{p\in S}\mathbb Z_p,\quad \underline{\mathbb Z}(S)=\mathbb Z,$$
$\Delta:1\mapsto(1)_{p\in S}$ diagonal, $P(S)=(\prod_{p\in S}\mathbb Z_p)/\mathbb Z$.

> **Theorem 61a (descent failure / sheafification).**
> 1. $\mathcal F$ is a **flasque sheaf** (a product of skyscrapers; the singleton-cover
>    equalizer degenerates to $\mathcal F(S)=\prod_p\mathcal F(\{p\})$ since pairwise
>    meets are $\varnothing$ and $\mathcal F(\varnothing)=0$), so $\check H^{\ge1}(-,
>    \mathcal F)=0$.
> 2. $\underline{\mathbb Z}$ (constant presheaf) is **not separated**: its sheafification
>    is the locally constant sheaf $\underline{\mathbb Z}^{\#}(S)=\mathbb Z^{S}=
>    \bigoplus_{p\in S}\mathbb Z$, with separation defect
>    $\mathbb Z^{S}/\Delta\mathbb Z\cong\mathbb Z^{|S|-1}$.
> 3. Hence $P$ **fails descent**: $P(S)\to\prod_{p\in S}P(\{p\})$ is surjective with kernel
>    $\cong\mathbb Z^{|S|-1}\ne0$ for $|S|\ge2$. The sheafification is the **stalkwise**
>    sheaf $P^{\#}=L$, $L(S)=\prod_{p\in S}(\mathbb Z_p/\mathbb Z)$ (stalk $\mathbb Z_p/
>    \mathbb Z$ at $p$), and the unit $P\twoheadrightarrow L$ has kernel
>    $\mathbb Z^{S}/\Delta\mathbb Z\cong\mathbb Z^{|S|-1}$.

*Proof.* Sheafify the SES; $a^{\#}$ is exact and $\mathcal F$ is already a sheaf, so
$P^{\#}=\mathcal F/\underline{\mathbb Z}^{\#}=\prod_p(\mathbb Z_p/\mathbb Z)=L$. The
comparison $0\to\mathbb Z^{S}/\Delta\mathbb Z\to P(S)\to L(S)\to0$ exhibits the kernel;
$\operatorname{coker}(\Delta:\mathbb Z\to\mathbb Z^{S})=\mathbb Z^{|S|-1}$ by Smith normal
form of the all-ones column (invariant factor $1$, free rank $|S|-1$, no torsion).
$\square$

### Rosser is the obstruction, not the sheafification

> **Theorem 61b (Rosser $=$ failure of descent).** The Rosser torsor $\mathrm{Ros}_m\cong
> \widehat{\mathbb Z}_m/\mathbb Z=P(S)$ ($S=\mathrm{rad}(m)$) is **not** the sheafification
> $L$. Sheafification kills the Rosser content. The Löb/Rosser dictionary splits along
> $P\twoheadrightarrow L$:
> - **Löb / sheaf:** $L(S)=\prod_p(\mathbb Z_p/\mathbb Z)$, the descent-respecting
>   stalkwise datum — "consistency is local at each prime";
> - **Rosser / phantom:** the **failure of descent**, $\ker(P\to L)$, with a *horizontal*
>   free part $\mathbb Z^{|S|-1}=\check H^1(\underline{\mathbb Z})$ over the prime cover
>   and a *vertical* $\varprojlim^1=\widehat{\mathbb Z}_p/\mathbb Z$ (dilation tower) inside
>   each stalk.
>
> The Pass-60 slogan holds only after **dualizing**: $P$ is a flabby *cosheaf*; its
> *cosheafification* (left adjoint, colimit glueing) reconstitutes the global
> $\widehat{\mathbb Z}_m/\mathbb Z$, while the *sheafification* (right adjoint) discards it.
> Slogan corrected: **Löb $=$ sheaf, Rosser $=$ cosheaf.**

This is the Skeptic's two-limits point made precise: the spectral (horizontal) cover and
the dilation (vertical) tower are orthogonal; the horizontal $\check H^1$ is the
*countable* free $\mathbb Z^{|S|-1}$, the vertical $\varprojlim^1$ is the *uncountable*
$2$-adic ghost, and the Rosser torsor is their amalgam — never visible in the sheaf $L$,
which is blind to both (it quotients out the horizontal relations and keeps each stalk
$\mathbb Z_p/\mathbb Z$ as a bare group).

### The cardinal threshold, sharpened

> **Theorem 61c ($\mathfrak b=\aleph_1$ wall; the threshold is bracketed, not named).** For
> the long ($\omega_1$-cofinal) cover, $\mathbf A_{\omega_1}$ the cover-fiber system:
> (a) $\mathfrak b=\aleph_1\Rightarrow\varprojlim^1\mathbf A_{\omega_1}\ne0$ — non-vanishing
> follows from $\mathfrak b=\aleph_1$ alone (strictly weaker than CH), since the
> Mardešić–Prasolov class is built from an unbounded $\le^*$-tower of length $\omega_1$.
> (b) $\mathrm{MA}_{\aleph_1}\Rightarrow\varprojlim^1\mathbf A_{\omega_1}=0$ (Dow–Simon–
> Vaughan), and $\mathrm{MA}_{\aleph_1}\Rightarrow\mathfrak b\ge\mathfrak p>\aleph_1$. So
> the threshold is **bracketed** $[\mathfrak b=\aleph_1\Rightarrow\ne0]$,
> $[\mathrm{MA}_{\aleph_1}\Rightarrow0]$, but admits **no** ZFC equivalence
> "$=0\iff\mathfrak X=\aleph_2$" for a single classical characteristic $\mathfrak X$; it is
> a genuinely higher (additivity-of-ideal-flavored) invariant, Suslin-sensitive in the gap.
> (c) An $\aleph_2$-cofinal cover yields **not** a $0/\aleph_1/2^{\aleph_0}$ trichotomy but
> a *sequence* of higher derived limits $\varprojlim^s\mathbf A_{\omega_2}$ ($s\ge2$) whose
> (non)vanishing is an independent family (the strong-homology spectrum); the clean
> dichotomy is special to cofinality $\omega$.

**Machine verification** (`code/scripts/check-pass61.py` →
`artifacts/reports/pass61-phantom-sheaf-descent-check.json`, PASS, run off-mount per
[[aps-run-sync-hazard]]): *coker_rank* — $\operatorname{coker}(\Delta:\mathbb Z\to
\mathbb Z^{S})$ free of rank $|S|-1$, no torsion, by SNF, $|S|=2..6$. *product_presheaf_descent*
— $\mathcal F(S)=\prod_p\mathbb Z/p^K$ satisfies the singleton-cover equalizer for
$S=\{2,3\},\{2,3,5\},\{3,5,7\},\{2,5,7,11\}$. *sheafification_kernel_rank* — $P(S)
\twoheadrightarrow L(S)$ kernel rank $|S|-1$. *rad_lattice_glue_restrict* — over all $64$
pairs from $\{2,3,4,6,10,12,15,30\}$, meet $=\gcd$-of-radicals (restriction), join
$=\mathrm{lcm}$-of-radicals (glueing). Overall PASS. Thm 61c is a literature result, not
machine-checkable.

**References.** Same set-theoretic sources as Pass 60 (Mardešić–Prasolov 1988;
Dow–Simon–Vaughan 1989); for the presheaf/sheaf/cosheaf machinery, R. Hartshorne,
*Algebraic Geometry* (Springer 1977), Ch. II.1 (sheafification, flasque sheaves);
J. Lurie, *Higher Topos Theory* (2009), §7.3 / S. Mac Lane & I. Moerdijk, *Sheaves in
Geometry and Logic* (Springer 1992), Ch. II–III (Grothendieck topologies, the
$\mathbf{Sh}\hookrightarrow\mathbf{PSh}$ adjunctions); for cosheaves, J. Curry,
*Sheaves, Cosheaves and Applications* (PhD thesis, 2014).

## Pass 62 — The Löb–Rosser bicomplex and the mixed class

Pass 61 split the total phantom $P(S)=\widehat{\mathbb Z}_S/\mathbb Z$ ($S=\mathrm{rad}(m)$)
into a *horizontal* free part $\mathbb Z^{|S|-1}=\check H^1_{\mathrm{prime}}(\underline{\mathbb
Z})$ (the descent defect of the constant presheaf over the prime cover) and a *vertical*
$\varprojlim^1=\widehat{\mathbb Z}_p/\mathbb Z$ (the dilation tower) inside each stalk, and
floated the slogan "Rosser $=$ cosheaf, Löb $=$ sheaf." Pass 62 assembles the two obstructions
into one bicomplex, reads the dictionary off its $E_2$ page, locates the "mixed class," and
**corrects** the cosheaf slogan.

### The bicomplex

Factor the phantom through a single $\mathbb N$-tower. By CRT $\mathbb Z/\pi^n\cong\prod_{p\in S}
\mathbb Z/p^n$ with $\pi=\prod_{p\in S}p=\mathrm{rad}(m)$, so (Pass 53/54) $\varprojlim^1(\mathbb
Z,\times\pi)=\widehat{\mathbb Z}_S/\mathbb Z=P(S)$. Build the first-quadrant double complex
$D^{\bullet,\bullet}$ with **vertical** differential the two-term Milnor cochain
$[\prod_n\mathbb Z\xrightarrow{1-p\,\mathrm{sh}}\prod_n\mathbb Z]$ of the per-prime dilation
tower $(\mathbb Z,\times p)$ — homology $H^0=\varprojlim=0$, $H^1=\varprojlim^1=\mathbb Z_p/\mathbb
Z$ — and **horizontal** differential the augmented reduced Čech cochain of $\underline{\mathbb Z}$
over the singleton prime cover — $\operatorname{coker}(\Delta:\mathbb Z\to\mathbb Z^S)=\mathbb
Z^{|S|-1}$, nothing higher.

> **Theorem 62a ($E_2 =$ the Löb/Rosser dictionary).** $H^1(\mathrm{Tot}\,D)=\widehat{\mathbb Z}_S/
> \mathbb Z=P(S)$, and both filtration spectral sequences degenerate at $E_2$ to exactly
> $$E_2^{1,0}=\mathbb Z^{|S|-1}\ \ (\text{Rosser, horizontal: integer relations among the primes}),
> \qquad E_2^{0,1}=\textstyle\prod_{p\in S}(\mathbb Z_p/\mathbb Z)=L(S)\ \ (\text{Löb, vertical:
> local ghosts}),$$
> all other $E_2^{p,q}=0$; in particular $E_2^{2,0}=\tilde H^2_{\mathrm{prime}}=0$ (the discrete
> cover has no $1$-simplices) and $E_2^{0,2}=\varprojlim^2=0$ ($\omega$-tower).

### The mixed class is an extension, not a differential

With the only survivors at the complementary cells $(1,0)$ and $(0,1)$ and their neighbours
zero, every $d_r$ ($r\ge2$) has zero target. So $E_2=E_\infty$ and the entire "horizontal $\to$
vertical mixing" the Pass-61 Next-step anticipated as a "$d_2$" is concentrated in the
**filtration extension**.

> **Theorem 62b (mixed Löb–Rosser class $=$ non-split extension).** The two-step filtration of
> $H^1(\mathrm{Tot})$ is
> $$0\to\underbrace{\mathbb Z^{|S|-1}}_{\text{Rosser}}\xrightarrow{\iota}\widehat{\mathbb Z}_S/
> \mathbb Z\xrightarrow{\rho}\underbrace{\textstyle\prod_{p\in S}(\mathbb Z_p/\mathbb Z)}_{\text{Löb}
> =L(S)}\to0,\quad\iota=[\mathbb Z^S/\Delta\mathbb Z\hookrightarrow\widehat{\mathbb Z}_S/\Delta\mathbb
> Z],\ \rho=\text{quotient by }\mathbb Z^S.$$
> For $|S|\ge2$ it does **not split**: a retraction $P\twoheadrightarrow\mathbb Z^{|S|-1}$ would
> restrict to $\mathrm{Hom}(\mathbb Z_p,\mathbb Z)=0$ on each stalk ($\mathbb Z_p$ is $q$-divisible
> for every $q\ne p$, and $\mathbb Z$ has no nonzero divisible subgroup), hence annihilate the
> integer points $e_p\in\mathbb Z^S$ that generate $\mathbb Z^S/\Delta\mathbb Z$ — contradiction.
> The class $\epsilon_S\in\mathrm{Ext}^1_{\mathbb Z}(L(S),\mathbb Z^{|S|-1})$ is nonzero: the mixed
> class is the connecting $\partial$ of the filtration, with no pure-horizontal or pure-vertical
> representative. A genuine page $d_2:E_2^{0,1}\to E_2^{2,0}$ realizing the same datum reappears
> only after **unabridging** each $\mathbb Z_p$ into its $\mathbb Z/p^n$-tower (which creates a
> third column $E_2^{2,0}\ne0$ — the obstruction to lifting the $p$-adic generator to an integer).

**Pathology ($S=\{2,3\}$).** $\widehat{\mathbb Z}_S/\mathbb Z=(\mathbb Z_2\times\mathbb Z_3)/
\Delta\mathbb Z$. The horizontal generator $g=[(1,0)]=[(0,-1)]$ spans $\mathbb Z^{|S|-1}=\mathbb Z$
and maps to $0$ in $L$ (every integer dies in $\mathbb Z_p/\mathbb Z$), yet $g$ is **not** a direct
summand — no homomorphism $P\to\mathbb Z$ carries $g\mapsto1$, since any such map vanishes on
$\mathbb Z_2$ and $\mathbb Z_3$ and $g$ is assembled from those factors. A purely horizontal
relation with no horizontal complement: the integer relation among the primes is welded to the
local ghosts — Smullyan's seam with no scissors.

### Cosheafification collapses — the slogan corrected

> **Theorem 62c (sheaf $=$ cosheaf on the discrete site).** On the singleton (discrete) prime
> site the cosheafification of $P$ is the costalk coproduct $\check P(S)=\bigoplus_{p\in S}
> (\mathbb Z_p/\mathbb Z)$; for finite $S$ the canonical $\bigoplus_{p\in S}\to\prod_{p\in S}$ is
> an isomorphism, so $\check P(S)=\prod_{p\in S}(\mathbb Z_p/\mathbb Z)=L(S)=P^{\#}(S)$:
> **sheafification and cosheafification coincide**, both equal to the Löb sheaf $L$. Hence the
> global phantom $\widehat{\mathbb Z}_S/\mathbb Z$ — a non-split extension of $L$ by
> $\mathbb Z^{|S|-1}$ (Thm 62b) — is **neither** sheaf nor cosheaf; it is irreducibly
> presheaf-level, recorded exactly by the descent defect $\ker\rho=\mathbb Z^{|S|-1}$. The
> Pass-61 slogan "Rosser $=$ cosheaf" is **false on the discrete prime site**: that topology is
> too disconnected for the two adjoints to differ. A nonzero $\check H^1$ — and a true
> cosheaf-theoretic home for the Rosser class — requires the coarser **Zariski/cofinite**
> topology on $\mathrm{Spec}\,\mathbb Z$, where the prime set $S$ acquires the generic point and
> the cover $\{V(p)\}$ has nonempty intersections.

So the corrected dictionary is: **Löb $=$ the common (co)sheafification $L=\prod_p(\mathbb Z_p/
\mathbb Z)$** (stalkwise, descent-respecting, blind to the horizontal relations); **Rosser $=$
the descent defect $\mathbb Z^{|S|-1}=\ker(P\to L)$**, an $\mathrm{Ext}^1$/$\check H^1$ datum that
neither adjoint sees on the discrete site, glued to the local ghosts by the non-split seam
$\epsilon_S$. The discrete topology is a Procrustean bed: it flattens $\mathbf{Sh}$ and
$\mathbf{coSh}$ onto each other, and the Rosser phantom survives only as a *presheaf*.

**Machine verification** (`code/scripts/check-pass62.py` →
`artifacts/reports/pass62-loeb-rosser-bicomplex-mixed-class-check.json`, PASS, run off-mount per
[[aps-run-sync-hazard]]): *coker_rank* — $\operatorname{coker}(\Delta:\mathbb Z\to\mathbb Z^S)$
free of rank $|S|-1$, no torsion, by SNF, $|S|=2..6$. *no_retraction* — the $\mathrm{Hom}(\mathbb
Z_p,\mathbb Z)=0$ obstruction (forced $r_n=p^{-n}\notin\mathbb Z$, $n\ge1$) for
$p\in\{2,3,5,7,11\}$, the non-splitting certificate of Thm 62b. *tower_higher_derived* — Milnor
cochain length $2$, $\varprojlim^{\ge2}=0$. *reduced_cech_no_d2* — for $S=\{2,3\},\{2,3,5\},
\{3,5,7\},\{2,5,7,11\}$ all pairwise intersections empty, no $1$-simplices, $E_2^{2,0}=0$,
$d_2$ cannot act. *cosheaf_collapse* — $|\bigoplus|=|\prod|$ for $S=\{2,3\},\{2,3,5\},\{3,5,7\}$,
cosheafification $=$ sheafification $=L$. *crt_radical* — phantom a functor of $\mathrm{rad}$.
Overall PASS.

**References.** For the spectral sequence of a double complex and the filtration/extension
$E_\infty$ problem, C. A. Weibel, *An Introduction to Homological Algebra* (CUP 1994), §5.6;
for $\varprojlim,\varprojlim^1$ and the Milnor sequence, *ibid.* §3.5; $\mathrm{Hom}(\mathbb Z_p,
\mathbb Z)=0$ and the structure of $\mathbb Z_p/\mathbb Z$ as a divisible (injective) group,
L. Fuchs, *Abelian Groups* (Springer 2015), Ch. 1–2; cosheaves and the costalk coproduct,
J. Curry, *Sheaves, Cosheaves and Applications* (PhD thesis, 2014); the Zariski topology of
$\mathrm{Spec}\,\mathbb Z$, R. Hartshorne, *Algebraic Geometry* (Springer 1977), Ch. II.1–2.

## Pass 63 — Zariski relocation, the unabridged $d_2$, and the $\mathrm{Ext}^1$ ghost line

Pass 62 closed the discrete-site descent analysis with a *correction*: the global phantom
$\widehat{\mathbb Z}_S/\mathbb Z$ ($S=\mathrm{rad}(m)$, $s=|S|$) is irreducibly presheaf-level —
sheafification and cosheafification both collapse to the Löb object $L(S)=\prod_{p\in S}(\mathbb
Z_p/\mathbb Z)$ — and flagged that a true cosheaf home for the Rosser class needs the
**Zariski/cofinite** topology. Pass 63 carries this out, realizes the Pass-62 extension as a
genuine page differential, and computes the relevant $\mathrm{Ext}^1$.

### The Zariski generic-point site

Model $S$-with-its-generic-point as the finite connected space $X=\{\eta\}\cup\{(p):p\in S\}$ with
the subspace (particular-point) Zariski topology: opens are $\varnothing$ and every set containing
the generic point $\eta$. Cover by minimal opens $\mathcal U=\{U_p=\{\eta,(p)\}\}$. The decisive
contrast with the discrete site: **every nonempty intersection is $\{\eta\}$**, so the nerve of
$\mathcal U$ is the *full simplex* $\Delta^{s-1}$ (contractible), where the discrete singleton
cover had $s$ disjoint vertices.

> **Theorem 63a (Zariski relocation of the Rosser class; "$j_!$-cosheaf" form).** With
> $j:\{\eta\}\hookrightarrow X$ the open generic point and $i:Z=\{(p):p\in S\}\hookrightarrow X$ the
> closed $s$-point complement:
> 1. The constant sheaf $\underline{\mathbb Z}$ is a genuine **sheaf** (connectivity) and
>    $\check H^{\ge1}(\mathcal U,\underline{\mathbb Z})=0$ (contractible nerve). In particular the
>    discrete-site horizontal defect $\check H^0_{\mathrm{red}}=\mathbb Z^{s-1}$ **vanishes**:
>    connectivity destroys constant-coefficient $H^1$.
> 2. The skyscraper product $\mathcal F=\bigoplus_{p}(i_p)_*\mathbb Z_p$ is flasque with
>    $\check H^{\ge1}=0$ and $\mathcal F(X)=\widehat{\mathbb Z}_S$.
> 3. The extension-by-zero sequence $0\to j_!\underline{\mathbb Z}\to\underline{\mathbb Z}_X\to
>    i_*\underline{\mathbb Z}_Z\to0$ gives $0\to\mathbb Z\xrightarrow{\Delta}\mathbb Z^s\to
>    H^1(X,j_!\mathbb Z)\to0$, hence
>    $$H^1(X,\ j_!\underline{\mathbb Z})\ \cong\ \mathbb Z^s/\Delta\mathbb Z\ \cong\ \mathbb Z^{\,s-1}\ \ne\ 0.$$
>    The horizontal Rosser relations are a genuine nonzero $\check H^1$ on the connected site —
>    *supported at the generic point*. Since $j_!$ is the left-adjoint (compact-support / cosheaf)
>    extension, **"Rosser $=$ cosheaf" holds, in the precise form Rosser $=H^1$ of $j_!$**, Löb $=$
>    the stalkwise sheaf $L(S)$.

The honest reading is a *third correction*: the naive cover-cosheafification (coequalizer over
$\mathcal U$) still returns $L(S)$, because the overlaps $U_p\cap U_q=\{\eta\}$ carry the skyscraper
value $0$. What rescues the Rosser part is specifically $j_!$ — the extension by zero from the
*open* generic point — not $\check{(-)}$ over $\mathcal U$. The discrete topology flattened
$\mathbf{Sh}$ onto $\mathbf{coSh}$; the Zariski topology separates them, and the Rosser class lives
on the $j_!$ (compact-support, generization-toward-$\eta$) side.

### The unabridged $d_2$

> **Theorem 63b (unabridged $d_2$ $=$ integer-lift obstruction).** Refine the Thm-62a bicomplex by
> resolving each vertical stalk $\mathbb Z_p=\varprojlim_n\mathbb Z/p^n$ by its $\mathbb Z/p^n$
> tower. This opens a third column $E_2^{2,0}=\operatorname{coker}(\Delta:\mathbb Z\to\mathbb Z^s)
> =\mathbb Z^{s-1}$, and the Pass-62 hidden $E_\infty$-extension becomes a genuine page differential
> $$d_2:\ E_2^{0,1}=L(S)\ \longrightarrow\ E_2^{2,0}=\mathbb Z^{s-1},\qquad
> d_2\big((x_p)\big)=\big[(x_p-x_{p_0})_{p\ne p_0}\big],$$
> the **common-integer-lift obstruction** (image rank $s-1$): the local ghosts $(x_p)$ lift to a
> single global integer modulo the diagonal iff $d_2$ vanishes. The Pass-62 connecting class
> $\epsilon_S=\partial$ and this $d_2$ are *one datum in two resolutions* — a two-column $E_\infty$
> extension becomes a $d_2$ exactly when a third column is manufactured (Weibel 1994, §5.6). Neither
> presentation is primary.

### The $\mathrm{Ext}^1$ ghost line; arithmetic $\succ$ cardinal

> **Theorem 63c.** 1. From $0\to\mathbb Z\to\mathbb Z_p\to\mathbb Z_p/\mathbb Z\to0$ and
> $\mathrm{Hom}(\mathbb Z_p,\mathbb Z)=\mathrm{Hom}(\mathbb Z_p/\mathbb Z,\mathbb Z)=0$, the
> connecting map gives
> $$0\to\mathbb Z\xrightarrow{\ \delta\ }\mathrm{Ext}^1(\mathbb Z_p/\mathbb Z,\mathbb Z)\to
> \mathrm{Ext}^1(\mathbb Z_p,\mathbb Z)\to0,\qquad \delta(1)=\epsilon_p,$$
> where $\epsilon_p$ is the ghost class. $\epsilon_p$ has **infinite order** ($\delta$ injective;
> lacunary witness $u=\sum_k p^{k!}\in\mathbb Z_p$ has $n\bar u\ne0$ for every $n\ge1$, as $u$ is
> $p$-adically irrational), generating the canonical $\mathbb Z$-line but **not** the ambient group
> ($\mathrm{Ext}^1(\mathbb Z_p,\mathbb Z)$ is a continuum-dimensional $\mathbb Q$-space).
> 2. For finite $S$, $\mathrm{Ext}^1(L(S),\mathbb Z^{s-1})=\bigoplus_{p\in S}\mathrm{Ext}^1(\mathbb
> Z_p/\mathbb Z,\mathbb Z)^{s-1}$, and $\epsilon_S\ne0$ of infinite order for $s\ge2$ (component
> $\epsilon_p$ in each base-difference direction $p\ne p_0$).
> 3. **Cardinal vs arithmetic.** The target rank $s-1$ depends only on $|S|$ (cardinal), but
> $\epsilon_S$ is supported on the pairwise **non-isomorphic** ghost groups $\mathbb Z_p/\mathbb Z$
> — torsion subgroup $\bigoplus_{q\ne p}\mathbb Z(q^\infty)$, uniquely *omitting* the $p$-Prüfer —
> so $\epsilon_S$ is a genuinely **arithmetic** invariant of the prime set, not a function of $s$:
> $\epsilon_{\{2,3\}}\ne\epsilon_{\{2,5\}}$ under any prime-respecting identification.

**Reading.** Three lessons stack. (i) *Topology matters*: connectivity is not a nuisance but the
mechanism — it kills the constant-coefficient $H^1$ and relocates the Rosser relations into
$j_!$-cohomology, finally giving "Rosser $=$ cosheaf" a precise (generic-point, compact-support)
meaning. (ii) *Extension $=$ differential*: the "mixed Löb–Rosser class" is resolution-relative —
$\partial$ in the abridged bicomplex, $d_2$ in the unabridged one — never a separate phenomenon.
(iii) *Arithmetic beats cardinal*: the phantom remembers *which* primes, because the ghost groups
$\mathbb Z_p/\mathbb Z$ are pairwise non-isomorphic — the Löb–Rosser dictionary is an arithmetic,
not merely a numerical, datum over $\mathrm{Spec}\,\mathbb Z$.

**Machine verification** (`code/scripts/check-pass63.py` →
`artifacts/reports/pass63-zariski-cosheaf-unabridged-d2-ext1-check.json`, PASS, run off-mount per
[[aps-run-sync-hazard]]): *Zariski_63a* — constant-coefficient $\check H^1=0$ vs $H^1(j_!\mathbb Z)
=\operatorname{coker}\Delta$ free of rank $s-1$, no torsion (SNF), $s=2..6$. *unabridged_d2_63b* —
the obstruction map $L(S)\to\mathbb Z^{s-1}$ has image rank $s-1$ for $S=\{2,3\},\{2,3,5\},\{3,5,7\},
\{2,5,7,11\}$. *Ext1_ghost_63c* — no-retraction $p^{-n}\notin\mathbb Z$ ($p\in\{2,3,5,7,11\}$);
infinite-order ghost (lacunary $\sum p^{k!}$); ghost-group torsion signature uniquely omits the
$p$-Prüfer. Overall PASS.

**References.** C. A. Weibel, *An Introduction to Homological Algebra* (CUP 1994), §3.5
($\varprojlim^1$), §5.6 (spectral-sequence extension vs $d_2$); L. Fuchs, *Abelian Groups*
(Springer 2015), Vol. 1, Ch. 1–2 ($\mathrm{Hom}(\mathbb Z_p,\mathbb Z)=0$, structure of
$\mathbb Z_p/\mathbb Z$, $\mathrm{Ext}(\widehat{\mathbb Z}_p,\mathbb Z)$); J. Curry, *Sheaves,
Cosheaves and Applications* (PhD thesis, 2014); R. Hartshorne, *Algebraic Geometry* (Springer
1977), II.1 (extension by zero $j_!$, the recollement triangle); B. Iversen, *Cohomology of
Sheaves* (Springer 1986), Ch. II ($j_!$ and compact supports).

## Pass 64 — The recollement of the Löb–Rosser dictionary; the prime-spectrum motive

Passes 61–63 dissected the total phantom $\widehat{\mathbb Z}_S/\mathbb Z$ ($S=\mathrm{rad}(m)$,
$s=|S|$) into a *horizontal* free Rosser part $\mathbb Z^{s-1}=H^1(X,j_!\underline{\mathbb Z})$
(supported at the generic point, Thm 63a) and a *vertical* Löb part
$L(S)=\prod_{p\in S}(\mathbb Z_p/\mathbb Z)$ (per-prime $\varprojlim^1$ stalks), welded by the
common-integer-lift class $\epsilon_S$ (the Pass-62 $\partial$ $=$ Pass-63 $d_2$). Pass 64 packages
all of this as the **single canonical recollement** of constructible sheaves on the finite
generic-point model of $\mathrm{Spec}\,\mathbb Z$, so that "Löb $=i^*$, Rosser $=j_!$" is not a
slogan but the open/closed gluing triangle of the six-functor formalism, and turns the prime
dependence of $\epsilon_S$ (Thm 63c) into a functor on the squarefree divisibility lattice.

### The recollement

Let $X=X_S=\{\eta\}\sqcup Z$ be the finite (Alexandrov) space of Pass 63, $Z=\{(p):p\in S\}$ the
closed discrete $s$-point complement, $j:U=\{\eta\}\hookrightarrow X$ the open generic point,
$i:Z\hookrightarrow X$ the closed immersion. On a finite/Alexandrov space the six operations exist
on $D(X)=D(\mathrm{Sh}(X))$, with $j^*=j^!$ (open immersion), $i_*=i_!$ (closed immersion), and the
two adjoint triples and gluing triangles below.

> **Theorem 64a (Löb–Rosser recollement).** The diagram
> $$D(Z)\ \underset{\textstyle i_*=i_!}{\hookrightarrow}\ D(X)\ \underset{\textstyle j^*=j^!}{\twoheadrightarrow}\ D(U),\qquad
> j_!\dashv j^*\dashv j_*,\quad i^*\dashv i_*\dashv i^!,$$
> is a **recollement** of triangulated categories: $i_*$ is fully faithful with essential image
> $\{\,F: j^*F=0\,\}$, $j^*i_*=0$, the units/counits $j_!j^*\to\mathrm{id}\to i_*i^*$ and
> $i_*i^!\to\mathrm{id}\to j_*j^*$ are exact triangles, and $j_!,j_*$ are fully faithful. For any
> $F\in D(X)$ these two triangles are the **open/closed gluing triangles**
> $$j_!\,j^*F\ \to\ F\ \to\ i_*\,i^*F\ \xrightarrow{+1},\qquad
> i_*\,i^!F\ \to\ F\ \to\ Rj_*\,j^*F\ \xrightarrow{+1}.$$

This is the Beĭlinson–Bernstein–Deligne recollement (Astérisque 100, §1.4) specialized to a
two-stratum finite space; on Alexandrov spaces it is elementary (functors on the poset of points),
and the adjunctions were machine-checked as hom-set identities over $\mathbb F_2$
(`C_adj_jShriek_jStar_*`, `C_closed_iStar_eq_iShriek`).

### The dilation coefficient and the total phantom

The constant sheaf gives only the horizontal half. The vertical $p$-adic ghosts require a
coefficient that carries the $\times p$ dilation. Define the **dilation coefficient** $\mathcal V$
as the pro-object (tower) $(\mathcal V_n)_{n\ge1}$ in $\mathrm{Sh}(X)$ with generic value
$j^*\mathcal V_n=\underline{\mathbb Z}$, closed costalks $(i^*\mathcal V_n)_{(p)}=\mathbb Z/p^n$
(generization $\mathbb Z\twoheadrightarrow\mathbb Z/p^n$ reduction), and tower maps
$\mathcal V_{n+1}\to\mathcal V_n$ acting by $\times p$ on the $(p)$-costalk and by $\mathrm{id}$ on
the generic stalk. Equivalently, $i^*\mathcal V$ is the per-prime Milnor pro-system of
$(\mathbb Z,\times p)$, whose $R\varprojlim_n$ has $H^0=\varprojlim=0$ (the **detached** limit fixed
point) and $H^1=\varprojlim^1=\mathbb Z_p/\mathbb Z$.

> **Theorem 64b (recollement realization of the phantom; the $H^1(j_!\mathcal V)$ formula).**
> Apply the open/closed gluing triangle to $j_!\mathcal V$. Since $j^*j_!=\mathrm{id}$ and
> $i^*j_!=0$ (extension by zero), the triangle gives the long exact sequence whose only nonzero
> segment is
> $$0\ \to\ \underbrace{H^1(X,\ j_!\underline{\mathbb Z})}_{=\ \mathbb Z^{\,s-1}\ \text{(Rosser/horizontal, Thm 63a)}}\ \to\
> H^1\!\big(X,\ j_!\,R\varprojlim_n\mathcal V_n\big)\ \to\
> \underbrace{\textstyle\prod_{p\in S}\varprojlim^1(\mathbb Z,\times p)}_{=\ L(S)=\prod_p(\mathbb Z_p/\mathbb Z)\ \text{(Löb/vertical)}}\ \xrightarrow{\ \partial\ }\ 0,$$
> and the middle term is the **total phantom**
> $$\boxed{\,H^1\!\big(X,\ j_!\,\mathcal V\big)\ \cong\ \widehat{\mathbb Z}_S/\mathbb Z\,.}$$
> The connecting map $\partial$ of this recollement triangle is **literally** the Pass-63
> $d_2:(x_p)\mapsto[(x_p-x_{p_0})_{p\ne p_0}]$ of image rank $s-1$ (kernel $=$ the diagonal global
> integer $\mathbb Z$), and the extension
> $0\to\mathbb Z^{s-1}\to\widehat{\mathbb Z}_S/\mathbb Z\to L(S)\to0$ it presents is the Pass-62
> non-split $\epsilon_S\in\mathrm{Ext}^1(L(S),\mathbb Z^{s-1})$. Thus the three avatars —
> Pass-62 filtration $\partial$, Pass-63 page $d_2$, Pass-64 recollement boundary — are **one
> morphism in three guises**.

Hence the dictionary becomes a clause-by-clause reading of the six functors: **Löb $=i^*$** (the
closed-stalk / sheaf part, the genuine local ghosts $\mathbb Z_p/\mathbb Z$ that *do* descend);
**Rosser $=j_!$** (the generic-point, compact-support part, the horizontal relations $\mathbb
Z^{s-1}$ that live only with proper support toward $\eta$); and the **mixing** $\epsilon_S$ is the
boundary operator gluing $j_!j^*$ to $i_*i^*$ — the irreducible obstruction to splitting the
phantom into "pure Löb $\oplus$ pure Rosser."

### Pathologies

*(i) $s=1$ — pure Löb, no Rosser.* For a single prime $S=\{p\}$, $H^1(j_!\underline{\mathbb Z})=
\mathbb Z^{0}=0$: the horizontal Rosser stratum is empty, the recollement triangle degenerates, and
the total phantom is the bare vertical ghost $\mathbb Z_p/\mathbb Z$. **Rosser relations are a
*relational* phenomenon — they need at least two primes to relate.** A one-prime world is purely
Löbian: every consistency ghost descends, no detached cross-prime comparison survives.

*(ii) Incomparable strata.* For $S=\{2,3\}$ and $S'=\{2,5\}$ (rad-incomparable, Cor 60c) neither
$X_S$ nor $X_{S'}$ is open in the other; the only common open sub-stratum is $X_{\{2\}}$, carrying
the shared $2$-adic ghost $\mathbb Z_2/\mathbb Z$. The classes differ, $\epsilon_{\{2,3\}}\ne
\epsilon_{\{2,5\}}$, although $|S|=|S'|$: the recollement remembers *which* primes (Thm 63c).

*(iii) The whole spectrum — the adelic punchline.* Let $S=\mathbb P$ be **all** primes, so
$X=\mathrm{Spec}\,\mathbb Z$ honestly (every closed point plus the generic point). Then
$$H^1\!\big(\mathrm{Spec}\,\mathbb Z,\ j_!\,\mathcal V\big)\ \cong\ \widehat{\mathbb Z}/\mathbb Z\ =\
\Big(\textstyle\prod_p\mathbb Z_p\Big)\big/\mathbb Z\ =\ \mathbb A_{\mathbb Q,\mathrm{fin}}^{\mathrm{int}}/\mathbb Z,$$
the **integral finite-adele class group**: the Löb–Rosser phantom of *all* of arithmetic is the
solenoidal object $\widehat{\mathbb Z}/\mathbb Z$, the same group that appears as the character
group of the adelic solenoid and as $\varprojlim^1$ of $\mathbb Z\xleftarrow{n!}\cdots$. A Smullyan
gloss: *the ghost haunting every consistency statement at once is precisely an adele that is not an
integer.*

### The prime-spectrum motive

> **Theorem 64c (the Löb–Rosser motive).** For $S\subseteq S'$ the inclusion realizes $X_S$ as an
> **open** subspace of $X_{S'}$ (complement $\{(p):p\in S'\setminus S\}$ is closed), giving an open
> immersion $\iota_{S,S'}:X_S\hookrightarrow X_{S'}$ and a restriction $\iota^*$ on the
> recollement data. The assignment
> $$M:\ (\mathcal P_{\mathrm{fin}}(\mathbb P),\subseteq)\ \longrightarrow\ D^b(\mathbb Z),\qquad
> S\ \longmapsto\ j_!\,\mathcal V_S\quad(\text{equivalently }S\mapsto\epsilon_S\in\mathrm{Ext}^1(L(S),\mathbb Z^{s-1}))$$
> is a **functor** on the squarefree divisibility lattice: $\iota^*$ sends the horizontal stratum
> $\mathbb Z^{s'-1}\twoheadrightarrow\mathbb Z^{s-1}$ (forget the primes in $S'\setminus S$) and the
> vertical $L(S')\twoheadrightarrow L(S)$ compatibly with $\epsilon$, so $\epsilon$ is a natural
> transformation $\mathrm{Ros}_{(-)}\Rightarrow\varprojlim^1(-)$ (extending the Pass-58/60 $\Theta$
> from the dilation tower to the full recollement). $M$ is genuinely **arithmetic** (Thm 63c): it is
> *not* a function of the cardinal $s$ — incomparable equicardinal $S,S'$ have non-isomorphic, and
> on overlaps unequal, classes.

We call $M$ the **motive of the Löb–Rosser dictionary over $\mathrm{Spec}\,\mathbb Z$** by analogy:
like a (mixed) motive it is a functorial, $\mathrm{Ext}^1$-valued, weight-filtered ($W_0=$ Löb
local part, $\mathrm{gr}^W_1=$ Rosser horizontal part) constructible-sheaf datum on the arithmetic
base, glued by a recollement. The analogy is deliberately *non-literal*: $M$ is an honest object of
constructible sheaves / $D^b(\mathbb Z)$ on the finite Spec-$\mathbb Z$ model, a perverse-type
gluing, not a Voevodsky motive — but it occupies the same structural niche (functor on a geometric
base, with a weight filtration whose graded pieces are the dictionary's two columns).

**Reading.** The six-functor packaging is the *terminus* of the Pass 50–63 homological programme:
every earlier invariant is now a clause of one recollement. The phantom Betti number (Pass 50) is
$\dim H^1(j_!\mathcal V)$; the deflated bracket $e=|F^\tau|$ (Pass 51) and the flipped $\Phi$ (Pass
52) are the constant-coefficient shadow $H^*(j_!\underline{\mathbb Z})$; the $2$-adic phantom
(Pass 53–56) is the vertical $i^*$-stalk $\varprojlim^1$; the rad-graded naturality (Pass 58–60) is
the functoriality of $M$; the descent corrections (Pass 61–63) are the identification of the two
strata. *Löb is what descends; Rosser is what only has compact support toward the generic point;
the dictionary is their gluing triangle.*

**Machine verification** (`code/scripts/check-pass64.py` →
`artifacts/reports/pass64-recollement-six-functor-motive-check.json`, PASS, run off-mount in
`/tmp` per [[aps-run-sync-hazard]]): *A_horizontal* — $H^1(j_!\underline{\mathbb Z})=\mathbb
Z^{s-1}$ by $\operatorname{coker}\Delta$ SNF, $s=1..6$; *A_vertical* — $\ker(1-p\,\mathrm{sh})=0$
(detached $\varprojlim=0$) and image index $p^n\uparrow$ (non-ML, $\varprojlim^1=\mathbb Z_p/\mathbb
Z$) for $p\in\{2,3,5\}$; *B_connecting* — recollement boundary $d$ image rank $s-1$, kernel the
diagonal $\mathbb Z$, $s=1..6$; *C_adjunctions* — $|\mathrm{Hom}(j_!L,F)|=|\mathrm{Hom}(L,j^*F)|$
over $\mathbb F_2$, closed $i_*=i_!$; *D_s1* — pure-Löb degeneration $H^1(j_!\mathbb Z)=0$;
*E_motive* — open-immersion chain $\{2\}\subset\{2,3\}\subset\{2,3,5\}$ with surjective restriction,
incomparable $\{2,3\}/\{2,5\}$ no-arrow, arithmetic$\ne$cardinal; *F* — full-spectrum adelic
punchline $\widehat{\mathbb Z}/\mathbb Z$. Overall PASS.

**References.** A. A. Beĭlinson, J. Bernstein, P. Deligne, *Faisceaux pervers*, Astérisque **100**
(1982), §1.4 (recollement $(j_!,j^*,j_*)\dashv(i^*,i_*,i^!)$, gluing of $t$-structures);
M. Kashiwara & P. Schapira, *Sheaves on Manifolds* (Springer 1990), §2.6, §3.1 (six operations,
open/closed decomposition, $j_!$ and proper supports); B. Iversen, *Cohomology of Sheaves*
(Springer 1986), Ch. II–III ($j_!$, $i^!$, the two gluing triangles); J. Curry, *Sheaves, Cosheaves
and Applications* (PhD thesis, 2014) (the cosheaf side of $j_!$); C. A. Weibel, *An Introduction to
Homological Algebra* (CUP 1994), §3.5, §5.6 ($\varprojlim^1$, extension-vs-$d_2$); for the adelic
$\widehat{\mathbb Z}/\mathbb Z$ as a solenoid/character object, D. Ramakrishnan & R. Valenza,
*Fourier Analysis on Number Fields* (Springer 1999), Ch. 5.

## Pass 65 - Verdier-dual recollement and the signed functional equation

Pass 64 packaged the Loeb-Rosser dictionary into the first open/closed gluing triangle
$j_!j^*\to\mathrm{id}\to i_*i^*\xrightarrow{+1}$. Pass 65 uses the second triangle
$$i_*i^!\to\mathrm{id}\to Rj_*j^*\xrightarrow{+1}$$
on the same finite generic-point model $X_S=\{\eta\}\sqcup\{(p):p\in S\}$. The outcome is a finite
Verdier-dual "functional equation": the mixed class is not fixed by duality; it is sent to the
negative transpose.

### The $i^!$ spine

Let $s=|S|$ and write the generic-to-closed diagonal as
$$\Delta:\mathbb Z\longrightarrow\mathbb Z^S,\qquad 1\longmapsto(1,\ldots,1).$$
The local-support / costalk spine of the second triangle is the two-term complex
$\mathbb Z\xrightarrow{\Delta}\mathbb Z^S$. Hence
$$H^0(i^!)=\ker\Delta=0,\qquad
H^1(i^!)=\operatorname{coker}\Delta\cong\mathbb Z^{s-1}.$$
Thus the horizontal Rosser lattice has two equivalent finite presentations:
$H^1(X,j_!\underline{\mathbb Z})$ from Pass 63 and $H^1(i^!)$ from the second recollement triangle.
This is the precise finite sense in which the second triangle recovers the Rosser side from closed
support.

### Signed Verdier functional equation

The Pass 62--64 boundary is
$$d_S:\mathbb Z^S\longrightarrow\mathbb Z^{s-1},\qquad
(x_p)_{p\in S}\longmapsto(x_p-x_{p_0})_{p\ne p_0}.$$
Contravariant Verdier duality exchanges the two open/closed presentations:
$$\mathbb D(j_!A)\simeq Rj_*\mathbb D(A),\qquad
\mathbb D(i_*B)\simeq i_*\mathbb D(B),$$
and reverses the connecting morphism. On the finite matrix spine this is the signed transpose
$$\mathbb D(d_S)=-d_S^T.$$

> **Theorem 65a (closed-support Rosser lattice).** On $X_S$, the $i^!$ spine has
> $H^0=0$ and $H^1\cong\mathbb Z^{s-1}$.
>
> **Theorem 65b (finite Verdier functional equation).** If $\epsilon_S$ is represented by
> $d_S$, then finite Verdier duality gives
> $$\mathbb D(\epsilon_S)=-\epsilon_S^\vee.$$
> Moreover $\mathbb D^2(d_S)=d_S$. The sign disappears over $\mathbb F_2$ but is visible over
> $\mathbb Z$ as the orientation of the gluing triangle.
>
> **Theorem 65c (finite-prime naturality).** For $S\subseteq S'$, restriction commutes with
> $d_S$ and, after duality, with $-d_S^T$. The signed functional equation is therefore compatible
> with the finite prime-spectrum motive of Pass 64.

**Machine verification** (`code/scripts/check-pass65.py` ->
`artifacts/reports/pass65-verdier-dual-recollement-functional-equation-check.json`, PASS): for
$s=1,\ldots,7$, $\ker\Delta=0$ and $\operatorname{coker}\Delta$ has rank $s-1$; $d_S$ and $-d_S^T$
have equal rank; $\mathbb D^2(d_S)=d_S$; the sign is invisible modulo $2$; and the restriction
squares commute for the finite inclusions $1\subset2$, $2\subset3$, $3\subset5$, $4\subset7$.

**Limit of the pass.** This is a finite/Alexandrov computation. A full scheme statement still
requires choosing the dualizing normalization on the actual arithmetic site, computing the duals of
$\mathbb Z_p/\mathbb Z$ and $\widehat{\mathbb Z}_S/\mathbb Z$, and controlling products versus sums.
So Pass 65 closes the finite sign question but leaves the honest $\mathrm{Spec}\,\mathbb Z$
Verdier-duality lift open.

## Pass 66 - Duality normalization and the product/direct-sum obstruction

Pass 65 left one ambiguity: which duality is meant when the finite signed equation is lifted toward
the arithmetic site?  Pass 66 separates three candidates.

### Plain $\mathbb Z$-linear duality is shifted

For a finite cyclic layer $\mathbb Z/n$, the unshifted dual is trivial:
$$\operatorname{Hom}_{\mathbb Z}(\mathbb Z/n,\mathbb Z)=0.$$
The layer reappears one degree later:
$$\operatorname{Ext}^1_{\mathbb Z}(\mathbb Z/n,\mathbb Z)\cong\mathbb Z/n.$$
Thus $R\mathrm{Hom}_{\mathbb Z}(-,\mathbb Z)$ is not wrong, but it is not the degree-preserving
duality behind the Pass-65 matrix equation.  It forces a cohomological shift before the local
dilation layers are visible.

### Character-normalized finite lift

Use character duality
$$D_{\mathrm{ch}}(A)=\operatorname{Hom}(A,\mathbb Q/\mathbb Z).$$
Then
$$D_{\mathrm{ch}}(\mathbb Z/n)\cong\mathbb Z/n,$$
so the finite layers of the dilation tower are preserved.  For finite $S$, products and direct
sums agree, so there is no support ambiguity.  The Pass-65 boundary
$$d_S:\mathbb Z^S\to\mathbb Z^{s-1}$$
is sent to the signed transpose $-d_S^T$, giving:

> **Theorem 66a (plain $R\mathrm{Hom}_{\mathbb Z}$ is shifted).** The local finite cyclic layers are
> killed by $\operatorname{Hom}_{\mathbb Z}(-,\mathbb Z)$ and recovered by
> $\operatorname{Ext}^1_{\mathbb Z}(-,\mathbb Z)$, so the unshifted $\mathbb Z$-dual is not the
> degree-preserving Loeb-Rosser duality.
>
> **Theorem 66b (finite-$S$ character-dual lift).** For every finite prime set $S$,
> character-normalized Verdier duality supports the equation
> $$D_{\mathrm{ch}}(\epsilon_S)=-\epsilon_S^\vee.$$
>
> **Theorem 66c (all-prime obstruction).** For $S=\mathbb P$, the bare infinite product does not
> self-dualize: continuous characters of a product have finite support, so the dual is a direct
> sum of local characters.  The all-prime statement requires a restricted-product / locally compact
> abelian normalization.

**Machine verification** (`code/scripts/check-pass66.py` ->
`artifacts/reports/pass66-duality-normalization-scheme-lift-check.json`, PASS): finite cyclic
layers $n=2,3,4,5,8,9,16,25$ have trivial $\operatorname{Hom}(-,\mathbb Z)$ but
$\operatorname{Ext}^1$ of order $n$; $D_{\mathrm{ch}}(\mathbb Z/p^k)$ has order $p^k$ for
$p=2,3,5,7$, $k=1,\ldots,4$; $d_S$ and $-d_S^T$ have matching rank and duality squared returns
$d_S$ for $s=1,\ldots,7$; finite product/direct-sum orders agree; finite-prefix support counts
exhibit the infinite product/direct-sum gap.

**Reading.** Finite $S$ is now stable: use character-normalized duality and the Pass-65 sign
survives.  The full spectrum is not a formal limit of those finite statements in the category of
bare groups.  It must be stated in a topological category of restricted products, the natural home
of finite adeles.

## Pass 67 - Restricted-product finite shadows and the derived quotient gap

Pass 66 showed that the all-prime duality cannot be a bare product statement. Pass 67 moves to the
finite conductor windows of the restricted product
$$\mathbb A_f=\prod_p'(\mathbb Q_p,\mathbb Z_p).$$
This proves the finite local self-duality needed by the restricted-product formulation, but also
shows that the Loeb-Rosser phantom $\widehat{\mathbb Z}/\mathbb Z$ is not an ordinary finite-stage
quotient.

### Finite conductor windows

At prime $p$ and conductor $k\ge1$, use
$$p^{-k}\mathbb Z_p/p^k\mathbb Z_p\cong\mathbb Z/p^{2k}\mathbb Z$$
with pairing
$$\langle x,y\rangle=\frac{xy}{p^{2k}}\in\mathbb Q/\mathbb Z.$$
The integral lattice $\mathbb Z_p/p^k\mathbb Z_p$ corresponds to
$p^k\mathbb Z/p^{2k}\mathbb Z$ and is self-annihilating. Finite products of these conductor
windows remain self-dual, with product integral lattice self-annihilating. In coordinates
normalized by this conductor pairing, the Pass-65 boundary still dualizes by signed transpose:
$$D(d_S)=-d_S^T,\qquad D^2(d_S)=d_S.$$

> **Theorem 67a (finite conductor self-duality).** The finite conductor group
> $p^{-k}\mathbb Z_p/p^k\mathbb Z_p$ is self-dual, and its integral lattice
> $\mathbb Z_p/p^k\mathbb Z_p$ is self-annihilating.
>
> **Theorem 67b (restricted-product finite shadow).** Finite products of these local conductor
> windows retain self-duality and the Pass-65 signed boundary equation.
>
> **Theorem 67c (CRT collapse).** For every finite conductor
> $N=\prod p^{e_p}$, the diagonal map
> $$\mathbb Z/N\mathbb Z\longrightarrow\prod_{p\mid N}\mathbb Z/p^{e_p}\mathbb Z$$
> is surjective. Hence the quotient by the diagonal is zero at every fixed finite conductor.

**Machine verification** (`code/scripts/check-pass67.py` ->
`artifacts/reports/pass67-restricted-product-adelic-duality-check.json`, PASS): local quotients
$\mathbb Z/4,\mathbb Z/16,\mathbb Z/9,\mathbb Z/81,\mathbb Z/25,\mathbb Z/49$ have nondegenerate
pairings and self-annihilating integral lattices; product windows of orders $36,144,900,4900$ have
self-annihilating product lattices; signed boundary transpose checks pass for $s=1,\ldots,7$; CRT
diagonal maps for $N=6,12,90,420$ are surjective.

**Reading.** Restricted-product duality fixes the product/direct-sum problem at the level of
finite conductor windows. It does not by itself produce the phantom quotient
$\widehat{\mathbb Z}/\mathbb Z$: fixed finite levels see zero by CRT, while the profinite topology
makes $\mathbb Z$ dense in $\widehat{\mathbb Z}$. The Loeb-Rosser phantom is therefore a
derived/pro quotient phenomenon. Pass 68 should identify the exact category, pro-category, or
condensed/solid setting in which the levelwise-zero CRT quotients assemble into the nonzero
extension class.

## Pass 68 - The derived pro-cokernel of the diagonal

Pass 67 showed that fixed finite conductor quotients cannot see the all-prime phantom: CRT kills
the finite quotient by the diagonal.  Pass 68 identifies the missing functor.  The phantom appears
as an $R^1\varprojlim$ of the kernel tower.

Let
$$N_n=\operatorname{lcm}(1,\ldots,n).$$
The tower $\{N_n\}$ is cofinal among positive integer moduli under divisibility.  At level $n$,
there is a short exact sequence
$$0\to K_n=N_n\mathbb Z\to\mathbb Z\to\mathbb Z/N_n\mathbb Z\to0.$$
The final map is levelwise surjective; equivalently, after prime-power factorization, CRT gives
$$\mathbb Z/N_n\mathbb Z\cong\prod_{p\mid N_n}\mathbb Z/p^{v_p(N_n)}\mathbb Z.$$
Thus the finite cokernel is zero at every fixed level.

However, the kernel tower $K_n=N_n\mathbb Z$ is not Mittag-Leffler.  Its transition maps are
inclusions $N_{n+1}\mathbb Z\subseteq N_n\mathbb Z$, equivalently multiplication by
$N_{n+1}/N_n$ after identifying each $K_n$ with $\mathbb Z$.  These image indices are unbounded,
and
$$\varprojlim_n K_n=\bigcap_n N_n\mathbb Z=0.$$
Applying $\varprojlim$ to the levelwise short exact sequence gives
$$0\to\mathbb Z\to\varprojlim_n\mathbb Z/N_n\mathbb Z\to
\varprojlim\nolimits^1 K_n\to0.$$
Since $\varprojlim_n\mathbb Z/N_n\mathbb Z=\widehat{\mathbb Z}$, this yields
$$\boxed{\ \varprojlim\nolimits^1(N_n\mathbb Z)\cong\widehat{\mathbb Z}/\mathbb Z\ }.$$

> **Theorem 68a (levelwise CRT zero).** The diagonal quotient is zero at every fixed finite
> conductor $N_n$.
>
> **Theorem 68b (derived pro-cokernel).** The all-prime Loeb-Rosser phantom is
> $\varprojlim^1(N_n\mathbb Z)$ for the cofinal lcm tower.  Equivalently, it is the derived
> cokernel of $\mathbb Z\to\{\mathbb Z/N_n\}_n$ in pro-abelian bookkeeping.
>
> **Theorem 68c (topology vs exactness).** The algebraic phantom is not an ordinary Hausdorff LCA
> quotient: $\mathbb Z$ is dense in $\widehat{\mathbb Z}$.  The derived pro-Ab category retains the
> extension data that Hausdorff quotienting would collapse.

**Machine verification** (`code/scripts/check-pass68.py` ->
`artifacts/reports/pass68-derived-pro-cokernel-phantom-check.json`, PASS): $N_n$ is cofinal for
moduli $1,\ldots,24$; CRT levelwise-zero checks pass for $N_2,N_3,N_4,N_5,N_6,N_8,N_{10},N_{12}$;
the kernel tower has 14 distinct values through $n=24$, unbounded image indices in $K_2$, and many
nontrivial transition ratios; $\varprojlim K_n=0$ is certified by unbounded $N_n$; completion
prefixes grow while the finite cokernel remains zero.

**Reading.** The all-prime object is now located algebraically: it is a derived pro-cokernel.
Restricted products handle local duality; $R^1\varprojlim$ handles the global diagonal phantom.
The next missing comparison is not "where does $\widehat{\mathbb Z}/\mathbb Z$ live?" but "is this
$R^1\varprojlim$ class the same morphism as the Pass-62/63/64 recollement $\epsilon$, with the
same signed Verdier duality?"

## Pass 70 - The derived pro-cokernel filtration is the recollement class

Pass 68 located the all-prime phantom as a derived pro-cokernel.  Pass 70 compares that object with
the Pass-62/63/64 recollement class.

For a finite prime set $S$, let
$$M_{S,k}=\prod_{p\in S}p^k.$$
Then
$$0\to M_{S,k}\mathbb Z\to\mathbb Z\to\mathbb Z/M_{S,k}\mathbb Z\to0$$
is the finite-prime version of the lcm-tower exact sequence, and
$$\varprojlim_k \mathbb Z/M_{S,k}\mathbb Z=\widehat{\mathbb Z}_S=\prod_{p\in S}\mathbb Z_p.$$
Since $\bigcap_k M_{S,k}\mathbb Z=0$, the derived exact sequence gives
$$\varprojlim\nolimits^1(M_{S,k}\mathbb Z)\cong\widehat{\mathbb Z}_S/\mathbb Z.$$

The map from the global derived pro-cokernel to the product of local derived cokernels is
$$\widehat{\mathbb Z}_S/\mathbb Z\longrightarrow
\prod_{p\in S}(\mathbb Z_p/\mathbb Z).$$
Its kernel consists of tuples represented by ordinary integers in each coordinate, modulo the
single diagonal integer.  Hence
$$\ker=\mathbb Z^S/\Delta\mathbb Z\cong\mathbb Z^{|S|-1}.$$
This gives exactly the Pass-62 filtration extension and the Pass-64 recollement boundary:
$$0\to\mathbb Z^S/\Delta\mathbb Z\to
\widehat{\mathbb Z}_S/\mathbb Z\to
\prod_{p\in S}(\mathbb Z_p/\mathbb Z)\to0.$$

> **Theorem 70a (finite-prime comparison).** For finite $S$, the derived pro-cokernel
> $\varprojlim^1(M_{S,k}\mathbb Z)$ is the middle term of the Loeb-Rosser recollement extension.
> The projection to local derived cokernels has kernel $\mathbb Z^S/\Delta\mathbb Z$, so the
> extension class is $\epsilon_S$.
>
> **Theorem 70b (cofinal all-prime compatibility).** The all-prime lcm tower restricts to the
> finite-prime towers above.  Thus $\widehat{\mathbb Z}/\mathbb Z$ is the compatible all-prime
> derived pro-cokernel whose finite-prime restrictions are the classes $\epsilon_S$.
>
> **Theorem 70c (finite signed shadow).** With
> $$d_S(x)=(x_p-x_{p_0})_{p\ne p_0},$$
> finite character-normalized duality sends the boundary to $-d_S^T$ and
> $D^2(d_S)=d_S$.  Therefore every finite-prime shadow satisfies
> $$D_{\mathrm{ch}}(\epsilon_S)=-\epsilon_S^\vee.$$

**Machine verification** (`code/scripts/check-pass70.py` ->
`artifacts/reports/pass70-derived-pro-epsilon-comparison-check.json`, PASS): for
$|S|=1,\ldots,5$, the CRT shadows for $M_{S,k}$, $1\le k\le4$, are bijective; the diagonal
matrix $\Delta:\mathbb Z\to\mathbb Z^S$ is primitive; the boundary
$d_S:\mathbb Z^S\to\mathbb Z^{|S|-1}$ is surjective with kernel the diagonal by rank; and
$-d_S^T$ double-dualizes back to $d_S$.

**Limit of the pass.** This closes the algebraic comparison between the derived pro-cokernel and
the recollement $\epsilon_S$.  It does not by itself prove the honest all-prime restricted-product
Verdier/Pontryagin functional equation; that remains a topological duality normalization problem.

## Pass 71 - Pro-restricted all-prime epsilon duality

Pass 70 identified the finite-prime derived pro-cokernel with the recollement class
$\epsilon_S$.  Pass 71 fixes the correct status of the all-prime signed statement:
it is not a theorem about the ordinary Pontryagin dual of the bare quotient
$\widehat{\mathbb Z}/\mathbb Z$.  Since $\mathbb Z$ is dense in
$\widehat{\mathbb Z}$, the ordinary topological quotient is not a Hausdorff LCA
object, and ordinary continuous characters of an infinite product see only
finite-support data.  The all-prime statement therefore has to live in a
restricted-product/pro-object presentation.

The proposed object is
$$\epsilon_{\mathbb P}=\{\epsilon_S\}_{S\subset\mathbb P,\ |S|<\infty}$$
together with the derived pro-cokernel
$$\varprojlim\nolimits^1(N_n\mathbb Z)\cong\widehat{\mathbb Z}/\mathbb Z.$$
Its topology and duality normalization are carried by finite conductor windows
$$p^{-k}\mathbb Z_p/p^k\mathbb Z_p$$
with self-annihilating integral lattices
$$\mathbb Z_p/p^k\mathbb Z_p.$$
The signed functional equation is then stated as a compatible finite-shadow law:
for every finite $S$ and every conductor window, the boundary
$$d_S(x)=(x_p-x_{p_0})_{p\ne p_0}$$
dualizes to $-d_S^T$, and these equations commute with finite-prime restrictions.

> **Theorem 71a (support-preserving criterion).** Any all-prime duality theorem for
> $\epsilon_{\mathbb P}$ must be formulated in a support-preserving category:
> restricted products with conductor/lattice data, or an equivalent exact
> pro/condensed/solid formalism.  The bare product duality is not admissible
> because it replaces all-prime product support by finite-support characters.
>
> **Theorem 71b (pro-restricted epsilon object).** The all-prime Loeb-Rosser
> class is the compatible finite-prime family $\{\epsilon_S\}_S$ plus the
> derived pro-Ab quotient $\widehat{\mathbb Z}/\mathbb Z$.  The finite shadows
> are the Pass-70 extensions
> $$0\to\mathbb Z^S/\Delta\mathbb Z\to
> \widehat{\mathbb Z}_S/\mathbb Z\to
> \prod_{p\in S}(\mathbb Z_p/\mathbb Z)\to0.$$
>
> **Theorem 71c (global signed law as finite-shadow theorem).** The expression
> $$D_{\mathrm{res}}(\epsilon_{\mathbb P})=-\epsilon_{\mathbb P}^{\vee}$$
> means that every finite-prime/conductor shadow satisfies
> $D(d_S)=-d_S^T$, duality squared returns $d_S$, and all restriction squares
> commute.  This is a precise pro-restricted formulation, not yet a completed
> LCA-sheaf or condensed proof.

**Machine verification** (`code/scripts/check-pass71.py` ->
`artifacts/reports/pass71-restricted-product-epsilon-duality-check.json`, PASS): finite boundary
matrices and signed transposes commute with prefix restrictions through six primes; conductor
windows for $p=2,3,5,7$ and $k=1,2$ have self-annihilating integral lattices; finite-prefix support
counts separate restricted-product product profiles from bounded finite-support dual profiles.

**Limit of the pass.** Pass 71 gives a disciplined all-prime formulation and a finite-shadow test
suite.  The remaining task is to choose and prove the ambient exact category: LCA sheaves over
finite adeles, condensed/solid abelian groups, or an explicit hybrid exact category combining
restricted products with derived pro-Ab quotients.

## Pass 72 - The hybrid epsilon exact category candidate

Pass 72 chooses the constrained route left open by Pass 71: define a small
hybrid bookkeeping category before trying to identify it with an established
LCA-sheaf or condensed category.  Call it $\mathcal H_\epsilon$.

An object of $\mathcal H_\epsilon$ has two synchronized layers:

1. finite restricted-product shadows
   $$(S,k,W_{S,k},L_{S,k},d_S),$$
   where
   $$W_{S,k}=\prod_{p\in S}(p^{-k}\mathbb Z_p/p^k\mathbb Z_p),\qquad
   L_{S,k}=\prod_{p\in S}(\mathbb Z_p/p^k\mathbb Z_p),$$
   and $d_S:\mathbb Z^S\to\mathbb Z^{|S|-1}$ is the Loeb-Rosser boundary;
2. the derived pro-Ab diagonal layer
   $$K_n=N_n\mathbb Z,\qquad N_n=\operatorname{lcm}(1,\ldots,n).$$

A sequence is **hybrid-exact** if all finite restricted-product shadows are
exact and the pro layer supplies the derived diagonal quotient
$$\varprojlim\nolimits^1K_n\cong\widehat{\mathbb Z}/\mathbb Z.$$
The finite layer keeps conductor and support; the pro layer keeps the phantom
that every fixed CRT quotient kills.  The candidate duality is
$$\mathbb D_{\mathcal H}(d_S)=-d_S^T,$$
with $\widehat{\mathbb Z}/\mathbb Z$ retained as a derived pro-Ab quotient, not
as an ordinary Hausdorff LCA quotient.

> **Definition 72a (hybrid-exact sequence).** A diagram in $\mathcal H_\epsilon$
> is hybrid-exact when its finite conductor shadows are exact after every
> finite restriction and the lcm kernel tower is interpreted through
> $R^1\varprojlim$.
>
> **Theorem 72b (finite exactness of $\epsilon_{\mathbb P}$ in
> $\mathcal H_\epsilon$).** The finite shadows of $\epsilon_{\mathbb P}$ are
> exact: $d_S$ is surjective, has diagonal kernel, and the signed dual
> $-d_S^T$ has primitive image.  Restriction maps compose and commute with the
> signed dual.
>
> **Theorem 72c (pro layer is not optional).** The finite CRT shadows remain
> levelwise zero, while the lcm kernel tower is non-Mittag-Leffler and gives
> $\varprojlim^1(N_n\mathbb Z)\cong\widehat{\mathbb Z}/\mathbb Z$.  Hence any
> exact category forgetting the pro layer loses the Loeb-Rosser phantom.

**Machine verification** (`code/scripts/check-pass72.py` ->
`artifacts/reports/pass72-hybrid-exact-epsilon-category-check.json`, PASS): exact shadows pass for
$|S|=1,\ldots,6$; restriction composition and signed-dual restriction pass for all chains
$S_r\subseteq S_s\subseteq S_t$ among the first six primes; conductor layers pass through
$k=1,2,3$; the lcm tower is cofinal for moduli up to $24$, has non-ML growth, and certifies the
finite-CRT-zero/pro-derived-nonzero split.

**Limit of the pass.** $\mathcal H_\epsilon$ is now a precise finite/pro bookkeeping candidate.
The remaining issue is external validation: prove a universal property for it, or embed it into an
established category such as LCA sheaves, condensed/solid abelian groups, or an exact pro-category
with restricted-product generators.

## Pass 73 - Presentation-level universal property of $\mathcal H_\epsilon$

Pass 73 proves the universal property available at the current level of
precision: $\mathcal H_\epsilon$ is initial among support-preserving certificate
targets.  A certificate target is not yet an ambient analytic category; it is a
target carrying images of the five generator families needed to type
$\epsilon_{\mathbb P}$:

1. finite conductor windows $W_{S,k}$ and lattices $L_{S,k}$;
2. Loeb-Rosser boundaries $d_S$;
3. finite-prime restriction maps;
4. signed duality maps $d_S\mapsto -d_S^T$;
5. the derived pro-Ab lcm tower $K_n=N_n\mathbb Z$.

An admissible certificate target is one where these images satisfy the
relations checked in Pass 72: finite exactness, restriction composition,
signed-dual compatibility, conductor bookkeeping, and non-Mittag-Leffler pro
growth.  Since $\mathcal H_\epsilon$ was defined by exactly these generators
and relations, any admissible target receives a unique generator-preserving
functor from $\mathcal H_\epsilon$.

> **Definition 73a (support-preserving certificate target).** A target $C$ is
> support-preserving for $\epsilon_{\mathbb P}$ if it supplies images of the
> five generator families above and satisfies the finite/pro relations.
>
> **Theorem 73b (presentation initiality).** $\mathcal H_\epsilon$ is initial
> among admissible support-preserving certificate targets: every such target
> receives a unique generator-preserving functor
> $\mathcal H_\epsilon\to C$.
>
> **Theorem 73c (minimality obstruction).** If any one of the five generator
> families is omitted, the target no longer certifies $\epsilon_{\mathbb P}$:
> omitting windows loses local support; omitting $d_S$ loses $\epsilon_S$;
> omitting restrictions loses assembly; omitting signed duality loses the
> functional equation; omitting the lcm tower loses
> $\widehat{\mathbb Z}/\mathbb Z$.

**Machine verification** (`code/scripts/check-pass73.py` ->
`artifacts/reports/pass73-h-epsilon-universal-property-check.json`, PASS): finite normal forms are
generated for conductor shadows through six primes and $k\le3$; pro normal forms are generated
through $N_{24}$; restriction and signed-dual relations commute; the lcm tower remains cofinal and
non-ML; admissible certificate targets receive a unique generator-preserving functor; and targets
omitting any generator family record the expected obstruction.

**Limit of the pass.** The universal property is now proved for the presented certificate
category.  The next problem is not more finite bookkeeping; it is external realization: construct a
faithful exact functor from $\mathcal H_\epsilon$ into an established analytic/categorical target,
or prove why no such faithful realization can preserve all five generator families.

## Pass 74 - Tagged restricted pro-Ab realization test

Pass 74 performs the first external realization test.  The target is not yet an
LCA-sheaf or condensed category; it is the concrete tagged restricted pro-Ab
certificate category
$$\mathcal R_\epsilon
=\mathbf{Pro}^{\mathrm{rp}}_{\mathrm{tag}}(\mathbf{Ab}_{\mathrm{fin}})
\times\mathbf{Pro}_{\mathrm{tag}}(\mathbf{Ab}).$$
The realization functor
$$\rho_{\mathrm{tag}}:\mathcal H_\epsilon\to\mathcal R_\epsilon$$
sends:

1. $(S,k,W_{S,k},L_{S,k})$ to finite abelian group data with support tag $S$,
   conductor tag $k$, and elementary/lattice divisor data;
2. $d_S$ to its tagged integer matrix;
3. each restriction $S\subseteq S'$ to a tagged coordinate-restriction matrix;
4. signed duality to the tagged matrix $-d_S^T$;
5. $K_n=N_n\mathbb Z$ to the tagged pro-stage $(n,N_n)$.

> **Theorem 74a (tagged generator faithfulness).** On the checked finite
> window, $\rho_{\mathrm{tag}}$ is faithful on all five generator families:
> no two tagged generator signatures collide.
>
> **Theorem 74b (tag-forgetting obstruction).** The same realization is not
> faithful after forgetting source/support/stage tags.  Restriction maps with
> different source support but the same visible target matrix collide, and lcm
> stages with repeated $N_n$ collide.  Therefore a plain untagged pro-Ab target
> cannot be the desired faithful realization.
>
> **Corollary 74c (next exact target constraint).** Any natural LCA-sheaf,
> condensed/solid, or exact pro-category realization must internalize the
> support and stage tags as mathematical structure, rather than discard them as
> bookkeeping.

**Machine verification** (`code/scripts/check-pass74.py` ->
`artifacts/reports/pass74-tagged-proab-realization-check.json`, PASS): 75 generators are tested
through six primes, $k\le3$, and $N_{24}$; tagged global injectivity has zero collisions; tagged
family faithfulness passes for finite conductor windows, boundaries, restrictions, signed duality,
and the lcm tower; the plain untagged comparison has collisions, including restriction-source
collisions and repeated lcm-stage collisions.

**Limit of the pass.** The first concrete realization succeeds only with tags.  The remaining
problem is to make those tags intrinsic: either construct them as support/stage structure in an
established exact target, or prove a no-go theorem for tag-free faithful realization.

## Pass 75 - Intrinsic support and stage projectors

Pass 75 replaces the explicit support/stage tags from Pass 74 by internal
projector structure.  The new target
$$\mathcal R_\epsilon^{\mathrm{proj}}$$
is still a certificate target, but the formerly external labels are encoded by
endomorphisms:

1. Boolean support idempotents $e_p$ with
   $$e_Se_T=e_{S\cap T};$$
2. lcm-stage projectors $q_n$ with
   $$q_nq_m=q_{\min(n,m)}.$$

The realization
$$\rho_{\mathrm{proj}}:\mathcal H_\epsilon\to\mathcal R_\epsilon^{\mathrm{proj}}$$
sends finite windows, boundaries, restrictions, signed duals, and pro stages to
finite/pro abelian data equipped with these projector actions.  Restriction
source support is recovered from the pair $(e_{S'},e_S)$ rather than from a
textual source tag; repeated lcm stages are separated by $q_n$ even when
$N_n=N_{n+1}$.

> **Theorem 75a (projector faithfulness).** On the checked finite/pro window,
> $\rho_{\mathrm{proj}}$ is faithful on all five generator families.
>
> **Theorem 75b (projector algebra).** The support projectors form the finite
> Boolean intersection algebra $e_Se_T=e_{S\cap T}$, and the stage projectors
> form the chain algebra $q_nq_m=q_{\min(n,m)}$.
>
> **Theorem 75c (plain exact-target warning).** The companion exact-obstruction
> check shows that an ordinary exact 1-category target is still insufficient:
> the $\varprojlim^1$ phantom is derived data, not a finite exact-cone value.
> Thus the projectors must live in a derived/pro or similarly enriched exact
> setting.

**Machine verification** (`code/scripts/check-pass75.py` ->
`artifacts/reports/pass75-intrinsic-projector-realization-check.json`, PASS): 75 generators are
tested through six primes, $k\le3$, and $N_{24}$; projector-enriched signatures have zero
collisions, while the plain target still has 12; Boolean support-projector relations pass; 576
stage-projector relations pass; and restriction projectors recover source/target support.
The previously untracked companion `code/scripts/check-pass73-exact-obstruction.py` ->
`artifacts/reports/pass73-exact-realization-obstruction-check.json` is integrated as a supporting
no-go check for ordinary exact-category initiality.

**Limit of the pass.** Tags are now internal projector structure.  The remaining problem is to
interpret $e_p$ and $q_n$ naturally in an established target: clopen/idempotent support in an
LCA-sheaf or condensed setting, and a derived pro-stage filtration carrying $\varprojlim^1$.

## Pass 76 - The finite-prime stratified pro-site model

Pass 76 gives the first *natural* model for the Pass-75 projectors, replacing
the abstract idempotents $e_p,q_n$ by geometric operations on a stratified
pro-site.  The model is
$$\mathrm{StratPro}_\epsilon(U,N),$$
where $U=\{2,3,5,7,11,13\}$ is the checked prime universe carried as a finite
discrete (Stone) space and $N$ is the lcm truncation depth.

The two projector families become two concrete geometric actions:

1. **Clopen support projectors.** $e_p$ is multiplication by the characteristic
   function $\mathbf 1_{\{p\}}$ of the clopen stratum $\{p\}\subseteq U$.  The
   Boolean relation is then literally pointwise idempotent multiplication,
   $$e_Se_T=(\cdot)\,\mathbf 1_S\mathbf 1_T=(\cdot)\,\mathbf 1_{S\cap T}=e_{S\cap T}.$$
2. **Pro-stage truncation projectors.** $q_n$ is the prefix truncation of the
   non-Mittag-Leffler lcm tower $K_m=N_m\mathbb Z$ at stage $n$, so
   $$q_nq_m=q_{\min(n,m)}$$
   is truncation idempotence, and the truncations remain cofinal so the derived
   datum $\varprojlim^1 K_m\cong\widehat{\mathbb Z}/\mathbb Z$ survives in the
   limit.

The projector realization factors through the site:
$$\rho_{\mathrm{proj}}=(\text{forget site})\circ\rho_{\mathrm{site}},\qquad
\rho_{\mathrm{site}}:\mathcal H_\epsilon\to\mathrm{StratPro}_\epsilon(U,N).$$

> **Definition 76a (stratified pro-site model).**
> $\mathrm{StratPro}_\epsilon(U,N)$ is the category of pro-Ab data over the
> finite Stone space of $U$ equipped with clopen support projectors
> $e_p=(\cdot)\mathbf 1_{\{p\}}$ and lcm prefix-stage projectors $q_n$, subject
> to $e_Se_T=e_{S\cap T}$ and $q_nq_m=q_{\min(n,m)}$.
>
> **Theorem 76b (site factorization and faithfulness).** On the checked window
> ($U$ the first six primes, conductors $k\le3$, lcm stages through $N_{24}$),
> $\rho_{\mathrm{proj}}$ factors as $\rho_{\mathrm{site}}$ followed by the
> site-forgetting functor, and $\rho_{\mathrm{site}}$ is faithful on all five
> generator families: the site signature separates the $75$ generators with
> zero collisions, whereas the plain tag-forgetting signature collapses them to
> $50$.
>
> **Theorem 76c (clopen and stage relations).** The clopen support projectors
> realize the finite Boolean algebra of strata ($4160$ verified
> $e_Se_T=e_{S\cap T}$ instances) and the stage projectors realize the
> prefix-truncation chain ($576$ verified $q_nq_m=q_{\min(n,m)}$ instances).
> The separation is forced exactly at the plain target's collisions, which
> include repeated lcm stages $N_n=N_{n+1}$ (e.g. $N_5=N_6=60$,
> $N_{13}=N_{14}=N_{15}=360360$) distinguished only by the stage index $n$.

**Machine verification** (`code/scripts/check-pass76.py` ->
`artifacts/reports/pass76-stratified-pro-site-realization-check.json`, PASS): 75 generators across
the five families are tested through six primes, $k\le3$, and lcm stages through $N_{24}$; site and
projector global injectivity each have zero collisions while the plain target has 12; site family
faithfulness passes for all five families; $4160$ clopen Boolean support relations and $576$
stage-filtration relations all pass; and the factorization of $\rho_{\mathrm{proj}}$ through
$\mathrm{StratPro}_\epsilon(U,N)$ is certified on the window.

**Limit of the pass.** The support and stage projectors now have a genuine geometric reading, but
only on a finite discrete prime universe with a truncated tower.  The remaining problem is to
upgrade $\mathrm{StratPro}_\epsilon(U,N)$ to an all-prime derived exact target -- an LCA sheaf on
the profinite prime space, a condensed/solid abelian object, or a canonical exact pro-category --
and to prove the signed duality law $D_{\mathrm{res}}(\epsilon_{\mathbb P})=-\epsilon_{\mathbb
P}^{\vee}$ there as a genuine all-prime theorem, or to exhibit the derived/non-Hausdorff barrier
that blocks it.

## Pass 77 - The all-prime derived realization: LCA no-go vs. solid degree-1 shift

Pass 77 settles the Pass-76 alternative.  The two candidate targets are not
rivals; they are the two ends of a single $[-1]$ shift.  In the classical
locally compact category there is a *hard* obstruction, and in the solid
category there is a realization whose duality is forced into cohomological
degree $1$ -- precisely the degree in which $\epsilon_{\mathbb P}=\varprojlim^1$
already lives.

**The LCA barrier.** $\mathbb Z$ is dense in
$\widehat{\mathbb Z}=\varprojlim_n\mathbb Z/N_n$ (Chinese remainder), so the
quotient $Q=\widehat{\mathbb Z}/\mathbb Z$ is non-Hausdorff and is not an object
of $\mathrm{LCA}$.  Even at the level of characters the class is annihilated:
$\widehat{\widehat{\mathbb Z}}=\mathbb Q/\mathbb Z$, and the map dual to
$\mathbb Z\hookrightarrow\widehat{\mathbb Z}$ is the *injective* inclusion of
torsion points $\mathbb Q/\mathbb Z\hookrightarrow\mathbb T$, whose kernel -- the
would-be $Q^{\vee}_{\mathrm{LCA}}$ -- is $0$.

**The solid shift.** The levelwise resolution
$\mathbb Z\xrightarrow{p^n}\mathbb Z\twoheadrightarrow\mathbb Z/p^n$ gives
$\mathrm{Hom}(\mathbb Z/p^n,\mathbb Z)=0$ and
$\mathrm{Ext}^1(\mathbb Z/p^n,\mathbb Z)=\mathbb Z/p^n$, so
$R\underline{\mathrm{Hom}}(\mathbb Z_p,\mathbb Z)\cong(\mathbb Q_p/\mathbb Z_p)[-1]$
(colimit over $n$ of $\mathbb Z/p^n[-1]$).  The solid product-to-sum identity
$R\underline{\mathrm{Hom}}(\prod_p\mathbb Z_p,\mathbb Z)=\bigoplus_p
R\underline{\mathrm{Hom}}(\mathbb Z_p,\mathbb Z)$ then yields
$$\widehat{\mathbb Z}^{\,*}=R\underline{\mathrm{Hom}}(\widehat{\mathbb Z},\mathbb Z)
\cong\Big(\bigoplus_p\mathbb Q_p/\mathbb Z_p\Big)[-1]=(\mathbb Q/\mathbb Z)[-1].$$
The all-prime support projectors $e_S$ become the clopen idempotents of the Stone
space $\beta\mathbb P$ (Stone dual of $\mathcal P(\mathbb P)$), with
$e_Se_T=e_{S\cap T}$ for *all* subsets, not just the finite-window strata of
Pass 76.

> **Theorem 77a (LCA no-go / dense-subgroup barrier).** $Q=\widehat{\mathbb Z}/
> \mathbb Z$ is not an object of $\mathrm{LCA}$ ($\mathbb Z$ dense in
> $\widehat{\mathbb Z}$ makes the quotient non-Hausdorff), and
> $$Q^{\vee}_{\mathrm{LCA}}=\operatorname{Ann}_{\widehat{\widehat{\mathbb Z}}}
> (\mathbb Z)=\ker\big(\mathbb Q/\mathbb Z\hookrightarrow\mathbb T\big)=0.$$
> No LCA-sheaf realization carries a nonzero $\epsilon_{\mathbb P}^{\vee}$; the
> signed law degenerates to $0=0$.
>
> **Theorem 77b (solid degree-shift realization).** In $\mathrm{Solid}_{\mathbb Z}$,
> $R\underline{\mathrm{Hom}}(\mathbb Z_p,\mathbb Z)\cong(\mathbb Q_p/\mathbb Z_p)[-1]$
> and $\widehat{\mathbb Z}^{\,*}\cong(\mathbb Q/\mathbb Z)[-1]$; the phantom
> $\epsilon_{\mathbb P}=\widehat{\mathbb Z}/\mathbb Z=\varprojlim^1(N_n\mathbb Z)$
> is nonzero and sits in cohomological degree $1$, the same degree as the dual of
> its profinite source.  Support projectors $e_S$ ($S\in\mathcal P(\mathbb P)$)
> are the clopen idempotents of $\beta\mathbb P$ ($e_Se_T=e_{S\cap T}$ for all
> subsets); stage projectors $q_n$ are pro-truncations ($q_nq_m=q_{\min(n,m)}$).
>
> **Theorem 77c (signed law as a degree-1 derived equation).**
> $D_{\mathrm{res}}(\epsilon_{\mathbb P})=-\epsilon_{\mathbb P}^{\vee}$ holds in
> $D(\mathrm{Solid})$ as a degree-$1$ statement: each finite shadow satisfies
> $D(d_S)=-d_S^{T}$, $D^2=\mathrm{id}$, and $d_S$ is surjective with diagonal
> kernel; the antipode sign $-1$ is carried to $\varprojlim^1$ through the odd
> shift $[-1]$; and the law is not realizable in degree $0$, where by 77a the
> only LCA value is $0$.  The Pass-76 alternative therefore resolves as **both**:
> LCA is the obstruction, $\mathrm{Solid}$ is the realization, and they are the
> two ends of one $[-1]$ shift.

**Machine verification** (`code/scripts/check-pass77.py` ->
`artifacts/reports/pass77-derived-solid-realization-check.json`, PASS): (A) the annihilator of the
dense image of $\mathbb Z$ in $\mathbb Z/N_n$ is trivial through $n=12$, certifying
$Q^{\vee}_{\mathrm{LCA}}=0$; (B) $\mathrm{Hom}(\mathbb Z/N_n,\mathbb Z)=0$ and
$\mathrm{Ext}^1(\mathbb Z/N_n,\mathbb Z)=\mathbb Z/N_n$ for all checked $n$, with the dual tower
$\mathbb Z/N_n\hookrightarrow\mathbb Z/N_{n+1}$ injective (colimit $\mathbb Q/\mathbb Z$); (C)
$D(d_S)=-d_S^{T}$, $D^2=\mathrm{id}$, $d_S$ surjective of rank $|S|-1$ for $|S|=2,\ldots,6$.

**Limit of the pass.** The realization is settled, but the *self*-duality is not yet proved.  The
remaining problem is solid reflexivity: whether the canonical evaluation
$\epsilon_{\mathbb P}\to\epsilon_{\mathbb P}^{**}$ is an isomorphism in $D(\mathrm{Solid})$ (so the
phantom is self-dual up to the antipode sign), or whether a $\varprojlim^1$-of-$\varprojlim^1$
secondary phantom blocks it.

## Pass 78 - Solid reflexivity of the phantom (self-duality up to the antipode)

Pass 78 settles the Pass-77 residue.  Write $\epsilon:=\epsilon_{\mathbb P}=
\widehat{\mathbb Z}/\mathbb Z=\varprojlim^1(N_n\mathbb Z)$ and let
$D(-)=R\underline{\mathrm{Hom}}(-,\mathbb Z)$ be the solid dualizing functor in
$D(\mathrm{Solid}_{\mathbb Z})$.  The whole computation runs on the Pass-77
building blocks alone -- $D\mathbb Z=\mathbb Z$, $D\widehat{\mathbb Z}=(\mathbb Q/
\mathbb Z)[-1]$, $D(\mathbb Z/n)=(\mathbb Z/n)[-1]$ -- and *never* touches the
large abstract group $\operatorname{Ext}^1_{\mathbb Z}(\mathbb Q,\mathbb Z)$.

**Single dual.** Dualize $0\to\mathbb Z\to\widehat{\mathbb Z}\to\epsilon\to0$.
The triangle $D\epsilon\to(\mathbb Q/\mathbb Z)[-1]\to\mathbb Z\xrightarrow{+1}$ has
long exact sequence forcing $H^0(D\epsilon)=0$ and
$$0\to\mathbb Z\xrightarrow{\ \delta\ }\operatorname{Ext}^1_{\mathrm{Solid}}
(\epsilon,\mathbb Z)\to\mathbb Q/\mathbb Z\to0,\qquad
\delta(1)=[\,0\to\mathbb Z\to\widehat{\mathbb Z}\to\epsilon\to0\,].$$
So $D\epsilon=E[-1]$, $E$ an extension of $\mathbb Q/\mathbb Z$ by $\mathbb Z$, whose
class in $\operatorname{Ext}^1(\mathbb Q/\mathbb Z,\mathbb Z)\cong\widehat{\mathbb Z}$
is the *unit* $1\in\widehat{\mathbb Z}^{\times}$ -- equivalently $E\cong\mathbb Q$
(the middle of $0\to\mathbb Z\to\mathbb Q\to\mathbb Q/\mathbb Z\to0$, whose
compatible preimages of $1/n$ assemble to $1\in\widehat{\mathbb Z}$).

**Double dual.** $\epsilon^{**}=D(E)[1]$.  Dualize $0\to\mathbb Z\to E\to
\mathbb Q/\mathbb Z\to0$; here solidity does the real work: $\mathbb Q/\mathbb Z=
\operatorname{colim}_n\mathbb Z/n$ dualizes *termwise* to the limit
$D(\mathbb Q/\mathbb Z)=\varprojlim_n(\mathbb Z/n)[-1]=\widehat{\mathbb Z}[-1]$
(Mittag-Leffler, no extra $\varprojlim^1$).  The triangle
$\widehat{\mathbb Z}[-1]\to D(E)\to\mathbb Z\xrightarrow{\ d\ }(+1)$ has connecting
map $d:\mathbb Z\to\widehat{\mathbb Z}$ equal to *multiplication by the unit class*
$c=1$, i.e. the dense inclusion; hence $H^0(DE)=\ker d=0$ and $H^1(DE)=
\operatorname{coker}d=\widehat{\mathbb Z}/\mathbb Z=\epsilon$, so $D(E)=\epsilon[-1]$
and $\epsilon^{**}\cong\epsilon$.

**No secondary phantom -- and a pathological contrast.** The reflexivity is clean
*because* $c$ is a unit.  Had the connecting class been a non-unit zero-divisor --
the cleanest pathological example being the idempotent $e_2\in\widehat{\mathbb Z}$
projecting onto the $2$-adic factor -- then $\operatorname{coker}d=\widehat{\mathbb
Z}/c\widehat{\mathbb Z}$ would acquire a secondary phantom of order
$\prod_{p\mid c}p^\infty$, i.e. a genuine $\varprojlim^1$-of-$\varprojlim^1$ term.
The full profinite completion forces $c=1$, killing it; any local truncation
(single prime, idempotent) would lose reflexivity.

**Sign.** On finite shadows the antipode-signed transpose squares to the identity,
$D^2(d_S)=-(-d_S^T)^T=d_S$ (sign $+1$).  But $\epsilon$ is realized one *odd* shift
$[-1]$ from the dualizing line, and biduality transposes the two degree-$1$ shifts,
contributing Koszul sign $(-1)^{1\cdot1}=-1$.  Thus $\eta_\epsilon=-\mathrm{id}$:
$\epsilon$ is self-dual *up to the antipode*, not its negation.

> **Theorem 78a (single solid dual).** $\operatorname{Hom}_{\mathrm{Solid}}
> (\epsilon,\mathbb Z)=0$ and $D\epsilon\cong E[-1]$ with $E\cong\mathbb Q$
> (extension class the unit $1\in\widehat{\mathbb Z}^\times$); the dual of the
> phantom is concentrated in cohomological degree $1$.
>
> **Theorem 78b (reflexivity, no secondary phantom).** $\epsilon^{**}=
> R\underline{\mathrm{Hom}}(R\underline{\mathrm{Hom}}(\epsilon,\mathbb Z),\mathbb Z)
> \cong\epsilon$, via $d=\big(\mathbb Z\hookrightarrow\widehat{\mathbb Z}\big)$
> (multiplication by the unit class): $\ker d=0$, $\operatorname{coker}d=
> \widehat{\mathbb Z}/\mathbb Z=\epsilon$.  A non-unit class $c'$ (e.g. $e_2$)
> would create a secondary $\varprojlim^1$-of-$\varprojlim^1$ phantom of order
> $\prod_{p\mid c'}p^\infty$; the unit class avoids it.
>
> **Theorem 78c (biduality sign = antipode).** The evaluation
> $\eta_\epsilon:\epsilon\to\epsilon^{**}$ is an isomorphism equal to
> $-\mathrm{id}_\epsilon$: $D^2(d_S)=d_S$ on shadows (sign $+1$) and the odd shift
> $[-1]$ contributes Koszul sign $-1$.  Hence $\epsilon$ is a $[-1]$-shift
> self-dual solid object up to the antipode.

**Machine verification** (`code/scripts/check-pass78.py` ->
`artifacts/reports/pass78-solid-reflexivity-phantom-check.json`, PASS): (A) for $n\le12$,
$\operatorname{Hom}(\mathbb Z/N_n,\mathbb Z)=0$, $\operatorname{Ext}^1(\mathbb Z/N_n,\mathbb Z)=
\mathbb Z/N_n$, dual tower $\mathbb Z/N_{n+1}\twoheadrightarrow\mathbb Z/N_n$ onto (Mittag-Leffler,
limit $\widehat{\mathbb Z}$); (B) the unit class $c=1$ is iso on every finite stage
($\ker=\operatorname{coker}=1$) so $\operatorname{coker}d=\widehat{\mathbb Z}/\mathbb Z$ with no
secondary phantom, while the idempotent $c=e_2$ is non-iso from $n=3$
($\ker=\operatorname{coker}=3,3,15,15$), exhibiting the obstruction the unit avoids; (C)
$D^2(d_S)=d_S$ for $|S|=2,\ldots,6$, and the degree-$1$ shift parity gives Koszul sign $-1$,
so $\eta_\epsilon=-\mathrm{id}$.

**Limit of the pass.** What is proved is *reflexivity* $\epsilon^{**}\cong\epsilon$ with single dual
$D\epsilon\cong\mathbb Q[-1]$, and the antipode sign $\eta_\epsilon=-\mathrm{id}$.  **Caveat (corrected
in Pass 79):** this is *not* an object-level self-duality $\epsilon\cong D\epsilon[1]$ -- that reading
is false, since $D\epsilon[1]\cong\mathbb Q\not\cong\epsilon$.  Reflexivity holds for every dualizable
object; self-duality is a much stronger and here *false* statement.  The remaining problem -- upgrading
to a pairing and deciding its type and any Lagrangian decomposition -- is taken up, and the premise
corrected, in Pass 79 below.

## Pass 79 - The phantom is a dual pair, not self-dual: pairing degree, type, and a Darboux no-go

Pass 79 audits the Pass-78 "Next step".  The conjecture asked for a self-pairing
$b:\epsilon\otimes^{\blacksquare}\epsilon\to\mathbb Z[-1]$ exhibiting $\epsilon$ as a symplectic
$\widehat{\mathbb Z}$-space with the primes as Darboux coordinates.  Every clause needs correction.

**$\epsilon$ is not self-dual.** Pass 78 gives $D\epsilon\cong\mathbb Q[-1]$; dualizing the
companion sequence $0\to\mathbb Z\to\mathbb Q\to\mathbb Q/\mathbb Z\to0$ analogously gives
$D\mathbb Q\cong\epsilon[-1]$.  So $\epsilon$ and $\mathbb Q$ are **Spanier-Whitehead duals up to the
shift $[-1]$** -- a *dual pair*, not a self-dual object.  As bare abelian groups, strong approximation
($\mathbb A_f=\mathbb Q+\widehat{\mathbb Z}$, $\mathbb Q\cap\widehat{\mathbb Z}=\mathbb Z$) gives
$\epsilon=\widehat{\mathbb Z}/\mathbb Z\cong\mathbb A_f/\mathbb Q$, a $\mathbb Q$-vector space of
dimension $2^{\aleph_0}$, whereas $\dim_{\mathbb Q}\mathbb Q=1$; no shift can make $D\epsilon\cong
\epsilon[s]$.

**Forced pairing degree.** By tensor-Hom adjunction and $D\epsilon=\mathbb Q[-1]$,
$$\operatorname{Hom}_{D(\mathrm{Solid})}(\epsilon\otimes^{\blacksquare}\epsilon,\mathbb Z[m])
=\operatorname{Hom}(\epsilon,(D\epsilon)[m])=\operatorname{Hom}(\epsilon,\mathbb Q[m-1])
=\operatorname{Ext}^{m-1}_{\mathrm{Solid}}(\epsilon,\mathbb Q).$$
The solid $R\underline{\mathrm{Hom}}(\epsilon,\mathbb Q)$ is computed *not* abstractly (over $\mathbb Z$,
$\mathbb Q$ is injective and $\operatorname{Ext}^1_{\mathbb Z}(\epsilon,\mathbb Q)=0$ -- the trap) but
*solidly* via dualizability: $R\underline{\mathrm{Hom}}(\widehat{\mathbb Z},\mathbb Q)=D\widehat{\mathbb Z}
\otimes^{\blacksquare}\mathbb Q=(\mathbb Q/\mathbb Z)[-1]\otimes\mathbb Q=0$ (torsion $\otimes\mathbb Q=0$),
so the triangle from $0\to\mathbb Z\to\widehat{\mathbb Z}\to\epsilon\to0$ yields
$R\underline{\mathrm{Hom}}(\epsilon,\mathbb Q)\cong R\underline{\mathrm{Hom}}(\mathbb Z,\mathbb Q)[-1]
=\mathbb Q[-1]$.  Hence the pairing space is $\mathbb Q$ for $m=2$ and $0$ otherwise: the **proposed
target $\mathbb Z[-1]$ admits only the zero pairing**, and the unique nonzero self-pairing lives in
$\mathbb Z[2]$.

**Identity and type of the self-pairing.** $\operatorname{Ext}^1_{\mathrm{Solid}}(\epsilon,\mathbb Q)
\cong\mathbb Q$ is generated by the **finite-adele class extension** $0\to\mathbb Q\to\mathbb A_f\to
\epsilon\to0$ (pushout of the defining sequence along $\mathbb Z\hookrightarrow\mathbb Q$; the middle
term is $\mathbb Q+\widehat{\mathbb Z}=\mathbb A_f$).  As a degree-$1$ (odd) Yoneda class the swap acts
by $(-1)^{1\cdot1}=-1$, so $b$ is **alternating** -- the Pass-78 antipode sign, vindicating the
symplectic *intuition* in the corrected degree -- but **degenerate**: its adjoint
$\hat b:\epsilon\to\mathbb Q[1]$ sits between cohomological degrees $0$ and $-1$ and is not an
isomorphism.  The genuine *nondegenerate* symplectic object is the **hyperbolic plane**
$H=\epsilon\oplus\mathbb Q$ with perfect cross-pairing $\langle\,,\rangle:\epsilon\otimes^{\blacksquare}
\mathbb Q\to\mathbb Z[1]$; $\epsilon$ and $\mathbb Q$ are its two complementary Lagrangians.

**Darboux no-go (prime-indecomposability).** The StratPro support idempotents $e_S$
($S\subseteq\mathbb P$) act on the *source* $\widehat{\mathbb Z}=\prod_p\mathbb Z_p$ but descend to
$\mathrm{End}_{\mathrm{Solid}}(\epsilon)$ **iff** they preserve the diagonal
$\mathbb Z\hookrightarrow\widehat{\mathbb Z}$, iff $e_S(1)=\mathbf 1_S$ is a constant CRT vector, iff
$S\in\{\varnothing,\mathbb P\}$.  For every proper nonempty $S$, $\mathbf 1_S\notin\mathbb Z$, so
$\epsilon$ admits *no* $e_S$-induced decomposition (Lagrangian or otherwise).  The obstruction is the
unit/diagonal class $1\in\widehat{\mathbb Z}^{\times}$ -- the *same* class that powers Pass-78
reflexivity.  The phantom is globally entangled across all primes; the primes are **not** its Darboux
coordinates.

> **Theorem 79a (dual pair, not self-dual).** $D\epsilon\cong\mathbb Q[-1]$, $D\mathbb Q\cong
> \epsilon[-1]$; no shift $s$ gives $D\epsilon\cong\epsilon[s]$ (as groups $\epsilon\cong\mathbb A_f/
> \mathbb Q$ has $\mathbb Q$-dimension $2^{\aleph_0}$, $\mathbb Q$ has dimension $1$).  Corrects the
> Pass-78 "$\epsilon\cong D\epsilon[1]$": reflexivity $\ne$ self-duality.
>
> **Theorem 79b (forced degree).** $\operatorname{Hom}_{D(\mathrm{Solid})}(\epsilon\otimes^{\blacksquare}
> \epsilon,\mathbb Z[m])\cong\operatorname{Ext}^{m-1}_{\mathrm{Solid}}(\epsilon,\mathbb Q)=\mathbb Q$
> iff $m=2$, else $0$.  The proposed $\mathbb Z[-1]$ carries only $0$; the unique nonzero self-pairing
> $b\in\operatorname{Ext}^1_{\mathrm{Solid}}(\epsilon,\mathbb Q)\cong\mathbb Q$, valued in $\mathbb Z[2]$,
> is the adele class $[\,0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0\,]$.
>
> **Theorem 79c (alternating, degenerate; hyperbolic Lagrangians).** $b$ is alternating
> ($\sigma^{*}b=-b$) but degenerate ($\hat b:\epsilon\to\mathbb Q[1]$ not iso).  The nondegenerate
> symplectic object is $H=\epsilon\oplus\mathbb Q$ with $\langle\,,\rangle:\epsilon\otimes^{\blacksquare}
> \mathbb Q\to\mathbb Z[1]$ perfect; $\epsilon,\mathbb Q$ are complementary Lagrangians.
>
> **Theorem 79d (Darboux no-go).** $e_S$ descends to $\mathrm{End}_{\mathrm{Solid}}(\epsilon)$ iff
> $S\in\{\varnothing,\mathbb P\}$; $\epsilon$ is prime-indecomposable, obstructed by the unit class
> $1\in\widehat{\mathbb Z}^{\times}$.

**Machine verification** (`code/scripts/check-pass79.py` ->
`artifacts/reports/pass79-symplectic-lagrangian-phantom-check.json`, overall PASS): (A) for $n\le12$,
$\operatorname{Hom}(\mathbb Z/N_n,\mathbb Q)=0$ and $\operatorname{Ext}^1(\mathbb Z/N_n,\mathbb Q)=
\mathbb Q/N_n\mathbb Q=0$ (certifying $R\underline{\mathrm{Hom}}(\widehat{\mathbb Z},\mathbb Q)=0$);
(B) the degree table $\dim_{\mathbb Q}\operatorname{Ext}^{m-1}(\epsilon,\mathbb Q)=[\,m=2\,]$ over
$m\in\{-1,0,1,2,3\}$; (C) CRT factorizations through $N_9$ for the adele pushout shadow;
(D) swap sign $-1$ (alternating), adjoint non-iso (degenerate); (E) the Darboux enumeration over all
$2^6=64$ subsets of $\{2,3,5,7,11,13\}$ -- exactly $2$ descend ($\varnothing$, full), $62$ fail;
(F) the finite duality pairing $\mathbb Z/N\times\mathbb Z/N\to\mathbb Q/\mathbb Z$ nondegenerate for
$N\le840$ (hyperbolic Lagrangian pair).

**Limit of the pass.** The symplectic structure is real but *external* to $\epsilon$: it lives on the
hyperbolic plane $H=\epsilon\oplus\mathbb Q$.  The next problem is the metaplectic/Weil structure of
$H$ -- whether the finite-adele Weil representation of $\mathrm{SL}_2(\mathbb A_f)$ descends to a
canonical action on the phantom with $\mathbb Q,\epsilon$ as its two polarizations, or whether the
degeneracy of $b$ blocks the metaplectic cocycle.

## Pass 80 - $\mathrm{Sp}(H)$ is a solid Borel, not $\mathrm{SL}_2$: metaplectic non-descent and the no-flip wall

Pass 80 computes the solid symplectic automorphism object of the Pass-79 hyperbolic plane
$H=\epsilon\oplus\mathbb Q$ and corrects the Pass-79 Next-step's guess about *which* feature blocks
the metaplectic structure.

**Read the endomorphism object directly (reflexive $\ne$ dualizable).**  A solid endomorphism of
$H=\epsilon\oplus\mathbb Q$ is a matrix
$$M=\begin{pmatrix}a&b\\c&d\end{pmatrix},\qquad
a\in\mathrm{End}(\epsilon),\ b\in\mathrm{Hom}(\mathbb Q,\epsilon),\
c\in\mathrm{Hom}(\epsilon,\mathbb Q),\ d\in\mathrm{End}(\mathbb Q).$$
One must compute the four Hom-objects *directly*, because $\epsilon$ -- although **reflexive**
($\epsilon^{**}\cong\epsilon$, Pass 78) -- is **not** $\otimes$-dualizable (as a group it is a
$\mathbb Q$-vector space of dimension $2^{\aleph_0}$), so the shortcut
$R\underline{\mathrm{Hom}}(\epsilon,\epsilon)=D\epsilon\otimes\epsilon$ is *illegitimate*.  The entries:
$\mathrm{End}(\mathbb Q)=\mathbb Q$; $\mathrm{Hom}(\mathbb Q,\epsilon)=\epsilon$ (for any
$\mathbb Q$-vector space $V$, $\mathrm{Hom}(\mathbb Q,V)=V$); and crucially, from the Pass-79
computation $R\underline{\mathrm{Hom}}(\epsilon,\mathbb Q)=\mathbb Q[-1]$,
$$\mathrm{Hom}_{\mathrm{Solid}}(\epsilon,\mathbb Q)=H^0(\mathbb Q[-1])=0.$$
So the lower-left entry $c$ **vanishes identically**: every solid endomorphism of $H$ is
**upper-triangular**.

**$\mathrm{Sp}(H)$ is the solid Borel $\mathbb Q^{\times}\ltimes\epsilon$.**  Upper-triangularity
collapses the would-be $\mathrm{SL}_2$ onto its Borel: the torus $T=\mathbb Q^{\times}$ rescales the
dual pair ($\lambda$ on $\mathbb Q$, $\lambda^{-1}$ on $\epsilon$, to fix
$\langle\,,\rangle:\epsilon\otimes\mathbb Q\to\mathbb Z[1]$); the unipotent radical $U$ is the abelian
solid group of symplectic shears $x\mapsto x+by,\ y\mapsto y$ ($b$ the degenerate Pass-79
self-pairing).  Thus $\mathrm{Sp}(H)=B=\mathbb Q^{\times}\ltimes\epsilon$ is the **affine "$ax+b$"
group** -- the Schrödinger parabolic that *fixes the polarization $\epsilon$*.  It is **solvable**: it
is neither $\mathrm{SL}_2$ (no opposite unipotent, no Weyl element) nor a nonabelian Heisenberg group
($U$ is abelian).  The Weyl flip $w=\begin{psmallmatrix}0&1\\-1&0\end{psmallmatrix}$ -- the
cross-polarization Fourier transform -- has **no solid model**, its $(2,1)$-entry being trapped in
$\mathrm{Hom}(\epsilon,\mathbb Q)=0$.

**Metaplectic non-descent, and the corrected wall.**  At every finite level $N$ the shadow is the
*full* $\mathrm{SL}_2(\mathbb Z/N)=\mathrm{Sp}(\mathbb Z/N\oplus\mathbb Z/N)$, the two coordinate
Lagrangians are *isomorphic* ($\cong\mathbb Z/N$), and the Weyl flip is realized by the finite Fourier
transform $F_N$ (quadratic Gauss sum, $F_N^4=I$, $|g_N|^2=N$).  The collapse is a pure *limit*
phenomenon: as $N\to\infty$ the two Lagrangians de-isomorphise into $\epsilon$ (the
prefix/$\varprojlim^1$ side) versus $\mathbb Q$ (the divisible side), and the only candidate limit of
$\{F_{N_n}\}$ would be an element of $\mathrm{Hom}_{\mathrm{Solid}}(\epsilon,\mathbb Q)=0$.  The
finite-adele Weil representation of $\mathrm{SL}_2(\mathbb A_f)$ therefore does **not** descend to the
phantom; only its Borel $B$ acts.  The precise wall is $\mathrm{Hom}_{\mathrm{Solid}}(\epsilon,
\mathbb Q)=0$ -- the *one-sidedness* of the dual pair $(\epsilon,\mathbb Q)$, equivalently the
reflexive-but-not-dualizable nature of $\epsilon$ -- and is **explicitly not** the degeneracy of $b$
that the Pass-79 Next step had hypothesised: the shear-by-$b$ unipotent is alive and well inside $B$;
what is missing is the *inverse* intertwiner $\epsilon\to\mathbb Q$.  This is the same unit-class
entanglement ($1\in\widehat{\mathbb Z}^{\times}$) that drove the Pass-79 Darboux no-go, now seen as
the absence of the cross-polarization Fourier flip.

> **Theorem 80a (upper-triangularity).** $\mathrm{Hom}_{\mathrm{Solid}}(\epsilon,\mathbb Q)=0$ and
> $\mathrm{Hom}_{\mathrm{Solid}}(\mathbb Q,\epsilon)=\epsilon\neq0$, $\mathrm{End}(\mathbb Q)=\mathbb Q$;
> hence every solid endomorphism of $H=\epsilon\oplus\mathbb Q$ is upper-triangular
> $\begin{psmallmatrix}a&b\\0&d\end{psmallmatrix}$, and $\epsilon$ is the unique
> $\mathrm{End}(H)$-stable line.
>
> **Theorem 80b ($\mathrm{Sp}(H)$ is a solid Borel).** $\mathrm{Sp}(H)=B=T\ltimes U$ with
> $T=\mathbb Q^{\times}$ and $U$ the abelian shear group (containing $b$); $B\cong\mathbb Q^{\times}
> \ltimes\epsilon$ is the affine "$ax+b$" group fixing the polarization $\epsilon$.  It is solvable:
> not $\mathrm{SL}_2$, not nonabelian Heisenberg.  The Weyl flip $w$ is not a solid morphism.
>
> **Theorem 80c (metaplectic non-descent; the wall).** The finite-adele Weil representation of
> $\mathrm{SL}_2(\mathbb A_f)$ does not descend to a solid action on $\epsilon$ with $\mathbb Q,
> \epsilon$ as polarizations.  At finite level the flip exists ($F_N$, $F_N^4=I$, $|g_N|^2=N$); its
> limit lies in $\mathrm{Hom}_{\mathrm{Solid}}(\epsilon,\mathbb Q)=0$.  The precise wall is that
> vanishing (one-sided dual pair / $\epsilon$ reflexive but not dualizable), **not** the degeneracy
> of $b$.

**Machine verification** (`code/scripts/check-pass80.py` ->
`artifacts/reports/pass80-metaplectic-borel-noflip-check.json`, overall PASS): (A) for $N\in\{2,\ldots,
12,60,420,840\}$, $|\mathrm{SL}_2(\mathbb Z/N)|=N^3\prod_{p\mid N}(1-p^{-2})$ (brute-force confirmed
for $N\le12$), $|B|=\varphi(N)N$, Bruhat $|\mathrm{SL}_2|=|B|\cdot|\mathbb P^1(\mathbb Z/N)|$, and $w$
present with $w^2=-I$ swapping the coordinate Lagrangians; (B) the $c$-tower
$\mathrm{Hom}(\mathbb Z/N_n,\mathbb Q)=0$, $\mathrm{Ext}^1(\mathbb Z/N_n,\mathbb Q)=\mathbb Q/N_n
\mathbb Q=0$ ($n\le12$, so $c\equiv0$) versus the $b$-tower $\mathrm{Hom}((1/N_n)\mathbb Z/\mathbb Z,
\mathbb Q/\mathbb Z)=\mathbb Z/N_n\neq0$ with surjective bonding; (C) finite Fourier $F_N$ for
$N\in\{3,5,7,9,11,15,21\}$ with $F_N^4=I$, $F_NF_N^{*}=I$, $|g_N|^2=N$ to $<10^{-7}$.

**Limit of the pass.** The symplectic group is *honest but solvable*: $\mathrm{Sp}(H)=\mathbb Q^{\times}
\ltimes\epsilon$, the Borel/Schrödinger model in the fixed polarization $\epsilon$, with no Weyl flip.
The next problem is whether this one-sided (non-self-dual) Borel is the algebraic shadow of a degenerate
principal series whose missing intertwiner $\in\mathrm{Hom}(\epsilon,\mathbb Q)=0$ is precisely the
obstruction to a self-dual functional equation -- and whether "no Fourier flip" is the
representation-theoretic face of the Pass-51 Löb/Rosser $\leftrightarrow$ integral/non-integral-unit
dividing line.

## Pass 81 - Degenerate principal series and the missing functional equation

Pass 81 reads the Pass-80 solid Borel
$$B=\mathbb Q^{\times}\ltimes\epsilon=\mathrm{Sp}(H)$$
as a representation-theoretic object.  For a torus character
$$\chi_s:B\twoheadrightarrow\mathbb Q^{\times}\xrightarrow{|\cdot|^s}R^{\times}$$
trivial on $U=\epsilon$, the induced module is
$$I(s)=\mathrm{Ind}_{B}^{\mathrm{Sp}(H)}\chi_s.$$
But $\mathrm{Sp}(H)=B$, so $\mathrm{Sp}(H)/B=\mathrm{pt}$ and
$$I(s)\cong\chi_s.$$
This is a **maximally degenerate principal series**: length $1$, no reducibility
points, and no Bruhat big cell.

The standard functional equation would be mediated by the Weyl/intertwining
operator
$$M(w,s):I(s)\to I(-s),\qquad
M(w,s)f(g)=\int_{\bar U}f(w^{-1}\bar u g)\,d\bar u.$$
Here
$$\bar U=\mathrm{Hom}_{\mathrm{Solid}}(\epsilon,\mathbb Q)=0,$$
so the integral has no nonzero solid datum.  The $c$-function is the empty
product $c(s)=1$, but there is no reflection operator; $I(s)$ and $I(-s)$ are
not canonically related for $s\ne0$.

> **Theorem 81a (maximally degenerate principal series).**
> $I(s)=\mathrm{Ind}_{B}^{\mathrm{Sp}(H)}\chi_s\cong\chi_s$ because
> $\mathrm{Sp}(H)=B$.  The flag variety is a point.
>
> **Theorem 81b (no functional equation).**
> The opposite unipotent $\bar U=\mathrm{Hom}_{\mathrm{Solid}}(\epsilon,\mathbb Q)$
> is zero, so no Weyl/Fourier intertwiner $M(w,s)$ exists in the solid target.
>
> **Theorem 81c (finite/limit dichotomy).**
> Finite levels still have Fourier intertwiners:
> $$F_ND_tF_N^{-1}=D_{t^{-1}}$$
> on $\mathbb C[\mathbb Z/N]$, with Gauss norms $|g(\psi)|^2=p$.  The functional
> equation is finitely present and limanly absent.
>
> **Theorem 81d (Lﾃｶb/Rosser face).**
> The surviving direction $\mathrm{Hom}(\mathbb Q,\epsilon)=\epsilon$ is the
> forgetful move from canonical Lﾃｶb data to Rosser torsor data.  The missing
> direction $\mathrm{Hom}(\epsilon,\mathbb Q)=0$ says that the Rosser torsor has
> no canonical retraction back to the Lﾃｶb side.
>
> **Corollary 81e.**
> Reflexivity is not enough for a functional equation; the polarization must be
> tensor-dualizable.  The phantom $\epsilon$ is reflexive but not dualizable.

**Machine verification** (`code/scripts/check-pass81.py` ->
`artifacts/reports/pass81-degenerate-principal-series-functional-equation-check.json`, PASS):
finite projective-line sizes are nontrivial while the solid opposite-unipotent
limit vanishes; $F_ND_tF_N^{-1}=D_{t^{-1}}$ holds for $N\le16$ to numerical
precision; Gauss sums satisfy $|g(\psi)|^2=p$ for $p\le23$; and the $c$-tower
vanishes while the shear tower remains nonzero.

**Limit of the pass.** The solid Borel has no self-dual functional equation.  The
next residue is whether a Whittaker or generalized-Whittaker functional remains,
and whether the real place repairs the lost finite-prime Fourier flip.

## Pass 82 - Whittaker vanishing and archimedean repair

Pass 82 closes the Pass-81 residue.  Since
$$I(s)=\chi_s$$
and $\chi_s$ is trivial on $U=\epsilon$, a $U$-equivariant functional
to a character $\psi$ exists only for the trivial character:
$$
\operatorname{Hom}_U(I(s),\psi)\cong
\begin{cases}
R,&\psi=1,\\
0,&\psi\ne1.
\end{cases}
$$
Thus the degenerate principal series has **no nontrivial Whittaker model**.
Only the constant term survives.  The Rosser torsor is not encoded by a generic
Whittaker coefficient; it is the unipotent shear parameter $U=\epsilon$ itself.

At finite level this is just the Fourier sum of a constant function:
$$
\sum_{x\in\mathbb Z/N}e^{2\pi ikx/N}
=
\begin{cases}
N,&k=0,\\
0,&k\ne0.
\end{cases}
$$
So finite nontrivial additive characters exist, but they do not produce a
nontrivial Whittaker coefficient for the collapsed solid principal series.

The archimedean place repairs a different object.  Strong approximation gives
the full adelic solenoid
$$
\Sigma=(\mathbb R\times\widehat{\mathbb Z})/\mathbb Z\cong\mathbb A/\mathbb Q
$$
and the exact sequence
$$
0\to\widehat{\mathbb Z}
\to\Sigma\to\mathbb R/\mathbb Z\to0.
$$
Pass 83 corrects the provisional Pass-82 wording: $\epsilon=\widehat{\mathbb Z}/\mathbb Z$
is not this closed kernel, but the dense quotient $\Sigma/\mathbb R$.  The real
circle makes $\Sigma$ compact Hausdorff and globally self-dual, so the full
adelic quotient has Fourier theory.  This does not create a finite-prime solid
morphism $\epsilon\to\mathbb Q$, hence it does not undo the no-Weyl-flip wall
for $\epsilon$.

> **Theorem 82a (Whittaker vanishing).**
> $\operatorname{Hom}_U(I(s),\psi)=0$ for every nontrivial character $\psi$ of
> $U=\epsilon$, and is one-dimensional for $\psi=1$.
>
> **Theorem 82b (constant-term finite shadow).**
> Nontrivial finite Fourier/Whittaker coefficients of the constant $U_N$-action
> vanish; the trivial coefficient is $N$.
>
> **Theorem 82c (archimedean repair without finite flip; corrected by Pass 83).**
> $\Sigma=(\mathbb R\times\widehat{\mathbb Z})/\mathbb Z$ repairs global adelic
> duality, while the finite-prime phantom $\epsilon$ remains one-sided and has no
> $\epsilon\to\mathbb Q$ Weyl morphism.  Pass 83 corrects the exact row:
> $\ker(\Sigma\to\mathbb R/\mathbb Z)=\widehat{\mathbb Z}$, and
> $\epsilon=\widehat{\mathbb Z}/\mathbb Z$ is the dense quotient $\Sigma/\mathbb R$.

**Machine verification** (`code/scripts/check-pass82.py` ->
`artifacts/reports/pass82-whittaker-archimedean-repair-check.json`, PASS): nontrivial
Fourier coefficients vanish for checked moduli $N\in\{2,3,4,5,6,8,9,12,15,16,30\}$;
the $U$-equivariant Hom table is $1$ for the trivial character and $0$ for nontrivial
characters; finite shadows of the solenoid exact sequence have kernel size $N$ and
pass the diagonal-reduction exactness check.

**Limit of the pass.** The next question is no longer Whittaker-genericity; it is the
exact-triangle comparison between the global solenoid $\Sigma$ and the finite phantom
$\epsilon$.  In particular, does $\Sigma\to\mathbb R/\mathbb Z$ split in any
solid/condensed sense compatible with $B$, and does global Fourier transform induce
only a constant term on $\epsilon$ or a boundary class measuring the lost finite Weyl
flip?

## Pass 83 - Correcting the solenoid exact triangle

Pass 83 audits the Pass-82 exact sequence.  For
$$
\Sigma=(\mathbb R\times\widehat{\mathbb Z})/\mathbb Z,
$$
projection to the real circle has closed kernel $\widehat{\mathbb Z}$:
$$
0\to\widehat{\mathbb Z}\to\Sigma\to\mathbb R/\mathbb Z\to0.
$$
Indeed, an element in the kernel has a representative $(n,z)$ with
$n\in\mathbb Z$, hence is equivalent to $(0,z-n)$, and two representatives
$(0,z),(0,z')$ are equivalent only when $z=z'$.  Thus the finite phantom
$\epsilon=\widehat{\mathbb Z}/\mathbb Z$ is **not** a closed subgroup of
$\Sigma$.  It is the dense quotient
$$
\Sigma/\mathbb R\cong
(\mathbb R\times\widehat{\mathbb Z})/(\Delta\mathbb Z+\mathbb R\times0)
\cong\widehat{\mathbb Z}/\mathbb Z.
$$

The compact row is nonsplit.  Pontryagin duality gives
$$
0\to\mathbb Z\to\mathbb Q\to\mathbb Q/\mathbb Z\to0,
$$
and this cannot split because $\mathbb Q$ is torsion-free while
$\mathbb Q/\mathbb Z$ is torsion.  Hence there is no continuous or condensed
degree-$0$ section $\mathbb R/\mathbb Z\to\Sigma$, and no $B$-compatible
section of the kind Pass 82 asked for.

The Fourier consequence is now sharper.  Global characters
$\widehat{\Sigma}\cong\mathbb Q$ restrict to finite characters on the closed
kernel $\widehat{\mathbb Z}$ via $\mathbb Q\to\mathbb Q/\mathbb Z$.  But a
finite character descends to
$\epsilon=\widehat{\mathbb Z}/\mathbb Z$ only if it kills the dense diagonal
$\mathbb Z$, so only the trivial character descends.  The finite-prime
Fourier data is therefore a **boundary quotient** $\mathbb Q/\mathbb Z$, not a
degree-$0$ character sheaf on $\epsilon$.

> **Theorem 83a (correct solenoid rows).**
> The full solenoid has the closed-kernel row
> $0\to\widehat{\mathbb Z}\to\Sigma\to\mathbb R/\mathbb Z\to0$ and the
> dense-quotient row $\mathbb R\to\Sigma\to\epsilon\to0$.
>
> **Theorem 83b (nonsplitting).**
> The compact row is nonsplit continuously/condensedly, since its dual
> $0\to\mathbb Z\to\mathbb Q\to\mathbb Q/\mathbb Z\to0$ has no torsion-valued
> section into $\mathbb Q$.
>
> **Theorem 83c (Fourier boundary).**
> Global Fourier theory restricts to $\mathbb Q/\mathbb Z$ on the closed
> profinite kernel, but only the trivial character descends to
> $\epsilon=\widehat{\mathbb Z}/\mathbb Z$ in degree $0$.

**Machine verification** (`code/scripts/check-pass83.py` ->
`artifacts/reports/pass83-solenoid-exact-triangle-correction-check.json`, PASS):
finite dual rows $0\to\mathbb Z\xrightarrow{\times N}\mathbb Z\to\mathbb Z/N\to0$
are exact and nonsplit for nontrivial $N$; finite characters on $\widehat{\mathbb Z}/N$ have
count $N$, but exactly one descends across the dense diagonal quotient; finite
level cokernels of $\mathbb Z\to\mathbb Z/N$ are zero, so the phantom is
derived/non-Hausdorff rather than an ordinary finite cokernel.

**Limit of the pass.**  The next task is to formulate the derived/solid exact
triangle behind the dense quotient $\mathbb R\to\Sigma\to\epsilon$ and identify
the boundary object $\mathbb Q/\mathbb Z$ (or its shifted solid dual) as the
precise replacement for the missing finite-prime Weyl flip.

## Pass 84 - Dense phantom boundary and the action obstruction

Pass 84 separates the topological quotient from the solid derived boundary.
The quotient
$$
\epsilon=\widehat{\mathbb Z}/\mathbb Z
$$
is indiscrete as a topological group: because $\mathbb Z$ is dense in
$\widehat{\mathbb Z}$, the saturation of any nonempty open subset is all of
$\widehat{\mathbb Z}$.  Therefore the Hausdorff reflection of $\epsilon$ is
$0$, and every continuous homomorphism $\epsilon\to H$ into a Hausdorff group
$H$ is zero.

Consequently the unipotent radical
$$
U=\epsilon
$$
of the solid Borel cannot act by nontrivial continuous translations on the
compact Hausdorff solenoid $\Sigma$.  A translation action would require a
nonzero continuous homomorphism $U\to\Sigma$, which the indiscrete quotient
forbids.  This is the topological face of the same degree-$0$ vanishing already
seen in Passes 82-83: finite characters live on the closed kernel
$\widehat{\mathbb Z}$, but only the trivial character descends to
$\epsilon=\widehat{\mathbb Z}/\mathbb Z$.

The phantom survives only after passing to the solid derived category:
$$
D\epsilon\simeq\mathbb Q[-1],
\qquad
\mathrm{Ext}^1_{\mathrm{Solid}}(\epsilon,\mathbb Q)\simeq\mathbb Q.
$$
The generator is the finite-adele extension
$$
0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0.
$$
Thus the missing finite-prime Weyl flip is not a morphism
$\epsilon\to\mathbb Q$ but a degree-$1$ boundary/shear class.  The finite group
$\mathbb Q/\mathbb Z$ is still visible as the character boundary of the closed
kernel $\widehat{\mathbb Z}$ in the compact row; the solid arithmetic boundary
attached to $\epsilon$ is its shifted completion $\mathbb Q[-1]$.

> **Theorem 84a (indiscrete quotient).**
> The topological quotient $\widehat{\mathbb Z}/\mathbb Z$ is indiscrete.
> Hence its Hausdorff reflection is $0$, and every continuous homomorphism from
> $\epsilon$ to a Hausdorff group is zero.
>
> **Theorem 84b (no topological $U$-translation on $\Sigma$).**
> The Borel unipotent $U=\epsilon$ has no nontrivial continuous translation
> action on the compact Hausdorff solenoid $\Sigma$.  Its action is a solid
> shear/boundary parameter of the hyperbolic plane $H=\epsilon\oplus\mathbb Q$.
>
> **Theorem 84c (derived Weyl replacement).**
> $D\epsilon\simeq\mathbb Q[-1]$ and
> $\mathrm{Ext}^1_{\mathrm{Solid}}(\epsilon,\mathbb Q)\simeq\mathbb Q$.
> The missing Weyl flip $\epsilon\to\mathbb Q$ is replaced by the degree-$1$
> finite-adele extension $0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0$.

**Machine verification** (`code/scripts/check-pass84.py` ->
`artifacts/reports/pass84-dense-phantom-boundary-action-check.json`, PASS):
finite quotient shadows have only empty/all saturated opens; continuous maps
from the indiscrete quotient to checked discrete Hausdorff targets are
constant, and continuous group homomorphisms are only the zero homomorphism;
finite characters on $\widehat{\mathbb Z}/N$ descend across the dense diagonal
only for the trivial character; finite degree-$0$ Hom/Ext shadows into
$\mathbb Q$ vanish at all checked stages.

**Limit of the pass.**  The next task is to write an explicit two-term complex
model for the boundary, comparing $[\mathbb Z\to\widehat{\mathbb Z}]$,
$[\mathbb R\to\Sigma]$, and $[\mathbb Q\to\mathbb A_f]$.

## Pass 85 - Two-term complex models of the phantom boundary

Pass 85 writes the boundary in cohomological degrees $0\to1$:
$$
C_{\mathbb Z}=[\,\mathbb Z\to\widehat{\mathbb Z}\,],\quad
C_{\mathbb R}=[\,\mathbb R\to\Sigma\,],\quad
C_{\mathbb Q}=[\,\mathbb Q\to\mathbb A_f\,].
$$
All three differentials are injective and all three quotients are
$$
H^1\cong\epsilon=\widehat{\mathbb Z}/\mathbb Z.
$$
For $C_{\mathbb R}$ this is $\Sigma/\mathbb R\cong\widehat{\mathbb Z}/\mathbb Z$;
for $C_{\mathbb Q}$ it is
$\mathbb A_f/\mathbb Q\cong\widehat{\mathbb Z}/\mathbb Z$ by strong
approximation $\mathbb A_f=\mathbb Q+\widehat{\mathbb Z}$ and
$\mathbb Q\cap\widehat{\mathbb Z}=\mathbb Z$.

Finite/Hausdorff probes see none of these quotients.  Modulo $N$, the diagonal
map $\mathbb Z\to\mathbb Z/N$ is surjective, so the ordinary finite cokernel is
zero; topologically, $\mathbb R$ is dense in $\Sigma$ and $\mathbb Q$ is dense
in $\mathbb A_f$.  The phantom is therefore not an ordinary cokernel but the
solid/derived residue of the non-Mittag-Leffler kernel tower $N_n\mathbb Z$.

The extension data distinguishes the rows.  The map
$$
C_{\mathbb Z}\to C_{\mathbb Q}
$$
is the pushout of $0\to\mathbb Z\to\widehat{\mathbb Z}\to\epsilon\to0$ along
$\mathbb Z\hookrightarrow\mathbb Q$, and therefore preserves the unit/Yoneda
class:
$$
0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0.
$$
This is the Borel shear class from Passes 79-84.  The archimedean row
$C_{\mathbb R}$ is quotient-equivalent but not shear-class-equivalent: it
repairs the global compact solenoid, while the finite-adele row carries the
solid Borel action.

> **Theorem 85a (three quotient complexes).**
> $C_{\mathbb Z}$, $C_{\mathbb R}$, and $C_{\mathbb Q}$ have $H^0=0$ and
> $H^1\cong\epsilon$.  Their finite/Hausdorff shadows are acyclic.
>
> **Theorem 85b (phantom source).**
> The nonzero boundary is the $\varprojlim^1$/solid residue of the
> non-Mittag-Leffler kernel tower $N_n\mathbb Z$; it is invisible to finite
> cokernel tests.
>
> **Theorem 85c (shear-preserving pushout).**
> The comparison $C_{\mathbb Z}\to C_{\mathbb Q}$ preserves the finite-adele
> shear class.  The comparison through $C_{\mathbb R}$ preserves only the
> quotient $\epsilon$, not the Borel shear extension.

**Machine verification** (`code/scripts/check-pass85.py` ->
`artifacts/reports/pass85-two-term-boundary-complex-check.json`, PASS): finite
diagonal images are all of $\mathbb Z/N$ and ordinary finite/Hausdorff
cokernels vanish; the lcm kernel tower has repeated strict drops; unit residues
$1\bmod N$ are compatible units; the comparison table marks
$C_{\mathbb Z}$ and $C_{\mathbb Q}$, but not $C_{\mathbb R}$, as preserving
the finite-adele shear class.

**Limit of the pass.**  The next task is a universal property: characterize
$C_{\mathbb Q}$ as the initial divisible-kernel quotient model receiving
$C_{\mathbb Z}$ and preserving the unit/shear class while killing finite
Hausdorff cokernels.

## Pass 86 - Universal property of the shear pushout

Pass 86 refines "divisible-kernel quotient model" to the exact hypothesis under
which the universal property is true.  Define $\mathcal P_{\mathbb Q}(\epsilon)$
to consist of shear-marked exact rows
$$
0\to D\to E\to\epsilon\to0
$$
receiving
$$
C_{\mathbb Z}=[\,\mathbb Z\to\widehat{\mathbb Z}\,],
$$
where $D$ is uniquely divisible, the row is the pushout of the unit extension
along $\mathbb Z\to D$, and finite/Hausdorff shadows of the quotient are
acyclic.  Since a uniquely divisible group is a $\mathbb Q$-vector object, the
map $\mathbb Z\to D$ extends uniquely to $\mathbb Q\to D$.  Therefore the
finite-adele row
$$
C_{\mathbb Q}=[\,\mathbb Q\to\mathbb A_f\,]
$$
is initial under $C_{\mathbb Z}$ in this category.

This is the precise categorical replacement for the missing Weyl flip:
instead of constructing a degree-$0$ map $\epsilon\to\mathbb Q$, one localizes
the kernel $\mathbb Z$ to $\mathbb Q$ inside the extension category and keeps
the shear/Yoneda class
$$
0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0.
$$
Finite probes still see no ordinary cokernel because the integer residues
already surject at every finite modulus.

The pass also records a necessary caveat.  If "divisible" is read literally,
the result is false.  The divisible torsion group $\mathbb Q/\mathbb Z$ admits
distinct maps
$$
q\mapsto kq\bmod\mathbb Z
$$
from $\mathbb Q$ that restrict to the same map on $\mathbb Z$ but differ on
fractions.  Thus torsion-divisible summands must be excluded, or else equipped
with additional shear/$\mathbb Q$-linear decoration.

> **Theorem 86a (initial shear pushout).**
> In $\mathcal P_{\mathbb Q}(\epsilon)$, the complex
> $C_{\mathbb Q}=[\mathbb Q\to\mathbb A_f]$ is initial under
> $C_{\mathbb Z}=[\mathbb Z\to\widehat{\mathbb Z}]$.
>
> **Theorem 86b (finite-shadow stability).**
> The pushout $C_{\mathbb Z}\to C_{\mathbb Q}$ preserves acyclicity of ordinary
> finite/Hausdorff shadows.
>
> **Theorem 86c (torsion-divisible caveat).**
> The same initiality statement fails for arbitrary divisible kernels; the
> torsion-divisible example $\mathbb Q/\mathbb Z$ supplies multiple extensions
> of the same map out of $\mathbb Z$.

**Machine verification** (`code/scripts/check-pass86.py` ->
`artifacts/reports/pass86-shear-pushout-universal-property-check.json`, PASS):
bounded denominator localizations $\mathbb Z[1/L]$ have unique extension into
checked $\mathbb Q$-vector targets; finite residue shadows remain killed; and
the maps $q\mapsto kq\bmod\mathbb Z$ give distinct torsion-divisible extensions
with identical restriction to $\mathbb Z$.

**Limit of the pass.**  The next task is to promote this finite certificate to
a mapping-space statement in $D(\mathrm{Solid})$, including an explicit rule
for excluding or decorating torsion-divisible kernel summands.

## Pass 87 - Mapping-space form of shear initiality

Pass 87 turns the Pass-86 universal property into a derived mapping-space
criterion.  For a shear-marked target row
$$
M=(0\to D\to E\to\epsilon\to0),
$$
restriction along
$$
C_{\mathbb Z}\to C_{\mathbb Q}
$$
gives
$$
\operatorname{Map}(C_{\mathbb Q},M)\to
\operatorname{Map}(C_{\mathbb Z},M).
$$
Because the cofiber of $\mathbb Z\to\mathbb Q$ is $\mathbb Q/\mathbb Z$, the
homotopy fiber over a fixed shear-marked map is
$$
\mathbf R\!\operatorname{Map}(\mathbb Q/\mathbb Z,D).
$$

For uniquely divisible $D$, the fiber is contractible.  The group
$\mathbb Q/\mathbb Z$ is torsion while $D$ is torsion-free, so
$\operatorname{Hom}(\mathbb Q/\mathbb Z,D)=0$; and $D$ is divisible, hence
injective, so higher Ext obstructions vanish.  This proves the Pass-86
initiality in the stronger derived sense.

For torsion-divisible summands $T$, the fiber is not contractible:
$$
\mathbf R\!\operatorname{Map}(\mathbb Q/\mathbb Z,T)
$$
contributes genuine components.  Finite approximations already show this: a
rank-$r$ torsion summand has $N^r$ boundary choices at modulus $N$.  Therefore
the strict initial object lives in the uniquely divisible subcategory.  If
torsion-divisible kernels are allowed, they must carry an explicit boundary
decoration choosing the $\mathbb Q/\mathbb Z\to T$ component.

> **Theorem 87a (mapping-space fiber).**
> For a shear-marked target with kernel $D$, the fiber of
> $\operatorname{Map}(C_{\mathbb Q},M)\to\operatorname{Map}(C_{\mathbb Z},M)$
> is $\mathbf R\!\operatorname{Map}(\mathbb Q/\mathbb Z,D)$.
>
> **Theorem 87b (contractible uniquely divisible fiber).**
> If $D$ is uniquely divisible, this fiber is contractible.
>
> **Theorem 87c (torsion decoration).**
> If $D$ contains torsion-divisible $T$, strict initiality fails by the extra
> fiber $\mathbf R\!\operatorname{Map}(\mathbb Q/\mathbb Z,T)$ unless this
> component is excluded or decorated.

**Machine verification** (`code/scripts/check-pass87.py` ->
`artifacts/reports/pass87-mapping-space-shear-initiality-check.json`, PASS):
the checker records the cofiber/fiber sequence, verifies contractible finite
torsion tests for $\mathbb Q$-vector kernels, and shows that torsion-divisible
finite shadows have $N^r$ components at modulus $N$.

**Limit of the pass.**  The next task is to compute the derived
automorphism/stabilizer of the final finite-adele shear extension and compare
it with the solid Borel action $\mathbb Q^\times\ltimes\epsilon$.

## Pass 88 - Stabilizer of the finite-adele shear extension

Pass 88 separates three automorphism levels attached to
$$
0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0.
$$

First, the strict object under
$$
C_{\mathbb Z}=[\mathbb Z\to\widehat{\mathbb Z}]
$$
is rigid.  Any rational scalar automorphism preserving the map from
$C_{\mathbb Z}$ must fix the marked unit $1\in\mathbb Z$, hence is scalar
$1$.  By Pass 87,
$$
\mathbf R\!\operatorname{Map}(\mathbb Q/\mathbb Z,\mathbb Q)=0,
$$
so there is no hidden derived automorphism for the final uniquely divisible
kernel.

Second, if the integral marking is forgotten and only the shear Ext line is
preserved, the degree-$0$ stabilizer is
$$
\mathbb Q^\times.
$$
Nonzero rational scalars act on $\mathbb Q$ and $\mathbb A_f$ and preserve the
one-dimensional finite-adele extension line.  This is the Levi component of
the Borel.

Third, the full solid Borel from Pass 80,
$$
B=\mathbb Q^\times\ltimes\epsilon,
$$
belongs to the hyperbolic object
$$
H=\epsilon\oplus\mathbb Q
$$
with fixed polarization.  The unipotent term $\epsilon$ is a shear of $H$, not
an endpoint-fixing automorphism of the bare exact row.  Endpoint-fixing
automorphisms of the row would be measured by
$\operatorname{Hom}_{\mathrm{Solid}}(\epsilon,\mathbb Q)=0$.

> **Theorem 88a (strict marked rigidity).**
> $\operatorname{Aut}_{C_{\mathbb Z},\mathrm{shear}}(C_{\mathbb Q})=1$, with no
> residual derived automorphisms after the Pass-87 torsion-boundary rule.
>
> **Theorem 88b (extension-line stabilizer).**
> The stabilizer of the finite-adele shear Ext line is $\mathbb Q^\times$.
>
> **Theorem 88c (Borel comparison).**
> The full solid Borel $\mathbb Q^\times\ltimes\epsilon$ is recovered only at
> the hyperbolic-plane level: $\mathbb Q^\times$ is the Levi of the extension
> line and $\epsilon$ is the unipotent shear parameter.

**Machine verification** (`code/scripts/check-pass88.py` ->
`artifacts/reports/pass88-shear-extension-stabilizer-check.json`, PASS):
nonzero rational scalars preserve the extension line, but only scalar $1$
preserves the integral unit marking; finite Borel shadows are
$(\mathbb Z/N)^\times\ltimes\mathbb Z/N$ with singleton strict unit stabilizer;
and no extra derived automorphisms survive for the final $\mathbb Q$-kernel
extension after torsion-boundary decoration.

**Limit of the pass.**  The next task is to turn the Passes 80-88 chain into a
Borel-torsor / extension-class theorem for the Rosser phantom.

## Pass 89 - Borel-torsor theorem for the Rosser phantom

Pass 89 packages the Passes 80-88 automorphic line with the earlier
Loeb/Rosser phantom line.  The main point is that the Rosser non-canonicity is
not merely an analogy with the finite-prime shear class.  In the repository's
APS/Rosser model, it is the same torsor class after passing through the Cech
and finite-adele bridges.

Start with a Guaspari-Solovay witness-comparison Cech cocycle.  Quotienting by
coboundaries gives a class in
$$
\operatorname{coker}\delta\cong
\varprojlim\nolimits^1(\mathbb Z,\times m)
\cong \widehat{\mathbb Z}_m/\mathbb Z.
$$
In the all-prime version this is
$$
\epsilon=\widehat{\mathbb Z}/\mathbb Z.
$$
The finite-adele bridge is the pushout of the integral row
$$
0\to\mathbb Z\to\widehat{\mathbb Z}\to\epsilon\to0
$$
along $\mathbb Z\to\mathbb Q$, giving
$$
0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0.
$$
Thus the Rosser unit-torsor, the integral $\varprojlim^1$ phantom, and the
finite-adele shear extension line are one obstruction read in three
categories.

The Borel comparison from Pass 88 then says exactly how much symmetry remains.
With the integral marking fixed, the object is rigid.  Forgetting the marking
but preserving the extension line leaves the Levi stabilizer
$$
\mathbb Q^\times.
$$
The full solid Borel
$$
\mathbb Q^\times\ltimes\epsilon
$$
appears only after passing to the hyperbolic plane
$$
H=\epsilon\oplus\mathbb Q,
$$
where $\epsilon$ is the unipotent shear parameter.

The invariant data under changing Guaspari-Solovay witness choices are:

- the cohomology class in $\operatorname{coker}\delta$;
- the finite conductor restrictions and radical support;
- the finite-adele extension line;
- the Borel shear orbit, modulo the $\epsilon$ action.

The non-invariant data are the section, the concrete cocycle representative,
the witness enumeration, and the finite-stage Loeb lift.  These are gauge
choices: changing them adds a Cech coboundary but does not change the torsor
class.

> **Theorem 89a (Rosser Borel-torsor theorem).**
> The Rosser unit-torsor, the $\varprojlim^1$ phantom, the finite-adele
> extension line, and the hyperbolic Borel shear orbit are four presentations
> of one torsor/extension class in the APS/Rosser phantom model.
>
> **Theorem 89b (witness-to-adele bridge).**
> The bridge sends a witness-comparison Cech cocycle to its class in
> $\operatorname{coker}\delta$, identifies this with
> $\widehat{\mathbb Z}_m/\mathbb Z$ or $\epsilon$, and pushes out
> $0\to\mathbb Z\to\widehat{\mathbb Z}\to\epsilon\to0$ along
> $\mathbb Z\to\mathbb Q$ to obtain
> $0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0$.
>
> **Theorem 89c (witness-choice invariance).**
> Guaspari-Solovay witness changes alter representatives and sections by
> coboundaries but preserve the torsor class, conductor restrictions, radical
> support, and finite-adele extension line.
>
> **Theorem 89d (Borel level).**
> Strict integral marking is rigid; the extension-line stabilizer is
> $\mathbb Q^\times$; and the full
> $\mathbb Q^\times\ltimes\epsilon$ occurs only in the hyperbolic
> realization.

**Machine verification** (`code/scripts/check-pass89.py` ->
`artifacts/reports/pass89-borel-torsor-rosser-phantom-check.json`, PASS):
finite Cech windows check that changing representative $1$ to $1+m^k$
preserves the class modulo the finite cokernel index $m^k$; finite Borel
shadows have affine size $\varphi(N)N$ with singleton strict marked
stabilizer; and the invariant/non-invariant witness-choice split is recorded
explicitly.

**Limit of the pass.**  The next task is to make the conductor/radical
functoriality of this Borel-torsor theorem precise: compare the $m$-adic
variants, radical-compatible maps, and the all-prime limit in one natural
diagram.

## Pass 90 - Conductor-functorial Borel torsors

Pass 90 resolves the Pass-89 naturality task by correcting the direction of
support functoriality.  The quotient
$$
P(S)=\left(\prod_{p\in S}\mathbb Z_p\right)/\Delta\mathbb Z
$$
is canonical for a finite squarefree support $S$, but maps between these
quotients are not symmetric in the support relation.

If $S\subseteq T$, coordinate projection gives
$$
\rho_{T,S}:P(T)\to P(S).
$$
This is well-defined because a diagonal integer in the larger product projects
to the same diagonal integer in the smaller product.  Hence the canonical
support functor is contravariant by restriction.

The tempting opposite map is not canonical.  Zero-insertion sends
$$
(x_p)_{p\in S}\mapsto (y_p)_{p\in T},\qquad
y_p=x_p\ (p\in S),\quad y_p=0\ (p\in T\setminus S).
$$
If one changes the source representative by the diagonal integer $1$, the
inserted vector changes by $(1,\ldots,1,0,\ldots,0)$, not by a diagonal vector
in the target.  Thus zero-insertion does not descend to
$P(S)\to P(T)$ whenever new primes are added.  Any enlargement of support must
be read as a span, a chosen section, or a finite-conductor lift.

For rad-incomparable supports the comparison is similarly span-shaped.  The
shared ghost is controlled by the meet:
$$
P(S)\to P(S\cap T)\leftarrow P(T),
$$
while gluing is tested in the join arena $P(S\cup T)$ by restricting back to
$S$ and $T$.  This keeps the Pass-60 radical lattice but removes the misleading
impression that the quotient torsors carry canonical coordinate insertions.

The finite Borel side remains straightforward.  At conductor $N$ the shadow is
$$
B_N=(\mathbb Z/N)^\times\ltimes\mathbb Z/N.
$$
For $N\mid N'$, reduction gives
$$
B_{N'}\to B_N,
$$
preserving the unit class $1\bmod N$ and the singleton strict marked
stabilizer.  Therefore the Pass-89 Borel-torsor theorem is functorial on
finite conductor shadows and on support restrictions, with support
enlargement handled by spans.

> **Theorem 90a (support restriction).**
> For $S\subseteq T$, projection induces a well-defined restriction
> $P(T)\to P(S)$ on diagonal quotient torsors.
>
> **Theorem 90b (no canonical zero insertion).**
> If $S\ne\varnothing$ and $T\setminus S\ne\varnothing$, zero-insertion does
> not descend to a homomorphism $P(S)\to P(T)$.
>
> **Theorem 90c (finite-conductor Borel naturality).**
> The finite affine Borel shadows $B_N$ reduce functorially along
> conductor divisibility, preserving the unit class and strict marked
> stabilizer.
>
> **Theorem 90d (meet/join comparison).**
> Rad-incomparable supports are compared by the meet span for shared ghost
> data and by the join arena for gluing.

**Machine verification** (`code/scripts/check-pass90.py` ->
`artifacts/reports/pass90-conductor-functorial-borel-torsors-check.json`,
PASS): the checker verifies radical support invariance, checks that
projection descends through the diagonal quotient while zero-insertion fails
when a new prime is added, records meet/join comparison rows, and verifies
finite Borel reductions along conductor divisibility.

**Limit of the pass.**  The next task is to decide the correct descent
language for this object: sheaf, stack, prestack, or descent-obstruction
object over the finite prime-cover site.

## Pass 91 - Borel torsor descent obstruction

Pass 91 answers the descent-language question from Pass 90.  On the finite
singleton-prime cover site, the Borel package is not a sheaf on multi-prime
supports.  It is a prestack/descent-obstruction object whose stackification is
the local Loeb object.

Let
$$
P(S)=\left(\prod_{p\in S}\mathbb Z_p\right)/\Delta\mathbb Z.
$$
Pass 61 already computed the singleton-cover descent defect:
$$
\ker\left(P(S)\to\prod_{p\in S}P(\{p\})\right)
\cong \mathbb Z^S/\Delta\mathbb Z
\cong \mathbb Z^{|S|-1}.
$$
This is the horizontal Rosser defect.  Adding the Borel does not eliminate it.
The global-Levi Borel prestack is
$$
B^{\mathrm{glob}}(S)=\mathbb Q^\times\ltimes P(S).
$$
It has the same unipotent descent kernel, and its constant Levi
$\mathbb Q^\times$ sheafifies on the singleton cover to independent local
Levi factors.

Thus the sheafification or stackification is the local Borel object
$$
B^\#(S)=(\mathbb Q^\times)^S\ltimes
\prod_{p\in S}(\mathbb Z_p/\mathbb Z).
$$
This is the Loeb-local object: it keeps stalkwise ghosts and local scalars but
forgets the horizontal Rosser kernel.  The map
$B^{\mathrm{glob}}\to B^\#$ therefore loses exactly the obstruction that made
the Rosser torsor nonlocal.

The hyperbolic shear action clarifies, rather than removes, the defect.  In
finite shadows the kernel has size $N^{|S|-1}$, and the unipotent shear orbit
on lifts with fixed local data has the same size.  So shear acts transitively
on choices of global lift.  But transitivity is not a canonical section:
without choosing a basepoint, the action transports the Rosser defect instead
of killing it.

> **Theorem 91a (Borel non-separatedness).**
> For $|S|\ge2$, the global-Levi Borel prestack
> $B^{\mathrm{glob}}(S)=\mathbb Q^\times\ltimes P(S)$ is not a sheaf on the
> singleton-prime cover.  Its unipotent descent kernel is
> $\mathbb Z^S/\Delta\mathbb Z$.
>
> **Theorem 91b (local Borel sheafification).**
> The sheafification/stackification on the discrete prime-cover site is
> $$B^\#(S)=(\mathbb Q^\times)^S\ltimes
> \prod_{p\in S}(\mathbb Z_p/\mathbb Z).$$
> It is the local Loeb object, not the global Rosser phantom.
>
> **Theorem 91c (shear transports the defect).**
> The unipotent shear action is simply transitive on finite descent-kernel
> lift sets, but it does not choose a canonical zero section.  Hence it
> preserves the Rosser defect as the kernel of stackification.
>
> **Corollary 91d (discrete-site verdict).**
> On the finite discrete prime-cover site, the Borel torsor is a
> prestack/descent-obstruction object.  A geometric home for the Rosser class
> must use the Zariski/generic-point relocation of Pass 63.

**Machine verification** (`code/scripts/check-pass91.py` ->
`artifacts/reports/pass91-borel-torsor-descent-obstruction-check.json`,
PASS): the checker verifies descent rank $|S|-1$, finite diagonal-kernel size
$N^{|S|-1}$, failure of the global Borel to be a sheaf for multi-prime
supports, local-Levi sheafification in a finite constant-group proxy, and the
fact that shear transports but does not kill descent-kernel lifts.

**Limit of the pass.**  The next task is to move from the disconnected
finite prime-cover site to the Zariski/generic-point site and compare the
Borel descent obstruction with the Pass-63 $j_!$ ghost line.

## Pass 92 - Zariski/generic Borel descent

Pass 92 relocates the Pass-91 discrete-site Borel defect to the
Zariski/generic-point site used in Pass 63.  The crucial correction is that the
constant Borel sheaf is no longer the defective object.  The site
$$
X_S=\{\eta\}\cup\{(p):p\in S\}
$$
is connected, and the cover by minimal opens $U_p=\{\eta,(p)\}$ has full-simplex
nerve.  Hence constant coefficients have no horizontal $H^1$ defect.

The Rosser/Borel obstruction is instead the unipotent $j_!$ class.  Let
$j:\{\eta\}\hookrightarrow X_S$ be the open generic point.  The boundary
sequence
$$
0\to j_!\underline{\mathbb Z}\to\underline{\mathbb Z}_{X_S}
\to i_*\underline{\mathbb Z}_{S}\to0
$$
gives
$$
H^1(X_S,j_!\underline{\mathbb Z})
\cong \operatorname{coker}(\Delta:\mathbb Z\to\mathbb Z^S)
\cong \mathbb Z^S/\Delta\mathbb Z
\cong \mathbb Z^{|S|-1}.
$$
This is the same group as the Pass-91 discrete descent kernel, but now it is a
genuine cohomology group supported at the generic point.

The Borel analogue of the Pass-63 ghost line is therefore the low-degree
semidirect coefficient
$$
\mathfrak b_{j!}(S)=\underline{\mathbb Q^\times}\ltimes
j_!\underline{\mathbb Z}.
$$
The Levi part $\mathbb Q^\times$ remains degree-$0$ global data on the connected
site, while the unipotent radical carries the $j_!$ cohomology.  Modulo $N$ the
same computation gives
$$
|H^1(X_S,j_!\mathbb Z/N)|=N^{|S|-1},
$$
matching the finite diagonal kernel size from Pass 91.

With the dilation coefficient $\mathcal V$, this horizontal group is the free
part of the total phantom:
$$
H^1(X_S,j_!\mathcal V)\cong\widehat{\mathbb Z}_S/\mathbb Z.
$$
Pushing out the integral row along $\mathbb Z\to\mathbb Q$ gives the finite-adele
extension line, while the hyperbolic Borel
$\mathbb Q^\times\ltimes\epsilon$ reads the same datum as a shear orbit.  The
Levi rescales classes; shear changes representatives.  Neither operation
selects a canonical zero section.

> **Theorem 92a (Zariski relocation of the Borel defect).**
> On $X_S$, constant coefficients have no horizontal $H^1$ defect, while
> $$H^1(X_S,j_!\underline{\mathbb Z})\cong
> \mathbb Z^S/\Delta\mathbb Z.$$
> This is the Zariski relocation of the Pass-91 discrete descent kernel.
>
> **Theorem 92b (Borel $j_!$ ghost coefficient).**
> The finite-support Borel ghost coefficient is
> $$\mathfrak b_{j!}(S)=\underline{\mathbb Q^\times}\ltimes
> j_!\underline{\mathbb Z}.$$
> The Levi stays in degree $0$; the unipotent radical carries the Rosser class
> in $H^1$.
>
> **Theorem 92c (finite shadows).**
> For every $N\ge2$,
> $$|H^1(X_S,j_!\mathbb Z/N)|=N^{|S|-1}.$$
>
> **Theorem 92d (finite-adele and Borel-shear comparison).**
> The horizontal $j_!$ ghost injects into
> $H^1(X_S,j_!\mathcal V)\cong\widehat{\mathbb Z}_S/\mathbb Z$; the
> pushout/localization along $\mathbb Z\to\mathbb Q$ gives the finite-adele
> extension line, and the hyperbolic Borel realizes the same datum as a shear
> orbit without a canonical splitting.

**Machine verification** (`code/scripts/check-pass92.py` ->
`artifacts/reports/pass92-zariski-generic-borel-descent-check.json`, PASS):
the checker verifies constant-coefficient vanishing, $j_!$ rank $|S|-1$,
finite mod-$N$ class size $N^{|S|-1}$, the degree-$0$ Levi / degree-$1$
unipotent split, and the comparison with the total phantom, finite-adele
pushout, and hyperbolic Borel shear orbit.

**Limit of the pass.**  The next task is to upgrade this finite-support
$j_!$ Borel class to the honest all-prime $\mathrm{Spec}\,\mathbb Z$ site and
state the required finiteness, continuity, or derived-completion hypotheses.

## Pass 93 - All-prime Spec Z Borel j_! upgrade

Pass 93 upgrades the finite-support Pass-92 computation to the honest
all-prime $\mathrm{Spec}\,\mathbb Z$ site.  The first point is negative:
the generic singleton is not open in $\mathrm{Spec}\,\mathbb Z$.  Every
nonempty basic open $D(n)$ contains $\eta$ and all but finitely many closed
primes.  Thus the notation $j_!$ is literal on each finite subspace
$X_S=\{\eta\}\cup S$, but all-prime it must mean a pro-open, continuous, or
solid coefficient built from the finite-support system.

Define the all-prime Borel coefficient as
$$
\mathfrak B^{\mathrm{cont}}_{j!}
=\mathbb Q^\times\ltimes
R\!\varprojlim_{S\Subset\mathbb P}j_{S,!}\mathcal V_S,
$$
where $\mathcal V_S$ is the dilation coefficient from Pass 64.  The transition
maps are restrictions from larger finite support to smaller finite support.
For the horizontal integer skeleton, if $S\subseteq T$ then
$$
\mathbb Z^T/\Delta\mathbb Z\to\mathbb Z^S/\Delta\mathbb Z
$$
is surjective with kernel of rank $|T|-|S|$; modulo $N$, the kernel has size
$N^{|T|-|S|}$.  Hence the support direction is Mittag-Leffler and contributes
no new $\varprojlim^1$.

The derived content is still exactly the per-prime dilation system inside
$\mathcal V$.  Therefore the all-prime statement is
$$
H^1_{\mathrm{cont}}(\mathrm{Spec}\,\mathbb Z,j_!\mathcal V)
:=\varprojlim_{S\Subset\mathbb P}H^1(X_S,j_{S,!}\mathcal V_S)
\cong
\left(\prod_p\mathbb Z_p\right)/\Delta\mathbb Z
=\widehat{\mathbb Z}/\mathbb Z.
$$

The global Levi remains a single $\mathbb Q^\times$.  Passing instead to
local Levi data $\prod_p\mathbb Q^\times$ would repeat the local Loeb
sheafification of Pass 91 and erase the Rosser torsor.  With the global Levi
kept, the finite-adele pushout
$$
0\to\mathbb Q\to\mathbb A_f\to\widehat{\mathbb Z}/\mathbb Z\to0
$$
and the hyperbolic Borel shear orbit are functorial all-prime forms of the
same continuous class.

> **Theorem 93a (no ordinary all-prime generic $j_!$).**
> In honest $\mathrm{Spec}\,\mathbb Z$, $\{\eta\}$ is not open.  The all-prime
> Borel $j_!$ coefficient is therefore not an ordinary sheaf obtained from an
> open generic-point inclusion.
>
> **Theorem 93b (continuous/pro-open Borel coefficient).**
> The all-prime coefficient is
> $$\mathfrak B^{\mathrm{cont}}_{j!}
> =\mathbb Q^\times\ltimes
> R\!\varprojlim_{S\Subset\mathbb P}j_{S,!}\mathcal V_S.$$
>
> **Theorem 93c (support ML).**
> Finite-support restriction maps are surjective; horizontally their kernels
> have rank $|T|-|S|$, and modulo $N$ size $N^{|T|-|S|}$.  The support
> direction contributes no extra $\varprojlim^1$.
>
> **Theorem 93d (all-prime Borel identity).**
> $$H^1_{\mathrm{cont}}(\mathrm{Spec}\,\mathbb Z,j_!\mathcal V)
> \cong\widehat{\mathbb Z}/\mathbb Z.$$
> The finite-adele extension row and the hyperbolic Borel shear orbit are the
> pushout and representation-theoretic presentations of this same class.

**Machine verification** (`code/scripts/check-pass93.py` ->
`artifacts/reports/pass93-all-prime-borel-jshriek-upgrade-check.json`, PASS):
the checker records the finite/all-prime open-point distinction, verifies
surjective support projections and finite mod-$N$ kernel sizes, confirms
support-direction ML/no extra $\varprojlim^1$, and records the all-prime
global-Levi Borel coefficient with unipotent limit $\widehat{\mathbb Z}/\mathbb Z$.

**Limit of the pass.**  The next task is to compute the Verdier/solid dual of
this continuous Borel $j_!$ coefficient and decide whether the antipode sign
gives a functional-equation shadow without producing a forbidden Weyl flip.

## Pass 94 - Solid dual of the all-prime Borel $j_!$ class

Pass 94 computes the dual requested at the end of Pass 93.  The all-prime
unipotent class is
$$
\epsilon=\widehat{\mathbb Z}/\mathbb Z.
$$
By the solid duality computation of Passes 77--79,
$$
D\epsilon\simeq\mathbb Q[-1],
\qquad
D\mathbb Q\simeq\epsilon[-1].
$$
Therefore the dual of the all-prime Borel $j_!$ coefficient is not an opposite
Borel group in degree $0$.  It is a Levi-marked boundary object: the global
Levi $\mathbb Q^\times$ remains, while the unipotent dual is the shifted
boundary $\mathbb Q[-1]$ with contragredient Levi action.

This is exactly the all-prime continuation of the finite signed Verdier rule.
For a finite support $S$, let
$$
d_S:\mathbb Z^S\to\mathbb Z^{|S|-1},
\qquad
(x_p)\mapsto(x_p-x_{p_0})_{p\ne p_0}.
$$
Finite Verdier duality sends
$$
d_S\longmapsto -d_S^T,
\qquad
D^2(d_S)=d_S.
$$
The sign is a genuine integral orientation datum, although it collapses modulo
$2$.

All-prime, this becomes the antipode sign on the solid bidual:
$$
\eta_\epsilon=-\mathrm{id}_\epsilon.
$$
The surviving object that replaces the finite Fourier/Weyl flip is the
degree-$1$ finite-adele boundary
$$
0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0,
$$
or equivalently the class in
$$
\operatorname{Ext}^1_{\mathrm{Solid}}(\epsilon,\mathbb Q).
$$
This is a functional-equation shadow only in the boundary sense.

The no-flip wall remains intact:
$$
\operatorname{Hom}^0_{\mathrm{Solid}}(\epsilon,\mathbb Q)=0.
$$
Thus there is still no opposite unipotent, no standard intertwiner, and no
degree-$0$ Weyl/Fourier operator.  The phrase "functional equation" is
therefore safe only when it means signed boundary duality, not an actual
$s\mapsto -s$ operator on a solid principal series.

> **Theorem 94a (all-prime solid dual).** For the unipotent limit
> $\epsilon=\widehat{\mathbb Z}/\mathbb Z$ of
> $\mathfrak B^{\mathrm{cont}}_{j!}$, one has
> $$D\epsilon\simeq\mathbb Q[-1].$$
>
> **Theorem 94b (signed finite shadows).** Finite recollement boundaries obey
> $$D(d_S)=-d_S^T,\qquad D^2(d_S)=d_S,$$
> with sign visible over $\mathbb Z$ and invisible modulo $2$.
>
> **Theorem 94c (boundary-only functional equation).** The Pass-65/77 sign
> survives all-prime as $\eta_\epsilon=-\mathrm{id}_\epsilon$, represented by
> the degree-$1$ finite-adele boundary
> $0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0$.
>
> **Theorem 94d (no Weyl flip).**
> $\operatorname{Hom}^0_{\mathrm{Solid}}(\epsilon,\mathbb Q)=0$, so the dual
> boundary does not create an opposite Borel or a standard Weyl/Fourier
> intertwiner.

**Machine verification** (`code/scripts/check-pass94.py` ->
`artifacts/reports/pass94-all-prime-borel-jshriek-solid-dual-check.json`, PASS):
finite boundary matrices satisfy the signed transpose rule, rank preservation,
duality squared, and mod-$2$ sign collapse; support restriction dualizes from
surjections to injections without creating a degree-$0$ flip; the all-prime
solid row records $D\epsilon=\mathbb Q[-1]$, the finite-adele boundary, the
biduality sign $-1$, and the absence of a degree-$0$ Weyl map.

**Limit of the pass.**  The next task is to package this boundary-shadow
functional equation as a constant-term or two-term Borel complex natural under
conductor restriction, while keeping the no-Weyl-flip wall explicit.

## Pass 95 - Boundary-only Borel constant-term complex

Pass 95 packages the boundary-shadow functional equation from Pass 94 as an
actual two-term complex.  The object is
$$
C_B=\mathbb Q^\times\ltimes[\mathbb Q\to\mathbb A_f],
$$
in cohomological degrees $0\to1$.  The map is the diagonal inclusion
$\mathbb Q\hookrightarrow\mathbb A_f$, and the global Levi $\mathbb Q^\times$
acts by scalar multiplication on both terms.

The all-prime solid cohomology is
$$
H^0(C_B)=0,\qquad
H^1(C_B)=\mathbb A_f/\mathbb Q\cong
\widehat{\mathbb Z}/\mathbb Z=\epsilon.
$$
Thus $C_B$ is the constant-term carrier of the Pass-94 boundary sign.  It is
not a principal-series intertwiner and not an opposite Borel.

At finite conductor $N$, the shadow is
$$
C_{B,N}=(\mathbb Z/N)^\times\ltimes
\left[\mathbb Z/N\to\prod_{p^e\parallel N}\mathbb Z/p^e\right].
$$
The diagonal is an isomorphism by CRT, so each fixed finite conductor shadow
is ordinary-acyclic:
$$
H^0(C_{B,N})=H^1(C_{B,N})=0.
$$
This explains why the phantom boundary is liman: finite stages see no
ordinary cokernel, while the solid all-prime limit retains
$\epsilon$.

The naturality has two different directions.  If $N\mid M$, conductor
reduction gives a commuting square of two-term complexes and preserves the
Borel unit class.  If $S\subseteq T$ are finite supports, projection
$T\to S$ is canonical.  But support enlargement $S\to T$ is not a canonical
all-prime map: at each finite conductor CRT can produce a lift with residues
$1$ on $S$ and $0$ on $T\setminus S$, but the exact idempotent vector is not a
diagonal integer in $\prod_{p\in T}\mathbb Z_p$.  So enlargement remains a
span or finite-conductor choice.

The result is a precise "functional equation without Weyl operator":
the signed boundary and constant term survive, but nontrivial Whittaker
coefficients and the standard Weyl/Fourier intertwiner remain absent.

> **Theorem 95a (constant-term complex).** The Borel boundary package is
> $$C_B=\mathbb Q^\times\ltimes[\mathbb Q\to\mathbb A_f],$$
> with $H^1(C_B)\cong\epsilon$ in the all-prime solid boundary.
>
> **Theorem 95b (finite conductor acyclicity).** For every conductor $N$,
> $$\mathbb Z/N\to\prod_{p^e\parallel N}\mathbb Z/p^e$$
> is an isomorphism.  Hence fixed finite conductor shadows of $C_B$ are
> ordinary-acyclic.
>
> **Theorem 95c (naturality).** Conductor reductions commute with the
> two-term diagonal complex and preserve the Borel unit.  Support projection
> is canonical; support enlargement is only a span or finite-conductor CRT
> choice.
>
> **Theorem 95d (no-Weyl constant term).** $C_B$ is a constant-term
> functional-equation shadow.  It has no nontrivial Whittaker component and no
> standard Weyl/Fourier intertwiner.

**Machine verification** (`code/scripts/check-pass95.py` ->
`artifacts/reports/pass95-boundary-only-borel-constant-term-complex-check.json`,
PASS): finite conductor complexes are CRT-isomorphism complexes; conductor
reduction squares commute and preserve the Borel unit; support projection
commutes while zero-insertion is only a finite CRT choice and not an exact
all-prime diagonal-preserving map; and the constant-term row records
$C_B=\mathbb Q^\times\ltimes[\mathbb Q\to\mathbb A_f]$ with solid
$H^1=\epsilon$, no nontrivial Whittaker coefficient, and no standard Weyl
intertwiner.

**Limit of the pass.**  The next task is to compare $C_B$ with the local Loeb
sheafification
$$
(\mathbb Q^\times)^S\ltimes\prod_{p\in S}(\mathbb Z_p/\mathbb Z)
$$
and identify exactly which kernel is lost when global Levi data are replaced
by local Levi data.

## Pass 96 - Constant-term complex versus local Loebification

Pass 96 compares the Pass-95 constant-term complex with the local Loeb object
from Pass 91.  The comparison is clearest on the compact finite-support
skeleton.  For finite support $S$, define
$$
C_B^{\mathrm{int}}(S)
=\mathbb Q^\times\ltimes
\left[\mathbb Z\to\prod_{p\in S}\mathbb Z_p\right]
$$
with $\mathbb Z$ embedded diagonally.  The local Loebified complex is
$$
C_L(S)=(\mathbb Q^\times)^S\ltimes
\left[\mathbb Z^S\to\prod_{p\in S}\mathbb Z_p\right],
$$
where $\mathbb Z^S$ maps coordinatewise.

There is a canonical map
$$
\alpha_S:C_B^{\mathrm{int}}(S)\to C_L(S)
$$
given by diagonal Levi, diagonal degree-$0$ unipotent, and identity on the
degree-$1$ compact adele product.  Hence the unipotent comparison on
cohomology is
$$
(\prod_{p\in S}\mathbb Z_p)/\Delta\mathbb Z
\to
\prod_{p\in S}(\mathbb Z_p/\mathbb Z).
$$
Its exact kernel is
$$
K_S=\mathbb Z^S/\Delta\mathbb Z\cong\mathbb Z^{|S|-1},
$$
so
$$
0\to K_S\to(\prod_{p\in S}\mathbb Z_p)/\Delta\mathbb Z\to
\prod_{p\in S}(\mathbb Z_p/\mathbb Z)\to0.
$$
Modulo $N$, this kernel has size $N^{|S|-1}$; it vanishes for singleton
supports and appears exactly when there is a multi-prime horizontal descent
defect.

The Levi comparison is not a kernel computation.  The diagonal map
$$
\mathbb Q^\times\to(\mathbb Q^\times)^S
$$
is injective.  What local Loebification forgets is the global coherence
condition tying the local Levi factors together, measured by
$$
\Lambda_S=(\mathbb Q^\times)^S/\Delta\mathbb Q^\times.
$$
In a finite constant-group proxy $G$, the corresponding quotient has size
$|G|^{|S|-1}$.

> **Theorem 96a (two-term comparison).** The map from global constant-term
> data to local Loeb data is the two-term complex map
> $$[\mathbb Z\to\prod_{p\in S}\mathbb Z_p]\to
> [\mathbb Z^S\to\prod_{p\in S}\mathbb Z_p],$$
> diagonal in degree $0$ and identity in degree $1$.
>
> **Theorem 96b (unipotent kernel lost by Loebification).**
> The kernel of the induced $H^1$ map is
> $$K_S=\mathbb Z^S/\Delta\mathbb Z.$$
>
> **Theorem 96c (finite shadow size).**
> At finite level $N$, the lost unipotent kernel has size $N^{|S|-1}$.
>
> **Theorem 96d (Levi quotient, not Levi kernel).**
> The diagonal Levi map has trivial kernel.  The new local Levi freedom is
> the quotient $(\mathbb Q^\times)^S/\Delta\mathbb Q^\times$.
>
> **Theorem 96e (formulation).**
> The comparison is a map of two-term complexes plus stackification/local
> constant-term projection.  Pure Hausdorff reflection captures only the
> unipotent quotient.

**Machine verification** (`code/scripts/check-pass96.py` ->
`artifacts/reports/pass96-constant-term-local-loebification-check.json`,
PASS): the checker verifies the rank $|S|-1$ kernel of the complex map,
finite sizes $N^{|S|-1}$, singleton vanishing, multi-prime nontriviality,
triviality of the Levi kernel, and the finite-proxy local Levi quotient size
$|G|^{|S|-1}$.

**Limit of the pass.**  The next task is to lift this compact comparison to
the full finite-adele row $[\mathbb Q\to\mathbb A_f]$ and decide whether
rationalization kills, regrades, or turns the free kernel
$\mathbb Z^S/\Delta\mathbb Z$ into $\mathbb Q^S/\Delta\mathbb Q$ boundary
data.

## Pass 97 - Rationalized finite-adele row

Pass 97 lifts the compact comparison from Pass 96 to the rationalized
finite-adele skeleton.  For finite support $S$, the map is
$$
[\mathbb Q\to\prod_{p\in S}\mathbb Q_p]\to
[\mathbb Q^S\to\prod_{p\in S}\mathbb Q_p],
$$
with diagonal degree $0$ and identity in degree $1$.  On $H^1$ this gives
$$
(\prod_{p\in S}\mathbb Q_p)/\Delta\mathbb Q
\to
\prod_{p\in S}(\mathbb Q_p/\mathbb Q).
$$
The kernel is
$$
K_{\mathbb Q,S}=\mathbb Q^S/\Delta\mathbb Q.
$$

Thus rationalization does not eliminate the Pass-96 kernel
$$
K_{\mathbb Z,S}=\mathbb Z^S/\Delta\mathbb Z.
$$
Instead, it embeds $K_{\mathbb Z,S}$ into the divisible
$\mathbb Q$-vector boundary $K_{\mathbb Q,S}$, with the same rank/dimension
$|S|-1$.

The finite shadow changes location.  Because $K_{\mathbb Q,S}$ is divisible,
$$
K_{\mathbb Q,S}/N K_{\mathbb Q,S}=0.
$$
But
$$
K_{\mathbb Q,S}/K_{\mathbb Z,S}
\cong
(\mathbb Q/\mathbb Z)^S/\Delta(\mathbb Q/\mathbb Z)
$$
has $N$-torsion of size $N^{|S|-1}$.  So the old finite kernel shadow is not
destroyed; it is regraded into $\mathbb Q/\mathbb Z$ torsion.

Support behavior remains controlled.  If $S\subseteq T$, then projection
$$
K_{\mathbb Q,T}\to K_{\mathbb Q,S}
$$
is surjective, with kernel of $\mathbb Q$-dimension $|T|-|S|$.  Hence the
support inverse direction remains Mittag-Leffler after rationalization.

> **Theorem 97a (rationalized comparison).** The finite-support rationalized
> Loebification map is
> $$[\mathbb Q\to\prod_{p\in S}\mathbb Q_p]\to
> [\mathbb Q^S\to\prod_{p\in S}\mathbb Q_p].$$
>
> **Theorem 97b (rational kernel survives).** The $H^1$ kernel is
> $$K_{\mathbb Q,S}=\mathbb Q^S/\Delta\mathbb Q,$$
> and $K_{\mathbb Z,S}$ injects into it.
>
> **Theorem 97c (finite shadow regrading).** For $N\ge2$,
> $$K_{\mathbb Q,S}/N K_{\mathbb Q,S}=0,$$
> while
> $$|(K_{\mathbb Q,S}/K_{\mathbb Z,S})[N]|=N^{|S|-1}.$$
>
> **Theorem 97d (support Mittag-Leffler after rationalization).** For
> $S\subseteq T$, the map $K_{\mathbb Q,T}\to K_{\mathbb Q,S}$ is surjective
> with kernel dimension $|T|-|S|$.
>
> **Theorem 97e (all-prime reading).** The all-prime rationalized comparison
> should be treated as a filtered support comparison with finite shadows
> regraded into $\mathbb Q/\mathbb Z$ torsion, not as a pure finite quotient
> calculation.

**Machine verification** (`code/scripts/check-pass97.py` ->
`artifacts/reports/pass97-rationalized-finite-adele-row-check.json`, PASS):
the checker verifies the dimension of $K_{\mathbb Q,S}$, injectivity of
$K_{\mathbb Z,S}\to K_{\mathbb Q,S}$, vanishing of finite quotients of the
divisible rational kernel, recovery of $N^{|S|-1}$ as torsion in
$K_{\mathbb Q,S}/K_{\mathbb Z,S}$, and support-projection surjectivity.

**Limit of the pass.**  The next task is to compare the torsion boundary
$(\mathbb Q/\mathbb Z)^S/\Delta(\mathbb Q/\mathbb Z)$ with the solid dual
$D\epsilon=\mathbb Q[-1]$ and decide whether they are two presentations of
the same shifted constant-term obstruction.

## Pass 98 - Torsion boundary versus solid dual

Pass 98 compares the regraded torsion boundary from Pass 97,
$$
T_S=(\mathbb Q/\mathbb Z)^S/\Delta(\mathbb Q/\mathbb Z)
\cong K_{\mathbb Q,S}/K_{\mathbb Z,S},
$$
with the all-prime solid-dual identity from Pass 94,
$$
D\epsilon\simeq\mathbb Q[-1],
\qquad
\epsilon=\widehat{\mathbb Z}/\mathbb Z.
$$

The first correction is degree-theoretic.  The torsion boundary $T_S$ is a
degree-$0$ torsion coefficient.  The solid dual $D\epsilon$ is shifted.  Thus
one should not identify
$$
(\mathbb Q/\mathbb Z)^S/\Delta(\mathbb Q/\mathbb Z)
$$
with $\mathbb Q[-1]$ as raw objects.

The bridge is the canonical unit extension
$$
0\to\mathbb Z\to\mathbb Q\to\mathbb Q/\mathbb Z\to0.
$$
Each independent $\mathbb Q/\mathbb Z$ coordinate in $T_S$ classifies one copy
of this extension.  Applying the extension/solid-dual passage sends this
coordinate to a shifted $\mathbb Q[-1]$ constant-term obstruction generator.
Since
$$
T_S\cong(\mathbb Q/\mathbb Z)^{|S|-1},
$$
the finite-support boundary presents $|S|-1$ copies of the generator before
any all-prime collapse or choice of a single boundary relation.

For finite level $N$,
$$
|T_S[N]|=N^{|S|-1}.
$$
This recovers the Pass-96 compact finite shadow, while
$K_{\mathbb Q,S}/N K_{\mathbb Q,S}=0$ because $K_{\mathbb Q,S}$ is divisible.
For $S\subseteq T$, the projection $T_T\to T_S$ is surjective and its
$N$-torsion kernel has size $N^{|T|-|S|}$, so the support direction remains
Mittag-Leffler at the torsion-boundary level.

> **Theorem 98a (torsion shadow).** The boundary
> $T_S=(\mathbb Q/\mathbb Z)^S/\Delta(\mathbb Q/\mathbb Z)$ has
> $|T_S[N]|=N^{|S|-1}$.
>
> **Theorem 98b (no raw equality).** $T_S$ is not literally the solid dual
> $D\epsilon\simeq\mathbb Q[-1]$; the comparison requires the degree shift.
>
> **Theorem 98c (extension bridge).** The exact bridge from finite torsion
> boundary to solid dual is the canonical extension
> $0\to\mathbb Z\to\mathbb Q\to\mathbb Q/\mathbb Z\to0$ followed by the
> solid-dual shift.  Each independent $\mathbb Q/\mathbb Z$ coordinate
> presents one shifted $\mathbb Q[-1]$ obstruction generator.
>
> **Theorem 98d (no-Weyl compatibility).** The bridge does not produce a
> degree-$0$ map $\epsilon\to\mathbb Q$; it is compatible with the Pass-94
> no-Weyl wall.

**Machine verification** (`code/scripts/check-pass98.py` ->
`artifacts/reports/pass98-torsion-boundary-solid-dual-check.json`, PASS):
the checker verifies the $N^{|S|-1}$ torsion counts, their equality with the
compact finite shadow, vanishing of divisible rational mod-$N$ quotients,
support-projection surjectivity, non-equality of raw torsion and shifted solid
dual objects, and compatibility with the extension bridge/no-Weyl wall.

**Limit of the pass.**  The next task is to construct the exact triangle or
functor from finite-support torsion boundaries to the all-prime constant-term
complex and check compatibility with the Pass-94 antipode sign.

## Pass 99 - Primitive-collapse bridge to the constant-term complex

Pass 99 constructs the promised bridge from finite torsion boundary to the
all-prime constant-term complex.  The canonical finite-support triangle is
$$
K_{\mathbb Z,S}\to K_{\mathbb Q,S}\to T_S\to K_{\mathbb Z,S}[1],
$$
where
$$
K_{\mathbb Z,S}=\mathbb Z^S/\Delta\mathbb Z,\qquad
K_{\mathbb Q,S}=\mathbb Q^S/\Delta\mathbb Q,\qquad
T_S=(\mathbb Q/\mathbb Z)^S/\Delta(\mathbb Q/\mathbb Z).
$$

A collapse from the $|S|-1$-generator torsion boundary to the one-generator
unit extension is not canonical.  It is determined by a zero-sum functional
$$
c=(c_p)_{p\in S}\in\mathbb Z^S,\qquad \sum_{p\in S}c_p=0.
$$
This condition is exactly what makes $c$ vanish on the diagonal and hence
descend to
$$
K_{\mathbb Z,S}\to\mathbb Z,\qquad
K_{\mathbb Q,S}\to\mathbb Q,\qquad
T_S\to\mathbb Q/\mathbb Z.
$$
The last map is surjective precisely when $c$ is primitive:
$$
\gcd_{p\in S}(c_p)=1.
$$

Thus a primitive $c$ gives a morphism of exact triangles
$$
\begin{array}{ccc}
K_{\mathbb Z,S} &\to& K_{\mathbb Q,S} &\to& T_S\\
\downarrow && \downarrow && \downarrow\\
\mathbb Z &\to& \mathbb Q &\to& \mathbb Q/\mathbb Z.
\end{array}
$$
Composing with the all-prime finite-adele realization gives the constant-term
complex
$$
[\mathbb Q\to\mathbb A_f],
\qquad
H^1=\epsilon=\mathbb A_f/\mathbb Q.
$$

For $r=|S|-1$ and finite level $N$, the primitive collapse satisfies
$$
T_S[N]\twoheadrightarrow(\mathbb Q/\mathbb Z)[N],
\qquad
|\ker|=N^{r-1}=N^{|S|-2}.
$$
Hence the bridge preserves the one-generator finite shadow while recording
the remaining $|S|-2$ finite-support degrees as the kernel of the chosen
collapse.

The canonicality warning is essential.  A support-symmetric collapse would
come from a symmetric integral functional, hence from a constant vector
$(a,\ldots,a)$; the zero-sum condition forces $a=0$.  Therefore the operation
which collapses $T_S$ to one constant-term generator is not a plain support
limit.  It is a torsor of primitive boundary orientations.

The antipode sends $c$ to $-c$, so it negates the chosen boundary class.  This
is the same sign behavior as Pass 94: visible over $\mathbb Z$, invisible mod
$2$, and shifted through $D\epsilon\simeq\mathbb Q[-1]$.  No degree-$0$ Weyl
or Fourier morphism $\epsilon\to\mathbb Q$ is produced.

> **Theorem 99a (finite triangle).** The inclusion
> $K_{\mathbb Z,S}\hookrightarrow K_{\mathbb Q,S}$ gives the exact triangle
> $K_{\mathbb Z,S}\to K_{\mathbb Q,S}\to T_S\to K_{\mathbb Z,S}[1]$.
>
> **Theorem 99b (primitive collapse).** A morphism to
> $\mathbb Z\to\mathbb Q\to\mathbb Q/\mathbb Z$ is determined by an integral
> zero-sum functional $c$ and is surjective on the torsion boundary exactly
> when $c$ is primitive.
>
> **Theorem 99c (orientation torsor).** There is no canonical
> support-symmetric primitive collapse $T_S\to\mathbb Q/\mathbb Z$; the
> collapse data form an orientation torsor of primitive zero-sum functionals.
>
> **Theorem 99d (constant-term compatibility).** After choosing $c$, the
> bridge lands in $[\mathbb Q\to\mathbb A_f]$, the antipode sends
> $c\mapsto -c$, and the construction remains compatible with the no-Weyl wall.

**Machine verification** (`code/scripts/check-pass99.py` ->
`artifacts/reports/pass99-torsion-boundary-constant-term-triangle-check.json`,
PASS): the checker verifies descent and surjectivity of primitive zero-sum
functionals, finite-shadow kernel size $N^{|S|-2}$, antipode sign behavior,
noncanonicity of the collapse, and compatibility with the shifted
constant-term target.

**Limit of the pass.**  The next task is to study the orientation torsor of
primitive zero-sum boundary functionals under support inclusions and decide
which transition maps preserve, negate, or destabilize chosen collapses.

## Pass 100 - Orientation torsor under support functoriality

Pass 100 studies the collapse choices introduced in Pass 99.  For a finite
support $S$ with $|S|\ge2$, define
$$
\mathcal O_S=
\{c=(c_p)_{p\in S}\in\mathbb Z^S:
\sum_{p\in S}c_p=0,\ \gcd_{p\in S}(c_p)=1\}.
$$
This is the primitive orientation torsor of collapses
$$
T_S=(\mathbb Q/\mathbb Z)^S/\Delta(\mathbb Q/\mathbb Z)
\twoheadrightarrow\mathbb Q/\mathbb Z.
$$
The antipode acts freely by $c\mapsto -c$.

For an inclusion $S\subseteq T$, the correct transition is contravariant with
respect to the boundary projection $T_T\to T_S$.  Pulling a collapse back
along this projection extends the functional by zero:
$$
e_{S,T}(c)_p=
\begin{cases}
c_p,&p\in S,\\
0,&p\in T\setminus S.
\end{cases}
$$
This preserves zero-sum and primitivity.  It is strictly functorial:
$$
e_{T,U}\circ e_{S,T}=e_{S,U},
$$
and it commutes with the antipode:
$$
e_{S,T}(-c)=-e_{S,T}(c).
$$

The reverse direction is not canonical.  If $d\in\mathcal O_T$, restriction
to $S$ can fail the zero-sum condition.  For example,
$$
(1,1,-2)\in\mathcal O_{\{2,3,5\}}
$$
restricts to $(1,1)$ on $\{2,3\}$, whose sum is nonzero.  Thus there is no
natural projection $\mathcal O_T\to\mathcal O_S$.

The finite kernel also behaves exactly as expected under zero-extension.  For
$c\in\mathcal O_S$ and $S\subseteq T$, the extended collapse on $T_T$ has
$N$-torsion kernel
$$
N^{|T|-2}=N^{|S|-2}\cdot N^{|T|-|S|}.
$$
The factor $N^{|S|-2}$ is the old collapse kernel; the factor
$N^{|T|-|S|}$ is the new support kernel introduced by $T_T\to T_S$.

Finally, no support-symmetric primitive orientation exists.  A symmetric
integral functional is constant on $S$, and the zero-sum condition forces it
to be zero.  Therefore the all-prime constant-term generator is not selected
by any canonical symmetric collapse.  One must work with an oriented-support
groupoid/stack, or pass to the antipode quotient / forgetful quotient when
only the single shifted generator $D\epsilon\simeq\mathbb Q[-1]$ is needed.

> **Theorem 100a (orientation torsor).** Primitive collapses
> $T_S\to\mathbb Q/\mathbb Z$ are represented by
> $\mathcal O_S=\{c\in\mathbb Z^S:\sum c_p=0,\gcd(c_p)=1\}$, with free
> antipode action $c\mapsto -c$.
>
> **Theorem 100b (zero-extension functoriality).** For $S\subseteq T$,
> zero-extension gives a functorial, antipode-equivariant map
> $\mathcal O_S\to\mathcal O_T$ compatible with pulling collapses back along
> $T_T\to T_S$.
>
> **Theorem 100c (restriction instability).** There is no canonical
> projection $\mathcal O_T\to\mathcal O_S$; restriction can fail zero-sum
> descent.
>
> **Theorem 100d (no symmetric orientation).** The only support-symmetric
> zero-sum functional is zero, so no distinguished all-prime primitive
> orientation exists.

**Machine verification** (`code/scripts/check-pass100.py` ->
`artifacts/reports/pass100-orientation-torsor-support-functoriality-check.json`,
PASS): the checker verifies primitive orientation objects, zero-extension
functoriality, antipode equivariance, restriction instability, finite kernel
factorization, and absence of a nonzero symmetric orientation.

**Limit of the pass.**  The next task is to package the oriented-support
groupoid/stack explicitly and compare its antipode quotient with the Pass-94
functional-equation sign.

## Pass 101 - Oriented-support groupoid and antipode quotient

Pass 101 packages the orientation torsor as a signed support object rather
than a set of unrelated choices.  For each finite support $S$, objects are
pairs $(S,c)$ with
$$
c\in\mathcal O_S
=\{c\in\mathbb Z^S:\sum_{p\in S}c_p=0,\ \gcd(c_p)=1\}.
$$
For an inclusion $S\subseteq T$, a morphism
$(S,c)\to(T,d)$ consists of a sign $\sigma\in\{\pm1\}$ satisfying
$$
d=\sigma e_{S,T}(c).
$$
Identities have sign $+1$, and composition multiplies signs.  Thus the
support functoriality from Pass 100 is strict once the sign is carried as
part of the morphism.

The antipode is the sign $-1$ morphism over a fixed support:
$$
(S,c)\to(S,-c).
$$
It is involutive and commutes with every zero-extension map.  Hence it is not
an accidental symmetry of representatives; it is the action responsible for
the functional-equation sign in the finite boundary package.

The coarse quotient
$$
[c]=\{c,-c\}
$$
is useful but too coarse by itself.  It remembers the primitive line of a
collapse and so presents a single all-prime generator, but it forgets whether
a transport path used the positive or negative orientation.  The sign must
therefore be retained either by working in the signed action groupoid or by
equipping the quotient with the induced $\mathbb Z/2$ sign local system.

At finite level $N$, this exactly matches the previous signed-duality
calculation.  Multiplication by $-1$ is a visible automorphism of
$(\mathbb Q/\mathbb Z)[N]$ for $N>2$, while it is invisible at $N=2$.  The
resulting package preserves the Pass-94 sign but still does not create a
degree-$0$ Weyl/Fourier morphism $\epsilon\to\mathbb Q$.

> **Theorem 101a (signed support category).** The signed oriented-support
> construction is strict: support inclusions compose by zero-extension and
> signs compose multiplicatively.
>
> **Theorem 101b (antipode involution).** The antipode is the sign $-1$
> morphism $(S,c)\to(S,-c)$, is involutive, and is compatible with
> zero-extension.
>
> **Theorem 101c (coarse quotient warning).** The coarse antipode quotient
> presents primitive collapse lines but loses the signed transport label.
>
> **Theorem 101d (local-system repair).** The signed groupoid, equivalently
> the coarse quotient plus its $\mathbb Z/2$ sign local system, retains exactly
> the Pass-94 functional-equation sign: visible for $N>2$ and collapsed for
> $N=2$.

**Machine verification** (`code/scripts/check-pass101.py` ->
`artifacts/reports/pass101-oriented-support-groupoid-antipode-quotient-check.json`,
PASS): the checker verifies signed morphism closure, multiplicative
composition, antipode involutivity, quotient sign loss, restoration by the
sign local system, and finite $N$-torsion sign behavior.

**Limit of the pass.**  The next task is to push the $\mathbb Z/2$ sign local
system through $[\mathbb Q\to\mathbb A_f]$ and identify the exact boundary or
Yoneda class representing biduality on $D\epsilon$.

## Pass 102 - Sign local system through the finite-adele boundary

Pass 102 pushes the signed orientation data one step further.  The relevant
one-generator extension after a primitive collapse is
$$
\beta=[0\to\mathbb Z\to\mathbb Q\to\mathbb Q/\mathbb Z\to0].
$$
The all-prime constant-term row is
$$
\delta_\epsilon=[0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0],
\qquad
\epsilon=\mathbb A_f/\mathbb Q.
$$
The sign local system acts on these boundary/Yoneda classes by
$$
\beta\mapsto\sigma\beta,\qquad
\delta_\epsilon\mapsto\sigma\delta_\epsilon,
\qquad \sigma\in\{\pm1\}.
$$

This clarifies the role of the antipode quotient.  The quotient $[c]=\{c,-c\}$
presents the primitive collapse line, but the local system records whether
the boundary class is transported as $+\delta_\epsilon$ or
$-\delta_\epsilon$.  No further finite conductor decoration is needed for the
sign itself.

At finite level $N$, the unit extension has Bockstein shadow
$$
1\in\operatorname{Ext}^1(\mathbb Z/N,\mathbb Z)\cong\mathbb Z/N.
$$
The signed class is $\sigma\in\mathbb Z/N$.  Hence the sign is visible exactly
for $N>2$ and collapses at $N=2$, recovering the Pass-94 finite signed-duality
behavior.

The boundary morphism
$$
\partial_\epsilon:\epsilon\to\mathbb Q[1]
$$
is the class whose shift gives
$$
D\epsilon\simeq\mathbb Q[-1].
$$
A one-sided sign change negates this class.  If the sign is applied on both
source and target, the class is multiplied by $(-1)^2=1$, so the biduality
square remains involutive.  This is a shifted-boundary statement only; it
does not supply a degree-$0$ Weyl/Fourier map $\epsilon\to\mathbb Q$.

> **Theorem 102a (local-system boundary action).** The
> $\mathbb Z/2$ sign local system acts on the unit extension and the
> finite-adele row by multiplication of the corresponding Yoneda class.
>
> **Theorem 102b (finite Bockstein shadow).** At finite level $N$, the signed
> boundary class is $\pm1\in\mathbb Z/N$, visible precisely for $N>2$ and
> collapsed for $N=2$.
>
> **Theorem 102c (biduality compatibility).** Under
> $D\epsilon\simeq\mathbb Q[-1]$, a one-sided sign negates the shifted class,
> while two-sided sign action squares to the identity.
>
> **Theorem 102d (no extra Weyl morphism).** The local system supplies all
> finite sign bookkeeping but creates no degree-$0$ morphism
> $\epsilon\to\mathbb Q$.

**Machine verification** (`code/scripts/check-pass102.py` ->
`artifacts/reports/pass102-sign-local-system-adele-boundary-check.json`,
PASS): the checker verifies signed finite Bockstein shadows, signed primitive
collapse surjectivity, support-transport preservation of the boundary sign,
one-sided Yoneda negation, two-sided biduality involutivity, and sufficiency
of the local-system package.

**Limit of the pass.**  The next task is to package the signed boundary class
as a natural transformation over finite conductor reductions and compare it
with the CRT-acyclic finite constant-term complexes from Pass 95.

## Pass 103 - Signed boundary naturality under conductor reduction

Pass 103 compares the signed boundary class with the Pass-95 finite conductor
complexes.  For a finite conductor $N$, write
$$
b_N^\sigma=\sigma\in\mathbb Z/N,\qquad \sigma\in\{\pm1\}.
$$
If $M\mid N$, conductor reduction satisfies
$$
\rho_{N,M}(b_N^\sigma)=b_M^\sigma.
$$
Thus the signed Bockstein/Yoneda class is natural over the finite conductor
category.  The sign disappears only when the target modulus is $2$.

Now twist the Pass-95 finite conductor differential by the sign:
$$
d_N^\sigma:\mathbb Z/N\to\prod_{p^e\parallel N}\mathbb Z/p^e,
\qquad
d_N^\sigma(x)=(\sigma x\bmod p^e)_p.
$$
Because $\sigma=\pm1$ is a unit, $d_N^\sigma$ is still a CRT isomorphism.
Therefore every fixed signed finite conductor shadow remains acyclic:
$$
H^0(C^\sigma_{B,N})=H^1(C^\sigma_{B,N})=0.
$$

For $M\mid N$, the signed CRT squares commute: reducing $x$ first and then
applying $d_M^\sigma$ gives the same prime-power residues as applying
$d_N^\sigma$ and then reducing every target coordinate.  Hence conductor
reduction introduces no new sign-twisted finite obstruction.  The nonzero
class remains the all-prime pro/solid boundary, not a fixed finite cokernel.

The Pass-95 support caveat persists.  Conductor reduction and support
projection are canonical, but support enlargement is still only a
finite-conductor CRT choice/span.  The signed naturality result does not
create a canonical all-prime zero-insertion map.

> **Theorem 103a (signed conductor naturality).** For $M\mid N$,
> $\rho_{N,M}(\sigma\bmod N)=\sigma\bmod M$.
>
> **Theorem 103b (signed CRT acyclicity).** The signed finite conductor
> differential $d_N^\sigma$ is a CRT isomorphism for $\sigma=\pm1$, so fixed
> finite signed shadows have zero ordinary cohomology.
>
> **Theorem 103c (no finite sign obstruction).** Signed conductor-reduction
> squares commute.  No sign-twisted finite conductor obstruction appears
> beyond the known modulus-$2$ sign collapse.
>
> **Theorem 103d (support caveat).** Signed conductor naturality does not make
> support enlargement into a canonical all-prime diagonal-preserving map.

**Machine verification** (`code/scripts/check-pass103.py` ->
`artifacts/reports/pass103-signed-boundary-conductor-naturality-check.json`,
PASS): the checker verifies signed finite CRT isomorphism/acyclicity,
naturality of signed Bockstein classes under conductor reductions, commutation
of signed CRT squares, modulus-$2$ sign collapse, and persistence of the
support-enlargement caveat.

**Limit of the pass.**  The next task is to assemble the signed conductor
system into a pro/solid all-prime boundary object and decide whether the
orientation double cover survives the all-prime limit or is absorbed by the
local system on $\epsilon$.

## Pass 104 - Signed pro/solid all-prime boundary object

Pass 104 assembles the finite signed conductor system from Pass 103.  For
each sign $\sigma\in\{\pm1\}$, the compatible residues
$$
b_N^\sigma=\sigma\bmod N
$$
define a point of the profinite completion:
$$
\{b_N^\sigma\}_N=\sigma\in\widehat{\mathbb Z}.
$$

This limit is a diagonal integer.  Therefore its image in the all-prime
boundary group
$$
\epsilon=\widehat{\mathbb Z}/\mathbb Z
$$
is zero.  In particular, the two signs do not give two distinct points of
$\epsilon$.  The orientation double cover visible before quotienting is not a
nontrivial point-cover of the solid boundary.

The sign survives in a different place: as monodromy of the boundary/Yoneda
line.  The finite-adele boundary class
$$
\delta_\epsilon=[0\to\mathbb Q\to\mathbb A_f\to\epsilon\to0]
$$
spans the shifted generator
$$
D\epsilon\simeq\mathbb Q[-1].
$$
The local system acts by
$$
\delta_\epsilon\mapsto\sigma\delta_\epsilon.
$$
Thus the all-prime passage absorbs the sign as an $\epsilon$-point but keeps
it as a $\mathbb Z/2$ action on the boundary line.

The minimal categorical package is:

- oriented-support action groupoid $(S,c)$ with zero-extension;
- finite-conductor pro-system of signed CRT-isomorphism complexes;
- $B\mathbb Z/2$ local system on the boundary/Yoneda line.

This package carries support, conductor, and sign without creating a
degree-$0$ Weyl/Fourier map $\epsilon\to\mathbb Q$.

> **Theorem 104a (pro-sign limit).** The compatible finite conductor classes
> $\{\sigma\bmod N\}_N$ limit to the diagonal integer
> $\sigma\in\widehat{\mathbb Z}$.
>
> **Theorem 104b (absorption in $\epsilon$).** Both signs map to zero in
> $\epsilon=\widehat{\mathbb Z}/\mathbb Z$.  Hence the orientation double
> cover does not survive as a nontrivial point-cover of $\epsilon$.
>
> **Theorem 104c (boundary-line survival).** The sign survives as the
> $\mathbb Z/2$ local-system action on $\delta_\epsilon$, equivalently on
> $D\epsilon\simeq\mathbb Q[-1]$.
>
> **Theorem 104d (minimal package).** The oriented-support groupoid over the
> finite-conductor pro-system, equipped with a $B\mathbb Z/2$ boundary-line
> local system, carries the needed data and preserves
> $\operatorname{Hom}^0(\epsilon,\mathbb Q)=0$.

**Machine verification** (`code/scripts/check-pass104.py` ->
`artifacts/reports/pass104-signed-pro-solid-boundary-object-check.json`,
PASS): the checker verifies conductor compatibility of the finite sign
system, identifies the pro-limit as the diagonal integer $\sigma$, verifies
that both signs vanish as points of $\epsilon$, records survival as a
$\mathbb Z/2$ boundary action, and checks that the minimal package carries
support/conductor/sign without creating a degree-$0$ Weyl map.

**Limit of the pass.**  The next task is to compare this signed pro-boundary
stack with support projections and zero-extension spans, then isolate the
exact descent/colimit statement for all-prime primitive orientations.

## Pass 105 - Support descent for all-prime primitive orientations

Pass 105 clarifies the support variance hidden in the previous all-prime
boundary package.  For finite support $S$, the primitive orientations are
$$
\mathcal O_S=
\{c\in\mathbb Z^S:\sum_{p\in S}c_p=0,\ \gcd(c_p)=1\}.
$$
For $S\subseteq T$, the canonical orientation map is zero-extension
$$
e_{S,T}:\mathcal O_S\to\mathcal O_T.
$$
It preserves zero-sum, primitivity, and the antipode, and it is strictly
functorial along support chains.

The boundary groups have canonical support projection in the opposite
direction,
$$
T_T\to T_S.
$$
This is why the all-prime package must be span-like.  A primitive orientation
on $T$ cannot generally be restricted to $S$: the vector
$$(1,1,-2)\in\mathcal O_{\{2,3,5\}}$$
restricts to $(1,1)$ on $\{2,3\}$, whose sum is nonzero.

Thus the exact colimit statement is: all-prime primitive orientations are
primitive finitely supported zero-sum integer functionals on the prime set,
formed as the filtered colimit of finite $\mathcal O_S$ by zero-extension and
modulo padded zero coordinates.  The antipode quotient gives primitive lines
$[c]=\{c,-c\}$, but the sign must remain as the $B\mathbb Z/2$ local system
on the boundary/Yoneda line from Pass 104.

> **Theorem 105a (zero-extension colimit).** The support inclusion maps
> $S\subseteq T$ induce canonical maps
> $e_{S,T}:\mathcal O_S\to\mathcal O_T$ that preserve primitivity, zero-sum,
> and the antipode and form a filtered colimit.
>
> **Theorem 105b (no restriction sheaf).** There is no canonical total
> restriction map $\mathcal O_T\to\mathcal O_S$ because deleting coordinates
> can break the zero-sum condition.
>
> **Theorem 105c (span-stack package).** The support-descent object combines
> zero-extension on orientations, projection on boundary groups, and the
> $B\mathbb Z/2$ boundary-line local system.  It is a span/Grothendieck
> object rather than a plain sheaf of primitive orientations.
>
> **Theorem 105d (no symmetric orientation).** A support-symmetric finitely
> supported integer functional is constant on its support; zero-sum then
> forces it to be zero, so no nonzero support-symmetric primitive orientation
> exists.

**Machine verification** (`code/scripts/check-pass105.py` ->
`artifacts/reports/pass105-support-descent-primitive-orientations-check.json`,
PASS): the checker verifies zero-extension preservation and functoriality,
explicit restriction failure, colimit padding equivalence, nonexistence of
support-symmetric primitive orientations, and the span-stack verdict.

**Limit of the pass.**  The next task is to compute the obstruction to
stackifying primitive orientations over finite supports if restriction maps
are demanded, and then state the universal property of the
span-stack/left-Kan colimit package.

## Pass 106 - Stackification obstruction for primitive orientations

Pass 106 computes the exact obstruction behind the Pass-105 warning that
primitive orientations do not form a restriction sheaf.  For $S\subseteq T$
and $d\in\mathcal O_T$, deleting the coordinates outside $S$ has additive
defect
$$
\Delta_{T,S}(d)=\sum_{p\in S}d_p
=-\sum_{p\in T\setminus S}d_p.
$$
Thus coordinate deletion reaches $\mathcal O_S$ only on the partial domain
where $\Delta_{T,S}(d)=0$ and $\gcd_{p\in S}(d_p)=1$.

The two requirements are independent.  The vector
$$
(2,-2,1,-1)\in\mathcal O_{\{2,3,5,7\}}
$$
has zero additive defect on $\{2,3\}$, but its deleted vector $(2,-2)$ is not
primitive.  Conversely, $(1,1,-2)$ on $\{2,3,5\}$ has primitive deletion
$(1,1)$ but nonzero additive defect.

A repair of nonzero defect is a choice of section of
$$
\Sigma_S:\mathbb Z^S\to\mathbb Z.
$$
Different sections, such as repairing at the first or last prime, can produce
different primitive orientation lines.  No support-symmetric integral section
exists for $|S|>1$: symmetry would make the image of $1$ a constant vector
$(k,\dots,k)$, forcing $|S|k=1$.

The universal statement is therefore covariant:
$$
\mathcal O_{\mathbb P}^{\mathrm{fin}}
=\operatorname*{colim}_{S}\mathcal O_S
$$
under zero-extension.  A zero-extension-compatible family of maps
$F_S:\mathcal O_S\to X$ factors uniquely through this colimit.  The colimit
is represented by primitive finitely supported zero-sum functions on the
prime set after trimming padded zero coordinates.

The antipode quotient $[c]=\{c,-c\}$ gives the coarse orientation line, but
it forgets the sign of the boundary action.  The all-prime package therefore
remains the orientation-line colimit together with the $B\mathbb Z/2$ local
system acting on $\delta_\epsilon$.

> **Theorem 106a (additive/primitivity defect).** Coordinate deletion
> defines a primitive restriction exactly on the partial domain where the
> additive defect vanishes and primitivity survives.
>
> **Theorem 106b (section obstruction).** Any repair of nonzero additive
> defect requires a section of $\Sigma_S$.  No support-symmetric integral
> section exists for $|S|>1$.
>
> **Theorem 106c (left-Kan colimit).** The all-prime primitive-orientation
> object is the zero-extension colimit of the $\mathcal O_S$, with the usual
> universal property for zero-extension-compatible families.
>
> **Theorem 106d (antipode quotient plus local system).** The quotient
> $[c]=\{c,-c\}$ is not enough by itself; the $B\mathbb Z/2$ local system is
> needed to retain the signed boundary action.

**Machine verification** (`code/scripts/check-pass106.py` ->
`artifacts/reports/pass106-stackification-obstruction-primitive-orientations-check.json`,
PASS): the checker verifies the deletion-defect formula, the partial
restriction domain, nonunique repairs by summation sections, absence of
support-symmetric sections, basepoint-dependence, the zero-extension colimit
universal property, and the antipode/local-system distinction.

**Limit of the pass.**  The next task is to model correction choices as
torsors under $\ker\Sigma_S$ and decide whether the support-defect data gives
a genuine Cech/cosheaf cohomology class or only an ordinary choice
obstruction.

## Pass 107 - Correction torsors for support-defect repairs

Pass 107 separates additive repair data from primitive repair data.  For
finite support $S$, let
$$
K_S=\ker\Sigma_S
=\{a\in\mathbb Z^S:\sum_{p\in S}a_p=0\}.
$$
If coordinate deletion gives $u=d|_S$ with defect
$\Delta=\Sigma_S(u)$, an additive repair is a vector
$$
r=u-a,\qquad \Sigma_S(a)=\Delta.
$$
The set of additive repairs is a free transitive $K_S$ torsor: two repairs
differ by an element of $K_S$, and adding any element of $K_S$ to a repair
gives another repair.

The primitive repair locus is not itself a torsor under the full kernel.
For example, on $\{2,3\}$, the primitive vector $(1,-1)$ lies in $K_S$, but
adding the kernel element $(1,-1)$ gives $(2,-2)$, which is zero-sum and
nonprimitive.  Thus primitivity is an arithmetic refinement of the additive
torsor.

A basepoint $b\in S$ gives a splitting
$$
s_b(n)=n e_b.
$$
For basepoints $a,b,c$, the transitions
$$
\tau_{a,b}=s_b(1)-s_a(1)
$$
lie in $K_S$ and satisfy
$$
\tau_{a,b}+\tau_{b,c}=\tau_{a,c}.
$$
They are coboundaries of chosen splittings.  Along support inclusions,
basepointed splittings are natural exactly when the basepoint is preserved.

Consequently the support-defect repair data is not a Rosser/cosheaf phantom.
At every finite support, the exact sequence
$$
0\to K_S\to\mathbb Z^S\xrightarrow{\Sigma_S}\mathbb Z\to0
$$
splits after choosing a basepoint.  No non-Mittag-Leffler inverse tower is
present.  The obstruction is the ordinary noncanonicity of choosing a
splitting, not a persistent derived class.  Linear repairs commute with the
antipode, so the $B\mathbb Z/2$ boundary-line local system remains unchanged.

> **Theorem 107a (additive torsor).** Additive repairs of a support defect
> form a free transitive $K_S$ torsor.
>
> **Theorem 107b (primitive refinement).** Primitive repairs are the primitive
> locus inside the additive repair torsor and are not stable under the full
> $K_S$ action.
>
> **Theorem 107c (basepoint coboundary).** Basepointed splittings trivialize
> the additive repair torsor; transitions between basepoints are $K_S$-valued
> coboundaries satisfying the cocycle identity.
>
> **Theorem 107d (not a phantom).** The repair torsor is ordinary finite
> choice data, not a Rosser/cosheaf phantom.  Antipode compatibility and the
> $B\mathbb Z/2$ boundary-line local system are preserved.

**Machine verification** (`code/scripts/check-pass107.py` ->
`artifacts/reports/pass107-correction-torsors-support-defect-check.json`,
PASS): the checker verifies additive repair torsors, non-stability of the
primitive locus under the full kernel, basepoint transition coboundaries,
inclusion naturality exactly under basepoint preservation, antipode
compatibility, and the ordinary-choice-not-phantom verdict.

**Limit of the pass.**  The next task is to classify the integral
equivariant obstruction: rational symmetric sections of $\Sigma_S$ exist by
barycenters, but integral support-symmetric sections do not.

## Pass 108 - Integral equivariant repair-section obstruction

Pass 108 identifies the exact obstruction to support-symmetric integral
repair sections.  Let $S$ be a finite support of size $n>1$, and let
$G=\operatorname{Sym}(S)$.  The summation map
$$
\Sigma_S:\mathbb Z^S\to\mathbb Z
$$
is $G$-equivariant.  A support-symmetric integral section would be an
invariant vector $v\in(\mathbb Z^S)^G$ with $\Sigma_S(v)=1$.

But the invariant lattice is
$$
(\mathbb Z^S)^G=\mathbb Z\mathbf 1_S,
$$
and
$$
\Sigma_S(k\mathbf 1_S)=nk.
$$
Thus the invariant image is $n\mathbb Z$, and no integral equivariant section
exists for $n>1$.

Over $\mathbb Q$, the obstruction disappears by the barycentric section
$$
s_{\mathrm{bar}}(1)=\frac1n\mathbf 1_S.
$$
Therefore the obstruction is exactly the denominator $n$: an equivariant
integral lift of $m\in\mathbb Z$ exists iff $n\mid m$.  In the augmentation
sequence
$$
0\to K_S\to\mathbb Z^S\xrightarrow{\Sigma_S}\mathbb Z\to0,
$$
the finite equivariant obstruction is
$$
\mathbb Z/\Sigma_S((\mathbb Z^S)^G)\cong\mathbb Z/n\mathbb Z.
$$

Basepoint splittings are integral but break support symmetry.  The
barycentric splitting is support-symmetric but rational.  Under a support
inclusion $S\subseteq T$, the zero-extended $S$-barycenter differs from the
$T$-barycenter by an element of $K_T\otimes\mathbb Q$, so barycentric
normalization has rational transition classes.

The antipode local system is independent of this denominator.  It acts by a
scalar sign on the boundary line and commutes with all support permutations;
changing $1$ to $-1$ changes the barycenter to its negative but leaves the
denominator $n$ unchanged.

> **Theorem 108a (no integral equivariant section).** For $|S|=n>1$,
> $\Sigma_S:\mathbb Z^S\to\mathbb Z$ has no
> $\operatorname{Sym}(S)$-equivariant integral section.
>
> **Theorem 108b (rational barycenter).** Over $\mathbb Q$, the barycentric
> vector $\frac1n\mathbf 1_S$ gives a canonical support-symmetric section.
>
> **Theorem 108c (exact denominator).** An equivariant integral lift of
> $m$ exists iff $n\mid m$; the obstruction is $\mathbb Z/n\mathbb Z$.
>
> **Theorem 108d (antipode independence).** The $B\mathbb Z/2$ boundary-line
> local system is independent of the support-symmetry denominator
> obstruction.

**Machine verification** (`code/scripts/check-pass108.py` ->
`artifacts/reports/pass108-integral-equivariant-repair-section-check.json`,
PASS): the checker verifies the invariant image $n\mathbb Z$, the rational
barycentric section, the divisibility rule for integral lifts, the exact
denominator $n$, non-naturality of barycentric sections under support
inclusion with rational-kernel transitions, and antipode independence.

**Limit of the pass.**  The next task is to analyze the rational
barycentric transition classes under support inclusions and compare their
denominators with finite conductor/CRT denominator bookkeeping.

## Pass 109 - Barycentric transition denominators

Pass 109 computes the rational support-transition class left open by
Pass 108.  For an inclusion $S\subset T$, write $|S|=n$ and $|T|=m$.  The
barycentric splittings are
$$
s_{\mathrm{bar},S}(1)=\frac1n\mathbf 1_S,\qquad
s_{\mathrm{bar},T}(1)=\frac1m\mathbf 1_T.
$$
The zero-extended transition
$$
\tau_{S,T}
=e_{S,T}s_{\mathrm{bar},S}(1)-s_{\mathrm{bar},T}(1)
$$
has entries
$$
(\tau_{S,T})_p=
\begin{cases}
\frac{m-n}{nm}, & p\in S,\\[2mm]
-\frac1m, & p\in T\setminus S.
\end{cases}
$$
Its sum is zero, so it lies in $K_T\otimes\mathbb Q$.

The exact denominator is $\operatorname{lcm}(n,m)$.  Indeed, if
$g=\gcd(n,m)$, $n=ga$, and $m=gb$, any clearing integer must be divisible by
$m$, say $gbq$, and then the on-support entry is integral exactly when
$a\mid q$.  Thus the minimal clearing integer is $gab=\operatorname{lcm}(n,m)$.

Clearing by this denominator gives a canonical primitive integral vector
$$
\eta_{S,T}:=\operatorname{lcm}(n,m)\tau_{S,T}.
$$
Its entries are $(m-n)/g$ on $S$ and $-n/g$ on $T\setminus S$.  Since these
values are $b-a$ and $-a$ with $\gcd(a,b)=1$, the vector is primitive as well
as zero-sum.

The rational transitions are coboundaries of the barycentric splittings.  For
$S\subset T\subset U$,
$$
e_{T,U}\tau_{S,T}+\tau_{T,U}=\tau_{S,U}.
$$
After clearing all terms by a common conductor, this identity is integral.
The individually primitive clearings are normalized at different
denominators, so their chain behavior is a rescaling problem rather than a
plain additive cocycle.

Comparison with finite conductor/CRT bookkeeping: a conductor $N$ clears
$\tau_{S,T}$ exactly when $\operatorname{lcm}(n,m)\mid N$.  But fixed
finite-conductor CRT maps, including the signed maps from Pass 103, remain
isomorphisms.  Therefore barycentric transition denominators are useful
support-normalization data, not a new finite CRT cohomology class.

> **Theorem 109a (barycentric transition formula).** The transition
> $\tau_{S,T}$ has entries $(m-n)/(nm)$ on $S$ and $-1/m$ on $T\setminus S$,
> hence lies in $K_T\otimes\mathbb Q$.
>
> **Theorem 109b (lcm denominator).** The exact denominator of
> $\tau_{S,T}$ is $\operatorname{lcm}(|S|,|T|)$; a finite conductor clears it
> exactly when it is divisible by that lcm.
>
> **Theorem 109c (primitive minimal clearing).** The minimally cleared vector
> $\eta_{S,T}$ is an integral primitive zero-sum vector on $T$.
>
> **Theorem 109d (no finite CRT obstruction).** The transition denominator
> records rational support normalization; ordinary and signed finite CRT
> shadows remain bijective.

**Machine verification** (`code/scripts/check-pass109.py` ->
`artifacts/reports/pass109-barycentric-transition-denominator-check.json`,
PASS): the checker verifies the transition formula, exact lcm denominator,
conductor clearing rule, primitive integral clearing, rational chain
coboundary identity, common-conductor integral identity, and unchanged CRT
and signed CRT bijections.

**Limit of the pass.**  The next task is to study the primitive
conductor-cleared vectors $\eta_{S,T}$ along support chains and determine
whether their rescaled edge law gives useful oriented-support data.

## Pass 110 - Primitive transition chain law

Pass 110 studies the conductor-cleared primitive vectors from Pass 109.  For
$S\subset T$, define
$$
L_{S,T}=\operatorname{lcm}(|S|,|T|),
\qquad
\eta_{S,T}=L_{S,T}\tau_{S,T}.
$$
If $|S|=n$, $|T|=m$, and $g=\gcd(n,m)$, then $\eta_{S,T}$ has entries
$(m-n)/g$ on $S$ and $-n/g$ on $T\setminus S$.  It is a primitive integral
zero-sum vector in $K_T$.

The chain law is weighted by conductor denominators.  For
$S\subset T\subset U$, put
$$
C=\operatorname{lcm}(L_{S,T},L_{T,U},L_{S,U}).
$$
Then
$$
\frac{C}{L_{S,T}}e_{T,U}\eta_{S,T}
+\frac{C}{L_{T,U}}\eta_{T,U}
=
\frac{C}{L_{S,U}}\eta_{S,U}.
$$
This is just the rational coboundary identity for $\tau$ multiplied by the
common conductor $C$.

Primitive vectors do not usually compose strictly.  The strict identity
$$
e_{T,U}\eta_{S,T}+\eta_{T,U}=\eta_{S,U}
$$
holds in the checked equal-conductor cases, but otherwise the coefficients
$C/L_{A,B}$ are essential.  Therefore the primitive line $[\eta_{S,T}]$ alone
is not enough to define functorial support-edge data.  The correct edge label
is the weighted pair $(L_{S,T},\eta_{S,T})$, equivalently the rational
transition $\tau_{S,T}$.

This matches the primitive repair torsor warning from Pass 107.  The
weighted sum always lies in the additive kernel $K_U$, but it can equal a
nonprimitive multiple of the endpoint vector.  Thus primitive support-edge
labels are normalized representatives inside additive kernel data, not a
sub-cocycle closed under addition.

The newest Claude Code review is orthogonal to this support-chain
calculation but concrete enough to become the next pass: it asks for a
MacNeille reflection checker repair, including a non-lattice witness, an
$L^{op}$ antitone closure rule, reflected/principal-unreflected output, and
extension-condition checks.

> **Theorem 110a (primitive cleared edge).** Every $\eta_{S,T}$ is an
> integral primitive zero-sum vector in $K_T$.
>
> **Theorem 110b (weighted chain law).** The common-conductor identity above
> holds for every support chain $S\subset T\subset U$.
>
> **Theorem 110c (primitive line insufficiency).** Primitive edge vectors or
> their lines are not generally functorial without conductor weights.
>
> **Theorem 110d (torsor comparison).** The chain law is closed in additive
> kernels but not in primitive loci, matching the Pass-107 repair-torsor
> distinction.

**Machine verification** (`code/scripts/check-pass110.py` ->
`artifacts/reports/pass110-primitive-transition-chain-law-check.json`,
PASS): the checker verifies primitive edge vectors, the weighted
common-conductor chain identity, strict-composition classification, failure
of primitive lines to be sufficient in general, and the repair-torsor
comparison.

**Limit of the pass.**  The next task is to incorporate the Claude Code
MacNeille reflection checker review and repair the completion/fixed-point
checker line.

## Pass 111 - MacNeille reflection checker repair

Pass 111 returns to the completion/fixed-point line that sits adjacent to the
G2/FG2 hierarchy.  The finite MacNeille checker now distinguishes three
phenomena that were previously conflated:

1. syntactic fixed points $p=\boxtimes p$ in the original preorder;
2. principal completed fixed cuts $i_L(a)$ that need not be reflected by
   $a=\boxtimes a$;
3. non-principal completed fixed cuts with no syntactic fixed point.

The current antitone extension rule is `antitone-dual-lower-cut-v1`,
$$
\widehat{\boxtimes}(C)=((\boxtimes[C])^{l_L})^{u_L},
$$
which treats $\boxtimes:L\to L^{op}$ as monotone before closing.  The legacy
`antitone-dual-lower-cut-v0` rule is retained only as a wrong-polarity
control.

The verified non-lattice witness `three-element-nolattice-nosynt` has no
syntactic fixed point and, under v1, the non-principal completion fixed cut
`{ 0, a, b }`.  It is classified as `nonprincipal-without-syntactic`.  Under
legacy v0, it instead gives a principal but unreflected cut `{ 0, a }` and
fails the principal extension condition twice.  The three-chain smoke test
under v1 is also `principal-unreflected`: the syntactic fixed point is `m`,
but the completed fixed cut is principal at `t`.

Both checked examples are non-G2 and non-FG2, so the result is a repaired
completion-reflection counterexample at the bare finite preAPS level, not yet
a theorem about APS axiom packages.  The next G2/FG2 task is therefore to add
axiom-package checks to the MacNeille search and test whether any G2-holding
finite model can keep the non-principal completion fixed point without a
syntactic fixed point.

**Machine verification** (`code/scripts/check-pass111.py` ->
`artifacts/reports/pass111-macneille-reflection-review-check.json`, PASS):
the audit verifies the v1 non-lattice witness, the v0 polarity control, the
v1 chain smoke test, and documentation markers for the repaired interface.

## Pass 112 - MacNeille G2/A2 boundary on the smallest non-lattice

Pass 112 refines the Pass-111 MacNeille witness by adding finite APS
axiom-package fields to the checker.  The original v1 non-lattice witness is
not merely a bare unchecked table: as a finite table it satisfies A1-A4, while
still having no syntactic $\boxtimes$-fixed point and having the non-principal
completion fixed cut `{ 0, a, b }`.  Its failure is exactly G2:
`boxtimes(T) <= bottom` holds but `T <= bottom` does not.

The fixed-carrier enumeration on `{0,a,b}` with `0<a` and `0<b` shows the
opposite side of the boundary.  Some separating tables satisfy G2, but only
vacuously, because the G2 antecedent `boxtimes(T) <= bottom` is false.  These
tables necessarily drop A2.  Once A2 is required, no separating table remains
on this carrier.

The finite counts are:

| condition on separating tables | count |
| --- | ---: |
| no extra package | 216 |
| G2 | 54 |
| G2 and A2 | 0 |
| G2 and A124Core | 0 |
| G2 and finite A1-A4 APS | 0 |
| finite A1-A4 APS but not G2 | 10 |

Hence the three-element non-lattice carrier realizes a clean local dichotomy:
finite A1-A4 can coexist with completion-created non-principal fixed cuts, but
G2 cuts across that example; G2 can coexist with such cuts only after A2 is
removed.  The next hierarchy question is whether this A2 gate survives on
four-element carriers or whether a genuine G2+A2 completion-separation witness
appears there.

**Machine verification** (`code/scripts/check-pass112.py` ->
`artifacts/reports/pass112-macneille-g2-boundary-check.json`, PASS): the
checker enumerates the fixed three-element non-lattice carrier, records
representative G2 and APS-but-not-G2 examples, and verifies the zero counts
for G2+A2, G2+A124Core, and G2+A1-A4 APS separation.

## Pass 113 - Four-element G2+FG2+finite-APS completion separation

Pass 113 breaks the Pass-112 A2 gate by adding one point.  The witness has
order
$$
0<a<b,\qquad 0<c,
$$
with `T=a` and `bottom=0`.  Define
$$
\boxtimes(0)=\boxtimes(a)=b,\qquad
\boxtimes(b)=\boxtimes(c)=0,
$$
and
$$
\Box(0)=\Box(a)=\Box(c)=0,\qquad \Box(b)=b.
$$

This table satisfies finite A1-A4.  It also satisfies G2 and FG2:
$$
\boxtimes T=b\not\le0,
$$
so G2 holds vacuously, and
$$
\boxtimes^2T=\boxtimes b=0\le b=\boxtimes T.
$$
There is no syntactic fixed point.  Nevertheless, the v1 MacNeille completion
has the non-principal fixed cut `{ 0, a, b, c }`.

The labelled four-element poset enumeration confirms that this is not an
isolated table accident.  Among unique-bottom labelled four-element posets,
there are 2784 separation+G2+finite-A1-A4 tables across 240 refutability
profiles and 36 posets.

This moves the hierarchy question: G2, FG2, and finite A1-A4 are not enough,
by themselves, to force syntactic reflection of MacNeille completion fixed
cuts.  Any positive theorem must use additional structure, such as residual
adjunctions, boundedness, completion-stability, or a definability/compactness
reflection condition.

**Machine verification** (`code/scripts/check-pass113.py` ->
`artifacts/reports/pass113-four-element-macneille-g2-boundary-check.json`,
PASS) plus standalone witness report
`artifacts/reports/macneille-reflection-four-element-g2-aps-nosynt-v1.json`.

## Pass 114 - Same-order residuation blocks the four-element witness

Pass 114 tests the first natural strengthening of the Pass-113 hierarchy
counterexample: keep the same carrier/order and ask for a two-sided-unit
associative monotone tensor with both residuals.  The exhaustive search scans
1,048,576 operation tables.  It finds 624 associative tensors and 56
associative+monotone tensors, but no full residual package.

The first obstruction among the surviving units is the non-principal fiber
$$
\{x:0\otimes x\le0\}=\{0,a,b,c\}.
$$
Since the carrier has no greatest element, this fiber cannot be represented by
any residual element.  Thus the Pass-113 witness separates finite A1-A4, G2,
and FG2 from syntactic fixed-point reflection only at the finite table level;
it does not yet separate the corresponding residuated APS package.

This suggests a sharper hierarchy question for the next pass: is residuation
blocking the witness because of missing top/join structure alone, or because
completion-stability of A1-A4/G2/FG2 fails even after the order is repaired?
