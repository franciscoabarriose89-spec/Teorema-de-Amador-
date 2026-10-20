from __future__ import annotations

from decimal import Decimal
from typing import Any, Dict

from .core import AmadorKernel


def canonical_report() -> Dict[str, Any]:
    kernel = AmadorKernel()
    report = kernel.execute_canonical_operator({
        "c1_BC": 0.0,
        "volume": 1.0,
        "n": 12,
        "gamma": 0.1,
        "rho": Decimal("1e-3"),
        "temperature": Decimal("1.0"),
        "alpha_prime": 1e-3,
        "spectral_dimension": 2.0,
    })
    return {
        "canonical_operator": report.canonical_operator,
        "verified_lemmas": report.verified_lemmas,
        "status": report.status,
        "entropy_delta": str(report.entropy_delta),
        "spectral_dimension": report.spectral_dimension,
    }


def main() -> None:
    data = canonical_report()
    print("=== Kernel de Amador: Auditor Canónico ===")
    print(f"Operador canónico: {data['canonical_operator']}")
    print(f"Estado: {data['status']}")
    print(f"Delta S total: {data['entropy_delta']} nats")
    print(f"Dimensión espectral: {data['spectral_dimension']}")
    print("Lemas verificados:")
    for name, ok in data["verified_lemmas"].items():
        print(f"  - {name}: {'OK' if ok else 'WARN'}")


if __name__ == "__main__":
    main()
