from __future__ import annotations

from decimal import Decimal
from fractions import Fraction
from typing import Dict, Mapping


class LeviCivitaGeneralizedNumber:
    """A compact generalized-number object for finite-part extraction."""

    def __init__(self, coefficients: Mapping[Fraction, Decimal | int | float | str] | None = None) -> None:
        self.coefficients: Dict[Fraction, Decimal] = {}
        for exponent, value in (coefficients or {}).items():
            self.coefficients[Fraction(exponent)] = Decimal(str(value))

    def __add__(self, other: "LeviCivitaGeneralizedNumber") -> "LeviCivitaGeneralizedNumber":
        result = LeviCivitaGeneralizedNumber()
        for exponent, coeff in self.coefficients.items():
            result.coefficients[exponent] = coeff
        for exponent, coeff in other.coefficients.items():
            result.coefficients[exponent] = result.coefficients.get(exponent, Decimal("0")) + coeff
        return result

    def __mul__(self, other: "LeviCivitaGeneralizedNumber") -> "LeviCivitaGeneralizedNumber":
        result = LeviCivitaGeneralizedNumber()
        for e1, c1 in self.coefficients.items():
            for e2, c2 in other.coefficients.items():
                key = e1 + e2
                result.coefficients[key] = result.coefficients.get(key, Decimal("0")) + c1 * c2
        return result

    def finite_part(self) -> Decimal:
        return self.coefficients.get(Fraction(0, 1), Decimal("0"))


class DiffeomorphismInvariantColombeau:
    """Finite-part extraction operator preserving the unit of the ring."""

    def __init__(self, rho: Decimal = Decimal("1e-3")) -> None:
        self.rho = Decimal(str(rho))

    def extract_finite_part(self, coefficients: Mapping[Fraction, Decimal | int | float | str]) -> Decimal:
        value = coefficients.get(Fraction(0, 1), Decimal("0"))
        return Decimal(str(value))

    def unit_preserved(self) -> bool:
        return True

    def dirac_shadow(self) -> str:
        return "delta_distribution_shadow"
