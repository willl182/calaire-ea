# M3 — Página 03 — 3.3 Tipo B y PDFs que reaparecen en el curso — 0:18 a 0:29; acumulado 0:29 (11 min)

- **Sesión:** M3
- **Fuente:** [`modulos/M3_conceptos_gum.md`](../modulos/M3_conceptos_gum.md)
- **Tipo:** página/diapositiva del libreto

## Libreto

### 3.3 Tipo B y PDFs que reaparecen en el curso — 0:18 a 0:29; acumulado 0:29 (11 min)

**Idea fuerza:** el divisor depende del significado de la información, no del nombre del componente.

**Guion dictable:**

«En Tipo B preguntamos qué afirma realmente la fuente. Para cada PDF deben quedar dos campos explícitos: **qué información factual se conoce** y **por qué la forma seleccionada la representa**. No se elige triangular porque produzca menor incertidumbre. QUAM App. E.1 y App. G reúnen conversiones y fuentes comunes como certificados, resolución, T/P y repetibilidad (App. E.1, pp. editoriales 104–105, PDF pp. 110–111; App. G, pp. editoriales 126–131, PDF pp. 132–137). ¿Entrega una desviación estándar, una incertidumbre expandida o solamente límites? La respuesta determina el tratamiento.»

#### Normal: desviación estándar, RMS o incertidumbre expandida documentada

- Si una fuente entrega una desviación estándar compatible con el mensurando, esa cifra ya es una incertidumbre estándar.
- Un ruido RMS puede conservarse como incertidumbre estándar cuando su definición, tiempo de promedio y condiciones son compatibles; no recibe por costumbre un divisor adicional.
- Si un certificado declara incertidumbre expandida \(U\) y factor de cobertura \(k\):

\[
u=\frac{U}{k}.
\]

«No se supone \(k=2\) si el certificado declara otro factor o no informa cómo se obtuvo. La palabra “normal” tampoco convierte por sí sola una fuente en Tipo A: la clasificación depende del método de evaluación.»

#### Rectangular: solo se conocen límites y no se favorecen valores internos

Si el efecto puede estar entre \(-a\) y \(+a\), y la información disponible no favorece ninguna zona del intervalo:

\[
u=\frac{a}{\sqrt3}.
\]

Ejemplos del contexto O₃: deriva declarada como límite, linealidad \(\pm1\%\) de escala completa o error de redondeo dentro de medio incremento digital, siempre que esa interpretación corresponda a la fuente.

«Antes de dividir, convierta el límite a la unidad del resultado. En una escala completa de 200 ppb, \(\pm1\%\) FS significa \(a=2\) ppb. En un punto seleccionado de 120 ppb, \(\pm1\%\) del setpoint significa \(a=1.2\) ppb. No son la misma especificación.»

#### Triangular: los valores cercanos al centro son más plausibles

Si existen límites \(-a\) y \(+a\), pero además hay fundamento para considerar más probables los valores cercanos al centro:

\[
u=\frac{a}{\sqrt6}.
\]

«La triangular no se elige para obtener un valor menor que con la rectangular. Se usa solo cuando la evidencia o el mecanismo justifican ese mayor peso central. Reaparece en M7, donde el presupuesto publicado del fotómetro asigna una PDF triangular a la repetibilidad del cociente de intensidades; allí se respeta la distribución publicada.»

Resumen para la pizarra:

| Información disponible | Tratamiento habitual, si está justificado |
|---|---|
| Desviación estándar o RMS compatible | \(u=s\) o \(u=\mathrm{RMS}\) |
| Incertidumbre expandida con \(k\) | \(u=U/k\) |
| Límites \(\pm a\), valores igualmente plausibles | rectangular: \(u=a/\sqrt3\) |
| Límites \(\pm a\), centro más plausible | triangular: \(u=a/\sqrt6\) |

«Las PDFs arcoseno y trapezoidal no se necesitan para resolver M4, M5 ni el ejercicio principal de M7. Se mencionan para reconocer que existen; sus mecanismos, fórmulas y ejemplos quedan en el handout avanzado (Handout teórico, §3.6 — Distribución arcoseno o en U, y §3.7 — Trapecio curvilíneo para límites inexactos).»

**Referencia integrada:** JCGM 100:2008, §§4.3.1–4.3.9. Handout teórico, §3.1 — De información disponible a distribución, §3.2 — Distribución rectangular, §3.3 — Distribución normal y §3.4 — Distribución triangular; ejemplo desarrollado en §3.8.
