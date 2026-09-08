# Balance final — evaluación de las propuestas de `diag_update/`

**Fecha:** 2026-08-28
**Alcance:** 11 archivos `.md` de `docs/capacitacion_incert/cursov2/diag_update/`
**Método:** 3 revisores independientes (Sonnet 5) en paralelo, con rúbrica común de 7 criterios; verificación propia de cifras contra el repositorio; consolidación y recalibración entre grupos.
**Marco de referencia:** `diag_opu.md` (evidencia medida sobre el árbol, esquema de marcado, `build_capas.py`, deuda D1–D8, plan por dependencia) y `diag_sol.md` (función meta, taxonomía A–H de productos, preguntas rectoras, diagnóstico pedagógico). No se evaluaron como propuestas: son el marco.

---

## 1. Hallazgo transversal

**Ninguna de las 11 propuestas es un diagnóstico independiente.** Las 11 son síntesis de `diag_opu.md` + `diag_sol.md`. Ninguna cuestiona el modelo de capas 0→1→2→3 + R, ninguna propone una arquitectura alternativa, ninguna aporta evidencia nueva medida sobre el árbol salvo una.

Lo que las separa no es la elegancia narrativa. Son dos ejes:

1. **¿Resolvieron las tensiones entre las dos fuentes, o solo las yuxtapusieron?**
2. **¿Reverificaron los datos, o heredaron cifras sin medir?**

Medición de derivación léxica (trigramas compartidos con el marco de referencia):

| Archivo | tokens | % en `diag_opu` | % en `diag_sol` | % en la unión |
|---|---:|---:|---:|---:|
| dd_mmxm3.md | 5107 | 36.9 | 54.9 | **91.2** |
| dd_dsv4p.md | 3850 | 52.6 | 34.8 | **86.7** |
| dd_qw38.md | 4179 | 47.0 | 35.3 | 81.6 |
| dd_glm53f.md | 3581 | 52.2 | 18.3 | 69.7 |
| dd_op5.md | 4326 | 38.7 | 28.4 | 66.5 |
| dd_g46oc.md | 3844 | 41.2 | 21.7 | 62.2 |
| dd_k3.md | 2549 | 43.4 | 15.2 | 57.7 |
| dd_grk46.md | 4779 | 29.0 | 23.4 | **51.8** |
| dd_muse12.md | 3336 | 22.5 | 11.2 | 33.2 |
| dd_gem.md | 323 | 17.1 | 2.8 | 19.3 |
| dd_ter.md | 2327 | 3.7 | 13.1 | 16.3 |

Lectura correcta de esta tabla: **alto = derivativo confirmado**. Bajo no prueba originalidad — `dd_gem` y `dd_ter` bajan porque comprimen y parafrasean, no porque aporten. Pero `dd_mmxm3` con 5107 tokens y 91.2 % de solapamiento es prácticamente relleno.

---

## 2. Verificación independiente de cifras

Medido hoy sobre el repositorio:

```
modulos/*.md              1489 líneas    (diag_opu.md dice 607)   ← desfasado
modulos/soluciones/*.md   1571 líneas    (coincide)
handout/gum_o3/*.md        749 líneas    (diag_opu.md dice 869)   ← desfasado
handout/no_nox/*.md        120 líneas    (coincide)
"acumulado" en modulos/     45           (coincide)
"Idea fuerza" en modulos/   27 líneas    (26 ocurrencias por otro conteo)
"Guion dictable"            18
```

**Solo `dd_op5.md` reverificó.** Declara en su encabezado *"Las cifras se reverificaron sobre el estado actual del repositorio; donde difieren de los diagnósticos previos, manda este documento"* y sus números (1489, 749, ~400 líneas duplicadas en el handout, 26 `Idea fuerza`) coinciden con la medición real. Las otras 10 heredan 607/869/520 sin cuestionar.

Consecuencia práctica: cualquier propuesta que se adopte necesita re-medir antes de actuar sobre D3 y D7.

---

## 3. Tabla comparativa final

Puntaje del revisor asignado, ajuste propio (por defectos duros verificados y por valor real de la aportación) y puesto final.

| # | Archivo | Revisor | Ajuste | **Final /70** | Veredicto |
|---|---|---:|---:|---:|---|
| 1 | `dd_grk46.md` | 61 | −2 | **59** | ADOPTAR COMO BASE |
| 2 | `dd_op5.md` | 59 | −2 | **57** | CANIBALIZAR — cifras y disciplina de verificación |
| 3 | `dd_glm53f.md` | 55 | −1 | **54** | CANIBALIZAR — reordenamiento de plan, D11 |
| 4 | `dd_qw38.md` | 55 | −3 | **52** | CANIBALIZAR — agrupación §8 |
| 5 | `dd_g46oc.md` | 52 | −2 | **50** | CANIBALIZAR — Regla 8 |
| 6 | `dd_muse12.md` | 54 | −6 | **48** | DESCARTAR |
| 7 | `dd_dsv4p.md` | 50 | −3 | **47** | DESCARTAR |
| 8 | `dd_k3.md` | 45 | −1 | **44** | DESCARTAR — sirve como plantilla de versión corta |
| 9 | `dd_ter.md` | 47 | −5 | **42** | DESCARTAR — canibalizar solo el formato de plan |
| 10 | `dd_gem.md` | 39 | −3 | **36** | DESCARTAR |
| 11 | `dd_mmxm3.md` | 41 | −6 | **35** | DESCARTAR |

Ajustes aplicados: penalización por cifras desfasadas no detectadas, por redundancia interna, por errores de diseño verificados, y por solapamiento léxico alto sin aportación proporcional.

---

## 4. Ranking comentado

**1.º `dd_grk46.md` (451 líneas) — 59.**
Único que trata `diag_opu` y `diag_sol` como insumos con **cegueras complementarias** (§0) y toma decisiones explícitas donde chocan (§2, ocho decisiones numeradas). Tres aportes reales:

- **Paso de continuidad** (§13.7): tras el recorte mecánico de capa 0, un pase corto de transiciones. Corrige el punto más frágil de todo el diseño — que un recorte automático produce fragmentos, no un manual continuo.
- **Secuencia corregida**: cierra los huecos pedagógicos *dentro del meta* (paso 5) **antes** de extraer capa 1 y antes de podar el handout (paso 6). Es la dependencia correcta; `diag_opu` y `dd_op5` la tienen invertida.
- **D9–D12** al inventario de deuda, incluido D12 (solucionarios reexplican teoría → riesgo de tercera doctrina), que ningún otro numera.

*Defectos:* su encabezado y la tabla de §0 **invierten las atribuciones** — asigna a `diag_sol.md` la evidencia cuantificada y a `diag_opu.md` la función meta; es al revés (verificado). El contenido de la tabla es correcto, solo las etiquetas de columna están cambiadas. Además hereda las cifras desfasadas (869, ~520 líneas). Su §10 (esquema de marcado) es copia literal de `diag_opu`.

**2.º `dd_op5.md` (433 líneas) — 57.**
El único con higiene de datos: reverifica contra el repo y declara que corrige al documento anterior. Añade D9–D11 y la "Regla 8 — toda copia es salida generada", que cierra el hueco de autoridad sobre `solo_md/`. Su §15 "Valoración del desfase" con criterio explícito de bajo/medio/alto es el mejor cierre ejecutivo de las once.
*Defectos:* el plan (§14) es el de `diag_opu` casi verbatim — sin paso de continuidad y con la secuencia handout/pedagogía sin corregir. Redundancia interna (asimetría O₃/NOx en §4.3 y §6.2). No marca línea por línea qué cifra cambió.

**3.º `dd_glm53f.md` (342 líneas) — 54.**
Media corrección de secuencia: mueve "derivar capa 1" antes de "podar handout O₃", con justificación de dependencia. Tabla de capas con columna "qué mantiene / qué quita". D11 con lista concreta de términos ausentes del glosario (SRP, repetibilidad, precisión intermedia, sesgo, deriva de cero/span).
*Defectos:* su diagrama final contradice su propio texto sobre si capa R es perpendicular o rama. 69.7 % derivativo.

**4.º `dd_qw38.md` — 52.** Mismas D9–D11 que op5 (convergencia independiente: señal de que esos huecos son reales). Agrupa los hallazgos pedagógicos residuales en un §8 propio — buena decisión de legibilidad. Cifras desfasadas, redundancia interna, 81.6 % derivativo.

**5.º `dd_g46oc.md` — 50.** Aporta la formulación citable "los derivados se generan, no se copian" y fusiona podar-handout con subir-lo-básico-a-capa-1 en un solo paso. Nomenclatura inconsistente entre "capa R", "anexo" y "ficha".

**6.º `dd_muse12.md` — 48.** Copia fiel y completa; cero aportación propia. Sirve como checksum de que ninguna síntesis perdió contenido, nada más.

**7.º `dd_dsv4p.md` — 47.** 86.7 % derivativo. Aporta D9/D10 y nada más. Mantiene la secuencia invertida podar-antes-de-decidir pese a que su propio D9 depende de la decisión.

**8.º `dd_k3.md` — 44.** 306 líneas, la compresión más honesta: conserva los hallazgos duros sin inflar. No resuelve ninguna tensión, no añade nada. Utilizable como borrador de la versión corta del README.

**9.º `dd_ter.md` — 42.** Error de diseño verificado: propone marcadores nuevos (`**Guion para participante:**`, `**Puntos para diapositiva:**`) distintos de los que ya existen de facto (`Guion dictable`, `Idea fuerza`). El diagnóstico D2 es que hay **tres** convenciones en pugna; ter introduce una cuarta. Descalifica su esquema. Rescatable: su plan en tabla con columna "resultado esperado" — el formato más verificable de las once.

**10.º `dd_gem.md` (34 líneas) — 36.** Correcto hasta donde llega, pero descarta toda la evidencia cuantitativa y **todos** los hallazgos pedagógicos (vocabulario invertido, cadena `u → u_c → U` sin dueño, polisemia de "cobertura", informe GUM exigido antes de enseñarse). El punto central de ambos diagnósticos base es que separar capas **no basta**; gem no lo reproduce. Vale como resumen ejecutivo de una página, nunca como base.

**11.º `dd_mmxm3.md` (764 líneas) — 35.** Peor relación coste/beneficio: el más largo, 91.2 % derivativo, repite el handout O₃ dos veces en secciones distintas sin añadir nada en la segunda pasada, y deja sin resolver la tensión de modelos (capa R perpendicular en §4 vs. árbol de ocho productos en §9) que `grk46` sí decide. El `build_dd_mmxm3.py` que lo acompaña **no es el pipeline del curso**: es un renderizador Markdown→HTML del propio diagnóstico, calcado de `build_paquete_html.py`. No toca `modulos/`, no implementa `build_capas.py`, no prueba el esquema de marcado. Sugiere una verificación ejecutable que no ocurrió.

---

## 5. Recomendación: base + parches

No adoptar ninguna tal cual. Receta de fusión, en este orden:

1. **Base: `dd_grk46.md`.** Por §0 (fuentes con ceguera complementaria), §2 (decisiones tomadas, no aplazadas), §13 (plan de 8 pasos con secuencia correcta) y D9–D12.
2. **Corregir en la base:** invertir las etiquetas de las columnas de §0 y del encabezado — `diag_opu.md` es la evidencia medida, `diag_sol.md` es el marco conceptual.
3. **Sustituir todas las cifras** por las de `dd_op5.md`, reverificadas y confirmadas: `modulos/` 1489, `handout/gum_o3/` 749, duplicación del handout ~400 líneas (no 520), `Idea fuerza` 26–27. Añadir la línea de disciplina de op5: *"donde difieren de diagnósticos previos, manda este documento"*.
4. **Añadir de `dd_op5.md`:** §15 "Valoración del desfase" con criterio explícito bajo/medio/alto y el cierre "el desfase es de capa y media, no de arquitectura equivocada".
5. **Añadir de `dd_g46oc.md`:** la Regla 8 — *los derivados se generan, no se copian* — como principio permanente del README. Es la formulación más citable de por qué `solo_md/` y el handout duplicado son el mismo antipatrón.
6. **Reformatear el plan** con el formato de `dd_ter.md`: tabla con columna "resultado esperado" por fila, en vez de "cierra D3". Criterio de "hecho" explícito, no inferido.
7. **Añadir de `dd_glm53f.md`:** la lista concreta de términos ausentes del glosario en D10.

Resultado esperado: un documento de ~350–400 líneas, con datos verificados, secuencia correcta y criterio de "hecho" por paso.

---

## 6. Lo que ninguna propuesta resolvió

Decisiones que siguen siendo del autor, no delegables a ningún diagnóstico:

- **M0 vs. prelectura.** Las once recomiendan M0 (15–20 min de la reserva logística de 78 min), pero ninguna mide qué se cae de la agenda si esa reserva se consume.
- **Redactar M5, M6 y M8.** D1 es bloqueante y de esfuerzo alto. Ninguna propuesta lo dimensiona ni propone cómo abordarlo; todas lo listan y siguen. Es el cuello de botella real de todo el plan.
- **Riesgo de sobre-ingeniería de `build_capas.py`.** Las once lo dan por bueno porque `diag_opu` lo propuso. Ninguna evalúa la alternativa más barata: etiquetar bien y extraer con un `awk` de 20 líneas, o incluso a mano una vez, si las capas 2 y 3 se producen una sola vez por edición del curso.
- **Si el desfase de cifras (607→1489, 869→749) indica que el árbol cambió** entre el diagnóstico y hoy, o que la medición original fue incorrecta. Importa: si el árbol se mueve rápido, cualquier plan basado en conteos caduca.

---

## 7. Nota de método

Los tres revisores puntuaron en escalas no calibradas entre sí (tope de grupo: 55 / 61 / 59). La columna "Final" recalibra con verificación propia y solo debe leerse como ordenamiento, no como medida absoluta. Un revisor invirtió las atribuciones de `diag_opu`/`diag_sol` en su preámbulo — repitiendo el mismo error que contiene `dd_grk46.md`; sus evaluaciones de las propuestas se mantienen, las etiquetas de fuente no.
