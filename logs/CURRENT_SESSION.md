# Session State: CALAIRE-EA Knowledge Graph

**Last Updated**: 2026-02-26 15:06

## Session Objective

Retomar la línea de trabajo sobre ajustes del aplicativo [[CALAIRE-APP]] considerando dos planes de hoy: un plan de corrección por fases (errores + usabilidad + validación) y un plan de implementación documental para ejecución técnica cuando se habilite el repositorio.

## Current State

- [x] Restauración de contexto (continue)
- [x] Ingesta de insumo técnico `docs/ajustes_app/Revisión aplicativo estadístico.pdf`
- [x] Consolidación del plan funcional `logs/plans/260226_1457_plan_ajustes-app-revision-2.md`
- [x] Consolidación del plan de implementación `logs/plans/260226_1457_plan_implementacion-ajustes-revision-aplicativo-estadistico.md`
- [x] Reanudación de sesión solicitada por el usuario (2026-02-26 15:06)
- [ ] Aprobación/priorización de fases por parte del usuario
- [ ] Acceso al repositorio de la app para ejecutar correcciones de Fase 1 y Fase 2

## Critical Technical Context

**Errores confirmados por César (Informe No. 2, 2026-02-23):**
- Fórmula B.10 de homogeneidad: no maneja radicando negativo (debe ser ss=0)
- MADe: calcula con datos de homogeneidad en vez de participantes
- Selección MADe/nIQR vs Algoritmo A: falta lógica para n ≥ 12

**Cálculos correctos:** nIQR ✅, Estabilidad ✅

**Recomendaciones:** separar zonas de carga, mejorar CSV, tablas claras de cálculos

**Planes activos (hoy):**
- `logs/plans/260226_1457_plan_ajustes-app-revision-2.md` (status: draft)
- `logs/plans/260226_1457_plan_implementacion-ajustes-revision-aplicativo-estadistico.md` (status: draft)

**Normativa referenciada:**
- ISO 13528:2022 (Anexo B, Secciones 9)
- ISO 17043:2023
- NTC ISO/IEC 17025:2017

## Next Steps

1. Definir priorización entre ambos planes para ejecución inmediata
2. Obtener acceso al repositorio de la app (código R/Shiny) para ejecutar Fase 1/Fase 2
3. Coordinar validación cruzada con César para cierre de Fase 3

**Archivos clave:**
- `logs/plans/260226_1457_plan_ajustes-app-revision-2.md` — Plan funcional de ajustes (draft)
- `logs/plans/260226_1457_plan_implementacion-ajustes-revision-aplicativo-estadistico.md` — Plan de implementación documental (draft)
- `docs/ajustes_app/Revisión aplicativo estadístico.pdf` — Informe No. 2 de César
- `logs/fase2_hallazgos_informe_especificos.md` — Hallazgos previos del informe EA
- `pages/CALAIRE-APP.md` — Estado de validación del aplicativo

**Sesiones anteriores:**
- Actualización de alcance por 3 contratos (2026-02-21)
- Revisión de propuesta técnica y solicitud de Luz Elena (2026-02-21)
- Fase 2 hallazgos del informe EA (2026-02-08)
