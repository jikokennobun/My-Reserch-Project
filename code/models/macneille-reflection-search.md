# MacNeille Reflection Search

This note specifies the first finite search target for completion-generated
versus syntactic fixed points.

## Goal

Find a small finite APS/preAPS candidate where MacNeille completion produces a
fixed point of the completed refutability operator, then classify whether that
fixed point is principal.

The desired outcomes are:

1. a principal reflected fixed point $q=i(p)$, confirming that the search
   setup can recover syntactic fixed points; or
2. a non-principal fixed cut $q\neq i(p)$, giving a concrete test case for
   failure of reflection.

## Search Space

Start with carriers of size $3$ and $4$. For each candidate:

- choose a preorder $\le$;
- choose distinguished $T$ and $\bot$;
- choose $\Box:L\to L$;
- choose antitone $\boxtimes:L\to L$;
- optionally choose negation, tensor, and residuals only after the bare APS
  search is stable.

## MacNeille Step

For $X\subseteq L$, compute:

$$
X^u=\{a:\forall x\in X,\ x\le a\},
\qquad
X^l=\{a:\forall x\in X,\ a\le x\}.
$$

The MacNeille completion consists of cuts $C=(C^u)^l$, ordered by inclusion.
The principal embedding is:

$$
i(a)=(\{a\}^u)^l.
$$

## Extension Discipline

For every candidate, record the exact extension rule for $\boxtimes$. Because
$\boxtimes$ is antitone on $L$, treat it first as a monotone map

$$
L\to L^{op}
$$

before comparing any completed value back with $\widehat L$. A result is not
usable unless its polarity convention is explicit.

The planned checker interface is specified in
[macneille-checker-interface.md](macneille-checker-interface.md). Its first
extension rule is only provisional and should be recorded as part of every
result.

## Classification Fields

Each candidate should record:

- carrier size;
- preorder;
- $T$, $\bot$, $\Box$, and $\boxtimes$;
- which APS/preAPS axioms or fragments are checked;
- whether G2 holds;
- whether FG2 holds;
- whether $p=\boxtimes p$ has a solution in $L$;
- whether $q=\widehat{\boxtimes}q$ has a solution in $\widehat L$;
- whether each completion fixed point is principal;
- if non-principal, whether any compact/definable rounding path is visible.

## First Target

The first target is a 3-element preorder with no primitive
$\boxtimes$-fixed point in $L$ but with a non-principal completion fixed
point in $\widehat L$, if such a candidate exists under the chosen extension
rule.

If no 3-element candidate exists, move to 4 elements and keep the failed search
as useful evidence about the strength of the reflection condition.

## Legacy v0 Checker Result

Report:
[../../artifacts/reports/macneille-reflection-three-chain-antitone.json](../../artifacts/reports/macneille-reflection-three-chain-antitone.json).

- Model: `three-chain-antitone`
- Extension rule: `antitone-dual-lower-cut-v0`
- Classification: `principal-only` under the legacy label set
- Syntactic fixed point: `m`
- Completed fixed point: `{ b, m, t }`, principal at `t`
- G2: false
- FG2: false
- A1-A4: not checked by the first milestone

This is a smoke-test baseline, not a reflection counterexample. Claude Code
Review 1 identified `antitone-dual-lower-cut-v0` as the wrong polarity for an
antitone $L\to L^{op}$ extension, so current passes should use v1.

## v1 Checker Results

Chain smoke test:
[../../artifacts/reports/macneille-reflection-three-chain-antitone-v1.json](../../artifacts/reports/macneille-reflection-three-chain-antitone-v1.json).

- Model: `three-chain-antitone`
- Extension rule: `antitone-dual-lower-cut-v1`
- Classification: `principal-unreflected`
- Syntactic fixed point: `m`
- Completed fixed point: `{ b, m, t }`, principal at `t`, not reflected because
  $\boxtimes t=b\neq t$
- G2: false
- FG2: false
- Principal extension condition: no failures when the v1 target is read as the
  dual principal cut $i_{L^{op}}(\boxtimes a)$

Non-lattice separation example:
[../../artifacts/reports/macneille-reflection-three-element-nolattice-nosynt-v1.json](../../artifacts/reports/macneille-reflection-three-element-nolattice-nosynt-v1.json).

- Model: `three-element-nolattice-nosynt`
- Extension rule: `antitone-dual-lower-cut-v1`
- Classification: `nonprincipal-without-syntactic`
- Syntactic fixed points: none
- Completed fixed point: `{ 0, a, b }`, non-principal
- G2: false
- FG2: false
- Principal extension condition: no failures

The size-3 non-lattice search target is therefore resolved for bare finite
preAPS data. The next substantive search should test which APS axiom packages
rule out this non-principal completion fixed point, or find a G2-holding
variant with the same separation.

Legacy v0 control on the same non-lattice model:
[../../artifacts/reports/macneille-reflection-three-element-nolattice-nosynt-v0.json](../../artifacts/reports/macneille-reflection-three-element-nolattice-nosynt-v0.json).

- Model: `three-element-nolattice-nosynt`
- Extension rule: `antitone-dual-lower-cut-v0`
- Classification: `principal-unreflected`
- Syntactic fixed points: none
- Completed fixed point: `{ 0, a }`, principal at `a`, not reflected
- Principal extension condition: two failures
- Interpretation: this is the wrong-polarity baseline that v1 replaces, not a
  current reflection witness.

Pass 111 verification audit:
[../../artifacts/reports/pass111-macneille-reflection-review-check.json](../../artifacts/reports/pass111-macneille-reflection-review-check.json).

The audit checks the v1 non-lattice witness, the v0 control, the v1 chain
smoke test, and documentation markers for `reflected`,
`principal-unreflected`, and the v1 dual principal-cut convention. Its result
is PASS. The next search target is now the G2/APS boundary: add axiom-package
checks and test whether the non-principal completion fixed cut can coexist
with G2 without a syntactic fixed point.
