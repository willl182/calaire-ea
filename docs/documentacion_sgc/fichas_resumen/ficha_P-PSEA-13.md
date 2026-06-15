# Ficha Resumen: P-PSEA-13

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `P-PSEA-13` |
| **Nombre decidido** | Procedimiento tecnico SO2 |
| **Tipo documental** | Procedimiento |
| **Estado** | Actualizar |
| **Prioridad** | Media |
| **Clase de ficha** | Ficha activa |

---

## Proposito y rol

### Proposito operativo

Procedimiento tecnico especifico para la evaluacion de aptitud en dioxido de azufre (SO2) dentro del PEA. Documenta las condiciones operativas, metodologias de referencia, particularidades del gas y criterios de aceptacion especificos para este analito. Debe citar documentos transversales y no duplicar estadistica, H/E, informe ni flujo de datos.

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
| `P-PSEA-07` | Diseno estadistico | Referencia obligatoria |
| `F-PSEA-11` | Registro de H/E | Referencia obligatoria |
| `P-PSEA-06` | Preparacion del item | Referencia |
| `F-PSEA-12` | Dataset oficial | Referencia |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| `P-PSEA-09` | Informe de resultados | Referencia |
| `F-PSEA-13` | Informe final | Referencia |

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `P-PSEA-07` | Cita para diseno estadistico | Obligatorio |
| `F-PSEA-11` | Cita para H/E | Obligatorio |
| `P-PSEA-09` | Cita para informe | Obligatorio |
| `P-PSEA-08` | Cita para flujo de datos | Obligatorio |
| `DG-PSEA-03` | Aplicativo de analisis | Referencia |
| `I-PSEA-04` | Instructivo de preprocesador | Referencia |
| `I-PSEA-05` | Instructivo de analisis | Referencia |

---

## Limites y riesgos

#### Limites de alcance

- No duplica el diseno estadistico (eso es `P-PSEA-07`).
- No duplica la evaluacion de H/E (eso es `F-PSEA-11` y `P-PSEA-07`).
- No duplica la generacion del informe (eso es `P-PSEA-09`).
- No duplica el flujo de datos (eso es `P-PSEA-08`).
- No es un instructivo de uso de aplicativos.

#### Riesgos de interpretacion

- **Duplicar P-PSEA-07:** El procedimiento debe citar `P-PSEA-07` para estadistica, no replicar definiciones.
- **Omitir particularidades de SO2:** Debe conservar las condiciones especificas de este gas (fluorescencia UV, interferencias, etc.).
- **Incluir H/E como procedimiento separado:** La evaluacion de H/E se documenta en `F-PSEA-11` y `P-PSEA-07`; aqui solo se cita.
- **Confundir con F-PSEA-13:** Este procedimiento no define el formato del informe; cita `P-PSEA-09` y `F-PSEA-13`.

---

## Criterio minimo de elaboracion

El procedimiento tecnico para SO2 contiene las condiciones especificas del analito, citando `P-PSEA-07`, `F-PSEA-11`, `P-PSEA-09` y `P-PSEA-08` sin duplicar estadistica, H/E, informe ni flujo de datos.
