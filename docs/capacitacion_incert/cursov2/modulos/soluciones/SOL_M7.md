# Solución M7 — Taller integrador: presupuesto y reporte de incertidumbre

## 1. Alcance, mensurando y modelo

El mensurando es la **fracción de cantidad de ozono en aire seco atribuida a KRISS-SRP5 al compararla, antes del transporte, con BIPM-SRP27 para un valor asignado de 100 nmol mol⁻¹**, expresada en nmol mol⁻¹.

Modelo publicado:

\[
y=a_0+a_1x.
\]

Datos:

- \(x=100\ \mathrm{nmol\ mol^{-1}}\);
- \(a_0=0.41\ \mathrm{nmol\ mol^{-1}}\), \(u(a_0)=0.28\ \mathrm{nmol\ mol^{-1}}\);
- \(a_1=0.9971\), \(u(a_1)=0.0046\);
- \(\operatorname{cov}(a_0,a_1)=-3.47\times10^{-4}\ \mathrm{nmol\ mol^{-1}}\);
- \(c_x=a_1\), \(c_{a_0}=1\), \(c_{a_1}=x\).

Fuentes: KRISS report, §14.1, ecuaciones 9–10, p. 9; BIPM.QM-K1 protocol v2.1, App. 1, ecuación 14, p. 23.

## 2. Presupuesto fotométrico de BIPM-SRP27

La expresión publicada es

\[
u(x)=\sqrt{0.28^2+(2.92\times10^{-3}x)^2}\ \mathrm{nmol\ mol^{-1}}.
\]

Para \(x=100\ \mathrm{nmol\ mol^{-1}}\):

\[
\begin{aligned}
u(x)&=\sqrt{0.28^2+(0.00292\times100)^2}\\
&=\sqrt{0.078400+0.085264}\\
&=0.404554\ \mathrm{nmol\ mol^{-1}}.
\end{aligned}
\]

El término constante procede principalmente del cociente de intensidades \(D\). Las contribuciones relativas de longitud óptica, presión y temperatura crecen con \(x\). La incertidumbre de la sección eficaz común se fija en cero para esta comparación entre fotómetros que emplean el mismo valor convencional; no es cero en todo presupuesto fotométrico posible.

## 3. Presupuesto completado

Estimación:

\[
y=0.41+0.9971(100)=100.120\ \mathrm{nmol\ mol^{-1}}.
\]

Propagación:

\[
u_c^2(y)=a_1^2u^2(x)+u^2(a_0)+x^2u^2(a_1)+2x\operatorname{cov}(a_0,a_1).
\]

| Componente | Origen | Estimación | \(u\) estándar | \(c_i\) | Contribución o término en \(u_c^2\) |
|---|---|---:|---:|---:|---:|
| Valor \(x\) | BIPM App. 1, ec. 14 | 100 nmol mol⁻¹ | 0.404554 nmol mol⁻¹ | 0.9971 | 0.162716 |
| Intercepto \(a_0\) | KRISS §14.1 | 0.41 nmol mol⁻¹ | 0.28 nmol mol⁻¹ | 1 | 0.078400 |
| Pendiente \(a_1\) | KRISS §14.1 | 0.9971 | 0.0046 | 100 nmol mol⁻¹ | 0.211600 |
| Covarianza \(a_0,a_1\) | KRISS §14.1 | \(-3.47\times10^{-4}\) nmol mol⁻¹ | no aplica | \(2x\) | −0.069400 |
| **Combinación** | modelo | 100.120 nmol mol⁻¹ | — | — | **0.383316** |

Comprobación numérica:

\[
\begin{aligned}
u_c^2(y)
&=(0.9971)^2(0.404554)^2+(0.28)^2+(100\times0.0046)^2\\
&\quad+2(100)(-3.47\times10^{-4})\\
&=0.162716+0.078400+0.211600-0.069400\\
&=0.383316\ (\mathrm{nmol\ mol^{-1}})^2,
\end{aligned}
\]

\[
u_c(y)=\sqrt{0.383316}=0.619125\ \mathrm{nmol\ mol^{-1}}.
\]

La mayor contribución positiva a la varianza es la asociada a la pendiente \(a_1\). La covarianza negativa reduce la varianza combinada en \(0.069400\ (\mathrm{nmol\ mol^{-1}})^2\); conservar su signo es indispensable.

## 4. Incertidumbre expandida y reporte

Para el ejercicio obligatorio se usa

\[
k=2,
\]

como aproximación convencional a una cobertura de aproximadamente 95 %. La elección es explícita porque las fuentes utilizadas no proporcionan grados de libertad documentados para todas las entradas y el objetivo del taller es construir e interpretar el presupuesto. No debe presentarse \(k=2\) como factor publicado por KRISS o BIPM.

\[
U=ku_c(y)=2(0.619125)=1.23825\ \mathrm{nmol\ mol^{-1}}.
\]

Con redondeo final:

\[
y=(100.12\pm1.24)\ \mathrm{nmol\ mol^{-1}},
\]

con \(u_c=0.619\ \mathrm{nmol\ mol^{-1}}\), \(k=2\), \(U=1.24\ \mathrm{nmol\ mol^{-1}}\) y cobertura aproximada de 95 % bajo la convención declarada.

### Declaración conforme a GUM §7

La fracción de cantidad de ozono en aire seco atribuida a KRISS-SRP5 al compararla, antes del transporte, con BIPM-SRP27 para un valor asignado de \(100\ \mathrm{nmol\ mol^{-1}}\) fue \(y=100.12\ \mathrm{nmol\ mol^{-1}}\). El resultado se obtuvo mediante el modelo \(y=a_0+a_1x\), con los parámetros de la regresión previa publicados por KRISS y la incertidumbre de \(x\) del presupuesto fotométrico de BIPM-SRP27. La incertidumbre estándar combinada fue \(u_c=0.619\ \mathrm{nmol\ mol^{-1}}\), incluida la covarianza publicada \(\operatorname{cov}(a_0,a_1)=-3.47\times10^{-4}\ \mathrm{nmol\ mol^{-1}}\). La incertidumbre expandida fue \(U=1.24\ \mathrm{nmol\ mol^{-1}}\), obtenida con \(k=2\), para una cobertura aproximada de 95 % bajo la convención declarada. El resultado se expresa como \((100.12\pm1.24)\ \mathrm{nmol\ mol^{-1}}\), donde el valor después de ± es la incertidumbre expandida. Los parámetros y la covarianza proceden del informe KRISS, §14.1, ecuaciones 9–10, p. 9; \(u(x)\) procede del protocolo BIPM.QM-K1 v2.1, App. 1, ecuación 14, p. 23.

## 5. Material avanzado opcional: Welch–Satterthwaite

Welch–Satterthwaite no forma parte del ejercicio obligatorio. Puede estudiarse con JCGM 100:2008, Anexo G.4, y `handout_teorico_gum_o3.md`, §4.5, cuando se disponga de grados de libertad sustentados para las contribuciones relevantes. No corresponde inventar grados de libertad para reproducir una selección de \(k\); si una aplicación exige una cobertura más rigurosa, deben documentarse la información estadística, el cálculo de \(\nu_{eff}\) y el cuantil utilizado.

## 6. Validación externa, alcance y transferencia a NOx

### Validación externa propuesta

Respuesta válida: repetir comparación después del transporte y contrastar diferencia observada con incertidumbre declarada; usar serie QC histórica bajo condiciones representativas; comparar contra otra SRP o patrón independiente; o repetir evaluación en segundo nivel. Dato debe ser independiente de entradas ya usadas y cubrir condiciones pertinentes. Concordancia razonable apoya orden de magnitud; no prueba presupuesto completo por sí sola.

### Alcance

Ejemplo: “Resultado aplica a comparación previa al transporte entre KRISS-SRP5 y BIPM-SRP27, a 100 nmol mol⁻¹, bajo modelo y condiciones documentados; no representa por sí solo incertidumbre de medición de estación, línea de muestreo ni otros niveles.”

### Transferencia a NOx

Respuesta modelo, 45 palabras: “Mensurando: fracción molar de NO₂ calculada en aire de muestra mediante \(c_{NO_2}=(c_{NO_x}-c_{NO})/\eta_c\). Canales NO y NOx comparten calibración y pueden estar correlacionados. Validación externa: GPT independiente o comparación con método selectivo, bajo condiciones representativas de línea y convertidor.”

Debe reconocerse covarianza como término cruzado, incertidumbre de eficiencia y riesgo de doble corrección si software ya aplica \(\eta_c\).

## 7. Rúbrica corta

| Criterio | Puntaje |
|---|---:|
| Define mensurando, unidad, nivel, alcance y modelo | 1.5 |
| Calcula \(u(x)\) y completa celdas sin doble conteo | 1.5 |
| Propaga \(a_0\), \(a_1\), \(u(x)\) y covarianza con signo | 2.0 |
| Calcula \(u_c\), aplica \(k=2\), obtiene \(U\) y redondea | 1.5 |
| Presenta reporte coherente con GUM §7 y QUAM cap. 9 | 1.5 |
| Propone validación externa pertinente | 1.0 |
| Transfiere método a NOx: mensurando, dependencia y validación | 1.0 |
| **Total** | **10** |

## 8. Errores esperables y cierre

- Clasificar una fuente como Tipo A o Tipo B únicamente por su distribución.
- Llamar al mensurando solo “concentración” o cambiar de unidad sin documentarlo.
- Sumar \(0.28\) y \(2.92\times10^{-3}x\) linealmente.
- Usar la expresión resumida de \(u(x)\) y volver a agregar \(L_{opt}\), \(P\), \(T\) y \(D\).
- Incluir la incertidumbre de \(\sigma\) aunque ambos fotómetros usan el mismo valor convencional, o afirmar que siempre es cero.
- Eliminar el signo negativo de la covarianza o tratarla como incertidumbre independiente.
- Omitir \(u(x)\) y calcular solo la incertidumbre de la recta condicionada a un \(x\) exacto.
- Atribuir \(k=2\) al protocolo BIPM o al informe KRISS.
- Afirmar que \(k=2\) resulta de Welch–Satterthwaite sin calcular grados efectivos sustentados.
- Redondear contribuciones antes de terminar la combinación.
- Informar únicamente \(U\) sin \(u_c\), \(k\), cobertura, modelo y fuentes.

El cierre conecta mensurando, fotometría UV, SRP, propagación, covarianza y reporte. La secuencia transferible es: definir, modelar, documentar, propagar, revisar, interpretar y reportar.
