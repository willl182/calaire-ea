- # Registro Semanal — Semana 2026-W21 (18 may – 24 may)
  type:: weekly-review
  project:: [[CALAIRE-EA]]

- ## Resumen Ejecutivo
  - Semana de correcciones metrológicas críticas, consolidación documental y diseño de infraestructura de skills para reconstrucción de historial. Se determinó que $U_{exp}$ es entrada manual (no auto-calculada), se reestructuró la documentación del SGC en dos bloques canónicos y se diseñó el skill `work-history-rebuild`.

- ## Reportable (Hitos y Entregables)
  - **Corrección metrológica del factor k y campo manual de incertidumbre:** la Incertidumbre Expandida $U(x)_{exp}$ se determinó como entrada manual, no auto-calculada con $u(x) \times k$. Columna `k` añadida al esquema `enviosPt`, con inputs para `k individual` y `k grupal` en formularios de participantes y referencia.
    date:: 2026-05-19
    category:: [[Desarrollo Técnico]]
    status:: completed
  - **Guía del Procedimiento v1.1:** definición de roles explícitos: `[PARTICIPANTE - AUTÓNOMO]`, `[PARTICIPANTE - CARGA EN APLICATIVO]`, `[CALAIRE - CONFIGURACIÓN]`, `[CALAIRE - PROCESAMIENTO INTERNO]`, `[CALAIRE - VALIDACIÓN]`, `[CALAIRE - NO DIVULGAR]` y `[COMÚN]`.
    date:: 2026-05-19
    category:: [[Desarrollo Técnico]]
    status:: completed
  - **Flujo definitivo de preprocesamiento:** documentación en `docs/workflow-preprocesamiento.md` y script wrapper `scripts/consolidar_ronda_pt_app.R` con modos `participants`, `reference`, `all`.
    date:: 2026-05-19
    category:: [[Desarrollo Técnico]]
    status:: completed
  - **Panel de resultados y edición avanzada de estructura de ronda:** pestaña unificada de Resultados globales con desglose interactivo. UI robusta para reconfigurar contaminantes, niveles y réplicas en rondas activas sin envíos confirmados.
    date:: 2026-05-21
    category:: [[Desarrollo Técnico]]
    status:: completed
  - **Guía del Participante:** documento `guia-ppt-agy-cld.md` (31 KB) con instrucciones de navegación y carga basadas estrictamente en la interfaz de la aplicación.
    date:: 2026-05-21
    category:: [[Desarrollo Técnico]]
    status:: completed
  - **Consolidación de documentación SGC y Prueba Piloto:** reorganización en `docs/documentacion_sgc/01_bloque_general/` (gobernanza) y `docs/documentacion_sgc/02_bloque_operativo/` (procedimientos e instructivos).
    date:: 2026-05-22
    category:: [[Actualizaciones de Documentación]]
    status:: completed

- ## Insight (Conocimiento Adquirido)
  - **$U_{exp}$ es entrada manual, no auto-calculada:** se determinó que la Incertidumbre Expandida reportada por participantes debe ingresarse manualmente y no derivarse automáticamente de $u(x) \times k$.
    date:: 2026-05-19
    category:: [[Desarrollo Técnico]]

- ## Internal (Trabajo de Desarrollo/PL)
  - **Edición administrativa absoluta — bypass de bloqueos por estado:** mutaciones y Server Actions para edición forzada desde rol coordinador, independientemente de envío o cierre de ronda. Sub-dashboard dedicado para corrección de mediciones cargadas. #internal
    date:: 2026-05-20
    category:: [[Desarrollo Técnico]]
  - **Eliminación de redirección forzada a Configuración PT:** se permitió agregar/modificar participantes sin niveles declarados previamente. #internal
    date:: 2026-05-20
    category:: [[Desarrollo Técnico]]
  - **Skill de reconstrucción de historial de trabajo (`work-history-rebuild`):** diseño de 4 fases (creación del skill, recolección paralela con 4 subagentes, síntesis de hallazgos, generación de journals). #internal
    date:: 2026-05-22
    category:: [[Desarrollo Técnico]]

- ## Referencias
  - [[CALAIRE-APP]]
  - [[Prueba Piloto]]
  - [[QMS]]
  - [[CALAIRE-EA]]
