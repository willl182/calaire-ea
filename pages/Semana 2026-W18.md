- # Registro Semanal — Semana 2026-W18 (27 abr – 3 may)
  type:: weekly-review
  project:: [[CALAIRE-EA]]

- ## Resumen Ejecutivo
  - Semana de refinamiento UI/UX y estabilización del portal web calaire-app. Se implementaron identificadores anónimos, se unificó el sistema visual del dashboard, se flexibilizaron flujos del participante y se habilitó compilación offline para entornos sandbox.

- ## Reportable (Hitos y Entregables)
  - **Rediseño de PT y flujo del participante:** grilla editable `PTLevelsBulkForm.tsx` con inserción dinámica de filas, acceso a Ficha de Registro en estado borrador y header de navegación del participante.
    date:: 2026-04-28
    category:: [[Desarrollo Técnico]]
    status:: completed
  - **Unificación visual del Dashboard:** layouts estandarizados (`max-w-7xl` para tablas, `max-w-3xl` para formularios), navegación contextual `RondaContextNav` con breadcrumbs, secuencia de pestañas basada en ciclo de trabajo.
    date:: 2026-04-29
    category:: [[Desarrollo Técnico]]
    status:: completed
  - **Sistema de identificadores anónimos:** `participantCode` de 6 caracteres con alfabeto restringido para evitar confusión visual. Inserción transaccional en alta y mutación `backfillParticipantCodes`.
    date:: 2026-04-30
    category:: [[Desarrollo Técnico]]
    status:: completed
  - **Compilación offline:** ajuste para ejecución en sandbox con pilas locales y dependencias offline (`@workos-inc/node`).
    date:: 2026-04-30
    category:: [[Desarrollo Técnico]]
    status:: completed

- ## Internal (Trabajo de Desarrollo/PL)
  - **Protección de exportación CSV con código 409:** bloqueo de descarga si existen registros con códigos vacíos o inconsistentes. #internal
    date:: 2026-04-30
    category:: [[Desarrollo Técnico]]

- ## Referencias
  - [[CALAIRE-APP]]
  - [[Prueba Piloto]]
