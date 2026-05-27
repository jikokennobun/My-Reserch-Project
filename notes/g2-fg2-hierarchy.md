# G2/FG2 Hierarchy and n-FG2

Source: https://chatgpt.com/share/6a0a7f2e-eec4-83ec-adc2-7fadc3feb442

Imported from Research Project handoff: 2026-05-22.
Extended by Claude Code Review 1, 2026-05-25 — certified results added.

## Topic

Hierarchy between G2 and FG2, including \(n\)-FG2 variants.

---

## Definitions

**G2**:

\[
\mathrm{G2}(S):
\quad
\boxtimes T\le\bot
\Rightarrow
T\le\bot.
\]

**\(n\)-FG2** (for \(k\ge 1\)):

\[
\mathrm{nFG2}(k):
\quad
\boxtimes^{k+1}T\le\boxtimes^k T.
\]

FG2 = nFG2(1). The sequence \(\mathrm{nFG2}(1),\mathrm{nFG2}(2),\ldots\) is the
**\(n\)-FG2 hierarchy**.

**Orbit of \(T\) under \(\boxtimes\)**:

\[
T,\;\boxtimes T,\;\boxtimes^2 T,\;\boxtimes^3 T,\;\ldots
\]

nFG2(\(k\)) asks whether one step back along this orbit is an upward step in \(L\).

---

## Certified Independence Results (3-element witnesses)

All models below are in `models/examples/` and are verified by `scripts/check-g2-zoo.py`.

### Theorem 1: G2 and FG2 are logically independent.

**(a) FG2 does not imply G2.** Model **M-010**:

\[
L=\{T,0,\bot\},\quad 0<\bot,\quad T\text{ isolated},
\quad \boxtimes T=\bot,\; \boxtimes\bot=0,\; \boxtimes 0=\bot.
\]

- G2: \(\boxtimes T=\bot\le\bot\) (antecedent true), consequent \(T\le\bot\)
  FALSE (T isolated). So G2 FAILS.
- FG2: \(\boxtimes^2 T=\boxtimes\bot=0\le\bot=\boxtimes T\) since \(0<\bot\).
  So FG2 HOLDS.

**(b) G2 does not imply FG2.** Model **M-100**:

\[
L=\{T,c,\bot\}\text{ discrete},
\quad \boxtimes T=c,\; \boxtimes c=T,\; \boxtimes\bot=T.
\]

- G2: \(\boxtimes T=c\not\le\bot\) (antecedent false). G2 holds VACUOUSLY.
- FG2: \(\boxtimes^2 T=T\not\le c=\boxtimes T\) (discrete order). FG2 FAILS.

---

### Certified separation: FG2 does not imply nFG2(2).

Witness: model **M-010** above. The \(\boxtimes\)-orbit of \(T\) is:

\[
T \to \bot \to 0 \to \bot \to 0 \to \bot \to \cdots
\]

(period-2 oscillation between \(\bot\) and \(0\) after the first step). Then:

\[
\mathrm{nFG2}(k) = \begin{cases}
\text{TRUE} & k\text{ odd} \\
\text{FALSE} & k\text{ even}
\end{cases}
\]

because for odd \(k\): \(\boxtimes^{k+1}T\in\{0\}\) and \(\boxtimes^k T\in\{\bot\}\),
and \(0<\bot\). For even \(k\): \(\boxtimes^{k+1}T\in\{\bot\}\) and
\(\boxtimes^k T\in\{0\}\), and \(\bot\not\le 0\).

**Status**: the full strictness problem is still open. The currently certified
statement is narrower: M-010 refutes
\(\mathrm{nFG2}(1)\Rightarrow\mathrm{nFG2}(2)\) and, more generally, refutes
\(\mathrm{nFG2}(k)\Rightarrow\mathrm{nFG2}(k+1)\) at every odd \(k\). It does
not refute the even-step implications. Arbitrary-depth strictness remains an
open finite-model search target.

---

### Theorem 3: G2 + FP-synt does NOT imply FG2.

Model **M-101**:

\[
L=\{T,c,\bot\}\text{ discrete},
\quad \boxtimes T=c,\; \boxtimes c=T,\; \boxtimes\bot=\bot.
\]

- G2 holds vacuously (\(\boxtimes T=c\not\le\bot\)).
- FP-synt: \(\boxtimes\bot=\bot\). ✓
- FG2: \(\boxtimes^2 T=T\not\le c=\boxtimes T\). FAILS.

This is the finite-model analogue of the Beklemishev-Shamkanov 2016 result:
the existence of a Jeroslow-style fixed point \(p=\boxtimes p\) does not imply
the formalized second incompleteness principle FG2.

References:
- [beklemishev_shamkanov_abstract_g2_beamer.pdf](https://drive.google.com/file/d/1Pkj6ZxECucSputAXulzhpYWuXxNnEf_J)
- See also `notes/bs16-fiber-residuated-aps.md`.

---

### Theorem 4: G2 + FG2 is consistent with ¬FP-synt.

Model **M-110**:

\[
L=\{T,c,\bot\},\quad T<c,\quad\bot\text{ isolated},
\quad \boxtimes T=c,\; \boxtimes c=T,\; \boxtimes\bot=T.
\]

- G2: \(\boxtimes T=c\not\le\bot\). Vacuous. ✓
- FG2: \(\boxtimes^2 T=T\le c=\boxtimes T\) since \(T<c\). ✓
- FP-synt: \(\boxtimes T=c\ne T\), \(\boxtimes c=T\ne c\), \(\boxtimes\bot=T\ne\bot\). NONE.

The n-FG2 pattern is TFTFTF... (same as M-010): FG2 holds but nFG2(2) fails.
FG2 holds here due to the order \(T<c\) not because the orbit stabilizes.

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

The n-FG2 pattern is determined by the \(\boxtimes\)-orbit of \(T\):

| Orbit type | Pattern | Models |
|-----------|---------|--------|
| Period-1 stabilization to FP | TTTTTTTT | M-011, M-111 |
| Period-2 with upward step | TFTFTFTF | M-010, M-110 |
| Period-2 without order relation | FFFFFFFF | M-000, M-001, M-100, M-101 |

**Proposition**: nFG2(\(k\)) iff \(\boxtimes^{k+1}T\le\boxtimes^k T\). The pattern
is periodic with period dividing the period of the \(\boxtimes\)-orbit of \(T\)
once the orbit enters its eventual cycle.

**Resolved below**: there is a uniform finite witness where nFG2(\(k\)) fails
for all \(k\le N\) but holds from \(k=N+1\) onward.

---

## Arbitrary-Depth First-True nFG2 Witnesses

For each \(N\ge 1\), define a finite preAPS \(D_N\) with carrier

\[
L_N=\{T,a_1,\ldots,a_{N+1},s\}.
\]

The order is reflexive plus the single non-reflexive relation:

\[
s\le a_{N+1}.
\]

Define \(\boxtimes\) by:

\[
\boxtimes T=a_1,\quad
\boxtimes a_i=a_{i+1}\ (1\le i\le N),\quad
\boxtimes a_{N+1}=s,\quad
\boxtimes s=s.
\]

This is antitone. The only nontrivial order relation is \(s\le a_{N+1}\), and
antitonicity there asks for
\(\boxtimes a_{N+1}=s\le s=\boxtimes s\), which holds.

The \(\boxtimes\)-orbit of \(T\) is:

\[
T\to a_1\to a_2\to\cdots\to a_{N+1}\to s\to s\to\cdots.
\]

For \(1\le k\le N\), nFG2(\(k\)) asks \(a_{k+1}\le a_k\), which is false by
construction. For \(k=N+1\), it asks \(s\le a_{N+1}\), which is true. All later
instances are \(s\le s\), also true.

Thus \(D_N\) proves arbitrary first-true depth for the nFG2 hierarchy:

\[
\neg\mathrm{nFG2}(1),\ldots,\neg\mathrm{nFG2}(N),
\quad
\mathrm{nFG2}(N+1),\mathrm{nFG2}(N+2),\ldots
\]

The generator
`scripts/new-nfg2-depth-witness.ps1` creates these models. The persisted
example `models/examples/nfg2-depth-3.json` is checked in
`outputs/g2-zoo-nfg2-depth-3.json` and has pattern `FFFTTTTT`.

---

## All-Level n-FG2 and Finite Orbit Stabilization

For a finite preAPS, all-level nFG2 has an exact orbit description.

**Theorem (finite orbit stabilization)**. Let \(S=(L,\le,\boxtimes,T,\bot)\)
be a finite preAPS. The following are equivalent:

1. \(\mathrm{nFG2}(k)\) holds for every \(k\ge 1\).
2. The tail orbit
   \(\boxtimes T,\boxtimes^2T,\boxtimes^3T,\ldots\) is non-increasing:
   \(\boxtimes^{k+1}T\le \boxtimes^kT\) for every \(k\ge 1\).
3. There is an \(N\ge 1\) such that
   \(\boxtimes T\ge\boxtimes^2T\ge\cdots\ge\boxtimes^NT\) and
   \(\boxtimes^NT\) is a syntactic fixed point.

The equivalence of (1) and (2) is definitional. For (2) to (3), finiteness
forces the non-increasing tail orbit to stabilize; if the stable value is
\(p=\boxtimes^NT\), then \(p=\boxtimes p\). The implication (3) to (2) is
immediate along the stated tail.

Consequently, all-level nFG2 implies a reachable syntactic fixed point in finite
models, but it does not imply G2: M-011 has all nFG2 levels true, a fixed point
at \(\bot\), and G2 false.

For infinite APS or non-Noetherian preorders, the proof breaks exactly at the
stabilization step. The useful next axiom candidate is therefore:

**Orbit well-foundedness**: every non-increasing \(\boxtimes\)-tail orbit from
\(\boxtimes T\) eventually stabilizes.

Under this axiom, the finite theorem extends verbatim to arbitrary preAPS.

## Non-Degenerate G2+FG2+FP Witness

Model `M4-G2FG2FP` is a 4-element non-collapsed witness where G2, FG2, and a
primitive syntactic fixed point all hold, with the fixed point at an interior
element \(p\), not at \(T\) or \(\bot\).

\[
L=\{\bot,p,c,T\},\quad \bot<p<T,\quad c<T,\quad c\parallel p,\quad c\parallel\bot,
\]

\[
\boxtimes T=p,\qquad \boxtimes p=p,\qquad
\boxtimes c=T,\qquad \boxtimes\bot=T.
\]

The checker report `outputs/g2-zoo-M4-G2FG2FP.json` verifies:

- G2: true, vacuously, since \(\boxtimes T=p\not\le\bot\);
- FG2: true, since \(\boxtimes^2T=p\le p=\boxtimes T\);
- FP-synt: true at \(p\);
- all checked nFG2 levels true by orbit \(T\to p\to p\to\cdots\);
- collapse: false.

This resolves the previously open "G2+FG2+FP with non-degenerate fixed point"
finite-model task. It remains open whether such a witness can be equipped with
nontrivial residual operations satisfying the intended APS axiom package.

### Full Residuation Search

The exhaustive search report
`outputs/residuated-search-M4-G2FG2FP.json` shows that `M4-G2FG2FP` has no
full residuated monoid expansion on the same carrier and order, for any choice
of unit among \(\{\bot,p,c,T\}\). The search enumerates all \(4^9=262144\)
binary operations compatible with each possible two-sided unit and rejects every
candidate after checking associativity, monotonicity, and existence of both
residuals.

Thus the non-degenerate G2+FG2+FP witness is not itself a residuated APS on this
underlying order. Any residuated version must either change the order, add
elements, weaken the residual requirement, or use a different witness family.

The smallest same-carrier order repair is now known. Adding just
\(\bot\le c\) to `M4-G2FG2FP` produces
`M4-G2FG2FP-order-plus-bot-c-residuated`, with the order
\(\bot<p<T\), \(\bot<c<T\), and \(p\parallel c\). The search report
`outputs/residuated-order-search-M4-G2FG2FP.json` finds a full residuated
expansion with unit \(p\). The model preserves non-collapse, G2, FG2, all
checked nFG2 levels, and the reachable fixed point at \(p\); see
`outputs/g2-zoo-M4-G2FG2FP-order-plus-bot-c-residuated.json`.

This repair has a concrete structural reading. The original M4 order already
has \(\bot\le p\), \(\bot\le T\), \(p\le T\), and \(c\le T\); its only missing
bottom-discipline instance is \(\bot\le c\). Adding that relation makes
\(\bot\) the actual least element and turns the order into the four-element
Boolean lattice. Thus the repair can be read as adding ex-falso/absurdity
weakening for the \(c\)-branch rather than as an arbitrary residuation trick.
Whether that principle is acceptable depends on the intended resource-sensitive
APS axiom package.

### Bottom Discipline Filter

The script `scripts/check-bottom-discipline.py` tests the finite G2-ZOO models
by adding every missing relation \(\bot\le x\), then checking whether the fixed
\(\boxtimes\) map remains antitone and whether the G2/FG2/FP/nFG2 behavior is
stable. The report is saved as
`outputs/bottom-discipline-filter-g2-zoo.json`.

The current finite witnesses split as follows:

| Model | Pure bottom-order repair keeps antitone? | Main effect |
|-------|------------------------------------------|-------------|
| `M-000` | yes | G2/FG2/FP stay false, but nFG2 changes from `FFFFFFFF` to `FTFTFTFT` |
| `M-010` | yes | FG2-not-G2 survives; all checked nFG2 become true and FP appears by \(0\sim\bot\) |
| `M-111` | yes | G2+FG2+FP stays stable |
| `M4-G2FG2FP` | yes | G2+FG2+FP stays stable; this is exactly the `bot <= c` repair |
| `M4-G2FG2FP-order-plus-bot-c-residuated` | already | already bottom-disciplined and stable |
| `bottom-nfg2-depth-3` | already | bottom-disciplined replacement with pattern `FFFTTTTT` |
| `bottom-G2FG2-noFP` | already | bottom-disciplined G2+FG2 without FP-synt |
| `M-001`, `M-011`, `M-100`, `M-101`, `M-110` | no | adding bottom pairs breaks antitonicity of \(\boxtimes\) |
| `nfg2-depth-3` | no | adding \(s\le T,a_1,a_2,a_3\) breaks antitonicity |

Pass 15 adds the missing bottom-disciplined arbitrary-depth replacement family.
Consequently bottom discipline preserves FG2-not-G2 via the repaired `M-010`,
and preserves G2-not-FG2, G2+FP-not-FG2, and arbitrary first-true nFG2 depth via
the bottom-disciplined \(B_N\) construction below. Pass 16 adds
`bottom-G2FG2-noFP`, so bottom discipline alone preserves all currently tracked
G2/FG2/FP-synt separations.

### Bottom-Disciplined Arbitrary-Depth Witnesses

For each \(N\ge 1\), define \(B_N\) with carrier

\[
\{b,T,a_1,\ldots,a_{N+1},s,U\}.
\]

The order has \(b\le x\le U\) for every carrier element \(x\), plus
\[
s\le a_{N+1}.
\]

Thus \(b\) is a genuine bottom element and \(B_N\) satisfies bottom discipline.
Define:

\[
\boxtimes b=U,\qquad
\boxtimes U=b,\qquad
\boxtimes T=a_1,\qquad
\boxtimes a_i=a_{i+1}\ (1\le i\le N),
\]

\[
\boxtimes a_{N+1}=s,\qquad
\boxtimes s=s.
\]

Antitonicity holds because every relation \(b\le x\) asks
\(\boxtimes x\le U=\boxtimes b\), every relation \(x\le U\) asks
\(b=\boxtimes U\le\boxtimes x\), and \(s\le a_{N+1}\) asks
\(s=\boxtimes a_{N+1}\le\boxtimes s=s\).

The \(T\)-orbit is again

\[
T\to a_1\to\cdots\to a_{N+1}\to s\to s\to\cdots.
\]

So nFG2(\(k\)) fails for \(k\le N\) and holds from \(N+1\) onward. Since
\(\boxtimes T=a_1\not\le b\), G2 holds vacuously; FG2 fails for \(N\ge 1\);
and FP-synt holds at \(s\). The generated depth-3 instance
`models/examples/bottom-nfg2-depth-3.json` is certified by
`outputs/g2-zoo-bottom-nfg2-depth-3.json` with pattern `FFFTTTTT`.

Pass 18 upgrades the checked depth-3 instance to full residuation on the same
carrier and order. The top-absorbing template uses \(T\) as unit, \(b\) as zero,
and sends every remaining nonzero, non-unit product to \(U\). The builder
`scripts/build-top-absorbing-residuated-expansion.py` verifies associativity,
monotonicity, principal left/right residuals, and the residuation law; see
`outputs/residuated-top-absorbing-report-bottom-nfg2-depth-3.json`. The
persisted expansion `bottom-nfg2-depth-3-residuated` keeps G2 true, FG2 false,
FP-synt true at \(s\), bottom discipline, and nFG2 pattern `FFFTTTTT`.

The same argument is uniform in \(N\). Let
\[
M_N=B_N\setminus\{b,T\}.
\]
Define a commutative tensor by
\[
b\otimes x=b,\qquad T\otimes x=x,\qquad
x\otimes y=U\quad(x,y\in M_N).
\]
This is a monoid with unit \(T\) and zero \(b\): after removing occurrences of
the unit, any product with \(b\) is \(b\), while any product of two elements of
\(M_N\) is \(U\), and \(U\in M_N\) absorbs all further non-unit nonzero
factors. Hence associativity is immediate by cases. Monotonicity follows from
the three kinds of order relation in \(B_N\): \(b\le x\), \(x\le U\), and
\(s\le a_{N+1}\). The first is absorbed by \(b\le(-)\), the second by
\((-)\le U\), and the last by the fact that both products with a non-unit
nonzero factor are \(U\), while products with \(b\) and \(T\) preserve the
relation.

For \(m\in M_N\), the residual fibers are principal:
\[
b\backslash c=U,\qquad T\backslash c=c,
\]
and
\[
m\backslash c=
\begin{cases}
U & c=U,\\
T & m\le c\ne U,\\
b & \text{otherwise.}
\end{cases}
\]
Commutativity gives the same table for right residuals. Thus every \(B_N\)
admits a same-carrier, same-order full-residuated expansion. The tensor is
deliberately coarse, so the open issue is no longer existence of full
residuation but whether a less top-collapsing tensor can carry the same
arbitrary-depth separations.

Pass 20 finds a less top-collapsing tensor for the checked \(B_3\) instance
under the still-strong constraint that \(U\otimes x=U\) for every nonzero
\(x\ne T\). The complete constrained search
`outputs/residuated-u-absorbing-search-bottom-nfg2-depth-3.json` minimizes the
number of \(U\)-valued products among the 15 unordered products on
\(\{a_1,a_2,a_3,a_4,s\}\). The top-absorbing template has 15 such products; the
new witness `bottom-nfg2-depth-3-u-absorbing-minU` has 7. Its non-\(U\) products
include:
\[
a_1^2=a_3,\quad a_1a_4=a_1s=a_2,\quad
a_2a_4=a_2s=a_3,\quad a_4^2=a_4s=s^2=a_1.
\]
The checker report `outputs/g2-zoo-bottom-nfg2-depth-3-u-absorbing-minU.json`
confirms that the G2/nFG2/FP profile is unchanged. This shows that the
top-absorbing tensor is sufficient but not minimal even inside the
\(U\)-absorbing search class.

Pass 21 tests the pattern at the next depth. A direct branch-and-bound search
for \(B_4\) did not finish within the local 120-second pass budget, but the
pass 20 table has a simple truncated-exponent reading. Give \(a_{N+1}\) and
\(s\) exponent 1, and give \(a_i\) exponent \(i+1\) for \(1\le i\le N\). Keep
\(T\) as unit, \(b\) as zero, and \(U\) absorbing over nonzero non-units; for
the remaining products, add exponents and return \(U\) exactly when the sum
exceeds \(N+1\). The builder
`scripts/build-truncated-u-absorbing-residuated.py` verifies this template for
`bottom-nfg2-depth-4`: it has 10 \(U\)-valued products among 21 unordered
products on \(\{a_1,\ldots,a_5,s\}\), rather than 21 for the top-absorbing
template, and preserves the `FFFFTTTT` profile. This supports a uniform
truncated-exponent \(B_N\) conjecture, now separated from the earlier
top-absorbing proof.

### Bottom-Disciplined G2+FG2 without FP

The remaining bottom-discipline separation is witnessed by
`bottom-G2FG2-noFP`. Its carrier is

\[
\{b,d,a,T,U\},
\]

with \(b\le x\le U\) for every \(x\) and one additional relation \(d\le a\).
The refutability map is:

\[
\boxtimes b=U,\quad \boxtimes U=b,\quad \boxtimes T=a,\quad
\boxtimes a=d,\quad \boxtimes d=a.
\]

Bottom discipline holds because \(b\) is least. Antitonicity holds because the
bounding pairs are absorbed by \(U\) and \(b\), and the only interior relation
\(d\le a\) maps to \(d=\boxtimes a\le\boxtimes d=a\). G2 holds vacuously since
\(\boxtimes T=a\not\le b\). FG2 holds because
\[
\boxtimes^2T=d\le a=\boxtimes T.
\]
There is no syntactic fixed point: \(b\leftrightarrow U\), \(a\leftrightarrow d\)
as a strict two-cycle, and \(T\mapsto a\) with \(T\not\sim a\). The checker
report `outputs/g2-zoo-bottom-G2FG2-noFP.json` verifies G2 true, FG2 true,
FP-synt false, and nFG2 pattern `TFTFTFTF`.

The same order also carries a full residuated expansion. A targeted commutative
search with unit \(T\) and absorbing zero \(b\) checks \(5^6=15625\) candidate
tensors and finds 8 full-residuated operations; see
`outputs/residuated-commutative-zero-search-bottom-G2FG2-noFP.json`. The
persisted expansion `bottom-G2FG2-noFP-residuated` uses \(T\) as the monoid
unit. Its tensor has \(b\) as zero, keeps \(U\) idempotent, and sends
\(a\otimes a=a\otimes d=d\otimes d=b\). Thus the bottom-disciplined
G2+FG2-without-FP separation survives full residuation on the same carrier and
order.

---

## Open Tasks

- Classify all non-isomorphic 3-element preAPS models by (G2, FG2, FP-synt, nFG2-pattern).
- Characterize the infinite analogue of finite orbit stabilization: which APS
  axiom packages imply orbit well-foundedness?
- Prove the truncated-exponent \(U\)-absorbing template uniformly for \(B_N\),
  including an explicit residual table; then test whether the \(U\)-absorbing
  assumption itself can be weakened.
- Compare with BS16 resource-sensitive separation and hidden-contraction analysis
  in `notes/bs16-fiber-residuated-aps.md`.
