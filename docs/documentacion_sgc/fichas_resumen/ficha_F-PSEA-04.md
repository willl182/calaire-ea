# Ficha Resumen: F-PSEA-04

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `F-PSEA-04` |
| **Nombre decidido** | Anexo tecnico de equipos e instrumentos del participante |
| **Tipo documental** | Formato |
| **Estado** | Mantener / Actualizar |
| **Prioridad** | Media |
| **Clase de ficha** | Ficha activa |

---

## Proposito y rol

### Proposito operativo

Registra los equipos e instrumentos utilizados por cada laboratorio participante en una ronda de ensayo de aptitud. Es equivalente al archivo `ronda_1_equipos.csv` y alimenta al modulo de analisis de `pt_app` para contextualizar los resultados de cada participante.

### Rol en el flujo

- [x] Registro oficial
- [x] Entrada
- [x] Evidencia
- [ ] Salida
- [ ] Criterio tecnico
- [ ] Instructivo
- [ ] Matriz
- [ ] Soporte documental

Es entrada para el analisis y evidencia de trazabilidad instrumental.

---

## Aplicativos y tecnologia

#### Aplicativo asociado

- [x] `calaire-app`
- [x] `pt_app`
- [ ] Ambos
- [ ] Ninguno

Se captura en `calaire-app` y se consume en `pt_app`.

---

## Flujo de datos

#### Entradas principales

| Codigo / fuente | Descripcion | Rol en el flujo |
|---|---|---|
| `calaire-app` | Registro de equipos por participante | Origen |
| `F-PSEA-03` | Registro de participacion | Referencia |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| `pt_app` | Datos de equipos para analisis | Entrada |
| `F-PSEA-12` | Dataset consolidado (incluye equipos) | Referencia |

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `F-PSEA-03` | Registro de participacion al que pertenece | Obligatorio |
| `F-PSEA-09` | Datos exportados que incluyen equipos | Obligatorio |
| `F-PSEA-12` | Dataset consolidado que incluye equipos | Obligatorio |
| `DG-PSEA-02` | Aplicativo de captura | Obligatorio |
| `DG-PSEA-03` | Aplicativo de consumo | Obligatorio |

---

## Limites y riesgos

#### Limites de alcance

- No es el registro de participacion (eso es `F-PSEA-03`); es el anexo de equipos.
- No contiene datos de concentracion (eso es `F-PSEA-08`).
- No es un instructivo de uso.

#### Riesgos de interpretacion

- **Confundir con F-PSEA-03:** `F-PSEA-03` es el registro de participacion; `F-PSEA-04` es el anexo tecnico de equipos.
- **Omitir trazabilidad:** Debe vincularse claramente con el participante y la ronda correspondiente.
- **No alimentar pt_app:** El anexo debe estar estructurado para que `pt_app` lo consuma automaticamente.

---

## Criterio minimo de elaboracion

El anexo tecnico de equipos contiene identificacion de equipos e instrumentos por participante, vinculado con `F-PSEA-03`, exportable desde `calaire-app` y consumible por `pt_app`, sin duplicar datos de concentracion ni de participacion.
