# Ficha Resumen: F-PSEA-06

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `F-PSEA-06` |
| **Nombre decidido** | Ficha digital de ronda EA |
| **Tipo documental** | Formato |
| **Estado** | Elaborar / Actualizar |
| **Prioridad** | Alta |
| **Clase de ficha** | Ficha activa |

---

## Proposito y rol

### Proposito operativo

Registra y exporta desde `calaire-app` la informacion estructurada de una ronda de ensayo de aptitud, incluyendo identificacion, participantes, cronograma, item de ensayo, niveles de concentracion y puntos A-U requeridos por ISO/IEC 17043:2023 7.2.1.3. Es el insumo principal para el `F-PSEA-05` (Plan de ronda).

### Rol en el flujo

- [x] Salida
- [x] Evidencia
- [ ] Entrada
- [ ] Registro oficial
- [ ] Criterio tecnico
- [ ] Instructivo
- [ ] Matriz
- [ ] Soporte documental

Es una salida exportable del aplicativo y evidencia de planificacion.

---

## Aplicativos y tecnologia

#### Aplicativo asociado

- [x] `calaire-app`
- [ ] `pt_app`
- [ ] Ambos
- [ ] Ninguno

Se genera, diligencia y exporta desde `calaire-app`.

---

## Flujo de datos

#### Entradas principales

| Codigo / fuente | Descripcion | Rol en el flujo |
|---|---|---|
| `calaire-app` | Datos de ronda ingresados en el aplicativo | Origen |
| `P-PSEA-04` | Planificacion de ronda | Referencia |
| `F-PSEA-01` | Calendario global | Referencia |
| `F-PSEA-02` | Cronograma detallado | Referencia |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| `F-PSEA-05` | Plan de ronda EA | Entrada principal |

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `P-PSEA-04` | Planificacion que genera la ficha | Obligatorio |
| `F-PSEA-05` | Plan de ronda que absorbe esta ficha | Obligatorio |
| `F-PSEA-01` | Calendario referenciado en la ficha | Referencia |
| `F-PSEA-02` | Cronograma referenciado en la ficha | Referencia |
| `DG-PSEA-02` | Aplicativo que genera la ficha | Obligatorio |

---

## Limites y riesgos

#### Limites de alcance

- No es el plan de ronda completo (eso es `F-PSEA-05`); es un insumo estructurado.
- No contiene datos reportados por participantes (eso es `F-PSEA-08`).
- No contiene anexos tecnicos de equipos (eso es `F-PSEA-04`).
- No es un instructivo de uso del aplicativo.

#### Riesgos de interpretacion

- **Confundir con F-PSEA-05:** `F-PSEA-06` es la ficha digital generada por el aplicativo; `F-PSEA-05` es el plan de ronda consolidado que la integra con otros elementos.
- **Omitir puntos A-U:** La ficha debe incluir o referenciar los puntos A-U de ISO/IEC 17043:2023 7.2.1.3.
- **Incluir datos de analisis:** Los datos estadisticos y resultados de aptitud no van en esta ficha; van en `F-PSEA-13` y `F-PSEA-12`.

---

## Criterio minimo de elaboracion

La ficha digital contiene o referencia: identificacion de ronda, participantes, cronograma, item de ensayo, niveles, puntos A-U, y se exporta desde `calaire-app` como insumo de `F-PSEA-05`.
