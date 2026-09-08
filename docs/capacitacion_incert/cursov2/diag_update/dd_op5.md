# Diagnóstico final consolidado — arquitectura documental de `cursov2`

**Directorio evaluado:** `docs/capacitacion_incert/cursov2/`
**Fecha:** 2026-08-28
**Estado:** diagnóstico. No se modificó ningún archivo del curso.
**Fuentes:** consolida `diag_sol.md` (marco conceptual del flujo autoral) y `diag_opu.md` (evidencia medida sobre el árbol). Las cifras se reverificaron sobre el estado actual del repositorio; donde difieren de los diagnósticos previos, manda este documento.

---

## 1. Conclusión en una frase

El paquete no tiene un problema de contenido: tiene un problema de **capas sin declarar**. Los módulos M1–M8 son ya una versión meta avanzada, pero cumplen simultáneamente el rol de material del participante; el handout de O₃ intenta cubrir ese rol por reescritura en lugar de por derivación; y las capas de diapositivas no existen. El trabajo pendiente es **editorial y arquitectónico, no técnico**.

---

## 2. Punto de partida y giro del diagnóstico

La evaluación arrancó con tres inquietudes:

1. si los términos metrológicos debían aclararse antes de iniciar los módulos;
2. si los módulos omitían contenido que había quedado solo en los handouts;
3. si los módulos ya funcionaban, de hecho, como su propio handout.

La primera lectura sugería que los módulos estaban sobrecargados y competían con los handouts. Esa interpretación era incompleta: faltaba declarar una pieza central del método de trabajo, la **versión meta del curso**.

Al reconocer esa capa cambia el diagnóstico. La densidad de los módulos, su minutaje, sus respuestas y sus instrucciones de facilitación **no son defectos**: son características coherentes con una capa 0. El problema real es doble:

- ese rol nunca se declaró;
- no existe una derivación limpia y sistemática hacia los demás productos.

---

## 3. Modelo de capas

Flujo declarado por el autor, en orden de producción, más un artefacto perpendicular.

| # | Capa | Pregunta rectora | Destinatario |
|---|---|---|---|
| **0** | **Meta maestro (autor/instructor)** | ¿Qué necesito saber, recordar y tener disponible para enseñar bien este bloque? | instructor |
| **1** | **Material teórico del participante** | ¿Qué necesita leer y conservar el participante para comprender el curso después de la sesión? | participante |
| **2** | **Guion textual de diapositivas** | ¿Qué necesita estar escrito en pantalla mientras se explica esta idea? | pantalla |
| **3** | **Diapositivas visuales** | ¿Cómo hacer visible la idea sin convertir la diapositiva en una página del manual? | pantalla |
| **R** | **Referencia de consulta** (no es etapa del flujo) | ¿Qué abre el operador seis meses después, en su puesto? | participante e instructor |

**Relación entre 0 y 1: superconjunto, no hermanos.** La capa 1 se obtiene *quitando* bloques de la capa 0, no reescribiéndola. Esta decisión gobierna todo el resto del diagnóstico: es exactamente la que el handout de O₃ incumplió.

### 3.1 Qué contiene cada capa

**Capa 0 — meta maestro.** Teoría completa; hilo narrativo cercano al discurso oral; propósito de cada bloque; secuencia pedagógica; transiciones; minutaje; instrucciones de facilitación; preguntas para el grupo; ejercicios y respuestas; resultados esperados; errores frecuentes; advertencias y puntos de énfasis; variantes según tiempo o nivel del grupo; contenido opcional; referencias y justificaciones; decisiones sobre qué incluir, simplificar o dejar como consulta. No se entrega al participante.

**Capa 1 — material teórico.** Mantiene explicación completa, hilo narrativo continuo, conceptos y definiciones, ecuaciones necesarias, ejemplos, figuras y tablas útiles, síntesis, ejercicios y referencias pertinentes. Elimina minutaje, instrucciones de tipo «dictar / preguntar / mostrar», estrategia de facilitación, respuestas anticipadas, soluciones completas, resultados de demostraciones antes de realizarlas, comentarios editoriales y decisiones internas del autor. Debe leerse como un manual breve y continuo: puede conservar la división M1–M8, pero cada módulo funciona como capítulo de una sola narrativa, no como documento independiente que obliga a consultar otra fuente para completar ideas básicas.

**Capa 2 — guion textual.** Deriva de la capa 1, no de una colección dispersa de módulos y handouts. Conserva el mismo orden conceptual, las mismas conclusiones, los mismos ejemplos esenciales y las mismas definiciones operativas. Reduce longitud, detalle, derivaciones, explicaciones secundarias y densidad verbal. Estilo telegráfico: una idea principal por diapositiva.

**Capa 3 — diapositivas visuales.** Deriva de la capa 2. Añade imágenes, diagramas, composición, jerarquía visual, tablas simplificadas, señales de énfasis y revelado progresivo. **No introduce teoría nueva.** Si una idea aparece por primera vez en la diapositiva visual, hay una ruptura en la cadena de derivación.

**Capa R — referencia.** Glosario, tablas, fórmulas, checklists, derivaciones avanzadas. Se consulta, no se lee en secuencia.

---

## 4. Estado real de cada capa

| Capa | Dónde vive hoy | Volumen | Estado |
|---|---|---:|---|
| 0 — Meta | `modulos/` + `modulos/soluciones/` | 1 489 + 1 571 líneas | existe, **fusionado con capa 1** |
| 1 — Teórico participante | embebido en `modulos/`, sin separar | ~818 líneas mezcladas | existe, **no extraíble** |
| 2 — Guion de diapositivas | — | 0 | **no existe** |
| 3 — Diapositivas visuales | — | 0 | **no existe** |
| R — Referencia | `handout/gum_o3/` + `handout/no_nox/` | 749 + 120 líneas | existe, **contaminado con capa 1 duplicada** (O₃) / **correcto** (NOx) |

Verificación de ausencia de las capas 2 y 3:

```
find . -iname "*slide*" -o -iname "*diapo*" -o -iname "*.pptx" \
       -o -iname "*reveal*" -o -iname "*beamer*"   →  0 resultados
```

---

## 5. Hallazgo principal: capas 0 y 1 comparten archivo

Reparto de líneas por rol de sección en los ocho módulos:

| Sección | Líneas | Audiencia |
|---|---:|---|
| Ficha + Objetivos (duración, prerrequisitos, materiales, distribución de tiempo) | 201 | solo instructor |
| Guion de exposición | 818 | **mezclado** |
| Ejercicio/actividad (enunciado, organización, tiempo, resultado esperado) | 245 | mezclado |
| Errores frecuentes + Cierre y transición | 161 | solo instructor |

Cerca del **42 % de `modulos/` es meta pura**, y el 57 % restante tampoco es limpio. Dentro del guion de exposición conviven marcadores de capas distintas (recuento sobre los ocho módulos, líneas coincidentes):

| Marcador | Ocurrencias | Capa |
|---|---:|---|
| `acumulado` (minutaje) | 45 | 0 |
| `Idea fuerza:` | 26 | 2 (semilla) |
| `Guion dictable` | 18 | 0 y 1 |
| `Apoyo en el handout:` | 17 | 0 |
| `Referencias exactas:` | 7 | 0 y 1 |
| `Enlace con la práctica:` | 5 | 0 |
| `Referencia integrada` | 4 | 0 y 1 |
| `Organización:` | 3 | 0 |
| `Párrafo dictable` | 3 | 0 y 1 |
| `Resultado esperado:` | 3 | 0 |
| `Conexión posterior` | 2 | 0 |
| `Pregunta de control:` | 1 | 0 |

Ejemplos concretos de contenido de capa 0 publicado donde el participante lo leería antes de tiempo:

- `modulos/M2_modelo_medicion.md` publica el resultado numérico del ejercicio;
- `modulos/M4_presupuesto_analizador.md` entrega los valores esperados de `u_c`, `U` y la contribución dominante;
- `modulos/M8_opcional_monte_carlo.md` anticipa resultados y conclusiones de la demostración.

**Consecuencia.** Un mismo archivo sirve a dos lectores con necesidades opuestas: el instructor quiere más carga, el participante quiere menos. Nadie queda bien servido. Los módulos no deben tratarse como error editorial ni convertirse directamente en handout: deben reconocerse como capa 0 y servir para producir la capa 1.

---

## 6. Hallazgo derivado: el handout de O₃ es un intento fallido de extraer la capa 1

`handout/gum_o3/` no es capa 0, no es capa 2, y solo parcialmente es capa R. Es una **reescritura** de la capa 1, no una extracción.

Solapamiento verificado:

- M3 §3.3 (PDFs y divisores) ≈ `O3_H03_tipo_b_pdfs.md`
- M2 §3.3 (coeficientes de sensibilidad) ≈ `O3_H04_propagacion_guf.md`
- M7 bloque 6 (informe) ≈ `O3_H07_informe_gum.md`
- M1 §3.1 (trazabilidad) ≈ `O3_H01 §1.5`

Contenido genuinamente único, es decir capa R legítima:

- `O3_H08_glosario.md` — 21 términos, no definidos en ningún módulo (45 líneas)
- `O3_H03` — tabla de PDFs con divisores
- `O3_H04` — ley de propagación en forma general
- `O3_H07` — checklist de informe GUM §7

De las 749 líneas, del orden de 350 son capa R real; el resto duplica narrativa.

### 6.1 Qué del handout O₃ sube a capa 1 y qué se queda en capa R

Suben al material teórico principal, porque son necesarios para seguir los módulos obligatorios y resolver las actividades requeridas:

- relación entre incertidumbre estándar, combinada y expandida;
- significado de `u`, `u_c`, `U` y `k`;
- vocabulario metrológico mínimo;
- noción de cobertura;
- reglas de presentación y redondeo;
- elementos mínimos de un informe conforme a GUM.

Permanecen como referencia avanzada, porque amplían, derivan o tratan casos especiales sin ser necesarios para completar el recorrido principal:

- tratamiento detallado de autocorrelación;
- distribución *t* desplazada;
- funciones de densidad de probabilidad (PDF) arcoseno y trapezoidal;
- Welch–Satterthwaite detallado;
- Cholesky;
- desarrollos extendidos del método de Monte Carlo (MCM).

El handout O₃ **no debe desaparecer**. Debe dejar de tapar en silencio huecos básicos de los módulos y asumir un papel explícito de capa R. Las 30 anclas existentes siguen sirviendo tras la poda.

### 6.2 Asimetría O₃ / NOx

`handout/no_nox/` tiene 120 líneas en 10 archivos (`NOX_H03` = 7 líneas, `NOX_H08` = 3). M6 lo cita **una sola vez**. De facto ya funciona como capa R pura —checklist y control documental, sin duplicar a M6—: está mejor alineado que el de O₃, por accidente, y sirve de modelo para podar el de O₃.

Su utilidad real es la de ficha operativa, referencia rápida, checklist de auditoría, ayuda de campo y recordatorio de fórmulas y controles documentales. **No necesita simetría artificial con el handout O₃.** Sin embargo, `README.md` presenta ambas familias como equivalentes, lo que crea una expectativa falsa.

### 6.3 Vacío de instrucción de uso

Búsqueda de `prelectura`, `lectura previa`, `antes del curso`, `leer.*handout` sobre `modulos/`, `README.md`, `diseno_curso_v2.md` y `handout/`: **0 resultados**. Nada dice si el handout se entrega antes, durante o después, ni si el participante debe leerlo. Esta indefinición es la que bloquea la decisión sobre el orden de los términos (§7).

---

## 7. Hallazgo pedagógico: inversión del vocabulario metrológico

La pregunta original —«¿no se deberían aclarar primero los términos?»— es correcta y apunta a una inversión real.

El vocabulario formal vive en `O3_H01` (mensurando, modelo de medición, error frente a incertidumbre, estándar/combinada/expandida, trazabilidad) y en el glosario `O3_H08`. Pero la secuencia de aula lo introduce operativamente antes:

| Momento | Términos usados | Dónde están definidos |
|---|---|---|
| M1 (min 0–35) | incertidumbre del patrón / del analizador / del valor transferido, corrección, incertidumbre residual, falla, doble conteo, covarianza | `O3_H01 §1.3`, `§1.4` — remitido, no dictado |
| M2 (min 35–83) | mensurando, coeficiente de sensibilidad | `O3_H01 §1.1`, `O3_H04 §4.1` |
| M3 (min 83–137) | **recién aquí** se definen Tipo A/B, PDF, combinación cuadrática | el módulo mismo |

`modulos/M1_trazabilidad.md:6` se autodeclara «establece el vocabulario y la arquitectura metrológica que se utilizarán en los módulos posteriores», pero `M1:111` delega ese vocabulario al handout. M1 pide prestado vocabulario que llega formalmente 82 min después, apoyándose en un documento cuyo momento de lectura nadie definió.

**Esta inversión no se resuelve sola al separar capas.** Requiere decisión explícita. Dos salidas:

1. **Handout O₃ (capa R) como prelectura obligatoria**, con `O3_H00` + `O3_H01` + glosario marcados como lectura mínima. M1 puede entonces asumir el vocabulario. Riesgo: depende de que lean; alto en operadores de red.
2. **Bloque M0 de vocabulario, 15–20 min**, antes de M1: mensurando, error/corrección/incertidumbre, estándar/combinada/expandida, trazabilidad y Tipo A/B en versión mínima. M3 pasa a profundizar, no a introducir. Costo: 20 min de los 78 min de reserva logística. El glosario de capa R queda como su respaldo natural.

**Recomendación: opción 2**, robusta a que nadie lea nada antes. Se aplica combinada en tres tiempos: mapa inicial corto con términos indispensables (M0); definición completa justo antes de operar con cada concepto (en su módulo dueño, §11); glosario final de consulta (capa R).

### 7.1 Términos de alta frecuencia ausentes del glosario

El glosario (`handout/gum_o3/O3_H08_glosario.md`) define 21 términos, algunos avanzados, y omite varios de uso práctico constante:

- fotómetro de referencia estándar (SRP);
- repetibilidad, precisión intermedia, reproducibilidad;
- calibración, verificación y ajuste;
- doble conteo;
- escala completa;
- sesgo;
- patrón de transferencia;
- deriva de cero y de span.

Además está ubicado como sección tardía del handout, no como puerta de entrada al curso.

### 7.2 Colisión terminológica: «cobertura»

El curso usa «cobertura» en tres sentidos: factor, probabilidad o intervalo de cobertura en sentido GUM; alcance cubierto por una evidencia; y «matriz de cobertura» como artefacto del curso. Conviene reservar **cobertura** para el sentido metrológico GUM y usar **alcance de la evidencia** para expresar qué condiciones o fuentes cubre un dato.

### 7.3 El informe GUM se exige antes de enseñarse

M7 solicita un resultado auditable conforme a GUM §7, mientras que la lista más completa de elementos del informe vive en `handout/gum_o3/O3_H07_informe_gum.md`. También se evalúan cobertura, redondeo y coherencia entre presupuesto y resultado. Estos criterios deben aparecer en la capa 1 antes del taller, no solo como apoyo consultado durante la revisión final.

---

## 8. Hallazgo estructural: la capa 1 no es extraíble en 4 de 8 módulos

Sin estructura regular, la derivación de las capas 1, 2 y 3 no se puede automatizar ni hacer consistente.

| Módulo | Subbloques `### 3.x` | `Idea fuerza` | Bloque de discurso |
|---|---:|---:|---|
| M1 | 5 | 5 | `Guion dictable` ×5 |
| M2 | 4 | 5 | `Guion dictable` ×4 |
| M3 | 4 | 5 | `Guion dictable` ×4 |
| M4 | 5 | 5 | `Guion dictable` ×5 |
| M5 | **0** | **1** | **ninguno** — §3 es prosa plana |
| M6 | 4 | **1** | **ninguno** |
| M7 | 0 (usa `### Bloque N` ×6) | 4 | `Párrafo dictable` ×3 |
| M8 | 0 | 1 | **ninguno** |

Tres convenciones distintas para el mismo objeto (`Guion dictable`, `Párrafo dictable`, ninguna) y dos esquemas de encabezado (`### 3.x` y `### Bloque N`).

**M5, M6 y M8 no tienen discurso redactado.** Tienen contenido, no narración. Para ellos la capa 1 no se puede extraer porque no hay qué extraer: hay que escribirla.

---

## 9. Hallazgo lateral: `solo_md/` es una capa derivada fuera de control

`solo_md/` replica el árbol completo (592 K) con los enlaces Markdown desanclados, para lectura fuera del repositorio.

- **No lo genera `build_paquete_html.py`** — `grep solo_md build_paquete_html.py` → 0 resultados.
- **No está en git** — sin historial; aparece como `??` en `git status`.
- **Ya divergió** de `modulos/`: M1 14 líneas, M3 16, M2 12, M7 10, M8 10, M4 8, M5 6, M6 2.

El delta es sistemático y benigno —quita `[texto](enlace)` y deja el texto—, pero la copia es manual y sin verificación. Es exactamente el patrón que produjo el problema del handout: dos archivos contando lo mismo, uno derivando en silencio.

Precedente positivo: `build_paquete_html.py` + `pandoc_rewrite_links.lua` ya generan `curso_paquete_completo.html` con validación de archivos, filas, anclas e IDs únicos. La infraestructura de derivación existe; `solo_md/` simplemente no la usa.

---

## 10. Arquitectura documental objetivo

Ocho productos, cada uno con base, destinatario y profundidad declarados.

```text
META MAESTRO (capa 0)
    ├── MATERIAL TEÓRICO DEL PARTICIPANTE (capa 1)
    │       └── GUION TEXTUAL DE DIAPOSITIVAS (capa 2)
    │               └── DIAPOSITIVAS VISUALES (capa 3)
    ├── ANEXOS TÉCNICOS ─────────┐
    ├── FICHAS OPERATIVAS ───────┤ capa R
    ├── PROTOCOLOS PRÁCTICOS ────┘
    └── SOLUCIONARIOS DEL INSTRUCTOR
```

**A. Meta maestro privado.** Base: módulos M1–M8, tratados como capítulos coordinados de un único meta maestro canónico. Si se necesita lectura continua, debe producirse mediante ensamblado generado desde M1–M8, **nunca mediante otra copia mantenida a mano**. Contiene teoría completa, discurso, decisiones pedagógicas, notas de instructor, tiempos, preguntas, respuestas, errores frecuentes, variantes, referencias y criterios de evaluación. Destinatario: instructor.

**B. Material teórico entregable.** Derivado de A por sustracción. Relato limpio y continuo, conceptos necesarios, ejemplos, fórmulas, conexiones entre módulos, síntesis y ejercicios sin revelar soluciones. Destinatario: participante. Es su fuente principal.

**C. Anexos técnicos.** Base: contenido avanzado del handout O₃. Derivaciones, casos especiales, métodos opcionales, referencias normativas extensas, material de profundización. Destinatario: participantes que profundizan e instructor en preparación. **No son lectura obligatoria** para completar el recorrido principal.

**D. Fichas operativas y ayudas de campo.** Base: `handout/no_nox/` y material práctico. Checklists, fórmulas rápidas, criterios de aceptación, controles documentales, advertencias de montaje y seguridad. Destinatario: participante durante práctica, operación o auditoría. Sirven para consulta rápida; **no conducen por sí solas una actividad completa**.

**E. Protocolos prácticos.** Base: `practica/` (protocolos E01–E09, E11, E14, E15, E16). Propósito y alcance, materiales y condiciones previas, secuencia completa de ejecución, datos a registrar, criterios de aceptación y cierre, y referencia al fundamento teórico. Destinatario: participante e instructor en laboratorio o campo. A diferencia de una ficha, **un protocolo conduce la ejecución completa de una actividad**.

**F. Solucionarios privados.** Resolución completa, cálculos paso a paso, criterios de corrección, errores típicos y variantes aceptables. Destinatario: instructor en preparación, acompañamiento y evaluación. El meta maestro conserva la respuesta breve y el resultado esperado; el solucionario conserva el desarrollo completo. Hoy los solucionarios reexplican teoría: esa repetición es tolerable para que la solución se lea de forma autónoma, pero **no debe convertirse en una tercera fuente doctrinal**.

**G. Guion textual de diapositivas.** Derivado de B. Títulos, frases cortas, estructura por diapositiva, mensajes centrales, indicaciones básicas de apoyo visual.

**H. Diapositivas visuales.** Derivadas de G. Diseño final, imágenes, diagramas, tablas simplificadas, composición y jerarquía visual.

---

## 11. Reglas de derivación y control

**Regla 1 — Una idea nueva nace en la capa meta.** Ninguna diapositiva, protocolo o solucionario introduce en silencio un concepto que no esté reconocido en la capa 0.

**Regla 2 — Cada capa tiene autoridad definida.** El meta maestro es canónico para contenido técnico, definiciones, ecuaciones, notación e intención pedagógica. El material teórico es canónico para orden, redacción y experiencia del participante. Toda corrección técnica entra primero al meta maestro y después se propaga.

**Regla 3 — Las diapositivas reducen, no amplían.** Capas 2 y 3 condensan, ilustran y jerarquizan; no agregan teoría ausente de la capa 1.

**Regla 4 — Los anexos amplían sin interrumpir.** El relato principal debe ser comprensible sin leer todos los anexos. Los anexos dan profundidad adicional, **no reparan huecos básicos**.

**Regla 5 — Fichas y protocolos repiten según su función.** Las fichas repiten solo lo necesario para consulta operativa rápida. Los protocolos repiten lo necesario para ejecutar una actividad de principio a fin, sin abandonar la actividad para consultar teoría. Ambos conservan notación, terminología y criterios de la capa 1, y remiten a ella para fundamentos. La duplicación es deliberada, nunca teoría alternativa o contradictoria.

**Regla 6 — Las respuestas permanecen fuera del entregable.** Ni resultados esperados ni soluciones se anticipan en la capa 1.

**Regla 7 — Cada concepto operativo tiene un módulo dueño.** Distribución objetivo:

- M0: vocabulario mínimo de orientación (nuevo, §7);
- M1: trazabilidad, mensurando y vocabulario base;
- M2: modelo de medición y coeficientes de sensibilidad;
- M3: incertidumbre estándar, Tipo A/B, PDFs y combinación;
- M4: presupuesto, contribuciones, doble conteo, `U`, `k`, cobertura y redondeo;
- M5: patrones, regresión, residuos y alcance de la evidencia;
- M6: modelo NOx, interferencias y covarianza;
- M7: integración, declaración del resultado e informe GUM;
- M8: validación opcional mediante MCM.

Otros módulos pueden recordar un concepto, pero no redefinirlo en paralelo. La cadena `u_i → u_c → U = k·u_c` debe quedar íntegramente bajo dueños de capa 1: hoy `U` y `k` aparecen en ejercicios y resultados, pero su introducción formal vive en el handout.

**Regla 8 — Toda copia es salida generada.** Ninguna réplica del contenido (`solo_md/`, ensamblados, exportaciones) se mantiene a mano. O la genera un script, o no existe.

---

## 12. Mecanismo propuesto: una fuente, marcado por audiencia

Fuente única por módulo (= capa 0). Las demás capas se generan quitando bloques. La convención ya existe de facto (`**Idea fuerza:**`, `**Guion dictable:**`, `**Apoyo en el handout:**`); falta que sea **regular y legible por máquina**. Esquema único por subbloque:

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
| capa 1 | `Guion dictable` + referencias cortas; sin minutaje, sin notas de facilitación, sin errores frecuentes, sin resultados esperados, sin punteros internos |
| capa 2 | `Idea fuerza` + `Puntos` |
| capa 3 | capa 2 + `Apoyo visual` como marcador de imagen |
| `solo_md/` | cualquiera de las anteriores, con enlaces desanclados |

Ventajas frente a mantener archivos paralelos:

1. Es lo que ya está escrito, sin querer.
2. Anti-drift: el handout O₃ y `solo_md/` demuestran qué pasa con dos archivos que cuentan lo mismo.
3. Un archivo por módulo, no dos ni cinco. Menos superficie que mantener.

---

## 13. Inventario de deuda

| # | Deuda | Impacto | Esfuerzo |
|---|---|---|---|
| D1 | M5, M6 y M8 sin discurso redactado — capa 1 inexistente ahí | **bloqueante** para capas 1–3 | alto: redactar |
| D2 | Tres convenciones distintas para el bloque de discurso; dos esquemas de encabezado | bloquea derivación mecánica | bajo: renombrar |
| D3 | `handout/gum_o3/` duplica ~400 líneas de capa 1 | confusión de roles, riesgo de drift | medio: podar a ~350 líneas |
| D4 | Rol del handout nunca declarado (prelectura / aula / consulta) | impide decidir el orden de términos | bajo: decisión + 1 párrafo en README |
| D5 | Inversión de vocabulario M1 ↔ M3 | pedagógico; afecta a todos los participantes | medio: bloque M0 de 15–20 min |
| D6 | `solo_md/` derivado a mano, fuera de git, ya divergido | drift silencioso | bajo: generar o borrar |
| D7 | 26 `Idea fuerza` para ~120 subbloques-equivalentes | capa 2 arranca con ~20 % de semillas | alto, pero mecánico tras D2 |
| D8 | README presenta handout O₃ y NOx como equivalentes siendo asimétricos | expectativa falsa | bajo: 1 tabla en README |
| D9 | Glosario incompleto (21 términos; faltan SRP, repetibilidad, sesgo, deriva, patrón de transferencia, doble conteo…) y ubicado al final | el participante no tiene puerta de entrada | bajo-medio: ampliar y reubicar |
| D10 | «Cobertura» con tres sentidos en circulación | ambigüedad conceptual | bajo: fijar término y sustituir |
| D11 | Resultados esperados y soluciones publicados en módulos (M2, M4, M8) | anticipan la respuesta si el módulo se entrega | se cierra solo con D2 + capa 1 |

---

## 14. Plan propuesto

Orden por dependencia, no por importancia.

1. **Declarar las cinco capas** en `README.md` y fijar la convención de bloques de §12. Renombrar `handout/` → `referencia/`, o declarar explícitamente su rol de capa R. Cierra D4 y D8. Sin tocar contenido.
2. **Piloto en M5**, el módulo más incompleto: 0 subbloques, 1 `Idea fuerza`, sin discurso. Si el esquema aguanta ahí, aguanta en todos. Ataca D1 y D2 en el peor caso.
3. **`build_capas.py`**, siguiendo el patrón de `build_paquete_html.py`. `solo_md/` pasa a ser salida generada. Cierra D6.
4. **Propagar el esquema** a M1–M4 y M7 (tienen discurso, solo falta etiquetar), después a M6 y M8 (hay que redactarlo). Cierra D1, D2 y, por construcción, D11.
5. **Podar el handout O₃** a capa R real: glosario, tabla de PDFs, ley de propagación, checklist de informe. Subir a capa 1 lo básico listado en §6.1. Las 30 anclas existentes siguen sirviendo. Cierra D3.
6. **Decidir el orden de términos**: bloque M0 de vocabulario (recomendado) o prelectura obligatoria de capa R. Ampliar y reubicar el glosario; fijar el uso de «cobertura». Cierra D5, D9 y D10.
7. **Capas 2 y 3** al final, cuando la derivación ya es mecánica. Cierra D7.

Producir las diapositivas antes de estabilizar la capa 1 consolidaría inconsistencias y multiplicaría el trabajo de revisión.

**Volumen estimado de capas 2 y 3:** 462 min de curso obligatorio, a 2–3 min por diapositiva ⇒ **150–200 diapositivas**.

---

## 15. Valoración del desfase

**Desfase** aquí expresa esfuerzo editorial y de consolidación hasta la arquitectura objetivo. No califica la calidad técnica del contenido existente.

- **bajo:** el producto existe y requiere ajustes menores de declaración, consistencia o limpieza;
- **medio:** el contenido existe, pero necesita consolidación, reclasificación o derivación significativa;
- **alto:** el producto o el pipeline no existe todavía como salida gobernada.

| Frente | Desfase |
|---|---|
| Contenido técnico | **bajo** — el conocimiento requerido ya existe en módulos, handouts, prácticas y solucionarios |
| Capa 0 (meta) | **bajo-medio** — base sólida; falta declarar el rol, cerrar saltos conceptuales y unificar convenciones |
| Capa 1 (teórico participante) | **medio-alto** — existe repartido; falta narrativa limpia, continua y entregable, y falta escribirla en M5, M6, M8 |
| Capa R (anexos y fichas) | **medio** — material valioso, pero referencia avanzada, resumen y ficha de campo están mezclados bajo el nombre «handout» |
| Capas 2 y 3 (diapositivas) | **alto como pipeline** — deben construirse después de estabilizar la capa 1 |

**Diagnóstico global.** No hay que reconstruir el curso. El desfase es **de una capa y media**, no de arquitectura equivocada: el contenido sobra, las capas 0 y 1 están fusionadas, y las capas 2 y 3 no arrancaron.

---

## 16. Lo que NO está mal

Para que el diagnóstico no se lea como condena:

- El contenido técnico es sólido y está trazado a fuente con página exacta (JCGM, QUAM, EN 14211, EPA, NISTIR, BIPM.QM-K1).
- El control documental es riguroso: la nota sobre APOA-370 frente a APNA-370 evita atribuir especificaciones equivocadas.
- Los datasets son reproducibles con semilla declarada (`20260819`).
- La separación curso teórico / práctica de laboratorio, con entregables evaluados independientes (M7 y E15), está bien argumentada.
- `build_paquete_html.py` ya valida archivos, filas, columnas, MathML, anclas, IDs únicos y ausencia de recursos externos. Es la base sobre la que se monta `build_capas.py`.
- `handout/no_nox/` ya es capa R correcta y sirve de modelo para podar la de O₃.

---

## 17. Conclusión

La inquietud inicial era válida: módulos y handouts se repetían, se completaban entre sí y no tenían fronteras claras. Pero la causa no era exceso de contenido ni mala concepción del curso, sino **ausencia de una arquitectura documental explícita**.

1. Los módulos no están sobrecargados: son una capa 0 avanzada que nunca se declaró como tal.
2. El material teórico entregable no existe todavía como producto único, limpio y continuo; en M5, M6 y M8 ni siquiera existe la materia prima narrativa.
3. El handout O₃ mezcla contenido básico que debe subir a la capa 1 con material avanzado que debe quedar como anexo.
4. El handout NOx ya es capa R correcta; el README no debe presentarlo como simétrico del de O₃.
5. Vocabulario inicial, cadena `u → u_c → U`, cobertura, redondeo e informe GUM requieren mejor ubicación dentro de la narrativa; el bloque M0 es la salida recomendada.
6. Guion textual y diapositivas visuales deben derivarse de la capa 1 estabilizada, no de fuentes paralelas.
7. Toda copia futura debe ser salida generada, no archivo mantenido a mano.

El curso está avanzado en conocimiento y en preparación docente. Su siguiente etapa natural es convertir esa riqueza meta en una secuencia controlada de productos, cada uno con destinatario, propósito y profundidad definidos.
