# I-PSEA-05: Instructivo de uso del modulo de analisis PT de pt_app

**Codigo:** I-PSEA-05  
**Tipo documental:** Instructivo  
**Nombre:** Instructivo de uso del modulo de analisis PT de pt_app  
**Version:** 1.0  
**Fecha:** 2026-06-18  
**Estado:** Activo

---

## 1. Objetivo

Explicar el uso operativo del modulo de analisis de ensayos de aptitud en pt_app, incluyendo carga del dataset consolidado, seleccion de criterios estadisticos, ejecucion de calculos, revision de resultados de homogeneidad y estabilidad, generacion de graficos y exportacion del informe.

## 2. Alcance

Este instructivo aplica al analista PT responsable de ejecutar el analisis estadistico del ensayo de aptitud.

Incluye:

- Carga del dataset oficial consolidado (F-PSEA-12).
- Carga de datos preprocesados de homogeneidad y estabilidad (F-PSEA-11A, F-PSEA-11B).
- Seleccion de criterios estadisticos de acuerdo con P-PSEA-07.
- Ejecucion de calculos de valor asignado, sigma_pt, incertidumbre y desempeno.
- Revision de resultados de homogeneidad (F-PSEA-11C) y estabilidad (F-PSEA-11D).
- Generacion de graficos y tablas de resultados.
- Exportacion del informe final de resultados (F-PSEA-13).

No incluye:

- Definicion de criterios estadisticos (P-PSEA-07).
- Preprocesamiento de datos (I-PSEA-04).
- Procedimiento formal de generacion y emision del informe (P-PSEA-09).
- Gestion de quejas o apelaciones.

## 3. Responsabilidades y uso

| Rol | Responsabilidad |
|---|---|
| Analista PT | Ejecutar el analisis estadistico siguiendo este instructivo y P-PSEA-07. |
| Revisor tecnico | Verificar que los criterios aplicados sean los correctos y que los resultados sean consistentes. |
| Responsable del informe | Asegurar que F-PSEA-13 corresponda al analisis ejecutado y sea la version aprobada. |

El modulo de analisis se ejecuta bajo lo definido en DG-PSEA-03, P-PSEA-07 y P-PSEA-09.

## 4. Entradas

| Codigo / fuente | Descripcion |
|---|---|
| F-PSEA-12 | Datos oficiales consolidados para evaluacion de aptitud. |
| F-PSEA-11A | Datos preprocesados de homogeneidad. |
| F-PSEA-11B | Datos preprocesados de estabilidad. |
| P-PSEA-07 | Criterio estadistico de referencia. |

## 5. Salidas

| Codigo | Descripcion |
|---|---|
| F-PSEA-13 | Informe final de resultados. |
| F-PSEA-11C | Resultados de homogeneidad. |
| F-PSEA-11D | Resultados de estabilidad. |

## 6. Procedimiento resumido

1. Verificar que el dataset consolidado (F-PSEA-12) sea la version oficial aprobada.
2. Cargar los datos preprocesados de homogeneidad (F-PSEA-11A) y estabilidad (F-PSEA-11B).
3. Seleccionar el criterio estadistico definido en P-PSEA-07.
4. Ejecutar los calculos de valor asignado, sigma_pt, incertidumbre y desempeno.
5. Revisar los resultados de homogeneidad (F-PSEA-11C) y estabilidad (F-PSEA-11D).
6. Generar graficos y tablas de resultados.
7. Exportar el informe final de resultados (F-PSEA-13).
8. Conservar trazabilidad entre el analisis, los criterios aplicados y el informe generado.

## 7. Campos minimos

El analisis debe registrar como minimo:

- Identificador de ronda.
- Dataset consolidado utilizado (F-PSEA-12).
- Criterio estadistico aplicado (referencia a P-PSEA-07).
- Metodo de calculo del valor asignado y sigma_pt.
- Resultados de homogeneidad y estabilidad (F-PSEA-11C / F-PSEA-11D).
- Informe final generado (F-PSEA-13).
- Responsable del analisis y fecha de ejecucion.

## 8. Controles

- El dataset consolidado (F-PSEA-12) debe ser la unica entrada del modulo de analisis.
- Los criterios estadisticos aplicados deben corresponder a P-PSEA-07.
- Los resultados de H/E deben ser revisados antes de emitir el informe final.
- La version del informe (F-PSEA-13) debe estar trazable al analisis ejecutado.
- Cualquier ajuste o exclusion de datos debe quedar documentado y justificado.

## 9. Relaciones documentales

| Codigo | Relacion |
|---|---|
| DG-PSEA-03 | Documento general del aplicativo pt_app. |
| P-PSEA-07 | Criterio estadistico que gobierna el analisis. |
| P-PSEA-08 | Flujo tecnico que contextualiza el paso. |
| P-PSEA-09 | Procedimiento de generacion del informe de resultados. |
| F-PSEA-12 | Dataset que alimenta el analisis. |
| I-PSEA-04 | Instructivo de uso del preprocesador. |

## 10. Limites

- No reemplaza P-PSEA-07; solo explica como operar la herramienta.
- No reemplaza P-PSEA-09; complementa la parte operativa de generacion del informe.
- No define que es un outlier, como se calcula el valor asignado ni que es sigma_pt.
- No es un procedimiento de control de calidad.
- No describe el preprocesamiento; eso se cubre en I-PSEA-04.
