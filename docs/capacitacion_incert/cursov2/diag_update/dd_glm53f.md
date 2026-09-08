# Diagnóstico final de arquitectura documental — cursov2

**Fecha:** 2026-08-28
**Directorio evaluado:** `docs/capacitacion_incert/cursov2/`
**Alcance:** arquitectura pedagógica y documental del curso; relación entre módulos, handouts, solucionarios, protocolos y futuras diapositivas.
**Estado:** diagnóstico. No se modificó ningún archivo.
**Origen:** fusión de los diagnósticos `diag_sol.md` y `diag_opu.md`, que coinciden en el modelo de capas y difieren en énfasis (uno pedagógico, el otro forense-quantitativo). Este documento conserva lo verificable de ambos.

---

## 1. Conclusión en una frase

El curso no tiene un problema de contenido: tiene un problema de **capas sin declarar**. Cinco artefactos con audiencias distintas conviven en dos carpetas, la capa de autor y la del participante comparten archivo, las capas de diapositivas no existen todavía, y los desajustes pedagógicos detectados (vocabulario invertido, conceptos usados antes de enseñarse) no se resuelven solos al separar capas: requieren decisión explícita.

---

## 2. Modelo de trabajo del autor

Flujo declarado, en orden de producción:

| # | Capa | Descripción | Pregunta rectora |
|---|---|---|---|
| **0** | **Meta maestro / instructor** | Versión más completa y cargada: teoría, discurso oral, minutaje, ficha, prerrequisitos, organización de actividades, errores frecuentes, transiciones, respuestas, variantes según grupo, procedencia exacta de fuentes, criterios de evaluación. | ¿Qué necesito saber, recordar y tener disponible para enseñar bien este bloque? |
| **1** | **Material teórico del participante** | Prosa completa, hilo narrativo lógico y consecuente. Es casi el discurso hablado. Se entrega como material teórico. | ¿Qué necesita leer y conservar el participante para comprender el curso después de la sesión? |
| **2** | **Guion textual de diapositivas** | Derivado de capa 1. Texto comprimido, telegráfico; una idea principal por diapositiva. | ¿Qué necesita estar escrito en pantalla mientras se explica esta idea? |
| **3** | **Diapositivas visuales** | Capa 2 + imágenes, diagramas, composición, jerarquía visual, revelado progresivo. | ¿Cómo hacer visible la idea sin convertir la diapositiva en una página del manual? |
| **R** | **Referencia de consulta** | (Artefacto perpendicular, no etapa del flujo.) Glosario, tablas, fórmulas, checklists. Lo que el operador abre seis meses después en su puesto. | — |

Relación entre 0 y 1: **superconjunto, no hermanos**. Capa 1 se obtiene *quitando* bloques de capa 0, no reescribiendo. Esta decisión gobierna todo el resto del diagnóstico. La capa 0 no es un handout ni se entrega al participante: es la fuente pedagógica superior del curso.

Productos auxiliares, fuera del eje de derivación pero con rol propio:

- **Solucionarios privados:** resolución completa, cálculos paso a paso, criterios de corrección, variantes aceptables. Material del instructor, no tercera fuente doctrinal.
- **Protocolos prácticos (E01–E16):** autonomía controlada; repiten lo necesario para ejecutar una actividad de principio a fin, con la misma notación y terminología del material principal.
- **Fichas operativas / ayudas de campo:** consulta rápida; no conducen una actividad completa.

---

## 3. Estado real de cada capa

| Capa | Dónde vive hoy | Volumen | Estado |
|---|---|---:|---|
| 0 — Meta | disperso dentro de `modulos/` + `modulos/soluciones/` | 607 + 1571 líneas | existe, **fusionada con capa 1** |
| 1 — Teórico participante | embebida en `modulos/`, sin separar | ~818 líneas mezcladas | existe, **no extraíble** en 4 de 8 módulos |
| 2 — Guion de diapositivas | — | 0 | **no existe** |
| 3 — Diapositivas visuales | — | 0 | **no existe** |
| R — Referencia | `handout/gum_o3/` + `handout/no_nox/` | 869 + 120 líneas | existe, **contaminada con capa 1 duplicada** (O₃) |

Verificación de ausencia de capas 2 y 3:

```text
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

Consecuencia: un mismo archivo sirve a dos lectores con necesidades opuestas. El instructor quiere más carga (minutaje, resultados de ejercicios como el numérico de `modulos/M2_modelo_medicion.md`, los valores esperados de `u_c` y `U` en `modulos/M4_presupuesto_analizador.md`, las conclusiones anticipadas de `modulos/M8_opcional_monte_carlo.md`); el participante quiere menos. Nadie queda bien servido.

Este contenido no es un defecto por sí mismo: es coherente con una versión meta. El problema real es que ese rol no está declarado y no existe una derivación limpia hacia los demás productos.

---

## 5. Hallazgo derivado: el handout es un intento fallido de extraer la capa 1

`handout/gum_o3/` no es capa 0, no es capa 2, y solo parcialmente es capa R. Es una **reescritura** de la capa 1, no una extracción. Además mezcla dos funciones:

1. piezas básicas que deberían formar parte del relato principal del participante;
2. desarrollos avanzados que funcionan correctamente como anexos técnicos.

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

De 869 líneas, ~350 son capa R real. **Asimetría O₃ / NOx:** `handout/no_nox/` tiene 120 líneas en 10 archivos (`NOX_H03` = 7 líneas, `NOX_H08` = 3). M6 lo cita una sola vez. De facto ya funciona como capa R pura — checklist y control documental, sin duplicar a M6. Está mejor alineado que el de O₃, por accidente. Pero `README.md` presenta ambas familias como equivalentes, lo que crea una expectativa falsa.

**Vacío de instrucción de uso.** Búsqueda de `prelectura`, `lectura previa`, `antes del curso`, `leer.*handout` sobre `modulos/`, `README.md`, `diseno_curso_v2.md` y `handout/`: **0 resultados**. Nada dice si el handout se entrega antes, durante o después, ni si el participante debe leerlo.

**Criterio de frontera propuesto:** pertenece al material teórico principal todo lo necesario para seguir los módulos obligatorios y resolver las actividades requeridas. Pertenece a anexos técnicos (capa R avanzada) aquello que amplía, deriva o trata casos especiales: autocorrelación detallada, distribución t desplazada, PDFs arcoseno y trapezoidal, Welch–Satterthwaite, Cholesky, extensiones del método de Monte Carlo.

---

## 6. Hallazgo pedagógico: inversión de vocabulario y conceptos adelantados

La pregunta original —«¿no se deberían aclarar primero los términos?»— es correcta y apunta a una inversión real.

El vocabulario formal vive en `O3_H01` y en el glosario `O3_H08`, pero la secuencia de aula lo introduce operativamente antes:

| Momento | Términos usados | Dónde están definidos |
|---|---|---|
| M1 (min 0–35) | incertidumbre del patrón / del analizador / del valor transferido, corrección, incertidumbre residual, falla, doble conteo, covarianza | `O3_H01 §1.3`, `§1.4` — remitido, no dictado |
| M2 (min 35–83) | mensurando, coeficiente de sensibilidad; usa `u(T)`, `u(P)` | `O3_H01 §1.1`, `O3_H04 §4.1` |
| M3 (min 83–137) | **recién aquí** se definen Tipo A/B, PDF, incertidumbre estándar, combinación cuadrática | el módulo mismo |

`modulos/M1_trazabilidad.md:6` se autodeclara «establece el vocabulario y la arquitectura metrológica que se utilizarán en los módulos posteriores», pero `M1:111` delega ese vocabulario al handout. M1 pide prestado vocabulario que llega formalmente 82 min después, apoyándose en un documento cuyo momento de lectura nadie definió.

Problemas conexos, todos vigentes:

- **La cadena `u_i → u_c → U = k·u_c` no tiene dueño docente claro.** `U` y `k` aparecen en ejercicios y resultados, pero su introducción formal vive principalmente en el handout.
- **El informe GUM se exige antes de enseñarse.** M7 solicita un resultado auditable conforme a GUM §7; la lista más completa de elementos del informe vive en `O3_H07_informe_gum.md`. Cobertura, redondeo y coherencia presupuesto–resultado se evalúan, pero no se enseñan en el material teórico antes del taller.
- **«Cobertura» tiene tres sentidos:** factor/probabilidad/intervalo GUM; alcance cubierto por una evidencia; y «matriz de cobertura» como artefacto del curso. Conviene reservar **cobertura** para el sentido metrológico GUM y usar **alcance de la evidencia** para lo demás.
- **El glosario no funciona como puerta de entrada:** está como sección tardía del handout y omite términos de alta frecuencia práctica (SRP, repetibilidad, precisión intermedia, reproducibilidad, calibración/verificación/ajuste, doble conteo, escala completa, sesgo, patrón de transferencia, deriva de cero y de span).

Esta inversión **no se resuelve sola** al separar capas. Requiere decisión explícita. Dos salidas:

1. **Capa R como prelectura obligatoria** (`O3_H00` + `O3_H01` + glosario como lectura mínima). Riesgo: depende de que lean; alto en operadores de red.
2. **Bloque M0 de vocabulario, 15–20 min, antes de M1:** mensurando, error/corrección/incertidumbre, estándar/combinada/expandida, trazabilidad, Tipo A/B en versión mínima. M3 pasa a profundizar, no a introducir. Costo: 20 min de los 78 min de reserva logística. El glosario de capa R queda como respaldo.

La opción 2 es robusta a que nadie lea nada antes; es la recomendada si el curso se dicta a operadores sin envío previo de material. Complemento en cualquier caso: mapa inicial corto de términos indispensables + definiciones completas justo antes de operar con cada concepto + glosario final de consulta.

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

**M5, M6 y M8 no tienen discurso redactado.** Tienen contenido, no narración. Para ellos, la capa 1 no se puede extraer porque no hay qué extraer: hay que escribirla.

---

## 8. Hallazgo lateral: `solo_md/` es una capa derivada fuera de control

`solo_md/` replica el árbol completo (592 K) con los enlaces Markdown desanclados, para lectura fuera del repositorio.

- **No lo genera `build_paquete_html.py`** — `grep solo_md build_paquete_html.py` → 0 resultados.
- **No está en git** — sin historial; aparece como `??` en `git status`.
- **Ya divergió** de `modulos/`: M1 14 líneas, M3 16, M2 12, M7 10, M8 10, M4 8, M5 6, M6 2.

El delta es sistemático y benigno —quita `[texto](enlace)` y deja el texto—, pero la copia es manual y sin verificación. Es exactamente el patrón que produjo el problema del handout: dos archivos contando lo mismo, uno derivando en silencio. Precedente positivo: `build_paquete_html.py` + `pandoc_rewrite_links.lua` ya generan `curso_paquete_completo.html` con validación de archivos, filas, anclas e IDs únicos. La infraestructura de derivación existe; `solo_md/` simplemente no la usa.

---

## 9. Mecanismo propuesto: una fuente, marcado por audiencia

Fuente única por módulo (= capa 0, capítulo del meta maestro). Las demás capas se generan quitando bloques. Si se necesita una lectura continua del meta maestro, se ensambla desde M1–M8 (más M0); nunca se mantiene otra copia manual.

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

## 10. Dueño conceptual por módulo

Cada concepto operativo debe tener un módulo dueño; el material del participante debe introducirlo antes de exigir su uso. Otros módulos pueden recordarlo, no redefinirlo en paralelo:

- **M0 (nuevo):** vocabulario mínimo para arrancar (mensurando, error/corrección/incertidumbre, estándar/combinada/expandida, trazabilidad, Tipo A/B básico);
- **M1:** trazabilidad, mensurando y vocabulario base;
- **M2:** modelo de medición y coeficientes de sensibilidad;
- **M3:** incertidumbre estándar, Tipo A/B, PDFs y combinación;
- **M4:** presupuesto, contribuciones, doble conteo, `U`, `k`, cobertura (sentido GUM) y redondeo;
- **M5:** patrones, regresión, residuos y alcance de la evidencia;
- **M6:** modelo NOx, interferencias y covarianza;
- **M7:** integración, declaración del resultado e informe GUM;
- **M8:** validación opcional mediante MCM.

---

## 11. Reglas de derivación y control

### Regla 1. Una idea nueva nace en la capa meta
Ninguna diapositiva, protocolo o solucionario introduce silenciosamente un concepto que no esté reconocido en la capa 0. Si aparece por primera vez en una diapositiva visual, hay ruptura del flujo de derivación.

### Regla 2. Cada capa tiene autoridad definida
La capa 0 es canónica para contenido técnico, definiciones, ecuaciones, notación e intención pedagógica. La capa 1 es canónica para orden, redacción y experiencia del participante. Toda corrección técnica se incorpora primero a la capa 0 y después se propaga.

### Regla 3. Las diapositivas reducen, no amplían
Guion y diapositivas pueden condensar, ilustrar y jerarquizar. No agregan teoría ausente del material teórico.

### Regla 4. Los anexos amplían sin interrumpir
El relato principal es comprensible sin leer la capa R. Los anexos dan profundidad; no reparan huecos básicos.

### Regla 5. Fichas y protocolos repiten según su función
Las fichas repiten solo lo necesario para consulta rápida. Los protocolos repiten lo necesario para ejecutar una actividad de principio a fin. Ambos conservan notación, terminología y criterios del material principal; la duplicación es deliberada y declarada.

### Regla 6. Las respuestas permanecen fuera del entregable principal
La capa 0 conserva respuesta breve, resultado esperado y propósito pedagógico. El solucionario conserva resolución completa, cálculos paso a paso, criterios de corrección y variantes aceptables. Ninguno se anticipa en la capa 1.

### Regla 7. Cada concepto operativo tiene un dueño
Mapa de la sección 10. Un concepto se define una vez; en otras capas se referencia.

---

## 12. Inventario de deuda

| # | Deuda | Impacto | Esfuerzo |
|---|---|---|---|
| D1 | M5, M6, M8 sin `Guion dictable` — capa 1 inexistente ahí | **bloqueante** para capas 1–3 | alto: redactar discurso |
| D2 | Tres convenciones distintas para el bloque de discurso | bloquea derivación mecánica | bajo: renombrar |
| D3 | `handout/gum_o3/` duplica ~520 líneas de capa 1 | confusión de roles, riesgo de drift | medio: podar a ~350 líneas de capa R real |
| D4 | Rol del handout nunca declarado (prelectura / aula / consulta) | impide decidir el orden de términos | bajo: decisión + 1 párrafo en README |
| D5 | Inversión de vocabulario M1/M2 ↔ M3; `u_i → u_c → U` sin dueño claro | pedagógico, afecta a todos los participantes | medio: bloque M0 de 15–20 min |
| D6 | `solo_md/` derivado a mano, fuera de git, ya divergido | drift silencioso | bajo: generar o borrar |
| D7 | 27 `Idea fuerza` para ~120 subbloques-equivalentes | capa 2 arranca con ~20 % de semillas | alto, pero mecánico tras D2 |
| D8 | README presenta handout O₃ y NOx como equivalentes siendo asimétricos | expectativa falsa | bajo: 1 tabla en README |
| D9 | Informe GUM §7 exigido en M7 antes de enseñarse en la capa 1 | participante no puede producir resultado auditable con lo aprendido en aula | medio: incorporar checklist y criterios de cobertura/redondeo al material teórico antes del taller |
| D10 | Colisión semántica de «cobertura» (GUM / evidencia / matriz del curso) | confusión terminológica | bajo: renombrar los dos usos no metrológicos («alcance de la evidencia») |
| D11 | Glosario tardío y con omisiones de alta frecuencia (SRP, repetibilidad, precisión intermedia, sesgo, deriva…) | vocabulario informal nunca queda fijado | medio: mapa inicial + definiciones in situ + glosario final |

---

## 13. Plan propuesto

Orden por dependencia, no por importancia.

1. **Declarar las cinco capas** en `README.md` y fijar la convención de bloques de §9. Renombrar `handout/` → `referencia/` o declarar explícitamente su rol de capa R. Resuelve D4 y D8. Sin tocar contenido.
2. **Piloto en M5** — el módulo más incompleto: 0 subbloques, 1 `Idea fuerza`, sin discurso. Si el esquema aguanta ahí, aguanta en todos. Ataca D1 y D2 en el peor caso.
3. **`build_capas.py`**, siguiendo el patrón de `build_paquete_html.py`. `solo_md/` pasa a ser salida generada. Resuelve D6.
4. **Propagar el esquema** a M1–M4 y M7 (tienen discurso, solo falta etiquetar), después a M6 y M8 (hay que redactarlo). Cierra D1, D2.
5. **Derivar la capa 1 completa** (material teórico del participante, continuo y limpio) y con ella incorporar al relato: la cadena `u_i → u_c → U = k·u_c` con dueño claro, los elementos del informe GUM antes del taller de M7, y el renombrado «alcance de la evidencia». Cierra D9 y D10, y la parte de D5 referida a `U` y `k`.
6. **Podar el handout O₃** a capa R real: glosario, tablas de PDFs, ley de propagación, checklist de informe. Las 30 anclas existentes siguen sirviendo. Las piezas básicas ya quedaron absorbidas por la capa 1 en el paso anterior. Cierra D3.
7. **Decidir el orden de términos:** bloque M0 de vocabulario (recomendado) o prelectura obligatoria de capa R; en ambos casos, glosario ampliado como respaldo. Cierra D5 y D11.
8. **Capas 2 y 3** al final, cuando la derivación ya es mecánica. Cierra D7. Estimación de volumen: 462 min de curso obligatorio, a 2–3 min por diapositiva ⇒ **150–200 diapositivas**.

Arquitectura resultante:

```text
CAPA 0 — META MAESTRO (fuente única por módulo, ensamblable)
    ├── CAPA 1 — MATERIAL TEÓRICO DEL PARTICIPANTE (generado)
    │       └── CAPA 2 — GUION TEXTUAL DE DIAPOSITIVAS (generado)
    │               └── CAPA 3 — DIAPOSITIVAS VISUALES (generadas)
    ├── CAPA R — REFERENCIA DE CONSULTA (glosario, tablas, checklists)
    ├── SOLUCIONARIOS PRIVADOS DEL INSTRUCTOR
    ├── FICHAS OPERATIVAS / AYUDAS DE CAMPO
    └── PROTOCOLOS PRÁCTICOS E01–E16 (autonomía controlada)
```

---

## 14. Lo que NO está mal

Para que el diagnóstico no se lea como una condena:

- **El contenido técnico es sólido y avanzado**, trazado a fuente con página exacta (JCGM, QUAM, EN 14211, EPA, NISTIR, BIPM.QM-K1). No se requiere reconstrucción técnica.
- **El control documental es riguroso:** la nota sobre APOA-370 vs. APNA-370 evita atribuir especificaciones equivocadas.
- **Los datasets son reproducibles** con semilla declarada (`20260819`).
- **La separación curso teórico / práctica de laboratorio**, con entregables evaluados independientes (M7 y E15), está bien argumentada.
- **Los módulos ya son una base meta avanzada:** minutaje, errores frecuentes, resultados esperados y decisiones docentes existen; solo falta declararlos como tal.
- **`build_paquete_html.py` ya valida** archivos, filas, columnas, MathML, anclas, IDs únicos y ausencia de recursos externos. Es la base sobre la que se monta `build_capas.py`.
- **`handout/no_nox/` ya es capa R correcta.** Sirve de modelo para podar la de O₃.

Valoración global del desfase (esfuerzo editorial, no calidad técnica):

| Aspecto | Estado |
|---|---|
| Conocimiento técnico | avanzado |
| Versión meta (capa 0) | avanzada, fusionada con capa 1 |
| Narrativa entregable (capa 1) | incompleta y no extraíble en 4 de 8 módulos |
| Clasificación de anexos (capa R) | ambigua (O₃ mezclado; NOx correcto por accidente) |
| Pipeline hacia diapositivas (capas 2–3) | no arrancado |

El desfase es **de una capa y media**, no de arquitectura equivocada: contenido sobra, capa 0 y 1 están fusionadas, capas 2 y 3 no arrancaron.

---

## 15. Conclusión final

La inquietud inicial —¿se deben aclarar antes los términos metrológicos? ¿los módulos omiten contenido que quedó solo en los handouts? ¿los módulos ya son su propio handout?— era válida, y la respuesta combinada es:

1. los módulos no están simplemente sobrecargados: son la capa meta (capa 0) sin declarar, y esa densidad es coherente con su función real;
2. la capa 1 (material teórico del participante) todavía no existe como producto único, limpio y continuo; en M5, M6 y M8 hay que redactarla;
3. el handout O₃ mezcla contenido básico que debe incorporarse al relato principal con material avanzado que debe quedar como anexo; el handout NOx ya es, de facto, la capa R correcta;
4. los desajustes pedagógicos —vocabulario invertido M1/M2 ↔ M3, `u → u_c → U` sin dueño, informe GUM exigido antes de enseñarse, colisión de «cobertura»— son reales y no desaparecen solos al separar capas; requieren el bloque M0 y el mapa de dueños conceptuales;
5. el mecanismo correcto es una fuente única por módulo con marcado por audiencia y derivación generada (`build_capas.py`), no archivos paralelos mantenidos a mano — el handout y `solo_md/` son el precedente negativo;
6. las capas 2 y 3 se construyen al final, cuando la derivación sea mecánica, no antes.

La causa principal no es exceso de contenido ni una mala concepción del curso: es la ausencia de una arquitectura documental explícita. El curso está avanzado en conocimiento y en preparación docente; su siguiente etapa natural es convertir esa riqueza meta en una secuencia controlada de productos, cada uno con destinatario, propósito y profundidad definidos.
