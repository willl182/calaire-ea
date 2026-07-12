# F-PSEA-03 Registro de participacion

**Codigo:** F-PSEA-03  
**Version:** 0  
**Tipo:** Formato maestro / registro digital  
**Aplicacion:** Carga y actualizacion de datos del participante en `calaire-app`.

---

## 1. Objetivo

Registrar en `calaire-app` la informacion suministrada por cada participante para una ronda de ensayo de aptitud, incluyendo datos de contacto, personal autorizado, alcance de participacion, equipos declarados, condiciones logisticas y aceptacion de condiciones de participacion.

---

## 2. Alcance

Este formato aplica desde la invitacion o apertura de inscripcion hasta el cierre de la informacion pre-ronda del participante. Es el registro primario que diligencia o actualiza el participante en la aplicacion.

No reemplaza:

- El anexo tecnico de equipos exportado desde este registro (`F-PSEA-04`).
- La ficha basica de ronda (`F-PSEA-05`).
- La planificacion completa de ronda (`F-PSEA-06`).
- Los datos de medicion reportados durante la ejecucion (`F-PSEA-08`).

---

## 3. Responsable funcional

| Rol | Responsabilidad |
|---|---|
| Participante | Cargar y mantener completa la informacion solicitada en `calaire-app`. |
| Coordinacion del PEA | Revisar completitud, aprobar estados de participacion y solicitar correcciones. |
| Responsable tecnico | Verificar coherencia tecnica de equipos, analitos y requisitos de instalacion. |
| Responsable de calidad | Asegurar trazabilidad, confidencialidad y conservacion del registro oficial. |

---

## 4. Campos minimos

### 4.1 Identificacion del participante

| Campo | Descripcion |
|---|---|
| Codigo_ronda | Identificador de la ronda. |
| Codigo_participante | Codigo anonimo asignado por el esquema. |
| Entidad_laboratorio | Nombre de la entidad o laboratorio participante. |
| NIT_identificacion | Identificacion institucional cuando aplique. |
| Ciudad | Ciudad de operacion del participante. |
| Contacto_principal | Nombre y rol del contacto oficial. |
| Correo_contacto | Correo oficial para comunicaciones de ronda. |
| Telefono_contacto | Telefono de contacto operativo. |

### 4.2 Participacion y alcance

| Campo | Descripcion |
|---|---|
| Estado_participacion | Invitado, inscrito, confirmado, retirado, no elegible o cerrado. |
| Analitos_participa | CO, SO2, O3, NO, NO2 u otros definidos por la ronda. |
| Ronda_preferida | Ventana o ronda solicitada cuando haya alternativas. |
| Ronda_asignada | Ronda finalmente asignada por coordinacion. |
| Acepta_condiciones | Confirmacion de lectura y aceptacion de condiciones de participacion. |
| Acepta_confidencialidad | Declaracion de confidencialidad y no divulgacion previa. |

### 4.3 Personal y acceso

| Campo | Descripcion |
|---|---|
| Personal_autorizado | Nombres, identificacion y rol del personal que ingresara. |
| Requisitos_ingreso | Datos necesarios para permisos, SST o control de acceso. |
| Observaciones_acceso | Restricciones o necesidades especiales informadas por el participante. |

### 4.4 Informacion tecnica y logistica

| Campo | Descripcion |
|---|---|
| Equipos_declarados | Relacion de analizadores e instrumentos cargados por el participante. |
| Servicios_requeridos | Energia, espacio, gases auxiliares permitidos, conectividad u otros. |
| Transporte_equipos | Medio, fecha estimada de llegada y necesidades de apoyo. |
| Observaciones_tecnicas | Informacion adicional relevante para planificacion. |

---

## 5. Salidas desde `calaire-app`

| Salida | Uso |
|---|---|
| Registro individual del participante | Evidencia de inscripcion, confirmacion y aceptacion. |
| Estado consolidado de participantes | Seguimiento de completitud y cierre pre-ronda. |
| `F-PSEA-04` Equipos e instrumentos | Exportacion tecnica de equipos declarados por participante. |
| Insumos para `F-PSEA-06` | Participantes, analitos, accesos, recursos y restricciones para la planificacion completa. |

---

## 6. Reglas de diligenciamiento

- Cada participante debe tener un unico registro activo por ronda.
- La informacion de equipos declarados debe poder exportarse como `F-PSEA-04`.
- El cambio de estado de participacion debe conservar fecha, responsable y justificacion cuando aplique.
- Los datos personales se tratan como informacion confidencial y se controlan conforme a `P-PSEA-19`.
- La informacion usada para planificar la ronda debe estar cerrada antes de aprobar `F-PSEA-06`.

---

## 7. Relacion documental

| Documento | Relacion |
|---|---|
| `DG-PSEA-02` | Aplicativo donde se carga y conserva el registro. |
| `I-PSEA-02` | Instructivo para diligenciamiento por participante. |
| `I-PSEA-03` | Instructivo de administracion y seguimiento interno. |
| `P-PSEA-03` | Control de registros y evidencias. |
| `P-PSEA-04` | Planificacion de ronda que usa la informacion cargada. |
| `P-PSEA-05` | Comunicaciones asociadas a apertura, correccion y cierre. |
| `F-PSEA-04` | Exportacion de equipos declarados desde este registro. |
| `F-PSEA-06` | Planificacion completa alimentada por el registro. |

---

## 8. Criterio de completitud

El registro se considera completo cuando el participante tiene estado definido, datos de contacto validos, personal autorizado, analitos confirmados, condiciones de participacion aceptadas y equipos declarados con informacion suficiente para exportar `F-PSEA-04`.
