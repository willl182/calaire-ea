# Ficha Resumen: P-PSEA-14

## Identificacion

| Campo | Valor |
|---|---|
| **Codigo** | `P-PSEA-14` |
| **Nombre decidido** | Colusion y falsificacion |
| **Tipo documental** | Procedimiento |
| **Estado** | Mantener / Actualizar |
| **Prioridad** | Media-alta |
| **Clase de ficha** | Ficha activa |

---

## Proposito y rol

### Proposito operativo

Gobierna las medidas preventivas y los criterios de deteccion de colusion y falsificacion en el PEA. Incluye controles en el plan de ronda, analisis estadistico de patrones sospechosos, y conexion con procedimientos de trabajo no conforme, confidencialidad y control de valores sensibles cuando se detectan indicios.

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
- [x] `pt_app`
- [ ] Ambos
- [ ] Ninguno

La deteccion puede involucrar ambos aplicativos: `calaire-app` para patrones de participacion, `pt_app` para analisis estadistico.

---

## Flujo de datos

#### Entradas principales

| Codigo / fuente | Descripcion | Rol en el flujo |
|---|---|---|
| `F-PSEA-05` | Plan de ronda (medidas preventivas) | Referencia |
| `F-PSEA-08` | Datos reportados (analisis de patrones) | Insumo |
| `F-PSEA-12` | Dataset consolidado (analisis estadistico) | Insumo |
| `P-PSEA-07` | Criterio estadistico (deteccion de outliers) | Referencia |

#### Salidas principales

| Codigo / destino | Descripcion | Rol en el flujo |
|---|---|---|
| `P-PSEA-15` | Trabajo no conforme / NC / CAPA | Referencia |
| `P-PSEA-16` | Control de valores sensibles | Referencia |
| `P-PSEA-19` | Confidencialidad operativa | Referencia |

---

## Relaciones documentales

#### Documentos relacionados

| Codigo | Relacion | Tipo de vinculo |
|---|---|---|
| `P-PSEA-15` | Si deriva en TNC/NC/CAPA | Obligatorio |
| `P-PSEA-16` | Control de valores sensibles afectados | Obligatorio |
| `P-PSEA-19` | Confidencialidad comprometida | Obligatorio |
| `F-PSEA-05` | Plan de ronda con medidas preventivas | Obligatorio |
| `P-PSEA-07` | Criterio estadistico para deteccion | Referencia |

---

## Limites y riesgos

#### Limites de alcance

- No es el procedimiento de TNC/NC/CAPA (eso es `P-PSEA-15`); conecta con el cuando aplica.
- No es el procedimiento de control de valores sensibles (eso es `P-PSEA-16`).
- No es un procedimiento de auditoria (eso esta fuera del alcance PEA).
- No define criterios estadisticos (eso es `P-PSEA-07`); aplica los criterios para deteccion.

#### Riesgos de interpretacion

- **Confundir con P-PSEA-15:** `P-PSEA-15` gobierna TNC/NC/CAPA; `P-PSEA-14` gobierna prevencion/deteccion de colusion.
- **Omitir medidas preventivas:** Debe incluir medidas preventivas en el plan de ronda (`F-PSEA-05`).
- **Omitir conexion con P-PSEA-16:** La colusion afecta valores sensibles; debe conectar con `P-PSEA-16`.
- **Incluir sanciones institucionales:** Las sanciones pueden exceder el alcance del PEA; este procedimiento se enfoca en deteccion y control operativo.

---

## Criterio minimo de elaboracion

El procedimiento define medidas preventivas en ronda, criterios de deteccion estadistica y operativa, y conexion con `P-PSEA-15`, `P-PSEA-16` y `P-PSEA-19`, sin duplicar TNC/NC/CAPA ni confidencialidad.
