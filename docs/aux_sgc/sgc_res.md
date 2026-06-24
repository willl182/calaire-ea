# Panorama actualizado del Sistema de Gestion de Calidad PEA

Este documento resume el estado vigente del mapa documental del **Proveedor de Ensayos de Aptitud (PEA)** para el proyecto **CALAIRE-EA**, alineado con `mapa_navegacion_sgc_pea.html` y con la bitacora de ejecucion `goals_mapeo_sgc.md`.

El sistema documental ya no debe leerse con la numeracion historica de los `.docx` antiguos. La referencia operativa vigente es el mapa funcional consolidado: documentos generales `DG-PSEA`, procedimientos `P-PSEA`, instructivos `I-PSEA` y formatos/registros `F-PSEA`, con trazabilidad entre aplicativos, flujo digital, formatos maestros y evidencias de ronda.

---

## 1. Marco de referencia

El SGC PEA se organiza para cubrir la operacion especifica del ensayo de aptitud de gases contaminantes criterio, tomando como referencias principales:

- **ISO/IEC 17043:2023:** requisitos para proveedores de ensayos de aptitud.
- **ISO 13528:2022:** criterios estadisticos para evaluacion de aptitud, valor asignado, desviacion estandar, outliers, homogeneidad y estabilidad.
- **ISO/IEC 17025:2017:** contexto tecnico de competencia para mediciones de gases contaminantes criterio.

El SGC PEA no pretende duplicar el sistema macro institucional. Cuando un proceso pertenece al sistema institucional general, el mapa PEA solo conserva la interfaz operativa necesaria para la ronda.

---

## 2. Arquitectura documental vigente

### 2.1 Documentos generales (`DG-PSEA`)

- `DG-PSEA-01` — Protocolo general de participacion. Se mantiene como documento marco y debe revisarse al cierre para citar el flujo digital, aplicativos e instructivos estabilizados.
- `DG-PSEA-02` — Aplicativo `calaire-app`. Documento maestro creado para gestion de rondas, participantes, cronogramas, ficha de ronda, captura/exportacion de datos y casos SGC asociados.
- `DG-PSEA-03` — Aplicativo `pt_app`. Documento maestro creado para preprocesamiento, consolidacion, analisis estadistico, homogeneidad/estabilidad e informe final.

Regla de control: los aplicativos no son formatos. Se documentan como documentos generales y se operan mediante instructivos; sus salidas oficiales se controlan como `F-PSEA`.

### 2.2 Procedimientos (`P-PSEA`)

La numeracion funcional vigente es:

| Codigo | Nombre funcional | Estado segun mapa / goals |
|---|---|---|
| `P-PSEA-01` | Protocolo general EA | Mantener; maestro editable `.md` y fuente `.docx` conviven para decision documental posterior. |
| `P-PSEA-02` | Matriz documental del PEA | Elaborar. |
| `P-PSEA-03` | Matriz de registros y evidencias | Elaborar. |
| `P-PSEA-04` | Planificacion de ronda EA | Actualizar; conecta con `calaire-app`, ficha digital, calendario, cronograma y plan de ronda. |
| `P-PSEA-05` | Comunicaciones | Actualizar. |
| `P-PSEA-06` | Preparacion y control del item de ensayo gaseoso | Maestro creado; diferencia item gaseoso del instructivo de embalaje de equipos de participantes. |
| `P-PSEA-07` | Diseno estadistico | Maestro creado desde la ficha vigente; corrige numeracion antigua. |
| `P-PSEA-08` | Flujo tecnico de datos digitales del PEA | Procedimiento de soporte creado para calaire-app, pt_app, CSV, H/E y dataset oficial. |
| `P-PSEA-09` | Generacion y emision del informe de resultados | Maestro existente/consolidado; absorbe el rol historico de informe de resultados. |
| `P-PSEA-10` | Procedimiento tecnico NO/NO2 | `.md` y `.docx` activo renombrado desde fuente antigua; debe aligerarse hacia particularidades del analito. |
| `P-PSEA-11` | Procedimiento tecnico CO | `.md` y `.docx` activo renombrado desde fuente antigua; debe aligerarse hacia particularidades del analito. |
| `P-PSEA-12` | Procedimiento tecnico O3 | `.md` y `.docx` activo renombrado desde fuente antigua; debe aligerarse hacia particularidades del analito. |
| `P-PSEA-13` | Procedimiento tecnico SO2 | `.md` y `.docx` activo renombrado desde fuente antigua; debe aligerarse hacia particularidades del analito. |
| `P-PSEA-14` | Colusion y falsificacion | Corregido; ya no corresponde a gestion de riesgos. |
| `P-PSEA-15` | Trabajo no conforme, no conformidades y acciones correctivas | Actualizar. |
| `P-PSEA-16` | Divulgacion y control de valores sensibles | Actualizar. |
| `P-PSEA-17` | Quejas | Actualizar. |
| `P-PSEA-18` | Apelaciones | Actualizar. |
| `P-PSEA-19` | Confidencialidad operativa | Actualizar. |
| `P-PSEA-20` | Competencia y autorizacion operativa | Reubicado como maestro de gestion. |
| `P-PSEA-21` | Proveedores criticos | Actualizar. |
| `P-PSEA-22` | Riesgos generales del PEA | Retirado/reservado fuera del mapa activo. |
| `P-PSEA-23` | Mejora continua del PEA | Reservado como placeholder; el contenido erroneo de gestion de datos fue retirado. |

Punto critico: `P-PSEA-14` es colusion y falsificacion. Cualquier referencia que lo trate como riesgos generales esta obsoleta.

### 2.3 Instructivos (`I-PSEA`)

Los instructivos vigentes quedan asociados al uso operativo de aplicativos:

- `I-PSEA-02` — Instructivo participante `calaire-app`.
- `I-PSEA-03` — Instructivo administracion de rondas en `calaire-app`.
- `I-PSEA-04` — Instructivo preprocesador `pt_app`.
- `I-PSEA-05` — Instructivo modulo de analisis PT en `pt_app`.

Las copias operativas duplicadas de estos instructivos en planificacion fueron movidas a `para_quitar/`; los maestros activos permanecen en `01_bloque_general/03_instructivos/`.

### 2.4 Formatos y registros (`F-PSEA`)

La estructura vigente de formatos y registros es:

| Codigo | Nombre funcional | Rol en el mapa |
|---|---|---|
| `F-PSEA-01` | Calendario global de ronda | Exportable desde `calaire-app`; alimenta planificacion y visualizaciones tipo Gantt. |
| `F-PSEA-02` | Cronograma detallado | Cronograma diligenciable/exportable de actividades de ronda. |
| `F-PSEA-04` | Equipos e instrumentos | Anexo tecnico de equipos e instrumentos del participante; insumo hacia `pt_app`. |
| `F-PSEA-05` | Plan de ronda EA | Plan tecnico-operativo de la ronda; debe indicar que H/E se documenta en `F-PSEA-11`. |
| `F-PSEA-05A` | Hoja de registro del participante | Subformato maestro creado; las variantes P1, P2 y DIL son anexos operativos retirados como maestros. |
| `F-PSEA-06` | Ficha digital de ronda | Formato maestro conservado en `01_bloque_general/04_formatos_maestros/`; copias de ronda son instancias/evidencias. |
| `F-PSEA-07` | Control del item gaseoso | Dossier/registro de preparacion, niveles y control del item. |
| `F-PSEA-08` | Datos reportados | Registro de datos reportados por participante en `calaire-app`. |
| `F-PSEA-09` | Exportacion para analisis PT | Exportacion oficial desde `calaire-app` hacia `pt_app`; no es el dataset consolidado final. |
| `F-PSEA-10` | Registro de preprocesamiento | Registro de ejecucion del preprocesador: entradas, salidas, version, responsable, ruta y observaciones. |
| `F-PSEA-11` | Homogeneidad y estabilidad | Registro principal H/E del item de ensayo. |
| `F-PSEA-11A` | Datos preprocesados de homogeneidad | Subformato maestro creado. |
| `F-PSEA-11B` | Datos preprocesados de estabilidad | Subformato maestro creado. |
| `F-PSEA-11C` | Resultados de homogeneidad | Subformato maestro creado. |
| `F-PSEA-11D` | Resultados de estabilidad | Subformato maestro creado. |
| `F-PSEA-12` | Dataset oficial consolidado | Datos oficiales consolidados para evaluacion de aptitud; equivalente a `ronda_<n>_completa.csv`. |
| `F-PSEA-13` | Informe final de resultados | Informe final generado desde `pt_app`. |
| `F-PSEA-14` | Registro caso de queja o NC segun aplique | Formato maestro creado y ajustado; conecta con quejas, TNC/NC y `calaire-app`. |
| `F-PSEA-15` | Registro de apelaciones | Formato maestro creado y ajustado. |
| `F-PSEA-16` | Matriz de competencia autorizacion | Formato maestro creado y ajustado. |
| `F-PSEA-17` | Evaluacion de proveedores criticos | Formato maestro creado y ajustado. |

Los formatos antiguos conflictivos `F-PSEA-03 Registro Planificacion Ronda EA.xlsx` y `F-PSEA-04 Formato Informe Resultados_v0.docx` fueron movidos a `para_quitar/` por conflicto con el mapa vigente.

---

## 3. Flujo oficial de datos

El flujo oficial de datos, segun `mapa_navegacion_sgc_pea.html`, se controla asi:

1. `P-PSEA-08` gobierna el flujo tecnico de datos digitales.
2. `DG-PSEA-02` documenta `calaire-app` como aplicativo de gestion, captura y exportacion.
3. `I-PSEA-02` guia al participante para registrar datos en `calaire-app`.
4. `F-PSEA-08` registra datos reportados por participantes.
5. `F-PSEA-09` consolida la exportacion oficial desde `calaire-app` hacia `pt_app`.
6. `DG-PSEA-03` documenta `pt_app` como aplicativo de preprocesamiento, analisis e informe.
7. `I-PSEA-04` guia la ejecucion del preprocesador.
8. `F-PSEA-10` registra la ejecucion del preprocesamiento.
9. `F-PSEA-12` conserva el dataset oficial consolidado para evaluacion de aptitud.
10. `I-PSEA-05` guia el modulo de analisis PT.
11. `F-PSEA-13` corresponde al informe final de resultados.

Los datasets tecnicos `ronda_1_completa.csv`, `ronda_1_equipos.csv`, `ronda_1_estabilidad.csv` y `ronda_1_homogeneidad.csv` se clasifican como evidencias/datasets tecnicos asociados al flujo digital. No se promueven automaticamente a formatos maestros independientes.

---

## 4. Ruta de homogeneidad y estabilidad

La ruta H/E queda separada del informe final y del flujo de captura de participantes:

1. `P-PSEA-06` define la preparacion y control del item gaseoso.
2. `F-PSEA-07` registra el control del item gaseoso.
3. `P-PSEA-07` define los criterios de diseno estadistico, incluyendo H/E.
4. `F-PSEA-11` es el registro principal de homogeneidad y estabilidad.
5. `F-PSEA-11A` a `F-PSEA-11D` documentan datos preprocesados y resultados de homogeneidad/estabilidad.
6. `I-PSEA-05` opera el modulo de analisis PT en `pt_app`.
7. `F-PSEA-13` integra el resultado final emitido como informe.

Correccion clave: ya no se deben usar codigos `F-PSEA-13A-D` para H/E. La serie vigente es `F-PSEA-11A-D`.

---

## 5. Ruta de planificacion de ronda

La planificacion se controla por:

- `P-PSEA-04` — procedimiento transversal de planificacion de ronda.
- `DG-PSEA-02` — soporte de `calaire-app`.
- `I-PSEA-03` — administracion interna de rondas y exportaciones.
- `F-PSEA-01` — calendario global de ronda.
- `F-PSEA-02` — cronograma detallado.
- `F-PSEA-05` — plan de ronda EA.
- `F-PSEA-06` — ficha digital de ronda.
- `P-PSEA-06` — enlace con preparacion/control del item.

Las copias por ronda se tratan como instancias/evidencias operativas, no como maestros paralelos.

---

## 6. Estado de cierre del mapeo

Segun `goals_mapeo_sgc.md`, el mapeo ya tiene resueltos los principales bloques de reorganizacion:

- Creacion de `DG-PSEA-02` y `DG-PSEA-03`.
- Creacion de instructivos `I-PSEA-02` a `I-PSEA-05`.
- Creacion de subformatos H/E `F-PSEA-11A` a `F-PSEA-11D`.
- Creacion y ajuste de formatos de gestion `F-PSEA-14` a `F-PSEA-17`.
- Consolidacion de `P-PSEA-06`, `P-PSEA-07`, `P-PSEA-08`, `P-PSEA-09` y `P-PSEA-14`.
- Renombrado/conservacion de procedimientos por analito `P-PSEA-10` a `P-PSEA-13` con `.md` y `.docx` activos.
- Reclasificacion de fuentes antiguas y movimiento de duplicados a `para_quitar/` cuando corresponde.
- Clasificacion de soportes `calaire-app`, datasets tecnicos, documentos de analisis, sesiones grill, informes operativos y evidencias de soporte.

Queda como control de calidad posterior revisar contenido interno de procedimientos de gestion que aun puedan conservar placeholders desalineados, especialmente `P-PSEA-15` y `P-PSEA-16`, antes de declarar el paquete documental listo para revision formal.

---

## 7. Referencias internas

- [Mapa de navegacion SGC PEA](mapa_navegacion_sgc_pea.html)
- [Goals mapeo SGC PEA](goals_mapeo_sgc.md)
- [Checklist mapeo SGC PEA](checklist_mapeo_sgc_pea.json)
- [Mapa de decisiones documentales](mapa_decisiones_documentales_pea.md)
- [Mapa tentativo del SGC PEA](mapa_tentativo_sgc_pea.md)
- [Indice de fichas resumen](fichas_resumen/README.md)
