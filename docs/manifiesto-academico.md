# Manifiesto Académico del Kernel de Amador

## Operador canónico

Omega_Amador_canonico := Pi_{T*M -> M} o ( M_alpha^{Toeplitz} (+) T_{A, c1_BC=0}^{Symp} (+) D_{(delta^i, delta^o)}^{H_N} (+) R_{nu_rho=0}^{G_hat(M)} ) o Pi_{ker(d ev)}^{PS-KL}

## Dominio 1

- Lema: Lema de Clausura de Amador-Kähler
- Módulo: `amador_kernel.kahler_ricci`
- Símbolo: `KahlerRicciEngine`
- Condición canónica: `c1_BC == 0.0`
- Invariante: ausencia de blow-up y convergencia al atractor de Calabi-Yau

## Dominio 2

- Lema: Lema de Convexificación PS-KL y Silla Estricta
- Módulo: `amador_kernel.ps_kl_optimizer`
- Símbolo: `ProjectivePSKLOptimizer`
- Condición canónica: proyección sobre `ker(d ev)`
- Invariante: autovalor mínimo negativo y desigualdad PL con theta = 0.5

## Dominio 3

- Lema: Reescalamiento Conifold-Strominger
- Módulo: `amador_kernel.strominger_conifold`
- Símbolo: `HullStromingerConifold`
- Condición canónica: estabilidad de pendiente y cancelación de anomalías
- Invariante: `alpha_prime(eps) = o(eps^2)` y `c2(E) == c2(X)`

## Dominio 4

- Lema: Tripla Espectral Comprimida y Morfogénesis
- Módulo: `amador_kernel.spectral_toeplitz`
- Símbolo: `ToeplitzSpectralTriple`
- Condición canónica: trazas restringidas al subespacio proyectado
- Invariante: `D_S = 0.0 -> 2.0 -> 4.0`

## Dominio 5

- Lema: Inmersión en `G_hat(M)` y valuación nula
- Módulo: `amador_kernel.colombeau_levi_civita`
- Símbolo: `DiffeomorphismInvariantColombeau`
- Condición canónica: extracción de la parte finita `c_0`
- Invariante: `1 != 0` y aislamiento de la sombra distribucional de Dirac

## Dominio 6

- Lema: `(inf,1)`-Topos Cohesivo `H_N` y daseinización
- Módulo: `amador_kernel.cohesive_topos`
- Símbolo: `CohesiveToposHN`
- Condición canónica: álgebra de Weil `W = R[X]/(X^k)`
- Invariante: orbifold nulo y daseinización `delta^i, delta^o`

## Dominio 7

- Lema: Inmersión simpléctica en `T*M` y filtrado de Itô
- Módulo: `amador_kernel.symplectic_thermodynamics`
- Símbolo: `KoopmanAmadorThermodynamics`
- Condición canónica: `div_{T*M} = 0` y `Delta_S_total = 0`
- Invariante: cancelación exacta entre contracción base y expansión en la fibra

## Regla de integridad

El kernel solo se considera canónico si:
- cada hipótesis del lema se cumple;
- cada módulo se ejecuta en orden fijo;
- el estado de entrada es compatible con el operador;
- los benchmarks solo validan comportamiento observable y no redefinen la teoría.

