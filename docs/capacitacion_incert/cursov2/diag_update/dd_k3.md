# Diagnóstico final y arquitectura documental — cursov2

**Fecha:** 2026-08-28  
**Alcance:** `docs/capacitacion_incert/cursov2/`  
**Propósito:** consolidar los diagnósticos `diag_opu.md` (evidencia cuantificada) y `diag_sol.md` (arquitectura objetivo) en una propuesta única.  
**Estado:** diagnóstico. No se modificó ningún archivo del curso.

---

## 1. Conclusión en una frase

El paquete no tiene problema de contenido: tiene problema de **capas sin declarar y sin reglas de derivación**. Los módulos M1–M8 funcionan de facto como versión meta del autor-instructor, comparten archivo con el material teórico del participante, el handout O₃ intenta fallidamente extraer ese material teórico, y las capas de diapositivas todavía no existen.

---

## 2. El modelo de capas del autor

Flujo de producción, en orden:

| # | Capa | Pregunta rectora | Descripción |
|---|---|---|---|
| **0** | **Meta maestro (autor/instructor)** | ¿Qué necesito para enseñar bien este bloque? | Versión más cargada: teoría completa, discurso, minutaje, facilitation, errores frecuentes, soluciones, variantes, referencias exactas. Privada. |
| **1** | **Material teórico del participante** | ¿Qué necesita leer el participante para comprender el curso después de la sesión? | Prosa completa, hilo narrativo continuo. Se deriva de capa 0 quitando bloques, no reescribiendo. |
| **2** | **Guion textual de diapositivas** | ¿Qué necesita estar escrito en pantalla? | Texto telegráfico, una idea por diapositiva. Derivado de capa 1. |
| **3** | **Diapositivas visuales** | ¿Cómo hacer visible la idea? | Capa 2 + imágenes, diagramas, composición. No introduce teoría nueva. |
| **R** | **Referencia de consulta** | Artefacto perpendicular al flujo | Glosario, tablas, fórmulas, checklists. Lo que el operador abre meses después. |

Relación entre 0 y 1: **superconjunto**, no hermanos. Toda idea nueva nace en capa 0.

---

## 3. Estado real de cada capa

| Capa | Dónde vive hoy | Volumen | Estado |
|---|---|---:|---|
| 0 — Meta | disperso dentro de `modulos/` + `modulos/soluciones/` | 607 + 1571 líneas | existe, **fusionado con capa 1** |
| 1 — Teórico participante | embebido en `modulos/`, sin separar | ~818 líneas (mezcladas) | existe, **no extraíble** |
| 2 — Diapositivas texto | — | 0 | **no existe** |
| 3 — Diapositivas finales | — | 0 | **no existe** |
| R — Referencia | `handout/gum_o3/` + `handout/no_nox/` | 869 + 120 líneas | existe, **contaminada con capa 1 duplicada** (O₃) / correcta (NOx) |

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
| Ficha + Objetivos | 201 | solo instructor |
| Guion de exposición | 818 | **mezclado** |
| Ejercicio/actividad | 245 | mezclado |
| Errores frecuentes + Cierre | 161 | solo instructor |

**42 % de `modulos/` es meta pura.** Dentro del guion de exposición conviven marcadores de capas distintas:

| Marcador | Ocurrencias | Capa |
|---|---:|---|
| `acumulado` (minutaje) | 45 | 0 |
| `Idea fuerza:` | 27 | 2 (semilla) |
| `Apoyo en el handout:` | 17 | 0 |
| `Referencias exactas:` | 7 | 0 + 1 |
| `Resultado esperado:` | 7 | 0 |
| `Enlace con la práctica:` | 5 | 0 |

Consecuencia: mismo archivo sirve a dos lectores con necesidades opuestas. El instructor quiere más carga; el participante quiere menos. Esto no es defecto editorial — es rol meta no declarado — pero hace imposible extraer capa 1 limpia.

---

## 5. El handout O₃ es un intento fallido de extraer capa 1

`handout/gum_o3/` no es capa 0, ni 2, y solo parcialmente es R. Es **reescritura** de capa 1, no extracción.

Solapamiento verificado:

- M3 §3.3 (PDFs y divisores) ≈ `O3_H03_tipo_b_pdfs.md`
- M2 §3.3 (coeficientes de sensibilidad) ≈ `O3_H04_propagacion_guf.md`
- M7 bloque 6 (informe) ≈ `O3_H07_informe_gum.md`
- M1 §3.1 (trazabilidad) ≈ `O3_H01 §1.5`

Contenido genuinamente único (capa R legítima):

- `O3_H08_glosario.md` — 23 términos definidos en ningún módulo
- `O3_H03` — tabla de PDFs con divisores
- `O3_H04` — ley de propagación en forma general
- `O3_H07` — checklist de informe GUM §7

De 869 líneas, ~350 son capa R real. El resto duplica narrativa.

**Asimetría O₃ / NOx.** `handout/no_nox/` tiene 120 líneas en 10 archivos; M6 lo cita una sola vez. De facto funciona como capa R pura — checklist y control documental, sin duplicar M6. Está mejor alineado por accidente, y sirve de modelo para podar O₃. Pero `README.md` presenta ambas familias como equivalentes. Además, en su función real NOx opera como **ficha operativa / ayuda de campo**, rol que debe declararse explícitamente.

**Vacío de instrucción de uso.** Búsqueda de `prelectura`, `lectura previa`, `antes del curso`, `leer.*handout` sobre `modulos/`, `README.md`, `diseno_curso_v2.md` y `handout/`: **0 resultados**. Nada dice si la referencia se entrega antes, durante o después.

---

## 6. Inversión del vocabulario metrológico

El vocabulario formal vive en `O3_H01` y en el glosario, pero la secuencia de aula lo usa operativamente antes:

| Momento | Términos usados | Dónde están definidos |
|---|---|---|
| M1 (min 0–35) | incertidumbre del patrón / del analizador / del valor transferido, corrección, incertidumbre residual, doble conteo, covarianza | `O3_H01` — remitido, no dictado |
| M2 (min 35–83) | mensurando, coeficiente de sensibilidad | `O3_H01`, `O3_H04` |
| M3 (min 83–137) | **recién aquí** Tipo A/B, PDF, combinación cuadrática | el módulo mismo |

`M1:6` se autodeclara portador del vocabulario, pero `M1:111` lo delega al handout, documento cuyo momento de lectura nadie definió. La cadena operativa:

```text
u_i → u_c → U = k·u_c
```

carece de dueño docente claro: `U` y `k` aparecen en ejercicios antes de su introducción formal.

**Solución recomendada: bloque M0 de vocabulario, 15–20 min**, antes de M1 (mensurando, error/corrección/incertidumbre, estándar/combinada/expandida, trazabilidad, Tipo A/B mínimo). Alternativa: prelectura obligatoria de capa R — riesgo alto con operadores de red. La estructura terminológica correcta combina tres piezas: mapa inicial corto, definiciones justo antes de operar cada concepto, glosario final de consulta. Cada concepto operativo debe tener un **módulo dueño**.

Distribución objetivo de dueños:

- M1: trazabilidad, mensurando, vocabulario base
- M2: modelo de medición y coeficientes de sensibilidad
- M3: incertidumbre estándar, Tipo A/B, PDFs, combinación
- M4: presupuesto, contribuciones, doble conteo, `U`, `k`, cobertura, redondeo
- M5: patrones, regresión, residuos, alcance de evidencia
- M6: modelo NOx, interferencias, covarianza
- M7: integración, declaración del resultado, informe GUM
- M8: validación opcional mediante MCM

Otros problemas pedagógicos que permanecen tras separar capas:

- **Informe GUM exigido antes de enseñarse.** M7 pide resultado auditable conforme a GUM §7, pero la lista completa de elementos vive en `O3_H07`. Cobertura, redondeo y coherencia presupuesto/resultado deben estar en capa 1 antes del taller.
- **Colisión del término "cobertura".** Usado como factor/probabilidad/intervalo (GUM), alcance de evidencia y "matriz de cobertura" del curso. Reservar *cobertura* para sentido GUM; usar *alcance de evidencia* para lo demás.
- **Glosario late y con vacíos.** Situado como sección tardía; omite SRP, repetibilidad, precisión intermedia, reproducibilidad, calibración/verificación/ajuste, doble conteo, escala completa, sesgo, patrón de transferencia, deriva de cero y de span.

---

## 7. Capa 1 no extraíble en 4 de 8 módulos

Sin estructura regular, la derivación hacia capas 1–3 no es automatizable:

| Módulo | Subbloques `### 3.x` | `Idea fuerza` | Bloque de discurso |
|---|---:|---:|---|
| M1 | 5 | 5 | `Guion dictable` ×5 |
| M2 | 4 | 5 | `Guion dictable` ×4 |
| M3 | 4 | 5 | `Guion dictable` ×4 |
| M4 | 5 | 5 | `Guion dictable` ×5 |
| M5 | **0** | **1** | **ninguno** — prosa plana |
| M6 | 4 | **1** | **ninguno** |
| M7 | 0 (`### Bloque N`) | 4 | `Párrafo dictable` ×4 |
| M8 | 0 | 1 | **ninguno** |

Tres nombres distintos para el mismo objeto y dos esquemas de encabezado. **M5, M6 y M8 no tienen discurso redactado**: para ellos, capa 1 no se extrae, hay que escribirla.

---

## 8. Hallazgo lateral: `solo_md/`, capa derivada fuera de control

`solo_md/` (592 K) replica el árbol con enlaces Markdown desanclados. No lo genera `build_paquete_html.py`, no está en git, y ya divergió (delta sistemático 2–16 líneas por módulo). Es exactamente el patrón que produjo el problema del handout: dos copias contando lo mismo, una derivando en silencio. Precedente positivo: `build_paquete_html.py` + `pandoc_rewrite_links.lua` ya validan archivos, filas, anclas e IDs. La infraestructura de derivación existe; `solo_md/` no la usa.

---

## 9. Arquitectura documental objetivo

```text
META MAESTRO (capa 0, privada)
    ├── MATERIAL TEÓRICO DEL PARTICIPANTE (capa 1)
    │       └── GUION TEXTUAL DE DIAPOSITIVAS (capa 2)
    │               └── DIAPOSITIVAS VISUALES (capa 3)
    ├── ANEXOS TÉCNICOS (capa R avanzada)
    ├── FICHAS OPERATIVAS / AYUDAS DE CAMPO (capa R práctica)
    ├── PROTOCOLOS PRÁCTICOS (E01–E16, autonomía controlada)
    └── SOLUCIONARIOS DEL INSTRUCTOR (privados)
```

Destinatarios y funciones:

| Producto | Base | Destinatario / uso |
|---|---|---|
| Meta maestro | M1–M8, gobernados como capítulos coordinados; ensamblado siempre generado, nunca copia manual | autor e instructor; preparar, impartir, actualizar |
| Material teórico entregable | derivado del meta maestro; narrativa limpia y continua, capítulos M1–M8 | participante; fuente principal |
| Anexos técnicos | contenido avanzado del handout O₃ (autocorrelación, t desplazada, Welch–Satterthwaite, Cholesky, MCM extendido) | profundización; no obligatorio para recorrido principal |
| Fichas operativas | partes útiles del handout NOx: checklists, fórmulas rápidas, criterios, controles documentales | participante en práctica, operación o auditoría; consulta rápida |
| Protocolos prácticos | E01–E16 | conductor completo de la actividad; repetición deliberada y gobernada, terminología del material principal |
| Solucionarios | resolución completa, criterios de corrección, variantes | instructor; desarrollo completo |
| Guion textual | derivado de capa 1 | títulos, frases cortas, estructura por diapositiva |
| Diapositivas visuales | derivadas del guion | diseño final, imágenes, diagramas |

La regla del corte básico vs. avanzado: pertenece a capa 1 todo lo necesario para seguir los módulos obligatorios y resolver las actividades requeridas; pertenece a anexos aquello que amplía, deriva o trata casos especiales sin ser necesario para el recorrido principal.

---

## 10. Mecanismo de derivación: fuente única marcada por audiencia

Fuente única por módulo (= capa 0). Las demás capas se generan **quitando bloques**.

Convención única por subbloque (extensión regular y legible por máquina de lo que ya existe de facto):

```markdown
### 3.N Título — 0:mm a 0:mm; acumulado 0:mm      ← capa 0 (minutaje)

**Idea fuerza:**            ← capa 2 (título de diapositiva)
**Guion dictable:**         ← capas 0 y 1 (discurso; texto del material teórico)
**Puntos:**                 ← capa 2 (3–5 viñetas)
**Apoyo visual:**           ← capa 3 (qué diagrama, foto, esquema)
**Nota de facilitación:**   ← capa 0
**Referencias exactas:**    ← capa 0 completa; capa 1 en versión corta
**Apoyo en la referencia:** ← capa 0 (puntero a capa R)
```

Un solo `build_capas.py` (patrón de `build_paquete_html.py`) emite:

| Salida | Regla |
|---|---|
| capa 0 | el archivo tal cual |
| capa 1 | `Guion dictable` + referencias cortas; sin minutaje, sin facilitation, sin errores frecuentes, sin punteros internos |
| capa 2 | `Idea fuerza` + `Puntos` |
| capa 3 | capa 2 + `Apoyo visual` como marcador de imagen |
| `solo_md/` | cualquiera de las anteriores, enlaces desanclados |

## 11. Reglas de derivación y control

1. **Una idea nueva nace en la capa meta.** Ninguna diapositiva, protocolo o solucionario introduce silenciosamente conceptos no reconocidos en capa 0.
2. **Autoridad definida por capa.** Meta maestro canónico para contenido técnico, definiciones, notación e intención pedagógica; material teórico canónico para orden y experiencia del participante; correcciones entran primero en capa 0 y se propagan.
3. **Diapositivas reducen, no amplían.** Condensan, ilustran, jerarquizan; no agregan teoría ausente de capa 1.
4. **Anexos amplían sin interrumpir.** El relato principal se comprende sin leerlos; no reparan huecos básicos.
5. **Fichas y protocolos repiten según su función.** Fichas: consulta operativa rápida. Protocolos: ejecución completa de principio a fin. Ambos conservan notación y criterios de capa 1.
6. **Respuestas fuera del entregable.** Meta maestro conserva respuesta breve y resultado esperado; solucionario conserva desarrollo completo; ninguno anticipa en capa 1.
7. **Cada concepto operativo tiene un dueño.** Distribución de §6; otros módulos pueden recordarlo, no redefinirlo paralelamente.

---

## 12. Inventario de deuda

| # | Deuda | Impacto | Esfuerzo |
|---|---|---|---|
| D1 | M5, M6, M8 sin discurso — capa 1 inexistente ahí | **bloqueante** para capas 1–3 | alto: redactar |
| D2 | Tres convenciones distintas para el bloque de discurso | bloquea derivación mecánica | bajo: renombrar |
| D3 | `handout/gum_o3/` duplica ~520 líneas de capa 1 | confusión de roles, riesgo de drift | medio: podar a ~350 |
| D4 | Rol del handout nunca declarado (prelectura / aula / consulta) | impide decidir orden de términos | bajo: decisión + 1 párrafo en README |
| D5 | Inversión de vocabulario M1 ↔ M3 | pedagógico, afecta a todos | medio: bloque M0 de 15–20 min |
| D6 | `solo_md/` derivado a mano, fuera de git, ya divergido | drift silencioso | bajo: generar o borrar |
| D7 | 27 `Idea fuerza` para ~120 subbloques | capa 2 arranca con ~20 % de semillas | alto, mecánico tras D2 |
| D8 | README presenta handout O₃ y NOx como equivalentes siendo asimétricos | expectativa falsa | bajo: 1 tabla en README |

Valoración del desfase (esfuerzo editorial, no calidad técnica):

| Área | Desfase |
|---|---|
| Contenido técnico | **bajo** — ya existe |
| Versión meta | **bajo a medio** — base sólida, falta declarar rol |
| Material teórico del participante | **medio a alto** — repartido entre fuentes, sin narrativa limpia |
| Anexos y ayudas operativas | **medio** — funciones mezcladas bajo "handout" |
| Guion textual y diapositivas | **alto** — pipeline inexistente |

Diagnóstico global: no se requiere reconstruir el curso; se requiere reorganización editorial y cadena de derivación explícita. Conocimiento: avanzado; meta: avanzada; narrativa entregable: incompleta; clasificación de anexos: ambigua; pipeline de diapositivas: no consolidado.

---

## 13. Plan propuesto

Orden por dependencia, no por importancia.

1. **Declarar las capas** en `README.md` y fijar la convención de bloques de §10. Declarar el rol de capa R (referencia) y la asimetría O₃/NOx. Resuelve D4, D8. Sin tocar contenido.
2. **Piloto en M5** — módulo más incompleto (0 subbloques, 1 `Idea fuerza`, sin discurso). Si el esquema aguanta ahí, aguanta en todos. Ataca D1, D2 en el peor caso.
3. **`build_capas.py`**, siguiendo el patrón de `build_paquete_html.py`. `solo_md/` pasa a salida generada. Resuelve D6.
4. **Propagar el esquema** a M1–M4 y M7 (tienen discurso, solo falta etiquetar), después a M6 y M8 (redactar discurso). Cierra D1, D2.
5. **Podar el handout O₃** a capa R real: glosario, tabla de PDFs, ley de propagación, checklist de informe. Las 30 anclas existentes siguen sirviendo. Cierra D3.
6. **Resolver orden de términos**: bloque M0 de vocabulario (recomendado) o prelectura obligatoria de capa R. Cierra D5.
7. **Capas 2 y 3** al final, cuando la derivación ya es mecánica. Cierra D7.

Estimación para capas 2 y 3: 462 min de curso obligatorio, a 2–3 min por diapositiva ⇒ **150–200 diapositivas**.

---

## 14. Lo que NO está mal

- Contenido técnico sólido, trazado a fuente con página exacta (JCGM, QUAM, EN 14211, EPA, NISTIR, BIPM.QM-K1).
- Control documental riguroso (nota APOA-370 vs. APNA-370).
- Datasets reproducibles con semilla declarada (`20260819`).
- Separación curso teórico / práctica, con entregables evaluados independientes (M7, E15).
- `build_paquete_html.py` ya valida archivos, filas, columnas, MathML, anclas, IDs únicos y ausencia de recursos externos: base para `build_capas.py`.
- `handout/no_nox/` ya es capa R correcta: modelo para podar O₃.

El desfase es de **una capa y media**, no de arquitectura equivocada: contenido sobra, capas 0 y 1 están fusionadas, capas 2 y 3 no arrancaron.

---

## 15. Conclusión

La inquietud inicial era válida: existe sensación de que módulos y handouts se repiten y completan entre sí sin fronteras claras. La causa no es exceso de contenido ni mala concepción — es ausencia de arquitectura documental explícita con reglas de derivación.

1. Los módulos no están sobrecargados; son la base avanzada del meta maestro.
2. El material teórico entregable todavía no existe como producto único y limpio.
3. El handout O₃ mezcla contenido básico (a integrar en capa 1) con avanzado (anexos).
4. El handout NOx funciona como ficha operativa y debe declararse así.
5. Vocabulario inicial, cadena `u → u_c → U`, cobertura, redondeo e informe GUM requieren mejor ubicación en la narrativa.
6. Guion textual y diapositivas deben derivarse del material teórico estabilizado mediante `build_capas.py`, no de fuentes paralelas.
7. `solo_md/` debe generarse o borrarse; derivación manual mata.
8. El trabajo pendiente es editorial y arquitectónico, no reconstrucción técnica.

El curso está avanzado en conocimiento y preparación docente. Su siguiente etapa es convertir esa riqueza meta en una secuencia gobernada de productos, cada uno con destinatario, propósito y profundidad definidos.
