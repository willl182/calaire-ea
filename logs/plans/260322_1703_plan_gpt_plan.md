# Plan: Actualización documental P-PSEA-09 y P-PSEA-06

**Created**: 2026-03-22 17:03
**Updated**: 2026-03-22 17:16
**Status**: completed
**Slug**: gpt_plan

---

## Objetivo

Definir una ruta de trabajo trazable para actualizar los procedimientos [P-PSEA-09](/home/w182/w421/calaire-ea/docs/ppsea09/P-PSEA-09.md) y [p-psea-06](/home/w182/w421/calaire-ea/docs/ppsea09/p-psea-06.md), integrando de forma coherente toda la documentación disponible en `docs/ppsea09/`, con énfasis en la transición a ISO/IEC 17043:2023, la consistencia con ISO 13528:2022 y el tratamiento explícito de escenarios con pocos participantes en ensayos de aptitud para gases contaminantes criterio.

---

## Alcance documental del plan

Las siguientes fuentes deben revisarse y utilizarse como insumo obligatorio durante la actualización:

| Fuente | Rol dentro de la actualización |
|---|---|
| `docs/ppsea09/P-PSEA-09.md` | Procedimiento base de planificación del EA a reestructurar |
| `docs/ppsea09/p-psea-06.md` | Procedimiento estadístico base a depurar y normalizar |
| `docs/ppsea09/iso 13528_2022.md` | Base normativa estadística primaria |
| `docs/ppsea09/iso 17043_2023.md` | Base normativa primaria para requisitos del proveedor PT |
| `docs/ppsea09/iso 17043_2023 eng.pdf` | Contraste terminológico y verificación de matices normativos |
| `docs/ppsea09/gpt_planea.md` | Síntesis amplia para rediseño de planificación del esquema |
| `docs/ppsea09/gpt_planstat.md` | Síntesis amplia para rediseño estadístico con pocos participantes |
| `docs/ppsea09/claude_planea.md` | Insumos sobre transición 2023, gestión, roles y operación |
| `docs/ppsea09/claude_planstat.md` | Insumos sobre n < 5, valor asignado independiente y métricas alternativas |
| `docs/ppsea09/gem_planea.md` | Insumos de análisis de riesgos, transición y estructura CASCO |
| `docs/ppsea09/gem_planstat.md` | Insumos de arquitectura metrológica y regulación de esquemas reducidos |
| `docs/ppsea09/z_planea.md` | Resumen operativo de estructura mínima del plan del EA |

---

## Criterios rectores de actualización

1. Separar con claridad el contenido de planificación del esquema ([P-PSEA-09](/home/w182/w421/calaire-ea/docs/ppsea09/P-PSEA-09.md)) del contenido de diseño y evaluación estadística ([p-psea-06](/home/w182/w421/calaire-ea/docs/ppsea09/p-psea-06.md)).
2. Eliminar comentarios incrustados, texto provisional y redacción ambigua, sustituyéndolos por lenguaje técnico final y controlado.
3. Resolver contradicciones internas sobre número mínimo de participantes, uso de consenso, uso de mediana, Algoritmo A, MADe, nIQR y criterios de evaluación.
4. Alinear ambos procedimientos con la lógica documental del SGC: roles autorizados, trazabilidad, confidencialidad, control documental, subcontratación permitida y gestión del riesgo.
5. Garantizar que ambos procedimientos queden mutuamente referenciados sin duplicación excesiva: `P-PSEA-09` define qué debe planificarse y `p-psea-06` define cómo se sustenta estadísticamente.

---

## Fases

### Fase 1: Diagnóstico y matriz de trazabilidad normativa

**Objetivo:** construir una matriz de decisión que relacione requisitos normativos, vacíos actuales y fuente documental de soporte para cada procedimiento.

| # | Archivo | Acción | Descripción |
|---|---|---|---|
| 1.1 | docs/ppsea09/P-PSEA-09.md | Verificar | Marcar vacíos por cada literal a-u, comentarios incrustados y puntos sin cierre técnico |
| 1.2 | docs/ppsea09/p-psea-06.md | Verificar | Marcar errores de sintaxis, fórmulas mal transcritas, ambigüedad metodológica y solapamientos con P-PSEA-09 |
| 1.3 | docs/ppsea09/iso 17043_2023.md | Verificar | Extraer requisitos aplicables a diseño, planificación, subcontratación, confidencialidad, evaluación y reporte |
| 1.4 | docs/ppsea09/iso 13528_2022.md | Verificar | Extraer reglas aplicables a valor asignado, sigma_pt, incertidumbre, homogeneidad, estabilidad y puntajes |
| 1.5 | docs/ppsea09/iso 17043_2023 eng.pdf | Verificar | Confirmar terminología crítica cuando exista duda en traducción o alcance de cláusulas |
| 1.6 | docs/ppsea09/*.md | Verificar | Consolidar una matriz fuente-tema-decisión para evitar repetir o contradecir criterios entre documentos |

### Fase 2: Reestructuración de P-PSEA-09

**Objetivo:** convertir [P-PSEA-09](/home/w182/w421/calaire-ea/docs/ppsea09/P-PSEA-09.md) en un procedimiento normativamente limpio para la planificación y preparación del esquema de EA.

| # | Archivo | Acción | Descripción |
|---|---|---|---|
| 2.1 | docs/ppsea09/P-PSEA-09.md | Modificar | Reescribir objetivo, alcance, definiciones y referencias con redacción final y sin notas marginales |
| 2.2 | docs/ppsea09/P-PSEA-09.md | Modificar | Reorganizar los literales a-u bajo una estructura legible y consistente con ISO/IEC 17043:2023 |
| 2.3 | docs/ppsea09/P-PSEA-09.md | Modificar | Precisar roles autorizados, evidencias de competencia y actividades no subcontratables |
| 2.4 | docs/ppsea09/P-PSEA-09.md | Modificar | Incorporar criterios de participación, límites operativos, confidencialidad, prevención de colusión y contingencias |
| 2.5 | docs/ppsea09/P-PSEA-09.md | Modificar | Reemplazar afirmaciones estadísticas simplificadas por referencias controladas hacia `p-psea-06.md` |
| 2.6 | docs/ppsea09/P-PSEA-09.md | Modificar | Armonizar referencias al SGC, gestión de riesgos, registros, formatos y comunicación con participantes |

### Fase 3: Depuración y fortalecimiento de p-psea-06

**Objetivo:** convertir [p-psea-06](/home/w182/w421/calaire-ea/docs/ppsea09/p-psea-06.md) en el procedimiento estadístico maestro, con reglas explícitas para escenarios estándar y de población reducida.

| # | Archivo | Acción | Descripción |
|---|---|---|---|
| 3.1 | docs/ppsea09/p-psea-06.md | Modificar | Corregir redacción, acentos, notación y fórmulas mal renderizadas o truncadas |
| 3.2 | docs/ppsea09/p-psea-06.md | Modificar | Definir jerarquía de métodos para valor asignado: referencia externa, formulado, consenso robusto y casos excepcionales |
| 3.3 | docs/ppsea09/p-psea-06.md | Modificar | Formalizar reglas por tamaño de muestra: `p >= 12`, `p < 12`, y escenarios críticos de muy pocos participantes |
| 3.4 | docs/ppsea09/p-psea-06.md | Modificar | Dejar explícito cuándo procede `z`, `z'`, `zeta` y `En`, y bajo qué supuestos de incertidumbre |
| 3.5 | docs/ppsea09/p-psea-06.md | Modificar | Integrar homogeneidad, estabilidad y presupuesto de incertidumbre definitiva del valor asignado |
| 3.6 | docs/ppsea09/p-psea-06.md | Modificar | Definir registros requeridos, criterios de convergencia, salidas del algoritmo y condiciones de revisión técnica |

### Fase 4: Armonización cruzada entre procedimientos

**Objetivo:** asegurar que ambos procedimientos funcionen como un sistema documental coherente y no como textos aislados.

| # | Archivo | Acción | Descripción |
|---|---|---|---|
| 4.1 | docs/ppsea09/P-PSEA-09.md | Verificar | Revisar que todo contenido estadístico de alto detalle se remita a `p-psea-06.md` |
| 4.2 | docs/ppsea09/p-psea-06.md | Verificar | Revisar que la lógica operativa, de comunicación y de planificación permanezca en `P-PSEA-09.md` |
| 4.3 | docs/ppsea09/P-PSEA-09.md | Modificar | Ajustar referencias internas a formatos, instructivos y demás procedimientos P-PSEA relacionados |
| 4.4 | docs/ppsea09/p-psea-06.md | Modificar | Ajustar referencias normativas, criterios y notas metodológicas a la versión final del procedimiento |

### Fase 5: Revisión editorial y cierre documental

**Objetivo:** dejar ambos archivos listos para revisión técnica interna y aprobación formal.

| # | Archivo | Acción | Descripción |
|---|---|---|---|
| 5.1 | docs/ppsea09/P-PSEA-09.md | Verificar | Controlar consistencia terminológica, numeración, tablas, referencias y lenguaje institucional |
| 5.2 | docs/ppsea09/p-psea-06.md | Verificar | Controlar consistencia entre fórmulas, variables, unidades, criterios de decisión y glosario |
| 5.3 | docs/ppsea09/ | Verificar | Confirmar que todas las fuentes de `docs/ppsea09/` quedaron absorbidas o descartadas con justificación |
| 5.4 | logs/history/ | Crear | Registrar hallazgos metodológicos o decisiones críticas que deban preservarse para futuras revisiones |

---

## Decisiones metodológicas preliminares a resolver durante la ejecución

1. Confirmar si `P-PSEA-09.md` debe mencionar umbrales estadísticos concretos o limitarse a remitir a `p-psea-06.md`.
2. Definir la postura institucional para poblaciones reducidas: si se permitirá consenso con mediana/Algoritmo A solo como contingencia o si se privilegiará de forma explícita el valor asignado independiente.
3. Determinar si `sigma_pt` será prescriptiva, derivada de consenso robusto o seleccionada por escenario, y cómo quedará documentada esa jerarquía.
4. Confirmar qué parte del presupuesto de incertidumbre queda en `p-psea-06.md` y cuál solo se referencia desde informes o registros técnicos.
5. Establecer si el procedimiento estadístico incorporará de forma explícita criterios/reglas para `n < 5` o si esos casos quedarán bajo anexo o nota técnica complementaria.

---

## Log de Ejecución

- [x] Fase 1 iniciada
- [x] Fase 1 completada
- [x] Fase 2 iniciada
- [x] Fase 2 completada
- [x] Fase 3 iniciada
- [x] Fase 3 completada
- [x] Fase 4 iniciada
- [x] Fase 4 completada
- [x] Fase 5 iniciada
- [x] Fase 5 completada

## Resultado de implementación

- Se implementaron los entregables finales en `docs/ppsea09/mm25_ppsea09.md` y `docs/ppsea09/mm25_ppsea06.md`.
- Se eliminó la redacción provisional presente en los documentos base y se trasladó a una estructura normativa limpia en los artefactos finales.
- Se consolidó la separación funcional: planificación operativa en `mm25_ppsea09.md` (21 ítems a-u de ISO 17043:2023 §7.2.1.3, autorización §6.2.6, gestión de riesgos §7.2.1.2, confidencialidad §4.2) y metodología estadística en `mm25_ppsea06.md` (jerarquía x_pt 5 niveles, jerarquía σ_pt 6 niveles, reglas p < 12, árboles de decisión z/z'/ζ/En, incertidumbre definitiva, homogeneidad/estabilidad, fallback Algoritmo A, multimodalidad y exclusión).
