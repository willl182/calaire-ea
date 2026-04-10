# F-PSEA-14 — Hoja de Cálculo y Aprobación Estadística

**Código:** F-PSEA-14  
**Nivel:** 4 — Formato / Registro  
**Estado:** placeholder — copia de trabajo (Ronda Compleja Fase 1)  
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

## Planificación de Contenido — Ronda Compleja Fase 1

| Campo | Valor esperado |
|-------|---------------|
| **Método valor asignado** | CRM + dilución para NO/NO₂; generador UV + SRN para O₃ |
| **σ_pt** | σ_pt = δ_E / 3 (EQA goal approach) por analito |
| **Algoritmo estadístico** | Algoritmo B (robusto, ISO 13528 §7) si n<15 |
| **Participantes** | P1 + P2 (n=2) |
| **Scores** | z, z' para P1 y P2 en O₃, NO, NO₂ |
| **Total scores** | 6 (3 analitos × 2 participantes) |

### Campos a completar — Cálculos por analito

- [ ] **O₃:** x_pt, u(x_pt), σ_pt, z-score P1, z-score P2
- [ ] **NO:** x_pt, u(x_pt), σ_pt, z-score P1, z-score P2
- [ ] **NO₂:** x_pt, u(x_pt), σ_pt, z-score P1, z-score P2

### Campos a completar — Aprobación

- [ ] Algoritmo B aplicado (documentar entrada/salida) si n<15
- [ ] Interpretación de scores por participante y analito
- [ ] |z| ≤ 2.0 → Satisfactorio; 2.0 < |z| < 3.0 → Cuestionable; |z| ≥ 3.0 → No satisfactorio
- [ ] Gráficos generados (exportados desde CALAIRE-APP): z-score por analito
- [ ] Verificación de consistencia de cálculos (6 scores)
- [ ] Comparabilidad de resultados P1 vs P2
- [ ] Firma de aprobación del estadístico responsable
- [ ] Aprobación por dirección técnica
