# Ficha Resumen: P-PSEA-09

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `P-PSEA-09` |
| **Nombre decidido** | Planificacion de ronda EA |
| **Tipo documental** | Procedimiento |
| **Estado** | Actualizar |
| **Prioridad** | Alta |
| **Clase de ficha** | Ficha activa |

---

## Proposito y rol

### Proposito operativo

Gobierna la planificacion de una ronda de ensayo de aptitud, incluyendo definicion de alcance, seleccion de participantes, calendario, cronograma, item de ensayo, niveles de concentracion y matriz de criterios de ISO/IEC 17043:2023 7.2.1.3 (nota/matriz A-U). La planificacion se soporta en `calaire-app` y en formatos exportables.

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
- [ ] `pt_app`
- [ ] Ambos
- [ ] Ninguno

La planificacion se ejecuta principalmente en `calaire-app`.

---

## Flujo de datos

#### Entradas principales

| Codigo / fuente | Descripcion | Rol en el flujo |
|---|---|---|
| `F-PSEA-01` | Calendario global de ronda | Insumo |
| `F-PSEA-02` | Cronograma detallado de ronda | Insumo |
| `F-PSEA-06` | Plan de ronda EA | Producto |
| `F-PSEA-07` | Ficha digital de ronda | Insumo / Producto |
| `F-PSEA-08` | Preparacion y control del item | Referencia |
| ISO/IEC 17043:2023 7.2.1.3 | Nota/matriz A-U | Referencia externa |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| `F-PSEA-06` | Plan de ronda consolidado | Producto |
| `F-PSEA-07` | Ficha digital de ronda | Producto |
| `P-PSEA-10` | Preparacion y control del item | Referencia |

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `DG-PSEA-02` | Aplicativo que soporta la planificacion | Obligatorio |
| `I-PSEA-16` | Instructivo de administracion de rondas | Obligatorio |
| `P-PSEA-10` | Preparacion del item que debe planificarse | Obligatorio |
| `F-PSEA-06` | Plan de ronda que este procedimiento produce | Obligatorio |
| `F-PSEA-07` | Ficha digital que este procedimiento produce | Obligatorio |
| `P-PSEA-08` | Colusion y falsificacion (medidas preventivas en plan) | Referencia |

---

## Limites y riesgos

#### Limites de alcance

- No es un instructivo de uso de `calaire-app` (eso es `I-PSEA-16`).
- No define criterios estadisticos (eso es `P-PSEA-06`).
- No es un procedimiento de preparacion del item (eso es `P-PSEA-10`).
- No incluye comunicaciones a participantes (eso es `P-PSEA-20`).

#### Riesgos de interpretacion

- **Confundir con F-PSEA-06:** `F-PSEA-06` es el plan de ronda como formato/registro; `P-PSEA-09` es el procedimiento que gobierna como planificar.
- **Omitir nota A-U:** La planificacion debe incluir o referenciar la nota/matriz A-U de ISO/IEC 17043:2023 7.2.1.3.
- **Describir funciones de calaire-app:** Las funciones del aplicativo se documentan en `DG-PSEA-02` e `I-PSEA-16`; este procedimiento gobierna la actividad de planificacion.
- **Incluir analisis estadistico:** El analisis ocurre despues de la planificacion y ejecucion, bajo `P-PSEA-06` y `P-PSEA-07`.

---

## Criterio minimo de elaboracion

El procedimiento define los pasos de planificacion, alcance, participantes, calendario, item, niveles y nota A-U, citando `calaire-app` como soporte y `F-PSEA-06` como producto, sin duplicar instructivos ni criterios estadisticos.
