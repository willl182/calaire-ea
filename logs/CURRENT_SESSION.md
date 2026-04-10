# Session State: CALAIRE-EA — SGC / Prueba Piloto

**Last Updated**: 2026-04-08 18:25

---

## Session Objective

Implementar skeletons de documentos del Sprint 2 del final_plan.md — comunicación con participantes y manejo de ítems PT — **COMPLETADO**.

---

## Current State

- [x] Generados 52 placeholders en `placeholders/` con trazabilidad normativa (sesión anterior)
- [x] Generadas copias enriquecidas (con trazabilidad ISO) en `docs/prueba_piloto/` — 52 archivos `.md`
- [x] Reorganización ejecutada: 16 docs gestión → `gestion/`, 3 carpetas de ronda creadas
- [x] Esqueletos de documentos críticos creados (sesión 2026-04-08 16:15): I-PSEA-10, I-PSEA-07, I-PSEA-08, I-PSEA-13, I-PSEA-02, F-PSEA-05A
- [x] **Sprint 2 prácticamente completado (sesión 2026-04-08 18:25)**:
  - `I-PSEA-09 Instrucciones a Participantes.md` — skeleton completo §1–9 + tabla 13 elementos ISO 17043 §7.3.5 + 3 brechas concretas + Gantt Mermaid
  - `P-PSEA-20 Comunicación PT.md` — skeleton completo: solicitudes, acuerdos, 5 comunicaciones pre-ronda con plazos/aprobaciones, fe de erratas, quejas/apelaciones
  - `P-PSEA-10 Procedimiento de Manejo de Items PT.md` — skeleton completo: MRC, almacenamiento, check-in/out participantes, tabla situaciones especiales, flowchart Mermaid

---

## Estructura de rondas del piloto (CONFIRMADO)

| | **Ronda Simple** | **Ronda Compleja F1** | **Ronda Compleja F2** |
|---|---|---|---|
| **Analitos** | CO, SO₂ | O₃, NO, NO₂ | CO, SO₂ |
| **Participantes** | P1 = SIATA | P1 + P2 = SIATA + UPB | P2 = UPB |
| **Semana** | Sem. 1 (20-25 abr) | Sem. 2 (27 abr–2 may) | Sem. 2 (cierre) |

---

## Estado Sprint 2 — final_plan.md

| # | Documento | Estado |
|---|---|---|
| 1 | F-PSEA-05A — Hoja de Registro del Participante | ✅ Skeleton completo |
| 2 | I-PSEA-02 — Producción PT Items | ✅ Skeleton completo |
| 3 | I-PSEA-09 — Instrucciones a Participantes | ✅ **Creado esta sesión** |
| 4 | I-PSEA-13 — Validación de Software | ✅ Skeleton completo |
| 5 | P-PSEA-20 — Comunicación PT | ✅ **Creado esta sesión** |
| 6 | P-PSEA-10 — Manejo de Ítems PT | ✅ **Creado esta sesión** |
| 7 | P-PSEA-02–05 — Verificar coherencia con rondas | ⬜ Pendiente (revisión, no creación) |
| 8 | Paquete pre-ronda real para envío | 🔴 **URGENTE** (antes del 13 abr) |

---

## Critical Technical Context

- **Patrón de skeletons I-PSEA:** `Objeto → Alcance → Referencias → Definiciones → Responsabilidades → Procedimiento (con > **Instrucción:**) → Criterios de aceptación → Registros → Diagrama Mermaid → Control de versiones`

- **Patrón de skeletons P-PSEA:** igual estructura pero con enfoque de gobierno/política, no ejecución técnica paso a paso.

- **I-PSEA-09 ↔ P-PSEA-20:** I-PSEA-09 es la ejecución técnica de §6.3 de P-PSEA-20. Son complementarios.

- **P-PSEA-10 adaptación clave:** CALAIRE-EA es esquema in situ. El "ítem PT" es la atmósfera generada en el manifold. No hay envío físico. Los cilindros de los participantes son sus propios materiales de calibración, no el ítem PT.

- **Fuente usada para I-PSEA-09:** `docs/docs_sgc/comunicacion_2_participantes.md` — segunda comunicación oficial, auditada contra ISO 17043 (`docs/instrucciones/compliance_comunicacion.md`). Los 13 elementos de §6.2 de I-PSEA-09 mapean esa auditoría.

- **3 brechas pendientes en las instrucciones a participantes** (I-PSEA-09 §6.3):
  1. σ_pt por analito (tabla vacía con [___])
  2. Proceso de apelaciones (párrafo a agregar)
  3. Normativa transporte cilindros peligrosos

- **Campos pendientes en los skeletons** (requieren datos reales del laboratorio):
  - Parámetros del CRM: proveedor, lote, concentración certificada, u_CRM (→ I-PSEA-08, P-PSEA-10 §6.1)
  - Valores σ_pt por analito (→ I-PSEA-07, I-PSEA-09 §6.3 Brecha 1)
  - Presión mínima de cilindro y tolerancia concentración (→ P-PSEA-10 §6.1 y §6.4)
  - Datos de contacto del coordinador: correo y teléfono de Wilson y Carmen (→ P-PSEA-20 §6.5)

---

## Next Steps

1. **URGENTE (antes del 13 abr):** Preparar paquete pre-ronda real — rellenar campos `[___]` en `comunicacion_2_participantes.md` y F-PSEA-05A con fechas, coordinador, σ_pt — y enviar a SIATA (P1) y UPB (P2)
2. **Sprint 3:** Formatos de ejecución: F-PSEA-06 (Plan de Ronda), F-PSEA-05 (Confirmación), F-PSEA-07 (Lista Participantes), F-PSEA-08 (Preparación Ítem), F-PSEA-09 (Homogeneidad), F-PSEA-10 (Estabilidad), F-PSEA-11 (Envío/Recepción), F-PSEA-12 (Reporte Participante), F-PSEA-13 (Revisión Datos), F-PSEA-14 (Hoja Cálculo)
3. **Pendiente revisión:** P-PSEA-02–05 coherencia con rondas piloto
4. **Pendiente (ver plan anterior):** Resolver duplicado P-PSEA-09 (2 versiones .docx en `docs/docs_sgc/202510 Documentacion SGC/`)
