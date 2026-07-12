# Instrucciones - F-PSEA-10 Registro de preprocesamiento de datos

**Codigo:** `F-PSEA-10`  
**Tipo:** Formato / registro tecnico  
**Sistema fuente:** `pt_app`  
**Entrada principal:** `F-PSEA-09 Datos de participantes exportados para analisis PT`  
**Salida principal:** `F-PSEA-12 Datos oficiales consolidados para evaluacion de aptitud`  
**Estado:** pendiente de consolidacion como maestro documental  
**Ubicacion esperada:** `01_bloque_general/04_formatos_maestros/F-PSEA-10 Registro de preprocesamiento de datos.docx`

---

## Proposito

Documentar de forma reproducible la ejecucion del preprocesamiento de datos en `pt_app`, desde la recepcion del paquete exportado por `calaire-app` hasta la generacion de salidas listas para consolidacion, analisis estadistico y evaluacion de aptitud.

El registro debe permitir reconstruir que archivo entro, que version del aplicativo se uso, que reglas fueron aplicadas, que registros fueron corregidos o excluidos y que archivo(s) se generaron como salida.

---

## Alcance

Aplica a toda ejecucion de preprocesamiento ejecutada sobre datos de participantes o datos tecnicos de ronda antes de producir:

- dataset oficial consolidado;
- datos preprocesados de homogeneidad;
- datos preprocesados de estabilidad;
- archivos listos para calculo estadistico;
- insumos del informe final.

No sustituye el procedimiento estadistico (`P-PSEA-07`) ni el instructivo de uso de `pt_app` (`I-PSEA-04`). Este formato registra la evidencia de una ejecucion especifica.

---

## Entradas minimas

| Entrada | Descripcion |
|---|---|
| `round_id` | Identificador de la ronda. |
| `input_file` | Ruta o nombre del archivo de entrada. |
| `input_source` | Fuente del archivo: normalmente `F-PSEA-09`. |
| `input_hash` | Hash o identificador de integridad si aplica. |
| `input_rows` | Numero de registros recibidos. |
| `input_columns` | Columnas recibidas. |
| `pt_app_version` | Version de `pt_app` usada. |
| `preprocessor_version` | Version del modulo/preprocesador si difiere de la app. |
| `executed_at` | Fecha y hora de ejecucion. |
| `executed_by` | Responsable de ejecucion. |

---

## Reglas a documentar

El registro debe indicar las reglas aplicadas, incluyendo:

- normalizacion de nombres de contaminantes;
- validacion de unidades;
- validacion de niveles y corridas;
- validacion de participantes esperados;
- tratamiento de valores faltantes;
- tratamiento de valores no numericos;
- identificacion de duplicados;
- conversion o estandarizacion de fechas;
- calculo o verificacion de promedios;
- verificacion de incertidumbre reportada;
- separacion por tipo de fuente: participante, referencia, homogeneidad, estabilidad u otra;
- reglas de exclusion o marcacion de observaciones.

---

## Campos minimos del registro

| Campo | Descripcion |
|---|---|
| `run_id` | Identificador unico de la ejecucion de preprocesamiento. |
| `round_id` | Ronda procesada. |
| `input_file` | Archivo de entrada. |
| `input_rows` | Numero de filas recibidas. |
| `valid_rows` | Numero de filas validas luego del preprocesamiento. |
| `excluded_rows` | Numero de filas excluidas. |
| `warning_count` | Numero de advertencias generadas. |
| `error_count` | Numero de errores bloqueantes. |
| `ruleset_version` | Version de reglas aplicadas. |
| `output_files` | Archivo(s) generados. |
| `output_hash` | Identificador de integridad de salida si aplica. |
| `status` | `aprobado`, `con observaciones`, `rechazado`. |
| `reviewed_by` | Responsable de revision tecnica si aplica. |
| `approved_by` | Responsable de aprobacion si aplica. |
| `observations` | Observaciones de ejecucion. |

---

## Tratamiento de exclusiones y correcciones

Toda exclusion o correccion debe registrar:

- identificador del registro afectado;
- campo afectado;
- valor original;
- accion aplicada: `corregido`, `excluido`, `marcado`, `aceptado con observacion`;
- regla que justifica la accion;
- responsable;
- fecha;
- observacion tecnica.

No se permite excluir datos sin justificacion documentada.

---

## Salidas esperadas

El preprocesamiento puede generar:

- `F-PSEA-12` Dataset oficial consolidado;
- `F-PSEA-11A` Datos preprocesados de homogeneidad;
- `F-PSEA-11B` Datos preprocesados de estabilidad;
- archivos de log;
- reporte de validacion;
- tabla de exclusiones/correcciones;
- insumos para `F-PSEA-13` Informe final de resultados.

---

## Criterio de aprobacion

`F-PSEA-10` se considera aprobado cuando:

1. el archivo de entrada esta identificado y trazado;
2. la version de `pt_app` y del preprocesador fue registrada;
3. las reglas aplicadas quedaron documentadas;
4. las exclusiones o correcciones tienen justificacion;
5. los archivos de salida fueron generados e identificados;
6. no hay errores bloqueantes;
7. el responsable tecnico aprueba la ejecucion o documenta observaciones.

---

## Relacion documental

| Documento | Relacion |
|---|---|
| `F-PSEA-09` | Entrada oficial exportada desde `calaire-app`. |
| `I-PSEA-04` | Instructivo operativo para ejecutar el preprocesador de `pt_app`. |
| `P-PSEA-07` | Procedimiento de diseno estadistico y reglas tecnicas aplicables. |
| `F-PSEA-11A-D` | Salidas relacionadas con homogeneidad y estabilidad. |
| `F-PSEA-12` | Salida consolidada para evaluacion de aptitud. |
| `F-PSEA-13` | Informe final que consume resultados procesados. |
