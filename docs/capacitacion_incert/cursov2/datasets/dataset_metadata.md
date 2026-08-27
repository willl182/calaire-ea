# Metadata — dataset_verificacion_multipunto.csv

Dataset **sintético** generado para los ejercicios M5 del curso. No contiene datos operativos de ninguna red ni esquema. Reproducible con `generar_dataset.R` (semilla `20260817`).

## Estructura

- 3 ciclos de verificación (días consecutivos simulados, 1 punto cada 20 min).
- Por ciclo: cero pre → 6 niveles (~20/40/70/100/140/180 ppb) → cero post. 24 filas.

| Columna | Unidad | Descripción |
|---|---|---|
| `timestamp` | ISO 8601 UTC | hora simulada del punto |
| `ciclo` | — | 1–3 |
| `punto` | — | `cero_pre`, `nivel`, `cero_post` |
| `nivel_nominal` | ppb | consigna del generador |
| `lectura_ref` | ppb | lectura del patrón de referencia, **sin corregir** por certificado |
| `lectura_uut` | ppb | lectura del equipo bajo prueba |
| `T_celda_K` | K | temperatura de celda |
| `P_celda_kPa` | kPa | presión de celda |
| `flujo_L_min` | L/min | flujo de muestra |

## Certificado simulado del patrón de referencia

Para corregir `lectura_ref`: X = (lectura_ref − b) / m, con:

- pendiente m = **1.003**
- intercepto b = **−0.4 ppb**
- U(X) = **0.5 ppb + 0.01·X** (k = 2)

## Efectos inyectados (para el solucionario del instructor)

- Ruido: 0.25 ppb RMS (spec Thermo 49i) + componente proporcional 0.15 %.
- Deriva del UUT: +0.15 ppb/ciclo en cero; +0.0008/ciclo en pendiente.
- Falta de ajuste: curvatura −1.85×10⁻⁵ ppb⁻¹ (≈ −0.6 ppb a 180 ppb).
- UUT base: pendiente 0.9950, offset +0.30 ppb respecto al valor generado.

Resultados esperados por ciclo (regresión UUT vs referencia corregida): pendiente ≈ 0.990–0.997, intercepto ≈ +0.1 a +1.3 ppb, s_residual ≈ 0.3–0.45 ppb.

> **Nota (defecto D8):** este dataset es enteramente conforme, con holgura amplia frente a los límites de aceptación y sin deriva observable entre ciclos que fuerce una decisión de no conformidad. No se regeneró para introducir un ciclo no conforme. La rama de rechazo/estado encontrado (punto o ciclo que falla, investigación previa a un ajuste) se ejercita con datos reales en la práctica de laboratorio, `practica/E02_verificacion_multipunto.md`, donde el resultado depende del instrumento real y no está garantizado de antemano.
>
> **Nota de unidades (defecto D7):** las columnas de este dataset usan `ppb` por continuidad con el ejercicio original de M5. Para la práctica de laboratorio (`practica/`) y para cualquier hoja de campo nueva, la unidad de referencia es **nmol/mol** (numéricamente equivalente a ppb para fracción molar, pero preferida por BIPM.QM-K1 §4).
