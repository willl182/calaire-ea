# Plan: Revisión del Informe de Resultados EA-2025

**Created**: 2026-02-08 19:17
**Updated**: 2026-02-08 19:17
**Status**: in_progress
**Slug**: revision-informe-resultados

---

## Objetivo

Revisar el informe de resultados del ensayo de aptitud EA_2025-12-10_13-z-3-3 conforme a los requisitos de ISO/IEC 17043:2023, ISO 13528:2022 y las mejores prácticas observadas en informes internacionales (JRC Barbiere, UBA). El objetivo es cerrar las brechas identificadas en el preanálisis y producir un documento de instrucciones (en formato markdown) que servirá como guía para la actualización de la plantilla Rmd que genera los informes futuros.

---

## Fases

### Fase 1: Insumos Normativos y Preanálisis

**Objetivo:** Consolidar los requisitos normativos aplicables y los hallazgos del preanálisis para construir la base de verificación del informe.

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 1.1 | docs/informes-calaire_vs-jrc_uba.md | Leer y analizar | Extraer hallazgos críticos: gestión de grupos pequeños (n<12), criterio σpt, estabilidad/homogeneidad, valor asignado (consenso vs referencia) |
| 1.2 | docs/referencias/iso 17043_2023.md | Leer y extraer | Requisitos de reporte (cláusula 7.4.3): elementos obligatorios en informes de EA |
| 1.3 | docs/referencias/iso 13528_2022.md | Leer y extraer | Métodos estadísticos: z-score, z′-score, ζ-score, algoritmo A, MADe, nIQR, compatibilidad metrológica (cláusula 7.8) |
| 1.4 | logs/plans/[new_file].md | Crear | Matriz de requisitos aplicables (valor asignado, σpt, estabilidad, criterios de evaluación, trazabilidad, reporte) |
| 1.5 | - | Revisar | Ejecutar revisión de fase con subagent `revisor-fase` |

### Fase 2: Revisión del Informe EA 2025-12-10

**Objetivo:** Convertir y analizar el informe actual para identificar brechas específicas frente a los requisitos normativos y el preanálisis.

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 2.1 | docs/docs_sgc/Informe_EA_2025-12-10_13-z-3-3.docx | Convertir | Convertir a markdown usando pandoc: `pandoc --track-changes=all archivo.docx -o informe_md.md` |
| 2.2 | docs/docs_sgc/informe_md.md | Leer y analizar | Revisar estructura: secciones presentes, tablas de datos, gráficas, notas metodológicas, criterios usados |
| 2.3 | docs/docs_sgc/informe_md.md | Identificar brechas | Comparar contra: (a) requisitos ISO 17043/13528, (b) hallazgos del preanálisis, (c) prácticas JRC/UBA |
| 2.4 | logs/plans/[new_file].md | Crear | Documento de hallazgos específicos (por sección del informe) con referencia a cláusulas normativas |
| 2.5 | - | Revisar | Ejecutar revisión de fase con subagent `revisor-fase` |

### Fase 3: Benchmarking con Barbiere/UBA y Plan de Cambios

**Objetivo:** Extraer buenas prácticas de los informes de referencia, comparar con el informe CALAIRE, y producir el documento final de instrucciones para Rmd.

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 3.1 | docs/referencias/2022 - Barbiere - Interlab SO2 CO O3 NOx-3.pdf | Extraer texto | Usar pdfplumber/pdftotext para extraer secciones: métodos estadísticos, criterios de desempeño, estabilidad/homogeneidad, estructura de reporte |
| 3.2 | docs/referencias/2024 - umweltbundeamt -Proficiency Testing 2024.pdf | Extraer texto | Extraer: uso de valores de referencia, criterio σpt fijo, gestión de inestabilidad |
| 3.3 | - | Comparar | Identificar prácticas alineadas con ISO que CALAIRE debe adoptar (ej: política de grupos pequeños, σpt fitness for purpose) |
| 3.4 | logs/plans/[new_file].md | Crear | Documento final `Instrucciones para Actualización de Plantilla Rmd de Informes EA.md` con: (a) cambios estructurales requeridos, (b) secciones nuevas a crear, (c) modificaciones en contenido, (d) ejemplos de texto a incluir |
| 3.5 | docs/Instrucciones para Actualización de Plantilla Rmd de Informes EA.md | Crear | Entregable final en formato markdown con todos los cambios explicados y ejemplos de implementación en Rmd |
| 3.6 | - | Revisar | Ejecutar revisión de fase con subagent `revisor-fase` |

---

## Log de Ejecución

- [x] Fase 1 iniciada
- [x] Fase 1 completada
- [x] Revisión Fase 1 ejecutada (pendiente)
- [x] Fase 2 iniciada
- [x] Fase 2 completada
- [x] Revisión Fase 2 ejecutada (pendiente)
- [x] Fase 3 iniciada
- [x] Fase 3 completada
- [x] Revisión Fase 3 ejecutada (pendiente)
- [x] Documento final entregado
