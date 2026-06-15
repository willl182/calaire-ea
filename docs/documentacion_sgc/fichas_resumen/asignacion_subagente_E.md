# Asignacion de Subagente E: Gestion Operativa PEA

**Subagente:** E  
**Paquete de trabajo:** Quejas, apelaciones, TNC/NC/CAPA y controles operativos  
**Documentos asignados:** `P-PSEA-14`, `P-PSEA-15`, `P-PSEA-05`, `P-PSEA-16`, `P-PSEA-17`, `P-PSEA-18`, `P-PSEA-19`, `P-PSEA-20`, `P-PSEA-21`, `F-PSEA-14`, `F-PSEA-15`, `F-PSEA-16`, `F-PSEA-17`  
**Fase del plan:** Fase 7

---

## Objetivo

Fichar los procedimientos y registros de gestion que soportan el control operativo del PEA. Las fichas deben distinguir claramente: quejas, apelaciones, TNC/NC/CAPA, confidencialidad, competencia y proveedores criticos.

---

## Documentos a fichar

### Procedimientos de gestion

#### `P-PSEA-14` — Colusion y falsificacion
- **Tipo:** Procedimiento
- **Clase:** Ficha activa
- **Prioridad:** Media-alta
- **Proposito:** Prevenir, detectar y tratar indicios de colusion o falsificacion.
- **Relacion critica:** `P-PSEA-15`, `P-PSEA-16`, `P-PSEA-19`, medidas preventivas en `F-PSEA-05`.

#### `P-PSEA-15` — Trabajo no conforme, no conformidades y acciones correctivas
- **Tipo:** Procedimiento
- **Clase:** Ficha activa
- **Prioridad:** Media-alta
- **Proposito:** TNC/NC/CAPA del PEA. Puede recibir casos desde colusion, quejas, apelaciones, datos o informe.
- **Relacion critica:** `F-PSEA-14` o caso/registro equivalente.

#### `P-PSEA-05` — Comunicaciones del PEA
- **Tipo:** Procedimiento
- **Clase:** Ficha activa
- **Prioridad:** Media-alta
- **Proposito:** Comunicaciones por `calaire-app` y correo, segun el tipo de comunicacion.
- **Relacion critica:** `I-PSEA-02`, `P-PSEA-16`, `P-PSEA-17`, `P-PSEA-18`, `P-PSEA-09`.

#### `P-PSEA-16` — Divulgacion y control de valores sensibles
- **Tipo:** Procedimiento
- **Clase:** Ficha activa
- **Prioridad:** Media-alta
- **Proposito:** Controlar divulgacion de niveles, `x_pt`, `sigma_pt`, valores de referencia, resultados agregados.
- **Relacion critica:** `F-PSEA-05`, `F-PSEA-13`, salidas de `pt_app`, registros de comunicacion.

#### `P-PSEA-17` — Quejas del PEA
- **Tipo:** Procedimiento
- **Clase:** Ficha activa
- **Prioridad:** Media-alta
- **Proposito:** Gestionar quejas como casos SGC en `calaire-app`.
- **Riesgo clave:** No confundir con apelaciones (`P-PSEA-18`).
- **Relacion critica:** `F-PSEA-14` o caso SGC equivalente; comunicaciones relacionadas.

#### `P-PSEA-18` — Apelaciones del PEA
- **Tipo:** Procedimiento
- **Clase:** Ficha activa
- **Prioridad:** Media-alta
- **Proposito:** Manejar apelaciones aparte, por correo formal al correo institucional del grupo.
- **Riesgo clave:** No se gestiona en `calaire-app`; va por correo formal.
- **Relacion critica:** `F-PSEA-15` o registro equivalente; comunicaciones formales.

#### `P-PSEA-19` — Confidencialidad operativa interna del PEA
- **Tipo:** Procedimiento
- **Clase:** Ficha activa
- **Prioridad:** Media-alta
- **Proposito:** Confidencialidad de datos, participantes, codigos, archivos exportados y resultados.
- **Riesgo clave:** No es politica institucional general; es acotada al PEA.
- **Relacion critica:** `F-PSEA-08`, `F-PSEA-09`, `F-PSEA-12`, `F-PSEA-13`.

#### `P-PSEA-20` — Competencia y autorizacion operativa del PEA
- **Tipo:** Procedimiento
- **Clase:** Ficha activa
- **Prioridad:** Media-alta
- **Proposito:** Roles tecnicos y operativos del PEA.
- **Riesgo clave:** No cubre talento humano general.
- **Relacion critica:** `F-PSEA-16` o matriz equivalente.

#### `P-PSEA-21` — Proveedores criticos del PEA
- **Tipo:** Procedimiento
- **Clase:** Ficha activa
- **Prioridad:** Media-alta
- **Proposito:** Proveedores o servicios criticos del PEA.
- **Riesgo clave:** Respetar limites de tercerizacion permitidos por ISO/IEC 17043; no cubre compras generales.
- **Relacion critica:** `F-PSEA-17` o evaluacion equivalente.

### Formatos de gestion

#### `F-PSEA-14` — Registro/caso de queja o NC
- **Tipo:** Formato / Registro
- **Clase:** Ficha preliminar
- **Prioridad:** Media
- **Proposito:** Caso SGC relacionado con quejas y/o NC.
- **Riesgo clave:** Confirmar estructura con implementacion de casos en `calaire-app`.
- **Relacion critica:** `P-PSEA-15`, `P-PSEA-17`.

#### `F-PSEA-15` — Registro de apelaciones
- **Tipo:** Formato / Registro
- **Clase:** Ficha preliminar
- **Prioridad:** Media
- **Proposito:** Registro de apelacion recibida por correo formal institucional.
- **Riesgo clave:** No se gestiona como caso en `calaire-app` por ahora.
- **Relacion critica:** `P-PSEA-18`, `P-PSEA-05`.

#### `F-PSEA-16` — Matriz de competencia/autorizacion
- **Tipo:** Formato / Registro
- **Clase:** Ficha preliminar
- **Prioridad:** Media
- **Proposito:** Evidencia de competencia/autorizacion de roles tecnicos y operativos.
- **Riesgo clave:** Confirmar estructura de matriz.
- **Relacion critica:** `P-PSEA-20`.

#### `F-PSEA-17` — Evaluacion de proveedores criticos
- **Tipo:** Formato / Registro
- **Clase:** Ficha preliminar
- **Prioridad:** Media
- **Proposito:** Evaluacion o registro de proveedores/servicios criticos.
- **Riesgo clave:** Confirmar estructura de evaluacion.
- **Relacion critica:** `P-PSEA-21`.

---

## Reglas especificas para este paquete

1. **Separar quejas de apelaciones:** Quejas (`P-PSEA-17`) van por `calaire-app`; apelaciones (`P-PSEA-18`) van por correo formal.
2. **Acotar al PEA:** `P-PSEA-19`, `P-PSEA-20`, `P-PSEA-21` no son politicas institucionales generales.
3. **Preliminaridad:** `F-PSEA-14`, `F-PSEA-15`, `F-PSEA-16`, `F-PSEA-17` requieren confirmacion de estructura; no desarrollar contenido de fondo.
4. **TNC/NC/CAPA:** `P-PSEA-15` puede recibir casos desde multiples fuentes; no duplicar rutas.

---

## Entregables

- `ficha_P-PSEA-14.md`
- `ficha_P-PSEA-15.md`
- `ficha_P-PSEA-05.md`
- `ficha_P-PSEA-16.md`
- `ficha_P-PSEA-17.md`
- `ficha_P-PSEA-18.md`
- `ficha_P-PSEA-19.md`
- `ficha_P-PSEA-20.md`
- `ficha_P-PSEA-21.md`
- `ficha_F-PSEA-14.md`
- `ficha_F-PSEA-15.md`
- `ficha_F-PSEA-16.md`
- `ficha_F-PSEA-17.md`

**Ubicacion:** `docs/documentacion_sgc/fichas_resumen/`

---

## Referencias obligatorias

- `00_plantilla_ficha_resumen.md`
- `00_inventario_maestro_fichas.md`
- `docs/documentacion_sgc/mapa_tentativo_sgc_pea.md`
- `docs/documentacion_sgc/mapa_decisiones_documentales_pea.md`
- `docs/documentacion_sgc/sesion_grill_sgc_pea_v1.md`
