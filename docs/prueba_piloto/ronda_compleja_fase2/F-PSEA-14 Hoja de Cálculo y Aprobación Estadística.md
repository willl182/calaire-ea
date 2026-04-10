# F-PSEA-14 — Hoja de Cálculo y Aprobación Estadística

**Código:** F-PSEA-14  
**Nivel:** 4 — Formato / Registro  
**Estado:** placeholder — copia de trabajo (Ronda Compleja Fase 2)  
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

## Planificación de Contenido — Ronda Compleja Fase 2

| Campo | Valor esperado |
|-------|---------------|
| **Método valor asignado** | CRM + dilución: x_pt = C_CRM × f_dilución (mismo que Ronda Simple) |
| **Incertidumbre x_pt** | u(x_pt) combinada (CRM + dilución) |
| **σ_pt** | σ_pt = δ_E / 3 (mismo δ_E que Ronda Simple) |
| **Algoritmo estadístico** | z-score directo contra valor de referencia (CRM) |
| **Participantes** | P2 (n=1) — validación directa contra CRM |
| **Scores** | z = (x_P2 - x_pt) / σ_pt para P2 en CO y SO₂ |
| **Valor comparativo** | Comparar z(P2) con z(P1) de Ronda Simple para mismos analitos |

### Campos a completar

- [ ] Cálculo de x_pt para CO: C_CRM × (Q_CRM / Q_total)
- [ ] Cálculo de u(x_pt) para CO: combinación u(CRM) + u(dilución)
- [ ] Cálculo de σ_pt para CO: δ_E / 3 (verificar consistencia con Ronda Simple)
- [ ] Cálculo de z-score P2 para CO: z = (x_P2 - x_pt) / σ_pt
- [ ] Cálculo de x_pt para SO₂: C_CRM × (Q_CRM / Q_total)
- [ ] Cálculo de u(x_pt) para SO₂: combinación u(CRM) + u(dilución)
- [ ] Cálculo de σ_pt para SO₂: δ_E / 3 (verificar consistencia con Ronda Simple)
- [ ] Cálculo de z-score P2 para SO₂: z = (x_P2 - x_pt) / σ_pt
- [ ] Interpretación: |z| ≤ 2.0 → Satisfactorio; 2.0 < |z| < 3.0 → Cuestionable; |z| ≥ 3.0 → No satisfactorio
- [ ] **Comparación con Ronda Simple:** z(P2) vs z(P1) para CO y SO₂
- [ ] Gráficos generados (exportados desde CALAIRE-APP)
- [ ] Verificación de consistencia de cálculos
- [ ] Firma de aprobación del estadístico responsable
- [ ] Aprobación por dirección técnica
