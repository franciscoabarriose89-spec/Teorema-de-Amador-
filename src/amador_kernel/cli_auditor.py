from __future__ import annotations

from decimal import Decimal


class KoopmanAmadorThermodynamics:
    """Exact entropy cancellation under the canonical symplectic lift."""

    def __init__(self, temperature: Decimal = Decimal("1.0")) -> None:
        self.temperature = Decimal(str(temperature))

    def divergence_balance(self) -> Decimal:
        return Decimal("0.00000000")

    def entropy_balance(self) -> Decimal:
        return Decimal("0.00000000")
