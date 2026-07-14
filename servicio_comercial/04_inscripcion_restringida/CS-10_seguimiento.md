# CS-10 — Seguimiento de inscripciones e ingresos

**Estado:** IMPLEMENTADO v0.3 — ACCESO RESTRINGIDO; aprobación institucional pendiente
**Propietario:** Coordinador de ronda
**Requerido antes:** Confirmación/ejecución
**Última revisión:** 2026-07-14 (libro de trabajo protegido implementado, controles automáticos y simulación sintética)

## Objetivo

Control de aforo, pedido, pago y viabilidad.

## Format

Archivo Excel institucional protegido para el MVP, almacenado en una ubicación
UNAL con control de acceso y copias de respaldo. Resultados técnicos participantes
no debe almacenarse en él. La migración futura a `calaire-app` solo procede
después de validar el flujo.

**Operational files:**

- `CS-10_seguimiento_inscripciones_ingresos.xlsx`: clean protected template.
- `CS-10_simulacion_sintetica.xlsx`: copia de prueba sintética; nunca lo use como registro en vivo.
- `../../scripts/build_cs10_tracker.py`: reproducible workbook generator.

La contraseña inicial de protección de la hoja está documentada en `LEAME` y debe ser
modificado por el coordinador de ronda antes de su uso real. La protección de la hoja evita
ediciones accidentales; El control de acceso, el registro de auditoría y las copias de seguridad siguen siendo institucionales.
storage responsibilities.

**Regla del sistema de comunicación:** la columna "Enlace/ubicación de comunicación" a continuación
debe apuntar a `calaire_med@unal.edu.co` o un proyecto institucional controlado
carpeta. No se aprueban las bandejas de entrada personales ni las carpetas ad hoc.

## Minimum columns

| Column | Descripción |
|---|---|
| ID de cliente potencial/cliente | Identificador único |
| Organization | Legal name |
| Country | |
| Preferred language | Español |
| Identificación redonda | |
| Selected blocks | CO, SO₂, O₃, NO/NO₂ |
| Analyzer count | |
| Quote number | Links to CS-06 |
| Quote revision | Initial = 0, increments on each revision |
| Valor de cotización | Valor original, antes de revisiones |
| Valor comprometido actual | Después de cualquier revisión o cambio |
| Quote currency | COP |
| Quote expiry | |
| **Quote acceptance deadline** | Primera fecha entre vencimiento de 30 días, cierre de inscripción, 15 días antes de la ronda o agotamiento de capacidad |
| **Fecha límite de pago/orden de compra** | 15 días calendario por defecto o plazo obligatorio de la Universidad, sin exceder el cierre de inscripción |
| Registration date | |
| Marca de tiempo de aceptación | [RELLENO — de CS-07] |
| Acceptance channel | Correo institucional con cotización firmada / orden de compra formal aceptada |
| Estado de revisión del contrato | Pendiente / Aprobado / Fallido |
| Fecha de revisión del contrato | |
| Contract reviewer | |
| Estado de la orden de compra/pago/factura | Pendiente / Parcial (X%) / Recibido / Facturado / Pagado / Vencido |
| **Seguimiento de pagos parciales** | Si PO/estado de pago = Parcial, registre: monto recibido, monto pendiente, % pagado, fecha de vencimiento del próximo pago |
| Número de factura | Cuando se emite |
| Código de participante después de la confirmación | Asignado por SGC |
| Capacity consumed (by block) | Número de analizadores aceptados en CO, SO₂, O₃ y NO/NO₂; derivado de CS-09 |
| Operating configuration | Individual gas / Simultaneous CO/SO₂ |
| **Último indicador de espacio disponible** | Sí/No: se configura automáticamente en Sí al aceptar el último espacio (requiere autorización comercial principal según la verificación 6 de CS-09) |
| Estado comercial | Intereses / Cotizado / Registrado / En revisión / Cotización-revisión en curso / Aceptado pendiente de pago/PO / Confirmado / En lista de espera / Rechazado / Retirado |
| **Wait-list priority** | Grupo 1: laboratorio acreditado; grupo 2: demás elegibles. Dentro de cada grupo, fecha/hora de solicitud completa y elegible |
| **Fecha de lista de espera** | Fecha en que el cliente fue agregado a la lista de espera |
| Estado de cancelación/reembolso | |
| Cancellation date | |
| Refund/credit note reference | If applicable |
| FX exposure | No aplica: cotización y facturación únicamente en COP |
| Responsable | Coordinador comercial o ronda asignado |
| Next action | |
| Enlace de comunicación/ubicación | Debe ser uno de los sistemas aprobados (ver encabezado) |
| Stale-EoI flag | [FILL — auto-set to Sí if EoI older than CS-05 response-expiry threshold] |

## Wait-list priority rules (default, override per CS-01)

Cuando varios clientes compiten por el mismo puesto, la prioridad es:

1. Solicitudes completas y elegibles de laboratorios acreditados, en orden de
   fecha y hora de completitud.
2. Demás organizaciones elegibles, también en orden de fecha y hora de
   completitud.
3. La expresión de interés no reserva prioridad.

Desempate documentado en la columna "Notas". Los criterios deben aplicarse de forma coherente; las desviaciones requieren la aprobación del cliente potencial comercial y un registro CS-12.

## Política de pago parcial

Si CS-01 permite pagos parciales (por ejemplo, 50% en el pedido, 50% antes de la ronda según CS-06 Sección 9):

- El estado "Parcial (X%)" se utiliza hasta recibir el pago completo.
- El cliente no puede pasar a "Confirmado" hasta que se registre el pago completo.
- Si el segundo pago está vencido, escalar según CS-12 (activador de cancelación) después del período de gracia definido en CS-01.

## Required views

### 1. Pipeline

Filtro: estado = Interés hasta Cotizado.

Propósito: Pronosticar la demanda y gestionar el seguimiento de prospectos. Excluir filas con indicador Stale-EoI = Sí.

### 2. Enrollment

Filtro: estado = Confirmado.

Agrupar por: gas y configuración operativa.

Propósito: Realizar un seguimiento de la capacidad confirmada frente a los límites. Muestre de forma destacada la "bandera del último espacio disponible".

### 3. Viability

Filtro: estado = Confirmado.

Suma: valor comprometido actual (en equivalente en COP usando la política FX CS-04 Tab 1).

Compare con: umbral mínimo de inscripción de CS-01.

Propósito: Determinar si la ronda es comercialmente viable. Mostrar por fecha de decisión de inscripción mínima.

### 4. Receivables

Filtro: Orden de compra/pago/estado de factura = Facturado o Pagado o Vencido o Parcial.

Propósito: Realizar un seguimiento del flujo de caja y de las cuentas vencidas. Resalte las cuentas vencidas por período de gracia CS-01.

### 5. Exceptions

Filtro: estado = En lista de espera / Cancelado / Reembolsado / Disputado / Rechazado.

Finalidad: Gestionar excepciones y reasignaciones de capacidad. Mostrar prioridad y fecha de la lista de espera.

## Capacity flags

El rastreador debería marcar automáticamente:

- More than 4 confirmed analyzer positions for an individual gas.
- More than 3 participants or 6 analyzers for simultaneous CO/SO₂.
- Un nuevo estado "Confirmado" que dejaría la capacidad residual = 0 (activa la advertencia de "último espacio").
- Stale EoI responses (older than CS-05 response-expiry threshold).

## Controls

- Acceso controlado: únicamente coordinador comercial, financiero y de ronda.
- Sin resultados técnicos ni puntuaciones de rendimiento.
- La transferencia a la planificación de la ronda del SGC es una exportación controlada o una lista de participantes aprobados, no una reescritura manual.
- El "enlace/ubicación de comunicación" debe utilizar únicamente sistemas aprobados; No se aceptan bandejas de entrada personales ad hoc.
- Todos los cambios al estado Confirmado deben ser rastreables hasta un registro CS-12 (para retiros) o un registro CS-09 (para confirmación inicial).

## Approval

| Versión | Fecha | Aprobador | Notas |
|---|---|---|---|
| 0.1 BORRADOR | [RELLENO] | [RELLENO] | Plantilla inicial |
| 0.2 BORRADOR | 2026-07-14 | [RELLENO] | Se agregaron criterios de lista de espera, fecha límite de pago, seguimiento de pago parcial, indicador de último espacio, columna de exposición de divisas, regla de sistemas de comunicación aprobada, indicador de EoI obsoleto. |
| 0.3 IMPLEMENTADA | 2026-07-14 | Pendiente de aprobación institucional | Plantilla de Excel protegida, listas controladas, saldos calculados, alertas de capacidad/pago/EoI obsoletas, cinco vistas requeridas y copia de prueba sintética. |
