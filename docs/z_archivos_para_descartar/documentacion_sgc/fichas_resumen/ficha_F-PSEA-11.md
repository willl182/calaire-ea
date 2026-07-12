# Ficha Resumen: F-PSEA-11

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `F-PSEA-11` |
| **Nombre decidido** | Homogeneidad y estabilidad del item |
| **Tipo documental** | Registro |
| **Estado** | Mantener / Actualizar |
| **Prioridad** | Alta |
| **Clase de ficha** | Ficha activa |

---

## Proposito y rol

### Proposito operativo

Registro principal de la evaluacion de homogeneidad y estabilidad del item de ensayo gaseoso. Integra los resultados de los subformatos `F-PSEA-11C` (resultados de homogeneidad) y `F-PSEA-11D` (resultados de estabilidad), y sirve como evidencia de que el item cumple con los criterios metrologicos para la ronda. No debe afirmarse que H/E no aplica.

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

- [ ] `calaire-app`
- [x] `pt_app`
- [ ] Ambos
- [ ] Ninguno

Los resultados de H/E se generan en `pt_app`.

---

## Flujo de datos

#### Entradas principales

| Codigo / fuente | Descripcion | Rol en el flujo |
|---|---|---|
| `F-PSEA-11C` | Resultados de homogeneidad | Insumo |
| `F-PSEA-11D` | Resultados de estabilidad | Insumo |
| `F-PSEA-07` | Preparacion y control del item | Referencia |
| `P-PSEA-07` | Criterio estadistico de H/E | Referencia |
| `P-PSEA-06` | Preparacion del item | Referencia |
| `P-PSEA-08` | Flujo de datos del PEA | Referencia |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| `F-PSEA-13` | Informe final (referencia H/E) | Referencia |
| `P-PSEA-10` a `P-PSEA-13` | Procedimientos por analito (citan H/E) | Referencia |

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `F-PSEA-11C` | Resultados de homogeneidad integrados | Obligatorio |
| `F-PSEA-11D` | Resultados de estabilidad integrados | Obligatorio |
| `F-PSEA-07` | Preparacion del item referenciada | Obligatorio |
| `P-PSEA-07` | Criterio estadistico aplicado | Obligatorio |
| `P-PSEA-06` | Procedimiento de preparacion del item | Obligatorio |
| `P-PSEA-08` | Flujo tecnico de datos digitales | Obligatorio |
| `P-PSEA-10` a `P-PSEA-13` | Procedimientos por analito que citan H/E | Referencia |

---

## Limites y riesgos

#### Limites de alcance

- No contiene datos preprocesados (eso es `F-PSEA-11A` y `F-PSEA-11B`); contiene resultados.
- No define criterios estadisticos (eso es `P-PSEA-07`); aplica los criterios.
- No es el dossier de preparacion del item (eso es `F-PSEA-07`).
- No es un instructivo de uso.

#### Riesgos de interpretacion

- **Afirmar que H/E no aplica:** H/E si aplica y se documenta en este registro y sus subformatos.
- **Confundir con F-PSEA-11A/B:** `F-PSEA-11A` y `F-PSEA-11B` contienen datos preprocesados; `F-PSEA-11` integra resultados.
- **Confundir con F-PSEA-07:** `F-PSEA-07` documenta preparacion; `F-PSEA-11` documenta evaluacion de H/E.
- **Omitir criterio estadistico:** Debe indicar claramente el criterio aplicado (cita `P-PSEA-07`).

---

## Criterio minimo de elaboracion

El registro principal de H/E integra `F-PSEA-11C` y `F-PSEA-11D`, referencia `F-PSEA-07` y `P-PSEA-06`, aplica criterios de `P-PSEA-07`, y se cita desde procedimientos por analito, sin afirmar que H/E no aplica.
