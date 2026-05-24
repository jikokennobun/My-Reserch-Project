# MacNeille Reflection Checker Interface

This note defines the planned interface for a finite MacNeille reflection
checker.

First implementation:
[../scripts/check-macneille-reflection.ps1](../scripts/check-macneille-reflection.ps1).

## Planned Command

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\check-macneille-reflection.ps1 `
  -ModelPath .\models\examples\three-element-example.json `
  -ExtensionRule antitone-dual-lower-cut-v0 `
  -OutputPath .\outputs\macneille-reflection-report.json
```

## Inputs

- `ModelPath`: JSON file conforming to `models/finite-aps-schema.json`.
- `ExtensionRule`: named rule for extending \(\boxtimes\) to MacNeille cuts.
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

- MacNeille closed lower cuts \(C=(C^u)^l\);
- principal cuts \(i(a)=(\{a\}^u)^l\);
- syntactic fixed points \(p=\boxtimes p\) in \(L\);
- completed fixed points \(q=\widehat{\boxtimes}q\) under the selected rule;
- whether each completed fixed point is principal;
- G2 and FG2 status when the required terms are available.

## Output Classification

Each model receives exactly one primary classification:

- `no-completion-fixed-point`
- `principal-only`
- `nonprincipal-without-syntactic`
- `nonprincipal-with-rounding-candidate`

The report must also include warnings for unchecked APS axioms, missing optional
operations, or extension-rule limitations.

## First Milestone

The first implementation supports:

- finite preorders;
- total `box` and `refutability` maps;
- MacNeille cuts by exhaustive subset enumeration;
- the provisional `antitone-dual-lower-cut-v0` extension rule;
- JSON and console-table output.

No result from the first milestone should be treated as a theorem until the
extension rule is reviewed against the completion-reflection square.
