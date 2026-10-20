from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from typing import Any, Dict, Iterable, List

from .kahler_ricci import CohomologicalObstructionError, KahlerRicciEngine
from .ps_kl_optimizer import ProjectivePSKLOptimizer
from .strominger_conifold import HullStromingerConifold
from .spectral_toeplitz import ToeplitzSpectralTriple
from .colombeau_levi_civita import DiffeomorphismInvariantColombeau
from .cohesive_topos import CohesiveToposHN
from .symplectic_thermodynamics import KoopmanAmadorThermodynamics


@dataclass(frozen=True)
class KernelState:
    """Minimal normalized state passed to the canonical operator."""

    c1_BC: float = 0.0
    volume: float = 1.0
    n: int = 12
    gamma: float = 0.1
    rho: Decimal | str = Decimal("1e-3")
    temperature: Decimal | str = Decimal("1.0")
    alpha_prime: float = 1e-3
    spectral_dimension: float = 2.0
    phi: float = 0.0
    t: float = 0.0
    details: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        object.__setattr__(self, "c1_BC", float(self.c1_BC))
        object.__setattr__(self, "volume", float(self.volume))
        object.__setattr__(self, "n", int(self.n))
        object.__setattr__(self, "gamma", float(self.gamma))
        object.__setattr__(self, "alpha_prime", float(self.alpha_prime))
        object.__setattr__(self, "spectral_dimension", float(self.spectral_dimension))
        object.__setattr__(self, "phi", float(self.phi))
        object.__setattr__(self, "t", float(self.t))
        object.__setattr__(self, "rho", Decimal(str(self.rho)))
        object.__setattr__(self, "temperature", Decimal(str(self.temperature)))


@dataclass(frozen=True)
class KernelExecutionReport:
    """Immutable execution report for the canonical operator."""

    canonical_operator: str
    verified_lemmas: Dict[str, bool]
    status: str
    entropy_delta: Decimal
    spectral_dimension: float
    details: Dict[str, Any]


class AmadorKernel:
    """Master execution pipeline for the canonical Amador operator."""

    def __init__(self) -> None:
        self.name = "Omega_Amador_canonico"

    def execute_canonical_operator(self, state: KernelState | Dict[str, Any]) -> KernelExecutionReport:
        """Execute a deterministic validation pipeline.

        The method accepts either a prebuilt KernelState or a mapping containing the
        required fields. It validates all relevant canonical conditions and returns a
        final immutable report.
        """
        if isinstance(state, KernelState):
            normalized = state
        else:
            normalized = KernelState(**state)

        verified: Dict[str, bool] = {}
        details: Dict[str, Any] = {}

        try:
            k = KahlerRicciEngine(
                c1_BC=normalized.c1_BC,
                volume=normalized.volume,
                f0=0.0,
            )
            k.validate()
            k.check_a_priori_bounds()
            phi = k.evolve_potential(normalized.phi, normalized.t)
            verified["kahlers_ricci_closure"] = True
            details["phi_evolved"] = phi
        except (CohomologicalObstructionError, ValueError) as exc:
            verified["kahlers_ricci_closure"] = False
            details["kahler_error"] = str(exc)
            return KernelExecutionReport(
                canonical_operator=self.name,
                verified_lemmas=verified,
                status="INVALID",
                entropy_delta=Decimal("0.00000000"),
                spectral_dimension=float(normalized.spectral_dimension),
                details=details,
            )

        try:
            opt = ProjectivePSKLOptimizer(n=normalized.n, gamma=normalized.gamma)
            proj = opt.project_to_ker_d_ev(list(range(1, min(4, normalized.n + 1))))
            verified["ps_kl_projection"] = bool(proj)
            details["projection"] = proj
        except Exception as exc:  # pragma: no cover - defensive branch
            verified["ps_kl_projection"] = False
            details["ps_kl_error"] = str(exc)

        try:
            conifold = HullStromingerConifold(alpha_prime=normalized.alpha_prime)
            verified["conifold_stability"] = conifold.validate_stability()
            details["conifold_recaling"] = conifold.dynamic_recaling(0.5)
            verified["anomaly_cancellation"] = conifold.check_anomaly_cancellation()
        except Exception as exc:  # pragma: no cover - defensive branch
            verified["conifold_stability"] = False
            verified["anomaly_cancellation"] = False
            details["conifold_error"] = str(exc)

        try:
            triple = ToeplitzSpectralTriple(sigma=normalized.spectral_dimension)
            verified["spectral_triple"] = triple.verify_commutation_relations()
            details["spectral_dimension"] = triple.dynamic_spectral_dimension(normalized.spectral_dimension)
        except Exception as exc:  # pragma: no cover - defensive branch
            verified["spectral_triple"] = False
            details["spectral_error"] = str(exc)

        try:
            colombeau = DiffeomorphismInvariantColombeau(rho=normalized.rho)
            finite = colombeau.extract_finite_part({0: Decimal("2.0")})
            verified["colombeau_regularization"] = finite == Decimal("2.0")
            details["colombeau_finite_part"] = str(finite)
            verified["unit_preserved"] = colombeau.unit_preserved()
        except Exception as exc:  # pragma: no cover - defensive branch
            verified["colombeau_regularization"] = False
            verified["unit_preserved"] = False
            details["colombeau_error"] = str(exc)

        try:
            cohesive = CohesiveToposHN()
            verified["cohesive_topos"] = cohesive.validate_orbifold()
            details["daseinization"] = cohesive.daseinization()
        except Exception as exc:  # pragma: no cover - defensive branch
            verified["cohesive_topos"] = False
            details["cohesive_error"] = str(exc)

        try:
            thermo = KoopmanAmadorThermodynamics(temperature=normalized.temperature)
            entropy = thermo.entropy_balance()
            verified["entropy_balance"] = entropy == Decimal("0.00000000")
            details["entropy_balance"] = str(entropy)
        except Exception as exc:  # pragma: no cover - defensive branch
            verified["entropy_balance"] = False
            details["thermo_error"] = str(exc)

        status = "VALID" if all(verified.values()) else "WARNING"
        spectral_dimension = float(details.get("spectral_dimension", normalized.spectral_dimension))
        entropy_delta = Decimal(str(details.get("entropy_balance", Decimal("0.00000000"))))

        return KernelExecutionReport(
            canonical_operator=self.name,
            verified_lemmas=verified,
            status=status,
            entropy_delta=entropy_delta,
            spectral_dimension=spectral_dimension,
            details=details,
        )

    def __call__(self, state: KernelState | Dict[str, Any]) -> KernelExecutionReport:
        return self.execute_canonical_operator(state)
