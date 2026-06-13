# Ficha Resumen: P-PSEA-23

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `P-PSEA-23` |
| **Nombre decidido** | Flujo tecnico de datos digitales del PEA |
| **Tipo documental** | Procedimiento |
| **Estado** | Elaborar / Actualizar |
| **Prioridad** | Alta |
| **Clase de ficha** | Ficha activa |

---

## Proposito y rol

### Proposito operativo

Mapea el flujo completo de datos digitales del PEA: desde la captura en `calaire-app`, pasando por la exportacion oficial, el preprocesamiento en `pt_app`, la generacion de subformatos H/E, la consolidacion del dataset oficial y la produccion del informe final. Documenta aplicativos, archivos tecnicos internos, formatos oficiales y salidas de analisis.

### Rol en el flujo

- [x] Criterio tecnico
- [x] Matriz
- [ ] Entrada
- [ ] Salida
- [ ] Registro oficial
- [ ] Evidencia
- [ ] Instructivo
- [ ] Soporte documental

Es el documento de referencia tecnica que gobierna la arquitectura de datos del PEA.

---

## Aplicativos y tecnologia

#### Aplicativo asociado

- [x] `calaire-app`
- [x] `pt_app`
- [ ] Ambos
- [ ] Ninguno

Ambos aplicativos son componentes centrales del flujo; este procedimiento los vincula.

---

## Flujo de datos

#### Entradas principales

| Codigo / fuente | Descripcion | Rol en el flujo |
|---|---|---|
| `calaire-app` | Captura de datos, participantes, cronogramas | Origen |
| `F-PSEA-12` | Exportacion oficial de datos de participantes | Entrada oficial |
| `F-PSEA-05A` | Anexo tecnico de equipos e instrumentos | Entrada oficial |
| Archivos tecnicos internos | `datos_ronda.csv`, `niveles_calaire.csv`, etc. | Insumo tecnico |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| `F-PSEA-10` | Registro de preprocesamiento | Registro oficial |
| `F-PSEA-13A` | Datos preprocesados de homogeneidad | Salida tecnica |
| `F-PSEA-13B` | Datos preprocesados de estabilidad | Salida tecnica |
| `F-PSEA-14` | Dataset oficial consolidado (`ronda_<n>_completa.csv`) | Salida oficial |
| `F-PSEA-04` | Informe final de resultados | Producto final |

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `DG-PSEA-02` | Origen de datos en calaire-app | Obligatorio |
| `DG-PSEA-03` | Destino de preprocesamiento y analisis | Obligatorio |
| `I-PSEA-17` | Instructivo de preprocesador | Obligatorio |
| `I-PSEA-18` | Instructivo de modulo de analisis | Obligatorio |
| `P-PSEA-06` | Criterio estadistico que gobierna el flujo | Obligatorio |
| `P-PSEA-07` | Generacion del informe | Obligatorio |
| `P-PSEA-12` | Matriz documental que lista elementos | Referencia |
| `P-PSEA-13` | Matriz de evidencias que valida registros | Referencia |

---

## Limites y riesgos

#### Limites de alcance

- No es un instructivo de uso de los aplicativos (eso es `I-PSEA-17` e `I-PSEA-18`).
- No gobierna aprobacion, versionamiento ni control de software.
- No define criterios estadisticos; cita `P-PSEA-06` para eso.
- No convierte archivos tecnicos internos en formatos `F-PSEA`; solo los mapea y controla.

#### Riesgos de interpretacion

- **Confundir flujo oficial con capacidad interna alternativa:** El procesamiento interno alternativo dentro de `pt_app` es posible, pero no es el flujo oficial rutinario.
- **Promover archivos tecnicos a F-PSEA:** Archivos como `datos_ronda.csv`, `niveles_calaire.csv`, `preprocesamiento_log.csv` deben mapearse aqui; solo `preprocesamiento_log.csv` se referencia en `F-PSEA-10`.
- **Confundir F-PSEA-12 con F-PSEA-14:** `F-PSEA-12` es exportacion desde `calaire-app`; `F-PSEA-14` es dataset consolidado desde `pt_app`.
- **Tratar P-PSEA-23 como instructivo:** Es procedimiento tecnico de flujo de datos, no manual de usuario.

---

## Criterio minimo de elaboracion

El procedimiento mapea con claridad: (1) que datos entran a cada aplicativo, (2) que archivos tecnicos internos se generan, (3) que formatos oficiales salen, (4) cual es la secuencia de transformacion, y (5) donde se diferencia el flujo oficial de capacidades internas alternativas.
