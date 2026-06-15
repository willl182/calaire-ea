- # Registro Semanal — Semana 2026-W17 (20 abr – 26 abr)
  type:: weekly-review
  project:: [[CALAIRE-EA]]

- ## Resumen Ejecutivo
  - Semana de producción técnica masiva. Se consolidó el proceso de inducción SST, se aprobó e implementó el plan de cifras significativas ISO en ptcalc, se completó el portal web calaire-app (etapas 1-6) con arquitectura Next.js + WorkOS + Supabase, y se ejecutó la migración a Convex con 11 tablas y backend transaccional reescrito.

- ## Reportable (Hitos y Entregables)
  - **Consolidación del proceso de Inducción SST Persona Natural:** flujo operativo de 3 etapas (curso UNVirtual, certificado, permiso de ingreso) sistematizado como requisito previo obligatorio para personal externo en [[Prueba Piloto]].
    date:: 2026-04-20
    category:: [[Gestión Administrativa]]
    status:: completed
  - **Plan de integración de cifras significativas ISO en pt_app:** aprobado el plan de 6 fases para implementar cifras significativas conforme ISO 13528:2022.
    date:: 2026-04-20
    category:: [[Desarrollo Técnico]]
    status:: in_progress
  - **Implementación de Fases 1-4 de cifras significativas:** criterios de convergencia del Algoritmo A actualizados y formateo numérico reconfigurado en app.R.
    date:: 2026-04-20
    category:: [[Desarrollo Técnico]]
    status:: in_progress
  - **Portal web calaire-app — Etapa 1 (Setup base):** esquema SQL con 4 tablas relacionales en Supabase (rondas, ronda_contaminantes, ronda_participantes, envios).
    date:: 2026-04-21
    category:: [[Desarrollo Técnico]]
    status:: completed
  - **Portal web calaire-app — Etapa 2 (Dashboard coordinador):** panel administrativo con creación de rondas, configuración por contaminante y transiciones de estado del ciclo de vida.
    date:: 2026-04-21
    category:: [[Desarrollo Técnico]]
    status:: completed
  - **Portal web calaire-app — Etapa 3 (Gestión de participantes):** módulo de búsqueda, asignación, listado y eliminación de participantes por ronda. Modelo de invitación por tokens pre-generados.
    date:: 2026-04-21
    category:: [[Desarrollo Técnico]]
    status:: completed
  - **Portal web calaire-app — Etapa 4 (Formulario de captura y cierre):** formulario reactivo con progress bar, KPI cards y mecanismo de cierre inmutable vía `submitted_at`.
    date:: 2026-04-21
    category:: [[Desarrollo Técnico]]
    status:: completed
  - **Portal web calaire-app — Etapa 5 (Resultados y exportación CSV):** tabla consolidada de envíos y exportación CSV compatible con contrato `summary_n13.csv` de pt_app.
    date:: 2026-04-21
    category:: [[Desarrollo Técnico]]
    status:: completed
  - **Portal web calaire-app — Etapa 6 (Hardening y validación):** validaciones server-side, páginas de error dedicadas, resolución de gaps funcionales (creación WorkOS y vista personalizada participante).
    date:: 2026-04-21
    category:: [[Desarrollo Técnico]]
    status:: completed
  - **Deprecación de columna sample_group en ptcalc:** eliminación definitiva del campo legacy del contrato de datos de entrada de ptcalc. Bump a v0.1.1, limpieza de CSVs, actualización de documentación.
    date:: 2026-04-22
    category:: [[Desarrollo Técnico]]
    status:: completed
  - **Digitalización de Ficha de Registro F-PSEA-05A:** 4 tablas en Supabase con RLS, auto-guardado onBlur y migración de `envios_pt` a columnas numéricas.
    date:: 2026-04-23
    category:: [[Desarrollo Técnico]]
    status:: completed
  - **Puesta en producción inicial de calaire-app:** despliegue en Vercel con gestión de variables de entorno y callbacks de AuthKit WorkOS.
    date:: 2026-04-24
    category:: [[Desarrollo Técnico]]
    status:: completed

- ## Insight (Conocimiento Adquirido)
  - #decision Decisión de invitación sin correo automático: modelo de tokens pre-generados con enlaces manuales. Elimina dependencia de servicios de correo transaccional y mantiene control operativo en manos del coordinador.
    date:: 2026-04-21
    category:: [[Desarrollo Técnico]]
  - #decision Decisión de cierre con `submitted_at`: no se crea tabla separada de submissions. La marca temporal en `envios` cumple doble función de trazabilidad y bloqueo post-envío, reduciendo complejidad del esquema.
    date:: 2026-04-21
    category:: [[Desarrollo Técnico]]
  - **Arquitectura de preprocesamiento pt_app:** el procesamiento pesado de datos crudos (limpieza, agregación, incertidumbre) se ejecutará offline en R (`pt_app` y `ptcalc`), dejando a `calaire-app` como portal transaccional ligero.
    date:: 2026-04-24
    category:: [[Desarrollo Técnico]]
  - **Corrección de `uncertainty_std`:** la incertidumbre reportada por participantes es estándar ($u_{xi}$), no expandida. Se corrigió el mapeo erróneo que la trataba como expandida.
    date:: 2026-04-24
    category:: [[Desarrollo Técnico]]
  - #decision Decisión WorkOS sin organización: `auth.role` siempre retorna `null`. Los perfiles se gestionan exclusivamente por `participant_profile` en Supabase, simplificando gestión de acceso.
    date:: 2026-04-22
    category:: [[Desarrollo Técnico]]

- ## Internal (Trabajo de Desarrollo/PL)
  - **Sistema de diseño "Institutional Gold":** implementación de paleta dorada (`#FDB913`) con CSS puro, clases `.card`, `.card-accent`, `.header-bar`, `.btn-primary`. #internal
    date:: 2026-04-21
    category:: [[Desarrollo Técnico]]
  - **Integración del logo UNAL:** componente `LogoUnal.tsx` con `next/image` y optimización LCP. #internal
    date:: 2026-04-21
    category:: [[Desarrollo Técnico]]
  - **Implementación de autenticación multi-proveedor:** Email OTP (Magic Auth) activado en WorkOS para universidades con Azure AD bloqueante. #internal
    date:: 2026-04-22
    category:: [[Desarrollo Técnico]]
  - **Panel de laboratorio de referencia:** componente `FormularioReferencia.tsx` con badge violeta y bifurcación por `participant_profile === 'member_special'`. #internal
    date:: 2026-04-22
    category:: [[Desarrollo Técnico]]
  - **Migración Supabase → Convex:** 11 tablas, 24 índices, reescritura total de capa de acceso en `lib/rondas.ts` y `lib/fichas.ts`. #internal
    date:: 2026-04-26
    category:: [[Desarrollo Técnico]]

- ## Referencias
  - [[CALAIRE-APP]]
  - [[Prueba Piloto]]
  - [[Desarrollo Técnico]]
  - [[QMS]]
