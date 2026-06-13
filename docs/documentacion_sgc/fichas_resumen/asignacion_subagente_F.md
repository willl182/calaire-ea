# Asignacion de Subagente F: Procedimientos por Analito

**Subagente:** F  
**Paquete de trabajo:** Fichas especificas por gas  
**Documentos asignados:** `P-PSEA-02`, `P-PSEA-03`, `P-PSEA-04`, `P-PSEA-05`  
**Fase del plan:** Fase 8

---

## Objetivo

Fichar los procedimientos tecnicos por gas despues de estabilizar los documentos transversales. Cada ficha debe indicar que el procedimiento por analito debe citar documentos transversales y no duplicar estadistica, H/E, informe ni flujo de datos.

---

## Documentos a fichar

### `P-PSEA-02` — Procedimiento tecnico NO/NO2
- **Tipo:** Procedimiento
- **Clase:** Ficha activa
- **Prioridad:** Media
- **Proposito:** Condiciones tecnicas propias de NO/NO2.
- **Riesgo clave:** No duplicar contenido de `P-PSEA-06`, `P-PSEA-07`, `P-PSEA-23`, `F-PSEA-13` ni `F-PSEA-14`.
- **Relaciones de cita obligatoria:**
  - `P-PSEA-06`: diseno estadistico, valor asignado, `sigma_pt`, incertidumbre, outliers, desempeno.
  - `F-PSEA-13`, `F-PSEA-13A-D`: homogeneidad y estabilidad.
  - `P-PSEA-07`: informe de resultados.
  - `P-PSEA-23`: flujo tecnico de datos.
  - `DG-PSEA-03`, `I-PSEA-17`, `I-PSEA-18`: `pt_app`.

### `P-PSEA-03` — Procedimiento tecnico CO
- **Tipo:** Procedimiento
- **Clase:** Ficha activa
- **Prioridad:** Media
- **Proposito:** Condiciones tecnicas propias de CO.
- **Riesgo clave:** No duplicar contenido transversal.
- **Relaciones de cita obligatoria:** Mismas que `P-PSEA-02`.

### `P-PSEA-04` — Procedimiento tecnico O3
- **Tipo:** Procedimiento
- **Clase:** Ficha activa
- **Prioridad:** Media
- **Proposito:** Condiciones tecnicas propias de O3.
- **Riesgo clave:** Corregir referencias antiguas y duplicaciones.
- **Relaciones de cita obligatoria:** Mismas que `P-PSEA-02`.

### `P-PSEA-05` — Procedimiento tecnico SO2
- **Tipo:** Procedimiento
- **Clase:** Ficha activa
- **Prioridad:** Media
- **Proposito:** Condiciones tecnicas propias de SO2.
- **Riesgo clave:** No duplicar contenido transversal.
- **Relaciones de cita obligatoria:** Mismas que `P-PSEA-02`.

---

## Reglas especificas para este paquete

1. **Aligerar:** Cada procedimiento por analito debe conservar solo condiciones y decisiones propias del gas.
2. **Citar, no duplicar:** Todo lo que sea estadistica, H/E, informe, flujo de datos o uso de aplicativo se cita, no se redefine.
3. **Referencia unica:** Si un criterio tecnico aparece en `P-PSEA-06`, no debe aparecer en `P-PSEA-02` a `P-PSEA-05`.
4. **Formatos relacionados:** `F-PSEA-08`, `F-PSEA-13`, `F-PSEA-13A-D`, `F-PSEA-14`, `F-PSEA-04`.

---

## Entregables

- `ficha_P-PSEA-02.md`
- `ficha_P-PSEA-03.md`
- `ficha_P-PSEA-04.md`
- `ficha_P-PSEA-05.md`

**Ubicacion:** `docs/documentacion_sgc/fichas_resumen/`

---

## Referencias obligatorias

- `00_plantilla_ficha_resumen.md`
- `00_inventario_maestro_fichas.md`
- `docs/documentacion_sgc/mapa_tentativo_sgc_pea.md`
- `docs/documentacion_sgc/mapa_decisiones_documentales_pea.md`
- `docs/documentacion_sgc/sesion_grill_sgc_pea_v1.md`
