# 4. Propagación mediante marco GUM clásico (GUF)

## 4.1 Coeficientes de sensibilidad {#gum-coef-sensibilidad}

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

## 4.2 Ley de propagación de incertidumbre {#gum-ley-propagacion}

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

## 4.3 Doble conteo: GUM §4.3.10 {#gum-doble-conteo}

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

## 4.4 Presupuesto y contribuciones {#gum-presupuesto-contribuciones}

El presupuesto debe incluir cada entrada, su estimación, la unidad, la PDF o el método, el divisor, la incertidumbre estándar, los grados de libertad, la sensibilidad, la contribución y el origen. La participación en la varianza de un componente independiente es

\[
p_i=100\frac{c_i^2u^2(x_i)}{u_c^2(y)}\ \%.
\]

Con correlaciones, el reparto simple puede ser engañoso porque los términos cruzados no pertenecen exclusivamente a una entrada. Deben informarse por separado o distribuirse con convención explícita.

La clasificación de las contribuciones orienta la mejora. Reducir un componente pequeño no cambia el resultado. Pero un componente omitido no aparece en la clasificación: la revisión física del modelo sigue siendo indispensable.

## 4.5 Welch–Satterthwaite y factor de cobertura {#gum-welch-satterthwaite}

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
