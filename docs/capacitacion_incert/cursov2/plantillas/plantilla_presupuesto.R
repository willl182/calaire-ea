#!/usr/bin/env Rscript
# ---------------------------------------------------------------------------
# plantilla_presupuesto.R
# Plantilla de presupuesto de incertidumbre (GUM / GUF) para el curso
# "Incertidumbre en analizadores de O3 y patrones de transferencia" (6 h).
#
# Uso pedagógico: cada componente es una fila. La función construye:
#   u estándar = valor / divisor
#   contribución u_i(y) = |c_i| * u
#   u_c = sqrt(sum(u_i^2)), varianza % y clasificación
#   nu_eff (Welch–Satterthwaite), k (t al 95.45 %), U = k * u_c
#
# Divisores habituales por PDF:
#   normal (u dada)      -> 1
#   normal (U, k=2)      -> 2
#   rectangular (semiancho a) -> sqrt(3)
#   triangular (semiancho a)  -> sqrt(6)
#   arcoseno (semiancho a)    -> sqrt(2)
#
# Casos precargados:
#   1) Analizador O3 a 120 nmol/mol, presupuesto Tipo B con especificaciones del
#      fabricante (estilo Thermo 49i Table 1-1) — ejercicio M4.
#   2) Patrón de transferencia comparado contra referencia — taller M7.
#   3) Self-test: presupuesto tipo EN 14625 (laboratorio, 120 nmol/mol).
#      Los VALORES POR COMPONENTE son una reconstrucción didáctica
#      (la fuente secundaria del curso solo reporta los totales:
#      u_c = 4.3 nmol/mol, W = 7.1 % con k = 2). El test comprueba la
#      maquinaria de combinación y que el total reproduzca 4.3 ± 0.1.
# ---------------------------------------------------------------------------

DIVISORES <- c(normal_u = 1, normal_U_k2 = 2,
               rectangular = sqrt(3), triangular = sqrt(6),
               arcoseno = sqrt(2))

# componente: data.frame(componente, descripcion, valor, pdf, ci, unidad, gl)
#   valor = semiancho / U / u según pdf ; ci = coeficiente de sensibilidad
#   gl = grados de libertad (Inf para Tipo B "bien conocidos")
presupuesto <- function(tabla, y_nominal = NA, nivel_confianza = 0.9545) {
  stopifnot(all(tabla$pdf %in% names(DIVISORES)))
  tabla$divisor <- DIVISORES[tabla$pdf]
  tabla$u       <- tabla$valor / tabla$divisor
  tabla$u_i     <- abs(tabla$ci) * tabla$u
  u_c  <- sqrt(sum(tabla$u_i^2))
  tabla$var_pct <- 100 * tabla$u_i^2 / u_c^2
  tabla$ranking <- rank(-tabla$var_pct, ties.method = "min")

  # Welch–Satterthwaite
  nu_eff <- u_c^4 / sum(tabla$u_i^4 / tabla$gl)
  k <- if (is.finite(nu_eff)) qt((1 + nivel_confianza) / 2, nu_eff) else
       qnorm((1 + nivel_confianza) / 2)
  U <- k * u_c

  list(tabla = tabla[order(tabla$ranking), ],
       u_c = u_c, nu_eff = nu_eff, k = k, U = U,
       W_pct = if (!is.na(y_nominal)) 100 * U / y_nominal else NA)
}

imprimir <- function(p, titulo, unidad = "nmol/mol") {
  cat("\n==", titulo, "==\n")
  t <- p$tabla
  cat(sprintf("%-28s %10s %-12s %7s %8s %8s %6s %4s\n",
              "componente", "valor", "PDF", "divisor", "u", "u_i(y)", "var%", "rk"))
  for (i in seq_len(nrow(t)))
    cat(sprintf("%-28s %10.4g %-12s %7.3f %8.4g %8.4g %6.1f %4d\n",
                t$componente[i], t$valor[i], t$pdf[i], t$divisor[i],
                t$u[i], t$u_i[i], t$var_pct[i], t$ranking[i]))
  cat(sprintf("u_c = %.3g %s | nu_eff = %.3g | k = %.3f | U = %.3g %s",
              p$u_c, unidad, p$nu_eff, p$k, p$U, unidad))
  if (!is.na(p$W_pct)) cat(sprintf(" | W = %.1f %%", p$W_pct))
  cat("\n")
}

fila <- function(componente, descripcion, valor, pdf, ci = 1, gl = Inf)
  data.frame(componente, descripcion, valor, pdf, ci, gl,
             stringsAsFactors = FALSE)

# ---------------------------------------------------------------------------
# CASO 1 — Analizador O3 a 120 nmol/mol (Tipo B, especificaciones del fabricante, M4)
# Especificaciones estilo Thermo 49i Table 1-1: ruido 0.25 ppb RMS (u directa),
# deriva cero <1 ppb/24 h, deriva span <1 %/24 h, linealidad ±1 % FS
# (FS = 200 ppb), exactitud P ±(interpretada 0.3 kPa -> efecto 0.36 ppb),
# resolución 0.1 ppb. Certificado de calibración U = 1.8 ppb (k = 2).
# ---------------------------------------------------------------------------
caso1 <- rbind(
  fila("ruido (RMS)",          "spec 0.25 ppb RMS, tratada como u",  0.25, "normal_u"),
  fila("deriva cero 24h",      "spec <1 ppb, rectangular",           1.0,  "rectangular"),
  # NOTA didactica: Table 1-1 del 49i especifica deriva de span <1 %/MES;
  # el valor 24 h de esta fila es un SUPUESTO para el ejercicio de auditoria
  # (M4). Presion, resolucion y certificado tampoco provienen de Table 1-1:
  # son entradas ilustrativas que el participante debe cuestionar.
  fila("deriva span 24h",      "SUPUESTO 1% de 120 ppb (spec real: 1%/mes)", 1.2, "rectangular"),
  fila("linealidad",           "±1% FS (200 ppb), rectangular",      2.0,  "rectangular"),
  fila("efecto presion",       "0.36 ppb equivalente, SUPUESTO",     0.36, "rectangular"),
  fila("resolucion",           "0.1 ppb, rectangular (semiancho/2)", 0.05, "rectangular"),
  fila("certificado calibr.",  "U = 1.8 ppb, k = 2, SUPUESTO",       1.8,  "normal_U_k2")
)
p1 <- presupuesto(caso1, y_nominal = 120)
imprimir(p1, "Caso 1: analizador O3 @ 120 nmol/mol (Tipo B, M4)", "ppb")

# ---------------------------------------------------------------------------
# CASO 2 — Patrón de transferencia vs referencia (taller M7)
# Componentes tipo BIPM.QM-K1 App.1: repetibilidad (Tipo A, gl = n-1),
# certificado de la referencia, falta de ajuste de la regresión,
# deriva entre verificaciones, aire cero.
# Nivel: 100 nmol/mol.
# ---------------------------------------------------------------------------
caso2 <- rbind(
  fila("repetibilidad",        "s de 3 ciclos (Tipo A)",             0.42, "normal_u", gl = 2),
  fila("certificado referencia","U(X)=0.5+0.01X ppb @100 -> 1.5, k=2",1.5, "normal_U_k2"),
  fila("falta de ajuste",      "residuo max regresion, rectangular", 0.6,  "rectangular"),
  fila("deriva entre verif.",  "cambio pendiente*nivel, rectangular",0.5,  "rectangular"),
  fila("aire cero",            "impureza <=1 ppb, rectangular",      1.0,  "rectangular")
)
p2 <- presupuesto(caso2, y_nominal = 100)
imprimir(p2, "Caso 2: patron de transferencia @ 100 nmol/mol (M7)", "ppb")

# ---------------------------------------------------------------------------
# CASO 3 — Self-test: presupuesto tipo EN 14625 laboratorio @ 120 nmol/mol.
# Valores por componente = reconstruccion didactica (ilustrativos).
# Totales de referencia (fuente secundaria): u_c = 4.3 nmol/mol, W = 7.1 %.
# ---------------------------------------------------------------------------
caso3 <- rbind(
  fila("u_r,z  repetib. cero",   "Tipo A",                    0.30, "normal_u", gl = 19),
  fila("u_r,lh repetib. 120",    "Tipo A",                    0.60, "normal_u", gl = 19),
  fila("u_l,lh falta de ajuste", "r_max=1.8% -> 1.8%*120/sqrt3 (valor=semiancho)", 2.16, "rectangular"),
  fila("u_gp   presion muestra", "influencia",                0.80, "normal_u"),
  fila("u_gt   temp. muestra",   "influencia",                0.70, "normal_u"),
  fila("u_st   temp. entorno",   "influencia",                0.50, "normal_u"),
  fila("u_V    tension",         "influencia",                0.30, "normal_u"),
  fila("u_H2O  vapor de agua",   "interferente positivo",     1.50, "normal_u"),
  fila("u_int  tolueno/xileno",  "interferentes",             1.00, "normal_u"),
  fila("u_av   promediado",      "efecto de promediado",      0.60, "normal_u"),
  fila("u_dsc  puertos",         "muestra vs calibracion",    0.50, "normal_u"),
  fila("u_cg   gas de calibr.",  "patron de calibracion",     3.34, "normal_u")
)
p3 <- presupuesto(caso3, y_nominal = 120)
imprimir(p3, "Caso 3 (self-test): EN 14625 laboratorio @ 120 nmol/mol")

# --- verificaciones ---------------------------------------------------------
chk <- function(nombre, cond) {
  cat(sprintf("[%s] %s\n", if (cond) "OK" else "FALLA", nombre))
  if (!cond) quit(status = 1)
}
# maquinaria: quadratura a mano de caso 3
u_manual <- sqrt(sum((abs(caso3$ci) * caso3$valor / DIVISORES[caso3$pdf])^2))
chk("quadratura coincide con calculo manual", abs(p3$u_c - u_manual) < 1e-12)
chk("u_c EN 14625 lab = 4.3 +/- 0.1 nmol/mol", abs(p3$u_c - 4.3) < 0.1)
chk("W = 7.1 +/- 0.3 %", abs(p3$W_pct - 7.1) < 0.3)

# exportar plantilla vacia + casos a CSV (base del xlsx posterior)
dir_out <- dirname(sub("--file=", "", grep("--file=", commandArgs(FALSE), value = TRUE)[1]))
if (is.na(dir_out) || dir_out == "") dir_out <- "."
write.csv(rbind(cbind(caso = "analizador_M4", caso1),
                cbind(caso = "patron_M7", caso2),
                cbind(caso = "en14625_lab_selftest", caso3)),
          file.path(dir_out, "plantilla_presupuesto_casos.csv"), row.names = FALSE)
cat("Escrito: plantilla_presupuesto_casos.csv\n")
