# Evaluación de incertidumbre en analizadores de ozono y patrones de transferencia

## Propósito y alcance

Este handout presenta fundamentos y métodos para evaluar la incertidumbre de medición en sistemas de ozono basados en analizadores y patrones de transferencia. Sigue la familia de documentos GUM y separa tres referencias que suelen confundirse:

- **JCGM 100:2008** contiene el GUM clásico: la evaluación Tipo A y Tipo B, la ley de propagación de la incertidumbre, la incertidumbre combinada, la incertidumbre expandida y el informe.
- **JCGM 101:2008** es el Suplemento 1: propagación de distribuciones mediante el método de Monte Carlo (MCM) para modelos con una magnitud de salida.
- **JCGM 102:2011** es el Suplemento 2: extensión a cualquier número de magnitudes de salida, incluidas matrices de covarianza y regiones de cobertura multivariantes.

JCGM GUM-1:2023 sirve como introducción vigente a la familia GUM. JCGM GUM-6:2020 desarrolla la construcción, selección y validación de modelos de medición.

El objetivo no consiste en obtener una cifra de incertidumbre mediante una plantilla mecánica. El objetivo consiste en construir una representación defendible del conocimiento disponible sobre el mensurando, el modelo, los datos y las fuentes de variación. Un modelo físicamente incompleto no mejora por usar un cálculo más sofisticado. Del mismo modo, una simulación con millones de valores no compensa PDFs mal asignadas, correlaciones omitidas ni el doble conteo.

---

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

# 2. Evaluación Tipo A

## 2.1 Media, desviación estándar e incertidumbre de la media

Para \(n\) observaciones \(x_1,\ldots,x_n\) obtenidas bajo condiciones de repetibilidad, la estimación de la expectativa es la media aritmética:

\[
\bar{x}=\frac{1}{n}\sum_{j=1}^{n}x_j.
\]

La desviación estándar experimental de las observaciones es

\[
s(x)=\sqrt{\frac{1}{n-1}\sum_{j=1}^{n}(x_j-\bar{x})^2}.
\]

Si las observaciones son independientes y representan la misma distribución estable, la incertidumbre estándar de la media es

\[
u(\bar{x})=s(\bar{x})=\frac{s(x)}{\sqrt{n}}.
\]

No debe confundirse \(s(x)\), la dispersión de una lectura, con \(s(\bar{x})\), la incertidumbre del promedio. La elección depende del mensurando. Si el resultado es una lectura individual futura, dividir por \(\sqrt n\) puede ser incorrecto. Si el resultado es el promedio de las \(n\) observaciones, la división resulta adecuada bajo independencia.

Ejemplo: diez lecturas de 80 nmol/mol presentan \(s=0.60\) nmol/mol. Para el promedio de diez lecturas independientes,

\[
u(\bar{x})=0.60/\sqrt{10}=0.19\ \text{nmol/mol}.
\]

Para una lectura individual bajo las mismas condiciones, el componente de repetibilidad sigue siendo 0.60 nmol/mol.

## 2.2 Grados de libertad

Para una estimación de la varianza basada en \(n\) observaciones independientes, los grados de libertad suelen ser

\[
\nu=n-1.
\]

Los grados de libertad reflejan la cantidad de información usada para estimar la incertidumbre, no el número de cifras ni el número de componentes. Son necesarios al seleccionar el factor de cobertura y al calcular los grados efectivos mediante Welch–Satterthwaite.

Para una evaluación Tipo B, los grados de libertad pueden considerarse infinitos si la incertidumbre se conoce con alta fiabilidad y no depende de una muestra finita. Si el conocimiento es débil, el GUM permite asignar grados de libertad finitos mediante un juicio sobre la fiabilidad de \(u(x_i)\), pero la asignación debe documentarse y no debe convertirse en una precisión ficticia.

## 2.3 Papel de la distribución t

Hay dos usos relacionados, pero distintos:

1. En el GUF clásico, \(s/\sqrt n\) es la incertidumbre estándar de la media y la distribución \(t\) se usa para determinar el factor de cobertura cuando la varianza se estima con pocos grados de libertad.
2. En la propagación de distribuciones, bajo los supuestos de observaciones normales, una media desconocida y una varianza desconocida, puede asignarse una distribución \(t\) desplazada y escalada:

\[
X=\bar{x}+\frac{s}{\sqrt n}T_\nu,\qquad \nu=n-1.
\]

Para \(\nu>2\), la varianza de \(T_\nu\) es \(\nu/(\nu-2)\). Por tanto, la varianza de esta distribución asignada a \(X\) es

\[
V(X)=\frac{s^2}{n}\frac{\nu}{\nu-2}
=\frac{s^2}{n}\frac{n-1}{n-3},\qquad n>3.
\]

Esto explica el factor que aparece en algunas guías. No debe mezclarse sin explicación con la fórmula Tipo A del GUM \(s^2/n\). Se trata de representaciones con supuestos y objetivos distintos.

## 2.4 Autocorrelación y tamaño de muestra efectivo

Las lecturas secuenciales de los analizadores suelen estar autocorrelacionadas por los filtros digitales, el tiempo de residencia, el control térmico, la respuesta de la celda o la estabilidad del generador. Si los datos no son independientes, \(s/\sqrt n\) subestima la incertidumbre de la media.

La forma general usa la función de autocorrelación muestral \(\rho_k\):

\[
\operatorname{Var}(\bar{x})\approx
\frac{s^2}{n}\left[1+2\sum_{k=1}^{K}
\left(1-\frac{k}{n}\right)\rho_k\right].
\]

Puede definirse un tamaño efectivo de muestra

\[
n_{\mathrm{eff}}=
\frac{n}{1+2\sum_{k=1}^{K}(1-k/n)\rho_k},
\]

y entonces

\[
u(\bar{x})\approx\frac{s}{\sqrt{n_{\mathrm{eff}}}}.
\]

Para una aproximación AR(1) con autocorrelación de retardo 1 \(\rho\) y una serie suficientemente larga,

\[
n_{\mathrm{eff}}\approx n\frac{1-\rho}{1+\rho}.
\]

Ejemplo: \(n=60\), \(s=0.50\) nmol/mol y \(\rho=0.70\). Entonces

\[
n_{\mathrm{eff}}\approx60\frac{0.30}{1.70}=10.6,
\qquad
u(\bar{x})\approx0.50/\sqrt{10.6}=0.154\ \text{nmol/mol}.
\]

Ignorar la autocorrelación daría 0.065 nmol/mol, menos de la mitad. El resultado muestra por qué una alta frecuencia de adquisición no equivale a una cantidad igual de información independiente.

Antes de aplicar una corrección, conviene revisar la estabilidad, la tendencia, el tiempo de calentamiento y los cambios de régimen. La autocorrelación no corrige la deriva. Si la serie contiene una tendencia, primero debe modelarse o restringirse a un tramo estacionario defendible. Las alternativas incluyen los promedios por bloques, los modelos de series temporales y los diseños con réplicas independientes.

---

# 3. Evaluación Tipo B y asignación de PDFs

## 3.1 De la información disponible a una distribución

La evaluación Tipo B comienza con información real: límites, una estimación y una desviación estándar, un certificado con incertidumbre expandida, la resolución, el historial, una especificación o un mecanismo físico. La PDF debe representar ese conocimiento, no una preferencia de software.

El principio de máxima entropía selecciona la distribución menos informativa compatible con las restricciones conocidas. No implica usar siempre una distribución rectangular. Si solo se conocen límites estrictos y no hay razón para favorecer determinados valores, la distribución rectangular es la elección natural. Si se conocen la media y la varianza sin límites, la distribución normal maximiza la entropía bajo esas restricciones. Si el mecanismo es sinusoidal y tiene una fase desconocida, la distribución arcoseno surge del mecanismo, no de la comodidad.

## 3.2 Distribución rectangular

Para \(X\in[a,b]\) con densidad uniforme:

\[
E(X)=\frac{a+b}{2},\qquad
u^2(X)=\frac{(b-a)^2}{12}.
\]

Si la especificación se expresa como \(x\pm a\), el semiancho es \(a\) y

\[
u(x)=\frac{a}{\sqrt3}.
\]

Los usos típicos comprenden la resolución, una tolerancia garantizada, una deriva acotada o un efecto ambiental conocido solo entre límites. Debe confirmarse que los límites correspondan a la variable modelada y a las condiciones de uso. Una especificación “±1 % de lectura + 0.5 nmol/mol” no se convierte en único número sin evaluar concentración.

## 3.3 Distribución normal

Para \(X\sim N(\mu,\sigma^2)\):

\[
E(X)=\mu,\qquad u(X)=\sigma.
\]

Se usa cuando la estimación y la incertidumbre estándar están disponibles y la forma normal resulta defendible por la información o el mecanismo. Si el certificado informa \(x\pm U\) con un factor \(k\), la conversión usual es

\[
u(x)=\frac{U}{k},
\]

si el certificado define claramente \(U\), \(k\) y la distribución. No debe dividirse por 2 por costumbre cuando el certificado informa un intervalo, una tolerancia o un límite distinto de la incertidumbre expandida.

## 3.4 Distribución triangular

Para \(X\) con límites \(a\) y \(b\) y máximo de densidad en el centro \((a+b)/2\):

\[
E(X)=\frac{a+b}{2},\qquad
u^2(X)=\frac{(b-a)^2}{24}.
\]

Si la información se expresa como \(x\pm a\), el semiancho es \(a\) y

\[
u(x)=\frac{a}{\sqrt6},
\]

que es menor que el valor de la distribución rectangular, \(a/\sqrt3\), porque los valores centrales son más probables que los extremos.

Su uso está justificado cuando la evidencia o el mecanismo indican que los valores cercanos al centro son más plausibles dentro de límites conocidos: por ejemplo, ante la suma de dos efectos rectangulares comparables o una repetibilidad publicada con esa PDF en un presupuesto de referencia. No se elige una distribución triangular para obtener un número menor; se elige cuando el conocimiento respalda un mayor peso central. Ante la duda entre una distribución rectangular y una triangular, la rectangular es la opción menos informativa compatible únicamente con los límites.

El muestreo puede realizarse con \(U_1,U_2\sim R(0,1)\) independientes:

\[
X=a+\frac{b-a}{2}\,(U_1+U_2).
\]

## 3.5 Distribución t desplazada y escalada

Para la información Tipo A con pocos grados de libertad, puede asignarse

\[
X=x_0+s_0T_\nu.
\]

Los parámetros \(x_0\), \(s_0\) y \(\nu\) deben conservarse. \(s_0\) es un parámetro de escala, no una desviación estándar. Para \(\nu>2\), la incertidumbre estándar es \(u(X)=s_0\sqrt{\nu/(\nu-2)}\), y la conversión inversa es \(s_0=u(X)\sqrt{(\nu-2)/\nu}\). La distribución tiene colas más pesadas que la normal. Su media existe para \(\nu>1\) y varianza para \(\nu>2\).

El procedimiento de muestreo estándar, claro y validable, es el siguiente:

1. Generar \(Z\sim N(0,1)\).
2. Generar \(W\sim\chi^2(\nu)\), que sea independiente de \(Z\).
3. Calcular

\[
T_\nu=\frac{Z}{\sqrt{W/\nu}};
\]

4. Transformar el resultado mediante \(X=x_0+s_0T_\nu\).

Este método sustituye algoritmos de aceptación-rechazo dudosos o incompletos. En el software científico, debe preferirse una implementación probada de una biblioteca estadística.

## 3.6 Distribución arcoseno o en U

Si la variable sigue un ciclo sinusoidal entre \(a\) y \(b\) y la fase de observación es uniforme, la PDF es

\[
g(x)=\frac{1}{\pi\sqrt{(x-a)(b-x)}},\qquad a<x<b.
\]

Los momentos son:

\[
E(X)=\frac{a+b}{2},\qquad
u^2(X)=\frac{(b-a)^2}{8}.
\]

Para \(x_0\pm a\), \(u=a/\sqrt2\), que es mayor que el valor de la distribución rectangular, \(a/\sqrt3\), porque los valores cercanos a los extremos son más probables. Un ejemplo válido exige evidencia de un ciclo aproximadamente sinusoidal y una fase no controlada, como una oscilación térmica estable. No debe asignarse una distribución arcoseno solo porque los datos “suben y bajan”.

El muestreo puede realizarse con \(U\sim R(0,1)\):

\[
X=\frac{a+b}{2}+\frac{b-a}{2}\sin\left[2\pi\left(U-\frac12\right)\right].
\]

## 3.7 Trapecio curvilíneo para límites inexactos

Cuando los límites inferior y superior de un intervalo rectangular no se conocen exactamente, puede modelarse la distribución obtenida al promediar distribuciones rectangulares cuyos límites tienen incertidumbre. Para la construcción específica usada en JCGM 101, con límites centrales \(a,b\) y una inexactitud simétrica parametrizada por \(d\), la forma curvilínea tiene

\[
E(X)=\frac{a+b}{2},\qquad
u^2(X)=\frac{(b-a)^2}{12}+\frac{d^2}{9}.
\]

El segundo término representa el desconocimiento adicional de los límites bajo esa construcción concreta. El parámetro \(d\) no es un semiancho genérico reutilizable con cualquier modelo de límites. Debe usarse solo cuando los supuestos definidos en la implementación de JCGM 101 coincidan con la información disponible. Como JCGM 101 no está en el corpus local, no se cita una cláusula ni se pretende derivar aquí la fórmula. El redondeo digital ordinario con un paso conocido suele requerir una distribución rectangular, no un trapecio curvilíneo.

## 3.8 Ejemplo Tipo B con especificación genérica

Suponga un ejemplo didáctico con una especificación de cero de ±0.4 nmol/mol, sin información adicional. Un ensayo independiente muestra el efecto térmico residual \(\Delta_T=A\sin\Phi\), con una amplitud \(A=0.8\) nmol/mol. El instante de medición no está sincronizado con el ciclo, por lo que la fase se modela como \(\Phi\sim R(0,2\pi)\).

- Cero, rectangular: \(u_0=0.4/\sqrt3=0.231\) nmol/mol.
- Efecto térmico sinusoidal, arcoseno: \(u_T=A/\sqrt2=0.566\) nmol/mol.

Si ambos efectos son independientes y entran aditivamente, la contribución combinada parcial es

\[
\sqrt{0.231^2+0.566^2}=0.611\ \text{nmol/mol}.
\]

La conclusión depende de las PDFs justificadas. Asignar una distribución rectangular a ambos efectos daría 0.516 nmol/mol; la diferencia no proviene de un “método conservador”, sino de un conocimiento distinto sobre los mecanismos.

---

# 4. Propagación mediante marco GUM clásico (GUF)

## 4.1 Coeficientes de sensibilidad

Para el modelo \(Y=f(X_1,\ldots,X_N)\), el coeficiente de sensibilidad de la entrada \(X_i\) es

\[
c_i=\left.\frac{\partial f}{\partial X_i}\right|_{x_1,\ldots,x_N}.
\]

La contribución estándar es

\[
u_i(y)=|c_i|u(x_i).
\]

El coeficiente convierte la unidad de la entrada en la unidad de salida. También muestra cuán sensible es el resultado a cambios pequeños. Puede calcularse analíticamente o mediante una diferencia numérica controlada. La derivada numérica debe probar su estabilidad frente al tamaño del paso.

Para el modelo simplificado de Beer–Lambert, si \(x\propto T/(\sigma LP)\), las sensibilidades relativas son

\[
\frac{c_T}{x}=\frac{1}{T},\quad
\frac{c_P}{x}=-\frac{1}{P},\quad
\frac{c_L}{x}=-\frac{1}{L},\quad
\frac{c_\sigma}{x}=-\frac{1}{\sigma}.
\]

Por tanto, para entradas independientes y parte multiplicativa,

\[
\left(\frac{u_c(x)}{x}\right)^2
\approx
\left(\frac{u(T)}{T}\right)^2+
\left(\frac{u(P)}{P}\right)^2+
\left(\frac{u(L)}{L}\right)^2+
\left(\frac{u(\sigma)}{\sigma}\right)^2+
\cdots.
\]

El término de transmitancia requiere la derivada de \(\ln D\) y puede dominar cerca de \(D=1\), lo que corresponde a una baja absorción.

## 4.2 Ley de propagación de incertidumbre

Para las entradas independientes, se aplica:

\[
u_c^2(y)=\sum_{i=1}^{N}c_i^2u^2(x_i).
\]

Para las entradas correlacionadas, se aplica la siguiente expresión (JCGM 100 §5.2):

\[
u_c^2(y)=
\sum_{i=1}^{N}c_i^2u^2(x_i)
+2\sum_{i=1}^{N-1}\sum_{j=i+1}^{N}
c_ic_j u(x_i,x_j),
\]

donde \(u(x_i,x_j)\) es la covarianza. Con coeficiente de correlación \(r_{ij}\):

\[
u(x_i,x_j)=r_{ij}u(x_i)u(x_j).
\]

La forma matricial es:

\[
u_c^2(y)=\mathbf{c}^\mathsf{T}\mathbf{U}_x\mathbf{c}.
\]

La correlación puede aumentar o reducir la incertidumbre, según los signos de la sensibilidad y de la covarianza. No debe fijarse en cero por falta de cálculo si las entradas comparten una calibración, un sensor, una corrección o datos. La falta de información sobre la correlación es un problema del modelo que debe investigarse o tratarse mediante un análisis de sensibilidad.

## 4.3 Doble conteo: GUM §4.3.10

GUM §4.3.10 advierte que debe evitarse contar dos veces el mismo componente. El riesgo aparece al incorporar simultáneamente:

- incertidumbre de certificado y otra especificación ya incluida en ese certificado;
- repetibilidad observada y resolución, cuando resolución ya se manifiesta plenamente en dispersión;
- deriva dentro de periodo de calibración y datos de reproducibilidad que ya incluyen esa deriva;
- incertidumbre de patrón en cada punto y matriz de calibración que ya fue ajustada usando ese patrón;
- una corrección y un efecto residual definidos sobre el mismo fenómeno.

La prevención exige un mapa de las fuentes y el linaje de cada dato. Para cada componente deben responderse tres preguntas:

1. ¿Qué efecto físico representa?
2. ¿Dónde aparece en el modelo?
3. ¿Está contenido total o parcialmente en otra estimación?

Ejemplo: el certificado del patrón informa una incertidumbre expandida que incluye la repetibilidad interna, la presión, la temperatura y la fotometría. El presupuesto de transferencia debe incorporar la incertidumbre certificada como un conjunto, salvo que el certificado permita una desagregación coherente. Agregar nuevamente presión y temperatura internas del patrón duplicaría componentes.

## 4.4 Presupuesto y contribuciones

El presupuesto debe incluir cada entrada, su estimación, la unidad, la PDF o el método, el divisor, la incertidumbre estándar, los grados de libertad, la sensibilidad, la contribución y el origen. La participación en la varianza de un componente independiente es

\[
p_i=100\frac{c_i^2u^2(x_i)}{u_c^2(y)}\ \%.
\]

Con correlaciones, el reparto simple puede ser engañoso porque los términos cruzados no pertenecen exclusivamente a una entrada. Deben informarse por separado o distribuirse con convención explícita.

La clasificación de las contribuciones orienta la mejora. Reducir un componente pequeño no cambia el resultado. Pero un componente omitido no aparece en la clasificación: la revisión física del modelo sigue siendo indispensable.

## 4.5 Welch–Satterthwaite y factor de cobertura

Cuando la incertidumbre combinada depende de componentes con grados de libertad finitos, los grados efectivos se aproximan mediante Welch–Satterthwaite (JCGM 100, Anexo G.4) por

\[
\nu_{\mathrm{eff}}=
\frac{u_c^4(y)}{
\displaystyle\sum_{i=1}^{N}
\frac{u_i^4(y)}{\nu_i}},
\]

para la forma usual con componentes independientes. Los componentes con \(\nu_i=\infty\) aportan cero al denominador. El resultado suele truncarse hacia abajo de manera conservadora al consultar los cuantiles.

Para una probabilidad bilateral \(p\), el factor se obtiene de la distribución \(t\):

\[
k=t_{(1+p)/2,\nu_{\mathrm{eff}}}.
\]

Ejemplo: dos contribuciones independientes, \(u_1=0.50\) nmol/mol con \(\nu_1=9\), y \(u_2=0.30\) nmol/mol con \(\nu_2=\infty\):

\[
u_c=\sqrt{0.50^2+0.30^2}=0.583\ \text{nmol/mol},
\]

\[
\nu_{\mathrm{eff}}=
\frac{0.583^4}{0.50^4/9}\approx16.6.
\]

Para 95 %, \(k\) es cercano a 2.12, no exactamente 2. La incertidumbre expandida es aproximadamente 1.24 nmol/mol.

Welch–Satterthwaite es una aproximación asociada a las condiciones del GUF y a una distribución t efectiva. Si la salida es fuertemente asimétrica o el modelo no es lineal, un intervalo obtenido mediante MCM puede ser más apropiado.

---

# 5. Propagación mediante método de Monte Carlo

## 5.1 Cuándo usar MCM

El MCM propaga las PDFs completas a través del modelo. Resulta preferible cuando:

- el modelo es fuertemente no lineal en la región de incertidumbre;
- las PDFs de entrada o de salida son asimétricas;
- existen límites físicos o truncamientos importantes;
- las incertidumbres son grandes respecto a la escala de no linealidad;
- las derivadas son difíciles de calcular, discontinuas o numéricamente inestables;
- se necesita un intervalo de cobertura no simétrico.

El MCM no es metrológicamente superior por definición. El GUF es válido y eficiente en la mayoría de los casos lineales o aproximadamente lineales, con incertidumbres moderadas y una salida aproximadamente normal o t. La elección depende de la aptitud para el propósito y de la validación.

## 5.2 Procedimiento general

1. Definir el modelo \(Y=f(\mathbf X)\).
2. Asignar la PDF conjunta de las entradas, incluidas sus dependencias.
3. Generar un vector \(\mathbf x_r\) de entradas para cada ensayo \(r\).
4. Evaluar \(y_r=f(\mathbf x_r)\).
5. Repetir el proceso hasta alcanzar la estabilidad numérica requerida.
6. Ordenar \(y_r\) para representar la función de distribución de la salida.
7. Calcular la estimación, la incertidumbre estándar y el intervalo de cobertura.

Para \(M\) valores, la estimación de la salida y la varianza de la PDF de salida son

\[
\hat y=\frac{1}{M}\sum_{r=1}^{M}y_r,
\]

\[
u^2(y)=s_y^2=\frac{1}{M-1}
\sum_{r=1}^{M}(y_r-\hat y)^2.
\]

Esta segunda expresión estima la incertidumbre metrológica asociada a la distribución de salida; no es la incertidumbre numérica de la media de Monte Carlo. Para ensayos independientes, el error estándar numérico de \(\hat y\) es aproximadamente \(s_y/\sqrt M\). Las estadísticas de los extremos requieren una evaluación propia, normalmente por bloques dentro del procedimiento adaptativo. La forma centrada de la varianza debe preferirse a la diferencia entre la media de los cuadrados y el cuadrado de la media, que puede sufrir cancelación numérica.

## 5.3 Muestreo de PDFs

El muestreo debe corresponder a las distribuciones asignadas. JCGM 101 gobierna el caso de una salida; JCGM 102 extiende la propagación a múltiples salidas y conserva las covarianzas entre ellas. El desarrollo de regiones multivariantes queda fuera del alcance de este handout:

- rectangular: transformación lineal de \(U\sim R(0,1)\);
- normal: generador normal validado de biblioteca científica;
- t: \(Z/\sqrt{W/\nu}\), con \(Z\sim N(0,1)\), \(W\sim\chi^2(\nu)\) independientes;
- arcoseno: transformación trigonométrica equivalente;
- distribuciones empíricas: remuestreo o inversión de la CDF, si esta representa la información disponible;
- entradas normales correlacionadas: factorización de Cholesky u otro método matricial estable a partir de una matriz de covarianza válida.

Puede usarse cualquier generador de números pseudoaleatorios validado, con periodo, calidad y reproducibilidad adecuados. Deben registrarse software, versión, algoritmo relevante y, cuando la reproducibilidad lo requiera, la semilla. La calidad del modelo y de las PDFs suele importar más que la elección entre generadores modernos validados.

## 5.4 Procedimiento adaptativo

El número de ensayos no debe fijarse como un requisito universal. JCGM 101 describe un procedimiento adaptativo para alcanzar la tolerancia numérica asociada a las cifras significativas requeridas.

Un esquema práctico es el siguiente:

1. Elegir la probabilidad de cobertura \(p\) y la tolerancia numérica \(\delta\).
2. Ejecutar secuencias o bloques de tamaño suficiente para estimar estabilidad de \(y\), \(u(y)\) y extremos del intervalo.
3. Tras cada conjunto de bloques, calcular dispersión de estimaciones obtenidas entre bloques.
4. Exigir que la incertidumbre numérica de cada magnitud informada sea menor que \(\delta\); el criterio habitual del procedimiento adaptativo usa dos veces la desviación estándar asociada a cada estimación.
5. Aumentar el número de ensayos y repetir el proceso hasta cumplir el criterio simultáneamente para la estimación, la incertidumbre estándar y ambos extremos.

La tolerancia \(\delta\) se liga a la resolución con la que se informará la incertidumbre. Si \(u(y)=0.37\) nmol/mol se informará con dos cifras significativas, la última cifra ocupa las centésimas; una tolerancia numérica del orden de media unidad en la última posición, 0.005 nmol/mol, es razonable. La definición exacta debe seguir el procedimiento de JCGM 101 y la política de redondeo.

La ventaja adaptativa consiste en que usa los ensayos necesarios para el problema. Las distribuciones regulares pueden estabilizarse con menos ensayos; las colas, los cuantiles extremos o los intervalos cortos pueden requerir más. El resultado debe mostrar que el error numérico de la simulación es despreciable frente a la incertidumbre metrológica.

## 5.5 Intervalos de cobertura

Con los valores ordenados

\[
y_{(1)}\le y_{(2)}\le\cdots\le y_{(M)},
\]

el intervalo probabilísticamente simétrico usa cuantiles de colas iguales, aproximadamente \((1-p)/2\) y \((1+p)/2\).

El intervalo de cobertura más corto selecciona, entre todos los intervalos que contienen una fracción \(p\), aquel que tiene la menor anchura. Si \(q\approx pM\), se buscan índices \(r\) que minimicen

\[
y_{(r+q)}-y_{(r)}.
\]

Para una distribución simétrica y unimodal, ambos intervalos suelen ser parecidos. Para una distribución sesgada, el intervalo más corto puede ser claramente asimétrico respecto a la media. El tipo de intervalo debe declararse; los extremos sin un método especificado son ambiguos.

El intervalo más corto no siempre es único, especialmente con distribuciones multimodales o discretas. En tales casos deben informarse el criterio y las limitaciones, y puede ser más útil presentar los cuantiles o la representación completa.

---

# 6. Validación GUF–MCM mediante tolerancia \(\delta\)

## 6.1 Propósito

La validación determina si la aproximación GUF produce un intervalo indistinguible, a la resolución requerida, del obtenido por propagación de distribuciones. No busca declarar un ganador universal.

La aplicación correcta usa el mismo modelo, las mismas estimaciones, incertidumbres, PDFs y correlaciones. Comparar presupuestos diferentes no valida el método; solo compara los supuestos.

## 6.2 Procedimiento

1. Aplicar GUF y obtener estimación \(y_{GUF}\), incertidumbre \(u_{GUF}\), grados efectivos y cobertura de probabilidad \(p\).
2. Formar el intervalo GUF \([y_{GUF}-U_p,\ y_{GUF}+U_p]\), o la aproximación correspondiente.
3. Aplicar un MCM estabilizado con la misma \(p\), obteniendo \([y_{low},y_{high}]\).
4. Definir la tolerancia numérica \(\delta\) según las cifras significativas de la incertidumbre informada.
5. Calcular

\[
d_{low}=\left|(y_{GUF}-U_p)-y_{low}\right|,
\]

\[
d_{high}=\left|(y_{GUF}+U_p)-y_{high}\right|.
\]

6. Considerar validado el GUF para la aplicación y la resolución si

\[
d_{low}\le\delta
\quad\text{y}\quad
d_{high}\le\delta.
\]

Si alguna diferencia excede \(\delta\), GUF no queda validado para ese modelo, esa información y ese criterio de informe. Entonces se informa el resultado del MCM o se mejora la aproximación, por ejemplo con términos de orden superior.

## 6.3 Interpretación

La validación es específica. Un cambio de concentración, de amplitud de las incertidumbres, de calibración, de PDF o de régimen operativo puede alterar la no linealidad. Para Beer–Lambert, el comportamiento cerca de la transmitancia unitaria puede diferir del observado a una mayor absorción. Conviene validar en puntos que cubran el intervalo de uso, no solo en el punto medio.

Una diferencia pequeña entre las incertidumbres estándar no garantiza la igualdad de los intervalos. El MCM puede mostrar un sesgo de salida y asimetría aunque la desviación estándar sea similar. Por eso, la validación usa los extremos de cobertura.

---

# 7. Informe según GUM §7

## 7.1 Contenido mínimo

JCGM 100 §7 exige información suficiente para comprender el resultado y repetir la evaluación cuando sea necesario. La síntesis siguiente combina el contenido de §7 con la organización didáctica de este handout. El informe basado en GUM/GUF debe incluir:

1. la definición completa del mensurando;
2. la estimación \(y\) y su unidad;
3. el modelo de medición y la relación funcional;
4. las correcciones aplicadas y las constantes usadas;
5. las fuentes de incertidumbre y el método Tipo A o Tipo B;
6. los datos, certificados, especificaciones y referencias de origen;
7. las PDFs asignadas, sus parámetros y su justificación;
8. las incertidumbres estándar y los grados de libertad;
9. los coeficientes de sensibilidad y las covarianzas o correlaciones;
10. el método de propagación: GUF, MCM u otro;
11. la incertidumbre estándar combinada;
12. la incertidumbre expandida, el factor de cobertura y la probabilidad, si corresponden;
13. los extremos y el tipo de intervalo de cobertura;
14. las reglas de redondeo;
15. el análisis de la validez del modelo, sus limitaciones y sus condiciones de uso.

Como información adicional requerida para la transparencia de la implementación del MCM, se debe agregar:

- el software y su versión;
- el generador pseudoaleatorio o la biblioteca utilizada;
- el manejo de las dependencias;
- el criterio adaptativo y \(\delta\);
- el número final de ensayos;
- la evidencia de estabilización;
- el método del intervalo: probabilísticamente simétrico o más corto.

## 7.2 Forma de expresar el resultado

Caso aproximadamente simétrico:

> Fracción molar de ozono: \(y=80.4\ \text{nmol/mol}\). Incertidumbre estándar combinada: \(u_c=0.62\ \text{nmol/mol}\). Incertidumbre expandida: \(U=1.3\ \text{nmol/mol}\), con \(k=2.09\), correspondiente a probabilidad de cobertura aproximada de 95 % y \(\nu_{eff}=19\). Resultado: \((80.4\pm1.3)\ \text{nmol/mol}\).

Caso asimétrico MCM:

> Fracción molar de ozono estimada: \(80.5\ \text{nmol/mol}\). Incertidumbre estándar: \(0.65\ \text{nmol/mol}\). Intervalo de cobertura más corto de 95 %: [79.4, 81.9] nmol/mol, obtenido mediante MCM adaptativo con tolerancia numérica \(\delta=0.01\ \text{nmol/mol}\).

No debe escribirse “95 % de confianza” sin aclarar el marco estadístico. En el GUM se habla de una probabilidad de cobertura basada en la información disponible. Tampoco debe informarse \(k=2\) y “95 %” como una equivalencia exacta cuando la distribución o los grados de libertad no la sustentan.

## 7.3 Redondeo

Los cálculos intermedios conservan una precisión suficiente. El redondeo se realiza al final. La práctica habitual es la siguiente:

- informar la incertidumbre con una o dos cifras significativas, según la política y la estabilidad;
- redondear la estimación a la misma posición decimal que la incertidumbre;
- evitar más dígitos de los justificados;
- no redondear los componentes antes de la combinación.

Si la decisión depende de un límite, la regla de decisión y el riesgo deben documentarse por separado. La incertidumbre no sustituye el criterio de conformidad.

## 7.4 Lista de comprobación

Antes de aprobar el informe:

- ¿El mensurando está especificado sin ambigüedad?
- ¿El modelo representa la operación real y las etapas de transferencia?
- ¿Los efectos conocidos se corrigieron cuando correspondía?
- ¿Los datos Tipo A son estables e independientes, o se trató la autocorrelación?
- ¿Las PDFs Tipo B corresponden a la información disponible?
- ¿Se incluyeron las correlaciones por fuentes compartidas?
- ¿Se evitó el doble conteo según GUM §4.3.10?
- ¿El factor de cobertura corresponde a los grados y a la distribución?
- ¿El MCM, si se usó, alcanzó la tolerancia adaptativa?
- ¿Están declarados el intervalo y la probabilidad?
- ¿La trazabilidad y las fuentes pueden auditarse?

---

# 8. Glosario breve

**Autocorrelación:** la dependencia estadística entre los valores de una misma serie separados por uno o más retardos.

**Coeficiente de correlación \(r_{ij}\):** la covarianza normalizada entre dos entradas; toma valores entre −1 y 1.

**Coeficiente de sensibilidad \(c_i\):** la derivada de la salida respecto a una entrada; convierte la incertidumbre de la entrada en una contribución expresada en la unidad de salida.

**Corrección:** la compensación aplicada por un efecto sistemático estimado. La corrección también tiene incertidumbre.

**Covarianza:** una medida de la variación conjunta de dos magnitudes; en metrología, también se denomina incertidumbre mutua.

**Error de medición:** la diferencia entre el valor medido y el valor de referencia; no equivale a la incertidumbre.

**Evaluación Tipo A:** la evaluación de un componente de incertidumbre mediante el análisis estadístico de los valores medidos.

**Evaluación Tipo B:** la evaluación mediante información distinta del análisis estadístico de las series actuales.

**Factor de cobertura \(k\):** el número por el que se multiplica la incertidumbre estándar combinada para obtener la incertidumbre expandida.

**GUF:** el marco GUM clásico basado normalmente en una aproximación de Taylor y en la ley de propagación de la incertidumbre.

**Incertidumbre expandida \(U\):** el producto de la incertidumbre estándar combinada por el factor de cobertura.

**Incertidumbre estándar:** la incertidumbre expresada como una desviación estándar.

**Intervalo de cobertura:** el intervalo que contiene los valores atribuidos al mensurando con una probabilidad declarada.

**MCM:** el método de Monte Carlo, que consiste en la propagación numérica de las PDFs de entrada mediante el muestreo y la evaluación repetida del modelo.

**Mensurando:** la magnitud que se desea medir.

**Modelo de medición:** la relación matemática entre la magnitud de salida y las entradas.

**PDF:** la función de densidad de probabilidad que representa el conocimiento sobre los valores de una magnitud continua.

**Probabilidad de cobertura:** la probabilidad de que el valor de una magnitud esté dentro de un intervalo especificado, basada en la información disponible.

**Tamaño efectivo de muestra \(n_{eff}\):** el número de observaciones independientes equivalente a una serie posiblemente autocorrelacionada.

**Trazabilidad metrológica:** la propiedad de un resultado por la cual este puede relacionarse con una referencia mediante una cadena documentada e ininterrumpida de calibraciones, cada una con una contribución a la incertidumbre.

**Welch–Satterthwaite:** una aproximación para calcular los grados efectivos de libertad de la incertidumbre combinada.

---

# Referencias

1. Joint Committee for Guides in Metrology (JCGM). **JCGM GUM-1:2023, Guide to the expression of uncertainty in measurement — Part 1: Introduction.** First edition, 2023.
2. Joint Committee for Guides in Metrology (JCGM). **JCGM GUM-6:2020, Guide to the expression of uncertainty in measurement — Part 6: Developing and using measurement models.** First edition, 2020.
3. Joint Committee for Guides in Metrology (JCGM). **JCGM 100:2008, Evaluation of measurement data — Guide to the expression of uncertainty in measurement.** First edition, September 2008; corrected version 2010. También publicado como ISO/IEC Guide 98-3:2008.
4. Joint Committee for Guides in Metrology (JCGM). **JCGM 101:2008, Evaluation of measurement data — Supplement 1 to the “Guide to the expression of uncertainty in measurement” — Propagation of distributions using a Monte Carlo method.** First edition, 2008. Documento citado para MCM; no disponible en corpus local suministrado. Por esa razón, este handout evita atribuir numerales específicos no comprobados.
5. Joint Committee for Guides in Metrology (JCGM). **JCGM 102:2011, Evaluation of measurement data — Supplement 2 to the “Guide to the expression of uncertainty in measurement” — Extension to any number of output quantities.** First edition, 2011. También publicado como ISO/IEC Guide 98-3/Suppl.2:2011.
