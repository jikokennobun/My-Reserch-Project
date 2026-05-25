# Claude Code Autonomous Review Prompt

Use this prompt inside Claude Code from the repository root.

Run one independent research review pass for this repository. Your job is to
complement the Codex autonomous loop, not to duplicate it.

Read:

- `docs/claude-code-research-bridge.md`
- `docs/codex-research-automation.md`
- `logs/autonomous-discussion.md`
- `logs/claude-code-review.md`
- `ideas/research-questions.md`
- `open_problems.md`
- `definitions.md`
- the most relevant topic notes under `notes/`
- relevant files under `models/` and `scripts/` when the focus concerns model
  search or implementation

Then perform one compact review pass with these roles:

- External Reviewer: identify the strongest objection or hidden assumption.
- Countermodel Hunter: propose the smallest model/search direction that could
  falsify or stress-test the current claim.
- Implementation Auditor: check whether scripts, schemas, or reports actually
  support the mathematical claim being made.
- Integrator: convert the useful output into repository-ready next steps.

Append the result to `logs/claude-code-review.md` using this format:

```text
### Review N - YYYY-MM-DD HH:MM JST

Focus:

External Reviewer:

Countermodel Hunter:

Implementation Auditor:

Integrator:

Suggested repository updates:

Questions for Codex:

Next step:
```

Guidelines:

- Prefer concise, actionable criticism over broad exposition.
- Do not fabricate private ChatGPT Project content, paper details, citations, or
  theorem attributions.
- If a claim needs a source, record it as a source gap.
- If you edit files, keep edits small and focused. Do not rewrite
  `logs/autonomous-discussion.md`; append to `logs/claude-code-review.md`
  instead.
- Do not commit or push unless the user explicitly asks for that.
- When reviewing scripts, run the relevant local check if it is available.

