# Ficha Resumen: F-PSEA-13D

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `F-PSEA-13D` |
| **Nombre decidido** | Resultados de estabilidad |
| **Tipo documental** | Formato |
| **Estado** | Elaborar |
| **Prioridad** | Alta |
| **Clase de ficha** | Ficha activa |

---

## Proposito y rol

### Proposito operativo

Subformato que contiene los resultados de la evaluacion de estabilidad del item de ensayo, exportados desde el modulo de analisis de `pt_app`. Es la evidencia de que el item cumple con los criterios de estabilidad definidos en `P-PSEA-06` y se integra en el informe final.

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

Generado por el modulo de analisis de `pt_app`.

---

## Flujo de datos

#### Entradas principales

| Codigo / fuente | Descripcion | Rol en el flujo |
|---|---|---|
| `F-PSEA-13B` | Datos preprocesados de estabilidad | Insumo |
| `P-PSEA-06` | Criterio estadistico de H/E | Referencia |
| `I-PSEA-18` | Instructivo de modulo de analisis | Referencia |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| `F-PSEA-04` | Informe final de resultados | Entrada |
| `F-PSEA-13` | Registro principal de H/E | Referencia |

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `F-PSEA-13` | Registro principal de H/E | Obligatorio |
| `F-PSEA-13B` | Datos preprocesados que alimentan este resultado | Obligatorio |
| `P-PSEA-06` | Criterio estadistico aplicado | Referencia |
| `P-PSEA-10` | Preparacion y control del item | Referencia |
| `P-PSEA-23` | Flujo tecnico de datos digitales | Obligatorio |
| `I-PSEA-18` | Instructivo de modulo de analisis | Referencia |

---

## Limites y riesgos

#### Limites de alcance

- No contiene datos preprocesados (eso es `F-PSEA-13B`).
- No es un registro de preprocesamiento (eso es `F-PSEA-10`).
- No define criterios estadisticos (eso es `P-PSEA-06`).
- No es un instructivo de uso.

#### Riesgos de interpretacion

- **Confundir con F-PSEA-13B:** `F-PSEA-13B` contiene datos preprocesados; `F-PSEA-13D` contiene resultados de analisis.
- **Confundir con F-PSEA-13:** `F-PSEA-13` es el registro principal de H/E; `F-PSEA-13D` es un subformato especifico de resultados.
- **Omitir criterio estadistico:** Los resultados deben indicar claramente el criterio estadistico aplicado (cita `P-PSEA-06`).

---

## Criterio minimo de elaboracion

El subformato contiene resultados de estabilidad con trazabilidad a los datos preprocesados (`F-PSEA-13B`), al criterio estadistico (`P-PSEA-06`) y al informe final (`F-PSEA-04`), sin incluir datos crudos ni preprocesados.
