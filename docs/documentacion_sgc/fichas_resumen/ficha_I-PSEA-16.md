# Ficha Resumen: I-PSEA-16

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `I-PSEA-16` |
| **Nombre decidido** | Instructivo de administracion de rondas en `calaire-app` |
| **Tipo documental** | Instructivo |
| **Estado** | Mantener / Actualizar |
| **Prioridad** | Media-alta |
| **Clase de ficha** | Ficha activa |

---

## Proposito y rol

### Proposito operativo

Explica el uso interno de `calaire-app` para configurar, administrar y controlar rondas de ensayo de aptitud: calendario, cronograma, ficha digital de ronda, participantes, comunicaciones operativas, exportaciones y casos SGC cuando aplique. No reemplaza el procedimiento de planificacion; describe como operar el aplicativo para ejecutar lo definido documentalmente.

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

Describe el uso operativo de `calaire-app` desde el rol administrador o coordinador de ronda.

---

## Flujo de datos

#### Entradas principales

| Codigo / fuente | Descripcion | Rol en el flujo |
|---|---|---|
| `P-PSEA-09` | Procedimiento de planificacion de ronda | Referencia |
| `DG-PSEA-02` | Documento general del aplicativo `calaire-app` | Referencia |
| `F-PSEA-01` | Calendario global de ronda | Insumo / salida controlada |
| `F-PSEA-02` | Cronograma detallado de ronda | Insumo / salida controlada |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| `F-PSEA-07` | Ficha digital de ronda EA | Salida |
| `F-PSEA-01` | Calendario global actualizado | Salida |
| `F-PSEA-02` | Cronograma detallado actualizado | Salida |
| `F-PSEA-12` | Exportacion de datos de participantes | Salida |
| `F-PSEA-16` | Caso SGC de queja o NC, si aplica | Registro |

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `DG-PSEA-02` | Aplicativo que se administra | Obligatorio |
| `P-PSEA-09` | Planificacion de ronda | Obligatorio |
| `P-PSEA-20` | Comunicaciones operativas | Obligatorio |
| `P-PSEA-24` | Quejas gestionadas como casos SGC | Referencia |
| `F-PSEA-07` | Ficha digital de ronda | Obligatorio |
| `P-PSEA-23` | Flujo tecnico que recibe exportaciones | Referencia |

---

## Limites y riesgos

#### Limites de alcance

- No reemplaza `P-PSEA-09`; solo explica como ejecutar en el aplicativo lo definido por el procedimiento.
- No define criterios estadisticos ni analisis de resultados.
- No reemplaza `I-PSEA-10`, que cubre el uso del participante.
- No gobierna quejas o apelaciones; solo puede explicar el registro operativo de casos cuando aplique.

#### Riesgos de interpretacion

- **Confundir con P-PSEA-09:** La planificacion se gobierna por procedimiento; este instructivo documenta la operacion del aplicativo.
- **Confundir quejas con apelaciones:** Las quejas pueden gestionarse como casos en `calaire-app`; las apelaciones siguen canal formal segun `P-PSEA-25`.
- **Omitir F-PSEA-07:** La ficha digital de ronda es una salida clave de la administracion en `calaire-app`.
- **Mezclar con pt_app:** `pt_app` interviene despues, en preprocesamiento y analisis; no pertenece a este instructivo.

---

## Criterio minimo de elaboracion

El instructivo describe la administracion interna de rondas en `calaire-app`: configuracion de calendario, cronograma, participantes, ficha digital de ronda, comunicaciones operativas, exportaciones y casos SGC cuando aplique, sin reemplazar `P-PSEA-09`, `P-PSEA-20`, `P-PSEA-24` ni los instructivos de `pt_app`.
