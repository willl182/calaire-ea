# Fichas Resumen del SGC PEA

**Estado:** revision de calidad e integracion  
**Fecha:** 2026-06-13  
**Proposito:** capa de fichas resumen que estabiliza el perfil de cada elemento documental del PEA antes de su elaboracion completa.

---

## Estructura de este directorio

| Archivo | Proposito |
|---|---|
| `README.md` | Este archivo. Indice y guia de navegacion. |
| `00_inventario_maestro_fichas.md` | Matriz maestra del universo de fichas (55 codigos documentales + 3 subformatos adicionales). Define estado, prioridad, clase y fase. |
| `00_plantilla_ficha_resumen.md` | Plantilla base para redactar cada ficha. Todos los subagentes deben usarla. |
| `asignacion_subagente_A.md` | Arquitectura documental: matrices, flujo de datos y aplicativos. |
| `asignacion_subagente_B.md` | Flujo digital y formatos criticos: instructivos `pt_app` y formatos de datos. |
| `asignacion_subagente_C.md` | Procedimientos transversales tecnicos: nucleo estadistico, informe, planificacion e item. |
| `asignacion_subagente_D.md` | Formatos operativos activos: planificacion, participantes, item, datos y H/E. |
| `asignacion_subagente_E.md` | Gestion operativa PEA: quejas, apelaciones, TNC/NC/CAPA y controles. |
| `asignacion_subagente_F.md` | Procedimientos por analito: NO/NO2, CO, O3, SO2. |
| `asignacion_subagente_G.md` | Control de no activos y cierre: documentos retirados, reservados, absorbidos y diferidos. |
| `ficha_*.md` | Fichas resumen individuales producidas por los subagentes. |

---

## Como trabajar

1. Leer el `00_inventario_maestro_fichas.md` para entender el universo completo.
2. Leer la `asignacion_subagente_*.md` correspondiente.
3. Usar `00_plantilla_ficha_resumen.md` como base para cada ficha.
4. Guardar cada ficha como `ficha_[CODIGO].md` en este mismo directorio.
5. Respetar las reglas de redaccion y el checklist de calidad de la plantilla.

---

## Referencias base del proyecto

- `docs/documentacion_sgc/mapa_tentativo_sgc_pea.md` — Vista rapida del sistema documental.
- `docs/documentacion_sgc/mapa_decisiones_documentales_pea.md` — Decisiones firmes por codigo.
- `docs/documentacion_sgc/sesion_grill_sgc_pea_v1.md` — Restricciones y flujo de datos acordado.
- `logs/plans/260613_1431_plan_fichas-resumen-sgc-pea.md` — Plan maestro de elaboracion.

---

## Progreso

| Fase | Estado | Documentos |
|---|---|---|
| Fase 1: Inventario maestro | Completado | `00_inventario_maestro_fichas.md` |
| Fase 2: Plantilla base | Completado | `00_plantilla_ficha_resumen.md` |
| Fase 3: Arquitectura documental | Completado | `P-PSEA-12`, `P-PSEA-13`, `P-PSEA-23`, `DG-PSEA-02`, `DG-PSEA-03` |
| Fase 4: Flujo digital y formatos criticos | Completado | `I-PSEA-10`, `I-PSEA-16`, `I-PSEA-17`, `I-PSEA-18`, `F-PSEA-07`, `F-PSEA-10`, `F-PSEA-13A-D`, `F-PSEA-14` |
| Fase 5: Procedimientos transversales | Completado | `P-PSEA-06`, `P-PSEA-07`, `P-PSEA-09`, `P-PSEA-10`, `F-PSEA-04` |
| Fase 6: Formatos operativos activos | Completado | `F-PSEA-01`, `F-PSEA-02`, `F-PSEA-05`, `F-PSEA-05A`, `F-PSEA-06`, `F-PSEA-08`, `F-PSEA-09`, `F-PSEA-12`, `F-PSEA-13` |
| Fase 7: Gestion operativa | Completado | `P-PSEA-08`, `P-PSEA-16`, `P-PSEA-20`, `P-PSEA-21`, `P-PSEA-24`, `P-PSEA-25`, `P-PSEA-26`, `P-PSEA-27`, `P-PSEA-28`, `F-PSEA-16`, `F-PSEA-17`, `F-PSEA-21`, `F-PSEA-23` |
| Fase 8: Procedimientos por analito | Completado | `P-PSEA-02`, `P-PSEA-03`, `P-PSEA-04`, `P-PSEA-05` |
| Fase 9: No activos y cierre | Completado | `DG-PSEA-01`, `P-PSEA-01`, `P-PSEA-11`, `P-PSEA-14`, `P-PSEA-15`, `P-PSEA-17`, `P-PSEA-18`, `P-PSEA-19`, `P-PSEA-22`, `F-PSEA-03`, `F-PSEA-11` |
| Fase 10: Revision de calidad | En revision | Auditoria de consistencia e integracion (`revision b`) |
