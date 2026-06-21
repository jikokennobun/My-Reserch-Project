# Barycentric Transition Denominators

Autonomous discussion Pass 109 computes the rational transition between
barycentric repair sections under a support inclusion.

Let $S\subset T$ be finite supports with $|S|=n$ and $|T|=m$.  The
barycentric sections are
$$
s_{\mathrm{bar},S}(1)=\frac1n\mathbf 1_S,\qquad
s_{\mathrm{bar},T}(1)=\frac1m\mathbf 1_T.
$$
After zero-extending the first vector to $T$, define
$$
\tau_{S,T}=e_{S,T}s_{\mathrm{bar},S}(1)-s_{\mathrm{bar},T}(1).
$$
Then
$$
(\tau_{S,T})_p=
\begin{cases}
\frac{m-n}{nm}, & p\in S,\\[2mm]
-\frac1m, & p\in T\setminus S.
\end{cases}
$$
The coordinate sum is zero, so $\tau_{S,T}\in K_T\otimes\mathbb Q$.

The exact denominator is
$$
\operatorname{den}(\tau_{S,T})=\operatorname{lcm}(n,m).
$$
Indeed, writing $g=\gcd(n,m)$, $n=ga$, and $m=gb$, an integer clearing the
off-support entries must be of the form $gbq$, and the on-support entries
are integral exactly when $a\mid q$.

Clearing by the minimal denominator gives
$$
\eta_{S,T}:=\operatorname{lcm}(n,m)\tau_{S,T}.
$$
This vector has entries $(m-n)/g$ on $S$ and $-n/g$ on $T\setminus S$.  It is
zero-sum and primitive, because these two integer values are $b-a$ and $-a$
with $\gcd(a,b)=1$.

For a chain $S\subset T\subset U$, the rational transitions satisfy
$$
e_{T,U}\tau_{S,T}+\tau_{T,U}=\tau_{S,U}.
$$
After clearing all terms by a common conductor, this identity also holds
integrally.  The individually primitive cleared vectors have different
normalizing conductors, so their chain behavior is a rescaling problem.

The comparison with finite conductor and CRT bookkeeping is conservative.  A
finite conductor $N$ clears $\tau_{S,T}$ exactly when
$\operatorname{lcm}(n,m)\mid N$, but the ordinary and signed CRT maps at
finite conductor remain bijections.  Thus the barycentric transition is
normalized rational support-comparison data, not a new finite CRT cohomology
class.

The checker
`artifacts/reports/pass109-barycentric-transition-denominator-check.json`
verifies the transition formula, kernel condition, exact lcm denominator,
conductor-clearance criterion, primitivity of the minimally cleared vector,
chain coboundary identity, and persistence of CRT and signed CRT bijections.

The next task is to study the primitive conductor-cleared vectors
$\eta_{S,T}$ along support chains and decide whether their rescaled edge law
defines useful oriented-support data.
