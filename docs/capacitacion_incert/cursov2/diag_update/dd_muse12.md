# Diagnóstico final integrado — arquitectura documental cursov2

**Síntesis de:** `diag_sol.md` + `diag_opu.md`  
**Directorio evaluado:** `docs/capacitacion_incert/cursov2/`  
**Fecha:** 2026-08-28  
**Estado:** diagnóstico integrado. No se modificó ningún archivo del curso.

---

## 1. Conclusión en una frase

El curso no tiene déficit de contenido: tiene **capas sin declarar**. Cinco artefactos con audiencias distintas conviven en dos carpetas, dos compiten por el mismo rol (módulo vs. handout como material del participante) y las capas de diapositivas no existen todavía. La densidad de M1–M8 no es defecto: es la **versión meta** bien cargada, pero fusionada con el entregable.

---

## 2. Punto de partida y aclaración decisiva

### 2.1 Tres inquietudes iniciales

1. ¿Términos metrológicos deben aclararse antes de M1?
2. ¿Módulos omiten contenido que solo vive en handouts?
3. ¿Módulos ya funcionan como su propio handout?

Lectura inicial mostraba mezcla de funciones: teoría, discurso, minutaje, instrucciones docentes, ejercicios con resultado, errores frecuentes. Handout O₃ mezcla básico y avanzado; handout NOx resume M6 sin su profundidad; protocolos reexplican conceptos para ser autónomos. Parecía sobrecarga.

### 2.2 La capa meta ya existe — distribuida

Flujo real de autoría no empieza en el entregable. Empieza en capa privada y cargada para autor/instructor. Hoy esa función **meta existe distribuida en M1–M8** (`modulos/M1_trazabilidad.md` a `M8_opcional_monte_carlo.md`), pero sin declarar ni gobernar.

Meta maestro objetivo debe contener — pregunta rectora: *¿Qué necesito saber, recordar y tener disponible para enseñar bien este bloque?*

- teoría completa, hilo narrativo cercano al discurso oral
- propósito, secuencia, transiciones, minutaje, preguntas de control
- instrucciones de facilitación, dónde se atasca el grupo y cómo destrabar
- ejercicios, respuestas breves, resultados esperados, errores frecuentes
- variantes por tiempo/nivel, contenido opcional, advertencias y énfasis
- referencias exactas con página, justificaciones y decisiones de alcance

No es handout ni entregable. Es fuente pedagógica superior. Al reconocerla, el diagnóstico cambia: minutaje, respuestas y densidad no son defectos — son coherentes con rol meta. El problema es ausencia de derivación limpia hacia demás productos.

---

## 3. Flujo autoral correcto

Cuatro capas principales + artefactos perpendiculares. Relación 0→1 es **superconjunto**: capa 1 se obtiene quitando bloques de capa 0, no reescribiendo.

| # | Capa | Descripción | Pregunta rectora |
|---|---|---|---|
| **0** | **Meta / instructor** | Versión más cargada. Minutaje, ficha, prerrequisitos, transiciones, procedencia exacta, soluciones, errores frecuentes. | ¿Qué necesito para enseñar bien? |
| **1** | **Material teórico del participante** | Prosa completa, hilo lógico. Casi el discurso hablado. Entregable. | ¿Qué necesita leer y conservar para comprender después? |
| **2** | **Diapositivas texto** | Derivada de capa 1. Texto telegráfico, 1 idea/diapa. | ¿Qué debe estar escrito en pantalla? |
| **3** | **Diapositivas finales** | Capa 2 + imagen, diagrama, jerarquía visual. No añade teoría. | ¿Cómo hacer visible sin convertir en página del manual? |
| **R** | **Referencia de consulta** | Perpendicular, no etapa. Glosario, tablas PDFs/divisores, checklists. Lo que abre 6 meses después. | ¿Qué necesita consultar rápido en puesto? |

**Productos auxiliares** (derivados, no capas): anexos técnicos (profundización), fichas operativas/checklists, protocolos prácticos E01–E16 (autónomos para ejecutar), solucionarios privados.

```
META MAESTRO (M1–M8)
    ├── MATERIAL TEÓRICO DEL PARTICIPANTE (capa 1)
    │       └── GUION TEXTUAL (capa 2) → DIAPOSITIVAS VISUALES (capa 3)
    ├── ANEXOS TÉCNICOS (handout O₃ avanzado podado)
    ├── FICHAS OPERATIVAS (handout NOx + checklists)
    ├── PROTOCOLOS PRÁCTICOS (E01–E16)
    └── SOLUCIONARIOS PRIVADOS
            ↑ perpendicular: REFERENCIA (glosario, tablas, fórmulas)
```

---

## 4. Estado real y evidencia cuantificada

### 4.1 Dónde vive cada capa hoy

| Capa | Ubicación actual | Volumen | Estado |
|---|---|---:|---|
| 0 — Meta | disperso en `modulos/` + `modulos/soluciones/` | 607 + 1571 líneas | existe, **fusionado con capa 1** |
| 1 — Teórico | embebido en `modulos/`, sin separar | ~818 líneas mezcladas | existe, **no extraíble limpio** |
| 2 — Diapo texto | — | 0 | **no existe** |
| 3 — Diapo final | — | 0 | **no existe** |
| R — Referencia | `handout/gum_o3/` (869 l) + `handout/no_nox/` (120 l) | 989 líneas | existe, **contaminado con duplicado capa 1** |

Verificación ausencia capas 2/3: `find . -iname "*slide*|*diapo*|*.pptx|*reveal*|*beamer*"` → 0 resultados.

### 4.2 Capa 0 y 1 comparten archivo — cuantificación

Reparto en M1–M8 (1425 líneas analizadas):

| Sección | Líneas | Audiencia |
|---|---:|---|
| Ficha + Objetivos (duración, prerrequisitos, materiales) | 201 | solo instructor (0) |
| Guion de exposición | 818 | **mezclado** |
| Ejercicio/actividad (enunciado, organización, resultado esperado) | 245 | mezclado |
| Errores frecuentes + Cierre y transición | 161 | solo instructor (0) |

**42 % de `modulos/` es meta pura.** Resto tampoco limpio: dentro del guion conviven marcadores:

| Marcador | Ocurr. | Capa |
|---|---:|---|
| `acumulado` (minutaje) | 45 | 0 |
| `Idea fuerza:` | 27 | 2 (semilla) |
| `Apoyo en el handout:` | 17 | 0 |
| `Referencias exactas:` | 7 | 0+1 |
| `Resultado esperado:` | 7 | 0 |
| `Enlace con la práctica:` | 5 | 0 |

Mismo archivo sirve a lectores opuestos: instructor quiere más carga, participante quiere menos.

### 4.3 Ubicación de materiales actuales en el flujo

**M1–M8:** se acercan a **meta**. Ejemplos: `modulos/M2_modelo_medicion.md` publica resultado numérico; `modulos/M4_presupuesto_analizador.md` entrega `u_c`, `U` y contribución dominante; `modulos/M8_opcional_monte_carlo.md` anticipa conclusiones de demostración. Útil para instructor, no para entregable.

**Handout GUM/O₃ (`handout/gum_o3/`):** mezcla dos funciones.  
*Básico — debe migrar a capa 1:* relación `u → u_c → U=k·u_c`, significado `u/u_c/U/k`, vocabulario mínimo, cobertura, redondeo, elementos mínimos informe GUM §7.  
*Avanzado — permanece como anexo/R:* autocorrelación detallada, t desplazada, PDFs arcoseno/trapezoidal, Welch–Satterthwaite detallado, Cholesky, MCM extendido.

**Handout NOx (`handout/no_nox/`, 120 líneas en 10 archivos, `NOX_H03`=7 l, `NOX_H08`=3 l):** no es simétrico a O₃. Ya funciona como **capa R pura** — checklist y control documental, sin duplicar M6 (M6 lo cita 1 vez). Está mejor alineado, por accidente. Pero `README.md` y `handout/handout_teorico_gum_o3.md` / `handout/handout_no_nox.md` los presentan como equivalentes.

**Solucionarios (`modulos/soluciones/`, 1571 l):** privados, con reexplicación teórica para ser autónomos. Riesgo: tercera versión doctrinal. Meta debe ser canónico para respuesta breve y propósito; solucionario para desarrollo paso a paso y criterios de corrección.

**Protocolos E01–E16 (`practica/`):** necesitan autonomía operativa. Duplicación deliberada permitida: incluir fórmula/advertencia necesaria para ejecutar sin abandonar actividad, remitir al teórico para fundamento, conservar notación.

### 4.4 Handout como intento fallido de extraer capa 1

`handout/gum_o3/` no es capa 0/2 y solo parcialmente R. Es **reescritura** de capa 1, no extracción.

Solapamiento: M3 §3.3 ≈ `O3_H03_tipo_b_pdfs.md`; M2 §3.3 ≈ `O3_H04_propagacion_guf.md`; M7 bloque 6 ≈ `O3_H07_informe_gum.md`; M1 §3.1 ≈ `O3_H01 §1.5`.

Contenido genuinamente R (~350 de 869 l): `O3_H08_glosario.md` (23 términos sin definición en módulos), tabla PDFs/divisores, ley propagación general, checklist informe.

**Vacío de instrucción de uso:** búsqueda `prelectura|lectura previa|antes del curso|leer.*handout` en `modulos/`, `README.md`, `diseno_curso_v2.md`, `handout/` → **0 resultados**. Nada declara si handout es prelectura, durante o consulta posterior.

### 4.5 `solo_md/` — capa derivada fuera de control

Replica árbol completo (592 K) con enlaces desanclados para lectura fuera de repo. No lo genera `build_paquete_html.py` (`grep solo_md build_paquete_html.py` → 0), no está en git (`??` en `git status`), ya divergió: M1 14 l, M3 16, M2 12, M7 10, M8 10, M4 8, M5 6, M6 2 (quita `[texto](enlace)` dejando texto). Patrón idéntico al drift handout.

Precedente positivo: `build_paquete_html.py` + `pandoc_rewrite_links.lua` ya generan `curso_paquete_completo.html` con validación de archivos, filas, MathML, anclas, IDs, 20 secciones handout. Infraestructura de derivación existe — `solo_md/` simplemente no la usa.

---

## 5. Diagnóstico pedagógico vigente (no se resuelve solo separando capas)

### 5.1 Falta entrada terminológica clara

Glosario existe en `handout/gum_o3/O3_H08_glosario.md` pero como sección tardía, no puerta de entrada. Define avanzados, omite alta frecuencia práctica: SRP, repetibilidad, precisión intermedia, reproducibilidad, calibración/verificación/ajuste, doble conteo, escala completa, sesgo, patrón de transferencia, deriva cero/span.

**Solución:** combinar (a) mapa inicial corto indispensable, (b) definición completa justo antes de operar concepto, (c) glosario final de consulta. No dictar glosario extenso antes de M1.

### 5.2 Conceptos usados antes de enseñarse — inversión M1↔M3

| Momento | Términos usados | Definición formal |
|---|---|---|
| M1 (0–35 min) | inc. patrón/analizador/valor transferido, corrección, inc. residual, falla, doble conteo, covarianza | `O3_H01 §1.3–1.4` — remitido, no dictado |
| M2 (35–83) | mensurando, coef. sensibilidad | `O3_H01 §1.1`, `O3_H04 §4.1` |
| M3 (83–137) | **recién aquí** Tipo A/B, PDF, combinación cuadrática | el módulo mismo |

`modulos/M1_trazabilidad.md:6` declara establecer vocabulario, pero `M1:111` delega tres incertidumbres al handout. Cadena `u_i → u_c → U=k·u_c` no tiene dueño docente claro; `U` y `k` aparecen en ejercicios pero su introducción formal vive en handout.

Requiere dueño explícito por módulo (ver §7). Cada concepto operativo debe introducirse antes de exigir uso.

**Dos salidas** (no excluyentes):

1. **Handout O₃ (R) como prelectura obligatoria** (`O3_H00`+`O3_H01`+glosario mínimo). M1 asume vocabulario. Riesgo: depende de lectura previa, alto en operadores.
2. **Bloque M0 de vocabulario 15–20 min** antes de M1: mensurando, error/corrección/incertidumbre, estándar/combinada/expandida, trazabilidad, Tipo A/B mínimo. M3 profundiza. Costo: 20 min de 78 min reserva logística. Recomendada si no hay envío previo.

### 5.3 Informe GUM se exige antes de enseñarse suficiente

M7 exige resultado auditable GUM §7; lista completa vive en `handout/gum_o3/O3_H07_informe_gum.md`. Cobertura, redondeo y coherencia presupuesto↔resultado se evalúan pero aparecen solo como apoyo en revisión final. Deben migrar a capa 1 antes del taller.

### 5.4 Polisemia de "cobertura"

Curso usa cobertura para: factor/probabilidad/intervalo GUM; alcance de evidencia; "matriz de cobertura" (artefacto). **Regla:** reservar **cobertura** para sentido GUM; usar **alcance de la evidencia** para qué condiciones/fuentes cubre un dato (ver Regla 5).

### 5.5 Duplicación no gobernada

Autocorrelación, covarianza, propagación aparecen en módulos/handouts/solucionarios/protocolos con distinto detalle. Repetición no siempre mala; es problemática cuando no se sabe cuál es canónica, resumen, ampliación o cuál actualizar primero.

---

## 6. Hallazgo estructural: la capa 1 no es extraíble en 4 de 8 módulos

Sin estructura regular, derivación de capas 1–3 no automatizable.

| Módulo | Subbloques `### 3.x` | `Idea fuerza` | Bloque discurso |
|---|---:|---:|---|
| M1 | 5 | 5 | `Guion dictable` ×5 |
| M2 | 4 | 5 | `Guion dictable` ×4 |
| M3 | 4 | 5 | `Guion dictable` ×4 |
| M4 | 5 | 5 | `Guion dictable` ×5 |
| M5 | **0** | **1** | **ninguno** — §3 prosa plana |
| M6 | 4 | **1** | **ninguno** |
| M7 | 0 (`### Bloque N`) | 4 | `Párrafo dictable` ×4 |
| M8 | 0 | 1 | **ninguno** |

Tres nombres para mismo objeto, dos esquemas de encabezado. **M5, M6, M8 no tienen discurso redactado** — tienen contenido, no narración. Para ellos capa 1 no se extrae: se escribe.

27 `Idea fuerza` para ~120 subbloques-equivalentes → capa 2 arranca con ~20% de semillas.

---

## 7. Arquitectura documental objetivo

### A. Meta maestro privado
*Base:* M1–M8. *Contenido:* teoría completa, discurso, decisiones pedagógicas, notas instructor, tiempos, preguntas, respuestas breves, errores, variantes, referencias, criterios evaluación. *Destinatario:* autor/instructor. Fuente superior de intención pedagógica. Si necesita lectura continua, ensamblado generado, nunca copia manual.

### B. Material teórico entregable (capa 1)
*Derivado de A quitando bloques.* Mantiene: explicación completa, hilo narrativo, definiciones, ecuaciones, ejemplos, figuras/tablas, síntesis, ejercicios sin solución, referencias pertinentes. Elimina: minutaje, instrucciones dictar/preguntar/mostrar, estrategia facilitación, respuestas, resultados anticipados, comentarios editoriales. *Destinatario:* participante. Debe leerse como manual breve continuo, capítulos M1–M8 en una sola narrativa.

### C. Anexos técnicos
*Base:* handout O₃ avanzado (~350 l). Derivaciones, casos especiales (arcoseno, trapezoidal, t desplazada, Welch–Satterthwaite, Cholesky, MCM extendido), referencias normativas extensas. *Destinatario:* participante que profundiza + instructor. No lectura obligatoria para recorrido principal.

### D. Fichas operativas y ayudas de campo
*Base:* handout NOx + parte operativa O₃. Checklists, fórmulas rápidas, criterios aceptación, controles documentales, advertencias montaje/seguridad. *Destinatario:* participante en práctica/operación/auditoría. Consulta rápida — no conduce actividad completa.

### E. Protocolos prácticos
*Base:* E01–E16 (`practica/`). Propósito/alcance, materiales, secuencia ejecución, datos a registrar, criterios aceptación/cierre, punteros a fundamento teórico. *Destinatario:* participante + instructor en laboratorio/campo. Conduce ejecución completa (a diferencia de ficha).

### F. Solucionarios privados
Resolución completa, cálculos paso a paso, criterios corrección, variantes aceptables, errores típicos. *Destinatario:* instructor. Meta conserva propósito y resultado esperado; solucionario conserva desarrollo.

### G. Guion textual de diapositivas (capa 2)
Derivado de B. Títulos, frases cortas, 1 idea/diapa, mensajes centrales, indicaciones apoyo visual. Telegráfico.

### H. Diapositivas visuales (capa 3)
Derivadas de G. Diseño final, imágenes, diagramas, tablas simplificadas, jerarquía, revelado progresivo. No introduce teoría nueva — si lo hace, ruptura de derivación.

---

## 8. Dueños conceptuales por módulo

Para que cada concepto tenga introducción antes de uso:

| Módulo | Dueño | Conceptos canónicos |
|---|---|---|
| **M1** | trazabilidad y vocabulario base | trazabilidad, mensurando, error/corrección/incertidumbre, SRP, patrón transferencia, cadena cal. |
| **M2** | modelo de medición | modelo físico (Beer–Lambert), coeficientes sensibilidad, identificación fuentes, doble conteo (introducción) |
| **M3** | incertidumbre estándar | Tipo A/B, PDFs/divisores, `u_i`, combinación `u_c`, covarianza (definición), autocorrelación/neff |
| **M4** | presupuesto y expansión | presupuesto, contribuciones, doble conteo (regla), `U=k·u_c`, cobertura GUM, redondeo, coherencia |
| **M5** | patrones y calibración | regresión multipunto, residuos, deriva cero/span, verificación, alcance evidencia, escala completa |
| **M6** | NOx y quimioluminiscencia | modelo NOx diferencial, eficiencia convertidor, interferencias, covarianza medida (NO/NOx), sesgo |
| **M7** | integración y reporte | integración presupuesto, validación, declaración resultado, informe GUM §7, transferencia a NOx |
| **M8** | validación opcional | MCM, Cholesky, validación marco GUM |

Otros módulos pueden recordar, no redefinir en paralelo.

---

## 9. Reglas de derivación y control

**R1. Una idea nueva nace en capa meta.** Ninguna diapositiva, protocolo o solucionario introduce concepto no reconocido en meta.

**R2. Autoridad definida.** Meta es canónico para contenido técnico, definiciones, ecuaciones, notación e intención. Capa 1 es canónico para orden y redacción entregable. Corrección técnica → primero meta, luego propagar.

**R3. Diapositivas reducen, no amplían.** Capa 2/3 condensa, ilustra, jerarquiza. No agrega teoría ausente de capa 1.

**R4. Anexos amplían sin interrumpir.** Relato principal comprensible sin anexos. Anexos permiten profundidad, no reparan huecos básicos.

**R5. Terminología reservada.** `cobertura` solo para GUM (factor/probabilidad/intervalo). `alcance de la evidencia` para cobertura de condiciones/fuentes. Unificar glosario (`O3_H08` + términos faltantes) y mapa inicial.

**R6. Respuestas fuera del entregable.** Meta: respuesta breve + propósito + resultado esperado. Solucionario: desarrollo completo + criterios. Nada anticipado en capa 1 (M2, M4, M8 hoy lo anticipan).

**R7. Repetición gobernada.** Ficha repite solo para consulta rápida; protocolo para autonomía de ejecución. Ambos conservan notación/terminología de capa 1 y remiten a ella para fundamento.

---

## 10. Mecanismo técnico: fuente única, marcado por audiencia

Superar archivos paralelos (handout y `solo_md` ya demostraron el drift). Una fuente por módulo (= capa 0), demás capas generadas quitando bloques.

Convención regular — esquema único por subbloque (extiende lo ya escrito sin querer):

```markdown
### 3.N Título — 0:mm a 0:mm; acumulado 0:mm      ← capa 0 (minutaje)

**Idea fuerza:**            ← capa 2 (título diapositiva)
**Guion dictable:**         ← capas 0 y 1 (discurso / material teórico)
**Puntos:**                 ← capa 2 (3–5 viñetas comprimidas)
**Apoyo visual:**           ← capa 3 (diagrama/foto/esquema)
**Nota de facilitación:**   ← capa 0 (dónde se atasca, cómo destrabar)
**Referencias exactas:**    ← capa 0 completa; capa 1 versión corta
**Apoyo en la referencia:** ← capa 0 (puntero a R)
```

`build_capas.py` (siguiendo patrón `build_paquete_html.py`) emite:

| Salida | Regla |
|---|---|
| capa 0 | archivo tal cual |
| capa 1 | `Guion dictable` + referencias cortas; sin minutaje, notas facilitación, errores, punteros internos |
| capa 2 | `Idea fuerza` + `Puntos` |
| capa 3 | capa 2 + `Apoyo visual` como marcador imagen |
| `solo_md/` | cualquiera anterior, con enlaces desanclados |

Ventajas: es lo ya escrito, anti-drift, un archivo por módulo.

Estimación volumen capas 2–3: 462 min obligatorios a 2–3 min/diapa ⇒ **150–200 diapositivas**.

---

## 11. Inventario de deuda y valoración del desfase

### 11.1 Deuda (ordenada por impacto)

| # | Deuda | Impacto | Esfuerzo | Origen |
|---|---|---|---|---|
| D1 | M5, M6, M8 sin `Guion dictable` — capa 1 inexistente | **bloqueante** capas 1–3 | alto: redactar discurso | opu §7, sol §5 |
| D2 | Tres convenciones discurso (`Guion`/`Párrafo`/ninguno) + dos esquemas encabezado | bloquea derivación mecánica | bajo: renombrar | opu §7 |
| D3 | `handout/gum_o3/` duplica ~520 l de capa 1 (869→~350 R real) | confusión roles, drift | medio: podar | opu §5, sol §4.2 |
| D4 | Rol handout nunca declarado (prelectura/aula/consulta) | impide decidir orden términos | bajo: decisión + párrafo README | opu §5 |
| D5 | Inversión vocabulario M1↔M3 + cadena `u→u_c→U` sin dueño | pedagógico, afecta a todos | medio: bloque M0 15–20 min | opu §6, sol §5.2 |
| D6 | `solo_md/` manual, fuera git, ya divergido (2–16 l/módulo) | drift silencioso | bajo: generar o borrar | opu §8 |
| D7 | 27 `Idea fuerza` / ~120 subbloques → capa 2 al 20% | capa 2 incompleta | alto mecánico tras D2 | opu §10, sol §8.5 |
| D8 | README presenta O₃/NOx como equivalentes (869 vs 120 l) | expectativa falsa | bajo: tabla en README | opu §5, sol §4.3 |

### 11.2 Valoración cualitativa del desfase

En esta sección desfase = esfuerzo editorial para arquitectura objetivo, no calidad técnica.

| Dimensión | Desfase | Comentario |
|---|---|---|
| Contenido técnico | **bajo** | Conocimiento ya existe en módulos/handouts/prácticas/solucionarios, trazado a JCGM/QUAM/EN14211/EPA/NISTIR/BIPM con página exacta |
| Versión meta | **bajo a medio** | Base sólida M1–M8; falta declarar rol, cerrar saltos (D5) y unificar (D2) |
| Material teórico entregable | **medio a alto** | Existe parcial pero repartido; falta narrativa limpia continua |
| Anexos/ayudas | **medio** | Material valioso pero funciones mezcladas bajo "handout" |
| Pipeline diapositivas | **alto como pipeline formal** | No iniciado; construir tras estabilizar capa 1 |
| **Global** | **1.5 capas** | No reconstrucción desde cero. Reorganización editorial + cadena derivación explícita |

Cualitativo: conocimiento avanzado, meta avanzada, narrativa entregable incompleta, clasificación anexos ambigua, pipeline diapositivas no consolidado.

---

## 12. Plan propuesto — orden por dependencia

1. **Declarar cinco capas y convención de bloques** en `README.md` y `diseno_curso_v2.md`. Renombrar mentalmente `handout/`→`referencia/` o declarar rol R. Fijar esquema §10. Resuelve D4 y D8 sin tocar contenido.
2. **Piloto en M5** — peor caso actual (0 subbloques, 1 Idea fuerza, sin discurso). Si aguanta ahí, aguanta en todos. Ataca D1+D2 de forma acotada.
3. **`build_capas.py`** siguiendo `build_paquete_html.py`. `solo_md/` pasa a salida generada (con `pandoc_rewrite_links.lua` ya disponible). Resuelve D6 y valida mecanismo.
4. **Propagar esquema a M1–M4 y M7** (tienen discurso, solo etiquetar), luego a **M6 y M8** (redactar). Cierra D1, D2 y habilita D7.
5. **Podar handout O₃ a R real** (~350 l: glosario 23 términos + términos faltantes, tabla PDFs/divisores, ley propagación, checklist informe GUM §7). 30 anclas existentes siguen válidas. Cierra D3. Handout NOx queda como modelo de ficha.
6. **Decidir orden de términos** — bloque M0 15–20 min (recomendado si no hay prelectura) o prelectura obligatoria R. Migrar cobertura/redondeo/informe a capa 1 antes de M7. Cierra D5.
7. **Capas 2 y 3 al final**, cuando derivación es mecánica. Completar `Idea fuerza`+`Puntos` faltantes y `Apoyo visual`. Cierra D7. Estimación 150–200 diapositivas.

---

## 13. Lo que no está mal — base para construir

- Contenido técnico sólido, trazado a fuente con página exacta (JCGM, QUAM, EN 14211, EPA, NISTIR, BIPM.QM-K1). Nota APOA-370 vs APNA-370 evita atribuir especificaciones equivocadas.
- Datasets reproducibles con semilla `20260819`.
- Separación curso teórico / práctica laboratorio con entregables evaluados independientes (M7 y E15) bien argumentada.
- `build_paquete_html.py` valida archivos, filas/columnas NOx, MathML, anclas, IDs, 20 secciones handout y ausencia recursos externos — base para `build_capas.py`.
- `handout/no_nox/` ya es capa R correcta — modelo para podar O₃.
- Control documental y rúbrica (mensurando completo, vínculo fuente-efecto, evidencia pertinente, sin doble conteo, covarianza/dependencias, coherencia presupuesto-reporte) bien definidos.

---

## 14. Conclusión final

Inquietud inicial válida — módulos y handouts parecían repetirse y completar huecos mutuamente. Causa no era exceso de contenido ni mala concepción, sino **arquitectura sin declarar**.

Con capa meta reconocida:

1. M1–M8 no están sobrecargados: son base avanzada del meta y deben gobernarse como tal.
2. Material teórico entregable no existe como producto único limpio y continuo — es la deuda central.
3. Handout O₃ mezcla básico (migrar a capa 1) con avanzado (quedar como anexo/R); NOx ya es ficha operativa y no necesita simetría artificial.
4. Vocabulario, cadena `u→u_c→U`, cobertura, redondeo e informe GUM requieren dueño y ubicación antes de exigir uso — M0 o prelectura + dueños por módulo.
5. Guion y diapositivas deben derivarse de capa 1 estabilizada, no de fuentes paralelas, mediante fuente única + marcado + `build_capas.py`.
6. `solo_md/` y duplicación handout demuestran el costo de mantener copias manuales — generar, no duplicar.
7. Trabajo pendiente es **editorial y arquitectónico** (1.5 capas), no reconstrucción técnica.

Curso avanzado en conocimiento y preparación docente. Siguiente etapa: convertir riqueza meta en secuencia controlada de productos, cada uno con destinatario, propósito y profundidad definidos.
