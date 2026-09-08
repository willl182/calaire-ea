# E16 — Monte Carlo para modelo diferencial con covarianza medida

Enlaza con **M8**. Usa como entradas los resultados de **E03** (covarianza medida) y **E04** (distribución de `η`).

## Objetivo

Propagar la distribución de `NO2=(X-N)/η` mediante Monte Carlo (MCM), preservando la covarianza medida en E03 y la distribución de `η` obtenida en E04; comparar con la aproximación GUM lineal.

## Instrumentos y software

Resultados de E03 y E04; computador con R; plantilla de presupuesto; semilla registrada; mínimo `10⁶` simulaciones para el resultado final.

## Procedimiento

1. **Reunir entradas, 5 min.** Medias `X,N`, `u_X,u_N`, covarianza o `ρ`, `η,u_η`, grados de libertad y evidencia de distribuciones.
2. **Validar matriz, 5 min.** Construir la matriz de covarianza y comprobar que es semidefinida positiva.
3. **Definir distribuciones, 5 min.** Normal bivariada para los canales si los datos lo respaldan. Normal truncada `0<η≤1`, beta ajustada o distribución empírica para la eficiencia.
4. **Simulación piloto, 5 min.** Ejecutar `10⁵` sorteos y revisar valores imposibles, histogramas y estabilidad.
5. **Simulación final, 10 min.** Ejecutar `10⁶` sorteos, calcular `y_j=(X_j-N_j)/η_j`, media, desviación, mediana e intervalo de cobertura 95 % por cuantiles.
6. **Comparación GUM, 5 min.** Calcular el modelo lineal con término de covarianza.
7. **Sensibilidad, 5 min.** Repetir con `ρ=0` para mostrar el efecto de ignorar la covarianza.

**Duración:** 40 min.

## Tabla de registro

| entrada | estimación | u estándar | distribución | correlación/fuente | unidad |
|---|---:|---:|---|---|---|
| X | | | normal conjunta | E03 | nmol/mol |
| N | | | normal conjunta | E03 | nmol/mol |
| η | | | normal truncada/beta/empírica | E04 | 1 |
| número de sorteos | 1 000 000 | — | — | — | — |
| semilla | | — | — | — | — |

## Modelo de cálculo

Matriz de canales:

\[
\Sigma=\begin{pmatrix}u_X^2&\rho u_Xu_N\\\rho u_Xu_N&u_N^2\end{pmatrix}.
\]

Para cada sorteo: `(X_j,N_j)~N₂[(X̄,N̄),Σ]`, `η_j~f_η`, `y_j=(X_j-N_j)/η_j`. Resultado MCM: media o mediana, desviación estándar y cuantiles 0.025 y 0.975. No imponer `U=2u` si la distribución de salida es asimétrica.

Aproximación GUM:

\[
u_c^2(y)=\frac{u_X^2+u_N^2-2\rho u_Xu_N}{\eta^2}+\left(\frac{X-N}{\eta^2}\right)^2u_\eta^2.
\]

## Ejemplo numérico trabajado

Entradas mixtas de dos experimentos distintos: `X=205.0, N=200.0` son un punto de la titulación GPT de **E04** (par NOx/NO observado a un nivel de la escalera), mientras que `ρ=0.70`, `u_X=1.2` y `u_N=1.0` provienen de la serie de covarianza medida en **E03** (que se ejecuta a concentración de NO estable, no necesariamente en el mismo punto de E04). Esta combinación es una simplificación didáctica: en un presupuesto real, las incertidumbres de canal deben corresponder al mismo nivel y condiciones del par `(X,N)` usado, o declararse explícitamente como una extrapolación. `η=0.970, u_η=0.010` provienen de **E04**. `cov(X,N)=0.84`. `y=5.0/0.970=5.1546 nmol/mol`.

Coeficientes: `c_X=1/0.970=1.03093`, `c_N=-1.03093`, `c_η=-5/0.970²=-5.31406`.

Varianza de canales: `1.03093²(1.2²+1.0²)-2(1.03093²)(0.84)=0.8077`. Varianza por eficiencia: `(5.31406)²(0.010)²=0.00282`.

\[
u_c=\sqrt{0.8077+0.00282}=0.9003\ \mathrm{nmol/mol},\qquad U_{k=2}=1.801\ \mathrm{nmol/mol}.
\]

Sin covarianza: `u_c=√[(1.2²+1.0²)/0.970²+0.00282]=1.611 nmol/mol`.

El MCM con normal bivariada y `η` normal truncada debe producir aproximadamente media 5.155 nmol/mol, `u` 0.90 nmol/mol e intervalo 95 % cercano a `[3.39, 6.92] nmol/mol`; los valores exactos dependen de la semilla y la distribución de `η`.

Código R mínimo:

```r
set.seed(20260826)
B <- 1e6
mu <- c(X = 205, N = 200)
Sigma <- matrix(c(1.2^2, 0.84, 0.84, 1.0^2), 2, 2)
L <- chol(Sigma)
z <- matrix(rnorm(2 * B), ncol = 2)
canales <- sweep(z %*% L, 2, mu, `+`)
eta <- rnorm(B, 0.970, 0.010)
while (any(eta <= 0 | eta > 1)) {
  i <- which(eta <= 0 | eta > 1)
  eta[i] <- rnorm(length(i), 0.970, 0.010)
}
y <- (canales[, 1] - canales[, 2]) / eta
c(media = mean(y), u = sd(y), quantile(y, c(0.025, 0.5, 0.975)))
```

## Criterios de aceptación

- Matriz de covarianza válida y fuente de `ρ` trazable a E03.
- Distribución de `η` respeta el dominio físico y la evidencia de E04.
- Resultado estable: duplicar sorteos cambia media, `u` y límites <0.5 %.
- MCM y GUM compatibles dentro de 2 % para el caso casi lineal; una diferencia mayor exige revisar no linealidad, truncamiento o código.
- La comparación con `ρ=0` se usa como diagnóstico, no como resultado si la covarianza fue medida.

## Seguridad

E16 es análisis de datos y no requiere gases. Si se ejecuta mientras el sistema permanece montado, el cilindro debe quedar cerrado y las líneas purgadas; el generador de O₃ apagado y el venteo conectado.
