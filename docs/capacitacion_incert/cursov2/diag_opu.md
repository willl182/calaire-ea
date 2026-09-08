# Diagnóstico de arquitectura documental — cursov2

**Fecha:** 2026-08-28
**Alcance:** `docs/capacitacion_incert/cursov2/`
**Estado:** diagnóstico. No se modificó ningún archivo.
**Origen:** conversación sobre el orden de los términos metrológicos, el rol del handout y el flujo de producción de material.

---

## 1. Conclusión en una frase

El paquete no tiene un problema de contenido: tiene un problema de **capas sin declarar**. Cinco artefactos con audiencias distintas conviven en dos carpetas, y dos de esos artefactos compiten por el mismo rol. Las capas de diapositivas no existen todavía.

---

## 2. El modelo de trabajo del autor

Flujo declarado, en orden de producción:

| # | Capa | Descripción |
|---|---|---|
| **0** | **Meta / instructor** | Versión más cargada del material teórico. Minutaje, ficha, prerrequisitos, organización de actividades, errores frecuentes, transiciones, procedencia exacta de fuentes, soluciones, cómo destrabar al grupo. |
| **1** | **Material teórico del participante** | Prosa completa, hilo narrativo lógico y consecuente. Es casi el discurso hablado. Se entrega como material teórico. |
| **2** | **Diapositivas texto** | Derivadas de capa 1. Texto comprimido, telegráfico. |
| **3** | **Diapositivas finales** | Capa 2 + imágenes, diagramas, diseño. |
| **R** | **Referencia de consulta** | (No es una etapa del flujo; artefacto perpendicular.) Glosario, tablas, fórmulas, checklists. Lo que el operador abre seis meses después en su puesto. |

Relación entre 0 y 1: **superconjunto**, no hermanos. Capa 1 se obtiene *quitando* bloques de capa 0, no reescribiendo. Esta decisión es la que gobierna todo el resto del diagnóstico.

---

## 3. Estado real de cada capa

| Capa | Dónde vive hoy | Volumen | Estado |
|---|---|---:|---|
| 0 — Meta | disperso dentro de `modulos/` + `modulos/soluciones/` | 607 + 1571 líneas | existe, **fusionado con capa 1** |
| 1 — Teórico participante | embebido en `modulos/`, sin separar | ~818 líneas (mezcladas) | existe, **no extraíble** |
| 2 — Diapositivas texto | — | 0 | **no existe** |
| 3 — Diapositivas finales | — | 0 | **no existe** |
| R — Referencia | `handout/gum_o3/` + `handout/no_nox/` | 869 + 120 líneas | existe, **contaminado con capa 1 duplicada** |

Verificación de ausencia de capas 2 y 3:

```
find . -iname "*slide*" -o -iname "*diapo*" -o -iname "*.pptx" \
       -o -iname "*reveal*" -o -iname "*beamer*"   →  0 resultados
```

---

## 4. Hallazgo principal: capa 0 y capa 1 comparten archivo

Reparto de líneas por rol de sección en los 8 módulos:

| Sección | Líneas | Audiencia |
|---|---:|---|
| Ficha + Objetivos (duración, prerrequisitos, materiales, distribución de tiempo) | 201 | solo instructor |
| Guion de exposición | 818 | **mezclado** |
| Ejercicio/actividad (enunciado, organización, tiempo, resultado esperado) | 245 | mezclado |
| Errores frecuentes + Cierre y transición | 161 | solo instructor |

**42 % de `modulos/` es meta pura.** El 57 % restante tampoco es limpio. Dentro del guion de exposición conviven, contados sobre los 8 módulos:

| Marcador | Ocurrencias | Capa |
|---|---:|---|
| `acumulado` (minutaje) | 45 | 0 |
| `Apoyo en el handout:` | 17 | 0 |
| `Idea fuerza:` | 27 | 2 (semilla) |
| `Referencias exactas:` | 7 | 0 + 1 |
| `Resultado esperado:` | 7 | 0 |
| `Enlace con la práctica:` | 5 | 0 |
| `Referencia integrada` | 4 | 0 + 1 |
| `Organización:` | 3 | 0 |
| `Conexión posterior` | 2 | 0 |
| `Pregunta de control:` | 1 | 0 |

Consecuencia: un mismo archivo sirve a dos lectores con necesidades opuestas. El instructor quiere más carga; el participante quiere menos. Nadie queda bien servido.

---

## 5. Hallazgo derivado: el handout es un intento fallido de extraer la capa 1

`handout/gum_o3/` no es capa 0, no es capa 2, y solo parcialmente es capa R. Es una **reescritura** de la capa 1, no una extracción.

Solapamiento verificado:

- M3 §3.3 (PDFs y divisores) ≈ `O3_H03_tipo_b_pdfs.md`
- M2 §3.3 (coeficientes de sensibilidad) ≈ `O3_H04_propagacion_guf.md`
- M7 bloque 6 (informe) ≈ `O3_H07_informe_gum.md`
- M1 §3.1 (trazabilidad) ≈ `O3_H01 §1.5`

Contenido genuinamente único, es decir capa R legítima:

- `O3_H08_glosario.md` — 23 términos, no aparecen definidos en ningún módulo
- `O3_H03` — tabla de PDFs con divisores
- `O3_H04` — ley de propagación en forma general
- `O3_H07` — checklist de informe GUM §7

Todo lo demás duplica narrativa. Estimación: de 869 líneas, ~350 son capa R real.

**Asimetría O₃ / NOx.** `handout/no_nox/` tiene 120 líneas en 10 archivos (`NOX_H03` = 7 líneas, `NOX_H08` = 3). M6 lo cita **una sola vez**. De facto ya funciona como capa R pura — checklist y control documental, sin duplicar a M6. Está mejor alineado que el de O₃, por accidente. Pero `README.md` presenta ambas familias como equivalentes.

**Vacío de instrucción de uso.** Búsqueda de `prelectura`, `lectura previa`, `antes del curso`, `leer.*handout` sobre `modulos/`, `README.md`, `diseno_curso_v2.md` y `handout/`: **0 resultados**. Nada dice si el handout se entrega antes, durante o después, ni si el participante debe leerlo.

---

## 6. Hallazgo sobre el orden de los términos metrológicos

La pregunta original —«¿no se deberían aclarar primero los términos?»— es correcta y apunta a una inversión real.

El vocabulario formal vive en `O3_H01` (mensurando, modelo de medición, error vs. incertidumbre, estándar/combinada/expandida, trazabilidad) y en el glosario `O3_H08`. Pero la secuencia de aula lo introduce operativamente antes:

| Momento | Términos usados | Dónde están definidos |
|---|---|---|
| M1 (min 0–35) | incertidumbre del patrón / del analizador / del valor transferido, corrección, incertidumbre residual, falla, doble conteo, covarianza | `O3_H01 §1.3`, `§1.4` — remitido, no dictado |
| M2 (min 35–83) | mensurando, coeficiente de sensibilidad | `O3_H01 §1.1`, `O3_H04 §4.1` |
| M3 (min 83–137) | **recién aquí** se definen Tipo A/B, PDF, combinación cuadrática | el módulo mismo |

`modulos/M1_trazabilidad.md:6` se autodeclara «establece el vocabulario y la arquitectura metrológica que se utilizarán en los módulos posteriores», pero `M1:111` delega ese vocabulario al handout: *«...para el vocabulario con que se distinguen estas tres incertidumbres»*.

M1 pide prestado vocabulario que llega formalmente 82 min después, apoyándose en un documento cuyo momento de lectura nadie definió.

Esta inversión **no se resuelve sola** al separar capas. Requiere decisión explícita. Dos salidas:

1. **Handout O₃ (capa R) como prelectura obligatoria**, con `O3_H00` + `O3_H01` + glosario marcados como lectura mínima. M1 puede entonces asumir el vocabulario. Riesgo: depende de que lean; alto en operadores de red.
2. **Bloque M0 de vocabulario, 15–20 min**, antes de M1: mensurando, error/corrección/incertidumbre, estándar/combinada/expandida, trazabilidad, Tipo A/B en versión mínima. M3 pasa a profundizar, no a introducir. Costo: 20 min de los 78 min de reserva logística. El glosario de capa R queda como su respaldo natural.

La opción 2 es robusta a que nadie lea nada antes. Es la recomendada si el curso se dicta a operadores sin envío previo de material.

---

## 7. Hallazgo sobre uniformidad: la capa 1 no es extraíble en 4 de 8 módulos

Sin estructura regular, la derivación de capas 1, 2 y 3 no se puede automatizar ni hacer consistente.

| Módulo | Subbloques `### 3.x` | `Idea fuerza` | Bloque de discurso |
|---|---:|---:|---|
| M1 | 5 | 5 | `Guion dictable` ×5 |
| M2 | 4 | 5 | `Guion dictable` ×4 |
| M3 | 4 | 5 | `Guion dictable` ×4 |
| M4 | 5 | 5 | `Guion dictable` ×5 |
| M5 | **0** | **1** | **ninguno** — §3 es prosa plana |
| M6 | 4 | **1** | **ninguno** |
| M7 | 0 (usa `### Bloque N`) | 4 | `Párrafo dictable` ×4 |
| M8 | 0 | 1 | **ninguno** |

Tres nombres distintos para el mismo objeto: `Guion dictable`, `Párrafo dictable`, ninguno. Dos esquemas de encabezado: `### 3.x` y `### Bloque N`.

**M5, M6 y M8 no tienen discurso redactado.** Tienen contenido, no narración. Para ellos, capa 1 no se puede extraer porque no hay qué extraer: hay que escribirla.

---

## 8. Hallazgo lateral: `solo_md/` es una capa derivada fuera de control

`solo_md/` replica el árbol completo (592 K) con los enlaces Markdown desanclados, para lectura fuera del repositorio.

- **No lo genera `build_paquete_html.py`** — `grep solo_md build_paquete_html.py` → 0 resultados.
- **No está en git** — sin historial; aparece como `??` en `git status`.
- **Ya divergió** de `modulos/`: M1 14 líneas, M3 16, M2 12, M7 10, M8 10, M4 8, M5 6, M6 2.

El delta es sistemático y benigno —quita `[texto](enlace)` y deja el texto—, pero la copia es manual y sin verificación. Es exactamente el patrón que produjo el problema del handout: dos archivos contando lo mismo, uno de ellos derivando en silencio.

Precedente positivo: `build_paquete_html.py` + `pandoc_rewrite_links.lua` ya generan `curso_paquete_completo.html` con validación de archivos, filas, anclas e IDs únicos. La infraestructura de derivación existe; `solo_md/` simplemente no la usa.

---

## 9. Mecanismo propuesto: una fuente, marcado por audiencia

Fuente única por módulo (= capa 0). Las demás capas se generan quitando bloques.

Ya existe la convención de facto: `**Idea fuerza:**`, `**Guion dictable:**`, `**Apoyo en el handout:**`. Falta que sea **regular y legible por máquina**. Esquema único por subbloque:

```markdown
### 3.N Título — 0:mm a 0:mm; acumulado 0:mm      ← capa 0 (minutaje)

**Idea fuerza:**            ← capa 2 (título de diapositiva)
**Guion dictable:**         ← capas 0 y 1 (el discurso; el texto del material teórico)
**Puntos:**                 ← capa 2 (3–5 viñetas comprimidas)
**Apoyo visual:**           ← capa 3 (qué diagrama, foto o esquema)
**Nota de facilitación:**   ← capa 0 (dónde se atasca el grupo, cómo destrabar)
**Referencias exactas:**    ← capa 0 completa; capa 1 en versión corta
**Apoyo en la referencia:** ← capa 0 (puntero a capa R)
```

Un solo `build_capas.py` emite:

| Salida | Regla |
|---|---|
| capa 0 | el archivo tal cual |
| capa 1 | `Guion dictable` + referencias cortas; sin minutaje, sin notas de facilitación, sin errores frecuentes, sin punteros internos |
| capa 2 | `Idea fuerza` + `Puntos` |
| capa 3 | capa 2 + `Apoyo visual` como marcador de imagen |
| `solo_md/` | cualquiera de las anteriores, con enlaces desanclados |

Ventajas frente a mantener archivos paralelos:

1. Es lo que ya está escrito, sin querer.
2. Anti-drift: el handout y `solo_md/` demuestran qué pasa con dos archivos que cuentan lo mismo.
3. Un archivo por módulo, no dos ni cinco. Menos superficie que mantener.

---

## 10. Inventario de deuda

| # | Deuda | Impacto | Esfuerzo |
|---|---|---|---|
| D1 | M5, M6, M8 sin `Guion dictable` — capa 1 inexistente ahí | **bloqueante** para capas 1–3 | alto: redactar discurso |
| D2 | Tres convenciones distintas para el bloque de discurso | bloquea derivación mecánica | bajo: renombrar |
| D3 | `handout/gum_o3/` duplica ~520 líneas de capa 1 | confusión de roles, riesgo de drift | medio: podar a ~350 líneas |
| D4 | Rol del handout nunca declarado (prelectura / aula / consulta) | impide decidir el orden de términos | bajo: decisión + 1 párrafo en README |
| D5 | Inversión de vocabulario M1 ↔ M3 | pedagógico, afecta a todos los participantes | medio: bloque M0 de 15–20 min |
| D6 | `solo_md/` derivado a mano, fuera de git, ya divergido | drift silencioso | bajo: generar o borrar |
| D7 | 27 `Idea fuerza` para ~120 subbloques-equivalentes | capa 2 arranca con ~20 % de semillas | alto, pero mecánico tras D2 |
| D8 | README presenta handout O₃ y NOx como equivalentes siendo asimétricos | expectativa falsa | bajo: 1 tabla en README |

---

## 11. Plan propuesto

Orden por dependencia, no por importancia.

1. **Declarar las cinco capas** en `README.md` y fijar la convención de bloques de §9. Renombrar `handout/` → `referencia/` o declarar explícitamente su rol de capa R. Resuelve D4 y D8. Sin tocar contenido.
2. **Piloto en M5** — el módulo más incompleto: 0 subbloques, 1 `Idea fuerza`, sin discurso. Si el esquema aguanta ahí, aguanta en todos. Ataca D1 y D2 en el peor caso.
3. **`build_capas.py`**, siguiendo el patrón de `build_paquete_html.py`. `solo_md/` pasa a ser salida generada. Resuelve D6.
4. **Propagar el esquema** a M1–M4 y M7 (tienen discurso, solo falta etiquetar), después a M6 y M8 (hay que redactarlo). Cierra D1, D2.
5. **Podar el handout O₃** a capa R real: glosario, tablas de PDFs, ley de propagación, checklist de informe. Las 30 anclas existentes siguen sirviendo. Cierra D3.
6. **Decidir el orden de términos**: bloque M0 de vocabulario (recomendado) o prelectura obligatoria de capa R. Cierra D5.
7. **Capas 2 y 3** al final, cuando la derivación ya es mecánica. Cierra D7.

Estimación de volumen para capas 2 y 3: 462 min de curso obligatorio, a 2–3 min por diapositiva ⇒ **150–200 diapositivas**.

---

## 12. Lo que NO está mal

Para evitar que el diagnóstico se lea como una condena:

- El contenido técnico es sólido y está trazado a fuente con página exacta (JCGM, QUAM, EN 14211, EPA, NISTIR, BIPM.QM-K1).
- El control documental es riguroso: la nota sobre APOA-370 vs. APNA-370 evita atribuir especificaciones equivocadas.
- Los datasets son reproducibles con semilla declarada (`20260819`).
- La separación curso teórico / práctica de laboratorio, con entregables evaluados independientes (M7 y E15), está bien argumentada.
- `build_paquete_html.py` ya valida archivos, filas, columnas, MathML, anclas, IDs únicos y ausencia de recursos externos. Es la base sobre la que se monta `build_capas.py`.
- `handout/no_nox/` ya es capa R correcta. Sirve de modelo para podar la de O₃.

El desfase es **de una capa y media**, no de arquitectura equivocada: contenido sobra, capa 0 y 1 están fusionadas, capas 2 y 3 no arrancaron.
