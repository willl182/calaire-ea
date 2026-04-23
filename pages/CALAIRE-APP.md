- tags:: [[MOC]], [[Software]]
- # CALAIRE-APP: Ecosistema de Software del Programa de EA
- **Visión General**
	- El ecosistema de software de [[CALAIRE-EA]] comprende dos aplicaciones complementarias: el motor estadístico (pt_app + ptcalc) para procesamiento ISO 13528:2022, y el portal web (calaire-app) para la gestión operativa de rondas de ensayo de aptitud. Ambas aplicaciones comparten la identidad visual "Institutional Gold" (`#FDB913`) y están integradas mediante un contrato de datos CSV.
- **Motor Estadístico: pt_app + ptcalc**
	- status:: operativo
	- repo:: `/home/w182/w421/pt_app`
	- deploy:: `https://w421.shinyapps.io/pt_app/`
	- **Stack técnico**
		- Lenguaje: R 4.1.0+ (Shiny)
		- Paquete interno: ptcalc v0.1.1
		- Normativa: ISO 13528:2022, ISO 17043:2023
	- **Capacidades validadas**
		- Algoritmo A robusto (corregido: `max(0,...)`, umbral `n ≥ 12`, convergencia `ALGO_A_TOL = 1e-04`)
		- Cadena completa: Homogeneidad → Estabilidad → Incertidumbres (`u_hom`, `u_stab`, `u_xpt_def`, `U_xpt`) → Puntajes (z, z', ζ, En)
		- Trazabilidad por serie (`pollutant ‖ n_lab ‖ level ‖ run`)
		- Pipeline de validación tripartita: APP / R puro / Python stdlib (15 combinaciones × 5 workbooks)
	- **Correcciones aplicadas (H1–H9)**
		- H1: Fórmula B.10 — `abs()` → `max(0,...)`
		- H2: MADe separado — `MADe_hom`/`sigma_pt_hom` diferenciado de σ_pt de puntajes
		- H4: Umbral Algoritmo A — `n ≥ 3` → `n ≥ 12` (ISO 13528:2022 §9.4)
		- Deprecación `sample_group` — columna eliminada del contrato (ptcalc v0.1.1)
	- **Pendientes**
		- TODO Completar Fases 5-6 cifras significativas (tests + validación cruzada)
		  project:: [[CALAIRE-APP]]
		  priority:: high
		- TODO Ejecutar `devtools::document()` para ptcalc
		  project:: [[CALAIRE-APP]]
		- TODO Corregir 3 FAILs pre-existentes en `test_04_puntajes.R`
		  project:: [[CALAIRE-APP]]
- **Portal Web: calaire-app**
	- status:: operativo-local
	- repo:: `/home/w182/w421/calaire-app`
	- deploy:: pendiente (Vercel)
	- **Stack técnico**
		- Frontend/Backend: Next.js 16 (App Router, Server Components, Server Actions)
		- Autenticación: WorkOS (Email OTP / Magic Auth)
		- Base de datos: Supabase (PostgreSQL)
		- Identidad visual: CSS vars "Institutional Gold" — unificada con pt_app
	- **Funcionalidades completadas (2026-04-21/22)**
		- Dashboard coordinador: rondas CRUD + transiciones de estado + contaminantes
		- Gestión participantes: búsqueda WorkOS, invitación por token, creación de usuarios
		- Formulario participante: auto-save (debounce 1500ms), cierre formal con `submitted_at`, modo solo lectura post-envío
		- Panel laboratorio de referencia: `FormularioReferencia.tsx` con badge violeta, bifurcación por `participant_profile`
		- Resultados + exportación CSV
		- Autenticación multi-proveedor (Email OTP para universidades con Azure AD bloqueado)
	- **Modelo de datos (Supabase)**
		- `rondas` → `ronda_contaminantes` + `ronda_participantes` → `envios`
		- Roles vía `participant_profile` en Supabase (no WorkOS `auth.role`)
	- **Pendientes**
		- TODO Deploy calaire-app en Vercel
		  project:: [[CALAIRE-APP]]
		  priority:: high
		- TODO Ejecutar migración `db/migrate_envios_pt_nuevos_campos.sql` en Supabase
		  project:: [[CALAIRE-APP]]
		  priority:: high
		- TODO Rotación de secretos (WORKOS_API_KEY, SUPABASE_SERVICE_ROLE_KEY)
		  project:: [[CALAIRE-APP]]
		  priority:: high
		- TODO Implementar exportación CSV compatible con pt_app (`summary_n13.csv`)
		  project:: [[CALAIRE-APP]]
		- TODO Smoke test flujo laboratorio de referencia (OTP → token → badge violeta)
		  project:: [[CALAIRE-APP]]
- **Integración pt_app ↔ calaire-app**
	- Contrato de datos: `summary_n13.csv` (7 columnas: `lab_code`, `pollutant`, `level`, `run`, `rep`, `result`, `unit`)
	- Flujo: Participante ingresa datos (calaire-app) → Exportación CSV (admin) → pt_app procesa estadísticas → Informe de resultados
	- Estado: Plan diseñado, implementación pendiente
- **Origen Contractual**
	- Contrato paralelo de desarrollo: Invitación Directa M-1256 (2025).
	- Desarrollo ejecutado por [[Wilson Salas]].
	- Carpeta de soporte: `docs/contrato_app/`.
	- Cierre contractual de desarrollo: Diciembre 2025.
- **Ver También**
	- [[CALAIRE-EA]]
	- [[Prueba Piloto]]
	- [[QMS]]
	- [[Desarrollo Técnico]]
