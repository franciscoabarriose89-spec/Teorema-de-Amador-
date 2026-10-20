# Arquitectura del Kernel de Amador

## Visión general

La librería `amador_kernel` implementa un pipeline científico con tres capas discretas:

1. Capa canónica determinista
2. Capa de benchmarks empíricos
3. Capa de validación formal y trazabilidad documental

## Capa 1: determinista

Se compone de un estado formal y de un conjunto de módulos que operan de manera reproducible.

- `KernelState` contiene la entrada canónica.
- `AmadorKernel.execute_canonical_operator` ejecuta el conjunto de validaciones y transformaciones.
- Cada módulo exige condiciones de cierre explícitas.
- Si un lema no cumple su hipótesis, la ejecución falla determinísticamente con una excepción específica.

## Capa 2: benchmarks

La capa de benchmarks debe:

- tomar entradas canónicas;
- medir tiempo y estabilidad;
- reportar resultados sin modificar la definición del operador;
- servir como evidencia computacional complementaria.

La validación empírica no reemplaza la teoría. Un benchmark solo confirma comportamiento observable.

## Capa 3: trazabilidad documental

El manifiesto formal y la documentación académica conectan cada dominio del manuscrito con:

- el módulo asociado;
- el símbolo matemático o clase correspondiente;
- la condición de cierre;
- el invariante observado;
- el procedimiento de validación formal.

## Regla de integridad

La librería solo admite ejecuciones canónicas si se cumplen todas las condiciones del manuscrito. El benchmark no es una licencia para redefinir las hipótesis del sistema.

## Flujo de ejecución

1. Normalizar el estado de entrada.
2. Validar `c1_BC == 0.0` dentro de tolerancia.
3. Ejecutar Kähler-Ricci.
4. Ejecutar PS-KL.
5. Ejecutar Conifold-Strominger.
6. Ejecutar triple espectral.
7. Ejecutar Colombeau.
8. Ejecutar topos cohesivo.
9. Ejecutar termodinámica simpléctica.
10. Devolver `KernelExecutionReport` con invariantes y estado final.

