# Ficha Resumen: F-PSEA-10

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `F-PSEA-10` |
| **Nombre decidido** | Registro de preprocesamiento de datos |
| **Tipo documental** | Registro |
| **Estado** | Elaborar |
| **Prioridad** | Alta |
| **Clase de ficha** | Ficha activa |

---

## Proposito y rol

### Proposito operativo

Documenta cada ejecucion del preprocesador de `pt_app`, listando archivos de entrada, archivos de salida, fecha, version, responsable, ruta y observaciones. Referencia `preprocesamiento_log.csv` como soporte tecnico. Es la evidencia de trazabilidad del paso de datos crudos a datos consolidados.

### Rol en el flujo

- [x] Registro oficial
- [x] Evidencia
- [ ] Entrada
- [ ] Salida
- [ ] Criterio tecnico
- [ ] Instructivo
- [ ] Matriz
- [ ] Soporte documental

---

## Aplicativos y tecnologia

#### Aplicativo asociado

- [ ] `calaire-app`
- [x] `pt_app`
- [ ] Ambos
- [ ] Ninguno

Se genera durante la ejecucion del preprocesador en `pt_app`.

---

## Flujo de datos

#### Entradas principales

| Codigo / fuente | Descripcion | Rol en el flujo |
|---|---|---|
| `F-PSEA-12` | Datos de participantes exportados | Insumo |
| `F-PSEA-05A` | Anexo tecnico de equipos | Insumo |
| Archivos tecnicos internos | Datos de ronda, niveles, H/E crudos | Insumo tecnico |
| `I-PSEA-17` | Instructivo de preprocesamiento | Referencia |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| `preprocesamiento_log.csv` | Archivo tecnico de log | Referencia |
| `F-PSEA-13A` | Datos preprocesados de homogeneidad | Salida |
| `F-PSEA-13B` | Datos preprocesados de estabilidad | Salida |
| `F-PSEA-14` | Dataset oficial consolidado | Salida |

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `P-PSEA-23` | Flujo tecnico que gobierna el paso | Obligatorio |
| `I-PSEA-17` | Instructivo que explica la operacion | Obligatorio |
| `DG-PSEA-03` | Aplicativo que ejecuta el preprocesamiento | Obligatorio |
| `F-PSEA-14` | Dataset que resulta del preprocesamiento | Obligatorio |
| `F-PSEA-13A` | Subformato de homogeneidad generado | Obligatorio |
| `F-PSEA-13B` | Subformato de estabilidad generado | Obligatorio |

---

## Limites y riesgos

#### Limites de alcance

- No es el aplicativo `pt_app` (eso es `DG-PSEA-03`); es un registro de su ejecucion.
- No es el criterio estadistico de preprocesamiento (eso es `P-PSEA-06`).
- No contiene datos crudos de participantes (eso es `F-PSEA-12`).
- No es el dataset consolidado final (eso es `F-PSEA-14`).

#### Riesgos de interpretacion

- **Tratar como aplicativo:** `F-PSEA-10` es un registro; el aplicativo es `DG-PSEA-03`.
- **Omitir preprocesamiento_log.csv:** El registro debe referenciar `preprocesamiento_log.csv` como soporte tecnico.
- **Confundir con F-PSEA-14:** `F-PSEA-10` documenta la ejecucion del preprocesamiento; `F-PSEA-14` es el dataset consolidado que resulta.
- **No documentar version y responsable:** Cada ejecucion debe quedar trazada con fecha, version y responsable.

---

## Criterio minimo de elaboracion

El registro de preprocesamiento contiene: identificacion de la ejecucion, archivos de entrada, archivos de salida, fecha, version, responsable, observaciones y referencia a `preprocesamiento_log.csv`, sin duplicar el criterio estadistico ni confundirse con el aplicativo.
