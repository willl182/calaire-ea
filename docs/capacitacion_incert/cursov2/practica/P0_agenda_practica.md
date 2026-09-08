# P0 — Agenda de la práctica de laboratorio

Contenido práctico complementario, **aparte de las 9 h del curso teórico** (M1–M8, ver `../README.md` y `../diseno_curso_v2.md`). Se programa como sesión independiente y ejecuta en instrumentos reales los protocolos que el curso teórico solo describe documentalmente. Referencias completas de cada experimento están en los archivos `E0x_*.md` de esta carpeta. **Duración real de P1: 7.5–9 h con dos subequipos en paralelo (O₃ y NOx); P2 añade 6.4–6.7 h adicionales.** Estos tiempos son propios de la práctica y no se cuentan dentro de las 9 h del curso teórico — ver el detalle de cómputo en las secciones P1 y P2 abajo (hallazgo A1 de la revisión de diseño).

## Prerrequisito logístico crítico: E08 se inicia ≥7 días antes

**E08 — Deriva de cero y span 24 h/7 d** es pasivo y de largo aliento: debe iniciarse **al menos 7 días antes** de la sesión práctica, con verificaciones en `t=0`, `24 h` y `7 d` (idealmente diarias). Si no se inicia con antelación, el equipo pierde la evidencia de deriva que alimenta E15 y debe sustituirla por el límite documental del fabricante, declarándolo como limitación.

Otras tareas de preparación, desde el día −7:

- Reunir certificados vigentes (patrón, cilindro NO, analizadores) para E14.
- Confirmar compatibilidad de líneas, destructor catalítico de O₃ y extracción con el montaje planeado.
- Verificar disponibilidad de cilindro de NO certificado, sujeción física y regulador compatible.
- Encender analizadores, calibrador y patrón la **noche anterior** a la sesión práctica (o mínimo 2 h antes si no es posible dejarlos encendidos), para no consumir tiempo de sesión en calentamiento.

## P1 — Bloque mínimo viable de la práctica (7.5–9 h con dos subequipos en paralelo)

**Corrección de cómputo (hallazgo A1):** sumar secuencialmente todos los experimentos de P1 en una sola vía da 580–640 min (9.7–10.7 h), no las "6.5–8 h" de una versión anterior de esta agenda. La sesión de 6–8 h solo es alcanzable dividiendo el equipo en **dos subequipos que trabajan en paralelo** —uno en la vía O₃, otro en la vía NOx— que convergen al final para el entregable conjunto E15. Con ese esquema, el **tiempo de pared (wall-clock) real de P1 es 7.5–9 h**, determinado por la vía O₃ (la más larga); la vía NOx termina antes y su subequipo puede apoyar a la vía O₃ o adelantar experimentos de P2.

También se reordenan dos experimentos respecto de versiones anteriores de esta agenda:
- **E11 (versión mínima, 30 min) sube a P1**, antes de E02, para fijar con evidencia propia la espera de estabilización usada en E02 (hallazgo A3), en vez de depender de la constante de tiempo del manual.
- **E09 sube a P1**, como prerrequisito de E01, porque su residual de aire cero alimenta directamente el término `u₀` calculado en el ejemplo de E01 (hallazgo A4).
- **E03 baja a P2**: al mover E09/E11 a P1, mantener E03 (130 min) también en P1 alargaba la vía NOx sin necesidad; en P2, el subequipo NOx puede ejecutarlo con más holgura.

### Vía O₃ (subequipo A)

| Orden | Experimento | Módulo asociado | Duración activa | Nota |
|---:|---|---|---|---|
| 1 | **E14** — Recorrido documental de cadena metrológica | M1 | 30–45 min | No requiere gases; puede iniciarse durante el calentamiento pasivo |
| 2 | **E09** — Calidad de aire cero (3 fuentes) | M4/M5 | 45 min | Prerrequisito de E01 (A4); alimenta `u₀` de E01 y E15 |
| 3 | **E01** — Ruido y repetibilidad de cero | M3/M4 | 55–70 min | Aire cero, O₃ apagado |
| 4 | **E11** — Tiempo de respuesta t10/t90 (versión mínima) | M5 | 30 min | Antes de E02 (A3); fija la espera de estabilización de E02 |
| 5 | **E02** — Verificación multipunto O₃, 3 ciclos | M5 | 180–210 min | O₃ activo, el bloque más largo de la práctica |
| 6 | **E15** — Presupuesto híbrido del equipo propio | M7 | 90 min | Entregable evaluado de la práctica (independiente del de M7); se ejecuta en conjunto con el subequipo NOx al converger las vías |

Subtotal vía O₃: 430–490 min (7.2–8.2 h). Con calentamiento compartido, checklist y cambios de configuración entre experimentos (~20–40 min de margen no desglosado arriba), el **tiempo de pared declarado para P1 es 7.5–9 h**.

### Vía NOx (subequipo B)

| Orden | Experimento | Módulo asociado | Duración activa | Nota |
|---:|---|---|---|---|
| 1 | **E04** — GPT y eficiencia del convertidor (sesión 1 de 2) | M6 | 100 min | Ver nota de segunda sesión abajo |
| 2 | **E05** — Verificación de corrección de firmware | M6 | 50 min | Requiere autorización para cambiar `η_f` temporalmente |
| — | (se une al subequipo A para E15) | M7 | — | Aporta resultados de E04/E05 al presupuesto conjunto |

Subtotal vía NOx antes de converger: 150 min (2.5 h) — termina antes que la vía O₃; el subequipo puede apoyar la vía O₃, avanzar checklist/documentación, o adelantar E03 (movido a P2) si el cronograma del día lo permite.

**E04 requiere una segunda sesión en día distinto** (ver protocolo E04): la primera sesión se ejecuta dentro de P1; la segunda (orden descendente, ~100 min) se agenda como continuación, idealmente el día siguiente a la práctica, o se sustituye por una nota de limitación en E15 si no se dispone de esa segunda sesión.

Si el grupo no puede dividirse en dos subequipos (por ejemplo, un solo equipo pequeño), P1 debe ejecutarse de forma secuencial y dura realmente **9.5–10.5 h** (una vía tras otra); en ese caso, planificar P1 como sesión completa, no como "6–8 h".

## P2 — Bloque adicional (opcional, según disponibilidad; no es "media sesión")

**Corrección de etiqueta (hallazgo A1):** los experimentos de este bloque suman 385–400 min (6.4–6.7 h), no media sesión (típicamente 3–4 h). Se ejecuta como una sesión adicional casi tan larga como P1, no como un complemento corto.

| Experimento | Módulo asociado | Duración | Nota |
|---|---|---|---|
| **E03** — Covarianza medida NO/NOx | M6/M8 | 130 min (60 min de adquisición útil) | Movido desde P1 (A1); cilindro NO abierto, O₃ apagado |
| **E06** — Transmisión de línea O₃ | M4 (plan de reemplazo) | 60–75 min | Requiere línea real + filtro de estación; mientras no se ejecute, E15 declara este término como documental (ver E15 y A4) |
| **E07** — Formación de NO₂ en línea corta/larga/larga caliente | M6 | 155 min | Mide la cinética real; el dataset de línea NOx del curso teórico queda como ejercicio de decisión (D6) |
| **E16** — MCM sobre modelo diferencial NO₂ con covarianza medida | M8 | 40 min | Usa resultados de E03 y E04; requiere computador con R |

Subtotal P2: 385–400 min (6.4–6.7 h). E10 (calibración de caudales del diluidor) y E12/E13 no cuentan con protocolo diseñado en los insumos de este curso y quedan fuera de P1/P2 hasta que se desarrollen.

## Entregable mínimo por equipo al cierre de la práctica

1. Hojas de registro de campo completas y sin sobrescritura (`hoja_registro_campo.md` y las tablas específicas de cada `E0x_*.md`).
2. Cálculos de `n_ef`, regresión multipunto, `u_pred`, covarianza NO/NOx, eficiencia GPT y, si se ejecutó, transmisión de línea, aire cero, t10/t90, deriva y MCM.
3. Matriz de cobertura y verificación anti-doble-conteo (ver E15).
4. Presupuesto híbrido del equipo propio (E15), con declaración final según la plantilla incluida en ese protocolo.
5. Si E08 no se completó por falta de anticipación, nota explícita de la limitación y sustitución por límite documental del fabricante.

## Referencias cruzadas con los módulos del curso teórico

- M3 → E01 (ruido y repetibilidad).
- M4 → E08/E15; el "plan de reemplazo" de M4 §4 apunta explícitamente a E01/E09 (u₀), E02 (u_r y falta de ajuste), E06 (transmisión de línea, documental hasta ejecutar P2) y E08 (deriva).
- M5 → E02 (multipunto, que ahora depende de E11 ejecutado antes en P1), E09 (aire cero), E11 (tiempo de respuesta y espera válida).
- M6 → E03 (covarianza, en P2), E04/E05 (GPT y firmware, en P1), E07 (línea NOx, en P2).
- M7 → **E15**, presupuesto del equipo propio, construido con evidencia de ambas vías (O₃ y NOx). Es el entregable evaluado **de la práctica**, separado del entregable de M7 (caso KRISS/BIPM), que se evalúa dentro del curso teórico y no se reemplaza.
- M8 → E03 (covarianza, P2) y E16 (MCM con covarianza medida, P2).
