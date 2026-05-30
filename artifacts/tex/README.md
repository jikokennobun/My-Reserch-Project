# TeX

TeX sources and compiled-paper source material go here. This directory is for
publication-oriented source, not for scratch notes.

## Role

Use this directory when a Markdown research note has matured into a paper-like
artifact requiring theorem environments, bibliographic control, or a stable PDF
layout.

## Expected Contents

- `.tex` sources for preprints or long technical appendices.
- Bibliography files used by those sources.
- Build notes when the TeX source requires a nonstandard command.

## Relationship to Markdown

The canonical early-stage source remains in `../../research/notes/` or
`../pdf/*.md`. When a TeX version is created, it should cite the originating
Markdown note and the generated PDF should also be collected under
`../pdf/`.

## Minimum Mathematical Shape

TeX material should expose definitions, lemmas, propositions, proof sketches,
examples, and open problems explicitly. Do not convert a thin Markdown stub to
TeX merely for formatting.
