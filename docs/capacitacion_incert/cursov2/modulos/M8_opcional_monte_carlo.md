# M8 — Método de Monte Carlo y validación del marco GUM

## 1. Ficha

- **Carácter:** **módulo opcional / material avanzado**.
- **Módulo:** M8 — Método de Monte Carlo y validación del marco GUM.
- **Duración adicional:** 30 min, fuera de jornada nominal de 9 h y del recorrido obligatorio de 462 min.
- **Posición:** último módulo del paquete, posterior al taller integrador M7 que cierra recorrido obligatorio.
- **Prerrequisitos:** reconocer mensurando, modelo de medición, magnitudes de entrada, incertidumbre estándar, coeficientes de sensibilidad, distribuciones normal, rectangular y triangular, incertidumbre expandida e intervalo de cobertura.
- **Materiales:** computador con R base; proyector o pantalla compartida; archivo `cursov2/scripts/demo_mcm_beer_lambert.R`; imagen `cursov2/scripts/demo_mcm_pdf_salida.png`; handout, §§5–6; pizarra o diapositiva para anotar los dos intervalos y la tolerancia.
- **Modalidad:** material avanzado opcional, desarrollado como exposición dialogada y demostración del facilitador de 10 min. No hay ejercicio individual ni instalación de software por parte de las personas participantes.
- **Idea fuerza:** Monte Carlo no sustituye el juicio metrológico: propaga numéricamente las distribuciones y dependencias asignadas al modelo, y permite comprobar si una aproximación coincide con esa propagación a la resolución requerida.

Fuente introductoria complementaria: Eurachem/CITAC QUAM 2012, App. E.3, pp. editoriales 108–114. Referencias técnicas principales permanecen JCGM 101 y JCGM 102.

**Advertencia QUAM:** MCM propaga modelo y distribuciones asignadas; no corrige omisiones, doble conteo, mensurando incompleto ni evidencia inadecuada.

La sesión usa una sola magnitud de salida para mostrar la lógica con claridad. JCGM 102:2011 extiende el método a cualquier número de magnitudes de salida, pero sus principios de muestreo, evaluación repetida, estabilidad y comparación sirven como marco verificable para la demostración escalar. Todo contraste debe conservar el mismo modelo, las mismas estimaciones, las mismas distribuciones, las mismas dependencias y la misma probabilidad de cobertura. Si los supuestos cambian entre cálculos, no se están validando métodos: se están comparando evaluaciones diferentes.

## 2. Objetivos específicos del material avanzado opcional

Si se desarrolla este módulo opcional, al finalizar la demostración del facilitador la persona participante podrá:

1. **Describir** en seis pasos el procedimiento de propagación mediante Monte Carlo, desde la asignación de distribuciones de entrada hasta la obtención de una estimación, una incertidumbre estándar y un intervalo de cobertura.
2. **Distinguir** la incertidumbre metrológica de la salida del error numérico de simulación y explicar por qué un número fijo de ensayos no garantiza por sí solo una tolerancia determinada.
3. **Interpretar** la tolerancia numérica \(\delta=0.05\) como media unidad en la última posición decimal elegida, sin tratarla como una nueva componente de incertidumbre ni como un límite instrumental.
4. **Comparar** los extremos de los intervalos obtenidos mediante el marco GUM y Monte Carlo y aplicar el criterio de concordancia definido para la demostración.
5. **Explicar** por qué el veredicto **VALIDACIÓN NO SATISFACTORIA** es un resultado intencional y específico del caso, no un error del programa ni una prueba de superioridad universal de Monte Carlo.

## 3. Guion de exposición con tiempos

El libreto de exposición está organizado en páginas/diapositivas Markdown independientes. Cada página conserva el texto dictable, el minutaje y sus apoyos; este apartado funciona como índice.

1. [M8 — Página 01 — 0:00–0:03 — Apertura y propósito (3 min; acumulado: 3 min).](../paginas/M8_01_0_000_03_apertura_y_proposito_3_min_acumulado_3_min.md)
2. [M8 — Página 02 — 0:03–0:08 — Procedimiento de propagación (5 min; acumulado: 8 min).](../paginas/M8_02_0_030_08_procedimiento_de_propagacion_5_min_acumulado_8_min.md)
3. [M8 — Página 03 — 0:08–0:13 — Número de ensayos, estabilidad y tolerancia (5 min; acumulado: 13 min).](../paginas/M8_03_0_080_13_numero_de_ensayos_estabilidad_y_tolerancia_5_min_acumulado_13_min.md)
4. [M8 — Página 04 — 0:13–0:23 — Demostración en vivo (10 min; acumulado: 23 min).](../paginas/M8_04_0_130_23_demostracion_en_vivo_10_min_acumulado_23_min.md)
5. [M8 — Página 05 — 0:23–0:26 — Interpretación metrológica (3 min; acumulado: 26 min).](../paginas/M8_05_0_230_26_interpretacion_metrologica_3_min_acumulado_26_min.md)
6. [M8 — Página 06 — 0:26–0:30 — Síntesis y enlace (4 min; acumulado: 30 min).](../paginas/M8_06_0_260_30_sintesis_y_enlace_4_min_acumulado_30_min.md)

## 4. Demostración opcional del facilitador

**Tipo:** demostración en vivo guiada; no es un ejercicio individual.

**Duración:** 10 min, integrada en el bloque 0:13–0:23 de la sección 3.

**Enunciado listo para presentar:** “Observaremos dos propagaciones de la misma información de entrada a través del mismo modelo. Antes de cada salida, anticipen qué resultado esperan y justifiquen su respuesta. Al final decidiremos si los límites de cobertura concuerdan dentro de \(\delta=0.05\), sin convertir la comparación en una clasificación universal de métodos”.

**Datos y archivo:** usar `cursov2/scripts/demo_mcm_beer_lambert.R`, sin editarlo. Proyectar las distribuciones de entrada, el presupuesto, la evolución por bloques, los intervalos y el gráfico `cursov2/scripts/demo_mcm_pdf_salida.png`. El facilitador ejecuta; el grupo responde oralmente a las preguntas del bloque de demostración.

**Resultado esperado en una línea:** con diferencias aproximadas de 0.072 y 0.059 frente a \(\delta=0.05\), el veredicto intencional es **VALIDACIÓN NO SATISFACTORIA**, aunque la simulación haya alcanzado estabilidad numérica.

## 5. Errores frecuentes y preguntas típicas

1. **“¿Más ensayos corrigen una distribución de entrada mal elegida?”** No. Más ensayos reducen el error numérico, pero propagan con mayor precisión el supuesto equivocado.
2. **“¿Delta es otra componente del presupuesto?”** No. Es una tolerancia numérica ligada a la posición decimal con la que se juzgan estabilidad y concordancia.
3. **“¿Incertidumbres estándar casi iguales garantizan intervalos iguales?”** No. Dos distribuciones pueden tener dispersión semejante y límites de cobertura diferentes.
4. **“¿VALIDACIÓN NO SATISFACTORIA significa que el script falló?”** No. El script se estabiliza y termina correctamente; el veredicto indica que los resultados comparados no concuerdan dentro de la tolerancia estipulada.
5. **“¿El resultado demuestra que Monte Carlo siempre debe reemplazar al marco GUM?”** No. La conclusión solo vale para el modelo, las entradas, la cobertura, el intervalo y la resolución evaluados.

## 6. Cierre del material avanzado opcional

Monte Carlo aporta una representación numérica de la distribución de salida, mientras el marco GUM conserva su utilidad cuando sus aproximaciones son adecuadas; la validación permite comprobar esa adecuación para un caso definido. El veredicto no satisfactorio de la demostración enseña a separar estabilidad computacional de concordancia metrológica, sin proclamar un ganador universal. Este módulo no añade entregables ni requisitos al curso obligatorio, cerrado previamente con taller integrador M7.

**Enlace con la práctica:** en el Día 2 de laboratorio, `practica/E16_mcm_covarianza.md` aplica este mismo procedimiento al modelo diferencial `NO2=(NOx-NO)/η`, usando la covarianza medida en `practica/E03_covarianza_no_nox.md` y la distribución de eficiencia de `practica/E04_gpt_eficiencia_convertidor.md` como entradas reales en lugar del ejemplo Beer–Lambert.
