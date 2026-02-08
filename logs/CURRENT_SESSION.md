# Session State: CALAIRE-EA Ajuste de Protocolo P-PSEA-01

**Last Updated**: 2026-02-08 18:22

## Session Objective

Planificar y preparar la actualización del Protocolo General de Ensayo de Aptitud (P-PSEA-01) para cerrar brechas identificadas frente a ISO/IEC 17043:2023 e ISO 13528:2022.

## Current State

- [x] Fase 1 completada: Categorización de 5 brechas (3 Blocking, 1 Required, 1 Suggestions)
- [x] Fase 2 completada: Análisis de estructura actual de P-PSEA-01
- [x] Fase 3 completada: Extracción de criterios de ISO 13528:2022
- [x] Fase 4 completada: Plan de mejora aprobado (4 nuevas secciones + 3 modificaciones)
- [x] Fase 5 completada: Implementación de cambios en P-PSEA-01
- [x] Revisión final, commit y push

## Critical Technical Context

**Documento Objetivo:**
- P-PSEA-01 Protocolo General EA (`docs/docs_sgc/P-PSEA-01 Protocolo General EA.md`)
- Formato actual: Markdown estructurado (tabla HTML convertida)

**Brechas críticas a cerrar:**

| # | Brecha | Severidad | Referencia |
|---|--------|-----------|------------|
| B1 | Algoritmos robustos no especificados | Blocking | ISO 13528 Anexo C |
| B2 | Criterios H/S cuantitativos ausentes | Blocking | ISO 13528 Anexo B |
| B3 | Criterio de decisión z vs z' no formalizado | Required | ISO 13528 §9.2.1, §9.5.1 |
| B4 | Tratamiento de grupos pequeños (n < 5) | Blocking | ISO 17043 §7.2.2.3, ISO 13528 §5.4 |
| B5 | Compatibilidad metrológica no mencionada | Suggestions | ISO 13528 §7.8 |

**Criterios normativos extraídos:**
- Homogeneidad: ss ≤ 0.3σpt (ISO 13528 B.2.2)
- z-score: z = (xi - xpt)/σpt (ISO 13528 9.4.1)
- z'-score: z' = (xi - xpt)/√(σpt² + u²(xpt)) (ISO 13528 9.5.1)
- ζ-score: ζ = (xi - xpt)/√(u²(xi) + u²(xpt)) (ISO 13528 9.6.1)
- Compatibilidad: |xdiff| > 2udiff → investigar (ISO 13528 7.8.2)

**Aplicativo CALAIRE-APP:**
- Software validado que implementa algoritmos de ISO 13528
- Manual v0.4.0 contiene fórmulas y criterios
- Debe ser vinculado formalmente en el protocolo

## Archivos del Plan

- **Plan principal:** `.opencode/plans/260208_1706_plan_ajuste-protocolo-psea-01.md`
- **Status del plan:** approved, in_progress

## Secciones a Crear en P-PSEA-01

1. **Métodos Estadísticos** - Definir Algoritmo A, MADe, nIQR
2. **Criterios de Homogeneidad y Estabilidad** - Tabla con criterios cuantitativos
3. **Contingencias Estadísticas** - Procedimiento n<5, incertidumbre alta
4. **Validación del Valor Asignado** - Compatibilidad metrológica

## Secciones a Modificar en P-PSEA-01

1. **Definiciones** - Añadir z', ζ-score, umbral de incertidumbre
2. **Procesamiento de Datos** - Vincular CALAIRE-APP validado
3. **Referencias** - Añadir ISO 13528:2022, Manual CALAIRE-APP v0.4.0

## Next Steps

1. Backup de P-PSEA-01 creado
2. Conversión de tabla HTML a markdown completada
3. Inserción de 4 nuevas secciones completada
4. Modificación de 3 secciones completada
5. Revisión con subagent `revisor-fase` completada
6. Commit y push completados

## Archivos Relevantes

- `docs/docs_sgc/P-PSEA-01 Protocolo General EA.md` - Documento a modificar
- `docs/compliance_protocolo_general.md` - Análisis de brechas original
- `docs/referencias/iso 13528_2022.md` - Fuente normativa
- `docs/referencias/iso 17043_2023.md` - Fuente normativa
