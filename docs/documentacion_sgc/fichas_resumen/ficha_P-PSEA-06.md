# Ficha Resumen: P-PSEA-06

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `P-PSEA-06` |
| **Nombre decidido** | Diseno estadistico |
| **Tipo documental** | Procedimiento |
| **Estado** | Mantener / Actualizar |
| **Prioridad** | Alta |
| **Clase de ficha** | Ficha activa |

---

## Proposito y rol

### Proposito operativo

Procedimiento tecnico central que gobierna el valor asignado, `sigma_pt`, incertidumbre, deteccion de outliers, evaluacion de homogeneidad y estabilidad como insumo, criterios de desempeno y reglas de decision para la evaluacion de aptitud en gases contaminantes criterio. Es el nucleo metrologico-estadistico del PEA.

### Rol en el flujo

- [x] Criterio tecnico
- [ ] Entrada
- [ ] Salida
- [ ] Registro oficial
- [ ] Evidencia
- [ ] Instructivo
- [ ] Matriz
- [ ] Soporte documental

Define los criterios que los demas procedimientos e instructivos aplican o citan.

---

## Aplicativos y tecnologia

#### Aplicativo asociado

- [ ] `calaire-app`
- [x] `pt_app`
- [ ] Ambos
- [ ] Ninguno

El criterio estadistico se implementa en `pt_app`, pero el procedimiento define el criterio, no la herramienta.

---

## Flujo de datos

#### Entradas principales

| Codigo / fuente | Descripcion | Rol en el flujo |
|---|---|---|
| `F-PSEA-14` | Dataset oficial consolidado | Insumo |
| `F-PSEA-13A` | Datos preprocesados de homogeneidad | Insumo |
| `F-PSEA-13B` | Datos preprocesados de estabilidad | Insumo |
| Criterios metrologicos | ISO/IEC 17043, ISO 13528 | Referencia externa |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| `F-PSEA-04` | Informe final (usa criterios de este procedimiento) | Referencia |
| `F-PSEA-13C` | Resultados de homogeneidad (aplican criterios de este procedimiento) | Referencia |
| `F-PSEA-13D` | Resultados de estabilidad (aplican criterios de este procedimiento) | Referencia |
| `P-PSEA-02` a `P-PSEA-05` | Procedimientos por analito que citan este procedimiento | Referencia |

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `P-PSEA-02` a `P-PSEA-05` | Procedimientos por analito que citan este procedimiento | Obligatorio |
| `I-PSEA-18` | Instructivo que aplica estos criterios en pt_app | Obligatorio |
| `P-PSEA-07` | Generacion del informe que usa estos criterios | Obligatorio |
| `P-PSEA-23` | Flujo tecnico que usa estos criterios | Obligatorio |
| `DG-PSEA-03` | Aplicativo que implementa estos criterios | Obligatorio |

---

## Limites y riesgos

#### Limites de alcance

- No es un instructivo de uso de `pt_app` (eso es `I-PSEA-18`).
- No es un procedimiento de planificacion de ronda (eso es `P-PSEA-09`).
- No define contenido del informe final (eso es `P-PSEA-07` y `F-PSEA-04`).
- No es un procedimiento de preparacion del item (eso es `P-PSEA-10`).
- No es un procedimiento de gestion operativa (eso es `P-PSEA-08`, `P-PSEA-16`, etc.).

#### Riesgos de interpretacion

- **Confundir con I-PSEA-18:** `I-PSEA-18` explica como usar la interfaz; `P-PSEA-06` define que calcular y por que.
- **Duplicar en procedimientos por gas:** `P-PSEA-02` a `P-PSEA-05` deben citar, no replicar, este procedimiento.
- **Omitir H/E como insumo:** La evaluacion de H/E es un insumo del diseno estadistico; no debe decirse que no aplica.
- **Cerrar prematuramente criterios:** Los criterios deben ser lo suficientemente estables para citarse, pero abiertos a actualizacion metrologica.

---

## Criterio minimo de elaboracion

El procedimiento define con precision: valor asignado, `sigma_pt`, incertidumbre, outliers, criterios de desempeno, reglas de decision y tratamiento de H/E como insumo, siendo citable por procedimientos por analito sin duplicacion.
