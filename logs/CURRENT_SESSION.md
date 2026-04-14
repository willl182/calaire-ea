# Session State: CALAIRE-EA — SGC / Prueba Piloto

**Last Updated**: 2026-04-10 11:45

---

## Session Objective

Cerrar brechas documentales críticas detectadas en la evaluación de `F-PSEA-06 Plan de Ronda EA` y dejar el paquete `I-PSEA-07` / `I-PSEA-09` / `F-PSEA-06` en estado aprobable antes de la ejecución de la ronda simple.

---

## Current State

- [x] Sprint 2 completado (sesión anterior): I-PSEA-09, P-PSEA-20, P-PSEA-10 — skeletons completos
- [x] **σ_pt resuelto conceptualmente:** enfoque post-ronda adoptado (σ_pt = a·x_pt + b, parámetros EPA, publicado solo en informe final)
- [x] `comunicacion_2_participantes.md` — nota sobre σ_pt post-ronda agregada en §8
- [x] `I-PSEA-09 §6.3 Brecha 1` — reescrita con Opción A (tabla fija) + Opción B (fórmula lineal); piloto usa Opción B
- [x] Logseq actualizado: Wilson Salas (móvil + email), David Pulgarín (móvil + email), SIATA (Mauricio Ramírez), UPB (Daniel Esteban Villada)
- [x] `comunicacion_3_siata.md` — lista para enviar a mauricio.ramirez@siata.gov.co
- [x] `comunicacion_3_upb.md` — lista para enviar a danielesteban.villada@upb.edu.co
- [x] `F-PSEA-05A` — encabezado completado (fecha límite 14/04/2026, correo calaire_med@unal.edu.co, coordinador Wilson)
- [x] `gantt_b.md` — mantenido con `excludes weekends` (decisión del usuario)
- [x] `F-PSEA-06 ronda simple` — Fases 2, 3 y 4 del ajuste implementadas (formato operativo completo)
- [x] **plan_oc_gpt53.md — Fase 4 completada:** dictamen `no_aprobable` emitido por brechas D3-01 (`sigma_pt`) y D3-02 (hito T-3); backlog C4-01 a C4-04 formalizado — `logs/history/260410_1134_findings.md`
- [x] **plan_oc_gpt53.md — Fase 6 completada:** informe ejecutivo emitido y dictamen `no_aprobable` ratificado hasta cierre verificable de C4-01 a C4-04 — `logs/history/260410_1144_findings.md`
- [x] **plan_pi_gpt53.md — Fase 5 completada:** informe de auditoría previa emitido; línea base pre-corrección consolidada (0 Blocking, 1 Required, 1 Suggestion) — `logs/history/260410_1143_findings.md`
- [x] **plan_gpt53.md — Fase 5 completada:** informe de auditoría previa a correcciones emitido; línea base auditada del dictamen `aprobable_con_ajustes` consolidada — `logs/history/260410_1145_findings.md`
- [x] **plan_sonnt46.md — Fase A completada:** 7/7 verificaciones estructurales CUMPLEN — `logs/history/260410_1124_findings.md`
- [ ] plan_sonnt46.md — Fase B pendiente (21 verificaciones de contenido, puntos a–u)
- [ ] plan_sonnt46.md — Fases C, D, E pendientes

---

## Estructura de rondas del piloto (CONFIRMADO — Propuesta A)

| | **Ronda Simple** | **Ronda Compleja F1** | **Ronda Compleja F2** |
|---|---|---|---|
| **Analitos** | CO, SO₂ | O₃, NO, NO₂ | CO, SO₂ |
| **Participantes** | P1 = SIATA | P1 + P2 = SIATA + UPB | P2 = UPB |
| **Instalación** | Mié 22 abr | Mié 29 abr | (cierre sem. 2) |
| **Medición** | Jue 23 abr | Jue 30 abr · Vie 1 may* · Sáb 2 may | Sáb 2 may |
| **Devolución** | Vie 24 abr | Sáb 2 may | Sáb 2 may |

*1 de mayo = festivo, usado como día de medición.

---

## Contactos confirmados

| Participante | Código | Contacto | Email |
|---|---|---|---|
| SIATA | P1 | Mauricio Ramírez | mauricio.ramirez@siata.gov.co |
| UPB | P2 | Daniel Esteban Villada | danielesteban.villada@upb.edu.co |
| CALAIRE-EA (técnico) | — | Wilson Salas | wilsonsalasc@gmail.com · (+57) 318 476 7422 |
| CALAIRE-EA (proyectos) | — | David Pulgarín | calaire_med@unal.edu.co · (+57) 314 874 8191 |

---

## σ_pt — Decisión de diseño

- **Enfoque adoptado:** Opción B — post-ronda, fórmula σ_pt = a·x_pt + b con parámetros US EPA
- **No se comunica a participantes** antes de la ronda (confirmado revisando ERLAP/Barbiere)
- **Parámetros EPA (a, b) por analito:** pendientes de suministro por Wilson → van a I-PSEA-07
- **Documentado en:** `comunicacion_2_participantes.md §8` (nota) + `I-PSEA-09 §6.3 Brecha 1` (Opción A/B)

---

## Critical Technical Context

- **Deadline Com. 3:** F-PSEA-05A debe devolverse antes del **martes 14 de abril** (trámite permiso ingreso a la U)
- **Propuesta A seleccionada** para la prueba piloto (Ronda Simple sem 20 abr → Ronda Compleja sem 27 abr)
- **Dictamen vigente F-PSEA-06:** `no_aprobable` hasta cerrar armonización de `sigma_pt` y completar control T-3 en cronograma pre-ronda
- **Congelamiento de `plan_gpt53.md`:** no ejecutar correcciones adicionales sobre la línea base auditada de `F-PSEA-06` hasta aceptar `logs/history/260410_1145_findings.md`
- **F-PSEA-05 (Confirmación de Participación):** placeholder sin contenido — se decidió que sobra; la confirmación va en F-PSEA-05A §5
- **plan_sonnt46.md:** Fase A cerrada (7/7 ✅); continuar con Fase B (21 puntos a–u del documento de planificación)

---

## Next Steps

1. **Iniciar corrección controlada post-auditoría (`plan_pi_gpt53.md`):** ejecutar cierre trazable del hallazgo `Required` por alineación de `sigma_pt` en `I-PSEA-07`, `I-PSEA-09` y `F-PSEA-06`.
2. **Cerrar C4-01 (alta, fecha objetivo 12 abr):** armonizar criterio oficial de `sigma_pt` en `I-PSEA-07`, `I-PSEA-09` y `F-PSEA-06`.
3. **Cerrar C4-02 (media, fecha objetivo 12 abr):** incorporar hito T-3 en sección 8 de `F-PSEA-06` con responsable y evidencia.
4. **Cerrar C4-03 (media, fecha objetivo 15 abr):** completar parámetros por analito y campos críticos pendientes en `I-PSEA-07`.
5. **Cerrar C4-04 (media, fecha objetivo 15 abr):** formalizar matriz de diligenciamiento de placeholders en `F-PSEA-06`.
6. **URGENTE (antes del 13 abr):** Enviar `comunicacion_3_siata.md` y `comunicacion_3_upb.md` con adjuntos: F-PSEA-05A + F-PSEA-01 + F-PSEA-02.
7. **Continuar plan_sonnt46.md — Fase B:** 21 verificaciones de contenido (puntos a–u).
8. **Continuar plan_sonnt46.md — Fases C, D, E** tras completar B.
9. **Brechas pendientes en I-PSEA-09 §6.3:**
   - Brecha 2 — Apelaciones: párrafo a agregar en comunicación oficial
   - Brecha 3 — Transporte cilindros: nota a agregar en §6 de la comunicación
10. **Aceptar o descartar formalmente el dictamen de `plan_gpt53.md`:** usar `logs/history/260410_1145_findings.md` como referencia antes de cualquier intervención derivada de ese plan.
11. **Sprint 3:** Formatos de ejecución (F-PSEA-06 a F-PSEA-14).
12. **Pendiente en F-PSEA-06:** diligenciar datos reales (código de ronda, responsables, CRM/lotes, setpoints, `x_pt`, `u(x_pt)`, `sigma_pt`) solo tras resolver el conflicto entre dictámenes activos.
13. **Pendiente revisión:** Coherencia P-PSEA-02–05 con rondas piloto.
