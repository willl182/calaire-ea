# CS-10 — Seguimiento de inscripciones e ingresos

<<<<<<< Updated upstream
**Propietario:** Profesional de proyectos
**Última revisión:** 2026-07-14 (libro de trabajo protegido implementado, controles automáticos y simulación sintética)
=======
**Estado:** IMPLEMENTADO v0.3 — ACCESO RESTRINGIDO; aprobación institucional pendiente\
**Propietario:** Coordinador de ronda\
**Requerido antes de:** confirmación / ejecución\
**Última revisión:** 2026-07-14 (libro de Excel protegido implementado, controles automáticos y simulación sintética)
>>>>>>> Stashed changes

## Objetivo

Controlar capacidad, pedido, pago y viabilidad.

## Formato

Archivo Excel institucional protegido para el MVP, almacenado en una ubicación
UNAL con control de acceso y copias de respaldo. Los resultados técnicos de los
participantes no se almacenan en él. La migración futura a `calaire-app` solo procede
después de validar el flujo.

**Archivos operativos:**

<<<<<<< Updated upstream
- `CS-10_seguimiento_inscripciones_ingresos.xlsx`: plantilla limpia y protegida.
- `CS-10_simulacion_sintetica.xlsx`: copia de prueba sintética; nunca lo use como registro en vivo.
- `../../scripts/build_cs10_tracker.py`: reproducible workbook generator.

La contraseña inicial de protección de la hoja está documentada en `LEAME` y debe ser
modificado por la Directora del grupo antes de su uso real. La protección de la hoja evita
ediciones accidentales; El control de acceso, el registro de auditoría y las copias de seguridad siguen siendo institucionales.
storage responsibilities.
=======
- `CS-10_seguimiento_inscripciones_ingresos.xlsx`: plantilla protegida limpia.
- `CS-10_simulacion_sintetica.xlsx`: copia de prueba sintética; nunca se usa como registro real.
- `../../scripts/build_cs10_tracker.py`: generador reproducible del libro.

La contraseña inicial de protección de la hoja está documentada en la hoja `LEAME` y
debe ser cambiada por el coordinador de ronda antes del uso real. La protección de la
hoja evita ediciones accidentales; el control de acceso, el registro de auditoría y las
copias de respaldo siguen siendo responsabilidad del almacenamiento institucional.
>>>>>>> Stashed changes

**Regla de comunicaciones:** la columna "Enlace / ubicación de comunicación" debe
apuntar a `calaire_med@unal.edu.co` o a una carpeta institucional controlada del
proyecto. No se aprueban bandejas personales ni carpetas ad hoc.

## Columnas mínimas

| Columna | Descripción |
|---|---|
<<<<<<< Updated upstream
| ID de cliente potencial/cliente | Identificador único |
| Organización | Nombre legal |
=======
| ID de prospecto / cliente | Identificador único |
| Organización | Razón social |
>>>>>>> Stashed changes
| País | |
| Idioma preferido | Español |
| Identificación de la ronda | |
| Bloques seleccionados | CO, SO₂, O₃, NO/NO₂ |
<<<<<<< Updated upstream
| Cantidad de analizadores | |
| Número de cotización | Enlaza con CS-06 |
| Revisión de cotización | Inicial = 0; se incrementa con cada revisión |
| Valor de cotización | Valor original, antes de revisiones |
| Valor comprometido actual | Después de cualquier revisión o cambio |
| Moneda de cotización | COP |
| Vencimiento de cotización | |
| **Plazo de aceptación de la cotización** | Primera fecha entre vencimiento de 30 días, cierre de inscripción, 15 días antes de la ronda o agotamiento de capacidad |
| **Fecha límite de pago/orden de compra** | 15 días calendario por defecto o plazo obligatorio de la Universidad, sin exceder el cierre de inscripción |
| Fecha de inscripción | |
| Marca de tiempo de aceptación | [POR DILIGENCIAR — de CS-07] |
| Canal de aceptación | Correo institucional con cotización firmada / orden de compra formal aceptada |
| Estado de revisión del contrato | Pendiente / Aprobado / Fallido |
=======
| Número de analizadores | |
| Número de cotización | Enlace a CS-06 |
| Revisión de la cotización | Inicial = 0; se incrementa en cada revisión |
| Valor de cotización | Valor original, antes de revisiones |
| Valor comprometido actual | Después de cualquier revisión o cambio |
| Moneda de la cotización | COP |
| Vencimiento de la cotización | |
| **Fecha límite de aceptación** | Primera fecha entre vencimiento de 30 días, cierre de inscripción, 15 días antes de la ronda o agotamiento de capacidad |
| **Fecha límite de pago/orden de compra** | 15 días calendario por defecto o plazo obligatorio de la Universidad, sin exceder el cierre de inscripción |
| Fecha de inscripción | |
| Marca de tiempo de aceptación | Tomada de CS-07 |
| Canal de aceptación | Correo institucional con cotización firmada / orden de compra formal aceptada |
| Estado de revisión del contrato | Pendiente / Aprobado / No aprobado |
>>>>>>> Stashed changes
| Fecha de revisión del contrato | |
| Revisor del contrato | |
| Estado de la orden de compra/pago/factura | Pendiente / Parcial (X%) / Recibido / Facturado / Pagado / Vencido |
| **Seguimiento de pagos parciales** | Si el estado de pago u orden de compra = Parcial, registrar: monto recibido, monto pendiente, % pagado, fecha de vencimiento del próximo pago |
| Número de factura | Cuando se emite |
| Código de participante después de la confirmación | Asignado por SGC |
| Capacidad consumida (por bloque) | Número de analizadores aceptados en CO, SO₂, O₃ y NO/NO₂; derivado de CS-09 |
<<<<<<< Updated upstream
| Configuración operativa | Gas individual / CO/SO₂ simultáneos |
| **Último indicador de espacio disponible** | Sí/No: se configura automáticamente en Sí al aceptar el último espacio (requiere autorización de la Directora del grupo según la verificación 6 de CS-09) |
| Estado comercial | Intereses / Cotizado / Registrado / En revisión / Cotización-revisión en curso / Aceptado pendiente de pago/PO / Confirmado / En lista de espera / Rechazado / Retirado |
=======
| Configuración de operación | Gas individual / CO y SO₂ simultáneos |
| **Indicador de último cupo** | Sí / No: se marca automáticamente en Sí al aceptar el último cupo (requiere autorización del líder comercial según la verificación 6 de CS-09) |
| Estado comercial | Interés / Cotizado / Inscrito / En revisión / Revisión de cotización en curso / Aceptado pendiente de pago u OC / Confirmado / En lista de espera / Rechazado / Retirado |
>>>>>>> Stashed changes
| **Prioridad en lista de espera** | Grupo 1: laboratorio acreditado; grupo 2: demás elegibles. Dentro de cada grupo, fecha/hora de solicitud completa y elegible |
| **Fecha de lista de espera** | Fecha en que el cliente fue agregado a la lista de espera |
| Estado de cancelación/reembolso | |
| Fecha de cancelación | |
| Referencia de reembolso / nota crédito | Si aplica |
| Exposición cambiaria | No aplica: cotización y facturación únicamente en COP |
<<<<<<< Updated upstream
| Responsable | Directora del grupo |
| Próxima acción | |
| Enlace de comunicación/ubicación | Debe ser uno de los sistemas aprobados (ver encabezado) |
| Indicador de expresión de interés obsoleta | [POR DILIGENCIAR — se establece automáticamente en Sí si la expresión de interés supera el umbral de caducidad de respuesta de CS-05] |

## Reglas de prioridad de la lista de espera (predeterminadas; CS-01 puede sustituirlas)
=======
| Responsable | Líder comercial o coordinador de ronda asignado |
| Próxima acción | |
| Enlace / ubicación de comunicación | Debe ser uno de los sistemas aprobados (ver encabezado) |
| Indicador de expresión de interés vencida | Se marca automáticamente en Sí cuando la expresión de interés supera la vigencia de 60 días de CS-05 |

## Reglas de prioridad de la lista de espera (CS-01 sección 7)
>>>>>>> Stashed changes

Cuando varios clientes compiten por el mismo cupo, la prioridad es:

1. Solicitudes completas y elegibles de laboratorios acreditados, en orden de
   fecha y hora de completitud.
2. Demás organizaciones elegibles, también en orden de fecha y hora de
   completitud.
3. La expresión de interés no reserva prioridad.

Desempate documentado en la columna "Notas". Los criterios deben aplicarse de forma coherente; las desviaciones requieren aprobación del líder comercial y un registro CS-12.

## Política de pago parcial

Si las políticas de la Universidad permiten pagos parciales (por ejemplo, 50 % con el pedido y 50 % antes de la ronda, según CS-06 sección 9):

- El estado "Parcial (X%)" se utiliza hasta recibir el pago completo.
- El cliente no puede pasar a "Confirmado" hasta que se registre el pago completo.
- Si el segundo pago está vencido, se escala según CS-12 (disparador de cancelación) al vencer el plazo de pago definido en CS-01.

## Vistas requeridas

<<<<<<< Updated upstream
### 1. Flujo de oportunidades
=======
### 1. Embudo
>>>>>>> Stashed changes

Filtro: estado = Interés hasta Cotizado.

Propósito: pronosticar la demanda y gestionar el seguimiento de prospectos. Excluye filas con expresión de interés vencida.

### 2. Inscripción

Filtro: estado = Confirmado.

Agrupar por: gas y configuración operativa.

Propósito: seguir la capacidad confirmada frente a los límites. Muestra de forma destacada el indicador de último cupo.

### 3. Viabilidad

Filtro: estado = Confirmado.

<<<<<<< Updated upstream
Suma: valor comprometido actual (en equivalente en COP usando la política cambiaria de la pestaña 1 de CS-04).
=======
Suma: valor comprometido actual (en COP).
>>>>>>> Stashed changes

Compare con: umbral mínimo de inscripción de CS-01.

Propósito: determinar si la ronda es comercialmente viable antes de la fecha de decisión de inscripción mínima.

<<<<<<< Updated upstream
### 4. Cuentas por cobrar
=======
### 4. Cartera
>>>>>>> Stashed changes

Filtro: estado de pago / orden de compra / factura = Facturado, Pagado, Vencido o Parcial.

Propósito: seguir el flujo de caja y las cuentas vencidas según el plazo de pago de CS-01.

### 5. Excepciones

Filtro: estado = En lista de espera / Cancelado / Reembolsado / Disputado / Rechazado.

Propósito: gestionar excepciones y reasignaciones de capacidad. Muestra prioridad y fecha de la lista de espera.

<<<<<<< Updated upstream
## Indicadores de capacidad
=======
## Alertas de capacidad
>>>>>>> Stashed changes

El seguimiento marca automáticamente:

<<<<<<< Updated upstream
- Más de 4 cupos confirmados de analizadores para un gas individual.
- Más de 3 participantes o 6 analizadores para CO/SO₂ simultáneos.
- Un nuevo estado "Confirmado" que dejaría la capacidad residual = 0 (activa la advertencia de "último espacio").
- Respuestas obsoletas de expresión de interés (más antiguas que el umbral de caducidad de respuesta de CS-05).

## Controles

- Acceso controlado: Directora del grupo y Profesional de proyectos.
=======
- Más de 4 analizadores confirmados para un gas individual.
- Más de 3 participantes o 6 analizadores en operación simultánea CO/SO₂.
- Un nuevo estado "Confirmado" que deja la capacidad residual en 0 (activa la advertencia de último cupo).
- Expresiones de interés vencidas (más de 60 días, según CS-05).

## Controles

- Acceso controlado: únicamente equipo comercial, finanzas y coordinador de ronda.
>>>>>>> Stashed changes
- Sin resultados técnicos ni puntuaciones de rendimiento.
- El traspaso a la planificación de la ronda en el SGC es una exportación controlada o una lista de participantes aprobados, no una reescritura manual.
- El "enlace/ubicación de comunicación" debe utilizar únicamente sistemas aprobados; no se aceptan bandejas de entrada personales ad hoc.
- Todos los cambios al estado Confirmado deben ser rastreables hasta un registro CS-12 (para retiros) o un registro CS-09 (para confirmación inicial).
<<<<<<< Updated upstream
=======

## Aprobación

| Versión | Fecha | Aprobador | Notas |
|---|---|---|---|
| 0.1 BORRADOR | 2026-07-12 | — | Plantilla inicial |
| 0.2 BORRADOR | 2026-07-14 | — | Se agregaron criterios de lista de espera, fecha límite de pago, seguimiento de pagos parciales, indicador de último cupo, columna de exposición cambiaria, regla de sistemas de comunicación aprobados e indicador de expresión de interés vencida. |
| 0.3 IMPLEMENTADA | 2026-07-14 | Pendiente de aprobación institucional | Plantilla de Excel protegida, listas controladas, saldos calculados, alertas de capacidad, pago y expresiones de interés vencidas, cinco vistas requeridas y copia de prueba sintética. |
>>>>>>> Stashed changes
