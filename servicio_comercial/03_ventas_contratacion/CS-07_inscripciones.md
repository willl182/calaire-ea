# CS-07 — Formulario de inscripción / pedido

**Propietario:** Profesional de proyectos
**Última revisión:** 2026-07-14 (marca de tiempo/IP/canal agregado, prioridad de la lista de espera, estado de cotización revisado, referencia del código SGC aclarada para datos técnicos)

## Objetivo

Captura de comprador, alcance seleccionado y datos administrativos. Reutiliza los campos técnicos de aplicaciones/SGC existentes en lugar de duplicarlos.

## Reutilizar en lugar de duplicar

Utilice la `calaire-app` existente y los campos técnicos del SGC para los datos de registro y equipos. Las referencias actuales de los campos del SGC (post-renumeración 2026-06-14) son:

- Datos de equipos e instrumentos: `F-PSEA-04` (antiguo `F-PSEA-05A`)
- Registro de participantes: `F-PSEA-03` (antiguo `F-PSEA-05`)

Ver `00_control/equivalencia_codigos_sgc.md` para el mapeo completo.

Agregue una sección comercial en lugar de crear un segundo sistema de registro técnico.

## Campos comerciales/legales para agregar

| Campo | Requerido | Notas |
|---|---|---|
| Nombre legal del cliente | Sí | Debe coincidir con los registros de impuestos |
| Identificación tributaria | Sí | |
| Dirección de facturación | Sí | |
| Contacto de facturación | Sí | |
| Número de cotización/orden de compra | Sí | Enlaces a CS-06 (deben ser válidos, no estar vencidos y no haber sido aceptados por otra parte) |
| Paquete de gases seleccionado | Sí | CO, SO₂, NO, NO₂, O₃ |
| Cantidad de analizadores | Sí | |
| Idioma del informe solicitado | Sí | Derivado de la pregunta 15 del CS-05 |
| Aceptación de los términos | Sí | Casilla de verificación / firma |
| Selección de confidencialidad / divulgación | Sí | Según `P-PSEA-19` (vigente tras la renumeración) |
| Consentimiento de marketing del participante | Sí | Separado del consentimiento del servicio; Texto de cumplimiento Ley 1581/2012 requerido |
| Contacto contractual autorizado | Sí | |
| Contacto técnico autorizado | Sí | |
| Documentos especiales de facturación / portal de adquisiciones | No | Si corresponde |
| **Marca de tiempo de aceptación** | Sí | ISO 8601 con zona horaria; capturado automáticamente por el portal o anotado por el cliente comercial si es en papel |
| **Canal de aceptación** | Sí | Portal / correo electrónico / PDF firmado / papel; facilita la resolución de controversias |
| **IP / origen de la aceptación (si se usa el portal)** | Sí (si se usa el portal) | Para auditoría; no se requiere en papel ni por correo electrónico |
| **Prioridad en lista de espera** | Opcional (completar automáticamente) | Completado por CS-10 si estado = En lista de espera; basado en criterios de prioridad CS-01 |
| Firma/fecha de aceptación | Sí | Fecha del lado del cliente (puede diferir de la marca de tiempo de aceptación si es postal) |

## Lógica de estado

```text
Interés → Cotizado → Inscrito → En revisión →
Aceptado, pendiente de pago/orden de compra → Confirmado → En lista de espera / Rechazado / Retirado
            │
            └──→ Revisión de cotización en curso (transitorio)
                  → volver a Cotizado con el número de cotización revisada
```

**Sucursal:** cuando un cliente acepta una cotización que requiere revisión (por ejemplo, la capacidad de la ronda cambió, el cliente desea agregar gas, el precio debe volver a cotizarse), el registro pasa a "Cotización-revisión en curso" antes de regresar a "Cotizada" con un nuevo número de cotización. La familia de cotizaciones original se registra como "reemplazada" y se abre un registro CS-12.

Solo los participantes **"confirmados"** pasan a la planificación formal de la ronda.

## Lista de verificación de la inscripción

- [] Campos técnicos completados (a través de `calaire-app` y los campos SGC mencionados anteriormente).
- [ ] Campos comerciales completados.
- [ ] Términos aceptados.
- [ ] Consentimiento de divulgación registrado.
- [ ] Consentimiento de comercialización registrado por separado con texto explícito de la Ley 1581.
- [ ] Número de cotización válido y que coincide con la selección (y que aún no ha sido aceptado por otra parte).
- [ ] Marca de tiempo / canal de aceptación registrados.
- [ ] Se inició la revisión del contrato (CS-09).
- [ ] Si estado = En lista de espera, se registra la prioridad de la lista de espera (CS-10) y se notifica al cliente.
