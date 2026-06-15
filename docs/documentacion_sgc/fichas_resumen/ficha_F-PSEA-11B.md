# Ficha Resumen: F-PSEA-11B

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `F-PSEA-11B` |
| **Nombre decidido** | Datos preprocesados de estabilidad |
| **Tipo documental** | Formato |
| **Estado** | Elaborar |
| **Prioridad** | Alta |
| **Clase de ficha** | Ficha activa |

---

## Proposito y rol

### Proposito operativo

Subformato que contiene los datos de estabilidad del item de ensayo despues del preprocesamiento en `pt_app`. Es un insumo tecnico para el modulo de analisis y se alimenta de archivos tecnicos internos de estabilidad.

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

Generado por el preprocesador de `pt_app`.

---

## Flujo de datos

#### Entradas principales

| Codigo / fuente | Descripcion | Rol en el flujo |
|---|---|---|
| Archivos tecnicos internos | Datos crudos de estabilidad | Insumo tecnico |
| `F-PSEA-10` | Registro de preprocesamiento | Referencia |
| `I-PSEA-04` | Instructivo de preprocesador | Referencia |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| `F-PSEA-11D` | Resultados de estabilidad | Entrada para analisis |
| `F-PSEA-12` | Dataset oficial consolidado | Referencia |

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `F-PSEA-11` | Registro principal de H/E | Obligatorio |
| `F-PSEA-11D` | Resultados de estabilidad que se alimentan de estos datos | Obligatorio |
| `P-PSEA-07` | Criterio estadistico de H/E | Referencia |
| `P-PSEA-06` | Preparacion y control del item | Referencia |
| `P-PSEA-08` | Flujo tecnico de datos digitales | Obligatorio |
| `I-PSEA-04` | Instructivo de preprocesamiento | Referencia |

---

## Limites y riesgos

#### Limites de alcance

- No contiene resultados finales de estabilidad (eso es `F-PSEA-11D`).
- No es un registro de preprocesamiento (eso es `F-PSEA-10`).
- No define criterios estadisticos (eso es `P-PSEA-07`).
- No es un instructivo de uso.

#### Riesgos de interpretacion

- **Confundir con F-PSEA-11D:** `F-PSEA-11B` contiene datos preprocesados; `F-PSEA-11D` contiene resultados de analisis.
- **Confundir con F-PSEA-11:** `F-PSEA-11` es el registro principal de H/E; `F-PSEA-11B` es un subformato especifico de datos preprocesados.
- **Omitir trazabilidad:** Debe vincularse con el registro de preprocesamiento (`F-PSEA-10`) y el item de ensayo (`P-PSEA-06`).

---

## Criterio minimo de elaboracion

El subformato contiene datos preprocesados de estabilidad con trazabilidad al item de ensayo, al registro de preprocesamiento y al criterio estadistico aplicado, sin incluir resultados finales ni datos crudos sin procesar.
