# Ficha Resumen: DG-PSEA-02

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `DG-PSEA-02` |
| **Nombre decidido** | Aplicativo `calaire-app` |
| **Tipo documental** | Documento general |
| **Estado** | Actualizar |
| **Prioridad** | Alta |
| **Clase de ficha** | Ficha activa |

---

## Proposito y rol

### Proposito operativo

Documenta el aplicativo de gestion de rondas de ensayo de aptitud, participantes, cronogramas, captura de datos, exportaciones y gestion de casos SGC de quejas. Es el sistema operativo principal del PEA en fase de planificacion, ejecucion de ronda y recoleccion de datos.

### Rol en el flujo

- [x] Soporte documental
- [ ] Entrada
- [ ] Salida
- [ ] Registro oficial
- [ ] Evidencia
- [ ] Criterio tecnico
- [ ] Instructivo
- [ ] Matriz

Es el documento general que define el alcance, funciones y limites del aplicativo.

---

## Aplicativos y tecnologia

#### Aplicativo asociado

- [x] `calaire-app`
- [ ] `pt_app`
- [ ] Ambos
- [ ] Ninguno

El documento describe el aplicativo mismo.

---

## Flujo de datos

#### Entradas principales

| Codigo / fuente | Descripcion | Rol en el flujo |
|---|---|---|
| Requisitos operativos PEA | Funciones requeridas para gestion de rondas | Insumo |
| `P-PSEA-09` | Planificacion de ronda | Referencia |
| `P-PSEA-20` | Comunicaciones del PEA | Referencia |
| Participantes | Datos reportados por laboratorios | Entrada |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| `F-PSEA-07` | Ficha digital de ronda | Salida |
| `F-PSEA-12` | Datos exportados para analisis PT | Salida |
| `F-PSEA-05` | Registro de participacion | Salida |
| `F-PSEA-05A` | Anexo tecnico de equipos e instrumentos | Salida |
| `F-PSEA-09` | Datos reportados por participante | Salida |
| `F-PSEA-01` | Calendario global de ronda | Salida |
| `F-PSEA-02` | Cronograma detallado de ronda | Salida |

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `I-PSEA-10` | Instructivo para participante | Obligatorio |
| `I-PSEA-16` | Instructivo de administracion de rondas | Obligatorio |
| `P-PSEA-09` | Planificacion que usa el aplicativo | Obligatorio |
| `P-PSEA-20` | Comunicaciones que usan el aplicativo | Obligatorio |
| `P-PSEA-24` | Quejas gestionadas como casos SGC | Obligatorio |
| `P-PSEA-23` | Flujo tecnico que recibe datos de calaire-app | Obligatorio |

---

## Limites y riesgos

#### Limites de alcance

- No es un formato `F-PSEA`; es un documento general.
- No es un instructivo de uso (eso es `I-PSEA-10` e `I-PSEA-16`).
- No define criterios estadisticos ni de evaluacion de aptitud.
- No genera el informe final ni el analisis estadistico (eso es `pt_app`).
- No es un procedimiento de control documental.

#### Riesgos de interpretacion

- **Codificar como formato F-PSEA:** `calaire-app` es un aplicativo; sus registros y exportaciones son formatos, pero el aplicativo mismo es `DG-PSEA-02`.
- **Confundir con P-PSEA-09:** `P-PSEA-09` gobierna la planificacion; `DG-PSEA-02` documenta la herramienta que la soporta.
- **Incluir analisis estadistico:** El analisis PT ocurre en `pt_app` (`DG-PSEA-03`), no en `calaire-app`.

---

## Criterio minimo de elaboracion

El documento general describe funciones principales, alcance operativo, limites respecto a `pt_app`, formatos que genera, y conexion con instructivos y procedimientos del PEA, sin codificarse como formato ni como instructivo.
