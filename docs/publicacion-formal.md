# Publicación Formal del Kernel de Amador

## Abstract

El Kernel de Amador constituye un núcleo científico computacional determinista para la ejecución del operador canónico Omega_Amador_canonico. La arquitectura se fundamenta en la separación estricta entre:

- la definición matemática canónica,
- la validación formal de hipótesis,
- la comprobación empírica por benchmarks.

La implementación propone un pipeline reproducible que preserva invariante de cierre cohomológico, geometría simpléctica, dimensión espectral y entropía total nula, con una estructura modular compatible con Python puro y librería estándar.

## Keywords

Kernel de Amador; operador canónico; determinismo científico; Kähler-Ricci; PS-KL; conifold; spectral triple; Colombeau; topos cohesivo; termodinámica simpléctica.

## 1. Introducción

El proyecto presenta un núcleo científico de carácter determinista con una semántica formal asociada al manuscrito del investigador principal. La finalidad de la librería es ejecutar un operador multimodal canónico sobre estados compatibles con la hipótesis del documento, sin introducir ruido, aleatoriedad ni dependencias externas.

La publicación formal enfatiza que el sistema no es un modelo heurístico abierto a la improvisación, sino un conjunto de módulos teóricamente vinculados a condiciones de cierre, invariantes y validación analítica.

## 2. Objetivos

- preservar la definición formal del operador canónico;
- garantizar la reproducibilidad del cálculo;
- mantener una arquitectura modular en siete dominios;
- separar definición teórica de validación empírica;
- ofrecer una auditoría formal y una infraestructura de benchmarks reproducibles.

## 3. Operador Canónico

Omega_Amador_canonico := Pi_{T*M -> M} o ( M_alpha^{Toeplitz} (+) T_{A, c1_BC=0}^{Symp} (+) D_{(delta^i, delta^o)}^{H_N} (+) R_{nu_rho=0}^{G_hat(M)} ) o Pi_{ker(d ev)}^{PS-KL}

Este operador se entiende como una composición secuencial de transformaciones deterministas aplicadas sobre un estado compatible con las hipótesis del manuscrito.

## 4. Arquitectura del Sistema

La arquitectura sigue una separación en tres capas:

1. Capa canónica determinista
   - `KernelState`
   - `AmadorKernel`
   - `KernelExecutionReport`

2. Capa empírica de benchmarks
   - `run_canonical_benchmark`
   - `BenchmarkReport`
   - `BenchmarkSample`

3. Capa de trazabilidad formal
   - `MANIFESTO.md`
   - `src/amador_kernel/manifiesto.py`
   - auditoría terminal con el CLI.

## 5. Módulos principales

### 5.1 Dominio 1 — Kähler-Ricci

La clase `KahlerRicciEngine` valida la anulación de la primera clase de Chern en cohomología de Bott-Chern. La evolución del potencial se realiza bajo hipótesis de cierre canónico y validación explícita de la condición `c1_BC == 0.0`.

### 5.2 Dominio 2 — PS-KL

`ProjectivePSKLOptimizer` implementa la proyección sobre el espacio nulo de `d ev`, con comprobación de silla estricta y control de descomposición de energía.

### 5.3 Dominio 3 — Conifold-Strominger

`HullStromingerConifold` modela la estabilidad conifold y el reescalamiento asintótico bajo la ley `alpha_prime(eps) = o(eps^2)`.

### 5.4 Dominio 4 — Spectral Toeplitz

`ToeplitzSpectralTriple` ofrece el control de trazas proyectadas y la dimensión espectral dinámica.

### 5.5 Dominio 5 — Colombeau y valuación nula

`DiffeomorphismInvariantColombeau` extrae la parte finita del cuerpo no arquimediano graduado, preservando la unidad del anillo y aislando la sombra distribucional.

### 5.6 Dominio 6 — Topos cohesivo H_N

`CohesiveToposHN` representa la estructura del orbifold nulo y la daseinización de los observables.

### 5.7 Dominio 7 — termodinámica simpléctica

`KoopmanAmadorThermodynamics` garantiza la cancelación exacta de la divergencia total y la entropía cero.

## 6. Validación formal

La validación formal se sustenta en estas premisas:

- la hipótesis canónica debe cumplirse antes de la ejecución;
- cada módulo exige condiciones de cierre explícitas;
- los errores de hipótesis se elevan con excepciones científicas relevantes;
- la salida del pipeline es un `KernelExecutionReport` con invariantes certificados.

## 7. Benchmarks y validación empírica

La capa empírica se ejecuta de forma reproducible sobre tamaños de entrada crecientes. No redefine la lógica del sistema; únicamente documenta y verifica el comportamiento observable bajo la misma semántica canónica.

Los indicadores medidos incluyen:

- estabilidad entre ejecuciones;
- tiempo de ejecución por tamaño;
- estado final `ok`;
- entropía total igual a cero;
- dimensión espectral estable dentro de las transiciones esperadas.

## 8. Reproducibilidad

La librería se mantiene compatible con Python puro, sin dependencias externas, y puede ejecutarse en entornos portátiles como Pydroid 3 o en instalaciones estándar del entorno científico.

## 9. Conclusión

El Kernel de Amador ofrece una implementación computacional formal y reproducible del operador canónico del manuscrito, con una estructura modular, una validación explícita por hipótesis y una capa empírica complementaria. Esta separación entre teoría, ejecución y observación es el eje que permite mantener la integridad del sistema científico y la trazabilidad documental del proyecto.

## 10. Apéndice

La publicación formal se articula con los siguientes materiales del repositorio:

- `MANIFESTO.md`
- `docs/README.md`
- `docs/arquitectura.md`
- `docs/manifiesto-academico.md`
- `docs/benchmarking.md`
- `src/amador_kernel/cli_auditor.py`

