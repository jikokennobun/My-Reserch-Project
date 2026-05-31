# Research Questions

## Active

- APS/G2周辺の構造を、論理・代数・証明論のどの軸で分類するのが自然か。
- Google Drive文献フォルダの分類と、研究ノート側の概念分類をどう対応させるか。
- $\exists p(p=\boxtimes p)$ と $\exists p(p=\neg\Box p)$ は、どのAPS/preAPS条件のもとで分離または崩壊するか。
- 完備化で得た不動点は、いつ構文的・定義可能な固定点へ反映されるか。
- 解析的APSでは、対角化補題をどの固定点定理で置き換えるべきか。
- 剰余付きdcpo/quantaleを APS/G2-ZOO の基本意味論にできるか。
- ChatGPT share-link ingestion is intermittent in this PowerShell environment: checks at `2026-05-25T22:59:42+09:00`, `2026-05-26T05:01:25+09:00`, `2026-05-27T07:05:18+09:00`, `2026-05-27T19:01:24+09:00`, `2026-05-28T01:03:13+09:00`, `2026-05-28T10:56:03+09:00`, `2026-05-28T17:33:45+09:00`, `2026-05-29T22:53:25+09:00`, `2026-05-30T05:03:17+09:00`, and `2026-05-30T17:36:14+09:00` failed (`remote server unreachable`), but `2026-05-27T13:01:02+09:00` and `2026-05-29T14:27:21+09:00` succeeded (`unchanged`). Decide on a fallback ingestion path (alternate network, different fetch method, or manual exports) so share diffs can resume reliably.
- The watched ChatGPT share link for `Local-FG2 Pullback and APS Zoo` returned HTTP 404 at `2026-05-26T18:02:00+09:00`, but was reachable again as of `2026-05-27T13:01:02+09:00`. Keep monitoring; if 404 recurs, re-share and update `research/references/chatgpt-share-watchlist.csv`.
- Google Drive folder scanning: keep validating the Drive-research outputs (Paper/Slide/Gemini/Claude) for new PDFs/slides/AI outputs, and summarize any new material into local notes.
- Does the finite orbit-stabilization theorem for all-level nFG2 extend to infinite APS under an existing proof-theoretic axiom, or does it require a new orbit well-foundedness/no-infinite-descent condition?
- Which nontrivial APS axiom packages preserve the arbitrary-depth $D_N$ nFG2 first-true witnesses, and which force collapse of the first-true depth?
- Can the orthogonal front-width theorem be upgraded from the current
  machine-checked closed residual formula to a polished paper lemma? (The
  non-orthogonal escape is now closed: Pass 34's front-rigidity theorem shows a
  commutative residuated front of $B_N$ is *forced* to be the orthogonal
  idempotent zero-band, so no nontrivial group front exists.)
- Does dropping commutativity reopen group fronts? Can a non-integral
  two-residual ($\backslash,/$) tensor on $B_N$ host a nontrivial finite group on
  the front, or does two-sided monotonicity still force $U$-absorption and the
  diagonal-residual failure? **(Resolved, Pass 35: rigidity is a genuine
  $B_N$-order phenomenon — two-sided $U$-absorption is forced, both diagonal
  fibers strand the incomparable $\{T,a_{i_0}\}$ pair, so $\lvert G\rvert=1$
  even non-commutatively, incl. $S_3$.)** Live successor: **capped-front /
  ceiling relaxation** — adjoin a sub-top cap $c<U$ above the front
  ($a_i\le c<U$) and ask whether $B_N^{\mathrm{cap}}$ hosts a nontrivial group
  front with $a_j\otimes c=c\otimes a_j=c$, whether antitonicity of $\boxtimes$
  survives an off-orbit cap (the same-carrier Route B died by an antitonicity
  cascade), and whether a deeper G2/nFG2 obstruction forbids group fronts in
  *every* finite bottom-disciplined ambient.
- Classify which finite commutative residuated structures (beyond the orthogonal
  band) can appear as integral tensor ideals glued onto the shifted $B_N$ tail.
- How should local/formalized G2 principles such as $\mathrm{LG2}(a)$ and
  $\mathrm{FG2}[q]$ be added to the G2-ZOO without confusing Horn rules with
  internal implication propositions?
- Which weak-APS packages capture Feferman/Shavrukov/Rosser-style provability
  predicates as controlled A4 failures while still preserving useful G2-like
  conclusions?
- Can self-elimination logic be modelled as a finite dynamic axiom-deletion
  system with stable extensions, two-cycles, and no-fixed-point cases?
- What is the minimal fibred/indexed sequentiality condition needed to supply
  a Jeroslow-style fixed point for APS?

## Later

## Resolved

- Google Drive folder scanning via the Drive MCP connector was blocked (handshake timeout) in prior runs, but was reachable again as of 2026-05-27.
