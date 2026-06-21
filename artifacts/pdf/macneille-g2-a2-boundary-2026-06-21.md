---
title: "MacNeille G2/A2 Boundary on the Smallest Non-Lattice Carrier"
date: 2026-06-21
---

# MacNeille G2/A2 Boundary

Pass 112 refines the MacNeille reflection search by adding finite APS
A1-A4 table checks to the checker output.  The result is a small but useful
boundary statement: on the fixed three-element non-lattice carrier
`{0,a,b}` with `0<a` and `0<b`, completion-created non-principal fixed cuts
can coexist with finite A1-A4, and they can coexist with G2 only if A2 is
dropped.

The current v1 witness `three-element-nolattice-nosynt` still has no
syntactic `boxtimes` fixed point.  Its MacNeille completion still has the
non-principal fixed cut `{ 0, a, b }`.  The new `apsAxioms` report fields show
that finite A1-A4 hold for this table, but G2 fails because
`boxtimes(T) <= bottom` while `T <= bottom` is false.

The exhaustive fixed-carrier search enumerated all total antitone
`boxtimes` tables and all total `Box` tables on the same V-shaped carrier.
It found:

| package | separating tables |
| --- | ---: |
| completion separation | 216 |
| separation + G2 | 54 |
| separation + G2 + A2 | 0 |
| separation + G2 + A124Core | 0 |
| separation + G2 + A1-A4 APS | 0 |
| separation + A1-A4 APS but not G2 | 10 |

Thus A2 is the first gate on this carrier.  The G2 examples are vacuous-G2
examples whose antecedent is false; the finite APS examples satisfy A2 but
fall on the non-G2 side.

This is not a global reflection theorem.  The checker still separates finite
table checks from residuals and completion-stability assumptions.  The next
test is to move from the fixed three-element V-carrier to four-element
carriers and ask whether a genuine G2+A2 completion-separation witness appears
there.

Machine artifacts:

- `artifacts/reports/pass112-macneille-g2-boundary-check.json`
- `artifacts/reports/macneille-reflection-three-element-nolattice-nosynt-v1.json`
- `code/scripts/check-pass112.py`
