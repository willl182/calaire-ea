# Ficha Resumen: P-PSEA-04

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `P-PSEA-04` |
| **Nombre decidido** | Procedimiento tecnico O3 |
| **Tipo documental** | Procedimiento |
| **Estado** | Actualizar |
| **Prioridad** | Media |
| **Clase de ficha** | Ficha activa |

---

## Proposito y rol

### Proposito operativo

Procedimiento tecnico especifico para la evaluacion de aptitud en ozono (O3) dentro del PEA. Documenta las condiciones operativas, metodologias de referencia, particularidades del gas y criterios de aceptacion especificos para este analito. Requiere correccion de referencias internas antiguas y duplicaciones. Debe citar documentos transversales y no duplicar estadistica, H/E, informe ni flujo de datos.

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

- [ ] `calaire-app`
- [x] `pt_app`
- [ ] Ambos
- [ ] Ninguno

El analisis estadistico se ejecuta en `pt_app`, pero este procedimiento define criterios especificos del analito.

---

## Flujo de datos

#### Entradas principales

| Codigo / fuente | Descripcion | Rol en el flujo |
|---|---|---|
| `P-PSEA-06` | Diseno estadistico | Referencia obligatoria |
| `F-PSEA-13` | Registro de H/E | Referencia obligatoria |
| `P-PSEA-10` | Preparacion del item | Referencia |
| `F-PSEA-14` | Dataset oficial | Referencia |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| `P-PSEA-07` | Informe de resultados | Referencia |
| `F-PSEA-04` | Informe final | Referencia |

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `P-PSEA-06` | Cita para diseno estadistico | Obligatorio |
| `F-PSEA-13` | Cita para H/E | Obligatorio |
| `P-PSEA-07` | Cita para informe | Obligatorio |
| `P-PSEA-23` | Cita para flujo de datos | Obligatorio |
| `DG-PSEA-03` | Aplicativo de analisis | Referencia |
| `I-PSEA-17` | Instructivo de preprocesador | Referencia |
| `I-PSEA-18` | Instructivo de analisis | Referencia |

---

## Limites y riesgos

#### Limites de alcance

- No duplica el diseno estadistico (eso es `P-PSEA-06`).
- No duplica la evaluacion de H/E (eso es `F-PSEA-13` y `P-PSEA-06`).
- No duplica la generacion del informe (eso es `P-PSEA-07`).
- No duplica el flujo de datos (eso es `P-PSEA-23`).
- No es un instructivo de uso de aplicativos.

#### Riesgos de interpretacion

- **Duplicar P-PSEA-06:** El procedimiento debe citar `P-PSEA-06` para estadistica, no replicar definiciones.
- **Omitir correcciones necesarias:** Debe corregir referencias internas antiguas y duplicaciones existentes.
- **Omitir particularidades de O3:** Debe conservar las condiciones especificas de este gas (inestabilidad, fotolisis, etc.).
- **Incluir H/E como procedimiento separado:** La evaluacion de H/E se documenta en `F-PSEA-13` y `P-PSEA-06`; aqui solo se cita.
- **Confundir con F-PSEA-04:** Este procedimiento no define el formato del informe; cita `P-PSEA-07` y `F-PSEA-04`.

---

## Criterio minimo de elaboracion

El procedimiento tecnico para O3 contiene las condiciones especificas del analito, corrige referencias antiguas, y cita `P-PSEA-06`, `F-PSEA-13`, `P-PSEA-07` y `P-PSEA-23` sin duplicar estadistica, H/E, informe ni flujo de datos.
