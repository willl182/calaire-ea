# 1. Conceptos básicos

## 1.1 Mensurando y resultado de medición

**Mensurando** es la magnitud que se desea medir. La definición debe ser suficientemente detallada para que el resultado tenga una interpretación inequívoca. En ozono, expresiones como “concentración de ozono” suelen ser insuficientes. Conviene especificar, al menos:

- tipo de magnitud: fracción de cantidad de sustancia, concentración másica u otra;
- matriz gaseosa y condiciones relevantes;
- intervalo temporal o regla de promedio;
- ubicación o punto del sistema al que se refiere;
- condiciones de temperatura y presión, si el resultado se convierte entre bases;
- correcciones aplicadas;
- estado operativo del analizador o patrón.

Ejemplo de definición útil:

> Fracción de cantidad de sustancia de ozono en aire sintético suministrado al puerto de muestra del analizador, promediada durante 10 min después de estabilización, expresada en nmol/mol y corregida mediante función de calibración vigente.

La definición determina qué efectos entran en el modelo. Si el mensurando se refiere a un valor instantáneo, la repetibilidad temporal y la respuesta dinámica tienen un papel distinto que si se refiere a un promedio horario. Si el resultado está corregido a condiciones de referencia, la temperatura y la presión pueden aparecer explícitamente. Si el analizador entrega directamente la fracción molar mediante fotometría UV interna, parte de esos efectos puede estar incorporada en la función de indicación, pero sigue siendo necesario evaluar su influencia residual.

El resultado completo incluye la estimación del mensurando y la declaración de incertidumbre. Una forma compacta es

\[
Y = y \pm U,
\]

acompañada por la unidad, el factor de cobertura o la probabilidad de cobertura, el método para obtener el intervalo y la definición del mensurando. El símbolo \(Y\) representa la magnitud de salida; \(y\), la estimación asignada.

## 1.2 Modelo de medición

El modelo expresa la relación entre la magnitud de salida y las entradas:

\[
Y=f(X_1,X_2,\ldots,X_N).
\]

Las entradas pueden ser magnitudes medidas directamente, correcciones, parámetros de calibración, constantes físicas o efectos cuya mejor estimación sea cero pero cuya incertidumbre no sea cero. JCGM GUM-6:2020 enfatiza la especificación del mensurando, la identificación de los efectos, la aptitud del modelo para el propósito, la deriva, los efectos compartidos y la validación.

Como ejemplo bajo supuestos explícitos, la fotometría UV basada en Beer–Lambert puede escribirse

\[
x_{O_3}=
-\frac{k_B T}{\sigma LP}\ln(D)
=-\frac{RT}{\sigma LPN_A}\ln(D),
\]

donde \(x_{O_3}\) es la fracción molar, \(\sigma\) es la sección eficaz por molécula, \(L\) es la longitud óptica efectiva, \(P\) es la presión absoluta, \(T\) es la temperatura termodinámica y \(D=I/I_0\) es la transmitancia adimensional. \(k_B=R/N_A\), por lo que ambas formas son equivalentes. En unidades SI, \(k_BT/P\) tiene dimensión de volumen por molécula y \(\sigma L\), de volumen, de modo que el resultado es adimensional. Si \(\sigma\) se expresa sobre una base molar, la ecuación debe reformularse. Los factores adicionales dependen del diseño óptico, del número de celdas y de la convención de señal. La ecuación exacta debe corresponder al instrumento y al procedimiento; no debe copiarse una versión genérica sin revisar las unidades, la geometría y la definición de \(D\).

Como parametrización puramente ilustrativa para calibración frente a patrón de transferencia puede escribirse

\[
y=\frac{I-b}{m}+\Delta_{drift}+\Delta_{env}+\Delta_{int}.
\]

Aquí, \(I\) es la indicación; \(m\) y \(b\) son la pendiente y el intercepto; y los términos \(\Delta\) representan correcciones residuales expresadas en la unidad de salida. La repetibilidad se incorpora normalmente mediante la incertidumbre de \(I\) o del promedio, no como una corrección física independiente. En un sistema real, la deriva, el ambiente y las interferencias pueden actuar sobre \(I\), \(m\), \(b\), la escala completa o el tiempo, y pueden estar correlacionados. El modelo debe ubicar cada efecto donde actúa físicamente. Cuando la mejor estimación de un efecto residual es cero, su incertidumbre todavía puede contribuir.

El modelo puede ser teórico, empírico o híbrido. En una cadena patrón primario–patrón de transferencia–analizador, el modelo suele ser multietapa. Los parámetros compartidos entre puntos de calibración generan correlación. Tratarlos como observaciones independientes produce incertidumbres incoherentes.

## 1.3 Error e incertidumbre no son sinónimos

El **error de medición** es la diferencia entre el valor medido y el valor de referencia. En general, un error concreto no se conoce exactamente. Puede descomponerse conceptualmente en componentes sistemáticos y aleatorios, pero esa clasificación describe el comportamiento de los efectos, no los métodos Tipo A y Tipo B.

La **incertidumbre de medición** es un parámetro no negativo que caracteriza la dispersión de los valores atribuidos al mensurando a partir de la información usada. No es equivocación, tolerancia, especificación del fabricante ni límite máximo permisible. Tampoco demuestra por sí sola ausencia de sesgo.

La regla fundamental es que un efecto sistemático significativo y conocido debe corregirse cuando sea viable. La incertidumbre asociada a la corrección permanece en el presupuesto. No resulta correcto convertir automáticamente un error conocido en una distribución simétrica centrada en cero para evitar la corrección. Solo si la corrección no es practicable y la decisión está justificada puede modelarse el efecto residual de forma explícita, informando el supuesto y el posible sesgo.

La evaluación **Tipo A** usa el análisis estadístico de los valores medidos (JCGM 100 §§2.3.2 y 4.2). La evaluación **Tipo B** usa otros conocimientos: certificados, especificaciones, resolución, datos previos, literatura, experiencia, límites físicos o juicio experto (JCGM 100 §§2.3.3 y 4.3). “Tipo A” no significa aleatorio y “Tipo B” no significa sistemático. Una misma fuente puede evaluarse por cualquiera de ambos métodos, según la información disponible.

## 1.4 Incertidumbre estándar, combinada y expandida

La **incertidumbre estándar** se expresa como una desviación estándar. Para la entrada \(X_i\), se denota \(u(x_i)\). Tras la propagación, la incertidumbre estándar de salida es \(u_c(y)\), frecuentemente abreviada como \(u(y)\).

La **incertidumbre expandida** es

\[
U=k\,u_c(y),
\]

donde \(k\) es el factor de cobertura. El valor \(k=2\) suele aproximar una probabilidad de cobertura de 95 % bajo una distribución aproximadamente normal y con grados de libertad suficientes, pero no es una regla universal. Con pocos grados de libertad se usa un factor de la distribución \(t\), y con una salida asimétrica conviene informar los extremos directos del intervalo en vez de forzar la forma \(y\pm U\).

## 1.5 Trazabilidad metrológica

La trazabilidad metrológica es la propiedad de un resultado por la cual este puede relacionarse con una referencia mediante una cadena documentada e ininterrumpida de calibraciones, cada una de las cuales contribuye a la incertidumbre. En los sistemas de ozono, la cadena típica enlaza una referencia UV de orden superior, un patrón de transferencia y un analizador.

La trazabilidad exige más que un certificado vigente. Requiere:

1. mensurando compatible en cada nivel;
2. procedimiento de transferencia definido;
3. incertidumbres incorporadas en cada enlace;
4. control de estabilidad entre calibraciones;
5. identificación de correcciones, unidades y condiciones;
6. evidencia de competencia y validez de calibraciones.

Si el mismo patrón, la misma sección eficaz, el mismo sensor de presión o la misma función de calibración intervienen en varios resultados, existe una fuente común. Esa dependencia debe conservarse como covarianza, especialmente al comparar puntos o calcular diferencias.

---
