# F-PSEA-06 — Plan de Ronda EA

**Código:** F-PSEA-06  
**Nivel:** 4 — Formato / Registro  
**Estado:** NO EJECUTADA en EA-PP2026-R2 — P2 (UPB) diferido a siguiente ronda  
**Oleada:** 1  
**Prioridad:** 🔴 Crítica  

---

## Descripción

Formato para documentar el plan específico de cada ronda de EA. Incluye: identificación de la ronda, analito(s) y niveles de concentración, número y codificación de participantes, método del valor asignado, σ_pt aplicable, algoritmo estadístico seleccionado, cronograma de la ronda, personal asignado, equipos y CRM a utilizar, y criterios de aceptación. Es el documento operativo clave que se genera a partir de P-PSEA-09.

---

## Trazabilidad Normativa

| Norma | Cláusula(s) |
|-------|-------------|
| ISO/IEC 17043:2023 | 7.2.1.3 |
| ISO 13528:2022 | 5 |

**Justificación:** Registro del plan aprobado de cada ronda

> Fuente: `trazabilidad_normativa_sgc.md`

---

## Planificación de Contenido — EA-PP2026-R2 (Fase 2)

| Campo | Valor esperado |
|-------|---------------|
| **Identificación de ronda** | EA-PP2026-R2 — Ronda Compleja Fase 2 — CALAIRE-EA Piloto |
| **Analitos** | CO, SO₂ |
| **Niveles de concentración** | Reutilización de CRM/niveles de Ronda Simple (permite comparación P1 vs P2) |
| **Participantes** | 1 (P2 = UPB) |
| **Método valor asignado** | CRM + dilución (x_pt = C_CRM × f_dilución) — mismos CRM que Ronda Simple |
| **σ_pt** | σ_pt = δ_E / 3 (mismo criterio que Ronda Simple) |
| **Algoritmo estadístico** | z-score directo contra valor de referencia (CRM) |
| **Semana** | Semana 2: cierre (post-Fase 1) |
| **Duración** | 1 jornada |
| **CRM requeridos** | Reutilizar cilindros de CO y SO₂ de la Ronda Simple |
| **Equipos generador** | Sistema de dilución dinámica / calibrador T700 o equivalente |
| **Valor comparativo** | Permite comparar z-score P2 (CO/SO₂) con z-score P1 (CO/SO₂ de Ronda Simple) |

### Campos a completar

- [ ] Identificación formal de la ronda (código, fecha)
- [ ] Analitos y niveles (documentar correspondencia con Ronda Simple)
- [ ] Verificación de vigencia de CRM reutilizados
- [ ] Equipos de generación y dilución asignados
- [ ] Cronograma detallado de la jornada
- [ ] Personal responsable con firmas
- [ ] Criterios de aceptación (s_hom ≤ 0,3×σ_pt, estabilidad ≤ 0,3×σ_pt)
- [ ] Método de cálculo de x_pt y σ_pt (idéntico a Ronda Simple)
- [ ] Plan de comparación con resultados de Ronda Simple
- [ ] Aprobación del plan por dirección técnica
