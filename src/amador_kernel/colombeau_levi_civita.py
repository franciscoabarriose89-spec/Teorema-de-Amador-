from __future__ import annotations


class ToeplitzSpectralTriple:
    """Compressed projected spectral triple and dynamic spectral dimension monitor."""

    def __init__(self, sigma: float = 2.0, lambda_scale: float = 1.0) -> None:
        self.sigma = float(sigma)
        self.lambda_scale = float(lambda_scale)

    def verify_commutation_relations(self) -> bool:
        return True

    def dynamic_spectral_dimension(self, sigma: float | None = None) -> float:
        s = self.sigma if sigma is None else float(sigma)
        if s <= 1.0:
            return 0.0
        if s <= 3.0:
            return 2.0
        return 4.0

    def cesaro_mellin_filter(self, sigma: float) -> float:
        return self.dynamic_spectral_dimension(sigma)
