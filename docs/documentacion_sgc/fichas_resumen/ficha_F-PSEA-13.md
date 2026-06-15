# Ficha Resumen: F-PSEA-13

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `F-PSEA-13` |
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
| `F-PSEA-12` | Dataset oficial consolidado | Insumo |
| `F-PSEA-11C` | Resultados de homogeneidad | Insumo |
| `F-PSEA-11D` | Resultados de estabilidad | Insumo |
| `P-PSEA-07` | Criterio estadistico aplicado | Referencia |
| `P-PSEA-09` | Procedimiento de generacion del informe | Referencia |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| Participantes | Comunicacion de resultados | Producto |
| `P-PSEA-16` | Control de valores sensibles | Referencia |

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `P-PSEA-09` | Procedimiento que gobierna su generacion | Obligatorio |
| `P-PSEA-07` | Criterio estadistico que debe presentar | Obligatorio |
| `DG-PSEA-03` | Aplicativo que lo genera | Obligatorio |
| `I-PSEA-05` | Instructivo que explica la operacion | Obligatorio |
| `F-PSEA-12` | Dataset que alimenta el informe | Obligatorio |
| `P-PSEA-16` | Control de valores sensibles al emitir | Obligatorio |

---

## Limites y riesgos

#### Limites de alcance

- No se define aun el contenido detallado del informe; esta ficha es preliminar.
- No es el criterio estadistico (eso es `P-PSEA-07`); es la presentacion de resultados.
- No es el procedimiento de generacion (eso es `P-PSEA-09`); es el formato del producto.
- No es un instructivo de uso de `pt_app`.

#### Riesgos de interpretacion

- **Cerrar prematuramente el contenido:** El contenido detallado del informe se definira en fase posterior; por ahora se documenta su rol y entradas/salidas.
- **Confundir con P-PSEA-09:** `P-PSEA-09` gobierna el proceso; `F-PSEA-13` es el formato del producto.
- **Omitir control de valores sensibles:** La emision del informe debe conectar con `P-PSEA-16`.
- **Incluir datos crudos:** El informe presenta resultados, no datos crudos ni preprocesados.

---

## Criterio minimo de elaboracion

El formato del informe se identifica como producto final de `pt_app`, con entradas oficiales (`F-PSEA-12`, `F-PSEA-11C`, `F-PSEA-11D`), procedimiento de generacion (`P-PSEA-09`) y criterio estadistico (`P-PSEA-07`), manteniendo su contenido detallado como preliminar hasta nueva fase de definicion.
