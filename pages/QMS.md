- tags:: [[MOC]], [[Quality]]
- # Sistema de Gestión de Calidad (QMS)
	alias:: [[SGC / Calidad]]
- **Estándares**
	- [[ISO 17043]] - Requisitos generales para EA.
	- [[ISO 13528]] - Métodos estadísticos.
	- [[ISO 17025]] - Competencia laboratorios (CALAIRE base).
- **Framework Documental (4 niveles)**
	- Arquitectura jerárquica alineada a ISO/IEC 17043:2023, con segregación operativa/gestión:
	- **Nivel 1 — Manual de Calidad:** declaración de políticas y alcance del SGC del Proveedor de EA.
	- **Nivel 2 — Procedimientos:** procesos operativos y de gestión documentados.
		- P-PSEA-01: Protocolo General EA (operativo)
		- P-PSEA-09: Procedimiento de Planificación Ronda EA (operativo)
		- P-PSEA-10: Procedimiento de Manejo de Ítems PT (skeleton completo)
		- P-PSEA-20: Comunicación PT (skeleton)
		- P-PSEA-22: Reportes PT (skeleton)
	- **Nivel 3 — Instructivos:** instrucciones técnicas de trabajo (14 creados: I-PSEA-02 a I-PSEA-15).
		- I-PSEA-07: Diseño Estadístico (skeleton con criterios n=1 definidos)
		- I-PSEA-09: Instrucciones a Participantes (skeleton, 3 brechas identificadas)
		- I-PSEA-10: Homogeneidad y Estabilidad (skeleton)
	- **Nivel 4 — Formatos y registros:** 23 formatos creados (F-PSEA-01 a F-PSEA-23).
		- F-PSEA-05: Confirmación de Participación (formato)
		- F-PSEA-05A: Hoja de Registro del Participante (formato, versiones XLSX/MD)
		- F-PSEA-06: Plan de Ronda EA (draft operativo — ronda simple completado, 4 auditorías ejecutadas)
		- F-PSEA-07 a F-PSEA-23: Formatos operativos (skeletons)
- **Auditorías del F-PSEA-06**
	- Auditoría de completitud: 41 verificaciones en 5 dimensiones (A–E). Dictamen: operativamente utilizable, formalmente `no_aprobable`.
	- Auditoría de placeholders: 16+ campos `[POR DEFINIR]` inventariados (inferibles vs. no inferibles).
	- Auditoría de coherencia interdocumental: 3 hallazgos críticos (σ_pt interdocumental, hito T-3, I-PSEA-07 skeleton).
	- Línea base pre-corrección: 0 Blocking, 1 Required (σ_pt), 1 Suggestion (checklist pre-ronda).
	- Backlog de correcciones: C4-01 a C4-04 definidos con fechas objetivo.
- **Brechas Abiertas**
	- TODO Alineación σ_pt interdocumental (I-PSEA-07, I-PSEA-09, F-PSEA-06)
	  project:: [[CALAIRE-EA]]
	  priority:: high
	- TODO Agregar hito T-3 al cronograma de F-PSEA-06
	  project:: [[CALAIRE-EA]]
	- TODO Completar secciones críticas de I-PSEA-07 (skeleton)
	  project:: [[CALAIRE-EA]]
	  priority:: high
	- TODO Cierre de backlog C4-01 a C4-04 para aprobación formal de F-PSEA-06
	  project:: [[CALAIRE-EA]]
	  priority:: high
- **Documentación Requerida (F-GCM-03)**
	- TODO Protocolo Técnico CO
	  status:: #borrador
	  assignee:: [[Technical Lead]]
	- TODO Protocolo Técnico NOx
	  status:: #borrador
	- TODO Protocolo Técnico SO2
	  status:: #borrador
	- TODO Protocolo Técnico O3
	  status:: #borrador
	- TODO Manual de Transporte de Equipos
	- TODO Actualización Portafolio de Servicios
- **Auditorías**
	- Próxima auditoría interna: TBD
- **SST y acceso a instalaciones**
	- [[Inducción SST Persona Natural]] - Curso obligatorio para contratistas persona natural, certificado de aprobación y permiso de ingreso institucional para actividades asociadas a [[Prueba Piloto]].
- **Decisiones Clave**
	- #decision Segregación operativa/gestión adoptada como principio organizador del SGC (2026-04-07)
	  date:: 2026-04-07
	- #decision Enfoque σ_pt post-ronda (fitness-for-purpose) con fórmula JRC-ERLAP: σ_pt = a · x_pt + b (2026-04-10)
	  date:: 2026-04-10
- **Ver También**
	- [[CALAIRE-EA]]
	- [[CALAIRE-APP]]
	- [[Prueba Piloto]]
	- [[Desarrollo Técnico]]
