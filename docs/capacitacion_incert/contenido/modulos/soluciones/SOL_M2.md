# SOL_M2 — Sensibilidad de la fracción molar a temperatura y presión

## 1. Enunciado resumido

Para una medición de ozono de \(x=100\ \text{nmol/mol}\), calcular los coeficientes de sensibilidad y las contribuciones estándar debidas a temperatura y presión. Interpretar sus signos y comparar ambas contribuciones después de expresarlas en la unidad del mensurando.

## 2. Solución paso a paso

### 2.1 Modelo y derivadas

El modelo de Beer–Lambert expresado como fracción molar es

\[
x=-\frac{k_B T\ln(D)}{\sigma L P}.
\]

Para derivar respecto de \(T\), se mantienen constantes \(P\), \(D\), \(\sigma\) y \(L\):

\[
\frac{\partial x}{\partial T}
=-\frac{k_B\ln(D)}{\sigma LP}.
\]

Como

\[
x=-\frac{k_BT\ln(D)}{\sigma LP},
\]

se obtiene

\[
c_T=\frac{\partial x}{\partial T}=\frac{x}{T}.
\]

Para derivar respecto de \(P\):

\[
\frac{\partial x}{\partial P}
=\frac{k_BT\ln(D)}{\sigma L P^2}
=-\frac{x}{P}.
\]

Por tanto,

\[
c_P=\frac{\partial x}{\partial P}=-\frac{x}{P}.
\]

### 2.2 Coeficiente de sensibilidad a temperatura

Datos:

\[
x=100\ \text{nmol/mol},\qquad T=298.15\ \text{K}.
\]

Sustitución:

\[
c_T=\frac{x}{T}
=\frac{100\ \text{nmol/mol}}{298.15\ \text{K}}
=0.33540\ \text{nmol mol}^{-1}\text{K}^{-1}.
\]

Redondeando:

\[
\boxed{c_T\approx +0.335\ \text{nmol mol}^{-1}\text{K}^{-1}}.
\]

El signo es positivo: si aumenta \(T\) y los demás inputs permanecen constantes, aumenta proporcionalmente la fracción molar calculada.

### 2.3 Coeficiente de sensibilidad a presión

Datos:

\[
x=100\ \text{nmol/mol},\qquad P=101.325\ \text{kPa}.
\]

Sustitución:

\[
c_P=-\frac{x}{P}
=-\frac{100\ \text{nmol/mol}}{101.325\ \text{kPa}}
=-0.98692\ \text{nmol mol}^{-1}\text{kPa}^{-1}.
\]

Redondeando:

\[
\boxed{c_P\approx -0.987\ \text{nmol mol}^{-1}\text{kPa}^{-1}}.
\]

El signo es negativo: si aumenta \(P\) y los demás inputs permanecen constantes, disminuye la fracción molar calculada porque la presión aparece en el denominador del modelo.

### 2.4 Contribución estándar de temperatura

La contribución se expresa en la unidad del mensurando:

\[
u_T(x)=|c_T|u(T).
\]

Con \(u(T)=0.15\ \text{K}\):

\[
\begin{aligned}
u_T(x)
&=\left|0.33540\ \text{nmol mol}^{-1}\text{K}^{-1}\right|
  (0.15\ \text{K})\\
&=0.05031\ \text{nmol/mol}.
\end{aligned}
\]

Por tanto,

\[
\boxed{u_T(x)\approx0.0503\ \text{nmol/mol}}.
\]

### 2.5 Contribución estándar de presión

\[
u_P(x)=|c_P|u(P).
\]

Con \(u(P)=0.05\ \text{kPa}\):

\[
\begin{aligned}
u_P(x)
&=\left|-0.98692\ \text{nmol mol}^{-1}\text{kPa}^{-1}\right|
  (0.05\ \text{kPa})\\
&=0.04935\ \text{nmol/mol}.
\end{aligned}
\]

Por tanto,

\[
\boxed{u_P(x)\approx0.0494\ \text{nmol/mol}}.
\]

### 2.6 Comparación de magnitudes

La contribución de temperatura es ligeramente mayor:

\[
0.05031-0.04935=0.00096\ \text{nmol/mol}.
\]

La razón entre ambas es

\[
\frac{u_T(x)}{u_P(x)}
=\frac{0.05031}{0.04935}
\approx1.0195.
\]

La contribución de temperatura supera la de presión en aproximadamente

\[
(1.0195-1)\times100\%\approx2.0\%.
\]

Esta diferencia es pequeña para el ejemplo. Ambas contribuciones son, a efectos prácticos, de magnitud similar. Aunque \(|c_P|>|c_T|\), la incertidumbre de presión es menor en su propia unidad; solo después de aplicar cada coeficiente puede hacerse una comparación válida.

## 3. Resultado final

> **Resultado:** \(c_T=+0.335\ \text{nmol mol}^{-1}\text{K}^{-1}\), \(c_P=-0.987\ \text{nmol mol}^{-1}\text{kPa}^{-1}\), \(u_T(x)=0.0503\ \text{nmol/mol}\) y \(u_P(x)=0.0494\ \text{nmol/mol}\). Temperatura produce aumento y presión produce disminución del resultado calculado. Las contribuciones estándar son casi iguales; diferencia de aproximadamente \(0.0010\ \text{nmol/mol}\) no es relevante en este ejemplo.

## 4. Criterios de valoración

### Respuesta completa

- Presenta o deriva correctamente \(c_T=x/T\) y \(c_P=-x/P\).
- Sustituye \(T\) en kelvin y \(P\) como presión absoluta en kilopascales.
- Obtiene valores compatibles con \(+0.335\ \text{nmol mol}^{-1}\text{K}^{-1}\) y \(-0.987\ \text{nmol mol}^{-1}\text{kPa}^{-1}\).
- Calcula \(u_T(x)\approx0.0503\ \text{nmol/mol}\) y \(u_P(x)\approx0.0494\ \text{nmol/mol}\), mostrando cancelación de unidades.
- Explica correctamente ambos signos y concluye que las contribuciones tienen magnitudes similares.

### Respuesta parcial

- Usa fórmulas correctas, pero presenta error aritmético menor, redondeo deficiente o alguna unidad incompleta.
- Calcula bien coeficientes o contribuciones, pero no ambos.
- Identifica cuál contribución es mayor, pero no explica por qué la diferencia es pequeña.
- Omite interpretación de uno de los signos sin alterar los resultados numéricos.

### Respuesta incorrecta

- Usa grados Celsius directamente en el denominador de \(c_T\).
- Trata presión como proporcional positiva y obtiene \(c_P>0\).
- Reporta una «incertidumbre negativa» por conservar el signo de \(c_P\) en la contribución.
- Compara \(u(T)=0.15\ \text{K}\) con \(u(P)=0.05\ \text{kPa}\) sin convertirlas a \(\text{nmol/mol}\).
- Obtiene resultados incompatibles por fórmula, conversión o unidades, sin procedimiento recuperable.

## 5. Errores esperables del participante y notas para el instructor

- Error esperable: usar \(25\ ^\circ\text{C}\) en vez de \(298.15\ \text{K}\). Reforzar que el modelo requiere temperatura termodinámica.
- Error esperable: interpretar signo negativo de \(c_P\) como incertidumbre negativa. Separar dirección de respuesta del modelo y magnitud no negativa de la contribución estándar.
- Error esperable: concluir que presión domina porque \(|c_P|\) es numéricamente mayor. Los coeficientes tienen unidades distintas; comparación válida exige multiplicar por incertidumbres correspondientes.
- Aceptar pequeñas diferencias por redondeo, por ejemplo \(0.050\) y \(0.049\ \text{nmol/mol}\), si procedimiento y unidades son correctos.
- Variante útil: pedir cambios estimados para incrementos positivos \(\Delta T\) y \(\Delta P\). Temperatura debe producir \(\Delta x>0\); presión, \(\Delta x<0\).
- No es necesario combinar \(u_T(x)\) y \(u_P(x)\): ejercicio pide calcular y comparar contribuciones individuales.
