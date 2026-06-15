- # Registro Semanal — Semana 2026-W14 (30 mar – 5 abr)
  type:: weekly-review
  project:: [[CALAIRE-EA]]

- ## Resumen Ejecutivo
  - Semana de cierre técnico del pipeline de validación tripartita. Se completó la implementación y validación de las 5 fases estadísticas (robust stats, homogeneidad, estabilidad, incertidumbres, puntajes) con convergencia entre tres fuentes independientes de cálculo.

- ## Reportable (Hitos y Entregables)
  - **Implementación del pipeline de validación tripartita POC (GPT53CDX):** pipeline integrando app.R/ptcalc, script R puro y script Python stdlib-only. Genera 5 workbooks Excel con estructura ÍNDICE + 15 hojas + RESUMEN.
    date:: 2026-03-30
    category:: [[Desarrollo Técnico]]
    status:: completed
  - **Fase 2 — Homogeneidad validada:** cálculos de homogeneidad convergen dentro de tolerancias entre las tres fuentes independientes.
    date:: 2026-03-31
    category:: [[Desarrollo Técnico]]
    status:: completed
  - **Fase 3 — Estabilidad validada:** incertidumbre de estabilidad `u_stab = d_max / sqrt(3)` aplica de forma incondicional con resultados consistentes.
    date:: 2026-03-31
    category:: [[Desarrollo Técnico]]
    status:: completed
  - **Fase 4 — Cadena de incertidumbres:** propagación en cuadratura de `u_hom`, `u_stab`, `u_xpt_def` y `U_xpt` reproducible entre R y Python.
    date:: 2026-03-31
    category:: [[Desarrollo Técnico]]
    status:: completed
  - **Fase 5 — Puntajes de desempeño:** validación de z, z', ζ y En con convergencia tripartita.
    date:: 2026-03-31
    category:: [[Desarrollo Técnico]]
    status:: completed

- ## Insight (Conocimiento Adquirido)
  - **Tolerancias adaptativas R↔Python:** un umbral global único (`1e-12`) es inadecuado para comparaciones R↔Python debido a diferencias numéricas inherentes en cuantiles y redondeo. Se requieren umbrales diferenciados por tipo de estadístico.
    date:: 2026-03-30
    category:: [[Desarrollo Técnico]]
  - **Decisiones de diseño estadístico consolidadas:** (1) `u_stab = d_max / sqrt(3)` incondicional, (2) `ALGO_A_TOL = 1e-04`, (3) puntajes NA para concentración cero, (4) tolerancias adaptativas por sección.
    date:: 2026-03-30
    category:: [[Desarrollo Técnico]]

- ## Internal (Trabajo de Desarrollo/PL)
  - **Diagnóstico de 4446 FAILs iniciales:** análisis de causa raíz determinó que la tolerancia `1e-12` era excesivamente estricta. #internal
    date:: 2026-03-30
    category:: [[Desarrollo Técnico]]

- ## Referencias
  - [[CALAIRE-APP]]
  - [[Desarrollo Técnico]]
  - [[CALAIRE-EA]]
