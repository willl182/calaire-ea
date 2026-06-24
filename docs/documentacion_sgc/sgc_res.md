# Resumen actualizado del SGC PEA

**Fecha de actualizacion:** 2026-06-23  
**Fuentes:** `goals_mapeo_sgc.md`, `rev1.md`, `mapa_navegacion_sgc_pea.html`, `calaire-app_registros-sgc.html` y `sgc_revision_registros_consolidado.html`.

---

## Estado ejecutivo

El mapa documental del SGC PEA quedo reorganizado bajo una lectura mas estable: se distinguen documentos maestros, registros operativos por ronda, soportes de aplicativos y archivos retirados. La revision mas reciente muestra que la cobertura editable esta casi completa para documentos generales, procedimientos e instructivos; las brechas principales estan en formatos maestros y en un procedimiento transversal.

La decision tecnica mas importante es que no debe confundirse la existencia de copias operativas de ronda con la existencia de un maestro documental controlado. Varios codigos tienen archivos `.docx` en carpetas de prueba piloto, pero aun no cuentan con version maestra en `01_bloque_general/04_formatos_maestros/`.

Tras la ultima definicion de fuentes, los faltantes principales fueron materializados como maestros base: se copiaron las fuentes operativas indicadas, se crearon plantillas para los registros dependientes de aplicativos y se respeto el criterio documental correcto: XLSX maestro con encabezado para registros tabulares, CSV como fuente/exportacion operativa y DOCX solo para procedimiento e informe.

Correccion posterior: los procedimientos por gas `P-PSEA-10` a `P-PSEA-13` no se reconstruyen ni se transcriben. Quedan controlados como copias DOCX de los originales suministrados con prefijo `0P-PSEA-*`, renombradas a la numeracion activa.

---

## Cobertura documental

| Familia | Estado | Resultado |
|---|---|---|
| `DG-PSEA` | Completo | `DG-PSEA-01`, `DG-PSEA-02` y `DG-PSEA-03` tienen version `.docx` activa. |
| `P-PSEA` | Completo como base documental | `P-PSEA-05` tiene base `.md`/`.docx`; `P-PSEA-10` a `P-PSEA-13` quedan como DOCX originales activos renombrados desde las fuentes `0P-PSEA-*`. |
| `I-PSEA` | Completo | `I-PSEA-01` a `I-PSEA-05` tienen version `.docx`. |
| `F-PSEA` | Base documental implementada | `F-PSEA-04`, `F-PSEA-07`, `F-PSEA-08`, `F-PSEA-09`, `F-PSEA-10`, `F-PSEA-11`, `F-PSEA-12` y `F-PSEA-13` quedaron materializados: XLSX maestro para datos tabulares, CSV operativo cuando aplica y DOCX para informe. |

---

## Correcciones de criterio incorporadas

- `F-PSEA-13` es el **Informe final de resultados** generado desde `pt_app`.
- `F-PSEA-14` no es informe; corresponde al **registro de caso de queja o no conformidad**, cuando aplique.
- `F-PSEA-11` no es plan operativo; corresponde a **homogeneidad y estabilidad del item**.
- `F-PSEA-05` y `F-PSEA-05A` no son equivalentes: `F-PSEA-05` es el plan de ronda y `F-PSEA-05A` es la hoja de registro del participante.
- `F-PSEA-01` y `F-PSEA-02` no deben forzarse a `.docx`, porque su control vigente corresponde a hojas de calculo.
- `calaire-app` administra ronda, participantes, datos y trazabilidad; `pt_app` gobierna preprocesamiento, analisis estadistico, homogeneidad/estabilidad, dataset oficial e informe.
- Los procedimientos por gas `P-PSEA-10` a `P-PSEA-13` deben conservarse como `.docx` originales renombrados; no deben reemplazarse por versiones generadas, fichas ni transcripciones `.md`.

---

## Flujo documental vigente

1. **Planificacion de ronda:** `P-PSEA-04`, `DG-PSEA-02`, `I-PSEA-03`, `F-PSEA-01`, `F-PSEA-02`, `F-PSEA-05` y `F-PSEA-06`.
2. **Registro de participante y soporte tecnico:** `I-PSEA-02`, `F-PSEA-05A`, `F-PSEA-04` y `F-PSEA-08`.
3. **Transferencia a pt_app:** `F-PSEA-09` como exportacion oficial desde `calaire-app`.
4. **Procesamiento tecnico:** `DG-PSEA-03`, `I-PSEA-04`, `I-PSEA-05`, `F-PSEA-10`, `F-PSEA-11`, `F-PSEA-11A-D` y `F-PSEA-12`.
5. **Cierre e informe:** `P-PSEA-09` y `F-PSEA-13`.
6. **Casos SGC si aplican:** `F-PSEA-14` a `F-PSEA-17`, asociados a quejas/NC, apelaciones, competencia y proveedores criticos.
7. **Procedimientos por gas:** `P-PSEA-10` a `P-PSEA-13` se mantienen como procedimientos DOCX originales para NO/NO2, CO, O3 y SO2.

---

## Faltantes priorizados implementados

| Prioridad | Codigo / archivo esperado | Motivo |
|---:|---|---|
| 1 | `01_bloque_general/02_procedimientos/P-PSEA-05 Comunicaciones del PEA.docx` | Implementado desde `instrucciones_P-PSEA-05_Comunicaciones_PEA.md`. |
| 2 | `01_bloque_general/04_formatos_maestros/F-PSEA-04 Anexo tecnico de equipos e instrumentos.xlsx` y `.csv` | Implementado copiando `ronda_1_equipos.csv`. |
| 3 | `01_bloque_general/04_formatos_maestros/F-PSEA-07 Preparacion y control del item.xlsx` | Implementado copiando `F-PSEA-02 Cronograma Detallado_v0.xlsx`. |
| 4 | `01_bloque_general/04_formatos_maestros/F-PSEA-08 Datos reportados por participante.xlsx` y `.csv` | Implementado como plantilla XLSX con encabezado; CSV conservado para `calaire-app`. |
| 5 | `01_bloque_general/04_formatos_maestros/F-PSEA-09 Datos de participantes exportados para analisis PT.xlsx` y `.csv` | Implementado como plantilla XLSX con encabezado; CSV conservado para exportacion `calaire-app` hacia `pt_app`. |
| 6 | `01_bloque_general/04_formatos_maestros/F-PSEA-10 Registro de preprocesamiento de datos.xlsx` y `.csv` | Implementado como plantilla XLSX con encabezado; CSV conservado para `pt_app`. |
| 7 | `01_bloque_general/04_formatos_maestros/F-PSEA-11 Homogeneidad datos.xlsx`/`.csv` y `F-PSEA-11 Estabilidad datos.xlsx`/`.csv` | Implementado copiando `ronda_1_homogeneidad.csv` y `ronda_1_estabilidad.csv`; otros anexos quedan por definir. |
| 8 | `01_bloque_general/04_formatos_maestros/F-PSEA-12 Datos oficiales consolidados para evaluacion de aptitud.xlsx` y `.csv` | Implementado copiando `ronda_1_completa.csv`. |
| 9 | `01_bloque_general/04_formatos_maestros/F-PSEA-13 Informe final de resultados.docx` | Implementado copiando `EA-PP2026-R1-1-z-4-2a.docx`. |

---

## Procedimientos originales por gas

| Codigo activo | Fuente original valida | Archivo activo |
|---|---|---|
| `P-PSEA-10` | `0P-PSEA-02 Procedimiento NO-NO2.docx` | `01_bloque_general/02_procedimientos/P-PSEA-10 Procedimiento tecnico NO-NO2.docx` |
| `P-PSEA-11` | `0P-PSEA-03 Procedimiento CO_v2.docx` | `01_bloque_general/02_procedimientos/P-PSEA-11 Procedimiento tecnico CO.docx` |
| `P-PSEA-12` | `0P-PSEA-04 Procedimiento O3_v2.docx` | `01_bloque_general/02_procedimientos/P-PSEA-12 Procedimiento tecnico O3.docx` |
| `P-PSEA-13` | `0P-PSEA-05 Procedimiento SO2_v2.docx` | `01_bloque_general/02_procedimientos/P-PSEA-13 Procedimiento tecnico SO2.docx` |

---

## Fuentes base definidas para los formatos pendientes

| Codigo | Fuente definida | Estado |
|---|---|---|
| `F-PSEA-04` | `ronda_1_equipos.csv` | Implementado como XLSX maestro con CSV operativo. |
| `F-PSEA-07` | `F-PSEA-02 Cronograma Detallado_v0.xlsx` | Implementado como XLSX maestro. |
| `F-PSEA-11` | `ronda_1_homogeneidad.csv`, `ronda_1_estabilidad.csv` | Implementado parcialmente como XLSX maestro con CSV operativo; anexos adicionales por definir. |
| `F-PSEA-12` | `ronda_1_completa.csv` | Implementado como XLSX maestro con CSV operativo. |
| `F-PSEA-13` | `EA-PP2026-R1-1-z-4-2a.docx` | Implementado como DOCX maestro. |

---

## Documentos y vistas actualizadas

| Archivo | Funcion |
|---|---|
| `rev1.md` | Auditoria de cobertura `.docx` y faltantes maestros. |
| `mapa_navegacion_sgc_pea.html` | Mapa interactivo de relaciones documentales con resumen de cobertura DOCX. |
| `calaire-app_registros-sgc.html` | Vista actualizada del flujo de registros SGC en `calaire-app` y `pt_app`. |
| `sgc_revision_registros_consolidado.html` | Pagina unificada de revision documental, flujo digital, matriz y brechas. |

---

## Riesgos de control

- Declarar cerrado un codigo por existir una copia de ronda, aunque falte el maestro controlado.
- Reintroducir la nomenclatura antigua que trataba `F-PSEA-14` como informe.
- Mantener duplicados de `P-PSEA-11`, `P-PSEA-12` y `P-PSEA-13` en `06_procedimientos_gestion/`, cuando su ubicacion natural es `02_procedimientos/`.
- Sustituir los procedimientos originales por gas por versiones generadas o transcripciones `.md`; las fuentes validas son los cuatro `0P-PSEA-*` registrados arriba.
- Crear `F-PSEA-03` sin cerrar antes su decision documental, porque el codigo sigue ambiguo entre fuentes anteriores, fichas y mapa vigente.

---

## Proximo bloque de trabajo recomendado

1. Revisar las plantillas XLSX generadas y completar metadatos de control si se requiere.
2. Revisar duplicados de procedimientos tecnicos por analito en `06_procedimientos_gestion/`.
3. Completar anexos aun no definidos para `F-PSEA-11`.
4. Mantener `calaire-app_registros-sgc.html` como referencia funcional para ajustar catalogos del aplicativo.
