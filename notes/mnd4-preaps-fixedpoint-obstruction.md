# MND4-preAPS and Fixed Point Obstruction

Source: https://chatgpt.com/share/6a0fbc5a-a86c-8322-8ce7-1888af5f455e

Imported: 2026-05-22

## Core Distinction

There are two different fixed point readings:

\[
p =_S \boxtimes p
\]

and

\[
p =_S \neg\Box p.
\]

The first is a Jeroslow/refutability-style fixed point where \(\boxtimes\) may be primitive. The second is a Godel-style fixed point where refutability is identified with classical negated provability.

The conversation's main conclusion is:

\[
\text{Classical }MND4\text{-preAPS}+\exists p(p=_S\neg\Box p)
\Longrightarrow
T\le \bot.
\]

If \(L\) is a bounded poset with \(\bot\) least and \(T\) greatest, this collapses the quotient order:

\[
L/{=}_S \text{ is one-point.}
\]

But the raw structure

\[
MND4\text{-preAPS}+\exists p(p=_S\boxtimes p)
\]

does not by itself force triviality, especially when \(\boxtimes\) is treated as a primitive refutability operator.

## Why This Matters

This separates two mechanisms:

- Primitive refutability fixed points can exist without immediate collapse.
- Classical Godel fixed points \(p=\neg\Box p\) interact with \(D/4\)-style provability conditions and explosion principles much more destructively.

For APS/G2-ZOO purposes, this is useful because it prevents conflating:

\[
\exists p(p=\boxtimes p)
\]

with

\[
\exists p(p=\neg\Box p).
\]

The former is closer to Beklemishev-Shamkanov abstract G2. The latter is closer to classical Godel sentence obstruction.

## Conditions to Formalize

The collapse result appears to require some classical package such as:

- \(\boxtimes x = \neg\Box x\), or another explicit reduction of refutability to negated provability.
- \(\neg\neg x = x\).
- A relative explosion principle:

\[
x\le y,\quad x\le \neg y
\Longrightarrow
x\le \bot.
\]

- Enough contraction or diagonal reuse to apply the same resource to both provability and refutability information.

## Next Tasks

- Write a precise definition of \(MND4\)-preAPS.
- Separate primitive \(\boxtimes\) from definitional \(\neg\Box\).
- Prove the collapse theorem under a clearly listed classical package.
- Build a small nontrivial model of \(MND4\)-preAPS with a primitive \(\boxtimes\)-fixed point.
- Compare the obstruction with [bs16-fiber-residuated-aps.md](bs16-fiber-residuated-aps.md), especially the role of hidden contraction.

## Related Drive Files

- [APS_dissertation.pdf](https://drive.google.com/file/d/1VtS6tSvhUcoIG01fWprIrxGKZ3vZPjxc)
- [aps_g2_zoo_research_notes_lualatex_thesis_expanded.pdf](https://drive.google.com/file/d/14hb_IBDliXyj3SG-2sn9bxlZ8Iibe8U3)
- [beklemishev_shamkanov_abstract_g2_beamer.pdf](https://drive.google.com/file/d/1Pkj6ZxECucSputAXulzhpYWuXxNnEf_J)

