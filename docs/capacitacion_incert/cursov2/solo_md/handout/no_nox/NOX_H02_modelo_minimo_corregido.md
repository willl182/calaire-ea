## 2 Modelo mínimo y corregido

\[
c_{NO_2}=c_{NO_x}-c_{NO},
\qquad
c_{NO_2}=\frac{c_{NO_x}-c_{NO}}{\eta_c}.
\]

Usar segunda expresión solo cuando arquitectura y software no hayan aplicado corrección. Confirmar definición de salidas y ruta de calibración.

Coeficientes:

\[
\frac{\partial c_{NO_2}}{\partial c_{NO_x}}=\frac1\eta,
\quad
\frac{\partial c_{NO_2}}{\partial c_{NO}}=-\frac1\eta,
\quad
\frac{\partial c_{NO_2}}{\partial\eta}=-\frac{c_{NO_x}-c_{NO}}{\eta^2}.
\]

Con covarianza:

\[
u^2(c_{NO_2})=\frac{u^2(NO_x)+u^2(NO)-2\operatorname{cov}(NO_x,NO)}{\eta^2}
+\left(\frac{NO_x-NO}{\eta^2}\right)^2u^2(\eta).
\]

Fuentes comunes pueden generar correlación. En diferencia, correlación positiva puede reducir incertidumbre; debe justificarse.
