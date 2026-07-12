# I-PSEA-04: Instructivo de uso del preprocesador de pt_app

**Codigo:** I-PSEA-04  
**Tipo documental:** Instructivo  
**Nombre:** Instructivo de uso del preprocesador de pt_app  
**Version:** 1.0  
**Fecha:** 2026-06-18  
**Estado:** Activo

---

## 1. Objetivo

Explicar el uso operativo del modulo preprocesador de pt_app, incluyendo carga de archivos de entrada, parametros de configuracion, secuencia de pasos, archivos tecnicos generados y registro de la ejecucion en F-PSEA-10.

## 2. Alcance

Este instructivo aplica al analista PT responsable de ejecutar el preprocesamiento de datos antes del analisis estadistico.

Incluye:

- Carga de archivos de entrada oficiales desde calaire-app.
- Carga de archivos tecnicos internos de homogeneidad y estabilidad.
- Configuracion de parametros de preprocesamiento.
- Ejecucion de la secuencia de pasos del preprocesador.
- Generacion de datos preprocesados de homogeneidad y estabilidad.
- Consolidacion del dataset oficial para analisis PT.
- Registro de la ejecucion en F-PSEA-10.

No incluye:

- Definicion de criterios estadisticos (P-PSEA-07).
- Flujo tecnico de datos macro del PEA (P-PSEA-08).
- Analisis estadistico propiamente dicho (I-PSEA-05).
- Generacion del informe final de resultados (P-PSEA-09).

## 3. Responsabilidades y uso

| Rol | Responsabilidad |
|---|---|
| Analista PT | Ejecutar el preprocesador siguiendo este instructivo y registrar la ejecucion en F-PSEA-10. |
| Revisor tecnico | Verificar que las entradas sean las versiones oficiales y que las salidas correspondan a lo esperado. |
| Responsable de ronda | Asegurar que F-PSEA-09 y F-PSEA-04 esten disponibles y aprobados. |

El preprocesador se ejecuta bajo lo definido en DG-PSEA-03, P-PSEA-08 y P-PSEA-07.

## 4. Entradas

| Codigo / fuente | Descripcion |
|---|---|
| F-PSEA-09 | Datos de participantes exportados desde calaire-app. |
| F-PSEA-04 | Anexo tecnico de equipos e instrumentos del participante. |
| Archivos tecnicos internos | Datos de ronda, niveles, homogeneidad y estabilidad crudos. |

## 5. Salidas

| Codigo | Descripcion |
|---|---|
| F-PSEA-10 | Registro de preprocesamiento de datos. |
| F-PSEA-11A | Datos preprocesados de homogeneidad. |
| F-PSEA-11B | Datos preprocesados de estabilidad. |
| F-PSEA-12 | Datos oficiales consolidados para evaluacion de aptitud. |

## 6. Procedimiento resumido

1. Verificar que las entradas F-PSEA-09 y F-PSEA-04 sean la version oficial de la ronda.
2. Cargar los archivos tecnicos internos de homogeneidad y estabilidad.
3. Configurar los parametros de preprocesamiento segun la ronda y el analito.
4. Ejecutar la secuencia de pasos del preprocesador en el orden establecido.
5. Revisar las salidas intermedias (F-PSEA-11A, F-PSEA-11B) y el dataset consolidado (F-PSEA-12).
6. Registrar la ejecucion en F-PSEA-10.
7. Entregar las salidas al modulo de analisis de pt_app.

## 7. Campos minimos

El registro de preprocesamiento (F-PSEA-10) debe incluir como minimo:

- Identificador de ronda.
- Fecha y hora de ejecucion.
- Version del aplicativo o script utilizado.
- Lista de archivos de entrada.
- Lista de archivos de salida generados.
- Parametros de configuracion aplicados.
- Responsable de la ejecucion.
- Observaciones o advertencias.

## 8. Controles

- Solo se deben usar como entradas las exportaciones oficiales desde calaire-app.
- Toda ejecucion debe quedar registrada en F-PSEA-10 antes de continuar con el analisis.
- Los archivos tecnicos internos deben conservarse con trazabilidad al item de ensayo y a la ronda.
- Las salidas F-PSEA-11A, F-PSEA-11B y F-PSEA-12 deben diferenciarse claramente.
- Cualquier anomalia en los datos debe reportarse en el campo de observaciones de F-PSEA-10.

## 9. Relaciones documentales

| Codigo | Relacion |
|---|---|
| DG-PSEA-03 | Documento general del aplicativo pt_app. |
| P-PSEA-07 | Criterio estadistico de referencia. |
| P-PSEA-08 | Flujo tecnico que contextualiza el paso. |
| F-PSEA-10 | Registro que documenta la ejecucion. |
| I-PSEA-05 | Instructivo de uso del modulo de analisis PT. |

## 10. Limites

- No reemplaza P-PSEA-07; solo explica como operar la herramienta.
- No reemplaza P-PSEA-08; complementa la parte operativa del preprocesador.
- No define que es un outlier, como se calcula el valor asignado ni que es sigma_pt.
- No es un procedimiento de control de calidad.
- No describe el analisis estadistico; eso se cubre en I-PSEA-05.
