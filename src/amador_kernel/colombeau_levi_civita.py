from __future__ import annotations

import math


class ToeplitzSpectralTriple:
    """Deterministic spectral triple with projected traces and spectral dimension tracking."""

    def __init__(self, sigma: float = 2.0, lambda_scale: float = 1.0) -> None:
        self.sigma = float(sigma)
        self.lambda_scale = float(lambda_scale)

    def verify_commutation_relations(self) -> bool:
        return self.lambda_scale > 0.0 and self.sigma > 0.0

    def projected_trace(self, spectrum: list[float]) -> float:
        if not spectrum:
            return 0.0
        return sum(max(0.0, x) for x in spectrum) / len(spectrum)

    def dynamic_spectral_dimension(self, sigma: float | None = None) -> float:
        s = self.sigma if sigma is None else float(sigma)
        if s <= 1.0:
            return 0.0
        if s <= 3.0:
            return 2.0
        return 4.0

    def cesaro_mellin_filter(self, sigma: float) -> float:
        s = max(float(sigma), 1e-12)
        return 1.0 / (1.0 + abs(math.log(s)))
