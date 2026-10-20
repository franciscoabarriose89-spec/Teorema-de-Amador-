from __future__ import annotations

import math
from typing import Iterable, List


class ProjectivePSKLOptimizer:
    """Deterministic PS-KL projector with strict-saddle verification."""

    def __init__(self, n: int = 12, gamma: float = 0.1) -> None:
        self.n = max(1, int(n))
        self.gamma = float(gamma)

    def project_to_ker_d_ev(self, vector: Iterable[float]) -> List[float]:
        values = [float(v) for v in vector]
        if not values:
            return []
        mean = sum(values) / len(values)
        return [v - mean for v in values]

    def strict_saddle_check(self, point: Iterable[float], hessian: Iterable[float]) -> bool:
        values = [float(v) for v in hessian]
        if not values:
            return False
        lam_min = min(values)
        threshold = max(self.gamma, 1.0 / self.n)
        return lam_min <= -threshold

    def polyak_lojasiewicz(self, objective_value: float, gradient_norm: float) -> float:
        if objective_value < 0.0:
            return 0.0
        geodesic_length = max(0.0, float(gradient_norm))
        theta = 0.5
        return theta if geodesic_length <= 1.0 else theta / max(1.0, geodesic_length)

    def effective_complexity(self) -> float:
        return float(self.n * math.log10(2.0))
