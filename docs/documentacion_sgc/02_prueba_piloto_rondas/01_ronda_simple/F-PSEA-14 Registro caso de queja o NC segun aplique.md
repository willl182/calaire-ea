# F-PSEA-14 — Hoja de Cálculo y Aprobación Estadística

**Código:** F-PSEA-14  
**Nivel:** 4 — Formato / Registro  
**Estado:** placeholder — copia de trabajo (EA-PP2026-R1)  
**Oleada:** 1  
**Prioridad:** 🔴 Crítica  

---

## Descripción

Registro formal de los cálculos estadísticos realizados para cada ronda y la aprobación de los resultados. Incluye: datos de entrada, algoritmo utilizado (A/B/C), estadísticos robustos calculados (media/mediana, s/NIQR), valor asignado x_pt, σ_pt, scores de cada participante (z, z', ζ), prueba de Grubbs, gráficos generados, verificación de consistencia, y firma de aprobación del estadístico responsable. Vinculado al aplicativo R/Shiny.

---

## Trazabilidad Normativa

| Norma | Cláusula(s) |
|-------|-------------|
| ISO/IEC 17043:2023 | 7.4.2 |
| ISO 13528:2022 | 7, 8, 9 |

**Justificación:** Registro de cálculos: x_pt, sigma_pt, z, decisión estadística

> Fuente: `trazabilidad_normativa_sgc.md`

---

## Planificación de Contenido — Ronda Simple

| Campo | Valor esperado |
|-------|---------------|
| **Método valor asignado** | CRM + dilución: x_pt = C_CRM × f_dilución |
| **Incertidumbre x_pt** | u(x_pt) combinada (CRM + dilución) |
| **σ_pt** | σ_pt = δ_E / 3 (EQA goal approach) |
| **Algoritmo estadístico** | z-score directo contra valor de referencia (CRM) |
| **Participantes** | P1 (n=1) — validación directa contra CRM |
| **Scores** | z = (x - x_pt) / σ_pt para P1 en CO y SO₂ |

### Campos a completar

- [ ] Cálculo de x_pt para CO: C_CRM × (Q_CRM / Q_total)
- [ ] Cálculo de u(x_pt) para CO: combinación u(CRM) + u(dilución)
- [ ] Cálculo de σ_pt para CO: δ_E / 3 (documentar δ_E)
- [ ] Cálculo de z-score P1 para CO: z = (x_P1 - x_pt) / σ_pt
- [ ] Cálculo de x_pt para SO₂: C_CRM × (Q_CRM / Q_total)
- [ ] Cálculo de u(x_pt) para SO₂: combinación u(CRM) + u(dilución)
- [ ] Cálculo de σ_pt para SO₂: δ_E / 3 (documentar δ_E)
- [ ] Cálculo de z-score P1 para SO₂: z = (x_P1 - x_pt) / σ_pt
- [ ] Interpretación: |z| ≤ 2.0 → Satisfactorio; 2.0 < |z| < 3.0 → Cuestionable; |z| ≥ 3.0 → No satisfactorio
- [ ] Gráficos generados (exportados desde pt_app)
- [ ] Verificación de consistencia de cálculos
- [ ] Firma de aprobación del estadístico responsable
- [ ] Aprobación por dirección técnica
