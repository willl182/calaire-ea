# F-PSEA-11 Homogeneidad y estabilidad del item

**Codigo:** F-PSEA-11  
**Version:** 0  
**Tipo:** Formato maestro  
**Fuentes base definidas:** `ronda_1_homogeneidad.csv`, `ronda_1_estabilidad.csv` y anexos por definir  
**Aplicacion:** Registro principal de verificacion de homogeneidad y estabilidad del item de ensayo gaseoso.

---

## 1. Objetivo

Consolidar la evidencia de homogeneidad y estabilidad del item de ensayo gaseoso, registrando los datos usados, criterios aplicados, resultados obtenidos y conclusion tecnica sobre la aptitud del item para la ronda.

---

## 2. Alcance

Aplica a la verificacion del sistema de generacion y distribucion de gases contaminantes criterio usados en la ronda. Incluye los datos de homogeneidad y estabilidad generados o procesados para cada contaminante, nivel y corrida.

---

## 3. Fuentes de datos

### 3.1 Homogeneidad

Fuente inicial: `ronda_1_homogeneidad.csv`

Campos observados:

| Campo | Descripcion |
|---|---|
| `pollutant` | Contaminante. |
| `run` | Corrida. |
| `level` | Nivel. |
| `replicate` | Replica. |
| `sample_id` | Identificador de muestra/punto. |
| `value` | Valor observado. |

### 3.2 Estabilidad

Fuente inicial: `ronda_1_estabilidad.csv`

Campos observados:

| Campo | Descripcion |
|---|---|
| `pollutant` | Contaminante. |
| `run` | Corrida. |
| `level` | Nivel. |
| `replicate` | Replica o momento de evaluacion. |
| `sample_id` | Identificador de muestra/punto. |
| `value` | Valor observado. |

---

## 4. Campos minimos del formato maestro

| Campo | Obligatorio | Descripcion |
|---|---|---|
| Ronda | Si | Identificador de ronda. |
| Contaminante | Si | Gas evaluado. |
| Corrida | Si | Corrida evaluada. |
| Nivel | Si | Nivel de concentracion. |
| Tipo de evaluacion | Si | Homogeneidad o estabilidad. |
| Fuente de datos | Si | Archivo o sistema fuente. |
| Numero de replicas | Si | Cantidad de replicas usadas. |
| Numero de puntos/muestras | Si | Cantidad de puntos o muestras evaluadas. |
| Resultado estadistico | No | Estadistico aplicado segun procedimiento. |
| Criterio de aceptacion | Si | Regla tecnica definida por el PEA. |
| Conclusion | Si | Cumple, no cumple, cumple con observacion. |
| Observaciones | No | Comentarios tecnicos. |

---

## 5. Relacion con subformatos

| Subformato | Uso |
|---|---|
| `F-PSEA-11A` | Datos preprocesados de homogeneidad. |
| `F-PSEA-11B` | Datos preprocesados de estabilidad. |
| `F-PSEA-11C` | Resultados de homogeneidad. |
| `F-PSEA-11D` | Resultados de estabilidad. |

`F-PSEA-11` debe funcionar como registro principal que consolida y referencia los subformatos.

---

## 6. Reglas de control

- La fuente de cada dato debe quedar identificada.
- Los datos modificados o excluidos deben remitir a `F-PSEA-10`.
- Los criterios de aceptacion deben estar alineados con `P-PSEA-07`.
- Las conclusiones deben distinguir homogeneidad y estabilidad.
- Si faltan anexos o datos por definir, el registro debe indicarlo explicitamente.

---

## 7. Criterio de completitud

El formato se considera completo cuando existen datos trazables de homogeneidad y estabilidad, resultados evaluados contra criterios definidos y una conclusion tecnica para cada contaminante/nivel aplicable.
