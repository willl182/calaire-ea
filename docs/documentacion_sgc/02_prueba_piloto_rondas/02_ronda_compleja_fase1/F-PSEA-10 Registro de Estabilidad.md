# F-PSEA-10 — Registro de Estabilidad

**Código:** F-PSEA-10  
**Nivel:** 4 — Formato / Registro  
**Estado:** placeholder — copia de trabajo (EA-PP2026-R2 — Fase 1)  
**Oleada:** 1  
**Prioridad:** 🔴 Crítica  

---

## Descripción

Registro de las pruebas de estabilidad del ítem PT conforme a ISO 13528 Anexo B, adaptado al esquema in situ. Cubre tres modalidades: (1) estabilidad intrajornada del sistema generador, (2) estabilidad durante la ventana de medición, (3) estabilidad por transporte (solo si aplica envío de cilindros). Registra: mediciones inicio/fin, cálculo de |x̄_inicio − x̄_fin|, verificación del criterio ≤ 0,3 × σ_pt, decisión, fecha y operador. Formato de I-PSEA-10.

---

## Trazabilidad Normativa

| Norma | Cláusula(s) |
|-------|-------------|
| ISO/IEC 17043:2023 | 7.3.2 |
| ISO 13528:2022 | Anexo B |

**Justificación:** Evidencia del estudio de estabilidad

> Fuente: `trazabilidad_normativa_sgc.md`

---

## Planificación de Contenido — Ronda Compleja Fase 1

| Campo | Valor esperado |
|-------|---------------|
| **Analitos** | O₃, NO, NO₂ |
| **Tipo de estabilidad** | Multijornada (2–3 jornadas de medición) |
| **Criterio de aceptación** | \|x̄_inicio − x̄_fin\| ≤ 0,3 × σ_pt por analito |
| **O₃ — atención especial** | Gas reactivo, requiere monitoreo continuo de deriva |
| **NO/NO₂** | Verificar estabilidad del convertidor y ausencia de artefactos |

### Campos a completar

- [ ] Mediciones inicio Jornada 1 — O₃, NO, NO₂ (media de n réplicas)
- [ ] Mediciones fin Jornada 1 — O₃, NO, NO₂
- [ ] Mediciones inicio Jornada 2 — O₃, NO, NO₂
- [ ] Mediciones fin Jornada 2 — O₃, NO, NO₂
- [ ] (Si aplica) Mediciones Jornada 3 — O₃, NO, NO₂
- [ ] Monitoreo de deriva de O₃ entre jornadas (¿requiere corrección?)
- [ ] Cálculo de |x̄_inicio − x̄_fin| para O₃, NO, NO₂
- [ ] Verificación por analito: |Δx̄| ≤ 0,3 × σ_pt
- [ ] Decisión de conformidad por analito (CONFORME / NO CONFORME)
- [ ] Notas especiales sobre estabilidad de O₃ (reactividad, fotólisis)
- [ ] Fecha, operador y firma de aprobación
