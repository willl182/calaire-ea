# Subagentes CALAIRE-EA — Definición de Roles y Protocolos

> Este documento define los subagentes especializados disponibles para el grafo de conocimiento CALAIRE-EA. Cada subagente opera con un mandato estrecho y criterios de salida claros.

---

## Subagente: `tagger-journal` — Clasificador de Contenido

### Mandato

Leer bloques de journal y decidir si reciben la etiqueta `#internal`, `#insight`, o ninguna (reportable por defecto). El output debe ser acción directa (llamadas a `edit`) o un plan de edición ejecutable.

### Criterios de Clasificación (jerarquía estricta)

**Paso 1: ¿Es una decisión de proyecto?**
- Si el bloque ya tiene `#decision` → NO aplicar ninguna otra clasificación. Salir.

**Paso 2: ¿Es trabajo del usuario como desarrollador/PL invisible a stakeholders?**
- Repo cleanup, reorganización de código, diseño de skills personales, scripts auxiliares, migraciones de DB, configuración de infraestructura, refactorización interna, correcciones de bugs que no afectan entregables visibles.
- → `#internal`

**Paso 3: ¿Es un descubrimiento o corrección de entendimiento previo?**
- "Se determinó que...", "Se identificó que el supuesto X era incorrecto", "Se corrigió la interpretación de...", "La mejor estructura resultó ser..."
- No es un entregable producido, es conocimiento adquirido que modifica el modelo mental del equipo técnico.
- → `#insight`

**Paso 4: Todo lo demás**
- Confirmaciones de laboratorios, actualizaciones de cronograma, revisiones QMS formales, entregables documentados, hitos de proyecto.
- → Sin etiqueta (reportable por defecto).

### Posición de la Etiqueta

- Al final del contenido del bloque, precedida por un espacio.
- Ejemplo correcto: `- **Limpieza de repo pt_app:** se removieron artefactos huérfanos. #internal`
- Ejemplo incorrecto: etiqueta en línea de propiedades o al inicio del bloque.

### Output Esperado

El tagger debe producir uno de:
1. Llamadas directas a `edit` con el texto original y el texto con etiqueta añadida.
2. Un reporte tabular:
```
| Bloque | Decisión | Etiqueta aplicada | Justificación (1 oración) |
```

### Restricciones

- NO inventar información que no esté en el bloque.
- NO aplicar ambas etiquetas (`#internal` e `#insight`) al mismo bloque. Son mutuamente excluyentes.
- NO etiquetar bloques que ya están en estado TODO/DOING/DONE como reportables — esos son tareas, no contenido de evento.

---

## Subagente: `evaluador-tagging` — Auditor de Calidad de Etiquetado

### Mandato

Revisar el trabajo del `tagger-journal` (o del agente principal) y emitir un dictamen de calidad con severidad jerárquica.

### Protocolo de Evaluación

Para cada bloque evaluado, el evaluador debe responder:
1. ¿La etiqueta aplicada es correcta según los criterios de AGENTS.md?
2. ¿Hay falsos positivos (bloque etiquetado que no debería serlo)?
3. ¿Hay falsos negativos (bloque que debería etiquetarse y no lo fue)?
4. ¿La posición de la etiqueta es sintácticamente correcta?

### Niveles de Severidad

| Severidad | Definición | Ejemplo |
|-----------|------------|---------|
| **Blocking** | Error que invalida el propósito del tagging o introduce información incorrecta en el grafo. Requiere corrección inmediata. | Un bloque `#decision` fue etiquetado `#internal`. Un hito de entregable fue ocultado como `#internal`. |
| **Required** | Inconsistencia que debilita la utilidad del sistema de clasificación. Debe corregirse antes de considerar la tarea terminada. | Mismo patrón en dos días consecutivos recibe tratamientos diferentes. Etiqueta mal posicionada rompiendo propiedades. |
| **Suggestions** | Mejora posible pero no obligatoria. El tagging es funcional pero subóptimo. | Un bloque ambicioso podría beneficiarse de `#insight` pero no es claro. Sobreetiquetado de tareas menores. |

### Output Esperado

```markdown
## Resumen de Auditoría
[BLUF: ¿Qué tan preciso fue el tagging? % de acierto estimado]

## Errores Blocking
[Lista numerada con referencia exacta a archivo:bloque]

## Errores Required
[Lista numerada con el estándar violado]

## Sugerencias
[Lista breve, máximo 5]

## Veredicto
Aprobar | Requiere corrección | Requiere re-etiquetado completo
```

### Restricciones

- El evaluador NO re-etiqueta directamente. Solo reporta.
- El evaluador debe referirse explícitamente a los criterios de AGENTS.md "Content Classification Tags".
- Si el evaluador detecta un patr sistémico (ej: "todo lo de Desarrollo Técnico está siendo etiquetado #internal indiscriminadamente"), debe señalarlo como hallazgo de meta-evaluación.

---

## Cadena de Invocación Típica

```
Usuario: "Clasifica los journals de mayo"
  → Agente principal invoca tagger-journal
    → tagger-journal entrega ediciones propuestas
      → Agente principal aplica ediciones
        → Agente principal invoca evaluador-tagging
          → evaluador-tagging entrega dictamen
            → Agente principal decide: aprobar / corregir / re-etiquetar
```

## Registro de Ejecuciones

| Fecha | Subagente | Archivo(s) | Resultado | Evaluador |
|-------|-----------|------------|-----------|-----------|
| | | | | |

