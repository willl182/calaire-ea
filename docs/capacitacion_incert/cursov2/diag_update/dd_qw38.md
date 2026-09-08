# Diagnóstico final consolidado — cursov2

**Fecha:** 2026-08-28
**Directorio evaluado:** `docs/capacitacion_incert/cursov2/`
**Alcance:** arquitectura pedagógica y documental del curso; relación entre módulos, handouts, solucionarios, prácticas y futuras diapositivas.
**Estado:** diagnóstico consolidado. No se modificó ningún archivo.
**Origen:** síntesis de `diag_sol.md` (arquitectura y pedagogía) y `diag_opu.md` (evidencia cuantitativa y plan de ejecución).

---

## 1. Conclusión en una frase

El paquete no tiene un problema de contenido: tiene un problema de **capas sin declarar**. Cinco artefactos con audiencias distintas conviven en dos carpetas, dos de esos artefactos compiten por el mismo rol, y las capas de diapositivas no existen todavía. El curso está avanzado en conocimiento y preparación docente; el trabajo pendiente es editorial y arquitectónico, no de reconstrucción técnica.

---

## 2. El modelo de trabajo del autor

Flujo declarado, en orden de producción:

| # | Capa | Descripción | Pregunta rectora |
|---|---|---|---|
| **0** | **Meta / instructor** | Versión más cargada del material teórico. Teoría completa, hilo narrativo cercano al discurso oral, minutaje, ficha, prerrequisitos, organización de actividades, instrucciones de facilitación, preguntas al grupo, ejercicios y respuestas, resultados esperados, errores frecuentes, transiciones, procedencia exacta de fuentes, variantes según tiempo o nivel, contenido opcional, decisiones sobre qué incluir, simplificar o dejar como consulta. | ¿Qué necesito saber, recordar y tener disponible para enseñar bien este bloque? |
| **1** | **Material teórico del participante** | Prosa completa, hilo narrativo lógico y consecuente. Explicación, conceptos y definiciones, ecuaciones necesarias, ejemplos, figuras y tablas útiles, síntesis, ejercicios apropiados, referencias pertinentes. Es casi el discurso hablado. Se entrega como material teórico. | ¿Qué necesita leer y conservar el participante para comprender el curso después de la sesión? |
| **2** | **Guion textual de diapositivas** | Derivado de capa 1. Mismo orden conceptual, mismas conclusiones, mismos ejemplos esenciales, mismas definiciones operativas. Texto comprimido, telegráfico: frases cortas, una idea principal por diapositiva. | ¿Qué necesita estar escrito en pantalla mientras se explica esta idea? |
| **3** | **Diapositivas visuales** | Capa 2 + imágenes, diagramas, composición, jerarquía visual, tablas simplificadas, señales de énfasis, revelado progresivo. No introduce teoría nueva. | ¿Cómo hacer visible la idea sin convertir la diapositiva en una página del manual? |
| **R** | **Referencia de consulta** | (No es una etapa del flujo; artefacto perpendicular.) Glosario, tablas, fórmulas, checklists, anexos técnicos. Lo que el operador abre seis meses después en su puesto. | ¿Qué consulto sin releer el curso completo? |

Relación entre 0 y 1: **superconjunto**, no hermanos. Capa 1 se obtiene *quitando* bloques de capa 0, no reescribiendo. Capa 1 elimina o separa: minutaje, instrucciones como «dictar», «preguntar» o «mostrar», estrategia de facilitación, respuestas anticipadas, soluciones completas, resultados de demostraciones antes de realizarlas, comentarios editoriales y decisiones internas del autor.

Esta decisión gobierna todo el resto del diagnóstico.

---

## 3. Estado real de cada capa

| Capa | Dónde vive hoy | Volumen | Estado |
|---|---|---:|---|
| 0 — Meta | disperso dentro de `modulos/` + `modulos/soluciones/` | 607 + 1571 líneas | existe, **fusionado con capa 1** |
| 1 — Teórico participante | embebido en `modulos/`, sin separar | ~818 líneas (mezcladas) | existe, **no extraíble** |
| 2 — Guion de diapositivas | — | 0 | **no existe** |
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

Reconocer la capa meta corrige la interpretación: la densidad de los módulos, sus respuestas, su minutaje y sus instrucciones **no son defectos por sí mismos**. Son características coherentes con una versión meta. Ejemplos legítimos de contenido meta: M2 publica el resultado numérico del ejercicio; M4 entrega valores esperados de `u_c`, `U` y contribución dominante; M8 anticipa resultados y conclusiones de la demostración. El problema real es que ese rol no está declarado y no existe todavía una derivación limpia y sistemática hacia los demás productos.

---

## 5. Hallazgo derivado: el handout O₃ es un intento fallido de extraer la capa 1

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

Dentro de la capa R hay además dos subfunciones que conviene declarar:

1. **Anexos técnicos** — derivaciones, casos especiales, métodos opcionales, referencias normativas extensas: tratamiento detallado de autocorrelación, distribución t desplazada, PDFs arcoseno y trapezoidal, Welch–Satterthwaite detallado, Cholesky, desarrollos extendidos del método de Monte Carlo. Destinatarios: participantes que necesiten profundizar e instructor en preparación o consulta. No son lectura obligatoria.
2. **Fichas operativas y ayudas de campo** — checklists, fórmulas rápidas, criterios de aceptación, controles documentales, advertencias de montaje y seguridad. Consulta rápida durante práctica, operación o auditoría; no conducen por sí solas una actividad completa.

Criterio general: pertenece al material principal todo lo necesario para seguir los módulos obligatorios y resolver las actividades requeridas. Pertenece a referencia/anexos aquello que amplía, deriva o trata casos especiales sin ser necesario para completar el recorrido principal.

### 5.1 Asimetría O₃ / NOx

`handout/no_nox/` tiene 120 líneas en 10 archivos (`NOX_H03` = 7 líneas, `NOX_H08` = 3). M6 lo cita **una sola vez**. De facto ya funciona como capa R pura — checklist y control documental, sin duplicar a M6. Está mejor alineado que el de O₃, por accidente. Su utilidad real se parece a ficha operativa, referencia rápida, checklist de auditoría y ayuda de campo. No necesita mantener una simetría artificial con el handout O₃. Pero `README.md` presenta ambas familias como equivalentes.

### 5.2 Vacío de instrucción de uso

Búsqueda de `prelectura`, `lectura previa`, `antes del curso`, `leer.*handout` sobre `modulos/`, `README.md`, `diseno_curso_v2.md` y `handout/`: **0 resultados**. Nada dice si el handout se entrega antes, durante o después, ni si el participante debe leerlo.

---

## 6. Hallazgo sobre el orden de los términos metrológicos

La pregunta original —«¿no se deberían aclarar primero los términos?»— es correcta y apunta a una inversión real.

El vocabulario formal vive en `O3_H01` (mensurando, modelo de medición, error vs. incertidumbre, estándar/combinada/expandida, trazabilidad) y en el glosario `O3_H08`. Pero la secuencia de aula lo introduce operativamente antes:

| Momento | Términos usados | Dónde están definidos |
|---|---|---|
| M1 (min 0–35) | incertidumbre del patrón / del analizador / del valor transferido, corrección, incertidumbre residual, falla, doble conteo, covarianza | `O3_H01 §1.3`, `§1.4` — remitido, no dictado |
| M2 (min 35–83) | mensurando, coeficiente de sensibilidad | `O3_H01 §1.1`, `O3_H04 §4.1` |
| M3 (min 83–137) | **recién aquí** se definen Tipo A/B, PDF, combinación cuadrática | el módulo mismo |

`modulos/M1_trazabilidad.md:6` se autodeclara «establece el vocabulario y la arquitectura metrológica que se utilizarán en los módulos posteriores», pero `M1:111` delega ese vocabulario al handout. M1 pide prestado vocabulario que llega formalmente 82 min después, apoyándose en un documento cuyo momento de lectura nadie definió.

Además: la cadena `u_i → u_c → U = k·u_c` no tiene un dueño docente completamente claro; `U` y `k` aparecen en ejercicios y resultados, pero su introducción formal está principalmente en el handout. M2 trabaja con `u(T)` y `u(P)` antes de que M3 defina formalmente la incertidumbre estándar.

El glosario existe en `handout/gum_o3/O3_H08_glosario.md`, pero está ubicado como sección tardía y omite términos de alta frecuencia práctica: fotómetro de referencia estándar (SRP), repetibilidad, precisión intermedia, reproducibilidad, calibración/verificación/ajuste, doble conteo, escala completa, sesgo, patrón de transferencia, deriva de cero y de span.

Esta inversión **no se resuelve sola** al separar capas. Requiere decisión explícita. Dos salidas:

1. **Handout O₃ (capa R) como prelectura obligatoria**, con `O3_H00` + `O3_H01` + glosario marcados como lectura mínima. M1 puede entonces asumir el vocabulario. Riesgo: depende de que lean; alto en operadores de red.
2. **Bloque M0 de vocabulario, 15–20 min**, antes de M1: mensurando, error/corrección/incertidumbre, estándar/combinada/expandida, trazabilidad, Tipo A/B en versión mínima. M3 pasa a profundizar, no a introducir. Costo: 20 min de los 78 min de reserva logística. El glosario de capa R queda como su respaldo natural.

La opción 2 es robusta a que nadie lea nada antes. **Es la recomendada** si el curso se dicta a operadores sin envío previo de material.

La solución terminológica completa combina tres piezas:

1. un mapa inicial corto con términos indispensables para orientarse (bloque M0);
2. definiciones completas justo antes de operar con cada concepto (cada concepto con módulo dueño);
3. un glosario final de consulta ampliado (capa R).

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

## 8. Otros hallazgos pedagógicos que permanecen vigentes

Reconocer la capa meta corrige la interpretación de los módulos, pero no elimina estos problemas:

### 8.1 El informe GUM se exige antes de enseñarse de manera suficiente

M7 solicita un resultado auditable conforme a GUM §7, mientras que la lista más completa de elementos del informe vive en `handout/gum_o3/O3_H07_informe_gum.md`. También se evalúan cobertura, redondeo y coherencia entre presupuesto y resultado. Estos criterios deben aparecer dentro del material teórico antes del taller, no únicamente como apoyo consultado durante la revisión final.

### 8.2 «Cobertura» tiene varios sentidos

El curso usa «cobertura» para: factor, probabilidad o intervalo de cobertura en sentido GUM; alcance cubierto por una evidencia; «matriz de cobertura» como artefacto del curso. Esta colisión puede confundir al participante. Conviene reservar **cobertura** para el sentido metrológico GUM y usar **alcance de la evidencia** para expresar qué condiciones o fuentes cubre un dato.

### 8.3 Existe duplicación no gobernada

Autocorrelación, covarianza, propagación y otros conceptos aparecen con distintos niveles de detalle en módulos, handouts, solucionarios y protocolos. La repetición no es siempre incorrecta. Se vuelve problemática cuando no se sabe: cuál versión es canónica, cuál es resumen, cuál es ampliación, cuál se mantiene manualmente, cuál debe actualizarse cuando cambia la teoría.

### 8.4 Solucionarios y protocolos: duplicación aceptable con reglas

Los solucionarios son material privado del instructor. Actualmente también reexplican parte de la teoría; esa repetición es útil para que la solución sea legible de forma autónoma, pero no debe convertirse en otra fuente conceptual paralela. El meta maestro es canónico para contenido técnico, respuestas breves, propósito pedagógico y resultados esperados; el solucionario contiene la resolución completa, cálculos paso a paso, criterios de corrección y variantes aceptables.

Los protocolos E01–E16 necesitan cierto grado de autonomía porque se usan durante trabajo de laboratorio o campo. La duplicación debe ser deliberada: incluir lo necesario para ejecutar el protocolo sin abandonar la actividad; remitir al material teórico para fundamentos; evitar teoría alternativa o contradictoria; conservar la misma notación y terminología del material principal. A diferencia de una ficha, un protocolo conduce la ejecución completa de una actividad.

---

## 9. Hallazgo lateral: `solo_md/` es una capa derivada fuera de control

`solo_md/` replica el árbol completo (592 K) con los enlaces Markdown desanclados, para lectura fuera del repositorio.

- **No lo genera `build_paquete_html.py`** — `grep solo_md build_paquete_html.py` → 0 resultados.
- **No está en git** — sin historial; aparece como `??` en `git status`.
- **Ya divergió** de `modulos/`: M1 14 líneas, M3 16, M2 12, M7 10, M8 10, M4 8, M5 6, M6 2.

El delta es sistemático y benigno —quita `[texto](enlace)` y deja el texto—, pero la copia es manual y sin verificación. Es exactamente el patrón que produjo el problema del handout: dos archivos contando lo mismo, uno de ellos derivando en silencio.

Precedente positivo: `build_paquete_html.py` + `pandoc_rewrite_links.lua` ya generan `curso_paquete_completo.html` con validación de archivos, filas, anclas e IDs únicos. La infraestructura de derivación existe; `solo_md/` simplemente no la usa.

---

## 10. Arquitectura documental objetivo

```text
META MAESTRO (capa 0)
    ├── MATERIAL TEÓRICO DEL PARTICIPANTE (capa 1)
    │       └── GUION TEXTUAL DE DIAPOSITIVAS (capa 2)
    │               └── DIAPOSITIVAS VISUALES (capa 3)
    ├── ANEXOS TÉCNICOS (capa R)
    ├── FICHAS OPERATIVAS Y AYUDAS DE CAMPO (capa R)
    ├── PROTOCOLOS PRÁCTICOS (autonomía controlada)
    └── SOLUCIONARIOS DEL INSTRUCTOR (privado)
```

| Producto | Base actual | Destinatario y uso |
|---|---|---|
| A. Meta maestro privado | módulos M1–M8 | autor e instructor; fuente superior de intención pedagógica |
| B. Material teórico entregable | derivado del meta maestro | participante; manual breve y continuo, una sola narrativa |
| C. Anexos técnicos | contenido avanzado del handout O₃ | profundización e instructor; no lectura obligatoria |
| D. Fichas operativas | partes útiles del handout NOx y material práctico | consulta rápida en práctica, operación o auditoría |
| E. Protocolos prácticos | protocolos E01–E16 | laboratorio o campo; conducen la ejecución completa |
| F. Solucionarios privados | `modulos/soluciones/` | instructor; desarrollo completo, no tercera versión doctrinal |
| G. Guion textual de diapositivas | derivado del material teórico | base de capa 2 |
| H. Diapositivas visuales | derivadas del guion textual | capa 3 |

Dentro de este modelo: los módulos actuales alimentan principalmente el meta maestro; las partes básicas del handout O₃ se integran al material teórico; las partes avanzadas del handout O₃ se convierten en anexos; el handout NOx se redefine como ayuda operativa o ficha de campo; los protocolos conservan autonomía controlada; los solucionarios permanecen privados; las diapositivas se derivan después de estabilizar la narrativa del participante.

El material teórico debe poder leerse como un manual breve y continuo. Puede conservar la división M1–M8, pero cada módulo debe funcionar como capítulo de una sola narrativa, no como documento independiente que obliga a consultar otra fuente para completar ideas básicas.

### 10.1 Propiedad conceptual por módulo

Cada concepto operativo tiene un módulo dueño. Otros módulos pueden recordar el concepto, pero no redefinirlo de manera paralela:

- M1: trazabilidad, mensurando y vocabulario base;
- M2: modelo de medición y coeficientes de sensibilidad;
- M3: incertidumbre estándar, Tipo A/B, PDFs y combinación;
- M4: presupuesto, contribuciones, doble conteo, `U`, `k`, cobertura y redondeo;
- M5: patrones, regresión, residuos y alcance de evidencia;
- M6: modelo NOx, interferencias y covarianza;
- M7: integración, declaración del resultado e informe GUM;
- M8: validación opcional mediante MCM.

---

## 11. Reglas de derivación y control

Para evitar drift entre productos, conviene adoptar reglas explícitas.

**Regla 1. Una idea nueva nace en la capa meta.** Ninguna diapositiva, protocolo o solucionario debe introducir silenciosamente un concepto que no esté reconocido en la versión meta. Si una idea aparece por primera vez en un producto derivado, existe una ruptura en el flujo de derivación.

**Regla 2. Cada capa tiene autoridad definida.** El meta maestro es canónico para contenido técnico, definiciones, ecuaciones, notación e intención pedagógica. El material teórico es canónico para orden, redacción y experiencia del participante. Toda corrección técnica debe incorporarse primero al meta maestro y después propagarse a productos derivados.

**Regla 3. Las diapositivas reducen, no amplían.** Guion textual y diapositivas visuales pueden condensar, ilustrar y jerarquizar. No deben agregar teoría ausente del material teórico.

**Regla 4. Los anexos amplían sin interrumpir.** El relato principal debe ser comprensible sin leer todos los anexos. Los anexos permiten profundidad adicional, no reparación de huecos básicos. El handout O₃ debe dejar de completar silenciosamente huecos básicos de los módulos y asumir un papel explícito como referencia técnica.

**Regla 5. Fichas y protocolos repiten según su función.** Las fichas repiten solo lo necesario para consulta operativa rápida y no sustituyen una secuencia completa. Los protocolos repiten lo necesario para ejecutar una actividad de principio a fin. Ambos conservan notación, terminología y criterios del material principal.

**Regla 6. Las respuestas permanecen fuera del entregable principal.** El meta maestro conserva respuesta breve, resultado esperado y propósito pedagógico. El solucionario conserva resolución completa, cálculos paso a paso, criterios de corrección y variantes aceptables. Ninguno de estos contenidos debe anticiparse en el material teórico entregable.

**Regla 7. Cada concepto operativo tiene un dueño.** Según la distribución de §10.1.

---

## 12. Mecanismo propuesto: una fuente, marcado por audiencia

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
4. Si se necesita una lectura continua del meta maestro, se ensambla desde M1–M8; nunca otra copia mantenida manualmente.

---

## 13. Inventario de deuda

| # | Deuda | Impacto | Esfuerzo |
|---|---|---|---|
| D1 | M5, M6, M8 sin `Guion dictable` — capa 1 inexistente ahí | **bloqueante** para capas 1–3 | alto: redactar discurso |
| D2 | Tres convenciones distintas para el bloque de discurso | bloquea derivación mecánica | bajo: renombrar |
| D3 | `handout/gum_o3/` duplica ~520 líneas de capa 1 | confusión de roles, riesgo de drift | medio: podar a ~350 líneas |
| D4 | Rol del handout nunca declarado (prelectura / aula / consulta) | impide decidir el orden de términos | bajo: decisión + 1 párrafo en README |
| D5 | Inversión de vocabulario M1 ↔ M3; cadena `u → u_c → U` sin dueño claro | pedagógico, afecta a todos los participantes | medio: bloque M0 de 15–20 min |
| D6 | `solo_md/` derivado a mano, fuera de git, ya divergido | drift silencioso | bajo: generar o borrar |
| D7 | 27 `Idea fuerza` para ~120 subbloques-equivalentes | capa 2 arranca con ~20 % de semillas | alto, pero mecánico tras D2 |
| D8 | README presenta handout O₃ y NOx como equivalentes siendo asimétricos | expectativa falsa | bajo: 1 tabla en README |
| D9 | Informe GUM (cobertura, redondeo, coherencia) se evalúa en M7 antes de enseñarse en capa 1 | criterios de evaluación invisibles para el participante | medio: incorporar a material teórico |
| D10 | «Cobertura» usado con tres sentidos distintos | confusión terminológica | bajo: reservar término GUM + «alcance de la evidencia» |
| D11 | Glosario omite términos de alta frecuencia práctica (SRP, repetibilidad, sesgo, deriva, etc.) | glosario incompleto como referencia | bajo: ampliar glosario capa R |

### 13.1 Valoración del desfase global

**Desfase** expresa esfuerzo editorial y de consolidación necesario para alcanzar la arquitectura objetivo. No califica calidad técnica del contenido existente. Escala: **bajo** (existe, ajustes menores), **medio** (contenido existe, necesita consolidación o reclasificación), **alto** (producto o pipeline no existe y debe construirse).

| Aspecto | Desfase |
|---|---|
| Contenido técnico | bajo — ya existe en módulos, handouts, prácticas y solucionarios |
| Versión meta | bajo a medio — base sólida; falta declarar rol y cerrar saltos conceptuales |
| Material teórico del participante | medio a alto — contenido repartido; falta narrativa limpia y continua |
| Anexos y ayudas operativas | medio — funciones mezcladas bajo el nombre «handout» |
| Guion textual y diapositivas visuales | alto como pipeline formal — construir después de estabilizar el material teórico |

Diagnóstico global: no se requiere reconstruir el curso desde cero. Se requiere una reorganización editorial importante y una cadena de derivación explícita. En términos cualitativos: conocimiento avanzado; versión meta avanzada; narrativa entregable incompleta; clasificación de anexos ambigua; pipeline hacia diapositivas no consolidado. El desfase es **de una capa y media**, no de arquitectura equivocada: contenido sobra, capa 0 y 1 están fusionadas, capas 2 y 3 no arrancaron.

---

## 14. Plan propuesto

Orden por dependencia, no por importancia.

1. **Declarar las cinco capas** en `README.md` y fijar la convención de bloques de §12. Renombrar `handout/` → `referencia/` o declarar explícitamente su rol de capa R. Resuelve D4 y D8. Sin tocar contenido.
2. **Piloto en M5** — el módulo más incompleto: 0 subbloques, 1 `Idea fuerza`, sin discurso. Si el esquema aguanta ahí, aguanta en todos. Ataca D1 y D2 en el peor caso.
3. **`build_capas.py`**, siguiendo el patrón de `build_paquete_html.py`. `solo_md/` pasa a ser salida generada. Resuelve D6.
4. **Propagar el esquema** a M1–M4 y M7 (tienen discurso, solo falta etiquetar), después a M6 y M8 (hay que redactarlo). Cierra D1, D2.
5. **Podar el handout O₃** a capa R real: glosario ampliado (D11), tablas de PDFs, ley de propagación, checklist de informe. Las 30 anclas existentes siguen sirviendo. Cierra D3.
6. **Decidir el orden de términos**: bloque M0 de vocabulario (recomendado) o prelectura obligatoria de capa R. Cierra D5.
7. **Incorporar criterios del informe GUM** al material teórico antes del taller M7 y reservar «cobertura» para el sentido GUM. Cierra D9, D10.
8. **Capas 2 y 3** al final, cuando la derivación ya es mecánica. Cierra D7.

Estimación de volumen para capas 2 y 3: 462 min de curso obligatorio, a 2–3 min por diapositiva ⇒ **150–200 diapositivas**.

---

## 15. Lo que NO está mal

Para evitar que el diagnóstico se lea como una condena:

- El contenido técnico es sólido y está trazado a fuente con página exacta (JCGM, QUAM, EN 14211, EPA, NISTIR, BIPM.QM-K1).
- El control documental es riguroso: la nota sobre APOA-370 vs. APNA-370 evita atribuir especificaciones equivocadas.
- Los datasets son reproducibles con semilla declarada (`20260819`).
- La separación curso teórico / práctica de laboratorio, con entregables evaluados independientes (M7 y E15), está bien argumentada.
- `build_paquete_html.py` ya valida archivos, filas, columnas, MathML, anclas, IDs únicos y ausencia de recursos externos. Es la base sobre la que se monta `build_capas.py`.
- `handout/no_nox/` ya es capa R correcta. Sirve de modelo para podar la de O₃.

---

## 16. Conclusión final

La inquietud inicial era válida: existía una sensación de que módulos y handouts se repetían, se completaban entre sí y no tenían fronteras claras. La causa principal no era exceso de contenido ni una mala concepción del curso. Era ausencia de una arquitectura documental explícita.

1. Los módulos no están simplemente sobrecargados; son una base avanzada del documento meta del autor e instructor (42 % meta pura verificada).
2. El material teórico entregable todavía no existe como producto único, limpio y continuo; en M5, M6 y M8 ni siquiera hay discurso redactado.
3. El handout O₃ es una reescritura de la capa 1: ~520 líneas duplicadas, ~350 de capa R real; debe podarse y asumir papel explícito de referencia.
4. El handout NOx tiene más sentido como ficha operativa que como tratado paralelo; el README debe dejar de presentarlos como equivalentes.
5. Vocabulario inicial, cadena `u → u_c → U`, cobertura, redondeo e informe GUM requieren mejor ubicación dentro de la narrativa; se recomienda bloque M0 de 15–20 min.
6. Guion textual y diapositivas visuales deben derivarse del material teórico estabilizado, mediante `build_capas.py`, no de fuentes paralelas.
7. El principal trabajo pendiente es editorial y arquitectónico, no una reconstrucción técnica.

El curso está avanzado en conocimiento y en preparación docente. Su siguiente etapa natural es convertir esa riqueza meta en una secuencia controlada de productos, cada uno con destinatario, propósito y profundidad definidos.
