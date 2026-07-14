# CS-13 — Mensaje de participación y entrega del informe

**Estado:** BORRADOR — contenido redactado; aprobación pendiente
**Propietario:** Coordinador de ronda
**Requerido antes:** Informar problema
**Última revisión:** 2026-07-14 (entrega alineada con la ruta del informe final directo)
**Referencia de códigos del SGC:** ver `00_control/equivalencia_codigos_sgc.md`. El informe final está en `F-PSEA-13` (código vigente tras la renumeración del 2026-06-14; antes `F-PSEA-04`).

## Objetivo

Completar la entrega al cliente de manera consistente. El SGC ya controla el informe técnico a través de `P-PSEA-09` y `F-PSEA-13`. La capa comercial sólo necesita un mensaje de entrega controlada y, si aún no está cubierto, una declaración de participación.

## Mensaje de entrega

### Campos obligatorios

| Campo | Valor |
|---|---|
| Código de participante y ronda | [RELLENO] |
| Identificador/versión del informe adjunto | [RELLENO] |
| Aviso de confidencialidad | [RELLENO — texto estándar: "Este informe es confidencial y está destinado únicamente al participante designado. La distribución a terceros requiere autorización por escrito de CALAIRE-EA."] |
| Estado del informe | FINAL |
| Plazo de apelación | [RELLENO — 14 días calendario desde la emisión final según P-PSEA-18] |
| Instrucciones de acceso seguro o entrega | [RELLENO] |
| Recordatorio de uso de informes | **Texto estándar: NO lo modifique sin la aprobación CS-01. Ver bloque abajo.** |
| Contactos comerciales y técnicos | [RELLENO] |

### Recordatorio de uso de informe estándar (uso sin cambios)

> "El participante podrá declarar que participó en la Ronda CALAIRE-EA [ID] para los gases [LISTA]. No podrá declarar ni dar a entender que CALAIRE-EA está acreditada, que la ronda está acreditada o que el participante es técnicamente competente únicamente en virtud de su participación. El informe debe utilizarse íntegramente y sin representaciones engañosas de sus resultados o alcance. La evaluación detallada del desempeño se proporciona en el informe técnico separado. La distribución de este informe o su contenido a terceros requiere autorización escrita de CALAIRE-EA."

Este texto coincide con la redacción aprobada en CS-01 apartado 9 (“Uso del informe”). Cualquier modificación debe aprobarse tanto en CS-01 como en CS-13 en la misma revisión para evitar divergencias.

### Plantilla: informe final

```text
Asunto: CALAIRE-EA — Ronda [ID] — Participante [CÓDIGO] — Informe final

Estimado/a [CONTACTO]:

Adjuntamos el informe final de la ronda [ID].

ID del informe: [ID]
Estado: FINAL

Los comentarios o apelaciones deben presentarse dentro de los 14 días calendario
siguientes a la emisión, conforme a P-PSEA-18. Toda corrección aceptada se controla
como una revisión del informe final; no existe una etapa de informe preliminar.

RECORDATORIO SOBRE EL USO DEL INFORME (estándar):
El participante podrá declarar que participó en la Ronda CALAIRE-EA [ID] para los gases [LISTA]. No podrá declarar ni dar a entender que CALAIRE-EA está acreditada, que la ronda está acreditada o que el participante es técnicamente competente únicamente en virtud de su participación. El informe debe utilizarse íntegramente y sin representaciones engañosas de sus resultados o alcance. La evaluación detallada del desempeño se proporciona en el informe técnico separado. La distribución de este informe o su contenido a terceros requiere autorización escrita de CALAIRE-EA.

Si se requiere, se adjunta por separado una declaración de participación.

Consultas técnicas: [CONTACTO TÉCNICO]
Consultas comerciales: [CONTACTO COMERCIAL]
```

## Gestión de la falta de recepción

Si el correo electrónico del informe rebota o no se recibe acuse de recibo dentro de los 5 días hábiles:

1. El coordinador de la ronda verifica la dirección de correo electrónico con los registros CS-07 y CS-11.
2. Reenvía el informe por el canal alternativo registrado en CS-11 (correo electrónico registrado, portal o correo postal para clientes internacionales).
3. Si aún no se recibe confirmación dentro de los 5 días hábiles adicionales, pase al contacto comercial.
4. Documentar la incidencia en CS-12 (registro de cambio/cancelación) con clasificación "no-recepción".
5. No marque el informe como "entregado" en CS-10 hasta que esté archivado un recibo confirmado (recibo de lectura, entrega firmada o acuse de recibo explícito).

## Retención

Los informes finales y el registro de entrega correspondiente se conservan en el almacenamiento controlado del SGC durante un mínimo de 5 años según los requisitos de retención de registros de ISO/IEC 17043. Los registros de entrega comercial (fecha, contacto, canal) se conservan en CS-10 durante el mismo período.

## Enlace a CS-12 (cambio/cancelación)

Si un comentario o apelación en el informe final identifica un error que requiere acción comercial (cambio de alcance, cambio de tarifa, días de ronda adicionales), el contacto comercial debe:

1. Abrir un registro CS-12 con el disparador "cambio de alcance/fecha/tarifa".
2. Actualizar CS-10 (estado comercial) para reflejar el cambio en curso.
3. Emitir una cotización revisada (revisión CS-06) si las tarifas cambian.
4. Cerrar el registro CS-12 una vez emitida la revisión controlada del informe final o resuelto el cambio.

## Declaración de participación

Si aún no está cubierto por el informe del SGC, se podrá emitir una declaración de participación por separado.

### Contenido permitido

- Nombre de la organización
- ID de ronda y fecha
- Identificador del analizador
- Gases seleccionados

### Contenido prohibido

- [ ] No debe reclamar la acreditación antes de que exista.
- [ ] No debe declarar ni implicar competencia técnica.
- [ ] No debe sustituir el informe detallado de desempeño.
- [ ] No debe publicar partituras confidenciales.
- [ ] No debe utilizar a1–a7 ni una calificación general.

### Plantilla

```text
CALAIRE-EA — DECLARACIÓN DE PARTICIPACIÓN

Organización: [NOMBRE]
Ronda: [ID]
Fecha: [FECHA]
Analizador: [ID]
Gases: [LISTA]

Esta declaración confirma la participación en la ronda indicada.
No constituye una acreditación ni una declaración de competencia técnica.
La evaluación detallada del desempeño se proporciona en el informe técnico separado.
```

## Aprobación

| Versión | Fecha | Aprobador | Notas |
|---|---|---|---|
| 0.1 BORRADOR | [RELLENO] | [RELLENO] | Plantilla inicial |
| 0.2 BORRADOR | 2026-07-14 | [RELLENO] | Recordatorio estandarizado de uso de informes; Se agregó enlace CS-12, manejo sin recepción, período de retención. |
| 0.2.1 CORRECCIÓN | 2026-07-14 | [RELLENO] | Bloque estándar de uso del informe unificado con CS-01 §9 y CS-08 cláusula 16 en las dos instancias; estado actualizado a BORRADOR. |
