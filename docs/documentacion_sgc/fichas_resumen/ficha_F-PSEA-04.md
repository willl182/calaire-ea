# Ficha Resumen: F-PSEA-04

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `F-PSEA-04` |
| **Nombre decidido** | Informe final de resultados |
| **Tipo documental** | Formato |
| **Estado** | Mantener / Actualizar |
| **Prioridad** | Media-alta |
| **Clase de ficha** | Ficha preliminar |

---

## Proposito y rol

### Proposito operativo

Formato del informe final de resultados del PEA, generado desde el modulo de analisis de `pt_app`. Presenta los resultados de la evaluacion de aptitud a los participantes, incluyendo valor asignado, `sigma_pt`, desempeno de cada laboratorio, y referencia a criterios estadisticos. Su contenido detallado no se define en esta fase.

### Rol en el flujo

- [x] Salida
- [x] Evidencia
- [ ] Entrada
- [ ] Registro oficial
- [ ] Criterio tecnico
- [ ] Instructivo
- [ ] Matriz
- [ ] Soporte documental

---

## Aplicativos y tecnologia

#### Aplicativo asociado

- [ ] `calaire-app`
- [x] `pt_app`
- [ ] Ambos
- [ ] Ninguno

Generado desde el modulo de analisis de `pt_app`.

---

## Flujo de datos

#### Entradas principales

| Codigo / fuente | Descripcion | Rol en el flujo |
|---|---|---|
| `F-PSEA-14` | Dataset oficial consolidado | Insumo |
| `F-PSEA-13C` | Resultados de homogeneidad | Insumo |
| `F-PSEA-13D` | Resultados de estabilidad | Insumo |
| `P-PSEA-06` | Criterio estadistico aplicado | Referencia |
| `P-PSEA-07` | Procedimiento de generacion del informe | Referencia |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| Participantes | Comunicacion de resultados | Producto |
| `P-PSEA-21` | Control de valores sensibles | Referencia |

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `P-PSEA-07` | Procedimiento que gobierna su generacion | Obligatorio |
| `P-PSEA-06` | Criterio estadistico que debe presentar | Obligatorio |
| `DG-PSEA-03` | Aplicativo que lo genera | Obligatorio |
| `I-PSEA-18` | Instructivo que explica la operacion | Obligatorio |
| `F-PSEA-14` | Dataset que alimenta el informe | Obligatorio |
| `P-PSEA-21` | Control de valores sensibles al emitir | Obligatorio |

---

## Limites y riesgos

#### Limites de alcance

- No se define aun el contenido detallado del informe; esta ficha es preliminar.
- No es el criterio estadistico (eso es `P-PSEA-06`); es la presentacion de resultados.
- No es el procedimiento de generacion (eso es `P-PSEA-07`); es el formato del producto.
- No es un instructivo de uso de `pt_app`.

#### Riesgos de interpretacion

- **Cerrar prematuramente el contenido:** El contenido detallado del informe se definira en fase posterior; por ahora se documenta su rol y entradas/salidas.
- **Confundir con P-PSEA-07:** `P-PSEA-07` gobierna el proceso; `F-PSEA-04` es el formato del producto.
- **Omitir control de valores sensibles:** La emision del informe debe conectar con `P-PSEA-21`.
- **Incluir datos crudos:** El informe presenta resultados, no datos crudos ni preprocesados.

---

## Criterio minimo de elaboracion

El formato del informe se identifica como producto final de `pt_app`, con entradas oficiales (`F-PSEA-14`, `F-PSEA-13C`, `F-PSEA-13D`), procedimiento de generacion (`P-PSEA-07`) y criterio estadistico (`P-PSEA-06`), manteniendo su contenido detallado como preliminar hasta nueva fase de definicion.
