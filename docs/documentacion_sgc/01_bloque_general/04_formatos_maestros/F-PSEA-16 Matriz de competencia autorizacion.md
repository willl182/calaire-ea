# F-PSEA-16: Matriz de competencia/autorización

**Codigo:** F-PSEA-16  
**Tipo documental:** Matriz  
**Nombre:** Matriz de competencia/autorización  
**Version:** 1.0  
**Fecha:** 2026-06-18  
**Estado:** Preliminar — Mantener / Actualizar  
**Clase:** Ficha preliminar

---

## 1. Objetivo

Documentar los requisitos de competencia, formacion, experiencia y autorizacion de los roles tecnicos y operativos del PEA, de forma que solo personal calificado ejecute funciones criticas y autorice informes oficiales.

## 2. Alcance

Esta matriz aplica a:

- Roles tecnicos y operativos del PEA (planificacion, operacion de aplicativos, analisis estadistico, emision de informes, preparacion del item, gestion de calidad).
- Registro de formacion, experiencia, autorizaciones vigentes y renovaciones.

No incluye:

- Talento humano general de la institucion.
- Competencia de proveedores externos (eso se documenta en `F-PSEA-17`).
- Proceso de evaluacion de desempeno institucional.

## 3. Responsable funcional

| Rol | Responsabilidad |
|---|---|
| Responsable de talento humano del PEA | Mantener la matriz actualizada y consolidar evidencia de formacion y experiencia. |
| Responsable de calidad | Verificar que cada rol cumpla los requisitos de competencia definidos en `P-PSEA-20`. |
| Responsable tecnico | Validar autorizaciones para funciones criticas y emision de informes. |
| Alta direccion del PEA | Aprobar autorizaciones para emision de informes finales y funciones de alto impacto. |

## 4. Momento de uso

- Al incorporar un nuevo rol o persona al PEA.
- Al definir o actualizar requisitos de competencia en `P-PSEA-20`.
- Antes de autorizar la emision de un informe final (`P-PSEA-09`).
- En auditorias internas o revisiones de gestion del PEA.
- Al renovar formaciones, autorizaciones o cuando cambian las funciones de una persona.

## 5. Campos minimos

| Campo | Descripcion |
|---|---|
| ID_rol | Identificacion del rol en el PEA. |
| Nombre_persona | Nombre del recurso humano asignado al rol. |
| Funciones_PEA | Funciones especificas que desempena en el ensayo de aptitud. |
| Formacion_requerida | Titulo, cursos o certificaciones exigidas para el rol. |
| Formacion_acreditada | Evidencia de formacion cumplida (diplomas, certificados). |
| Experiencia_requerida | Anios o proyectos minimos exigidos. |
| Experiencia_documentada | Resumen de experiencia relevante demostrada. |
| Competencias_tecnicas | Conocimientos especificos (ISO/IEC 17043, ISO 13528, metrologia, estadistica, gases). |
| Autorizacion | Funciones para las que esta autorizado (ej. emitir informes, operar aplicativos). |
| Fecha_autorizacion | Fecha de otorgamiento de la autorizacion. |
| Vigencia_autorizacion | Fecha de vencimiento o periodo de renovacion. |
| Responsable_autorizacion | Persona que otorgo la autorizacion. |
| Restricciones | Limitaciones de alcance en la autorizacion, si aplica. |
| Estado | Activo / En formacion / Suspendido / Vencido. |

## 6. Controles de calidad

- Cada rol debe estar definido en `P-PSEA-20` con requisitos de competencia claros.
- La formacion y experiencia deben contar con evidencia documental soporte.
- Las autorizaciones para emitir informes deben ser aprobadas por quien corresponda segun la estructura del PEA.
- La matriz debe revisarse al menos una vez al anio o ante cambios de personal o funciones.
- Las autorizaciones vencidas deben identificarse y renovarse antes de ejecutar funciones criticas.
- La informacion de personal debe manejarse con confidencialidad conforme a `P-PSEA-19`.

## 7. Relaciones documentales

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `P-PSEA-20` | Procedimiento de competencia y autorizacion operativa del PEA. | Obligatorio |
| `P-PSEA-19` | Confidencialidad operativa, que protege el acceso a la informacion de la matriz. | Obligatorio |
| `P-PSEA-21` | Proveedores criticos, para competencia de terceros que no se incluye en esta matriz. | Obligatorio |
| `P-PSEA-09` | Emision de informes, que requiere autorizacion registrada en esta matriz. | Referencia |
| `P-PSEA-07` | Analisis estadistico, que requiere competencia demostrada. | Referencia |

## 8. Limites

- No es el procedimiento de competencia; es la matriz documental que soporta `P-PSEA-20`.
- No cubre talento humano general; solo roles tecnicos y operativos del PEA.
- No documenta evaluacion de proveedores (eso es `F-PSEA-17`).
- Su estructura es preliminar y requiere validacion antes de declararse estable.
- No reemplaza los registros de formacion institucional ni los expedientes de personal.
