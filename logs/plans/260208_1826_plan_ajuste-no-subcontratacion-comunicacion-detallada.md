# Plan: Ajuste de Sección 8.1 - Declaración de No Subcontratación

**Created**: 2026-02-08 18:26
**Updated**: 2026-02-08 18:26
**Status**: approved
**Slug**: ajuste-no-subcontratacion-comunicacion-detallada

---

## Objetivo

Corregir la sección 8.1 de la Comunicación Detallada del EA para declarar explícitamente que CALAIRE realiza **todas** las actividades del programa de EA internamente, sin utilizar subcontratistas, cumpliendo con el requisito de transparencia de ISO/IEC 17043:2023 cláusula 6.4.

---

## Justificación Normativa

ISO/IEC 17043:2023 cláusula 6.4 exige declarar la situación de subcontratación:
- Si hay subcontratación: identificar subcontratista, actividades, supervisión
- Si **no** hay subcontratación: declararlo explícitamente para transparencia

Referencia del Protocolo General EA (línea 49):
> *"El proveedor de EA no debe utilizar proveedores de servicios externos para las siguientes actividades: a) el diseño y la planificación de los programas de EA; b) la evaluación del rendimiento; c) la autorización de informes."*

---

## Fases

### Fase 1: Backup y Análisis

**Objetivo:** Crear backup y cuantificar extensión a reemplazar

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 1.1 | `docs/docs_sgc/backup_260208_1826_M.LCAFMi-## Comunicacion Detallada EAdocx.md` | Crear | Backup antes de modificaciones |
| 1.2 | Líneas 159-204 | Analizar | Cuantificar extensión a reemplazar |

### Fase 2: Redacción de Nueva Sección 8.1

**Objetivo:** Redactar declaración explícita de NO subcontratación

| # | Contenido | Descripción |
|---|-----------|-------------|
| 2.1 | Nueva sección 8.1 | Declaración explícita de NO subcontratación |
| 2.2 | Mantener título | "8.1. Subcontratación de Actividades" (mismo título) |
| 2.3 | Eliminar subsecciones | Eliminar 8.1.1, 8.1.2, 8.1.3, 8.1.4 |

**Texto propuesto para nueva sección 8.1:**

```markdown
**8.1. Subcontratación de Actividades**

El Laboratorio CALAIRE como proveedor del Ensayo de Aptitud declara que **todas las actividades** del programa de EA se realizan internamente por personal propio del Laboratorio, de conformidad con la norma ISO/IEC 17043:2023 (cláusula 6.4).

**No se utilizan servicios de subcontratistas** para ninguna de las actividades del programa de EA, incluyendo:

- Diseño y planificación del programa de EA
- Preparación, caracterización y homogeneidad del ítem de ensayo
- Ensayos de homogeneidad y estabilidad
- Evaluación del rendimiento de los participantes
- Elaboración y autorización de informes

El personal técnico del Laboratorio CALAIRE involucrado en cada actividad cuenta con la competencia técnica documentada y las autorizaciones formales correspondientes, conforme a los perfiles de cargo establecidos en el Sistema de Gestión de Calidad.

Esta declaración cumple con el requisito de transparencia de la norma ISO/IEC 17043:2023 (cláusula 6.4.1) respecto a la comunicación del esquema de gestión de actividades a los participantes del EA.
```

### Fase 3: Implementación

**Objetivo:** Editar documento final

| # | Acción | Archivo | Líneas |
|---|--------|---------|--------|
| 3.1 | Reemplazar | `M.LCAFMi-##_Comunicacion_Detallada_EAdocx.md` | 159-204 → nuevo texto |
| 3.2 | Verificar | Coherencia con sección 8 (Confidencialidad) | - |
| 3.3 | Verificar | Transición a sección 9 (Seguridad Industrial) | - |

### Fase 4: Verificación de Coherencia

**Objetivo:** Alinear con otros documentos del SGC

| # | Documento | Verificar |
|---|-----------|-----------|
| 4.1 | `P-PSEA-01 Protocolo General EA.md` | Alineación con declaración de roles internos (línea 49) |
| 4.2 | `P-PSEA-09 Procedimiento de Planificacion Ronda EA.md` | Revisar si menciona subcontratación, ajustar si necesario |
| 4.3 | `logs/plans/260208_1635_plan_ajuste-comunicacion-detallada-ea.md` | Actualizar estado |

### Fase 5: Documentación y Commit

**Objetivo:** Persistir cambios y documentar

| # | Acción | Descripción |
|---|--------|-------------|
| 5.1 | Actualizar plan padre | Añadir registro de corrección post-implementación |
| 5.2 | Crear finding | `logs/history/YYMMDD_HHMM_findings.md` con corrección |
| 5.3 | Commit | Mensaje descriptivo del cambio |

---

## Impacto Esperado

| Métrica | Antes | Después |
|---------|-------|---------|
| Líneas sección 8.1 | 46 (159-204) | ~15 |
| Subsecciones 8.1.x | 4 (8.1.1-8.1.4) | 0 |
| Estado ISO 6.4 | Declara subcontratación (incorrecto) | Declara NO subcontratación (correcto) |

---

## Riesgos y Mitigaciones

| Riesgo | Mitigación |
|--------|------------|
| Otros documentos mencionan subcontratación como opción | Verificar P-PSEA-09 en Fase 4.2 |
| Backup insuficiente | Ya existe backup 260208_1749 del plan anterior |

---

## Log de Ejecución

- [x] Fase 1 iniciada (2026-02-08 18:28)
- [x] Fase 1 completada (2026-02-08 18:28) - Revisada con revisor-fase, hallazgos sugerencias
- [x] Fase 2 iniciada (2026-02-08 18:30)
- [x] Fase 2 completada (2026-02-08 18:30)
- [x] Fase 3 iniciada (2026-02-08 18:31)
- [x] Fase 3 completada (2026-02-08 18:31) - Revisada con revisor-fase, sin hallazgos Blocking/Required
- [x] Fase 4 iniciada (2026-02-08 18:35)
- [x] Fase 4 completada (2026-02-08 18:43) - Todas las correcciones aplicadas
- [x] Fase 5 iniciada (2026-02-08 18:43)
- [x] Fase 5 completada (2026-02-08 18:45)

---

## Resumen de Ejecución

**Fecha de finalización:** 2026-02-08 18:45

### Documentos Modificados

| Documento | Líneas modificadas | Cambio principal |
|-----------|-------------------|-----------------|
| `M.LCAFMi-## Comunicacion_Detallada_EAdocx.md` | 159-204 (46→15) | Declaración NO subcontratación |
| `P-PSEA-01 Protocolo General EA.md` | 49, 61 | Eliminadas referencias a subcontratación |
| `P-PSEA-09 Procedimiento de Planificacion Ronda EA.md` | 13 (literal b) | Limpieza de comentarios, declaración NO subcontratación |

### Backups Creados

| Archivo | Timestamp |
|---------|-----------|
| `backup_260208_1826_M.LCAFMi-## Comunicacion Detallada EAdocx.md` | 2026-02-08 18:26 |
| `backup_260208_1838_P-PSEA-01 Protocolo General EA.md` | 2026-02-08 18:38 |

### Archivos de Documentación

| Archivo | Tipo |
|---------|------|
| `logs/plans/260208_1826_plan_ajuste-no-subcontratacion-comunicacion-detallada.md` | Plan de corrección |
| `logs/history/260208_1837_findings.md` | Hallazgos y lecciones aprendidas |

### Cumplimiento ISO/IEC 17043:2023

| Cláusula | Requisito | Estado |
|----------|-----------|--------|
| 6.4 Subcontratación | Declarar situación | ✅ CUMPLE (NO subcontratación) |
| 6.4.1 Informar a participantes | Transparencia | ✅ CUMPLE (declaración disponible) |

---

## Hallazgos Revisor-Fase Fase 4

**Primera Revisión (2026-02-08 18:35):**
- Required: Inconsistencia P-PSEA-01 vs P-PSEA-09 (nota de subcontratación)
- Required: Comentarios internos en P-PSEA-09

**Segunda Revisión (2026-02-08 18:40):**
- Required: Referencia a "servicios externos" en sección de comunicación de P-PSEA-01

**Correcciones aplicadas:**
- ✅ P-PSEA-01 (línea 49): Eliminada nota que permitía subcontratación
- ✅ P-PSEA-01 (línea 61): Eliminada mención de "servicios externos" en comunicación
- ✅ P-PSEA-09: Eliminados comentarios embebidos ("--- comentario:", "[...]")

---

## Hallazgos Revisor-Fase Fase 1

**Revisado:** 2026-02-08 18:29

**Resultados:**
- ✅ Backup creado correctamente en `docs/docs_sgc/backup_260208_1826_M.LCAFMi-## Comunicacion Detallada EAdocx.md`
- ✅ Rango 159-204 (46 líneas) incluye sección 8.1 y subsecciones 8.1.1-8.1.4
- ℹ️ Nota: Línea 204 es una línea en blanco antes de la sección 9; mantener al reemplazar para preservar espaciado visual

---

## Texto Preparado para Sección 8.1 (Fase 2)

```markdown
**8.1. Subcontratación de Actividades**

El Laboratorio CALAIRE como proveedor del Ensayo de Aptitud declara que **todas las actividades** del programa de EA se realizan internamente por personal propio del Laboratorio, de conformidad con la norma ISO/IEC 17043:2023 (cláusula 6.4).

**No se utilizan servicios de subcontratistas** para ninguna de las actividades del programa de EA, incluyendo:

- Diseño y planificación del programa de EA
- Preparación, caracterización y homogeneidad del ítem de ensayo
- Ensayos de homogeneidad y estabilidad
- Evaluación del rendimiento de los participantes
- Elaboración y autorización de informes

El personal técnico del Laboratorio CALAIRE involucrado en cada actividad cuenta con la competencia técnica documentada y las autorizaciones formales correspondientes, conforme a los perfiles de cargo establecidos en el Sistema de Gestión de Calidad.

Esta declaración cumple con el requisito de transparencia de la norma ISO/IEC 17043:2023 (cláusula 6.4.1) respecto a la comunicación del esquema de gestión de actividades a los participantes del EA.
```
