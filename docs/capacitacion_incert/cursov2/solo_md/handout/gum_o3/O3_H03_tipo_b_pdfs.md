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
