from __future__ import annotations

import argparse
from decimal import Decimal
from typing import Any, Dict

from .benchmarking import run_canonical_benchmark
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
    parser = argparse.ArgumentParser(description="Auditor canónico del Kernel de Amador")
    parser.add_argument("--benchmark", action="store_true", help="ejecuta la capa empírica de benchmarks")
    args = parser.parse_args()

    data = canonical_report()
    print("=== Kernel de Amador: Auditor Canónico ===")
    print(f"Operador canónico: {data['canonical_operator']}")
    print(f"Estado: {data['status']}")
    print(f"Delta S total: {data['entropy_delta']} nats")
    print(f"Dimensión espectral: {data['spectral_dimension']}")
    print("Lemas verificados:")
    for name, ok in data["verified_lemmas"].items():
        print(f"  - {name}: {'OK' if ok else 'WARN'}")

    if args.benchmark:
        print("\n=== Benchmarks deterministas ===")
        report = run_canonical_benchmark(n_values=[8, 16, 32, 64], repeat=2)
        for sample in report.samples:
            print(f"n={sample.n}: {sample.elapsed_seconds:.6f}s | status={sample.status} | entropy={sample.entropy_delta} | dim={sample.spectral_dimension}")
        print(f"Estabilidad: {'OK' if report.stable else 'WARN'}")


if __name__ == "__main__":
    main()
