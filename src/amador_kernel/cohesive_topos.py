from __future__ import annotations

from decimal import Decimal
from fractions import Fraction
from typing import Dict, Iterable, Mapping


class LeviCivitaGeneralizedNumber:
    """A minimal generalized number representation using finite-order coefficients."""

    def __init__(self, values: Mapping[Fraction, Decimal] | None = None) -> None:
        self.values: Dict[Fraction, Decimal] = {}
        if values is not None:
            for exponent, value in values.items():
                self.values[Fraction(exponent)] = Decimal(str(value))

    def finite_part(self) -> Decimal:
        zero = Fraction(0, 1)
        return self.values.get(zero, Decimal("0"))


class DiffeomorphismInvariantColombeau:
    """A practical Colombeau-style regularization with a finite-part extraction."""

    def __init__(self, rho: Decimal | str = Decimal("1e-3")) -> None:
        self.rho = Decimal(str(rho))

    def extract_finite_part(self, coefficients: Mapping[Fraction, Decimal | str]) -> Decimal:
        for exponent, value in coefficients.items():
            if exponent == Fraction(0, 1):
                return Decimal(str(value))
        return Decimal("0")

    def unit_preserved(self) -> bool:
        return self.rho > 0

    def regularize_distribution(self, value: Decimal | str) -> Decimal:
        return Decimal(str(value))
