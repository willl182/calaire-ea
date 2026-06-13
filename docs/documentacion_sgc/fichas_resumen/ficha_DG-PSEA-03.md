# Ficha Resumen: DG-PSEA-03

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `DG-PSEA-03` |
| **Nombre decidido** | Aplicativo `pt_app` |
| **Tipo documental** | Documento general |
| **Estado** | Elaborar |
| **Prioridad** | Alta |
| **Clase de ficha** | Ficha activa |

---

## Proposito y rol

### Proposito operativo

Documenta el aplicativo de preprocesamiento, consolidacion de datos, analisis estadistico, evaluacion de homogeneidad y estabilidad, e informe final de resultados del PEA. Es el sistema operativo del PEA en fase de analisis y emision de resultados.

### Rol en el flujo

- [x] Soporte documental
- [ ] Entrada
- [ ] Salida
- [ ] Registro oficial
- [ ] Evidencia
- [ ] Criterio tecnico
- [ ] Instructivo
- [ ] Matriz

Es el documento general que define el alcance, funciones y limites del aplicativo analitico.

---

## Aplicativos y tecnologia

#### Aplicativo asociado

- [ ] `calaire-app`
- [x] `pt_app`
- [ ] Ambos
- [ ] Ninguno

El documento describe el aplicativo `pt_app`.

---

## Flujo de datos

#### Entradas principales

| Codigo / fuente | Descripcion | Rol en el flujo |
|---|---|---|
| `F-PSEA-12` | Datos de participantes exportados desde `calaire-app` | Entrada oficial |
| `F-PSEA-05A` | Anexo tecnico de equipos e instrumentos | Entrada oficial |
| Archivos tecnicos internos | Datos de ronda, niveles, H/E crudos | Insumo tecnico |
| `P-PSEA-06` | Criterio estadistico de referencia | Referencia |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| `F-PSEA-10` | Registro de preprocesamiento | Registro oficial |
| `F-PSEA-13A` | Datos preprocesados de homogeneidad | Salida tecnica |
| `F-PSEA-13B` | Datos preprocesados de estabilidad | Salida tecnica |
| `F-PSEA-14` | Dataset oficial consolidado | Salida oficial |
| `F-PSEA-13C` | Resultados de homogeneidad | Salida tecnica |
| `F-PSEA-13D` | Resultados de estabilidad | Salida tecnica |
| `F-PSEA-04` | Informe final de resultados | Producto final |

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `I-PSEA-17` | Instructivo de preprocesador | Obligatorio |
| `I-PSEA-18` | Instructivo de modulo de analisis | Obligatorio |
| `P-PSEA-06` | Criterio estadistico que gobierna el analisis | Obligatorio |
| `P-PSEA-07` | Generacion del informe de resultados | Obligatorio |
| `P-PSEA-23` | Flujo tecnico que mapea el paso de datos | Obligatorio |
| `DG-PSEA-02` | Aplicativo que alimenta datos de entrada | Obligatorio |

---

## Limites y riesgos

#### Limites de alcance

- No es un formato `F-PSEA`; es un documento general.
- No es un instructivo de uso (eso es `I-PSEA-17` e `I-PSEA-18`).
- No define criterios estadisticos; cita `P-PSEA-06` para eso.
- No captura datos de participantes (eso es `calaire-app`).
- No es un procedimiento de control documental.

#### Riesgos de interpretacion

- **Codificar como formato F-PSEA:** `pt_app` es un aplicativo; sus registros y salidas son formatos, pero el aplicativo mismo es `DG-PSEA-03`.
- **Confundir con P-PSEA-06:** `P-PSEA-06` define el criterio estadistico; `DG-PSEA-03` documenta la herramienta que lo implementa.
- **Confundir con P-PSEA-07:** `P-PSEA-07` gobierna la generacion del informe; `DG-PSEA-03` documenta la herramienta que lo produce.
- **Tratar como instructivo:** Es documento general, no manual de usuario.

---

## Criterio minimo de elaboracion

El documento general describe funciones principales (preprocesamiento, analisis, H/E, informe), alcance operativo, entradas oficiales desde `calaire-app`, salidas oficiales, limites respecto a criterios tecnicos (`P-PSEA-06`), y conexion con instructivos y flujo de datos (`P-PSEA-23`), sin codificarse como formato ni como instructivo.
