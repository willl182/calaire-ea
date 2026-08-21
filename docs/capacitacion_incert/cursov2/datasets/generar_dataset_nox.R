#!/usr/bin/env Rscript
# Genera datos sintéticos para M6 — NO/NO2/NOx por quimioluminiscencia.
# Semilla fija: 20260819. No representa desempeño de equipo comercial.

set.seed(20260819)

out_dir <- dirname(sub("--file=", "", grep("--file=", commandArgs(FALSE), value = TRUE)[1]))
if (is.na(out_dir) || out_dir == "") out_dir <- "."

niveles <- c(0, 40, 80, 120, 150)
filas <- list()
t0 <- as.POSIXct("2026-08-19 08:00:00", tz = "UTC")
idx <- 0

for (ciclo in 1:3) {
  for (nivel in niveles) {
    idx <- idx + 1
    flujo_no <- if (nivel == 0) 0 else 40 + rnorm(1, 0, 0.10)
    flujo_dil <- 9.96 + rnorm(1, 0, 0.008)
    flujo_o3 <- if (nivel == 0) 0 else (nivel / 150) * 0.030 + rnorm(1, 0, 0.00015)
    no_cil <- 40.00
    no_generado <- if (nivel == 0) 0 else no_cil * 1000 * (flujo_no / 1000) / (flujo_dil + flujo_no / 1000)
    no2_gpt <- if (nivel == 0) 0 else nivel * (1 + rnorm(1, 0, 0.0015))
    no_remanente <- max(0, no_generado - no2_gpt)
    eta <- 0.972 - 0.0015 * (ciclo - 1)
    error_comun <- rnorm(1, 0, 0.28)
    lectura_no <- no_remanente + error_comun + rnorm(1, 0, 0.16)
    lectura_nox <- no_remanente + eta * no2_gpt + 0.35 + error_comun + rnorm(1, 0, 0.16)

    filas[[idx]] <- data.frame(
      ciclo = ciclo,
      nivel = if (nivel == 0) "cero" else sprintf("N%03d", nivel),
      timestamp = format(t0 + (ciclo - 1) * 86400 + (match(nivel, niveles) - 1) * 900,
                         "%Y-%m-%dT%H:%M:%SZ"),
      no_cilindro_umol_mol = no_cil,
      u_no_cilindro_umol_mol = 0.08,
      impureza_no2_nmol_mol = 0.40,
      flujo_no_ml_min = round(flujo_no, 3),
      u_flujo_no_ml_min = 0.08,
      flujo_dilucion_l_min = round(flujo_dil, 4),
      u_flujo_dilucion_l_min = 0.008,
      flujo_o3_l_min = round(max(0, flujo_o3), 5),
      u_flujo_o3_l_min = 0.00015,
      temperatura_K = round(298.15 + rnorm(1, 0, 0.18), 2),
      u_temperatura_K = 0.20,
      presion_kPa = round(101.325 + rnorm(1, 0, 0.08), 3),
      u_presion_kPa = 0.10,
      no_generado_nmol_mol = round(no_generado, 2),
      no2_gpt_nmol_mol = round(no2_gpt, 2),
      lectura_no_nmol_mol = round(lectura_no, 2),
      lectura_nox_nmol_mol = round(lectura_nox, 2),
      lectura_no2_nmol_mol = round(lectura_nox - lectura_no, 2),
      temperatura_convertidor_C = round(350 + rnorm(1, 0, 1.2), 1),
      presion_camara_kPa = round(48.0 + rnorm(1, 0, 0.18), 2),
      caudal_muestra_l_min = round(0.70 + rnorm(1, 0, 0.004), 3),
      observacion = if (nivel == 0) "cero de ciclo" else "GPT sintética"
    )
  }
}

gpt <- do.call(rbind, filas)
write.csv(gpt, file.path(out_dir, "dataset_nox_gpt_convertidor.csv"), row.names = FALSE, quote = TRUE)

linea <- data.frame(
  configuracion = c("A_corta", "B_larga", "C_larga_caliente"),
  longitud_m = c(2, 8, 8),
  diametro_interno_mm = c(4, 6, 6),
  volumen_interno_ml = c(25.13, 226.19, 226.19),
  caudal_l_min = c(1.00, 1.80, 1.55),
  tiempo_residencia_externo_s = c(1.51, 7.54, 8.76),
  tiempo_residencia_interno_s = c(1.50, 1.80, 1.80),
  tiempo_residencia_total_s = c(3.01, 9.34, 10.56),
  temperatura_C = c(22, 28, 35),
  no_entrada_nmol_mol = c(180, 180, 180),
  o3_entrada_nmol_mol = c(90, 90, 90),
  no2_entrada_nmol_mol = c(20, 20, 20),
  no2_formado_estimado_nmol_mol = c(0.18, 0.43, 0.62),
  cambio_relativo_pct = c(0.90, 2.15, 3.10),
  criterio_pct = c(2.00, 2.00, 2.00),
  decision_esperada = c("aceptar_y_vigilar", "reducir_residencia_y_repetir", "invalidar_hasta_corregir")
)
write.csv(linea, file.path(out_dir, "dataset_nox_linea_muestreo.csv"), row.names = FALSE, quote = TRUE)

for (ciclo_i in 1:3) {
  s <- gpt[gpt$ciclo == ciclo_i & gpt$nivel != "cero", ]
  ajuste <- lm(lectura_no2_nmol_mol ~ no2_gpt_nmol_mol, data = s)
  cat(sprintf("ciclo %d: intercepto %.3f; eficiencia %.4f\n",
              ciclo_i, coef(ajuste)[1], coef(ajuste)[2]))
}
cat("Escritos:", nrow(gpt), "filas GPT y", nrow(linea), "configuraciones de línea\n")
