# Session State: CALAIRE-EA Knowledge Graph

**Last Updated**: 2026-02-08 21:38

## Session Objective

Implementar Fase 4 del plan de ajuste del Sistema de Gestión Documental ISO 17025/17043/13528 para el proyecto CALAIRE-EA (Ensayos de Aptitud para Gases Contaminantes Criterio en Colombia).

## Current State

- [x] Fase 1: Matriz Maestra de Cumplimiento Normativo completada (2026-02-08)
- [x] Fase 2: Inventario Documental del SGC completado (2026-02-08)
- [x] Fase 3: Árbol Maestro PSEA y Diccionario de Documentos SGC completados (2026-02-08)
- [x] Fase 4: Backlog Priorizado y Roadmap de Implementación completados (2026-02-08)
- [ ] Fase 5: Ejecutar Ajustes por Oleadas (pendiente correcciones de revisor-fase)
- [ ] Fase 6: Verificar Conformidad y Cierre

### Fase 4 Completada

**Entregables creados:**

1. **Backlog Priorizado de Documentos SGC** (`docs/docs_sgc/Backlog Priorizado de Documentos SGC.md`)
   - 37 documentos priorizados en 4 niveles (P1-P4)
   - 52 horas de esfuerzo para Oleada 1 (10 documentos P1)
   - 44 horas para Oleada 2 (10 documentos P2)
   - 34 horas para Oleada 3 (10 documentos P3)
   - 17 horas para Oleada 4 (7 documentos P4)
   - Total: 147 horas en 6-8 semanas

2. **Roadmap de Implementación por Oleadas** (`docs/docs_sgc/Roadmap de Implementación por Oleadas.md`)
   - 4 oleadas con cronograma semanal detallado
   - Hitos de calidad al final de cada oleada
   - Diagrama Gantt en Mermaid para visualización
   - Recursos asignados por responsable

**Hallazgos pendientes de corrección (Revisor-fase - Revisión 3):**

1. **[Blocking] Déficit de documentos:** Objetivo de 41 vs 37 planificados (4 faltantes)
2. **[Required] Colisión de códigos de formatos:** F-PSEA-01 al F-PSEA-04 duplicados en P3 y P4
3. **[Required] Dependencias cruzadas:** P-PSEA-18 depende de P-PSEA-15 (Oleada 2), P-PSEA-23 depende de P-PSEA-13 (Oleada 3), P-PSEA-09 depende de P-PSEA-06 pero cronograma lo invierte
4. **[Required] Documentos no planificados en "Recursos Asignados":** P-PSEA-32, P-PSEA-33, P-PSEA-35, P-PSEA-36, P-PSEA-37, P3-F01 al P3-F07
5. **[Required] Resúmenes inflados por colisión de códigos**
6. **[Suggestions] Criterios de aceptación vagos:** Sin evidencia verificable específica
7. **[Suggestions] Cronograma sin buffers ni revisión intermedia**

## Critical Technical Context

**Estructura del SGC CALAIRE-EA:**

- **DG (Documento General):** Nivel 1 - Políticas, manuales (ej: DG-PSEA-01)
- **P (Procedimiento):** Nivel 2 - Qué, quién, cuándo, evidencia (ej: P-PSEA-01 al P-PSEA-30)
- **I (Instructivo):** Nivel 3 - Cómo se ejecuta (eliminados en Fase 3, contenido absorbido por procedimientos)
- **F (Formato):** Nivel 4 - Registro/evidencia (ej: F-PSEA-01 al F-PSEA-04)

**Jerarquía Normativa:**

```
ISO/IEC 17025:2017 (Macro - Sistema de gestión de competencia)
    └── ISO/IEC 17043:2023 (Operativo - Requisitos específicos para PT)
            └── ISO 13528:2022 (Metodológico - Métodos estadísticos)
```

**Brechas críticas identificadas:**

- ISO 17043 cap. 7: Diseño estadístico, valor asignado, homogeneidad/estabilidad, evaluación de desempeño
- ISO 17043 cap. 8: Gestión de datos, no conformidades, quejas/apelaciones, mejora continua
- ISO 13528 cap. 5-9: Métodos estadísticos específicos para PT

**Procedimientos específicos por gas:**

- P-PSEA-02: NO-NO2
- P-PSEA-03: CO
- P-PSEA-04: O3
- P-PSEA-05: SO2

**Procedimientos nuevos creados (Fase 3):**

- P-PSEA-06: Diseño Estadístico (v0)
- P-PSEA-07: Informe Resultados (v0)
- P-PSEA-08: Colusión Falsificación (v0)
- P-PSEA-09: Planificación Ronda EA (expansión)

**Formatos creados (Fase 3):**

- F-PSEA-01: Calendario Tipo (v0)
- F-PSEA-02: Cronograma Detallado (v0)
- F-PSEA-03: Registro Planificación Ronda EA
- F-PSEA-04: Formato Informe Resultados (v0)

## Next Steps

1. **Correcciones pendientes de Revisión 3 (Fase 4):**
   - Alinear el alcance con el objetivo de 41 documentos o ajustar objetivo
   - Normalizar códigos de formatos (F-PSEA-01 al F-PSEA-04)
   - Corregir dependencias inter-oleadas (P-PSEA-18, P-PSEA-23, P-PSEA-09)
   - Ajustar cronograma y Gantt para respetar dependencias
   - Depurar "Recursos Asignados" en Roadmap
   - Añadir evidencia verificable en criterios de aceptación
   - Revisar resúmenes de esfuerzo/cantidad

2. **Fase 5 - Ejecutar Ajustes por Oleadas:**
   - Iniciar Oleada 1 con 10 documentos P1 (52 horas)
   - Revisar fase con revisor-fase después de cada oleada
   - Actualizar plan con hallazgos
   - Commit y push después de cada oleada

3. **Fase 6 - Verificar Conformidad y Cierre:**
   - Validar que todos los requisitos normativos tienen documento asignado
   - Crear reporte de conformidad por norma
   - Crear matriz de trazabilidad final
   - Crear plan de mantenimiento del SGC

**Archivos clave creados en esta sesión:**

- `docs/docs_sgc/Matriz Maestra de Cumplimiento Normativo.md`
- `docs/docs_sgc/Inventario Documental del SGC.md`
- `docs/docs_sgc/Árbol Maestro PSEA.md`
- `docs/docs_sgc/Diccionario de Documentos SGC.md`
- `docs/docs_sgc/Backlog Priorizado de Documentos SGC.md`
- `docs/docs_sgc/Roadmap de Implementación por Oleadas.md`
- `logs/plans/260208_1932_plan_ajuste-sgc-17025-17043-13528.md`

**Plan activo:**
`logs/plans/260208_1932_plan_ajuste-sgc-17025-17043-13528.md`

**Estado del plan:** in_progress (Fases 1-4 completadas, Fase 5 pendiente correcciones)

## Sesiones Anteriores

**Sesión de 2026-02-08 20:32 - Sistema de Seguimiento de Tareas y Análisis de Tags:**

- Completado sistema de seguimiento de tareas (Python + CSV + Google Apps Script)
- Análisis de tags del grafo detectó 12 tags con sintaxis errónea
- Plan de corrección de tags pendiente aprobación

**Referencias:**
- `tools/export_tareas.py` - Script de exportación de tareas
- `tareas_calaire.csv` - CSV con 28 tareas
- `tools/alertas_tareas.gs` - Apps Script para alertas automáticas
- `tools/README_SEGUIMIENTO.md` - Documentación completa
- `logs/plans/260208_2029_plan_correccion-sintaxis-tags.md` - Plan de corrección de tags
