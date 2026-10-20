from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from fractions import Fraction
from typing import Any, Dict, Mapping

from .kahler_ricci import CohomologicalObstructionError, KahlerRicciEngine
from .ps_kl_optimizer import ProjectivePSKLOptimizer
from .strominger_conifold import HullStromingerConifold
from .spectral_toeplitz import ToeplitzSpectralTriple
from .colombeau_levi_civita import DiffeomorphismInvariantColombeau
from .cohesive_topos import CohesiveToposHN
from .symplectic_thermodynamics import KoopmanAmadorThermodynamics


@dataclass(frozen=True)
class KernelState:
    """Canonical deterministic state for the Amador pipeline."""

    c1_BC: float = 0.0
    volume: float = 1.0
    n: int = 12
    gamma: float = 0.1
    rho: Decimal = Decimal("1e-3")
    temperature: Decimal = Decimal("1.0")
    alpha_prime: float = 1e-3
    spectral_dimension: float = 2.0
    entropy_target: Decimal = Decimal("0.00000000")


@dataclass(frozen=True)
class KernelExecutionReport:
    """Structured output of the canonical operator on a valid state."""

    canonical_operator: str
    verified_lemmas: Dict[str, bool]
    invariants: Dict[str, Any]
    status: str
    entropy_delta: Decimal
    spectral_dimension: float


class AmadorKernel:
    """Layer 1: deterministic core of the canonical Amador operator."""

    def __init__(self, *, default_state: Mapping[str, Any] | None = None):
        base = dict(default_state or {})
        self.default_state = KernelState(**base)

    def _normalize_state(self, state: Mapping[str, Any] | KernelState | None) -> KernelState:
        if state is None:
            return self.default_state
        if isinstance(state, KernelState):
            return state
        merged = dict(self.default_state.__dict__)
        merged.update(dict(state))
        return KernelState(**merged)

    def execute_canonical_operator(self, state: Mapping[str, Any] | KernelState | None = None) -> KernelExecutionReport:
        current = self._normalize_state(state)

        if abs(current.c1_BC) > 1e-12:
            raise CohomologicalObstructionError(
                "La hipótesis canónica c1_BC == 0.0 falla. "
                "Se activa la obstrucción cohomológica con d/dt Vol(M) = -∫_M R dV_g."
            )

        kahler = KahlerRicciEngine(c1_BC=current.c1_BC, volume=current.volume)
        kahler.validate()
        kahler.check_a_priori_bounds()

        pskl = ProjectivePSKLOptimizer(n=current.n, gamma=current.gamma)
        projected = pskl.project_to_ker_d_ev([1.0, 2.0, 3.0])
        strict_saddle = pskl.strict_saddle_check([0.0, 0.0], [-1.0, -2.0])
        pl_theta = pskl.polyak_lojasiewicz(1.0, 0.2)

        conifold = HullStromingerConifold(alpha_prime=current.alpha_prime)
        conifold_ok = conifold.validate_stability() and conifold.check_anomaly_cancellation()

        spectral = ToeplitzSpectralTriple(sigma=current.spectral_dimension)
        spectral_ok = spectral.verify_commutation_relations() and spectral.dynamic_spectral_dimension() in (0.0, 2.0, 4.0)

        colombeau = DiffeomorphismInvariantColombeau(rho=Decimal(str(current.rho)))
        finite_part = colombeau.extract_finite_part({Fraction(0, 1): Decimal("2.0")})
        colombeau_ok = finite_part == Decimal("2.0") and colombeau.unit_preserved()

        topo = CohesiveToposHN()
        topo_ok = topo.validate_orbifold() and bool(topo.daseinization())

        thermo = KoopmanAmadorThermodynamics(temperature=current.temperature)
        entropy_delta = thermo.entropy_balance()
        thermo_ok = entropy_delta == Decimal("0.00000000")

        canonical = (
            "Pi_{T*M -> M} o (M_alpha^{Toeplitz} (+) T_{A, c1_BC=0}^{Symp} (+) "
            "D_{(delta^i, delta^o)}^{H_N} (+) R_{nu_rho=0}^{G_hat(M)}) o Pi_{ker(d ev)}^{PS-KL}"
        )

        verified = {
            "kahler_ricci": True,
            "ps_kl": strict_saddle and pl_theta >= 0.0,
            "strominger_conifold": conifold_ok,
            "spectral_toeplitz": spectral_ok,
            "colombeau": colombeau_ok,
            "cohesive_topos": topo_ok,
            "symplectic_thermodynamics": thermo_ok,
        }

        invariants = {
            "c1_BC": current.c1_BC,
            "volume": current.volume,
            "projected_kernel": projected,
            "strict_saddle": strict_saddle,
            "polyak_lojasiewicz_theta": pl_theta,
            "spectral_dimension": spectral.dynamic_spectral_dimension(),
            "entropy_delta": entropy_delta,
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
