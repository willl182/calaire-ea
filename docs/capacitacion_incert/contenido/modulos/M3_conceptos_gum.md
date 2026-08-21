# M3 — Conceptos GUM: Tipo A/B, PDFs y sensibilidad

## 1 Ficha

- **Duración:** 60 min: 44 min de exposición y 16 min de ejercicio.
- **Posición en la jornada:** tercer módulo; cierra el primer bloque de la jornada y antecede el descanso de 15 min previsto en el diseño maestro.
- **Prerrequisitos:** M1, especialmente la distinción entre incertidumbre del analizador, del patrón y del valor transferido; M2, especialmente el modelo de medición y la interpretación de entradas, salida y coeficientes de sensibilidad en Beer–Lambert.
- **Materiales:** proyección o copia de la ficha Sabio Model 2030; tabla del ejercicio en papel o formato digital; calculadora; pizarra; handout teórico, §§1.3–1.4, 2.1–2.4, 3.1–3.6 y 4.1–4.3.
- **Fuentes principales:** JCGM 100:2008 / ISO/IEC Guide 98-3:2008, §§2.3, 3.2–3.3, 4.2–4.3 y 5.1–5.2; Sabio Environmental, *Model 2030 Portable Ozone Transfer Standard*, ficha técnica de una página, 28 nov. 2023.
- **Idea fuerza:** una incertidumbre estándar no se obtiene aplicando divisores de memoria. Primero se identifica qué información existe, qué efecto representa, dónde entra en el modelo y qué PDF describe de manera defendible ese conocimiento.

## 2 Objetivos específicos

Al finalizar el módulo, la persona participante podrá:

1. **distinguir** evaluaciones Tipo A y Tipo B según el método empleado, sin confundirlas con efectos aleatorios y sistemáticos;
2. **calcular** la desviación estándar experimental, la incertidumbre estándar de una media y sus grados de libertad bajo los supuestos aplicables;
3. **convertir** información RMS, incertidumbres expandidas y límites de especificación en incertidumbres estándar mediante una PDF justificada;
4. **aplicar** coeficientes de sensibilidad para expresar contribuciones en la unidad de la magnitud de salida;
5. **detectar** autocorrelación, correlaciones entre entradas y doble conteo como riesgos para un presupuesto de incertidumbre.

## 3 Guion de exposición con tiempos

### 3.1 Tipo A y Tipo B (0:00–0:08; acumulado 0:08)

**Idea fuerza:** Tipo A y Tipo B describen cómo se evalúa una componente, no la naturaleza física del efecto.

**Guion dictable:**

«Comencemos por una distinción que evita muchos errores. El GUM define la evaluación Tipo A como la que usa análisis estadístico de series de observaciones, y la Tipo B como la que usa medios distintos de ese análisis. Por tanto, Tipo A no es sinónimo de aleatorio y Tipo B no es sinónimo de sistemático. Una corrección por un efecto sistemático puede tener una incertidumbre evaluada con datos repetidos, es decir, Tipo A. Una variación de comportamiento aleatorio puede evaluarse mediante información histórica o una especificación, es decir, Tipo B.»

«La incertidumbre estándar es una desviación estándar que representa la dispersión de valores atribuibles razonablemente a una magnitud. Antes de calcularla necesitamos un modelo de medición, aunque sea sencillo: una salida depende de entradas, correcciones y efectos residuales. El mismo dato de dispersión puede conducir a tratamientos distintos según el mensurando. No es igual estimar una lectura individual que el promedio de diez lecturas.»

«También debemos separar error e incertidumbre. Cuando conocemos un efecto significativo y podemos corregirlo, aplicamos la corrección; la incertidumbre de esa corrección permanece. No convertimos automáticamente un error conocido en una distribución simétrica centrada en cero. La incertidumbre expresa conocimiento incompleto, no reemplaza una corrección necesaria.»

**Referencia integrada:** JCGM 100:2008, definiciones de incertidumbre estándar y evaluaciones Tipo A/B, §§2.3.1–2.3.3, p. 3; error, corrección e incertidumbre, §§3.2.2–3.3.5, pp. 5–6.

### 3.2 Tipo A: dispersión, media e independencia (0:08–0:20; acumulado 0:20)

**Idea fuerza:** dividir por raíz de n solo corresponde cuando el mensurando es la media y las observaciones son independientes bajo condiciones estables.

**Guion dictable:**

«Para una serie de n observaciones, la media aritmética estima el valor esperado. La desviación estándar experimental de las observaciones, s(x), describe la dispersión de una observación. Si el resultado informado es la media y las observaciones son independientes, la incertidumbre estándar de esa media es s(x) dividida por raíz de n. Son cantidades diferentes: s(x) caracteriza una lectura; s(x) dividida por raíz de n caracteriza el promedio.»

\[
\bar{x}=\frac{1}{n}\sum_{j=1}^{n}x_j,
\qquad
s(x)=\sqrt{\frac{\sum_{j=1}^{n}(x_j-\bar{x})^2}{n-1}},
\qquad
\nu=n-1.
\]

\[
u(\bar{x})=\frac{s(x)}{\sqrt n}
\quad\text{solo bajo independencia y para el mensurando media.}
\]

«Los grados de libertad son \(\nu=n-1\) en este caso simple. Expresan cuánta información sustenta la estimación de la varianza y serán relevantes al seleccionar un factor de cobertura. No deben confundirse con el número de cifras ni con el número de componentes del presupuesto.»

«Las secuencias rápidas de un analizador pueden compartir información por filtros digitales, tiempo de residencia o control térmico. Si existe autocorrelación, registrar con mayor frecuencia no crea el mismo número de observaciones independientes. El GUM advierte que, cuando las variaciones están correlacionadas en el tiempo, las fórmulas simples para la media y su desviación estándar pueden ser inapropiadas. Debemos usar un análisis para series correlacionadas, promedios por bloques o un tamaño efectivo de muestra.»

«Antes de dividir por raíz de n formulemos dos preguntas: ¿el resultado representa una lectura futura o un promedio definido por el procedimiento?, y ¿las observaciones son estables e independientes? Sin esas respuestas, la fórmula está incompleta.»

**Referencia integrada:** JCGM 100:2008, media, varianza e incertidumbre de la media, §§4.2.1–4.2.3, p. 10; grados de libertad y observaciones correlacionadas, §§4.2.6–4.2.7, p. 11. Desarrollo: handout, §§2.1–2.4.

### 3.3 Tipo B y asignación de PDFs (0:20–0:28; acumulado 0:28)

**Idea fuerza:** la PDF se asigna a partir de la información disponible y del mecanismo, no por preferencia de cálculo.

**Guion dictable:**

«Una evaluación Tipo B puede apoyarse en especificaciones del fabricante, certificados, mediciones anteriores, literatura, resolución o conocimiento del comportamiento del instrumento. No es necesariamente de menor calidad que una evaluación Tipo A. Su calidad depende de la pertinencia y fiabilidad de la información.»

«Si un certificado declara una incertidumbre expandida U y proporciona el factor de cobertura k, normalmente obtenemos la incertidumbre estándar como U dividido por k. Si una fuente proporciona directamente una desviación estándar o un valor RMS de ruido bajo condiciones definidas, ese valor puede funcionar como incertidumbre estándar de una indicación individual; no se divide de nuevo por raíz de tres. Si solo conocemos límites simétricos más o menos a y no hay razón para favorecer valores dentro del intervalo, una PDF rectangular conduce a a dividido por raíz de tres.»

\[
u=\frac{U}{k}
\quad\text{para una incertidumbre expandida documentada},
\qquad
u=\frac{a}{\sqrt3}
\quad\text{para límites }\pm a\text{ con PDF rectangular}.
\]

«Una PDF normal es defendible cuando conocemos media y desviación estándar o cuando el certificado y el mecanismo la justifican. Una PDF triangular asigna más peso al centro y requiere información que sustente esa preferencia; para semiancho a, su desviación estándar es a dividido por raíz de seis. Una PDF arcoseno corresponde a un mecanismo sinusoidal con fase desconocida; no se elige solo porque una serie suba y baje. La regla es declarar qué sabemos y por qué la PDF representa ese conocimiento.»

**Referencia integrada:** JCGM 100:2008, fuentes Tipo B, §4.3.1, p. 11; incertidumbres citadas, intervalos y distribución rectangular, §§4.3.3–4.3.7, pp. 12–13; distribuciones trapezoidal y triangular, §4.3.9, p. 14; representaciones gráficas, Fig. 2 y §§4.4.4–4.4.6, pp. 17–18. Desarrollo: handout, §§3.1–3.6.

### 3.4 Sensibilidad, combinación y correlación (0:28–0:36; acumulado 0:36)

**Idea fuerza:** antes de combinar, cada incertidumbre de entrada debe convertirse a la unidad de la salida.

**Guion dictable:**

«Representemos el resultado como \(Y=f(X_1,\ldots,X_N)\). El coeficiente de sensibilidad de una entrada es la derivada parcial de la salida respecto a esa entrada, evaluada en las mejores estimaciones. Indica cuánto cambia la salida ante un cambio pequeño de la entrada y permite convertir unidades.»

\[
c_i=\frac{\partial f}{\partial X_i},
\qquad
u_i(y)=|c_i|u(x_i).
\]

«Si las entradas son independientes, combinamos las contribuciones como raíz de la suma de cuadrados. No sumamos directamente límites, tolerancias o porcentajes que permanecen en escalas distintas.»

\[
u_c(y)=\sqrt{\sum_i c_i^2u^2(x_i)}.
\]

«En el ejercicio aparecerán componentes aditivas, expresadas en ppb, y relativas, expresadas como porcentaje de escala completa o del punto seleccionado. Para una corrección aditiva en la misma unidad, el coeficiente suele ser uno. Para una especificación relativa r aplicada a una concentración C, primero expresamos el semiancho absoluto como r por C. La linealidad referida a escala completa no equivale a exactitud relativa a la lectura.»

«Si dos entradas comparten calibración, sensor o patrón, pueden estar correlacionadas. La suma de cuadrados sin covarianzas solo es válida cuando la independencia está justificada. Este módulo introduce la advertencia; el tratamiento completo se retoma cuando el presupuesto lo requiera.»

**Referencia integrada:** JCGM 100:2008, ley de propagación y coeficientes de sensibilidad, §§5.1.1–5.1.3, pp. 18–19; covarianzas y correlaciones, §§5.2.1–5.2.5, pp. 21–23.

### 3.5 Doble conteo y lectura de especificaciones (0:36–0:44; acumulado 0:44)

**Idea fuerza:** cada componente debe representar un efecto físico único y aparecer una sola vez en el presupuesto.

**Guion dictable:**

«El GUM advierte expresamente que no deben contarse dos veces las componentes. Si la repetibilidad observada ya contiene plenamente el efecto de resolución, agregar otra componente de resolución puede duplicarlo. Si la incertidumbre de un certificado integra varios efectos internos, no debemos agregarlos de nuevo salvo que exista una desagregación coherente.»

«Para revisar una fila del presupuesto haremos tres preguntas: ¿qué efecto físico representa?, ¿dónde entra en el modelo?, y ¿está incluido total o parcialmente en otra estimación? Esta comprobación es tan importante como el divisor.»

«Una especificación del fabricante no es automáticamente una incertidumbre estándar ni demuestra el desempeño de cada unidad. Debemos identificar si informa RMS, un límite, porcentaje de escala completa o porcentaje del punto seleccionado. También debemos fijar el intervalo y las condiciones de uso. La ficha Sabio Model 2030 ofrece varios rangos; por eso uno por ciento de escala completa produce valores absolutos distintos según el rango elegido.»

**Referencia integrada:** JCGM 100:2008, advertencia de doble conteo, §4.3.10, p. 14. Sabio Environmental, *Model 2030 Portable Ozone Transfer Standard*, p. 1: ruido de cero 0.6 ppb RMS; deriva límite de cero <1.0 ppb/24 h; linealidad ±1 % FS; generador ±1 % del setpoint; rangos 0–100, 0–200 y 0–500 ppb, entre otros.

## 4 Ejercicio/actividad

**Enunciado listo para entregar:** A partir de la ficha Sabio Model 2030, convierta cada especificación en una incertidumbre estándar, indique la PDF propuesta, el divisor o tratamiento aplicado, la unidad y un supuesto justificativo; no combine todavía las componentes.

**Datos:**

- ruido de cero: **0.6 ppb RMS**;
- deriva límite de cero: **<1.0 ppb/24 h**;
- linealidad: **±1 % de escala completa (FS)**;
- exactitud del generador: **±1 % del punto seleccionado (setpoint)**;
- rango asignado para el ejercicio: **0–200 ppb**;
- punto seleccionado: **120 ppb**.

| Componente | Información original | PDF propuesta | Conversión a incertidumbre estándar | Unidad | Supuesto y justificación |
|---|---|---|---|---|---|
| Ruido | 0.6 ppb RMS |  |  | ppb |  |
| Deriva de cero | <1.0 ppb/24 h |  |  | ppb |  |
| Linealidad | ±1 % FS; FS = 200 ppb |  |  | ppb |  |
| Generador | ±1 % setpoint; setpoint = 120 ppb |  |  | ppb |  |

**Tiempo:** 10 min de trabajo en equipos y 6 min de puesta en común; total acumulado 1:00.

**Resultado esperado:** tabla con cuatro incertidumbres estándar expresadas en ppb, cada una acompañada por una PDF, conversión y supuesto defendibles, sin solución numérica desarrollada ni combinación final.

## 5 Errores frecuentes y preguntas típicas

1. **Error: “Tipo A significa aleatorio y Tipo B significa sistemático”.** Respuesta corta: no; A y B clasifican el método de evaluación, mientras que aleatorio y sistemático describen el comportamiento de los efectos.
2. **Pregunta: “¿Siempre debo dividir una especificación por raíz de tres?”.** Respuesta corta: no; solo corresponde a límites modelados con PDF rectangular. Un RMS que representa una desviación estándar no recibe ese divisor.
3. **Error: dividir el ruido por raíz de n sin definir el mensurando.** Respuesta corta: la división solo procede para la incertidumbre de una media de n observaciones independientes; no para una lectura individual ni para datos autocorrelacionados.
4. **Pregunta: “¿Uno por ciento FS es igual a uno por ciento de la lectura?”.** Respuesta corta: no; FS se aplica al valor de escala completa, mientras que el porcentaje del setpoint o de la lectura depende del valor seleccionado.
5. **Error: sumar resolución, repetibilidad y componentes del certificado sin revisar solapamientos.** Respuesta corta: debe trazarse cada efecto físico y comprobar si ya está contenido en otra estimación para evitar el doble conteo de JCGM 100 §4.3.10.

## 6 Cierre y transición

Tipo A, Tipo B, PDF y sensibilidad forman una sola cadena de decisiones: identificar la información, representarla como incertidumbre estándar y convertirla en contribución a la salida sin duplicar efectos. En M4 se aplicará esta cadena a un presupuesto de incertidumbre de un analizador de ozono, comparando condiciones de laboratorio y campo y evaluando críticamente especificaciones de fabricante.
