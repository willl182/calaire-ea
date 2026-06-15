# Sesion de Grill SGC PEA - Version 1

**Fecha:** 2026-06-13  
**Estado:** primera version consolidada  
**Proposito:** conservar las decisiones de arquitectura documental tomadas durante la revision del sistema de gestion del PEA, antes de actualizar `sgc_res.md`, `README.md` o `P-PSEA-01`.

## Alcance de la sesion

La sesion reviso el sistema documental del PEA considerando dos aplicativos operativos:

- `calaire-app`: aplicativo de gestion de rondas, participantes, cronogramas, captura/exportacion de datos y gestion de algunos casos SGC.
- `pt_app`: aplicativo para preprocesamiento, consolidacion de datos, analisis estadistico, homogeneidad/estabilidad e informe final.

El objetivo no fue crear un SGC paralelo completo, sino ordenar el mapa documental del PEA para que despues pueda integrarse con el sistema de gestion macro.

## Restricciones decididas

- No actualizar `sgc_res.md` hasta el cierre de la revision global.
- No actualizar `README.md` hasta el cierre.
- No intervenir `P-PSEA-01` por ahora.
- No entrar todavia en el contenido detallado del informe final `F-PSEA-04`.
- No desarrollar por ahora riesgos generales ni mejora continua.
- No incluir aprobacion, obsolescencia, retencion o control documental macro en esta fase.

## Decisiones estructurales

### Aplicativos como documentos generales

Los aplicativos no se codifican como formatos. Quedan como documentos generales:

- `DG-PSEA-02`: aplicativo `calaire-app`.
- `DG-PSEA-03`: aplicativo `pt_app`.

Los formatos `F-PSEA` representan registros, evidencias, exportaciones oficiales o salidas del sistema, no el software en si.

### Instructivos de aplicativos

Se definio el siguiente esquema:

- `I-PSEA-10`: instructivo para participante en `calaire-app`.
- `I-PSEA-16`: instructivo de administracion de rondas en `calaire-app`.
- `I-PSEA-17`: instructivo de uso del preprocesador de datos de `pt_app`.
- `I-PSEA-18`: instructivo de uso del modulo de analisis PT de `pt_app`.

La separacion clave es que un procedimiento define criterio tecnico y un instructivo explica uso operativo del aplicativo.

## Mapa de formatos F-PSEA

| Codigo | Decision |
|---|---|
| `F-PSEA-01` | Calendario global de ronda en `calaire-app`, exportable y utilizable para Gantt/Mermaid. |
| `F-PSEA-02` | Cronograma detallado de ronda en `calaire-app`, diligenciable/exportable. |
| `F-PSEA-03` | Retirado o reservado; sustituido por `F-PSEA-06`. |
| `F-PSEA-04` | Informe final de resultados generado desde `pt_app`; no definir contenido aun. |
| `F-PSEA-05` | Registro de participacion. |
| `F-PSEA-05A` | Anexo tecnico de equipos e instrumentos del participante; equivalente a `ronda_1_equipos.csv`; alimenta `pt_app`. |
| `F-PSEA-06` | Plan de Ronda EA. Debe integrar `F-PSEA-01`, `F-PSEA-02`, `F-PSEA-07` y nota/matriz A-U ISO/IEC 17043:2023 7.2.1.3. |
| `F-PSEA-07` | Ficha digital de ronda exportada desde `calaire-app`; insumo de `F-PSEA-06`. |
| `F-PSEA-08` | Dossier/registro de preparacion y control del item de ensayo gaseoso. |
| `F-PSEA-09` | Registro de datos reportados por el participante en `calaire-app`. |
| `F-PSEA-10` | Registro de preprocesamiento de datos. No es aplicativo. |
| `F-PSEA-11` | Reservado/no aplicable por ahora; el antiguo envio de items no aplica. |
| `F-PSEA-12` | Datos de participantes exportados desde `calaire-app` para analisis PT. No es `ronda_<n>_completa.csv`. |
| `F-PSEA-13` | Registro de homogeneidad y estabilidad del item de ensayo. |
| `F-PSEA-13A` | Datos preprocesados de homogeneidad. |
| `F-PSEA-13B` | Datos preprocesados de estabilidad. |
| `F-PSEA-13C` | Resultados de homogeneidad exportados desde `pt_app`. |
| `F-PSEA-13D` | Resultados de estabilidad exportados desde `pt_app`. |
| `F-PSEA-14` | Datos oficiales consolidados para evaluacion de aptitud, equivalente a `ronda_<n>_completa.csv`. |

## Flujo de datos acordado

El flujo oficial de datos de participantes es:

1. El participante registra datos en `calaire-app`.
2. `calaire-app` genera/exporta `F-PSEA-09`, `F-PSEA-12`, `F-PSEA-05A` y la informacion de ronda.
3. `pt_app` recibe `F-PSEA-12` y `F-PSEA-05A`.
4. El preprocesador de `pt_app` genera `F-PSEA-10`, `F-PSEA-13A`, `F-PSEA-13B` y `F-PSEA-14`.
5. El modulo de analisis de `pt_app` usa `F-PSEA-14` y los resultados H/E para generar analisis e informe final `F-PSEA-04`.

El procesamiento interno alternativo con datos de participantes dentro de `pt_app` queda como capacidad posible, pero no como flujo oficial rutinario.

## Archivos tecnicos del preprocesador

Los archivos tecnicos del preprocesador no se convierten automaticamente en formatos `F-PSEA`. Deben listarse y controlarse en `P-PSEA-23`.

Ejemplos:

- `datos_estabilidad_homogeneidad.csv`
- `datos_ronda.csv`
- `datos_ronda_part.csv`
- `datos_ronda_2a.csv`
- `datos_ronda_2b.csv`
- `niveles_calaire.csv`
- `diseno_estabilidad_homogeneidad.csv`
- `h_estabilidad_homogeneidad.csv`
- `mm_estabilidad_homogeneidad.csv`
- `incertidumbre.md`
- `preprocesamiento_log.csv`
- `h_referencia_ronda.csv`
- `referencia_ronda.csv`

`preprocesamiento_log.csv` se referencia dentro de `F-PSEA-10`, sin duplicarlo.

## Decisiones sobre procedimientos

### Procedimientos tecnicos por gas

`P-PSEA-02` a `P-PSEA-05` se mantienen como procedimientos especificos por analito/gas:

- `P-PSEA-02`: NO/NO2.
- `P-PSEA-03`: CO.
- `P-PSEA-04`: O3.
- `P-PSEA-05`: SO2.

Deben aligerarse para documentar condiciones y decisiones propias del gas. Deben citar, no duplicar:

- `P-PSEA-06`: diseno estadistico.
- `F-PSEA-13` y `F-PSEA-13A-D`: homogeneidad y estabilidad.
- `P-PSEA-07`: informe de resultados.
- `P-PSEA-23`: flujo tecnico de datos.
- `DG-PSEA-03`, `I-PSEA-17`, `I-PSEA-18`: `pt_app`.

### Procedimiento estadistico

`P-PSEA-06` queda como procedimiento tecnico/metrologico central para:

- diseno estadistico;
- valor asignado;
- `sigma_pt`;
- incertidumbre;
- outliers;
- desempeno;
- H/E como insumo;
- reglas de decision.

No es instructivo de uso de `pt_app`.

### Informe de resultados

`P-PSEA-07` debe gobernar la generacion/emision del informe de resultados y absorber el rol de `P-PSEA-22`.

El informe final es `F-PSEA-04` y se genera desde `pt_app`. No se define aun su contenido.

### Colusion y falsificacion

`P-PSEA-08` se mantiene independiente. Debe cubrir prevencion y deteccion de colusion/falsificacion, con conexiones a:

- `P-PSEA-16`, si deriva en TNC/NC/CAPA.
- `P-PSEA-21`, por valores sensibles.
- `P-PSEA-26`, por confidencialidad.
- `F-PSEA-06`, por medidas preventivas en el plan de ronda.

### Planificacion

`P-PSEA-09` se mantiene como procedimiento transversal de planificacion de ronda. Debe actualizarse para reflejar que la planificacion se soporta en `calaire-app` y formatos exportables:

- `F-PSEA-01`
- `F-PSEA-02`
- `F-PSEA-06`
- `F-PSEA-07`
- `F-PSEA-08`

Debe incluir o referenciar la matriz/nota A-U de ISO/IEC 17043:2023 7.2.1.3.

### Item de ensayo gaseoso

`P-PSEA-10` queda como procedimiento de preparacion y control del item de ensayo gaseoso. No es envio/recepcion.

Debe describir como generar concentraciones usando calibrador dinamico y cilindro, tomando niveles definidos desde `calaire-app`.

Registro asociado:

- `F-PSEA-08`: dossier/registro de preparacion y control del item.

### Procedimientos retirados, reservados o absorbidos

| Codigo | Decision |
|---|---|
| `P-PSEA-11` | Reservado/no aplicable por ahora. |
| `P-PSEA-17` | Retirado; auditorias internas/externas quedan fuera del alcance PEA. |
| `P-PSEA-18` | Retirado; revision por la direccion queda fuera del alcance PEA. |
| `P-PSEA-19` | Retirado; imparcialidad se maneja por fuera del sistema documental propio del PEA. |
| `P-PSEA-22` | Absorbido/reservado dentro de `P-PSEA-07`. |

### Matrices y flujo documental

`P-PSEA-12` sera la matriz documental basica del PEA. Debe listar todo lo numerado:

- `DG-PSEA`
- `P-PSEA`
- `I-PSEA`
- `F-PSEA`
- subformatos

No debe tratar aprobacion, retencion, obsolescencia ni control documental macro.

`P-PSEA-13` sera la matriz de registros/evidencias generadas por ronda o evento. No lista procedimientos, instructivos ni aplicativos.

`P-PSEA-23` sera el mapa/procedimiento de flujo tecnico de datos digitales del PEA. Debe mapear aplicaciones, archivos tecnicos, formatos oficiales y salidas de analisis.

### Gestion operativa

| Codigo | Decision |
|---|---|
| `P-PSEA-14` | Riesgos generales del PEA; mantener idea, no desarrollar ahora. |
| `P-PSEA-15` | Mejora continua del PEA; mantener idea, no desarrollar ahora. |
| `P-PSEA-16` | Mantener como TNC/NC/CAPA del PEA. |
| `P-PSEA-20` | Mantener comunicaciones del PEA, usando `calaire-app` y correo segun aplique. |
| `P-PSEA-21` | Mantener divulgacion/control de valores sensibles. |
| `P-PSEA-24` | Mantener quejas del PEA como casos SGC en `calaire-app`. |
| `P-PSEA-25` | Mantener apelaciones aparte; se reciben por correo formal al correo institucional del grupo. |
| `P-PSEA-26` | Mantener confidencialidad operativa interna del PEA, acotada a datos, participantes y resultados. |
| `P-PSEA-27` | Mantener competencia/autorizacion de roles tecnicos y operativos del PEA. |
| `P-PSEA-28` | Mantener proveedores criticos del PEA, respetando limites de tercerizacion de ISO/IEC 17043. |

## Correcciones importantes hechas durante la sesion

- `F-PSEA-06` no debe decir que homogeneidad/estabilidad no aplica. Eso era falso. Debe indicar que H/E se documenta en `F-PSEA-13`.
- `F-PSEA-10` no es el aplicativo; es el registro de preprocesamiento de datos.
- `F-PSEA-14` no debe perderse del mapa; es el dataset oficial consolidado.
- `P-PSEA-17`, `P-PSEA-18` y `P-PSEA-19` salen del alcance PEA.
- `P-PSEA-25` no se gestiona en `calaire-app`; va por correo formal institucional.

## Documentos creados o actualizados en esta etapa

- `docs/documentacion_sgc/F-PSEA-06 Plan de Ronda EA.md`
- `docs/documentacion_sgc/mapa_decisiones_documentales_pea.md`
- `docs/documentacion_sgc/sesion_grill_sgc_pea_v1.md`
- `logs/CURRENT_SESSION.md`
- `logs/history/260613_1334_findings.md`
- `logs/history/260613_1342_findings.md`

## Siguientes pasos sugeridos

1. Revisar esta version con el mapa de decisiones.
2. Estabilizar `P-PSEA-12`, `P-PSEA-13` y `P-PSEA-23`.
3. Luego actualizar documentos especificos en orden: formatos, procedimientos transversales, procedimientos por gas.
4. Solo al final actualizar `sgc_res.md`, `README.md` y `P-PSEA-01`.
