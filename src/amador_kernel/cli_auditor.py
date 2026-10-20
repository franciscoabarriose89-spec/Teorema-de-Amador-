from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional


@dataclass(frozen=True)
class CanonicalRule:
    domain: str
    lemma: str
    module: str
    symbol: str
    closure_condition: str
    invariant: str
    status: str = "canonical"


class CanonicalManifest:
    """Formal registry linking the manuscript and the deterministic implementation."""

    def __init__(self, entries: Iterable[CanonicalRule]):
        self.entries: List[CanonicalRule] = list(entries)

    def as_dict(self) -> List[Dict[str, str]]:
        return [
            {
                "domain": entry.domain,
                "lemma": entry.lemma,
                "module": entry.module,
                "symbol": entry.symbol,
                "closure_condition": entry.closure_condition,
                "invariant": entry.invariant,
                "status": entry.status,
            }
            for entry in self.entries
        ]

    def lookup(self, symbol: str) -> Optional[CanonicalRule]:
        for entry in self.entries:
            if entry.symbol == symbol:
                return entry
        return None

    def validate(self) -> bool:
        return all(entry.status == "canonical" for entry in self.entries)


CANONICAL_MANIFEST = CanonicalManifest(
    [
        CanonicalRule(
            domain="Dominio 1",
            lemma="Lema de Clausura de Amador-Kähler",
            module="amador_kernel.kahler_ricci",
            symbol="KahlerRicciEngine",
            closure_condition="c1_BC == 0.0 bajo cohomología de Bott-Chern",
            invariant="d/dt Vol(M) = -∫_M R dV_g; ausencia de blow-up; convergencia hacia atractor de Calabi-Yau",
        ),
        CanonicalRule(
            domain="Dominio 2",
            lemma="Lema de Convexificación PS-KL y Silla Estricta",
            module="amador_kernel.ps_kl_optimizer",
            symbol="ProjectivePSKLOptimizer",
            closure_condition="Pi_ker(d ev) sobre truncaciones proyectivas finitas CP^{N(n)}",
            invariant="lambda_min(Hess_g Phi_n(x_c)) <= -gamma(n) < 0; desigualdad PL con theta = 0.5",
        ),
        CanonicalRule(
            domain="Dominio 3",
            lemma="Lema de Reescalamiento Conifold-Strominger",
            module="amador_kernel.strominger_conifold",
            symbol="HullStromingerConifold",
            closure_condition="d(||Omega||_omega * omega^2) = 0; estabilidad de pendiente de Mumford-Takemoto",
            invariant="alpha_prime(eps) = o(eps^2); cancelación de anomalías c2(E) == c2(X)",
        ),
        CanonicalRule(
            domain="Dominio 4",
            lemma="Lema de Tripla Espectral Comprimida y Morfogénesis",
            module="amador_kernel.spectral_toeplitz",
            symbol="ToeplitzSpectralTriple",
            closure_condition="H_alpha = A(H); trazas restringidas al subespacio proyectado; resolvente compacto",
            invariant="D_S = 0.0 -> 2.0 -> 4.0; dimensión espectral dinámica",
        ),
        CanonicalRule(
            domain="Dominio 5",
            lemma="Lema de Inmersión en G_hat(M) y Valuación Nula",
            module="amador_kernel.colombeau_levi_civita",
            symbol="DiffeomorphismInvariantColombeau",
            closure_condition="R_rho = Pi_{nu_rho = 0} y extracción de parte finita c_0",
            invariant="[1] != [0]; parte finita exacta; aislamiento de la sombra distribucional de Dirac",
        ),
        CanonicalRule(
            domain="Dominio 6",
            lemma="Lema del (inf,1)-Topos Cohesivo H_N y Daseinización",
            module="amador_kernel.cohesive_topos",
            symbol="CohesiveToposHN",
            closure_condition="W = R[X]/(X^k) y axioma de Kock-Lawvere",
            invariant="orbifold nulo [(R^{1,d})^D // Gamma]; daseinización (delta^i, delta^o)",
        ),
        CanonicalRule(
            domain="Dominio 7",
            lemma="Lema de Inmersión Simpléctica en T*M y Filtrado de Itô",
            module="amador_kernel.symplectic_thermodynamics",
            symbol="KoopmanAmadorThermodynamics",
            closure_condition="div_{T*M} = 0; Delta_S_total = 0.00000000 nats",
            invariant="cancelación exacta entre contracción base y expansión simpléctica en la fibra",
        ),
        CanonicalRule(
            domain="Pipeline Maestro",
            lemma="Operador Multimodal Canónico",
            module="amador_kernel.core",
            symbol="AmadorKernel",
            closure_condition="ejecución secuencial de los siete dominios sobre un estado compatible",
            invariant="KernelExecutionReport con invariantes topológicos, espectrales y termodinámicos certificados",
        ),
    ]
)


def get_manifest() -> List[Dict[str, str]]:
    return CANONICAL_MANIFEST.as_dict()


def validate_manifest() -> bool:
    return CANONICAL_MANIFEST.validate()


__all__ = ["CanonicalRule", "CanonicalManifest", "CANONICAL_MANIFEST", "get_manifest", "validate_manifest"]
