# Solución M7 — Taller integrador: presupuesto y reporte de incertidumbre

## 1. Enunciado resumido, alcance, mensurando y datos

Se deben responder las ocho preguntas dirigidas del extracto, preparar presupuestos auditables para 30 y 500 nmol mol⁻¹, propagar la covarianza entre intercepto y pendiente, aplicar Welch–Satterthwaite simplificado y redactar dos declaraciones conformes a GUM §7.

El mensurando es la **fracción de cantidad de ozono en aire seco atribuida a KRISS-SRP5 al compararla, antes del transporte, con BIPM-SRP27**, expresada en nmol mol⁻¹.

Modelo publicado:

\[
y=a_0+a_1x,
\]

con los valores exactos del extracto:

- \(a_0=0.41\ \mathrm{nmol\ mol^{-1}}\);
- \(u(a_0)=0.28\ \mathrm{nmol\ mol^{-1}}\);
- \(a_1=0.9971\);
- \(u(a_1)=0.0046\);
- \(\operatorname{cov}(a_0,a_1)=-3.47\times10^{-4}\ \mathrm{nmol\ mol^{-1}}\);
- \(c_x=a_1\), \(c_{a_0}=1\) y \(c_{a_1}=x\).

La incertidumbre estándar del valor asignado por BIPM-SRP27 es:

\[
u(x)=\sqrt{0.28^2+(2.92\times10^{-3}x)^2}\ \mathrm{nmol\ mol^{-1}}.
\]

Fuentes: informe KRISS, §14.1, ecuaciones 9–10, p. 9; BIPM.QM-K1 protocol v2.1, App. 1, ecuación 14, p. 23. El escenario \(\nu_{a_1}=2\), con \(\nu=\infty\) para las demás contribuciones, está definido expresamente por el taller; **no es un dato publicado por KRISS o BIPM**.

## 2. Respuestas modelo a las ocho preguntas dirigidas

### 1. ¿Qué fuentes podrían evaluarse como tipo A y cuáles como tipo B?

El informe no publica una clasificación Tipo A/Tipo B; por tanto, la respuesta debe presentarse como una interpretación del **método de evaluación**, no como un dato del informe.

- Las fuentes denominadas *Repeatability* o *Variability* podrían ser Tipo A **si** sus incertidumbres se obtuvieron mediante análisis estadístico de observaciones repetidas.
- La escala de medición, factores de corrección, manómetros, sondas, resolución, diferencias entre celdas, gradientes o sesgos, divergencia y valor convencional de la sección eficaz podrían ser Tipo B **si** se evaluaron mediante certificados, especificaciones, calibraciones previas, límites o conocimiento técnico distinto de una serie estadística actual.
- La forma de distribución no decide la clasificación: una distribución normal no implica por sí sola Tipo A y una rectangular no implica por sí sola Tipo B.
- Sin información adicional sobre cómo se obtuvo cada valor, la clasificación oficial permanece **no reportada**.

### 2. ¿Por qué \(D\) produce un término constante y \(L_{opt}\), \(P\), \(T\) y \(\sigma\) términos proporcionales a \(x\)?

En el modelo fotométrico, la incertidumbre del cociente de intensidades \(D\) se propaga como una contribución absoluta sobre la fracción medida; por ello, la expresión publicada la resume como \(0.28\ \mathrm{nmol\ mol^{-1}}\), independiente de \(x\). En cambio, las incertidumbres relativas de longitud óptica, presión, temperatura y sección eficaz multiplican la fracción medida, de modo que sus contribuciones crecen linealmente con \(x\).

Para BIPM-SRP27, las contribuciones publicadas son:

\[
u_L=2.89\times10^{-3}x,\quad
u_P=3.37\times10^{-4}x,\quad
u_T=2.29\times10^{-4}x,\quad
u_D=0.28.
\]

Al usar el mismo valor convencional de \(\sigma\) en ambos fotómetros, su incertidumbre común se fija en cero para esta comparación; no se afirma que sea cero en el presupuesto completo del método.

### 3. Reconstrucción de \(u(x)\) de BIPM-SRP27 a 30 y 500 nmol mol⁻¹

La combinación de los coeficientes proporcionales publicados es:

\[
\begin{aligned}
b&=\sqrt{(2.89\times10^{-3})^2+(3.37\times10^{-4})^2+(2.29\times10^{-4})^2}\\
 &=\sqrt{8.3521\times10^{-6}+1.13569\times10^{-7}+5.2441\times10^{-8}}\\
 &=2.9186\times10^{-3}\approx2.92\times10^{-3}.
\end{aligned}
\]

A 30 nmol mol⁻¹:

\[
\begin{aligned}
u_L&=0.08670, &u_P&=0.01011, &u_T&=0.00687, &u_D&=0.28000,\\
u(30)&=\sqrt{0.28^2+(0.00292\times30)^2}\\
&=\sqrt{0.078400+0.00767376}\\
&=0.293383\ \mathrm{nmol\ mol^{-1}}.
\end{aligned}
\]

A 500 nmol mol⁻¹:

\[
\begin{aligned}
u_L&=1.4450, &u_P&=0.1685, &u_T&=0.1145, &u_D&=0.2800,\\
u(500)&=\sqrt{0.28^2+(0.00292\times500)^2}\\
&=\sqrt{0.078400+2.131600}\\
&=1.486607\ \mathrm{nmol\ mol^{-1}}.
\end{aligned}
\]

Los términos constante y proporcional son iguales cuando

\[
0.28=0.00292x\Rightarrow x=95.89\ \mathrm{nmol\ mol^{-1}}.
\]

Por debajo de aproximadamente 96 nmol mol⁻¹ domina el término constante; por encima domina el proporcional. Así, a 30 domina \(0.28\), y a 500 domina \(1.46\).

### 4. Repetición para KRISS-SRP5 con término constante de 0.24 nmol mol⁻¹

La expresión publicada es:

\[
u_{\mathrm{KRISS}}(x)=\sqrt{0.24^2+(2.92\times10^{-3}x)^2}.
\]

A 30 nmol mol⁻¹:

\[
u_{\mathrm{KRISS}}(30)=\sqrt{0.057600+0.00767376}=0.255487\ \mathrm{nmol\ mol^{-1}}.
\]

A 500 nmol mol⁻¹:

\[
u_{\mathrm{KRISS}}(500)=\sqrt{0.057600+2.131600}=1.479595\ \mathrm{nmol\ mol^{-1}}.
\]

Comparación práctica:

| Nivel | \(u_{\mathrm{BIPM}}\) | \(u_{\mathrm{KRISS}}\) | Diferencia |
|---:|---:|---:|---:|
| 30 nmol mol⁻¹ | 0.293383 | 0.255487 | 0.037896 nmol mol⁻¹ |
| 500 nmol mol⁻¹ | 1.486607 | 1.479595 | 0.007012 nmol mol⁻¹ |

La reducción del término constante tiene efecto visible en el nivel bajo, pero casi ninguno en el alto porque allí domina el término proporcional común. Para KRISS, la igualdad entre términos ocurre en \(0.24/0.00292=82.19\ \mathrm{nmol\ mol^{-1}}\).

### 5. Consecuencias de ignorar covarianzas entre niveles del mismo fotómetro

El modelo publicado es

\[
u(x_i,x_j)=x_ix_j u_b^2,\qquad u_b=2.92\times10^{-3}.
\]

La covarianza no es cero porque los niveles comparten efectos proporcionales del mismo fotómetro. Por ejemplo, entre 30 y 500 nmol mol⁻¹:

\[
\begin{aligned}
u(x_{30},x_{500})
&=(30)(500)(2.92\times10^{-3})^2\\
&=15000(8.5264\times10^{-6})\\
&=0.127896\ (\mathrm{nmol\ mol^{-1}})^2.
\end{aligned}
\]

Tratar esos puntos como independientes usaría una matriz de covarianza incorrecta. En una regresión generalizada, ello puede modificar las incertidumbres de pendiente e intercepto, su covarianza, los pesos efectivos y los intervalos derivados. No puede afirmarse con los datos del extracto la magnitud ni la dirección exacta del cambio en los parámetros; sí puede afirmarse que las incertidumbres calculadas bajo independencia no representarían el modelo publicado.

### 6. Aplicación de los criterios a los resultados pre y post

**Antes del transporte:**

\[
|a_0|=|0.41|=0.41<2u(a_0)=2(0.28)=0.56,
\]

\[
|1-a_1|=|1-0.9971|=0.0029<2u(a_1)=2(0.0046)=0.0092.
\]

**Después del transporte:**

\[
|a_0|=|-0.03|=0.03<0.56,
\]

\[
|1-a_1|=|1-0.9976|=0.0024<0.0092.
\]

Los cuatro criterios se cumplen. En el sentido específico de los criterios usados por el informe, los interceptos son consistentes con cero y las pendientes con uno; esto respalda su conclusión de acuerdo. No constituye por sí solo una prueba completa de igualdad pre/post.

### 7. ¿El cambio de pendiente de 0.05 % basta para declarar estabilidad?

No por sí solo. La diferencia publicada es

\[
\Delta a_1=0.9976-0.9971=0.0005,
\]

que corresponde aproximadamente a \(0.05\%\). Para evaluar directamente la estabilidad sería deseable calcular

\[
u^2(\Delta a_1)=u^2(a_{1,post})+u^2(a_{1,pre})
-2\operatorname{cov}(a_{1,post},a_{1,pre}),
\]

y comparar \(|\Delta a_1|\) con \(u(\Delta a_1)\) o con una incertidumbre expandida definida. También sería deseable hacer lo mismo para \(\Delta a_0\), examinar residuos y considerar la correlación creada por instrumentos, datos o calibraciones compartidos. El extracto no publica la covarianza pre/post necesaria; por ello no debe inventarse una prueba numérica adicional. La estabilidad aquí se informa como conclusión del informe, apoyada por el cambio pequeño frente a las incertidumbres publicadas.

### 8. Elementos para juzgar trazabilidad y comparabilidad, y vacíos de información

Elementos publicados que permiten una evaluación:

- identificación de BIPM-SRP27 como referencia común y de KRISS-SRP3 como patrón de transferencia;
- secuencia temporal antes–BIPM–después y rango de 0 a 500 nmol mol⁻¹;
- secuencia de niveles, diez mediciones por punto y criterio de aceptación de la serie;
- componentes, distribuciones e incertidumbres estándar de los presupuestos;
- expresiones resumidas de \(u(x)\) y modelo de covarianza entre niveles;
- modelo de regresión, método de mínimos cuadrados generalizados, parámetros, incertidumbres y covarianza \(\operatorname{cov}(a_0,a_1)\);
- criterios usados para juzgar interceptos y pendientes;
- referencias de sección, tabla, ecuación y página.

Elementos no reportados en el extracto para una reproducción independiente completa:

- datos individuales de las mediciones y matriz completa de covarianza usada en los ajustes;
- clasificación oficial Tipo A/Tipo B y grados de libertad de los componentes;
- covarianzas entre los ajustes pre y post necesarias para una prueba cuantitativa de sus diferencias;
- una prueba estadística independiente específica para el cambio pre/post del intercepto;
- información suficiente para reconstruir exactamente todas las decisiones y configuraciones del software OzonE.

Por tanto, el extracto permite seguir el modelo y reproducir los cálculos aquí pedidos, pero no rehacer de manera independiente todo el ajuste original.

## 3. Presupuesto completo a 30 nmol mol⁻¹

La propagación exigida es:

\[
u_c^2(y)=a_1^2u^2(x)+u^2(a_0)+x^2u^2(a_1)+2x\operatorname{cov}(a_0,a_1).
\]

Estimación:

\[
y=0.41+0.9971(30)=30.323\ \mathrm{nmol\ mol^{-1}}.
\]

| Componente | Origen | Estimación | Método | Divisor | \(u\) estándar | \(\nu\) | \(c_i\) | Contribución \(c_iu_i\) | Aporte firmado a \(u_c^2\) | Participación firmada |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| Valor \(x\) | BIPM App. 1, ec. 14 | 30 nmol mol⁻¹ | expresión publicada | 1 | 0.293383 | ∞ | 0.9971 | 0.292532 nmol mol⁻¹ | 0.0855753 | 52.759 % |
| Intercepto \(a_0\) | KRISS §14.1 | 0.41 nmol mol⁻¹ | incertidumbre publicada | 1 | 0.28 | ∞ | 1 | 0.280000 nmol mol⁻¹ | 0.0784000 | 48.336 % |
| Pendiente \(a_1\) | KRISS §14.1 | 0.9971 | incertidumbre publicada | 1 | 0.0046 | 2, didáctico | 30 nmol mol⁻¹ | 0.138000 nmol mol⁻¹ | 0.0190440 | 11.741 % |
| Covarianza \(a_0,a_1\) | KRISS §14.1 | \(-3.47\times10^{-4}\) nmol mol⁻¹ | término cruzado | no aplica | no aplica | no aplica | \(2x\) | no aplica | −0.0208200 | −12.836 % |

Los porcentajes son aportes firmados divididos por la varianza final; la covarianza no es una fuente independiente ni debe adjudicarse por completo a una fila.

Operación completa:

\[
\begin{aligned}
u_c^2(30)
&=(0.9971)^2(0.2933833)^2+0.28^2+(30\times0.0046)^2\\
&\quad+2(30)(-3.47\times10^{-4})\\
&=0.0855753+0.0784000+0.0190440-0.0208200\\
&=0.1621993\ (\mathrm{nmol\ mol^{-1}})^2,
\end{aligned}
\]

\[
u_c(30)=\sqrt{0.1621993}=0.4027397\ \mathrm{nmol\ mol^{-1}}.
\]

Welch–Satterthwaite simplificado, con grados finitos solo para la pendiente:

\[
\begin{aligned}
\nu_{eff}
&=\frac{u_c^4}{[xu(a_1)]^4/\nu_{a_1}}\\
&=\frac{(0.4027397)^4}{(0.138)^4/2}\\
&=145.0813.
\end{aligned}
\]

Se trunca hacia abajo: \(\nu=145\). Para una cobertura bilateral de 95 %:

\[
k=t_{0.975,145}=1.976460,
\]

\[
U=ku_c=(1.976460)(0.4027397)=0.795999\ \mathrm{nmol\ mol^{-1}}.
\]

Resultado redondeado: \((30.32\pm0.80)\ \mathrm{nmol\ mol^{-1}}\).

## 4. Presupuesto completo a 500 nmol mol⁻¹

Estimación:

\[
y=0.41+0.9971(500)=498.960\ \mathrm{nmol\ mol^{-1}}.
\]

| Componente | Origen | Estimación | Método | Divisor | \(u\) estándar | \(\nu\) | \(c_i\) | Contribución \(c_iu_i\) | Aporte firmado a \(u_c^2\) | Participación firmada |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| Valor \(x\) | BIPM App. 1, ec. 14 | 500 nmol mol⁻¹ | expresión publicada | 1 | 1.486607 | ∞ | 0.9971 | 1.482296 nmol mol⁻¹ | 2.1972006 | 30.438 % |
| Intercepto \(a_0\) | KRISS §14.1 | 0.41 nmol mol⁻¹ | incertidumbre publicada | 1 | 0.28 | ∞ | 1 | 0.280000 nmol mol⁻¹ | 0.0784000 | 1.086 % |
| Pendiente \(a_1\) | KRISS §14.1 | 0.9971 | incertidumbre publicada | 1 | 0.0046 | 2, didáctico | 500 nmol mol⁻¹ | 2.300000 nmol mol⁻¹ | 5.2900000 | 73.283 % |
| Covarianza \(a_0,a_1\) | KRISS §14.1 | \(-3.47\times10^{-4}\) nmol mol⁻¹ | término cruzado | no aplica | no aplica | no aplica | \(2x\) | no aplica | −0.3470000 | −4.807 % |

Operación completa:

\[
\begin{aligned}
u_c^2(500)
&=(0.9971)^2(1.4866069)^2+0.28^2+(500\times0.0046)^2\\
&\quad+2(500)(-3.47\times10^{-4})\\
&=2.1972006+0.0784000+5.2900000-0.3470000\\
&=7.2186006\ (\mathrm{nmol\ mol^{-1}})^2,
\end{aligned}
\]

\[
u_c(500)=\sqrt{7.2186006}=2.6867454\ \mathrm{nmol\ mol^{-1}}.
\]

Welch–Satterthwaite simplificado:

\[
\begin{aligned}
\nu_{eff}
&=\frac{(2.6867454)^4}{(2.300000)^4/2}\\
&=3.724129.
\end{aligned}
\]

Se trunca hacia abajo: \(\nu=3\). Para una cobertura bilateral de 95 %:

\[
k=t_{0.975,3}=3.182446,
\]

\[
U=ku_c=(3.182446)(2.6867454)=8.550423\ \mathrm{nmol\ mol^{-1}}.
\]

Resultado redondeado: \((499.0\pm8.6)\ \mathrm{nmol\ mol^{-1}}\). El valor alto de \(k\) proviene del escenario didáctico de grados de libertad y no es un factor publicado por KRISS.

## 5. Código R usado

El siguiente código usa R base, conserva los valores exactos del extracto y aplica la regla de truncamiento indicada en M7:

```r
a0   <- 0.41
u_a0 <- 0.28
a1   <- 0.9971
u_a1 <- 0.0046
cov_a0_a1 <- -3.47e-4

calcular <- function(x) {
  u_x <- sqrt(0.28^2 + (2.92e-3 * x)^2)
  y <- a0 + a1 * x

  var_x   <- (a1 * u_x)^2
  var_a0  <- u_a0^2
  var_a1  <- (x * u_a1)^2
  var_cov <- 2 * x * cov_a0_a1

  var_c <- var_x + var_a0 + var_a1 + var_cov
  u_c <- sqrt(var_c)

  # Escenario didáctico: nu_a1 = 2; las demás contribuciones, Inf.
  nu_eff <- u_c^4 / ((x * u_a1)^4 / 2)
  nu_usado <- floor(nu_eff)
  k <- qt(0.975, df = nu_usado)
  U <- k * u_c

  data.frame(
    x = x, u_x = u_x, y = y,
    var_x = var_x, var_a0 = var_a0,
    var_a1 = var_a1, var_cov = var_cov,
    var_c = var_c, u_c = u_c,
    nu_eff = nu_eff, nu_usado = nu_usado,
    k = k, U = U
  )
}

resultados <- rbind(calcular(30), calcular(500))
print(resultados, digits = 10)

# Pregunta 4: presupuesto publicado de KRISS-SRP5
u_kriss <- function(x) sqrt(0.24^2 + (2.92e-3 * x)^2)
u_kriss(c(30, 500))

# Ejemplo de covarianza entre niveles, pregunta 5
30 * 500 * (2.92e-3)^2
```

Resultados principales del código:

| \(x\) | \(u(x)\) | \(y\) | \(u_c(y)\) | \(\nu_{eff}\) | \(\nu\) usado | \(k\) | \(U\) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 30 | 0.2933833 | 30.323 | 0.4027397 | 145.0813 | 145 | 1.976460 | 0.7959987 |
| 500 | 1.4866069 | 498.960 | 2.6867454 | 3.724129 | 3 | 3.182446 | 8.5504228 |

## 6. Resultado final y declaraciones conforme a GUM §7

Resultados finales:

- 30 nmol mol⁻¹: \(y=(30.32\pm0.80)\ \mathrm{nmol\ mol^{-1}}\), con \(u_c=0.403\ \mathrm{nmol\ mol^{-1}}\), \(\nu_{eff}=145.081\), \(\nu=145\), \(k=1.976\) y cobertura bilateral aproximada de 95 %.
- 500 nmol mol⁻¹: \(y=(499.0\pm8.6)\ \mathrm{nmol\ mol^{-1}}\), con \(u_c=2.687\ \mathrm{nmol\ mol^{-1}}\), \(\nu_{eff}=3.724\), \(\nu=3\), \(k=3.182\) y cobertura bilateral aproximada de 95 %.

En ambos resultados, valor después de ± es incertidumbre expandida. Grados de libertad de \(u(a_1)\) pertenecen al escenario didáctico.

### Declaraciones conforme a GUM §7

### Nivel de 30 nmol mol⁻¹

La fracción de cantidad de ozono en aire seco atribuida a KRISS-SRP5 al compararla, antes del transporte, con BIPM-SRP27 en el nivel asignado de 30 nmol mol⁻¹ fue \(y=30.32\ \mathrm{nmol\ mol^{-1}}\). El resultado se obtuvo mediante el modelo \(y=a_0+a_1x\), con los parámetros de la regresión previa publicados por KRISS y la incertidumbre de \(x\) del presupuesto de BIPM-SRP27. La incertidumbre estándar combinada fue \(u_c=0.403\ \mathrm{nmol\ mol^{-1}}\), incluida la covarianza publicada \(\operatorname{cov}(a_0,a_1)=-3.47\times10^{-4}\ \mathrm{nmol\ mol^{-1}}\). La incertidumbre expandida fue \(U=0.80\ \mathrm{nmol\ mol^{-1}}\), con \(k=1.976\), \(\nu_{eff}=145.081\), truncado a 145 para seleccionar el cuantil t, y probabilidad de cobertura bilateral aproximada de 95 %. El resultado se expresa como \((30.32\pm0.80)\ \mathrm{nmol\ mol^{-1}}\), donde el valor después de ± es la incertidumbre expandida. Los parámetros y la covarianza proceden del informe KRISS, §14.1, ecuaciones 9–10, p. 9; \(u(x)\) procede del protocolo BIPM.QM-K1 v2.1, App. 1, ecuación 14, p. 23. La asignación \(\nu_{a_1}=2\) es un escenario didáctico simplificado, no un dato publicado por KRISS o BIPM.

### Nivel de 500 nmol mol⁻¹

La fracción de cantidad de ozono en aire seco atribuida a KRISS-SRP5 al compararla, antes del transporte, con BIPM-SRP27 en el nivel asignado de 500 nmol mol⁻¹ fue \(y=499.0\ \mathrm{nmol\ mol^{-1}}\). El resultado se obtuvo mediante el modelo \(y=a_0+a_1x\), con los parámetros de la regresión previa publicados por KRISS y la incertidumbre de \(x\) del presupuesto de BIPM-SRP27. La incertidumbre estándar combinada fue \(u_c=2.687\ \mathrm{nmol\ mol^{-1}}\), incluida la covarianza publicada \(\operatorname{cov}(a_0,a_1)=-3.47\times10^{-4}\ \mathrm{nmol\ mol^{-1}}\). La incertidumbre expandida fue \(U=8.6\ \mathrm{nmol\ mol^{-1}}\), con \(k=3.182\), \(\nu_{eff}=3.724\), truncado a 3 para seleccionar el cuantil t, y probabilidad de cobertura bilateral aproximada de 95 %. El resultado se expresa como \((499.0\pm8.6)\ \mathrm{nmol\ mol^{-1}}\), donde el valor después de ± es la incertidumbre expandida. Los parámetros y la covarianza proceden del informe KRISS, §14.1, ecuaciones 9–10, p. 9; \(u(x)\) procede del protocolo BIPM.QM-K1 v2.1, App. 1, ecuación 14, p. 23. La asignación \(\nu_{a_1}=2\) es un escenario didáctico simplificado, no un dato publicado por KRISS o BIPM; el factor de cobertura resultante no debe interpretarse como un valor oficial del informe.

## 7. Rúbrica corta

| Criterio | Puntaje |
|---|---:|
| Define mensurando, unidad y modelo; identifica fuentes | 1 |
| Responde las ocho preguntas con distinción entre datos publicados e interpretación | 2 |
| Reconstruye \(u(x)\) a 30 y 500 nmol mol⁻¹ sin doble conteo | 1 |
| Propaga \(a_0\), \(a_1\), \(u(x)\) y la covarianza con signo correcto | 2 |
| Aplica Welch–Satterthwaite, truncamiento, t bilateral y redondeo final | 2 |
| Presenta dos declaraciones GUM §7 completas y auditables | 2 |
| **Total** | **10** |

## 8. Errores esperables

- Clasificar una fuente como Tipo A o Tipo B únicamente por su distribución, o atribuir al informe una clasificación que no publicó.
- Llamar al mensurando solo “concentración” o cambiar de unidad sin documentarlo.
- Sumar \(0.28\) y \(2.92\times10^{-3}x\) linealmente en lugar de combinarlos en cuadratura.
- Usar simultáneamente la expresión resumida de \(u(x)\) y volver a agregar \(L_{opt}\), \(P\), \(T\) y \(D\), produciendo doble conteo.
- Incluir la incertidumbre de \(\sigma\) aunque ambos fotómetros usan el mismo valor convencional, o afirmar erróneamente que siempre es cero.
- Eliminar el signo negativo de la covarianza, tomar su valor absoluto o tratarla como una incertidumbre independiente con raíz cuadrada propia.
- Omitir \(u(x)\) y calcular solo la incertidumbre de la recta condicionada a un \(x\) exacto.
- Fijar \(k=2\) después de afirmar que se aplicó Welch–Satterthwaite.
- No truncar \(\nu_{eff}\) según la regla del ejercicio antes de consultar la distribución t.
- Presentar \(\nu_{a_1}=2\) o el \(k\) resultante como cifras oficiales de KRISS o BIPM.
- Redondear contribuciones antes de terminar la combinación.
- Repartir el término cruzado negativo por completo a una sola fuente o exigir porcentajes individuales no negativos.
- Declarar que el cambio de pendiente demuestra por sí solo estabilidad, inventando una covarianza pre/post no publicada.
- Informar únicamente \(U\) sin \(u_c\), \(k\), cobertura, grados efectivos, modelo, fuentes y limitación didáctica.
