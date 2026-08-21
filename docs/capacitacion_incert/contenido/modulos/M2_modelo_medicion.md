# 1. Ficha

**Título:** M2 — Modelo de medición: fotometría UV y Beer–Lambert  
**Duración total:** 40 min  
**Distribución:** exposición guiada, 30 min; ejercicio de sensibilidad de la fracción molar a temperatura y presión, 10 min.  
**Posición en la jornada:** segundo módulo del curso, inmediatamente después de M1 y antes de la introducción sistemática a los conceptos GUM de M3.  
**Prerrequisito:** M1, en particular la distinción entre mensurando, referencia, instrumento y cadena de trazabilidad.  
**Materiales:** diapositiva o pizarra para las ecuaciones; calculadora básica; hoja del ejercicio; extractos de 40 CFR 50 Appendix D, NISTIR 6963, JCGM GUM-6:2020 y handout teórico del curso.

**Idea fuerza del módulo:** una ecuación de medición no es solo una fórmula para obtener un número. Es una representación física que permite identificar qué magnitudes influyen, en qué dirección lo hacen y cuánto aporta la incertidumbre de cada una. En fotometría UV, temperatura, presión, longitud óptica y coeficiente de absorción producen dependencias proporcionales a la fracción molar; el cociente de intensidades entra mediante un logaritmo y requiere especial atención cuando la transmitancia se aproxima a uno.

# 2. Objetivos específicos

Al finalizar el módulo, la persona participante podrá:

1. **Explicar** cómo la disminución de intensidad UV se relaciona con la cantidad de ozono mediante la ley de Beer–Lambert.
2. **Formular** el modelo de fracción molar \(x=-k_BT\ln(D)/(\sigma LP)\), identificando el significado y las unidades de sus inputs.
3. **Derivar** los coeficientes de sensibilidad respecto de \(L\), \(T\), \(P\), \(D\) y \(\sigma\).
4. **Clasificar** fuentes físicas de incertidumbre como aproximadamente constantes o proporcionales a la fracción molar, cuando el modelo y la evidencia sustenten esa clasificación.
5. **Calcular y comparar** las contribuciones estándar asociadas a temperatura y presión en un punto de medición dado.

# 3. Guion de exposición con tiempos

## 3.1 Subbloque 1 — De la absorción UV al mensurando (0–7 min; acumulado: 7 min)

**Idea fuerza:** el fotómetro no observa directamente una fracción molar; observa una disminución de intensidad y la convierte mediante un modelo físico.

**Guion dictable:** Comencemos por separar tres elementos. El mensurando es la fracción molar de ozono que queremos atribuir al gas. Las observaciones primarias son dos intensidades ópticas: \(I_0\), obtenida para una condición de referencia sin absorción de ozono, e \(I\), obtenida cuando el ozono está presente en el trayecto óptico. El puente entre ambas observaciones y el mensurando es la ley de Beer–Lambert.

La transmitancia se define como

\[
D=\frac{I}{I_0}.
\]

La formulación reglamentaria expresa

\[
\text{Transmittance}=\frac{I}{I_0}=e^{-\alpha c l},
\]

y, al despejar la concentración expresada en partes por millón,

\[
c(\text{ppm})=-\frac{10^6}{\alpha l}\ln\left(\frac{I}{I_0}\right).
\]

La lectura física es directa. Sin absorción, \(I\) e \(I_0\) son casi iguales, \(D\) se aproxima a uno y \(\ln D\) se aproxima a cero. Al aumentar la cantidad de ozono en el camino óptico, disminuye \(D\), el logaritmo se hace más negativo y el signo menos situado delante de la expresión produce una concentración positiva.

La regla final de la EPA de 2023 adopta para el coeficiente de absorción del ozono el valor \(304.39\ \text{atm}^{-1}\text{cm}^{-1}\), con incertidumbre estándar \(0.94\ \text{atm}^{-1}\text{cm}^{-1}\). La incertidumbre estándar relativa correspondiente es aproximadamente \(0.31\,\%\). Este parámetro fija la escala de la medición: una variación relativa en el coeficiente produce una variación relativa de igual magnitud y signo contrario en el resultado calculado.

**Referencia exacta del bloque:** EPA, final rule 2023; **40 CFR Part 50, Appendix D, §4.1**; *Federal Register*, página **70595**, página **1 del PDF**, ecuaciones \(\text{Transmittance}=I/I_0=e^{-\alpha c l}\) y \(c(\text{ppm})=-10^6(\alpha l)^{-1}\ln(I/I_0)\). NISTIR 6963, **§3, página impresa 7**, para el principio de fotometría UV.

## 3.2 Subbloque 2 — Modelo de fracción molar y condiciones físicas (7–17 min; acumulado: 17 min)

**Idea fuerza:** temperatura y presión conectan la absorción observada con el número de moléculas y, por tanto, con la fracción molar.

**Guion dictable:** Para trabajar con fracción molar emplearemos como contenido maestro el modelo

\[
x=-\frac{k_B T\ln(D)}{\sigma L P},
\]

donde \(x\) es la fracción molar, \(k_B\) es la constante de Boltzmann, \(T\) es la temperatura termodinámica del gas, \(P\) es la presión absoluta, \(\sigma\) es la sección eficaz de absorción por molécula, \(L\) es la longitud óptica efectiva y \(D=I/I_0\) es la transmitancia.

Leamos el modelo antes de calcular. La temperatura aparece en el numerador: manteniendo los demás inputs fijos, una temperatura mayor produce una fracción molar calculada mayor. Presión, longitud óptica y sección eficaz aparecen en el denominador: si cualquiera aumenta mientras la absorción observada permanece fija, la fracción molar calculada disminuye. La transmitancia está dentro de un logaritmo y, por ello, su comportamiento no es simplemente proporcional.

El modelo obliga a revisar las unidades y la realización de cada magnitud. \(T\) debe ser temperatura termodinámica, no un valor Celsius insertado directamente. \(P\) debe ser presión absoluta, no manométrica. \(L\) debe representar el trayecto óptico efectivo y no solo una dimensión nominal. La definición y las unidades de \(\sigma\) deben ser compatibles con la formulación molecular. Si se usa el coeficiente \(\alpha\) en \(\text{atm}^{-1}\text{cm}^{-1}\), corresponde emplear la forma reglamentaria y las conversiones pertinentes, no sustituirlo automáticamente en la ecuación molecular.

La ecuación (4) de la regulación hace visibles correcciones equivalentes mediante los factores \(T/273\) y \(760/P\), junto con una corrección de longitud asociada a pérdidas de ozono. Esa escritura y el modelo basado en \(k_B\) representan la misma necesidad física: relacionar la absorción con las condiciones del gas y con el camino efectivo de las moléculas que llegan a la celda.

**Referencia exacta del bloque:** **40 CFR Part 50, Appendix D, §4.5.3.10**; *Federal Register*, página **70599**, página **5 del PDF**, ecuación (4), incluidos \(T/273\), \(760/P\) y la corrección de \(L\) por pérdidas. Handout teórico, **§1.2**, modelo de medición. JCGM GUM-6:2020, **§§5.5–5.9 y 6.1–6.7, páginas impresas 4–9**, para especificación y construcción del modelo.

## 3.3 Subbloque 3 — Coeficientes de sensibilidad (17–24 min; acumulado: 24 min)

**Idea fuerza:** una derivada convierte la incertidumbre de un input, expresada en su unidad, en una contribución expresada en la unidad del mensurando.

**Guion dictable:** Para el modelo \(x=f(T,P,L,\sigma,D)\), cada coeficiente de sensibilidad es una derivada parcial evaluada en los mejores estimados disponibles. Las derivadas son

\[
c_T=\frac{\partial x}{\partial T}=\frac{x}{T},
\qquad
c_P=\frac{\partial x}{\partial P}=-\frac{x}{P},
\]

\[
c_L=\frac{\partial x}{\partial L}=-\frac{x}{L},
\qquad
c_\sigma=\frac{\partial x}{\partial \sigma}=-\frac{x}{\sigma},
\]

\[
c_D=\frac{\partial x}{\partial D}
=-\frac{k_B T}{\sigma LPD}
=\frac{x}{D\ln D}.
\]

Los signos tienen interpretación física. \(c_T\) es positivo porque un incremento de temperatura incrementa el valor calculado de \(x\). Los coeficientes de presión, longitud y sección eficaz son negativos porque esas magnitudes dividen la expresión. Como \(0<D<1\), \(\ln D\) es negativo; por ello \(c_D\) también es negativo: una transmitancia mayor representa menor absorción y conduce a una fracción molar menor.

La contribución estándar de un input \(q_i\) se calcula como

\[
u_i(x)=|c_i|u(q_i).
\]

El signo no debe borrarse del razonamiento, porque permite interpretar la respuesta del modelo y resulta necesario al considerar covarianzas. No obstante, para comparar magnitudes de contribuciones independientes se usa el valor absoluto y, al combinar varianzas, cada contribución aparece al cuadrado.

Las sensibilidades relativas de \(T\), \(P\), \(L\) y \(\sigma\) tienen magnitud uno. Un cambio relativo pequeño de uno por ciento en cualquiera produce, en primera aproximación, un cambio relativo de uno por ciento en \(x\), con el signo correspondiente. La sensibilidad a \(D\) contiene \(1/(D\ln D)\). Cuando \(D\) se aproxima a uno, \(\ln D\) se aproxima a cero y la sensibilidad puede crecer; por eso la resolución y estabilidad del cociente de intensidades adquieren especial importancia a baja absorción.

**Referencia exacta del bloque:** Handout teórico, **§4.1**, coeficientes de sensibilidad. JCGM GUM-6:2020, **§§7.1–7.2, páginas impresas 9–10**, evaluación del modelo y sensibilidades. NISTIR 6963, **§11, páginas impresas 14–15**, ecuaciones y presupuesto de incertidumbre.

## 3.4 Subbloque 4 — Fuentes físicas y componentes constantes o proporcionales (24–30 min; acumulado: 30 min)

**Idea fuerza:** el presupuesto debe representar mecanismos físicos; copiar especificaciones sin conectarlas con el modelo no basta.

**Guion dictable:** Conectemos cada término con la realización práctica. Primero, las pérdidas de ozono en líneas, conexiones o superficies hacen que la cantidad que llega a la celda sea menor que la presente aguas arriba. La regulación incorpora una corrección asociada a la longitud o al factor de pérdida. Los materiales de las líneas deben seleccionarse y acondicionarse para minimizar reactividad. Una pérdida conocida debe corregirse; la incertidumbre de esa corrección permanece en el presupuesto.

Segundo, los gradientes de temperatura importan porque el valor introducido en la ecuación debe representar el gas en la región pertinente. Un sensor exacto situado en un punto no representativo no elimina la deficiencia del modelo. Deben considerarse calibración, resolución, estabilidad y diferencia entre la temperatura indicada y la temperatura efectiva de la celda.

Tercero, la exactitud de presión influye de manera inversa. Debe verificarse que la presión sea absoluta, que el punto de medición represente la celda y que no se omitan caídas de presión. Calibración, resolución y estabilidad del sensor son fuentes separadas solamente si representan efectos que no están contenidos en una estimación agregada.

Cuarto, la resolución del cociente de intensidades afecta \(D\). Intervienen resolución digital, ruido óptico, estabilidad de la fuente, detección electrónica y cálculo de \(I/I_0\). Debido a la función logarítmica, una resolución fija de señal puede comportarse aproximadamente como una contribución constante en unidades de fracción molar dentro de un intervalo limitado y puede dominar cerca de cero.

Conviene distinguir componentes proporcionales y constantes. Incertidumbres relativas aproximadamente constantes de \(\sigma\), \(L\), \(T\) y \(P\) producen contribuciones que aumentan con \(x\). Por ejemplo, la incertidumbre relativa de \(0.31\,\%\) del coeficiente de absorción aporta aproximadamente \(0.31\,\%\) del valor medido. En cambio, resolución, ruido de señal, corrección residual de cero o una pérdida expresada como cantidad fija pueden aportar una magnitud casi constante. Esta clasificación depende del modelo y de la evidencia y no debe imponerse por conveniencia.

**Referencia exacta del bloque:** NISTIR 6963, **§§7–8, páginas impresas 9–10**, materiales y líneas; **§11, páginas impresas 14–15**, presupuesto. **40 CFR Part 50, Appendix D, §4.5.3.10** y *Federal Register*, página **70599**, página **5 del PDF**, corrección de longitud por pérdidas. JCGM GUM-6:2020, **§§5.5–5.9, páginas impresas 4–6**, identificación y representación de efectos.

# 4. Ejercicio/actividad

**Título:** Sensibilidad de la fracción molar a temperatura y presión  
**Tiempo:** 10 min, del minuto 30 al 40.  
**Organización sugerida:** 2 min para leer y ordenar datos; 4 min de cálculo individual; 3 min de comparación en parejas; 1 min de puesta en común.

**Enunciado completo:** Para una medición de fracción molar, calcule los coeficientes de sensibilidad respecto de temperatura y presión y sus contribuciones estándar. Interprete el signo de cada coeficiente y compare las magnitudes obtenidas. La comparación debe hacerse después de convertir ambas incertidumbres de entrada a la unidad del mensurando.

**Datos de entrada:**

- \(x=100\ \text{nmol/mol}\)
- \(T=298.15\ \text{K}\)
- \(P=101.325\ \text{kPa}\)
- \(u(T)=0.15\ \text{K}\)
- \(u(P)=0.05\ \text{kPa}\)
- \(c_T=x/T\)
- \(c_P=-x/P\)
- \(u_T(x)=|c_T|u(T)\)
- \(u_P(x)=|c_P|u(P)\)

**Tareas:**

1. Calcule \(c_T\) en \(\text{nmol mol}^{-1}\text{K}^{-1}\).
2. Calcule \(c_P\) en \(\text{nmol mol}^{-1}\text{kPa}^{-1}\).
3. Calcule \(u_T(x)\) y \(u_P(x)\) en \(\text{nmol/mol}\).
4. Explique por qué \(c_T\) es positivo y \(c_P\) es negativo.
5. Indique cuál contribución es mayor y si la diferencia es relevante para este ejemplo.

**Resultado esperado, en una línea:** \(c_T\approx0.335\ \text{nmol mol}^{-1}\text{K}^{-1}\), \(c_P\approx-0.987\ \text{nmol mol}^{-1}\text{kPa}^{-1}\), \(u_T\approx0.0503\ \text{nmol/mol}\), \(u_P\approx0.0494\ \text{nmol/mol}\); las magnitudes son similares.

# 5. Errores frecuentes y preguntas típicas

1. **¿Se puede usar temperatura en grados Celsius dentro del modelo?** No. La ecuación requiere temperatura termodinámica expresada en kelvin.
2. **¿El signo negativo de \(c_P\) significa incertidumbre negativa?** No. El signo indica la dirección del cambio de \(x\); la incertidumbre estándar y la magnitud de la contribución son no negativas.
3. **¿El valor nominal de la longitud de la celda siempre es \(L\)?** No necesariamente. Debe representar la longitud óptica efectiva y considerar la corrección aplicable por pérdidas.
4. **¿La mayor incertidumbre numérica de entrada produce siempre la mayor contribución?** No. Primero debe multiplicarse cada incertidumbre por su coeficiente de sensibilidad y comparar en la unidad de salida.
5. **¿Todos los efectos son proporcionales a la fracción molar?** No. Los efectos de escala suelen ser proporcionales, mientras resolución, ruido o cero pueden comportarse aproximadamente como componentes constantes en un intervalo definido.

# 6. Cierre y transición al M3

El modelo físico nos permitió identificar inputs, signos y factores de conversión hacia la fracción molar. En M3 se usará esta estructura para asignar incertidumbres estándar a los inputs, distinguir evaluaciones Tipo A y Tipo B y comenzar a construir un presupuesto de incertidumbre defendible.
