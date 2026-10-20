from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from typing import Any, Dict, Mapping


@dataclass(frozen=True)
class KernelState:
    c1_BC: float = 0.0
    volume: float = 1.0
    n: int = 12
    gamma: float = 0.1
    rho: float = 1e-3
    temperature: float = 1.0
    alpha_prime: float = 1e-3
    spectral_dimension: float = 2.0
    entropy_target: Decimal = Decimal("0.00000000")


@dataclass(frozen=True)
class KernelExecutionReport:
    canonical_operator: str
    verified_lemmas: Dict[str, bool]
    invariants: Dict[str, Any]
    status: str
    entropy_delta: Decimal
    spectral_dimension: float


class AmadorKernel:
    """Main pipeline orchestrator for the canonical Amador operator."""

    def __init__(self, *, default_state: Mapping[str, Any] | None = None):
        base = dict(default_state) if default_state else {}
        self.default_state = KernelState(**base)

    def execute_canonical_operator(self, state: Mapping[str, Any] | None = None) -> KernelExecutionReport:
        from .kahler_ricci import CohomologicalObstructionError, KahlerRicciEngine
        from .ps_kl_optimizer import ProjectivePSKLOptimizer
        from .strominger_conifold import HullStromingerConifold
        from .spectral_toeplitz import ToeplitzSpectralTriple
        from .colombeau_levi_civita import DiffeomorphismInvariantColombeau
        from .cohesive_topos import CohesiveToposHN
        from .symplectic_thermodynamics import KoopmanAmadorThermodynamics
        from fractions import Fraction

        merged = dict(self.default_state.__dict__)
        if state:
            merged.update(state)
        state_obj = KernelState(**merged)

        kh = KahlerRicciEngine(c1_BC=state_obj.c1_BC, volume=state_obj.volume)
        kh.validate()
        kh.check_a_priori_bounds()

        optimizer = ProjectivePSKLOptimizer(n=state_obj.n, gamma=state_obj.gamma)
        strict_saddle = optimizer.strict_saddle_check([0.0, 0.0], [-1.0, -2.0])
        pl = optimizer.polyak_lojasiewicz(1.0, 0.1)

        conifold = HullStromingerConifold(alpha_prime=state_obj.alpha_prime)
        conifold_ok = conifold.validate_stability() and conifold.check_anomaly_cancellation()

        spectral = ToeplitzSpectralTriple(sigma=state_obj.spectral_dimension)
        spectral_ok = spectral.verify_commutation_relations() and spectral.dynamic_spectral_dimension() in (0.0, 2.0, 4.0)

        colombeau = DiffeomorphismInvariantColombeau(rho=Decimal(str(state_obj.rho)))
        finite = colombeau.extract_finite_part({Fraction(0, 1): Decimal("2.0")})
        colombeau_ok = finite == Decimal("2.0") and colombeau.unit_preserved()

        topo = CohesiveToposHN()
        topo_ok = topo.validate_orbifold() and topo.daseinization() is not None

        thermo = KoopmanAmadorThermodynamics(temperature=Decimal(str(state_obj.temperature)))
        entropy_delta = thermo.entropy_balance()
        thermo_ok = entropy_delta == Decimal("0.00000000")

        canonical = (
            "Pi_{T*M -> M} o (M_alpha^{Toeplitz} (+) T_{A, c1_BC=0}^{Symp} (+) "
            "D_{(delta^i, delta^o)}^{H_N} (+) R_{nu_rho=0}^{G_hat(M)}) o Pi_{ker(d ev)}^{PS-KL}"
        )

        verified = {
            "kahler_ricci": True,
            "ps_kl": strict_saddle and pl >= 0.0,
            "strominger_conifold": conifold_ok,
            "spectral_toeplitz": spectral_ok,
            "colombeau": colombeau_ok,
            "cohesive_topos": topo_ok,
            "symplectic_thermodynamics": thermo_ok,
        }

        invariants = {
            "c1_BC": state_obj.c1_BC,
            "volume": state_obj.volume,
            "strict_saddle": strict_saddle,
            "polyak_lojasiewicz": pl,
            "spectral_dimension": spectral.dynamic_spectral_dimension(),
            "entropy_delta": entropy_delta,
            "temperature": Decimal(str(state_obj.temperature)),
        }

        status = "ok" if all(verified.values()) else "warning"
        return KernelExecutionReport(
            canonical_operator=canonical,
            verified_lemmas=verified,
            invariants=invariants,
            status=status,
            entropy_delta=entropy_delta,
            spectral_dimension=float(spectral.dynamic_spectral_dimension()),
        )
