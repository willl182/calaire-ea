- # Registro Semanal — Semana 2026-W15 (6 abr – 12 abr)
  type:: weekly-review
  project:: [[CALAIRE-EA]]

- ## Resumen Ejecutivo
  - Semana de consolidación del Framework del SGC y desarrollo del formato operativo F-PSEA-06 para ronda simple. Se formalizó la arquitectura documental de 4 niveles, se completaron 4 fases de aterrizaje operativo del formato de plan de ronda y se documentaron decisiones metodológicas críticas sobre σ_pt.

- ## Reportable (Hitos y Entregables)
  - **Consolidación del Framework del SGC:** estructura jerárquica documental definida en 4 niveles (Manual de Calidad, Procedimientos, Instructivos, Formatos/Registros), alineada con ISO/IEC 17043:2023.
    date:: 2026-04-07
    category:: [[QMS]]
    status:: completed
  - **Diseño del plan de rondas piloto:** formalización de arquitectura documental para ronda simple (n=1, SIATA) y ronda compleja (n≥2, múltiples laboratorios).
    date:: 2026-04-07
    category:: [[Prueba Piloto]]
    status:: completed
  - **Fase 1 — Criterios de adaptación F-PSEA-06:** separación sistemática de contenido en aplicable directamente, adaptable y no trasladable.
    date:: 2026-04-10
    category:: [[QMS]]
    status:: completed
  - **Fase 2 — Formato operativo F-PSEA-06:** transformación de placeholder a formato de control pre-ronda con secciones de prerrequisitos, roles, custodia de ítems PT y cronograma operativo.
    date:: 2026-04-10
    category:: [[QMS]]
    status:: completed
  - **Fase 3 — Aterrizaje operativo ronda simple:** controles específicos para elegibilidad, logística, roles, custodia y trazabilidad.
    date:: 2026-04-10
    category:: [[QMS]]
    status:: completed
  - **Fase 4 — Depuración de placeholders:** inventario de campos `[POR DEFINIR]`; solo 16 campos genuinamente pendientes.
    date:: 2026-04-10
    category:: [[QMS]]
    status:: completed
  - **Sprint 2 de documentación SGC:** creación de skeletons I-PSEA-09, I-PSEA-10 y P-PSEA-10 con estructura normativa ISO 17043:2023.
    date:: 2026-04-08
    category:: [[QMS]]
    status:: completed

- ## Insight (Conocimiento Adquirido)
  - #decision Decisión de segregación documental operativa/gestión: separación estricta entre documentación de ejecución técnica y documentación de gobernanza del SGC, siguiendo la lógica de ISO 17043:2023 cláusulas 6-8 (operacional) vs. 9-10 (gestión).
    date:: 2026-04-07
    category:: [[QMS]]
  - #decision Decisión sobre σ_pt post-ronda: enfoque fitness-for-purpose con σ_pt = a · x_pt + b, coeficientes determinados a partir de datos recopilados en la ronda. Alineación con protocolo JRC-ERLAP.
    date:: 2026-04-10
    category:: [[Desarrollo Técnico]]
  - **Brechas en I-PSEA-09:** tres brechas críticas detectadas: (1) σ_pt sin metodología definida, (2) proceso de apelaciones no especificado, (3) criterios de elegibilidad pendientes.
    date:: 2026-04-08
    category:: [[QMS]]

- ## Internal (Trabajo de Desarrollo/PL)
  - **Auditoría de completitud F-PSEA-06:** 41 puntos de control en 5 dimensiones. Dictamen: operativamente utilizable, formalmente `no_aprobable` por inconsistencias en cadena de σ_pt. #internal
    date:: 2026-04-10
    category:: [[QMS]]
  - **Auditoría de coherencia interdocumental:** verificación entre F-PSEA-06, I-PSEA-07 e I-PSEA-09. Dictamen `no_aprobable` con 3 hallazgos críticos y backlog C4-01 a C4-04. #internal
    date:: 2026-04-10
    category:: [[QMS]]

- ## Referencias
  - [[QMS]]
  - [[Prueba Piloto]]
  - [[Desarrollo Técnico]]
  - [[CALAIRE-EA]]
