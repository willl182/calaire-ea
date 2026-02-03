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

---

## No Build/Test Commands

This knowledge graph has no:
- Package managers (npm, pip, etc.)
- Build systems
- Test frameworks
- Linters or formatters

Validation is done visually in Logseq application.
