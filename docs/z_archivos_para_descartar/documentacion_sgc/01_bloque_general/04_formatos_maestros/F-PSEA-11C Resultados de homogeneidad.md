# F-PSEA-11C: Resultados de homogeneidad

**Codigo:** F-PSEA-11C  
**Tipo documental:** Formato / registro  
**Nombre:** Resultados de homogeneidad  
**Version:** 1.0  
**Fecha:** 2026-06-18  
**Estado:** Activo

---

## 1. Objetivo

Registrar los resultados de la evaluacion de homogeneidad del item de ensayo, exportados desde el modulo de analisis de pt_app, como evidencia de que el item cumple con los criterios definidos en P-PSEA-07.

## 2. Alcance

Este formato aplica a los resultados de homogeneidad generados por el modulo de analisis de pt_app para cada ronda de ensayo de aptitud en gases contaminantes criterio.

Incluye:

- Resultados del analisis de homogeneidad.
- Identificacion del item de ensayo y la ronda.
- Criterio estadistico aplicado.
- Trazabilidad a los datos preprocesados (F-PSEA-11A).

No incluye:

- Datos preprocesados (F-PSEA-11A).
- Datos crudos sin procesar (archivos tecnicos internos).
- Registro de preprocesamiento (F-PSEA-10).

## 3. Responsabilidades y uso

| Rol | Responsabilidad |
|---|---|
| Analista PT | Ejecutar el analisis de homogeneidad y generar este formato. |
| Revisor tecnico | Verificar que los resultados sean consistentes con los datos preprocesados y el criterio estadistico. |
| Responsable del informe | Integrar este formato en el informe final de resultados (F-PSEA-13). |

Este formato se genera siguiendo I-PSEA-05 y se utiliza como entrada para el informe final de resultados.

## 4. Entradas

| Codigo / fuente | Descripcion |
|---|---|
| F-PSEA-11A | Datos preprocesados de homogeneidad. |
| P-PSEA-07 | Criterio estadistico de H/E. |
| I-PSEA-05 | Instructivo de uso del modulo de analisis. |

## 5. Salidas

| Codigo | Descripcion |
|---|---|
| F-PSEA-13 | Informe final de resultados. |
| F-PSEA-11 | Registro principal de H/E (referencia). |

## 6. Campos minimos

| Campo | Descripcion |
|---|---|
| ID_ronda | Codigo o identificador de la ronda. |
| ID_item | Identificador del item de ensayo. |
| Analito | Gas contaminante criterio evaluado. |
| Nivel | Nivel de concentracion del item. |
| Estadistico_H | Estadistico de homogeneidad calculado. |
| Criterio_aceptacion | Valor limite o criterio definido en P-PSEA-07. |
| Decision | Acepta / No acepta / Requiere revision. |
| Criterio_aplicado | Referencia al criterio de P-PSEA-07 utilizado. |
| ID_datos_preprocesados | Referencia a F-PSEA-11A. |
| Responsable | Persona que ejecuto el analisis. |
| Fecha_analisis | Fecha y hora del analisis. |
| Observaciones | Notas sobre supuestos, exclusiones o advertencias. |

## 7. Controles

- Los resultados deben provenir de los datos preprocesados (F-PSEA-11A).
- Debe indicarse claramente el criterio estadistico aplicado (P-PSEA-07).
- La decision de aceptabilidad debe estar fundamentada en el criterio definido.
- Cada resultado debe ser trazable al item de ensayo y a la ronda.
- La version del formato debe coincidir con la version del modulo de analisis utilizado.

## 8. Relaciones documentales

| Codigo | Relacion |
|---|---|
| F-PSEA-11 | Registro principal de homogeneidad y estabilidad. |
| F-PSEA-11A | Datos preprocesados que alimentan este resultado. |
| F-PSEA-13 | Informe final de resultados. |
| P-PSEA-06 | Preparacion y control del item de ensayo. |
| P-PSEA-07 | Criterio estadistico aplicado. |
| P-PSEA-08 | Flujo tecnico de datos digitales. |
| I-PSEA-05 | Instructivo de uso del modulo de analisis. |

## 9. Limites

- No contiene datos preprocesados (eso es F-PSEA-11A).
- No es un registro de preprocesamiento (eso es F-PSEA-10).
- No define criterios estadisticos (eso es P-PSEA-07).
- No es un instructivo de uso.
- No incluye datos crudos sin procesar.
