# Asignacion de Subagente F: Procedimientos por Analito

**Subagente:** F  
**Paquete de trabajo:** Fichas especificas por gas  
**Documentos asignados:** `P-PSEA-10`, `P-PSEA-11`, `P-PSEA-12`, `P-PSEA-13`  
**Fase del plan:** Fase 8

---

## Objetivo

Fichar los procedimientos tecnicos por gas despues de estabilizar los documentos transversales. Cada ficha debe indicar que el procedimiento por analito debe citar documentos transversales y no duplicar estadistica, H/E, informe ni flujo de datos.

---

## Documentos a fichar

### `P-PSEA-10` — Procedimiento tecnico NO/NO2
- **Tipo:** Procedimiento
- **Clase:** Ficha activa
- **Prioridad:** Media
- **Proposito:** Condiciones tecnicas propias de NO/NO2.
- **Riesgo clave:** No duplicar contenido de `P-PSEA-07`, `P-PSEA-09`, `P-PSEA-08`, `F-PSEA-11` ni `F-PSEA-12`.
- **Relaciones de cita obligatoria:**
  - `P-PSEA-07`: diseno estadistico, valor asignado, `sigma_pt`, incertidumbre, outliers, desempeno.
  - `F-PSEA-11`, `F-PSEA-11A-D`: homogeneidad y estabilidad.
  - `P-PSEA-09`: informe de resultados.
  - `P-PSEA-08`: flujo tecnico de datos.
  - `DG-PSEA-03`, `I-PSEA-04`, `I-PSEA-05`: `pt_app`.

### `P-PSEA-11` — Procedimiento tecnico CO
- **Tipo:** Procedimiento
- **Clase:** Ficha activa
- **Prioridad:** Media
- **Proposito:** Condiciones tecnicas propias de CO.
- **Riesgo clave:** No duplicar contenido transversal.
- **Relaciones de cita obligatoria:** Mismas que `P-PSEA-10`.

### `P-PSEA-12` — Procedimiento tecnico O3
- **Tipo:** Procedimiento
- **Clase:** Ficha activa
- **Prioridad:** Media
- **Proposito:** Condiciones tecnicas propias de O3.
- **Riesgo clave:** Corregir referencias antiguas y duplicaciones.
- **Relaciones de cita obligatoria:** Mismas que `P-PSEA-10`.

### `P-PSEA-13` — Procedimiento tecnico SO2
- **Tipo:** Procedimiento
- **Clase:** Ficha activa
- **Prioridad:** Media
- **Proposito:** Condiciones tecnicas propias de SO2.
- **Riesgo clave:** No duplicar contenido transversal.
- **Relaciones de cita obligatoria:** Mismas que `P-PSEA-10`.

---

## Reglas especificas para este paquete

1. **Aligerar:** Cada procedimiento por analito debe conservar solo condiciones y decisiones propias del gas.
2. **Citar, no duplicar:** Todo lo que sea estadistica, H/E, informe, flujo de datos o uso de aplicativo se cita, no se redefine.
3. **Referencia unica:** Si un criterio tecnico aparece en `P-PSEA-07`, no debe aparecer en `P-PSEA-10` a `P-PSEA-13`.
4. **Formatos relacionados:** `F-PSEA-07`, `F-PSEA-11`, `F-PSEA-11A-D`, `F-PSEA-12`, `F-PSEA-13`.

---

## Entregables

- `ficha_P-PSEA-10.md`
- `ficha_P-PSEA-11.md`
- `ficha_P-PSEA-12.md`
- `ficha_P-PSEA-13.md`

**Ubicacion:** `docs/documentacion_sgc/fichas_resumen/`

---

## Referencias obligatorias

- `00_plantilla_ficha_resumen.md`
- `00_inventario_maestro_fichas.md`
- `docs/documentacion_sgc/mapa_tentativo_sgc_pea.md`
- `docs/documentacion_sgc/mapa_decisiones_documentales_pea.md`
- `docs/documentacion_sgc/sesion_grill_sgc_pea_v1.md`
