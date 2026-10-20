# Manifiesto del Kernel de Amador

Este manifiesto fija la correspondencia entre el manuscrito científico y la implementación determinista del kernel.

## Operador canónico

Omega_Amador_canonico := Pi_{T*M -> M} o ( M_alpha^{Toeplitz} (+) T_{A, c1_BC=0}^{Symp} (+) D_{(delta^i, delta^o)}^{H_N} (+) R_{nu_rho=0}^{G_hat(M)} ) o Pi_{ker(d ev)}^{PS-KL}

## Correspondencia por dominio

1. Dominio 1 — Lema de Clausura de Amador-Kähler
   - módulo: `amador_kernel.kahler_ricci`
   - símbolo: `KahlerRicciEngine`
   - condición canónica: `c1_BC == 0.0`

2. Dominio 2 — Lema de Convexificación PS-KL y Silla Estricta
   - módulo: `amador_kernel.ps_kl_optimizer`
   - símbolo: `ProjectivePSKLOptimizer`
   - condición canónica: proyección sobre `ker(d ev)`

3. Dominio 3 — Lema de Reescalamiento Conifold-Strominger
   - módulo: `amador_kernel.strominger_conifold`
   - símbolo: `HullStromingerConifold`
   - condición canónica: estabilidad de pendiente y cancelación de anomalías

4. Dominio 4 — Lema de Tripla Espectral Comprimida y Morfogénesis
   - módulo: `amador_kernel.spectral_toeplitz`
   - símbolo: `ToeplitzSpectralTriple`
   - condición canónica: trazas sobre subespacio proyectado

5. Dominio 5 — Lema de Inmersión en G_hat(M) y Valuación Nula
   - módulo: `amador_kernel.colombeau_levi_civita`
   - símbolo: `DiffeomorphismInvariantColombeau`
   - condición canónica: extracción de parte finita `c_0`

6. Dominio 6 — Lema del (inf,1)-Topos Cohesivo H_N y Daseinización
   - módulo: `amador_kernel.cohesive_topos`
   - símbolo: `CohesiveToposHN`
   - condición canónica: duality algebra `W = R[X]/(X^k)`

7. Dominio 7 — Lema de Inmersión Simpléctica en T*M y Filtrado de Itô
   - módulo: `amador_kernel.symplectic_thermodynamics`
   - símbolo: `KoopmanAmadorThermodynamics`
   - condición canónica: `div_{T*M} = 0` y `Delta_S_total = 0`

8. Pipeline maestro
   - módulo: `amador_kernel.core`
   - símbolo: `AmadorKernel`
   - condición canónica: ejecución secuencial y determinista de los siete dominios

## Regla de integridad

La implementación determina los invariantes del manuscrito solamente si:
- el estado de entrada cumple la hipótesis canónica,
- cada operador se ejecuta en orden fijo,
- cada validación se resuelve con tolerancia explícita,
- los benchmarks son solo capa empírica complementaria.

## Uso

```python
from amador_kernel import AmadorKernel, get_manifest

report = AmadorKernel().execute_canonical_operator({"c1_BC": 0.0, "volume": 1.0, "n": 12})
print(report.status)
print(get_manifest())
```
