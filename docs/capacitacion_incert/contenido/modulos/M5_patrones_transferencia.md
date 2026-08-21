# M5 — Patrones de transferencia: calibración multipunto, deriva y verificación

## 1. Ficha

- **Duración:** 60 min.
- **Posición en el curso:** módulo 5 de 7; sigue al presupuesto de incertidumbre del analizador y precede a la demostración de propagación mediante Monte Carlo.
- **Prerrequisitos:** M1–M4. La persona participante debe reconocer la cadena de trazabilidad del ozono, interpretar un modelo de medición, distinguir evaluaciones Tipo A y Tipo B, y comprender incertidumbre estándar, sensibilidad y presupuesto de incertidumbre.
- **Materiales:** proyector o pantalla; calculadora, hoja de cálculo o software estadístico; `contenido/datasets/dataset_verificacion_multipunto.csv`; `contenido/datasets/dataset_metadata.md`; certificado simulado incluido en el enunciado; hoja o archivo para registrar regresión, diferencias y residuos.
- **Fuentes principales:** USEPA P1016Y93, §§4–5 y App. A; USEPA, *SOP for Calibrators*, §12; CARB, *Performance Audits Using a Portable Ozone Transfer Standard*, v5, App. C, §§C.7–C.9; JCGM GUM-6:2020, §10.6; USEPA, *Quality Assurance Handbook for Air Pollution Measurement Systems*, vol. II, §12.4.
- **Idea fuerza:** verificar no es ajustar hasta obtener coincidencia; es conservar el estado encontrado y obtener evidencia de que la relación metrológica permanece aceptable bajo un criterio declarado.

## 2. Objetivos específicos

Al finalizar el módulo, la persona participante podrá:

1. **Distinguir** calibración, verificación, reverificación y ajuste, explicando qué evidencia se pierde cuando se interviene el instrumento antes de registrar su estado encontrado.
2. **Corregir** la indicación de una referencia mediante la pendiente y el intercepto de su certificado, conservando por separado los datos originales y los valores corregidos.
3. **Calcular e interpretar** diferencias por punto, pendiente, intercepto y residuos para cada ciclo de una comparación multipunto.
4. **Evaluar** la estabilidad entre tres ciclos mediante la dispersión de pendientes e interceptos y reconocer indicios de deriva, curvatura o estabilización insuficiente.
5. **Emitir y documentar** una decisión de conformidad contra límites explícitos, identificando el requisito decisivo y una comprobación técnica previa a cualquier ajuste.

## 3. Guion de exposición con tiempos

**Bloque 0–8 min — Verificación, calibración y estado encontrado.**

Comience con una pregunta: “Si ajustamos el instrumento antes de comparar, ¿qué sabemos sobre su desempeño durante el periodo anterior?”. Recoja dos o tres respuestas y establezca la distinción. La **calibración** determina una relación entre indicaciones y valores de referencia, junto con información para interpretar el resultado. La **verificación** aporta evidencia de que se cumplen requisitos especificados. La **reverificación** comprueba que la relación previamente establecida continúa siendo válida. El **ajuste** modifica la respuesta del instrumento y, por ello, no debe confundirse con la observación independiente de su desempeño.

Un patrón de transferencia lleva un valor de referencia desde un sistema de mayor jerarquía hasta otro instrumento o lugar. Su utilidad depende de una relación documentada, de una incertidumbre adecuada al propósito y de estabilidad entre calibraciones. Un certificado vigente no elimina la necesidad de controlar lo ocurrido desde su emisión.

Lea y explique esta cita exacta: “A candidate transfer standard must pass all the requirements below before being used for O3 measurement activities.” La frase exige evidencia previa y criterios, no confianza basada únicamente en que el equipo entrega valores plausibles (USEPA, *Transfer Standards for the Calibration of Air Monitoring Analyzers for Ozone*, P1016Y93, §4.1, p. física 33).

**Bloque 8–16 min — Diseño de una comparación multipunto.**

Explique que un diseño útil separa **nivel**, **ciclo** y **tiempo**. Cada ciclo incluye cero y varios niveles distribuidos en el intervalo de uso. El cero identifica desplazamientos aditivos; los niveles bajos permiten evaluar diferencias absolutas; los niveles medios sostienen la estimación de la relación; y los niveles altos revelan diferencias proporcionales o curvatura. Repetir ciclos permite distinguir estabilidad de una secuencia aislada.

P1016Y93 establece para la verificación un mínimo de tres ciclos estables, cada uno con cero y al menos seis concentraciones superiores a cero. Su apéndice indica exactamente: “A verification consists of three (3) testing cycles (performed independently) in which the candidate standard’s measurements are compared to those of the bench standard” (P1016Y93, §4.4.1 y App. A, pp. físicas 37 y 59).

Presente los controles del montaje: calentamiento, acondicionamiento de líneas, aire cero, longitud y material de tubería, ausencia de fugas, flujo excedente, presión, temperatura y criterio de estabilidad. CARB advierte: “Incorrect venting of bypass flow will affect the total flow presented to the station and may introduce ambient air into the test path” (CARB, v5, App. C, §C.7.2, p. física 12). Una discrepancia puede originarse en el patrón, el equipo evaluado o la instalación; no debe atribuirse automáticamente a uno de ellos.

El registro mínimo por punto comprende fecha y hora, ciclo, nivel nominal, indicaciones de referencia y equipo evaluado, temperatura, presión, flujo, configuración, tiempo de estabilización e incidencias. El SOP de calibradores aporta una regla operativa: “It is recommended to wait for a good stability (less than 1 ppb change in 5 minutes) before calibrating the point instead of calibrating the point consecutively until the point becomes stable” (USEPA, *SOP for Calibrators*, §12.3.3.1.7, p. física 10). La cifra pertenece a ese procedimiento; el principio transferible consiste en demostrar estabilidad antes de registrar o ajustar.

**Bloque 16–24 min — Corrección por certificado, regresión y residuos.**

Muestre que la indicación de la referencia no siempre es el valor que debe usarse como eje de comparación. Si el certificado simulado define

\[
X=\frac{I_{ref}-b}{m},
\]

primero se corrige la indicación \(I_{ref}\), y después se compara el equipo evaluado con \(X\). Los datos originales nunca se sobrescriben. Deben existir columnas distintas para indicación, valor corregido, diferencia y resultado de la regresión.

Para cada ciclo se ajusta

\[
y_i=b_0+m_0X_i+e_i,
\]

donde \(m_0\) es la pendiente, \(b_0\) el intercepto y \(e_i\) el residuo. Una pendiente diferente de uno sugiere un efecto proporcional. Un intercepto diferente de cero sugiere un efecto aditivo. El residuo muestra la parte que la recta no explica: un patrón curvo puede revelar falta de ajuste; una tendencia con el orden temporal puede indicar deriva o estabilización incompleta; un punto aislado exige revisar el registro antes de excluirlo.

P1016Y93 describe el ajuste así: “an ordinary least squares linear regression line is fitted to data from all concentration test points to predict the measurement from the candidate transfer standard as a simple linear function of the measurement from the standard of higher authority” (P1016Y93, App. A, §A3, p. física 61). Aclare que la regresión del ejercicio sigue ese procedimiento. Una evaluación metrológica más amplia puede requerir incertidumbre en ambos ejes y covarianzas compartidas.

No use el coeficiente de determinación como única prueba. Una relación casi perfectamente lineal puede conservar una pendiente inaceptable, un intercepto importante o diferencias por punto fuera del límite. La decisión se toma con todos los requisitos declarados.

**Bloque 24–32 min — Estabilidad, deriva y decisión de ajustar.**

Compare tres escalas temporales: variación dentro de un punto, diferencias entre ciclos y cambio entre verificaciones separadas. La deriva puede actuar sobre cero, pendiente, dispersión o varios elementos a la vez. La desviación estándar de las pendientes y de los interceptos entre ciclos proporciona una comprobación sencilla de estabilidad durante la verificación, pero no sustituye la historia de calibraciones.

JCGM GUM-6 declara: “Whenever the standard is used, it is necessary to update its value and standard uncertainty reflecting the possible change in the measurement standard since it was last calibrated” (JCGM GUM-6:2020, §10.6.1). La historia temporal puede justificar un modelo de deriva y una predicción al tiempo de uso; esa predicción también posee incertidumbre y puede constituir extrapolación.

Explique por qué ajustar con frecuencia puede empeorar la evidencia. La USEPA señala: “Performing frequent adjustments to provide the ‘most accurate data possible’ can sometimes be self-defeating and result in additional measurement uncertainty” (*Quality Assurance Handbook*, vol. II, §12.4). Si una verificación cumple, se conserva el estado y se documenta. Si falla, primero se revisan referencia, certificado, aire cero, tubería, flujo, presión, temperatura, estabilización, factores internos y mantenimiento. Solo después se decide repetir, reparar, ajustar o recalibrar conforme al procedimiento autorizado.

**Bloque 52–60 min — Puesta en común y síntesis posterior al ejercicio.**

Solicite a dos grupos que comuniquen únicamente cuatro elementos: decisión, requisito decisivo, patrón de residuos y comprobación previa al ajuste. Contraste datos, criterio, interpretación y acción: los datos muestran; el criterio clasifica; la interpretación propone causas; el procedimiento autoriza acciones. Una causa posible no debe escribirse como hecho confirmado.

Cierre el bloque con la secuencia de baja fricción: **corregir la referencia, conservar los originales, evaluar todos los puntos y ciclos, inspeccionar residuos, aplicar el criterio predefinido y documentar antes de intervenir**. P1016Y93 resume el deber documental: “Ensure all documentation is complete and all records are saved to the appropriate data storage system” (§5.1, p. física 40).

## 4. Ejercicio/actividad

**Duración total: 20 min (acumulado: 32–52 min).**

**Enunciado.** Trabajen en parejas con `contenido/datasets/dataset_verificacion_multipunto.csv`. El archivo contiene tres ciclos de verificación. Cada ciclo presenta cero previo, seis niveles cercanos a 20, 40, 70, 100, 140 y 180 ppb, y cero posterior. Las columnas relevantes son `ciclo`, `punto`, `nivel_nominal`, `lectura_ref`, `lectura_uut`, `T_celda_K`, `P_celda_kPa` y `flujo_L_min`.

El certificado simulado de la referencia establece:

- pendiente \(m=1.003\);
- intercepto \(b=-0.4\ \text{ppb}\);
- corrección \(X=(\text{lectura_ref}-b)/m\);
- incertidumbre expandida \(U(X)=0.5\ \text{ppb}+0.01X\), con \(k=2\).

**Trabajo de cálculo, 8 min (32–40 min).** Conserven `lectura_ref` y creen una columna para \(X\). Para cada fila calculen \(d=\text{lectura_uut}-X\). Para cada ciclo ajusten `lectura_uut = intercepto + pendiente × X` usando ceros y niveles, calculen residuos y registren pendiente, intercepto, residuo de mayor magnitud, cero previo y cero posterior. No calculen diferencia porcentual cuando \(X=0\).

**Trabajo de evaluación, 12 min (40–52 min).** Apliquen el siguiente **criterio de conformidad didáctico, fijado antes del análisis**:

- para cada punto con \(X\le50\ \text{ppb}\): \(|d|\le1.5\ \text{ppb}\);
- para cada punto con \(X>50\ \text{ppb}\): \(|100d/X|\le3.1\%\);
- pendiente de cada ciclo entre 0.97 y 1.03;
- intercepto de cada ciclo entre −3 y +3 ppb;
- desviación estándar de las tres pendientes menor que 0.0075;
- desviación estándar de los tres interceptos menor que 1.00 ppb.

Los límites reproducen con finalidad formativa P1016Y93 §4.4.1 y App. A. La incertidumbre expandida del certificado no se sumará a los límites: el ejercicio usa una regla binaria simple. Para un uso real, el sistema de calidad debe definir la regla de decisión y el tratamiento del riesgo.

Entreguen una tabla de tres filas, una por ciclo, con pendiente, intercepto, máxima diferencia y máxima magnitud de residuo. Añadan una conclusión de máximo 100 palabras: **conforme** o **no conforme**, requisito decisivo, patrón visible en los residuos y una comprobación técnica previa a cualquier ajuste. No se solicita solución numérica desarrollada.

**Resultado esperado:** decisión de conformidad trazable, sustentada en valores de referencia corregidos, requisitos por punto y por ciclo, estabilidad entre ciclos e inspección de residuos.

## 5. Errores frecuentes y preguntas típicas

1. **¿Puedo usar `lectura_ref` directamente?** No. Debe aplicarse la ecuación del certificado y conservar tanto la indicación original como el valor corregido.
2. **¿Una pendiente aceptable demuestra conformidad?** No. También deben cumplir intercepto, diferencias por punto, estabilidad entre ciclos y cualquier otro requisito declarado.
3. **¿Un coeficiente de determinación cercano a uno elimina la necesidad de revisar residuos?** No. Puede coexistir con sesgo proporcional, desplazamiento o curvatura sistemática.
4. **¿Si un punto falla debo ajustar inmediatamente?** No. Primero se revisan estabilidad, montaje, aire cero, flujo, presión, tubería, certificado, transcripción y estado de ambos instrumentos.
5. **¿La deriva es simplemente la diferencia entre cero previo y cero posterior?** No. Esa diferencia es un diagnóstico de corto plazo; la deriva también puede afectar pendiente y requiere historia temporal para caracterizarse.

Errores frecuentes adicionales son sobrescribir datos originales, mezclar niveles de ciclos distintos en una única regresión, calcular porcentajes cerca de cero, eliminar un punto sin causa técnica documentada, redondear antes de decidir y presentar una hipótesis causal como conclusión comprobada.

## 6. Cierre y transición

Una verificación defendible conserva el estado encontrado, aplica las correcciones vigentes, evalúa puntos, regresión, residuos y estabilidad, y documenta la decisión antes de cualquier intervención. El M6 retomará este principio de modelo explícito para comparar la propagación lineal con Monte Carlo cuando la no linealidad o las distribuciones de entrada hagan insuficiente una aproximación simple.