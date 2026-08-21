# Solución M5 — Verificación multipunto, deriva y conformidad

## 1. Enunciado resumido

A partir de los tres ciclos del archivo `dataset_verificacion_multipunto.csv` se debe:

1. conservar `lectura_ref` y corregirla con el certificado mediante
   \(X=(\text{lectura_ref}-b)/m\), con \(m=1.003\) y \(b=-0.4\ \text{ppb}\);
2. calcular en cada fila \(d=\text{lectura_uut}-X\);
3. ajustar, **con ceros y niveles**, una regresión `lectura_uut = intercepto + pendiente × X` por ciclo y otra global;
4. examinar pendientes, interceptos, residuos, diferencias entre ceros y cambios entre ciclos;
5. aplicar todos los criterios fijados y emitir una decisión razonada antes de proponer cualquier ajuste.

## 2. Solución paso a paso

### Paso 1. Corregir la lectura de referencia

La ecuación correcta del certificado es:

\[
X=\frac{I_{ref}-b}{m}
 =\frac{I_{ref}-(-0.4)}{1.003}
 =\frac{I_{ref}+0.4}{1.003}.
\]

No se multiplica `lectura_ref` por la pendiente ni se suma el intercepto después de dividir. Tampoco se reemplaza la columna original.

Ejemplo, ciclo 1, nivel nominal 20 ppb:

\[
X=\frac{19.73+0.4}{1.003}=20.069791\ \text{ppb},
\]

\[
d=20.44-20.069791=+0.370209\ \text{ppb}.
\]

Como \(X\le 50\ \text{ppb}\), se usa el límite absoluto:

\[
|d|=0.370209\ \text{ppb}\le1.5\ \text{ppb}.
\]

Ejemplo para un nivel alto, ciclo 1, nominal 180 ppb:

\[
X=\frac{179.58+0.4}{1.003}=179.441675\ \text{ppb},
\]

\[
d=178.08-179.441675=-1.361675\ \text{ppb},
\]

\[
\left|\frac{100d}{X}\right|
=\left|\frac{100(-1.361675)}{179.441675}\right|
=0.758840\%\le3.1\%.
\]

La incertidumbre expandida del certificado se puede calcular, por ejemplo en el primer caso, como

\[
U(X)=0.5+0.01(20.069791)=0.700698\ \text{ppb},\quad k=2,
\]

pero el enunciado establece una regla binaria: esta incertidumbre **no se suma a los límites**.

### Paso 2. Valores corregidos y diferencias

Los resultados siguientes se muestran redondeados; la evaluación se hizo sin redondeo previo.

| Ciclo | Punto | Nominal (ppb) | \(X\) (ppb) | UUT (ppb) | \(d=UUT-X\) (ppb) | Resultado aplicable | Cumple |
|---:|:---|---:|---:|---:|---:|---:|:---:|
| 1 | cero_pre | 0 | 0.1296 | 0.56 | +0.4304 | \(|d|=0.4304\) ppb | Sí |
| 1 | nivel | 20 | 20.0698 | 20.44 | +0.3702 | \(|d|=0.3702\) ppb | Sí |
| 1 | nivel | 40 | 39.9103 | 40.27 | +0.3597 | \(|d|=0.3597\) ppb | Sí |
| 1 | nivel | 70 | 70.4487 | 69.99 | −0.4587 | 0.6510 % | Sí |
| 1 | nivel | 100 | 99.8903 | 99.68 | −0.2103 | 0.2106 % | Sí |
| 1 | nivel | 140 | 139.2024 | 139.20 | −0.0024 | 0.0017 % | Sí |
| 1 | nivel | 180 | 179.4417 | 178.08 | −1.3617 | 0.7588 % | Sí |
| 1 | cero_post | 0 | −0.2692 | 0.53 | +0.7992 | \(|d|=0.7992\) ppb | Sí |
| 2 | cero_pre | 0 | 0.2094 | 0.30 | +0.0906 | \(|d|=0.0906\) ppb | Sí |
| 2 | nivel | 20 | 20.0897 | 20.09 | +0.0003 | \(|d|=0.0003\) ppb | Sí |
| 2 | nivel | 40 | 40.0399 | 39.81 | −0.2299 | \(|d|=0.2299\) ppb | Sí |
| 2 | nivel | 70 | 69.8006 | 70.41 | +0.6094 | 0.8731 % | Sí |
| 2 | nivel | 100 | 100.2493 | 99.68 | −0.5693 | 0.5678 % | Sí |
| 2 | nivel | 140 | 140.3789 | 139.89 | −0.4889 | 0.3482 % | Sí |
| 2 | nivel | 180 | 179.7109 | 179.29 | −0.4209 | 0.2342 % | Sí |
| 2 | cero_post | 0 | 0.0598 | 0.47 | +0.4102 | \(|d|=0.4102\) ppb | Sí |
| 3 | cero_pre | 0 | −0.1097 | 1.02 | +1.1297 | \(|d|=1.1297\) ppb | Sí |
| 3 | nivel | 20 | 19.8106 | 20.57 | +0.7594 | \(|d|=0.7594\) ppb | Sí |
| 3 | nivel | 40 | 40.2592 | 41.12 | +0.8608 | \(|d|=0.8608\) ppb | Sí |
| 3 | nivel | 70 | 69.6909 | 70.30 | +0.6091 | 0.8740 % | Sí |
| 3 | nivel | 100 | 99.6810 | 100.31 | +0.6290 | 0.6311 % | Sí |
| 3 | nivel | 140 | 139.8405 | 139.88 | +0.0395 | 0.0283 % | Sí |
| 3 | nivel | 180 | 180.2193 | 179.26 | −0.9593 | 0.5323 % | Sí |
| 3 | cero_post | 0 | 0.4686 | 0.39 | −0.0786 | \(|d|=0.0786\) ppb | Sí |

No se calcula una diferencia porcentual para los puntos de cero. Aunque la corrección produce valores de \(X\) pequeños que no son exactamente cero, esos puntos pertenecen al intervalo \(X\le50\ \text{ppb}\) y se evalúan en ppb.

Máximas diferencias absolutas, considerando ceros y niveles:

- ciclo 1: \(\max|d|=1.361675\ \text{ppb}\), nivel 180;
- ciclo 2: \(\max|d|=0.609402\ \text{ppb}\), nivel 70;
- ciclo 3: \(\max|d|=1.129671\ \text{ppb}\), cero previo.

Para la comprobación por puntos, el máximo bajo \(X\le50\) es \(1.129671\ \text{ppb}<1.5\ \text{ppb}\). Para \(X>50\), el máximo es \(0.873963\%<3.1\%\).

### Paso 3. Regresión por ciclo, usando ceros y niveles

En cada ciclo se ajustan las ocho observaciones:

\[
I_{UUT,i}=b_j+m_jX_i+e_i,
\qquad
e_i=I_{UUT,i}-(b_j+m_jX_i).
\]

Resultados:

| Ciclo | Pendiente \(m_j\) | Intercepto \(b_j\) (ppb) | \(s_{res}\) (ppb) | \(\max|e|\) (ppb) | Punto de \(\max|e|\) | Máx. \(|d|\) (ppb) |
|---:|---:|---:|---:|---:|:---|---:|
| 1 | 0.991209 | +0.593923 | 0.368146 | 0.627464 | nivel 140 | 1.361675 |
| 2 | 0.995917 | +0.206211 | 0.360195 | 0.688215 | nivel 70 | 0.609402 |
| 3 | 0.992973 | +0.856651 | 0.522569 | 0.931952 | cero posterior | 1.129671 |

Ejemplo explícito del residuo máximo del ciclo 1:

\[
\hat I_{UUT}=0.593922529+0.991208632(139.202392822)
=138.572535881\ \text{ppb},
\]

\[
e=139.20-138.572535881=+0.627464119\ \text{ppb}.
\]

Ejemplo del residuo máximo del ciclo 3:

\[
\hat I_{UUT}=0.856650509+0.992973448(0.468594217)
=1.321952125\ \text{ppb},
\]

\[
e=0.39-1.321952125=-0.931952125\ \text{ppb}.
\]

Residuos por ciclo:

| Nominal (ppb) | Ciclo 1 (ppb) | Ciclo 2 (ppb) | Ciclo 3 (ppb) |
|---:|---:|---:|---:|
| cero previo | −0.1624 | −0.1147 | +0.2723 |
| 20 | −0.0473 | −0.1239 | +0.0420 |
| 40 | +0.1167 | −0.2726 | +0.2870 |
| 70 | −0.4332 | +0.6882 | +0.2421 |
| 100 | +0.0739 | −0.3661 | +0.4728 |
| 140 | +0.6275 | −0.1219 | +0.1655 |
| 180 | −0.3781 | +0.1068 | −0.5497 |
| cero posterior | +0.2029 | +0.2042 | −0.9320 |

Las tres pendientes cumplen \(0.97\le m_j\le1.03\), y los tres interceptos cumplen \(-3\le b_j\le+3\ \text{ppb}\).

### Paso 4. Regresión global

Como diagnóstico complementario se reúnen las 24 observaciones, sin sustituir las regresiones por ciclo:

\[
I_{UUT}=0.552141+0.993370X.
\]

Resultados globales:

- pendiente: \(0.993370\);
- intercepto: \(+0.552141\ \text{ppb}\);
- desviación estándar residual: \(0.453232\ \text{ppb}\);
- residuo de mayor magnitud: \(0.737749\ \text{ppb}\).

Los residuos globales medios por nivel nominal son:

| Nominal (ppb) | Residuo global medio (ppb) |
|---:|---:|
| 0 | −0.0880 |
| 20 | −0.0430 |
| 40 | +0.0437 |
| 70 | +0.1651 |
| 100 | +0.0602 |
| 140 | +0.2241 |
| 180 | −0.2742 |

El cambio a residuo medio negativo en 180 ppb, después de valores medios positivos entre 40 y 140 ppb, muestra una **falta de ajuste lineal leve en el extremo alto**. No basta para atribuir una causa por sí sola, pero sí justifica vigilar la respuesta de nivel alto y revisar el montaje y la estabilización antes de intervenir el equipo.

### Paso 5. Estabilidad y deriva entre ciclos

Se usa la desviación estándar muestral.

Promedio de pendientes:

\[
\bar m=\frac{0.991208632+0.995916599+0.992973448}{3}
=0.993366226.
\]

Dispersión de pendientes:

\[
s_m=\sqrt{\frac{\sum_{j=1}^{3}(m_j-\bar m)^2}{3-1}}
=0.002378<0.0075.
\]

Promedio de interceptos:

\[
\bar b=\frac{0.593922529+0.206210533+0.856650509}{3}
=0.552261190\ \text{ppb}.
\]

Dispersión de interceptos:

\[
s_b=\sqrt{\frac{\sum_{j=1}^{3}(b_j-\bar b)^2}{3-1}}
=0.327215\ \text{ppb}<1.00\ \text{ppb}.
\]

Cambios observados de un ciclo al siguiente:

- pendiente: \(m_2-m_1=+0.004708\); \(m_3-m_2=-0.002943\);
- intercepto: \(b_2-b_1=-0.387712\ \text{ppb}\); \(b_3-b_2=+0.650440\ \text{ppb}\).

No hay una secuencia monotónica limpia en los coeficientes estimados. La deriva pequeña queda parcialmente enmascarada por el ruido, la distribución de puntos y la falta de ajuste lineal de nivel alto. Por eso, tres ciclos permiten comprobar estabilidad durante esta verificación, pero no estimar con firmeza una deriva histórica.

Ceros observados del UUT:

| Ciclo | Cero previo (ppb) | Cero posterior (ppb) | Posterior − previo (ppb) |
|---:|---:|---:|---:|
| 1 | 0.56 | 0.53 | −0.03 |
| 2 | 0.30 | 0.47 | +0.17 |
| 3 | 1.02 | 0.39 | −0.63 |

El cambio de −0.63 ppb del ciclo 3 es el mayor indicio de variación dentro de un ciclo. No es un requisito de rechazo adicional porque el ejercicio no fijó un límite para este cambio, pero obliga a revisar estabilidad, aire cero, fugas, tiempos y condiciones del montaje antes de ajustar.

### Paso 6. Contraste con los efectos inyectados

Los metadatos indican que el conjunto sintético contiene:

- UUT base con pendiente 0.9950 y offset +0.30 ppb;
- deriva de cero de +0.15 ppb por ciclo;
- deriva de pendiente de +0.0008 por ciclo;
- curvatura de \(-1.85\times10^{-5}\ \text{ppb}^{-1}\), aproximadamente −0.6 ppb a 180 ppb;
- ruido de 0.25 ppb RMS y componente proporcional de 0.15 %.

El ajuste global recupera razonablemente la escala central: pendiente 0.993370, cercana a 0.9950, e intercepto +0.552 ppb, del mismo orden que el offset base más la evolución simulada del cero. Las pendientes por ciclo no aumentan de forma monotónica pese a la deriva inyectada de +0.0008/ciclo; esto ilustra que una deriva pequeña no necesariamente se reconoce directamente en solo tres estimaciones ruidosas.

La señal más coherente con la curvatura inyectada está en el extremo alto: el residuo global medio a 180 ppb es −0.274 ppb y los ciclos 1 y 3 presentan diferencias de −1.362 y −0.959 ppb en ese nivel. El efecto teórico de curvatura a 180 ppb es

\[
-1.85\times10^{-5}(180)^2=-0.5994\ \text{ppb},
\]

compatible en signo y orden de magnitud con la falta de ajuste observada, aunque el ruido impide recuperar exactamente ese valor en cada ciclo. El contraste se usa para explicar el diseño del ejercicio, no para afirmar que esos efectos podrían identificarse de manera única a partir de estos datos.

### Paso 7. Conformidad razonada

| Requisito | Resultado observado | Decisión |
|:---|:---|:---:|
| Para cada punto con \(X\le50\): \(|d|\le1.5\) ppb | máximo 1.129671 ppb | Cumple |
| Para cada punto con \(X>50\): \(|100d/X|\le3.1\%\) | máximo 0.873963 % | Cumple |
| Pendiente de cada ciclo entre 0.97 y 1.03 | 0.991209; 0.995917; 0.992973 | Cumple |
| Intercepto de cada ciclo entre −3 y +3 ppb | +0.593923; +0.206211; +0.856651 ppb | Cumple |
| \(s\) de pendientes menor que 0.0075 | 0.002378 | Cumple |
| \(s\) de interceptos menor que 1.00 ppb | 0.327215 ppb | Cumple |

## 3. Código R reproducible usado

Ejecutar desde la raíz del curso o adaptar `archivo` a una ruta absoluta:

```r
archivo <- "contenido/datasets/dataset_verificacion_multipunto.csv"
d <- read.csv(archivo, stringsAsFactors = FALSE)

m_cert <- 1.003
b_cert <- -0.4

d$X <- (d$lectura_ref - b_cert) / m_cert
d$diferencia <- d$lectura_uut - d$X

# El porcentaje se informa solo para niveles altos; no para ceros.
d$porcentaje <- ifelse(
  d$X > 50,
  100 * d$diferencia / d$X,
  NA_real_
)

d$cumple_punto <- ifelse(
  d$X <= 50,
  abs(d$diferencia) <= 1.5,
  abs(d$porcentaje) <= 3.1
)

# Regresiones solicitadas: incluyen ceros y niveles.
indices <- split(seq_len(nrow(d)), d$ciclo)
ajustes <- lapply(indices, function(i) {
  lm(lectura_uut ~ X, data = d[i, ])
})

d$residuo_ciclo <- NA_real_
for (nm in names(indices)) {
  d$residuo_ciclo[indices[[nm]]] <- residuals(ajustes[[nm]])
}

resumen_ciclos <- do.call(rbind, lapply(names(ajustes), function(nm) {
  i <- indices[[nm]]
  z <- d[i, ]
  fit <- ajustes[[nm]]
  k_d <- which.max(abs(z$diferencia))
  k_e <- which.max(abs(residuals(fit)))

  data.frame(
    ciclo = as.integer(nm),
    intercepto = unname(coef(fit)[1]),
    pendiente = unname(coef(fit)[2]),
    s_residual = summary(fit)$sigma,
    maxima_diferencia = max(abs(z$diferencia)),
    punto_max_d = paste(z$punto[k_d], z$nivel_nominal[k_d]),
    maximo_residuo = max(abs(residuals(fit))),
    punto_max_residuo = paste(z$punto[k_e], z$nivel_nominal[k_e]),
    cero_pre = z$lectura_uut[z$punto == "cero_pre"],
    cero_post = z$lectura_uut[z$punto == "cero_post"]
  )
}))

ajuste_global <- lm(lectura_uut ~ X, data = d)

sd_pendientes <- sd(resumen_ciclos$pendiente)
sd_interceptos <- sd(resumen_ciclos$intercepto)

print(d[, c("ciclo", "punto", "nivel_nominal", "lectura_ref",
            "X", "lectura_uut", "diferencia", "porcentaje",
            "residuo_ciclo", "cumple_punto")], digits = 10)
print(resumen_ciclos, digits = 10)
print(summary(ajuste_global), digits = 10)
cat("SD pendientes:", sd_pendientes, "\n")
cat("SD interceptos:", sd_interceptos, "ppb\n")

residuos_medios <- aggregate(
  residuals(ajuste_global),
  by = list(nivel_nominal = d$nivel_nominal),
  FUN = mean
)
print(residuos_medios, digits = 10)
```

## 4. Resultado final

> **CONFORME según la regla binaria del ejercicio.** Cumplen todos los puntos, las pendientes e interceptos de los tres ciclos y las dos condiciones de estabilidad entre ciclos. La evidencia no justifica ajustar el equipo: primero debe conservarse el estado encontrado. No obstante, los residuos y las diferencias a 180 ppb muestran una falta de ajuste lineal leve en el extremo alto, y el ciclo 3 presenta un cambio de cero de −0.63 ppb. Antes de intervenir se deben comprobar estabilización, aire cero, fugas, tubería, flujo, presión, temperatura y aplicación correcta del certificado.

## 5. Rúbrica corta

- **Completa:** corrige con \(X=(I_{ref}+0.4)/1.003\), conserva `lectura_ref`, calcula diferencias en las 24 filas, usa ceros y niveles en las regresiones por ciclo, informa ajuste global, residuos, estabilidad, falta de ajuste alto y concluye conforme con comprobaciones previas al ajuste.
- **Parcial:** llega a la decisión correcta, pero omite alguna operación, los ceros, el ajuste global, la deriva o el análisis de residuos.
- **Incorrecta:** usa `lectura_ref` sin corregir, aplica la ecuación del certificado al revés, excluye los ceros de las regresiones solicitadas, calcula porcentajes para decidir en cero, modifica límites con la incertidumbre o decide usando solo pendiente o \(R^2\).

## 6. Errores esperables

1. Usar \(X=mI_{ref}+b\) en vez de \(X=(I_{ref}-b)/m\).
2. Sobrescribir `lectura_ref` y perder el dato original.
3. Ajustar solo los seis niveles, aunque el enunciado pide usar ceros y niveles.
4. Mezclar los tres ciclos en una única regresión y omitir los ajustes individuales.
5. Aplicar 3.1 % a puntos con \(X\le50\ \text{ppb}\), especialmente a los ceros.
6. Comparar la diferencia en ppb de 180 ppb con el límite de 1.5 ppb, en lugar de usar el porcentaje.
7. Redondear pendientes e interceptos antes de calcular residuos o desviaciones estándar.
8. Usar desviación estándar poblacional en vez de muestral.
9. Concluir que un \(R^2\) muy alto elimina la necesidad de revisar residuos.
10. Confundir variación de cero dentro de un ciclo con una estimación completa de deriva histórica.
11. Declarar demostrada una causa solo porque los residuos sugieren curvatura.
12. Ajustar el instrumento antes de verificar montaje, estabilidad, referencia y condiciones ambientales.
