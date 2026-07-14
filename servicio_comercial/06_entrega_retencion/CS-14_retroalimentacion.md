# CS-14 — Formulario de comentarios del cliente

**Estado:** BORRADOR — contenido redactado; aprobación pendiente
**Propietario:** Gerente de servicio
**Requerido antes:** Cierre redondo
**Last revision:** 2026-07-14 (added submission date, channel, anonymity option, link to CS-05 for renewal preference, updated QMS codes)  
**QMS code reference:** ver `00_control/equivalencia_codigos_sgc.md`. `P-PSEA-17` (vigente) = Quejas del PEA. `P-PSEA-18` (vigente) = Apelaciones del PEA. `F-PSEA-14` (vigente post-renumeración) = Registro de queja / NC / CAPA. `F-PSEA-15` (vigente) = Registro de apelaciones.

## Objetivo

Medir la experiencia y la demanda del servicio.

## Form metadata

| Campo | Valor |
|---|---|
| Canal de envío | [FILL: por ejemplo, URL del formulario, dirección de correo electrónico, enlace de la aplicación] |
| Idiomas disponibles | [FILL — igual que CS-02] |
| Opción de anonimato | Sí, el envío puede ser anónimo (sin enlace al código de participante) |
| Ventana de envío | [FILL – abierto desde la entrega del informe final hasta N días después, luego cerrado] |
| Link to renewal EoI (CS-05) | [FILL — Q11 below feeds CS-05] |

## Important

Los comentarios técnicos que indiquen una queja, apelación o disconformidad deben dirigirse al procedimiento PEA existente (`P-PSEA-17`, `P-PSEA-18`, `F-PSEA-14`, `F-PSEA-15`) en lugar de gestionarse únicamente como un comentario de encuesta.

## Minimum questions

| # | Question | Scale / type | Required |
|---|---|---|---|
| 0 | Submission date (auto-captured) | Date | Auto |
| 0a | Submission channel | Portal / email / paper | Auto |
| 1 | Claridad de oferta y cotización | 1–5 | Sí |
| 2 | Facilidad de registro y pago | 1–5 | Sí |
| 3 | Claridad y puntualidad de las comunicaciones | 1–5 | Sí |
| 4 | Facility/logistics experience | 1–5 | Yes |
| 5 | Utilidad y oportunidad de la entrega de informes | 1–5 | Sí |
| 6 | Valor percibido por precio | 1–5 | Sí |
| 7 | Interés de gas/paquete para la próxima ronda (enlace cruzado con CS-05 para evitar preguntas dobles) | Selección múltiple + comentarios | Sí |
| 8 | Periodo preferido y plazo de entrega de adquisiciones | Texto | Opcional |
| 9 | Likelihood of returning or recommending | 0–10 (NPS) | Yes |
| 10 | Complaint/improvement comments | Free text | Optional |
| 11 | Permission to be contacted for renewal (links to CS-05) | Checkbox | Yes |
| 12 | Anonymity preference | "Submit anonymously" checkbox | Optional |

## Routing rules

- If Q10 mentions a specific complaint, appeal or nonconformity:
- Ruta a `P-PSEA-17` (quejas) / `P-PSEA-18` (apelaciones) en 1 día hábil.
- No cierre el registro de comentarios hasta que la queja se registre por separado.
- Registrar la vinculación en `F-PSEA-14` (queja/NC/CAPA) o `F-PSEA-15` (apelaciones).
- Si la P10 menciona algún tema comercial (facturación, plazos, cancelación):
- Ruta a plomo comercial y apertura CS-12 en caso de impacto financiero.
- If Q10 is general improvement:
- Inicie sesión en el registro de mejoras para la revisión de la gestión.
- Si P11 = sí, inserte las preferencias de gas/paquete (P7) y el período (P8) en una nueva fila de expresión de interés CS-05, vinculada al registro CS-10 existente del participante.
- Si P12 = "Enviar de forma anónima", el envío se almacena sin código de participante; sólo son posibles vistas agregadas.

## Approval

| Versión | Fecha | Aprobador | Notas |
|---|---|---|---|
| 0.1 BORRADOR | [RELLENO] | [RELLENO] | Plantilla inicial |
| 0.2 BORRADOR | 2026-07-14 | [RELLENO] | Se agregó fecha/canal de envío, opción de anonimato, enlace cruzado CS-05, códigos QMS actualizados. |
