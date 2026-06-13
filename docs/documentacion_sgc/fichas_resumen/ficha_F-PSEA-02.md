# Ficha Resumen: F-PSEA-02

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `F-PSEA-02` |
| **Nombre decidido** | Cronograma detallado de ronda |
| **Tipo documental** | Formato |
| **Estado** | Actualizar |
| **Prioridad** | Media |
| **Clase de ficha** | Ficha activa |

---

## Proposito y rol

### Proposito operativo

Registra el cronograma detallado de una ronda de ensayo de aptitud, desglosando actividades, responsables, fechas y dependencias. Se diligencia y exporta desde `calaire-app` y se basa en el formato de cronograma de ronda establecido.

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

- [x] `calaire-app`
- [ ] `pt_app`
- [ ] Ambos
- [ ] Ninguno

Diligenciable y exportable desde `calaire-app`.

---

## Flujo de datos

#### Entradas principales

| Codigo / fuente | Descripcion | Rol en el flujo |
|---|---|---|
| `calaire-app` | Datos de planificacion de ronda | Origen |
| `F-PSEA-01` | Calendario global | Referencia |
| `P-PSEA-09` | Planificacion de ronda | Referencia |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| `F-PSEA-06` | Plan de ronda EA | Entrada |

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `P-PSEA-09` | Planificacion que produce el cronograma | Obligatorio |
| `F-PSEA-01` | Calendario global que se desglosa | Obligatorio |
| `F-PSEA-06` | Plan de ronda que integra el cronograma | Obligatorio |
| `DG-PSEA-02` | Aplicativo que genera el cronograma | Obligatorio |

---

## Limites y riesgos

#### Limites de alcance

- No es el calendario global (eso es `F-PSEA-01`); es el desglose detallado.
- No contiene datos de participantes (eso es `F-PSEA-05`).
- No es un instructivo de uso de `calaire-app`.

#### Riesgos de interpretacion

- **Confundir con F-PSEA-01:** `F-PSEA-02` es el cronograma detallado; `F-PSEA-01` es el calendario global.
- **Omitir responsables:** El cronograma debe indicar responsables y dependencias.
- **Incluir datos de analisis:** El cronograma no contiene resultados estadisticos.

---

## Criterio minimo de elaboracion

El cronograma detallado contiene actividades, responsables, fechas y dependencias, diligenciable/exportable desde `calaire-app`, como insumo de `F-PSEA-06`.
