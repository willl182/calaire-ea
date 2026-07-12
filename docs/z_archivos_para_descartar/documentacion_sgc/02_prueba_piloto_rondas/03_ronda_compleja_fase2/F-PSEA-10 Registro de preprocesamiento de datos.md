# F-PSEA-10 — Registro de Estabilidad

**Código:** F-PSEA-10  
**Nivel:** 4 — Formato / Registro  
**Estado:** NO EJECUTADA en EA-PP2026-R2 — P2 (UPB) diferido a siguiente ronda  
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

## Planificación de Contenido — Ronda Compleja Fase 2

| Campo | Valor esperado |
|-------|---------------|
| **Analitos** | CO, SO₂ |
| **Tipo de estabilidad** | Intrajornada (1 jornada de medición, cierre) |
| **Criterio de aceptación** | \|x̄_inicio − x̄_fin\| ≤ 0,3 × σ_pt |
| **Modalidad transporte** | No aplica (in situ) |
| **Nota** | Post-devolución de equipos O₃/NO/NO₂ — verificar estado de sistemas |

### Campos a completar

- [ ] Mediciones al inicio de la jornada — CO (media de n réplicas)
- [ ] Mediciones al inicio de la jornada — SO₂ (media de n réplicas)
- [ ] Mediciones al final de la jornada — CO (media de n réplicas)
- [ ] Mediciones al final de la jornada — SO₂ (media de n réplicas)
- [ ] Cálculo de |x̄_inicio − x̄_fin| para CO
- [ ] Cálculo de |x̄_inicio − x̄_fin| para SO₂
- [ ] Verificación: |Δx̄|(CO) ≤ 0,3 × σ_pt(CO)
- [ ] Verificación: |Δx̄|(SO₂) ≤ 0,3 × σ_pt(SO₂)
- [ ] Verificación post-cambio de configuración (de O₃/NO/NO₂ a CO/SO₂)
- [ ] Decisión de conformidad (CONFORME / NO CONFORME)
- [ ] Fecha, operador y firma de aprobación
