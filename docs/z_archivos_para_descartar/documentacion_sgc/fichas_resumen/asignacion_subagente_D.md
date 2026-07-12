# Asignacion de Subagente D: Formatos Operativos Activos

**Subagente:** D  
**Paquete de trabajo:** Planificacion, participantes, item y H/E  
**Documentos asignados:** `F-PSEA-01`, `F-PSEA-02`, `F-PSEA-03`, `F-PSEA-04`, `F-PSEA-05`, `F-PSEA-07`, `F-PSEA-08`, `F-PSEA-09`, `F-PSEA-11`  
**Fase del plan:** Fase 6

---

## Objetivo

Fichar los registros y formatos operativos activos que soportan planificacion, participantes, datos, H/E e informe. Cada formato activo debe indicar origen, responsable funcional, procedimiento relacionado, salida esperada y aplicativo asociado.

---

## Documentos a fichar

### Planificacion

#### `F-PSEA-01` — Calendario global de ronda
- **Tipo:** Formato / Registro
- **Clase:** Ficha activa
- **Prioridad:** Media
- **Proposito:** Calendario general desde inicio de ronda hasta entrega de informe final; exportable desde `calaire-app` y util para Gantt/Mermaid.
- **Relacion critica:** `P-PSEA-04`, `F-PSEA-05`.

#### `F-PSEA-02` — Cronograma detallado de ronda
- **Tipo:** Formato / Registro
- **Clase:** Ficha activa
- **Prioridad:** Media
- **Proposito:** Cronograma diligenciable/exportable de actividades detalladas de ronda.
- **Relacion critica:** `P-PSEA-04`, `F-PSEA-05`.

### Participantes

#### `F-PSEA-03` — Registro de participacion
- **Tipo:** Formato / Registro
- **Clase:** Ficha activa
- **Prioridad:** Media
- **Proposito:** Registro de participacion del laboratorio/participante.
- **Relacion critica:** `P-PSEA-04`, `P-PSEA-05`.

#### `F-PSEA-04` — Anexo tecnico de equipos e instrumentos
- **Tipo:** Formato / Registro
- **Clase:** Ficha activa
- **Prioridad:** Media
- **Proposito:** Datos de equipos e instrumentos del participante; equivalente a `ronda_1_equipos.csv`.
- **Riesgo clave:** Alimenta `pt_app`; no confundir con `F-PSEA-08`.
- **Relacion critica:** `P-PSEA-08`, `P-PSEA-07`.

### Item y ronda

#### `F-PSEA-05` — Plan de ronda EA
- **Tipo:** Formato / Registro
- **Clase:** Ficha activa
- **Prioridad:** Media-alta
- **Proposito:** Plan tecnico-operativo de la ronda. Indica que H/E se documenta en `F-PSEA-11`.
- **Riesgo clave:** Debe integrar `F-PSEA-01`, `F-PSEA-02`, `F-PSEA-06` y nota/matriz A-U.
- **Relacion critica:** `P-PSEA-04`, `P-PSEA-14`, `P-PSEA-06`, `P-PSEA-16`.

#### `F-PSEA-07` — Preparacion y control del item
- **Tipo:** Formato / Registro
- **Clase:** Ficha activa
- **Prioridad:** Media
- **Proposito:** Dossier/registro de preparacion y control del item gaseoso.
- **Relacion critica:** `P-PSEA-06`, `P-PSEA-10` a `P-PSEA-13`, `P-PSEA-04`.

### Datos y exportaciones

#### `F-PSEA-08` — Datos reportados por participante
- **Tipo:** Formato / Registro
- **Clase:** Ficha activa
- **Prioridad:** Media
- **Proposito:** Registro diligenciado por el participante en `calaire-app`.
- **Relacion critica:** `P-PSEA-05`, `P-PSEA-08`, `P-PSEA-19`.

#### `F-PSEA-09` — Datos de participantes exportados para analisis PT
- **Tipo:** Formato / Exportacion
- **Clase:** Ficha activa
- **Prioridad:** Alta
- **Proposito:** Exportacion oficial desde `calaire-app` hacia `pt_app`.
- **Riesgo clave:** No es `ronda_<n>_completa.csv`. Ese es `F-PSEA-12`.
- **Relacion critica:** `P-PSEA-08`, `P-PSEA-19`.

### H/E

#### `F-PSEA-11` — Homogeneidad y estabilidad del item
- **Tipo:** Formato / Registro
- **Clase:** Ficha activa
- **Prioridad:** Alta
- **Proposito:** Registro principal de H/E del item de ensayo.
- **Relacion critica:** `P-PSEA-07`, `P-PSEA-06`, `P-PSEA-08`.
- **Subformatos:** `F-PSEA-11A` a `F-PSEA-11D`.

---

## Reglas especificas para este paquete

1. **`F-PSEA-05` integra:** `F-PSEA-01`, `F-PSEA-02`, `F-PSEA-06` y nota A-U.
2. **`F-PSEA-09` vs `F-PSEA-12`:** `F-PSEA-09` es la exportacion bruta desde `calaire-app`; `F-PSEA-12` es el dataset consolidado oficial.
3. **`F-PSEA-04` alimenta `pt_app`:** Es equivalente a `ronda_1_equipos.csv`.
4. **`F-PSEA-11` es el registro principal H/E:** Los subformatos `F-PSEA-11A-D` detallan fases especificas.

---

## Entregables

- `ficha_F-PSEA-01.md`
- `ficha_F-PSEA-02.md`
- `ficha_F-PSEA-03.md`
- `ficha_F-PSEA-04.md`
- `ficha_F-PSEA-05.md`
- `ficha_F-PSEA-07.md`
- `ficha_F-PSEA-08.md`
- `ficha_F-PSEA-09.md`
- `ficha_F-PSEA-11.md`

**Ubicacion:** `docs/documentacion_sgc/fichas_resumen/`

---

## Referencias obligatorias

- `00_plantilla_ficha_resumen.md`
- `00_inventario_maestro_fichas.md`
- `docs/documentacion_sgc/mapa_tentativo_sgc_pea.md`
- `docs/documentacion_sgc/mapa_decisiones_documentales_pea.md`
- `docs/documentacion_sgc/sesion_grill_sgc_pea_v1.md`
