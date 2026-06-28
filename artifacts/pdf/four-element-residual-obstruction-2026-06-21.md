---
title: "Four-Element Same-Order Residual Obstruction"
date: 2026-06-21
---

# Four-Element Same-Order Residual Obstruction

Pass 114 tests the Pass-113 MacNeille witness for a same-carrier, same-order
residuated tensor expansion.  The witness has carrier `{0,a,b,c}` and order

$$
0<a<b,\qquad 0<c,
$$

with `b` incomparable to `c`.  It satisfies finite A1-A4, G2, and FG2 as a
table check, has no syntactic `boxtimes` fixed point, and has the
non-principal MacNeille fixed cut `{0,a,b,c}`.

The residual search keeps this exact carrier and order fixed.  For every
possible unit, it enumerates every binary operation with that unit as a
two-sided unit, then keeps operations that are associative, monotone in both
arguments, and admit both residuals by the principal-downset criterion.

The exhaustive counts are:

| unit | operation space | associative | associative+monotone | full residual |
| --- | ---: | ---: | ---: | ---: |
| `0` | 262144 | 156 | 0 | 0 |
| `a` | 262144 | 156 | 6 | 0 |
| `b` | 262144 | 156 | 18 | 0 |
| `c` | 262144 | 156 | 32 | 0 |

Across all units, 624 tensors are associative and 56 are associative and
monotone, but none admits both residuals.  The first named obstruction among
the surviving units is the fiber

$$
\{x:0\otimes x\le0\}=\{0,a,b,c\}.
$$

This is the whole carrier.  Since the carrier has no greatest element, the
fiber is not a principal downset and cannot be represented by a residual
element.

The result is therefore a fixed-carrier and fixed-order no-go: the Pass-113
witness is not yet a residuated APS witness.  It does not rule out order
repairs, completion-level tensors, or other four-element witnesses.  The next
test is to add the weakest top/join repair that makes the whole-carrier fiber
principal, then re-check finite A1-A4, G2, FG2, and MacNeille separation.

Machine artifacts: `code/scripts/check-pass114.py`,
`artifacts/reports/pass114-four-element-residual-boundary-check.json`, and
`artifacts/reports/pass114-four-element-witness-residuated-tensor-search.json`.
