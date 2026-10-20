# Kernel de Amador

Este repositorio ha incorporado la capa de publicación formal académica. La documentación formal y la referencia al manuscrito quedan separadas del código ejecutable para preservar la integridad de la semántica canónica.

## Documentación formal disponible

- `docs/publicacion-formal.md`
- `docs/manifiesto-academico.md`
- `docs/arquitectura.md`
- `docs/benchmarking.md`

## Entrada principal

```bash
python -m src.amador_kernel.cli_auditor --benchmark
```

## Semántica central

El nucleo opera sobre el operador canónico:

Omega_Amador_canonico := Pi_{T*M -> M} o ( M_alpha^{Toeplitz} (+) T_{A, c1_BC=0}^{Symp} (+) D_{(delta^i, delta^o)}^{H_N} (+) R_{nu_rho=0}^{G_hat(M)} ) o Pi_{ker(d ev)}^{PS-KL}

