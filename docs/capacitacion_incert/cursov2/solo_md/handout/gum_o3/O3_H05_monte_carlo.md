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
