# Control de acceso — `04_inscripcion_restringida/`

**Carpeta:** `servicio_comercial/04_inscripcion_restringida/`
**Clasificación:** RESTRINGIDO
**Propietario:** Directora del grupo
**Última actualización:** 2026-07-14


## Archivos de esta carpeta

| Archivo | Clasificación | Acceso de lectura | Acceso de escritura |
|---|---|---|---|
| `CS-10_seguimiento.md` (el rastreador operativo, en la práctica una hoja de cálculo) | RESTRINGIDO: identidad del participante, estado del pedido, pago, capacidad, exposición cambiaria | Directora del grupo y Profesional de proyectos | Directora del grupo, con revisión del Profesional de proyectos para cambios de estado confirmados |
| `CS-11_confirmaciones.md` | RESTRINGIDO: códigos de participante, datos de contacto, estado de pago | Directora del grupo, Profesional de proyectos y personal autorizado por la dirección | Directora del grupo (con revisión de Profesional de proyectos para cambios a un registro Confirmado) |

## Por qué esta carpeta es restringida

- `CS-10_seguimiento.md` (el rastreador en vivo) contiene **identidad del participante, nombre legal de la organización, datos de contacto, estado de pago, consumo de capacidad y exposición a divisas**: toda la PII y datos comercialmente confidenciales. La divulgación fuera del equipo autorizado violaría la Ley 1581/2012 (Habeas Data) y comprometería la confidencialidad comercial.
- `CS-11_confirmaciones.md` incluye la **asignación de código de participante** (vinculada a los códigos SGC) y el **contenido del paquete de incorporación** que incluye referencias técnicas de campos SGC; este es el puente entre la confirmación comercial y la entrada en la planificación de la ronda SGC.

## Procedimientos de acceso

- **Se otorga acceso de lectura** a la Directora del grupo y al Profesional de proyectos. El personal técnico puede recibir acceso de lectura para participantes confirmados específicos según sea necesario, registrado en el registro de auditoría.
- **Se otorga acceso de escritura** a la Directora del grupo.
- **No se permite la exportación** de datos de identidad de los participantes a sistemas externos (correo electrónico personal, SaaS de terceros, impresiones en papel dejadas desatendidas) sin una autorización explícita de la Directora del grupo documentada en `00_control/registro_cambios_versiones.md`.
- **Consentimiento de marketing del cliente** es un indicador independiente en `CS-10`; Los datos solo se pueden utilizar para marketing si la bandera se establece según el consentimiento capturado en "CS-05" y confirmado en "CS-07".
- **Retención de datos:** los registros de seguimiento se conservan durante 5 años según la retención de registros ISO/IEC 17043; Los registros CS-11 siguen el mismo período (según la sección de retención CS-13).

## Datos transfronterizos

- Para los participantes internacionales, el **consentimiento de divulgación transfronteriza** capturado en CS-09 verificación 13 rige cualquier transferencia de datos fuera de Colombia. Sin consentimiento explícito, el informe se entrega al país de registro del participante solo cuando ese país tiene una decisión o tratado de adecuación con Colombia, O el participante firma un acuerdo de transferencia transfronteriza por separado.

## Auditoría

- Cualquier lectura o escritura de archivos en esta carpeta debe registrarse en el sistema de registro de acceso institucional.
- Revisión trimestral: Directora del grupo y Profesional de proyectos verifican que las listas de acceso estén actualizadas y que los registros obsoletos estén archivados según la política de retención.

## Artefactos relacionados

- `00_control/CS-01_decisiones_comerciales.md` — reglas de confidencialidad / divulgación.
- `00_control/registro_cambios_versiones.md` — historial de versiones.
- `docs/qms/P-PSEA-19` (vigente) — Confidencialidad operativa interna, el control SGC con el que se alinea esta carpeta.
- `docs/sgc/matriz_equivalencias_codigos_sgc_pea.md` — para el mapeo de códigos.
