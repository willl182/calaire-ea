- # Registro Semanal — Semana 2026-W20 (11 may – 17 may)
  type:: weekly-review
  project:: [[CALAIRE-EA]]

- ## Resumen Ejecutivo
  - Semana de validación estadística intensiva y refinamiento del motor de cálculo. Se ejecutó una campaña masiva de validación para O₃ con fórmulas nativas en Excel, se incorporó el Método de Laboratorios Expertos para estimar σ_pt y se refinó la UI de puntajes con renderizado MathJax/LaTeX.

- ## Reportable (Hitos y Entregables)
  - **Validación de cálculos en entorno dedicado validation_3 (O₃):** Etapa 1 exitosa para estadísticos robustos (Algoritmo A, MADe, nIQR). Etapa 2 validó homogeneidad simulada para O₃ en tres niveles.
    date:: 2026-05-12
    category:: [[Desarrollo Técnico]]
    status:: in_progress
  - **Validación masiva de O₃ con fórmulas nativas en Excel:** 9 fases de construcción de plantillas interactivas independientes cubriendo Estadísticos Robustos, Homogeneidad, Estabilidad, Cadena de Incertidumbre y Puntajes.
    date:: 2026-05-13
    category:: [[Desarrollo Técnico]]
    status:: completed
  - **Método de Laboratorios Expertos (Método 4):** integración de `calculate_expert_sigma_pt()` en la aplicación Shiny para estimar σ_pt sin alterar el modelo de datos.
    date:: 2026-05-13
    category:: [[Desarrollo Técnico]]
    status:: completed
  - **Bootstrap reproducible y refinamiento UI/UX de puntajes:** script `build_bootstrap_homogeneity_stability.R` con semilla fija `13528` y 200 iteraciones. Renderizado MathJax/LaTeX para fórmulas estadísticas en interfaz Shiny.
    date:: 2026-05-14
    category:: [[Desarrollo Técnico]]
    status:: completed
  - **Robustez del informe final, heatmap general y compatibilidad metrológica:** reescritura de plantilla `report_template.Rmd` con validaciones `is_nonempty_df()`, parámetro reactivo `report_participant` y corrección del heatmap global para visualización comparativa de todos los laboratorios.
    date:: 2026-05-15
    category:: [[Desarrollo Técnico]]
    status:: completed

- ## Insight (Conocimiento Adquirido)
  - **Bug en convergencia del Algoritmo A:** si el estimador robusto inicial $s^*_0$ por MADe es cero pero el conjunto tiene variación aritmética, el algoritmo debe sustituir $s^*_0$ por `stats::sd(values)` para evitar aborto del bucle.
    date:: 2026-05-13
    category:: [[Desarrollo Técnico]]

- ## Internal (Trabajo de Desarrollo/PL)
  - **Refinamiento UI/UX de puntajes y outliers:** integración de visualización explícita de σ_pt y renderizado LaTeX. #internal
    date:: 2026-05-14
    category:: [[Desarrollo Técnico]]
  - **Blindaje de plantilla de informes finales:** eliminación de supuestos obsoletos (participante fijo `"ref"`), renombrado de posicionales rígidos. #internal
    date:: 2026-05-15
    category:: [[Desarrollo Técnico]]

- ## Referencias
  - [[CALAIRE-APP]]
  - [[Prueba Piloto]]
