# Code

Executable and machine-checkable material lives here. Code is treated as the
verification layer for the APS/G2-ZOO notes, not as a separate project.

## Directory Roles

- `scripts/`: checkers, generators, search tools, sync tools, and publication
  helpers.
- `models/`: finite APS/preAPS model schemas, named witnesses, and
  model-facing documentation.

## Verification Contract

When a research note states a finite-model claim, the preferred workflow is:

1. encode the model or search family under `models/`;
2. run the relevant checker from `scripts/`;
3. write the machine report under `../artifacts/reports/`;
4. cite that report from the research note.

For G2-ZOO work, the checked properties should include at least:

$$
\mathrm{G2},
\qquad
\mathrm{FG2},
\qquad
\mathrm{nFG2}(k),
\qquad
\mathrm{FP\text{-}synt}.
$$

When relevant, also record bottom discipline, antitonicity of $\boxtimes$,
residuated expansions, completion fixed points, and local-FG2 profiles.

## Publication Helpers

Research outputs intended as deliverables should be published with:

```powershell
powershell -ExecutionPolicy Bypass -File .\code\scripts\publish-research-output.ps1 -MarkdownPath .\artifacts\pdf\<name>.md
```

The resulting PDF is stored under `../artifacts/pdf/` and mirrored to the
configured Google Drive backup when the sync folder is available.
