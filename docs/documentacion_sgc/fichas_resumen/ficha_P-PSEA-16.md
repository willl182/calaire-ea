# Ficha Resumen: P-PSEA-16

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `P-PSEA-16` |
| **Nombre decidido** | Divulgacion y control de valores sensibles |
| **Tipo documental** | Procedimiento |
| **Estado** | Mantener / Actualizar |
| **Prioridad** | Media-alta |
| **Clase de ficha** | Ficha activa |

---

## Proposito y rol

### Proposito operativo

Gobierna el control de divulgacion de niveles de concentracion, valor asignado (`x_pt`), desviacion estandar (`sigma_pt`), valores de referencia y resultados agregados de laboratorios antes, durante y despues de una ronda. Conecta con colusion, confidencialidad, comunicaciones y generacion del informe.

### Rol en el flujo

- [x] Criterio tecnico
- [x] Procedimiento
- [ ] Entrada
- [ ] Salida
- [ ] Registro oficial
- [ ] Evidencia
- [ ] Instructivo
- [ ] Matriz
- [ ] Soporte documental

---

## Aplicativos y tecnologia

#### Aplicativo asociado

- [x] `calaire-app`
- [x] `pt_app`
- [ ] Ambos
- [ ] Ninguno

Ambos aplicativos contienen valores sensibles; este procedimiento gobierna su control.

---

## Flujo de datos

#### Entradas principales

| Codigo / fuente | Descripcion | Rol en el flujo |
|---|---|---|
| `P-PSEA-07` | Valor asignado y `sigma_pt` | Referencia |
| `F-PSEA-13` | Informe final (control de emision) | Referencia |
| `P-PSEA-14` | Colusion y falsificacion | Referencia |
| `P-PSEA-19` | Confidencialidad operativa | Referencia |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| `P-PSEA-05` | Comunicaciones (control de divulgacion) | Referencia |
| `P-PSEA-18` | Apelaciones (acceso controlado) | Referencia |
| `F-PSEA-13` | Informe (emision controlada) | Referencia |

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `P-PSEA-07` | Valores sensibles generados | Obligatorio |
| `P-PSEA-14` | Colusion que compromete valores | Obligatorio |
| `P-PSEA-19` | Confidencialidad que protege valores | Obligatorio |
| `P-PSEA-05` | Comunicaciones que divulgan valores | Obligatorio |
| `P-PSEA-09` | Generacion del informe (control de emision) | Obligatorio |
| `F-PSEA-13` | Informe final (control de divulgacion) | Obligatorio |

---

## Limites y riesgos

#### Limites de alcance

- No es un procedimiento de confidencialidad general (eso es `P-PSEA-19`); conecta con el.
- No es un procedimiento de colusion (eso es `P-PSEA-14`); conecta con el.
- No es un procedimiento de comunicaciones (eso es `P-PSEA-05`); conecta con el.
- No define criterios estadisticos (eso es `P-PSEA-07`); gobierna su divulgacion.

#### Riesgos de interpretacion

- **Confundir con P-PSEA-19:** `P-PSEA-19` es confidencialidad operativa; `P-PSEA-16` es control especifico de valores sensibles.
- **Omitir niveles de calaire-app:** Los niveles definidos en `calaire-app` son sensibles antes de la ronda.
- **Omitir control de resultados agregados:** Los resultados individuales de laboratorios son sensibles hasta la emision oficial.
- **Divulgar prematuramente:** El procedimiento debe definir claramente el momento de emision autorizada.

---

## Criterio minimo de elaboracion

El procedimiento define que valores son sensibles, quien puede acceder a ellos, en que momento, por que canal, y conexion con `P-PSEA-07`, `P-PSEA-14`, `P-PSEA-19`, `P-PSEA-05` y `P-PSEA-09`, sin duplicar confidencialidad ni colusion.
