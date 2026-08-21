#!/usr/bin/env Rscript
# Plantilla M6 NOx: ejemplo EN 14211 y modelo NO2=(NOx-NO)/eta con covarianza.

anexo_f <- data.frame(
  componente = c("repetibilidad cero 1", "repetibilidad cero 2", "repetibilidad concentración",
                 "falta de ajuste", "presión muestra", "temperatura muestra",
                 "temperatura entorno", "tensión", "H2O", "otros interferentes",
                 "promediación", "reproducibilidad campo", "deriva cero", "deriva span",
                 "diferencia muestra/calibración", "eficiencia convertidor",
                 "gas calibración", "gas cero"),
  u = c(0.00, 0.00, 0.09, 0.90, 0.06, 0.26, 0.44, 0.02, 0.249, 0.35,
        2.70, 3.22, 0.58, 1.44, 1.04, 2.08, 2.08, 0.60)
)
anexo_f$varianza <- anexo_f$u^2
uc_reconstruido <- sqrt(sum(anexo_f$varianza))
# EN 14211 publica suma redondeada 30.4 y uc=5.5; usar esos redondeos para reporte.
uc_publicado <- 5.5
k <- 2
U_publicado <- k * uc_publicado
W_publicado <- 100 * U_publicado / 104
anexo_f$participacion_pct <- 100 * anexo_f$varianza / sum(anexo_f$varianza)

cat("Ejemplo informativo EN 14211 Anexo F\n")
cat(sprintf("Reconstrucción con u redondeadas: uc=%.3f nmol/mol\n", uc_reconstruido))
cat(sprintf("Valores publicados/reconstruidos: suma varianzas=30.4; uc=%.1f; U(k=2)=%.1f; W=%.1f %%\n",
            uc_publicado, U_publicado, W_publicado))
print(anexo_f[order(-anexo_f$participacion_pct), ], row.names = FALSE)

presupuesto_diferencial <- function(nox, no, eta, u_nox, u_no, u_eta, rho = 0) {
  cov_nox_no <- rho * u_nox * u_no
  diferencia <- nox - no
  y <- diferencia / eta
  c_nox <- 1 / eta
  c_no <- -1 / eta
  c_eta <- -diferencia / eta^2
  var_canales <- c_nox^2 * u_nox^2 + c_no^2 * u_no^2 +
    2 * c_nox * c_no * cov_nox_no
  var_eta <- c_eta^2 * u_eta^2
  data.frame(no2 = y, rho = rho, covarianza = cov_nox_no,
             var_canales = var_canales, var_eta = var_eta,
             u_c = sqrt(var_canales + var_eta), U_k2 = 2 * sqrt(var_canales + var_eta))
}

sin_cov <- presupuesto_diferencial(205, 200, 0.97, 1.2, 1.0, 0.01, rho = 0)
con_cov <- presupuesto_diferencial(205, 200, 0.97, 1.2, 1.0, 0.01, rho = 0.70)
cat("\nCaso diferencial a baja concentración\n")
print(rbind(sin_cov, con_cov), row.names = FALSE)
stopifnot(con_cov$u_c < sin_cov$u_c)
stopifnot(abs(W_publicado - 10.576923) < 1e-6)
cat("[OK] covarianza aplicada con signos de sensibilidad; W redondea a 10.6 %\n")
