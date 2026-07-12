# P-PSEA-07 Diseno estadistico

## Objetivo

Establecer los criterios metrologicos y estadisticos para evaluar el desempeno de participantes en el PEA, incluyendo valor asignado, `sigma_pt`, incertidumbre, tratamiento de datos, homogeneidad, estabilidad y reglas de decision.

## Alcance

Aplica al analisis estadistico de rondas de ensayo de aptitud para gases contaminantes criterio. El procedimiento define el criterio tecnico; la ejecucion operativa en software se documenta en `DG-PSEA-03`, `I-PSEA-04` e `I-PSEA-05`.

## Entradas

| Entrada | Uso |
|---|---|
| `F-PSEA-12` | Dataset oficial consolidado para evaluacion de aptitud. |
| `F-PSEA-11A` y `F-PSEA-11B` | Datos preprocesados de homogeneidad y estabilidad. |
| `P-PSEA-10` a `P-PSEA-13` | Particularidades por analito. |
| ISO/IEC 17043 e ISO 13528 | Referencias normativas y estadisticas. |

## Actividades

1. Definir o confirmar el valor asignado aplicable a cada analito y nivel.
2. Definir o confirmar `sigma_pt` y su justificacion tecnica.
3. Evaluar incertidumbre y su efecto en la interpretacion del desempeno.
4. Revisar datos atipicos, consistencia interna y criterios de inclusion/exclusion.
5. Evaluar homogeneidad y estabilidad como insumo para la validez de la ronda.
6. Calcular estadisticos y puntuaciones de desempeno segun el criterio aprobado.
7. Documentar resultados, advertencias y restricciones para el informe final.

## Salidas y registros

| Salida | Descripcion |
|---|---|
| `F-PSEA-11C` | Resultados de homogeneidad. |
| `F-PSEA-11D` | Resultados de estabilidad. |
| `F-PSEA-13` | Informe final que incorpora los criterios estadisticos. |
| Registros de `pt_app` | Evidencia de procesamiento y resultados calculados. |

## Controles

- Mantener trazabilidad entre dataset, criterios aplicados, version de calculo y resultados emitidos.
- No modificar criterios durante una ronda sin autorizacion tecnica documentada.
- Separar el criterio estadistico del instructivo de uso del aplicativo.
- Evidenciar el tratamiento de H/E antes de interpretar resultados de desempeno.

## Documentos relacionados

| Codigo | Relacion |
|---|---|
| `DG-PSEA-03` | Aplicativo que implementa los calculos. |
| `I-PSEA-05` | Uso del modulo de analisis en `pt_app`. |
| `P-PSEA-08` | Flujo tecnico de datos digitales. |
| `P-PSEA-09` | Generacion y emision del informe de resultados. |
| `P-PSEA-10` a `P-PSEA-13` | Procedimientos por analito que citan este criterio. |

## Limites

- No es manual de usuario de `pt_app`.
- No define el contenido editorial completo del informe final.
- No sustituye el procedimiento de preparacion del item.
- No debe duplicarse dentro de los procedimientos por analito.
