# Ficha Resumen: P-PSEA-03

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `P-PSEA-03` |
| **Nombre decidido** | Matriz de registros y evidencias del PEA |
| **Tipo documental** | Matriz |
| **Estado** | Elaborar |
| **Prioridad** | Alta |
| **Clase de ficha** | Ficha activa |

---

## Proposito y rol

### Proposito operativo

Lista los registros y evidencias generadas por cada ronda o evento del PEA. Identifica que formatos y registros se producen, quien los genera, desde que aplicativo y cual es su destino. Es la contraparte operativa de `P-PSEA-02` (matriz documental).

### Rol en el flujo

- [x] Matriz
- [x] Evidencia
- [ ] Entrada
- [ ] Salida
- [ ] Registro oficial
- [ ] Criterio tecnico
- [ ] Instructivo
- [ ] Soporte documental

Funciona como mapa de evidencias y registro de trazabilidad operativa.

---

## Aplicativos y tecnologia

#### Aplicativo asociado

- [x] `calaire-app`
- [x] `pt_app`
- [ ] Ambos
- [ ] Ninguno

Genera registros desde ambos aplicativos; la matriz los cataloga.

---

## Flujo de datos

#### Entradas principales

| Codigo / fuente | Descripcion | Rol en el flujo |
|---|---|---|
| Ronda o evento PEA | Ejecucion de una ronda piloto o EA | Insumo |
| `F-PSEA-01` a `F-PSEA-12` | Formatos generados durante la ronda | Referencia |
| `P-PSEA-06` | Preparacion y control del item | Referencia |
| `P-PSEA-08` | Flujo tecnico de datos | Referencia |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| `P-PSEA-02` | Referencia cruzada con matriz documental | Referencia |
| Auditorias internas | Evidencia de registros generados | Evidencia |
| `F-PSEA-13` | Informe que consolida evidencias | Salida |

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `P-PSEA-02` | Diferencia de alcance / Referencia | Obligatorio |
| `P-PSEA-08` | Flujo de datos que alimenta registros | Obligatorio |
| `F-PSEA-11` | Registro de H/E como evidencia | Obligatorio |
| `F-PSEA-10` | Registro de preprocesamiento como evidencia | Obligatorio |

---

## Limites y riesgos

#### Limites de alcance

- No lista procedimientos, instructivos ni aplicativos (eso es `P-PSEA-02`).
- No lista archivos tecnicos internos del preprocesador (van en `P-PSEA-08`).
- No define criterios de aprobacion, retencion ni obsolescencia.
- No es un procedimiento de control documental macro.

#### Riesgos de interpretacion

- **Confundir con P-PSEA-02:** `P-PSEA-03` es evidencia por ronda; `P-PSEA-02` es catalogo de documentos.
- **Promover archivos tecnicos a F-PSEA:** Los archivos tecnicos internos del preprocesador deben quedar en `P-PSEA-08`, no en esta matriz ni como formatos.
- **Incluir aplicativos como evidencia:** Los aplicativos (`DG-PSEA-02`, `DG-PSEA-03`) no son registros de ronda.

---

## Criterio minimo de elaboracion

La matriz de registros y evidencias lista, para cada tipo de ronda o evento, los formatos y registros generados, su aplicativo de origen, su destino y su estado documental, sin incluir archivos tecnicos internos ni aplicativos.
