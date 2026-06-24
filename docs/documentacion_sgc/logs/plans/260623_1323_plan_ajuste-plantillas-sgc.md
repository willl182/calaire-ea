# Plan: Ajuste de documentos controlados SGC a plantillas base

**Created**: 2026-06-23 13:23
**Updated**: 2026-06-24 11:30
**Status**: in_progress
**Slug**: ajuste-plantillas-sgc

---

## Objetivo

Asegurar que todo documento controlado del SGC PEA listado en `mapa_navegacion_sgc_pea.html` utilice la plantilla institucional que corresponde a su familia documental:

| Familia | Plantilla base obligatoria |
|---|---|
| DG | `01_bloque_general/00_plantillas_base/DG-PSEA- Documento General.docx` |
| P | `01_bloque_general/00_plantillas_base/P-PSEA-01 Plantilla Procedimiento.doc` |
| I | `01_bloque_general/00_plantillas_base/I-PSEA-01 Plantilla Instructivo.doc` |
| F | `01_bloque_general/00_plantillas_base/F-PSEA-01 Plantilla Formato_Excel.xlsx` |

El ajuste debe conservar el contenido técnico vigente, codificación documental, títulos, trazabilidad normativa, estado del mapa y vínculo con los registros operativos. La salida esperada es un conjunto de documentos maestros normalizados y una evidencia de verificación que indique qué archivo fue reconstruido desde plantilla, cuál no aplica y cuál queda pendiente por decisión.

---

## Alcance

### Incluido

- Documentos controlados identificados en `mapa_navegacion_sgc_pea.html` con códigos `DG-PSEA`, `P-PSEA`, `I-PSEA` y `F-PSEA`.
- Documentos maestros ubicados principalmente en:
	- `01_bloque_general/01_documentos_marco/`
	- `01_bloque_general/02_procedimientos/`
	- `01_bloque_general/03_instructivos/`
	- `01_bloque_general/04_formatos_maestros/`
	- `01_bloque_general/06_procedimientos_gestion/`
- Formatos maestros `F-PSEA` en Word o Excel cuando el mapa los trata como documentos controlados del sistema.
- Actualización de evidencias de control documental: inventario, mapa de navegación y registro de ajustes.

### Excluido

- Copias operativas por ronda en `02_prueba_piloto_rondas/`, salvo que se decida expresamente regenerarlas desde el maestro normalizado.
- Archivos en `para_quitar/`.
- CSV operativos, imágenes, HTML de análisis y documentos auxiliares no controlados.
- Reescritura técnica del contenido, salvo ajustes mínimos requeridos para encajar en la plantilla o corregir metadatos documentales.

---

## Inventario inicial desde el mapa

### Documentos generales

| Código | Documento | Estado mapa | Acción de plantilla |
|---|---|---|---|
| DG-PSEA-01 | Protocolo general de participación | Mantener | Verificar y, si no usa plantilla DG, reconstruir desde `DG-PSEA- Documento General.docx`. |
| DG-PSEA-02 | Aplicativo calaire-app | Actualizar | Reconstruir desde plantilla DG y conservar descripción del aplicativo. |
| DG-PSEA-03 | Aplicativo pt_app | Elaborar | Elaborar/reconstruir desde plantilla DG. |

### Procedimientos

| Código | Documento | Estado mapa | Acción de plantilla |
|---|---|---|---|
| P-PSEA-01 | Protocolo general EA | Mantener | Normalizar contra plantilla P. |
| P-PSEA-02 | Matriz documental del PEA | Elaborado | Normalizar contra plantilla P o reclasificar si su naturaleza no es procedimiento. |
| P-PSEA-03 | Control de registros y evidencias | Elaborado | Normalizar contra plantilla P. |
| P-PSEA-04 | Planificación de ronda EA | Actualizar | Normalizar contra plantilla P. |
| P-PSEA-05 | Comunicaciones | Implementado | Verificar plantilla; reconstruir si fue generado sin base P. |
| P-PSEA-06 | Preparación y control del ítem | Actualizar | Normalizar contra plantilla P. |
| P-PSEA-07 | Diseño estadístico | Actualizar | Normalizar contra plantilla P. |
| P-PSEA-08 | Flujo técnico de datos digitales | Elaborar | Elaborar desde plantilla P. |
| P-PSEA-09 | Informe de resultados | Elaborar | Elaborar desde plantilla P. |
| P-PSEA-10 | NO/NO2 | Implementado | Migrar contenido del DOCX original a plantilla P. |
| P-PSEA-11 | CO | Implementado | Migrar contenido del DOCX original a plantilla P. |
| P-PSEA-12 | O3 | Implementado | Migrar contenido del DOCX original a plantilla P. |
| P-PSEA-13 | SO2 | Implementado | Migrar contenido del DOCX original a plantilla P. |
| P-PSEA-14 | Colusión y falsificación | Actualizar | Normalizar contra plantilla P. |
| P-PSEA-15 | TNC / NC / CAPA | Actualizar | Normalizar contra plantilla P. |
| P-PSEA-16 | Valores sensibles | Actualizar | Normalizar contra plantilla P. |
| P-PSEA-17 | Quejas | Actualizar | Normalizar contra plantilla P. |
| P-PSEA-18 | Apelaciones | Actualizar | Normalizar contra plantilla P. |
| P-PSEA-19 | Confidencialidad | Actualizar | Normalizar contra plantilla P. |
| P-PSEA-20 | Competencia | Actualizar | Normalizar contra plantilla P. |
| P-PSEA-21 | Proveedores críticos | Actualizar | Normalizar contra plantilla P. |

### Instructivos

| Código | Documento | Estado mapa | Acción de plantilla |
|---|---|---|---|
| I-PSEA-02 | Participante en calaire-app | Actualizar | Normalizar contra plantilla I. |
| I-PSEA-03 | Administración de rondas | Actualizar | Normalizar contra plantilla I. |
| I-PSEA-04 | Preprocesador pt_app | Elaborar | Elaborar desde plantilla I. |
| I-PSEA-05 | Análisis PT en pt_app | Elaborar | Elaborar desde plantilla I. |

### Formatos

| Código | Documento | Estado mapa | Acción de plantilla |
|---|---|---|---|
| F-PSEA-01 | Calendario global de ronda | Actualizar | Normalizar como XLSX desde plantilla F. |
| F-PSEA-02 | Cronograma detallado | Actualizar | Normalizar como XLSX desde plantilla F. |
| F-PSEA-04 | Equipos e instrumentos | Implementado | Verificar estructura XLSX contra plantilla F; ajustar encabezado y control documental. |
| F-PSEA-05 | Plan de ronda EA | Actualizar | Decidir si debe ser DOCX o XLSX; si es formato controlado, aplicar plantilla F o justificar excepción. |
| F-PSEA-06 | Ficha digital de ronda | Elaborar | Decidir si debe ser DOCX o XLSX; si es formato controlado, aplicar plantilla F o justificar excepción. |
| F-PSEA-07 | Control del ítem gaseoso | Implementado | Normalizar como XLSX desde plantilla F. |
| F-PSEA-08 | Datos reportados | Implementado | Normalizar como XLSX desde plantilla F. |
| F-PSEA-09 | Exportación para análisis PT | Implementado | Normalizar como XLSX desde plantilla F. |
| F-PSEA-10 | Registro de preprocesamiento | Implementado | Normalizar como XLSX desde plantilla F. |
| F-PSEA-11 | Homogeneidad y estabilidad | Parcial | Normalizar XLSX maestros desde plantilla F y cerrar decisión sobre anexos. |
| F-PSEA-11A | Subformato H/E A | Elaborar | Definir soporte documental y plantilla obligatoria. |
| F-PSEA-11B | Subformato H/E B | Elaborar | Definir soporte documental y plantilla obligatoria. |
| F-PSEA-11C | Subformato H/E C | Elaborar | Definir soporte documental y plantilla obligatoria. |
| F-PSEA-11D | Subformato H/E D | Elaborar | Definir soporte documental y plantilla obligatoria. |
| F-PSEA-12 | Dataset oficial consolidado | Implementado | Normalizar como XLSX desde plantilla F. |
| F-PSEA-13 | Informe final de resultados | Implementado | Tratar como excepción controlada: aunque su código es F, el mapa lo define como informe DOCX; documentar si debe usar plantilla DG, plantilla específica de informe o si se mantiene formato propio. |

---

## Fases

### Fase 1: Auditoría técnica de uso de plantillas

**Objetivo:** Confirmar, con evidencia, qué documentos controlados no fueron creados desde su plantilla base y cuáles requieren migración.

| # | Archivo / conjunto | Acción | Descripción |
|---|---|---|---|
| 1.1 | `mapa_navegacion_sgc_pea.html` | Extraer | Generar lista canónica de documentos controlados, familia, estado y ruta esperada. |
| 1.2 | `01_bloque_general/00_plantillas_base/` | Perfilar | Identificar estructura, estilos, encabezados, pies, metadatos y campos obligatorios de cada plantilla. |
| 1.3 | `01_bloque_general/**/*.docx`, `*.doc`, `*.xlsx` | Auditar | Comparar estilos, encabezados, propiedades y estructura contra la plantilla correspondiente. |
| 1.4 | `01_bloque_general/05_matrices_inventarios/Inventario Documental del SGC.md` | Contrastar | Verificar que el inventario refleje el mismo universo documental que el mapa. |
| 1.5 | `logs/` o `docs_sgc/` | Documentar | Crear matriz de brechas: código, archivo, plantilla requerida, evidencia de incumplimiento, acción y prioridad. |

**Criterios de aceptación:**

- Existe una matriz de brechas con todos los documentos controlados del mapa.
- Cada documento tiene clasificación: `cumple`, `no cumple`, `no existe`, `excepción por definir` o `no aplica`.
- Las excepciones `F-PSEA-05`, `F-PSEA-06`, `F-PSEA-13` y subformatos `F-PSEA-11A` a `F-PSEA-11D` quedan explícitamente señaladas para decisión.

### Fase 2: Definición de reglas de migración

**Objetivo:** Evitar ajustes inconsistentes entre familias documentales antes de modificar archivos maestros.

| # | Archivo / conjunto | Acción | Descripción |
|---|---|---|---|
| 2.1 | Plantillas `DG`, `P`, `I`, `F` | Definir | Establecer campos obligatorios: código, título, versión, fecha, responsable, aprobación, control de cambios y paginación. |
| 2.2 | Documentos `P-PSEA` | Definir | Regla de transferencia de contenido: portada, objetivo, alcance, responsabilidades, desarrollo, registros, anexos y control de cambios. |
| 2.3 | Documentos `I-PSEA` | Definir | Regla de transferencia: propósito operativo, prerrequisitos, pasos, salidas, registros y control de versión. |
| 2.4 | Documentos `DG-PSEA` | Definir | Regla de transferencia para documentos descriptivos o marco. |
| 2.5 | Documentos `F-PSEA` | Definir | Regla de reconstrucción desde XLSX base: hoja de control, hoja diligenciable, validaciones, encabezados y campos protegidos. |
| 2.6 | Excepciones | Decidir | Definir tratamiento de informes y formatos actualmente en DOCX aunque pertenecen a familia `F`. |

**Criterios de aceptación:**

- Hay una regla escrita por familia documental.
- No se inicia migración masiva sin resolver si los formatos `F` en DOCX siguen en Word, pasan a Excel o quedan como excepción aprobada.

### Fase 3: Reconstrucción de documentos maestros

**Objetivo:** Crear versiones normalizadas de los documentos controlados usando la plantilla correspondiente como archivo de partida.

| # | Archivo / conjunto | Acción | Descripción |
|---|---|---|---|
| 3.1 | Documentos `DG-PSEA` | Reconstruir | Copiar plantilla DG y transferir contenido vigente conservando código y título. |
| 3.2 | Procedimientos `P-PSEA-01` a `P-PSEA-21` | Reconstruir | Copiar plantilla P y migrar contenido técnico por secciones. |
| 3.3 | Instructivos `I-PSEA-02` a `I-PSEA-05` | Reconstruir | Copiar plantilla I y migrar pasos operativos. |
| 3.4 | Formatos `F-PSEA` XLSX | Reconstruir | Copiar plantilla F y trasladar estructura, encabezados y validaciones necesarias. |
| 3.5 | Formatos `F-PSEA` DOCX | Resolver | Aplicar decisión de Fase 2: convertir a XLSX, migrar a plantilla documental aprobada o registrar excepción. |
| 3.6 | Archivos originales | Respaldar | Mantener copia trazable de los archivos previos a la normalización en una ubicación de respaldo acordada. |

**Criterios de aceptación:**

- Cada archivo maestro controlado inicia desde la plantilla base o tiene excepción documentada.
- El contenido técnico vigente no se pierde.
- Los archivos normalizados mantienen nomenclatura documental coherente con el mapa.

### Fase 4: Control de consistencia documental

**Objetivo:** Verificar que los documentos normalizados sean consistentes entre sí y con el sistema de navegación.

| # | Archivo / conjunto | Acción | Descripción |
|---|---|---|---|
| 4.1 | Documentos normalizados | Revisar | Verificar código, título, versión, fecha, responsable, tablas, numeración y control de cambios. |
| 4.2 | `mapa_navegacion_sgc_pea.html` | Actualizar | Cambiar notas de cobertura para indicar plantilla aplicada, estado y excepciones. |
| 4.3 | Inventario documental | Actualizar | Registrar ubicación, tipo, plantilla usada, estado y observación de control. |
| 4.4 | Matriz de brechas | Cerrar | Cambiar estado de cada documento a `normalizado`, `pendiente` o `excepción aprobada`. |
| 4.5 | Copias de ronda | Evaluar | Determinar si las carpetas de ronda deben regenerarse desde los maestros normalizados o conservarse como evidencia histórica. |

**Criterios de aceptación:**

- El mapa y el inventario no contradicen los archivos maestros.
- Todo documento controlado tiene plantilla aplicada o justificación de excepción.
- Quedan separadas las versiones maestras de las copias operativas de ronda.

### Fase 5: Cierre y trazabilidad

**Objetivo:** Dejar evidencia auditable del ajuste realizado.

| # | Archivo / conjunto | Acción | Descripción |
|---|---|---|---|
| 5.1 | Registro de ajustes | Crear | Documentar fecha, documento, acción, plantilla aplicada, responsable y observaciones. |
| 5.2 | `logs/CURRENT_SESSION.md` | Guardar | Persistir estado final, pendientes y decisiones tomadas. |
| 5.3 | Git | Commit | Confirmar cambios con mensaje trazable del ajuste documental. |
| 5.4 | Revisión final | Revisar | Confirmar que no quedan documentos controlados fuera de plantilla sin excepción. |

**Criterios de aceptación:**

- Existe evidencia de cierre de brechas.
- El repositorio contiene únicamente cambios intencionales.
- El siguiente responsable puede continuar sin reinterpretar el alcance.

---

## Prioridad de ejecución

1. Procedimientos `P-PSEA-10` a `P-PSEA-13`, porque el mapa indica que son copias directas de documentos originales y probablemente no nacen de la plantilla P.
2. Procedimientos transversales `P-PSEA-01` a `P-PSEA-09`, porque gobiernan el flujo técnico del PEA.
3. Documentos generales `DG-PSEA-01` a `DG-PSEA-03`, porque cierran el marco documental y los aplicativos.
4. Instructivos `I-PSEA-02` a `I-PSEA-05`, porque dependen de la estabilización de procedimientos y aplicativos.
5. Formatos `F-PSEA`, separando primero los XLSX naturales y dejando para decisión los formatos en DOCX o los informes.

---

## Riesgos y controles

| Riesgo | Impacto | Control |
|---|---|---|
| Pérdida de contenido técnico durante la migración | Alto | Transferir contenido desde copia respaldada y revisar contra MD fuente cuando exista. |
| Mezcla entre documento maestro y copia de ronda | Alto | Trabajar primero solo en `01_bloque_general/`; diferir `02_prueba_piloto_rondas/`. |
| Formatos `F` en DOCX sin regla clara | Alto | Resolver decisión en Fase 2 antes de migrar. |
| Plantillas P/I están en `.doc` legacy | Medio | Definir si se conserva `.doc` o se convierte a `.docx` como paso técnico controlado. |
| Mapa e inventario quedan desactualizados | Medio | Actualizarlos en Fase 4 como parte del criterio de aceptación, no como tarea opcional. |

---

## Decisiones pendientes

- Definir si `P-PSEA-01 Protocolo general EA` debe seguir como procedimiento `P` o tratarse como documento marco `DG`.
- Definir si `F-PSEA-05 Plan de ronda EA` y `F-PSEA-06 Ficha digital de ronda EA` deben permanecer en Word, migrar a Excel o registrarse como excepción.
- Definir si `F-PSEA-13 Informe final de resultados`, aunque tiene código `F`, requiere plantilla propia de informe, plantilla DG o excepción documentada.
- Definir si las plantillas `.doc` de procedimientos e instructivos deben convertirse a `.docx` antes de normalizar documentos nuevos.
- Definir ubicación de respaldos pre-migración para evitar mezclar archivos obsoletos con documentos activos.

---

## Log de Ejecución

- [x] Plan creado con inventario inicial desde `mapa_navegacion_sgc_pea.html`.
- [x] Fase 1 iniciada.
- [x] Fase 1 completada.
- [x] Fase 2 iniciada.
- [x] Fase 2 completada.
- [x] Fase 3 iniciada.
- [x] Fase 3 completada.
- [x] Fase 4 iniciada.
- [ ] Fase 4 completada.
- [ ] Fase 5 iniciada.
- [ ] Fase 5 completada.

### Ejecución 2026-06-24

- Intento de implementación descartado: se reconstruyeron documentos con conversión automática desde Markdown/CSV, lo cual no equivale a aplicar la plantilla mediante copia y pegado conservando la estructura fina del documento original.
- Se restauraron los 36 archivos modificados desde el respaldo temporal `/tmp/calaire_sgc_template_backup_20260624_073317/`.
- La siguiente ejecución debe aplicar el método correcto: abrir/copiar la plantilla institucional, preservar encabezado, estilos y secciones base, y pegar el contenido del documento anterior dentro de la estructura de la plantilla, con revisión visual por archivo.
- Reaplicación aceptada por decisión del usuario: se usó Pandoc con `--reference-doc` para DOCX y la plantilla Excel `F-PSEA-01 Plantilla Formato_Excel.xlsx` para XLSX.
- Se regeneraron 29 documentos Word: `DG-PSEA-02`, `DG-PSEA-03`, `P-PSEA-02` a `P-PSEA-09`, `P-PSEA-14` a `P-PSEA-21`, `I-PSEA-02` a `I-PSEA-05`, `F-PSEA-05`, `F-PSEA-06`, `F-PSEA-11A` a `F-PSEA-11D` y `F-PSEA-13`.
- Se regeneraron 7 libros Excel: `F-PSEA-04`, `F-PSEA-08`, `F-PSEA-09`, `F-PSEA-10`, `F-PSEA-11 Estabilidad`, `F-PSEA-11 Homogeneidad` y `F-PSEA-12`.
- Se conservaron fuera del ajuste `P-PSEA-01 Protocolo General EA_v2.docx` y `P-PSEA-10` a `P-PSEA-13`.
- Validación técnica: todos los DOCX/XLSX son Office ZIP válidos; los DOCX contienen el código documental correcto en encabezado; los XLSX conservan hojas de plantilla y una hoja `Datos` con el mismo número de filas que el CSV fuente.
- Respaldo temporal de esta reaplicación: `/tmp/calaire_sgc_template_backup_reapply_20260624_113010/`.
