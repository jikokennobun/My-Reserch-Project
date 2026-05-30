# Claude Code Review Log

## State

- Started: 2026-05-25
- Mode: independent review and counterexample search for the Codex-centered
  research loop
- Source of truth: this repository
- Integration rule: Codex or the user decides which review items are promoted
  into notes, open problems, scripts, or model files.

## Review Format

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

## Reviews

### Review 1 - 2026-05-25 23:00 JST

Focus:

Audit the `antitone-dual-lower-cut-v0` extension rule and the current smoke-test
result. Determine whether the classification `principal-only` is mathematically
meaningful as a reflection criterion, and search for the smallest model exposing
a non-principal completion fixed point.

---

External Reviewer:

The classification `principal-only` is an inadequate surrogate for the reflection
property. The smoke-test reports the completion fixed point $\{b,m,t\} = i(t)$
as "principal at $t$," but the checker never asks whether $t = \boxtimes t$.
Manual inspection of the model `three-chain-antitone.json` shows $\boxtimes(t)=b$,
so $t$ is emphatically not a syntactic fixed point. The completion fixed point is
principal yet unreflected. The current classifier cannot distinguish these two
situations, and the existing documentation slogan

$$\text{completion fixed point} \neq \text{syntactic fixed point}$$

is already violated by the smoke-test model itself — but the checker reports this
as `principal-only` without flagging the failure of reflection. Every consumer of
the report who conflates "principal" with "reflected" will draw a wrong conclusion.

The deeper hidden assumption: because the smoke-test model is a chain (already
a complete lattice), $\widehat{L} = L$ and every MacNeille cut is trivially
principal. A lattice model can never produce a non-principal cut. The search
target specified in `code/models/macneille-reflection-search.md` ("find a model with
a non-principal completion fixed point") is unreachable inside the class of
lattice inputs. The search space must include non-lattice preorders.

---

Countermodel Hunter:

A non-principal completion fixed point exists at size 3, not 4.

**Model** (`three-element-nolattice-nosynt`):

$$L = \{0, a, b\},\quad 0 < a,\quad 0 < b,\quad a \parallel b,\quad
\bot = 0,\quad T = a.$$

Define $\boxtimes: 0 \mapsto a,\; a \mapsto 0,\; b \mapsto 0$.

Antitonicity: the only strict comparabilities are $0 < a$ and $0 < b$.
$\boxtimes(a) = 0 \leq a = \boxtimes(0)$ and $\boxtimes(b) = 0 \leq a = \boxtimes(0)$. ✓

Syntactic fixed points: $\boxtimes(0)=a\neq 0$, $\boxtimes(a)=0\neq a$,
$\boxtimes(b)=0\neq b$. None. ✓

MacNeille cuts of $L$: since $a \vee b$ does not exist in $L$,
the MacNeille completion adds exactly one non-principal cut:

$$i(0)=\{0\},\quad i(a)=\{0,a\},\quad i(b)=\{0,b\},\quad
q^* = \{0,a,b\}\text{ (non-principal: the missing join)}.$$

Under the **correct lower extension** $\widehat{\boxtimes}(C) = ((\boxtimes[C])^{l_L})^{u_L}$
(i.e., MacNeille closure in $\widehat{L^{op}}$):

$$\widehat{\boxtimes}(\{0\}) = \{a\},\quad
\widehat{\boxtimes}(\{0,a\}) = \{0,a,b\},\quad
\widehat{\boxtimes}(\{0,b\}) = \{0,a,b\},\quad
\widehat{\boxtimes}(\{0,a,b\}) = \{0,a,b\}.$$

Fixed point: $q^* = \{0,a,b\}$ satisfies $\widehat{\boxtimes}(q^*) = q^*$.
Classification: `nonprincipal-without-syntactic`. No reflection.

Under the **provisional rule** $\widehat{\boxtimes}(C) = ((\boxtimes[C])^{u_L})^{l_L}$
(MacNeille closure in $L$, wrong polarity):

$$\widehat{\boxtimes}(\{0\}) = \{0,a\},\quad
\widehat{\boxtimes}(\{0,a\}) = \{0,a\},\quad
\widehat{\boxtimes}(\{0,b\}) = \{0,a\},\quad
\widehat{\boxtimes}(\{0,a,b\}) = \{0,a\}.$$

Provisional fixed point: $\{0,a\} = i(a)$. Classification: `principal-only`.
But $\boxtimes(a) = 0 \neq a$, so this principal completion fixed point is also
unreflected. Worse, the provisional rule completely misses the genuine
non-principal fixed point $q^*$.

**Summary**: the provisional rule gives the wrong classification AND the wrong
fixed point on the first non-lattice model tested. This confirms the rule must
not be promoted beyond smoke-test status.

---

Implementation Auditor:

Three concrete defects in the current checker script
(`code/scripts/check-macneille-reflection.ps1`):

**Defect 1 — Wrong polarity in `Invoke-CompletedRefutability`.**

The function computes:

```powershell
foreach ($x in $Cut) { $image += $refutability[$x] }
return Get-MacNeilleClosure($image)   # L-closure, not L^op-closure
```

For an antitone map $\boxtimes: L \to L^{op}$ (monotone), the canonical lower
extension to $\widehat{L} \to (\widehat{L})^{op}$ requires closure in
$\widehat{L^{op}}$, not in $\widehat{L}$. The $L^{op}$-MacNeille closure of
$S \subseteq L$ is $(S^{l_L})^{u_L}$, not $(S^{u_L})^{l_L}$.

On the 3-chain (a lattice), both closures give the same result for the full cut,
so the bug is invisible. On the 3-element non-lattice above, they diverge.

**Defect 2 — Missing reflection check.**

The checker reports `principal: true` and `principalElement: "t"` for the
smoke-test completion fixed point, but never checks whether
$\boxtimes(\text{principalElement}) = \text{principalElement}$. The output
JSON should include a `reflected` boolean field:

```
"reflected": (principalElement != null) && (refutability[principalElement] == principalElement)
```

Without this field, every reader of the report conflates "principal" with
"reflected."

**Defect 3 — Extension condition not verified.**

The script does not check whether the chosen extension rule satisfies the
canonical extension condition $\widehat{\boxtimes}(i(a)) = i(\boxtimes a)$ on
principal cuts. For the smoke-test model, a one-line verification reveals:

$$\widehat{\boxtimes}_{\mathrm{prov}}(i(m)) = \{b,m,t\} \neq i(m) = \{b,m\}.$$

The extension condition FAILS at $m$ for the provisional rule. This should
appear as a warning in the report, not merely the blanket warning that the rule
is "provisional."

---

Integrator:

Concrete repository updates:

1. **New model file** `code/models/examples/three-element-nolattice-nosynt.json`:
   carrier $\{0,a,b\}$, $0<a$, $0<b$, $a\parallel b$, $\bot=0$, $T=a$,
   $\boxtimes: 0\mapsto a, a\mapsto 0, b\mapsto 0$.
   Expected classification under correct extension: `nonprincipal-without-syntactic`.
   This model should become the first test case for any corrected extension rule.

2. **New extension rule** `antitone-dual-lower-cut-v1` in the checker:
   Replace `Get-MacNeilleClosure($image)` with the $L^{op}$-closure
   $((\boxtimes[C])^{l_L})^{u_L}$. Specifically:

   ```powershell
   # L^op-closure: lower-bounds then upper-closure
   $lowerBounds = $carrier | Where-Object {
       $lb = $_
       $image | ForEach-Object { Test-Leq -Left $lb -Right $_ } | Where-Object { -not $_ } | Select-Object -First 1
   } | Where-Object { $null -eq $_ } # ... [full implementation needed]
   ```

   (Concrete PowerShell implementation should be left to Codex or the user.)

3. **New checker output field** `reflected` per completion fixed point:
   true iff `principal` AND `refutability[principalElement] == principalElement`.

4. **New primary classification** `principal-unreflected`: a principal completion
   fixed point where the principal element is not a syntactic fixed point. The
   smoke-test model falls into this class; currently it is misclassified as
   `principal-only`.

5. **Update `research/open_problems.md`**: add the problem "Characterize when principal
   completion fixed points are reflected (i.e., the principal element is also a
   syntactic fixed point)."

6. **Update `code/models/macneille-reflection-search.md`**: the 3-element non-lattice
   model above already achieves `nonprincipal-without-syntactic` under the
   correct extension. The search can now shift focus to characterizing which APS
   axiom packages allow or prevent this.

---

Suggested repository updates:

- `code/models/examples/three-element-nolattice-nosynt.json`: new model file (see above).
- `code/scripts/check-macneille-reflection.ps1`: add `reflected` field; add extension
  condition verification warning per principal cut.
- `code/models/macneille-checker-interface.md`: document $L^{op}$-closure formula;
  add `principal-unreflected` to output classification list; add `reflected` to
  computed data fields.
- `research/open_problems.md`: add "principal ≠ reflected" separation problem.
- `research/notes/completion-and-fixed-points.md`: add the $L^{op}$-closure formula as
  the definition of the correct antitone extension.

---

Questions for Codex:

1. Should `antitone-dual-lower-cut-v1` be defined as the lower or upper extension
   of $\boxtimes: L \to L^{op}$, or should both be computed and compared?
2. The 3-element non-lattice model has $T = a$ and $\boxtimes(T) = 0 = \bot$.
   Under G2: $\boxtimes T \leq \bot \Rightarrow T \leq \bot$, so antecedent
   is $\boxtimes a = 0 \leq 0$, which is TRUE, and consequent $a \leq 0$ is
   FALSE. Thus G2 FAILS. Is there a variant of the model with G2 holding?
3. Is `nonprincipal-without-syntactic` classifiable by any APS axiom schema, or
   does it require explicit model-theoretic separation?

---

Next step:

Add the `three-element-nolattice-nosynt` model file and run the existing checker
(which will give the wrong `principal-only` output, exposing Defect 1 visibly).
Then implement `antitone-dual-lower-cut-v1` and re-run to confirm
`nonprincipal-without-syntactic`. This sequence gives Codex a reproducible test
pair for the corrected extension rule.

