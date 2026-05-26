# Models

This folder is for machine-checkable finite APS/preAPS models.

## Planned Artifacts

- JSON schema for finite APS models.
- Small 3- and 4-element countermodels.
- MacNeille reflection search protocol:
  [macneille-reflection-search.md](macneille-reflection-search.md).
- Checker interface for the first MacNeille reflection tool:
  [macneille-checker-interface.md](macneille-checker-interface.md).
- Smoke-test example:
  [examples/three-chain-antitone.json](examples/three-chain-antitone.json).
- G2-ZOO examples:
  [examples/M-000.json](examples/M-000.json) through
  [examples/M-111.json](examples/M-111.json), plus the 4-element
  [examples/M4-G2FG2FP.json](examples/M4-G2FG2FP.json).
- Scripts to check G2, FG2, nFG2, fixed point principles, MacNeille completion
  properties, and collapse conditions.

## Minimal Model Fields

- carrier
- order
- top
- bottom
- box
- refutability
- optional negation
- optional tensor/residuals
- metadata about satisfied principles
