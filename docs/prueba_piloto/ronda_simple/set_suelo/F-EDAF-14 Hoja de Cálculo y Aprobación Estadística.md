# F-EDAF-14 — Hoja de Cálculo y Aprobación Estadística

**Código:** F-EDAF-14  
**Nivel:** 4 — Formato / Registro  
**Estado:** draft — listo para diligenciamiento y aprobación  
**Prioridad:** 🔴 Crítica  

---

## 1. Propósito del formato

Registro formal de los cálculos estadísticos realizados para cada ronda de suelos y la aprobación de los resultados. Incluye: datos de entrada, método de cálculo del valor asignado, estadísticos calculados, valor asignado x_pt, σ_pt, scores de cada participante (z, z', ζ), prueba de Grubbs, gráficos generados, verificación de consistencia, y firma de aprobación del responsable estadístico.

---

## 2. Trazabilidad normativa

| Norma | Cláusula(s) |
|-------|-------------|
| ISO/IEC 17043:2023 | 7.4.2 |
| ISO 13528:2022 | 7, 8, 9 |

**Justificación:** Registro de cálculos: x_pt, sigma_pt, z, decisión estadística

> Fuente: `trazabilidad_normativa_sgc.md`

---

## 3. Identificación de la ronda

| Campo | Dato |
|-------|------|
| Código de la ronda | `[POR DEFINIR]` |
| Nombre de la ronda | Ronda Simple — Suelos Agrícolas |
| Fecha de cálculo | `[POR DEFINIR]` |
| Analista / estadístico responsable | `[POR DEFINIR]` |
| Revisó | `[POR DEFINIR]` |
| Aprobó | `[POR DEFINIR]` |
| Vinculado a F-EDAF-12 y F-EDAF-13 | `[Sí / No]` |

---

## 4. Datos de entrada

### 4.1 Información del participante

| Campo | Dato |
|---|---|
| Código anónimo del participante | `[POR DEFINIR]` |
| Resultados reportados | Ver F-EDAF-12 |
| Incertidumbre reportada (si aplica) | Ver F-EDAF-12 |
| Método de análisis declarado | Ver F-EDAF-12 |

### 4.2 Valor de referencia (x_pt)

| Analito | Fuente del valor | x_pt | u(x_pt) | Unidad |
|---|---|---|---|---|
| pH | CRM certificado | `[POR DEFINIR]` | `[POR DEFINIR]` | unidades pH |
| Materia orgánica | CRM certificado | `[POR DEFINIR]` | `[POR DEFINIR]` | % p/p |
| Nitrógeno total | CRM certificado | `[POR DEFINIR]` | `[POR DEFINIR]` | % p/p |
| Fósforo disponible | CRM certificado | `[POR DEFINIR]` | `[POR DEFINIR]` | mg/kg |
| Potasio intercambiable | CRM certificado | `[POR DEFINIR]` | `[POR DEFINIR]` | mg/kg |
| CEC | CRM certificado | `[POR DEFINIR]` | `[POR DEFINIR]` | cmol(+)/kg |
| Textura (% arena) | CRM certificado | `[POR DEFINIR]` | `[POR DEFINIR]` | % p/p |
| Textura (% limo) | CRM certificado | `[POR DEFINIR]` | `[POR DEFINIR]` | % p/p |
| Textura (% arcilla) | CRM certificado | `[POR DEFINIR]` | `[POR DEFINIR]` | % p/p |

### 4.3 Desviación estándar del esquema (σ_pt)

| Analito | σ_pt | Unidad | Fuente / criterio |
|---|---|---|---|
| pH | `[POR DEFINIR]` | unidades pH | `[EQA goal / δ_E / 3]` |
| Materia orgánica | `[POR DEFINIR]` | % p/p | `[EQA goal / δ_E / 3]` |
| Nitrógeno total | `[POR DEFINIR]` | % p/p | `[EQA goal / δ_E / 3]` |
| Fósforo disponible | `[POR DEFINIR]` | mg/kg | `[EQA goal / δ_E / 3]` |
| Potasio intercambiable | `[POR DEFINIR]` | mg/kg | `[EQA goal / δ_E / 3]` |
| CEC | `[POR DEFINIR]` | cmol(+)/kg | `[EQA goal / δ_E / 3]` |
| Textura (% arena) | `[POR DEFINIR]` | % p/p | `[EQA goal / δ_E / 3]` |
| Textura (% limo) | `[POR DEFINIR]` | % p/p | `[EQA goal / δ_E / 3]` |
| Textura (% arcilla) | `[POR DEFINIR]` | % p/p | `[EQA goal / δ_E / 3]` |

---

## 5. Métodos de cálculo

### 5.1 Método de cálculo del valor asignado

- [ ] **CRM directo:** x_pt = valor certificado del CRM de suelo (NIST SRM 2710a, SRM 2711a o equivalente).
- [ ] **Promedio robusto:** x_pt = mediana o promedio recortado de resultados de participantes (n ≥ 5). No aplica para ronda con participante único.
- [ ] **Otro método:** `[POR DEFINIR]` (justificar).

### 5.2 Método de cálculo de σ_pt

- [ ] **EQA goal approach:** σ_pt = δ_E / 3, donde δ_E es la tolerancia máxima aceptable.
- [ ] **Desviación estándar del CRM:** σ_pt = u(x_pt) × factor de expansión.
- [ ] **Otro método:** `[POR DEFINIR]` (justificar).

### 5.3 Método de evaluación del desempeño

- [ ] **z-score directo:** z = (x_participante - x_pt) / σ_pt
- [ ] **z' (incertidumbre del valor asignado incluida):** z' = (x - x_pt) / √(σ_pt² + u(x_pt)²)
- [ ] **ζ (incertidumbre del participante incluida):** ζ = (x - x_pt) / √(σ_pt² + u(x_pt)² + u(x)²)
- [ ] **Otro:** `[POR DEFINIR]` (justificar).

---

## 6. Cálculos estadísticos

### 6.1 Cálculo de x_pt y u(x_pt)

| Analito | x_pt | u(x_pt) | Cálculo detallado |
|---|---|---|---|
| pH | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` |
| MO | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` |
| N total | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` |
| P disponible | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` |
| K intercambiable | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` |
| CEC | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` |
| Textura (% arena) | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` |
| Textura (% limo) | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` |
| Textura (% arcilla) | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` |

### 6.2 Cálculo de σ_pt

| Analito | σ_pt | Fuente de δ_E | Cálculo |
|---|---|---|---|
| pH | `[POR DEFINIR]` | `[POR DEFINIR]` | σ_pt = δ_E / 3 |
| MO | `[POR DEFINIR]` | `[POR DEFINIR]` | σ_pt = δ_E / 3 |
| N total | `[POR DEFINIR]` | `[POR DEFINIR]` | σ_pt = δ_E / 3 |
| P disponible | `[POR DEFINIR]` | `[POR DEFINIR]` | σ_pt = δ_E / 3 |
| K intercambiable | `[POR DEFINIR]` | `[POR DEFINIR]` | σ_pt = δ_E / 3 |
| CEC | `[POR DEFINIR]` | `[POR DEFINIR]` | σ_pt = δ_E / 3 |
| Textura (% arena) | `[POR DEFINIR]` | `[POR DEFINIR]` | σ_pt = δ_E / 3 |
| Textura (% limo) | `[POR DEFINIR]` | `[POR DEFINIR]` | σ_pt = δ_E / 3 |
| Textura (% arcilla) | `[POR DEFINIR]` | `[POR DEFINIR]` | σ_pt = δ_E / 3 |

### 6.3 Cálculo de scores por participante

| Analito | x_participante | x_pt | σ_pt | z calculado | z' (si aplica) | ζ (si aplica) |
|---|---|---|---|---|---|---|
| pH | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` |
| MO | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` |
| N total | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` |
| P disponible | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` |
| K intercambiable | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` |
| CEC | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` |
| Textura (% arena) | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` |
| Textura (% limo) | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` |
| Textura (% arcilla) | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` |

---

## 7. Interpretación de resultados

| Rango de |z| | Clasificación | Color | Acción |
|---|---|---|---|---|
| \|z\| ≤ 2.0 | Satisfactorio | 🟢 Verde | Participante demuestra competencia |
| 2.0 < \|z\| < 3.0 | Cuestionable | 🟡 Amarillo | Seguimiento requerido, posible acción preventiva |
| \|z\| ≥ 3.0 | No satisfactorio | 🔴 Rojo | Acción correctiva requerida, considerar exclusión de analito |

### 7.1 Resumen de desempeño por analito

| Analito | z / z' / ζ | Clasificación | Color |
|---|---|---|---|
| pH | `[POR DEFINIR]` | `[Satisfactorio / Cuestionable / No satisfactorio]` | `[🟢 / 🟡 / 🔴]` |
| MO | `[POR DEFINIR]` | `[Satisfactorio / Cuestionable / No satisfactorio]` | `[🟢 / 🟡 / 🔴]` |
| N total | `[POR DEFINIR]` | `[Satisfactorio / Cuestionable / No satisfactorio]` | `[🟢 / 🟡 / 🔴]` |
| P disponible | `[POR DEFINIR]` | `[Satisfactorio / Cuestionable / No satisfactorio]` | `[🟢 / 🟡 / 🔴]` |
| K intercambiable | `[POR DEFINIR]` | `[Satisfactorio / Cuestionable / No satisfactorio]` | `[🟢 / 🟡 / 🔴]` |
| CEC | `[POR DEFINIR]` | `[Satisfactorio / Cuestionable / No satisfactorio]` | `[🟢 / 🟡 / 🔴]` |
| Textura (% arena) | `[POR DEFINIR]` | `[Satisfactorio / Cuestionable / No satisfactorio]` | `[🟢 / 🟡 / 🔴]` |
| Textura (% limo) | `[POR DEFINIR]` | `[Satisfactorio / Cuestionable / No satisfactorio]` | `[🟢 / 🟡 / 🔴]` |
| Textura (% arcilla) | `[POR DEFINIR]` | `[Satisfactorio / Cuestionable / No satisfactorio]` | `[🟢 / 🟡 / 🔴]` |

---

## 8. Detección y tratamiento de valores atípicos

### 8.1 Prueba de Grubbs (si n ≥ 3 participantes)

| Analito | Estadístico de Grubbs | Valor crítico (α=0.05) | ¿Outlier? |
|---|---|---|---|
| pH | `[POR DEFINIR]` | `[POR DEFINIR]` | `[Sí / No / No aplica]` |
| MO | `[POR DEFINIR]` | `[POR DEFINIR]` | `[Sí / No / No aplica]` |
| N total | `[POR DEFINIR]` | `[POR DEFINIR]` | `[Sí / No / No aplica]` |
| P disponible | `[POR DEFINIR]` | `[POR DEFINIR]` | `[Sí / No / No aplica]` |
| K intercambiable | `[POR DEFINIR]` | `[POR DEFINIR]` | `[Sí / No / No aplica]` |
| CEC | `[POR DEFINIR]` | `[POR DEFINIR]` | `[Sí / No / No aplica]` |
| Textura (% arena) | `[POR DEFINIR]` | `[POR DEFINIR]` | `[Sí / No / No aplica]` |
| Textura (% limo) | `[POR DEFINIR]` | `[POR DEFINIR]` | `[Sí / No / No aplica]` |
| Textura (% arcilla) | `[POR DEFINIR]` | `[POR DEFINIR]` | `[Sí / No / No aplica]` |

**Nota:** Para ronda con participante único (n=1), la prueba de Grubbs no aplica. Se evalúa directamente contra el valor de referencia.

### 8.2 Tratamiento de outliers identificados

- [ ] Outlier confirmado: excluir del cálculo de estadísticos robustos (si aplica multi-participante).
- [ ] Outlier no confirmado: mantener en el análisis.
- [ ] Investigación documentada: registrar causas posibles y evidencia.
- [ ] Decisión aprobada por responsable estadístico.

---

## 9. Gráficos generados

- [ ] Gráfico de barras de z-scores por analito.
- [ ] Gráfico de Youden (si aplica para comparación entre analitos).
- [ ] Gráfico de tendencia (si hay rondas históricas).
- [ ] Archivos exportados del aplicativo CALAIRE-APP (R/Shiny).

---

## 10. Verificación de consistencia de cálculos

| Verificación | Estado | Observaciones |
|---|---|---|
| x_pt calculado correctamente desde CRM | `[Correcto / Incorrecto]` | |
| σ_pt calculado correctamente (δ_E / 3) | `[Correcto / Incorrecto]` | |
| z-score calculado correctamente | `[Correcto / Incorrecto]` | |
| Unidades consistentes entre x_pt, x_participante y σ_pt | `[Correcto / Incorrecto]` | |
| Clasificación de colores asignada correctamente | `[Correcto / Incorrecto]` | |
| Prueba de Grubbs ejecutada (si aplica) | `[Ejecutada / No aplica]` | |
| Archivos del aplicativo verificados | `[Correcto / Incorrecto]` | |

---

## 11. Campos pendientes de diligentiamiento

- Valores numéricos finales de x_pt, u(x_pt) y σ_pt por analito.
- Scores calculados por participante.
- Clasificación final de desempeño.
- Gráficos generados y archivados.
- Firmas de aprobación estadística.

---

## 12. Aprobaciones

| Cargo | Nombre | Firma | Fecha |
|---|---|---|---|
| Estadístico responsable | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` |
| Responsable técnico | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` |
| Aprobó (Dirección EA) | `[POR DEFINIR]` | `[POR DEFINIR]` | `[POR DEFINIR]` |
