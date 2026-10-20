# Kernel de Amador

Este repositorio contiene una implementación determinista, modular y portátil del Kernel de Amador en Python puro, sin dependencias externas.

## Objetivo

El kernel ejecuta el operador canónico

Omega_Amador_canonico := Pi_{T*M -> M} o ( M_alpha^{Toeplitz} (+) T_{A, c1_BC=0}^{Symp} (+) D_{(delta^i, delta^o)}^{H_N} (+) R_{nu_rho=0}^{G_hat(M)} ) o Pi_{ker(d ev)}^{PS-KL}

mediante la composición de siete componentes deterministas:

- Kähler-Ricci
- PS-KL optimization
- Conifold-Strominger
- Spectral Toeplitz
- Colombeau-Levi-Civita
- Cohesive Topos H_N
- Symplectic Thermodynamics

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Uso

```python
from amador_kernel import AmadorKernel

kernel = AmadorKernel()
report = kernel.execute_canonical_operator({
    "c1_BC": 0.0,
    "volume": 1.0,
    "n": 12,
    "gamma": 0.1,
    "rho": 1e-3,
    "temperature": 1.0,
    "alpha_prime": 1e-3,
    "spectral_dimension": 2.0,
})

print(report.status)
print(report.canonical_operator)
print(report.verified_lemmas)
```

## Auditor CLI

```bash
python -m src.amador_kernel.cli_auditor
```

## Pruebas

```bash
python -m unittest discover -s tests -v
```

La implementación está diseñada para funcionar sobre Python 3.9+ y puede trasladarse a entornos compactos como Pydroid 3 sin depender de bibliotecas externas.
