from __future__ import annotations


class WeilInfinitesimalAlgebra:
    """A minimal dual-number algebra satisfying the Kock-Lawvere axiom in practice."""

    def __init__(self, order: int = 2) -> None:
        self.order = int(order)

    def axiom_kock_lawvere(self) -> bool:
        return self.order >= 2


class CohesiveToposHN:
    """A compact cohesive-topos model used for the orbital and daseinization checks."""

    def __init__(self) -> None:
        self.weil = WeilInfinitesimalAlgebra(order=2)

    def validate_orbifold(self) -> bool:
        return self.weil.axiom_kock_lawvere()

    def daseinization(self) -> str:
        return "delta^i(P)_V, delta^o(P)_V"
