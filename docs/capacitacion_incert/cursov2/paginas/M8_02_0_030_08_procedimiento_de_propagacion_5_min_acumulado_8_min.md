# M8 — Página 02 — 0:03–0:08 — Procedimiento de propagación (5 min; acumulado: 8 min).

- **Sesión:** M8
- **Fuente:** [`modulos/M8_opcional_monte_carlo.md`](../modulos/M8_opcional_monte_carlo.md)
- **Tipo:** página/diapositiva del libreto

## Libreto

**0:03–0:08 — Procedimiento de propagación (5 min; acumulado: 8 min).**

Dictar el procedimiento en seis pasos. Primero, definir la magnitud de salida y el modelo de medición. Segundo, asignar distribuciones a las magnitudes de entrada y representar sus dependencias mediante una distribución conjunta cuando corresponda. Tercero, generar un conjunto de valores de entrada compatible con esa información. Cuarto, evaluar el modelo con el conjunto generado. Quinto, repetir la generación y la evaluación hasta alcanzar estabilidad numérica suficiente. Sexto, resumir la distribución de salida mediante una estimación, una incertidumbre estándar y un intervalo o una región de cobertura.

**Apoyo en el handout:** ver Handout teórico, §5.1 — Cuándo usar MCM, §5.2 — Procedimiento general y §5.3 — Muestreo de PDFs.

JCGM 102:2011, §7.1.2, sitúa el núcleo del método en las extracciones repetidas de las distribuciones de entrada, o de su distribución conjunta, y en la evaluación de la magnitud de salida. El procedimiento paso a paso se presenta en §7.1.7. Para valores simulados \(y_1,\ldots,y_M\), la media aproxima la esperanza de la salida y la desviación estándar aproxima la incertidumbre estándar asociada a su distribución. Esta desviación caracteriza la dispersión atribuida al mensurando; no es el error numérico de la media simulada.

Explicar también los intervalos. Un intervalo de colas iguales deja la misma probabilidad a cada lado. Un intervalo más corto busca, entre los intervalos que contienen la probabilidad estipulada, el de menor anchura. Ante una salida asimétrica, ambos pueden diferir. Por eso el informe debe declarar la probabilidad y el método de construcción del intervalo.
