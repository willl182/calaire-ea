# Access Control — `04_inscripcion_restringida/`

**Folder:** `servicio_comercial/04_inscripcion_restringida/`
**Classification:** RESTRICTED
**Propietario:** Coordinador de ronda
**Last updated:** 2026-07-14

## Files in this folder

| File | Classification | Read access | Write access |
|---|---|---|---|
| `CS-10_seguimiento.md` (el rastreador operativo, en la práctica una hoja de cálculo) | RESTRINGIDO: identidad del participante, estado comercial, pago, capacidad, exposición cambiaria | Coordinador comercial, financiero, ronda, gerente de servicios | Coordinador de ronda (con autorización comercial líder para cambios de estado Confirmados) |
| `CS-11_confirmaciones.md` | RESTRINGIDO: códigos de participante, datos de contacto, estado de pago | Comercial, coordinador de rondas, responsable de servicios, gestión | Coordinador de ronda (con liderazgo comercial para cualquier cambio a un registro Confirmado) |

## Why this folder is restricted

- `CS-10_seguimiento.md` (el rastreador en vivo) contiene **identidad del participante, nombre legal de la organización, datos de contacto, estado de pago, consumo de capacidad y exposición a divisas**: toda la PII y datos comercialmente confidenciales. La divulgación fuera del equipo autorizado violaría la Ley 1581/2012 (Habeas Data) y comprometería la confidencialidad comercial.
- `CS-11_confirmaciones.md` incluye la **asignación de código de participante** (vinculada a los códigos QMS) y el **contenido del paquete de incorporación** que incluye referencias técnicas de campos QMS; este es el puente entre la confirmación comercial y la entrada en la planificación de la ronda QMS.

## Access procedures

- **Se otorga acceso de lectura** a: equipo comercial, finanzas, coordinador de ronda, gerente de servicios, gerencia. El personal técnico puede recibir acceso de lectura para participantes confirmados específicos según sea necesario, registrado en el registro de auditoría.
- **Se otorga acceso de escritura** a: coordinador de ronda (principal), con autorización comercial principal para cualquier cambio en un registro de estado Confirmado (reasignación de capacidad, procesamiento de retiros, etc.).
- **No se permite la exportación** de datos de identidad de los participantes a sistemas externos (correo electrónico personal, SaaS de terceros, impresiones en papel dejadas desatendidas) sin una autorización comercial explícita documentada en el registro de cambios en línea del archivo.
- **Consentimiento de marketing del cliente** es un indicador independiente en `CS-10`; Los datos solo se pueden utilizar para marketing si la bandera se establece según el consentimiento capturado en "CS-05" y confirmado en "CS-07".
- **Retención de datos:** los registros de seguimiento se conservan durante 5 años según la retención de registros ISO/IEC 17043; Los registros CS-11 siguen el mismo período (según la sección de retención CS-13).

## Cross-border data

- Para los participantes internacionales, el **consentimiento de divulgación transfronteriza** capturado en CS-09 verificación 13 rige cualquier transferencia de datos fuera de Colombia. Sin consentimiento explícito, el informe se entrega al país de registro del participante solo cuando ese país tiene una decisión o tratado de adecuación con Colombia, O el participante firma un acuerdo de transferencia transfronteriza por separado.

## Audit

- Cualquier lectura o escritura de archivos en esta carpeta debe registrarse en el sistema de registro de acceso institucional.
- Revisión trimestral: el coordinador de ronda y el líder comercial verifican que las listas de acceso estén actualizadas y que los registros obsoletos estén archivados según la política de retención.

## Related artifacts

- `00_control/CS-01_decisiones_comerciales.md` — confidentiality / disclosure rules.
- `00_control/registro_cambios_versiones.md` — release history.
- `docs/qms/P-PSEA-19` (vigente) — Confidencialidad operativa interna, el control QMS con el que se alinea esta carpeta.
- `docs/sgc/matriz_equivalencias_codigos_sgc_pea.md` — for code mapping.
