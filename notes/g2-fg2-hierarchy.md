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

**Open**: Find a model with strictly increasing n-FG2 depth, i.e.,
nFG2(\(k\)) fails for all \(k\le N\) but holds for \(k=N+1\), for arbitrary \(N\).

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

---

## Open Tasks

- Classify all non-isomorphic 3-element preAPS models by (G2, FG2, FP-synt, nFG2-pattern).
- Characterize the infinite analogue of finite orbit stabilization: which APS
  axiom packages imply orbit well-foundedness?
- Determine whether a G2+FG2+FP-reachable witness such as `M4-G2FG2FP` can carry
  nontrivial residual operations.
- Build finite models separating \(n\)-FG2 at each depth \(N\) (find a model with
  nFG2 pattern first \(N\) entries all F and subsequent entry T).
- Compare with BS16 resource-sensitive separation and hidden-contraction analysis
  in `notes/bs16-fiber-residuated-aps.md`.
