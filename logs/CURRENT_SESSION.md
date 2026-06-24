# Session State: CALAIRE-EA Knowledge Graph

**Last Updated**: 2026-06-23 13:25 -0500

## Session Objective

Corregir la sustitucion indebida de los procedimientos originales por analito del SGC PEA y preservar en memoria las fuentes originales validas.

## Current State

- [x] Eliminados los procedimientos tecnicos generados previamente para `P-PSEA-10` a `P-PSEA-13` en `docs/documentacion_sgc/01_bloque_general/02_procedimientos/`.
- [x] Copiados los procedimientos originales indicados por el usuario desde la raiz de `docs/documentacion_sgc/` hacia la carpeta activa de procedimientos.
- [x] Renombradas las fuentes originales segun la numeracion activa requerida:
  - `0P-PSEA-02 Procedimiento NO-NO2.docx` -> `P-PSEA-10 Procedimiento tecnico NO-NO2.docx`
  - `0P-PSEA-03 Procedimiento CO_v2.docx` -> `P-PSEA-11 Procedimiento tecnico CO.docx`
  - `0P-PSEA-04 Procedimiento O3_v2.docx` -> `P-PSEA-12 Procedimiento tecnico O3.docx`
  - `0P-PSEA-05 Procedimiento SO2_v2.docx` -> `P-PSEA-13 Procedimiento tecnico SO2.docx`
- [x] Verificado con `cmp` que las cuatro copias activas son byte-a-byte identicas a las fuentes originales `0P-PSEA-*`.
- [x] Actualizados los artefactos derivados para reflejar la correccion: `docs/documentacion_sgc/calaire-app_registros-sgc.html`, `docs/documentacion_sgc/mapa_navegacion_sgc_pea.html`, `docs/documentacion_sgc/sgc_revision_registros_consolidado.html`, `docs/documentacion_sgc/sgc_res.md` y las fichas `fichas_resumen/ficha_P-PSEA-10` a `ficha_P-PSEA-13` en `.md` y `.html`.

## Critical Technical Context

- Los archivos `0P-PSEA-02 Procedimiento NO-NO2.docx`, `0P-PSEA-03 Procedimiento CO_v2.docx`, `0P-PSEA-04 Procedimiento O3_v2.docx` y `0P-PSEA-05 Procedimiento SO2_v2.docx` son las fuentes originales validas para los procedimientos por gas.
- No se deben reconstruir estos procedimientos desde los `.md` generados ni desde fichas resumen. La accion correcta es conservar los `.docx` originales y solo renombrarlos/copiarlos a la numeracion activa `P-PSEA-10` a `P-PSEA-13`.
- En la carpeta activa deben quedar los `.docx` originales renombrados; los `.md` generados previamente para `P-PSEA-10` a `P-PSEA-13` fueron eliminados.
- Las fichas resumen y vistas HTML ya deben leerse con el criterio actualizado: estado `Implementado`, fuente original `0P-PSEA-*`, archivo activo `P-PSEA-10` a `P-PSEA-13`, y advertencia de no sustituir por transcripciones generadas.

## Next Steps

1. Revisar si `goals_mapeo_sgc.md` o `rev1.md` necesitan el mismo ajuste narrativo para indicar que los procedimientos activos son copias directas de los originales, no transcripciones.
2. Decidir con el usuario si se conservan o se eliminan de la raiz las fuentes `0P-PSEA-*` tras quedar copiadas en la carpeta activa.
