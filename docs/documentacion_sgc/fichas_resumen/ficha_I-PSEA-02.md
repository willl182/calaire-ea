# Ficha Resumen: I-PSEA-02

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `I-PSEA-02` |
| **Nombre decidido** | Instructivo de uso de `calaire-app` por participante |
| **Tipo documental** | Instructivo |
| **Estado** | Mantener / Actualizar |
| **Prioridad** | Media-alta |
| **Clase de ficha** | Ficha activa |

---

## Proposito y rol

### Proposito operativo

Explica al laboratorio participante como usar `calaire-app` para confirmar participacion, consultar informacion de la ronda, registrar datos, cargar informacion de equipos/instrumentos y atender comunicaciones operativas asociadas al ensayo de aptitud. No define criterios tecnicos del PEA; describe la operacion de la interfaz del participante.

### Rol en el flujo

- [x] Instructivo
- [ ] Entrada
- [ ] Salida
- [ ] Registro oficial
- [ ] Evidencia
- [ ] Criterio tecnico
- [ ] Matriz
- [ ] Soporte documental

---

## Aplicativos y tecnologia

#### Aplicativo asociado

- [x] `calaire-app`
- [ ] `pt_app`
- [ ] Ambos
- [ ] Ninguno

Describe el uso operativo de `calaire-app` desde el rol del participante.

---

## Flujo de datos

#### Entradas principales

| Codigo / fuente | Descripcion | Rol en el flujo |
|---|---|---|
| `DG-PSEA-02` | Documento general del aplicativo `calaire-app` | Referencia |
| `F-PSEA-03` | Registro de participacion | Insumo operativo |
| `F-PSEA-04` | Informacion de equipos e instrumentos | Insumo operativo |
| `P-PSEA-05` | Comunicaciones del PEA | Referencia |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| `F-PSEA-08` | Datos reportados por participante | Registro oficial |
| `F-PSEA-03` | Confirmacion o actualizacion de participacion | Registro |
| `F-PSEA-04` | Informacion tecnica de equipos/instrumentos | Registro |
| `F-PSEA-09` | Exportacion posterior de datos hacia analisis | Salida derivada |

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `DG-PSEA-02` | Aplicativo que se opera | Obligatorio |
| `P-PSEA-05` | Comunicaciones al participante | Obligatorio |
| `F-PSEA-03` | Registro de participacion | Obligatorio |
| `F-PSEA-04` | Anexo tecnico de equipos/instrumentos | Obligatorio |
| `F-PSEA-08` | Datos reportados por participante | Obligatorio |
| `P-PSEA-08` | Flujo tecnico que recibe la informacion capturada | Referencia |

---

## Limites y riesgos

#### Limites de alcance

- No reemplaza `DG-PSEA-02`; solo explica el uso operativo para participantes.
- No define criterios estadisticos, valor asignado, `sigma_pt` ni reglas de desempeno.
- No gobierna comunicaciones formales del PEA; debe alinearse con `P-PSEA-05`.
- No describe la administracion interna de rondas; eso corresponde a `I-PSEA-03`.

#### Riesgos de interpretacion

- **Confundir con procedimiento:** El instructivo explica como usar la interfaz; los criterios de comunicacion, planificacion y datos se gobiernan en procedimientos.
- **Omitir trazabilidad:** La captura del participante debe conectarse con `F-PSEA-08`, `F-PSEA-04` y la exportacion `F-PSEA-09`.
- **Incluir analisis estadistico:** El participante no opera `pt_app`; el analisis se documenta en `I-PSEA-04`, `I-PSEA-05` y `P-PSEA-07`.
- **Duplicar I-PSEA-03:** Este instructivo cubre el rol participante; la administracion interna de ronda queda separada.

---

## Criterio minimo de elaboracion

El instructivo describe el uso de `calaire-app` por el participante para consulta de ronda, confirmacion, registro de datos y equipos, y seguimiento de comunicaciones, con trazabilidad a `F-PSEA-03`, `F-PSEA-04`, `F-PSEA-08` y `F-PSEA-09`, sin definir criterios tecnicos ni funciones administrativas internas.
