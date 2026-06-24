# F-PSEA-05A: Hoja de registro del participante

**Codigo:** F-PSEA-05A  
**Tipo documental:** Formato  
**Nombre:** Hoja de registro del participante  
**Version:** 1.0  
**Fecha:** 2026-06-18  
**Estado:** Preliminar — Subformato derivado de F-PSEA-05  
**Clase:** Plantilla maestra / subformato operativo

---

## 1. Objetivo

Recopilar la informacion tecnica, logistica y de contacto de cada participante antes de una ronda de ensayo de aptitud, para planificar espacios, equipos, ingreso a instalaciones y asignacion de codigos anonimos.

## 2. Alcance

Este formato aplica como plantilla maestra para:

- Registro de datos del participante, acompanantes y personal que ingresara a las instalaciones.
- Declaracion de analizadores, instrumentos auxiliares y equipos de transporte.
- Confirmacion de disponibilidad, confidencialidad y aceptacion de condiciones de participacion.

No incluye:

- La lista maestra consolidada de participantes (eso es `F-PSEA-07`).
- El plan de ronda completo (eso es `F-PSEA-05`).
- Los datos reportados durante la ejecucion de la ronda (eso es `F-PSEA-08`).
- El informe final de resultados (eso es `F-PSEA-13`).

## 3. Responsable funcional

| Rol | Responsabilidad |
|---|---|
| Coordinador de ronda | Personalizar y enviar la hoja de registro a cada participante. |
| Participante | Diligenciar la informacion con veracidad y dentro del plazo establecido. |
| Responsable de logistica | Verificar que la informacion permita planificar espacios, ingresos y puestos de trabajo. |
| Responsable de calidad | Asegurar que las declaraciones de confidencialidad y condiciones de participacion queden documentadas. |

## 4. Momento de uso

- Durante la comunicacion pre-ronda a los participantes confirmados.
- Como minimo con la antelacion definida en `P-PSEA-04` y `P-PSEA-05`.
- Al recibir la hoja diligenciada, antes de consolidarla en `F-PSEA-07`.
- Durante la gestion de ingresos a las instalaciones y asignacion de puestos en el manifold.

## 5. Campos minimos

### 5.1. Datos del participante y contacto

| Campo | Descripcion |
|---|---|
| Codigo_ronda | Identificacion de la ronda a la cual se inscribe el participante. |
| Codigo_participante | Codigo anonimo asignado por el coordinador (P1, P2, etc.). |
| Nombre_participante | Nombre completo del titular. |
| Documento_identidad | Numero de identificacion para autorizacion de ingreso. |
| Correo_electronico | Correo oficial para comunicaciones. |
| Telefono | Numero de contacto. |
| Laboratorio_entidad | Nombre del laboratorio o entidad participante. |
| Cargo_rol | Funcion del titular en la ronda. |

### 5.2. Acompanantes

| Campo | Descripcion |
|---|---|
| Nombre_acompanante | Nombre completo de la persona adicional. |
| Documento_acompanante | Numero de identificacion. |
| Rol_acompanante | Funcion durante la ronda. |

### 5.3. Equipos a utilizar

| Campo | Descripcion |
|---|---|
| Analito | Gas contaminante criterio que mide el equipo. |
| Fabricante | Marca del analizador. |
| Modelo_referencia | Modelo o referencia del equipo. |
| Numero_serie | Serial del analizador. |
| Principio_medicion | Tecnica de medicion (NDIR, UV fotometrico, quimioluminiscencia, etc.). |
| Metodo_US_EPA | Metodo de referencia declarado, si aplica. |
| Fecha_ultima_calibracion | Fecha de la ultima calibracion. |
| Certificado_calibracion_vigente | Confirmacion de vigencia del certificado (Si/No). |
| Incertidumbre_expandida | Valor U (k=2) declarado por el participante. |
| Unidad_salida | Unidad de salida del equipo. |

### 5.4. Instrumentos auxiliares

| Campo | Descripcion |
|---|---|
| Descripcion_equipo | Tipo de equipo auxiliar (computador, cables, cilindros, reguladores, etc.). |
| Marca_modelo | Marca y modelo. |
| Numero_serie | Serial, si aplica. |
| Cantidad | Numero de unidades declaradas. |

### 5.5. Logistica

| Campo | Descripcion |
|---|---|
| Medio_transporte | Vehiculo propio, taxi, transporte publico u otro. |
| Fecha_estimada_llegada | Fecha prevista de llegada con equipos. |
| Hora_estimada_llegada | Hora prevista de llegada. |
| Requiere_ayuda_montaje | Indicacion de si necesita apoyo para montaje (Si/No). |
| Requiere_estacionamiento | Indicacion de necesidad de parqueadero. |
| Observaciones | Requerimientos especiales o restricciones. |

### 5.6. Declaraciones del participante

| Campo | Descripcion |
|---|---|
| Acepta_condiciones | Confirmacion de lectura y aceptacion de las condiciones de participacion. |
| Compromiso_confidencialidad | Compromiso de no divulgar resultados antes de la publicacion oficial. |
| Disponibilidad_equipos | Confirmacion de que los equipos declarados estaran disponibles y operativos. |
| Veracidad_datos | Declaracion de que la informacion suministrada es veraz. |
| Acuerdo_anonimato | Entendimiento de que los resultados se reportaran con codigo anonimo. |
| Nombre_firma | Nombre y firma del participante. |
| Fecha_firma | Fecha de la declaracion. |

### 5.7. Uso interno del coordinador

| Campo | Descripcion |
|---|---|
| Fecha_recibido | Fecha de recepcion del formulario diligenciado. |
| Ingreso_universidad_gestionado | Estado de gestion de ingreso a instalaciones. |
| Puesto_manifold_asignado | Puerto o puesto de trabajo asignado. |
| Consolidado_F-PSEA-07 | Confirmacion de traslado a la lista maestra de participantes. |
| Observaciones_coordinador | Notas internas sobre logistica o seguimiento. |

## 6. Controles de calidad

- La hoja debe enviarse como plantilla maestra y retornar como copia diligenciada por cada participante.
- Los datos tecnicos de los equipos deben ser consistentes con la capacidad de medicion declarada para la ronda.
- Los certificados de calibracion deben estar vigentes al momento de la ronda.
- Las declaraciones de confidencialidad y anonimato deben quedar registradas antes del inicio de la ronda.
- La informacion personal debe manejarse conforme a `P-PSEA-16` y `P-PSEA-19`.
- Al recibirse, la informacion debe consolidarse en `F-PSEA-07` y usarse para planificar logistica.

## 7. Relaciones documentales

| Codigo | Relacion |
|---|---|
| `F-PSEA-05` | Plan de ronda EA, del cual este formato es subformato derivado. |
| `F-PSEA-07` | Lista maestra de participantes, que se alimenta de este formato. |
| `P-PSEA-04` | Planificacion de ronda EA. |
| `P-PSEA-05` | Comunicaciones oficiales del PEA. |
| `I-PSEA-02` | Instructivo para participante. |
| `P-PSEA-16` | Control de valores sensibles en la informacion recolectada. |
| `P-PSEA-19` | Confidencialidad operativa. |

## 8. Limites

- Es un subformato derivado de `F-PSEA-05`; no reemplaza el plan de ronda ni la lista maestra de participantes.
- Este archivo es la plantilla maestra. Las copias diligenciadas por cada participante y las versiones con sufijos operativos (P1, P2, DIL, etc.) son evidencias de ronda, no el maestro.
- No registra datos de medicion ni resultados de aptitud.
- No es un acuerdo de confidencialidad formal, aunque recoge la declaracion del participante.
- Su estructura es preliminar y requiere validacion antes de declararse estable.
- La informacion de equipos declarada aqui se consolida en la lista maestra de participantes (`F-PSEA-07`) y se vincula con el anexo tecnico de equipos del mapa documental vigente (`F-PSEA-04`).
