# Ficha Resumen: I-PSEA-18

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `I-PSEA-18` |
| **Nombre decidido** | Instructivo de uso del modulo de analisis PT de `pt_app` |
| **Tipo documental** | Instructivo |
| **Estado** | Elaborar |
| **Prioridad** | Alta |
| **Clase de ficha** | Ficha activa |

---

## Proposito y rol

### Proposito operativo

Explica el uso operativo del modulo de analisis de ensayos de aptitud en `pt_app`, incluyendo carga del dataset consolidado, seleccion de criterios estadisticos, ejecucion de calculos, revision de resultados H/E, generacion de graficos y exportacion del informe. No define criterios estadisticos; describe como operar la herramienta.

### Rol en el flujo

- [x] Instructivo
- [ ] Entrada
- [ ] Salida
- [ ] Registro oficial
- [ ] Evidencia
- [ ] Criterio tecnico
- [ ] Matriz
- [ ] Soporte documental

---

## Aplicativos y tecnologia

#### Aplicativo asociado

- [ ] `calaire-app`
- [x] `pt_app`
- [ ] Ambos
- [ ] Ninguno

Describe el uso operativo del modulo de analisis dentro de `pt_app`.

---

## Flujo de datos

#### Entradas principales

| Codigo / fuente | Descripcion | Rol en el flujo |
|---|---|---|
| `F-PSEA-14` | Dataset oficial consolidado | Insumo |
| `F-PSEA-13A` | Datos preprocesados de homogeneidad | Insumo |
| `F-PSEA-13B` | Datos preprocesados de estabilidad | Insumo |
| `P-PSEA-06` | Criterio estadistico de referencia | Referencia |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| `F-PSEA-04` | Informe final de resultados | Producto |
| `F-PSEA-13C` | Resultados de homogeneidad | Salida |
| `F-PSEA-13D` | Resultados de estabilidad | Salida |

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `DG-PSEA-03` | Documento general del aplicativo | Obligatorio |
| `P-PSEA-23` | Flujo tecnico que contextualiza el paso | Obligatorio |
| `P-PSEA-06` | Criterio estadistico que debe consultarse | Referencia |
| `P-PSEA-07` | Generacion del informe | Referencia |
| `F-PSEA-14` | Dataset que alimenta el analisis | Obligatorio |

---

## Limites y riesgos

#### Limites de alcance

- No reemplaza `P-PSEA-06` (criterio estadistico); solo explica como operar la herramienta.
- No reemplaza `P-PSEA-07` (generacion del informe); complementa la parte operativa.
- No define que es un outlier, como se calcula el valor asignado ni que es `sigma_pt`.
- No es un procedimiento de control de calidad.

#### Riesgos de interpretacion

- **Confundir con P-PSEA-06:** El instructivo explica botones, parametros y pasos; el procedimiento define criterios tecnicos.
- **Confundir con P-PSEA-07:** `P-PSEA-07` gobierna la generacion del informe; `I-PSEA-18` explica la operacion del modulo que lo produce.
- **Describir preprocesamiento:** El preprocesamiento se cubre en `I-PSEA-17`.
- **Omitir referencia a P-PSEA-06:** El usuario debe consultar `P-PSEA-06` para entender los criterios que selecciona en la interfaz.

---

## Criterio minimo de elaboracion

El instructivo describe paso a paso la operacion del modulo de analisis: carga de datos, seleccion de criterios, ejecucion, revision de resultados H/E, exportacion de informe y graficos, sin definir criterios estadisticos ni contenido del informe final.
