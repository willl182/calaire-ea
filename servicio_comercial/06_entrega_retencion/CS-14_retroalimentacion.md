# CS-14 — Formulario de comentarios del cliente

**Propietario:** Profesional de proyectos
**Última revisión:** 2026-07-14 (se agregaron la fecha y el canal de envío, la opción de anonimato y el enlace con CS-05 para la preferencia de renovación; se actualizaron los códigos del SGC)
**Referencia de códigos del SGC:** ver `00_control/equivalencia_codigos_sgc.md`. `P-PSEA-17` (vigente) = Quejas del PEA. `P-PSEA-18` (vigente) = Apelaciones del PEA. `F-PSEA-14` (vigente tras la renumeración) = Registro de queja / NC / CAPA. `F-PSEA-15` (vigente) = Registro de apelaciones.

## Objetivo

Medir la experiencia y la demanda del servicio.

## Metadatos del formulario

| Campo | Valor |
|---|---|
| Canal de envío | [POR DILIGENCIAR — por ejemplo, URL del formulario, dirección de correo electrónico, enlace de la aplicación] |
| Idiomas disponibles | [POR DILIGENCIAR — igual que CS-02] |
| Opción de anonimato | Sí, el envío puede ser anónimo (sin enlace al código de participante) |
| Ventana de envío | [POR DILIGENCIAR — abierto desde la entrega del informe final hasta N días después, luego cerrado] |
| Enlace a la expresión de interés de renovación (CS-05) | [POR DILIGENCIAR — la P11 siguiente alimenta CS-05] |

## Importante

Los comentarios técnicos que indiquen una queja, apelación o disconformidad deben dirigirse al procedimiento PEA existente (`P-PSEA-17`, `P-PSEA-18`, `F-PSEA-14`, `F-PSEA-15`) en lugar de gestionarse únicamente como un comentario de encuesta.

## Preguntas mínimas

| # | Pregunta | Escala / tipo | Obligatoria |
|---|---|---|---|
| 0 | Fecha de envío (capturada automáticamente) | Fecha | Automática |
| 0a | Canal de envío | Portal / correo electrónico / papel | Automática |
| 1 | Claridad de oferta y cotización | 1–5 | Sí |
| 2 | Facilidad de registro y pago | 1–5 | Sí |
| 3 | Claridad y puntualidad de las comunicaciones | 1–5 | Sí |
| 4 | Facility/logistics experience | 1–5 | Yes |
| 5 | Utilidad y oportunidad de la entrega de informes | 1–5 | Sí |
| 6 | Valor percibido por precio | 1–5 | Sí |
| 7 | Interés de gas/paquete para la próxima ronda (enlace cruzado con CS-05 para evitar preguntas dobles) | Selección múltiple + comentarios | Sí |
| 8 | Periodo preferido y plazo de entrega de adquisiciones | Texto | Opcional |
| 9 | Probabilidad de volver o recomendar | 0–10 (NPS) | Sí |
| 10 | Comentarios sobre quejas o mejoras | Texto libre | Opcional |
| 11 | Permiso para recibir contacto de renovación (enlaza con CS-05) | Casilla de verificación | Sí |
| 12 | Anonymity preference | "Submit anonymously" checkbox | Optional |

## Reglas de encaminamiento

- Si la P10 menciona una queja, apelación o no conformidad específica:
- Ruta a `P-PSEA-17` (quejas) / `P-PSEA-18` (apelaciones) en 1 día hábil.
- No cierre el registro de comentarios hasta que la queja se registre por separado.
- Registrar la vinculación en `F-PSEA-14` (queja/NC/CAPA) o `F-PSEA-15` (apelaciones).
- Si la P10 menciona algún tema comercial (facturación, plazos, cancelación):
- Ruta a plomo comercial y apertura CS-12 en caso de impacto financiero.
- Si la P10 es una mejora general:
- Inicie sesión en el registro de mejoras para la revisión de la gestión.
- Si P11 = sí, inserte las preferencias de gas/paquete (P7) y el período (P8) en una nueva fila de expresión de interés CS-05, vinculada al registro CS-10 existente del participante.
- Si P12 = "Enviar de forma anónima", el envío se almacena sin código de participante; solo son posibles vistas agregadas.
