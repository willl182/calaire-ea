# 1. Ficha

- **Módulo:** M6 — Método de Monte Carlo y validación del marco GUM.
- **Duración:** 30 min.
- **Posición:** sexto módulo del curso, después de la construcción de modelos, la asignación de distribuciones y la elaboración de presupuestos de incertidumbre; antes del taller integrador M7.
- **Prerrequisitos:** reconocer mensurando, modelo de medición, magnitudes de entrada, incertidumbre estándar, coeficientes de sensibilidad, distribuciones normal, rectangular y triangular, incertidumbre expandida e intervalo de cobertura.
- **Materiales:** computador con R base; proyector o pantalla compartida; archivo `contenido/scripts/demo_mcm_beer_lambert.R`; imagen `contenido/scripts/demo_mcm_pdf_salida.png`; handout, §§5–6; pizarra o diapositiva para anotar los dos intervalos y la tolerancia.
- **Modalidad:** exposición dialogada con una demostración en vivo de 10 min. No hay ejercicio individual ni instalación de software por parte de las personas participantes.
- **Idea fuerza:** Monte Carlo no sustituye el juicio metrológico: propaga numéricamente las distribuciones y dependencias asignadas al modelo, y permite comprobar si una aproximación coincide con esa propagación a la resolución requerida.

La sesión usa una sola magnitud de salida para mostrar la lógica con claridad. JCGM 102:2011 extiende el método a cualquier número de magnitudes de salida, pero sus principios de muestreo, evaluación repetida, estabilidad y comparación sirven como marco verificable para la demostración escalar. Todo contraste debe conservar el mismo modelo, las mismas estimaciones, las mismas distribuciones, las mismas dependencias y la misma probabilidad de cobertura. Si los supuestos cambian entre cálculos, no se están validando métodos: se están comparando evaluaciones diferentes.

# 2. Objetivos específicos

Al finalizar el módulo, la persona participante podrá:

1. **Describir** en seis pasos el procedimiento de propagación mediante Monte Carlo, desde la asignación de distribuciones de entrada hasta la obtención de una estimación, una incertidumbre estándar y un intervalo de cobertura.
2. **Distinguir** la incertidumbre metrológica de la salida del error numérico de simulación y explicar por qué un número fijo de ensayos no garantiza por sí solo una tolerancia determinada.
3. **Interpretar** la tolerancia numérica \(\delta=0.05\) como media unidad en la última posición decimal elegida, sin tratarla como una nueva componente de incertidumbre ni como un límite instrumental.
4. **Comparar** los extremos de los intervalos obtenidos mediante el marco GUM y Monte Carlo y aplicar el criterio de concordancia definido para la demostración.
5. **Explicar** por qué el veredicto **VALIDACIÓN NO SATISFACTORIA** es un resultado intencional y específico del caso, no un error del programa ni una prueba de superioridad universal de Monte Carlo.

# 3. Guion de exposición con tiempos

**0:00–0:03 — Apertura y propósito (3 min; acumulado: 3 min).**

Comenzar con esta pregunta: “Si una simulación contiene dos millones de evaluaciones, ¿eso garantiza que representa adecuadamente la medición?”. Recoger dos o tres respuestas y cerrar con una afirmación dictable: “Una gran cantidad de evaluaciones puede reducir el error numérico, pero no corrige un mensurando mal definido, un modelo incompleto, una distribución injustificada ni una dependencia omitida”.

Presentar la diferencia de enfoque. El marco GUM basado en la ley de propagación usa normalmente una aproximación local del modelo y resume la información mediante estimaciones, incertidumbres estándar y covarianzas. Monte Carlo genera realizaciones de las entradas según sus distribuciones, evalúa el modelo para cada realización y construye una representación numérica de la distribución de salida. Ningún enfoque es automáticamente superior; la elección depende de la aptitud para el propósito y de las condiciones del problema.

**0:03–0:08 — Procedimiento de propagación (5 min; acumulado: 8 min).**

Dictar el procedimiento en seis pasos. Primero, definir la magnitud de salida y el modelo de medición. Segundo, asignar distribuciones a las magnitudes de entrada y representar sus dependencias mediante una distribución conjunta cuando corresponda. Tercero, generar un conjunto de valores de entrada compatible con esa información. Cuarto, evaluar el modelo con el conjunto generado. Quinto, repetir la generación y la evaluación hasta alcanzar estabilidad numérica suficiente. Sexto, resumir la distribución de salida mediante una estimación, una incertidumbre estándar y un intervalo o una región de cobertura.

JCGM 102:2011, §7.1.2, sitúa el núcleo del método en las extracciones repetidas de las distribuciones de entrada, o de su distribución conjunta, y en la evaluación de la magnitud de salida. El procedimiento paso a paso se presenta en §7.1.7. Para valores simulados \(y_1,\ldots,y_M\), la media aproxima la esperanza de la salida y la desviación estándar aproxima la incertidumbre estándar asociada a su distribución. Esta desviación caracteriza la dispersión atribuida al mensurando; no es el error numérico de la media simulada.

Explicar también los intervalos. Un intervalo de colas iguales deja la misma probabilidad a cada lado. Un intervalo más corto busca, entre los intervalos que contienen la probabilidad estipulada, el de menor anchura. Ante una salida asimétrica, ambos pueden diferir. Por eso el reporte debe declarar la probabilidad y el método de construcción del intervalo.

**0:08–0:13 — Número de ensayos, estabilidad y tolerancia (5 min; acumulado: 13 min).**

JCGM 102:2011, §§7.2.1–7.2.2, advierte que un número de ensayos fijado de antemano no garantiza resultados con una tolerancia prescrita. La cantidad necesaria depende de la forma de la distribución de salida, de la probabilidad de cobertura y del carácter aleatorio del cálculo. Por esa razón, §7.8 desarrolla un procedimiento adaptativo.

La tolerancia se vincula con las cifras significativas consideradas útiles. JCGM 102:2011, §7.8.2.1, define la tolerancia numérica como media unidad en la última posición decimal significativa seleccionada. Si el resultado se examina a una décima de la unidad de salida, media unidad en esa posición es \(\delta=0.05\). Frase dictable: “Delta no es una incertidumbre adicional ni un criterio de aceptación del instrumento; es la resolución con la que se juzgan la estabilidad del cálculo y la concordancia entre resultados”.

El script trabaja en bloques de 50 000 ensayos. Después de varios bloques calcula la dispersión de la media, la desviación estándar y los extremos del intervalo. Declara estabilidad cuando dos veces cada dispersión es menor o igual que \(\delta\). La lógica corresponde al uso de aplicaciones sucesivas y pruebas de estabilidad de JCGM 102:2011, §7.8.3, pasos g) a n), adaptada aquí a una salida y al control directo de los extremos. Destacar que la media puede parecer estable antes que los límites de cobertura; detenerse solo al estabilizar la media sería insuficiente.

**0:13–0:23 — Demostración en vivo (10 min; acumulado: 23 min).**

Proyectar y ejecutar `Rscript contenido/scripts/demo_mcm_beer_lambert.R`. Durante los primeros 2 min, mostrar el modelo no lineal y las cinco entradas: coeficiente de absorción con distribución normal; longitud, temperatura y presión con distribuciones rectangulares; cociente de intensidades con distribución triangular simétrica. Preguntar cuál entrada domina el presupuesto. Se espera identificar el cociente de intensidades, cuya contribución estándar es cercana a 0.707 unidades de salida, seguido por el coeficiente de absorción, con aproximadamente 0.310.

Durante los minutos 2–4, mostrar el cálculo mediante la ley de propagación: valor nominal 100.000000; incertidumbre estándar combinada aproximada 0.789731; incertidumbre expandida aproximada 1.579462 con factor 2; intervalo aproximado [98.420538, 101.579462]. Preguntar si el factor 2 garantiza, por definición, el mismo intervalo que la propagación empírica de 95 %. La respuesta esperada es “no; la concordancia debe comprobarse para este caso”.

Durante los minutos 4–7, dejar avanzar el procedimiento por bloques. La semilla fija permite reproducir la secuencia. La ejecución verificada alcanza estabilidad en el bloque 37, con 1 850 000 ensayos. La media esperada es 100.000934; la desviación estándar, 0.789424; y el intervalo de cobertura más corto de 95 %, [98.492630, 101.520573]. Aclarar que los últimos dígitos pertenecen a esta ejecución reproducible, no son constantes universales.

Durante los minutos 7–9, comparar extremos. La diferencia inferior es aproximadamente 0.072092 y la superior 0.058889. Ambas superan \(\delta=0.05\). Antes de mostrar el veredicto, preguntar: “Si las incertidumbres estándar son casi iguales, ¿la validación será necesariamente satisfactoria?”. La respuesta es “no”, porque el criterio examina la cobertura y no solamente una medida global de dispersión.

Durante el minuto 9–10, mostrar la gráfica y revelar **VALIDACIÓN NO SATISFACTORIA**. Explicar que la simulación sí se estabilizó, el programa terminó y la salida fue producida correctamente. El resultado es intencional: la concordancia estipulada no se alcanzó a la resolución seleccionada.

**0:23–0:26 — Interpretación metrológica (3 min; acumulado: 26 min).**

JCGM 102:2011, §8.1, recomienda comparar el marco GUM y Monte Carlo cuando existan dudas acerca de las condiciones de aplicación de la aproximación. El objetivo de §8.3 es determinar si los resultados concuerdan dentro de tolerancias numéricas estipuladas. La nota 1 de §8.3 limita la validación a la probabilidad y a la región de cobertura especificadas; la nota 2 permite formular la prueba mediante los parámetros que definen otro tipo de región. Para esta salida escalar, los parámetros comparados son los extremos del intervalo.

Como 0.072 y 0.059 son mayores que 0.05, la validación es no satisfactoria. Esto significa que, para este modelo, estas distribuciones, esta probabilidad, este tipo de intervalo y esta resolución, la aproximación comparada no reproduce los límites obtenidos mediante Monte Carlo. Puede informarse el resultado de Monte Carlo o estudiarse una aproximación mejorada. No debe extrapolarse la conclusión a otros niveles, amplitudes de incertidumbre o regímenes de operación.

**0:26–0:30 — Síntesis y enlace (4 min; acumulado: 30 min).**

Pedir al grupo que complete oralmente tres frases: “Monte Carlo propaga…”, “Delta representa…” y “Validación no satisfactoria significa…”. Respuestas esperadas: distribuciones completas mediante evaluaciones repetidas; una tolerancia asociada a la resolución numérica; y falta de concordancia bajo condiciones estipuladas, no fallo informático. Concluir que estabilidad numérica y validación son pruebas distintas.

**Referencias verificadas:** JCGM 102:2011, *Evaluation of measurement data — Supplement 2 to the “Guide to the expression of uncertainty in measurement” — Extension to any number of output quantities*, primera edición, 2011, también ISO/IEC Guide 98-3:2008/Suppl.2:2011: §§7.1.2 y 7.1.7, fundamento y procedimiento; §§7.2.1–7.2.2, número de ensayos; §7.8.2.1, tolerancia; §7.8.3, procedimiento adaptativo; §§8.1–8.3, validación. JCGM 101:2008 es la referencia para una sola salida; JCGM 102:2011 remite a su procedimiento escalar en §7.8.3, nota 3. Complementan estas fuentes `contenido/handout/handout_teorico_gum_o3.md`, §§5–6, y `contenido/scripts/demo_mcm_beer_lambert.R`.

# 4. Ejercicio/actividad

**Tipo:** demostración en vivo guiada; no es un ejercicio individual.

**Duración:** 10 min, integrada en el bloque 0:13–0:23 de la sección 3.

**Enunciado listo para presentar:** “Observaremos dos propagaciones de la misma información de entrada a través del mismo modelo. Antes de cada salida, anticipen qué resultado esperan y justifiquen su respuesta. Al final decidiremos si los límites de cobertura concuerdan dentro de \(\delta=0.05\), sin convertir la comparación en una clasificación universal de métodos”.

**Datos y archivo:** usar `contenido/scripts/demo_mcm_beer_lambert.R`, sin editarlo. Proyectar las distribuciones de entrada, el presupuesto, la evolución por bloques, los intervalos y el gráfico `contenido/scripts/demo_mcm_pdf_salida.png`. El facilitador ejecuta; el grupo responde oralmente a las preguntas del bloque de demostración.

**Resultado esperado en una línea:** con diferencias aproximadas de 0.072 y 0.059 frente a \(\delta=0.05\), el veredicto intencional es **VALIDACIÓN NO SATISFACTORIA**, aunque la simulación haya alcanzado estabilidad numérica.

# 5. Errores frecuentes y preguntas típicas

1. **“¿Más ensayos corrigen una distribución de entrada mal elegida?”** No. Más ensayos reducen el error numérico, pero propagan con mayor precisión el supuesto equivocado.
2. **“¿Delta es otra componente del presupuesto?”** No. Es una tolerancia numérica ligada a la posición decimal con la que se juzgan estabilidad y concordancia.
3. **“¿Incertidumbres estándar casi iguales garantizan intervalos iguales?”** No. Dos distribuciones pueden tener dispersión semejante y límites de cobertura diferentes.
4. **“¿VALIDACIÓN NO SATISFACTORIA significa que el script falló?”** No. El script se estabiliza y termina correctamente; el veredicto indica que los resultados comparados no concuerdan dentro de la tolerancia estipulada.
5. **“¿El resultado demuestra que Monte Carlo siempre debe reemplazar al marco GUM?”** No. La conclusión solo vale para el modelo, las entradas, la cobertura, el intervalo y la resolución evaluados.

# 6. Cierre y transición

Monte Carlo aporta una representación numérica de la distribución de salida, mientras el marco GUM conserva su utilidad cuando sus aproximaciones son adecuadas; la validación permite comprobar esa adecuación para un caso definido. El veredicto no satisfactorio de la demostración enseña a separar estabilidad computacional de concordancia metrológica, sin proclamar un ganador universal. M7 retomará esta disciplina para integrar modelo, componentes, propagación, cobertura y reporte en un presupuesto completo y defendible.
