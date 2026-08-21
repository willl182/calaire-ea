#!/usr/bin/env Rscript

# Demostración de propagación de incertidumbre por GUF y Monte Carlo
# para fotometría UV de ozono según JCGM 100 y JCGM 101.
#
# Modelo de Beer-Lambert:
#   x = -[1 / (sigma * L)] * (T / T0) * (P0 / P) * ln(D) * 1e9
#
# Unidades:
#   x     concentración (fracción de cantidad de sustancia), en nmol/mol
#   sigma coeficiente de absorción, en atm^-1 cm^-1
#   L     longitud óptica, en cm
#   T,T0  temperaturas, en K
#   P,P0  presiones, en kPa; P0/P es adimensional
#   D     cociente de intensidades I/I0, adimensional
#   1e9   conversión de mol/mol a nmol/mol
#
# Solo usa R base. Ejecutar con:
#   Rscript demo_mcm_beer_lambert.R

options(width = 110, digits = 8)

# -----------------------------------------------------------------------------
# Datos de entrada y modelo de medición
# -----------------------------------------------------------------------------

sigma0 <- 304.39       # atm^-1 cm^-1
u_rel_sigma <- 0.0031  # incertidumbre estándar relativa; distribución normal
u_sigma <- sigma0 * u_rel_sigma

L0 <- 38.0             # cm
semi_L <- 0.05         # cm; distribución rectangular

T0_ref <- 298.15       # K; temperatura de referencia
T0 <- 298.15           # K
semi_T <- 0.5          # K; distribución rectangular

P0_ref <- 101.325      # kPa; presión de referencia
P0 <- 101.325          # kPa
semi_P <- 0.2          # kPa; distribución rectangular

# Se fija x nominal en 100 nmol/mol y se despeja D del modelo.
x_objetivo <- 100.0
D0 <- exp(
  -x_objetivo * 1e-9 * sigma0 * L0 *
    (T0_ref / T0) * (P0 / P0_ref)
)
semi_D <- 2.0e-5       # adimensional; distribución triangular simétrica

modelo <- function(sigma, L, T, P, D) {
  -(1 / (sigma * L)) * (T / T0_ref) * (P0_ref / P) * log(D) * 1e9
}

y_guf <- modelo(sigma0, L0, T0, P0, D0)

cat("DEMOSTRACIÓN MCM: FOTOMETRÍA UV DE OZONO\n")
cat("============================================================\n")
cat(sprintf("D nominal elegido: %.9f\n", D0))
cat(sprintf("Resultado nominal: %.6f nmol/mol\n\n", y_guf))

# -----------------------------------------------------------------------------
# Parte 1. GUF analítico: ley de propagación de incertidumbre
# -----------------------------------------------------------------------------

# Incertidumbres estándar de las distribuciones no normales:
#   rectangular simétrica con semi-ancho a: u = a / sqrt(3)
#   triangular simétrica con semi-ancho a:   u = a / sqrt(6)
u_L <- semi_L / sqrt(3)
u_T <- semi_T / sqrt(3)
u_P <- semi_P / sqrt(3)
u_D <- semi_D / sqrt(6)

# Coeficientes de sensibilidad, evaluados en los valores nominales.
# Si x = -C * ln(D) / (sigma * L) * T / P, entonces:
#   dx/dsigma = -x / sigma
#   dx/dL     = -x / L
#   dx/dT     =  x / T
#   dx/dP     = -x / P
#   dx/dD     = -[1/(sigma*L)]*(T/T0)*(P0/P)*(1/D)*1e9
c_sigma <- -y_guf / sigma0
c_L <- -y_guf / L0
c_T <- y_guf / T0
c_P <- -y_guf / P0
c_D <- -(1 / (sigma0 * L0)) * (T0 / T0_ref) *
  (P0_ref / P0) * (1 / D0) * 1e9

presupuesto <- data.frame(
  Magnitud = c("sigma", "L", "T", "P", "D"),
  Valor = c(sigma0, L0, T0, P0, D0),
  Distribucion = c("normal", "rectangular", "rectangular", "rectangular", "triangular"),
  u_entrada = c(u_sigma, u_L, u_T, u_P, u_D),
  Sensibilidad = c(c_sigma, c_L, c_T, c_P, c_D),
  Contribucion_u = abs(c(c_sigma, c_L, c_T, c_P, c_D) *
    c(u_sigma, u_L, u_T, u_P, u_D)),
  stringsAsFactors = FALSE
)

u_c <- sqrt(sum(presupuesto$Contribucion_u^2))
k <- 2
U <- k * u_c

cat("PARTE 1. PRESUPUESTO GUF\n")
cat("------------------------------------------------------------\n")
print(presupuesto, row.names = FALSE, right = FALSE)
cat(sprintf("\nu_c = %.6f nmol/mol\n", u_c))
cat(sprintf("U = k*u_c = %.6f nmol/mol, con k = %g\n", U, k))
cat(sprintf("Intervalo GUF: [%.6f, %.6f] nmol/mol\n\n", y_guf - U, y_guf + U))

# -----------------------------------------------------------------------------
# Parte 2. Propagación MCM adaptativa según JCGM 101
# -----------------------------------------------------------------------------

# Intervalo empírico de cobertura más corto para probabilidad p.
intervalo_mas_corto <- function(x, p = 0.95) {
  xs <- sort(x)
  n <- length(xs)
  m <- floor(p * n)
  if (m < 1L || m >= n) {
    stop("Cantidad insuficiente de resultados para calcular el intervalo.")
  }
  anchos <- xs[(m + 1L):n] - xs[1L:(n - m)]
  i <- which.min(anchos)
  c(inferior = xs[i], superior = xs[i + m])
}

# Generador triangular simétrico en [centro-a, centro+a].
# Diferencia de dos U(0,1): densidad triangular con moda en cero.
rtriangular_simetrica <- function(n, centro, a) {
  centro + a * (runif(n) - runif(n))
}

set.seed(20260817)

# r define resolución decimal requerida. JCGM 101 usa delta = 0.5*10^r.
r <- -1
delta <- 0.5 * 10^r
h <- 50000L             # ensayos por bloque
min_bloques <- 4L       # mínimo para estimar dispersión entre bloques
max_bloques <- 40L      # límite de seguridad: máximo 2 000 000 ensayos
p_cobertura <- 0.95

resultados <- numeric(0)
resumen_bloques <- data.frame(
  media = numeric(0),
  u = numeric(0),
  inferior = numeric(0),
  superior = numeric(0)
)
estabilizado <- FALSE

cat("PARTE 2. MONTE CARLO ADAPTATIVO\n")
cat("------------------------------------------------------------\n")
cat(sprintf("h = %d ensayos/bloque; delta = %.3f nmol/mol\n", h, delta))

for (b in seq_len(max_bloques)) {
  sigma_b <- rnorm(h, mean = sigma0, sd = u_sigma)
  L_b <- runif(h, min = L0 - semi_L, max = L0 + semi_L)
  T_b <- runif(h, min = T0 - semi_T, max = T0 + semi_T)
  P_b <- runif(h, min = P0 - semi_P, max = P0 + semi_P)
  D_b <- rtriangular_simetrica(h, centro = D0, a = semi_D)

  y_b <- modelo(sigma_b, L_b, T_b, P_b, D_b)
  int_b <- intervalo_mas_corto(y_b, p_cobertura)
  resultados <- c(resultados, y_b)
  resumen_bloques[b, ] <- c(mean(y_b), sd(y_b), int_b)

  if (b >= min_bloques) {
    # Criterio adaptativo: cada dispersión estándar entre resultados de
    # bloques, multiplicada por 2, debe ser menor o igual que delta.
    dispersion <- vapply(resumen_bloques, sd, numeric(1))
    criterio <- 2 * dispersion
    estabilizado <- all(criterio <= delta)

    cat(sprintf(
      "Bloque %2d: 2s(media,u,LI,LS) = (%0.4f, %0.4f, %0.4f, %0.4f)%s\n",
      b, criterio[1], criterio[2], criterio[3], criterio[4],
      if (estabilizado) "  ESTABLE" else ""
    ))

    if (estabilizado) break
  }
}

if (!estabilizado) {
  warning("No se alcanzó estabilización antes del máximo de bloques.")
}

M <- length(resultados)
y_mcm <- mean(resultados)
u_mcm <- sd(resultados)
intervalo_mcm <- intervalo_mas_corto(resultados, p_cobertura)

cat(sprintf("\nEnsayos totales M = %d (%d bloques)\n", M, nrow(resumen_bloques)))
cat(sprintf("Esperanza MCM = %.6f nmol/mol\n", y_mcm))
cat(sprintf("Desviación estándar MCM = %.6f nmol/mol\n", u_mcm))
cat(sprintf(
  "Intervalo MCM más corto al 95 %%: [%.6f, %.6f] nmol/mol\n\n",
  intervalo_mcm[1], intervalo_mcm[2]
))

# -----------------------------------------------------------------------------
# Parte 3. Validación de resultados según JCGM 101, sección 8
# -----------------------------------------------------------------------------

limites_guf <- c(inferior = y_guf - U, superior = y_guf + U)
dlow <- abs(limites_guf[1] - intervalo_mcm[1])
dhigh <- abs(limites_guf[2] - intervalo_mcm[2])
validado <- (dlow <= delta) && (dhigh <= delta)

cat("PARTE 3. VALIDACIÓN GUF FRENTE A MCM\n")
cat("------------------------------------------------------------\n")
cat(sprintf("d_low  = |LI_GUF - LI_MCM| = %.6f nmol/mol\n", dlow))
cat(sprintf("d_high = |LS_GUF - LS_MCM| = %.6f nmol/mol\n", dhigh))
cat(sprintf("Tolerancia delta = %.6f nmol/mol\n", delta))
cat(sprintf(
  "Veredicto: %s\n\n",
  if (validado) "VALIDACIÓN SATISFACTORIA" else "VALIDACIÓN NO SATISFACTORIA"
))

# -----------------------------------------------------------------------------
# Parte 4. PDF de salida e intervalos de cobertura
# -----------------------------------------------------------------------------

script_arg <- grep("^--file=", commandArgs(trailingOnly = FALSE), value = TRUE)
if (length(script_arg) == 1L) {
  directorio_salida <- dirname(normalizePath(sub("^--file=", "", script_arg)))
} else {
  directorio_salida <- getwd()
}
ruta_png <- file.path(directorio_salida, "demo_mcm_pdf_salida.png")

png(filename = ruta_png, width = 1400, height = 900, res = 150)
par(mar = c(5.2, 5.2, 4.2, 1.5), las = 1)

hist(
  resultados,
  breaks = "FD",
  probability = TRUE,
  col = "#D9E2E8",
  border = "white",
  main = "PDF de salida: concentración de ozono por MCM",
  xlab = "Concentración x (nmol/mol)",
  ylab = "Densidad"
)
lines(density(resultados), col = "#263238", lwd = 2.2)

# Azul sólido: GUF. Naranja discontinuo: MCM. Tipo de línea aporta
# codificación adicional y evita depender solo del color.
abline(v = limites_guf, col = "#0072B2", lwd = 2.2, lty = 1)
abline(v = intervalo_mcm, col = "#D55E00", lwd = 2.2, lty = 2)
abline(v = y_guf, col = "#455A64", lwd = 1.5, lty = 3)

legend(
  "topright",
  legend = c("Densidad MCM", "Intervalo GUF, k = 2", "Intervalo MCM más corto, 95 %", "Valor nominal"),
  col = c("#263238", "#0072B2", "#D55E00", "#455A64"),
  lwd = c(2.2, 2.2, 2.2, 1.5),
  lty = c(1, 1, 2, 3),
  bty = "n",
  cex = 0.88
)

grid(nx = NA, ny = NULL, col = "#CFD8DC", lty = 3)
box(col = "#78909C")
dev.off()

cat("PARTE 4. GRÁFICO\n")
cat("------------------------------------------------------------\n")
cat(sprintf("PNG guardado en: %s\n", ruta_png))
