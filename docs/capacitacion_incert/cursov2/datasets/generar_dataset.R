#!/usr/bin/env Rscript
# ---------------------------------------------------------------------------
# generar_dataset.R
# Genera el dataset sintético de verificación multipunto para los ejercicios
# del módulo M5 del curso "Incertidumbre en analizadores de O3 y
# patrones de transferencia" (6 h).
#
# Diseño:
#   - 3 ciclos de verificación (días consecutivos simulados)
#   - Cada ciclo: cero pre + 6 niveles (~20/40/70/100/140/180 ppb) + cero post
#   - Columnas: nivel_nominal, ciclo, lectura_ref, lectura_uut,
#               T_celda_K, P_celda_kPa, flujo_L_min, timestamp
#   - Ruido realista basado en specs Thermo 49i (ruido cero 0.25 ppb RMS)
#   - Deriva leve del UUT entre ciclos (+0.15 ppb/ciclo en cero,
#     +0.0008 en pendiente por ciclo)
#   - Falta de ajuste didáctica: leve curvatura negativa del UUT visible
#     en el nivel alto (~ -0.6 ppb a 180 ppb)
#
# Certificado simulado del patrón de referencia (para los ejercicios):
#   pendiente = 1.003, intercepto = -0.4 ppb
#   U(X) = 0.5 ppb + 0.01 * X  (k = 2)
#
# Reproducible: semilla fija.
# Salida: dataset_verificacion_multipunto.csv (mismo directorio)
# ---------------------------------------------------------------------------

set.seed(20260817)

# --- parámetros "verdaderos" del ejercicio ---------------------------------
niveles      <- c(0, 20, 40, 70, 100, 140, 180)   # ppb nominales (0 = cero)
ciclos       <- 1:3
cert_pend    <- 1.003    # certificado del patrón de referencia
cert_inter   <- -0.4     # ppb

# Comportamiento verdadero del UUT respecto al valor verdadero generado:
uut_pend0    <- 0.9950            # pendiente base del UUT
uut_inter0   <- 0.30              # ppb, offset base
deriva_cero  <- 0.15              # ppb por ciclo
deriva_pend  <- 0.0008            # por ciclo
curvatura    <- -1.85e-5          # ppb^-1: falta de ajuste, -0.6 ppb @ 180

ruido_ref    <- 0.25              # ppb RMS (spec 49i, ruido en cero)
ruido_uut    <- 0.25              # ppb RMS
prop_ruido   <- 0.0015            # componente proporcional del ruido

filas <- list()
t0 <- as.POSIXct("2026-05-04 08:00:00", tz = "UTC")

for (c_i in ciclos) {
  # secuencia del ciclo: cero pre, 6 niveles ascendentes, cero post
  secuencia <- c(0, niveles[niveles > 0], 0)
  etiqueta  <- c("cero_pre", rep("nivel", 6), "cero_post")
  for (j in seq_along(secuencia)) {
    nom <- secuencia[j]

    # valor verdadero generado por el fotómetro generador (estable)
    verdadero <- nom * (1 + rnorm(1, 0, 0.001))   # pequeña variación de punto

    # lectura del patrón de referencia: invierte su certificado + ruido
    # (lectura_ref tal como la muestra el patrón, sin corregir)
    ref <- cert_pend * verdadero + cert_inter +
      rnorm(1, 0, sqrt(ruido_ref^2 + (prop_ruido * verdadero)^2))

    # lectura del UUT: pendiente/offset con deriva por ciclo + curvatura
    pend_c <- uut_pend0 + deriva_pend * (c_i - 1)
    intr_c <- uut_inter0 + deriva_cero * (c_i - 1)
    uut <- pend_c * verdadero + intr_c + curvatura * verdadero^2 +
      rnorm(1, 0, sqrt(ruido_uut^2 + (prop_ruido * verdadero)^2))

    # condiciones de celda: rectangulares alrededor de nominal + lenta deriva
    T_K  <- 298.15 + runif(1, -0.4, 0.4) + 0.15 * (c_i - 1)
    P_kPa <- 101.325 + runif(1, -0.25, 0.25)
    flujo <- 0.70 + runif(1, -0.01, 0.01)   # L/min, spec 49i ~0.7

    filas[[length(filas) + 1]] <- data.frame(
      timestamp     = format(t0 + (c_i - 1) * 86400 + (j - 1) * 1200,
                             "%Y-%m-%dT%H:%M:%SZ"),
      ciclo         = c_i,
      punto         = etiqueta[j],
      nivel_nominal = nom,
      lectura_ref   = round(ref, 2),
      lectura_uut   = round(uut, 2),
      T_celda_K     = round(T_K, 2),
      P_celda_kPa   = round(P_kPa, 3),
      flujo_L_min   = round(flujo, 3)
    )
  }
}

d <- do.call(rbind, filas)

# --- salida -----------------------------------------------------------------
dir_out <- dirname(sub("--file=", "", grep("--file=", commandArgs(FALSE), value = TRUE)[1]))
if (is.na(dir_out) || dir_out == "") dir_out <- "."
out <- file.path(dir_out, "dataset_verificacion_multipunto.csv")
write.csv(d, out, row.names = FALSE, quote = FALSE)
cat("Escrito:", out, "-", nrow(d), "filas\n")

# --- chequeo rápido (pedagógico): regresión por ciclo -----------------------
for (c_i in ciclos) {
  s <- subset(d, ciclo == c_i & punto == "nivel")
  # corregir lectura_ref por certificado: X = (ref - intercepto)/pendiente
  X <- (s$lectura_ref - cert_inter) / cert_pend
  f <- lm(s$lectura_uut ~ X)
  cat(sprintf("ciclo %d: pendiente %.4f  intercepto %+.2f ppb  s_res %.2f ppb\n",
              c_i, coef(f)[2], coef(f)[1], summary(f)$sigma))
}
