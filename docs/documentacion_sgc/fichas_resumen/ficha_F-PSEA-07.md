# Ficha Resumen: F-PSEA-07

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `F-PSEA-07` |
| **Nombre decidido** | Preparacion y control del item |
| **Tipo documental** | Formato |
| **Estado** | Mantener / Actualizar |
| **Prioridad** | Media |
| **Clase de ficha** | Ficha activa |

---

## Proposito y rol

### Proposito operativo

Dossier o registro de la preparacion y control del item de ensayo gaseoso. Documenta las condiciones de generacion, niveles de concentracion, controles realizados, trazabilidad del calibrador dinamico y del cilindro, y evidencia de que el item cumple con los requisitos para la ronda. Se genera desde la operacion tecnica y se referencia en `P-PSEA-06`.

### Rol en el flujo

- [x] Registro oficial
- [x] Evidencia
- [ ] Entrada
- [ ] Salida
- [ ] Criterio tecnico
- [ ] Instructivo
- [ ] Matriz
- [ ] Soporte documental

---

## Aplicativos y tecnologia

#### Aplicativo asociado

- [x] `calaire-app`
- [ ] `pt_app`
- [ ] Ambos
- [ ] Ninguno

Los niveles se definen en `calaire-app`; el registro se genera desde la operacion tecnica.

---

## Flujo de datos

#### Entradas principales

| Codigo / fuente | Descripcion | Rol en el flujo |
|---|---|---|
| `P-PSEA-06` | Preparacion y control del item (procedimiento) | Referencia |
| `calaire-app` | Niveles de concentracion definidos | Insumo |
| Calibrador dinamico | Datos de generacion de concentraciones | Insumo tecnico |
| Cilindro de gas | Datos de trazabilidad | Insumo tecnico |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| `F-PSEA-05` | Plan de ronda (referencia al item) | Referencia |
| `F-PSEA-11` | Registro de H/E del item | Referencia |
| `P-PSEA-07` | Criterio estadistico de H/E | Referencia |

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `P-PSEA-06` | Procedimiento que gobierna la preparacion | Obligatorio |
| `F-PSEA-11` | Registro de H/E del item | Obligatorio |
| `F-PSEA-05` | Plan de ronda que referencia al item | Obligatorio |
| `P-PSEA-07` | Criterio estadistico de H/E | Referencia |
| `DG-PSEA-02` | Aplicativo donde se definen niveles | Obligatorio |

---

## Limites y riesgos

#### Limites de alcance

- No es el procedimiento de preparacion (eso es `P-PSEA-06`); es el registro/dossier.
- No es el registro de H/E (eso es `F-PSEA-11`); es el registro de preparacion del item.
- No contiene datos de participantes.
- No es un instructivo de uso de equipos.

#### Riesgos de interpretacion

- **Confundir con P-PSEA-06:** `P-PSEA-06` es el procedimiento; `F-PSEA-07` es el registro que resulta.
- **Confundir con F-PSEA-11:** `F-PSEA-07` documenta preparacion; `F-PSEA-11` documenta H/E.
- **Omitir trazabilidad:** Debe incluir trazabilidad del calibrador dinamico y del cilindro.
- **Omitir niveles de calaire-app:** Los niveles deben referenciarse a los definidos en `calaire-app`.

---

## Criterio minimo de elaboracion

El dossier de preparacion del item contiene condiciones de generacion, niveles, controles, trazabilidad del calibrador y cilindro, vinculado con `P-PSEA-06` y `F-PSEA-11`, sin duplicar procedimientos ni criterios estadisticos.
