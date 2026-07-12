# P-PSEA-06 Preparacion y control del item de ensayo gaseoso

## Objetivo

Definir el procedimiento para preparar y controlar el item de ensayo gaseoso del PEA, asegurando que las concentraciones generadas con calibrador dinamico y cilindro de gas sean trazables, estables y adecuadas para la evaluacion de aptitud.

## Alcance

Aplica a la generacion in situ de concentraciones de gases contaminantes criterio durante las rondas del PEA. Incluye preparacion, verificacion operativa, control del item, registro de condiciones y enlace con la evaluacion de homogeneidad y estabilidad.

No aplica al envio o recepcion fisica de items de ensayo, porque el esquema genera el item gaseoso en sitio.

## Entradas

| Entrada | Uso |
|---|---|
| `DG-PSEA-02` / `calaire-app` | Fuente de niveles y parametros definidos para la ronda. |
| `P-PSEA-04` | Planificacion de ronda y condiciones operativas. |
| Calibrador dinamico | Generacion de concentraciones objetivo. |
| Cilindro de gas patron | Fuente de gas para preparacion del item. |
| Procedimientos por analito `P-PSEA-10` a `P-PSEA-13` | Particularidades tecnicas del gas. |

## Actividades

1. Confirmar la ronda, analito, niveles nominales y condiciones de operacion definidos en la planificacion.
2. Verificar disponibilidad, identificacion y estado metrologico del calibrador dinamico, cilindro, lineas y elementos auxiliares.
3. Configurar el sistema de generacion de acuerdo con el analito y el nivel requerido.
4. Ejecutar estabilizacion inicial antes de registrar lecturas o exponer equipos participantes.
5. Registrar condiciones de preparacion, controles aplicados, desviaciones y observaciones operativas.
6. Generar o consolidar los datos necesarios para homogeneidad y estabilidad cuando aplique.
7. Entregar los registros al flujo digital y estadistico definido en `P-PSEA-08` y `P-PSEA-07`.

## Salidas y registros

| Salida | Descripcion |
|---|---|
| `F-PSEA-07` | Dossier o registro de preparacion y control del item. |
| `F-PSEA-11` | Registro principal de homogeneidad y estabilidad del item. |
| `F-PSEA-11A` | Datos preprocesados de homogeneidad. |
| `F-PSEA-11B` | Datos preprocesados de estabilidad. |

## Controles

- Confirmar que los niveles usados corresponden a la ronda vigente.
- Registrar identificacion de equipos, cilindros, fechas, responsables y condiciones ambientales relevantes.
- Separar controles del item de los criterios estadisticos generales, que se gobiernan por `P-PSEA-07`.
- Mantener trazabilidad entre preparacion del item, datos H/E y dataset oficial de la ronda.

## Documentos relacionados

| Codigo | Relacion |
|---|---|
| `P-PSEA-04` | Planificacion de ronda. |
| `P-PSEA-07` | Diseno estadistico y criterios H/E. |
| `P-PSEA-08` | Flujo tecnico de datos digitales. |
| `P-PSEA-10` a `P-PSEA-13` | Procedimientos tecnicos por analito. |
| `DG-PSEA-02` | Definicion digital de niveles y ronda. |
| `DG-PSEA-03` | Analisis H/E y procesamiento posterior. |

## Limites

- No reemplaza los procedimientos tecnicos por analito.
- No define `sigma_pt`, valor asignado, outliers ni reglas de desempeno.
- No documenta envio fisico de items de ensayo.
- No sustituye instructivos de uso de aplicativos o equipos.
