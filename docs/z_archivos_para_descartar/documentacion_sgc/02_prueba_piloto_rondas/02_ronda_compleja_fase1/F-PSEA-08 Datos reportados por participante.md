# F-PSEA-08 — Registro de Preparación del Ítem

**Código:** F-PSEA-08  
**Nivel:** 4 — Formato / Registro  
**Estado:** placeholder — copia de trabajo (EA-PP2026-R2 — Fase 1)  
**Oleada:** 1  
**Prioridad:** 🔴 Crítica  

---

## Descripción

Registro de la preparación/generación de cada ítem PT utilizado en la ronda. Para CALAIRE-EA (atmósferas generadas in situ): identifica el CRM utilizado, certificado del CRM, sistema de dilución, caudales configurados, concentración objetivo, concentración medida con método de referencia, condiciones ambientales (T, P, HR), fecha/hora, operador y criterio de aceptación. Soporta la trazabilidad metrológica.

---

## Trazabilidad Normativa

| Norma | Cláusula(s) |
|-------|-------------|
| ISO/IEC 17043:2023 | 7.3.1 |
| ISO 13528:2022 | — |

**Justificación:** Trazabilidad de la preparación del ítem

> Fuente: `trazabilidad_normativa_sgc.md`

---

## Planificación de Contenido — Ronda Compleja Fase 1

| Campo | Valor esperado |
|-------|---------------|
| **Tipo de ítem PT** | Atmósferas generadas in situ |
| **Sistema generador** | Calibrador dinámico + generador UV O₃ / T700 o equivalente |
| **Analitos** | O₃, NO, NO₂ |
| **Complejidad** | 3 analitos = más registros de preparación |
| **CRM fuente** | Cilindro certificado NO/NO₂ + generador UV O₃ |
| **Generación O₃** | Fotólisis de O₂ con lámpara UV calibrada |
| **Generación NO/NO₂** | Dilución dinámica desde cilindro CRM |

### Campos a completar

- [ ] Identificación del CRM NO/NO₂ (número de cilindro, certificado, fecha vencimiento)
- [ ] Trazabilidad del generador de O₃ (lámpara UV, calibración, certificado SRN)
- [ ] Sistema de dilución utilizado (modelo, serie, calibración vigente)
- [ ] Caudales configurados (Q_CRM, Q_dilución, Q_total) — NO/NO₂
- [ ] Parámetros del generador O₃ (intensidad UV, caudal)
- [ ] Concentración objetivo (setpoint) por analito: O₃, NO, NO₂
- [ ] Concentración medida (método de referencia) por analito
- [ ] Conversión NO→NO₂ si aplica (químoluminiscencia con convertidor)
- [ ] Condiciones ambientales: T (°C), P (kPa), HR (%)
- [ ] Fecha y hora de generación (por jornada)
- [ ] Operador responsable
- [ ] Criterio de aceptación: diferencia ≤ 2% del valor nominal por analito
- [ ] Verificación de trazabilidad metrológica completa (3 analitos)
