from __future__ import annotations

from decimal import Decimal

from .core import AmadorKernel


def main() -> None:
    kernel = AmadorKernel()
    report = kernel.execute_canonical_operator(
        {
            "c1_BC": 0.0,
            "volume": 1.0,
            "n": 12,
            "gamma": 0.1,
            "rho": Decimal("1e-3"),
            "temperature": Decimal("1.0"),
            "alpha_prime": 1e-3,
            "spectral_dimension": 2.0,
        }
    )

    print("=== Kernel de Amador: Auditor Canónico ===")
    print(f"Operador canónico: {report.canonical_operator}")
    print(f"Estado: {report.status}")
    print(f"Delta S total: {report.entropy_delta} nats")
    print(f"Dimensión espectral: {report.spectral_dimension}")
    print("Lemas verificados:")
    for name, ok in report.verified_lemmas.items():
        print(f"  - {name}: {'OK' if ok else 'WARN'}")


if __name__ == "__main__":
    main()
