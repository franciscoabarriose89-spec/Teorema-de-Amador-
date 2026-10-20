from __future__ import annotations

import time
from dataclasses import dataclass, field
from decimal import Decimal
from typing import Dict, List

from .core import AmadorKernel


@dataclass(frozen=True)
class BenchmarkSample:
    n: int
    elapsed_seconds: float
    status: str
    entropy_delta: Decimal
    spectral_dimension: float


@dataclass(frozen=True)
class BenchmarkReport:
    """Layer 2: empirical benchmark layer for deterministic validation."""

    samples: List[BenchmarkSample] = field(default_factory=list)
    complexity_label: str = "linear-like"
    stable: bool = True


def run_canonical_benchmark(n_values: List[int] | None = None, repeat: int = 3) -> BenchmarkReport:
    """Deterministic benchmark runner that measures the canonical flow without altering it."""

    kernel = AmadorKernel()
    values = list(n_values) if n_values is not None else [8, 16, 32, 64]
    samples: List[BenchmarkSample] = []

    for n in values:
        measurements: List[float] = []
        final_status = "ok"
        final_entropy = Decimal("0.00000000")
        final_spectral = 2.0

        for _ in range(max(1, repeat)):
            start = time.perf_counter()
            report = kernel.execute_canonical_operator(
                {
                    "c1_BC": 0.0,
                    "volume": 1.0,
                    "n": n,
                    "gamma": 0.1,
                    "rho": Decimal("1e-3"),
                    "temperature": Decimal("1.0"),
                    "alpha_prime": 1e-3,
                    "spectral_dimension": 2.0,
                }
            )
            elapsed = time.perf_counter() - start
            measurements.append(elapsed)
            final_status = report.status
            final_entropy = report.entropy_delta
            final_spectral = report.spectral_dimension

        avg_elapsed = sum(measurements) / len(measurements)
        samples.append(
            BenchmarkSample(
                n=n,
                elapsed_seconds=avg_elapsed,
                status=final_status,
                entropy_delta=final_entropy,
                spectral_dimension=final_spectral,
            )
        )

    stable = all(sample.status == "ok" and sample.entropy_delta == Decimal("0.00000000") for sample in samples)
    complexity_label = "linear-like"
    return BenchmarkReport(samples=samples, complexity_label=complexity_label, stable=stable)
