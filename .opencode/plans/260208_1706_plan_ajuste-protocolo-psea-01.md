# Plan: Ajuste del Protocolo General de Ensayo de Aptitud P-PSEA-01

**Created**: 2026-02-08 17:06
**Updated**: 2026-02-08 17:53
**Status**: implementation_ready
**Slug**: ajuste-protocolo-psea-01

---

## Objetivo

Actualizar el P-PSEA-01 para cerrar las brechas identificadas frente a ISO/IEC 17043:2023 e ISO 13528:2022, integrando formalmente el aplicativo CALAIRE-APP y definiendo criterios estadísticos explícitos.

---

## Fases

### Fase 1: Revisión del Análisis Preliminar

**Objetivo:** Validar y estructurar las brechas identificadas en el documento de compliance.

| # | Acción | Descripción |
|---|--------|-------------|
| 1.1 | Categorizar brechas | Clasificar las 5 brechas identificadas por criticidad (Blocking/Required/Suggestions) |
| 1.2 | Mapear requisitos normativos | Vincular cada brecha con cláusulas específicas de ISO 13528 e ISO 17043 |
| 1.3 | Priorizar | Ordenar por impacto en la validez del EA y factibilidad de implementación |
| 1.4 | Documentar hallazgos | Crear tabla resumen de brechas categorizadas |

**Brechas identificadas:**

| # | Brecha | Severidad | Referencia Normativa |
|---|--------|-----------|----------------------|
| B1 | Algoritmos robustos no especificados | Blocking | ISO 13528 Anexo C (C.2, C.3) |
| B2 | Criterios H/S cuantitativos ausentes | Blocking | ISO 13528 Cláusula 6.1, Anexo B |
| B3 | Criterio de decisión z vs z' no formalizado | Required | ISO 13528 Cláusula 9.2, 9.5 |
| B4 | Tratamiento grupos pequeños (n<5) no documentado | Blocking | ISO 17043 7.2.2.3, ISO 13528 5.4 |
| B5 | Compatibilidad metrológica no mencionada | Suggestions | ISO 13528 Cláusula 7.8 |

---

### Fase 2: Revisión del Protocolo Actual

**Objetivo:** Analizar estructura actual y determinar puntos de inserción para nuevos contenidos.

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 2.1 | P-PSEA-01 | Mapear secciones | Identificar estructura actual (Objetivo, Alcance, Definiciones, etc.) |
| 2.2 | P-PSEA-01 | Identificar vacíos | Contrastar secciones existentes vs. requisitos ISO 17043 Cláusula 7.2 |
| 2.3 | Procedimientos P-PSEA-02 a 05 | Revisar procedimientos | Verificar si los procedimientos específicos ya cubren algunas brechas |
| 2.4 | Manual CALAIRE-APP | Extraer criterios | Documentar criterios técnicos implementados en el software |

---

### Fase 3: Análisis de Ejemplos de Referencia

**Objetivo:** Extraer buenas prácticas de protocolos de referencia internacionales.

| # | Archivo | Enfoque de análisis |
|---|---------|---------------------|
| 3.1 | ERLAP GAS_PHASE_11_8_March_2023_protocol.pdf | Estructura para gases, definición de algoritmos |
| 3.2 | UBA_proficiency_testing_scheme_2025.pdf | Criterios de homogeneidad/estabilidad, grupos pequeños |
| 3.3 | PTB_Study_Guide_Proficiency_Testing_EN.pdf | Guías pedagógicas de buenas prácticas |
| 3.4 | PTPP_ZK 2023-1_EN.pdf | Formato de reporte de resultados |
| 3.5 | Barbiere 2022/2023 | Ejemplos reales de EA para SO2, CO, O3, NOx |

**Aspectos a extraer:**
- Estructura documental (secciones obligatorias)
- Redacción de criterios estadísticos
- Manejo de contingencias (n pequeño, incertidumbre alta)
- Formato de tablas de criterios

---

### Fase 4: Plan de Mejora del Protocolo

**Objetivo:** Definir los cambios específicos a implementar.

| # | Sección a crear/modificar | Contenido propuesto |
|---|---------------------------|---------------------|
| 4.1 | **Nueva sección: Métodos Estadísticos** | Especificar Algoritmo A, MADe, nIQR como métodos primarios (ref. ISO 13528 Anexo C) |
| 4.2 | **Nueva sección: Criterios de Homogeneidad y Estabilidad** | Definir umbral s_s ≤ 0.3σ_pt (ISO 13528 Anexo B) |
| 4.3 | **Modificar: Definiciones** | Añadir z', ζ-score, criterio u(x_pt) > 0.3σ_pt |
| 4.4 | **Nueva sección: Contingencias Estadísticas** | Procedimiento para n<5 participantes |
| 4.5 | **Modificar: Procesamiento de Datos** | Vincular formalmente al aplicativo CALAIRE-APP validado |
| 4.6 | **Nueva sección: Validación del Valor Asignado** | Comparación con valor de referencia (compatibilidad metrológica) |

---

### Fase 5: Implementación

**Objetivo:** Ejecutar los cambios en el documento P-PSEA-01.

| # | Acción | Archivo | Descripción |
|---|--------|---------|-------------|
| 5.1 | Crear backup | P-PSEA-01 | Preservar versión actual antes de edición |
| 5.2 | Añadir sección Métodos Estadísticos | P-PSEA-01 | Algoritmo A, MADe, nIQR con fórmulas |
| 5.3 | Añadir sección Criterios H/S | P-PSEA-01 | Tabla con criterios cuantitativos |
| 5.4 | Actualizar Definiciones | P-PSEA-01 | z', ζ, umbral incertidumbre |
| 5.5 | Añadir sección Contingencias | P-PSEA-01 | Procedimiento n<5 |
| 5.6 | Vincular CALAIRE-APP | P-PSEA-01 | Referencia formal al software |
| 5.7 | Añadir validación VA | P-PSEA-01 | Compatibilidad metrológica |
| 5.8 | Actualizar referencias | P-PSEA-01 | ISO 13528:2022, Manual CALAIRE-APP |
| 5.9 | Revisar con subagent | Fase 5 completa | Ejecutar revisor-fase |
| 5.10 | Commit y push | Git | Documentar cambios |

---

## Decisiones de Implementación

- **Formato:** Convertir P-PSEA-01 de tabla HTML a markdown estructurado
- **Nuevas secciones:** 4 (Métodos Estadísticos, Criterios H/S, Contingencias, Validación VA)
- **Secciones modificadas:** 3 (Definiciones, Procesamiento de Datos, Referencias)

---

## Log de Ejecución

- [x] Plan creado y aprobado (2026-02-08 17:06)
- [x] Fase 1 completada (2026-02-08 17:10) - Brechas categorizadas
- [x] Fase 2 completada (2026-02-08 17:12) - Estructura analizada
- [x] Fase 3 completada (2026-02-08 17:14) - Criterios ISO extraídos
- [x] Fase 4 completada (2026-02-08 17:15) - Plan de mejora aprobado
- [x] Fase 5 iniciada (2026-02-08 18:22) - Implementación en P-PSEA-01
- [x] Fase 5 completada (2026-02-08 18:22) - Secciones nuevas y modificaciones aplicadas
- [x] Revisión Fase 5 con revisor-fase (2026-02-08 18:22) - Ajustes de tabla H/E, redacción y enlaces
- [x] Revisión final y commit (2026-02-08 18:22)

---
## Sesión Guardada

- **CURRENT_SESSION.md**: Actualizado con estado de sesión P-PSEA-01
- **Hallazgos**: `logs/history/260208_1822_findings.md`
- **Timestamp**: 260208_1822
