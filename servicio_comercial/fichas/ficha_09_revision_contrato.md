# Lista de verificación de revisión de contrato

**Archivo fuente:** `servicio_comercial/03_ventas_contratacion/CS-09_revisiones_contrato.md`

## Propósito

Impedir que CALAIRE-EA acepte un pedido que no puede entregar o cuya orden de compra contradiga las condiciones del servicio. Es la compuerta previa a toda confirmación.

## Contenido clave

- 17 verificaciones firmadas (iniciales obligatorias): validez de la cotización, no doble reserva, gases ofrecidos en la ronda, capacidad disponible y residual ≥ 0, compatibilidad del equipo, coherencia de precio y pagos.
- Revisión de la orden de compra contra los términos: que no anule en silencio reglas de cancelación, confidencialidad, informes ni la ausencia de calificación agregada.
- Tres consentimientos de divulgación verificados por separado: regulatorio, de mercadeo y transfronterizo (Ley 1581/2012). Un «acepto la divulgación» genérico es insuficiente.

## Se conecta con

- Lee capacidad del rastreador; su decisión (aceptado, lista de espera, rechazado) lo actualiza y dispara el paquete de confirmación.
- Si el pedido consume el último cupo se marca «último espacio» y requiere autorización del Líder técnico.

## Reglas críticas

- Iniciales faltantes bloquean la decisión; los rechazos exigen motivo documentado y compartido con el cliente.
- Pedidos en lista de espera se rastrean con fecha y criterios de prioridad aplicados.

---

*Documento de consulta · corte al 2026-07-16 · índice: [indice.md](indice.md)*
