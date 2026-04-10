# F-PSEA-06 — Plan de Ronda EA

**Código:** F-PSEA-06  
**Nivel:** 4 — Formato / Registro  
**Estado:** placeholder — copia de trabajo (Ronda Simple)  
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

## Planificación de Contenido — Ronda Simple

| Campo | Valor esperado |
|-------|---------------|
| **Identificación de ronda** | Ronda Simple — CALAIRE-EA Piloto |
| **Analitos** | CO, SO₂ |
| **Niveles de concentración** | Según P-PSEA-03 (niveles CO) y P-PSEA-05 (niveles SO₂) |
| **Participantes** | 1 (P1 = SIATA) |
| **Método valor asignado** | CRM + dilución (x_pt = C_CRM × f_dilución) |
| **σ_pt** | σ_pt = δ_E / 3 (EQA goal approach) |
| **Algoritmo estadístico** | z-score clásico (n=1, validación directa contra CRM) |
| **Semana** | Semana 1: 20–25 de abril 2026 |
| **Duración** | 1 jornada |
| **CRM requeridos** | Cilindros certificados CO y SO₂ |
| **Equipos generador** | Sistema de dilución dinámica / calibrador T700 o equivalente |
| **Personal asignado** | Por definir (responsable técnico, operador) |

### Campos a completar

- [ ] Identificación formal de la ronda (código, fecha)
- [ ] Analitos y niveles aprobados
- [ ] Lista de CRM con certificados vigentes
- [ ] Equipos de generación y dilución asignados
- [ ] Cronograma detallado de la jornada
- [ ] Personal responsable con firmas
- [ ] Criterios de aceptación (s_hom ≤ 0,3×σ_pt, estabilidad ≤ 0,3×σ_pt)
- [ ] Método de cálculo de x_pt y σ_pt documentado
- [ ] Aprobación del plan por dirección técnica
