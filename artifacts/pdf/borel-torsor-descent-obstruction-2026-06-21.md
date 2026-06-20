# Borel Torsor Descent Obstruction

Date: 2026-06-21

## Summary

Pass 91 decides the descent status of the restriction/span Borel torsor over
the finite singleton-prime cover site.  The global-Levi Borel package is not a
sheaf on multi-prime supports.  Its sheafification or stackification is the
local Loeb object, and the Rosser class is exactly the kernel lost in that
process.

For a finite support $S$,
$$
P(S)=\left(\prod_{p\in S}\mathbb Z_p\right)/\Delta\mathbb Z.
$$
The singleton-cover descent kernel is
$$
\mathbb Z^S/\Delta\mathbb Z\cong\mathbb Z^{|S|-1}.
$$

## Main Claims

- **Borel non-separatedness.** The global-Levi Borel prestack
  $\mathbb Q^\times\ltimes P(S)$ is not a sheaf for $|S|\ge2$.
- **Local Borel stackification.** The local object is
  $$(\mathbb Q^\times)^S\ltimes
  \prod_{p\in S}(\mathbb Z_p/\mathbb Z).$$
- **Rosser kernel.** The horizontal Rosser defect
  $\mathbb Z^S/\Delta\mathbb Z$ is the kernel lost under stackification.
- **Shear action.** The hyperbolic shear action transports global lifts with
  the same local data but does not choose a canonical zero section.

## Machine Verification

`code/scripts/check-pass91.py` produced
`artifacts/reports/pass91-borel-torsor-descent-obstruction-check.json` with
overall PASS.  It checks descent ranks $|S|-1$, finite kernel sizes
$N^{|S|-1}$, global Borel non-sheaf behavior on multi-prime supports,
local-Levi sheafification in a finite proxy, and the fact that shear
transports but does not kill descent-kernel lifts.

## Next Use

Pass 92 should relocate the Borel descent obstruction to the Zariski/generic
prime site and compare it with the Pass-63 $j_!$ ghost line.
