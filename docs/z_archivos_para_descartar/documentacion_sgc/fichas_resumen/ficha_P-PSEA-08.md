# Ficha Resumen: P-PSEA-08

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `P-PSEA-08` |
| **Nombre decidido** | Flujo tecnico de datos digitales del PEA |
| **Tipo documental** | Procedimiento con matriz resumen y matriz operativa anexa |
| **Estado** | Elaborar / Actualizar |
| **Prioridad** | Alta |
| **Clase de ficha** | Ficha activa |

---

## Proposito y rol

### Proposito operativo

Mapea el flujo completo de datos digitales del PEA: desde la captura en `calaire-app`, pasando por la exportacion oficial, el preprocesamiento en `pt_app`, la generacion de subformatos H/E, la consolidacion del dataset oficial y la produccion del informe final. Documenta aplicativos, archivos tecnicos internos, formatos oficiales y salidas de analisis.

### Rol en el flujo

- [x] Criterio tecnico
- [x] Matriz
- [ ] Entrada
- [ ] Salida
- [ ] Registro oficial
- [ ] Evidencia
- [ ] Instructivo
- [ ] Soporte documental

Es el documento de referencia tecnica que gobierna la arquitectura de datos del PEA.

### Estructura documental esperada

`P-PSEA-08` debe desarrollarse como procedimiento tecnico, no como tabla aislada. El cuerpo principal define el flujo, responsabilidades, puntos de control y reglas de trazabilidad de datos. Dentro del procedimiento debe incluirse una matriz resumen de CSV simples para consulta rapida. Como anexo, debe mantenerse una matriz operativa detallada con todos los CSV simples relevantes del flujo, su condicion de conservacion y su relacion con formatos oficiales o evidencias.

---

## Aplicativos y tecnologia

#### Aplicativo asociado

- [x] `calaire-app`
- [x] `pt_app`
- [ ] Ambos
- [ ] Ninguno

Ambos aplicativos son componentes centrales del flujo; este procedimiento los vincula.

---

## Flujo de datos

#### Entradas principales

| Codigo / fuente | Descripcion | Rol en el flujo |
|---|---|---|
| `calaire-app` | Captura de datos, participantes, cronogramas | Origen |
| `F-PSEA-09` | Exportacion oficial de datos de participantes | Entrada oficial |
| `F-PSEA-04` | Anexo tecnico de equipos e instrumentos | Entrada oficial |
| Anexos CSV de `P-PSEA-08` | `datos_ronda.csv`, `niveles_calaire.csv`, archivos de configuracion y demas CSV operativos del flujo digital | Insumo tecnico controlado |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| `F-PSEA-10` | Registro de preprocesamiento | Registro oficial |
| `F-PSEA-11A` | Datos preprocesados de homogeneidad | Salida tecnica |
| `F-PSEA-11B` | Datos preprocesados de estabilidad | Salida tecnica |
| `F-PSEA-12` | Dataset oficial consolidado (`ronda_<n>_completa.csv`) | Salida oficial |
| `F-PSEA-13` | Informe final de resultados | Producto final |

#### Anexos CSV del procedimiento

Los CSV simples que soportan la ejecucion tecnica del flujo digital se tratan como anexos operativos de `P-PSEA-08`. Por trazabilidad de datos conforme al enfoque de ISO/IEC 17043, este procedimiento debe identificar todos los CSV simples relevantes del flujo, incluyendo entradas, archivos intermedios, archivos de configuracion, salidas tecnicas y datasets consolidados. Para cada CSV debe quedar claro su nombre, funcion, punto de generacion o consumo, aplicativo asociado, relacion con formatos oficiales y condicion de conservacion. Solo los CSV que quedan como evidencia oficial o soporte trazable de una ronda/evento se registran ademas en `P-PSEA-03`.

La matriz operativa anexa se limita a archivos `.csv` simples. No incluye archivos `.xlsx`, `.json`, `.rds`, `.html`, `.qmd` ni otros artefactos digitales; esos archivos se controlan mediante el formato oficial, instructivo o documento especifico que corresponda.

La matriz resumen del procedimiento debe clasificar cada CSV simple con una condicion de conservacion minima: `evidencia_oficial`, `soporte_trazable`, `intermedio_reproducible` o `transitorio`. La matriz operativa anexa desarrolla el detalle tecnico de cada archivo, incluyendo ruta o ubicacion, responsable, version o fecha de generacion, ronda/evento asociado, formato relacionado y observaciones de trazabilidad.

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `DG-PSEA-02` | Origen de datos en calaire-app | Obligatorio |
| `DG-PSEA-03` | Destino de preprocesamiento y analisis | Obligatorio |
| `I-PSEA-04` | Instructivo de preprocesador | Obligatorio |
| `I-PSEA-05` | Instructivo de modulo de analisis | Obligatorio |
| `P-PSEA-07` | Criterio estadistico que gobierna el flujo | Obligatorio |
| `P-PSEA-09` | Generacion del informe | Obligatorio |
| `P-PSEA-02` | Matriz documental que lista elementos | Referencia |
| `P-PSEA-03` | Procedimiento que trackea los CSV y salidas del flujo cuando quedan como registros o evidencias | Obligatorio |

---

## Limites y riesgos

#### Limites de alcance

- No es un instructivo de uso de los aplicativos (eso es `I-PSEA-04` e `I-PSEA-05`).
- No gobierna aprobacion, versionamiento ni control de software.
- No define criterios estadisticos; cita `P-PSEA-07` para eso.
- No convierte archivos tecnicos internos en formatos `F-PSEA`; los declara como anexos CSV del flujo cuando aplique y remite a `P-PSEA-03` solo aquellos que queden como registros o evidencias conservadas.
- No sustituye la matriz operativa de `P-PSEA-03`; su matriz operativa anexa gobierna el flujo tecnico de archivos, mientras `P-PSEA-03` gobierna el tracking de evidencias conservadas.

#### Riesgos de interpretacion

- **Confundir flujo oficial con capacidad interna alternativa:** El procesamiento interno alternativo dentro de `pt_app` es posible, pero no es el flujo oficial rutinario.
- **Promover archivos tecnicos a F-PSEA:** Archivos como `datos_ronda.csv`, `niveles_calaire.csv`, `preprocesamiento_log.csv` deben mapearse como anexos CSV de `P-PSEA-08`; solo los que correspondan se reflejan en formatos oficiales como `F-PSEA-10` o `F-PSEA-12`.
- **Confundir F-PSEA-09 con F-PSEA-12:** `F-PSEA-09` es exportacion desde `calaire-app`; `F-PSEA-12` es dataset consolidado desde `pt_app`.
- **Tratar P-PSEA-08 como instructivo:** Es procedimiento tecnico de flujo de datos, no manual de usuario.
- **Duplicar control de evidencias:** `P-PSEA-08` identifica y contextualiza todos los CSV relevantes para trazabilidad de datos; `P-PSEA-03` solo trackea los que quedan como registros o evidencias conservadas.

---

## Criterio minimo de elaboracion

El procedimiento mapea con claridad: (1) que datos entran a cada aplicativo, (2) que anexos CSV o archivos tecnicos internos se generan, (3) que formatos oficiales salen, (4) cual es la secuencia de transformacion, (5) donde se diferencia el flujo oficial de capacidades internas alternativas, (6) cuales CSV quedan como evidencia oficial o soporte trazable para ser trackeados en `P-PSEA-03`, y (7) como se separa la matriz resumen interna de la matriz operativa anexa.
