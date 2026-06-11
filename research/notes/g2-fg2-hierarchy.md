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
