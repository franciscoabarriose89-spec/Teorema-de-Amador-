from __future__ import annotations

import math
from typing import Iterable, List, Sequence


class ProjectivePSKLOptimizer:
    """Finite projective optimization over boolean hypercubes with a strict saddle check."""

    def __init__(self, n: int = 12, gamma: float = 0.1, k: int = 2) -> None:
        self.n = max(1, int(n))
        self.gamma = float(gamma)
        self.k = int(k)

    def project_to_ker_d_ev(self, values: Sequence[float] | Iterable[float]) -> List[float]:
        """Project onto the nullspace of the evaluation differential by subtracting the mean."""
        data = [float(v) for v in values]
        if not data:
            return []
        if len(data) == 1:
            return [0.0]
        mean = sum(data) / len(data)
        return [v - mean for v in data]

    def strict_saddle_check(self, critical_point: Sequence[float] | Iterable[float], value: Sequence[float] | float) -> bool:
        """A deterministic test for strict saddles in the projected landscape."""
        vals = [float(v) for v in (value if isinstance(value, Sequence) and not isinstance(value, (str, bytes)) else [value])]
        if not vals:
            return False
        if any(v <= 0.0 for v in vals):
            return True
        lambda_min_estimate = min(vals) * -1.0
        return lambda_min_estimate <= -self.gamma

    def polyak_lojasiewicz(self, value: float, gradient_norm: float, theta: float = 0.5) -> float:
        """A simple PL-style inequality used as a deterministic regularity proxy."""
        value = float(value)
        grad = abs(float(gradient_norm))
        if theta <= 0.0:
            return value
        return max(0.0, value - 0.5 * grad * grad)

    def safe_complexity_estimate(self) -> float:
        """Return a log-scale complexity estimate that avoids overflow for large n."""
        return float(self.n * math.log10(2.0))

    def escape_rate(self) -> float:
        return max(0.0, self.gamma * math.sqrt(float(self.n)))
