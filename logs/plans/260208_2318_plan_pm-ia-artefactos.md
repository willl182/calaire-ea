# Plan: Implementación de Artefactos PMI con Estrategia AI-Driven

**Created**: 2026-02-08 23:18
**Updated**: 2026-02-08 23:55
**Status**: draft
**Slug**: pm-ia-artefactos

---

## Objetivo

Transformar la información dispersa del grafo CALAIRE-EA en 10 artefactos formales de gestión de proyectos alineados con PMI/PMBOK, implementando una estrategia IA-Driven que aprovecha OpenCode, Linux y AppSheet para automatizar el flujo de trabajo.

---

## Estrategia AI-Driven PM

### Flujo de Trabajo Propuesto

1. **Captura (Logseq):** Registro diario, notas de reuniones, ideas rápidas
2. **Procesamiento (OpenCode/Linux):** El agente estructura la información, genera documentos formales (Charter, Informes) y escribe/testea código R
3. **Control (AppSheet):** Gestión estructurada de Riesgos, Issues y datos de campo (sincronizado vía CSV/Drive)
4. **Publicación (Pandoc):** Conversión final a formatos entregables oficiales (PDF/Docx)

### Integraciones Técnicas

| Tecnología | Uso Principal |
|------------|----------------|
| **OpenCode** | Agente de Documentación: lee grafo, genera artefactos, tests R, documenta código |
| **Pandoc** | Conversión Markdown → PDF/Docx con plantilla institucional |
| **AppSheet** | Bitácora de campo, control de hallazgos QMS, gestión móvil de riesgos |
| **Git Hooks** | Pre-commit para auditoría de código R/Shiny |
| **CSV Bridge** | Sincronización Logseq ↔ AppSheet |

---

## Inventario de Información Existente

| Artefacto PMI | Cobertura Actual | Archivos Fuente |
|---------------|------------------|-----------------|
| Project Charter | 70% | `docs/proyecto.md`, `pages/CALAIRE-EA.md`, `pages/Equipo.md` |
| Registro de Interesados | 80% | `pages/Laboratorios.md`, páginas individuales de labs |
| EDT/WBS | 60% | `pages/CALAIRE-EA.md`, inventario SGC |
| Diccionario EDT | 20% | Disperso en MOCs |
| Cronograma | 75% | `docs/gantt.md`, `docs/timeline.md`, `pages/Prueba Piloto.md` |
| Presupuesto | 10% | Solo total ($437M) - **Fuera de alcance técnico** |
| Registro de Riesgos | 40% | `docs/proyecto.md`, `logs/fase1_matriz_requisitos_normativos.md` |
| Plan de Gestión de Calidad | 50% | `docs/docs_sgc/Roadmap de Implementación por Oleadas.md` |
| Registro de Incidentes | 0% | No existe |
| Registro de Lecciones Aprendidas | 30% | Disperso en journals |

---

## Estructura Propuesta

```
docs/instrucciones/                       # Guías y artefactos PMI
├── README.md                           # Índice MOC de artefactos PM (NUEVO)
├── 01_Project_Charter.md               # Acta de Constitución (NUEVO)
├── 02_Registro_Interesados.md          # Stakeholder Register (NUEVO)
├── 03_EDT_WBS.md                       # Estructura de Desglose (Mermaid) (NUEVO)
├── 04_Diccionario_EDT.md               # WBS Dictionary (NUEVO)
├── 05_Cronograma.md                    # Gantt integrado con dependencias (CONSOLIDAR existente)
├── 06_Presupuesto.md                   # Línea base de costos (placeholder) (NUEVO)
├── 07_Registro_Riesgos.md              # Risk Register (NUEVO)
├── 08_Plan_Gestion_Calidad.md          # Quality Management Plan (NUEVO)
├── 09_Registro_Incidentes.md           # Issue Log (NUEVO)
└── 10_Lecciones_Aprendidas.md          # Lessons Learned Register (NUEVO)

# Guías existentes en docs/instrucciones/:
- guide_pm_charter.md                    # Guía detallada para Project Charter
- guide_pm_wbs.md                      # Guía detallada para EDT/WBS
- pm_ai_plan.md                         # Estrategia IA-Driven PM
- pm_guia_lista.md                     # Guía para elaborar artefactos
- pm_lista.md                           # Lista de documentos prioritarios
- pm_roadmap.md                        # Análisis de brechas
- instrucciones_informe_rmd.md           # Guía informes
- compliance_*.md                       # Compliance documentos
- informes-calaire_vs-jrc_uba.md        # Referencias

docs/auxiliares/                         # Archivos operativos y CSV
├── gantt.md                            # Diagrama Gantt existente (Mermaid)
├── timeline.md                          # Timeline existente (Mermaid)
├── tareas_calaire.csv                   # Tareas (fuente AppSheet)
├── tags_project.csv                     # Clasificación correos
├── planificacion_ronda.csv              # Planificación rondas
├── doc_calendario_2026.md             # Calendario 2026
├── memoria_2025.md                     # Memoria 2025
└── gmail_project_v3.csv                # CSV Gmail

scripts/pm/                             # Automatización IA-Driven (NUEVO)
├── export_project_charter.sh           # Pandoc: Markdown → Docx
├── extract_deadlines.py                # Extrae DEADLINE del grafo
├── sync_appsheet.sh                    # Sincroniza docs/auxiliares/ ↔ AppSheet
└── pre_commit_audit_r.sh              # Git hook: auditoría código R
```

---

## Fases

### Fase 1: Infraestructura y Prioridad Inmediata
**Objetivo:** Dar "nacimiento formal" al proyecto con documentos de autoridad y alineación estratégica.

**Guías existentes:** `docs/instrucciones/guide_pm_charter.md` (guía detallada para Project Charter)

| # | Archivo | Acción | Fuentes | Esfuerzo Est. |
|---|---------|--------|---------|---------------|
| 1.1 | `docs/instrucciones/README.md` | Crear | Plantilla MOC + índice guías existentes | 20 min |
| 1.2 | `docs/instrucciones/01_Project_Charter.md` | Crear | `guide_pm_charter.md`, `docs/proyecto.md`, `pages/CALAIRE-EA.md`, `pages/Equipo.md` | 45 min |
| 1.3 | `scripts/pm/export_project_charter.sh` | Crear | Plantilla Pandoc | 20 min |
| 1.4 | `docs/instrucciones/02_Registro_Interesados.md` | Crear | `guide_pm_charter.md`, `pages/Laboratorios.md`, páginas de labs, `pages/Equipo.md` | 30 min |

**Entregables:**
- Project Charter con objetivo, alcance, autoridad, hitos, riesgos estratégicos (basado en `guide_pm_charter.md`)
- Matriz de interesados con poder/interés/influencia
- Script Pandoc para conversión a Docx con plantilla INM/UNAL
- README con índice navegable de guías y artefactos en `docs/instrucciones/`

---

### Fase 2: Líneas Base de Planificación
**Objetivo:** Establecer contra qué se medirá el éxito (Alcance, Tiempo, Costo).

**Guías existentes:** `docs/instrucciones/guide_pm_wbs.md` (guía detallada para EDT/WBS)

| # | Archivo | Acción | Fuentes | Esfuerzo Est. |
|---|---------|--------|---------|---------------|
| 2.1 | `docs/instrucciones/03_EDT_WBS.md` | Crear | `guide_pm_wbs.md`, `pages/CALAIRE-EA.md`, `docs/docs_sgc/Inventario Documental del SGC.md` | 60 min |
| 2.2 | `docs/instrucciones/04_Diccionario_EDT.md` | Crear | EDT, `guide_pm_wbs.md`, `pages/CALAIRE-APP.md`, criterios de entregables | 45 min |
| 2.3 | `docs/instrucciones/05_Cronograma.md` | Crear/Consolidar | `docs/auxiliares/gantt.md`, `docs/auxiliares/timeline.md`, `pages/Prueba Piloto.md` | 45 min |
| 2.4 | `scripts/pm/extract_deadlines.py` | Crear | Plantilla extractor de DEADLINE/SCHEDULED | 30 min |
| 2.5 | `docs/auxiliares/tareas_projecto.csv` | Crear/Consolidar | `tareas_calaire.csv` existente + output script extractor | 15 min |
| 2.6 | `docs/instrucciones/06_Presupuesto.md` | Crear | `docs/proyecto.md` (total $437M) | 15 min |

**Entregables:**
- EDT gráfica en Mermaid (3 niveles: Proyecto > Fases > Entregables) basada en `guide_pm_wbs.md`
- Diccionario con criterios de aceptación para entregables complejos
- Cronograma integrado con dependencias y ruta crítica (consolidando `gantt.md` y `timeline.md` existentes)
- Script Python que extrae DEADLINE/SCHEDULED del grafo
- CSV de tareas consolidado en `docs/auxiliares/` como fuente de datos para AppSheet
- Presupuesto con placeholder para área de costeo

---

### Fase 3: Gestión de Riesgos y Calidad
**Objetivo:** Proteger el proyecto de incertidumbres y asegurar conformidad normativa.

| # | Archivo | Acción | Fuentes | Esfuerzo Est. |
|---|---------|--------|---------|---------------|
| 3.1 | `docs/instrucciones/07_Registro_Riesgos.md` | Crear | `pm_guia_lista.md`, `docs/proyecto.md`, `logs/fase1_matriz_requisitos_normativos.md` | 45 min |
| 3.2 | `docs/auxiliares/riesgos_identificados.csv` | Crear | Registro de Riesgos (puente AppSheet) | 20 min |
| 3.3 | `docs/instrucciones/08_Plan_Gestion_Calidad.md` | Crear | `docs/docs_sgc/Roadmap de Implementación por Oleadas.md`, `pm_guia_lista.md` | 30 min |

**Entregables:**
- Registro de Riesgos formal (ID, Causa>Riesgo>Efecto, P×I, Dueño, Estrategia)
- CSV de riesgos en `docs/auxiliares/` para vista "Semáforo" en AppSheet
- Plan de Gestión de Calidad (cómo se crean/revisan/aprueban los 30+ procedimientos)

---

### Fase 4: Monitoreo y Control
**Objetivo:** Herramientas vivas para seguimiento diario de la Prueba Piloto.

| # | Archivo | Acción | Fuentes | Esfuerzo Est. |
|---|---------|--------|---------|---------------|
| 4.1 | `docs/instrucciones/09_Registro_Incidentes.md` | Crear | Plantilla + incidentes cerrados (CALAIRE-APP, subcontratación) | 20 min |
| 4.2 | `docs/auxiliares/incidentes_qms.csv` | Crear | Registro de Incidentes (puente AppSheet) | 15 min |
| 4.3 | `docs/instrucciones/10_Lecciones_Aprendidas.md` | Crear | `docs/proyecto.md` (Aprendizajes Clave), journals con #decision | 30 min |

**Entregables:**
- Issue Log con estructura para nuevos problemas operativos
- CSV de incidentes en `docs/auxiliares/` para Tablero de Control de Hallazgos QMS en AppSheet
- Lessons Learned Register con aprendizajes formalizados

---

### Fase 5: Integración con Logseq
**Objetivo:** Vincular artefactos PM con el grafo de conocimiento.

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 5.1 | `pages/CALAIRE-EA.md` | Modificar | Añadir sección "Artefactos de Gestión" con enlaces a `docs/instrucciones/` |
| 5.2 | `pages/Prueba Piloto.md` | Modificar | Añadir enlaces a Cronograma y Registro de Riesgos |
| 5.3 | Crear página MOC `[[Gestión del Proyecto]]` | Crear | MOC central que aglutina todos los artefactos PMI en `docs/instrucciones/` |

---

### Fase 6: Infraestructura AppSheet y Sincronización
**Objetivo:** Configurar puente entre Logseq (local) y AppSheet (móvil).

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 6.1 | `scripts/pm/sync_appsheet.sh` | Crear | Script de sincronización `docs/auxiliares/` ↔ Google Drive/Dropbox |
| 6.2 | `docs/auxiliares/visitas_campo.csv` | Crear | Plantilla CSV para "Bitácora de Campo Digital" (visitas a laboratorios) |
| 6.3 | Documentación AppSheet | Crear | `docs/instrucciones/Guia_AppSheet.md` con configuración de vistas: Calendario/Gantt, Semáforo de Riesgos, Tablero Hallazgos |

**Entregables:**
- Script automatizado que sincroniza `docs/auxiliares/` con repositorio en la nube
- Plantilla de bitácora de campo para visitas piloto (UdeM, SIATA, UPB)
- Guía de configuración AppSheet con 3 vistas principales:
  - **Calendario/Gantt:** Tareas del proyecto (fuente: `tareas_calaire.csv` en `docs/auxiliares/`)
  - **Semáforo de Riesgos:** Clasificación P×I móvil (fuente: `riesgos_identificados.csv` en `docs/auxiliares/`)
  - **Tablero Hallazgos QMS:** Gestión de no conformidades (fuente: `incidentes_qms.csv` en `docs/auxiliares/`)

---

### Fase 7: Automatización para CALAIRE-APP (R/Shiny) ⚠️ CONDICIONAL
**Objetivo:** Implementar pruebas automáticas y auditoría de código para validación ISO 13528.

**Requisito previo:** Repositorio de CALAIRE-APP migrado a GitHub (ver `pages/CALAIRE-APP.md` TODO: "Migrar repositorio a GitHub del grupo")

**Nota técnica:** CALAIRE-APP está desarrollado en **R (Shiny + paquete ptcalc)**. Esta fase se alinea con el stack real del proyecto.

| # | Archivo | Acción | Fuentes | Esfuerzo Est. | Estado |
|---|---------|--------|---------|---------------|---------|
| 7.1 | `tests/testthat/test-algoritmo_a.R` | Crear | `ptcalc/R/pt_robust_stats.R`, Anexo C ISO 13528 | 60 min | Pendiente (requiere acceso código) |
| 7.2 | `scripts/pm/add_roxygen2.sh` | Crear | Plantilla para docstrings Roxygen2 | 20 min | Pendiente (requiere acceso código) |
| 7.3 | `scripts/pm/pre_commit_audit_r.sh` | Crear | Plantilla Git hook para auditoría de código R | 30 min | Pendiente (requiere acceso código) |
| 7.4 | `.git/hooks/pre-commit` | Crear | Enlace simbólico al script de auditoría | 5 min | Pendiente (requiere acceso código) |
| 7.5 | `scripts/pm/add_type_hints.sh` | Crear | Plantilla para type hints (opcional, no estándar en R) | 15 min | Pendiente (requiere acceso código) |
| 7.6 | `tests/testthat/test-homogeneity.R` | Crear | `ptcalc/R/pt_homogeneity.R`, datos ISO 13528 | 30 min | Pendiente (requiere acceso código) |
| 7.7 | `tests/testthat/test-scores.R` | Crear | `ptcalc/R/pt_scores.R`, fórmulas puntajes | 30 min | Pendiente (requiere acceso código) |

**Entregables (condicionales):**
- Test unitario para Algoritmo A usando **testthat** (validación contra datos Anexo C ISO 13528)
- Test unitario para funciones de homogeneidad (ANOVA, componentes de varianza)
- Test unitario para funciones de puntajes (z, z', zeta, En)
- Script para agregar comentarios Roxygen2 (título, parámetros, return, ejemplos, @references)
- Git hook pre-commit que verifica:
  - Falta de documentación (Roxygen2)
  - Violaciones de estilo (lintr)
  - Posibles errores en fórmulas estadísticas críticas
- Comandos de ejecución:
  - `devtools::test()`
  - `lintr::lint_package()`
  - `devtools::document("ptcalc")`
- Type hints opcionales (estándar no común en R, pero útil para R6 classes)

**Librerías R sugeridas:**
- `testthat`: Framework de testing (estándar R packages)
- `testthat::snapshot_*`: Snapshot testing para reportes
- `lintr`: Linting de código
- `devtools`: Desarrollo de paquetes
- `roxygen2`: Documentación automática

---

## Log de Ejecución

- [ ] Fase 1 iniciada
- [ ] Fase 1 completada
- [ ] Fase 2 iniciada
- [ ] Fase 2 completada
- [ ] Fase 3 iniciada
- [ ] Fase 3 completada
- [ ] Fase 4 iniciada
- [ ] Fase 4 completada
- [ ] Fase 5 iniciada
- [ ] Fase 5 completada
- [ ] Fase 6 iniciada
- [ ] Fase 6 completada
- [ ] Fase 7 iniciada
- [ ] Fase 7 completada

---

## Estimación Total

| Fase | Artefactos | Scripts/AppSheet | Esfuerzo Estimado | Estado |
|------|------------|------------------|-------------------|---------|
| Fase 1 | 3 | 1 | ~1.75 horas | Pendiente |
| Fase 2 | 6 | 1 | ~3.25 horas | Pendiente |
| Fase 3 | 3 | 1 | ~1.5 horas | Pendiente |
| Fase 4 | 3 | 1 | ~1.1 horas | Pendiente |
| Fase 5 | 3 | 0 | ~30 min | Pendiente |
| Fase 6 | 3 | 1 | ~2 horas | Pendiente |
| Fase 7 | 7 | 0 | ~3 horas | ⚠️ CONDICIONAL (requiere migración GitHub) |
| **Total** | **28** | **5** | **~13 horas** | |

**Notas sobre Fase 7:**
- No se incluye en el tiempo total de ejecución inmediata
- Se ejecutará como fase adicional cuando se complete la migración del repositorio CALAIRE-APP a GitHub
- Stack tecnológico: **R (Shiny + paquete ptcalc)**
- Esfuerzo total sin Fase 7: **~10 horas** (Fases 1-6)

---

## Dependencias

```
Fase 1 ──► Fase 2 ──► Fase 3 ──► Fase 4 ──► Fase 5 ──► Fase 6 ──► Fase 7
           │                                                    │
           └──► EDT es prerequisito para Diccionario EDT      └──► Tests requieren código R existente
           └──► EDT es prerequisito para Cronograma
           └──► Cronograma es prerequisito para CSV AppSheet
```

**Integraciones cruzadas:**

```
Logseq (Journals/Pages)
    ↓ OpenCode (minería)
CSV Bridge (data/)
    ↓ Sincronización
AppSheet (Móvil)
    ↑ Documentación
docs/pm/ (Artefactos formales)
```

---

## Notas Especiales

### Ubicación de Documentos
- **Artefactos PMI:** `docs/instrucciones/` - Guías y documentos de gestión de proyectos
- **Archivos CSV:** `docs/auxiliares/` - Datos operativos, calendarios y archivos CSV
- **Guías Existentes:**
  - `guide_pm_charter.md` - Guía detallada para Project Charter
  - `guide_pm_wbs.md` - Guía detallada para EDT/WBS
  - `pm_ai_plan.md` - Estrategia IA-Driven PM
  - `pm_guia_lista.md` - Guía para elaborar artefactos
  - `pm_lista.md` - Lista de documentos prioritarios
  - `pm_roadmap.md` - Análisis de brechas
  - `instrucciones_informe_rmd.md` - Guía informes

### Presupuesto
- El artefacto `06_Presupuesto.md` se creará como **placeholder** que indique que la gestión financiera está a cargo del área de costeo
- No se incluye en el análisis de variación automatizada (fuera del alcance técnico)

### AppSheet
- Se asume acceso a Google Drive o Dropbox para sincronización de `docs/auxiliares/`
- La configuración de la App en AppSheet está fuera del alcance de OpenCode (requiere interfaz web)
- Se documentará la estructura de CSV y configuración de vistas en `docs/instrucciones/Guia_AppSheet.md`

### CALAIRE-APP
- Fase 7 requiere que el código R/Shiny exista en repositorio
- Tests unitarios usan librería `testthat` (estándar R)
- Documentación usa formato `Roxygen2` (estándar R packages)

---

## Referencias

### Guías y Documentación PMI (docs/instrucciones/)
- `guide_pm_charter.md` - Guía detallada Project Charter
- `guide_pm_wbs.md` - Guía detallada EDT/WBS
- `pm_ai_plan.md` - Estrategia IA-Driven PM
- `pm_guia_lista.md` - Guía para elaborar artefactos
- `pm_lista.md` - Lista de documentos prioritarios
- `pm_roadmap.md` - Análisis de brechas
- `instrucciones_informe_rmd.md` - Guía informes

### Archivos Operativos (docs/auxiliares/)
- `gantt.md` - Diagrama Gantt existente
- `timeline.md` - Timeline existente
- `tareas_calaire.csv` - Tareas (fuente para AppSheet)
- `tags_project.csv` - Clasificación correos
- `planificacion_ronda.csv` - Planificación rondas

### Documentación del Proyecto
- `docs/proyecto.md` - Plan detallado
- `pages/CALAIRE-EA.md` - MOC principal
- `docs/docs_sgc/` - Documentos SGC
- AGENTS.md - Guía para agentes AI
