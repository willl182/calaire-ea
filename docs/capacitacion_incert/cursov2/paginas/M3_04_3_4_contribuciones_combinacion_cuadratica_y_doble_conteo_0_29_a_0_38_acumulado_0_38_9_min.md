# M3 — Página 04 — 3.4 Contribuciones, combinación cuadrática y doble conteo — 0:29 a 0:38; acumulado 0:38 (9 min)

- **Sesión:** M3
- **Fuente:** [`modulos/M3_conceptos_gum.md`](../modulos/M3_conceptos_gum.md)
- **Tipo:** página/diapositiva del libreto

## Libreto

### 3.4 Contribuciones, combinación cuadrática y doble conteo — 0:29 a 0:38; acumulado 0:38 (9 min)

**Idea fuerza:** primero se expresan todas las contribuciones en la unidad del resultado; después se combinan una sola vez.

**Guion dictable:**

«Una incertidumbre de entrada no entra al presupuesto solo por estar expresada como desviación estándar. Debemos saber cuánto cambia el resultado cuando cambia esa entrada. Para un modelo \(Y=f(X_1,\ldots,X_N)\), el coeficiente de sensibilidad es:»

\[
c_i=\frac{\partial f}{\partial X_i},
\qquad
u_i(y)=|c_i|u(x_i).
\]

«En muchos presupuestos operativos de O₃, las entradas ya se convierten a ppb o nmol mol⁻¹ equivalentes y entonces \(c_i=1\). En M7, en cambio, la sensibilidad de la pendiente de una recta es el nivel \(x\); por eso su contribución aumenta para el nivel alto.»

Si las contribuciones pueden tratarse como independientes:

\[
u_c(y)=\sqrt{\sum_i [c_i u(x_i)]^2}.
\]

Ejemplo breve para la pizarra: si dos contribuciones independientes son 0.6 y 0.8 nmol mol⁻¹,

\[
u_c=\sqrt{0.6^2+0.8^2}=1.0\ \mathrm{nmol\ mol^{-1}},
\]

no 1.4 nmol mol⁻¹.

«La combinación cuadrática no corrige un modelo incompleto. Una cifra global debe declarar su **cobertura**. Por ejemplo, la precisión intermedia obtenida durante meses puede cubrir ruido, recalibración, operador, parte del ambiente y variación del equipo. Esas ramas no se añaden otra vez sin demostrar qué fracción queda fuera. La incertidumbre del patrón o las pérdidas de línea pueden permanecer externas y sumarse si no están cubiertas.»

«La combinación cuadrática no corrige un modelo incompleto. Antes de calcular, revise el **doble conteo**: cada fila debe representar un efecto identificable y aparecer una sola vez. Si un certificado ya incluye repetibilidad o condiciones ambientales, no se agregan otra vez sin una desagregación coherente. Si la repetibilidad observada ya contiene la resolución, una fila adicional de resolución puede duplicar parte de la variación.»

Use esta lista por fila:

1. ¿Qué mecanismo representa?
2. ¿Qué evidencia lo cuantifica?
3. ¿Qué periodo y condiciones cubre?
4. ¿Cómo se convierte a incertidumbre estándar y a la unidad de salida?
5. ¿Qué ramas ya están cubiertas por esa cifra?
6. ¿Qué dependencia existe con otras entradas?

«La fórmula anterior supone independencia. Las entradas que comparten patrón, calibración o datos pueden requerir covarianza. Como el cálculo explícito de covarianza aparece recién en M7, aquí queda como alerta: no imponer independencia si se conoce una fuente compartida. El desarrollo y los términos cruzados se consultan en el handout avanzado (Handout teórico, §4.2 — Ley de propagación de incertidumbre) y se trabajan en M7.»

**Referencia integrada:** JCGM 100:2008, §§5.1–5.2 y advertencia de doble conteo en §4.3.10. Eurachem/CITAC QUAM 2012, caps. 7–8, pp. editoriales 16–29 (PDF pp. 22–35), y ejemplo A4, pp. editoriales 60–71 (PDF pp. 66–77), para agrupación de precisión, sesgo y fuentes externas. Handout teórico, §4.1 — Coeficientes de sensibilidad, §4.2 — Ley de propagación de incertidumbre y §4.3 — Doble conteo: GUM §4.3.10.
