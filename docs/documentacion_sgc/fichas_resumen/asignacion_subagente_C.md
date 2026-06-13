# Asignacion de Subagente C: Procedimientos Transversales Tecnicos

**Subagente:** C  
**Paquete de trabajo:** Nucleo tecnico-operativo  
**Documentos asignados:** `P-PSEA-06`, `P-PSEA-07`, `P-PSEA-09`, `P-PSEA-10`, `F-PSEA-04`  
**Fase del plan:** Fase 5

---

## Objetivo

Fichar los procedimientos transversales que deben ser citados por los documentos especificos por gas. Estos son el nucleo tecnico-operativo del PEA y deben quedar listos para ser citados sin duplicacion.

---

## Documentos a fichar

### `P-PSEA-06` — Diseno estadistico
- **Tipo:** Procedimiento
- **Clase:** Ficha activa
- **Prioridad:** Alta
- **Proposito:** Procedimiento tecnico central para valor asignado, `sigma_pt`, incertidumbre, outliers, desempeno, reglas de decision e integracion de H/E.
- **Riesgo clave:** No es instructivo de `pt_app`. `I-PSEA-17` e `I-PSEA-18` explican uso operativo; `P-PSEA-06` define criterio tecnico.
- **Relacion critica:** `F-PSEA-13`, `F-PSEA-13A-D`, `F-PSEA-14`, `F-PSEA-04`.
- **Llamado desde:** `P-PSEA-02` a `P-PSEA-05` (procedimientos por analito).

### `P-PSEA-07` — Generacion/emision del informe de resultados
- **Tipo:** Procedimiento
- **Clase:** Ficha preliminar
- **Prioridad:** Alta
- **Proposito:** Gobierna la generacion y emision del informe final desde `pt_app`. Absorbe el rol de `P-PSEA-22`.
- **Riesgo clave:** No desarrollar contenido detallado de `F-PSEA-04` (informe final). Mantener preliminar.
- **Relacion critica:** `F-PSEA-04`, `F-PSEA-14`, resultados H/E cuando apliquen.
- **Nota:** `F-PSEA-04` es formato preliminar; no definir aun su contenido.

### `P-PSEA-09` — Planificacion de ronda EA
- **Tipo:** Procedimiento
- **Clase:** Ficha activa
- **Prioridad:** Alta
- **Proposito:** Procedimiento transversal para planificar la ronda usando `calaire-app` y formatos exportables.
- **Riesgo clave:** Debe incluir o referenciar la matriz/nota A-U de ISO/IEC 17043:2023 7.2.1.3.
- **Relacion critica:** `F-PSEA-01`, `F-PSEA-02`, `F-PSEA-06`, `F-PSEA-07`, `F-PSEA-08`, `DG-PSEA-02`.

### `P-PSEA-10` — Preparacion y control del item de ensayo gaseoso
- **Tipo:** Procedimiento
- **Clase:** Ficha activa
- **Prioridad:** Alta
- **Proposito:** Generar concentraciones con calibrador dinamico y cilindro, tomando niveles definidos en la ronda.
- **Riesgo clave:** No trata envio fisico de items. El antiguo enfoque de envio/recepcion no aplica.
- **Relacion critica:** `F-PSEA-07`, `F-PSEA-08`, `F-PSEA-13`, `F-PSEA-13A-D`.
- **Nota:** `F-PSEA-06` debe indicar que H/E se documenta en `F-PSEA-13`.

### `F-PSEA-04` — Informe final de resultados
- **Tipo:** Formato
- **Clase:** Ficha preliminar
- **Prioridad:** Media-alta
- **Proposito:** Informe final generado desde `pt_app`.
- **Riesgo clave:** No definir contenido detallado aun. Mantener ficha preliminar con restriccion expresa.
- **Relacion critica:** `P-PSEA-07`, `P-PSEA-06`, `P-PSEA-20`, `P-PSEA-21`.

---

## Reglas especificas para este paquete

1. **No duplicar en procedimientos por gas:** `P-PSEA-02` a `P-PSEA-05` deben citar estos documentos, no replicarlos.
2. **Preliminaridad de `F-PSEA-04`:** La ficha debe indicar expresamente que el contenido del informe no se define en esta fase.
3. **H/E si aplica:** `P-PSEA-10` conecta con H/E; no afirmar que H/E no aplica.
4. **`P-PSEA-07` absorbe `P-PSEA-22`:** Indicar que `P-PSEA-22` ya no existe como documento independiente.

---

## Entregables

- `ficha_P-PSEA-06.md`
- `ficha_P-PSEA-07.md`
- `ficha_P-PSEA-09.md`
- `ficha_P-PSEA-10.md`
- `ficha_F-PSEA-04.md`

**Ubicacion:** `docs/documentacion_sgc/fichas_resumen/`

---

## Referencias obligatorias

- `00_plantilla_ficha_resumen.md`
- `00_inventario_maestro_fichas.md`
- `docs/documentacion_sgc/mapa_tentativo_sgc_pea.md`
- `docs/documentacion_sgc/mapa_decisiones_documentales_pea.md`
- `docs/documentacion_sgc/sesion_grill_sgc_pea_v1.md`
