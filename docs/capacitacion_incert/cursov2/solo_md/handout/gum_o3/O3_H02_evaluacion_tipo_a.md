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
