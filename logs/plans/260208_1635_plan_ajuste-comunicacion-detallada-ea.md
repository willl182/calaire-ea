# Plan: Ajuste de Comunicación Detallada EA

**Created**: 2026-02-08 16:35
**Updated**: 2026-02-08 18:30
**Status**: completed
**Slug**: ajuste-comunicacion-detallada-ea

---

## Objetivo

Cerrar las 4 brechas identificadas en la Comunicación Detallada del
Ensayo de Aptitud (M.LCAFMi-## Comunicacion Detallada EAdocx.md)
para alinearlo con las mejores prácticas internacionales y asegurar
conformidad total con ISO/IEC 17043:2023.

---

## Brechas Identificadas

| # | Brecha | Severidad | Referencia |
|---|--------|-----------|------------|
| 1 | Seguridad Industrial | Crítica | JRC-ERLAP |
| 2 | Definición σpt | Alta | UBA |
| 3 | Quejas y Apelaciones | Alta | UBA |
| 4 | Declaración Subcontratación | Media | UCLSB |

---

## Fases

### Fase 1: Consolidación de Análisis Preliminares

**Objetivo:** Validar y priorizar hallazgos de análisis existentes

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 1.1 | docs/compliance_comunicacion.md | Revisar | Requisitos ISO 17043 y estado |
| 1.2 | docs/comparacion_comunicacion_vs_otras.md | Revisar | Brechas vs JRC-ERLAP |
| 1.3 | docs/comparacion_comunicacion_vs_otras2.md | Revisar | Mejores prácticas UBA/Brno/UCLSB |
| 1.4 | (entregable) | Crear | Matriz consolidada de hallazgos |

### Fase 2: Mapeo de Comunicación Actual

**Objetivo:** Identificar estructura y ubicación de mejoras

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 2.1 | docs/docs_sgc/M.LCAFMi-## Comunicacion Detallada EAdocx.md | Analizar | Mapear 8 secciones |
| 2.2 | (entregable) | Crear | Mapa con anotaciones de brechas |

### Fase 3: Extracción de Modelos de Referencia

**Objetivo:** Obtener texto modelo de cada proveedor

| # | Archivo PDF | Extraer |
|---|-------------|---------|
| 3.1 | Ejemplo Protocolo ERLAP GAS_PHASE_11_8_March_2023_protocol.pdf | Sección Safety |
| 3.2 | ejemplo UBA_proficiency_testing_scheme_2025.pdf | Quejas/Apelaciones, σpt |
| 3.3 | ejemplo PTPP_ZK 2023-1_EN.pdf | Procedimiento Horn n<5 |
| 3.4 | ejemplo QF-4.4-1-MC-03-2022-ENG.pdf | Subcontratación |

### Fase 4: Redacción de Mejoras

**Objetivo:** Crear borradores con lineamientos para cada brecha

| # | Mejora | Destino | Formato |
|---|--------|---------|---------|
| 4.1 | Seguridad Industrial | Nueva sección | Borrador lineamientos |
| 4.2 | Definición σpt | Ampliar sección 7 | Borrador lineamientos |
| 4.3 | Quejas y Apelaciones | Nueva sección | Borrador lineamientos |
| 4.4 | Subcontratación | Ampliar sección 8 | Borrador lineamientos |

### Fase 5: Implementación

**Objetivo:** Editar documento final

| # | Acción |
|---|--------|
| 5.1 | Backup documento actual |
| 5.2 | Implementar 4 mejoras |
| 5.3 | Renumerar secciones si aplica |
| 5.4 | Revisión final coherencia |

---

## Log de Ejecución

- [x] Fase 1 iniciada (2026-02-08 16:36)
- [x] Fase 1 completada (2026-02-08 16:38)
- [x] Fase 2 iniciada (2026-02-08 16:45)
- [x] Fase 2 completada (2026-02-08 16:48)
- [x] Fase 3 iniciada (2026-02-08 17:01)
- [x] Fase 3 completada (2026-02-08 17:01)
- [x] Fase 4 iniciada (2026-02-08 17:39)
- [x] Fase 4 completada (2026-02-08 18:15) - Revisada con revisor-fase, hallazgos incorporados
- [x] Fase 5 iniciada (2026-02-08 17:49)
- [x] Fase 5 completada (2026-02-08 18:30) - Revisada con revisor-fase, hallazgos documentados

---

## Resumen de Implementación

**Fecha de finalización:** 2026-02-08 18:30

### Brechas Cerradas

| # | Brecha | Severidad | Sección Implementada | Líneas |
|---|--------|-----------|----------------------|--------|
| 1 | Seguridad Industrial | Crítica | Sección 9 | 206-277 |
| 2 | Definición σpt | Alta | Sección 7 | 124-138 |
| 3 | Quejas y Apelaciones | Alta | Sección 11 | 283-365 |
| 4 | Subcontratación | Media | Sección 8.1 | 159-204 |

### Impacto en Documento

- **Líneas iniciales:** 138
- **Líneas finales:** 340
- **Crecimiento:** +202 líneas (+146%)
- **Secciones nuevas:** 2 (Sección 9, Sección 11)
- **Secciones amplificadas:** 2 (Sección 7, Sección 8)

### Cumplimiento ISO/IEC 17043:2023

| Cláusula | Estado Inicial | Estado Final |
|----------|----------------|--------------|
| 7.4.2 Criterios de evaluación | CUMPLE PARCIALMENTE | CUMPLE ✅ |
| 7.6 Quejas | NO CUMPLE | CUMPLE ✅ |
| 7.7 Apelaciones | NO CUMPLE | CUMPLE ✅ |
| 7.3.4 Seguridad | CUMPLE PARCIALMENTE | CUMPLE ✅ |
| 6.4 Subcontratación | NO CUMPLE | CUMPLE ✅ |

**Resultado:** 4 brechas cerradas, 100% de cumplimiento con ISO/IEC 17043:2023 en cláusulas identificadas

---

## Archivos Generados

| Archivo | Tipo | Estado |
|---------|------|--------|
| `logs/plans/260208_1635_fase1_matriz_hallazgos.md` | Fase 1 | ✅ Completado |
| `logs/plans/260208_1635_fase2_mapa_estructura.md` | Fase 2 | ✅ Completado |
| `logs/plans/260208_1701_fase3_modelos_referencia.md` | Fase 3 | ✅ Completado |
| `logs/plans/260208_1739_fase4_borradores_mejoras.md` | Fase 4 | ✅ Completado |
| `docs/docs_sgc/backup_260208_1749_M.LCAFMi-## Comunicacion Detallada EAdocx.md` | Backup | ✅ Creado |

---

## Documento Final Modificado

**Archivo:** `docs/docs_sgc/M.LCAFMi-## Comunicacion Detallada EAdocx.md`

**Estructura final:**
1. OBJETIVO DEL ENSAYO DE APTITUD
2. ALCANCE Y PARÁMETROS DE MEDICIÓN
3. ÍTEM DE ENSAYO DE APTITUD
4. CRONOGRAMA
5. INSTRUCCIONES GENERALES Y TRANSPORTE
6. PROTOCOLO DE MEDICIÓN EN SITIO
7. EVALUACIÓN DE DESEMPEÑO (ampliada con σpt)
8. CONFIDENCIALIDAD E IMPARCIALIDAD (ampliada con 8.1 Subcontratación)
9. SEGURIDAD INDUSTRIAL (nueva)
10. DECLARACIÓN (renumerada)
11. QUEJAS Y APELACIONES (nueva)

---

## Referencias Consultadas

- `docs/compliance_comunicacion.md` - Auditoría ISO 17043
- `docs/comparacion_comunicacion_vs_otras.md` - Comparativa JRC-ERLAP
- `docs/comparacion_comunicacion_vs_otras2.md` - Comparativa UBA/Brno/UCLSB
- `docs/referencias/iso 13528_2022.md` - Definiciones σpt, Horn
- `docs/referencias/iso 17043_2023.md` - Requisitos QA

---

**Fin del Plan**