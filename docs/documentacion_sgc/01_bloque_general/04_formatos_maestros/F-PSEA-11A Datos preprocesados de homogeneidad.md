# F-PSEA-11A: Datos preprocesados de homogeneidad

**Codigo:** F-PSEA-11A  
**Tipo documental:** Formato / registro  
**Nombre:** Datos preprocesados de homogeneidad  
**Version:** 1.0  
**Fecha:** 2026-06-18  
**Estado:** Activo

---

## 1. Objetivo

Registrar los datos de homogeneidad del item de ensayo despues del preprocesamiento en pt_app, como insumo tecnico para el modulo de analisis.

## 2. Alcance

Este formato aplica a los datos de homogeneidad generados por el preprocesador de pt_app para cada ronda de ensayo de aptitud en gases contaminantes criterio.

Incluye:

- Datos crudos de homogeneidad depurados y estructurados.
- Identificacion del item de ensayo y la ronda.
- Trazabilidad al registro de preprocesamiento (F-PSEA-10).

No incluye:

- Resultados finales de homogeneidad (F-PSEA-11C).
- Datos crudos sin procesar (archivos tecnicos internos).
- Criterios estadisticos aplicados (P-PSEA-07).

## 3. Responsabilidades y uso

| Rol | Responsabilidad |
|---|---|
| Analista PT | Ejecutar el preprocesador y generar este formato. |
| Revisor tecnico | Verificar que los datos preprocesados sean consistentes con los archivos tecnicos internos. |
| Responsable de ronda | Asegurar que el formato quede vinculado al item de ensayo y a la ronda correspondiente. |

Este formato se genera siguiendo I-PSEA-04 y se utiliza como entrada para el modulo de analisis de pt_app.

## 4. Entradas

| Codigo / fuente | Descripcion |
|---|---|
| Archivos tecnicos internos | Datos crudos de homogeneidad. |
| F-PSEA-10 | Registro de preprocesamiento. |
| I-PSEA-04 | Instructivo de uso del preprocesador. |

## 5. Salidas

| Codigo | Descripcion |
|---|---|
| F-PSEA-11C | Resultados de homogeneidad. |
| F-PSEA-12 | Dataset oficial consolidado (referencia). |

## 6. Campos minimos

| Campo | Descripcion |
|---|---|
| ID_ronda | Codigo o identificador de la ronda. |
| ID_item | Identificador del item de ensayo. |
| Analito | Gas contaminante criterio evaluado. |
| Nivel | Nivel de concentracion del item. |
| Replica | Numero de replica o unidad de muestreo. |
| Valor_medido | Valor medido de homogeneidad. |
| Unidad | Unidad del valor medido. |
| Fecha_medicion | Fecha y hora de la medicion. |
| ID_preprocesamiento | Referencia al registro F-PSEA-10. |
| Responsable | Persona que ejecuto el preprocesamiento. |
| Observaciones | Notas sobre depuracion, exclusiones o advertencias. |

## 7. Controles

- Los datos deben provenir de los archivos tecnicos internos de homogeneidad.
- Cada registro debe estar vinculado a un F-PSEA-10.
- No debe incluir resultados de analisis ni conclusiones de aceptabilidad.
- Los valores deben estar en las unidades definidas para la ronda.
- La version del formato debe coincidir con la version del preprocesador utilizado.

## 8. Relaciones documentales

| Codigo | Relacion |
|---|---|
| F-PSEA-11 | Registro principal de homogeneidad y estabilidad. |
| F-PSEA-11C | Resultados de homogeneidad que se alimentan de estos datos. |
| F-PSEA-10 | Registro de preprocesamiento. |
| P-PSEA-06 | Preparacion y control del item de ensayo. |
| P-PSEA-07 | Criterio estadistico de H/E. |
| P-PSEA-08 | Flujo tecnico de datos digitales. |
| I-PSEA-04 | Instructivo de uso del preprocesador. |

## 9. Limites

- No contiene resultados finales de homogeneidad (eso es F-PSEA-11C).
- No es un registro de preprocesamiento (eso es F-PSEA-10).
- No define criterios estadisticos (eso es P-PSEA-07).
- No es un instructivo de uso.
- No incluye datos crudos sin procesar.
