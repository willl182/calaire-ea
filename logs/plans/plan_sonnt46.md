# Plan: Evaluación de la Implementación del Ajuste F-PSEA-06 (Ronda Simple)

**Created**: 2026-04-10 11:30 -0500  
**Status**: approved  
**Slug**: eval-impl-fpsea06-ronda-simple  
**Modelo evaluador**: claude-sonnet-4-6  
**Referencia**: `logs/plans/260410_1026_plan_ajuste-fpsea06-ronda-simple.md`  
**Archivo evaluado**: `docs/prueba_piloto/ronda_simple/F-PSEA-06 Plan de Ronda EA.md`

---

## Objetivo

Verificar que la implementación del ajuste de `F-PSEA-06` —ejecutada en las Fases 2, 3 y 4 del plan de ajuste— cumple con lo declarado en los resultados de cada fase y que el documento resultante es coherente con los instructivos del piloto y funcional como registro operativo aprobable.

La evaluación no reabre decisiones de diseño ya tomadas. Se limita a contrastar las afirmaciones del plan de ajuste con la evidencia textual presente en el documento.

---

## Alcance de la evaluación

| Dimensión | Qué se evalúa |
|---|---|
| Completitud estructural | Que todas las secciones prometidas en la Fase 2 existan en el documento |
| Fidelidad de contenido | Que el contenido de la Fase 3 aterrizó correctamente los puntos a)–u) del documento de planificación |
| Coherencia inter-documental | Que F-PSEA-06 no contradice I-PSEA-07, I-PSEA-09 y P-PSEA-10 en los puntos identificados como críticos |
| Depuración de placeholders | Que los campos `[POR DEFINIR]` se limitan a datos no inferibles declarados en la Fase 4 |
| Exclusiones explícitas | Que las exclusiones para n=1 están presentes y bien formuladas |
| Funcionalidad como registro | Que el documento puede usarse como formato de aprobación sin requerir reestructuración |

---

## Fases de evaluación

### Fase A: Verificación estructural (resultado Fase 2 del plan de ajuste)

**Objetivo:** Confirmar que el formato tiene todas las secciones declaradas como implementadas en la Fase 2.

| # | Verificación | Sección esperada en F-PSEA-06 | Criterio de aceptación |
|---|---|---|---|
| A.1 | Control documental | §3 Identificación y control documental | Tabla con código, nombre, versión, fecha, elaboró/revisó/aprobó |
| A.2 | Alcance técnico | §4 Alcance técnico de la ronda | Participante, analitos, base metrológica, enfoque estadístico y score |
| A.3 | Tabla maestra de ronda | §5 Tabla maestra | Participante P1=SIATA, CO y SO₂, fechas 22/23/24 abr, 1 jornada |
| A.4 | Recursos CALAIRE | §7.1 Recursos de CALAIRE | CRM CO, CRM SO₂, dilución, aire cero, manifold, UPS, ambiental |
| A.5 | Personal autorizado | §7.2 Personal autorizado | 4 roles: coordinación EA, técnico, soporte metrológico, logística |
| A.6 | Control estadístico | §9 Control estadístico pre-ronda | `x_pt`, `u(x_pt)`, `σ_pt`, tipo de score, justificación n=1 |
| A.7 | Aprobaciones | §12 Aprobaciones | Tabla con elaboró, revisó, aprobó |

**Documentación de resultados:** tabla A — sección encontrada/no encontrada, observaciones.

---

### Fase B: Verificación de contenido (resultado Fase 3 del plan de ajuste)

**Objetivo:** Confirmar que los 21 puntos a)–u) del documento de planificación fueron abordados según el mapa de aplicabilidad definido en la Fase 1.

| # | Puntos fuente | Sección esperada en F-PSEA-06 | Criterio de aceptación |
|---|---|---|---|
| B.1 | a) Personal competente | §7.2 + §7.2.1 RACI | Matriz RACI con 5 roles y 8 actividades críticas |
| B.2 | b) Proveedores/servicios ext. | §7.1.1 Proveedores externos | Al menos 3 tipos de servicio con aplicación específica a la ronda simple |
| B.3 | c) Criterios de participación | §6.1 Elegibilidad | Al menos 4 criterios explícitos para SIATA/analizadores EPA |
| B.4 | d) Capacidad — exclusión parcial | §10.3 Adaptaciones y exclusiones | Debe excluir explícitamente capacidad de 8 equipos y multi-participante |
| B.5 | e) Información requerida al part. | §6.2 Información requerida | Tabla con ≥4 campos de información pre-ronda |
| B.6 | f) Rangos esperados | §9.2 Rangos de trabajo | CO 0–10 ppm, SO₂ 0–500 ppb con nota sobre setpoints |
| B.7 | g) Riesgos técnicos | §9.3 Riesgos | Al menos 4 riesgos con impacto y control |
| B.8 | h) Control del ítem PT | §7.3 + §7.3.1 + §7.3.2 | Origen in situ, control MRC, manifold, incidentes (fuga, deterioro, fallo, daño) |
| B.9 | i) Integridad de resultados | §10.1 Integridad | Formato normalizado, entrega mínima, revisión interna, retroalimentación |
| B.10 | j) Actividades del participante | §8.1 Actividades del participante | ≥3 actividades con resultado esperado y registro |
| B.11 | k) Info suministrada al part. — adaptada | §8.2 Información y cronograma | Incluir solo lo aplicable a n=1: instrucciones, rangos tentativos, no setpoints |
| B.12 | l) Cronograma | §8 Cronograma operativo | T-14, T-7, T-1, Día 1, Día 2, Día 3 con responsable y registro |
| B.13 | m) Homogeneidad/estabilidad | §9.5 Homogeneidad y estabilidad | Distinguir que no aplica homogeneidad entre unidades; sí aplica estabilidad del generador |
| B.14 | n) Reporte | §8.3 Fechas de medición y reporte | Frecuencia, fecha de medición, ventana de reporte (15 días → 2026-05-08) |
| B.15 | o) Valor asignado — exclusión parcial | §9.1 + §10.3 | Debe excluir consenso/mediana; incluir referencia trazable y σ_pt prescrito |
| B.16 | p) Trazabilidad metrológica | §9.4 Trazabilidad | CRM trazable, cadena metrológica, u(x_pt) |
| B.17 | q) Diseño estadístico | §9 Control estadístico + §9.1 | Justificación n=1, z' o ζ, sin consenso |
| B.18 | r) Evaluación del desempeño | §9.4 | Score z' o ζ, no segregación por método |
| B.19 | s) Devoluciones al participante | §10.1 | Retroalimentación o informe según cronograma |
| B.20 | t) Confidencialidad | §10.2 | Control de acceso, codificación, difusión autorizada |
| B.21 | u) Respuesta ante incidentes | §7.3.2 | Tabla con 4 escenarios, respuesta mínima y registro |

**Documentación de resultados:** tabla B — punto cubierto/parcial/ausente, observaciones.

---

### Fase C: Coherencia inter-documental

**Objetivo:** Verificar que F-PSEA-06 no contradice los tres instructivos de referencia en los puntos críticos identificados en la Fase 1.

| # | Par a verificar | Punto crítico | Criterio de aceptación |
|---|---|---|---|
| C.1 | F-PSEA-06 §9 vs I-PSEA-07 | Diseño estadístico n=1 | F-PSEA-06 no menciona consenso, mediana ni NIQR; documenta referencia trazable y σ_pt prescrito |
| C.2 | F-PSEA-06 §8 vs I-PSEA-09 | Cronograma T-14 y paquete pre-ronda | Los hitos del cronograma en F-PSEA-06 coinciden con los definidos en I-PSEA-09 §6.x |
| C.3 | F-PSEA-06 §7.3 vs P-PSEA-10 | Ítem PT in situ vs materiales del participante | F-PSEA-06 deja explícita la distinción: cilindros del participante ≠ ítem PT |
| C.4 | F-PSEA-06 §6 vs I-PSEA-09 | Prerrequisitos y F-PSEA-05A | F-PSEA-06 menciona F-PSEA-05A como prerrequisito y es coherente con plazo T-14 |

**Fuentes a leer durante la evaluación:** `I-PSEA-07`, `I-PSEA-09`, `P-PSEA-10` (solo las secciones relevantes señaladas).

---

### Fase D: Depuración de placeholders y datos inferibles

**Objetivo:** Confirmar que los únicos campos `[POR DEFINIR]` son los listados en la Fase 4 del plan de ajuste como no inferibles.

**Campos autorizados como pendientes:**

| Campo pendiente autorizado | Sección en F-PSEA-06 |
|---|---|
| Código formal de la ronda | §3 |
| Elaboró / Revisó / Aprobó (nombre) | §3 y §12 |
| Setpoints aprobados (niveles CO y SO₂) | §9.2 / §11 |
| CRM: proveedor, lote, certificado, vigencia | §7.1 |
| Equipos declarados y cilindros del participante | §6 |
| Autorización de acceso | §6 |
| Confirmaciones documentales (F-PSEA-05A recibido, etc.) | §6.2 y §10 |
| `x_pt`, `u(x_pt)`, `σ_pt` por analito | §9 / §11 |
| Firmas | §12 |

**Verificaciones de la Fase D:**

| # | Verificación | Criterio |
|---|---|---|
| D.1 | Todo `[POR DEFINIR]` presente en F-PSEA-06 corresponde a la lista anterior | No debe haber placeholders en campos que podían inferirse de comunicaciones, instructivos o plan de ajuste |
| D.2 | La sede de ejecución está completa y correcta | §3 debe leer: "Laboratorio CALAIRE — UNAL Medellín (Bloque 19A, Campus El Volador, Cra 65 No 59A-110)" |
| D.3 | La ventana de reporte está explícita | §8.3 debe indicar 15 días + fecha límite 2026-05-08 |
| D.4 | No existen campos vacíos sin marcador `[POR DEFINIR]` que queden silenciosamente en blanco | Revisión de completitud de tablas |

---

### Fase E: Funcionalidad como registro operativo aprobable

**Objetivo:** Verificar que el documento puede operar como registro de aprobación sin requerir reestructuración.

| # | Criterio de funcionalidad | Verificación |
|---|---|---|
| E.1 | El documento tiene una sección de aprobaciones con los roles mínimos | §12 con elaboró, revisó, aprobó |
| E.2 | El flujo de aprobación pre-ronda puede seguirse de forma lineal en el documento | Lectura secuencial: §3 → §4 → §5 → §6 → §7 → §8 → §9 → §10 → §11 → §12 |
| E.3 | Los campos `[POR DEFINIR]` son distinguibles y no se confunden con texto narrativo | Todos los campos pendientes usan el marcador estándar |
| E.4 | Las exclusiones están formuladas como declaraciones positivas y no solo como ausencia | §10.3 debe tener formulaciones explícitas del tipo "No aplica X porque…" |
| E.5 | El documento no arrastra texto genérico copiado del documento de planificación general sin adaptar | Sin bloques narrativos en primera persona o con referencias a "el programa" sin especificar la ronda simple |

---

## Documentación de resultados

### Formato de reporte de la evaluación

Al ejecutar cada fase, registrar en un hallazgo de evaluación (`logs/history/YYMMDD_HHMM_findings.md`) con la siguiente estructura:

```
## Evaluación F-PSEA-06 — Ronda Simple

### Resumen ejecutivo
- Fases evaluadas: A, B, C, D, E
- Veredicto global: [Aprobado / Aprobado con observaciones / Requiere ajuste]

### Tabla de resultados por fase
| Fase | Verificaciones | Cumple | Parcial | No cumple |
|------|---------------|--------|---------|-----------|
| A    | 7             |        |         |           |
| B    | 21            |        |         |           |
| C    | 4             |        |         |           |
| D    | 4             |        |         |           |
| E    | 5             |        |         |           |

### Observaciones por verificación fallida o parcial
[Listado con ID de verificación, descripción del hallazgo y acción sugerida]

### Conclusión
[Párrafo de cierre con recomendación: el documento está listo para diligenciamiento y aprobación / requiere los siguientes ajustes antes de proceder]
```

---

## Supuestos de la evaluación

- La evaluación usa únicamente la versión actual de `F-PSEA-06` y los documentos referenciados (`I-PSEA-07`, `I-PSEA-09`, `P-PSEA-10`); no relee el documento fuente de planificación general completo.
- No se reabre el diseño estadístico, la selección de participante ni la estructura de rondas del piloto (Propuesta A). Son restricciones fijas.
- Las verificaciones son binarias (cumple/no cumple) o de tres niveles (cumple/parcial/ausente), con observación escrita solo cuando el resultado no es "cumple".
- Si se detectan ajustes necesarios, se documentan como observaciones en el hallazgo; no se aplican directamente durante la evaluación sin autorización del usuario.

---

## Log de Ejecución

- [x] Fase A iniciada — 2026-04-10 11:24
- [x] Fase A completada — 7/7 CUMPLE — `logs/history/260410_1124_findings.md`
- [x] Fase B iniciada — 2026-04-10 11:35
- [x] Fase B completada — 21/21 CUMPLE — `logs/history/260410_1135_findings.md`
- [x] Fase C iniciada — 2026-04-10 11:48
- [x] Fase C completada — 3/4 CUMPLE, 1 PARCIAL (C.2) — `logs/history/260410_1148_findings.md`
- [x] Fase D iniciada — 2026-04-10 12:00
- [x] Fase D completada — 4/4 CUMPLE — `logs/history/260410_1200_findings.md`
- [x] Fase E iniciada — 2026-04-10 12:15
- [x] Fase E completada — 4/5 CUMPLE, 1 PARCIAL (E.4) — `logs/history/260410_1215_findings.md`
- [x] Hallazgo de evaluación registrado — `logs/history/260410_1220_findings.md`
