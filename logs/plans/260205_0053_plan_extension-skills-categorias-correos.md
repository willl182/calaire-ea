# Plan: Extension Skills + Categorías + Equipos + Correos

**Created**: 2026-02-05 00:53
**Updated**: 2026-02-05 01:48
**Status**: in_progress
**Slug**: `extension-skills-categorias-correos`

---

## Objetivo

Extender los skills `saver` y `continue` para soportar planes persistentes, luego ejecutar el plan de categorías MOC, sistema de equipos e ingesta de correos 2026.

---

## Fase 1: Extensión de Skills

**Objetivo:** Agregar soporte para `logs/plans/` en saver y continue.

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 1.1 | `~/.config/opencode/skills/saver/SKILL.md` | Modificar | Agregar sección plans en File Structure, When to Use, y Step 4C |
| 1.2 | `~/.config/opencode/skills/continue/SKILL.md` | Modificar | Agregar verificación de plans en Step 3 y Step 4 |
| 1.3 | `logs/plans/` | Crear directorio | Estructura para planes persistentes |

**Cambios detallados en saver:**
- File Structure: agregar ítem 4 para `logs/plans/YYMMDD_HHMM_plan_[slug].md`
- When to Use: agregar ítem 4 "When to user requests to create or save a work plan"
- Step 1: agregar `mkdir -p logs/plans` al comando
- Nuevo Step 4C: template para planes con status, log de ejecución y campo `Updated`
- Mejoras de redacción: "Represents" → "Represents", "prevent" → "prevent", "requests" → "requests"

**Cambios detallados en continue:**
- Step 3: agregar `ls -t logs/plans/ 2>/dev/null | head -n 2 || echo "No plans found"`
- Step 4: agregar bullet "Active Plans" en resumen ejecutivo

---

## Fase 2: Sistema de Categorías como MOCs

**Objetivo:** Las 5 categorías del journal funcionan como páginas navegables.

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 2.1 | `docs/tags_project.csv` | Modificar | Columna `Categoria_Journal` con formato `[[...]]` |
| 2.2 | `pages/Gestión Administrativa.md` | Crear | MOC para finanzas, contratación, comunicaciones |
| 2.3 | `pages/Desarrollo Técnico.md` | Crear | MOC para calibración, app, protocolos, capacitación |
| 2.4 | `pages/Infraestructura.md` | Crear | MOC para TI, instalaciones, transporte |
| 2.5 | `pages/Prueba Piloto.md` | Verificar | Ya existe, confirmar estructura MOC |
| 2.6 | `pages/QMS.md` | Verificar | Ya existe como SGC/Calidad |
| 2.7 | `pages/CALAIRE-EA.md` | Modificar | Agregar sección "Categorías Temáticas" |

---

## Fase 3: Sistema de Equipos

**Objetivo:** Crear estructura para gestión de equipos de referencia.

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 3.1 | `pages/Equipos.md` | Crear | MOC de equipos de medición y calibración |
| 3.2 | `pages/Calibrador T700.md` | Crear | Página técnica calibrador nuevo, enlace a diapositivas |
| 3.3 | `pages/CALAIRE-EA.md` | Modificar | Agregar `[[Equipos]]` a MOCs Principales |

---

## Fase 4: Ingesta de Correos 2026

**Objetivo:** Procesar 8 correos relevantes de 2026 y registrar en journals.

| # | Archivo | Acción | Correos | Categoría |
|---|---------|--------|---------|-----------|
| 4.1 | `journals/2026_01_29.md` | Crear | #229 Funciones contrato | `[[Gestión Administrativa]]` |
| 4.2 | `journals/2026_01_30.md` | Modificar | #231 Re:Funciones, #232 T700 | `[[Gestión Administrativa]]`, `[[Desarrollo Técnico]]` |
| 4.3 | `journals/2026_02_02.md` | Modificar | #233 Re:Funciones | `[[Gestión Administrativa]]` |
| 4.4 | `journals/2026_02_03.md` | Modificar | #234-235 Cuentas, #236 UdeM | `[[Gestión Administrativa]]`, `[[Prueba Piloto]]` |
| 4.5 | `journals/2026_02_04.md` | Crear | #237 César Yate app | `[[Desarrollo Técnico]]` |

---

## Fase 5: Documentación

**Objetivo:** Actualizar documentación con nuevas estructuras.

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 5.1 | `ref/setup.md` | Modificar | Agregar secciones: Categorías como MOCs, Páginas de Equipos |
| 5.2 | `AGENTS.md` | Modificar | Agregar operación: Crear página de equipo |
| 5.3 | `README.md` | Modificar | Agregar referencias a categorías y equipos |
| 5.4 | `logs/CURRENT_SESSION.md` | Modificar | Actualizar estado de sesión |

---

## Resumen

| Tipo | Cantidad | Archivos |
|------|----------|----------|
| **Crear** | 8 | `logs/plans/`, `Gestión Administrativa.md`, `Desarrollo Técnico.md`, `Infraestructura.md`, `Equipos.md`, `Calibrador T700.md`, `2026_01_29.md`, `2026_02_04.md` |
| **Modificar** | 12 | `saver/SKILL.md`, `continue/SKILL.md`, `tags_project.csv`, `CALAIRE-EA.md`, `Prueba Piloto.md`, `2026_01_30.md`, `2026_02_02.md`, `2026_02_03.md`, `ref/setup.md`, `AGENTS.md`, `README.md`, `CURRENT_SESSION.md` |
| **Verificar** | 2 | `Prueba Piloto.md`, `QMS.md` |

---

## Log de Ejecución

- [x] Fase 1: Extensión de Skills (completada con mejoras de redacción)
  - [x] 1.1 saver/SKILL.md
  - [x] 1.2 continue/SKILL.md
  - [x] 1.3 logs/plans/
- [x] Fase 2: Sistema de Categorías
  - [x] 2.1 tags_project.csv
  - [x] 2.2-2.4 Crear MOCs (Gestión Administrativa, Desarrollo Técnico, Infraestructura)
  - [x] 2.5-2.6 Verificar y actualizar MOCs existentes (Prueba Piloto, QMS, CALAIRE-EA)
  - [x] Correcciones aplicadas:
  - [x] Agregar `[[Prueba Piloto]]` y `[[SGC / Calidad]]` a CALAIRE-EA.md
  - [x] Completar tags en Gestión Administrativa.md
  - [x] Mover `[[[EVENTO] Taller]]` a Prueba Piloto.md
  - [x] Corregir indentación con tabs (MOCs reescritos)
---

## Resultados de Revisión (Subagente) - Fase 2

**Hallazgos críticos**: Ninguno.

**Hallazgos importantes**:
- Falta de categorías en MOC principal: corregido agregando `[[Prueba Piloto]]` y `[[SGC / Calidad]]`
- Tags faltantes en MOCs: corregido agregando `[[[EVENTO] Socialización]]` y `[[[EVENTO] Congreso/Evento]]` a Gestión Administrativa
- Tags en categoría incorrecta: corregido moviendo `[[[EVENTO] Taller]]` a Prueba Piloto

**Hallazgos menores**:
- Posible problema de indentación con tabs (pendiente verificación visual en Logseq)

**Riesgos**:
- Inconsistencia potencial entre `[[SGC / Calidad]]` en CSV vs `[[QMS]]` en QMS.md (no documentado)

**Recomendaciones del revisor**:
1. Verificar indentación con tabs en MOCs de categorías
2. Documentar convención definitiva entre `[[SGC / Calidad]]` y `[[QMS]]` en `ref/setup.md`
3. Verificar que MOC de `[[Prueba Piloto]]` liste todos los tags del CSV mapeados a esa categoría

**Checklist de verificación del revisor - Fase 2** (7/7 completados):
- [x] `docs/tags_project.csv` mantiene 5 categorías únicas con formato `[[...]]` y nombres alineados
- [x] `pages/CALAIRE-EA.md` lista las 5 categorías en "Categorías Temáticas (Journal)"
- [x] `pages/Gestión Administrativa.md` incluye todos los tags de su categoría
- [x] `pages/Desarrollo Técnico.md` contiene solo los tags de su categoría
- [x] Existe MOC explícito para `[[SGC / Calidad]]` o el CSV se ajusta a `[[QMS]]`
- [x] MOC de `[[Prueba Piloto]]` lista los tags asociados del CSV
- [x] Indentación con tabs validada en los MOCs de categorías

---

## Resultados de Revisión (Subagente) - Fase 3

**Hallazgos críticos**: Ninguno.

**Hallazgos importantes** (todos corregidos):
- `pages/Equipos.md` tenía líneas sin prefijo `- ` (rompían estructura de bloques): corregido
- `pages/Equipos.md` usaba espacios en indentación en lugar de tabs: corregido
- Bloque con template no anidado correctamente: corregido
- Tabla de estatus dentro de bloque: corregido

**Hallazgos menores**:
- Ninguno después de correcciones

**Riesgos**:
- Riesgo de navegación mitigado: estructura de bloques corregida en `pages/Equipos.md`

**Checklist de verificación del revisor - Fase 3** (6/6 completados):
- [x] `pages/Equipos.md` sin líneas sueltas (todas con prefijo `- `)
- [x] `pages/Equipos.md` con indentación por tabs en sub-bloques
- [x] Template de equipos correctamente anidado bajo su bloque
- [x] Tabla de estatus dentro de un bloque y legible en Logseq
- [x] `[[Equipos]]` y `[[Equipo]]` mantenidos como páginas distintas y usados correctamente
- [x] `[[Presentación T700]]` presente en `pages/Calibrador T700.md`

- [x] Fase 3: Sistema de Equipos
   - [x] 3.1 Crear MOC `pages/Equipos.md`
   - [x] 3.2 Crear página técnica `pages/Calibrador T700.md`
   - [x] 3.3 Agregar `[[Equipos]]` a `pages/CALAIRE-EA.md`
- [ ] Fase 4: Ingesta de Correos
  - [ ] 4.1-4.5
- [ ] Fase 5: Documentación
  - [ ] 5.1-5.4
