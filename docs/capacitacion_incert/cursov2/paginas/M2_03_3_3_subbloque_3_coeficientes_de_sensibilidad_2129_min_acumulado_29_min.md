# M2 — Página 03 — 3.3 Subbloque 3 — Coeficientes de sensibilidad (21–29 min; acumulado: 29 min)

- **Sesión:** M2
- **Fuente:** [`modulos/M2_modelo_medicion.md`](../modulos/M2_modelo_medicion.md)
- **Tipo:** página/diapositiva del libreto

## Libreto

### 3.3 Subbloque 3 — Coeficientes de sensibilidad (21–29 min; acumulado: 29 min)

**Idea fuerza:** una derivada convierte la incertidumbre de una magnitud de entrada, expresada en su unidad, en una contribución expresada en la unidad del mensurando.

**Guion dictable:** Para el modelo \(x=f(T,P,L,\sigma,D)\), cada coeficiente de sensibilidad es una derivada parcial evaluada a partir de las mejores estimaciones disponibles. Las derivadas son

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

**Apoyo en el handout:** ver Handout teórico, §4.1 — Coeficientes de sensibilidad, donde estas mismas derivadas del modelo de Beer–Lambert están desarrolladas paso a paso.

Los signos tienen interpretación física. \(c_T\) es positivo porque un incremento de temperatura incrementa el valor calculado de \(x\). Los coeficientes de presión, longitud y sección eficaz son negativos porque esas magnitudes dividen la expresión. Como \(0<D<1\), \(\ln D\) es negativo; por ello \(c_D\) también es negativo: una transmitancia mayor representa menor absorción y conduce a una fracción molar menor.

La contribución estándar de una magnitud de entrada \(q_i\) se calcula como

\[
u_i(x)=|c_i|u(q_i).
\]

El signo no debe borrarse del razonamiento, porque permite interpretar la respuesta del modelo y resulta necesario al considerar covarianzas. No obstante, para comparar magnitudes de contribuciones independientes se usa el valor absoluto y, al combinar varianzas, cada contribución aparece al cuadrado.

Las sensibilidades relativas de \(T\), \(P\), \(L\) y \(\sigma\) tienen magnitud uno. Un cambio relativo pequeño de uno por ciento en cualquiera produce, en primera aproximación, un cambio relativo de uno por ciento en \(x\), con el signo correspondiente. La sensibilidad a \(D\) contiene \(1/(D\ln D)\). Cuando \(D\) se aproxima a uno, \(\ln D\) se aproxima a cero y la sensibilidad puede crecer; por eso la resolución y estabilidad del cociente de intensidades adquieren especial importancia a baja absorción.

**Referencia exacta del bloque:** Handout teórico, **§4.1**, coeficientes de sensibilidad. JCGM GUM-6:2020, **§§7.1–7.2, páginas impresas 9–10**, evaluación del modelo y sensibilidades. NISTIR 6963, **§11, páginas impresas 14–15**, ecuaciones y presupuesto de incertidumbre.
