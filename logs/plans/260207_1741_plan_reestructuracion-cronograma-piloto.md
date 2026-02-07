# Plan: Reestructuración Cronograma Prueba Piloto

**Created**: 2026-02-07 17:41
**Updated**: 2026-02-07 19:50
**Status**: in_progress
**Slug**: `reestructuracion-cronograma-piloto`

---

## Objetivo

Reestructurar el cronograma de la Prueba Piloto debido a la cancelación de las rondas de febrero, reubicar a SIATA en abril, extender el calendario con rondas adicionales (6, 7, 8), actualizar los diagramas Mermaid, y documentar los cambios en contratación y hallazgos de CALAIRE-APP.

---

## Contexto y Aprendizajes

### Decisiones Clave (2026-02-07)

1. **Rondas 1 y 2 canceladas:** Febrero no es adecuado por preparación de contingencias para SIATA y autoridades ambientales (Corantioquia, otras zonas con contingencias en marzo).

2. **SIATA reubicado:** De Rondas 1-2 (febrero) a Ronda 6 (abril 15-20).

3. **Extensión del calendario:** Se crean Rondas 6, 7 y 8 para mayor flexibilidad en abril-mayo.

4. **Contratación Fabián:** Posterga de febrero a marzo-abril. La nueva contratación del técnico principal no alcanza a salir antes.

5. **CALAIRE-APP:** Las discrepancias reportadas por César Yate fueron principalmente por imputación de datos (menor gravedad de lo esperado). Pendiente enviar informe de hallazgos.

### Aprendizaje Documentado

> **Evitar programar rondas en periodos cercanos a contingencias ambientales.** Febrero-marzo es periodo crítico para SIATA y autoridades ambientales como Corantioquia debido a temporada de contingencias. Este aprendizaje aplica para futuras programaciones del servicio de ensayos de aptitud.

---

## Nuevo Cronograma

| Ronda | Fechas | Laboratorio | Status |
|-------|--------|-------------|--------|
| ~~Ronda 1~~ | ~~Feb 18-23~~ | - | cancelled |
| ~~Ronda 2~~ | ~~Feb 25-Mar 2~~ | - | cancelled |
| **Ronda 3** | Mar 18-23 | Universidad de Medellín | confirmed |
| **Ronda 4** | Mar 25-30 | Universidad de Medellín | confirmed |
| **Ronda 5** | Abr 8-13 | Universidad Pontificia Bolivariana | confirmed |
| **Ronda 6** | Abr 15-20 | SIATA | pending |
| **Ronda 7** | Abr 22-27 | (buffer/Politécnico) | planificada |
| **Ronda 8** | Abr 29 - May 4 | (buffer) | planificada |

**Inicio real:** 18 de marzo 2026 (Ronda 3)
**Fin:** 4 de mayo 2026 (Ronda 8)

---

## Fases

### Fase 1: Registro del Día + Cancelación Rondas Febrero

**Objetivo:** Documentar decisiones en journal y marcar Rondas 1-2 como cancelled con aprendizaje.

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 1.1 | `journals/2026_02_07.md` | Crear | Registrar: cancelación febrero, SIATA→abril, Fabián→marzo-abril, hallazgo imputación CALAIRE-APP |
| 1.2 | `pages/Ronda 1.md` | Modificar | `status:: cancelled` + observación con aprendizaje |
| 1.3 | `pages/Ronda 2.md` | Modificar | `status:: cancelled` + observación con aprendizaje |

---

### Fase 2: Crear Rondas 6, 7 y 8

**Objetivo:** Extender el calendario de abril hasta mayo con tres rondas adicionales.

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 2.1 | `pages/Ronda 6.md` | Crear | Abr 15-20, SIATA asignado, `status:: planificada` |
| 2.2 | `pages/Ronda 7.md` | Crear | Abr 22-27, buffer/Politécnico, `status:: planificada` |
| 2.3 | `pages/Ronda 8.md` | Crear | Abr 29 - May 4, buffer, `status:: planificada` |

---

### Fase 3: Actualizar Cronograma en Prueba Piloto y SIATA

**Objetivo:** Reflejar el nuevo calendario en los MOCs principales.

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 3.1 | `pages/Prueba Piloto.md` | Modificar | Nuevo inicio: Mar 18. Fin: May 4. Agregar R6-R8. Marcar R1-R2 cancelled. Actualizar confirmaciones SIATA→R6. |
| 3.2 | `pages/SIATA.md` | Modificar | R1-R2: cancelled, R6: pending (asignada). Actualizar observaciones. |

---

### Fase 4: Actualizar Diagramas Mermaid

**Objetivo:** Sincronizar visualizaciones con el nuevo cronograma. Mantener R1-R2 visibles con etiqueta "(CANCELLED)".

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 4.1 | `docs/gantt.md` | Modificar | Marcar R1-R2 como "(CANCELLED)". Agregar R6, R7, R8. Actualizar fechas inicio/fin. |
| 4.2 | `docs/timeline.md` | Modificar | Extender hasta mayo. Marcar Feb como cancelled. Agregar semanas R6-R8. |

---

### Fase 5: Actualizar Contratación Fabián

**Objetivo:** Reflejar nuevo timeline de contratación (marzo-abril en lugar de febrero).

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 5.1 | `pages/Fabian Moreno.md` | Modificar | Timeline: contratación marzo-abril |
| 5.2 | `pages/Equipo.md` | Modificar | Reflejar nuevo timeline técnico principal |

---

### Fase 6: Actualizar CALAIRE-APP

**Objetivo:** Documentar hallazgo de imputación y agregar tarea de envío de informe.

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 6.1 | `pages/CALAIRE-APP.md` | Modificar | Hallazgo: imputación de datos (menor gravedad). TODO: enviar informe a César Yate. |

---

### Fase 7: Actualizar Estado de Sesión

**Objetivo:** Sincronizar CURRENT_SESSION.md con nuevo estado del proyecto.

| # | Archivo | Acción | Descripción |
|---|---------|--------|-------------|
| 7.1 | `logs/CURRENT_SESSION.md` | Modificar | Reflejar estado actual, aprendizajes, nuevo cronograma |

---

## Hallazgos por Fase

### Fase 1 - Registro del Día + Cancelación Rondas Febrero

**Revisor**: `revisor-fase` (2026-02-07 18:15)

**Hallazgos importantes:**
- `status:: cancelled` aparece como bloque hijo con guion bajo "Estado", lo cual es consistente con la estructura del grafo pero puede limitar visibilidad en queries.

**Correcciones aplicadas:**
- Agregada etiqueta "(CANCELLED)" en el título de `pages/Ronda 1.md` y `pages/Ronda 2.md` para mejorar visibilidad en navegación y backlinks.

**Estado:** Completado con correcciones.

### Fase 2 - Crear Rondas 6, 7 y 8

**Revisor**: `revisor-fase` (2026-02-07 18:20)

**Hallazgos importantes:**
- Inconsistencia de enlace: `[[Politécnico JIC]]` en `pages/Ronda 7.md` no coincide con la página existente `pages/Politécnico Colombiano Jaime Isaza Cadavid.md`.

**Correcciones aplicadas:**
- Enlace corregido a `[[Politécnico Colombiano Jaime Isaza Cadavid|Politécnico JIC]]` usando alias para mantener texto corto.

**Observaciones:**
- Sección "Laboratorio" en rondas nuevas (singular) vs "Laboratorios Confirmados" en Ronda 5 (plural) - no se corrige por ser diferenciación intencional según estado de confirmación.

**Estado:** Completado con correcciones.

### Fase 3 - Actualizar Cronograma en Prueba Piloto y SIATA

**Revisor**: `revisor-fase` (2026-02-07 18:30)

**Hallazgos importantes:**
- Inconsistencia de enlaces: `[[Ronda 1 (CANCELLED)]]` en `pages/Prueba Piloto.md` vs `[[Ronda 1]]` en `pages/SIATA.md`.
- Sintaxis Logseq con indentación por espacios en secciones secundarias de ambos archivos.
- Uso de enlaces con triple corchete `[[[TECH]...]]` que no es sintaxis estándar de Logseq.

**Correcciones aplicadas:**
- Enlaces normalizados: `[[Ronda 1]]` y `[[Ronda 2]]` en ambos archivos (páginas ya tienen etiqueta "(CANCELLED)" en título).
- Título actualizado: "Coordinacion Prueba Piloto (Marzo-Mayo 2026) - Febrero cancelado por contingencias ambientales".
- Triple corchetes corregidos a doble corchete estándar en tags de correo.
- Indentación corregida: todos los bloques hijos ahora usan tabs (no espacios) en ambos archivos.
- Sed commands aplicados para reemplazar espacios por tabs en secciones secundarias.

**Observaciones:**
- Problema de encoding detectado en ambos archivos: caracteres acentuados no se muestran correctamente (M-CM-3, M-CM--n, etc.). No se corrigió en esta fase para evitar cambios mayores, pero debe ser monitoreado.

**Estado:** Completado con correcciones.

### Fase 4 - Actualizar Diagramas Mermaid

**Revisor**: `revisor-fase` (2026-02-07 19:40)

**Hallazgos importantes:**
- Blocking: En `docs/gantt.md` varias líneas no cumplen sintaxis gantt (faltan IDs en tareas como Inicio/Fin Prueba Piloto y múltiples Devolución Equipos).
- Required: `docs/gantt.md` reutiliza IDs (a1-a6) en todas las rondas. En Mermaid Gantt los IDs deben ser únicos.
- Required: `docs/timeline.md` extendía el calendario hasta May 9, contradiciendo el requisito de terminar en May 4.
- Required: Semanas marcadas como "(vacía)" que se superponen con R6-R8.

**Correcciones aplicadas:**
- IDs únicos asignados a cada tarea en `docs/gantt.md` (r1_rec, r1_ac, etc.).
- Agregados IDs a milestones (Inicio/Fin Prueba Piloto).
- `docs/timeline.md` ajustado para terminar en May 4 (eliminadas fechas May 5-9).
- Eliminadas etiquetas "(vacía)" en secciones correspondientes a R6-R8.
- Agregadas rondas 6, 7 y 8 en ambos diagramas con fechas correctas.
- R1-R2 marcadas con "(CANCELLED)" en ambos diagramas.

**Estado:** Completado con correcciones.

---

## Resumen de Archivos

| Tipo | Cantidad | Archivos |
|------|----------|----------|
| **Crear** | 4 | `journals/2026_02_07.md`, `pages/Ronda 6.md`, `pages/Ronda 7.md`, `pages/Ronda 8.md` |
| **Modificar** | 10 | `pages/Ronda 1.md`, `pages/Ronda 2.md`, `pages/Prueba Piloto.md`, `pages/SIATA.md`, `docs/gantt.md`, `docs/timeline.md`, `pages/Fabian Moreno.md`, `pages/Equipo.md`, `pages/CALAIRE-APP.md`, `logs/CURRENT_SESSION.md` |

---

## Log de Ejecución

- [x] Fase 1 iniciada
- [x] Fase 1 completada
- [x] Fase 1 corregida (hallazgos revisor-fase)
- [x] Fase 2 iniciada
- [x] Fase 2 completada
- [x] Fase 2 corregida (hallazgos revisor-fase)
- [x] Fase 3 iniciada
- [x] Fase 3 completada
- [x] Fase 3 corregida (hallazgos revisor-fase)
- [x] Fase 4 iniciada
- [x] Fase 4 completada
- [x] Fase 4 corregida (hallazgos revisor-fase)
- [x] Fase 5 iniciada
- [x] Fase 5 completada
- [ ] Fase 5 corregida (hallazgos revisor-fase)
- [ ] Fase 6 iniciada
- [ ] Fase 6 completada
- [ ] Fase 7 iniciada
- [ ] Fase 7 completada
