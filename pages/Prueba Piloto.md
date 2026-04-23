- tags:: [[MOC]], [[Operation]]
- # Coordinacion Prueba Piloto (Marzo-Mayo 2026) - Febrero cancelado por preparación de autoridades ambientales para contingencias de marzo
- **Cronograma General**
	- Inicio: 2026-04-22
	- Fin: 2026-05-04
	- 2 rondas activas de prueba piloto en planificación operativa
- **Tareas Urgentes**
	- DONE Actualizacion de cartas de invitacion y calendario
	  project:: [[CALAIRE-EA]]
	  deadline:: 2026-02-10
	- TODO Confirmacion final de disponibilidad de [[SIATA]] y [[Universidad Pontificia Bolivariana]]
	  project:: [[CALAIRE-EA]]
	  priority:: high
	  deadline:: 2026-04-10
	- DONE Ajuste de fechas por auditoria CALAIRE (semanas 1-2 marzo)
	  project:: [[CALAIRE-EA]]
	- TODO Cerrar secuenciacion final entre ronda simple y ronda doble
	  project:: [[CALAIRE-EA]]
	  priority:: high
	- TODO Planificar y alistar prueba piloto (encendido, estabilizacion, calibracion multipunto, calibrador nuevo)
	  project:: [[CALAIRE-EA]]
	- TODO Preparar presentacion para participantes y resolver dudas
	  project:: [[CALAIRE-EA]]
	- TODO Planificar revision documental SGC
	  project:: [[CALAIRE-EA]]
	- TODO Seguimiento a licitacion publica (info solicitada por Luz)
	  project:: [[CALAIRE-EA]]
	- TODO Preparar logistica equipos (recepcion/devolucion)
	  project:: [[CALAIRE-EA]]
	  deadline:: 2026-04-15
- **Rondas**
	- [[Ronda 7]] (Apr 22-27) - Ronda simple CO/SO2 para [[SIATA]]
	- [[Ronda 8]] (Apr 29-May 4) - Ronda doble O3, NO, NO2 para [[SIATA]] y [[Universidad Pontificia Bolivariana]]
- **Confirmaciones de Laboratorios**
	- [[SIATA]] :: Definido como P1 para las dos rondas activas del piloto
	- [[Universidad Pontificia Bolivariana]] :: Definida como P2 para la ronda doble O3, NO, NO2
- **Logística**
	- Equipos a transportar: Analizadores CO, NOx, SO2, O3.
	- Responsable transporte: por confirmar en plan operativo de recepción y devolución
	- [[Inducción SST Persona Natural]] :: requisito administrativo para contratistas persona natural antes del ingreso a instalaciones de la Universidad Nacional Sede Medellín. Incluye curso SST persona natural, descarga de certificado aprobado y diligenciamiento del permiso de ingreso institucional.
- **Portal Web de Rondas**
	- Aplicación calaire-app (Next.js 16 + WorkOS + Supabase) operativa en entorno local desde 2026-04-21.
	- Dashboard coordinador: creación de rondas, asignación de participantes por token, visualización de resultados.
	- Formulario participante: entrada de datos con auto-save, cierre formal con bloqueo post-envío.
	- Panel laboratorio de referencia: interfaz diferenciada con badge violeta.
	- Integración con [[CALAIRE-APP]] (pt_app): exportación CSV compatible con `summary_n13.csv` (plan diseñado, implementación pendiente).
	- Deploy Vercel: **pendiente**.
- **Documentación SGC Operativa**
	- F-PSEA-06 (Plan de Ronda EA): draft operativo completado para ronda simple, 4 auditorías cruzadas ejecutadas, dictamen `no_aprobable` por inconsistencia σ_pt interdocumental. Backlog C4-01 a C4-04 definido.
	- I-PSEA-09 (Instrucciones a Participantes): skeleton con 3 brechas identificadas.
	- Decisión σ_pt: enfoque post-ronda adoptado (fitness-for-purpose, fórmula JRC-ERLAP).
- **Referencias de planificación**
	- [[SIATA]]
	- [[Universidad Pontificia Bolivariana]]
	- [[Ronda 7]]
	- [[Ronda 8]]
	- [[Inducción SST Persona Natural]]
	- [[CALAIRE-APP]]
	- [[QMS]]
	- [[docs/auxiliares/formulario_codex/diseno_workos_rondas_participantes.md]]
- ## Tags de Correo Asociados
	- `[[Seguimiento - Entregable]]`
	- `[[Seguimiento - Report]]`
	- `[[Seguimiento - Riesgo/Problema]]`
	- `[[Seguimiento - Entregable - Técnico]]`
	- `[[TECH] Ronda Piloto]`
	- `[[TECH] Ronda - Confirmación Lab]`
	- `[[TECH] Ronda - Equipos]`
	- `[[Reunión - Interna]]`
	- `[[EVENTO] Taller]`
