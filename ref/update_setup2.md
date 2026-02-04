# Actualización 2: Clarificación de Ubicación de TODOs en Journals

**Fecha:** 2026-02-03
**Motivo:** Identificar ambigüedad en el setup sobre dónde ubicar TODOs y #decision en journals diarios. En `2026_02_02.md` había 4 bloques sueltos al final sin categoría clara.

---

## Diagnóstico

### Bloques sueltos en `journals/2026_02_02.md` (líneas 14-31)

| Línea | Bloque | Categoría correspondiente |
|-------|--------|---------------------------|
| 14-15 | `#decision` Reajuste cronograma | **Prueba Piloto** |
| 16-21 | `DOING` Gestión de recursos | **Gestión Administrativa** |
| 22-27 | `TODO` Alistamiento Operativo | **Prueba Piloto** |
| 28-29 | `TODO` Diseño de socialización | **Prueba Piloto** |
| 30-31 | `TODO` Planificación auditoría SGC | **SGC / Calidad** |

### Raíz del problema

`ref/setup.md` no tenía instrucciones explícitas sobre la ubicación de TODOs/decisiones. Solo decía:

> "Nueva Tarea: Crear bloque en Journal → `TODO Tarea... project:: [[CALAIRE-EA]]`"

Pero no especificaba si debían ir dentro de categorías o sueltos al final.

---

## Solución Definida

**Decisión:** Opción A - TODOs y decisiones **dentro de categorías temáticas**

**Justificación:**
- Contexto inmediato: el bloque está junto al contenido relacionado
- Sin duplicación: no hay que mantener dos lugares
- Compatible con queries: Logseq igual captura todos los bloques con `project:: [[CALAIRE-EA]]`
- Consistencia: mismo patrón que el contenido narrativo

---

## Cambios a Implementar

### 1. `ref/setup.md` - Agregar instrucciones (línea ~110)

**Nueva sección a insertar después de "Uso del Journal Diario":**

```markdown
### Ubicación de TODOs y Decisiones

- **TODOs** y **#decision** van **dentro de la categoría temática** correspondiente.
- No crear secciones separadas para tareas al final del journal.
- Esto mantiene contexto inmediato y evita duplicación.

| Tipo de bloque | Ubicación |
|----------------|-----------|
| `TODO`, `DOING`, `DONE` | Bajo la categoría temática donde aplica |
| `#decision` | Bajo la categoría donde aplica la decisión |
```

---

### 2. `journals/2026_02_02.md` - Reorganizar bloques

**Estructura actual (problemática):**
```
- ## Prueba Piloto
    - [contenido]
- ## Gestión Administrativa
    - [contenido]
- ## Infraestructura
    - [contenido]
- #decision [sueltas]
- DOING [sueltas]
- TODO [sueltas]
- TODO [sueltas]
- TODO [sueltas]
```

**Estructura resultante (corregida):**
```
- ## Prueba Piloto
    - [contenido reprogramación]
    - #decision Reajuste del cronograma operativo...
      date:: 2026-02-02
    - TODO Alistamiento Operativo y Metrológico...
      project:: [[CALAIRE-EA]]
      collapsed:: true
        - Protocolo de encendido...
        - Ejecución de calibración...
        - Validación funcional...
    - TODO Diseño de socialización técnica para participantes...
      project:: [[CALAIRE-EA]]
- ## Gestión Administrativa
    - **Gestión Documental:** [contenido]
    - **Contratación:** [contenido]
    - DOING Gestión de recursos: Solicitar aval a Dirección ([[Carmen Zapata]]) para inicio de operaciones técnicas por parte de [[Fabian Moreno]]
      project:: [[CALAIRE-EA]]
      owner:: [[David Pulgarin]]
      :LOGBOOK:
      CLOCK: [2026-02-03 Tue 00:57:08]
      :END:
- ## SGC / Calidad
    - TODO Planificación de auditoría interna documental del SGC (Revisión de repositorio local)
      project:: [[CALAIRE-EA]]
- ## Infraestructura
  collapsed:: true
    - **Infraestructura IT:** cotización de equipos de cómputo remitida.
```

**Cambios específicos:**
1. Mover `#decision` (líneas 14-15) bajo `## Prueba Piloto`
2. Mover `DOING Gestión de recursos` (líneas 16-21) bajo `## Gestión Administrativa`
3. Mover `TODO Alistamiento Operativo` (líneas 22-27) bajo `## Prueba Piloto`
4. Mover `TODO Diseño de socialización` (líneas 28-29) bajo `## Prueba Piloto`
5. Mover `TODO Planificación auditoría` (líneas 30-31) a nueva sección `## SGC / Calidad`

---

## Checklist de Implementación

- [ ] Crear archivo `ref/update_setup2.md` con este contenido
- [ ] Leer `ref/setup.md` completo para identificar punto de inserción exacto
- [ ] Editar `ref/setup.md`: agregar sección "Ubicación de TODOs y Decisiones"
- [ ] Leer `journals/2026_02_02.md` completo
- [ ] Editar `journals/2026_02_02.md`: reorganizar bloques según estructura resultante
- [ ] Actualizar `logs/CURRENT_SESSION.md` con highlights y errores
- [ ] Crear log histórico si hay hallazgos relevantes
- [ ] Git add, commit, push

---

## Validación

**Criterios de éxito:**
- [ ] `ref/setup.md` tiene sección explícita sobre ubicación de TODOs
- [ ] `journals/2026_02_02.md` no tiene bloques sueltos al final
- [ ] Todos los TODOs/#decision están bajo su categoría temática
- [ ] Estructura es coherente con el template `journal-daily`
- [ ] Git commit con mensaje descriptivo
- [ ] Push exitoso a `origin/main`
