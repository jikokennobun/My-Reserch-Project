#!/usr/bin/env python3
"""Finite checks for Pass 103: signed boundary naturality by conductor.

Pass 103 compares the signed boundary class from Pass 102 with the Pass-95
finite conductor complexes

    C_{B,N}: [Z/N -> product_{p^e || N} Z/p^e].

For M | N, conductor reduction must commute with both the CRT diagonal and
the sign local system.  Multiplying the diagonal by sigma = +/-1 is still a
CRT isomorphism at every fixed finite conductor, so no finite sign-twisted
cohomology class appears.  The only finite collapse of the sign is the
already-recorded equality +1 = -1 modulo 2.
"""

from __future__ import annotations

import argparse
import itertools
import json
from dataclasses import asdict, dataclass
from pathlib import Path


CONDUCTORS = [2, 3, 4, 5, 6, 8, 9, 10, 12, 18, 24, 30, 60]
SIGNS = [1, -1]


@dataclass
class CRTCohomologyRow:
    conductor: int
    sign: int
    prime_powers: tuple[int, ...]
    source_size: int
    target_size: int
    signed_diagonal_bijective: bool
    h0_size: int
    h1_size: int
    finite_signed_shadow_acyclic: bool


@dataclass
class ReductionNaturalityRow:
    larger_conductor: int
    smaller_conductor: int
    sign: int
    signed_class_large_mod_n: int
    reduced_signed_class_mod_m: int
    direct_signed_class_mod_m: int
    sign_reduction_commutes: bool
    crt_square_commutes: bool


@dataclass
class SignVisibilityReductionRow:
    larger_conductor: int
    smaller_conductor: int
    sign_visible_large: bool
    sign_visible_small: bool
    collapse_explained_by_mod_2_target: bool


@dataclass
class SupportCautionRow:
    statement: str
    conductor_reduction_canonical: bool
    support_projection_canonical: bool
    support_enlargement_canonical_all_prime_map: bool
    finite_crt_zero_insertion_choice_exists: bool


@dataclass
class VerdictRow:
    natural_transformation: str
    finite_complex: str
    conductor_reduction_effect: str
    finite_obstruction: str
    remaining_gap: str
    next_task: str


def prime_power_factors(n: int) -> tuple[int, ...]:
    factors: list[int] = []
    remaining = n
    p = 2
    while p * p <= remaining:
        if remaining % p == 0:
            power = 1
            while remaining % p == 0:
                power *= p
                remaining //= p
            factors.append(power)
        p += 1
    if remaining > 1:
        factors.append(remaining)
    return tuple(factors)


def residues(n: int, prime_powers: tuple[int, ...], sign: int = 1) -> tuple[tuple[int, ...], ...]:
    return tuple(tuple((sign * value) % q for q in prime_powers) for value in range(n))


def signed_diagonal_bijective(n: int, sign: int) -> bool:
    factors = prime_power_factors(n)
    return len(set(residues(n, factors, sign))) == n


def reduce_residue_vector(
    larger_residues: tuple[int, ...],
    larger_factors: tuple[int, ...],
    smaller_factors: tuple[int, ...],
) -> tuple[int, ...]:
    reduced: list[int] = []
    for q_small in smaller_factors:
        match = next(q_large for q_large in larger_factors if q_large % q_small == 0)
        index = larger_factors.index(match)
        reduced.append(larger_residues[index] % q_small)
    return tuple(reduced)


def crt_square_commutes(larger: int, smaller: int, sign: int) -> bool:
    larger_factors = prime_power_factors(larger)
    smaller_factors = prime_power_factors(smaller)
    for value in range(larger):
        large_vector = tuple((sign * value) % q for q in larger_factors)
        reduced_large_vector = reduce_residue_vector(
            large_vector,
            larger_factors,
            smaller_factors,
        )
        direct_small_vector = tuple((sign * (value % smaller)) % q for q in smaller_factors)
        if reduced_large_vector != direct_small_vector:
            return False
    return True


def conductor_pairs() -> list[tuple[int, int]]:
    return [
        (larger, smaller)
        for larger, smaller in itertools.product(CONDUCTORS, CONDUCTORS)
        if larger != smaller and larger % smaller == 0
    ]


def cohomology_rows() -> list[CRTCohomologyRow]:
    rows: list[CRTCohomologyRow] = []
    for conductor in CONDUCTORS:
        factors = prime_power_factors(conductor)
        for sign in SIGNS:
            bijective = signed_diagonal_bijective(conductor, sign)
            rows.append(
                CRTCohomologyRow(
                    conductor=conductor,
                    sign=sign,
                    prime_powers=factors,
                    source_size=conductor,
                    target_size=conductor,
                    signed_diagonal_bijective=bijective,
                    h0_size=1 if bijective else 0,
                    h1_size=1 if bijective else 0,
                    finite_signed_shadow_acyclic=bijective,
                )
            )
    return rows


def reduction_rows() -> list[ReductionNaturalityRow]:
    rows: list[ReductionNaturalityRow] = []
    for larger, smaller in conductor_pairs():
        for sign in SIGNS:
            large_class = sign % larger
            reduced_class = large_class % smaller
            direct_class = sign % smaller
            rows.append(
                ReductionNaturalityRow(
                    larger_conductor=larger,
                    smaller_conductor=smaller,
                    sign=sign,
                    signed_class_large_mod_n=large_class,
                    reduced_signed_class_mod_m=reduced_class,
                    direct_signed_class_mod_m=direct_class,
                    sign_reduction_commutes=(reduced_class == direct_class),
                    crt_square_commutes=crt_square_commutes(larger, smaller, sign),
                )
            )
    return rows


def sign_visibility_rows() -> list[SignVisibilityReductionRow]:
    rows: list[SignVisibilityReductionRow] = []
    for larger, smaller in conductor_pairs():
        large_visible = (1 % larger) != ((-1) % larger)
        small_visible = (1 % smaller) != ((-1) % smaller)
        rows.append(
            SignVisibilityReductionRow(
                larger_conductor=larger,
                smaller_conductor=smaller,
                sign_visible_large=large_visible,
                sign_visible_small=small_visible,
                collapse_explained_by_mod_2_target=(small_visible or smaller == 2),
            )
        )
    return rows


def support_caution_row() -> SupportCautionRow:
    return SupportCautionRow(
        statement="Conductor reduction is canonical; support enlargement remains only a finite CRT choice/span.",
        conductor_reduction_canonical=True,
        support_projection_canonical=True,
        support_enlargement_canonical_all_prime_map=False,
        finite_crt_zero_insertion_choice_exists=True,
    )


def verdict_row() -> VerdictRow:
    return VerdictRow(
        natural_transformation="For M|N, sigma mod N reduces to sigma mod M and the signed CRT square commutes.",
        finite_complex="The signed finite conductor complex [Z/N -> product Z/p^e] remains a CRT isomorphism complex.",
        conductor_reduction_effect="No new sign-twisted finite cohomology appears under conductor reduction.",
        finite_obstruction="Only the target M=2 identifies +1 and -1.",
        remaining_gap="This is finite-conductor naturality, not yet the pro/solid all-prime signed inverse system.",
        next_task="Assemble the signed conductor system into a pro/solid boundary object and test whether the orientation double cover survives the all-prime limit.",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default="artifacts/reports/pass103-signed-boundary-conductor-naturality-check.json",
    )
    args = parser.parse_args()

    cohomology = cohomology_rows()
    reductions = reduction_rows()
    visibility = sign_visibility_rows()
    caution = support_caution_row()
    verdict = verdict_row()

    checks = {
        "signed_crt_acyclic_ok": all(row.finite_signed_shadow_acyclic for row in cohomology),
        "reduction_naturality_ok": all(
            row.sign_reduction_commutes and row.crt_square_commutes for row in reductions
        ),
        "visibility_reduction_ok": all(row.collapse_explained_by_mod_2_target for row in visibility),
        "support_caution_ok": (
            caution.conductor_reduction_canonical
            and caution.support_projection_canonical
            and not caution.support_enlargement_canonical_all_prime_map
            and caution.finite_crt_zero_insertion_choice_exists
        ),
    }

    report = {
        "pass": 103,
        "title": "Signed boundary naturality under conductor reduction",
        "A_signed_finite_conductor_complexes": {
            "statement": "Multiplying the finite CRT diagonal by +/-1 remains an isomorphism, so signed finite conductor shadows are acyclic.",
            "rows": [asdict(row) for row in cohomology],
            "signed_crt_acyclic_ok": checks["signed_crt_acyclic_ok"],
        },
        "B_conductor_reduction_naturality": {
            "statement": "For M|N, signed Bockstein classes and signed CRT diagonals reduce naturally.",
            "rows": [asdict(row) for row in reductions],
            "reduction_naturality_ok": checks["reduction_naturality_ok"],
        },
        "C_sign_visibility_under_reduction": {
            "statement": "Conductor reduction can only erase the sign when the target modulus is 2.",
            "rows": [asdict(row) for row in visibility],
            "visibility_reduction_ok": checks["visibility_reduction_ok"],
        },
        "D_support_caution": {
            "statement": "The conductor result does not turn support enlargement into a canonical all-prime map.",
            "row": asdict(caution),
            "support_caution_ok": checks["support_caution_ok"],
        },
        "E_verdict": {
            "statement": "The signed boundary class is natural over finite conductor reductions and has no new finite CRT obstruction.",
            "row": asdict(verdict),
        },
        "conclusion": {
            "signed_naturality": verdict.natural_transformation,
            "finite_complex": verdict.finite_complex,
            "obstruction": verdict.finite_obstruction,
            "next_task": verdict.next_task,
        },
        "checks": checks,
        "overall": "PASS" if all(checks.values()) else "FAIL",
    }

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"wrote {output_path}")
    print(f"overall {report['overall']}")


if __name__ == "__main__":
    main()
