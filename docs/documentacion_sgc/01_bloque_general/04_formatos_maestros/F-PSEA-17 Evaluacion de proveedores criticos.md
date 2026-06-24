# F-PSEA-17: Evaluación de proveedores críticos

**Codigo:** F-PSEA-17  
**Tipo documental:** Registro  
**Nombre:** Evaluación de proveedores críticos  
**Version:** 1.0  
**Fecha:** 2026-06-18  
**Estado:** Preliminar — Mantener / Actualizar  
**Clase:** Ficha preliminar

---

## 1. Objetivo

Documentar la evaluacion, seleccion, seguimiento y decision de aprobacion o rechazo de proveedores y servicios criticos para el PEA, garantizando que su desempeno no afecte la validez de los ensayos de aptitud.

## 2. Alcance

Este registro aplica a:

- Proveedores de cilindros de gas patron, calibradores dinamicos, equipos de medicion y otros insumos que afecten la validez del item de ensayo.
- Servicios criticos como software de gestion, mantenimiento especializado, transporte de equipos sensibles y servicios de calibracion externa.
- Evaluaciones iniciales, reevaluaciones periodicas y registros de desempeno.

No incluye:

- Compras generales o servicios administrativos que no afecten la validez del EA.
- Evaluacion de competencia del personal interno (eso es `F-PSEA-16`).
- Gestion de contratos o acuerdos de confidencialidad, aunque si los referencia.

## 3. Responsable funcional

| Rol | Responsabilidad |
|---|---|
| Responsable de compras y proveedores del PEA | Iniciar y consolidar la evaluacion de proveedores criticos. |
| Responsable tecnico | Definir criterios tecnicos de aceptacion y validar la idoneidad del proveedor. |
| Responsable de calidad | Verificar que la evaluacion cumpla los requisitos de `P-PSEA-21` y los limites de tercerizacion de ISO/IEC 17043. |
| Alta direccion del PEA | Aprobar la lista de proveedores criticos y las decisiones de rechazo. |

## 4. Momento de uso

- Antes de contratar o aprobar un nuevo proveedor critico.
- Durante la reevaluacion periodica de proveedores aprobados.
- Cuando un proveedor incumple especificaciones o presenta desviaciones.
- Al actualizar la lista de proveedores criticos del PEA.
- Antes de utilizar un proveedor en la preparacion del item de ensayo (`P-PSEA-06`).

## 5. Campos minimos

| Campo | Descripcion |
|---|---|
| ID_proveedor | Codigo interno de identificacion del proveedor. |
| Nombre_proveedor | Razon social o nombre del proveedor. |
| Tipo_servicio | Cilindro de gas, calibrador, software, mantenimiento, transporte, calibracion externa, otro. |
| Criterios_evaluacion | Requisitos tecnicos, metrologicos, de trazabilidad, experiencia y capacidad definidos. |
| Evidencia_soportes | Certificados, acreditaciones, informes de desempeno, referencias, visitas tecnicas. |
| Evaluacion_inicial | Resultado de la evaluacion previa al primer uso: aprobado / condicional / rechazado. |
| Fecha_aprobacion | Fecha en que se aprobo al proveedor. |
| Vigencia_aprobacion | Periodo de validez de la aprobacion. |
| Seguimiento_desempeno | Registro de incumplimientos, desviaciones o resultados de seguimiento. |
| Reevaluacion | Resultado y fecha de la evaluacion periodica. |
| Decision_actual | Aprobado / Suspendido / Rechazado / En observacion. |
| Alcance_aprobado | Servicios o productos especificos autorizados. |
| Limitaciones | Restricciones de tercerizacion segun ISO/IEC 17043. |
| Observaciones | Notas sobre riesgos, acciones correctivas o condiciones especiales. |

## 6. Controles de calidad

- Los criterios de evaluacion deben estar definidos en `P-PSEA-21` y ser acordes al riesgo del servicio.
- La trazabilidad de productos criticos (cilindros, calibradores) debe verificarse antes de la aprobacion.
- Las aprobaciones deben revisarse periodicamente y actualizarse ante cambios de desempeno.
- Los proveedores suspendidos o rechazados deben quedar claramente identificados para evitar su uso.
- Se debe respetar el alcance de tercerizacion permitido por ISO/IEC 17043.
- Los cambios de proveedor critico deben evaluarse antes de afectar la preparacion del item de ensayo.

## 7. Relaciones documentales

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `P-PSEA-21` | Procedimiento de proveedores criticos del PEA. | Obligatorio |
| `P-PSEA-20` | Competencia y autorizacion, para evaluar competencia de terceros que prestan servicios criticos. | Obligatorio |
| `P-PSEA-06` | Preparacion y control del item, que utiliza proveedores aprobados. | Obligatorio |
| `P-PSEA-07` | Criterio estadistico, que puede verse afectado por la calidad de insumos y servicios. | Referencia |
| `F-PSEA-07` | Preparacion y control del item, donde se registra trazabilidad de insumos criticos. | Referencia |

## 8. Limites

- No es el procedimiento de proveedores; es el registro que resulta de su aplicacion (`P-PSEA-21`).
- No cubre compras generales ni servicios administrativos; solo los que afectan la validez del EA.
- No es un contrato ni un acuerdo de confidencialidad, aunque puede referenciarlos.
- Su estructura es preliminar y requiere validacion antes de declararse estable.
- No autoriza tercerizaciones fuera de los limites establecidos por ISO/IEC 17043.
