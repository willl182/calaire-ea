# Ficha Resumen: P-PSEA-06

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `P-PSEA-06` |
| **Nombre decidido** | Preparacion y control del item de ensayo gaseoso |
| **Tipo documental** | Procedimiento |
| **Estado** | Elaborar / Actualizar |
| **Prioridad** | Alta |
| **Clase de ficha** | Ficha activa |

---

## Proposito y rol

### Proposito operativo

Gobierna la preparacion y control del item de ensayo gaseoso para el PEA, incluyendo la generacion de concentraciones mediante calibrador dinamico y cilindro de gas, tomando niveles definidos desde `calaire-app`. Documenta las condiciones, controles y registros necesarios para garantizar que el item es adecuado para la evaluacion de aptitud.

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

`calaire-app` actua como fuente de referencia para los niveles de concentracion definidos en la ronda; `pt_app` actua como aplicativo de evaluacion de H/E. El procedimiento no convierte a ninguno de los dos aplicativos en formato ni sustituye sus instructivos de uso.

---

## Flujo de datos

#### Entradas principales

| Codigo / fuente | Descripcion | Rol en el flujo |
|---|---|---|
| `calaire-app` | Niveles de concentracion definidos | Insumo |
| Calibrador dinamico | Equipo de generacion de concentraciones | Insumo tecnico |
| Cilindro de gas | Fuente de gas patron | Insumo tecnico |
| `P-PSEA-04` | Planificacion de ronda | Referencia |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| `F-PSEA-07` | Dossier/registro de preparacion y control del item | Registro oficial |
| `F-PSEA-11` | Registro de homogeneidad y estabilidad | Registro oficial |
| `F-PSEA-11A` | Datos preprocesados de homogeneidad | Salida |
| `F-PSEA-11B` | Datos preprocesados de estabilidad | Salida |

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `P-PSEA-07` | Criterio estadistico de H/E | Obligatorio |
| `P-PSEA-04` | Planificacion que define el item y niveles | Obligatorio |
| `P-PSEA-08` | Flujo tecnico que conecta item con datos | Obligatorio |
| `F-PSEA-07` | Registro de preparacion del item | Obligatorio |
| `F-PSEA-11` | Registro de H/E del item | Obligatorio |
| `DG-PSEA-02` | Aplicativo donde se definen niveles | Obligatorio |

---

## Limites y riesgos

#### Limites de alcance

- No es un procedimiento de envio/recepcion fisica de items (el antiguo `P-PSEA-11` no aplica).
- No define criterios estadisticos generales (eso es `P-PSEA-07`); aplica criterios especificos de H/E al item.
- No es un instructivo de uso de equipos.
- No incluye gestion de proveedores del cilindro (eso es `P-PSEA-21`).

#### Riesgos de interpretacion

- **Confundir con envio/recepcion:** El PEA de gases no envia items fisicos; el item se genera in situ con calibrador dinamico.
- **Omitir H/E:** Debe documentarse claramente que H/E se evalua y se registra en `F-PSEA-11` y subformatos.
- **Describir niveles en calaire-app:** Los niveles se definen en `calaire-app` pero este procedimiento gobierna su uso operativo en la preparacion.
- **Duplicar P-PSEA-07:** Solo aplica criterios de H/E al item; el diseno estadistico general queda en `P-PSEA-07`.

---

## Criterio minimo de elaboracion

El procedimiento describe la preparacion del item gaseoso, uso de calibrador dinamico y cilindro, niveles desde `calaire-app`, controles, registro en `F-PSEA-07` y evaluacion de H/E en `F-PSEA-11`, sin confundirse con envio fisico ni duplicar criterios estadisticos generales.
