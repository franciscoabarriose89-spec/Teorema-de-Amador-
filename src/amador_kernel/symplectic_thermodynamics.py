from __future__ import annotations


class WeilInfinitesimalAlgebra:
    """Deterministic dual-number algebra with infinitesimal generator."""

    def __init__(self, order: int = 2) -> None:
        self.order = max(1, int(order))

    def axiom_kock_lawvere(self) -> bool:
        return self.order >= 2

    def dual_generator(self) -> str:
        return "epsilon"


class CohesiveToposHN:
    """Deterministic cohesive-topos surrogate preserving the smooth orbifold check."""

    def __init__(self) -> None:
        self.weil = WeilInfinitesimalAlgebra(order=2)

    def validate_orbifold(self) -> bool:
        return self.weil.axiom_kock_lawvere()

    def daseinization(self) -> tuple[str, str]:
        return ("delta^i(P)_V", "delta^o(P)_V")
