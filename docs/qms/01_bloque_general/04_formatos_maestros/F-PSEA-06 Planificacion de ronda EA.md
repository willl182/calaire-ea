# F-PSEA-06 Planificacion de ronda EA

**Codigo:** F-PSEA-06  
**Nivel:** 4 — Formato / Registro  
**Estado:** Formato maestro para planificacion completa de ronda  
**Aplicacion:** Planificacion tecnica, logistica, metrologica y documental de una ronda especifica.

---

## 1. Proposito del formato

Formato completo para planificar, aprobar y controlar la ejecucion de una ronda especifica del esquema CALAIRE-EA. Consolida identificacion, alcance tecnico, participantes, equipos exportados desde `F-PSEA-03` como `F-PSEA-04`, recursos criticos, cronograma, enfoque estadistico pre-ronda, puntos A-U de ISO/IEC 17043:2023 7.2.1.3 y aprobaciones requeridas antes de iniciar actividades en laboratorio.

---

## 2. Trazabilidad normativa

| Norma | Clausula(s) |
|-------|-------------|
| ISO/IEC 17043:2023 | 7.1, 7.2.1.3, 7.4, 7.5 |
| ISO 13528:2022 | 5 |

**Justificacion:** Registro completo del plan aprobado de cada ronda.

---

## 3. Identificacion y control documental

| Campo | Dato |
|-------|------|
| Codigo interno de ronda | |
| Nombre de la ronda | |
| Tipo de ronda | |
| Semana operativa | |
| Jornada(s) de medicion | |
| Sede de ejecucion | |
| Version del plan | |
| Fecha de elaboracion | |
| Elaboro | |
| Reviso | |
| Aprobo | |

---

## 4. Alcance tecnico de la ronda

| Aspecto | Definicion aprobada |
|---|---|
| Participantes previstos | |
| Numero de participantes | |
| Analitos | |
| Naturaleza del item PT | |
| Base metrologica del valor asignado | |
| Enfoque estadistico | |
| Puntaje aplicable | |
| Criterios de aceptacion operativa | |

---

## 5. Participantes, contactos y prerrequisitos

| Insumo | Registro asociado | Estado |
|---|---|---|
| Registro de participacion cargado por participante | `F-PSEA-03` | |
| Equipos e instrumentos exportados | `F-PSEA-04` | |
| Personal autorizado e ingreso | `F-PSEA-03` / comunicaciones | |
| Confirmacion de instrucciones y condiciones | `F-PSEA-03` / `F-PSEA-18` | |

**Prerrequisitos de participacion**

- Registro `F-PSEA-03` completo y revisado antes del cierre pre-ronda.
- Exportacion `F-PSEA-04` disponible para revisar equipos, instrumentos y compatibilidad tecnica.
- Confirmacion de asistencia, personal visitante y equipos a ingresar.
- Aceptacion de condiciones de participacion, confidencialidad y reporte.

---

## 6. Recursos criticos y condiciones de operacion

| Recurso | Registro requerido | Estado |
|---|---|---|
| Materiales de referencia / CRM | Proveedor, lote, certificado, vigencia | |
| Sistema de dilucion o generacion | Equipo, serial, estado de verificacion | |
| Aire cero / suministro auxiliar | Fuente y condicion operativa | |
| Manifold de distribucion | Identificacion, puertos habilitados, limpieza | |
| Respaldo electrico | Equipo asignado y autonomia | |
| Monitoreo ambiental | Temperatura, presion, HR | |
| Servicios o proveedores criticos | Identificacion y evaluacion cuando aplique | |

---

## 7. Roles y responsabilidades

| Actividad | Coordinacion EA | Responsable tecnico | Soporte metrologico / estadistico | Apoyo logistico | Participante |
|---|---|---|---|---|---|
| Apertura y comunicacion pre-ronda | A/R | C | I | I | I |
| Revision de `F-PSEA-03` | A/R | C | I | C | R |
| Revision de `F-PSEA-04` | C | A/R | C | I | C |
| Preparacion del item PT | I | A/R | C | C | I |
| Definicion de `x_pt`, `u(x_pt)` y `sigma_pt` | I | C | A/R | I | I |
| Check-in, montaje y asignacion de puerto | C | R | I | A/R | R |
| Ejecucion de medicion | I | A/R | C | I | R |
| Recepcion y control de datos | A/R | C | C | I | R |
| Cierre, desmontaje y tratamiento de incidentes | A | R | I | A/R | C |

**Convencion:** `A` aprueba, `R` ejecuta, `C` consulta/apoya, `I` recibe informacion.

---

## 8. Cronograma operativo de la ronda

| Momento | Actividad | Responsable | Registro asociado |
|---|---|---|---|
| T-14 | Envio de instrucciones y apertura/cierre de carga de datos | Coordinacion EA | `F-PSEA-03`, `F-PSEA-18` |
| T-7 | Confirmacion de participantes, equipos y acceso | Coordinacion EA / Responsable tecnico | `F-PSEA-03`, `F-PSEA-04` |
| T-3 | Verificacion documental y tecnica final | Coordinacion EA | `F-PSEA-06`, `F-PSEA-04` |
| Dia 0 | Ingreso, instalacion y acondicionamiento | Coordinacion EA + Responsable tecnico | `F-PSEA-07`, bitacora de ronda |
| Medicion | Ejecucion de corridas por analito y nivel | Responsable tecnico + Participante | `F-PSEA-08` |
| Post-ronda | Desmontaje, cierre y bloqueo de datos | Coordinacion EA | `F-PSEA-09`, evidencias de cierre |

---

## 9. Criterios operativos del item PT

| Criterio | Definicion |
|---|---|
| Origen del item PT | |
| Punto de entrega | |
| Control de custodia | |
| Condiciones ambientales | |
| Restricciones de conexion o uso de equipos del participante | |
| Respuesta ante desviaciones | |

---

## 10. Control estadistico pre-ronda

| Elemento | Definicion |
|---|---|
| Valor asignado previsto | |
| Incertidumbre del valor asignado | |
| Desviacion estandar para evaluacion de aptitud | |
| Criterio de desempeno | |
| Tratamiento de valores atipicos | |
| Regla de redondeo y unidades | |

---

## 11. Matriz A-U ISO/IEC 17043:2023 7.2.1.3

| Literal | Requisito de diseno | Definicion / referencia en la ronda |
|---|---|---|
| A | Objetivo de la ronda | |
| B | Items de ensayo de aptitud | |
| C | Participantes previstos | |
| D | Metodos o procedimientos aplicables | |
| E | Preparacion, manipulacion y distribucion | |
| F | Homogeneidad y estabilidad | |
| G | Informacion requerida a participantes | |
| H | Forma de reporte de resultados | |
| I | Evaluacion estadistica | |
| J | Valor asignado y su incertidumbre | |
| K | Criterios de desempeno | |
| L | Confidencialidad y colusion | |
| M | Cronograma | |
| N | Comunicaciones | |
| O | Subcontratacion o proveedores | |
| P | Instrucciones a participantes | |
| Q | Seguridad y ambiente | |
| R | Registros y trazabilidad | |
| S | Tratamiento de quejas/apelaciones | |
| T | Informe | |
| U | Revision y aprobacion del diseno | |

---

## 12. Aprobacion y control de cambios

| Version | Fecha | Cambio | Elaboro | Aprobo |
|---|---|---|---|---|
| 0 | | Emision inicial de la planificacion de ronda | | |

---

## 13. Criterio de completitud

La planificacion se considera completa cuando `F-PSEA-03` esta cerrado para los participantes confirmados, `F-PSEA-04` esta exportado y revisado, los recursos criticos estan definidos, el cronograma esta aprobado, la matriz A-U esta diligenciada y las aprobaciones previas a ejecucion estan registradas.
