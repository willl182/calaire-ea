# Ficha Resumen: F-PSEA-14

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `F-PSEA-14` |
| **Nombre decidido** | Datos oficiales consolidados para evaluacion de aptitud |
| **Tipo documental** | Registro |
| **Estado** | Elaborar |
| **Prioridad** | Alta |
| **Clase de ficha** | Ficha activa |

---

## Proposito y rol

### Proposito operativo

Dataset oficial consolidado para la evaluacion de aptitud, generado por el preprocesador de `pt_app` y equivalente a `ronda_<n>_completa.csv`. Es la entrada unica y autorizada para el modulo de analisis PT y para la generacion del informe final. Integra datos de participantes, equipos y resultados en un formato estandarizado.

### Rol en el flujo

- [x] Registro oficial
- [x] Salida
- [x] Entrada
- [ ] Evidencia
- [ ] Criterio tecnico
- [ ] Instructivo
- [ ] Matriz
- [ ] Soporte documental

Es simultaneamente salida del preprocesamiento y entrada oficial del analisis.

---

## Aplicativos y tecnologia

#### Aplicativo asociado

- [ ] `calaire-app`
- [x] `pt_app`
- [ ] Ambos
- [ ] Ninguno

Generado por el preprocesador de `pt_app`.

---

## Flujo de datos

#### Entradas principales

| Codigo / fuente | Descripcion | Rol en el flujo |
|---|---|---|
| `F-PSEA-12` | Datos de participantes exportados desde `calaire-app` | Entrada oficial |
| `F-PSEA-05A` | Anexo tecnico de equipos e instrumentos | Entrada oficial |
| Archivos tecnicos internos | Datos de ronda, niveles, H/E crudos | Insumo tecnico |
| `F-PSEA-10` | Registro de preprocesamiento | Referencia |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| `pt_app` (modulo analisis) | Dataset para evaluacion de aptitud | Entrada oficial |
| `F-PSEA-04` | Informe final de resultados | Referencia |
| `P-PSEA-06` | Analisis estadistico | Referencia |

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `P-PSEA-23` | Flujo tecnico que define el paso | Obligatorio |
| `F-PSEA-10` | Registro de preprocesamiento | Obligatorio |
| `F-PSEA-12` | Exportacion desde calaire-app que alimenta el dataset | Obligatorio |
| `F-PSEA-05A` | Equipos e instrumentos que alimentan el dataset | Obligatorio |
| `P-PSEA-06` | Criterio estadistico que usa este dataset | Obligatorio |
| `P-PSEA-07` | Generacion del informe que usa este dataset | Obligatorio |

---

## Limites y riesgos

#### Limites de alcance

- No es la exportacion desde `calaire-app` (eso es `F-PSEA-12`); es la consolidacion en `pt_app`.
- No es el informe final (eso es `F-PSEA-04`); es el dataset que lo alimenta.
- No contiene resultados de H/E (eso es `F-PSEA-13C` y `F-PSEA-13D`); puede referenciarlos.
- No es un instructivo de uso.

#### Riesgos de interpretacion

- **Confundir con F-PSEA-12:** `F-PSEA-12` es la exportacion cruda desde `calaire-app`; `F-PSEA-14` es el dataset consolidado y validado en `pt_app`.
- **Confundir con F-PSEA-04:** `F-PSEA-14` es datos; `F-PSEA-04` es el informe interpretativo.
- **Omitir trazabilidad:** Debe vincularse con `F-PSEA-10` (registro de preprocesamiento) y `P-PSEA-23` (flujo de datos).
- **Usar datos no consolidados:** Solo el dataset oficial consolidado debe alimentar el analisis; no usar exportaciones parciales.

---

## Criterio minimo de elaboracion

El dataset oficial consolidado contiene datos de participantes, equipos y resultados en formato estandarizado, con trazabilidad a `F-PSEA-12`, `F-PSEA-05A`, `F-PSEA-10` y `P-PSEA-23`, y se identifica como `ronda_<n>_completa.csv`, sin confundirse con `F-PSEA-12` ni con `F-PSEA-04`.
