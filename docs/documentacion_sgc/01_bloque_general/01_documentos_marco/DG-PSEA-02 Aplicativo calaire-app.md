# DG-PSEA-02: Aplicativo calaire-app

**Codigo:** DG-PSEA-02  
**Tipo documental:** Documento general  
**Nombre:** Aplicativo calaire-app  
**Version:** 1.0  
**Fecha:** 2026-06-18  
**Estado:** Activo

---

## 1. Objetivo

Documentar el alcance, funciones, entradas, salidas y limites del aplicativo calaire-app, sistema operativo del PEA para la gestion de rondas de ensayo de aptitud, participantes, cronogramas, captura de datos, exportaciones y gestion de casos SGC de quejas.

## 2. Alcance

Este documento aplica al aplicativo calaire-app durante las fases de planificacion, ejecucion de ronda y recoleccion de datos del ensayo de aptitud para gases contaminantes criterio.

Incluye:

- Gestion de rondas de ensayo de aptitud.
- Registro y administracion de participantes.
- Configuracion de calendarios y cronogramas de ronda.
- Captura de datos reportados por los participantes.
- Registro de informacion tecnica de equipos e instrumentos.
- Exportacion de datos hacia pt_app.
- Registro operativo de casos SGC de quejas, cuando aplique.

No incluye:

- Criterios estadisticos ni evaluacion de aptitud (P-PSEA-07).
- Preprocesamiento, analisis estadistico ni emision del informe final (DG-PSEA-03 / pt_app).
- Procedimientos de comunicacion, planificacion o control documental del PEA.

## 3. Responsabilidades y uso

| Rol | Responsabilidad |
|---|---|
| Coordinador de ronda | Configurar ronda, calendario, cronograma y participantes en calaire-app. |
| Administrador del aplicativo | Gestionar usuarios, permisos, estructura de ronda y casos SGC de quejas. |
| Participante | Confirmar participacion, consultar informacion de ronda y registrar datos y equipos. |
| Analista PT | Recibir exportaciones oficiales (F-PSEA-09) para continuar el flujo en pt_app. |

El aplicativo se utiliza como herramienta operativa bajo lo definido en P-PSEA-04 (planificacion de ronda), P-PSEA-05 (comunicaciones) y P-PSEA-17 (quejas).

## 4. Entradas

| Codigo / fuente | Descripcion |
|---|---|
| Requisitos operativos PEA | Funciones requeridas para gestion de rondas. |
| P-PSEA-04 | Procedimiento de planificacion de ronda. |
| P-PSEA-05 | Procedimiento de comunicaciones del PEA. |
| Participantes | Datos reportados por laboratorios participantes. |

## 5. Salidas

| Codigo | Descripcion |
|---|---|
| F-PSEA-01 | Calendario global de ronda. |
| F-PSEA-02 | Cronograma detallado de ronda. |
| F-PSEA-03 | Registro de participacion. |
| F-PSEA-04 | Anexo tecnico de equipos e instrumentos del participante. |
| F-PSEA-06 | Ficha digital de ronda EA. |
| F-PSEA-08 | Datos reportados por participante. |
| F-PSEA-09 | Datos de participantes exportados para analisis PT. |
| F-PSEA-14 | Caso SGC de queja o NC, si aplica. |

## 6. Campos minimos

Cada ronda configurada en calaire-app debe registrar como minimo:

- Codigo y nombre de la ronda.
- Periodo de ejecucion (fecha inicio / fecha fin).
- Analito(s) asociados.
- Niveles de concentracion definidos.
- Laboratorios participantes y estado de confirmacion.
- Responsable de la ronda.
- Version o identificador de la ficha digital de ronda (F-PSEA-06).

Cada participante debe registrar como minimo:

- Identificacion del laboratorio.
- Contacto operativo.
- Equipos e instrumentos asociados (F-PSEA-04).
- Datos reportados por analito y nivel (F-PSEA-08).

## 7. Controles

- Las exportaciones hacia pt_app deben ser versionadas y conservarse como F-PSEA-09.
- Los cambios en calendario, cronograma o ficha digital de ronda deben quedar trazables en el historial del aplicativo o en el formato correspondiente.
- El acceso al aplicativo debe estar acotado por rol (administrador / participante / analista).
- Los casos SGC de queja registrados en calaire-app deben alinearse con P-PSEA-17 y P-PSEA-16 cuando deriven en NC/CAPA.

## 8. Relaciones documentales

| Codigo | Relacion |
|---|---|
| I-PSEA-02 | Instructivo de uso de calaire-app por participante. |
| I-PSEA-03 | Instructivo de administracion de rondas en calaire-app. |
| P-PSEA-04 | Procedimiento de planificacion de ronda que usa el aplicativo. |
| P-PSEA-05 | Procedimiento de comunicaciones que usa el aplicativo. |
| P-PSEA-08 | Flujo tecnico de datos digitales del PEA. |
| P-PSEA-17 | Procedimiento de quejas del PEA gestionadas como casos SGC. |
| DG-PSEA-03 | Aplicativo pt_app que recibe las exportaciones oficiales. |

## 9. Limites

- No es un formato F-PSEA; es un documento general del aplicativo.
- No es un instructivo de uso; la operacion se documenta en I-PSEA-02 e I-PSEA-03.
- No define criterios estadisticos, valor asignado, sigma_pt ni reglas de desempeno.
- No genera el informe final de resultados ni el analisis estadistico.
- No reemplaza procedimientos de planificacion, comunicaciones ni control documental.

---

**Nota:** La documentacion tecnica interna de calaire-app (calaire-app_func_docs_sgc.md, calaire-app_reg_docs_sgc.md, calaire-app_registros-sgc.html) se mantiene en carpeta aparte como soporte del aplicativo y no forma parte de este documento general codificado.
