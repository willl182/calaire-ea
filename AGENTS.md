# AGENTS.md - AI Agent Guidelines for CALAIRE-EA Knowledge Graph

## Project Overview

This is a **Logseq knowledge graph** for managing the CALAIRE-EA project (Project 61134):
*Implementación de Ensayos de Aptitud para Gases Contaminantes Criterio* (Proficiency Testing
for Criterion Pollutant Gases in Colombia).

**This is NOT a software codebase.** There are no build commands, test suites, or package
managers. Content is structured markdown files consumed by Logseq.

---

## Directory Structure

```
/                       # Graph root
├── journals/           # Daily entries (YYYY_MM_DD.md format)
├── pages/              # Permanent notes, MOCs, templates
├── docs/               # External documentation, ISO standards, static references
├── ref/                # System references (Logseq guide, setup docs)
└── logseq/             # Logseq configuration
    ├── config.edn      # Graph settings, queries, macros
    └── custom.css      # Theme customizations
```

---

## Language Conventions

| Context                | Language  | Examples                                      |
|------------------------|-----------|-----------------------------------------------|
| **Content/Prose**      | Spanish   | Titles, descriptions, meeting notes           |
| **Properties/Tags**    | English   | `priority::`, `deadline::`, `type::`, `status::`|
| **Page References**    | Spanish   | `[[Prueba Piloto]]`, `[[Reunión: Tema]]`      |
| **System Tags**        | English   | `#decision`, `#MOC`, `#System`                |

---

## Content Development Guidelines

### Input Processing

The user provides quick notes, bullet points, or informal ideas in Spanish. The agent
must:

1. **Expand and develop** the content into well-structured technical prose
2. **Use domain-appropriate vocabulary** (metrology, proficiency testing, ISO standards)
3. **Add context and detail** that clarifies the technical significance
4. **Never copy user input verbatim** - always reformulate and enrich

### Tone and Style

- Technical and professional
- Third person or impersonal voice
- Avoid colloquialisms
- Include relevant links to MOCs (`[[Prueba Piloto]]`, `[[CALAIRE-EA]]`, `[[QMS]]`, `[[CALAIRE-APP]]`)
- Convert facts into milestones: what happened, why it matters, impact, next control

### Examples

| User Input | Agent Output |
|------------|--------------|
| "UdeM confirmó rondas 3 y 4" | "**Universidad de Medellín:** respuesta positiva recibida. Confirman disponibilidad para participar en [[Ronda 3]] y [[Ronda 4]] del calendario piloto (periodos 18-23 de marzo y 25-30 de marzo 2026 respectivamente)." |
| "verificando espacio al lado del lab" | "**Verificación de espacio físico:** en evaluación activa la disponibilidad del área contigua al laboratorio de gases para almacenamiento temporal de equipos y operaciones auxiliares durante las rondas de ensayo." |
| "David ajustó cartas" | "Se ejecutó la actualización técnica de cartas de invitación para laboratorios participantes. David completó la revisión y ajuste de fechas del calendario operativo, procediendo al envío formal de las comunicaciones." |

### Key Principle

**Do not copy user input verbatim.** Always reformulate and enrich with:
- Technical context relevant to CALAIRE-EA project
- Connections to project MOCs and phases
- Clear, professional Spanish prose suitable for documentation

---

## Logseq Markdown Syntax

### Block Structure
- Every line starting with `- ` is a block
- Indentation uses tabs (not spaces) for hierarchy
- Properties use `property:: value` syntax inline or below block

### Key Syntax Elements
```markdown
- Block content here
  property:: value
  another-property:: [[Page Reference]]
  collapsed:: true

- TODO Task description
  deadline:: 2026-03-15
  priority:: A
  project:: [[CALAIRE-EA]]

- [[Page Reference]] links to another page
- #tag creates inline tag
- ((block-id)) references a specific block
```

### Task Workflow
```
TODO → DOING → DONE
```
- Use `TODO`, `DOING`, `DONE` as block prefixes
- Tasks appear in journal queries automatically when tagged with `[[CALAIRE-EA]]`

---

## Templates (in pages/templates.md)

Available templates to insert via `/template` command in Logseq:

| Template Name    | Purpose                                    |
|------------------|--------------------------------------------|
| `reunion`        | Meeting notes with attendees, decisions    |
| `protocolo`      | Technical protocol for gas testing         |
| `ronda-piloto`   | Pilot round tracking per laboratory        |
| `entregable`     | Deliverable with deadline and criteria     |

### Template Properties Pattern
```markdown
- #[[Reunión]]
  type:: [[Meeting]]
  attendees:: 
  project:: [[CALAIRE-EA]]
  date:: 
```

---

## MOCs (Maps of Content) - Entry Points

| Page               | Purpose                                    |
|--------------------|--------------------------------------------|
| `[[CALAIRE-EA]]`   | Main project overview, phases, links       |
| `[[Prueba Piloto]]`| Pilot test coordination (March 2026)       |
| `[[CALAIRE-APP]]`  | Statistical software development           |
| `[[QMS]]`          | Quality management, ISO 17043/13528        |
| `[[Laboratorios]]` | Participant laboratory registry            |
| `[[Equipo]]`       | Team directory and roles                   |
| `[[Equipos]]`      | Equipment inventory and calibration assets |

---

## Editing Guidelines

### DO
- Preserve tab-based indentation exactly
- Keep properties on separate lines below their block
- Use `[[Page Name]]` for internal links
- Add `project:: [[CALAIRE-EA]]` to tasks for query visibility
- Use `collapsed:: true` for large content blocks
- Write prose in Spanish, properties in English

### DO NOT
- Use spaces for indentation (Logseq requires tabs)
- Create new pages without linking from existing MOCs
- Remove or modify `template::` declarations in templates.md
- Add files to `logseq/` directory without understanding config.edn
- Change journal filename format (must be `YYYY_MM_DD.md`)

---

## File Naming Conventions

| Directory   | Format                  | Example                    |
|-------------|-------------------------|----------------------------|
| `journals/` | `YYYY_MM_DD.md`         | `2026_01_30.md`            |
| `pages/`    | Title Case with spaces  | `Prueba Piloto.md`         |
| `docs/`     | lowercase_with_underscores | `iso 17043_2023.md`     |

---

## Journal Entry Format

Daily journal entries in `journals/` must follow this standard format consistently.

### Required Structure

```markdown
# Registro del Día
  project:: [[CALAIRE-EA]]
- ## [Nombre de Sección]
	- **[Título del Evento]:** descripción técnica detallada del evento, incluyendo contexto, impacto y próximos pasos cuando aplique. Usar tercera persona o voz impersonal.
	  date:: YYYY-MM-DD
	  category:: [[Categoría]]
	  status:: [status_value]
- ## Referencias
	- [[Página Relevante 1]]
	- [[Página Relevante 2]]
```

### Section Categories

Use these standard section names (in Spanish):

| Section Name | Purpose |
|--------------|---------|
| `Gestión de Cronograma Prueba Piloto` | Schedule changes, round updates |
| `Gestión de Participantes Prueba Piloto` | Lab confirmations, invitations |
| `Recursos Humanos` | Team changes, hiring, roles |
| `Desarrollo Técnico` | CALAIRE-APP, technical findings |
| `Gestión Administrativa` | Administrative tasks, communications |
| `Infraestructura` | Equipment, facilities, space |
| `Prospectación de Laboratorios` | New lab contacts, outreach |
| `Aprendizajes y Decisiones` | Lessons learned, key decisions |
| `Actualizaciones de Documentación` | Graph updates, sync activities |
| `Referencias` | Links to relevant pages (always last) |

### Block Properties

Each event block should include:

| Property | Format | Values |
|----------|--------|--------|
| `date::` | `YYYY-MM-DD` | Date of the event |
| `category::` | `[[Category]]` | `[[Prueba Piloto]]`, `[[Desarrollo Técnico]]`, `[[Gestión Administrativa]]` |
| `status::` | lowercase | `confirmed`, `pending`, `in_progress`, `in_review`, `cancelled`, `completed`, `documented`, `in_study` |

### Writing Style for Journals

1. **Format**: Start with `**Título del Evento:**` followed by description
2. **Voice**: Third person or impersonal (never first person)
3. **Tone**: Technical and professional
4. **Detail**: Include context, impact, and next steps
5. **Links**: Reference relevant MOCs and pages with `[[Page Name]]`
6. **Never copy user input verbatim**: Always reformulate and enrich

### Example Journal Entry

```markdown
# Registro del Día
  project:: [[CALAIRE-EA]]
- ## Gestión de Participantes Prueba Piloto
	- **Confirmación Universidad Pontificia Bolivariana (Gelima):** respuesta positiva recibida para participación en [[Ronda 5]] (segunda semana de abril 2026, periodo 8-13 de abril). Se procederá a actualizar documentación de confirmaciones y asignación de cupo en el calendario operativo.
	  date:: 2026-02-05
	  category:: [[Prueba Piloto]]
	  status:: confirmed
- ## Desarrollo Técnico
	- **Resultados Iniciales CALAIRE-APP:** César Yate, consultor especialista en ISO 17043, remitió primer análisis de validación comparativa entre cálculos ejecutados en el aplicativo y verificación manual. Los resultados evidencian discrepancias metodológicas que requieren revisión técnica profunda de los algoritmos implementados en [[CALAIRE-APP]].
	  date:: 2026-02-05
	  category:: [[Desarrollo Técnico]]
	  status:: in_review
- ## Referencias
	- [[Prueba Piloto]]
	- [[CALAIRE-APP]]
```

---

## Mermaid Diagrams

This graph uses Mermaid for visualizations (Gantt, Timeline). Example pattern:
```markdown
- Diagram Title
  collapsed:: true
    - CODIGO
      ```mermaid
      gantt
          title Chart Title
          dateFormat YYYY-MM-DD
          section Section 1
          Task :a1, 2026-03-02, 6d
      ```
```

---

## Config Reference (logseq/config.edn)

Key configurations:
- `:preferred-workflow :todo` - Uses TODO/DOING/DONE workflow
- `:journal/page-title-format "yyyy-MM-dd"` - ISO date format
- `:default-queries` - Auto-queries shown in journal footer:
  - `📋 CALAIRE-EA Tasks` - All open tasks linked to project
  - `🎯 Decisiones Recientes` - Blocks tagged `#decision`

---

## Common Operations

### Add a new task
```markdown
- TODO Descripción de la tarea
  project:: [[CALAIRE-EA]]
  deadline:: 2026-03-15
```

### Record a decision
```markdown
- #decision Se aprobó el protocolo de CO
  date:: 2026-01-30
```

### Create a meeting note
1. Create block: `[[Reunión: Tema de la reunión]]`
2. Navigate to the new page
3. Apply template `reunion`

### Create a laboratory page
1. Create file in `/pages/` with format: `Nombre del Laboratorio.md`
2. Use standard structure (see `ref/setup.md` section "Estructura de Páginas de Laboratorios")
3. Add to MOC `[[Laboratorios]]` under appropriate status section
4. Update `[[Prueba Piloto]]` with lab links if applicable

### Create an equipment page
1. Create file in `/pages/` with format: `Nombre del Equipo.md`
2. Use the standard structure from `pages/Equipos.md` (Plantilla para Nuevos Equipos)
3. Add the equipment link in `pages/Equipos.md` under the correct category
4. Link to `[[Prueba Piloto]]` and `[[Laboratorios]]` when it impacts logistics or ownership

### Create a work plan
1. Get timestamp: `date +"%y%m%d_%H%M"`
2. Create slug from topic (kebab-case, 5-7 words max)
3. Create file: `logs/plans/[TIMESTAMP]_plan_[slug].md`
4. Use structure from "Plan Creation Workflow" section

---

## Git Workflow

- Commit meaningful changes to content
- Exclude (already in .gitignore):
  - `.DS_Store`, `bak/`, `pages-metadata.edn`
  - `logseq/graphs-txid.edn`, `logseq/.recycle/`

---

## Session Continuity

This graph uses a memory system via `logs/` directory to persist context between agent sessions.

### Directory Structure

| File/Path                              | Purpose                              |
|----------------------------------------|--------------------------------------|
| `logs/CURRENT_SESSION.md`              | Live session state (mutable)         |
| `logs/history/YYMMDD_HHMM_findings.md` | Technical discoveries, milestones    |
| `logs/history/YYMMDD_HHMM_problems.md` | Blockers and troubleshooting records |
| `logs/plans/YYMMDD_HHMM_plan_[slug].md` | Multi-phase work plans with lifecycle tracking |

### Skills

| Skill      | When to Use                                                |
|------------|------------------------------------------------------------|
| `continue` | Session start, user says "continúa", "resumen", "qué sigue"|
| `saver`    | Session end, complex problem resolved, milestone completed |

### Boot Sequence

On ANY task, the agent should:
1. Check if `logs/CURRENT_SESSION.md` exists
2. If exists, read it immediately before proceeding
3. Check `logs/history/` for recent `_problems.md` files (priority blockers)
4. Check `logs/plans/` for active plans (status: approved or in_progress)

---

## Plan Creation Workflow

When the user requests planning or structuring multi-phase work (ej: "planificar categorización", "crear sistema de equipos", "migrar estructura"):

### Plan File Creation

1. **Generate timestamp:** `date +"%y%m%d_%H%M"`
2. **Create slug:** kebab-case, 5-7 words max (ej: `categorizacion-correos`, `sistema-equipos`)
3. **Create file:** `logs/plans/[TIMESTAMP]_plan_[slug].md`

### Plan Structure

```markdown
# Plan: [Título Descriptivo]

**Created**: YYYY-MM-DD HH:MM
**Updated**: YYYY-MM-DD HH:MM
**Status**: draft | approved | in_progress | completed | cancelled
**Slug**: [slug-corto]

---

## Objetivo

[Descripción concisa del objetivo del plan]

---

## Fases

### Fase 1: [Nombre de la fase]

**Objetivo:** [Descripción del objetivo de esta fase]

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 1.1 | path/file.md | Crear/Modificar/Verificar | Notas |

### Fase 2: [Nombre de la fase]

...

---

## Log de Ejecución

- [ ] Fase 1 iniciada
- [ ] Fase 1 completada
- [ ] Fase 2 iniciada
- [ ] Fase 2 completada
```

### Lifecycle Status

- `draft`: Plan created, not yet reviewed/approved
- `approved`: Plan reviewed, ready for execution
- `in_progress`: Plan is being executed
- `completed`: All phases completed successfully
- `cancelled`: Plan abandoned (document reason in log)

### Plan Update Rules

- Update `Updated` field whenever plan changes
- Update `Status` when transitioning between lifecycle stages
- Add checkboxes to Log de Ejecución as phases progress
- Add review findings from `revisor-fase` after each phase

---

## Phase Workflow

When working with plans in `logs/plans/` that have multiple phases (Fase 1, Fase 2, etc.), follow this workflow after completing each phase. See "Plan Creation Workflow" for how to create and structure plans.

### Per Phase Completion

1. **Execute Phase Review:** Use subagent `revisor-fase` to review the implemented phase for errors, inconsistencies, and risks
2. **Update Plan:** Incorporate findings from the reviewer into the plan file (`logs/plans/[slug].md`)
3. **Save Session:** Use the `saver` skill to persist state and create findings record
4. **Git Commit:** Commit changes with meaningful message
5. **Git Push:** Push commits to remote repository

### Subagent: `revisor-fase`

Use `task` with `subagent_type: "revisor-fase"` to execute phase reviews. The reviewer will:
- Identify errors in syntax (indentation, properties, markdown)
- Detect inconsistencies in links, tags, and references
- Highlight risks in content structure or navigation
- Provide structured feedback with severity tiers (Blocking, Required, Suggestions)

**Example invocation:**
```
Task: Revisar Fase 3 - Sistema de Equipos
Phase: Fase 3
Context: Se crearon `pages/Equipos.md` y `pages/Calibrador T700.md`, se actualizó `pages/CALAIRE-EA.md`
```

---

## No Build/Test Commands

This knowledge graph has no:
- Package managers (npm, pip, etc.)
- Build systems
- Test frameworks
- Linters or formatters

Validation is done visually in Logseq application.
