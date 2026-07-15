# CS-05 — Expression-of-Interest Form

**Estado:** BORRADOR — contenido redactado; aprobación pendiente
**Propietario:** Líder comercial
**Requerido antes:** Lanzamiento de marketing
**Last revision:** 2026-07-14 (added calibration certificate question, response expiry, preferred language, data protection consent text)

## Objetivo

Verificar la demanda antes de comprometer fechas y costos.

## Important note

Esto no es un registro y no crea ningún lugar reservado. El formulario debe decirlo explícitamente.

## Form metadata

| Campo | Valor |
|---|---|
| Idiomas disponibles | Español |
| Caducidad de la respuesta | [FILL: por ejemplo, 60 días desde el envío; respuestas obsoletas eliminadas de CS-10] |
| Almacenamiento | [FILL: por ejemplo, CRM comercial, backend de formulario seguro] |
| Propietario de la última reseña | [LLENAR NOMBRE] |

## Minimum questions

| # | Pregunta | Tipo de respuesta | Propósito |
|---|---|---|---|
| 1 | Organization name | Text | Identify prospect |
| 2 | Nombre de contacto y correo electrónico | Texto | Seguimiento comercial |
| 3 | País/ciudad | Texto | Logística y huso horario |
| 4 | Desired gas(es) | Multi-select: CO, SO₂, NO, NO₂, O₃ | Scope validation |
| 5 | Número y tipo de analizadores (fabricante, modelo, año) | Texto | Planificación de capacidad y compatibilidad |
| 6 | Fecha de la última calibración del analizador | Fecha | Filtro de compatibilidad: las calibraciones obsoletas pueden necesitar una recalibración antes de la ronda |
| 7 | Certificado de calibración válido hasta | Fecha | Filtro de compatibilidad: debe ser válido al inicio de la ronda |
| 8 | ¿Se traerán analizadores de CO y SO₂ separados? | Sí / No / Desconocido | Determina la viabilidad de configuración simultánea |
| 9 | ¿Le resulta factible el funcionamiento simultáneo con CO/SO₂? | Sí / No / Desconocido | Determina el uso de la configuración de 3 participantes/6 analizadores |
| 10 | Preferred period | Date range / quarter | Calendar planning |
| 11 | Método de adquisición y plazo de entrega aproximado | Texto | Estimación del ciclo de ventas |
| 12 | Capacidad para transportar equipos a Medellín | Sí / No / Con asistencia | Bandera de riesgo |
| 13 | Interés en participar bajo un modelo de tarifa plana por organización para uno a cuatro bloques; el valor todavía está en evaluación y no constituye oferta | Sí / No / Depende del valor aprobado | Validar aceptación de la arquitectura sin publicar un precio no aprobado |
| 14 | ¿Su proceso de compra admite cotización y facturación en COP? | Sí / No / Requiere revisión | Identificar barreras de compra; la moneda aprobada es únicamente COP |
| 15 | Idioma preferido para comunicaciones comerciales | Selección única (español/inglés/otro) | Soporte multilingüe |
| 16 | Autorización para seguimiento comercial (con texto de consentimiento explícito) | Casilla de verificación (obligatoria) | Cumplimiento de la protección de datos — ver texto abajo |

## Texto de consentimiento (pregunta 17, debe ser visible y no verificado previamente)

> "Autorizo a CALAIRE-EA a contactarme en relación con esta expresión de interés y a almacenar la información suministrada con el fin de evaluar la viabilidad del servicio y, si corresponde, preparar una cotización. Entiendo que puedo revocar esta autorización en cualquier momento escribiendo a `calaire_med@unal.edu.co` y que mis datos serán tratados conforme a la política institucional aplicable y a la normativa colombiana de protección de datos."

La URL completa de la política de privacidad o la referencia en PDF deben estar vinculadas junto a la casilla de verificación.

## Controls

- El formulario indica explícitamente: "La presentación de esta expresión de interés no reserva un lugar en la ronda".
- Data handling references existing confidentiality controls (`P-PSEA-19`, código vigente tras renumeración 2026-06-14; ver `00_control/equivalencia_codigos_sgc.md`).
- Responses feed into CS-10 tracker as pipeline stage "Interest".
- Las respuestas anteriores al umbral de caducidad de respuesta se marcan como "obsoletas" en CS-10 y se excluyen de las vistas de canalización activa.
- Las preguntas 6 y 7 (fechas de calibración) alimentan la verificación de compatibilidad del equipo CS-09.
- La pregunta 15 (idioma preferido) alimenta la selección de idiomas de CS-06 y CS-08.

## Approval

| Versión | Fecha | Aprobador | Notas |
|---|---|---|---|
| 0.1 BORRADOR | [RELLENO] | [RELLENO] | Plantilla inicial |
| 0.2 BORRADOR | 2026-07-14 | [RELLENO] | Se agregaron fechas de calibración, vencimiento de respuesta, preferencia de idioma, texto de consentimiento de Ley 1581. |
