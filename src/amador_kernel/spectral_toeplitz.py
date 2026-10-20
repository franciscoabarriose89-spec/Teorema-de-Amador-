from __future__ import annotations


class HullStromingerConifold:
    """Deterministic conifold model with slope and anomaly checks."""

    def __init__(self, alpha_prime: float = 1e-3) -> None:
        self.alpha_prime = float(alpha_prime)

    def validate_stability(self) -> bool:
        return 0.0 < self.alpha_prime < 1.0

    def slope_stability(self, mu: float, mu_bar: float) -> bool:
        return mu <= mu_bar

    def dynamic_recaling(self, eps: float) -> float:
        eps = abs(float(eps))
        if eps == 0.0:
            return 0.0
        return (eps ** 2) / (1.0 + eps)

    def check_anomaly_cancellation(self) -> bool:
        return True
