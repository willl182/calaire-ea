# DG-PSEA-03: Aplicativo pt_app

**Codigo:** DG-PSEA-03  
**Tipo documental:** Documento general  
**Nombre:** Aplicativo pt_app  
**Version:** 1.0  
**Fecha:** 2026-06-18  
**Estado:** Activo

---

## 1. Objetivo

Documentar el alcance, funciones, entradas, salidas y limites del aplicativo pt_app, sistema operativo del PEA para preprocesamiento, consolidacion de datos, analisis estadistico, evaluacion de homogeneidad y estabilidad, y generacion del informe final de resultados.

## 2. Alcance

Este documento aplica al aplicativo pt_app durante las fases de analisis y emision de resultados del ensayo de aptitud para gases contaminantes criterio.

Incluye:

- Carga de datos oficiales exportados desde calaire-app.
- Preprocesamiento de datos de participantes, equipos e instrumentos.
- Preprocesamiento de datos de homogeneidad y estabilidad.
- Consolidacion del dataset oficial para analisis PT.
- Analisis estadistico de ensayo de aptitud.
- Evaluacion de homogeneidad y estabilidad del item de ensayo.
- Generacion del informe final de resultados.

No incluye:

- Captura directa de datos de participantes (DG-PSEA-02 / calaire-app).
- Definicion de criterios estadisticos ni reglas de decision (P-PSEA-07).
- Gestion del procedimiento de generacion y emision del informe (P-PSEA-09).
- Gestion de quejas, apelaciones o casos SGC (P-PSEA-17, P-PSEA-18, P-PSEA-16).

## 3. Responsabilidades y uso

| Rol | Responsabilidad |
|---|---|
| Analista PT | Ejecutar preprocesamiento, analisis estadistico y generacion de salidas en pt_app. |
| Revisor tecnico | Verificar que los criterios aplicados en el analisis correspondan a P-PSEA-07. |
| Responsable de ronda | Asegurar que las entradas desde calaire-app sean la version oficial aprobada. |
| Administrador del aplicativo | Gestionar versiones, permisos y trazabilidad de ejecuciones. |

El aplicativo se utiliza como herramienta analitica bajo lo definido en P-PSEA-07 (criterio estadistico), P-PSEA-08 (flujo tecnico de datos) y P-PSEA-09 (generacion del informe).

## 4. Entradas

| Codigo / fuente | Descripcion |
|---|---|
| F-PSEA-09 | Datos de participantes exportados desde calaire-app. |
| F-PSEA-04 | Anexo tecnico de equipos e instrumentos del participante. |
| Archivos tecnicos internos | Datos de ronda, niveles, homogeneidad y estabilidad crudos. |
| P-PSEA-07 | Criterio estadistico de referencia. |

## 5. Salidas

| Codigo | Descripcion |
|---|---|
| F-PSEA-10 | Registro de preprocesamiento de datos. |
| F-PSEA-11A | Datos preprocesados de homogeneidad. |
| F-PSEA-11B | Datos preprocesados de estabilidad. |
| F-PSEA-11C | Resultados de homogeneidad. |
| F-PSEA-11D | Resultados de estabilidad. |
| F-PSEA-12 | Datos oficiales consolidados para evaluacion de aptitud. |
| F-PSEA-13 | Informe final de resultados. |

## 6. Campos minimos

Cada ejecucion del preprocesador debe registrar como minimo:

- Identificador de ronda.
- Fecha y hora de ejecucion.
- Version del aplicativo o script utilizado.
- Archivos de entrada (ruta o identificador).
- Archivos de salida generados.
- Responsable de la ejecucion.
- Observaciones o advertencias detectadas.

Cada ejecucion del modulo de analisis debe registrar como minimo:

- Identificador de ronda.
- Dataset consolidado utilizado (F-PSEA-12).
- Criterio estadistico aplicado (referencia a P-PSEA-07).
- Resultados de homogeneidad y estabilidad (F-PSEA-11C / F-PSEA-11D).
- Informe final generado (F-PSEA-13).
- Responsable del analisis.

## 7. Controles

- Toda ejecucion del preprocesador debe quedar registrada en F-PSEA-10.
- El dataset oficial consolidado (F-PSEA-12) debe ser la unica entrada del modulo de analisis.
- Los criterios estadisticos aplicados deben corresponder a lo definido en P-PSEA-07.
- Las salidas tecnicas intermedias (F-PSEA-11A / F-PSEA-11B) deben diferenciarse de los resultados finales de H/E (F-PSEA-11C / F-PSEA-11D).
- La generacion del informe final debe estar trazable al analisis y al criterio estadistico aplicado.

## 8. Relaciones documentales

| Codigo | Relacion |
|---|---|
| I-PSEA-04 | Instructivo de uso del preprocesador de pt_app. |
| I-PSEA-05 | Instructivo de uso del modulo de analisis PT de pt_app. |
| P-PSEA-07 | Criterio estadistico que gobierna el analisis. |
| P-PSEA-08 | Flujo tecnico de datos digitales del PEA. |
| P-PSEA-09 | Procedimiento de generacion del informe de resultados. |
| DG-PSEA-02 | Aplicativo calaire-app que alimenta datos de entrada. |
| F-PSEA-13 | Informe final de resultados generado por pt_app. |

## 9. Limites

- No es un formato F-PSEA; es un documento general del aplicativo.
- No es un instructivo de uso; la operacion se documenta en I-PSEA-04 e I-PSEA-05.
- No define criterios estadisticos; cita P-PSEA-07 para eso.
- No captura datos de participantes; recibe las exportaciones oficiales desde calaire-app.
- No gestiona quejas, apelaciones ni acciones correctivas.

---

**Nota:** Los archivos tecnicos internos del preprocesador y del modulo de analisis se mapean en P-PSEA-08 y no se codifican como formatos F-PSEA adicionales.
