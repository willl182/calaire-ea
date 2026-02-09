# Plan: Corrección de Sintaxis de Tags y Alineación CSV

**Created**: 2026-02-08 20:29
**Updated**: 2026-02-08 20:29
**Status**: draft
**Slug**: correccion-sintaxis-tags

---

## Objetivo

Corregir la sintaxis incorrecta de tags en el grafo Logseq (`[[[TAG]]]` → `[[TAG]]`) y alinear el CSV de tags (`docs/tags_project.csv`) con el uso real en páginas MOC de categorías.

---

## Contexto del Problema

### Hallazgos del Análisis

| Problema | Severidad | Impacto |
|----------|-----------|---------|
| **Tags no usados en journals** | Alta | El sistema existe solo en documentación |
| **Sintaxis triple corchete `[[[TAG]]]`** | Alta | Logseq no los interpreta como enlaces |
| **Tags SGC del CSV faltan en MOCs** | Media | Inconsistencia entre definición y uso |
| **Inconsistencia SGC vs QMS** | Media | `[[SGC / Calidad]]` en CSV vs `[[QMS]]` real |

### Datos Cuantitativos

- Tags definidos en CSV: 35
- Tags referenciados en MOCs: ~28
- Tags con sintaxis errónea: 12
- Tags usados en journals: **0**
- Tags SGC faltantes: 3 (Auditoría, Procedimiento, Acreditación)

---

## Fases

### Fase 1: Corregir Sintaxis Triple Corchete → Doble Corchete

**Objetivo:** Convertir 12 tags con `[[[TAG]]]` a sintaxis válida `[[TAG]]`

| # | Archivo | Línea | Tag Actual | Tag Corregido | Acción |
|---|---------|-------|-----------|---------------|--------|
| 1.1 | `pages/Gestión Administrativa.md` | 21 | `[[[ACCION] Aprobación]]` | `[[ACCION] Aprobación]]` | Editar |
| 1.2 | `pages/Gestión Administrativa.md` | 22 | `[[[ACCION] Decisión]]` | `[[ACCION] Decisión]]` | Editar |
| 1.3 | `pages/Gestión Administrativa.md` | 27 | `[[[EVENTO] Socialización]]` | `[[EVENTO] Socialización]]` | Editar |
| 1.4 | `pages/Gestión Administrativa.md` | 28 | `[[[EVENTO] Congreso/Evento]]` | `[[EVENTO] Congreso/Evento]]` | Editar |
| 1.5 | `pages/Desarrollo Técnico.md` | 18 | `[[[TECH] Desarrollo App]]` | `[[TECH] Desarrollo App]]` | Editar |
| 1.6 | `pages/Desarrollo Técnico.md` | 19 | `[[[TECH] Calibración]]` | `[[TECH] Calibración]]` | Editar |
| 1.7 | `pages/Desarrollo Técnico.md` | 23 | `[[[EVENTO] Capacitación]]` | `[[EVENTO] Capacitación]]` | Editar |
| 1.8 | `pages/Infraestructura.md` | 14 | `[[[INFRA] TI]]` | `[[INFRA] TI]]` | Editar |
| 1.9 | `pages/Infraestructura.md` | 15 | `[[[INFRA] Instalaciones]]` | `[[INFRA] Instalaciones]]` | Editar |
| 1.10 | `pages/Infraestructura.md` | 16 | `[[[INFRA] Transporte]]` | `[[INFRA] Transporte]]` | Editar |
| 1.11 | `pages/Infraestructura.md` | 17 | `[[[TECH] Ronda - Equipos]]` | `[[TECH] Ronda - Equipos]]` | Editar |
| 1.12 | Verificar | - | - | - | Confirmar que `grep '\[\[\[' pages/*.md` devuelve 0 resultados |

### Fase 2: Definir Convención SGC vs QMS

**Objetivo:** Documentar la convención de nombres entre `[[SGC / Calidad]]` (CSV) y `[[QMS]]` (página existente)

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 2.1 | `ref/setup.md` | Crear | Sección "Convenciones de Nombres de Tags" |
| 2.2 | `ref/setup.md` | Documentar | Definir que `[[QMS]]` es el nombre estándar del MOC |
| 2.3 | `ref/setup.md` | Documentar | Aclarar que tags de categoría usan `[[SGC]]` como prefijo para emails |
| 2.4 | `ref/setup.md` | Documentar | Relación: `[[QMS]]` (página MOC) ↔ `[[SGC] ...]` (tags de correo) |
| 2.5 | `docs/tags_project.csv` | Considerar | ¿Actualizar CSV para usar `[[QMS]]` en lugar de `[[SGC / Calidad]]`? |

### Fase 3: Agregar Tags Faltantes del CSV a MOCs

**Objetivo:** Agregar los 3 tags SGC del CSV que no existen en ningún MOC

| # | Tag del CSV | Ubicación propuesta | Acción |
|---|-------------|-------------------|--------|
| 3.1 | `[[SGC] Auditoría]` | Crear `pages/SGC Calidad.md` o agregar a `[[QMS]]` | Decisión pendiente |
| 3.2 | `[[SGC] Procedimiento]` | Crear `pages/SGC Calidad.md` o agregar a `[[QMS]]` | Decisión pendiente |
| 3.3 | `[[SGC] Acreditación]` | Crear `pages/SGC Calidad.md` o agregar a `[[QMS]]` | Decisión pendiente |

**Nota:** Si existe `pages/QMS.md`, agregar estos tags allí. Si no, decidir entre:
- Opción A: Crear `pages/SGC Calidad.md` (página separada)
- Opción B: Agregar tags a `[[QMS]]` (mismo MOC, tags diferentes)

### Fase 4: Actualizar Documentación de Uso de Tags

**Objetivo:** Crear guía clara para aplicar tags en journals

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 4.1 | `pages/templates.md` | Crear | Template `etiqueta` con ejemplo de uso |
| 4.2 | `pages/templates.md` | Documentar | Instrucciones: "Cuándo y cómo usar tags de correo" |
| 4.3 | `AGENTS.md` | Actualizar | Agregar sección "Uso de Tags de Correo" |
| 4.4 | `AGENTS.md` | Actualizar | Agregar nota sobre sintaxis correcta (doble corchete, no triple) |

---

## Log de Ejecución

- [ ] Fase 1 iniciada - Corrección de sintaxis triple corchete
- [ ] Fase 1 completada - 12 tags corregidos
- [ ] Fase 2 iniciada - Documentación de convención SGC vs QMS
- [ ] Fase 2 completada - Convención documentada en `ref/setup.md`
- [ ] Fase 3 iniciada - Agregar tags SGC faltantes
- [ ] Fase 3 completada - 3 tags SGC agregados a MOCs
- [ ] Fase 4 iniciada - Actualizar documentación de uso de tags
- [ ] Fase 4 completada - Template y guías creadas

---

## Preguntas Abiertas

### Decisiones Pendientes

| # | Pregunta | Opciones | Recomendación |
|---|----------|----------|---------------|
| 1 | ¿Dónde ubicar tags SGC? | A) Crear `pages/SGC Calidad.md`, B) Agregar a `[[QMS]]` | **A** - Página separada para tags SGC |
| 2 | ¿Actualizar CSV para usar `[[QMS]]`? | A) Sí, actualizar CSV, B) Mantener `[[SGC / Calidad]]` | **B** - Mantener CSV actual, documentar mapeo |
| 3 | ¿Agregar template `etiqueta` a `templates.md`? | A) Sí, crear template, B) No, documentación suficiente | **A** - Template ayuda a agente y usuario |
| 4 | ¿Corregir CSV si tags no se usan? | A) Marcar como "no usado", B) Eliminar del CSV, C) Mantener | **C** - Mantener, se usarán en el futuro |

---

## Riesgos

| Riesgo | Impacto | Mitigación |
|--------|---------|------------|
| Romper enlaces existentes | Bajo | Solo corregimos sintaxis `[[[ → [[`, no cambiamos nombres |
| Inconsistencia persistente | Medio | Documentar convención clara en `ref/setup.md` |
| Tags nunca se usan en journals | Alto | Incluir ejemplo de uso en `templates.md` y `AGENTS.md` |

---

## Referencias

- `docs/tags_project.csv` - Definición original de 35 tags
- `AGENTS.md` - Directrices del grafo Logseq
- `ref/setup.md` - Guía de configuración y convenciones
- `logs/history/260205_0133_findings.md` - Hallazgos previos sobre tags (líneas 150-156)
