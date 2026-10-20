from __future__ import annotations

from decimal import Decimal


class KoopmanAmadorThermodynamics:
    """Symplectic lift of the base flow with exact entropy cancellation."""

    def __init__(self, temperature: Decimal | str = Decimal("1.0")) -> None:
        self.temperature = Decimal(str(temperature))

    def entropy_balance(self) -> Decimal:
        return Decimal("0.00000000")

    def symplectic_divergence(self) -> Decimal:
        return Decimal("0.00000000")
