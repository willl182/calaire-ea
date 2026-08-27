# M6 — Página 02 — 3.2 Modelo, convertidor y covarianza — 0:12 a 0:27; acumulado 0:27 (15 min)

- **Sesión:** M6
- **Fuente:** [`modulos/M6_no_nox_quimioluminiscencia.md`](../modulos/M6_no_nox_quimioluminiscencia.md)
- **Tipo:** página/diapositiva del libreto

## Libreto

### 3.2 Modelo, convertidor y covarianza — 0:12 a 0:27; acumulado 0:27 (15 min)

Modelo mínimo:

\[
c_{NO_2}=c_{NO_x}-c_{NO}.
\]

Modelo didáctico corregido:

\[
c_{NO_2}=\frac{c_{NO_x}-c_{NO}}{\eta_c}.
\]

Antes de aplicarlo, verificar arquitectura y software: si instrumento ya corrige eficiencia, dividir otra vez genera doble corrección.

Coeficientes de sensibilidad:

\[
c_{NO_x}=1/\eta_c,\quad c_{NO}=-1/\eta_c,\quad
c_{\eta}=-\frac{c_{NO_x}-c_{NO}}{\eta_c^2}.
\]

Propagación:

\[
u^2(c_{NO_2})=\frac{u^2(c_{NO_x})+u^2(c_{NO})-2\operatorname{cov}(c_{NO_x},c_{NO})}{\eta_c^2}
+\left(\frac{c_{NO_x}-c_{NO}}{\eta_c^2}\right)^2u^2(\eta_c).
\]

Covarianza positiva reduce varianza de diferencia porque coeficientes de canales tienen signos opuestos. No asumir independencia ni correlación sin evidencia.

- **Eficiencia:** fracción de NO₂ convertida.
- **Selectividad:** capacidad de evitar respuesta por HNO₃, HONO, PAN, NH₃ y otros NOy.
- **Estabilidad:** cambio con temperatura, edad, contaminación y matriz.

EN 14211:2012 distingue capacidad mínima de convertidor, criterio de aprobación y corrección en intervalo intermedio; verificar cláusula y edición aplicables antes de convertir esos valores en regla local. Método EPA de 2002 usa criterio histórico distinto; no mezclar contextos.
