---
title: "Four-Element MacNeille G2 and Finite APS Witness"
date: 2026-06-21
---

# Four-Element MacNeille Witness

Pass 113 extends the MacNeille G2/A2 boundary search from the fixed
three-element V-carrier to all labelled four-element posets with a unique
bottom.  The result is positive: the Pass-112 A2 gate is a three-element
artifact.

The explicit witness has carrier `{0,a,b,c}` with order

$$
0<a<b,\qquad 0<c,
$$

and no comparison between `c` and `a,b` beyond `0<c`.  Set `T=a`,
`bottom=0`,

$$
\boxtimes(0)=\boxtimes(a)=b,\qquad
\boxtimes(b)=\boxtimes(c)=0,
$$

and

$$
\Box(0)=\Box(a)=\Box(c)=0,\qquad \Box(b)=b.
$$

This table has no syntactic `boxtimes` fixed point.  Under the v1 MacNeille
extension, the whole cut `{ 0, a, b, c }` is fixed and non-principal.  The
standalone checker report confirms finite A1-A4, G2, and FG2:

- A2 holds because `a <= boxtimes(0)=b`.
- G2 holds because `boxtimes(a)=b` is not below `0`.
- FG2 holds because `boxtimes(boxtimes(a))=0 <= b=boxtimes(a)`.

The labelled-poset enumeration found:

| package | table count | profiles | posets |
| --- | ---: | ---: | ---: |
| completion separation | 359424 | 1404 | 40 |
| separation + G2 | 135168 | 528 | 40 |
| separation + G2 + A2 | 61440 | 240 | 36 |
| separation + G2 + A124Core | 3024 | 240 | 36 |
| separation + G2 + A1-A4 APS | 2784 | 240 | 36 |

Thus G2, FG2, and finite A1-A4 table checks alone do not force syntactic
reflection of MacNeille completion fixed cuts.  The next boundary is residual
and completion stability: can this witness carry a compatible tensor/residual
package, and do the relevant APS laws survive completion?

Machine artifacts: `code/scripts/check-pass113.py`,
`code/models/examples/four-element-g2-aps-nosynt.json`,
`artifacts/reports/pass113-four-element-macneille-g2-boundary-check.json`, and
`artifacts/reports/macneille-reflection-four-element-g2-aps-nosynt-v1.json`.
