# Panorama del Sistema de Gestion de Calidad PEA y Estado Actual

Este documento resume el estado actual del sistema documental del **Proveedor de Ensayos de Aptitud (PEA)** para el proyecto **CALAIRE-EA**: *Implementacion de Ensayos de Aptitud para Gases Contaminantes Criterio en Colombia*.

El sistema se encuentra en fase de reorganizacion documental. La prioridad actual es consolidar la trazabilidad entre procedimientos, formatos, aplicativos, instructivos y flujo digital de datos antes de integrar el esquema con el SGC macro institucional.

---

## 1. Marco normativo y tecnico

El sistema PEA se estructura tomando como referencia principal:

- **ISO/IEC 17043:2023:** requisitos para proveedores de ensayos de aptitud.
- **ISO 13528:2022:** metodos estadisticos aplicables a ensayos de aptitud.
- **ISO/IEC 17025:2017:** marco tecnico de competencia de laboratorios, usado como contexto para las mediciones de gases contaminantes criterio.

El alcance de este sistema documental no busca duplicar el SGC macro. Elementos como auditorias internas/externas, revision por la direccion, imparcialidad institucional, control documental macro, talento humano general y compras generales se manejan por fuera del sistema documental propio del PEA.

---

## 2. Arquitectura documental de trabajo

La arquitectura documental se encuentra organizada, para efectos de revision y elaboracion progresiva, en cuatro familias:

### 2.1 Documentos generales (`DG-PSEA`)

- `DG-PSEA-01`: Protocolo general de participacion EA. Se mantiene como documento marco, pendiente de revision final.
- `DG-PSEA-02`: Aplicativo `calaire-app`. Documento general del aplicativo usado para gestion de rondas, participantes, cronogramas, ficha de ronda, captura/exportacion de datos y quejas.
- `DG-PSEA-03`: Aplicativo `pt_app`. Documento general del aplicativo usado para preprocesamiento, consolidacion, analisis estadistico, homogeneidad/estabilidad e informe final.

Control de trabajo: los aplicativos no deben codificarse como formatos. Los formatos `F-PSEA` corresponden a registros, evidencias, exportaciones oficiales o salidas del sistema.

### 2.2 Procedimientos (`P-PSEA`)

Los procedimientos se reorganizan segun su funcion real:

- Procedimientos tecnicos por analito: `P-PSEA-02` a `P-PSEA-05` para NO/NO2, CO, O3 y SO2. Deben aligerarse para documentar solo particularidades tecnicas del gas y citar los documentos transversales.
- Procedimiento estadistico central: `P-PSEA-06`, para valor asignado, `sigma_pt`, incertidumbre, outliers, criterios de desempeno, reglas de decision e integracion de homogeneidad/estabilidad.
- Informe de resultados: `P-PSEA-07`, que absorbe el rol antes atribuido a `P-PSEA-22`.
- Colusion/falsificacion: `P-PSEA-08`, independiente.
- Planificacion de ronda: `P-PSEA-09`, soportado en `calaire-app` y formatos exportables.
- Preparacion/control del item gaseoso: `P-PSEA-10`, enfocado en generacion de concentraciones con calibrador dinamico y cilindro.
- Mapeo documental, registros y datos: `P-PSEA-12`, `P-PSEA-13` y `P-PSEA-23`.
- Gestion operativa propia del PEA: `P-PSEA-16`, `P-PSEA-20`, `P-PSEA-21`, `P-PSEA-24`, `P-PSEA-25`, `P-PSEA-26`, `P-PSEA-27` y `P-PSEA-28`.

Quedan fuera o reservados:

- `P-PSEA-11`: reservado/no aplicable por ahora.
- `P-PSEA-17`: auditorias internas/externas, fuera del alcance PEA.
- `P-PSEA-18`: revision por la direccion, fuera del alcance PEA.
- `P-PSEA-19`: imparcialidad, manejada por fuera.
- `P-PSEA-22`: absorbido/reservado dentro de `P-PSEA-07`.

### 2.3 Instructivos (`I-PSEA`)

Los instructivos clave quedan asociados a la operacion de aplicativos:

- `I-PSEA-10`: uso de `calaire-app` por el participante.
- `I-PSEA-16`: administracion de rondas en `calaire-app`.
- `I-PSEA-17`: uso del preprocesador de datos de `pt_app`.
- `I-PSEA-18`: uso del modulo de analisis PT de `pt_app`.

Control de trabajo: el procedimiento define el criterio tecnico; el instructivo explica como operar el aplicativo.

### 2.4 Formatos y registros (`F-PSEA`)

Los formatos se redefinen como registros, evidencias o salidas oficiales. Los cambios principales son:

- `F-PSEA-03`: retirado/reservado; sustituido por `F-PSEA-06`.
- `F-PSEA-04`: informe final de resultados generado desde `pt_app`.
- `F-PSEA-05A`: anexo tecnico de equipos e instrumentos del participante; equivalente a `ronda_1_equipos.csv`.
- `F-PSEA-06`: plan de ronda EA.
- `F-PSEA-07`: ficha digital de ronda exportable desde `calaire-app`.
- `F-PSEA-08`: dossier/registro de preparacion y control del item de ensayo gaseoso.
- `F-PSEA-09`: datos reportados por el participante en `calaire-app`.
- `F-PSEA-10`: registro de preprocesamiento de datos.
- `F-PSEA-11`: reservado/no aplicable por ausencia de envio fisico de items.
- `F-PSEA-12`: datos de participantes exportados desde `calaire-app` para analisis PT.
- `F-PSEA-13`: registro de homogeneidad y estabilidad.
- `F-PSEA-13A-D`: datos y resultados de homogeneidad/estabilidad generados o exportados desde `pt_app`.
- `F-PSEA-14`: datos oficiales consolidados para evaluacion de aptitud, equivalente a `ronda_<n>_completa.csv`.

---

## 3. Flujo digital de datos

El flujo de datos propuesto para elaboracion documental se controla asi:

1. `calaire-app` gestiona la ronda, participantes, cronogramas, ficha de ronda y captura de datos.
2. El participante registra sus datos en `calaire-app`, generando `F-PSEA-09`.
3. `calaire-app` exporta datos de participantes como `F-PSEA-12` y equipos/instrumentos como `F-PSEA-05A`.
4. `pt_app` recibe esos datos y ejecuta el preprocesamiento.
5. El preprocesamiento genera `F-PSEA-10`, subformatos H/E (`F-PSEA-13A-B`) y el dataset oficial `F-PSEA-14`.
6. `pt_app` ejecuta el analisis estadistico y genera resultados H/E (`F-PSEA-13C-D`) e informe final `F-PSEA-04`.

Los archivos tecnicos internos del preprocesador no se convierten automaticamente en formatos. Deben listarse y controlarse dentro de `P-PSEA-23`, incluyendo archivos como `datos_estabilidad_homogeneidad.csv`, `datos_ronda.csv`, `niveles_calaire.csv`, `diseno_estabilidad_homogeneidad.csv`, `preprocesamiento_log.csv`, `h_referencia_ronda.csv` y `referencia_ronda.csv`.

---

## 4. Estado actual de consolidacion

Se generaron tres documentos de trabajo para estabilizar la arquitectura antes de intervenir los documentos principales:

- [mapa_decisiones_documentales_pea.md](mapa_decisiones_documentales_pea.md): matriz de decisiones por documento.
- [mapa_tentativo_sgc_pea.md](mapa_tentativo_sgc_pea.md): mapa tentativo de todo el SGC PEA, con descripcion rapida y formatos relacionados.
- [sesion_grill_sgc_pea_v1.md](sesion_grill_sgc_pea_v1.md): primera version consolidada de la sesion de revision.

Tambien se corrigio `F-PSEA-06 Plan de Ronda EA` para eliminar la afirmacion incorrecta de que homogeneidad/estabilidad no aplicaba. El plan ahora debe indicar que H/E se documenta mediante `F-PSEA-13` y sus subformatos.

---

## 5. Prioridades de actualizacion

El orden recomendado de trabajo es:

1. Elaborar `P-PSEA-12` como matriz documental del PEA.
2. Elaborar `P-PSEA-13` como matriz de registros/evidencias.
3. Elaborar o actualizar `P-PSEA-23` como flujo tecnico de datos digitales.
4. Documentar `DG-PSEA-03`, `I-PSEA-17` e `I-PSEA-18` para `pt_app`.
5. Crear o ajustar los formatos redefinidos: `F-PSEA-07`, `F-PSEA-10`, `F-PSEA-13A-D` y `F-PSEA-14`.
6. Actualizar procedimientos transversales: `P-PSEA-06`, `P-PSEA-07`, `P-PSEA-09`, `P-PSEA-10`, `P-PSEA-20`, `P-PSEA-21`, `P-PSEA-24`, `P-PSEA-25`, `P-PSEA-26`, `P-PSEA-27` y `P-PSEA-28`.
7. Actualizar procedimientos por analito `P-PSEA-02` a `P-PSEA-05`, eliminando duplicaciones y citando los procedimientos transversales.
8. Revisar al final `DG-PSEA-01` / `P-PSEA-01` y el `README.md` del directorio.

---

## 6. Referencias internas

- [Mapa de decisiones documentales](mapa_decisiones_documentales_pea.md)
- [Mapa tentativo del SGC PEA](mapa_tentativo_sgc_pea.md)
- [Sesion de grill SGC PEA - version 1](sesion_grill_sgc_pea_v1.md)
- [Documentacion funcional de calaire-app](calaire-app_func_docs_sgc.md)
- [Documentacion de registros de calaire-app](calaire-app_reg_docs_sgc.md)
