# MacNeille Reflection Checker Interface

This note defines the planned interface for a finite MacNeille reflection
checker.

First implementation:
[../scripts/check-macneille-reflection.ps1](../scripts/check-macneille-reflection.ps1).

## Planned Command

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\check-macneille-reflection.ps1 `
  -ModelPath .\code\models\examples\three-element-example.json `
  -ExtensionRule antitone-dual-lower-cut-v1 `
  -OutputPath .\artifacts\reports\macneille-reflection-report.json
```

## Inputs

- `ModelPath`: JSON file conforming to `code/models/finite-aps-schema.json`.
- `ExtensionRule`: named rule for extending $\boxtimes$ to MacNeille cuts.
  The current default is `antitone-dual-lower-cut-v1`; legacy reports may still
  use `antitone-dual-lower-cut-v0`.
- `OutputPath`: optional JSON report path. If omitted, the checker prints a
  compact table to stdout.

## Required Validation

The checker should reject a model unless:

- every named element in `top`, `bottom`, `box`, and `refutability` belongs to
  `carrier`;
- `order` is reflexive and transitive;
- `box` and `refutability` are total maps on `carrier`;
- `refutability` is antitone with respect to `order`;
- the selected `ExtensionRule` is written into the report.

## Computed Data

For each accepted model, compute:

- MacNeille closed lower cuts $C=(C^u)^l$;
- principal cuts $i(a)=(\{a\}^u)^l$;
- syntactic fixed points $p=\boxtimes p$ in $L$;
- completed fixed points $q=\widehat{\boxtimes}q$ under the selected rule;
- whether each completed fixed point is principal;
- whether each principal completed fixed point is reflected by an actual
  syntactic fixed point;
- whether the selected extension rule preserves principal cuts. For v1, the
  expected target is the dual principal cut
  $i_{L^{op}}(\boxtimes a)$, not the lower-cut principal $i_L(\boxtimes a)$;
- finite A1-A4 table status in an `apsAxioms` block;
- G2 and FG2 status when the required terms are available.

## Output Classification

Each model receives exactly one primary classification:

- `no-completion-fixed-point`
- `reflected-only`
- `principal-unreflected`
- `nonprincipal-without-syntactic`
- `nonprincipal-with-rounding-candidate`

Legacy v0 reports may contain `principal-only`; treat that label as a pre-review
classification that did not distinguish reflected from principal-unreflected
fixed points.

The report must also include warnings for unchecked APS axioms, missing optional
operations, extension-rule limitations, or principal-extension failures.

## First Milestone

The first implementation supports:

- finite preorders;
- total `box` and `refutability` maps;
- MacNeille cuts by exhaustive subset enumeration;
- the current `antitone-dual-lower-cut-v1` extension rule, which treats
  antitone refutability as a monotone map $L\to L^{op}$ and uses
  $((\boxtimes[C])^{l_L})^{u_L}$;
- the legacy `antitone-dual-lower-cut-v0` extension rule, retained only to
  reproduce earlier output and expose the wrong-polarity issue;
- JSON and console-table output.

No checker result should be treated as an APS theorem until the relevant APS
axioms and completion-stability assumptions are verified for the model family.

The first finite APS fields are intentionally table-level:

- `A1BoxMonotone`
- `A1BoxtimesAntitone`
- `A2TopLeBoxtimesBottom`
- `A3CollisionCut`
- `A4BoxtimesLeBoxBoxtimes`
- `A124Core`
- `APS`

Reports also retain a warning that residuals and completion-stability
assumptions are not checked.

## Pass 111 Audit Status

The Claude Code review repair is audited by
`../../artifacts/reports/pass111-macneille-reflection-review-check.json`.
The audit verifies:

- v1 on `three-element-nolattice-nosynt` gives
  `nonprincipal-without-syntactic` with fixed cut `{ 0, a, b }`;
- legacy v0 on the same model gives `principal-unreflected` with fixed cut
  `{ 0, a }` and two principal-extension failures;
- v1 on `three-chain-antitone` gives `principal-unreflected`, separating the
  syntactic fixed point `m` from the completed fixed cut principal at `t`;
- the interface and research notes contain the repaired rule and
  classification vocabulary.

## Pass 112 Boundary Status

The Pass-112 report
`../../artifacts/reports/pass112-macneille-g2-boundary-check.json` verifies the
smallest G2/A2 boundary on the fixed three-element non-lattice carrier.  The
v1 witness satisfies finite A1-A4 but fails G2.  Conversely, G2 separation
tables exist on that carrier only vacuously and disappear as soon as A2 is
required.

Next interface extension: add explicit residual and completion-stability
fields, then generalize the search driver from the fixed V-carrier to
four-element carriers.

## Pass 113 Boundary Status

The four-element search driver
`../scripts/check-pass113.py` now enumerates all labelled four-element posets
with a unique bottom.  It reports a positive finite-table witness:
`examples/four-element-g2-aps-nosynt.json`.  The corresponding checker output
is
`../../artifacts/reports/macneille-reflection-four-element-g2-aps-nosynt-v1.json`.

This witness verifies that `g2`, `fg2`, and `apsAxioms.APS` can all be true
while the v1 MacNeille completion has a non-principal fixed cut and the
original carrier has no syntactic fixed point.  The report still records only
finite table checks; residual operations and completion-stability fields remain
the next interface gap.

## Pass 114 Residual Boundary Status

The fixed-carrier residual boundary is now checked separately by
`../scripts/check-pass114.py`.  It keeps
`examples/four-element-g2-aps-nosynt.json` on the same carrier and order and
enumerates every two-sided-unit tensor for every possible unit.  The report
`../../artifacts/reports/pass114-four-element-residual-boundary-check.json`
records 1,048,576 operation tables, 624 associative tensors, 56
associative+monotone tensors, and zero tensors with both residuals.

The first named obstruction is the non-principal fiber
`{x : 0 tensor x <= 0} = {0,a,b,c}`.  This should be treated as a residual
interface field in the next checker iteration: reports should distinguish
finite table APS status, same-carrier residual obstruction, order-repair
residual success/failure, and completion-stability status.
