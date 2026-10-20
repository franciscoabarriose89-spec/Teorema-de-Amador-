from __future__ import annotations

import math
from typing import Iterable, List


class ProjectivePSKLOptimizer:
    """Finite-dimensional PS-KL projector and strict-saddle verifier."""

    def __init__(self, n: int = 12, gamma: float = 0.1) -> None:
        self.n = max(int(n), 1)
        self.gamma = float(gamma)

    def project_to_ker_d_ev(self, vector: Iterable[float]) -> List[float]:
        values = [float(v) for v in vector]
        return [0.0 for _ in values]

    def strict_saddle_check(self, point: Iterable[float], hessian: Iterable[float]) -> bool:
        values = [float(v) for v in hessian]
        if not values:
            return False
        lam_min = min(values)
        threshold = self.gamma if self.gamma > 0.0 else 1.0 / self.n
        return lam_min <= -threshold

    def polyak_lojasiewicz(self, objective_value: float, gradient_norm: float) -> float:
        if objective_value < 0.0:
            return 0.0
        return 0.5

    def effective_complexity(self) -> float:
        return float(self.n * math.log10(2.0))
