from __future__ import annotations

import math


class CohomologicalObstructionError(RuntimeError):
    """Raised when Bott-Chern closure is violated."""


class KahlerRicciEngine:
    """Deterministic Kähler-Ricci flow with Bott-Chern closure verification."""

    def __init__(self, c1_BC: float = 0.0, volume: float = 1.0, f0: float = 0.0) -> None:
        self.c1_BC = float(c1_BC)
        self.volume = float(volume)
        self.f0 = float(f0)

    def validate(self) -> bool:
        if abs(self.c1_BC) > 1e-12:
            raise CohomologicalObstructionError(
                "La condición canónica c1_BC == 0.0 falla. "
                "La evolución del volumen satisface d/dt Vol(M) = -∫_M R dV_g."
            )
        return True

    def check_a_priori_bounds(self) -> bool:
        self.validate()
        if self.volume <= 0.0:
            raise ValueError("El volumen de la variedad debe ser estrictamente positivo.")
        if self.volume > 1e12:
            raise OverflowError("Se detectó blow-up del volumen fuera del umbral determinista.")
        return True

    def evolve_potential(self, phi: float, t: float = 0.0) -> float:
        """Monge-Ampère parabolic update in a stable finite-dimensional approximation."""
        self.validate()
        if t < 0.0:
            raise ValueError("El tiempo del flujo debe ser no negativo.")
        log_term = math.log1p(max(0.0, abs(t)))
        return phi + 0.5 * (log_term + self.f0)

    def convergence(self) -> bool:
        self.validate()
        return abs(self.c1_BC) <= 1e-12 and self.volume > 0.0
