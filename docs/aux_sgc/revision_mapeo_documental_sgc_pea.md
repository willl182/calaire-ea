# Revision de mapeo documental SGC PEA

**Fecha de revision:** 2026-06-18  
**Fuente normativa usada:** `mapa_navegacion_sgc_pea.html`  
**Alcance:** contraste entre la nomenclatura oficial del mapa HTML y los archivos existentes en `docs/documentacion_sgc`.

## Criterio aplicado

El archivo `mapa_navegacion_sgc_pea.html` se toma como fuente vigente para codificacion, numeracion y nombre documental. Los archivos en `fichas_resumen/` se tratan como derivados documentales y no como documentos maestros. Los archivos en `para_quitar/` se tratan como retirados o historicos, aunque se listan como evidencia de codigos obsoletos.

## Codigos oficiales del mapa HTML

| Familia | Codigos oficiales |
|---|---|
| Documentos generales | `DG-PSEA-01`, `DG-PSEA-02`, `DG-PSEA-03` |
| Procedimientos | `P-PSEA-01` a `P-PSEA-21` |
| Instructivos | `I-PSEA-02`, `I-PSEA-03`, `I-PSEA-04`, `I-PSEA-05` |
| Formatos / registros | `F-PSEA-01`, `F-PSEA-02`, `F-PSEA-04` a `F-PSEA-13`, `F-PSEA-11A`, `F-PSEA-11B`, `F-PSEA-11C`, `F-PSEA-11D` |

> Nota critica: el mapa HTML no lista `F-PSEA-03`, `I-PSEA-01`, `F-PSEA-05A`, `F-PSEA-14` a `F-PSEA-17`, `P-PSEA-22` ni `P-PSEA-23`.

## Mapa de archivos cuyo nombre o codigo debe cambiar

| Archivo actual | Diagnostico | Nombre/codigo recomendado segun mapa HTML |
|---|---|---|
| `01_bloque_general/02_procedimientos/P-PSEA-02 Procedimiento NO-NO2_v2.docx` | Usa numeracion antigua. En el mapa vigente `P-PSEA-02` es la matriz documental del PEA. | `P-PSEA-10 Procedimiento tecnico NO-NO2` |
| `01_bloque_general/02_procedimientos/P-PSEA-03 Procedimiento CO_v2.docx` | Usa numeracion antigua. En el mapa vigente `P-PSEA-03` es la matriz de registros y evidencias. | `P-PSEA-11 Procedimiento tecnico CO` |
| `01_bloque_general/02_procedimientos/P-PSEA-04 Procedimiento O3_v2.docx` | Usa numeracion antigua y entra en conflicto con `P-PSEA-04 Planificacion de ronda EA.md`. | `P-PSEA-12 Procedimiento tecnico O3` |
| `01_bloque_general/02_procedimientos/P-PSEA-05 Procedimiento SO2_v2.docx` | Usa numeracion antigua. En el mapa vigente `P-PSEA-05` es comunicaciones. | `P-PSEA-13 Procedimiento tecnico SO2` |
| `01_bloque_general/02_procedimientos/P-PSEA-06 Procedimiento Diseño Estadistico_v0.docx` | Usa numeracion antigua. En el mapa vigente `P-PSEA-06` es preparacion y control del item. | `P-PSEA-07 Diseno estadistico` |
| `01_bloque_general/02_procedimientos/P-PSEA-07 Procedimiento Informe Resultados_v0.docx` | Usa numeracion antigua. En el mapa vigente `P-PSEA-07` es diseno estadistico. | `P-PSEA-09 Informe de resultados` |
| `01_bloque_general/02_procedimientos/P-PSEA-08 Proc Colusión Falsificacion_v0.docx` | Usa numeracion antigua. En el mapa vigente `P-PSEA-08` es flujo tecnico de datos digitales. | `P-PSEA-14 Colusion y falsificacion` |
| `01_bloque_general/02_procedimientos/P-PSEA-09 Procedimiento Planificacion Ronda EA.docx` | Usa codigo correcto solo si se interpreta con mapa antiguo; en mapa HTML la planificacion es `P-PSEA-04`. | `P-PSEA-04 Planificacion de ronda EA`; consolidar con el `.md` existente |
| `01_bloque_general/02_procedimientos/P-PSEA-09 Procedimiento de Planificacion Ronda EA.docx` | Duplicado de planificacion con codigo incorrecto frente al mapa HTML. | Consolidar en `P-PSEA-04 Planificacion de ronda EA` o retirar duplicado |
| `01_bloque_general/04_formatos_maestros/F-PSEA-04 Formato Informe Resultados_v0.docx` | En el mapa vigente `F-PSEA-04` es equipos e instrumentos. El informe final es `F-PSEA-13`. | `F-PSEA-13 Informe final de resultados` |
| `01_bloque_general/04_formatos_maestros/F-PSEA-03 Registro Planificacion Ronda EA.xlsx` | `F-PSEA-03` no existe en el mapa HTML. | Retirar/reservar o absorber en `F-PSEA-05 Plan de ronda EA` / `F-PSEA-06 Ficha digital de ronda`, segun contenido |
| `02_prueba_piloto_rondas/00_planificacion/F-PSEA-05A Hoja de Registro del Participante.xlsx` | `F-PSEA-05A` no existe en el mapa HTML. | Requiere decision: absorber en `F-PSEA-08 Datos reportados` si son datos del participante, o recodificar como `F-PSEA-04` si corresponde a equipos e instrumentos |
| `02_prueba_piloto_rondas/00_planificacion/F-PSEA-05A-P1.xlsx`, `F-PSEA-05A-P1_DIL.xlsx`, `F-PSEA-05A-P2.xlsx` | Subformatos operativos no reconocidos por el mapa HTML. | Mantener solo como anexos operativos de ronda sin codigo maestro, o recodificar bajo el formato oficial que corresponda |
| `02_prueba_piloto_rondas/00_planificacion/F-PSEA-14 Registro caso de queja o NC segun aplique.md` | `F-PSEA-14` no existe en el mapa HTML. | Integrar el registro al flujo de `P-PSEA-15`, `P-PSEA-17` y el sistema de casos SGC; no conservar como formato oficial sin decision |
| `02_prueba_piloto_rondas/00_planificacion/F-PSEA-15 Registro de apelaciones.md` | `F-PSEA-15` no existe en el mapa HTML. | Asociar a `P-PSEA-18 Apelaciones`; no conservar como formato oficial sin decision |
| `02_prueba_piloto_rondas/00_planificacion/F-PSEA-16 Matriz de competencia autorizacion.md` | `F-PSEA-16` no existe en el mapa HTML. | Asociar a `P-PSEA-20 Competencia`; no conservar como formato oficial sin decision |
| `02_prueba_piloto_rondas/00_planificacion/F-PSEA-17 Evaluacion de proveedores criticos.md` | `F-PSEA-17` no existe en el mapa HTML. | Asociar a `P-PSEA-21 Proveedores criticos`; no conservar como formato oficial sin decision |
| `02_prueba_piloto_rondas/00_planificacion/P-PSEA-22 Riesgos generales del PEA.md` | `P-PSEA-22` no existe en el mapa HTML. | Retirar, reservar fuera del mapa o absorber en la gestion transversal definida por el SGC |
| `01_bloque_general/06_procedimientos_gestion/P-PSEA-23 Mejora continua del PEA.md` | `P-PSEA-23` no existe en el mapa HTML. | Retirar, reservar fuera del mapa o gestionar como parte del sistema macro de mejora |
| `01_bloque_general/03_instructivos/I-PSEA-01 Instructivo de Embalaje_v1.docx` | `I-PSEA-01` no existe en el mapa HTML, pero debe mantenerse por decision del equipo. | Mantener y corregir alcance: aplica al embalaje/manejo de equipos de participantes, no a items de ensayo |

## Codigos oficiales sin archivo maestro activo

| Codigo oficial | Nombre oficial en mapa HTML | Estado en mapa | Observacion |
|---|---|---:|---|
| `DG-PSEA-02` | `calaire-app` | Actualizar | Hay documentos sueltos (`calaire-app_func_docs_sgc.md`, `calaire-app_reg_docs_sgc.md`, `calaire-app_registros-sgc.html`), pero no existe archivo maestro codificado `DG-PSEA-02`. |
| `DG-PSEA-03` | `pt_app` | Elaborar | No se encontro archivo maestro codificado. Debe documentar preprocesamiento, consolidacion, analisis estadistico, H/E e informe final. |
| `F-PSEA-11A` | Subformato H/E A | Elaborar | Solo existe ficha resumen derivada; no hay formato maestro activo. |
| `F-PSEA-11B` | Subformato H/E B | Elaborar | Solo existe ficha resumen derivada; no hay formato maestro activo. |
| `F-PSEA-11C` | Subformato H/E C | Elaborar | Solo existe ficha resumen derivada; no hay formato maestro activo. |
| `F-PSEA-11D` | Subformato H/E D | Elaborar | Solo existe ficha resumen derivada; no hay formato maestro activo. |

## Codigos oficiales con archivos activos, pero con duplicidad o ubicacion a revisar

| Codigo | Archivos encontrados | Accion recomendada |
|---|---|---|
| `P-PSEA-01` | `.docx` y `.md` en `01_bloque_general/02_procedimientos/` | Definir archivo maestro unico y usar el otro como fuente historica o version editable. |
| `P-PSEA-04` | `.md` correcto y `.docx` antiguo de O3 con el mismo codigo | Renombrar el `.docx` de O3 a `P-PSEA-12`; conservar `P-PSEA-04` para planificacion. |
| `P-PSEA-09` | `.md` de informe y dos `.docx` de planificacion con codigo incorrecto | Conservar `P-PSEA-09` para informe; renombrar/retirar los `.docx` de planificacion. |
| `P-PSEA-10` | Archivo activo en `02_prueba_piloto_rondas/00_planificacion/` | Mover o consolidar como procedimiento maestro, no como documento operativo de ronda. |
| `P-PSEA-20` | Archivo activo en `02_prueba_piloto_rondas/00_planificacion/` | Mover o consolidar como procedimiento maestro de gestion, no como documento operativo de ronda. |
| `F-PSEA-01` | Plantilla base, formato maestro y version piloto | Mantener plantilla/base separada de evidencia de ronda; el maestro debe llamarse segun `Calendario global de ronda`. |
| `F-PSEA-02` | Formato maestro, copias piloto, exportaciones `PP202601/PP202602` | Separar formato maestro de registros diligenciados por ronda. |
| `F-PSEA-05` a `F-PSEA-13` | Copias en `00_planificacion`, `01_ronda_simple`, `02_ronda_compleja_fase1`, `03_ronda_compleja_fase2` | Conservar un maestro por codigo y tratar las copias de ronda como registros/evidencias de ejecucion. |
| `F-PSEA-06` | Copias por ronda y una copia en raiz | Eliminar o reubicar la copia de raiz si no es el maestro; evitar duplicidad fuera de carpeta. |

## Documentos, procedimientos, instructivos y formatos no listados por el mapa HTML

### Activos fuera de `para_quitar/`

| Codigo / archivo | Tipo | Diagnostico |
|---|---|---|
| `I-PSEA-01 Instructivo de Embalaje_v1.docx` | Instructivo | No listado, pero debe quedar. Alcance corregido: embalaje/manejo de equipos de participantes, no items de ensayo. |
| `F-PSEA-03 Registro Planificacion Ronda EA.xlsx` | Formato | No listado. Debe retirarse, reservarse o absorberse en formatos de planificacion vigentes. |
| `F-PSEA-05A*` | Formato/subformato | No listado. Requiere decision documental antes de mantenerlo como codigo oficial. |
| `F-PSEA-14 Registro caso de queja o NC segun aplique.md` | Formato/registro | No listado. El tratamiento debe quedar ligado a `P-PSEA-15` y `P-PSEA-17`, sin codigo oficial por ahora. |
| `F-PSEA-15 Registro de apelaciones.md` | Formato/registro | No listado. Asociado conceptualmente a `P-PSEA-18`, pero no reconocido como formato oficial. |
| `F-PSEA-16 Matriz de competencia autorizacion.md` | Formato/matriz | No listado. Asociado conceptualmente a `P-PSEA-20`, pero no reconocido como formato oficial. |
| `F-PSEA-17 Evaluacion de proveedores criticos.md` | Formato/registro | No listado. Asociado conceptualmente a `P-PSEA-21`, pero no reconocido como formato oficial. |
| `P-PSEA-22 Riesgos generales del PEA.md` | Procedimiento | No listado. Debe retirarse, reservarse fuera del mapa o integrarse a gestion transversal. |
| `P-PSEA-23 Mejora continua del PEA.md` | Procedimiento | No listado. Debe retirarse, reservarse fuera del mapa o gestionarse como proceso macro. |

### Retirados o historicos en `para_quitar/`

| Codigos encontrados | Diagnostico |
|---|---|
| `P-PSEA-24`, `P-PSEA-25`, `P-PSEA-26`, `P-PSEA-27`, `P-PSEA-28` | No listados por el mapa HTML. La carpeta confirma que la numeracion anterior fue retirada. |
| `F-PSEA-18`, `F-PSEA-19`, `F-PSEA-20`, `F-PSEA-21`, `F-PSEA-22`, `F-PSEA-23` | No listados. Deben permanecer fuera del sistema maestro salvo decision explicita de reincorporacion. |
| `I-PSEA-06` a `I-PSEA-15` | No listados. Corresponden a una arquitectura anterior de instructivos desagregados que el mapa vigente no conserva. |

## Archivos sin codigo SGC que requieren clasificacion

| Archivo o grupo | Diagnostico | Accion recomendada |
|---|---|---|
| `calaire-app_func_docs_sgc.md`, `calaire-app_reg_docs_sgc.md`, `calaire-app_registros-sgc.html` | Documentan partes de `calaire-app`, pero no estan codificados. | No tocarlos; mantenerlos en carpeta aparte como soporte, sin absorberlos en `DG-PSEA-02`. |
| `ronda_1_completa.csv`, `ronda_1_equipos.csv`, `ronda_1_estabilidad.csv`, `ronda_1_homogeneidad.csv` | Evidencias/datasets tecnicos de ronda. | Mapear como registros asociados a `F-PSEA-12`, `F-PSEA-04` y `F-PSEA-11A-D`, no necesariamente como formatos maestros. |
| `Planificacion_R1_PP (1).md` y copia en `01_bloque_general/` | Documento operativo duplicado. | Consolidar como evidencia de ronda o absorber en `F-PSEA-05` / `F-PSEA-02`. |
| `analisis_sgc.md`, `sgc_res.md`, `mapa_tentativo_sgc_pea.md`, `mapa_decisiones_documentales_pea.md` | Documentos de analisis/arquitectura, no documentos controlados del SGC. | Mantener como documentos de trabajo; no codificar como `P/I/F` salvo decision. |
| `sesion_grill_sgc_pea_v1.md`, `sesion_grill_sgc_pea_v2.md` | Evidencia de trabajo interno de diseno documental. | Mantener como soporte historico; no codificar como documento del SGC. |
| `02_prueba_piloto_rondas/04_informes_operativos/*` | Informes operativos de proyecto/piloto. | Clasificar como evidencia de gestion de prueba piloto, no como `F-PSEA-13` salvo que sean informes finales de resultados EA. |
| `02_prueba_piloto_rondas/05_evidencias_soporte/*` y `06_ronda_fase3/*` | Evidencias de soporte, Gantt y timelines. | Mantener como soportes operativos; no confundir con formatos maestros. |

## Recomendacion de reorganizacion documental

1. Declarar `mapa_navegacion_sgc_pea.html` como fuente vigente de codigos.
2. Separar tres capas: documentos maestros, registros/evidencias de ronda y documentos de trabajo.
3. Renombrar o retirar los documentos con numeracion antigua antes de seguir redactando contenido.
4. Crear los maestros faltantes `DG-PSEA-02`, `DG-PSEA-03` y `F-PSEA-11A` a `F-PSEA-11D`.
5. Resolver explicitamente si `F-PSEA-14` a `F-PSEA-17`, `P-PSEA-22` y `P-PSEA-23` quedan fuera del SGC PEA o si el mapa HTML debe actualizarse para reincorporarlos.
6. Actualizar las fichas resumen despues de estabilizar nombres y codigos maestros, no antes.
