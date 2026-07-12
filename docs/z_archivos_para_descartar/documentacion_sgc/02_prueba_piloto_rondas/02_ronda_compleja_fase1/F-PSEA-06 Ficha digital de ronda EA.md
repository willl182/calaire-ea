# F-PSEA-06 — Plan de Ronda EA

**Código:** F-PSEA-06  
**Nivel:** 4 — Formato / Registro  
**Estado:** placeholder — copia de trabajo (EA-PP2026-R2 — Fase 1)  
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

## Planificación de Contenido — EA-PP2026-R2 (Fase 1)

| Campo | Valor esperado |
|-------|---------------|
| **Identificación de ronda** | EA-PP2026-R2 — Ronda Compleja Fase 1 — CALAIRE-EA Piloto |
| **Analitos** | O₃, NO, NO₂ |
| **Niveles de concentración** | Según P-PSEA-02 (niveles O₃) y P-PSEA-04 (niveles NO/NO₂) |
| **Participantes previstos** | 2 (P1 = SIATA, P2 = UPB) |
| **Participantes efectivos** | 1 (P1 = SIATA) — UPB diferido a siguiente ronda por requerimiento de cliente |
| **Método valor asignado** | CRM + dilución dinámica (O₃ por fotólisis/generador; NO/NO₂ desde cilindro CRM) |
| **σ_pt** | σ_pt = δ_E / 3 (EQA goal approach) |
| **Algoritmo estadístico** | Algoritmo B (robusto) si n<15; z-score contra valor de referencia |
| **Semana** | Semana 2: 27 de abril – 2 de mayo 2026 |
| **Duración** | 2–3 jornadas (medición en paralelo de ambos participantes) |
| **CRM requeridos** | Cilindro certificado NO/NO₂ + generador UV de O₃ |
| **Equipos generador** | Sistema de dilución dinámica, generador de O₃, calibrador T700 o equivalente |
| **Complejidad** | Multi-analito (3) × multi-participante (2) = 6 combinaciones de scoring |

### Campos a completar

- [ ] Identificación formal de la ronda (código, fecha)
- [ ] Analitos y niveles aprobados: O₃, NO, NO₂
- [ ] Lista de CRM con certificados vigentes (NO/NO₂ y trazabilidad O₃)
- [ ] Equipos de generación, dilución y fotólisis asignados
- [ ] Cronograma detallado por jornada (coordinación P1 + P2)
- [ ] Personal responsable con firmas
- [ ] Criterios de aceptación (s_hom ≤ 0,3×σ_pt, estabilidad ≤ 0,3×σ_pt por analito)
- [ ] Método de cálculo de x_pt y σ_pt documentado por analito
- [ ] Plan de coordinación de medición en paralelo
- [ ] Aprobación del plan por dirección técnica
