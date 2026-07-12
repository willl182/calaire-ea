# Checklist de Elaboracion Documental SGC PEA

**Fecha de control:** 2026-06-14  
**Fuente de trabajo:** `sgc_pdts.md`  
**Referencia estructural:** `docs/documentacion_sgc/01_bloque_general/02_procedimientos/P-PSEA-01 Protocolo General EA_v2.docx`  
**Plantillas obligatorias:** `docs/documentacion_sgc/01_bloque_general/00_plantillas_base/`
**Matriz de equivalencias:** `matriz_equivalencias_codigos_sgc_pea.md`

---

## Decision de Formato Fuente y Entregable

- Cada documento debe tener una version fuente en Markdown (`.md`) para facilitar procesamiento, revision por agentes y trazabilidad de cambios.
- Los procedimientos e instructivos se exportaran desde Markdown a `.docx` mediante Pandoc y luego se ajustaran contra la plantilla base correspondiente cuando sea necesario.
- Los formatos y matrices se disenaran primero en Markdown como especificacion de campos, reglas y trazabilidad. Si el `F-PSEA` es tabular, debe tener version cruda `.csv`; el `.xlsx` debe incluir una hoja operativa/formateada y otra hoja exportable equivalente al CSV. Si el `F-PSEA` es un formulario narrativo, acta, plantilla diligenciable o registro tipo Word, se generara como `.docx` desde Markdown usando base Word aplicable.
- `F-PSEA-11` se controla como un paquete documental unico de revision de datos con cuatro subsalidas: `13A` datos preprocesados de homogeneidad, `13B` datos preprocesados de estabilidad, `13C` resultados de homogeneidad y `13D` resultados de estabilidad. Cada subsalida debe tener CSV crudo y hoja exportable dentro del XLSX del paquete.
- `P-PSEA-02` y `P-PSEA-03` se elaboraran como procedimientos completos. Las matrices de documentos, registros y evidencias seran anexos o salidas operativas asociadas, no sustitutos del procedimiento.
- `P-PSEA-09` recuperara contenido del `.docx v0` existente, pero la fuente oficial se reconstruira en Markdown antes de exportar a `.docx` y ajustar contra plantilla.
- Las fuentes Markdown y los derivados `.docx`, `.xlsx` y `.csv` deben guardarse en la misma carpeta funcional del documento dentro de `docs/documentacion_sgc/`, no en una carpeta paralela. La ficha resumen permanece como referencia navegable, no como ubicacion de trabajo principal.
- Cuando ya exista un Markdown con el codigo documental correcto, ese archivo se reemplazara/desarrollara como fuente oficial. No se crearan duplicados tipo `_fuente.md`; el historial se conserva mediante git.
- Cuando un documento solo exista como ficha resumen, se creara un nuevo Markdown fuente en la carpeta funcional que corresponda dentro de `docs/documentacion_sgc/`. La ficha se usara solo como insumo de alcance y relaciones.
- Se mantendran nombres simples y existentes siempre que sean claros. Solo se ajustara el nombre cuando exista ambiguedad real para el control documental o para distinguir procedimiento, formato, instructivo o salida digital.
- Antes de renombrar archivos o elaborar documentos finales se debe aprobar la matriz de equivalencias viejo/nuevo en `matriz_equivalencias_codigos_sgc_pea.md`.
- `P-PSEA-02` debe elaborarse usando el mapa documental y el analisis de conectividad existentes. Debe resolver o dejar controlados los formatos desconectados identificados: `F-PSEA-03`, `F-PSEA-14`, `F-PSEA-15`, `F-PSEA-16` y `F-PSEA-17`.
- `P-PSEA-02` tendra dos capas: procedimiento Markdown con reglas y matriz resumida, y matriz documental tabular separada en CSV/XLSX para procesamiento operativo.
- La matriz documental separada de `P-PSEA-02` debe incluir como campos minimos: `codigo`, `nombre`, `tipo`, `estado`, `ubicacion`, `documento_rector`, `formatos_asociados`, `aplicativo_origen`, `accion_requerida` y `observaciones`.
- Las fichas resumen existentes no sustituyen el documento fuente: sirven como insumo de diseno y mapa de alcance.

---

## Criterio de Control

- **PTE:** el documento requiere elaboracion o cierre tecnico.
- **Disenado:** existe ficha, placeholder, Markdown de alcance, matriz conceptual o borrador inicial suficiente para no partir de cero.
- **Elaborado:** existe documento final en formato operativo SGC, alineado con plantilla base y listo para revision/aprobacion.
- **Decision grill-me:** antes de enviar a elaboracion se debe responder si el insumo existente es suficiente, si debe migrarse a plantilla base y que nivel de detalle exige el flujo real del PEA.

---

## Estructura Base a Mantener

Los procedimientos que se elaboren deben conservar la logica documental del protocolo general:

- Identificacion documental y control de revision.
- Objetivo, alcance, definiciones y documentos de referencia.
- Condiciones generales.
- Informacion especifica del procedimiento.
- Roles y responsabilidades.
- Desarrollo secuencial del proceso.
- Registros, salidas y evidencias asociadas.
- Control de revision, revision y aprobacion.

Las plantillas base a usar son:

- Procedimientos: `P-PSEA-01 Plantilla Procedimiento.doc`.
- Instructivos: `I-PSEA-01 Plantilla Instructivo.doc`.
- Formatos/registros tabulares: `F-PSEA-01 Plantilla Formato_Excel.xlsx`.
- Documentos generales: `DG-PSEA- Documento General.docx`, si el subagente determina que el artefacto no corresponde a procedimiento, instructivo o formato.

---

## Checklist Maestro

| Codigo | Documento por elaborar/controlar | Tipo | Evidencia encontrada | Plantilla base | PTE | Disenado | Elaborado | Accion siguiente |
|---|---|---|---|---|---|---|---|---|
| P-PSEA-09 | Procedimiento de generacion/emision del informe de resultados | Procedimiento | Existe `.docx v0` y ficha resumen | `P-PSEA-01 Plantilla Procedimiento.doc` | [x] | [x] | [ ] | Recuperar contenido del `.docx v0`, reconstruir fuente Markdown y exportar documento formal. |
| P-PSEA-06 | Preparacion y control del item de ensayo gaseoso | Procedimiento | Existe Markdown y ficha resumen | `P-PSEA-01 Plantilla Procedimiento.doc` | [x] | [x] | [ ] | Migrar desde Markdown a documento SGC y alinear con preparacion dinamica por cilindros/calibradores. |
| P-PSEA-02 | Control documental y matriz documental del PEA | Procedimiento de gestion documental + matriz tabular | Existe Markdown, ficha resumen, mapa documental y analisis de conectividad | `P-PSEA-01 Plantilla Procedimiento.doc` + `F-PSEA-01 Plantilla Formato_Excel.xlsx` | [x] | [x] | [ ] | Elaborar procedimiento completo con matriz resumida; crear matriz documental separada en CSV/XLSX para controlar documentos y formatos desconectados. |
| P-PSEA-03 | Control de registros, evidencias y matriz de registros del PEA | Procedimiento de gestion de registros | Existe Markdown y ficha resumen | `P-PSEA-01 Plantilla Procedimiento.doc` | [x] | [x] | [ ] | Elaborar procedimiento completo; la matriz de registros/evidencias queda como anexo o salida operativa asociada. |
| P-PSEA-08 | Flujo tecnico de datos digitales del PEA | Procedimiento | Existe Markdown y ficha resumen | `P-PSEA-01 Plantilla Procedimiento.doc` | [x] | [x] | [ ] | Elaborar flujo completo `calaire-app` a `pt_app`, entradas, validaciones, salidas y controles. |
| F-PSEA-06 | Ficha digital de ronda EA / lista maestra de participantes | Formato/registro | Existe Markdown por planificacion y rondas, mas ficha resumen | `F-PSEA-01 Plantilla Formato_Excel.xlsx` | [x] | [x] | [ ] | Convertir a formato tabular controlado exportable desde `calaire-app`. |
| F-PSEA-10 | Registro de preprocesamiento de datos / estabilidad | Formato/registro | Existe Markdown por planificacion y rondas, mas ficha resumen | `F-PSEA-01 Plantilla Formato_Excel.xlsx` | [x] | [x] | [ ] | Resolver nombre definitivo y campos de evidencia del `preprocesamiento_log.csv`. |
| F-PSEA-11A | Datos preprocesados de homogeneidad | Formato/salida digital | Existe ficha resumen especifica | `F-PSEA-01 Plantilla Formato_Excel.xlsx` | [x] | [x] | [ ] | Definir columnas, metadatos de ronda, version de script y criterio de trazabilidad. |
| F-PSEA-11B | Datos preprocesados de estabilidad | Formato/salida digital | Existe ficha resumen especifica | `F-PSEA-01 Plantilla Formato_Excel.xlsx` | [x] | [x] | [ ] | Definir columnas, metadatos de ronda, version de script y criterio de trazabilidad. |
| F-PSEA-11C | Resultados de homogeneidad | Formato/salida digital | Existe ficha resumen especifica | `F-PSEA-01 Plantilla Formato_Excel.xlsx` | [x] | [x] | [ ] | Definir salida estadistica, criterios ISO 13528 y evidencia de aprobacion. |
| F-PSEA-11D | Resultados de estabilidad | Formato/salida digital | Existe ficha resumen especifica | `F-PSEA-01 Plantilla Formato_Excel.xlsx` | [x] | [x] | [ ] | Definir salida estadistica, criterios ISO 13528 y evidencia de aprobacion. |
| F-PSEA-12 | Datos oficiales consolidados para evaluacion de aptitud | Formato/registro | Existe Markdown por planificacion y rondas, mas ficha resumen | `F-PSEA-01 Plantilla Formato_Excel.xlsx` | [x] | [x] | [ ] | Alinear con dataset definitivo `ronda_<n>_completa.csv` y aprobacion estadistica. |
| I-PSEA-04 | Uso del preprocesador de datos de `pt_app` | Instructivo | Existe ficha resumen | `I-PSEA-01 Plantilla Instructivo.doc` | [x] | [x] | [ ] | Elaborar paso a paso operativo con entradas, ejecucion, salidas y errores esperados. |
| I-PSEA-05 | Uso del modulo de analisis PT de `pt_app` | Instructivo | Existe ficha resumen | `I-PSEA-01 Plantilla Instructivo.doc` | [x] | [x] | [ ] | Elaborar paso a paso operativo para analisis estadistico, validacion e informe. |
| P-PSEA-15 | Trabajo no conforme, no conformidades y acciones correctivas | Procedimiento de gestion | Existe Markdown y ficha resumen | `P-PSEA-01 Plantilla Procedimiento.doc` | [x] | [x] | [ ] | Redactar cierre tecnico CAPA, relacion con quejas, apelaciones e imparcialidad. |
| P-PSEA-05 | Comunicaciones del PEA | Procedimiento de gestion | Existe Markdown y ficha resumen | `P-PSEA-01 Plantilla Procedimiento.doc` | [x] | [x] | [ ] | Formalizar canales oficiales, comunicaciones por aplicativo/correo y trazabilidad. |
| P-PSEA-16 | Divulgacion y control de valores sensibles | Procedimiento de gestion | Existe Markdown y ficha resumen | `P-PSEA-01 Plantilla Procedimiento.doc` | [x] | [x] | [ ] | Definir control de `x_pt`, `sigma_pt`, valores asignados y momentos de divulgacion. |
| P-PSEA-17 | Quejas del PEA | Procedimiento de gestion | Existe Markdown y ficha resumen | `P-PSEA-01 Plantilla Procedimiento.doc` | [x] | [x] | [ ] | Elaborar flujo de recepcion, evaluacion, respuesta, registro y cierre de quejas. |
| P-PSEA-18 | Apelaciones del PEA | Procedimiento de gestion | Existe Markdown y ficha resumen | `P-PSEA-01 Plantilla Procedimiento.doc` | [x] | [x] | [ ] | Elaborar flujo formal de apelaciones y separarlo de quejas/no conformidades. |
| P-PSEA-19 | Confidencialidad operativa interna del PEA | Procedimiento de gestion | Existe Markdown y ficha resumen | `P-PSEA-01 Plantilla Procedimiento.doc` | [x] | [x] | [ ] | Controlar codigos de participantes, acceso a datos y reglas de anonimato. |
| P-PSEA-20 | Competencia y autorizacion del personal del PEA | Procedimiento de gestion | Existe Markdown y ficha resumen | `P-PSEA-01 Plantilla Procedimiento.doc` | [x] | [x] | [ ] | Definir perfiles, autorizaciones, evidencias de competencia y matriz asociada. |
| P-PSEA-21 | Proveedores criticos del PEA | Procedimiento de gestion | Existe Markdown y ficha resumen | `P-PSEA-01 Plantilla Procedimiento.doc` | [x] | [x] | [ ] | Definir evaluacion de CRM, calibraciones externas y comunicacion de servicios externos. |
| F-PSEA-14 | Registro/caso de queja o no conformidad | Formato/registro | Existe Markdown y ficha resumen | `F-PSEA-01 Plantilla Formato_Excel.xlsx` | [x] | [x] | [ ] | Revisar si debe separar queja, no conformidad y CAPA o mantener formato integrado. |
| F-PSEA-15 | Registro de apelaciones | Formato/registro | Existe Markdown y ficha resumen | `F-PSEA-01 Plantilla Formato_Excel.xlsx` | [x] | [x] | [ ] | Diseñar campos de trazabilidad, evaluador independiente, decision y cierre. |
| F-PSEA-16 | Matriz de competencia y autorizacion | Formato/matriz | Existe Markdown y ficha resumen | `F-PSEA-01 Plantilla Formato_Excel.xlsx` | [x] | [x] | [ ] | Convertir a matriz controlada de roles, competencias, autorizaciones y vigencia. |
| F-PSEA-17 | Evaluacion de proveedores criticos | Formato/registro | Existe Markdown y ficha resumen | `F-PSEA-01 Plantilla Formato_Excel.xlsx` | [x] | [x] | [ ] | Definir criterios, calificacion, reevaluacion y evidencia documental. |

---

## Prioridad de Elaboracion

Los documentos que dependen directamente de `calaire-app` o `pt_app` no se elaboraran completamente desde este repositorio. En este grafo se dejara la instruccion documental, alcance SGC, estructura esperada y criterios de control; la elaboracion tecnica detallada debe delegarse a agentes dentro del repositorio de cada aplicativo.

La primera ola de preparacion debe concentrarse en dejar instrucciones para el flujo digital critico y sus evidencias:

1. `P-PSEA-08` Gestion de Datos: instruccion marco para agentes de `calaire-app` y `pt_app`.
2. `I-PSEA-04` Uso del preprocesador de datos de `pt_app`: elaborar en repositorio `pt_app`.
3. `I-PSEA-05` Uso del modulo de analisis PT de `pt_app`: elaborar en repositorio `pt_app`.
4. `F-PSEA-11` Paquete de revision/resultados de datos, con subsalidas `13A` a `13D`: especificar aqui, implementar con agente de `pt_app`.
5. `F-PSEA-12` Datos oficiales consolidados para evaluacion de aptitud: especificar aqui, implementar con agente de `pt_app`/`calaire-app` segun origen del dato.
6. `P-PSEA-09` Generacion/emision del informe de resultados: coordinar con agente de `pt_app` si el informe se genera automaticamente.

---

## Preguntas Grill-Me Pendientes Antes de Elaborar

1. Para cada procedimiento, confirmar la ruta exacta del Markdown fuente y del `.docx` exportado/formal.
2. Para cada formato F-PSEA, confirmar el esquema de columnas del CSV crudo y la correspondencia con la hoja exportable del XLSX.
3. Para `F-PSEA-11A` a `F-PSEA-11D`, definir columnas, reglas de validacion y hojas equivalentes dentro del paquete XLSX `F-PSEA-11`.
4. Para `P-PSEA-02` y `P-PSEA-03`, definir el anexo/matriz asociada y sus campos de control.
5. Para `P-PSEA-09`, extraer contenido util del `.docx v0` y mapearlo a la estructura Markdown oficial.

---

## Instruccion para Subagente Kimi 2.7 Code

Cuando se autorice la elaboracion de un documento, enviar al subagente con:

- Codigo documental y nombre decidido.
- Ruta del insumo existente identificado en este checklist.
- Plantilla base obligatoria segun tipo documental.
- Referencia estructural `P-PSEA-01 Protocolo General EA_v2.docx`.
- Alcance tecnico esperado segun `sgc_pdts.md`.
- Resultado requerido: documento elaborado en formato SGC, no solo ficha resumen.

Para documentos dependientes de aplicativos, el subagente Kimi en este repositorio no debe inventar comportamiento tecnico interno. Debe producir instrucciones de elaboracion, campos esperados, interfaces documentales y preguntas para el agente del repositorio aplicativo correspondiente.
