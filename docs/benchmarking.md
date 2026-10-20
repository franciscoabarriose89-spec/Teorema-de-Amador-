# Benchmarking del Kernel de Amador

## Propósito

La suite de benchmarks sirve para medir la conducta empírica del kernel sin modificar la definición del operador canónico.

## Regla de no redefinición

Los benchmarks no redefinen la lógica del manuscrito. Solo validan que las hipótesis y los invariantes se mantienen bajo ejecuciones repetidas.

## Protocolo recomendado

- tomar una lista de tamaños `n` crecientes, p.ej. `[8, 16, 32, 64, 128]`;
- ejecutar el mismo estado canónico sobre cada `n`;
- medir tiempos de ejecución;
- verificar `status == "ok"`;
- verificar `entropy_delta == Decimal("0.00000000")`;
- verificar `spectral_dimension` dentro de los valores esperados;
- reportar estabilidad y no variación de invariantes.

## Indicadores esperados

- estabilidad determinista entre ejecuciones repetidas;
- invariantes no degradados bajo tamaños crecientes;
- complejidad observada compatible con régimen lineal o quasi-lineal;
- ausencia de cambio de semántica por ruido o aleatoriedad.

## Ejemplo

```python
from amador_kernel import run_canonical_benchmark

report = run_canonical_benchmark(n_values=[8, 16, 32, 64], repeat=3)
print(report.stable)
print(report.complexity_label)
for sample in report.samples:
    print(sample.n, sample.elapsed_seconds, sample.status)
```

## Conclusión

Los benchmarks forman una capa de validación observacional, no una capa de definición. La teoría sigue siendo la referencia principal y determinista del kernel.

