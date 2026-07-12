# P-PSEA-08 Flujo tecnico de datos digitales del PEA

## Objetivo

Definir el flujo tecnico de datos digitales del PEA desde la captura en `calaire-app` hasta el preprocesamiento, analisis estadistico, generacion de subformatos H/E, consolidacion del dataset oficial y produccion del informe final.

## Alcance

Aplica a datos, archivos CSV simples, exportaciones oficiales, registros de procesamiento y salidas digitales generadas durante una ronda o evento del PEA. No convierte archivos tecnicos internos en formatos oficiales salvo decision documental explicita.

## Entradas

| Entrada | Uso |
|---|---|
| `DG-PSEA-02` / `calaire-app` | Captura de participantes, ronda, cronogramas y datos reportados. |
| `F-PSEA-09` | Exportacion oficial de datos de participantes. |
| `F-PSEA-04` | Anexo tecnico de equipos e instrumentos cuando aplique. |
| CSV operativos | Archivos simples usados como soporte tecnico del flujo. |

## Actividades

1. Identificar el origen de cada dato digital y su aplicativo responsable.
2. Exportar desde `calaire-app` los datos oficiales requeridos para analisis.
3. Registrar ingreso, validacion y preprocesamiento en `pt_app`.
4. Generar subformatos de homogeneidad y estabilidad cuando aplique.
5. Consolidar el dataset oficial para evaluacion de aptitud.
6. Entregar resultados al modulo de analisis y al flujo de informe final.
7. Clasificar CSV simples como evidencia oficial, soporte trazable, intermedio reproducible o transitorio.

## Matriz resumen de salidas

| Codigo / archivo | Funcion | Condicion |
|---|---|---|
| `F-PSEA-10` | Registro de preprocesamiento | evidencia_oficial |
| `F-PSEA-11A` | Datos preprocesados de homogeneidad | soporte_trazable |
| `F-PSEA-11B` | Datos preprocesados de estabilidad | soporte_trazable |
| `F-PSEA-12` | Dataset oficial consolidado | evidencia_oficial |
| `F-PSEA-13` | Informe final de resultados | evidencia_oficial |

## Controles

- Diferenciar `F-PSEA-09` como exportacion desde `calaire-app` y `F-PSEA-12` como dataset consolidado desde `pt_app`.
- Registrar el responsable y momento de generacion de cada archivo conservado.
- Mantener los CSV tecnicos como anexos del flujo, no como formatos `F-PSEA` independientes.
- Asegurar que las evidencias conservadas tambien se reflejen en la matriz de registros/evidencias correspondiente.

## Documentos relacionados

| Codigo | Relacion |
|---|---|
| `DG-PSEA-02` | Origen digital de la ronda. |
| `DG-PSEA-03` | Preprocesamiento, analisis e informe. |
| `I-PSEA-04` | Uso del preprocesador. |
| `I-PSEA-05` | Uso del modulo de analisis. |
| `P-PSEA-07` | Criterio estadistico aplicado. |
| `P-PSEA-09` | Generacion del informe final. |

## Limites

- No es instructivo de uso de aplicativos.
- No gobierna desarrollo, validacion o versionamiento de software.
- No define criterios estadisticos.
- No sustituye el control documental ni la matriz de registros conservados.
