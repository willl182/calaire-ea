# M5 — Página 03 — Bloque 18–28 min — Corrección por certificado, regresión y residuos.

- **Sesión:** M5
- **Fuente:** [`modulos/M5_patrones_transferencia.md`](../modulos/M5_patrones_transferencia.md)
- **Tipo:** página/diapositiva del libreto

## Libreto

**Bloque 18–28 min — Corrección por certificado, regresión y residuos.**

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

**Apoyo en el handout:** ver *Handout teórico GUM–O₃*, §2.1 — Media, desviación estándar e incertidumbre de la media, para interpretar la dispersión de los residuos, y §2.4 — Autocorrelación y tamaño de muestra efectivo, si las lecturas por punto proceden de series promediadas.

P1016Y93 describe el ajuste así: “an ordinary least squares linear regression line is fitted to data from all concentration test points to predict the measurement from the candidate transfer standard as a simple linear function of the measurement from the standard of higher authority” (P1016Y93, App. A, §A3, p. física 61). Aclare que la regresión del ejercicio sigue ese procedimiento. Una evaluación metrológica más amplia puede requerir incertidumbre en ambos ejes y covarianzas compartidas.

QUAM App. E.4 señala que la incertidumbre de una concentración predicha depende de dispersión residual, pendiente, número de réplicas, número de puntos y posición respecto del centro de calibración. \(R^2\) no cuantifica por sí solo incertidumbre. OLS presupone una estructura de errores que debe declararse; si el eje de referencia posee incertidumbre relevante puede requerirse otro modelo (QUAM App. E.4, pp. editoriales 115–116; PDF pp. 121–122).

Distinga cobertura: el residual informa falta de ajuste y precisión local; la dispersión de pendientes e interceptos entre ciclos informa estabilidad corta de la función; y la incertidumbre del valor de referencia no queda incluida automáticamente en el residual.

No use el coeficiente de determinación como única prueba. Una relación casi perfectamente lineal puede conservar una pendiente inaceptable, un intercepto importante o diferencias por punto fuera del límite. La decisión se toma con todos los requisitos declarados.
