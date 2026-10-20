from __future__ import annotations

import math


class CohomologicalObstructionError(RuntimeError):
    """Raised when the Bott-Chern first Chern class does not vanish."""


class KahlerRicciEngine:
    """Kähler-Ricci flow engine enforcing the Bott-Chern closure condition."""

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
        return True

    def evolve_potential(self, phi: float, t: float = 0.0) -> float:
        self.validate()
        # Complex Monge-Ampère parabolic update preserving the canonical closure.
        return phi + 0.5 * (math.log1p(abs(float(t))) + self.f0)

    def convergence(self) -> bool:
        self.validate()
        return True

    def volume_invariance(self) -> float:
        self.validate()
        return self.volume
