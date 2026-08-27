# M8 — Página 03 — 0:08–0:13 — Número de ensayos, estabilidad y tolerancia (5 min; acumulado: 13 min).

- **Sesión:** M8
- **Fuente:** [`modulos/M8_opcional_monte_carlo.md`](../modulos/M8_opcional_monte_carlo.md)
- **Tipo:** página/diapositiva del libreto

## Libreto

**0:08–0:13 — Número de ensayos, estabilidad y tolerancia (5 min; acumulado: 13 min).**

JCGM 102:2011, §§7.2.1–7.2.2, advierte que un número de ensayos fijado de antemano no garantiza resultados con una tolerancia prescrita. La cantidad necesaria depende de la forma de la distribución de salida, de la probabilidad de cobertura y del carácter aleatorio del cálculo. Por esa razón, §7.8 desarrolla un procedimiento adaptativo.

La tolerancia se vincula con las cifras significativas consideradas útiles. JCGM 102:2011, §7.8.2.1, define la tolerancia numérica como media unidad en la última posición decimal significativa seleccionada. Si el resultado se examina a una décima de la unidad de salida, media unidad en esa posición es \(\delta=0.05\). Frase dictable: “Delta no es una incertidumbre adicional ni un criterio de aceptación del instrumento; es la resolución con la que se juzgan la estabilidad del cálculo y la concordancia entre resultados”.

**Apoyo en el handout:** ver Handout teórico, §5.4 — Procedimiento adaptativo y §5.5 — Intervalos de cobertura.

El script trabaja en bloques de 50 000 ensayos. Después de varios bloques calcula la dispersión de la media, la desviación estándar y los extremos del intervalo. Declara estabilidad cuando dos veces cada dispersión es menor o igual que \(\delta\). La lógica corresponde al uso de aplicaciones sucesivas y pruebas de estabilidad de JCGM 102:2011, §7.8.3, pasos g) a n), adaptada aquí a una salida y al control directo de los extremos. Destacar que la media puede parecer estable antes que los límites de cobertura; detenerse solo al estabilizar la media sería insuficiente.
