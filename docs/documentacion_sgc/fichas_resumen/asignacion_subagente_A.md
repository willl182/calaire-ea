# Asignacion de Subagente A: Arquitectura Documental

**Subagente:** A  
**Paquete de trabajo:** Fichas base y matrices  
**Documentos asignados:** `P-PSEA-02`, `P-PSEA-03`, `P-PSEA-08`, `DG-PSEA-02`, `DG-PSEA-03`  
**Fase del plan:** Fase 3

---

## Objetivo

Estabilizar primero las fichas que gobiernan el mapa documental y el flujo digital del PEA. Estas fichas son la base sobre la cual se construyen todas las demas. Deben quedar claras y sin ambiguedad antes de que otros subagentes inicien sus paquetes.

---

## Documentos a fichar

### 1. `P-PSEA-02` — Matriz documental del PEA
- **Tipo:** Procedimiento / Matriz
- **Clase:** Ficha activa
- **Prioridad:** Alta
- **Proposito:** Lista todo lo numerado del PEA (`DG`, `P`, `I`, `F` y subformatos) con estado y relacion documental.
- **Riesgo clave:** No debe tratar aprobacion, retencion, obsolescencia ni control documental macro.
- **Relacion critica:** `P-PSEA-03` (matriz de evidencias), `P-PSEA-08` (flujo de datos).

### 2. `P-PSEA-03` — Matriz de registros y evidencias del PEA
- **Tipo:** Procedimiento / Matriz
- **Clase:** Ficha activa
- **Prioridad:** Alta
- **Proposito:** Lista registros generados por ronda o evento, no procedimientos ni instructivos.
- **Riesgo clave:** No listar archivos tecnicos internos del preprocesador como registros oficiales.
- **Relacion critica:** `P-PSEA-02`, todos los `F-PSEA` vigentes.

### 3. `P-PSEA-08` — Flujo tecnico de datos digitales del PEA
- **Tipo:** Procedimiento
- **Clase:** Ficha activa
- **Prioridad:** Alta
- **Proposito:** Mapea aplicaciones, archivos tecnicos internos, formatos oficiales y salidas de analisis.
- **Riesgo clave:** Los archivos tecnicos internos se mapean aqui, no se convierten en `F-PSEA`.
- **Relacion critica:** `DG-PSEA-02`, `DG-PSEA-03`, `I-PSEA-04`, `I-PSEA-05`, `F-PSEA-08`, `F-PSEA-10`, `F-PSEA-09`, `F-PSEA-11A-D`, `F-PSEA-12`, `F-PSEA-13`.

### 4. `DG-PSEA-02` — Aplicativo `calaire-app`
- **Tipo:** Documento general
- **Clase:** Ficha activa
- **Prioridad:** Alta
- **Proposito:** Documento general del aplicativo de gestion de rondas, participantes, captura/exportacion de datos y casos de quejas.
- **Riesgo clave:** No es un formato `F-PSEA`; no confundir con `F-PSEA-06`, `F-PSEA-09` o `F-PSEA-08`.
- **Relacion critica:** `I-PSEA-02`, `I-PSEA-03`, todos los formatos de `calaire-app`.

### 5. `DG-PSEA-03` — Aplicativo `pt_app`
- **Tipo:** Documento general
- **Clase:** Ficha activa
- **Prioridad:** Alta
- **Proposito:** Documento general del aplicativo de preprocesamiento, analisis estadistico, H/E e informe final.
- **Riesgo clave:** No es un formato `F-PSEA`; no confundir con `F-PSEA-10` ni `F-PSEA-12`.
- **Relacion critica:** `I-PSEA-04`, `I-PSEA-05`, `F-PSEA-10`, `F-PSEA-11A-D`, `F-PSEA-12`, `F-PSEA-13`.

---

## Reglas especificas para este paquete

1. **Diferencia clave:** `P-PSEA-02` lista documentos; `P-PSEA-03` lista evidencias/registros; `P-PSEA-08` mapea flujo de datos.
2. **Los aplicativos son documentos generales:** `DG-PSEA-02` y `DG-PSEA-03` no se confunden con formatos, instructivos ni procedimientos.
3. **Archivos tecnicos internos:** Listar en `P-PSEA-08` solo como insumos, no como formatos oficiales.
4. **No tocar:** `sgc_res.md`, `README.md`, `P-PSEA-01`.

---

## Entregables

- `ficha_P-PSEA-02.md`
- `ficha_P-PSEA-03.md`
- `ficha_P-PSEA-08.md`
- `ficha_DG-PSEA-02.md`
- `ficha_DG-PSEA-03.md`

**Ubicacion:** `docs/documentacion_sgc/fichas_resumen/`

---

## Referencias obligatorias

- `00_plantilla_ficha_resumen.md` — usar como base.
- `00_inventario_maestro_fichas.md` — verificar estados y prioridades.
- `docs/documentacion_sgc/mapa_tentativo_sgc_pea.md` — verificar relaciones documentales.
- `docs/documentacion_sgc/mapa_decisiones_documentales_pea.md` — verificar decisiones firmes.
- `docs/documentacion_sgc/sesion_grill_sgc_pea_v1.md` — verificar restricciones y flujo de datos.
