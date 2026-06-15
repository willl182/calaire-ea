- # Registro Semanal — Semana 2026-W11 (9 mar – 15 mar)
  type:: weekly-review
  project:: [[CALAIRE-EA]]

- ## Resumen Ejecutivo
  - Semana de implementación estadística intensiva. Se completaron 9 correcciones críticas en el motor ptcalc (H1-H9), se consolidó el plan de ajustes final y se formalizó el plan de validación cruzada tripartita para el Algoritmo A.

- ## Reportable (Hitos y Entregables)
  - **Consolidación de planes de ajuste CALAIRE-APP:** documento `docs/ajustes_app/final_opus.md` consolidado a partir de 8 planes generados por IA, con hallazgos H1-H9 estructurados por severidad y fase.
    date:: 2026-03-09
    category:: [[Desarrollo Técnico]]
    status:: completed
  - **Implementación de 9 correcciones estadísticas (H1-H9) en ptcalc:** correcciones completadas en ramas paralelas cubriendo errores de fórmulas ISO e inconsistencias de nomenclatura.
    date:: 2026-03-10
    category:: [[Desarrollo Técnico]]
    status:: completed
  - **Formalización del Plan de Validación Cruzada A2:** definición de validación para 15 combinaciones (5 contaminantes × 3 niveles) mediante pipeline tripartita (app.R, R puro, Python stdlib).
    date:: 2026-03-11
    category:: [[Desarrollo Técnico]]
    status:: completed
  - **Validación cruzada del Algoritmo A:** pruebas de consistencia matemática sobre `summary_n13` verificando convergencia de media robusta ($x^*$) y desviación estándar robusta ($s^*$).
    date:: 2026-03-12
    category:: [[Desarrollo Técnico]]
    status:: completed

- ## Insight (Conocimiento Adquirido)
  - **H1 — Corrección fórmula B.10:** la expresión `abs(s_x_bar_sq - sw_sq/m)` genera varianzas negativas espurias cuando la variabilidad intra-muestra domina. Debe reemplazarse por `max(0, s_x_bar_sq - (sw_sq/m))`.
    date:: 2026-03-10
    category:: [[Desarrollo Técnico]]
  - **H2 — Separación de MADe de homogeneidad:** el MADe calculado en homogeneidad evalúa variabilidad del material de referencia entre unidades, mientras que σ_pt define desviación estándar para evaluación del desempeño del participante. Son conceptos estadísticos independientes.
    date:: 2026-03-10
    category:: [[Desarrollo Técnico]]
  - **H4 — Umbral del Algoritmo A:** para `n < 12` el Algoritmo A robusto produce estimaciones inestables. El umbral mínimo debe ser `n ≥ 12`, usando estimadores robustos no iterativos (MADe o nIQR) para conjuntos pequeños.
    date:: 2026-03-10
    category:: [[Desarrollo Técnico]]
  - **Trazabilidad por serie (run):** los resultados deben cachearse indexados por `pollutant ‖ n_lab ‖ level ‖ run` para permitir análisis diferenciado entre réplicas sin recalcular.
    date:: 2026-03-10
    category:: [[Desarrollo Técnico]]

- ## Internal (Trabajo de Desarrollo/PL)
  - **Implementación técnica de correcciones en 3 archivos de ptcalc:** `pt_homogeneity.R`, `calculate_stability_stats()` y `funciones_finales.R`. #internal
    date:: 2026-03-10
    category:: [[Desarrollo Técnico]]

- ## Referencias
  - [[CALAIRE-APP]]
  - [[Desarrollo Técnico]]
  - [[QMS]]
