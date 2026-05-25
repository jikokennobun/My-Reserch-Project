# Claude Code Research Bridge

This note defines how to add Claude Code as a second autonomous research agent
without replacing the existing Codex-centered loop.

## Purpose

Use Claude Code for independent review, counterexample search, and implementation
audits over the same repository state that Codex uses. The goal is not to create
two competing sources of truth. The repository remains the shared ledger, while
Codex and Claude Code contribute different passes over it.

## Recommended Division

- Codex: scheduled repository discussion, Drive/ChatGPT relay checks, scripts,
  Git-tracked synthesis, and final integration.
- Claude Code: adversarial review, proof-obligation discovery, finite-model
  search planning, code review of research scripts, and alternative formulations.
- Shared source of truth: Markdown notes, model JSON files, generated reports,
  and logs in this repository.
- Human role: choose the focus and decide which Claude Code suggestions should
  be promoted into notes, scripts, or open problems.

## Shared Files

- `docs/claude-code-autonomous-review-prompt.md`: stable prompt for Claude Code.
- `logs/claude-code-review.md`: Claude Code review results and suggested tasks.
- `outputs/claude-code/`: generated handoff packets for one-off Claude Code runs.
- `logs/autonomous-discussion.md`: Codex autonomous discussion state.
- `logs/research-log.md`: short project-level trace of meaningful events.

## Operating Loop

1. Codex or the user chooses a concrete focus.
2. Generate a handoff packet:

   ```powershell
   powershell -ExecutionPolicy Bypass -File .\scripts\new-claude-code-handoff.ps1 -Focus "Review the MacNeille extension rule and propose the next finite-model search."
   ```

3. Open Claude Code in the repository root and give it the generated handoff
   packet, or paste the stable prompt from
   `docs/claude-code-autonomous-review-prompt.md`.
4. Claude Code writes or proposes its review in `logs/claude-code-review.md`.
5. Codex incorporates accepted items into `open_problems.md`, `ideas/`, `notes/`,
   `models/`, or `scripts/`, then records the integration in
   `logs/research-log.md`.

## Conflict Discipline

- Codex remains responsible for final synthesis and Git push unless the user
  explicitly asks Claude Code to commit.
- Claude Code should prefer appending review entries over rewriting existing
  Codex discussion logs.
- If Claude Code changes files, Codex should review the diff before treating the
  result as project state.
- Neither agent should fabricate paper details, private ChatGPT Project content,
  or citation claims. Missing sources should be recorded as source gaps.

## High-Value Claude Code Tasks

- Challenge a Codex pass: look for hidden assumptions, unstated variance
  conventions, or overclaimed mathematical consequences.
- Audit a checker script against its interface note and model schema.
- Propose small finite model candidates, then leave exact verification to the
  checker script.
- Convert a proof sketch into named definitions, lemmas, and failure cases.
- Review whether a generated note should become an open problem, a conjecture,
  a model-search task, or a literature-search task.

## Minimal Success Criteria

A useful Claude Code pass should produce at least one of:

- a sharper proof obligation,
- a plausible counterexample or search target,
- a concrete implementation defect or missing test,
- a cleaner formulation of a definition or conjecture,
- a source gap that should block further claims.

