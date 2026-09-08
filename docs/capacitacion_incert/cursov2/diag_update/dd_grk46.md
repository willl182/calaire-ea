# Diagnóstico final de arquitectura documental — cursov2

**Fecha:** 2026-08-28  
**Directorio:** `docs/capacitacion_incert/cursov2/`  
**Estado:** propuesta de diagnóstico. No se modificó ningún archivo del curso.  
**Fuentes:** `diag_sol.md` (evidencia cuantificada, convención de bloques, pipeline, inventario de deuda) y `diag_opu.md` (función meta, taxonomía de productos, diagnóstico pedagógico persistente, reglas de derivación).

---

## 0. Cómo se fusionan las dos lecturas

Los dos diagnósticos no compiten. Responden preguntas distintas y fallan si se usan solos.

| | `diag_sol.md` | `diag_opu.md` |
|---|---|---|
| Pregunta que responde | ¿Qué hay en disco y cómo extraerlo sin drift? | ¿Qué productos deben existir, para quién, y qué huecos pedagógicos quedan? |
| Fortaleza | Conteos, marcadores, solapamientos verificados, esquema legible por máquina, plan por dependencia | Función meta, preguntas rectoras, corte básico/avanzado, dueños conceptuales, reglas de autoridad |
| Ceguera si se usa solo | Tratar capa 1 como recorte mecánico del `Guion dictable` (M5, M6 y M8 no tienen qué recortar; el relato continuo entre módulos no nace del recorte) | Arquitectura de ocho productos sin mecanismo de producción (se reescribe a mano y se recrea el drift del handout) |

Este documento toma la evidencia y el pipeline de `diag_sol.md`, la taxonomía y las reglas de `diag_opu.md`, y **resuelve las tensiones** en lugar de dejarlas como alternativas. Las decisiones están en §2 y §8.

---

## 1. Conclusión en una frase

El curso no tiene un problema de contenido: tiene un problema de **capas sin declarar**. La versión meta ya está escrita y fusionada con el entregable del participante; el handout O₃ intenta extraer ese entregable reescribiéndolo; las diapositivas no existen; y varios conceptos se usan en aula antes de enseñarse. El trabajo pendiente es editorial y de derivación, no una reconstrucción técnica.

---

## 2. Decisiones que esta propuesta toma

Estas no son opciones aplazadas. Son el criterio con el que se lee el resto.

1. **Eje de derivación 0 → 1 → 2 → 3**, más productos perpendiculares (anexos, fichas, protocolos, solucionarios). No es un modelo de cinco capas *o* de ocho productos: el eje es el flujo de autoría; los perpendiculares son hermanos del meta, no etapas del mismo flujo.
2. **Capa 1 se obtiene quitando bloques de capa 0, no reescribiendo.** Después del recorte hace falta un pase corto de continuidad entre módulos. El recorte evita el drift; el pase evita un manual hecho de fragmentos.
3. **El handout O₃ se parte, no se borra.** Lo básico (vocabulario mínimo, cadena `u → u_c → U`, cobertura, redondeo, elementos del informe GUM) migra al material teórico. Lo avanzado permanece como anexo. Las anclas existentes se conservan.
4. **El handout NOx no se simetriza con el de O₃.** Se declara como ficha operativa / ayuda de campo. Ya está más cerca de ese rol que el de O₃.
5. **Entrada terminológica en tres piezas, no un glosario dictado.** Mapa inicial de 15–20 min (M0, tomado de la reserva logística de 78 min, no de M1–M7); definición completa justo antes de operar cada concepto, con un módulo dueño; glosario de consulta en la referencia. La prelectura de la referencia es complemento, no sustituto: el curso debe dictarse bien aunque nadie haya leído nada.
6. **Piloto en M5**, el módulo más incompleto. Si el esquema aguanta ahí, aguanta en todos.
7. **Diapositivas al final.** Producirlas antes de estabilizar capa 1 consolida inconsistencias y multiplica revisión.
8. **«Cobertura» se reserva al sentido GUM.** Para el resto se usa **alcance de la evidencia**.

---

## 3. Punto de partida

La evaluación comenzó con tres inquietudes:

1. si los términos metrológicos debían aclararse antes de iniciar los módulos;
2. si los módulos omitían contenido importante que había quedado únicamente en los handouts;
3. si los módulos ya funcionaban, en la práctica, como su propio handout.

La primera lectura mostraba una mezcla de funciones. Los módulos contienen teoría, discurso, minutaje, instrucciones docentes, ejercicios, resultados y errores frecuentes. El handout de O₃ contiene tanto conceptos básicos como desarrollos avanzados. El handout de NOx resume parte de M6, pero no alcanza su profundidad. Los protocolos prácticos vuelven a explicar algunos conceptos para poder usarse de forma autónoma.

Con esa información parecía que los módulos estaban sobrecargados y que competían con los handouts como material del participante. Esa interpretación era incompleta: faltaba declarar la **versión meta del curso**.

Al reconocerla, cambia el diagnóstico. La densidad, el minutaje, las respuestas y las instrucciones de facilitación no son defectos por sí mismos: son características coherentes con una versión meta. El problema real es que ese rol no está declarado y no existe todavía una derivación limpia hacia los demás productos.

---

## 4. Modelo de trabajo

### 4.1 Eje de derivación

Relación entre 0 y 1: **superconjunto, no hermanos**. Capa 1 se obtiene *quitando* bloques de capa 0. Toda idea nueva nace en 0. Las diapositivas se derivan de 1, no de una colección dispersa de módulos y handouts.

| # | Capa | Pregunta rectora | Qué es |
|---|---|---|---|
| **0** | **Meta maestro** (autor / instructor, privado) | ¿Qué necesito saber, recordar y tener disponible para enseñar bien este bloque? | Teoría completa, discurso oral, propósito, secuencia, transiciones, minutaje, facilitación, preguntas, ejercicios y respuestas breves, resultados esperados, errores frecuentes, variantes por grupo, contenido opcional, referencias exactas, criterios de evaluación. |
| **1** | **Material teórico del participante** | ¿Qué necesita leer y conservar el participante para comprender el curso después de la sesión? | Prosa completa, hilo narrativo continuo, definiciones, ecuaciones, ejemplos, figuras y tablas útiles, síntesis, ejercicios sin solución, referencias pertinentes. Sin minutaje, sin «dictar / preguntar / mostrar», sin estrategia de facilitación, sin respuestas ni resultados anticipados. |
| **2** | **Guion textual de diapositivas** | ¿Qué necesita estar escrito en pantalla mientras se explica esta idea? | Texto telegráfico; una idea principal por diapositiva; mismo orden, mismas conclusiones y mismas definiciones operativas que capa 1. |
| **3** | **Diapositivas visuales** | ¿Cómo hacer visible la idea sin convertir la diapositiva en una página del manual? | Capa 2 más imágenes, diagramas, composición, jerarquía visual, revelado progresivo. No introduce teoría nueva. |

Capa 0 no se entrega al participante. Si se necesita una lectura continua del meta, se ensambla desde M1–M8; nunca se mantiene otra copia a mano.

Capa 1 debe poder leerse como un manual breve y continuo. Puede conservar la división M1–M8, pero cada módulo funciona como capítulo de una sola narrativa, no como documento que obliga a consultar otra fuente para completar ideas básicas.

### 4.2 Productos perpendiculares

No son etapas del eje. Nacen del meta y tienen destinatario propio.

```text
META MAESTRO (capa 0, privada)
    ├── MATERIAL TEÓRICO DEL PARTICIPANTE (capa 1)
    │       └── GUION TEXTUAL (capa 2)
    │               └── DIAPOSITIVAS VISUALES (capa 3)
    ├── ANEXOS TÉCNICOS
    ├── FICHAS OPERATIVAS / AYUDAS DE CAMPO
    ├── PROTOCOLOS PRÁCTICOS (E01–E16)
    └── SOLUCIONARIOS DEL INSTRUCTOR
```

| Producto | Base actual | Destinatario y uso |
|---|---|---|
| **Anexos técnicos** | Contenido avanzado de `handout/gum_o3/` | Profundización. No son lectura obligatoria para completar el recorrido principal. |
| **Fichas operativas** | `handout/no_nox/` y checklists de práctica | Consulta rápida en operación, práctica o auditoría. No conducen una actividad completa. |
| **Protocolos prácticos** | `practica/E01`–`E16` | Conducen la ejecución de principio a fin. Repetición deliberada de fórmulas y advertencias; fundamento en capa 1. |
| **Solucionarios** | `modulos/soluciones/` | Instructor. Resolución completa, cálculos, criterios de corrección, variantes. El meta conserva respuesta breve y resultado esperado; el solucionario no es una tercera doctrina. |

Criterio de corte básico / avanzado: pertenece a capa 1 todo lo necesario para seguir los módulos obligatorios y resolver las actividades requeridas. Pertenece a anexos aquello que amplía, deriva o trata casos especiales sin ser necesario para el recorrido principal.

---

## 5. Estado real de cada capa

| Capa / producto | Dónde vive hoy | Volumen | Estado |
|---|---|---:|---|
| 0 — Meta | disperso en `modulos/` + `modulos/soluciones/` | 607 + 1571 líneas | existe, **fusionada con capa 1** |
| 1 — Teórico participante | embebida en `modulos/`, sin separar | ~818 líneas mezcladas | existe, **no extraíble** en 4 de 8 módulos |
| 2 — Guion de diapositivas | — | 0 | **no existe** |
| 3 — Diapositivas visuales | — | 0 | **no existe** |
| Anexos / fichas (hoy «handout») | `handout/gum_o3/` + `handout/no_nox/` | 869 + 120 líneas | O₃ **contaminado** con duplicado de capa 1; NOx ya funciona como ficha |
| Protocolos | `practica/` | — | existen, con autonomía no del todo gobernada |
| Solucionarios | `modulos/soluciones/` | 1571 líneas | existen; reexplican teoría para ser autónomos |

Verificación de ausencia de capas 2 y 3:

```text
find . -iname "*slide*" -o -iname "*diapo*" -o -iname "*.pptx" \
       -o -iname "*reveal*" -o -iname "*beamer*"   →  0 resultados
```

---

## 6. Hallazgos sobre el estado actual

### 6.1 Capa 0 y capa 1 comparten archivo

Reparto de líneas por rol de sección en los ocho módulos:

| Sección | Líneas | Audiencia |
|---|---:|---|
| Ficha + Objetivos (duración, prerrequisitos, materiales, distribución de tiempo) | 201 | solo instructor |
| Guion de exposición | 818 | **mezclado** |
| Ejercicio / actividad (enunciado, organización, tiempo, resultado esperado) | 245 | mezclado |
| Errores frecuentes + Cierre y transición | 161 | solo instructor |

**42 % de `modulos/` es meta pura.** El 57 % restante tampoco es limpio. Dentro del guion de exposición conviven, contados sobre los ocho módulos:

| Marcador | Ocurrencias | Capa |
|---|---:|---|
| `acumulado` (minutaje) | 45 | 0 |
| `Idea fuerza:` | 27 | 2 (semilla) |
| `Apoyo en el handout:` | 17 | 0 |
| `Referencias exactas:` | 7 | 0 + 1 |
| `Resultado esperado:` | 7 | 0 |
| `Enlace con la práctica:` | 5 | 0 |
| `Referencia integrada` | 4 | 0 + 1 |
| `Organización:` | 3 | 0 |
| `Conexión posterior` | 2 | 0 |
| `Pregunta de control:` | 1 | 0 |

Un mismo archivo sirve a dos lectores con necesidades opuestas. El instructor quiere más carga; el participante quiere menos. Eso no se «limpia» borrando el 42 %: se declara como meta y se deriva capa 1 quitando esos bloques.

Ejemplos de contenido meta que no corresponde al entregable: M2 publica el resultado numérico del ejercicio; M4 entrega valores esperados de `u_c`, `U` y contribución dominante; M8 anticipa resultados y conclusiones de la demostración.

### 6.2 El handout O₃ es una reescritura, no una extracción

`handout/gum_o3/` no es capa 0, no es capa 2, y solo parcialmente es referencia. Es una **reescritura** de capa 1.

Solapamiento verificado:

- M3 §3.3 (PDFs y divisores) ≈ `O3_H03_tipo_b_pdfs.md`
- M2 §3.3 (coeficientes de sensibilidad) ≈ `O3_H04_propagacion_guf.md`
- M7 bloque 6 (informe) ≈ `O3_H07_informe_gum.md`
- M1 §3.1 (trazabilidad) ≈ `O3_H01` §1.5

Contenido genuinamente de referencia (~350 de 869 líneas):

- `O3_H08_glosario.md` — 23 términos no definidos en ningún módulo
- `O3_H03` — tabla de PDFs con divisores
- `O3_H04` — ley de propagación en forma general
- `O3_H07` — checklist de informe GUM §7

El resto duplica narrativa. Eso no implica borrar ~520 líneas: una parte de esa «duplicación» es contenido básico que **falta como relato canónico en capa 1** y hoy vive solo (o mejor) en el handout. La prescripción es bidireccional:

- **Absorber en capa 1:** relación entre incertidumbre estándar, combinada y expandida; significado de `u`, `u_c`, `U` y `k`; vocabulario metrológico mínimo; noción de cobertura; reglas de presentación y redondeo; elementos mínimos de un informe conforme a GUM.
- **Dejar como anexo:** tratamiento detallado de autocorrelación; distribución t desplazada; PDFs arcoseno y trapezoidal; Welch–Satterthwaite detallado; Cholesky; desarrollos extendidos de MCM.

### 6.3 Asimetría O₃ / NOx y vacío de uso

`handout/no_nox/` tiene 120 líneas en 10 archivos (`NOX_H03` = 7 líneas, `NOX_H08` = 3). M6 lo cita **una sola vez**. De facto ya funciona como ficha operativa: checklist y control documental, sin duplicar a M6. Está mejor alineado que el de O₃, por accidente. `README.md` presenta ambas familias como equivalentes.

Búsqueda de `prelectura`, `lectura previa`, `antes del curso`, `leer.*handout` sobre `modulos/`, `README.md`, `diseno_curso_v2.md` y `handout/`: **0 resultados**. Nada dice si el handout se entrega antes, durante o después, ni si el participante debe leerlo.

### 6.4 Capa 1 no es extraíble en cuatro de ocho módulos

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

Tres nombres para el mismo objeto (`Guion dictable`, `Párrafo dictable`, ninguno) y dos esquemas de encabezado (`### 3.x`, `### Bloque N`).

**M5, M6 y M8 no tienen discurso redactado.** Tienen contenido, no narración. Para ellos, capa 1 no se extrae: se escribe. Hay 27 `Idea fuerza` para ~120 subbloques-equivalentes: capa 2 arranca con ~20 % de semillas.

### 6.5 `solo_md/` es una capa derivada fuera de control

`solo_md/` replica el árbol completo (592 K) con los enlaces Markdown desanclados, para lectura fuera del repositorio.

- No lo genera `build_paquete_html.py`.
- No está en git (`??` en `git status`).
- Ya divergió de `modulos/`: M1 14 líneas, M3 16, M2 12, M7 10, M8 10, M4 8, M5 6, M6 2.

El delta es sistemático y benigno —quita `[texto](enlace)` y deja el texto—, pero la copia es manual y sin verificación. Es el mismo patrón que produjo el problema del handout: dos archivos contando lo mismo, uno derivando en silencio.

Precedente positivo: `build_paquete_html.py` + `pandoc_rewrite_links.lua` ya generan `curso_paquete_completo.html` con validación de archivos, filas, anclas e IDs únicos. La infraestructura de derivación existe; `solo_md/` no la usa.

### 6.6 Solucionarios y protocolos

Los solucionarios son material privado del instructor. Hoy también reexplican parte de la teoría para ser legibles de forma autónoma. Esa repetición puede ser útil; no debe convertirse en otra fuente conceptual paralela.

Los protocolos E01–E16 necesitan autonomía porque se usan en laboratorio o campo. La duplicación debe ser deliberada: incluir lo necesario para ejecutar sin abandonar la actividad; remitir al material teórico para fundamentos; evitar una teoría alternativa; conservar la misma notación y terminología.

---

## 7. Diagnóstico pedagógico que no se resuelve solo al separar capas

Reconocer la capa meta corrige la interpretación de los módulos. No elimina estos problemas.

### 7.1 Inversión de vocabulario y cadena `u → u_c → U`

El vocabulario formal vive en `O3_H01` y en el glosario `O3_H08`. La secuencia de aula lo usa operativamente antes:

| Momento | Términos usados | Dónde están definidos |
|---|---|---|
| M1 (min 0–35) | incertidumbre del patrón / del analizador / del valor transferido, corrección, incertidumbre residual, falla, doble conteo, covarianza | `O3_H01` §1.3–1.4 — remitido, no dictado |
| M2 (min 35–83) | mensurando, coeficiente de sensibilidad; `u(T)`, `u(P)` | `O3_H01` §1.1, `O3_H04` §4.1 |
| M3 (min 83–137) | **recién aquí** Tipo A/B, PDF, combinación cuadrática | el módulo mismo |

`modulos/M1_trazabilidad.md:6` se autodeclara «establece el vocabulario y la arquitectura metrológica que se utilizarán en los módulos posteriores», pero más adelante delega ese vocabulario al handout. M1 pide prestado vocabulario que llega formalmente 82 min después, apoyándose en un documento cuyo momento de lectura nadie definió.

La cadena operativa `u_i → u_c → U = k·u_c` no tiene dueño docente claro. `U` y `k` aparecen en ejercicios y resultados; su introducción formal está principalmente en el handout.

**Resolución (no son alternativas excluyentes):**

- **M0, 15–20 min, tomados de los 78 min de reserva logística.** Mapa inicial, no glosario extenso: mensurando, error / corrección / incertidumbre, estándar / combinada / expandida, trazabilidad, Tipo A/B en versión mínima. M1 conserva sus 35 min y puede asumir el vocabulario. M3 profundiza, no introduce.
- **Dueño por módulo** para la definición operativa completa (tabla en §9). Otros módulos pueden recordar el concepto; no lo redefinen en paralelo.
- **Glosario de consulta** en la referencia, enriquecido con los términos de alta frecuencia que hoy faltan.
- **Prelectura de `O3_H00` + `O3_H01` + glosario** como complemento si hay envío previo. El curso no depende de que lean.

### 7.2 El glosario llega tarde y tiene vacíos

`O3_H08_glosario.md` está ubicado como sección tardía del handout y no funciona como puerta de entrada. Define algunos términos avanzados y omite varios de alta frecuencia práctica: fotómetro de referencia estándar (SRP), repetibilidad, precisión intermedia, reproducibilidad, calibración / verificación / ajuste, doble conteo, escala completa, sesgo, patrón de transferencia, deriva de cero y de span.

### 7.3 El informe GUM se exige antes de enseñarse de manera suficiente

M7 solicita un resultado auditable conforme a GUM §7, mientras que la lista más completa de elementos del informe vive en `O3_H07_informe_gum.md`. También se evalúan cobertura, redondeo y coherencia entre presupuesto y resultado. Estos criterios deben aparecer en capa 1 **antes** del taller, no únicamente como apoyo consultado durante la revisión final. Dueño propuesto: introducción en M4 (expansión, `U`, `k`, redondeo); integración y declaración en M7.

### 7.4 «Cobertura» tiene varios sentidos

El curso usa «cobertura» para:

- factor, probabilidad o intervalo de cobertura en sentido GUM;
- alcance cubierto por una evidencia;
- «matriz de cobertura» como artefacto del curso.

Reservar **cobertura** para el sentido metrológico GUM. Usar **alcance de la evidencia** para expresar qué condiciones o fuentes cubre un dato.

### 7.5 Duplicación no gobernada

Autocorrelación, covarianza, propagación y otros conceptos aparecen con distintos niveles de detalle en módulos, handouts, solucionarios y protocolos. La repetición no es siempre incorrecta. Se vuelve problemática cuando no se sabe cuál versión es canónica, cuál es resumen, cuál es ampliación, cuál se mantiene a mano y cuál debe actualizarse cuando cambia la teoría.

---

## 8. Arquitectura documental objetivo

### A. Meta maestro privado (capa 0)

Base: módulos M1–M8, gobernados como capítulos coordinados. Contiene teoría, discurso, decisiones pedagógicas, notas de instructor, tiempos, preguntas, respuestas breves, errores frecuentes, variantes, referencias y criterios de evaluación. Fuente superior de intención pedagógica. Lectura continua solo por ensamblado generado.

### B. Material teórico entregable (capa 1)

Derivado del meta quitando bloques, más un pase de continuidad. Relato limpio, conceptos necesarios, ejemplos, fórmulas, conexiones entre módulos, síntesis, ejercicios sin revelar soluciones. Fuente principal del participante.

### C. Anexos técnicos

Base: contenido avanzado del handout O₃. Derivaciones, casos especiales, métodos opcionales, referencias normativas extensas. No reparan huecos básicos del relato principal.

### D. Fichas operativas y ayudas de campo

Base: handout NOx y material práctico de consulta rápida. Checklists, fórmulas rápidas, criterios de aceptación, controles documentales, advertencias de montaje y seguridad.

### E. Protocolos prácticos

Base: E01–E16. Propósito y alcance, materiales, secuencia de ejecución, datos a registrar, criterios de aceptación y cierre, punteros al fundamento teórico. Conducen la actividad completa.

### F. Solucionarios privados

Resolución completa, cálculos paso a paso, criterios de corrección, errores típicos, variantes aceptables.

### G–H. Guion textual y diapositivas visuales (capas 2 y 3)

Derivados de capa 1, en ese orden. Estimación: 462 min de curso obligatorio, a 2–3 min por diapositiva ⇒ **150–200 diapositivas**.

El nombre «handout» deja de ser la categoría arquitectónica. En `README.md` se declara primero la función (anexo vs. ficha); el rename físico de `handout/` → `referencia/` (o equivalente) puede esperar a que el recorte de O₃ esté hecho, para no romper anclas a medias.

---

## 9. Dueños conceptuales por módulo

Cada concepto operativo se introduce en su módulo dueño **antes** de exigirse su uso. M0 desbloquea el vocabulario mínimo; no le quita la titularidad a M1.

| Módulo | Dueño de | Conceptos canónicos |
|---|---|---|
| **M0** (preámbulo, 15–20 min) | mapa inicial | mensurando, error / corrección / incertidumbre, `u` / `u_c` / `U` en versión mínima, trazabilidad, Tipo A/B mínimo |
| **M1** | trazabilidad y vocabulario de cadena | trazabilidad del resultado, SRP, patrón de transferencia, tres incertidumbres (patrón / analizador / valor transferido) |
| **M2** | modelo de medición | Beer–Lambert, coeficientes de sensibilidad, identificación de fuentes |
| **M3** | incertidumbre estándar | Tipo A/B, PDFs y divisores, `u_i`, combinación `u_c`, covarianza (definición), autocorrelación / `n_eff` |
| **M4** | presupuesto y expansión | contribuciones, doble conteo (regla), `U = k·u_c`, cobertura GUM, redondeo, coherencia presupuesto / resultado |
| **M5** | patrones y calibración | regresión multipunto, residuos, deriva de cero y span, verificación vs. ajuste, alcance de la evidencia, escala completa |
| **M6** | NOx y quimioluminiscencia | modelo diferencial, eficiencia del convertidor, interferencias, covarianza medida NO/NOx, sesgo |
| **M7** | integración y reporte | declaración del resultado, informe GUM §7, transferencia breve a NOx |
| **M8** | validación opcional | MCM, Cholesky, validación del marco GUM |

---

## 10. Mecanismo: una fuente, marcado por audiencia

Fuente única por módulo = capa 0. Las demás capas se generan quitando bloques. Ya existe la convención de facto (`Idea fuerza`, `Guion dictable`, `Apoyo en el handout`). Falta que sea **regular y legible por máquina**.

Esquema único por subbloque:

```markdown
### 3.N Título — 0:mm a 0:mm; acumulado 0:mm      ← capa 0 (minutaje)

**Idea fuerza:**            ← capa 2 (título de diapositiva)
**Guion dictable:**         ← capas 0 y 1 (discurso; texto del material teórico)
**Puntos:**                 ← capa 2 (3–5 viñetas comprimidas)
**Apoyo visual:**           ← capa 3 (qué diagrama, foto o esquema)
**Nota de facilitación:**   ← capa 0 (dónde se atasca el grupo, cómo destrabar)
**Referencias exactas:**    ← capa 0 completa; capa 1 en versión corta
**Apoyo en la referencia:** ← capa 0 (puntero a anexo o ficha)
```

Un solo `build_capas.py`, siguiendo el patrón de `build_paquete_html.py`, emite:

| Salida | Regla |
|---|---|
| capa 0 | el archivo tal cual |
| capa 1 | `Guion dictable` + referencias cortas; sin minutaje, sin notas de facilitación, sin errores frecuentes, sin punteros internos de instructor |
| capa 2 | `Idea fuerza` + `Puntos` |
| capa 3 | capa 2 + `Apoyo visual` como marcador de imagen |
| `solo_md/` | cualquiera de las anteriores, con enlaces desanclados |

Después de extraer capa 1, un pase editorial corto añade transiciones entre módulos y absorbe el vocabulario básico que hoy vive solo en el handout O₃. Ese pase no reescribe el discurso: lo conecta y cierra huecos de titularidad.

Ventajas frente a mantener archivos paralelos:

1. Es lo que ya está escrito, sin querer, en M1–M4 y M7.
2. Anti-drift: el handout y `solo_md/` demuestran qué pasa con dos archivos que cuentan lo mismo.
3. Un archivo por módulo como fuente, no dos ni cinco.

---

## 11. Reglas de derivación y control

1. **Una idea nueva nace en la capa meta.** Ninguna diapositiva, protocolo o solucionario introduce silenciosamente un concepto no reconocido en capa 0.
2. **Autoridad definida por capa.** El meta es canónico para contenido técnico, definiciones, ecuaciones, notación e intención pedagógica. Capa 1 es canónica para orden, redacción y experiencia del participante. Toda corrección técnica entra primero en el meta y después se propaga.
3. **Las diapositivas reducen, no amplían.** Condensan, ilustran y jerarquizan. No agregan teoría ausente de capa 1. Si una idea aparece por primera vez en la diapositiva visual, hay una ruptura del flujo.
4. **Los anexos amplían sin interrumpir.** El relato principal se comprende sin leerlos. No reparan huecos básicos.
5. **Fichas y protocolos repiten según su función.** Fichas: consulta operativa rápida. Protocolos: ejecución completa. Ambos conservan notación, terminología y criterios de capa 1.
6. **Las respuestas permanecen fuera del entregable.** El meta conserva respuesta breve, resultado esperado y propósito pedagógico. El solucionario conserva desarrollo completo, criterios de corrección y variantes. Ninguno se anticipa en capa 1.
7. **Cada concepto operativo tiene un dueño.** Distribución de §9. Otros módulos pueden recordarlo; no lo redefinen en paralelo.
8. **Terminología reservada.** `cobertura` solo en sentido GUM. `alcance de la evidencia` para condiciones o fuentes cubiertas por un dato.

---

## 12. Inventario de deuda

| # | Deuda | Impacto | Esfuerzo |
|---|---|---|---|
| D1 | M5, M6 y M8 sin `Guion dictable` — capa 1 inexistente ahí | **bloqueante** para capas 1–3 | alto: redactar discurso |
| D2 | Tres convenciones distintas para el bloque de discurso | bloquea derivación mecánica | bajo: renombrar |
| D3 | `handout/gum_o3/` duplica ~520 líneas y retiene básico que debería estar en capa 1 | confusión de roles, drift, huecos en el relato | medio: absorber básico + podar a anexo |
| D4 | Rol del handout nunca declarado (prelectura / aula / consulta) | impide decidir el orden de términos | bajo: decisión + un párrafo en README |
| D5 | Inversión de vocabulario M1 ↔ M3 y cadena `u → u_c → U` sin dueño | pedagógico; afecta a todos los participantes | medio: M0 + dueños de §9 |
| D6 | `solo_md/` derivado a mano, fuera de git, ya divergido | drift silencioso | bajo: generar o borrar |
| D7 | 27 `Idea fuerza` para ~120 subbloques-equivalentes | capa 2 arranca con ~20 % de semillas | alto, mecánico tras D2 |
| D8 | README presenta handout O₃ y NOx como equivalentes | expectativa falsa | bajo: una tabla de funciones en README |
| D9 | Informe GUM, redondeo y coherencia se exigen en M7 y viven en el handout | el taller evalúa lo que el relato no enseñó | medio: titularidad M4 + M7 en capa 1 |
| D10 | Glosario tardío y con vacíos de alta frecuencia (SRP, deriva, verificación vs. ajuste, …) | el mapa inicial no tiene respaldo de consulta | bajo: completar `O3_H08` |
| D11 | Polisemia de «cobertura» | confusión de participantes | bajo: reserva terminológica + reemplazo |
| D12 | Solucionarios reexplican teoría; riesgo de tercera doctrina | drift conceptual | bajo: recortar a resolución y criterios |

Valoración del desfase (esfuerzo editorial, no calidad técnica):

| Área | Desfase |
|---|---|
| Contenido técnico | **bajo** — el conocimiento ya existe |
| Versión meta | **bajo a medio** — base sólida; falta declarar rol, cerrar saltos y uniformar bloques |
| Material teórico del participante | **medio a alto** — existe parcialmente, repartido; falta narrativa limpia y continua |
| Anexos y fichas | **medio** — funciones mezcladas bajo el nombre «handout» |
| Guion textual y diapositivas | **alto** — el pipeline no existe; construirlo antes de estabilizar capa 1 sería un error |

No se requiere reconstruir el curso desde cero. Se requiere una reorganización editorial y una cadena de derivación explícita.

---

## 13. Plan propuesto

Orden por dependencia, no por importancia.

1. **Declarar el modelo** en `README.md`: eje 0–1–2–3, productos perpendiculares, asimetría O₃ (anexo) / NOx (ficha), y que la referencia no es prelectura obligatoria. Fijar la convención de bloques de §10. Resuelve D4 y D8. Sin tocar contenido.
2. **Piloto en M5** — 0 subbloques, 1 `Idea fuerza`, prosa plana, sin discurso. Redactar `Guion dictable`, etiquetar el esquema, y comprobar que de ahí se puede extraer un capítulo de capa 1 legible. Si el esquema aguanta en el peor caso, aguanta en todos. Ataca D1 y D2.
3. **`build_capas.py`**, siguiendo el patrón de `build_paquete_html.py`. `solo_md/` pasa a salida generada o se borra. Resuelve D6.
4. **Propagar el esquema** a M1–M4 y M7 (tienen discurso; falta etiquetar y, en M7, unificar `Párrafo dictable` → `Guion dictable`). Después redactar discurso en M6 y M8. Cierra D1 y D2.
5. **Cerrar huecos pedagógicos en el meta, antes de extraer capa 1 en limpio:** M0; dueños de §9; elementos del informe GUM, redondeo y coherencia en M4/M7; reserva de «cobertura»; términos faltantes en el glosario. Cierra D5, D9, D10, D11.
6. **Partir el handout O₃:** absorber lo básico en capa 1; dejar lo avanzado como anexo; conservar anclas. Declarar NOx como ficha. Recortar solucionarios a resolución y criterios. Cierra D3 y D12.
7. **Pase de continuidad de capa 1** sobre el recorte mecánico: transiciones entre capítulos, una sola narrativa, ejercicios sin soluciones.
8. **Capas 2 y 3** cuando la derivación ya es mecánica. Cierra D7. Volumen esperado: 150–200 diapositivas.

---

## 14. Lo que no está mal

Para que el diagnóstico no se lea como una condena:

- El contenido técnico es sólido y está trazado a fuente con página exacta (JCGM, QUAM, EN 14211, EPA, NISTIR, BIPM.QM-K1).
- El control documental es riguroso: la nota sobre APOA-370 vs. APNA-370 evita atribuir especificaciones equivocadas.
- Los datasets son reproducibles con semilla declarada (`20260819`).
- La separación curso teórico / práctica de laboratorio, con entregables evaluados independientes (M7 y E15), está bien argumentada.
- `build_paquete_html.py` ya valida archivos, filas, columnas, MathML, anclas, IDs únicos y ausencia de recursos externos. Es la base sobre la que se monta `build_capas.py`.
- `handout/no_nox/` ya es ficha operativa correcta. Sirve de modelo para partir el de O₃.
- La densidad de los módulos, una vez declarado su rol meta, deja de ser un defecto y pasa a ser inventario reutilizable.

El desfase es **de una capa y media**, no de arquitectura equivocada: contenido sobra, capa 0 y 1 están fusionadas, capas 2 y 3 no arrancaron, y unos pocos conceptos operativos están mal ubicados en la secuencia.

---

## 15. Conclusión

La inquietud inicial era válida: módulos y handouts se repetían, se completaban entre sí y no tenían fronteras claras. La causa no era exceso de contenido ni una mala concepción del curso. Era la ausencia de una arquitectura documental explícita.

1. Los módulos no están simplemente sobrecargados: son una base avanzada del documento meta del autor e instructor.
2. El material teórico entregable todavía no existe como producto único, limpio y continuo; en M5, M6 y M8 ni siquiera hay discurso del que extraerlo.
3. El handout O₃ mezcla contenido básico que debe incorporarse al relato principal con material avanzado que debe quedar como anexo.
4. El handout NOx tiene más sentido como ficha operativa que como tratado paralelo.
5. Vocabulario inicial, cadena `u → u_c → U`, cobertura, redondeo e informe GUM requieren dueño y ubicación dentro de la narrativa; eso no se arregla solo al separar archivos.
6. Guion textual y diapositivas visuales deben derivarse del material teórico estabilizado, no de fuentes paralelas.
7. El mecanismo es una fuente marcada por audiencia más un recorte gobernado; no un segundo árbol mantenido a mano (`solo_md/` y el handout ya mostraron por qué).

El curso está avanzado en conocimiento y en preparación docente. Su siguiente etapa es convertir esa riqueza meta en una secuencia controlada de productos, cada uno con destinatario, propósito y profundidad definidos.
