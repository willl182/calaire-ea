# Ficha Resumen: F-PSEA-01

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `F-PSEA-01` |
| **Nombre decidido** | Calendario global de ronda |
| **Tipo documental** | Formato |
| **Estado** | Actualizar |
| **Prioridad** | Media |
| **Clase de ficha** | Ficha activa |

---

## Proposito y rol

### Proposito operativo

Registra el calendario global de una ronda de ensayo de aptitud, incluyendo fechas de inicio, cierre, periodos de recepcion de datos y emision de resultados. Se genera y exporta desde `calaire-app` y puede utilizarse para diagramas Gantt o Mermaid.

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

Generado y exportado desde `calaire-app`.

---

## Flujo de datos

#### Entradas principales

| Codigo / fuente | Descripcion | Rol en el flujo |
|---|---|---|
| `calaire-app` | Datos de planificacion de ronda | Origen |
| `P-PSEA-09` | Planificacion de ronda | Referencia |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| `F-PSEA-06` | Plan de ronda EA | Entrada |
| `F-PSEA-02` | Cronograma detallado | Referencia |

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `P-PSEA-09` | Planificacion que produce el calendario | Obligatorio |
| `F-PSEA-06` | Plan de ronda que integra el calendario | Obligatorio |
| `F-PSEA-02` | Cronograma detallado derivado | Obligatorio |
| `DG-PSEA-02` | Aplicativo que genera el calendario | Obligatorio |

---

## Limites y riesgos

#### Limites de alcance

- No es el cronograma detallado (eso es `F-PSEA-02`); es el calendario global.
- No contiene datos de participantes (eso es `F-PSEA-05`).
- No es un instructivo de uso de `calaire-app`.

#### Riesgos de interpretacion

- **Confundir con F-PSEA-02:** `F-PSEA-01` es el calendario global; `F-PSEA-02` es el cronograma detallado.
- **Omitir exportabilidad:** Debe poder exportarse desde `calaire-app` para usar en Gantt/Mermaid.
- **Incluir datos de analisis:** El calendario no contiene resultados estadisticos.

---

## Criterio minimo de elaboracion

El calendario global contiene fechas de inicio, cierre, recepcion de datos y emision de resultados, exportable desde `calaire-app`, como insumo de `F-PSEA-06`.
