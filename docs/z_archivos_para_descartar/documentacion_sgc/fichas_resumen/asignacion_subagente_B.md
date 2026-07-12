# Asignacion de Subagente B: Flujo Digital y Formatos Criticos

**Subagente:** B  
**Paquete de trabajo:** Aplicativos, instructivos y formatos de datos criticos  
**Documentos asignados:** `I-PSEA-02`, `I-PSEA-03`, `I-PSEA-04`, `I-PSEA-05`, `F-PSEA-06`, `F-PSEA-10`, `F-PSEA-11A`, `F-PSEA-11B`, `F-PSEA-11C`, `F-PSEA-11D`, `F-PSEA-12`  
**Fase del plan:** Fase 4

---

## Objetivo

Documentar los elementos que habilitan el flujo digital y los formatos nuevos o redefinidos que conectan `calaire-app` con `pt_app`. Debe quedar cerrado el perfil documental de los insumos y salidas criticos del flujo.

---

## Documentos a fichar

### Instructivos

#### `I-PSEA-02` — Uso de `calaire-app` por participante
- **Tipo:** Instructivo
- **Clase:** Ficha activa
- **Prioridad:** Media-alta
- **Proposito:** Explicar al laboratorio participante como consultar la ronda, confirmar participacion, registrar datos y cargar informacion tecnica en `calaire-app`.
- **Riesgo clave:** No reemplaza `P-PSEA-05` ni define criterios tecnicos; solo explica uso operativo del aplicativo.
- **Salidas:** `F-PSEA-03`, `F-PSEA-04`, `F-PSEA-08`, exportacion posterior `F-PSEA-09`.

#### `I-PSEA-03` — Administracion de rondas en `calaire-app`
- **Tipo:** Instructivo
- **Clase:** Ficha activa
- **Prioridad:** Media-alta
- **Proposito:** Explicar la configuracion y administracion interna de rondas, cronogramas, participantes, ficha digital, exportaciones y casos SGC cuando aplique.
- **Riesgo clave:** No reemplaza `P-PSEA-04`; solo documenta la operacion del aplicativo.
- **Salidas:** `F-PSEA-01`, `F-PSEA-02`, `F-PSEA-06`, `F-PSEA-09`, `F-PSEA-14` si aplica.

#### `I-PSEA-04` — Uso del preprocesador de `pt_app`
- **Tipo:** Instructivo
- **Clase:** Ficha activa
- **Prioridad:** Alta
- **Proposito:** Explicar operativamente como ejecutar preprocesamiento y registrar salidas.
- **Riesgo clave:** No reemplaza `P-PSEA-07` (diseno estadistico); solo explica uso del aplicativo.
- **Salidas:** `F-PSEA-10`, `F-PSEA-11A`, `F-PSEA-11B`, `F-PSEA-12`.

#### `I-PSEA-05` — Uso del modulo de analisis PT de `pt_app`
- **Tipo:** Instructivo
- **Clase:** Ficha activa
- **Prioridad:** Alta
- **Proposito:** Explicar operativamente como ejecutar analisis PT y generar salidas/informe.
- **Riesgo clave:** No reemplaza `P-PSEA-07`; solo explica uso del aplicativo.
- **Salidas:** `F-PSEA-11C`, `F-PSEA-11D`, `F-PSEA-12`, `F-PSEA-13`.

### Formatos criticos

#### `F-PSEA-06` — Ficha digital de ronda EA
- **Tipo:** Formato / Exportacion
- **Clase:** Ficha activa
- **Prioridad:** Alta
- **Proposito:** Exportacion desde `calaire-app` con informacion estructurada de la ronda, incluyendo matriz/nota A-U.
- **Riesgo clave:** No es el plan de ronda (`F-PSEA-05`); es insumo de el.
- **Entrada:** `calaire-app`.
- **Salida:** `F-PSEA-05`.

#### `F-PSEA-10` — Registro de preprocesamiento de datos
- **Tipo:** Formato / Registro
- **Clase:** Ficha activa
- **Prioridad:** Alta
- **Proposito:** Registro de ejecucion del preprocesador: entradas, salidas, fecha, version, responsable/ruta y observaciones.
- **Riesgo clave:** No es el aplicativo `pt_app`; es un registro. Referencia `preprocesamiento_log.csv`.
- **Entrada:** `F-PSEA-09`, `F-PSEA-04`.
- **Salida:** `F-PSEA-11A`, `F-PSEA-11B`, `F-PSEA-12`.

#### `F-PSEA-11A` — Datos preprocesados de homogeneidad
- **Tipo:** Formato / Subformato
- **Clase:** Ficha activa
- **Prioridad:** Alta
- **Proposito:** Subformato producido por `pt_app` para datos preprocesados de homogeneidad.
- **Riesgo clave:** No confundir con `F-PSEA-11C` (resultados de homogeneidad).

#### `F-PSEA-11B` — Datos preprocesados de estabilidad
- **Tipo:** Formato / Subformato
- **Clase:** Ficha activa
- **Prioridad:** Alta
- **Proposito:** Subformato producido por `pt_app` para datos preprocesados de estabilidad.
- **Riesgo clave:** No confundir con `F-PSEA-11D` (resultados de estabilidad).

#### `F-PSEA-11C` — Resultados de homogeneidad
- **Tipo:** Formato / Subformato
- **Clase:** Ficha activa
- **Prioridad:** Alta
- **Proposito:** Resultado de homogeneidad exportado desde `pt_app`.
- **Riesgo clave:** No confundir con `F-PSEA-11A` (datos preprocesados).

#### `F-PSEA-11D` — Resultados de estabilidad
- **Tipo:** Formato / Subformato
- **Clase:** Ficha activa
- **Prioridad:** Alta
- **Proposito:** Resultado de estabilidad exportado desde `pt_app`.
- **Riesgo clave:** No confundir con `F-PSEA-11B` (datos preprocesados).

#### `F-PSEA-12` — Datos oficiales consolidados para evaluacion de aptitud
- **Tipo:** Formato / Dataset oficial
- **Clase:** Ficha activa
- **Prioridad:** Alta
- **Proposito:** Dataset oficial `ronda_<n>_completa.csv`, generado por el preprocesador y usado para evaluacion de aptitud.
- **Riesgo clave:** No es `F-PSEA-09` (exportacion desde `calaire-app`). Es el dataset consolidado final.
- **Entrada:** `F-PSEA-09`, `F-PSEA-04`, preprocesador.
- **Salida:** Modulo de analisis `pt_app`, `F-PSEA-13`.

---

## Reglas especificas para este paquete

1. **Instructivos vs. Procedimientos:** `I-PSEA-04` e `I-PSEA-05` explican "como usar el boton"; `P-PSEA-07` explica "que significa el resultado y como se calcula".
2. **Cadena H/E:** `F-PSEA-11A` -> `F-PSEA-11C` (homogeneidad); `F-PSEA-11B` -> `F-PSEA-11D` (estabilidad).
3. **`F-PSEA-12` es el dataset oficial:** Diferenciar explicitamente de `F-PSEA-09` y de archivos tecnicos intermedios.
4. **`F-PSEA-10` es registro:** No es el preprocesador; es la evidencia de que se ejecuto.

---

## Entregables

- `ficha_I-PSEA-02.md`
- `ficha_I-PSEA-03.md`
- `ficha_I-PSEA-04.md`
- `ficha_I-PSEA-05.md`
- `ficha_F-PSEA-06.md`
- `ficha_F-PSEA-10.md`
- `ficha_F-PSEA-11A.md`
- `ficha_F-PSEA-11B.md`
- `ficha_F-PSEA-11C.md`
- `ficha_F-PSEA-11D.md`
- `ficha_F-PSEA-12.md`

**Ubicacion:** `docs/documentacion_sgc/fichas_resumen/`

---

## Referencias obligatorias

- `00_plantilla_ficha_resumen.md`
- `00_inventario_maestro_fichas.md`
- `docs/documentacion_sgc/mapa_tentativo_sgc_pea.md`
- `docs/documentacion_sgc/mapa_decisiones_documentales_pea.md`
- `docs/documentacion_sgc/sesion_grill_sgc_pea_v1.md`
