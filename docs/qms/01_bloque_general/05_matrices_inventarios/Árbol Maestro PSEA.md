# Arbol Maestro PSEA - Sistema de Gestion de Calidad CALAIRE-EA

Actualizado: 2026-06-27  
Fuente vigente: `P-PSEA-02 Matriz documental basica del PEA` y `mapa_navegacion_sgc_pea.html`.

## Criterio

Este arbol presenta la estructura vigente de documentos controlados o reservados en `P-PSEA-02` y el flujo del mapa de navegacion.

## Estructura maestra

```mermaid
flowchart LR
  P01["P-PSEA-01\nProtocolo general EA"] --> DG01["DG-PSEA-01\nProtocolo general participacion"]
  P01 --> P02["P-PSEA-02\nMatriz documental"]
  P02 --> P03["P-PSEA-03\nRegistros y evidencias"]
  P03 --> P08["P-PSEA-08\nFlujo tecnico digital"]

  P01 --> P04["P-PSEA-04\nPlanificacion ronda"]
  P04 --> DG02["DG-PSEA-02\ncalaire-app"]
  P04 --> I03["I-PSEA-03\nAdministracion rondas"]
  P04 --> F01["F-PSEA-01\nCalendario"]
  P04 --> F02["F-PSEA-02\nCronograma"]
  P04 --> F03["F-PSEA-03\nRegistro participante"]
  F03 --> F04["F-PSEA-04\nEquipos instrumentos"]
  P04 --> F05["F-PSEA-05\nFicha basica"]
  P04 --> F06["F-PSEA-06\nPlanificacion ronda"]
  P04 --> F16["F-PSEA-16\nCompetencia autorizacion"]
  P04 --> F17["F-PSEA-17\nProveedores criticos"]
  F05 --> F05A

  P01 --> P06["P-PSEA-06\nPreparacion item"]
  P06 --> F07["F-PSEA-07\nControl item"]
  P06 --> F11["F-PSEA-11\nH/E"]

  P01 --> P07["P-PSEA-07\nDiseno estadistico"]
  P07 --> F11
  P07 --> F11A["F-PSEA-11A\nDatos homogeneidad"]
  P07 --> F11B["F-PSEA-11B\nDatos estabilidad"]
  P07 --> F11C["F-PSEA-11C\nResultados homogeneidad"]
  P07 --> F11D["F-PSEA-11D\nResultados estabilidad"]
  P07 --> F12["F-PSEA-12\nDataset oficial"]

  P08 --> DG02
  P08 --> DG03["DG-PSEA-03\npt_app"]
  P08 --> I02["I-PSEA-02\nParticipante calaire-app"]
  P08 --> I04["I-PSEA-04\nPreprocesador pt_app"]
  P08 --> I05["I-PSEA-05\nAnalisis PT"]
  P08 --> F04
  P08 --> F08["F-PSEA-08\nDatos reportados"]
  P08 --> F09["F-PSEA-09\nExportacion PT"]
  P08 --> F10["F-PSEA-10\nPreprocesamiento"]
  P08 --> F12

  DG02 --> I02
  DG02 --> I03
  DG03 --> I04
  DG03 --> I05
  I04 --> F10
  I04 --> F11A
  I04 --> F11B
  I04 --> F11C
  I04 --> F11D
  I05 --> F13["F-PSEA-13\nInforme final"]

  P01 --> P09["P-PSEA-09\nInforme resultados"]
  P09 --> F13

  P10["P-PSEA-10\nNO-NO2"] --> P06
  P11["P-PSEA-11\nCO"] --> P06
  P12["P-PSEA-12\nO3"] --> P06
  P13["P-PSEA-13\nSO2"] --> P06
  P10 --> P07
  P11 --> P07
  P12 --> P07
  P13 --> P07
  P10 --> P09
  P11 --> P09
  P12 --> P09
  P13 --> P09

  P14["P-PSEA-14\nColusion falsificacion"] --> P15["P-PSEA-15\nTNC NC CAPA"]
  P14 --> P05["P-PSEA-05\nComunicaciones"]
  P14 --> P16["P-PSEA-16\nValores sensibles"]
  P14 --> P17["P-PSEA-17\nQuejas"]
  P14 --> P18["P-PSEA-18\nApelaciones"]
  P14 --> P19["P-PSEA-19\nConfidencialidad"]
  P14 --> P20["P-PSEA-20\nCompetencia"]
  P14 --> P21["P-PSEA-21\nProveedores"]
  P05 --> F18["F-PSEA-18\nComunicacion participantes"]
  P15 --> F14["F-PSEA-14\nQueja o NC"]
  P17 --> F14
  P18 --> F15["F-PSEA-15\nApelaciones"]
  P20 --> F16
  P21 --> F17
  P03 --> F14
  P03 --> F15
  P03 --> F16
  P03 --> F17
```

## Estructura operativa de ronda

Cada ronda se materializa bajo `02_despliegue_rondas/<codigo_ronda>/`. La raiz de la ronda contiene solo `checklist_ronda.md` y las siete carpetas de etapa definidas por `P-PSEA-03`:

```text
02_despliegue_rondas/<codigo_ronda>/
  checklist_ronda.md
  01_planificacion_ronda/
  02_comunicaciones_participantes/
  03_preparacion_item/
  04_datos_y_preprocesamiento/
  05_homogeneidad_estabilidad/
  06_analisis_e_informe/
  07_cierre_sgc/
```

## Nivel 1 - Documentos generales

| Codigo | Nombre | Funcion |
|---|---|---|
| `DG-PSEA-01` | Protocolo general de participacion EA | Marco de participacion y politica general. |
| `DG-PSEA-02` | Aplicativo calaire-app | Gestion de rondas, participantes, cronogramas, ficha y captura/exportacion. |
| `DG-PSEA-03` | Aplicativo pt_app | Preprocesamiento, analisis PT, H/E e informe final. |

## Nivel 2 - Procedimientos

| Grupo | Codigos | Funcion |
|---|---|---|
| Marco y control documental | `P-PSEA-01` a `P-PSEA-03` | Protocolo, matriz documental y control de registros/evidencias. |
| Operacion de ronda | `P-PSEA-04` a `P-PSEA-09` | Planificacion, comunicaciones, item, estadistica, flujo digital e informe. |
| Procedimientos tecnicos por analito | `P-PSEA-10` a `P-PSEA-13` | NO-NO2, CO, O3 y SO2. |
| Gestion | `P-PSEA-14` a `P-PSEA-21` | Colusion, NC/CAPA, valores sensibles, quejas, apelaciones, confidencialidad, competencia y proveedores. |
| Reservado | `P-PSEA-23` | Mejora continua del PEA; pendiente de integracion plena. |

## Nivel 3 - Instructivos

| Codigo | Nombre | Funcion |
|---|---|---|
| `I-PSEA-02` | Participante calaire-app | Uso por participante y reporte de datos. |
| `I-PSEA-03` | Administracion rondas calaire-app | Administracion interna de rondas y exportaciones. |
| `I-PSEA-04` | Preprocesador pt_app | Preprocesamiento, entradas, salidas, version y responsable. |
| `I-PSEA-05` | Analisis PT pt_app | Analisis estadistico y generacion de informe. |

## Nivel 4 - Formatos y registros

| Grupo | Codigos | Funcion |
|---|---|---|
| Planificacion | `F-PSEA-01`, `F-PSEA-02`, `F-PSEA-03`, `F-PSEA-04`, `F-PSEA-05`, `F-PSEA-06`, `F-PSEA-16`, `F-PSEA-17` | Calendario, cronograma, registro participante, equipos, ficha basica, planificacion completa, competencia y proveedores cuando aplique. |
| Datos y aplicativos | `F-PSEA-04`, `F-PSEA-08`, `F-PSEA-09`, `F-PSEA-10`, `F-PSEA-12` | Equipos, datos reportados, exportacion PT, preprocesamiento y dataset oficial. |
| Item y H/E | `F-PSEA-07`, `F-PSEA-11`, `F-PSEA-11A` a `F-PSEA-11D` | Control del item, homogeneidad y estabilidad. |
| Informe | `F-PSEA-13` | Informe final de resultados. |
| Comunicaciones | `F-PSEA-18` | Comunicaciones formales y evidencia de envio/respuesta. |
| Cierre SGC | `F-PSEA-14`, `F-PSEA-15` | Cierre documental, queja/NC y apelaciones cuando apliquen. |

## Rutas criticas del mapa

| Ruta | Secuencia |
|---|---|
| Flujo oficial de datos | `P-PSEA-08` -> `DG-PSEA-02` -> `I-PSEA-02` -> `F-PSEA-08` -> `F-PSEA-09` -> `DG-PSEA-03` -> `I-PSEA-04` -> `F-PSEA-10` -> `F-PSEA-12` -> `I-PSEA-05` -> `F-PSEA-13` |
| Homogeneidad y estabilidad | `P-PSEA-06` -> `F-PSEA-07` -> `P-PSEA-07` -> `F-PSEA-11` / `F-PSEA-11A` a `F-PSEA-11D` -> `I-PSEA-05` -> `F-PSEA-13` |
| Planificacion de ronda | `P-PSEA-04` -> `P-PSEA-05` -> `DG-PSEA-02` -> `I-PSEA-03` -> `F-PSEA-03` -> `F-PSEA-04` -> `F-PSEA-06` -> `F-PSEA-05` -> `F-PSEA-01` -> `F-PSEA-02` -> `F-PSEA-16` -> `F-PSEA-17` -> `F-PSEA-18` -> `P-PSEA-06` |
| Estructura de ronda | `P-PSEA-03` -> `P-PSEA-05` -> `F-PSEA-01` -> `F-PSEA-02` -> `F-PSEA-03` -> `F-PSEA-04` -> `F-PSEA-05` -> `F-PSEA-06` -> `F-PSEA-16` -> `F-PSEA-17` -> `F-PSEA-18` -> `F-PSEA-07` -> `F-PSEA-08` -> `F-PSEA-09` -> `F-PSEA-10` -> `F-PSEA-12` -> `F-PSEA-11` -> `F-PSEA-11A` a `F-PSEA-11D` -> `F-PSEA-13` -> `F-PSEA-14` -> `F-PSEA-15` |
| Cierre y gestion SGC | `P-PSEA-03` -> `P-PSEA-14` / `P-PSEA-15` / `P-PSEA-17` / `P-PSEA-18` / `P-PSEA-20` / `P-PSEA-21` -> `F-PSEA-14` / `F-PSEA-15` / `F-PSEA-16` / `F-PSEA-17` |
