# Ficha Resumen: P-PSEA-16

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `P-PSEA-16` |
| **Nombre decidido** | Trabajo no conforme, no conformidades y acciones correctivas |
| **Tipo documental** | Procedimiento |
| **Estado** | Mantener / Actualizar |
| **Prioridad** | Media-alta |
| **Clase de ficha** | Ficha activa |

---

## Proposito y rol

### Proposito operativo

Gobierna la identificacion, registro, evaluacion, decision y seguimiento de trabajo no conforme (TNC), no conformidades (NC) y acciones correctivas (CAPA) dentro del PEA. Conecta con quejas, apelaciones, colusion y el flujo de datos cuando un resultado o proceso afecta la conformidad del ensayo.

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

Los casos de quejas/NC pueden gestionarse en `calaire-app` como casos SGC.

---

## Flujo de datos

#### Entradas principales

| Codigo / fuente | Descripcion | Rol en el flujo |
|---|---|---|
| `P-PSEA-08` | Colusion y falsificacion (si deriva en NC) | Referencia |
| `P-PSEA-24` | Quejas del PEA | Referencia |
| `P-PSEA-25` | Apelaciones del PEA | Referencia |
| `F-PSEA-04` | Informe afectado (si aplica) | Referencia |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| `F-PSEA-16` | Registro/caso de queja o NC | Referencia |
| `P-PSEA-23` | Flujo de datos afectado | Referencia |

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `P-PSEA-08` | Colusion que puede derivar en NC | Obligatorio |
| `P-PSEA-24` | Quejas que pueden derivar en NC | Obligatorio |
| `P-PSEA-25` | Apelaciones que pueden derivar en NC | Obligatorio |
| `P-PSEA-23` | Flujo de datos que puede afectarse | Obligatorio |
| `F-PSEA-16` | Registro de caso de queja o NC | Obligatorio |
| `F-PSEA-04` | Informe que puede requerir correccion | Referencia |

---

## Limites y riesgos

#### Limites de alcance

- No es un procedimiento de auditoria (fuera del alcance PEA).
- No es un procedimiento de colusion (eso es `P-PSEA-08`); conecta con el.
- No es un procedimiento de quejas (eso es `P-PSEA-24`); conecta con el.
- No es un procedimiento de apelaciones (eso es `P-PSEA-25`); conecta con el.

#### Riesgos de interpretacion

- **Duplicar P-PSEA-08:** La deteccion de colusion es `P-PSEA-08`; la NC que resulta es `P-PSEA-16`.
- **Omitir conexion con quejas/apelaciones:** Debe conectar claramente con `P-PSEA-24` y `P-PSEA-25`.
- **Omitir flujo de datos:** Una NC puede afectar datos, registros o informes; debe conectar con `P-PSEA-23`.
- **Cerrar prematuramente sin seguimiento:** Debe incluir seguimiento de CAPA.

---

## Criterio minimo de elaboracion

El procedimiento define TNC/NC/CAPA especifico del PEA, conectando con `P-PSEA-08`, `P-PSEA-24`, `P-PSEA-25`, `P-PSEA-23` y `F-PSEA-16`, sin duplicar colusion, quejas ni apelaciones.
