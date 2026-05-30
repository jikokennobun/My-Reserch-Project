# Research

Research-facing material lives here. This directory is the mathematical center
of the repository; code and artifacts should point back here when they certify,
export, or visualize a result.

## Directory Roles

- `definitions.md`: normalized APS/G2-ZOO definitions. Use this before adding
  new notation to a note.
- `open_problems.md`: active, resolved, and partially resolved research
  problems. Each problem should have a checkable next step.
- `bibliography.md`: citation anchors and publication-level bibliography.
- `notes/`: substantive research notes, including imported Project
  discussions. Notes should follow `../docs/research-note-quality-standard.md`.
- `ideas/`: staging area for questions that are not yet stable research notes.
- `references/`: indexes for Drive, ChatGPT shares, Obsidian vault material,
  and other external relay sources.

## Research Note Standard

A note in `notes/` should not remain a short summary once it is used as
research evidence. It should contain:

1. source/provenance;
2. precise definitions;
3. named claims, conjectures, or theorem schemas;
4. proof sketches or verification tasks;
5. relation to existing APS/G2-ZOO notes.

When an autonomous research pass produces a finished result, write a Markdown
summary under `../artifacts/pdf/` and publish it as a PDF through
`../code/scripts/publish-research-output.ps1`.

## Mathematical Spine

Most current notes orbit the following core data:

$$
S=(L,\le,\Box,\boxtimes,T,\bot),
$$

with:

$$
\mathrm{G2}(S):
\quad
\boxtimes T\le\bot\Rightarrow T\le\bot,
$$

and:

$$
\mathrm{FG2}(S):
\quad
\boxtimes\boxtimes T\le\boxtimes T.
$$

New notes should say explicitly whether they concern order-only APS, indexed
APS, residuated APS, proof-relevant APS, topological/domain-theoretic APS, or
syntactic diagonalization.
