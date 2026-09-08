# Diagnóstico final y arquitectura documental propuesta

## Curso de incertidumbre de medición para operadores de redes de calidad del aire

**Directorio evaluado:** `docs/capacitacion_incert/cursov2/`
**Alcance:** arquitectura pedagógica y documental del curso; relación entre módulos, handouts, solucionarios, prácticas y futuras diapositivas.
**Propósito:** consolidar el diagnóstico alcanzado después de aclarar el flujo real de autoría y uso del material.

---

## 1. Conclusión en una frase

El paquete no tiene un problema de contenido técnico: tiene un problema de **capas sin declarar**. Cinco artefactos con audiencias distintas conviven en dos carpetas, dos de ellos compiten por el mismo rol, y los `Guion dictable` que deberían producir la capa del participante faltan en tres módulos. El desfase es de una capa y media, no de arquitectura equivocada.

---

## 2. Punto de partida

La evaluación comenzó con tres inquietudes:

1. si los términos metrológicos debían aclararse antes de iniciar los módulos;
2. si los módulos omitían contenido importante que había quedado únicamente en los handouts;
3. si los módulos ya funcionaban, en la práctica, como su propio handout.

La primera lectura mostraba una mezcla de funciones. Los módulos contienen teoría, discurso, minutaje, instrucciones docentes, ejercicios, resultados y errores frecuentes. El handout de O₃ contiene tanto conceptos básicos como desarrollos avanzados. El handout de NOx resume parte de M6, pero no alcanza su profundidad. Los protocolos prácticos vuelven a explicar algunos conceptos para poder utilizarse de forma autónoma.

Con esa información, parecía que los módulos estaban sobrecargados y que competían con los handouts como material del participante. Esa interpretación era incompleta porque faltaba declarar una pieza central del método de trabajo: la **versión meta del curso**.

---

## 3. Aclaración decisiva: la función meta ya existe

El flujo de autoría no comienza con el material que recibe el participante. Comienza con una capa más amplia, privada y cargada, que sirve al autor y al instructor.

En el estado actual, esa función meta existe de manera distribuida, principalmente en los módulos M1–M8, pero todavía no está declarada ni gobernada como sistema. La decisión propuesta es tratarlos como capítulos coordinados del **meta maestro canónico**. Si se necesita una lectura continua, debe producirse mediante un ensamblado generado desde M1–M8, nunca mediante otra copia mantenida manualmente.

El meta maestro objetivo debe contener:

- teoría completa;
- hilo narrativo cercano al discurso oral;
- propósito de cada bloque;
- secuencia pedagógica;
- transiciones;
- minutaje;
- instrucciones de facilitación;
- preguntas para el grupo;
- ejercicios y respuestas;
- resultados esperados;
- errores frecuentes;
- advertencias y puntos de énfasis;
- variantes según tiempo o nivel del grupo;
- contenido opcional;
- referencias y justificaciones;
- decisiones sobre qué incluir, simplificar o dejar como consulta.

Su pregunta rectora es:

> ¿Qué necesito saber, recordar y tener disponible para enseñar bien este bloque?

Esta pieza no es un handout ni debe entregarse directamente al participante. Es la fuente pedagógica superior del curso.

Al reconocer esta capa, cambia el diagnóstico: la densidad de los módulos, sus respuestas, su minutaje y sus instrucciones no son defectos por sí mismos. Son características coherentes con una versión meta. El problema real es que ese rol no está declarado y no existe todavía una derivación limpia y sistemática hacia los demás productos.

---

## 4. Modelo de capas y flujo autoral correcto

El flujo deseado tiene cuatro capas principales y un artefacto perpendicular de referencia.

### 4.1 Modelo de trabajo del autor

| # | Capa | Descripción |
|---|---|---|
| **0** | **Meta / instructor** | Versión más cargada del material teórico. Minutaje, ficha, prerrequisitos, organización de actividades, errores frecuentes, transiciones, procedencia exacta de fuentes, soluciones, cómo destrabar al grupo. |
| **1** | **Material teórico del participante** | Prosa completa, hilo narrativo lógico y consecuente. Es casi el discurso hablado. Se entrega como material teórico. |
| **2** | **Diapositivas texto** | Derivadas de capa 1. Texto comprimido, telegráfico. |
| **3** | **Diapositivas finales** | Capa 2 + imágenes, diagramas, diseño. |
| **R** | **Referencia de consulta** | Artefacto perpendicular, no etapa del flujo. Glosario, tablas, fórmulas, checklists. Lo que el operador abre seis meses después en su puesto. |

Relación entre 0 y 1: **superconjunto**, no hermanos. Capa 1 se obtiene *quitando* bloques de capa 0, no reescribiendo. Esta decisión gobierna todo el resto del diagnóstico.

### 4.2 Capa 0 — versión meta del autor e instructor

Es la fuente pedagógica más completa. Conserva teoría, relato oral y decisiones docentes. Debe permitir preparar, impartir, ajustar y actualizar el curso.

Actualmente, los módulos M1–M8 forman una fuente meta distribuida. El estado objetivo debe tratarlos como capítulos coordinados de un meta maestro y, si se necesita una lectura continua, ensamblarlos sin crear otra copia mantenida manualmente.

### 4.3 Capa 1 — material teórico del participante

Se deriva de la versión meta.

Mantiene:

- explicación completa;
- hilo narrativo lógico y consecuente;
- conceptos y definiciones;
- ecuaciones necesarias;
- ejemplos;
- figuras y tablas útiles;
- síntesis;
- ejercicios apropiados;
- referencias pertinentes.

Elimina o separa:

- minutaje;
- instrucciones como "dictar", "preguntar" o "mostrar";
- estrategia de facilitación;
- respuestas anticipadas;
- soluciones completas;
- resultados de demostraciones antes de realizarlas;
- comentarios editoriales;
- decisiones internas del autor.

Su pregunta rectora es:

> ¿Qué necesita leer y conservar el participante para comprender el curso después de la sesión?

Este material debe poder leerse como un manual breve y continuo. Puede conservar la división M1–M8, pero cada módulo debe funcionar como capítulo de una sola narrativa, no como documento independiente que obliga a consultar otra fuente para completar ideas básicas.

### 4.4 Capa 2 — guion textual de diapositivas

Se deriva del material teórico, no directamente de una colección dispersa de módulos y handouts.

Mantiene:

- mismo orden conceptual;
- mismas conclusiones;
- mismos ejemplos esenciales;
- mismas definiciones operativas.

Reduce:

- longitud;
- detalle;
- derivaciones;
- explicaciones secundarias;
- densidad verbal.

Su estilo es telegráfico y de alta síntesis: frases cortas, una idea principal por diapositiva y texto suficiente para orientar sin reemplazar la exposición oral.

Su pregunta rectora es:

> ¿Qué necesita estar escrito en pantalla mientras se explica esta idea?

### 4.5 Capa 3 — diapositivas visuales

Se deriva del guion textual. Añade:

- imágenes;
- diagramas;
- composición;
- jerarquía visual;
- tablas simplificadas;
- señales de énfasis;
- revelado progresivo, cuando sea útil.

No debe introducir teoría nueva. Si una idea aparece por primera vez en la diapositiva visual, existe una ruptura en el flujo de derivación.

Su pregunta rectora es:

> ¿Cómo hacer visible la idea sin convertir la diapositiva en una página del manual?

### 4.6 Capa R — referencia de consulta (perpendicular)

Glosario, tablas de PDFs, ley de propagación, checklists de informe, fichas operativas. Lo que se abre seis meses después en el puesto de trabajo. No es etapa del flujo lineal: se construye y mantiene como artefacto aparte, paralelo a la capa 1.

---

## 5. Estado real de cada capa

| Capa | Dónde vive hoy | Volumen | Estado |
|---|---|---:|---|
| 0 — Meta | disperso dentro de `modulos/` + `modulos/soluciones/` | 607 + 1571 líneas | existe, **fusionado con capa 1** |
| 1 — Teórico participante | embebido en `modulos/`, sin separar | ~818 líneas (mezcladas) | existe, **no extraíble en 4 de 8 módulos** |
| 2 — Diapositivas texto | — | 0 | **no existe** |
| 3 — Diapositivas finales | — | 0 | **no existe** |
| R — Referencia | `handout/gum_o3/` + `handout/no_nox/` | 869 + 120 líneas | existe, **contaminado con capa 1 duplicada** |

Verificación de ausencia de capas 2 y 3:

```bash
find . -iname "*slide*" -o -iname "*diapo*" -o -iname "*.pptx" \
       -o -iname "*reveal*" -o -iname "*beamer*"
# 0 resultados
```

Reparto de líneas por rol de sección en los 8 módulos:

| Sección | Líneas | Audiencia |
|---|---:|---|
| Ficha + Objetivos (duración, prerrequisitos, materiales, distribución de tiempo) | 201 | solo instructor |
| Guion de exposición | 818 | mezclado |
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

## 6. Mecanismo propuesto: una fuente, marcado por audiencia

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

Precedente positivo: `build_paquete_html.py` + `pandoc_rewrite_links.lua` ya generan `curso_paquete_completo.html` con validación de archivos, filas, anclas e IDs únicos. La infraestructura de derivación existe; `solo_md/` y las capas 1–3 simplemente no la usan.

---

## 7. Ubicación de los materiales actuales dentro del flujo

### 7.1 Módulos M1–M8

Los módulos actuales se acercan principalmente a la **versión meta**. Incluyen guion dictable, minutaje, exposición, ejercicios, resultados esperados, errores frecuentes y conexiones con otros materiales.

Ejemplos:

- M2 publica el resultado numérico del ejercicio en `modulos/M2_modelo_medicion.md`;
- M4 entrega valores esperados de `u_c`, `U` y contribución dominante en `modulos/M4_presupuesto_analizador.md`;
- M8 anticipa resultados y conclusiones de la demostración en `modulos/M8_opcional_monte_carlo.md`.

Ese contenido es útil para el instructor, pero no corresponde íntegramente al material entregable. Por tanto, los módulos no deben tratarse como un error editorial ni convertirse directamente en handout. Deben reconocerse como fuente meta y servir para producir una versión teórica limpia.

### 7.2 Hallazgo crítico: la capa 1 no es extraíble en 4 de 8 módulos

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

### 7.3 Handout de GUM (Guía para la Expresión de la Incertidumbre de Medida) y O₃

El handout de O₃ es una **reescritura** de la capa 1, no una extracción.

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

El handout de O₃ mezcla dos funciones:

1. contiene piezas básicas que deberían formar parte del relato principal del participante;
2. contiene desarrollos avanzados que funcionan correctamente como anexos técnicos.

Pertenecen al material teórico principal, por ejemplo:

- relación entre incertidumbre estándar, combinada y expandida;
- significado de `u`, `u_c`, `U` y `k`;
- vocabulario metrológico mínimo;
- noción de cobertura;
- reglas de presentación y redondeo;
- elementos mínimos de un informe conforme a GUM.

Pueden permanecer como referencia avanzada:

- tratamiento detallado de autocorrelación;
- distribución t desplazada;
- funciones de densidad de probabilidad (PDF) arcoseno y trapezoidal;
- Welch–Satterthwaite detallado;
- Cholesky;
- desarrollos extendidos del método de Monte Carlo (MCM).

Criterio general: pertenece al material principal todo lo necesario para seguir los módulos obligatorios y resolver las actividades requeridas. Pertenece a anexos aquello que amplía, deriva o trata casos especiales sin ser necesario para completar el recorrido principal.

El handout O₃ no debe desaparecer. Debe dejar de completar silenciosamente huecos básicos de los módulos y asumir un papel explícito como conjunto de anexos o referencia técnica.

### 7.4 Asimetría O₃ / NOx

`handout/no_nox/` tiene 120 líneas en 10 archivos (`NOX_H03` = 7 líneas, `NOX_H08` = 3). M6 lo cita **una sola vez**. De facto ya funciona como capa R pura — checklist y control documental, sin duplicar a M6. Está mejor alineado que el de O₃, por accidente. Pero `README.md` presenta ambas familias como equivalentes.

El handout de NOx no es equivalente al handout O₃. Es mucho más breve y, en varios puntos, contiene menos información que M6. Su utilidad real se parece más a:

- ficha operativa;
- referencia rápida;
- checklist de auditoría;
- ayuda de campo;
- recordatorio de fórmulas y controles documentales.

No necesita mantener una simetría artificial con el handout O₃. Puede ser un producto distinto y legítimo, siempre que su función se declare correctamente.

### 7.5 Vacío de instrucción de uso del handout

Búsqueda de `prelectura`, `lectura previa`, `antes del curso`, `leer.*handout` sobre `modulos/`, `README.md`, `diseno_curso_v2.md` y `handout/`: **0 resultados**. Nada dice si el handout se entrega antes, durante o después, ni si el participante debe leerlo. Esta ambigüedad es la que permite que el handout O₃ termine completando huecos de M1–M7 sin que nadie lo haya decidido.

### 7.6 Solucionarios

Los solucionarios son material privado del instructor. Actualmente también reexplican parte de la teoría. Esa repetición puede ser útil para que la solución sea legible de forma autónoma, pero no debe convertirse en otra fuente conceptual paralela.

El meta maestro debe ser canónico para contenido técnico, respuestas breves, propósito pedagógico y resultados esperados. El solucionario debe contener la resolución completa, los cálculos paso a paso, los criterios de corrección y las variantes aceptables, sin crear una tercera versión doctrinal.

### 7.7 Protocolos prácticos

Los protocolos E01–E16 necesitan cierto grado de autonomía porque se usan durante trabajo de laboratorio o campo. Por ello, alguna repetición de fórmulas, criterios y advertencias es aceptable.

La duplicación debe ser deliberada:

- incluir lo necesario para ejecutar el protocolo sin abandonar la actividad;
- remitir al material teórico para fundamentos;
- evitar desarrollar una teoría alternativa o contradictoria;
- conservar la misma notación y terminología del material principal.

### 7.8 `solo_md/` — capa derivada fuera de control

`solo_md/` replica el árbol completo (592 K) con los enlaces Markdown desanclados, para lectura fuera del repositorio.

- **No lo genera `build_paquete_html.py`** — `grep solo_md build_paquete_html.py` → 0 resultados.
- **No está en git** — sin historial; aparece como `??` en `git status`.
- **Ya divergió** de `modulos/`: M1 14 líneas, M3 16, M2 12, M7 10, M8 10, M4 8, M5 6, M6 2.

El delta es sistemático y benigno —quita `[texto](enlace)` y deja el texto—, pero la copia es manual y sin verificación. Es exactamente el patrón que produjo el problema del handout: dos archivos contando lo mismo, uno de ellos derivando en silencio.

---

## 8. Diagnóstico pedagógico que permanece vigente

Reconocer la capa meta corrige la interpretación de los módulos, pero no elimina todos los problemas encontrados.

### 8.1 Falta una entrada terminológica clara

El glosario existe en `handout/gum_o3/O3_H08_glosario.md`, pero está ubicado como sección tardía del handout y no funciona como puerta de entrada al curso.

Además, define algunos términos avanzados y omite varios de alta frecuencia práctica:

- fotómetro de referencia estándar (SRP);
- repetibilidad;
- precisión intermedia;
- reproducibilidad;
- calibración, verificación y ajuste;
- doble conteo;
- escala completa;
- sesgo;
- patrón de transferencia;
- deriva de cero y de span.

### 8.2 Inversión de vocabulario M1 ↔ M3

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

### 8.3 Existen conceptos usados antes de ser enseñados

M2 trabaja con expresiones como `u(T)` y `u(P)` antes de que M3 defina formalmente la incertidumbre estándar.

La cadena:

```text
u_i → u_c → U = k·u_c
```

no tiene todavía un dueño docente completamente claro. `U` y `k` aparecen en ejercicios y resultados, pero su introducción formal está principalmente en el handout.

En la arquitectura final, cada concepto operativo debe tener un módulo dueño. El material del participante debe introducirlo antes de exigir su uso.

### 8.4 El informe GUM se exige antes de enseñarse de manera suficiente

M7 solicita un resultado auditable conforme a GUM §7, mientras que la lista más completa de elementos del informe vive en `handout/gum_o3/O3_H07_informe_gum.md`.

También se evalúan cobertura, redondeo y coherencia entre presupuesto y resultado. Estos criterios deben aparecer dentro del material teórico antes del taller, no únicamente como apoyo consultado durante la revisión final.

### 8.5 "Cobertura" tiene varios sentidos

El curso usa "cobertura" para:

- factor, probabilidad o intervalo de cobertura en sentido GUM;
- alcance cubierto por una evidencia;
- "matriz de cobertura" como artefacto del curso.

Esta colisión puede confundir al participante. Conviene reservar **cobertura** para el sentido metrológico GUM y usar **alcance de la evidencia** para expresar qué condiciones o fuentes cubre un dato.

### 8.6 Existe duplicación no gobernada

Autocorrelación, covarianza, propagación y otros conceptos aparecen con distintos niveles de detalle en módulos, handouts, solucionarios y protocolos.

La repetición no es siempre incorrecta. Se vuelve problemática cuando no se sabe:

- cuál versión es canónica;
- cuál es resumen;
- cuál es ampliación;
- cuál se mantiene manualmente;
- cuál debe actualizarse cuando cambia la teoría.

---

## 9. Arquitectura documental objetivo

### A. Meta maestro privado

**Base:** módulos M1–M8.

**Contenido:**

- teoría completa;
- discurso;
- decisiones pedagógicas;
- notas de instructor;
- tiempos;
- preguntas;
- respuestas;
- errores frecuentes;
- variantes;
- referencias;
- criterios de evaluación.

Es fuente superior de intención pedagógica.

### B. Material teórico entregable

**Derivado del meta maestro.**

**Contenido:**

- relato limpio y continuo;
- conceptos necesarios;
- ejemplos;
- fórmulas;
- conexiones entre módulos;
- síntesis;
- ejercicios sin revelar anticipadamente soluciones.

Es fuente principal del participante.

### C. Anexos técnicos

**Base:** contenido avanzado del handout O₃.

**Contenido:**

- derivaciones;
- casos especiales;
- métodos opcionales;
- referencias normativas extensas;
- material para profundización posterior.

**Destinatario y uso:** participantes que necesiten profundizar e instructor durante preparación o consulta. No son lectura obligatoria para completar recorrido principal.

### D. Fichas operativas y ayudas de campo

**Base:** partes útiles del handout NOx y material práctico.

**Contenido:**

- checklists;
- fórmulas rápidas;
- criterios de aceptación;
- controles documentales;
- advertencias de montaje y seguridad.

**Destinatario y uso:** participantes durante práctica, operación o auditoría. Sirven para consulta rápida; no conducen por sí solas una actividad completa.

### E. Protocolos prácticos

**Base:** protocolos E01–E16.

**Contenido:**

- propósito y alcance de cada actividad;
- materiales y condiciones previas;
- secuencia completa de ejecución;
- datos que deben registrarse;
- criterios de aceptación y cierre;
- referencias al fundamento teórico correspondiente.

**Destinatario y uso:** participantes e instructor durante laboratorio o campo. A diferencia de una ficha, un protocolo conduce la ejecución completa de una actividad.

### F. Solucionarios privados

**Contenido:**

- resolución completa;
- cálculos paso a paso;
- criterios de corrección;
- errores típicos;
- variantes aceptables.

**Destinatario y uso:** instructor durante preparación, acompañamiento y evaluación. El meta maestro conserva respuesta breve, propósito pedagógico y resultado esperado; el solucionario conserva desarrollo completo.

### G. Guion textual de diapositivas

**Derivado del material teórico.**

**Contenido:**

- títulos;
- frases cortas;
- estructura por diapositiva;
- mensajes centrales;
- indicaciones básicas de apoyo visual.

### H. Diapositivas visuales

**Derivadas del guion textual.**

**Contenido:**

- diseño final;
- imágenes;
- diagramas;
- tablas simplificadas;
- composición y jerarquía visual.

---

## 10. Reglas de derivación y control

Para evitar drift entre productos, conviene adoptar reglas explícitas.

### Regla 1. Una idea nueva nace en la capa meta

Ninguna diapositiva, protocolo o solucionario debe introducir silenciosamente un concepto que no esté reconocido en la versión meta.

### Regla 2. Cada capa tiene autoridad definida

El meta maestro es canónico para contenido técnico, definiciones, ecuaciones, notación e intención pedagógica. El material teórico es canónico para orden, redacción y experiencia del participante. Toda corrección técnica debe incorporarse primero al meta maestro y después propagarse a productos derivados.

### Regla 3. Las diapositivas reducen, no amplían

Guion textual y diapositivas visuales pueden condensar, ilustrar y jerarquizar. No deben agregar teoría ausente del material teórico.

### Regla 4. Los anexos amplían sin interrumpir

El relato principal debe ser comprensible sin leer todos los anexos. Los anexos permiten profundidad adicional, no reparación de huecos básicos.

### Regla 5. Fichas y protocolos repiten según su función

Las fichas repiten solo lo necesario para consulta operativa rápida y no sustituyen una secuencia completa. Los protocolos repiten lo necesario para ejecutar una actividad de principio a fin. Ambos deben conservar notación, terminología y criterios del material principal.

### Regla 6. Las respuestas permanecen fuera del entregable principal

El meta maestro conserva respuesta breve, resultado esperado y propósito pedagógico. El solucionario conserva resolución completa, cálculos paso a paso, criterios de corrección y variantes aceptables. Ninguno de estos contenidos debe anticiparse en el material teórico entregable.

### Regla 7. Cada concepto operativo tiene un dueño

Distribución conceptual objetivo propuesta:

- **M0 (vocabulario, propuesto):** mensurando, error/corrección/incertidumbre, estándar/combinada/expandida, trazabilidad, Tipo A/B en versión mínima.
- **M1:** trazabilidad, mensurando y vocabulario base;
- **M2:** modelo de medición y coeficientes de sensibilidad;
- **M3:** incertidumbre estándar, Tipo A/B, PDFs y combinación;
- **M4:** presupuesto, contribuciones, doble conteo, `U`, `k`, cobertura y redondeo;
- **M5:** patrones, regresión, residuos y alcance de evidencia;
- **M6:** modelo NOx, interferencias y covarianza;
- **M7:** integración, declaración del resultado e informe GUM;
- **M8:** validación opcional mediante MCM.

Otros módulos pueden recordar el concepto, pero no redefinirlo de manera paralela.

---

## 11. Valoración del desfase actual

En esta sección, **desfase** expresa esfuerzo editorial y de consolidación necesario para alcanzar arquitectura objetivo. No califica calidad técnica del contenido existente.

Escala usada:

- **bajo:** producto ya existe y requiere ajustes menores de declaración, consistencia o limpieza;
- **medio:** contenido existe, pero necesita consolidación, reclasificación o derivación significativa;
- **alto:** producto o pipeline todavía no existe como salida gobernada y debe construirse a partir de capas previas.

### 11.1 Contenido técnico

**Desfase bajo.** Gran parte del conocimiento requerido ya existe en módulos, handouts, prácticas y solucionarios.

### 11.2 Versión meta

**Desfase bajo a medio.** Los módulos ya constituyen una base sólida. Requieren declarar su rol, cerrar algunos saltos conceptuales y mejorar consistencia global.

### 11.3 Material teórico del participante

**Desfase medio a alto.** Su contenido existe parcialmente, pero está repartido entre varias fuentes. Falta una narrativa limpia, continua y explícitamente entregable. Bloqueante: M5, M6 y M8 no tienen `Guion dictable`.

### 11.4 Anexos y ayudas operativas

**Desfase medio.** Existe material valioso, pero las funciones de referencia avanzada, resumen y ficha de campo están mezcladas bajo el nombre "handout".

### 11.5 Guion textual y diapositivas visuales

**Desfase alto como pipeline formal.** Deben construirse después de estabilizar el material teórico. Producirlas antes consolidaría inconsistencias y multiplicaría trabajo de revisión.

### 11.6 Diagnóstico global

No se requiere reconstruir el curso desde cero. Se requiere una reorganización editorial importante y una cadena de derivación explícita.

En términos cualitativos:

- conocimiento: avanzado;
- versión meta: avanzada;
- narrativa entregable: incompleta;
- clasificación de anexos: ambigua;
- pipeline hacia diapositivas: todavía no consolidado.

---

## 12. Inventario de deuda

| # | Deuda | Impacto | Esfuerzo |
|---|---|---|---|
| D1 | M5, M6, M8 sin `Guion dictable` — capa 1 inexistente ahí | **bloqueante** para capas 1–3 | alto: redactar discurso |
| D2 | Tres convenciones distintas para el bloque de discurso (`Guion dictable`, `Párrafo dictable`, ninguna) y dos esquemas de encabezado (`### 3.x`, `### Bloque N`) | bloquea derivación mecánica | bajo: renombrar |
| D3 | `handout/gum_o3/` duplica ~520 líneas de capa 1 | confusión de roles, riesgo de drift | medio: podar a ~350 líneas de capa R real |
| D4 | Rol del handout nunca declarado (prelectura / aula / consulta) | impide decidir el orden de términos | bajo: decisión + 1 párrafo en README |
| D5 | Inversión de vocabulario M1 ↔ M3 (M1 usa términos cuya definición formal llega 82 min después) | pedagógico, afecta a todos los participantes | medio: bloque M0 de 15–20 min |
| D6 | `solo_md/` derivado a mano, fuera de git, ya divergido | drift silencioso | bajo: generar con `build_capas.py` o borrar |
| D7 | 27 `Idea fuerza` para ~120 subbloques-equivalentes | capa 2 arranca con ~20 % de semillas | alto, pero mecánico tras D2 |
| D8 | README presenta handout O₃ y NOx como equivalentes siendo asimétricos | expectativa falsa | bajo: 1 tabla en README |

Estimación de volumen para capas 2 y 3: 462 min de curso obligatorio, a 2–3 min por diapositiva ⇒ **150–200 diapositivas**.

---

## 13. Plan propuesto

Orden por dependencia, no por importancia.

1. **Declarar las cinco capas** en `README.md` y fijar la convención de bloques de §6. Renombrar `handout/` → `referencia/` o declarar explícitamente su rol de capa R. Resuelve D4 y D8. Sin tocar contenido.
2. **Piloto en M5** — el módulo más incompleto: 0 subbloques, 1 `Idea fuerza`, sin discurso. Si el esquema aguanta ahí, aguanta en todos. Ataca D1 y D2 en el peor caso.
3. **`build_capas.py`**, siguiendo el patrón de `build_paquete_html.py`. `solo_md/` pasa a ser salida generada. Resuelve D6.
4. **Propagar el esquema** a M1–M4 y M7 (tienen discurso, solo falta etiquetar), después a M6 y M8 (hay que redactarlo). Cierra D1, D2.
5. **Podar el handout O₃** a capa R real: glosario, tablas de PDFs, ley de propagación, checklist de informe. Las 30 anclas existentes siguen sirviendo. Cierra D3.
6. **Decidir el orden de términos**: bloque M0 de vocabulario (recomendado) o prelectura obligatoria de capa R. Cierra D5.
7. **Capas 2 y 3** al final, cuando la derivación ya es mecánica. Cierra D7.

---

## 14. Solución conceptual

La solución no consiste en escoger entre módulos y handouts como si fueran productos rivales. Consiste en reconocer que cumplen funciones distintas y declararlas.

```text
META MAESTRO (capa 0)              ─ fuente pedagógica superior
    ├── MATERIAL TEÓRICO (capa 1)  ─ entregable principal del participante
    │       └── GUION TEXTUAL (capa 2)
    │               └── DIAPOSITIVAS VISUALES (capa 3)
    ├── ANEXOS TÉCNICOS            ─ profundización opcional
    ├── FICHAS OPERATIVAS          ─ consulta rápida en puesto
    ├── PROTOCOLOS PRÁCTICOS       ─ ejecución autónoma en laboratorio/campo
    └── SOLUCIONARIOS              ─ privado del instructor

REFERENCIA (capa R)                ─ perpendicular: glosario, tablas, checklists
```

Dentro de este modelo:

- módulos actuales alimentan principalmente el meta maestro;
- partes básicas del handout O₃ se integran al material teórico;
- partes avanzadas del handout O₃ se convierten en anexos;
- handout NOx se redefine como ayuda operativa o ficha de campo;
- protocolos conservan autonomía controlada;
- solucionarios permanecen privados;
- diapositivas se derivan después de estabilizar narrativa del participante.

---

## 15. Lo que NO está mal

Para evitar que el diagnóstico se lea como una condena:

- El contenido técnico es sólido y está trazado a fuente con página exacta (JCGM, QUAM, EN 14211, EPA, NISTIR, BIPM.QM-K1).
- El control documental es riguroso: la nota sobre APOA-370 vs. APNA-370 evita atribuir especificaciones equivocadas.
- Los datasets son reproducibles con semilla declarada (`20260819`).
- La separación curso teórico / práctica de laboratorio, con entregables evaluados independientes (M7 y E15), está bien argumentada.
- `build_paquete_html.py` ya valida archivos, filas, columnas, MathML, anclas, IDs únicos y ausencia de recursos externos. Es la base sobre la que se monta `build_capas.py`.
- `handout/no_nox/` ya es capa R correcta. Sirve de modelo para podar la de O₃.

El desfase es **de una capa y media**, no de arquitectura equivocada: contenido sobra, capa 0 y 1 están fusionadas, capas 2 y 3 no arrancaron.

---

## 16. Conclusión final

La inquietud inicial era válida: existía una sensación de que módulos y handouts se repetían, se completaban entre sí y no tenían fronteras claras. Sin embargo, la causa principal no era exceso de contenido ni una mala concepción del curso. Era ausencia de una arquitectura documental explícita.

La aclaración sobre la versión meta permite interpretar correctamente el estado actual:

1. los módulos no están simplemente sobrecargados; son una base avanzada del documento meta del autor e instructor;
2. el material teórico entregable todavía no existe como producto único, limpio y continuo, y en M5/M6/M8 ni siquiera tiene discurso redactado;
3. el handout O₃ mezcla contenido básico que debe incorporarse al relato principal con material avanzado que debe quedar como anexo, y duplica ~520 líneas de capa 1;
4. el handout NOx tiene más sentido como ficha operativa que como tratado paralelo;
5. vocabulario inicial, cadena `u → u_c → U`, cobertura, redondeo e informe GUM requieren mejor ubicación dentro de la narrativa — la inversión M1 ↔ M3 es la más urgente;
6. guion textual y diapositivas visuales deben derivarse del material teórico estabilizado, no de fuentes paralelas;
7. el mecanismo ya tiene precedente (`build_paquete_html.py`) y la convención de marcado ya existe de facto en los módulos; falta declararla y formalizarla;
8. el principal trabajo pendiente es editorial y arquitectónico, no una reconstrucción técnica.

El curso está avanzado en conocimiento y en preparación docente. Su siguiente etapa natural es convertir esa riqueza meta en una secuencia controlada de productos, cada uno con destinatario, propósito y profundidad definidos.
