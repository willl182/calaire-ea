# 6. Validación GUF–MCM mediante tolerancia \(\delta\) {#gum-validacion-guf-mcm}

## 6.1 Propósito {#gum-validacion-proposito}

La validación determina si la aproximación GUF produce un intervalo indistinguible, a la resolución requerida, del obtenido por propagación de distribuciones. No busca declarar un ganador universal.

La aplicación correcta usa el mismo modelo, las mismas estimaciones, incertidumbres, PDFs y correlaciones. Comparar presupuestos diferentes no valida el método; solo compara los supuestos.

## 6.2 Procedimiento {#gum-validacion-procedimiento}

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

## 6.3 Interpretación {#gum-validacion-interpretacion}

La validación es específica. Un cambio de concentración, de amplitud de las incertidumbres, de calibración, de PDF o de régimen operativo puede alterar la no linealidad. Para Beer–Lambert, el comportamiento cerca de la transmitancia unitaria puede diferir del observado a una mayor absorción. Conviene validar en puntos que cubran el intervalo de uso, no solo en el punto medio.

Una diferencia pequeña entre las incertidumbres estándar no garantiza la igualdad de los intervalos. El MCM puede mostrar un sesgo de salida y asimetría aunque la desviación estándar sea similar. Por eso, la validación usa los extremos de cobertura.

---
