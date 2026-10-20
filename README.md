# Kernel de Amador

Kernel de Amador es un núcleo computacional científico modular implementado en Python puro, sin dependencias externas, pensado como una arquitectura ejecutable para el operador canónico multimodal.

El proyecto está diseñado para validar invariantes geométricos, topológicos, espectrales y termodinámicos antes de aceptar una ejecución como válida. Su propósito es ofrecer un marco reproducible, portátil y auditable para la investigación científica asociada al operador canónico de Amador.

## Descripción

La librería integra los siguientes dominios:

- Kähler-Ricci flow y cierre cohomológico
- Optimización PS-KL y sillas estrictas
- Reescalamiento conifold-Strominger
- Triplete espectral proyectado
- Regularización de Colombeau y valuación nula
- Topos cohesivo H_N y daseinización
- Termodinámica simpléctica y entropía nula

La ejecución principal se realiza a través de la clase `AmadorKernel`, que devuelve un informe certificado con los invariantes y lemas verificados.

## Estructura del proyecto

```text
amador_kernel/
├── LICENSE
├── README.md
├── pyproject.toml
├── src/
│   └── amador_kernel/
│       ├── __init__.py
│       ├── core.py
│       ├── kahler_ricci.py
│       ├── ps_kl_optimizer.py
│       ├── strominger_conifold.py
│       ├── spectral_toeplitz.py
│       ├── colombeau_levi_civita.py
│       ├── cohesive_topos.py
│       ├── symplectic_thermodynamics.py
│       └── cli_auditor.py
└── tests/
    └── test_amador_kernel.py
```

## Instalación

Desde la raíz del proyecto:

```bash
python -m pip install --upgrade pip
pip install -e .
```

## Uso básico

```python
from src.amador_kernel import AmadorKernel

kernel = AmadorKernel()
report = kernel.execute_canonical_operator({
    "c1_BC": 0.0,
    "volume": 1.0,
    "n": 12,
    "gamma": 0.1,
    "rho": "1e-3",
    "temperature": "1.0",
    "alpha_prime": 1e-3,
    "spectral_dimension": 2.0,
})

print(report.status)
print(report.canonical_operator)
print(report.entropy_delta)
print(report.verified_lemmas)
```

## Auditoría desde consola

```bash
python -m src.amador_kernel.cli_auditor
```

## Verificación de pruebas

```bash
python -m unittest discover -s tests -v
```

## Licencia

Este proyecto está licenciado bajo la licencia MIT. Puedes consultar el archivo `LICENSE` para ver el texto completo.

## Nota

Este proyecto está orientado a investigación científica, validación matemática y software científico reproducible, y se desarrolla con Python puro, evitando dependencias externas para maximizar compatibilidad y portabilidad.
