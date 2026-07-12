# Session State: CALAIRE-EA SGC

**Last Updated**: 2026-06-27 11:59 -05

## Session Objective

Cerrar y persistir el trabajo de normalizacion documental del SGC PEA, especialmente la aplicacion de plantillas institucionales y la reorganizacion documental asociada.

## Current State

- [x] Se aplicaron plantillas a documentos controlados del SGC mediante Pandoc con `--reference-doc` para DOCX y plantilla Excel para XLSX.
- [x] Se corrigio el enfoque despues de una objecion del usuario: el intento inicial de reconstruccion automatica fue revertido y luego reaplicado como metodo aceptado.
- [x] Se hicieron dos commits separados y ambos fueron empujados a `origin/main`.
- [x] Commit `f5a937f`: `Aplicar plantillas a documentos controlados SGC`.
- [x] Commit `818ae00`: `Actualizar estructura documental SGC restante`.
- [x] El arbol de trabajo quedo limpio al finalizar.

## Critical Technical Context

- El repositorio Git raiz es `/home/w182/w421/calaire-ea`.
- El grafo/documentacion SGC activo esta en `/home/w182/w421/calaire-ea/docs/documentacion_sgc`.
- La rama activa es `main` y esta sincronizada con `origin/main`.
- Para aplicar plantillas en DOCX se uso Pandoc con `--reference-doc`; para las plantillas `.doc` de procedimientos e instructivos se convirtieron copias temporales a `.docx` mediante LibreOffice.
- Para XLSX se partio de `01_bloque_general/00_plantillas_base/F-PSEA-01 Plantilla Formato_Excel.xlsx` y se incorporo una hoja `Datos` con filas provenientes de los CSV fuente.
- El usuario acepto el metodo Pandoc despues de la aclaracion, pero el aprendizaje importante es no presentar una conversion automatica como equivalente perfecto a copiar/pegar manual en Word.
- Respaldo temporal de la reaplicacion: `/tmp/calaire_sgc_template_backup_reapply_20260624_113010/`.

## Next Steps

1. Si se revisan los DOCX visualmente en Word/LibreOffice, corregir manualmente los casos donde Pandoc no preserve formato fino.
2. Si se modifica el mapa o inventario, mantener consistencia con `mapa_navegacion_sgc_pea.html` y los documentos maestros en `01_bloque_general/`.
3. Si aparece una objecion sobre formato, revisar primero el archivo especifico antes de rehacer masivamente.
