# Diagnóstico final — arquitectura documental cursov2

**Síntesis de:** `diag_sol.md` (arquitectura pedagógica, reglas, dueños conceptuales) + `diag_opu.md` (evidencia cuantificada, deuda, plan por dependencia).  
**Directorio evaluado:** `docs/capacitacion_incert/cursov2/`  
**Fecha:** 2026-08-28  
**Estado:** diagnóstico. No se modificó ningún archivo del curso.

---

## 1. Conclusión en una frase

El paquete no tiene déficit de contenido: tiene **capas sin declarar y sin reglas de derivación**. M1–M8 son ya una versión meta avanzada, fusionada en el mismo archivo con el material del participante; el handout O₃ intenta extraer ese material y falla; NOx ya es referencia; las diapositivas no existen. Separar capas no basta: hay inversión de vocabulario, conceptos usados antes de enseñarse y cuatro módulos sin discurso extraíble.

---

## 2. Punto de partida y aclaración decisiva

Tres inquietudes abrieron la evaluación:

1. ¿Los términos metrológicos deben aclararse antes de M1?
2. ¿Los módulos omiten contenido que solo vive en los handouts?
3. ¿Los módulos ya funcionan, en la práctica, como su propio handout?

La primera lectura mostraba mezcla de funciones. Los módulos cargan teoría, discurso, minutaje, instrucciones docentes, ejercicios, resultados y errores frecuentes. El handout O₃ mezcla básico y avanzado. El handout NOx resume M6 sin su profundidad. Los protocolos reexplican conceptos para usarse autónomos. Parecía sobrecarga y competencia entre productos.

Esa lectura era incompleta: faltaba declarar la **versión meta**. El flujo de autoría no empieza en el entregable. Empieza en una capa privada y cargada, para autor e instructor. Hoy esa función existe **distribuida en M1–M8**, sin gobernarse como sistema.

Pregunta rectora de la meta:

> ¿Qué necesito saber, recordar y tener disponible para enseñar bien este bloque?

Al reconocerla, cambia el diagnóstico: densidad, minutaje, respuestas y errores frecuentes no son defectos. Son coherentes con rol meta. El problema real es que ese rol no está declarado y no hay derivación limpia hacia los demás productos.

---

## 3. Flujo autoral correcto

Cuatro capas en eje de producción y artefactos perpendiculares. Relación 0→1: **superconjunto, no hermanos**. Capa 1 se obtiene *quitando* bloques de capa 0, no reescribiendo. Esa decisión gobierna el resto.

| # | Capa | Pregunta rectora | Qué mantiene / qué quita |
|---|---|---|---|
| **0** | **Meta maestro (autor/instructor)** | ¿Qué necesito para enseñar bien este bloque? | Teoría completa, discurso, minutaje, ficha, prerrequisitos, transiciones, preguntas, respuestas breves, errores frecuentes, variantes, procedencia exacta, criterios de evaluación. Privada. |
| **1** | **Material teórico del participante** | ¿Qué necesita leer y conservar para comprender después de la sesión? | Relato continuo, definiciones, ecuaciones, ejemplos, síntesis, ejercicios **sin** soluciones. Quita minutaje, «dictar/preguntar/mostrar», facilitación, respuestas, resultados de demostración, comentarios editoriales. |
| **2** | **Guion textual de diapositivas** | ¿Qué necesita estar escrito en pantalla? | Mismo orden, mismas conclusiones, mismas definiciones operativas. Reduce longitud, derivaciones y densidad verbal. Telegráfico: una idea por diapositiva. |
| **3** | **Diapositivas visuales** | ¿Cómo hacer visible la idea sin convertirla en página del manual? | Capa 2 + imagen, diagrama, jerarquía, revelado. **No introduce teoría nueva.** |
| **R** | **Referencia de consulta** | ¿Qué abre el operador seis meses después en su puesto? | Perpendicular al flujo. Glosario, tablas, fórmulas, checklists. No es etapa de producción. |

Productos auxiliares, con destinatario y repetición deliberada:

| Producto | Base actual | Función | Destinatario |
|---|---|---|---|
| **Anexos técnicos** | avanzado de `handout/gum_o3/` | profundización; no repara huecos del relato principal | participante que profundiza; instructor en preparación |
| **Fichas operativas** | `handout/no_nox/` + checklists | consulta rápida; no conducen una actividad completa | participante en práctica, operación o auditoría |
| **Protocolos E01–E16** | `practica/` | conducen ejecución de principio a fin; autonomía controlada | participante e instructor en laboratorio/campo |
| **Solucionarios** | `modulos/soluciones/` | resolución completa, criterios de corrección, variantes | instructor; privados |

```text
META MAESTRO (M1–M8 = capa 0)
    ├── MATERIAL TEÓRICO DEL PARTICIPANTE (capa 1)
    │       └── GUION TEXTUAL (capa 2)
    │               └── DIAPOSITIVAS VISUALES (capa 3)
    ├── ANEXOS TÉCNICOS
    ├── FICHAS OPERATIVAS
    ├── PROTOCOLOS PRÁCTICOS
    └── SOLUCIONARIOS PRIVADOS
            ⊥  REFERENCIA (glosario, tablas, fórmulas, checklists)
```

Capa 0 es canónica para contenido técnico, definiciones, ecuaciones, notación e intención pedagógica. Capa 1 es canónica para orden, redacción y experiencia del participante **después** de extraerse. Toda corrección técnica entra primero en capa 0 y se propaga.

---

## 4. Estado real de cada capa

| Capa | Dónde vive hoy | Volumen | Estado |
|---|---|---:|---|
| 0 — Meta | disperso en `modulos/` + `modulos/soluciones/` | 607 + 1571 líneas | existe, **fusionada con capa 1** |
| 1 — Teórico participante | embebida en `modulos/`, sin separar | ~818 líneas mezcladas | existe, **no extraíble** en 4 de 8 módulos |
| 2 — Guion de diapositivas | — | 0 | **no existe** |
| 3 — Diapositivas visuales | — | 0 | **no existe** |
| R — Referencia | `handout/gum_o3/` + `handout/no_nox/` | 869 + 120 líneas | existe; O₃ **contaminada** con duplicado de capa 1; NOx ya es R |

Verificación de ausencia de capas 2 y 3:

```text
find . -iname "*slide*" -o -iname "*diapo*" -o -iname "*.pptx" \
       -o -iname "*reveal*" -o -iname "*beamer*"   →  0 resultados
```

---

## 5. Hallazgos

### 5.1 Capa 0 y capa 1 comparten archivo

Reparto de líneas por rol de sección en los 8 módulos:

| Sección | Líneas | Audiencia |
|---|---:|---|
| Ficha + Objetivos (duración, prerrequisitos, materiales, distribución de tiempo) | 201 | solo instructor |
| Guion de exposición | 818 | **mezclado** |
| Ejercicio/actividad (enunciado, organización, tiempo, resultado esperado) | 245 | mezclado |
| Errores frecuentes + Cierre y transición | 161 | solo instructor |

**42 % de `modulos/` es meta pura.** El 57 % restante tampoco es limpio. Marcadores contados sobre los 8 módulos:

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

Ejemplos de contenido meta filtrado al entregable:

- M2 publica el resultado numérico del ejercicio en `modulos/M2_modelo_medicion.md`
- M4 entrega valores esperados de `u_c`, `U` y contribución dominante en `modulos/M4_presupuesto_analizador.md`
- M8 anticipa resultados y conclusiones de la demostración en `modulos/M8_opcional_monte_carlo.md`

Un mismo archivo sirve a dos lectores con necesidades opuestas. El instructor quiere más carga; el participante quiere menos.

### 5.2 El handout O₃ es un intento fallido de extraer capa 1; NOx ya es R

`handout/gum_o3/` no es capa 0, no es capa 2, y solo parcialmente es capa R. Es una **reescritura** de capa 1, no una extracción.

Solapamiento verificado:

- M3 §3.3 (PDFs y divisores) ≈ `O3_H03_tipo_b_pdfs.md`
- M2 §3.3 (coeficientes de sensibilidad) ≈ `O3_H04_propagacion_guf.md`
- M7 bloque 6 (informe) ≈ `O3_H07_informe_gum.md`
- M1 §3.1 (trazabilidad) ≈ `O3_H01` §1.5

Contenido genuinamente único (capa R o anexo legítimo):

- `O3_H08_glosario.md` — 23 términos, no definidos en ningún módulo
- `O3_H03` — tabla de PDFs con divisores
- `O3_H04` — ley de propagación en forma general
- `O3_H07` — checklist de informe GUM §7
- tratamiento detallado de autocorrelación, *t* desplazada, PDF arcoseno/trapezoidal, Welch–Satterthwaite, Cholesky, MCM extendido (anexos, no relato principal)

Estimación: de 869 líneas, ~350 son R/anexo real; ~520 duplican narrativa.

Criterio de corte: pertenece al material principal todo lo necesario para seguir los módulos obligatorios y resolver las actividades. Pertenece a anexos lo que amplía, deriva o trata casos especiales. Pertenece a R lo que se consulta en puesto (glosario, tablas, checklists).

**Asimetría O₃ / NOx.** `handout/no_nox/` tiene 120 líneas en 10 archivos (`NOX_H03` = 7 líneas, `NOX_H08` = 3). M6 lo cita **una sola vez**. De facto ya funciona como ficha/R: checklist y control documental, sin duplicar a M6. Está mejor alineado que el de O₃, por accidente. `README.md` presenta ambas familias como equivalentes.

**Vacío de instrucción de uso.** Búsqueda de `prelectura`, `lectura previa`, `antes del curso`, `leer.*handout` sobre `modulos/`, `README.md`, `diseno_curso_v2.md` y `handout/`: **0 resultados**. Nada dice si el handout se entrega antes, durante o después.

El handout O₃ no debe desaparecer. Debe dejar de completar silenciosamente huecos básicos de los módulos. El de NOx no necesita simetría artificial con O₃.

### 5.3 Inversión de vocabulario: se usa antes de definirse

La pregunta original —«¿no se deberían aclarar primero los términos?»— es correcta. El glosario vive en `O3_H08` como sección tardía del handout, no como puerta de entrada. Define algunos términos avanzados y omite varios de alta frecuencia práctica:

- fotómetro de referencia estándar (SRP)
- repetibilidad, precisión intermedia, reproducibilidad
- calibración, verificación y ajuste
- doble conteo, escala completa, sesgo
- patrón de transferencia
- deriva de cero y de span

La secuencia de aula introduce operativamente antes de definir:

| Momento | Términos usados | Dónde están definidos |
|---|---|---|
| M1 (min 0–35) | incertidumbre del patrón / del analizador / del valor transferido, corrección, incertidumbre residual, falla, doble conteo, covarianza | `O3_H01` §1.3, §1.4 — remitido, no dictado |
| M2 (min 35–83) | mensurando, coeficiente de sensibilidad; además `u(T)` y `u(P)` antes de que M3 defina incertidumbre estándar | `O3_H01` §1.1, `O3_H04` §4.1 |
| M3 (min 83–137) | **recién aquí** se definen Tipo A/B, PDF, combinación cuadrática | el módulo mismo |

`modulos/M1_trazabilidad.md:6` se autodeclara «establece el vocabulario y la arquitectura metrológica que se utilizarán en los módulos posteriores», pero `M1:111` delega ese vocabulario al handout. M1 pide prestado vocabulario que llega formalmente 82 min después, apoyándose en un documento cuyo momento de lectura nadie definió.

La cadena `u_i → u_c → U = k·u_c` no tiene dueño docente claro. `U` y `k` aparecen en ejercicios y resultados; su introducción formal está principalmente en el handout.

Esta inversión **no se resuelve sola** al separar capas. Requiere decisión explícita. Dos salidas:

1. **Capa R como prelectura obligatoria**, con `O3_H00` + `O3_H01` + glosario como lectura mínima. M1 asume el vocabulario. Riesgo: depende de que lean; alto en operadores de red.
2. **Bloque M0 de vocabulario, 15–20 min**, antes de M1: mensurando, error/corrección/incertidumbre, estándar/combinada/expandida, trazabilidad, Tipo A/B en versión mínima. M3 profundiza, no introduce. Costo: 20 min de los 78 min de reserva logística.

La opción 2 es robusta a que nadie lea nada antes. Es la recomendada si el curso se dicta a operadores sin envío previo. Encaja con el esquema de tres niveles de `diag_sol.md`:

1. mapa inicial corto (M0) con términos indispensables;
2. definiciones completas justo antes de operar con cada concepto (dueño por módulo, §8);
3. glosario final de consulta (capa R).

### 5.4 Informe GUM y colisión de «cobertura»

M7 solicita un resultado auditable conforme a GUM §7, mientras que la lista más completa de elementos del informe vive en `O3_H07_informe_gum.md`. También se evalúan cobertura, redondeo y coherencia entre presupuesto y resultado. Esos criterios deben aparecer en capa 1 **antes** del taller, no solo como apoyo durante la revisión final.

El curso usa «cobertura» para tres cosas:

- factor, probabilidad o intervalo de cobertura en sentido GUM;
- alcance cubierto por una evidencia;
- «matriz de cobertura» como artefacto del curso.

Reservar **cobertura** para el sentido metrológico GUM. Usar **alcance de la evidencia** para lo que cubre un dato.

### 5.5 Uniformidad: capa 1 no es extraíble en 4 de 8 módulos

Sin estructura regular, la derivación de capas 1, 2 y 3 no se automatiza ni se hace consistente.

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

Tres nombres para el mismo objeto: `Guion dictable`, `Párrafo dictable`, ninguno. Dos esquemas de encabezado: `### 3.x` y `### Bloque N`.

**M5, M6 y M8 no tienen discurso redactado.** Tienen contenido, no narración. Para ellos, capa 1 no se extrae: hay que escribirla.

### 5.6 Duplicación no gobernada

Autocorrelación, covarianza, propagación y otros conceptos aparecen con distintos niveles de detalle en módulos, handouts, solucionarios y protocolos. La repetición no es siempre incorrecta. Se vuelve problemática cuando no se sabe cuál versión es canónica, cuál es resumen, cuál es ampliación, cuál se mantiene a mano y cuál debe actualizarse cuando cambia la teoría.

Los solucionarios reexplican parte de la teoría para ser legibles autónomos. Esa repetición puede ser útil; no debe convertirse en tercera fuente doctrinal. Capa 0 conserva respuesta breve, propósito y resultado esperado. El solucionario conserva desarrollo completo, cálculos, criterios de corrección y variantes aceptables.

Los protocolos E01–E16 necesitan autonomía de laboratorio/campo. Duplicación deliberada: lo necesario para ejecutar sin abandonar la actividad; remisión a capa 1 para fundamentos; misma notación y terminología; ninguna teoría alternativa.

### 5.7 `solo_md/` es una capa derivada fuera de control

`solo_md/` replica el árbol completo (592 K) con enlaces Markdown desanclados, para lectura fuera del repositorio.

- **No lo genera** `build_paquete_html.py` (`grep solo_md` → 0).
- **No está en git** — aparece como `??`.
- **Ya divergió** de `modulos/`: M1 14 líneas, M3 16, M2 12, M7 10, M8 10, M4 8, M5 6, M6 2.

El delta es sistemático y benigno —quita `[texto](enlace)` y deja el texto—, pero la copia es manual y sin verificación. Es el mismo patrón que produjo el problema del handout: dos archivos contando lo mismo, uno derivando en silencio.

Precedente positivo: `build_paquete_html.py` + `pandoc_rewrite_links.lua` ya generan `curso_paquete_completo.html` con validación de archivos, filas, anclas e IDs únicos. La infraestructura de derivación existe; `solo_md/` no la usa.

---

## 6. Mecanismo propuesto: una fuente, marcado por audiencia

Fuente única por módulo = capa 0. Las demás capas se generan quitando bloques. Ya existe la convención de facto (`**Idea fuerza:**`, `**Guion dictable:**`, `**Apoyo en el handout:**`). Falta que sea **regular y legible por máquina**.

Esquema único por subbloque:

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

Un `build_capas.py`, siguiendo el patrón de `build_paquete_html.py`, emite:

| Salida | Regla |
|---|---|
| capa 0 | el archivo tal cual |
| capa 1 | `Guion dictable` + referencias cortas; sin minutaje, sin notas de facilitación, sin errores frecuentes, sin punteros internos, sin resultados anticipados |
| capa 2 | `Idea fuerza` + `Puntos` |
| capa 3 | capa 2 + `Apoyo visual` como marcador de imagen |
| `solo_md/` | cualquiera de las anteriores, con enlaces desanclados |

Ventajas frente a archivos paralelos mantenidos a mano:

1. Es lo que ya está escrito, sin querer.
2. Anti-drift: el handout y `solo_md/` demuestran qué pasa con dos archivos que cuentan lo mismo.
3. Un archivo por módulo, no dos ni cinco.

---

## 7. Reglas de derivación y control

### Regla 1. Una idea nueva nace en capa 0

Ninguna diapositiva, protocolo, ficha o solucionario introduce silenciosamente un concepto no reconocido en la versión meta.

### Regla 2. Cada capa tiene autoridad definida

Capa 0 es canónica para contenido técnico, definiciones, ecuaciones, notación e intención pedagógica. Capa 1 es canónica para orden, redacción y experiencia del participante. Toda corrección técnica entra primero en capa 0 y se propaga.

### Regla 3. Las diapositivas reducen, no amplían

Guion textual y diapositivas visuales condensan, ilustran y jerarquizan. No agregan teoría ausente de capa 1.

### Regla 4. Los anexos amplían sin interrumpir

El relato principal se comprende sin leer todos los anexos. Los anexos dan profundidad, no reparan huecos básicos.

### Regla 5. Fichas y protocolos repiten según su función

Las fichas repiten solo lo necesario para consulta operativa rápida. Los protocolos repiten lo necesario para ejecutar una actividad de principio a fin. Ambos conservan notación, terminología y criterios de capa 1.

### Regla 6. Las respuestas permanecen fuera del entregable

Capa 0 conserva respuesta breve, resultado esperado y propósito pedagógico. El solucionario conserva resolución completa, cálculos, criterios de corrección y variantes. Ninguno de esos contenidos se anticipa en capa 1.

### Regla 7. Cada concepto operativo tiene un dueño

Otros módulos pueden recordar el concepto; no lo redefinen en paralelo. Ver §8.

### Regla 8. Derivados se generan, no se copian

`solo_md/`, capa 1 extraída, capa 2 y capa 3 salen de un pipeline. Una copia manual es deuda, no producto.

---

## 8. Dueños conceptuales

Distribución objetivo. Cada concepto operativo se introduce en su módulo dueño **antes** de exigirse su uso.

| Módulo | Dueño de |
|---|---|
| **M0** (propuesto) | mapa mínimo: mensurando, error/corrección/incertidumbre, `u` / `u_c` / `U`, trazabilidad, Tipo A/B en versión corta |
| **M1** | trazabilidad, mensurando, vocabulario base de la cadena de transferencia |
| **M2** | modelo de medición y coeficientes de sensibilidad |
| **M3** | incertidumbre estándar, Tipo A/B, PDFs y combinación (profundización de M0) |
| **M4** | presupuesto, contribuciones, doble conteo, `U`, `k`, cobertura GUM y redondeo |
| **M5** | patrones, regresión, residuos y **alcance de evidencia** |
| **M6** | modelo NOx, interferencias y covarianza |
| **M7** | integración, declaración del resultado e informe GUM §7 (elementos en capa 1, no solo en R) |
| **M8** | validación opcional mediante MCM |

---

## 9. Inventario de deuda

| # | Deuda | Impacto | Esfuerzo |
|---|---|---|---|
| D1 | M5, M6, M8 sin `Guion dictable` — capa 1 inexistente ahí | **bloqueante** para capas 1–3 | alto: redactar discurso |
| D2 | Tres convenciones distintas para el bloque de discurso | bloquea derivación mecánica | bajo: renombrar |
| D3 | `handout/gum_o3/` duplica ~520 líneas de capa 1 | confusión de roles, drift | medio: podar a ~350 líneas R/anexo |
| D4 | Rol del handout nunca declarado (prelectura / aula / consulta) | impide decidir el orden de términos | bajo: decisión + 1 párrafo en README |
| D5 | Inversión de vocabulario M1 ↔ M3, más términos de alta frecuencia ausentes del glosario | pedagógico; afecta a todos los participantes | medio: bloque M0 15–20 min + ampliar glosario R |
| D6 | `solo_md/` derivado a mano, fuera de git, ya divergido | drift silencioso | bajo: generar o borrar |
| D7 | 27 `Idea fuerza` para ~120 subbloques-equivalentes | capa 2 arranca con ~20 % de semillas | alto, pero mecánico tras D2 |
| D8 | README presenta handout O₃ y NOx como equivalentes siendo asimétricos | expectativa falsa | bajo: 1 tabla en README |
| D9 | Cadena `u → u_c → U` y elementos del informe GUM §7 viven en handout, se exigen en M4/M7 | el participante no puede cumplir el taller con solo capa 1 | medio: mover al dueño (M4, M7) |
| D10 | «Cobertura» con tres sentidos | confusión de aula | bajo: reservar término GUM; «alcance de evidencia» en M5 |

---

## 10. Plan propuesto

Orden por dependencia, no por importancia.

1. **Declarar las capas** en `README.md` y fijar la convención de bloques de §6. Renombrar `handout/` → `referencia/` o declarar explícitamente su rol (R + anexos + fichas). Distinguir O₃ (podar) de NOx (ya es ficha). Resuelve D4 y D8. Sin tocar contenido.
2. **Piloto en M5** — el módulo más incompleto: 0 subbloques, 1 `Idea fuerza`, sin discurso. Si el esquema aguanta ahí, aguanta en todos. Ataca D1 y D2 en el peor caso.
3. **`build_capas.py`**, siguiendo el patrón de `build_paquete_html.py`. `solo_md/` pasa a ser salida generada. Resuelve D6.
4. **Propagar el esquema** a M1–M4 y M7 (tienen discurso; falta etiquetar), después a M6 y M8 (hay que redactarlo). Cierra D1, D2.
5. **Podar el handout O₃** a R/anexo real: glosario, tablas de PDFs, ley de propagación, checklist de informe, desarrollos avanzados. Integrar al relato principal lo básico que hoy solo vive ahí (`u`/`u_c`/`U`, redondeo, elementos de informe). Las 30 anclas existentes siguen sirviendo. Cierra D3 y D9.
6. **Decidir el orden de términos:** bloque M0 de vocabulario (recomendado) o prelectura obligatoria de capa R. Ampliar el glosario con términos de alta frecuencia. Reservar «cobertura». Cierra D5 y D10.
7. **Capas 2 y 3** al final, cuando la derivación ya es mecánica. Cierra D7.

Estimación de volumen para capas 2 y 3: 462 min de curso obligatorio, a 2–3 min por diapositiva ⇒ **150–200 diapositivas**. Producirlas antes de estabilizar capa 1 consolidaría inconsistencias y multiplicaría revisión.

---

## 11. Valoración del desfase

**Desfase** = esfuerzo editorial y de consolidación para alcanzar la arquitectura objetivo. No califica calidad técnica del contenido.

Escala: **bajo** = existe, ajustes menores de declaración o limpieza; **medio** = existe, necesita consolidación, reclasificación o derivación; **alto** = producto o pipeline aún no existe como salida gobernada.

| Dimensión | Desfase | Lectura |
|---|---|---|
| Contenido técnico | **bajo** | conocimiento requerido ya está en módulos, handouts, prácticas y solucionarios |
| Versión meta (capa 0) | **bajo a medio** | M1–M8 son base sólida; falta declarar rol, cerrar saltos, uniformar |
| Material teórico (capa 1) | **medio a alto** | contenido repartido; 4 de 8 módulos sin discurso extraíble |
| Anexos, fichas y R | **medio** | material valioso; funciones mezcladas bajo el nombre «handout» |
| Guion y diapositivas (2–3) | **alto como pipeline** | 0 archivos; construir después de estabilizar capa 1 |
| `solo_md/` | **bajo** (operativo) | patrón de drift; se resuelve generando |

Diagnóstico global: no se reconstruye el curso desde cero. Se requiere reorganización editorial y cadena de derivación explícita. En términos cualitativos:

- conocimiento: avanzado;
- versión meta: avanzada;
- narrativa entregable: incompleta;
- clasificación de anexos/fichas/R: ambigua;
- pipeline hacia diapositivas: no consolidado.

El desfase es **de una capa y media**, no de arquitectura equivocada: contenido sobra, capas 0 y 1 están fusionadas, capas 2 y 3 no arrancaron, y tres desajustes pedagógicos (vocabulario, informe GUM, cobertura) sobreviven a la separación de capas.

---

## 12. Lo que no está mal

- El contenido técnico es sólido y está trazado a fuente con página exacta (JCGM, QUAM, EN 14211, EPA, NISTIR, BIPM.QM-K1).
- El control documental es riguroso: la nota sobre APOA-370 vs. APNA-370 evita atribuir especificaciones equivocadas.
- Los datasets son reproducibles con semilla declarada (`20260819`).
- La separación curso teórico / práctica de laboratorio, con entregables evaluados independientes (M7 y E15), está bien argumentada.
- `build_paquete_html.py` ya valida archivos, filas, columnas, MathML, anclas, IDs únicos y ausencia de recursos externos. Es la base sobre la que se monta `build_capas.py`.
- `handout/no_nox/` ya es capa R/ficha correcta. Sirve de modelo para podar la de O₃.
- Los protocolos E01–E16 y los solucionarios son productos legítimos; no hay que eliminarlos, hay que gobernar su repetición.

---

## 13. Conclusión

La inquietud inicial era válida: módulos y handouts se repetían, se completaban entre sí y no tenían fronteras claras. La causa no era exceso de contenido ni mala concepción del curso. Era ausencia de una arquitectura documental explícita.

1. Los módulos no están simplemente sobrecargados; son una base avanzada del documento meta del autor e instructor.
2. El material teórico entregable todavía no existe como producto único, limpio y continuo; en M5, M6 y M8 no hay siquiera discurso que extraer.
3. El handout O₃ mezcla contenido básico que debe incorporarse al relato principal con material avanzado que debe quedar como anexo o R; el de NOx ya es ficha y no debe forzarse a simetría.
4. Vocabulario inicial, cadena `u → u_c → U`, cobertura, redondeo e informe GUM requieren ubicación dentro de la narrativa, no solo en consulta. Un M0 corto es la salida robusta.
5. Guion textual y diapositivas visuales se derivan del material teórico estabilizado, no de fuentes paralelas. Estimación: 150–200 diapositivas.
6. `solo_md/` y el handout duplicado ilustran el mismo anti-patrón: copia manual. Los derivados se generan.
7. El trabajo pendiente es editorial, arquitectónico y de marcado; no una reconstrucción técnica.

El curso está avanzado en conocimiento y en preparación docente. La siguiente etapa es convertir esa riqueza meta en una secuencia controlada de productos, cada uno con destinatario, propósito, profundidad y regla de derivación.
