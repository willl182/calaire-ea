# F-PSEA-15: Registro de apelaciones

**Codigo:** F-PSEA-15  
**Tipo documental:** Registro  
**Nombre:** Registro de apelaciones  
**Version:** 1.0  
**Fecha:** 2026-06-18  
**Estado:** Preliminar — Revisar  
**Clase:** Ficha preliminar

---

## 1. Objetivo

Documentar la recepcion, evaluacion, decision y cierre de apelaciones presentadas por los participantes contra decisiones del PEA, garantizando imparcialidad, trazabilidad y confidencialidad del proceso.

## 2. Alcance

Este registro aplica a:

- Apelaciones formales recibidas por correo electronico institucional contra resultados de ensayo de aptitud, decisiones de aceptacion/rechazo o cualquier decision del esquema.
- Registro del panel revisor, fundamentos, decision y comunicacion al apelante.

No incluye:

- Quejas del PEA (eso es `F-PSEA-14`).
- Comunicaciones generales (eso es `P-PSEA-05`).
- No conformidades/CAPA (eso se gestiona en `P-PSEA-15` y `F-PSEA-14`, aunque una apelacion pueda derivar en ellas).

## 3. Responsable funcional

| Rol | Responsabilidad |
|---|---|
| Recepcionista oficial del PEA | Recibir la apelacion por correo institucional, confirmar recepcion y asignar numero de registro. |
| Responsable de calidad | Validar que la apelacion cumple requisitos formales y coordinar la revision. |
| Panel revisor | Evaluar la apelacion de manera imparcial y proponer decision fundamentada. |
| Decision designada | Emitir la decision final y asegurar su comunicacion al apelante. |
| Alta direccion del PEA | Resolver conflictos de interes y aprobar decisiones que afecten la validez del esquema. |

## 4. Momento de uso

- Al recibir una apelacion formal dentro del plazo establecido.
- Durante la conformacion y actuacion del panel revisor.
- Al comunicar la decision al apelante.
- Al cerrar el caso y archivar la evidencia.
- Cuando una apelacion deriva en NC/CAPA o afecta un informe emitido.

## 5. Campos minimos

| Campo | Descripcion |
|---|---|
| ID_apelacion | Codigo unico de seguimiento (ej. APEL-AAAA-NNN). |
| Fecha_recepcion | Fecha y hora de recepcion del correo de apelacion. |
| Apelante | Nombre, laboratorio y datos de contacto del participante. |
| Decision_apelada | Decision del PEA que se apela (resultado, informe, criterio aplicado). |
| Ronda_informe_afectado | Codigo de ronda o informe (`F-PSEA-13`) objeto de la apelacion. |
| Fundamento_apelacion | Argumentos y evidencias presentadas por el apelante. |
| Requisitos_formales | Verificacion de plazo, forma y documentacion adjunta. |
| Miembros_panel | Nombres y roles de quienes evaluan la apelacion. |
| Analisis_tecnico | Evaluacion del panel sobre la decision apelada. |
| Decision_panel | Decision fundamentada: a favor / en contra / parcial. |
| Acciones_derivadas | NC/CAPA, correccion de informe u otras acciones, si aplica. |
| Fecha_decision | Fecha de emision de la decision. |
| Fecha_comunicacion | Fecha de envio de la respuesta al apelante. |
| Medio_comunicacion | Correo formal u otro canal oficial. |
| Fecha_cierre | Fecha de cierre del caso. |
| Estado | Recibida / En revision / Decidida / Cerrada. |

## 6. Controles de calidad

- La apelacion debe recibirse por correo electronico institucional; no se gestiona en `calaire-app`.
- El panel revisor debe ser imparcial y no tener conflicto de interes con el apelante.
- La decision debe estar fundamentada tecnicamente y documentarse antes de su comunicacion.
- La respuesta al apelante debe enviarse por el mismo canal formal de recepcion.
- La informacion sensible debe protegerse conforme a `P-PSEA-16`.
- Si la apelacion deriva en NC/CAPA, debe vincularse a `P-PSEA-15` y `F-PSEA-14`.

## 7. Relaciones documentales

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `P-PSEA-18` | Procedimiento de apelaciones del PEA. | Obligatorio |
| `P-PSEA-15` | Procedimiento de TNC/NC/CAPA, si la apelacion deriva en no conformidad. | Obligatorio |
| `P-PSEA-05` | Comunicaciones oficiales del PEA. | Obligatorio |
| `P-PSEA-16` | Control de valores sensibles en apelaciones. | Obligatorio |
| `P-PSEA-17` | Quejas del PEA (diferenciadas de apelaciones). | Referencia |
| `F-PSEA-13` | Informe final de resultados, si es objeto de apelacion. | Referencia |
| `F-PSEA-14` | Registro de caso de queja o NC, si la apelacion deriva en NC/CAPA. | Referencia |

## 8. Limites

- No es el procedimiento de apelaciones; es el registro que resulta de su aplicacion (`P-PSEA-18`).
- No se gestiona en `calaire-app`; su canal oficial es el correo electronico institucional.
- No registra quejas (eso es `F-PSEA-14`).
- Su estructura es preliminar y requiere validacion antes de declararse estable.
- No sustituye la comunicacion formal ni los plazos definidos en el procedimiento.
