# Ficha Resumen: P-PSEA-03

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `P-PSEA-03` |
| **Nombre decidido** | Control de registros y evidencias del PEA |
| **Tipo documental** | Procedimiento con matrices anexas |
| **Estado** | Elaborado |
| **Prioridad** | Alta |
| **Clase de ficha** | Ficha activa |

---

## Proposito y rol

### Proposito operativo

Establece como se identifican, clasifican y trackean los registros y evidencias generadas por cada ronda o evento del PEA. Incluye una matriz resumen dentro del procedimiento y una matriz operativa como anexo para el seguimiento detallado de registros, evidencias y anexos tecnicos que quedan como evidencia, incluidos los CSV del flujo digital cuando deban conservarse. Es la contraparte operativa de `P-PSEA-02` (matriz documental).

### Rol en el flujo

- [x] Criterio tecnico
- [x] Matriz
- [x] Evidencia
- [ ] Entrada
- [ ] Salida
- [ ] Registro oficial
- [ ] Instructivo
- [ ] Soporte documental

Funciona como procedimiento de control operativo de registros/evidencias y como punto de trazabilidad para las matrices anexas.

---

## Aplicativos y tecnologia

#### Aplicativo asociado

- [x] `calaire-app`
- [x] `pt_app`
- [ ] Ambos
- [ ] Ninguno

Recibe registros desde ambos aplicativos; el procedimiento define como se controlan y las matrices los catalogan.

---

## Flujo de datos

#### Entradas principales

| Codigo / fuente | Descripcion | Rol en el flujo |
|---|---|---|
| Ronda o evento PEA | Ejecucion de una ronda piloto o EA | Insumo |
| `F-PSEA-01` a `F-PSEA-12` | Formatos generados durante la ronda | Referencia |
| `P-PSEA-06` | Preparacion y control del item | Referencia |
| `P-PSEA-08` | Flujo tecnico de datos y anexos CSV | Referencia |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| Matriz resumen de registros/evidencias | Vista consolidada dentro del procedimiento | Salida de control |
| Matriz operativa anexa | Seguimiento detallado por ronda, evento, formato o CSV conservado como evidencia | Anexo operativo |
| `P-PSEA-02` | Referencia cruzada con matriz documental | Referencia |
| `F-PSEA-13` | Informe que consolida evidencias | Salida |

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `P-PSEA-02` | Diferencia de alcance / Referencia | Obligatorio |
| `P-PSEA-08` | Flujo de datos y anexos CSV, de los cuales algunos alimentan registros/evidencias | Obligatorio |
| `F-PSEA-11` | Registro de H/E como evidencia | Obligatorio |
| `F-PSEA-10` | Registro de preprocesamiento como evidencia | Obligatorio |

---

## Limites y riesgos

#### Limites de alcance

- No lista procedimientos, instructivos ni aplicativos como catalogo documental (eso es `P-PSEA-02`).
- No describe el flujo tecnico interno de los CSV ni del preprocesador (eso va en `P-PSEA-08`).
- No reemplaza el control documental institucional ni la gestion macro de versiones.
- No define criterios estadisticos ni reglas de decision.

#### Riesgos de interpretacion

- **Confundir con P-PSEA-02:** `P-PSEA-03` es evidencia por ronda; `P-PSEA-02` es catalogo de documentos.
- **Promover archivos tecnicos a F-PSEA:** Los archivos tecnicos internos del preprocesador se describen como anexos de flujo en `P-PSEA-08`; `P-PSEA-03` solo los trackea cuando quedan como registros o evidencias conservadas.
- **Incluir aplicativos como evidencia:** Los aplicativos (`DG-PSEA-02`, `DG-PSEA-03`) no son registros de ronda.
- **Reducir el procedimiento a una tabla:** La matriz resumen y la matriz operativa son anexos de control; el documento principal debe conservar reglas de identificacion, responsabilidad, seguimiento y cierre de registros/evidencias.

---

## Criterio minimo de elaboracion

El procedimiento define como se controlan los registros y evidencias del PEA, incluye una matriz resumen para consulta rapida y remite a una matriz operativa anexa donde se trackean, por ronda o evento, los formatos, registros, evidencias y anexos CSV conservados como evidencia, sin duplicar el flujo tecnico descrito en `P-PSEA-08` ni el catalogo documental de `P-PSEA-02`.

## Evidencia de elaboracion

| Campo | Valor |
|---|---|
| **Archivo maestro** | `01_bloque_general/02_procedimientos/P-PSEA-03 Control de registros y evidencias del PEA.md` |
| **Resultado** | Se materializa el procedimiento de control de registros y evidencias con matriz resumen, campos minimos para matriz operativa por ronda y controles especificos para `F-PSEA-02`, `F-PSEA-03` y anexos digitales. |
