# Documentación Académica del Kernel de Amador

Este directorio centraliza la documentación formal, la arquitectura y la validación empírica del Kernel de Amador.

## Índice

- `arquitectura.md`: descripción de la arquitectura en tres capas.
- `manifiesto-academico.md`: trazabilidad entre el manuscrito y la implementación.
- `benchmarking.md`: protocolo empírico de validación computacional.

## Principio rector

La documentación del kernel se mantiene separada de la ejecución canónica:

- la lógica canónica es determinista y reproducible;
- la documentación describe la semántica formal;
- los benchmarks validan empíricamente la conducta del sistema;
- el operador no se redefine a partir de mediciones experimentales.

## Operador canónico

Omega_Amador_canonico := Pi_{T*M -> M} o ( M_alpha^{Toeplitz} (+) T_{A, c1_BC=0}^{Symp} (+) D_{(delta^i, delta^o)}^{H_N} (+) R_{nu_rho=0}^{G_hat(M)} ) o Pi_{ker(d ev)}^{PS-KL}

## Capa 1: núcleo determinista

- `amador_kernel.core`: ejecución del operador canónico.
- `amador_kernel.kahler_ricci`: cierre cohomológico y flujo Kähler-Ricci.
- `amador_kernel.ps_kl_optimizer`: proyección sobre `ker(d ev)` y validación de silla estricta.
- `amador_kernel.strominger_conifold`: estabilidad conifold y reescalamiento.
- `amador_kernel.spectral_toeplitz`: triple espectral proyectado y dimensión espectral.
- `amador_kernel.colombeau_levi_civita`: extracción de parte finita y valuación nula.
- `amador_kernel.cohesive_topos`: daseinización y orbifold nulo.
- `amador_kernel.symplectic_thermodynamics`: equilibrio simpléctico y entropía cero.

## Capa 2: benchmarks empíricos

Los benchmarks validan comportamiento observable, no definición matemática.
Se ejecutan sobre tamaños crecientes y comparan estabilidad, tiempo y invariantes.

## Capa 3: validación formal

Se verifican:
- cierre cohomológico c1_BC == 0;
- proyección sobre ker(d ev);
- ausencia de blow-up;
- entropía exacta Delta_S_total = 0;
- dimensión espectral en las transiciones esperadas;
- estado final `status == "ok"`.

