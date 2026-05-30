# Research Note Quality Standard

This document fixes the minimum standard for Markdown research notes in this
repository. It is meant to prevent imported Project discussions, automated
research outputs, and handwritten notes from becoming thin summaries.

## Target Level

A research note should be readable as a small preprint seed. It need not prove
every claim completely, but it must make the mathematical object clear enough
that a specialist can check, extend, or refute it.

For Project-derived imports, do not compress the discussion to a short
paraphrase. Preserve the mathematical content by reconstructing the actual
definitions, distinctions, examples, and proof obligations that appeared in the
conversation.

## Required Shape

Each substantive research note should contain the following sections, unless a
section is genuinely inapplicable.

### Source and Provenance

Record the source link, import date, and access status. If the source is
temporarily unreachable, say so explicitly and separate direct extraction from
mathematical reconstruction.

### Abstract

Give a compact statement of the central problem, not merely the topic label.
The abstract should say what structure is studied, what principle is being
tested, and why it matters for APS/G2-ZOO.

### Background and Notation

Fix notation before using it. If the note uses APS, write at least:

$$
S=(L,\le,\Box,\boxtimes,T,\bot).
$$

State the intended reading of $T$, $\bot$, $\Box$, and $\boxtimes$, and link to
`research/definitions.md` when the note uses repository-wide terminology.

### Definitions

Definitions should be formal enough to be implemented or checked. Avoid phrases
such as "some topology" or "some categorical construction" unless followed by
candidate definitions.

Acceptable forms include:

$$
\mathrm{G2}(S):
\quad
\boxtimes T\le\bot\Rightarrow T\le\bot,
$$

or a typed categorical datum such as:

$$
P:C^{op}\to\mathbf{Preord}.
$$

### Lemmas and Propositions

Record claims as named lemmas, propositions, or conjectures. Even if the proof
is incomplete, give the expected proof route and the exact assumptions used.
Do not mix theorem strength with motivational prose.

### Examples and Counterexamples

When the claim concerns G2/FG2 separation, local FG2, topological taming, or
fixed points, include at least one of:

- a known finite model from `code/models/`;
- a candidate model profile to search for;
- a minimal abstract example showing why the assumptions are nontrivial.

### Relation to Existing Notes

Every note should explain how it touches at least one existing line:

- G2/FG2/nFG2 hierarchy;
- APS-ZOO classification;
- fixed-point existence and reflection;
- indexed/fibred APS;
- residuated APS;
- proof-relevant or categorical semantics.

### Open Problems

End with concrete tasks that can be checked. Prefer questions of the form
"prove X under assumptions A" or "find finite preAPS with profile P" over
"think about X".

## Markdown and PDF Rules

Use display math for long formulas. Avoid dense inline formulas that wrap badly
in GitHub.

Every autonomous research result that is meant as an output artifact must be:

1. written in Markdown;
2. converted to PDF;
3. collected under `artifacts/pdf/`;
4. backed up to the configured Drive/local PDF collection when available.

## Thin Note Remediation Rule

A note is considered thin if it has only a source link, a topic sentence, and a
task list. Thin notes must be upgraded before they are cited as research
evidence. The upgrade must add definitions, at least one claim or conjecture,
and at least one concrete verification task.
