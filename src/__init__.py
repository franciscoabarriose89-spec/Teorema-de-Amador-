# Kernel de Amador

Este repositorio implementa una arquitectura de tres capas para el Kernel de Amador:

1. Capa canónica determinista (Layer 1)
   - define el operador Omega_Amador_canonico
   - usa entradas deterministas y validaciones explícitas
   - devuelve reportes reproducibles

2. Capa de benchmarks empíricos (Layer 2)
   - ejecuta la misma lógica con tamaños crecientes
   - mide tiempos y estabilidad sin alterar la definición del operador
   - valida comportamiento asintótico complementario

3. Capa de validación formal (Layer 3)
   - pruebas unitarias y auditorías de integración
   - comprueba invariantes, cierre cohomológico y entropía exacta

El manifiesto formal del documento está disponible en `MANIFESTO.md` y en `src/amador_kernel/manifiesto.py`.

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Uso canónico

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

## Auditor

```bash
python -m src.amador_kernel.cli_auditor --benchmark
```

## Pruebas

```bash
python -m unittest discover -s tests -v
```

La lógica canónica permanece determinista por diseño: sin aleatoriedad, sin ruido y sin dependencias externas.
Los benchmarks solo observan y documentan el comportamiento empírico de ese núcleo.
