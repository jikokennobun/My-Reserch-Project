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

Next interface extension: add explicit APS axiom-package fields so reports can
say which of A1-A4, G2, FG2, residuation, and completion-stability assumptions
were actually checked.
