# Session State: CALAIRE-EA Knowledge Graph

**Last Updated**: 2026-02-09 00:05

## Session Objective

Planificar la implementación del sistema de gestión de proyectos PMI con estrategia AI-Driven para CALAIRE-EA, corrigiendo el stack tecnológico de CALAIRE-APP (R/Shiny, no Python) y actualizando la estructura de directorios para ubicaciones correctas (`docs/pm/` para artefactos PMI).

## Current State

- [x] Exploración del grafo para identificar información existente para artefactos PMI
- [x] Revisión de documentación de PMI (pm_roadmap.md, pm_lista.md, pm_guia_lista.md)
- [x] Lectura de docs/pm_ai_plan.md para integrar estrategia AI-Driven
- [x] Verificación del stack tecnológico de CALAIRE-APP (R/Shiny confirmado en MANUAL_COMPLETO_PT_APP.md)
- [x] Descubrimiento de estructura correcta de carpetas:
  - **docs/instrucciones/**: Guías PMI (guide_pm_charter.md, guide_pm_wbs.md, pm_*.md)
  - **docs/auxiliares/**: Archivos operativos CSV (tareas_calaire.csv, tags_project.csv, gantt.md, timeline.md)
- [x] Creación del plan de implementación en logs/plans/260208_2318_plan_pm-ia-artefactos.md
- [x] Corrección de referencias incorrectas a Python en archivos:
  - pages/CALAIRE-APP.md
  - docs/pm_guia_lista.md
  - docs/proyecto.md
  - journals/2026_01_30.md
  - logs/plans/260208_2318_plan_pm-ia-artefactos.md
- [x] Actualización del plan para reflejar rutas correctas:
  - `docs/pm/` → `docs/instrucciones/`
  - `data/` → `docs/auxiliares/`
  - Incorporación de guías existentes (guide_pm_charter.md, guide_pm_wbs.md)
- [x] Corrección final de estructura:
  - Artefactos PMI → `docs/pm/` (NUEVA carpeta)
  - Guías PMI → `docs/instrucciones/` (carpeta existente)
  - Archivos CSV → `docs/auxiliares/` (carpeta existente)
  - MOC [[Gestión del Proyecto]] añadido
- [x] Actualización de AGENTS.md con estructura final correcta
- [ ] Ejecución del plan (Fases 1-7 pendientes)
- [ ] Git commit
- [ ] Git push

## Critical Technical Context

**Estructura Final Correcta:**

```
docs/
├── pm/                    # Artefactos PMI (NUEVA carpeta)
│   ├── 01_Project_Charter.md
│   ├── 02_Registro_Interesados.md
│   ├── 03_EDT_WBS.md
│   ├── 04_Diccionario_EDT.md
│   ├── 05_Cronograma.md
│   ├── 06_Presupuesto.md
│   ├── 07_Registro_Riesgos.md
│   ├── 08_Plan_Gestion_Calidad.md
│   ├── 09_Registro_Incidentes.md
│   └── 10_Lecciones_Aprendidas.md
├── instrucciones/         # Guías PMI (carpeta existente)
│   ├── guide_pm_charter.md
│   ├── guide_pm_wbs.md
│   ├── pm_ai_plan.md
│   ├── pm_guia_lista.md
│   └── pm_lista.md
└── auxiliares/           # Archivos operativos CSV (carpeta existente)
    ├── gantt.md
    ├── timeline.md
    ├── tareas_calaire.csv
    ├── tags_project.csv
    └── planificacion_ronda.csv
```

**Stack Tecnológico CALAIRE-APP:**
- R 4.1.0+ y Shiny (NO Python)
- Paquete `ptcalc` para cálculos ISO 13528:2022
- Librerías de desarrollo: testthat, roxygen2, lintr, devtools
- Repositorio pendiente de migración a GitHub

**Fase 7 del Plan es CONDICIONAL:**
- Requiere migración del repositorio CALAIRE-APP a GitHub
- No se incluye en el tiempo total de ejecución inmediata (~10 horas para Fases 1-6)
- Stack: R/Shiny (testthat para pruebas unitarias, Roxygen2 para documentación)

**Reglas de Navegación para AGENTS.md:**
- Artefactos PMI → `docs/pm/`
- Guías PMI → `docs/instrucciones/`
- Archivos CSV → `docs/auxiliares/`
- Referenciar guías existentes antes de crear artefactos
- Consolidar gantt.md + timeline.md existentes en `docs/auxiliares/`

## Next Steps

1. **Git commit**: Commit cambios con mensaje "AGENTS.md: Actualizar estructura PMI - docs/pm, docs/instrucciones, docs/auxiliares"
2. **Git push**: Push commits a repositorio remoto
3. **Revisión de plan**: Usuario debe aprobar plan en `logs/plans/260208_2318_plan_pm-ia-artefactos.md`
4. **Ejecución Fase 1**: Crear infraestructura en `docs/pm/` (README, Project Charter, Registro Interesados)
5. **Revisión fase por revisor-fase**: Validar cada fase antes de continuar

**Archivos clave creados/actualizados:**
- `logs/plans/260208_2318_plan_pm-ia-artefactos.md` - Plan completo de implementación PMI
- `AGENTS.md` - Actualizado con estructura correcta
- `logs/history/260208_2355_findings.md` - Hallazgos técnicos
- `logs/history/260208_2341_findings.md` - Hallazgos sobre estructura de carpetas

**Archivos corregidos:**
- `pages/CALAIRE-APP.md` - Stack tecnológico actualizado
- `docs/pm_guia_lista.md` - EDT ajustada
- `docs/proyecto.md` - Tecnología actualizada
- `journals/2026_01_30.md` - Contexto corregido

## Sesiones Anteriores

**Sesión de 2026-02-08 23:38 - Sistema de Gestión Documental ISO 17025/17043/13528:**
- Fases 1-4 del plan SGC completadas
- Fase 5 (Ejecutar Ajustes por Oleadas) pendiente de correcciones de revisor-fase
- Plan activo: logs/plans/260208_1932_plan_ajuste-sgc-17025-17043-13528.md

**Referencias:**
- `docs/pm_roadmap.md` - Análisis de brechas en artefactos PMI
- `docs/pm_lista.md` - Lista de documentos a elaborar
- `docs/pm_guia_lista.md` - Guía para elaboración de artefactos
- `docs/pm_ai_plan.md` - Estrategia IA-Driven PM
- `docs/docs_sgc/MANUAL_COMPLETO_PT_APP.md` - Documentación técnica CALAIRE-APP (R/Shiny)
