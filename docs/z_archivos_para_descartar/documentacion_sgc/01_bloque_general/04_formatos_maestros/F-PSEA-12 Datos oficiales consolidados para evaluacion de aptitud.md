# F-PSEA-12 Datos oficiales consolidados para evaluacion de aptitud

**Codigo:** F-PSEA-12  
**Version:** 0  
**Tipo:** Formato maestro  
**Fuente base definida:** `ronda_1_completa.csv`  
**Aplicacion:** Dataset oficial consolidado para evaluacion de aptitud.

---

## 1. Objetivo

Formalizar el dataset oficial consolidado que se usa para la evaluacion de aptitud, integrando datos de participantes, referencia o fuentes tecnicas necesarias para el analisis estadistico.

---

## 2. Alcance

Aplica al conjunto de datos consolidado posterior a la recepcion, exportacion y preprocesamiento. Este formato representa la base oficial para calculos estadisticos, evaluacion de desempeno e informe final.

---

## 3. Fuente de datos

La fuente definida es `ronda_1_completa.csv`, con el siguiente esquema observado:

| Campo | Descripcion |
|---|---|
| `pollutant` | Contaminante. |
| `level` | Nivel de concentracion. |
| `source` | Fuente del dato. |
| `run` | Corrida. |
| `unit` | Unidad. |
| `instrument` | Instrumento asociado. |
| `mean_h1` | Primer promedio horario. |
| `mean_h2` | Segundo promedio horario. |
| `mean_h3` | Tercer promedio horario. |
| `mean_value` | Promedio consolidado. |
| `sd_value` | Desviacion estandar. |
| `u_value` | Incertidumbre estandar u otra declarada. |
| `n_hours` | Numero de horas usadas. |
| `hour_starts` | Fechas/horas asociadas. |
| `participant_id` | Identificador de participante. |
| `tipo` | Tipo de dato: participante, referencia u otro. |
| `k_factor` | Factor de cobertura. |
| `u_exp` | Incertidumbre expandida. |
| `n_lab` | Numero de laboratorios asociados al calculo o nivel. |

---

## 4. Reglas de consolidacion

- El dataset debe generarse despues de `F-PSEA-10`.
- Los datos deben estar normalizados por contaminante, nivel, corrida y unidad.
- Cada fila debe conservar trazabilidad de fuente, participante/instrumento y tipo.
- Los campos de incertidumbre deben conservarse como valores separados, no solo como observaciones.
- Las filas excluidas del analisis no deben aparecer como oficiales, salvo que esten marcadas con estado y justificacion.
- El archivo consolidado debe versionarse si se regenera.

---

## 5. Campos de control del formato

| Campo de control | Descripcion |
|---|---|
| Ronda | Identificador de ronda. |
| Archivo fuente | Archivo consolidado usado. |
| Fecha de consolidacion | Fecha/hora de generacion. |
| Responsable | Responsable de consolidacion. |
| Version de `pt_app` | Version usada para generar el dataset. |
| Numero de filas | Cantidad de registros oficiales. |
| Contaminantes incluidos | Lista de gases incluidos. |
| Estado | `aprobado`, `con observaciones`, `reemplazado`. |
| Observaciones | Comentarios tecnicos. |

---

## 6. Relacion documental

| Documento | Relacion |
|---|---|
| `F-PSEA-09` | Exportacion oficial desde `calaire-app`. |
| `F-PSEA-10` | Preprocesamiento que genera o valida el dataset. |
| `P-PSEA-07` | Procedimiento estadistico que usa el dataset. |
| `F-PSEA-13` | Informe final que reporta resultados derivados. |

---

## 7. Criterio de completitud

El formato se considera completo cuando el dataset oficial esta generado, versionado, aprobado y contiene todos los campos necesarios para reproducir la evaluacion de aptitud.
