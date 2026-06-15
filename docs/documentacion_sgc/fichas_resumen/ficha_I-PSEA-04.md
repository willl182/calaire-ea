# Ficha Resumen: I-PSEA-04

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `I-PSEA-04` |
| **Nombre decidido** | Instructivo de uso del preprocesador de datos de `pt_app` |
| **Tipo documental** | Instructivo |
| **Estado** | Elaborar |
| **Prioridad** | Alta |
| **Clase de ficha** | Ficha activa |

---

## Proposito y rol

### Proposito operativo

Explica el uso operativo del modulo preprocesador de `pt_app`, incluyendo carga de archivos de entrada, parametros de configuracion, secuencia de pasos, archivos tecnicos generados y registro de la ejecucion en `F-PSEA-10`. No define criterios estadisticos; describe como operar la herramienta.

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

- [ ] `calaire-app`
- [x] `pt_app`
- [ ] Ambos
- [ ] Ninguno

Describe el uso operativo del preprocesador dentro de `pt_app`.

---

## Flujo de datos

#### Entradas principales

| Codigo / fuente | Descripcion | Rol en el flujo |
|---|---|---|
| `F-PSEA-09` | Datos de participantes exportados desde `calaire-app` | Insumo |
| `F-PSEA-04` | Anexo tecnico de equipos e instrumentos | Insumo |
| Archivos tecnicos internos | Datos de ronda, niveles, H/E crudos | Insumo |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| `F-PSEA-10` | Registro de preprocesamiento | Registro oficial |
| `F-PSEA-11A` | Datos preprocesados de homogeneidad | Salida |
| `F-PSEA-11B` | Datos preprocesados de estabilidad | Salida |
| `F-PSEA-12` | Dataset oficial consolidado | Salida |

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `DG-PSEA-03` | Documento general del aplicativo | Obligatorio |
| `P-PSEA-08` | Flujo tecnico que contextualiza el paso | Obligatorio |
| `P-PSEA-07` | Criterio estadistico de referencia | Referencia |
| `F-PSEA-10` | Registro que documenta la ejecucion | Obligatorio |

---

## Limites y riesgos

#### Limites de alcance

- No reemplaza `P-PSEA-07` (criterio estadistico); solo explica como operar la herramienta.
- No reemplaza `P-PSEA-08` (flujo tecnico); complementa la parte operativa del preprocesador.
- No define que es un outlier, como se calcula el valor asignado ni que es `sigma_pt`.
- No es un procedimiento de control de calidad.

#### Riesgos de interpretacion

- **Confundir con P-PSEA-07:** El instructivo explica botones, parametros y pasos; el procedimiento define criterios tecnicos.
- **Omitir F-PSEA-10:** El instructivo debe mencionar la obligacion de registrar cada ejecucion en `F-PSEA-10`.
- **Describir analisis estadistico:** El analisis PT propiamente dicho se cubre en `I-PSEA-05`.

---

## Criterio minimo de elaboracion

El instructivo describe paso a paso la operacion del preprocesador: archivos de entrada, parametros, secuencia, archivos de salida, registro en `F-PSEA-10`, y puntos de control sin definir criterios estadisticos ni flujo de datos macro.
