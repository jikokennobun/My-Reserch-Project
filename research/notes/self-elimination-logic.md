# Self-Elimination Logic

Source: https://chatgpt.com/share/6a143fbc-a1b0-8321-9149-bb06c05af8b7

Imported: 2026-05-30

## Core Idea

This thread explores a "self-elimination" or "self-killing" logic where the
self-reference is not about truth or provability, but about axiomhood itself.

The motivating forms are:

$$
E \leftrightarrow \text{``}E\text{ is not an axiom / is deleted''}
$$

and the global nihilistic sentence:

$$
N \equiv \text{``this system has no axioms.''}
$$

The main warning is that this should not be read as an ordinary static classical
theory. If axiomhood reflection is unrestricted, the system collapses.

## Static Collapse

Let $\operatorname{Ax}(x)$ be an axiomhood predicate and put:

$$
N:=\forall x\,\neg \operatorname{Ax}(x).
$$

If $N$ itself is an axiom and the system proves axiomhood of every axiom, then:

$$
\vdash \operatorname{Ax}(\ulcorner N\urcorner)
$$

and also, by instantiating $N$,

$$
\vdash \neg \operatorname{Ax}(\ulcorner N\urcorner).
$$

With classical explosion, the theory becomes trivial.

## Dynamic Reading

The proposed nontrivial reading separates:

- candidate axioms;
- active axioms;
- deleted axioms;
- proof closure;
- deletion/update operations.

The logic is therefore closer to nonmonotonic or dynamic semantics than to a
single static consequence relation. It may be modelled by a deletion operator
on axiom states:

$$
A_{n+1}=A_n\setminus D(A_n),
$$

where $D(A)$ is the set of axioms marked for deletion by the current state.

## Expected Phenomena

- Self-deleting axioms can create two-cycles.
- Global deletion principles may have no stable fixed point.
- Soft deletion and hard deletion should be separated.
- External stabilization may choose among possible stable extensions.
- Monotonicity can fail because adding an axiom may trigger deletion of itself
  or of other axioms.

## Relation to Current Project

This is not currently an APS theorem, but it is relevant as a nearby
fixed-point and anti-fixed-point phenomenon:

$$
\text{fixed point of truth/provability}
\quad\text{versus}\quad
\text{anti-fixed point of axiomhood/deletion}.
$$

It may connect to:

- non-normal modal logics without necessitation or monotonicity;
- default logic and stable-extension semantics;
- argumentation frameworks;
- resource-sensitive accounts where contraction/weakening are not automatic.

## Next Tasks

- Define a minimal self-elimination system with hard and soft deletion.
- Prove the static-collapse proposition as a baseline.
- Build finite-state transition examples showing fixed points, two-cycles, and
  no-fixed-point behavior.
- Decide whether the deletion operator belongs in APS proper, weak APS, or a
  separate "prelogic" layer.
