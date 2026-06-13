# Ficha Resumen: F-PSEA-06

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `F-PSEA-06` |
| **Nombre decidido** | Plan de ronda EA |
| **Tipo documental** | Formato |
| **Estado** | Mantener / Actualizar |
| **Prioridad** | Media-alta |
| **Clase de ficha** | Ficha activa |

---

## Proposito y rol

### Proposito operativo

Documento consolidado del plan de una ronda de ensayo de aptitud. Integra el calendario global (`F-PSEA-01`), el cronograma detallado (`F-PSEA-02`), la ficha digital de ronda (`F-PSEA-07`) y la nota/matriz A-U de ISO/IEC 17043:2023 7.2.1.3. Es el documento maestro de planificacion de cada ronda.

### Rol en el flujo

- [x] Registro oficial
- [x] Evidencia
- [x] Salida
- [ ] Entrada
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

Se genera desde `calaire-app` integrando multiples formatos.

---

## Flujo de datos

#### Entradas principales

| Codigo / fuente | Descripcion | Rol en el flujo |
|---|---|---|
| `F-PSEA-01` | Calendario global de ronda | Insumo |
| `F-PSEA-02` | Cronograma detallado de ronda | Insumo |
| `F-PSEA-07` | Ficha digital de ronda | Insumo |
| `F-PSEA-08` | Preparacion y control del item | Referencia |
| `P-PSEA-09` | Planificacion de ronda | Referencia |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| Participantes | Comunicacion del plan de ronda | Producto |
| `P-PSEA-08` | Colusion y falsificacion (medidas preventivas) | Referencia |

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `P-PSEA-09` | Procedimiento que gobierna la planificacion | Obligatorio |
| `F-PSEA-01` | Calendario global integrado | Obligatorio |
| `F-PSEA-02` | Cronograma detallado integrado | Obligatorio |
| `F-PSEA-07` | Ficha digital integrada | Obligatorio |
| `F-PSEA-08` | Preparacion del item referenciada | Obligatorio |
| `P-PSEA-08` | Colusion y falsificacion (medidas preventivas) | Referencia |
| `DG-PSEA-02` | Aplicativo que genera el plan | Obligatorio |

---

## Limites y riesgos

#### Limites de alcance

- No es un procedimiento de planificacion (eso es `P-PSEA-09`); es el formato/registro del plan.
- No contiene datos reportados por participantes (eso es `F-PSEA-09`).
- No contiene resultados de aptitud (eso es `F-PSEA-04`).
- No es un instructivo de uso.

#### Riesgos de interpretacion

- **Confundir con P-PSEA-09:** `P-PSEA-09` es el procedimiento de planificacion; `F-PSEA-06` es el formato/registro del plan.
- **Omitir nota A-U:** Debe integrar o referenciar la nota/matriz A-U de ISO/IEC 17043:2023 7.2.1.3.
- **Omitir H/E:** No debe decir que H/E no aplica; H/E se documenta en `F-PSEA-13`.
- **Incluir datos de analisis:** El plan de ronda no incluye resultados estadisticos.

---

## Criterio minimo de elaboracion

El plan de ronda integra `F-PSEA-01`, `F-PSEA-02`, `F-PSEA-07`, referencia a `F-PSEA-08` y nota A-U, generado desde `calaire-app`, como documento maestro de planificacion sin incluir datos de participantes ni resultados de analisis.
