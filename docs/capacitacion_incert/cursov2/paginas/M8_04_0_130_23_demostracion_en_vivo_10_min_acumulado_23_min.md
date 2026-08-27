# M8 — Página 04 — 0:13–0:23 — Demostración en vivo (10 min; acumulado: 23 min).

- **Sesión:** M8
- **Fuente:** [`modulos/M8_opcional_monte_carlo.md`](../modulos/M8_opcional_monte_carlo.md)
- **Tipo:** página/diapositiva del libreto

## Libreto

**0:13–0:23 — Demostración en vivo (10 min; acumulado: 23 min).**

Proyectar y ejecutar `Rscript cursov2/scripts/demo_mcm_beer_lambert.R`. Durante los primeros 2 min, mostrar el modelo no lineal y las cinco entradas: coeficiente de absorción con distribución normal; longitud, temperatura y presión con distribuciones rectangulares; cociente de intensidades con distribución triangular simétrica. Preguntar cuál entrada domina el presupuesto. Se espera identificar el cociente de intensidades, cuya contribución estándar es cercana a 0.707 unidades de salida, seguido por el coeficiente de absorción, con aproximadamente 0.310.

Antes de ejecutar, preguntar: “Si misma simulación usa PDF injustificada u omite correlación, ¿más ensayos arreglan evaluación?”. Respuesta: no; solo estabilizan propagación del supuesto equivocado.

Durante los minutos 2–4, mostrar el cálculo mediante la ley de propagación: valor nominal 100.000000; incertidumbre estándar combinada aproximada 0.789731; incertidumbre expandida aproximada 1.579462 con factor 2; intervalo aproximado [98.420538, 101.579462]. Preguntar si el factor 2 garantiza, por definición, el mismo intervalo que la propagación empírica de 95 %. La respuesta esperada es “no; la concordancia debe comprobarse para este caso”.

Durante los minutos 4–7, dejar avanzar el procedimiento por bloques. La semilla fija permite reproducir la secuencia. La ejecución verificada alcanza estabilidad en el bloque 37, con 1 850 000 ensayos. La media esperada es 100.000934; la desviación estándar, 0.789424; y el intervalo de cobertura más corto de 95 %, [98.492630, 101.520573]. Aclarar que los últimos dígitos pertenecen a esta ejecución reproducible, no son constantes universales.

Durante los minutos 7–9, comparar extremos. La diferencia inferior es aproximadamente 0.072092 y la superior 0.058889. Ambas superan \(\delta=0.05\). Antes de mostrar el veredicto, preguntar: “Si las incertidumbres estándar son casi iguales, ¿la validación será necesariamente satisfactoria?”. La respuesta es “no”, porque el criterio examina la cobertura y no solamente una medida global de dispersión.

Durante los minutos 9 y 10, mostrar la gráfica y revelar **VALIDACIÓN NO SATISFACTORIA**. Explicar que la simulación sí se estabilizó, el programa terminó y la salida fue producida correctamente. El resultado es intencional: la concordancia estipulada no se alcanzó a la resolución seleccionada.
