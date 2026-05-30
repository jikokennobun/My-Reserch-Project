# Self-Existence Sentences

Source: https://chatgpt.com/share/6a0fbc9d-be30-8324-9ae2-943bd3ed2b14

Imported: 2026-05-22

## Core Construction

Fix a theory $T$ and a one-variable formula $E(x)$, read as an existence predicate.

A sentence $\sigma$ is an $E$-self-existence sentence when:

$$
T\vdash \sigma \leftrightarrow E(\ulcorner\sigma\urcorner).
$$

By the diagonal lemma, if $T$ can represent the diagonal/substitution function, then such a $\sigma$ exists for any $E(x)$.

## Proof Pattern

Let $d(x)$ be the primitive recursive function sending the code of a one-variable formula to the code of its self-substitution:

$$
d(\ulcorner \theta(v)\urcorner)
=
\ulcorner \theta(\overline{\ulcorner \theta(v)\urcorner})\urcorner.
$$

Define a formula $\theta(v)$ that says:

$$
E(d(v)).
$$

Then put:

$$
\sigma := \theta(\ulcorner\theta\urcorner).
$$

By construction:

$$
T\vdash \sigma \leftrightarrow E(\ulcorner\sigma\urcorner).
$$

## Possible Meanings of $E(x)$

The phrase "exists" is not unique. Candidate interpretations:

- $x$ codes a well-formed sentence.
- $x$ is registered in a namespace.
- $x$ is constructible.
- $x$ is provably constructible.
- $x$ has a proof of existence.
- $x$ denotes a stable object in an APS/domain model.

Different choices of $E$ give different self-existence principles.

## APS Relevance

This gives a syntactic companion to the abstract fixed point assumption:

$$
\exists p(p=\boxtimes p).
$$

The question becomes: what is the APS-level analogue of an existence predicate $E$? One possibility is to treat existence as a modality or as membership in a definable part of a completion.

## Next Tasks

- Define $E(x)$ for "formula exists", "proof object exists", and "completion object is definable".
- Compare $E$-self-existence with Godel and Jeroslow fixed points.
- Relate this to [residuated-fixedpoint-existence.md](residuated-fixedpoint-existence.md).
- Explore whether "self-existence" can separate syntactic fixed points from completion fixed points.

