# Kernel de Amador

El Kernel de Amador es una librería científica escrita en Python puro, sin dependencias externas, diseñada para ejecutar el operador canónico

Omega_Amador_canonico := Pi_{T*M -> M} o ( M_alpha^{Toeplitz} (+) T_{A, c1_BC=0}^{Symp} (+) D_{(delta^i, delta^o)}^{H_N} (+) R_{nu_rho=0}^{G_hat(M)} ) o Pi_{ker(d ev)}^{PS-KL}

con validación simbólico-numérica, colapso determinista de complejidad O(2^n) -> O(n) y evolución geométrica bajo termodinámica tensorial a entropía cero.

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Ejecución del auditor científico

```bash
python -m src.amador_kernel.cli_auditor
```

## Ejecutar pruebas

```bash
python -m unittest discover -s tests -v
```

## Uso básico

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
})

print(report.status)
print(report.canonical_operator)
print(report.verified_lemmas)
```

## Estructura

- `core.py`: orquestación maestra del kernel.
- `kahler_ricci.py`: cierre cohomológico y flujo de Kähler-Ricci.
- `ps_kl_optimizer.py`: optimización proyectiva PS-KL.
- `strominger_conifold.py`: transición conifold y estabilidad.
- `spectral_toeplitz.py`: triple espectral comprimido.
- `colombeau_levi_civita.py`: números generalizados de Colombeau.
- `cohesive_topos.py`: topología cohesiva y daseinización.
- `symplectic_thermodynamics.py`: levantamiento simpléctico y entropía.
- `cli_auditor.py`: auditor científico en consola.

## Invariantes certificados

La librería devuelve un `KernelExecutionReport` con:

- `canonical_operator`: nombre formal del operador canónico.
- `verified_lemmas`: siete lemas verificados.
- `invariants`: medidas relevantes del flujo.
- `status`: estado final del cálculo.
- `entropy_delta`: diferencia de entropía, normalmente `Decimal('0.00000000')`.

