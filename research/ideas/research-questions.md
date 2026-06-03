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
  even non-commutatively, incl. $S_3$.)** Capped-front successor **(Resolved,
  Pass 36: $\lvert G\rvert=1$ for every single-cap placement — antitonicity
  survives with forced $\boxtimes c=b$ and the Route-B
cascade is escaped, but no cap repairs the at/below-front fiber obstruction.)**
Selective-median successor **(Resolved, Pass 37: adjoining the single join
$m=T\vee e_G$ below the absorbing top makes the diagonal fiber principal, so
$\lvert G\rvert$ is unbounded for finite abelian fronts — the rigidity ceiling
was the missing join $T\vee e_G$.)** Non-abelian successor **(Resolved for the
tested battery, Pass 38: the same one-point median makes both diagonal fibers
principal for $S_3$, $D_4$, $Q_8$, $\mathbb Z/4$; $\#$(medians) $=1$ uniformly,
not a new group invariant.)**
- **(Resolved, Pass 39)** Uniform all-finite-groups non-abelian selective-median
  theorem: for *every* finite group $G$, $B_N^{\mathrm{med}}$ ($N=\lvert
  G\rvert$) with front $F_k\cong G$ and single join $m=T\vee e_G$ is fully
  two-sided residuated; $\#$(medians) $=1$ and max front-group order $=\infty$,
  uniformly. Proof = three $G$-free lemmas (ideal-extension associativity via
  the $G^1$-block $F\cup\{m\}\cong G^1$; monotonicity from the identity law
  $a_1\otimes a_j=a_j$; diagonal fibers always strand $\{T,e_G\}$, off-diagonal
  fibers strand no pair; right fibers via the anti-automorphism $\phi$). Battery
  $\mathbb Z/6,(\mathbb Z/2)^3,D_5,A_4,S_4$ (to order 24) reconfirms it.
- **(Resolved, Pass 40)** The selective median as a *free / least* construction.
  (a) *Uniqueness (stronger than minimality):* the poset $\mathcal M$ of
  admissible medians is a **singleton** $\{T\vee e_G\}$ — the least repair is the
  *only* repair, by the backwards-Cap-Ejection forcing; $m$ is a representable
  (free) repair, initial and terminal in $\mathcal M$. (b) *Infinite fronts:*
  residuation is **cardinality-free** (every fiber $\le4$ elts or cofinal-at-$U$;
  survives $\mathbb Z,\mathbb Q,S_\infty$ verbatim, DM completion of the front
  adds nothing); only the $\boxtimes$-*orbit/profile* needs finiteness, repaired
  by the limit FP $s_\omega=\bigwedge_n\boxtimes^n T$.
- **Active (Pass 41 target):** (a) *Limit-FP orbit completion:* model
  infinite-front $B_\infty^{\mathrm{med}}$ with $\boxtimes$-orbit decoupled from
  the residuated front, adjoin $s_\omega=\bigwedge_n\boxtimes^n T$, and test
  whether antitonicity + full residuation survive and all-level nFG2 is restored
  — and whether $s_\omega$ breeds a new join-deficient pair $\{T,s_\omega\}$,
  degrading the single median into a countable tower $m_0,m_1,\dots$ (b)
  *Multi-pair geometry:* with two group fronts $F^{(1)},F^{(2)}$, does $\mathcal
  M$ stay a singleton ($T\vee e_1\vee e_2$ serving both) or acquire genuine
  moduli?

