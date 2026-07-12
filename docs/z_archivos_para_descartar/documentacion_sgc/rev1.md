# Revision 1 - Cobertura documental del mapa SGC PEA

**Fecha:** 2026-06-19  
**Fuente principal:** `goals_mapeo_sgc.md`, `mapa_navegacion_sgc_pea.html` e inventario de archivos activos.  
**Alcance:** documentos generales (`DG-PSEA`), procedimientos (`P-PSEA`), instructivos (`I-PSEA`) y formatos/registros (`F-PSEA`). Se excluye `para_quitar/` por contener archivos retirados, duplicados o fuentes antiguas.

---

## Resumen ejecutivo

La cobertura documental esta completa para documentos generales, procedimientos e instructivos. Los formatos tabulares no se controlan como `.docx`; se controlan como `.xlsx` maestro con encabezado institucional y, cuando aplica, conservan `.csv` como fuente operativa o exportacion del aplicativo.

| Familia | Universo revisado | Con `.docx` activo | Faltante / condicion |
|---|---:|---:|---|
| Documentos generales (`DG`) | 3 | 3 | Sin faltantes. |
| Procedimientos (`P`) | 21 codigos del mapa | 21 | Sin faltantes. `P-PSEA-05` fue creado en `.md` y `.docx`. |
| Instructivos (`I`) | 5 codigos activos/decididos | 5 | Sin faltantes. Incluye `I-PSEA-01` como documento mantenido por decision. |
| Formatos/registros (`F`) | 21 codigos activos/decididos | Implementados en formato natural | `F-PSEA-04`, `F-PSEA-07`, `F-PSEA-08`, `F-PSEA-09`, `F-PSEA-10`, `F-PSEA-11` y `F-PSEA-12` quedan como XLSX maestro con CSV operativo cuando aplica; `F-PSEA-13` queda como DOCX. |

**Conclusion:** la revision queda ajustada al criterio correcto: no todos los formatos deben tener version `.docx`. Los registros derivados de datos se mantienen como XLSX maestro con CSV operativo; los documentos narrativos o informes se mantienen en DOCX.

**Actualizacion posterior:** el usuario definio fuentes base y se materializaron los maestros base. `F-PSEA-04` se copio desde `ronda_1_equipos.csv`; `F-PSEA-07` desde `F-PSEA-02 Cronograma Detallado_v0.xlsx`; `F-PSEA-11` desde `ronda_1_homogeneidad.csv` y `ronda_1_estabilidad.csv`; `F-PSEA-12` desde `ronda_1_completa.csv`; `F-PSEA-13` desde `EA-PP2026-R1-1-z-4-2a.docx`. Tambien se crearon plantillas XLSX con encabezado y CSV operativo para `F-PSEA-08`, `F-PSEA-09` y `F-PSEA-10`.

---

## Criterio usado

- **OK DOCX:** existe version `.docx` activa fuera de `para_quitar/` cuando el documento es narrativo.
- **OK maestro:** existe archivo controlado en la carpeta maestra esperada, en su formato natural.
- **OK XLSX:** el formato maestro vigente es tabular y se controla como `.xlsx`; el `.csv` queda como fuente operativa/exportable cuando aplica.
- **Operacion, no maestro:** existe evidencia operacional, pero falta promoverla a la carpeta maestra.
- **Falta maestro:** no se encontro archivo activo para el codigo en el formato documental que corresponde.

---

## Documentos generales

| Codigo | Documento | Estado DOCX | Archivo encontrado |
|---|---|---|---|
| `DG-PSEA-01` | Protocolo general de participacion EA | OK | `01_bloque_general/01_documentos_marco/DG-PSEA-01 Protocolo Participación EA Gases Contaminantes Criterio.docx` |
| `DG-PSEA-02` | Aplicativo calaire-app | OK | `01_bloque_general/01_documentos_marco/DG-PSEA-02 Aplicativo calaire-app.docx` |
| `DG-PSEA-03` | Aplicativo pt_app | OK | `01_bloque_general/01_documentos_marco/DG-PSEA-03 Aplicativo pt_app.docx` |

**Resultado:** no faltan versiones `.docx` para documentos generales.

---

## Procedimientos

| Codigo | Documento | Estado DOCX | Observacion |
|---|---|---|---|
| `P-PSEA-01` | Protocolo general EA | OK | Tiene version historica y version activa `.docx`. |
| `P-PSEA-02` | Matriz documental basica del PEA | OK | Maestro `.docx` activo. |
| `P-PSEA-03` | Control de registros y evidencias del PEA | OK | Maestro `.docx` activo. |
| `P-PSEA-04` | Planificacion de ronda EA | OK | Maestro `.docx` activo. |
| `P-PSEA-05` | Comunicaciones del PEA | OK | Creado en `01_bloque_general/02_procedimientos/P-PSEA-05 Comunicaciones del PEA.md` y `.docx`. |
| `P-PSEA-06` | Preparacion y control del item de ensayo gaseoso | OK | Maestro `.docx` activo. |
| `P-PSEA-07` | Diseno estadistico | OK | Maestro `.docx` activo. |
| `P-PSEA-08` | Flujo tecnico de datos digitales del PEA | OK | Maestro `.docx` activo. |
| `P-PSEA-09` | Generacion/emision del informe de resultados | OK | Maestro `.docx` activo. |
| `P-PSEA-10` | Procedimiento tecnico NO-NO2 | OK | Maestro `.docx` activo. |
| `P-PSEA-11` | Procedimiento tecnico CO | OK | Hay duplicidad entre `02_procedimientos/` y `06_procedimientos_gestion/`; conservar ubicacion correcta. |
| `P-PSEA-12` | Procedimiento tecnico O3 | OK | Hay duplicidad entre `02_procedimientos/` y `06_procedimientos_gestion/`; conservar ubicacion correcta. |
| `P-PSEA-13` | Procedimiento tecnico SO2 | OK | Hay duplicidad entre `02_procedimientos/` y `06_procedimientos_gestion/`; conservar ubicacion correcta. |
| `P-PSEA-14` | Colusion y falsificacion | OK | Maestro `.docx` activo. |
| `P-PSEA-15` | Trabajo no conforme, no conformidades y acciones correctivas | OK | Maestro `.docx` activo. |
| `P-PSEA-16` | Divulgacion y control de valores sensibles | OK | Maestro `.docx` activo. |
| `P-PSEA-17` | Quejas del PEA | OK | Maestro `.docx` activo. |
| `P-PSEA-18` | Apelaciones del PEA | OK | Maestro `.docx` activo. |
| `P-PSEA-19` | Confidencialidad operativa interna del PEA | OK | Maestro `.docx` activo. |
| `P-PSEA-20` | Competencia y autorizacion operativa del PEA | OK | Maestro `.docx` activo. |
| `P-PSEA-21` | Proveedores criticos del PEA | OK | Maestro `.docx` activo. |

**Resultado:** no faltan versiones `.docx` para procedimientos.

---

## Instructivos

| Codigo | Documento | Estado DOCX | Archivo encontrado |
|---|---|---|---|
| `I-PSEA-01` | Instructivo de embalaje | OK | `01_bloque_general/03_instructivos/I-PSEA-01 Instructivo de Embalaje_v1.docx` |
| `I-PSEA-02` | Instructivo participante calaire-app | OK | `01_bloque_general/03_instructivos/I-PSEA-02 Instructivo participante calaire-app.docx` |
| `I-PSEA-03` | Instructivo administracion rondas calaire-app | OK | `01_bloque_general/03_instructivos/I-PSEA-03 Instructivo administracion rondas calaire-app.docx` |
| `I-PSEA-04` | Instructivo preprocesador pt_app | OK | `01_bloque_general/03_instructivos/I-PSEA-04 Instructivo preprocesador pt_app.docx` |
| `I-PSEA-05` | Instructivo modulo analisis pt_app | OK | `01_bloque_general/03_instructivos/I-PSEA-05 Instructivo modulo analisis pt_app.docx` |

**Resultado:** no faltan versiones `.docx` para instructivos.

---

## Formatos y registros

| Codigo | Documento | Estado DOCX | Observacion |
|---|---|---|---|
| `F-PSEA-01` | Calendario tipo | No aplica DOCX | Maestro vigente en `.xlsx`: `01_bloque_general/04_formatos_maestros/F-PSEA-01 Calendario Tipo_v0.xlsx`. |
| `F-PSEA-02` | Cronograma detallado | No aplica DOCX | Maestro vigente en `.xlsx`: `01_bloque_general/04_formatos_maestros/F-PSEA-02 Cronograma Detallado_v0.xlsx`. |
| `F-PSEA-03` | Registro de participacion / codigo no estable | **Sin maestro activo** | El ajuste previo movio el archivo antiguo a `para_quitar/`; requiere decision si vuelve como codigo activo o queda absorbido. |
| `F-PSEA-04` | Anexo tecnico de equipos e instrumentos | OK XLSX | Maestro XLSX creado con encabezado desde `ronda_1_equipos.csv`; CSV conservado como fuente operativa. |
| `F-PSEA-05` | Plan de ronda EA | OK maestro | `01_bloque_general/04_formatos_maestros/F-PSEA-05 Plan de ronda EA.docx`. |
| `F-PSEA-05A` | Hoja de registro del participante | OK maestro | `01_bloque_general/04_formatos_maestros/F-PSEA-05A Hoja de registro del participante.docx`. |
| `F-PSEA-06` | Ficha digital de ronda EA | OK maestro | `01_bloque_general/04_formatos_maestros/F-PSEA-06 Ficha digital de ronda EA.docx`. |
| `F-PSEA-07` | Preparacion y control del item | OK XLSX | Maestro copiado desde `F-PSEA-02 Cronograma Detallado_v0.xlsx`. |
| `F-PSEA-08` | Datos reportados por participante | OK XLSX | Plantilla XLSX creada con encabezado; CSV operativo disponible para datos capturados por `calaire-app`; instrucciones creadas en `instrucciones_F-PSEA-08_Datos_Reportados_Participante.md`. |
| `F-PSEA-09` | Datos exportados para analisis PT | OK XLSX | Plantilla XLSX creada con encabezado; CSV operativo disponible para la exportacion oficial desde `calaire-app` hacia `pt_app`. |
| `F-PSEA-10` | Registro de preprocesamiento de datos | OK XLSX | Plantilla XLSX creada con encabezado; CSV operativo disponible para trazabilidad del preprocesamiento; instrucciones creadas en `instrucciones_F-PSEA-10_Registro_Preprocesamiento.md`. |
| `F-PSEA-11` | Homogeneidad y estabilidad del item | OK XLSX parcial | Se crearon XLSX maestros desde `ronda_1_homogeneidad.csv` y `ronda_1_estabilidad.csv`; quedan otros anexos por definir. |
| `F-PSEA-11A` | Datos preprocesados de homogeneidad | OK maestro | `01_bloque_general/04_formatos_maestros/F-PSEA-11A Datos preprocesados de homogeneidad.docx`. |
| `F-PSEA-11B` | Datos preprocesados de estabilidad | OK maestro | `01_bloque_general/04_formatos_maestros/F-PSEA-11B Datos preprocesados de estabilidad.docx`. |
| `F-PSEA-11C` | Resultados de homogeneidad | OK maestro | `01_bloque_general/04_formatos_maestros/F-PSEA-11C Resultados de homogeneidad.docx`. |
| `F-PSEA-11D` | Resultados de estabilidad | OK maestro | `01_bloque_general/04_formatos_maestros/F-PSEA-11D Resultados de estabilidad.docx`. |
| `F-PSEA-12` | Datos oficiales consolidados para evaluacion de aptitud | OK XLSX | Maestro XLSX creado con encabezado desde `ronda_1_completa.csv`; CSV conservado como fuente operativa. |
| `F-PSEA-13` | Informe final de resultados | OK DOCX | Maestro copiado desde `EA-PP2026-R1-1-z-4-2a.docx`. |
| `F-PSEA-14` | Registro caso de queja o NC | OK maestro | `01_bloque_general/04_formatos_maestros/F-PSEA-14 Registro caso de queja o NC segun aplique.docx`. |
| `F-PSEA-15` | Registro de apelaciones | OK maestro | `01_bloque_general/04_formatos_maestros/F-PSEA-15 Registro de apelaciones.docx`. |
| `F-PSEA-16` | Matriz de competencia autorizacion | OK maestro | `01_bloque_general/04_formatos_maestros/F-PSEA-16 Matriz de competencia autorizacion.docx`. |
| `F-PSEA-17` | Evaluacion de proveedores criticos | OK maestro | `01_bloque_general/04_formatos_maestros/F-PSEA-17 Evaluacion de proveedores criticos.docx`. |

---

## Faltantes priorizados

1. `01_bloque_general/02_procedimientos/P-PSEA-05 Comunicaciones del PEA.docx` - implementado desde las instrucciones en `instrucciones_P-PSEA-05_Comunicaciones_PEA.md`.
2. `01_bloque_general/04_formatos_maestros/F-PSEA-04 Anexo tecnico de equipos e instrumentos.xlsx` y `.csv` - implementado desde `ronda_1_equipos.csv`.
3. `01_bloque_general/04_formatos_maestros/F-PSEA-07 Preparacion y control del item.xlsx` - implementado desde `F-PSEA-02 Cronograma Detallado_v0.xlsx`.
4. `01_bloque_general/04_formatos_maestros/F-PSEA-08 Datos reportados por participante.xlsx` y `.csv` - plantilla implementada para `calaire-app`.
5. `01_bloque_general/04_formatos_maestros/F-PSEA-09 Datos de participantes exportados para analisis PT.xlsx` y `.csv` - plantilla implementada para exportacion `calaire-app` hacia `pt_app`.
6. `01_bloque_general/04_formatos_maestros/F-PSEA-10 Registro de preprocesamiento de datos.xlsx` y `.csv` - plantilla implementada para trazabilidad de `pt_app`.
7. `01_bloque_general/04_formatos_maestros/F-PSEA-11 Homogeneidad datos.xlsx`/`.csv` y `F-PSEA-11 Estabilidad datos.xlsx`/`.csv` - implementados desde los CSV de ronda; otros anexos quedan por definir.
8. `01_bloque_general/04_formatos_maestros/F-PSEA-12 Datos oficiales consolidados para evaluacion de aptitud.xlsx` y `.csv` - implementado desde `ronda_1_completa.csv`.
9. `01_bloque_general/04_formatos_maestros/F-PSEA-13 Informe final de resultados.docx` - implementado desde `EA-PP2026-R1-1-z-4-2a.docx`.

## Hallazgos de control

- `P-PSEA-11`, `P-PSEA-12` y `P-PSEA-13` tienen duplicados en `01_bloque_general/06_procedimientos_gestion/`; la ubicacion natural por tipo documental es `01_bloque_general/02_procedimientos/`.
- `F-PSEA-01`, `F-PSEA-02`, `F-PSEA-04`, `F-PSEA-07`, `F-PSEA-08`, `F-PSEA-09`, `F-PSEA-10`, `F-PSEA-11` y `F-PSEA-12` no deben forzarse a `.docx`; el maestro controlado es XLSX y el CSV queda como fuente/exportacion operativa cuando aplica.
- `F-PSEA-11` queda implementado parcialmente con homogeneidad y estabilidad; los anexos adicionales deben definirse cuando exista la fuente operacional.
- `F-PSEA-03` permanece ambiguo entre el mapa, las fichas y los ajustes ejecutados. No se recomienda crear `.docx` hasta cerrar la decision de codigo.
