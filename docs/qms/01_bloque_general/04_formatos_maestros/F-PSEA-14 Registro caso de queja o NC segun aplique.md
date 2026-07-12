# F-PSEA-14: Registro/caso de queja o NC según aplique

**Codigo:** F-PSEA-14  
**Tipo documental:** Registro  
**Nombre:** Registro/caso de queja o NC según aplique  
**Version:** 1.0  
**Fecha:** 2026-06-18  
**Estado:** Preliminar — Revisar  
**Clase:** Ficha preliminar

---

## 1. Objetivo

Documentar la recepcion, evaluacion, respuesta y cierre de quejas recibidas en el PEA y de los casos de no conformidad (NC) o trabajo no conforme (TNC) que de ellas se deriven, de forma que quede trazabilidad del ciclo completo del caso SGC.

## 2. Alcance

Este registro aplica a:

- Quejas de participantes u otras partes interesadas sobre el desarrollo del ensayo de aptitud.
- Casos de trabajo no conforme (TNC) o no conformidades (NC) detectados en operaciones del PEA.
- Acciones correctivas/preventivas (CAPA) asociadas a una queja o NC.

No incluye:

- Apelaciones contra resultados de EA (eso es `F-PSEA-15`).
- Colusion o falsificacion (eso se gestiona en `P-PSEA-14`, pudiendo derivar aqui si se confirma una NC).
- Comunicaciones generales del PEA (eso es `P-PSEA-05`).

## 3. Responsable funcional

| Rol | Responsabilidad |
|---|---|
| Responsable del caso SGC | Registrar el caso en `calaire-app`, documentar la queja/NC y coordinar la respuesta. |
| Responsable de calidad | Evaluar si la queja deriva en NC/TNC y aprobar el plan de accion. |
| Responsable de area afectada | Ejecutar acciones correctivas/preventivas y evidenciar su cierre. |
| Alta direccion del PEA | Aprobar cierre cuando la queja o NC afecte la conformidad del ensayo o la imagen del esquema. |

## 4. Momento de uso

- Al recibir una queja formal por cualquier canal oficial.
- Al detectar un TNC/NC durante la operacion del PEA.
- Durante el seguimiento de acciones derivadas hasta su cierre.
- Al reportar metricas de quejas y NC en revisiones de gestion.

## 5. Campos minimos

| Campo | Descripcion |
|---|---|
| ID_caso | Codigo unico del caso SGC en `calaire-app`. |
| Fecha_recepcion | Fecha y hora de recepcion de la queja o deteccion de la NC. |
| Canal_recepcion | Medio por el cual se recibio (correo, telefono, aplicativo, reunion). |
| Tipo | Queja / TNC / NC / CAPA derivada. |
| Origen | Participante, auditoria interna, operacion, otro. |
| Descripcion | Narrativa completa de la queja o no conformidad. |
| Referencia_ronda | Codigo de ronda afectada, si aplica. |
| Referencia_informe | Codigo de informe afectado (`F-PSEA-13`), si aplica. |
| Analisis_causa | Causa raiz identificada, si deriva en NC/CAPA. |
| Accion_inmediata | Correccion o mitigacion aplicada sin demora. |
| Accion_correctiva | Accion planificada para eliminar la causa raiz. |
| Responsable_accion | Persona asignada a la accion correctiva. |
| Fecha_compromiso | Fecha limite para ejecutar la accion. |
| Verificacion_eficacia | Evidencia de que la accion fue efectiva. |
| Fecha_cierre | Fecha de cierre del caso. |
| Estado | Abierto / En seguimiento / Cerrado / Escalado. |

## 6. Controles de calidad

- Cada caso debe tener un ID unico y correlativo en `calaire-app`.
- La clasificacion como queja, TNC, NC o CAPA debe ser validada por el responsable de calidad.
- Las causas raiz y acciones correctivas deben ser verificables y pertinentes.
- Los casos cerrados deben contar con evidencia de eficacia antes del cierre.
- Los casos que afecten la validez de un informe emitido deben vincularse a `F-PSEA-13` y `P-PSEA-09`.
- La informacion sensible debe manejarse conforme a `P-PSEA-16` (control de valores sensibles).

## 7. Relaciones documentales

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `P-PSEA-17` | Procedimiento de quejas del PEA. | Obligatorio |
| `P-PSEA-15` | Procedimiento de TNC/NC/CAPA que gobierna los casos que derivan en no conformidad. | Obligatorio |
| `P-PSEA-05` | Comunicaciones oficiales del PEA. | Obligatorio |
| `DG-PSEA-02` | Aplicativo `calaire-app` donde se gestionan los casos SGC. | Obligatorio |
| `P-PSEA-14` | Colusion y falsificacion, si el caso lo involucra. | Referencia |
| `P-PSEA-08` | Flujo tecnico de datos digitales, si la NC afecta registros o informes. | Referencia |
| `F-PSEA-13` | Informe final de resultados, si el caso lo afecta. | Referencia |

## 8. Limites

- No es el procedimiento de quejas; es el registro que resulta de su aplicacion (`P-PSEA-17`).
- No es el procedimiento de TNC/NC/CAPA; es la evidencia documental del caso (`P-PSEA-15`).
- No gestiona apelaciones (`P-PSEA-18` / `F-PSEA-15`).
- Su estructura es preliminar y requiere validacion antes de declararse estable.
- No sustituye los registros de comunicacion formal ni los acuerdos de confidencialidad.
